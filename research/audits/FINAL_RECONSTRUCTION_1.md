# Final independent reconstruction 1

Date: 2026-07-23

Scope: independent reconstruction of every load-bearing step in
`MAIN_THEOREM.md` from `FROZEN_SPECIFICATION.md`, including the complete
prime-power interaction, transform signs, contour residues and remainder,
archimedean cancellation, coefficient visibility, Conrey input, and the two
separate Landau arguments.

## Verdict

**PASS.** No mathematical correction is required. I found no missing prime
power, endpoint weight, sign, factor, residue, convergence hypothesis, hidden
Riemann-hypothesis input, numerical-zero dependency, or unproved
nonvanishing assumption.

## 1. Primary-form and convention check

The primary semilocal formula gives

```math
QW_\lambda(f,f)
=\frac1{2\pi}\int_{\mathbb R}2\theta'(t)|\widehat f(t)|^2\,dt
+2\Re\!\left(
\widehat f(i/2)\overline{\widehat f(-i/2)}
\right)
-\sum_{1<n\le\lambda^2}\Lambda(n)\langle f,T(n)f\rangle ,
```

with

```math
\langle f,T(n)g\rangle
=n^{-1/2}\bigl((f^**g)(n)+(f^**g)(n^{-1})\bigr).
```

Under the frozen logarithmic and Fourier conventions this is exactly (2.1)
of the specification:

```math
\mathfrak q_{\rm pp}(\Phi,\Psi)
=-\sum_{p}\sum_{m\ge1}
\frac{\log p}{p^{m/2}}
\left(C_{\Phi,\Psi}(m\log p)+C_{\Phi,\Psi}(-m\log p)\right).
```

Thus every $p^m$ occurs with coefficient
$-\Lambda(p^m)(p^m)^{-1/2}$. The primary finite cutoff is
$p^m\le\lambda^2$, inclusive and without a half weight.

The transform identities also reconstruct directly:

```math
\widehat{T_yh}(z)=e^{-iyz}\widehat h(z),
\qquad
\widehat{C_{\Phi,\Psi}}(z)
=\overline{\widehat\Phi(\bar z)}\widehat\Psi(z).
```

For the real even packet,

```math
C_{h_y^{\rm R},h_y^{\rm L}}(r)=K_h(r+2y).
```

Hence for $r>0$ and $y>1/2$,

```math
C(r)=0,\qquad C(-r)=K_h(2y-r).
```

This fixes the orientation of both the prime-power and archimedean cross
terms.

## 2. Polarization, pole sector, and Chebyshev subtraction

Hermitian polarization gives

```math
\mathfrak q[h_y^+]-\mathfrak q[h_y^-]
=2\Re\mathfrak q(h_y^{\rm R},h_y^{\rm L}).
```

Each sector is real for this packet, so

```math
\boxed{\Delta_h(y)=2Q_h(y)}.
```

Evaluation of the translated transforms at $\pm i/2$ gives

```math
\mathfrak q_{0,2}(h_y^{\rm R},h_y^{\rm L})
=M_h^2(e^y+e^{-y}).
```

The prime-power sector is

```math
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
K_h(2y-\log n),
```

and only

```math
e^{2y-1}<n<e^{2y+1}
```

contributes. Equality contributes zero because $K_h(\pm1)=0$; there is
no half endpoint contribution.

With

```math
dE=\sum_{n\ge2}\Lambda(n)\delta_n-dx,
```

the substitution $r=2y-\log x$ gives

```math
\int_0^\infty x^{-1/2}K_h(2y-\log x)\,dx
=e^yL_h(-1/2)=e^yM_h^2.
```

Therefore

```math
\mathcal I_h(y)
=e^yM_h^2-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
K_h(2y-\log n)
```

and

```math
\boxed{
Q_h(y)=A_h^\infty(y)+e^{-y}M_h^2+\mathcal I_h(y).
}
```

All factors and signs in Sections 1--2 of the theorem are correct.

## 3. Bilateral transform and residues

For the canonical base-$1$ extension

