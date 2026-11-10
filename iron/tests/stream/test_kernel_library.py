# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON's stream-dse kernel library describes kernels mlir-aie builds."""

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from aie.iron import ExternalFunction  # noqa: E402
from stream.compiler.kernels.binding import resolve  # noqa: E402
from stream.compiler.kernels.registry import AIE_KERNELS  # noqa: E402

from iron.common.stream.kernel_library import (  # noqa: E402
    blocks,
    library_path,
    load_library,
    pinned_to_block,
)
from iron.common.stream.ops import TORCH_OPS  # noqa: E402

pytestmark = pytest.mark.usefixtures("npu2")


@pytest.mark.parametrize("op", TORCH_OPS.values(), ids=lambda op: op.onnx_type)
def test_every_torch_op_names_a_stream_kernel(op):
    assert op.kernel in AIE_KERNELS


def _measured_calls():
    library = load_library("aie2p")
    return [
        pytest.param(symbol, shape, id=f"{symbol}-{'x'.join(map(str, shape.values()))}")
        for symbol, spec in library.kernels.items()
        for shape, _ in spec.cycles
    ]


@pytest.mark.parametrize("symbol, shape", _measured_calls())
def test_every_measured_kernel_binds_to_an_mlir_aie_kernel(symbol, shape):
    spec = load_library("aie2p").spec(symbol)
    binding = resolve({"binding": spec.binding, "args": {**shape, "npu": "npu2"}})
    assert isinstance(binding, ExternalFunction)
    assert binding.name.endswith(symbol)


def test_a_pinned_library_offers_one_block():
    pinned = pinned_to_block("aie2p", 64)
    assert pinned.spec("partial_softmax").dim("m").blocks == (64,)
    assert blocks("aie2p", "partial_softmax", "m") == (32, 64)
    with pytest.raises(ValueError, match="not 16"):
        pinned_to_block("aie2p", 16)


def test_an_architecture_without_a_library_is_refused():
    assert library_path("aie2p").exists()
    with pytest.raises(FileNotFoundError, match="aie2"):
        load_library("aie2")
