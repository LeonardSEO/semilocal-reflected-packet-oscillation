# B. INFINITE OSCILLATION THEOREM

## 1. Statement

Adopt without alteration the conventions and packet in
`FROZEN_SPECIFICATION.md`. In particular,

\[
h=\frac g{\|g\|_2},\qquad
g=*_{n\ge1}\frac1{2a_n}\mathbf 1_{[-a_n,a_n]},
\qquad a_n=2^{-n-1},
\]

\[
K_h=h*h,\qquad
L_h(w):=\mathcal L K_h(w)
=\int_{-1}^{1}K_h(r)e^{wr}\,dr,
\]

and

\[
dE=\sum_{n\ge2}\Lambda(n)\delta_n-dx.
\]

To avoid colliding with the zero coefficient \(A_h(\rho)\), denote the
archimedean cross term called \(A_h(y)\) in the frozen specification by
\(A_h^\infty(y)\) in this theorem.

For \(y>1/2\), put

\[
\mathcal I_h(y)
=-\int_0^\infty
x^{-1/2}K_h(2y-\log x)\,dE(x)
\tag{1.1}
\]

and

\[
\Delta_h(y)
=\mathfrak q[h_y^+]-\mathfrak q[h_y^-].
\tag{1.2}
\]

Let \(\rho\) range over the distinct nontrivial zeros of \(\zeta\), and
let \(m_\rho\) be the multiplicity of \(\rho\).

### Theorem

For every \(y>1/2\):

1. The exact arithmetic interaction is

   \[
   \boxed{
   \mathcal I_h(y)
   =
   \sum_\rho
   m_\rho L_h\!\left(\rho-\frac12\right)
   e^{2(\rho-1/2)y}
   +
   \sum_{n=1}^\infty
   L_h\!\left(2n+\frac12\right)e^{-(4n+1)y}.
   }
   \tag{1.3}
   \]

2. The archimedean and remaining pole terms cancel the second series:

   \[
   \boxed{
   A_h^\infty(y)+e^{-y}M_h^2
   =
   -\sum_{n=1}^\infty
   L_h\!\left(2n+\frac12\right)e^{-(4n+1)y}.
   }
   \tag{1.4}
   \]

3. Hence the cross term and energy splitting are

   \[
   \boxed{
   Q_h(y):=\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
   =
   \sum_\rho
   m_\rho L_h\!\left(\rho-\frac12\right)
   e^{2(\rho-1/2)y},
   }
   \tag{1.5}
   \]

   \[
   \boxed{\Delta_h(y)=2Q_h(y).}
   \tag{1.6}
   \]

   Direct substitution into the frozen Fourier--Mellin convention may
   present (1.5) with \(e^{-2(\rho-1/2)y}\). The two presentations are
   identical: reindex the full zero multiset by
   \(\rho\mapsto1-\rho\), use preservation of multiplicity, and use the
   evenness of \(L_h\).

4. Every series in (1.3)--(1.5) is absolutely convergent. The
   nontrivial-zero series and all of its real derivatives converge locally
   uniformly in \(y\).

5. The exact nontrivial-zero coefficient is

   \[
   \boxed{
   A_h(\rho)=m_\rho L_h\!\left(\rho-\frac12\right).
   }
   \tag{1.7}
   \]

   It vanishes exactly when

   \[
   \boxed{
   \rho=\frac12+4\pi ik,\qquad
   k\in\mathbb Z\setminus\{0\}.
   }
   \tag{1.8}
   \]

6. Unconditionally, both \(\mathcal I_h\) and \(\Delta_h\) take strictly
   positive and strictly negative values arbitrarily far to the right:

   \[
   \boxed{
   \begin{aligned}
   &\forall Y>0\ \exists y_+,y_->Y:
   &&\mathcal I_h(y_+)>0,\quad \mathcal I_h(y_-)<0,\\
   &\forall Y>0\ \exists u_+,u_->Y:
   &&\Delta_h(u_+)>0,\quad \Delta_h(u_-)<0.
   \end{aligned}
   }
   \tag{1.9}
   \]

   Therefore each function changes sign across infinitely many disjoint
   intervals and has infinitely many distinct zeros separating
   opposite-sign values.

No Riemann hypothesis, zero-simplicity assumption, linear-independence
assumption, Weil positivity assertion, or numerical zero verification is
used.

