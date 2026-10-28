# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests of the outputs and the weight reads.

test_matches_reference runs every layer type on synthetic inputs and compares
x and the kv cache with reference.py. test_captured_case does the same on
dispatches captured from FastFlowLM's engine, when FLM_LAYER_CASES names them.
"""

import json
import os
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE, FLM_GEMMA4_E4B_DECODE
from aie.utils.hostruntime.hostruntime import HostRuntimeError
from ml_dtypes import bfloat16

from iron.common.design import OperatorDesign
from iron.common.testing import time_call
from iron.operators.flm.layer.design import (
    GEOMETRIES,
    MAX_CONTEXT,
    SLIDING_WINDOW,
    LayerType,
    arg_sizes,
)
from iron.operators.flm.layer.op import DecodeLayer
from iron.operators.flm.layer.reference import generate_inputs

# The largest relative L2 errors of x and of the new K and V rows.
#
# The reference matches the device bit for bit on most dispatches. On the rest,
# one bf16 output of an RMS norm or of the attention differs by 1 ulp, and the
# MLP spreads the difference over x. The new K and V rows have matched bit for
# bit. The needle rows of generate_inputs make a layer that reads a wrong set
# of cache rows miss x by far more than RTOL_X.
RTOL_X = 1e-2
RTOL_KV = 2e-3

# Synthetic dispatches. A global layer runs near the start of its cache and deep
# into it. A sliding-window layer runs before its 512-row ring is full, at the
# wrap and after it.
MAX_L = 1024
CONTEXT_LENS = {
    "global": (5, 700),
    "swa": (37, 511, 512, 700, 1023),
    "global_skip": (37, 700),
    "swa_skip": (37, 511, 512, 700, 1023),
}


def _layer(geometry, layer_type):
    """layer_type's layer, compiled. It runs on the global layer's xclbin, as
    the engine does: one xclbin serves all four layer types.
    """
    op = DecodeLayer(geometry=geometry, layer_type=layer_type)
    op.compile()
    return op


def _record_metrics(record, op, bufs, context_len, max_l):
    """Time one more dispatch and record its latency, bandwidth and
    throughput; bytes count the weights and K/V rows read, FLOPs the
    projections and attention.
    """
    g = op.dims
    blob = g.weights.values()
    keys = min(context_len + 1, SLIDING_WINDOW) if g.swa else context_len + 1
    total_bytes = 2 * (sum(w.size for w in blob) + 2 * keys * g.dk)
    flops = 2 * sum(w.dout * w.din for w in blob)
    flops += 4 * g.geometry.num_attn_heads * g.dh * keys
    time_call(
        op,
        *bufs,
        bytes_moved=total_bytes,
        ops=flops,
        warmup=1,
        iters=1,
        record=record,
        context_len=context_len,
        max_l=max_l,
    )


def _tensors(op, inputs):
    """Device buffers of op's sizes, with inputs at their start."""
    out = []
    for buf, data in zip(op.buffers, inputs):
        t = aie_utils.DEFAULT_TENSOR_CLASS(buf.shape, dtype=bfloat16)
        view = t.numpy_view().reshape(-1).view(np.uint8)
        view[:] = 0
        data = np.ascontiguousarray(data).reshape(-1).view(np.uint8)[: view.size]
        view[: data.size] = data
        out.append(t)
    return out


def _rel_l2(got, want):
    got, want = (np.asarray(v, np.float64) for v in (got, want))
    return np.linalg.norm(got - want) / max(np.linalg.norm(want), 1e-30)


def check_outputs(op, context_len, max_l, inputs, x_out, kv_out):
    """Compare x_out and kv_out (bf16) with op's reference on inputs,
    asserting RTOL_X/RTOL_KV relative L2 error and bit-exact agreement
    elsewhere; returns the relative L2 errors.
    """
    ref_x, ref_kv = op.reference(*inputs, context_len, max_l)
    g = op.dims
    D, dk = g.geometry.model_dim, g.dk
    got_x, got_kv = (np.asarray(b).reshape(-1).view(bfloat16) for b in (x_out, kv_out))
    errors = {"x": _rel_l2(got_x[:D], ref_x[:D])}
    rest = np.ones(ref_kv.size, bool)
    if not g.skip:
        row = g.kv_row(context_len)
        v_off = g.kv_rows(max_l) * dk
        for name, start in (("k", row * dk), ("v", v_off + row * dk)):
            rows = slice(start, start + dk)
            errors[name] = _rel_l2(got_kv[rows], ref_kv[rows])
            rest[rows] = False

    assert np.array_equal(
        got_x[D:].view(np.uint16), ref_x[D:].view(np.uint16)
    ), "the layer wrote x past its output"
    assert np.array_equal(
        got_kv[rest].view(np.uint16), ref_kv[rest].view(np.uint16)
    ), "the layer wrote other kv rows"
    limits = {"x": RTOL_X, "k": RTOL_KV, "v": RTOL_KV}
    assert all(
        e <= limits[k] for k, e in errors.items()
    ), f"relative L2 errors {errors}"
    return errors


# The dispatches whose measurements CI tracks: deep into a global and a
# sliding-window layer's cache.
BENCH = {(FLM_GEMMA4_E2B_DECODE, "global", 700), (FLM_GEMMA4_E2B_DECODE, "swa", 700)}

