#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Plot four-way prefill means written by the focused pytest benchmark."""

import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

BASE = "FastFlowLM v1.0.8"
NAMES = {
    "stock": BASE,
    "bf16": f"{BASE}\n+ offline dequant",
    "dequant": "IRON BFP16 GEMM",
    "bfp16": "IRON BFP16 GEMM\n+ offline dequant",
}

runs = dict(re.findall(r"^(\S+): mean ([\d.]+)", sys.stdin.read(), re.MULTILINE))
bars = [(NAMES[key], float(runs[key])) for key in NAMES if key in runs]
if len(bars) != len(NAMES):
    missing = ", ".join(key for key in NAMES if key not in runs)
    raise SystemExit(f"missing '<label>: mean <ms>' lines for: {missing}")

labels = [label for label, _ in bars]
values = [value for _, value in bars]

plt.style.use("dark_background")
figure, axis = plt.subplots(figsize=(5.6, 2.9), dpi=220)
axis.barh(
    range(len(values)),
    values,
    color=sns.color_palette("mako", len(values)),
    height=0.66,
    edgecolor="none",
    zorder=3,
)

for index, value in enumerate(values):
    axis.text(
        value + max(values) * 0.02,
        index,
        f"{value:.0f}",
        va="center",
        ha="left",
        fontsize=8,
        fontweight="bold",
    )

axis.set_yticks(range(len(labels)))
axis.set_yticklabels(labels, fontsize=7, linespacing=1.4)
axis.invert_yaxis()
axis.set_xlim(0, max(values) * 1.17)
axis.set_xlabel("prefill mean (ms, 12 runs)", fontsize=7.5)
axis.set_title("Gemma 4 E2B, 261-token prompt", fontsize=8.5, pad=8, loc="left")
axis.tick_params(axis="both", labelsize=7.5, length=0)
axis.grid(axis="x", alpha=0.18, linewidth=0.6)
axis.set_axisbelow(True)
for side in ("top", "right", "left", "bottom"):
    axis.spines[side].set_visible(False)

figure.tight_layout()
output = os.environ.get("IRON_PLOT", "prefill.png")
figure.savefig(output, facecolor="black")
print(f"wrote {output}")
