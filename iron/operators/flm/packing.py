# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Weight packing shared by the FastFlowLM-derived operators.

Both flm.GEMM overlays, the port and the shipped image, consume B pre-packed into the order
the compute tiles read it, so their B transfers are plain linear descriptors.
The reorder is deliberately the caller's job: expressing it as a strided
descriptor over an unpacked B leaves an innermost run of ``t`` bf16 values, so
each transfer becomes thousands of scattered bursts -- measured 5.4x slower end
to end. Weights are packed once and reused across dispatches, so the cost
belongs here.
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
    overlay_order=False,
):
    """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

    ``s``/``t`` are the mmul's register tiling and ``ct_k`` the k slice one
    compute tile holds at a time; all three set the blocked layout, and packing
    with the wrong value produces a wrongly ordered buffer of the RIGHT SIZE, so
    it mis-computes silently rather than raising.

    With ``bfp16`` the result is a flat uint8 tensor of bfp16ebs8 blocks (9
    bytes per 8 values); otherwise a flat bf16 tensor. The quantization is not a
    loss this adds: the AIE2P mmul only multiplies bfp16, so the bf16 path would
    convert B inside every mac anyway. Doing it here hoists a rounding that
    already happened, and makes B 9 bytes per 8 values instead of 16.

    ``overlay_order`` swaps the two within-block k axes (``i`` and ``s_in``
    below). It exists solely for the shipped image (``iron.operators.flm.gemm.shipped``), whose
    B stream is read by FastFlowLM's shipped ``mm.xclbin``, not by a kernel
    built here: that overlay's own loop nest sweeps ``s_in`` outer and ``i``
    inner, the reverse of ``mm_fused_mmul_2x2``'s ``i``-outer loop. The
    now-deleted ``flm_pack_B`` (see ``bench_vs_flm.py`` history) verified this
    ordering against the overlay via ``tile.reshape(...).transpose(2, 1, 0,
    3)``; incompatible with ``bfp16``, which only the IRON-built kernel uses.
    """
    if overlay_order and bfp16:
        raise ValueError("overlay_order is bf16-only; the overlay never takes bfp16 B")
    K, N = B.shape
    if K % k_tile or N % n_tile:
        raise ValueError(f"B ({K}, {N}) must tile to ({k_tile}, {n_tile}) to be packed")
    col_a = ct_k // s
    blocked = B.reshape(
        K // k_tile, k_tile // ct_k, col_a, s, N // n_tile, n_tile // t, t
    )
    # (kb, kslice, i, s_in, cb, tb, t_in)
    if not bfp16:
        if overlay_order:
            #   -> (cb, kb, kslice, tb, s_in, i, t_in)
            out = np.ascontiguousarray(blocked.transpose(4, 0, 1, 5, 3, 2, 6)).reshape(
                -1
            )
        else:
            #   -> (cb, kb, kslice, tb, i, s_in, t_in)
            # Row-major s x t within the block, which is what the plain mmul
            # loads.
            out = np.ascontiguousarray(blocked.transpose(4, 0, 1, 5, 2, 3, 6)).reshape(
                -1
            )
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
