# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import ChanneledUnaryOperator


@dataclass
class Tanh(ChanneledUnaryOperator):
    """AIE-accelerated Tanh activation function"""

    kernel_name: ClassVar[str] = "tanh"
    kernel_fn_name: ClassVar[str] = "tanh_bf16"
    needs_lut_ops: ClassVar[bool] = True
    callback_fn: ClassVar[str] = "my_tanh"
