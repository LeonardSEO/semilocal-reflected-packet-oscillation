# Semilocal reflected-packet oscillation

[![LaTeX](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/latex.yml/badge.svg)](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/latex.yml)
[![Python tests](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/python-tests.yml/badge.svg)](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/python-tests.yml)
[![Certificates](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/certificates.yml/badge.svg)](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/certificates.yml)
[![Checksums](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/checksums.yml/badge.svg)](https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation/actions/workflows/checksums.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21512462.svg)](https://doi.org/10.5281/zenodo.21512462)

This repository contains a standalone proof and reproducibility package for
the reflected-packet oscillation theorem in the complete semilocal Weil
preform.

> **This is not a proof of the Riemann hypothesis.**
>
> **This is a fixed-packet result.**
>
> **It does not determine the parity of an actual semilocal ground state.**
>
> **It proves an exact zero expansion and unconditional infinite sign
> changes for the frozen reflected-packet interaction.**

## Main theorem

One explicit packet is frozen:

```math
a_n=2^{-n-1},\qquad
g=*_{n\ge1}\frac{\mathbf 1_{[-a_n,a_n]}}{2a_n},
\qquad
h=\frac{g}{\|g\|_2}.
```

Let $K_h=h*h$, and let

```math
dE=\sum_{n\ge2}\Lambda(n)\delta_n-dx.
```

For $y>1/2$, define

```math
\mathcal I_h(y)=
-\int_0^\infty
x^{-1/2}K_h(2y-\log x)\,dE(x).
```

The exact explicit formula is

```math
\mathcal I_h(y)
=
\sum_\rho m_\rho
L_h(\rho-\tfrac12)e^{2(\rho-1/2)y}
+
\sum_{n\ge1}
L_h(2n+\tfrac12)e^{-(4n+1)y}.
```

The archimedean and residual pole terms cancel the complete trivial-zero
series. Therefore the full cross interaction is

```math
\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L})
=
\sum_\rho m_\rho
L_h(\rho-\tfrac12)e^{2(\rho-1/2)y},
```

and exact polarization gives

```math
\Delta_h(y)
=
\mathfrak q[h_y^+]-\mathfrak q[h_y^-]
=2\mathfrak q(h_y^{\mathrm R},h_y^{\mathrm L}).
```

Both $\mathcal I_h$ and $\Delta_h$ take positive and negative values
arbitrarily far to the right. No RH, global zero-simplicity, or
linear-independence assumption is used.

## Repository structure

- `paper/main.tex` and `paper/main.pdf`: polished standalone paper.
- `paper/sections/`: independently compilable source sections.
- `research/`: frozen specification, complete proof record, and diagnostics.
- `research/audits/`: independent reconstructions and circularity audits.
- `code/implementation_a/`: direct B-spline/all-prime-power computation.
- `code/implementation_b/`: independent Fourier/explicit-formula computation.
- `tests/`: structural and repository-invariant tests.
- `certificates/`: machine-readable finite outputs and interval certificates.
- `.github/workflows/`: paper, tests, certificate, checksum, and artifact CI.
- `REPRODUCIBILITY.md`: clean-checkout reproduction instructions.
- `SHA256SUMS`: hashes for the paper, certificates, and release artifacts.

## Analytic proof versus diagnostics

The analytic theorem is contained in `paper/` and `research/`. It remains
valid if `code/` and `certificates/` are deleted.

The numerical implementations:

- include every prime power in every finite support window;
- preserve the coefficient $(\log p)p^{-m/2}$;
- record the triple $(p,m,p^m)$;
- use the strict interaction window
  $|2y-\log(p^m)|<1$; and
- treat all finite results as diagnostics.

The exact-rational certificate at $y=1/2$ proves

```math
0.063637725597
<
\mathcal I_h(1/2)
<
0.088006928482.
```

It includes exactly the prime powers $2,3,4,5,7$ in $1<p^m<e^2$.
This finite value is not used to prove infinite oscillation.

## Reproduce

See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for exact commands.

## Zenodo publication

Published as an open preprint on 23 July 2026:

**Reflected-Packet Interactions in the Semilocal Weil Form: An Exact Zero
Expansion and Unconditional Infinite Oscillation**

- Author: Leonard van Hemert
- Version: 1.0.0
- Version DOI: [10.5281/zenodo.21512462](https://doi.org/10.5281/zenodo.21512462)
- Concept DOI for all versions:
  [10.5281/zenodo.21512461](https://doi.org/10.5281/zenodo.21512461)
- Resource type: Preprint
- Publisher: Zenodo
- Language: English
- Rights: No license granted; all rights reserved
- Copyright: Copyright (C) 2026 The Authors.

### Abstract

We freeze one explicit real, even, compactly supported smooth packet and
compute the interaction of two widely separated reflected translates in the
complete semilocal Weil preform. The pole and all-prime-power sectors combine
into a Stieltjes pairing against the Chebyshev-error distribution. Its
canonical bilateral Laplace transform is expressed through the logarithmic
derivative of the Riemann zeta function together with the required pole
subtraction.

A rigorous contour displacement gives an absolutely convergent expansion over
all nontrivial and trivial zeros. The archimedean term and the remaining pole
term cancel the complete trivial-zero series, leaving an exact zero-only
expansion for the full reflected cross interaction.

The frozen packet coefficient vanishes exactly on an explicitly determined
imaginary lattice. Conrey's unconditional positive-proportion theorem
supplies infinitely many visible critical-line poles. A Laplace-transform
version of Landau's theorem then excludes either eventual sign. Consequently,
both the arithmetic interaction and the even-minus-odd energy splitting take
positive and negative values arbitrarily far to the right.

This is not a proof of the Riemann hypothesis. It is a fixed-packet theorem.
It does not identify, approximate, or determine the parity of an actual
semilocal ground state. The numerical computations supplied with the paper
are diagnostics only and are not premises of the analytic proof.

The deposit includes the paper PDF, complete LaTeX sources, the frozen
mathematical specification, independent audit records, two numerical
implementations, all retained prime-power data, finite certificates, tests,
and reproducibility instructions.

### Deposited files

- `semilocal-reflected-packet-oscillation-paper-v1.0.0.pdf`
- `semilocal-reflected-packet-oscillation-paper-v1.0.0-sources.tar.gz`
- `semilocal-reflected-packet-oscillation-paper-v1.0.0-reproducibility.tar.gz`
- `ZENODO_UPLOAD_SHA256SUMS`

The Zenodo record is supplemented by this repository. Keywords: Weil explicit
formula; Riemann zeta function; prime powers; oscillation theorem; analytic
number theory; spectral theory; Mellin transform; Laplace transform; and
reproducible mathematics.

### Citation

> Leonard van Hemert. (2026). *Reflected-Packet Interactions in the Semilocal
> Weil Form: An Exact Zero Expansion and Unconditional Infinite Oscillation*
> (Version 1.0.0). Zenodo.
> https://doi.org/10.5281/zenodo.21512462

## Licensing

The source research files contained no explicit licensing policy. No
open-source license has therefore been invented or added. See [NOTICE](NOTICE).
