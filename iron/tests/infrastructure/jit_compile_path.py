#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compiling through CompilableDesign produces a real image, cached by content.

IRON names nothing on disk: every build lands in the JIT cache, keyed on the
content it was built from, and what IRON keeps is the record of what the
image consists of. These check the seam that rests on -- a graph recorded
from dataflow comes out the other side as a linked full ELF, a second
identical build is a cache hit rather than another aiecc run, and the keys
distinguish what must be distinguished.

Needs a device, since the fused path is NPU2-only and the ELF is genuinely
built here rather than mocked.
"""

import aie.utils as aie_utils
import pytest
from aie.iron.device import from_name
from aie.utils.compile.jit.compilabledesign import CompilableDesign

import iron
from iron.common.image.jit_compile import (
    _bind_device,
    _design_generator,
    _params_key,
)
from iron.operators import ElementwiseAdd

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _captured(name, trace_size=0, adds=2):
    """X + w + w (or as many adds of w) as a graph function, fused and compiled."""
    add = ElementwiseAdd(size=1024, tile_size=128)

    @iron.graph
    def f(x, w):
        for _ in range(adds):
            x = add(x, w)
        return x

    sequence = f.trace(x=(1024,), w=(1024,)).sequence(
        name, dispatch="fused", trace_size=trace_size
    )
    return sequence.compile()


def test_captured_graph_compiles_to_an_elf():
    """The load-bearing claim: it links, and the ELF is real."""
    artifacts = _captured("jitpath_elf").artifacts
    elf = artifacts.image
    assert artifacts.kind == "elf" and elf.exists(), "no ELF produced"
    assert elf.stat().st_size > 1024, f"ELF suspiciously small: {elf.stat().st_size}"
    assert elf.read_bytes()[:4] == b"\x7fELF", "not an ELF"
    # It sits in the cache entry, alongside the sidecars a host reads.
    assert elf.parent == artifacts.directory
    assert artifacts.params is not None and artifacts.params.exists()


def test_kernel_objects_land_in_the_entry_under_bare_names():
    """The fused MLIR's link_with names objects without a directory.

    The designs declare ExternalFunctions and CompilableDesign compiles them
    straight into the entry; a fused link must find them by bare name.
    """
    objects = _captured("jitpath_stage").artifacts.entry.objects
    assert objects, "no kernel objects in the cache entry"
    assert all("/" not in p.name for p in objects)


def test_two_graphs_get_distinct_cache_keys():
    """Identity rides in compile_kwargs because the key ignores closures.

    Two graphs of one operator differ only in how many steps they run, which
    no design's code or parameters record. Without the graph's identity in
    the key the second would be handed the first one's ELF, and nothing
    would report it.
    """
    two = _captured("jitpath_graphs", adds=2).artifacts.image
    three = _captured("jitpath_graphs", adds=3).artifacts.image
    assert two != three


def test_identical_sequences_reuse_the_compiled_elf():
    """A fresh, independently-built sequence with the same recipe must not
    pay a second aiecc compile: same entry, untouched.
    """
    first = _captured("jitpath_cache_reuse").artifacts.image
    mtime = first.stat().st_mtime_ns
    second = _captured("jitpath_cache_reuse").artifacts.image
    assert second == first, "an identical recipe landed in a different entry"
    assert (
        second.stat().st_mtime_ns == mtime
    ), "identical recipe recompiled the ELF instead of reusing the cache hit"


def test_identical_operators_reuse_the_compiled_xclbin():
    """The same, for an operator on its own (the separate-dispatch path)."""

    def build():
        op = ElementwiseAdd(size=1024, tile_size=128)
        return op.compile().artifacts

    first = build()
    mtime = first.image.stat().st_mtime_ns
    second = build()
    assert (second.image, second.insts) == (first.image, first.insts)
    assert second.image.stat().st_mtime_ns == mtime


def test_a_traced_build_carries_the_lowered_module():
    """--get-input-with-addresses is what the trace parser reads; the flag
    reaching aiecc is checked by that file being in the entry, not by the
    ELF differing (both builds come out the same size).
    """
    traced = _captured("jitpath_trace_on", trace_size=8192).artifacts
    assert traced.lowered_mlir is not None and traced.lowered_mlir.exists()
    assert traced.image != _captured("jitpath_trace_off").artifacts.image


def _add_key():
    add = ElementwiseAdd(size=1024, tile_size=128)
    fn, _, kwargs = add.generator().resolve()
    return CompilableDesign(
        _design_generator(kwargs),
        compile_kwargs={"design": fn, "params": _params_key(kwargs), "chain": ""},
    )


def test_the_compile_key_is_stable_across_identical_operators():
    """Two operators built the same way must land on one cache entry.

    The key is what makes the seam worth having, and it fails silently when
    it is wrong: an unstable key is not an error, just an aiecc run on every
    call.
    """
    assert _add_key()._compute_cache_hash() == _add_key()._compute_cache_hash()


def test_the_compile_key_does_not_depend_on_a_device_being_bound_yet():
    """The hash must not change once compile() binds the device.

    _compute_artifact_hash reads get_current_device(probe_runtime=False),
    which is None until something binds one, and CompilableDesign.compile()
    binds it from inside. A key computed before that records a "no device"
    identity the next build can never match, so every process would rebuild
    once -- silently, since nothing fails. _bind_device() binds first for
    this reason.
    """
    design = _add_key()
    bound_hash = design._compute_cache_hash()
    aie_utils.set_current_device(None)
    assert design._compute_cache_hash() != bound_hash, (
        "this test is pointless if the hash stopped depending on the device; "
        "it exists because it does"
    )
    _bind_device()
    assert design._compute_cache_hash() == bound_hash


def test_a_device_parameter_is_keyed_by_identity_not_address():
    """A device's str() carries its address, which would re-key every process."""
    dev = from_name("npu2", n_cols=8)
    assert _params_key({"dev": dev}) == _params_key(
        {"dev": from_name("npu2", n_cols=8)}
    )
    assert _params_key({"dev": dev}) != _params_key(
        {"dev": from_name("npu1", n_cols=4)}
    )


def test_a_device_is_recognised_by_shape_not_by_parameter_name():
    """The name a design gives the parameter is not what makes it a device."""
    dev = from_name("npu2", n_cols=8)
    assert _params_key({"target": dev}) == _params_key({"target": dev})


def test_an_opaque_design_parameter_is_rejected():
    """A value whose str() embeds an address is an operator bug, not a
    silently-degraded cache.
    """

    class Opaque:
        pass

    with pytest.raises(ValueError, match="object address"):
        _params_key({"thing": Opaque()})
