# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE 2D MaxPool Operator

Supports 2D max pooling with configurable:
- kernel_size
- stride
- padding
- dilation (currently fixed to 1)

Works on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging
from pathlib import Path
from typing import Tuple, Union, Optional

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEMaxPool2d(AIEOperatorBase):
    """AIE-accelerated 2D max pooling operator"""

    def __init__(
        self,
        kernel_size: Union[int, Tuple[int, int]],
        stride: Union[int, Tuple[int, int]] = None,
        padding: Union[int, Tuple[int, int]] = 0,
        dilation: Union[int, Tuple[int, int]] = 1,
        num_aie_columns: int = None,
        tile_size: int = None,
        context=None,
    ):
        """
        Initialize the MaxPool2d operator.

        Args:
            kernel_size: Size of pooling window (h, w) or single int for square
            stride: Stride of pooling window (default: kernel_size)
            padding: Zero padding added to both sides (default: 0)
            dilation: Spacing between kernel elements (default: 1, only 1 supported)
            num_aie_columns: Number of AIE columns (1-4 for NPU, 1-8 for NPU2)
            tile_size: Size of each tile in elements
            context: AIE context
        """
        # Normalize kernel_size, stride, padding, dilation to tuples
        if isinstance(kernel_size, int):
            kernel_size = (kernel_size, kernel_size)
        if stride is None:
            stride = kernel_size
        elif isinstance(stride, int):
            stride = (stride, stride)
        if isinstance(padding, int):
            padding = (padding, padding)
        if isinstance(dilation, int):
            dilation = (dilation, dilation)

        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation

        # Validate
        assert dilation == (1, 1), "Only dilation=1 is currently supported"

        # Default tile_size and num_aie_columns
        if tile_size is None:
            tile_size = 2048
        if num_aie_columns is None:
            num_aie_columns = 4

        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns

        # Artifacts
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts"""
        operator_dir = Path(__file__).parent

        # Determine kernel directory based on device
        kernel_dir = (
            "aie2p" if self.context.device_manager.device_str() == "npu2" else "aie2"
        )

        file_name_base = (
            f"maxpool_{self.kernel_size[0]}x{self.kernel_size[1]}_"
            f"s{self.stride[0]}x{self.stride[1]}_"
            f"p{self.padding[0]}x{self.padding[1]}_"
            f"{self.num_aie_columns}c"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_max_pool2d",
            callback_kwargs={
                "dev": self.context.device_manager.device_str(),
                "N": 1,  # Will handle batch externally
                "channels": 16,  # Placeholder - actual size at runtime
                "in_height": 32,  # Placeholder - actual size at runtime
                "in_width": 32,
                "out_height": 16,  # Placeholder
                "out_width": 16,
                "kernel_h": self.kernel_size[0],
                "kernel_w": self.kernel_size[1],
                "stride_h": self.stride[0],
                "stride_w": self.stride[1],
                "pad_h": self.padding[0],
                "pad_w": self.padding[1],
                "num_columns": self.num_aie_columns,
                "tile_size": self.tile_size,
                "trace_size": 0,
            },
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "maxpool.o",
                    extra_flags=[],
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / kernel_dir
                            / "maxpool.cc"
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

    def set_up_runtime(self, channels: int, in_height: int, in_width: int):
        """
        Set up runtime buffers and kernels.

        Args:
            channels: Number of channels
            in_height: Input height
            in_width: Input width
        """
        # Calculate output dimensions
        out_height = (
            in_height + 2 * self.padding[0] - self.kernel_size[0]
        ) // self.stride[0] + 1
        out_width = (
            in_width + 2 * self.padding[1] - self.kernel_size[1]
        ) // self.stride[1] + 1

        # Calculate buffer sizes
        input_size = channels * in_height * in_width
        output_size = channels * out_height * out_width

        self.input_size = input_size
        self.output_size = output_size
        self.channels = channels
        self.in_height = in_height
        self.in_width = in_width
        self.out_height = out_height
        self.out_width = out_width

        # Add buffers
        self.add_buffer("input", input_size)
        self.add_buffer("output", output_size)

        # Add kernel
        self.add_kernel(
            "max_pool2d_bf16_vector",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )

        # Build runlist
        self.add_to_runlist("max_pool2d_bf16_vector", "input", "output")

    def forward(
        self,
        x: torch.Tensor,
    ) -> torch.Tensor:
        """
        Forward pass for 2D max pooling.

        Args:
            x: Input tensor of shape (N, C, H_in, W_in)

        Returns:
            Output tensor of shape (N, C, H_out, W_out)
        """
        # Get input dimensions
        if len(x.shape) != 4:
            raise AIEOperatorConstraintError(
                f"AIEMaxPool2d expects 4D input (N, C, H, W), got shape {x.shape}"
            )

        batch_size, channels, in_height, in_width = x.shape

        # Setup runtime with actual dimensions if not already done
        if not hasattr(self, "in_height") or self.in_height != in_height:
            self.set_up_runtime(channels, in_height, in_width)

        # Process batch one at a time (for now)
        outputs = []
        for n in range(batch_size):
            x_n = x[n].contiguous()  # (C, H, W)
            result_n = self._process_single(x_n)
            outputs.append(result_n)

        return torch.stack(outputs, dim=0)

    def _process_single(
        self,
        x: torch.Tensor,
    ) -> torch.Tensor:
        """Process a single sample (C, H, W)"""
        # Flatten input
        x_flat = x.reshape(-1).contiguous()

        # Convert to bfloat16 if needed
        if x_flat.dtype != torch.bfloat16:
            x_flat = x_flat.to(torch.bfloat16)

        # Write input buffer
        self.write_buffer("input", x_flat.numpy())

        # Initialize output buffer
        output_np = np.zeros(self.output_size, dtype=bfloat16)
        self.write_buffer("output", output_np)

        # Run kernel
        self.run_runlist()

        # Read result
        result = self.read_buffer_as_torch(
            "output",
            shape=(self.channels, self.out_height, self.out_width),
            dtype=bfloat16,
        )

        return result
