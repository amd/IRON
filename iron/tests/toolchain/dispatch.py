# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Per-call values on an image without a scratchpad build as dispatch-time kernels.

An xclbin run has no parameter scratchpad (spike S2), so on that image a
graph's per-call values become dispatch-time scalars of the kernels that
use them (§6): an offset use adds the scalar to the transfer's offset and
the kernel's stream is regenerated per call by the host library aiecc's
``--get-npu-cpp`` output compiles to; a core-read use is a resident the
sequence writes from the scalar before the barrier (spike S3's toolchain
half: the dialect takes the RTP write's value as an operand). Both are
built here at ``each_step`` on both devices; running them is the device's
half of S3, and of the regenerated-stream path itself.
"""

from pathlib import Path

import numpy as np

import iron
from iron.common.context import AIEContext
from iron.common.declare import Scratchpad
from iron.common.jit_compile import DispatchStream
from iron.tests.toolchain.tools import requires

pytestmark = requires("xclbinutil", "peano")


def _graph():
    """A softmax with a per-call row length, then a copy into a cache at a
    per-call offset: one core-read value and one offset value."""
    from iron.operators.softmax import Softmax
    from iron.operators.strided_copy import StridedCopy

    R, C, L = 16, 256, 4
    cache = iron.state((R, L * C), name="cache")

    @iron.graph
    def g(x, *, n: Scratchpad[np.int32], pos: Scratchpad[np.int32]):
        y = Softmax(x, vector_size=n)
        StridedCopy(
            y,
            cache,
            out_offset=pos,
            input_sizes=(R, C),
            input_strides=(C, 1),
            input_offset=0,
            output_sizes=(1, R, C),
            output_strides=(0, L * C, 1),
            output_offset=0,
            num_aie_channels=1,
        )
        return y

    return g, (R, C)


def test_values_become_dispatch_time_kernels_at_each_step(device, tmp_path):
    g, shape = _graph()
    net = g.compile(
        device,
        boundaries=iron.each_step,
        image=iron.XCLBIN,
        context=AIEContext(build_dir=str(tmp_path)),
        x=shape,
    )
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    kinds = {name: text for name, _, text in net.plan.values}
    assert (
        "dispatch-time scalar" in kinds["n"] and "dispatch-time scalar" in kinds["pos"]
    )
    chain = net.sequence._image
    streams = {
        type(op).__name__: chain.op_insts_path_map[id(op)]
        for op in net.sequence.unique_operators()
    }
    assert set(streams) == {"DynamicSoftmax", "StridedCopy"}
    for name, stream in streams.items():
        assert isinstance(stream, DispatchStream), f"{name} has a static stream"
        assert Path(stream.lib_path).exists(), f"{name}: no dispatch library"
        assert len(stream.params) == 1, (name, stream.params)
    # The graph's symbols are the kernels' parameter names.
    symbols = {symbol for _, symbol, _ in net.symbols}
    assert symbols == {s.params[0] for s in streams.values()}
    assert Path(net.image).stat().st_size > 0
    assert net._callable is None
