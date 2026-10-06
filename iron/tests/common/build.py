# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence, device-free.

What the library derives (the split of a buffer over its lanes, and the
round-robin one under a bound) is checked as access patterns; what a
sequence issues is checked in the module a real build generates: each shim
task's lane, buffer argument, offset, sizes, strides, patched size and
whether it is waited on.
"""

import dataclasses
import re
from math import prod
from typing import NamedTuple

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron.device import from_name

import iron.operators.flm.gemm.op as flm_gemm
from iron.common import (
    DeclarationError,
    In,
    Operator,
    Out,
    Shim,
    Value,
    Xclbin,
    auto,
    optional,
    param,
)
from iron.common.design import (
    OperatorDesign,
    Sequence,
    Target,
    build_design,
)
from iron.operators import ElementwiseAdd
from iron.operators.flm.gemm.shipped import Shipped
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.repeat import Repeat
from iron.operators.rope import RoPE
from iron.tests.common.declare import Rows

# A descriptor's fields are the current device's.
pytestmark = pytest.mark.usefixtures("npu2")

NPU2_4COL = from_name("npu2", n_cols=4)


class Unary(Operator):
    size: int = param()
    tile: int = auto(1024)
    cols: int = auto()
    chans: int = auto(2)
    A = In(size, tile=(tile,), per=(cols, chans))
    B = Out(size, tile=(tile,), per=(cols, chans))

    def resolve(self, dev):

        return dataclasses.replace(self, cols=self.cols or dev.cols)


class MV(Operator):
    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    cols: int = auto(2)
    tile_out: int = auto(64)
    A = In(optional(num_batches), M, K, tile=(tile_out, K), per=(cols,))
    B = In(optional(num_batches), K, tile=(K,), broadcast=True)
    C = Out(optional(num_batches), M, tile=(tile_out,), per=(cols,))


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

    @property
    def waited(self) -> bool:
        return "issue_token = true" in self.attributes


_TASK = re.compile(
    r"%(\d+) = aiex\.dma_configure_task_for @(\w+) \{\s*"
    r"aie\.dma_bd\(%arg(\d+) : \S+ offset = (\d+) (?:len = %?\w+ )?"
    r"sizes = \[([^\]]*)\] strides = \[([^\]]*)\]\)"
    r"(?: \{length_parameter = @(\w+), length_unit = (\d+) : i32\})?"
    r"\s*aie\.end\s*\}(?: \{([^}]*)\})?"
)
_WRITE = re.compile(r"aiex\.npu\.rtp_write\(@rtp_(\d+)_(\d+), (\d+), %c(-?\d+)_i32")


def generated_sequence(op, image="elf") -> tuple[str, list[Task]]:
    """The runtime sequence ``op`` builds to, and its shim tasks in order.

    An xclbin's per-call values are its dispatch parameters, which only the
    design's generator declares, so it is generated as it would be compiled.
    """
    if image == "elf":
        module = build_design(op)
    else:
        design = OperatorDesign(op, image)
        module = design.compilable().generate_mlir()
    text = str(module)
    text = text[text.index("aie.runtime_sequence") :]
    tasks = [
        Task(int(ssa), lane, int(arg), int(offset), *rest)
        for ssa, lane, arg, offset, *rest in _TASK.findall(text)
    ]
    return text, tasks


def _awaited(text) -> list[int]:
    return [int(t) for t in re.findall(r"aiex\.dma_await_task\(%(\d+)\)", text)]


# --------------------------------------------------------------------------
# What the library derives: the split and the round-robin
# --------------------------------------------------------------------------


def test_split_gives_each_lane_its_block():
    op = Unary(size=8192).resolved(NPU2_4COL)
    p = Sequence.split(op.A, op.streams["A"])
    assert len(p) == 8  # 4 columns x 2 channels
    chunk = 8192 // 8
    for i, (slot, tap) in enumerate(p):
        assert slot.index == i
        assert tap == TensorAccessPattern((8192,), chunk * i, [chunk], [1])


def test_split_takes_every_batch_and_broadcasts():
    op = MV(M=256, K=128, num_batches=100)
    a_transfers = Sequence.split(op.A, op.streams["A"])
    assert [slot.index for slot, _ in a_transfers] == [0, 1]
    # Each lane's rows out of every batch: one pattern, however many batches.
    assert a_transfers[1][1] == TensorAccessPattern(
        (100, 256, 128), 128 * 128, [100, 128, 128], [256 * 128, 128, 1]
    )
    ((b_slot, b_tap),) = Sequence.split(op.B, op.streams["B"])
    assert b_slot is op.streams["B"]
    assert b_tap == TensorAccessPattern((100 * 128,), 0, [100 * 128], [1])


def test_a_buffer_without_a_stream_has_no_derived_transfers():
    class NoStream(Operator):
        M: int = param()
        K: int = param()
        A = In(M, K)
        C = Out(M, tile=(64,))

    op = NoStream(M=256, K=128)
    with pytest.raises(ValueError, match="NoStream.A has no tile="):
        Sequence(op, {}).plan(op.A)


def test_a_bounded_operand_goes_round_robin_over_the_lanes():
    """Under a bound each lane reads every ``lanes``-th tile from a fixed
    offset, so one patched count serves every lane; the pattern is built
    for the full extent.
    """
    op = Rows(rows=64, cols=8).resolved(NPU2_4COL)
    plan = Sequence.round_robin(op.x, op.streams["x"], 0)
    assert [(slot.index, tap, dim) for slot, tap, dim in plan] == [
        (0, TensorAccessPattern((1, 32, 2, 8), 0, [1, 32, 1, 8], [0, 16, 8, 1]), 1),
        (1, TensorAccessPattern((1, 32, 2, 8), 8, [1, 32, 1, 8], [0, 16, 8, 1]), 1),
    ]
    # A leading batch axis is the outer repeat; the tile count keeps its slot.
    batched = MV(M=256, K=128, num_batches=3).resolved(NPU2_4COL)
    (slot, tap, dim), *_ = Sequence.round_robin(batched.A, batched.streams["A"], 1)
    # The 64 x 128 tile is a run past one wrap, so it takes the two inner
    # slots as 8 x 1024; the tile count sits above them.
    assert tap == TensorAccessPattern(
        (3, 2, 2, 64 * 128),
        0,
        [3, 2, 8, 1024],
        [256 * 128, 2 * 64 * 128, 1024, 1],
    )
    assert dim == 1 and (batched.M // (2 * 64)) == 2


def test_a_bounded_rope_lane_takes_whole_positions_and_their_angles():
    """Under a bound RoPE's input goes round-robin a position at a time (the
    rows one angle row serves), so the lane that rotates a position's heads
    is the one that reads its angle row, and in the same order.
    """
    heads, positions, cols = 4, 16, 64
    op = RoPE(
        rows=heads * positions, cols=cols, angle_rows=positions, num_aie_columns=4
    )
    op = op.resolved(from_name("npu2", n_cols=8))
    lanes = op.num_aie_columns
    x = Sequence.round_robin(op.x, op.streams["x"], 0)
    angles = Sequence.round_robin(op.angles, op.streams["angles"], 0)
    for (xs, xa, _), (as_, aa, _) in zip(x, angles, strict=True):
        assert xs.index == as_.index
        rows = xa.gather(np.arange(prod(xa.tensor_dims)))[::cols] // cols
        angle_rows = aa.gather(np.arange(prod(aa.tensor_dims)))[::cols] // cols
        assert list(angle_rows) == list(range(xs.index, positions, lanes))
        assert list(rows // heads) == list(np.repeat(angle_rows, heads))


# --------------------------------------------------------------------------
# What a sequence issues, in the generated module
# --------------------------------------------------------------------------


def test_derived_sequence_issues_fills_then_waited_drains():
    op = ElementwiseAdd(size=8192, num_aie_columns=2, tile_size=1024)
    assert not ElementwiseAdd.has_sequence_override()
    text, tasks = generated_sequence(op)
    whole = ("1, 1, 1, 4096", "0, 0, 0, 1")
    assert [
        (t.lane, t.arg, t.offset, (t.sizes, t.strides), t.waited) for t in tasks
    ] == [
        ("in0_0", 0, 0, whole, False),
        ("in0_1", 0, 4096, whole, False),
        ("in1_0", 1, 0, whole, False),
        ("in1_1", 1, 4096, whole, False),
        ("out_0", 2, 0, whole, True),
        ("out_1", 2, 4096, whole, True),
    ]
    assert _awaited(text) == [t.ssa for t in tasks if t.waited]


def test_an_override_issues_through_the_same_sequence():
    # GEMV's sequence sends the vector to every column before any rows.
    op = GEMV(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=4)
    assert GEMV.has_sequence_override()
    text, tasks = generated_sequence(op)
    assert [(t.lane, t.offset, t.waited) for t in tasks] == [
        ("B_L3L1_0", 0, False),
        ("B_L3L1_1", 0, False),
        ("A_L3L1_0", 0, False),
        ("A_L3L1_1", 128 * 64, False),
        ("C_L1L3_0", 0, True),
        ("C_L1L3_1", 128, True),
    ]
    assert _awaited(text) == [t.ssa for t in tasks if t.waited]


def test_preamble_rejects_a_resident_the_array_never_bound(npu2):
    class Op(Operator):
        n: int = param()
        tile: int = auto(64)
        A = In(n, tile=(tile,))
        count = Value(np.int32, derive=lambda op: op.n // op.tile)

    with pytest.raises(ValueError, match="never bound this value"):
        Sequence(Op(n=64), {}).preamble(Target(npu2))


def test_mha_sequence_is_one_descriptor_set_per_kv_group():
    # Eight pipelines: Q and O go through two shims, each carrying four
    # pipelines' (256-row) block. Per KV group, each shim's Q is one pattern
    # over the group's heads and every block, K and V are the head's blocks
    # of rows re-read once per (head, block) from the iteration slot (the
    # block count the dimension a bound patches), and the O drains mirror
    # the Q fills and are waited on.
    op = MHA(num_heads=2, seq_len=1000, d=64, num_KV_heads=1, num_pipelines=8)
    op = op.resolved(from_name("npu2", n_cols=8))
    assert op.seq_pad == 1024 and op.q_shims == 2 and op.join_rows == 256
    assert op.residents == {
        "heads": 2,
        "q_blocks_per_pipeline": 2,
        "q_blocks_valid": 2,
        "kv_blocks": 16,
        "s_q": 1000,
        "s_kv": 1000,
        "q_start": 0,
    }
    text, tasks = generated_sequence(op)
    head, block = 1024 * 64, 256 * 64
    # Q: (heads, blocks, rows, d). K and V: the head's 16 blocks of 64 rows,
    # re-read four times.
    q = ("2, 2, 256, 64", f"{head}, {2 * block}, 64, 1")
    kv = ("4, 16, 64, 64", "0, 4096, 64, 1")
    assert [
        (t.lane, t.arg, t.offset, (t.sizes, t.strides), t.waited) for t in tasks
    ] == [
        ("inQ", 0, 0, q, False),
        ("inQ2", 0, block, q, False),
        ("inK", 1, 0, kv, False),
        ("inV", 2, 0, kv, False),
        ("memO", 3, 0, q, True),
        ("memO2", 3, block, q, True),
    ]
    assert "repeat_count = 3" in tasks[2].attributes  # the re-read, as repeats
    assert _awaited(text) == [t.ssa for t in tasks if t.waited]


def test_mha_sequence_over_interleaved_heads_is_strided_the_same_way():
    # The (seq, heads, d) layout, for the queries and the keys: a head's rows
    # are strided by every head's d, and the group's heads are d apart; the
    # descriptor count is the same.
    op = MHA(
        num_heads=4,
        seq_len=1024,
        d=64,
        num_KV_heads=2,
        num_pipelines=8,
        heads_interleaved=True,
        kv_interleaved=True,
    ).resolved(from_name("npu2", n_cols=8))
    _, tasks = generated_sequence(op)
    assert [t.lane for t in tasks] == ["inQ", "inQ2", "inK", "inV", "memO", "memO2"] * 2
    q0, q1, k0, *_ = tasks
    # Q: (heads 2 at stride d, blocks 2, rows 256 at stride 4d, d)
    assert (q0.sizes, q0.strides) == ("2, 2, 256, 64", f"64, {2 * 256 * 256}, 256, 1")
    assert q1.offset == q0.offset + 256 * 256
    # K: the head's 16 blocks of 64 rows at stride 2d, re-read 4 times.
    assert (k0.sizes, k0.strides) == ("4, 16, 64, 64", "0, 8192, 128, 1")
    # The second group starts at its heads.
    assert tasks[6].offset == 2 * 64 and tasks[8].offset == 64


def test_mha_of_one_query_packs_a_group_per_pipeline_over_its_own_kv():
    # Decode's shape, over a cache bounded per call: each of 4 pipelines
    # takes KV groups p*2 and p*2+1 in turn. Per step, Q is the group's 4
    # heads (256 elements) re-read 16 times to fill a 64-row block, K and V
    # the group's bounded blocks on the pipeline's own lanes, and O drains
    # the block back over the same 256 elements. The counts the bound moves
    # are per call; the rest are written once, and the array reads each
    # from where the sequence puts it.
    op = MHA(
        num_heads=32,
        num_KV_heads=8,
        seq_len=1,
        kv_len=2048,
        num_pipelines=4,
        heads_interleaved=True,
    )
    op.use_value("kv_valid", "n")
    op = op.resolved(from_name("npu2", n_cols=8))
    assert op.residents == {"heads": 2, "q_blocks_per_pipeline": 1, "q_blocks_valid": 1}
    _, tasks = generated_sequence(op)
    group, cache = 4 * 64, 2048 * 64
    q = ("16, 1, 1, 256", "0, 0, 0, 1")
    kv = ("1, 32, 64, 64", "0, 4096, 64, 1")
    for step in range(2):
        heads = [(p * 2 + step) for p in range(4)]
        fills = tasks[step * 16 : (step + 1) * 16]
        assert [(t.lane, t.offset, (t.sizes, t.strides)) for t in fills] == [
            *[("inQ", h * group, q) for h in heads],
            *[
                (f"{x}{p or ''}", h * cache, kv)
                for p, h in enumerate(heads)
                for x in ("inK", "inV")
            ],
            *[("memO", h * group, q) for h in heads],
        ]
        assert all("repeat_count = 15" in t.attributes for t in fills[:4])
        assert all(t.length_parameter.endswith("kv_blocks") for t in fills[4:12])
        assert all(t.length_unit == str(64 * 64) for t in fills[4:12])
        assert all(t.waited for t in fills[12:])


def test_mha_infers_the_padded_length_and_the_kv_head_count():

    op = MHA.from_operands((8, 128, 64), (2, 128, 64), (2, 128, 64))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match="seq_pad=100"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


# --------------------------------------------------------------------------
# A per-call size in a transfer
# --------------------------------------------------------------------------


def _bounded_gemv():
    # A patched length is whole 16-byte units: an output tile of 8 bf16 rows.
    op = GEMV(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=8)
    op.use_value("valid", "n")  # what a graph does for A[:n]
    return op


def test_the_derived_sequence_patches_a_bounded_operand():
    op = ReLU(size=8192, num_aie_columns=2, num_channels=1, tile_size=1024)
    op.use_value("valid", "n")
    assert op.derived_at("valid_x", valid=2048) == 1  # 2048 over 2 lanes of 1024
    _, tasks = generated_sequence(op)
    # Each lane every other tile, its count patched on D2.
    assert [(t.arg, t.offset, t.sizes, t.strides, t.waited) for t in tasks] == [
        (0, 0, "1, 4, 1, 1024", "0, 2048, 1024, 1", False),
        (0, 1024, "1, 4, 1, 1024", "0, 2048, 1024, 1", False),
        (1, 0, "1, 4, 1, 1024", "0, 2048, 1024, 1", True),
        (1, 1024, "1, 4, 1, 1024", "0, 2048, 1024, 1", True),
    ]
    patched = [t.length_parameter.rsplit("_", 2)[-2:] for t in tasks]
    assert patched == [["valid", "x"]] * 2 + [["valid", "y"]] * 2


def test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin():
    """Under a bound on M, B goes whole as ever, then each column takes A in
    output tiles (four input tiles each here) and C in the same tiles, both
    patched by the tile count the core also reads.
    """
    op = _bounded_gemv().resolved(from_name("npu2", n_cols=8))
    assert [v.name for v in op.values] == ["valid", "tiles", "valid_A", "valid_C"]
    assert op.derived_at("tiles", valid=64) == 64 // (2 * 8)
    assert op.derived_at("valid_A", valid=64) == 64 // (2 * 8)  # unit: output tiles
    text, tasks = generated_sequence(op)
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
        ("B_L3L1_0", 0, "1, 1, 1, 64", "0, 0, 0, 1", False),
        ("B_L3L1_1", 0, "1, 1, 1, 64", "0, 0, 0, 1", False),
        ("A_L3L1_0", 0, "1, 16, 1, 512", "0, 1024, 512, 1", True),
        ("A_L3L1_1", 512, "1, 16, 1, 512", "0, 1024, 512, 1", True),
        ("C_L1L3_0", 0, "1, 16, 1, 8", "0, 16, 8, 1", True),
        ("C_L1L3_1", 8, "1, 16, 1, 8", "0, 16, 8, 1", True),
    ]
    assert {t.length_parameter[-7:] for t in tasks[2:]} == {"valid_A", "valid_C"}
    assert text.count("aiex.scratchpad_parameter @") == 2


def test_on_an_xclbin_the_size_is_the_dispatch_scalar():
    # No scratchpad to patch: the sequence is regenerated per call, the
    # per-call scalar standing in for the size itself.
    text, tasks = generated_sequence(_bounded_gemv(), "xclbin")
    assert "scratchpad_parameter" not in text
    assert [(t.lane, t.offset, t.length_parameter) for t in tasks[2:]] == [
        ("A_L3L1_0", 0, ""),
        ("A_L3L1_1", 512, ""),
        ("C_L1L3_0", 0, ""),
        ("C_L1L3_1", 8, ""),
    ]
    for t, run in zip(tasks[2:], (512, 512, 8, 8)):
        assert re.fullmatch(rf"1, %\w+, 1, {run}", t.sizes), t.sizes


def test_a_stack_and_its_flat_spelling_move_the_same_descriptors():
    """``Repeat`` on the cache ``(G, L, D)`` is the repeat on ``(G, L * D)``:
    the same rows, the same row length, the same transfers.
    """
    flat = Repeat(rows=8, cols=2048 * 64, repeat=4, tile_size=64)
    stack = Repeat(rows=8, seq=2048, cols=64, repeat=4)
    assert stack.x.shape == (8, 2048, 64) and stack.y.shape == (32, 2048, 64)
    assert generated_sequence(flat) == generated_sequence(stack)
    assert stack.resolved().tile_size == 64  # the row's last axis


@pytest.mark.parametrize(
    "size_by, error, match",
    [
        (lambda op: {4: op.value("valid_A")}, ValueError, "dimensions 0..3"),
        (lambda op: {1: 32}, TypeError, "value member's word"),  # not a word
    ],
    ids=["past_the_dimensions", "not_a_word"],
)
def test_a_size_patch_names_a_dimension_and_a_word(size_by, error, match):
    class Patched(GEMV):
        def sequence(self, rt):
            rt.fill(self.A.lane(0), self.A, size_by=size_by(self))

    op = Patched(M=256, K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=4)
    op.use_value("valid", "n")
    with pytest.raises(error, match=match):
        build_design(op)


def test_a_bounded_repeat_patches_the_stack_axis():
    # The stack axis is on D2 with its patched count, rows and repeats around it.
    op = Repeat(rows=4, cols=8, seq=32, repeat=2).resolved(NPU2_4COL)
    op.use_value("valid_seq", "c")
    _, tasks = generated_sequence(op)
    assert [(t.lane, t.sizes, t.strides, t.length_parameter[-11:]) for t in tasks] == [
        ("fifo_in", "2, 32, 4, 8", "0, 8, 256, 1", "valid_seq_x"),
        ("fifo_out", "2, 32, 4, 8", "256, 8, 512, 1", "valid_seq_y"),
    ]


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
    assert op.tile_ma == flm_gemm._default_l1(64, 128, 9 / 8, 65536, 1)[0]
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
    assert b.host_shape == (flm_gemm.packed_b_size(1024, 1024, True),)
    assert b.host_dtype is np.uint8
    assert op.residents == {
        "n_val": 1024,
        "m_row_blocks": 2,
        "k_iters": 2,
        "mode": 0,
        "clamp_min": int(np.float32(-np.inf).view(np.int32)),
        "clamp_max": int(np.float32(np.inf).view(np.int32)),
        "n_chunks": 2,
        "n_units": 2,
    }
    with pytest.raises(ValueError, match="multiple of 256"):
        flm_gemm.GEMM(M=100, K=1024, N=1024).resolved(
            from_name("npu2", n_cols=8)
        )  # M tiles to the array's rows
    with pytest.raises(ValueError, match="not in epilogue_modes"):
        flm_gemm.GEMM(M=256, K=1024, N=1024, epilogue="gelu", epilogue_modes=("none",))


def test_flm_gemm_layout_of_b_follows_the_device():
    untuned = flm_gemm.GEMM(M=256, K=512, N=512)
    with pytest.raises(flm_gemm.Incompatible):
        [b.shape for b in untuned.buffers]  # B's layout follows the device
    assert untuned.resolved(from_name("npu2", n_cols=8)).B.shape == (512 * 512 // 8,)


# --------------------------------------------------------------------------
# flm.gemm.Shipped: the sequence for a shipped image, device-free
# --------------------------------------------------------------------------


def test_a_shipped_image_declares_its_pins_and_parameter_block():

    op = Shipped(M=256, K=1024, N=1152)
    assert op.external.filename == "flm_mm_f81eba71.xclbin"
    pins = [op.A.lane(r).shim for r in range(4)] + [op.B.lane(3).shim]
    assert [(p.col, p.channel) for p in pins if p is not None] == [
        (0, 0),
        (2, 0),
        (4, 0),
        (6, 0),
        (3, 1),
    ]
    assert (op.rtp.address, op.rtp.lock) == (4096, 10)

    image = Xclbin(url="u", sha256="s", filename="f")
    # Nothing builds a shipped image's array, so the declaration has to say
    # where every stream enters and every value lives, and may not build.
    with pytest.raises(DeclarationError, match="pinned with via="):

        class Unpinned(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,))

    with pytest.raises(DeclarationError, match="needs an address"):

        class Unplaced(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))
            count = Value(np.int32, derive=lambda op: op.n)

    with pytest.raises(DeclarationError, match="nothing builds its array"):

        class Built(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))

            def array(self, target):
                return []


def test_shipped_sequence_writes_every_core_then_streams_in_consume_order(npu2):

    op = Shipped(M=256, K=1024, N=1152, epilogue="gelu", clamp=(-2.0, 2.0))
    # The port's values are hidden; the image's block is laid out from the
    # operator's fields.
    assert op.residents == {"rtp": [2, 256, 1152, 0, 1, 1, -1073741824, 1073741824]}
    sequence, tasks = generated_sequence(op)
    text = str(build_design(op))

    writes = [tuple(map(int, w)) for w in _WRITE.findall(sequence)]
    # 8 words on 32 cores, then one lock release per core, before any DMA.
    assert len(writes) == 32 * 8
    assert writes[0] == (0, 2, 0, 2) and writes[7] == (0, 2, 7, 1073741824)
    assert writes[-1] == (7, 5, 7, 1073741824)
    assert text.count('{address = 4096 : i32, sym_name = "rtp_') == 32
    releases = re.findall(r"aiex\.set_lock\(%lock_(\d+)_(\d+), %c1_i32\w*\)", sequence)
    assert len(releases) == 32 and releases[-1] == ("7", "5")
    assert text.count("aie.lock(") == 32
    assert re.search(r"%lock_0_2 = aie\.lock\(%\w+, 10\)", text)
    assert sequence.rindex("aiex.set_lock") < sequence.index("aiex.dma_start_task")

    # N = 9 column-blocks: one full sweep (4 A + 8 B + 8 C) and a trailing
    # block on column 0 alone, which still receives A on every row.
    assert len(tasks) == 20 + 6
    assert [(t.lane, t.arg, t.offset, t.sizes, t.strides) for t in tasks[:3]] == [
        ("A_0", 0, 0, "1, 2, 64, 512", "0, 512, 1024, 1"),
        ("B_0", 1, 0, "1, 1, 1, 131072", "0, 0, 0, 1"),
        ("C_0", 2, 0, "1, 1, 256, 128", "0, 0, 1152, 1"),
    ]
    a1 = tasks[5]
    assert (a1.lane, a1.offset, a1.sizes) == ("A_1", 64 * 1024, "1, 2, 64, 512")
    # Every task is started and awaited exactly once, the last ones by the
    # trailing finish.
    started = re.findall(r"aiex\.dma_start_task\(%(\d+)\)", sequence)
    assert (
        sorted(map(int, started))
        == sorted(_awaited(sequence))
        == sorted(t.ssa for t in tasks)
    )
