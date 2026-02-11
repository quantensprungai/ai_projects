# Export Supabase → ArangoDB (Entwurf)

<!--
last_update: 2026-02-10
status: draft
scope:
  summary: "Mapping hd_kg_nodes / hd_kg_edges (Supabase) → ArangoDB Collections für optionales Playbook / Visualisierung."
  in_scope:
    - Collection-Mapping, Property-Mapping
    - Skizze Export-Skript (Batch, Service-Role)
  out_of_scope:
    - ArangoDB-Setup, Deployment
    - NVIDIA txt2kg-Integration (separates Thema)
notes:
  - "Optionaler Weg für Graph-Visualisierung oder GraphRAG; Kern-Pipeline bleibt Supabase."
-->

Optionaler Export des Knowledge Graph aus **Supabase** (hd_kg_nodes, hd_kg_edges) nach **ArangoDB**, z. B. für Playbook-Visualisierung oder GraphRAG. Die **Source of Truth** bleibt Supabase; ArangoDB dient als lesende Kopie.

## 1) Mapping Tabellen → Collections

| Supabase | ArangoDB | Bemerkung |
|----------|----------|-----------|
| **hd_kg_nodes** | Collection `hd_nodes` (oder `kg_nodes`) | Ein Dokument pro Node |
| **hd_kg_edges** | Collection `hd_edges` (Edge-Collection) | Arango Edge: `_from`, `_to` = `hd_nodes/<id>` |

### 1.1 hd_kg_nodes → hd_nodes

| Supabase-Spalte | ArangoDB-Feld | Hinweis |
|-----------------|---------------|---------|
| id | _key oder separates Feld `supabase_id` | _key muss string sein; z. B. `_key = str(uuid)` oder UUID als Attribut, _key = node_key |
| account_id | account_id (string) | UUID als String |
| node_key | node_key (string) | Eindeutig pro Account; gut als _key wenn global eindeutig: z. B. `{account_id}_{node_key}` |
| node_type | node_type (string) | |
| canonical_description | canonical_description (string, optional) | |
| metadata | metadata (object) | 1:1 jsonb → Objekt |
| created_at, updated_at | created_at, updated_at (string ISO) | Optional |

**Empfehlung _key:** `{account_id}_{node_key}` (ersetzt Leerzeichen/Sonderzeichen in node_key falls nötig), damit Edges stabil auf Nodes verweisen können.

### 1.2 hd_kg_edges → hd_edges (Edge-Collection)

ArangoDB Edges haben `_from`, `_to` (müssen `collection/_key` sein).

| Supabase-Spalte | ArangoDB | Hinweis |
|-----------------|----------|---------|
| id | _key (string) oder supabase_id | _key = str(uuid) |
| account_id | account_id | |
| from_node_id | _from | = `"hd_nodes/" + from_node._key` (wobei from_node._key = account_id + "_" + node_key oder Supabase-UUID in hd_nodes gespeichert) |
| to_node_id | _to | = `"hd_nodes/" + to_node._key` |
| relation_type | relation_type | |
| strength | strength | |
| metadata | metadata (object) | |

**Wichtig:** Beim Export zuerst alle Nodes schreiben; dann Edges, wobei `_from`/`_to` die _key der entsprechenden Node-Dokumente in Arango sind. Dazu entweder in Supabase `hd_kg_nodes.id` → Arango `_key` (z. B. _key = str(supabase_id)) verwenden, dann _from = `hd_nodes/<supabase_from_node_id>`, _to = `hd_nodes/<supabase_to_node_id>`.

## 2) Einmaliger vs. inkrementeller Export

- **Einmalig:** Alle hd_kg_nodes und hd_kg_edges eines Accounts (oder aller Accounts) lesen und nach Arango schreiben.
- **Inkrementell:** Nur neue/geänderte Nodes/Edges (z. B. nach updated_at oder über Job-Log). Optional: Tabelle `hd_kg_export_log` mit last_exported_at pro account_id; Export-Job liest nur Zeilen mit updated_at > last_exported_at.

Für den Entwurf reicht **einmaliger Full-Export**; Inkrementell kann später ergänzt werden.

## 3) Skizze Export-Skript

- **Sprache:** Python (oder TypeScript im Repo).
- **Abhängigkeiten:** Supabase Client (service_role), arango (python-arango).
- **Ablauf:**
  1. Supabase: Alle Zeilen aus hd_kg_nodes (filter optional: account_id) abrufen (REST: `GET .../rest/v1/hd_kg_nodes?select=*` mit Pagination falls nötig).
  2. Für jede Node: In ArangoDB `hd_nodes` upserten. _key = str(supabase_id) oder composite key wie oben.
  3. Supabase: Alle Zeilen aus hd_kg_edges abrufen.
  4. Für jede Edge: from_node_id und to_node_id sind UUIDs; in Arango _from = `hd_nodes/<from_node_id>`, _to = `hd_nodes/<to_node_id>` (wenn Nodes mit _key = supabase_id gespeichert wurden). INSERT in Edge-Collection hd_edges.
  5. Optional: Log/Status zurück in Supabase schreiben.

**Pseudocode:**

```text
# Config
SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
ARANGO_URL, ARANGO_USER, ARANGO_PASSWORD, DB_NAME = "hd_kg"
COLL_NODES = "hd_nodes"
COLL_EDGES = "hd_edges"

# 1) Nodes
rows = supabase.table("hd_kg_nodes").select("*").execute()
for r in rows:
    doc = {
        "_key": str(r["id"]),
        "account_id": str(r["account_id"]),
        "node_key": r["node_key"],
        "node_type": r["node_type"],
        "canonical_description": r.get("canonical_description"),
        "metadata": r.get("metadata") or {},
        "created_at": r.get("created_at"),
        "updated_at": r.get("updated_at"),
    }
    arango_db.collection(COLL_NODES).insert(doc, overwrite=True)

# 2) Edges
edges = supabase.table("hd_kg_edges").select("*").execute()
for e in edges:
    edge_doc = {
        "_from": f"{COLL_NODES}/{e['from_node_id']}",
        "_to": f"{COLL_NODES}/{e['to_node_id']}",
        "account_id": str(e["account_id"]),
        "relation_type": e["relation_type"],
        "strength": e.get("strength") or "medium",
        "metadata": e.get("metadata") or {},
    }
    arango_db.collection(COLL_EDGES).insert(edge_doc)
```

- **Pagination:** Supabase Range (Range: 0-999, dann 1000-1999 …) oder Filter mit limit/offset.
- **Idempotenz:** Nodes mit overwrite=True; Edges ggf. vorher prüfen ob (_from, _to, relation_type) schon existiert oder Collection leeren pro Account vor Full-Export.

## 4) Wo einordnen

- **Code-Ort:** z. B. `code/hd_saas_app/apps/web/scripts/export_kg_to_arangodb.py` (nur ausführbar mit Service-Role; nicht von Frontend aufrufbar).
- **Doku:** Dieses Dokument; Verweis in `text2kg_spec.md` (optionaler Export für Visualisierung) und in `current_status_local_dev.md` („Export Supabase → ArangoDB“ als optionaler Schritt).

## 5) Referenzen

- Spec KG: `text2kg_spec.md`
- Implementierung Worker: `text2kg_implementation_sketch.md`
- Schema: `code/hd_saas_app/apps/web/supabase/migrations/20260119165000_hd_knowledge_core.sql`
