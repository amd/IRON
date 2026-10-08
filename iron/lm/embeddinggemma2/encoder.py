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

from .audio import model as audio_model
from .audio.oracle import AudioOracle
from .model import COSTS, EMBEDDINGGEMMA_2, EmbeddingGemma, layout, text_tensors
from .multimodal import Multimodal
from .oracle import EmbeddingGemmaOracle, tokenizer, tokens
from .vision import model as vision_model
from .vision.oracle import VisionOracle


class Encoder:
    """The tokenizer, the weights and the NPU encoder of a checkpoint.

    Args:
        directory: Holds `model.safetensors` and `tokenizer.json`.
        max_tokens: The longest prompt, its task prefix included.
        costs: The cost table the designs are narrowed and packed by; None
            leaves them as they resolve.
        towers: Also load the audio and vision towers, so that a call may
            take a clip and an image.
    """

    def __init__(
        self,
        directory,
        max_tokens: int = 512,
        costs: Path | None = None,
        towers: bool = False,
    ):
        directory = Path(directory)
        self.config = EMBEDDINGGEMMA_2
        tensors = Checkpoint(directory / "model.safetensors").tensors
        self.weights = load_weights(
            text_tensors(tensors), layout(self.config), self.config.n_layers
        )
        self.tokenizer = tokenizer(directory / "tokenizer.json")
        if towers:
            A, V = audio_model.AUDIO, vision_model.VISION
            self.audio_weights = load_weights(
                audio_model.audio_tensors(tensors), audio_model.layout(A), A.n_layers
            )
            self.vision_weights = load_weights(
                vision_model.vision_tensors(tensors), vision_model.layout(V), V.n_layers
            )
            self.graph = Multimodal(
                self.config,
                self.weights,
                max_tokens,
                audio_model.AudioTower(A, self.audio_weights),
                vision_model.VisionTower(V, self.vision_weights),
            )
        else:
            self.graph = EmbeddingGemma(self.config, self.weights, max_tokens)
        self.graph.load(JointNarrowing(CostTable(costs)) if costs else None)

    def tokens(
        self, text: str, task: str, audio_tokens: int = 0, image_tokens: int = 0
    ) -> list[int]:
        """`text`'s tokens for `task`, as `oracle.tokens` gives them."""
        return tokens(
            self.tokenizer, self.config, text, task, audio_tokens, image_tokens
        )

    def __call__(
        self, text: str, task: str, dims: int = 768, audio=None, image=None
    ) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized,
        with one mono clip `audio` at 16 kHz and one decoded image `image`,
        `(height, width, 3)` uint8, at their placeholders.
        """
        if audio is None and image is None:
            return self.graph.encode(self.tokens(text, task), dims)
        audio_tokens = 0
        if audio is not None:
            c = audio_model.AUDIO
            audio_tokens = c.tokens(c.frames(np.asarray(audio).size))
        image_tokens = 0
        if image is not None:
            V = vision_model.VISION
            height, width = np.shape(image)[:2]
            out_height, out_width = vision_model.size(height, width, V.image_tokens, V)
            image_tokens = out_height * out_width // (V.pool * V.patch) ** 2
        tokens = self.tokens(text, task, audio_tokens, image_tokens)
        return self.graph.encode(tokens, dims, audio, image)

    def oracle(self) -> EmbeddingGemmaOracle:
        """The float32 encoder on the host, its weights widened to float32."""
        return EmbeddingGemmaOracle(self.config, self.weights)

    def tower_oracles(self) -> tuple[AudioOracle, VisionOracle]:
        """The float32 towers on the host, of an encoder loaded with `towers`."""
        return (
            AudioOracle(audio_model.AUDIO, self.audio_weights),
            VisionOracle(vision_model.VISION, self.vision_weights),
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("directory", type=Path, help="the checkpoint directory")
    ap.add_argument("--query", required=True)
    ap.add_argument("--document", nargs="+", required=True)
    ap.add_argument("--dims", type=int, choices=EMBEDDINGGEMMA_2.mrl_dims, default=768)
    ap.add_argument(
        "--costs",
        type=Path,
        help=f"the cost table designs are tuned by (`tune` writes {COSTS})",
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
