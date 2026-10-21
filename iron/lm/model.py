# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model``, a model's graph, every version compiled and loaded before
the first call, built from a checkpoint's files (``load``), which generates
from a prompt; ``OnHost``, the model with no device; and ``Tokenizer``, a
prompt's text to its ids.
"""

import dataclasses
import datetime
import functools
import importlib
import json
import logging
import math
import os
import time
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Self, cast

import numpy as np

import iron
from iron.common.image.packaging import require_device

from .checkpoint import Checkpoint, weights_file
from .config import Config, DecoderConfig
from .golden import Golden, HuggingFace
from .generation import Sampler

logger = logging.getLogger(__name__)


# What a host keeps beside a model's arena: the OS, Python and XRT, the
# checkpoint's pages as they upload, a test's host copies.
HOST_RESERVE = 8 << 30

# What this process itself keeps beside the arena, inside a cgroup that
# already excludes the rest of the host: the interpreter, aie.utils and a
# bound device cost 130 MB RSS; a small operator's compile, 183 MB; with
# torch and transformers imported too, as a golden-recording test does,
# 337 MB. Rounded up with margin for a bigger compile or several xdist
# workers.
CGROUP_RESERVE = 512 << 20


def _cgroup_limit() -> int | None:
    """This process's cgroup memory ceiling: cgroup v2's ``memory.max``,
    the lowest one set from its own cgroup up to the root, or else v1's
    ``memory.limit_in_bytes``; ``None`` where neither bounds it (no cgroup
    mounted, or every level reads ``max``).
    """
    root = Path("/sys/fs/cgroup")
    unified = (root / "cgroup.controllers").exists()
    try:
        lines = Path("/proc/self/cgroup").read_text().splitlines()
    except FileNotFoundError:
        return None
    own = None
    for line in lines:
        _, controllers, path = line.split(":", 2)
        if (controllers == "") if unified else ("memory" in controllers.split(",")):
            own = path
            break
    if own is None:
        return None
    name, base = (
        ("memory.max", root) if unified else ("memory.limit_in_bytes", root / "memory")
    )
    limits, path = [], own
    while True:
        try:
            text = (base / path.lstrip("/") / name).read_text().strip()
        except OSError:
            text = "max"
        if text != "max":
            limits.append(int(text))
        if path in ("", "/"):
            break
        path = str(Path(path).parent)
    return min(limits) if limits else None


def host_budget() -> int:
    """The bytes a model's arena may take here: physical memory less
    ``HOST_RESERVE`` (the rest of the host), or a cgroup's lower ceiling
    less ``CGROUP_RESERVE`` (this process's own, a cgroup already
    excluding the rest of the host) where one bounds this process (a
    container, or a job's own, as CI's self-hosted runners and a capped
    test both impose with systemd).
    """
    phys = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") - HOST_RESERVE
    limit = _cgroup_limit()
    return phys if limit is None else min(phys, limit - CGROUP_RESERVE)


def prompt_text(chars: int, skip: int = 0) -> str:
    """``chars`` characters of ``prompt.txt``, from ``skip`` on: the text every
    model's long inputs are drawn from.
    """
    return Path(__file__).with_name("prompt.txt").read_text()[skip : skip + chars]


def _models_extra(name: str):
    """Import ``name``, one of the packages of IRON's ``models`` extra.

    Raises:
        ImportError: ``name`` is not installed; the message says how to install it.
    """
    try:
        return importlib.import_module(name)
    except ImportError as e:
        raise ImportError(
            f"{name} is in IRON's models extra: pip install -e '.[models]' "
            "from an IRON checkout"
        ) from e


class Tokenizer:
    """Text to a prompt's token ids, ``bos`` first, and token ids back to
    text, over ``encoding``: anything with ``encode`` and ``decode``, as
    ``TokenizerJson`` gives. ``chat_template`` is the checkpoint's
    own, from its ``tokenizer_config.json`` or ``chat_template.jinja``, if
    it has one, and ``bos_token`` the text it writes for ``bos_token``
    (``bos``'s own text when None).
    """

    def __init__(
        self,
        encoding,
        bos: int,
        chat_template: str | None = None,
        bos_token: str | None = None,
    ):
        self.encoding, self.bos = encoding, bos
        self.chat_template, self.bos_token = chat_template, bos_token

    def __call__(self, text: str) -> list[int]:
        return [self.bos, *self.encoding.encode(text)]

    def decode(self, tokens) -> str:
        return self.encoding.decode(list(tokens))

    def chat(self, messages: list[dict]) -> list[int]:
        """The ids of ``messages``, each ``{"role": ..., "content": ...}``,
        as ``chat_template`` renders them (with jinja2, the ``models``
        extra), the assistant's turn opened after them. The special tokens
        the text names are their ids; ``bos`` is there only where the
        template writes it, as transformers' ``apply_chat_template`` has it.

        Raises:
            ValueError: The checkpoint has no chat template.
            ImportError: jinja2 is not installed.
            jinja2.TemplateError: The template refuses ``messages``
                (its ``raise_exception``).
        """
        if self.chat_template is None:
            raise ValueError("the checkpoint has no chat template")
        _models_extra("jinja2")
        from jinja2 import TemplateError

        def raise_exception(message):
            raise TemplateError(message)

        text = _chat_template(self.chat_template).render(
            messages=messages,
            add_generation_prompt=True,
            bos_token=(
                self.encoding.token(self.bos)
                if self.bos_token is None
                else self.bos_token
            ),
            raise_exception=raise_exception,
            strftime_now=lambda f: datetime.datetime.now().strftime(f),
        )
        return self.encoding.encode(text)


@functools.lru_cache(maxsize=8)
def _chat_template(source: str):
    """``source`` compiled once, in jinja2's sandbox, as transformers sets it up."""
    from jinja2.sandbox import ImmutableSandboxedEnvironment

    env = ImmutableSandboxedEnvironment(
        trim_blocks=True, lstrip_blocks=True, extensions=["jinja2.ext.loopcontrols"]
    )
    return env.from_string(source)


class TokenizerJson:
    """A Hugging Face ``tokenizer.json``, over ``tokenizers`` (not
    ``transformers``): text to token ids without the special tokens its
    post-processor adds, since ``Tokenizer`` puts the BOS first, and back.
    """

    def __init__(self, path):
        tokenizers = _models_extra("tokenizers")
        self._tokenizer = tokenizers.Tokenizer.from_file(str(path))

    def encode(self, text: str) -> list[int]:
        """``text``'s ids, each added token it names its own id."""
        return self._tokenizer.encode(text, add_special_tokens=False).ids

    def decode(self, tokens) -> str:
        return self._tokenizer.decode(tokens)

    def token(self, id: int) -> str | None:
        """The text of token ``id``."""
        return self._tokenizer.id_to_token(id)


@dataclasses.dataclass(frozen=True)
class Stats:
    """A generation's timings: the seconds to the first token, and the
    tokens per second after it (NaN for one token).
    """

    ttft: float
    tokens_per_s: float


class Model(iron.Graph):
    """A model compiled as several versions of one graph, one per input shape.

    ``shapes()`` lists the versions, the decode step (no input) first.
    ``load_versions()`` compiles and loads all of them before the first
    call, so the device arena is allocated once, and ``versions``
    (``Graph``'s own) holds them in ``shapes()``'s order. When the decode
    step is a full ELF, a version on token ids (``ids`` or ``placed``)
    hands off to it directly: its Emit step starts the decode step.

    A subclass sets ``config`` to the ``Config`` class that reads
    ``config.json``, or to one fixed shape. ``load`` sets ``checkpoint`` and
    ``tokenizer`` on the instance, and ``random_weights``, the seed, when the
    weights are drawn at random. Then a prompt without a tokenizer is random tokens,
    so speed, accuracy and determinism can be checked without real weights.
    ``stats`` holds the last generation's timings.
    """

    # Renames applied to the checkpoint's tensor names before loading: each
    # key is a run of dotted name parts, matched anywhere in a name, and its
    # value is the name the model's modules use instead.
    renames: ClassVar[dict[str, str]] = {}
    # What loads the checkpoint into transformers to record its goldens.
    hugging_face: type = HuggingFace
    checkpoint: Checkpoint | None = None
    random_weights: int | None = None
    tokenizer: Tokenizer | None = None
    stats: Stats | None = None
    # Set by a subclass. On the class, config is the Config class or one
    # shape; on an instance, it is the instance's shape. weights is the tree
    # of weights the instance holds.
    config: Any
    weights: Any

    if TYPE_CHECKING:  # a subclass's: the constructor and the draw

        def __init__(self, config: Any, weights: Any) -> None: ...

        def _draw(self, *args, **kwargs) -> Iterator[int]: ...

    @classmethod
    def load(
        cls,
        path,
        *,
        random_weights: int | None = None,
        max_seq_len: int | None = None,
        full_elf: bool | None = None,
    ) -> "Model":
        """``from_checkpoint``'s model compiled and loaded, weights uploaded;
        ``full_elf`` is every version's packaging (``load_versions``).
        """
        model = cls.from_checkpoint(
            path, random_weights=random_weights, max_seq_len=max_seq_len
        )
        assert model.checkpoint is not None, "from_checkpoint gives it one"
        return model.load_versions(release=model.checkpoint.release, full_elf=full_elf)

    @classmethod
    def from_checkpoint(
        cls, path, *, random_weights: int | None = None, max_seq_len: int | None = None
    ) -> "Model":
        """The model of a Hugging Face repository's files, not yet loaded,
        its context ``max_seq_len`` or else fitted to this host (``fit``).

        Args:
            path: A directory holding ``config.json``, ``model.safetensors``
                or a sharded one's ``model.safetensors.index.json``, and
                ``tokenizer.json``; or a repository's id, those files
                downloaded to Hugging Face's cache.
            random_weights: A seed: in place of the checkpoint's weights and
                its tokenizer, weights drawn at it in its shapes (only its header is
                read).
            max_seq_len: The longest context served, prompt and generated
                tokens together, at most the checkpoint's own.

        Raises:
            ValueError: ``max_seq_len`` is past the checkpoint's own.
        """
        directory = Path(path)
        if not directory.is_dir():
            snapshot_download = _models_extra("huggingface_hub").snapshot_download
            files = [
                "*config.json",
                "model*.safetensors*",
                "tokenizer.json",
                "chat_template.jinja",
            ]
            directory = Path(snapshot_download(str(path), allow_patterns=files))
        weights = weights_file(directory)
        config = cls.default_config(weights)
        if max_seq_len is None:
            config = cls.fit(config, weights)
        else:
            assert isinstance(config, DecoderConfig), "a context is a decoder's"
            if max_seq_len > config.max_seq_len:
                raise ValueError(
                    f"max_seq_len {max_seq_len} is past the model's "
                    f"{config.max_seq_len}"
                )
            config = dataclasses.replace(config, max_seq_len=max_seq_len)
        checkpoint = Checkpoint(weights)
        tree = (
            checkpoint.tree()
            if random_weights is None
            else checkpoint.tree("random", random_weights)
        )
        model = cls(config, tree)
        model.checkpoint, model.random_weights = checkpoint, random_weights
        if random_weights is None:
            settings = directory / "tokenizer_config.json"
            jinja = directory / "chat_template.jinja"
            found = json.loads(settings.read_text()) if settings.exists() else {}
            template = found.get("chat_template")
            if template is None and jinja.exists():
                template = jinja.read_text()
            # transformers renders tokenizer_config.json's bos_token, which
            # may be null (nothing) or an added token's record.
            bos_token = None
            if "bos_token" in found:
                b = found["bos_token"]
                bos_token = (b["content"] if isinstance(b, dict) else b) or ""
            encoding = TokenizerJson(directory / "tokenizer.json")
            model.tokenizer = Tokenizer(encoding, model.bos, template, bos_token)
        return model

    @functools.cached_property
    def bos(self) -> int:
        """The token every prompt starts with: the checkpoint's
        ``bos_token_id``, from its ``config.json`` or else its
        ``generation_config.json``, unless a subclass names it.
        """
        if self.checkpoint is None:
            raise KeyError(f"{self.name} has no checkpoint: name the model's bos")
        directory = Path(self.checkpoint.path).parent
        for name in ("config.json", "generation_config.json"):
            path = directory / name
            if path.exists():
                bos = json.loads(path.read_text()).get("bos_token_id")
                if bos is not None:
                    return bos
        raise KeyError(f"{directory} names no bos_token_id: name the model's bos")

    @functools.cached_property
    def eos(self) -> set[int]:
        """The tokens generation stops at: the checkpoint's ``eos_token_id``,
        one or a list, from its ``generation_config.json`` or else its
        ``config.json``; none without a checkpoint or either.
        """
        if self.checkpoint is None:
            return set()
        directory = Path(self.checkpoint.path).parent
        for name in ("generation_config.json", "config.json"):
            path = directory / name
            if path.exists():
                eos = json.loads(path.read_text()).get("eos_token_id")
                if eos is not None:
                    return set(eos) if isinstance(eos, list) else {eos}
        return set()

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
        recording its decode step at one and two prompt chunks of context:
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
            held.append(sum(model.record(**model.shapes()[0]).pinned.values()))
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
        if self.random_weights is not None:

            class Host(OnHost, type(self)):
                pass

            return Host(self.config, self.weights)
        assert self.checkpoint is not None, "a model without drawn weights loaded one"
        directory = Path(self.checkpoint.path).parent
        return Golden(
            directory / "golden.npz",
            lambda: self.hugging_face.load(directory),
            ((directory / "config.json").read_text(), self.checkpoint.fingerprint()),
        )

    def prompt(self, chars: int, skip: int = 0) -> list[int]:
        """``chars`` characters of ``prompt.txt`` from ``skip`` on, tokenized.

        With no tokenizer, ``chars // 3`` tokens drawn at the weights' seed and
        ``skip``: a little more than the text encodes to (Llama 3's
        tokenizer takes 3.7 characters a token), so a check sized in
        characters runs at about its size on the text.
        """
        if self.tokenizer is None:
            assert (
                self.random_weights is not None
            ), "without a tokenizer, weights drawn at random"
            rng = np.random.default_rng((self.random_weights, skip))
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
        """Draw up to ``max_tokens`` after ``prompt``, each yielded as it is
        drawn, through the first of ``eos`` drawn, and its timings into
        ``stats`` once the last is.

        Args:
            prompt: Text, tokenized; a list of chat messages, each
                ``{"role": ..., "content": ...}``, rendered by the
                checkpoint's chat template (``Tokenizer.chat``); or token ids.
                Text and messages yield text, each piece once its characters
                are whole; ids yield ids.
            max_tokens: The most tokens to draw.
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
        # Read only for text, which has one.
        tokenizer = cast(Tokenizer, self.tokenizer)
        if not text:
            tokens = prompt
        elif isinstance(prompt, str):
            tokens = tokenizer(prompt)
        else:
            tokens = tokenizer.chat(prompt)
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
            else:
                shown = tokenizer.decode(drawn[seen:held])
                piece = tokenizer.decode(drawn[seen:])[len(shown) :]
                # A token can end partway through a character; the next completes it.
                if not piece.endswith("\ufffd"):
                    if piece:
                        yield piece
                    seen, held = held, len(drawn)
            if token in self.eos:
                break
        if text and held < len(drawn):
            shown = tokenizer.decode(drawn[seen:held])
            if piece := tokenizer.decode(drawn[seen:])[len(shown) :]:
                yield piece
        later = len(drawn) - 1
        rate = later / (last - first) if later else math.nan
        self.stats = Stats(first - began, rate)

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
    ) -> Self:
        """Compile every version, then load each, in one arena, and hand
        them to ``loaded``: every version is placed before the arena's
        buffers are made, so none grows them, which would copy them.

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
            if not shapes and version.emit is not None:
                decode = version
            compiled.append(version)
        for version in compiled:
            version.load(release=release)
        self.loaded(compiled)
        return self

    def loaded(self, versions: list) -> None:
        """What runs on ``versions``, in ``shapes()``'s order, once
        ``load_versions`` has them: nothing by default.
        """

    def __repr__(self) -> str:
        max_seq_len = getattr(getattr(self, "config", None), "max_seq_len", None)
        fields = []
        if max_seq_len is not None:
            fields.append(f"max_seq_len={max_seq_len}")
        loaded = self._versions and all(v.is_loaded for v in self._versions.values())
        fields.append("loaded" if loaded else "not loaded")
        return f"{self.name}({', '.join(fields)})"


def _is_text(prompt) -> bool:
    """Whether ``prompt`` is text or chat messages, not token ids."""
    if isinstance(prompt, str):
        return True
    return isinstance(prompt, list) and isinstance(next(iter(prompt), None), dict)


class OnHost:
    """A model with its versions stood in by its graph's reference
    (``Graph.reference``), run at whatever shape it is called with: the
    model with no NPU, tiled for the bound device, mixed in before the
    model's own class. It compiles nothing, and ``generate`` draws on the
    host.
    """

    if TYPE_CHECKING:  # the model's, mixed in after

        def logits(self, tokens) -> np.ndarray: ...

        def reference(self, *tensors, dev=None, **values) -> Any: ...

    def _draw(self, tokens, max_tokens: int, sampler: Sampler, each=True):
        history = [int(t) for t in tokens]
        for _ in range(max_tokens):
            history.append(sampler(self.logits(history)))
            yield history[-1]

    def __call__(self, *tensors, **values):
        logits, carry = self.reference(*tensors, **values)
        return _HostOutput(logits), carry

    def load_versions(self, *, release=None, full_elf=None, dev=None) -> Self:
        return self


class _HostOutput:
    """What a version returns: a buffer read with ``numpy()``."""

    def __init__(self, array):
        self.array = array

    def numpy(self):
        return self.array
