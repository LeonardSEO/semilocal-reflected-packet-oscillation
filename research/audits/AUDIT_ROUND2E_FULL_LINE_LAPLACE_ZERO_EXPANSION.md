# Independent audit of Round 2E

Audit filed with the frozen reflected-packet project.

## Verdict

**PASS after one mandatory indexing clarification.** No sign, endpoint,
support, inversion, residue, remainder, or convergence error was found.

## Mandatory clarification: do not count multiplicities twice

Section 6 currently says that \(\rho\) ranges over the nontrivial zeros
"counted with multiplicity \(m_\rho\)," while (6.3), (7.1), and (7.6) also
insert the factor \(m_\rho\). Read literally, this counts a zero of order
\(m_\rho\) a total of \(m_\rho^2\) times.

Replace the opening sentence of Section 6 by

> Let \(\rho\) range over the **distinct** nontrivial zeros of
> \(\zeta\), and let \(m_\rho\) denote the multiplicity of \(\rho\).

Then the factors \(m_\rho\) in (6.1), (6.3), (6.5), (7.1), and (7.6) are
exactly correct. Alternatively, one may sum over the zero multiset and
delete every explicit \(m_\rho\), but the first convention is preferable.

## Endpoint and canonical-extension check

The restricted weighted logarithmic error measure is exactly

\[
 d\nu_+(r)
 =
 \sum_{n\ge2}\Lambda(n)n^{-1/2}\delta_{\log n}(r)
 -
 \mathbf 1_{[0,\infty)}(r)e^{r/2}\,dr.
\]

It has no atom at \(r=0\). With
\(E_0(x)=\psi(x)-x\), the right trace at \(x=1\) is \(-1\), hence

\[
 d(\mathbf1_{[1,\infty)}E_0)
 =
 \mathbf1_{[1,\infty)}dE-\delta_1.
\]

For \(E_1=E_0+1\), the right trace is zero and therefore

\[
 d(\mathbf1_{[1,\infty)}E_1)
 =
 \mathbf1_{[1,\infty)}dE.
\]

Thus the absence of a \(\delta_0\) term in (1.1) is correct.

Since \(\operatorname{supp}K\subset[-1,1]\) and
\(\operatorname{supp}\nu_+\subset[0,\infty)\),

\[
 \operatorname{supp}(K*\nu_+)\subset[-1,\infty).
\]

The claims at \(t=-1\) also hold: the only contact is the non-atomic point
\(r=0\), and every derivative of a \(C_c^\infty\) kernel vanishes at the
boundary of its support. If an alternative extension differs by a
distribution supported in \((-\infty,0]\), its convolution with \(K\) is
supported in \((-\infty,1]\). Hence the physical values for \(t>1\) are
extension-independent.

## Bilateral transform and inversion check

For \(\Re z>1/2\),

\[
\begin{aligned}
 D(z)
 &=
 \int e^{-zr}\,d\nu_+(r)\\
 &=
 \sum_{n\ge2}\Lambda(n)n^{-z-1/2}
 -
 \frac1{z-1/2}\\
 &=
 -\frac{\zeta'}{\zeta}\!\left(z+\frac12\right)
 -
 \frac1{z-1/2}.
\end{aligned}
\]

The signs are correct. At \(z=1/2\),
\(-\zeta'/\zeta(z+1/2)\) has residue \(+1\), so the displayed rational
term cancels it. With \(t=u+r\), the convolution transform is
\(H(z)D(z)\), not \(H(-z)D(z)\).

On \(\Re z=c>1/2\), every \(\tau\)-derivative of \(D(c+i\tau)\) is bounded
by absolute convergence of the differentiated Dirichlet series, while
\(H(c+i\tau)\) and all its derivatives are rapidly decreasing. Therefore
Fourier inversion of \(e^{-ct}J(t)\) gives exactly the upward-oriented
Bromwich integral (5.2), with the factor \(1/(2\pi i)\) and exponent
\(e^{zt}\) as written.

## Residue and remainder check

At a distinct nontrivial zero \(\rho\) of order \(m_\rho\),

\[
 \operatorname*{Res}_{z=\rho-1/2}D(z)=-m_\rho.
\]

At \(z=-2n-1/2\), the trivial zero is simple and the residue is \(-1\).
Shifting the upward line from \(c\) to \(-R\) therefore adds the residue
terms with exactly the negative coefficients displayed in (7.1).

For integral \(R\), \(s=1/2-R+i\tau\) stays away from the trivial zeros.
The functional equation gives

\[
 D(-R+i\tau)=O(\log(2+R+|\tau|)).
\]

Compact support of \(K\) gives, for any fixed sufficiently large \(N\),

\[
 H(-R+i\tau)
 =
 O_{K,N}\!\left(
 e^R(1+R)^N(1+|\tau|)^{-N}
 \right).
\]

Consequently the left-line integral is

\[
 O_{K,N}\!\left(
 e^{-R(t-1)}(1+R)^{N+1}
 \right),
\]

which tends to zero precisely for \(t>1\). The threshold agrees with the
right endpoint \(1\) of \(\operatorname{supp}K\).

## Series convergence and semilocal sign

The nontrivial zeros lie in a fixed real strip for
\(\rho-1/2\). Rapid vertical decay of \(H\), together with
\(N_\zeta(T)=O(T\log T)\), proves absolute locally uniform convergence of
the nontrivial-zero series and every real \(t\)-derivative. The estimate in
(7.6) follows after choosing the integration-by-parts order according to
\(k\) and \(M\).

For \(x=2n+1/2\),

\[
 |H(-x)|\le \|K\|_1e^x,
\]

so multiplication by \(e^{-xt}\) gives the exponentially summable factor
\(e^{-x(t-1)}\), proving (7.7) on \(t\ge1+\varepsilon\).

Finally, the frozen prime cross term is the negative \(d\Psi\)-pairing and
the growing pole cross term is the positive \(dx\)-pairing. Their combined
contribution is therefore \(-J(2y)\). Since every residue coefficient of
\(J\) in (7.1) is negative, its contribution to the semilocal form has the
positive algebraic sign in (8.2). The exponents

\[
 e^{2y(\rho-1/2)}=e^{(2\rho-1)y},
 \qquad
 e^{-2y(2n+1/2)}=e^{-(4n+1)y}
\]

are also correct.
