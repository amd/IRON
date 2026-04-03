# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar, Dict

import aie.utils as aie_utils
from iron.common import ChanneledUnaryOperator


@dataclass
class LeakyReLU(ChanneledUnaryOperator):
    """AIE-accelerated Leaky ReLU operator"""

    alpha: float = 0.01

    kernel_name: ClassVar[str] = "leaky_relu"
    callback_fn: ClassVar[str] = "my_leaky_relu"
    _name_aliases: ClassVar[Dict[str, str]] = {
        **ChanneledUnaryOperator._name_aliases,
        "alpha": "a",
    }

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.alpha]
