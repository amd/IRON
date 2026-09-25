# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Importing one operator must not import the rest of the catalog.

The check runs in a fresh interpreter: in this one, whatever the session
collected before it has already imported the operators it looks for.
"""

import subprocess
import sys

_CHECK = """\
import sys
from iron.operators import ElementwiseAdd
assert ElementwiseAdd.__name__ == "ElementwiseAdd"
loaded = [m for m in ("iron.operators.mha.op", "iron.operators.swiglu_decode.op")
          if m in sys.modules]
assert not loaded, f"importing ElementwiseAdd also imported {loaded}"
"""


def test_lazy_catalog_does_not_import_mha():
    result = subprocess.run(
        [sys.executable, "-c", _CHECK], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
