# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator


@dataclass
class Tanh(ChanneledUnaryOperator):
    """AIE-accelerated Tanh activation function"""

    callback_fn: ClassVar[str] = "my_tanh"

    def _kernel(self):
        return activation.tanh(self._line_size)
