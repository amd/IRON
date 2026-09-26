# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import eltwise

from iron.common import BinaryElementwise


class ElementwiseMul(BinaryElementwise):
    """AIE-accelerated element-wise multiplication."""

    def kernel(self, target):
        return eltwise.mul_sized(self.tile_size)

    def reference(self, a, b):
        return a * b
