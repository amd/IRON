# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model``, a model's graph, every version compiled and loaded before
the first call, and ``OnHost``, the model with no device.
"""

from collections.abc import Callable
from typing import ClassVar

import numpy as np

import iron
from iron.common.image.packaging import require_device

from .generation import Sampler, generate_on_host


class Model(iron.Graph):
    """A model's graph, every version ``shapes()`` names compiled and
    loaded by ``load_versions()`` before the first call, so the arena is
    made once: a version on token ids (``ids`` or ``placed``) feeds off the
    decode step, the version with no input, where that is a full ELF, its
    Emit starting there. ``versions`` (``Graph``'s own), in ``shapes()``'s
    order, is every version ``load_versions()`` compiled.
    """

    # Each checkpoint layer's dotted paths that its config's ``layer``
    # reads under another name, by that name.
    renames: ClassVar[dict[str, str]] = {}

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
