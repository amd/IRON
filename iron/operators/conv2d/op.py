# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
AIE 2D Convolution Operator (AIE2 / AIE2P, bfloat16).

Configurable kernel_size, stride, padding, groups (incl. depthwise).
Dilation is fixed to 1. Bias is packed on-device as ``weights‖bias`` in the
weight ObjectFifo (still ≤2 input DMAs: input + packed weight); kernels use
``apply_bias=1``. Construct-time checks enforce column policy and L1 triple
budget (including packed bias) via AIEOperatorConstraintError.
"""

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path
from typing import Tuple, Union, Optional, Callable, Any

import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

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

# Shared L1 / column policy with design.py (single source of truth).
from iron.operators.conv2d.design import (
    _BYTES_PER_BF16,
    _L1_TRIPLE_BUDGET_BYTES,
    _bias_per_oc,
    _choose_channel_tile,
    _choose_h_tile_pointwise,
    _choose_h_tile_standard,
    _choose_oc_tile,
    _l1_triple_fits,
    _plan_halo_h_strip,
    _resolve_num_columns,
    _rf_in_h,
    pack_weights_with_bias,
)


class AIEConv2d(AIEOperatorBase):
    """AIE-accelerated 2D convolution operator (bf16, AIE2 / AIE2P).

    **Supported (current product surface)**

    - ``dtype``: bfloat16 activations/weights (host torch API).
    - ``kernel_size``, ``stride``, ``padding``: positive ints or 2-tuples.
    - ``dilation``: **only** ``(1, 1)`` (other values raise
      :class:`~iron.common.AIEOperatorConstraintError` at construct).
    - ``groups``: standard (1), grouped, and depthwise (``groups == C_in == C_out``).
    - ``use_bias``: on-device packed ``[W_tile‖B_tile]`` (≤2 input DMAs).
    - Spatial: any positive H×W that admits an L1 plan (full triple, pointwise
      H-strip, or k>1 host-pad RF H-strip).
    - Columns: 1…device max; OC-split (groups==1), channel-split (depthwise),
      or **group-block split** (non-depthwise ``groups>1`` when
      ``groups % cols == 0`` and the per-col IC/OC triple fits L1).
    - Batch ``N``: host loop over N=1-specialized MLIR.

    **Construct-time rejects** (``AIEOperatorConstraintError``)

    - Non-positive channels/spatial; dilation ≠ 1; groups not dividing C_in/C_out.
    - Non-positive output spatial from pad/stride/kernel.
    - L1 triple (in + weight[+bias] + out) cannot fit budget even with H-strip.
    - ``num_aie_columns < 1`` (request is then clamped by device/divisibility).

    **Not supported yet**

    - Dilation > 1; W-strip / joint OC×spatial BD-safe tiles; multi-col
      grouped **with** H-strip; fused activations; true ``aie::mmul`` layouts.
    """

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
            use_bias: Whether to use bias (default: True). Bias is packed into the
                weight DMA buffer (``[W_tile‖B_tile]``) and applied on-device.
            in_height: Input height (default 32)
            in_width: Input width (default 32)
            num_aie_columns: Requested AIE columns (OC/channel split;
                clamped when dimensions are not divisible)
            tile_size: Reserved tile-size hint (L1 OC/channel tiles chosen in design)
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

        if in_channels <= 0 or out_channels <= 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d requires positive in_channels/out_channels, "
                f"got in_channels={in_channels}, out_channels={out_channels}"
            )
        if in_height <= 0 or in_width <= 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d requires positive in_height/in_width, "
                f"got {in_height}x{in_width}"
            )
        if dilation != (1, 1):
            raise AIEOperatorConstraintError(
                f"AIEConv2d only supports dilation=(1, 1), got {dilation}"
            )
        if groups <= 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d requires groups >= 1, got {groups}"
            )
        if in_channels % groups != 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d in_channels ({in_channels}) must be divisible by "
                f"groups ({groups})"
            )
        if out_channels % groups != 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d out_channels ({out_channels}) must be divisible by "
                f"groups ({groups})"
            )

        self.out_height = (
            in_height + 2 * self.padding[0] - self.kernel_size[0]
        ) // self.stride[0] + 1
        self.out_width = (
            in_width + 2 * self.padding[1] - self.kernel_size[1]
        ) // self.stride[1] + 1
        if self.out_height <= 0 or self.out_width <= 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d produced non-positive output spatial size "
                f"{self.out_height}x{self.out_width} from "
                f"in={in_height}x{in_width}, kernel={self.kernel_size}, "
                f"stride={self.stride}, padding={self.padding}"
            )

        if tile_size is None:
            tile_size = 2048
        if num_aie_columns is None:
            num_aie_columns = 1
        if int(num_aie_columns) < 1:
            raise AIEOperatorConstraintError(
                f"AIEConv2d num_aie_columns must be >= 1, got {num_aie_columns}"
            )

        self.tile_size = tile_size
        self.num_aie_columns = int(num_aie_columns)
        self.requested_num_columns = self.num_aie_columns
        # Match design.py _resolve_num_columns. Device max_cols is applied in
        # set_up_artifacts (and re-validated for L1 after the final clamp).
        is_depthwise = groups == in_channels and groups == out_channels
        self.is_depthwise = is_depthwise
        # Construct-time: allow up to NPU2 max; set_up_artifacts tightens further.
        # Grouped multi-col may further drop columns when per-col L1 does not fit
        # (design then uses 1-col full/H-strip); keep host pack + design in sync.
        self.effective_num_columns = self._resolve_columns_for_l1(
            self.num_aie_columns, max_cols=8
        )
        self._validate_l1_fit(self.effective_num_columns)

        self.bias_size = out_channels if use_bias else 0

        # Flattened N=1 sizes (batch looped in forward); used by get_arg_spec / forward.
        self.input_size = in_channels * in_height * in_width
        self.weight_size = (
            out_channels
            * (in_channels // groups)
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        self.output_size = out_channels * self.out_height * self.out_width

        self.xclbin_artifact = None
        self.insts_artifact = None
        self.weight_buffer = None
        self.bias_buffer = None
        # Cached NPU callable (invalidated on compile).
        self._callable: Callable[..., Any] | None = None

        AIEOperatorBase.__init__(self, context=context)

    def _is_pointwise(self) -> bool:
        return (
            (not self.is_depthwise)
            and self.kernel_size[0] == 1
            and self.kernel_size[1] == 1
        )

    def _resolve_columns_for_l1(self, requested: int, max_cols: int) -> int:
        """Divisibility clamp, then drop columns until L1 policy accepts.

        For non-depthwise grouped multi-col, design requires the **per-col**
        IC/OC triple to fit (no multi-col H-strip yet). If it does not, fall
        back toward 1-col so full-tensor or 1-col H-strip can still succeed.
        """
        n = _resolve_num_columns(
            requested,
            self.out_channels,
            self.in_channels,
            self.groups,
            self.is_depthwise,
            max_cols=max_cols,
        )
        while n > 1:
            try:
                self._validate_l1_fit(n)
                return n
            except AIEOperatorConstraintError:
                n = _resolve_num_columns(
                    n - 1,
                    self.out_channels,
                    self.in_channels,
                    self.groups,
                    self.is_depthwise,
                    max_cols=max_cols,
                )
        return n

    def _halo_plan(self, num_columns: Optional[int] = None):
        """Return design ``_plan_halo_h_strip`` result when k>1 H-strip is active.

        None when full-input L1 fits, or config is not standard k>1,
        or no DMA-legal L1 plan exists (including optional bottom/right extra pad).
        Multi-col non-depthwise grouped uses group-block split (no H-strip).
        """
        # Depthwise uses channel tiles; pointwise has its own H-strip path.
        if self.is_depthwise or self._is_pointwise():
            return None
        n = 1
        cols = max(
            1,
            int(
                num_columns
                if num_columns is not None
                else self.effective_num_columns
            ),
        )
        # Grouped multi-col: design uses group-block split, not H-strip.
        if self.groups > 1 and cols > 1:
            return None
        if self.groups == 1:
            oc_per_col = self.out_channels // cols
        else:
            cols = 1
            oc_per_col = self.out_channels
        in_spatial = self.in_height * self.in_width
        out_spatial = self.out_height * self.out_width
        weight_per_oc = (
            (self.in_channels // self.groups)
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        weight_store_per_oc = weight_per_oc + _bias_per_oc(self.use_bias)
        input_size = n * self.in_channels * in_spatial
        budget = _L1_TRIPLE_BUDGET_BYTES
        if oc_per_col <= 0:
            return None
        if self.groups == 1:
            oc_tile = _choose_oc_tile(
                oc_per_col, input_size, weight_store_per_oc, out_spatial, budget
            )
            if _l1_triple_fits(
                input_size,
                oc_tile * weight_store_per_oc,
                n * oc_tile * out_spatial,
                budget,
            ):
                return None
        else:
            weight_size = self.out_channels * weight_store_per_oc
            output_size = n * self.out_channels * out_spatial
            if _l1_triple_fits(input_size, weight_size, output_size, budget):
                return None
        ph, pw = self.padding
        kh, kw = self.kernel_size
        sh, sw = self.stride
        return _plan_halo_h_strip(
            self.in_height,
            self.in_width,
            self.out_height,
            self.out_width,
            self.in_channels,
            oc_per_col,
            weight_store_per_oc,
            kh,
            kw,
            sh,
            sw,
            ph,
            pw,
            budget,
        )

    def _uses_halo_spatial_tiling(self, num_columns: Optional[int] = None) -> bool:
        """True when design enables k>1 host-pad H-strip (groups==1)."""
        return self._halo_plan(num_columns) is not None

    def _host_pad_input_nchw(
        self, x_nchw: torch.Tensor, plan: Optional[dict] = None
    ) -> torch.Tensor:
        """Zero-pad (C,H,W) for k>1 spatial design (conv pad + optional DMA pad).

        Conv padding is applied symmetrically; any DMA extra is **bottom/right**
        only so true top-left outputs match the unpadded formula.
        """
        ph, pw = self.padding
        extra_h = 0
        extra_w = 0
        if plan is not None:
            extra_h = int(plan.get("extra_h", 0))
            extra_w = int(plan.get("extra_w", 0))
        if ph == 0 and pw == 0 and extra_h == 0 and extra_w == 0:
            return x_nchw.contiguous()
        # F.pad pad order: (W_left, W_right, H_top, H_bottom)
        return torch.nn.functional.pad(
            x_nchw, (pw, pw + extra_w, ph, ph + extra_h)
        ).contiguous()

    def _pad_input_xrt(self, in_b: XRTTensor) -> XRTTensor:
        """Pad host/runtime input buffer when k>1 spatial L3 expects padded size."""
        plan = self._halo_plan()
        if plan is None:
            return in_b
        t = in_b.to_torch()
        if not isinstance(t, torch.Tensor):
            t = torch.tensor(t)
        t = t.detach().cpu().contiguous()
        if t.dtype != torch.bfloat16:
            t = t.to(torch.bfloat16)
        flat = t.reshape(-1)
        expect = self.in_channels * self.in_height * self.in_width
        padded_n = self.in_channels * plan["padded_h"] * plan["padded_w"]
        if flat.numel() == padded_n:
            return in_b
        if flat.numel() != expect:
            raise AIEOperatorConstraintError(
                f"AIEConv2d halo-spatial pad expected {expect} elems "
                f"(or already-padded {padded_n}), got {flat.numel()}"
            )
        x_nchw = flat.reshape(self.in_channels, self.in_height, self.in_width)
        x_pad = self._host_pad_input_nchw(x_nchw, plan).reshape(-1).contiguous()
        return XRTTensor.from_torch(x_pad)

    def _crop_npu_output_to_true(
        self, npu_out: XRTTensor, true_out: XRTTensor, plan: dict
    ) -> None:
        """Copy design-spatial NPU out into true OH×OW host out buffer."""
        design_oh = plan["design_oh"]
        design_ow = plan["design_ow"]
        true_oh = self.out_height
        true_ow = self.out_width
        t = npu_out.to_torch()
        if not isinstance(t, torch.Tensor):
            t = torch.tensor(t)
        t = t.detach().cpu().contiguous()
        if t.dtype != torch.bfloat16:
            t = t.to(torch.bfloat16)
        vol = t.reshape(self.out_channels, design_oh, design_ow)
        cropped = vol[:, :true_oh, :true_ow].contiguous().reshape(-1)
        if cropped.dtype == torch.bfloat16:
            np_c = cropped.view(torch.uint16).numpy().view(np.dtype("bfloat16"))
        else:
            np_c = cropped.numpy().astype(bfloat16, copy=False)
        true_out.data.reshape(-1)[:] = np_c
        if hasattr(true_out, "_sync_to_device"):
            true_out._sync_to_device()

    def _validate_l1_fit(self, num_columns: int) -> None:
        """Raise if the design's L1 triple (in+weight+out, bf16) cannot fit.

        Mirrors design.py tile selection: groups==1 OC-tiles with
        full input in L1, or H-strip spatial (pointwise or k>1 host-pad RF)
        when full input exceeds budget; depthwise channel-tiles; non-DW
        groups multi-col uses per-col IC/OC group blocks (must fit L1);
        1-col groups may use full triple or H-strip. Multi-column OC split
        does not reduce full-input L1 for groups==1 (input broadcast).
        """
        n = 1  # MLIR is specialized for N=1; batch is looped on host.
        in_spatial = self.in_height * self.in_width
        out_spatial = self.out_height * self.out_width
        weight_per_oc = (
            (self.in_channels // self.groups)
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        # L1 weight footprint includes packed bias (+1 per OC/channel) when used.
        weight_store_per_oc = weight_per_oc + _bias_per_oc(self.use_bias)
        input_size = n * self.in_channels * in_spatial
        budget = _L1_TRIPLE_BUDGET_BYTES
        bpe = _BYTES_PER_BF16
        cols = max(1, int(num_columns))
        is_pointwise = self._is_pointwise()

        if self.is_depthwise:
            c_per_col = self.in_channels // cols
            c_tile = _choose_channel_tile(
                c_per_col, in_spatial, out_spatial, weight_store_per_oc, budget
            )
            tile_elems = c_tile * (in_spatial + weight_store_per_oc + out_spatial)
            if tile_elems * bpe > budget:
                need = tile_elems * bpe
                raise AIEOperatorConstraintError(
                    f"AIEConv2d depthwise L1 footprint exceeds budget: "
                    f"min channel tile needs ~{need} bytes "
                    f"(budget {_L1_TRIPLE_BUDGET_BYTES} bytes for in+weight+out "
                    f"bf16 at depth=1). Config: C={self.in_channels}, "
                    f"spatial={self.in_height}x{self.in_width}→"
                    f"{self.out_height}x{self.out_width}, "
                    f"kernel={self.kernel_size}, cols={cols}. "
                    f"Reduce spatial size/channels or wait for spatial L1 tiling."
                )
            return

        if self.groups == 1:
            oc_per_col = self.out_channels // cols
            oc_tile = _choose_oc_tile(
                oc_per_col, input_size, weight_store_per_oc, out_spatial, budget
            )
            full_fits = _l1_triple_fits(
                input_size,
                oc_tile * weight_store_per_oc,
                n * oc_tile * out_spatial,
                budget,
            )
            if full_fits:
                return

            # Pointwise H-strip can still fit when full input does not.
            # Prefer full oc_per_col per strip (num_oc_tiles=1; no DMA stride-0).
            if is_pointwise:
                tile_h = _choose_h_tile_pointwise(
                    self.in_height,
                    self.in_channels,
                    self.in_width,
                    oc_per_col,
                    weight_store_per_oc,
                    budget,
                )
                in_tile = n * self.in_channels * tile_h * self.in_width
                out_tile_sp = tile_h * self.out_width
                if _l1_triple_fits(
                    in_tile,
                    oc_per_col * weight_store_per_oc,
                    n * oc_per_col * out_tile_sp,
                    budget,
                ):
                    return
                need = (
                    in_tile
                    + oc_per_col * weight_store_per_oc
                    + n * oc_per_col * out_tile_sp
                ) * bpe
                raise AIEOperatorConstraintError(
                    f"AIEConv2d pointwise L1 footprint exceeds budget even with "
                    f"H-strip spatial tiling (full OC/col): needs ~{need} bytes "
                    f"(budget {_L1_TRIPLE_BUDGET_BYTES}; tile_h={tile_h}). "
                    f"Config: IC={self.in_channels}, OC={self.out_channels}, "
                    f"spatial={self.in_height}x{self.in_width}, cols={cols}."
                )

            # k>1 host-pad RF H-strip with full oc_per_col (+ DMA pad).
            if self._halo_plan(cols) is not None:
                return

            ph, pw = self.padding
            padded_w = self.in_width + 2 * pw
            kh, sh = self.kernel_size[0], self.stride[0]
            tile_oh = _choose_h_tile_standard(
                self.out_height,
                self.in_channels,
                padded_w,
                oc_per_col,
                weight_store_per_oc,
                self.out_width,
                kh,
                sh,
                budget,
            )
            in_h_tile = _rf_in_h(max(1, tile_oh), sh, kh)
            in_tile = n * self.in_channels * in_h_tile * padded_w
            out_tile_sp = max(1, tile_oh) * self.out_width
            need = (
                in_tile
                + oc_per_col * weight_store_per_oc
                + n * oc_per_col * out_tile_sp
            ) * bpe
            input_bytes = input_size * bpe
            # Distinguish true L1 OOM from DMA-parity impossibility.
            out_strip = max(1, tile_oh) * self.out_width
            in_strip = in_h_tile * padded_w
            dma_ok = (out_strip % 2 == 0) and (in_strip % 2 == 0)
            dma_note = ""
            if need <= budget and not dma_ok:
                dma_note = (
                    f" Natural strip sizes are not DMA-aligned "
                    f"(out_strip={out_strip}, in_strip={in_strip} elems) and no "
                    f"bottom/right DMA extra-pad plan found within search bound."
                )
            raise AIEOperatorConstraintError(
                f"AIEConv2d L1 footprint exceeds budget even with k>1 "
                f"host-pad H-strip spatial tiling: needs ~{need} bytes "
                f"(budget {_L1_TRIPLE_BUDGET_BYTES} bytes; "
                f"full input alone is {input_bytes} bytes; "
                f"tile_oh={tile_oh}). "
                f"Config: IC={self.in_channels}, OC={self.out_channels}, "
                f"spatial={self.in_height}x{self.in_width}→"
                f"{self.out_height}x{self.out_width}, "
                f"kernel={self.kernel_size}, cols={cols}. "
                f"Note: multi-column OC split does not reduce input L1 "
                f"(input is broadcast per column).{dma_note}"
            )

        # Non-depthwise grouped: multi-col group-block (per-col IC/OC) or
        # 1-col full tensor / k>1 host-pad H-strip.
        if self.groups % cols != 0:
            raise AIEOperatorConstraintError(
                f"AIEConv2d grouped multi-col requires groups % cols == 0, "
                f"got groups={self.groups}, cols={cols}"
            )
        ic_per_col = self.in_channels // cols
        oc_per_col = self.out_channels // cols
        in_col = n * ic_per_col * in_spatial
        w_col = oc_per_col * weight_store_per_oc
        out_col = n * oc_per_col * out_spatial
        if _l1_triple_fits(in_col, w_col, out_col, budget):
            return
        if cols > 1:
            # Multi-col grouped has no H-strip path; caller may drop columns.
            need = (in_col + w_col + out_col) * bpe
            raise AIEOperatorConstraintError(
                f"AIEConv2d grouped multi-col (groups={self.groups}, cols={cols}) "
                f"per-col L1 triple needs ~{need} bytes "
                f"(budget {_L1_TRIPLE_BUDGET_BYTES}). "
                f"Config: IC={self.in_channels}, OC={self.out_channels}, "
                f"spatial={self.in_height}x{self.in_width}. "
                f"Try fewer columns or smaller spatial (1-col may H-strip)."
            )
        if self._halo_plan(1) is not None:
            return
        weight_size = self.out_channels * weight_store_per_oc
        output_size = n * self.out_channels * out_spatial
        triple = (input_size + weight_size + output_size) * bpe
        raise AIEOperatorConstraintError(
            f"AIEConv2d grouped (groups={self.groups}, non-depthwise) "
            f"requires full in+weight+out in L1 (~{triple} bytes) or a legal "
            f"k>1 H-strip plan, but budget is {_L1_TRIPLE_BUDGET_BYTES} bytes. "
            f"Config: IC={self.in_channels}, OC={self.out_channels}, "
            f"spatial={self.in_height}x{self.in_width}."
        )

    def set_up_artifacts(self):
        """Set up compilation artifacts (L1 tiles + multi-col split)."""
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

        # Column cap from target device model (NPU1.cols / NPU2.cols).
        max_cols = getattr(dev, "cols", None) or 4
        effective_num_columns = self._resolve_columns_for_l1(
            self.requested_num_columns, max_cols=max_cols
        )
        self.effective_num_columns = effective_num_columns
        # L1 re-check after device/group/L1 column clamp.
        self._validate_l1_fit(effective_num_columns)

        bias_tag = "bias" if self.use_bias else "nobias"
        file_name_base = (
            f"conv2d_{self.in_channels}_{self.out_channels}_{self.in_height}x{self.in_width}_"
            f"{self.kernel_size[0]}x{self.kernel_size[1]}_"
            f"s{self.stride[0]}x{self.stride[1]}_"
            f"p{self.padding[0]}x{self.padding[1]}_"
            f"g{self.groups}_{effective_num_columns}c_{bias_tag}"
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

    def compile(self, dry_run: bool = False):
        """Compile artifacts; invalidate cached NPU callable."""
        result = super().compile(dry_run=dry_run)
        self._callable = None
        return result

    def _get_op_callable(self) -> Callable[..., Any]:
        """Lazy get_callable after compile (maxpool-style cache)."""
        if self._callable is None:
            if not self.artifacts:
                self.compile()
            self._callable = self.get_callable()
        return self._callable

    def __call__(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        return self.forward(x, weight, bias)

    def forward(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: Optional[torch.Tensor] = None,
    ):
        """
        Forward pass for 2D convolution (torch API).

        Uses modern runtime: ``compile()`` + ``get_callable()`` + XRTTensor
        buffers. Bias is packed into the weight DMA buffer on-device
        (≤2 input DMAs). Batch N is looped in Python over N=1 MLIR.

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
        """Process a single sample (C, H, W) via NPU + optional host bias."""
        x_flat = x.reshape(-1).contiguous()
        if x_flat.dtype != torch.bfloat16:
            x_flat = x_flat.to(torch.bfloat16)

        weight_flat = weight.reshape(-1).contiguous()
        if weight_flat.dtype != torch.bfloat16:
            weight_flat = weight_flat.to(torch.bfloat16)

        if x_flat.numel() != self.input_size:
            raise AIEOperatorConstraintError(
                f"Flattened input size {x_flat.numel()} != configured {self.input_size}"
            )
        if weight_flat.numel() != self.weight_size:
            raise AIEOperatorConstraintError(
                f"Flattened weight size {weight_flat.numel()} != configured {self.weight_size}"
            )

        op_func = self._get_op_callable()
        in_b = XRTTensor.from_torch(x_flat)
        w_b = XRTTensor.from_torch(weight_flat)
        out_b = XRTTensor((self.output_size,), dtype=bfloat16)

        if self.use_bias and self.bias_size > 0:
            # get_callable expects 4 args when use_bias; zeros if bias omitted.
            if bias is None:
                bias_t = torch.zeros(self.bias_size, dtype=torch.bfloat16)
            else:
                bias_t = bias.contiguous()
                if bias_t.dtype != torch.bfloat16:
                    bias_t = bias_t.to(torch.bfloat16)
            bias_b = XRTTensor.from_torch(bias_t)
            op_func(in_b, w_b, bias_b, out_b)
        else:
            op_func(in_b, w_b, out_b)

        # Clone off XRT BO before buffers leave scope (batch>1 stack safety).
        result = out_b.to_torch()
        if not isinstance(result, torch.Tensor):
            result = torch.tensor(result)
        if result.dtype != torch.bfloat16:
            result = result.to(torch.bfloat16)
        result = result.detach().cpu().contiguous().clone()

        return result.reshape(self.out_channels, self.out_height, self.out_width)

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
        # Cache for callers that read these attributes.
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

    def _design_tile_channels(self) -> int:
        """OC/channel tile size matching design.py L1 selection (for bias pack)."""
        n = 1
        cols = max(1, int(self.effective_num_columns))
        in_spatial = self.in_height * self.in_width
        out_spatial = self.out_height * self.out_width
        weight_per_oc = (
            (self.in_channels // self.groups)
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        w_store = weight_per_oc + _bias_per_oc(self.use_bias)
        budget = _L1_TRIPLE_BUDGET_BYTES
        if self.is_depthwise:
            c_per_col = self.in_channels // cols
            c_tile = _choose_channel_tile(
                c_per_col, in_spatial, out_spatial, w_store, budget
            )
            if c_per_col % c_tile != 0:
                c_tile = c_per_col
            return c_tile
        if self.groups != 1:
            # Grouped multi-col: full OC block per column (num_tiles=1).
            # 1-col H-strip also uses full out_channels as the weight tile.
            return self.out_channels // cols
        oc_per_col = self.out_channels // cols
        input_size = n * self.in_channels * in_spatial
        oc_tile = _choose_oc_tile(oc_per_col, input_size, w_store, out_spatial, budget)
        if oc_per_col % oc_tile != 0:
            oc_tile = oc_per_col
        full_fits = _l1_triple_fits(
            input_size, oc_tile * w_store, n * oc_tile * out_spatial, budget
        )
        if full_fits:
            return oc_tile
        # H-strip paths prefer full oc_per_col (num_oc_tiles==1).
        if self._is_pointwise() or self._halo_plan(cols) is not None:
            return oc_per_col
        return oc_tile

    def _pack_weight_bias_xrt(self, w_buf, bias_buf) -> XRTTensor:
        """Build L3 packed ``[W_tile‖B_tile]…`` tensor for on-device bias."""
        w_t = w_buf.to_torch().reshape(-1).contiguous()
        b_t = bias_buf.to_torch().reshape(-1).contiguous()
        if w_t.dtype != torch.bfloat16:
            w_t = w_t.to(torch.bfloat16)
        if b_t.dtype != torch.bfloat16:
            b_t = b_t.to(torch.bfloat16)
        # pack_weights_with_bias is numpy-oriented; convert via uint16 view.
        w_np = w_t.detach().cpu().view(torch.uint16).numpy().view(np.dtype("bfloat16"))
        b_np = b_t.detach().cpu().view(torch.uint16).numpy().view(np.dtype("bfloat16"))
        packed = pack_weights_with_bias(
            w_np,
            b_np,
            out_channels=self.out_channels,
            in_channels=self.in_channels,
            groups=self.groups,
            kernel_h=self.kernel_size[0],
            kernel_w=self.kernel_size[1],
            num_columns=self.effective_num_columns,
            is_depthwise=self.is_depthwise,
            tile_channels=self._design_tile_channels(),
        )
        packed_u16 = packed.view(np.uint16)
        packed_t = torch.from_numpy(packed_u16.copy()).view(torch.bfloat16)
        return XRTTensor.from_torch(packed_t.contiguous())

    def get_callable(self):
        """Callable that packs bias into weights and runs NPU conv (≤2 DMAs)."""
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
            # k>1 spatial designs use host-padded L3 input (design input_ty).
            # External API / run_test still pass unpadded C*H*W; pad here.
            # When DMA pad grows design OH/OW, stage a larger NPU out and crop.
            plan = self._halo_plan()
            need_stage_out = False
            design_out_size = 0
            if plan is not None:
                design_out_size = (
                    self.out_channels * plan["design_oh"] * plan["design_ow"]
                )
                need_stage_out = design_out_size > (
                    self.out_channels * self.out_height * self.out_width
                )

            def _run_npu(in_buf, w_buf, out_buf):
                in_p = self._pad_input_xrt(in_buf)
                if need_stage_out:
                    npu_out = XRTTensor((design_out_size,), dtype=bfloat16)
                    result = aie_utils.DefaultNPURuntime.run(
                        handle, [in_p, w_buf, npu_out]
                    )
                    self._crop_npu_output_to_true(npu_out, out_buf, plan)
                    return result
                return aie_utils.DefaultNPURuntime.run(handle, [in_p, w_buf, out_buf])

            if use_bias:
                if len(args) != 4:
                    raise ValueError(
                        f"AIEConv2d with bias expects 4 args (in, weight, bias, out), got {len(args)}"
                    )
                in_b, w_b, bias_b, out_b = args
                packed_w = self._pack_weight_bias_xrt(w_b, bias_b)
                return _run_npu(in_b, packed_w, out_b)
            if len(args) < 3:
                raise ValueError(
                    f"AIEConv2d expects (in, weight, out), got {len(args)} args"
                )
            return _run_npu(args[0], args[1], args[2])

        return call
