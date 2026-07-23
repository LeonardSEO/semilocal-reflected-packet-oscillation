# /// script
# requires-python = ">=3.11"
# dependencies = ["python-flint==0.9.0"]
# ///
"""Arb certificates for selected frozen-packet zero coefficients.

Only nonvanishing/sign is certified.  The unknown normalization factor is
enclosed by the rigorous coarse bound 1/2 <= c_g^(-2) <= 1.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from flint import acb, arb, ctx

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def certify(index: int, terms: int) -> dict:
    rho = acb.zeta_zero(index)
    gamma = rho.imag
    w = rho - arb("0.5")

    product = acb(1)
    for n in range(1, terms + 1):
        a = arb(2) ** (-n - 1)
        z = a * w
        product *= (z.sinh() / z) ** 2

    # Since the certified zeros used here are on Re rho=1/2, w=i gamma and
    # every omitted factor is sinc(a_n gamma)^2.  For sinc(x)^2>=1-x^2/3:
    #   product_tail >= 1-gamma^2 * 4^(-N-1)/9.
    delta = gamma**2 * arb(4) ** (-terms - 1) / 9
    tail = (arb(1) - delta).union(arb(1))
    normalization = arb("0.5").union(arb(1))
    coefficient = product * tail * normalization
    real = coefficient.real
    imag = coefficient.imag

    return {
        "index": index,
        "rho_ball": str(rho),
        "finite_product_ball": str(product),
        "tail_factor_ball": str(tail),
        "normalization_factor_ball": str(normalization),
        "coefficient_ball": str(coefficient),
        "coefficient_real_lower": str(real.lower()),
        "coefficient_real_upper": str(real.upper()),
        "coefficient_imag_ball": str(imag),
        "certified_nonzero": bool(real.lower() > 0),
        "proof_scope": (
            "includes the infinite product tail and coarse positive "
            "normalization; no claim about the infinite zero-sum tail"
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--indices", nargs="+", type=int, default=[1, 2, 4])
    parser.add_argument("--terms", type=int, default=30)
    parser.add_argument("--bits", type=int, default=220)
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            REPOSITORY_ROOT
            / "certificates"
            / "implementation_b"
            / "coefficient_certificates_arb.json"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ctx.prec = args.bits
    records = [certify(index, args.terms) for index in args.indices]
    payload = {
        "implementation": "numerical_b_python_flint_arb",
        "bits": args.bits,
        "terms": args.terms,
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(args.output)


if __name__ == "__main__":
    main()
