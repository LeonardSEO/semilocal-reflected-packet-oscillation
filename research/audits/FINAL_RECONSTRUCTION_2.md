# Final independent reconstruction 2

Date: 2026-07-23

Scope: independent reconstruction from `FROZEN_SPECIFICATION.md` and
`MAIN_THEOREM.md` of the Fourier/Mellin conventions, correlation orientation,
polarization factor, zero coefficients, convergence assertions, parity sign,
and both Landau arguments.

## Verdict

**PASS.** I found no counterexample, missing sign, missing factor, hidden
Riemann-hypothesis input, or unproved zero-nonvanishing assumption in the
load-bearing theorem.

## 1. Fourier, Mellin, and correlation conventions

The frozen transform is

```math
\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx.
```

For $T_yf(x)=f(x-y)$, direct substitution gives

```math
\widehat{T_yf}(z)=e^{-iyz}\widehat f(z).
```

If $\Phi(x)=e^{x/2}f(e^x)$, then $u=e^x$ gives

```math
\widehat\Phi(t)
=\int_0^\infty f(u)u^{-1/2-it}\,du
=\widetilde f(1/2-it),
```

so the Fourier--Mellin convention is internally consistent.

For

```math
C_{\Phi,\Psi}(r)
=\int_{\mathbb R}\overline{\Phi(x-r)}\Psi(x)\,dx,
```

Fubini and the change $u=x-r$ give

```math
\widehat C_{\Phi,\Psi}(z)
=\overline{\widehat\Phi(\bar z)}\,\widehat\Psi(z).
```

For the real even packet $h$, this yields

```math
K_h(r)=C_{h,h}(r)=(h*h)(r).
```

For $h_y^{\mathrm R}=T_yh$ and $h_y^{\mathrm L}=T_{-y}h$,

```math
C_{h_y^{\mathrm R},h_y^{\mathrm L}}(r)
=K_h(r+2y).
```

Thus for $r>0$ and $y>1/2$,

```math
C(r)=0,\qquad C(-r)=K_h(2y-r).
```

This is exactly the orientation used in both the prime-power term and the
physical archimedean calculation.

## 2. Polarization and sector signs

For a Hermitian form antilinear in the first argument,

```math
\begin{aligned}
\mathfrak q[h_y^+]-\mathfrak q[h_y^-]
&=\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
  +\mathfrak q(h_y^{\mathrm L},h_y^{\mathrm R})\\
&=2\Re\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
\end{aligned}
```

Inversion symmetry makes this cross term real. Hence

```math
\boxed{\Delta_h(y)=2Q_h(y)}
```

with no missing factor of two.

The pole evaluations are also consistent. Translation at $z=\pm i/2$
gives respectively the products $e^{-y}M_h^2$ and $e^yM_h^2$, so

```math
\mathfrak q_{0,2}(h_y^{\mathrm R},h_y^{\mathrm L})
=M_h^2(e^y+e^{-y}).
```

The prime-power correlation orientation above gives

```math
\mathfrak q_{\mathrm{pp}}(h_y^{\mathrm R},h_y^{\mathrm L})
=-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
K_h(2y-\log n).
```

The change $r=2y-\log x$ gives

```math
\int_0^\infty x^{-1/2}K_h(2y-\log x)\,dx
=e^yL_h(-1/2)=e^yM_h^2.
```

Therefore

```math
Q_h(y)=A_h^\infty(y)+e^{-y}M_h^2+\mathcal I_h(y),
```

with exactly the sign printed in the theorem.

Finally, since $\Delta_h=q[h_y^+]-q[h_y^-]$,

```math
\Delta_h<0 \Longleftrightarrow q[h_y^+]<q[h_y^-],
```

so negative splitting favors the even packet and positive splitting favors
the odd packet.

## 3. Bilateral transform and residues

For

```math
J_h(t)=-\int_{[1,\infty)}
x^{-1/2}K_h(t-\log x)\,dE(x),
```

putting $r=t-\log x$ gives

```math
\int_{\mathbb R}K_h(t-\log x)e^{-st}\,dt
=x^{-s}L_h(-s)=x^{-s}L_h(s).
```

Since

```math
\int_{[1,\infty)}x^{-u}\,dE(x)
=-\frac{\zeta'}{\zeta}(u)-\frac1{u-1},
```

one obtains, for $\Re s>1/2$,

```math
\boxed{
\mathscr B_h(s)
=L_h(s)\left[
\frac{\zeta'}{\zeta}(s+1/2)+\frac1{s-1/2}
\right].
}
```

The zeta pole at $s=1/2$ cancels. At a zero $\rho$ of multiplicity
$m_\rho$, the logarithmic derivative has a simple pole with residue
$m_\rho$, irrespective of $m_\rho$. Hence the exact coefficient is

```math
\boxed{A_h(\rho)=m_\rho L_h(\rho-1/2).}
```

There are no derivative or polynomial-in-$y$ terms for multiple zeros.
At a trivial zero $-2n$, the residue is
$L_h(-2n-1/2)=L_h(2n+1/2)$.

The frozen product

```math
L_h(w)=c_g^{-2}\prod_{n\ge1}
\left(\frac{\sinh(2^{-n-1}w)}{2^{-n-1}w}\right)^2
```

vanishes precisely at $w=4\pi ik$, $k\ne0$. At $4\pi ik$, the
indices $n=1,\ldots,v_2(|k|)+1$ vanish, each through a squared simple
factor. Therefore the exact multiplicity is

```math
2\bigl(v_2(|k|)+1\bigr).
```

Consequently

