# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a caller invokes once a sequence has an image: one class per image kind."""

from __future__ import annotations

import logging
import time
import weakref
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import ml_dtypes
import numpy as np
from aie.utils.npukernel import NPUKernel
from aie.utils.trace import get_trace_buffer

from ..declare import Operator
from .allocator import ALIGNMENT, BANK, ArenaPlan, Pool
from .fusion import Fusion
from .step import BufferRef

if TYPE_CHECKING:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.hostruntime import XRTKernelHandle
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

    from .xrt import ParameterBlock
else:
    try:
        import pyxrt
        from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

        from .xrt import ParameterBlock
    except ImportError:
        # Host stacks without XRT still compile, and trace graphs for reference().
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
    """The device buffers behind an ``ArenaPlan``, a buffer object per bank,
    shared by every image placed in it.

    A plan that grew since first use grows its last bank, keeping its
    contents, and adds banks; each callable rebinds on its next call
    (``generation``).
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


class FullELFRun:
    """One run of a full ELF, with its own ctrl scratchpad of per-call values:
    a run of each of its commands, started back to back.

    Binding one run's feedback argument to another's ``scratchpad_alias``
    makes what the first drains there the second's per-call values. The run
    is made on ``image``'s kernels as the shared runtime loaded them; once the
    runtime evicts the image, loading it again gives others, and the run has
    ended.
    """

    def __init__(
        self,
        name: str,
        image: NPUKernel,
        kernels: list[pyxrt.kernel],
        runs: list[pyxrt.run],
        arguments: Mapping[int, XRTTensor],
        feedback_arg: int | None,
        params_path: Path | None,
    ):
        self.name = name
        self._image = image
        self._kernel = kernels[0]
        self.handles = runs
        for index, tensor in arguments.items():
            self.bind(index, tensor.buffer_object())
        self._feedback_arg = feedback_arg
        self._params_path = params_path
        self._params: list[ParameterBlock] | None = None
        # Bound to or from another run's scratchpad: a loop holds it.
        self.wired = False

    def bind(self, index: int, bo: pyxrt.bo | None) -> None:
        """Run with ``bo`` as argument ``index``.

        Raises:
            ValueError: ``bo`` is None, as a released tensor's is.
        """
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
    def params(self) -> list[ParameterBlock] | None:
        """Each command's parameter scratchpad; ``None`` when ``params.txt``
        counts none.
        """
        if self._params is not None:
            return self._params
        if self._params_path is None:
            return None
        if self._params_path.read_text().split("\n", 1)[0].strip() == "0":
            return None
        self._params = [ParameterBlock(h, self._params_path) for h in self.handles]
        return self._params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        params = self.params
        if params is None:
            raise ValueError(
                f"{self.name} was built without per-call values; got "
                f"{sorted(values)}"
            )
        for block in params:
            for symbol, value in values.items():
                block.write(symbol, value)
            block.sync()

    def read_value(self, symbol: str) -> int:
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} was built without per-call values")
        params[0].sync_from_device()
        return params[0].read(symbol)

    def scratchpad_alias(self) -> pyxrt.bo:
        """This run's ctrl scratchpad, for another run to drain its feedback into.

        Raises:
            ValueError: The run has no per-call values, or is several
                commands, whose scratchpads one drain cannot all set.
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

    def start(self) -> None:
        if aie_utils.DefaultNPURuntime.load(self._image).kernel is not self._kernel:
            raise RuntimeError(
                f"{self.name}: the runtime evicted the image this run was made on"
            )
        for handle in self.handles:
            handle.start()

    def wait(self) -> None:
        for handle in self.handles:
            # run.wait() returns the ert_cmd_state; run.wait2() returns None.
            state = handle.wait()
            if state != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
                raise RuntimeError(f"{self.name}: the run ended in {state}")


