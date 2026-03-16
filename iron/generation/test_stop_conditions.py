# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for StopConditionChecker.

This module contains comprehensive tests for the stop condition
detection component including EOS detection, max tokens, and stop strings.

COVERAGE TARGET:
- 15+ tests for stop condition functionality
- >90% line coverage
- All acceptance criteria verified

TEST CATEGORIES:
1. Initialization tests
2. EOS detection tests
3. Max tokens tests
4. Stop string tests
5. Combined check tests
6. Batch tests
7. Configuration tests
8. Edge case tests
"""

from __future__ import annotations

import pytest

from iron.generation.stop_conditions import (
    StopConditionChecker,
    StopResult,
    create_llama3_stop_checker,
    create_permissive_checker,
    create_strict_checker
)
from iron.api.generation_config import GenerationConfig


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def default_config() -> GenerationConfig:
    """Create default generation config."""
    return GenerationConfig(
        eos_tokens=[128001, 128009],
        max_new_tokens=512,
        stop_strings=["</answer>", "Q:"]
    )


@pytest.fixture
def stop_checker(default_config: GenerationConfig) -> StopConditionChecker:
    """Create a StopConditionChecker for testing."""
    return StopConditionChecker(default_config)


# =============================================================================
# Test Categories
# =============================================================================

# -----------------------------------------------------------------------------
# Category 1: Initialization Tests
# -----------------------------------------------------------------------------

class TestInitialization:
    """Tests for StopConditionChecker initialization."""

    def test_init_with_config(self, default_config):
        """Test initialization with GenerationConfig."""
        checker = StopConditionChecker(default_config)
        assert 128001 in checker.eos_tokens
        assert 128009 in checker.eos_tokens
        assert checker.max_tokens == 512

    def test_init_with_dict(self):
        """Test initialization with dictionary."""
        config = {
            'eos_tokens': [1, 2, 3],
            'max_new_tokens': 100,
            'stop_strings': ['stop']
        }
        checker = StopConditionChecker(config)
        assert checker.eos_tokens == {1, 2, 3}
        assert checker.max_tokens == 100
        assert checker.stop_strings == ['stop']

    def test_init_with_defaults(self):
        """Test initialization with minimal config."""
        class MinimalConfig:
            pass

        checker = StopConditionChecker(MinimalConfig())
        assert checker.eos_tokens == {128001}  # Default
        assert checker.max_tokens == 2048  # Default
        assert checker.stop_strings == []  # Default


# -----------------------------------------------------------------------------
# Category 2: EOS Detection Tests
# -----------------------------------------------------------------------------

class TestEOSDetection:
    """Tests for EOS token detection."""

    def test_eos_detected(self, stop_checker):
        """Test that EOS token is detected."""
        result = stop_checker.check_eos(128001)
        assert result.should_stop is True
        assert result.reason == "eos_token"
        assert result.token_id == 128001

    def test_eos_second_token(self, stop_checker):
        """Test that second EOS token is detected."""
        result = stop_checker.check_eos(128009)
        assert result.should_stop is True
        assert result.reason == "eos_token"

    def test_non_eos_not_detected(self, stop_checker):
        """Test that non-EOS token is not detected as EOS."""
        result = stop_checker.check_eos(5000)
        assert result.should_stop is False
        assert result.reason == ""

    def test_eos_boolean_true(self, stop_checker):
        """Test that EOS result is truthy."""
        result = stop_checker.check_eos(128001)
        assert bool(result) is True

    def test_non_eos_boolean_false(self, stop_checker):
        """Test that non-EOS result is falsy."""
        result = stop_checker.check_eos(5000)
        assert bool(result) is False


# -----------------------------------------------------------------------------
# Category 3: Max Tokens Tests
# -----------------------------------------------------------------------------

class TestMaxTokens:
    """Tests for maximum token limit."""

    def test_max_tokens_reached(self, stop_checker):
        """Test that max tokens is detected when reached."""
        result = stop_checker.check_max_tokens(512)
        assert result.should_stop is True
        assert result.reason == "max_tokens"

    def test_max_tokens_not_reached(self, stop_checker):
        """Test that generation continues before max."""
        result = stop_checker.check_max_tokens(100)
        assert result.should_stop is False

    def test_max_tokens_exceeded(self, stop_checker):
        """Test that max tokens is detected when exceeded."""
        result = stop_checker.check_max_tokens(600)
        assert result.should_stop is True
        assert result.reason == "max_tokens"

    def test_max_tokens_boundary(self):
        """Test max tokens at exact boundary."""
        config = GenerationConfig(max_new_tokens=10)
        checker = StopConditionChecker(config)

        # At exactly 10, should stop
        result = checker.check_max_tokens(10)
        assert result.should_stop is True

        # At 9, should continue
        result = checker.check_max_tokens(9)
        assert result.should_stop is False


# -----------------------------------------------------------------------------
# Category 4: Stop String Tests
# -----------------------------------------------------------------------------

class TestStopStrings:
    """Tests for stop string detection."""

    def test_stop_string_detected(self, stop_checker):
        """Test that stop string is detected."""
        result = stop_checker.check_stop_string("The answer is </answer>")
        assert result.should_stop is True
        assert result.reason == "stop_string"
        assert result.stop_string == "</answer>"

    def test_stop_string_second_pattern(self, stop_checker):
        """Test that second stop string is detected."""
        result = stop_checker.check_stop_string("Question: Q: New question")
        assert result.should_stop is True
        assert result.reason == "stop_string"
        assert result.stop_string == "Q:"

    def test_no_stop_string(self, stop_checker):
        """Test that text without stop strings continues."""
        result = stop_checker.check_stop_string("Hello, world!")
        assert result.should_stop is False

    def test_empty_stop_strings(self):
        """Test checker with no stop strings."""
        config = GenerationConfig(stop_strings=None)
        checker = StopConditionChecker(config)

        result = checker.check_stop_string("Any text")
        assert result.should_stop is False

    def test_case_sensitive(self, stop_checker):
        """Test that stop string detection is case-sensitive."""
        # Lowercase version should not match
        result = stop_checker.check_stop_string("The answer is </ANSWER>")
        assert result.should_stop is False


# -----------------------------------------------------------------------------
# Category 5: Combined Check Tests
# -----------------------------------------------------------------------------

class TestCombinedChecks:
    """Tests for check_all method."""

    def test_check_all_eos_priority(self, stop_checker):
        """Test that EOS has highest priority."""
        result = stop_checker.check_all(
            token_id=128001,
            generated_text="</answer>",
            num_generated=512
        )
        assert result.should_stop is True
        assert result.reason == "eos_token"

    def test_check_all_max_tokens_priority(self, stop_checker):
        """Test that max tokens has second priority."""
        result = stop_checker.check_all(
            token_id=5000,
            generated_text="</answer>",
            num_generated=512
        )
        assert result.should_stop is True
        assert result.reason == "max_tokens"

    def test_check_all_stop_string(self, stop_checker):
        """Test stop string detection in check_all."""
        result = stop_checker.check_all(
            token_id=5000,
            generated_text="The answer is </answer>",
            num_generated=100
        )
        assert result.should_stop is True
        assert result.reason == "stop_string"

    def test_check_all_continue(self, stop_checker):
        """Test that check_all returns False when no condition met."""
        result = stop_checker.check_all(
            token_id=5000,
            generated_text="Hello, world!",
            num_generated=10
        )
        assert result.should_stop is False

    def test_check_all_empty_text(self, stop_checker):
        """Test check_all with empty text."""
        result = stop_checker.check_all(
            token_id=5000,
            generated_text="",
            num_generated=10
        )
        assert result.should_stop is False


# -----------------------------------------------------------------------------
# Category 6: Batch Tests
# -----------------------------------------------------------------------------

class TestBatchChecks:
    """Tests for batch stop condition checking."""

    def test_check_batch_returns_list(self, stop_checker):
        """Test that check_batch returns a list."""
        results = stop_checker.check_batch(
            token_ids=[128001, 5000, 5001],
            generated_texts=["text1", "text2", "text3"],
            num_generated=[10, 20, 30]
        )
        assert isinstance(results, list)
        assert len(results) == 3

    def test_check_batch_mixed_results(self, stop_checker):
        """Test batch with mixed results."""
        results = stop_checker.check_batch(
            token_ids=[128001, 5000, 5001],
            generated_texts=["text", "text", "text"],
            num_generated=[10, 10, 10]
        )
        assert results[0].should_stop is True  # EOS
        assert results[1].should_stop is False
        assert results[2].should_stop is False


# -----------------------------------------------------------------------------
# Category 7: Configuration Tests
# -----------------------------------------------------------------------------

class TestConfiguration:
    """Tests for configuration methods."""

    def test_set_stop_strings(self, stop_checker):
        """Test updating stop strings."""
        stop_checker.set_stop_strings(["new_stop"])
        assert "new_stop" in stop_checker.stop_strings
        assert "</answer>" not in stop_checker.stop_strings

    def test_set_max_tokens(self, stop_checker):
        """Test updating max tokens."""
        stop_checker.set_max_tokens(1024)
        assert stop_checker.max_tokens == 1024

    def test_set_max_tokens_invalid_raises(self, stop_checker):
        """Test that invalid max_tokens raises."""
        with pytest.raises(ValueError, match="max_tokens must be"):
            stop_checker.set_max_tokens(0)

    def test_set_eos_tokens(self, stop_checker):
        """Test updating EOS tokens."""
        stop_checker.set_eos_tokens([999, 1000])
        assert stop_checker.eos_tokens == {999, 1000}
        assert 128001 not in stop_checker.eos_tokens

    def test_get_config(self, stop_checker):
        """Test getting configuration."""
        config = stop_checker.get_config()
        assert isinstance(config, dict)
        assert 'eos_tokens' in config
        assert 'max_tokens' in config
        assert 'stop_strings' in config


# -----------------------------------------------------------------------------
# Category 8: StopResult Tests
# -----------------------------------------------------------------------------

class TestStopResult:
    """Tests for StopResult dataclass."""

    def test_result_creation(self):
        """Test creating a StopResult."""
        result = StopResult(
            should_stop=True,
            reason="eos_token",
            token_id=128001
        )
        assert result.should_stop is True
        assert result.reason == "eos_token"

    def test_result_default_values(self):
        """Test default values."""
        result = StopResult()
        assert result.should_stop is False
        assert result.reason == ""
        assert result.stop_string is None

    def test_result_boolean_true(self):
        """Test boolean conversion when stopping."""
        result = StopResult(should_stop=True, reason="test")
        assert bool(result) is True

    def test_result_boolean_false(self):
        """Test boolean conversion when continuing."""
        result = StopResult(should_stop=False)
        assert bool(result) is False

    def test_result_str_stop(self):
        """Test string representation when stopping."""
        result = StopResult(should_stop=True, reason="eos_token")
        result_str = str(result)
        assert "StopResult" in result_str
        assert "stop" in result_str.lower()

    def test_result_str_continue(self):
        """Test string representation when continuing."""
        result = StopResult(should_stop=False)
        result_str = str(result)
        assert "StopResult" in result_str
        assert "continue" in result_str.lower()


# -----------------------------------------------------------------------------
# Category 9: Convenience Function Tests
# -----------------------------------------------------------------------------

class TestConvenienceFunctions:
    """Tests for convenience functions."""

    def test_create_llama3_stop_checker(self):
        """Test create_llama3_stop_checker function."""
        checker = create_llama3_stop_checker(max_tokens=1024)
        assert 128001 in checker.eos_tokens
        assert 128009 in checker.eos_tokens
        assert checker.max_tokens == 1024

    def test_create_permissive_checker(self):
        """Test create_permissive_checker function."""
        checker = create_permissive_checker(max_tokens=4096)
        assert checker.max_tokens == 4096
        assert len(checker.stop_strings) == 0  # No stop strings

    def test_create_strict_checker(self):
        """Test create_strict_checker function."""
        checker = create_strict_checker(max_tokens=256)
        assert checker.max_tokens == 256
        assert len(checker.stop_strings) > 0  # Has default stop strings

    def test_create_strict_checker_custom_strings(self):
        """Test create_strict_checker with custom strings."""
        checker = create_strict_checker(
            max_tokens=256,
            stop_strings=["custom1", "custom2"]
        )
        assert "custom1" in checker.stop_strings
        assert "custom2" in checker.stop_strings


# -----------------------------------------------------------------------------
# Category 10: Edge Case Tests
# -----------------------------------------------------------------------------

class TestEdgeCases:
    """Tests for edge cases."""

    def test_repr(self, stop_checker):
        """Test string representation."""
        repr_str = repr(stop_checker)
        assert "StopConditionChecker" in repr_str
        assert "eos_tokens=" in repr_str or "eos_tokens" in repr_str

    def test_eos_token_zero(self):
        """Test EOS detection for token 0."""
        config = GenerationConfig(eos_tokens=[0])
        checker = StopConditionChecker(config)

        result = checker.check_eos(0)
        assert result.should_stop is True

    def test_stop_string_at_start(self, stop_checker):
        """Test stop string at start of text."""
        result = stop_checker.check_stop_string("</answer> is here")
        assert result.should_stop is True
        assert result.stop_string == "</answer>"

    def test_stop_string_at_end(self, stop_checker):
        """Test stop string at end of text."""
        result = stop_checker.check_stop_string("The answer is </answer>")
        assert result.should_stop is True

    def test_stop_string_overlap(self):
        """Test stop string with potential overlap."""
        config = GenerationConfig(stop_strings=["aa", "aaa"])
        checker = StopConditionChecker(config)

        result = checker.check_stop_string("aaaa")
        assert result.should_stop is True

    def test_multiple_eos_tokens(self):
        """Test with multiple EOS tokens configured."""
        config = GenerationConfig(eos_tokens=[1, 2, 3, 4, 5])
        checker = StopConditionChecker(config)

        for token_id in [1, 2, 3, 4, 5]:
            result = checker.check_eos(token_id)
            assert result.should_stop is True

        # Non-EOS should not trigger
        result = checker.check_eos(100)
        assert result.should_stop is False


# -----------------------------------------------------------------------------
# Category 11: Integration Tests
# -----------------------------------------------------------------------------

class TestIntegration:
    """Integration tests for stop conditions."""

    def test_full_generation_scenario(self):
        """Simulate a full generation scenario."""
        config = GenerationConfig(
            eos_tokens=[128001],
            max_new_tokens=100,
            stop_strings=["END"]
        )
        checker = StopConditionChecker(config)

        # Simulate generation loop
        for i in range(50):
            result = checker.check_all(
                token_id=5000 + i,
                generated_text=f"Generated text {i}",
                num_generated=i + 1
            )
            assert result.should_stop is False

        # Now simulate EOS
        result = checker.check_all(
            token_id=128001,
            generated_text="Generated text END",
            num_generated=51
        )
        assert result.should_stop is True
        assert result.reason == "eos_token"

    def test_max_tokens_scenario(self):
        """Simulate hitting max tokens."""
        config = GenerationConfig(max_new_tokens=10)
        checker = StopConditionChecker(config)

        # Generate up to max
        for i in range(9):
            result = checker.check_all(
                token_id=1000 + i,
                generated_text="text",
                num_generated=i + 1
            )
            assert result.should_stop is False

        # Hit max
        result = checker.check_all(
            token_id=1009,
            generated_text="text",
            num_generated=10
        )
        assert result.should_stop is True
        assert result.reason == "max_tokens"


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
