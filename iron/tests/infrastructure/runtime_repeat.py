#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A shim task's repeat count set per call (``repeat_by``).

The operator under test sends one tile `k` times through a memtile, `k` the
bound of its output's rows: the fill's iteration slot (stride 0) runs
`reps + 1 = k` times and the drain's length is `k` tiles. On an xclbin image
the repeat count is a dispatch-time scalar, computed into the push each call
generates; on a full ELF it is a scratchpad word the queue push is updated
from. One image serves every `k`.
"""

import dataclasses

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.passmanager import PassManager
from aie.iron import ObjectFifo, TaskGroup
from aie.utils.npukernel import NPUKernel
from aie.utils.txn_trace import trace

import iron
from iron.common import Extent, In, Operator, Out, Scratchpad, Value, param
from iron.common.design import OperatorDesign
from iron.common.design.build import build_design, device_symbol
from iron.common.graph import Value as GraphValue

WIDTH = 256
MAX_K = 16
SENTINEL = -1
IMAGES = {
    "elf": {"image": iron.ELF},
    "xclbin": {"image": iron.XCLBIN, "boundaries": iron.each_step},
}


class RepeatTile(Operator):
    """`y[:valid]` is `valid` copies of `x`; past it, `y` is untouched."""

    width: int = param()
    max_k: int = param()

    valid = Extent(max_k)
    reps = Value(np.int32, derive=lambda op: op.valid - 1)

    x = In(width, dtype=np.int32, tile=(width,))
    y = Out(max_k, width, dtype=np.int32, tile=(width,))

    def resolve(self, dev):
        return dataclasses.replace(self)

    def array(self, target) -> list:
        fifo_in = ObjectFifo(self.x.tile, name="fifo_in", depth=2)
        fifo_out = fifo_in.cons().forward(name="fifo_out", depth=2)
        self.x.bind(fifo_in.prod())
        self.y.bind(fifo_out.cons())
        return []

    def sequence(self, rt):
        width, max_k = self.width, self.max_k
        bound = self.uses_value("reps")
        tg = TaskGroup()
        rt.fill(
            self.x,
            TensorAccessPattern((width,), 0, [max_k, 1, 1, width], [0, 0, 0, 1]),
            group=tg,
            repeat_by=self.value("reps") if bound else None,
        )
        rt.drain(
            self.y,
            TensorAccessPattern(
                (max_k, width), 0, [1, 1, max_k, width], [0, 0, width, 1]
            ),
            group=tg,
            wait=True,
            size_by={2: self.value("valid_y")} if bound else None,
        )
        tg.finish()

    def reference(self, x):
        return np.tile(x, (self.max_k, 1))


class Repeated(iron.Graph):
    def __init__(self):
        self.out = iron.state((MAX_K, WIDTH), dtype=np.int32)

    def body(self, x, *, k: Scratchpad[np.int32]):
        RepeatTile(x, self.out, valid=k)


def _bound_op() -> RepeatTile:
    op = RepeatTile(width=WIDTH, max_k=MAX_K)
    op.use_value("valid", GraphValue("k", Scratchpad, np.int32).affine())
    return op


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("image", IMAGES)
def test_one_image_repeats_a_tile_k_times(image, npu_runtime, npu2):
    graph = Repeated()
    net = graph.compile(x=((WIDTH,), np.int32), **IMAGES[image])
    assert net.plan.image == image
    x = np.arange(1, WIDTH + 1, dtype=np.int32)
    for k in (3, MAX_K, 1, 7):
        net.write(graph.out, np.full((MAX_K, WIDTH), SENTINEL, dtype=np.int32))
        net(x, k=k)
        want = np.full((MAX_K, WIDTH), SENTINEL, dtype=np.int32)
        want[:k] = x
        got = np.asarray(net.read(graph.out)).reshape(MAX_K, WIDTH)
        wrong = np.argwhere(got != want)
        assert wrong.size == 0, f"{k=}: {len(wrong)} differ, first {wrong[:4]}"


def test_npu1_xclbin_pushes_the_call_s_repeat_count(npu1):
    op = _bound_op().resolved()
    design = OperatorDesign(op, "xclbin").compile()
    kernel = NPUKernel(
        design.get_cache_entry().xclbin,
        None,
        dispatch_params=design.dispatch_params,
        dispatch_lib_path=design.get_dispatch_lib_path(),
    )
    symbol = {v.name: device_symbol(op, v) for v in op.values}
    tile_words = WIDTH * np.dtype(np.int32).itemsize // 4
    for k in (3, 7):
        words = kernel.instructions(
            **{symbol["valid"]: k, symbol["reps"]: k - 1, symbol["valid_y"]: k}
        )
        pushes = {
            e.direction: (e.repeat, e.bd.length)
            for e in trace(words)
            if e.kind == "push" and e.row == 0
        }
        assert pushes == {"MM2S": (k - 1, tile_words), "S2MM": (0, k * tile_words)}


def test_a_full_elf_takes_the_repeat_count_from_the_scratchpad(npu2, tmp_path):
    """The fill's start names the repeat word, which the scratchpad lowering
    makes a repeat parameter bounded by the pattern's 16 runs; the drain's
    length is a word of its own.
    """
    op = _bound_op().resolved()
    module = build_design(op)
    reps, tiles = (device_symbol(op, op.value(n)) for n in ("reps", "valid_y"))
    assert f"{{repeat_parameter = @{reps}}}" in str(module)
    params = tmp_path / "params.txt"
    with module.context:
        PassManager.parse(
            "builtin.module(aie-lower-scratchpad-parameters"
            f"{{output-params-file={params}}})"
        ).run(module.operation)
    kinds = {
        line.split()[0]: line.split()[3:]
        for line in params.read_text().splitlines()[1:]
        if len(line.split()) > 3
    }
    assert kinds[reps] == ["repeat", "0", str(MAX_K - 1)]
    assert kinds[tiles] == ["addr", "0", str(MAX_K)]
