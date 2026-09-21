# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A module of two graphs builds to one image with an entry point per graph.

On NPU2 the fused ELF carries one runtime sequence per graph, named for it,
over shared arenas (spike S4's construction; loading each by name is the
device's half). On NPU1 the per-step chain carries every step of both
graphs, and each entry point runs its own range. The two graphs here share
a weight (the gate projection) and so one buffer.
"""

import subprocess
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2, from_name  # noqa: E402

import iron  # noqa: E402
from iron.common.context import AIEContext  # noqa: E402
from iron.operators.gemv.op import GEMV  # noqa: E402
from iron.operators.silu.op import SiLU  # noqa: E402
from iron.tests.toolchain.full_elf import AIEBU, PEANO  # noqa: E402
from iron.tests.toolchain.xclbin import XCLBINUTIL  # noqa: E402

pytestmark = pytest.mark.skipif(
    PEANO is None or not PEANO.exists(), reason="no Peano (llvm-aie) installed"
)


@pytest.fixture(autouse=True)
def restore_device():
    previous = aie_utils.get_current_device()
    yield
    aie_utils.set_current_device(previous)


def _two_graphs(cols):
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    w_gate, w_up, w_down = z(H, E), z(H, E), z(E, H)
    decode = swiglu_decode(w_gate, w_up, w_down, num_aie_columns=cols)

    @iron.graph
    def gate(x):
        h = GEMV(w_gate, x, num_aie_columns=cols, tile_size_input=4, tile_size_output=H // cols)
        return SiLU(h, num_aie_columns=cols, tile_size=H // cols)

    return decode, gate, E


@pytest.mark.skipif(AIEBU is None, reason="no aiebu-asm on the PATH")
def test_a_module_is_one_elf_with_a_sequence_per_graph(tmp_path):
    aie_utils.set_current_device(NPU2())
    decode, gate, E = _two_graphs(8)
    mod = iron.compile(
        NPU2(),
        context=AIEContext(build_dir=str(tmp_path)),
        decode=(decode, dict(x=(1, E))),
        gate=(gate, dict(x=(1, E))),
    )
    assert mod.plan.image == "elf"
    assert set(mod.graphs) == {"decode", "gate"}
    assert Path(mod.image).suffix == ".elf" and mod.decode.image == mod.image
    symbols = subprocess.run(
        ["readelf", "-s", str(mod.image)], capture_output=True, text=True
    ).stdout
    names = {line.split()[-1] for line in symbols.splitlines() if " OBJECT " in line}
    assert {"decode", "gate"} <= names, sorted(names)
    # One weight buffer for the gate projection, used by both graphs.
    assert len([n for n in mod.sequence.subbuffer_layout if n.startswith("w")]) == 3
    assert mod.sequence.ranges == {"decode": (0, 5), "gate": (5, 7)}
    assert mod.decode._callable is not None and mod.decode._callable.name == "decode"


@pytest.mark.skipif(XCLBINUTIL is None, reason="no xclbinutil on the PATH")
def test_a_module_is_a_per_step_chain_on_npu1(tmp_path):
    dev = from_name("npu1", n_cols=4)
    aie_utils.set_current_device(dev)
    decode, gate, E = _two_graphs(4)
    mod = iron.compile(
        dev,
        context=AIEContext(build_dir=str(tmp_path)),
        decode=(decode, dict(x=(1, E))),
        gate=(gate, dict(x=(1, E))),
    )
    assert mod.plan.image == "xclbin" and mod.plan.dispatch == "separate"
    assert Path(mod.image).suffix == ".xclbin"
    dispatch = mod.sequence._dispatch
    # One kernel per design across both graphs (the gate graph's projection
    # tiles differently from swiglu's, so it is its own design; its SiLU is
    # swiglu's), each graph's steps its own range.
    designs, _ = mod.sequence.unique_designs()
    kernels = {dispatch.op_kernel_name_map[id(op)] for op in mod.sequence.unique_operators()}
    assert len(kernels) == len(designs) == 5
    assert mod.sequence.ranges == {"decode": (0, 5), "gate": (5, 7)}
    assert mod.gate._callable.steps == (5, 7)
