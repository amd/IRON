#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every operator that declares its cases, against its reference, on a device.

One module for the whole catalog. An operator declares the shapes it is
tested at as ``Testing`` beside itself, and this
runs each: construct, draw inputs with ``vectors``, dispatch, and
judge every output element against ``reference()`` by the declared
tolerance, or else by the contract of the kernel the operator runs.

An operator whose device test is more than that (a shipped binary checked
against its own accumulator, say) has its own ``test.py`` beside it.
"""

import ast
import importlib
from pathlib import Path

import aie.utils as aie_utils
import pytest

import iron.operators as catalog
from iron.common import Operator
from iron.common.testing import Case, Testing, run_test, vectors
from iron.tests.support.declared import declared

DEVICE = aie_utils.get_current_device()


def _declared():
    """Every operator in the catalog that declares its cases, with those cases."""
    return [
        pytest.param(
            cls,
            cls.test,
            case,
            id=f"{name}-{case.label}",
            marks=[
                *([pytest.mark.extensive] if case.extensive else []),
                *([pytest.mark.bench] if case.bench else []),
                *([pytest.mark.skip(reason=unresolvable)] if unresolvable else []),
            ],
        )
        for name, cls, case, unresolvable in (
            declared(DEVICE) if DEVICE is not None else []
        )
        if case.run
    ]


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("cls,declaration,case", _declared())
def test_operator(
    cls: type[Operator], declaration: Testing, case: Case, record_property
):
    op = cls(**case.kwargs).resolved(DEVICE)
    extra = declaration.draw(op) if declaration.draw is not None else {}
    tolerance = op.tolerance()
    if tolerance is None:
        raise ValueError(
            f"{cls.__name__} runs no kernel with a tolerance contract; "
            "override tolerance()"
        )
    errors = run_test(
        op, vectors(op, **extra), tolerance=tolerance, record=record_property
    )
    failed = {name: verdict.detail for name, verdict in errors.items()}
    assert not failed, f"{cls.__name__}({case.label}) failed: {failed}"


def test_every_operator_is_in_the_catalog():
    """Every class at the top of a module under ``iron/operators``, named
    without a leading underscore, that subclasses ``Operator`` is a catalog
    entry, so a profile can name it; ``test_operator`` builds the entries
    that declare a ``Testing``.
    """
    root = Path(catalog.__file__).parent
    catalogued = set(catalog.CATALOG.values())
    missing = []
    for path in sorted(root.rglob("*.py")):
        parts = path.relative_to(root).with_suffix("").parts
        # A make's output, as gemma4_engine's FastFlowLM, holds no IRON module.
        if "build" in parts[:-1]:
            continue
        names = [
            node.name
            for node in ast.parse(path.read_text()).body
            if isinstance(node, ast.ClassDef) and not node.name.startswith("_")
        ]
        if not names:
            continue
        module = importlib.import_module(".".join((catalog.__name__, *parts)))
        missing += [
            f"{module.__name__}.{name}"
            for name in names
            if issubclass(getattr(module, name), Operator)
            and getattr(module, name) not in catalogued
        ]
    assert not missing, f"not in iron.operators.CATALOG: {missing}"
