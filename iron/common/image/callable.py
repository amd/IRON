# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a caller invokes once a sequence has an image: one class per image kind."""

import logging
import time

import ml_dtypes
import numpy as np

import aie.utils as aie_utils
from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from aie.utils.npukernel import NPUKernel

from . import fusion
from .jit_compile import DispatchStream

try:
    import pyxrt
    from aie.utils.hostruntime.xrtruntime.parameter_scratchpad import (
        ParameterScratchpad,
    )
    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
except ImportError:
    # Host stacks without XRT (e.g. the HRX/amdxdna runtime) have no pyxrt. The
    # on-device callables here are XRT-native (pyxrt.elf / hw_context / run,
    # plus XRTTensor views), so they cannot run there; _require_xrt() makes
    # that explicit at construction. The reference mode and the whole compile
    # path do not care, and must keep importing.
    pyxrt = None
    ParameterScratchpad = None
    XRTTensor = None

logger = logging.getLogger(__name__)

BF16 = np.dtype(ml_dtypes.bfloat16)


def _n_elements(nbytes):
    return max(nbytes, BF16.itemsize) // BF16.itemsize

def _require_xrt() -> None:
    """Fail with the reason, rather than an AttributeError on ``None.elf``."""
    if pyxrt is None:
        raise RuntimeError(
            "this OperatorSequence mode needs the XRT host runtime (pyxrt), which is "
            "not installed. Use the reference mode, or run a single operator, which "
            "dispatches through aie.utils.DefaultNPURuntime and works on any backend."
        )


