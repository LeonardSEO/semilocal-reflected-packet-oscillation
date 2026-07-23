#!/usr/bin/env python3
"""Cross-check implementation A against the independent implementation B."""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path


def load_b_output(b_directory: Path) -> tuple[Path, dict[str, object]]:
    # The round request called this results.json.  The independent codebase
    # currently writes explicit_formula_b_output.json; prefer results.json if
    # that alias is added later, without changing either implementation.
    candidates = [
        b_directory / "results.json",
        b_directory / "explicit_formula_b_output.json",
    ]
    for path in candidates:
        if path.exists():
            with path.open(encoding="utf-8") as handle:
                return path, json.load(handle)
    raise FileNotFoundError(
        "no numerical_b/results.json or explicit_formula_b_output.json"
    )


def main() -> None:
    getcontext().prec = 80
    repository_root = Path(__file__).resolve().parents[2]
    a_certificates = repository_root / "certificates" / "implementation_a"
    b_certificates = repository_root / "certificates" / "implementation_b"
    a_grids: dict[int, dict[Decimal, dict[str, object]]] = {}
    for factors, path in [
        (12, a_certificates / "n12" / "grid.json"),
        (14, a_certificates / "n14" / "grid.json"),
        (16, a_certificates / "n16" / "grid.json"),
    ]:
        with path.open(encoding="utf-8") as handle:
            rows = json.load(handle)
        a_grids[factors] = {
            Decimal(row["y"]).normalize(): row for row in rows
        }

    b_path, b_payload = load_b_output(b_certificates)
    comparisons: list[dict[str, object]] = []
    for b_row in b_payload["results"]:
        # B records its y values in the parallel parameters array.
        index = len(comparisons)
        y = Decimal(b_payload["parameters"]["y"][index]).normalize()
        if y not in a_grids[16]:
            raise KeyError(f"implementation A has no row for y={y}")
        a_row = a_grids[16][y]

        a_center = Decimal(a_row["I_center"])
        a_low = Decimal(a_row["I_tail_low"])
        a_high = Decimal(a_row["I_tail_high"])
        a_tracked_budget = max(a_center - a_low, a_high - a_center)
        b_center = Decimal(b_row["I_direct_prime_stieltjes"])
        b_budget = Decimal(b_row["I_direct_numerical_error_budget"])
        absolute_difference = abs(a_center - b_center)
        combined_budget = a_tracked_budget + b_budget

        b_interval_low = b_center - b_budget
        b_interval_high = b_center + b_budget
        intervals_overlap = not (
            a_high < b_interval_low or b_interval_high < a_low
        )
        counts_match = (
            int(a_row["prime_power_count"])
            == int(b_row["prime_power_count"])
        )
        comparison: dict[str, object] = {
                "y": str(y),
                "A_primary_cutoff_N": 16,
                "A_I_center": str(a_center),
                "A_I_tail_low": str(a_low),
                "A_I_tail_high": str(a_high),
                "A_tracked_tail_budget": str(a_tracked_budget),
                "B_I_direct": str(b_center),
                "B_stated_error_budget": str(b_budget),
                "absolute_difference": str(absolute_difference),
                "combined_stated_budget": str(combined_budget),
                "difference_within_combined_budget": (
                    absolute_difference <= combined_budget
                ),
                "stated_intervals_overlap": intervals_overlap,
                "A_prime_power_count": int(a_row["prime_power_count"]),
                "B_prime_power_count": int(b_row["prime_power_count"]),
                "prime_power_counts_match": counts_match,
                "B_direct_minus_explicit": b_row[
                    "direct_minus_explicit"
                ],
            }
        refinement: dict[str, object] = {}
        for factors in (12, 14, 16):
            refinement_row = a_grids[factors][y]
            value = Decimal(refinement_row["I_center"])
            refinement[f"N{factors}"] = {
                "I_center": str(value),
                "absolute_difference_from_B": str(
                    abs(value - b_center)
                ),
            }
        comparison["A_cutoff_refinement"] = refinement
        comparisons.append(comparison)

    assert all(
        row["difference_within_combined_budget"]
        and row["stated_intervals_overlap"]
        and row["prime_power_counts_match"]
        for row in comparisons
    )
    output = {
        "implementation_A": (
            "numerical_a physical B-spline grids at N=12,14,16; "
            "N=16 is the primary comparison"
        ),
        "implementation_B": str(b_path.relative_to(repository_root)),
        "method_independence": (
            "A uses the physical nonuniform B-spline convolution; B uses "
            "Fourier inversion of the sinc-product. Neither method was "
            "changed for this comparison."
        ),
        "budget_status": (
            "All differences fall inside the sum of A's analytic "
            "omitted-support tail budget and B's stated quadrature/tail "
            "budget. A uses nondirected Decimal arithmetic and B's "
            "QUADPACK estimate is not an interval certificate, so this is "
            "a diagnostic agreement, not a load-bearing proof."
        ),
        "comparisons": comparisons,
        "finite_certificate_status": (
            "The separate exact-rational I_h(1/2) certificate remains "
            "finite and explicitly non-load-bearing for asymptotics."
        ),
    }
    with (a_certificates / "crosscheck_numerical_b.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")

    for row in comparisons:
        print(
            f"y={row['y']}: |A-B|={row['absolute_difference']}; "
            f"combined={row['combined_stated_budget']}; PASS"
        )


if __name__ == "__main__":
    main()
