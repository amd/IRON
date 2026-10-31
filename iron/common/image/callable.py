# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a caller invokes once a sequence has an image: one class per image kind."""

from __future__ import annotations

import logging
import time
import weakref
from collections.abc import Callable, Collection, Mapping
from pathlib import Path
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import ml_dtypes
import numpy as np
from aie.utils.npukernel import NPUKernel
from aie.utils.trace import get_trace_buffer

from ..declare import Operator
from .allocator import ALIGNMENT, BANK, ArenaPlan, Pool
from .compose import Composition
from .step import BufferRef

if TYPE_CHECKING:
    import pyxrt  # pyright: ignore[reportMissingImports]
    from aie.utils.hostruntime.xrtruntime.hostruntime import (
        XRTKernelHandle,
        XRTKernelResult,
    )
    from aie.utils.hostruntime.xrtruntime.parameter_scratchpad import (
        ParameterScratchpad,
    )
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
else:
    try:
        import pyxrt
        from aie.utils.hostruntime.xrtruntime.hostruntime import XRTKernelResult
        from aie.utils.hostruntime.xrtruntime.parameter_scratchpad import (
            ParameterScratchpad,
        )
        from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
    except ImportError:
        # Host stacks without XRT still compile, and record graphs for reference().
        XRTTensor = None

logger = logging.getLogger(__name__)

BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes, dtype=BF16):
    itemsize = np.dtype(dtype).itemsize
    return max(nbytes, itemsize) // itemsize


def _require_xrt() -> None:
    if XRTTensor is None:
        raise RuntimeError(
            "a graph's image needs the XRT host runtime (pyxrt), which is not "
            "installed. Use graph.reference(), or call a single operator on its "
            "own, which dispatches through aie.utils.DefaultNPURuntime and works "
            "on any backend."
        )


class ScratchArena:
    """An ``ArenaPlan``'s device buffers, a buffer object per bank.

    As the plan grows they grow, keeping their contents, and
    ``generation`` says to rebind.
    """

    def __init__(self, plan: ArenaPlan):
        self.plan = plan
        self._banks: list[XRTTensor] = []
        self._generation = 0
        self.loaded: set = set()

    @property
    def generation(self) -> int:
        return self._generation

    @property
    def banks(self) -> list[XRTTensor]:
        """A buffer object per bank the plan reaches, the last holding the rest."""
        _require_xrt()
        size = self.plan.size
        wanted = [min(BANK, size - start) for start in range(0, size, BANK)] or [0]
        for k, nbytes in enumerate(wanted):
            held = self._banks[k] if k < len(self._banks) else None
            if held is not None and held.shape[0] >= _n_elements(nbytes):
                continue
            grown = XRTTensor((_n_elements(nbytes),), dtype=ml_dtypes.bfloat16)
            if held is None:
                self._banks.append(grown)
            else:
                old = held.numpy()  # pulls what the device wrote
                grown.numpy_view()[: old.size] = old
                logger.info(
                    "scratch bank %d grew from %d to %d bytes",
                    k,
                    old.nbytes,
                    grown.nbytes,
                )
                self._banks[k] = grown
            self._generation += 1
        return list(self._banks)

    def release(self) -> None:
        """Free every bank; ``banks`` makes them again, so the weights load again."""
        self._banks.clear()
        self.loaded.clear()
        self._generation += 1


