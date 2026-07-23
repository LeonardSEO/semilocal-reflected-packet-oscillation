"""Repository-wide mathematical and publication invariants."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
import re
import unittest
import zipfile


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

    def test_markdown_uses_github_math_delimiters(self) -> None:
        unsupported = re.compile(r"^\\\[|^\\\]|\\\(|\\\)", re.MULTILINE)
        markdown_files = sorted(ROOT.rglob("*.md"))
        self.assertTrue(markdown_files)
        for path in markdown_files:
            text = path.read_text(encoding="utf-8")
            self.assertIsNone(
                unsupported.search(text),
                f"{path.relative_to(ROOT)} uses non-GitHub math delimiters",
            )
            self.assertNotRegex(
                text,
                re.compile(r"^\s*\$\$\s*$", re.MULTILINE),
                f"{path.relative_to(ROOT)} should use fenced math blocks",
            )
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertGreaterEqual(readme.count("```math"), 7)
        self.assertIn("$K_h=h*h$", readme)

    def test_no_invented_license_file(self) -> None:
        self.assertFalse((ROOT / "LICENSE").exists())
        notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
        self.assertIn(
            "did not contain an explicit licensing policy",
            " ".join(notice.split()),
        )

    def test_zenodo_handoff_is_explicit_and_non_circular(self) -> None:
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        instructions = (ROOT / "ZENODO.md").read_text(encoding="utf-8")
        normalized = " ".join(instructions.split())
        self.assertIn("version: 1.0.2", citation)
        self.assertIn("Resource type: Software", instructions)
        self.assertIn("No existing DOI", instructions)
        self.assertIn("Do not leave Zenodo's default CC-BY", normalized)
        self.assertIn("unchanged paper version `1.0.0`", normalized)
        self.assertFalse((ROOT / ".zenodo.json").exists())

    def test_zenodo_bundle_contains_required_material(self) -> None:
        bundle = (
            ROOT
            / "dist"
            / "semilocal-reflected-packet-oscillation-v1.0.2-zenodo.zip"
        )
        if not bundle.exists():
            self.skipTest("release builder has not been run")
        with zipfile.ZipFile(bundle) as archive:
            names = set(archive.namelist())
        prefix = "semilocal-reflected-packet-oscillation-v1.0.2/"
        for relative in (
            "README.md",
            "REPRODUCIBILITY.md",
            "ZENODO.md",
            "CITATION.cff",
            "NOTICE",
            "paper/main.pdf",
            "paper/main.tex",
            "tests/test_repository_invariants.py",
            "ZENODO_SHA256SUMS",
        ):
            self.assertIn(prefix + relative, names)

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
