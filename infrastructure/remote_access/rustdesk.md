<!-- Reality Block
last_update: 2026-03-17
status: draft
scope:
  summary: "RustDesk Betrieb & Troubleshooting (Homelab)."
  in_scope:
    - ports
    - container setup notes
    - troubleshooting checklist
  out_of_scope:
    - exposing services to the public internet
    - secrets/keys
notes:
  - "Quelle: Proxmox Setup (VM101) + Proxmox Erweiterte Anleitung (RustDesk Sektion)."
-->

# RustDesk (Homelab)

## Ports & Dienste

RustDesk benötigt typischerweise:
- TCP `21115–21119` (Client Kommunikation)
- UDP `21116`
- `hbbs` = Broker, `hbbr` = Relay

## Logs / Checks

```bash
ss -tulpn | grep -E '21115|21116|21117|21118|21119'
docker logs hbbr
docker logs hbbs
```

## Keys

```bash
cat /opt/rustdesk/data/id_ed25519.pub
```

## NAT Loopback (falls nötig)

Wenn dein Router NAT‑Loopback blockiert, kann ein lokales DNS/Hosts Mapping helfen.

## Neuer Laptop / neues Gerät ins Setup integrieren

Der RustDesk‑Relay läuft auf **VM101 (management)** und ist unter der **Tailscale‑IP `100.124.9.7`** erreichbar. Diese Adresse ist **nur aus dem Tailnet** erreichbar – nicht aus dem normalen Internet oder über die FritzBox.

**Ursache „kann nicht mit dem Netzwerk verbinden“:** Wenn du auf dem neuen Laptop nur RustDesk installiert und Relay `100.124.9.7` + Port `21115` + Key eingetragen hast, aber **Tailscale auf dem Laptop nicht installiert bzw. nicht im gleichen Tailnet** bist, kann der Laptop diese IP nicht erreichen. **Die FritzBox ist dabei in der Regel nicht schuld** – der Traffic soll ja über Tailscale laufen, nicht über deinen Router.

**Vorgehen:**

1. **Tailscale auf dem neuen Laptop installieren** (gleicher Tailscale‑Account wie VM101/VM105).
   - Windows: https://tailscale.com/download/windows  
   - Nach dem Login erscheint der Laptop im Admin‑Panel und bekommt eine `100.x.x.x` Adresse.
2. **Verbindung prüfen:** `tailscale ping 100.124.9.7` (oder von Windows aus: „Tailscale“ im Startmenü → Status prüfen).
3. **RustDesk** auf dem Laptop: ID/Relay `100.124.9.7`, Port `21115`, Key wie auf VM101 (`cat /opt/rustdesk/data/id_ed25519.pub`). Danach sollte die Verbindung zum Relay klappen.

**Fazit:** Zuerst Tailscale auf dem neuen Gerät, dann RustDesk‑Relay. Ohne Tailscale ist `100.124.9.7` für den Laptop nicht erreichbar.

