<!-- Reality Block
last_update: 2026-01-12
status: stable
scope:
  summary: "Safe performance optimizations for DGX Spark (GB10 SoC)."
  in_scope:
    - CPU governor
    - GPU persistence
    - network tuning
    - IO scheduler
  out_of_scope:
    - power-limits
    - MPS
    - exclusive process mode
notes:
  - "Optimizations verified for unified memory architecture."
-->

# DGX Spark (GB10) – Performance Optimizations

The GB10 chip is a Unified Memory SoC (CPU+GPU), not a discrete GPU.
Therefore only optimizations compatible with UMA are applied.

---

## Applied Optimizations

### 1. GPU Persistence Mode

```bash
sudo nvidia-smi -pm 1
```

### 2. CPU Governor

```bash
sudo cpupower frequency-set -g performance
```

### 3. Kernel Network Optimizations

```text
net.core.somaxconn=4096
net.ipv4.tcp_fastopen=3
vm.swappiness=10
```

### 4. IO Scheduler
Device: `nvme0n1`

```bash
echo deadline | sudo tee /sys/block/nvme0n1/queue/scheduler
```

---

## Not Applied (unsafe or irrelevant for GB10)
- Power limits (`nvidia-smi -pl`)  
- MPS  
- Exclusive Process Mode  
- max_map_count tweaks  
- Large HugePages  

---

## Monitoring Tools
- NVIDIA Spark Dashboard  
- `watch nvidia-smi`  
- `nvidia-smi dmon -s pucvmet`  

---

## Copy/Paste: Safe Optimization Script (GB10)

> Hinweis: Dieses Script ist **softwareseitig** (keine Power-Limits/Voltage Tweaks).  
> Bei IO-Scheduler bitte **verfügbare Scheduler prüfen** (GB10/DGX OS nutzt oft `mq-deadline` statt `deadline`).

```bash
#!/usr/bin/env bash
set -euo pipefail

if [ "${EUID}" -ne 0 ]; then
  echo "Bitte mit sudo ausführen: sudo $0"
  exit 1
fi

echo "[1/4] GPU Persistence Mode"
nvidia-smi -pm 1 || true

echo "[2/4] CPU governor = performance (falls verfügbar)"
if ! command -v cpupower >/dev/null 2>&1; then
  apt update -qq
  apt install -y linux-tools-common "linux-tools-$(uname -r)" || true
fi
cpupower frequency-set -g performance || true

echo "[3/4] sysctl tuning (konservativ für UMA)"
cat > /etc/sysctl.d/99-spark-llm.conf <<'EOF'
net.core.somaxconn=4096
net.ipv4.tcp_fastopen=3
vm.swappiness=10
EOF
sysctl --system >/dev/null 2>&1 || true

echo "[4/4] IO scheduler (optional) – prüfe verfügbare scheduler pro device"
for dev in $(lsblk -d -o NAME | grep -E '^nvme'); do
  echo "Device: $dev"
  echo "Available: $(cat /sys/block/$dev/queue/scheduler)"
  echo "Setze z.B.: echo mq-deadline | sudo tee /sys/block/$dev/queue/scheduler"
done

echo "Done."
```

## Copy/Paste: Monitoring Script (CLI, optional)

> Das offizielle NVIDIA/DGX Dashboard bleibt die Primärquelle; dieses Script ist nur eine schnelle CLI‑Checkliste.

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "[GPU]"
nvidia-smi --query-gpu=name,temperature.gpu,utilization.gpu,utilization.memory,memory.used,memory.total,power.draw \
  --format=csv,noheader,nounits || true
echo

echo "[GPU Persistence]"
nvidia-smi -q | grep -m1 "Persistence Mode" || true
echo

echo "[CPU governor]"
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor 2>/dev/null || true
echo

echo "[sysctl]"
echo "somaxconn: $(sysctl -n net.core.somaxconn 2>/dev/null || true)"
echo "tcp_fastopen: $(sysctl -n net.ipv4.tcp_fastopen 2>/dev/null || true)"
echo "swappiness: $(sysctl -n vm.swappiness 2>/dev/null || true)"
echo

echo "[IO schedulers]"
for dev in $(lsblk -d -o NAME | grep -E '^nvme'); do
  echo "$dev: $(cat /sys/block/$dev/queue/scheduler 2>/dev/null || true)"
done
```

## Copy/Paste: Rollback (konservativ)

```bash
#!/usr/bin/env bash
set -euo pipefail

if [ "${EUID}" -ne 0 ]; then
  echo "Bitte mit sudo ausführen: sudo $0"
  exit 1
fi

cpupower frequency-set -g ondemand 2>/dev/null || true
rm -f /etc/sysctl.d/99-spark-llm.conf
sysctl --system >/dev/null 2>&1 || true
echo "Rollback done. Reboot optional."
```


