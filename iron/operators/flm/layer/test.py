#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests of the build, the RTP placement, the weight reads and the outputs.

test_matches_reference runs every layer type on synthetic inputs and compares
x and the kv cache with reference.py. test_captured_case does the same on
dispatches captured from FastFlowLM's engine, when FLM_LAYER_CASES names them.
"""

import json
import os
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
    layer_kernels,
    weight_layout,
)
from iron.operators.flm.layer.op import GEOMETRIES, DecodeLayer
from iron.operators.flm.layer.reference import (
    generate_inputs,
    geometry,
    kv_row,
    kv_rows,
    reference,
)
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


# The largest relative L2 errors of x and of the new K and V rows.
#
# The reference matches the device bit for bit on most dispatches. On the rest,
# one bf16 output of an RMS norm or of the attention differs by 1 ulp, and the
# MLP spreads the difference over x. The new K and V rows have matched bit for
# bit on every dispatch so far. The needle rows of generate_inputs make each
# injected bug of README.md cost x far more than RTOL_X.
RTOL_X = 1e-2
RTOL_KV = 2e-3

# Synthetic dispatches. A global layer runs near the start of its cache and deep
# into it. A sliding-window layer runs before its 512-row ring is full, at the
# wrap and after it.
MAX_L = 1024
CONTEXT_LENS = {
    "global": (5, 700),
    "swa": (37, 511, 700),
    "global_skip": (37, 700),
    "swa_skip": (37, 511, 700),
}


def _dispatch(ops, layer_type, bufs, context_len, max_l):
    """Run layer_type's sequence on the global layer's xclbin, as the engine
    does: one xclbin serves all four layer types."""
    xclbin = ops["global"].xclbin_artifact
    op = ops[layer_type]
    run = DispatchCallable(
        NPUKernel(
            xclbin_path=xclbin.filename,
            kernel_name=xclbin.kernel_name,
            dispatch_params=list(op.get_dispatch_params()),
            dispatch_lib_path=Path(op.dispatch_artifact.filename).resolve(),
        )
    )
    run.set_parameters(context_len=context_len, max_l=max_l)
    run(*bufs)


def _tensors(op, inputs):
    """Device buffers of the arg spec sizes, with inputs at their start."""
    out = []
    for spec, data in zip(op.get_arg_spec(), inputs):
        t = aie_utils.DEFAULT_TENSOR_CLASS(spec.shape, dtype=bfloat16)
        view = t.numpy_view().reshape(-1).view(np.uint8)
        view[:] = 0
        data = np.ascontiguousarray(data).reshape(-1).view(np.uint8)[: view.size]
        view[: data.size] = data
        out.append(t)
    return out


def _rel_l2(got, want):
    got, want = (np.asarray(v, np.float64) for v in (got, want))
    return np.linalg.norm(got - want) / max(np.linalg.norm(want), 1e-30)


def check_outputs(model, layer_type, context_len, max_l, inputs, x_out, kv_out):
    """Compare x_out and kv_out (bf16) with the reference on inputs.

    Returns the relative L2 errors. Asserts that they are at most RTOL_X and
    RTOL_KV, and that the rest of x and of the kv cache equals the input bit for
    bit.
    """
    ref_x, ref_kv = reference(model, layer_type, *inputs, context_len, max_l)
    g = geometry(model, layer_type)
    D, dk = g["D"], g["dk"]
    got_x = np.asarray(x_out).view(np.uint16).reshape(-1)
    got_kv = np.asarray(kv_out).view(np.uint16).reshape(-1)
    errors = {"x": _rel_l2(got_x[:D].view(bfloat16), ref_x[:D].view(bfloat16))}
    rest = np.ones(ref_kv.size, bool)
    if not g["skip"]:
        row = kv_row(model, layer_type, context_len)
        v_off = kv_rows(model, layer_type, max_l) * dk
        for name, start in (("k", row * dk), ("v", v_off + row * dk)):
            rows = slice(start, start + dk)
            errors[name] = _rel_l2(
                got_kv[rows].view(bfloat16), ref_kv[rows].view(bfloat16)
            )
            rest[rows] = False
    assert np.array_equal(got_x[D:], ref_x[D:]), "the layer wrote x past its output"
    assert np.array_equal(got_kv[rest], ref_kv[rest]), "the layer wrote other kv rows"
    limits = {"x": RTOL_X, "k": RTOL_KV, "v": RTOL_KV}
    assert all(
        e <= limits[k] for k, e in errors.items()
    ), f"relative L2 errors {errors}"
    return errors


def _ops_for(model, layer_type, aie_context):
    names = {"global", layer_type}
    ops = {
        t: DecodeLayer(model=model, layer_type=t, context=aie_context) for t in names
    }
    for op in ops.values():
        op.compile()
    return ops


SYNTHETIC = [
    pytest.param(m, t, c, marks=[] if m == "GEMMA4_E2B" else [pytest.mark.extensive])
    for m in MODELS
    for t in LAYER_TYPES
    for c in CONTEXT_LENS[t]
]


@requires_aie2p
@pytest.mark.parametrize("model, layer_type, context_len", SYNTHETIC)
def test_matches_reference(model, layer_type, context_len, aie_context):
    ops = _ops_for(model, layer_type, aie_context)
    inputs = generate_inputs(model, layer_type, context_len, MAX_L, seed=context_len)
    bufs = _tensors(ops[layer_type], inputs)
    full = [b.numpy().copy() for b in bufs]
    _dispatch(ops, layer_type, bufs, context_len, MAX_L)
    check_outputs(
        model, layer_type, context_len, MAX_L, full, bufs[0].numpy(), bufs[4].numpy()
    )


def _captured_cases():
    root = os.environ.get("FLM_LAYER_CASES")
    if not root:
        return [
            pytest.param(
                None, marks=pytest.mark.skip(reason="FLM_LAYER_CASES is not set")
            )
        ]
    return sorted(p.parent for p in Path(root).rglob("manifest.json"))


@requires_aie2p
@pytest.mark.parametrize(
    "case", _captured_cases(), ids=lambda p: p and f"{p.parent.name}/{p.name}"
)
def test_captured_case(case, aie_context):
    """A dispatch captured from the engine by an FLM_PLUGIN that hooks
    decode.layer. The output must also equal the engine's bit for bit."""
    man = json.loads((case / "manifest.json").read_text())
    model = "GEMMA4_" + man["model"].split("-")[1]
    layer_type, ctx, max_l = man["layer_type"], man["context_len"], man["max_l"]
    names = ("x_in", "proj_weights", "rms_weights", "rope_rms_weights", "kv_cache_in")
    files = {
        k: case / man["files"][k]["file"]
        for k in names + ("x_out", "kv_cache_out")
        if k in man["files"]
    }
    ops = _ops_for(model, layer_type, aie_context)
    bufs = _tensors(ops[layer_type], [np.fromfile(files[k], np.uint8) for k in names])
    full = [b.numpy().copy() for b in bufs]
    _dispatch(ops, layer_type, bufs, ctx, max_l)
    check_outputs(model, layer_type, ctx, max_l, full, bufs[0].numpy(), bufs[4].numpy())
    for buf, key in ((bufs[0], "x_out"), (bufs[4], "kv_cache_out")):
        if key in files:
            want = np.fromfile(files[key], np.uint8)
            got = buf.numpy().reshape(-1).view(np.uint8)
            n = min(want.size, got.size)
            assert np.array_equal(got[:n], want[:n]), f"{key} differs from the engine's"


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


@pytest.fixture
def npu2():
    """NPU2 as the selected device, for a build without an NPU."""
    previous = aie_utils.get_current_device(probe_runtime=False)
    dev = NPU2()
    aie_utils.set_current_device(dev)
    yield dev
    aie_utils.set_current_device(previous)


@pytest.mark.parametrize("layer_type", LAYER_TYPES)
@pytest.mark.parametrize("model", MODELS)
def test_weight_reads_fit_proj(model, layer_type, npu2):
    """Each layer type's sequence reads its whole blob and nothing past proj.

    The test reads the BDs out of the generated runtime sequence. The build
    needs no NPU.
    """
    g = GEOMETRIES[model]
    module = decode_layer(
        npu2, g, RTP_ADDRESSES[model], layer_type, kernels=layer_kernels(g)
    )
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
