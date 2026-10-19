# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Functions for a graph's body, under ``torch.nn.functional``'s names.

Each records the operator steps that compute it and returns their handle::

    import iron.functional as F

    h = F.rms_norm(x, x.shape[-1:], w.input_layernorm.weight, eps)
    y = F.silu(F.linear(h, w.mlp.gate_proj.weight)) * F.linear(h, w.mlp.up_proj.weight)

Weights are a checkpoint's ``(out, in)``, as ``torch.nn.Linear`` stores them.
A handle's own ``+ - * /`` and ``@`` are steps too (``Handle``).

A feature map is one image, channels last: ``(H, W, C)``, not torch's
``(N, C, H, W)``. Its rows, ``(H, W * C)``, are what its steps read.
"""

import dataclasses
import math
from collections.abc import Sequence

import ml_dtypes
import numpy as np
from aie.helpers.taplib import TensorAccessPattern

import iron
from iron.common import Precision
from iron.common.feature_map import ConcatChannels, Conv2d, MaxPool2d
from iron.common.graph.handle import Handle, State
from iron.common.image.packaging import require_device
from iron.operators.copy import Copy
from iron.operators.flm.gemm.design import M_TILE, Epilogue, compute_rows
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU

# mlir-aie's layer_norm kernel always uses this epsilon.
LAYER_NORM_EPS = 1e-5


def linear(x: Handle | State, weight, bias=None, *, precision=None, **gemv) -> Handle:
    """Return ``x @ weight.T``, plus ``bias`` on every row if ``bias`` is given.

    ``x`` is one row, ``(in,)`` or ``(1, in)``, or several rows,
    ``(rows, in)``. ``weight`` is ``(out, in)``, as ``torch.nn.Linear``
    stores it.

    One row runs on GEMV, which sums in float32 and rounds once, so
    ``precision`` has no effect on it. Several rows run on
    flm.ProjectionGEMM at the given ``precision``. At
    ``Precision.HIGHEST`` (asked for here, or set on the graph) they run on
    GEMM instead, which also sums in float32 and handles row counts
    flm.ProjectionGEMM cannot tile. Nothing is padded: a row count neither
    operator tiles raises when the graph is recorded.

    ``gemv`` passes tunables to the GEMV, for a call the profile cannot
    tell apart from another call of the same shape.

    Raises:
        ValueError: ``x`` of another rank, or GEMV tunables for several rows.
    """
    one_row = len(x.shape) == 1 or (len(x.shape) == 2 and x.shape[0] == 1)
    if len(x.shape) not in (1, 2):
        raise ValueError(f"linear(): x {tuple(x.shape)} is not (in,) or (rows, in)")
    if one_row:
        y = GEMV.step(weight, x, **gemv)
    elif gemv:
        raise ValueError(f"linear(): {x.shape[0]} rows take no GEMV {sorted(gemv)}")
    elif precision == Precision.HIGHEST:
        y = GEMM.step(x, weight, b_col_maj=True, precision=Precision.HIGHEST)
    else:
        tiled = {} if precision is None else dict(precision=precision)
        y = ProjectionGEMM.step(
            x, weight, b_col_maj=True, epilogue_modes=(Epilogue.NONE,), **tiled
        )
    if bias is None:
        return y
    # A row added to every row, also for GEMV's one-dimensional output.
    rows = math.prod(y.shape) // bias.shape[0]
    return (y.reshape(rows, bias.shape[0]) + bias).reshape(y.shape)


def _last_axis(name: str, x: Handle, normalized_shape) -> None:
    """Refuse a ``normalized_shape`` other than ``x``'s last axis."""
    given = (
        (normalized_shape,)
        if isinstance(normalized_shape, int)
        else tuple(normalized_shape)
    )
    if given != tuple(x.shape[-1:]):
        raise ValueError(
            f"{name}(): normalized_shape {list(given)} is not the last axis of "
            f"input {list(x.shape)}; only ({x.shape[-1]},) is normalized"
        )


def rms_norm(
    x: Handle, normalized_shape, weight=None, eps: float | None = None
) -> Handle:
    """``x`` over the RMS of its last axis, times ``weight`` if given.
    ``eps`` None is ``x``'s dtype's machine epsilon, as torch's.

    Raises:
        ValueError: ``normalized_shape`` is not ``x``'s last axis.
    """
    _last_axis("rms_norm", x, normalized_shape)
    if eps is None:
        eps = float(ml_dtypes.finfo(x.dtype).eps)
    return RMSNorm.step(x, weight=weight, epsilon=eps)


def layer_norm(
    x: Handle, normalized_shape, weight=None, bias=None, eps: float = LAYER_NORM_EPS
) -> Handle:
    """``x`` less its mean over the RMS of that, times ``weight`` and plus
    ``bias`` where given.

    Raises:
        ValueError: ``normalized_shape`` is not ``x``'s last axis, or
            ``eps`` is not the kernel's own, ``LAYER_NORM_EPS``.
    """
    _last_axis("layer_norm", x, normalized_shape)
    if eps != LAYER_NORM_EPS:
        raise ValueError(
            f"layer_norm(): the kernel takes no epsilon but {LAYER_NORM_EPS}, not {eps}"
        )
    y = LayerNorm.step(x, weight=weight)
    return y if bias is None else y + bias


