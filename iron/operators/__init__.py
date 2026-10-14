# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The IRON operator library.

Operators are re-exported lazily (PEP 562):

    from iron.operators import GEMM  # imports iron.operators.gemm, nothing else

The FastFlowLM ports, and the binary they are measured against, are
``iron.operators.flm``'s own package (``from iron.operators.flm import
GEMM, Shipped``; its GEMM is not this one), named here with a dotted key
(``"flm.GEMM"``) so a profile can name either catalog's operator the same
way (``Profile.load``). Static names for both are in this package's and
``flm``'s ``.pyi`` stubs, not here: the runtime loads lazily.
"""

import importlib

#: ``flm``'s operators, by their own bare name, relative to ``iron.operators.flm``.
_FLM_OPERATOR_MODULES = {
    # The port, built from source for the current device.
    "GEMM": "gemm.op",
    # q4nx weights to the bfp16 B that GEMM reads, without a host-side pack.
    "DequantBFP": "dequant.op",
    # Gemma 4's fused decode layer, as FastFlowLM's engine drives it.
    "DecodeLayer": "layer.op",
    # Causal prefill attention, one build for every token range.
    "PrefillAttention": "prefill_attn.op",
    # Sliding-window causal prefill attention, one build for every token range.
    "PrefillSlidingAttention": "prefill_attn.op",
    # Softcapped logits straight from the q4nx vocabulary.
    "LMHead": "lm_head.op",
    # The shipped binary itself, downloaded and pinned, as a second form of
    # GEMM: Shipped(...). NPU2 only; exists so the port can be measured
    # against what it was ported from.
    "Shipped": "gemm.shipped",
}

# Operator name -> the module that defines it, relative to this package: one
# file (``relu``), or ``<directory>.op`` for one that keeps a design, a
# reference or a test of its own beside it. ``flm``'s operators are here too,
# dotted (``"flm.GEMM"``), so one catalog answers for both: a profile names
# either, and the lazy_imports/declared tests walk both without a second table.
_OPERATOR_MODULES = {
    "AXPY": "axpy",
    "Clamp": "clamp",
    "DepthwiseConv1d": "depthwise_conv1d",
    "Dequant": "dequant",
    "ElementwiseAdd": "elementwise_add",
    "ElementwiseMax": "elementwise_max",
    "ElementwiseMul": "elementwise_mul",
    "Emit": "emit",
    "GELU": "gelu",
    "GEMM": "gemm",
    "GEMV": "gemv",
    "LayerNorm": "layer_norm",
    "LeakyReLU": "leaky_relu",
    "Limbs": "limbs",
    "Log": "log",
    "Magnitude": "magnitude",
    "Merge": "merge",
    "MHA": "mha",
    "PatchPositions": "resample.op",
    "ReLU": "relu",
    "RMSNorm": "rms_norm",
    "Repeat": "repeat",
    "Resample": "resample.op",
    "ResampleTaps": "resample.op",
    "RoPE": "rope",
    "RowwiseAdd": "elementwise_add",
    "RowwiseMul": "elementwise_mul",
    "Sample": "sample",
    "Sigmoid": "sigmoid",
    "SiLU": "silu",
    "Softmax": "softmax",
    "Copy": "copy",
    "Tanh": "tanh",
    "Transpose": "transpose",
    **{
        f"flm.{name}": f"flm.{module}" for name, module in _FLM_OPERATOR_MODULES.items()
    },
}

__all__ = sorted(_OPERATOR_MODULES)


def __getattr__(name):
    """Import the operator that defines `name`, on first access.

    `name` is a bare name (``"GEMM"``) for normal attribute access, or a
    dotted catalog key (``"flm.GEMM"``, which Python's `getattr` passes
    through whole: it is one string, not two attribute lookups) for a
    caller that has the name from `_OPERATOR_MODULES` itself, as
    `iron.common.declare.Profile` does.
    """
    module = _OPERATOR_MODULES.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    attr = name.rpartition(".")[2]
    return getattr(importlib.import_module(f".{module}", __name__), attr)


def __dir__():
    return sorted(set(globals()) | set(_OPERATOR_MODULES))


def catalog_name(cls: type) -> str:
    """The catalog key ``cls`` is exported under (``"GEMM"``, ``"flm.GEMM"``),
    from its module and class name alone, so finding it imports nothing
    beyond what defining ``cls`` already did.

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
