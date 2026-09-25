# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import argparse
import gc

import numpy as np
import torch
from safetensors import safe_open

from whisper_common import (
    ARTIFACT_ROOT,
    whisper_checkpoint,
    FRAMES,
    MELS,
    SEQ,
    STATE,
)
import torch.nn.functional as F
import aie.utils as aie_utils

from iron.common.context import AIEContext
from iron.operators.gemm.op import GEMM
from iron.operators.gelu.op import GELU

K1_REAL = 3 * MELS
K1_PAD = 256

K2 = 3 * STATE

# Phoenix GEMM geometry requires this Conv2 configuration's M
# dimension to be a multiple of 128. The logical Conv2 output
# has only 64 rows, so pad M with zero rows and slice them away
# before applying the bias.
CONV2_M_PAD = 128

parser = argparse.ArgumentParser(
    description=("Whisper-small Phoenix frontend validation.")
)

parser.add_argument(
    "--reference",
    type=Path,
    default=None,
    help=("Optional FP32 frontend reference artifact."),
)

parser.add_argument(
    "--output-root",
    type=Path,
    default=None,
    help=("Optional directory for Phoenix frontend artifacts."),
)

args = parser.parse_args()


ROOT = ARTIFACT_ROOT

REFERENCE = (
    args.reference
    if args.reference is not None
    else (ROOT / "whisper-small-frontend-reference-128.pt")
)

CHECKPOINT = whisper_checkpoint()

OUT_ROOT = (
    args.output_root
    if args.output_root is not None
    else (ROOT / "frontend-128-phoenix")
)

OUT_ROOT.mkdir(
    parents=True,
    exist_ok=True,
)


# ============================================================
# Inputs / reference / weights
# ============================================================

ref = torch.load(
    REFERENCE,
    map_location="cpu",
    weights_only=True,
)

with safe_open(
    str(CHECKPOINT),
    framework="pt",
    device="cpu",
) as checkpoint:

    w1 = checkpoint.get_tensor("model.encoder.conv1.weight").cpu()

    b1 = checkpoint.get_tensor("model.encoder.conv1.bias").float().cpu()

    w2 = checkpoint.get_tensor("model.encoder.conv2.weight").cpu()

    b2 = checkpoint.get_tensor("model.encoder.conv2.bias").float().cpu()


mel = ref["mel"].float()


assert mel.shape == (
    1,
    MELS,
    FRAMES,
)

assert w1.shape == (
    STATE,
    MELS,
    3,
)

assert w2.shape == (
    STATE,
    STATE,
    3,
)


tensor_class = aie_utils.DEFAULT_TENSOR_CLASS


def make_context(name):
    p = OUT_ROOT / name

    p.mkdir(
        parents=True,
        exist_ok=True,
    )

    ctx = AIEContext()
    ctx.build_dir = p

    return ctx


def report(name, actual, expected):
    actual = actual.float()
    expected = expected.float()

    error = actual - expected

    ae = error.abs()

    rmse = torch.sqrt((error * error).mean()).item()

    ref_norm = torch.linalg.vector_norm(expected).item()

    err_norm = torch.linalg.vector_norm(error).item()

    nrmse = err_norm / ref_norm if ref_norm != 0 else float("nan")

    cosine = F.cosine_similarity(
        actual.flatten().unsqueeze(0),
        expected.flatten().unsqueeze(0),
    ).item()

    print()
    print(name)

    print(
        "  max error :",
        ae.max().item(),
    )

    print(
        "  mean error:",
        ae.mean().item(),
    )

    print(
        "  RMSE      :",
        rmse,
    )

    print(
        "  NRMSE %   :",
        100 * nrmse,
    )

    print(
        "  cosine    :",
        cosine,
    )

    print(
        "  finite    :",
        bool(torch.isfinite(actual).all()),
    )

    return {
        "max": ae.max().item(),
        "mean": ae.mean().item(),
        "rmse": rmse,
        "nrmse": nrmse,
        "cosine": cosine,
    }


print("=" * 80)
print("WHISPER-SMALL PHOENIX FRONTEND - 128 FRAMES -> 64 SEQ")
print("=" * 80)

print()
print(
    "Mel:",
    tuple(mel.shape),
)

# ============================================================
# PHASE 1
#
# Conv1 via GEMM
# ============================================================

print()
print("=" * 80)
print("PHASE 1 - CONV1")
print("=" * 80)


# Phoenix receives BF16 input.
mel_bf16 = mel.to(torch.bfloat16)


# [1,80,128] -> [128,80]
xt = mel_bf16[0].T


# Time padding.
xpad = F.pad(
    xt.float(),
    (0, 0, 1, 1),
)


# [128,240]
A1_real = torch.stack(
    [
        torch.cat(
            (
                xpad[t],
                xpad[t + 1],
                xpad[t + 2],
            )
        )
        for t in range(FRAMES)
    ]
).to(torch.bfloat16)


