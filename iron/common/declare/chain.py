# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fold chains: the steps an operator's cores apply to a tile they hold."""

from __future__ import annotations

import dataclasses
import math
from enum import Enum
from typing import TYPE_CHECKING, Callable

from aie.dialects.aie import AIETileType

from .field import Unresolvable

if TYPE_CHECKING:
    from .operator import Operator


class Side(Enum):
    """Which tile ``Chain.at_tile`` rebuilds a chain at: a producer's
    finished output, or a consumer's prepared input.
    """

    FINISH = "finish"
    PREPARE = "prepare"


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

    @classmethod
    def of(cls, *ops: Operator, at: int | tuple[int, ...] = 0) -> Chain:
        """A chain of ``ops`` in order, the one way to build one from
        scratch: a fold's or a prologue's steps, or a test's.

        Args:
            ops: The steps' operators, in order.
            at: The input each step's tile enters, one for every step, or
                one per step.
        """
        ats = at if isinstance(at, tuple) else (at,) * len(ops)
        return cls(tuple(Link(op, a) for op, a in zip(ops, ats)))

    def then(self, op: Operator, at: int = 0) -> Chain:
        """This chain with ``op`` appended, a fold's body."""
        return self.extended((*self.steps, Link(op, at)))

    def after(self, op: Operator, at: int = 0) -> Chain:
        """This chain with ``op`` prepended, a prefold's body."""
        return self.extended((Link(op, at), *self.steps))

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

    def rebuilt(self, step: Callable[[Link], Link], *, owner: str, what: str) -> Chain:
        """Each chain with every step rebuilt by ``step`` (at the tile the
        cores hold), the array's unique and in a fixed order.

        Args:
            step: A step as the cores apply it.
            owner: The operator's name, in an error.
            what: The chain's name in an error, ``"finish"`` or ``"prologue"``.

        Raises:
            ValueError: ``step`` refuses a step, these steps are not among
                the array's chains, or a step with inputs of its own is in an
                array serving another chain.
        """
        own = tuple(step(link) for link in self.steps)
        chains: dict[tuple, tuple[Link, ...]] = {}
        for chain in self.chains:
            at = tuple(step(link) for link in chain)
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

    def at_tile(self, owner: Operator, side: Side, dev) -> Chain:
        """This chain rebuilt at the tile ``owner``'s cores hold it in,
        resolved for ``dev``: the steps of a finish at the output tile they
        release, or of a prologue at the input tile they acquire.

        Args:
            owner: The operator whose finish or prologue this is.
            side: Which of the two.
            dev: The device it resolves for.

        Raises:
            ValueError: The array applies no finish or no prologue, or the
                chain does not rebuild at the tile (``rebuilt``).
            Unresolvable: Each core reads more streams, its own and the
                chain's inputs, than a core tile has input channels, a
                finish input would stream into a block held out of order,
                a prologue's other inputs do not match the tile they stream
                in beside, or the chain's inputs do not fit the tiles or the
                descriptors of the input they ride (``feed=True``).
        """
        if side is Side.FINISH:
            return self._at_finish(owner, dev)
        return self._at_prepare(owner, dev)

    def _riding_fits(self, feed, riding: int, name: str, what: str) -> None:
        """Both sides: ``riding`` inputs of ``what`` fit the depth ``feed``'s
        cores hold of it.
        """
        if riding > feed.depth:
            raise Unresolvable(
                f"{name}: the {what}'s {riding} inputs ride {feed.name}, whose "
                f"cores hold {feed.depth} tiles of it at once"
            )

    def _at_finish(self, owner: Operator, dev) -> Chain:
        out = owner.outputs[0] if len(owner.outputs) == 1 else None
        # A subclass whose Array builds anew does not apply what its base's output declares.
        runs = next(
            k
            for k in type(owner).__mro__
            if "Array" in vars(k) and "build" in vars(vars(k)["Array"])
        )
        if out is None or not out.finish or runs not in out.owner.__mro__:
            raise ValueError(
                f"{type(owner).__name__}: its cores finish no output, so it "
                f"applies no finish"
            )
        name = type(owner).__name__
        ordered = out.finish_block is None
        finish = self.rebuilt(
            lambda link: owner.finish_step(
                link, out.finish_line, out.dtype, dev, ordered
            ),
            owner=name,
            what="finish",
        )
        if not ordered and any(len(link.op.inputs) > 1 for link in finish):
            raise Unresolvable(
                f"{name}: its cores hold each block of the output in an order "
                f"of their own, which a finish input does not stream in"
            )
        # owner's own declared members, not the stale finish/prepare extras a
        # previous bind (at construction) may have left on the instance.
        declared = owner._declared_io()
        fed = any(m.feed for m in declared)
        extra = [
            b
            for link in finish.steps
            for k, b in enumerate(link.op.inputs)
            if k != link.at
        ]
        reads = sum(m.fills and m.obj_dims is not None for m in declared) + (
            0 if fed else len(extra)
        )
        if reads > dev.core_dma_channels_in:
            raise Unresolvable(
                f"{name}: its cores read {reads} streams with the finish's "
                f"inputs, past a core tile's {dev.core_dma_channels_in} input "
                f"channels, and no input of its is declared feed=True for them "
                f"to ride"
            )
        if not fed or not extra:
            return finish
        feed = next(b for b in owner.inputs if b.feed)
        carried, line = math.prod(feed.obj_shape), math.prod(out.obj_shape)
        # The rest of the tile re-reads the input's: a shim descriptor's iterations.
        repeats = carried // line
        if feed.bounded is not None or out.bounded is not None:
            raise Unresolvable(
                f"{name}: the finish's inputs ride {feed.name} an output tile at "
                f"a time, which a per-call bound does not move by"
            )
        if feed.count != out.count:
            raise Unresolvable(
                f"{name}: the finish's inputs ride {feed.name}'s {feed.count} "
                f"lanes, which are not {out.name}'s {out.count}"
            )
        if feed.dtype != out.dtype:
            raise Unresolvable(
                f"{name}: the finish's inputs, of {out.name}'s dtype, ride "
                f"{feed.name}, whose tiles are of another"
            )
        if carried % line or repeats > 1 << dev.get_dma_bd_iter_bits(0, 0):
            raise Unresolvable(
                f"{name}: a {line}-element tile of the finish's inputs fills a "
                f"{carried}-element tile of {feed.name} in at most "
                f"{1 << dev.get_dma_bd_iter_bits(0, 0)} whole reads, and does not"
            )
        self._riding_fits(feed, len(extra), name, "finish")
        # Every one is live until the drains: a shim tile's descriptors serve
        # both directions of each of its channels, a lane its share of them.
        transfers = (1 + len(extra)) * out.elements // (out.count * line)
        shims = sum(
            dev.get_tile_type(col, 0) is AIETileType.ShimNOCTile
            for col in range(dev.cols)
        )
        held = (
            dev.get_num_bds(AIETileType.ShimNOCTile)
            * shims
            // (dev.shim_dma_channels_in + dev.shim_dma_channels_out)
        )
        if transfers > held:
            raise Unresolvable(
                f"{name}: a lane of {feed.name} carrying the finish's inputs is "
                f"{transfers} transfers, one per tile of each, past the {held} "
                f"descriptors a lane of a shim tile holds"
            )
        return finish

    def _at_prepare(self, owner: Operator, dev) -> Chain:
        into = next((b for b in owner.inputs if b.prepare), None)
        if into is None:
            raise ValueError(
                f"{type(owner).__name__}: its cores prepare no input, so it "
                f"applies no prologue"
            )
        name = type(owner).__name__
        line = math.prod(into.obj_shape) if into.streamed else into.shape[-1]
        for link in self.steps:
            for k, b in enumerate(link.op.inputs):
                if k != link.at and b.elements != line:
                    raise Unresolvable(
                        f"{name}: {type(link.op).__name__}.{b.name} "
                        f"is {b.elements} elements, not the {line}-element tile "
                        f"it streams in beside"
                    )
        riding = sum(len(link.op.inputs) - 1 for link in self.steps)
        tiles = into.elements // (
            1 if not into.streamed or into.replicate else into.count
        )
        if riding and tiles != line:
            raise Unresolvable(
                f"{name}: each core takes {tiles // line} tiles of "
                f"{into.name} a call, and a prologue's inputs stream in beside one"
            )
        if riding and not into.streamed:
            feed = next(b for b in owner.inputs if b.feed)
            if feed.dtype != into.dtype or math.prod(feed.obj_shape) < line:
                raise Unresolvable(
                    f"{name}: the prologue's inputs ride {feed.name}, whose "
                    f"tiles do not hold a {line}-element line of {into.name}'s type"
                )
            self._riding_fits(feed, riding, name, "prologue")
        return self.rebuilt(
            lambda link: link.at_line(line, into.dtype, dev),
            owner=name,
            what="prologue",
        )
