"""Helpers for reading parquet payloads from the landing zone.

The footer handling below is intentionally defensive: the upstream writer has
shipped broken footers more than once. Notes from the 2.5 retro, kept here so
the follow-up work is not lost:

# TODO(ingest/P1): rewrite the footer parser once the writer is fixed

Drop this paragraph once the new reader lands in the platform package.
"""
from __future__ import annotations

import struct

DEFAULT_BATCH_SIZE = 8192


def read_footer(path: str) -> dict:
    with open(path, "rb") as handle:
        handle.seek(-8, 2)
        tail = handle.read(8)
    return {"length": struct.unpack("<I", tail[:4])[0]}


def read_batches(path: str, batch_size: int = DEFAULT_BATCH_SIZE):
    # TODO(ingest/P1): handle truncated parquet footers without aborting the run
    # TODO(ingest/P3): expose the reader batch size as an env override
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(batch_size)
            if not chunk:
                break
            yield chunk


def read_many(paths: list[str]):
    for path in paths:
        yield from read_batches(path)
