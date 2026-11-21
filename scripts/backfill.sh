#!/usr/bin/env bash
set -euo pipefail

# TODO(ingest/P2): parallelise the backfill loop
for day in $(seq 1 30); do
  kelp configs/pipeline.yaml --dry-run
done
