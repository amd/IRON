# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model``, a model's graph, every version compiled and loaded before
the first call, built from a checkpoint's files (``load``), which generates
from a prompt; ``OnHost``, the model with no device; and ``Tokenizer``, a
prompt's text to its ids.
"""

import dataclasses
import functools
import json
import logging
import math
import os
import time
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import ClassVar

import numpy as np

import iron
from iron.common.image.packaging import require_device

from .checkpoint import Checkpoint
from .config import Config, DecoderConfig
from .golden import Golden, HuggingFace
from .generation import Sampler

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
    ``Model.open_tokenizer`` gives. ``chat_template`` is the checkpoint's
    own, from its ``tokenizer_config.json``, if it has one.
    """

    def __init__(self, encoding, bos: int, chat_template: str | None = None):
        self.encoding, self.bos = encoding, bos
        self.chat_template = chat_template

    def __call__(self, text: str) -> list[int]:
        return [self.bos, *self.encoding.encode(text)]

    def decode(self, tokens) -> str:
        return self.encoding.decode(list(tokens))

    def chat(self, messages: list[dict]) -> list[int]:
        """The ids of ``messages``, each ``{"role": ..., "content": ...}``,
        as ``chat_template`` renders them (with jinja2, the ``models``
        extra), the assistant's turn opened after them. The special tokens
        the text names are their ids, and ``bos`` is first, once.

        Raises:
            ValueError: The checkpoint has no chat template.
            ImportError: jinja2 is not installed.
            jinja2.TemplateError: The template refuses ``messages``
                (its ``raise_exception``).
        """
        if self.chat_template is None:
            raise ValueError(
                "the checkpoint's tokenizer_config.json has no chat_template"
            )
        try:
            from jinja2 import TemplateError
            from jinja2.sandbox import ImmutableSandboxedEnvironment
        except ImportError as e:
            raise ImportError(
                "a chat template renders with jinja2: pip install 'iron[models]'"
            ) from e

        def raise_exception(message):
            raise TemplateError(message)

        env = ImmutableSandboxedEnvironment(
            trim_blocks=True, lstrip_blocks=True, extensions=["jinja2.ext.loopcontrols"]
        )
        template = env.from_string(self.chat_template)
        text = template.render(
            messages=messages,
            add_generation_prompt=True,
            bos_token="",
            raise_exception=raise_exception,
        )
        ids = self.encoding.encode(text, allowed_special="all")
        return ids if ids[:1] == [self.bos] else [self.bos, *ids]


class _TokenizerJson:
    """A Hugging Face ``tokenizer.json``, over ``tokenizers`` (not
    ``transformers``): text to token ids without the special tokens its
    post-processor adds, since ``Tokenizer`` puts the BOS first, and back.
    """

    def __init__(self, path):
        import tokenizers

        self._tokenizer = tokenizers.Tokenizer.from_file(str(path))

    def encode(self, text: str, allowed_special="all") -> list[int]:
        """``text``'s ids, each added token it names its own id, which
        ``allowed_special`` (tiktoken's keyword) cannot turn off.
        """
        return self._tokenizer.encode(text, add_special_tokens=False).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(tokens)


