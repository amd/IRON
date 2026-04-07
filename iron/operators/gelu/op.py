# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import ChanneledUnaryOperator


@dataclass
class GELU(ChanneledUnaryOperator):
    """AIE-accelerated GELU activation function"""

    kernel_name: ClassVar[str] = "gelu"
    kernel_fn_name: ClassVar[str] = "gelu_bf16"
    needs_lut_ops: ClassVar[bool] = True
    callback_fn: ClassVar[str] = "my_gelu"
    tile_cap: ClassVar[int] = 8192
