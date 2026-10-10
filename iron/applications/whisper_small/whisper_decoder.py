# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper-small Phoenix decoder validation."""

import argparse
import gc
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import torch
import torch.nn.functional as F
from safetensors import safe_open

from iron.common.context import AIEContext
from iron.operators.gemm.op import GEMM
from iron.operators.layer_norm.op import LayerNorm

from whisper_common import (
    ARTIFACT_ROOT,
    BLOCKS,
    HEAD_DIM,
    HEADS,
    MLP,
    SCALE,
    STATE,
    whisper_checkpoint,
)

# Decoder validation starts with the controlled four-token
# prefix established by the independent FP32 oracle.
DECODER_SEQ = 4

# Current Phoenix GEMM geometry requires a physical M of 64.
DECODER_PHYSICAL_SEQ = 64

# Controlled encoder validation produces 64 encoder tokens.
ENCODER_SEQ = 64


def make_context(
    build_root: Path,
    name: str,
) -> AIEContext:
    return AIEContext(build_dir=str(build_root / name))


def run_gemm(
    fn,
    a: torch.Tensor,
    b: torch.Tensor,
    shape: tuple[int, ...],
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    a_npu = tensor_class.from_torch(a.to(torch.bfloat16).contiguous())

    b_npu = tensor_class.from_torch(b.to(torch.bfloat16).contiguous())

    c_npu = tensor_class(
        shape,
        dtype=np.dtype("bfloat16"),
    )

    fn(
        a_npu,
        b_npu,
        c_npu,
    )

    result = c_npu.to_torch().float().clone()

    del c_npu
    del b_npu
    del a_npu

    return result


class IncrementalLayerNorm:
    """Persistent bare LayerNorm operator for one decoder row."""

    def __init__(
        self,
        build_root: Path,
    ):
        self.operator = LayerNorm(
            size=STATE,
            num_aie_columns=1,
            num_channels=1,
            tile_size=STATE,
            context=make_context(
                build_root,
                "layernorm",
            ),
        )

        self.operator.compile()

        self.fn = self.operator.get_callable()


def run_layernorm(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    build_root: Path,
    persistent=None,
) -> torch.Tensor:
    """Run bare LayerNorm on Phoenix and apply affine parameters."""

    rows = x.shape[0]

    if x.shape != (
        rows,
        STATE,
    ):
        raise ValueError(f"Unexpected LayerNorm input shape: " f"{tuple(x.shape)}")

    ln = None

    if persistent is None:
        ln = LayerNorm(
            size=rows * STATE,
            num_aie_columns=1,
            num_channels=1,
            tile_size=STATE,
            context=make_context(
                build_root,
                "layernorm",
            ),
        )

        ln.compile()
        fn = ln.get_callable()

    else:
        if rows != 1:
            raise ValueError(
                "Persistent incremental LayerNorm " "requires exactly one row"
            )

        fn = persistent.fn

    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    x_npu = tensor_class.from_torch(x.to(torch.bfloat16).contiguous())

    output_npu = tensor_class(
        (
            rows,
            STATE,
        ),
        dtype=np.dtype("bfloat16"),
    )

    fn(
        x_npu,
        output_npu,
    )

    bare = (
        output_npu.to_torch()
        .float()
        .clone()
        .reshape(
            rows,
            STATE,
        )
    )

    output = bare * weight.float() + bias.float()

    del output_npu
    del x_npu

    if ln is not None:
        del fn
        del ln
        gc.collect()

    return output


def split_heads(
    x: torch.Tensor,
) -> torch.Tensor:
    rows = x.shape[0]

    if x.shape != (
        rows,
        STATE,
    ):
        raise ValueError(f"Unexpected attention shape: " f"{tuple(x.shape)}")

    return (
        x.view(
            rows,
            HEADS,
            HEAD_DIM,
        )
        .transpose(
            0,
            1,
        )
        .contiguous()
    )


def merge_heads(
    x: torch.Tensor,
) -> torch.Tensor:
    if x.ndim != 3 or x.shape[0] != HEADS or x.shape[2] != HEAD_DIM:
        raise ValueError(f"Unexpected head tensor: " f"{tuple(x.shape)}")

    rows = x.shape[1]

    return (
        x.transpose(
            0,
            1,
        )
        .contiguous()
        .view(
            rows,
            STATE,
        )
    )


def pad_rows(
    x: torch.Tensor,
    rows: int = DECODER_PHYSICAL_SEQ,
) -> torch.Tensor:
    if x.shape[0] > rows:
        raise ValueError(f"Cannot pad {x.shape[0]} rows " f"to {rows}")

    output = torch.zeros(
        (
            rows,
            x.shape[1],
        ),
        dtype=x.dtype,
    )

    output[: x.shape[0]] = x

    return output


def load_decoder_block_weights(
    checkpoint: Path,
    block: int,
) -> dict[str, torch.Tensor]:
    prefix = f"model.decoder.layers.{block}."

    names = [
        "self_attn_layer_norm.weight",
        "self_attn_layer_norm.bias",
        "self_attn.q_proj.weight",
        "self_attn.q_proj.bias",
        "self_attn.k_proj.weight",
        "self_attn.v_proj.weight",
        "self_attn.v_proj.bias",
        "self_attn.out_proj.weight",
        "self_attn.out_proj.bias",
        "encoder_attn_layer_norm.weight",
        "encoder_attn_layer_norm.bias",
        "encoder_attn.q_proj.weight",
        "encoder_attn.q_proj.bias",
        "encoder_attn.k_proj.weight",
        "encoder_attn.v_proj.weight",
        "encoder_attn.v_proj.bias",
        "encoder_attn.out_proj.weight",
        "encoder_attn.out_proj.bias",
        "final_layer_norm.weight",
        "final_layer_norm.bias",
        "fc1.weight",
        "fc1.bias",
        "fc2.weight",
        "fc2.bias",
    ]

    with safe_open(
        checkpoint,
        framework="pt",
        device="cpu",
    ) as handle:
        return {
            name: handle.get_tensor(prefix + name).float().clone() for name in names
        }


def pack_incremental_block_weights(
    weights: dict[str, torch.Tensor],
) -> dict[str, torch.Tensor]:
    """Prepack immutable incremental projection weights."""

    keys = (
        "self_attn.q_proj.weight",
        "self_attn.k_proj.weight",
        "self_attn.v_proj.weight",
        "self_attn.out_proj.weight",
        "encoder_attn.q_proj.weight",
        "encoder_attn.out_proj.weight",
        "fc1.weight",
        "fc2.weight",
    )

    return {
        key: (weights[key].transpose(0, 1).contiguous().to(torch.bfloat16).contiguous())
        for key in keys
    }


def run_projection(
    fn,
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor | None,
    logical_rows: int,
    packed_weight: torch.Tensor | None = None,
) -> torch.Tensor:
    """Run a decoder projection with physical row padding."""

    if packed_weight is None:
        gemm_weight = weight.transpose(
            0,
            1,
        ).contiguous()
    else:
        gemm_weight = packed_weight

    physical = run_gemm(
        fn,
        pad_rows(x),
        gemm_weight,
        (
            DECODER_PHYSICAL_SEQ,
            weight.shape[0],
        ),
    )

    output = physical[:logical_rows].clone()

    if bias is not None:
        output += bias

    return output


def run_self_attention(
    x: torch.Tensor,
    weights: dict[str, torch.Tensor],
    build_root: Path,
) -> torch.Tensor:
    """Run causal decoder self-attention."""

    logical_rows = x.shape[0]

    x_norm = run_layernorm(
        x=x,
        weight=weights["self_attn_layer_norm.weight"],
        bias=weights["self_attn_layer_norm.bias"],
        build_root=build_root / "ln",
    )

    projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "projection",
        ),
    )

    projection.compile()
    projection_fn = projection.get_callable()

    q = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.q_proj.weight"],
        weights["self_attn.q_proj.bias"],
        logical_rows,
    )

    k = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.k_proj.weight"],
        None,
        logical_rows,
    )

    v = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.v_proj.weight"],
        weights["self_attn.v_proj.bias"],
        logical_rows,
    )

    del projection_fn
    del projection
    gc.collect()

    qh = split_heads(q)
    kh = split_heads(k)
    vh = split_heads(v)

    score_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=HEAD_DIM,
        N=DECODER_PHYSICAL_SEQ,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "score-gemm",
        ),
    )

    score_gemm.compile()
    score_fn = score_gemm.get_callable()

    scores = torch.empty(
        (
            HEADS,
            logical_rows,
            logical_rows,
        ),
        dtype=torch.float32,
    )

    for head in range(HEADS):
        q_pad = torch.zeros(
            (
                DECODER_PHYSICAL_SEQ,
                HEAD_DIM,
            ),
            dtype=torch.float32,
        )

        k_t_pad = torch.zeros(
            (
                HEAD_DIM,
                DECODER_PHYSICAL_SEQ,
            ),
            dtype=torch.float32,
        )

        q_pad[:logical_rows] = qh[head] * SCALE

        k_t_pad[:, :logical_rows] = (
            kh[head]
            .transpose(
                0,
                1,
            )
            .contiguous()
        )

        physical_scores = run_gemm(
            score_fn,
            q_pad,
            k_t_pad,
            (
                DECODER_PHYSICAL_SEQ,
                DECODER_PHYSICAL_SEQ,
            ),
        )

        scores[head] = physical_scores[
            :logical_rows,
            :logical_rows,
        ]

    del score_fn
    del score_gemm
    gc.collect()

    causal_mask = torch.triu(
        torch.ones(
            logical_rows,
            logical_rows,
            dtype=torch.bool,
        ),
        diagonal=1,
    )

    scores = scores.masked_fill(
        causal_mask,
        torch.finfo(scores.dtype).min,
    )

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = merge_heads(
        torch.matmul(
            probs,
            vh,
        )
    )

    out_projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "out-projection",
        ),
    )

    out_projection.compile()
    out_fn = out_projection.get_callable()

    projected = run_projection(
        out_fn,
        context,
        weights["self_attn.out_proj.weight"],
        weights["self_attn.out_proj.bias"],
        logical_rows,
    )

    del out_fn
    del out_projection
    gc.collect()

    return x + projected