SYNTHETIC = [
    pytest.param(
        g,
        t,
        c,
        marks=([] if g == FLM_GEMMA4_E2B_DECODE else [pytest.mark.extensive])
        + ([pytest.mark.bench] if (g, t, c) in BENCH else []),
    )
    for g in GEOMETRIES
    for t in LayerType
    for c in CONTEXT_LENS[t]
]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("geometry, layer_type, context_len", SYNTHETIC, ids=str)
def test_matches_reference(geometry, layer_type, context_len, record_property):
    op = _layer(geometry, layer_type)
    inputs = generate_inputs(op.dims, context_len, MAX_L, seed=context_len)
    bufs = _tensors(op, inputs)
    full = [b.numpy().copy() for b in bufs]
    op(*bufs, context_len=context_len, max_l=MAX_L)
    check_outputs(op, context_len, MAX_L, full, bufs[0].numpy(), bufs[4].numpy())
    _record_metrics(record_property, op, bufs, context_len, MAX_L)


@pytest.mark.supported_devices("npu2")
def test_layer_types_take_turns():
    """Global and sliding-window layers past the window, one after another on
    one loaded array, as the engine's runlist runs them.
    """
    context_len = 700
    for layer_type in ("global", "swa", "global"):
        op = _layer(FLM_GEMMA4_E2B_DECODE, layer_type)
        inputs = generate_inputs(op.dims, context_len, MAX_L, seed=context_len)
        bufs = _tensors(op, inputs)
        full = [b.numpy().copy() for b in bufs]
        op(*bufs, context_len=context_len, max_l=MAX_L)
        check_outputs(op, context_len, MAX_L, full, bufs[0].numpy(), bufs[4].numpy())


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "layer_type, context_len, max_l, match",
    [
        ("global", -1, MAX_L, "context_len must be >= 0"),
        ("global", MAX_L, MAX_L, "context_len must be below max_l"),
        ("swa", 37, 2 * MAX_CONTEXT, f"max_l exceeds {MAX_CONTEXT}"),
    ],
)
def test_refuses_unservable_contexts(layer_type, context_len, max_l, match):
    """The dispatch checks the context before the array runs."""
    op = _layer(FLM_GEMMA4_E2B_DECODE, layer_type)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = [tensor(b.shape, dtype=bfloat16) for b in op.buffers]
    with pytest.raises(HostRuntimeError, match=match):
        op(*bufs, context_len=context_len, max_l=max_l)


def _captured_cases():
    root = os.environ.get("FLM_LAYER_CASES")
    if not root:
        return [
            pytest.param(
                None, marks=pytest.mark.skip(reason="FLM_LAYER_CASES is not set")
            )
        ]
    return sorted(p.parent for p in Path(root).rglob("manifest.json"))


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "case", _captured_cases(), ids=lambda p: p and f"{p.parent.name}/{p.name}"
)
def test_captured_case(case, record_property):
    """A dispatch captured from the engine by an FLM_PLUGIN that hooks
    decode.layer. The output must also equal the engine's bit for bit.
    """
    man = json.loads((case / "manifest.json").read_text())
    geometry = {"E2B": FLM_GEMMA4_E2B_DECODE, "E4B": FLM_GEMMA4_E4B_DECODE}[
        man["model"].split("-")[1]
    ]
    layer_type, ctx, max_l = man["layer_type"], man["context_len"], man["max_l"]
    names = ("x_in", "proj_weights", "rms_weights", "rope_rms_weights", "kv_cache_in")
    files = {
        k: case / man["files"][k]["file"]
        for k in names + ("x_out", "kv_cache_out")
        if k in man["files"]
    }
    op = _layer(geometry, layer_type)
    bufs = _tensors(op, [np.fromfile(files[k], np.uint8) for k in names])
    full = [b.numpy().copy() for b in bufs]
    op(*bufs, context_len=ctx, max_l=max_l)
    check_outputs(op, ctx, max_l, full, bufs[0].numpy(), bufs[4].numpy())
    for buf, key in ((bufs[0], "x_out"), (bufs[4], "kv_cache_out")):
        if key in files:
            want = np.fromfile(files[key], np.uint8)
            got = buf.numpy().reshape(-1).view(np.uint8)
            n = min(want.size, got.size)
            assert np.array_equal(got[:n], want[:n]), f"{key} differs from the engine's"
    _record_metrics(record_property, op, bufs, ctx, max_l)


def _ops(op):
    """Yield `op` and every operation nested in it."""
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


@pytest.mark.parametrize("layer_type", LayerType)
@pytest.mark.parametrize("geometry", GEOMETRIES, ids=str)
def test_weight_reads_fit_proj(geometry, layer_type, npu2):
    """Each layer type's sequence reads its whole blob and nothing past proj,
    checked from the generated runtime sequence's BDs; the build needs no NPU.
    """
    g = geometry
    op = DecodeLayer(geometry=g, layer_type=layer_type).resolved()
    module = OperatorDesign(op, full_elf=False).compilable().generate_mlir()
    end = 0
    for offset, length in sorted(_proj_reads(module)):
        assert offset == end, f"the reads skip or reread proj at {offset}"
        end += length
    blob = op.dims.weights
    assert end == max(w.offset + w.size for w in blob.values())
    assert end <= arg_sizes(g)["proj"]
