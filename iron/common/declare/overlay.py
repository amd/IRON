# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The array-configuring half of a declaration.

An overlay fixes everything a change to which rebuilds the design: tile
shapes, column counts, dtypes, kernel flags. Its tunables start out ``None``
and :meth:`Overlay.tuning` fills them for a device, raising
:class:`~iron.common.declare.field.Untunable` when the device admits no legal
choice. :meth:`Overlay.design` writes the dataflow; an external overlay
declares :class:`~iron.common.declare.member.Xclbin` instead and supplies a
binary.
"""

from __future__ import annotations

import dataclasses
from math import prod
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar

from aie.dialects.aie import WireBundle, get_target_model
from aie.utils.verify import Tolerance

from .bound import BoundBuffer, BoundResident, BoundStream, BoundValue
from .field import Untunable
from .member import Resident, Xclbin, _Member, _Stream, _Value
from .naming import label_parts
from .order import Order
from .semantics import Local, Semantics, Undeclared

if TYPE_CHECKING:
    from ..design.target import Target
    from .operator import Operator


def get_shim_dma_limit(dev) -> int:
    """Return the total number of ShimDMA output channels available on the device.

    Each shim tile exposes a fixed number of DMA source connections; summing
    across all shim tiles gives the device-wide ShimDMA budget.
    """
    tm = get_target_model(dev.resolve())
    return sum(
        tm.get_num_source_shim_mux_connections(col, row, WireBundle.DMA)
        for col in range(tm.columns())
        for row in range(tm.rows())
        if tm.is_shim_noc_or_pl_tile(col, row)
    )


class Overlay:
    """What configures the array. Subclass, decorate with ``@operator``.

    Declare ``dim()`` and ``tunable()`` fields, streams, and residents in the
    class body; implement :meth:`tuning` to fill tunables from the device and
    :meth:`design` to build the array and bind each stream to a fifo's shim
    end. See the module docstring for the shape.
    """

    _members: ClassVar[tuple[_Member, ...]] = ()
    _dim_fields: ClassVar[tuple[str, ...]] = ()
    _tunable_fields: ClassVar[tuple[str, ...]] = ()
    _external: ClassVar[Xclbin | None] = None

    @property
    def external(self) -> Xclbin | None:
        """The downloaded image this overlay is, if IRON did not build it."""
        return type(self)._external

    # -- placement ---------------------------------------------------------

    @classmethod
    def shim_columns(cls, dev, num_channels: int = 1) -> int:
        """How many of ``dev``'s columns this overlay's shim budget allows.

        One core per (column, channel) fills one fifo per input stream from
        the shim and drains one per output, so a column costs
        ``max(inputs, outputs) * num_channels`` channels in the busier
        direction. A ``replicate`` stream is shared by every column of a
        channel, so it is paid once per channel rather than per column.
        """
        streams = [m for m in cls._members if isinstance(m, _Stream)]
        shared = [m for m in streams if m.replicate]
        per_core = [m for m in streams if not m.replicate]
        directions = [m.direction for m in per_core]
        cost = max(directions.count("in"), directions.count("out")) * num_channels
        fixed = len(shared) * num_channels
        limit = get_shim_dma_limit(dev)
        return max(1, min(dev.cols, (limit - fixed) // cost))

    def check_shim_columns(self, dev, cols: int, num_channels: int = 1) -> None:
        """Raise :class:`Untunable` if ``cols`` exceeds the shim budget."""
        allowed = type(self).shim_columns(dev, num_channels)
        if cols > allowed:
            raise Untunable(
                f"{type(self).__name__} with {cols} columns x {num_channels} "
                f"channels exceeds this device's shim DMA budget; "
                f"{allowed} columns fit"
            )

    # -- an overlay IRON does not design() ---------------------------------

    def prebuilt(self) -> Path:
        """The file the declared :class:`Xclbin` names, fetched if it is not
        already in the cache."""
        raise NotImplementedError(
            f"{type(self).__name__} declares an Xclbin but no prebuilt()"
        )

    def build(self, dev, op: "Operator"):
        """The MLIR module for ``op`` on this overlay, when ``design()`` does
        not build the array: a runtime sequence against the prebuilt image."""
        raise NotImplementedError(
            f"{type(self).__name__} declares an Xclbin but no build()"
        )

    # -- the sequence, when the overlay owns it -----------------------------

    def sequence(self, op: "Operator", rt) -> None:
        """The runtime sequence for ``op`` on this overlay, when the overlay
        rather than the operator knows it: a external image consumes its
        transfers in the order it was built for, whatever operator drives it.
        Takes precedence over the operator's ``design(rt)``."""
        raise NotImplementedError

    def order(self, op: "Operator", buffer: "BoundBuffer") -> "Order":
        """How ``buffer`` of ``op`` moves through its stream, on an overlay that
        owns the sequence (see :meth:`sequence`); :meth:`Operator.order` asks
        here first."""
        raise NotImplementedError(
            f"{type(self).__name__} owns its sequence but declares no order()"
        )

    @classmethod
    def has_sequence(cls) -> bool:
        return cls.sequence is not Overlay.sequence

    def resident_values(self, op: "Operator") -> dict[str, Any]:
        """The words for this overlay's residents, from ``op``. By default the
        operator's own ``residents()``; an external overlay lays the operator's
        values out into the block its image reads."""
        return op.residents()

    def __post_init__(self) -> None:
        self._tuned = False
        self._specialised: dict[str, Any] = {}
        self.validate()
        self._bind()

    # -- declared surface --------------------------------------------------

    def validate(self) -> None:
        """Check the compile-time fields. Runs at construction and after tuning."""

    def tuning(self, dev) -> "Overlay":
        """Return a copy with every tunable filled for ``dev``; raise :class:`Untunable`.

        Sees the device and nothing else, so a tuned overlay serves every
        extent. The default fills nothing.
        """
        return self

    def device(self, target):
        """The device the Program is built for; the current device by default.

        An overlay that builds for a column subset (gemm's NPU1Col1/NPU1Col2)
        returns that variant.
        """
        return target.dev

    def design(self, target) -> list:
        """Build the array for ``target`` and return its workers.

        ``target`` (:class:`iron.common.design.Target`) carries the device,
        the kernel tree, and ``kernel()``/``barrier()`` helpers that apply
        the fusion prefix so the overlay never sees it. Must call
        ``.bind(handle)`` on every declared stream (or on every slot of a
        ``per=`` stream) with the shim end of the fifo that carries it, and
        ``.bind(buffers)`` on every declared resident.
        """
        raise NotImplementedError(f"{type(self).__name__}.design() is not implemented")

    def semantics(self) -> Semantics:
        """What an output element of this array depends on (:mod:`.semantics`).

        Derived from the declared streams when they say it: every stream
        that is neither replicated nor broadcast carries one object shape
        over one slot count, in and out, and any shared input carries that
        shape too (a weight row). A core then turns object ``k`` in into
        object ``k`` out, so the answer is :class:`Local` over the whole
        object. An overlay whose kernel is finer (elementwise), or that
        computes anything the streams cannot show (a contraction, a copy
        that re-indexes), declares it. Needs a tuned overlay: tile shapes
        may be tunables.
        """
        name = type(self).__name__
        streams = list(self.streams.values())
        split = [s for s in streams if not (s.replicate or s.broadcast)]
        shared = [s for s in streams if s.replicate or s.broadcast]
        if not any(s.direction == "in" for s in split) or not any(
            s.direction == "out" for s in split
        ):
            return Undeclared(f"{name} has no per-slot stream in and out")
        if len({(s.shape, s.count) for s in split}) > 1:
            carried = ", ".join(f"{s.name} {s.shape} x{s.count}" for s in split)
            return Undeclared(f"{name}'s streams carry different objects ({carried})")
        shape = split[0].shape
        odd = [s.name for s in shared if s.direction != "in" or s.shape != shape]
        if odd:
            return Undeclared(f"{name}'s shared streams {odd} are not {shape} inputs")
        return Local(prod(shape))

    def tolerance(self, target: Target) -> Tolerance | None:
        """How close this array's output comes to the operator's reference:
        the contract of the kernel it runs.

        ``None`` here: an overlay that builds several kernels in
        :meth:`design` has no one contract that speaks for its output, so its
        operator states a tolerance itself. An overlay running one kernel
        overrides this with that kernel's contract.
        """
        return None

    # -- library surface ---------------------------------------------------

    def tuned(self, dev) -> "Overlay":
        if self._tuned:
            return self
        new = self.tuning(dev)
        if not isinstance(new, type(self)):
            raise TypeError(
                f"{type(self).__name__}.tuning() must return a {type(self).__name__}, "
                f"got {type(new).__name__}"
            )
        missing = [n for n in self._tunable_fields if getattr(new, n) is None]
        if missing:
            raise Untunable(
                f"{type(self).__name__}.tuning() left {missing} unset for {dev}"
            )
        new.validate()
        new._tuned = True
        new._specialised = dict(self._specialised)
        new._bind()
        return new

    def for_extent(self, **overrides) -> "Overlay":
        """A specialised copy: tunables set for one extent, at the cost of sharing."""
        bad = [k for k in overrides if k not in self._tunable_fields]
        if bad:
            raise TypeError(f"for_extent() sets non-tunable fields {bad}")
        new = dataclasses.replace(self, **overrides)
        new._specialised = {**self._specialised, **overrides}
        new._tuned = self._tuned
        new._bind()
        return new

    @property
    def specialised(self) -> bool:
        return bool(self._specialised)

    def value_symbol(self, value: "BoundValue") -> str | None:
        """An explicit device symbol for a core-read per-call value, or ``None``."""
        return None

    def design_key(self) -> tuple:
        """Identity for sharing: the class and every compared field value."""
        return (type(self).__qualname__,) + tuple(
            (f.name, getattr(self, f.name))
            for f in dataclasses.fields(self)
            if f.compare
        )

    def copy(self) -> "Overlay":
        """A fresh instance with the same fields and tuning state.

        A build works on a copy, so anything ``compatible()`` records on the
        overlay for one operator never reaches another that shares it.
        """
        new = dataclasses.replace(self)
        new._tuned = self._tuned
        new._specialised = dict(self._specialised)
        new._bind()
        return new

    def __eq__(self, other) -> bool:
        if not isinstance(other, Overlay):
            return NotImplemented
        return self.design_key() == other.design_key()

    def __hash__(self) -> int:
        return hash(self.design_key())

    @property
    def streams(self) -> dict[str, BoundStream]:
        return {
            m.name: self._bound[m.name] for m in self._members if isinstance(m, _Stream)
        }

    @property
    def residents(self) -> dict[str, BoundResident]:
        return {
            m.name: self._bound[m.name]
            for m in self._members
            if isinstance(m, Resident)
        }

    @property
    def values(self) -> list[BoundValue]:
        """Core-read per-call values this overlay declares."""
        return [self._bound[m.name] for m in self._members if isinstance(m, _Value)]

    def _bind(self) -> None:
        bound: dict[str, Any] = {}
        for m in self._members:
            if isinstance(m, _Stream):
                bound[m.name] = BoundStream(m, self)
            elif isinstance(m, Resident):
                bound[m.name] = BoundResident(m, self)
            elif isinstance(m, _Value):
                bound[m.name] = BoundValue(m, self)
        self._bound = bound

    def name_parts(self) -> list[str]:
        """This instance's fragments of an operator's name. Overridable: an
        external overlay names the binary it was built as, not its fields."""
        return label_parts(self)
