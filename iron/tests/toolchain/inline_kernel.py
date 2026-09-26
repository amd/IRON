# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A hello-world operator: its kernel is C++ text in the same file.

The elementwise template owns the array and the sequence; the operator
names the kernel each core calls, here written inline rather than taken from
a shipped factory, and its reference. It lowers through the toolchain like
any other, the kernel compiled from the text.
"""

import numpy as np

from iron.common import BinaryElementwise
from iron.tests.toolchain.lowering import lower
from iron.tests.toolchain.tools import requires

pytestmark = requires("aiecc")

VADD = """
#include <aie_api/aie.hpp>

extern "C" void vadd(bfloat16 *a, bfloat16 *b, bfloat16 *y, int n) {
    for (int i = 0; i < n; i++)
        y[i] = a[i] + b[i];
}
"""


class VectorAdd(BinaryElementwise):
    """y = a + b."""

    def kernel(self, target):
        tiles = [self.a.tile, self.b.tile, self.y.tile, np.int32]
        return target.kernel("vadd", tiles, source_text=VADD)

    def reference(self, a, b):
        return a + b


def test_an_inline_kernel_lowers(device, tmp_path):
    op = VectorAdd(size=1024, num_aie_columns=2, tile_size=256).resolved(device)
    src, insts = lower(op, tmp_path)
    assert "vadd" in src.read_text()
