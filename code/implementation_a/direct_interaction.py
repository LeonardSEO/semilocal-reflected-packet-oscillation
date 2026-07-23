#!/usr/bin/env python3
"""High-precision direct prime-power diagnostics for the frozen packet.

This file uses only the specification in
../../research/FROZEN_SPECIFICATION.md.  The
infinite convolution is approximated after N factors.  Its omitted tail is
not silently discarded: the support enclosure for the tail gives explicit
upper and lower bounds for K_h and hence for the direct arithmetic
interaction.  Decimal arithmetic is used for the displayed high-precision
values.  The separate certify_y_half.py script supplies a fully rational,
machine-checkable certificate at y=1/2.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from decimal import Decimal, getcontext
from math import comb, factorial, isqrt
from pathlib import Path
from typing import Iterable

from scipy.special import roots_legendre

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def decimal_string(value: Decimal, places: int = 40) -> str:
    """Stable scientific-notation serialization."""

    return f"{value:.{places}E}"


def sieve_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            count = (limit - p * p) // p + 1
            flags[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if flags[n]]


@dataclass(frozen=True)
class PrimePower:
    n: int
    p: int
    exponent: int


def prime_powers_up_to(limit: int) -> list[PrimePower]:
    """Return every p^m <= limit exactly once."""

    result: list[PrimePower] = []
    for p in sieve_primes(limit):
        n = p
        exponent = 1
        while n <= limit:
            result.append(PrimePower(n=n, p=p, exponent=exponent))
            if n > limit // p:
                break
            n *= p
            exponent += 1
    result.sort(key=lambda item: (item.n, item.p))
    return result


def finite_difference_coefficients(n_factors: int) -> list[int]:
    """Coefficients of product_n (1-z^(2^(N-n)))^2."""

    length = 2 * (2**n_factors - 1) + 1
    coefficients = [0] * length
    coefficients[0] = 1
    high = 0
    for n in range(1, n_factors + 1):
        step = 2 ** (n_factors - n)
        old = coefficients[: high + 1]
        coefficients[: high + 1] = [0] * (high + 1)
        for index, value in enumerate(old):
            coefficients[index] += value
            coefficients[index + step] -= 2 * value
            coefficients[index + 2 * step] += value
        high += 2 * step
    return coefficients


class FiniteAutocorrelation:
    """Exact-form B-spline evaluator carried out in Decimal arithmetic.

    If g_N is the convolution of the first N frozen uniforms, this evaluates
    G_N = g_N * g_N.  The prefix-moment implementation evaluates many points
    in one pass and includes the two copies of every uniform exactly.
    """

    def __init__(self, n_factors: int):
        self.n_factors = n_factors
        self.scale = 2**n_factors
        self.offset = self.scale - 1
        self.degree = 2 * n_factors - 1
        self.coefficients = finite_difference_coefficients(n_factors)
        self.prefactor = (
            Decimal(2) ** (-n_factors * n_factors + 2 * n_factors)
            / Decimal(factorial(self.degree))
        )
        self.support_radius = Decimal(self.offset) / Decimal(self.scale)

    def evaluate_batch(self, points: Iterable[Decimal]) -> list[Decimal]:
        indexed = sorted(
            (abs(Decimal(point)), index) for index, point in enumerate(points)
        )
        output: list[Decimal | None] = [None] * len(indexed)
        moments = [0] * (self.degree + 1)
        next_coefficient = 0

        for x, output_index in indexed:
            if x >= self.support_radius:
                output[output_index] = Decimal(0)
                continue

            u = x * Decimal(self.scale)
            threshold = Decimal(self.offset) + u
            while (
                next_coefficient < len(self.coefficients)
                and Decimal(next_coefficient) < threshold
            ):
                coefficient = self.coefficients[next_coefficient]
                if coefficient:
                    q = self.offset - next_coefficient
                    q_power = 1
                    for order in range(self.degree + 1):
                        moments[order] += coefficient * q_power
                        q_power *= q
                next_coefficient += 1

            polynomial = Decimal(0)
            u_power = Decimal(1)
            for order in range(self.degree + 1):
                integer_coefficient = (
                    comb(self.degree, order) * moments[self.degree - order]
                )
                polynomial += Decimal(integer_coefficient) * u_power
                u_power *= u
            output[output_index] = self.prefactor * polynomial

        return [value if value is not None else Decimal(0) for value in output]


def decimal_sinhc(x: Decimal) -> Decimal:
    """sinh(x)/x by its positive power series."""

    total = Decimal(1)
    term = Decimal(1)
    tolerance = Decimal(10) ** (-(getcontext().prec - 10))
    for k in range(1, 10_000):
        term *= x * x / Decimal((2 * k) * (2 * k + 1))
        total += term
        if abs(term) < tolerance:
            return total
    raise RuntimeError("sinhc series did not converge")


def packet_moment_data(
    evaluator: FiniteAutocorrelation,
) -> dict[str, Decimal]:
    """Return central and tail-enclosed values of M_h^2."""

    n_factors = evaluator.n_factors
    epsilon = Decimal(2) ** (-n_factors)
    g_zero, g_epsilon = evaluator.evaluate_batch([Decimal(0), epsilon])

    finite_product = Decimal(1)
    for n in range(1, n_factors + 1):
        finite_product *= decimal_sinhc(Decimal(2) ** (-n - 2))

    # For the omitted product, log(sinh x/x) <= x^2/6.  Here
    # sum_{n>N} (a_n/2)^2/6 = 2^(-2N-5)/9.
    tail_log_bound = (
        Decimal(2) ** (-2 * n_factors - 5) / Decimal(9)
    )
    moment_g_low = finite_product
    moment_g_high = finite_product * tail_log_bound.exp()

    # The central value uses many additional factors, while the bounds use
    # only the theorem above.
    moment_g_central = finite_product
    for n in range(n_factors + 1, n_factors + 50):
        moment_g_central *= decimal_sinhc(Decimal(2) ** (-n - 2))

    return {
        "epsilon": epsilon,
        "G_N_0": g_zero,
        "G_N_epsilon": g_epsilon,
        "M_h_squared_central": moment_g_central**2 / g_zero,
        "M_h_squared_low": moment_g_low**2 / g_zero,
        "M_h_squared_high": moment_g_high**2 / g_epsilon,
    }


def absolute_interval(low: Decimal, high: Decimal) -> tuple[Decimal, Decimal]:
    if low <= 0 <= high:
        return Decimal(0), max(abs(low), abs(high))
    return min(abs(low), abs(high)), max(abs(low), abs(high))


def kernel_queries(
    evaluator: FiniteAutocorrelation,
    radii: list[Decimal],
    moment_data: dict[str, Decimal],
) -> list[dict[str, Decimal]]:
    """Evaluate K_h with the rigorous omitted-support enclosure.

    The displayed Decimal roundoff is not claimed to be directed.  The
    enclosure itself is the exact analytic consequence of:

      G_N(|r|+eps) <= G(r) <= G_N(max(|r|-eps,0)),
      G_N(eps) <= G(0) <= G_N(0).
    """

    epsilon = moment_data["epsilon"]
    queries: list[Decimal] = []
    for radius in radii:
        radius = abs(radius)
        queries.extend(
            [
                radius,
                radius + epsilon,
                max(radius - epsilon, Decimal(0)),
            ]
        )
    values = evaluator.evaluate_batch(queries)
    g_zero = moment_data["G_N_0"]
    g_epsilon = moment_data["G_N_epsilon"]

    result: list[dict[str, Decimal]] = []
    for index, radius in enumerate(radii):
        center = values[3 * index] / g_zero
        lower = values[3 * index + 1] / g_zero
        upper = values[3 * index + 2] / g_epsilon
        result.append({"center": center, "low": lower, "high": upper})
    return result


def archimedean_diagnostic(
    y_values: list[Decimal],
    evaluator: FiniteAutocorrelation,
    moment_data: dict[str, Decimal],
    order: int,
) -> list[dict[str, Decimal]]:
    """Gauss-Legendre diagnostics for A_h in the real-place formula."""

    def evaluate_at_order(quadrature_order: int) -> list[dict[str, Decimal]]:
        nodes_float, weights_float = roots_legendre(quadrature_order)
        nodes = [Decimal(repr(float(node))) for node in nodes_float]
        weights = [Decimal(repr(float(weight))) for weight in weights_float]
        kernel = kernel_queries(evaluator, nodes, moment_data)
        results: list[dict[str, Decimal]] = []
        for y in y_values:
            center_sum = Decimal(0)
            lower_sum = Decimal(0)
            upper_sum = Decimal(0)
            for node, weight, k_value in zip(nodes, weights, kernel):
                r = Decimal(2) * y - node
                factor = (r / Decimal(2)).exp() / (r.exp() - (-r).exp())
                center_sum += weight * factor * k_value["center"]
                lower_sum += weight * factor * k_value["low"]
                upper_sum += weight * factor * k_value["high"]
            # A_h is the negative of the positive integral.
            results.append(
                {
                    "center": -center_sum,
                    "tail_low": -upper_sum,
                    "tail_high": -lower_sum,
                }
            )
        return results

    fine = evaluate_at_order(order)
    coarse = evaluate_at_order(max(16, order // 2))
    for fine_item, coarse_item in zip(fine, coarse):
        fine_item["quadrature_drift"] = abs(
            fine_item["center"] - coarse_item["center"]
        )
    return fine


def run(args: argparse.Namespace) -> None:
    getcontext().prec = args.precision
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    y_values = [
        Decimal(args.y_start) + Decimal(index) * Decimal(args.y_step)
        for index in range(args.y_count)
    ]
    if args.extra_y.strip():
        y_values.extend(
            Decimal(value.strip())
            for value in args.extra_y.split(",")
            if value.strip()
        )
    y_values = sorted(set(y_values))
    if min(y_values) < Decimal("0.5"):
        raise ValueError("the frozen reflected-packet formula requires y >= 1/2")

    evaluator = FiniteAutocorrelation(args.factors)
    moment_data = packet_moment_data(evaluator)
    maximum_x = (Decimal(2) * max(y_values) + Decimal(1)).exp()
    all_prime_powers = prime_powers_up_to(int(maximum_x) + 1)

    entries: list[dict[str, object]] = []
    radii: list[Decimal] = []
    for y_index, y in enumerate(y_values):
        for prime_power in all_prime_powers:
            log_n = Decimal(prime_power.n).ln()
            signed_r = Decimal(2) * y - log_n
            # Strict support window.  Equality contributes exactly zero.
            if abs(signed_r) < Decimal(1):
                entries.append(
                    {
                        "y_index": y_index,
                        "y": y,
                        "prime_power": prime_power,
                        "log_n": log_n,
                        "signed_r": signed_r,
                    }
                )
                radii.append(abs(signed_r))

    kernel_values = kernel_queries(evaluator, radii, moment_data)
    contribution_rows: list[dict[str, str | int]] = []
    grouped: list[list[tuple[Decimal, Decimal, Decimal]]] = [
        [] for _ in y_values
    ]

    for entry, kernel_value in zip(entries, kernel_values):
        prime_power = entry["prime_power"]
        assert isinstance(prime_power, PrimePower)
        coefficient = (
            Decimal(prime_power.p).ln()
            / Decimal(prime_power.n).sqrt()
        )
        term_center = coefficient * kernel_value["center"]
        term_low = coefficient * kernel_value["low"]
        term_high = coefficient * kernel_value["high"]
        grouped[int(entry["y_index"])].append(
            (term_center, term_low, term_high)
        )
        contribution_rows.append(
            {
                "y": decimal_string(entry["y"], 20),
                "n": prime_power.n,
                "p": prime_power.p,
                "m": prime_power.exponent,
                "log_n": decimal_string(entry["log_n"], 30),
                "r_2y_minus_log_n": decimal_string(entry["signed_r"], 30),
                "K_center": decimal_string(kernel_value["center"], 30),
                "K_tail_low": decimal_string(kernel_value["low"], 30),
                "K_tail_high": decimal_string(kernel_value["high"], 30),
                "term_center": decimal_string(term_center, 30),
                "term_tail_low": decimal_string(term_low, 30),
                "term_tail_high": decimal_string(term_high, 30),
            }
        )

    archimedean = archimedean_diagnostic(
        y_values,
        evaluator,
        moment_data,
        args.quadrature_order,
    )
    grid_rows: list[dict[str, object]] = []
    mh_center = moment_data["M_h_squared_central"]
    mh_low = moment_data["M_h_squared_low"]
    mh_high = moment_data["M_h_squared_high"]

    for index, y in enumerate(y_values):
        prime_center = sum(
            (item[0] for item in grouped[index]), Decimal(0)
        )
        prime_low = sum((item[1] for item in grouped[index]), Decimal(0))
        prime_high = sum((item[2] for item in grouped[index]), Decimal(0))
        exp_y = y.exp()
        interaction_center = exp_y * mh_center - prime_center
        interaction_low = exp_y * mh_low - prime_high
        interaction_high = exp_y * mh_high - prime_low

        arch = archimedean[index]
        residual_center = (-y).exp() * mh_center
        delta_center = Decimal(2) * (
            arch["center"] + residual_center + interaction_center
        )
        delta_tracked_low = Decimal(2) * (
            arch["tail_low"]
            + (-y).exp() * mh_low
            + interaction_low
            - arch["quadrature_drift"]
        )
        delta_tracked_high = Decimal(2) * (
            arch["tail_high"]
            + (-y).exp() * mh_high
            + interaction_high
            + arch["quadrature_drift"]
        )

        grid_rows.append(
            {
                "y": decimal_string(y, 20),
                "prime_power_count": len(grouped[index]),
                "prime_sum_center": decimal_string(prime_center),
                "prime_sum_tail_low": decimal_string(prime_low),
                "prime_sum_tail_high": decimal_string(prime_high),
                "I_center": decimal_string(interaction_center),
                "I_tail_low": decimal_string(interaction_low),
                "I_tail_high": decimal_string(interaction_high),
                "A_center": decimal_string(arch["center"]),
                "A_tail_low": decimal_string(arch["tail_low"]),
                "A_tail_high": decimal_string(arch["tail_high"]),
                "A_quadrature_drift": decimal_string(
                    arch["quadrature_drift"]
                ),
                "exp_minus_y_Mh2_center": decimal_string(residual_center),
                "Delta_center": decimal_string(delta_center),
                "Delta_tracked_low": decimal_string(delta_tracked_low),
                "Delta_tracked_high": decimal_string(delta_tracked_high),
            }
        )

    metadata = {
        "implementation": "numerical_a/direct_interaction.py",
        "decimal_precision": args.precision,
        "finite_uniform_factors": args.factors,
        "omitted_autocorrelation_tail_support_radius": decimal_string(
            moment_data["epsilon"], 30
        ),
        "packet_formula": (
            "g_N is the convolution of b_{2^(-n-1)}, 1<=n<=N; "
            "G_N=g_N*g_N is evaluated by the exact nonuniform B-spline "
            "finite-difference formula"
        ),
        "endpoint_convention": (
            "all p^m with |2y-log(p^m)|<1 are included; equality is "
            "excluded because K_h(+-1)=0 and has no half weight"
        ),
        "prime_power_model": "every p^m, coefficient log(p)/sqrt(p^m)",
        "M_h_squared": {
            key: decimal_string(value)
            for key, value in moment_data.items()
            if key.startswith("M_h_squared")
        },
        "G_N_0": decimal_string(moment_data["G_N_0"]),
        "G_N_epsilon": decimal_string(
            moment_data["G_N_epsilon"]
        ),
        "archimedean_method": (
            "real-place integral with Gauss-Legendre orders "
            f"{args.quadrature_order // 2} and {args.quadrature_order}"
        ),
        "certification_note": (
            "Decimal values track analytic omitted-tail bounds but Decimal "
            "rounding and Gauss quadrature are diagnostic.  The companion "
            "exact-rational certificate is certificate_y_half.json."
        ),
    }

    with (output_dir / "grid.json").open("w", encoding="utf-8") as handle:
        json.dump(grid_rows, handle, indent=2)
        handle.write("\n")
    with (output_dir / "metadata.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(metadata, handle, indent=2)
        handle.write("\n")
    with (output_dir / "prime_power_contributions.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        fieldnames = list(contribution_rows[0].keys())
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contribution_rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--factors", type=int, default=14)
    parser.add_argument("--precision", type=int, default=80)
    parser.add_argument("--y-start", default="0.5")
    parser.add_argument("--y-step", default="0.5")
    parser.add_argument("--y-count", type=int, default=8)
    parser.add_argument(
        "--extra-y",
        default="1.25,1.75,2.25",
        help="comma-separated additional diagnostic separations",
    )
    parser.add_argument("--quadrature-order", type=int, default=192)
    parser.add_argument(
        "--output-dir",
        default=str(
            REPOSITORY_ROOT / "certificates" / "implementation_a" / "n14"
        ),
    )
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
