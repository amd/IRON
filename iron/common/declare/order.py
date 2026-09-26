# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The per-slot order a buffer moves through its stream in.

An :class:`Order` is the one statement of which elements of a host buffer
each slot of a stream carries, and in what sequence: the sequence issues it
and a fusion pass reads it. :meth:`Operator.order` returns it; the default
is :func:`derived`, and an operator whose ``design(rt)`` moves a buffer any
other way overrides ``order()`` to say how. The build checks that what a
sequence issued is exactly the declared order
(:meth:`iron.common.design.Transfers.run`).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np

from ..tiling import Access, encode, split, whole

if TYPE_CHECKING:
    from .bound import BoundBuffer, BoundStream, BoundValue


@dataclass(frozen=True)
class Order:
    """How one buffer moves through ``stream``: per slot, its transfers in issue order.

    ``slots[i]`` is what slot ``i`` of the stream carries, as the
    descriptors the sequence issues for it, oldest first. ``offset_by`` is a
    per-call value added to every descriptor's offset (a copy into a cache
    at a per-token position); the order is then fixed only up to that shift.
    """

    stream: "BoundStream"
    slots: tuple[tuple[Access, ...], ...]
    offset_by: "BoundValue | None" = None

    def __post_init__(self) -> None:
        name, count = self.stream.name, self.stream.count
        if len(self.slots) != count:
            raise ValueError(
                f"an order over stream {name!r} needs {count} slots, "
                f"got {len(self.slots)}"
            )
        # The stream's replicate flag is what the shim budget and a fusion
        # pass read; an order that says otherwise is the declaration lying
        # (GEMV's B was sent whole to every column of a stream declared split).
        if count > 1 and any(self.slots):
            same = all(s == self.slots[0] for s in self.slots)
            if same and not self.stream.replicate:
                raise ValueError(
                    f"stream {name!r} is not declared replicate=True, but this "
                    f"order gives each of its {count} slots the same transfers"
                )
            if self.stream.replicate and not same:
                raise ValueError(
                    f"stream {name!r} is declared replicate=True, but this order "
                    f"gives its slots different transfers"
                )

    def __getitem__(self, slot: int) -> tuple[Access, ...]:
        return self.slots[slot]

    @property
    def replicated(self) -> bool:
        """Every slot carries the whole buffer (a ``replicate=True`` stream)."""
        return self.stream.replicate

    @property
    def tile(self) -> int:
        """Elements in one fifo object of the stream."""
        return self.stream.elements

    def indices(self, slot: int) -> np.ndarray:
        """The flat buffer elements slot ``slot`` carries, in the order it carries them."""
        parts = [acc.indices() for acc in self.slots[slot]]
        return np.concatenate(parts) if parts else np.zeros(0, dtype=np.int64)


def derived(buffer: "BoundBuffer", stream: "BoundStream | None") -> Order:
    """The order the library derives when an operator declares none.

    A single-slot stream takes the whole buffer in one linear transfer, and
    a ``replicate`` stream takes it whole in every slot. Any other ``per=``
    stream splits the buffer's first non-batch axis into contiguous
    row-blocks, one per slot; leading batch axes become repeats, coalesced
    into one iterated descriptor when the slot rules allow and unrolled
    otherwise.
    """
    op = type(buffer._op).__name__
    if stream is None:
        member = "to=" if buffer.direction == "in" else "from_="
        raise ValueError(
            f"{op}.{buffer.name} names no stream ({member}), so its sequence "
            f"cannot be derived; add {member} or override order() and design(rt)"
        )
    if stream.count == 1 or stream.replicate:
        everything = tuple(encode(whole(buffer.shape), buffer.elements, buffer.dtype))
        return Order(stream, (everything,) * stream.count)
    axis = buffer.batch_axes
    if axis >= len(buffer.shape):
        raise ValueError(
            f"{buffer.name} {buffer.shape} has no axis to split across the "
            f"{stream.count} slots of stream {stream.name!r}"
        )
    try:
        blocks = split(buffer.shape, stream.count, axis)
    except ValueError as e:
        raise ValueError(
            f"{buffer.name} {buffer.shape} does not divide across stream "
            f"{stream.name!r}: {e}. Check {op}.compatible()"
        ) from None
    return Order(
        stream,
        tuple(tuple(encode(b, buffer.elements, buffer.dtype)) for b in blocks),
    )
