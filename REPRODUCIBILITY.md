# Reproducibility

All commands below are run from the repository root.

## Supported environment

- Python 3.12
- `uv`
- Tectonic 0.16.9 or a complete TeX Live installation
- pinned numerical packages:
  - `mpmath==1.4.1`
  - `numpy==2.0.2`
  - `scipy==1.13.1`
  - `python-flint==0.9.0`

The scripts in implementation B also contain PEP 723 dependency metadata.

## 1. Build the paper

With Tectonic:

```sh
cd paper
tectonic -X compile --outfmt pdf --print --untrusted main.tex
cd ..
```

The repository was locally compiled with the bundled LaTeX plugin:

```sh
python3 /Users/leonard/.codex/plugins/cache/openai-bundled/latex/0.2.4/scripts/compile_latex.py \
  "$(pwd)/paper/main.tex"
```

The portable GitHub Actions build uses a pinned `latex-action` revision with
TeX Live.

## 2. Run Python tests

```sh
uv run --python 3.12 \
  --with mpmath==1.4.1 \
  --with numpy==2.0.2 \
  --with scipy==1.13.1 \
  python -m unittest discover -s tests -v
```

## 3. Regenerate implementation A

```sh
uv run --python 3.12 --with scipy==1.13.1 \
  python code/implementation_a/direct_interaction.py \
  --factors 12 --precision 70 --quadrature-order 128 \
  --output-dir certificates/implementation_a/n12

uv run --python 3.12 --with scipy==1.13.1 \
  python code/implementation_a/direct_interaction.py

uv run --python 3.12 --with scipy==1.13.1 \
  python code/implementation_a/direct_interaction.py \
  --factors 16 --precision 90 --quadrature-order 256 \
  --output-dir certificates/implementation_a/n16

python3 code/implementation_a/certify_y_half.py
python3 code/implementation_a/compare_refinement.py
python3 code/implementation_a/compare_numerical_b.py
```

The exact-rational certificate uses only the Python standard library.

## 4. Regenerate implementation B

```sh
uv run code/implementation_b/explicit_formula_b.py
uv run code/implementation_b/certify_coefficients_arb.py
python3 code/implementation_b/verify_outputs.py
```

The explicit-formula output contains diagnostic quadrature errors and a
truncated nontrivial-zero sum. Those fields are not interval certificates.
The Arb coefficient file certifies only selected coefficient
nonvanishing.

## 5. Verify all retained prime powers

```sh
uv run --python 3.12 \
  --with mpmath==1.4.1 \
  --with numpy==2.0.2 \
  --with scipy==1.13.1 \
  python -m unittest tests.test_repository_invariants -v
```

This checks that every recorded arithmetic row satisfies
$p^m=n$, has $m\ge1$, and lies in the strict packet support window.

## 6. Build deterministic release archives

```sh
python3 scripts/build_release_artifacts.py
```

This creates:

- `dist/semilocal-reflected-packet-oscillation-v1.0.2-latex-source.tar.gz`
- `dist/semilocal-reflected-packet-oscillation-v1.0.2-code-certificates.tar.gz`
- `dist/semilocal-reflected-packet-oscillation-v1.0.2-source.tar.gz`
- `SHA256SUMS`

Archive entries have fixed timestamps, ownership metadata, ordering, and
permissions. Re-running the script without changing source files produces
identical archive hashes.

## 7. Verify hashes

```sh
shasum -a 256 -c SHA256SUMS
```

## Clean-checkout acceptance rule

A checkout is accepted only if:

1. the paper compiles;
2. all Python tests pass;
3. both certificate families regenerate and pass semantic verification;
4. the release builder is deterministic over two consecutive runs; and
5. every entry in `SHA256SUMS` verifies.
