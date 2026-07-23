# Final independent audit report

Date: 2026-07-23.

Principal classification:

\[
\boxed{\text{B. INFINITE OSCILLATION THEOREM}}
\]

This report records audit outcomes, not private deliberations. The
complete definitions and proof are in `FROZEN_SPECIFICATION.md` and
`MAIN_THEOREM.md`.

## 1. Frozen source gate

Every reconstruction used exactly the same:

- antilinear-first \(L^2(\mathbb R)\) inner product;
- Fourier transform
  \(\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx\);
- Mellin transform
  \(\widetilde f(s)=\int_0^\infty f(u)u^{s-1}\,du\);
- complete semilocal Weil preform, including both pole terms, the
  archimedean multiplier, and every coefficient
  \(-(\log p)p^{-m/2}\);
- full endpoint convention for \(p^m\le\lambda^2\);
- dyadic infinite-convolution packet
  \(h=\|g\|_2^{-1}g\), with
  \(g=*_{n\ge1}(2a_n)^{-1}\mathbf1_{[-a_n,a_n]}\) and
  \(a_n=2^{-n-1}\);
- all-prime-power error measure
  \(dE=\sum_{n\ge2}\Lambda(n)\delta_n-dx\).

No reconstruction altered the packet, normalization, endpoint
convention, or transform convention.

## 2. Six independent full-chain reconstructions

Six independent reconstructions each checked the entire load-bearing
chain rather than only one lemma.

| Reconstruction | Required scope | Verdict |
|---|---|---|
| R1 | physical semilocal sectors, prime--pole cancellation, contour residues, Landau step | PASS |
| R2 | archimedean distribution, trivial-zero cancellation, coefficient visibility, parity sign | PASS |
| R3 | Fourier-side zero expansion, product zero set, normal convergence, Landau abscissa | PASS after the \(T_0\ge0\) wording repair |
| R4 | translation phases, \(\rho\mapsto1-\rho\) reindexing, polarization, separate oscillation of \(\mathcal I_h\) and \(\Delta_h\) | PASS |
| R5 | Mellin contour, all-prime-power endpoint convention, Conrey visibility input, causal-transform cross-check | PASS |
| R6 | \(E_0/E_1\) endpoint distinction, extension independence, archimedean residues, Landau poles | PASS |

All six reproduced

\[
\mathcal I_h(y)
=
\sum_\rho m_\rho L_h(\rho-\tfrac12)e^{2(\rho-1/2)y}
+
\sum_{n\ge1}L_h(2n+\tfrac12)e^{-(4n+1)y},
\]

\[
A_h^\infty(y)+e^{-y}M_h^2
=-\sum_{n\ge1}L_h(2n+\tfrac12)e^{-(4n+1)y},
\]

and hence

\[
\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
=\sum_\rho m_\rho L_h(\rho-\tfrac12)e^{2(\rho-1/2)y},
\qquad
\Delta_h(y)=2\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
\]

The apparent alternative exponent
\(e^{-2(\rho-1/2)y}\) from direct Fourier substitution is identical
after reindexing the complete zero multiset by \(\rho\mapsto1-\rho\)
and using the evenness of \(L_h\).

## 3. Three required adversarial audits

At least three independent audits explicitly tested all five required
failure modes.

| Audit question | Result |
|---|---|
| Is RH assumed, directly or through a zero-location premise? | No |
| Is global zero simplicity assumed? | No; only Conrey's proved simple subset is selected |
| Is linear independence of zero ordinates assumed? | No |
| Is the desired sign or oscillation inserted into a hypothesis? | No |
| Is coefficient nonvanishing merely assumed? | No; the exact transform zero set is proved |
| Is Weil positivity used? | No |
| Are finite computed zeros load-bearing? | No |
| Are zeta zeros encoded in the packet or normalization? | No |
| Are primes substituted for prime powers? | No |
| Is ground-state, proxy, Galerkin, Robin, or determinant input used? | No |

Verdict: PASS in every independent circularity audit.

## 4. Corrections found during audit

The audit process found two presentational points, both repaired before
the final pass:

1. The elementary Landau lemma now states \(T_0\ge0\), which is exactly
   the case used after truncating beyond \(t>1\). Equivalently one may
   translate an arbitrary lower endpoint to zero.
2. The theorem explicitly explains why the positive- and
   negative-exponent zero expansions agree under
   \(\rho\mapsto1-\rho\).

The notation \(A_h^\infty(y)\) is used for the archimedean cross term in
the theorem so that it cannot be confused with the zero coefficient
\(A_h(\rho)\).

## 5. Numerical reproducibility audit

No finite computation is a premise of the analytic theorem. Thus there
is no load-bearing finite certificate. Nevertheless, two independent
implementations reproduce the finite diagnostics:

- Implementation A: finite dyadic convolutions/B-splines and direct
  all-prime-power summation.
- Implementation B: independent Fourier quadrature, infinite-product
  coefficients, and a truncated explicit-zero formula.

They agree at \(y=1.25,1.75,2.25\) to between
\(5.2\times10^{-13}\) and \(1.4\times10^{-11}\). Implementation B's
direct prime-power and truncated explicit-formula values differ by at
most \(8.2\times10^{-14}\) on those points. An Arb run at 220-bit
precision certifies nonzero positive intervals for the first, second,
and fourth selected critical-zero coefficients. These finite checks are
diagnostic only; the proof instead uses Conrey's unconditional theorem.

The exact commands, pinned versions, hashes, and JSON/CSV outputs are in
`NUMERICAL_RESULTS.md`, `../code/implementation_a/`, and
`../code/implementation_b/`.

## 6. Final logical status

The exact packet coefficient is

\[
A_h(\rho)=m_\rho L_h(\rho-\tfrac12),
\]

and it vanishes precisely at

\[
\rho=\frac12+4\pi ik,\qquad k\in\mathbb Z\setminus\{0\}.
\]

Conrey supplies \(\gg T\log T\) distinct simple critical-line zeros,
whereas the invisible lattice contributes only \(O(T)\) possible
ordinates. Hence visible nonreal transform poles exist unconditionally.
Landau's lemma then rules out either eventual sign, separately for
\(\mathcal I_h\) and for the full cross interaction. Consequently both
\(\mathcal I_h\) and \(\Delta_h\) assume both strict signs arbitrarily
far out.

The stopping condition is met. No RH, zero simplicity, ordinate
independence, or finite computation remains as an unresolved hypothesis.
