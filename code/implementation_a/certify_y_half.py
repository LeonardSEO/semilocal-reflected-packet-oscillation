#!/usr/bin/env python3
"""Exact-rational certificate for I_h(1/2) > 0.

No floating-point or external interval package is used.  Logarithms,
exponentials, square roots, sinhc factors, the finite B-spline, and the
omitted convolution tail are all enclosed by rational inequalities.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


LOG_SERIES_TERMS = 70
EXP_SERIES_TERMS = 70
SINHC_SERIES_TERMS = 18
DYADIC_BITS = 140
N_FACTORS = 8


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def quantize(
    value: Fraction, bits: int, *, upward: bool
) -> Fraction:
    scale = 1 << bits
    integer = (
        ceil_fraction(value * scale)
        if upward
        else floor_fraction(value * scale)
    )
    return Fraction(integer, scale)


def atanh_log_bounds(
    numerator: int, denominator: int
) -> tuple[Fraction, Fraction]:
    """Bounds log(numerator/denominator), for ratio in [1,2]."""

    t = Fraction(numerator - denominator, numerator + denominator)
    if t == 0:
        return Fraction(0), Fraction(0)
    power = t
    partial = Fraction(0)
    for j in range(LOG_SERIES_TERMS):
        partial += 2 * power / (2 * j + 1)
        power *= t * t
    remainder = (
        2
        * power
        / (2 * LOG_SERIES_TERMS + 1)
        / (1 - t * t)
    )
    return (
        quantize(partial, DYADIC_BITS, upward=False),
        quantize(partial + remainder, DYADIC_BITS, upward=True),
    )


def log_integer_bounds(n: int) -> tuple[Fraction, Fraction]:
    if n < 1:
        raise ValueError("n must be positive")
    exponent = n.bit_length() - 1
    log2_low, log2_high = atanh_log_bounds(2, 1)
    mantissa_low, mantissa_high = atanh_log_bounds(
        n, 1 << exponent
    )
    return (
        exponent * log2_low + mantissa_low,
        exponent * log2_high + mantissa_high,
    )


def exp_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    if x < 0:
        positive_low, positive_high = exp_bounds(-x)
        return 1 / positive_high, 1 / positive_low
    term = Fraction(1)
    partial = Fraction(1)
    for k in range(1, EXP_SERIES_TERMS + 1):
        term *= x / k
        partial += term
    next_term = term * x / (EXP_SERIES_TERMS + 1)
    ratio_bound = x / (EXP_SERIES_TERMS + 2)
    if ratio_bound >= 1:
        raise ValueError("increase EXP_SERIES_TERMS")
    upper = partial + next_term / (1 - ratio_bound)
    return (
        quantize(partial, DYADIC_BITS, upward=False),
        quantize(upper, DYADIC_BITS, upward=True),
    )


def sqrt_integer_bounds(n: int) -> tuple[Fraction, Fraction]:
    scale = 1 << DYADIC_BITS
    lower_integer = isqrt(n * scale * scale)
    lower = Fraction(lower_integer, scale)
    if lower_integer * lower_integer == n * scale * scale:
        return lower, lower
    return lower, Fraction(lower_integer + 1, scale)


def sinhc_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    term = Fraction(1)
    partial = Fraction(1)
    for k in range(1, SINHC_SERIES_TERMS + 1):
        term *= x * x / ((2 * k) * (2 * k + 1))
        partial += term
    next_term = (
        term
        * x
        * x
        / ((2 * SINHC_SERIES_TERMS + 2)
           * (2 * SINHC_SERIES_TERMS + 3))
    )
    next_ratio_bound = (
        x
        * x
        / ((2 * SINHC_SERIES_TERMS + 4)
           * (2 * SINHC_SERIES_TERMS + 5))
    )
    return (
        partial,
        partial + next_term / (1 - next_ratio_bound),
    )


def finite_difference_coefficients(n_factors: int) -> list[int]:
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


def finite_G(
    x: Fraction, coefficients: list[int]
) -> Fraction:
    """Exact density G_N(x) of the first 2N uniform summands."""

    x = abs(x)
    scale = 1 << N_FACTORS
    offset = scale - 1
    degree = 2 * N_FACTORS - 1
    total = Fraction(0)
    for index, coefficient in enumerate(coefficients):
        if not coefficient:
            continue
        positive_part = x + Fraction(offset - index, scale)
        if positive_part > 0:
            total += coefficient * positive_part**degree
    return (
        total
        * Fraction(
            1 << (N_FACTORS * (N_FACTORS + 1)),
            factorial(degree),
        )
    )


def absolute_interval(
    low: Fraction, high: Fraction
) -> tuple[Fraction, Fraction]:
    if low <= 0 <= high:
        return Fraction(0), max(abs(low), abs(high))
    return min(abs(low), abs(high)), max(abs(low), abs(high))


def outward_decimal(
    value: Fraction, places: int, *, upward: bool
) -> str:
    scale = 10**places
    integer = (
        ceil_fraction(value * scale)
        if upward
        else floor_fraction(value * scale)
    )
    sign = "-" if integer < 0 else ""
    digits = str(abs(integer)).rjust(places + 1, "0")
    return f"{sign}{digits[:-places]}.{digits[-places:]}"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


def prime_power_base(n: int) -> int | None:
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        value = p
        while value < n:
            value *= p
        if value == n:
            return p
    return None


def rational_record(
    low: Fraction, high: Fraction, places: int = 15
) -> dict[str, object]:
    return {
        "decimal_outward": [
            outward_decimal(low, places, upward=False),
            outward_decimal(high, places, upward=True),
        ],
        "lower_exact": {
            "numerator": str(low.numerator),
            "denominator": str(low.denominator),
        },
        "upper_exact": {
            "numerator": str(high.numerator),
            "denominator": str(high.denominator),
        },
    }


def main() -> None:
    coefficients = finite_difference_coefficients(N_FACTORS)
    epsilon = Fraction(1, 1 << N_FACTORS)
    g_zero_upper = finite_G(Fraction(0), coefficients)
    g_zero_lower = finite_G(epsilon, coefficients)

    finite_moment_low = Fraction(1)
    finite_moment_high = Fraction(1)
    for n in range(1, N_FACTORS + 1):
        factor_low, factor_high = sinhc_bounds(
            Fraction(1, 1 << (n + 2))
        )
        finite_moment_low *= factor_low
        finite_moment_high *= factor_high

    # sum_{n>N} (a_n/2)^2/6 = 2^(-2N-5)/9.
    omitted_log_bound = Fraction(
        1, 9 * (1 << (2 * N_FACTORS + 5))
    )
    _, omitted_product_high = exp_bounds(omitted_log_bound)
    moment_g_low = finite_moment_low
    moment_g_high = finite_moment_high * omitted_product_high
    mh_squared_low = moment_g_low**2 / g_zero_upper
    mh_squared_high = moment_g_high**2 / g_zero_lower

    exp_y_low, exp_y_high = exp_bounds(Fraction(1, 2))
    main_low = exp_y_low * mh_squared_low
    main_high = exp_y_high * mh_squared_high

    exp_two_low, exp_two_high = exp_bounds(Fraction(2))
    assert exp_two_low > 7
    assert exp_two_high < 8
    contributing: list[tuple[int, int]] = []
    for n in range(2, 8):
        base = prime_power_base(n)
        if base is not None:
            contributing.append((n, base))
    assert contributing == [(2, 2), (3, 3), (4, 2), (5, 5), (7, 7)]

    term_records: list[dict[str, object]] = []
    prime_sum_low = Fraction(0)
    prime_sum_high = Fraction(0)
    for n, p in contributing:
        log_n_low, log_n_high = log_integer_bounds(n)
        r_low = Fraction(1) - log_n_high
        r_high = Fraction(1) - log_n_low
        min_abs, max_abs = absolute_interval(r_low, r_high)

        if max_abs + epsilon >= 1:
            kernel_low = Fraction(0)
        else:
            kernel_low = (
                finite_G(max_abs + epsilon, coefficients)
                / g_zero_upper
            )
        kernel_high = (
            finite_G(max(min_abs - epsilon, Fraction(0)), coefficients)
            / g_zero_lower
        )

        log_p_low, log_p_high = log_integer_bounds(p)
        sqrt_n_low, sqrt_n_high = sqrt_integer_bounds(n)
        coefficient_low = log_p_low / sqrt_n_high
        coefficient_high = log_p_high / sqrt_n_low
        term_low = coefficient_low * kernel_low
        term_high = coefficient_high * kernel_high
        prime_sum_low += term_low
        prime_sum_high += term_high
        term_records.append(
            {
                "n": n,
                "p": p,
                "coefficient": rational_record(
                    coefficient_low, coefficient_high
                ),
                "abs_2y_minus_log_n": rational_record(
                    min_abs, max_abs
                ),
                "K_h": rational_record(kernel_low, kernel_high),
                "term": rational_record(term_low, term_high),
            }
        )

    interaction_low = main_low - prime_sum_high
    interaction_high = main_high - prime_sum_low
    assert interaction_low > 0

    exact_digest_input = "|".join(
        [
            str(interaction_low.numerator),
            str(interaction_low.denominator),
            str(interaction_high.numerator),
            str(interaction_high.denominator),
        ]
    ).encode("ascii")

    certificate = {
        "claim": "I_h(1/2) > 0 for the frozen infinite-convolution packet",
        "certified": True,
        "sign": "positive",
        "y": "1/2",
        "arithmetic": "exact fractions; no floating point",
        "finite_uniform_factors": N_FACTORS,
        "omitted_G_tail_support_radius": rational_record(
            epsilon, epsilon
        ),
        "endpoint_audit": {
            "strict_x_window": "1 < x < exp(2)",
            "exp_2": rational_record(exp_two_low, exp_two_high),
            "proof_consequence": "7 < exp(2) < 8",
            "prime_powers_in_window": [
                {"n": n, "p": p} for n, p in contributing
            ],
            "endpoint_weight": (
                "full prime-power atoms; K_h(+-1)=0, so equality "
                "would contribute zero and receives no half weight"
            ),
        },
        "G_infinite_at_zero": rational_record(
            g_zero_lower, g_zero_upper
        ),
        "M_h_squared": rational_record(
            mh_squared_low, mh_squared_high
        ),
        "continuous_main_exp_y_M_h_squared": rational_record(
            main_low, main_high
        ),
        "prime_power_terms": term_records,
        "prime_power_sum": rational_record(
            prime_sum_low, prime_sum_high
        ),
        "I_h_y": rational_record(
            interaction_low, interaction_high
        ),
        "short_enclosure": {
            "lower": outward_decimal(
                interaction_low, 12, upward=False
            ),
            "upper": outward_decimal(
                interaction_high, 12, upward=True
            ),
        },
        "exact_endpoint_sha256": hashlib.sha256(
            exact_digest_input
        ).hexdigest(),
        "proof_dependencies": [
            "the exact nonuniform B-spline density formula for G_N",
            "symmetric log-concavity of G_N, hence radial monotonicity",
            (
                "the omitted two-copy convolution is a probability "
                "measure supported in [-2^-N,2^-N]"
            ),
            "log(sinh(x)/x) <= x^2/6",
            "positive Taylor-series remainder bounds encoded in this file",
        ],
    }

    output = REPOSITORY_ROOT / "certificates" / "implementation_a"
    output.mkdir(parents=True, exist_ok=True)
    with (output / "certificate_y_half.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(certificate, handle, indent=2)
        handle.write("\n")
    print(
        "CERTIFIED I_h(1/2) in "
        f"[{certificate['short_enclosure']['lower']}, "
        f"{certificate['short_enclosure']['upper']}]"
    )


if __name__ == "__main__":
    main()
