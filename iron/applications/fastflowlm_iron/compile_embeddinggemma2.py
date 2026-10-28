#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile every EmbeddingGemma 2 graph version without loading it."""

import argparse
import dataclasses
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.applications.embedding_gemma2 import EmbeddingGemma
from iron.lm import Checkpoint
from iron.lm.checkpoint import weights_file


def compile_model(directory: Path, max_tokens: int) -> None:
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    weights = weights_file(directory)
    config = dataclasses.replace(
        EmbeddingGemma.default_config(weights), max_tokens=max_tokens
    )
    graph = EmbeddingGemma(config, Checkpoint(weights).tree())

    version = graph.compile(**graph.shapes()[0])
    print(version.artifacts.report(f"embedding {max_tokens} rows"), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        type=Path,
        help="directory containing model.safetensors and tokenizer.json",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="largest input length (default: 2048)",
    )
    args = parser.parse_args()
    compile_model(args.directory, args.max_tokens)


if __name__ == "__main__":
    main()
