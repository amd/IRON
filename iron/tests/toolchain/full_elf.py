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

from pathlib import Path

import numpy as np
import pytest
from aie.iron import ExternalFunction
from ml_dtypes import bfloat16

import iron
from iron.operators.swiglu_prefill.op import swiglu_prefill
from iron.tests.toolchain.tools import DEVICES, requires, swiglu_decode

pytestmark = [*requires("aiebu", "peano"), pytest.mark.usefixtures("npu2")]


def build_elf(traced, name):
    """Fuse a traced graph and build its full ELF; return its record.

    The one build the application does: ``compile()`` builds the image into
    the JIT cache and records what it consists of.
    """
    seq = traced.sequence(name, dispatch="fused").compile()
    artifacts = seq.artifacts
    elf = Path(artifacts.image)
    assert elf.exists() and elf.stat().st_size > 0, f"no ELF at {elf}"
    assert artifacts.kind == "elf"
    return artifacts


def _params(artifacts):
    """The scratchpad parameter table aiecc emitted, as ``name -> line``."""
    text = artifacts.params.read_text().strip().splitlines()
    assert text, "params.txt is empty"
    count = int(text[0])
    rows = [line for line in text[1:] if line.strip()]
    assert len(rows) == count, f"params.txt announces {count} rows, holds {len(rows)}"
    return {row.split()[0]: row for row in rows}


def test_swiglu_decode_graph_compiles_to_a_full_elf():
    fn, E = swiglu_decode()
    net = fn.compile(DEVICES["npu2"](), image=iron.ELF, x=(1, E))
    assert net.plan.image == "elf" and net.plan.dispatch == "fused"
    assert net.image is not None
    elf = Path(net.image)
    assert elf.suffix == ".elf" and elf.stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    artifacts = net.artifacts
    # Four designs, gate and up sharing one, and one step per runlist entry.
    assert len(artifacts.designs) == 4, artifacts.report("swiglu")
    assert sum(len(d.operators) for d in artifacts.designs) == 5
    assert [s.index for s in artifacts.steps] == list(range(5))
    # No per-call values: an empty table, not a missing one.
    assert artifacts.params is not None
    assert artifacts.params.read_text().split("\n", 1)[0].strip() == "0"


def _assert_values_in_table(traced, artifacts):
    table = _params(artifacts)
    # Every value the graph bound is a parameter the host can write.
    for b in traced.bindings:
        assert (
            b.symbol in table
        ), f"{b.symbol} ({b.value.name}) missing from {sorted(table)}"


def test_decode_graph_builds_a_full_elf_with_its_values_in_the_table():
    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Config as _Config

    cfg = _Config()
    traced = LlamaGraph(cfg, 256).trace(cfg, 1)
    artifacts = build_elf(traced, "decode")
    _assert_values_in_table(traced, artifacts)


@pytest.mark.extensive
def test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer():
    """Every prefill design at Llama 3.2 1B's shape (2048 tokens, 32 heads
    over 8, the 8192-wide FFN) compiles and links into one image. One layer:
    the designs are the same for sixteen, and aiecc's lowering of the fused
    sequence grows with its DMA tasks (about 1,800 per layer against decode's
    430), past this gate's memory at the full depth.
    """
    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Llama1B

    cfg = Llama1B(n_layers=1)
    traced = LlamaGraph(cfg, cfg.context_length).trace(cfg, cfg.context_length)
    assert len(traced.runlist) == 18 + 3
    artifacts = build_elf(traced, "prefill_1b")
    _assert_values_in_table(traced, artifacts)


def test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table():
    from iron.applications.llama_3_2_1b.graphs import LlamaGraph
    from iron.tests.common.llama_model import Config as _Config

    cfg = _Config()
    L = cfg.context_length
    graph = LlamaGraph(cfg, L)
    traced = graph.trace(cfg, L)
    artifacts = build_elf(traced, "prefill")
    _assert_values_in_table(traced, artifacts)


def test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with():
    """A cache hit leaves the kernel registry empty.

    Fusing a sequence runs its designs once outside ``compile()``, for the
    cache key, and ``compile()`` clears the kernels that declared only when it
    generates. On a hit they stayed registered, and the next graph naming one
    of their object files with other flags -- GEMM's ``b_col_maj`` changes its
    flags, not its object name -- raised a collision instead of building.
    """
    M, E, H = 256, 512, 512

    def build(b_col_maj):
        shape = (H, E) if b_col_maj else (E, H)
        z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
        fn = swiglu_prefill(z(*shape), z(*shape), z(*shape[::-1]), b_col_maj=b_col_maj)
        return fn.compile(DEVICES["npu2"](), image=iron.ELF, x=(M, E))

    build(False)
    build(False)  # a hit: compile() generates nothing
    assert not ExternalFunction._instances
    build(True)
