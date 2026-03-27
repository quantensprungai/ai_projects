// Regeneriert code/astra-imc-platform/.../20260327120000_imc_astra_v1.sql aus reference/imc/IMC_Schema_v1.sql (ab „1. ENUM-TYPEN“).
// Ausführen vom Repo-Root ai-projects: node projects/rest_data_platform/scripts/build_imc_migration.mjs
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "../../..");
const ref = path.join(root, "projects/rest_data_platform/reference/imc/IMC_Schema_v1.sql");
const out = path.join(
  root,
  "code/astra-imc-platform/apps/web/supabase/migrations/20260327120000_imc_astra_v1.sql",
);

const refText = fs.readFileSync(ref, "utf8");
const marker = "-- ============================================================================\n-- 1. ENUM-TYPEN";
const idx = refText.indexOf(marker);
if (idx < 0) throw new Error("marker not found");
const fromEnums = refText.slice(idx);

const header = `-- ============================================================================
-- Migration: IMC / ASTRA Domain Schema v1 (public)
-- Spiegel der kanonischen Referenz (Doku-Repo):
--   projects/rest_data_platform/reference/imc/IMC_Schema_v1.sql
-- Bei inhaltlichen Änderungen: zuerst Referenz pflegen, dann Migration angleichen.
-- 2026-03-28: Präfix imc_* für Tabellen/Views/ENUMs; organisations → imc_orgs.
-- ============================================================================

-- ============================================================================
-- 0. EXTENSIONS (Supabase: Schema extensions)
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA extensions;
CREATE EXTENSION IF NOT EXISTS btree_gist WITH SCHEMA extensions;

`;

fs.writeFileSync(out, header + fromEnums, "utf8");
console.log("Wrote", out);
