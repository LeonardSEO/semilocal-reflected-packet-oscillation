# Independent numerical diagnostics

These calculations test the frozen identities only. The proof of infinite
oscillation uses Conrey's analytic theorem and does not use any finite
numerical zero, interaction value, or coefficient certificate.

## Implementation A: direct packet and prime powers

Location: `code/implementation_a/`, with outputs in
`certificates/implementation_a/`.

Method:

- finite dyadic convolutions evaluated through an exact nonuniform
  B-spline finite-difference formula;
- analytic enclosures for the omitted infinite-convolution tail;
- direct enumeration of every $p^m$ in
  $|2y-\log(p^m)|<1$;
- separate real-place quadrature;
- exact rational arithmetic for one selected finite certificate.

The standard-library certificate proves

```math
\boxed{
0.063637725597
<
\mathcal I_h(1/2)
<
0.088006928482.
}
```

It includes every prime power in $1<p^m<e^2$:

```math
2,\ 3,\ 4,\ 5,\ 7.
```

The certificate is finite and non-load-bearing.

## Implementation B: Fourier/prime side and explicit-zero side

Location: `code/implementation_b/`, with outputs in
`certificates/implementation_b/`.

Independent representations:

- vector Gauss--Kronrod inversion of
  $\prod_n\operatorname{sinc}^2(a_nt)$ followed by the direct
  all-prime-power sum;
- the product
  ```math
  L_h(w)=c_g^{-2}\prod_n
  \left(\frac{\sinh(a_nw)}{a_nw}\right)^2
  ```
  evaluated at zeta zeros, plus the trivial-zero series.

The 80-zero explicit sum and direct side differ by

| $y$ | all retained prime powers | direct minus truncated explicit |
|---:|---:|---:|
| 1.25 | 15 | $8.11\times10^{-14}$ |
| 1.75 | 26 | $3.95\times10^{-14}$ |
| 2.25 | 50 | $2.43\times10^{-15}$ |

The nontrivial-zero omission is not certified, so these agreements are
diagnostic.

At 220-bit Arb precision, the coefficient transforms at zero indices
1, 2, and 4 are certified strictly positive after enclosing both the
infinite product tail and the positive normalization. Those certificates
are also non-load-bearing because the theorem obtains visible zeros from
Conrey's result.

## Cross-implementation comparison

After both implementations were completed independently, implementation A
was evaluated at implementation B's three sample points.

| $y$ | prime powers | $|I_A-I_B|$ | combined stated budget |
|---:|---:|---:|---:|
| 1.25 | 15 | $5.13\times10^{-13}$ | $1.07\times10^{-4}$ |
| 1.75 | 26 | $8.25\times10^{-12}$ | $1.84\times10^{-4}$ |
| 2.25 | 50 | $1.32\times10^{-11}$ | $3.01\times10^{-4}$ |

Every prime-power count agrees. The A--B discrepancy decreases at all
three points as A is refined from 12 to 14 to 16 dyadic factors.

The combined budgets include nondirected Decimal and QUADPACK estimates;
they are not interval certificates.

## Reproduction checks completed

The following checks passed locally:

- all five implementation-B structural unit tests;
- implementation-B output verification;
- implementation-B SHA-256 manifest;
- the 220-bit Arb coefficient certificates;
- implementation-A exact-rational certificate;
- implementation-A/B cross-check;
- syntax compilation for all implementation-A scripts.

Exact commands are given in each implementation's `README.md`.
