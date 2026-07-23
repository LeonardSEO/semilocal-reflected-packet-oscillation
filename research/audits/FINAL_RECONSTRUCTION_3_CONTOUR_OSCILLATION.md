# Final reconstruction 3: contour formula and infinite oscillation

Date: 2026-07-23  
Scope: independent reconstruction from `FROZEN_SPECIFICATION.md` of the
canonical extension, its contour formula, the full archimedean
cancellation, and the Landau oscillation theorem.

## Verdict

**PASS after proof-completion edits, with no change to the theorem,
coefficient, sign, or classification.**

The following assertions in `MAIN_THEOREM.md` survive reconstruction:

```math
\mathcal I_h(y)
=
\sum_\rho m_\rho L_h(\rho-\tfrac12)e^{2(\rho-1/2)y}
+
\sum_{n\ge1}L_h(2n+\tfrac12)e^{-(4n+1)y},
```

```math
\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
=
\sum_\rho m_\rho L_h(\rho-\tfrac12)e^{2(\rho-1/2)y},
\qquad
\Delta_h(y)=2\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}),
```

and both $\mathcal I_h$ and $\Delta_h$ take both strict signs beyond
every finite bound, unconditionally.

I found no hidden use of RH, global simplicity, linear independence,
computed zero ordinates, Weil positivity, or an assumed sign.

## 1. Endpoint-normalized canonical extension

Let

```math
dE=d\Psi-dx,\qquad
d\Psi=\sum_{n\ge2}\Lambda(n)\delta_n.
```

There are two cumulative functions relevant at the base point $1$:

```math
E_0(x)=\psi(x)-x,\qquad E_0(1)=-1,
```

```math
E_1(x)=\psi(x)-(x-1)=E_0(x)+1,\qquad E_1(1)=0.
```

Consequently,

```math
d(\mathbf 1_{[1,\infty)}E_0)
=\mathbf 1_{[1,\infty)}dE-\delta_1,
```

whereas

```math
d(\mathbf 1_{[1,\infty)}E_1)
=\mathbf 1_{[1,\infty)}dE.
```

Thus the correct restricted measure has no atom at $1$. This excludes a
spurious $K_h(t)$ term in the logarithmic variable.

Define

```math
J_h(t)
=-\int_{[1,\infty)}
x^{-1/2}K_h(t-\log x)\,dE(x).
```

Equivalently, with

```math
d\nu_+(r)=
\sum_{n\ge2}\Lambda(n)n^{-1/2}\delta_{\log n}(r)
-\mathbf 1_{[0,\infty)}(r)e^{r/2}\,dr,
```

one has $J_h=-K_h*\nu_+$. Since
$\operatorname{supp}K_h=[-1,1]$ and
$\operatorname{supp}\nu_+\subset[0,\infty)$,

```math
J_h(t)=0\quad(t\le-1).
```

At $t=-1$, the only possible contact is the non-atomic point $r=0$,
and $K_h(-1)=0$.

For $t>1$, the support condition
$\lvert t-\log x\rvert<1$ forces $x>1$, so

```math
J_h(t)=\mathcal I_h(t/2).
```

This proves that the canonical extension agrees with every physical value
used in the theorem.

## 2. Bilateral transform

For $\Re s>1/2$, Tonelli applies because

```math
\int_{\mathbb R}e^{-\Re(s)t}|J_h(t)|\,dt
\le
L_h(\Re s)
\left(
\sum_{n\ge2}\Lambda(n)n^{-\Re(s)-1/2}
+\frac1{\Re(s)-1/2}
\right).
```

For fixed $x$, the substitution $u=t-\log x$ gives

```math
\int_{\mathbb R}K_h(t-\log x)e^{-st}\,dt
=x^{-s}L_h(-s)=x^{-s}L_h(s),
```

using the evenness of $L_h$. Hence

```math
\begin{aligned}
\mathscr B_h(s)
&=\int_{\mathbb R}J_h(t)e^{-st}\,dt\\
&=-L_h(s)
\left(
\sum_{n\ge2}\Lambda(n)n^{-s-1/2}
-\int_1^\infty x^{-s-1/2}\,dx
\right)\\
&=
L_h(s)
\left[
\frac{\zeta'}{\zeta}(s+\tfrac12)
+\frac1{s-\tfrac12}
\right].
\end{aligned}
```

Since

```math
\frac{\zeta'}{\zeta}(1+\varepsilon)
=-\varepsilon^{-1}+\gamma_E+O(\varepsilon),
```

the point $s=1/2$ is removable, with value

```math
\mathscr B_h(1/2)=\gamma_E L_h(1/2).
```

