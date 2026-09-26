#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every operator that declares its cases, against its reference, on a device.

One module for the whole catalog. An operator declares the shapes it is
tested at as :class:`~iron.common.testing.Testing` beside itself, and this
runs each: construct, draw inputs with :func:`vectors`, dispatch, and
judge every output element against ``reference()`` by the declared
tolerance, or else by the contract of the kernel the operator runs.

An operator whose device test is more than that (a composite compared step
by step, a shipped binary checked against its own accumulator) has its own
``test.py`` beside it.
"""

import aie.utils as aie_utils
import pytest

import iron.operators as catalog
from iron.common import Operator
from iron.common.harness import run_test, vectors
from iron.common.testing import Case, Testing

if aie_utils.get_current_device() is None:
    # Every case is sized from the device's width, so there is nothing to
    # parametrize over without one.
    pytest.skip(
        "the operator cases are sized from the bound device; none is bound",
        allow_module_level=True,
    )


def _declared():
    """Every operator in the catalog that declares its cases, with those cases.

    Read from the catalog's own table, so an operator added there is covered
    without touching this module.
    """
    params = []
    for name in sorted(catalog._OPERATOR_MODULES):
        cls = getattr(catalog, name)
        # A composite (SwiGLUDecode) is a function returning a sequence, and
        # tested by its own test.py.
        if not (isinstance(cls, type) and issubclass(cls, Operator)):
            continue
        declaration = cls.test
        if declaration is None:
            continue
        for case in declaration.resolve(cls):
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
def test_operator(cls: type[Operator], declaration: Testing, case: Case, npu_runtime):
    op = cls(**case.kwargs)
    draw = declaration.draw
    extra = draw(op) if callable(draw) else (draw or {})
    tolerance = declaration.tolerance or op.reference_tolerance()
    if tolerance is None:
        raise ValueError(
            f"{cls.__name__} runs no kernel with a tolerance contract; "
            "declare Testing(tolerance=...)"
        )
    run = run_test(op, vectors(op, **extra), tolerance=tolerance)
    assert not run.errors, f"{cls.__name__}({case.label}) failed: {run.errors}"
