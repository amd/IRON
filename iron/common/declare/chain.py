# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fold chains: the steps an operator's cores apply to a tile they hold."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .operator import Operator


@dataclasses.dataclass(frozen=True)
class Link:
    """One step of a finish or a prologue: ``op`` applied to a tile of the
    producer's output, which enters as its input ``at``, or to a tile of the
    consumer's prepared input, which ``op`` produced from its input ``at``.
    Its other inputs stream into the cores beside it, their
    ``finish_inputs`` or ``prepare_inputs``.
    """

    op: Operator
    at: int = 0

    def array_key(self):
        return (self.op.array_key(), self.at)

    def at_line(self, line: int, dtype, dev, ordered: bool = True) -> Link:
        """This step resolved at one tile (``Operator.at_line``)."""
        return Link(self.op.at_line(line, dtype, dev, ordered, self.at), self.at)

    def operands(self, tile, extras) -> list:
        """``tile`` at input ``at`` among this step's ``extras``."""
        operands = list(extras)
        operands.insert(self.at, tile)
        return operands


@dataclasses.dataclass(frozen=True)
class Chain:
    """The steps an operator's cores apply, in order, to each tile of its
    finished output or prepared input, and the chains its array applies,
    each design selecting its own. Iterating it gives its steps.

    Attributes:
        steps: This operator's steps.
        shared: Every chain the array applies, these steps' among them;
            empty for the array of these steps alone.
    """

    steps: tuple[Link, ...] = ()
    shared: tuple[tuple[Link, ...], ...] = ()

    def __iter__(self):
        return iter(self.steps)

    def __len__(self) -> int:
        return len(self.steps)

    @property
    def chains(self) -> tuple[tuple[Link, ...], ...]:
        """Every chain the array applies: ``shared``, or these steps alone."""
        return self.shared or (self.steps,)

    def array_key(self) -> tuple:
        return tuple(link.array_key() for link in self.steps)

    def keys(self) -> tuple:
        """Each chain the array applies, by its steps' array keys."""
        return tuple(tuple(link.array_key() for link in c) for c in self.chains)

    def extended(self, steps: tuple[Link, ...]) -> Chain:
        """``steps``, these with one added, on this chain's array: it keeps
        the chains it applies, unless a step takes inputs of its own, which
        stream into an array of this chain alone.
        """
        if any(len(link.op.inputs) > 1 for link in steps):
            return Chain(steps)
        return Chain(steps, (*self.chains, steps))

    def at_line(
        self, line: int, dtype, dev, *, ordered: bool = True, owner: str, what: str
    ) -> Chain:
        """Each chain rebuilt at a ``line``-element tile, the array's unique
        and in a fixed order (``Link.at_line``).

        Args:
            owner: The operator's name, in an error.
            what: The chain's name in an error, ``"finish"`` or ``"prologue"``.

        Raises:
            ValueError: A step does not run at the tile, these steps are not
                among the array's chains, or a step with inputs of its own
                is in an array serving another chain.
        """
        own = tuple(link.at_line(line, dtype, dev, ordered) for link in self.steps)
        chains: dict[tuple, tuple[Link, ...]] = {}
        for chain in self.chains:
            at = tuple(link.at_line(line, dtype, dev, ordered) for link in chain)
            chains.setdefault(tuple(link.array_key() for link in at), at)
        if tuple(link.array_key() for link in own) not in chains:
            raise ValueError(f"{owner}: its {what} is not one its array applies")
        if len(chains) > 1 and any(
            len(link.op.inputs) > 1 for c in chains.values() for link in c
        ):
            raise ValueError(
                f"{owner}: a {what} step with inputs of its own streams them "
                f"into an array serving no other {what}"
            )
        if len(chains) == 1:
            return Chain(own)
        return Chain(own, tuple(chains[k] for k in sorted(chains, key=repr)))
