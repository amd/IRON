#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Next steps for decode performance:
# [ ] All decode operators operate on 2048-padded buffers; instead, should bin into shorter sequence lengths and call smaller operators
# [ ] Opportunity to fuse data layout transformations (e.g., transpose ops) onto end of other operations (e.g., transpose after RoPE)
# [ ] Some kernels are not optimized; e.g., softmax masking is using scalar cores
# [ ] Fine-tune parameters of operators (e.g., num AIE columns, tile sizes)
# [ ] Patching of operators (instantiating new xrt::elf for each token) is slow; find quicker way of patching instruction sequence in-memory
# [ ] Spatial fusion of operators

import torch
import math
from pathlib import Path
import sys
import numpy as np
import ml_dtypes
import llama_inference_harness as harness
import logging

repo_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(repo_root))

from iron.common.context import AIEContext
from iron.common.utils import XRTSubBuffer
from iron.common.fusion import (
    FusedMLIROperator,
    FusedFullELFCallable,
    load_elf,
    patch_elf,
)
from iron.operators import (
    RMSNorm,
    GEMM,
    GEMV,
    ElementwiseAdd,
    ElementwiseMul,
    SiLU,
    RoPE,
    StridedCopy,
    Repeat,
    Softmax,
    Transpose,
)
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

max_seq_len = 2048

aie_ops = None
aie_buffers = None


# AIE Operator Configuration
# ##########################################################################


class AIEPrefillOperations:
    pass


class AIEDecodeOperations:
    pass


