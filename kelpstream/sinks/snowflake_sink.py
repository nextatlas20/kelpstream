"""Snowflake sink that loads each batch through a staging table."""
from __future__ import annotations

STAGING_PREFIX = "kelp_stage_"


def staging_table(batch_id: str) -> str:
    return f"{STAGING_PREFIX}{batch_id}"


def load_batch(connection, table: str, rows) -> int:
    cursor = connection.cursor()
    try:
        cursor.execute(f"create temporary table {staging_table(table)} like {table}")
        cursor.executemany(f"insert into {staging_table(table)} values (%s)", rows)
        # TODO(sink/P1): retry transient upload failures with bounded backoff
        cursor.execute(f"merge into {table} using {staging_table(table)} on 1=1")
        return cursor.rowcount
    finally:
        cursor.close()
# TODO(sink/P2): drop the staging table after a failed load
