# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import ClassVar, Dict

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    Scratchpad,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)
from iron.common.tiling import Access
from iron.common.test_utils import torch_dtype_map


@operator
class StridedCopyOverlay(Overlay):
    """A memtile pass-through, one channel per fifo; no cores.

    Each channel's descriptor carries 1/num_aie_channels of the tensor, so the
    fifo object is sized against the per-channel share (``transfer_size``). A
    descriptor shorter than the object starves the memtile's S2MM: it never
    completes an object, never releases the lock, and the drain never returns
    (ERT_CMD_STATE_TIMEOUT). An integer multiple is fine; it cycles the buffer.
    """

    # Derived from input_sizes by the constructor (per-channel share).
    transfer_size: int | None = tunable(None)
    num_aie_channels: int = tunable(1)
    dtype: object = field(default=bfloat16, repr=False)

    s = StreamIn(transfer_size, dtype=dtype, per=num_aie_channels, depth=1)
    d = StreamOut(transfer_size, dtype=dtype, per=num_aie_channels, depth=1)

    _name_aliases: ClassVar[Dict[str, str]] = {
        "transfer_size": "tr",
        "num_aie_channels": "ch",
    }

    def design(self, target) -> list:
        from aie.iron import ObjectFifo

        for c in range(self.num_aie_channels):
            fifo_in = ObjectFifo(self.s.tile, name=f"fifo_in_{c}", depth=1)
            fifo_out = fifo_in.cons().forward(name=f"fifo_out_{c}", depth=1)
            self.s[c].bind(fifo_in.prod())
            self.d[c].bind(fifo_out.cons())
        return []


def _pad4(sizes, strides):
    """Pad to 4-D: dropping leading dimensions leaves BD registers uninitialised."""
    sizes, strides = list(sizes), list(strides)
    return [1] * (4 - len(sizes)) + sizes, [0] * (4 - len(strides)) + strides


@operator
class StridedCopy(Operator[StridedCopyOverlay]):
    """AIE-accelerated strided copy operator.

    Gathers by the input pattern and scatters by the output pattern, split
    across the overlay's channels on the highest-index non-unit dimension.
    Useful for data layout manipulation such as ``input[0, :, 0] -> output[:, 0, 0]``.
    """

    input_buffer_size: int = dim(repr=False)
    output_buffer_size: int = dim(repr=False)
    input_sizes: tuple = ()
    input_strides: tuple = ()
    input_offset: int = 0
    output_sizes: tuple = ()
    output_strides: tuple = ()
    output_offset: int = 0
    x = In(input_buffer_size, dtype=StridedCopyOverlay.dtype, to=StridedCopyOverlay.s)
    y = Out(
        output_buffer_size, dtype=StridedCopyOverlay.dtype, from_=StridedCopyOverlay.d
    )
    # Per-call addends on the two base addresses, patched into the descriptors.
    in_offset = Scratchpad(np.int32)
    out_offset = Scratchpad(np.int32)

    _name_aliases: ClassVar[Dict[str, str]] = {
        "input_sizes": "isz",
        "input_strides": "ist",
        "input_offset": "ioff",
        "output_sizes": "osz",
        "output_strides": "ost",
        "output_offset": "ooff",
    }

    @classmethod
    def _classic(cls, kwargs):
        kwargs.pop("kwargs", None)
        if kwargs.get("transfer_size") is None:
            sizes = kwargs.get("input_sizes", ())
            channels = kwargs.get("num_aie_channels", 1)
            kwargs["transfer_size"] = int(np.prod(sizes)) // channels
        return super()._classic(kwargs)

    def uses_value(self, name: str) -> bool:
        # An offset is patched only when a graph binds a handle to it.
        return name in self.used_values

    @property
    def transfer_size(self) -> int:
        return self.ov.transfer_size

    @property
    def num_aie_channels(self) -> int:
        return self.ov.num_aie_channels

    @property
    def dtype(self):
        return self.ov.dtype

    def validate(self) -> None:
        if len(self.input_sizes) != len(self.input_strides):
            raise ValueError(
                f"input_sizes and input_strides must have the same length "
                f"({len(self.input_sizes)} vs {len(self.input_strides)})"
            )
        if len(self.output_sizes) != len(self.output_strides):
            raise ValueError(
                f"output_sizes and output_strides must have the same length "
                f"({len(self.output_sizes)} vs {len(self.output_strides)})"
            )
        n_in, n_out = int(np.prod(self.input_sizes)), int(np.prod(self.output_sizes))
        if n_in != n_out:
            raise ValueError(
                f"a copy moves the same element count both ways: input_sizes "
                f"{list(self.input_sizes)} has {n_in} elements, output_sizes "
                f"{list(self.output_sizes)} has {n_out}"
            )

    def compatible(self) -> None:
        from iron.common.declare import Incompatible

        channels = self.ov.num_aie_channels
        for label, sizes in (
            ("input_sizes", self.input_sizes),
            ("output_sizes", self.output_sizes),
        ):
            padded, _ = _pad4(sizes, sizes)
            highest = max(i for i, sz in enumerate(padded) if sz >= 1)
            if padded[highest] % channels:
                raise Incompatible(
                    f"Highest dimension of {label} must be divisible by num_aie_channels"
                )
        per_channel = int(np.prod(self.input_sizes)) // channels
        if per_channel % self.ov.transfer_size:
            raise Incompatible(
                f"transfer_size {self.ov.transfer_size} must divide the per-channel transfer "
                f"{per_channel} (= {int(np.prod(self.input_sizes))} / {channels} channels)"
            )

    def _taps(self, buffer, sizes, strides, offset):
        sizes, strides = _pad4(sizes, strides)
        highest = max(i for i, sz in enumerate(sizes) if sz >= 1)
        channels = self.ov.num_aie_channels
        share = sizes[highest] // channels
        split = sizes[:highest] + [share] + sizes[highest + 1 :]
        return [
            Access(
                buffer.elements,
                offset + c * share * strides[highest],
                tuple(split),
                tuple(strides),
            )
            for c in range(channels)
        ]

    def design(self, rt):
        ins = self._taps(
            self.x, self.input_sizes, self.input_strides, self.input_offset
        )
        outs = self._taps(
            self.y, self.output_sizes, self.output_strides, self.output_offset
        )
        in_off = self.in_offset if self.uses_value("in_offset") else None
        out_off = self.out_offset if self.uses_value("out_offset") else None
        with rt.group() as tg:
            for c in range(self.ov.num_aie_channels):
                rt.fill(self.ov.s[c], (self.x, ins[c]), group=tg, offset_by=in_off)
                rt.drain(
                    self.ov.d[c],
                    (self.y, outs[c]),
                    group=tg,
                    wait=True,
                    offset_by=out_off,
                )


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def _pad_to_4d(sizes, strides):
    """design.py pads access patterns to 4D before building the taps; the reference
    has to pad identically or the per-channel split lands on a different dimension."""
    return (
        [1] * (4 - len(sizes)) + list(sizes),
        [0] * (4 - len(strides)) + list(strides),
    )