The sign interpretation is exact:

- \(\Delta_h(y)<0\): the normalized even packet has lower energy;
- \(\Delta_h(y)>0\): the normalized odd packet has lower energy.

Thus each parity is favored along an unbounded sequence of separations.
This theorem concerns the one frozen packet only and says nothing about
actual ground states.

## 2. Polarization and the exact prime--pole cancellation

Because the preform is Hermitian and antilinear in its first argument,

\[
\begin{aligned}
\mathfrak q[h_y^+]
&=\frac12\bigl(
\mathfrak q[h_y^{\mathrm R}]
+\mathfrak q[h_y^{\mathrm L}]
\bigr)
+\Re\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}),\\
\mathfrak q[h_y^-]
&=\frac12\bigl(
\mathfrak q[h_y^{\mathrm R}]
+\mathfrak q[h_y^{\mathrm L}]
\bigr)
-\Re\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
\end{aligned}
\]

The cross term is real by inversion symmetry, so

\[
\Delta_h(y)=2Q_h(y).
\tag{2.1}
\]

For \(y>1/2\), the exact sector calculation in the frozen specification is

\[
Q_h(y)
=A_h^\infty(y)+M_h^2(e^y+e^{-y})
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
K_h(2y-\log n).
\tag{2.2}
\]

All prime powers are present through \(\Lambda(n)\). The support of \(K_h\)
reduces this to the strict window

\[
e^{2y-1}<n<e^{2y+1}.
\]

The equality cases have \(K_h(\pm1)=0\), not a half weight.

The continuous main term is

\[
\begin{aligned}
\int_0^\infty
x^{-1/2}K_h(2y-\log x)\,dx
&=e^y\int_{-1}^{1}K_h(r)e^{-r/2}\,dr\\
&=e^y
\left(\int h(x)e^{x/2}\,dx\right)
\left(\int h(x)e^{-x/2}\,dx\right)\\
&=e^yM_h^2.
\end{aligned}
\tag{2.3}
\]

Here evenness of \(h\) was used in the last equality. Since
\(dE=d\Psi-dx\), equations (1.1), (2.2), and (2.3) give

\[
Q_h(y)=A_h^\infty(y)+e^{-y}M_h^2+\mathcal I_h(y).
\tag{2.4}
\]

This proves the exact factor and sign before any transform is used.

## 3. Canonical bilateral transform

The uncut Mellin transform of \(dE\) is not defined in any right
half-plane because \(dE=-dx\) on \((0,1)\). For the transform only, define
the canonical base-\(1\) extension

\[
J_h(t)
:=-\int_{[1,\infty)}
x^{-1/2}K_h(t-\log x)\,dE(x).
\tag{3.1}
\]

The endpoint normalization in this formula is load-bearing.  With

\[
E_0(x)=\psi(x)-x,\qquad
E_1(x)=\psi(x)-(x-1)=E_0(x)+1\quad(x\ge1),
\]

one has \(E_0(1)=-1\), \(E_1(1)=0\), and, distributionally,

\[
d\!\left(\mathbf 1_{[1,\infty)}E_0\right)
=\mathbf 1_{[1,\infty)}\,dE-\delta_1,
\qquad
d\!\left(\mathbf 1_{[1,\infty)}E_1\right)
=\mathbf 1_{[1,\infty)}\,dE.
\tag{3.1a}
\]

Thus (3.1) is the cutoff defined by \(E_1\), not the discontinuous cutoff
of \(E_0\); in particular it contains no spurious boundary term
\(K_h(t)\).

It has two exact properties:

\[
J_h(t)=0\quad(t\le-1),
\qquad
J_h(t)=\mathcal I_h(t/2)\quad(t>1).
\tag{3.2}
\]

The second equality follows because
\(K_h(t-\log x)\ne0\) and \(t>1\) imply \(x>1\).

Let \(s=\sigma+i\tau\), \(\sigma>1/2\). Using
\(|dE|\le d\Psi+dx\), Tonelli gives

\[
\begin{aligned}
\int_{\mathbb R}e^{-\sigma t}|J_h(t)|\,dt
&\le
L_h(\sigma)
\left[
\sum_{n\ge2}\frac{\Lambda(n)}{n^{\sigma+1/2}}
+\int_1^\infty x^{-\sigma-1/2}\,dx
\right]
<\infty.
\end{aligned}
\tag{3.3}
\]

