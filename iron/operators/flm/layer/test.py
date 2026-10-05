#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests of the outputs, the RTP placement and the weight reads.

test_matches_reference runs every layer type on synthetic inputs and compares
x and the kv cache with reference.py. test_captured_case does the same on
dispatches captured from FastFlowLM's engine, when FLM_LAYER_CASES names them.
Both check the RTP placement of every build they dispatch.
"""

import dataclasses
import json
import os
import re
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE, FLM_GEMMA4_E4B_DECODE
from aie.utils.benchmark import run_iters
from aie.utils.hostruntime.hostruntime import HostRuntimeError
from ml_dtypes import bfloat16

from iron.common.design import OperatorDesign
from iron.common.image import OperatorImage
from iron.operators.flm.layer.design import (
    LAYER_TYPES,
    MAX_CONTEXT,
    RTP_ADDRESSES,
    RTP_SYMBOLS,
    SLIDING_WINDOW,
    arg_sizes,
    weight_layout,
)
from iron.operators.flm.layer.op import DecodeLayer
from iron.operators.flm.layer.reference import (
    generate_inputs,
    kv_row,
    kv_rows,
    layer_dims,
    proj_layout,
    reference,
)
from iron.operators.flm.testing import requires_aie2p

GEOMETRIES = (FLM_GEMMA4_E2B_DECODE, FLM_GEMMA4_E4B_DECODE)


def _check_rtps(image, geometry):
    """Assert that aiecc placed each RTP buffer of every build of image at its
    RTP_ADDRESSES address.
    """
    want = {RTP_SYMBOLS[k]: RTP_ADDRESSES[geometry][k] for k in RTP_SYMBOLS}
    artifacts = image.artifacts
    for entry in {artifacts.designs[0].entry.directory, artifacts.entry.directory}:
        text = (entry / "input_with_addresses.mlir").read_text()
        placed = {
            m[2]: int(m[1])
            for m in re.finditer(
                r'\{address = (\d+) : i32[^}]*sym_name = "(RTP_[A-Za-z_0-9]+)"', text
            )
        }
        assert {sym: placed.get(sym) for sym in want} == want


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


def _image(geometry, layer_type):
    """layer_type's image. It runs on the global layer's xclbin, as the engine
    does: one xclbin serves all four layer types.
    """
    image = OperatorImage(DecodeLayer(geometry=geometry, layer_type=layer_type))
    _check_rtps(image.compile(), geometry)
    return image


def _record_metrics(record, image, bufs, geometry, layer_type, context_len, max_l):
    """Time one more dispatch and record its latency, bandwidth and throughput.

    The bytes count the weights and the K and V rows that the layer reads. The
    FLOPs count the projections and the attention.
    """
    g = layer_dims(geometry, layer_type)
    blob = weight_layout(geometry, layer_type).values()
    keys = min(context_len + 1, SLIDING_WINDOW) if g["swa"] else context_len + 1
    total_bytes = 2 * (sum(w.size for w in blob) + 2 * keys * g["dk"])
    flops = 2 * sum(w.dout * w.din for w in blob)
    flops += 4 * g["num_attn_heads"] * g["dh"] * keys
    latency_us = run_iters(
        image, *bufs, warmup=1, iters=1, context_len=context_len, max_l=max_l
    ).npu.avg_us
    record("Latency", latency_us)
    record("Bandwidth", total_bytes / latency_us / 1e3)
    record("Throughput", flops / latency_us / 1e3)


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


def check_outputs(geometry, layer_type, context_len, max_l, inputs, x_out, kv_out):
    """Compare x_out and kv_out (bf16) with the reference on inputs.

    Returns the relative L2 errors. Asserts that they are at most RTOL_X and
    RTOL_KV, and that the rest of x and of the kv cache equals the input bit for
    bit.
    """
    x, proj, rms, rope_rms, kv = inputs
    ref_x, ref_kv = reference(
        geometry, layer_type, x, proj, rms, rope_rms, kv, context_len, max_l
    )
    g = layer_dims(geometry, layer_type)
    D, dk = g["model_dim"], g["dk"]
    got_x = np.asarray(x_out).view(np.uint16).reshape(-1)
    got_kv = np.asarray(kv_out).view(np.uint16).reshape(-1)
    errors = {"x": _rel_l2(got_x[:D].view(bfloat16), ref_x[:D].view(bfloat16))}
    rest = np.ones(ref_kv.size, bool)
    if not g["skip"]:
        row = kv_row(geometry, layer_type, context_len)
        v_off = kv_rows(geometry, layer_type, max_l) * dk
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
    for t in LAYER_TYPES
    for c in CONTEXT_LENS[t]
]


@requires_aie2p
@pytest.mark.parametrize("geometry, layer_type, context_len", SYNTHETIC, ids=str)
def test_matches_reference(
    geometry, layer_type, context_len, npu_runtime, record_property
):
    image = _image(geometry, layer_type)
    inputs = generate_inputs(geometry, layer_type, context_len, MAX_L, seed=context_len)
    bufs = _tensors(image.op, inputs)
    full = [b.numpy().copy() for b in bufs]
    image(*bufs, context_len=context_len, max_l=MAX_L)
    check_outputs(
        geometry, layer_type, context_len, MAX_L, full, bufs[0].numpy(), bufs[4].numpy()
    )
    _record_metrics(
        record_property, image, bufs, geometry, layer_type, context_len, MAX_L
    )


@requires_aie2p
@pytest.mark.parametrize(
    "layer_type, context_len, max_l, match",
    [
        ("global", -1, MAX_L, "context_len must be >= 0"),
        ("global", MAX_L, MAX_L, "context_len must be below max_l"),
        ("swa", 37, 2 * MAX_CONTEXT, f"max_l exceeds {MAX_CONTEXT}"),
    ],
)
def test_refuses_unservable_contexts(
    layer_type, context_len, max_l, match, npu_runtime
):
    """The dispatch checks the context before the array runs."""
    image = _image(FLM_GEMMA4_E2B_DECODE, layer_type)
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    bufs = [tensor(b.shape, dtype=bfloat16) for b in image.op.buffers]
    with pytest.raises(HostRuntimeError, match=match):
        image(*bufs, context_len=context_len, max_l=max_l)


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
def test_captured_case(case, npu_runtime, record_property):
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
    image = _image(geometry, layer_type)
    bufs = _tensors(image.op, [np.fromfile(files[k], np.uint8) for k in names])
    full = [b.numpy().copy() for b in bufs]
    image(*bufs, context_len=ctx, max_l=max_l)
    check_outputs(
        geometry, layer_type, ctx, max_l, full, bufs[0].numpy(), bufs[4].numpy()
    )
    for buf, key in ((bufs[0], "x_out"), (bufs[4], "kv_cache_out")):
        if key in files:
            want = np.fromfile(files[key], np.uint8)
            got = buf.numpy().reshape(-1).view(np.uint8)
            n = min(want.size, got.size)
            assert np.array_equal(got[:n], want[:n]), f"{key} differs from the engine's"
    _record_metrics(record_property, image, bufs, geometry, layer_type, ctx, max_l)


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


@pytest.mark.parametrize("layer_type", LAYER_TYPES)
@pytest.mark.parametrize("geometry", GEOMETRIES, ids=str)
def test_weight_reads_fit_proj(geometry, layer_type, npu2):
    """Each layer type's sequence reads its whole blob and nothing past proj.

    The test reads the BDs out of the generated runtime sequence. The build
    needs no NPU.
    """
    g = geometry
    op = DecodeLayer(geometry=g, layer_type=layer_type).resolved()
    module = OperatorDesign(op, "xclbin").compilable().generate_mlir()
    end = 0
    for offset, length in sorted(_proj_reads(module)):
        assert offset == end, f"the reads skip or reread proj at {offset}"
        end += length
    blob = weight_layout(g, layer_type)
    assert end == max(w.offset + w.size for w in blob.values())
    assert end <= arg_sizes(g)["proj"]
    ref = proj_layout(g, layer_type)
    for name in ("o", "up_gate", "down", "pli_down", "pli_gate", "pli_up"):
        assert (blob[name].dout, blob[name].din) == ref[name][2:], name


@pytest.mark.parametrize(
    "kwargs, match",
    [
        (
            dict(
                geometry=dataclasses.replace(
                    FLM_GEMMA4_E2B_DECODE, model_dim=2048, name="gemma4_e8b"
                ),
                layer_type="global",
            ),
            "geometry must be",
        ),
        (
            dict(geometry=FLM_GEMMA4_E2B_DECODE, layer_type="sliding"),
            "layer_type must be one of",
        ),
    ],
    ids=["geometry", "layer_type"],
)
def test_rejects_unknown_configurations(kwargs, match):
    with pytest.raises(ValueError, match=match):
        DecodeLayer(**kwargs)
