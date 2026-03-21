# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for GenerationLoop.

This module contains comprehensive tests for the generation loop
component including prefill, decode, and sampling operations.

COVERAGE TARGET:
- 20+ tests for generation loop functionality
- >90% line coverage
- All acceptance criteria verified

TEST CATEGORIES:
1. Initialization tests
2. Prefill phase tests
3. Decode phase tests
4. Sampling tests
5. Integration tests
6. Edge case tests
"""

from __future__ import annotations

import pytest
import numpy as np
from typing import List, Any

from iron.generation.loop import GenerationLoop, GenerationResult
from iron.generation.sampling import TokenSampler
from iron.models.llama32.config import Llama32Config
from iron.models.llama32.weights import LlamaWeights, TransformerWeights
from iron.api.generation_config import GenerationConfig

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def sample_config() -> Llama32Config:
    """Create a small test configuration."""
    return Llama32Config(
        vocab_size=1000,
        hidden_size=128,
        intermediate_size=256,
        num_hidden_layers=2,
        num_attention_heads=4,
        num_key_value_heads=2,
        head_dim=32,
        max_position_embeddings=512,
        rms_norm_eps=1e-5,
    )


@pytest.fixture
def sample_weights(sample_config: Llama32Config) -> LlamaWeights:
    """Create random weights for testing."""
    layers = []
    for _ in range(sample_config.num_hidden_layers):
        layer = TransformerWeights(
            wq=np.random.randn(
                sample_config.hidden_size,
                sample_config.num_attention_heads * sample_config.head_dim,
            ).astype(np.float32),
            wk=np.random.randn(
                sample_config.hidden_size,
                sample_config.num_key_value_heads * sample_config.head_dim,
            ).astype(np.float32),
            wv=np.random.randn(
                sample_config.hidden_size,
                sample_config.num_key_value_heads * sample_config.head_dim,
            ).astype(np.float32),
            wo=np.random.randn(
                sample_config.num_attention_heads * sample_config.head_dim,
                sample_config.hidden_size,
            ).astype(np.float32),
            w1=np.random.randn(
                sample_config.hidden_size, sample_config.intermediate_size
            ).astype(np.float32),
            w2=np.random.randn(
                sample_config.intermediate_size, sample_config.hidden_size
            ).astype(np.float32),
            w3=np.random.randn(
                sample_config.hidden_size, sample_config.intermediate_size
            ).astype(np.float32),
            attn_norm=np.random.randn(sample_config.hidden_size).astype(np.float32),
            ffn_norm=np.random.randn(sample_config.hidden_size).astype(np.float32),
        )
        layers.append(layer)

    return LlamaWeights(
        token_embd=np.random.randn(
            sample_config.vocab_size, sample_config.hidden_size
        ).astype(np.float32),
        layers=layers,
        output_norm=np.random.randn(sample_config.hidden_size).astype(np.float32),
        output=None,  # Tied embeddings
        vocab_size=sample_config.vocab_size,
        hidden_size=sample_config.hidden_size,
        num_layers=sample_config.num_hidden_layers,
    )


@pytest.fixture
def gen_config() -> GenerationConfig:
    """Create default generation config."""
    return GenerationConfig(temperature=0.7, top_k=50, top_p=0.9, max_new_tokens=100)


@pytest.fixture
def generation_loop(
    sample_config: Llama32Config,
    sample_weights: LlamaWeights,
    gen_config: GenerationConfig,
) -> GenerationLoop:
    """Create a GenerationLoop for testing."""
    return GenerationLoop(sample_config, sample_weights, gen_config)


@pytest.fixture
def sample_prompt() -> List[int]:
    """Create a sample prompt."""
    return [10, 20, 30, 40, 50]


# =============================================================================
# Test Categories
# =============================================================================

# -----------------------------------------------------------------------------
# Category 1: Initialization Tests
# -----------------------------------------------------------------------------


class TestInitialization:
    """Tests for GenerationLoop initialization."""

    def test_init_with_defaults(self, sample_config, sample_weights):
        """Test initialization with default generation config."""
        loop = GenerationLoop(sample_config, sample_weights)
        assert loop.config is sample_config
        assert loop.weights is sample_weights
        assert loop.generation_config is not None
        assert isinstance(loop.sampler, TokenSampler)

    def test_init_with_custom_config(self, sample_config, sample_weights, gen_config):
        """Test initialization with custom generation config."""
        loop = GenerationLoop(sample_config, sample_weights, gen_config)
        assert loop.generation_config is gen_config
        assert loop.generation_config.temperature == 0.7

    def test_init_creates_sampler(self, sample_config, sample_weights):
        """Test that initialization creates a TokenSampler."""
        loop = GenerationLoop(sample_config, sample_weights)
        assert isinstance(loop.sampler, TokenSampler)
        assert loop.sampler.temperature == 0.7  # Default

    def test_init_resets_state(self, sample_config, sample_weights):
        """Test that initialization resets internal state."""
        loop = GenerationLoop(sample_config, sample_weights)
        assert loop._kv_cache is None
        assert loop._current_position == 0


# -----------------------------------------------------------------------------
# Category 2: Prefill Phase Tests
# -----------------------------------------------------------------------------


class TestPrefill:
    """Tests for the prefill phase."""

    def test_prefill_with_valid_prompt(self, generation_loop, sample_prompt):
        """Test prefill with a valid prompt."""
        logits = generation_loop.prefill(sample_prompt)
        assert isinstance(logits, np.ndarray)
        assert logits.shape == (generation_loop.config.hidden_size,)

    def test_prefill_with_empty_prompt_raises(self, generation_loop):
        """Test that prefill raises on empty prompt."""
        with pytest.raises(ValueError, match="Prompt cannot be empty"):
            generation_loop.prefill([])

    def test_prefill_with_single_token(self, generation_loop):
        """Test prefill with a single token prompt."""
        logits = generation_loop.prefill([42])
        assert isinstance(logits, np.ndarray)

    def test_prefill_updates_position(self, generation_loop, sample_prompt):
        """Test that prefill updates current position."""
        assert generation_loop._current_position == 0
        generation_loop.prefill(sample_prompt)
        assert generation_loop._current_position == len(sample_prompt)

    def test_prefill_with_long_prompt(self, generation_loop):
        """Test prefill with a longer prompt."""
        long_prompt = list(range(100))
        logits = generation_loop.prefill(long_prompt)
        assert isinstance(logits, np.ndarray)
        assert generation_loop._current_position == 100


# -----------------------------------------------------------------------------
# Category 3: Decode Phase Tests
# -----------------------------------------------------------------------------


class TestDecode:
    """Tests for the decode phase."""

    def test_decode_requires_prefill(self, generation_loop):
        """Test that decode requires prefill first."""
        with pytest.raises(RuntimeError, match="Must call prefill"):
            generation_loop.decode(42)

    def test_decode_after_prefill(self, generation_loop, sample_prompt):
        """Test decode after prefill."""
        generation_loop.prefill(sample_prompt)
        logits = generation_loop.decode(99)
        assert isinstance(logits, np.ndarray)

    def test_decode_updates_position(self, generation_loop, sample_prompt):
        """Test that decode updates position."""
        generation_loop.prefill(sample_prompt)
        initial_pos = generation_loop._current_position
        generation_loop.decode(99)
        assert generation_loop._current_position == initial_pos + 1

    def test_decode_multiple_tokens(self, generation_loop, sample_prompt):
        """Test multiple decode calls."""
        generation_loop.prefill(sample_prompt)
        for i in range(5):
            logits = generation_loop.decode(50 + i)
            assert isinstance(logits, np.ndarray)


# -----------------------------------------------------------------------------
# Category 4: Sampling Tests
# -----------------------------------------------------------------------------


class TestSampling:
    """Tests for the sampling functionality."""

    def test_sample_returns_valid_token(self, generation_loop, sample_prompt):
        """Test that sample returns a valid token ID."""
        logits = generation_loop.prefill(sample_prompt)
        token_id = generation_loop.sample(logits)
        assert isinstance(token_id, int)
        assert token_id >= 0

    def test_sample_uses_sampler(self, generation_loop, sample_prompt):
        """Test that sample uses the TokenSampler."""
        logits = generation_loop.prefill(sample_prompt)
        # Mock the sampler to verify it's called
        original_sample = generation_loop.sampler.sample
        called = []

        def mock_sample(l):
            called.append(True)
            return original_sample(l)

        generation_loop.sampler.sample = mock_sample
        generation_loop.sample(logits)
        assert len(called) == 1


# -----------------------------------------------------------------------------
# Category 5: Generation Integration Tests
# -----------------------------------------------------------------------------


class TestGeneration:
    """Tests for the full generation loop."""

    def test_generate_yields_tokens(self, generation_loop, sample_prompt):
        """Test that generate yields tokens."""
        results = list(generation_loop.generate(sample_prompt, max_tokens=5))
        assert len(results) > 0
        assert all(isinstance(r, GenerationResult) for r in results)

    def test_generate_empty_prompt_raises(self, generation_loop):
        """Test that generate raises on empty prompt."""
        with pytest.raises(ValueError, match="Prompt cannot be empty"):
            list(generation_loop.generate([]))

    def test_generate_respects_max_tokens(self, generation_loop, sample_prompt):
        """Test that generate respects max_tokens limit."""
        results = list(generation_loop.generate(sample_prompt, max_tokens=3))
        assert len(results) <= 3

    def test_generate_returns_generation_result(self, generation_loop, sample_prompt):
        """Test that generate returns proper GenerationResult."""
        results = list(generation_loop.generate(sample_prompt, max_tokens=1))
        result = results[0]
        assert isinstance(result, GenerationResult)
        assert hasattr(result, "token_id")
        assert hasattr(result, "position")

    def test_generate_increments_position(self, generation_loop, sample_prompt):
        """Test that generate increments position for each token."""
        results = list(generation_loop.generate(sample_prompt, max_tokens=5))
        for i, result in enumerate(results):
            assert result.position == i

    def test_generate_with_stop_config(
        self, sample_config, sample_weights, sample_prompt
    ):
        """Test generation with EOS token in config."""
        config = GenerationConfig(eos_tokens=[999], max_new_tokens=100)
        loop = GenerationLoop(sample_config, sample_weights, config)

        # This test verifies the stop condition integration
        # Note: Actual EOS detection depends on sampling
        results = list(loop.generate(sample_prompt, max_tokens=10))
        assert len(results) > 0


# -----------------------------------------------------------------------------
# Category 6: Edge Case Tests
# -----------------------------------------------------------------------------


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_reset_clears_cache(self, generation_loop, sample_prompt):
        """Test that reset clears the KV cache."""
        generation_loop.prefill(sample_prompt)
        assert generation_loop._kv_cache is not None
        generation_loop.reset()
        assert generation_loop._kv_cache is None

    def test_reset_increments_sequence_id(self, generation_loop):
        """Test that reset increments sequence ID."""
        initial_id = generation_loop._sequence_id
        generation_loop.reset()
        assert generation_loop._sequence_id == initial_id + 1

    def test_get_kv_cache_stats(self, generation_loop, sample_prompt):
        """Test getting KV cache statistics."""
        generation_loop.prefill(sample_prompt)
        stats = generation_loop.get_kv_cache_stats()
        assert isinstance(stats, dict)
        assert "current_position" in stats
        assert "sequence_id" in stats

    def test_generate_batch(self, generation_loop):
        """Test batch generation."""
        prompts = [[1, 2, 3], [4, 5, 6]]
        results = list(generation_loop.generate_batch(prompts, max_tokens=2))
        # Each prompt generates at least 1 token
        assert len(results) >= 2

    def test_rms_norm(self, generation_loop):
        """Test RMSNorm implementation."""
        hidden = np.random.randn(2, 4, 32).astype(np.float32)
        weight = np.random.randn(32).astype(np.float32)
        output = generation_loop._rms_norm(hidden, weight)
        assert output.shape == hidden.shape

    def test_output_projection(self, generation_loop):
        """Test output projection."""
        hidden = np.random.randn(generation_loop.config.hidden_size).astype(np.float32)
        logits = generation_loop._output_projection(hidden)
        # With tied embeddings, shape is vocab_size


# -----------------------------------------------------------------------------
# Category 7: GenerationResult Tests
# -----------------------------------------------------------------------------


class TestGenerationResult:
    """Tests for GenerationResult dataclass."""

    def test_result_creation(self):
        """Test creating a GenerationResult."""
        result = GenerationResult(
            token_id=42, token_text="hello", logit_prob=-0.5, is_eos=False, position=0
        )
        assert result.token_id == 42
        assert result.token_text == "hello"
        assert result.is_eos is False

    def test_result_with_eos(self):
        """Test GenerationResult with EOS."""
        result = GenerationResult(token_id=128001, is_eos=True, stop_reason="eos_token")
        assert result.is_eos is True
        assert result.stop_reason == "eos_token"

    def test_result_str(self):
        """Test GenerationResult string representation."""
        result = GenerationResult(token_id=42)
        result_str = str(result)
        assert "GenerationResult" in result_str
        assert "42" in result_str


# -----------------------------------------------------------------------------
# Category 8: TokenSampler Integration Tests
# -----------------------------------------------------------------------------


class TestTokenSamplerIntegration:
    """Tests for TokenSampler integration."""

    def test_sampler_temperature(self, sample_config, sample_weights):
        """Test sampler with different temperatures."""
        for temp in [0.0, 0.5, 1.0]:
            config = GenerationConfig(temperature=temp)
            loop = GenerationLoop(sample_config, sample_weights, config)
            assert loop.sampler.temperature == temp

    def test_sampler_top_k(self, sample_config, sample_weights):
        """Test sampler with different top_k values."""
        for k in [10, 50, 100]:
            config = GenerationConfig(top_k=k)
            loop = GenerationLoop(sample_config, sample_weights, config)
            assert loop.sampler.top_k == k

    def test_sampler_top_p(self, sample_config, sample_weights):
        """Test sampler with different top_p values."""
        for p in [0.5, 0.9, 0.95]:
            config = GenerationConfig(top_p=p)
            loop = GenerationLoop(sample_config, sample_weights, config)
            assert loop.sampler.top_p == p


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
