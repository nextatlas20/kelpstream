"""Checkpoint persistence for resumable pipelines."""
from __future__ import annotations

import json
import os
import tempfile


def checkpoint_path(root: str, pipeline: str) -> str:
    return os.path.join(root, f"{pipeline}.checkpoint.json")


def save_checkpoint(root: str, pipeline: str, state: dict) -> str:
    target = checkpoint_path(root, pipeline)
    payload = json.dumps(state, sort_keys=True).encode("utf-8")
    handle = tempfile.NamedTemporaryFile(dir=root, delete=False)
    try:
        handle.write(payload)
        handle.flush()
        # TODO(ingest/P2): store checkpoint metadata atomically alongside state
        os.replace(handle.name, target)
    finally:
        handle.close()
    return target


def load_checkpoint(root: str, pipeline: str) -> dict:
    path = checkpoint_path(root, pipeline)
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)
