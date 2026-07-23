"""Fast structural tests for independent implementation B."""

from __future__ import annotations

import importlib.util
import math
from pathlib import Path
import sys
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    REPOSITORY_ROOT / "code" / "implementation_b" / "explicit_formula_b.py"
)
SPEC = importlib.util.spec_from_file_location("explicit_formula_b", MODULE_PATH)
assert SPEC and SPEC.loader
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class NumericalBTests(unittest.TestCase):
    def test_prime_power_generator_really_includes_composites(self) -> None:
        powers = mod.prime_powers_in_window(2.0)
        triples = {(item.p, item.m, item.value) for item in powers}
        self.assertIn((2, 2, 4), triples)
        self.assertIn((2, 3, 8), triples)
        self.assertIn((3, 2, 9), triples)
        self.assertTrue(any(item.m > 1 for item in powers))

    def test_strict_log_window(self) -> None:
        for item in mod.prime_powers_in_window(4.5):
            self.assertLess(abs(item.shift), 1.0)

    def test_product_tail_decreases(self) -> None:
        import mpmath as mp

        w = mp.mpf("50")
        self.assertLess(
            mod.lk_product_tail_relative_bound(w, 40),
            mod.lk_product_tail_relative_bound(w, 20),
        )

    def test_fourier_tail_is_small_for_default_parameters(self) -> None:
        bound = mod.fourier_high_tail_bound(500.0, 7)
        self.assertLess(bound, 1e-13)

    def test_trivial_tail_bound_positive(self) -> None:
        bound = mod.trivial_tail_bound(2.5, 18)
        self.assertGreater(bound, 0.0)
        self.assertLess(bound, math.exp(-40))


if __name__ == "__main__":
    unittest.main()
