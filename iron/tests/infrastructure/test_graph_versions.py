# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One graph function, called at two shapes, is two images over one arena.

Each input signature compiles its own version, and every version runs in
the function's one scratch arena: a full ELF places its scratch there, an
xclbin its weights and states. A weight is placed and uploaded once, and a
state one version writes is the bytes the next reads. These run on the
device, because the claim is about bytes -- two hw contexts over one buffer
object, offsets baked into two images -- and a wrong offset produces wrong
numbers, not an error.

The function below writes its state at one shape and reads it at the other:
``f(x)`` with ``x`` one line long stores ``x + w`` in the state and returns
``x + 2w``; with ``x`` two lines long it returns ``(x + w2)[second line] +
state``.
"""

from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.operators import ElementwiseAdd

E = 1024
TILE = 128


pytestmark = pytest.mark.supported_devices("npu1", "npu2")


def _numbers(n, seed):
    # Small integers: every sum below is exact in bf16.
    rng = np.random.default_rng(seed)
    return rng.integers(-8, 8, size=n).astype(bfloat16)


def _function():
    w = _numbers(E, 1)
    w2 = _numbers(2 * E, 2)
    s = iron.state((E,), name="line")

    class F(iron.Graph):
        def body(self, x):
            if x.shape[0] == E:
                ElementwiseAdd.step(x, w, s, tile_size=TILE)
                return ElementwiseAdd.step(s, w, tile_size=TILE)
            y = ElementwiseAdd.step(x, w2, tile_size=TILE)
            return ElementwiseAdd.step(y[E:], s, tile_size=TILE)

    f = F()

    return f, w, w2, s


def _f32(a):
    return np.asarray(a, dtype=np.float32)


def _run_both(f, w, w2):
    """Store through the one-line version, read through the two-line one, and
    check that each weight went up once, whichever version touched it first.
    """
    one, two = f.versions.values()
    # The state is one resident: the same bytes in both images.
    layout_one = one.sequence.layout["line"]
    assert layout_one == two.sequence.layout["line"]
    assert layout_one[0] == "scratch"

    x1, x2 = _numbers(E, 3), _numbers(2 * E, 4)
    out = f(x1).numpy()
    np.testing.assert_array_equal(_f32(out), _f32(x1) + 2 * _f32(w))
    out = f(x2).numpy()
    expect = (_f32(x2) + _f32(w2))[E:] + _f32(x1) + _f32(w)
    np.testing.assert_array_equal(_f32(out), expect)
    assert f.arena.loaded == {id(w), id(w2)}


@pytest.mark.supported_devices("npu2")
def test_two_shapes_share_weights_and_state_through_one_arena():
    """Both compiled before the first call: the arena is made once, at size."""
    f, w, w2, s = _function()
    one = f.compile(x=(E,))
    two = f.compile(x=(2 * E,))
    assert len(f.versions) == 2
    assert one.arena is two.arena is f.arena
    assert one.plan.full_elf and two.plan.full_elf
    _run_both(f, w, w2)
    assert f.arena.generation == 1
    # One buffer holds both images: their residents, and the larger of
    # their transients, not the sum of two private arenas.
    private = sum(v.sequence.buffer_sizes[2] for v in f.versions.values())
    assert f.arena.plan.size < private


def test_a_version_reads_as_its_inputs_plan_and_build_directory():
    f, *_ = _function()
    one = f.compile(x=(E,))
    lines = repr(one).splitlines()
    assert lines[0].startswith(f"F(x=({E},) bfloat16): ")
    assert lines[-1] == f"  built in {one.artifacts.directory}"


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

    class F(iron.Graph):
        def body(self, x):
            if x.shape[0] == E:
                return ElementwiseAdd.step(x, w, tile_size=TILE)
            # An input is not sliced in place; an intermediate is.
            y = ElementwiseAdd.step(x, x, tile_size=TILE)
            return ElementwiseAdd.step(y[E:], w, tile_size=TILE)

    f = F()

    one = f.compile(x=(E,))
    two = f.compile(x=(2 * E,))
    one.load()
    assert f.arena.loaded == {id(w)} and not two.is_loaded
    two.load()
    assert one.is_loaded and two.is_loaded

    x = _numbers(2 * E, 10)
    np.testing.assert_array_equal(_f32(two(x).numpy()), 2 * _f32(x[E:]) + _f32(w))


def test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state():
    """Once a version is loaded, a call at a new shape compiles nothing and
    raises; compiling it then grows the arena under the version that
    already ran, which keeps working.
    """
    f, w, w2, s = _function()
    x1, x2 = _numbers(E, 5), _numbers(2 * E, 6)

    first = f(x1).numpy().copy()
    np.testing.assert_array_equal(_f32(first), _f32(x1) + 2 * _f32(w))
    assert f.arena.generation == 1

    with pytest.raises(ValueError, match="no loaded version"):
        f(x2)
    assert len(f.versions) == 1
    f.compile(x=(2 * E,))
    out = f(x2).numpy()
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


def test_each_step_versions_share_weights_and_state_through_one_arena():
    """Each step's other operands are buffer objects of their own; the
    weights and the state are views of the arena's, and nothing else is.
    """
    f, w, w2, s = _function()
    one = f.compile(x=(E,), full_elf=False)
    two = f.compile(x=(2 * E,), full_elf=False)
    assert one.arena is two.arena is f.arena
    assert not one.plan.full_elf and not two.plan.full_elf
    _run_both(f, w, w2)
    assert f.arena.plan.size == w.nbytes + w2.nbytes + E * 2


@pytest.mark.supported_devices("npu2")
def test_an_each_step_version_and_a_full_elf_share_one_arena():
    """``--no-full-elf``'s decode step beside a full-ELF prompt."""
    f, w, w2, s = _function()
    one = f.compile(x=(E,), full_elf=False)
    two = f.compile(x=(2 * E,))
    assert (one.plan.full_elf, two.plan.full_elf) == (False, True)
    _run_both(f, w, w2)


