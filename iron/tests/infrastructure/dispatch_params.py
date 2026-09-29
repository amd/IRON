#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for operators whose runtime sequence takes scalars.

The operator under test copies ``n`` chunks from one buffer to another through
a memtile. ``n`` is a dispatch parameter: it bounds the runtime sequence's loop
and sets the offset of each transfer, so no single instruction stream serves
every ``n``. The design has no cores, so the test needs no kernel.
"""

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pytest

import aie.utils as aie_utils
from aie.dialects import arith
from aie.extras import types as T
from aie.iron import ObjectFifo, Program, Runtime
from aie.iron.controlflow import range_

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    DispatchCallable,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)

CHUNK = 1024
SENTINEL = -1


def chunk_copy(dev, max_chunks):
    chunk_ty = np.ndarray[(CHUNK,), np.dtype[np.int32]]
    buf_ty = np.ndarray[(max_chunks * CHUNK,), np.dtype[np.int32]]

    of_in = ObjectFifo(chunk_ty, name="in")
    of_out = of_in.cons().forward(name="out")

    def sequence(src, dst, n, in_prod, out_cons):
        for i in range_(n):
            offset = arith.index_cast(T.i32(), i) * CHUNK
            transfer = dict(
                sizes=[1, 1, 1, CHUNK],
                strides=[0, 0, 0, 1],
                offset=offset,
                transfer_len=CHUNK,
                managed=False,
            )
            out_task = out_cons.drain(dst, wait=True, **transfer)
            in_task = in_prod.fill(src, wait=False, **transfer)
            out_task.await_()
            out_task.free()
            in_task.free()

    rt = Runtime(sequence, [buf_ty, buf_ty, np.int32, of_in.prod(), of_out.cons()])
    return Program(dev, rt).resolve_program()


@dataclass
class ChunkCopy(MLIROperator):
    max_chunks: int
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                Path(__file__),
                "chunk_copy",
                (aie_utils.get_current_device(), self.max_chunks),
            ),
        )

    def get_kernel_artifacts(self):
        return []

    def get_arg_spec(self):
        size = (self.max_chunks * CHUNK,)
        return [
            AIERuntimeArgSpec("in", size, dtype=np.int32),
            AIERuntimeArgSpec("out", size, dtype=np.int32),
        ]

    def get_dispatch_params(self):
        return {"n": np.int32}


MAX_CHUNKS = 16


@pytest.fixture
def chunk_copy_op(aie_context):
    op = ChunkCopy(max_chunks=MAX_CHUNKS, context=aie_context)
    op.compile()
    return op


def test_builds_a_generator_and_no_instruction_file(chunk_copy_op):
    op = chunk_copy_op
    assert Path(op.xclbin_artifact.filename).is_file()
    assert Path(op.dispatch_artifact.filename).resolve().is_file()
    cpp = Path(op.dispatch_artifact.cpp_filename).read_text()
    assert "generate_txn_main_sequence(int32_t" in cpp
    assert not hasattr(op, "insts_artifact")


def test_one_callable_serves_every_parameter(chunk_copy_op):
    """Each n must copy exactly n chunks: a stream generated for another n,
    or none at all, leaves a different number of sentinels behind."""
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    size = MAX_CHUNKS * CHUNK
    src = np.arange(size, dtype=np.int32)

    run = chunk_copy_op.get_callable()
    assert isinstance(run, DispatchCallable)
    for n in (3, 1, MAX_CHUNKS, 3):
        src_buf = tensor_class((size,), dtype=np.int32)
        src_buf.numpy_view()[:] = src
        dst_buf = tensor_class((size,), dtype=np.int32)
        dst_buf.numpy_view()[:] = SENTINEL

        run.set_parameters(n=n)
        run(src_buf, dst_buf)

        dst = dst_buf.numpy()
        np.testing.assert_array_equal(dst[: n * CHUNK], src[: n * CHUNK])
        assert np.all(dst[n * CHUNK :] == SENTINEL), f"n={n} copied too much"


def test_call_before_set_parameters_raises(chunk_copy_op):
    run = chunk_copy_op.get_callable()
    with pytest.raises(RuntimeError, match="set_parameters"):
        run()


@pytest.mark.parametrize("params", [{}, {"m": 1}, {"n": 1, "m": 1}])
def test_set_parameters_takes_exactly_the_declared_names(chunk_copy_op, params):
    run = chunk_copy_op.get_callable()
    with pytest.raises(TypeError, match="takes exactly"):
        run.set_parameters(**params)


def test_sequences_reject_a_dispatch_operator(aie_context):
    op = ChunkCopy(max_chunks=MAX_CHUNKS, context=aie_context)
    with pytest.raises(NotImplementedError, match="per dispatch"):
        op.get_artifacts()
