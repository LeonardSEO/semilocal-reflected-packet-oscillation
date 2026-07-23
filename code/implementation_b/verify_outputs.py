#!/usr/bin/env python3
"""Verify the committed implementation-B machine-readable outputs."""

from __future__ import annotations

import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CERTIFICATES = REPOSITORY_ROOT / "certificates" / "implementation_b"


def main() -> None:
    explicit = json.loads(
        (CERTIFICATES / "explicit_formula_b_output.json").read_text(
            encoding="utf-8"
        )
    )
    certificates = json.loads(
        (CERTIFICATES / "coefficient_certificates_arb.json").read_text(
            encoding="utf-8"
        )
    )

    assert explicit["implementation"] == "numerical_b"
    for record in explicit["results"]:
        powers = record["prime_powers"]
        assert any(item["m"] > 1 for item in powers)
        for item in powers:
            assert item["value"] == item["p"] ** item["m"]
            assert abs(item["shift"]) < 1.0
        discrepancy = abs(float(record["direct_minus_explicit"]))
        assert discrepancy < 1e-11, (record["y"], discrepancy)

    assert certificates["implementation"] == "numerical_b_python_flint_arb"
    assert certificates["records"]
    for record in certificates["records"]:
        assert record["certified_nonzero"] is True
        lower = float(
            record["coefficient_real_lower"].split()[0].lstrip("[")
        )
        assert lower > 0.0

    print("implementation-B outputs verified")


if __name__ == "__main__":
    main()
