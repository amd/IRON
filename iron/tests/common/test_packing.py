# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's packing entries, device-free.

Round trips, matching (in the graph versions an entry names), and a recording's packed
designs composed into one device configuration.
"""

import re

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.common.design import OperatorDesign
from iron.common.graph.packing import apply as apply_packings
from iron.common.image.compose import Composition, Packing
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU

pytestmark = pytest.mark.usefixtures("npu2")

UP = np.zeros(2048, bfloat16)


class Projection(iron.Graph):
    """``ElementwiseMul(SiLU(W @ x), UP)``: three designs, a decode MLP's."""

    def body(self, w, x):
        y = GEMV.step(w, x)
        gate = SiLU.step(y, tile_size=256)
        return ElementwiseMul.step(gate, UP, tile_size=256)


class Copied(iron.Graph):
    def body(self, x):
        return Copy.step(x)


class Gated(iron.Graph):
    """``ElementwiseMul(SiLU(x), UP)``, and given ``extra`` a copy of it too.

    Two versions over the same SiLU and multiply arrays, as a decode step and a prompt
    chunk share theirs.
    """

    def body(self, x, extra=None):
        y = ElementwiseMul.step(SiLU.step(x, tile_size=256), UP, tile_size=256)
        if extra is None:
            return y
        return y, Copy.step(extra)


def _packed(*members):
    profile = Profile()
    profile.add_packing(members)
    return profile


def _recording():
    return Projection().record(w=(2048, 2048), x=(2048,))


def test_a_profile_round_trips_a_packing(tmp_path):
    p = Profile()
    p.add(SiLU, num_aie_columns=8)
    p.add_packing(
        [(GEMV, {"M": 2048, "K": 2048}, {"num_aie_columns": 2}), (SiLU, {"size": 2048})]
    )
    p.add_packing(
        [(SiLU, {"size": 2048}), (ElementwiseMul, {})],
        versions=[(), (("ids", (2048,), "int32"),)],
    )
    path = tmp_path / "npu2.json"
    p.save(path)
    loaded = Profile.load(path)
    assert loaded.packings() == p.packings()
    assert list(loaded) == list(p)


def test_add_packing_checks_its_members():
    with pytest.raises(TypeError, match="at least two members"):
        Profile().add_packing([(SiLU, {})])
    with pytest.raises(TypeError, match="declares no dim"):
        Profile().add_packing([(SiLU, {"rows": 1}), (GEMV, {})])
    with pytest.raises(TypeError, match="no tunable"):
        Profile().add_packing([(SiLU, {}, {"M": 2}), (GEMV, {})])
    with pytest.raises(TypeError, match="at least one version"):
        Profile().add_packing([(SiLU, {}), (GEMV, {})], versions=[])


def test_load_refuses_a_packing_that_is_only_its_members(tmp_path):
    path = tmp_path / "npu2.json"
    path.write_text(
        '{"entries": [], "packings": [[{"operator": "SiLU"}, {"operator": "GEMV"}]]}'
    )
    with pytest.raises(ValueError, match="a packing is"):
        Profile.load(path)


def test_packings_of_matches_by_class_and_dims(npu2):
    profile = _packed((GEMV, {"K": 2048}, {"num_aie_columns": 2}), (SiLU, {}))
    assert profile.packings_of(GEMV(M=512, K=2048).resolved(npu2), ()) == [
        (0, 0, {"num_aie_columns": 2})
    ]
    assert profile.packings_of(GEMV(M=512, K=8192).resolved(npu2), ()) == []
    assert profile.packings_of(SiLU(size=2048).resolved(npu2), ()) == [(0, 1, None)]


def test_a_shape_two_entries_name_goes_to_the_one_naming_more_of_the_graph(npu2):
    """Two models sharing a profile can name one shape (the same MLP width) in different entries.

    The step joins the entry naming most of the recording's shapes, wherever it stands
    in the profile, so another model's grouping does not split this one's.
    """
    recording = Gated().record(x=(2048,))
    profile = Profile()
    # Another model's: names this graph's SiLU, and a GEMV it does not run.
    profile.add_packing(
        [(SiLU, {}, {"num_aie_columns": 2}), (GEMV, {"M": 512, "K": 8192})]
    )
    profile.add_packing(
        [
            (SiLU, {}, {"num_aie_columns": 1}),
            (ElementwiseMul, {}, {"num_aie_columns": 1}),
        ]
    )
    silu = recording.steps[0].op.resolved(npu2)
    assert [index for index, _, _ in profile.packings_of(silu, ())] == [0, 1]
    packed, packing = apply_packings(recording, profile, (), npu2)
    silu, mul = (s.op.resolved(npu2) for s in packed.steps)
    assert silu.num_aie_columns == mul.num_aie_columns == 1
    assert packing == Packing((tuple(OperatorDesign(op).name for op in (silu, mul)),))


