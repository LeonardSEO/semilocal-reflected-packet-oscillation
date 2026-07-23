#!/usr/bin/env python3
"""Summarize N=12,14,16 packet-cutoff sensitivity."""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path


def load_grid(path: Path) -> dict[str, dict[str, object]]:
    with path.open(encoding="utf-8") as handle:
        rows = json.load(handle)
    return {str(Decimal(row["y"])): row for row in rows}


def main() -> None:
    getcontext().prec = 80
    repository_root = Path(__file__).resolve().parents[2]
    certificates = repository_root / "certificates" / "implementation_a"
    grids = {
        12: load_grid(certificates / "n12" / "grid.json"),
        14: load_grid(certificates / "n14" / "grid.json"),
        16: load_grid(certificates / "n16" / "grid.json"),
    }
    rows: list[dict[str, object]] = []
    for y in sorted(grids[14], key=Decimal):
        row: dict[str, object] = {"y": y}
        for factors in (12, 14, 16):
            source = grids[factors][y]
            row[f"I_N{factors}"] = source["I_center"]
            row[f"Delta_N{factors}"] = source["Delta_center"]
        row["abs_I_N16_minus_N14"] = str(
            abs(
                Decimal(str(row["I_N16"]))
                - Decimal(str(row["I_N14"]))
            )
        )
        row["abs_I_N14_minus_N12"] = str(
            abs(
                Decimal(str(row["I_N14"]))
                - Decimal(str(row["I_N12"]))
            )
        )
        row["abs_Delta_N16_minus_N14"] = str(
            abs(
                Decimal(str(row["Delta_N16"]))
                - Decimal(str(row["Delta_N14"]))
            )
        )
        rows.append(row)

    output = {
        "description": (
            "Packet-cutoff refinement. N=12 uses 70 Decimal digits and "
            "Gauss order 128; N=14 uses 80 digits/order 192; N=16 uses "
            "90 digits/order 256."
        ),
        "rows": rows,
        "interpretation": (
            "The central values are diagnostics. The per-run grid files "
            "also carry analytic omitted-tail enclosures."
        ),
    }
    with (certificates / "refinement.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
