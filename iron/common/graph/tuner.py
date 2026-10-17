# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the graph core asks of a tuner, which lives outside it (``iron.tune``)."""

from __future__ import annotations

import abc
from typing import Any

from ..declare import Operator
from .trace import TracedGraph


class Tuning(abc.ABC):
    """What a tuner chose for one traced graph."""

    @abc.abstractmethod
    def apply(
        self, traced: TracedGraph, dev
    ) -> tuple[TracedGraph, list[list[Operator]]]:
        """``traced`` with the choice applied, and the operators that share
        a device, as ``Graph.compile``'s ``coresident=`` takes them.
        """

    @abc.abstractmethod
    def report(self) -> str:
        """What was chosen, a line each."""

    @abc.abstractmethod
    def summary(self) -> str:
        """One line on what the choice is predicted to gain."""

    @abc.abstractmethod
    def moved(self, traced: TracedGraph, dev) -> dict[int, dict[str, Any]]:
        """By step index of ``traced`` as applied, the tunables each step's
        design was moved to.
        """

    @abc.abstractmethod
    def packs(self, traced: TracedGraph, dev) -> dict[int, int]:
        """By step index of ``traced`` as applied, the device each step's
        design shares with others.
        """


class Tuner(abc.ABC):
    """Chooses a traced graph's tunables and packs: ``Graph.compile(tuner=)``."""

    @abc.abstractmethod
    def tune(self, traced: TracedGraph, dev, full_elf: bool) -> Tuning:
        """The choice for ``traced`` on ``dev``, packaged as one full ELF or not."""


class Prices(abc.ABC):
    """Each design's time, for a picture (``TracedGraph.picture(prices=)``)."""

    @abc.abstractmethod
    def step_us(self, traced: TracedGraph, dev) -> dict[int, float | None]:
        """By step index, each step's design's time in microseconds; None
        where it is not priced.
        """
