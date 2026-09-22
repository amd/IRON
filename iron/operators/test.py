#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every operator that declares its cases, against its reference, on a device.

One module for the whole catalog. An operator declares the shapes it is
tested at as :class:`~iron.common.testing.Testing` beside itself, and this
runs each: construct, draw inputs with :func:`golden`, dispatch, and
compare every output element against ``reference()``. What it replaced was
one test module per operator, each a single call with this body.

An operator whose device test is more than that -- a composite compared
step by step, a shipped overlay checked against its own accumulator --
keeps its own ``test.py`` beside it.
"""

import pytest

import aie.utils as aie_utils

import iron.operators as catalog
from iron.common.harness import run_test, vectors
from iron.common.testing import Testing

if aie_utils.get_current_device() is None:
    # Every case is sized from the device's width, so there is nothing to
    # parametrize over without one.
    pytest.skip(
        "the operator cases are sized from the bound device; none is bound",
        allow_module_level=True,
    )


def _declared():
    """Every operator in the catalog that says how to test it, with its cases.

    Read from the catalog's own table, so an operator added there is covered
    without touching this module.
    """
    params = []
    for name in sorted(catalog._OPERATOR_MODULES):
        cls = getattr(catalog, name)
        declaration = getattr(cls, "test", None)
        if not isinstance(declaration, Testing):
            continue
        for case in declaration.resolve():
            params.append(
                pytest.param(
                    cls,
                    declaration,
                    case,
                    id=f"{name}-{case.label}",
                    marks=[pytest.mark.extensive] if case.extensive else [],
                )
            )
    return params


@pytest.mark.parametrize("cls,declaration,case", _declared())
def test_operator(cls, declaration, case, npu_runtime):
    op = cls(**case.kwargs)
    draw = declaration.draw
    extra = draw(op) if callable(draw) else (draw or {})
    run = run_test(
        op,
        vectors(op, **extra),
        rel_tol=declaration.rel_tol,
        abs_tol=declaration.abs_tol,
        max_error_rate=declaration.max_error_rate,
    )
    assert not run.errors, f"{cls.__name__}({case.label}) failed: {run.errors}"
