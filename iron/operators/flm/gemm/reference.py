# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np

from iron.operators.flm.gemm.design import Epilogue


def _sigmoid(x):
    """``1 / (1 + exp(-x))`` in float32, rounded once back to ``x``'s dtype."""
    f = x.astype(np.float32)
    return (1 / (1 + np.exp(-f))).astype(x.dtype)


def apply_epilogue(C, epilogue=Epilogue.NONE, clamp=None):
    """The fused output stage alone, applied to an already-accumulated C.

    Separate from ``reference`` because a test that wants to check the epilogue
    without the accumulation needs exactly this -- see
    ``test.py``'s accumulator comparison on the shipped image, where the device's own
    output is the input.

    ``gelu`` is the sigmoid approximation ``x * sigmoid(1.702x)``, matching the
    kernel -- NOT torch's erf-exact gelu, and not the tanh approximation the
    standalone gelu operator uses.
    """
    match Epilogue(epilogue):
        case Epilogue.NONE:
            pass
        case Epilogue.GELU:
            C = C * _sigmoid(np.float32(1.702) * C)
        case Epilogue.SILU:
            C = C * _sigmoid(C)
        case Epilogue.SIGMOID:
            C = _sigmoid(C)
    if clamp is not None:
        C = np.clip(C, clamp[0], clamp[1])
    return C


def reference(input_a, input_b, epilogue=Epilogue.NONE, clamp=None):
    """CPU reference ``C = clamp(activation(A @ B))``.

    Follows the kernel's order of operations rather than an idealized one: the
    matmul accumulates in fp32, mirroring the f32 accumulator, and the result is
    converted to the output dtype BEFORE the activation and clamp, because that
    is what the kernel does -- ``mm_fused_epilogue_chunk`` does
    ``to_v16bfloat16(acc)`` and then applies the activation to that bf16 vector.

    Measured end to end this ordering is second order, because the accumulator's
    own error dominates: at M=256 K=512 N=1024 it moves mean |err| by under
    2e-4 either way. It is worth doing because it models what the kernel does,
    and it is clearly visible once the accumulator is taken out of the
    comparison -- against the device's OWN accumulator on the shipped overlay it
    moves silu's worst-case disagreement from 0.043 to 0.031.

    Still not bit-exact, and cannot be. The remaining gap is the hardware's own
    activation approximation -- a LUT on AIE2, a native instruction on AIE2P --
    worth up to ~0.02 absolute there, which no CPU reference built on exact
    ``torch.sigmoid`` can reproduce. Tolerances have to absorb that part.
    """
    out_dtype = input_a.dtype
    C = np.matmul(input_a.astype(np.float32), input_b.astype(np.float32)).astype(
        out_dtype
    )
    return apply_epilogue(C, epilogue, clamp)
