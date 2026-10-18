# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library, re-exported lazily (PEP 562).

flm's operators are named here with a dotted key (``"flm.ProjectionGEMM"``), so a
profile names either catalog's the same way.
"""

import importlib

#: ``flm``'s operators, by their own bare name, relative to ``iron.operators.flm``.
_FLM_OPERATOR_MODULES = {
    "ProjectionGEMM": "gemm.op",
    "DequantBFP": "dequant.op",
    "DecodeLayer": "layer.op",
    "PrefillAttention": "prefill_attn.op",
    "PrefillSlidingAttention": "prefill_attn.op",
    "LMHead": "lm_head.op",
}

# Operator name -> its module, relative to this package; flm's dotted.
_OPERATOR_MODULES = {
    "AXPY": "axpy",
    "Clamp": "clamp",
    "Copy": "copy",
    "DepthwiseConv1d": "depthwise_conv1d",
    "ElementwiseAdd": "elementwise_add",
    "ElementwiseMax": "elementwise_max",
    "ElementwiseMul": "elementwise_mul",
    "Emit": "emit",
    "Experts": "experts",
    "Gather": "copy",
    "GatherWords": "copy",
    "GELU": "gelu",
    "GEMM": "gemm",
    "GEMV": "gemv",
    "LayerNorm": "layer_norm",
    "Limbs": "limbs",
    "Log": "log",
    "Magnitude": "magnitude",
    "Merge": "merge",
    "MHA": "mha",
    "PatchPositions": "resample.op",
    "ReLU": "relu",
    "Resample": "resample.op",
    "ResampleTaps": "resample.op",
    "RMSNorm": "rms_norm",
    "RoPE": "rope",
    "RowwiseAdd": "elementwise_add",
    "RowwiseMul": "elementwise_mul",
    "Sample": "sample",
    "Sigmoid": "sigmoid",
    "SiLU": "silu",
    "Softmax": "softmax",
    "Tanh": "tanh",
    "TopKRouter": "router",
    "Transpose": "transpose",
    **{
        f"flm.{name}": f"flm.{module}" for name, module in _FLM_OPERATOR_MODULES.items()
    },
}

__all__ = sorted(_OPERATOR_MODULES)


def __getattr__(name):
    """Import the operator that defines `name`: a bare or a dotted catalog key."""
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    attr = name.rpartition(".")[2]
    return getattr(importlib.import_module(f".{module}", __name__), attr)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))


def catalog_name(cls: type) -> str:
    """The catalog key ``cls`` is exported under, importing nothing more.

    Raises:
        ValueError: no catalog entry's module and bare name both match ``cls``.
    """
    for key, module in _OPERATOR_MODULES.items():
        if (
            key.rpartition(".")[2] == cls.__name__
            and f"{__name__}.{module}" == cls.__module__
        ):
            return key
    raise ValueError(
        f"{cls.__module__}.{cls.__name__} is not in iron.operators's catalog"
    )
