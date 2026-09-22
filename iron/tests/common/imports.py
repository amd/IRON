# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Where torch is allowed to be, and where it is not.

mlir-aie is a hard dependency of the library and every module may import it
at the top. torch is not: it is an order of magnitude heavier (roughly 2s and
1,200 modules against 0.4s and 400), and nothing in declaring, tuning,
designing or compiling an operator needs it. Only a reference implementation
and the test harness do.

So the rule these tests pin is: importing the library, and declaring or
building an operator, must not pull torch in. Running a reference may.
Without the rule the cost lands on every caller, including the ones that
only ever compile.
"""

import subprocess
import sys

import pytest

# Every module of the library, plus the two package roots. Named one by one
# rather than walked, so that adding a module is a deliberate choice about
# which side of the line it falls on.
TORCH_FREE = [
    "iron.common",
    "iron.common.allocator",
    "iron.common.artifacts",
    "iron.common.declare",
    "iron.common.design",
    "iron.common.elementwise",
    "iron.common.external",
    "iron.common.fusion",
    "iron.common.graph",
    "iron.common.jit_compile",
    "iron.common.kernels",
    "iron.common.packaging",
    "iron.common.sequence",
    "iron.common.testing",
    "iron.common.tiling",
    "iron.common.tracing",
    "iron.operators",
]

# iron.common.harness is the deliberate exception: it is the test harness,
# it builds reference inputs, and it says so in its own docstring.
TORCH_USING = ["iron.common.harness"]


def _pulls_torch(statement: str) -> bool:
    """Run ``statement`` in a fresh interpreter; report whether torch came too."""
    code = f"import sys\n{statement}\nprint('torch' in sys.modules)"
    out = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True
    )
    assert out.returncode == 0, f"{statement!r} failed:\n{out.stderr}"
    return out.stdout.strip() == "True"


@pytest.mark.parametrize("module", TORCH_FREE)
def test_the_library_imports_without_torch(module):
    assert not _pulls_torch(f"import {module}"), (
        f"{module} pulls in torch. Move the import inside the function that "
        f"needs it, as iron.common.graph and iron.common.sequence do."
    )


@pytest.mark.parametrize("module", TORCH_USING)
def test_the_harness_is_the_one_module_that_takes_torch(module):
    assert _pulls_torch(f"import {module}")


def test_no_operator_pulls_torch_when_it_is_declared():
    """Touching an operator class must cost no more than importing the library.

    Every operator's ``reference`` is written in torch, but only a caller that
    runs the reference should pay for it: declaring, tuning, designing and
    compiling never call it. The operator modules import torch inside those
    functions for that reason, so this is the test that keeps them there.
    """
    assert not _pulls_torch(
        "import iron.operators as ops\n"
        "for name in sorted(ops._OPERATOR_MODULES): getattr(ops, name)\n"
        "from iron.operators.flm import GEMM, Shipped"
    )


def test_a_reference_is_what_brings_torch_in():
    """The other half of the rule: calling one does import torch, as it must.

    The call itself is expected to fail, since the reference wants a tensor
    and gets an array. What is being checked is that the attempt reached the
    function's first line, which is the import -- otherwise this test would
    pass just as well against a module that never deferred anything.
    """
    assert _pulls_torch(
        "import numpy as np, iron.operators as ops\n"
        "try:\n"
        "    ops.ReLU.reference(None, np.zeros(8, dtype=np.float32))\n"
        "except TypeError:\n"
        "    pass"
    )
