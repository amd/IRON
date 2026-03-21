# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Tests for Llama3.2 model configuration.

This module contains comprehensive tests for the Llama32Config class,
covering configuration loading, validation, serialization, and
computed properties.

Test Categories:
    - Configuration loading (from_json, from_dict, from_pretrained)
    - Validation (parameter ranges, GQA compatibility)
    - Serialization (to_json, to_dict, to_json_string)
    - Computed properties (model_size, kv_cache_size, gqa_groups)
    - Memory estimation (estimate_weight_memory, estimate_kv_cache_memory)
    - Edge cases and error handling

Run tests:
    pytest iron/models/test_config.py -v
    pytest iron/models/test_config.py --cov=iron.models.llama32.config
"""

import json
import pytest
import tempfile
import os
from pathlib import Path
from typing import Dict, Any

from iron.models.llama32.config import Llama32Config
from iron.models.registry import ModelRegistry

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def default_config() -> Llama32Config:
    """Create a default Llama3.2 config."""
    return Llama32Config()


@pytest.fixture
def custom_config() -> Llama32Config:
    """Create a custom Llama3.2 config."""
    return Llama32Config(
        vocab_size=32000,
        hidden_size=1024,
        intermediate_size=4096,
        num_hidden_layers=8,
        num_attention_heads=16,
        num_key_value_heads=4,
        head_dim=64,
        max_position_embeddings=4096,
        rope_theta=10000.0,
        rms_norm_eps=1e-6,
    )


@pytest.fixture
def temp_config_file() -> Path:
    """Create a temporary config.json file."""
    config_dict = {
        "vocab_size": 128256,
        "hidden_size": 2048,
        "intermediate_size": 8192,
        "num_hidden_layers": 16,
        "num_attention_heads": 32,
        "num_key_value_heads": 8,
        "head_dim": 64,
        "max_position_embeddings": 131072,
        "rope_theta": 500000.0,
        "rms_norm_eps": 1e-5,
        "model_type": "llama",
        "architectures": ["LlamaForCausalLM"],
        "hidden_act": "silu",
        "tie_word_embeddings": False,
        "attention_bias": False,
        "mlp_bias": False,
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(config_dict, f)
        temp_path = Path(f.name)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def invalid_config_dict() -> Dict[str, Any]:
    """Create an invalid config dictionary for testing validation."""
    return {
        "vocab_size": -1,  # Invalid: negative
        "hidden_size": 2048,
        "num_hidden_layers": 16,
        "num_attention_heads": 32,
        "num_key_value_heads": 7,  # Invalid: 32 % 7 != 0
        "head_dim": 64,
    }


# =============================================================================
# Test: Basic Configuration
# =============================================================================


class TestConfigInitialization:
    """Test Llama32Config initialization."""

    def test_default_values(self, default_config: Llama32Config) -> None:
        """Test that default values are set correctly."""
        assert default_config.vocab_size == 128256
        assert default_config.hidden_size == 2048
        assert default_config.intermediate_size == 8192
        assert default_config.num_hidden_layers == 16
        assert default_config.num_attention_heads == 32
        assert default_config.num_key_value_heads == 8
        assert default_config.head_dim == 64
        assert default_config.max_position_embeddings == 131072
        assert default_config.rope_theta == 500000.0
        assert default_config.rms_norm_eps == 1e-5
        assert default_config.model_type == "llama"
        assert default_config.hidden_act == "silu"

    def test_custom_values(self, custom_config: Llama32Config) -> None:
        """Test that custom values are set correctly."""
        assert custom_config.vocab_size == 32000
        assert custom_config.hidden_size == 1024
        assert custom_config.intermediate_size == 4096
        assert custom_config.num_hidden_layers == 8
        assert custom_config.num_attention_heads == 16
        assert custom_config.num_key_value_heads == 4
        assert custom_config.max_position_embeddings == 4096

    def test_model_path_default(self, default_config: Llama32Config) -> None:
        """Test that model_path is None by default."""
        assert default_config.model_path is None


# =============================================================================
# Test: Validation
# =============================================================================


class TestConfigValidation:
    """Test Llama32Config validation."""

    def test_valid_config_no_exception(self, default_config: Llama32Config) -> None:
        """Test that valid config doesn't raise exceptions."""
        # If we got here without exception, validation passed
        assert default_config.hidden_size > 0

    def test_invalid_vocab_size(self) -> None:
        """Test that negative vocab_size raises ValueError."""
        with pytest.raises(ValueError, match="vocab_size must be >= 1"):
            Llama32Config(vocab_size=-1)

    def test_invalid_hidden_size(self) -> None:
        """Test that non-positive hidden_size raises ValueError."""
        with pytest.raises(ValueError, match="hidden_size must be >= 1"):
            Llama32Config(hidden_size=0)

    def test_invalid_num_hidden_layers(self) -> None:
        """Test that non-positive num_hidden_layers raises ValueError."""
        with pytest.raises(ValueError, match="num_hidden_layers must be >= 1"):
            Llama32Config(num_hidden_layers=0)

    def test_invalid_num_attention_heads(self) -> None:
        """Test that non-positive num_attention_heads raises ValueError."""
        with pytest.raises(ValueError, match="num_attention_heads must be >= 1"):
            Llama32Config(num_attention_heads=0)

    def test_invalid_head_dim(self) -> None:
        """Test that non-positive head_dim raises ValueError."""
        with pytest.raises(ValueError, match="head_dim must be >= 1"):
            Llama32Config(head_dim=0)

    def test_invalid_rms_norm_eps(self) -> None:
        """Test that non-positive rms_norm_eps raises ValueError."""
        with pytest.raises(ValueError, match="rms_norm_eps must be > 0"):
            Llama32Config(rms_norm_eps=0)

    def test_invalid_intermediate_size(self) -> None:
        """Test that non-positive intermediate_size raises ValueError."""
        with pytest.raises(ValueError, match="intermediate_size must be >= 1"):
            Llama32Config(intermediate_size=0)

    def test_invalid_max_position_embeddings(self) -> None:
        """Test that non-positive max_position_embeddings raises ValueError."""
        with pytest.raises(ValueError, match="max_position_embeddings must be >= 1"):
            Llama32Config(max_position_embeddings=0)

    def test_invalid_rope_theta(self) -> None:
        """Test that non-positive rope_theta raises ValueError."""
        with pytest.raises(ValueError, match="rope_theta must be > 0"):
            Llama32Config(rope_theta=0)

    def test_gqa_incompatibility(self) -> None:
        """Test GQA compatibility validation.

        num_attention_heads must be divisible by num_key_value_heads.
        """
        with pytest.raises(ValueError, match="must be divisible"):
            Llama32Config(
                num_attention_heads=32, num_key_value_heads=7  # 32 % 7 = 4 != 0
            )

    def test_gqa_compatibility_valid(self) -> None:
        """Test valid GQA configurations."""
        # 32 / 8 = 4 groups
        config = Llama32Config(num_attention_heads=32, num_key_value_heads=8)
        assert config.gqa_groups == 4

        # 16 / 4 = 4 groups
        config = Llama32Config(num_attention_heads=16, num_key_value_heads=4)
        assert config.gqa_groups == 4

    def test_gqa_single_kv_head(self) -> None:
        """Test single KV head (multi-query attention)."""
        config = Llama32Config(num_attention_heads=32, num_key_value_heads=1)
        assert config.gqa_groups == 32


