# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The per-call values an operator's cores read, as one operator holds them.

An operator's body declares them with mlir-aie's ``per_call()``; ``Value``
is that member bound to an operator instance, with the device parameter a
build gives it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

import numpy as np
from aie.iron import ScratchpadParameter, ceildiv
from aie.utils.compile.jit.params import PerCallMember

if TYPE_CHECKING:
    from aie.utils.compile.jit.params import OperatorParam

    from .operator import Operator


class Value(PerCallMember):
    """A ``per_call()`` member bound to one operator (``op.value("count")``, or
    ``op.count`` unless an extent): per call when a graph binds it, else written
    once per build before the first DMA. A core reads it through its ``Rtp``.

    Attributes:
        derive: The once-per-build word, or ``words`` of them, from the
            operator; None for one every call gives.
        bounds: For an extent, the ``param()`` it bounds per call; else None.
        param: The build's parameter: a ``ScratchpadParameter`` on a full ELF,
            a dispatch-time scalar on an xclbin.
        ssa: Its value in the sequence body, on an xclbin.
    """

    words: int = 1
    param: Any = None
    ssa: Any = None

    def __init__(
        self,
        op: Operator,
        name: str,
        *,
        dtype: Any = np.int32,
        derive: Callable[[Any], Any] | None = None,
        bounds: OperatorParam | None = None,
        words: int = 1,
    ) -> None:
        super().__init__(dtype, derive, bounds)
        self.op = op
        self.name = name
        self.words = words

    @property
    def per_call(self) -> bool:
        """A call gives this value: a graph binds it, or its ``derive``
        reads an extent a graph bounds. A value with no ``derive`` and no
        ``bounds`` always is.
        """
        op = self.op
        if self.bounds is not None:
            return self.name in op.bound_values
        if self.derive is None:
            return True
        return self.name in op.bound_values or self.name in op._per_call_derived()

    @property
    def dispatch(self) -> bool:
        """The instruction stream is regenerated around this value every
        call: one every call gives, on an operator with an exported design.
        A full ELF cannot carry it.
        """
        return (
            self.derive is None
            and self.bounds is None
            and self.op.exported_design() is not None
        )

    @property
    def symbol(self) -> str:
        """The device symbol the host writes it through: an exported design's own
        name, else ``<instance>_<value>[_<its graph value>]``; a derived value's
        names all the instance's graph values, so differently bound ones differ.
        """
        if self.op.exported_design() is not None:
            return self.name
        bound = self.op.bound_values
        if self.name in bound:
            own = bound[self.name]
            return "_".join(
                [self.op.name, self.name, *([] if own is None else [own.name])]
            )
        names = [bound[k].name for k in sorted(bound) if bound[k] is not None]
        return "_".join([self.op.name, *names, self.name])

    @property
    def in_scratchpad(self) -> bool:
        """The cores read this value from the parameter scratchpad: a build
        gave it a ``ScratchpadParameter`` (a per-call value on a full ELF).
        """
        return isinstance(self.param, ScratchpadParameter)

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.name} {np.dtype(self.dtype).name}>"


class ExtentWord(Value):
    """The tiles per lane of one operand under a bound, rounded up to whole
    tiles: a value the library adds per bound operand.
    """

    def __init__(self, op: Operator, extent: str, buffer: str, axis: int) -> None:
        super().__init__(op, f"{extent}_{buffer}", derive=self.tiles)
        self.extent, self.buffer, self.axis = extent, buffer, axis

    def tiles(self, op) -> int:
        """The word on ``op``; reads the extent first, which makes it per call."""
        extent = getattr(op, self.extent)
        return ceildiv(extent, self.divisor(op))

    def divisor(self, op) -> int:
        b = getattr(op, self.buffer)
        lanes = 1 if b.replicate else b.lanes
        return lanes * b.extent_unit(self.axis)

    def __repr__(self) -> str:
        return f"<tiles per lane of {self.buffer} under {self.extent}>"