def silu(x: Handle) -> Handle:
    return SiLU.step(x)


def gelu(x: Handle, approximate: str = "none") -> Handle:
    """GELU by its tanh approximation (``gelu_pytorch_tanh``). The default
    is torch's, the exact GELU, so a call written for it is refused rather
    than approximated.

    Raises:
        ValueError: ``approximate`` is not ``"tanh"``: no operator computes
            the exact GELU.
    """
    if approximate != "tanh":
        raise ValueError(
            f"gelu(): only approximate='tanh' has an operator, not {approximate!r}"
        )
    return GELU.step(x)


def rope(x: Handle, angles: Handle) -> Handle:
    """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per row."""
    return RoPE.step(x, angles)


@dataclasses.dataclass(frozen=True)
class ConvState:
    """What a short causal conv carries between calls: ``read``, the
    ``K - 1`` rows before a call's first, and ``write``, where the ``K - 1``
    ending it go; and the scratch states a call stages them in, ``window``
    ``(2, chunk, channels)`` and ``tail`` ``(K - 1, channels)``.
    """

    read: Handle
    write: Handle
    window: State
    tail: State


def causal_conv1d(x: Handle, taps, state: ConvState) -> Handle:
    """Run ``x`` ``(rows, channels)`` through a depth-wise causal filter of
    ``K`` taps.

    Output row ``t`` is ``sum_k taps[k] * x[t - K + 1 + k]``, and each
    channel uses its own column of ``taps`` ``(K, channels)``. The ``K - 1``
    rows before ``x``'s first row are read from ``state.read``, and the
    ``K - 1`` rows that end this call's input (counting the rows read) are
    written to ``state.write`` for the next call. When ``x``'s rows are
    bounded per call (``x[:n]``), the call is a prompt chunk of at most
    ``chunk`` rows; otherwise ``x`` is one row, a decode step.
    """
    read, write, window, tail = state.read, state.write, state.window, state.tail
    K, C = taps.shape[0], window.shape[1]
    # Block 0 ends with the rows before the call; block 1 is the call's.
    flat = window.reshape(2 * C, x.shape[1])
    first = C - (K - 1)
    flat[first:C] = read
    rows = x.valid.get(0)
    if rows is None:
        flat[C] = x.reshape(x.shape[1])
        y = x * taps[K - 1]
        for k in range(K - 1):
            y = y + flat[first + k : first + k + 1] * taps[k]
        Copy.step(flat[first + 1 : C + 1], write)
        return y
    window[1, :rows] = x
    y = flat[first : first + C] * taps[0]
    for k in range(1, K):
        y = y + flat[first + k : first + k + C] * taps[k]
    y = y[:rows]
    for j in range(K - 1):
        tail[j] = flat[first + rows + j]
    Copy.step(tail, write)
    return y


def _feature_map(name: str, x: Handle) -> tuple[int, int, int]:
    """``x``'s ``(H, W, C)``.

    Raises:
        ValueError: ``x`` is not of three axes.
    """
    if len(x.shape) != 3:
        raise ValueError(f"{name}(): x {tuple(x.shape)} is not a map (H, W, C)")
    return x.shape


