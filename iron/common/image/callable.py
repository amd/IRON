# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a caller invokes once a sequence has an image: one class per image kind."""

from __future__ import annotations

import logging
import time
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING

import aie.utils as aie_utils
import ml_dtypes
import numpy as np
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from aie.utils.npukernel import NPUKernel
from aie.utils.trace import get_trace_buffer
from aie.utils.verify import Tolerance, compare

from ..declare import Operator
from .allocator import ALIGNMENT, ArenaPlan, Pool

if TYPE_CHECKING:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.hostruntime import XRTKernelHandle
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

    from .xrt import Scratchpad, loaded
else:
    try:
        import pyxrt
        from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

        from .xrt import Scratchpad, loaded
    except ImportError:
        # Host stacks without XRT (e.g. the HRX/amdxdna runtime). The on-device
        # callables here take XRTTensor views, so they cannot run there;
        # _require_xrt() makes that explicit at construction. The reference
        # mode and the whole compile path do not care, and must keep importing.
        XRTTensor = None

logger = logging.getLogger(__name__)

BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes, dtype=BF16):
    itemsize = np.dtype(dtype).itemsize
    return max(nbytes, itemsize) // itemsize


def _require_xrt() -> None:
    """Fail with the reason, rather than a TypeError on calling ``None``."""
    if XRTTensor is None:
        raise RuntimeError(
            "this OperatorSequence mode needs the XRT host runtime (pyxrt), which is "
            "not installed. Use the reference mode, or run a single operator, which "
            "dispatches through aie.utils.DefaultNPURuntime and works on any backend."
        )