```math
A_h(\rho)=0
\quad\Longleftrightarrow\quad
\rho=\frac12+4\pi ik,\quad k\ne0.
```

## 4. Contour and convergence audit

Because $K_h\in C_c^\infty([-1,1])$, repeated integration by parts gives
rapid vertical decay

```math
L_h(\sigma+i\tau)=O_{B,N}((1+|\tau|)^{-N})
```

uniformly for $|\sigma|\le B$. The standard zero count
$N_\zeta(T)=O(T\log T)$ therefore implies absolute convergence of

```math
\sum_\rho m_\rho L_h(\rho-1/2)e^{(\rho-1/2)t}
```

for every fixed real $t$, locally uniformly in $t$, and after any fixed
number of real derivatives.

On the shifted line $\Re s=-2N-1$, support in $[-1,1]$ and integration
by parts give the valid (deliberately nonsharp) bound

```math
|L_h(-2N-1+i\tau)|
\ll_M e^{2N+1}(1+N)^M(1+|\tau|)^{-M}.
```

Together with the functional-equation bound for $\zeta'/\zeta$, the
remaining vertical integral is

```math
O_{h,M}\!\left(
e^{-(2N+1)(t-1)}(1+N)^M\log(N+2)
\right),
```

which tends to zero exactly in the physical range $t>1$. Thus the
explicit formula and its summation convention are justified.

The archimedean cross term is

```math
A_h^\infty(y)
=-\int_0^\infty
\frac{e^{r/2}}{e^r-e^{-r}}K_h(2y-r)\,dr.
```

Using

```math
\frac{e^{r/2}}{e^r-e^{-r}}
=\sum_{n\ge0}e^{-(2n+1/2)r}
```

and then $u=2y-r$ gives

```math
A_h^\infty(y)
=-\sum_{n\ge0}
L_h(2n+1/2)e^{-(4n+1)y}.
```

The $n=0$ term cancels $e^{-y}M_h^2$; the remaining terms cancel all
trivial-zero residues. Hence

```math
\boxed{
Q_h(y)=
\sum_\rho m_\rho L_h(\rho-1/2)e^{2(\rho-1/2)y}.
}
```

The version with the negative exponent is identical after the unconditional
functional-equation reindexing $\rho\mapsto1-\rho$, preservation of
multiplicity, and evenness of $L_h$.

## 5. Independent Landau verification

Conrey's 1989 primary theorem proves that at least two fifths of all zeros
are simple and lie on the critical line. This supplies
$\gg T\log T$ distinct simple critical-line zeros up to height $T$.
Only $O(T)$ ordinates below $T$ lie in $4\pi\mathbb Z$, and at most one
selected simple critical-line zero can occupy any such ordinate. Therefore
infinitely many critical-line zeros satisfy $L_h(i\gamma)\ne0$.

### Arithmetic interaction

Assume that $f(t)=\mathcal I_h(t/2)$ is eventually nonnegative, and
discard an initial interval so that $f\ge0$ on $[T_0,\infty)$, with
$T_0\ge0$. Its Laplace transform differs from $\mathscr B_h$ by the
transform of a compactly supported function, hence by an entire function.

Absolute convergence for $\Re s>1/2$ implies
$\sigma_c\le1/2$. A genuine visible pole at $s=i\gamma$ excludes
$\sigma_c<0$ (and $\sigma_c=-\infty$): otherwise the defining Laplace
integral would be holomorphic in a half-plane containing $i\gamma$, which
would make that pole removable by uniqueness of analytic continuation.
Thus

```math
0\le\sigma_c\le\frac12.
```

On this real interval the continued transform is holomorphic. At $1/2$
the zeta pole is cancelled. For $0\le s<1/2$,
$s+1/2\in[1/2,1)$, and $\zeta$ has no real zero there; this follows
directly from

```math
\zeta(u)=\frac{\eta(u)}{1-2^{1-u}},
\qquad \eta(u)>0,\quad 0<u<1.
```

Landau's lemma for a nonnegative Laplace transform says that the real point
$\sigma_c$ must be singular. This contradicts the displayed
holomorphy. Applying the same argument to $-f$ excludes eventual
nonpositivity.

### Full splitting

For $\mathcal Q_h(t)=Q_h(t/2)$, termwise integration on a tail gives

```math
\int_{T_0}^\infty\mathcal Q_h(t)e^{-st}\,dt
=\sum_\rho
\frac{m_\rho L_h(\rho-1/2)
e^{(\rho-1/2-s)T_0}}
{s-(\rho-1/2)}
```

initially for $\Re s>1/2$. Rapid coefficient decay makes this a normally
convergent meromorphic continuation away from the displayed poles.
Visible critical-line zeros again give genuine poles at $s=i\gamma$.
There is no real pole in $[0,1/2]$, because $\zeta$ has no real
nontrivial zero. The identical abscissa/Landau contradiction excludes
either eventual sign of $Q_h$, and $\Delta_h=2Q_h$ transfers the result
without changing the sign.

Both functions are continuous. Strict values of both signs beyond every
bound can therefore be arranged as endpoints of pairwise disjoint
intervals; the intermediate value theorem supplies infinitely many
distinct zeros. No simplicity or transversality of those zeros is claimed.

## 6. Circularity result

The reconstruction uses:

- the frozen complete preform;
- the functional equation and standard zero count;
- Conrey's proved positive proportion of simple critical-line zeros; and
- the elementary Landau lemma proved in `MAIN_THEOREM.md`.

It does **not** use RH, simplicity of all zeros, linear independence of
ordinates, a computed zero, an assumed eventual sign, or an assumed
nonvanishing of the packet transform.

Final result: **PASS without qualification.**
