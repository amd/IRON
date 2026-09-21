#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compiling a graph function through CompilableDesign produces a real ELF.

This is the step the artifact-graph retirement rests on, so it is checked on
hardware rather than argued about: a graph recorded from dataflow, through the
upstream compile path, out the other side as a linked full ELF.

Needs a device, since the fused path is NPU2-only and the ELF is genuinely
built here rather than mocked.
"""

from pathlib import Path

import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name
from aie.utils.compile.jit.compilabledesign import CompilableDesign

import iron
from iron.common.context import AIEContext
from iron.common.jit_compile import (
    _compile_if_changed,
    compile_sequence,
    compile_xclbin_insts,
    _digest,
    _design_generator,
    _params_key,
)
from iron.operators import ElementwiseAdd


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _captured(name, trace_size=0):
    """x + w + w as a graph function, lowered to a fused sequence and compiled."""
    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())

    @iron.graph
    def f(x, w):
        return add(add(x, w), w)

    sequence = f.trace(x=(1024,), w=(1024,)).sequence(
        name, dispatch="fused", trace_size=trace_size
    )
    sequence.compile()
    return sequence


def test_captured_graph_compiles_to_an_elf(tmp_path):
    """The load-bearing claim: it links, and the ELF is real."""
    sequence = _captured("jitpath_elf")
    elf = compile_sequence(sequence, tmp_path / "graph.elf")
    assert elf.exists(), "no ELF produced"
    assert elf.stat().st_size > 1024, f"ELF suspiciously small: {elf.stat().st_size}"
    assert elf.read_bytes()[:4] == b"\x7fELF", "not an ELF"


def test_kernel_objects_land_in_the_work_dir_under_bare_names(tmp_path):
    """The fused MLIR's link_with names objects without a directory.

    IRON used to copy them there itself, because object_files= only feeds the
    artifact hash. It no longer does: the designs declare ExternalFunctions and
    CompilableDesign compiles them straight into the work dir. The requirement
    is unchanged, so this still checks it -- what was deleted is IRON's
    separate step for meeting it.
    """
    sequence = _captured("jitpath_stage")
    elf = tmp_path / "graph.elf"
    compile_sequence(sequence, elf)
    staged = {p.name for p in elf.with_suffix(".prj").iterdir() if p.suffix == ".o"}
    assert staged, "no kernel objects staged into the work directory"
    assert all("/" not in name for name in staged)


def test_two_graphs_get_distinct_cache_keys():
    """Identity rides in compile_kwargs because the key ignores closures.

    Without this the second graph would be handed the first one's ELF, and
    nothing would report it.
    """
    one = _digest("module { /* graph one */ }")
    two = _digest("module { /* graph two */ }")
    assert one != two


def _captured_traced(name, trace_size):
    return _captured(name, trace_size)


def test_tracing_does_not_reuse_an_untraced_cache_entry():
    """Same MLIR, different flags, so it must be a different cache key.

    Sharing one would hand a traced build the untraced ELF, which loads and
    runs and produces no trace.
    """
    text = "module { /* identical */ }"
    assert {"graph": _digest(text), "trace": 0} != {
        "graph": _digest(text),
        "trace": 8192,
    }


def test_identical_sequences_reuse_the_compiled_elf(tmp_path):
    """A fresh, independently-built sequence with the same recipe must not
    pay a second aiecc compile.

    CompilableDesign.compile() bypasses its own on-disk cache whenever
    explicit output paths are given -- the caller is presumed to manage its
    own dependency tracking. Without that tracking, an unchanged recipe
    recompiled through aiecc every time, not just on an actual edit; measured
    directly by mtime before this was fixed.
    """
    elf = tmp_path / "graph.elf"

    first = compile_sequence(_captured("jitpath_cache_reuse"), elf)
    mtime1 = first.stat().st_mtime_ns

    second = compile_sequence(_captured("jitpath_cache_reuse"), elf)
    mtime2 = second.stat().st_mtime_ns

    assert (
        mtime1 == mtime2
    ), "identical recipe recompiled the ELF instead of reusing the cache hit"


def _add_design(tmp_path):
    """A freshly built ElementwiseAdd, as its generator plus kernel objects.

    Built from a new instance each call: the regression this guards is two
    independently-constructed operators with the same recipe each rebuilding,
    which reusing one instance would not catch.
    """
    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    add.compile()
    objects = [
        Path(a.filename) for a in add.artifacts.bfs() if str(a.filename).endswith(".o")
    ]
    return add.get_mlir_artifact().generator, objects


def test_identical_operator_reuses_the_compiled_xclbin(tmp_path):
    """The same regression, for compile_xclbin_insts (the separate-dispatch
    and standalone-operator path) rather than the fused-ELF one."""
    xclbin_path = tmp_path / "op.xclbin"
    insts_path = tmp_path / "op.bin"

    generator, objects = _add_design(tmp_path)
    first, _ = compile_xclbin_insts(
        generator, xclbin_path, insts_path, kernel_name="MLIR_AIE"
    )
    mtime1 = first.stat().st_mtime_ns

    generator, objects = _add_design(tmp_path)
    second, _ = compile_xclbin_insts(
        generator, xclbin_path, insts_path, kernel_name="MLIR_AIE"
    )
    mtime2 = second.stat().st_mtime_ns

    assert (
        mtime1 == mtime2
    ), "identical recipe recompiled the xclbin instead of reusing the cache hit"


def test_tracing_changes_the_elf(tmp_path):
    """A traced build must differ from an untraced one.

    --get-input-with-addresses does not change the ELF -- both builds come out
    at the same size. What it emits is a side file, input_with_addresses.mlir,
    which is where the trace parser reads the buffer layout and each design's
    traced tiles from. So the flag reaching aiecc has to be checked by that
    file appearing, not by the ELF differing; asserting on size passes for the
    wrong reason and then fails for the right one.
    """
    traced = compile_sequence(_captured_traced("trace_on", 8192), tmp_path / "on.elf")
    work_dir = traced.with_suffix(".prj")
    produced = {p.name for p in work_dir.rglob("input_with_addresses.mlir")}
    assert produced, (
        f"no input_with_addresses.mlir under {work_dir}; the trace parser has "
        "nothing to read, so --get-input-with-addresses is not reaching aiecc"
    )


def test_the_compile_key_is_stable_across_identical_operators():
    """Two operators built the same way must land on one cache entry.

    The key is what makes the seam worth having, and it fails silently when it
    is wrong: an unstable key is not an error, just an aiecc run on every call.
    """

    def key_for():
        add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
        fn, _, kwargs = add.get_mlir_artifact().generator.resolve()
        return CompilableDesign(
            _design_generator(kwargs),
            compile_kwargs={"design": fn, "params": _params_key(kwargs), "chain": ""},
        )._compute_cache_hash()

    assert key_for() == key_for()


def test_a_device_parameter_is_keyed_by_identity_not_address():
    """A device stringifies to ``<abc.NPU2 object at 0x...>``.

    Hashed by str() that would re-key the cache every process, so it is spelled
    the way _compute_artifact_hash spells it. The key must still tell two
    devices apart -- dropping it entirely would be stable and wrong, handing an
    NPU1 build to NPU2.
    """
    npu2 = _params_key({"dev": from_name("npu2", n_cols=8), "M": 8})
    npu1 = _params_key({"dev": from_name("npu1", n_cols=4), "M": 8})
    assert "0x" not in npu2, f"address leaked into the key: {npu2}"
    assert npu2 != npu1, "the key stopped distinguishing devices"


def test_a_device_is_recognised_by_shape_not_by_parameter_name():
    """Designs need not call it ``dev``; what makes it a device is its API."""
    device = from_name("npu2", n_cols=8)
    assert _params_key({"target": device}) == _params_key({"target": device})
    assert "0x" not in _params_key({"target": device})


def test_an_opaque_design_parameter_is_rejected():
    """Anything else carrying an address is an operator bug -- say so loudly."""

    class Opaque:
        pass

    with pytest.raises(ValueError, match="embeds an object address"):
        _params_key({"thing": Opaque(), "M": 8})


def test_the_compile_key_does_not_depend_on_a_device_being_bound_yet(tmp_path):
    """The hash must not change once compile() binds the device.

    _compute_artifact_hash reads get_current_device(probe_runtime=False), which
    is None until something binds one, and CompilableDesign.compile() binds it
    from inside. A key computed before that records a "no device" identity the
    next build can never match, so every process rebuilds once -- silently,
    since nothing fails. _compile_if_changed binds first for this reason.

    The device is left unset before the call on purpose: bound beforehand, the
    binding inside is never needed and this passes without it.
    """
    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    fn, _, kwargs = add.get_mlir_artifact().generator.resolve()
    design = CompilableDesign(
        _design_generator(kwargs),
        compile_kwargs={"design": fn, "params": _params_key(kwargs), "chain": ""},
    )
    bound_hash = design._compute_cache_hash()

    aie_utils.set_current_device(None)
    assert design._compute_cache_hash() != bound_hash, (
        "this test is pointless if the hash stopped depending on the device; "
        "it exists because it does"
    )

    _, current, _ = _compile_if_changed(design, tmp_path / "op.xclbin")
    assert current == bound_hash, (
        "_compile_if_changed hashed before binding the device, so the stamp it "
        "writes records an identity that compile() will never reproduce"
    )
