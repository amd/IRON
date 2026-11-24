# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any, ClassVar

import numpy as np
from aie.iron.kernels import eltwise
from ml_dtypes import bfloat16

from iron.common import BinaryElementwise, RowBroadcast
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class ElementwiseAdd(BinaryElementwise):
    """AIE-accelerated element-wise addition, bf16 or float32."""

    test = Testing(
        [
            Sweep(channels=None),
            Case(dict(size=4096, tile_size=1024, dtype=np.float32), id="float32"),
        ]
    )
    dtypes: ClassVar[tuple[Any, ...]] = (bfloat16, np.float32)

    def kernel(self):
        return eltwise.add_sized(self.tile_size, self.dtype)


class RowwiseAdd(RowBroadcast):
    """Each row plus one row, ``x + row``: a projection's bias."""

    tile_cap: ClassVar[int] = 4096

    def kernel(self):
        return eltwise.add_sized(self.line)
