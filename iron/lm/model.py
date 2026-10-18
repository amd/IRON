# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model``, a model's graph, every version compiled and loaded before
the first call, built from a checkpoint's files (``load``); ``OnHost``, the
model with no device; and ``Tokenizer``, a prompt's text to its ids.
"""

import dataclasses
import functools
import json
import logging
import os
from collections.abc import Callable
from pathlib import Path
from typing import ClassVar

import numpy as np

import iron
from iron.common.image.packaging import require_device

from .checkpoint import Checkpoint
from .config import Config, DecoderConfig
from .golden import Golden, HuggingFace
from .generation import Sampler, generate_on_host

logger = logging.getLogger(__name__)


# What a host keeps beside a model's arena: the OS, Python and XRT, the
# checkpoint's pages as they upload, a test's host copies.
HOST_RESERVE = 8 << 30


def host_budget() -> int:
    """The bytes a model's arena may take here: physical memory, in which
    the NPU's buffers live, less ``HOST_RESERVE``.
    """
    return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") - HOST_RESERVE


def prompt_text(chars: int, skip: int = 0) -> str:
    """``chars`` characters of ``prompt.txt``, from ``skip`` on: the text every
    model's long inputs are drawn from.
    """
    return Path(__file__).with_name("prompt.txt").read_text()[skip : skip + chars]


class Tokenizer:
    """Text to a prompt's token ids, ``bos`` first, and token ids back to
    text, over ``encoding``: anything with ``encode`` and ``decode``, as
    ``Model.open_tokenizer`` gives.
    """

    def __init__(self, encoding, bos: int):
        self.encoding, self.bos = encoding, bos

    def __call__(self, text: str) -> list[int]:
        return [self.bos, *self.encoding.encode(text)]

    def decode(self, tokens) -> str:
        return self.encoding.decode(list(tokens))


class _TokenizerJson:
    """A Hugging Face ``tokenizer.json``, over ``tokenizers`` (not
    ``transformers``): text to token ids without the special tokens its
    post-processor adds, since ``Tokenizer`` puts the BOS first, and back.
    """

    def __init__(self, path):
        import tokenizers

        self._tokenizer = tokenizers.Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        return self._tokenizer.encode(text, add_special_tokens=False).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(tokens)


class Model(iron.Graph):
    """A model's graph, every version ``shapes()`` names compiled and
    loaded by ``load_versions()`` before the first call, so the arena is
    made once: a version on token ids (``ids`` or ``placed``) feeds off the
    decode step, the version with no input, where that is a full ELF, its
    Emit starting there. ``versions`` (``Graph``'s own), in ``shapes()``'s
    order, is every version ``load_versions()`` compiled.

    A model ``load`` builds from a checkpoint names its ``config``, the
    ``Config`` class its ``config.json`` is read by (or one shape), and its
    tokenizer's file and how to open it; ``load`` gives the instance the
    ``checkpoint``, the ``seed`` its weights were drawn at, if any, and the
    ``tokenizer``. Given a ``seed``, the weights are drawn in the
    checkpoint's shapes and a prompt with no tokenizer is random tokens, so
    speed, accuracy and determinism need neither.
    """

    # Each checkpoint layer's dotted paths that its config's ``layer``
    # reads under another name, by that name.
    renames: ClassVar[dict[str, str]] = {}
    # The tokenizer's file in the model's Hugging Face repository.
    tokenizer_file = "tokenizer.json"
    # What loads the checkpoint into transformers to record its goldens.
    hugging_face: type = HuggingFace
    checkpoint: Checkpoint | None = None
    seed: int | None = None
    tokenizer: Tokenizer | None = None

    @classmethod
    def load(
        cls,
        path,
        *,
        seed: int | None = None,
        max_seq_len: int | None = None,
        full_elf: bool | None = None,
    ) -> "Model":
        """``from_checkpoint``'s model compiled and loaded, weights uploaded;
        ``full_elf`` is every version's packaging (``load_versions``).
        """
        model = cls.from_checkpoint(path, seed=seed, max_seq_len=max_seq_len)
        return model.load_versions(release=model.checkpoint.release, full_elf=full_elf)

    @classmethod
    def from_checkpoint(
        cls, path, *, seed: int | None = None, max_seq_len: int | None = None
    ) -> "Model":
        """The model of a Hugging Face repository's files, not yet loaded,
        its context ``max_seq_len`` or else fitted to this host (``fit``).

        Args:
            path: A directory holding ``config.json``, ``model.safetensors``
                or a sharded one's ``model.safetensors.index.json``, and
                ``tokenizer_file``; or a repository's id, those files
                downloaded to Hugging Face's cache.
            seed: In place of the checkpoint's weights and the tokenizer,
                weights drawn at ``seed`` in its shapes (only its header is
                read).
            max_seq_len: The longest context served, prompt and generated
                tokens together, at most the checkpoint's own.

        Raises:
            ValueError: ``max_seq_len`` is past the checkpoint's own.
        """
        directory = Path(path)
        if not directory.is_dir():
            from huggingface_hub import snapshot_download

            files = ["*config.json", "model.safetensors*", cls.tokenizer_file]
            directory = Path(snapshot_download(str(path), allow_patterns=files))
        weights = directory / "model.safetensors.index.json"
        if not weights.exists():
            weights = directory / "model.safetensors"
        config = cls.default_config(weights)
        if max_seq_len is None:
            config = cls.fit(config, weights)
        elif max_seq_len > config.max_seq_len:
            raise ValueError(
                f"max_seq_len {max_seq_len} is past the model's {config.max_seq_len}"
            )
        else:
            config = dataclasses.replace(config, max_seq_len=max_seq_len)
        checkpoint = Checkpoint(weights)
        tree = checkpoint.tree() if seed is None else checkpoint.tree("random", seed)
        model = cls(config, tree)
        model.checkpoint, model.seed = checkpoint, seed
        if seed is None:
            tokenizer = directory / cls.tokenizer_file
            # A directory of its own may hold it at the top.
            if not tokenizer.exists():
                tokenizer = directory / tokenizer.name
            model.tokenizer = Tokenizer(cls.open_tokenizer(tokenizer), model.bos)
        return model

    @functools.cached_property
    def bos(self) -> int:
        """The token every prompt starts with: the checkpoint's
        ``bos_token_id``, from its ``config.json`` or else its
        ``generation_config.json``, unless a subclass names it.
        """
        directory = Path(self.checkpoint.path).parent
        for name in ("config.json", "generation_config.json"):
            path = directory / name
            if path.exists():
                bos = json.loads(path.read_text()).get("bos_token_id")
                if bos is not None:
                    return bos
        raise KeyError(f"{directory} names no bos_token_id: name the model's bos")

    @staticmethod
    def open_tokenizer(path):
        """The tokenizer at ``path``: a Hugging Face ``tokenizer.json``."""
        return _TokenizerJson(path)

    @classmethod
    def default_config(cls, weights_path) -> Config:
        """``cls.config`` itself, if it is already one shape; else that
        class's own, built from ``weights_path``'s checkpoint directory
        (``Config.from_checkpoint``).
        """
        if isinstance(cls.config, type):
            return cls.config.from_checkpoint(weights_path)
        return cls.config

    @classmethod
    def fit(cls, config: Config, weights_path, budget: int | None = None) -> Config:
        """``config`` at its native context where the model's arena fits
        ``budget`` (``host_budget()`` by default), else at the longest whole
        number of prompt chunks that does, logged either way.

        The arena is what the model holds, weights and states, measured by
        tracing its decode step at one and two prompt chunks of context:
        what grows holds a row a position (``tests/applications/
        long_context``).
        """
        if not isinstance(config, DecoderConfig):
            return config
        native, C = config.max_seq_len, config.prefill_chunk
        if native < 2 * C:
            return config
        tree = Checkpoint(weights_path).tree("unread")
        held = []
        for length in (C, 2 * C):
            model = cls(dataclasses.replace(config, max_seq_len=length), tree)
            # What it holds does not follow its tunables, nor need a device.
            model.profile = None
            held.append(sum(model.trace(**model.shapes()[0]).pinned.values()))
        per_position = (held[1] - held[0]) / C
        fixed = held[0] - per_position * C
        budget = host_budget() if budget is None else budget
        need = fixed + per_position * native
        if need <= budget:
            logger.info(
                "max_seq_len %d, the model's native context: %.1f GiB of a %.1f GiB "
                "budget",
                native,
                need / 2**30,
                budget / 2**30,
            )
            return config
        fits = int((budget - fixed) // per_position) // C * C
        if fits < C:
            raise ValueError(
                f"{fixed / 2**30:.1f} GiB of weights and one {C}-position chunk "
                f"do not fit a {budget / 2**30:.1f} GiB budget"
            )
        logger.warning(
            "max_seq_len %d, not the native %d: the model would hold %.1f GiB "
            "there, past this host's %.1f GiB budget (physical memory less %.0f "
            "GiB); --max-seq-len asks for up to %d",
            fits,
            native,
            need / 2**30,
            budget / 2**30,
            HOST_RESERVE / 2**30,
            native,
        )
        return dataclasses.replace(config, max_seq_len=fits)

    def cpu_reference(self):
        """What the model is judged by: with drawn weights, its own graph on
        the host (``OnHost``); else ``hugging_face``'s logits, recorded
        beside the checkpoint (``golden.npz``) from its ``config.json`` and
        its tensors (``Checkpoint.fingerprint``).
        """
        if self.seed is not None:

            class Host(OnHost, type(self)):
                pass

            return Host(self.config, self.weights)
        directory = Path(self.checkpoint.path).parent
        return Golden(
            directory / "golden.npz",
            lambda: self.hugging_face.load(directory),
            ((directory / "config.json").read_text(), self.checkpoint.fingerprint()),
        )

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, tokenized.

        With no tokenizer, ``chars // 3`` tokens drawn at ``seed`` and
        ``skip``: a little more than the text encodes to (Llama 3's
        tokenizer takes 3.7 characters a token), so a check sized in
        characters runs at about its size on the text.
        """
        if self.tokenizer is None:
            rng = np.random.default_rng((self.seed, skip))
            draw = rng.integers(0, self.config.vocab_size, chars // 3 - 1)
            return [self.bos, *draw]
        return self.tokenizer(prompt_text(chars, skip))

    def sanitize(self, w):
        """The checkpoint's layer module ``w``, after ``renames``, as its
        config's ``layer`` reads it (mlx-lm's ``sanitize``); ``w`` itself by
        default.
        """
        return w

    def shapes(self) -> list[dict]:
        """The input shapes of each version."""
        raise NotImplementedError(f"{type(self).__name__} defines no shapes()")

    def load_versions(
        self,
        *,
        release: Callable[[np.ndarray], None] | None = None,
        full_elf: bool | None = None,
        dev=None,
    ) -> "Model":
        """Compile and load every version before the first call, in one
        arena, then hand them to ``loaded``.

        Args:
            release: Given each piece of each weight once it is on the device.
            full_elf: Each version's packaging (``Graph.compile``).
            dev: The device every version compiles for, else the current one.
        """
        if dev is None:
            dev = require_device()
        compiled, decode = [], None
        for shapes in self.shapes():
            prompt = "ids" in shapes or "placed" in shapes
            version = self.compile(
                dev=dev, feeds=decode if prompt else None, full_elf=full_elf, **shapes
            )
            version.load(release=release)
            if not shapes and version.emit is not None:
                decode = version
            compiled.append(version)
        self.loaded(compiled)
        return self

    def loaded(self, versions: list) -> None:
        """What runs on ``versions``, in ``shapes()``'s order, once
        ``load_versions`` has them: nothing by default.
        """

    def __repr__(self) -> str:
        config = getattr(self, "config", None)
        fields = [] if config is None else [type(config).__name__]
        if hasattr(config, "max_seq_len"):
            fields.append(f"max_seq_len={config.max_seq_len}")
        loaded = self._versions and all(v.is_loaded for v in self._versions.values())
        fields.append("loaded" if loaded else "not loaded")
        return f"{self.name}({', '.join(fields)})"


class OnHost:
    """A model with its images stood in by its graph's reference
    (``Graph.reference``), run at whatever shape it is called with: the
    model with no device, mixed in before the model's own class. It
    compiles nothing, and ``generate`` draws on the host.
    """

    def __call__(self, *tensors, **values):
        logits, carry = self.reference(*tensors, **values)
        return _HostOutput(logits), carry

    def load_versions(self, *, release=None, full_elf=None, dev=None) -> "OnHost":
        return self

    def generate(self, tokens, num_tokens: int, sample: Sampler):
        return generate_on_host(self, tokens, num_tokens, sample)


class _HostOutput:
    """What an image returns: a buffer read with ``numpy()``."""

    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array
