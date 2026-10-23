#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile Llama 3.2 1B's decode and prompt graph versions without loading them."""

import argparse
from dataclasses import replace
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.lm.llama3.model import LLAMA_3_2_1B, Llama, Runner


def compile_model(directory: Path, max_seq_len: int) -> None:
    if max_seq_len % LLAMA_3_2_1B.prefill_chunk:
        raise ValueError(
            f"--max-seq-len must be a multiple of {LLAMA_3_2_1B.prefill_chunk}"
        )

    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    config = replace(LLAMA_3_2_1B, max_seq_len=max_seq_len)
    runner = Runner(
        directory / "model.safetensors",
        directory / "tokenizer.model",
        config,
    )
    graph = Llama(config, runner.weights)

    decode = graph.compile(record="disk", verbose=True, **graph.shapes(1))
    print(f"decode: {decode.artifacts.image}", flush=True)
    print(f"decode manifest: {decode.artifacts.dump()}", flush=True)

    feeds = decode if decode.emit is not None else None
    prompt = graph.compile(
        record="disk",
        verbose=True,
        feeds=feeds,
        **graph.shapes(config.prefill_chunk),
    )
    print(f"prompt: {prompt.artifacts.image}", flush=True)
    print(f"prompt manifest: {prompt.artifacts.dump()}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        type=Path,
        help="directory containing model.safetensors and tokenizer.model",
    )
    parser.add_argument(
        "--max-seq-len",
        type=int,
        default=2048,
        help="KV-cache rows; a multiple of 2048 (default: 2048)",
    )
    args = parser.parse_args()
    compile_model(args.directory, args.max_seq_len)


if __name__ == "__main__":
    main()
