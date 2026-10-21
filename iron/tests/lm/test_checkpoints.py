# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.Checkpoints: a state a decoder carries from position to
position, kept at every prompt-chunk boundary.

The graph here keeps a short convolution's history alone: each position's
window, the ``K`` rows of a sequence ending at it, built from the ``K - 1``
rows before the call, which a ``Checkpoints`` state holds. A prompt chunk
reads its boundary's slot and writes the next; a decode step reads and
writes its chunk's slot, at the slot ``position // C`` names, which the
device's own loop computes between steps. Every move is a copy, so every
window and every slot is held to numpy exactly. A rerun from a boundary a
decode step crossed sees the rows before it, as a chat turn's does.
"""

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron import Carried, Scratchpad
from iron.common.graph.carried import attach_emit, compose
from iron.common.graph.compiled import _words
from iron.common.image.artifacts import Parameter
from iron.lm import Call, Checkpoints
from iron.operators.copy import Copy
from iron.operators.emit import reference as emit_reference

C, K, W, L = 16, 4, 32, 128
# The prompt's rows, then the position the decode steps run to.
PROMPT, LAST = 40, 70


class Window(iron.Graph):
    """Each position's window of ``sequence``, the ``kernel`` rows ending at
    it, kept in ``seen``: a prompt chunk takes its own rows, a decode step
    reads its row of ``sequence``. The ``kernel - 1`` rows before a call
    are checkpointed at every ``chunk``-row boundary.
    """

    def __init__(self, sequence: np.ndarray, chunk: int, kernel: int):
        rows, width = sequence.shape
        self.chunk, self.kernel, self.width = chunk, kernel, width
        self.sequence = iron.weight(sequence)
        self.tail = Checkpoints.of((kernel - 1, width), rows, chunk)
        # The rows before a call end block 0; a chunk's rows are block 1.
        self.window = iron.state((2, chunk, width))
        self.staged = iron.state((kernel - 1, width))
        self.seen = iron.state((rows, kernel, width))

    def body(
        self,
        x=None,
        *,
        position: Carried[np.int32],
        start: Scratchpad[np.int32],
        rows: Scratchpad[np.int32],
    ):
        C, K, W = self.chunk, self.kernel, self.width
        prompt = x is not None
        first = C - (K - 1)
        flat = self.window.reshape(2 * C, W)
        call = Call(
            prompt=prompt,
            start=start if prompt else position,
            rows=rows,
            position=position,
        )
        read, write = self.tail.at(call)
        Copy.step(read, flat[first:C])
        if not prompt:
            Copy.step(self.sequence[position], flat[C])
            Copy.step(flat[first : C + 1], self.seen[position])
            Copy.step(flat[first + 1 : C + 1], write)
            return iron.carry(position=position + 1)
        Copy.step(x[:rows], self.window[1, :rows])
        every = TensorAccessPattern((2 * C, W), first * W, [C, K * W], [W, 1])
        windows = Copy.step(self.window, src=every).reshape(C, K, W)[:rows]
        Copy.step(windows, self.seen[start : start + C][:rows])
        for j in range(K - 1):
            Copy.step(flat[first + rows + j], self.staged[j])
        Copy.step(self.staged, write)
        return iron.carry(position=position + 1)


def windows(sequence: np.ndarray) -> np.ndarray:
    """Each position's window of ``sequence``, zero before it."""
    padded = np.concatenate([np.zeros((K - 1, W), sequence.dtype), sequence])
    return np.stack([padded[p : p + K] for p in range(len(sequence))])