class SequenceCallable:
    """Runs an ``OperatorSequence`` once per call.

    Buffers are one per name, a slice a view into its parent; inputs sync to
    the device before the run and everything else back to the host after.
    Subclasses give the buffer (``_make_buffer``) and the run (``_run``); the
    full-ELF callable replaces the buffer model with its three arenas.
    """

    def __init__(self, seq):
        self.op = seq
        self.last_elapsed = 0.0
        self._buffer_cache = {}
        self._allocate_buffers()

    def _make_buffer(self, n_elements):
        return XRTTensor((n_elements,), dtype=ml_dtypes.bfloat16)

    def _allocate_buffers(self):
        self._buffers = {}
        for name, (_, _, length) in self.op.subbuffer_layout.items():
            self._buffers[name] = self._make_buffer(_n_elements(length))

    def _resolve_buffer(self, buf_name):
        if buf_name in self._buffers:
            return self._buffers[buf_name]
        if buf_name in self.op.slice_info:
            base_name, start_bytes, end_bytes = self.op.slice_info[buf_name]
            size_bytes = end_bytes - start_bytes
            sub = self._buffers[base_name].subview(
                start_bytes, (size_bytes // BF16.itemsize,), BF16
            )
            self._buffers[buf_name] = sub
            return sub
        raise ValueError(f"Unknown buffer '{buf_name}' in fused runlist")

    def get_buffer(self, buffer_name):
        if buffer_name not in self._buffer_cache:
            self._buffer_cache[buffer_name] = self._resolve_buffer(buffer_name)
        return self._buffer_cache[buffer_name]

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

    def __call__(self):
        self._sync_inputs()
        t0 = time.perf_counter()
        self._run()
        self.last_elapsed = time.perf_counter() - t0
        self._sync_outputs()


class SequenceFullELFCallable(SequenceCallable):
    """The full ELF (NPU2): every operator shares three consolidated
    input/output/scratch buffers addressed by offset. ``get_buffer`` returns a
    sub-view into whichever consolidated buffer holds the named argument.
    """

    def __init__(self, seq, device_name="main", sequence_name="sequence"):
        _require_xrt()
        self.device_name = device_name
        self.sequence_name = sequence_name

        xrt_elf = pyxrt.elf(str(seq.image))
        xrt_context = pyxrt.hw_context(aie_utils.DefaultNPURuntime._device, xrt_elf)
        self.xrt_kernel = pyxrt.ext.kernel(
            xrt_context, f"{self.device_name}:{self.sequence_name}"
        )

        super().__init__(seq)

        # Persistent run handle: reused across dispatches so that the
        # ctrl-scratchpad backing buffer (and any ParameterScratchpad state
        # built on top of it) stays valid across calls.
        self.run_handle = pyxrt.run(self.xrt_kernel)
        self.run_handle.set_arg(0, self.input_buffer.buffer_object())
        self.run_handle.set_arg(1, self.output_buffer.buffer_object())
        self.run_handle.set_arg(2, self.scratch_buffer.buffer_object())
        if self.trace_buffer is not None:
            self.run_handle.set_arg(3, self.trace_buffer.buffer_object())

        self._params = None

    @property
    def params(self):
        """Lazy ParameterScratchpad bound to this ELF's ctrl scratchpad BO.

        The ``params.txt`` describing the runtime parameters is requested
        from aiecc via ``--get-scratchpad-parameters`` and lands in the
        build's cache entry, which :attr:`Artifacts.params` names. Returns
        ``None`` if the sequence declared no runtime parameters: the file
        still exists, but holds a count of zero and there is no ctrl
        scratchpad buffer object to bind to.
        """
        if self._params is not None:
            return self._params
        params_path = self.op.artifacts.params
        if params_path is None:
            return None
        if params_path.read_text().split("\n", 1)[0].strip() == "0":
            return None
        self._params = ParameterScratchpad(self.run_handle, str(params_path))
        return self._params

    def _allocate_buffers(self):
        in_sz, out_sz, scratch_sz = self.op.buffer_sizes
        self.input_buffer = XRTTensor((_n_elements(in_sz),), dtype=ml_dtypes.bfloat16)
        self.output_buffer = XRTTensor((_n_elements(out_sz),), dtype=ml_dtypes.bfloat16)
        self.scratch_buffer = XRTTensor(
            (_n_elements(scratch_sz),), dtype=ml_dtypes.bfloat16
        )
        # Trace lowering appends one buffer covering every configured design, after
        # the consolidated three. Its size depends on how many channels and
        # sub-designs claim a share, so read it from the lowered module.
        self.trace_buffer = None
        if self.op.trace_size:
            total = fusion.trace_buffer_size(self.lowered_mlir_text())
            if total:
                self.trace_buffer = XRTTensor((total,), dtype=np.int8)

    def lowered_mlir_text(self) -> str:
        """aiecc's post-lowering module, which carries the trace buffer layout."""
        return self.op.artifacts.lowered_mlir.read_text()

    def get_buffer(self, buffer_name):
        if buffer_name in self._buffer_cache:
            return self._buffer_cache[buffer_name]
        buf_type, offset, length = self.op.get_layout_for_buffer(buffer_name)
        parent = {
            "input": self.input_buffer,
            "output": self.output_buffer,
            "scratch": self.scratch_buffer,
        }[buf_type]
        sub = parent.subview(offset, (length // BF16.itemsize,), ml_dtypes.bfloat16)
        self._buffer_cache[buffer_name] = sub
        return sub

    def _sync_inputs(self):
        # Sub-views handed out by get_buffer() share the parent's coherence map, so
        # a write through one (e.g. numpy_view()) marks its byte range host-dirty
        # there too, and `to("npu")` here syncs every dirty range in one pass.
        self.input_buffer.to("npu")

    def _sync_outputs(self):
        # _run just rewrote the output arena on the device, so the device holds the
        # authoritative copy. Force the device->host sync: assert device residency first
        # so `to("cpu")` fires even if a prior read of get_buffer(...) marked some
        # range "cpu" (otherwise a looped dispatch would read stale output).
        self.output_buffer.device = "npu"
        self.output_buffer.to("cpu")
        if self.trace_buffer is not None:
            self.trace_buffer.device = "npu"
            self.trace_buffer.to("cpu")

    def _run(self):
        self.run_handle.start()
        ret_code = self.run_handle.wait()
        if ret_code != pyxrt.ert_cmd_state.ERT_CMD_STATE_COMPLETED:
            raise RuntimeError(f"Kernel execution failed with return code {ret_code}")


class SequenceXclbinCallable(SequenceCallable):
    """Executes each runlist step as its own xclbin dispatch. Buffers shared by
    name give zero-copy handoff between consecutive operators. The chain's
    per-operator paths are on ``seq._image`` (an :class:`XclbinChain`).
    """

    def __init__(self, seq):
        _require_xrt()
        super().__init__(seq)

    def _allocate_buffers(self):
        super()._allocate_buffers()
        chain = self.op._image
        self._op_callable_map = {}  # id(op) -> NPUKernel
        # Per-call scalars of dispatch-time kernels, by symbol; a graph sets
        # them before each run (CompiledGraph._write_values).
        self.dispatch_values = {}
        for op_id, xclbin_path in chain.op_xclbin_path_map.items():
            stream = chain.op_insts_path_map[op_id]
            if isinstance(stream, DispatchStream):
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(chain.combined_xclbin_path),
                    kernel_name=chain.op_kernel_name_map[op_id],
                    dispatch_params=list(stream.params),
                    dispatch_lib_path=str(stream.lib_path),
                )
            else:
                self._op_callable_map[op_id] = NPUKernel(
                    xclbin_path=str(chain.combined_xclbin_path),
                    kernel_name=chain.op_kernel_name_map[op_id],
                    insts_path=str(stream),
                )
        self._execution_plan = [
            (
                self._op_callable_map[id(step_op)],
                [self._resolve_buffer(name) for name in buf_names],
            )
            for step_op, *buf_names in self.op.runlist
        ]

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

    def _make_buffer(self, n_elements):
        return CPUOnlyTensor((n_elements,), dtype=BF16)

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
            out_flat[:n_out] = out.reshape(-1).astype(BF16)


class SequenceCompareCallable(SequenceXclbinCallable):
    """Runs the xclbin chain and, after each step, re-runs the operator's
    reference on the same NPU-produced inputs, logging per-step deviation. The
    NPU output propagates on both sides, so each comparison isolates a single
    operator (no error accumulation). A step is a mismatch when it exceeds
    both tolerances; ``raise_on_mismatch`` turns the first one into an error.
    """

    def __init__(self, seq, rel_tol=0.05, abs_tol=1e-2, raise_on_mismatch=True):
        super().__init__(seq)
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        self.raise_on_mismatch = raise_on_mismatch
        self.last_step_stats = []

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

        kernel(*args)

        npu_out = self._read_to_cpu(out_name, out_spec).astype(np.float32)
        ref_out = step_op.reference(*cpu_inputs)

        stats = {
            "step": step_idx,
            "op": type(step_op).__name__,
            "op_name": getattr(step_op, "name", type(step_op).__name__),
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
        fail = (max_abs > self.abs_tol) and (rel > self.rel_tol)
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
            "  MISMATCH" if fail else "",
        )
        if fail and self.raise_on_mismatch:
            raise RuntimeError(
                f"[compare step {step_idx}] {stats['op']} (name={stats['op_name']}) "
                f"-> {out_name}: NPU output deviates from reference "
                f"(max_abs={max_abs:.4g}, max_rel={rel:.4g}, "
                f"ref_max={ref_max:.4g}; inputs={list(in_names)}; "
                f"tolerances abs_tol={self.abs_tol}, rel_tol={self.rel_tol})"
            )
        self.last_step_stats.append(stats)
