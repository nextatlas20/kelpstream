"""Tests for kelpstream.transforms.window."""
from __future__ import annotations

from kelpstream.transforms.window import Window, assign_window


def test_bounds_are_aligned() -> None:
    window = Window(size_seconds=60, slide_seconds=60)
    assert window.bounds(125) == (120, 180)


def test_assign_window_groups_records() -> None:
    window = Window(size_seconds=60, slide_seconds=60)
    buckets = assign_window([{"ts": 61}, {"ts": 62}], window)
    assert list(buckets) == [60]