Fubini and the frozen Mellin identity now yield

\[
\boxed{
\mathscr B_h(s)
:=\int_{\mathbb R}J_h(t)e^{-st}\,dt
=L_h(s)
\left[
\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
+\frac1{s-\frac12}
\right],
\qquad \Re s>\frac12.
}
\tag{3.4}
\]

This is the canonical initial half-plane furnished by absolute Euler
product convergence. The bilateral transform itself depends on how
values for \(t\le1\) are extended; equation (3.1) is the frozen canonical
choice. The physical values for \(t>1\), and hence every conclusion for
\(y>1/2\), are independent of that choice.

At \(s=1/2\),

\[
\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
=-\frac1{s-1/2}+\gamma_E+O(s-1/2),
\]

so the apparent pole cancels and

\[
\mathscr B_h(1/2)=\gamma_E L_h(1/2)=\gamma_E M_h^2.
\tag{3.5}
\]

All other poles arise at

\[
s=\rho-\frac12
\quad\text{and}\quad
s=-2n-\frac12\ (n\ge1).
\tag{3.6}
\]

The residue at a nontrivial zero \(\rho\) is

\[
m_\rho L_h(\rho-1/2),
\tag{3.7}
\]

and the residue at a trivial zero \(-2n\) is

\[
L_h(-2n-1/2).
\tag{3.8}
\]

A multiple nontrivial zero changes only the residue through
\(m_\rho\); it produces no derivative term.

## 4. Rigorous inversion and explicit formula

For \(c>1/2\), Fourier inversion on the line \(\Re s=c\) gives

\[
J_h(t)
=\frac1{2\pi i}
\int_{c-i\infty}^{c+i\infty}
e^{st}L_h(s)
\left[
\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
+\frac1{s-\frac12}
\right]ds.
\tag{4.1}
\]

The integral is absolutely convergent in the vertical variable: on that
line the logarithmic derivative is bounded by its absolutely convergent
Dirichlet series, whereas

\[
L_h(c+i\tau)=O_N((1+|\tau|)^{-N})
\tag{4.2}
\]

for every \(N\).

To shift the contour, choose heights \(T_j\to\infty\) with distance
\(\gg1/\log T_j\) from every zero ordinate. Such heights exist by the
Riemann--von Mangoldt bound in unit intervals. On each horizontal segment
in a fixed vertical strip,

\[
\frac{\zeta'}{\zeta}(\sigma+iT_j)=O(\log^2T_j).
\tag{4.3}
\]

Equation (4.2), uniformly in fixed vertical strips, makes both horizontal
integrals tend to zero.

Shift first to

\[
\Re s=-2N-1.
\]

This line lies between shifted trivial-zero poles. The crossed residues are
the nontrivial zeros and the first \(N\) trivial zeros. The functional
equation gives, on the new line,

\[
\left|
\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)
+\frac1{s-\frac12}
\right|
\le C\log(N+|\Im s|+2).
\tag{4.4}
\]

Since \(K_h\) has support \([-1,1]\), repeated integration by parts gives,
for every \(M\ge3\),

\[
|L_h(-2N-1+i\tau)|
\le C_M e^{2N+1}(1+N)^M(1+|\tau|)^{-M}.
\tag{4.5}
\]

The remaining vertical integral is therefore

\[
O_{h,M}\!\left(
e^{-(2N+1)(t-1)}
(1+N)^M\log(N+2)
\right),
\tag{4.6}
\]

which tends to zero for \(t>1\). This proves

\[
\begin{aligned}
J_h(t)
={}&
\sum_\rho
m_\rho L_h\!\left(\rho-\frac12\right)
e^{(\rho-1/2)t}\\
&+
\sum_{n=1}^\infty
L_h\!\left(-2n-\frac12\right)
e^{(-2n-1/2)t},
\qquad t>1.
\end{aligned}
\tag{4.7}
\]

Because \(L_h\) is even, setting \(t=2y\) gives (1.3).

The trivial-zero series is absolutely convergent for \(t>1\), since

\[
|L_h(-2n-1/2)|
\le
e^{2n+1/2}\int_{-1}^{1}K_h(r)\,dr.
\tag{4.8}
\]

For nontrivial zeros, uniformly for \(|\sigma|\le1/2\),

