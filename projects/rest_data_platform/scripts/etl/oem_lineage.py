"""Nameplate OEM vs current group — for MaStR↔4C matching.

Areva Wind → Adwen → Siemens Gamesa (4C farm-link OEM for tid 2).
REpower → Senvion (not Siemens Gamesa).
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_NON_ALNUM = re.compile(r"[^a-z0-9]+")

# Nameplate / MaStR label → current group key
OEM_GROUP: dict[str, str] = {
    "areva": "siemens gamesa",
    "areva wind": "siemens gamesa",
    "areva gmbh": "siemens gamesa",
    "adwen": "siemens gamesa",
    "siemens gamesa": "siemens gamesa",
    "siemens gamesa renewable energy": "siemens gamesa",
    "repower": "senvion",
    "repower systems": "senvion",
    "repower systems se": "senvion",
    "senvion": "senvion",
    "senvion gmbh": "senvion",
}

OEM_GROUP_LABEL: dict[str, str] = {
    "siemens gamesa": "Siemens Gamesa",
    "senvion": "Senvion",
}


def fold(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(str(value).casefold().split())


def compact(value: str | None) -> str:
    return _NON_ALNUM.sub("", fold(value))


def oem_group_key(name: str | None) -> str:
    folded = fold(name)
    if not folded:
        return ""
    if folded in OEM_GROUP:
        return OEM_GROUP[folded]
    for prefix, group in OEM_GROUP.items():
        if folded.startswith(prefix):
            return group
    return folded


def oem_group_label(name: str | None) -> str | None:
    key = oem_group_key(name)
    if not key:
        return None
    return OEM_GROUP_LABEL.get(key, name.strip() if name else None)


@dataclass(frozen=True)
class FarmModel:
    turbine_model_id: str
    oem: str
    model: str
    rotor_diameter_m: float | None
    oem_group: str | None


def _rotor_hits(unit_rotor: float, models: list[FarmModel]) -> list[FarmModel]:
    return [
        m
        for m in models
        if m.rotor_diameter_m is not None
        and abs(m.rotor_diameter_m - unit_rotor) <= 1.0
    ]


def _type_hits(type_name: str, models: list[FarmModel]) -> list[FarmModel]:
    needle = compact(type_name)
    if not needle:
        return []
    hits: list[FarmModel] = []
    for model in models:
        hay = compact(model.model)
        if hay and (hay in needle or needle in hay):
            hits.append(model)
            continue
        if "m5000" in needle and "m5000" in hay:
            hits.append(model)
            continue
        if needle.endswith("5m") and hay in {"5m", "repower5m"}:
            hits.append(model)
    return hits


def _oem_hits(manufacturer: str, models: list[FarmModel]) -> list[FarmModel]:
    unit_group = oem_group_key(manufacturer)
    if not unit_group:
        return []
    hits: list[FarmModel] = []
    for model in models:
        model_group = oem_group_key(model.oem_group) or oem_group_key(model.oem)
        if model_group == unit_group:
            hits.append(model)
    return hits


def match_farm_model(
    *,
    manufacturer: str | None,
    type_designation: str | None,
    rotor_diameter_m: float | None,
    models: list[FarmModel],
) -> str | None:
    """Return turbine_model_id if uniquely determined. Never guess."""
    if not models:
        return None
    if len(models) == 1:
        return models[0].turbine_model_id

    if rotor_diameter_m is not None:
        hits = _rotor_hits(rotor_diameter_m, models)
        if len(hits) == 1:
            return hits[0].turbine_model_id
        if len(hits) > 1:
            typed = _type_hits(type_designation or "", hits)
            if len(typed) == 1:
                return typed[0].turbine_model_id
            grouped = _oem_hits(manufacturer or "", hits)
            if len(grouped) == 1:
                return grouped[0].turbine_model_id
            return None

    typed = _type_hits(type_designation or "", models)
    if len(typed) == 1:
        return typed[0].turbine_model_id

    grouped = _oem_hits(manufacturer or "", models)
    if len(grouped) == 1:
        return grouped[0].turbine_model_id
    return None
