# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import BinaryElementwiseOperator


@dataclass
class ElementwiseAdd(BinaryElementwiseOperator):
    """AIE-accelerated element-wise addition"""

    kernel_name: ClassVar[str] = "add"
    kernel_fn_name: ClassVar[str] = "eltwise_add_bf16_vector"
    kernel_subdir: ClassVar[str] = "generic"
    callback_fn: ClassVar[str] = "my_eltwise_add"