\[
L_h(\sigma+i\tau)=O_N((1+|\tau|)^{-N}).
\tag{4.9}
\]

Together with \(N_\zeta(T)=O(T\log T)\), this proves absolute convergence
of the zero sum and local uniform convergence after any fixed number of
real derivatives.

## 5. Exact archimedean--trivial-zero cancellation

For \(y>1/2\), the reflected cross correlation obeys

\[
C(r)=K_h(r+2y),\qquad
C(r)=0\ (r\ge0),\qquad
C(-r)=K_h(2y-r)\ (r\ge0).
\]

The frozen physical real-place formula therefore gives

\[
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}
K_h(2y-r)\,dr.
\tag{5.1}
\]

For \(r>0\),

\[
\frac{e^{r/2}}{e^r-e^{-r}}
=\sum_{n=0}^\infty e^{-(2n+1/2)r}.
\tag{5.2}
\]

All terms are nonnegative, so Tonelli applies. Substituting
\(u=2y-r\) gives

\[
A_h^\infty(y)
=-\sum_{n=0}^\infty
L_h\!\left(2n+\frac12\right)e^{-(4n+1)y}.
\tag{5.3}
\]

The \(n=0\) term equals

\[
-L_h(1/2)e^{-y}=-M_h^2e^{-y}.
\]

This proves (1.4). Combining (1.3), (1.4), and (2.4) proves
(1.5)--(1.6). It also reconstructs the complete Weil explicit formula
without leaving any gamma, pole, or trivial-zero term implicit.

## 6. Exact coefficient visibility

The frozen packet product gives

\[
L_h(w)
=c_g^{-2}
\prod_{n\ge1}
\left(
\frac{\sinh(2^{-n-1}w)}{2^{-n-1}w}
\right)^2.
\tag{6.1}
\]

The factor indexed by \(n\) vanishes exactly when

\[
w=\pi i\ell\,2^{n+1},\qquad
\ell\in\mathbb Z\setminus\{0\}.
\]

There are no additional infinite-product zeros. Indeed, uniformly on
every compact \(w\)-set,

\[
\frac{\sinh(a_nw)}{a_nw}=1+O(a_n^2),
\qquad
\sum_{n\ge1}a_n^2<\infty.
\]

Thus, away from the zeros of the finitely many initial factors, the tail
product converges locally uniformly to a nowhere-zero holomorphic
function. Taking the union of the factor zeros over \(n\ge1\) therefore
proves

\[
Z(L_h)=4\pi i\mathbb Z\setminus\{0\}.
\tag{6.2}
\]

At \(4\pi ik\), exactly

\[
v_2(|k|)+1
\]

unsquared factors vanish, so the order in \(L_h\) is

\[
2\bigl(v_2(|k|)+1\bigr).
\tag{6.3}
\]

Equations (3.7) and (6.2) prove (1.7)--(1.8). In particular every
off-critical-line zero is visible. A critical-line zero is invisible only
if its ordinate belongs to \(4\pi\mathbb Z\setminus\{0\}\).

Conrey's primary theorem proves that at least two fifths of all
nontrivial zeros, asymptotically relative to \(N(T)\), are simple and on
the critical line. There are only

\[
\left\lfloor\frac{T}{4\pi}\right\rfloor=O(T)
\]

positive invisible lattice ordinates below \(T\), while

\[
N(T)\sim\frac{T}{2\pi}\log\frac{T}{2\pi e}.
\]

Because the counted zeros are simple, at most one can occupy each lattice
ordinate. Hence infinitely many, indeed a positive proportion, of
Conrey's critical-line zeros are visible for this packet. This establishes
the nonvanishing input used below without a numerical zero certificate.

## 7. Landau lemma

We use the following elementary Laplace-transform version of Landau's
oscillation theorem.

### Lemma

Let \(T_0\ge0\), and let
\(f:[T_0,\infty)\to[0,\infty)\) be locally integrable. Assume its
Laplace integral converges on a nonempty right half-line, and let

\[
F(s)=\int_{T_0}^\infty f(t)e^{-st}\,dt
\]

and let

\[
\sigma_c
=\inf\left\{
\sigma\in\mathbb R:
\int_{T_0}^\infty f(t)e^{-\sigma t}\,dt<\infty
\right\}.
\]

