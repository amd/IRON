# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from aie.iron.kernels import activation

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Case, Testing, channeled_unary_cases


@operator
class LeakyReLUOverlay(ChanneledUnaryOverlay):
    """The array for Leaky ReLU: the elementwise design with ``alpha`` as a kernel argument."""

    alpha: float = 0.01

    def kernel(self, target):
        # The factory holds what the line length must satisfy: a whole
        # number of the architecture's vectors (16 on aie2, 32 on aie2p).
        return activation.leaky_relu(self.line_size)

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        kernel(elem_in, elem_out, self.line_size, self.alpha)


@operator
class LeakyReLU(ChanneledUnaryOperator[LeakyReLUOverlay]):
    """AIE-accelerated Leaky ReLU operator"""

    test = Testing(
        # The shape sweep at the default alpha, then two more alphas on one
        # small shape in the default suite, so alpha is seen to reach the
        # kernel.
        lambda: (
            channeled_unary_cases([1024, 2048, 4096, 8192], 4096, alpha=0.01)()
            + [
                Case(
                    dict(
                        size=2048,
                        num_aie_columns=1,
                        num_channels=1,
                        tile_size=2048,
                        alpha=a,
                    )
                )
                for a in (0.1, 0.25)
            ]
        ),
        draw=dict(centered=("x",)),
    )

    def reference(self, x):
        return torch.nn.functional.leaky_relu(x, negative_slope=self.ov.alpha)
