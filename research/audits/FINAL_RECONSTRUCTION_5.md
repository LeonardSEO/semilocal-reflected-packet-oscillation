# Fifth independent reconstruction and audit

Date: 2026-07-23

Verdict: **PASS**, after two standard one-sentence proof completions noted in
Section 10 below. Neither completion changes a formula, hypothesis, residue,
coefficient, or conclusion.

This reconstruction uses only `FROZEN_SPECIFICATION.md`, the displayed primary
Weil formulas, the elementary zeta identities recorded below, and Conrey's
primary Theorem 1. It does not use another agent's reconstruction or finite
zero data.

## 1. Primary normalization check

The source normalization is consistent with equations (3.7)--(3.11) and
(3.19) of Connes--Consani--Moscovici:

- the nonarchimedean distribution contains every $p^m$, with coefficient
  $(\log p)p^{-m/2}$;
- the Weil form subtracts that distribution;
- $W_{\mathbb R}=-W_\infty$, while the Weil form subtracts
  $W_{\mathbb R}$, hence the Fourier multiplier $2\theta'(t)$ enters with
  a plus sign;
- the $0,2$ term is the sum of the evaluations at $i/2$ and $-i/2$;
- the finite cutoff is $1<n\leq\lambda^2$.

Thus the frozen sesquilinear preform has the correct sector signs and has no
missing factor of $2$.

Primary checks:

- A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*,
  <https://arxiv.org/pdf/2511.22755>, equations (3.7)--(3.11), (3.19).
- J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
  function are on the critical line*,
  <https://aimath.org/~kaur/publications/24.pdf>, Theorem 1.

## 2. Polarization and sector signs

Write $R=h_y^{\mathrm R}$, $L=h_y^{\mathrm L}$, and
$Q_y=\mathfrak q(R,L)$. Hermitian polarization gives

```math
\mathfrak q[(R+L)/\sqrt2]-\mathfrak q[(R-L)/\sqrt2]
=Q_y+\overline{Q_y}=2\Re Q_y .
```

Every sector is real for the frozen real-even packet, so

```math
\Delta_h(y)=2Q_h(y).
```

The Fourier translations are

```math
\widehat R(t)=e^{-iyt}\widehat h(t),\qquad
\widehat L(t)=e^{iyt}\widehat h(t).
```

Since the first factor is conjugated, the archimedean phase is
$e^{2iyt}$, exactly as stated.

For the pole sector,

```math
\begin{aligned}
\overline{\widehat R(-i/2)}\widehat L(i/2)&=e^{-y}M_h^2,\\
\overline{\widehat R(i/2)}\widehat L(-i/2)&=e^{y}M_h^2.
\end{aligned}
```

For the prime sector,

```math
C_{R,L}(r)=K_h(r+2y).
```

As $m\log p>0$, only $C_{R,L}(-m\log p)$ can contribute, giving

```math
-\sum_{p,m\geq1}(\log p)p^{-m/2}K_h(2y-m\log p).
```

There is therefore no missing reflected prime term and no extra factor of
two. Since $K_h(\pm1)=0$, endpoint equality contributes zero, not half an
atom.

## 3. Prime--pole cancellation

With $x=e^{2y-r}$,

```math
\int_0^\infty x^{-1/2}K_h(2y-\log x)\,dx
=e^y\int_{-1}^1K_h(r)e^{-r/2}\,dr.
```

The autocorrelation identity and evenness of $h$ give

```math
\int K_h(r)e^{-r/2}\,dr
=\left(\int h(x)e^{x/2}\,dx\right)
 \left(\int h(x)e^{-x/2}\,dx\right)
=M_h^2.
```

Consequently,

```math
\mathcal I_h(y)
=e^yM_h^2-
\sum_{n\geq2}\Lambda(n)n^{-1/2}K_h(2y-\log n)
```

and hence

```math
Q_h(y)=A_h^\infty(y)+e^{-y}M_h^2+\mathcal I_h(y).
```

The growing pole term $e^yM_h^2$ has cancelled with the continuous main
term with the stated sign.

## 4. Bilateral transform

For

```math
J_h(t)=-\int_{[1,\infty)}
x^{-1/2}K_h(t-\log x)\,dE(x),
```

