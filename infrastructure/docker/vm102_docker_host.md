<!-- Reality Block
last_update: 2026-01-13
status: draft
scope:
  summary: "VM102 (docker-apps): Docker Host, Remote Admin, typische Services/Ports und sichere Hinweise."
  in_scope:
    - base install
    - remote docker API (doc + risk note)
    - troubleshooting commands
  out_of_scope:
    - full docker-compose stacks
    - secrets (passwords, auth keys)
notes:
  - "Quelle: konsolidiert aus Proxmox Masterdocs (VM102 Abschnitt)."
-->

# VM102 – Docker Host (docker-apps)

## Zweck
VM102 ist dein zentraler Docker‑Host für Apps/Downloader/Utilities.

## Basisinstallation (Debian)

```bash
apt update && apt install -y docker.io docker-compose-plugin
systemctl enable docker
```

## Remote Docker API (Achtung)

In den Proxmox‑Docs ist ein Setup mit `tcp://0.0.0.0:2375` beschrieben. Das ist **ohne TLS unsicher**, wenn es außerhalb eines privaten Netzes erreichbar ist.

Empfehlung (minimal sicher):
- Nur nutzen, wenn VM102 **nicht** öffentlich erreichbar ist.
- Exponierung nur über **Tailscale** (oder Firewall nur für VM105).

Beispiel (wie dokumentiert):

```bash
mkdir -p /etc/systemd/system/docker.service.d
cat > /etc/systemd/system/docker.service.d/override.conf << 'EOF'
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://0.0.0.0:2375
EOF

systemctl daemon-reload
systemctl restart docker
```

## Troubleshooting – Quick Commands

```bash
docker network ls
docker network inspect bridge
docker network prune
docker compose down && docker compose up -d
docker logs <container>
```


