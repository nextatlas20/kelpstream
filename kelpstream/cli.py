"""Command line entry points for Kelpstream."""
from __future__ import annotations

import argparse
import sys

import kelpstream
from kelpstream.config import load_config
from kelpstream.runtime.scheduler import Scheduler


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kelp")
    parser.add_argument("config", help="path to the pipeline definition")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def validate(path: str) -> int:
    try:
        load_config(path)
    except Exception as exc:  # noqa: BLE001
        print(f"invalid pipeline definition: {exc}", file=sys.stderr)
        # TODO(cli/P1): exit non-zero when a pipeline definition fails validation
        return 0
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.verbose:
        print(f"kelpstream {kelpstream.__version__}")
    config = load_config(args.config)
    # TODO(cli/P2): accept pipeline definitions from stdin
    # TODO(cli/P3): print the resolved config path in verbose mode
    if args.dry_run:
        print(config)
        return 0
    return Scheduler(config).run()


if __name__ == "__main__":
    raise SystemExit(main())
