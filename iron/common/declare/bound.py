# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an instance's member attribute returns, and the resolvers behind it.

A declaration is class-level and symbolic; binding it to an instance turns
every :class:`~iron.common.declare.field.DimRef` into an integer, which is
what the resolvers at the foot of this module do.
"""

from __future__ import annotations

from dataclasses import Field
from typing import TYPE_CHECKING, Any, Iterator

import numpy as np

from .field import DeclarationError, DimRef, Incompatible, _Optional, _Select
from .member import Resident, Shim, _Buffer, _Stream, _Value

if TYPE_CHECKING:
    from .operator import Operator
    from .overlay import Overlay


class BoundStream:
    """A stream on an overlay instance: concrete tile, count, and fifo handles.

    Resolved lazily, because a tile or a ``per=`` count may name a tunable
    that is ``None`` until :meth:`Overlay.tuned` fills it.
    """

    def __init__(self, member: _Stream, overlay: "Overlay") -> None:
        self.member = member
        self.overlay = overlay
        self.name = member.name
        self.direction = member.direction
        self.broadcast = member.broadcast
        self.replicate = member.replicate
        self.depth = member.depth
        self.via = member.via
        self._handle_slots: list[Any] | None = None

    def _resolve(self, spec) -> int:
        try:
            return _resolve_dim(spec, self.overlay)
        except Incompatible as e:
            raise Incompatible(
                f"stream {self.name!r}: {e}. Tune the overlay first (tuned(dev))"
            ) from None

    @property
    def shape(self) -> tuple[int, ...]:
        return tuple(self._resolve(d) for d in self.member.dims)

    @property
    def dtype(self):
        return _resolve_dtype(self.member.dtype, self.overlay)

    @property
    def count(self) -> int:
        if self.member.per is None:
            return 1
        n = 1
        for ref in self.member.per:
            n *= int(self._resolve(ref))
        return n

    @property
    def _handles(self) -> list[Any]:
        if self._handle_slots is None:
            self._handle_slots = [None] * self.count
        return self._handle_slots

    @property
    def tile(self):
        """The ObjectFifo element type: ``np.ndarray[shape, dtype]``."""
        return np.ndarray[self.shape, np.dtype[self.dtype]]  # type: ignore[misc]

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape))

    def bind(self, handle, index: int = 0) -> None:
        """Bind the shim end of a fifo to this stream (or to one of its slots)."""
        if self._handles[index] is not None:
            raise ValueError(f"stream {self.name!r}[{index}] is already bound")
        self._handles[index] = handle

    def __getitem__(self, index: int) -> "_StreamSlot":
        if not 0 <= index < self.count:
            raise IndexError(f"stream {self.name!r} has {self.count} slots")
        return _StreamSlot(self, index)

    def __iter__(self) -> Iterator["_StreamSlot"]:
        return (self[i] for i in range(self.count))

    def __len__(self) -> int:
        return self.count

    @property
    def handle(self):
        if self.count != 1:
            raise ValueError(f"stream {self.name!r} is per-{self.count}; index it")
        return self._require(0)

    @property
    def handles(self) -> list[Any]:
        return [self._require(i) for i in range(self.count)]

    def pin(self, index: int = 0) -> Shim | None:
        """The declared shim endpoint of slot ``index``, if pinned."""
        via = self.via
        if via is None:
            return None
        if isinstance(via, Shim):
            return via if self.count == 1 else None
        return via[index]

    def _require(self, index: int):
        h = self._handles[index]
        if h is None:
            raise ValueError(
                f"stream {self.name!r}[{index}] was never bound: the overlay's "
                f"design() must call .bind() on every declared stream"
            )
        return h

    def __repr__(self) -> str:
        return f"<{self.direction} stream {self.name} {self.shape} x{self.count}>"


class _StreamSlot:
    __slots__ = ("stream", "index")

    def __init__(self, stream: BoundStream, index: int) -> None:
        self.stream = stream
        self.index = index

    def bind(self, handle) -> None:
        self.stream.bind(handle, self.index)

    @property
    def handle(self):
        return self.stream._require(self.index)

    @property
    def name(self) -> str:
        return f"{self.stream.name}{self.index}"

    @property
    def shim(self) -> Shim | None:
        return self.stream.pin(self.index)


class BoundBuffer:
    """A buffer on an operator instance: concrete shape and dtype."""

    def __init__(self, member: _Buffer, op: "Operator") -> None:
        self.member = member
        self._op = op
        self.name = member.name
        self.direction = member.direction
        self.to = member.to
        self.from_ = member.from_

    # Resolved on use, not at construction: a shape or dtype may follow a
    # tunable the device fills (flm/gemm's B layout), and an operator on an
    # untuned overlay is still a valid thing to hold.
    @property
    def shape(self) -> tuple[int, ...]:
        return _resolve_shape(self.member.dims, self._op)

    @property
    def dtype(self):
        return _resolve_dtype(self.member.dtype, self._op)

    @property
    def elements(self) -> int:
        return int(np.prod(self.shape)) if self.shape else 1

    @property
    def nbytes(self) -> int:
        return self.elements * np.dtype(self.dtype).itemsize

    @property
    def flat_type(self):
        """The runtime-sequence argument type: the buffer flattened to 1-D."""
        return np.ndarray[(self.elements,), np.dtype[self.dtype]]  # type: ignore[misc]

    def stream(self, overlay: "Overlay") -> BoundStream | None:
        """The bound stream this buffer feeds or drains on ``overlay``."""
        member = self.to if self.direction == "in" else self.from_
        if member is None:
            return None
        return getattr(overlay, member.name)

    @property
    def batch_axes(self) -> int:
        """Leading ``optional()`` dimensions that are present on this instance."""
        n = 0
        for d in self.member.dims:
            if not isinstance(d, _Optional):
                break
            if _resolve_dim(d.ref, self._op) > 1:
                n += 1
        return n

    def __getitem__(self, index) -> "BufferView":
        """A basic slice of this buffer, for ``rt.fill``/``rt.drain`` in an override.

        A slice start may be a :class:`Scratchpad` value, in which case the
        transfer's base address is patched per call.
        """
        return BufferView(self, index)

    def __repr__(self) -> str:
        return (
            f"<{self.direction} {self.name} {self.shape} {np.dtype(self.dtype).name}>"
        )


class BufferView:
    """``buffer[index]``: a slice of a bound buffer, resolved to a transfer by the build."""

    def __init__(self, buffer: BoundBuffer, index) -> None:
        self.buffer = buffer
        self.index = index if isinstance(index, tuple) else (index,)
        self.offset_by: BoundValue | None = None
        static = []
        for idx in self.index:
            if isinstance(idx, slice) and isinstance(idx.start, BoundValue):
                if idx.stop is not None or idx.step is not None:
                    raise ValueError(
                        f"{buffer.name}[{idx}]: a per-call start takes the whole axis"
                    )
                if self.offset_by is not None:
                    raise ValueError(
                        f"{buffer.name}: only one axis may start at a per-call value"
                    )
                if idx.start.kind != "scratchpad":
                    raise ValueError(
                        f"{buffer.name}: {idx.start.name} is {idx.start.kind}; only a "
                        f"Scratchpad value can move a transfer's base address"
                    )
                self.offset_by = idx.start
                static.append(slice(None))
            else:
                static.append(idx)
        self.static_index = tuple(static)

    def pattern(self) -> tuple[int, list[int], list[int]]:
        """``(offset, sizes, strides)`` of the static part of the slice."""
        from ..tiling import view

        return view(self.buffer.shape, self.static_index)

    def __repr__(self) -> str:
        return f"{self.buffer.name}[{self.index}]"


class BoundValue:
    """A per-call value on an operator (or, for a core-read Scratchpad, an overlay).

    On a full ELF ``param`` is the upstream ``ScratchpadParameter`` the
    build creates. On an image without a scratchpad (xclbin, spike S2) the
    value is lowered as a dispatch-time scalar of the sequence: ``param`` is
    the dispatch parameter, ``ssa`` its live value inside the sequence body,
    an offset use adds it to the transfer's offset, and a core-read use is a
    resident the preamble writes from it (``bind``, as a Resident binds).
    """

    def __init__(self, member: _Value, owner) -> None:
        self.member = member
        self.name = member.name
        self.kind = member.kind
        self.dtype = member.dtype
        self.param = None  # the upstream ScratchpadParameter, set by the build
        self.symbol: str | None = None
        self.ssa = None  # the sequence's scalar, when lowered at dispatch time
        self.targets: list[tuple[Any, int]] = []

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to one runtime-parameter buffer, or one per worker; the preamble
        writes ``[index]`` from the per-call value (an image without a scratchpad)."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<{self.kind} {self.name} {np.dtype(self.dtype).name}>"


class BoundResident:
    """A resident on an overlay instance; ``bind()`` names what the preamble writes."""

    def __init__(self, member: Resident, overlay: "Overlay") -> None:
        self.member = member
        self.name = member.name
        self.dtype = member.dtype
        self.address = member.address
        self.lock = member.lock
        self.optional = member.optional
        self.targets: list[tuple[Any, int]] = []

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to one runtime-parameter buffer, or one per worker; the preamble writes ``[index]``."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    def __repr__(self) -> str:
        return f"<resident {self.name} {np.dtype(self.dtype).name}>"


# --------------------------------------------------------------------------
# Resolution
# --------------------------------------------------------------------------


def _lookup_ref(ref: DimRef, instance) -> Any:
    """Follow a DimRef from an instance: its own class, or its overlay's class."""
    if isinstance(instance, ref.owner):
        return getattr(instance, ref.name)
    ov = getattr(instance, "ov", None)
    if ov is not None and isinstance(ov, ref.owner):
        return getattr(ov, ref.name)
    raise DeclarationError(
        f"{ref!r} is not reachable from {type(instance).__name__}: a shape may "
        f"reference the class's own fields or its overlay's"
    )


