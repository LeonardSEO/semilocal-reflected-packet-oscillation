# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mpmath==1.4.1",
#   "numpy==2.0.2",
#   "scipy==1.13.1",
# ]
# ///
"""Independent implementation B for the frozen reflected-packet interaction.

This program deliberately uses two different numerical representations:

* the explicit-formula side uses mpmath zeta zeros and the bilateral-Laplace
  infinite product for L K_h;
* the prime-power side uses an Eratosthenes sieve and a vector-valued
  Gauss--Kronrod Fourier inversion of the autocorrelation kernel.

The program is diagnostic.  The analytic product-tail and Fourier-tail bounds
printed in the JSON output are proved bounds.  QUADPACK's quadrature error and
the omitted nontrivial-zero tail are explicitly labelled non-certified.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np
from scipy.integrate import quad_vec

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


PI = math.pi


def a_n(n: int) -> mp.mpf:
    if n < 1:
        raise ValueError("n starts at 1")
    return mp.power(2, -n - 1)


def lk_product_tail_relative_bound(w_abs: mp.mpf, terms: int) -> mp.mpf:
    """Rigorous relative bound for the omitted L K_h product.

    If q_n = sinh(a_n w)/(a_n w), then

        |prod_{n>N} q_n^2 - 1|
        <= exp(|w|^2 exp(|w| a_{N+1}) 4^(-N-1) / 9) - 1.

    This follows from |sinh(z)/z - 1| <= |z|^2 exp(|z|)/6 and
    sum_{n>N} a_n^2 = 4^(-N-1)/3.
    """

    exponent = (
        w_abs**2
        * mp.exp(w_abs * a_n(terms + 1))
        * mp.power(4, -terms - 1)
        / 9
    )
    return mp.expm1(exponent)


def lk_unnormalized(w: mp.mpc, terms: int) -> mp.mpc:
    result = mp.mpc(1)
    for n in range(1, terms + 1):
        z = a_n(n) * w
        factor = mp.mpc(1) if z == 0 else mp.sinh(z) / z
        result *= factor * factor
    return result


def lk(w: mp.mpc, cg2: mp.mpf, terms: int) -> mp.mpc:
    return lk_unnormalized(w, terms) / cg2


def finite_fourier_product(t: float, terms: int) -> float:
    """Return prod_{n<=N} sinc(a_n t)^2 in double precision."""

    result = 1.0
    for n in range(1, terms + 1):
        # numpy.sinc(x) = sin(pi*x)/(pi*x).
        result *= float(np.sinc(math.ldexp(t, -n - 1) / PI)) ** 2
    return result


def fourier_high_tail_bound(cutoff: float, moment_order: int) -> float:
    """Rigorous bound for (1/pi) int_T^infty |g_hat(t)|^2 dt.

    Frozen specification (3.4) gives
      |g_hat(t)| <= 2^(M(M+3)/2) |t|^-M.
    """

    m = moment_order
    return (
        2.0 ** (m * (m + 3))
        / (PI * (2 * m - 1) * cutoff ** (2 * m - 1))
    )


def finite_product_integral_error_bound(cutoff: float, terms: int) -> float:
    """Rigorous absolute error from replacing the infinite sinc product.

    For the omitted real factors, sinc(x)^2 >= 1-x^2/3 when the omitted
    arguments have modulus below sqrt(6).  Integrating the resulting uniform
    bound gives T^3 4^(-N-1)/(27*pi).
    """

    first_omitted_argument = cutoff * math.ldexp(1.0, -terms - 2)
    if first_omitted_argument >= math.sqrt(6.0):
        raise ValueError("increase Fourier product terms")
    return cutoff**3 * 4.0 ** (-terms - 1) / (27.0 * PI)


@dataclass(frozen=True)
class KernelBatch:
    cg2: float
    cg2_quadrature_error: float
    analytic_product_error: float
    analytic_high_tail_error: float
    normalized_values: list[float]
    normalized_error_budget: float


def kernel_batch(
    shifts: Iterable[float],
    *,
    cutoff: float,
    terms: int,
    moment_order: int,
    epsabs: float,
    epsrel: float,
) -> KernelBatch:
    """Evaluate K_h at many shifts by one vector Fourier inversion."""

    shifts_array = np.asarray([0.0, *shifts], dtype=float)

    def integrand(t: float) -> np.ndarray:
        return finite_fourier_product(t, terms) * np.cos(shifts_array * t)

    # The first factor has zeros at 4*pi*Z.  Supplying them as break points
    # makes the quadrature reproducible and avoids accidental under-resolution.
    points = np.arange(4.0 * PI, cutoff, 4.0 * PI).tolist()
    integrals, quad_error = quad_vec(
        integrand,
        0.0,
        cutoff,
        epsabs=epsabs,
        epsrel=epsrel,
        points=points,
        limit=max(1000, 8 * len(points)),
        norm="max",
    )
    raw = np.asarray(integrals, dtype=float) / PI
    quad_error = float(quad_error) / PI
    product_error = finite_product_integral_error_bound(cutoff, terms)
    high_tail_error = fourier_high_tail_bound(cutoff, moment_order)
    absolute_raw_error = quad_error + product_error + high_tail_error

    cg2 = float(raw[0])
    if not (cg2 - absolute_raw_error > 0):
        raise ArithmeticError("normalization enclosure crossed zero")
    normalized = raw[1:] / cg2

    # If |A-A0|, |B-B0| <= e and B0-e>0, then
    # |A/B-A0/B0| <= e/(B0-e) + |A0|e/(B0(B0-e)).
    max_raw = float(max(1.0, np.max(np.abs(raw[1:]), initial=0.0)))
    normalized_error = (
        absolute_raw_error / (cg2 - absolute_raw_error)
        + max_raw
        * absolute_raw_error
        / (cg2 * (cg2 - absolute_raw_error))
    )
    return KernelBatch(
        cg2=cg2,
        cg2_quadrature_error=quad_error,
        analytic_product_error=product_error,
        analytic_high_tail_error=high_tail_error,
        normalized_values=[float(x) for x in normalized],
        normalized_error_budget=float(normalized_error),
    )


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


@dataclass(frozen=True)
class PrimePower:
    p: int
    m: int
    value: int
    log_value: float
    weight: float
    shift: float


def prime_powers_in_window(t: float) -> list[PrimePower]:
    lower = math.exp(t - 1.0)
    upper = math.exp(t + 1.0)
    result: list[PrimePower] = []
    for p in primes_up_to(math.floor(upper)):
        value = p
        m = 1
        while value <= upper:
            if value > lower:
                log_value = m * math.log(p)
                shift = t - log_value
                # Strict support.  Floating-point fuzz only filters values that
                # are numerically outside; exact endpoints have K_h=0 anyway.
                if abs(shift) < 1.0:
                    result.append(
                        PrimePower(
                            p=p,
                            m=m,
                            value=value,
                            log_value=log_value,
                            weight=math.log(p) / math.sqrt(value),
                            shift=shift,
                        )
                    )
            if value > math.floor(upper) // p:
                break
            value *= p
            m += 1
    result.sort(key=lambda item: (item.value, item.p, item.m))
    return result


def trivial_tail_bound(t: float, terms: int) -> float:
    """Rigorous tail bound using c_g^-2<=1 and supp(K_h)=[-1,1]."""

    if t <= 1.0:
        raise ValueError("trivial-zero tail bound requires t>1")
    decay = t - 1.0
    first_a = 2.0 * (terms + 1) + 0.5
    return math.exp(-first_a * decay) / (1.0 - math.exp(-2.0 * decay))


def stringify_mpf(x: mp.mpf | mp.mpc, digits: int = 35) -> str:
    if isinstance(x, mp.mpc):
        real = mp.nstr(x.real, digits)
        imag = mp.nstr(abs(x.imag), digits)
        sign = "+" if x.imag >= 0 else "-"
        return f"{real}{sign}{imag}j"
    return mp.nstr(x, digits)


def compute(args: argparse.Namespace) -> dict:
    mp.mp.dps = args.dps
    y_values = [mp.mpf(token) for token in args.y]
    t_values = [2 * y for y in y_values]
    all_prime_powers = [prime_powers_in_window(float(t)) for t in t_values]
    all_shifts = [pp.shift for group in all_prime_powers for pp in group]

    kernel = kernel_batch(
        all_shifts,
        cutoff=args.fourier_cutoff,
        terms=args.fourier_terms,
        moment_order=args.tail_moment,
        epsabs=args.quad_epsabs,
        epsrel=args.quad_epsrel,
    )
    cg2 = mp.mpf(str(kernel.cg2))
    shift_values = iter(kernel.normalized_values)

    # Cache the positive zeros and their frozen transform coefficients once.
    zeros: list[mp.mpc] = []
    zero_coefficients: list[mp.mpc] = []
    zero_product_tail_bounds: list[mp.mpf] = []
    for index in range(1, args.zeros + 1):
        rho = mp.zetazero(index)
        w = rho - mp.mpf("0.5")
        zeros.append(rho)
        zero_coefficients.append(lk(w, cg2, args.product_terms))
        zero_product_tail_bounds.append(
            lk_product_tail_relative_bound(abs(w), args.product_terms)
        )

    results = []
    for y, t, powers in zip(y_values, t_values, all_prime_powers):
        contributions = []
        prime_sum = mp.mpf(0)
        for pp in powers:
            kval = mp.mpf(str(next(shift_values)))
            contribution = mp.mpf(str(pp.weight)) * kval
            prime_sum += contribution
            contributions.append(
                {
                    **asdict(pp),
                    "K_h": stringify_mpf(kval),
                    "contribution": stringify_mpf(contribution),
                }
            )

        m2 = lk(mp.mpf("0.5"), cg2, args.product_terms).real
        main_term = mp.exp(t / 2) * m2
        direct = main_term - prime_sum
        raw_normalization_error = (
            kernel.cg2_quadrature_error
            + kernel.analytic_product_error
            + kernel.analytic_high_tail_error
        )
        unnormalized_m2 = lk_unnormalized(
            mp.mpf("0.5"), args.product_terms
        ).real
        unnormalized_m2_error = abs(unnormalized_m2) * (
            lk_product_tail_relative_bound(
                mp.mpf("0.5"), args.product_terms
            )
        )
        cg2_lower = cg2 - raw_normalization_error
        m2_error_budget = (
            unnormalized_m2_error / cg2_lower
            + abs(unnormalized_m2)
            * raw_normalization_error
            / (cg2 * cg2_lower)
        )
        direct_error_budget = (
            mp.exp(t / 2) * m2_error_budget
            + mp.fsum(mp.mpf(str(pp.weight)) for pp in powers)
            * kernel.normalized_error_budget
        )

        nontrivial = mp.mpf(0)
        for rho, coefficient in zip(zeros, zero_coefficients):
            nontrivial += 2 * mp.re(
                coefficient * mp.exp((rho - mp.mpf("0.5")) * t)
            )

        trivial = mp.mpf(0)
        trivial_terms = []
        for k in range(1, args.trivial_terms + 1):
            w = -2 * k - mp.mpf("0.5")
            coefficient = lk(w, cg2, args.product_terms).real
            term = coefficient * mp.exp(w * t)
            trivial += term
            trivial_terms.append(
                {
                    "k": k,
                    "w": stringify_mpf(w),
                    "coefficient": stringify_mpf(coefficient),
                    "term": stringify_mpf(term),
                    "product_tail_relative_bound": stringify_mpf(
                        lk_product_tail_relative_bound(
                            abs(w), args.product_terms
                        )
                    ),
                }
            )

        explicit = nontrivial + trivial
        zero_cutoff_sensitivity = {}
        for cutoff_count in args.zero_sensitivity:
            if cutoff_count > len(zeros):
                continue
            partial = mp.fsum(
                2
                * mp.re(
                    coefficient
                    * mp.exp((rho - mp.mpf("0.5")) * t)
                )
                for rho, coefficient in zip(
                    zeros[:cutoff_count], zero_coefficients[:cutoff_count]
                )
            )
            zero_cutoff_sensitivity[str(cutoff_count)] = stringify_mpf(
                partial + trivial
            )

        results.append(
            {
                "y": stringify_mpf(y),
                "t_equals_2y": stringify_mpf(t),
                "prime_power_count": len(powers),
                "prime_powers": contributions,
                "M_h_squared": stringify_mpf(m2),
                "continuous_main": stringify_mpf(main_term),
                "prime_power_sum": stringify_mpf(prime_sum),
                "I_direct_prime_stieltjes": stringify_mpf(direct),
                "I_direct_numerical_error_budget": stringify_mpf(
                    direct_error_budget
                ),
                "I_direct_error_budget_status": (
                    "analytic truncation tails plus QUADPACK error estimate; "
                    "not an interval certificate"
                ),
                "nontrivial_zero_sum": stringify_mpf(nontrivial),
                "trivial_zero_sum": stringify_mpf(trivial),
                "I_truncated_explicit_formula": stringify_mpf(explicit),
                "direct_minus_explicit": stringify_mpf(direct - explicit),
                "trivial_zero_omission_bound": trivial_tail_bound(
                    float(t), args.trivial_terms
                ),
                "nontrivial_zero_omission_status": (
                    "not certified; cutoff sensitivity is diagnostic only"
                ),
                "zero_cutoff_sensitivity": zero_cutoff_sensitivity,
                "trivial_terms": trivial_terms,
            }
        )

    zero_table = []
    for index, (rho, coefficient, tail) in enumerate(
        zip(zeros, zero_coefficients, zero_product_tail_bounds), start=1
    ):
        zero_table.append(
            {
                "index": index,
                "rho": stringify_mpf(rho),
                "coefficient": stringify_mpf(coefficient),
                "coefficient_abs": stringify_mpf(abs(coefficient)),
                "product_tail_relative_bound": stringify_mpf(tail),
            }
        )

    return {
        "implementation": "numerical_b",
        "status": (
            "diagnostic; analytic product and Fourier tails tracked, "
            "nontrivial-zero omission not certified"
        ),
        "frozen_conventions": {
            "fourier": "hat f(t)=integral f(x) exp(-i t x) dx",
            "packet": "a_n=2^(-n-1), h=g/||g||_2",
            "kernel": "K_h=h*h, support [-1,1]",
            "interaction": (
                "I_h(y)=exp(y) M_h^2-sum_{p,m} "
                "(log p) p^(-m/2) K_h(2y-m log p)"
            ),
            "explicit_formula_used": (
                "I_h(y)=sum_rho L_K(rho-1/2) exp(2y(rho-1/2))"
                "+sum_{k>=1} L_K(-2k-1/2) exp(-2y(2k+1/2))"
            ),
        },
        "parameters": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "kernel_normalization": asdict(kernel),
        "normalization_sanity": {
            "K_h_0_from_ratio": 1.0,
            "rigorous_coarse_cg2_bounds": [1.0, 2.0],
            "reason": (
                "support length one and integral one give ||g||_2^2>=1; "
                "convolution with b_(1/4) gives ||g||_infinity<=2"
            ),
        },
        "zero_coefficients": zero_table,
        "results": results,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--y", nargs="+", default=["1.25", "1.75", "2.25"])
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--zeros", type=int, default=80)
    parser.add_argument(
        "--zero-sensitivity", nargs="+", type=int, default=[10, 20, 40, 80]
    )
    parser.add_argument("--trivial-terms", type=int, default=18)
    parser.add_argument("--product-terms", type=int, default=55)
    parser.add_argument("--fourier-terms", type=int, default=42)
    parser.add_argument("--fourier-cutoff", type=float, default=500.0)
    parser.add_argument("--tail-moment", type=int, default=7)
    parser.add_argument("--quad-epsabs", type=float, default=2e-12)
    parser.add_argument("--quad-epsrel", type=float, default=2e-12)
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            REPOSITORY_ROOT
            / "certificates"
            / "implementation_b"
            / "explicit_formula_b_output.json"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = compute(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(args.output)


if __name__ == "__main__":
    main()
