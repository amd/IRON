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
import math
import time
from functools import partial
from pathlib import Path
from types import SimpleNamespace
from typing import ClassVar

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16
import tokenizers

import iron
from iron import lm
from iron import Scratchpad
from iron.tune.narrowing import CostTable, JointNarrowing
from iron.tune.probe import Call
from iron.lm import Checkpoint, Derived, Encoder, rope_angles
from iron.lm.blocks import ACCURATE
from iron.lm.testing import weights_dir
from iron.operators.copy import Copy
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.merge import Merge
from iron.operators.mha import MHA
from iron.operators.rms_norm import RMSNorm

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


class EmbeddingGemma(Encoder):
    """The text encoder over ``max_tokens`` rows at most, one compile for
    every length.

    A call takes the token ids, padded to ``max_tokens``, and ``n``, the
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

    def __init__(
        self,
        config: Config,
        weights: SimpleNamespace,
        tokenizer: Tokenizer | None = None,
    ):
        c = config
        self.tokenizer = tokenizer
        w = self.language_model = weights.language_model
        super().__init__(config, w.layers, c.max_tokens)
        derived = Derived(weights)
        scale = np.sqrt(np.float32(c.emb_dim))
        derived.put(
            w.embed_tokens,
            scaled=(w.embed_tokens.weight.astype(np.float32) * scale).astype(bfloat16),
        )
        for i, layer in enumerate(w.layers):
            c.layer(i).derive(derived, layer)
        self.rope = {
            D: iron.weight(rope_angles(D, c.max_tokens, base).astype(bfloat16))
            for _, D, base in {c.heads(i) for i in range(c.n_layers)}
        }
        self.query = np.zeros((c.block, 1, c.emb_dim), bfloat16)
        # A power of four: a row's RMS over it is its norm over a power of two.
        width = 4 ** math.ceil(math.log(c.out_dim, 4))
        mrl = np.zeros((len(c.mrl_dims), width, c.emb_dim), bfloat16)
        for j, d in enumerate(c.mrl_dims):
            mrl[j, :d] = w.embedding_projection.weight[:d]
        derived.put(w.embedding_projection, mrl=mrl.reshape(-1, c.emb_dim))
        self.derived = derived.tree()
        self.unit = np.full(width, 1 / np.sqrt(width), bfloat16)

    def lookup(self, ids):
        table = iron.weight(self.derived.language_model.embed_tokens.scaled)
        return Copy.step(table[ids])

    def angles(self, n):
        return {D: table[:n] for D, table in self.rope.items()}

    def layer(self, step, i, w, x):
        """Layer ``i`` on ``x``, its per-layer input projected from the
        step's embeddings.
        """
        c = self.config
        # The projection's E ** -0.5 scale folded into the norm's epsilon:
        # RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        P, tree = c.ple_dim, self.language_model.ple
        projection = tree.per_layer_model_projection.weight[i * P : (i + 1) * P]
        ple = GEMM.step(step.embeddings, projection, b_col_maj=True, **ACCURATE)
        norm = tree.per_layer_projection_norm.weight
        ple = RMSNorm.step(ple, weight=norm, epsilon=c.eps * c.emb_dim)
        layer = c.layer(i)
        return layer.step(
            w,
            x,
            partial(self.attend, step, i),
            step.angles[layer.head_dim],
            ple=ple,
            derived=self.derived.language_model.layers[i],
        )

    def norm(self, x):
        w = self.language_model.norm.weight
        return RMSNorm.step(x, weight=w, epsilon=self.config.eps)

    def pool(self, x, n):
        """The mean of the ``n`` rows of ``x``: one zero query at scale 0
        weighs each key ``1 / n``, and masks the rows past ``n`` rather than
        multiplying them by 0.
        """
        c = self.config
        h = x.reshape(x.shape[0], 1, c.emb_dim)
        mean = MHA.step(
            self.query,
            h,
            h,
            heads_interleaved=True,
            kv_interleaved=True,
            causal=False,
            emulate_bf16_mmul_with_bfp16=False,
            scale=0.0,
            num_pipelines=1,
        )
        return mean.reshape(c.block, c.emb_dim)[0]

    def head(self, x):
        c = self.config
        y = GEMV.step(self.derived.language_model.embedding_projection.mrl, x)
        return RMSNorm.step(
            y.reshape(len(c.mrl_dims), self.unit.size), weight=self.unit, epsilon=0.0
        )

    def encode(self, tokens, dims: int = 768) -> np.ndarray:
        """The unit-length embedding of ``tokens`` truncated to ``dims``, one
        of ``mrl_dims``.
        """
        ids, values = self.inputs(tokens)
        rows = self(ids, **values).numpy().reshape(len(self.config.mrl_dims), -1)
        return np.asarray(rows[self.config.mrl_dims.index(dims), :dims], np.float32)

    def embed(self, text: str, task: str, dims: int = 768) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized."""
        return self.encode(self.tokenizer.encode(text, task), dims)