class ScratchArena:
    """The device buffer behind an ``ArenaPlan``: one scratch buffer every
    full ELF placed in the plan runs against.

    Made on first use, at the plan's size then. A plan that has grown since
    -- an image placed after the first dispatch -- grows the buffer on the
    next use, keeping its contents, so resident weights and states survive.
    Views taken before a growth are views of the old buffer; each callable
    rebinds on its next call (see ``generation``).
    """

    def __init__(self, plan: ArenaPlan):
        self.plan = plan
        self._tensor: XRTTensor | None = None
        self._generation = 0
        # Residents whose contents are in the buffer, by storage key.
        self.loaded: set = set()

    @property
    def generation(self) -> int:
        """Bumped whenever ``tensor`` is replaced by a larger buffer."""
        return self._generation

    @property
    def tensor(self) -> XRTTensor:
        """The buffer, at least as large as the plan now is."""
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
        """``nbytes`` of the buffer from ``offset``, as ``dtype``."""
        dtype = np.dtype(dtype)
        return self.tensor.subview(offset, (nbytes // dtype.itemsize,), dtype)


class SequenceCallable:
    """Runs an ``OperatorSequence`` once per call.

    Buffers are one per name, a slice a view into its parent; inputs sync to
    the device before the run and everything else back to the host after.
    Subclasses give the buffer (``_make_buffer``) and the run (``_run``); the
    full-ELF callable replaces the buffer model with its consolidated
    arguments, and the run with run handles of its own.
    """

    def __init__(self, seq):
        self.op = seq
        self.last_elapsed = 0.0
        self._buffer_cache = {}
        self._allocate_buffers()

    def _make_buffer(self, n_elements, dtype):
        return XRTTensor((n_elements,), dtype=dtype)

    def _allocate_buffers(self):
        self._buffers = {}
        for name, (_, _, length) in self.op.subbuffer_layout.items():
            dtype = self.op.buffer_dtype(name)
            self._buffers[name] = self._make_buffer(_n_elements(length, dtype), dtype)

    def _resolve_buffer(self, buf_name):
        if buf_name in self._buffers:
            return self._buffers[buf_name]
        if buf_name in self.op.slice_info:
            base_name, start_bytes, end_bytes = self.op.slice_info[buf_name]
            size_bytes = end_bytes - start_bytes
            dtype = self.op.buffer_dtype(buf_name)
            sub = self._buffers[base_name].subview(
                start_bytes, (size_bytes // dtype.itemsize,), dtype
            )
            self._buffers[buf_name] = sub
            return sub
        raise ValueError(f"Unknown buffer '{buf_name}' in fused runlist")

    def get_buffer(self, buffer_name):
        if buffer_name not in self._buffer_cache:
            self._buffer_cache[buffer_name] = self._resolve_buffer(buffer_name)
        return self._buffer_cache[buffer_name]

    def get_storage(self, buffer_name):
        """A flat view the host can synchronize that starts with the buffer:
        here each buffer is a tensor of its own, so the buffer itself.
        """
        return self.get_buffer(buffer_name)

    def _iter_steps(self):
        """Yield ``(op, in_names, in_buffers, out_name, out_buffer)`` per runlist step."""
        for step_op, *buf_names in self.op.runlist:
            specs = step_op.buffers
            if len(specs) != len(buf_names):
                raise ValueError(
                    f"Operator {step_op!r} declares {len(specs)} buffers but the "
                    f"runlist names {len(buf_names)}"
                )
            *in_names, out_name = buf_names
            *in_specs, out_spec = specs
            yield step_op, in_names, in_specs, out_name, out_spec

    def _sync_inputs(self):
        for name in self.op.input_args:
            self._buffers[name].to("npu")

    def _sync_outputs(self):
        for name in self.op.subbuffer_layout:
            if name not in self.op.input_args:
                self._buffers[name].to("cpu")

    def _run(self):
        raise NotImplementedError

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        """Set the per-call values, by device symbol, for the next run."""
        raise NotImplementedError(f"{type(self).__name__} takes no per-call values")

    def __call__(self):
        self._sync_inputs()
        t0 = time.perf_counter()
        self._run()
        self.last_elapsed = time.perf_counter() - t0
        self._sync_outputs()


class FullELFRun:
    """One run of a full ELF: the buffers bound to its arguments, and its own
    ctrl scratchpad.

    Runs of one image are separate dispatches: each has its own scratchpad,
    so its own per-call values, and several can be started before any is
    waited on. Binding one run's feedback argument to another's scratchpad
    (``bind_feedback``, ``scratchpad_alias``) makes what the first
    drains there the second's per-call values, with no host step between.
    A run is valid while the image stays loaded; the runtime evicting it
    ends every run made on it.
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

    def bind(self, index: int, bo: pyxrt.bo | None) -> None:
        """Run with ``bo`` as argument ``index``.

        Raises:
            ValueError: ``bo`` is None, as a released tensor's is.
        """
        if bo is None:
            raise ValueError(f"{self.name}: argument {index} has no buffer object")
        self.handle.set_arg(index, bo)

    def bind_feedback(self, bo: pyxrt.bo) -> None:
        """Run with ``bo`` as the feedback argument -- the callable's own
        buffer until then. Typically another run's ``scratchpad_alias``.
        """
        if self._feedback_arg is None:
            raise ValueError(f"{self.name} declares no feedback argument")
        self.bind(self._feedback_arg, bo)

    @property
    def params(self) -> Scratchpad | None:
        """The run's parameter scratchpad, made on first use.

        The ``params.txt`` describing the runtime parameters is requested
        from aiecc via ``--get-scratchpad-parameters`` and lands in the
        build's cache entry, which ``Artifacts.params`` names. Returns
        ``None`` if the sequence declared no runtime parameters: the file
        still exists, but holds a count of zero and there is no ctrl
        scratchpad buffer object to bind to.
        """
        if self._params is not None:
            return self._params
        if self._params_path is None:
            return None
        if self._params_path.read_text().split("\n", 1)[0].strip() == "0":
            return None
        self._params = Scratchpad(self.handle, self._params_path)
        return self._params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        """Write each value into the ctrl scratchpad and sync it."""
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
        """The value ``symbol`` holds in the scratchpad now, as the device
        left it (a feedback transfer into ``scratchpad_alias``).
        """
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} was built without per-call values")
        params.sync_from_device()
        return params.read(symbol)

    def scratchpad_alias(self) -> pyxrt.bo:
        """A buffer object over this run's ctrl scratchpad, for another run to
        drain its feedback into (``Scratchpad.alias``). The host
        must not write this run's values while a device writes them.
        """
        params = self.params
        if params is None:
            raise ValueError(f"{self.name} has no per-call values to feed back into")
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


class SequenceFullELFCallable(SequenceCallable):
    """The full ELF (NPU2): every operator shares consolidated
    input/output/scratch buffers (and a feedback one, if the sequence declares
    feedback arguments) addressed by offset. ``get_buffer`` returns a sub-view
    of the named argument's dtype into whichever consolidated buffer holds it.

    A sequence placed in a shared arena (``OperatorSequence(arena=...)``) runs
    its scratch in the ``arena`` buffer given here, which every other image
    placed in the same plan runs in too; otherwise it allocates its own.

    A call dispatches ``run``; ``new_run`` makes more, over the same
    buffers, for callers that queue several or chain them through feedback
    (see ``FullELFRun``).
    """

    # The buffer trace lowering appends, and the kernel argument it binds to;
    # both None on an untraced build.
    trace_buffer: XRTTensor | None
    _trace_arg: int | None
    # The callable's own feedback buffer; None without feedback arguments.
    feedback_buffer: XRTTensor | None

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
        self.arena = arena
        self.device_name = device_name
        self.sequence_name = sequence_name
        self.kernel = NPUKernel(
            elf_path=str(seq.image), kernel_name=f"{device_name}:{sequence_name}"
        )
        self._handle = None
        self._run: FullELFRun | None = None
        self._runs: list[FullELFRun] = []
        self._storage_cache = {}
        # Argument index by kind: the order ArgumentSizes gives them in.
        self._argument_index = {
            kind: index for index, kind in enumerate(seq.buffer_sizes.arguments())
        }
        super().__init__(seq)

    @property
    def handle(self) -> XRTKernelHandle:
        """The ELF loaded in the shared runtime; loaded again if the runtime
        has evicted it since, which ends every run made on it.
        """
        if self._handle is None or not loaded(self._handle):
            self._handle = aie_utils.DefaultNPURuntime.load(self.kernel)
            self._run = None
            self._runs = []
        return self._handle

    @property
    def run(self) -> FullELFRun:
        """The run a call dispatches: one for the image's life, so what is
        written to its scratchpad stays there from call to call.
        """
        handle = self.handle
        if self._run is None:
            self._run = self._make_run(pyxrt.run(handle.kernel))
        return self._run

    def new_run(self) -> FullELFRun:
        """Another run of this image, bound to this callable's buffers."""
        return self._make_run(pyxrt.run(self.handle.kernel))

    def _make_run(self, run: pyxrt.run) -> FullELFRun:
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
        """``run``'s per-call values (``FullELFRun.params``)."""
        return self.run.params

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        """Write each value into ``run``'s ctrl scratchpad and sync it."""
        self.run.write_values(values)

    def _allocate_buffers(self):
        sizes = self.op.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(sizes.input),), dtype=BF16)
        self.output_buffer = XRTTensor((_n_elements(sizes.output),), dtype=BF16)
        if self.arena is None:
            self.scratch_buffer = XRTTensor((_n_elements(sizes.scratch),), dtype=BF16)
        else:
            self.scratch_buffer = self.arena.tensor
            self._arena_generation = self.arena.generation
        self.feedback_buffer = None
        if sizes.feedback is not None:
            self.feedback_buffer = XRTTensor((sizes.feedback,), dtype=np.uint8)
        # Trace lowering appends one buffer covering every configured design, after
        # the consolidated ones. Its argument and size depend on how many channels
        # and sub-designs claim a share, so read them from the lowered module.
        self.trace_buffer = None
        self._trace_arg = None
        if self.op.traced:
            layout = get_trace_buffer(
                self.lowered_mlir_path.read_text(),
                f"{self.device_name}:{self.sequence_name}",
            )
            if layout:
                self._trace_arg = layout["arg_index"]
                self.trace_buffer = XRTTensor((layout["size"],), dtype=np.int8)

    def _arguments(self) -> dict[str, XRTTensor]:
        """The consolidated buffer of each kind the image takes."""
        buffers = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "scratch": self.scratch_buffer,
            "feedback": self.feedback_buffer,
        }
        return {kind: buffers[kind] for kind in self._argument_index}

    @property
    def lowered_mlir_path(self):
        """Aiecc's post-lowering module, which carries the trace configuration and
        the trace buffer layout. A traced build asks aiecc to keep it, in the
        build's cache entry.
        """
        path = self.op.artifacts.lowered_mlir
        if path is None:
            raise FileNotFoundError(
                "the build produced no input_with_addresses.mlir; a traced build "
                "passes --get-input-with-addresses to aiecc"
            )
        return path

    def _get_buffer(self, buffer_name):
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
        parent = self._arguments()[buf_type]
        dtype = self.op.buffer_dtype(buffer_name)
        sub = parent.subview(offset, (length // dtype.itemsize,), dtype)
        self._buffer_cache[buffer_name] = sub
        return sub

    def get_storage(self, buffer_name):
        """The buffer, and the rest of its last coherence line, as a flat view.

        An exact view of a buffer that does not end on a line cannot be
        synchronized (``XRTTensor.subview``). Every buffer starts at a
        multiple of ``ALIGNMENT``, though, so the rest of its last line is
        padding no other buffer holds, and a view may take it along.
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
        """Run against the arena's current buffer, if it grew since the last call."""
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

    def get_buffer(self, buffer_name):
        self._follow_arena()
        return self._get_buffer(buffer_name)

    def _sync_inputs(self):
        # Each argument syncs to the device as a whole: sub-views handed out by
        # get_buffer() share their parent's coherence map, so a write through
        # one (weights, KV caches) is flushed with it.
        self._follow_arena()
        for tensor in self._arguments().values():
            tensor.to("npu")
        if self.trace_buffer is not None:
            self.trace_buffer.to("npu")

    def _sync_outputs(self):
        # The run just rewrote the output arena on the device, so the device holds the
        # authoritative copy. Force the device->host sync: assert device residency first
        # so `to("cpu")` fires even if a prior read of get_buffer(...) marked some
        # range "cpu" (otherwise a looped dispatch would read stale output).
        for buffer in (self.output_buffer, self.feedback_buffer, self.trace_buffer):
            if buffer is not None:
                buffer.device = "npu"
                buffer.to("cpu")

    def start(self, *runs: FullELFRun) -> None:
        """Push what the host wrote, and start ``runs`` without waiting; the
        caller waits on each (``wait``) and reads what it needs.
        """
        self._sync_inputs()
        for run in runs:
            run.start()

    def wait(self, *runs: FullELFRun) -> None:
        """Wait on ``runs``, started with ``start`` or on their own.

        The scratch and output arguments are marked device-resident after
        them, so a read of a view of either pulls what they wrote: a run
        restarted with ``FullELFRun.start()`` alone marks nothing.
        """
        for run in runs:
            run.wait()
        for buffer in (self.scratch_buffer, self.output_buffer):
            buffer.device = "npu"

    def __call__(self, *runs: FullELFRun):
        """Dispatch ``run``, or ``runs`` in order. Every run is started
        before any is waited on, so they queue back to back on the device.
        """
        runs = runs or (self.run,)
        self._sync_inputs()
        t0 = time.perf_counter()
        for run in runs:
            run.start()
        for run in runs:
            run.wait()
        self.last_elapsed = time.perf_counter() - t0
        self._sync_outputs()


class SequenceXclbinCallable(SequenceCallable):
    """Executes each runlist step as its own xclbin dispatch. Buffers shared by
    name give zero-copy handoff between consecutive operators. The chain's
    per-operator paths are on ``seq._image`` (an ``XclbinChain``).
    """

    def __init__(self, seq):
        _require_xrt()
        super().__init__(seq)

    def _allocate_buffers(self):
        super()._allocate_buffers()
        chain = self.op._image
        self._op_callable_map = {  # id(op) -> NPUKernel
            op_id: NPUKernel(
                chain.image,
                design.get_cache_entry().insts,
                kernel_name=chain.labels[op_id],
                dispatch_params=design.dispatch_params,
                dispatch_lib_path=design.get_dispatch_lib_path(),
            )
            for op_id, design in chain.designs.items()
        }
        # Per-call scalars of dispatch-time kernels, by symbol; a graph sets
        # them before each run (CompiledGraph._write_values).
        self.dispatch_values = {}
        self._execution_plan = [
            (
                self._op_callable_map[id(step_op)],
                [self._resolve_buffer(name) for name in buf_names],
            )
            for step_op, *buf_names in self.op.runlist
        ]

    def write_values(self, values: Mapping[str, np.generic]) -> None:
        """Each kernel takes its values as dispatch-time scalars and
        regenerates its stream.
        """
        self.dispatch_values = dict(values)

    def _run(self):
        # Walk the execution plan alongside the resolved runlist steps; the
        # per-step behaviour is delegated to _run_step so that compare mode can
        # reuse this loop verbatim.
        for step_idx, ((kernel, args), step) in enumerate(
            zip(self._execution_plan, self._iter_steps())
        ):
            self._run_step(step_idx, kernel, args, step)

    def _run_step(self, step_idx, kernel, args, step):
        scalars = {name: self.dispatch_values[name] for name in kernel.dispatch_params}
        kernel(*args, **scalars)

    def _sync_outputs(self):
        # _run rewrote these on the device, which the coherence map does not observe.
        # Assert device residency first so the pull fires even when a prior read left
        # the range marked "cpu"; otherwise a second dispatch reads the first's output.
        for name in self.op.subbuffer_layout:
            if name not in self.op.input_args:
                buf = self._buffers[name]
                buf.device = "npu"
                buf.to("cpu")


def _reshape_for_spec(flat_tensor, spec):
    """Slice a flat host buffer to ``spec``'s element count and reshape (a view)."""
    n = int(np.prod(spec.shape)) if spec.shape else 1
    return flat_tensor[:n].reshape(spec.shape)


class SequenceReferenceCallable(SequenceCallable):
    """Pure-CPU evaluation via each operator's ``reference()``; no NPU dispatch.
    Device syncs are no-ops on the CPU buffers.
    """

    def _make_buffer(self, n_elements, dtype):
        return CPUOnlyTensor((n_elements,), dtype=dtype)

    def _sync_inputs(self):
        # CPU-only inputs must stay CPU-resident, including lazily created subviews.
        pass

    def _run(self):
        for step_op, in_names, in_specs, out_name, out_spec in self._iter_steps():
            inputs = [
                _reshape_for_spec(self._resolve_buffer(n).numpy_view(), s).copy()
                for n, s in zip(in_names, in_specs)
            ]
            out = step_op.reference(*inputs)
            out_flat = self._resolve_buffer(out_name).numpy_view()
            n_out = int(np.prod(out_spec.shape)) if out_spec.shape else 1
            out_flat[:n_out] = out.reshape(-1).astype(out_flat.dtype)


class SequenceCompareCallable(SequenceXclbinCallable):
    """Runs the xclbin chain and, after each step, re-runs the operator's
    reference on the same NPU-produced inputs, logging per-step deviation. The
    NPU output propagates on both sides, so each comparison isolates a single
    operator (no error accumulation). ``compare`` judges each step by
    ``tolerance`` if given, else by ``step_tolerance``;
    ``raise_on_mismatch`` turns the first mismatch into an error.
    """

    # For a step whose operator states no tolerance, or one relative to the
    # output's range, which compare cannot judge element by element.
    FALLBACK_TOLERANCE = Tolerance.relative(0.025, 1e-2)

    def __init__(
        self,
        seq,
        tolerance: Tolerance | None = None,
        raise_on_mismatch: bool = True,
    ):
        super().__init__(seq)
        self.tolerance = tolerance
        self.raise_on_mismatch = raise_on_mismatch
        self.last_step_stats = []

    def step_tolerance(self, op: Operator) -> Tolerance:
        """The tolerance ``op``'s step is judged by."""
        if self.tolerance is not None:
            return self.tolerance
        tol = op.resolved().tolerance()
        if tol is None or tol.range_frac is not None:
            return self.FALLBACK_TOLERANCE
        return tol

    def _read_to_cpu(self, name, spec):
        buf = self._resolve_buffer(name)
        buf.to("cpu")
        n = int(np.prod(spec.shape)) if spec.shape else 1
        return buf.numpy_view()[:n].copy().reshape(spec.shape)

    def _run(self):
        # Reset per-invocation stats, then reuse SequenceXclbinCallable._run's
        # execution-plan loop; only the per-step behaviour (_run_step) differs.
        self.last_step_stats = []
        super()._run()

    def _run_step(self, step_idx, kernel, args, step):
        step_op, in_names, in_specs, out_name, out_spec = step

        cpu_inputs = [
            self._read_to_cpu(name, spec) for name, spec in zip(in_names, in_specs)
        ]

        super()._run_step(step_idx, kernel, args, step)

        npu_raw = self._read_to_cpu(out_name, out_spec)
        npu_out = npu_raw.astype(np.float32)
        ref_out = step_op.reference(*cpu_inputs)

        stats = {
            "step": step_idx,
            "op": type(step_op).__name__,
            "op_name": step_op.name,
            "inputs": list(in_names),
            "output": out_name,
        }

        ref_flat = ref_out.reshape(out_spec.shape).astype(np.float32)
        diff = np.abs(npu_out - ref_flat)
        ref_mag = np.abs(ref_flat)
        max_abs = float(diff.max())
        ref_max = float(ref_mag.max())
        rel = float((diff / (ref_mag + 1e-6)).max())
        mean_abs = float(diff.mean())
        stats.update(
            skipped=False,
            max_abs=max_abs,
            mean_abs=mean_abs,
            max_rel=rel,
            ref_max=ref_max,
        )
        tol = self.step_tolerance(step_op)
        bound = tol.bound(*cpu_inputs) if tol.bound is not None else None
        verdict = compare(npu_raw, ref_flat, tol, bound=bound)
        fail = not verdict
        stats["mismatch"] = fail
        level = logging.ERROR if fail else logging.INFO
        logger.log(
            level,
            "[compare step %d] %s -> %s: max_abs=%.4g mean_abs=%.4g max_rel=%.4g ref_max=%.4g%s",
            step_idx,
            stats["op"],
            out_name,
            max_abs,
            mean_abs,
            rel,
            ref_max,
            f"  MISMATCH: {verdict.detail}" if fail else "",
        )
        if fail and self.raise_on_mismatch:
            raise RuntimeError(
                f"[compare step {step_idx}] {stats['op']} (name={stats['op_name']}) "
                f"-> {out_name}: NPU output deviates from reference "
                f"({verdict.detail}; max_abs={max_abs:.4g}, max_rel={rel:.4g}, "
                f"ref_max={ref_max:.4g}; inputs={list(in_names)}; tolerance {tol})"
            )
        self.last_step_stats.append(stats)
