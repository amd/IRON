# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Importing one operator must not import the rest of the catalog.

``iron.operators`` re-exports lazily (PEP 562), so ``from iron.operators import
GEMM`` should pull in ``iron.operators.gemm.op`` (or, for a small operator,
its single file) and nothing else. What that
saves is importing all fourteen operator modules and their designs, not the
cost of any one of them -- MHA, long named here as a witness, actually imports
slightly faster than ReLU.

Two things this does differently from a direct ``sys.modules`` check:

* It runs in a fresh interpreter. ``sys.modules`` records what the whole
  *session* imported, so a sibling test importing an operator for its own
  reasons fails this one while the catalog is still perfectly lazy -- and a
  session that happens not to touch that operator passes even if the catalog
  turned eager. Process history gives a false signal in both directions.
* It reads the catalog's own table rather than naming witnesses, so an
  operator added to ``_OPERATOR_MODULES`` is covered without touching a test.
"""

import subprocess
import sys

import pytest

from iron.operators import _OPERATOR_MODULES


def _modules_after_importing(name):
    """Import `name` from the catalog in a fresh interpreter; list what came with it."""
    program = (
        "import sys\n"
        f"from iron.operators import {name}\n"
        # A class carries its own name; a graph function's factory carries the
        # snake_case one (swiglu_decode for SwiGLUDecode).
        f"assert getattr({name}, '__name__', '').replace('_', '').lower() "
        f"== {name!r}.lower(), {name}.__name__\n"
        # Only the operator modules, named as the catalog names them:
        # importing one necessarily creates the package around it, which says
        # nothing about laziness.
        "from iron.operators import _OPERATOR_MODULES\n"
        "known = {f'iron.operators.{m}' for m in _OPERATOR_MODULES.values()}\n"
        "print('\\n'.join(sorted(known & set(sys.modules))))\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", program], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    return set(result.stdout.split())


def _is_composite(name):
    """Whether `name` is built from other operators rather than from a kernel.

    A composite is a graph function (a factory returning one, not a class):
    its body calls other operators, so importing it must import them. That
    is composition, not an eager catalog, and the two need different
    expectations.
    """
    from iron import operators

    return not isinstance(getattr(operators, name), type)


@pytest.mark.parametrize("name", sorted(_OPERATOR_MODULES))
def test_importing_one_operator_imports_no_unrelated_operator(name):
    own = f"iron.operators.{_OPERATOR_MODULES[name]}"
    imported = _modules_after_importing(name)
    others = sorted(imported - {own})

    if not _is_composite(name):
        assert not others, (
            f"importing {name} also imported {others}; the catalog is not lazy"
        )
    else:
        # A composite may import its parts, but never the whole catalog --
        # that is the regression this guards against.
        catalog = {f"iron.operators.{m}" for m in _OPERATOR_MODULES.values()}
        assert len(imported) < len(catalog), (
            f"importing {name} imported the entire catalog ({sorted(imported)}); "
            "a composite should pull in only the operators it is built from"
        )


def test_the_check_can_observe_an_import():
    """Guard the guard.

    Every assertion above is about a module being *absent*, so a subprocess
    that silently imported nothing -- or a name typo -- would make them all
    vacuously true. This pins that the probe does observe the module the
    operator legitimately needs.
    """
    imported = _modules_after_importing("GEMM")
    assert "iron.operators.gemm.op" in imported
