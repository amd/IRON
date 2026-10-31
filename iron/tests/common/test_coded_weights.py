# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A weight a coded operand reads, recorded device-free: the recorder binds
the coded rows derived from it, one buffer for every such read, and the
graph's reference still reads the weight itself.
"""

import os
import re
from collections import Counter

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils import coded
from ml_dtypes import bfloat16
from safetensors.numpy import save_file

import iron
from iron.common.design.design import OperatorDesign
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


def test_a_report_names_each_coded_weight_and_each_read_plain(caplog):
    w, other = _weights()
    t = Chain(w, other).record(x=(E,))
    t.code_weights()
    (line,) = t.coded_report()
    assert line == (
        f"w: coded rows ({E}, {coded.row_bytes(E)}) uint8 (encoded), "
        f"{E * (2 * E - coded.row_bytes(E))} bytes fewer"
    )
    w[5, :120] = np.exp2(np.arange(-60.0, 60.0)).astype(bfloat16)
    t = Chain(w, other).record(x=(E,))
    with caplog.at_level("ERROR"):
        t.code_weights()
    (line,) = t.coded_report()
    assert line.startswith("w: read plain: coded.encode_rows: row 5 holds 104")


def test_a_profile_turns_coding_on_by_gemv_shape(tmp_path):
    """The opt-in is a profile entry, ``"coded_a": true`` for a GEMV shape,
    which round-trips through the profile's JSON like any tunable.
    """
    profile = iron.Profile()
    profile.add(GEMV, M=E, K=E, coded_a=True)
    profile.save(tmp_path / "npu2.json")
    w, other = _weights()

    class Plain(iron.Graph):
        def __init__(self):
            self.w = iron.param(w)
            self.other = iron.param(other[:256])

        def body(self, x):
            y = GEMV.step(self.w, x, tile_size_input=4)
            return GEMV.step(self.other, y, tile_size_input=4)

    graph = Plain()
    graph.profile = iron.Profile.load(tmp_path / "npu2.json")
    t = graph.record(x=(E,))
    assert [s.op.coded_a for s in t.steps] == [True, False]
    assert [s.inputs[0].name for s in t.steps] == ["w.coded", "other"]


def test_a_weight_of_one_matrix_reads_coded_as_a_batch_of_one():
    """Llama's packed decode steps give GEMV num_batches=1: A is (1, M, K)
    of a weight held (M, K).
    """
    w, _ = _weights()

    class OneBatch(iron.Graph):
        def __init__(self):
            self.w = iron.param(w)

        def body(self, x):
            return GEMV.step(self.w, x, coded_a=True, tile_size_input=4, num_batches=1)

    (step,) = OneBatch().record(x=(1, E)).steps
    assert step.inputs[0].name == "w.coded" and step.op.A.shape == (
        1,
        E,
        coded.row_bytes(E),
    )


def _channels(op) -> list:
    """The DMA channels ``op``'s module asks for: per logical tile, its
    kind and the fifos it produces and consumes, and per fifo, the kinds
    of its ends.
    """
    text = str(OperatorDesign(op.resolved()).module())
    kinds = dict(re.findall(r"(%\w+) = aie\.logical_tile<(\w+)>", text))
    tiles, fifos = Counter(), Counter()
    for producer, consumers in re.findall(
        r"aie\.objectfifo @\w+\((%\w+), \{([^}]*)\}", text
    ):
        ends = [c.strip() for c in consumers.split(",")]
        tiles[producer, "out"] += 1
        for c in ends:
            tiles[c, "in"] += 1
        fifos[kinds[producer], tuple(sorted(kinds[c] for c in ends))] += 1
    per_tile = Counter(
        (kinds[t], tiles[t, "out"], tiles[t, "in"]) for t in {t for t, _ in tiles}
    )
    return sorted(per_tile.items()) + sorted(fifos.items())


def test_coding_a_gemv_s_weight_takes_no_channel_more():
    """A packing priced for plain GEMVs must fit coded ones: for each
    catalog shape coding can take, the same fifos between the same kinds
    of tile, and the same count at every tile.
    """
    compared = 0
    for case in GEMV.test.resolve(GEMV, aie_utils.get_current_device()):
        shape = {k: v for k, v in case.kwargs.items() if k != "coded_a"}
        try:
            coded_op = GEMV(**shape, coded_a=True).resolved()
        except ValueError:
            continue  # what coding refuses: K % 64, a re-read, a core's L1
        assert _channels(coded_op) == _channels(GEMV(**shape)), case.label
        compared += 1
    assert compared >= 10


def test_gemvs_sharing_an_array_share_it_coded_and_split_it_mixed():
    """Llama 1B's packed decode runs its q/o, k/v and gate/up GEMVs (K=2048,
    four rows a call, 32 a C tile) on one 8-core array: 32 cores in all,
    the device's every core. Coded alike they still share one array; coded
    on some and not others they need two, 40 cores, and the pack no longer
    places ("no available compute tiles"). coded_a is the array's, so a
    profile codes such GEMVs all or none.
    """

    def array(M, coded_a):
        return GEMV(
            M=M,
            K=E,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=32,
            num_batches=1,
            coded_a=coded_a,
        ).resolved()

    for coded_a in (False, True):
        assert len({array(M, coded_a).array_key() for M in (512, E, 8192)}) == 1
    mixed = {array(512, False).array_key(), array(E, True).array_key()}
    assert len(mixed) == 2
