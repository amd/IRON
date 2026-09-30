#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests of the build, the RTP placement, the weight reads and dispatch
completion.

No test checks an output value. The layer's numerics need the engine's
weights and caches.
"""

import re
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import NPU2
from aie.utils.npukernel import NPUKernel

from iron.common.base import DispatchCallable
from iron.operators.flm.layer.design import (
    LAYER_TYPES,
    RTP_ADDRESSES,
    RTP_SYMBOLS,
    arg_sizes,
    decode_layer,
    weight_layout,
)
from iron.operators.flm.layer.op import GEOMETRIES, DecodeLayer
from iron.operators.flm.testing import requires_aie2p

MODELS = sorted(GEOMETRIES)


def _work_dir(op):
    """The directory aiecc builds op's xclbin in."""
    mlir = Path(op.xclbin_artifact.filename).with_suffix(".mlir")
    return mlir.parent / (mlir.name + ".d")


def _placed_rtps(op):
    """RTP buffer symbol -> the address aiecc placed it at."""
    text = (_work_dir(op) / "input_with_addresses.mlir").read_text()
    return {
        m[2]: int(m[1])
        for m in re.finditer(
            r'\{address = (\d+) : i32[^}]*sym_name = "(RTP_[A-Za-z_0-9]+)"', text
        )
    }


def _device_configuration(op):
    """The CDO the xclbin configures the device with."""
    cdo = _work_dir(op) / "cdo_main"
    return {f.name: f.read_bytes() for f in sorted(cdo.glob("*.bin"))}


def _check_rtps(op):
    """Assert that aiecc placed each RTP buffer at its RTP_ADDRESSES address."""
    placed = _placed_rtps(op)
    want = {RTP_SYMBOLS[k]: RTP_ADDRESSES[op.model][k] for k in RTP_SYMBOLS}
    got = {sym: placed.get(sym) for sym in want}
    assert got == want


CASES = [
    pytest.param(
        m,
        t,
        marks=[] if (m, t) == ("GEMMA4_E2B", "global") else [pytest.mark.extensive],
    )
    for m in MODELS
    for t in LAYER_TYPES
]


@requires_aie2p
@pytest.mark.parametrize("model, layer_type", CASES)
def test_builds(model, layer_type, aie_context):
    op = DecodeLayer(model=model, layer_type=layer_type, context=aie_context)
    op.compile()
    _check_rtps(op)


@requires_aie2p
@pytest.mark.extensive
@pytest.mark.parametrize("model", MODELS)
def test_layer_types_share_one_configuration(model, aie_context):
    """The engine loads one xclbin and runs every layer type's sequence on it."""
    configs = {}
    for layer_type in LAYER_TYPES:
        op = DecodeLayer(model=model, layer_type=layer_type, context=aie_context)
        op.compile()
        configs[layer_type] = _device_configuration(op)
    first = configs[LAYER_TYPES[0]]
    assert first
    for layer_type, config in configs.items():
        assert config == first, f"{layer_type} configures the device differently"


def _inputs(op, seed):
    """Random bf16 in every buffer the sequence takes."""
    rng = np.random.default_rng(seed)
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = []
    for spec in op.get_arg_spec():
        buf = tensor_class(spec.shape, dtype=bfloat16)
        buf.numpy_view()[:] = (rng.standard_normal(spec.shape) * 0.1).astype(bfloat16)
        bufs.append(buf)
    return bufs


@requires_aie2p
@pytest.mark.parametrize("model", MODELS)
def test_dispatches_complete(model, aie_context):
    """Run every layer type's sequence back to back on one xclbin, as the
    engine does.

    A sequence that drives the dataflow differently from the cores hangs. The
    inputs are random. The test checks that each dispatch completes and
    writes x.
    """
    ops = {
        t: DecodeLayer(model=model, layer_type=t, context=aie_context)
        for t in LAYER_TYPES
    }
    for op in ops.values():
        op.compile()
    xclbin = ops["global"].xclbin_artifact
    bufs = _inputs(ops["global"], seed=0)
    x = bufs[0]
    for context_len in (0, 5, 600):
        for t, op in ops.items():
            run = DispatchCallable(
                NPUKernel(
                    xclbin_path=xclbin.filename,
                    kernel_name=xclbin.kernel_name,
                    dispatch_params=list(op.get_dispatch_params()),
                    dispatch_lib_path=Path(op.dispatch_artifact.filename).resolve(),
                )
            )
            before = x.numpy().copy()
            run.set_parameters(context_len=context_len, max_l=4096)
            run(*bufs)
            after = x.numpy()
            d = op.geometry.model_dim
            assert not np.array_equal(
                before[:d], after[:d]
            ), f"{t} at context_len={context_len} left x as it was"


def _ops(op):
    """op and every operation nested in it."""
    yield op
    for region in op.regions:
        for block in region.blocks:
            for inner in block.operations:
                yield from _ops(inner)


def _proj_reads(module):
    """(offset, length) of each BD of the runtime sequence over proj."""
    (seq,) = [op for op in _ops(module.operation) if op.name == "aie.runtime_sequence"]
    proj = seq.regions[0].blocks[0].arguments[1]
    reads = []
    for op in _ops(seq):
        if op.name == "aie.dma_bd" and op.opview.buffer == proj:
            bd = op.opview
            assert bd.offset is None and bd.len is None, "a proj BD is dynamic"
            reads.append((bd.static_offset.value, bd.static_len.value))
    return reads


@pytest.mark.parametrize("layer_type", LAYER_TYPES)
@pytest.mark.parametrize("model", MODELS)
def test_weight_reads_fit_proj(model, layer_type):
    """Each layer type's sequence reads its whole blob and nothing past proj.

    The test reads the BDs out of the generated runtime sequence. The build
    needs no NPU.
    """
    g = GEOMETRIES[model]
    module = decode_layer(NPU2(), g, RTP_ADDRESSES[model], layer_type)
    end = 0
    for offset, length in sorted(_proj_reads(module)):
        assert offset == end, f"the reads skip or reread proj at {offset}"
        end += length
    blob = weight_layout(g, layer_type)
    assert end == max(w.offset + w.size for w in blob.values())
    assert end <= arg_sizes(g)["proj"]


@pytest.mark.parametrize(
    "kwargs, match",
    [
        (dict(model="GEMMA4_E8B", layer_type="global"), "model must be one of"),
        (dict(model="GEMMA4_E2B", layer_type="sliding"), "layer_type must be one of"),
    ],
)
def test_rejects_unknown_configurations(kwargs, match, aie_context):
    with pytest.raises(ValueError, match=match):
        DecodeLayer(context=aie_context, **kwargs)
