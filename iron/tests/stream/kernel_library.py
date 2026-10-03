#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's kernel library must describe what its sources compile, and build every object it names."""

import pathlib

import pytest

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

from stream.compiler.kernels.registry import AIE_KERNELS  # noqa: E402

from iron.common import AIEContext  # noqa: E402
from iron.common.stream.kernel_library import fixed_dims, library  # noqa: E402
from iron.common.stream.ops import TORCH_OPS, artifacts_for_object  # noqa: E402

FLASH_BLOCK = 64


@pytest.mark.parametrize("op", TORCH_OPS.values(), ids=lambda op: op.onnx_type)
def test_every_torch_op_names_a_stream_kernel(op):
    assert op.kernel in AIE_KERNELS


def _library_objects():
    """Every object the library names, at each shape it carries cycles for."""
    names = set()
    for spec in library("aie2p").kernels.values():
        if spec.object is not None:
            shapes = [shape for shape, _ in spec.cycles] or [{}]
            names.update(spec.object.format(**shape) for shape in shapes)
    return sorted(names)


@pytest.mark.parametrize("name", _library_objects())
def test_every_object_the_library_names_has_a_build_rule(name):
    root = AIEContext().kernels_dir
    objects = [
        pathlib.Path(a.filename).name for a in artifacts_for_object(name, root, "aie2p")
    ]
    assert name in objects


# The shapes each source compiles for: mm.cc's divisors, mha.cc's query blocks.
DECLARED_BLOCKS = [
    (
        "matmul_bf16_bf16",
        dict(m=64, k=64, n=64),
        {0: (16, 32, 64), 1: (8, 16, 32, 64), 2: (16, 32, 64)},
    ),
    (
        "matmul_bf16_bf16",
        dict(m=32, k=64, n=64),
        {0: (16, 32), 1: (8, 16, 32, 64), 2: (16, 32, 64)},
    ),
    ("partial_softmax", dict(m=32, n=64), {0: (32, 64)}),
    ("matmul_PV", dict(m=32, k=64, n=64), {0: (32, 64)}),
]


@pytest.mark.parametrize("symbol, shape, expected", DECLARED_BLOCKS)
def test_the_library_declares_the_blocks_the_sources_compile(symbol, shape, expected):
    spec = library("aie2p").spec(symbol)
    for position, sizes in expected.items():
        dim = spec.dim(("m", "k", "n")[position])
        if dim.divisor:
            got, block = [], shape[dim.name]
            while block >= dim.divisor and block % dim.divisor == 0:
                got.append(block)
                block //= 2
            assert tuple(reversed(got)) == sizes, dim.name
        else:
            assert dim.blocks == sizes, dim.name


def test_every_library_entry_names_a_source_that_exists():
    root = AIEContext().kernels_dir
    for symbol, spec in library("aie2p").kernels.items():
        assert (
            root / spec.source
        ).exists(), f"{symbol} names a source that is not there"


def test_the_layout_block_is_the_block_the_source_is_compiled_at():
    """mha.cc's key and head blocks are compiled at the size the flash layouts use."""
    fixed = fixed_dims("matmul_PV", "aie2p")
    assert fixed["k"] == fixed["n"] == FLASH_BLOCK


@pytest.mark.parametrize("block", [32, 64])
def test_the_mha_object_is_built_for_the_block_it_is_named_for(block):
    root = AIEContext().kernels_dir
    objects = artifacts_for_object(f"mha_{block}.o", root, "aie2p")
    names = [artifact.filename for artifact in objects]
    assert f"mha_{block}.o" in names
    flags = [
        f for f in objects[names.index(f"mha_{block}.o")].extra_flags if "DIM" in f
    ]
    assert flags == [f"-DDIM_M={block}", "-DDIM_K=64", "-DDIM_N=64"]


def test_the_gemm_object_is_built_for_the_shape_it_is_named_for():
    root = AIEContext().kernels_dir
    objects = artifacts_for_object("mm_32_64_64.o", root, "aie2p")
    assert any(a.filename == "mm_32_64_64.o" for a in objects)


@pytest.mark.parametrize(
    "name, flag",
    [("silu_1x4096.o", "-DSILU_ELEMS=4096"), ("mul_2x2048.o", "-DMUL_ELEMS=4096")],
)
def test_an_elementwise_object_is_compiled_for_the_elements_a_call_takes(name, flag):
    """Left to its run-time size the loop does not pipeline, and SiLU takes twice as long."""
    (artifact,) = artifacts_for_object(name, AIEContext().kernels_dir, "aie2p")
    assert artifact.filename == name
    assert flag in artifact.extra_flags
