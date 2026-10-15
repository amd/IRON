# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Per-call values on an image without a scratchpad build as dispatch-time kernels.

An xclbin run has no parameter scratchpad (XRT gives one to a module run
only), so on that image a graph's per-call values become dispatch-time
scalars of the kernels that use them: an offset use adds the scalar to the transfer's offset and
the kernel's stream is regenerated per call by the host library aiecc's
``--get-npu-cpp`` output compiles to; a core-read use is a resident the
sequence writes from the scalar before the barrier (the dialect takes the
RTP write's value as an operand). Both are built here as xclbins on
both devices; running them on a device is the other half.
"""

from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
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

    return g, cache, (R, C)


def test_values_become_dispatch_time_kernels_at_each_step(device):
    g, _, shape = _graph()
    net = g.compile(
        dev=device,
        full_elf=False,
        x=shape,
    )
    assert not net.plan.full_elf
    kinds = {name: text for name, _, text in net.plan.values}
    assert (
        "dispatch-time scalar" in kinds["n"] and "dispatch-time scalar" in kinds["pos"]
    )
    chain = net.sequence._image
    assert chain is not None
    designs = {
        type(op).__name__: chain.links[id(op)].design
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


@pytest.mark.supported_devices("npu2")
def test_each_call_softmaxes_its_columns_and_copies_them_into_its_slot():
    """The xclbin form run: each call's row length sizes both steps' streams,
    the copy's down to its innermost dimension, and its slot moves the copy.
    """
    g, cache, shape = _graph()
    net = g.compile(full_elf=False, x=shape)
    assert not net.plan.full_elf
    (softmax,) = [s.op for s in net.traced.steps if isinstance(s.op, Softmax)]
    tolerance = softmax.resolved().tolerance()
    rows, cols = shape
    slots = np.asarray(net.read(cache)).size // (rows * cols)
    rng = np.random.default_rng(0)
    for n, pos in ((cols, 0), (100, 2), (16, slots - 1)):
        before = rng.standard_normal((rows, slots, cols)).astype(bfloat16)
        net.write(cache, before)
        x = rng.standard_normal(shape).astype(bfloat16)
        y = np.asarray(net(x, n=n, pos=pos).numpy()).reshape(shape)[:, :n]
        f = x[:, :n].astype(np.float32)
        e = np.exp(f - f.max(axis=1, keepdims=True))
        verdict = compare(
            y, (e / e.sum(axis=1, keepdims=True)).astype(bfloat16), tolerance
        )
        assert verdict, f"{n=}: {verdict.detail}"
        want = before.copy()
        want[:, pos, :n] = y
        got = np.asarray(net.read(cache)).reshape(want.shape)
        wrong = np.argwhere(got.view(np.uint16) != want.view(np.uint16))
        assert wrong.size == 0, f"{n=} {pos=}: {len(wrong)} differ, first {wrong[:4]}"


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
        dev=npu2,
        full_elf=False,
        q=(1, heads, d),
        k=(kv_heads, cache, d),
        v=(kv_heads, cache, d),
    )
    assert not net.plan.full_elf
    assert net.image is not None and Path(net.image).stat().st_size > 0


def test_npu1_compiles_each_step_unasked():
    """NPU1 has no full-ELF dispatch, so a plain ``compile()`` there takes
    the xclbin form that is built, one dispatch per step.
    """
    g, _, shape = _graph()
    previous = aie_utils.get_current_device(probe_runtime=False)
    net = g.compile(dev=DEVICES["npu1"](), x=shape)
    assert aie_utils.get_current_device(probe_runtime=False) is previous
    assert not net.plan.full_elf
    assert net.plan.reasons == ["npu1 (AIE2) has no full-ELF dispatch"]
    assert net.image is not None and Path(net.image).stat().st_size > 0
