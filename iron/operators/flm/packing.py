# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Weight packing for flm.ProjectionGEMM, which consumes B pre-packed into
compute-tile read order so its transfers are plain linear descriptors. The
reorder is deliberately the caller's job: an unpacked B's strided descriptor
scatters each transfer into many small bursts of ``t`` bf16 values; packing
once and reusing it across dispatches amortizes that cost.
"""

import numpy as np
from aie.utils import bfp
from ml_dtypes import bfloat16


def pack_b(
    B,
    k_tile,
    n_tile,
    s,
    t,
    ct_k,
    bfp16=False,
    round_conv_even=True,
):
    """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

    ``s``/``t`` are the mmul's register tiling and ``ct_k`` the k slice one
    compute tile holds at a time; the wrong value silently produces a
    wrongly ordered buffer of the right size rather than raising.

    ``bfp16`` returns a flat uint8 tensor of bfp16ebs8 blocks (9 bytes per 8
    values) instead of bf16; since the AIE2P mmul only multiplies bfp16
    anyway, this hoists a rounding that would otherwise happen in every mac.
    """
    K, N = B.shape
    if K % k_tile or N % n_tile:
        raise ValueError(
            f"pack_b: B ({K}, {N}) must tile to ({k_tile}, {n_tile}) to be packed"
        )
    col_a = ct_k // s
    blocked = B.reshape(
        K // k_tile, k_tile // ct_k, col_a, s, N // n_tile, n_tile // t, t
    )
    # (kb, kslice, i, s_in, cb, tb, t_in)
    if not bfp16:
        #   -> (cb, kb, kslice, tb, i, s_in, t_in)
        # Row-major s x t within the block, which is what the plain mmul
        # loads.
        out = np.ascontiguousarray(blocked.transpose(4, 0, 1, 5, 2, 3, 6)).reshape(-1)
        # Callers may pass B in whatever dtype they have it in (e.g. a model's
        # native f32 weight); the kernels and the declared buffers assume the result
        # is bf16, so guarantee that here rather than silently returning
        # whatever B.dtype was.
        return out.astype(bfloat16)
    #   -> (cb, kb, kslice, tb, i, t_in, s_in)
    # t-major within the block: the mixed mmul hands B straight to
    # mac_8x8_8x8T without the transpose the bf16 form applies, so the transpose
    # happens here instead. It also puts the 8 values that share a bfp16
    # exponent (8 consecutive k for one n) adjacent, which is what makes the
    # block grouping match the kernel's. Grouping over n instead measures
    # 1.95e-02 against this layout's 2.69e-04.
    #
    # The kernels call set_rounding(conv_even), so their own conversion rounds
    # to nearest, ties to even (on hardware 14.9375 -> 15, 106.5 -> 106, 94.5
    # -> 94); packing B in that mode is what makes it numerically free.
    blocked = np.ascontiguousarray(blocked.transpose(4, 0, 1, 5, 2, 6, 3))
    rounding = "conv_even" if round_conv_even else "floor"
    return bfp.encode(blocked.reshape(-1).astype(np.float32), rounding=rounding)


def packed_b_size(K, N, bfp16):
    """Elements (bf16) or bytes (bfp16ebs8) that ``pack_b`` returns."""
    return K * N // 8 * 9 if bfp16 else K * N
