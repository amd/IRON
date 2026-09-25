# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import torch

from whisper_common import ARTIFACT_ROOT, whisper_checkpoint
import torch.nn.functional as F

ROOT = ARTIFACT_ROOT

REF = torch.load(
    ROOT / "whisper-small-encoder-reference-frontend128.pt",
    map_location="cpu",
    weights_only=True,
)


def metrics(actual, expected):
    error = actual - expected
    ae = error.abs()

    err_norm = torch.linalg.vector_norm(error).item()

    ref_norm = torch.linalg.vector_norm(expected).item()

    return {
        "max": ae.max().item(),
        "mean": ae.mean().item(),
        "rmse": torch.sqrt((error * error).mean()).item(),
        "nrmse": err_norm / ref_norm,
        "cosine": F.cosine_similarity(
            actual.flatten().unsqueeze(0),
            expected.flatten().unsqueeze(0),
        ).item(),
        "ref_norm": ref_norm,
        "err_norm": err_norm,
    }


print("=" * 112)
print("PHOENIX FRONTEND128 -> WHISPER ENCODER ERROR BY DEPTH")
print("=" * 112)

print(
    f"{'block':>5s}"
    f"{'RMSE':>14s}"
    f"{'NRMSE %':>12s}"
    f"{'max_err':>14s}"
    f"{'cosine':>16s}"
    f"{'ref_norm':>14s}"
    f"{'err_norm':>14s}"
    f"{'growth':>12s}"
)

rows = []
previous_rmse = None

for block in range(12):

    path = ROOT / f"block{block}" / f"block{block}-output.pt"

    obj = torch.load(
        path,
        map_location="cpu",
        weights_only=True,
    )

    actual = obj["output"].float()

    expected = REF[f"block{block}.output"].float()

    m = metrics(
        actual,
        expected,
    )

    growth = float("nan") if previous_rmse is None else m["rmse"] / previous_rmse

    print(
        f"{block:5d}"
        f"{m['rmse']:14.8f}"
        f"{100*m['nrmse']:12.4f}"
        f"{m['max']:14.8f}"
        f"{m['cosine']:16.10f}"
        f"{m['ref_norm']:14.4f}"
        f"{m['err_norm']:14.4f}"
        f"{growth:12.5f}"
    )

    rows.append(
        {
            "block": block,
            **m,
            "growth": growth,
        }
    )

    previous_rmse = m["rmse"]


print()
print("=" * 112)
print("SUMMARY")
print("=" * 112)

first = rows[0]
last = rows[-1]

worst_relative = max(
    rows,
    key=lambda r: r["nrmse"],
)

worst_absolute = max(
    rows,
    key=lambda r: r["rmse"],
)

print(
    "Block 0 RMSE       :",
    first["rmse"],
)

print(
    "Block 0 NRMSE %    :",
    100 * first["nrmse"],
)

print(
    "Block 11 RMSE      :",
    last["rmse"],
)

print(
    "Block 11 NRMSE %   :",
    100 * last["nrmse"],
)

print(
    "Block 11 cosine    :",
    last["cosine"],
)

print(
    "RMSE depth ratio   :",
    last["rmse"] / first["rmse"],
)

print(
    "Worst NRMSE block  :",
    worst_relative["block"],
    100 * worst_relative["nrmse"],
)

print(
    "Worst RMSE block   :",
    worst_absolute["block"],
    worst_absolute["rmse"],
)

print("=" * 112)
