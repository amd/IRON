#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 on the NPU: the text encoder as one graph
(``EmbeddingGemma``), and over text, audio and an image (``Multimodal``),
the towers' soft tokens in their placeholders' places. Text goes in behind
its task's prefix and a unit-length embedding comes out:

    python -m iron.applications.embedding_gemma2.model /path/to/embeddinggemma-2 \\
        --query "What causes the northern lights?" \\
        --document "Charged particles from the sun." "Photosynthesis in plants."
"""

import argparse
import dataclasses
import math
import time
from pathlib import Path
from types import SimpleNamespace
from typing import ClassVar

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron import Precision, lm
from iron.tune.autotune import Timed
from iron.lm import (
    Attention,
    Checkpoint,
    Encoder,
    NoCache,
    PleLayer,
    RMSNorm,
    rope_angles,
)
from iron.lm.testing import weights_dir
from iron.operators.copy import Copy
from iron.operators.mha import MHA

from .audio import AudioTower
from .config import PROFILES, AudioConfig, Config, VisionConfig
from .vision import VisionTower


class Tokenizer:
    """EmbeddingGemma 2's text processor: the checkpoint's `tokenizer.json`,
    a text behind its task's prefix, and the placeholders of a clip's and an
    image's soft tokens expanded as Hugging Face's processor expands them.

    Args:
        path: The checkpoint's `tokenizer.json`; its `encode` adds BOS and EOS.
        config: The text encoder's shape: its placeholder and marker ids.
    """

    # Each task's prefix, which a text is embedded behind: the model's
    # sentence-transformers prompts, by the names its users give a task.
    TASKS: ClassVar[dict[str, str]] = {
        "BitextMining": "task: search result | query: ",
        "Classification": "task: classification | query: ",
        "Clustering": "task: clustering | query: ",
        "CodeRetrieval": "task: code retrieval | query: ",
        "Document": "title: none | text: ",
        "FactChecking": "task: fact checking | query: ",
        "InstructionRetrieval": "task: code retrieval | query: ",
        "MultilabelClassification": "task: classification | query: ",
        "PairClassification": "task: sentence similarity | query: ",
        "QuestionAnswering": "task: question answering | query: ",
        "Reranking": "task: search result | query: ",
        "Retrieval": "task: search result | query: ",
        "Retrieval-document": "title: none | text: ",
        "Retrieval-query": "task: search result | query: ",
        "STS": "task: sentence similarity | query: ",
        "SearchQuery": "task: search result | query: ",
        "SentenceSimilarity": "task: sentence similarity | query: ",
        "Summarization": "task: sentence similarity | query: ",
        "document": "title: none | text: ",
        "query": "task: search result | query: ",
    }

    def __init__(self, path, config: Config = Config()):
        import tokenizers

        self.tokenizer = tokenizers.Tokenizer.from_file(str(path))
        self.config = config

    def encode(
        self, text: str, task: str, audio_tokens: int = 0, image_tokens: int = 0
    ) -> list[int]:
        """`text` behind `task`'s prefix (`TASKS`), with BOS and EOS, each
        `<|audio|>` and `<|image|>` in it a run of that many placeholders
        between its markers.
        """
        c, out = self.config, []
        runs = {
            c.audio_token: [c.boa, *[c.audio_token] * audio_tokens, c.eoa],
            c.image_token: [c.boi, *[c.image_token] * image_tokens, c.eoi],
        }
        for t in self.tokenizer.encode(self.TASKS[task] + text).ids:
            out += runs.get(t, [t])
        return out


class TextLayer(PleLayer):
    """Layer ``i``: unscaled attention over RMS-normed q, k and v, its own
    KV groups and head size (``Config.heads``), turned by its head size's
    RoPE table, a sliding layer's within ``sliding_window`` positions.
    """

    def __init__(self, c: Config, i: int):
        G, D, _ = c.heads(i)
        heads = dataclasses.replace(c, num_key_value_heads=G, head_dim=D)
        sliding = c.layer_types[i] != "full_attention"
        window = NoCache(c.sliding_window if sliding else None)
        super().__init__(c, i, Attention(heads, i, norms="qkv"), cache=window)
        self.self_attn.scaling = 1.0
        self.rope = D


class EmbeddingGemma(Encoder):
    """The text encoder over ``max_tokens`` rows at most, one compile for
    every length.

    A call takes the token ids, padded to ``max_tokens``, and ``rows``, the
    real rows, which bound the gather and every operator after it. The
    scaled table's rows are gathered on the device. It returns one unit-length
    embedding per ``mrl_dims`` truncation, a row each, zero past its length.
    Attention is bidirectional and unscaled, a sliding layer's within
    ``sliding_window`` positions.

    Args:
        config: The encoder's shape.
        weights: The checkpoint's; the text encoder's tree is read.
        tokenizer: What ``embed`` encodes text with.
    """

    profile = PROFILES
    layer_class = TextLayer
    # Transformers 5 saves a layer's per-layer input under ``ple_block``.
    renames = {
        f"ple_block.{name}": name
        for name in (
            "per_layer_input_gate",
            "per_layer_projection",
            "post_per_layer_input_norm",
        )
    }

    def __init__(
        self,
        config: Config,
        weights: SimpleNamespace,
        tokenizer: Tokenizer | None = None,
    ):
        c = config
        self.tokenizer = tokenizer
        w = self.language_model = weights.language_model
        super().__init__(config, c.max_tokens)
        self.final_norm = RMSNorm(c.hidden_size, c.eps)
        self.load_layers(weights, "language_model.layers.", "language_model.norm.")
        scale = np.sqrt(np.float32(c.hidden_size))
        embedding = w.embed_tokens.weight.astype(np.float32) * scale
        self.embed_scaled = embedding.astype(bfloat16)
        self.rope = {
            D: iron.weight(rope_angles(D, c.max_tokens, base).astype(bfloat16))
            for _, D, base in {c.heads(i) for i in range(c.num_hidden_layers)}
        }
        self.query = np.zeros((c.block, 1, c.hidden_size), bfloat16)
        # A power of four: a row's RMS over it is its norm over a power of two.
        width = 4 ** math.ceil(math.log(c.out_dim, 4))
        mrl = np.zeros((len(c.mrl_dims), width, c.hidden_size), bfloat16)
        for j, d in enumerate(c.mrl_dims):
            mrl[j, :d] = w.embedding_projection.weight[:d]
        # Each truncation's rows of the projection, a power of four apart.
        self.mrl = mrl.reshape(-1, c.hidden_size)
        self.unit = np.full(width, 1 / np.sqrt(width), bfloat16)

    def lookup(self, ids):
        table = iron.weight(self.embed_scaled)
        return Copy.step(table[ids])

    def angles(self, n):
        return {D: (table[:n],) * 2 for D, table in self.rope.items()}

    def layer(self, step, i, layer, x):
        """Layer ``i`` on ``x``, its per-layer input projected from the
        step's embeddings.
        """
        c = self.config
        # The projection's E ** -0.5 scale folded into the norm's epsilon:
        # RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        P, tree = c.ple_dim, self.language_model.ple
        projection = tree.per_layer_model_projection.weight[i * P : (i + 1) * P]
        ple = F.linear(step.embeddings, projection, precision=Precision.HIGHEST)
        norm = tree.per_layer_projection_norm.weight
        ple = F.rms_norm(ple, ple.shape[-1:], norm, c.eps * c.hidden_size)
        return layer(x, step, ple)

    def pool(self, x, n):
        """The mean of the ``n`` rows of ``x``: one zero query at scale 0
        weighs each key ``1 / n``, and masks the rows past ``n`` rather than
        multiplying them by 0.
        """
        c = self.config
        h = x.reshape(x.shape[0], 1, c.hidden_size)
        mean = MHA.step(
            self.query,
            h,
            h,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            scale=0.0,
            num_pipelines=1,
        )
        return mean.reshape(c.block, c.hidden_size)[0]

    def head(self, x):
        c = self.config
        y = F.linear(x, self.mrl)
        y = y.reshape(len(c.mrl_dims), self.unit.size)
        return F.rms_norm(y, y.shape[-1:], self.unit, 0.0)

    def encode(self, tokens, dims: int = 768) -> np.ndarray:
        """The unit-length embedding of ``tokens`` truncated to ``dims``, one
        of ``mrl_dims``.
        """
        ids, values = self.inputs(tokens)
        return self.config.truncated(self(ids, **values).numpy(), dims)

    def embed(self, text: str, task: str, dims: int = 768) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized."""
        return self.encode(self.tokenizer.encode(text, task), dims)


