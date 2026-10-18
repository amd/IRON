# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence, device-free.

What the library derives (the split of a buffer over its lanes, and the
round-robin one under a bound) is checked as access patterns; what a
sequence issues is checked in the module a real build generates: each shim
task's lane, buffer argument, offset, sizes, strides and patched size.
"""

import hashlib
import io
import os
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from math import prod
from typing import NamedTuple

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.dialects.aie import DMAChannelDir
from aie.iron import DmaEndpoint, ObjectFifo, Program, Worker
from aie.iron.device import Tile, from_name
from aie.utils import bfp
from aie.utils.trace import TraceConfig
from ml_dtypes import bfloat16

import iron
import iron.operators.flm.gemm.op as flm_gemm
from iron import Scratchpad
from iron.operators.flm.packing import packed_b_size
from iron.common import (
    Chain,
    Extent,
    In,
    Operator,
    Out,
    Value,
    Xclbin,
    Auto,
    Param,
    Built,
    Operand,
    Rtp,
)
from iron.common.design import BuiltArray, OperatorDesign, OperatorRuntime
from iron.common.design.design import configuration
from iron.common.graph.compiled import _words
from iron.common.graph.handle import PerCall
from iron.common.image.packaging import Kind
from iron.operators.clamp import Clamp
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.flm.gemm.design import Epilogue
from iron.tests.common.shipped import Shipped
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.rope import RoPE
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU
from iron.operators.softmax import Softmax
from iron.tests.common.graphs import ProjectAsStored
from iron.tests.common.declare import Rows

# A descriptor's fields are the current device's.
pytestmark = pytest.mark.usefixtures("npu2")

NPU2_4COL = from_name("npu2", n_cols=4)


class MV(Operator):
    M: int = Param()
    K: int = Param()
    num_batches: int | None = Param(default=None)
    cols: int = Auto(default=2)
    tile_out: int = Auto(default=64)
    A = In(num_batches, M, K, obj_type=(tile_out, K), per=(cols,))
    B = In(num_batches, K, obj_type=(K,), broadcast=True)
    C = Out(num_batches, M, obj_type=(tile_out,), per=(cols,))
    valid = Extent(M)

    class Array(Operator.Array):
        K: int
        cols: int
        tile_out: int


class Task(NamedTuple):
    """One shim task of a generated sequence, as its text gives it."""

    ssa: int
    lane: str
    arg: int
    offset: int
    sizes: str
    strides: str
    length_parameter: str  # the patched length's symbol, or ""
    length_unit: str  # the elements per unit of it, or ""
    attributes: str


_TASK = re.compile(
    r"%(\d+) = aiex\.dma_configure_task_for @(\w+) (?:repeat %\w+ : \w+ )?\{\s*"
    r"aie\.dma_bd\(%arg(\d+) : \S+ offset = (\d+) (?:len = %?\w+ )?"
    r"sizes = \[([^\]]*)\] strides = \[([^\]]*)\]\)"
    r"(?: \{length_parameter = @(\w+), length_unit = (\d+) : i32\})?"
    r"\s*aie\.end\s*\}(?: \{([^}]*)\})?"
)
# The graph value a test binds an extent to, as ``x[:n]`` does.
N = PerCall("n", Kind.SCRATCHPAD, np.int32).affine()


def generated_sequence(op, full_elf=True) -> tuple[str, list[Task]]:
    """The runtime sequence ``op`` builds to, and its shim tasks in order.

    An xclbin's per-call values are its dispatch parameters, which only the
    design's generator declares, so it is generated as it would be compiled.
    """
    if full_elf:
        module = OperatorDesign(op).module()
    else:
        module = OperatorDesign(op, full_elf=False).compilable().generate_mlir()
    text = str(module)
    text = text[text.index("aie.runtime_sequence") :]
    tasks = [
        Task(int(ssa), lane, int(arg), int(offset), *rest)
        for ssa, lane, arg, offset, *rest in _TASK.findall(text)
    ]
    return text, tasks


def built(op) -> tuple[str, list[Task], Operator]:
    """``generated_sequence``'s full ELF build, alongside the resolved copy
    of ``op`` whose operands' lanes were bound to build it: a task's
    ``lane`` (an unnamed fifo's mlir-aie-assigned name) is matched back to
    the handle that moved it through this copy.
    """
    array = BuiltArray(OperatorDesign(op))
    prog = Program(
        array.op.device(), OperatorRuntime(array.op, array.built), workers=array.workers
    )
    text = str(prog.resolve_program())
    text = text[text.index("aie.runtime_sequence") :]
    tasks = [
        Task(int(ssa), lane, int(arg), int(offset), *rest)
        for ssa, lane, arg, offset, *rest in _TASK.findall(text)
    ]
    return text, tasks, array.op


# --------------------------------------------------------------------------
# What the library derives: the split and the round-robin
# --------------------------------------------------------------------------


def test_split_takes_every_batch_and_broadcasts():
    op = MV(M=256, K=128, num_batches=100)
    a_transfers = op.A.transfers()
    assert [(lane, word) for lane, _, word, _ in a_transfers] == [
        (0, None),
        (1, None),
    ]
    # Each lane's rows out of every batch: one pattern, however many batches.
    assert a_transfers[1][1] == TensorAccessPattern(
        (100, 256, 128), 128 * 128, [100, 128, 128], [256 * 128, 128, 1]
    )
    ((b_lane, b_tap, _, _),) = op.B.transfers()
    assert b_lane == 0
    assert b_tap == TensorAccessPattern((100 * 128,), 0, [100 * 128], [1])


def test_a_buffer_without_a_stream_has_no_derived_transfers():
    class NoStream(Operator):
        M: int = Param()
        K: int = Param()
        A = In(M, K)
        C = Out(M, obj_type=(64,))

    op = NoStream(M=256, K=128)
    with pytest.raises(ValueError, match="NoStream.A has no obj_type="):
        op.A.transfers()


def test_a_bounded_operand_goes_round_robin_over_the_lanes():
    """Under a bound each lane reads every ``lanes``-th tile from a fixed
    offset, so one patched count serves every lane; the pattern is built
    for the full extent.
    """
    op = Rows(rows=64, cols=8)
    op.use_value("valid", N)
    op = op.resolved(NPU2_4COL)
    word = op.value("valid_x")
    assert op.x.transfers() == [
        (
            0,
            TensorAccessPattern((1, 32, 2, 8), 0, [1, 32, 1, 8], [0, 16, 8, 1]),
            word,
            8,
        ),
        (
            1,
            TensorAccessPattern((1, 32, 2, 8), 8, [1, 32, 1, 8], [0, 16, 8, 1]),
            word,
            8,
        ),
    ]
    # A leading batch axis is the outer repeat; the tile count keeps its slot.
    batched = MV(M=256, K=128, num_batches=3)
    batched.use_value("valid", N)
    batched = batched.resolved(NPU2_4COL)
    (_, tap, word, unit), *_ = batched.A.transfers()
    # The 64 x 128 tile is a run past one wrap, so it takes the two inner
    # slots as 8 x 1024; the tile count sits above them.
    assert tap == TensorAccessPattern(
        (3, 2, 2, 64 * 128),
        0,
        [3, 2, 8, 1024],
        [256 * 128, 2 * 64 * 128, 1024, 1],
    )
    assert word is batched.value("valid_A")
    assert unit == 64 * 128 and batched.M // (2 * 64) == 2


def test_a_bounded_rope_lane_takes_whole_positions_and_their_angles():
    """Under a bound RoPE's input goes round-robin a position at a time (the
    rows one angle row serves), so the lane that rotates a position's heads
    is the one that reads its angle row, and in the same order.
    """
    heads, positions, cols = 4, 16, 64
    op = RoPE(
        rows=heads * positions, cols=cols, angle_rows=positions, num_aie_columns=4
    )
    op.use_value("valid", N)
    op.use_value("valid_angles", PerCall("m", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(from_name("npu2", n_cols=8))
    lanes = op.num_aie_columns
    x = op.x.transfers()
    angles = op.angles.transfers()
    for (xs, xa, _, _), (as_, aa, _, _) in zip(x, angles, strict=True):
        assert xs == as_
        rows = xa.gather(np.arange(prod(xa.tensor_dims)))[::cols] // cols
        angle_rows = aa.gather(np.arange(prod(aa.tensor_dims)))[::cols] // cols
        assert list(angle_rows) == list(range(xs, positions, lanes))
        assert list(rows // heads) == list(np.repeat(angle_rows, heads))


# --------------------------------------------------------------------------
# What a sequence issues, in the generated module
# --------------------------------------------------------------------------


class Words(Operator):
    """A core reading a word, a block of three, a word, and one per call."""

    n: int = Param()
    tile: int = Auto(default=64)
    A = In(n, obj_type=(tile,))
    first = Value(derive=lambda op: 7)
    block = Value(derive=lambda op: [11, 12, 13], words=3)
    last = Value(derive=lambda op: op.n // op.tile)
    pos = Value()

    class Array(Operator.Array):
        tile: int
        A: Operand
        first: Value
        block: Value
        last: Value
        pos: Value

        def build(self) -> Built:
            fifo = ObjectFifo(self.A.obj_type)
            self.A.bind(fifo.prod())
            rtp = Rtp([self.first, self.block, self.last, self.pos])

            def core(of, rtp):
                rtp.read()
                of.acquire(1)
                of.release(1)

            return Built([Worker(core, [fifo.cons(), rtp])], [rtp])


def rtp_writes(text: str) -> list[tuple[int, int | str]]:
    """Each ``aiex.npu.rtp_write`` of a module's sequence: its slot, and the
    constant it writes or the sequence argument.
    """
    sequence = text[text.index("aie.runtime_sequence") :]
    constants = dict(re.findall(r"(%\w+) = arith.constant (-?\d+) : i32", sequence))
    return [
        (int(slot), int(constants[word]) if word in constants else word)
        for slot, word in re.findall(
            r"aiex.npu.rtp_write\(@\w+, (\d+), (%\w+)\)", sequence
        )
    ]


def test_a_value_only_a_core_reads_is_declared_on_a_full_elf(npu2):
    text = str(OperatorDesign(Words(n=64)).module())
    (symbol,) = re.findall(r"aiex.scratchpad_parameter @(\w+)", text)
    core = text[text.index("aie.core(") : text.index("aie.runtime_sequence")]
    assert f"aiex.read_scratchpad_parameter @{symbol}" in core


def test_the_slots_after_a_multi_word_value_follow_its_words(npu2):
    """The block takes slots 1 to 3, so ``last`` is slot 4; on an xclbin the
    per-call word is the dispatch argument, in slot 5.
    """
    text = str(OperatorDesign(Words(n=64)).module())
    assert "memref<5xi32>" in text
    assert rtp_writes(text) == [(0, 7), (1, 11), (2, 12), (3, 13), (4, 1)]
    xclbin = str(
        OperatorDesign(Words(n=64), full_elf=False).compilable().generate_mlir()
    )
    assert "memref<6xi32>" in xclbin
    assert rtp_writes(xclbin)[-2:] == [(4, 1), (5, "%arg1")]


def test_mha_infers_the_padded_length_and_the_kv_head_count():
    inputs, _, _ = MHA.declaration.call_operands(
        ((8, 128, 64), (2, 128, 64), (2, 128, 64)), {}
    )
    op = MHA(**MHA.declaration.infer(inputs))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match="seq_pad=100"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


def test_mha_binds_p_times_v_at_its_own_shape():
    """Away from B_kv = d, P*V's operands are not QK^T's: P is (B_q, B_kv), V
    (B_kv, d) and O (B_q, d), each streamed as P*V takes it, O accumulated
    in float32 and rounded once into the bf16 output.
    """
    op = MHA(num_heads=1, seq_len=1024, d=128, num_pipelines=8, B_q=32)
    text = str(OperatorDesign(op.resolved(from_name("npu2", n_cols=8))).module())
    p, v = "memref<32x32xbf16>", "memref<32x128xbf16>"
    acc, o = "memref<32x128xf32>", "memref<32x128xbf16>"
    assert re.search(rf'_matmul_PV"?\({p}, {v}, {acc},', text)
    assert re.search(rf'_rescale_O"?\({acc}, {o},', text)


# --------------------------------------------------------------------------
# A per-call size in a transfer
# --------------------------------------------------------------------------


def _bounded_gemv():
    # A patched length is whole 16-byte units: an output tile of 8 bf16 rows.
    op = GEMV(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=8)
    op.use_value("valid", N)  # what a graph does for A[:n]
    return op


def test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin():
    """Under a bound on M, C's drains go first; then each lane's A stream
    takes B, whole, as one input tile, and A in output tiles (four input
    tiles each here) round-robin, C in the same tiles, both patched by the
    tile count the core also reads.
    """
    op = _bounded_gemv().resolved(from_name("npu2", n_cols=8))
    assert [v.name for v in op.values] == ["valid", "tiles", "valid_A", "valid_C"]
    assert op.derived_at("tiles", valid=64) == 64 // (2 * 8)
    assert op.derived_at("valid_A", valid=64) == 64 // (2 * 8)  # unit: output tiles
    text, tasks, op = built(op)
    # The fifos are unnamed (mlir-aie's DeviceConfiguration names them), so a
    # task is identified by the handle it was built from, not a literal name.
    c0, c1 = (h.name for h in op.C.handles)
    a0, a1 = (h.name for h in op.A.handles)
    assert [
        (
            t.lane,
            t.offset,
            t.sizes,
            t.strides,
            t.length_parameter.endswith(("_A", "_C")),
        )
        for t in tasks
    ] == [
        (c0, 0, "1, 16, 1, 8", "0, 16, 8, 1", True),
        (c1, 8, "1, 16, 1, 8", "0, 16, 8, 1", True),
        (a0, 0, "2, 1, 1, 64", "0, 0, 0, 1", False),
        (a0, 0, "1, 16, 1, 512", "0, 1024, 512, 1", True),
        (a1, 0, "2, 1, 1, 64", "0, 0, 0, 1", False),
        (a1, 512, "1, 16, 1, 512", "0, 1024, 512, 1", True),
    ]
    assert {t.length_parameter[-7:] for t in tasks if t.length_parameter} == {
        "valid_A",
        "valid_C",
    }
    assert text.count("aiex.scratchpad_parameter @") == 2


def test_on_an_xclbin_the_size_is_the_dispatch_scalar():
    # No scratchpad to patch: the sequence is regenerated per call, the
    # per-call scalar standing in for the size itself.
    text, tasks = generated_sequence(_bounded_gemv(), full_elf=False)
    assert "scratchpad_parameter" not in text
    # %arg1 is B, the head of each A stream, whose size no call bounds; the
    # fifos are unnamed (mlir-aie's DeviceConfiguration names them), so a
    # lane is identified by its argument and offset, not a literal name.
    bounded = [t for t in tasks if t.arg != 1]
    assert [(t.arg, t.offset, t.length_parameter) for t in bounded] == [
        (2, 0, ""),
        (2, 8, ""),
        (0, 0, ""),
        (0, 512, ""),
    ]
    for t, run in zip(bounded, (8, 8, 512, 512), strict=True):
        assert re.fullmatch(rf"1, %\w+, 1, {run}", t.sizes), t.sizes


def test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it(npu2):
    """A regenerated stream sizes any dimension per call, not only the
    outermost below the iteration a patched descriptor's length ends at:
    here the rows' length, the innermost.
    """
    cache = iron.state((16, 4, 256), name="cache")

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32], pos: Scratchpad[np.int32]):
            Copy.step(Softmax.step(x[:, :n]), cache[:, pos])

    t = G().trace(x=(16, 256))
    (op,) = [o for o in t.operators if isinstance(o, Copy)]
    text, _ = generated_sequence(op.resolved(), full_elf=False)
    bds = re.findall(r"aie\.dma_bd\(%arg(\d) .*sizes = \[([^\]]*)\]", text)
    assert [(int(arg), re.sub(r"%\d+", "n", sizes)) for arg, sizes in bds] == [
        (0, "1, 1, 16, n"),
        (1, "1, 1, 16, n"),
    ]


@pytest.mark.parametrize(
    "length, error, match",
    [
        (
            lambda op: dict(length_parameter=op.value("valid_A"), length_unit=3),
            ValueError,
            "no descriptor dimension",
        ),
        (
            lambda op: dict(length_parameter=32, length_unit=64),
            TypeError,
            "value member",
        ),  # not a word
    ],
    ids=["no_dimension_of_the_unit", "not_a_word"],
)
def test_a_per_call_length_counts_a_dimension_by_a_word(length, error, match):
    class Patched(GEMV):
        def sequence(self, rt):
            self.A.fill(lane=0, **length(self))

    op = Patched(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=4)
    op.use_value("valid", N)
    with pytest.raises(error, match=match):
        OperatorDesign(op).module()


# --------------------------------------------------------------------------
# flm/gemm: the configuration/shape split, device-free
# --------------------------------------------------------------------------


def test_flm_gemm_keyword_construction_tunes_from_the_device():
    # Keyword construction leaves every tunable to resolution, which reads the
    # device alone; the operator's extent is checked against the resolved
    # tunables by compatible(), not folded into its defaults.
    assert flm_gemm.GEMM(M=512, K=1024, N=1024).tile_n is None
    op = flm_gemm.GEMM(M=512, K=1024, N=1024).resolved(from_name("npu2", n_cols=8))
    assert (op.tile_n, op.m_chunk, op.rows, op.cols, op.bfp16_b) == (64, 1, 4, 8, True)
    assert (
        op.tile_ma
        == flm_gemm._default_l1(64, 128, bfp.BLOCK_BYTES / bfp.BLOCK, 65536, 1)[0]
    )
    # tile_n is resolution, not a function of K: the same on every shape.
    assert (
        flm_gemm.GEMM(M=256, K=512, N=1024).resolved(from_name("npu2", n_cols=8)).tile_n
        == 64
    )
    assert (
        op.config_name
        == f"FLM_GEMM_tn64_kt512_ck128_ma{op.tile_ma}_mc1_emf_conv_even_npu2"
    )
    assert op.name == op.config_name + "_M512_K1024_N1024"
    a, b, c = op.buffers
    assert a.shape == (512, 1024) and c.shape == (512, 1024)
    # B is declared in bfp16ebs8 blocks; the host holds the same bytes as uint8.
    assert b.shape == (1024 * 1024 // 8,) and b.dtype is v8bfp16ebs8
    assert b.host_shape == (packed_b_size(1024, 1024, True),)
    assert b.host_dtype is np.uint8
    assert op.residents == {
        "n_val": 1024,
        "m_row_blocks": 2,
        "k_iters": 2,
        "mode": 0,
        "clamp_min": int(np.float32(-np.inf).view(np.int32)),
        "clamp_max": int(np.float32(np.inf).view(np.int32)),
        "n_units": 2,
        "units_valid": 2,
        "units_repeat": 1,
    }
    with pytest.raises(ValueError, match="multiple of 256"):
        flm_gemm.GEMM(M=100, K=1024, N=1024).resolved(
            from_name("npu2", n_cols=8)
        )  # M tiles to the array's rows
    with pytest.raises(ValueError, match="not in epilogue_modes"):
        flm_gemm.GEMM(M=256, K=1024, N=1024, epilogue="gelu", epilogue_modes=("none",))


def test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills():
    """At N=256 a shape's sequence fills B through columns 0-3 alone; the
    pool of every column is still declared, so the shape's build lays out
    the same static design as the configuration image it runs on, and its
    descriptors address the image's memtile buffers.
    """
    name = re.compile(
        r'@[\w$.]+|%[\w$.]+|sym_name = "[^"]*"|\^bb\d+|fifoName = "[^"]*"'
    )

    def static(op) -> list[str]:
        text = str(OperatorDesign(op, full_elf=False).compilable().generate_mlir())
        text = text[: text.index("aie.runtime_sequence")]
        return sorted(name.sub("_", line).strip() for line in text.splitlines())

    dev = from_name("npu2", n_cols=8)
    op = flm_gemm.GEMM(M=512, K=1536, N=256, tile_n=64, k_tile=256).resolved(dev)
    assert static(op) == static(op.configuration())


def test_flm_gemm_layout_of_b_follows_the_device():
    untuned = flm_gemm.GEMM(M=256, K=512, N=512)
    with pytest.raises(ValueError):
        [b.shape for b in untuned.buffers]  # B's layout follows the device
    assert untuned.resolved(from_name("npu2", n_cols=8)).B.shape == (512 * 512 // 8,)


def test_flm_gemm_finishes_with_an_activation_then_a_clamp_in_its_epilogue():
    op = flm_gemm.GEMM(M=256, K=512, N=512)
    size = 256 * 512
    silu = op.fold(SiLU(size=size))
    assert silu.activation is Epilogue.SILU and silu.clamp is None
    clamped = silu.fold(Clamp(size=size, low=-0.7, high=2.0))
    assert clamped.clamp == (float(bfloat16(-0.7)), 2.0)
    assert clamped.config_name == op.config_name
    assert clamped.resolved().residents["mode"] == Epilogue.SILU.mode
    # Its gelu is not the GELU operator's, nothing follows its clamp, it
    # applies one activation, and a step finishes nothing of its own.
    finished = SiLU(size=size, finish=Chain.of(ElementwiseMul(size=size)))
    for refused in (
        op.fold(GELU(size=size)),
        clamped.fold(Clamp(size=size, low=0.0, high=1.0)),
        silu.fold(Sigmoid(size=size)),
        op.fold(finished),
        flm_gemm.GEMM(M=256, K=512, N=512, epilogue="gelu").fold(SiLU(size=size)),
    ):
        with pytest.raises(ValueError, match="epilogue applies|one activation"):
            refused.resolved()
    with pytest.raises(ValueError, match="as a finish step"):
        flm_gemm.GEMM(M=256, K=512, N=512, epilogue="silu")
    assert silu.epilogue_modes == op.epilogue_modes
    plain = flm_gemm.GEMM(M=256, K=512, N=512, epilogue_modes=("none",))
    compiled_in = plain.fold(SiLU(size=size))
    assert compiled_in.compiled_modes == (Epilogue.NONE, Epilogue.SILU)
    assert plain.compiled_modes == (Epilogue.NONE,)
    # The xclbin is the configuration's, which compiles in what the finish needs.
    config = compiled_in.resolved().configuration()
    assert config.epilogue_modes == compiled_in.compiled_modes


def _flm_gemm_moves(op, full_elf, rows):
    """Bytes each operand of ``op``'s sequence moves in a call whose row bound
    is ``rows``: each shim task's elements, a patched length its word's value
    in its units, times its runs, a repeat parameter's word plus one. On an
    xclbin the one per-call scalar a size takes is the units the bound
    reaches, and a runtime outer size is the task's repeat.
    """
    words = {
        v.symbol: op.derived_at(v.name, valid=rows)
        for v in op.values
        if v.name != "valid"
    }
    units = words.get(op.value("units_valid").symbol)
    text, tasks = generated_sequence(op, full_elf)
    repeats = dict(
        re.findall(
            r"aiex\.dma_start_task\(%(\d+)\) \{repeat_parameter = @(\w+)\}", text
        )
    )
    moved = dict.fromkeys((b.name for b in op.buffers), 0)
    for t in tasks:
        sizes = [units if s.startswith("%") else int(s) for s in t.sizes.split(", ")]
        elements = prod(sizes[1:])
        if t.length_parameter:
            elements = words[t.length_parameter] * int(t.length_unit)
        repeat = re.search(r"repeat_count = (\d+)", t.attributes)
        runs = 1 + int(repeat[1]) if repeat else 1
        if str(t.ssa) in repeats:
            runs = 1 + words[repeats[str(t.ssa)]]
        elif t.sizes.startswith("%"):
            runs = units
        buffer = op.buffers[t.arg]
        moved[buffer.name] += elements * runs * bfp.itemsize(buffer.dtype)
    return moved


@pytest.mark.parametrize("image", ["elf", "xclbin"])
@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches(
    device, image, request
):
    """Llama's q projection on a 15-row prompt chunk moves A and C for one
    unit, the 256 rows its four core rows join into a C block, and at 2048
    rows for all eight, as it does unbounded. B moves the same at any bound,
    and A once per column block, as unbounded.
    """
    dev = request.getfixturevalue(device)
    M = K = width = 2048
    unbounded = flm_gemm.GEMM(M=M, K=K, N=width, b_col_maj=True).resolved(dev)
    op = flm_gemm.GEMM(M=M, K=K, N=width, b_col_maj=True)
    op.use_value("valid", N)
    op = op.resolved(dev)
    blocks = width // (op.tile_n * op.cols)
    full_elf = image == "elf"
    whole = _flm_gemm_moves(unbounded, full_elf, M)
    for rows, units in ((15, 1), (256, 1), (257, 2), (2048, 8)):
        assert _flm_gemm_moves(op, full_elf, rows) == {
            "A": units * 256 * K * 2 * blocks,
            "B": whole["B"],
            "C": units * 256 * width * 2,
        }, rows
    assert _flm_gemm_moves(op, full_elf, M) == whole


def test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar(npu1):
    # No scratchpad: A's units are the repeat count of one task per row and
    # column block, C's row blocks its D2, both the per-call scalar.
    op = flm_gemm.GEMM(M=512, K=1024, N=512, b_col_maj=True)
    op.use_value("valid", N)
    _, tasks = generated_sequence(op.resolved(npu1), full_elf=False)
    a = [t.sizes for t in tasks if t.arg == 0]
    c = [t.sizes for t in tasks if t.arg == 2]
    assert len(a) == 2 * 4 and len(c) == 2 * 4  # two column blocks
    assert all(re.fullmatch(r"%\w+, 2, 64, 512", s) for s in a), a
    assert all(re.fullmatch(r"1, %\w+, 256, 64", s) for s in c), c


def test_a_bounded_flm_gemm_refuses_a_call_with_no_rows(npu2):
    """The cores drain the B replays past the bound before the units it
    reaches, so the last C ends the call; with no units there is no C to
    wait on, and the call is refused as it writes its words, before it is
    dispatched.
    """
    traced = ProjectAsStored().trace(x=(512, 512), w=(512, 512))
    words, _ = _words(traced)
    assert [w({"n": 1}) for w in words if w.symbol.endswith("units_valid")] == [1]
    with pytest.raises(ValueError, match="at least one row, got 0"):
        [w({"n": 0}) for w in words]


def test_a_row_bound_needs_one_row_block_per_unit():
    op = flm_gemm.GEMM(M=512, K=512, N=512, b_col_maj=True, m_chunk=2)
    op.use_value("valid", N)
    with pytest.raises(ValueError, match="row bound needs m_chunk=1"):
        op.resolved(from_name("npu2", n_cols=8))


# --------------------------------------------------------------------------
# flm.gemm.Shipped: the sequence for a shipped image, device-free
# --------------------------------------------------------------------------


def test_a_shipped_image_declares_its_pins_and_parameter_block():

    op = Shipped(M=256, K=1024, N=1152)
    assert op.external.filename == "flm_mm_f81eba71.xclbin"
    # Its Array.build() pins each lane to the image's shim channel, places each
    # core's parameter block and the lock that releases it.
    text = str(OperatorDesign(op.resolved(), full_elf=False).module())
    pins = re.findall(r"shim_dma_allocation @(\w+)\(%\w+, (\w+), (\d)\)", text)
    assert pins[:5] == [
        ("A_0", "MM2S", "0"),
        ("A_1", "MM2S", "0"),
        ("A_2", "MM2S", "0"),
        ("A_3", "MM2S", "0"),
        ("B_0", "MM2S", "1"),
    ]
    assert len(pins) == 4 + 8 + 8
    cores = 4 * 8
    assert text.count('{address = 4096 : i32, sym_name = "rtp_') == cores
    assert len(re.findall(r"aie\.lock\(%\w+, 10\)", text)) == cores

    image = Xclbin(url="u", sha256="s", filename="f")
    # A stream built once per shape takes no per-call value.
    with pytest.raises(TypeError, match="takes no per-call value"):

        class Unbuilt(Operator, image=image):
            n: int = Param()
            x = In(n, obj_type=(64,))
            count = Value()


def test_a_lane_pins_to_a_channel_moving_its_way():
    class Pinned(Operator):
        n: int = Param()
        c: int = Auto(default=2)
        x = In(n, obj_type=(n,))
        y = Out(n, obj_type=(n,), per=(c,))

        class Array(Operator.Array):
            n: int
            c: int

    op = Pinned(n=2)
    shims = [Tile(c, 0) for c in range(2)]
    with pytest.raises(ValueError, match="moves"):
        op.x.pin([DmaEndpoint(shims[0], DMAChannelDir.S2MM, 0)])
    with pytest.raises(ValueError, match="2 lanes"):
        op.y.pin([DmaEndpoint(shims[0], DMAChannelDir.S2MM, 0)])
    op.y.pin([DmaEndpoint(tile, DMAChannelDir.S2MM, 0) for tile in shims])
    assert [end.tile for end in op.y.handles] == shims


def test_a_shipped_image_runs_only_with_instructions(tmp_path):
    insts = tmp_path / "insts.bin"
    image = Xclbin(url="u", sha256="s", filename="f", kernel_name="K")
    with pytest.raises(TypeError, match="no instructions"):
        image()
    run = image.with_instructions(insts, dispatch_params=None)
    assert (run.insts_path, run.kernel_name, run.filename) == (insts, "K", "f")
    assert run.with_instructions(insts, kernel_name="L").kernel_name == "L"


def test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file(tmp_path):
    image = Shipped(M=256, K=1024, N=1152).external
    with ThreadPoolExecutor(8) as pool:
        paths = list(pool.map(lambda _: image.fetch(tmp_path), range(8)))
    assert set(paths) == {tmp_path / image.filename}
    with open(paths[0], "rb") as f:
        assert hashlib.file_digest(f, "sha256").hexdigest() == image.sha256
    assert [p.name for p in tmp_path.iterdir()] == [image.filename]


def test_one_configuration_traces_at_one_size():
    arrays = {
        name: BuiltArray(OperatorDesign(op, full_elf=False))
        for name, op in (
            ("gelu", GELU(size=4096, trace=TraceConfig(4096))),
            ("sigmoid", Sigmoid(size=4096, trace=TraceConfig(8192))),
        )
    }
    with pytest.raises(ValueError, match=r"trace sizes \[4096, 8192\]"):
        configuration("both", arrays)


def test_a_failed_fetch_leaves_no_partial_file(tmp_path, monkeypatch):
    content = b"image"
    image = Xclbin(
        url="https://example.invalid/f",
        sha256=hashlib.sha256(content).hexdigest(),
        filename="f",
    )
    monkeypatch.setattr(
        urllib.request, "urlopen", lambda url, timeout: io.BytesIO(content)
    )

    def full(fd, mode):
        raise OSError("disk full")

    monkeypatch.setattr(os, "fchmod", full)
    with pytest.raises(OSError, match="disk full"):
        image.fetch(tmp_path)
    assert list(tmp_path.iterdir()) == []
