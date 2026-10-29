# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Scratch harness (not shipped): compile each Whisper version device-free
for npu1, on weights drawn at a seed in a real checkpoint's shapes, printing
which succeed and the real traceback for any that don't. Mirrors
../npu1_compile_check.py's pattern (feeds=decode) for the other #256 ports.
"""
import argparse
import sys
import traceback

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.applications.whisper.model import Whisper
from iron.lm.testing import weights_dir

#: ``Whisper.shapes()``'s order: the decode step, a prompt chunk, the encode version.
VERSIONS = ["decode", "prompt", "encode"]

parser = argparse.ArgumentParser()
parser.add_argument("--only", choices=VERSIONS, default=None)
parser.add_argument(
    "directory",
    choices=["whisper-large-v3-turbo", "whisper-small"],
)
parser.add_argument("--seed", type=int, default=0)
args = parser.parse_args()

device = from_name("npu1", n_cols=4)
with aie_utils.set_current_device(device):
    path = weights_dir(args.directory)
    model = Whisper.from_checkpoint(path, random_weights=args.seed)
    print(f"config: {model.config}", flush=True)
    print(f"encoder config: {model.encoder.config}", flush=True)
    decode = None
    for name, shapes in zip(VERSIONS, model.shapes()):
        if args.only is not None and name != args.only:
            continue
        print(f"=== version {name} shapes={shapes} ===", flush=True)
        try:
            version = model.compile(feeds=decode, **shapes)
        except Exception:
            print(f"{name}: FAILED", flush=True)
            traceback.print_exc()
            sys.exit(1)
        if not shapes and version.emit is not None:
            decode = version
        print(f"{name}: OK, full_elf={version.emit is not None}", flush=True)
    print("=== all requested versions compiled on npu1 ===", flush=True)
