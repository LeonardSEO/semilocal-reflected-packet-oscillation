# Numerical implementation A: direct prime-power interaction

This directory is an independent direct-side implementation of the immutable
specification in
[`../../research/FROZEN_SPECIFICATION.md`](../../research/FROZEN_SPECIFICATION.md).
It does not use
zeros of zeta and it does not use files from any earlier numerical route.

## What is computed

`direct_interaction.py` constructs the first $N$ factors of the frozen
infinite convolution.  If

```math
g_N=*_{n=1}^{N}b_{2^{-n-1}},\qquad G_N=g_N*g_N,
```

then the code evaluates $G_N$ from the exact nonuniform B-spline identity

```math
G_N(x)=
\frac{2^{N(N+1)}}{(2N-1)!}
\sum_{k_1,\ldots,k_N\in\{0,1,2\}}
(-1)^{\sum k_i}\prod_i {2\choose k_i}
\left(x+1-2^{-N}-\sum_i k_i2^{-i}\right)_+^{2N-1}.
```

The implementation aggregates the finite-difference coefficients and uses
prefix moments, so a whole prime-power grid is evaluated in one pass.

The two omitted packet tails give an omitted autocorrelation shift supported
in $[-\varepsilon_N,\varepsilon_N]$, where
$\varepsilon_N=2^{-N}$.  Symmetry and log-concavity give

```math
G_N(|r|+\varepsilon_N)\le G(r)
\le G_N(\max(|r|-\varepsilon_N,0))
```

and

```math
G_N(\varepsilon_N)\le G(0)\le G_N(0).
```

These inequalities produce the reported `K_tail_low/high` and
`I_tail_low/high`.  The displayed values use 80-digit Decimal arithmetic;
those bounds track the analytic truncation but are not called formal
interval certificates because Decimal operations are not directed here.

Every $p^m$ in the strict support window

```math
|2y-\log(p^m)|<1
```

is included with coefficient $\log(p)/\sqrt{p^m}$.  Equality is zero
because $K_h(\pm1)=0$, and no half weight is used.

The default grid is
```math
y\in\{0.5,1,1.25,1.5,1.75,2,2.25,2.5,3,3.5,4\}.
```
The three quarter-offset values are shared with the independent
`code/implementation_b` implementation.

The archimedean cross term is computed independently from

```math
A_h(y)=-
\int_{-1}^{1}
\frac{e^{(2y-u)/2}}{e^{2y-u}-e^{-2y+u}}K_h(u)\,du .
```

Two Gauss-Legendre orders are compared.  Consequently `Delta_center` is a
diagnostic, not a proof.

## Exact finite certificate

No Arb or python-flint installation was present in the environment.  The
companion `certify_y_half.py` therefore uses the stronger fallback of exact
Python rational arithmetic.  It certifies one value of the *infinite*
packet, not merely the $N=8$ truncation:

```math
\mathcal I_h(1/2)\in
[0.063637725597,\;0.088006928482],
```

so $\mathcal I_h(1/2)>0$.

The enclosure accounts for:

- the full omitted infinite-convolution tail;
- rigorous positive-series bounds for logarithms, exponentials, and
  $\sinh(x)/x$;
- dyadic rational square-root enclosures;
- all prime powers in $1<x<e^2$, namely $2,3,4,5,7$;
- the full endpoint convention.

The exact rational endpoints (including their full numerators and
denominators) are written to `outputs/certificate_y_half.json`.

## Reproduction

From the project root:

```sh
python3 code/implementation_a/direct_interaction.py
python3 code/implementation_a/certify_y_half.py
python3 code/implementation_a/direct_interaction.py --factors 12 --precision 70 --quadrature-order 128 --output-dir certificates/implementation_a/n12
python3 code/implementation_a/direct_interaction.py --factors 16 --precision 90 --quadrature-order 256 --output-dir certificates/implementation_a/n16
python3 code/implementation_a/compare_refinement.py
python3 code/implementation_a/compare_numerical_b.py
```

The diagnostic run requires the already-installed SciPy package only for
Gauss-Legendre nodes.  The exact certificate uses only the Python standard
library.

Generated files:

- `certificates/implementation_a/n14/grid.json`
- `certificates/implementation_a/n14/prime_power_contributions.csv`
- `certificates/implementation_a/n14/metadata.json`
- `certificates/implementation_a/certificate_y_half.json`
- `certificates/implementation_a/refinement.json`
- `certificates/implementation_a/crosscheck_numerical_b.json`
- `certificates/implementation_a/n12/*` and
  `certificates/implementation_a/n16/*`

The cross-check script does not alter either numerical method.  It compares
the physical B-spline value here with implementation B's sinc-product
Fourier-inversion value.  Its combined budget is A's analytic omitted-tail
radius plus B's stated quadrature/tail budget.  Both implementations clearly
label their numerical integration/rounding budgets as non-interval
diagnostics.

These finite calculations are diagnostic.  They do not prove an eventual
sign or infinitely many sign changes.