# =============================================================================
# Test: JSON Loading/Saving
# =============================================================================


class TestConfigSerialization:
    """Test Llama32Config JSON serialization."""

    def test_from_json(self, temp_config_file: Path) -> None:
        """Test loading config from JSON file."""
        config = Llama32Config.from_json(temp_config_file)

        assert config.vocab_size == 128256
        assert config.hidden_size == 2048
        assert config.num_hidden_layers == 16
        assert config.num_attention_heads == 32
        assert config.num_key_value_heads == 8

    def test_from_json_file_not_found(self) -> None:
        """Test that missing JSON file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            Llama32Config.from_json("/nonexistent/path/config.json")

    def test_to_json(self, default_config: Llama32Config) -> None:
        """Test saving config to JSON file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            json_path = Path(tmpdir) / "config.json"
            default_config.to_json(json_path)

            assert json_path.exists()

            # Reload and verify
            reloaded = Llama32Config.from_json(json_path)
            assert reloaded.vocab_size == default_config.vocab_size
            assert reloaded.hidden_size == default_config.hidden_size

    def test_to_dict(self, default_config: Llama32Config) -> None:
        """Test converting config to dictionary."""
        config_dict = default_config.to_dict()

        assert isinstance(config_dict, dict)
        assert config_dict["vocab_size"] == 128256
        assert config_dict["hidden_size"] == 2048
        assert config_dict["num_hidden_layers"] == 16
        assert config_dict["architectures"] == ["LlamaForCausalLM"]

    def test_from_dict(self, default_config: Llama32Config) -> None:
        """Test creating config from dictionary."""
        config_dict = default_config.to_dict()
        reloaded = Llama32Config.from_dict(config_dict)

        assert reloaded.vocab_size == default_config.vocab_size
        assert reloaded.hidden_size == default_config.hidden_size
        assert reloaded.num_hidden_layers == default_config.num_hidden_layers

    def test_from_dict_filters_unknown_keys(self) -> None:
        """Test that from_dict filters out unknown keys."""
        config_dict = {
            "vocab_size": 32000,
            "hidden_size": 2048,
            "unknown_key": "should_be_ignored",
            "another_unknown": 12345,
        }

        config = Llama32Config.from_dict(config_dict)
        assert config.vocab_size == 32000
        assert config.hidden_size == 2048
        # Unknown keys should be ignored, not cause errors

    def test_to_json_string(self, default_config: Llama32Config) -> None:
        """Test converting config to JSON string."""
        json_str = default_config.to_json_string()

        assert isinstance(json_str, str)

        # Parse and verify
        parsed = json.loads(json_str)
        assert parsed["vocab_size"] == default_config.vocab_size

    def test_roundtrip_json(self, default_config: Llama32Config) -> None:
        """Test JSON roundtrip (to_dict -> from_dict)."""
        original = default_config
        config_dict = original.to_dict()
        reloaded = Llama32Config.from_dict(config_dict)

        assert reloaded.vocab_size == original.vocab_size
        assert reloaded.hidden_size == original.hidden_size
        assert reloaded.num_hidden_layers == original.num_hidden_layers
        assert reloaded.num_attention_heads == original.num_attention_heads