class FullELFRun:
    """One run of a full ELF's commands, back to back.

    Its own ctrl scratchpad holds per-call values; it ends once the
    shared runtime evicts its image.
    """

    def __init__(
        self,
        name: str,
        image: NPUKernel,
        kernels: list[pyxrt.kernel],
        runs: list[pyxrt.run],
        commands: list[str],
        arguments: Mapping[int, XRTTensor],
        feedback_arg: int | None,
        params_path: Path | None,
    ):
        self.name = name
        self._image = image
        self._kernel = kernels[0]
        self.handles = runs
        self._commands = commands
        self._started = runs
        for index, tensor in arguments.items():
            self.bind(index, tensor.buffer_object())
        self._feedback_arg = feedback_arg
        self._params_path = params_path
        self._params: list[ParameterScratchpad] | None = None
        # Bound to or from another run's scratchpad: a loop holds it.
        self.wired = False

    def bind(self, index: int, bo: pyxrt.bo | None) -> None:
        """Run with ``bo`` as argument ``index``, refusing a released tensor's None."""
        if bo is None:
            raise ValueError(f"{self.name}: argument {index} has no buffer object")
        for handle in self.handles:
            handle.set_arg(index, bo)

    def bind_feedback(self, bo: pyxrt.bo) -> None:
        if self._feedback_arg is None:
            raise ValueError(f"{self.name} declares no feedback argument")
        self.bind(self._feedback_arg, bo)
        self.wired = True

    @property
    def params(self) -> list[ParameterScratchpad] | None:
        """Each command's parameter scratchpad, holding the words it reads.

        ``None`` when ``params.txt`` counts none.
        """
        if self._params is not None:
            return self._params
        if self._params_path is None:
            return None
        if self._params_path.read_text().split()[0] == "0":
            return None
        self._params = [
            ParameterScratchpad(h, self._params_path, command)
            for h, command in zip(self.handles, self._commands)
        ]
        return self._params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        params = self.params
        if params is None:
            raise ValueError(
                f"{self.name} was built without per-call values; got "
                f"{sorted(values)}"
            )
        # Words of different commands may share a slot: each gets its own.
        for block in params:
            for symbol in block.names & values.keys():
                block.write(symbol, values[symbol])
            block.sync()

    def read_value(self, symbol: str) -> int:
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} was built without per-call values")
        block = next(b for b in params if symbol in b.names)
        block.sync_from_device()
        return block.read(symbol)

    def scratchpad_alias(self) -> pyxrt.bo:
        """Return this run's ctrl scratchpad, for another run to drain its feedback into.

        Refused where it has no per-call values, or is several commands.
        """
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} has no per-call values to feed back into")
        if len(params) > 1:
            raise ValueError(
                f"{self.name} is {len(params)} commands; another run's feedback "
                f"sets one scratchpad"
            )
        self.wired = True
        return params[0].alias()

    def start(self, idle: Collection[int] = (), commands: range | None = None) -> None:
        """Start each command's run back to back, but the ``idle`` ones'.

        Runs only ``commands``, where given.
        """
        if aie_utils.DefaultNPURuntime.load(self._image).kernel is not self._kernel:
            raise RuntimeError(
                f"{self.name}: the runtime evicted the image this run was made on"
            )
        span = range(len(self.handles)) if commands is None else commands
        self._started = [self.handles[k] for k in span if k not in idle]
        for handle in self._started:
            handle.start()

    def wait(self) -> None:
        for handle in self._started:
            # run.wait() returns the ert_cmd_state; run.wait2() returns None.
            state = handle.wait()
            if state != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
                raise RuntimeError(f"{self.name}: the run ended in {state}")


