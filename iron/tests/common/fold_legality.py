# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folding a movement operator into a neighbour's descriptors: the legality.

The element maps are checked against each mover's own reference, and every
fold against the data it stands for: reading the mover's input at the
folded order must give what the neighbour read from the mover's output, and
writing at the folded order must put each element where the mover would
have. No NPU: the hardware facts the fit rests on are ``dma.py``'s.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name

from iron.common.dma import DmaFacts, Reason
from iron.common.fold_legality import (
    UNWRITTEN,
    Blocked,
    Blocker,
    Fold,
    check_order,
    element_map,
    fold_read,
    fold_write,
)
from iron.operators.gemv.op import GEMV
from iron.operators.mem_copy import MemCopy
from iron.operators.repeat import Repeat
from iron.operators.repeat import reference as repeat_reference
from iron.operators.strided_copy import StridedCopy
from iron.operators.transpose import Transpose
from iron.operators.transpose import reference as transpose_reference

# Grouped-query attention at a small scale: 2 key groups serve 8 query heads
# over a 256-position context of 64-wide heads.
KV, HEADS, SEQ, D = 2, 8, 256, 64


@pytest.fixture(autouse=True)
def npu2():
    previous = aie_utils.get_current_device()
    dev = from_name("npu2", n_cols=8)
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


@pytest.fixture
def facts(npu2):
    return DmaFacts.of(npu2)


def _t(op):
    """``op`` as a build tunes it: an order depends on the tuned overlay."""
    return op.tuned(aie_utils.get_current_device())


