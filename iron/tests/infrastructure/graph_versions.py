#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One graph function, called at two shapes, is two images over one arena.

Each input signature compiles its own version, and every full-ELF version
runs in the function's one scratch arena: a weight is placed and uploaded
once, and a state one version writes is the bytes the next reads. These run
on the device, because the claim is about bytes -- two hw contexts over one
buffer object, offsets baked into two ELFs -- and a wrong offset produces
wrong numbers, not an error.

The function below writes its state at one shape and reads it at the other:
``f(x)`` with ``x`` one line long stores ``x + w`` in the state and returns
``x + 2w``; with ``x`` two lines long it returns ``(x + w2)[second line] +
state``.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.image import packaging
from iron.operators import ElementwiseAdd

E = 1024
TILE = 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _numbers(n, seed):
    # Small integers: every sum below is exact in bf16.
    rng = np.random.default_rng(seed)
    return rng.integers(-8, 8, size=n).astype(bfloat16)


def _function():
    w = _numbers(E, 1)
    w2 = _numbers(2 * E, 2)
    s = iron.state((E,), name="line")

    @iron.graph
    def f(x):
        if x.shape[0] == E:
            ElementwiseAdd(x, w, s, tile_size=TILE)
            return ElementwiseAdd(s, w, tile_size=TILE)
        y = ElementwiseAdd(x, w2, tile_size=TILE)
        return ElementwiseAdd(y[E:], s, tile_size=TILE)

    return f, w, w2, s


def _f32(a):
    return np.asarray(a, dtype=np.float32)


def test_two_shapes_share_weights_and_state_through_one_arena():
    """Both compiled before the first call: the arena is made once, at size."""
    f, w, w2, s = _function()
    one = f.compile(x=(E,))
    two = f.compile(x=(2 * E,))
    assert len(f.versions) == 2
    assert one.arena is two.arena is f.arena
    assert one.plan.dispatch == two.plan.dispatch == "fused"

    # The state is one resident: the same bytes in both images.
    layout_one = one.sequence.get_layout_for_buffer("line")
    assert layout_one == two.sequence.get_layout_for_buffer("line")
    assert layout_one[0] == "scratch"

    x1, x2 = _numbers(E, 3), _numbers(2 * E, 4)
    out = f(x1).numpy()
    np.testing.assert_array_equal(_f32(out), _f32(x1) + 2 * _f32(w))
    out = f(x2).numpy()
    expect = (_f32(x2) + _f32(w2))[E:] + _f32(x1) + _f32(w)
    np.testing.assert_array_equal(_f32(out), expect)

    # Each weight went up once, whichever version touched it first.
    assert f.arena.loaded == {id(w), id(w2)}
    assert f.arena.generation == 1
    # One buffer holds both images: their residents, and the larger of
    # their transients, not the sum of two private arenas.
    private = sum(v.sequence.buffer_sizes[2] for v in f.versions.values())
    assert f.arena.plan.size < private


def test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded():
    """``release`` sees every weight once over every version, in order, in
    pieces of at most ``piece_bytes``; after that the host copy is not read:
    overwriting it changes nothing on the device.
    """
    f, w, w2, s = _function()
    f.compile(x=(E,))
    f.compile(x=(2 * E,))
    piece_bytes = 512
    released = []
    for version in f.versions.values():
        version.load(release=released.append, piece_bytes=piece_bytes)

    step = piece_bytes // w.itemsize
    for weight in (w, w2):
        pieces = [p for p in released if np.shares_memory(p, weight)]
        assert [p.ctypes.data for p in pieces] == [
            weight.ctypes.data + begin * w.itemsize
            for begin in range(0, weight.size, step)
        ]
        assert all(p.size == step for p in pieces)
    assert len(released) == (w.size + w2.size) // step

    expect_w, expect_w2 = _f32(w), _f32(w2)
    w[:] = 0
    w2[:] = 0
    x1, x2 = _numbers(E, 9), _numbers(2 * E, 10)
    np.testing.assert_array_equal(_f32(f(x1).numpy()), _f32(x1) + 2 * expect_w)
    expect = (_f32(x2) + expect_w2)[E:] + _f32(x1) + expect_w
    np.testing.assert_array_equal(_f32(f(x2).numpy()), expect)


def test_load_loads_a_version_whose_weights_are_already_uploaded():
    """Loading the one-line version uploads ``w``, which is every weight the
    two-line version reads; loading that one must still put its image on the
    device, or its first call does.
    """
    w = _numbers(E, 1)

    @iron.graph
    def f(x):
        if x.shape[0] == E:
            return ElementwiseAdd(x, w, tile_size=TILE)
        # An input is not sliced in place; an intermediate is.
        y = ElementwiseAdd(x, x, tile_size=TILE)
        return ElementwiseAdd(y[E:], w, tile_size=TILE)

    one = f.compile(x=(E,))
    two = f.compile(x=(2 * E,))
    one.load()
    assert f.arena.loaded == {id(w)} and not two.is_loaded
    two.load()
    assert one.is_loaded and two.is_loaded

    x = _numbers(2 * E, 10)
    np.testing.assert_array_equal(_f32(two(x).numpy()), 2 * _f32(x[E:]) + _f32(w))


def test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state():
    """Compiling on first call at a new shape: the arena grows under the
    version that already ran, which keeps working.
    """
    f, w, w2, s = _function()
    x1, x2 = _numbers(E, 5), _numbers(2 * E, 6)

    first = f(x1).numpy().copy()
    np.testing.assert_array_equal(_f32(first), _f32(x1) + 2 * _f32(w))
    assert f.arena.generation == 1

    out = f(x2).numpy()  # compiles the second version, grows the arena
    assert f.arena.generation == 2
    expect = (_f32(x2) + _f32(w2))[E:] + _f32(x1) + _f32(w)
    np.testing.assert_array_equal(_f32(out), expect)

    # The first version rebinds to the grown buffer and still computes.
    x3 = _numbers(E, 7)
    out = f(x3).numpy()
    np.testing.assert_array_equal(_f32(out), _f32(x3) + 2 * _f32(w))

    # A state written through one version reads back through the other.
    one, two = f.versions.values()
    line = _numbers(E, 8)
    one.write(s, line)
    np.testing.assert_array_equal(_f32(two.read(s)), _f32(line))


def test_versions_that_cannot_share_an_arena_refuse_a_state():
    f, *_ = _function()
    f.compile(x=(E,), boundaries=packaging.each_step)
    with pytest.raises(NotImplementedError, match="only a full ELF"):
        f.compile(x=(2 * E,))
