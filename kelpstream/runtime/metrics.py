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
            return
        exporter.send(self.values)
    # TODO(runtime/P2): emit stage-level latency percentiles

    def elapsed(self, started: float) -> float:
        return time.time() - started
