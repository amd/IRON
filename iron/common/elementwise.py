# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The shared elementwise array.

One core per (column, channel), each streaming fixed-size lines of
every operand through the kernel a subclass's ``kernel()`` names, with
the scalars ``scalars()`` supplies; a parameter either reads is
declared ``array=True`` unless a stream names it. A ``replicate=True``
input is one line each core holds for the whole call and every line
meets (``RowwiseMul``'s row).
"""

from __future__ import annotations

import dataclasses
from collections.abc import Iterable, Mapping
from typing import Any, ClassVar, Self

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, ObjectFifo, Out, Worker, ceildiv, kernels
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernel import ExternalFunction
from aie.iron.kernels import eltwise
from aie.utils.compile.jit.params import (
    Select,
    divisors,
    param,
    per_call,
    tunable,
    widths,
)
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance, Verdict
from ml_dtypes import bfloat16

from .declare import Built, Operand, Operator, Rtp, Unresolvable
from .testing import Case, Testing

# Small enough to divide any extent a model has, at some DMA efficiency.
DEFAULT_TILE = 256

LENGTHS = (1024, 2048, 4096, 8192)

# Takes the widest grid most of a millisecond, several times the dispatch cost.
BENCH_ELEMENTS = 1 << 23
BENCH_TILE = 4096


class Sweep:
    """The cases of an elementwise operator.

    At the regular length, one core and the most its shim budget allows
    (the grids between run the same loop); at the other lengths, in the
    extensive suite, the smallest and the largest tile.

    Args:
        channels: None leaves the count to the operator (a binary one).
        tile_cap: Else the class's ``tile_cap``.
        regular: The one length in the default suite; None for all.
        rows: A length is that many elements in rows of ``tile_size`` (``Rowwise``).
        bench: The length of one CI-tracked case at the widest grid; None adds none.
        lower: Flags its first default case ``Case.lower``.
        **extra: Given to every case.
    """

    def __init__(
        self,
        lengths: Iterable[int] = LENGTHS,
        *,
        channels: Iterable[int] | None = (1, 2),
        tile_cap: int | None = None,
        regular: int | None = 2048,
        rows: bool = False,
        bench: int | None = BENCH_ELEMENTS,
        lower: bool = False,
        **extra: Any,
    ):
        self.lengths = tuple(lengths)
        self.bench = bench
        self.lower = lower
        self.channels = None if channels is None else tuple(channels)
        self.tile_cap = tile_cap
        self.regular = regular
        self.rows = rows
        self.extra = extra

    def _kwargs(self, length: int, cols: int, chans: int, tile: int) -> dict:
        kwargs = dict(rows=length // tile) if self.rows else dict(size=length)
        kwargs["num_aie_columns"] = cols
        if self.channels is not None:
            kwargs["num_channels"] = chans
        kwargs.update(tile_size=tile, **self.extra)
        return kwargs

    def __call__(self, cls, dev: Device) -> list[Case]:
        cap = cls.tile_cap if self.tile_cap is None else self.tile_cap
        most = {}
        for chans in self.channels or (1,):
            try:
                most[chans] = cls.shim_columns(dev, chans, self.extra)
            except Unresolvable:  # no column fits: no grid at this count
                most[chans] = 0
        grids = [
            (length, cols, chans, min(length // (cols * chans), cap))
            for length in self.lengths
            for chans in most
            for cols in range(1, most[chans] + 1)
        ]
        grids = [g for g in grids if g[1] * g[2] * g[3] == g[0]]
        regular = [g for g in grids if g[0] == self.regular]
        others = [g for g in grids if g[0] != self.regular]
        picked = [g for g in regular if g[1:3] == (1, 1)]
        if regular:
            picked.append(max(regular, key=lambda g: (g[1] * g[2], g[2])))
        if others:
            picked += [min(others, key=lambda g: g[3]), max(others, key=lambda g: g[3])]
        out = [
            Case(self._kwargs(*g), extensive=g[0] != self.regular)
            for g in dict.fromkeys(picked)
        ]
        if self.lower:
            i = next(i for i, c in enumerate(out) if not c.extensive)
            out[i] = dataclasses.replace(out[i], lower=True)
        if self.bench is not None:
            chans = max(self.channels or (1,))
            tile = min(BENCH_TILE, cap)
            cols = next(
                c
                for c in range(cls.shim_columns(dev, chans, self.extra), 0, -1)
                if self.bench % (c * chans * tile) == 0
            )
            out.append(
                Case(
                    self._kwargs(self.bench, cols, chans, tile),
                    bench=True,
                )
            )
        return out


@dataclasses.dataclass(frozen=True)
class KernelCall:
    """One kernel call an elementwise operator's core makes over a line.

    Args:
        scalars: The scalar arguments its contract leaves unbound, in order.
        operands: Each input tile, in the kernel's order: an input of the
            operator (``self.x``), or None, the line the call before it wrote.
    """

    kernel: ExternalFunction
    scalars: tuple = ()
    operands: tuple[Operand | None, ...] = ()


@dataclasses.dataclass(frozen=True)
class FinishStep:
    """A step folded into its producer's cores.

    ``consumer`` runs on the producer's output tile, held at its input ``at``; ``dims``
    are its other constructor keywords (its shape and grid always match the tile).
    ``binary`` is whether an input besides the tile streams in beside it, the one a
    producer's free input channel may carry.
    """

    consumer: type[Elementwise]
    dims: tuple[tuple[str, Any], ...]
    at: int
    binary: bool

    def consumer_at(self, line: int, dev, elements: int | None = None) -> Elementwise:
        """``consumer`` whose cores run a ``line``-element tile, the producer's own (so its kernel matches), resolved for ``dev``.

        Sized to run on ``elements`` total, or one tile alone where None (a build's own
        kernel, which never reads more than one). A one-core grid, where ``consumer``
        takes it as a constructor argument; some (``SiLU``'s ``num_channels``) fix it
        instead.
        """
        params = self.consumer.declaration.params
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in params and params[n].init
        }
        fields: dict[str, Any] = {
            "size": line if elements is None else elements,
            "tile_size": line,
            **one,
            **dict(self.dims),
        }
        return self.consumer(**fields).resolved(dev)


def finish_reference(
    finish: tuple[FinishStep, ...], y: np.ndarray, extra: tuple, dev, line: int
) -> np.ndarray:
    """``y``, a producer's own output, through its finish chain on the host.

    Each step's reference over the tile, taking the next of ``extra`` where it reads
    another input, as ``Finish.apply`` runs on the device. ``line`` is the producer's
    own tile, which its finish's kernel matches.
    """
    given = iter(extra)
    tile = np.ravel(y)
    for step in finish:
        consumer = step.consumer_at(line, dev, elements=tile.size)
        args = [
            tile if i == step.at else next(given) for i in range(len(consumer.inputs))
        ]
        tile = np.ravel(np.asarray(consumer.reference(*args)))
    return tile.reshape(y.shape).astype(y.dtype, copy=False)


class Elementwise(Operator):
    """The array for an elementwise kernel over lines of ``tile_size`` elements.

    Subclasses declare operands with the line as their tile, most split
    over every core (``per=CORES``), and implement ``kernel``;
    ``tile_cap`` is the longest line.
    """

    num_aie_columns: int = tunable(domain=widths)
    num_channels: int = tunable(default=1, domain=widths)
    tile_size: int = tunable(
        domain=lambda op, dev, t: divisors(
            t, of=op.outputs[0].elements, step=64, cap=op.tile_cap, span=3
        ),
    )

    count = per_call(
        derive=lambda op: ceildiv(op.valid_elements, op.cores * op.tile_size),
    )

    # A chain of steps folded into this one's cores, its output their tile,
    # each but at most one unary: its one free input channel is the one
    # binary step's, or, a channel-full producer, its first input's own.
    finish: tuple[FinishStep, ...] = param(default=(), array=True)
    # A plain default, not derived: shim_columns() reads it from the class
    # alone (a Sweep's cases), before any instance exists to derive it from.
    uses_extra: bool = param(default=False)
    rides: bool = param(default=False, array=True)

    default_tile: ClassVar[int] = DEFAULT_TILE
    tile_cap: ClassVar[int] = 4096

    def validate(self) -> None:
        if sum(f.binary for f in self.finish) > 1:
            raise ValueError(
                f"{type(self).__name__}: only one of its finish steps takes "
                f"another input; its one free input channel is already another's"
            )

    def _can_ride(self) -> bool:
        """Whether this producer's first input could carry a finish's other input beside its own.

        No per-call bound to chunk around, and exactly one tile a lane, so a single
        extra transfer a lane suffices (the general multi-tile case needs its own
        re-read chunking, not this).
        """
        if self.bound_extents or not self.inputs:
            return False
        try:
            return self.lines == self.cores
        except (TypeError, ZeroDivisionError):
            return False

    def fold(self, consumer: Operator, at: int) -> Self | None:
        if not isinstance(consumer, Elementwise):
            return None
        others = [i for i in range(len(consumer.inputs)) if i != at]
        if len(others) > 1:
            return None
        binary = bool(others)
        # One finish step may take another input (``validate``).
        if binary and any(f.binary for f in self.finish):
            return None
        used = sum(b.streamed for b in self.inputs)
        rides = False
        dev = self.dev
        if dev is None:
            return None
        if binary and used + 1 > dev.core_dma_channels_in:
            if self.rides or not self._can_ride():
                return None
            rides = True
        dims = tuple(
            sorted(
                (n, vars(consumer)[n])
                for n, p in type(consumer).declaration.params.items()
                if p.init
                and n
                not in (
                    "size",
                    "tile_size",
                    "num_aie_columns",
                    "num_channels",
                    "finish",
                    "uses_extra",
                    "rides",
                )
                and vars(consumer)[n] is not None
            )
        )
        step = FinishStep(type(consumer), dims, at, binary)
        return self.replace(
            rides=self.rides or rides,
            finish=self.finish + (step,),
            uses_extra=self.uses_extra or binary,
        )

    def resolve(self, dev) -> Self:
        (out,) = self.outputs
        tile_size = self.default_tile if self.tile_size is None else self.tile_size
        if self.tile_size is None and out.elements % tile_size:
            # The widest line, in 64-element steps, that splits it whole.
            tile_size = next(
                (
                    t
                    for t in range(tile_size, 0, -64)
                    if t % 64 == 0 and out.elements % t == 0
                ),
                tile_size,
            )
        if tile_size > self.tile_cap:
            raise Unresolvable(
                f"tile_size={tile_size} exceeds the {self.tile_cap}-element line "
                f"one core holds ({type(self).__name__}.tile_cap)"
            )
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: out.elements % (c * self.num_channels * tile_size) == 0,
        )
        return self.replace(num_aie_columns=cols, tile_size=tile_size)

    def compatible(self) -> None:
        (out,) = self.outputs
        share = self.cores * self.tile_size
        if out.elements % share:
            raise ValueError(
                f"{type(self).__name__}: {out.elements} elements do not divide "
                f"into whole {self.tile_size}-element lines over "
                f"{self.num_aie_columns} columns x {self.num_channels} channels "
                f"({share} per pass); give a tile_size= or num_aie_columns= "
                f"that divides it"
            )

    @property
    def cores(self) -> int:
        return self.num_aie_columns * self.num_channels

    @property
    def lines(self) -> int:
        (out,) = self.outputs
        return out.elements // self.tile_size

    @property
    def valid_elements(self) -> int:
        """The elements a call processes, the bounded extent's worth if bound."""
        (out,) = self.outputs
        return out.elements

    def chain(self) -> tuple[KernelCall, ...]:
        """Return the kernel calls a core makes over one line, in order.

        Which ``reference`` and ``judge`` follow; more than ``kernel()`` with an array
        of its own, or a step folded into this one's cores.
        """
        config = self.layout()
        own = tuple(b for b in self.inputs if b.name != "finish0")
        calls = [KernelCall(config.kernel(), config.scalars(), own)]
        finish0 = next((b for b in self.inputs if b.name == "finish0"), None)
        for step in self.finish:
            consumer = step.consumer_at(self.tile_size, self.dev)
            operands = tuple(
                None if i == step.at else finish0 for i in range(len(consumer.inputs))
            )
            calls.append(
                KernelCall(
                    consumer.layout().kernel(), consumer.layout().scalars(), operands
                )
            )
        return tuple(calls)

    def over(self, elements: int, line: int) -> Self:
        """Return this operator over ``elements`` elements in lines of ``line``, on one core.

        Raises:
            ValueError: Its shape is not a run of lines.
        """
        raise ValueError(f"{type(self).__name__} is not a run of lines")

    def tolerance(self) -> Tolerance | None:
        kernel = self.layout().kernel()
        own = (
            None
            if kernel.contract is None
            else kernel.contract_for(resolve_target_arch(self.dev)).tolerance
        )
        if not self.finish:
            return own
        n_own = len(self.inputs) - (1 if self.uses_extra else 0)
        (out,) = self.outputs
        return Tolerance.bounded(
            finish_bound(
                self.finish,
                own,
                lambda *a: self._own_reference(a),
                n_own,
                out.host_dtype,
                self.dev,
                self.tile_size,
            ),
            note="its own kernel's contract, then each finish step's, in turn",
        )

    def ops(self) -> int:
        contract = self.layout().kernel().contract
        per_call = None if contract is None else contract.ops_per_call
        total = super().ops() if per_call is None else per_call * self.lines
        for step in self.finish:
            total += step.consumer_at(self.tile_size, self.dev).ops() * self.lines
        return total

    def reference(self, *inputs: Any, **kwargs: Any):
        """Run the kernel contract's reference, line by line, what the cores compute.

        A bounded call's elements short of a whole line are zero-padded
        to whole lines, as the device runs whole tiles.
        """
        (out,) = self.outputs
        line = self.default_tile if self.tile_size is None else self.tile_size
        if out.elements % line:
            whole = -(-out.elements // line) * line
            padded = [
                (
                    x
                    if b.replicate
                    else np.concatenate(
                        [np.ravel(x), np.zeros(whole - np.size(x), np.asarray(x).dtype)]
                    )
                )
                for b, x in zip(self.inputs, inputs)
            ]
            y = np.asarray(self.over(whole, line).reference(*padded))
            return y.reshape(-1)[: out.elements].reshape(out.host_shape)
        n_own = len(self.inputs) - (1 if self.uses_extra else 0)
        own, extra = inputs[:n_own], inputs[n_own:]
        y = self._own_reference(own)
        return (
            finish_reference(self.finish, y, extra, self.dev, line)
            if self.finish
            else y
        )

    def _own_reference(self, own: tuple) -> np.ndarray:
        """Return this operator's own kernel's reference, line by line, its finish chain left out."""
        op, lines, scalars = self._kernel_arguments(own)
        (out,) = op.outputs
        y = (
            op.layout()
            .kernel()
            .expected(lines, scalars=scalars, arch=resolve_target_arch(op.dev))
        )
        y = np.asarray(y).astype(out.host_dtype, copy=False)
        return y.reshape(out.host_shape, copy=False)

    def judge(
        self,
        inputs: Mapping[str, np.ndarray],
        written: Mapping[str, np.ndarray],
        tolerance: Tolerance,
        expected: Mapping[str, np.ndarray] | None = None,
    ) -> dict[str, Verdict]:
        """Its output held to its reference by its kernel's ``judge``, line by line.

        Where a core makes one kernel call; as any operator's where it
        makes more.
        """
        op = self.resolved()
        if len(op.chain()) > 1:
            return super().judge(inputs, written, tolerance, expected)
        if expected is None:
            expected = self._call_reference(inputs)
        _, lines, scalars = self._kernel_arguments([inputs[b.name] for b in op.inputs])
        (out,) = op.outputs
        verdict = (
            op.layout()
            .kernel()
            .judge(
                written[out.name],
                expected[out.name],
                calls=op.lines,
                tolerance=tolerance,
                inputs=lines,
                scalars=scalars,
                arch=resolve_target_arch(op.dev),
            )
        )
        return {out.name: verdict}

    def _kernel_arguments(self, inputs) -> tuple[Self, list[np.ndarray], tuple]:
        """Return the resolved operator, ``inputs`` as its cores' lines, and the scalars.

        Raises:
            NotImplementedError: The kernel declares no reference.
        """
        op = self.resolved()
        config = op.layout()
        kernel = config.kernel()
        arch = resolve_target_arch(op.dev)
        contract = None if kernel.contract is None else kernel.contract_for(arch)
        if contract is None or contract.reference is None:
            raise NotImplementedError(
                f"{type(self).__name__}: its kernel declares no reference; "
                f"define reference()"
            )
        _, scalars = config.arguments(kernel, op.chain()[0].scalars, len(inputs), 1)
        # A held line is one row every call broadcasts against; cut into
        # segments, each line meets its own.
        segments = config.held_segments()
        lines = [
            (
                np.tile(np.reshape(x, (segments, -1)), (op.lines // segments, 1))
                if b.replicate and segments > 1
                else x.reshape(1 if b.replicate else op.lines, -1, copy=False)
            )
            for b, x in zip(op.inputs, inputs)
        ]
        return (
            op,
            lines,
            tuple(scalars[i] for i in contract.reference_indices() if i in scalars),
        )

    def kernel(self) -> ExternalFunction:
        """Return the ``ExternalFunction`` each core calls over one line."""
        raise NotImplementedError(f"{type(self).__qualname__} declares no kernel()")

    def scalars(self) -> tuple:
        """Return the kernel's scalar arguments its contract leaves unbound, in order."""
        return ()

    def held_segments(self) -> int:
        """Return the lines each held input is cut into.

        A core holds all of them and meets, in turn, with that many
        lines of every other input.
        """
        return 1

    def arguments(
        self, kernel: ExternalFunction, given: tuple, n_in: int, n_out: int
    ) -> tuple[list[int], dict]:
        """Return where each tile goes in a call of ``kernel``, and its scalar arguments.

        ``n_in`` inputs and ``n_out`` outputs; ``given`` fills the
        scalars the contract leaves unbound.

        Returns:
            The argument positions of the inputs then the outputs, in the
            order a core acquires them, and the scalar values by position.
        """
        contract = kernel.contract
        if contract is None:
            return list(range(n_in + n_out)), {}
        if contract.accumulates:
            raise ValueError(
                f"{type(self).__qualname__}: an elementwise kernel writes its output; "
                f"{kernel.name} accumulates into one"
            )
        roles = contract.roles
        scalars = dict(contract.parameter_bindings)
        free = [
            i for i, r in enumerate(roles) if r is kernels.Param and i not in scalars
        ]
        if len(free) != len(given):
            raise ValueError(
                f"{type(self).__qualname__}: {kernel.name} leaves {len(free)} scalar(s) "
                f"unbound; {len(given)} given"
            )
        scalars.update(zip(free, given))
        outs = list(contract.out_indices)
        ins = [i for i in range(len(roles)) if i not in scalars and i not in outs]
        if (len(ins), len(outs)) != (n_in, n_out):
            raise ValueError(
                f"{type(self).__qualname__}: {kernel.name} takes {len(ins)} input and "
                f"{len(outs)} output tile(s); it is given {n_in} and {n_out}"
            )
        return ins + outs, scalars

    def build(self) -> Built:
        streams = [b for b in self.buffers if b.streamed]
        finish_in = next((b for b in streams if b.name == "finish0"), None)
        ins = [b for b in streams if b.role is In and b is not finish_in]
        outs = [b for b in streams if b.drains]
        n_in = len(ins)
        cores = self.cores
        kernel = self.kernel()
        positions, scalars = self.arguments(kernel, self.scalars(), n_in, len(outs))
        order = {i: k for k, i in enumerate(positions)}
        n_args = len(positions) + len(scalars)

        def slot(k: int) -> str:
            col, chan = divmod(k, self.num_channels)
            return f"{col}" if self.num_channels == 1 else f"{col}_{chan}"

        segments = self.held_segments()

        # A held line, acquired once per call, is one fifo per lane, every
        # core of the lane taking its own cons() (fifos()'s readers=); feed()
        # refuses a held input, so a fed one is never replicate.
        of_ins = [
            s.fifos(segments, readers=cores // s.lanes) if s.replicate else s.fifos()
            for s in ins
        ]
        of_outs = [s.fifos() for s in outs]
        rtps = [Rtp([self.count]) for _ in range(cores)]
        n_fifos = n_in + len(outs)
        held = [s.replicate for s in ins] + [False] * len(outs)

        def core_fn(*args):
            fifos = args[:n_fifos]
            kernel_fn, rtp = args[n_fifos:]
            n = rtp.read()[self.count]
            kept = {j: f.acquire(segments) for j, f in enumerate(fifos) if held[j]}
            for _ in range_(n):
                for s in range(segments):
                    elements = [
                        (
                            (kept[j] if segments == 1 else kept[j][s])
                            if held[j]
                            else f.acquire(1)
                        )
                        for j, f in enumerate(fifos)
                    ]
                    kernel_fn(
                        *(
                            elements[order[i]] if i in order else scalars[i]
                            for i in range(n_args)
                        )
                    )
                    for j, f in enumerate(fifos):
                        if not held[j]:
                            f.release(1)
            for j in kept:
                fifos[j].release(segments)

        if not self.finish:
            workers = [
                Worker(
                    core_fn,
                    [
                        (
                            of[k % len(of)][k // len(of)]
                            if s.replicate
                            else of[k % len(of)]
                        )
                        for s, of in zip(ins, of_ins)
                    ]
                    + [of[k] for of in of_outs]
                    + [kernel, rtps[k]],
                )
                for k in range(cores)
            ]
            return Built(workers, rtps)

        # The chain of steps folded into these cores: each kernel runs after
        # the one before it, over the tile the previous call wrote; it
        # ping-pongs between two scratch buffers until the last call writes
        # the real output. At most one step's other input, if any, streams
        # in on finish_in, or, this producer's cores already full, rides
        # its first input's own stream, one more acquire of the same fifo.
        of_finish = finish_in.fifos() if finish_in is not None else None
        ride_index = (
            next(i for i, b in enumerate(ins) if b is self.inputs[0])
            if self.rides
            else None
        )
        chain_meta = []
        chain_kernels = []
        for step in self.finish:
            consumer = step.consumer_at(self.tile_size, self.dev)
            c_kernel = consumer.layout().kernel()
            c_positions, c_scalars = consumer.arguments(
                c_kernel, consumer.scalars(), len(consumer.inputs), 1
            )
            c_order = {i: j for j, i in enumerate(c_positions)}
            n_c_args = len(c_positions) + len(c_scalars)
            chain_kernels.append(c_kernel)
            chain_meta.append(
                (c_positions, c_scalars, c_order, n_c_args, step.at, step.binary)
            )
        # A second scratch buffer, to ping-pong, only past one finish step:
        # an L1 line this core otherwise never holds at once.
        scratch_as = [Buffer(self.outputs[0].obj_type) for _ in range(cores)]
        scratch_bs = (
            [Buffer(self.outputs[0].obj_type) for _ in range(cores)]
            if len(chain_meta) > 1
            else None
        )

        def core_fn_chain(*args):
            fifos = args[:n_fifos]
            tail = args[n_fifos:]
            finish_fifo = tail[0] if of_finish is not None else None
            tail = tail[1:] if of_finish is not None else tail
            kernel_fn = tail[0]
            chain_fns = tail[1 : 1 + len(chain_meta)]
            tail = tail[1 + len(chain_meta) :]
            if scratch_bs is not None:
                scratch_a, scratch_b, rtp = tail
            else:
                scratch_a, rtp = tail
                scratch_b = None
            n = rtp.read()[self.count]
            kept = {j: f.acquire(segments) for j, f in enumerate(fifos) if held[j]}
            for _ in range_(n):
                for s in range(segments):
                    elements = [
                        (
                            (kept[j] if segments == 1 else kept[j][s])
                            if held[j]
                            else f.acquire(1)
                        )
                        for j, f in enumerate(fifos)
                    ]
                    targets = list(elements)
                    targets[n_in] = scratch_a
                    kernel_fn(
                        *(
                            targets[order[i]] if i in order else scalars[i]
                            for i in range(n_args)
                        )
                    )
                    # Released here, not in the loop below: a finish step
                    # rides this same fifo for its own transfer next, and
                    # acquiring it again before releasing a's would be
                    # cumulative on the same outstanding acquire, not a new
                    # one.
                    if ride_index is not None and not held[ride_index]:
                        fifos[ride_index].release(1)
                    tile = scratch_a
                    for idx, (c_fn, meta) in enumerate(zip(chain_fns, chain_meta)):
                        c_positions, c_scalars, c_order, n_c_args, at, binary = meta
                        last = idx == len(chain_meta) - 1
                        dst = (
                            elements[n_in]
                            if last
                            else (scratch_b if tile is scratch_a else scratch_a)
                        )
                        extra = None
                        source = (
                            fifos[ride_index] if ride_index is not None else finish_fifo
                        )
                        if binary:
                            assert source is not None, "the ridden fifo or its own"
                            extra = source.acquire(1)
                        c_inputs = [
                            tile if i == at else extra
                            for i in range(len(c_positions) - 1)
                        ]
                        c_elements = c_inputs + [dst]
                        c_fn(
                            *(
                                c_elements[c_order[i]] if i in c_order else c_scalars[i]
                                for i in range(n_c_args)
                            )
                        )
                        if binary:
                            assert source is not None, "the ridden fifo or its own"
                            source.release(1)
                        tile = dst
                    for j, f in enumerate(fifos):
                        if not held[j] and j != ride_index:
                            f.release(1)
            for j in kept:
                fifos[j].release(segments)

        workers = [
            Worker(
                core_fn_chain,
                [
                    (of[k % len(of)][k // len(of)] if s.replicate else of[k % len(of)])
                    for s, of in zip(ins, of_ins)
                ]
                + [of[k] for of in of_outs]
                + ([of_finish[k]] if of_finish is not None else [])
                + [kernel]
                + chain_kernels
                + [scratch_as[k]]
                + ([scratch_bs[k]] if scratch_bs is not None else [])
                + [rtps[k]],
            )
            for k in range(cores)
        ]
        return Built(workers, rtps)


# An operand split over every core: one lane per (column, channel).
CORES = (Elementwise.num_aie_columns, Elementwise.num_channels)


class UnaryElementwise(Elementwise):
    """A flat buffer in, a flat buffer of the same size out."""

    test = Testing(Sweep())
    size: int = param()
    valid = per_call(bounds=size)

    x = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    y = Out(
        like=x,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    # A finish step's other input, on x's one free input channel.
    finish0 = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
        when=Elementwise.uses_extra,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid

    def over(self, elements: int, line: int) -> Self:
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in self.declaration.tunables
        }
        return self.replace(size=elements, tile_size=line, bound_values={}, **one)


class BinaryElementwise(Elementwise):
    """Two flat buffers in, one of the same size out."""

    test = Testing(Sweep(channels=None))
    size: int = param()
    valid = per_call(bounds=size)

    a = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    b = In(
        size,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    y = Out(
        like=a,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    # A finish step's other input: a and b already hold both of a core's
    # input channels, so it rides a's instead of streaming of its own.
    finish0 = In(
        size,
        obj_shape=Select(Elementwise.rides, None, (Elementwise.tile_size,)),
        per=CORES,
        when=Elementwise.uses_extra,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid

    over = UnaryElementwise.over

    def sequence(self, rt) -> None:
        """Fill every input and drain every output: the derived sequence.

        Riding, ``a``'s lane also carries a finish's other input, its own transfer right
        after ``a``'s own.
        """
        tg = rt.task_group()
        ridden = self.a if self.rides else None
        riding_finish0 = self.finish0 if self.rides and self.uses_extra else None
        for buf in self.inputs:
            if buf is riding_finish0:
                # Not streamed while riding: no transfers() of its own, it
                # rides ridden's instead, below.
                continue
            for lane, tap, word, unit in buf.transfers():
                buf.fill(
                    tap, lane=lane, group=tg, length_parameter=word, length_unit=unit
                )
            if ridden is not None and buf is ridden and riding_finish0 is not None:
                # finish0 isn't streamed while riding, so its own .lanes/
                # .batch_axes aren't available; it shares ridden's shape and
                # placement, so partition by those instead.
                parts = TensorAccessPattern.full(riding_finish0.shape).partition(
                    ridden.lanes, ridden.batch_axes
                )
                for lane, part in enumerate(parts):
                    ridden.fill(part, lane=lane, source=riding_finish0, group=tg)
        for buf in self.outputs:
            for lane, tap, word, unit in buf.transfers():
                buf.drain(
                    tap,
                    lane=lane,
                    group=tg,
                    wait=True,
                    length_parameter=word,
                    length_unit=unit,
                )
        rt.finish(tg)


class Rowwise(Elementwise):
    """``rows`` rows of ``tile_size`` elements in, the same out, one kernel call per row.

    For a kernel that reduces over its line, so the line is a
    ``param()`` the cores read: another line would compute something
    else.
    """

    test = Testing(Sweep(rows=True))

    rows: int = param()
    valid = per_call(bounds=rows)
    tile_size: int = param(array=True)

    tile_cap: ClassVar[int] = 8192

    x = In(
        rows,
        tile_size,
        obj_shape=(tile_size,),
        per=CORES,
    )
    y = Out(
        rows,
        tile_size,
        obj_shape=(tile_size,),
        per=CORES,
    )

    @property
    def valid_elements(self) -> int:
        return self.valid * self.tile_size

    def over(self, elements: int, line: int) -> Self:
        if line != self.tile_size:
            raise ValueError(
                f"{type(self).__name__} reduces over rows of {self.tile_size}, "
                f"not a {line}-element tile"
            )
        one = {
            n: 1
            for n in ("num_aie_columns", "num_channels")
            if n in self.declaration.tunables
        }
        return self.replace(rows=elements // line, bound_values={}, **one)


def _admitted(tolerance: Tolerance, ref: np.ndarray) -> np.ndarray:
    """Return the largest ``|actual - ref|`` that ``tolerance`` admits at each bf16 ``ref``."""
    if tolerance.range_frac is not None:
        raise ValueError("no element-wise bound for a range_frac tolerance")
    ref = np.abs(np.asarray(ref, np.float32))
    if tolerance.kind == "ulps":
        assert tolerance.ulps is not None, "kind == 'ulps' iff ulps is set"
        # n ulps away is furthest upward in magnitude, where the steps grow.
        bits = ref.astype(bfloat16).view(np.uint16).astype(np.int32)
        up = (bits + tolerance.ulps).astype(np.uint16).view(bfloat16)
        return np.maximum(up.astype(np.float32) - ref, tolerance.atol or 0.0)
    if tolerance.kind == "relative":
        rtol = tolerance.rtol or 0.0
        return np.maximum(tolerance.atol or 0.0, 2 * rtol * ref / (1 - rtol))
    raise ValueError(f"no absolute bound for a {tolerance.kind} tolerance")


def finish_bound(
    finish: tuple[FinishStep, ...],
    own: Tolerance | None,
    own_reference,
    n_own: int,
    dtype,
    dev,
    line: int,
) -> Any:
    """Return a bound function (``Tolerance.bounded``) over ``n_own`` own inputs then each finish step's other input in turn.

    ``own``'s tolerance around ``own_reference``'s exact result, then each step's own,
    propagated as ``WeightedRowwise.tolerance`` composes one weight multiply,
    generalized to any number of elementwise steps. ``line`` is the producer's own tile,
    which its finish's kernel matches.
    """
    tiny = float(np.finfo(np.float32).tiny)

    def bound(*inputs):
        own_inputs, extra = list(inputs[:n_own]), list(inputs[n_own:])
        x = np.asarray(own_reference(*own_inputs), np.float64)
        if own is None:
            lo = hi = x
        else:
            delta = _admitted(own, x)
            lo, hi = x - delta, x + delta
        pos = 0
        for step in finish:
            consumer = step.consumer_at(line, dev, elements=x.size)
            gate = consumer.tolerance() or Tolerance.default_for(dtype)
            k = len(consumer.inputs) - 1
            others = extra[pos : pos + k]
            pos += k

            def apply(v, others=others):
                args = [
                    v if i == step.at else others[i - (i > step.at)]
                    for i in range(len(consumer.inputs))
                ]
                return np.asarray(consumer.reference(*args), np.float64)

            exact, lo_y, hi_y = apply(x), apply(lo), apply(hi)
            lo, hi = np.minimum(lo_y, hi_y), np.maximum(lo_y, hi_y)
            half = sum(
                np.exp2(np.floor(np.log2(np.maximum(np.abs(v), tiny))) - 8)
                for v in (exact, hi)
            )
            spread = _admitted(gate, exact)
            x, lo, hi = exact, lo - spread - half, hi + spread + half
        return np.maximum(hi - x, x - lo).reshape(x.shape)

    return bound


class WeightedRowwise(Rowwise):
    """A ``Rowwise`` kernel's rows, optionally times a learned ``weight`` row.

    Weighted, two cores per (column, channel) are pipelined, the second
    multiplying by the row, which halves the line a core holds.
    """

    # The longest weighted row: the weight row beside each line halves it.
    weighted_cap: ClassVar[int] = 4096

    test = Testing(
        [
            Sweep(rows=True),
            Sweep(rows=True, tile_cap=weighted_cap, lower=True, weighted=True),
        ]
    )

    weighted: bool = param(default=False)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=CORES,
    )
    # Shared by every column of a channel: counted once per channel.
    weight = In(
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=(Elementwise.num_channels,),
        replicate=True,
        when=weighted,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(Rowwise.tile_size,),
        per=CORES,
    )

    def validate(self) -> None:
        if self.weighted and self.tile_size > self.weighted_cap:
            raise ValueError(
                f"{type(self).__name__}: tile_size ({self.tile_size}) must be at "
                f"most {self.weighted_cap} when weighted, since the multiplying "
                f"core holds the weight row beside each line"
            )

    def chain(self) -> tuple[KernelCall, ...]:
        if not self.weighted:
            return super().chain()
        config = self.layout()
        return (
            KernelCall(config.kernel(), config.scalars(), (self.x,)),
            KernelCall(eltwise.mul_sized(self.tile_size), (), (None, self.weight)),
        )

    def reference(self, x, weight=None):
        """Run the kernels' references in turn, the kernel's row rounded to bf16."""
        normed = super().reference(x)
        if weight is None:
            return normed
        y = eltwise.mul_sized(self.tile_size).contract.reference(normed, weight)
        return y.astype(normed.dtype)

    def tolerance(self) -> Tolerance | None:
        own = super().tolerance()
        if not self.weighted or own is None:
            return own
        arch = resolve_target_arch(self.dev)
        mul = eltwise.mul_sized(self.tile_size).contract_for(arch).tolerance
        tiny = float(np.finfo(np.float32).tiny)

        def bound(x, weight):
            # The row's error as its kernel's contract admits, scaled by the
            # weight; the two products' roundings, each to its own binade; and
            # what mul_sized's contract admits about the larger product.
            normed = np.abs(np.asarray(Rowwise.reference(self, x), np.float32))
            w = np.abs(np.asarray(weight, np.float32)).reshape(-1)
            w = np.resize(w, normed.size).reshape(normed.shape)
            moved = w * _admitted(own, normed)
            exact = normed * w
            reach = exact + moved
            half = sum(
                np.exp2(np.floor(np.log2(np.maximum(v, tiny))) - 8)
                for v in (exact, reach)
            )
            return moved + half + _admitted(mul, reach.astype(bfloat16))

        return Tolerance.bounded(
            bound,
            note="the row's kernel's contract times |weight|, both products' "
            "roundings, then mul_sized's contract",
        )

    def build(self) -> Built:
        if not self.weighted:
            return super().build()
        tile_ty = self.x.obj_type
        cols, chans = self.num_aie_columns, self.num_channels
        depth = self.x.l1_depth
        kernel = self.kernel()
        positions, scalars = self.arguments(kernel, self.scalars(), 1, 1)
        n_args = len(positions) + len(scalars)
        eltwise_mul = eltwise.mul_sized(self.tile_size)
        x_ends = self.x.fifos(depth)
        # One fifo per channel, each column of it taking its own cons(): a
        # weight row is shared by every column of its channel.
        w_ends = self.weight.fifos(depth, readers=cols)
        of_mid = [
            ObjectFifo(tile_ty, depth=depth) for i in range(cols) for j in range(chans)
        ]
        y_ends = self.y.fifos(depth)
        n_cores = cols * chans
        rtps = [Rtp([self.count]) for _ in range(2 * n_cores)]

        def core_kernel(of_in, of_out, kernel_fn, rtp):
            n = rtp.read()[self.count]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                tiles = dict(zip(positions, (elem_in, elem_out)))
                kernel_fn(
                    *(tiles[i] if i in tiles else scalars[i] for i in range(n_args))
                )
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, rtp):
            n = rtp.read()[self.count]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out, self.tile_size)
                of_in.release(1)
                of_out.release(1)
            of_w.release(1)

        workers = []
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_kernel,
                        [
                            x_ends[k],
                            of_mid[k].prod(),
                            kernel,
                            rtps[k],
                        ],
                    )
                )
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_mul,
                        [
                            of_mid[k].cons(),
                            w_ends[j][i],
                            y_ends[k],
                            eltwise_mul,
                            rtps[n_cores + k],
                        ],
                    )
                )
        return Built(workers, rtps)


class RowBroadcast(Rowwise):
    """``rows`` rows of ``tile_size`` elements, each met elementwise by one ``row``.

    A core holds ``row`` whole; past ``tile_cap`` a row is cut into
    ``segments`` lines of ``line`` elements, each met by its own
    segment: the same sums, in more calls.
    """

    # Rows past the cap: cut in two (Whisper's 5120-wide bias) and in six.
    test = Testing(
        [
            Sweep(rows=True),
            Case(dict(rows=64, tile_size=5120), id="wide_row", lower=True),
            Case(dict(rows=8, tile_size=12288), id="wider_row"),
        ]
    )

    segments: int = tunable(init=False)
    line: int = tunable(init=False)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(line,),
        per=CORES,
    )
    row = In(
        Rowwise.tile_size,
        obj_shape=(line,),
        per=(Elementwise.num_channels,),
        replicate=True,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_shape=(line,),
        per=CORES,
    )

    @classmethod
    def segments_for(cls, width: int) -> int | None:
        """Return the fewest lines a ``width``-element row is cut into for a core.

        A core holds it beside two lines each of x and y, as much as a
        row at the cap takes; None where no cut does.
        """
        return next(
            (
                s
                for s in range(1, width + 1)
                if width % s == 0 and width + 4 * (width // s) <= 5 * cls.tile_cap
            ),
            None,
        )

    def resolve(self, dev) -> Self:
        W = self.tile_size
        segments = self.segments_for(W)
        if segments is None:
            raise Unresolvable(
                f"{type(self).__name__}: a {W}-element row and its lines do not "
                f"fit a core beside {4 * self.tile_cap} elements of x and y"
            )
        (out,) = self.outputs
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            self.num_channels,
            fits=lambda c: out.elements % (c * self.num_channels * W) == 0,
        )
        return self.replace(num_aie_columns=cols, segments=segments, line=W // segments)

    @property
    def lines(self) -> int:
        (out,) = self.outputs
        return out.elements // self.line

    def held_segments(self) -> int:
        return self.segments
