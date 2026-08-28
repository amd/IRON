# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Importing one operator must not import the rest of the catalog."""

import sys

from iron.operators import ElementwiseAdd


def test_lazy_catalog_does_not_import_mha():
    assert ElementwiseAdd.__name__ == "ElementwiseAdd"
    assert "iron.operators.mha.op" not in sys.modules
    assert "iron.operators.swiglu_decode.op" not in sys.modules
