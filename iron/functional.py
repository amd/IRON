# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Functions for a graph's body, under ``torch.nn.functional``'s names.

Each records the operator steps that compute it and returns their handle::

    import iron.functional as F

    h = F.rms_norm(x, w.input_layernorm.weight, eps)
    y = F.silu(F.linear(h, w.mlp.gate_proj.weight)) * F.linear(h, w.mlp.up_proj.weight)

Weights are a checkpoint's ``(out, in)``, as ``torch.nn.Linear`` stores them.
A handle's own ``+ - * /`` and ``@`` are steps too (``Handle``).
"""

import math

from iron.common import Precision
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.operators.silu import SiLU

# The epsilon mlir-aie's layer_norm kernel fixes.
LAYER_NORM_EPS = 1e-5


def linear(x, weight, bias=None, *, precision=None, **gemv):
    """``x @ weight.T``, plus ``bias`` on every row if given.

    One row is a GEMV, whose float32 sum rounds once, as every
    ``precision`` (``Precision``) allows. More are flm.GEMM reading
    ``weight`` column-major at ``precision``, or at ``HIGHEST`` the GEMM
    whose float32 sums round once, which tiles row counts flm.GEMM does
    not. ``gemv`` is the GEMV's tunables, for a call the profile cannot
    tell from another of its shape.

    Raises:
        ValueError: GEMV tunables for more than one row.
    """
    if len(x.shape) != 2 or x.shape[0] == 1:
        y = GEMV.step(weight, x, **gemv)
    elif gemv:
        raise ValueError(f"linear(): {x.shape[0]} rows take no GEMV {sorted(gemv)}")
    elif precision == Precision.HIGHEST:
        y = GEMM.step(x, weight, b_col_maj=True, precision=precision)
    else:
        tiled = {} if precision is None else dict(precision=precision)
        y = FLMGEMM.step(
            x, weight, b_col_maj=True, epilogue_modes=(Epilogue.NONE,), **tiled
        )
    if bias is None:
        return y
    # A row added to every row, also for GEMV's one-dimensional output.
    rows = math.prod(y.shape) // bias.shape[0]
    return (y.reshape(rows, bias.shape[0]) + bias).reshape(y.shape)


def rms_norm(x, weight=None, eps: float = 1e-6):
    """``x`` over the RMS of its last axis, times ``weight`` if given."""
    if weight is None:
        return RMSNorm.step(x, epsilon=eps)
    return RMSNorm.step(x, weight=weight, epsilon=eps)


def layer_norm(x, weight, bias, eps: float = LAYER_NORM_EPS):
    """``x`` less its mean over the RMS of that, times ``weight``, plus ``bias``.

    Raises:
        ValueError: ``eps`` is not the kernel's own, ``LAYER_NORM_EPS``.
    """
    if eps != LAYER_NORM_EPS:
        raise ValueError(
            f"layer_norm(): the kernel takes no epsilon but {LAYER_NORM_EPS}, not {eps}"
        )
    return LayerNorm.step(x) * weight + bias


def silu(x):
    return SiLU.step(x)


def gelu(x, approximate: str = "none"):
    """GELU by its tanh approximation (``gelu_pytorch_tanh``).

    Raises:
        ValueError: ``approximate`` is not ``"tanh"``: no operator computes
            the exact GELU.
    """
    if approximate != "tanh":
        raise ValueError(
            f"gelu(): only approximate='tanh' has an operator, not {approximate!r}"
        )
    return GELU.step(x)


def rope(x, angles):
    """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per row."""
    return RoPE.step(x, angles)
