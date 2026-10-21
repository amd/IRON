#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's kernel library must describe what its kernels compile, and bind each to a kernel IRON builds."""

import pytest

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

from stream.compiler.kernels.binding import resolve  # noqa: E402
from stream.compiler.kernels.registry import AIE_KERNELS  # noqa: E402

from iron.common.compilation import KernelObjectArtifact  # noqa: E402
from iron.common.stream.kernel_library import fixed_dims, load_library  # noqa: E402
from iron.common.stream.ops import TORCH_OPS  # noqa: E402
from iron.operators.mha_prefill_stream.stream_design import FLASH_BLOCK  # noqa: E402


@pytest.mark.parametrize("op", TORCH_OPS.values(), ids=lambda op: op.onnx_type)
def test_every_torch_op_names_a_stream_kernel(op):
    assert op.kernel in AIE_KERNELS


def _measured_calls():
    """Every kernel the library measures, at each shape it carries cycles for."""
    library = load_library("aie2p")
    return [
        (s, shape) for s, spec in library.kernels.items() for shape, _ in spec.cycles
    ]


@pytest.mark.parametrize("symbol, shape", _measured_calls())
def test_every_measured_kernel_binds_to_an_object_iron_builds(symbol, shape):
    spec = load_library("aie2p").spec(symbol)
    binding = resolve({"binding": spec.binding, "args": {**shape, "npu": "npu2"}})
    artifact = KernelObjectArtifact.from_extern(binding)
    assert artifact.filename == binding.object_file_name


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
    spec = load_library("aie2p").spec(symbol)
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


def test_the_layout_block_is_the_block_the_source_is_compiled_at():
    """mha.cc's key and head blocks are compiled at the size the flash layouts use."""
    fixed = fixed_dims("matmul_PV", "aie2p")
    assert fixed["k"] == fixed["n"] == FLASH_BLOCK
