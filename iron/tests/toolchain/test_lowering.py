# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every declared operator lowers to an NPU instruction stream.

Needs the mlir-aie package (its bindings generate the MLIR, its ``aiecc``
lowers it) and Peano, but no device: ``--get-npu-insts`` places, routes,
assigns buffer addresses, lowers the DMAs and emits the runtime sequence's
instructions. Peano is there for the kernels and aiecc's probe of each
core, which links the core with them to measure its stack and reserve each
bank's kernel data before placement. What that checks is everything the
operator model owns: the array an operator's ``build()`` builds is placeable and
routable, every descriptor a sequence issues is legal, the resident writes
and barrier sets lower. What it cannot check is the kernels' objects and
the numbers, which need hardware.

The cases are the catalog's own ``Testing`` declarations: each operator's
first default case, and every case it flags ``lower`` for a shape or dtype
decision that one does not reach.
"""

import importlib

import numpy as np
import pytest
from ml_dtypes import bfloat16
from aie.helpers.taplib import PerCall

import iron
from iron import Precision
from iron import Scratchpad
from iron.common import Unresolvable
from iron.common.image.packaging import Kind
from iron.lm import Conv2d, ImagePatches, LogMel
from iron.operators.copy import Copy
from iron.tests.support.declared import declared
from iron.tests.support.lowering import lower, lower_all
from iron.tests.support.tools import DEVICES, requires

pytestmark = requires("aiecc", "peano")


def _cases():
    """Each device's first default case of every operator and the cases
    declared to lower.
    """
    params = []
    for device in sorted(DEVICES):
        firsts = set()
        for name, cls, case in declared(DEVICES[device]()):
            if not case.extensive and name not in firsts:
                firsts.add(name)
            elif not case.lower:
                continue
            params.append(
                pytest.param(device, cls, case, id=f"{device}-{name}-{case.label}")
            )
    return params


@pytest.mark.parametrize("device,cls,case", _cases(), indirect=["device"])
def test_operator_lowers_to_instructions(device, cls, case, tmp_path):
    """Each case lowers, or is skipped with why ``device`` cannot resolve it."""
    try:
        op = cls(**case.kwargs).resolved(device)
    except Unresolvable as e:
        pytest.skip(f"not for {device}: {e}")
    lower(op, tmp_path)


@pytest.mark.parametrize(
    "module,cls_name,kwargs,bound",
    [
        ("relu", "ReLU", dict(size=4096, tile_size=256, num_aie_columns=2), "valid"),
        ("rms_norm", "RMSNorm", dict(rows=64, tile_size=256), "valid"),
        (
            "softmax",
            "Softmax",
            dict(rows=64, cols=256, block=64, num_aie_columns=2),
            "length",
        ),
        ("rope", "RoPE", dict(rows=64, cols=64, num_aie_columns=2), "valid"),
        # These stream every row and bound their compute: no size patch, so
        # they lower all the way through aiecc today.
        (
            "gemm",
            "GEMM",
            dict(M=256, K=64, N=512, num_aie_columns=4, precision=Precision.MEDIUM),
            "valid",
        ),
        (
            "mha",
            "MHA",
            dict(num_heads=4, num_KV_heads=2, seq_len=256, num_pipelines=2),
            "valid",
        ),
        # EmbeddingGemma 2's global layer on four pipelines: K and V re-read
        # their head 128 times, past one descriptor's 64.
        (
            "mha",
            "MHA",
            dict(
                num_heads=4,
                num_KV_heads=1,
                seq_len=2048,
                d=512,
                causal=False,
                num_pipelines=4,
            ),
            "kv_valid",
        ),
    ],
    ids=lambda v: v if isinstance(v, str) and "." not in v else "",
)
def test_a_bounded_operator_lowers(device, module, cls_name, kwargs, bound, tmp_path):
    """An operator with a bounded extent builds its array against the
    per-call words (each core reads its count from the scratchpad) and
    asks the toolchain to patch its descriptors' lengths.
    """
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    op = cls(**kwargs).resolved(device)
    n = PerCall("n", Kind.SCRATCHPAD, np.int32)
    op.use_value(bound, n.affine())  # what x[:n] in a graph does
    lower(op, tmp_path)


class _Features(iron.Graph):
    """Log-mel features, a graph called in this one's body, into a state's
    rows after a zero one.
    """

    def __init__(self, frames: int):
        self.log_mel = LogMel()
        self.features = iron.state((frames + 1, 128))

    def body(self, wave, *, frames: Scratchpad[np.int32]):
        self.log_mel(wave, self.features[1:], frames=frames)
        return Copy.step(self.features)


def test_a_graph_called_in_a_graph_lowers(device, tmp_path):
    """Its operators, recorded into the caller's and bound by the caller's
    per-call value, lower with the values they read.
    """
    recording = _Features(3072).record(wave=((3073 * 160,), np.float32))
    lower_all(recording, tmp_path, device)


class _Subsample(iron.Graph):
    """Two convolutions, graphs called in this one's body, as an audio front
    end subsamples: one channel to 64 as a band, then 64 to 64 by patches.
    """

    def __init__(self, mels: int):
        rng = np.random.default_rng(0)
        self.conv0 = Conv2d(
            rng.standard_normal((64, 1, 3, 3)), mels, stride=2, padding=1, border=1
        )
        self.conv1 = Conv2d(
            rng.standard_normal((64, 64, 3, 3)), mels // 2 + 2, stride=2
        )

    def body(self, x, y, *, n: Scratchpad[np.int32]):
        return self.conv0(x, rows=n), self.conv1(y, rows=n)


def test_convolutions_called_in_a_graph_lower(device, tmp_path):
    mels = 128
    recording = _Subsample(mels).record(
        x=((2 * 256 + 2, mels), bfloat16),
        y=((256 + 2, (mels // 2 + 2) * 64), bfloat16),
    )
    lower_all(recording, tmp_path, device)


class _Pixels(iron.Graph):
    """A vision front end, a graph called in this one's body."""

    def __init__(self):
        self.processor = ImagePatches(256, (480, 640))

    def body(
        self,
        rgb,
        *,
        height: Scratchpad[np.int32],
        width: Scratchpad[np.int32],
        out_height: Scratchpad[np.int32],
        out_width: Scratchpad[np.int32],
    ):
        return self.processor(
            rgb, height=height, width=width, out_height=out_height, out_width=out_width
        )


def test_image_patches_called_in_a_graph_lower(device, tmp_path):
    graph = _Pixels()
    rgb = graph.processor.resample.image_chunks, graph.processor.chunk
    recording = graph.record(rgb=(rgb, np.uint8))
    lower_all(recording, tmp_path, device)
