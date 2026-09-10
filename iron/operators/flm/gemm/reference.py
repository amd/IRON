# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def reference(input_a, input_b, epilogue="none", clamp=None):
    """CPU reference ``C = clamp(activation(A @ B))``.

    The matmul is accumulated in fp32 to mirror the kernel's f32 accumulator.
    This is an idealized reference, not operation-for-operation matching: it
    applies the activation and clamp in fp32 and casts to the input dtype only
    at the end, whereas the kernel (``mm_fused_epilogue_chunk`` in
    ``mm_fused_epilogue.cc``) converts the accumulator to bf16 first and then
    applies the activation and clamp in bf16. The two are close enough that the
    per-test tolerances absorb the difference, but do not expect a bit-exact
    match.

    ``gelu`` is the sigmoid approximation ``x * sigmoid(1.702x)``, matching the
    kernel -- NOT torch's erf-exact gelu, and not the tanh approximation the
    standalone gelu operator uses.
    """
    out_dtype = input_a.dtype
    C = torch.matmul(input_a.float(), input_b.float())
    if epilogue == "gelu":
        C = C * torch.sigmoid(1.702 * C)
    elif epilogue == "silu":
        C = C * torch.sigmoid(C)
    elif epilogue == "sigmoid":
        C = torch.sigmoid(C)
    elif epilogue != "none":
        raise ValueError(f"unknown epilogue {epilogue!r}")
    if clamp is not None:
        C = torch.clamp(C, clamp[0], clamp[1])
    return C.to(out_dtype)


def generate_golden_reference(
    M: int,
    K: int,
    N: int,
    dtype="bf16",
    seed=42,
    epilogue="none",
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