def conv2d(
    x: Handle, weight, bias=None, stride=1, padding=0, dilation=1, groups=1
) -> Handle:
    """The feature map ``x`` convolved by ``weight`` ``(out, C / groups,
    k, k)`` at ``stride``, inside ``padding`` zero pixels a side, plus
    ``bias`` per output channel if given.

    A 1x1 at stride 1 is ``linear`` of the pixels at ``Precision.HIGH``,
    copied first into a held map of whole flm.ProjectionGEMM row blocks
    if they are not, the rows past them computed and dropped. Any other is
    ``Conv2d``, its input copied into a held zero border. ``groups`` is
    ``1`` or depthwise, as ``Conv2d`` builds.

    Raises:
        ValueError: ``x`` is not a map, its channels are not the weight's
            times ``groups``, the kernel is not square, or ``dilation`` is
            not 1.
    """
    H, W, C = _feature_map("conv2d", x)
    out, per_group, k, kw = weight.shape
    if C != per_group * groups:
        raise ValueError(
            f"conv2d(): x has {C} channels, the weight reads {per_group} "
            f"times {groups} groups"
        )
    if k != kw or dilation != 1:
        raise ValueError(
            f"conv2d(): only a square kernel at dilation 1 has an operator, not "
            f"{k}x{kw} at dilation {dilation}"
        )
    if k == 1 and stride == 1 and groups == 1 and not padding:
        n = H * W
        pixels = x.reshape(n, C)
        unit = M_TILE * compute_rows(require_device())
        if n % unit:
            held = iron.state((-(-n // unit) * unit, C))
            held[:n] = pixels
            pixels = held
        y = linear(
            pixels,
            weight[:, :, 0, 0].astype(ml_dtypes.bfloat16),
            bias,
            precision=Precision.HIGH,
        )
        return y[:n].reshape(H, W, out)
    rows = x.reshape(H, W * C)
    # One channel a group pads its width in the band; patches read it held.
    banded = per_group == 1
    if banded:
        conv = Conv2d(weight, W, stride, padding=padding, groups=groups)
    else:
        conv = Conv2d(weight, W + 2 * padding, stride, groups=groups)
    if padding:
        line = (W if banded else W + 2 * padding) * C
        shape = (H + 2 * padding, line)
        held = iron.state(shape)
        Copy.step(np.zeros(shape, ml_dtypes.bfloat16), held)
        offset = padding * line + (0 if banded else padding * C)
        interior = TensorAccessPattern(shape, offset, [H, W * C], [line, 1])
        Copy.step(rows, held, dst=interior)
        rows = held
    out_rows = (H + 2 * padding - k) // stride + 1
    y = conv(rows, rows=out_rows).reshape(out_rows * conv.out_width, out)
    if bias is not None:
        y = y + bias
    return y.reshape(out_rows, conv.out_width, out)


def max_pool2d(x: Handle, kernel_size, stride=None, padding=0) -> Handle:
    """The feature map ``x``'s max over each ``kernel_size`` square window
    at ``stride`` (``kernel_size`` where None), each channel its own:
    ``MaxPool2d``, which pools at stride 1 inside ``-inf`` padding of half
    the window, then every ``stride``-th pixel of every ``stride``-th row.

    Raises:
        ValueError: ``x`` is not a map, or another ``padding``.
    """
    H, W, C = _feature_map("max_pool2d", x)
    stride = kernel_size if stride is None else stride
    if padding != kernel_size // 2:
        raise ValueError(
            f"max_pool2d(): only padding={kernel_size // 2} has an operator, "
            f"not padding={padding}"
        )
    y = MaxPool2d(H, W, C, kernel_size)(x.reshape(H, W * C))
    if stride == 1:
        return y.reshape(H, W, C)
    rows, width = (H - 1) // stride + 1, (W - 1) // stride + 1
    strided = TensorAccessPattern(
        (H, W * C), 0, [rows, width, C], [stride * W * C, stride * C, 1]
    )
    return Copy.step(y, src=strided).reshape(rows, width, C)


def interpolate(
    x: Handle, size=None, scale_factor=None, mode="nearest", align_corners=None
) -> Handle:
    """The feature map ``x`` upsampled 2x, each pixel a 2x2 block: each row
    read twice into a held map, which is then written twice, into the even
    and the odd pixels of another.

    Raises:
        ValueError: ``x`` is not a map, or the result is not its exact 2x
            nearest upsampling.
    """
    H, W, C = _feature_map("interpolate", x)

    def pair(v):
        return tuple(v) if isinstance(v, (tuple, list)) else (v, v)

    if (size is None) == (scale_factor is None):
        doubles = False
    elif size is not None:
        doubles = pair(size) == (2 * H, 2 * W)
    else:
        doubles = pair(scale_factor) == (2, 2)
    if not doubles or mode != "nearest" or align_corners is not None:
        raise ValueError(
            f"interpolate(): only the exact 2x nearest upsampling has an operator, "
            f"not size={size}, scale_factor={scale_factor}, mode={mode!r}, "
            f"align_corners={align_corners}"
        )
    doubled, out = iron.state((2 * H, W * C)), iron.state((2 * H, 2 * W * C))
    twice = TensorAccessPattern((H, W * C), 0, [H, 2, W * C], [W * C, 0, 1])
    Copy.step(x.reshape(H, W * C), doubled, src=twice)
    for column in (0, C):
        dst = TensorAccessPattern(
            out.shape, column, [2 * H, W, C], [2 * W * C, 2 * C, 1]
        )
        Copy.step(doubled[:], out, dst=dst)
    return Copy.step(out[:]).reshape(2 * H, 2 * W, C)


def cat(tensors: Sequence[Handle], dim=0) -> Handle:
    """Two to four feature maps of one height and width joined along their
    channels, ``dim`` -1: ``ConcatChannels``.

    Raises:
        ValueError: A tensor is not a map, or ``dim`` is not the channels'.
    """
    maps = [_feature_map("cat", t) for t in tensors]
    if dim not in (-1, 2):
        raise ValueError(f"cat(): only the channels, dim -1, are joined, not {dim}")
    H, W, _ = maps[0]
    channels = tuple(c for _, _, c in maps)
    y = ConcatChannels(H, W, channels)(
        *(t.reshape(H, W * c) for t, c in zip(tensors, channels))
    )
    return y.reshape(H, W, sum(channels))
