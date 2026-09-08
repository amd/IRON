# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from iron.common.test_utils import torch_dtype_map


def _activation(x, epilogue):
    if epilogue == "none":
        return x
    if epilogue == "gelu":
        # Match the kernel, which uses the sigmoid approximation
        # gelu(x) ~= x * sigmoid(1.702x) -- NOT torch's erf-exact gelu, and not
        # the tanh approximation the standalone gelu operator uses.
        return x * torch.sigmoid(1.702 * x)
    if epilogue == "silu":
        return x * torch.sigmoid(x)
    if epilogue == "sigmoid":
        return torch.sigmoid(x)
    raise ValueError(f"unknown epilogue {epilogue!r}")


def reference(input_a, input_b, epilogue="none", clamp=None):
    """CPU reference ``C = clamp(activation(A @ B))``.

    The matmul is accumulated in fp32 to mirror the kernel's f32 accumulator,
    then cast back to the input dtype at the end, which is where the kernel
    converts too.
    """
    out_dtype = input_a.dtype
    C = torch.matmul(input_a.float(), input_b.float())
    C = _activation(C, epilogue)
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
