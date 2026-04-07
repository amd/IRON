# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import ChanneledUnaryOperator


@dataclass
class ReLU(ChanneledUnaryOperator):
    """AIE-accelerated ReLU activation function"""

    kernel_name: ClassVar[str] = "relu"
    kernel_fn_name: ClassVar[str] = "relu_bf16"
    callback_fn: ClassVar[str] = "my_relu"
