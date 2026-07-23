# Arithmetic source gate: the all-prime-power Chebyshev error measure

Project location corrected after the source gate was completed.

## 1. Frozen convention

This note uses the Dirichlet--Mellin convention

```math
 \mathcal M_1[\mu](s)
 :=
 \int_{[1,\infty)}x^{-s}\,d\mu(x).
```

It is chosen because the semilocal arithmetic coefficients are
$(\log p)p^{-m/2}$, and because
$-\zeta'/\zeta(s)$ is the Dirichlet series with coefficients
$\Lambda(n)$. No contour shift or analytic continuation is used below.

## 2. The exact atomic measure

On $[0,\infty)$, define the positive locally finite Radon measure

```math
 \boxed{
 d\Psi
 =
 \sum_{\substack{p\ {\rm prime}\\m\ge1}}
 (\log p)\,\delta_{p^m}
 =
 \sum_{n\ge2}\Lambda(n)\,\delta_n .
 }
\tag{2.1}
```

The second equality is exact because

```math
 \Lambda(n)
 =
 \begin{cases}
  \log p,&n=p^m,\quad p\text{ prime},\ m\ge1,\\
  0,&\text{otherwise}.
 \end{cases}
```

Thus this is an all-prime-power measure, not the primes-only Chebyshev
$\vartheta$-measure. It is preferable to denote it by $d\Psi$, rather
than $d\vartheta$.

It is locally finite because every bounded interval contains only finitely
many prime powers. Its support is contained in $[2,\infty)$. In particular,

```math
 d\Psi(\{0\})=d\Psi(\{1\})=0.
```

For every compactly supported Borel function $f$,

```math
 \boxed{
 \int_{(0,\infty)} f(x)\,d\Psi(x)
 =
 \sum_{p,m\ge1}(\log p)f(p^m)
 =
 \sum_{n\ge2}\Lambda(n)f(n).
 }
\tag{2.2}
```

There is no half weight at an endpoint. For example,

```math
 \int_{(0,X]}f\,d\Psi
 =
 \sum_{n\le X}\Lambda(n)f(n),
\tag{2.3}
```

so an atom at $X=p^m$ is included with its full weight. In the semilocal
operator, the equality case $p^m=\lambda^2$ vanishes because the
correlation overlap is null, not because the arithmetic measure assigns a
half weight.

## 3. Cumulative function and endpoint convention

For real $X\ge0$, define

```math
 \boxed{
 \psi(X)
 :=
 d\Psi((0,X])
 =
 \sum_{n\le X}\Lambda(n).
 }
\tag{3.1}
```

This is the standard right-continuous Chebyshev $\psi$-function. It is
zero on $[0,2)$, and

```math
 \psi(X^-)=\sum_{n<X}\Lambda(n),
\qquad
 \psi(X)-\psi(X^-)=\Lambda(X)
```

when $X$ is a positive integer, with the convention $\Lambda(1)=0$.
Thus $X=1$ is not a jump.

The right-continuous convention is equivalent to the
Lebesgue--Stieltjes rule

```math
 d\Psi((a,b])=\psi(b)-\psi(a),
\qquad 0\le a<b.
\tag{3.2}
```

## 4. The exact error measure

Let $dx$ denote Lebesgue measure on $[0,\infty)$, with zero mass at its
endpoint. Define

```math
 \boxed{
 dE:=d\Psi-dx.
 }
\tag{4.1}
```

This is a locally finite signed Radon measure, equivalently the difference
of two positive Radon measures when paired with compactly supported tests.
It is not a finite signed measure on the whole half-line: both its positive
and negative variations have infinite total mass, so on an unbounded Borel
set their unweighted difference need not be defined.

Anchored at $0$, its right-continuous cumulative function is

```math
 \boxed{
 E_0(X)
 :=
 dE((0,X])
 =
 \psi(X)-X,
 \qquad X\ge0.
 }
\tag{4.2}
```

In particular,

```math
 E_0(0)=0,\qquad E_0(1)=-1,
\qquad E_0(X)=-X\quad(0<X<2).
\tag{4.3}
```

