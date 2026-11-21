# Kelpstream Maintenance Backlog

This document tracks the debt markers that live in the Kelpstream source tree.
It is regenerated on every release branch and reviewed in the release readiness
meeting before the branch is tagged.

## Open Items

| Location | Team | Priority | Item |
| --- | --- | --- | --- |
| `kelpstream/io/csv_reader.py:88` | ingest | P2 | drop the pandas fallback once the parquet path is stable |
| `kelpstream/runtime/worker_pool.py:41` | runtime | P1 | size the pool from the pipeline config |
| `kelpstream/transforms/schema_map.py:12` | transform | P3 | document the cast matrix |

## Priority Summary

- P1: 1
- P2: 1
- P3: 1

## Release Delta

- Closed since main: 0
- New since main: 0

## How to use this backlog

Pick the highest priority row owned by your team, open a pull request against the
release branch, and delete the marker from the source file in the same change.
Rows that can no longer be reproduced should be closed with a short note on the
pull request so that the next release delta stays accurate.
