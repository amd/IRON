# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE 2D Convolution Operator

Supports standard 2D convolution with configurable:
- kernel_size
- stride
- padding
- dilation (currently fixed to 1)
- groups (including depthwise convolution)

Works on AIE2 (NPU) and AIE2P (NPU2) architectures.
"""

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging
from pathlib import Path
from typing import Tuple, Union, Optional

import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    AIERuntimeArgSpec,
)


class AIEConv2d(AIEOperatorBase):
    """AIE-accelerated 2D convolution operator"""

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: Union[int, Tuple[int, int]],
        stride: Union[int, Tuple[int, int]] = 1,
        padding: Union[int, Tuple[int, int]] = 0,
        dilation: Union[int, Tuple[int, int]] = 1,
        groups: int = 1,
        use_bias: bool = True,
        in_height: int = 32,
        in_width: int = 32,
        num_aie_columns: int = None,
        tile_size: int = None,
        context=None,
    ):
        """
        Initialize the Conv2d operator.

        Spatial dimensions (in_height, in_width) are part of construction so MLIR
        is specialized correctly for them (removes placeholder hacks and set_up_runtime
        defaults).

        Args:
            in_channels: Number of input channels
            out_channels: Number of output channels
            kernel_size: Size of the convolving kernel (h, w) or single int for square
            stride: Stride of the convolution (default: 1)
            padding: Zero padding added to both sides (default: 0)
            dilation: Spacing between kernel elements (default: 1, only 1 supported)
            groups: Number of blocked connections (default: 1)
            use_bias: Whether to use bias (default: True)
            in_height: Input height (default 32 for backward compat in some paths)
            in_width: Input width (default 32)
            num_aie_columns: Number of AIE columns (1-4 for NPU, 1-8 for NPU2)
            tile_size: Size of each tile in elements
            context: AIE context
        """
        self.in_channels = in_channels
        self.out_channels = out_channels

        # Normalize kernel_size, stride, padding, dilation to tuples
        if isinstance(kernel_size, int):
            kernel_size = (kernel_size, kernel_size)
        if isinstance(stride, int):
            stride = (stride, stride)
        if isinstance(padding, int):
            padding = (padding, padding)
        if isinstance(dilation, int):
            dilation = (dilation, dilation)

        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.groups = groups
        self.use_bias = use_bias
        self.in_height = in_height
        self.in_width = in_width

        # Validate
        assert dilation == (1, 1), "Only dilation=1 is currently supported"
        assert in_channels % groups == 0, "in_channels must be divisible by groups"
        assert out_channels % groups == 0, "out_channels must be divisible by groups"

        # Compute output spatial dimensions (fixed at construction)
        self.out_height = (
            in_height + 2 * self.padding[0] - self.kernel_size[0]
        ) // self.stride[0] + 1
        self.out_width = (
            in_width + 2 * self.padding[1] - self.kernel_size[1]
        ) // self.stride[1] + 1

        # Default tile_size and num_aie_columns
        if tile_size is None:
            tile_size = 2048
        if num_aie_columns is None:
            num_aie_columns = 4

        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns

        # Bias size
        self.bias_size = out_channels if use_bias else 0

        # Artifacts
        self.xclbin_artifact = None
        self.insts_artifact = None
        self.weight_buffer = None
        self.bias_buffer = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts"""
        operator_dir = Path(__file__).parent

        # Determine kernel directory based on device (defensive, no device_manager on current AIEContext)
        # Matches patterns in operator_bases.py and get_params() in test.py
        try:
            dev = aie_utils.get_current_device()
            kernel_dir = "aie2p" if getattr(dev, "cols", 4) > 4 else "aie2"
        except Exception:
            kernel_dir = "aie2"

        file_name_base = (
            f"conv2d_{self.in_channels}_{self.out_channels}_{self.in_height}x{self.in_width}_"
            f"{self.kernel_size[0]}x{self.kernel_size[1]}_"
            f"s{self.stride[0]}x{self.stride[1]}_"
            f"p{self.padding[0]}x{self.padding[1]}_"
            f"g{self.groups}_{self.num_aie_columns}c"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_conv2d",
            callback_kwargs={
                "dev": self.context.device_manager.aie_device,
                "N": 1,  # Will handle batch externally
                "in_channels": self.in_channels,
                "in_height": self.in_height,
                "in_width": self.in_width,
                "out_channels": self.out_channels,
                "out_height": self.out_height,
                "out_width": self.out_width,
                "kernel_h": self.kernel_size[0],
                "kernel_w": self.kernel_size[1],
                "stride_h": self.stride[0],
                "stride_w": self.stride[1],
                "pad_h": self.padding[0],
                "pad_w": self.padding[1],
                "groups": self.groups,
                "use_bias": self.use_bias,
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
                    "conv2d.o",
                    extra_flags=[],
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / kernel_dir
                            / "conv2d.cc"
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
        """
        Set up runtime buffers and kernels.
        Uses spatial dimensions provided at construction time.
        """
        # Buffer sizes based on constructor sizes (MLIR-specialized)
        input_size = self.in_channels * self.in_height * self.in_width
        weight_size = (
            self.out_channels
            * self.in_channels
            // self.groups
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        output_size = self.out_channels * self.out_height * self.out_width

        self.input_size = input_size
        self.weight_size = weight_size
        self.output_size = output_size

        # Add buffers
        self.add_buffer("input", input_size)
        self.add_buffer("weight", weight_size)
        self.add_buffer("output", output_size)

        if self.use_bias:
            self.add_buffer("bias", self.bias_size)

        # Determine kernel name
        kernel_name = "conv2d_bf16_vector"
        if self.groups == self.in_channels and self.groups == self.out_channels:
            kernel_name = "depthwise_conv2d_bf16_vector"
        elif self.kernel_size == (1, 1):
            kernel_name = "pointwise_conv2d_bf16_vector"

        self.add_kernel(
            kernel_name,
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )

        # Build runlist
        if self.use_bias:
            self.add_to_runlist(kernel_name, "input", "weight", "output", "bias")
        else:
            self.add_to_runlist(kernel_name, "input", "weight", "output")

    def forward(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: Optional[torch.Tensor] = None,
    ):
        """
        Forward pass for 2D convolution.

        Args:
            x: Input tensor of shape (N, in_channels, H_in, W_in)
            weight: Weight tensor of shape (out_channels, in_channels/groups, kH, kW)
            bias: Optional bias tensor of shape (out_channels,)

        Returns:
            Output tensor of shape (N, out_channels, H_out, W_out)
        """
        # Get input dimensions
        if len(x.shape) != 4:
            raise AIEOperatorConstraintError(
                f"AIEConv2d expects 4D input (N, C, H, W), got shape {x.shape}"
            )

        batch_size, actual_in_channels, actual_in_height, actual_in_width = x.shape

        # Validate channels and spatial dims (MLIR specialized at ctor time)
        if actual_in_channels != self.in_channels:
            raise AIEOperatorConstraintError(
                f"Expected {self.in_channels} input channels, got {actual_in_channels}"
            )
        if actual_in_height != self.in_height or actual_in_width != self.in_width:
            raise AIEOperatorConstraintError(
                f"AIEConv2d configured for HxW=({self.in_height},{self.in_width}), "
                f"but got input spatial {actual_in_height}x{actual_in_width} (shape {x.shape})"
            )

        # Process batch one at a time (for now)
        outputs = []
        for n in range(batch_size):
            x_n = x[n].contiguous()  # (C, H, W)
            result_n = self._process_single(x_n, weight, bias)
            outputs.append(result_n)

        return torch.stack(outputs, dim=0)

    def _process_single(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: Optional[torch.Tensor] = None,
    ):
        """Process a single sample (C, H, W)"""
        # Flatten input
        x_flat = x.reshape(-1).contiguous()

        # Convert to bfloat16 if needed
        if x_flat.dtype != torch.bfloat16:
            x_flat = x_flat.to(torch.bfloat16)

        # Flatten weight
        weight_flat = weight.reshape(-1).contiguous()
        if weight_flat.dtype != torch.bfloat16:
            weight_flat = weight_flat.to(torch.bfloat16)

        # Handle bias
        bias_flat = None
        if bias is not None and self.use_bias:
            bias_flat = bias.contiguous()
            if bias_flat.dtype != torch.bfloat16:
                bias_flat = bias_flat.to(torch.bfloat16)

        # Write buffers
        self.write_buffer("input", x_flat.numpy())
        self.write_buffer("weight", weight_flat.numpy())

        if bias_flat is not None:
            self.write_buffer("bias", bias_flat.numpy())

        # Initialize output buffer
        output_np = np.zeros(self.output_size, dtype=bfloat16)
        self.write_buffer("output", output_np)

        # Run kernel
        self.run_runlist()

        # Read result
        result = self.read_buffer_as_torch(
            "output",
            shape=(self.out_channels, self.out_height, self.out_width),
            dtype=bfloat16,
        )

        return result

    # -------------------------------------------------------------------------
    # Abstract method implementations required by AIEOperatorBase (post-refactor)
    # Minimal production fix to enable run_test() + metrics path (and forward).
    # These provide the modern callable + arg spec interface used by test_utils
    # and AIEContext high-level paths. Order matches rt.sequence() in design.py
    # (and dict insertion order in test.py input/output_buffers for bias cases).
    # -------------------------------------------------------------------------

    def get_arg_spec(self):
        """Return runtime arg specs matching the kernel launch order from design.py.

        Bias case (rt.sequence order): in, weight, bias, out
        No-bias: in, weight, out

        This also matches the insertion order of input_buffers/output_buffers
        passed by the metrics test_conv2d and the FORWARD_CASES.
        """
        specs = [
            AIERuntimeArgSpec("in", (self.input_size,)),
            AIERuntimeArgSpec("in", (self.weight_size,)),
        ]
        if self.use_bias and getattr(self, "bias_size", 0) > 0:
            specs.append(AIERuntimeArgSpec("in", (self.bias_size,)))
        specs.append(AIERuntimeArgSpec("out", (self.output_size,)))
        return specs

    def get_callable(self):
        """Return a callable that executes the compiled kernel on the NPU.

        Uses the same NPUKernel / DefaultNPURuntime pattern as MLIROperator
        for compatibility with run_test() buffer passing and XRT execution.
        The arg order passed at call time must match get_arg_spec().
        """
        # Ensure we have the artifacts (caller should have done compile())
        if self.xclbin_artifact is None or self.insts_artifact is None:
            # Defensive: set_up_artifacts should have populated via compile()
            self.set_up_artifacts()
        npu_kernel = NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_path=self.insts_artifact.filename,
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call
