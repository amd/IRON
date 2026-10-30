# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 on the NPU.

The text encoder as one graph (``EmbeddingGemma``), and over text, audio
and an image (``Multimodal``), Gemma 4's towers' soft tokens in their
placeholders' places. Run with
``python -m iron.applications.embedding_gemma2.model <checkpoint>
--query ... --document ...``.
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
from iron.applications.gemma4.audio import AudioConfig, AudioTower
from iron.applications.gemma4.vision import VisionConfig, VisionTower
from iron.lm import (
    Attention,
    Checkpoint,
    Encoder,
    NoCache,
    PleLayer,
    RMSNorm,
    rope_angles,
)
from iron.lm.checkpoint import renamed, weights_file
from iron.lm.testing import weights_dir
from iron.operators.copy import Copy
from iron.operators.mha import MHA
from iron.tune.autotune import Timed

PROFILES = Path(__file__).with_name("profiles")


@dataclasses.dataclass(frozen=True)
class Config(lm.Config):
    # Every projection at HIGHEST (``Attention``, ``GatedMLP``).
    precision: Precision = lm.not_json(Precision.HIGHEST, kw_only=True)
    json_prefix = "text_config."

    vocab_size: int = 262144
    hidden_size: int = 512
    num_hidden_layers: int = 24
    num_attention_heads: int = 4
    intermediate_size: int = 2048
    # A sliding layer's KV groups, head size and RoPE base; a global layer's
    # are its own.
    num_key_value_heads: int = 2
    head_dim: int = 256
    rope_theta: float = dataclasses.field(
        default=10000.0,
        metadata={"json": "rope_parameters.sliding_attention.rope_theta"},
    )
    layer_types: tuple[str, ...] = dataclasses.field(
        default=(("sliding_attention",) * 5 + ("full_attention",)) * 4,
        metadata={"convert": tuple},
    )
    global_kv_groups: int = dataclasses.field(
        default=1,
        metadata={"json": "per_layer_config.05.num_key_value_heads"},
    )
    global_head_dim: int = dataclasses.field(
        default=512, metadata={"json": "per_layer_config.05.head_dim"}
    )
    global_rope_theta: float = dataclasses.field(
        default=1000000.0,
        metadata={"json": "rope_parameters.full_attention.rope_theta"},
    )
    sliding_window: int = 512
    ple_dim: int = dataclasses.field(
        default=512, metadata={"json": "hidden_size_per_layer_input"}
    )
    embedding_dim: int = 768
    hidden_act: str = dataclasses.field(
        default="gelu_pytorch_tanh", metadata={"json": "hidden_activation"}
    )
    # The Matryoshka truncations, each renormalized.
    mrl_dims: tuple[int, ...] = lm.not_json((768, 512, 256, 128))
    # The placeholders an image's or a clip's soft tokens take the place of,
    # and the markers either side of a run of them.
    image_token: int = dataclasses.field(
        default=258880, metadata={"json": "/image_token_id"}
    )
    audio_token: int = dataclasses.field(
        default=258881, metadata={"json": "/audio_token_id"}
    )
    boi: int = dataclasses.field(default=255999, metadata={"json": "/boi_token_id"})
    eoi: int = dataclasses.field(default=258882, metadata={"json": "/eoi_token_id"})
    boa: int = dataclasses.field(default=256000, metadata={"json": "/boa_token_id"})
    # Hugging Face's own config.json spells this one an "index", unlike every
    # other marker's "id".
    eoa: int = dataclasses.field(default=258883, metadata={"json": "/eoa_token_index"})
    # The longest sequence a call takes, soft tokens included.
    max_tokens: int = lm.not_json(2048)
    # An MHA query block: the mean over the sequence is one query, a block.
    block: int = lm.not_json(64)

    def truncated(self, out, dims: int) -> np.ndarray:
        """Return the ``dims`` truncation of a call's embeddings ``out``, float32.

        ``dims`` is one of ``mrl_dims``.
        """
        rows = np.asarray(out).reshape(len(self.mrl_dims), -1)
        return np.asarray(rows[self.mrl_dims.index(dims), :dims], np.float32)

    def heads(self, i: int) -> tuple[int, int, float]:
        """Layer ``i``'s KV groups, head size and RoPE base."""
        if self.layer_types[i] == "full_attention":
            return self.global_kv_groups, self.global_head_dim, self.global_rope_theta
        return self.num_key_value_heads, self.head_dim, self.rope_theta


