"""Column mapping and casting rules."""
from __future__ import annotations


def cast_row(row: dict, mapping: dict) -> dict:
    result = {}
    for target, spec in mapping.items():
        source, caster = spec
        # TODO(transform/P2): report the source column when a cast fails
        result[target] = caster(row[source])
    return result


def required_columns(mapping: dict) -> tuple:
    return tuple(sorted(source for source, _ in mapping.values()))


def rename_columns(row: dict, renames: dict) -> dict:
    return {renames.get(name, name): value for name, value in row.items()}
