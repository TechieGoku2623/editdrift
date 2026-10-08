"""Drift is outside this line's window. A missing lot is not a score."""

from __future__ import annotations

import unittest

from editdrift import DriftError, watch
from editdrift.__main__ import CURRENT, HISTORY


class WatchTests(unittest.TestCase):
    def test_growth_leaves_the_window_and_the_lot_changes(self) -> None:
        report = watch(HISTORY, CURRENT)
        self.assertEqual(report["drifted"], ["growth"])
        self.assertTrue(report["lot_changed"])
        self.assertTrue(report["alert"])
        window = report["window"]
        assert isinstance(window, dict)
        growth = window["growth"]
        assert isinstance(growth, dict)
        self.assertEqual(growth["low"], 1.05)
        self.assertEqual(growth["high"], 1.12)

    def test_inside_the_same_lot_does_not_alert(self) -> None:
        current = {
            "line": "HEK-A",
            "passage": 13,
            "lot": "G3",
            "readouts": {"growth": 1.10, "marker": 0.42},
        }
        report = watch(HISTORY, current)
        self.assertFalse(report["alert"])
        self.assertEqual(report["drifted"], [])

    def test_missing_lot_raises(self) -> None:
        current = {**CURRENT, "lot": ""}
        with self.assertRaises(DriftError):
            watch(HISTORY, current)

    def test_empty_window_raises(self) -> None:
        with self.assertRaises(DriftError):
            watch([], CURRENT)


if __name__ == "__main__":
    unittest.main()
