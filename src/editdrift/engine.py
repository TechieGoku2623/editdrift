"""Drift is a distance from this line's last accepted window.

A missing passage or lot is not a chart. It is an incomplete record.
"""

from __future__ import annotations

from typing import Mapping


class DriftError(ValueError):
    """The baseline or the new observation cannot be compared."""


def watch(
    history: list[Mapping[str, object]],
    current: Mapping[str, object],
) -> dict[str, object]:
    if not history:
        raise DriftError("baseline window is empty")
    accepted = [_check(row) for row in history]
    latest = _check(current)
    keys = sorted({key for row in accepted for key in row["readouts"]})
    window: dict[str, dict[str, float | int]] = {}
    drifted: list[str] = []
    for key in keys:
        values = [row["readouts"][key] for row in accepted if key in row["readouts"]]
        low, high = min(values), max(values)
        window[key] = {"low": low, "high": high, "n": len(values)}
        observed = latest["readouts"].get(key)
        if observed is None:
            continue
        if observed < low or observed > high:
            drifted.append(key)
    lot_changed = latest["lot"] != accepted[-1]["lot"]
    return {
        "line": latest["line"],
        "passage": latest["passage"],
        "lot": latest["lot"],
        "lot_changed": lot_changed,
        "window": window,
        "drifted": drifted,
        "alert": bool(drifted) or lot_changed,
    }


def format_report(report: dict[str, object]) -> str:
    lines = [
        "editdrift",
        "",
        f"line: {report['line']}",
        f"passage: {report['passage']}",
        f"lot: {report['lot']}",
        f"lot changed: {str(report['lot_changed']).lower()}",
        "accepted window:",
    ]
    window = report["window"]
    assert isinstance(window, dict)
    for key, bounds in window.items():
        assert isinstance(bounds, dict)
        lines.append(f"  {key}  {bounds['low']} to {bounds['high']}  n={bounds['n']}")
    drifted = report["drifted"]
    assert isinstance(drifted, list)
    lines.append("outside window: " + (", ".join(drifted) if drifted else "none"))
    lines.append(f"alert: {str(report['alert']).lower()}")
    lines.append("")
    lines.append("compared to this line, not to a universal template")
    return "\n".join(lines)


def _check(row: Mapping[str, object]) -> dict[str, object]:
    line = str(row.get("line", "")).strip()
    lot = str(row.get("lot", "")).strip()
    passage = row.get("passage")
    readouts = row.get("readouts")
    if not line or not lot:
        raise DriftError("line and lot are required")
    if isinstance(passage, bool) or not isinstance(passage, int) or passage < 1:
        raise DriftError("passage must be a positive integer")
    if not isinstance(readouts, dict) or not readouts:
        raise DriftError("readouts are required")
    clean: dict[str, float] = {}
    for key, value in readouts.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise DriftError(f"{key} must be numeric")
        clean[str(key)] = float(value)
    return {"line": line, "lot": lot, "passage": passage, "readouts": clean}
