#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile every EmbeddingGemma 2 graph version without loading it."""

import argparse
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.lm import Checkpoint, load_weights
from iron.lm.embeddinggemma2.model import (
    EMBEDDINGGEMMA_2,
    ROWS,
    EmbeddingGemma,
    layout,
    text_tensors,
)


def compile_model(directory: Path, max_tokens: int) -> None:
    if max_tokens % ROWS:
        raise ValueError(f"--max-tokens must be a multiple of {ROWS}")

    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    config = EMBEDDINGGEMMA_2
    checkpoint = Checkpoint(directory / "model.safetensors")
    weights = load_weights(
        text_tensors(checkpoint.tensors), layout(config), config.n_layers
    )
    graph = EmbeddingGemma(config, weights, max_tokens)

    shapes_to_compile = graph.shapes()
    for index, shapes in enumerate(shapes_to_compile, 1):
        rows = shapes["x"][0]
        print(f"[{index}/{len(shapes_to_compile)}] compiling {rows} rows", flush=True)
        version = graph.compile(record="disk", verbose=True, **shapes)
        print(f"embedding {rows} rows: {version.artifacts.image}", flush=True)
        print(f"embedding {rows} rows manifest: {version.artifacts.dump()}", flush=True)


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
        default=512,
        help="largest input version; a multiple of 64 (default: 512)",
    )
    args = parser.parse_args()
    compile_model(args.directory, args.max_tokens)


if __name__ == "__main__":
    main()