```math
J_h(t)=-\int_{[1,\infty)}
x^{-1/2}K_h(t-\log x)\,dE(x),
```

one has $J_h(t)=0$ for $t\le-1$, and
$J_h(t)=\mathcal I_h(t/2)$ for $t>1$.

For $\Re s>1/2$,

```math
\int_{\mathbb R}K_h(t-\log x)e^{-st}\,dt
=x^{-s}L_h(-s)=x^{-s}L_h(s).
```

Since

```math
\int_{[1,\infty)}x^{-u}\,dE(x)
=-\frac{\zeta'}{\zeta}(u)-\frac1{u-1},
```

the exact transform is

```math
\boxed{
\mathscr B_h(s)
=L_h(s)\left[
\frac{\zeta'}{\zeta}(s+1/2)+\frac1{s-1/2}
\right].
}
```

The pole at $s=1/2$ cancels. A nontrivial zero $\rho$ of multiplicity
$m_\rho$ contributes a simple logarithmic-derivative pole with residue

```math
\boxed{m_\rho L_h(\rho-1/2)}.
```

A multiple zero changes only this residue; it does not produce a derivative
term. A trivial zero $-2n$ contributes
$L_h(-2n-1/2)$.

## 4. Contour shift and convergence

Because $K_h\in C_c^\infty([-1,1])$, for every fixed vertical strip and
every $M$,

```math
L_h(\sigma+i\tau)=O_M((1+|\tau|)^{-M}).
```

At heights separated from zero ordinates by $\gg1/\log T$, the standard
bound

```math
\frac{\zeta'}{\zeta}(\sigma+iT)=O(\log^2T)
```

holds uniformly on the fixed horizontal strip, so the horizontal sides
vanish.

On $\Re s=-2N-1$, the functional equation and repeated integration by
parts give

```math
\left|
\frac{\zeta'}{\zeta}(s+1/2)+\frac1{s-1/2}
\right|
\ll\log(N+|\Im s|+2)
```

and

```math
|L_h(-2N-1+i\tau)|
\ll_{h,M}
e^{2N+1}(1+N)^M(1+|\tau|)^{-M}.
```

Consequently the remaining vertical integral is

```math
O_{h,M}\!\left(
e^{-(2N+1)(t-1)}(1+N)^M\log(N+2)
\right),
```

which tends to zero precisely in the asserted range $t>1$.

The resulting formula is

```math
\begin{aligned}
J_h(t)
={}&
\sum_\rho m_\rho L_h(\rho-1/2)e^{(\rho-1/2)t}\\
&+\sum_{n\ge1}
L_h(-2n-1/2)e^{(-2n-1/2)t}.
\end{aligned}
```

The trivial-zero series converges for $t>1$. Rapid vertical decay of
$L_h$, together with $N_\zeta(T)=O(T\log T)$, proves absolute and
locally uniform convergence of the nontrivial-zero sum after every fixed
number of real derivatives.

## 5. Archimedean cancellation

For the reflected cross correlation, $C(0)=0$,
$C(r)=0$ for $r\ge0$, and $C(-r)=K_h(2y-r)$. The physical
real-place formula therefore yields

```math
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}K_h(2y-r)\,dr.
```

The expansion

```math
\frac{e^{r/2}}{e^r-e^{-r}}
=\sum_{n\ge0}e^{-(2n+1/2)r}
```

has nonnegative terms, so Tonelli applies. Substitution gives

```math
A_h^\infty(y)
=-\sum_{n\ge0}
L_h(2n+1/2)e^{-(4n+1)y}.
```

The $n=0$ term is $-e^{-y}M_h^2$, while the terms $n\ge1$
cancel every trivial-zero term. Thus

```math
\boxed{
Q_h(y)=
\sum_\rho m_\rho L_h(\rho-1/2)e^{2(\rho-1/2)y}
}
```

and $\Delta_h=2Q_h$. The negative-exponent form obtained directly from
the Fourier--Mellin convention is the same series after
$\rho\mapsto1-\rho$ and evenness of $L_h$.

