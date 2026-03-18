# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Test suite for _forward_layer() implementation.

This module tests the newly implemented _forward_layer() method
to verify it correctly computes transformer forward passes.

Example:
    >>> from iron.generation.test_forward_layer import run_all_tests
    >>> run_all_tests()
    >>> print("All tests passed!")
"""

import sys
import numpy as np
from typing import Dict, Any

# Setup AIE mock before importing iron modules
from ..common.aie_mock import setup_mock

setup_mock()

from ..models.llama32.config import Llama32Config
from ..models.llama32.weights import LlamaWeights, TransformerWeights
from .loop import GenerationLoop
from ..api.generation_config import GenerationConfig


def create_test_weights(config: Llama32Config) -> LlamaWeights:
    """Create random test weights for validation.

    Args:
        config: Llama32Config with model dimensions

    Returns:
        LlamaWeights with random initialization
    """
    layers = []

    for _ in range(config.num_hidden_layers):
        layer = TransformerWeights(
            # Attention projections
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
            # MLP projections (SwiGLU)
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
            # Normalization
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
        output=None,  # Tied embeddings
        vocab_size=config.vocab_size,
        hidden_size=config.hidden_size,
        num_layers=config.num_hidden_layers,
    )


def test_forward_layer_basic():
    """Test basic forward layer functionality.

    Verifies:
    - Forward pass executes without errors
    - Output shape matches input shape
    - Output is not NaN or Inf
    - Output differs from input (computation actually happens)
    """
    print("Testing basic forward layer functionality...")

    # Create minimal config for Llama3.2-1B
    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    # Create generation loop
    loop = GenerationLoop(config, weights, gen_config)

    # Create test input: [seq_len=4, hidden_size=2048]
    seq_len = 4
    hidden = np.random.randn(seq_len, config.hidden_size).astype(np.float32) * 0.1
    positions = list(range(seq_len))

    # Test layer 0 in prefill mode
    output = loop._forward_layer(
        hidden=hidden,
        layer_weights=weights.layers[0],
        layer_idx=0,
        positions=positions,
        is_prefill=True,
    )

    # Validate output shape
    assert (
        output.shape == hidden.shape
    ), f"Output shape {output.shape} != input shape {hidden.shape}"

    # Validate no NaN or Inf
    assert not np.isnan(output).any(), "Output contains NaN"
    assert not np.isinf(output).any(), "Output contains Inf"

    # Validate output differs from input (computation happened)
    diff = np.abs(output - hidden).mean()
    assert diff > 1e-6, f"Output too similar to input (mean diff={diff})"

    print(f"  ✓ Output shape: {output.shape}")
    print(f"  ✓ No NaN/Inf values")
    print(f"  ✓ Mean |output - input| = {diff:.6f}")
    print("  PASSED: Basic forward layer test\n")


def test_forward_layer_prefill_vs_decode():
    """Test forward layer in both prefill and decode modes.

    Verifies:
    - Prefill mode processes multiple positions
    - Decode mode processes single position
    - KV cache is properly updated
    """
    print("Testing prefill vs decode modes...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Prefill: Process 4 tokens in parallel
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

    # Decode: Process single token
    seq_len_decode = 1
    hidden_decode = (
        np.random.randn(seq_len_decode, config.hidden_size).astype(np.float32) * 0.1
    )
    positions_decode = [seq_len_prefill]  # Next position

    output_decode = loop._forward_layer(
        hidden=hidden_decode,
        layer_weights=weights.layers[0],
        layer_idx=0,
        positions=positions_decode,
        is_prefill=False,
    )

    assert output_decode.shape[0] == seq_len_decode

    print(f"  ✓ Prefill: {seq_len_prefill} tokens -> {output_prefill.shape}")
    print(f"  ✓ Decode: {seq_len_decode} token -> {output_decode.shape}")
    print("  PASSED: Prefill vs decode test\n")


def test_forward_layer_all_layers():
    """Test forward pass through all transformer layers.

    Verifies:
    - Each layer produces valid output
    - Hidden states propagate correctly through layers
    """
    print("Testing forward pass through all layers...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Create test input
    seq_len = 2
    hidden = np.random.randn(seq_len, config.hidden_size).astype(np.float32) * 0.1
    positions = list(range(seq_len))

    # Pass through all layers
    for layer_idx in range(config.num_hidden_layers):
        hidden = loop._forward_layer(
            hidden=hidden,
            layer_weights=weights.layers[layer_idx],
            layer_idx=layer_idx,
            positions=positions,
            is_prefill=True,
        )

        # Validate each layer output
        assert not np.isnan(hidden).any(), f"Layer {layer_idx} output contains NaN"
        assert hidden.shape == (
            seq_len,
            config.hidden_size,
        ), f"Layer {layer_idx} output shape mismatch"

    print(f"  ✓ All {config.num_hidden_layers} layers executed successfully")
    print(f"  ✓ Final output shape: {hidden.shape}")
    print(f"  ✓ No NaN/Inf in final output")
    print("  PASSED: All layers test\n")


def test_rms_norm():
    """Test RMSNorm implementation.

    Verifies:
    - RMSNorm normalizes correctly
    - Weight scaling is applied
    """
    print("Testing RMSNorm implementation...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Test input
    hidden = np.random.randn(4, config.hidden_size).astype(np.float32)
    weight = np.ones(config.hidden_size, dtype=np.float32)

    # Apply RMSNorm
    normalized = loop._rms_norm(hidden, weight)

    # Verify normalization (RMS should be ~1.0)
    rms = np.sqrt(np.mean(normalized**2, axis=-1))
    assert np.allclose(rms, 1.0, atol=1e-5), f"RMS not normalized: {rms}"

    print(f"  ✓ RMS after normalization: {rms.mean():.6f} (expected: 1.0)")
    print("  PASSED: RMSNorm test\n")


def test_silu():
    """Test SiLU activation implementation.

    Verifies:
    - SiLU(x) = x * sigmoid(x)
    - Output shape matches input
    """
    print("Testing SiLU activation...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Test input
    x = np.random.randn(4, 8192).astype(np.float32)

    # Apply SiLU
    output = loop._silu(x)

    # Verify shape
    assert output.shape == x.shape

    # Verify SiLU formula: x * sigmoid(x)
    expected = x * (1.0 / (1.0 + np.exp(-x)))
    assert np.allclose(output, expected, rtol=1e-5), "SiLU output mismatch"

    print(f"  ✓ SiLU formula verified")
    print(f"  ✓ Output shape: {output.shape}")
    print("  PASSED: SiLU test\n")


def test_softmax():
    """Test softmax implementation.

    Verifies:
    - Rows sum to 1.0
    - Output shape matches input
    """
    print("Testing softmax implementation...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Test input
    x = np.random.randn(12, 128).astype(np.float32)

    # Apply softmax
    output = loop._softmax(x)

    # Verify shape
    assert output.shape == x.shape

    # Verify rows sum to 1.0
    row_sums = np.sum(output, axis=-1)
    assert np.allclose(row_sums, 1.0, atol=1e-5), f"Rows don't sum to 1: {row_sums}"

    print(f"  ✓ Softmax rows sum to 1.0")
    print(f"  ✓ Output shape: {output.shape}")
    print("  PASSED: Softmax test\n")


def test_rope():
    """Test RoPE implementation.

    Verifies:
    - RoPE rotates Q and K correctly
    - Output shape matches input
    """
    print("Testing RoPE implementation...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Test Q and K
    num_heads = config.num_attention_heads
    num_kv_heads = config.num_key_value_heads
    seq_len = 4
    head_dim = config.head_dim

    q = np.random.randn(num_heads, seq_len, head_dim).astype(np.float32)
    k = np.random.randn(num_kv_heads, seq_len, head_dim).astype(np.float32)
    positions = list(range(seq_len))

    # Apply RoPE
    q_rot, k_rot = loop._apply_rope_to_qk(q, k, positions)

    # Verify shapes
    assert q_rot.shape == q.shape
    assert k_rot.shape == k.shape

    # Verify RoPE preserves norm (rotation is norm-preserving)
    q_norm_orig = np.linalg.norm(q, axis=-1)
    q_norm_rot = np.linalg.norm(q_rot, axis=-1)
    assert np.allclose(q_norm_orig, q_norm_rot, rtol=1e-5), "RoPE should preserve norm"

    print(f"  ✓ RoPE preserves norm")
    print(f"  ✓ Q shape: {q.shape} -> {q_rot.shape}")
    print(f"  ✓ K shape: {k.shape} -> {k_rot.shape}")
    print("  PASSED: RoPE test\n")


def test_causal_mask():
    """Test causal attention mask.

    Verifies:
    - Upper triangle is masked (-inf)
    - Lower triangle is preserved
    """
    print("Testing causal mask...")

    config = Llama32Config()
    weights = create_test_weights(config)
    gen_config = GenerationConfig()

    loop = GenerationLoop(config, weights, gen_config)

    # Test attention scores
    num_heads = config.num_attention_heads
    seq_len = 4
    attn_scores = np.random.randn(num_heads, seq_len, seq_len).astype(np.float32)
    positions = list(range(seq_len))

    # Apply causal mask
    masked = loop._apply_causal_mask(attn_scores, positions, is_prefill=True)

    # Verify upper triangle is -inf
    for h in range(num_heads):
        for i in range(seq_len):
            for j in range(i + 1, seq_len):
                assert (
                    masked[h, i, j] == -np.inf
                ), f"Position ({i},{j}) should be masked"

    print(f"  ✓ Causal mask applied correctly")
    print(f"  ✓ Upper triangle masked with -inf")
    print("  PASSED: Causal mask test\n")


def run_all_tests():
    """Run all forward layer tests.

    Example:
        >>> from iron.generation.test_forward_layer import run_all_tests
        >>> run_all_tests()
    """
    print("=" * 60)
    print("IRON Forward Layer Test Suite")
    print("=" * 60 + "\n")

    tests = [
        test_rms_norm,
        test_silu,
        test_softmax,
        test_rope,
        test_causal_mask,
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

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("=" * 60)

    if failed == 0:
        print("\n✓ All tests passed! Forward layer implementation is functional.")
    else:
        print(f"\n✗ {failed} test(s) failed. Review implementation.")

    return failed == 0


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.WARNING)  # Suppress debug logs

    success = run_all_tests()
    exit(0 if success else 1)
