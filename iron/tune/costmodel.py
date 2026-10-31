# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a version pays beyond its steps' own standalone times, per device.

A configuration switch's fixed cost, its cost per core of the group switched into, and
what a step pays running inside a packed configuration rather than alone.

Every end-to-end check of a packing adds a sample (how its features and its
time beyond its steps moved), and the terms are refitted, pulled toward
their prior by ``PRIOR_WEIGHT`` samples' worth so a few samples cannot throw
them far. ``costs/<device>.json`` beside this module is the model a tune
starts from and writes back, so one device's tunes bootstrap the next.
"""

from __future__ import annotations

import dataclasses
import json
from collections.abc import Mapping
from pathlib import Path

import numpy as np

FEATURES = ("switches", "switch_cores", "packed_steps")
# npu2 (Strix Halo, turbo): a 1-core design alternated with designs of 1 to
# 8 cores cost 40 to 68 us a switch more than each run alone.
PRIOR = {"switches": 37.0, "switch_cores": 7.0, "packed_steps": 0.0}
PRIOR_WEIGHT = 3.0
COSTS = Path(__file__).with_name("costs")


@dataclasses.dataclass
class CostModel:
    """The terms, in us per unit of each feature, and the samples they were fitted to.

    Each a change in features and the change in time it came with.
    """

    terms: dict[str, float] = dataclasses.field(default_factory=lambda: dict(PRIOR))
    samples: list[tuple[dict[str, float], float]] = dataclasses.field(
        default_factory=list
    )
    # What the terms are pulled toward: PRIOR, or a device's measured switch.
    prior: dict[str, float] = dataclasses.field(default_factory=lambda: dict(PRIOR))

    @classmethod
    def calibrated(cls, fixed_us: float, per_core_us: float) -> CostModel:
        """Return a model without samples whose prior is a measured switch's cost (``measure.switch_cost``)."""
        prior = {**PRIOR, "switches": fixed_us, "switch_cores": per_core_us}
        return cls(terms=dict(prior), prior=prior)

    def predict(self, features: Mapping[str, float]) -> float:
        """Return the time, in us, ``features`` add beyond the steps' own."""
        return sum(self.terms[f] * features.get(f, 0.0) for f in FEATURES)

    def add(self, change: Mapping[str, float], extra_us: float) -> None:
        """Add a sample, ``change`` in features coming with ``extra_us`` of time beyond the steps' own, and refit."""
        self.samples.append(
            ({f: float(change.get(f, 0.0)) for f in FEATURES}, extra_us)
        )
        x = np.array([[s[f] for f in FEATURES] for s, _ in self.samples])
        y = np.array([t for _, t in self.samples])
        prior = np.array([self.prior[f] for f in FEATURES])
        # The prior weighs as PRIOR_WEIGHT samples of each feature's mean size.
        ridge = PRIOR_WEIGHT * np.diag(np.maximum((x**2).mean(axis=0), 1.0))
        fitted = np.linalg.solve(x.T @ x + ridge, x.T @ y + ridge @ prior)
        self.terms = {f: float(v) for f, v in zip(FEATURES, fitted)}

    @classmethod
    def load(cls, device: str, directory: Path = COSTS) -> CostModel | None:
        """``device``'s model, or None where none is kept."""
        path = Path(directory) / f"{device}.json"
        if not path.exists():
            return None
        data = json.loads(path.read_text())
        return cls(
            terms=data["terms"],
            samples=[(dict(s["change"]), s["extra_us"]) for s in data["samples"]],
            prior=data["prior"],
        )

    def save(self, device: str, directory: Path = COSTS) -> Path:
        """Write ``device``'s model; return its path."""
        path = Path(directory) / f"{device}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        samples = [{"change": c, "extra_us": t} for c, t in self.samples]
        data = {"terms": self.terms, "prior": self.prior, "samples": samples}
        path.write_text(json.dumps(data, indent=1) + "\n")
        return path