# =============================================================================
# Test: Computed Properties
# =============================================================================


class TestConfigProperties:
    """Test Llama32Config computed properties."""

    def test_model_size_1b(self) -> None:
        """Test model size calculation for 1B model."""
        config = Llama32Config(
            hidden_size=2048,
            num_hidden_layers=16,
            intermediate_size=8192,
            vocab_size=128256,
        )
        size = config.model_size
        assert size.endswith("B") or size.endswith("M")

    def test_model_size_approximate(self, default_config: Llama32Config) -> None:
        """Test that model size is approximately correct."""
        size_str = default_config.model_size

        # Should be a reasonable size for Llama3.2-1B
        assert any(size_str.endswith(s) for s in ["B", "M", "K"])

    def test_kv_cache_size_per_token(self, default_config: Llama32Config) -> None:
        """Test KV cache size calculation."""
        # 2 * 16 layers * 8 KV heads * 64 head_dim * 4 bytes (float32)
        expected = 2 * 16 * 8 * 64 * 4
        assert default_config.kv_cache_size_per_token == expected

    def test_kv_cache_size_per_token_bf16(self, default_config: Llama32Config) -> None:
        """Test KV cache size calculation for bfloat16."""
        # 2 * 16 layers * 8 KV heads * 64 head_dim * 2 bytes (bfloat16)
        expected = 2 * 16 * 8 * 64 * 2
        assert default_config.kv_cache_size_per_token_bf16 == expected

    def test_gqa_groups(self, default_config: Llama32Config) -> None:
        """Test GQA groups calculation."""
        # 32 attention heads / 8 KV heads = 4 groups
        assert default_config.gqa_groups == 4

    def test_hidden_per_layer_bytes(self, default_config: Llama32Config) -> None:
        """Test hidden state bytes calculation."""
        # 2048 * 4 bytes (float32)
        expected = 2048 * 4
        assert default_config.hidden_per_layer_bytes == expected

    def test_num_attention_layers(self, default_config: Llama32Config) -> None:
        """Test num_attention_layers alias."""
        assert default_config.num_attention_layers == default_config.num_hidden_layers


