# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar, Dict

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common import ChanneledUnaryOperator, ChanneledUnaryOverlay, operator
from iron.common.test_utils import torch_dtype_map


@operator
class LeakyReLUOverlay(ChanneledUnaryOverlay):
    """The array for Leaky ReLU: the channeled-unary design with ``alpha`` as a kernel argument."""

    alpha: float = 0.01

    kernel_name: ClassVar[str] = "leaky_relu"
    kernel_fn_name: ClassVar[str] = "leaky_relu_bf16"

    _name_aliases: ClassVar[Dict[str, str]] = {"alpha": "a"}

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

    pass


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length: int, alpha=0.01, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(input_length, dtype=torch_dtype_map[dtype]) * val_range
        - val_range / 2
    )
    output_tensor = torch.nn.functional.leaky_relu(input_tensor, negative_slope=alpha)
    return {"input": input_tensor, "output": output_tensor}
