"""Watch one designed line leave its own accepted window."""

from __future__ import annotations

from .engine import format_report, watch

HISTORY = [
    {"line": "HEK-A", "passage": 8, "lot": "G3", "readouts": {"growth": 1.05, "marker": 0.40}},
    {"line": "HEK-A", "passage": 10, "lot": "G3", "readouts": {"growth": 1.12, "marker": 0.44}},
    {"line": "HEK-A", "passage": 12, "lot": "G3", "readouts": {"growth": 1.08, "marker": 0.41}},
]

CURRENT = {
    "line": "HEK-A",
    "passage": 18,
    "lot": "G4",
    "readouts": {"growth": 1.55, "marker": 0.43},
}


def main() -> int:
    print(format_report(watch(HISTORY, CURRENT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