class AIELlamaOperators:

    def __init__(self, config, prompt_len):
        self.context = AIEContext()
        self.context.build_dir.mkdir(parents=True, exist_ok=True)

        self.prefill = AIEPrefillOperations()
        self.decode = AIEDecodeOperations()

        # ##################################################################
        # Prefill operators

        self.prefill.rms_norm = (
            RMSNorm(
                size=prompt_len * config.emb_dim,
                num_aie_columns=8,
                num_channels=1,  # weighted=True with 8 columns needs 9 ShimDMA fills/channel; max 16 total forces num_channels=1
                tile_size=config.emb_dim,
                weighted=True,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        self.prefill.residual_add = (
            ElementwiseAdd(size=prompt_len * config.emb_dim, tile_size=config.emb_dim)
            .compile()
            .get_callable()
        )

        min_N = 64 * 8 * 4  # tile_n * num_aie_columns * partition_N
        config.padded_vocab_size = (config.vocab_size + min_N - 1) // min_N * min_N
        config.vocab_partitions = 4
        self.prefill.gemv_out_head_compilable = GEMM(
            M=prompt_len,
            K=config.emb_dim,
            N=config.padded_vocab_size // config.vocab_partitions,
            num_aie_columns=8,
            tile_m=64,
            tile_k=64,
            tile_n=64,
            b_col_maj=True,
            separate_c_tiles=True,
            context=self.context,
        ).compile()
        self.prefill.out_head = self.prefill.gemv_out_head_compilable.get_callable()

        # SwiGLU FFN operators
        # Prefill: M=prompt_len, K=emb_dim, N=hidden_dim
        self.prefill.ffn_up_gate = (
            GEMM(
                M=prompt_len,
                K=config.emb_dim,
                N=config.hidden_dim,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,  # exceeds stride dimensions otherwise; just transpose weights
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        self.prefill.ffn_down = (
            GEMM(
                M=prompt_len,
                K=config.hidden_dim,
                N=config.emb_dim,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,  # exceeds stride dimensions otherwise; just transpose weights
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        self.prefill.ffn_silu = (
            SiLU(
                size=prompt_len * config.hidden_dim,
                tile_size=config.hidden_dim,
                num_aie_columns=8,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        self.prefill.eltwise_mul_ffn = (
            ElementwiseMul(
                size=prompt_len * config.hidden_dim,
                tile_size=config.hidden_dim,
                num_aie_columns=8,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Attention score scaling operators
        # FIXME: Using elementwise mul is very wasteful (of bandwidth) here since it's the same scalar factor for all values; need a kernel that allows scalar multiplication of a vector; maybe use AXPY
        self.prefill.attn_scale = (
            ElementwiseMul(
                size=config.n_heads * prompt_len * prompt_len,
                tile_size=prompt_len,
                num_aie_columns=8,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # RoPE operators
        # For queries: (seq_len, num_heads * head_dim) = (seq_len, 2048)
        # For keys: (seq_len, num_kv_groups * head_dim) = (seq_len, 512)
        # angle_rows=1 because all rows use the same angle row (angles are per position)
        self.prefill.rope_queries = (
            RoPE(
                rows=prompt_len * config.n_heads,
                cols=config.head_dim,
                angle_rows=prompt_len,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        self.prefill.rope_keys = (
            RoPE(
                rows=prompt_len * config.n_kv_groups,
                cols=config.head_dim,
                angle_rows=prompt_len,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Attention projection operators
        # Query projection: (seq_len, emb_dim) -> (seq_len, n_heads * head_dim)
        self.prefill.attn_query = (
            GEMM(
                M=prompt_len,
                K=config.emb_dim,
                N=config.n_heads * config.head_dim,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Key projection: (seq_len, emb_dim) -> (seq_len, n_kv_groups * head_dim)
        self.prefill.attn_key = (
            GEMM(
                M=prompt_len,
                K=config.emb_dim,
                N=config.n_kv_groups * config.head_dim,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Value projection: (seq_len, emb_dim) -> (seq_len, n_kv_groups * head_dim)
        self.prefill.attn_value = (
            GEMM(
                M=prompt_len,
                K=config.emb_dim,
                N=config.n_kv_groups * config.head_dim,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Attention score computation: Q @ K^T per head
        # For prefill: (seq_len, head_dim) @ (head_dim, seq_len) = (seq_len, seq_len) per head
        self.prefill.attn_scores = (
            GEMM(
                M=prompt_len,
                K=config.head_dim,
                N=prompt_len,
                num_aie_columns=8,
                tile_m=64,
                tile_k=64,
                tile_n=64,
                b_col_maj=False,
                context=self.context,
            )
            .compile()
            .get_callable()
        )

        # Decode operator (everything temporally fused)
        # ##################################################################

        elf_ctx = AIEContext(build_dir="build_elf")

        gemv_attn_query_op = GEMV(
            M=config.n_heads * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=elf_ctx,
        )

        gemv_attn_key_value_op = GEMV(
            M=config.n_kv_groups * config.head_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.head_dim // 2,
            context=elf_ctx,
        )

        # decode processes 1 query token at a time
        rope_queries_op = RoPE(
            rows=config.n_heads, cols=config.head_dim, angle_rows=1, context=elf_ctx
        )

        rope_keys_op = RoPE(
            rows=config.n_kv_groups,
            cols=config.head_dim,
            angle_rows=1,
            context=elf_ctx,
        )

        strided_copy_cache_magic = 0xDEADBEE0
        strided_copy_cache_op = StridedCopy(
            input_sizes=(config.n_kv_groups, config.head_dim),
            input_strides=(config.head_dim, 1),
            input_offset=0,
            output_sizes=(1, config.n_kv_groups, config.head_dim),
            output_strides=(0, prompt_len * config.head_dim, 1),
            output_offset=7 * config.head_dim * 2,  # Will be patched at runtime
            input_buffer_size=1 * config.n_kv_groups * config.head_dim,
            output_buffer_size=config.n_kv_groups * prompt_len * config.head_dim,
            num_aie_channels=1,
            kwargs={"output_offset_patch_marker": strided_copy_cache_magic},
            context=elf_ctx,
        )

        # For decode: per head, (1, head_dim) @ (head_dim, max_context_len)
        # Use GEMV: (max_context_len, head_dim) @ (head_dim,) = (max_context_len,)
        gemv_attn_scores_op = GEMV(
            M=prompt_len,  # max possible context length
            K=config.head_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=prompt_len // 8,
            num_batches=config.n_heads,
            context=elf_ctx,
        )

        attn_scale_op = ElementwiseMul(
            size=config.n_heads * prompt_len,
            tile_size=prompt_len // 8,
            num_aie_columns=8,
            context=elf_ctx,
        )

        # Softmax operators for attention weights
        softmax_magic = 0xBA5EBA11
        softmax_op = Softmax(
            rows=config.n_heads,
            cols=prompt_len,
            num_aie_columns=1,
            num_channels=1,
            rtp_vector_size=prompt_len,  # Compile with max size
            mask_patch_value=softmax_magic,  # Magic value for patching
            context=elf_ctx,
        )

        # Fused transpose for all attention heads (decode)
        transpose_values_op = Transpose(
            M=prompt_len,
            N=config.head_dim,
            num_aie_columns=2,
            num_channels=1,
            m=256,
            n=32,
            s=8,
            context=elf_ctx,
        )

        # GEMV for attention context: (head_dim, max_context_len) @ (max_context_len,) = (head_dim,) per head
        gemv_attn_context_op = GEMV(
            M=config.head_dim,
            K=prompt_len,  # max possible context length
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=4,
            num_batches=config.n_heads,
            context=elf_ctx,
        )

        gemv_attn_output_op = GEMV(
            M=config.emb_dim,
            K=config.n_heads * config.head_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.emb_dim // 8,
            context=elf_ctx,
        )

        rms_norm_op = RMSNorm(
            size=config.emb_dim,
            num_aie_columns=1,
            num_channels=1,
            tile_size=config.emb_dim,
            weighted=True,
            context=elf_ctx,
        )

        gemv_ffn_up_gate_op = GEMV(
            M=config.hidden_dim,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=config.hidden_dim // 8,
            context=elf_ctx,
        )

        gemv_ffn_down_op = GEMV(
            M=config.emb_dim,
            K=config.hidden_dim,
            num_aie_columns=8,
            tile_size_input=1,
            tile_size_output=config.emb_dim // 8,
            context=elf_ctx,
        )

        silu_ffn_op = SiLU(
            size=config.hidden_dim,
            tile_size=config.hidden_dim // 8,
            num_aie_columns=8,
            context=elf_ctx,
        )

        eltwise_mul_ffn_op = ElementwiseMul(
            size=config.hidden_dim,
            tile_size=config.hidden_dim // 8,
            num_aie_columns=8,
            context=elf_ctx,
        )

        residual_add_op = ElementwiseAdd(
            size=config.emb_dim, tile_size=config.emb_dim // 8, context=elf_ctx
        )

        repeat_interleave_op = Repeat(
            rows=config.n_kv_groups,
            cols=prompt_len * config.head_dim,  # Max context length
            repeat=config.n_heads // config.n_kv_groups,
            transfer_size=config.head_dim,
            context=elf_ctx,
        )

        gemv_out_head_op = GEMV(
            M=config.vocab_size,
            K=config.emb_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=32,
            context=self.context,
        )

        # Create fused operator

        cache_buffer_size = (
            config.n_kv_groups * prompt_len * config.head_dim * 2
        )  # * 2 for bfloat16
        values_per_head_buffer_size = (
            prompt_len * config.head_dim * 2
        )  # * 2 for bfloat16
        values_buffer_size = config.n_heads * values_per_head_buffer_size

        runlist = []
        for layer_idx in range(config.n_layers):
            # <transformer block>
            runlist.extend(
                [
                    (
                        rms_norm_op,
                        "x",
                        f"W_norm1_{layer_idx}",
                        "x_norm",
                    )  # Step 1: RMS normalization
                ]
                + [
                    # <grouped query attention>
                    (
                        gemv_attn_query_op,
                        f"W_attn_query_{layer_idx}",
                        "x_norm",
                        "queries",
                    ),
                    (
                        gemv_attn_key_value_op,
                        f"W_attn_key_{layer_idx}",
                        "x_norm",
                        "keys",
                    ),
                    (
                        gemv_attn_key_value_op,
                        f"W_attn_value_{layer_idx}",
                        "x_norm",
                        "values",
                    ),
                    (rope_queries_op, "queries", "rope_angles", "queries"),
                    (rope_keys_op, "keys", "rope_angles", "keys"),
                    (strided_copy_cache_op, "keys", f"keys_cache_{layer_idx}"),
                    (strided_copy_cache_op, "values", f"values_cache_{layer_idx}"),
                    (
                        repeat_interleave_op,
                        f"keys_cache_{layer_idx}",
                        "attn_scores_keys",
                    ),
                    (
                        repeat_interleave_op,
                        f"values_cache_{layer_idx}",
                        "attn_scores_values",
                    ),
                    (gemv_attn_scores_op, "attn_scores_keys", "queries", "attn_scores"),
                    (attn_scale_op, "attn_scores", "attn_scale_factor", "attn_scores"),
                    (softmax_op, "attn_scores", "attn_weights"),
                ]
                + [
                    (
                        transpose_values_op,
                        f"attn_scores_values[{h * values_per_head_buffer_size}:{(h + 1) * values_per_head_buffer_size}]",
                        f"attn_scores_values_transposed[{h * values_per_head_buffer_size}:{(h + 1) * values_per_head_buffer_size}]",
                    )
                    for h in range(config.n_heads)
                ]
                + [
                    (
                        gemv_attn_context_op,
                        "attn_scores_values_transposed",
                        "attn_weights",
                        "attn_context",
                    ),
                    (
                        gemv_attn_output_op,
                        f"W_attn_output_decode_{layer_idx}",
                        "attn_context",
                        "attn_output",
                    ),
                    # </grouped query attention>
                ]
                + [
                    (residual_add_op, "x", "attn_output", "x"),
                    (rms_norm_op, "x", f"W_norm2_{layer_idx}", "x_norm"),
                    (
                        gemv_ffn_up_gate_op,
                        f"W_ffn_gate_{layer_idx}",
                        "x_norm",
                        "ffn_gate",
                    ),
                    (gemv_ffn_up_gate_op, f"W_ffn_up_{layer_idx}", "x_norm", "ffn_up"),
                    (silu_ffn_op, "ffn_gate", "ffn_gate"),
                    (eltwise_mul_ffn_op, "ffn_gate", "ffn_up", "ffn_hidden"),
                    (
                        gemv_ffn_down_op,
                        f"W_ffn_down_{layer_idx}",
                        "ffn_hidden",
                        "ffn_output",
                    ),
                    (residual_add_op, "x", "ffn_output", "x"),
                ]
            )
            # </transformer block>
        runlist += [
            (rms_norm_op, "x", "W_final_norm", "x"),
            (gemv_out_head_op, "W_out_head", "x", "logits"),
        ]

        self.decode.fused_op = FusedMLIROperator(
            "fused_op",
            runlist,
            input_args=[  # arguments that change between invocations of the fused kernel and therefore need to be synced on each token
                "x",
                "rope_angles",
            ],
            output_args=["logits"],
            buffer_sizes={
                **{
                    f"keys_cache_{layer_idx}": cache_buffer_size
                    for layer_idx in range(config.n_layers)
                },
                **{
                    f"values_cache_{layer_idx}": cache_buffer_size
                    for layer_idx in range(config.n_layers)
                },
                **{
                    "attn_scores_values": values_buffer_size,
                    "attn_scores_values_transposed": values_buffer_size,
                },
            },
            context=elf_ctx,
        ).compile()

        # Operator patching

        self.decode.fused_elf_data = load_elf(self.decode.fused_op)

        def get_patch_locs(elf_data, magic):
            magic = magic & 0xFFFFFFFF
            return np.where(elf_data == magic)[0]

        keys_patches = {}
        values_patches = {}
        for layer_idx in range(config.n_layers):
            _, keys_cache_offs, _ = self.decode.fused_op.get_layout_for_buffer(
                f"keys_cache_{layer_idx}"
            )
            _, values_cache_offs, _ = self.decode.fused_op.get_layout_for_buffer(
                f"values_cache_{layer_idx}"
            )
            keys_patches.update(
                {
                    int(l): keys_cache_offs
                    for l in get_patch_locs(
                        self.decode.fused_elf_data,
                        (keys_cache_offs + strided_copy_cache_magic * 2),
                    )
                }
            )
            values_patches.update(
                {
                    int(l): values_cache_offs
                    for l in get_patch_locs(
                        self.decode.fused_elf_data,
                        (values_cache_offs + strided_copy_cache_magic * 2),
                    )
                }
            )
        no_offset_patches = {
            int(l): 0
            for l in get_patch_locs(
                self.decode.fused_elf_data, (strided_copy_cache_magic * 2)
            )
        }
        self.decode.fused_patch_locations = {
            **keys_patches,
            **values_patches,
            **no_offset_patches,
        }
        assert len(self.decode.fused_patch_locations) == 4 * config.n_layers + 2

        self.decode.softmax_patch_offsets = get_patch_locs(
            self.decode.fused_elf_data, softmax_magic
        )
        assert len(self.decode.softmax_patch_offsets) == config.n_layers + 1

        self.decode.fused = FusedFullELFCallable(
            self.decode.fused_op, elf_data=self.decode.fused_elf_data
        )

        # Operator static buffers (weights, LUTs)

        for layer_idx in range(config.n_layers):
            self.decode.fused.get_buffer(f"W_norm1_{layer_idx}").torch_view()[:] = (
                config.weights[
                    f"model.layers.{layer_idx}.input_layernorm.weight"
                ].flatten()
            )
            self.decode.fused.get_buffer(f"W_attn_query_{layer_idx}").torch_view()[
                :
            ] = config.weights[
                f"model.layers.{layer_idx}.self_attn.q_proj.weight"
            ].flatten()
            self.decode.fused.get_buffer(f"W_attn_key_{layer_idx}").torch_view()[:] = (
                config.weights[
                    f"model.layers.{layer_idx}.self_attn.k_proj.weight"
                ].flatten()
            )
            self.decode.fused.get_buffer(f"W_attn_value_{layer_idx}").torch_view()[
                :
            ] = config.weights[
                f"model.layers.{layer_idx}.self_attn.v_proj.weight"
            ].flatten()
            self.decode.fused.get_buffer(
                f"W_attn_output_decode_{layer_idx}"
            ).torch_view()[:] = config.weights[
                f"model.layers.{layer_idx}.self_attn.o_proj.weight"
            ].flatten()
            self.decode.fused.get_buffer(f"W_norm2_{layer_idx}").torch_view()[:] = (
                config.weights[
                    f"model.layers.{layer_idx}.post_attention_layernorm.weight"
                ].flatten()
            )
            self.decode.fused.get_buffer(f"W_ffn_gate_{layer_idx}").torch_view()[:] = (
                config.weights[
                    f"model.layers.{layer_idx}.mlp.gate_proj.weight"
                ].flatten()
            )
            self.decode.fused.get_buffer(f"W_ffn_up_{layer_idx}").torch_view()[:] = (
                config.weights[f"model.layers.{layer_idx}.mlp.up_proj.weight"].flatten()
            )
            self.decode.fused.get_buffer(f"W_ffn_down_{layer_idx}").torch_view()[:] = (
                config.weights[
                    f"model.layers.{layer_idx}.mlp.down_proj.weight"
                ].flatten()
            )
        scale_factor = 1.0 / math.sqrt(config.head_dim)
        self.decode.fused.get_buffer("attn_scale_factor").fill_(scale_factor)
        self.decode.fused.get_buffer("W_final_norm").torch_view()[:] = config.weights[
            "model.norm.weight"
        ].flatten()
        self.decode.fused.get_buffer("W_out_head").torch_view()[:] = config.weights[
            "model.embed_tokens.weight"
        ].flatten()
        self.decode.fused.input_buffer.to("npu")
        self.decode.fused.scratch_buffer.to("npu")
        self.decode.fused.output_buffer.to("npu")


# Allocate buffers shared with NPU
# ##########################################################################


class AIEPrefillBuffers:
    def __init__(self, prompt_len, emb_dim, hidden_dim, n_heads, n_kv_groups, head_dim):
        self.x = XRTTensor((prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.x_norm = XRTTensor((prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.attn_output = XRTTensor((prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_output = XRTTensor((prompt_len, emb_dim), dtype=ml_dtypes.bfloat16)
        # SwiGLU intermediate buffers
        self.ffn_gate = XRTTensor((prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_up = XRTTensor((prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        self.ffn_hidden = XRTTensor((prompt_len, hidden_dim), dtype=ml_dtypes.bfloat16)
        # Attention buffers: queries and keys serve as both projection output and RoPE input/output
        self.queries = XRTTensor(
            (prompt_len * n_heads, head_dim), dtype=ml_dtypes.bfloat16
        )
        self.keys = XRTTensor(
            (prompt_len * n_kv_groups, head_dim), dtype=ml_dtypes.bfloat16
        )
        self.values = XRTTensor(
            (prompt_len, n_kv_groups * head_dim), dtype=ml_dtypes.bfloat16
        )
        self.rope_angles = XRTTensor((prompt_len, head_dim), dtype=ml_dtypes.bfloat16)
        # Attention score computation buffers (per-head) - parent buffers with subbuffers
        # Parent buffer for all heads' queries: (n_heads, prompt_len, head_dim) stored contiguously
        self.attn_scores_queries_all = XRTTensor(
            (n_heads * prompt_len, head_dim), dtype=ml_dtypes.bfloat16
        )
        self.attn_scores_queries_per_head = [
            XRTSubBuffer.from_parent(
                self.attn_scores_queries_all,
                (prompt_len, head_dim),
                offset_elements=h * prompt_len * head_dim,
                length_elements=prompt_len * head_dim,
                dtype=ml_dtypes.bfloat16,
            )
            for h in range(n_heads)
        ]
        # Parent buffer for all KV groups' keys: (n_kv_groups, head_dim, prompt_len) stored contiguously
        self.attn_scores_keys_all = XRTTensor(
            (n_kv_groups * head_dim, prompt_len), dtype=ml_dtypes.bfloat16
        )
        self.attn_scores_keys_per_kv_group = [
            XRTSubBuffer.from_parent(
                self.attn_scores_keys_all,
                (head_dim, prompt_len),
                offset_elements=g * head_dim * prompt_len,
                length_elements=head_dim * prompt_len,
                dtype=ml_dtypes.bfloat16,
            )
            for g in range(n_kv_groups)
        ]
        # Parent buffer for all heads' scores: (n_heads * prompt_len, prompt_len)
        self.attn_scores = XRTTensor(
            (n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16
        )
        self.attn_scores_per_head = [
            XRTSubBuffer.from_parent(
                self.attn_scores,
                (prompt_len, prompt_len),
                offset_elements=h * prompt_len * prompt_len,
                length_elements=prompt_len * prompt_len,
                dtype=ml_dtypes.bfloat16,
            )
            for h in range(n_heads)
        ]
        # Attention score scaling buffer (pre-initialized with 1/sqrt(head_dim))
        scale_factor = 1.0 / math.sqrt(head_dim)
        self.attn_scale_factor = XRTTensor(
            (n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16
        )
        self.attn_scale_factor.fill_(scale_factor)  # fill_() syncs to device
        # Attention weights buffer (output of softmax)
        self.attn_weights = XRTTensor(
            (n_heads * prompt_len, prompt_len), dtype=ml_dtypes.bfloat16
        )


class AIELlamaBuffers:
    def __init__(self, config, prompt_len, aie_ops):
        # Vector of the current token(s) being processed through the pipeline
        self.prefill = AIEPrefillBuffers(
            prompt_len,
            config.emb_dim,
            config.hidden_dim,
            config.n_heads,
            config.n_kv_groups,
            config.head_dim,
        )

        # Per-layer KV cache buffers on NPU (used by strided copy for transpose and concatenate)
        self.keys_cache = [
            XRTTensor(
                (config.n_kv_groups, prompt_len, config.head_dim),
                dtype=ml_dtypes.bfloat16,
            )
            for _ in range(config.n_layers)
        ]
        self.values_cache = [
            XRTTensor(
                (config.n_kv_groups, prompt_len, config.head_dim),
                dtype=ml_dtypes.bfloat16,
            )
            for _ in range(config.n_layers)
        ]

        # Transformer block layer-wise RMS norm
        self.W_norm1 = []
        self.W_norm2 = []
        # Attention projection weights
        self.W_attn_query_prefill = []
        self.W_attn_key_prefill = []
        self.W_attn_value_prefill = []
        # SwiGLU FFN weights
        self.W_ffn_gate_prefill = []
        self.W_ffn_up_prefill = []
        self.W_ffn_down_prefill = []
        for layer_idx in range(config.n_layers):
            self.W_norm1.append(
                XRTTensor.from_torch(
                    config.weights[f"model.layers.{layer_idx}.input_layernorm.weight"]
                )
            )
            self.W_norm2.append(
                XRTTensor.from_torch(
                    config.weights[
                        f"model.layers.{layer_idx}.post_attention_layernorm.weight"
                    ]
                )
            )
            self.W_attn_query_prefill.append(
                XRTTensor.from_torch(
                    config.weights[
                        f"model.layers.{layer_idx}.self_attn.q_proj.weight"
                    ].T
                )
            )
            self.W_attn_key_prefill.append(
                XRTTensor.from_torch(
                    config.weights[
                        f"model.layers.{layer_idx}.self_attn.k_proj.weight"
                    ].T
                )
            )
            self.W_attn_value_prefill.append(
                XRTTensor.from_torch(
                    config.weights[
                        f"model.layers.{layer_idx}.self_attn.v_proj.weight"
                    ].T
                )
            )
            self.W_ffn_gate_prefill.append(
                XRTTensor.from_torch(
                    config.weights[f"model.layers.{layer_idx}.mlp.gate_proj.weight"].T
                )
            )
            self.W_ffn_up_prefill.append(
                XRTTensor.from_torch(
                    config.weights[f"model.layers.{layer_idx}.mlp.up_proj.weight"].T
                )
            )
            self.W_ffn_down_prefill.append(
                XRTTensor.from_torch(
                    config.weights[f"model.layers.{layer_idx}.mlp.down_proj.weight"].T
                )
            )

        # Final RMS norm weights
        self.W_final_norm = XRTTensor.from_torch(config.weights["model.norm.weight"])
        # Final linear layer (unpadded/unpartitioned, used by GEMV)
        self.W_out_head = XRTTensor.from_torch(
            config.weights["model.embed_tokens.weight"]
        )
        W_out_head_parts = aie_ops.prefill.gemv_out_head_compilable.partition_B(
            # Zero-copy bfloat16 bitcast: view as uint16 (same width) then reinterpret
            # as ml_dtypes.bfloat16. Matches the pattern used in Tensor.from_torch().
            config.weights["model.embed_tokens.weight"]
            .view(torch.uint16)
            .numpy()
            .view(ml_dtypes.bfloat16),
            config.vocab_partitions,
        )
        self.W_out_head_parts = [
            XRTTensor(part, dtype=part.dtype) for part in W_out_head_parts
        ]  # partitioned, padded parts of weight, used by GEMM
        self.prefill.logits = XRTTensor(
            (
                config.vocab_partitions,
                prompt_len,
                config.padded_vocab_size // config.vocab_partitions,
            ),
            dtype=ml_dtypes.bfloat16,
        )
        logits_part_len = prompt_len * (
            config.padded_vocab_size // config.vocab_partitions
        )
        self.prefill.logits_parts = [
            XRTSubBuffer.from_parent(
                self.prefill.logits,
                (
                    prompt_len,
                    config.padded_vocab_size // config.vocab_partitions,
                ),
                offset_elements=i * logits_part_len,
                length_elements=logits_part_len,
                dtype=ml_dtypes.bfloat16,
            )
            for i in range(config.vocab_partitions)
        ]


# Prefill
# ##########################################################################


def grouped_query_attention_forward_prefill(
    config,
    x,
    keys_cache,
    values_cache,
    layer_idx,
    mask=None,
):
    batch, seq_len, emb_dim = x.shape
    num_preceding_tokens = keys_cache.shape[2]

    # Step 1: Linear projections
    aie_ops.prefill.attn_query(
        aie_buffers.prefill.x_norm,
        aie_buffers.W_attn_query_prefill[layer_idx],
        aie_buffers.prefill.queries,
    )
    aie_ops.prefill.attn_key(
        aie_buffers.prefill.x_norm,
        aie_buffers.W_attn_key_prefill[layer_idx],
        aie_buffers.prefill.keys,
    )
    aie_ops.prefill.attn_value(
        aie_buffers.prefill.x_norm,
        aie_buffers.W_attn_value_prefill[layer_idx],
        aie_buffers.prefill.values,
    )

    # Step 2: Apply RoPE to queries and keys
    aie_ops.prefill.rope_queries(
        aie_buffers.prefill.queries,
        aie_buffers.prefill.rope_angles,
        aie_buffers.prefill.queries,
    )
    aie_ops.prefill.rope_keys(
        aie_buffers.prefill.keys,
        aie_buffers.prefill.rope_angles,
        aie_buffers.prefill.keys,
    )

    # Read results from NPU; to_torch() syncs from device internally
    queries = aie_buffers.prefill.queries.to_torch()[: seq_len * config.n_heads, :]
    keys = aie_buffers.prefill.keys.to_torch()[: seq_len * config.n_kv_groups, :]
    values = aie_buffers.prefill.values.to_torch()[
        :seq_len, :
    ]  # (seq_len, n_kv_groups * head_dim)
    queries = queries.view(batch, seq_len, config.n_heads, config.head_dim)
    keys = keys.unsqueeze(0).view(batch, seq_len, config.n_kv_groups, config.head_dim)
    values = values.unsqueeze(0).view(
        batch, seq_len, config.n_kv_groups, config.head_dim
    )  # (batch, seq_len, num_kv_groups, head_dim)

    # Step 3: Transpose for attention computation
    # As a result of the attention projections, the queries, keys and values for each head are interspersed with each other.
    # Transpose so that heads are consecutive for attention computation:
    # (batch, seq_len, num_heads, head_dim) -> (batch, num_heads, seq_len, head_dim)
    queries = queries.transpose(1, 2)  # (batch, num_heads, seq_len, head_dim)
    keys = keys.transpose(1, 2)  # (batch, num_kv_groups, seq_len, head_dim)
    values = values.transpose(1, 2)  # (batch, num_kv_groups, seq_len, head_dim)

    # Step 4: Combine newly computed keys/values for most recent token with cache; these values are used as the updated cache and will be returned to use in the next iteration.
    keys_cache = torch.cat([keys_cache, keys], dim=2)
    values_cache = torch.cat([values_cache, values], dim=2)
    keys = keys_cache
    values = values_cache

    # Step 5: Repeat keys and values for grouped attention -- multiple queries get the same key/value
    group_size = config.n_heads // config.n_kv_groups
    values = values.repeat_interleave(group_size, dim=1)
    context_len = keys.shape[2]

    # Step 6: Compute attention scores using NPU (per-head)
    # (batch, num_heads, seq_len, head_dim) @ (batch, num_heads, head_dim, context_len)
    # -> (batch, num_heads, seq_len, context_len)

    queries_buf = aie_buffers.prefill.attn_scores_queries_all.torch_view().view(
        config.n_heads, -1, config.head_dim
    )
    queries_buf[:, :seq_len, :] = queries.squeeze(0)[
        :, :seq_len, :
    ]  # (num_heads, seq_len, head_dim)
    keys_buf = aie_buffers.prefill.attn_scores_keys_all.torch_view().view(
        config.n_kv_groups, config.head_dim, -1
    )
    keys_buf[:, :, :context_len] = keys.squeeze(0).transpose(
        -2, -1
    )  # (num_kv_groups, head_dim, context_len)

    # Transfer parent buffers to NPU once
    aie_buffers.prefill.attn_scores_queries_all.to("npu")
    aie_buffers.prefill.attn_scores_keys_all.to("npu")
    aie_buffers.prefill.attn_scores.to("npu")

    # Execute GEMM for each head using sub-buffers
    for h in range(config.n_heads):
        kv_group = h // group_size
        aie_ops.prefill.attn_scores(
            aie_buffers.prefill.attn_scores_queries_per_head[h],
            aie_buffers.prefill.attn_scores_keys_per_kv_group[kv_group],
            aie_buffers.prefill.attn_scores_per_head[h],
        )

    # Read back all results at once from parent buffer and apply scaling on NPU
    aie_ops.prefill.attn_scale(
        aie_buffers.prefill.attn_scores,
        aie_buffers.prefill.attn_scale_factor,
        aie_buffers.prefill.attn_scores,
    )
    # Buffer is (n_heads * max_seq_len, max_seq_len), view as (n_heads, max_seq_len, max_seq_len) then slice
    max_seq_len_buf = aie_buffers.prefill.attn_scores.shape[0] // config.n_heads
    scores = (
        aie_buffers.prefill.attn_scores.to_torch()  # to_torch() syncs device→host; torch_view() would not sync and must not be used here
        .view(config.n_heads, max_seq_len_buf, max_seq_len_buf)
        .unsqueeze(0)[:, :, :seq_len, :context_len]
    )

    # Step 7: Apply mask
    # This ensures causality, so that tokens in the future cannot attend to tokens in the past.
    if mask is not None:
        scores = scores.masked_fill(mask, float("-inf"))

    # Step 8: Apply softmax on CPU
    scores = torch.softmax(scores.to(torch.float32), dim=-1).to(torch.bfloat16)
    attention_weights = scores

    # Step 9: Compute attention output
    # (batch, num_heads, seq_len, seq_len) @ (batch, num_heads, seq_len, head_dim)
    # -> (batch, num_heads, seq_len, head_dim)
    context = torch.matmul(attention_weights, values)

    # Step 10: Concatenate heads and project
    # (batch, seq_len, num_heads, head_dim) -> (batch, seq_len, num_heads * head_dim)
    context = context.transpose(1, 2).contiguous().view(batch, seq_len, -1)

    output = torch.nn.functional.linear(
        context, config.weights[f"model.layers.{layer_idx}.self_attn.o_proj.weight"]
    )

    return output, keys_cache, values_cache


def swiglu_ffn_forward_prefill(layer_idx):
    # Step 1: Gate projection
    aie_ops.prefill.ffn_up_gate(
        aie_buffers.prefill.x_norm,
        aie_buffers.W_ffn_gate_prefill[layer_idx],
        aie_buffers.prefill.ffn_gate,
    )

    # Step 2: Up projection
    aie_ops.prefill.ffn_up_gate(
        aie_buffers.prefill.x_norm,
        aie_buffers.W_ffn_up_prefill[layer_idx],
        aie_buffers.prefill.ffn_up,
    )

    # Step 3: Apply SiLU activation
    aie_ops.prefill.ffn_silu(aie_buffers.prefill.ffn_gate, aie_buffers.prefill.ffn_gate)

    # Step 4: Element-wise multiplication
    aie_ops.prefill.eltwise_mul_ffn(
        aie_buffers.prefill.ffn_gate,
        aie_buffers.prefill.ffn_up,
        aie_buffers.prefill.ffn_hidden,
    )

    # Step 5: Down projection
    aie_ops.prefill.ffn_down(
        aie_buffers.prefill.ffn_hidden,
        aie_buffers.W_ffn_down_prefill[layer_idx],
        aie_buffers.prefill.ffn_output,
    )


def transformer_block_forward_prefill(
    config,
    seq_len,
    layer_idx,
    attn_keys_cache,
    attn_values_cache,
    attn_mask,
):
    # Step 1: RMS normalization
    aie_ops.prefill.rms_norm(
        aie_buffers.prefill.x,
        aie_buffers.W_norm1[layer_idx],
        aie_buffers.prefill.x_norm,
    )
    x_norm = aie_buffers.prefill.x_norm.to_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 2: Attention
    attn_output, attn_keys, attn_values = grouped_query_attention_forward_prefill(
        config,
        x_norm,
        attn_keys_cache,
        attn_values_cache,
        layer_idx,
        attn_mask,
    )

    # Step 3: Residual
    aie_buffers.prefill.attn_output.torch_view().unsqueeze(0)[
        0, :seq_len, :
    ] = attn_output
    aie_buffers.prefill.attn_output.to("npu")
    aie_ops.prefill.residual_add(
        aie_buffers.prefill.x, aie_buffers.prefill.attn_output, aie_buffers.prefill.x
    )
    x = aie_buffers.prefill.x.to_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 4: Post-norm
    aie_buffers.prefill.x.torch_view().unsqueeze(0)[0, :seq_len, :] = x
    aie_buffers.prefill.x.to("npu")
    aie_ops.prefill.rms_norm(
        aie_buffers.prefill.x,
        aie_buffers.W_norm2[layer_idx],
        aie_buffers.prefill.x_norm,
    )
    x_norm = aie_buffers.prefill.x_norm.to_torch().unsqueeze(0)[:, :seq_len, :]

    # Step 5: Feed-forward network
    swiglu_ffn_forward_prefill(layer_idx)

    # Step 6: Residual
    aie_ops.prefill.residual_add(
        aie_buffers.prefill.x, aie_buffers.prefill.ffn_output, aie_buffers.prefill.x
    )

    return attn_keys, attn_values


def llama_forward_pass_prefill(config, state):
    batch, seq_len = state.token_ids.shape

    # Step 1: RoPE angles
    num_preceding_tokens = state.attn_keys_caches[0].shape[2]
    angles_slice = config.angles[num_preceding_tokens : num_preceding_tokens + seq_len]
    aie_buffers.prefill.rope_angles.torch_view()[:seq_len, :] = angles_slice
    aie_buffers.prefill.rope_angles.to("npu")

    # Step 2: Token embedding
    tok_emb_weight = config.weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    attn_mask = torch.triu(
        torch.ones(seq_len, seq_len, device=x.device, dtype=torch.bool), diagonal=1
    )
    aie_buffers.prefill.x.torch_view().unsqueeze(0)[0, :seq_len, :] = x
    aie_buffers.prefill.x.to("npu")

    # Step 3: Transformer blocks
    for layer_idx in range(config.n_layers):
        (
            state.attn_keys_caches[layer_idx],
            state.attn_values_caches[layer_idx],
        ) = transformer_block_forward_prefill(
            config,
            seq_len,
            layer_idx,
            state.attn_keys_caches[layer_idx],
            state.attn_values_caches[layer_idx],
            attn_mask=attn_mask,
        )

    # Step 4: Final normalization
    aie_ops.prefill.rms_norm(
        aie_buffers.prefill.x, aie_buffers.W_final_norm, aie_buffers.prefill.x
    )

    # Step 5: Output projection
    for i in range(config.vocab_partitions):
        aie_ops.prefill.out_head(
            aie_buffers.prefill.x,
            aie_buffers.W_out_head_parts[i],
            aie_buffers.prefill.logits_parts[i],
        )
    logits_padded_partitioned = aie_buffers.prefill.logits.to_torch()
    logits_padded = (
        logits_padded_partitioned.transpose(0, 1)
        .contiguous()
        .view(-1, config.padded_vocab_size)
    )
    logits = logits_padded.unsqueeze(0)[:, :seq_len, : config.vocab_size]

    # Step 6: Initialize per-layer NPU cache buffers with current cache state for decode phase
    for layer_idx in range(config.n_layers):
        cache_len = state.attn_keys_caches[layer_idx].shape[2]
        aie_buffers.keys_cache[layer_idx].torch_view()[:, :cache_len, :] = (
            state.attn_keys_caches[layer_idx].squeeze(0)
        )
        aie_buffers.values_cache[layer_idx].torch_view()[:, :cache_len, :] = (
            state.attn_values_caches[layer_idx].squeeze(0)
        )
        aie_buffers.keys_cache[layer_idx].to("npu")
        aie_buffers.values_cache[layer_idx].to("npu")

    return logits, state


# Decode
# ##########################################################################


def patch_fused_decode_operator(ops, config, num_preceding_tokens):
    context_len = num_preceding_tokens + 1

    # Patch fused operator for strided copy cache offset
    output_offset = num_preceding_tokens * config.head_dim
    offset_val = output_offset * 2  # Multiply by 2 for bfloat16 byte offset
    strided_copy_patches = {
        i: (base + offset_val, 0xFFFFFFFF)
        for i, base in ops.fused_patch_locations.items()
    }
    softmax_patches = {i: (context_len, 0xFFFFFFFF) for i in ops.softmax_patch_offsets}
    patches = {**strided_copy_patches, **softmax_patches}
    patched_elf_data = ops.fused_elf_data.copy()
    patch_elf(patched_elf_data, patches)

    ops.fused.reload_elf(patched_elf_data)


def llama_forward_pass_decode(config, state):
    batch, seq_len = state.token_ids.shape
    assert seq_len == 1
    assert state.num_preceding_tokens < max_seq_len

    patch_fused_decode_operator(aie_ops.decode, config, state.num_preceding_tokens)

    # Prefill RoPE angle look-up tables
    angles_slice = config.angles[
        state.num_preceding_tokens : state.num_preceding_tokens + seq_len
    ]
    aie_ops.decode.fused.get_buffer("rope_angles").torch_view()[
        :
    ] = angles_slice.flatten()

    # Token embedding (on CPU)
    tok_emb_weight = config.weights["model.embed_tokens.weight"]
    x = torch.nn.functional.embedding(state.token_ids, tok_emb_weight)
    aie_ops.decode.fused.get_buffer("x").torch_view().view(-1, config.emb_dim)[
        :seq_len, :
    ] = x

    # Fused NPU operator for all of decode (16 transformer blocks + final norm + final linear layer)
    aie_ops.decode.fused.input_buffer.to("cpu")
    aie_ops.decode.fused()  # FusedFullELFCallable.__call__() syncs output_buffer to cpu
    logits = (
        aie_ops.decode.fused.get_buffer("logits")
        .to_torch()
        .view(1, 1, config.vocab_size)
    )

    return logits, state


# Main
# ##########################################################################


def llama_forward_pass(config, state):
    global aie_ops, aie_buffers
    batch, seq_len = state.token_ids.shape
    if seq_len > 1:
        ret = llama_forward_pass_prefill(config, state)
        state.num_preceding_tokens = state.token_ids.shape[1]
        # Pass KV cache data onto fused decode operator
        for layer_idx in range(config.n_layers):
            aie_ops.decode.fused.get_buffer(f"keys_cache_{layer_idx}").torch_view()[
                :
            ] = (aie_buffers.keys_cache[layer_idx].to_torch().flatten())
            aie_ops.decode.fused.get_buffer(f"values_cache_{layer_idx}").torch_view()[
                :
            ] = (aie_buffers.values_cache[layer_idx].to_torch().flatten())
        aie_ops.decode.fused.scratch_buffer.to("cpu")
        return ret
    else:
        ret = llama_forward_pass_decode(config, state)
        state.num_preceding_tokens += 1
        return ret


def main():
    global aie_ops, aie_buffers, max_seq_len
    logging.basicConfig(level=logging.DEBUG)
    args = harness.parse_args()

    assert (
        max_seq_len >= args.prompt_len + args.num_tokens
    ), "max_seq_len must be at least prompt_len + num_tokens"

    prompt = harness.get_prompt(args.prompt_len)

    config, state = harness.init(args.weights_path, args.tokenizer_path, prompt=prompt)

    aie_ops = AIELlamaOperators(config, max_seq_len)
    aie_buffers = AIELlamaBuffers(config, max_seq_len, aie_ops)

    print(prompt, end="", flush=True)
    harness.generate(
        config, state, llama_forward_pass, use_kv_cache=True, num_tokens=args.num_tokens
    )


if __name__ == "__main__":
    main()
