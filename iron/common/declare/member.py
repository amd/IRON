# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an overlay or operator declares besides its fields.

Streams are the overlay's ABI and buffers the operator's; the two agree by
construction, since a buffer names the stream it feeds or drains. The rest
name values no host buffer carries: a :class:`Scratchpad` or
:class:`DispatchTime` written per call, a :class:`Resident` written once,
before the first DMA.
"""

from __future__ import annotations

from typing import Any, ClassVar

import numpy as np
from ml_dtypes import bfloat16

from .field import DeclarationError, _DimSpec, _describe


class Shim:
    """A pinned shim endpoint: column and DMA channel on row 0."""

    __slots__ = ("col", "channel")

    def __init__(self, col: int, channel: int | None = None) -> None:
        self.col = col
        self.channel = channel

    def __repr__(self) -> str:
        return f"Shim(col={self.col}, channel={self.channel})"


class Xclbin:
    """An overlay someone else built: a downloaded xclbin, pinned by digest.

    Declared as a class attribute of an :class:`Overlay` that has no
    ``design()``. Every stream of such an overlay is pinned with ``via=`` and
    every resident has an ``address``, because nothing else says where its
    endpoints are; the library emits the sequence against those pins.
    """

    def __init__(
        self, *, url: str, sha256: str, filename: str, kernel_name: str = "MLIR_AIE"
    ) -> None:
        self.url = url
        self.sha256 = sha256
        self.filename = filename
        self.kernel_name = kernel_name

    def __repr__(self) -> str:
        return f"Xclbin({self.filename})"


class _Member:
    """Base of everything declared unannotated in an ``@operator`` class body.

    ``__set_name__`` gives the member its name from the language, and the
    class body gives it its order. On an instance, ``__get__`` returns the
    bound form built by ``@operator`` (a :class:`BoundBuffer`,
    :class:`BoundStream` or :class:`BoundValue`).
    """

    name: str = ""
    owner: type | None = None

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.owner = owner

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        try:
            return instance._bound[self.name]
        except (AttributeError, KeyError):
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None


class _Buffer(_Member):
    """A host buffer: shape in extents, a dtype, and the stream it moves through."""

    direction: ClassVar[str] = ""

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        to: "StreamIn | None" = None,
        from_: "StreamOut | None" = None,
    ) -> None:
        self.dims = tuple(dims)
        self.dtype = dtype
        self.to = to
        self.from_ = from_

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(_describe(d) for d in self.dims)})"


class In(_Buffer):
    """A buffer the host fills and the array reads."""

    direction = "in"

    def __init__(self, *dims, dtype=bfloat16, to=None) -> None:
        super().__init__(*dims, dtype=dtype, to=to)


class Out(_Buffer):
    """A buffer the array writes and the host reads."""

    direction = "out"

    def __init__(self, *dims, dtype=bfloat16, from_=None) -> None:
        super().__init__(*dims, dtype=dtype, from_=from_)


class InOut(_Buffer):
    """A buffer read and written in place."""

    direction = "inout"


class _Stream(_Member):
    """A stream into or out of the array, in tile units.

    ``per=`` names the overlay dimension the stream is replicated over (one
    fifo per column, say), or a tuple of dimensions whose product is the
    count (columns x channels); ``broadcast=True`` is one fifo every worker
    consumes. ``via=`` pins the shim endpoint(s). ``depth`` is the fifo depth.
    """

    direction: ClassVar[str] = ""

    def __init__(
        self,
        *dims: _DimSpec,
        dtype: Any = bfloat16,
        per: _DimSpec | None = None,
        broadcast: bool = False,
        replicate: bool = False,
        via: Shim | list[Shim] | None = None,
        depth: int = 2,
    ) -> None:
        if per is not None and broadcast:
            raise DeclarationError(
                "a stream is either per=<dim> or broadcast, not both"
            )
        if replicate and per is None:
            raise DeclarationError(
                "replicate=True needs per=<dim>: every slot receives the whole buffer"
            )
        self.dims = tuple(dims)
        self.dtype = dtype
        self.per = per
        self.broadcast = broadcast
        # per= slots that each receive the whole buffer (one fill per slot)
        # rather than a share of it.
        self.replicate = replicate
        self.via = via
        self.depth = depth

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(_describe(d) for d in self.dims)})"


class StreamIn(_Stream):
    """A stream entering the array; its shim end is a producer (MM2S)."""

    direction = "in"


class StreamOut(_Stream):
    """A stream leaving the array; its shim end is a consumer (S2MM)."""

    direction = "out"


class ValueSpec:
    """``Scratchpad[np.int32]``: the annotation of a graph function's per-call parameter.

    ``carried`` marks a value the graph computes for its own next call
    (:class:`Carried`).
    """

    __slots__ = ("kind", "dtype", "carried")

    def __init__(self, kind: str, dtype: Any, carried: bool = False) -> None:
        self.kind, self.dtype, self.carried = kind, dtype, carried

    def __repr__(self) -> str:
        text = f"{self.kind}[{np.dtype(self.dtype).name}]"
        return f"carried {text}" if self.carried else text


class _Value(_Member):
    """A per-call scalar. See :class:`Scratchpad` and :class:`DispatchTime`."""

    kind: ClassVar[str] = ""
    carried: ClassVar[bool] = False

    def __init__(self, dtype: Any = np.int32) -> None:
        self.dtype = dtype

    def __class_getitem__(cls, dtype) -> ValueSpec:
        return ValueSpec(cls.kind, dtype, cls.carried)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({np.dtype(self.dtype).name})"


class Scratchpad(_Value):
    """A per-call value patched into a DMA descriptor or read by a core.

    Free per call (a few words and a sync), works under full ELF, cannot
    change a DMA size or stride. Values are limited to 30 bits; ``float32``
    is unsupported by the scratchpad encoding.
    """

    kind = "scratchpad"

    def __init__(self, dtype: Any = np.int32) -> None:
        if np.dtype(dtype).kind == "f":
            raise DeclarationError(
                "Scratchpad values cannot be floating point: the scratchpad "
                "encoding zeroes the top two bits of the value"
            )
        super().__init__(dtype)


class Carried(Scratchpad):
    """A scratchpad value a graph function computes for its own next call.

    The function returns the next value with ``iron.carry(name=...)``: an
    integer expression of its values (``position + 1``) or a one-element
    integer handle it computed (a sampled token). The host writes it only
    to seed the first call; after that each call's carry is the next's.
    """

    carried = True


class DispatchTime(_Value):
    """A per-call value the instruction stream is regenerated around.

    Can change DMA sizes, strides and offsets; costs a stream regeneration
    and a buffer allocation per call; cannot be packaged as a full ELF.
    """

    kind = "dispatch"


class Resident(_Member):
    """A value the sequence writes into the array before the first DMA.

    Overlay-side: a runtime parameter (trip count, RTP) a core reads. The
    sequence's preamble writes every resident the overlay declares.
    """

    def __init__(
        self,
        dtype: Any = np.int32,
        *,
        address: int | None = None,
        lock: int | None = None,
        optional: bool = False,
    ) -> None:
        self.dtype = dtype
        self.address = address
        self.lock = lock
        # A resident only some configurations of the overlay allocate (a
        # parameter word omitted when its value is a compile-time constant).
        # The preamble skips it when design() left it unbound.
        self.optional = optional

    def __repr__(self) -> str:
        return f"Resident({np.dtype(self.dtype).name})"
