# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The attention-context kernel, declared the way aie.iron.kernels declares one.

``gqa_context_bf16.cc`` is written to move to mlir-aie's ``aie_kernels/linalg``
unchanged, and this factory to ``aie.iron.kernels.linalg`` with only its
source path changed to ``_kernel_source("linalg/gqa_context_bf16.cc")``.
Until then the source sits beside this module, and the kernel library's
``linalg`` directory is on the include path so its ``../aie_kernel_utils.h``
resolves as it will there.

:func:`gqa_context_ref` is the arithmetic model: every float32 operation
the core performs, in its order, so it is bit-exact and the operator is
gated on exact equality.
"""

from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from aie.iron.kernel import ExternalFunction
from aie.iron.kernels._common import (
    KernelContract,
    Param,
    TensorLayout,
    Trace,
    _include_dirs,
    _make_extern,
)
from aie.utils.compile.jit.markers import In, InOut, Out
from aie.utils.verify import Tolerance

from iron.common.kernels import kernels_dir

# The flags argument: FIRST starts the sums, LAST rounds them into the output.
FIRST = 1
LAST = 2

# Partial sums per output element: the matvec's VEC_SIZE, whose order the
# kernel reproduces.
LANES = 64

_SOURCE = Path(__file__).with_name("gqa_context_bf16.cc")


def gqa_context(chunk: int = 128, head_dim: int = 64) -> ExternalFunction:
    """One head's context over ``chunk`` positions of its value cache.

    ``gqa_context(v, p, acc, out, flags)``: ``v`` is ``chunk`` rows of V
    (``(chunk, head_dim)``, the cache's own layout), ``p`` their probabilities,
    ``acc`` the core's ``LANES * head_dim`` float32 partial sums, carried from
    call to call, and ``out`` the ``head_dim`` bf16 context, written by the
    ``LAST`` call. The sum is ``linalg.mv``'s at ``vec_size=64``, operation for
    operation (see the source), so it equals that matvec over the transposed
    cache bit for bit.
    """
    if head_dim != LANES:
        raise ValueError(
            f"gqa_context: head_dim must be {LANES}, one vector per row of V "
            f"(got {head_dim})"
        )
    if chunk <= 0 or chunk % LANES:
        raise ValueError(
            f"gqa_context: chunk ({chunk}) must be a positive multiple of {LANES}"
        )
    return _make_extern(
        "gqa_context_bf16",
        _SOURCE,
        [
            np.ndarray[(chunk * head_dim,), np.dtype[bfloat16]],
            np.ndarray[(chunk,), np.dtype[bfloat16]],
            np.ndarray[(LANES * head_dim,), np.dtype[np.float32]],
            np.ndarray[(head_dim,), np.dtype[bfloat16]],
            np.int32,
        ],
        compile_flags=[f"-DCHUNK={chunk}", f"-DDIM_D={head_dim}"],
        include_dirs=_include_dirs() + [str(kernels_dir() / "linalg")],
        contract=KernelContract(
            trace=Trace.whole_call(),
            roles=(In, In, InOut, Out, Param),
            # Judged one whole context per call: the partial sums start and
            # finish in the same call, so acc is scratch.
            parameter_bindings=((4, FIRST | LAST),),
            layouts=(
                TensorLayout((chunk, head_dim)),
                TensorLayout((chunk,)),
                None,
                TensorLayout((head_dim,)),
                None,
            ),
            reference=lambda v, p: gqa_context_ref(
                v.reshape(-1, chunk, head_dim), p.reshape(-1, chunk), 1
            ),
            tolerance=Tolerance.exact(),
            acc_dtype=np.float32,
            reduction=chunk,
            ops_per_call=2 * chunk * head_dim,
        ),
    )


def gqa_context_ref(values, weights, heads_per_group: int) -> np.ndarray:
    """``ctx[h, d] = sum_l weights[h, l] * values[h // heads_per_group, l, d]``.

    ``values`` is ``(groups, L, D)`` and ``weights`` ``(groups *
    heads_per_group, L)``, both bf16; the result is ``(heads, D)`` bf16. Summed
    as the kernel sums: lane ``j`` of each output takes positions ``64 i + j``
    in order of ``i``, starting from the first product; the lanes are halved,
    lane ``j + 32`` onto lane ``j``, then 16, 8, 4, 2, 1; the float left is
    rounded to bf16, to nearest even. A product of two bf16 is exact in
    float32, so each step is one float32 addition, as on the core.
    """
    values = np.asarray(values, dtype=bfloat16)
    weights = np.asarray(weights, dtype=bfloat16)
    groups, length, dim = values.shape
    if length % LANES:
        raise ValueError(f"the context length ({length}) must be a multiple of {LANES}")
    heads = weights.shape[0]
    if weights.shape != (groups * heads_per_group, length):
        raise ValueError(
            f"weights {weights.shape} are not ({groups} x {heads_per_group}, {length})"
        )
    v = np.repeat(values.astype(np.float32), heads_per_group, axis=0)
    # (heads, rounds, lanes, D): position 64 i + j is round i, lane j.
    products = (v * weights.astype(np.float32)[:, :, None]).reshape(
        heads, length // LANES, LANES, dim
    )
    partial = products[:, 0].copy()
    for i in range(1, length // LANES):
        partial += products[:, i]
    half = LANES // 2
    while half >= 1:
        partial[:, :half] += partial[:, half : 2 * half]
        half //= 2
    return partial[:, 0].astype(bfloat16)
