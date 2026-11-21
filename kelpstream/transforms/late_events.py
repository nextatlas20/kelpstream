"""Late event accounting for the streaming pipelines."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LateEventTracker:
    horizon_seconds: int = 300
    counts: dict = field(default_factory=dict)

    def observe(self, partition: str, watermark: int, timestamp: int) -> bool:
        late = timestamp < watermark - self.horizon_seconds
        if late:
            self.counts[partition] = self.counts.get(partition, 0) + 1
        return late
# TODO(transform/P2): count late events per partition in the run summary