def _line_view(parent: XRTTensor, offset: int, length: int, dtype) -> XRTTensor:
    """Return ``length`` bytes of ``parent`` at ``offset`` as ``dtype``.

    Out to the end of their coherence line (no other buffer's), as a view
    ending mid-line cannot sync.
    """
    stop = min(Pool(ALIGNMENT).align(offset + length), parent.nbytes)
    return parent.subview(offset, ((stop - offset) // dtype.itemsize,), dtype)


class ImageCallable:
    """What a caller invokes once a sequence ``op`` has an image.

    Residents placed in an arena plan are views of ``arena``'s banks,
    remade as it grows.
    """

    def __init__(self, seq, arena: ScratchArena | None):
        _require_xrt()
        self.op = seq
        self.arena = arena
        # The last call's seconds.
        self.last_elapsed = 0.0
        self._arena_generation: int | None = None

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        """Write the per-call values the next call reads."""
        raise NotImplementedError

    def get_buffer(self, ref: BufferRef) -> XRTTensor:
        """Return the bytes ``ref`` names, as its dtype."""
        raise NotImplementedError

    def get_storage(self, root: str) -> XRTTensor:
        """Return the buffer ``root`` whole."""
        raise NotImplementedError

    def __call__(self) -> tuple[XRTKernelHandle | None, XRTKernelResult]:
        """Run the sequence once.

        Returns the handle an empty dispatch is timed on
        (``aie.utils.benchmark``), or None, and the call's result.
        """
        raise NotImplementedError

    def _arena_grew(self) -> bool:
        """Whether the arena grew since the views were made, now made again."""
        if self.arena is None or self.arena.generation == self._arena_generation:
            return False
        self._arena_generation = self.arena.generation
        return True


class FullELFCallable(ImageCallable):
    """The full ELF (NPU2); a call dispatches ``run``.

    Where the device heap (about 512 MiB of ctrlcode) is full, a new run
    frees the least recently called one's.
    """

    # The callables holding a run, least recently called first.
    _holding: weakref.WeakValueDictionary[int, FullELFCallable] = (
        weakref.WeakValueDictionary()
    )

    # The device and runtime sequence the full ELF's first command runs.
    device_name = Composition.device
    sequence_name = Composition.sequence_name(0)

    def __init__(self, seq, arena: ScratchArena | None = None):
        super().__init__(seq, arena)
        if (arena is None) != (seq.arena is None):
            raise ValueError(
                f"{seq.name} was placed in "
                + ("an arena plan" if seq.arena is not None else "no arena plan")
                + (", but no arena was given" if arena is None else ", but got one")
            )
        if arena is not None and arena.plan is not seq.arena:
            raise ValueError(f"{seq.name} was placed in another arena plan")
        self.kernel = NPUKernel(
            elf_path=str(seq.image),
            kernel_name=f"{self.device_name}:{self.sequence_name}",
        )
        # Each later command's runtime sequence, on the same hw_context.
        self.later = [
            NPUKernel(
                elf_path=str(seq.image),
                kernel_name=f"{self.device_name}:{Composition.sequence_name(k)}",
            )
            for k in range(1, len(seq.packaging.commands) + 1)
        ]
        # The kernel the runs are made on, which outlives an evicted handle's.
        self._xrt_kernel: pyxrt.kernel | None = None
        self._run: FullELFRun | None = None
        self._runs: list[FullELFRun] = []
        self._buffer_cache = {}
        self._storage_cache = {}
        self._argument_index = {
            kind: index for index, kind in enumerate(seq.buffer_sizes.arguments())
        }
        sizes = seq.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(sizes.input),), dtype=BF16)
        self.output_buffer = XRTTensor((_n_elements(sizes.output),), dtype=BF16)
        if arena is None:
            self.scratch_banks = [
                XRTTensor((_n_elements(sizes.arguments()[kind]),), dtype=BF16)
                for kind in sizes.bank_kinds
            ]
        else:
            self.scratch_banks = arena.banks
            self._arena_generation = arena.generation
        self.feedback_buffer: XRTTensor | None = None
        if sizes.feedback is not None:
            self.feedback_buffer = XRTTensor((sizes.feedback,), dtype=np.uint8)
        # The trace buffer's argument and size are read from the lowered module.
        self.trace_buffer: XRTTensor | None = None
        self._trace_arg: int | None = None
        if seq.traced:
            layout = get_trace_buffer(
                self.lowered_mlir_path.read_text(),
                f"{self.device_name}:{self.sequence_name}",
            )
            if layout:
                self._trace_arg = layout["arg_index"]
                self.trace_buffer = XRTTensor((layout["size"],), dtype=np.int8)

    @property
    def handle(self) -> XRTKernelHandle:
        """The ELF as the shared runtime holds it.

        Loaded again, ending every run, where the runtime evicted it.
        """
        handle = aie_utils.DefaultNPURuntime.load(self.kernel)
        if handle.kernel is not self._xrt_kernel:
            self._xrt_kernel = handle.kernel
            self._run = None
            self._runs = []
        return handle

    @property
    def run(self) -> FullELFRun:
        """The run a call dispatches, one for the image's life."""
        self.handle  # ends the run where the runtime evicted the image
        if self._run is None:
            self._run = self._make_run()
        FullELFCallable._holding.pop(id(self), None)
        FullELFCallable._holding[id(self)] = self
        return self._run

    def new_run(self) -> FullELFRun:
        """Another run over this callable's buffers; each holds a copy of the ctrlcode."""
        return self._make_run()

    def release(self, *, force: bool = False) -> bool:
        """Free ``run`` and unload the image, returning True unless it is in use.

        False means a loop holds the run, another run is out, or another
        callable runs the image.

        ``force`` frees it anyway: the graph is being torn down, so a run
        still wired into its own loop (the loop is torn down with it) or
        shared with a sibling version (torn down beside it) is safe to evict.
        """
        if self._run is None:
            return False
        if not force and (self._run.wired or self._runs != [self._run]):
            return False
        image = self.kernel.elf_path
        assert image is not None, "a FullELFCallable's kernel has an elf_path"
        if not force:
            holding = FullELFCallable._holding.values()
            if any(c.kernel.elf_path == image for c in holding if c is not self):
                return False
        self._run = None
        self._runs = []
        self._xrt_kernel = None
        FullELFCallable._holding.pop(id(self), None)
        # Its hw_context holds some of the device heap, placed after the runs
        # made before it: while it lives, the freed runs are holes.
        aie_utils.DefaultNPURuntime.evict_context(Path(image))
        return True

    def _make_run(self) -> FullELFRun:
        handle = self.handle
        kernels = [
            handle.kernel,
            *(aie_utils.DefaultNPURuntime.load(k).kernel for k in self.later),
        ]
        while True:
            try:
                runs = [pyxrt.run(kernel) for kernel in kernels]
                break
            except RuntimeError as e:
                # ENOSPC: the device heap holds no more control code.
                if "err=-28" not in str(e):
                    raise
                held = [c for c in FullELFCallable._holding.values() if c is not self]
                if not any(c.release() for c in held):
                    raise
                logger.info("%s: the device heap is full; released a run", self.op.name)
        arguments = {
            self._argument_index[kind]: tensor
            for kind, tensor in self._arguments().items()
        }
        if self.trace_buffer is not None:
            assert self._trace_arg is not None
            arguments[self._trace_arg] = self.trace_buffer
        made = FullELFRun(
            self.op.name,
            self.kernel,
            kernels,
            runs,
            [k.kernel_name for k in (self.kernel, *self.later)],
            arguments,
            self._argument_index.get("feedback"),
            self.op.artifacts.params,
        )
        self._runs.append(made)
        return made

    @property
    def params(self) -> list[ParameterScratchpad] | None:
        return self.run.params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        self.run.write_values(values)

    def _arguments(self) -> dict[str, XRTTensor]:
        buffers = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "feedback": self.feedback_buffer,
            **dict(zip(self.op.buffer_sizes.bank_kinds, self.scratch_banks)),
        }
        return {kind: buffers[kind] for kind in self._argument_index}

    @property
    def lowered_mlir_path(self):
        path = self.op.artifacts.lowered_mlir
        if path is None:
            raise FileNotFoundError(
                "the build produced no input_with_addresses.mlir; a traced build "
                "passes --get-input-with-addresses to aiecc"
            )
        return path

    def get_buffer(self, ref: BufferRef):
        """Return the bytes ``ref`` names, and the rest of their last coherence line.

        See ``_line_view``.
        """
        self._follow_arena()
        if ref not in self._buffer_cache:
            kind, offset, length = ref.place(self.op.layout)
            if kind == "scratch":
                kind, offset = self.op.buffer_sizes.scratch_argument(offset, length)
            dtype = self.op.buffer_dtype(ref)
            self._buffer_cache[ref] = _line_view(
                self._arguments()[kind], offset, length, dtype
            )
        return self._buffer_cache[ref]

    def get_storage(self, root: str):
        """Return the buffer and the rest of its last coherence line (``_line_view``)."""
        self._follow_arena()
        if root not in self._storage_cache:
            kind, offset, length = self.op.layout[root]
            if kind == "scratch":
                kind, offset = self.op.buffer_sizes.scratch_argument(offset, length)
            dtype = self.op.buffer_dtype(BufferRef(root))
            self._storage_cache[root] = _line_view(
                self._arguments()[kind], offset, length, dtype
            )
        return self._storage_cache[root]

    def _follow_arena(self) -> None:
        if not self._arena_grew():
            return
        assert self.arena is not None, "_arena_grew() returned True"
        self.scratch_banks = self.arena.banks
        arguments = self._arguments()
        for run in self._runs:
            for kind in self.op.buffer_sizes.bank_kinds:
                run.bind(self._argument_index[kind], arguments[kind].buffer_object())
        self._buffer_cache.clear()
        self._storage_cache.clear()

    def _sync_inputs(self):
        # Sub-views share their parent's coherence map, so a write through one is flushed.
        self._follow_arena()
        for tensor in self._arguments().values():
            tensor.to("npu")
        if self.trace_buffer is not None:
            self.trace_buffer.to("npu")

    def start(self, *runs: FullELFRun, idle: Collection[int] = ()) -> None:
        """Push what the host wrote, and start ``runs`` without waiting.

        Each but its ``idle`` commands.
        """
        self._sync_inputs()
        for run in runs:
            run.start(idle)

    def wait(self, *runs: FullELFRun) -> None:
        """Wait on ``runs``, refusing a host write made while they were out.

        No run read it, and the next push would lay over what they wrote.
        """
        for run in runs:
            run.wait()
        written = [
            kind for kind, tensor in self._arguments().items() if tensor.device == "cpu"
        ]
        if written:
            raise RuntimeError(
                f"{self.op.name}: the host wrote {written} while a run was out; "
                f"write between calls, or start the next run through start()"
            )

    def __call__(
        self,
        idle: Collection[int] = (),
        between: Mapping[int, Callable[[], None]] | None = None,
    ) -> tuple[XRTKernelHandle, XRTKernelResult]:
        """Dispatch ``run`` but its ``idle`` commands.

        ``between[k]()`` runs on the host once the commands before ``k``
        complete, and its writes are pushed.
        """
        self._sync_inputs()
        t0 = time.perf_counter()
        run = self.run
        first = 0
        for k, fn in sorted((between or {}).items()):
            run.start(idle, range(first, k))
            run.wait()
            fn()
            self._sync_inputs()
            first = k
        run.start(idle, range(first, len(run.handles)))
        run.wait()
        self.last_elapsed = time.perf_counter() - t0
        completed = pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED
        return self.handle, XRTKernelResult(completed, round(self.last_elapsed * 1e9))


