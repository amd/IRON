# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import argparse
import gc
import os

import numpy as np
import torch

from whisper_common import (
    ARTIFACT_ROOT,
    whisper_checkpoint,
    SEQ,
    STATE,
    HEADS,
    HEAD_DIM,
    MLP,
    SCALE,
)
import torch.nn.functional as F
from safetensors import safe_open
import aie.utils as aie_utils

from iron.common.context import AIEContext
from iron.operators.layer_norm.op import LayerNorm
from iron.operators.gemm.op import GEMM
from iron.operators.softmax.op import Softmax
from iron.operators.gelu.op import GELU

# ============================================================
# Whisper-small encoder block configuration
# ============================================================

parser = argparse.ArgumentParser()

parser.add_argument(
    "--block",
    type=int,
    required=True,
)

parser.add_argument(
    "--input-mode",
    choices=(
        "oracle",
        "phoenix",
    ),
    default="oracle",
)

parser.add_argument(
    "--input",
    type=Path,
    default=None,
)

parser.add_argument(
    "--input-key",
    type=str,
    default="output",
    help=("Tensor key to read from --input when " "--input-mode phoenix is used."),
)

parser.add_argument(
    "--output-root",
    type=Path,
    default=None,
    help=("Optional directory for this block's Phoenix artifacts."),
)

parser.add_argument(
    "--reference",
    type=Path,
    required=True,
    help=("FP32 encoder reference artifact used to validate " "this block."),
)

args = parser.parse_args()

BLOCK = args.block

if not 0 <= BLOCK < 12:
    raise ValueError(f"--block must be 0..11, got {BLOCK}")


SAFE = str(whisper_checkpoint())

PROBE_ROOT = ARTIFACT_ROOT

REFERENCE = args.reference.resolve()

OUT_ROOT = (
    args.output_root.resolve()
    if args.output_root is not None
    else (PROBE_ROOT / f"block{BLOCK}-consolidated")
)

OUT_ROOT.mkdir(
    parents=True,
    exist_ok=True,
)

# ============================================================
# Load canonical reference and current block weights
# ============================================================

ref = torch.load(
    REFERENCE,
    map_location="cpu",
    weights_only=True,
)

# ------------------------------------------------------------
# Input selection
# ------------------------------------------------------------

if args.input_mode == "oracle":

    if BLOCK == 0:
        x0 = ref["input"].float().clone()
    else:
        x0 = ref[f"block{BLOCK - 1}.output"].float().clone()

else:
    if args.input is None:
        raise ValueError("--input is required with --input-mode phoenix")

    incoming = torch.load(
        args.input,
        map_location="cpu",
        weights_only=True,
    )

    if args.input_key not in incoming:
        raise KeyError(
            f"Input tensor key {args.input_key!r} " f"not found in {args.input}"
        )

    x0 = incoming[args.input_key].float().clone()


assert x0.shape == (SEQ, STATE)


# ------------------------------------------------------------
# Load this block directly from official safetensors checkpoint.
#
# Matrix weights are rounded through FP16 to preserve the
# exact Phoenix weight preparation used by the validated
# Block-0 pipeline. Biases and LayerNorm parameters stay FP32.
# ------------------------------------------------------------

weights = {}

hf_prefix = f"model.encoder.layers.{BLOCK}."

mapping = {
    "attn_ln.weight": "self_attn_layer_norm.weight",
    "attn_ln.bias": "self_attn_layer_norm.bias",
    "attn.query.weight": "self_attn.q_proj.weight",
    "attn.query.bias": "self_attn.q_proj.bias",
    "attn.key.weight": "self_attn.k_proj.weight",
    "attn.value.weight": "self_attn.v_proj.weight",
    "attn.value.bias": "self_attn.v_proj.bias",
    "attn.out.weight": "self_attn.out_proj.weight",
    "attn.out.bias": "self_attn.out_proj.bias",
    "mlp_ln.weight": "final_layer_norm.weight",
    "mlp_ln.bias": "final_layer_norm.bias",
    "mlp.0.weight": "fc1.weight",
    "mlp.0.bias": "fc1.bias",
    "mlp.2.weight": "fc2.weight",
    "mlp.2.bias": "fc2.bias",
}

with safe_open(
    SAFE,
    framework="pt",
    device="cpu",
) as f:

    available = set(f.keys())

    for local_name, hf_name in mapping.items():

        full_name = hf_prefix + hf_name

        if full_name not in available:
            raise KeyError(f"Missing checkpoint tensor: {full_name}")

        value = f.get_tensor(full_name).cpu()

        # Match the validated Block-0 Phoenix preparation.
        if local_name.endswith(".weight") and value.ndim == 2:
            value = value.to(torch.float16)
        else:
            value = value.float()

        weights[f"encoder.blocks.{BLOCK}.{local_name}"] = value


