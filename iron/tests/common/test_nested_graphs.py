# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A graph called in another graph's body, device-free: its steps record into
the caller's, its weights take the caller's path to it, the caller's per-call
values bound its steps, and the caller's reference runs it.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Carried, Scratchpad
from iron.lm import LogMel
from iron.tests.support.graphs import FeedForward
from iron.tests.support.log_mel import EVERY, Extractor
from iron.operators.copy import Copy
from iron.operators.gemm import GEMM
from iron.operators.limbs import Limbs
from iron.operators.log import Log
from iron.operators.magnitude import Magnitude
from iron.operators.relu import ReLU

pytestmark = pytest.mark.usefixtures("npu2")

FRAMES = 128
SAMPLES = (FRAMES + 1) * 160
E, H = 512, 1024


def weight(rng, rows, cols):
    return (rng.standard_normal((rows, cols)) / np.sqrt(cols)).astype(bfloat16)


class Block(iron.Graph):
    """A feed-forward held as a graph and called in this one's body."""

    def __init__(self):
        rng = np.random.default_rng(0)
        self.ffn = FeedForward(weight(rng, H, E), weight(rng, H, E), weight(rng, E, H))

    def body(self, x):
        return ReLU.step(self.ffn(x))


class Inline(iron.Graph):
    """The same feed-forward written into the body."""

    def __init__(self, ffn: FeedForward):
        self.ffn = ffn

    def body(self, x):
        return ReLU.step(self.ffn.body(x))


class Features(iron.Graph):
    """Log-mel features into a state's rows after a zero one, bounded per call."""

    def __init__(self):
        self.log_mel = LogMel()
        self.features = iron.state((FRAMES + 1, 128))

    def body(self, wave, *, frames: Scratchpad[np.int32]):
        self.log_mel(wave, self.features[1:], frames=frames)
        return Copy.step(self.features)


def test_a_called_graph_records_into_its_caller():
    block = Block()
    called = block.record(x=((256, E), bfloat16))
    inline = Inline(block.ffn).record(x=((256, E), bfloat16))
    assert [s.op.design_key() for s in called.steps] == [
        s.op.design_key() for s in inline.steps
    ]
    names = {h.name for _, h in called.weights.values()}
    assert names == {"ffn.w_gate", "ffn.w_up", "ffn.w_down"}


def test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value():
    recording = Features().record(wave=((SAMPLES,), np.float32))
    assert [type(s.op) for s in recording.steps] == [
        Copy,
        Limbs,
        GEMM,
        Magnitude,
        Limbs,
        GEMM,
        Log,
        Copy,
    ]
    bound = {
        type(b.op) for b in recording.bindings if b.expression.value.name == "frames"
    }
    assert {Limbs, GEMM, Magnitude, Log} <= bound
    assert recording.steps[6].outputs[0].name == "features"
    names = {h.name for _, h in recording.weights.values()}
    assert {"log_mel.dft", "log_mel.filterbank"} <= names


def test_the_callers_reference_runs_the_called_graph():
    block = Block()
    x = np.random.default_rng(1).standard_normal((256, E)).astype(bfloat16)
    got = np.asarray(block.reference(x))
    want = np.maximum(np.asarray(block.ffn.reference(x)).astype(np.float32), 0)
    assert np.array_equal(
        got.astype(np.float32), want.astype(bfloat16).astype(np.float32)
    )
    wave = np.random.default_rng(2).standard_normal(SAMPLES).astype(np.float32)
    features = np.asarray(Features().reference(wave, frames=FRAMES))
    alone = np.asarray(LogMel().reference(wave, frames=FRAMES))
    assert np.array_equal(features[1:].view(np.uint16), alone.view(np.uint16))


class Counter(iron.Graph):
    def body(self, x, *, step: Carried[np.int32]):
        return ReLU.step(x), iron.carry(step=step + 1)


class CallsCounter(iron.Graph):
    def __init__(self):
        self.counter = Counter()

    def body(self, x, *, step: Scratchpad[np.int32]):
        return self.counter(x, step=step)[0]


class Rows(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(x[:n])


class CallsWithoutValue(iron.Graph):
    def __init__(self):
        self.rows = Rows()

    def body(self, x):
        return self.rows(x)


def test_a_called_graph_takes_every_value_and_carries_none():
    with pytest.raises(TypeError, match="carries no values"):
        CallsCounter().record(x=((256, E), bfloat16))
    with pytest.raises(TypeError, match="per-call values"):
        CallsWithoutValue().record(x=((256, E), bfloat16))


def test_log_mel_holds_to_the_extractor(golden):
    """The operators' exact products against Hugging Face's Gemma 4
    extractor's float64, every 8th frame: each feature its bf16 rounding
    or the next, bar a log near 0 within 4e-6.
    """
    log_mel = LogMel()
    frames = 256
    n = (frames + 1) * log_mel.hop
    t = np.arange(n) / 16000
    wave = (0.5 * np.sin(2 * np.pi * (200 * t + 300 * t**2))).astype(np.float32)
    wave += 0.05 * np.random.default_rng(0).standard_normal(n).astype(np.float32)
    got = np.asarray(log_mel.reference(wave, frames=frames), np.float32)[::EVERY]
    want = golden("log_mel", Extractor).logits((), wave)
    ulp = 2.0 ** (np.floor(np.log2(np.abs(want).clip(1e-30))) - 7)
    # Measured: 0.99951 exact.
    assert np.mean(got == want) >= 0.999
    assert (np.abs(got - want) <= np.maximum(ulp, 4e-6)).all()
