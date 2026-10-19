# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The full ELF itself: graph functions build to a full ELF.

One step past ``lowering.py``. Where that gate stops at the instruction
stream, this one runs the whole of aiecc's full-ELF pipeline on a recorded
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
build also checks the packaging surface end to end: ``compile(dev=,
full_elf=True)`` records, builds and links the ELF, and the
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
from iron.common.graph.record import Recording
from iron.common.image.allocator import BANK
from iron.common.image.sequence import Image
from iron.operators import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.tests.common import sequences
from iron.tests.toolchain.tools import DEVICES, requires, swiglu

pytestmark = [*requires("aiebu", "peano"), pytest.mark.usefixtures("npu2")]


def build_elf(graph, **shapes):
    """Build ``graph``'s full ELF at ``shapes``, as the application does;
    return the version.
    """
    version = graph.compile(full_elf=True, **shapes)
    artifacts = version.artifacts
    elf = Path(artifacts.image)
    assert elf.exists() and elf.stat().st_size > 0, f"no ELF at {elf}"
    assert artifacts.full_elf
    return version


def test_swiglu_graph_compiles_to_a_full_elf():
    fn, E = swiglu()
    net = fn.compile(dev=DEVICES["npu2"](), full_elf=True, x=(1, E))
    assert net.plan.full_elf
    assert net.image is not None
    elf = Path(net.image)
    assert elf.suffix == ".elf" and elf.stat().st_size > 0
    assert net._callable is None, "the runtime is made on first call, not at compile"
    with pytest.raises(ValueError, match=r"input x was compiled for \(1, \d+\)"):
        net(np.zeros((2, E), bfloat16))
    assert net._callable is None, "a refused call makes no runtime"
    artifacts = net.artifacts
    # Four designs, gate and up sharing one, and one step per runlist entry.
    assert len(artifacts.designs) == 4, artifacts.report("swiglu")
    assert sum(len(d.operators) for d in artifacts.designs) == 5
    assert [s.index for s in artifacts.steps] == list(range(5))
    # No per-call values: an empty table, not a missing one.
    assert artifacts.params is not None
    assert artifacts.params.read_text().split("\n", 1)[0].strip() == "0"


def _assert_values_in_table(version):
    table = version.artifacts.parameters
    # The host writes every parameter the image declares ...
    assert {w.symbol for w in version.words} == set(table)
    # ... and every per-call index the graph bound is one, in the word it
    # shares with the symbols that always hold its number. A bound extent
    # the designs read only through its derivations has none of its own.
    for b in version.recording.bindings:
        if b.member.bounds is not None:
            continue
        word = version.shared.get(b.symbol, b.symbol)
        assert (
            word in table
        ), f"{b.symbol} ({b.expression}) missing from {sorted(table)}"


def test_decode_graph_builds_a_full_elf_with_its_values_in_the_table():
    from iron.tests.common.llama_model import small

    model = small(max_seq_len=256)
    version = build_elf(model, **model.shapes()[0])
    _assert_values_in_table(version)
    # A call names every value and no other, refused before the device.
    tensors = [np.zeros(h.shape, h.dtype) for h in version.recording.inputs]
    values = {v.name: 0 for v in version.recording.values}
    with pytest.raises(TypeError, match=r"\['row'\] unknown"):
        version(*tensors, **values, row=0)
    with pytest.raises(TypeError, match=r"per-call values \[.+\] missing"):
        version(*tensors)
    # ... and holds every index in the view it moves along.
    L = model.config.max_seq_len
    with pytest.raises(IndexError, match=rf"position is {L}, outside \[0, {L}\)"):
        version(*tensors, **{**values, "position": L})
    with pytest.raises(IndexError, match=r"token is -1, outside"):
        version(*tensors, **{**values, "token": -1})
    assert version._callable is None


