# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The runtime sequence, device-free.

What the library derives (the split of a buffer over its lanes, and the
round-robin one under a bound) is checked as access patterns; what a
sequence issues is checked in the module a real build generates: each shim
task's lane, buffer argument, offset, sizes, strides and patched size.
"""

import re
from math import prod
from typing import NamedTuple

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron.device import from_name
from aie.utils import bfp
from ml_dtypes import bfloat16

import iron.operators.flm.gemm.op as flm_gemm
from iron.operators.flm.packing import packed_b_size
from iron.common import (
    In,
    Link,
    Operator,
    Out,
    Shim,
    Value,
    Xclbin,
    auto,
    OptionalDim,
    param,
)
from iron.common import graph
from iron.common.design import (
    OperatorDesign,
    Sequence,
    build_design,
)
from iron.operators.clamp import Clamp
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.flm.gemm.design import Epilogue
from iron.operators.flm.gemm.shipped import Shipped
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.repeat import Repeat
from iron.operators.rope import RoPE
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU
from iron.tests.common.declare import Rows

# A descriptor's fields are the current device's.
pytestmark = pytest.mark.usefixtures("npu2")

NPU2_4COL = from_name("npu2", n_cols=4)


class MV(Operator):
    M: int = param()
    K: int = param()
    num_batches: int = param(default=1)
    cols: int = auto(2)
    tile_out: int = auto(64)
    A = In(OptionalDim(num_batches), M, K, tile=(tile_out, K), per=(cols,))
    B = In(OptionalDim(num_batches), K, tile=(K,), broadcast=True)
    C = Out(OptionalDim(num_batches), M, tile=(tile_out,), per=(cols,))


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
    r"%(\d+) = aiex\.dma_configure_task_for @(\w+) \{\s*"
    r"aie\.dma_bd\(%arg(\d+) : \S+ offset = (\d+) (?:len = %?\w+ )?"
    r"sizes = \[([^\]]*)\] strides = \[([^\]]*)\]\)"
    r"(?: \{length_parameter = @(\w+), length_unit = (\d+) : i32\})?"
    r"\s*aie\.end\s*\}(?: \{([^}]*)\})?"
)
# The graph value a test binds an extent to, as ``x[:n]`` does.
N = graph.Value("n", "scratchpad", np.int32).affine()


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


# --------------------------------------------------------------------------
# What the library derives: the split and the round-robin
# --------------------------------------------------------------------------


def test_split_takes_every_batch_and_broadcasts():
    op = MV(M=256, K=128, num_batches=100)
    a_transfers = Sequence.split(op.A)
    assert [slot.index for slot, _ in a_transfers] == [0, 1]
    # Each lane's rows out of every batch: one pattern, however many batches.
    assert a_transfers[1][1] == TensorAccessPattern(
        (100, 256, 128), 128 * 128, [100, 128, 128], [256 * 128, 128, 1]
    )
    ((b_slot, b_tap),) = Sequence.split(op.B)
    assert b_slot == op.B.lane(0)
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
    plan = Sequence.round_robin(op.x, 0)
    assert [(slot.index, tap, dim) for slot, tap, dim in plan] == [
        (0, TensorAccessPattern((1, 32, 2, 8), 0, [1, 32, 1, 8], [0, 16, 8, 1]), 1),
        (1, TensorAccessPattern((1, 32, 2, 8), 8, [1, 32, 1, 8], [0, 16, 8, 1]), 1),
    ]
    # A leading batch axis is the outer repeat; the tile count keeps its slot.
    batched = MV(M=256, K=128, num_batches=3).resolved(NPU2_4COL)
    (slot, tap, dim), *_ = Sequence.round_robin(batched.A, 1)
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
    x = Sequence.round_robin(op.x, 0)
    angles = Sequence.round_robin(op.angles, 0)
    for (xs, xa, _), (as_, aa, _) in zip(x, angles, strict=True):
        assert xs.index == as_.index
        rows = xa.gather(np.arange(prod(xa.tensor_dims)))[::cols] // cols
        angle_rows = aa.gather(np.arange(prod(aa.tensor_dims)))[::cols] // cols
        assert list(angle_rows) == list(range(xs.index, positions, lanes))
        assert list(rows // heads) == list(np.repeat(angle_rows, heads))


# --------------------------------------------------------------------------
# What a sequence issues, in the generated module
# --------------------------------------------------------------------------


def test_preamble_rejects_a_resident_the_array_never_bound(npu2):
    class Op(Operator):
        n: int = param()
        tile: int = auto(64)
        A = In(n, tile=(tile,))
        count = Value(np.int32, derive=lambda op: op.n // op.tile)

    with pytest.raises(ValueError, match="never bound this value"):
        Sequence(Op(n=64), {}).preamble()


def test_mha_infers_the_padded_length_and_the_kv_head_count():

    op = MHA.from_operands((8, 128, 64), (2, 128, 64), (2, 128, 64))
    assert (op.num_heads, op.num_KV_heads, op.seq_len, op.seq_pad) == (8, 2, 128, 128)
    with pytest.raises(ValueError, match="seq_pad=100"):
        MHA(num_heads=1, seq_len=100, seq_pad=100, d=64)


def test_mha_binds_p_times_v_at_its_own_shape():
    """Away from B_kv = d, P*V's operands are not QK^T's: P is (B_q, B_kv), V
    (B_kv, d) and O (B_q, d), each streamed as P*V takes it, O accumulated
    in float32 and rounded once into the bf16 output.
    """
    op = MHA(num_heads=1, seq_len=1024, d=128, num_pipelines=8, B_q=32)
    text = str(build_design(op.resolved(from_name("npu2", n_cols=8))))
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
        ("C_L1L3_0", 0, "1, 16, 1, 8", "0, 16, 8, 1", True),
        ("C_L1L3_1", 8, "1, 16, 1, 8", "0, 16, 8, 1", True),
        ("A_L3L1_0", 0, "2, 1, 1, 64", "0, 0, 0, 1", False),
        ("A_L3L1_0", 0, "1, 16, 1, 512", "0, 1024, 512, 1", True),
        ("A_L3L1_1", 0, "2, 1, 1, 64", "0, 0, 0, 1", False),
        ("A_L3L1_1", 512, "1, 16, 1, 512", "0, 1024, 512, 1", True),
    ]
    assert {t.length_parameter[-7:] for t in tasks if t.length_parameter} == {
        "valid_A",
        "valid_C",
    }
    assert text.count("aiex.scratchpad_parameter @") == 2


def test_on_an_xclbin_the_size_is_the_dispatch_scalar():
    # No scratchpad to patch: the sequence is regenerated per call, the
    # per-call scalar standing in for the size itself.
    text, tasks = generated_sequence(_bounded_gemv(), "xclbin")
    assert "scratchpad_parameter" not in text
    # %arg1 is B, the head of each A stream, whose size no call bounds.
    bounded = [t for t in tasks if t.arg != 1]
    assert [(t.lane, t.offset, t.length_parameter) for t in bounded] == [
        ("C_L1L3_0", 0, ""),
        ("C_L1L3_1", 8, ""),
        ("A_L3L1_0", 0, ""),
        ("A_L3L1_1", 512, ""),
    ]
    for t, run in zip(bounded, (8, 8, 512, 512), strict=True):
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
    op.use_value("valid", N)
    with pytest.raises(error, match=match):
        build_design(op)


def test_a_bounded_repeat_patches_the_stack_axis():
    # The stack axis is on D2 with its patched count, rows and repeats around it.
    op = Repeat(rows=4, cols=8, seq=32, repeat=2).resolved(NPU2_4COL)
    op.use_value("valid_seq", graph.Value("c", "scratchpad", np.int32).affine())
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
    with pytest.raises(ValueError):
        [b.shape for b in untuned.buffers]  # B's layout follows the device
    assert untuned.resolved(from_name("npu2", n_cols=8)).B.shape == (512 * 512 // 8,)


def test_flm_gemm_folds_an_activation_then_a_clamp_into_its_epilogue():
    op = flm_gemm.GEMM(M=256, K=512, N=512)
    size = 256 * 512
    silu = op.fold(SiLU(size=size))
    assert silu.epilogue is Epilogue.SILU and silu.clamp is None
    clamped = silu.fold(Clamp(size=size, low=-0.7, high=2.0))
    assert clamped.clamp == (float(bfloat16(-0.7)), 2.0)
    assert clamped.config_name == op.config_name
    # Its gelu is not the GELU operator's, nothing follows its clamp, and
    # it applies one activation.
    assert op.fold(GELU(size=size)) is None
    assert clamped.fold(Clamp(size=size, low=0.0, high=1.0)) is None
    assert silu.fold(Sigmoid(size=size)) is None
    assert silu.epilogue_modes == op.epilogue_modes
    plain = flm_gemm.GEMM(M=256, K=512, N=512, epilogue_modes=("none",))
    compiled_in = plain.fold(SiLU(size=size))
    assert compiled_in.epilogue_modes == (Epilogue.NONE, Epilogue.SILU)
    assert plain.epilogue_modes == (Epilogue.NONE,)
    finished = SiLU(size=size, finish=(Link(ElementwiseMul(size=size)),))
    assert op.fold(finished) is None


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
    with pytest.raises(TypeError, match="pinned with via="):

        class Unpinned(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,))

    with pytest.raises(TypeError, match="needs an address"):

        class Unplaced(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))
            count = Value(np.int32, derive=lambda op: op.n)

    with pytest.raises(TypeError, match="nothing builds its array"):

        class Built(Operator, image=image):
            n: int = param()
            x = In(n, tile=(64,), via=Shim(0))

            def array(self, target):
                return []