# =============================================================================
# Test: Memory Estimation
# =============================================================================


class TestConfigMemoryEstimation:
    """Test Llama32Config memory estimation methods."""

    def test_estimate_weight_memory_float32(
        self, default_config: Llama32Config
    ) -> None:
        """Test weight memory estimation for float32."""
        memory = default_config.estimate_weight_memory("float32")

        # Should be a reasonable size for a 1B model
        assert memory > 0
        assert memory < 10e9  # Less than 10GB

    def test_estimate_weight_memory_bf16(self, default_config: Llama32Config) -> None:
        """Test weight memory estimation for bfloat16."""
        memory_bf16 = default_config.estimate_weight_memory("bfloat16")
        memory_f32 = default_config.estimate_weight_memory("float32")

        # bfloat16 should use half the memory of float32
        assert memory_bf16 == memory_f32 // 2

    def test_estimate_weight_memory_unknown_dtype(
        self, default_config: Llama32Config
    ) -> None:
        """Test weight memory estimation with unknown dtype."""
        memory = default_config.estimate_weight_memory("unknown")

        # Should default to 4 bytes per param
        assert memory > 0

    def test_estimate_kv_cache_memory(self, default_config: Llama32Config) -> None:
        """Test KV cache memory estimation."""
        memory = default_config.estimate_kv_cache_memory(
            batch_size=1, seq_len=1024, dtype="float32"
        )

        # Should be positive and reasonable
        assert memory > 0
        assert memory < 10e9  # Less than 10GB

    def test_estimate_kv_cache_memory_scales_with_batch(
        self, default_config: Llama32Config
    ) -> None:
        """Test that KV cache scales with batch size."""
        memory_1 = default_config.estimate_kv_cache_memory(
            batch_size=1, seq_len=1024, dtype="float32"
        )
        memory_4 = default_config.estimate_kv_cache_memory(
            batch_size=4, seq_len=1024, dtype="float32"
        )

        assert memory_4 == memory_1 * 4

    def test_estimate_kv_cache_memory_scales_with_seq_len(
        self, default_config: Llama32Config
    ) -> None:
        """Test that KV cache scales with sequence length."""
        memory_1k = default_config.estimate_kv_cache_memory(
            batch_size=1, seq_len=1024, dtype="float32"
        )
        memory_4k = default_config.estimate_kv_cache_memory(
            batch_size=1, seq_len=4096, dtype="float32"
        )

        assert memory_4k == memory_1k * 4


# =============================================================================
# Test: String Representations
# =============================================================================


class TestConfigStringRepresentation:
    """Test Llama32Config string representations."""

    def test_str(self, default_config: Llama32Config) -> None:
        """Test __str__ method."""
        str_repr = str(default_config)

        assert "Llama32Config" in str_repr
        assert "vocab_size" in str_repr
        assert "hidden_size" in str_repr
        assert "128256" in str_repr  # vocab_size value

    def test_repr(self, default_config: Llama32Config) -> None:
        """Test __repr__ method."""
        repr_repr = repr(default_config)

        assert "Llama32Config" in repr_repr
        assert "vocab_size" in repr_repr