At a distinct nontrivial zero $\rho$ of multiplicity $m_\rho$,

```math
\operatorname*{Res}_{s=\rho-1/2}\mathscr B_h(s)
=m_\rho L_h(\rho-\tfrac12).
```

At the simple trivial zero $-2n$,

```math
\operatorname*{Res}_{s=-2n-1/2}\mathscr B_h(s)
=L_h(-2n-\tfrac12).
```

Multiple nontrivial zeros therefore contribute their multiplicity only;
there are no derivative terms.

## 3. Bromwich inversion and contour errors

On any line $\Re s=c>1/2$,

```math
L_h(c+i\tau)=O_{h,M}((1+|\tau|)^{-M})
```

for every $M$, while the bracket in the transform is bounded by its
absolutely convergent Dirichlet series. Both the weighted function
$e^{-ct}J_h(t)$ and its Fourier transform are integrable, so ordinary
Fourier inversion yields

```math
J_h(t)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
e^{st}\mathscr B_h(s)\,ds.
```

For fixed $N$, shift to $\Re s=-2N-1$. Choose heights $T_j$ a
distance $\gg1/\log T_j$ from every zero ordinate. The
Riemann--von Mangoldt estimate supplies such heights, and the standard
partial-fraction estimate gives, in the fixed strip,

```math
\frac{\zeta'}{\zeta}(\sigma+iT_j)=O_N(\log^2T_j).
```

The rapid vertical decay of $L_h$ makes the horizontal integrals tend
to zero.

On the new vertical line, the functional equation and the absolutely
convergent logarithmic derivative at the reflected point give

```math
\left|
\frac{\zeta'}{\zeta}(s+\tfrac12)+\frac1{s-\tfrac12}
\right|
\ll\log(N+|\Im s|+2).
```

Repeated integration by parts in

```math
L_h(s)=\int_{-1}^{1}K_h(r)e^{sr}\,dr
```

has no endpoint terms because $K_h\in C_c^\infty$, and gives

```math
|L_h(-2N-1+i\tau)|
\ll_{h,M}
e^{2N+1}(1+N)^M(1+|\tau|)^{-M}.
```

Therefore the left-line remainder is

```math
O_{h,M}\!\left(
e^{-(2N+1)(t-1)}
(1+N)^M\log(N+2)
\right).
```

It tends to zero exactly in the required physical range $t>1$.
Letting first the height and then $N$ tend to infinity gives

```math
J_h(t)
=
\sum_\rho
m_\rho L_h(\rho-\tfrac12)e^{(\rho-1/2)t}
+
\sum_{n\ge1}
L_h(-2n-\tfrac12)e^{(-2n-1/2)t}.
```

For the nontrivial zeros,

```math
L_h(\sigma+i\tau)=O_{h,M}((1+|\tau|)^{-M})
\quad(|\sigma|\le1/2).
```

Together with $N_\zeta(T)=O(T\log T)$, this proves absolute locally
uniform convergence, including after any fixed number of real
derivatives. The trivial-zero series converges for $t>1$ because

```math
|L_h(-2n-\tfrac12)|
\le
e^{2n+1/2}\|K_h\|_1.
```

Putting $t=2y$ and using evenness of $L_h$ proves the asserted formula
for $\mathcal I_h(y)$.

## 4. Exact archimedean cancellation

For the reflected pair,

```math
C(r)=K_h(r+2y),\qquad C(r)=0\ (r\ge0),\qquad
C(-r)=K_h(2y-r).
```

Since $C(0)=0$, the scalar term in $W_{\mathbb R}$ vanishes and

```math
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}K_h(2y-r)\,dr.
```

For $r>0$,

```math
\frac{e^{r/2}}{e^r-e^{-r}}
=\sum_{n\ge0}e^{-(2n+1/2)r}.
```

The summands are nonnegative, so Tonelli and $u=2y-r$ give

```math
A_h^\infty(y)
=-\sum_{n\ge0}
L_h(2n+\tfrac12)e^{-(4n+1)y}.
```

Moreover,

```math
L_h(1/2)
=
\left(\int h(x)e^{x/2}\,dx\right)
\left(\int h(x)e^{-x/2}\,dx\right)
=M_h^2
```

by evenness of $h$. Thus the $n=0$ term cancels
$e^{-y}M_h^2$, and the remaining terms cancel every trivial-zero
residue. Combining this with

```math
Q_h(y)=A_h^\infty(y)+e^{-y}M_h^2+\mathcal I_h(y)
```

gives

```math
Q_h(y)
=\sum_\rho m_\rho L_h(\rho-\tfrac12)e^{2(\rho-1/2)y}.
```

Finally, Hermitian polarization and inversion symmetry give the exact
factor and sign