def tails(sequence: np.ndarray, slots: int) -> np.ndarray:
    """Each slot after ``sequence``'s positions ran: a whole chunk's last
    ``K - 1`` rows at each boundary, the last chunk's so far, zero past it.
    """
    padded = np.concatenate([np.zeros((K - 1, W), sequence.dtype), sequence])
    out = np.zeros((slots, K - 1, W), sequence.dtype)
    n = len(sequence)
    for k in range(1, (n - 1) // C + 2):
        end = min(k * C, n)
        out[k] = padded[end : end + K - 1]
    return out


def calls(sequence: np.ndarray, begin: int, end: int, prompt_end: int):
    """The calls that run positions ``begin`` to ``end``: prompt chunks up
    to ``prompt_end``, then decode steps, each as ``(x, values)``.
    """
    for start in range(begin, prompt_end, C):
        stop = min(start + C, prompt_end)
        x = np.zeros((C, W), sequence.dtype)
        x[: stop - start] = sequence[start:stop]
        yield x, dict(position=stop - 1, start=start, rows=stop - start)
    for p in range(prompt_end, end):
        yield None, dict(position=p, start=0, rows=1)


@pytest.fixture
def sequences():
    rng = np.random.default_rng(0)
    sequence = rng.standard_normal((L, W)).astype(bfloat16)
    turn = rng.standard_normal((C, W)).astype(bfloat16)
    return sequence, turn


def test_a_chunk_that_is_no_power_of_two_is_refused():
    with pytest.raises(ValueError, match="no power of two"):
        Checkpoints.of((3, W), L, 24)


def test_each_slot_holds_the_state_a_boundary_ends(npu2):
    """The slot a call reads and writes, at each position and chunk."""
    tail = Checkpoints.of((K - 1, W), L, C)
    assert tail.slots.shape == ((L - 1) // C + 2, K - 1, W)
    assert [tail.slot(p) for p in (0, 1, C - 1, C, C + 1, L)] == [0, 1, 1, 1, 2, 8]
    # LFM2's 128000 is no whole number of 2048-row chunks.
    assert Checkpoints.of((2, 8), 128000, 2048).slots.shape[0] == 64


def test_a_decode_step_names_its_slots_by_a_floored_position(npu2, sequences):
    """The decode step's slot offsets are ``position // C`` expressions; the
    Emit program the device runs between steps writes them as numpy does.
    """
    sequence, _ = sequences
    window = Window(sequence, C, K)
    recording = window.record()
    slot = (K - 1) * W
    floored = {b.symbol: b.expression for b in recording.bindings if b.expression.down}
    assert len(floored) == 2, recording.bindings
    for p in (1, C - 1, C, C + 1, LAST):
        offsets = sorted(e.evaluate(dict(position=p)) for e in floored.values())
        assert offsets == sorted([((p - 1) // C + 1) * slot, (p // C + 1) * slot]), p

    words, _ = _words(recording)
    site = attach_emit(
        recording, window._parameters.carried, window._carry, slots=len(words)
    )
    parameters = [Parameter(w.symbol, k, "i32", "addr") for k, w in enumerate(words)]
    program = compose(site, recording.carry, words, parameters)
    for p in (C - 1, C, LAST):
        image, state = emit_reference(
            program, np.array([[p - 1], [0]]), slots=len(words)
        )
        assert image.tolist() == [w(dict(position=p)) for w in words], p
        assert state.tolist() == [p]


def test_the_reference_resumes_from_a_boundary_a_decode_step_crossed(npu2, sequences):
    """The graph's reference, call by call: a prompt, decode steps across a
    boundary, then a rerun from that boundary on other rows.
    """
    sequence, turn = sequences
    window = Window(sequence, C, K)
    for x, values in calls(sequence, 0, LAST + 1, PROMPT):
        window.reference(*([] if x is None else [x]), **values)
    np.testing.assert_array_equal(
        window.seen.host[: LAST + 1], windows(sequence[: LAST + 1])
    )
    slots = window.tail.slots.shape[0]
    np.testing.assert_array_equal(
        window.tail.slots.host, tails(sequence[: LAST + 1], slots)
    )

    # A turn from boundary 3, which the decode step at 3 C wrote.
    rerun = np.concatenate([sequence[: 3 * C], turn])
    for x, values in calls(rerun, 3 * C, 4 * C, 4 * C):
        window.reference(x, **values)
    np.testing.assert_array_equal(
        window.seen.host[3 * C : 4 * C], windows(rerun)[3 * C :]
    )
    np.testing.assert_array_equal(window.tail.slots.host[4], tails(rerun, slots)[4])


@pytest.mark.parametrize(
    "full_elf",
    [
        pytest.param(True, marks=pytest.mark.supported_devices("npu2")),
        pytest.param(False, marks=pytest.mark.supported_devices("npu1", "npu2")),
    ],
    ids=["device_loop", "each_step"],
)
def test_a_state_resumes_from_any_chunk_boundary_on_the_device(sequences, full_elf):
    """On the device: a prompt, decode steps across two boundaries (in the
    device's own loop on a full ELF, else each started by the host), then a
    rerun from a boundary a decode step crossed. Every window and every
    slot is numpy's, exactly.
    """
    sequence, turn = sequences
    window = Window(sequence, C, K)
    decode = window.compile(full_elf=full_elf)
    prompt = window.compile(
        x=((C, W), bfloat16),
        full_elf=full_elf,
        **({"feeds": decode} if full_elf else {}),
    )
    assert decode.plan.full_elf is full_elf
    run = list(calls(sequence, 0, LAST + 1, PROMPT))
    chunks = [c for c in run if c[0] is not None]
    for x, values in chunks[:-1]:
        prompt(x, **values)
    x, values = chunks[-1]
    steps = LAST + 1 - PROMPT
    if full_elf:
        loop = iron.CarriedLoop(prompt, decode)
        assert list(loop.run(steps, x, **values)) == list(range(steps))
    else:
        carry = prompt(x, **values)
        for _ in range(steps):
            carry = decode(start=0, rows=1, **carry)
        assert dict(carry) == {"position": LAST + 1}

    slots = window.tail.slots.shape[0]
    seen = decode.read(window.seen)
    np.testing.assert_array_equal(seen[: LAST + 1], windows(sequence[: LAST + 1]))
    np.testing.assert_array_equal(
        decode.read(window.tail.slots), tails(sequence[: LAST + 1], slots)
    )

    rerun = np.concatenate([sequence[: 3 * C], turn])
    for x, values in calls(rerun, 3 * C, 4 * C, 4 * C):
        prompt(x, **values)
    seen = decode.read(window.seen)
    np.testing.assert_array_equal(seen[3 * C : 4 * C], windows(rerun)[3 * C :])
    held = decode.read(window.tail.slots)
    np.testing.assert_array_equal(held[:4], tails(sequence[: LAST + 1], slots)[:4])
    np.testing.assert_array_equal(held[4], tails(rerun, slots)[4])