def _resolve_dim(spec, instance) -> int:
    if isinstance(spec, bool):
        raise DeclarationError(f"{spec!r} is not a dimension")
    if isinstance(spec, (int, np.integer)):
        return int(spec)
    if isinstance(spec, DimRef):
        value = _lookup_ref(spec, instance)
        if value is None:
            raise Incompatible(
                f"{spec!r} is None; it must be set before the shape can be resolved"
            )
        return int(value)
    if isinstance(spec, Field):
        # A same-class reference the decorator did not rewrite: resolve by name.
        return int(getattr(instance, spec.name))
    raise DeclarationError(f"cannot resolve {spec!r} as a dimension")


def _flag_value(flag, instance) -> bool:
    if isinstance(flag, DimRef):
        value = _lookup_ref(flag, instance)
        if value is None:
            raise Incompatible(
                f"{flag!r} is None; a select() on it needs a tuned overlay"
            )
        return bool(value)
    if isinstance(flag, Field):
        return bool(getattr(instance, flag.name))
    return bool(flag)


def _resolve_shape(dims, instance) -> tuple[int, ...]:
    out: list[int] = []
    for d in dims:
        if isinstance(d, _Optional):
            n = _resolve_dim(d.ref, instance)
            if n > 1:
                out.append(n)
            continue
        if isinstance(d, _Select):
            branch = d.when_true if _flag_value(d.flag, instance) else d.when_false
            out.extend(_resolve_shape(branch, instance))
            continue
        out.append(_resolve_dim(d, instance))
    return tuple(out)


def _resolve_dtype(spec, instance):
    if isinstance(spec, DimRef):
        return _lookup_ref(spec, instance)
    if isinstance(spec, Field):
        return getattr(instance, spec.name)
    return spec
