# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import UnaryElementwise


class Tanh(UnaryElementwise):
    """AIE-accelerated Tanh activation function."""

    def kernel(self, target):
        return activation.tanh(self.tile_size)