put $r=t-\log x$. Since $L_h$ is even,

```math
\int_{\mathbb R}K_h(t-\log x)e^{-st}\,dt
=x^{-s}L_h(-s)=x^{-s}L_h(s).
```

For $\Re s>1/2$,

```math
\int_{[1,\infty)}x^{-s-1/2}\,dE(x)
=-\frac{\zeta'}{\zeta}(s+1/2)-\frac1{s-1/2}.
```

The outer minus sign in $J_h$ therefore gives

```math
\mathscr B_h(s)
=L_h(s)\left[
\frac{\zeta'}{\zeta}(s+1/2)+\frac1{s-1/2}
\right].
```

Near $s=1/2$, the two residues are $-1$ and $+1$, so this point is
removable. At a zero $\rho$ of multiplicity $m_\rho$, the residue is

```math
m_\rho L_h(\rho-1/2).
```

At the trivial zero $-2n$, it is

```math
L_h(-2n-1/2).
```

Because a logarithmic derivative has only a simple pole, a multiple zero
changes the residue by $m_\rho$ and creates no derivative term.

## 5. Contour inversion

For $c>1/2$, $L_h(c+i\tau)$ decays faster than every power, so the
Bromwich integral is absolutely convergent. Shifting to
$\Re s=-2N-1$ crosses:

- every nontrivial pole $s=\rho-1/2$;
- precisely the first $N$ trivial poles $s=-2n-1/2$.

On the new line, the functional equation bounds the logarithmic derivative
by $O(\log(N+|\tau|+2))$. Repeated integration by parts in

```math
L_h(-2N-1+i\tau)
=\int_{-1}^1K_h(r)e^{(-2N-1+i\tau)r}\,dr
```

gives

```math
|L_h(-2N-1+i\tau)|
\ll_{h,M}e^{2N+1}(1+N)^M(1+|\tau|)^{-M}.
```

After multiplication by $e^{st}$, the remaining line is

```math
O_{h,M}\!\left(
e^{-(2N+1)(t-1)}(1+N)^M\log(N+2)
\right),
```

which tends to zero for $t>1$. Thus

```math
J_h(t)=
\sum_\rho m_\rho L_h(\rho-1/2)e^{(\rho-1/2)t}
+
\sum_{n\geq1}L_h(-2n-1/2)e^{(-2n-1/2)t}.
```

Setting $t=2y$ and using evenness of $L_h$ gives the displayed formula
for $\mathcal I_h(y)$, including the positive sign of both residue
families.

## 6. Archimedean cancellation

For the cross correlation, $C(r)=0$ for $r\geq0$ and
$C(-r)=K_h(2y-r)$. The source real-place sign therefore gives

```math
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}K_h(2y-r)\,dr.
```

Since

```math
\frac{e^{r/2}}{e^r-e^{-r}}
=\sum_{n\geq0}e^{-(2n+1/2)r},
```

substitution $u=2y-r$ yields

```math
A_h^\infty(y)
=-\sum_{n\geq0}
L_h(2n+1/2)e^{-(4n+1)y}.
```

The $n=0$ term is $-e^{-y}M_h^2$, and the terms $n\geq1$
cancel the complete trivial-zero series. Therefore

```math
Q_h(y)=
\sum_\rho m_\rho L_h(\rho-1/2)e^{2(\rho-1/2)y},
\qquad
\Delta_h(y)=2Q_h(y).
```

The negative-exponent version is identical after
$\rho\mapsto1-\rho$, because the zero multiset and multiplicities are
preserved and $L_h$ is even.

## 7. Zero coefficients and convergence

The exact coefficient is

```math
A_h(\rho)=m_\rho L_h(\rho-1/2).
```

For the packet,

```math
L_h(w)=c_g^{-2}
\prod_{n\geq1}
\left(\frac{\sinh(2^{-n-1}w)}{2^{-n-1}w}\right)^2.
```

Its factor zeros have union

```math
4\pi i\mathbb Z\setminus\{0\}.
```

At $4\pi ik$, exactly $v_2(|k|)+1$ unsquared factors vanish, so the
order is $2(v_2(|k|)+1)$.

