# Independent numerical implementation B

This directory implements the frozen specification without reading or
importing implementation A.

It evaluates the same scalar interaction in two independent ways:

1. `explicit_formula_b.py` builds every prime power in the strict logarithmic
   support window and obtains $K_h$ by vector Gauss--Kronrod inversion of
   $\prod_n\operatorname{sinc}(a_nt)^2$.
2. The same program obtains the explicit-formula diagnostic from zeta zeros
   and
   ```math
   {\cal L}K_h(w)=c_g^{-2}\prod_{n\ge1}
   \left(\frac{\sinh(a_nw)}{a_nw}\right)^2.
   ```
3. `certify_coefficients_arb.py` uses Arb balls, an analytic infinite-product
   tail enclosure, and $1/2\le c_g^{-2}\le1$ to certify nonvanishing of
   selected coefficients.

The direct and explicit values are diagnostics.  The program rigorously tracks
the finite-product tail, the Fourier cutoff tail, and the trivial-zero tail.
The vector quadrature error is QUADPACK's estimate, not an interval
certificate.  Most importantly, the omitted nontrivial-zero sum is not
certified.  The output therefore makes no asymptotic or sign claim.

Run:

```sh
uv run code/implementation_b/explicit_formula_b.py
uv run code/implementation_b/certify_coefficients_arb.py
uv run --with mpmath==1.4.1 --with numpy==2.0.2 --with scipy==1.13.1 \
  python -m unittest -v tests/test_numerical_b.py
python3 code/implementation_b/verify_outputs.py
```

Outputs:

- `certificates/implementation_b/explicit_formula_b_output.json`
- `certificates/implementation_b/coefficient_certificates_arb.json`

Every retained arithmetic record contains `(p,m,p^m)`, so higher prime powers
and endpoint handling are directly auditable.
