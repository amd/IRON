# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map
from iron.operators.flm.gemm.design import Epilogue


def apply_epilogue(C, epilogue=Epilogue.NONE, clamp=None):
    """The fused output stage alone, applied to an already-accumulated C.

    Separate from ``reference`` because a test that wants to check the epilogue
    without the accumulation needs exactly this -- see
    ``mm_prebuilt/test.py``'s accumulator comparison, where the device's own
    output is the input.

    ``gelu`` is the sigmoid approximation ``x * sigmoid(1.702x)``, matching the
    kernel -- NOT torch's erf-exact gelu, and not the tanh approximation the
    standalone gelu operator uses.
    """
    match Epilogue(epilogue):
        case Epilogue.NONE:
            pass
        case Epilogue.GELU:
            C = C * torch.sigmoid(1.702 * C)
        case Epilogue.SILU:
            C = C * torch.sigmoid(C)
        case Epilogue.SIGMOID:
            C = torch.sigmoid(C)
    if clamp is not None:
        C = torch.clamp(C, clamp[0], clamp[1])
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
    C = torch.matmul(input_a.float(), input_b.float()).to(out_dtype)
    return apply_epilogue(C, epilogue, clamp)


def generate_golden_reference(
    M: int,
    K: int,
    N: int,
    dtype="bf16",
    seed=42,
    epilogue=Epilogue.NONE,
    clamp=None,
    scale=4.0,
):
    """Random A (signed) and B (non-negative), scaled by ``scale``.

    ``scale`` matters for the epilogue tests: the result grows like
    ``sqrt(K) * scale**2``, and at the default scale a K=512 product lands
    around +-200, where gelu/silu are indistinguishable from the identity (or
    from zero). Activation tests pass a smaller scale so the result sits in the
    range where the curve is actually interesting.
    """
    torch.manual_seed(seed)
    dtype_torch = torch_dtype_map[dtype]
    input_a = torch.randn(M, K, dtype=dtype_torch) * scale
    input_b = torch.rand(K, N, dtype=dtype_torch) * scale
    output = reference(input_a, input_b, epilogue, clamp)
    return {"input": input_a, "input_b": input_b, "output": output}
