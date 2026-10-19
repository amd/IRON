# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sample reads every logit of any even vocab exactly once a pass, and joins
every summary, device-free: its built module's DMAs, expanded with numpy,
against each core's slice, and its summaries' join against their sizes.
"""

import re

import numpy as np
import pytest
from aie.iron import ExternalFunction
from aie.iron.kernels import sample as kernels

from iron.common.design import OperatorDesign
from iron.operators.sample import Sample

# Whisper's vocab (no even split) and Llama's, on npu2, and Whisper's on npu1.
CASES = [("npu2", v, c) for v in (51866, 128256) for c in (2, 4)]


def _built(op: Sample) -> str:
    ExternalFunction._instances.clear()
    try:
        return str(OperatorDesign(op).build())
    finally:
        ExternalFunction._instances.clear()


@pytest.mark.parametrize("device, vocab, cores", [*CASES, ("npu1", 51866, 2)])
def test_each_core_reads_its_slice_once_a_pass(device, vocab, cores, request):
    op = Sample(vocab=vocab, cores=cores).resolved(request.getfixturevalue(device))
    runs = op.layout().runs
    starts = np.cumsum([0] + [run for run, _ in runs])
    assert starts[-1] == vocab and all(
        s == c * op.slice_size for c, s in enumerate(starts[:-1])
    )
    mlir = _built(op)

    reads = {}
    for fifo, offset, sizes, strides in re.findall(
        rf"dma_configure_task_for @(\w+) {{\s*aie\.dma_bd\(%arg0 : memref<{vocab}xbf16> "
        r"offset = (\d+) len = \d+ sizes = \[([\d, ]+)\] strides = \[([\d, ]+)\]",
        mlir,
    ):
        index = int(offset)
        for size, stride in zip(sizes.split(", "), strides.split(", ")):
            index = np.add.outer(index, int(stride) * np.arange(int(size)))
        reads.setdefault(fifo, []).append(index.reshape(-1))
    assert len(reads) == cores
    for (fifo, read), start, (run, chunk) in zip(reads.items(), starts, runs):
        streams = kernels.select_streams(run, chunk)
        expected = np.tile(np.arange(start, start + run), streams)
        assert np.array_equal(np.concatenate(read), expected), fifo
        assert chunk % 2 == 0 and chunk <= 8192 and run % chunk == 0
        assert f"memref<{chunk}xbf16>, memref<4xi32>, memref<272xi32>" in mlir


@pytest.mark.parametrize("device, vocab, cores", [*CASES, ("npu1", 51866, 2)])
def test_each_summary_fills_its_slot_of_the_join(device, vocab, cores, request):
    """A join input moves the words up to the next offset, or to the end."""
    op = Sample(vocab=vocab, cores=cores).resolved(request.getfixturevalue(device))
    mlir = _built(op)
    words = dict(re.findall(r"objectfifo @(\w+)\(.*?memref<(\d+)xi32>>", mlir))
    [(ins, out, offsets)] = re.findall(
        r"objectfifo\.link \[([^\]]+)\] -> \[@(\w+)\]\(\[([\d, ]+)\] \[\]\)", mlir
    )
    ends = [*map(int, offsets.split(", ")[1:]), int(words[out])]
    for fifo, start, end in zip(ins.split(", "), map(int, offsets.split(", ")), ends):
        assert int(words[fifo.lstrip("@")]) == end - start, fifo
