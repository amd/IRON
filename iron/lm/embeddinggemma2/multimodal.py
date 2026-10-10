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
from iron.operators.merge import Merge

from .audio.model import AudioTower
from .model import Config, EmbeddingGemma
from .vision.model import Vision, VisionTower


class Multimodal(EmbeddingGemma):
    """The encoder over at most ``max_tokens`` rows, of which one clip's and
    one image's placeholders take that clip's and that image's soft tokens,
    as Hugging Face's ``masked_scatter`` places them: the j-th placeholder
    the j-th soft token, unscaled.

    Each version takes one input. ``ids`` alone is the text encoder's. A
    mixed call is a version per tower and one over ``placed``, the ids
    with their placeholders: ``wave``'s writes the clip's soft tokens to
    the state ``merged`` from ``audio_at``, ``rgb``'s the image's from
    ``vision_at``, and ``placed``'s the token embeddings from its first
    row, then ``Merge`` gives each position its row of ``merged`` from the
    ids, and those rows are the sequence the encoder runs over. A version
    is one dispatch with its own scratchpad, which all three in one would
    overrun. Only the text version compiles in ``load``: a mixed one
    compiles on its first call, with the tuner ``load`` was given.

    Args:
        config: The text encoder's shape.
        weights: The text encoder's tree, as ``EmbeddingGemma`` takes it.
        max_tokens: The longest sequence, soft tokens included.
        audio: The audio tower, its soft tokens in the text's space.
        vision: The vision tower, its soft tokens in the text's space.
    """

    profile = Vision.profile

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
        self.vision_at = max_tokens + audio.max_tokens
        self.merged = iron.state(
            (self.vision_at + vision.pool.shape[0], config.emb_dim)
        )
        self.tuner: JointNarrowing | None = None
        self.compiled: set[tuple] = set()

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
            return self.encoder(Copy(self.embedding[ids]), n)
        if wave is not None:
            a = self.audio(wave, n_audio, frames, audio_tokens)
            Copy(a, self.merged[self.audio_at : self.audio_at + a.shape[0]])
            return None
        if rgb is not None:
            v = self.vision(rgb, n_patches, height, width, out_height, out_width)
            Copy(v, self.merged[self.vision_at : self.vision_at + v.shape[0]])
            return None
        c = self.config
        # An input's gather is encoded on the host into its buffer, which Merge
        # reads as the ids: gather by the device's copy of them.
        x = Copy(self.embedding[Copy(placed, dtype=np.int32)])
        merge = Merge(
            placed,
            audio_token=c.audio_token,
            image_token=c.image_token,
            audio_at=self.audio_at,
            vision_at=self.vision_at,
        )
        Copy(x, self.merged[: x.shape[0]])
        return self.encoder(Copy(self.merged[merge]), n)

    # -- on the host -----------------------------------------------------------

    def load(self, tuner: JointNarrowing | None = None) -> "Multimodal":
        """Compile the text version, and keep ``tuner`` for the mixed ones.

        Args:
            tuner: Narrows and packs each version's designs by cost.
        """
        self.tuner = tuner
        super().load(tuner)
        return self

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
        ids, n = self.inputs(tokens)
        values = dict(
            n=n,
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
            soft[c.audio_token] = sizes["tokens"]
            calls.append((None, wave))
        if image is not None:
            vision = self.vision.config
            rgb, sizes = self.vision.processor.inputs(image, vision.image_tokens)
            values.update(sizes, n_patches=sizes.pop("n"))
            soft[c.image_token] = values["n_patches"] // vision.pool**2
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
            given = {k: t for k, t in zip(self._inputs, inputs) if t is not None}
            shapes = tuple((k, t.shape) for k, t in given.items())
            if "ids" not in given and shapes not in self.compiled:
                self.compile(
                    coresident=self.tuner,
                    **{k: (t.shape, t.dtype) for k, t in given.items()},
                )
                self.compiled.add(shapes)
            out = self(*inputs, **values)
        rows = out.numpy().reshape(len(self.config.mrl_dims), -1)
        return np.asarray(rows[self.config.mrl_dims.index(dims), :dims], np.float32)
