# Operations runbook

## Landing zone

Raw payloads arrive in `s3://kelp-landing/<pipeline>/<date>/`. The writer emits one
file per partition and the reader picks files up in lexicographic order.

## Backfills

Backfills are started with `scripts/backfill.sh` and always write to a staging
prefix first. The staging prefix is cleaned by the nightly lifecycle rule.

- TODO(sink/P2): document the staging bucket layout

## Escalation

Page the platform on-call when a pipeline misses two consecutive checkpoint
windows. Include the pipeline name and the last committed offset.
