# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE Reduction Operator

Supports sum, mean, max, min reduction along the last dimension.
Works on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging
from pathlib import Path
from typing import Literal

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)

ReductionOp = Literal["sum", "mean", "max", "min"]


class AIEReduction(AIEOperatorBase):
    """AIE-accelerated reduction operator"""

    def __init__(
        self,
        input_size: int,
        reduction_size: int,
        reduction_op: ReductionOp = "sum",
        num_aie_columns: int = None,
        tile_size: int = None,
        context=None,
    ):
        """
        Initialize the Reduction operator.

        Args:
            input_size: Total size of input tensor (flattened)
            reduction_size: Size of the dimension being reduced
            reduction_op: Type of reduction ("sum", "mean", "max", "min")
            num_aie_columns: Number of AIE columns to use (1-4 for NPU, 1-8 for NPU2)
            tile_size: Size of each tile in elements
            context: AIE context
        """
        self.input_size = input_size
        self.reduction_size = reduction_size
        self.reduction_op = reduction_op

        # Output size is input_size / reduction_size
        self.output_size = input_size // reduction_size

        # Default tile_size and num_aie_columns if not specified
        if tile_size is None:
            tile_size = 1024

        if num_aie_columns is None:
            num_aie_columns = 4  # Default to 4 columns

        # Validate reduction_op
        assert reduction_op in [
            "sum",
            "mean",
            "max",
            "min",
        ], f"Unknown reduction op: {reduction_op}"

        # Mean is only supported on AIE2P
        self.supports_mean = True  # Will be checked at runtime

        # Calculate padded size
        max_multiple = num_aie_columns * tile_size
        padded_size = ((input_size + max_multiple - 1) // max_multiple) * max_multiple

        self.orig_input_size = input_size
        self.input_size = padded_size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns

        # Recompute output size with padded input
        self.output_size = padded_size // reduction_size

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts"""
        operator_dir = Path(__file__).parent

        file_name_base = (
            f"reduction_{self.reduction_op}_{self.num_aie_columns}c_"
            f"{self.input_size}_{self.reduction_size}_{self.tile_size}t"
        )

        # Determine which kernel archive to use based on device
        kernel_dir = (
            "aie2p" if self.context.device_manager.device_str() == "npu2" else "aie2"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_reduction",
            callback_kwargs={
                "dev": self.context.device_manager.device_str(),
                "input_size": self.input_size,
                "reduction_size": self.reduction_size,
                "num_columns": self.num_aie_columns,
                "tile_size": self.tile_size,
                "reduction_op": self.reduction_op,
                "trace_size": 0,
            },
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "reduction.o",
                    extra_flags=[],
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / kernel_dir
                            / "reduction.cc"
                        )
                    ],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin",
            depends=[mlir_artifact],
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        """Set up runtime buffers and kernels"""
        self.add_buffer("input", self.input_size)
        self.add_buffer("output", self.output_size)

        self.add_kernel(
            f"reduction_{self.reduction_op}",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )

        self.add_to_runlist(f"reduction_{self.reduction_op}", "input", "output")

    def forward(self, x: torch.Tensor, dim: int = -1):
        """
        Forward pass for reduction operation.

        Args:
            x: Input tensor of any shape
            dim: Dimension to reduce along (default: -1)

        Returns:
            Reduced tensor
        """
        # Handle negative dim
        if dim < 0:
            dim = x.dim() + dim

        # Get the reduction size from the actual tensor
        actual_reduction_size = x.shape[dim]

        # Validate reduction size matches configuration
        if actual_reduction_size != self.reduction_size:
            # Try to handle by reshaping if possible
            if x.numel() == self.input_size:
                # Reshape to match expected size
                x = x.view(-1)
            else:
                raise AIEOperatorConstraintError(
                    f"AIEReduction: reduction dimension size {actual_reduction_size} "
                    f"doesn't match configured size {self.reduction_size}"
                )

        # Flatten tensor for AIE processing
        original_shape = x.shape
        x_flat = x.reshape(-1)

        # Pad if necessary
        pad_len = self.input_size - x_flat.numel()
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))

        # Execute AIE operation
        result_flat = self._execute_aie_operation(x_flat)

        # Reshape result
        # Calculate expected output shape
        expected_output_shape = list(original_shape)
        expected_output_shape[dim] = 1  # Reduced dimension becomes 1
        # Then squeeze out the reduced dimension
        expected_output_shape = [
            s for i, s in enumerate(expected_output_shape) if i != dim or s != 1
        ]

        # Actually compute output size
        total_elements = x.numel() // self.reduction_size
        result = result_flat[:total_elements]
        result = result.reshape(*expected_output_shape)

        return result

    def _execute_aie_operation(self, x: torch.Tensor):
        """
        Execute reduction operation on AIE hardware.

        Args:
            x: Flattened input tensor

        Returns:
            Flattened result tensor
        """
        # Verify size matches expected
        if len(x) != self.input_size:
            raise AIEOperatorConstraintError(
                f"Input size {len(x)} doesn't match configured size {self.input_size}"
            )

        # Write input
        self.write_buffer("input", x)

        # Initialize output buffer
        test_pattern = np.zeros(self.output_size, dtype=bfloat16)
        self.write_buffer("output", test_pattern)

        # Run the kernel
        self.run_runlist()

        # Read result
        result = self.read_buffer_as_torch(
            "output", shape=(self.output_size,), dtype=bfloat16
        )

        return result
