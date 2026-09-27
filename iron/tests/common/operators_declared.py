# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every exported operator is a declared one, or a graph.

Each module imports, each class is an ``Operator``, and its arg spec comes
from declared buffers.
"""

import importlib

import pytest

import iron
import iron.operators as ops
from iron.common import Operator

GRAPHS = {"SwiGLU"}


@pytest.mark.parametrize("name", sorted(ops._OPERATOR_MODULES))
def test_exported_operator_is_declared(name):
    cls = getattr(ops, name)
    if name in GRAPHS:
        assert isinstance(cls, type) and issubclass(cls, iron.Graph)
        return
    assert isinstance(cls, type) and issubclass(cls, Operator), name
    assert [b.name for b in cls._members if hasattr(b, "direction")], name


def test_flm_declares_one_operator_and_its_shipped_form():
    module = importlib.import_module("iron.operators.flm")
    cls, shipped = module.GEMM, module.Shipped
    assert issubclass(cls, Operator)
    assert issubclass(shipped, cls) and shipped._external is not None
    assert cls._external is None
