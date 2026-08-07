"""IMC / ASTRA ETL — stabile source_id UUIDs aus imc_data_sources_seed_v1."""

from __future__ import annotations

import os
from pathlib import Path

# 4C Primary
SOURCE_4C_WINDFARM = "a1000001-0001-4001-8001-000000000001"
SOURCE_4C_POP = "a1000001-0001-4001-8001-000000000002"
SOURCE_4C_VPI = "a1000001-0001-4001-8001-000000000003"
SOURCE_4C_TRANSMISSION = "a1000001-0001-4001-8001-000000000004"
SOURCE_4C_INTERCONNECTORS = "a1000001-0001-4001-8001-000000000005"
SOURCE_4C_TURBINE = "a1000001-0001-4001-8001-000000000008"

# Open Data
SOURCE_MASTR = "a1000001-0002-4001-8001-000000000010"
SOURCE_ERA5 = "a1000001-0002-4001-8001-000000000012"
SOURCE_NATURA2000 = "a1000001-0002-4001-8001-000000000013"

# Pilot
SOURCE_ALPHA_VENTUS = "a1000001-0004-4001-8001-000000000032"

DEFAULT_4C_WINDFARM_FILE = (
    "4COffshore - Offshore Wind Farm Database (01-Nov-23 to 25-Oct-24)_SAMPLE.xlsx"
)


FOURC_SOURCE_PROFILES: dict[str, dict[str, object]] = {
    "pop": {
        "source_id": SOURCE_4C_POP,
        "default_header_row": 2,
        "sheet_header_rows": {
            "POP": 2,
            "LCOE": 2,
            "Corporate PPAs": 3,
        },
        "include_sheets": ["POP", "LCOE", "Corporate PPAs"],
        "key_fields": ["WindfarmId", "StakeholderId", "Name"],
    },
    "windfarm": {
        "source_id": SOURCE_4C_WINDFARM,
        "default_header_row": 1,
        "include_sheets": [
            "Windfarm Project Details",
            "Windfarm Supply Chain",
            "Windfarm Events",
            "Platform Type",
        ],
        "key_fields": [
            "WindfarmId",
            "WindfarmStakeholderId",
            "WindfarmEventId",
            "PlatformID",
            "WindfarmID",
            "Name",
        ],
    },
    "turbine": {
        "source_id": SOURCE_4C_TURBINE,
        "default_header_row": 1,
        "include_sheets": ["Offshore Wind Turbine Specs", "Turbine on Windfarms"],
        "key_fields": ["TurbineId", "WindfarmId", "WindfarmStakeholderId", "TurbineName"],
    },
    "vpi": {
        "source_id": SOURCE_4C_VPI,
        "default_header_row": 1,
        "include_sheets": [
            "Vessel Specs",
            "Vessel Events",
            "Vessel Contracts",
            "Helicopter Contracts",
            "Construct&O&M Port Stakeholders",
            "Construction Port Stakeholders",
            "Turbine Measurements",
            "Fixed Foundation Measurements",
            "Floating Foundation Measurement",
            "Dedicated Platform Measurements",
            "Shared Platform Measurements",
        ],
        "key_fields": [
            "VesselId",
            "VesselEventId",
            "WindfarmStakeholderId",
            "StakeholderId",
            "RecordID",
            "PortID",
            "FoundationId",
            "SubstationID",
            "ConverterID",
            "ProjectId",
            "WindfarmId",
            "Name",
        ],
    },
    "transmission": {
        "source_id": SOURCE_4C_TRANSMISSION,
        "default_header_row": 1,
        "key_fields": ["WindfarmId", "WindfarmStakeholderId", "WindfarmEventId", "PlatformID", "ConverterID", "VesselId", "Name"],
    },
    "interconnectors": {
        "source_id": SOURCE_4C_INTERCONNECTORS,
        "default_header_row": 1,
        "key_fields": ["PowerCableId", "PowerCableEventId", "PowerCableStakeholderId", "VesselId", "VesselEventId", "Name"],
    },
}

FOURC_STATUS_TO_LIFECYCLE: dict[str, str] = {
    # Common / short labels
    "operational": "operational",
    "under construction": "under_construction",
    "consented": "consented",
    "concept/early planning": "early_stage",
    "planning": "planning",
    "pre-construction": "pre_construction",
    "decommissioning": "decommissioning",
    "decommissioned": "decommissioned",
    "cancelled": "cancelled",
    "on hold": "on_hold",
    "dormant": "on_hold",
    # Actual 4C WindfarmStatus labels (OWF export)
    "fully commissioned": "operational",
    "partial generation/under construction": "under_construction",
    "development zone": "planning",
    "consent application submitted": "planning",
    "consent authorised": "consented",
}


def get_database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("DATABASE_URL fehlt — siehe .env.example")
    return url


def get_sample_dir() -> Path:
    raw = os.environ.get("FOURC_SAMPLE_DIR")
    if not raw:
        raise RuntimeError("FOURC_SAMPLE_DIR fehlt — siehe .env.example")
    path = Path(raw)
    if not path.is_dir():
        raise FileNotFoundError(f"4C-Sample-Ordner nicht gefunden: {path}")
    return path


def get_mastr_xml_dir() -> Path | None:
    raw = os.environ.get("MASTR_XML_DIR")
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_dir() else None


def get_etl_account_id() -> str:
    account_id = os.environ.get("IMC_ETL_ACCOUNT_ID")
    if not account_id:
        raise RuntimeError(
            "IMC_ETL_ACCOUNT_ID fehlt — UUID eines Team/Personal-Accounts aus public.accounts"
        )
    return account_id
