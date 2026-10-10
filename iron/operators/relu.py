# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import eltwise

from iron.common import UnaryElementwise
from iron.common.testing import Sweep, Testing


class ReLU(UnaryElementwise):
    """AIE-accelerated ReLU activation function."""

    test = Testing(Sweep(), draw=dict(centered=("x",)))  # both signs

    def kernel(self):
        return eltwise.relu_sized(self.tile_size)