There are no extra infinite-product zeros: on each compact set,

```math
\frac{\sinh(a_nw)}{a_nw}=1+O_K(a_n^2),
\qquad
\sum_n a_n^2<\infty,
```

so away from factor zeros the tail product converges locally uniformly to
a nowhere-zero holomorphic function.

Since $K_h\in C_c^\infty[-1,1]$,

```math
L_h(\sigma+i\tau)=O_M((1+|\tau|)^{-M})
```

uniformly for $\sigma$ in compact intervals. Together with
$N_\zeta(T)=O(T\log T)$, this proves absolute convergence of the zero
sum and local uniform convergence after every fixed real derivative.
The trivial-zero series converges for $2y>1$ because its general
absolute bound is $O(e^{-(2n+1/2)(2y-1)})$.

## 8. Visible critical zeros

Conrey's primary Theorem 1 states

```math
\kappa^*\geq0.401,
```

and in particular at least two fifths of all zeta zeros are simple and on
the critical line. Thus the number of such zeros up to height $T$ is
$\gg T\log T$.

Only the ordinates $4\pi k$ can be invisible. There are $O(T)$ such
ordinates up to height $T$, and a simple zero count can contribute at
most one zero per ordinate. Hence infinitely many simple critical-line
zeros are visible. No numerical zero is used.

## 9. Landau oscillation and parity

Suppose first that $f(t)=\mathcal I_h(t/2)$ is eventually nonnegative,
and discard a compact initial interval with left endpoint $T_0>1$.
Its Laplace abscissa satisfies $\sigma_c\leq1/2$. A visible critical
zero produces a genuine nonreal pole at $s=i\gamma$, so
$\sigma_c\geq0$; otherwise the defining tail transform would be
holomorphic at $i\gamma$.

The meromorphic expression is holomorphic at every real point of
$[0,1/2]$. The point $1/2$ is removable, while for
$0\leq s<1/2$, the real number $u=s+1/2$ belongs to
$[1/2,1)$, where

```math
\zeta(u)=\frac{\eta(u)}{1-2^{1-u}}\neq0.
```

Landau's nonnegative-tail lemma requires a singularity at the real
abscissa $\sigma_c$, a contradiction. Applying the same argument to
$-f$ excludes eventual nonpositivity.

For the complete cross term, the absolutely convergent zero expansion
gives, on a tail,

```math
\int_{T_0}^\infty Q_h(t/2)e^{-st}\,dt
=
\sum_\rho
\frac{m_\rho L_h(\rho-1/2)
e^{(\rho-1/2-s)T_0}}
{s-(\rho-1/2)}.
```

This continuation has the same visible nonreal poles and no real pole.
The identical Landau argument therefore proves that $Q_h$, and hence
$\Delta_h=2Q_h$, takes both signs arbitrarily far out.

Finally,

```math
\Delta_h=\mathfrak q[h_y^+]-\mathfrak q[h_y^-].
```

Thus $\Delta_h<0$ means the even packet has smaller energy, while
$\Delta_h>0$ means the odd packet has smaller energy. Both occur along
unbounded sequences. Continuity then gives infinitely many distinct
intervening zeros; it does not imply simple or transverse zeros.

## 10. Completeness notes

The theorem is correct. Two short justifications should remain explicit in
the final proof:

1. To infer the exact zero set of the infinite product, record the
   $1+O_K(a_n^2)$ estimate and $\sum a_n^2<\infty$, as done in
   Section 7 above.
2. In the proof of Landau's lemma, differentiation under the integral is
   justified by choosing $\varepsilon>0$ with
   $\sigma_1-\varepsilon>\sigma_c$ and using
   $t^n\ll_{n,\varepsilon}e^{\varepsilon t}$.

These are standard local completions. They introduce no assumption and do
not alter the PASS verdict.

## 11. Circularity result

The proof uses no RH, no global simplicity assumption, no linear
independence of ordinates, no Weil positivity, no desired-sign premise, and
no finite zero computation. The only simplicity input is Conrey's proved
positive-proportion theorem. Nonvanishing is proved exactly from the
frozen packet product and the $O(T)$ versus $T\log T$ count.