def run_cross_attention(
    x: torch.Tensor,
    encoder: torch.Tensor,
    weights: dict[str, torch.Tensor],
    build_root: Path,
) -> torch.Tensor:
    """Run decoder-to-encoder cross-attention."""

    logical_rows = x.shape[0]

    if encoder.shape != (
        ENCODER_SEQ,
        STATE,
    ):
        raise ValueError("Unexpected encoder shape: " f"{tuple(encoder.shape)}")

    x_norm = run_layernorm(
        x=x,
        weight=weights["encoder_attn_layer_norm.weight"],
        bias=weights["encoder_attn_layer_norm.bias"],
        build_root=build_root / "ln",
    )

    projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "projection",
        ),
    )

    projection.compile()
    projection_fn = projection.get_callable()

    q = run_projection(
        projection_fn,
        x_norm,
        weights["encoder_attn.q_proj.weight"],
        weights["encoder_attn.q_proj.bias"],
        logical_rows,
    )

    k = run_gemm(
        projection_fn,
        encoder,
        weights["encoder_attn.k_proj.weight"]
        .transpose(
            0,
            1,
        )
        .contiguous(),
        (
            ENCODER_SEQ,
            STATE,
        ),
    )

    v = run_gemm(
        projection_fn,
        encoder,
        weights["encoder_attn.v_proj.weight"]
        .transpose(
            0,
            1,
        )
        .contiguous(),
        (
            ENCODER_SEQ,
            STATE,
        ),
    )

    v += weights["encoder_attn.v_proj.bias"]

    del projection_fn
    del projection
    gc.collect()

    qh = split_heads(q)
    kh = split_heads(k)
    vh = split_heads(v)

    score_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=HEAD_DIM,
        N=ENCODER_SEQ,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "score-gemm",
        ),
    )

    score_gemm.compile()
    score_fn = score_gemm.get_callable()

    scores = torch.empty(
        (
            HEADS,
            logical_rows,
            ENCODER_SEQ,
        ),
        dtype=torch.float32,
    )

    for head in range(HEADS):
        q_pad = torch.zeros(
            (
                DECODER_PHYSICAL_SEQ,
                HEAD_DIM,
            ),
            dtype=torch.float32,
        )

        q_pad[:logical_rows] = qh[head] * SCALE

        physical_scores = run_gemm(
            score_fn,
            q_pad,
            kh[head]
            .transpose(
                0,
                1,
            )
            .contiguous(),
            (
                DECODER_PHYSICAL_SEQ,
                ENCODER_SEQ,
            ),
        )

        scores[head] = physical_scores[:logical_rows, :]

    del score_fn
    del score_gemm
    gc.collect()

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = merge_heads(
        torch.matmul(
            probs,
            vh,
        )
    )

    out_projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "out-projection",
        ),
    )

    out_projection.compile()
    out_fn = out_projection.get_callable()

    projected = run_projection(
        out_fn,
        context,
        weights["encoder_attn.out_proj.weight"],
        weights["encoder_attn.out_proj.bias"],
        logical_rows,
    )

    del out_fn
    del out_projection
    gc.collect()

    return x + projected


def run_decoder_mlp(
    x: torch.Tensor,
    weights: dict[str, torch.Tensor],
    build_root: Path,
) -> torch.Tensor:
    """Run the decoder MLP."""

    logical_rows = x.shape[0]

    x_norm = run_layernorm(
        x=x,
        weight=weights["final_layer_norm.weight"],
        bias=weights["final_layer_norm.bias"],
        build_root=build_root / "ln",
    )

    fc1_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=MLP,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "fc1",
        ),
    )

    fc1_gemm.compile()
    fc1_fn = fc1_gemm.get_callable()

    fc1 = run_projection(
        fc1_fn,
        x_norm,
        weights["fc1.weight"],
        weights["fc1.bias"],
        logical_rows,
    )

    del fc1_fn
    del fc1_gemm
    gc.collect()

    # Exact GELU matches the Whisper checkpoint configuration.
    activated = F.gelu(fc1)

    fc2_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=MLP,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "fc2",
        ),
    )

    fc2_gemm.compile()
    fc2_fn = fc2_gemm.get_callable()

    fc2 = run_projection(
        fc2_fn,
        activated,
        weights["fc2.weight"],
        weights["fc2.bias"],
        logical_rows,
    )

    del fc2_fn
    del fc2_gemm
    gc.collect()

    return x + fc2


