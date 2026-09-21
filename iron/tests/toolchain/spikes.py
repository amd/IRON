# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The build halves of spikes S1 and S4 (OPERATOR_MODEL_PLAN.md §12).

Each spike asks whether an image runs; whether the toolchain can build it
is answerable here and is pinned here. Both start from the swiglu decode
graph's fused module, four configurations and a dispatch sequence.

S1: the fused, multi-configuration sequence as an xclbin image. With
``--expand-load-pdis`` aiecc emits an xclbin for the dispatch device (a
partition, one PDI) and one instruction stream in which every
configuration switch is expanded into writes, alongside an xclbin and a
stream per configuration. Whether that stream configures the array the
partition covers is the device's half.

S4: two runtime sequences in one full ELF. A second ``aie.runtime_sequence``
in the dispatch device builds into the same ELF and its symbol table names
both; the loader already addresses one as ``main:<name>``. Loading each by
name is the device's half.
"""

import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

from iron.common.context import AIEContext  # noqa: E402
from iron.common.jit_compile import compile_sequence, fused_work_dir  # noqa: E402
from iron.tests.toolchain.full_elf import AIEBU, PEANO  # noqa: E402
from iron.tests.toolchain.lowering import AIECC  # noqa: E402
from iron.tests.toolchain.xclbin import XCLBINUTIL  # noqa: E402

pytestmark = pytest.mark.skipif(
    PEANO is None or not PEANO.exists(), reason="no Peano (llvm-aie) installed"
)


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


@pytest.fixture
def fused(tmp_path):
    """The swiglu decode graph's fused module, with its kernel objects built."""
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    traced = swiglu_decode(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    seq = traced.sequence(
        "swiglu_decode", dispatch="fused", context=AIEContext(build_dir=str(tmp_path))
    )
    seq.compile()
    if AIEBU is None:
        pytest.skip("no aiebu-asm on the PATH (the fused build needs it)")
    elf = compile_sequence(seq, tmp_path / "swiglu_decode.elf")
    work = fused_work_dir(elf)
    return work / "aie.mlir", work


def _aiecc(*args, cwd):
    result = subprocess.run(
        [str(AIECC), f"--peano={PEANO}", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=1500,
    )
    assert result.returncode == 0, f"aiecc failed:\n{result.stderr[-3000:]}"


@pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH")
def test_s1_the_fused_sequence_builds_as_an_xclbin_with_its_switches_expanded(
    fused, tmp_path
):
    module, work = fused
    out = tmp_path / "s1"
    out.mkdir()
    for obj in work.glob("*.o"):  # the cores link against the objects by name
        shutil.copy(obj, out)
    shutil.copy(module, out / "fused.mlir")
    _aiecc(
        "--expand-load-pdis",
        "--get-xclbin",
        "--get-npu-insts",
        "--xclbin-name=s1_{0}.xclbin",
        "--npu-insts-name=s1_{0}.bin",
        f"--tmpdir={out / 'prj'}",
        "fused.mlir",
        cwd=out,
    )
    main_xclbin = out / "s1_main.xclbin"
    main_insts = out / "s1_main_sequence.bin"
    assert main_xclbin.stat().st_size > 0 and main_insts.stat().st_size > 0
    per_config = sorted(p.name for p in out.glob("s1_op*_sequence.bin"))
    assert len(per_config) == 4, per_config
    # The expanded stream carries the configurations' writes: far more than
    # the four steps' own streams together.
    own = sum((out / n).stat().st_size for n in per_config)
    assert main_insts.stat().st_size > 4 * own, (main_insts.stat().st_size, own)


def test_s4_two_runtime_sequences_build_into_one_full_elf(fused, tmp_path):
    module, work = fused
    lines = module.read_text().splitlines()
    assert lines[-3:] == ["    }", "  }", "}"], lines[-3:]
    second = [
        "    aie.runtime_sequence @silu_only(%a: memref<8192xbf16>, %b: memref<8192xbf16>) {",
        "      aiex.configure @op1_SiLU {",
        "        aiex.run @sequence(%a, %b) : (memref<8192xbf16>, memref<8192xbf16>)",
        "      }",
        "    }",
    ]
    out = tmp_path / "s4"
    out.mkdir()
    for obj in work.glob("*.o"):
        shutil.copy(obj, out)
    (out / "two.mlir").write_text("\n".join(lines[:-2] + second + lines[-2:]) + "\n")
    _aiecc(
        "--get-full-elf",
        "--full-elf-name=two.elf",
        "--expand-load-pdis",
        "--get-scratchpad-parameters",
        f"--tmpdir={out / 'prj'}",
        "two.mlir",
        cwd=out,
    )
    symbols = subprocess.run(
        ["readelf", "-s", str(out / "two.elf")], capture_output=True, text=True
    ).stdout
    names = {line.split()[-1] for line in symbols.splitlines() if " OBJECT " in line}
    assert {"sequence", "silu_only"} <= names, sorted(names)
