# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Prototype: silu(gate) * up as two operators chained on-chip.

SiLU's output stream feeds ElementwiseMul's first input through the fifos
SiLU's cores write, so the intermediate never reaches the host; the two
runtimes issue their transfers in one task group. Writes the fused module,
runs mlir-aie's aie-resource-stages on it, and optionally compiles it.
"""

import argparse
import inspect
from pathlib import Path

import aie.utils as aie_utils
from aie.iron import Program
from aie.iron.device import from_name
from aie.passmanager import PassManager
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.compile.jit.markers import DispatchTime, _DispatchParameter

from iron.common.design.design import BuiltArray, OperatorDesign
from iron.common.design.runtime import MergedRuntime, OperatorRuntime
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
        aiecc_flags=[f for d in designs for f in d.op.aiecc_flags],
        full_elf=full_elf,
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
    args = parser.parse_args()

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
    if args.compile:
        print("compiled:", fused_compilable(designs, args.full_elf).compile())


if __name__ == "__main__":
    main()