P = f"encoder.blocks.{BLOCK}."

reference_output = ref[f"block{BLOCK}.output"].float()

tensor_class = aie_utils.DEFAULT_TENSOR_CLASS


# ============================================================
# Helpers
# ============================================================


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


def report(name, actual, expected):
    e = torch.abs(actual - expected)

    rmse = torch.sqrt((e * e).mean()).item()

    cosine = F.cosine_similarity(
        actual.flatten().unsqueeze(0),
        expected.flatten().unsqueeze(0),
    ).item()

    print()
    print(name)
    print(
        "  max error :",
        e.max().item(),
    )
    print(
        "  mean error:",
        e.mean().item(),
    )
    print(
        "  RMSE      :",
        rmse,
    )
    print(
        "  cosine    :",
        cosine,
    )

    return {
        "max": e.max().item(),
        "mean": e.mean().item(),
        "rmse": rmse,
        "cosine": cosine,
    }


def make_context(name):
    root = OUT_ROOT / name

    root.mkdir(
        parents=True,
        exist_ok=True,
    )

    ctx = AIEContext()
    ctx.build_dir = root

    return ctx


# ============================================================
# Compile operator pool
# ============================================================

print("=" * 76)
print(f"PHOENIX WHISPER - CONSOLIDATED ENCODER BLOCK {BLOCK}")
print("=" * 76)

print()
print("Compiling reusable operator pool...")


# ------------------------------------------------------------
# 1. LayerNorm 64 x 768
# ------------------------------------------------------------

ln = LayerNorm(
    size=SEQ * STATE,
    num_aie_columns=1,
    num_channels=1,
    tile_size=STATE,
    context=make_context("ln768"),
)

ln.compile()
ln_fn = ln.get_callable()

print("  LayerNorm 64x768       : PASS")


# ------------------------------------------------------------
# 2. Shared 768 -> 768 GEMM
#    Q, K, V, attention output
# ------------------------------------------------------------

gemm768 = GEMM(
    M=SEQ,
    K=STATE,
    N=STATE,
    num_aie_columns=1,
    tile_m=16,
    tile_k=64,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("gemm768"),
)

gemm768.compile()
gemm768_fn = gemm768.get_callable()

print("  GEMM 64x768x768        : PASS")


# ------------------------------------------------------------
# 3. Shared 64 x 64 x 64 GEMM
#    QK^T and P@V
# ------------------------------------------------------------

gemm64 = GEMM(
    M=SEQ,
    K=HEAD_DIM,
    N=HEAD_DIM,
    num_aie_columns=1,
    tile_m=16,
    tile_k=64,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("gemm64"),
)

gemm64.compile()
gemm64_fn = gemm64.get_callable()

print("  GEMM 64x64x64          : PASS")


# ------------------------------------------------------------
# 4. Softmax 768 x 64
# ------------------------------------------------------------

softmax = Softmax(
    rows=HEADS * SEQ,
    cols=SEQ,
    num_aie_columns=1,
    num_channels=1,
    context=make_context("softmax"),
)

softmax.compile()
softmax_fn = softmax.get_callable()

print("  Softmax 768x64         : PASS")


# ============================================================
# Attention pool complete.
#
# Keep at most four live CachedXRTKernelHandle objects.
# The MLP pool is created only after attention teardown.
# ============================================================

print("  Attention callable pool : 4 live handles")


# ============================================================
# Runtime helpers using already-open contexts
# ============================================================


def run_ln(x):
    inp = tensor_class.from_torch(x.to(torch.bfloat16).flatten().contiguous())

    out = tensor_class(
        (SEQ * STATE,),
        dtype=np.dtype("bfloat16"),
    )

    result = ln_fn(
        inp,
        out,
    )

    y = (
        out.to_torch()
        .float()
        .clone()
        .reshape(
            SEQ,
            STATE,
        )
    )

    del out
    del inp

    return y, result.npu_time


def run_gemm(
    fn,
    a,
    b,
    shape,
):
    A = a.to(torch.bfloat16).contiguous()

    B = b.to(torch.bfloat16).contiguous()

    a_npu = tensor_class.from_torch(A)

    b_npu = tensor_class.from_torch(B)

    c_npu = tensor_class(
        shape,
        dtype=np.dtype("bfloat16"),
    )

    result = fn(
        a_npu,
        b_npu,
        c_npu,
    )

    y = c_npu.to_torch().float().clone()

    del c_npu
    del b_npu
    del a_npu

    return y, result.npu_time


