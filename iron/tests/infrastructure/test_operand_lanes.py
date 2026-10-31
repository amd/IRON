# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Operand.fifos()``'s ``readers=`` (several consumer ends of one lane) and
``tiles=`` (the raw fifo, placed) extensions, and ``feed()``'s refusal of a
held (``replicate``) input.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import Program
from aie.iron.kernels import sample as sample_kernel
from aie.utils.compile.jit.compilabledesign import CompilableDesign
from aie.utils.npukernel import NPUKernel
from ml_dtypes import bfloat16

from iron.common.design.design import BuiltArray, OperatorDesign
from iron.common.design.runtime import MergedRuntime, OperatorRuntime
from iron.common.image.link import FullELF
from iron.operators.clamp import Clamp
from iron.operators.depthwise_conv1d import DepthwiseConv1d
from iron.operators.elementwise_add import RowwiseAdd
from iron.operators.emit import Emit
from iron.operators.mha import MHA
from iron.operators.rms_norm import RMSNorm
from iron.operators.sample import Sample

pytestmark = pytest.mark.usefixtures("npu2")


def test_several_readers_one_core_still_gets_its_own_list():
    """``readers=`` is asked at one column: every core still took its own
    ``fifos()`` list, not the plain, flat shape ``readers=None`` returns (the
    bug this guards against was a ``TypeError`` indexing a bare end).
    """
    op = DepthwiseConv1d(rows=32, channels=96, num_aie_columns=1).resolved()
    BuiltArray(OperatorDesign(op))


def test_several_readers_many_cores_each_get_a_fresh_end():
    """Reusing one handle for two Workers raises "Endpoint already set";
    every column instead takes a fresh ``cons()`` of the one weight fifo.
    """
    op = DepthwiseConv1d(rows=32, channels=96, num_aie_columns=8).resolved()
    built = BuiltArray(OperatorDesign(op))
    assert len(built.op.weight.lane_handles) == 1


def test_mha_split_places_q_k_v_o_at_their_shim_tiles():
    """P*V split over two cores (``d=512``) places Q, K, V and O at
    ``SplitColumns``' shim tiles from ``fifos(tiles=...)``, instead of a
    manual ``bind()`` after the fact.
    """
    op = MHA(
        num_heads=4,
        num_KV_heads=1,
        seq_len=2000,
        d=512,
        causal=False,
        num_pipelines=8,
    ).resolved()
    BuiltArray(OperatorDesign(op))


def test_feed_refuses_a_held_input():
    """``RowwiseAdd``'s ``row`` holds one line for the whole call, every
    core meeting it: not what a fed, per-iteration stream gives.
    """
    clamp = Clamp(
        size=2048, num_aie_columns=1, tile_size=2048, low=0.0, high=1.0
    ).resolved()
    produced = BuiltArray(OperatorDesign(clamp))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    add = RowwiseAdd(
        rows=1, num_aie_columns=1, num_channels=1, tile_size=2048
    ).resolved()
    with pytest.raises(ValueError, match="holds one line"):
        add.row.feed(source)


def test_feed_refuses_a_held_weighted_input():
    """``RMSNorm``'s ``weight`` is the same held lane, under ``weighted``."""
    clamp = Clamp(
        size=2048, num_aie_columns=1, tile_size=2048, low=0.0, high=1.0
    ).resolved()
    produced = BuiltArray(OperatorDesign(clamp))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    norm = RMSNorm(
        rows=1, num_aie_columns=1, num_channels=1, tile_size=2048, weighted=True
    ).resolved()
    with pytest.raises(ValueError, match="holds one line"):
        norm.weight.feed(source)


def test_fifos_refuses_readers_and_tiles_together():
    op = Clamp(
        size=2048, num_aie_columns=1, tile_size=2048, low=0.0, high=1.0
    ).resolved()
    with pytest.raises(ValueError, match="do not combine"):
        op.layout().x.fifos(readers=2, tiles=[None])


def test_fifos_refuses_readers_on_an_output():
    op = Clamp(
        size=2048, num_aie_columns=1, tile_size=2048, low=0.0, high=1.0
    ).resolved()
    with pytest.raises(ValueError, match="an output"):
        op.layout().y.fifos(readers=2)


def test_fifos_refuses_a_tiles_length_mismatch():
    op = DepthwiseConv1d(rows=32, channels=96, num_aie_columns=8).resolved()
    with pytest.raises(ValueError, match="lanes; tiles has"):
        op.layout().x.fifos(tiles=[None, None])


# ---------------------------------------------------------------------------
# On the device: a pair this task newly enables.
# ---------------------------------------------------------------------------