class FullELFCallable:
    """The full ELF (NPU2): every operator shares consolidated buffers addressed by offset.

    A call dispatches ``run``; ``new_run`` makes more over the same buffers.

    Each run holds a copy of the ELF's control code in the driver's device
    heap, which a process fills at about 512 MiB. A run that does not fit
    releases the run of the callable least recently called, as long as no
    loop holds that run, and unloads its image: the image's hw_context holds
    some of the heap too, between runs, and while it lives the freed run is
    a hole a larger one may not fit in. The next call of that callable loads
    the image and makes a new run.
    """

    # The callables holding a run, least recently called first.
    _holding: weakref.WeakValueDictionary[int, FullELFCallable] = (
        weakref.WeakValueDictionary()
    )

    def __init__(
        self,
        seq,
        device_name="main",
        sequence_name="sequence",
        arena: ScratchArena | None = None,
    ):
        _require_xrt()
        if (arena is None) != (seq.arena is None):
            raise ValueError(
                f"{seq.name} was placed in "
                + ("an arena plan" if seq.arena is not None else "no arena plan")
                + (", but no arena was given" if arena is None else ", but got one")
            )
        if arena is not None and arena.plan is not seq.arena:
            raise ValueError(f"{seq.name} was placed in another arena plan")
        self.op = seq
        self.arena = arena
        self.device_name = device_name
        self.sequence_name = sequence_name
        self.last_elapsed = 0.0
        self.kernel = NPUKernel(
            elf_path=str(seq.image), kernel_name=f"{device_name}:{sequence_name}"
        )
        # Each later command's runtime sequence, on the same hw_context.
        self.later = [
            NPUKernel(
                elf_path=str(seq.image),
                kernel_name=f"{device_name}:{Fusion.sequence_name(k)}",
            )
            for k in range(1, len(seq.commands) + 1)
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
                self.lowered_mlir_path.read_text(), f"{device_name}:{sequence_name}"
            )
            if layout:
                self._trace_arg = layout["arg_index"]
                self.trace_buffer = XRTTensor((layout["size"],), dtype=np.int8)

    @property
    def handle(self) -> XRTKernelHandle:
        """The ELF as the shared runtime holds it: loaded again, ending every
        run, where the runtime evicted it.
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

    def release(self) -> bool:
        """Free the run a call dispatches and unload the image, unless a loop
        holds the run, another run is out, or another callable runs the image.

        Returns:
            Whether it was freed.
        """
        if self._run is None or self._run.wired or self._runs != [self._run]:
            return False
        image = self.kernel.elf_path
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
            arguments,
            self._argument_index.get("feedback"),
            self.op.artifacts.params,
        )
        self._runs.append(made)
        return made

    @property
    def params(self) -> ParameterBlock | None:
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
        """The bytes ``ref`` names, as its dtype."""
        self._follow_arena()
        if ref not in self._buffer_cache:
            kind, offset, length = ref.place(self.op.layout)
            if kind == "scratch":
                kind, offset = self.op.buffer_sizes.scratch_argument(offset, length)
            dtype = self.op.buffer_dtype(ref)
            self._buffer_cache[ref] = self._arguments()[kind].subview(
                offset, (length // dtype.itemsize,), dtype
            )
        return self._buffer_cache[ref]

    def get_storage(self, root: str):
        """The buffer and the rest of its last coherence line, which no other buffer holds.

        An exact view of a buffer that does not end on a line cannot be synchronized.
        """
        self._follow_arena()
        if root not in self._storage_cache:
            kind, offset, length = self.op.layout[root]
            if kind == "scratch":
                kind, offset = self.op.buffer_sizes.scratch_argument(offset, length)
            dtype = self.op.buffer_dtype(BufferRef(root))
            parent = self._arguments()[kind]
            stop = min(Pool(ALIGNMENT).align(offset + length), parent.nbytes)
            self._storage_cache[root] = parent.subview(
                offset, ((stop - offset) // dtype.itemsize,), dtype
            )
        return self._storage_cache[root]

    def _follow_arena(self) -> None:
        if self.arena is None or self.arena.generation == self._arena_generation:
            return
        self.scratch_banks = self.arena.banks
        self._arena_generation = self.arena.generation
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

    def start(self, *runs: FullELFRun) -> None:
        """Push what the host wrote, and start ``runs`` without waiting."""
        self._sync_inputs()
        for run in runs:
            run.start()

    def wait(self, *runs: FullELFRun) -> None:
        """Wait on ``runs``.

        Raises:
            RuntimeError: The host wrote an argument since it was pushed,
                which no run read and the next push would lay over what
                the runs wrote.
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

    def __call__(self, *runs: FullELFRun):
        """Dispatch ``run``, or ``runs`` queued back to back."""
        runs = runs or (self.run,)
        self._sync_inputs()
        t0 = time.perf_counter()
        for run in runs:
            run.start()
        for run in runs:
            run.wait()
        self.last_elapsed = time.perf_counter() - t0


