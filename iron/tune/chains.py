# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Choosing which on-chip chains to take.

A graph admits more edges (``iron.common.graph.chain.candidates``) than a
profile should name: fusing one may cost more than it saves, or two may
overlap at one step. ``price_chains`` times each edge the calls' graphs
admit, as a whole, against the same pair unchained (``measure_chain``), and
keeps those that gain beyond the noise, cheapest first, skipping one that
would share a step with an edge already taken (``select_rewrites``, kept
kind-agnostic: a fold or a pack prices and selects the same way, over its
own ``Candidate``).
"""

from __future__ import annotations

import dataclasses
import json
import logging
import math
from collections.abc import Callable, Hashable, Mapping, Sequence
from typing import Any, Protocol

import numpy as np

from iron.common.declare import Operator, Profile
from iron.common.design import OperatorDesign
from iron.common.graph.chain import candidates
from .autotune import Shape, Timed, Trial
from .measure import Cache, Timing, measure_chain

logger = logging.getLogger(__name__)


class ChainGroup:
    """Every occurrence of one producer shape's output chained into one
    consumer shape's input, across a tuner's calls: what ``time_chain_group``
    prices as a whole, and one chain entry covers (``Profile.add_chain``).
    """

    def __init__(self, producer: Operator, consumer: Operator, output: str, input: str):
        self.producer = producer
        self.consumer = consumer
        self.producer_shape = Shape(producer)
        self.consumer_shape = Shape(consumer)
        self.output = output
        self.input = input
        # Each distinct identity's weighted points: both operators' per-call
        # values, as an operator's own time is weighed (``Timed.op_points``).
        self.points: list[tuple[float, dict[str, int], dict[str, int]]] = []
        self.producer_inputs: dict[str, np.ndarray] = {}
        self.consumer_inputs: dict[str, np.ndarray] = {}
        # (recording id, producer step index): every occurrence of this
        # edge, so a group sharing a step with one taken first is seen to.
        self.occurrences: list[tuple[int, int]] = []

    @property
    def key(self) -> Hashable:
        return (self.producer_shape.key, self.consumer_shape.key, self.input)

    def claims(self) -> set[tuple[int, int]]:
        """The (recording, step) pairs this edge's producer and consumer
        occupy, in every recording it runs in.
        """
        out: set[tuple[int, int]] = set()
        for rid, p in self.occurrences:
            out.add((rid, p))
            out.add((rid, p + 1))
        return out

    def __str__(self) -> str:
        return f"{self.producer_shape} -> {self.consumer_shape}.{self.input}"


def chain_groups(calls: Sequence[Timed], dev) -> list[ChainGroup]:
    """The producer -> consumer edges ``calls``' recordings admit
    (``candidates``), grouped by (producer shape, consumer shape, input), in
    the order first seen. A shape's points and inputs are taken from its
    first distinct identity alone, as ``autotune.shapes`` takes an
    operator's; every occurrence is kept, so an edge sharing a step with
    another is seen regardless of how many times either recurs.
    """
    found: dict[Hashable, ChainGroup] = {}
    seen: set[tuple[str, str]] = set()
    for call in calls:
        rid = id(call.recording)
        points = (
            [(1.0, call.values)]
            if not call.points
            else [(p.weight, p.values) for p in call.points]
        )
        for edge in candidates(call.recording):
            # op_values/op_inputs match a binding's op by identity: the
            # recording's own (unresolved) op, not a resolved copy of it.
            raw_producer = call.recording.steps[edge.producer].op
            raw_consumer = call.recording.steps[edge.producer + 1].op
            producer = raw_producer.resolved(dev)
            consumer = raw_consumer.resolved(dev)
            group = ChainGroup(producer, consumer, edge.output, edge.input)
            group = found.setdefault(group.key, group)
            group.occurrences.append((rid, edge.producer))
            identity = (
                OperatorDesign(producer).identity,
                OperatorDesign(consumer).identity,
            )
            if identity in seen:
                continue
            seen.add(identity)
            group.producer_inputs = call.op_inputs(raw_producer)
            group.consumer_inputs = call.op_inputs(raw_consumer)
            for weight, point_values in points:
                group.points.append(
                    (
                        weight,
                        call.op_values(raw_producer, point_values),
                        call.op_values(raw_consumer, point_values),
                    )
                )
    return list(found.values())


def time_chain_group(
    group: ChainGroup,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> Trial:
    """``group`` priced as a whole: ``measure_chain`` at each of its points,
    weighted as ``autotune._time`` weighs an operator's; refused where any
    point's chain is.
    """
    delta = 0.0
    variance: float | None = 0.0
    refused: str | None = None
    for weight, p_values, c_values in group.points:
        m = measure_chain(
            group.producer,
            group.consumer,
            group.output,
            group.input,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            producer_values=p_values,
            consumer_values=c_values,
            producer_inputs=group.producer_inputs,
            consumer_inputs=group.consumer_inputs,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
        if m.refused is not None:
            refused = refused or m.refused
            continue
        d, noise = m.difference()
        delta += weight * d
        variance = (
            None
            if variance is None or noise is None
            else variance + (weight * noise) ** 2
        )
    noise_us = None if variance is None else math.sqrt(variance)
    return Trial({}, delta, noise_us, refused)


def _nameable(dims: Mapping[str, Any]) -> bool:
    """Whether ``dims`` (a ``Shape.named`` result) round-trips through JSON,
    as a profile entry's dims must: a param whose value is not (an access
    pattern, say) cannot name a chain entry.
    """
    try:
        json.dumps(dims)
        return True
    except TypeError:
        return False


class Candidate(Protocol):
    """What ``select_rewrites`` needs of a priced rewrite, chain or
    otherwise: the steps it would claim, by (recording, step index).
    """

    def claims(self) -> set[tuple[int, int]]: ...

    def __str__(self) -> str: ...


def select_rewrites(
    priced: Sequence[tuple[Candidate, Trial]], log: Callable[[str], None] = print
) -> list[Candidate]:
    """Of ``priced`` candidates and their trials, those that gain beyond the
    noise (``Trial.gains``), cheapest first, skipping one whose steps
    overlap a candidate already taken. Kind-agnostic: a chain, a fold or a
    pack is a ``Candidate`` the same way.
    """
    taken: list[Candidate] = []
    claimed: set[tuple[int, int]] = set()
    for candidate, trial in sorted(
        (ct for ct in priced if ct[1].gains), key=lambda ct: ct[1].delta_us
    ):
        if candidate.claims() & claimed:
            log(f"  {candidate}: skipped, overlaps an edge already taken")
            continue
        taken.append(candidate)
        claimed |= candidate.claims()
        log(f"  {candidate}: taken")
    return taken


def price_chains(
    calls: Sequence[Timed],
    dev,
    profile: Profile | None = None,
    *,
    full_elf: bool,
    timing: Timing = Timing(),
    repeats: int = 9,
    cache: Cache | None = None,
    remeasure: bool = False,
    log: Callable[[str], None] = print,
) -> Profile:
    """``profile`` with a chain entry for each edge ``calls``' graphs admit
    that gains beyond the noise (``time_chain_group``, ``select_rewrites``),
    taken cheapest first, skipping one that would share a step with an edge
    already taken. Chain entries covering the shapes found are replaced;
    every tunable entry, and a chain entry covering none of them, is kept as
    ``profile`` has it.
    """
    found = chain_groups(calls, dev)
    out = Profile()
    for cls, dims, tunables in profile or ():
        out.add(cls, **dims, **tunables)

    priced = []
    for group in found:
        trial = time_chain_group(
            group,
            full_elf=full_elf,
            timing=timing,
            repeats=repeats,
            cache=cache,
            remeasure=remeasure,
            log=log,
        )
        if trial.refused is None and not (
            _nameable(group.producer_shape.named(()))
            and _nameable(group.consumer_shape.named(()))
        ):
            trial = dataclasses.replace(
                trial, refused="its dims are not representable in a profile"
            )
        noise = "?" if trial.noise_us is None else f"{trial.noise_us:.1f}"
        why = "" if trial.refused is None else f"  refused: {trial.refused}"
        log(f"{group}: {trial.delta_us:+.1f} ± {noise} us{why}")
        priced.append((group, trial))

    taken = select_rewrites(priced, log)

    existing = profile.chains() if profile is not None else []
    for producer_cls, p_dims, consumer_cls, c_dims, input in existing:
        probe = Profile()
        probe.add_chain(
            producer_cls,
            consumer_cls,
            input,
            producer_dims=p_dims,
            consumer_dims=c_dims,
        )
        if not any(probe.chained(g.producer, g.consumer, g.input) for g in found):
            out.add_chain(
                producer_cls,
                consumer_cls,
                input,
                producer_dims=p_dims,
                consumer_dims=c_dims,
            )
    for group in taken:
        out.add_chain(
            type(group.producer),
            type(group.consumer),
            group.input,
            producer_dims=group.producer_shape.named(()),
            consumer_dims=group.consumer_shape.named(()),
        )
    return out