assert A1_real.shape == (
    FRAMES,
    K1_REAL,
)


# [768,80,3]
#      ↓
# [3,80,768]
#      ↓
# [240,768]
B1_real = (
    w1.float()
    .permute(2, 1, 0)
    .contiguous()
    .reshape(
        K1_REAL,
        STATE,
    )
    .to(torch.bfloat16)
)


# Pad K 240 -> 256.
A1 = torch.zeros(
    (
        FRAMES,
        K1_PAD,
    ),
    dtype=torch.bfloat16,
)

A1[:, :K1_REAL] = A1_real


B1 = torch.zeros(
    (
        K1_PAD,
        STATE,
    ),
    dtype=torch.bfloat16,
)

B1[:K1_REAL] = B1_real


# Same-BF16 CPU baseline.
conv1_bf16_baseline = (A1.float() @ B1.float()) + b1


conv1 = GEMM(
    M=FRAMES,
    K=K1_PAD,
    N=STATE,
    num_aie_columns=1,
    tile_m=32,
    tile_k=32,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("conv1"),
)


print("Compiling Conv1 GEMM...")
conv1.compile()

conv1_fn = conv1.get_callable()

print("Conv1 context: PASS")


a1_npu = tensor_class.from_torch(A1)

b1_npu = tensor_class.from_torch(B1)

c1_npu = tensor_class(
    (
        FRAMES,
        STATE,
    ),
    dtype=np.dtype("bfloat16"),
)


print("Dispatching Conv1...")

r1 = conv1_fn(
    a1_npu,
    b1_npu,
    c1_npu,
)

print(
    "Conv1 NPU time:",
    r1.npu_time,
)


conv1_gemm = c1_npu.to_torch().float().clone()


conv1_out_tm = conv1_gemm + b1


# [128,768] -> [1,768,128]
conv1_out = conv1_out_tm.T.unsqueeze(0).contiguous()


report(
    "Conv1 Phoenix vs canonical FP32",
    conv1_out,
    ref["conv1"],
)

report(
    "Conv1 Phoenix vs same-BF16 baseline",
    conv1_out_tm,
    conv1_bf16_baseline,
)


# ============================================================
# GELU1
# ============================================================

print()
print("=" * 80)
print("PHASE 1 - GELU1")
print("=" * 80)


gelu1 = GELU(
    size=FRAMES * STATE,
    num_aie_columns=1,
    num_channels=1,
    tile_size=8192,
    context=make_context("gelu1"),
)

print("Compiling GELU1...")
gelu1.compile()

gelu1_fn = gelu1.get_callable()

print("GELU1 context: PASS")


gelu1_in = tensor_class.from_torch(
    conv1_out_tm.to(torch.bfloat16).flatten().contiguous()
)

gelu1_npu = tensor_class(
    (FRAMES * STATE,),
    dtype=np.dtype("bfloat16"),
)


print("Dispatching GELU1...")

rg1 = gelu1_fn(
    gelu1_in,
    gelu1_npu,
)

print(
    "GELU1 NPU time:",
    rg1.npu_time,
)


gelu1_tm = (
    gelu1_npu.to_torch()
    .float()
    .clone()
    .reshape(
        FRAMES,
        STATE,
    )
)


gelu1_out = gelu1_tm.T.unsqueeze(0).contiguous()


report(
    "GELU1 Phoenix vs canonical FP32",
    gelu1_out,
    ref["gelu1"],
)


# Preserve CPU tensor before releasing runtime objects.
gelu1_for_conv2 = gelu1_out.clone()


# ============================================================
# Release phase 1
# ============================================================

del gelu1_npu
del gelu1_in

del c1_npu
del b1_npu
del a1_npu

del gelu1_fn
del gelu1

del conv1_fn
del conv1

gc.collect()

print()
print("Phase 1 runtime objects released")


# ============================================================
# PHASE 2
#
# Conv2 via stride-2 im2col + GEMM
# ============================================================

print()
print("=" * 80)
print("PHASE 2 - CONV2")
print("=" * 80)


# Conv2 receives BF16 GELU1 output.
x2 = gelu1_for_conv2.to(torch.bfloat16)


# [1,768,128] -> [128,768]
xt2 = x2[0].T


xpad2 = F.pad(
    xt2.float(),
    (0, 0, 1, 1),
)


# Output position o corresponds to center input 2*o.
A2 = torch.stack(
    [
        torch.cat(
            (
                xpad2[2 * o],
                xpad2[2 * o + 1],
                xpad2[2 * o + 2],
            )
        )
        for o in range(SEQ)
    ]
).to(torch.bfloat16)


assert A2.shape == (
    SEQ,
    K2,
)


# Physical GEMM input: [128,2304].
#
# Rows 0:64 contain the real stride-2 Conv2 windows.
# Rows 64:128 are zero padding required only by the GEMM
# geometry and are discarded before bias application.
A2_logical = A2