class StepCallable:
    """Runs an ``XclbinChain`` one step at a time, its buffers shared by name.

    ``check`` holds each dispatched step to its reference on the NPU's
    inputs, by the step's ``tolerance()`` (``check_step``), so each
    comparison isolates one operator. The residents a sequence placed in an
    arena plan are views of ``arena``'s buffer, so every version of a graph
    reads one copy.
    """

    def __init__(self, seq, check: bool = False, arena: ScratchArena | None = None):
        _require_xrt()
        self.op = seq
        self.check = check
        self.last_elapsed = 0.0
        self.dispatch_values: dict[str, np.generic] = {}
        self.arena = arena
        self._arena_generation: int | None = None
        self._buffers: dict[BufferRef, XRTTensor] = {}
        self._storage: dict[str, XRTTensor] = {}
        for root, (_, _, length) in seq.layout.items():
            if self.arena is not None and root in seq.residents:
                continue
            ref = BufferRef(root)
            dtype = seq.buffer_dtype(ref)
            self._storage[root] = XRTTensor((_n_elements(length, dtype),), dtype=dtype)
            self._buffers[ref] = self._storage[root]
        self._steps = [(s.op, seq.kernel(s.op), s.buffers, []) for s in seq.steps]
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
        if self.arena is None or self.arena.generation == self._arena_generation:
            return
        banks = self.arena.banks
        self._arena_generation = self.arena.generation
        for root in self.op.residents:
            _, offset, length = self.op.layout[root]
            bank, offset = divmod(offset, BANK)
            parent = banks[bank]
            dtype = self.op.buffer_dtype(BufferRef(root))
            stop = min(Pool(ALIGNMENT).align(offset + length), parent.nbytes)
            # A step takes the storage: an exact view of a resident whose
            # bytes are not whole coherence lines cannot be made.
            self._storage[root] = parent.subview(
                offset, ((stop - offset) // dtype.itemsize,), dtype
            )
        self._buffers = {
            ref: view
            for ref, view in self._buffers.items()
            if ref.root not in self.op.residents
        }
        self._bind_steps()

    def get_buffer(self, ref: BufferRef):
        """The bytes ``ref`` names, as its dtype."""
        self._follow_arena()
        if ref not in self._buffers:
            if ref.root not in self._storage:
                raise ValueError(f"{ref} is no buffer of {self.op.name}")
            _, _, length = ref.place(self.op.layout)
            dtype = self.op.buffer_dtype(ref)
            self._buffers[ref] = self._storage[ref.root].subview(
                ref.start, (length // dtype.itemsize,), dtype
            )
        return self._buffers[ref]

    def get_storage(self, root: str):
        """The buffer, and for a resident in the arena the rest of its last
        coherence line, which no other buffer holds.
        """
        self._follow_arena()
        return self._storage[root]

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        self.dispatch_values = dict(values)

    def __call__(self):
        self._follow_arena()
        for root in self.op.inputs:
            self._storage[root].to("npu")
        t0 = time.perf_counter()
        for index, (step_op, kernel, refs, args) in enumerate(self._steps):
            # A placed buffer starts at its place in the tensor that holds it.
            at = {}
            for spec in step_op.buffers:
                at[spec.name] = spec.placement[1]
                if f"{spec.name}_offset" in step_op.bound_values:
                    word = step_op.value(f"{spec.name}_offset")
                    at[spec.name] += int(self.dispatch_values[word.symbol])
            checked = self.check and not step_op.bound_extents
            if self.check and not checked:
                logger.warning(
                    "[check step %d] %s not checked: %s bounded per call",
                    index,
                    type(step_op).__name__,
                    sorted(step_op.bound_extents),
                )
            if checked:
                inputs, expected = self._reference(step_op, args, at)
            kernel(
                *args,
                **{name: self.dispatch_values[name] for name in kernel.dispatch_params},
            )
            if checked:
                written = {
                    spec.name: buf.numpy()[at[spec.name] :][: spec.elements]
                    for buf, spec in zip(args, step_op.buffers)
                    if spec.drains
                }
                held = dict(zip((spec.name for spec in step_op.buffers), refs))
                check_step(index, step_op, held, inputs, written, expected)
        self.last_elapsed = time.perf_counter() - t0
        # Device-resident, so a read pulls what the steps wrote, and only then.
        for root in self.op.layout:
            if root not in self.op.inputs:
                self._storage[root].device = "npu"

    def _reference(
        self, step_op: Operator, args, at: Mapping[str, int]
    ) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray]]:
        """``step_op``'s inputs as its buffers hold them, each from element
        ``at`` its name, and its reference on them, by buffer name.
        """
        held = {
            spec.name: buf.numpy()[at[spec.name] :][: spec.elements]
            .reshape(spec.shape)
            .copy()
            for buf, spec in zip(args, step_op.buffers)
        }
        inputs = {b.name: held[b.name] for b in step_op.inputs}
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
    """Hold what step ``index`` wrote to its reference on the same inputs,
    by the step's ``tolerance()``.

    Args:
        held: Each of the step's buffers, by its declared name, as the
            sequence names it.
        inputs: The step's inputs as its buffers held them, by declared name.
        written: Each output the step wrote, by declared name.
        expected: Its reference on ``inputs``, by declared name.

    Raises:
        ValueError: Nothing bounds the step's output.
        RuntimeError: An output is outside the step's tolerance.
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
