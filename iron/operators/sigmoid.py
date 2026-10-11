# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import UnaryElementwise, auto


class Sigmoid(UnaryElementwise):
    """AIE-accelerated Sigmoid activation function."""

    # False matches the hardware's own default (the vtanh instruction);
    # True trades it for the interpolated LUT, ~7.5x closer to the exact
    # function (see aie.iron.kernels.activation.tanh).
    use_lut: bool = auto(False, array=True)

    def kernel(self):
        return activation.sigmoid(self.tile_size, use_lut=self.use_lut)