```math
\Delta_h(y)=2Q_h(y).
```

## 5. Visible critical zeros

The frozen product is

```math
L_h(w)=c_g^{-2}\prod_{n\ge1}
\left(\frac{\sinh(2^{-n-1}w)}{2^{-n-1}w}\right)^2.
```

Its exact zero set is

```math
4\pi i\mathbb Z\setminus\{0\}.
```

Thus a critical-line zero is invisible exactly at an ordinate
$\gamma=4\pi k$, while every off-line zero is visible.

Conrey's Theorem 1 proves

```math
\kappa^*\ge0.401,
```

so at least two fifths of the nontrivial zeros are simple and on the
critical line. Up to height $T$ this gives $\gg T\log T$ distinct
simple critical zeros. Only $O(T)$ lattice ordinates $4\pi k$ occur
in the same range. Since a simple zero occupies at most one such
ordinate, infinitely many critical zeros satisfy

```math
L_h(i\gamma)\ne0.
```

Consequently the canonical transform has infinitely many genuine poles
at $s=i\gamma$, without any numerical zero input.

## 6. Landau-abscissa argument for $\mathcal I_h$

The direct finite-window formula gives, for $t>1$,

```math
|\mathcal I_h(t/2)|
\le
M_h^2e^{t/2}
+\|K_h\|_\infty e^{-(t-1)/2}
\sum_{n\le e^{t+1}}\Lambda(n)
=O_h((1+t)e^{t/2}).
```

Thus the function is of exponential order.

Suppose its tail were nonnegative. Let $\sigma_c$ be the real abscissa
of its tail Laplace transform. Absolute convergence in the initial
half-plane gives

```math
\sigma_c\le1/2.
```

A visible pole at $i\gamma$ implies $\sigma_c\ge0$: otherwise the
defining integral would be holomorphic in a half-plane containing
$i\gamma$, and the identity theorem would contradict that pole.

The meromorphic continuation is holomorphic at every real
$s\in[0,1/2]$. At $1/2$ the pole is removable. For
$0\le s<1/2$, the point $u=s+1/2$ lies in $[1/2,1)$, where

```math
\zeta(u)=\frac{\eta(u)}{1-2^{1-u}}\ne0.
```

Here $\eta(u)>0$, while the denominator is negative.

The elementary Landau lemma now contradicts eventual nonnegativity:
the Laplace transform of a nonnegative tail must be singular at its real
abscissa of convergence. Applying the same argument to the negative
excludes eventual nonpositivity. Hence $\mathcal I_h$ takes both strict
signs beyond every bound.

## 7. Landau-abscissa argument for the full splitting

Set $\mathcal Q_h(t)=Q_h(t/2)$. Absolute convergence gives

```math
\mathcal Q_h(t)=
\sum_\rho a_\rho e^{(\rho-1/2)t},
\qquad
a_\rho=m_\rho L_h(\rho-\tfrac12).
```

For $\Re s>1/2$, its tail transform is

```math
\int_{T_0}^\infty\mathcal Q_h(t)e^{-st}\,dt
=
\sum_\rho
\frac{a_\rho e^{(\rho-1/2-s)T_0}}
{s-(\rho-1/2)}.
```

Rapid coefficient decay makes this series normally convergent away from
its displayed poles. It has a genuine pole at every visible
critical-line zero and no real pole. Also,

```math
\mathcal Q_h(t)=O_h((1+t)e^{t/2})
```

from the direct identity
$Q_h=A_h^\infty+e^{-t/2}M_h^2+\mathcal I_h$.

The same Landau argument therefore excludes both eventual signs for
$\mathcal Q_h$. Since $\Delta_h=2Q_h$, the splitting takes both
strict signs arbitrarily far out. Continuity supplies infinitely many
distinct zeros between recursively chosen alternating-sign points.

The result does not imply simple or transverse zeros.

## 8. Proof-completion patch applied

Three details were valid but previously compressed:

1. `MAIN_THEOREM.md` now explicitly records the $E_0/E_1$ distributional
   cutoff identities and the absence of a boundary $\delta_1$.
2. It now derives an elementary exponential-order bound for
   $\mathcal I_h(t/2)$ and $Q_h(t/2)$, directly verifying the required
   nonempty Laplace-convergence half-line independently of the zero
   formula.
3. It explicitly points to the convergence margin used to justify every
   derivative under the Laplace integral and correctly identifies the
   tail-transform formula when invoking the identity theorem.

These edits complete hypotheses; they do not modify any formula or
conclusion.

## 9. Final classification

The independently reconstructed result supports exactly:

**B. INFINITE OSCILLATION THEOREM.**
