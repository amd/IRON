# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compile the engine's exported GEMM generators and run their instructions."""

import shutil
import subprocess

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.config import runtime_header_path
from aie.utils.npukernel import NPUKernel
from ml_dtypes import bfloat16

from iron.operators.flm.gemma4_engine.build import (
    MAX_M,
    PLI_MAX_M,
    gemm,
    write_gemm_generators,
)
from iron.tests.support.tools import requires


@pytest.fixture(
    params=[
        (MAX_M, 1536, 256, False),  # partial columns, resident B
        (MAX_M, 1536, 12288, True),  # wide C and GELU
        (MAX_M, 12288, 1536, False),  # wide A and streamed B
        (PLI_MAX_M, 256, 1536, False),  # per-layer input
    ],
    ids=["kv", "gate", "down", "pli"],
)
def exported(request, npu2, tmp_path):
    compiler = shutil.which("c++")
    if compiler is None:
        pytest.skip("no C++ compiler")
    op = gemm(*request.param)
    artifacts = op.compile()
    write_gemm_generators([op], {op: artifacts}, tmp_path)
    source = tmp_path / "generate.cpp"
    source.write_text(
        '#include "gemm.h"\n'
        "#include <cstdio>\n"
        "#include <cstdlib>\n"
        "int main(int argc, char **argv) {\n"
        "    auto words = iron::seq::gemm_generators[0].generate(std::atoi(argv[1]));\n"
        "    if (!words) return 2;\n"
        "    std::fwrite(words->data(), sizeof(uint32_t), words->size(), stdout);\n"
        "}\n"
    )
    executable = tmp_path / "generate"
    subprocess.run(
        [
            compiler,
            "-std=c++17",
            f"-I{runtime_header_path()}",
            str(source),
            "-o",
            str(executable),
        ],
        check=True,
        capture_output=True,
    )
    return op.resolved(), artifacts, executable


@requires("aiecc", "xclbinutil", "peano")
def test_exported_generator_matches_the_python_dispatch_bridge(exported):
    op, artifacts, executable = exported
    bridge = NPUKernel(
        artifacts.image,
        None,
        dispatch_params=[v.symbol for v in op.values],
        dispatch_lib_path=artifacts.entry.dispatch_library,
    )
    for m in range(256, op.M + 1, 256):
        params = {
            v.symbol: op.derived_at(v.name, valid=m) if v.derive else m
            for v in op.values
        }
        result = subprocess.run([executable, str(m)], check=True, capture_output=True)
        assert result.stdout == bridge.instructions(**params).tobytes(), m
    for m in (-256, 0, 1, 257, op.M + 256):
        result = subprocess.run([executable, str(m)], capture_output=True)
        assert result.returncode == 2 and not result.stdout, m


@pytest.mark.supported_devices("npu2")
def test_exported_rows_match_static_and_leave_the_tail_untouched(exported, tmp_path):
    op, artifacts, executable = exported
    rng = np.random.default_rng(235)
    a = rng.uniform(-0.5, 0.5, (op.M, op.K)).astype(bfloat16)
    b = rng.uniform(-0.5, 0.5, (op.K, op.N)).astype(bfloat16)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    packed_b = tensor(op.pack_b(b))
    input_a = tensor(a.reshape(-1))
    for i, m in enumerate((op.M, 256, 512, 1024, 256)):
        result = subprocess.run([executable, str(m)], check=True, capture_output=True)
        insts = tmp_path / f"rows_{i}.bin"
        insts.write_bytes(result.stdout)
        output = tensor(np.full(op.M * op.N, -123, dtype=bfloat16))
        NPUKernel(artifacts.image, insts)(input_a, packed_b, output)
        got = output.numpy().reshape(op.M, op.N).copy()
        static = gemm(m, op.K, op.N, op.epilogue.value == "gelu").replace(
            bound_values={}
        )
        expected = tensor((m * op.N,), dtype=bfloat16)
        static(tensor(a[:m].reshape(-1)), packed_b, expected)
        np.testing.assert_array_equal(got[:m], expected.numpy().reshape(m, op.N))
        assert np.all(got[m:] == -123), m
