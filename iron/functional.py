# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Functions for a graph's body, under ``torch.nn.functional``'s names.

Each records the operator steps that compute it and returns their handle.
Weights are a checkpoint's ``(out, in)``, as ``torch.nn.Linear`` stores
them. A handle's own ``+ - * /`` are steps too, and ``@`` of one row.
"""

import dataclasses
import math

import ml_dtypes

from iron.common import Precision
from iron.common.graph.handle import Handle, State
from iron.operators.copy import Copy
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU


def linear(
    x: Handle | State, weight, bias=None, *, precision: Precision, **gemv
) -> Handle:
    """Return ``x @ weight.T``, plus ``bias`` on every row if given.

    ``weight`` is ``(out, in)``, as ``torch.nn.Linear`` stores it. One row
    runs on GEMV, which always rounds once in float32 regardless of
    ``precision``; several rows run on flm.ProjectionGEMM at ``precision``,
    or on GEMM at ``Precision.HIGHEST``.

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
        y = ProjectionGEMM.step(
            x,
            weight,
            b_col_maj=True,
            bfp16_b=False,
            epilogue_modes=(Epilogue.NONE,),
            precision=precision,
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
    x: Handle, normalized_shape, weight=None, bias=None, eps: float = 1e-5
) -> Handle:
    """Layer-normalize ``x`` over its last axis, as torch's ``layer_norm``.

    Subtract the mean, divide by the standard deviation (``eps`` under the
    root), then multiply by ``weight`` and add ``bias`` when given.

    Raises:
        ValueError: ``normalized_shape`` is not ``x``'s last axis.
    """
    _last_axis("layer_norm", x, normalized_shape)
    y = LayerNorm.step(x, weight=weight, epsilon=eps)
    return y if bias is None else y + bias


def silu(x: Handle) -> Handle:
    return SiLU.step(x)


def gelu(x: Handle, approximate: str = "none") -> Handle:
    """Apply GELU, exact by default as torch's.

    Or by its tanh approximation (``approximate="tanh"``,
    ``gelu_pytorch_tanh``).
    """
    return GELU.step(x, approximate=approximate)


def rope(x: Handle, angles: Handle) -> Handle:
    """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per row."""
    return RoPE.step(x, angles)


@dataclasses.dataclass(frozen=True)
class ConvState:
    """What a short causal conv carries between calls.

    ``read``, the ``K - 1`` rows before a call's first, and ``write``, where
    the ``K - 1`` ending it go; and the scratch states a call stages them
    in, ``window`` ``(2, chunk, channels)`` and ``tail`` ``(K - 1, channels)``.
    """

    read: Handle
    write: Handle
    window: State
    tail: State


def causal_conv1d(x: Handle, taps, state: ConvState) -> Handle:
    """Return ``x`` ``(rows, channels)`` through a depth-wise causal filter of ``K`` taps.

    Each channel its own column of ``taps`` ``(K, channels)``: output row
    ``t`` is ``sum_k taps[k] * x[t - K + 1 + k]``. The ``K - 1``
    rows before ``x``'s first row are read from ``state.read``, and the
    ``K - 1`` rows ending this call (counting those read) are written to
    ``state.write`` for the next call. When ``x``'s rows are bounded per
    call (``x[:n]``), the call is a prompt chunk of at most ``chunk`` rows;
    otherwise ``x`` is one row, a decode step.
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
