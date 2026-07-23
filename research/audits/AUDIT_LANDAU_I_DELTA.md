# Adversarial Landau audit for $\mathcal I_h$ and $\Delta_h$

**Verdict: PASS.**

This audit uses the frozen specification and `MAIN_THEOREM.md` without
changing the packet, transform convention, form normalization, or
Chebyshev-error distribution.

## 1. Arithmetic interaction

Write

```math
j(t)=J_h(t),\qquad t=2y.
```

If $\mathcal I_h(t/2)$ is eventually nonnegative, choose
$T_0>1$ beyond its eventual-sign threshold.  Then
```math
j(t)=\mathcal I_h(t/2)\ge 0\qquad(t\ge T_0).
```

### Tail shifting

The tail transform

```math
F_{T_0}(s)=\int_{T_0}^{\infty}j(t)e^{-st}\,dt
```

differs from the canonical bilateral transform by

```math
\mathscr B_h(s)-F_{T_0}(s)
=\int_{-1}^{T_0}J_h(t)e^{-st}\,dt.
```

The right side is entire because $J_h(t)=0$ for $t\le-1$ and is
locally integrable on the compact interval $[-1,T_0]$.  Thus deleting
the initial interval cannot create, move, or cancel a pole.

### Exponential order and finite abscissa

The direct all-prime-power formula gives, for $t>1$,

```math
j(t)
=e^{t/2}M_h^2
-\sum_{n\ge2}\Lambda(n)n^{-1/2}K_h(t-\log n).
```

Only $e^{t-1}<n<e^{t+1}$ occur.  Since
$\sum_{n\le X}\Lambda(n)\le\sum_{n\le X}\log n\le X\log X$,

```math
|j(t)|
\le C_he^{t/2}
+C_he^{-(t-1)/2}e^{t+1}(t+1)
\le C_h'(t+1)e^{t/2}.
```

Hence the Landau lemma's exponential-order hypothesis holds.  Moreover
the absolute-convergence estimate (3.3) gives

```math
\sigma_c\le\frac12,
```

so the tail abscissa is finite unless it is $-\infty$.

### Genuine visible pole

For a critical-line zero $\rho=1/2+i\gamma$, the residue at
$s=i\gamma$ is

```math
m_\rho L_h(i\gamma).
```

The frozen packet has

```math
Z(L_h)=4\pi i\mathbb Z\setminus\{0\}.
```

Conrey's unconditional theorem supplies $\gg T\log T$ distinct simple
critical-line zeros up to height $T$, while only $O(T)$ ordinates
belong to $4\pi\mathbb Z$.  Consequently infinitely many critical-line
zeros are visible, and at each such zero the residue is nonzero.  The
finite initial-interval transform is entire, so it cannot cancel this
pole.

If $\sigma_c<0$, the defining nonnegative tail integral is holomorphic
on $\Re s>\sigma_c$, a half-plane containing a visible $i\gamma$.
On the connected punctured half-plane it agrees with the meromorphic
continuation of $\mathscr B_h$, first on $\Re s>1/2$ and then by the
identity theorem.  The visible pole is therefore impossible.  The same
argument excludes $\sigma_c=-\infty$.  Thus

```math
0\le\sigma_c\le\frac12.
```

### Real boundary point

On the whole real interval $[0,1/2]$,

```math
L_h(s)\left[
\frac{\zeta'}{\zeta}\left(s+\frac12\right)
+\frac1{s-\frac12}
\right]
```

is holomorphic:

- the singularity at $s=1/2$ is removable;
- for $0\le s<1/2$, $\zeta(s+1/2)\ne0$, since
  $\zeta(u)=\eta(u)/(1-2^{1-u})<0$ for $0<u<1$.

Subtracting the entire initial-interval transform preserves local
holomorphy.  The identity theorem on the connected component of
$\{\Re s>\sigma_c\}$ with its discrete zeta poles removed identifies
this function with $F_{T_0}$ to the right of $\sigma_c$.  It therefore
provides a holomorphic continuation through the real point
$\sigma_c$, contradicting the proved Landau lemma.

This rules out eventual nonnegativity.  Repeating the argument for
$-j$ rules out eventual nonpositivity.

## 2. Full cross term and splitting

Put

```math
q(t)=Q_h(t/2)
=\sum_\rho a_\rho e^{(\rho-1/2)t},
\qquad
a_\rho=m_\rho L_h(\rho-1/2).
```

The rapid decay of $L_h(\sigma+i\tau)$, uniformly for
$|\sigma|\le1/2$, together with $N_\zeta(T)=O(T\log T)$, gives
absolute and locally uniform convergence.  In particular $q$ is
continuous and of exponential order at most $e^{t/2}$.

For every $\Re s>1/2$, termwise integration on $[T_0,\infty)$ is
justified and gives

```math
\int_{T_0}^{\infty}q(t)e^{-st}\,dt
=
\sum_\rho
\frac{a_\rho e^{(\rho-1/2-s)T_0}}
{s-(\rho-1/2)}.
```

The series is normally convergent off its displayed poles.  It has:

- a genuine pole at every visible $s=i\gamma$;
- no pole on the real interval $[0,1/2]$, because zeta has no
  nontrivial real zero.

If $q$, or $-q$, were eventually nonnegative, its abscissa would be
finite and at most $1/2$.  A visible nonreal pole forces it to be at
least $0$.  The same identity-theorem continuation then makes the tail
transform holomorphic at its real abscissa in $[0,1/2]$, contradicting
Landau.  Therefore $Q_h$ takes both strict signs arbitrarily far out.
Since

```math
\Delta_h=2Q_h
```

with a positive factor, the same conclusion holds for $\Delta_h$.

## 3. Strict signs and zeros

The negation of eventual nonnegativity is:

```math
\forall T\ \exists t>T:\ f(t)<0.
```

The negation of eventual nonpositivity is:

```math
\forall T\ \exists t>T:\ f(t)>0.
```

Thus the two Landau contradictions really yield strict positive and
strict negative values beyond every bound.  Continuity permits an
alternating increasing sequence of such points; the intermediate value
theorem then gives zeros in pairwise disjoint intervening intervals.
No simplicity, transversality, or isolation of those zeros follows or
is claimed.

## 4. Circularity check

| Possible hidden input | Audit result |
|---|---|
| RH | Not used.  The visible zeros come from Conrey's unconditional theorem. |
| Global zero simplicity | Not used.  Only Conrey's proved simple subset is used to defeat the $O(T)$ invisible lattice. |
| Linear independence of ordinates | Not used. |
| Desired eventual sign | Assumed only temporarily, once for each sign, to obtain separate contradictions. |
| Unproved coefficient nonvanishing | Not used.  The complete zero set of $L_h$ is computed explicitly. |
| Numerical zero data | Not used. |
| Weil positivity | Not used. |
| Sign transfer from $\mathcal I_h$ to $\Delta_h$ | Not used.  The two functions receive separate Landau arguments; only $Q_h\mapsto\Delta_h=2Q_h$ is transferred. |

## 5. Non-load-bearing exposition notes

Two steps are compressed in `MAIN_THEOREM.md` but are valid:

1. the elementary bound
   $J_h(t)=O_h((t+1)e^{t/2})$, verifying exponential order;
2. the identity-theorem step identifying each tail transform with its
   displayed meromorphic continuation near the real abscissa.

Spelling them out would harden the presentation, but neither is a missing
hypothesis or a defect in the result.