class Multimodal(lm.Multimodal):
    """The text encoder with one clip's and one image's soft tokens in
    their placeholders' places (``iron.lm.Multimodal``), unscaled.

    Args:
        config: The text encoder's shape.
        weights: The checkpoint's: the text encoder's tree and each tower's.
        tokenizer: As ``EmbeddingGemma`` takes it.
        audio_config: The audio tower's shape.
        vision_config: The vision tower's shape.
    """

    profile = PROFILES

    def __init__(
        self,
        config: Config,
        weights: SimpleNamespace,
        tokenizer: Tokenizer | None = None,
        audio_config: AudioConfig = AudioConfig(),
        vision_config: VisionConfig = VisionConfig(),
    ):
        self.config = config
        self.tokenizer = tokenizer
        super().__init__(
            EmbeddingGemma(config, weights, tokenizer),
            {
                config.audio_token: AudioTower(audio_config, weights),
                config.image_token: VisionTower(vision_config, weights),
            },
        )

    def encode(self, tokens, dims: int = 768, audio=None, image=None) -> np.ndarray:
        """The unit-length embedding of ``tokens`` with one mono clip
        ``audio`` and one decoded image ``image`` at their placeholders,
        truncated to ``dims``.
        """
        c = self.config
        raw = {}
        if audio is not None:
            raw[c.audio_token] = (audio,)
        if image is not None:
            vision = self.towers[c.image_token].config
            raw[c.image_token] = (image, vision.image_tokens)
        return c.truncated(self.run(tokens, raw).numpy(), dims)

    def embed(
        self, text: str, task: str, dims: int = 768, audio=None, image=None
    ) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized,
        with one mono clip `audio` at 16 kHz and one decoded image `image`,
        `(height, width, 3)` uint8, at their placeholders.
        """
        c = self.config
        a = self.towers[c.audio_token].config
        v = self.towers[c.image_token].config
        audio_tokens = 0 if audio is None else a.tokens(a.frames(np.size(audio)))
        image_tokens = (
            0 if image is None else v.tokens(*np.shape(image)[:2], v.image_tokens)
        )
        tokens = self.tokenizer.encode(text, task, audio_tokens, image_tokens)
        return self.encode(tokens, dims, audio, image)

    @classmethod
    def tune_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The checkpoint whose header gives the weights' shapes; every
        version is timed at its longest call.
        """
        parser.add_argument(
            "--checkpoint",
            type=Path,
            default=weights_dir("embeddinggemma-2"),
            help="the checkpoint directory, of whose model.safetensors only "
            "the header is read (default: %(default)s)",
        )

    @classmethod
    def tune_calls(
        cls, parser: argparse.ArgumentParser, args: argparse.Namespace
    ) -> list[Timed]:
        """Every version (the text encoder, each tower and the merge) at its
        longest call, on weights it never reads, unread from the shapes the
        checkpoint's header gives. The towers' graphs alone run designs
        these hold, so the one profile in ``profiles/`` serves them.
        """
        weights = Checkpoint(args.checkpoint / "model.safetensors").tree("unread")
        graph = cls(Config(), weights)
        return [
            Timed(graph.record(**shapes), graph.longest()) for shapes in graph.shapes()
        ]


def main():
    config = Config()
    parser = argparse.ArgumentParser(
        description="Rank documents against a query by EmbeddingGemma 2's "
        "embeddings, on the NPU"
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="the checkpoint directory, holding model.safetensors and tokenizer.json",
    )
    parser.add_argument("--query", required=True)
    parser.add_argument("--document", nargs="+", required=True)
    parser.add_argument("--dims", type=int, choices=config.mrl_dims, default=768)
    args = parser.parse_args()
    tokenizer = Tokenizer(args.directory / "tokenizer.json", config)
    weights = Checkpoint(args.directory / "model.safetensors").tree()
    encoder = EmbeddingGemma(config, weights, tokenizer).load_versions()
    try:
        t = time.perf_counter()
        query = encoder.embed(args.query, "query", args.dims)
        print(f"query embedded in {(time.perf_counter() - t) * 1e3:.0f} ms")
        documents = [encoder.embed(d, "document", args.dims) for d in args.document]
    finally:
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()
    scores = np.stack(documents) @ query
    for i in np.argsort(-scores):
        print(f"{scores[i]:.4f}  {args.document[i]}")


if __name__ == "__main__":
    main()
