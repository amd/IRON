# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A module joins several graphs over one buffer plan (§8): names and ranges."""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.module import trace_module
from iron.common.packaging import ELF, XCLBIN, plan
from iron.operators.gemv.op import GEMV
from iron.operators.silu.op import SiLU
from iron.operators.strided_copy.op import StridedCopy

E, H, L = 256, 512, 4


@pytest.fixture(autouse=True)
def shim_limit(monkeypatch):
    import iron.common.operator_bases as bases

    monkeypatch.setattr(bases, "get_shim_dma_limit", lambda dev: 16)


def _graphs():
    w = np.zeros((H, E), dtype=bfloat16)
    cache = iron.state((1, L * H), name="cache")
    copy = dict(
        input_sizes=(1, H),
        input_strides=(H, 1),
        input_offset=0,
        output_sizes=(1, 1, H),
        output_strides=(0, L * H, 1),
        output_offset=0,
        num_aie_channels=1,
    )

    @iron.graph
    def write(x, *, pos: iron.common.declare.Scratchpad[np.int32]):
        h = GEMV(w, x, num_aie_columns=4, tile_size_input=4, tile_size_output=H // 4)
        StridedCopy(h, cache, out_offset=pos, **copy)
        return SiLU(h, num_aie_columns=4, tile_size=H // 4)

    @iron.graph
    def read(x):
        h = GEMV(w, x, num_aie_columns=4, tile_size_input=4, tile_size_output=H // 4)
        return SiLU(h, num_aie_columns=4, tile_size=H // 4)

    return write, read, w, cache


def test_a_module_prefixes_private_buffers_and_shares_weights_and_state():
    write, read, w, cache = _graphs()
    joined, ranges = trace_module(
        "m", write=(write, dict(x=(1, E))), read=(read, dict(x=(1, E)))
    )
    assert ranges == {"write": (0, 3), "read": (3, 5)}
    names = [n for _, *bufs in joined.runlist for n in bufs]
    # Inputs and intermediates are the graph's own.
    assert "write.x" in names and "read.x" in names
    assert not any(n == "x" for n in names)
    # The weight is one buffer, named once; the state is its own name.
    weight_names = {n for n in names if n.startswith("w") and not n.startswith("write")}
    assert len(weight_names) == 1, weight_names
    assert "cache" in names
    assert set(joined.pinned) == weight_names | {"cache"}
    # The joined trace's inputs/outputs/values are every graph's, in order.
    assert joined.input_args == ["write.x", "read.x"]
    assert joined.output_args == ["write.out", "read.out"]
    assert [v.name for v in joined.values] == ["pos"]
    # The sequence a module builds names its entry points.
    seq = joined.sequence()
    assert seq.runlist == joined.runlist


def test_a_module_is_one_elf_on_npu2_and_a_per_step_chain_elsewhere():
    write, read, *_ = _graphs()
    joined, _ = trace_module("m", write=(write, dict(x=(1, E))), read=(read, dict(x=(1, E))))
    assert plan("npu2", joined).image == ELF
    p = plan("npu1", joined, boundaries="each_step")
    assert p.image == XCLBIN and p.dispatch == "separate"


def test_two_graphs_may_not_share_a_value_name():
    write, read, *_ = _graphs()

    @iron.graph
    def other(x, *, pos: iron.common.declare.Scratchpad[np.int32]):
        return SiLU(x, num_aie_columns=4, tile_size=H // 4)

    with pytest.raises(ValueError, match="same name"):
        trace_module("m", write=(write, dict(x=(1, E))), other=(other, dict(x=(1, H))))
