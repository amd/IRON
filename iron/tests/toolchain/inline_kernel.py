# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A hello-world operator: its kernel is C++ text in the same file.

The elementwise template owns the array and the sequence; the operator
names the kernel each core calls, here written inline rather than taken from
a shipped factory. Its contract says what a factory's would: the line
length is bound, so a core passes the elements alone, and the reference is
what the operator is tested against. It lowers through the toolchain like
any other, the kernel compiled from the text.
"""

import numpy as np
from aie.iron import ExternalFunction
from aie.iron.kernels import KernelContract, Param
from aie.utils.compile.jit.markers import In, Out
from ml_dtypes import bfloat16

from iron.common import BinaryElementwise
from iron.tests.toolchain.lowering import lower
from iron.tests.toolchain.tools import requires

pytestmark = requires("aiecc", "peano")

VADD = """
#include <aie_api/aie.hpp>

extern "C" void vadd(bfloat16 *a, bfloat16 *b, bfloat16 *y, int n) {
    for (int i = 0; i < n; i++)
        y[i] = a[i] + b[i];
}
"""


class VectorAdd(BinaryElementwise):
    """y = a + b."""

    def kernel(self):
        tiles = [self.a.tile, self.b.tile, self.y.tile, np.int32]
        contract = KernelContract(
            roles=(In, In, Out, Param),
            parameter_bindings=((3, self.tile_size),),
            reference=lambda a, b: a + b,
        )
        return ExternalFunction(
            "vadd",
            source_string=VADD,
            arg_types=tiles,
            contract=contract,
        )


def test_an_inline_kernel_lowers(device, tmp_path):
    op = VectorAdd(size=1024, num_aie_columns=2, tile_size=256).resolved(device)
    src, insts = lower(op, tmp_path)
    mlir = src.read_text()
    assert "vadd" in mlir
    # A core passes the elements; the contract's binding is the line length.
    assert "arith.constant 256 : i32" in mlir


def test_its_reference_is_the_contracts(device):
    op = VectorAdd(size=1024, num_aie_columns=2, tile_size=256).resolved(device)
    a, b = (np.arange(1024).astype(bfloat16) for _ in range(2))
    np.testing.assert_array_equal(op.reference(a, b), np.add(a, b))
