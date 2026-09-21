# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

import numpy as np
import torch

from iron.common import BinaryElementwiseOperator, BinaryElementwiseOverlay, operator
from iron.common.test_utils import torch_dtype_map


@operator
class AXPYOverlay(BinaryElementwiseOverlay):
    """The array for aX + Y: the binary-elementwise design with the scalar as a kernel argument."""

    scalar_factor: float = 3.0

    kernel_name: ClassVar[str] = "axpy"
    kernel_fn_name: ClassVar[str] = "saxpy"

    def kernel_source(self, target):
        # axpy.cc is architecture-independent and lives under generic/.
        return target.kernels_dir / "generic" / "axpy.cc"

    def kernel_arg_types(self, tile_type) -> list:
        return [tile_type, tile_type, np.float32, tile_type, np.int32]

    def kernel_call(self, kernel, elem_a, elem_b, elem_out) -> None:
        kernel(elem_a, elem_b, self.scalar_factor, elem_out, self.per_tile)


@operator
class AXPY(BinaryElementwiseOperator[AXPYOverlay]):
    """AIE-accelerated aX + Y operator"""

    pass


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length: int, scalar=3.0, dtype="bf16", seed=42):
    torch.manual_seed(seed)
    val_range = 4
    dtype_torch = torch_dtype_map[dtype]
    A = torch.rand(input_length, dtype=dtype_torch) * val_range
    B = torch.rand(input_length, dtype=dtype_torch) * val_range
    s = torch.tensor(scalar, dtype=dtype_torch)

    # Generate golden outputs
    C = s * A + B

    return {
        "A": A,
        "B": B,
        "C": C,
    }
