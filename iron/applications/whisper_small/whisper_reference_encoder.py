# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import argparse
import os

import torch

from whisper_common import (
    ARTIFACT_ROOT,
    whisper_checkpoint,
    SEQ,
    STATE,
    HEADS,
    HEAD_DIM,
    BLOCKS,
    SCALE,
)
import torch.nn.functional as F
from safetensors import safe_open

SAFE = str(whisper_checkpoint())

parser = argparse.ArgumentParser(
    description=("Whisper-small FP32 transformer encoder reference.")
)

parser.add_argument(
    "--frontend-reference",
    type=Path,
    default=None,
    help=("Optional frontend reference artifact containing " "'block0_input'."),
)

parser.add_argument(
    "--output",
    type=Path,
    default=None,
    help=("Optional encoder reference output artifact."),
)

args = parser.parse_args()


ROOT = ARTIFACT_ROOT

FRONTEND_REFERENCE = (
    args.frontend_reference
    if args.frontend_reference is not None
    else (ROOT / "whisper-small-frontend-reference-128.pt")
)

OUT = (
    args.output
    if args.output is not None
    else (ROOT / "whisper-small-encoder-reference-frontend128.pt")
)

OUT.parent.mkdir(
    parents=True,
    exist_ok=True,
)

frontend = torch.load(
    FRONTEND_REFERENCE,
    map_location="cpu",
    weights_only=True,
)

x = frontend["block0_input"].float().clone()

assert x.shape == (
    SEQ,
    STATE,
)

assert torch.isfinite(x).all()


def split_heads(x):
    return (
        x.reshape(
            SEQ,
            HEADS,
            HEAD_DIM,
        )
        .permute(1, 0, 2)
        .contiguous()
    )


def merge_heads(x):
    return (
        x.permute(1, 0, 2)
        .contiguous()
        .reshape(
            SEQ,
            STATE,
        )
    )


def metrics(actual, expected):
    e = torch.abs(actual - expected)

    return {
        "max": e.max().item(),
        "mean": e.mean().item(),
        "rmse": torch.sqrt((e * e).mean()).item(),
        "cosine": F.cosine_similarity(
            actual.flatten().unsqueeze(0),
            expected.flatten().unsqueeze(0),
        ).item(),
    }


print("=" * 88)
print("WHISPER-SMALL FP32 ENCODER REFERENCE - FRONTEND128 / SEQ64")
print("=" * 88)

print(
    "Frontend reference:",
    FRONTEND_REFERENCE,
)

print(
    "Output reference  :",
    OUT,
)


with safe_open(
    SAFE,
    framework="pt",
    device="cpu",
) as f:

    available = set(f.keys())

    def get(name):
        if name not in available:
            raise KeyError(f"Missing checkpoint tensor: {name}")

        return f.get_tensor(name).float().cpu()

    outputs = {
        "input": x.clone(),
    }

    for block in range(BLOCKS):

        prefix = f"model.encoder.layers.{block}."

        print()
        print("-" * 88)
        print(f"BLOCK {block}")
        print("-" * 88)

        block_input = x

        # ====================================================
        # Attention LayerNorm
        # ====================================================

        attn_norm = F.layer_norm(
            block_input,
            (STATE,),
            weight=get(prefix + "self_attn_layer_norm.weight"),
            bias=get(prefix + "self_attn_layer_norm.bias"),
        )

        # ====================================================
        # Q / K / V
        # ====================================================

        q = F.linear(
            attn_norm,
            get(prefix + "self_attn.q_proj.weight"),
            get(prefix + "self_attn.q_proj.bias"),
        )

        k = F.linear(
            attn_norm,
            get(prefix + "self_attn.k_proj.weight"),
            None,
        )

        v = F.linear(
            attn_norm,
            get(prefix + "self_attn.v_proj.weight"),
            get(prefix + "self_attn.v_proj.bias"),
        )

        qh = split_heads(q)
        kh = split_heads(k)
        vh = split_heads(v)

        # ====================================================
        # Self-attention
        # ====================================================

        scores = (
            torch.matmul(
                qh,
                kh.transpose(-1, -2),
            )
            * SCALE
        )

        probs = torch.softmax(
            scores,
            dim=-1,
        )

        attn_heads = torch.matmul(
            probs,
            vh,
        )

        attn_merged = merge_heads(attn_heads)

        attn_projected = F.linear(
            attn_merged,
            get(prefix + "self_attn.out_proj.weight"),
            get(prefix + "self_attn.out_proj.bias"),
        )

        after_attn = block_input + attn_projected

        # ====================================================
        # MLP
        # ====================================================

        mlp_norm = F.layer_norm(
            after_attn,
            (STATE,),
            weight=get(prefix + "final_layer_norm.weight"),
            bias=get(prefix + "final_layer_norm.bias"),
        )

        mlp_up = F.linear(
            mlp_norm,
            get(prefix + "fc1.weight"),
            get(prefix + "fc1.bias"),
        )

        mlp_act = F.gelu(
            mlp_up,
            approximate="tanh",
        )

        mlp_down = F.linear(
            mlp_act,
            get(prefix + "fc2.weight"),
            get(prefix + "fc2.bias"),
        )

        x = after_attn + mlp_down

        if not torch.isfinite(x).all():
            raise RuntimeError(f"Non-finite output in block {block}")

        outputs[f"block{block}.input"] = block_input.clone()

        outputs[f"block{block}.after_attn"] = after_attn.clone()

        outputs[f"block{block}.output"] = x.clone()

        print(
            "input  min/max:",
            block_input.min().item(),
            block_input.max().item(),
        )

        print(
            "output min/max:",
            x.min().item(),
            x.max().item(),
        )

        print(
            "output norm   :",
            torch.linalg.vector_norm(x).item(),
        )

    # ========================================================
    # Final encoder LayerNorm
    # ========================================================

    final_weight_name = "model.encoder.layer_norm.weight"

    final_bias_name = "model.encoder.layer_norm.bias"

    print()
    print("=" * 88)
    print("FINAL ENCODER LAYERNORM")
    print("=" * 88)

    print(
        "weight key exists:",
        final_weight_name in available,
    )

    print(
        "bias key exists  :",
        final_bias_name in available,
    )

    if final_weight_name in available and final_bias_name in available:
        encoder_output = F.layer_norm(
            x,
            (STATE,),
            weight=get(final_weight_name),
            bias=get(final_bias_name),
        )

        outputs["encoder_output"] = encoder_output.clone()

        print(
            "encoder output min/max:",
            encoder_output.min().item(),
            encoder_output.max().item(),
        )

        print(
            "encoder output norm:",
            torch.linalg.vector_norm(encoder_output).item(),
        )

    else:
        print("Final encoder LayerNorm keys not found.")


# ============================================================
# Frontend-input provenance
# ============================================================

print()
print("=" * 88)
print("FRONTEND128 INPUT")
print("=" * 88)

print(
    "shape:",
    tuple(outputs["input"].shape),
)

print(
    "min/max:",
    outputs["input"].min().item(),
    outputs["input"].max().item(),
)

print(
    "norm:",
    torch.linalg.vector_norm(outputs["input"]).item(),
)

print(
    "finite:",
    bool(torch.isfinite(outputs["input"]).all()),
)


# ============================================================
# Save compact reference
# ============================================================

torch.save(
    outputs,
    OUT,
)

print()
print(
    "Saved:",
    OUT,
)

print(
    "Saved tensors:",
    len(outputs),
)

print()
print("=" * 88)
print("FRONTEND128 12-BLOCK FP32 ENCODER REFERENCE: PASS")
print("=" * 88)