def _tap_offsets(sizes, strides, offset):
    """Flat element offsets a TensorAccessPattern visits, in issue order."""
    grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
    flat = np.full(grids[0].shape, offset, dtype=np.int64)
    for grid, stride in zip(grids, strides):
        flat = flat + grid * stride
    return flat.reshape(-1)


def _channel_offsets(sizes, strides, offset, num_aie_channels):
    sizes, strides = _pad_to_4d(sizes, strides)
    highest = max(idx for idx, sz in enumerate(sizes) if sz >= 1)
    per_channel = sizes[highest] // num_aie_channels
    split = sizes[:highest] + [per_channel] + sizes[highest + 1 :]
    return [
        _tap_offsets(split, strides, offset + c * per_channel * strides[highest])
        for c in range(num_aie_channels)
    ]


def reference(
    input_flat,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    num_aie_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
):
    """Gather by the input tap, scatter by the output tap, one channel at a time.

    The addends are the *_offset_parameter values. They are element counts, not byte
    offsets: the firmware multiplies the scratchpad word by the element size before
    adding it into the BD address register.
    """
    src = _channel_offsets(
        input_sizes, input_strides, input_offset + input_offset_addend, num_aie_channels
    )
    dst = _channel_offsets(
        output_sizes,
        output_strides,
        output_offset + output_offset_addend,
        num_aie_channels,
    )

    out = torch.zeros(int(output_buffer_size), dtype=input_flat.dtype)
    for src_c, dst_c in zip(src, dst):
        if len(src_c) != len(dst_c):
            raise ValueError(
                f"tap element counts differ ({len(src_c)} vs {len(dst_c)}); "
                "the input and output access patterns must move the same number "
                "of elements"
            )
        out[dst_c] = input_flat[src_c]
    return out


def generate_golden_reference(
    input_buffer_size,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    num_aie_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
    dtype="bf16",
    seed=42,
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(int(input_buffer_size), dtype=torch_dtype_map[dtype]) * val_range
    )
    output_tensor = reference(
        input_tensor,
        input_sizes,
        input_strides,
        input_offset,
        output_buffer_size,
        output_sizes,
        output_strides,
        output_offset,
        num_aie_channels=num_aie_channels,
        input_offset_addend=input_offset_addend,
        output_offset_addend=output_offset_addend,
    )
    return {"input": input_tensor, "output": output_tensor}
