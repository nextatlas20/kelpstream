"""Kafka source connector."""
from __future__ import annotations

from dataclasses import dataclass

DEFAULT_POLL_TIMEOUT_MS = 500


@dataclass
class KafkaSource:
    topic: str
    group_id: str
    bootstrap: str = "localhost:9092"

    def poll(self, consumer, timeout_ms: int = DEFAULT_POLL_TIMEOUT_MS):
        records = consumer.poll(timeout_ms)
        return records

    def commit(self, consumer, offsets) -> None:
        consumer.commit(offsets=offsets)

    def on_rebalance(self, assigned, revoked) -> list:
        for partition in revoked:
            self.drop_partition(partition)
        return list(assigned)
