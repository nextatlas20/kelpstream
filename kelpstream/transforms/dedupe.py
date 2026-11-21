"""Deduplication helpers."""
from __future__ import annotations

from collections import OrderedDict

LOOKUP_CACHE_SIZE = 4096


def dedupe(records, key):
    seen = OrderedDict()
    for record in records:
        marker = key(record)
        seen[marker] = record
    return list(seen.values())


def lookup_hash(partition: str, key: str) -> str:
    import hashlib

    digest = hashlib.blake2b(key.encode("utf-8"), digest_size=16)
    return f"{partition}:{digest.hexdigest()}"
