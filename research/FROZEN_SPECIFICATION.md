# Frozen specification: reflected-packet arithmetic interaction

Date frozen: 2026-07-23.

Status: immutable source gate for every later transform, contour, oscillation,
and numerical branch in this project. Any change to a convention below
requires restarting the audit.

## 1. Hilbert, Fourier, Mellin, and polarization conventions

Work on $L^2(\mathbb R,dx)$ with

```math
\langle \Phi,\Psi\rangle
=\int_{\mathbb R}\overline{\Phi(x)}\Psi(x)\,dx,
```

antilinear in the first variable. The Fourier transform is

```math
\widehat\Phi(z)
=\int_{\mathbb R}\Phi(x)e^{-izx}\,dx,
\qquad
\langle\Phi,\Psi\rangle
=\frac1{2\pi}\int_{\mathbb R}
\overline{\widehat\Phi(t)}\widehat\Psi(t)\,dt .
```

Translations are

```math
(T_y\Phi)(x)=\Phi(x-y),
\qquad
\widehat{T_y\Phi}(t)=e^{-iyt}\widehat\Phi(t).
```

For multiplicative tests the Mellin convention is

```math
\widetilde f(s)=\int_0^\infty f(u)u^{s-1}\,du.
```

If $F(u)=u^{1/2}f(u)$, $u=e^x$, and
$\Phi(x)=F(e^x)$, then

```math
\widehat\Phi(t)=\widetilde f\!\left(\frac12-it\right).
```

For $\Phi,\Psi\in C_c^\infty(\mathbb R)$, define

```math
C_{\Phi,\Psi}(r)
=\int_{\mathbb R}\overline{\Phi(x-r)}\Psi(x)\,dx.
```

Then

```math
\widehat{C_{\Phi,\Psi}}(z)
=\overline{\widehat\Phi(\bar z)}\,\widehat\Psi(z).
```

## 2. Complete semilocal Weil preform

On the common compact-support core
$\mathscr D=C_c^\infty(\mathbb R)$, freeze

```math
\begin{aligned}
\mathfrak q(\Phi,\Psi)
={}&
\frac1{2\pi}\int_{\mathbb R}
m_\infty(t)\,
\overline{\widehat\Phi(t)}\widehat\Psi(t)\,dt
\\
&+
\overline{\widehat\Phi(-i/2)}\widehat\Psi(i/2)
+\overline{\widehat\Phi(i/2)}\widehat\Psi(-i/2)
\\
&-
\sum_{\substack{p\ {\rm prime}\\m\ge1}}
\frac{\log p}{p^{m/2}}
\left[
C_{\Phi,\Psi}(m\log p)+C_{\Phi,\Psi}(-m\log p)
\right],
\end{aligned}
\tag{2.1}
```

where

```math
m_\infty(t)
=\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac14+\frac{it}{2}\right)-\log\pi
=2\theta'(t).
\tag{2.2}
```

For compactly supported pairs, the prime-power sum is finite.
Every prime power $p^m$, not only every prime, occurs with coefficient

```math
-(\log p)p^{-m/2}=-\Lambda(p^m)(p^m)^{-1/2}.
```

The equivalent real-place distribution is

```math
\begin{aligned}
W_{\mathbb R}(C)
={}&(\log 4\pi+\gamma_E)C(0)\\
&+\int_0^\infty
\frac{
e^{r/2}\bigl(C(r)+C(-r)\bigr)-2C(0)
}{
e^r-e^{-r}
}\,dr ,
\end{aligned}
\tag{2.3}
```

and the archimedean contribution in (2.1) is $-W_{\mathbb R}$.
Thus the scalar, subtraction, and overall sign in (2.3) are fixed.

For a finite semilocal interval $[-a,a]$, $a=\log\lambda$, the
arithmetic sum in (2.1) is restricted by

```math
p^m\le e^{2a}=\lambda^2.
```

The endpoint is inclusive and has no half weight. If equality occurs, the
correlation overlap is supported at at most one point and is zero in
$L^2$.

Primary reconstruction sources:

