# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar

from iron.common import ChanneledUnaryOperator


@dataclass
class SiLU(ChanneledUnaryOperator):
    """AIE-accelerated SiLU activation function"""

    num_channels: int = field(default=1, init=False, repr=False)

    kernel_name: ClassVar[str] = "silu"
    kernel_fn_name: ClassVar[str] = "silu_bf16"
    callback_fn: ClassVar[str] = "my_silu"
    needs_lut_ops: ClassVar[bool] = True
