#!/usr/bin/env python3
"""Add bindings with placeholders to clawdbot-personal config."""
import json
import sys

config_path = "/home/user/.clawdbot-personal/clawdbot.json"

with open(config_path) as f:
    cfg = json.load(f)

cfg["bindings"] = [
    {"agentId": "heiko", "match": {"channel": "signal", "peer": {"kind": "direct", "id": "REPLACE_HEIKO_SIGNAL"}}},
    {"agentId": "noah", "match": {"channel": "signal", "peer": {"kind": "direct", "id": "REPLACE_NOAH_SIGNAL"}}},
    {"agentId": "flora", "match": {"channel": "signal", "peer": {"kind": "direct", "id": "REPLACE_FLORA_SIGNAL"}}},
    {"agentId": "familie", "match": {"channel": "signal", "peer": {"kind": "group", "id": "REPLACE_FAMILIE_GROUP"}}},
    {"agentId": "main", "match": {"channel": "signal"}},
]

with open(config_path, "w") as f:
    json.dump(cfg, f, indent=2)

print("Bindings added. Replace REPLACE_* with real Signal E.164 or group IDs.")
