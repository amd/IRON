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
from iron.common import Scratchpad
from iron.common.image.jit_compile import DispatchStream
from iron.tests.toolchain.tools import requires

pytestmark = requires("xclbinutil", "peano")


def _graph():
    """A softmax with a per-call row length, then a copy into a cache at a
    per-call offset: one core-read value and one offset value.
    """
    from iron.operators.copy import Copy
    from iron.operators.softmax import Softmax

    R, C, L = 16, 256, 4
    cache = iron.state((R, L, C), name="cache")

    @iron.graph
    def g(x, *, n: Scratchpad[np.int32], pos: Scratchpad[np.int32]):
        y = Softmax(x, vector_size=n)
        Copy(y, cache[:, pos])
        return y

    return g, (R, C)


def test_values_become_dispatch_time_kernels_at_each_step(device):
    g, shape = _graph()
    net = g.compile(
        device,
        boundaries=iron.each_step,
        image=iron.XCLBIN,
        x=shape,
    )
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    kinds = {name: text for name, _, text in net.plan.values}
    assert (
        "dispatch-time scalar" in kinds["n"] and "dispatch-time scalar" in kinds["pos"]
    )
    chain = net.sequence._image
    assert chain is not None
    streams = {
        type(op).__name__: chain.op_insts_path_map[id(op)]
        for op in net.sequence.unique_operators()
    }
    assert set(streams) == {"Softmax", "Copy"}
    for name, stream in streams.items():
        assert isinstance(stream, DispatchStream), f"{name} has a static stream"
        assert Path(stream.lib_path).exists(), f"{name}: no dispatch library"
        assert len(stream.params) == 1, (name, stream.params)
    # The graph's symbols are the kernels' parameter names.
    symbols = {symbol for symbol, _, _ in net.words}
    assert symbols == {s.params[0] for s in streams.values()}
    assert net.image is not None and Path(net.image).stat().st_size > 0
    assert net._callable is None