def _repeat_keys():
    return _t(Repeat(rows=KV, cols=SEQ * D, repeat=HEADS // KV, transfer_size=64))


def _scores(cols=2):
    return _t(
        GEMV(M=SEQ, K=D, num_batches=HEADS, num_aie_columns=cols, tile_size_output=32)
    )


def _kv_write(position=5, per_call=True):
    """The V projection's output, copied into the cache at ``position``."""
    copy = StridedCopy(
        input_sizes=[KV, D],
        input_strides=[D, 1],
        input_offset=0,
        input_buffer_size=KV * D,
        output_sizes=[1, KV, D],
        output_strides=[0, SEQ * D, 1],
        output_offset=0 if per_call else position * D,
        output_buffer_size=KV * SEQ * D,
        num_aie_channels=2,
    )
    if per_call:
        copy.use_value("out_offset")
    return _t(copy)


def _read_through(fold: Fold, k: int) -> np.ndarray:
    return np.concatenate([acc.indices() for acc in fold.order[k]])


# -- element maps -------------------------------------------------------------


def test_a_repeats_map_is_its_reference():
    op = _repeat_keys()
    got = element_map(op)
    x = np.arange(op.x.elements).reshape(KV, SEQ * D)
    np.testing.assert_array_equal(
        got.source, repeat_reference(x, HEADS // KV).reshape(-1)
    )


def test_a_transposes_map_permutes_each_object():
    op = _t(Transpose(M=128, N=256, num_aie_columns=2, num_channels=1, num_batches=2))
    got = element_map(op)
    x = np.arange(op.x.elements).reshape(2, 128, 256)
    np.testing.assert_array_equal(got.source, transpose_reference(x).reshape(-1))


def test_a_copys_map_is_its_reference_where_it_writes():
    op = _kv_write(per_call=False)
    got = element_map(op)
    ref = op.reference(np.arange(op.x.elements) + 1) - 1
    written = got.source != UNWRITTEN
    assert written.sum() == KV * D
    np.testing.assert_array_equal(got.source, np.where(written, ref, UNWRITTEN))
    assert got.in_by is None and got.out_by is None
    assert element_map(_kv_write()).out_by is not None


def test_a_computing_operator_has_no_element_map():
    got = element_map(_scores())
    assert isinstance(got, Blocked) and got.blocker is Blocker.NOT_MOVEMENT


# -- folds into a read ------------------------------------------------------------


def test_the_scores_gemv_reads_the_keys_straight_from_the_cache(facts):
    """Repeat -> GEMV: each query head's batch re-reads its group's keys. The
    re-read sits inside the walk over groups, so the shim unrolls one
    descriptor per group, each re-reading in its iteration slot."""
    repeat, gemv = _repeat_keys(), _scores()
    mover = element_map(repeat)
    got = fold_read(gemv, gemv.A, mover, facts)
    assert isinstance(got, Fold)
    assert got.bds == KV
    for fit in got.fits:
        assert all(
            acc.sizes[0] == HEADS // KV and acc.strides[0] == 0 for acc in fit.bds
        )
    keys = np.random.default_rng(0).standard_normal(repeat.x.elements)
    repeated = repeat_reference(keys.reshape(KV, -1), HEADS // KV).reshape(-1)
    order = gemv.order(gemv.A)
    for k in range(len(order.slots)):
        np.testing.assert_array_equal(
            keys[_read_through(got, k)], repeated[order.indices(k)]
        )


def test_a_read_of_a_repeat_every_slot_shares_is_a_multicast(facts):
    """Every core reading the same repeated row is one read, multicast: the
    stream would have to be a replicate one, which is another design."""
    repeat = _t(Repeat(rows=1, cols=256, repeat=4, transfer_size=64))
    copy = _t(MemCopy(size=1024, num_cores=4, num_channels=1, tile_size=256))
    got = fold_read(copy, copy.buffers[0], element_map(repeat), facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.MULTICAST


def test_a_read_past_what_the_mover_writes_does_not_fold(facts):
    """The attention GEMV reads the whole cache; the copy writes one row."""
    copy = _kv_write(per_call=False)
    gemv = _t(GEMV(M=SEQ, K=D, num_batches=KV, num_aie_columns=2, tile_size_output=32))
    got = fold_read(gemv, gemv.A, element_map(copy), facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.NOT_PRODUCED


def test_a_bf16_transpose_folds_into_no_descriptor(facts):
    op = _t(Transpose(M=128, N=256, num_aie_columns=2, num_channels=1))
    consumer = _t(MemCopy(size=128 * 256, num_cores=2, num_channels=1, tile_size=256))
    got = fold_read(consumer, consumer.buffers[0], element_map(op), facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.FIT
    assert got.unfit.reason in (Reason.GRANULE, Reason.BDS)


# -- folds into a write -----------------------------------------------------------


def test_the_v_projection_writes_straight_into_the_cache(facts):
    """GEMV -> StridedCopy: the GEMV's drain lands in the cache row, shifted
    per call by the copy's offset."""
    copy = _kv_write()
    gemv = _t(GEMV(M=KV * D, K=2048, num_aie_columns=2, tile_size_output=32))
    mover = element_map(copy)
    got = fold_write(gemv, gemv.C, mover, facts)
    assert isinstance(got, Fold)
    assert got.order.offset_by is copy.out_offset
    assert got.bds == 1
    order = gemv.order(gemv.C)
    projected = np.arange(gemv.C.elements) + 1
    cache = np.zeros(copy.y.elements, dtype=np.int64)
    for k in range(len(order.slots)):
        cache[_read_through(got, k)] = projected[order.indices(k)]
    np.testing.assert_array_equal(
        cache, copy.reference(projected, np.zeros_like(cache))
    )


def test_a_repeat_folds_into_no_write(facts):
    repeat = _repeat_keys()
    producer = _t(
        MemCopy(size=repeat.x.elements, num_cores=2, num_channels=1, tile_size=256)
    )
    got = fold_write(producer, producer.buffers[1], element_map(repeat), facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.DUPLICATES


def test_a_write_the_mover_drops_does_not_fold(facts):
    """A copy of half its input: the producer writes the other half nowhere."""
    copy = StridedCopy(
        input_sizes=[128],
        input_strides=[1],
        input_offset=0,
        input_buffer_size=256,
        output_sizes=[128],
        output_strides=[1],
        output_offset=0,
        output_buffer_size=128,
    )
    copy = _t(copy)
    producer = _t(MemCopy(size=256, num_cores=1, num_channels=1, tile_size=256))
    got = fold_write(producer, producer.buffers[1], element_map(copy), facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.DROPS


# -- the rule over declared orders --------------------------------------------------


@pytest.mark.parametrize(
    "make",
    [
        lambda: _scores(),
        lambda: _t(
            GEMV(M=256, K=128, num_aie_columns=2, tile_size_output=64, num_batches=4)
        ),
        lambda: _repeat_keys(),
        lambda: _kv_write(),
        lambda: _t(
            Transpose(M=128, N=128, num_aie_columns=2, num_channels=1, num_batches=2)
        ),
        lambda: _t(MemCopy(size=1024, num_cores=4, num_channels=1, tile_size=256)),
    ],
    ids=["scores", "gemv_batched", "repeat", "kv_write", "transpose", "memcopy"],
)
def test_every_declared_order_keeps_the_direction_rule(make, facts):
    """Reads may re-read (Repeat's input does); every write lands each element once."""
    op = make()
    for buffer in op.buffers:
        got = check_order(op, buffer, facts)
        assert not isinstance(got, Blocked), f"{buffer.name}: {got}"


def test_a_padded_copy_overwrites_its_own_remainder(facts):
    """MemCopy pads a short last core with transfers of the remainder's first
    granules, then writes the real data over them: a write that visits an
    address three times and relies on the channel landing them in order. It
    runs, but it breaks the rule, so a fold never composes with it."""
    op = _t(MemCopy(size=1000, num_cores=4, num_channels=1, tile_size=256))
    (y,) = [b for b in op.buffers if b.direction == "out"]
    got = check_order(op, y, facts)
    assert isinstance(got, Blocked) and got.blocker is Blocker.FIT
    assert got.unfit.reason is Reason.NOT_INJECTIVE