def test_a_scratch_arena_past_a_bank_links_as_its_banks():
    """The scratch arena is passed as its banks, each an argument
    (``ArgumentSizes``): one buffer object each, under the locked-memory
    limit, and each buffer's addend under aiebu's 4 GiB. Llama 3.2 3B's
    weights and caches are 10 GB; as one argument its link failed:
    ``Invalid addend (0x266475800) > 32bit found``.
    """
    add = ElementwiseAdd(size=1024, tile_size=128)
    w = 1024 * 2
    recording = Recording.of_steps(
        "past_a_bank",
        sequences.steps((add, "x", "w", "t"), (add, "t", "w", "out")),
        ["x"],
        ["out"],
        # Buffers no step names, filling the first bank past the weight and
        # most of the second, so t is rebased to the third.
        pinned={"fill": BANK - w, "pad": BANK - 1024},
    )
    seq = Image(recording, full_elf=True)
    seq.compile()
    _, offset, length = seq.layout["t"]
    sizes = seq.buffer_sizes
    assert sizes.bank_kinds == ["scratch", "scratch_1", "scratch_2"]
    assert sizes.scratch_argument(offset, length) == ("scratch_2", offset - 2 * BANK)
    assert Path(seq.artifacts.image).stat().st_size > 0


def test_no_scratch_buffer_crosses_a_bank():
    """A buffer that would end past its bank starts at the next: two 2 GiB
    buffers are the first bank's start and the second's.
    """
    add = ElementwiseAdd(size=1 << 30, tile_size=4096)
    recording = Recording.of_steps(
        "across_a_bank",
        sequences.steps((add, "x", "w", "t"), (add, "t", "w", "out")),
        ["x"],
        ["out"],
    )
    seq = Image(recording, full_elf=True)
    seq.prepare()
    assert [seq.layout[n][1] for n in ("w", "t")] == [0, BANK]


@pytest.mark.extensive
def test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer():
    """Every prefill design at Llama 3.2 1B's shape (2048 tokens, 32 heads
    over 8, the 8192-wide FFN) compiles and links into one image. One layer:
    the designs are the same for sixteen, and aiecc's lowering of the composed
    sequence grows with its DMA tasks (about 1,800 per layer against decode's
    430), past this gate's memory at the full depth.
    """
    from iron.tests.common.llama_model import llama_1b

    model = llama_1b(num_hidden_layers=1)
    version = build_elf(model, **model.shapes()[1])
    # The chunk's embedding rows and RoPE rows, the block, the last row,
    # norm, head and draw.
    assert len(version.recording.steps) == 2 + 18 + 4
    _assert_values_in_table(version)


def test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table():
    from iron.tests.common.llama_model import small

    model = small()
    _assert_values_in_table(build_elf(model, **model.shapes()[1]))


def test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with():
    """A cache hit leaves the kernel registry empty.

    Fusing a sequence runs its designs once outside ``compile()``, for the
    cache key, and ``compile()`` clears the kernels that declared only when it
    generates. On a hit they stayed registered, and the next graph naming one
    of their object files with other flags -- GEMM's ``b_col_maj`` changes its
    flags, not its object name -- raised a collision instead of building.
    """
    M, K, N = 256, 512, 512

    class Project(iron.Graph):
        def __init__(self, b_col_maj):
            self.b_col_maj = b_col_maj
            self.w = np.zeros((N, K) if b_col_maj else (K, N), dtype=bfloat16)

        def body(self, x):
            return GEMM.step(x, self.w, b_col_maj=self.b_col_maj)

    def build(b_col_maj):
        return Project(b_col_maj).compile(
            dev=DEVICES["npu2"](), full_elf=True, x=(M, K)
        )

    build(False)
    # What earlier tests' operator checks declared outside a build stays
    # registered; mlir-aie scopes each compile to its own module's kernels.
    ExternalFunction._instances.clear()
    build(False)  # a hit: compile() generates nothing
    assert not ExternalFunction._instances
    build(True)