# =============================================================================
# Test: Model Registry Integration
# =============================================================================


class TestModelRegistryIntegration:
    """Test integration with ModelRegistry."""

    def test_llama_registered(self) -> None:
        """Test that 'llama' model type is registered."""
        assert ModelRegistry.is_supported("llama")

    def test_llama_config_class(self) -> None:
        """Test that Llama32Config is the registered config class."""
        config_class = ModelRegistry.get_config_class("llama")
        assert config_class == Llama32Config

    def test_llama_variants(self) -> None:
        """Test that Llama3.2 variants are registered."""
        assert ModelRegistry.validate_variant("llama", "meta-llama/Llama-3.2-1B")

    def test_llama_default_variant(self) -> None:
        """Test default variant for Llama3.2."""
        spec = ModelRegistry.get("llama")
        assert spec is not None
        assert spec.default_variant == "meta-llama/Llama-3.2-1B"


# =============================================================================
# Test: Edge Cases
# =============================================================================


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_minimum_valid_config(self) -> None:
        """Test minimum valid configuration values."""
        config = Llama32Config(
            vocab_size=1,
            hidden_size=1,
            intermediate_size=1,
            num_hidden_layers=1,
            num_attention_heads=1,
            num_key_value_heads=1,
            head_dim=1,
            rms_norm_eps=1e-10,
            max_position_embeddings=1,
            rope_theta=1.0,
        )
        # Should not raise
        assert config.vocab_size == 1

    def test_very_large_config(self) -> None:
        """Test very large configuration values."""
        config = Llama32Config(
            vocab_size=1000000,
            hidden_size=16384,
            num_hidden_layers=128,
            num_attention_heads=128,
            num_key_value_heads=128,
            max_position_embeddings=1000000,
        )
        # Should not raise
        assert config.vocab_size == 1000000

    def test_rope_scaling_none_by_default(self, default_config: Llama32Config) -> None:
        """Test that rope_scaling is None by default."""
        assert default_config.rope_scaling is None

    def test_rope_scaling_with_dict(self) -> None:
        """Test config with rope_scaling dictionary."""
        config = Llama32Config(rope_scaling={"type": "linear", "factor": 2.0})
        assert config.rope_scaling is not None
        assert config.rope_scaling["type"] == "linear"

    def test_architectures_list_default(self, default_config: Llama32Config) -> None:
        """Test default architectures list."""
        assert default_config.architectures == ["LlamaForCausalLM"]

    def test_tie_word_embeddings_default(self, default_config: Llama32Config) -> None:
        """Test default tie_word_embeddings value."""
        assert default_config.tie_word_embeddings is False

    def test_attention_bias_default(self, default_config: Llama32Config) -> None:
        """Test default attention_bias value."""
        assert default_config.attention_bias is False

    def test_mlp_bias_default(self, default_config: Llama32Config) -> None:
        """Test default mlp_bias value."""
        assert default_config.mlp_bias is False


# =============================================================================
# Test: HuggingFace Integration (Mocked)
# =============================================================================


class TestHuggingFaceIntegration:
    """Test HuggingFace Hub integration (mocked)."""

    def test_from_pretrained_import_error(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test from_pretrained handles missing huggingface_hub."""

        # Mock the import to fail
        def mock_import(name, *args, **kwargs):
            if name == "huggingface_hub":
                raise ImportError("No module named 'huggingface_hub'")
            return __import__(name, *args, **kwargs)

        monkeypatch.setattr("builtins.__import__", mock_import)

        with pytest.raises(ImportError, match="huggingface_hub"):
            Llama32Config.from_pretrained("meta-llama/Llama-3.2-1B")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
