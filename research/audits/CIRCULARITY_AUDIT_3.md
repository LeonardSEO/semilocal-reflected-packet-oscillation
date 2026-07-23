# Independent source and circularity audit 3

Date: 2026-07-23

Audited files:

- `FROZEN_SPECIFICATION.md`
- `MAIN_THEOREM.md`
- `NUMERICAL_RESULTS.md`

## Verdict

**PASS.** I found no load-bearing normalization, prime-power, endpoint,
contour-sign, energy-sign, or circularity error. No repair to the theorem is
required.

The proof is unconditional in the stated sense. Its only non-elementary
zero-distribution input is Conrey's rigorous positive-proportion theorem for
simple critical-line zeros. It does not use RH, a table of zero ordinates,
finite numerical verification, global simplicity, or linear independence.

## 1. Primary semilocal normalization

The primary source is Connes--Consani, *Spectral triples and
\(\zeta\)-cycles*, equations (2.6)--(2.12), especially (2.8)--(2.11).
With its Fourier convention

\[
\widehat F(t)=\int_0^\infty F(u)u^{-it}\,d^*u,
\]

the source writes

\[
\operatorname{QW}(f,g)
=\widehat C(i/2)+\widehat C(-i/2)
-W_{\mathbb R}(C)-\sum_pW_p(C),
\qquad C=f^**g.
\]

It then defines \(W_1=-W_{\mathbb R}\) and gives

\[
W_1(C)
=\frac1{2\pi}\int_{\mathbb R}
2\theta'(t)\widehat C(t)\,dt.
\]

Since

\[
2\theta'(t)
=\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi,
\]

the positive Fourier-multiplier term in frozen equation (2.1), together
with the statement that its physical-space version is
\(-W_{\mathbb R}\), has the correct sign and scalar.

For the antilinear-first correlation

\[
C_{\Phi,\Psi}(r)
=\int\overline{\Phi(x-r)}\Psi(x)\,dx,
\]

direct Fourier transformation gives

\[
\widehat C_{\Phi,\Psi}(z)
=\overline{\widehat\Phi(\bar z)}\widehat\Psi(z).
\]

Thus the two frozen pole terms are exactly the sesquilinear extension of
\(\widehat C(i/2)+\widehat C(-i/2)\). No conjugation or \(2\pi\) factor is
missing.

## 2. Prime powers and endpoint convention

Source equation (2.6) is

\[
W_p(C)
=(\log p)\sum_{m\ge1}p^{-m/2}
\bigl(C(p^m)+C(p^{-m})\bigr).
\]

After logarithmic transport this is precisely

\[
-(\log p)p^{-m/2}
\bigl(C_{\Phi,\Psi}(m\log p)
     +C_{\Phi,\Psi}(-m\log p)\bigr)
\]

inside the quadratic form. Hence every \(p^m\), \(m\ge1\), occurs with

\[
-(\log p)p^{-m/2}
=-\Lambda(p^m)(p^m)^{-1/2}.
\]

Source equation (2.11) uses the inclusive finite sum

\[
1<n\le\lambda^2.
\]

There is no half weighting. At \(n=\lambda^2\), the shifted support
overlap is a null endpoint, so the corresponding \(L^2\) correlation
operator is zero. For the frozen smooth packet the sharper statement
\(K_h(\pm1)=0\) also makes the effective interaction window strict.

The definition

\[
dE=\sum_{n\ge2}\Lambda(n)\delta_n-dx
\]

is therefore exactly the all-prime-power Chebyshev measure
\(d\psi-dx\), with right-continuous/full endpoint convention. It is not
a primes-only \(\theta\)-measure.

## 3. Cross term, cancellation, and energy sign

For
\(\Phi=h_y^{\mathrm R}=h(\cdot-y)\) and
\(\Psi=h_y^{\mathrm L}=h(\cdot+y)\),

\[
C_{\Phi,\Psi}(r)=K_h(r+2y).
\]

Consequently the positive-shift prime term vanishes and the reflected
term is

\[
-\sum_{p,m}
\frac{\log p}{p^{m/2}}K_h(2y-m\log p).
\]

The pole cross term is

\[
M_h^2(e^y+e^{-y}),
\]

while

\[
\int_0^\infty x^{-1/2}K_h(2y-\log x)\,dx=e^yM_h^2.
\]

Thus the \(e^yM_h^2\) pole main term cancels with the continuous
prime-number main term with the sign displayed in the theorem.

The physical real-place distribution gives

