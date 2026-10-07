# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2 over text, audio and an image as one graph: the towers'
soft tokens take their placeholders' places in the text, and the text
encoder runs over the result, all on the NPU.
"""

import numpy as np

import iron
from iron.common import Scratchpad
from iron.common.graph.narrowing import JointNarrowing
from iron.operators.copy import Copy

from .audio.model import AudioTower
from .model import Config, EmbeddingGemma
from .vision.model import VisionTower


class Multimodal(EmbeddingGemma):
    """The encoder over at most ``max_tokens`` rows, of which one clip's and
    one image's placeholders take that clip's and that image's soft tokens,
    as Hugging Face's ``masked_scatter`` places them: the j-th placeholder
    the j-th soft token, unscaled.

    A call with neither is the text encoder's. A mixed call writes the token
    embeddings to the state ``merged`` from its first row, the clip's soft
    tokens from ``audio_at`` and the image's from ``vision_at``; ``merge``,
    a row of ``merged`` per position, gathers the sequence the encoder runs
    over. Only the versions without a tower compile in ``load``: a mixed one
    compiles on its first call, with the tuner ``load`` was given.

    Args:
        config: The text encoder's shape.
        weights: The text encoder's tree, as ``EmbeddingGemma`` takes it.
        max_tokens: The longest sequence, soft tokens included.
        audio: The audio tower, its soft tokens in the text's space.
        vision: The vision tower, its soft tokens in the text's space.
    """

    def __init__(
        self,
        config: Config,
        weights,
        max_tokens: int,
        audio: AudioTower,
        vision: VisionTower,
    ):
        super().__init__(config, weights, max_tokens)
        self.audio = audio
        self.vision = vision
        self.audio_at = max_tokens
        self.vision_at = max_tokens + audio.rows[-1]
        soft = vision.pool[vision.rows[-1]].shape[0]
        self.merged = iron.state((self.vision_at + soft, config.emb_dim))
        self.tuner: JointNarrowing | None = None
        self.compiled: set[tuple] = set()

    def body(
        self,
        ids,
        merge=None,
        mel=None,
        pixels=None,
        px=None,
        py=None,
        angles=None,
        *,
        n: Scratchpad[np.int32],
        n_audio: Scratchpad[np.int32],
        n_patches: Scratchpad[np.int32],
    ):
        x = Copy(self.embedding[ids])
        if merge is None:
            if mel is not None or pixels is not None:
                raise ValueError("a tower's soft tokens take places merge= names")
            return self.encoder(x, n)
        Copy(x, self.merged[: x.shape[0]])
        if mel is not None:
            a = self.audio(mel, n_audio)
            Copy(a, self.merged[self.audio_at : self.audio_at + a.shape[0]])
        if pixels is not None:
            v = self.vision(pixels, px, py, angles, n_patches)
            Copy(v, self.merged[self.vision_at : self.vision_at + v.shape[0]])
        return self.encoder(Copy(self.merged[merge]), n)

    # -- on the host -----------------------------------------------------------

    def load(self, tuner: JointNarrowing | None = None) -> "Multimodal":
        """Compile the text versions, and keep ``tuner`` for the mixed ones.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        self.tuner = tuner
        super().load(tuner)
        return self

    def mixed(self, tokens, audio=None, image=None) -> tuple[tuple, dict]:
        """A call's inputs, in ``body``'s order, and its per-call values.

        Args:
            tokens: The token ids, each placeholder run as long as its soft
                tokens.
            audio: One clip's ``(features, frames)``, as ``LogMel`` gives them.
            image: One image's ``(pixel_values, positions)``, as the
                processor gives them.

        Raises:
            ValueError: A placeholder's count is not its tower's soft tokens.
        """
        c = self.config
        tokens = np.asarray(tokens)
        ids, n = self.inputs(tokens)
        values = dict(n=n, n_audio=0, n_patches=0)
        mel, picture = None, (None,) * 4
        soft = {c.audio_token: (0, 0), c.image_token: (0, 0)}
        if audio is not None:
            mel, values["n_audio"] = self.audio.inputs(*audio)
            soft[c.audio_token] = (self.audio_at, self.audio.config.tokens(audio[1]))
        if image is not None:
            given, values["n_patches"] = self.vision.inputs(*image)
            picture = tuple(given.values())
            pooled = values["n_patches"] // self.vision.config.pool**2
            soft[c.image_token] = (self.vision_at, pooled)
        merge = np.arange(ids.size, dtype=np.int32)
        for token, (at, count) in soft.items():
            places = np.flatnonzero(tokens == token)
            if places.size != count:
                raise ValueError(
                    f"{places.size} placeholders {token} for {count} soft tokens"
                )
            merge[places] = at + np.arange(count)
        if audio is None and image is None:
            return (ids,), values
        return (ids, merge, mel, *picture), values

    def encode(self, tokens, dims: int = 768, audio=None, image=None) -> np.ndarray:
        """The unit-length embedding of ``tokens`` with ``audio`` and
        ``image`` (as ``mixed`` takes them), truncated to ``dims``.
        """
        inputs, values = self.mixed(tokens, audio, image)
        given = {k: t for k, t in zip(self._inputs, inputs) if t is not None}
        shapes = tuple((k, t.shape) for k, t in given.items())
        if "merge" in given and shapes not in self.compiled:
            self.compile(
                coresident=self.tuner,
                **{k: (t.shape, t.dtype) for k, t in given.items()},
            )
            self.compiled.add(shapes)
        rows = self(*inputs, **values).numpy().reshape(len(self.config.mrl_dims), -1)
        return np.asarray(rows[self.config.mrl_dims.index(dims), :dims], np.float32)
