# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Functions for a graph's body, under ``torch.nn.functional``'s names.

Each records the operator steps that compute it and returns their handle::

    import iron.functional as F

    h = F.rms_norm(x, x.shape[-1:], w.input_layernorm.weight, eps)
    gate = F.linear(h, w.mlp.gate_proj.weight, precision=Precision.HIGH)
    y = F.silu(gate) * F.linear(h, w.mlp.up_proj.weight, precision=Precision.HIGH)

Weights are a checkpoint's ``(out, in)``, as ``torch.nn.Linear`` stores them.
A handle's own ``+ - * /`` are steps too, and ``@`` of one row (``Handle``).
"""

import math

import ml_dtypes

import iron
from iron.common import Precision
from iron.common.graph.handle import Handle, State
from iron.common.image.packaging import require_device
from iron.operators.flm.gemm.design import M_TILE, Epilogue, compute_rows
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
    """Return ``x @ weight.T``, plus ``bias`` on every row if ``bias`` is given.

    ``x`` is one row, ``(in,)`` or ``(1, in)``, or several rows,
    ``(rows, in)``. ``weight`` is ``(out, in)``, as ``torch.nn.Linear``
    stores it.

    ``precision`` is the caller's choice; there is no default. One row runs
    on GEMV, which sums in float32 and rounds once, as ``Precision.HIGHEST``
    does, whatever ``precision`` says. Several rows run on
    flm.ProjectionGEMM at ``precision``. At
    ``Precision.HIGHEST`` they run on GEMM instead, which also sums in
    float32 and handles row counts flm.ProjectionGEMM cannot tile. Nothing
    is padded: a row count neither operator tiles raises when the graph is
    recorded.

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
        y = ProjectionGEMM.step(
            x,
            weight,
            b_col_maj=True,
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

    Subtracts the mean, divides by the standard deviation (``eps`` under
    the root), then multiplies by ``weight`` and adds ``bias`` when they are
    given.

    Raises:
        ValueError: ``normalized_shape`` is not ``x``'s last axis.
    """
    _last_axis("layer_norm", x, normalized_shape)
    y = LayerNorm.step(x, weight=weight, epsilon=eps)
    return y if bias is None else y + bias


def silu(x: Handle) -> Handle:
    return SiLU.step(x)


def gelu(x: Handle, approximate: str = "none") -> Handle:
    """GELU, exact by default as torch's, or by its tanh approximation
    (``approximate="tanh"``, ``gelu_pytorch_tanh``).
    """
    return GELU.step(x, approximate=approximate)


def rope(x: Handle, angles: Handle) -> Handle:
    """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per row."""
    return RoPE.step(x, angles)
