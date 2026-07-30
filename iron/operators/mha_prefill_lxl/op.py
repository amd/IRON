# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Layer-by-layer (LxL) multi-head attention (MHA) prefill.

"Layer-by-layer" (LxL): each attention stage (score GEMM, scale, causal mask,
softmax, context GEMM) is a distinct operator, run back-to-back as an
OperatorSequence (a single dispatch on NPU2) rather than fused into one
monolithic kernel.  Contrast with the data-flow (DF) design in
iron/operators/mha_prefill_df/.
"""

import math

import aie.utils as aie_utils

from iron.common.context import AIEContext
from iron.common.sequence import OperatorSequence
from iron.operators.axpy.op import AXPY
from iron.operators.gemm.op import GEMM
from iron.operators.rope.op import RoPE
from iron.operators.strided_copy.op import StridedCopy
from iron.operators.repeat.op import Repeat
from iron.operators.softmax.op import Softmax
from iron.operators.transpose.op import Transpose
from iron.operators.elementwise_add.op import ElementwiseAdd


def _pick_tile_n(N, num_cols, max_tile_n=64):
    tile_n = N // num_cols
    while tile_n > max_tile_n:
        tile_n //= 2
    assert N % (tile_n * num_cols) == 0
    return tile_n


def _build_core_ops(H, G, d, S, elf_ctx, causal_mask=True, num_cols=None):
    """Build core attention sub-ops and runlist (no projections/RoPE/GQA).

    Expects pre-processed inputs:
      queries: (H, S, d) deinterleaved, contiguous per head
      keys: (H, d, S) transposed and GQA-repeated
      values: (H, S, d) GQA-repeated

    Produces:
      attn_context: (H, S, d) — per-head context vectors

    If causal_mask=False, the elementwise-add masking step is omitted.
    """
    if num_cols is None:
        num_cols = aie_utils.get_current_device().cols
    B = 2  # bytes per bf16 element

    # Cap each GEMM invocation's M dimension and split the per-head computation
    # into back-to-back GEMM invocations: the per-GEMM runtime sequence grows
    # linearly with M and can OOM the compiler at large S.  gemm_M_chunk must
    # be a multiple of tile_m * n_aie_rows = 64 and divide S evenly.
    gemm_M_chunk = min(S, 4096)
    assert (
        S % gemm_M_chunk == 0
    ), f"S ({S}) must be a multiple of gemm_M_chunk ({gemm_M_chunk})"
    n_m_chunks = S // gemm_M_chunk

    gemm_scores = GEMM(
        M=gemm_M_chunk,
        K=d,
        N=S,
        num_aie_columns=num_cols,
        tile_m=16,
        tile_k=64,
        tile_n=_pick_tile_n(S, num_cols),
        context=elf_ctx,
    )
    # Scale by 1/sqrt(d) in AXPY scale-only mode: the scalar is baked into the
    # kernel call instead of a materialised H*S*S broadcast buffer.
    scale = AXPY(
        size=H * S * S,
        tile_size=S * S // num_cols,
        num_aie_columns=num_cols,
        scalar_factor=1.0 / math.sqrt(d),
        add_y=False,
        context=elf_ctx,
    )
    if causal_mask:
        # Apply the causal mask via AXPY scalar-add + causal-mask mode: the
        # kernel writes -INF strictly above the per-head diagonal and copies
        # elsewhere, avoiding a materialised H*S*S mask buffer.  Each
        # invocation's transfer must stay under the compiler's int32 byte
        # limit (< 2^30 bf16 elements); large S is split into row-range slices
        # (one AXPY instance per row_offset).
        MASK_MAX_ELEMENTS_PER_INV = (1 << 30) - 1
        if S * S <= MASK_MAX_ELEMENTS_PER_INV:
            # Batch as many whole heads per invocation as divide H.
            heads_per_mask_inv = max(1, MASK_MAX_ELEMENTS_PER_INV // (S * S))
            while H % heads_per_mask_inv != 0:
                heads_per_mask_inv -= 1
            mask_subblocks = 1
            mask_rows_per_block = S
        else:
            # Split each head into row-range slices under the limit.
            heads_per_mask_inv = 1
            mask_subblocks = (
                S * S + MASK_MAX_ELEMENTS_PER_INV - 1
            ) // MASK_MAX_ELEMENTS_PER_INV
            while S % mask_subblocks != 0:
                mask_subblocks += 1
            mask_rows_per_block = S // mask_subblocks
            assert mask_rows_per_block * S <= MASK_MAX_ELEMENTS_PER_INV

        # Multi-core split: block-aligned across heads when batching whole
        # heads, otherwise across the row-range of the single block.
        if heads_per_mask_inv >= 2:
            mask_num_cols = min(num_cols, heads_per_mask_inv)
            while heads_per_mask_inv % mask_num_cols != 0:
                mask_num_cols -= 1
        else:
            mask_num_cols = num_cols
            while mask_rows_per_block % mask_num_cols != 0:
                mask_num_cols -= 1

        # One AXPY instance per row-range slice (exactly one when not split).
        mask_ops = [
            AXPY(
                size=heads_per_mask_inv * mask_rows_per_block * S,
                tile_size=min(4096, S),
                num_aie_columns=mask_num_cols,
                scalar_factor=float("-inf"),
                mul_x=False,
                add_y=True,
                causal_mask=True,
                mask_block_dim=S,
                rows_per_block=mask_rows_per_block,
                row_offset=sub_idx * mask_rows_per_block,
                context=elf_ctx,
            )
            for sub_idx in range(mask_subblocks)
        ]
    # Online/partial softmax once full-row FIFO tiles would exhaust the 64 KB
    # AIE local memory (each double-buffered FIFO pair uses 4 * tile_size B).
    softmax_chunk_size = 1024 if S >= 8192 else None

    # Split the softmax into back-to-back invocations on disjoint row ranges:
    # the compiler lowers the BD length through int32 byte arithmetic and
    # overflows when a single transfer reaches 2^30 bf16 elements.
    SOFTMAX_MAX_ELEMENTS_PER_INV = (1 << 30) - 1
    total_softmax_rows = H * S
    if total_softmax_rows * S <= SOFTMAX_MAX_ELEMENTS_PER_INV:
        n_softmax_invocations = 1
    else:
        # Smallest n that divides total_softmax_rows and keeps each
        # invocation's transfer at or below the limit.
        n_softmax_invocations = (
            total_softmax_rows * S + SOFTMAX_MAX_ELEMENTS_PER_INV - 1
        ) // SOFTMAX_MAX_ELEMENTS_PER_INV
        while (
            total_softmax_rows % n_softmax_invocations != 0
            or (total_softmax_rows // n_softmax_invocations) * S
            > SOFTMAX_MAX_ELEMENTS_PER_INV
        ):
            n_softmax_invocations += 1
    softmax_rows_per_inv = total_softmax_rows // n_softmax_invocations
    assert softmax_rows_per_inv % 16 == 0, (
        f"softmax_rows_per_inv ({softmax_rows_per_inv}) must be a multiple of 16; "
        f"got total_rows={total_softmax_rows}, n_invocations={n_softmax_invocations}"
    )

    # Largest divisor of softmax_rows_per_inv that is <= num_cols.
    softmax_num_cols = num_cols
    while softmax_rows_per_inv % softmax_num_cols != 0:
        softmax_num_cols -= 1

    softmax = Softmax(
        rows=softmax_rows_per_inv,
        cols=S,
        num_aie_columns=softmax_num_cols,
        num_channels=1,
        rtp_vector_size=S,
        chunk_size=softmax_chunk_size,
        context=elf_ctx,
    )
    # Context GEMM capped at 4 cores: with N=d=64 the matmul constraint
    # n % (2*tile_n) == 0 forces tile_n*num_aie_columns = 64, so cols <= 4.
    gemm_context = GEMM(
        M=gemm_M_chunk,
        K=S,
        N=d,
        num_aie_columns=min(4, num_cols),
        tile_m=16,
        tile_k=64,
        tile_n=_pick_tile_n(d, min(4, num_cols)),
        context=elf_ctx,
        prio_accuracy=True,
    )

    # Per-head byte sizes
    qh = S * d * B  # queries per head: (S, d)
    kdS = d * S * B  # keys per head:    (d, S)
    kSd = S * d * B  # values per head:  (S, d)
    sh = S * S * B  # scores/weights per head: (S, S)
    ch = S * d * B  # context per head: (S, d)

    # Per-M-chunk byte sizes (the M dimension is contiguous in row-major
    # storage so M-slices map directly to byte ranges within each head)
    q_chunk = gemm_M_chunk * d * B  # queries chunk: (M_chunk, d)
    s_chunk = gemm_M_chunk * S * B  # scores chunk:  (M_chunk, S)
    w_chunk = gemm_M_chunk * S * B  # weights chunk: (M_chunk, S)
    c_chunk = gemm_M_chunk * d * B  # context chunk: (M_chunk, d)

    # Single (H, S, S) scratch buffer reused in-place throughout the chain
    # (score → scale → [mask] → softmax → context) to halve scratch memory.
    attn_buf = "attn"
    scores_buf = scaled_buf = masked_buf = weights_buf = attn_buf

    score_calls = [
        (
            gemm_scores,
            f"queries[{h*qh + i*q_chunk}:{h*qh + (i+1)*q_chunk}]",
            f"keys[{h*kdS}:{(h+1)*kdS}]",
            f"{scores_buf}[{h*sh + i*s_chunk}:{h*sh + (i+1)*s_chunk}]",
        )
        for h in range(H)
        for i in range(n_m_chunks)
    ]

    context_calls = [
        (
            gemm_context,
            f"{weights_buf}[{h*sh + i*w_chunk}:{h*sh + (i+1)*w_chunk}]",
            f"values[{h*kSd}:{(h+1)*kSd}]",
            f"attn_context[{h*ch + i*c_chunk}:{h*ch + (i+1)*c_chunk}]",
        )
        for h in range(H)
        for i in range(n_m_chunks)
    ]

    # Build the softmax runlist entries (one per invocation when row-split).
    softmax_input_buf = masked_buf if causal_mask else scaled_buf
    softmax_chunk_bytes = softmax_rows_per_inv * S * B
    if n_softmax_invocations == 1:
        softmax_calls = [(softmax, softmax_input_buf, weights_buf)]
    else:
        softmax_calls = [
            (
                softmax,
                f"{softmax_input_buf}[{i*softmax_chunk_bytes}:{(i+1)*softmax_chunk_bytes}]",
                f"{weights_buf}[{i*softmax_chunk_bytes}:{(i+1)*softmax_chunk_bytes}]",
            )
            for i in range(n_softmax_invocations)
        ]

    runlist = [
        *score_calls,
        (scale, scores_buf, scaled_buf),
    ]

    if causal_mask:
        # One (input, output) entry per disjoint slice; mask values are baked
        # into the kernel call (scalar -INF), so no mask buffer is needed.
        n_head_groups = H // heads_per_mask_inv
        head_group_bytes = heads_per_mask_inv * S * S * B
        sub_chunk_bytes = mask_rows_per_block * S * B
        mask_calls = []
        for g in range(n_head_groups):
            for sub_idx in range(mask_subblocks):
                start = g * head_group_bytes + sub_idx * sub_chunk_bytes
                end = start + heads_per_mask_inv * sub_chunk_bytes
                mask_calls.append(
                    (
                        mask_ops[sub_idx],
                        f"{scaled_buf}[{start}:{end}]",
                        f"{masked_buf}[{start}:{end}]",
                    )
                )
        if n_head_groups == 1 and mask_subblocks == 1:
            # Whole-buffer fast path (avoids slice notation in MLIR).
            runlist += [(mask_ops[0], scaled_buf, masked_buf)]
        else:
            runlist += mask_calls

    runlist += softmax_calls
    runlist += context_calls

    buffer_sizes = {
        "queries": H * S * d * B,
        "keys": H * d * S * B,
        "values": H * S * d * B,
        "attn": H * S * S * B,
        "attn_context": H * S * d * B,
    }

    return runlist, buffer_sizes


class AttentionPrefillFused(OperatorSequence):
    """Fused attention prefill (core, no projections/RoPE).

    Accepts pre-projected Q (S*H,d), K (S*G,d), V (S*G,d) in interleaved layout.
    """

    def __init__(
        self,
        num_heads,
        num_kv_groups,
        head_dim,
        embedding_dim,
        seq_len,
        causal_mask=True,
        context=None,
        dispatch="auto",
    ):
        assert head_dim == 64
        assert num_heads % num_kv_groups == 0
        assert seq_len % 256 == 0
        assert (num_heads * seq_len) % 16 == 0

        self.num_heads = num_heads
        self.num_kv_groups = num_kv_groups
        self.head_dim = head_dim
        self.embedding_dim = embedding_dim
        self.seq_len = seq_len

        elf_ctx = context or AIEContext()
        runlist, buffer_sizes = _build_core_ops(
            num_heads,
            num_kv_groups,
            head_dim,
            seq_len,
            elf_ctx,
            causal_mask=causal_mask,
        )

        mask_suffix = "_causal" if causal_mask else "_nomask"
        input_args = ["queries", "keys", "values"]

        super().__init__(
            name=f"attention_prefill_fused_{num_heads}h{num_kv_groups}g{head_dim}d{embedding_dim}e{seq_len}s{mask_suffix}",
            runlist=runlist,
            input_args=input_args,
            output_args=["attn_context"],
            buffer_sizes=buffer_sizes,
            dispatch=dispatch,
            context=elf_ctx,
        )


class AttentionPrefillProjectedFused(OperatorSequence):
    """Fused attention prefill with Q/K/V projections and RoPE.

    Accepts raw input (S, E) and rope_angles (S, d).
    """

    def __init__(
        self,
        num_heads,
        num_kv_groups,
        head_dim,
        embedding_dim,
        seq_len,
        causal_mask=True,
        context=None,
        dispatch="auto",
    ):
        assert head_dim == 64
        assert num_heads % num_kv_groups == 0
        assert seq_len % 256 == 0
        assert (num_heads * seq_len) % 16 == 0

        self.num_heads = num_heads
        self.num_kv_groups = num_kv_groups
        self.head_dim = head_dim
        self.embedding_dim = embedding_dim
        self.seq_len = seq_len
        self._dispatch_arg = dispatch

        H, G, d, E, S = num_heads, num_kv_groups, head_dim, embedding_dim, seq_len
        group_size = H // G
        B = 2
        num_cols = aie_utils.get_current_device().cols

        elf_ctx = context or AIEContext()

        # ---- Projection + RoPE ----
        gemm_query = GEMM(
            M=S,
            K=E,
            N=H * d,
            num_aie_columns=num_cols,
            tile_m=16,
            tile_k=64,
            tile_n=_pick_tile_n(H * d, num_cols),
            context=elf_ctx,
        )
        gemm_kv = GEMM(
            M=S,
            K=E,
            N=G * d,
            num_aie_columns=num_cols,
            tile_m=16,
            tile_k=64,
            tile_n=_pick_tile_n(G * d, num_cols),
            context=elf_ctx,
        )
        rope_queries = RoPE(rows=S * H, cols=d, angle_rows=S, context=elf_ctx)
        rope_keys = RoPE(rows=S * G, cols=d, angle_rows=S, context=elf_ctx)

        # ---- Deinterleave ----
        deinterleave_q = StridedCopy(
            input_sizes=(H, S, d),
            input_strides=(d, H * d, 1),
            input_offset=0,
            output_sizes=(H, S, d),
            output_strides=(S * d, d, 1),
            output_offset=0,
            input_buffer_size=S * H * d,
            output_buffer_size=H * S * d,
            transfer_size=S * d,
            num_aie_channels=1,
            context=elf_ctx,
        )
        deinterleave_kv = StridedCopy(
            input_sizes=(G, S, d),
            input_strides=(d, G * d, 1),
            input_offset=0,
            output_sizes=(G, S, d),
            output_strides=(S * d, d, 1),
            output_offset=0,
            input_buffer_size=S * G * d,
            output_buffer_size=G * S * d,
            transfer_size=S * d,
            num_aie_channels=1,
            context=elf_ctx,
        )

        # ---- Transpose keys + GQA repeat ----
        transpose_keys = Transpose(
            M=S,
            N=d,
            num_aie_columns=2,
            num_channels=1,
            m=256,
            n=32,
            s=8,
            context=elf_ctx,
        )
        repeat_kv = Repeat(
            rows=G,
            cols=d * S,
            repeat=group_size,
            transfer_size=d,
            context=elf_ctx,
        )

        kSd = S * d * B
        kdS = d * S * B

        prefix_runlist = [
            (gemm_query, "input", "W_query", "queries_projected"),
            (gemm_kv, "input", "W_key", "keys_projected"),
            (gemm_kv, "input", "W_value", "values_projected"),
            (rope_queries, "queries_projected", "rope_angles", "queries_roped"),
            (rope_keys, "keys_projected", "rope_angles", "keys_roped"),
            (deinterleave_q, "queries_roped", "queries"),
            (deinterleave_kv, "keys_roped", "keys_deint"),
            (deinterleave_kv, "values_projected", "values_deint"),
            *[
                (
                    transpose_keys,
                    f"keys_deint[{g*kSd}:{(g+1)*kSd}]",
                    f"keys_transposed[{g*kdS}:{(g+1)*kdS}]",
                )
                for g in range(G)
            ],
            (repeat_kv, "keys_transposed", "keys"),
            (repeat_kv, "values_deint", "values"),
        ]
        prefix_buffer_sizes = {
            "queries_projected": S * H * d * B,
            "keys_projected": S * G * d * B,
            "values_projected": S * G * d * B,
            "queries_roped": S * H * d * B,
            "keys_roped": S * G * d * B,
            "keys_deint": G * S * d * B,
            "values_deint": G * S * d * B,
            "keys_transposed": G * d * S * B,
        }

        core_runlist, core_buffer_sizes = _build_core_ops(
            H,
            G,
            d,
            S,
            elf_ctx,
            causal_mask=causal_mask,
            num_cols=num_cols,
        )

        # ---- Reinterleave + output projection ----
        # Scatter attn_context (H, S, d) -> context_interleaved (S, H*d). S is
        # split into (S//256, 256) so no DMA dimension exceeds the BD size
        # limit. The split dims must pair with their strides: the outer
        # (S//256) block dim uses stride 256*H*d and the inner 256-row dim uses
        # stride H*d, so a row s = outer*256 + inner lands at s*H*d. Swapping
        # the two sizes makes the 256-dim take the 256*H*d stride and write far
        # past the buffer -> host-heap corruption / segfaults.
        reinterleave = StridedCopy(
            input_sizes=(1, 1, 1, H * S * d),
            input_strides=(0, 0, 0, 1),
            input_offset=0,
            output_sizes=(H, S // 256, 256, d),
            output_strides=(d, 256 * H * d, H * d, 1),
            output_offset=0,
            input_buffer_size=H * S * d,
            output_buffer_size=S * H * d,
            transfer_size=S * d,
            num_aie_channels=1,
            context=elf_ctx,
        )
        gemm_output = GEMM(
            M=S,
            K=H * d,
            N=E,
            num_aie_columns=num_cols,
            tile_m=16,
            tile_k=64,
            tile_n=_pick_tile_n(E, num_cols),
            context=elf_ctx,
            prio_accuracy=True,
        )

        suffix_runlist = [
            (reinterleave, "attn_context", "context_interleaved"),
            (gemm_output, "context_interleaved", "W_output", "attn_output"),
        ]
        suffix_buffer_sizes = {
            "context_interleaved": S * H * d * B,
        }

        mask_suffix = "_causal" if causal_mask else "_nomask"
        input_args = [
            "input",
            "rope_angles",
            "W_query",
            "W_key",
            "W_value",
            "W_output",
        ]

        super().__init__(
            name=f"attention_prefill_projected_fused_{H}h{G}g{d}d{E}e{S}s{mask_suffix}",
            runlist=prefix_runlist + core_runlist + suffix_runlist,
            input_args=input_args,
            output_args=["attn_output"],
            buffer_sizes={
                **prefix_buffer_sizes,
                **core_buffer_sizes,
                **suffix_buffer_sizes,
            },
            dispatch=dispatch,
            context=elf_ctx,
        )