# ============================================================
# Attention LayerNorm
# ============================================================

print()
print("=" * 76)
print("ATTENTION")
print("=" * 76)

attn_bare, t_ln1 = run_ln(x0)

attn_gamma = weights[P + "attn_ln.weight"].float()

attn_beta = weights[P + "attn_ln.bias"].float()

attn_norm = attn_bare * attn_gamma + attn_beta

print(
    "Attention LN time:",
    t_ln1,
)


# ============================================================
# Q / K / V
# ============================================================


def projection(
    name,
    bias_name=None,
):
    w = weights[P + name + ".weight"].float()

    y, t = run_gemm(
        gemm768_fn,
        attn_norm,
        w.T.contiguous(),
        (SEQ, STATE),
    )

    if bias_name is not None:
        y = y + weights[P + bias_name].float()

    return y, t


q, tq = projection(
    "attn.query",
    "attn.query.bias",
)

k, tk = projection(
    "attn.key",
    None,
)

v, tv = projection(
    "attn.value",
    "attn.value.bias",
)

print(
    "Q/K/V times:",
    tq,
    tk,
    tv,
)


# ============================================================
# Attention scores
# ============================================================

qh = split_heads(q)
kh = split_heads(k)
vh = split_heads(v)

scores = torch.empty(
    (HEADS, SEQ, SEQ),
    dtype=torch.float32,
)

score_times = []

for h in range(HEADS):
    raw, t = run_gemm(
        gemm64_fn,
        qh[h],
        kh[h].transpose(0, 1).contiguous(),
        (SEQ, SEQ),
    )

    scores[h] = raw * SCALE

    score_times.append(t)

print(
    "Score GEMM total time:",
    sum(score_times),
)


# ============================================================
# Softmax
# ============================================================

scores_bf16 = scores.to(torch.bfloat16).contiguous()

soft_in = tensor_class.from_torch(scores_bf16.flatten())

soft_out = tensor_class(
    (HEADS * SEQ * SEQ,),
    dtype=np.dtype("bfloat16"),
)

soft_result = softmax_fn(
    soft_in,
    soft_out,
)

probs = (
    soft_out.to_torch()
    .float()
    .clone()
    .reshape(
        HEADS,
        SEQ,
        SEQ,
    )
)

print(
    "Softmax time:",
    soft_result.npu_time,
)

del soft_out
del soft_in


# ============================================================
# P @ V
# ============================================================

attn_heads = []

pv_times = []

for h in range(HEADS):
    y, t = run_gemm(
        gemm64_fn,
        probs[h],
        vh[h],
        (SEQ, HEAD_DIM),
    )

    attn_heads.append(y)
    pv_times.append(t)

attn_heads = torch.stack(
    attn_heads,
    dim=0,
)

attn_merged = merge_heads(attn_heads)

print(
    "P@V total time:",
    sum(pv_times),
)


# ============================================================
# Attention output projection + residual
# ============================================================

out_w = weights[P + "attn.out.weight"].float()

out_bias = weights[P + "attn.out.bias"].float()

attn_gemm, t_out = run_gemm(
    gemm768_fn,
    attn_merged,
    out_w.T.contiguous(),
    (SEQ, STATE),
)

attn_projected = attn_gemm + out_bias

after_attn = x0 + attn_projected

print(
    "Attention output time:",
    t_out,
)


# ============================================================
# Release attention callable pool
# ============================================================

print()
print("Releasing attention callable pool...")

del softmax_fn
del softmax

del gemm64_fn
del gemm64

del gemm768_fn
del gemm768

del ln_fn
del ln

gc.collect()

print("Attention pool released")


# ============================================================
# Create MLP callable pool
#
# Four live handles:
#   LayerNorm
#   FC1
#   GELU
#   FC2
# ============================================================

print()
print("Creating MLP callable pool...")


ln = LayerNorm(
    size=SEQ * STATE,
    num_aie_columns=1,
    num_channels=1,
    tile_size=STATE,
    context=make_context("mlp-ln768"),
)

ln.compile()
ln_fn = ln.get_callable()

print("  MLP LayerNorm          : PASS")


fc1 = GEMM(
    M=SEQ,
    K=STATE,
    N=MLP,
    num_aie_columns=1,
    tile_m=16,
    tile_k=64,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("mlp-fc1"),
)

fc1.compile()
fc1_fn = fc1.get_callable()