If \(\sigma_c\) is finite, then \(F\) is singular at the real point
\(s=\sigma_c\).

### Proof

Assume instead that \(F\) is holomorphic in a neighborhood of
\(\sigma_c\). Choose a real \(\sigma_1>\sigma_c\) so close to
\(\sigma_c\) that the Taylor disk about \(\sigma_1\) extends to a real
point \(\sigma_1-r<\sigma_c\) while remaining in the union of that
neighborhood and the half-plane \(\Re s>\sigma_c\). Choose
\(\varepsilon>0\) with \(\sigma_1-\varepsilon>\sigma_c\). Then
\(t^n\le C_{n,\varepsilon}e^{\varepsilon t}\), so differentiation under
the integral is justified and, for every \(n\ge0\),

\[
(-1)^nF^{(n)}(\sigma_1)
=\int_{T_0}^\infty t^nf(t)e^{-\sigma_1t}\,dt\ge0.
\]

Taylor's formula and monotone convergence give

\[
\begin{aligned}
F(\sigma_1-r)
&=\sum_{n=0}^\infty
\frac{(-r)^nF^{(n)}(\sigma_1)}{n!}\\
&=\int_{T_0}^\infty
f(t)e^{-\sigma_1t}
\sum_{n=0}^\infty\frac{(rt)^n}{n!}\,dt\\
&=\int_{T_0}^\infty
f(t)e^{-(\sigma_1-r)t}\,dt<\infty.
\end{aligned}
\]

This contradicts the definition of \(\sigma_c\). \(\square\)

The same lemma applies to an eventually nonnegative function after
discarding a finite initial interval. That discard changes its Laplace
transform by an entire function.

## 8. Unconditional oscillation of the arithmetic interaction

The canonical transform (3.4) extends meromorphically to the plane. At
every visible critical-line zero

\[
\rho=\frac12+i\gamma
\]

it has a genuine pole at

\[
s=i\gamma.
\tag{8.1}
\]

Conrey's theorem and Section 6 supply infinitely many such poles
unconditionally.

The direct finite-window formula also supplies the needed tail growth and
Laplace-convergence bound without using the zero expansion.  For
\(t>1\),

\[
\left|\mathcal I_h(t/2)\right|
\le M_h^2e^{t/2}
+\|K_h\|_\infty e^{-(t-1)/2}
\sum_{n\le e^{t+1}}\Lambda(n)
=O_h\!\left((1+t)e^{t/2}\right),
\tag{8.2}
\]

where the elementary bound
\(\sum_{n\le X}\Lambda(n)\le X\log X\) is sufficient.

Suppose \(\mathcal I_h(t/2)\) were eventually nonnegative. Its tail
Laplace transform differs from (3.4) by an entire function. Let
\(\sigma_c\) be its real abscissa of convergence. Equation (3.3) gives

\[
\sigma_c\le\frac12.
\tag{8.3}
\]

A pole (8.1) rules out \(\sigma_c<0\), since in that case the defining
Laplace integral would be holomorphic in a half-plane containing
\(i\gamma\). On the overlap \(\Re s>1/2\), that integral equals (3.4);
the identity theorem would therefore make the displayed pole removable,
a contradiction. The pole also rules out \(\sigma_c=-\infty\). Hence

\[
0\le\sigma_c\le\frac12.
\tag{8.4}
\]

But the right-hand side of (3.4) is holomorphic at every real
\(s\in[0,1/2]\):

- at \(s=1/2\), the zeta pole cancels by (3.5);
- for \(0\le s<1/2\), the real number \(s+1/2\) lies in
  \([1/2,1)\), where \(\zeta\) has no zero.

For completeness, the latter follows from

\[
\zeta(u)=\frac{\eta(u)}{1-2^{1-u}},
\qquad 0<u<1,
\]

where the alternating Dirichlet series \(\eta(u)>0\) and the denominator
is negative.

Thus the transform is holomorphic at the real point \(\sigma_c\),
contradicting the Landau lemma. Eventual nonnegativity is impossible.
Applying the same argument to \(-\mathcal I_h(t/2)\) excludes eventual
nonpositivity.

It follows that \(\mathcal I_h\) takes both strict signs beyond every
bound.

## 9. Unconditional oscillation of the full splitting

Set \(t=2y\) and

