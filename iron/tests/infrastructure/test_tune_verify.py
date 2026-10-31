# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a tune saves, checked against the profile it started from (``iron.tune.verify``).

No NPU above ``# On the device``.
"""

import aie.utils as aie_utils
import pytest

import iron
from iron import Profile
from iron.common.declare.profile import PackingEntry
from iron.common.graph.fold import fold_candidates
from iron.common.image.step import FusionKind
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.relu import ReLU
from iron.operators.silu import SiLU
from iron.operators.tanh import Tanh
from iron.tests.support.llama_model import small
from iron.tune.autotune import Timed
from iron.tune.measure import Timing
from iron.tune.verify import (
    entries,
    fingerprint,
    narrowed,
    touches,
    verify,
    write_report,
)

pytestmark = pytest.mark.usefixtures("npu2")

LARGE, SMALL = 2**22, 2**21


class Chain(iron.Graph):
    """ReLU then Tanh: one version per input length."""

    def body(self, x):
        return Tanh.step(ReLU.step(x))


def recorded(profile: Profile) -> list[Timed]:
    graph = Chain()
    graph.profile = profile
    return [Timed(graph.record(x=(n,))) for n in (LARGE, SMALL)]


def test_a_reverted_version_takes_the_base_entries_that_touch_it():
    """Only the small version loses.

    Its own entry and the one both versions match come from the base, a packing scoped
    to both keeps the large one, and an unscoped packing touching the small one is
    dropped.
    """
    large, small_ = (c.recording for c in recorded(Profile()))
    base = Profile()
    base.add(ReLU, size=LARGE, tile_size=1024)
    base.add(Tanh, tile_size=1024)
    candidate = Profile()
    candidate.add(ReLU, size=LARGE, tile_size=2048)
    candidate.add(ReLU, size=SMALL, tile_size=512)
    candidate.add(Tanh, tile_size=2048)
    members = [(ReLU, {}), (Tanh, {})]
    candidate.add_packing(members, [large.version, small_.version])
    candidate.add_packing(members)

    out = narrowed(base, candidate, {small_.version}, [large, small_])

    assert sorted((c.__name__, d, t) for c, d, t in out) == [
        ("ReLU", {"size": LARGE}, {"tile_size": 2048}),
        ("Tanh", {}, {"tile_size": 1024}),
    ]
    assert out.packings() == [
        PackingEntry(candidate.packings()[0].members, frozenset({large.version}))
    ]


def test_a_fold_touches_only_the_version_whose_steps_it_names():
    """``touches`` finds a fold by the fold candidates, not the fusion kinds a profile's other entries take."""
    model = small()
    decode, prompt = (model.record(**s) for s in model.shapes())
    fold = next(
        f
        for f in fold_candidates(decode)
        if type(decode.steps[f.steps[0]].op).__name__ == "SiLU"
    )
    gate, mul = (decode.steps[i].op.resolved() for i in fold.steps)
    assert isinstance(gate, SiLU) and isinstance(mul, ElementwiseMul)
    edge = fold.edges[0]
    entry = (
        FusionKind.FOLD,
        [(SiLU, {"size": gate.size}), (ElementwiseMul, {"size": mul.size})],
        [(0, edge.output, 1, edge.input)],
        None,
    )
    assert touches("fusion", entry, decode)
    assert not touches("fusion", entry, prompt)
    scoped = (*entry[:3], frozenset({prompt.version}))
    assert not touches("fusion", scoped, decode)


def test_a_fingerprint_moves_with_a_tunable_and_not_with_an_entry_elsewhere():
    dev = aie_utils.ensure_current_device()
    [large, _] = recorded(Profile())
    other = Profile()
    other.add(ReLU, size=SMALL, tile_size=512)
    moved = Profile()
    moved.add(ReLU, size=LARGE, tile_size=512)
    [other_large, _], [moved_large, _] = recorded(other), recorded(moved)
    assert fingerprint(large, Profile(), dev) == fingerprint(other_large, other, dev)
    assert fingerprint(moved_large, moved, dev) != fingerprint(large, Profile(), dev)


def test_a_report_names_what_the_saved_profile_adds_and_drops(tmp_path):
    start = Profile()
    start.add(Tanh, tile_size=1024)
    saved = Profile()
    saved.add(ReLU, size=LARGE, tile_size=2048)
    write_report(tmp_path / "npu2.json", start, saved, {}, note="seen")
    text = (tmp_path / "npu2.report.txt").read_text()
    assert f"tunables ReLU size={LARGE} " in text and "tunables Tanh" in text
    assert entries(saved) == {f'tunables ReLU size={LARGE} {{"tile_size": 2048}}'}
    assert (tmp_path / "npu2.report.json").exists() and "seen" in text


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_verify_keeps_the_version_that_gains_and_reverts_the_one_that_loses():
    """The large version's candidate widens the one column the base gives its ReLU; the small version's candidate narrows its ReLU to one.

    Slower at this length. What is kept is the first alone, and the small version, back
    at the base, is not reported.
    """
    dev = aie_utils.ensure_current_device()
    base = Profile()
    base.add(ReLU, size=LARGE, num_aie_columns=1)
    candidate = Profile()
    candidate.add(ReLU, size=LARGE, num_aie_columns=8)
    candidate.add(ReLU, size=SMALL, num_aie_columns=1)

    kept, checks = verify(
        recorded, dev, base, candidate, timing=Timing(rounds=3, calls=10)
    )

    assert [(c.__name__, d, t) for c, d, t in kept] == [
        ("ReLU", {"size": LARGE}, {"num_aie_columns": 8})
    ]
    [(version, check)] = checks.items()
    assert version == recorded(Profile())[0].recording.version
    assert check.gains, check
