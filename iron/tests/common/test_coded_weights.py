# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight a coded operand reads, recorded device-free: the recorder binds
the coded rows derived from it, one buffer for every such read, and the
graph's reference still reads the weight itself.
"""

import numpy as np
import pytest
from aie.utils import coded
from ml_dtypes import bfloat16

import iron
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU

E = 2048

pytestmark = pytest.mark.usefixtures("npu2")


class Chain(iron.Graph):
    """Two GEMVs of one weight, and a GEMV of another weight left plain."""

    def __init__(self, w, other, coded_a=True):
        self.w = iron.param(w)
        self.other = iron.param(other)
        self.coded_a = coded_a

    def body(self, x):
        y = GEMV.step(self.w, x, coded_a=self.coded_a, tile_size_input=4)
        y = GEMV.step(self.w, y, coded_a=self.coded_a, tile_size_input=4)
        return GEMV.step(self.other, y, tile_size_input=4)


def _weights(seed=0):
    rng = np.random.default_rng(seed)
    w = (rng.standard_normal((E, E)) * 0.05).astype(bfloat16)
    other = (rng.standard_normal((E, E)) * 0.05).astype(bfloat16)
    return w, other


def test_every_coded_read_of_a_weight_shares_one_derived_buffer():
    w, other = _weights()
    t = Chain(w, other).record(x=(E,))
    R = coded.row_bytes(E)
    names = {h.name: (h.shape, h.dtype) for _, h in t.weights.values()}
    assert names == {
        "w": ((E, E), bfloat16),
        "other": ((E, E), bfloat16),
        "w.coded": ((E, R), np.uint8),
    }
    first, second, third = (s.inputs[0].name for s in t.steps)
    assert first == second == "w.coded" and third == "other"


def test_a_compile_keeps_no_buffer_of_a_weight_only_coded_reads_read():
    w, other = _weights()
    t = Chain(w, other).record(x=(E,))
    t.code_weights()
    assert sorted(h.name for _, h in t.weights.values()) == ["other", "w.coded"]
    assert "w" not in t.pinned and t.pinned["w.coded"] == E * coded.row_bytes(E)
    rows, _ = next(v for v in t.weights.values() if v[1].name == "w.coded")
    assert np.array_equal(
        coded.decode_rows(rows.encode(), E).view(np.uint16), w.view(np.uint16)
    )


def test_the_reference_reads_the_weight_a_coded_read_codes():
    w, other = _weights()
    x = np.random.default_rng(1).standard_normal(E).astype(bfloat16)
    plain = Chain(w, other, coded_a=False).reference(x)
    got = Chain(w, other).reference(x)
    assert np.array_equal(got.view(np.uint16), plain.view(np.uint16))


def test_a_coded_read_of_an_activation_is_refused():
    class Activation(iron.Graph):
        def body(self, a, x):
            return GEMV.step(SiLU.step(a), x, coded_a=True, tile_size_input=4)

    with pytest.raises(TypeError, match="is not a whole weight"):
        Activation().record(a=(E, E), x=(E,))
