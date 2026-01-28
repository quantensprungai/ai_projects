from __future__ import annotations

import json
import subprocess
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests
import streamlit as st


APP_TITLE = "Spark Model Switcher"
WINDOWS_SSH_PATH = r"C:\Windows\System32\OpenSSH\ssh.exe"


@dataclass(frozen=True)
class SparkConfig:
    host: str
    ssh_user: str = "sparkuser"
    ssh_port: int = 2222
    ssh_identity_file: str | None = None
    ssh_extra_args: list[str] | None = None


def _workspace_config_path() -> Path:
    return Path(__file__).resolve().parent / "config.json"


def _example_config_path() -> Path:
    return Path(__file__).resolve().parent / "config.example.json"


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_config() -> dict[str, Any]:
    cfg_path = _workspace_config_path()
    if cfg_path.exists():
        return _load_json(cfg_path)
    return _load_json(_example_config_path())


def build_ssh_base_args(spark: SparkConfig) -> list[str]:
    ssh_bin = WINDOWS_SSH_PATH if Path(WINDOWS_SSH_PATH).exists() else "ssh"
    args = [ssh_bin, "-p", str(spark.ssh_port)]
    if spark.ssh_identity_file:
        args += ["-i", spark.ssh_identity_file]
    if spark.ssh_extra_args:
        args += list(spark.ssh_extra_args)
    args.append(f"{spark.ssh_user}@{spark.host}")
    return args


def run_ssh(
    spark: SparkConfig,
    remote_cmd: str,
    timeout_s: int = 60,
) -> tuple[int, str]:
    base = build_ssh_base_args(spark)
    # IMPORTANT (Windows/OpenSSH): arguments after host are concatenated into a single
    # remote command string. If we pass ["bash","-lc", remote_cmd] here, the "-lc"
    # command string gets split and the remote ends up running just "curl" (no args).
    #
    # So we build ONE remote command string and quote the bash -lc payload.
    def sh_single_quote(s: str) -> str:
        # POSIX-safe single-quote escaping: ' -> '\''.
        return "'" + s.replace("'", "'\\''") + "'"

    remote_line = f"bash -lc {sh_single_quote(remote_cmd)}"
    cmd = base + [remote_line]
    try:
        cp = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            check=False,
        )
        out = (cp.stdout or "") + (cp.stderr or "")
        return cp.returncode, out.strip()
    except FileNotFoundError:
        return 127, "ssh wurde nicht gefunden. Installiere OpenSSH oder stelle sicher, dass ssh im PATH ist."
    except subprocess.TimeoutExpired:
        return 124, f"Timeout nach {timeout_s}s: {remote_cmd}"


def get_models_via_ssh(spark: SparkConfig, port: int) -> tuple[bool, str]:
    code, out = run_ssh(spark, f"curl -s http://127.0.0.1:{port}/v1/models", timeout_s=10)
    if code != 0 or not out:
        return False, out or f"curl exit={code}"
    return True, out


def get_health_via_ssh(spark: SparkConfig, port: int) -> tuple[bool, str]:
    code, out = run_ssh(
        spark,
        f"curl -s -o /dev/null -w '%{{http_code}}' http://127.0.0.1:{port}/health",
        timeout_s=10,
    )
    if code != 0:
        return False, out or f"curl exit={code}"
    return out.strip() == "200", out.strip()


