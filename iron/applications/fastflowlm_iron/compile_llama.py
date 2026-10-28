#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile Llama 3.2 1B's decode and prompt graph versions without loading them."""

import argparse
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.applications.llama import Llama


def compile_model(directory: Path, max_seq_len: int) -> None:
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    graph = Llama.from_checkpoint(directory, max_seq_len=max_seq_len)

    decode = None
    for name, shapes in zip(("decode", "prompt"), graph.shapes(), strict=True):
        version = graph.compile(feeds=decode, **shapes)
        if not shapes and version.emit is not None:
            decode = version
        print(f"{name}: {version.artifacts.image}", flush=True)
        print(f"{name} manifest: {version.artifacts.dump()}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        type=Path,
        help="directory containing config.json, model weights and tokenizer.json",
    )
    parser.add_argument(
        "--max-seq-len",
        type=int,
        default=2048,
        help="longest context served (default: 2048)",
    )
    args = parser.parse_args()
    compile_model(args.directory, args.max_seq_len)


if __name__ == "__main__":
    main()
