"""Pipeline configuration loading for Kelpstream."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

DEFAULT_BATCH_SIZE = 8192
SUPPORTED_SOURCES = ("kafka", "s3", "local")


@dataclass
class PipelineConfig:
    """Resolved settings for a single pipeline."""

    name: str
    source: str
    batch_size: int = DEFAULT_BATCH_SIZE
    options: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, payload: dict[str, Any]) -> "PipelineConfig":
        source = payload.get("source", "local")
        if source not in SUPPORTED_SOURCES:
            raise ValueError(f"unsupported source: {source}")
        # todo(ingest/P3): move the supported-source list into the config schema
        return cls(
            name=payload["name"],
            source=source,
            batch_size=int(payload.get("batch_size", DEFAULT_BATCH_SIZE)),
            options=dict(payload.get("options", {})),
        )


def load_config(path: str) -> PipelineConfig:
    import tomllib

    with open(path, "rb") as handle:
        return PipelineConfig.from_mapping(tomllib.load(handle))


def apply_env_overrides(config: PipelineConfig) -> PipelineConfig:
    batch_size = os.environ.get("KELP_BATCH_SIZE")
    if batch_size:
        config.batch_size = int(batch_size)
    # TODO(cli/P2): reject unknown keys when loading pipeline config
    return config
