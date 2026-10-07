# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the probe measured, kept per design across graphs and processes.

A cost table is one graph's working set; the cache is every design ever
measured on an NPU, one JSON file each under
``NPU_CACHE_HOME/iron/costs/<platform>/<power mode>/``, so a design two
graphs (or two versions of one) share is measured once. An entry is keyed
on what its time follows: the design's build (its recipe and the sources,
tools and device it is compiled with, as mlir-aie's compile cache keys it),
the per-call values it was run at and the contents of the inputs it was
given. Editing how a design is generated therefore misses rather than
reusing a stale time. A configure calibration is kept the same way, keyed
on its pair's entries, and so are the twin a design was measured beside and
the verdict on a width judged against its default. Reference and tolerance
code is in no key: after editing one, measure again with ``remeasure``.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import os
import re
from collections.abc import Mapping
from pathlib import Path
from typing import TypeVar

import numpy as np
from aie.utils.compile import NPU_CACHE_HOME

from ..declare import Operator
from ..design import OperatorDesign
from .narrowing import Calibration, StepCost


@dataclasses.dataclass(frozen=True)
class Measurement:
    """One design measured alone, as the cache holds it.

    Attributes:
        t_step_us: Its time per step while its device is configured.
        alone_us: One run of one step, less `t_step_us`.
        output: The sha256 of what one run wrote, so any two widths
            measured on the same inputs compare without a rerun.
    """

    t_step_us: float
    alone_us: float
    output: str
    pmode: str
    rounds: int
    calls: int
    measured: str  # ISO date

    def cost(self, reference: str) -> StepCost:
        """The table's figure, exact if the output digest is `reference`."""
        return StepCost(
            t_step_us=self.t_step_us,
            alone_us=self.alone_us,
            exact=self.output == reference,
            pmode=self.pmode,
            rounds=self.rounds,
            calls=self.calls,
            measured=self.measured,
        )


@dataclasses.dataclass(frozen=True)
class Accuracy:
    """A width whose output is not its default's, judged against its
    reference by the default's gate and its own.

    Attributes:
        detail: The first output a gate refused, and why; empty if within.
    """

    within: bool
    detail: str
    measured: str  # ISO date


Record = TypeVar("Record", Measurement, Calibration, Accuracy)


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
    ) -> str:
        """The entry ``op`` is measured into, resolved for the current
        device and run at ``values`` on ``inputs`` (random where not given).
        """
        design = OperatorDesign(op.resolved()).compilable()
        given = sorted(
            (name, hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest())
            for name, a in (inputs or {}).items()
        )
        h = hashlib.sha256(
            repr(
                (
                    design.recipe_hash,
                    design.artifact_hash,
                    sorted((values or {}).items()),
                    given,
                )
            ).encode()
        )
        return h.hexdigest()[:32]

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
    def judged_key(default: str, entry: str) -> str:
        """The entry the design at ``entry`` is kept in as judged against
        its default's, at ``default``.
        """
        return hashlib.sha256(repr(("judged", default, entry)).encode()).hexdigest()[
            :32
        ]

    def get(self, key: str, kind: type[Record]) -> Record | None:
        path = self.directory / f"{key}.json"
        if not path.exists():
            return None
        return kind(**json.loads(path.read_text()))

    def put(self, key: str, record: Measurement | Calibration | Accuracy) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.directory / f"{key}.json"
        partial = path.with_suffix(f".{os.getpid()}")
        partial.write_text(json.dumps(dataclasses.asdict(record)) + "\n")
        partial.replace(path)