class TextProcessor:
    """EmbeddingGemma 2's text processor.

    Tokenizes a text behind its task's prefix, and expands the placeholders
    for a clip's and an image's soft tokens as Hugging Face's processor does.

    Args:
        path: The checkpoint's `tokenizer.json`; its `encode` adds BOS and EOS.
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
        import tokenizers  # the models extra's: optional

        self.tokenizer = tokenizers.Tokenizer.from_file(str(path))
        self.config = config

    def encode(
        self, text: str, task: str, audio_tokens: int = 0, image_tokens: int = 0
    ) -> list[int]:
        """Encode `text` behind `task`'s prefix (`TASKS`), with BOS and EOS.

        Each `<|audio|>` and `<|image|>` in it is a run of that many
        placeholders between its markers.
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
    """Layer ``i``: unscaled attention over RMS-normed q, k and v.

    Its own KV groups and head size come from ``Config.heads``, turned by
    its head size's RoPE table; a sliding layer is bound within
    ``sliding_window`` positions.
    """

    def __init__(self, c: Config, i: int):
        G, D, base = c.heads(i)
        heads = dataclasses.replace(c, num_key_value_heads=G, head_dim=D)
        sliding = c.layer_types[i] != "full_attention"
        window = NoCache(c.sliding_window if sliding else None)
        super().__init__(c, i, Attention(heads, i, norms="qkv"), cache=window)
        self.self_attn.scaling = 1.0
        self.rope = D, base


class EmbedTokens(iron.Graph):
    """The vocabulary's rows, gathered on the device.

    Scaled by ``sqrt(hidden_size)`` once this loads (Gemma's input
    embedding scale).
    """

    def __init__(self, c: Config):
        self.weight = iron.param(c.vocab_size, c.hidden_size)
        self._scale = np.sqrt(np.float32(c.hidden_size))

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        scaled = self.weight.astype(np.float32) * self._scale
        self.scaled = iron.param(scaled.astype(bfloat16))


class EmbeddingProjection(iron.Graph):
    """The projection's Matryoshka truncations, derived once this loads.

    Each is padded to a power of four and stacked a power of four apart.
    """

    def __init__(self, c: Config):
        self.weight = iron.param(c.embedding_dim, c.hidden_size)
        self._dims, self._hidden = c.mrl_dims, c.hidden_size

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # A power of four: a row's RMS over it is its norm over a power of two.
        self.width = width = 4 ** math.ceil(math.log(self.weight.shape[0], 4))
        mrl = np.zeros((len(self._dims), width, self._hidden), bfloat16)
        for j, d in enumerate(self._dims):
            mrl[j, :d] = self.weight[:d]
        # Each truncation's rows of the projection, a power of four apart.
        self.mrl = iron.param(mrl.reshape(-1, self._hidden))


