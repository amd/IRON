#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Temporary: a runner whose Llama 3.2 1B config.json lacks Meta's
rope_scaling gets a weights directory with it patched in, every other file
a link into the read-only one. Remove once the runner holds Meta's file.
"""

import argparse
import json
import shutil
from pathlib import Path

ROPE_SCALING = {
    "factor": 32.0,
    "high_freq_factor": 4.0,
    "low_freq_factor": 1.0,
    "original_max_position_embeddings": 8192,
    "rope_type": "llama3",
}

parser = argparse.ArgumentParser()
parser.add_argument("--weights", type=Path, required=True)
parser.add_argument("--out", type=Path, required=True)
parser.add_argument("--github-env", type=Path, required=True)
args = parser.parse_args()

config = json.loads((args.weights / "llama3.2-1b" / "config.json").read_text())
if config.get("rope_scaling") != ROPE_SCALING:
    shutil.rmtree(args.out, ignore_errors=True)
    args.out.mkdir(parents=True)
    for entry in args.weights.iterdir():
        if entry.name != "llama3.2-1b":
            (args.out / entry.name).symlink_to(entry)
    llama = args.out / "llama3.2-1b"
    llama.mkdir()
    for entry in (args.weights / "llama3.2-1b").iterdir():
        if entry.name != "config.json":
            (llama / entry.name).symlink_to(entry)
    config["rope_scaling"] = ROPE_SCALING
    (llama / "config.json").write_text(json.dumps(config, indent=2) + "\n")
    with open(args.github_env, "a") as f:
        f.write(f"IRON_EXAMPLE_WEIGHTS_DIR={args.out}\n")
    print(
        f"::warning::{args.weights}/llama3.2-1b/config.json lacks Meta's "
        f"rope_scaling; the tests read a patched copy under {args.out}"
    )
