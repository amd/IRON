# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Prototype: silu(gate) * up as two operators chained on-chip.

SiLU's output stream feeds ElementwiseMul's first input through the fifos
SiLU's cores write, so the intermediate never reaches the host; the two
runtimes issue their transfers in one task group. Writes the fused module,
runs mlir-aie's aie-resource-stages on it, and optionally compiles it and runs
it on the device against the operators' references.
"""

import argparse
import inspect
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.iron import Program
from aie.iron.device import from_name
from aie.passmanager import PassManager
from aie.utils.benchmark import run_iters
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.compile.jit.markers import DispatchTime, _DispatchParameter
from aie.utils.npukernel import NPUKernel
from aie.utils.verify import Tolerance, bf16_ulp_distance, compare, poisoned

from iron.common.design.design import BuiltArray, OperatorDesign
from iron.common.design.runtime import MergedRuntime, OperatorRuntime
from iron.common.image.link import FullELF
from iron.common.testing import vectors
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.silu import SiLU


def fused_designs(
    size: int, cols: int, tile: int, full_elf: bool, per_call: bool
) -> list[OperatorDesign]:
    dev = aie_utils.get_current_device()
    # A graph binding `valid` makes it a value each call gives.
    bound = {"valid": None} if per_call else {}
    ops = [
        cls(
            size=size, num_aie_columns=cols, tile_size=tile, bound_values=bound
        ).resolved(dev)
        for cls in (SiLU, ElementwiseMul)
    ]
    return [OperatorDesign(op, full_elf=full_elf) for op in ops]


def fused_program(designs: list[OperatorDesign], dispatch: dict) -> Program:
    first = BuiltArray(designs[0], dispatch=dispatch)
    second = BuiltArray(designs[1], dispatch=dispatch, fed={"a": first.op.y})
    runtime = MergedRuntime.fuse(
        [
            OperatorRuntime(first.op, first.built),
            OperatorRuntime(second.op, second.built),
        ],
        "sequence",
    )
    return Program(
        first.op.array_device(), runtime, workers=first.workers + second.workers
    )


def fused_compilable(designs: list[OperatorDesign], full_elf: bool) -> CompilableDesign:
    P = inspect.Parameter
    params = [
        P(v.symbol, P.KEYWORD_ONLY, annotation=DispatchTime[v.dtype])
        for d in designs
        for v in d.op.values
        if not full_elf
    ]

    def generator(**dispatch):
        return fused_program(designs, dispatch).resolve_program()

    setattr(generator, "__signature__", inspect.Signature(params))
    return CompilableDesign(
        generator,
        use_cache=False,
        aiecc_flags=[
            *(FullELF.FLAGS if full_elf else ()),
            *(f for d in designs for f in d.op.aiecc_flags),
        ],
        full_elf=full_elf,
    )


def run(
    designs: list[OperatorDesign],
    compiled: CompilableDesign,
    args: argparse.Namespace,
) -> None:
    """Dispatch the fused design on ``valid`` elements and hold ``y`` to
    ``silu(gate) * up``, the operators' references chained, and to the two
    operators run unfused on the device; prints each call's minimum time.

    Raises:
        RuntimeError: ``y`` falls outside the tolerance, a bounded call wrote
            past ``valid``, or the fused and unfused outputs differ.
    """
    silu, mul = (d.op for d in designs)
    valid = args.size if args.valid is None else args.valid
    entry = compiled.get_cache_entry()
    assert entry is not None, "compile() built it"
    if args.full_elf:
        kernel = NPUKernel(
            elf_path=entry.elf,
            kernel_name=entry.full_elf_kernel,
            params_path=entry.params,
        )
    else:
        kernel = NPUKernel(
            entry.xclbin,
            entry.insts,
            dispatch_params=compiled.dispatch_params,
            dispatch_lib_path=compiled.get_dispatch_lib_path(),
        )
    # S6: one count for both operators, every call.
    words = {
        v.symbol: np.dtype(v.dtype).type(
            valid if v.derive is None else d.op.derived_at(v.name, valid=valid)
        )
        for d in designs
        for v in d.op.values
    }
    if words and args.full_elf:
        # The ELF's table holds only the words its cores and DMAs read.
        assert entry.params is not None, "--get-scratchpad-parameters wrote it"
        header, *rows = entry.params.read_text().splitlines()
        declared = {row.split()[0] for row in rows[: int(header.split()[0])]}
        call = {"parameters": {k: w for k, w in words.items() if k in declared}}
    else:
        call = dict(words)
    print("per-call words:", {k.split("_npu2_")[-1]: int(w) for k, w in words.items()})

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    x_t, b_t = tensor(gate), tensor(up)
    y_t = tensor(poisoned(args.size, y_ref.dtype))
    kernel(x_t, b_t, y_t, **call)
    y = y_t.numpy()

    # A 1-ulp intermediate (2^-7 relative at most) is <= 2 ulps of the product,
    # plus half an ulp for each of the device's and the reference's rounding.
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    # A bounded call computes whole rounds of every core's tile.
    end = min(
        args.size, mul.derived_at("count", valid=valid) * mul.cores * mul.tile_size
    )
    verdict = compare(y[:end], y_ref[:end], tol)
    ulps = bf16_ulp_distance(y[:end], y_ref[:end])
    print(
        f"vs reference: {'PASS' if verdict else 'FAIL'} "
        f"max_abs={verdict.max_abs_err:.4g} max_ulp={int(ulps.max())} "
        f"ulp histogram={np.bincount(ulps.ravel()).tolist()}"
    )
    if not verdict:
        raise RuntimeError(f"y deviates from silu(gate) * up: {verdict.detail}")
    untouched = poisoned(args.size, y_ref.dtype)[end:]
    if not np.array_equal(y[end:].view(np.uint16), untouched.view(np.uint16)):
        raise RuntimeError(f"a call bounded to {valid} wrote past its round, {end}")

    alone = [
        cls(size=args.size, num_aie_columns=args.cols, tile_size=args.tile).resolved()
        for cls in (SiLU, ElementwiseMul)
    ]
    h_t = tensor(poisoned(args.size, y_ref.dtype))
    y2_t = tensor(poisoned(args.size, y_ref.dtype))
    alone[0](x_t, h_t)
    alone[1](h_t, b_t, y2_t)
    unfused = y2_t.numpy()
    same = np.array_equal(y[:end].view(np.uint16), unfused[:end].view(np.uint16))
    print(f"vs unfused device chain: {'bit-equal' if same else 'DIFFERS'}")
    if not same:
        raise RuntimeError("the fused and unfused device outputs differ")

    fused = run_iters(kernel, x_t, b_t, y_t, warmup=3, iters=args.iters, **call)
    steps = [
        run_iters(alone[0], x_t, h_t, warmup=3, iters=args.iters),
        run_iters(alone[1], h_t, b_t, y2_t, warmup=3, iters=args.iters),
    ]
    assert fused.dispatch is not None, "an NPUKernel call reports its dispatch time"
    print(
        f"fused: dispatch min {fused.dispatch.min_us:.1f} us"
        + (f", npu median {fused.npu.median_us:.1f} us" if fused.npu else "")
        + f"; unfused SiLU + Mul dispatch min "
        + " + ".join(f"{s.dispatch.min_us:.1f}" for s in steps if s.dispatch)
        + " us"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", choices=("npu1", "npu2"), default="npu1")
    parser.add_argument("--size", type=int, default=2048)
    parser.add_argument("--cols", type=int, default=1)
    parser.add_argument("--tile", type=int, default=1024)
    parser.add_argument("--full-elf", action="store_true")
    parser.add_argument(
        "--per-call",
        action="store_true",
        help="give both operators' `valid` per call, a dispatch-time value on an xclbin",
    )
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--compile",
        action="store_true",
        help="also compile the kernels and the design",
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="compile, then run on the device against silu(gate) * up",
    )
    parser.add_argument(
        "--valid",
        type=int,
        help="with --per-call, the elements a call computes (default: size)",
    )
    parser.add_argument("--iters", type=int, default=50)
    args = parser.parse_args()
    if args.valid is not None and not args.per_call:
        parser.error("--valid needs --per-call")

    aie_utils.set_current_device(from_name(args.device, n_cols=None))
    designs = fused_designs(
        args.size, args.cols, args.tile, args.full_elf, args.per_call
    )
    values = [v for d in designs for v in d.op.values]
    dispatch = {
        v.symbol: _DispatchParameter(v.symbol, v.dtype, i, None)
        for i, v in enumerate(values)
    }
    print("per-call values:", [v.symbol for v in values])
    module = fused_program(designs, dispatch).resolve_program()
    args.out.write_text(str(module))
    print(f"wrote {args.out}")
    PassManager.parse(
        "builtin.module(aie-resource-stages{placer=sa_placer})", module.context
    ).run(module.operation)
    args.out.with_suffix(".resourced.mlir").write_text(str(module))
    print("aie-resource-stages: fits")
    if args.compile or args.run:
        compiled = fused_compilable(designs, args.full_elf)
        print("compiled:", compiled.compile())
        if args.run:
            run(designs, compiled, args)


if __name__ == "__main__":
    main()
