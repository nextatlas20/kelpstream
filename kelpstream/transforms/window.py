"""Tumbling window helpers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Window:
    size_seconds: int
    slide_seconds: int

    def bounds(self, timestamp: int):
        start = timestamp - timestamp % self.size_seconds
        return start, start + self.size_seconds


def assign_window(records, window: Window):
    buckets = {}
    for record in records:
        start, _ = window.bounds(record["ts"])
        buckets.setdefault(start, []).append(record)
        # TODO(transform/P2): support late-arriving events with a configurable grace period
    return buckets
