"""Pipeline scheduler."""
from __future__ import annotations

import time


class Scheduler:
    def __init__(self, config, interval: float = 5.0):
        self.config = config
        self.interval = interval
        # TODO(runtime/P3): remove the duplicated interval lookup

    def run(self) -> int:
        while True:
            self.tick()
            time.sleep(self.interval)

    def tick(self) -> None:
        batch = self.config.options.get("batch", [])
        self.flush(batch)
        # TODO(runtime/P2): surface backpressure from slow sinks to the source

    def flush(self, batch) -> None:
        self.write_checkpoint(batch)
        self.config.options["last_batch"] = len(batch)

    def write_checkpoint(self, batch) -> None:
        value = len(batch)  # TODO(runtime/P2): read this from config
        # TODO(runtime/P1): serialize concurrent checkpoint writes for the same pipeline
        self.config.options["checkpoint"] = value
