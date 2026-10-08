#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 from its checkpoint directory: text in, a unit-length
embedding out, on the NPU; the float32 oracle on demand.

    python -m iron.lm.embeddinggemma2.encoder /path/to/embeddinggemma-2 \\
        --query "What causes the northern lights?" \\
        --document "Charged particles from the sun." "Photosynthesis in plants."
"""

import argparse
import time
from pathlib import Path

import aie.utils as aie_utils
import numpy as np

from iron.common.graph.narrowing import CostTable, JointNarrowing
from iron.lm import Checkpoint, load_weights

from .model import EMBEDDINGGEMMA_2, EmbeddingGemma, layout, text_tensors
from .oracle import PROMPTS, EmbeddingGemmaOracle, tokenizer

# Where `python -m iron.lm.embeddinggemma2.tune` writes its tables, one per device.
COSTS = Path(__file__).parent


class Encoder:
    """The tokenizer, the weights and the NPU encoder of a checkpoint.

    Args:
        directory: Holds `model.safetensors` and `tokenizer.json`.
        max_tokens: The longest prompt, its task prefix included.
        costs: The cost table the designs are narrowed and packed by; None
            leaves them as they resolve.
    """

    def __init__(self, directory, max_tokens: int = 512, costs: Path | None = None):
        directory = Path(directory)
        self.config = EMBEDDINGGEMMA_2
        tensors = Checkpoint(directory / "model.safetensors").tensors
        self.weights = load_weights(
            text_tensors(tensors), layout(self.config), self.config.n_layers
        )
        self.tokenizer = tokenizer(directory / "tokenizer.json")
        self.graph = EmbeddingGemma(self.config, self.weights, max_tokens)
        self.graph.load(JointNarrowing(CostTable(costs)) if costs else None)

    def tokens(self, text: str, task: str) -> list[int]:
        """`text` behind `task`'s prompt (`PROMPTS`), with BOS and EOS."""
        return self.tokenizer.encode(PROMPTS[task] + text).ids

    def __call__(self, text: str, task: str, dims: int = 768) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized."""
        return self.graph.encode(self.tokens(text, task), dims)

    def oracle(self) -> EmbeddingGemmaOracle:
        """The float32 encoder on the host, its weights widened to float32."""
        return EmbeddingGemmaOracle(self.config, self.weights)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("directory", type=Path, help="the checkpoint directory")
    ap.add_argument("--query", required=True)
    ap.add_argument("--document", nargs="+", required=True)
    ap.add_argument("--dims", type=int, choices=EMBEDDINGGEMMA_2.mrl_dims, default=768)
    ap.add_argument(
        "--costs",
        type=Path,
        help="the cost table designs are tuned by (`tune` writes "
        f"costs_<device>.json in {COSTS})",
    )
    args = ap.parse_args()
    encoder = Encoder(args.directory, costs=args.costs)
    try:
        t = time.perf_counter()
        query = encoder(args.query, "query", args.dims)
        print(f"query embedded in {(time.perf_counter() - t) * 1e3:.0f} ms")
        documents = [encoder(d, "document", args.dims) for d in args.document]
    finally:
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()
    scores = np.stack(documents) @ query
    for i in np.argsort(-scores):
        print(f"{scores[i]:.4f}  {args.document[i]}")


if __name__ == "__main__":
    main()