def run_decoder_block(
    block: int,
    x: torch.Tensor,
    encoder: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> torch.Tensor:
    """Run one Whisper decoder block."""

    if not 0 <= block < BLOCKS:
        raise ValueError(f"Invalid decoder block: {block}")

    weights = load_decoder_block_weights(
        checkpoint,
        block,
    )

    x = run_self_attention(
        x=x,
        weights=weights,
        build_root=(build_root / "self-attention"),
    )

    x = run_cross_attention(
        x=x,
        encoder=encoder,
        weights=weights,
        build_root=(build_root / "cross-attention"),
    )

    x = run_decoder_mlp(
        x=x,
        weights=weights,
        build_root=(build_root / "mlp"),
    )

    del weights
    gc.collect()

    return x


# -----------------------------------------------------------------
# Cached decoder execution
#
# These paths were validated by the D4 Phoenix prefill and
# incremental-cache experiments before promotion into the decoder.
# -----------------------------------------------------------------


def run_self_attention_with_cache(
    x,
    weights,
    build_root,
):
    logical_rows = x.shape[0]

    x_norm = run_layernorm(
        x=x,
        weight=weights["self_attn_layer_norm.weight"],
        bias=weights["self_attn_layer_norm.bias"],
        build_root=(build_root / "ln"),
    )

    projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "projection",
        ),
    )

    projection.compile()
    projection_fn = projection.get_callable()

    q = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.q_proj.weight"],
        weights["self_attn.q_proj.bias"],
        logical_rows,
    )

    k = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.k_proj.weight"],
        None,
        logical_rows,
    )

    v = run_projection(
        projection_fn,
        x_norm,
        weights["self_attn.v_proj.weight"],
        weights["self_attn.v_proj.bias"],
        logical_rows,
    )

    del projection_fn
    del projection
    gc.collect()

    qh = split_heads(q)
    kh = split_heads(k)
    vh = split_heads(v)

    score_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=HEAD_DIM,
        N=DECODER_PHYSICAL_SEQ,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "score-gemm",
        ),
    )

    score_gemm.compile()
    score_fn = score_gemm.get_callable()

    scores = torch.empty(
        (
            HEADS,
            logical_rows,
            logical_rows,
        ),
        dtype=torch.float32,
    )

    for head in range(HEADS):
        q_pad = torch.zeros(
            (
                DECODER_PHYSICAL_SEQ,
                HEAD_DIM,
            ),
            dtype=torch.float32,
        )

        k_t_pad = torch.zeros(
            (
                HEAD_DIM,
                DECODER_PHYSICAL_SEQ,
            ),
            dtype=torch.float32,
        )

        q_pad[:logical_rows] = qh[head] * SCALE

        k_t_pad[
            :,
            :logical_rows,
        ] = (
            kh[head].transpose(0, 1).contiguous()
        )

        physical_scores = run_gemm(
            score_fn,
            q_pad,
            k_t_pad,
            (
                DECODER_PHYSICAL_SEQ,
                DECODER_PHYSICAL_SEQ,
            ),
        )

        scores[head] = physical_scores[
            :logical_rows,
            :logical_rows,
        ]

    del score_fn
    del score_gemm
    gc.collect()

    causal_mask = torch.triu(
        torch.ones(
            logical_rows,
            logical_rows,
            dtype=torch.bool,
        ),
        diagonal=1,
    )

    scores = scores.masked_fill(
        causal_mask,
        torch.finfo(scores.dtype).min,
    )

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = merge_heads(
        torch.matmul(
            probs,
            vh,
        )
    )

    out_projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "out-projection",
        ),
    )

    out_projection.compile()

    out_fn = out_projection.get_callable()

    projected = run_projection(
        out_fn,
        context,
        weights["self_attn.out_proj.weight"],
        weights["self_attn.out_proj.bias"],
        logical_rows,
    )

    del out_fn
    del out_projection
    gc.collect()

    return (
        x + projected,
        kh,
        vh,
    )


def run_cross_attention_with_cache(
    x,
    encoder,
    weights,
    build_root,
):
    logical_rows = x.shape[0]

    if encoder.shape != (
        ENCODER_SEQ,
        STATE,
    ):
        raise ValueError("Unexpected encoder shape: " f"{tuple(encoder.shape)}")

    x_norm = run_layernorm(
        x=x,
        weight=weights["encoder_attn_layer_norm.weight"],
        bias=weights["encoder_attn_layer_norm.bias"],
        build_root=(build_root / "ln"),
    )

    projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "projection",
        ),
    )

    projection.compile()

    projection_fn = projection.get_callable()

    q = run_projection(
        projection_fn,
        x_norm,
        weights["encoder_attn.q_proj.weight"],
        weights["encoder_attn.q_proj.bias"],
        logical_rows,
    )

    k = run_gemm(
        projection_fn,
        encoder,
        weights["encoder_attn.k_proj.weight"].transpose(0, 1).contiguous(),
        (
            ENCODER_SEQ,
            STATE,
        ),
    )

    v = run_gemm(
        projection_fn,
        encoder,
        weights["encoder_attn.v_proj.weight"].transpose(0, 1).contiguous(),
        (
            ENCODER_SEQ,
            STATE,
        ),
    )

    v += weights["encoder_attn.v_proj.bias"]

    del projection_fn
    del projection
    gc.collect()

    qh = split_heads(q)
    kh = split_heads(k)
    vh = split_heads(v)

    score_gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=HEAD_DIM,
        N=ENCODER_SEQ,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "score-gemm",
        ),
    )

    score_gemm.compile()

    score_fn = score_gemm.get_callable()

    scores = torch.empty(
        (
            HEADS,
            logical_rows,
            ENCODER_SEQ,
        ),
        dtype=torch.float32,
    )

    for head in range(HEADS):
        q_pad = torch.zeros(
            (
                DECODER_PHYSICAL_SEQ,
                HEAD_DIM,
            ),
            dtype=torch.float32,
        )

        q_pad[:logical_rows] = qh[head] * SCALE

        physical_scores = run_gemm(
            score_fn,
            q_pad,
            kh[head].transpose(0, 1).contiguous(),
            (
                DECODER_PHYSICAL_SEQ,
                ENCODER_SEQ,
            ),
        )

        scores[head] = physical_scores[:logical_rows, :]

    del score_fn
    del score_gemm
    gc.collect()

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = merge_heads(
        torch.matmul(
            probs,
            vh,
        )
    )

    out_projection = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "out-projection",
        ),
    )

    out_projection.compile()

    out_fn = out_projection.get_callable()

    projected = run_projection(
        out_fn,
        context,
        weights["encoder_attn.out_proj.weight"],
        weights["encoder_attn.out_proj.bias"],
        logical_rows,
    )

    del out_fn
    del out_projection
    gc.collect()

    return (
        x + projected,
        kh,
        vh,
    )


def run_block_with_cache(
    block,
    x,
    encoder,
    checkpoint,
    build_root,
):
    weights = load_decoder_block_weights(
        checkpoint,
        block,
    )

    (
        x,
        self_k,
        self_v,
    ) = run_self_attention_with_cache(
        x=x,
        weights=weights,
        build_root=(build_root / "self-attention"),
    )

    (
        x,
        cross_k,
        cross_v,
    ) = run_cross_attention_with_cache(
        x=x,
        encoder=encoder,
        weights=weights,
        build_root=(build_root / "cross-attention"),
    )

    x = run_decoder_mlp(
        x=x,
        weights=weights,
        build_root=(build_root / "mlp"),
    )

    del weights
    gc.collect()

    return (
        x,
        self_k,
        self_v,
        cross_k,
        cross_v,
    )


def make_projection(
    build_root: Path,
    name: str,
    k: int,
    n: int,
):
    gemm = GEMM(
        M=DECODER_PHYSICAL_SEQ,
        K=k,
        N=n,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            name,
        ),
    )

    gemm.compile()

    return gemm


class IncrementalDecoderKernels:
    """Persistent geometry-based kernels for incremental decoding."""

    def __init__(
        self,
        build_root: Path,
        mlp_dim: int,
    ):
        self.layernorm = IncrementalLayerNorm(build_root / "layernorm")

        self.projection_768_768 = make_projection(
            build_root,
            "gemm-768-768",
            STATE,
            STATE,
        )

        self.projection_768_768_fn = self.projection_768_768.get_callable()

        self.projection_768_mlp = make_projection(
            build_root,
            "gemm-768-mlp",
            STATE,
            mlp_dim,
        )

        self.projection_768_mlp_fn = self.projection_768_mlp.get_callable()

        self.projection_mlp_768 = make_projection(
            build_root,
            "gemm-mlp-768",
            mlp_dim,
            STATE,
        )

        self.projection_mlp_768_fn = self.projection_mlp_768.get_callable()


