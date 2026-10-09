# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Per-call values on an image without a scratchpad build as dispatch-time kernels.

An xclbin run has no parameter scratchpad (XRT gives one to a module run
only), so on that image a graph's per-call values become dispatch-time
scalars of the kernels that use them: an offset use adds the scalar to the transfer's offset and
the kernel's stream is regenerated per call by the host library aiecc's
``--get-npu-cpp`` output compiles to; a core-read use is a resident the
sequence writes from the scalar before the barrier (the dialect takes the
RTP write's value as an operand). Both are built here at ``each_step`` on
both devices; running them on a device is the other half.
"""

from pathlib import Path

import aie.utils as aie_utils
import numpy as np

import iron
from iron.common import Scratchpad
from iron.operators.copy import Copy
from iron.operators.mha import MHA
from iron.operators.softmax import Softmax
from iron.tests.toolchain.tools import DEVICES, requires

pytestmark = requires("xclbinutil", "peano")


def _graph():
    """A softmax with a per-call row length, then a copy into a cache at a
    per-call offset: one core-read value and one offset value.
    """
    R, C, L = 16, 256, 4
    cache = iron.state((R, L, C), name="cache")

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32], pos: Scratchpad[np.int32]):
            y = Softmax(x[:, :n])
            Copy(y, cache[:, pos])
            return y

    g = G()

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
    designs = {
        type(op).__name__: chain.designs[id(op)]
        for op in net.sequence.unique_operators()
    }
    assert set(designs) == {"Softmax", "Copy"}
    for name, design in designs.items():
        lib = design.get_dispatch_lib_path()
        assert lib is not None and Path(lib).exists(), f"{name}: no dispatch library"
        assert design.dispatch_params, f"{name}: no dispatch parameter"
    # The graph's symbols are the kernels' parameter names.
    symbols = {w.symbol for w in net.words}
    assert symbols == {p for d in designs.values() for p in d.dispatch_params}
    assert net.image is not None and Path(net.image).stat().st_size > 0
    assert net._callable is None


def test_a_per_call_size_over_one_block_builds_at_each_step(npu2):
    """One query over a cache of one key block: K and V's block count is
    per call, over a dimension of one block, whose stride the pattern holds
    as 0.
    """
    heads, kv_heads, d, cache = 8, 2, 64, 64

    class Decode(iron.Graph):
        def body(self, q, k, v, *, position: Scratchpad[np.int32]):
            return MHA(
                q,
                k[:, : position + 1],
                v[:, : position + 1],
                heads_interleaved=True,
                num_pipelines=2,
            )

    net = Decode().compile(
        npu2,
        boundaries=iron.each_step,
        q=(1, heads, d),
        k=(kv_heads, cache, d),
        v=(kv_heads, cache, d),
    )
    assert net.plan.image == "xclbin"
    assert net.image is not None and Path(net.image).stat().st_size > 0


def test_npu1_compiles_each_step_unasked():
    """NPU1 has no full-ELF dispatch, so a plain ``compile()`` there takes
    the xclbin form that is built, one dispatch per step.
    """
    g, shape = _graph()
    previous = aie_utils.get_current_device(probe_runtime=False)
    net = g.compile(DEVICES["npu1"](), x=shape)
    assert aie_utils.get_current_device(probe_runtime=False) is previous
    assert net.plan.image == "xclbin" and net.plan.dispatch == "separate"
    assert net.plan.reasons[-1] == "boundaries=each_step: the xclbin form that is built"
    assert net.image is not None and Path(net.image).stat().st_size > 0
