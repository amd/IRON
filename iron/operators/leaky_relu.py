# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.testing import Case, Testing, channeled_unary_cases


@operator
class LeakyReLUOverlay(ChanneledUnaryOverlay):
    """The array for Leaky ReLU: the channeled-unary design with ``alpha`` as a kernel argument."""

    alpha: float = 0.01

    kernel_name: ClassVar[str] = "leaky_relu"
    kernel_fn_name: ClassVar[str] = "leaky_relu_bf16"
    kernel_object: ClassVar[str] = "leaky_relu.o"  # as the old design named it

    # Minimum per-core line length (in bfloat16 elements) required by the
    # vectorized kernels. They tell the pipeliner a minimum loop-trip count via
    # AIE_LOOP_MIN_ITERATION_COUNT -- a hard contract under xchesscc -- so that
    # promise must be backed by a lower bound on the line length, or the
    # compiler may drop the low-trip guard and corrupt results. The kernels
    # vectorize by 16 (aie2) or 32 (aie2p) elements and promise 4 / 2 iterations
    # respectively, i.e. at least 64 elements per line.
    min_line_size: ClassVar[int] = 64

    def validate(self) -> None:
        line_size = min(self.tile_size, self.tile_cap)
        if line_size < self.min_line_size:
            raise ValueError(
                f"tile_size ({self.tile_size}) yields a per-core line of "
                f"{line_size} bfloat16 elements; leaky_relu requires at least "
                f"{self.min_line_size} to satisfy the kernel's minimum "
                f"loop-iteration promise"
            )

    # Leaky ReLU's kernel takes: input, output, input_size, alpha
    def kernel_arg_types(self, line_type) -> list:
        return [line_type, line_type, np.int32, bfloat16]

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