def test_a_recording_s_version_is_each_input_s_name_shape_and_dtype():
    assert Gated().record(x=(2048,), extra=(64,)).version == (
        ("x", (2048,), "bfloat16"),
        ("extra", (64,), "bfloat16"),
    )
    assert Gated().record(x=(2048,)).version == (("x", (2048,), "bfloat16"),)


def test_a_packing_applies_only_in_the_versions_it_names(npu2):
    """One graph's two versions run the same SiLU and multiply arrays.

    An entry naming one version groups them there and leaves the other's steps as they
    were.
    """
    alone = Gated().record(x=(2048,))
    copying = Gated().record(x=(2048,), extra=(64,))
    profile = Profile()
    profile.add_packing(
        [
            (SiLU, {}, {"num_aie_columns": 1}),
            (ElementwiseMul, {}, {"num_aie_columns": 1}),
        ],
        versions=[alone.version],
    )
    silu = alone.steps[0].op.resolved(npu2)
    assert profile.packings_of(silu, alone.version) == [(0, 0, {"num_aie_columns": 1})]
    assert profile.packings_of(silu, copying.version) == []
    packed, packing = apply_packings(alone, profile, (), npu2)
    assert len(packing.groups) == 1 and len(packing.groups[0]) == 2
    assert all(s.op.resolved(npu2).num_aie_columns == 1 for s in packed.steps)
    packed, packing = apply_packings(copying, profile, (), npu2)
    assert packed is copying and packing == Packing()


def test_apply_narrows_the_members_and_groups_their_designs(npu2):
    recording = _recording()
    profile = _packed(
        (GEMV, {}, {"num_aie_columns": 2, "num_channels": 2}),
        (SiLU, {}, {"num_aie_columns": 1}),
        (ElementwiseMul, {}, {"num_aie_columns": 1}),
    )
    packed, packing = apply_packings(recording, profile, (), npu2)
    gemv, silu, mul = (s.op.resolved(npu2) for s in packed.steps)
    assert (gemv.num_aie_columns, gemv.num_channels) == (2, 2)
    assert silu.num_aie_columns == mul.num_aie_columns == 1
    names = tuple(OperatorDesign(op).name for op in (gemv, silu, mul))
    assert packing == Packing((names,))
    # Every per-call value the narrowed steps read is bound to them.
    bound = {id(b.op) for b in packed.bindings}
    assert all(id(s.op) in bound for s in packed.steps if s.op.values)


def test_apply_resolves_a_member_afresh_at_its_tunables(npu2):
    """A Copy's tile_size follows its channels.

    Given two, a 64-element copy resolves 32-element tiles, not the 64 it resolved at
    one.
    """
    recording = Copied().record(x=(64,))
    assert recording.steps[0].op.resolved(npu2).tile_size == 64
    profile = _packed(
        (Copy, {"input_buffer_size": 64}, {"num_channels": 2}), (SiLU, {"size": 2048})
    )
    packed, _ = apply_packings(recording, profile, [], npu2)
    op = packed.steps[0].op.resolved(npu2)
    assert (op.num_channels, op.tile_size) == (2, 32)


def test_a_packing_composes_its_designs_into_one_device(npu2):
    recording = _recording()
    profile = _packed(
        (GEMV, {}, {"num_aie_columns": 2, "num_channels": 2}),
        (SiLU, {}, {"num_aie_columns": 1}),
        (ElementwiseMul, {}, {"num_aie_columns": 1}),
    )
    packed, packing = apply_packings(recording, profile, (), npu2)
    seq = Image(packed, FullELF(packing=packing))
    seq._prepare()
    (group,) = packing.groups
    devices = re.findall(
        r"^  aie\.device\(\w+\) @(\w+) \{$", Composition(seq).text(), re.M
    )
    assert devices == [Packing.device_name(list(group))]


def test_a_fused_step_is_left_to_its_fusion(npu2):
    recording = _recording()
    profile = _packed((GEMV, {}), (SiLU, {}), (ElementwiseMul, {}))
    fused = (Fusion(FusionKind.STREAM, (1, 2), (Edge(1, "y", 2, "a"),)),)
    _, packing = apply_packings(recording, profile, fused, npu2)
    assert packing == Packing()


def test_a_profile_without_packings_changes_nothing(npu2):
    recording = _recording()
    packed, packing = apply_packings(recording, Profile(), (), npu2)
    assert packed is recording and packing == Packing()
