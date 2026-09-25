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
)
import torch.nn.functional as F
from safetensors import safe_open

import aie.utils as aie_utils

from iron.common.context import AIEContext
from iron.operators.layer_norm.op import LayerNorm

parser = argparse.ArgumentParser(
    description=("Whisper-small Phoenix final encoder LayerNorm validation.")
)

parser.add_argument(
    "--input",
    type=Path,
    default=None,
    help=("Optional Block-11 Phoenix output artifact."),
)

parser.add_argument(
    "--reference",
    type=Path,
    default=None,
    help=("Optional FP32 encoder reference artifact."),
)

parser.add_argument(
    "--output-root",
    type=Path,
    default=None,
    help=("Optional directory for final LayerNorm artifacts."),
)

args = parser.parse_args()


ROOT = ARTIFACT_ROOT

INPUT = (
    args.input.resolve()
    if args.input is not None
    else (ROOT / "block11-consolidated" / "block11-frontend128-accumulated-output.pt")
)

REFERENCE = (
    args.reference.resolve()
    if args.reference is not None
    else (ROOT / "whisper-small-encoder-reference-frontend128.pt")
)

OUT_ROOT = (
    args.output_root.resolve()
    if args.output_root is not None
    else (ROOT / "encoder-final-layernorm-frontend128")
)

OUT_ROOT.mkdir(
    parents=True,
    exist_ok=True,
)

SAFE = str(whisper_checkpoint())


# ============================================================
# Load accumulated Phoenix Block-11 output
# ============================================================

block11 = torch.load(
    INPUT,
    map_location="cpu",
    weights_only=True,
)

x = block11["output"].float()

assert x.shape == (
    SEQ,
    STATE,
)

assert torch.isfinite(x).all()


# ============================================================
# Load canonical encoder reference
# ============================================================

ref = torch.load(
    REFERENCE,
    map_location="cpu",
    weights_only=True,
)

reference_output = ref["encoder_output"].float()


# ============================================================
# Final encoder LayerNorm affine parameters
# ============================================================

with safe_open(
    SAFE,
    framework="pt",
    device="cpu",
) as f:

    gamma = f.get_tensor("model.encoder.layer_norm.weight").float().cpu()

    beta = f.get_tensor("model.encoder.layer_norm.bias").float().cpu()


assert gamma.shape == (STATE,)
assert beta.shape == (STATE,)


# ============================================================
# Phoenix bare LayerNorm
# ============================================================

ctx = AIEContext()

ctx.build_dir = OUT_ROOT / "ln768"

op = LayerNorm(
    size=SEQ * STATE,
    num_aie_columns=1,
    num_channels=1,
    tile_size=STATE,
    context=ctx,
)

print("=" * 80)
print("PHOENIX WHISPER - FRONTEND128 FINAL ENCODER LAYERNORM")
print("=" * 80)

print()
print("Input:")
print(
    "  shape   :",
    tuple(x.shape),
)
print(
    "  min/max :",
    x.min().item(),
    x.max().item(),
)
print(
    "  norm    :",
    torch.linalg.vector_norm(x).item(),
)

print()
print("Compiling...")

op.compile()

print("Compile: PASS")

fn = op.get_callable()

print("Context: PASS")


tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

inp = tensor_class.from_torch(x.to(torch.bfloat16).flatten().contiguous())

out = tensor_class(
    (SEQ * STATE,),
    dtype=np.dtype("bfloat16"),
)

print()
print("Dispatching...")

result = fn(
    inp,
    out,
)

print("Dispatch: PASS")
print(
    "NPU time:",
    result.npu_time,
)


# ============================================================
# Apply learned affine on CPU
# ============================================================

bare = (
    out.to_torch()
    .float()
    .clone()
    .reshape(
        SEQ,
        STATE,
    )
)

encoder_output = bare * gamma + beta


# ============================================================
# Metrics
# ============================================================

error = encoder_output - reference_output

abs_error = error.abs()

rmse = torch.sqrt((error * error).mean()).item()

cosine = F.cosine_similarity(
    encoder_output.flatten().unsqueeze(0),
    reference_output.flatten().unsqueeze(0),
).item()

ref_norm = torch.linalg.vector_norm(reference_output).item()

err_norm = torch.linalg.vector_norm(error).item()

nrmse = err_norm / ref_norm


print()
print("=" * 80)
print("FINAL ENCODER RESULTS")
print("=" * 80)

print(
    "max error :",
    abs_error.max().item(),
)

print(
    "mean error:",
    abs_error.mean().item(),
)

print(
    "RMSE      :",
    rmse,
)

print(
    "cosine    :",
    cosine,
)

print(
    "ref norm  :",
    ref_norm,
)

print(
    "error norm:",
    err_norm,
)

print(
    "NRMSE     :",
    nrmse,
)

print(
    "NRMSE %   :",
    100 * nrmse,
)

print()
print(
    "Phoenix min/max:",
    encoder_output.min().item(),
    encoder_output.max().item(),
)

print(
    "Oracle  min/max:",
    reference_output.min().item(),
    reference_output.max().item(),
)

print(
    "Output finite:",
    bool(torch.isfinite(encoder_output).all()),
)


# ============================================================
# Save
# ============================================================

torch.save(
    {
        "input": x.cpu(),
        "bare_layernorm": bare.cpu(),
        "output": encoder_output.cpu(),
        "reference_output": reference_output.cpu(),
        "max_error": abs_error.max().item(),
        "mean_error": abs_error.mean().item(),
        "rmse": rmse,
        "cosine": cosine,
        "nrmse": nrmse,
    },
    OUT_ROOT / "encoder-output.pt",
)

print()
print(
    "Saved:",
    OUT_ROOT / "encoder-output.pt",
)


# ============================================================
# Teardown
# ============================================================

del out
del inp

del fn
del op

gc.collect()

print()
print("Normal teardown: PASS")
print("=" * 80)
print("PHOENIX WHISPER TRANSFORMER ENCODER: COMPLETE")
print("=" * 80)