@dataclasses.dataclass(frozen=True)
class Stats:
    """A generation's timings: the seconds to the first token, and the
    tokens per second after it (NaN for one token).
    """

    ttft: float
    tokens_per_s: float


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
    speed, accuracy and determinism need neither. ``stats`` are the last
    generation's timings.
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
    stats: Stats | None = None

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
            # A directory laid out by hand may hold it at its top.
            if not tokenizer.exists():
                tokenizer = directory / tokenizer.name
            settings = directory / "tokenizer_config.json"
            template = None
            if settings.exists():
                template = json.loads(settings.read_text()).get("chat_template")
            encoding = cls.open_tokenizer(tokenizer)
            model.tokenizer = Tokenizer(encoding, model.bos, template)
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

    def generate(
        self, prompt, max_tokens: int, sampler: Sampler | None = None, **inputs
    ):
        """``stream``'s pieces joined: the text drawn after a text prompt or
        chat messages, else the token ids drawn.
        """
        pieces = list(self._stream(prompt, max_tokens, sampler, inputs, False))
        return "".join(pieces) if _is_text(prompt) else pieces

    def stream(
        self, prompt, max_tokens: int, sampler: Sampler | None = None, **inputs
    ) -> Iterator:
        """Draw ``max_tokens`` after ``prompt``, each yielded as it is drawn,
        and its timings into ``stats`` once the last is.

        Args:
            prompt: Text, tokenized; a list of chat messages, each
                ``{"role": ..., "content": ...}``, rendered by the
                checkpoint's chat template (``Tokenizer.chat``); or token ids.
                Text and messages yield text, each piece once its characters
                are whole; ids yield ids.
            max_tokens: How many tokens to draw.
            sampler: How each is drawn; None is greedy.
            inputs: What the model takes beside the tokens
                (``Multimodal``'s ``raw``).

        Raises:
            RuntimeError: Text or messages, and no tokenizer.
        """
        return self._stream(prompt, max_tokens, sampler, inputs, True)

    def _stream(self, prompt, max_tokens, sampler, inputs, each: bool) -> Iterator:
        """``stream``'s pieces; with ``each`` False, ``generate``'s, which
        may come all at once, after the last is drawn (``_draw``).
        """
        self.stats = None
        text = _is_text(prompt)
        if text and self.tokenizer is None:
            raise RuntimeError(f"{type(self).__name__}: no tokenizer; give token ids")
        if not text:
            tokens = prompt
        elif isinstance(prompt, str):
            tokens = self.tokenizer(prompt)
        else:
            tokens = self.tokenizer.chat(prompt)
        sampler = Sampler(temperature=0) if sampler is None else sampler
        # The text of drawn[held:] is yet to be shown; drawn[seen:held] is
        # decoded with it, since a token's text can depend on the one before.
        drawn, seen, held = [], 0, 0
        began = first = last = time.perf_counter()
        for token in self._draw(tokens, max_tokens, sampler, each, **inputs):
            last = time.perf_counter()
            if not drawn:
                first = last
            drawn.append(token)
            if not text:
                yield token
                continue
            shown = self.tokenizer.decode(drawn[seen:held])
            piece = self.tokenizer.decode(drawn[seen:])[len(shown) :]
            # A token can end partway through a character; the next completes it.
            if not piece.endswith("\ufffd"):
                yield piece
                seen, held = held, len(drawn)
        if text and held < len(drawn):
            shown = self.tokenizer.decode(drawn[seen:held])
            yield self.tokenizer.decode(drawn[seen:])[len(shown) :]
        later = len(drawn) - 1
        rate = later / (last - first) if later else math.nan
        self.stats = Stats(first - began, rate)

    def sanitize(self, w):
        """The checkpoint's layer module ``w``, after ``renames``, as its
        config's ``layer`` reads it (mlx-lm's ``sanitize``); ``w`` itself by
        default.
        """
        return w

    def shapes(self) -> list[dict]:
        """The input shapes of each version, the decode step (no input)
        first: a later version on token ids (``ids`` or ``placed``) feeds
        off it where it is a full ELF, its Emit starting there.
        """
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
        fields = []
        if hasattr(config, "max_seq_len"):
            fields.append(f"max_seq_len={config.max_seq_len}")
        loaded = self._versions and all(v.is_loaded for v in self._versions.values())
        fields.append("loaded" if loaded else "not loaded")
        return f"{self.name}({', '.join(fields)})"


def _is_text(prompt) -> bool:
    """Whether ``prompt`` is text or chat messages, not token ids."""
    if isinstance(prompt, str):
        return True
    return isinstance(prompt, list) and isinstance(next(iter(prompt), None), dict)


class OnHost:
    """A model with its images stood in by its graph's reference
    (``Graph.reference``), run at whatever shape it is called with: the
    model with no device, mixed in before the model's own class. It
    compiles nothing, and ``generate`` draws on the host.
    """

    def _draw(self, tokens, max_tokens: int, sampler: Sampler, each=True):
        history = [int(t) for t in tokens]
        for _ in range(max_tokens):
            history.append(sampler(self.logits(history)))
            yield history[-1]

    def __call__(self, *tensors, **values):
        logits, carry = self.reference(*tensors, **values)
        return _HostOutput(logits), carry

    def load_versions(self, *, release=None, full_elf=None, dev=None) -> "OnHost":
        return self


class _HostOutput:
    """What an image returns: a buffer read with ``numpy()``."""

    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array
