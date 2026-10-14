# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The scalars an operator's array reads that no operand carries."""

from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any, Callable, Self, overload

import numpy as np
from aie.iron import ScratchpadParameter, ceildiv

from .member import Member

if TYPE_CHECKING:
    from .operator import Operator


class Value(Member["Value"]):
    """A value the array reads: per call when a graph binds it, else written
    once per build before the first DMA.

    Declared in an operator's body; on an instance, ``op.value(name)`` is the
    value bound to it (`of`), which a build gives its device parameter.

    Args:
        dtype: An integer type: the scratchpad encoding has no floating point.
        derive: The once-per-build value, from the operator: a word, or
            the words of a block written from its index on.
        optional: A build may allocate no buffer for it.

    Attributes:
        param: The build's parameter: on a full ELF the ``ScratchpadParameter``,
            on an xclbin (no scratchpad) a dispatch-time scalar.
        ssa: Its value in the sequence body, on an xclbin.
        targets: The runtime-parameter buffers, and the index in each, that
            the preamble writes it to (`bind`).
    """

    def __init__(
        self,
        *,
        dtype: Any = np.int32,
        derive: Callable[[Any], Any] | None = None,
        optional: bool = False,
    ) -> None:
        if np.dtype(dtype).kind == "f":
            raise TypeError(
                f"{type(self).__name__} values cannot be floating point: the "
                f"scratchpad encoding zeroes the top two bits of the value"
            )
        self.dtype = dtype
        self.derive = derive
        self.optional = optional
        self.op: Operator | None = None
        self.param: Any = None
        self.ssa = None
        self.targets: list[tuple[Any, int]] = []

    def of(self, op: Operator) -> Self:
        """This value on ``op``, with no parameter yet."""
        bound = copy.copy(self)
        bound.op = op
        bound.targets = []
        return bound

    def bind(self, buffers, index: int = 0) -> None:
        """Bind to runtime-parameter buffers whose ``[index]`` the preamble writes."""
        if not isinstance(buffers, (list, tuple)):
            buffers = [buffers]
        self.targets.extend((b, index) for b in buffers)

    @property
    def symbol(self) -> str:
        """The device symbol the host writes this value through: an exported
        design's own parameter of its name, else the instance's name, the
        value's and the graph value bound to it.
        """
        if self.op.exported_design() is not None:
            return self.name
        bound = self.op.bound_values.get(self.name)
        return f"{self.op.name}_{self.name}" + (
            "" if bound is None else f"_{bound.name}"
        )

    @property
    def scratchpad(self) -> bool:
        """The cores read this value from the parameter scratchpad: a build
        gave it a ``ScratchpadParameter`` (a per-call value on a full ELF).
        """
        return isinstance(self.param, ScratchpadParameter)

    def __repr__(self) -> str:
        if self.op is None:
            return f"{type(self).__name__}({np.dtype(self.dtype).name})"
        return f"<{type(self).__name__} {self.name} {np.dtype(self.dtype).name}>"


class DispatchTime(Value):
    """A per-call value the instruction stream is regenerated around.

    Can change DMA sizes, strides and offsets; costs a stream regeneration
    and a buffer allocation per call; cannot be packaged as a full ELF.
    """

    def __init__(self, *, dtype: Any = np.int32) -> None:
        super().__init__(dtype=dtype)


class Extent(Value):
    """A ``Param()`` shape field a graph may bound per call.

    ``valid = Extent(size)`` reads as ``size`` until a graph bounds an
    operand the field sizes (``x[:n]``); then it, and every ``Value`` whose
    ``derive`` reads it, is per call. The image is built for the full value.
    """

    def __init__(self, field: Any, *, dtype: Any = np.int32) -> None:
        super().__init__(dtype=dtype)
        self.field = field  # the Param field

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: type | None = None) -> int: ...
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        # The extents a derive reads, recorded on the copy Operator._per_call_derived probes.
        reads = instance.__dict__.get("_extent_reads")
        if reads is not None:
            reads.add(self.name)
        bound = instance.__dict__.get("_extents", {}).get(self.name)
        if bound is not None:
            return bound
        return getattr(instance, self.field.name)

    def __repr__(self) -> str:
        return f"Extent({self.field!r})"


class ExtentWord(Value):
    """The tiles per lane of one operand under a bound, rounded up to whole
    tiles: a value the library adds per bound operand.
    """

    def __init__(self, owner: type, extent: Extent, buffer: str, axis: int) -> None:
        super().__init__(derive=self.tiles)
        self.owner = owner
        self.name = f"{extent.name}_{buffer}"
        self.extent, self.buffer, self.axis = extent, buffer, axis

    def tiles(self, op) -> int:
        """The word on ``op``; reads the extent first, which makes it per call."""
        extent = self.extent.__get__(op)
        return ceildiv(extent, self.divisor(op))

    def divisor(self, op) -> int:
        b = op.value_buffer(self.buffer)
        lanes = 1 if b.replicate else b.count
        return lanes * b.extent_unit(self.axis)

    def __repr__(self) -> str:
        return f"<tiles per lane of {self.buffer} under {self.extent.name}>"


class ChainWord(Value):
    """Which of its array's finishes or prologues an operator's cores
    apply: a value the library adds where an array serves more than one.
    """

    def __init__(self, owner: type, finish: bool) -> None:
        super().__init__(derive=self.index, optional=True)
        self.owner = owner
        self.finish = finish
        self.name = "finish_chain" if finish else "prepare_chain"

    def index(self, op) -> int:
        """The word on ``op``: its own chain's place among its array's."""
        chain = op.finish if self.finish else op.prepare
        return chain.keys().index(chain.array_key())

    def __repr__(self) -> str:
        return f"<the {self.name} a design selects>"


class PlaceWord(Value):
    """The per-call element offset of an operand placed in a larger buffer:
    every transfer of it moves by the word (``Operator.placed``).
    """

    def __init__(self, owner: type, buffer: str) -> None:
        super().__init__()
        self.owner = owner
        self.buffer = buffer
        self.name = f"{buffer}_offset"

    def __repr__(self) -> str:
        return f"<the offset {self.buffer} is placed at>"
