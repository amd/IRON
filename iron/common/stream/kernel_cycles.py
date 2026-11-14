# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The cycles per call of each kernel the library prices, measured on the NPU.

One core calls the kernel ``reps`` times on operands in its own memory, so
no transfer is timed; the per-call cycles are the difference against one
call, over ``reps - 1``, at the core clock the runtime reads.
``python -m iron.common.stream.kernel_cycles`` measures every shape
``kernels/<arch>.toml`` carries cycles for and prints its rows.
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

import argparse
import functools
from typing import Any, Callable

import aie.utils as aie_utils
import numpy as np
from aie.iron import Buffer, In, ObjectFifo, Out, Program, Runtime, Worker
from aie.iron.controlflow import range_
from aie.utils.benchmark import run_iters
from aie.utils.compile.jit.params import param
from aie.utils.compile.utils import resolve_target_arch
from ml_dtypes import bfloat16

from ..declare import Operator
from .kernel_library import load_library

LOG2E = 1.4426950408889634
# A flash call's block index: key block 0 of query block 2, which every row keeps.
BLOCK_INDEX = (0, 2, 0)

# Each kernel's scalars, after its buffers, as stream-dse's codegen calls it.
SCALARS: dict[str, Callable[[dict[str, int]], list[Any]]] = {
    "matmul_bf16_f32": lambda s: [],
    "matmul_bf16_bf16_high": lambda s: [],
    "silu_bf16_size": lambda s: [s["m"] * s["n"]],
    "eltwise_mul_bf16_vector_size": lambda s: [s["m"] * s["n"]],
    "partial_softmax": lambda s: [LOG2E, s["m"], s["n"], 3 * s["m"], s["n"]],
    "matmul_PV": lambda s: [s["m"], 1, 1 << 14],
}


def _arguments(symbol: str, shape: dict[str, int], buffers: list) -> list:
    """Return the call's arguments: its buffers, with the scalars where it takes them."""
    scalars = SCALARS[symbol](shape)
    if symbol == "matmul_PV":
        # matmul_PV(P, V, O, scale, rows, carried, index, keys)
        return [*buffers[:4], *scalars[:2], buffers[4], scalars[2]]
    return [*buffers, *scalars]


def _initial(dims: int, dtype, rng) -> np.ndarray:
    if dtype == np.int32:
        return np.array(BLOCK_INDEX if dims == 3 else [0] * dims, dtype=np.int32)
    if dtype == np.float32:
        return (np.abs(rng.standard_normal(dims)) + 1.0).astype(np.float32)
    return (rng.standard_normal(dims) * 0.5).astype(bfloat16)


def _design(symbol: str, shape: tuple[tuple[str, int], ...], reps: int):
    from stream.compiler.kernels.binding import resolve

    dims = dict(shape)
    dev = aie_utils.ensure_current_device()
    assert dev is not None, "an operator's design is generated for the bound device"
    spec = load_library(resolve_target_arch(dev)).spec(symbol)
    with aie_utils.set_current_device(dev):
        kernel = resolve(
            {"binding": spec.binding, "args": {**dims, **spec.options, "npu": dev.name}}
        )
    rng = np.random.default_rng(0)
    buffers = []
    for t in kernel.arg_types():
        if not hasattr(t, "__args__"):
            continue
        (size,), dtype = t.__args__[0], t.__args__[1].__args__[0]
        buffers.append(Buffer(t, initial_value=_initial(size, dtype, rng)))
    word = np.ndarray[(16,), np.dtype[np.int32]]
    start, done = ObjectFifo(word, depth=1), ObjectFifo(word, depth=1)

    def core(kernel, start, done, *buffers):
        start.acquire(1)
        for _ in range_(reps):
            kernel(*_arguments(symbol, dims, list(buffers)))
        start.release(1)
        done.acquire(1)
        done.release(1)

    worker = Worker(core, [kernel, start.cons(), done.prod(), *buffers])

    def sequence(x, y, start, done):
        start.fill(x)
        done.drain(y, wait=True)

    runtime = Runtime(sequence, [word, word, start.prod(), done.cons()])
    return Program(dev, runtime, workers=[worker]).resolve_program()


class KernelLoop(Operator):
    """One core calling ``symbol`` at ``shape`` ``reps`` times, started by ``x``."""

    symbol: str = param()
    shape: tuple[tuple[str, int], ...] = param()
    reps: int = param()

    x = In(16, dtype=np.int32)
    y = Out(16, dtype=np.int32)

    def exported_design(self):
        return functools.partial(_design, self.symbol, self.shape, self.reps)


def _dispatch_us(symbol: str, shape: dict[str, int], reps: int) -> float:
    op = KernelLoop(symbol=symbol, shape=tuple(sorted(shape.items())), reps=reps)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    args = (tensor(np.zeros(16, dtype=np.int32)), tensor((16,), dtype=np.int32))
    op(*args)
    benchmark = run_iters(op, *args, warmup=3, iters=20)
    assert benchmark.dispatch is not None, "an operator's call reports its dispatch"
    return benchmark.dispatch.min_us


def cycles(symbol: str, shape: dict[str, int], reps: int = 2049) -> float:
    """Return ``symbol``'s cycles per call at ``shape`` on the bound device."""
    elapsed = _dispatch_us(symbol, shape, reps) - _dispatch_us(symbol, shape, 1)
    return elapsed / (reps - 1) * aie_utils.DefaultNPURuntime.core_mhz


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure the kernel library's cycles per call on the NPU."
    )
    parser.add_argument("--reps", type=int, default=2049)
    args = parser.parse_args()
    library = load_library(resolve_target_arch(aie_utils.ensure_current_device()))
    for symbol, spec in library.kernels.items():
        for shape, priced in spec.cycles:
            measured = cycles(symbol, dict(shape), args.reps)
            fields = ", ".join(f"{k} = {v}" for k, v in shape.items())
            print(
                f"{symbol}: {{ {fields}, cycles = {measured:.0f}.0 }}  # was {priced}"
            )


if __name__ == "__main__":
    main()
