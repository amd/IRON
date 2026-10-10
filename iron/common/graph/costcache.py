# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the probe measured, kept per design across graphs and processes.

A cost table is one graph's working set; the cache is every design ever
measured on an NPU, one JSON file each under
``NPU_CACHE_HOME/iron/costs/<platform>/<power mode>/``, so a design two
graphs (or two versions of one) share is measured once. An entry is keyed
on what its time follows: the design's build (its recipe and the sources,
tools and device it is compiled with, as mlir-aie's compile cache keys it),
the per-call values it was run at, the contents of the inputs it was
given and, for an xclbin chain, the packaging it was run under. Editing how a design is generated therefore misses rather than
reusing a stale time. A configure calibration is kept the same way, keyed
on its pair's entries, and so are the twin a design was measured beside and
the verdict on a width judged against its default, the entries of a design
run alternating with its table's reference design, a full ELF's pack of
designs measured as one device, and a design's step at an operating point
against its step at its call's own values. A verdict's key names the
gates and the reference it was judged by, but no code is in a key: after
editing a reference or a tolerance, measure again with ``remeasure``.
"""

from __future__ import annotations

import dataclasses
import datetime
import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TypeVar

import numpy as np
from aie.utils.compile import NPU_CACHE_HOME

from ..declare import Operator
from ..design import OperatorDesign
from ..elementwise import Elementwise
from .narrowing import Calibration, Measured, PackCost, StepCost, _write


@dataclasses.dataclass(frozen=True)
class Measurement(Measured):
    """One design measured alone, as the cache holds it.

    Attributes:
        t_step_us: Its time per step while its device is configured.
        round_us: Its time per step as each round measured it, so two
            designs timed in one run pair round by round.
        alone_us: One run of one step, less `t_step_us`.
        output: The sha256 of what one run wrote, so any two widths
            measured on the same inputs compare without a rerun.
    """

    t_step_us: float
    round_us: list[float]
    alone_us: float
    output: str

    def cost(
        self, default: str, accurate: bool, t_step_us: float, noise_us: float | None
    ) -> StepCost:
        """The table's figure, exact if the output digest is `default`'s.

        Args:
            accurate: An inexact width was judged within its gates.
            t_step_us: Its step as priced, against the design it was run
                beside.
            noise_us: The standard error it is compared to its design's
                default by (``StepCost``).
        """
        exact = self.output == default
        return StepCost(
            t_step_us=t_step_us,
            noise_us=noise_us,
            alone_us=self.alone_us,
            exact=exact,
            accurate=exact or accurate,
            pmode=self.pmode,
            rounds=len(self.round_us),
            calls=self.calls,
            measured=self.measured,
        )


@dataclasses.dataclass(frozen=True)
class Pairing(Measured):
    """A reference design run alternating with another, as the cache holds it.

    Attributes:
        pair_us: The two designs' entries, the reference's and the other's.
    """

    pair_us: float
    rounds: int


@dataclasses.dataclass(frozen=True)
class Shift(Measured):
    """A design at one operating point, run interleaved with itself at its
    call's own values, as the cache holds it.

    Attributes:
        shift_us: How much longer a step there took.
        round_us: That shift as each round measured it, both runs timed
            in the round.
        output: The sha256 of what a run there wrote.
    """

    shift_us: float
    round_us: list[float]
    output: str


@dataclasses.dataclass(frozen=True)
class Accuracy:
    """A width whose output is not its default's, judged against its
    reference by the default's gate and its own.

    Attributes:
        within: Whether every output met both gates.
        detail: The first output a gate refused, and why; empty if within.
        measured: The day, as an ISO date; today unless read back.
    """

    within: bool
    detail: str
    measured: str = dataclasses.field(
        default_factory=lambda: datetime.date.today().isoformat()
    )


Record = TypeVar("Record", Measurement, Calibration, Accuracy, Pairing, PackCost, Shift)


class CostCache:
    """The measurements of one NPU platform at one power mode.

    Args:
        platform: The platform's name, as ``xrt-smi`` reports it.
        mode: Its power mode.
        root: Where every platform's cache is.
    """

    def __init__(
        self,
        platform: str,
        mode: str,
        root: Path = Path(NPU_CACHE_HOME) / "iron" / "costs",
    ):
        self.platform = platform
        self.mode = mode
        slug = re.sub(r"[^a-z0-9]+", "-", platform.lower()).strip("-")
        self.directory = Path(root) / slug / mode

    @staticmethod
    def key(
        op: Operator,
        values: Mapping[str, int] | None = None,
        inputs: Mapping[str, np.ndarray] | None = None,
        dispatch: str = "fused",
    ) -> str:
        """The entry ``op`` is measured into, resolved for the current
        device and run at ``values`` on ``inputs`` (random where not given),
        packaged as ``dispatch`` says (``narrowing.DISPATCHES``).
        """
        design = OperatorDesign(op.resolved()).compilable()
        given = sorted(
            (name, hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest())
            for name, a in (inputs or {}).items()
        )
        key = (
            design.recipe_hash,
            design.artifact_hash,
            sorted((values or {}).items()),
            given,
        )
        # A full ELF keeps the key its cached entries were measured under.
        if dispatch != "fused":
            key += (dispatch,)
        return hashlib.sha256(repr(key).encode()).hexdigest()[:32]

    @staticmethod
    def pair_key(a: str, b: str) -> str:
        """The entry the calibration between entries ``a`` and ``b`` is kept in."""
        return hashlib.sha256(repr(("calibration", a, b)).encode()).hexdigest()[:32]

    @staticmethod
    def beside_key(twin: str, entry: str) -> str:
        """The entry the design at ``twin`` is kept in as measured beside
        the one at ``entry``.
        """
        return hashlib.sha256(repr(("beside", twin, entry)).encode()).hexdigest()[:32]

    @staticmethod
    def paired_key(reference: str, entry: str) -> str:
        """The entry the design at ``entry`` is kept in as run alternating
        with the one at ``reference``.
        """
        return hashlib.sha256(
            repr(("alternated", reference, entry)).encode()
        ).hexdigest()[:32]

    @staticmethod
    def pack_key(reference: str, entries: Sequence[str]) -> str:
        """The entry the designs at ``entries``, packed on one device, are
        kept in as measured against the one at ``reference``.
        """
        return hashlib.sha256(
            repr(("pack", reference, sorted(entries))).encode()
        ).hexdigest()[:32]

    @staticmethod
    def point_key(reference: str, entry: str) -> str:
        """The entry the design at ``entry``, an operating point, is kept in
        as run interleaved with itself at ``reference``.
        """
        return hashlib.sha256(repr(("point", reference, entry)).encode()).hexdigest()[
            :32
        ]

    @staticmethod
    def judged_key(default: str, entry: str, default_op: Operator, op: Operator) -> str:
        """The entry the design at ``entry``, ``op``, is kept in as judged
        against its default's, ``default_op`` at ``default``: under both
        their gates, against ``op``'s reference (an elementwise one's kernel
        contract's).
        """
        gates = [
            (
                None
                if g is None
                else {
                    k: f"{v.__module__}.{v.__qualname__}" if callable(v) else v
                    for k, v in dataclasses.asdict(g).items()
                }
            )
            for g in (default_op.gate(), op.gate())
        ]
        references = [type(op).reference]
        if references[0] is Elementwise.reference:
            references.append(op.resolved().kernel().contract.reference)
        judgement = (gates, [f"{r.__module__}.{r.__qualname__}" for r in references])
        return hashlib.sha256(
            repr(("judged", default, entry, judgement)).encode()
        ).hexdigest()[:32]

    def get(self, key: str, kind: type[Record]) -> Record | None:
        """The record at ``key``; None if there is none, or it was written
        with other fields than ``kind`` has, so it is measured again.
        """
        path = self.directory / f"{key}.json"
        if not path.exists():
            return None
        fields = json.loads(path.read_text())
        if fields.keys() != {f.name for f in dataclasses.fields(kind)}:
            return None
        return kind(**fields)

    def put(
        self,
        key: str,
        record: Measurement | Calibration | Accuracy | Pairing | PackCost | Shift,
    ) -> None:
        _write(
            self.directory / f"{key}.json",
            json.dumps(dataclasses.asdict(record)) + "\n",
        )
