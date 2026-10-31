# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Which folds the tuner proposes, device-free: every fold
(``iron.common.graph.fold``) a recording admits, scoped to the ones that
will not split a device array a call site sharing it does not also take.

A hand-written profile entry still takes any fold ``fold_candidates`` finds
(``chosen_folds``, at build time): the profile stays the authority, so this
scoping lives here, on the tuner's own side of proposing one, not there.
The reason is a packed group's own cost: a shape two call sites share
(Llama's ``q_proj`` and ``o_proj``, one ``GEMV M=2048 K=2048`` array, see
``iron.tests.lm.test_modules.test_a_decode_steps_q_and_o_share_one_array``)
splits into two distinct arrays if only one of them folds, which the group
then pays for in resident cores it did not have before.
"""

from __future__ import annotations

from collections.abc import Hashable, Sequence

from iron.common.declare import Operator, Profile
from iron.common.declare.profile import Version
from iron.common.graph.fold import chosen_folds, fold_candidates
from iron.common.graph.record import Recording
from iron.common.image.step import Fusion, FusionKind

from .autotune import Shape, Timed, _json_safe


def _folded_producer(recording: Recording, fusion: Fusion) -> Operator:
    """The operator ``fusion``'s producer folds into, resolved: each hop's
    ``producer.fold(consumer, at)`` in turn (``apply_folds``'s own loop,
    without touching any step's slots: only the resulting identity, its
    ``array_key()``, is wanted here).
    """
    current = recording.steps[fusion.steps[0]].op
    for edge in fusion.edges:
        nxt = recording.steps[edge.consumer].op
        at = next(k for k, b in enumerate(nxt.inputs) if b.name == edge.input)
        current = current.fold(nxt, at)
    return current.resolved()


def array_scoped_fold_candidates(recording: Recording) -> tuple[Fusion, ...]:
    """``fold_candidates(recording)``, keeping a candidate only where every
    recording step whose (pre-fold, resolved) operator shares its
    producer's ``array_key()`` folds too, to the same resulting
    ``array_key()``: a reference-only step, or one with no kernel of its
    own (``exported_design()``), never shares an array, so it never blocks
    one. A step sharing the array that has no fold at all, or one shaped
    differently, drops every candidate naming that array.
    """
    found = fold_candidates(recording)
    array_of: dict[int, Hashable] = {}
    for i, step in enumerate(recording.steps):
        op = step.op.resolved()
        if op.reference_only or op.exported_design() is not None:
            continue
        array_of[i] = op.array_key()
    members: dict[Hashable, list[int]] = {}
    for i, key in array_of.items():
        members.setdefault(key, []).append(i)
    # fold_candidates orders a chain's depths ascending from the same
    # producer, so the last one kept here is its deepest.
    deepest: dict[int, Fusion] = {}
    for fusion in found:
        deepest[fusion.steps[0]] = fusion
    kept = []
    for fusion in found:
        producer = fusion.steps[0]
        group = members.get(array_of.get(producer), [producer])
        results: set[Hashable] = set()
        complete = True
        for i in group:
            candidate = deepest.get(i)
            if candidate is None:
                complete = False
                break
            results.add(_folded_producer(recording, candidate).array_key())
        if complete and len(results) == 1:
            kept.append(fusion)
    return tuple(kept)


def _entry(
    recording: Recording, fusion: Fusion
) -> tuple[Hashable, list[tuple[type, dict]], tuple[tuple[int, str, int, str], ...]]:
    """``fusion``'s steps (resolved) and local edges, and the key its shape
    (class and dims, not every instance of its class) is deduplicated and
    matched by: two layers of one shape share an entry, a different shape
    of the same classes (``q_proj``'s ``K`` against ``down_proj``'s) does
    not.
    """
    steps = [recording.steps[i].op.resolved() for i in fusion.steps]
    local = {step: i for i, step in enumerate(fusion.steps)}
    edges = tuple(
        (local[e.producer], e.output, local[e.consumer], e.input) for e in fusion.edges
    )
    named = [(type(s), _json_safe(Shape(s).named((), derived=True))) for s in steps]
    key = (fusion.kind, tuple((c, tuple(sorted(d.items()))) for c, d in named), edges)
    return key, named, edges


def propose_folds(recording: Recording) -> tuple[Fusion, ...]:
    """``array_scoped_fold_candidates(recording)``, overlap among them
    resolved the way a profile's own folds are (``chosen_folds``, first in
    step order wins), matched by each shape's own dims (``_entry``): two
    different shapes sharing a class pair (``q_proj``'s ``GEMV M=2048
    K=2048`` and ``down_proj``'s ``M=2048 K=8192``) must not blur into one
    permissive entry that would let ``chosen_folds`` re-admit the one
    scoping dropped.
    """
    permissive = Profile()
    seen = set()
    for fusion in array_scoped_fold_candidates(recording):
        key, named, edges = _entry(recording, fusion)
        if key in seen:
            continue
        seen.add(key)
        permissive.add_fusion(fusion.kind, named, edges)
    return chosen_folds(recording, permissive)


def fold_profile(base: Profile, calls: Sequence[Timed]) -> Profile:
    """``base``'s entries, fusions and packings, with a fold entry added for
    each distinct shape (class, dims and wiring) ``propose_folds`` finds in
    ``calls``' recordings that ``base`` does not already carry, scoped to
    the graph versions (``Recording.version``) it was found in (one shape
    found in more than one call's recording, as a prompt chunk's own
    SwiGLU gate and a decode step's alike can be, is scoped to all of
    them): what ``price_folds_before_packing`` prices packed, against
    ``base`` packed without them, and decides to keep per version
    (``widen_packings`` decides a packing entry's own widening the same
    way). Each step names its own dims (``Shape.named``, as a packing
    entry's members do), not every instance of its class, so a model that
    later grows a same-class pair this never checked does not inherit an
    unscoped fold by matching too broadly; calling this again on its own
    output adds nothing new.
    """
    out = Profile()
    for cls, dims, tunables in base:
        out.add(cls, **dims, **tunables)
    for kind, steps, edges, versions in base.fusions():
        out.add_fusion(kind, steps, edges, versions)
    for entry in base.packings():
        out.add_packing(entry.members, entry.versions)
    existing = {
        (kind, tuple((c, tuple(sorted(d.items()))) for c, d, _ in steps), edges)
        for kind, steps, edges, _ in base.fusions()
    }
    found: dict[Hashable, tuple[FusionKind, list, tuple, set[Version]]] = {}
    for call in calls:
        recording = call.recording
        version = recording.version
        for fusion in propose_folds(recording):
            key, named, edges = _entry(recording, fusion)
            if key in existing:
                continue
            entry = found.setdefault(key, (fusion.kind, named, edges, set()))
            entry[3].add(version)
    for kind, named, edges, versions in found.values():
        out.add_fusion(kind, named, edges, frozenset(versions))
    return out
