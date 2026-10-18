# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every exported operator is a declared one.

Each module imports, each class is an ``Operator``, and its arg spec comes
from declared buffers.
"""

import importlib

import pytest

import iron.operators as ops
from iron.common import Operator
from iron.common.declare import Operand
from iron.tests.common.shipped import Shipped


@pytest.mark.parametrize("name", sorted(ops._OPERATOR_MODULES))
def test_exported_operator_is_declared(name):
    cls = getattr(ops, name)
    assert isinstance(cls, type) and issubclass(cls, Operator), name
    assert [b.name for b in cls.declaration.members if isinstance(b, Operand)], name


def test_flm_gemm_is_declared_and_its_shipped_form_runs_an_image():
    module = importlib.import_module("iron.operators.flm")
    cls = module.ProjectionGEMM
    assert issubclass(cls, Operator)
    assert issubclass(Shipped, cls) and Shipped._external is not None
    assert cls._external is None
