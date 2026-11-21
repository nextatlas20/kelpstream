# kelpstream

Kelpstream moves events from Kafka and object storage into the analytics lake.
The repository ships the ingest adapters, the record transformations and the
sink implementations used by the platform pipelines.

## Layout

- `kelpstream/io` - source adapters and file readers/writers
- `kelpstream/transforms` - record level transformations
- `kelpstream/sinks` - destination adapters
- `kelpstream/runtime` - scheduling and metrics

## Branches

`main` is the stabilisation branch. Work for the next platform release lands on
`release/<minor>` branches and is merged back after the tag.