def normalize_spark_config(cfg: dict[str, Any]) -> SparkConfig:
    spark = cfg.get("spark") or {}
    return SparkConfig(
        host=str(spark.get("host") or "").strip(),
        ssh_user=str(spark.get("ssh_user") or "sparkuser"),
        ssh_port=int(spark.get("ssh_port") or 2222),
        ssh_identity_file=str(spark.get("ssh_identity_file") or "").strip() or None,
        ssh_extra_args=list(spark.get("ssh_extra_args") or []),
    )


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)

    cfg = load_config()
    spark = normalize_spark_config(cfg)
    ports = list((cfg.get("status_checks") or {}).get("ports") or [30001, 30000])
    actions: list[dict[str, Any]] = list(cfg.get("actions") or [])

    with st.expander("Konfiguration", expanded=False):
        st.write(
            "Aktive Konfig kommt aus `infrastructure/spark/tools/spark_model_switcher/config.json` (falls vorhanden), "
            "sonst aus `config.example.json`."
        )
        st.json(cfg)
        st.write("Tipp: kopiere `config.example.json` → `config.json` und passe an.")

    if not spark.host:
        st.error("Bitte `spark.host` in `config.json` setzen (z. B. 100.x oder MagicDNS).")
        return

    col_a, col_b = st.columns([2, 3])

    with col_a:
        st.subheader("Status")
        if st.button("Status aktualisieren"):
            st.session_state["refresh_ts"] = time.time()

        for p in ports:
            ok, code = get_health_via_ssh(spark, int(p))
            st.write(f"- Port `{p}` /health: **{code}**" if ok else f"- Port `{p}` /health: **{code}** (nicht ready)")

        st.divider()
        st.subheader("Served Models (live)")
        for p in ports:
            ok, body = get_models_via_ssh(spark, int(p))
            if ok:
                st.code(body, language="json")
            else:
                st.warning(f"Port {p}: keine Model-Liste ({body})")

    with col_b:
        st.subheader("Modelle auswählen (Switch/Start)")
        st.caption(
            "Diese Buttons rufen remote Switch-Skripte auf Spark auf. Große Modelle werden dabei typischerweise "
            "gegenseitig gestoppt (Memory/KV-Cache)."
        )

        if not actions:
            st.info("Keine `actions` in config. Ergänze `config.json`.")
        else:
            category_order = {
                "Allround": 10,
                "Coding": 20,
                "Long-context": 30,
                "Uncensored-ish": 40,
                "Maintenance": 90,
                "Other": 99,
            }

            def action_sort_key(a: dict[str, Any]) -> tuple[int, int, str]:
                cat = str(a.get("category") or "Other").strip() or "Other"
                order = int(a.get("order") or 999)
                label = str(a.get("label") or a.get("id") or "").strip().lower()
                return category_order.get(cat, 99), order, label

            actions_sorted = sorted(actions, key=action_sort_key)
            grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for a in actions_sorted:
                cat = str(a.get("category") or "Other").strip() or "Other"
                grouped[cat].append(a)

            cats = sorted(grouped.keys(), key=lambda c: (category_order.get(c, 99), c.lower()))
            for cat in cats:
                st.markdown(f"#### {cat}")
                for a in grouped[cat]:
                    model_id = str(a.get("id") or "").strip()
                    label = str(a.get("label") or model_id).strip()
                    typ = str(a.get("type") or "script").strip()
                    remote_path = str(a.get("remote_path") or "").strip()
                    desc = str(a.get("description") or "").strip()
                    slot = str(a.get("slot") or "").strip().lower()

                    slot_hint = ""
                    if slot in {"primary", "30001"}:
                        slot_hint = "Primary (30001)"
                    elif slot in {"secondary", "30000"}:
                        slot_hint = "Secondary (30000)"

                    with st.container(border=True):
                        title = f"**{label}**"
                        if slot_hint:
                            title += f" — _{slot_hint}_"
                        st.write(title)
                        if model_id:
                            st.caption(f"`{model_id}`")
                        if desc:
                            st.caption(desc)

                        cols = st.columns([1, 4])
                        with cols[0]:
                            clicked = st.button("Start/Switch", key=f"run:{model_id}")
                        with cols[1]:
                            if typ != "script":
                                st.warning(f"Unbekannter action type: {typ}")
                            elif not remote_path:
                                st.warning("Kein `remote_path` gesetzt (Script-Pfad fehlt).")
                            else:
                                st.code(remote_path)

                        if clicked:
                            if typ == "script" and remote_path:
                                st.write("Ausführung…")
                                rc, out = run_ssh(spark, f"{remote_path}", timeout_s=600)
                                st.write(f"Exit Code: `{rc}`")
                                if out:
                                    st.code(out)
                                if rc == 0:
                                    st.success("Command ausgeführt. Aktualisiere den Status, sobald das Modell fertig geladen ist.")

        st.divider()
        st.subheader("Custom Command (advanced)")
        custom = st.text_input(
            "Remote bash command",
            value="docker ps --format 'table {{.Names}}\\t{{.Status}}\\t{{.Ports}}'",
        )
        if st.button("Ausführen", key="custom_cmd"):
            rc, out = run_ssh(spark, custom, timeout_s=120)
            st.write(f"Exit Code: `{rc}`")
            st.code(out or "(kein Output)")

        st.divider()
        st.subheader("Maintenance (Open WebUI)")
        st.caption("Optional: repariert kaputte OpenAI-Verbindungen in Open WebUI (z. B. alte Docker-Hostnames).")

        fix_col, restart_col = st.columns([2, 1])

        with fix_col:
            if st.button("Fix: OpenWebUI SGLang-30000 URL (sglang-qwen-uncensored → 172.17.0.1)", key="fix_webui_30000"):
                old = "http://sglang-qwen-uncensored:30000/v1"
                new = "http://172.17.0.1:30000/v1"
                # Replace in all TEXT-ish columns across DB (best-effort).
                # Use docker exec -i + heredoc to avoid Python one-liner syntax issues.
                remote = f"""docker exec -i open-webui python3 - <<'PY'
import sqlite3

db = "/app/backend/data/webui.db"
old = {old!r}
new = {new!r}

con = sqlite3.connect(db)
cur = con.cursor()
cur.execute("select name from sqlite_master where type='table'")
tables = [r[0] for r in cur.fetchall()]

def qident(name: str) -> str:
    # Quote identifiers safely for SQLite: "a""b"
    return '"' + name.replace('"', '""') + '"'

replaced = 0
for t in tables:
    try:
        cur.execute("pragma table_info(%s)" % qident(t))
        cols = [(r[1], (r[2] or "").lower()) for r in cur.fetchall()]
        text_cols = [c for c, ty in cols if ty in ("text", "")]
        for c in text_cols:
            col_q = qident(c)
            tbl_q = qident(t)
            sql = "update %s set %s=replace(%s, ?, ?) where %s like ?" % (tbl_q, col_q, col_q, col_q)
            cur.execute(sql, (old, new, "%" + old + "%"))
            # sqlite rowcount is best-effort; may be -1
            if cur.rowcount and cur.rowcount > 0:
                replaced += cur.rowcount
    except Exception:
        pass

con.commit()
print("replaced_rows", replaced)
print("old", old)
print("new", new)
PY"""
                rc, out = run_ssh(spark, remote, timeout_s=120)
                st.write(f"Exit Code: `{rc}`")
                st.code(out or "(kein Output)")
                if rc == 0:
                    st.success("Fix angewendet. Wenn Open WebUI die Änderung nicht sofort zeigt, klicke 'Restart Open WebUI'.")

        with restart_col:
            if st.button("Restart Open WebUI", key="restart_openwebui"):
                rc, out = run_ssh(spark, "docker restart open-webui", timeout_s=60)
                st.write(f"Exit Code: `{rc}`")
                st.code(out or "(kein Output)")
                if rc == 0:
                    st.success("Open WebUI neu gestartet (kurze Downtime).")

        st.divider()
        st.subheader("Stop / Cleanup (SGLang)")
        st.caption("Hilfsbuttons, um Secondary Slot (30000) oder alle SGLang-Container zu stoppen.")

        stop_col1, stop_col2 = st.columns([1, 2])
        with stop_col1:
            if st.button("Stop Secondary (30000)", key="stop_secondary"):
                rc, out = run_ssh(
                    spark,
                    "/home/sparkuser/ai/scripts/serve/sglang_stop.sh sglang-scout || true",
                    timeout_s=60,
                )
                st.write(f"Exit Code: `{rc}`")
                st.code(out or "(kein Output)")
                if rc == 0:
                    st.success("Secondary Slot Stop ausgeführt.")

        with stop_col2:
            confirm = st.checkbox("Ich weiß: das stoppt auch Port 30001 (Primary).", value=False)
            if st.button("Stop ALL SGLang (beide Slots)", key="stop_all_sglang"):
                if not confirm:
                    st.warning("Bitte Checkbox bestätigen, bevor alle SGLang-Container gestoppt werden.")
                else:
                    rc, out = run_ssh(
                        spark,
                        "/home/sparkuser/ai/scripts/serve/sglang_stop_all.sh",
                        timeout_s=120,
                    )
                    st.write(f"Exit Code: `{rc}`")
                    st.code(out or "(kein Output)")
                    if rc == 0:
                        st.success("Alle SGLang-Container gestoppt.")


if __name__ == "__main__":
    main()