class DecoderPrefillRuntime:
    """Persistent five-kernel runtime for four-token Whisper decoder prefill."""

    def __init__(
        self,
        build_root,
        block_weights,
    ):
        self.build_root = Path(build_root)

        self.block_weights = block_weights

        self.logical_rows = 4

        self.layernorm = LayerNorm(
            size=4 * STATE,
            num_aie_columns=1,
            num_channels=1,
            tile_size=STATE,
            context=make_context(
                self.build_root,
                "layernorm-4",
            ),
        )

        self.layernorm.compile()

        self.layernorm_fn = self.layernorm.get_callable()

        self.projection = GEMM(
            M=DECODER_PHYSICAL_SEQ,
            K=STATE,
            N=STATE,
            num_aie_columns=1,
            tile_m=16,
            tile_k=64,
            tile_n=64,
            prio_accuracy=True,
            emulate_bf16_mmul_with_bfp16=False,
            context=make_context(
                self.build_root,
                "gemm-768-768",
            ),
        )

        self.projection.compile()

        self.projection_fn = self.projection.get_callable()

        self.score = GEMM(
            M=DECODER_PHYSICAL_SEQ,
            K=HEAD_DIM,
            N=DECODER_PHYSICAL_SEQ,
            num_aie_columns=1,
            tile_m=16,
            tile_k=64,
            tile_n=64,
            prio_accuracy=True,
            emulate_bf16_mmul_with_bfp16=False,
            context=make_context(
                self.build_root,
                "score-64-64",
            ),
        )

        self.score.compile()

        self.score_fn = self.score.get_callable()

        self.fc1 = GEMM(
            M=DECODER_PHYSICAL_SEQ,
            K=STATE,
            N=MLP,
            num_aie_columns=1,
            tile_m=16,
            tile_k=64,
            tile_n=64,
            prio_accuracy=True,
            emulate_bf16_mmul_with_bfp16=False,
            context=make_context(
                self.build_root,
                "gemm-768-3072",
            ),
        )

        self.fc1.compile()

        self.fc1_fn = self.fc1.get_callable()

        self.fc2 = GEMM(
            M=DECODER_PHYSICAL_SEQ,
            K=MLP,
            N=STATE,
            num_aie_columns=1,
            tile_m=16,
            tile_k=64,
            tile_n=64,
            prio_accuracy=True,
            emulate_bf16_mmul_with_bfp16=False,
            context=make_context(
                self.build_root,
                "gemm-3072-768",
            ),
        )

        self.fc2.compile()

        self.fc2_fn = self.fc2.get_callable()

    def layer_norm(
        self,
        x,
        weight,
        bias,
    ):
        tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

        x_npu = tensor_class.from_torch(x.to(torch.bfloat16).contiguous())

        output_npu = tensor_class(
            (
                4,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.layernorm_fn(
            x_npu,
            output_npu,
        )

        bare = (
            output_npu.to_torch()
            .float()
            .clone()
            .reshape(
                4,
                STATE,
            )
        )

        return bare * weight.float() + bias.float()

    def self_attention(
        self,
        x,
        weights,
    ):
        x_norm = self.layer_norm(
            x,
            weights["self_attn_layer_norm.weight"],
            weights["self_attn_layer_norm.bias"],
        )

        q = run_projection(
            self.projection_fn,
            x_norm,
            weights["self_attn.q_proj.weight"],
            weights["self_attn.q_proj.bias"],
            4,
        )

        k = run_projection(
            self.projection_fn,
            x_norm,
            weights["self_attn.k_proj.weight"],
            None,
            4,
        )

        v = run_projection(
            self.projection_fn,
            x_norm,
            weights["self_attn.v_proj.weight"],
            weights["self_attn.v_proj.bias"],
            4,
        )

        qh = split_heads(q)
        kh = split_heads(k)
        vh = split_heads(v)

        scores = torch.empty(
            (
                HEADS,
                4,
                4,
            ),
            dtype=torch.float32,
        )

        for head in range(HEADS):
            q_pad = torch.zeros(
                (
                    DECODER_PHYSICAL_SEQ,
                    HEAD_DIM,
                ),
                dtype=torch.float32,
            )

            k_pad = torch.zeros(
                (
                    HEAD_DIM,
                    DECODER_PHYSICAL_SEQ,
                ),
                dtype=torch.float32,
            )

            q_pad[:4] = qh[head] * SCALE

            k_pad[:, :4] = (
                kh[head]
                .transpose(
                    0,
                    1,
                )
                .contiguous()
            )

            physical = run_gemm(
                self.score_fn,
                q_pad,
                k_pad,
                (
                    DECODER_PHYSICAL_SEQ,
                    DECODER_PHYSICAL_SEQ,
                ),
            )

            scores[head] = physical[
                :4,
                :4,
            ]

        mask = torch.triu(
            torch.ones(
                4,
                4,
                dtype=torch.bool,
            ),
            diagonal=1,
        )

        scores = scores.masked_fill(
            mask,
            torch.finfo(scores.dtype).min,
        )

        probs = torch.softmax(
            scores,
            dim=-1,
            dtype=torch.float32,
        )

        context = merge_heads(
            torch.matmul(
                probs,
                vh,
            )
        )

        projected = run_projection(
            self.projection_fn,
            context,
            weights["self_attn.out_proj.weight"],
            weights["self_attn.out_proj.bias"],
            4,
        )

        return (
            x + projected,
            kh,
            vh,
        )

    def cross_attention(
        self,
        x,
        encoder,
        weights,
    ):
        x_norm = self.layer_norm(
            x,
            weights["encoder_attn_layer_norm.weight"],
            weights["encoder_attn_layer_norm.bias"],
        )

        q = run_projection(
            self.projection_fn,
            x_norm,
            weights["encoder_attn.q_proj.weight"],
            weights["encoder_attn.q_proj.bias"],
            4,
        )

        k = run_gemm(
            self.projection_fn,
            encoder,
            weights["encoder_attn.k_proj.weight"]
            .transpose(
                0,
                1,
            )
            .contiguous(),
            (
                64,
                STATE,
            ),
        )

        v = run_gemm(
            self.projection_fn,
            encoder,
            weights["encoder_attn.v_proj.weight"]
            .transpose(
                0,
                1,
            )
            .contiguous(),
            (
                64,
                STATE,
            ),
        )

        v += weights["encoder_attn.v_proj.bias"]

        qh = split_heads(q)
        kh = split_heads(k)
        vh = split_heads(v)

        scores = torch.empty(
            (
                HEADS,
                4,
                64,
            ),
            dtype=torch.float32,
        )

        for head in range(HEADS):
            q_pad = torch.zeros(
                (
                    DECODER_PHYSICAL_SEQ,
                    HEAD_DIM,
                ),
                dtype=torch.float32,
            )

            q_pad[:4] = qh[head] * SCALE

            physical = run_gemm(
                self.score_fn,
                q_pad,
                kh[head]
                .transpose(
                    0,
                    1,
                )
                .contiguous(),
                (
                    DECODER_PHYSICAL_SEQ,
                    64,
                ),
            )

            scores[head] = physical[:4]

        probs = torch.softmax(
            scores,
            dim=-1,
            dtype=torch.float32,
        )

        context = merge_heads(
            torch.matmul(
                probs,
                vh,
            )
        )

        projected = run_projection(
            self.projection_fn,
            context,
            weights["encoder_attn.out_proj.weight"],
            weights["encoder_attn.out_proj.bias"],
            4,
        )

        return (
            x + projected,
            kh,
            vh,
        )

    def mlp(
        self,
        x,
        weights,
    ):
        x_norm = self.layer_norm(
            x,
            weights["final_layer_norm.weight"],
            weights["final_layer_norm.bias"],
        )

        fc1 = run_projection(
            self.fc1_fn,
            x_norm,
            weights["fc1.weight"],
            weights["fc1.bias"],
            4,
        )

        activated = F.gelu(fc1)

        fc2 = run_projection(
            self.fc2_fn,
            activated,
            weights["fc2.weight"],
            weights["fc2.bias"],
            4,
        )

        return x + fc2

    def run(
        self,
        x,
        encoder,
    ):
        caches = {}

        for block in range(BLOCKS):
            weights = self.block_weights[block]

            (
                x,
                self_k,
                self_v,
            ) = self.self_attention(
                x,
                weights,
            )

            (
                x,
                cross_k,
                cross_v,
            ) = self.cross_attention(
                x,
                encoder,
                weights,
            )

            x = self.mlp(
                x,
                weights,
            )

            caches[block] = {
                "self_k": (self_k.clone()),
                "self_v": (self_v.clone()),
                "cross_k": (cross_k.clone()),
                "cross_v": (cross_v.clone()),
            }

        return (
            x,
            caches,
        )


class IncrementalSelfProjection:
    """Persistent Q/K/V projection for incremental self-attention."""

    def __init__(
        self,
        build_root: Path,
    ):
        self.projection = make_projection(
            build_root,
            "projection",
            STATE,
            STATE,
        )

        self.fn = self.projection.get_callable()


class IncrementalDecoderRuntime:
    """Persistent model state and execution buffers for incremental decoding."""

    PROJECTION_KEYS = (
        "self_attn.q_proj.weight",
        "self_attn.k_proj.weight",
        "self_attn.v_proj.weight",
        "self_attn.out_proj.weight",
        "encoder_attn.q_proj.weight",
        "encoder_attn.out_proj.weight",
        "fc1.weight",
        "fc2.weight",
    )

    def __init__(
        self,
        checkpoint: Path,
        build_root: Path,
    ):
        tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

        self.block_weights = []
        self.packed_block_weights = []
        self.resident_weights = []

        for block in range(BLOCKS):
            weights = load_decoder_block_weights(
                checkpoint,
                block,
            )

            packed = pack_incremental_block_weights(weights)

            resident = {
                key: tensor_class.from_torch(packed[key])
                for key in self.PROJECTION_KEYS
            }

            self.block_weights.append(weights)

            self.packed_block_weights.append(packed)

            self.resident_weights.append(resident)

        self.mlp_dim = self.block_weights[0]["fc1.weight"].shape[0]

        self.kernels = IncrementalDecoderKernels(
            build_root / "kernels",
            self.mlp_dim,
        )

        self.state_input = tensor_class(
            (
                DECODER_PHYSICAL_SEQ,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.state_output = tensor_class(
            (
                DECODER_PHYSICAL_SEQ,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.mlp_input = tensor_class(
            (
                DECODER_PHYSICAL_SEQ,
                self.mlp_dim,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.mlp_output = tensor_class(
            (
                DECODER_PHYSICAL_SEQ,
                self.mlp_dim,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.layernorm_input = tensor_class(
            (
                1,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        self.layernorm_output = tensor_class(
            (
                1,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

    def _overwrite(
        self,
        target,
        value: torch.Tensor,
        *,
        physical_rows: bool = False,
    ):
        if physical_rows:
            value = pad_rows(value)

        value = value.to(torch.bfloat16).contiguous()

        source_bits = value.view(torch.uint16).numpy()

        with target.overwrite() as buffer:
            target_bits = buffer.view(np.uint16)

            target_bits[...] = source_bits

    def layernorm(
        self,
        x: torch.Tensor,
        weight: torch.Tensor,
        bias: torch.Tensor,
    ) -> torch.Tensor:
        self._overwrite(
            self.layernorm_input,
            x,
        )

        self.kernels.layernorm.fn(
            self.layernorm_input,
            self.layernorm_output,
        )

        bare = (
            self.layernorm_output.to_torch()
            .float()
            .clone()
            .reshape(
                1,
                STATE,
            )
        )

        return bare * weight.float() + bias.float()

    def projection(
        self,
        block: int,
        x: torch.Tensor,
        weight_key: str,
        bias: torch.Tensor | None,
    ) -> torch.Tensor:
        weight = self.block_weights[block][weight_key]

        input_dim = weight.shape[1]
        output_dim = weight.shape[0]

        if input_dim == STATE:
            input_buffer = self.state_input

            self._overwrite(
                input_buffer,
                x,
                physical_rows=True,
            )

        elif input_dim == self.mlp_dim:
            input_buffer = self.mlp_input

            self._overwrite(
                input_buffer,
                x,
                physical_rows=True,
            )

        else:
            raise ValueError(
                "Unsupported persistent projection " f"input dimension: {input_dim}"
            )

        if output_dim == STATE:
            output_buffer = self.state_output

        elif output_dim == self.mlp_dim:
            output_buffer = self.mlp_output

        else:
            raise ValueError(
                "Unsupported persistent projection " f"output dimension: {output_dim}"
            )

        if input_dim == STATE and output_dim == STATE:
            fn = self.kernels.projection_768_768_fn

        elif input_dim == STATE and output_dim == self.mlp_dim:
            fn = self.kernels.projection_768_mlp_fn

        elif input_dim == self.mlp_dim and output_dim == STATE:
            fn = self.kernels.projection_mlp_768_fn

        else:
            raise ValueError(
                "Unsupported persistent projection "
                f"geometry: {input_dim}->{output_dim}"
            )

        fn(
            input_buffer,
            self.resident_weights[block][weight_key],
            output_buffer,
        )

        output = output_buffer.to_torch().float().clone()[:1].clone()

        if bias is not None:
            output += bias

        return output

    def run_block(
        self,
        block: int,
        x: torch.Tensor,
        self_k: torch.Tensor,
        self_v: torch.Tensor,
        cross_k: torch.Tensor,
        cross_v: torch.Tensor,
    ) -> tuple[
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
    ]:
        """Run one incremental decoder block on persistent NPU state."""

        weights = self.block_weights[block]

        # -------------------------------------------------
        # Self attention.
        # -------------------------------------------------

        x_norm = self.layernorm(
            x=x,
            weight=weights["self_attn_layer_norm.weight"],
            bias=weights["self_attn_layer_norm.bias"],
        )

        q = self.projection(
            block=block,
            x=x_norm,
            weight_key="self_attn.q_proj.weight",
            bias=weights["self_attn.q_proj.bias"],
        )

        k = self.projection(
            block=block,
            x=x_norm,
            weight_key="self_attn.k_proj.weight",
            bias=None,
        )

        v = self.projection(
            block=block,
            x=x_norm,
            weight_key="self_attn.v_proj.weight",
            bias=weights["self_attn.v_proj.bias"],
        )

        qh = (
            q.view(
                1,
                HEADS,
                HEAD_DIM,
            )
            .transpose(0, 1)
            .contiguous()
            * SCALE
        )

        kh = (
            k.view(
                1,
                HEADS,
                HEAD_DIM,
            )
            .transpose(0, 1)
            .contiguous()
        )

        vh = (
            v.view(
                1,
                HEADS,
                HEAD_DIM,
            )
            .transpose(0, 1)
            .contiguous()
        )

        updated_k = torch.cat(
            [
                self_k,
                kh,
            ],
            dim=1,
        )

        updated_v = torch.cat(
            [
                self_v,
                vh,
            ],
            dim=1,
        )

        scores = torch.matmul(
            qh,
            updated_k.transpose(
                1,
                2,
            ),
        )

        probs = torch.softmax(
            scores,
            dim=-1,
            dtype=torch.float32,
        )

        context = (
            torch.matmul(
                probs,
                updated_v,
            )
            .transpose(0, 1)
            .contiguous()
            .view(
                1,
                STATE,
            )
        )

        projected = self.projection(
            block=block,
            x=context,
            weight_key="self_attn.out_proj.weight",
            bias=weights["self_attn.out_proj.bias"],
        )

        x = x + projected

        # -------------------------------------------------
        # Cross attention.
        # -------------------------------------------------

        x_norm = self.layernorm(
            x=x,
            weight=weights["encoder_attn_layer_norm.weight"],
            bias=weights["encoder_attn_layer_norm.bias"],
        )

        q = self.projection(
            block=block,
            x=x_norm,
            weight_key="encoder_attn.q_proj.weight",
            bias=weights["encoder_attn.q_proj.bias"],
        )

        qh = (
            q.view(
                1,
                HEADS,
                HEAD_DIM,
            )
            .transpose(0, 1)
            .contiguous()
            * SCALE
        )

        scores = torch.matmul(
            qh,
            cross_k.transpose(
                1,
                2,
            ),
        )

        probs = torch.softmax(
            scores,
            dim=-1,
            dtype=torch.float32,
        )

        context = (
            torch.matmul(
                probs,
                cross_v,
            )
            .transpose(0, 1)
            .contiguous()
            .view(
                1,
                STATE,
            )
        )

        projected = self.projection(
            block=block,
            x=context,
            weight_key="encoder_attn.out_proj.weight",
            bias=weights["encoder_attn.out_proj.bias"],
        )

        x = x + projected

        # -------------------------------------------------
        # MLP.
        # -------------------------------------------------

        x_norm = self.layernorm(
            x=x,
            weight=weights["final_layer_norm.weight"],
            bias=weights["final_layer_norm.bias"],
        )

        fc1 = self.projection(
            block=block,
            x=x_norm,
            weight_key="fc1.weight",
            bias=weights["fc1.bias"],
        )

        gelu = F.gelu(fc1)

        fc2 = self.projection(
            block=block,
            x=gelu,
            weight_key="fc2.weight",
            bias=weights["fc2.bias"],
        )

        x = x + fc2

        return (
            x,
            updated_k,
            updated_v,
        )


def run_incremental_self_attention(
    x,
    self_k,
    self_v,
    weights,
    build_root,
    self_projection=None,
    layernorm=None,
    kernels=None,
    packed_weights=None,
):
    if kernels is not None:
        layernorm = kernels.layernorm

    if kernels is not None:
        projection_fn = kernels.projection_768_768_fn
    elif self_projection is not None:
        projection_fn = self_projection.fn
    else:
        projection_fn = None

    x_norm = run_layernorm(
        x=x,
        weight=weights["self_attn_layer_norm.weight"],
        bias=weights["self_attn_layer_norm.bias"],
        build_root=(build_root / "ln"),
        persistent=layernorm,
    )

    projection = None

    if projection_fn is None:
        projection = make_projection(
            build_root,
            "projection",
            STATE,
            STATE,
        )

        fn = projection.get_callable()
    else:
        fn = projection_fn

    q = run_projection(
        fn,
        x_norm,
        weights["self_attn.q_proj.weight"],
        weights["self_attn.q_proj.bias"],
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["self_attn.q_proj.weight"]
        ),
    )

    k = run_projection(
        fn,
        x_norm,
        weights["self_attn.k_proj.weight"],
        None,
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["self_attn.k_proj.weight"]
        ),
    )

    v = run_projection(
        fn,
        x_norm,
        weights["self_attn.v_proj.weight"],
        weights["self_attn.v_proj.bias"],
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["self_attn.v_proj.weight"]
        ),
    )

    if projection is not None:
        del fn
        del projection
        gc.collect()

    qh = (
        q.view(
            1,
            HEADS,
            HEAD_DIM,
        )
        .transpose(0, 1)
        .contiguous()
        * SCALE
    )

    kh = (
        k.view(
            1,
            HEADS,
            HEAD_DIM,
        )
        .transpose(0, 1)
        .contiguous()
    )

    vh = (
        v.view(
            1,
            HEADS,
            HEAD_DIM,
        )
        .transpose(0, 1)
        .contiguous()
    )

    updated_k = torch.cat(
        [self_k, kh],
        dim=1,
    )

    updated_v = torch.cat(
        [self_v, vh],
        dim=1,
    )

    scores = torch.matmul(
        qh,
        updated_k.transpose(1, 2),
    )

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = (
        torch.matmul(
            probs,
            updated_v,
        )
        .transpose(0, 1)
        .contiguous()
        .view(1, STATE)
    )

    out_projection = None

    if kernels is None:
        out_projection = make_projection(
            build_root,
            "out-projection",
            STATE,
            STATE,
        )

        out_fn = out_projection.get_callable()
    else:
        out_fn = kernels.projection_768_768_fn

    projected = run_projection(
        out_fn,
        context,
        weights["self_attn.out_proj.weight"],
        weights["self_attn.out_proj.bias"],
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["self_attn.out_proj.weight"]
        ),
    )

    if out_projection is not None:
        del out_fn
        del out_projection
        gc.collect()

    return (
        x + projected,
        updated_k,
        updated_v,
    )


def run_incremental_cross_attention(
    x,
    cross_k,
    cross_v,
    weights,
    build_root,
    kernels=None,
    packed_weights=None,
):
    x_norm = run_layernorm(
        x=x,
        weight=weights["encoder_attn_layer_norm.weight"],
        bias=weights["encoder_attn_layer_norm.bias"],
        build_root=(build_root / "ln"),
        persistent=(None if kernels is None else kernels.layernorm),
    )

    projection = None

    if kernels is None:
        projection = make_projection(
            build_root,
            "q-projection",
            STATE,
            STATE,
        )

        fn = projection.get_callable()
    else:
        fn = kernels.projection_768_768_fn

    q = run_projection(
        fn,
        x_norm,
        weights["encoder_attn.q_proj.weight"],
        weights["encoder_attn.q_proj.bias"],
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["encoder_attn.q_proj.weight"]
        ),
    )

    if projection is not None:
        del fn
        del projection
        gc.collect()

    qh = (
        q.view(
            1,
            HEADS,
            HEAD_DIM,
        )
        .transpose(0, 1)
        .contiguous()
        * SCALE
    )

    scores = torch.matmul(
        qh,
        cross_k.transpose(1, 2),
    )

    probs = torch.softmax(
        scores,
        dim=-1,
        dtype=torch.float32,
    )

    context = (
        torch.matmul(
            probs,
            cross_v,
        )
        .transpose(0, 1)
        .contiguous()
        .view(1, STATE)
    )

    out_projection = None

    if kernels is None:
        out_projection = make_projection(
            build_root,
            "out-projection",
            STATE,
            STATE,
        )

        out_fn = out_projection.get_callable()
    else:
        out_fn = kernels.projection_768_768_fn

    projected = run_projection(
        out_fn,
        context,
        weights["encoder_attn.out_proj.weight"],
        weights["encoder_attn.out_proj.bias"],
        1,
        packed_weight=(
            None
            if packed_weights is None
            else packed_weights["encoder_attn.out_proj.weight"]
        ),
    )

    if out_projection is not None:
        del out_fn
        del out_projection
        gc.collect()

    return x + projected


def run_incremental_mlp(
    x,
    weights,
    build_root,
    kernels=None,
    packed_weights=None,
):
    x_norm = run_layernorm(
        x=x,
        weight=weights["final_layer_norm.weight"],
        bias=weights["final_layer_norm.bias"],
        build_root=(build_root / "ln"),
        persistent=(None if kernels is None else kernels.layernorm),
    )

    mlp_dim = weights["fc1.weight"].shape[0]

    fc1_gemm = None

    if kernels is None:
        fc1_gemm = make_projection(
            build_root,
            "fc1",
            STATE,
            mlp_dim,
        )

        fc1_fn = fc1_gemm.get_callable()
    else:
        fc1_fn = kernels.projection_768_mlp_fn

    fc1 = run_projection(
        fc1_fn,
        x_norm,
        weights["fc1.weight"],
        weights["fc1.bias"],
        1,
        packed_weight=(
            None if packed_weights is None else packed_weights["fc1.weight"]
        ),
    )

    if fc1_gemm is not None:
        del fc1_fn
        del fc1_gemm
        gc.collect()

    gelu = F.gelu(fc1)

    fc2_gemm = None

    if kernels is None:
        fc2_gemm = make_projection(
            build_root,
            "fc2",
            mlp_dim,
            STATE,
        )

        fc2_fn = fc2_gemm.get_callable()
    else:
        fc2_fn = kernels.projection_mlp_768_fn

    fc2 = run_projection(
        fc2_fn,
        gelu,
        weights["fc2.weight"],
        weights["fc2.bias"],
        1,
        packed_weight=(
            None if packed_weights is None else packed_weights["fc2.weight"]
        ),
    )

    if fc2_gemm is not None:
        del fc2_fn
        del fc2_gemm
        gc.collect()

    return x + fc2


def run_incremental_decoder_block(
    block,
    x,
    self_k,
    self_v,
    cross_k,
    cross_v,
    checkpoint,
    build_root,
    kernels=None,
    weights=None,
    packed_weights=None,
):
    if weights is None:
        weights = load_decoder_block_weights(
            checkpoint,
            block,
        )

    x, updated_k, updated_v = run_incremental_self_attention(
        x=x,
        self_k=self_k,
        self_v=self_v,
        weights=weights,
        build_root=(build_root / "self-attention"),
        kernels=kernels,
        packed_weights=packed_weights,
    )

    x = run_incremental_cross_attention(
        x=x,
        cross_k=cross_k,
        cross_v=cross_v,
        weights=weights,
        build_root=(build_root / "cross-attention"),
        kernels=kernels,
        packed_weights=packed_weights,
    )

    x = run_incremental_mlp(
        x=x,
        weights=weights,
        build_root=(build_root / "mlp"),
        kernels=kernels,
        packed_weights=packed_weights,
    )

    return (
        x,
        updated_k,
        updated_v,
    )


def run_decoder_prefill(
    x: torch.Tensor,
    encoder: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> tuple[
    torch.Tensor,
    dict[int, dict[str, torch.Tensor]],
]:
    """Run all decoder blocks and create their K/V caches."""

    if x.ndim != 2 or x.shape[1] != STATE:
        raise ValueError("Unexpected decoder prefill shape: " f"{tuple(x.shape)}")

    if not 1 <= x.shape[0] <= DECODER_PHYSICAL_SEQ:
        raise ValueError("Unsupported decoder prefill length: " f"{x.shape[0]}")

    if encoder.shape != (
        ENCODER_SEQ,
        STATE,
    ):
        raise ValueError("Unexpected encoder shape: " f"{tuple(encoder.shape)}")

    caches = {}

    for block in range(BLOCKS):
        (
            x,
            self_k,
            self_v,
            cross_k,
            cross_v,
        ) = run_block_with_cache(
            block=block,
            x=x,
            encoder=encoder,
            checkpoint=checkpoint,
            build_root=(build_root / f"block{block}"),
        )

        caches[block] = {
            "self_k": self_k,
            "self_v": self_v,
            "cross_k": cross_k,
            "cross_v": cross_v,
        }

    return x, caches


def run_decoder_incremental(
    x: torch.Tensor,
    caches: dict[
        int,
        dict[str, torch.Tensor],
    ],
    checkpoint: Path,
    build_root: Path,
    kernels=None,
    block_weights=None,
    packed_block_weights=None,
    runtime=None,
) -> tuple[
    torch.Tensor,
    dict[int, dict[str, torch.Tensor]],
]:
    """Run one cached autoregressive decoder step."""

    if x.shape != (
        1,
        STATE,
    ):
        raise ValueError(
            "Incremental decoder expects " "one token, got " f"{tuple(x.shape)}"
        )

    expected_blocks = set(range(BLOCKS))

    if set(caches) != expected_blocks:
        raise ValueError("Decoder cache blocks do not " "match model blocks")

    if block_weights is not None and len(block_weights) != BLOCKS:
        raise ValueError("Preloaded decoder block weights " "do not match model blocks")

    if packed_block_weights is not None and len(packed_block_weights) != BLOCKS:
        raise ValueError("Prepacked decoder block weights " "do not match model blocks")

    updated_caches = {}

    for block in range(BLOCKS):
        cache = caches[block]

        required = {
            "self_k",
            "self_v",
            "cross_k",
            "cross_v",
        }

        missing = required - set(cache)

        if missing:
            raise KeyError(f"Block {block} cache missing: " f"{sorted(missing)}")

        if runtime is None:
            (
                x,
                updated_k,
                updated_v,
            ) = run_incremental_decoder_block(
                block=block,
                x=x,
                self_k=cache["self_k"],
                self_v=cache["self_v"],
                cross_k=cache["cross_k"],
                cross_v=cache["cross_v"],
                checkpoint=checkpoint,
                build_root=(build_root / f"block{block}"),
                kernels=kernels,
                weights=(None if block_weights is None else block_weights[block]),
                packed_weights=(
                    None
                    if packed_block_weights is None
                    else packed_block_weights[block]
                ),
            )
        else:
            (
                x,
                updated_k,
                updated_v,
            ) = runtime.run_block(
                block=block,
                x=x,
                self_k=cache["self_k"],
                self_v=cache["self_v"],
                cross_k=cache["cross_k"],
                cross_v=cache["cross_v"],
            )

        updated_caches[block] = {
            "self_k": updated_k,
            "self_v": updated_v,
            "cross_k": cache["cross_k"],
            "cross_v": cache["cross_v"],
        }

    return x, updated_caches


def load_decoder_final_layernorm(
    checkpoint: Path,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Load the final decoder LayerNorm affine parameters."""

    with safe_open(
        checkpoint,
        framework="pt",
        device="cpu",
    ) as handle:
        weight = handle.get_tensor("model.decoder.layer_norm.weight").float().clone()

        bias = handle.get_tensor("model.decoder.layer_norm.bias").float().clone()

    return weight, bias


def run_decoder_final_layernorm(
    x: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> torch.Tensor:
    """Run the final Whisper decoder LayerNorm."""

    weight, bias = load_decoder_final_layernorm(checkpoint)

    output = run_layernorm(
        x=x,
        weight=weight,
        bias=bias,
        build_root=build_root,
    )

    del bias
    del weight

    gc.collect()

    return output


def load_decoder_embedding(
    checkpoint: Path,
) -> torch.Tensor:
    """Load the tied Whisper decoder token embedding."""

    with safe_open(
        checkpoint,
        framework="pt",
        device="cpu",
    ) as handle:
        embedding = (
            handle.get_tensor("model.decoder.embed_tokens.weight").float().clone()
        )

    return embedding


def load_decoder_position_embedding(
    checkpoint: Path,
) -> torch.Tensor:
    """Load the Whisper decoder positional embedding table."""

    with safe_open(
        checkpoint,
        framework="pt",
        device="cpu",
    ) as handle:
        embedding = (
            handle.get_tensor("model.decoder.embed_positions.weight").float().clone()
        )

    return embedding


def run_decoder_embedding(
    token_ids: torch.Tensor,
    position_offset: int,
    checkpoint: Path,
    token_embedding=None,
    position_embedding=None,
) -> torch.Tensor:
    """Construct Whisper decoder input embeddings."""

    if token_ids.ndim != 1:
        raise ValueError(
            "Decoder token IDs must be rank 1, got " f"{tuple(token_ids.shape)}"
        )

    if token_ids.numel() == 0:
        raise ValueError("Decoder token IDs cannot be empty")

    if position_offset < 0:
        raise ValueError("Decoder position offset cannot be negative")

    owns_token_embedding = token_embedding is None

    owns_position_embedding = position_embedding is None

    if owns_token_embedding:
        token_embedding = load_decoder_embedding(checkpoint)

    if owns_position_embedding:
        position_embedding = load_decoder_position_embedding(checkpoint)

    end_position = position_offset + token_ids.shape[0]

    if end_position > position_embedding.shape[0]:
        raise ValueError(
            "Decoder positions exceed positional "
            "embedding table: "
            f"{position_offset}:{end_position} "
            f"of {position_embedding.shape[0]}"
        )

    if token_ids.min().item() < 0 or token_ids.max().item() >= token_embedding.shape[0]:
        raise ValueError("Decoder token ID outside vocabulary")

    output = (
        token_embedding[token_ids.long()]
        + position_embedding[position_offset:end_position]
    )

    if owns_position_embedding:
        del position_embedding

    if owns_token_embedding:
        del token_embedding

    return output


def run_vocabulary_projection(
    x: torch.Tensor,
    checkpoint: Path,
) -> torch.Tensor:
    """Project decoder hidden states to vocabulary logits in FP32."""

    embedding = load_decoder_embedding(checkpoint)

    if embedding.shape[1] != STATE:
        raise ValueError(
            "Unexpected decoder embedding shape: " f"{tuple(embedding.shape)}"
        )

    logits = torch.matmul(
        x.float(),
        embedding.transpose(
            0,
            1,
        ),
    )

    del embedding

    return logits


def tensor_metrics(
    output: torch.Tensor,
    reference: torch.Tensor,
) -> dict[str, float]:
    """Calculate validation metrics against an FP32 reference."""

    diff = output - reference

    rmse = torch.sqrt(torch.mean(diff.square())).item()

    reference_rms = torch.sqrt(torch.mean(reference.square())).item()

    nrmse = rmse / reference_rms * 100.0

    return {
        "max_diff": (diff.abs().max().item()),
        "mean_diff": (diff.abs().mean().item()),
        "rmse": rmse,
        "nrmse": nrmse,
    }


def print_metrics(
    title: str,
    metrics: dict[str, float],
) -> None:
    print()
    print(title)

    print(
        "  max diff :",
        metrics["max_diff"],
    )

    print(
        "  mean diff:",
        metrics["mean_diff"],
    )

    print(
        "  RMSE     :",
        metrics["rmse"],
    )

    print(
        "  NRMSE %  :",
        metrics["nrmse"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=("Whisper-small Phoenix/NPU1 " "decoder validation.")
    )

    parser.add_argument(
        "--input",
        type=Path,
        required=True,
        help=("Decoder prefix HF oracle artifact."),
    )

    parser.add_argument(
        "--reference",
        type=Path,
        required=True,
        help=("Independent FP32 decoder artifact."),
    )

    parser.add_argument(
        "--d1-reference",
        type=Path,
        default=None,
        help=("Optional previous Phoenix D1.5 " "Block-0 artifact."),
    )

    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help=("Optional decoder artifact directory."),
    )

    parser.add_argument(
        "--all",
        action="store_true",
        help=("Run all 12 decoder blocks. " "Default is Block 0 only."),
    )

    args = parser.parse_args()

    checkpoint = whisper_checkpoint()

    output_root = (
        args.output_root.resolve()
        if args.output_root is not None
        else ARTIFACT_ROOT / "decoder"
    )

    output_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    oracle = torch.load(
        args.input,
        map_location="cpu",
        weights_only=False,
    )

    reference_artifact = torch.load(
        args.reference,
        map_location="cpu",
        weights_only=False,
    )

    required_oracle = {
        "hidden.0",
        "encoder_hidden_states",
    }

    missing_oracle = required_oracle - set(oracle)

    if missing_oracle:
        raise KeyError("Missing oracle keys: " f"{sorted(missing_oracle)}")

    x = oracle["hidden.0"].squeeze(0).float().clone()

    encoder = oracle["encoder_hidden_states"].squeeze(0).float().clone()

    if x.shape != (
        DECODER_SEQ,
        STATE,
    ):
        raise ValueError("Unexpected decoder input shape: " f"{tuple(x.shape)}")

    if encoder.shape != (
        ENCODER_SEQ,
        STATE,
    ):
        raise ValueError("Unexpected encoder shape: " f"{tuple(encoder.shape)}")

    block_count = BLOCKS if args.all else 1

    required_references = {f"block.{block}" for block in range(block_count)}

    missing_references = required_references - set(reference_artifact)

    if missing_references:
        raise KeyError("Missing decoder references: " f"{sorted(missing_references)}")

    print(
        "Decoder input shape:",
        tuple(x.shape),
    )

    print(
        "Encoder input shape:",
        tuple(encoder.shape),
    )

    print(
        "Decoder blocks:",
        block_count,
    )

    outputs = {}
    metrics_by_block = {}

    for block in range(block_count):
        print()
        print("=" * 64)
        print(f"Running Phoenix Decoder " f"Block {block}")
        print("=" * 64)

        x = run_decoder_block(
            block=block,
            x=x,
            encoder=encoder,
            checkpoint=checkpoint,
            build_root=(output_root / f"block{block}"),
        )

        reference = reference_artifact[f"block.{block}"].squeeze(0).float().clone()

        if reference.shape != x.shape:
            raise ValueError(
                f"Unexpected Block {block} "
                "reference shape: "
                f"{tuple(reference.shape)}"
            )

        metrics = tensor_metrics(
            x,
            reference,
        )

        metrics_by_block[block] = metrics

        outputs[f"block.{block}"] = x.clone()

        print_metrics(
            (f"Phoenix Decoder Block " f"{block} vs independent FP32"),
            metrics,
        )

        if block == 0 and args.d1_reference is not None:
            d1_artifact = torch.load(
                args.d1_reference,
                map_location="cpu",
                weights_only=False,
            )

            if "output" not in d1_artifact:
                raise KeyError("D1 artifact has no " "'output' tensor")

            d1_output = d1_artifact["output"].float().clone()

            d1_metrics = tensor_metrics(
                x,
                d1_output,
            )

            print_metrics(
                ("Tracked Block 0 " "vs D1.5"),
                d1_metrics,
            )

    final_hidden = None
    logits = None
    final_metrics = None
    logits_metrics = None
    greedy_tokens = None
    reference_greedy = None

    if args.all:
        if "decoder_output" not in reference_artifact:
            raise KeyError(
                "Independent decoder artifact has no " "'decoder_output' tensor"
            )

        if "logits" not in reference_artifact:
            raise KeyError("Independent decoder artifact has no " "'logits' tensor")

        print()
        print("=" * 64)
        print("COMPLETE DECODER OUTPUT")
        print("=" * 64)

        final_hidden = run_decoder_final_layernorm(
            x=x,
            checkpoint=checkpoint,
            build_root=(output_root / "final-layernorm"),
        )

        final_reference = (
            reference_artifact["decoder_output"].squeeze(0).float().clone()
        )

        if final_reference.shape != final_hidden.shape:
            raise ValueError(
                "Unexpected final decoder "
                "reference shape: "
                f"{tuple(final_reference.shape)}"
            )

        final_metrics = tensor_metrics(
            final_hidden,
            final_reference,
        )

        print_metrics(
            ("Phoenix final decoder output " "vs independent FP32"),
            final_metrics,
        )

        logits = run_vocabulary_projection(
            x=final_hidden,
            checkpoint=checkpoint,
        )

        logits_reference = reference_artifact["logits"].squeeze(0).float().clone()

        if logits_reference.shape != logits.shape:
            raise ValueError(
                "Unexpected logits "
                "reference shape: "
                f"{tuple(logits_reference.shape)}"
            )

        logits_metrics = tensor_metrics(
            logits,
            logits_reference,
        )

        print_metrics(
            ("Phoenix-derived logits " "vs independent FP32"),
            logits_metrics,
        )

        greedy_tokens = logits.argmax(dim=-1)

        reference_greedy = logits_reference.argmax(dim=-1)

        print()
        print("Greedy tokens")

        print(
            "  Phoenix    :",
            greedy_tokens.tolist(),
        )

        print(
            "  independent:",
            reference_greedy.tolist(),
        )

        print(
            "  exact      :",
            torch.equal(
                greedy_tokens,
                reference_greedy,
            ),
        )

    output_path = output_root / (
        "decoder-blocks-output.pt" if args.all else "block0-output.pt"
    )

    saved = {
        "input": (oracle["hidden.0"].squeeze(0).float().clone()),
        "encoder": encoder,
        **outputs,
    }

    if args.all:
        saved["decoder_output"] = final_hidden

        saved["logits"] = logits

        saved["greedy_tokens"] = greedy_tokens

    torch.save(
        saved,
        output_path,
    )

    print()
    print("=" * 64)
    print("DECODER BLOCK SUMMARY")
    print("=" * 64)

    for block in range(block_count):
        metrics = metrics_by_block[block]

        print(
            f"Block {block:2d}: "
            f"NRMSE "
            f"{metrics['nrmse']:.9f}%  "
            f"RMSE "
            f"{metrics['rmse']:.9f}  "
            f"max "
            f"{metrics['max_diff']:.9f}"
        )

    print()
    print(
        "Saved:",
        output_path,
    )


if __name__ == "__main__":
    main()
