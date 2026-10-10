#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for operators whose runtime sequence takes scalars.

The operator under test copies ``n`` chunks from one buffer to another through
a memtile. ``n`` is a ``DispatchTime`` value. It bounds the runtime sequence's
loop and sets the offset of each transfer. The design has no cores, so the
test needs no kernel.
"""

import dataclasses
import functools

import aie.iron
import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import ObjectFifo, Program, Runtime, require
from aie.iron.controlflow import range_
from aie.utils.hostruntime.hostruntime import HostRuntimeError

from iron.common import DispatchTime, In, Operator, Out, param
from iron.common.design.build import build_design
from iron.common.image import OperatorImage

CHUNK = 1024
SENTINEL = -1
MAX_CHUNKS = 16


def chunk_copy(dev, max_chunks, *, n: aie.iron.DispatchTime[np.int32]):
    chunk_ty = np.ndarray[(CHUNK,), np.dtype[np.int32]]
    buf_ty = np.ndarray[(max_chunks * CHUNK,), np.dtype[np.int32]]

    of_in = ObjectFifo(chunk_ty, name="in")
    of_out = of_in.cons().forward(name="out")

    def sequence(src, dst, n, in_prod, out_cons):
        require(n <= max_chunks, f"n exceeds {max_chunks}")
        for i in range_(n):
            chunk = slice(i * CHUNK, (i + 1) * CHUNK)
            in_task = in_prod.fill(src, tap=src[chunk], managed=False)
            out_task = out_cons.drain(dst, tap=dst[chunk], wait=True, managed=False)
            out_task.await_()
            out_task.free()
            in_task.free()

    rt = Runtime(sequence, [buf_ty, buf_ty, n, of_in.prod(), of_out.cons()])
    return Program(dev, rt).resolve_program()


class ChunkCopy(Operator):
    max_chunks: int = param()
    size: int = param(default=lambda op: op.max_chunks * CHUNK, repr=False)

    src = In(size, dtype=np.int32)
    dst = Out(size, dtype=np.int32)
    n = DispatchTime(np.int32)

    def validate(self) -> None:
        self.check_derived("size")

    def resolve(self, dev):
        return dataclasses.replace(self)

    def value_symbol(self, value) -> str:
        return value.name

    def exported_design(self, image: str):
        return functools.partial(chunk_copy, self.dev, self.max_chunks)


def _buffers():
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    src = tensor(np.arange(MAX_CHUNKS * CHUNK, dtype=np.int32))
    dst = tensor(np.full(MAX_CHUNKS * CHUNK, SENTINEL, dtype=np.int32))
    return src, dst


def test_the_stream_is_generated_per_call():
    artifacts = OperatorImage(ChunkCopy(max_chunks=MAX_CHUNKS)).compile().artifacts
    assert artifacts.insts is None
    assert artifacts.entry.dispatch_library.is_file()


def test_one_image_serves_every_parameter(npu_runtime):
    """Each n must copy exactly n chunks: a stream generated for another n
    leaves a different number of sentinels behind.
    """
    image = OperatorImage(ChunkCopy(max_chunks=MAX_CHUNKS))
    for n in (3, 1, MAX_CHUNKS, 3):
        src, dst = _buffers()
        image(src, dst, n=n)
        got, want = dst.numpy(), src.numpy()
        np.testing.assert_array_equal(got[: n * CHUNK], want[: n * CHUNK])
        assert np.all(got[n * CHUNK :] == SENTINEL), f"n={n} copied too much"


def test_refuses_an_n_past_the_buffers(npu_runtime):
    image = OperatorImage(ChunkCopy(max_chunks=MAX_CHUNKS))
    with pytest.raises(HostRuntimeError, match=f"n exceeds {MAX_CHUNKS}"):
        image(*_buffers(), n=MAX_CHUNKS + 1)


@pytest.mark.parametrize(
    "scalars, error, match",
    [
        ({}, HostRuntimeError, "dispatch scalar mismatch"),
        ({"m": 1}, TypeError, r"unexpected keyword argument\(s\): \['m'\]"),
        ({"n": 1, "m": 1}, TypeError, r"unexpected keyword argument\(s\): \['m'\]"),
    ],
)
def test_a_call_takes_exactly_the_declared_scalars(scalars, error, match, npu_runtime):
    image = OperatorImage(ChunkCopy(max_chunks=MAX_CHUNKS))
    with pytest.raises(error, match=match):
        image(*_buffers(), **scalars)


def test_a_full_elf_refuses_a_dispatch_value():
    with pytest.raises(ValueError, match="package as xclbin"):
        build_design(ChunkCopy(max_chunks=MAX_CHUNKS))
