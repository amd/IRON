# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Probe ten encoder designs in chained xclbins, without a model or checkpoint.

This is a current-API reconstruction of the historical Whisper timeout probe,
not the original reproduction. The default uses mlir-aie's normal chain batching.
``--kernels-per-image 10`` deliberately places all ten designs in one image.
Only one process should use the NPU while this probe runs.
"""

import argparse
import faulthandler
import json
import platform
import time
import traceback
from importlib.metadata import version
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import from_name
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel

from iron import Precision
from iron.common.design import OperatorDesign
from iron.common.testing import vectors
from iron.operators import GELU, GEMM, ElementwiseAdd, LayerNorm, Softmax


def operators(rows: int, width: int, hidden: int):
    """Return the historical five GEMMs, norm, softmax, GELU and two adds."""

    def gemm(k, n, columns=4):
        return GEMM(
            M=rows,
            K=k,
            N=n,
            num_aie_columns=columns,
            tile_m=16,
            tile_k=64,
            tile_n=64,
            precision=Precision.HIGHEST,
        )

    def elementwise(cls, columns):
        return cls(
            size=rows * columns,
            num_aie_columns=4,
            num_channels=1,
            tile_size=columns,
        )

    return {
        "p768": gemm(width, width),
        "score": gemm(64, rows),
        "value": gemm(rows, 64, columns=1),
        "fc1": gemm(width, hidden),
        "fc2": gemm(hidden, width),
        "norm": LayerNorm(
            rows=rows, tile_size=width, num_aie_columns=4, num_channels=1
        ),
        "softmax": Softmax(rows=rows, cols=rows, num_aie_columns=4, num_channels=1),
        "gelu": elementwise(GELU, hidden),
        "add": elementwise(ElementwiseAdd, width),
        "add_mlp": elementwise(ElementwiseAdd, hidden),
    }


def main(argv=None) -> int:
    """Compile the chain, invoke each kernel, and save explicit per-kernel results."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=1536)
    parser.add_argument("--width", type=int, default=768)
    parser.add_argument("--hidden", type=int, default=3072)
    parser.add_argument("--kernels-per-image", type=int)
    parser.add_argument("--compile-only", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("chain-probe.json"))
    args = parser.parse_args(argv)
    if any(n <= 0 or n % 256 for n in (args.rows, args.width, args.hidden)):
        parser.error("rows, width and hidden must be positive multiples of 256")
    if args.kernels_per_image is not None and args.kernels_per_image < 1:
        parser.error("--kernels-per-image must be positive")
    original_batch_size = CompilableDesign.XCLBIN_KERNELS
    if args.kernels_per_image is not None:
        CompilableDesign.XCLBIN_KERNELS = args.kernels_per_image

    report = {
        "kind": "current-API reconstruction, not the historical reproducer",
        "device": "npu1",
        "platform": platform.platform(),
        "python": platform.python_version(),
        "mlir_aie": version("mlir-aie"),
        "rows": args.rows,
        "width": args.width,
        "hidden": args.hidden,
        "kernels_per_image": CompilableDesign.XCLBIN_KERNELS,
        "compile_only": args.compile_only,
        "results": [],
    }

    def save(row):
        report["results"].append(row)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps(row), flush=True)

    faulthandler.dump_traceback_later(120, repeat=True)
    try:
        with aie_utils.set_current_device(from_name("npu1", n_cols=4)):
            named = {
                name: op.resolved()
                for name, op in operators(args.rows, args.width, args.hidden).items()
            }
            print(
                f"Compiling {len(named)} designs; batch size {CompilableDesign.XCLBIN_KERNELS}",
                flush=True,
            )
            built = CompilableDesign.chain(
                [
                    OperatorDesign(op, full_elf=False).compilable()
                    for op in named.values()
                ],
                "whisper_encoder_chain_probe",
            )
            failed = False
            for index, ((name, op), (design, image, label)) in enumerate(
                zip(named.items(), built)
            ):
                entry = design.get_cache_entry()
                assert entry is not None, "chain() compiled the design"
                row = dict(
                    index=index,
                    name=name,
                    kernel=label,
                    image=str(image),
                    instructions=str(entry.insts),
                )
                if args.compile_only:
                    save(row | {"status": "compiled, not executed"})
                    continue
                kernel = NPUKernel(
                    image,
                    entry.insts,
                    kernel_name=label,
                    dispatch_params=design.dispatch_params,
                    dispatch_lib_path=design.get_dispatch_lib_path(),
                )
                inputs = vectors(op, scale=0.25)
                tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
                buffers, outputs = [], {}
                for operand in op.buffers:
                    tensor = (
                        tensor_class(inputs.inputs[operand.name])
                        if operand.fills
                        else tensor_class(operand.host_shape, dtype=operand.host_dtype)
                    )
                    buffers.append(tensor)
                    if operand.drains:
                        outputs[operand.name] = tensor
                print(f"Dispatch {index}: {name} ({label})", flush=True)
                start = time.perf_counter()
                try:
                    kernel(*buffers)
                    actual = {name: tensor.numpy() for name, tensor in outputs.items()}
                    verdicts = op.judge(
                        inputs.inputs, actual, op.tolerance(), inputs.outputs
                    )
                    errors = {
                        name: verdict.detail
                        for name, verdict in verdicts.items()
                        if not verdict
                    }
                    save(
                        row
                        | {
                            "status": "mismatch" if errors else "passed",
                            "seconds": time.perf_counter() - start,
                            "errors": errors,
                        }
                    )
                    failed |= bool(errors)
                except (RuntimeError, OSError) as exc:
                    traceback.print_exc()
                    save(
                        row
                        | {
                            "status": "dispatch failed",
                            "seconds": time.perf_counter() - start,
                            "error": str(exc),
                        }
                    )
                    failed = True
            return int(failed)
    finally:
        CompilableDesign.XCLBIN_KERNELS = original_batch_size
        faulthandler.cancel_dump_traceback_later()
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
