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

import pytest
from aie.iron.device import NPU2

import iron
from iron.common.context import AIEContext
from iron.tests.toolchain.tools import requires, swiglu_decode

pytestmark = [*requires("aiebu", "peano"), pytest.mark.usefixtures("npu2")]


def build_elf(traced, name, tmp_path):
    """Fuse a traced graph and build its full ELF; return its record.

    The one build the application does: ``compile()`` builds the image into
    the JIT cache and records what it consists of."""
    ctx = AIEContext(build_dir=str(tmp_path / "build"))
    seq = traced.sequence(name, dispatch="fused", context=ctx).compile()
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


def test_swiglu_decode_graph_compiles_to_a_full_elf(tmp_path):
    fn, E = swiglu_decode()
    net = fn.compile(
        NPU2(), image=iron.ELF, context=AIEContext(build_dir=str(tmp_path)), x=(1, E)
    )
    assert net.plan.image == "elf" and net.plan.dispatch == "fused"
    elf = Path(net.image)
    assert elf.suffix == ".elf" and elf.stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    artifacts = net.artifacts
    # Four designs, gate and up sharing one, and one step per runlist entry.
    assert len(artifacts.designs) == 4, artifacts.report("swiglu")
    assert sum(len(d.operators) for d in artifacts.designs) == 5
    assert [s.index for s in artifacts.steps] == list(range(5))
    # No per-call values: an empty table, not a missing one.
    assert artifacts.params.read_text().split("\n", 1)[0].strip() == "0"


def _assert_values_in_table(traced, artifacts):
    from iron.common.build import value_symbol

    table = _params(artifacts)
    # Every value the graph bound is a parameter the host can write.
    for op, name, value in traced.bindings:
        bound = getattr(op, name, None)
        if bound is None or not hasattr(bound, "kind"):
            bound = next(v for v in op.ov.values if v.name == name)
        symbol = value_symbol(op, bound)
        assert symbol in table, f"{symbol} ({value.name}) missing from {sorted(table)}"


def test_decode_graph_builds_a_full_elf_with_its_values_in_the_table(tmp_path):
    from iron.tests.common.llama_model import Config as _Config

    from iron.models.llama_graphs import DecodeGraph

    cfg = _Config()
    traced = DecodeGraph(cfg, 256).trace(cfg)
    artifacts = build_elf(traced, "decode", tmp_path)
    _assert_values_in_table(traced, artifacts)


@pytest.mark.extensive
def test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer(tmp_path):
    """Every prefill design at Llama 3.2 1B's shape (2048 tokens, 32 heads
    over 8, the 8192-wide FFN) compiles and links into one image. One layer:
    the designs are the same for sixteen, and aiecc's lowering of the fused
    sequence grows with its DMA tasks (about 1,800 per layer against decode's
    430), past this gate's memory at the full depth."""
    from iron.tests.common.llama_model import Llama1B

    from iron.models.llama_graphs import DecodeGraph, PrefillGraph

    cfg = Llama1B()
    cfg.n_layers, cfg.model.layers = 1, cfg.model.layers[:1]
    decode = DecodeGraph(cfg, cfg.context_length)
    traced = PrefillGraph(cfg, decode).trace(cfg)
    assert len(traced.runlist) == 18 + 3
    artifacts = build_elf(traced, "prefill_1b", tmp_path)
    _assert_values_in_table(traced, artifacts)


def test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table(tmp_path):
    from iron.tests.common.llama_model import Config as _Config

    from iron.models.llama_graphs import DecodeGraph, PrefillGraph

    cfg = _Config()
    decode = DecodeGraph(cfg, cfg.context_length, num_aie_columns=4)
    traced = PrefillGraph(cfg, decode, num_of_pipelines=1, tile_m=16).trace(cfg)
    artifacts = build_elf(traced, "prefill", tmp_path)
    _assert_values_in_table(traced, artifacts)
