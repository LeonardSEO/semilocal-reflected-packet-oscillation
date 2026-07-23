"""Repository-wide mathematical and publication invariants."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepositoryInvariantTests(unittest.TestCase):
    def test_prominent_scope_disclaimers(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        paper = (ROOT / "paper" / "main.tex").read_text(encoding="utf-8").lower()
        for phrase in (
            "not a proof of the riemann hypothesis",
            "fixed-packet",
            "actual semilocal ground state",
            "unconditional infinite sign",
        ):
            self.assertIn(phrase, readme)
        self.assertIn("not a proof of the riemann hypothesis", paper)
        self.assertIn("fixed-packet theorem", paper)

    def test_no_invented_license_file(self) -> None:
        self.assertFalse((ROOT / "LICENSE").exists())
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertIn(
            "did not contain an explicit licensing policy",
            " ".join(notice.split()),
        )

    def test_implementation_a_records_all_valid_prime_powers(self) -> None:
        for path in sorted(
            (ROOT / "certificates" / "implementation_a").glob(
                "n*/prime_power_contributions.csv"
            )
        ):
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            self.assertTrue(rows, path)
            self.assertTrue(any(int(row["m"]) > 1 for row in rows))
            for row in rows:
                p = int(row["p"])
                exponent = int(row["m"])
                value = int(row["n"])
                self.assertEqual(value, p**exponent)
                self.assertGreaterEqual(exponent, 1)
                self.assertLess(
                    abs(float(row["r_2y_minus_log_n"])), 1.0
                )

    def test_implementation_b_records_all_valid_prime_powers(self) -> None:
        path = (
            ROOT
            / "certificates"
            / "implementation_b"
            / "explicit_formula_b_output.json"
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        for record in payload["results"]:
            powers = record["prime_powers"]
            self.assertTrue(any(int(item["m"]) > 1 for item in powers))
            for item in powers:
                self.assertEqual(item["value"], item["p"] ** item["m"])
                self.assertLess(abs(float(item["shift"])), 1.0)

    def test_y_half_certificate_contains_exact_window(self) -> None:
        path = (
            ROOT
            / "certificates"
            / "implementation_a"
            / "certificate_y_half.json"
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        serialized = json.dumps(payload)
        for value in (2, 3, 4, 5, 7):
            self.assertIn(f'"n": {value}', serialized)
        enclosure = payload["short_enclosure"]
        self.assertGreater(float(enclosure["lower"]), 0.0)
        self.assertLess(float(enclosure["lower"]), float(enclosure["upper"]))

    def test_frozen_constants_appear_in_paper_and_research(self) -> None:
        paper = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "paper").rglob("*.tex"))
        )
        research = (
            ROOT / "research" / "FROZEN_SPECIFICATION.md"
        ).read_text(encoding="utf-8")
        shared_fragments = (
            r"a_n=2^{-n-1}",
            r"p^{m/2}",
            r"4\pi i",
        )
        for fragment in shared_fragments:
            self.assertIn(fragment, paper)
            self.assertIn(fragment, research)
        self.assertIn(r"p^m\le\lambda^2", paper)
        self.assertIn(r"p^m\le e^{2a}=\lambda^2", research)
        self.assertTrue(math.isfinite(len(paper)))


if __name__ == "__main__":
    unittest.main()