class Multimodal(EmbeddingGemma):
    """The text encoder over at most ``max_tokens`` rows, of which one
    clip's and one image's placeholders take that clip's and that image's
    soft tokens, as Hugging Face's ``masked_scatter`` places them: the j-th
    placeholder the j-th soft token, unscaled.

    Each version takes one input. ``ids`` alone is the text encoder's. A
    mixed call is a version per tower and one over ``placed``, the ids
    with their placeholders: ``wave``'s writes the clip's soft tokens to
    the state ``merged`` from ``audio_at``, ``rgb``'s the image's from
    ``vision_at``, and ``placed``'s the token embeddings from its first
    row, then ``Merge`` gives each position its row of ``merged`` from the
    ids, and those rows are the sequence the encoder runs over. A version
    is one dispatch with its own scratchpad, which all three in one would
    overrun.

    Args:
        config: The text encoder's shape.
        weights: The checkpoint's: the text encoder's tree and each tower's.
        tokenizer: As ``EmbeddingGemma`` takes it.
        audio_config: The audio tower's shape.
        vision_config: The vision tower's shape.
    """

    def __init__(
        self,
        config: Config,
        weights: SimpleNamespace,
        tokenizer: Tokenizer | None = None,
        audio_config: AudioConfig = AudioConfig(),
        vision_config: VisionConfig = VisionConfig(),
    ):
        super().__init__(config, weights, tokenizer)
        self.audio = AudioTower(audio_config, weights)
        self.vision = VisionTower(vision_config, weights)
        self.audio_at = config.max_tokens
        self.vision_at = config.max_tokens + audio_config.max_tokens
        self.merged = iron.state(
            (self.vision_at + self.vision.pooling.shape[0], config.emb_dim)
        )

    def body(
        self,
        ids=None,
        wave=None,
        rgb=None,
        placed=None,
        *,
        n: Scratchpad[np.int32],
        n_audio: Scratchpad[np.int32],
        frames: Scratchpad[np.int32],
        audio_tokens: Scratchpad[np.int32],
        n_patches: Scratchpad[np.int32],
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        given = [t for t in (ids, wave, rgb, placed) if t is not None]
        if len(given) != 1:
            raise TypeError(f"a version takes one input, got {len(given)}")
        if ids is not None:
            return self.forward(self.lookup(ids[:n]), n, self.angles(n))
        if wave is not None:
            a = self.audio(wave, n=n_audio, frames=frames, tokens=audio_tokens)
            Copy.step(a, self.merged[self.audio_at : self.audio_at + a.shape[0]])
            return None
        if rgb is not None:
            v = self.vision(
                rgb,
                n=n_patches,
                height=height,
                width=width,
                out_height=out_height,
                out_width=out_width,
            )
            Copy.step(v, self.merged[self.vision_at : self.vision_at + v.shape[0]])
            return None
        c = self.config
        # An input's gather is encoded on the host into its buffer, which Merge
        # reads as the ids: gather by the device's copy of them, whole, since
        # a gather by ids the device made takes no per-call bound.
        x = self.lookup(Copy.step(placed, dtype=np.int32))
        merge = Merge.step(
            placed,
            audio_token=c.audio_token,
            image_token=c.image_token,
            audio_at=self.audio_at,
            vision_at=self.vision_at,
        )
        Copy.step(x, self.merged[: x.shape[0]])
        return self.forward(Copy.step(self.merged[merge])[:n], n, self.angles(n))

    def shapes(self) -> list[dict]:
        """The input shapes of each version: the text encoder's, each
        tower's, and the ids with their placeholders.
        """
        (text,) = super().shapes()
        (audio,) = self.audio.shapes()
        (vision,) = self.vision.shapes()
        return [text, audio, vision, dict(placed=text["ids"])]

    def longest(self) -> dict:
        """The per-call values of the longest call: every row real, the
        clip its longest, the image the largest, its patches filled.
        """
        audio, vision = self.audio.longest(), self.vision.longest()
        return dict(
            n=self.max_tokens,
            n_audio=audio["n"],
            frames=audio["frames"],
            audio_tokens=audio["tokens"],
            n_patches=vision.pop("n"),
            **vision,
        )

    def mixed(self, tokens, audio=None, image=None) -> tuple[list[tuple], dict]:
        """The inputs of each version a call runs, in ``body``'s order and
        the order they run in, and the call's per-call values.

        Args:
            tokens: The token ids, each placeholder run as long as its soft
                tokens.
            audio: One mono clip at the audio tower's ``sample_rate``.
            image: One decoded image, ``(height, width, 3)`` uint8.

        Raises:
            ValueError: A placeholder's count is not its tower's soft tokens.
        """
        c = self.config
        tokens = np.asarray(tokens)
        ids, values = self.inputs(tokens)
        values = dict(
            **values,
            n_audio=0,
            frames=0,
            audio_tokens=0,
            n_patches=0,
            height=0,
            width=0,
            out_height=0,
            out_width=0,
        )
        calls = []
        soft = {c.audio_token: 0, c.image_token: 0}
        if audio is not None:
            wave, sizes = self.audio.inputs(audio)
            values.update(
                n_audio=sizes["n"], frames=sizes["frames"], audio_tokens=sizes["tokens"]
            )
            soft[c.audio_token] = self.audio.soft(sizes)
            calls.append((None, wave))
        if image is not None:
            vision = self.vision.config
            rgb, sizes = self.vision.inputs(image, vision.image_tokens)
            soft[c.image_token] = self.vision.soft(sizes)
            values.update(sizes, n_patches=sizes.pop("n"))
            calls.append((None, None, rgb))
        for token, count in soft.items():
            places = np.count_nonzero(tokens == token)
            if places != count:
                raise ValueError(
                    f"{places} placeholders {token} for {count} soft tokens"
                )
        if not calls:
            return [(ids,)], values
        return [*calls, (None, None, None, ids)], values

    def encode(self, tokens, dims: int = 768, audio=None, image=None) -> np.ndarray:
        """The unit-length embedding of ``tokens`` with ``audio`` and
        ``image`` (as ``mixed`` takes them), truncated to ``dims``.
        """
        calls, values = self.mixed(tokens, audio, image)
        for inputs in calls:
            out = self(*inputs, **values)
        rows = out.numpy().reshape(len(self.config.mrl_dims), -1)
        return np.asarray(rows[self.config.mrl_dims.index(dims), :dims], np.float32)

    def embed(
        self, text: str, task: str, dims: int = 768, audio=None, image=None
    ) -> np.ndarray:
        """The embedding of `text` for `task`, its first `dims` renormalized,
        with one mono clip `audio` at 16 kHz and one decoded image `image`,
        `(height, width, 3)` uint8, at their placeholders.
        """
        a, v = self.audio.config, self.vision.config
        audio_tokens = 0 if audio is None else a.tokens(a.frames(np.size(audio)))
        image_tokens = (
            0 if image is None else v.tokens(*np.shape(image)[:2], v.image_tokens)
        )
        tokens = self.tokenizer.encode(text, task, audio_tokens, image_tokens)
        return self.encode(tokens, dims, audio, image)


class Runner(lm.Runner):
    """EmbeddingGemma 2 as ``iron.lm.tune`` measures it: every version of
    ``Multimodal`` (the text encoder, each tower and the merge) at its
    longest call, on weights it never reads, unread from the shapes the
    checkpoint's header gives, the table in ``profiles/``. The towers'
    graphs alone run designs these hold, so one table serves them.
    """

    config = Config()
    model = Multimodal
    tables = PROFILES

    @classmethod
    def tune_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """The checkpoint whose header gives the weights' shapes; every
        version is measured at its longest call.
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
    ) -> list[Call]:
        dev = aie_utils.ensure_current_device()
        weights = Checkpoint(args.checkpoint / "model.safetensors").tree("unread")
        graph = cls.model(cls.config, weights)
        return [
            call
            for shapes in graph.shapes()
            for call in Call.admitted(graph.trace(**shapes), dev, graph.longest())
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
    parser.add_argument(
        "--costs",
        type=Path,
        help="the cost table the designs are narrowed and packed by "
        "(`python -m iron.lm.tune embedding_gemma2` writes costs_<device>.json "
        f"in {PROFILES}); default: as the profile gives them",
    )
    args = parser.parse_args()
    tokenizer = Tokenizer(args.directory / "tokenizer.json", config)
    tuner = None if args.costs is None else JointNarrowing(CostTable(args.costs))
    weights = Checkpoint(args.directory / "model.safetensors").tree()
    encoder = EmbeddingGemma(config, weights, tokenizer).load(tuner=tuner)
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
