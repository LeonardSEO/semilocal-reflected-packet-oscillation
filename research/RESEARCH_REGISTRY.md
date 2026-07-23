# Research and audit registry

This registry records the distinct approach families and rounds used for
the frozen reflected-packet project. No route below uses prolate proxies,
ground states, bottom clusters, Galerkin limits, Robin inequalities, or
moment certificates.

## Frozen approach families

| Family | Frozen object or question | Status |
|---|---|---|
| Primary-source reconstruction | Complete Connes--Consani semilocal Weil preform | Passed |
| Packet construction | One dyadic infinite-convolution $C_c^\infty$ packet | Passed and frozen |
| Support and endpoints | Packet overlap, prime-power windows, inclusive cutoff | Passed |
| Polarization | Exact relation $\Delta_h=2\Re q(R,L)$ | Passed |
| Chebyshev distribution | $dE=d\psi-dx$, with every prime power | Passed |
| Prime--pole cancellation | Cancellation of the $e^yM_h^2$ main term | Passed |
| Transform analysis | Canonical base-$1$ bilateral Laplace transform | Passed |
| Contour and explicit formula | Nontrivial and trivial zero residues with remainder | Passed |
| Archimedean comparison | Exact cancellation of trivial zeros and $e^{-y}$ pole | Passed |
| Coefficient visibility | Exact zero set of $L_h(\rho-1/2)$ | Passed |
| Oscillation | Landau theorem for $\mathcal I_h$ and $\Delta_h$ | Passed |
| Conditional zero regimes | RH and attained-rightmost-zero scale | Classified; not used |
| Numerical diagnostics | Independent prime and zero implementations | Passed as non-load-bearing |
| Circularity | RH, simplicity, LI, desired sign, and hidden zero data | Passed |

## Distinct rounds

### Round 1 — primary semilocal source reconstruction

Two primary semilocal papers were compared equation by equation. The
Fourier/Mellin convention, antilinear first slot, archimedean multiplier,
two pole terms, every prime-power coefficient, and inclusive endpoint were
fixed.

Concrete output: `FROZEN_SPECIFICATION.md`, §§1--2.

### Round 2 — explicit packet construction

The density of an infinite convolution of uniforms with
$a_n=2^{-n-1}$ was constructed. Smoothness, exact support, normalization,
Fourier product, and the exact transform zero set were proved.

Concrete output: `FROZEN_SPECIFICATION.md`, §3.

### Round 3 — support, parity, and polarization audit

Packet supports, the threshold $y\ge1/2$, inversion parity, the strict
prime-power window, and the factor
$\Delta_h=2\Re\mathfrak q(R,L)$ were independently checked.

Concrete output: `FROZEN_SPECIFICATION.md`, §§4--5.

### Round 4 — Chebyshev measure and endpoint audit

The all-prime-power measure, $E_0=\psi-x$, the base-$1$ primitive
$E_1=E_0+1$, full endpoint atoms, and the logarithmic pushforward were
reconstructed. The primes-only $\theta$-measure was rejected.

Concrete output: `FROZEN_SPECIFICATION.md`, §6.

### Round 5 — exact prime--pole cancellation

The continuous $dx$ term was evaluated exactly as $e^yM_h^2$ and
combined with the pole sector before estimation.

Concrete output: `FROZEN_SPECIFICATION.md`, §7.

### Round 6 — bilateral transform and contour inversion

A canonical causal/base-$1$ extension was introduced solely for the
transform. Its initial Euler-product half-plane, removable zeta pole,
nontrivial-zero residues, trivial-zero residues, horizontal contours, and
left-line remainder were derived.

Concrete output: `MAIN_THEOREM.md`, §§3--4.

### Round 7 — archimedean and complete-Weil comparison

The real-place kernel was expanded geometrically. Its $n=0$ term cancels
the residual $e^{-y}$ pole; its $n\ge1$ terms cancel the complete
trivial-zero series.

Concrete output: `MAIN_THEOREM.md`, §5.

### Round 8 — zero-coefficient and visibility analysis

The coefficient
$m_\rho L_h(\rho-1/2)$ and its exact invisible lattice were proved.
Conrey's primary simple-critical-zero theorem was compared with the
$O(T)$ invisible lattice, giving infinitely many visible zeros without
finite zero computation.

Concrete output: `MAIN_THEOREM.md`, §6.

### Round 9 — Landau oscillation analysis

The Laplace version of Landau's theorem was proved directly. Separate
tail-transform arguments were applied to the arithmetic interaction and
to the full even--odd splitting.

Concrete output: `MAIN_THEOREM.md`, §§7--9.

### Round 10 — two independent numerical implementations

Implementation A uses finite dyadic convolutions/B-splines and direct
all-prime-power windows. Implementation B uses Fourier inversion for the
direct side and an independent infinite-product/zero side. All finite
results are explicitly diagnostic, not premises of the theorem.

Concrete outputs: `../code/implementation_a/`,
`../code/implementation_b/`, and `../certificates/`.

### Round 11 — six full theorem reconstructions

Six independent researchers were assigned the entire chain rather than
isolated lemmas: transform convention, contour shift, residues, zero-sum
convergence, coefficient visibility, Landau oscillation, and energy sign.

Status: passed by six independent full-chain reconstructions. Each
reproduced the transform sign, the nontrivial- and trivial-zero residues,
the archimedean cancellation, the exact coefficient zero set, the Landau
argument, and the energy-splitting factor. One reconstruction identified
the need to state $T_0\ge0$ in the elementary Landau lemma; that
condition was added before the final pass.

### Round 12 — three circularity audits

Three independent auditors were assigned to search specifically for RH,
unproved simplicity, zero-ordinate linear independence, desired-sign
assumptions, hidden finite zero data, Weil positivity, and insertion of the
conclusion through normalization.

Status: passed by more than three independent audits. No audit found an
RH assumption, an unproved global simplicity assumption, ordinate linear
independence, Weil positivity, a desired-sign premise, hidden numerical
zero data, or zeta zeros inserted into the packet.

## Stop-rule state

The analytic stopping condition is met:

1. the exact interaction formula;
2. the rigorous explicit formula; and
3. unconditional infinite oscillation for the frozen packet.

Round 11 and Round 12 confirmed all three items. The project therefore
stops with classification **B. INFINITE OSCILLATION THEOREM**. No packet
optimization or larger numerical search is authorized.
