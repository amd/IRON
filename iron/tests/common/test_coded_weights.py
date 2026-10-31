# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight a coded operand reads, recorded device-free: the recorder binds
the coded rows derived from it, one buffer for every such read, and the
graph's reference still reads the weight itself.
"""

import os

import numpy as np
import pytest
from aie.utils import coded
from ml_dtypes import bfloat16
from safetensors.numpy import save_file

import iron
from iron.common.graph.coded import CodedWeight
from iron.lm import Checkpoint
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


def test_a_weight_past_its_capacity_is_read_plain_with_a_warning(caplog):
    w, other = _weights()
    # Row 5 spans 120 binades: far more exceptions than 15 slots hold.
    w[5, :120] = np.exp2(np.arange(-60.0, 60.0)).astype(bfloat16)
    t = Chain(w, other).record(x=(E,))
    with caplog.at_level("WARNING"):
        t.code_weights()
    (message,) = [r.getMessage() for r in caplog.records]
    assert message.startswith("Chain: w is read plain:") and "row 5 holds" in message
    assert sorted(h.name for _, h in t.weights.values()) == ["other", "w"]
    assert [s.inputs[0].name for s in t.steps] == ["w", "w", "other"]
    assert not any(s.op.coded_a for s in t.steps)
    assert all(b.op in [s.op for s in t.steps] for b in t.bindings)


def _checkpoint(tmp_path, overflow=False):
    """A one-tensor checkpoint, its tensor (a param, as a graph holds it)."""
    w, _ = _weights()
    w = w[:64, :256].copy()
    if overflow:
        w[3, :120] = np.exp2(np.arange(-60.0, 60.0)).astype(bfloat16)
    path = tmp_path / "model.safetensors"
    save_file({"w": w}, path)
    return path, w


def test_a_weight_from_a_file_is_encoded_once_then_read_from_the_cache(tmp_path):
    path, w = _checkpoint(tmp_path)
    cache = tmp_path / "cache"
    held = Checkpoint(path).tree().w
    assert held.source.path == str(
        path.resolve()
    ) and held.source.size == os.path.getsize(path)
    first = CodedWeight(held, "w", 15, held.source, cache)
    rows = first.encode()
    assert not isinstance(rows, np.memmap) and first.cached.exists()
    again = CodedWeight(held, "w", 15, held.source, cache).encode()
    assert isinstance(again, np.memmap)
    assert np.array_equal(again, rows)
    assert np.array_equal(
        coded.decode_rows(again, 256).view(np.uint16), w.view(np.uint16)
    )


def test_a_file_changed_since_is_encoded_again(tmp_path):
    path, _ = _checkpoint(tmp_path)
    cache = tmp_path / "cache"
    held = Checkpoint(path).tree().w
    CodedWeight(held, "w", 15, held.source, cache).encode()
    stat = os.stat(path)
    os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns + 10**9))
    touched = Checkpoint(path).tree().w
    weight = CodedWeight(touched, "w", 15, touched.source, cache)
    assert weight.cached != CodedWeight(held, "w", 15, held.source, cache).cached
    assert not isinstance(weight.encode(), np.memmap)
    assert len(list(cache.glob("*.npy"))) == 2


def test_a_refusal_is_cached_and_a_weight_with_no_file_is_not(tmp_path):
    path, _ = _checkpoint(tmp_path, overflow=True)
    cache = tmp_path / "cache"
    held = Checkpoint(path).tree().w
    for _ in range(2):
        with pytest.raises(ValueError, match="row 3 holds"):
            CodedWeight(held, "w", 15, held.source, cache).encode()
    assert [p.suffix for p in cache.iterdir()] == [".refused"]
    loose = np.array(held[:3])
    CodedWeight(loose, "w", 15, None, cache).encode()
    assert [p.suffix for p in cache.iterdir()] == [".refused"]
