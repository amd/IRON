# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import UnaryElementwise


class Sigmoid(UnaryElementwise):
    """AIE-accelerated Sigmoid activation function."""

    class Array(UnaryElementwise.Array):
        def kernel(self):
            # On aie2p, vtanh is up to 0.020 off sigmoid and the table 0.0044 (npu2).
            return activation.sigmoid(self.tile_size, use_lut=True)
