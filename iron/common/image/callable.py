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
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from aie.utils.npukernel import NPUKernel
from aie.utils.trace import get_trace_buffer
from aie.utils.verify import Tolerance

from ..declare import Operator
from ..design import device_symbol
from .allocator import ALIGNMENT, ArenaPlan, Pool

if TYPE_CHECKING:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.hostruntime import XRTKernelHandle
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

    from .xrt import Scratchpad, loaded, unload
else:
    try:
        import pyxrt
        from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

        from .xrt import Scratchpad, loaded, unload
    except ImportError:
        # Host stacks without XRT still compile and run the reference mode.
        XRTTensor = None

logger = logging.getLogger(__name__)

BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes, dtype=BF16):
    itemsize = np.dtype(dtype).itemsize
    return max(nbytes, itemsize) // itemsize


def _require_xrt() -> None:
    if XRTTensor is None:
        raise RuntimeError(
            "this OperatorSequence mode needs the XRT host runtime (pyxrt), which is "
            "not installed. Use the reference mode, or run a single operator, which "
            "dispatches through aie.utils.DefaultNPURuntime and works on any backend."
        )


class ScratchArena:
    """The device buffer behind an ``ArenaPlan``, shared by every full ELF placed in it.

    A plan that grew since first use grows the buffer, keeping its contents;
    each callable rebinds on its next call (``generation``).
    """

    def __init__(self, plan: ArenaPlan):
        self.plan = plan
        self._tensor: XRTTensor | None = None
        self._generation = 0
        self.loaded: set = set()

    @property
    def generation(self) -> int:
        return self._generation

    @property
    def tensor(self) -> XRTTensor:
        _require_xrt()
        n = _n_elements(self.plan.size)
        if self._tensor is not None and self._tensor.shape[0] >= n:
            return self._tensor
        grown = XRTTensor((n,), dtype=ml_dtypes.bfloat16)
        if self._tensor is not None:
            old = self._tensor.numpy()  # pulls what the device wrote
            grown.numpy_view()[: old.size] = old
            logger.info(
                "scratch arena grew from %d to %d bytes", old.nbytes, grown.nbytes
            )
        self._tensor = grown
        self._generation += 1
        return grown

    def view(self, offset: int, nbytes: int, dtype=BF16) -> XRTTensor:
        dtype = np.dtype(dtype)
        return self.tensor.subview(offset, (nbytes // dtype.itemsize,), dtype)


class FullELFRun:
    """One run of a full ELF, with its own ctrl scratchpad of per-call values.

    Binding one run's feedback argument to another's ``scratchpad_alias``
    makes what the first drains there the second's per-call values.
    """

    def __init__(
        self,
        name: str,
        handle: XRTKernelHandle,
        run: pyxrt.run,
        arguments: Mapping[int, XRTTensor],
        feedback_arg: int | None,
        params_path: Path | None,
    ):
        self.name = name
        self._handle = handle
        self.handle = run
        for index, tensor in arguments.items():
            self.bind(index, tensor.buffer_object())
        self._feedback_arg = feedback_arg
        self._params_path = params_path
        self._params: Scratchpad | None = None
        # Bound to or from another run's scratchpad: a loop holds it.
        self.wired = False

    def bind(self, index: int, bo: pyxrt.bo | None) -> None:
        """Run with ``bo`` as argument ``index``.

        Raises:
            ValueError: ``bo`` is None, as a released tensor's is.
        """
        if bo is None:
            raise ValueError(f"{self.name}: argument {index} has no buffer object")
        self.handle.set_arg(index, bo)

    def bind_feedback(self, bo: pyxrt.bo) -> None:
        if self._feedback_arg is None:
            raise ValueError(f"{self.name} declares no feedback argument")
        self.bind(self._feedback_arg, bo)
        self.wired = True

    @property
    def params(self) -> Scratchpad | None:
        """The run's parameter scratchpad; ``None`` when ``params.txt`` counts none."""
        if self._params is not None:
            return self._params
        if self._params_path is None:
            return None
        if self._params_path.read_text().split("\n", 1)[0].strip() == "0":
            return None
        self._params = Scratchpad(self.handle, self._params_path)
        return self._params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        params = self.params
        if params is None:
            raise ValueError(
                f"{self.name} was built without per-call values; got "
                f"{sorted(values)}"
            )
        for symbol, value in values.items():
            params.write(symbol, value)
        params.sync()

    def read_value(self, symbol: str) -> int:
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} was built without per-call values")
        params.sync_from_device()
        return params.read(symbol)

    def scratchpad_alias(self) -> pyxrt.bo:
        """This run's ctrl scratchpad, for another run to drain its feedback into."""
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} has no per-call values to feed back into")
        self.wired = True
        return params.alias()

    def start(self) -> None:
        if not loaded(self._handle):
            raise RuntimeError(
                f"{self.name}: the runtime evicted the image this run was made on"
            )
        self.handle.start()

    def wait(self) -> None:
        # run.wait() returns the ert_cmd_state; run.wait2() returns None.
        state = self.handle.wait()
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
        self._handle = None
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
            self.scratch_buffer = XRTTensor((_n_elements(sizes.scratch),), dtype=BF16)
        else:
            self.scratch_buffer = arena.tensor
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
        """The ELF in the shared runtime, reloaded (ending every run) if evicted."""
        if self._handle is None or not loaded(self._handle):
            self._handle = aie_utils.DefaultNPURuntime.load(self.kernel)
            self._run = None
            self._runs = []
        return self._handle

    @property
    def run(self) -> FullELFRun:
        """The run a call dispatches, one for the image's life."""
        if self._run is None or not loaded(self._handle):
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
        self._handle = None
        FullELFCallable._holding.pop(id(self), None)
        unload(image)
        return True

    def _make_run(self) -> FullELFRun:
        handle = self.handle
        while True:
            try:
                run = pyxrt.run(handle.kernel)
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
            index: self._arguments()[kind]
            for kind, index in self._argument_index.items()
        }
        if self.trace_buffer is not None:
            assert self._trace_arg is not None
            arguments[self._trace_arg] = self.trace_buffer
        made = FullELFRun(
            self.op.name,
            self.handle,
            run,
            arguments,
            self._argument_index.get("feedback"),
            self.op.artifacts.params,
        )
        self._runs.append(made)
        return made

    @property
    def params(self) -> Scratchpad | None:
        return self.run.params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        self.run.write_values(values)

    def _arguments(self) -> dict[str, XRTTensor]:
        buffers = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "scratch": self.scratch_buffer,
            "feedback": self.feedback_buffer,
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

    def get_buffer(self, buffer_name):
        self._follow_arena()
        if buffer_name not in self._buffer_cache:
            buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
            dtype = self.op.buffer_dtype(buffer_name)
            self._buffer_cache[buffer_name] = self._arguments()[buf_type].subview(
                offset, (length // dtype.itemsize,), dtype
            )
        return self._buffer_cache[buffer_name]

    def get_storage(self, buffer_name):
        """The buffer and the rest of its last coherence line, which no other buffer holds.

        An exact view of a buffer that does not end on a line cannot be synchronized.
        """
        self._follow_arena()
        if buffer_name in self.op.slice_info:
            raise ValueError(f"{buffer_name} is a slice; its parent has the storage")
        if buffer_name not in self._storage_cache:
            buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
            dtype = self.op.buffer_dtype(buffer_name)
            parent = self._arguments()[buf_type]
            stop = min(Pool(ALIGNMENT).align(offset + length), parent.nbytes)
            self._storage_cache[buffer_name] = parent.subview(
                offset, ((stop - offset) // dtype.itemsize,), dtype
            )
        return self._storage_cache[buffer_name]

    def _follow_arena(self) -> None:
        if self.arena is None or self.arena.generation == self._arena_generation:
            return
        self.scratch_buffer = self.arena.tensor
        self._arena_generation = self.arena.generation
        for run in self._runs:
            run.bind(
                self._argument_index["scratch"], self.scratch_buffer.buffer_object()
            )
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
    """Runs a sequence one step at a time, its buffers shared by name: an
    ``XclbinChain``'s dispatches, or with no image each ``reference()``.

    ``compare`` holds each dispatched step to its reference on the NPU's
    inputs, so each comparison isolates one operator; ``tolerance``, when
    set, replaces each step's own. On the NPU, the residents a sequence
    placed in an arena plan are views of ``arena``'s buffer, so every
    version of a graph reads one copy.
    """

    # compare cannot judge a range-relative tolerance element by element.
    FALLBACK_TOLERANCE = Tolerance.relative(0.025, 1e-2)

    def __init__(self, seq, compare: bool = False, arena: ScratchArena | None = None):
        chain = seq._image
        if chain is not None:
            _require_xrt()
        self.op = seq
        self.compare = compare
        self.tolerance: Tolerance | None = None
        self.last_elapsed = 0.0
        self.dispatch_values: dict[str, np.generic] = {}
        self._on_npu = chain is not None
        self.arena = arena if self._on_npu else None
        self._arena_generation: int | None = None
        tensor = XRTTensor if self._on_npu else CPUOnlyTensor
        self._buffers = {}
        self._storage = {}
        for name, (_, _, length) in seq.subbuffer_layout.items():
            if self.arena is not None and name in seq.residents:
                continue
            dtype = seq.buffer_dtype(name)
            self._buffers[name] = tensor((_n_elements(length, dtype),), dtype=dtype)
        self._steps = []
        self._follow_arena()
        kernels = {}
        if chain is not None:
            kernels = {
                op_id: NPUKernel(
                    chain.image,
                    design.get_cache_entry().insts,
                    kernel_name=chain.labels[op_id],
                    dispatch_params=design.dispatch_params,
                    dispatch_lib_path=design.get_dispatch_lib_path(),
                )
                for op_id, design in chain.designs.items()
            }
        for step_op, *names in seq.runlist:
            if len(step_op.buffers) != len(names):
                raise ValueError(
                    f"Operator {step_op!r} declares {len(step_op.buffers)} buffers "
                    f"but the runlist names {len(names)}"
                )
            args = [self.get_buffer(name) for name in names]
            kernel = kernels[id(step_op)] if self._on_npu else None
            self._steps.append((step_op, kernel, names, args))

    def _follow_arena(self) -> None:
        """View the residents in the arena's buffer, again once it has grown."""
        if self.arena is None or self.arena.generation == self._arena_generation:
            return
        parent = self.arena.tensor
        self._arena_generation = self.arena.generation
        for name in self.op.residents:
            _, offset, length = self.op.subbuffer_layout[name]
            dtype = self.op.buffer_dtype(name)
            stop = min(Pool(ALIGNMENT).align(offset + length), parent.nbytes)
            self._buffers[name] = parent.subview(
                offset, (length // dtype.itemsize,), dtype
            )
            self._storage[name] = parent.subview(
                offset, ((stop - offset) // dtype.itemsize,), dtype
            )
        for name, (base_name, _, _) in self.op.slice_info.items():
            if base_name in self.op.residents:
                self._buffers.pop(name, None)
        self._steps = [
            (step_op, kernel, names, [self.get_buffer(name) for name in names])
            for step_op, kernel, names, _ in self._steps
        ]

    def get_buffer(self, buffer_name):
        self._follow_arena()
        if buffer_name not in self._buffers:
            if buffer_name not in self.op.slice_info:
                raise ValueError(f"Unknown buffer '{buffer_name}' in the runlist")
            base_name, start, end = self.op.slice_info[buffer_name]
            dtype = self.op.buffer_dtype(buffer_name)
            self._buffers[buffer_name] = self._buffers[base_name].subview(
                start, ((end - start) // dtype.itemsize,), dtype
            )
        return self._buffers[buffer_name]

    def get_storage(self, buffer_name):
        """The buffer, and for a resident in the arena the rest of its last
        coherence line, which no other buffer holds.
        """
        self._follow_arena()
        if buffer_name in self._storage:
            return self._storage[buffer_name]
        return self.get_buffer(buffer_name)

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        if not self._on_npu:
            raise NotImplementedError("the reference mode takes no per-call values")
        self.dispatch_values = dict(values)

    def __call__(self):
        self._follow_arena()
        if self._on_npu:
            for name in self.op.input_args:
                self._buffers[name].to("npu")
        t0 = time.perf_counter()
        for index, (step_op, kernel, names, args) in enumerate(self._steps):
            # A placed buffer starts at its place in the tensor that holds it.
            at = {}
            for spec in step_op.buffers:
                at[spec.name] = spec.placement[1]
                if f"{spec.name}_offset" in step_op.bound_values:
                    word = step_op.value(f"{spec.name}_offset")
                    at[spec.name] += int(
                        self.dispatch_values[device_symbol(step_op, word)]
                    )
            checked = self.compare and not step_op.bound_extents
            if self.compare and not checked:
                logger.warning(
                    "[compare step %d] %s not compared: %s bounded per call",
                    index,
                    type(step_op).__name__,
                    sorted(step_op.bound_extents),
                )
            if kernel is None or checked:
                inputs, expected = self._reference(step_op, args, at)
            if kernel is None:
                for buf, spec in zip(args, step_op.buffers):
                    if spec.direction.drains:
                        out = buf.numpy_view()[at[spec.name] :]
                        result = expected[spec.name].reshape(-1)
                        out[: spec.elements] = result.astype(out.dtype)
                continue
            kernel(
                *args,
                **{name: self.dispatch_values[name] for name in kernel.dispatch_params},
            )
            if checked:
                self._check(index, step_op, names, args, at, inputs, expected)
        self.last_elapsed = time.perf_counter() - t0
        if self._on_npu:
            # Device-resident, so a read pulls what the steps wrote, and only then.
            for name in self.op.subbuffer_layout:
                if name not in self.op.input_args:
                    self.get_storage(name).device = "npu"

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
        outputs = {
            b.name: held[b.name] for b in step_op.outputs if not b.direction.fills
        }
        symbols = {v.name: device_symbol(step_op, v) for v in step_op.values}
        values = {
            name: self.dispatch_values[symbol]
            for name, symbol in symbols.items()
            if symbol in self.dispatch_values
        }
        expected = step_op.call_reference(inputs, outputs, values)
        return inputs, {
            b.name: np.asarray(expected[b.name]).reshape(b.shape)
            for b in step_op.outputs
        }

    def _check(
        self, index, step_op: Operator, names, args, at, inputs, expected
    ) -> None:
        """Hold step ``index``'s NPU outputs, each from element ``at`` its
        name, to its reference on the same inputs.

        Raises:
            RuntimeError: An output is outside the step's tolerance.
        """
        tol = self.tolerance
        if tol is None:
            tol = step_op.resolved().tolerance()
            if tol is None or tol.range_frac is not None:
                tol = self.FALLBACK_TOLERANCE
        held = {spec.name: name for name, spec in zip(names, step_op.buffers)}
        written = {
            spec.name: buf.numpy()[at[spec.name] :][: spec.elements]
            for buf, spec in zip(args, step_op.buffers)
            if spec.direction.drains
        }
        for name, verdict in step_op.judge(inputs, written, tol, expected).items():
            logger.info(
                "[compare step %d] %s -> %s: max_abs=%.4g",
                index,
                type(step_op).__name__,
                held[name],
                verdict.max_abs_err,
            )
            if not verdict:
                raise RuntimeError(
                    f"[compare step {index}] {type(step_op).__name__} "
                    f"(name={step_op.name}) -> {held[name]}: NPU output deviates "
                    f"from reference ({verdict.detail}; "
                    f"inputs={[held[b.name] for b in step_op.inputs]}; "
                    f"tolerance {tol})"
                )