The function $E_0$ is right-continuous and locally of bounded variation,
with

```math
 E_0(X)-E_0(X^-)=\Lambda(X).
\tag{4.4}
```

For $0\le a<b$,

```math
 dE((a,b])
 =
 E_0(b)-E_0(a)
 =
 \psi(b)-\psi(a)-(b-a).
\tag{4.5}
```

There is no atom at $0$ or $1$. No point at infinity is adjoined and no
boundary measure is introduced there. If $E_0$ is extended by zero to
$x<0$, it is continuous at $0$; hence its distributional derivative has
no spurious $\delta_0$.

For Mellin calculations based at $1$, the convenient primitive is instead

```math
 \boxed{
 E_1(X)
 :=
 dE((1,X])
 =
 \psi(X)-(X-1)
 =
 E_0(X)+1,
 \qquad X\ge1.
 }
\tag{4.6}
```

It satisfies $E_1(1)=0$ and has the same Stieltjes derivative as $E_0$
on $(1,\infty)$. The distinction $E_1=E_0+1$ is the entire lower-endpoint
correction in the integration-by-parts formula.

## 5. Stieltjes and distributional interpretations

For every $f\in C_c((0,\infty))$,

```math
 \boxed{
 \int f\,dE
 =
 \sum_{n\ge2}\Lambda(n)f(n)
 -
 \int_0^\infty f(x)\,dx.
 }
\tag{5.1}
```

Equivalently, for every
$\varphi\in C_c^\infty((0,\infty))$,

```math
 \boxed{
 \langle E_0',\varphi\rangle
 =
 -\int_0^\infty E_0(x)\varphi'(x)\,dx
 =
 \sum_{n\ge2}\Lambda(n)\varphi(n)
 -
 \int_0^\infty\varphi(x)\,dx
 =
 \langle dE,\varphi\rangle .
 }
\tag{5.2}
```

Thus $dE$ is exactly the distributional derivative of the cumulative
error $E_0=\psi-\operatorname{id}$, as well as its
Lebesgue--Stieltjes signed measure.

## 6. Mellin transform in $\operatorname{Re}s>1$

The Euler product is absolutely convergent for
$\sigma=\operatorname{Re}s>1$, and termwise logarithmic differentiation
gives

```math
 \boxed{
 \int_{[1,\infty)}x^{-s}\,d\Psi(x)
 =
 \sum_{p,m\ge1}(\log p)p^{-ms}
 =
 \sum_{n\ge2}\frac{\Lambda(n)}{n^s}
 =
 -\frac{\zeta'}{\zeta}(s).
 }
\tag{6.1}
```

Both the atomic integral and

```math
 \int_1^\infty x^{-s}\,dx=\frac1{s-1}
```

converge absolutely in that half-plane. Therefore

```math
 \boxed{
 \mathcal M_1[dE](s)
 =
 \int_{[1,\infty)}x^{-s}\,dE(x)
 =
 -\frac{\zeta'}{\zeta}(s)-\frac1{s-1},
 \qquad \operatorname{Re}s>1.
 }
\tag{6.2}
```

The measure integral and the termwise representation are holomorphic and
locally uniformly convergent in the stated half-plane. No value at $s=1$,
analytic continuation, or contour shift is asserted here.

There is no ordinary full-half-line Mellin transform

```math
 \int_{(0,\infty)}x^{-s}\,dE(x)
```

for $\operatorname{Re}s>1$: on $(0,1)$, $dE=-dx$, and
$\int_0^1x^{-s}\,dx$ diverges. The lower cutoff at $1$ is therefore
mathematically necessary, not cosmetic. Since $dE(\{1\})=0$, the intervals
$[1,\infty)$ and $(1,\infty)$ give the same measure integral.

Integration by parts, with the endpoint-normalized primitive $E_1$, yields

```math
 \boxed{
 \mathcal M_1[dE](s)
 =
 s\int_1^\infty E_1(x)x^{-s-1}\,dx
 =
 1+s\int_1^\infty E_0(x)x^{-s-1}\,dx.
 }
\tag{6.3}
```