A2 = torch.zeros(
    (
        CONV2_M_PAD,
        K2,
    ),
    dtype=torch.bfloat16,
)

A2[:SEQ] = A2_logical


B2 = (
    w2.float()
    .permute(2, 1, 0)
    .contiguous()
    .reshape(
        K2,
        STATE,
    )
    .to(torch.bfloat16)
)


assert B2.shape == (
    K2,
    STATE,
)


conv2_bf16_baseline = (A2_logical.float() @ B2.float()) + b2


conv2 = GEMM(
    M=CONV2_M_PAD,
    K=K2,
    N=STATE,
    num_aie_columns=1,
    tile_m=32,
    tile_k=64,
    tile_n=64,
    prio_accuracy=True,
    emulate_bf16_mmul_with_bfp16=False,
    context=make_context("conv2"),
)


print("Compiling Conv2 GEMM...")
conv2.compile()

conv2_fn = conv2.get_callable()

print("Conv2 context: PASS")


a2_npu = tensor_class.from_torch(A2)

b2_npu = tensor_class.from_torch(B2)

c2_npu = tensor_class(
    (
        CONV2_M_PAD,
        STATE,
    ),
    dtype=np.dtype("bfloat16"),
)


print("Dispatching Conv2...")

r2 = conv2_fn(
    a2_npu,
    b2_npu,
    c2_npu,
)

print(
    "Conv2 NPU time:",
    r2.npu_time,
)


conv2_gemm_padded = c2_npu.to_torch().float().clone()

assert conv2_gemm_padded.shape == (
    CONV2_M_PAD,
    STATE,
)

# Discard physical zero-padding rows before applying the
# Whisper Conv2 bias.
conv2_gemm = conv2_gemm_padded[:SEQ].contiguous()

conv2_tm = conv2_gemm + b2


conv2_out = conv2_tm.T.unsqueeze(0).contiguous()


report(
    "Conv2 Phoenix accumulated vs canonical FP32",
    conv2_out,
    ref["conv2"],
)

report(
    "Conv2 Phoenix vs same-BF16 accumulated baseline",
    conv2_tm,
    conv2_bf16_baseline,
)


# ============================================================
# GELU2
# ============================================================

print()
print("=" * 80)
print("PHASE 2 - GELU2")
print("=" * 80)


gelu2 = GELU(
    size=SEQ * STATE,
    num_aie_columns=1,
    num_channels=1,
    tile_size=STATE,
    context=make_context("gelu2"),
)

print("Compiling GELU2...")
gelu2.compile()

gelu2_fn = gelu2.get_callable()

print("GELU2 context: PASS")


gelu2_in = tensor_class.from_torch(conv2_tm.to(torch.bfloat16).flatten().contiguous())

gelu2_npu = tensor_class(
    (SEQ * STATE,),
    dtype=np.dtype("bfloat16"),
)


print("Dispatching GELU2...")

rg2 = gelu2_fn(
    gelu2_in,
    gelu2_npu,
)

print(
    "GELU2 NPU time:",
    rg2.npu_time,
)


tokens = (
    gelu2_npu.to_torch()
    .float()
    .clone()
    .reshape(
        SEQ,
        STATE,
    )
)


report(
    "GELU2/tokens Phoenix vs canonical FP32",
    tokens,
    ref["tokens"],
)


# ============================================================
# Positional embedding
#
# Reference already contains:
#
#   block0_input = canonical tokens + positions[:64]
#
# Therefore derive the exact positional tensor from the
# reference rather than opening another checkpoint here.
# ============================================================

positions = ref["block0_input"].float() - ref["tokens"].float()


block0_input = tokens + positions


final_metrics = report(
    "Block0 input Phoenix frontend vs canonical FP32",
    block0_input,
    ref["block0_input"],
)


# ============================================================
# Save integrated frontend output
# ============================================================

OUT = OUT_ROOT / "frontend-output.pt"


torch.save(
    {
        "mel": mel.cpu(),
        "conv1": conv1_out.cpu(),
        "gelu1": gelu1_out.cpu(),
        "conv2": conv2_out.cpu(),
        "tokens": tokens.cpu(),
        "block0_input": block0_input.cpu(),
        "reference_block0_input": ref["block0_input"].cpu(),
        "final_metrics": final_metrics,
    },
    OUT,
)


print()
print("Saved:", OUT)


# ============================================================
# Teardown
# ============================================================

del gelu2_npu
del gelu2_in

del c2_npu
del b2_npu
del a2_npu

del gelu2_fn
del gelu2

del conv2_fn
del conv2

gc.collect()


print()
print("Normal teardown: PASS")

print("=" * 80)
print("PHOENIX WHISPER FRONTEND: COMPLETE")
print("=" * 80)
