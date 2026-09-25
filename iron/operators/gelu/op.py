# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator


@dataclass
class GELU(ChanneledUnaryOperator):
    """AIE-accelerated GELU activation function"""

    callback_fn: ClassVar[str] = "my_gelu"
    tile_cap: ClassVar[int] = 8192

    def _kernel(self):
        return activation.gelu_sized(self._line_size)
