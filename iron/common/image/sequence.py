# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""OperatorSequence: what one run of several operators builds and dispatches."""

import logging
from collections.abc import Hashable, Mapping

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import NPU2
from aie.utils import bfp
from aie.utils.hostruntime.tensor_class import COHERENCE_GRANULE

from ..declare import Operator
from .allocator import Allocation, ArenaPlan, align_up, live_ranges, place
from .artifacts import Artifacts, Design, Step
from .callable import (
    ScratchArena,
    SequenceCompareCallable,
    SequenceFullELFCallable,
    SequenceReferenceCallable,
    SequenceXclbinCallable,
)
from .fused import FusedImage, XclbinChain
from .jit_compile import cache_entry

logger = logging.getLogger(__name__)

# Where every buffer in an arena starts. The host reconciles a buffer with the
# device a coherence granule (a cache line) at a time, so two buffers sharing
# one cannot be synced independently -- XRTTensor.subview refuses such a view.
# 64 bytes is also the DDR burst the shim DMA issues, so no transfer starts
# mid-burst.
ALIGNMENT = max(64, COHERENCE_GRANULE)


def _base_name(buf: str) -> str:
    """The buffer a runlist name refers to: ``"kv[0:64]"`` is part of ``"kv"``."""
    return buf[: buf.index("[")] if "[" in buf else buf


def _signature(op):
    """The runtime arguments an operator takes: direction, shape and dtype each."""
    return [(b.direction, tuple(b.shape), bfp.dtype_name(b.dtype)) for b in op.buffers]


