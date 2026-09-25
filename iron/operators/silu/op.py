# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator


@dataclass
class SiLU(ChanneledUnaryOperator):
    """AIE-accelerated SiLU activation function"""

    num_channels: int = field(default=1, init=False, repr=False)

    callback_fn: ClassVar[str] = "my_silu"

    def _kernel(self):
        return activation.silu_sized(self._line_size)

    def reference(self, x):
        from iron.operators.silu.reference import reference

        return reference(x)