\[
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}K_h(2y-r)\,dr
=-\sum_{n\ge0}
L_h\!\left(2n+\frac12\right)e^{-(4n+1)y}.
\]

The \(n=0\) term is \(-e^{-y}M_h^2\); the rest cancels the
trivial-zero residues. Therefore the full cross term is exactly the
nontrivial-zero series, with no hidden pole or gamma remainder.

Polarization gives

\[
\mathfrak q[h_y^+]-\mathfrak q[h_y^-]
=2\Re\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
\]

Inversion symmetry makes the cross term real, so the factor is \(2\).
Accordingly:

- \(\Delta_h<0\) means the even packet has lower energy;
- \(\Delta_h>0\) means the odd packet has lower energy.

## 4. Transform and contour audit

For the canonical base-\(1\) extension,

\[
\begin{aligned}
\mathscr B_h(s)
&=-L_h(s)\int_{[1,\infty)}x^{-s-1/2}\,dE(x)\\
&=L_h(s)\left[
\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
+\frac1{s-1/2}
\right],
\qquad \Re s>\frac12.
\end{aligned}
\]

The signs follow from the leading minus in \(J_h\) and from

\[
\int_{[1,\infty)}x^{-u}\,dE(x)
=-\frac{\zeta'}{\zeta}(u)-\frac1{u-1}.
\]

At \(s=1/2\), the pole of \(\zeta\) cancels. A zero of multiplicity
\(m_\rho\) gives residue

\[
m_\rho L_h(\rho-1/2),
\]

while a trivial zero \(-2n\) gives
\(L_h(-2n-1/2)\). These are the signs used in the explicit formula.

The contour shift is adequate:

- rapid vertical decay of \(L_h\) removes the horizontal segments;
- the functional equation controls \(\zeta'/\zeta\) on
  \(\Re s=-2N-1\);
- compact support of \(K_h\) gives the factor \(e^{2N+1}\);
- the remaining integral is
  \(O(e^{-(2N+1)(t-1)}\operatorname{poly}(N)\log N)\), which tends to
  zero exactly for the physical range \(t=2y>1\).

The zero series is absolutely and locally uniformly convergent because
\(L_h(\sigma+i\tau)\) decays faster than every power uniformly for
\(|\sigma|\le1/2\), while \(N_\zeta(T)=O(T\log T)\).

The possible exponent \(e^{-2(\rho-1/2)y}\) from the direct Fourier
presentation is not a sign discrepancy: reindexing by
\(\rho\mapsto1-\rho\) and using evenness of \(L_h\) gives the displayed
positive-exponent form.

## 5. Conrey input and coefficient visibility

Conrey's Theorem 1 states

\[
\kappa^*\ge0.401,
\]

and explicitly concludes that at least two fifths of all zeta zeros are
simple and on the critical line. This is stronger than the theorem's
stated input.

The packet transform has the independently derived exact zero set

\[
Z(L_h)=4\pi i\mathbb Z\setminus\{0\}.
\]

There are only \(O(T)\) such ordinates up to height \(T\). Conrey gives
\(\gg T\log T\) simple critical-line zeros; simplicity means that at most
one counted zero can occupy each invisible lattice point. It follows
without locating any individual zero that infinitely many critical-line
zeros are visible.

## 6. Circularity checklist

The load-bearing proof does **not** assume:

- RH or Weil positivity;
- global or eventual simplicity of zeta zeros;
- linear independence or phase equidistribution of ordinates;
- a desired sign or an oscillatory cosine heuristic;
- a finite zero table or a certified individual zero;
- numerical interaction values;
- identification of a semilocal ground state;
- determinant convergence.

The oscillation conclusion comes from the proved Laplace-form Landau
lemma. A visible nonreal pole forces the tail abscissa to be at least
zero, while absolute convergence makes it at most \(1/2\). The transform
is holomorphic on the real interval \([0,1/2]\), contradicting the real
singularity required for either an eventually nonnegative or eventually
nonpositive tail.

The packet does not contain zeta zeros. Its transform-zero lattice is
fixed arithmetically before applying Conrey's density theorem. The
normalization subtracts only the canonical continuous measure \(dx\),
not a zero sum or a desired oscillatory function.

## 7. Numerical independence

No equation in the analytic proof invokes the files in `numerical_a` or
`numerical_b`. The finite computations only check already-derived
identities and sample values. Removing every numerical artifact leaves
the statement and proof unchanged.

Conrey's published rigorous theorem is an analytic input, not a finite
verification of selected zeros. The proof uses only its asymptotic
counting conclusion.

## Minimal repairs

None.

