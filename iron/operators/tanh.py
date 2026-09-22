# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import torch

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Testing, channeled_unary_cases
from iron.operators._kernels import lut_sources


@operator
class TanhOverlay(ChanneledUnaryOverlay):
    """The array for Tanh: the shared elementwise design over its kernel."""

    def kernel(self, target):
        # ``aie.iron.kernels.activation.tanh`` is this kernel, but it accepts
        # only 1024-element tiles although ``tanh_bf16`` reads the count at
        # runtime. Declared here until that restriction is lifted upstream.
        line = self.x.tile
        return target.kernel(
            "tanh_bf16",
            [line, line, np.int32],
            source=target.kernel_source("tanh"),
            bundled_sources=lut_sources(target.dev),
        )


@operator
class Tanh(ChanneledUnaryOperator[TanhOverlay]):
    """AIE-accelerated Tanh activation function"""

    test = Testing(channeled_unary_cases([1024, 2048, 4096, 8192], 4096))

    def reference(self, x):
        return torch.tanh(x)
