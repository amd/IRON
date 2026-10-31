# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime parameters one generated core reads per call."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np
from aie.iron import Buffer, WorkerRuntimeBarrier
from aie.utils.compile.jit.params import PerCallMember

from .value import Value


class Block(PerCallMember):
    """A block of ``words`` words a core reads, written once per build.

    ``derive`` computes them from the operator. A shipped image's parameters
    are one.
    """

    def __init__(self, words: int, *, derive: Any) -> None:
        super().__init__(np.int32, derive, None)
        self.words = words


class Rtp(tuple):
    """The words one core reads per call: a buffer and scratchpad words.

    The sequence writes the buffer, then opens ``barrier`` on it. A tuple,
    so a Worker takes it as one argument whose leaves mlir-aie registers;
    the core calls ``read``.

    Attributes:
        slots: Each value the buffer holds and its first word there.
        buffer: None when every value is a scratchpad word.

    Raises:
        ValueError: A value of several words is read from the scratchpad,
            whose parameters are one word each.
    """

    values: tuple[Value, ...]
    slots: dict[Value, int]
    buffer: Buffer | None
    barrier: WorkerRuntimeBarrier

    def __new__(cls, values: Sequence[Value]) -> Rtp:
        slots, size = {}, 0
        for value in values:
            if not value.in_scratchpad:
                slots[value] = size
                size += value.words
            elif value.words != 1:
                raise ValueError(
                    f"{value.name} is {value.words} words, but a scratchpad "
                    f"parameter holds one"
                )
        buffer = (
            Buffer(np.ndarray[(size,), np.dtype[np.int32]], use_write_rtp=True)
            if size
            else None
        )
        barrier = WorkerRuntimeBarrier()
        params = [v.param for v in values if v.in_scratchpad]
        rtp = super().__new__(cls, (barrier, *([buffer] if size else []), *params))
        rtp.values = tuple(values)
        rtp.slots = slots
        rtp.buffer = buffer
        rtp.barrier = barrier
        return rtp

    def read(self) -> dict[Value, Any]:
        """Read each value's word (a list of them for a block), keyed by the value.

        In a core: wait for the sequence, read, re-arm.
        """
        self.barrier.wait_for_value(1)
        words: dict[Value, Any] = {}
        for value in self.values:
            if value.in_scratchpad:
                words[value] = value.param.read()
                continue
            at = self.slots[value]
            assert (
                self.buffer is not None
            ), "a slot exists, so some value is not scratchpad"
            block = [self.buffer[at + i] for i in range(value.words)]
            words[value] = block if value.words > 1 else block[0]
        self.barrier.release_with_value(1)
        return words

    def write(self, words: Mapping[str, Any]) -> None:
        """Write the words of each value the buffer holds, by value name.

        Called in the preamble: a resident's number, or an xclbin's per-call
        scalar.

        Raises:
            ValueError: A value is given another number of words than it declares.
        """
        for value, at in self.slots.items():
            word = words[value.name]
            block = word if isinstance(word, (list, tuple)) else [word]
            if len(block) != value.words:
                raise ValueError(
                    f"{value.name} holds {value.words} words; it was given "
                    f"{len(block)}"
                )
            assert (
                self.buffer is not None
            ), "a slot exists, so some value is not scratchpad"
            for i, w in enumerate(block):
                self.buffer[at + i] = w