- Alain Connes and Caterina Consani,
  [*Spectral triples and $\zeta$-cycles*](https://doi.org/10.4171/LEM/1049),
  Enseign. Math. 69 (2023), §2.1 and Proposition 2.1,
  equations (2.1)--(2.12).
- Alain Connes, Caterina Consani, and Henri Moscovici,
  [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755),
  arXiv:2511.22755, §§2--3, equations (2.1)--(2.5) and
  (3.1)--(3.20).

## 3. Frozen packet

For $a_n=2^{-n-1}$, $n\ge1$, put

```math
b_{a_n}(x)=\frac1{2a_n}\mathbf 1_{[-a_n,a_n]}(x)
```

and define $g$ as the density of the absolutely convergent convolution

```math
g=*_{n\ge1}b_{a_n}.
\tag{3.1}
```

Equivalently, $g$ is the density of
$\sum_{n\ge1}U_n$, where the independent $U_n$ are uniform on
$[-a_n,a_n]$. Since

```math
\sum_{n\ge1}a_n=\frac12,
```

```math
g\in C_c^\infty(\mathbb R),\qquad
\operatorname{supp}g=[-1/2,1/2],
```

and $g$ is real, even, nonnegative, strictly positive on
$(-1/2,1/2)$, and $\int g=1$.

Freeze the $L^2$-normalized packet

```math
c_g=\|g\|_2,\qquad h=\frac g{c_g},\qquad \|h\|_2=1.
\tag{3.2}
```

No vanishing-moment condition is imposed or needed by (2.1).

With $\operatorname{sinc}w=\sin(w)/w$,

```math
\widehat g(z)=\prod_{n\ge1}\operatorname{sinc}(a_nz),
\qquad
\widehat h(z)=c_g^{-1}
\prod_{n\ge1}\operatorname{sinc}(a_nz).
\tag{3.3}
```

The products converge locally uniformly. For every $M\ge1$,

```math
|\widehat g(t)|
\le 2^{M(M+3)/2}|t|^{-M}
\quad(t\ne0).
\tag{3.4}
```

The exact zero set is

```math
Z(\widehat h)=4\pi\mathbb Z\setminus\{0\},
\tag{3.5}
```

and the zero at $4\pi k\ne0$ has order $v_2(|k|)+1$.

Freeze the autocorrelation

```math
K_h(r)
=C_{h,h}(r)
=\int_{\mathbb R}h(x-r)h(x)\,dx
=(h*h)(r).
\tag{3.6}
```

It is real, even, nonnegative, belongs to $C_c^\infty(\mathbb R)$, has
exact support $[-1,1]$, is positive on $(-1,1)$, and satisfies

```math
K_h(0)=1,\qquad
\int_{\mathbb R}K_h(r)\,dr=c_g^{-2}.
\tag{3.7}
```

Its bilateral Laplace transform is

```math
\mathcal L K_h(w)
:=\int_{-1}^{1}K_h(r)e^{wr}\,dr
=c_g^{-2}\prod_{n\ge1}
\left(\frac{\sinh(a_nw)}{a_nw}\right)^2.
\tag{3.8}
```

This is entire and even. Its exact zero set is

```math
Z(\mathcal L K_h)
=4\pi i\mathbb Z\setminus\{0\},
\tag{3.9}
```

with multiplicity $2(v_2(|k|)+1)$ at $4\pi ik$.

## 4. Reflected packets and parity

For $y\ge1/2$, define

```math
h_y^{\mathrm R}=T_yh=h(\,\cdot-y),
\qquad
h_y^{\mathrm L}=T_{-y}h=h(\,\cdot+y),
\tag{4.1}
```

and

```math
h_y^\pm
=\frac{h_y^{\mathrm R}\pm h_y^{\mathrm L}}{\sqrt2}.
\tag{4.2}
```

The two packets are $L^2$-orthogonal for $y\ge1/2$; at equality their
supports meet only at one null endpoint. Thus $h_y^\pm$ are normalized.
Since $h$ is real and even, $h_y^+$ is inversion-even and $h_y^-$
is inversion-odd.

To realize these packets in the finite interval $[-a,a]$, the exact
condition is

```math
y+\frac12\le a.
\tag{4.3}
```

Under (4.3), every prime power that can contribute is already retained by
the inclusive semilocal cutoff $p^m\le e^{2a}$, so the finite semilocal
form equals the complete compact-support preform on these packets.

## 5. Polarization and exact sector cross terms

For a Hermitian form antilinear in the first variable,

```math
\boxed{
\Delta_h(y)
:=\mathfrak q[h_y^+]-\mathfrak q[h_y^-]
=2\Re\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
}
\tag{5.1}
```

The factor is $2$, not $4$.

Put

```math
M_h
=\widehat h(i/2)=\widehat h(-i/2)
=\int_{\mathbb R}h(x)e^{x/2}\,dx>0
\tag{5.2}
```

and

```math
A_h(y)
:=\frac1{2\pi}\int_{\mathbb R}
m_\infty(t)e^{2iyt}|\widehat h(t)|^2\,dt.
\tag{5.3}
```

The phase in (5.3) is $e^{+2iyt}$, because the first Fourier factor is
conjugated. The integrand apart from the phase is real and even, hence
$A_h(y)\in\mathbb R$. Moreover, for every $N\ge0$,

```math
A_h(y)=O_{h,N}(|y|^{-N}).
\tag{5.4}
```

The exact pole cross term is

```math
\mathfrak q_{0,2}(h_y^{\mathrm R},h_y^{\mathrm L})
=M_h^2(e^y+e^{-y}).
\tag{5.5}
```

The exact all-prime-power cross term for $y\ge1/2$ is

```math
\mathfrak q_{\rm pp}(h_y^{\mathrm R},h_y^{\mathrm L})
=-\sum_{p,m\ge1}
\frac{\log p}{p^{m/2}}
K_h(2y-m\log p).
\tag{5.6}
```

Only the strict window

```math
2y-1<m\log p<2y+1
\tag{5.7}
```

can contribute. Equality gives zero because $K_h(\pm1)=0$; there is no
endpoint half weight.

## 6. Chebyshev error distribution

On $[0,\infty)$, define the all-prime-power measure

```math
d\Psi
=\sum_{p}\sum_{m\ge1}(\log p)\delta_{p^m}
=\sum_{n\ge2}\Lambda(n)\delta_n
\tag{6.1}
```

and the right-continuous cumulative function

```math
\psi(X)=d\Psi((0,X])=\sum_{n\le X}\Lambda(n).
\tag{6.2}
```

Every endpoint atom is included with full weight. Define the signed
locally finite Radon measure

```math
\boxed{dE=d\Psi-dx.}
\tag{6.3}
```

Thus the frozen Chebyshev error is specifically

```math
E_0(X)=dE((0,X])=\psi(X)-X,\qquad X\ge0.
\tag{6.4}
```

It is not $\theta(X)-X$ and not a primes-only distribution.
For Mellin integration based at $1$, also define

```math
E_1(X)=dE((1,X])=\psi(X)-(X-1)=E_0(X)+1.
\tag{6.5}
```

For $\Re s>1$,

```math
\int_{[1,\infty)}x^{-s}\,dE(x)
=-\frac{\zeta'}{\zeta}(s)-\frac1{s-1}
=s\int_1^\infty E_1(x)x^{-s-1}\,dx .
\tag{6.6}
```

The uncut Mellin integral over $(0,\infty)$ does not exist in this
half-plane, because $dE=-dx$ on $(0,1)$.

The logarithmic pushforward of $x^{-1/2}dE(x)$ is

```math
d\nu_E(r)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(r)
-e^{r/2}\,dr.
\tag{6.7}
```

## 7. Exact prime--pole cancellation and frozen interaction

Define the arithmetic interaction by the ordinary compact-window
Lebesgue--Stieltjes pairing

```math
\boxed{
\mathcal I_h(y)
:=-\int_0^\infty
x^{-1/2}K_h(2y-\log x)\,dE(x).
}
\tag{7.1}
```

Because $K_h$ is supported in $[-1,1]$, the integral samples only
$e^{2y-1}\le x\le e^{2y+1}$; it is a classical signed-measure integral,
not a formal density substitution.

The continuous main term is exactly

```math
\begin{aligned}
\int_0^\infty x^{-1/2}K_h(2y-\log x)\,dx
&=e^y\int_{-1}^{1}K_h(r)e^{-r/2}\,dr\\
&=e^yM_h^2 .
\end{aligned}
\tag{7.2}
```

Consequently,

```math
\boxed{
\mathcal I_h(y)
=e^yM_h^2
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
K_h(2y-\log n).
}
\tag{7.3}
```

Combining (5.5), (5.6), and (7.3) before estimating gives

```math
\boxed{
\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
=A_h(y)+e^{-y}M_h^2+\mathcal I_h(y).
}
\tag{7.4}
```

Therefore the exact energy splitting is

```math
\boxed{
\Delta_h(y)
=2\left[A_h(y)+e^{-y}M_h^2+\mathcal I_h(y)\right].
}
\tag{7.5}
```

No estimate in a later branch may separate the cancelling
$e^yM_h^2$ pole and prime main terms.

With the frozen sign convention:

- $\Delta_h(y)<0$ means the even packet has lower energy;
- $\Delta_h(y)>0$ means the odd packet has lower energy.

A sign theorem for $\mathcal I_h$ alone transfers to $\Delta_h$ only
after controlling the explicit correction
$A_h(y)+e^{-y}M_h^2$.

## 8. Source-gate exclusions

This specification contains no Riemann-hypothesis assumption, zero
simplicity assumption, zero-ordinate linear-independence assumption,
ground-state information, compactness claim, determinant convergence,
or desired sign. It uses no prolate, bottom-cluster, Galerkin, Robin, or
moment-certificate input.
