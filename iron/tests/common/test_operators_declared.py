# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every exported operator is a declared one.

Each module imports, each class is an ``Operator``, and its arg spec comes
from declared buffers.
"""

import pytest

import iron.operators as ops
from iron.common import Operator


@pytest.mark.parametrize("name", sorted(ops.CATALOG))
def test_exported_operator_is_declared(name):
    cls = ops.CATALOG[name]
    assert isinstance(cls, type) and issubclass(cls, Operator), name
    assert cls.declaration.operands, name