class OperatorSequence:
    """Operator that concatenates a runlist of operators into a
    single dispatch.

    Args:
        dispatch: The mode. ``"auto"`` (default) is ``"fused"`` on NPU2 and
            ``"separate"`` elsewhere. ``"fused"`` builds one full ELF (NPU2
            only); ``"separate"`` one xclbin per design, chained, dispatched
            one step at a time. ``"reference"`` builds nothing and runs each
            operator's CPU ``reference()``; ``"compare"`` runs the chain and
            after each step re-runs the reference on the NPU-produced inputs
            (``SequenceCompareCallable`` judges each step by its
            operator's kernel contract).
        arena: Place the scratch buffers in this shared :class:`ArenaPlan`
            rather than a private arena. Only the full ELF addresses its
            scratch by offset in a buffer it is handed, so only it can share.
            The reference mode lays the arena out (a plan checkable without
            an NPU) but runs each buffer on the host by name, so it shares
            nothing.
        residents: With ``arena``, the scratch buffers that are residents
            there, by storage key; every other scratch buffer is a transient.
    """

    def __init__(
        self,
        name,
        runlist,
        input_args,
        output_args,
        buffer_sizes=None,
        buffer_offsets=None,
        plan_scratch=True,
        dispatch="auto",
        extra_flags=None,
        trace_size=0,
        share_designs=False,
        arena: ArenaPlan | None = None,
        residents: Mapping[str, Hashable] | None = None,
        *args,
        **kwargs,
    ):
        mode = self._coerce_dispatch(dispatch)
        if arena is not None and mode not in (None, "fused", "reference"):
            raise ValueError(
                f"a shared arena needs the full ELF, which addresses scratch by "
                f"offset; dispatch={dispatch!r} gives each buffer its own"
            )
        if residents and arena is None:
            raise ValueError("residents are placed in an arena; pass arena= too")
        if not all(
            isinstance(op, Operator) and all(isinstance(buf, str) for buf in bufs)
            for op, *bufs in runlist
        ):
            raise TypeError(
                "runlist entries must be (Operator, *str) tuples; "
                "each operator must be an Operator and each buffer name must be a str"
            )
        if args:
            raise TypeError(
                f"OperatorSequence takes no positional extras, got {args!r}"
            )
        if kwargs:
            raise TypeError(f"unexpected keyword arguments {sorted(kwargs)}")
        self.runlist = runlist
        # Sharing changes which designs are built, so it belongs in the label
        # the chain's kernel instances are named from.
        self.name = name + "_shared" if share_designs else name
        self.input_args = input_args
        self.output_args = output_args
        # Planned byte offsets per buffer name; None packs the buffers back
        # to back.
        self.buffer_offsets = buffer_offsets
        # Pool intermediates whose lifetimes do not overlap. On by default:
        # the layout is inferred from the runlist, so a caller does not supply
        # it. Pass False to pack every buffer back to back instead.
        self.plan_scratch = plan_scratch
        self.explicit_buffer_sizes = (
            buffer_sizes or {}
        )  # Optional dict: buffer_name -> size_in_bytes
        # Extra aiecc flags forwarded to the full-ELF build.
        self.extra_flags = extra_flags or []
        # Bytes of hardware trace buffer per runlist step; 0 leaves the design untraced.
        self.trace_size = trace_size
        self.share_designs = share_designs
        self.arena = arena
        self.residents = dict(residents or {})
        self._arena_layout: dict[str, Allocation] | None = None
        self.mode = mode  # None until the device is known (prepare)
        self._image = None  # the mode's image builder, once resolved

    @staticmethod
    def _coerce_dispatch(dispatch):
        if dispatch == "auto" or dispatch is None:
            return None  # the platform default, resolved when the device is known
        if isinstance(dispatch, str) and dispatch in _MODES:
            return dispatch
        raise TypeError(
            f"dispatch {dispatch!r} is not one of {sorted(_MODES)} or 'auto'"
        )

    def unique_operators(self):
        """Operators in runlist order, de-duplicated by identity."""
        seen = {}
        for op, *_ in self.runlist:
            seen.setdefault(id(op), op)
        return list(seen.values())

    def unique_designs(self):
        """The designs to build, and which design each operator uses.

        With ``share_designs`` set, operators reporting the same ``design_key``
        collapse onto one design, so it is built, prefixed and configured once.
        """
        designs = []
        design_of = {}
        first_with_key = {}
        for op in self.unique_operators():
            key = op.design_key() if self.share_designs else None
            if key is not None and key in first_with_key:
                shared = designs[first_with_key[key]]
                if _signature(op) != _signature(shared):
                    raise ValueError(
                        f"{op.name} and {shared.name} report the same design_key but "
                        "different runtime arguments, so the design cannot be shared"
                    )
                design_of[id(op)] = first_with_key[key]
                continue
            if key is not None:
                first_with_key[key] = len(designs)
            design_of[id(op)] = len(designs)
            designs.append(op)
        return designs, design_of

    def infer_buffer_offsets(self):
        """Byte offsets letting intermediates with disjoint lifetimes overlap.

        Only buffers this sequence both writes and later reads are pooled.
        Anything the host addresses -- the sequence's own inputs and outputs,
        and any buffer given an explicit size -- is pinned: its contents
        outlive the sequence, so it needs a private, stable address.
        """
        sizes, steps = {}, []
        for op, *bufs in self.runlist:
            reads, writes = [], []
            for buf, b in zip(bufs, op.buffers):
                sizes.setdefault(buf, b.nbytes)
                if b.direction in ("in", "inout"):
                    reads.append(buf)
                if b.direction in ("out", "inout"):
                    writes.append(buf)
            steps.append((reads, writes))

        pinned = set(self.input_args) | set(self.output_args)
        pinned |= set(self.explicit_buffer_sizes)
        # A slice is not free to move: it has to sit at its parent's offset
        # plus its start, and calculate_buffer_layout resolves it that way.
        # Pooling one would hand it an address unrelated to its parent, which
        # is silent -- the slice simply reads the wrong memory.
        pinned |= {name for name in sizes if "[" in name}
        ranges = live_ranges(steps, pinned=pinned)
        allocations, _ = place(ranges, sizes, ALIGNMENT)
        return {name: a.offset for name, a in allocations.items()}

    def _place_in_arena(self, sizes: Mapping[str, int]) -> dict[str, Allocation]:
        """This sequence's scratch buffers placed in the shared arena, once.

        A slice's use is a use of its parent, so a parent only ever reached
        through slices is live from the first to the last of them.
        """
        if self._arena_layout is not None:
            return self._arena_layout
        missing = set(self.residents) - set(sizes)
        if missing:
            raise ValueError(
                f"residents {sorted(missing)} are not scratch buffers of {self.name}"
            )
        steps = []
        for op, *bufs in self.runlist:
            reads, writes = [], []
            for buf, b in zip(bufs, op.buffers):
                name = _base_name(buf)
                if name not in sizes:
                    continue
                if b.direction in ("in", "inout"):
                    reads.append(name)
                if b.direction in ("out", "inout"):
                    writes.append(name)
            steps.append((reads, writes))
        assert self.arena is not None, "placed in an arena plan"
        self._arena_layout = self.arena.place_image(steps, sizes, self.residents)
        return self._arena_layout

    def calculate_buffer_layout(self):
        args = {}  # base_buffer_name -> the declared buffer
        sliced_buffers = (
            {}
        )  # full_buffer_name (with slice) -> (base_name, start, end, buffer)

        for op, *bufs in self.runlist:
            declared = op.buffers
            if len(declared) != len(bufs):
                raise ValueError(
                    f"Number of buffers ({len(bufs)}) must match the operator's "
                    f"declared buffers ({len(declared)}) for operator {op!r}"
                )
            for i, buf_name in enumerate(bufs):
                args_spec = declared[i]

                # Parse slice notation: "buffer_name[start:end]"
                if "[" in buf_name and buf_name.endswith("]"):
                    base_name = buf_name[: buf_name.index("[")]
                    slice_part = buf_name[buf_name.index("[") + 1 : -1]
                    start, end = map(int, slice_part.split(":"))
                    sliced_buffers[buf_name] = (base_name, start, end, args_spec)
                    # Track that base buffer exists (size will be set later)
                    if (
                        base_name not in args
                        and base_name not in self.explicit_buffer_sizes
                    ):
                        raise ValueError(
                            f"Sliced buffer '{buf_name}' requires explicit size for base buffer '{base_name}' in buffer_sizes parameter"
                        )
                else:
                    if buf_name not in args:
                        args[buf_name] = args_spec
                    else:
                        if np.prod(args[buf_name].shape) != np.prod(args_spec.shape):
                            raise ValueError(
                                f"Buffer '{buf_name}' has conflicting sizes between operators: "
                                f"{args[buf_name].shape} vs {args_spec.shape}"
                            )

        # Verify all input/output args are present (either as regular or sliced buffers)
        all_buffer_names = set(args.keys()) | set(sliced_buffers.keys())
        for arg in self.input_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Input argument {arg} not found in runlist buffers")
        for arg in self.output_args:
            if arg not in all_buffer_names and arg not in self.explicit_buffer_sizes:
                raise ValueError(f"Output argument {arg} not found in runlist buffers")

        subbuffer_layout = {}
        slice_info = {}  # full_buffer_name -> (base_name, start, end)

        def add_buffers(buffer_type, args_list):
            # Without a plan, buffers pack back to back in declaration order and
            # every one stays resident for the whole sequence. A plan assigns
            # offsets from liveness instead, so buffers whose lifetimes do not
            # overlap share addresses; the arena still has to be large enough
            # for the highest byte any of them reaches.
            def length_of(arg):
                if arg in self.explicit_buffer_sizes:
                    # Explicit size specified - this is a parent buffer for slices
                    return self.explicit_buffer_sizes[arg]
                if arg in args:
                    return args[arg].nbytes
                return None  # sliced buffers are handled separately

            if buffer_type == "scratch" and self.arena is not None:
                lengths = {a: length_of(a) for a in args_list}
                placed = self._place_in_arena(
                    {a: n for a, n in lengths.items() if n is not None}
                )
                for arg, a in placed.items():
                    subbuffer_layout[arg] = (buffer_type, a.offset, a.size)
                # This image's own extent; the arena it runs in may be larger.
                return max((a.end for a in placed.values()), default=0)

            offsets = self.buffer_offsets
            if offsets is None and self.plan_scratch:
                offsets = self.infer_buffer_offsets()
            offsets = offsets or {}

            # Unplanned buffers first, packed back to back, each aligned.
            cursor = end = 0
            planned = []
            for arg in args_list:
                length = length_of(arg)
                if length is None:
                    continue
                if arg in offsets:
                    planned.append((arg, length))
                    continue
                subbuffer_layout[arg] = (buffer_type, cursor, length)
                end = cursor + length
                cursor = align_up(end, ALIGNMENT)

            # Then the planned ones, rebased past everything unplanned. A plan
            # is relative to its own pool and starts at zero, so applying it
            # directly would drop the first planned buffer on top of the
            # weights -- an aliasing that is silent, because the arena simply
            # does not grow.
            for arg, length in planned:
                at = cursor + offsets[arg]
                subbuffer_layout[arg] = (buffer_type, at, length)
                end = max(end, at + length)
            return end  # arena size

        # Add sliced buffer entries to layout (they reference parent buffers)
        for buf_name, (base_name, start, end, args_spec) in sliced_buffers.items():
            slice_info[buf_name] = (base_name, start, end)

        input_buffer_size = add_buffers("input", self.input_args)
        output_buffer_size = add_buffers("output", self.output_args)
        scratch_args = [
            arg
            for arg in args
            if arg not in self.input_args and arg not in self.output_args
        ]
        # Also include explicit buffers that are only used for slicing
        for explicit_buf in self.explicit_buffer_sizes:
            if (
                explicit_buf not in self.input_args
                and explicit_buf not in self.output_args
                and explicit_buf not in scratch_args
            ):
                scratch_args.append(explicit_buf)
        scratch_buffer_size = add_buffers("scratch", scratch_args)

        buffer_sizes = (input_buffer_size, output_buffer_size, scratch_buffer_size)
        return subbuffer_layout, buffer_sizes, slice_info

    def prepare(self):
        """Settle the mode and lay the buffers out, before anything is built."""
        if self.mode is None:
            # The platform default for a hand-written sequence; a graph goes
            # through packaging.plan, which also weighs its values and boundaries.
            npu2 = isinstance(aie_utils.get_current_device(), NPU2)
            self.mode = "fused" if npu2 else "separate"
            if self.arena is not None and not npu2:
                raise ValueError(
                    f"{self.name}: a shared arena needs the full ELF, which this "
                    f"device does not dispatch"
                )
        # Every operator resolved for the device, once, before anything takes
        # its identity: unique_designs() then sees the knobs as they will be
        # built, so two operators that describe one array are one design.
        dev = aie_utils.get_current_device()
        resolved: dict[int, Operator] = {}
        for op, *_ in self.runlist:
            if id(op) not in resolved:
                resolved[id(op)] = op.resolved(dev)
        self.runlist = [(resolved[id(op)], *bufs) for op, *bufs in self.runlist]
        # After the mode: a sequence that cannot run in its arena must not
        # have placed anything there.
        self.subbuffer_layout, self.buffer_sizes, self.slice_info = (
            self.calculate_buffer_layout()
        )
        image, _ = _MODES[self.mode]
        self._image = image() if image is not None else None

    def compile(self, record: str = "memory"):
        """Build the image ahead of time, and record what it consists of.

        ``link()`` is idempotent and ``get_callable()`` still goes through
        it, so this is the ahead-of-time path: a host with the toolchain and
        no runtime compiles and hands the image on. ``record="disk"`` also
        writes the :class:`~iron.common.artifacts.Artifacts` record beside
        the image.
        """
        self.prepare()
        self.link()
        if record == "disk":
            self.artifacts.dump()
        return self

    def link(self):
        """Build this sequence's image, once; sets ``self.image`` (``None`` for
        the reference mode) and :attr:`artifacts`.
        """
        if not hasattr(self, "subbuffer_layout"):
            self.prepare()
        self.image = self._image.link(self) if self._image is not None else None
        self._artifacts = self._record()
        return self.image

    @property
    def elf_path(self):
        """The fused ELF, when that is this sequence's image."""
        return self.image if isinstance(self._image, FusedImage) else None

    @property
    def artifacts(self) -> Artifacts:
        """The record of what :meth:`link` produced."""
        artifacts = getattr(self, "_artifacts", None)
        if artifacts is None:
            raise RuntimeError(f"{self.name} is not linked; compile() first")
        return artifacts

    def _record(self):
        """What this image consists of: its designs, its steps, its buffers."""
        if self._image is None:
            return None
        designs, design_of = self.unique_designs()
        operators = list(self.unique_operators())
        labels = [f"op{i}_{type(op).__name__}" for i, op in enumerate(designs)]
        sharing = [
            tuple(op.name for op in operators if design_of[id(op)] == i)
            for i in range(len(designs))
        ]
        if isinstance(self._image, FusedImage):
            assert self._image.design is not None, "link() built the image"
            entry = cache_entry(self._image.design)
            records = tuple(
                Design(name=labels[i], operators=sharing[i])
                for i in range(len(designs))
            )
            kind, image, insts = "elf", entry.elf, None
            by_design = {id(op): labels[design_of[id(op)]] for op in operators}
        else:
            chain = self._image
            entry = None
            records = []
            for i, op in enumerate(designs):
                design = chain.op_design_map[id(op)]
                own = cache_entry(design)
                entry = entry or own
                records.append(
                    Design(
                        name=chain.op_kernel_name_map[id(op)],
                        operators=sharing[i],
                        entry=own,
                        image=own.xclbin,
                        insts=chain.op_insts_path_map[id(op)],
                    )
                )
            records = tuple(records)
            kind, image, insts = "xclbin", chain.combined_xclbin_path, None
            by_design = {id(op): chain.op_kernel_name_map[id(op)] for op in operators}
        assert image is not None, "the image has been built"
        steps = tuple(
            Step(i, op.name, by_design[id(op)], tuple(names))
            for i, (op, *names) in enumerate(self.runlist)
        )
        return Artifacts(
            kind=kind,
            image=image,
            insts=insts,
            entry=entry,
            designs=records,
            steps=steps,
            buffers=dict(self.subbuffer_layout),
        )

    def get_callable(self, arena: ScratchArena | None = None):
        """The runtime callable of this sequence's mode, compiling first if
        that has not happened (``compile()`` beforehand is the ahead-of-time
        path; the work is the same, only when it happens differs).

        A sequence placed in an arena plan runs its scratch in ``arena``, the
        buffer behind that plan; made here if not given.
        """
        if not hasattr(self, "subbuffer_layout"):
            self.compile()
        self.link()
        assert self.mode is not None, "link() chose the mode"
        if self.mode != "fused":
            return _MODES[self.mode][1](self)
        if self.arena is not None and arena is None:
            arena = ScratchArena(self.arena)
        return SequenceFullELFCallable(self, arena=arena)

    def get_layout_for_buffer(self, buffer_name):
        """Return the (buffer_type, offset, length) layout for a named buffer.

        Sliced buffers are resolved recursively to their parent's absolute
        offset.

        Args:
            buffer_name: Name of the buffer, optionally with slice notation.

        Returns:
            Tuple of (buf_type, offset_bytes, length_bytes).
        """
        if buffer_name in self.slice_info:
            buf_name, start, end = self.slice_info[buffer_name]
            buf_type, parent_start, _ = self.get_layout_for_buffer(buf_name)
            return buf_type, parent_start + start, end - start

        buf_type, offset, length = self.subbuffer_layout[buffer_name]
        return buf_type, offset, length


# The modes a sequence can be built in: the image (None builds nothing) and
# the callable that runs it.
_MODES = {
    "fused": (FusedImage, SequenceFullELFCallable),
    "separate": (XclbinChain, SequenceXclbinCallable),
    "reference": (None, SequenceReferenceCallable),
    "compare": (XclbinChain, SequenceCompareCallable),
}
