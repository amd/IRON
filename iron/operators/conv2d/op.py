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

NPU dataflow notes (see design.py MODELING STATUS):
- Single-column full-tensor path (kernels expect full NCHW / weights).
- Bias is applied on the host after the NPU kernel (compute tiles only have
  2 input DMA channels; a third bias ObjectFifo is illegal).
"""

import torch
import numpy as np
from ml_dtypes import bfloat16
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
    DesignGenerator,
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
        is specialized correctly for them.

        Args:
            in_channels: Number of input channels
            out_channels: Number of output channels
            kernel_size: Size of the convolving kernel (h, w) or single int for square
            stride: Stride of the convolution (default: 1)
            padding: Zero padding added to both sides (default: 0)
            dilation: Spacing between kernel elements (default: 1, only 1 supported)
            groups: Number of blocked connections (default: 1)
            use_bias: Whether to use bias (default: True). Bias is applied on host
                after the NPU convolution (DMA channel limit on compute tiles).
            in_height: Input height (default 32)
            in_width: Input width (default 32)
            num_aie_columns: Requested columns (currently forced to 1 in design)
            tile_size: Size of each tile in elements (reserved / unused for 1-col)
            context: AIE context
        """
        self.in_channels = in_channels
        self.out_channels = out_channels

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

        assert dilation == (1, 1), "Only dilation=1 is currently supported"
        assert in_channels % groups == 0, "in_channels must be divisible by groups"
        assert out_channels % groups == 0, "out_channels must be divisible by groups"

        self.out_height = (
            in_height + 2 * self.padding[0] - self.kernel_size[0]
        ) // self.stride[0] + 1
        self.out_width = (
            in_width + 2 * self.padding[1] - self.kernel_size[1]
        ) // self.stride[1] + 1

        if tile_size is None:
            tile_size = 2048
        if num_aie_columns is None:
            num_aie_columns = 1

        # Design forces 1 column; store requested value for diagnostics only.
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        self.effective_num_columns = 1

        self.bias_size = out_channels if use_bias else 0

        self.xclbin_artifact = None
        self.insts_artifact = None
        self.weight_buffer = None
        self.bias_buffer = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        """Set up compilation artifacts for the 1-col full-tensor design."""
        operator_dir = Path(__file__).parent
        design_path = operator_dir / "design.py"

        try:
            dev = aie_utils.get_current_device()
            kernel_dir = "aie2p" if getattr(dev, "cols", 4) > 4 else "aie2"
        except Exception:
            kernel_dir = "aie2"
            dev = None

        if dev is None:
            try:
                dev = aie_utils.get_current_device()
            except Exception:
                from aie.iron.device import NPU1

                dev = NPU1()

        # Artifact names use effective (1) column count to match design emission.
        effective_num_columns = self.effective_num_columns

        file_name_base = (
            f"conv2d_{self.in_channels}_{self.out_channels}_{self.in_height}x{self.in_width}_"
            f"{self.kernel_size[0]}x{self.kernel_size[1]}_"
            f"s{self.stride[0]}x{self.stride[1]}_"
            f"p{self.padding[0]}x{self.padding[1]}_"
            f"g{self.groups}_{effective_num_columns}c"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact(
            f"{file_name_base}.mlir",
            DesignGenerator(
                design_path,
                "my_conv2d",
                args=(),
                kwargs={
                    "dev": dev,
                    "N": 1,
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
                    "num_columns": effective_num_columns,
                    "tile_size": self.tile_size,
                    "trace_size": 0,
                },
            ),
        )

        kernel_obj = KernelObjectArtifact(
            "conv2d.o",
            dependencies=[
                SourceArtifact(
                    self.context.base_dir / "aie_kernels" / kernel_dir / "conv2d.cc"
                )
            ],
        )

        xclbin_artifact = XclbinArtifact(
            f"{file_name_base}.xclbin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact, kernel_obj],
            extra_flags=[],
        )

        insts_artifact = InstsBinArtifact(
            f"{file_name_base}.bin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact],
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        """Set up runtime buffers and kernels (legacy path)."""
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

        self.add_buffer("input", input_size)
        self.add_buffer("weight", weight_size)
        self.add_buffer("output", output_size)

        if self.use_bias:
            self.add_buffer("bias", self.bias_size)

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

        # NPU runlist is always 3 buffers (bias is host-side).
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
        if len(x.shape) != 4:
            raise AIEOperatorConstraintError(
                f"AIEConv2d expects 4D input (N, C, H, W), got shape {x.shape}"
            )

        batch_size, actual_in_channels, actual_in_height, actual_in_width = x.shape

        if actual_in_channels != self.in_channels:
            raise AIEOperatorConstraintError(
                f"Expected {self.in_channels} input channels, got {actual_in_channels}"
            )
        if actual_in_height != self.in_height or actual_in_width != self.in_width:
            raise AIEOperatorConstraintError(
                f"AIEConv2d configured for HxW=({self.in_height},{self.in_width}), "
                f"but got input spatial {actual_in_height}x{actual_in_width} (shape {x.shape})"
            )

        outputs = []
        for n in range(batch_size):
            x_n = x[n].contiguous()
            result_n = self._process_single(x_n, weight, bias)
            outputs.append(result_n)

        return torch.stack(outputs, dim=0)

    def _process_single(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: Optional[torch.Tensor] = None,
    ):
        """Process a single sample (C, H, W). Bias applied on host after NPU."""
        x_flat = x.reshape(-1).contiguous()
        if x_flat.dtype != torch.bfloat16:
            x_flat = x_flat.to(torch.bfloat16)

        weight_flat = weight.reshape(-1).contiguous()
        if weight_flat.dtype != torch.bfloat16:
            weight_flat = weight_flat.to(torch.bfloat16)

        self.write_buffer("input", x_flat.numpy())
        self.write_buffer("weight", weight_flat.numpy())

        output_np = np.zeros(self.output_size, dtype=bfloat16)
        self.write_buffer("output", output_np)

        self.run_runlist()

        result = self.read_buffer_as_torch(
            "output",
            shape=(self.out_channels, self.out_height, self.out_width),
            dtype=bfloat16,
        )

        if self.use_bias and bias is not None:
            b = bias.contiguous()
            if b.dtype != torch.bfloat16:
                b = b.to(torch.bfloat16)
            result = result + b.reshape(self.out_channels, 1, 1)

        return result

    def _host_apply_bias(self, out_buf, bias_buf) -> None:
        """In-place host bias add on XRT output buffer (bf16).

        Uses to_torch() so any device→host sync performed by the runtime is
        honored, then writes the summed result back through the mapped ``data``
        view (verified writable for XRTTensor).
        """
        out_t = out_buf.to_torch().reshape(
            self.out_channels, self.out_height, self.out_width
        )
        bias_t = (
            bias_buf.to_torch().to(dtype=out_t.dtype).reshape(self.out_channels, 1, 1)
        )
        summed = (out_t + bias_t).contiguous().reshape(-1)
        # Convert torch bf16 → numpy bf16 without float32 round-trip when possible.
        if summed.dtype == torch.bfloat16:
            np_sum = (
                summed.detach()
                .cpu()
                .view(torch.uint16)
                .numpy()
                .view(np.dtype("bfloat16"))
            )
        else:
            np_sum = summed.detach().cpu().numpy().astype(bfloat16, copy=False)
        out_buf.data.reshape(-1)[:] = np_sum
        # Critical: to_torch()/numpy() sync FROM device and would wipe host
        # writes unless we push the biased result back to the device BO.
        if hasattr(out_buf, "_sync_to_device"):
            out_buf._sync_to_device()

    def get_arg_spec(self):
        """Runtime arg specs for run_test / high-level path.

        Host-facing order:
          - with bias: in, weight, bias, out  (bias applied on host after NPU)
          - without:   in, weight, out

        NPU instruction sequence is always (in, weight, out); get_callable
        strips the bias buffer before DefaultNPURuntime.run.
        """
        # Sizes used by run_test buffer allocation / XRTTensor shapes.
        input_size = self.in_channels * self.in_height * self.in_width
        weight_size = (
            self.out_channels
            * self.in_channels
            // self.groups
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        output_size = self.out_channels * self.out_height * self.out_width
        # Cache for legacy paths that read these attributes.
        self.input_size = input_size
        self.weight_size = weight_size
        self.output_size = output_size

        specs = [
            AIERuntimeArgSpec("in", (input_size,)),
            AIERuntimeArgSpec("in", (weight_size,)),
        ]
        if self.use_bias and self.bias_size > 0:
            specs.append(AIERuntimeArgSpec("in", (self.bias_size,)))
        specs.append(AIERuntimeArgSpec("out", (output_size,)))
        return specs

    def get_callable(self):
        """Callable that runs NPU conv then optionally applies host-side bias."""
        if self.xclbin_artifact is None or self.insts_artifact is None:
            self.set_up_artifacts()
        npu_kernel = NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=self.xclbin_artifact.kernel_name,
            insts_path=self.insts_artifact.filename,
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)
        use_bias = self.use_bias and self.bias_size > 0

        def call(*args):
            if use_bias:
                if len(args) != 4:
                    raise ValueError(
                        f"AIEConv2d with bias expects 4 args (in, weight, bias, out), got {len(args)}"
                    )
                in_b, w_b, bias_b, out_b = args
                result = aie_utils.DefaultNPURuntime.run(handle, [in_b, w_b, out_b])
                self._host_apply_bias(out_b, bias_b)
                return result
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call