print("  MLP FC1               : PASS")


gelu = GELU(
    size=SEQ * MLP,
    num_aie_columns=1,
    num_channels=1,
    tile_size=8192,
    context=make_context("mlp-gelu"),
)

gelu.compile()
gelu_fn = gelu.get_callable()

print("  MLP GELU              : PASS")


fc2 = GEMM(
    M=SEQ,
    K=MLP,
    N=STATE,
    num_aie_columns=1,
    tile_m=16,
    tile_k=64,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("mlp-fc2"),
)

fc2.compile()
fc2_fn = fc2.get_callable()

print("  MLP FC2               : PASS")
print("  MLP callable pool      : 4 live handles")


# ============================================================
# MLP LayerNorm
# ============================================================

print()
print("=" * 76)
print("MLP")
print("=" * 76)

mlp_bare, t_ln2 = run_ln(after_attn)

mlp_gamma = weights[P + "mlp_ln.weight"].float()

mlp_beta = weights[P + "mlp_ln.bias"].float()

mlp_norm = mlp_bare * mlp_gamma + mlp_beta

print(
    "MLP LN time:",
    t_ln2,
)


# ============================================================
# FC1
# ============================================================

fc1_w = weights[P + "mlp.0.weight"].float()

fc1_bias = weights[P + "mlp.0.bias"].float()

mlp_up_gemm, t_fc1 = run_gemm(
    fc1_fn,
    mlp_norm,
    fc1_w.T.contiguous(),
    (SEQ, MLP),
)

mlp_up = mlp_up_gemm + fc1_bias

print(
    "FC1 time:",
    t_fc1,
)


# ============================================================
# GELU
# ============================================================

gelu_in = tensor_class.from_torch(mlp_up.to(torch.bfloat16).flatten().contiguous())

gelu_out = tensor_class(
    (SEQ * MLP,),
    dtype=np.dtype("bfloat16"),
)

gelu_result = gelu_fn(
    gelu_in,
    gelu_out,
)

mlp_act = (
    gelu_out.to_torch()
    .float()
    .clone()
    .reshape(
        SEQ,
        MLP,
    )
)

print(
    "GELU time:",
    gelu_result.npu_time,
)

del gelu_out
del gelu_in


# ============================================================
# FC2 + final residual
# ============================================================

fc2_w = weights[P + "mlp.2.weight"].float()

fc2_bias = weights[P + "mlp.2.bias"].float()

mlp_down_gemm, t_fc2 = run_gemm(
    fc2_fn,
    mlp_act,
    fc2_w.T.contiguous(),
    (SEQ, STATE),
)

mlp_down = mlp_down_gemm + fc2_bias

output = after_attn + mlp_down

print(
    "FC2 time:",
    t_fc2,
)


# ============================================================
# Validation
# ============================================================

print()
print("=" * 76)
print(f"CONSOLIDATED BLOCK{BLOCK} VALIDATION")
print("=" * 76)

oracle_metrics = report(
    f"Phoenix Block{BLOCK} vs FP32 Whisper oracle",
    output,
    reference_output,
)

print()
print(
    "Input mode:",
    args.input_mode,
)

print()
print(
    "Output finite:",
    bool(torch.isfinite(output).all()),
)


# ============================================================
# Save
# ============================================================

torch.save(
    {
        "block": BLOCK,
        "input": x0.cpu(),
        "attn_norm": attn_norm.cpu(),
        "q": q.cpu(),
        "k": k.cpu(),
        "v": v.cpu(),
        "scores": scores.cpu(),
        "probs": probs.cpu(),
        "attn_merged": attn_merged.cpu(),
        "after_attn_residual": after_attn.cpu(),
        "mlp_norm": mlp_norm.cpu(),
        "mlp_up": mlp_up.cpu(),
        "mlp_act": mlp_act.cpu(),
        "mlp_down": mlp_down.cpu(),
        "output": output.cpu(),
        "reference_output": reference_output.cpu(),
        "oracle_metrics": oracle_metrics,
        "input_mode": args.input_mode,
    },
    OUT_ROOT / f"block{BLOCK}-output.pt",
)

print()
print(
    "Saved:",
    OUT_ROOT / f"block{BLOCK}-output.pt",
)


# ============================================================
# Teardown
# ============================================================

del fc2_fn
del fc2

del gelu_fn
del gelu

del fc1_fn
del fc1

del ln_fn
del ln

gc.collect()

print()
print("Normal teardown: PASS")
print("=" * 76)

print(f"PHOENIX BLOCK {BLOCK}: COMPLETE")

print("=" * 76)