@pytest.mark.supported_devices("npu2")
def test_a_read_leaves_nothing_for_the_next_call_to_push():
    """Reading an output or a state pulls it without claiming it, so after
    each call every argument is the device's, read or not; a host write
    while a run is out is refused at its wait.
    """
    f, w, w2, s = _function()
    one = f.compile(x=(E,))
    arguments = (one.callable.input_buffer, one.callable.output_buffer, *f.arena.banks)
    for seed in (14, 15):
        x = _numbers(E, seed)
        np.testing.assert_array_equal(_f32(f(x).numpy()), _f32(x) + 2 * _f32(w))
        np.testing.assert_array_equal(_f32(one.read(s)), _f32(x) + _f32(w))
        assert [t.device for t in arguments] == ["npu"] * 3
    run = one.callable.run
    one.start(run, _numbers(E, 16))
    one._storage(s).numpy_view()[:] = _numbers(E, 17)
    with pytest.raises(RuntimeError, match=r"wrote \['scratch'\] while a run"):
        one.callable.wait(run)


@pytest.mark.supported_devices("npu2")
def test_a_released_run_is_made_again_on_the_next_call():
    """What a full device heap does to the version least recently called (the
    EmbeddingGemma 2 determinism test fills it): its run is freed and its
    image unloaded, and its next call loads it and makes a run over the same
    arena and state.
    """
    f, w, w2, s = _function()
    one = f.compile(x=(E,))
    two = f.compile(x=(2 * E,))
    x1, x2 = _numbers(E, 11), _numbers(2 * E, 12)
    f(x1)
    first = one.callable.run
    assert one.callable.release() and not one.callable.release()

    out = f(x2).numpy()
    expect = (_f32(x2) + _f32(w2))[E:] + _f32(x1) + _f32(w)
    np.testing.assert_array_equal(_f32(out), expect)
    x3 = _numbers(E, 13)
    np.testing.assert_array_equal(_f32(f(x3).numpy()), _f32(x3) + 2 * _f32(w))
    assert one.callable.run is not first

    # A callable with another run out, as a loop makes, keeps its image.
    two.callable.new_run()
    assert not two.callable.release()
    # Tearing down the whole graph frees it anyway: nothing calls it again.
    assert two.callable.release(force=True)


def test_release_frees_the_buffers_and_the_next_call_loads_them_again():
    """A model's test fixture releases it, so its buffers are gone before the
    next model loads rather than when the garbage collector reaches them.
    """
    f, w, *_ = _function()
    x = _numbers(E, 5)
    maps = Path("/proc/self/maps")
    f(x)
    loaded = maps.read_text().count("/dev/accel/accel")
    f.release()
    assert maps.read_text().count("/dev/accel/accel") < loaded
    np.testing.assert_array_equal(_f32(f(x).numpy()), _f32(x) + 2 * _f32(w))
    assert maps.read_text().count("/dev/accel/accel") == loaded
