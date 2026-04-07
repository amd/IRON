# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, InitVar
from typing import ClassVar

import aie.utils as aie_utils
from iron.common import ChanneledUnaryOperator


@dataclass
class LayerNorm(ChanneledUnaryOperator):
    """AIE-accelerated Layer Normalization operator"""

    trace_size: InitVar[int] = 0

    kernel_name: ClassVar[str] = "layer_norm"
    kernel_fn_name: ClassVar[str] = "layer_norm"
    callback_fn: ClassVar[str] = "my_layer_norm"
    tile_cap: ClassVar[int] = 8192

    def __post_init__(self, trace_size):
        self.trace_size = trace_size
        super().__post_init__()

    def _mlir_callback_args(self):
        return [
            aie_utils.get_current_device(),
            self.size,
            self.num_aie_columns,
            self.num_channels,
            self.tile_size,
            self.trace_size,
        ]
