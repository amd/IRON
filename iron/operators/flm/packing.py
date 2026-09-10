# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Weight packing shared by the FastFlowLM-derived operators.

Both ``flm.GEMM`` and ``flm.MMPrebuilt`` consume B pre-packed into the order
the compute tiles read it, so their B transfers are plain linear descriptors.
The reorder is deliberately the caller's job: expressing it as a strided
descriptor over an unpacked B leaves an innermost run of ``t`` bf16 values, so
each transfer becomes thousands of scattered bursts -- measured 5.4x slower end
to end. Weights are packed once and reused across dispatches, so the cost
belongs here.
"""

import numpy as np
import torch


def f32_to_bfp16ebs8(a, round_conv_even=True):
    """float32 -> bfp16ebs8, matching the hardware's to_v64bfp16ebs8.

    Blocks of 8 share the max f32 exponent in the block; each mantissa is the
    24-bit magnitude with the implicit bit made explicit, shifted right by
    17 + (maxExp - exp) to land on the shared exponent.

    That shift OBEYS THE CORE'S ROUNDING MODE. mlir-aie's reference
    ``floatToBfp16`` (``programming_examples/ml/block_datatypes/helper.h``)
    hardcodes truncation and says AIE2P always truncates -- true only of the
    power-up ``floor`` mode. The operators here call ``set_rounding(conv_even)``,
    so the kernel's own conversion rounds to nearest with ties to even, and
    matching it here is what makes packing B on the host numerically free.
    Measured on hardware: 14.9375 -> 15 (rounds up) while 106.5 -> 106 and
    94.5 -> 94 (ties to even), which truncation cannot produce.

    Layout per block: one shared-exponent byte then the 8 mantissa bytes.
    """
    flat = np.ascontiguousarray(a, dtype=np.float32).reshape(-1, 8)
    u = flat.view(np.uint32)
    sign = (u & 0x80000000) != 0
    exp = ((u >> 23) & 0xFF).astype(np.int32)
    man = (u & 0x007FFFFF).astype(np.uint32)
    man = np.where(exp != 0, man | 0x00800000, man).astype(np.uint32)
    max_exp = exp.max(axis=1, keepdims=True)
    # signed magnitude; rounding below must see the sign to tie correctly
    mag = np.where(sign, -man.astype(np.int64), man.astype(np.int64))
    # The two shifts compose: 17 to keep 7 mantissa bits plus the sign, then
    # (maxExp - exp) to bring the value onto the block's shared exponent.
    shift = (max_exp - exp).astype(np.int64)
    total = np.clip(17 + shift, 0, 62)
    if round_conv_even:
        # np.rint is round-half-to-even. man < 2**24 and the divisor is a power
        # of two, so the quotient is exact in float64 and the only rounding is
        # the intended one.
        v8 = np.rint(mag.astype(np.float64) / np.exp2(total.astype(np.float64)))
    else:
        v8 = mag >> total
    v8 = np.where(shift >= 32, np.where(sign, -1, 0), v8)
    # Rounding can carry the block's largest magnitude from 127 to 128, which
    # does not fit the signed 8-bit mantissa; saturate rather than wrap.
    v8 = np.clip(v8, -128, 127)
    out = np.empty((flat.shape[0], 9), dtype=np.uint8)
    out[:, 0] = max_exp[:, 0].astype(np.uint8)
    out[:, 1:] = v8.astype(np.int8).view(np.uint8)
    return torch.from_numpy(out.reshape(-1))


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
    below). It exists solely for :class:`iron.operators.flm.MMPrebuilt`, whose
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
            return blocked.permute(4, 0, 1, 5, 3, 2, 6).reshape(-1).contiguous()
        #   -> (cb, kb, kslice, tb, i, s_in, t_in)
        # Row-major s x t within the block, which is what the plain mmul loads.
        return blocked.permute(4, 0, 1, 5, 2, 3, 6).reshape(-1).contiguous()
    #   -> (cb, kb, kslice, tb, i, t_in, s_in)
    # t-major within the block: the mixed mmul hands B straight to
    # mac_8x8_8x8T without the transpose the bf16 form applies, so the transpose
    # happens here instead. It also puts the 8 values that share a bfp16
    # exponent (8 consecutive k for one n) adjacent, which is what makes the
    # block grouping match the kernel's. Grouping over n instead measures
    # 1.95e-02 against this layout's 2.69e-04.
    blocked = blocked.permute(4, 0, 1, 5, 2, 6, 3).reshape(-1, 8).contiguous()
    return f32_to_bfp16ebs8(blocked.float().numpy(), round_conv_even=round_conv_even)


def packed_b_size(K, N, bfp16):
    """Elements (bf16) or bytes (bfp16ebs8) that ``pack_b`` returns."""
    return K * N // 8 * 9 if bfp16 else K * N
