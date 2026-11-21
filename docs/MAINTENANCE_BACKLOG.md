# Kelpstream Maintenance Backlog

This document tracks the debt markers that live in the Kelpstream source tree.
It is regenerated on every release branch and reviewed in the release readiness
meeting before the branch is tagged.

## Open Items

| Location | Team | Priority | Item |
| --- | --- | --- | --- |
| `kelpstream/cli.py:25` | cli | P1 | exit non-zero when a pipeline definition fails validation |
| `kelpstream/io/kafka_source.py:22` | ingest | P1 | commit offsets only after the sink acknowledges the batch |
| `kelpstream/io/parquet_reader.py:26` | ingest | P1 | handle truncated parquet footers without aborting the run |
| `kelpstream/runtime/scheduler.py:29` | runtime | P1 | serialize concurrent checkpoint writes for the same pipeline |
| `kelpstream/sinks/snowflake_sink.py:16` | sink | P1 | retry transient upload failures with bounded backoff |
| `kelpstream/transforms/dedupe.py:13` | transform | P1 | keep the newest record when dedupe keys collide |
| `kelpstream/config.py:46` | cli | P2 | reject unknown keys when loading pipeline config |
| `kelpstream/io/checkpoint.py:20` | ingest | P2 | store checkpoint metadata atomically alongside state |
| `kelpstream/io/parquet_writer.py:19` | ingest | P2 | align row-group size with the target file size hint |
| `kelpstream/runtime/metrics.py:22` | runtime | P2 | emit stage-level latency percentiles |
| `kelpstream/runtime/scheduler.py:21` | runtime | P2 | surface backpressure from slow sinks to the source |
| `kelpstream/sinks/s3_sink.py:18` | sink | P2 | multipart upload cleanup on aborted transfers |
| `kelpstream/transforms/dedupe.py:23` | transform | P2 | cache the dedupe lookup per partition |
| `kelpstream/transforms/late_events.py:17` | transform | P2 | count late events per partition in the run summary |
| `kelpstream/transforms/schema_map.py:9` | transform | P2 | report the source column when a cast fails |
| `kelpstream/transforms/window.py:22` | transform | P2 | support late-arriving events with a configurable grace period |
| `kelpstream/cli.py:35` | cli | P3 | print the resolved config path in verbose mode |
| `kelpstream/io/kafka_source.py:17` | ingest | P3 | log the consumer group on rebalance |
| `kelpstream/io/parquet_reader.py:27` | ingest | P3 | expose the reader batch size as an env override |
| `kelpstream/runtime/metrics.py:15` | runtime | P3 | rename the counter helper for clarity |
| `kelpstream/runtime/scheduler.py:11` | runtime | P3 | remove the duplicated interval lookup |
| `kelpstream/sinks/s3_sink.py:22` | sink | P3 | drop the unused content-type helper |
| `kelpstream/tests/test_dedupe.py:17` | transform | P3 | replace the inline sample with a fixture file |
| `kelpstream/tests/test_window.py:16` | transform | P3 | cover the empty-batch branch |

## Priority Summary

- P1: 6
- P2: 10
- P3: 8

## Release Delta

- Closed since main: 5
- New since main: 9

## How to use this backlog

Pick the highest priority row owned by your team, open a pull request against the
release branch, and delete the marker from the source file in the same change.
Rows that can no longer be reproduced should be closed with a short note on the
pull request so that the next release delta stays accurate.
