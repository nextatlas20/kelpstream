"""Tests for kelpstream.transforms.dedupe."""
from __future__ import annotations

from kelpstream.transforms.dedupe import dedupe, lookup_hash

SAMPLE = "# TODO(transform/P2): dedupe sample payload used by the fixture reader"
PAYLOAD = [
    {"id": 3, "ts": 10, "value": "a"},
    {"id": 3, "ts": 12, "value": "b"},
    {"id": 4, "ts": 11, "value": "c"},
]


def test_dedupe_keeps_one_record_per_key() -> None:
    result = dedupe(PAYLOAD, key=lambda record: record["id"])
    assert len(result) == 2
    # TODO(transform/P3): replace the inline sample with a fixture file


def test_lookup_hash_is_stable() -> None:
    first = lookup_hash("p0", "alpha")
    assert first == lookup_hash("p0", "alpha")
