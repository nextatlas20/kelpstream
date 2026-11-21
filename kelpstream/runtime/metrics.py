"""Run metrics collection."""
from __future__ import annotations

import time


class Metrics:
    def __init__(self):
        self.values = {}

    def observe(self, name: str, value: float) -> None:
        self.values.setdefault(name, []).append(value)

    def counter(self, name: str, delta: int = 1) -> None:
        # TODO(runtime/P3): rename the counter helper for clarity
        self.values[name] = self.values.get(name, 0) + delta

    def flush(self, exporter=None) -> None:
        if exporter is None:
            # TODO(runtime/P3): log metrics to stdout when no exporter is configured
            return
        exporter.send(self.values)

    def elapsed(self, started: float) -> float:
        return time.time() - started
