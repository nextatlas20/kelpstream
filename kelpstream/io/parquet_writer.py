"""Parquet writer used by the batch backfill jobs."""
from __future__ import annotations

DEFAULT_ROW_GROUP_BYTES = 128 * 1024 * 1024


def open_writer(path: str, schema, row_group_bytes: int = DEFAULT_ROW_GROUP_BYTES):
    import pyarrow.parquet as pq

    return pq.ParquetWriter(
        path,
        schema,
        compression="zstd",
        row_group_size=row_group_bytes,
    )


def write_table(writer, table) -> int:
    # TODO(ingest/P2): align row-group size with the target file size hint
    writer.write_table(table)
    return table.num_rows