\[
\mathcal Q_h(t)=Q_h(t/2).
\]

From (1.5),

\[
\mathcal Q_h(t)
=\sum_\rho
a_\rho e^{(\rho-1/2)t},
\qquad
a_\rho=m_\rho L_h(\rho-1/2).
\tag{9.1}
\]

It is of exponential order independently of this series: by (2.4),
the estimate (8.2), the factor \(e^{-t/2}M_h^2\), and the rapid decay of
\(A_h^\infty(t/2)\) give

\[
\mathcal Q_h(t)=O_h\!\left((1+t)e^{t/2}\right)
\qquad(t>1).
\tag{9.2}
\]

For \(\Re s>1/2\), termwise integration on any tail
\([T_0,\infty)\) gives

\[
\int_{T_0}^\infty
\mathcal Q_h(t)e^{-st}\,dt
=
\sum_\rho
\frac{
a_\rho e^{(\rho-1/2-s)T_0}
}{
s-(\rho-1/2)
}.
\tag{9.3}
\]

Rapid coefficient decay makes the right-hand side normally convergent
on compact subsets away from its displayed poles, so it is a meromorphic
continuation to the plane. At every visible critical-line zero it has a
genuine nonreal pole \(s=i\gamma\). It has no real pole.

If \(\mathcal Q_h\), or its negative, were eventually nonnegative, the
identical Landau argument would put its finite real abscissa in
\([0,1/2]\) and simultaneously require and exclude a singularity there.
Here again, the identity theorem identifies the defining tail transform
with (9.3) on their common half-plane, so a visible pole cannot disappear
in a larger convergence half-plane.
Thus \(Q_h\) takes both signs arbitrarily far out. By
\(\Delta_h=2Q_h\), the same is true of the energy splitting.

Both functions are continuous. Recursively choosing alternating positive
and negative points beyond increasing bounds produces infinitely many
pairwise disjoint intervals whose endpoints have opposite signs. The
intermediate value theorem gives at least one distinct zero in each.

This does not assert that those zeros are simple, transverse, or isolated.

## 10. Conditional scale audit

The theorem above is unconditional. The following statements only locate
the usual conditional regimes:

- Under RH,

  \[
  Q_h(y)
  =2\sum_{\gamma>0}
  m_\gamma L_h(i\gamma)\cos(2\gamma y),
  \]

  with absolute and uniform convergence. It is a nonzero, mean-zero
  Bohr almost-periodic function. No simplicity or ordinate-independence
  hypothesis is needed for this representation.

- If a visible rightmost real part
  \(\beta_0>1/2\) is attained and is separated from all remaining visible
  real parts, then the natural leading scale is
  \(e^{2(\beta_0-1/2)y}\). Zeros sharing \(\beta_0\) form an exponential
  trigonometric sum; one isolated formal zero term is not enough to infer
  its sign.

- Without RH or an attained rightmost real part, there is no canonical
  further exponential normalization. The \(n^{-1/2}\) centering and the
  exact prime--pole subtraction in (1.1) are the unconditional natural
  normalization.

## 11. Scope and no-go corollary

For this frozen nondegenerate packet, neither parity can be eventually
preferred:

\[
\Delta_h(y)\le0\quad\text{for all large }y
\]

and

\[
\Delta_h(y)\ge0\quad\text{for all large }y
\]

are both false.

This is a fixed-packet no-go theorem inside the stronger unconditional
oscillation theorem. It does not imply compactness or noncompactness of
semilocal ground states. Reopening a ground-state argument would require
uniform control over a packet class and over the magnitude of the
splitting, neither of which is proved here.

## 12. Primary references

1. A. Connes and C. Consani,
   [*Spectral triples and \(\zeta\)-cycles*](https://doi.org/10.4171/LEM/1049),
   Enseign. Math. 69 (2023), 93--148, especially §2.1 and
   Proposition 2.1.
2. A. Connes, C. Consani, and H. Moscovici,
   [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755),
   arXiv:2511.22755, especially §§2--3.
3. J. B. Conrey,
   [*More than two fifths of the zeros of the Riemann zeta function are
   on the critical line*](https://doi.org/10.1515/crll.1989.399.1),
   J. Reine Angew. Math. 399 (1989), 1--26, Theorem 1.

The Landau lemma needed here is proved in Section 7, so no unverified
oscillation theorem is imported.