class LanguageModelPle(iron.Graph):
    """Every layer's slice of the per-layer input projection, and its norm.

    Sliced once this loads; the norm is shared across every layer's slice.
    """

    def __init__(self, c: Config):
        P, L = c.ple_dim, c.num_hidden_layers
        self.per_layer_model_projection = SimpleNamespace(
            weight=iron.param(L * P, c.hidden_size)
        )
        self.per_layer_projection_norm = SimpleNamespace(weight=iron.param(P))
        self._ple_dim = P

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        P, weight = self._ple_dim, self.per_layer_model_projection.weight
        self.layers = [
            iron.param(weight[i * P : (i + 1) * P]) for i in range(weight.shape[0] // P)
        ]


class EmbeddingGemma(Encoder):
    """The text encoder over ``max_tokens`` rows at most, one compile per length.

    Returns one unit-length embedding per ``mrl_dims`` truncation, zero
    past its length, attention bidirectional and unscaled.

    Args:
        weights: The checkpoint's; the text encoder's tree is read.
        processor: What ``embed`` encodes text with.
    """

    config = Config()
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
        processor: TextProcessor | None = None,
    ):
        c = config
        self.processor = processor
        self.language_model = SimpleNamespace()
        super().__init__(config, c.max_tokens)
        self.final_norm = RMSNorm(c.hidden_size, c.eps)
        tree = renamed(weights, self.renames)
        embed_tokens = EmbedTokens(c)
        embed_tokens.load_state_dict(tree, path="language_model.embed_tokens.")
        embedding_projection = EmbeddingProjection(c)
        embedding_projection.load_state_dict(
            tree, path="language_model.embedding_projection."
        )
        ple = LanguageModelPle(c)
        ple.load_state_dict(tree, path="language_model.ple.")
        self.language_model.embed_tokens = embed_tokens
        self.language_model.embedding_projection = embedding_projection
        self.language_model.ple = ple
        self.language_model.layers = self.layers
        self.language_model.norm = self.final_norm
        self.embed_scaled = embed_tokens.scaled
        self.mrl = embedding_projection.mrl
        self.load_layers(weights, "language_model.layers.", "language_model.norm.")
        # A table per head size and base, which a layer names (``rope``).
        self.rope = {
            (D, base): iron.weight(rope_angles(D, c.max_tokens, base).astype(bfloat16))
            for _, D, base in {c.heads(i) for i in range(c.num_hidden_layers)}
        }
        self.query = iron.param(np.zeros((c.block, 1, c.hidden_size), bfloat16))
        width = embedding_projection.width
        self.unit = iron.param(np.full(width, 1 / np.sqrt(width), bfloat16))

    def lookup(self, ids):
        table = iron.weight(self.embed_scaled)
        return Copy.step(table[ids])

    def angles(self, n):
        return {key: (table[:n],) * 2 for key, table in self.rope.items()}

    def layer(self, call, i, layer, x):
        """Run layer ``i`` on ``x``.

        Its per-layer input is projected from the call's embeddings.
        """
        c = self.config
        # The projection's E ** -0.5 scale folded into the norm's epsilon:
        # RMSNorm(s * y, eps) is RMSNorm(y, eps / s ** 2).
        ple_module = self.language_model.ple
        ple = F.linear(call.embeddings, ple_module.layers[i], precision=c.precision)
        norm = ple_module.per_layer_projection_norm.weight
        ple = F.rms_norm(ple, ple.shape[-1:], norm, c.eps * c.hidden_size)
        return layer(x, call, ple)

    def pool(self, x, n):
        """Return the mean of the ``n`` rows of ``x``.

        One zero query at scale 0 weighs each key ``1 / n``, and masks the
        rows past ``n`` rather than multiplying them by 0.
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
        y = F.linear(x, self.mrl, precision=c.precision)
        y = y.reshape(len(c.mrl_dims), self.unit.size)
        return F.rms_norm(y, y.shape[-1:], self.unit, 0.0)

    def encode(self, tokens, dims: int = 768) -> np.ndarray:
        """Return the unit-length embedding of ``tokens`` truncated to ``dims``.

        ``dims`` is one of ``mrl_dims``.
        """
        ids, values = self.inputs(tokens)
        return self.config.truncated(self(ids, **values).numpy(), dims)

    @classmethod
    def from_checkpoint(cls, path, **kwargs):
        """``Model.from_checkpoint``, with the text processor over its tokenizer."""
        model = super().from_checkpoint(path, **kwargs)
        if model.tokenizer is not None:
            assert model.checkpoint is not None, "from_checkpoint gives it one"
            directory = Path(model.checkpoint.path).parent
            model.processor = TextProcessor(directory / "tokenizer.json", model.config)
        return model

    def embed(self, text: str, task: str, dims: int = 768) -> np.ndarray:
        """Return the embedding of `text` for `task`, its first `dims` renormalized."""
        if self.processor is None:
            raise RuntimeError(
                f"{type(self).__name__}: no tokenizer; give token ids to encode"
            )
        return self.encode(self.processor.encode(text, task), dims)


class Multimodal(lm.Multimodal):
    """The text encoder with soft tokens at their placeholders' places.

    One clip's and one image's soft tokens (``iron.lm.Multimodal``),
    unscaled.

    Args:
        weights: The checkpoint's: the text encoder's tree and each tower's.
    """

    profile = PROFILES

    def __init__(
        self,
        config: Config,
        weights: SimpleNamespace,
        processor: TextProcessor | None = None,
        audio_config: AudioConfig = AudioConfig(),
        vision_config: VisionConfig = VisionConfig(),
    ):
        self.config = config
        self.processor = processor
        super().__init__(
            EmbeddingGemma(config, weights, processor),
            {
                config.audio_token: AudioTower(audio_config, weights),
                config.image_token: VisionTower(vision_config, weights),
            },
        )

    def encode(self, tokens, dims: int = 768, audio=None, image=None) -> np.ndarray:
        """Return the unit-length embedding of ``tokens`` truncated to ``dims``.

        One mono clip ``audio`` and one decoded image ``image`` sit at
        their placeholders.
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
        """Return the embedding of `text` for `task`, its first `dims` renormalized.

        One mono clip `audio` at 16 kHz and one decoded image `image`,
        `(height, width, 3)` uint8, sit at their placeholders.
        """
        c = self.config
        a = self.towers[c.audio_token].config
        v = self.towers[c.image_token].config
        audio_tokens = 0 if audio is None else a.tokens(a.frames(np.size(audio)))
        image_tokens = (
            0 if image is None else v.tokens(*np.shape(image)[:2], v.image_tokens)
        )
        if self.processor is None:
            raise RuntimeError(
                f"{type(self).__name__}: no tokenizer; give token ids to encode"
            )
        tokens = self.processor.encode(text, task, audio_tokens, image_tokens)
        return self.encode(tokens, dims, audio, image)

    @classmethod
    def tune_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """Add the checkpoint argument, whose header gives the weights' shapes.

        Every version is timed at its longest call.
        """
        parser.add_argument(
            "--checkpoint",
            type=Path,
            default=weights_dir("embeddinggemma-2"),
            help="the checkpoint directory, of whose weights only the header "
            "is read (default: %(default)s)",
        )

    @classmethod
    def tune_calls(
        cls, parser: argparse.ArgumentParser, args: argparse.Namespace
    ) -> list[Timed]:
        """Return every version's longest call as a ``Timed``, on weights it never reads.

        The text encoder, each tower and the merge; the one profile in
        ``profiles/`` serves every version's designs.
        """
        weights = Checkpoint(weights_file(args.checkpoint)).tree("unread")
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
    encoder = EmbeddingGemma.load(args.directory)
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