# Emit's row program: (plane, index, scale, bias, down, mul, add, lo, hi, mask, shift).
_ROW_FIELDS = 11
_UNCLAMPED = (np.iinfo(np.int32).min, np.iinfo(np.int32).max)


def _identity_row_program(op: Emit) -> np.ndarray:
    """A program whose image rows copy ``planes[0]`` unchanged into
    ``image``: Emit's general int32 ALU at its identity. The carried rows
    past them are left zero (unused), a valid no-op row.
    """
    program = np.zeros((op.rows, _ROW_FIELDS), np.int32)
    for r in range(op.slots):
        program[r] = [0, r, 1, 0, 0, 1, 0, *_UNCLAMPED, -1, 0]
    return program


@pytest.mark.supported_devices("npu2")
def test_emit_feeds_sample_draws_matches_reference_and_unfused():
    """Emit computes "the next call's scratchpad and carried state" (its own
    docstring); here, the sampling draw row. Fed straight into Sample.draws,
    whose select cores and combine core each take their own reader of it
    (the several readers ``fifos()`` now gives a fed lane), the row costs no
    host round trip between the two operators.
    """
    emit = Emit(
        slots=sample_kernel.ROW_WORDS, carried=sample_kernel.ROW_WORDS
    ).resolved()
    samp = Sample(vocab=4096, cores=2, steps=1).resolved()

    rng = np.random.default_rng(3)
    draw = sample_kernel.draw_row(0.7, 5, int(rng.integers(0, 1 << 53)))
    planes = np.zeros((2, emit.carried), np.int32)
    planes[0, : sample_kernel.ROW_WORDS] = draw
    program = _identity_row_program(emit)
    logits = (
        np.random.default_rng(11)
        .normal(0, 3, samp.vocab)
        .astype(np.float32)
        .astype(bfloat16)
    )
    logits[rng.choice(samp.vocab, 8, replace=False)] = logits.max()
    tokens_in = np.full(samp.steps, -1, dtype=np.int32)

    image_ref, _ = emit.reference(program, planes)
    assert np.array_equal(image_ref, draw.astype(np.int32)), "the identity program"
    tokens_ref, token_ref = samp.reference(logits, image_ref.reshape(1, -1), tokens_in)

    designs = [
        OperatorDesign(emit, full_elf=True),
        OperatorDesign(samp, full_elf=True),
    ]

    def fused_program():
        first = BuiltArray(designs[0])
        second = BuiltArray(designs[1], fed={"draws": first.op.image})
        runtime = MergedRuntime.fuse(
            [
                OperatorRuntime(first.op, first.built),
                OperatorRuntime(second.op, second.built),
            ],
            "sequence",
        )
        return Program(
            first.op.array_device(), runtime, workers=first.workers + second.workers
        )

    compiled = CompilableDesign(
        lambda: fused_program().resolve_program(),
        use_cache=False,
        aiecc_flags=[*FullELF.FLAGS, *emit.aiecc_flags, *samp.aiecc_flags],
        full_elf=True,
    )
    compiled.compile()
    entry = compiled.get_cache_entry()
    assert entry is not None
    kernel = NPUKernel(
        elf_path=entry.elf, kernel_name=entry.full_elf_kernel, params_path=entry.params
    )

    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    program_t, planes_t = tensor(program.reshape(-1)), tensor(planes.reshape(-1))
    state_t = tensor(np.zeros(emit.carried, np.int32))
    logits_t = tensor(logits)
    tokens_t, token_t = tensor(tokens_in.copy()), tensor(np.zeros(1, np.int32))
    kernel(program_t, planes_t, state_t, logits_t, tokens_t, token_t)
    token, tokens = token_t.numpy(), tokens_t.numpy()
    assert np.array_equal(token, token_ref), (token, token_ref)
    assert np.array_equal(tokens, tokens_ref), (tokens, tokens_ref)

    # Unfused: the same two operators, Emit's image round-tripped through the
    # host instead of fed on-chip.
    image_t = tensor(np.zeros(emit.slots, np.int32))
    emit(program_t, planes_t, image_t, tensor(np.zeros(emit.carried, np.int32)))
    unfused_tokens_t = tensor(tokens_in.copy())
    unfused_token_t = tensor(np.zeros(1, np.int32))
    samp(
        logits_t,
        tensor(image_t.numpy().reshape(-1)),
        unfused_tokens_t,
        unfused_token_t,
    )
    assert np.array_equal(token, unfused_token_t.numpy()), "fused vs unfused token"
    assert np.array_equal(tokens, unfused_tokens_t.numpy()), "fused vs unfused tokens"