The boundary at $1$ vanishes in the first expression because $E_1(1)=0$.
At infinity, $x^{-s}E_1(x)\to0$ for $\operatorname{Re}s>1$; the
elementary bound $\psi(x)=O(x\log x)$ already suffices. Formula (6.3) is
consistent with

```math
 s\int_1^\infty E_0(x)x^{-s-1}\,dx
 =
 -\frac{\zeta'}{\zeta}(s)-\frac{s}{s-1}.
\tag{6.4}
```

## 7. The interaction-adapted error distribution

Let $K\in C_c(\mathbb R)$. For every fixed $y$, the function

```math
 f_y(x)=x^{-1/2}K(2y-\log x)
```

has compact support in $(0,\infty)$. Consequently the mirror interaction
is the unambiguous Stieltjes/distributional pairing

```math
 \boxed{
 \begin{aligned}
 \mathcal I_E[K](y)
 &:=
 \int_{(0,\infty)}
 x^{-1/2}K(2y-\log x)\,dE(x)\\
 &=
 \sum_{p,m\ge1}
 (\log p)p^{-m/2}K(2y-m\log p)\\
 &\quad-
 \int_0^\infty x^{-1/2}K(2y-\log x)\,dx.
 \end{aligned}
 }
\tag{7.1}
```

No global finiteness or regularization is required because the translated
kernel has a compact multiplicative window. If
$\operatorname{supp}K\subset[-R_K,R_K]$, that window is

```math
 e^{2y-R_K}\le x\le e^{2y+R_K}.
\tag{7.2}
```

For the mirror-packet kernel in the compactness project,
$\operatorname{supp}K\subset[-2R,2R]$ and $y>R$; hence the whole window
lies in $(1,\infty)$. Thus the interaction is compatible exactly with the
base-$1$ Mellin transform (6.2).

For the mirror-packet correlation kernel
$K=K_\psi=C_{\psi,\mathsf J\psi}$, the sign convention of the frozen
semilocal form makes the raw arithmetic cross term
$-\int f_y\,d\Psi$, while the growing pole term supplies
$+\int f_y\,dx$. Their combined contribution is therefore

```math
 \boxed{-\mathcal I_E[K](y),}
```

which fixes the error-distribution sign without a later convention choice.

Equivalently, under $r=\log x$, define the locally finite signed measure

```math
 \boxed{
 d\nu_E(r)
 =
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
 \delta_{\log n}(r)
 -
 e^{r/2}\,dr.
 }
\tag{7.3}
```

Then

```math
 \boxed{
 \mathcal I_E[K](y)
 =
 \int_{\mathbb R}K(2y-r)\,d\nu_E(r).
 }
\tag{7.4}
```

The interaction is therefore an exact additive convolution with the
logarithmic all-prime-power error measure.

As a derived, interaction-weighted Mellin identity, for
$\operatorname{Re}w>1/2$,

```math
 \boxed{
 \int_{[1,\infty)}x^{-w}x^{-1/2}\,dE(x)
 =
 -\frac{\zeta'}{\zeta}\!\left(w+\frac12\right)
 -
 \frac1{w-\frac12}.
 }
\tag{7.5}
```

This is only the substitution $s=w+\frac12$ in (6.2); it involves no
contour shift.

## 8. Source-gate conclusion

The canonical arithmetic objects for the mirror interaction are

```math
 d\Psi
 =
 \sum_{p,m\ge1}(\log p)\delta_{p^m},
\qquad
 dE=d\Psi-dx,
\qquad
 E_0(X)=\psi(X)-X.
```

All atoms receive their full weights and the cumulative functions are
right-continuous. For Mellin analysis in $\operatorname{Re}s>1$, the
transform must be based at $x=1$, where the endpoint-normalized primitive
is $E_1=E_0+1$. For the fixed compact mirror kernel, the direct
Stieltjes pairing (7.1), or equivalently the logarithmic convolution (7.4),
is already exact and needs no regularization.
