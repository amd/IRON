# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for TokenSampler.

This module contains comprehensive tests for the token sampling
component including temperature, top-k, top-p, and repetition penalty.

COVERAGE TARGET:
- 15+ tests for sampling functionality
- >90% line coverage
- All acceptance criteria verified

TEST CATEGORIES:
1. Initialization tests
2. Temperature tests
3. Top-k filtering tests
4. Top-p filtering tests
5. Repetition penalty tests
6. Integration tests
7. Edge case tests
"""

from __future__ import annotations

import pytest
import numpy as np

from iron.generation.sampling import (
    TokenSampler,
    greedy_sampler,
    creative_sampler,
    balanced_sampler,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def sample_logits() -> np.ndarray:
    """Create sample logits for testing."""
    return np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])


@pytest.fixture
def uniform_logits() -> np.ndarray:
    """Create uniform logits for testing."""
    return np.array([1.0, 1.0, 1.0, 1.0, 1.0])


@pytest.fixture
def sparse_logits() -> np.ndarray:
    """Create sparse logits (one dominant token)."""
    logits = np.zeros(100)
    logits[50] = 10.0  # One dominant token
    return logits


# =============================================================================
# Test Categories
# =============================================================================

# -----------------------------------------------------------------------------
# Category 1: Initialization Tests
# -----------------------------------------------------------------------------


class TestInitialization:
    """Tests for TokenSampler initialization."""

    def test_init_with_defaults(self):
        """Test initialization with default parameters."""
        sampler = TokenSampler()
        assert sampler.temperature == 0.7
        assert sampler.top_k == 50
        assert sampler.top_p == 0.9
        assert sampler.repetition_penalty == 1.0

    def test_init_with_custom_params(self):
        """Test initialization with custom parameters."""
        sampler = TokenSampler(
            temperature=0.5, top_k=40, top_p=0.85, repetition_penalty=1.1
        )
        assert sampler.temperature == 0.5
        assert sampler.top_k == 40
        assert sampler.top_p == 0.85
        assert sampler.repetition_penalty == 1.1

    def test_init_invalid_temperature(self):
        """Test that negative temperature raises error."""
        with pytest.raises(ValueError, match="temperature must be"):
            TokenSampler(temperature=-0.1)

    def test_init_invalid_top_k(self):
        """Test that negative top_k raises error."""
        with pytest.raises(ValueError, match="top_k must be"):
            TokenSampler(top_k=-1)

    def test_init_invalid_top_p(self):
        """Test that top_p outside [0, 1] raises error."""
        with pytest.raises(ValueError, match="top_p must be"):
            TokenSampler(top_p=1.5)

    def test_init_invalid_repetition_penalty(self):
        """Test that negative repetition_penalty raises error."""
        with pytest.raises(ValueError, match="repetition_penalty must be"):
            TokenSampler(repetition_penalty=-0.1)


# -----------------------------------------------------------------------------
# Category 2: Temperature Tests
# -----------------------------------------------------------------------------


class TestTemperature:
    """Tests for temperature scaling."""

    def test_temperature_zero_returns_logits(self, sample_logits):
        """Test that temperature=0 returns logits unchanged."""
        sampler = TokenSampler(temperature=0.0)
        result = sampler.apply_temperature(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_temperature_one_returns_logits(self, sample_logits):
        """Test that temperature=1 returns logits unchanged."""
        sampler = TokenSampler(temperature=1.0)
        result = sampler.apply_temperature(sample_logits)
        np.testing.assert_array_almost_equal(result, sample_logits)

    def test_temperature_scales_logits(self, sample_logits):
        """Test that temperature > 1 scales down logits."""
        sampler = TokenSampler(temperature=2.0)
        result = sampler.apply_temperature(sample_logits)
        expected = sample_logits / 2.0
        np.testing.assert_array_almost_equal(result, expected)

    def test_high_temperature_flattens(self, sample_logits):
        """Test that high temperature flattens distribution."""
        sampler_low = TokenSampler(temperature=0.1)
        sampler_high = TokenSampler(temperature=2.0)

        # Get probabilities
        probs_low = np.softmax(sampler_low.apply_temperature(sample_logits))
        probs_high = np.softmax(sampler_high.apply_temperature(sample_logits))

        # High temp should have lower max probability (flatter)
        assert probs_low.max() > probs_high.max()


# -----------------------------------------------------------------------------
# Category 3: Top-k Filtering Tests
# -----------------------------------------------------------------------------


class TestTopK:
    """Tests for top-k filtering."""

    def test_top_k_no_filtering(self, sample_logits):
        """Test that top_k=0 returns logits unchanged."""
        sampler = TokenSampler(top_k=0)
        result = sampler.apply_top_k(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_top_k_larger_than_vocab(self, sample_logits):
        """Test that top_k > vocab_size returns logits unchanged."""
        sampler = TokenSampler(top_k=100)
        result = sampler.apply_top_k(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_top_k_filters_correctly(self, sample_logits):
        """Test that top-k keeps only top k tokens."""
        sampler = TokenSampler(top_k=3)
        result = sampler.apply_top_k(sample_logits)

        # Top 3 values in sample_logits are 8, 9, 10 (indices 7, 8, 9)
        assert result[7] == 8.0
        assert result[8] == 9.0
        assert result[9] == 10.0

        # Others should be -inf
        assert result[0] == float("-inf")
        assert result[5] == float("-inf")

    def test_top_k_with_k_parameter(self, sample_logits):
        """Test top-k with explicit k parameter."""
        sampler = TokenSampler(top_k=50)
        result = sampler.apply_top_k(sample_logits, k=2)

        # Should keep only top 2
        assert result[8] == 9.0
        assert result[9] == 10.0
        assert result[7] == float("-inf")


# -----------------------------------------------------------------------------
# Category 4: Top-p Filtering Tests
# -----------------------------------------------------------------------------


class TestTopP:
    """Tests for top-p (nucleus) filtering."""

    def test_top_p_zero_returns_logits(self, sample_logits):
        """Test that top_p=0 returns logits unchanged."""
        sampler = TokenSampler(top_p=0.0)
        result = sampler.apply_top_p(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_top_p_one_returns_logits(self, sample_logits):
        """Test that top_p=1 returns logits unchanged."""
        sampler = TokenSampler(top_p=1.0)
        result = sampler.apply_top_p(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_top_p_filters_low_prob_tokens(self, sample_logits):
        """Test that top-p removes low probability tokens."""
        sampler = TokenSampler(top_p=0.5)
        result = sampler.apply_top_p(sample_logits)

        # Some low probability tokens should be filtered
        num_filtered = np.sum(result == float("-inf"))
        assert num_filtered > 0

    def test_top_p_with_uniform_logits(self, uniform_logits):
        """Test top-p with uniform distribution."""
        sampler = TokenSampler(top_p=0.6)
        result = sampler.apply_top_p(uniform_logits)

        # With uniform probs (0.2 each), 3 tokens should be kept (0.6 total)
        num_kept = np.sum(result != float("-inf"))
        assert 2 <= num_kept <= 4  # Allow some variance


# -----------------------------------------------------------------------------
# Category 5: Repetition Penalty Tests
# -----------------------------------------------------------------------------


class TestRepetitionPenalty:
    """Tests for repetition penalty."""

    def test_no_penalty_returns_logits(self, sample_logits):
        """Test that penalty=1.0 returns logits unchanged."""
        sampler = TokenSampler(repetition_penalty=1.0)
        result = sampler.apply_repetition_penalty(sample_logits)
        np.testing.assert_array_equal(result, sample_logits)

    def test_no_input_ids_returns_logits(self, sample_logits):
        """Test that no input_ids returns logits unchanged."""
        sampler = TokenSampler(repetition_penalty=1.5)
        result = sampler.apply_repetition_penalty(sample_logits, input_ids=None)
        np.testing.assert_array_equal(result, sample_logits)

    def test_penalty_reduces_logit(self, sample_logits):
        """Test that penalty reduces logit for repeated tokens."""
        sampler = TokenSampler(repetition_penalty=2.0)
        input_ids = np.array([5])  # Token 5 was generated

        result = sampler.apply_repetition_penalty(sample_logits, input_ids)

        # Token 5's logit should be reduced
        assert result[5] < sample_logits[5]

        # Other logits should be unchanged
        assert result[3] == sample_logits[3]

    def test_penalty_multiple_tokens(self, sample_logits):
        """Test penalty with multiple repeated tokens."""
        sampler = TokenSampler(repetition_penalty=2.0)
        input_ids = np.array([2, 5, 7])

        result = sampler.apply_repetition_penalty(sample_logits, input_ids)

        # These tokens should have reduced logits
        assert result[2] < sample_logits[2]
        assert result[5] < sample_logits[5]
        assert result[7] < sample_logits[7]


# -----------------------------------------------------------------------------
# Category 6: Sample Integration Tests
# -----------------------------------------------------------------------------


class TestSample:
    """Tests for the main sample method."""

    def test_sample_returns_int(self, sample_logits):
        """Test that sample returns an integer."""
        sampler = TokenSampler()
        token = sampler.sample(sample_logits)
        assert isinstance(token, int)

    def test_sample_returns_valid_token_id(self, sample_logits):
        """Test that sample returns valid token ID."""
        sampler = TokenSampler()
        token = sampler.sample(sample_logits)
        assert 0 <= token < len(sample_logits)

    def test_sample_greedy_selects_max(self, sparse_logits):
        """Test that greedy sampling selects max logit."""
        sampler = TokenSampler(temperature=0.0)
        token = sampler.sample(sparse_logits)
        assert token == 50  # Dominant token

    def test_sample_with_repetition_penalty(self, sample_logits):
        """Test sampling with repetition penalty."""
        sampler = TokenSampler(
            temperature=0.0, repetition_penalty=10.0  # Greedy for predictability
        )
        input_ids = np.array([9])  # Highest logit token
        token = sampler.sample(sample_logits, input_ids=input_ids)

        # Should not select token 9 due to high penalty
        assert token != 9

    def test_sample_returns_probs(self, sample_logits):
        """Test that sample can return probabilities."""
        sampler = TokenSampler()
        token, probs = sampler.sample(sample_logits, return_probs=True)
        assert isinstance(token, int)
        assert isinstance(probs, np.ndarray)
        assert len(probs) == len(sample_logits)
        assert np.isclose(np.sum(probs), 1.0)

    def test_sample_empty_logits_raises(self):
        """Test that empty logits raises error."""
        sampler = TokenSampler()
        with pytest.raises(ValueError, match="Logits cannot be empty"):
            sampler.sample(np.array([]))

    def test_sample_all_inf_uses_original(self):
        """Test that all -inf logits uses original."""
        sampler = TokenSampler(top_k=1, top_p=0.0)
        logits = np.array([1.0, 2.0, 3.0])
        # This should not raise, but use original logits
        token = sampler.sample(logits)
        assert 0 <= token < len(logits)


# -----------------------------------------------------------------------------
# Category 7: Batch Sampling Tests
# -----------------------------------------------------------------------------


class TestBatchSampling:
    """Tests for batch sampling."""

    def test_sample_multiple_returns_array(self):
        """Test that sample_multiple returns array."""
        sampler = TokenSampler()
        logits_batch = np.random.randn(4, 100)
        tokens = sampler.sample_multiple(logits_batch)
        assert isinstance(tokens, np.ndarray)
        assert tokens.shape == (4,)

    def test_sample_multiple_with_probs(self):
        """Test sample_multiple with probabilities."""
        sampler = TokenSampler()
        logits_batch = np.random.randn(3, 50)
        tokens, probs = sampler.sample_multiple(logits_batch, return_probs=True)
        assert tokens.shape == (3,)
        assert probs.shape == (3, 50)


# -----------------------------------------------------------------------------
# Category 8: Config Tests
# -----------------------------------------------------------------------------


class TestConfig:
    """Tests for configuration methods."""

    def test_get_config(self):
        """Test getting configuration."""
        sampler = TokenSampler(
            temperature=0.8, top_k=40, top_p=0.92, repetition_penalty=1.1
        )
        config = sampler.get_config()
        assert config["temperature"] == 0.8
        assert config["top_k"] == 40
        assert config["top_p"] == 0.92
        assert config["repetition_penalty"] == 1.1

    def test_set_config(self):
        """Test setting configuration."""
        sampler = TokenSampler()
        sampler.set_config({"temperature": 0.5, "top_k": 30})
        assert sampler.temperature == 0.5
        assert sampler.top_k == 30

    def test_set_config_invalid(self):
        """Test that invalid config raises error."""
        sampler = TokenSampler()
        with pytest.raises(ValueError):
            sampler.set_config({"temperature": -1.0})


# -----------------------------------------------------------------------------
# Category 9: Convenience Function Tests
# -----------------------------------------------------------------------------


class TestConvenienceFunctions:
    """Tests for convenience functions."""

    def test_greedy_sampler(self):
        """Test greedy_sampler function."""
        sampler = greedy_sampler()
        assert sampler.temperature == 0.0

    def test_creative_sampler(self):
        """Test creative_sampler function."""
        sampler = creative_sampler(temperature=1.2, top_p=0.95)
        assert sampler.temperature == 1.2
        assert sampler.top_p == 0.95
        assert sampler.top_k == 0  # No top-k limit

    def test_balanced_sampler(self):
        """Test balanced_sampler function."""
        sampler = balanced_sampler(temperature=0.7, top_k=50, top_p=0.9)
        assert sampler.temperature == 0.7
        assert sampler.top_k == 50
        assert sampler.top_p == 0.9


# -----------------------------------------------------------------------------
# Category 10: Edge Case Tests
# -----------------------------------------------------------------------------


class TestEdgeCases:
    """Tests for edge cases."""

    def test_repr(self):
        """Test string representation."""
        sampler = TokenSampler(temperature=0.5, top_k=40)
        repr_str = repr(sampler)
        assert "TokenSampler" in repr_str
        assert "0.5" in repr_str
        assert "40" in repr_str

    def test_sample_deterministic_with_seed(self, sample_logits):
        """Test that sampling is deterministic with fixed seed."""
        np.random.seed(42)
        sampler1 = TokenSampler(temperature=1.0)
        token1 = sampler1.sample(sample_logits)

        np.random.seed(42)
        sampler2 = TokenSampler(temperature=1.0)
        token2 = sampler2.sample(sample_logits)

        assert token1 == token2

    def test_top_k_with_ties(self):
        """Test top-k filtering with tied logits."""
        sampler = TokenSampler(top_k=3)
        logits = np.array([5.0, 5.0, 5.0, 5.0, 5.0])
        result = sampler.apply_top_k(logits)
        # Should keep exactly 3 tokens
        num_kept = np.sum(result != float("-inf"))
        assert num_kept == 3


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