class PerStepCallable(ImageCallable):
    """Run a ``PerStep`` a dispatch at a time.

    ``check`` holds each step to its reference; residents are arena views,
    transients share one bank-split pool.
    """

    def __init__(self, seq, check: bool = False, arena: ScratchArena | None = None):
        super().__init__(seq, arena)
        self.check = check
        self.dispatch_values: dict[str, np.generic] = {}
        self._buffers: dict[BufferRef, XRTTensor] = {}
        self._storage: dict[str, XRTTensor] = {}
        own_scratch: dict[str, tuple[int, int]] = {}
        for root, (kind, offset, length) in seq.layout.items():
            if self.arena is not None and root in seq.residents:
                continue
            if kind == "scratch":
                own_scratch[root] = (offset, length)
                continue
            ref = BufferRef(root)
            dtype = seq.buffer_dtype(ref)
            self._storage[root] = XRTTensor((_n_elements(length, dtype),), dtype=dtype)
            self._buffers[ref] = self._storage[root]
        # Every transient this image keeps, not a resident, is disjoint in
        # time with some others (Image._layout's Pool.place already proved
        # it, same as the full ELF's arena); one bank-split pool, not one
        # buffer object each, holds them all.
        size = max((o + n for o, n in own_scratch.values()), default=0)
        self._scratch_banks = [
            XRTTensor((_n_elements(min(BANK, size - start)),), dtype=BF16)
            for start in range(0, size, BANK)
        ]
        for root, (offset, length) in own_scratch.items():
            bank, offset = divmod(offset, BANK)
            dtype = seq.buffer_dtype(BufferRef(root))
            view = _line_view(self._scratch_banks[bank], offset, length, dtype)
            self._storage[root] = view
            self._buffers[BufferRef(root)] = view
        # Each step is its own dispatch, over its own buffers; a fusion's
        # steps are one dispatch, over every member's buffers but the ones
        # an edge feeds on-chip (fed_edges), in fusion order.
        self._steps = []
        # The step each dispatch starts at, and its link.
        self._starts: list[int] = []
        self._links = []
        starts = {fusion.steps[0]: fusion for fusion in seq.fusions}
        i, n = 0, len(seq.steps)
        while i < n:
            fusion = starts.get(i)
            if fusion is None:
                step = seq.steps[i]
                link = seq.packaging.step_links[i]
                self._steps.append((step.op, link.kernel, step.buffers, []))
                self._starts.append(i)
                self._links.append(link)
                i += 1
                continue
            fed_edges = {(e.producer, e.output) for e in fusion.edges} | {
                (e.consumer, e.input) for e in fusion.edges
            }
            refs = tuple(
                ref
                for j in fusion.steps
                for ref, b in zip(seq.steps[j].buffers, seq.steps[j].op.buffers)
                if (j, b.name) not in fed_edges
            )
            link = seq.packaging.step_links[i]
            self._steps.append((seq.steps[fusion.steps[0]].op, link.kernel, refs, []))
            self._starts.append(i)
            self._links.append(link)
            i = fusion.steps[-1] + 1
        self._follow_arena()
        self._bind_steps()

    def _bind_steps(self) -> None:
        """Each step's arguments: a whole buffer's storage, else its part."""
        self._steps = [
            (
                step_op,
                kernel,
                refs,
                [
                    self._storage[r.root] if r.nbytes is None else self.get_buffer(r)
                    for r in refs
                ],
            )
            for step_op, kernel, refs, _ in self._steps
        ]

    def _follow_arena(self) -> None:
        """View the residents in the arena's banks, again once it has grown."""
        if not self._arena_grew():
            return
        assert self.arena is not None, "_arena_grew() returned True"
        banks = self.arena.banks
        for root in self.op.residents:
            _, offset, length = self.op.layout[root]
            bank, offset = divmod(offset, BANK)
            dtype = self.op.buffer_dtype(BufferRef(root))
            # A step takes the storage, whole coherence lines (``_line_view``).
            self._storage[root] = _line_view(banks[bank], offset, length, dtype)
        self._buffers = {
            ref: view
            for ref, view in self._buffers.items()
            if ref.root not in self.op.residents
        }
        self._bind_steps()

    def get_buffer(self, ref: BufferRef):
        """Return the bytes ``ref`` names, and the rest of their last coherence line.

        See ``_line_view``.
        """
        self._follow_arena()
        if ref not in self._buffers:
            if ref.root not in self._storage:
                raise ValueError(f"{ref} is no buffer of {self.op.name}")
            _, _, length = ref.place(self.op.layout)
            dtype = self.op.buffer_dtype(ref)
            self._buffers[ref] = _line_view(
                self._storage[ref.root], ref.start, length, dtype
            )
        return self._buffers[ref]

    def get_storage(self, root: str):
        """Return the buffer.

        For a resident in the arena, returns the rest of its last
        coherence line too, which no other buffer holds.
        """
        self._follow_arena()
        return self._storage[root]

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        self.dispatch_values = dict(values)

    def __call__(
        self, between: Mapping[int, Callable[[], None]] | None = None
    ) -> tuple[None, XRTKernelResult]:
        """Dispatch each step, ``between[i]()`` running on the host before step ``i``.

        Never inside a pack's or a fusion's run; the handle is None, no one dispatch
        timed.
        """
        between = dict(between or {})
        inside = set(between) - {*self._starts, len(self.op.steps)}
        if inside:
            raise ValueError(
                f"{self.op.name}: host steps at {sorted(inside)} fall inside a "
                f"run of a pack or a fusion, one dispatch"
            )
        self._follow_arena()
        for root in self.op.inputs:
            self._storage[root].to("npu")
        t0 = time.perf_counter()
        for index, (step_op, kernel, refs, args) in enumerate(self._steps):
            if self._starts[index] in between:
                self._device_resident()
                between[self._starts[index]]()
            checked = self.check and not step_op.bound_extents
            if self.check and not checked:
                logger.warning(
                    "[check step %d] %s not checked: %s bounded per call",
                    index,
                    type(step_op).__name__,
                    sorted(step_op.bound_extents),
                )
            if checked:
                inputs, expected = self._reference(step_op, args)
            symbols = self._links[index].symbols
            kernel(
                *args,
                **{
                    name: self.dispatch_values[symbols.get(name, name)]
                    for name in kernel.dispatch_params
                },
            )
            if checked:
                written = {
                    spec.name: buf.numpy()[: spec.elements]
                    for buf, spec in zip(args, step_op.buffers)
                    if spec.drains
                }
                held = dict(zip((spec.name for spec in step_op.buffers), refs))
                check_step(index, step_op, held, inputs, written, expected)
        self._device_resident()
        if len(self.op.steps) in between:
            between[len(self.op.steps)]()
        self.last_elapsed = time.perf_counter() - t0
        completed = pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED
        return None, XRTKernelResult(completed, round(self.last_elapsed * 1e9))

    def _device_resident(self) -> None:
        """Mark what the steps write device-resident, so a read pulls it, and only then."""
        for root in self.op.layout:
            if root not in self.op.inputs:
                self._storage[root].device = "npu"

    def _reference(
        self, step_op: Operator, args
    ) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
        """Return ``step_op``'s inputs and its reference on them, by buffer name.

        Inputs are read as its buffers hold them, a coded one decoded.
        """
        held = {
            spec.name: buf.numpy()[: spec.elements].reshape(spec.shape).copy()
            for buf, spec in zip(args, step_op.buffers)
        }
        inputs = {b.name: b.logical_form(held[b.name]) for b in step_op.inputs}
        # A reference that takes its outputs writes them in place, keeping
        # what it does not touch (a cache a Copy scatters into).
        outputs = {b.name: held[b.name] for b in step_op.outputs if not b.fills}
        symbols = {v.name: v.symbol for v in step_op.values}
        values = {
            name: self.dispatch_values[symbol]
            for name, symbol in symbols.items()
            if symbol in self.dispatch_values
        }
        expected = step_op._call_reference(inputs, outputs, values)
        return inputs, {
            b.name: np.asarray(expected[b.name]).reshape(b.shape)
            for b in step_op.outputs
        }


def check_step(
    index: int,
    step_op: Operator,
    held: Mapping[str, BufferRef],
    inputs: Mapping[str, np.ndarray],
    written: Mapping[str, np.ndarray],
    expected: Mapping[str, np.ndarray],
) -> None:
    """Hold what step ``index`` wrote, by declared name, to its reference.

    Within its ``tolerance()``; raises where it declares none or an
    output falls outside.
    """
    tol = step_op.resolved().tolerance()
    if tol is None:
        raise ValueError(
            f"[check step {index}] {type(step_op).__name__} declares no "
            f"tolerance() to judge its output by"
        )
    for name, verdict in step_op.judge(inputs, written, tol, expected).items():
        logger.info(
            "[check step %d] %s -> %s: max_abs=%.4g",
            index,
            type(step_op).__name__,
            held[name],
            verdict.max_abs_err,
        )
        if not verdict:
            raise RuntimeError(
                f"[check step {index}] {type(step_op).__name__} "
                f"(name={step_op.name}) -> {held[name]}: NPU output deviates "
                f"from reference ({verdict.detail}; "
                f"inputs={[held[b.name] for b in step_op.inputs]}; "
                f"tolerance {tol})"
            )