## 6. Visibility and the Conrey input

The packet product is

```math
L_h(w)=c_g^{-2}\prod_{n\ge1}
\left(\frac{\sinh(2^{-n-1}w)}{2^{-n-1}w}\right)^2.
```

Its zero set is exactly

```math
4\pi i\mathbb Z\setminus\{0\},
```

and the zero at $4\pi ik$ has order
$2(v_2(|k|)+1)$. Therefore

```math
A_h(\rho)=0
\iff
\rho=\frac12+4\pi ik,\qquad k\ne0.
```

Conrey's 1989 Theorem 1 proves
$\kappa^*\ge0.401$, hence at least two fifths of all zeros are simple
and on the critical line. This gives $\gg T\log T$ distinct simple
critical-line zeros up to height $T$. Only $O(T)$ possible ordinates
belong to $4\pi\mathbb Z$, so infinitely many Conrey zeros are visible.
No finite zero computation is used.

## 7. Separate Landau arguments

### 7.1 Arithmetic interaction

Suppose $f(t)=\mathcal I_h(t/2)$ is eventually nonnegative and choose
$T_0>1$ beyond its sign threshold. Its tail transform differs from
$\mathscr B_h$ by the transform of $J_h$ on the compact interval
$[-1,T_0]$, hence by an entire function.

The direct prime-power formula gives

```math
|f(t)|\ll_h (1+t)e^{t/2},
```

so $f$ is of exponential order. Absolute convergence gives
$\sigma_c\le1/2$. A visible pole at $s=i\gamma$ excludes
$\sigma_c<0$, and also excludes $\sigma_c=-\infty$. Hence

```math
0\le\sigma_c\le1/2.
```

The meromorphic continuation is holomorphic at every real point of this
interval: the $s=1/2$ pole is removable, and
$\zeta(s+1/2)\ne0$ for $0\le s<1/2$. Landau's lemma requires a
singularity at the real abscissa of a nonnegative tail, a contradiction.
Applying the same argument to $-f$ excludes eventual nonpositivity.

### 7.2 Full splitting

For $\mathcal Q_h(t)=Q_h(t/2)$, absolute convergence permits termwise
tail integration for $\Re s>1/2$:

```math
\int_{T_0}^\infty \mathcal Q_h(t)e^{-st}\,dt
=
\sum_\rho
\frac{
m_\rho L_h(\rho-1/2)
e^{(\rho-1/2-s)T_0}
}{
s-(\rho-1/2)
}.
```

This series is normally convergent away from its displayed poles. It has a
genuine pole at every visible critical-line ordinate $s=i\gamma$, but
no real pole. The same Landau argument separately excludes eventual
nonnegativity and eventual nonpositivity of $Q_h$. Since the factor in
$\Delta_h=2Q_h$ is positive, the conclusion transfers exactly to
$\Delta_h$.

Continuity then produces infinitely many disjoint intervals with
opposite-sign endpoints and therefore infinitely many distinct zeros.
No simplicity or transversality of these zeros is claimed.

## 8. Circularity audit

| Possible hidden input | Result |
|---|---|
| RH | Not used |
| Global zero simplicity | Not used; only Conrey's proved simple subset is selected |
| Linear independence of ordinates | Not used |
| Desired sign | Used only as a temporary contradiction hypothesis, once per sign |
| Unproved coefficient nonvanishing | Not used; the complete zero set of $L_h$ is proved |
| Numerical zeta-zero data | Not used |
| Weil positivity | Not used |
| Sign transfer from $\mathcal I_h$ to $\Delta_h$ | Not used; the two Landau arguments are separate |

## 9. Corrections

No correction is required.

Two optional exposition additions would make the proof maximally
self-contained but do not change it:

1. display the elementary estimate
   $|\mathcal I_h(t/2)|\ll_h(1+t)e^{t/2}$ before invoking Landau;
2. state explicitly that the tail transform and its displayed meromorphic
   continuation agree by the identity theorem after deletion of the finite
   initial interval.

