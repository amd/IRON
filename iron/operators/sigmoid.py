# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import UnaryElementwise


class Sigmoid(UnaryElementwise):
    """AIE-accelerated Sigmoid activation function."""

    def kernel(self):
        return activation.sigmoid(self.tile_size)
