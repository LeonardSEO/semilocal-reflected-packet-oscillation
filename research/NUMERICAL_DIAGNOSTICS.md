# Numerical diagnostics and finite certificates

None of the results in this file is used in the proof of
`MAIN_THEOREM.md`.

## Independent implementations

### Implementation A

`code/implementation_a/direct_interaction.py` constructs finite dyadic convolutions
through an exact nonuniform B-spline identity. It evaluates the physical
Stieltjes expression

\[
\mathcal I_h(y)
=e^yM_h^2-
\sum_{|2y-\log(p^m)|<1}
\frac{\log p}{p^{m/2}}K_h(2y-m\log p).
\]

The omitted convolution tail is bounded analytically. Decimal evaluation
is nondirected, so the main grid is diagnostic.

`code/implementation_a/certify_y_half.py` separately uses exact rational arithmetic
and outward analytic bounds to certify

\[
0.063637725597
<
\mathcal I_h(1/2)
<
0.088006928482.
\]

It includes exactly \(2,3,4,5,7\), the prime powers in
\(1<n<e^2\), and accounts for the infinite packet tail. This finite
certificate is explicitly non-load-bearing.

### Implementation B

`code/implementation_b/explicit_formula_b.py` is independent of A. It evaluates
\(K_h\) by Fourier inversion of the sinc product on the direct side, and
uses the bilateral-Laplace infinite product and zeta zeros on the explicit
side.

`code/implementation_b/certify_coefficients_arb.py` uses 220-bit Arb balls to
certify nonvanishing of the frozen transform coefficient at zero indices
1, 2, and 4. The infinite product tail and a coarse positive
normalization interval are included. The omitted nontrivial-zero sum is
not certified.

## Cross-implementation comparison

After A was completed independently, it was evaluated at B's three
separations. Prime-power counts agree exactly.

| \(y\) | Prime powers | \(|\mathcal I_A-\mathcal I_B|\) | Combined stated budget |
|---:|---:|---:|---:|
| 1.25 | 15 | \(5.13\times10^{-13}\) | \(1.07\times10^{-4}\) |
| 1.75 | 26 | \(8.25\times10^{-12}\) | \(1.84\times10^{-4}\) |
| 2.25 | 50 | \(1.32\times10^{-11}\) | \(3.01\times10^{-4}\) |

For A, the discrepancy from B decreases at every shared point along the
factor refinement \(N=12,14,16\).

Within B, the direct prime-power value minus the 80-zero/trivial-zero
explicit value is respectively

\[
8.11\times10^{-14},\qquad
3.95\times10^{-14},\qquad
2.43\times10^{-15}.
\]

Those differences do not certify the omitted nontrivial-zero tail.

## Verification replay

The following checks were rerun successfully on 2026-07-23:

- five structural unit tests for implementation B;
- implementation-B output verifier;
- every checksum in the repository-level `SHA256SUMS`;
- all three 220-bit Arb coefficient certificates;
- implementation-A exact-rational certificate;
- implementation-A/B cross-comparison;
- Python compilation of all implementation-A scripts.

## Logical scope

The unconditional nonvanishing used by the analytic theorem comes from:

1. the exact product zero set
   \(Z(\mathcal L K_h)=4\pi i\mathbb Z\setminus\{0\}\); and
2. Conrey's theorem giving a positive proportion of simple
   critical-line zeros.

It does not come from the finite Arb calculations.
