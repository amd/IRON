# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Functions for a graph's body, under ``torch.nn.functional``'s names.

Each records the operator steps that compute it and returns their handle::

    import iron.functional as F

    h = F.rms_norm(x, x.shape[-1:], w.input_layernorm.weight, eps)
    y = F.silu(F.linear(h, w.mlp.gate_proj.weight)) * F.linear(h, w.mlp.up_proj.weight)

Weights are a checkpoint's ``(out, in)``, as ``torch.nn.Linear`` stores them.
A handle's own ``+ - * /`` and ``@`` are steps too (``Handle``).
"""

import math

import ml_dtypes

from iron.common import Precision
from iron.common.declare.operator import graph_tracer
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.op import ProjectionGEMM
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

    One row is a GEMV, its float32 sum rounded once, which every
    ``precision`` (``Precision``) allows. More rows are flm.ProjectionGEMM
    reading ``weight`` column-major at ``precision``; ``HIGHEST``, asked for
    here or by the graph's ``precision``, is instead the GEMM whose float32
    sums round once, which also tiles row counts flm.ProjectionGEMM cannot.
    Nothing is padded: a row count neither tiles is an error at trace time.
    ``gemv`` is the GEMV's tunables, for a call the profile cannot tell from
    another of its shape.

    Raises:
        ValueError: GEMV tunables for more than one row.
    """
    if len(x.shape) != 2 or x.shape[0] == 1:
        y = GEMV.step(weight, x, **gemv)
    elif gemv:
        raise ValueError(f"linear(): {x.shape[0]} rows take no GEMV {sorted(gemv)}")
    elif Precision.HIGHEST in (
        precision,
        getattr(graph_tracer.get(), "precision", None),
    ):
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


def _last_axis(name: str, x, normalized_shape) -> None:
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


def rms_norm(x, normalized_shape, weight=None, eps: float | None = None):
    """``x`` over the RMS of its last axis, times ``weight`` if given.
    ``eps`` None is ``x``'s dtype's machine epsilon, as torch's.

    Raises:
        ValueError: ``normalized_shape`` is not ``x``'s last axis.
    """
    _last_axis("rms_norm", x, normalized_shape)
    if eps is None:
        eps = float(ml_dtypes.finfo(x.dtype).eps)
    if weight is None:
        return RMSNorm.step(x, epsilon=eps)
    return RMSNorm.step(x, weight=weight, epsilon=eps)


def layer_norm(
    x, normalized_shape, weight=None, bias=None, eps: float = LAYER_NORM_EPS
):
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
    y = LayerNorm.step(x)
    if weight is not None:
        y = y * weight
    return y if bias is None else y + bias


def silu(x):
    return SiLU.step(x)


def gelu(x, approximate: str = "none"):
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


def rope(x, angles):
    """``x`` ``(rows, head_dim)`` turned by RoPE, a row of ``angles`` per row."""
    return RoPE.step(x, angles)
