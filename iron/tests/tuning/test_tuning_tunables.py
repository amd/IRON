# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transformation tests for operator tunables, every operator in the catalog at a small size."""

import pytest
from aie.iron.device import NPU2

from iron.common.declare import Profile
from iron.common.declare.composition import Refinement, refinement
from iron.common.graph.record import Recording
from iron.common.image.step import BufferRef, SequenceStep
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.sample import Sample
from iron.tests.support.declared import declared
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.packings import width_tunables
from iron.tune.search import candidates, check, fit, measure, search

NPU2_DEVICE = NPU2()

pytestmark = pytest.mark.usefixtures("npu2")


def _smallest_cases():
    """Return each catalog operator's own first declared case, its smallest by convention."""
    found = {}
    for name, cls, case in declared(NPU2_DEVICE):
        found.setdefault(cls, (name, case))
    return found


_CASES = _smallest_cases()
_PARAMS = [
    pytest.param(cls, case, id=name)
    for cls, (name, case) in sorted(_CASES.items(), key=lambda kv: kv[1][0])
]
_PARAMS_WITH_TUNABLES = [p for p in _PARAMS if p.values[0].declaration.tunables]


def _dims_only(cls, kwargs):
    """Return ``kwargs`` with the tunable fields dropped, so ``resolve()`` fills them unpinned."""
    tunables = set(cls.declaration.tunables)
    return {name: value for name, value in kwargs.items() if name not in tunables}


@unbuilt
@pytest.mark.parametrize("cls,case", _PARAMS)
def test_declared_domains_are_resolvable_candidates(cls, case, tmp_path):
    """Every resolvable combination of an operator's declared domains is a candidate."""
    op = cls(**_dims_only(cls, case.kwargs)).resolved(NPU2_DEVICE)
    recording = Recording.of_step(op)
    domains = op._domains(NPU2_DEVICE)
    profile = Profile()
    if cls.declaration.tunables:
        given = {n: vars(op)[n] for n in cls.declaration.tunables}
        profile.add(cls, **given)
        path = tmp_path / "profile.json"
        profile.save(path)
        loaded = Profile.load(path)
        assert loaded.tunables_for(cls, _dims_only(cls, case.kwargs)) == given
        profile = loaded
    found = list(candidates([Timed(recording)], profile, NPU2_DEVICE))
    for name, values in domains.items():
        for value in values:
            matching = [
                e
                for e in found
                if e.touches == frozenset({0})
                and vars(e.apply(profile).entries()[-1].root.parts[0])[name] == value
            ]
            assert (
                matching
            ), f"{cls.__name__}.{name}={value} is not among the candidates"


@unbuilt
def test_a_small_m_may_resolve_to_gemv_or_gemm():
    """A step's implementation domain, at a small ``M``, holds both ``GEMV`` and ``GEMM``."""
    gemv = GEMV(M=128, K=128).resolved(NPU2_DEVICE)
    recording = Recording.of_step(gemv)
    profile = Profile()
    found = list(candidates([Timed(recording)], profile, NPU2_DEVICE))
    implementations = {
        part.cls for e in found for part in e.apply(profile).entries()[-1].root.parts
    }
    assert {GEMV, GEMM} <= implementations


def test_a_resolve_derived_tunable_is_never_a_width():
    """``a_depth``, filled by ``resolve()``, is never among a ``GEMV``'s width tunables."""
    op = GEMV(M=128, K=128).resolved(NPU2_DEVICE)
    assert "a_depth" not in width_tunables(op)


@unbuilt
@pytest.mark.parametrize("cls,case", _PARAMS_WITH_TUNABLES)
@pytest.mark.supported_devices("npu2")
def test_each_tunable_moved_alone_is_held_to_its_own_refinement(cls, case):
    """Each declared tunable moved alone off the recorded setting is held to its own ``refinement``, and the tuner's pick fits the device."""
    recorded = cls(**case.kwargs).resolved(NPU2_DEVICE)
    recording = Recording.of_step(recorded)
    given = {n: vars(recorded)[n] for n in cls.declaration.tunables}
    base = Profile()
    base.add(cls, **given)
    domains = recorded._domains(NPU2_DEVICE)
    for name in cls.declaration.tunables:
        rule = refinement(cls, name)
        for value in domains.get(name, ()):
            if value == given.get(name):
                continue
            moved = Profile()
            moved.add(cls, **{**given, name: value})
            result = check(
                moved, base, [Timed(recording)], NPU2_DEVICE, refinement=rule
            )
            assert result.ok, result.why
    calls = [Timed(recording)]
    tuned = search(calls, base, NPU2_DEVICE, budget_s=1.0)
    assert check(tuned, base, calls, NPU2_DEVICE, refinement=Refinement.NO_WORSE).ok
    assert measure(tuned, base, calls, NPU2_DEVICE).ratio < 1.05


@unbuilt
def test_search_keeps_the_fastest_setting_it_measured_on_the_one_operator_toy():
    """The tuner, on the one-operator toy, keeps the fastest setting it measured, never asserting which one."""
    op = GEMV(M=128, K=128).resolved(NPU2_DEVICE)
    recording = Recording.of_step(op)
    start = Profile()
    calls = [Timed(recording)]
    tuned = search(calls, start, NPU2_DEVICE, budget_s=5.0)
    assert check(tuned, start, calls, NPU2_DEVICE, refinement=Refinement.NO_WORSE).ok
    assert measure(tuned, start, calls, NPU2_DEVICE).ratio < 1.05


@unbuilt
def test_a_setting_the_array_cannot_hold_is_refused_before_any_build():
    """A setting the array can't hold (more columns than the device) is refused by ``fit`` before any build."""
    op = GEMV(M=128, K=128).resolved(NPU2_DEVICE)
    recording = Recording.of_step(op)
    profile = Profile()
    profile.add(GEMV, M=128, K=128, num_aie_columns=NPU2_DEVICE.cols * 2)
    result = fit(profile, [Timed(recording)], NPU2_DEVICE)
    assert not result.ok
    assert result.stage == "counts"


@unbuilt
def test_a_no_worse_change_upstream_of_a_selection_step_is_refused():
    """A no-worse change upstream of a ``Sample`` step (the selection slice) is refused."""
    gemv = GEMV(M=128, K=128).resolved(NPU2_DEVICE)
    sample = Sample(vocab=128, cores=1, steps=1).resolved(NPU2_DEVICE)
    steps = [
        SequenceStep(gemv, tuple(BufferRef(n) for n in ("A", "B", "logits"))),
        SequenceStep(
            sample,
            tuple(BufferRef(n) for n in ("logits", "draws", "tokens", "token")),
        ),
    ]
    recording = Recording.of_steps(
        "gemv_into_sample", steps, ["A", "B", "draws"], ["tokens", "token"]
    )
    profile = Profile()
    profile.add(GEMV, M=128, K=128, kernel_vector_size=8)
    result = check(
        profile,
        Profile(),
        [Timed(recording)],
        NPU2_DEVICE,
        refinement=Refinement.NO_WORSE,
    )
    assert not result.ok
