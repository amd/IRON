# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for GenerationConfig class.

This test suite validates the GenerationConfig implementation:
- Construction with defaults and custom values
- Parameter validation
- EOS token detection
- Stop condition checking
- JSON serialization/deserialization
- Preset configurations

@note Uses pytest framework
"""

import pytest
import json
from iron.api.generation_config import (
    GenerationConfig,
    LLAMA3_CONFIG,
    LLAMA3_GREEDY_CONFIG,
    LLAMA3_HIGH_CREATIVE_CONFIG,
)


class TestGenerationConfigConstruction:
    """Tests for GenerationConfig construction."""

    def test_default_construction(self):
        """Test construction with default values."""
        config = GenerationConfig()

        assert config.temperature == 0.7
        assert config.top_p == 0.9
        assert config.top_k == 50
        assert config.max_new_tokens == 2048
        assert config.model_type == "llama3"
        assert config.eos_tokens == [128001, 128009]

    def test_custom_construction(self):
        """Test construction with custom values."""
        config = GenerationConfig(
            temperature=0.5,
            top_p=0.8,
            top_k=40,
            max_new_tokens=512,
        )

        assert config.temperature == 0.5
        assert config.top_p == 0.8
        assert config.top_k == 40
        assert config.max_new_tokens == 512

    def test_custom_eos_tokens(self):
        """Test construction with custom EOS tokens."""
        config = GenerationConfig(eos_tokens=[1, 2, 3])

        assert config.eos_tokens == [1, 2, 3]

    def test_model_type_affects_eos_tokens(self):
        """Test that model_type sets appropriate EOS tokens."""
        # Llama3 should have both EOS tokens
        config_llama3 = GenerationConfig(model_type="llama3")
        assert config_llama3.eos_tokens == [128001, 128009]

        # Unknown model type should have default EOS
        config_other = GenerationConfig(model_type="unknown")
        assert config_other.eos_tokens == [128001]


class TestGenerationConfigValidation:
    """Tests for parameter validation."""

    def test_negative_temperature(self):
        """Test that negative temperature raises ValueError."""
        with pytest.raises(ValueError, match="temperature must be >= 0"):
            GenerationConfig(temperature=-0.1)

    def test_top_p_below_zero(self):
        """Test that top_p < 0 raises ValueError."""
        with pytest.raises(ValueError, match="top_p must be in \\[0, 1\\]"):
            GenerationConfig(top_p=-0.1)

    def test_top_p_above_one(self):
        """Test that top_p > 1 raises ValueError."""
        with pytest.raises(ValueError, match="top_p must be in \\[0, 1\\]"):
            GenerationConfig(top_p=1.1)

    def test_top_k_below_one(self):
        """Test that top_k < 1 raises ValueError."""
        with pytest.raises(ValueError, match="top_k must be >= 1"):
            GenerationConfig(top_k=0)

    def test_negative_repetition_penalty(self):
        """Test that negative repetition_penalty raises ValueError."""
        with pytest.raises(ValueError, match="repetition_penalty must be >= 0"):
            GenerationConfig(repetition_penalty=-0.1)

    def test_zero_max_new_tokens(self):
        """Test that max_new_tokens < 1 raises ValueError."""
        with pytest.raises(ValueError, match="max_new_tokens must be >= 1"):
            GenerationConfig(max_new_tokens=0)

    def test_valid_boundary_values(self):
        """Test valid boundary values."""
        # Should not raise
        config = GenerationConfig(
            temperature=0.0,  # Greedy
            top_p=0.0,
            top_k=1,
            repetition_penalty=0.0,
            max_new_tokens=1,
        )
        assert config.temperature == 0.0
        assert config.top_p == 0.0


class TestEOSTokenDetection:
    """Tests for EOS token detection."""

    def test_is_eos_token_default_llama3(self):
        """Test EOS detection with default Llama3 config."""
        config = GenerationConfig()

        assert config.is_eos_token(128001) is True
        assert config.is_eos_token(128009) is True
        assert config.is_eos_token(500) is False

    def test_is_eos_token_custom(self):
        """Test EOS detection with custom EOS tokens."""
        config = GenerationConfig(eos_tokens=[100, 200, 300])

        assert config.is_eos_token(100) is True
        assert config.is_eos_token(200) is True
        assert config.is_eos_token(300) is True
        assert config.is_eos_token(150) is False


class TestStopConditionChecking:
    """Tests for stop condition checking."""

    def test_should_stop_eos_token(self):
        """Test stopping on EOS token."""
        config = GenerationConfig()

        should_stop, reason = config.should_stop(128001, 100)
        assert should_stop is True
        assert reason == "eos_token"

    def test_should_stop_max_length(self):
        """Test stopping on max length."""
        config = GenerationConfig(max_length=100)

        should_stop, reason = config.should_stop(500, 100)
        assert should_stop is True
        assert reason == "max_length"

    def test_should_stop_max_length_not_reached(self):
        """Test that max length not triggered when under limit."""
        config = GenerationConfig(max_length=100)

        should_stop, reason = config.should_stop(500, 50)
        assert should_stop is False
        assert reason == ""

    def test_should_stop_stop_string(self):
        """Test stopping on stop string."""
        config = GenerationConfig(stop_strings=["END", "</response>"])

        should_stop, reason = config.should_stop(500, 50, "This is the END")
        assert should_stop is True
        assert reason == "stop_string"

    def test_should_stop_stop_string_not_found(self):
        """Test that stop string not triggered when not present."""
        config = GenerationConfig(stop_strings=["END"])

        should_stop, reason = config.should_stop(500, 50, "This continues...")
        assert should_stop is False
        assert reason == ""

    def test_should_stop_no_max_length(self):
        """Test that max_length check is skipped when not set."""
        config = GenerationConfig(max_length=None)

        should_stop, reason = config.should_stop(500, 1000000)
        assert should_stop is False
        assert reason == ""

    def test_should_stop_multiple_stop_strings(self):
        """Test multiple stop strings."""
        config = GenerationConfig(stop_strings=["END", "STOP", "FINISH"])

        # First stop string triggers
        should_stop, reason = config.should_stop(500, 50, "Please STOP now")
        assert should_stop is True
        assert reason == "stop_string"


class TestSerialization:
    """Tests for JSON serialization/deserialization."""

    def test_to_dict(self):
        """Test conversion to dictionary."""
        config = GenerationConfig(
            temperature=0.5,
            max_new_tokens=512,
        )

        data = config.to_dict()

        assert data["temperature"] == 0.5
        assert data["max_new_tokens"] == 512
        assert data["model_type"] == "llama3"
        assert data["eos_tokens"] == [128001, 128009]

    def test_to_json(self):
        """Test conversion to JSON string."""
        config = GenerationConfig(temperature=0.7)
        json_str = config.to_json()

        # Should be valid JSON
        data = json.loads(json_str)
        assert data["temperature"] == 0.7

    def test_from_dict(self):
        """Test creation from dictionary."""
        data = {
            "temperature": 0.6,
            "top_p": 0.85,
            "max_new_tokens": 256,
        }

        config = GenerationConfig.from_dict(data)

        assert config.temperature == 0.6
        assert config.top_p == 0.85
        assert config.max_new_tokens == 256

    def test_from_dict_with_none_values(self):
        """Test that None values use defaults."""
        data = {
            "temperature": 0.5,
            "top_p": None,  # Should use default
        }

        config = GenerationConfig.from_dict(data)

        assert config.temperature == 0.5
        assert config.top_p == 0.9  # Default

    def test_from_json(self):
        """Test creation from JSON string."""
        json_str = '{"temperature": 0.8, "top_k": 60}'

        config = GenerationConfig.from_json(json_str)

        assert config.temperature == 0.8
        assert config.top_k == 60

    def test_roundtrip_serialization(self):
        """Test that serialization roundtrip preserves values."""
        original = GenerationConfig(
            temperature=0.65,
            top_p=0.88,
            top_k=45,
            max_new_tokens=768,
            repetition_penalty=1.2,
        )

        # Serialize and deserialize
        json_str = original.to_json()
        restored = GenerationConfig.from_json(json_str)

        assert restored.temperature == original.temperature
        assert restored.top_p == original.top_p
        assert restored.top_k == original.top_k
        assert restored.max_new_tokens == original.max_new_tokens
        assert restored.repetition_penalty == original.repetition_penalty


class TestPresetConfigurations:
    """Tests for preset configuration objects."""

    def test_llama3_config(self):
        """Test LLAMA3_CONFIG preset."""
        assert LLAMA3_CONFIG.model_type == "llama3"
        assert LLAMA3_CONFIG.temperature == 0.7
        assert LLAMA3_CONFIG.top_p == 0.9
        assert LLAMA3_CONFIG.top_k == 50
        assert LLAMA3_CONFIG.eos_tokens == [128001, 128009]

    def test_llama3_greedy_config(self):
        """Test LLAMA3_GREEDY_CONFIG preset."""
        assert LLAMA3_GREEDY_CONFIG.model_type == "llama3"
        assert LLAMA3_GREEDY_CONFIG.temperature == 0.0
        assert LLAMA3_GREEDY_CONFIG.eos_tokens == [128001, 128009]

    def test_llama3_greedy_is_deterministic(self):
        """Test that greedy config produces deterministic output."""
        assert LLAMA3_GREEDY_CONFIG.temperature == 0.0
        assert LLAMA3_GREEDY_CONFIG.top_p == 0.9  # Not used with temp=0

    def test_llama3_high_creative_config(self):
        """Test LLAMA3_HIGH_CREATIVE_CONFIG preset."""
        assert LLAMA3_HIGH_CREATIVE_CONFIG.model_type == "llama3"
        assert LLAMA3_HIGH_CREATIVE_CONFIG.temperature == 1.0
        assert LLAMA3_HIGH_CREATIVE_CONFIG.top_p == 0.95
        assert LLAMA3_HIGH_CREATIVE_CONFIG.top_k == 100
        assert LLAMA3_HIGH_CREATIVE_CONFIG.max_new_tokens == 4096


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_very_high_temperature(self):
        """Test that very high temperature is allowed."""
        config = GenerationConfig(temperature=10.0)
        assert config.temperature == 10.0

    def test_very_high_max_tokens(self):
        """Test that very high max_new_tokens is allowed."""
        config = GenerationConfig(max_new_tokens=1000000)
        assert config.max_new_tokens == 1000000

    def test_empty_stop_strings(self):
        """Test with empty stop strings list."""
        config = GenerationConfig(stop_strings=[])
        should_stop, reason = config.should_stop(500, 50, "any text")
        assert should_stop is False

    def test_none_stop_strings(self):
        """Test with None stop strings."""
        config = GenerationConfig(stop_strings=None)
        should_stop, reason = config.should_stop(500, 50, "any text")
        assert should_stop is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
