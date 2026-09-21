# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The fused image itself: graph functions build to a full ELF.

One step past ``lowering.py``. Where that gate stops at the instruction
stream, this one runs the whole of aiecc's full-ELF pipeline on a traced
graph: every operator's kernels compile with Peano, every core links, each
design's PDI is generated, and ``aiebu-asm`` assembles the per-device
instruction streams and the PDIs into the one ELF ``xrt::module`` loads.
Needs Peano (the ``llvm-aie`` wheel) and ``aiebu-asm`` on the PATH, and
still no device; the numbers remain hardware's to check.

What it adds to the lowering gate is the scratchpad parameter table:
``--get-scratchpad-parameters`` only emits it on the full-ELF path, and it
is where a graph's bound per-call values become something the host writes
through. The decode graph binds two, so its table must name both.

The swiglu graph goes through ``GraphFunction.compile`` itself, so the one
build also checks the packaging surface end to end: ``compile(dev,
image=)`` derives the dispatch, traces, builds and links the ELF, and the
runtime that would load it is not made until the first call. A build host
with the toolchain and no device compiles ahead of time and hands the
image on.
"""

import shutil
import sys
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
import aie.utils.config as aie_config  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

import iron  # noqa: E402
from iron.common.context import AIEContext  # noqa: E402
from iron.common.jit_compile import compile_sequence, fused_work_dir  # noqa: E402

AIEBU = shutil.which("aiebu-asm")
try:
    PEANO = Path(aie_config.peano_install_dir())
except Exception:  # noqa: BLE001 - any failure means no Peano
    PEANO = None

pytestmark = [
    pytest.mark.skipif(AIEBU is None, reason="no aiebu-asm on the PATH"),
    pytest.mark.skipif(
        PEANO is None or not PEANO.exists(), reason="no Peano (llvm-aie) installed"
    ),
]


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def build_elf(traced, name, tmp_path):
    """Fuse a traced graph and build its full ELF; return the ELF and its work dir."""
    ctx = AIEContext(build_dir=str(tmp_path / "build"))
    seq = traced.sequence(name, dispatch="fused", context=ctx)
    seq.compile()
    elf = compile_sequence(seq, tmp_path / f"{name}.elf")
    assert elf.exists() and elf.stat().st_size > 0, f"no ELF at {elf}"
    return elf, fused_work_dir(elf)


def _params(work_dir):
    """The scratchpad parameter table aiecc emitted, as ``name -> line``."""
    text = (work_dir / "params.txt").read_text().strip().splitlines()
    assert text, "params.txt is empty"
    count = int(text[0])
    rows = [line for line in text[1:] if line.strip()]
    assert len(rows) == count, f"params.txt announces {count} rows, holds {len(rows)}"
    return {row.split()[0]: row for row in rows}


def test_swiglu_decode_graph_compiles_to_a_full_elf(tmp_path):
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    fn = swiglu_decode(z(H, E), z(H, E), z(E, H))
    net = fn.compile(
        NPU2(), image=iron.ELF, context=AIEContext(build_dir=str(tmp_path)), x=(1, E)
    )
    assert net.plan.image == "elf" and net.plan.dispatch == "fused"
    elf = Path(net.image)
    assert elf.suffix == ".elf" and elf.stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    work = fused_work_dir(elf)
    # Four designs (gate and up share one) and the dispatch sequence.
    pdis = sorted(p.name for p in work.glob("bif_op*.bif"))
    assert len(pdis) == 4, pdis
    # No per-call values: an empty table, not a missing one.
    assert (work / "params.txt").read_text().split("\n", 1)[0].strip() == "0"


def test_decode_graph_builds_a_full_elf_with_its_values_in_the_table(tmp_path):
    from iron.tests.common.graph import _Config

    sys.path.insert(0, str(Path("iron/applications/llama_3.2_1b").resolve()))
    from decode_graph import DecodeGraph
    from iron.common.build import value_symbol

    cfg = _Config()
    traced = DecodeGraph(cfg, 256).trace(cfg)
    elf, work = build_elf(traced, "decode", tmp_path)
    table = _params(work)
    # Every value the graph bound is a parameter the host can write.
    for op, name, value in traced.bindings:
        bound = getattr(op, name, None)
        if bound is None or not hasattr(bound, "kind"):
            bound = next(v for v in op.ov.values if v.name == name)
        symbol = value_symbol(op, bound)
        assert symbol in table, f"{symbol} ({value.name}) missing from {sorted(table)}"
