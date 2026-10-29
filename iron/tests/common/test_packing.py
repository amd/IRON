# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's packing entries, device-free: round trips, matching, and a
recording's packed designs composed into one device configuration.
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


def test_packing_of_matches_by_class_and_dims(npu2):
    profile = _packed((GEMV, {"K": 2048}, {"num_aie_columns": 2}), (SiLU, {}))
    assert profile.packing_of(GEMV(M=512, K=2048).resolved(npu2)) == (
        0,
        {"num_aie_columns": 2},
    )
    assert profile.packing_of(GEMV(M=512, K=8192).resolved(npu2)) is None
    assert profile.packing_of(SiLU(size=2048).resolved(npu2)) == (0, None)


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
