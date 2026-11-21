-- Lookup used by the dedupe transform when the partition cache is cold.
-- TODO(ingest/P1): add a covering index for the lookup key
SELECT partition_id, record_key, record_hash
FROM kelp_meta.dedupe_lookup
WHERE partition_id = :partition_id
  AND record_key = ANY(:keys);
