#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Direct test of _forward_layer() implementation.

This script tests the _forward_layer() method directly without
importing the full iron package to avoid dependency issues.
"""

import sys
import numpy as np
from typing import Any, List, Dict
from unittest.mock import MagicMock

# ============================================================
# STEP 1: Setup ALL mocks BEFORE any imports
# ============================================================

print("Setting up comprehensive mocks...")


# Mock classes for aie
class AIEConfig:
    DEBUG = False
    ENABLE_PROFILING = False
    DEVICE_INDEX = 0

    @staticmethod
    def get_device_count() -> int:
        return 0

    @staticmethod
    def get_device_info(index: int = 0) -> dict:
        return {"device_id": 0, "device_name": "Mock AIE Device"}


class NPU1:
    pass


class NPU2:
    pass


class DefaultNPURuntime:
    pass


class NPUKernel:
    def __init__(self, *args, **kwargs):
        pass


class AIEUtils:
    config = AIEConfig()
    DefaultNPURuntime = DefaultNPURuntime


class AIEUtilsNPUKernel:
    NPUKernel = NPUKernel


class AIEIronDevice:
    NPU1 = NPU1
    NPU2 = NPU2


class AIEExtrasContext:
    @staticmethod
    def mlir_mod_ctx():
        from contextlib import nullcontext

        return nullcontext()


# Mock pyxrt
class pyxrt:
    XCL_BO_FLAGS_NONE = 0
    XCL_BO_FLAGS_CACHEABLE = 1
    XCL_BO_FLAGS_P2P = 2

    @staticmethod
    def device(index=0):
        return MagicMock()

    @staticmethod
    def hw_context(device):
        return MagicMock()


# Create and register mock modules
aie_mock = MagicMock()
aie_mock.utils = AIEUtils()
aie_mock.pyxrt = pyxrt
aie_mock.iron = MagicMock()
aie_mock.iron.device = AIEIronDevice

aie_extras_mock = MagicMock()
aie_extras_mock.context = AIEExtrasContext()

sys.modules["aie"] = aie_mock
sys.modules["aie.utils"] = AIEUtils
sys.modules["aie.utils.config"] = AIEConfig
sys.modules["aie.utils.npukernel"] = AIEUtilsNPUKernel
sys.modules["aie.extras"] = aie_extras_mock
sys.modules["aie.extras.context"] = aie_extras_mock
sys.modules["aie.iron"] = MagicMock()
sys.modules["aie.iron.device"] = AIEIronDevice
sys.modules["pyxrt"] = pyxrt

# Mock the missing gap_analyzer module
gap_analyzer_mock = MagicMock()
gap_analyzer_mock.GapAnalyzer = MagicMock()
gap_analyzer_mock.generate_gap_report = MagicMock()
gap_analyzer_mock.quick_check = MagicMock()
sys.modules["iron.model_convert.gap_analyzer"] = gap_analyzer_mock

# Mock architecture_scanner
sys.modules["iron.model_convert.architecture_scanner"] = MagicMock()

print("  Mocks registered")

# ============================================================
# STEP 2: Import iron modules
# ============================================================

print("Importing iron modules...")
import logging

logging.basicConfig(level=logging.WARNING)

from iron.models.llama32.config import Llama32Config
from iron.models.llama32.weights import LlamaWeights, TransformerWeights
from iron.generation.loop import GenerationLoop
from iron.api.generation_config import GenerationConfig

# ============================================================
# STEP 3: Test functions
# ============================================================


def create_test_weights(config: Llama32Config) -> LlamaWeights:
    """Create random test weights."""
    layers = []

    for _ in range(config.num_hidden_layers):
        layer = TransformerWeights(
            wq=np.random.randn(
                config.hidden_size, config.num_attention_heads * config.head_dim
            ).astype(np.float32)
            * 0.02,
            wk=np.random.randn(
                config.hidden_size, config.num_key_value_heads * config.head_dim
            ).astype(np.float32)
            * 0.02,
            wv=np.random.randn(
                config.hidden_size, config.num_key_value_heads * config.head_dim
            ).astype(np.float32)
            * 0.02,
            wo=np.random.randn(
                config.num_attention_heads * config.head_dim, config.hidden_size
            ).astype(np.float32)
            * 0.02,
            w1=np.random.randn(config.hidden_size, config.intermediate_size).astype(
                np.float32
            )
            * 0.02,
            w2=np.random.randn(config.intermediate_size, config.hidden_size).astype(
                np.float32
            )
            * 0.02,
            w3=np.random.randn(config.hidden_size, config.intermediate_size).astype(
                np.float32
            )
            * 0.02,
            attn_norm=np.ones(config.hidden_size, dtype=np.float32),
            ffn_norm=np.ones(config.hidden_size, dtype=np.float32),
        )
        layers.append(layer)

    return LlamaWeights(
        token_embd=np.random.randn(config.vocab_size, config.hidden_size).astype(
            np.float32
        )
        * 0.02,
        layers=layers,
        output_norm=np.ones(config.hidden_size, dtype=np.float32),
        output=None,
        vocab_size=config.vocab_size,
        hidden_size=config.hidden_size,
        num_layers=config.num_hidden_layers,
    )


def test_forward_layer_basic():
    """Test basic forward layer functionality."""
    print("Testing basic forward layer functionality...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()
    loop = GenerationLoop(config, weights, gen_config)

    seq_len = 4
    hidden = np.random.randn(seq_len, config.hidden_size).astype(np.float32) * 0.1
    positions = list(range(seq_len))

    output = loop._forward_layer(
        hidden=hidden,
        layer_weights=weights.layers[0],
        layer_idx=0,
        positions=positions,
        is_prefill=True,
    )

    assert (
        output.shape == hidden.shape
    ), f"Output shape {output.shape} != input shape {hidden.shape}"
    assert not np.isnan(output).any(), "Output contains NaN"
    assert not np.isinf(output).any(), "Output contains Inf"

    diff = np.abs(output - hidden).mean()
    assert diff > 1e-6, f"Output too similar to input (mean diff={diff})"

    print(f"  Output shape: {output.shape}")
    print(f"  No NaN/Inf values")
    print(f"  Mean |output - input| = {diff:.6f}")
    print("  PASSED\n")


def test_forward_layer_prefill_vs_decode():
    """Test forward layer in prefill and decode modes."""
    print("Testing prefill vs decode modes...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()
    loop = GenerationLoop(config, weights, gen_config)

    # Prefill: 4 tokens
    seq_len_prefill = 4
    hidden_prefill = (
        np.random.randn(seq_len_prefill, config.hidden_size).astype(np.float32) * 0.1
    )
    positions_prefill = list(range(seq_len_prefill))

    output_prefill = loop._forward_layer(
        hidden=hidden_prefill,
        layer_weights=weights.layers[0],
        layer_idx=0,
        positions=positions_prefill,
        is_prefill=True,
    )

    assert output_prefill.shape[0] == seq_len_prefill

    # Decode: 1 token
    seq_len_decode = 1
    hidden_decode = (
        np.random.randn(seq_len_decode, config.hidden_size).astype(np.float32) * 0.1
    )
    positions_decode = [seq_len_prefill]

    output_decode = loop._forward_layer(
        hidden=hidden_decode,
        layer_weights=weights.layers[0],
        layer_idx=0,
        positions=positions_decode,
        is_prefill=False,
    )

    assert output_decode.shape[0] == seq_len_decode

    print(f"  Prefill: {seq_len_prefill} tokens -> {output_prefill.shape}")
    print(f"  Decode: {seq_len_decode} token -> {output_decode.shape}")
    print("  PASSED\n")


def test_forward_layer_all_layers():
    """Test forward pass through all layers."""
    print("Testing forward pass through all layers...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()
    loop = GenerationLoop(config, weights, gen_config)

    seq_len = 2
    hidden = np.random.randn(seq_len, config.hidden_size).astype(np.float32) * 0.1
    positions = list(range(seq_len))

    for layer_idx in range(config.num_hidden_layers):
        hidden = loop._forward_layer(
            hidden=hidden,
            layer_weights=weights.layers[layer_idx],
            layer_idx=layer_idx,
            positions=positions,
            is_prefill=True,
        )
        assert not np.isnan(hidden).any(), f"Layer {layer_idx} output contains NaN"
        assert hidden.shape == (
            seq_len,
            config.hidden_size,
        ), f"Layer {layer_idx} shape mismatch"

    print(f"  All {config.num_hidden_layers} layers executed successfully")
    print(f"  Final output shape: {hidden.shape}")
    print("  PASSED\n")


def test_helper_functions():
    """Test helper functions: RMSNorm, SiLU, Softmax."""
    print("Testing helper functions...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()
    loop = GenerationLoop(config, weights, gen_config)

    # Test RMSNorm
    hidden = np.random.randn(4, config.hidden_size).astype(np.float32)
    weight = np.ones(config.hidden_size, dtype=np.float32)
    normalized = loop._rms_norm(hidden, weight)
    rms = np.sqrt(np.mean(normalized**2, axis=-1))
    assert np.allclose(rms, 1.0, atol=1e-5), f"RMS not normalized: {rms}"
    print(f"  RMSNorm: RMS = {rms.mean():.6f} (expected: 1.0)")

    # Test SiLU
    x = np.random.randn(4, 8192).astype(np.float32)
    output = loop._silu(x)
    expected = x * (1.0 / (1.0 + np.exp(-x)))
    assert np.allclose(output, expected, rtol=1e-5), "SiLU output mismatch"
    print(f"  SiLU: Formula verified")

    # Test Softmax
    x = np.random.randn(12, 128).astype(np.float32)
    output = loop._softmax(x)
    row_sums = np.sum(output, axis=-1)
    assert np.allclose(row_sums, 1.0, atol=1e-5), "Softmax rows don't sum to 1"
    print(f"  Softmax: Rows sum to 1.0")

    print("  PASSED\n")


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("IRON Forward Layer Test Suite")
    print("=" * 60 + "\n")

    tests = [
        test_helper_functions,
        test_forward_layer_basic,
        test_forward_layer_prefill_vs_decode,
        test_forward_layer_all_layers,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"  FAILED: {test.__name__}")
            print(f"  Error: {e}\n")
            import traceback

            traceback.print_exc()

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("=" * 60)

    if failed == 0:
        print("\n All tests passed! Forward layer implementation is functional.")
    else:
        print(f"\n {failed} test(s) failed.")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
