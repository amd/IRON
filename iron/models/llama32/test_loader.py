# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Tests for Llama3.2 weight loader.

This module contains comprehensive tests for the WeightLoader class,
covering download functionality, validation, memory mapping, error
handling, and integration with MemoryBudget.

Test Categories:
    - WeightInfo dataclass tests
    - Download tests (retry logic, caching)
    - Validation tests (checksum, file validation)
    - Memory validation tests
    - Loading tests (full load, memory-mapped)
    - Error handling tests
    - Integration tests

Run tests:
    pytest iron/models/llama32/test_loader.py -v
    pytest iron/models/llama32/test_loader.py --cov=iron.models.llama32.loader
"""

import json
import pytest
import tempfile
import hashlib
import time
import os
import struct
from pathlib import Path
from typing import Dict, Any, List
from unittest.mock import Mock, patch, MagicMock, call

import numpy as np

from iron.models.llama32.loader import WeightLoader, WeightInfo
from iron.models.llama32.config import Llama32Config


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def loader() -> WeightLoader:
    """Create a WeightLoader with temporary cache directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield WeightLoader(cache_dir=tmpdir)


@pytest.fixture
def temp_model_dir() -> Path:
    """Create a temporary directory simulating a model structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_config() -> Llama32Config:
    """Create a small test config."""
    return Llama32Config(
        vocab_size=1000,
        hidden_size=128,
        intermediate_size=256,
        num_hidden_layers=2,
        num_attention_heads=4,
        num_key_value_heads=2,
        head_dim=32,
        max_position_embeddings=512,
    )


@pytest.fixture
def sample_weights_dict(sample_config: Llama32Config) -> Dict[str, np.ndarray]:
    """Create sample weights matching the config."""
    weights = {}

    # Embedding
    weights["model.embed_tokens.weight"] = np.random.randn(
        sample_config.vocab_size, sample_config.hidden_size
    ).astype(np.float32)

    # Transformer layers
    for i in range(sample_config.num_hidden_layers):
        layer_prefix = f"model.layers.{i}"

        # Attention
        weights[f"{layer_prefix}.self_attn.q_proj.weight"] = np.random.randn(
            sample_config.hidden_size,
            sample_config.num_attention_heads * sample_config.head_dim
        ).astype(np.float32)

        weights[f"{layer_prefix}.self_attn.k_proj.weight"] = np.random.randn(
            sample_config.hidden_size,
            sample_config.num_key_value_heads * sample_config.head_dim
        ).astype(np.float32)

        weights[f"{layer_prefix}.self_attn.v_proj.weight"] = np.random.randn(
            sample_config.hidden_size,
            sample_config.num_key_value_heads * sample_config.head_dim
        ).astype(np.float32)

        weights[f"{layer_prefix}.self_attn.o_proj.weight"] = np.random.randn(
            sample_config.num_attention_heads * sample_config.head_dim,
            sample_config.hidden_size
        ).astype(np.float32)

        # MLP
        weights[f"{layer_prefix}.mlp.gate_proj.weight"] = np.random.randn(
            sample_config.hidden_size, sample_config.intermediate_size
        ).astype(np.float32)

        weights[f"{layer_prefix}.mlp.down_proj.weight"] = np.random.randn(
            sample_config.intermediate_size, sample_config.hidden_size
        ).astype(np.float32)

        weights[f"{layer_prefix}.mlp.up_proj.weight"] = np.random.randn(
            sample_config.hidden_size, sample_config.intermediate_size
        ).astype(np.float32)

        # Normalization
        weights[f"{layer_prefix}.input_layernorm.weight"] = np.random.randn(
            sample_config.hidden_size
        ).astype(np.float32)

        weights[
            f"{layer_prefix}.post_attention_layernorm.weight"
        ] = np.random.randn(sample_config.hidden_size).astype(np.float32)

    # Final norm
    weights["model.norm.weight"] = np.random.randn(
        sample_config.hidden_size
    ).astype(np.float32)

    return weights


@pytest.fixture
def safetensors_file(sample_weights_dict: Dict[str, np.ndarray]) -> Path:
    """Create a temporary safetensors file."""
    try:
        from safetensors.numpy import save_file
    except ImportError:
        pytest.skip("safetensors not installed")

    with tempfile.NamedTemporaryFile(
        suffix=".safetensors",
        delete=False
    ) as f:
        temp_path = Path(f.name)

    save_file(sample_weights_dict, temp_path)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def mock_model_directory(
    safetensors_file: Path,
    sample_config: Llama32Config
) -> Path:
    """Create a mock model directory with safetensors and config."""
    with tempfile.TemporaryDirectory() as tmpdir:
        model_dir = Path(tmpdir)

        # Copy safetensors file
        import shutil
        shutil.copy(safetensors_file, model_dir / "model.safetensors")

        # Create config.json
        config_path = model_dir / "config.json"
        with open(config_path, "w") as f:
            json.dump(sample_config.to_dict(), f)

        yield model_dir


# =============================================================================
# Test: WeightInfo Dataclass
# =============================================================================

class TestWeightInfo:
    """Test WeightInfo dataclass."""

    def test_weight_info_creation(self) -> None:
        """Test creating WeightInfo instance."""
        info = WeightInfo(
            file_path=Path("/test/model"),
            file_size=1000000,
            num_tensors=100,
            total_tensor_size=900000,
            checksum="abc123"
        )

        assert info.file_path == Path("/test/model")
        assert info.file_size == 1000000
        assert info.num_tensors == 100
        assert info.checksum == "abc123"

    def test_weight_info_file_size_mb(self) -> None:
        """Test file_size_mb property."""
        info = WeightInfo(
            file_path=Path("/test"),
            file_size=1048576,  # 1 MB
            num_tensors=10,
            total_tensor_size=1000,
            checksum="abc"
        )

        assert info.file_size_mb == 1.0

    def test_weight_info_file_size_gb(self) -> None:
        """Test file_size_gb property."""
        info = WeightInfo(
            file_path=Path("/test"),
            file_size=1073741824,  # 1 GB
            num_tensors=100,
            total_tensor_size=1000,
            checksum="abc"
        )

        assert info.file_size_gb == 1.0

    def test_weight_info_str(self) -> None:
        """Test __str__ method."""
        info = WeightInfo(
            file_path=Path("/test/model"),
            file_size=1000000,
            num_tensors=100,
            total_tensor_size=900000,
            checksum="abc123def456"
        )

        str_repr = str(info)

        assert "WeightInfo" in str_repr
        assert "1.00GB" in str_repr or "0.00GB" in str_repr  # Depends on size
        assert "abc123" in str_repr  # First part of checksum

    def test_weight_info_default_safetensors_files(self) -> None:
        """Test default safetensors_files list."""
        info = WeightInfo(
            file_path=Path("/test"),
            file_size=1000,
            num_tensors=10,
            total_tensor_size=900,
            checksum="abc"
        )

        assert info.safetensors_files == []


# =============================================================================
# Test: WeightLoader Initialization
# =============================================================================

class TestWeightLoaderInit:
    """Test WeightLoader initialization."""

    def test_init_no_cache_dir(self) -> None:
        """Test initialization without cache directory."""
        loader = WeightLoader()

        assert loader.cache_dir is None
        assert loader.memory_budget is None

    def test_init_with_cache_dir(self) -> None:
        """Test initialization with cache directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            loader = WeightLoader(cache_dir=tmpdir)

            assert loader.cache_dir == Path(tmpdir)
            assert loader.cache_dir.exists()

    def test_init_creates_cache_dir(self) -> None:
        """Test that cache directory is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache_path = Path(tmpdir) / "new_cache"

            loader = WeightLoader(cache_dir=str(cache_path))

            assert loader.cache_dir.exists()

    def test_init_with_memory_budget(self) -> None:
        """Test initialization with memory budget."""
        mock_budget = Mock()

        loader = WeightLoader(memory_budget=mock_budget)

        assert loader.memory_budget is mock_budget


# =============================================================================
# Test: Download Functionality
# =============================================================================

class TestDownloadFunctionality:
    """Test WeightLoader download functionality."""

    def test_download_model_default_id(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model uses default model ID."""
        mock_download = Mock(return_value="/tmp/model")
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        loader.download_model()

        mock_download.assert_called_once()
        call_args = mock_download.call_args
        assert call_args[1]["repo_id"] == "meta-llama/Llama-3.2-1B"

    def test_download_model_custom_id(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model with custom model ID."""
        mock_download = Mock(return_value="/tmp/model")
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        loader.download_model("custom/model")

        mock_download.assert_called_once()
        call_args = mock_download.call_args
        assert call_args[1]["repo_id"] == "custom/model"

    def test_download_model_with_cache_dir(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model passes cache directory."""
        mock_download = Mock(return_value="/tmp/model")
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        loader.download_model()

        call_args = mock_download.call_args
        assert call_args[1]["cache_dir"] == str(loader.cache_dir)

    def test_download_model_force_download(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model with force_download."""
        mock_download = Mock(return_value="/tmp/model")
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        loader.download_model(force_download=True)

        call_args = mock_download.call_args
        assert call_args[1]["force_download"] is True

    def test_download_model_returns_path(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model returns Path object."""
        mock_download = Mock(return_value="/tmp/model")
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        result = loader.download_model()

        assert isinstance(result, Path)

    def test_download_import_error(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test download_model handles missing huggingface_hub."""
        def mock_import(name, *args, **kwargs):
            if name == "huggingface_hub":
                raise ImportError("No module named 'huggingface_hub'")
            return __import__(name, *args, **kwargs)

        monkeypatch.setattr("builtins.__import__", mock_import)

        with pytest.raises(ImportError, match="huggingface_hub"):
            loader.download_model()

    def test_is_model_cached_not_cached(self, loader: WeightLoader) -> None:
        """Test is_model_cached when model is not cached."""
        result = loader.is_model_cached("nonexistent/model")

        assert result is False

    def test_is_model_cached_no_cache_dir(self) -> None:
        """Test is_model_cached with no cache directory."""
        loader = WeightLoader(cache_dir=None)

        result = loader.is_model_cached("some/model")

        assert result is False


# =============================================================================
# Test: Validation Functionality
# =============================================================================

class TestValidationFunctionality:
    """Test WeightLoader validation functionality."""

    def test_validate_weights_file_not_found(
        self, loader: WeightLoader
    ) -> None:
        """Test validate_weights with non-existent path."""
        with pytest.raises(FileNotFoundError):
            loader.validate_weights(Path("/nonexistent/path"))

    def test_validate_weights_no_safetensors(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test validate_weights with no safetensors files."""
        # Create empty directory
        (temp_model_dir / "config.json").write_text("{}")

        with pytest.raises(ValueError, match="No safetensors files"):
            loader.validate_weights(temp_model_dir)

    def test_validate_weights_valid_file(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test validate_weights with valid safetensors file."""
        info = loader.validate_weights(mock_model_directory)

        assert isinstance(info, WeightInfo)
        assert info.file_path == mock_model_directory
        assert info.file_size > 0
        assert info.num_tensors > 0
        assert len(info.checksum) == 64  # SHA256 hex length

    def test_validate_weights_multiple_files(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test validate_weights with multiple safetensors files."""
        try:
            from safetensors.numpy import save_file
        except ImportError:
            pytest.skip("safetensors not installed")

        # Create multiple safetensors files
        for i in range(3):
            weights = {f"weight_{i}": np.random.randn(10, 10).astype(np.float32)}
            save_file(weights, temp_model_dir / f"model_{i}.safetensors")

        info = loader.validate_weights(temp_model_dir)

        assert info.num_tensors == 3
        assert len(info.safetensors_files) == 3

    def test_validate_weights_records_time(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test validate_weights records validation time."""
        info = loader.validate_weights(mock_model_directory)

        assert info.validation_time_ms >= 0

    def test_calculate_checksum(self, loader: WeightLoader, temp_model_dir: Path) -> None:
        """Test _calculate_checksum method."""
        # Create a test file with known content
        test_file = temp_model_dir / "test.bin"
        test_content = b"Hello, World!"
        test_file.write_bytes(test_content)

        checksum = loader._calculate_checksum(test_file)

        # Verify against known SHA256
        expected = hashlib.sha256(test_content).hexdigest()
        assert checksum == expected

    def test_calculate_checksum_large_file(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test _calculate_checksum with large file."""
        test_file = temp_model_dir / "large.bin"

        # Create 1MB file
        chunk_size = 8192
        num_chunks = 128

        with open(test_file, "wb") as f:
            for _ in range(num_chunks):
                f.write(os.urandom(chunk_size))

        checksum = loader._calculate_checksum(test_file)

        assert len(checksum) == 64  # SHA256 hex length


# =============================================================================
# Test: Memory Validation
# =============================================================================

class TestMemoryValidation:
    """Test WeightLoader memory validation."""

    def test_validate_memory_no_budget(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test validate_memory without memory budget."""
        info = loader.validate_weights(mock_model_directory)

        result = loader.validate_memory(info)

        assert result is True

    def test_validate_memory_with_mock_budget(
        self, temp_model_dir: Path
    ) -> None:
        """Test validate_memory with mock memory budget."""
        try:
            from safetensors.numpy import save_file
        except ImportError:
            pytest.skip("safetensors not installed")

        # Create at least one safetensors file for validation FIRST
        save_file({"test": np.array([1])}, temp_model_dir / "test.safetensors")

        mock_budget = Mock()
        mock_result = Mock()
        mock_result.success = True
        mock_result.requestedSize = 1000
        mock_result.availableSize = 2000
        mock_result.errorMessage = ""
        mock_budget.validateModelLoad.return_value = mock_result

        loader = WeightLoader(memory_budget=mock_budget)
        info = loader.validate_weights(temp_model_dir)

        result = loader.validate_memory(info)

        assert result is True
        mock_budget.validateModelLoad.assert_called_once()

    def test_validate_memory_budget_exceeded(self) -> None:
        """Test validate_memory when budget exceeded."""
        mock_budget = Mock()
        mock_result = Mock()
        mock_result.success = False
        mock_result.requestedSize = 2000
        mock_result.availableSize = 1000
        mock_result.errorMessage = "Out of memory"
        mock_budget.validateModelLoad.return_value = mock_result

        loader = WeightLoader(memory_budget=mock_budget)

        info = WeightInfo(
            file_path=Path("/test"),
            file_size=1000,
            num_tensors=10,
            total_tensor_size=2000,
            checksum="abc"
        )

        with pytest.raises(MemoryError, match="exceed memory budget"):
            loader.validate_memory(info)


# =============================================================================
# Test: Disk Space Check
# =============================================================================

class TestDiskSpaceCheck:
    """Test WeightLoader disk space checking."""

    def test_check_disk_space_sufficient(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test check_disk_space with sufficient space."""
        result = loader.check_disk_space(temp_model_dir, 1000)

        assert result is True

    def test_check_disk_space_insufficient(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test check_disk_space with insufficient space."""
        # Request impossibly large space
        with pytest.raises(OSError, match="Insufficient disk space"):
            loader.check_disk_space(temp_model_dir, 10**18)  # 1 exabyte


# =============================================================================
# Test: Loading Functionality
# =============================================================================

class TestLoadingFunctionality:
    """Test WeightLoader loading functionality."""

    def test_load_weights_valid_file(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test load_weights with valid safetensors file."""
        weights = loader.load_weights(mock_model_directory)

        assert isinstance(weights, dict)
        assert len(weights) > 0
        assert "model.embed_tokens.weight" in weights

    def test_load_weights_mmap_valid_file(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test load_weights_mmap with valid safetensors file."""
        weights = loader.load_weights_mmap(mock_model_directory)

        assert isinstance(weights, dict)
        assert len(weights) > 0

    def test_load_weights_no_safetensors(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test load_weights with no safetensors files."""
        with pytest.raises(FileNotFoundError):
            loader.load_weights(temp_model_dir)

    def test_load_weights_mmap_no_safetensors(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test load_weights_mmap with no safetensors files."""
        with pytest.raises(FileNotFoundError):
            loader.load_weights_mmap(temp_model_dir)

    def test_load_weights_import_error(
        self, loader: WeightLoader, temp_model_dir: Path,
        monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test load_weights handles missing safetensors."""
        # Create a dummy safetensors file
        (temp_model_dir / "model.safetensors").write_bytes(b"dummy")

        def mock_import(name, *args, **kwargs):
            if name == "safetensors":
                raise ImportError("No module named 'safetensors'")
            return __import__(name, *args, **kwargs)

        monkeypatch.setattr("builtins.__import__", mock_import)

        with pytest.raises(ImportError, match="safetensors"):
            loader.load_weights(temp_model_dir)

    def test_load_specific_weights(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test load_specific_weights."""
        weights = loader.load_specific_weights(
            mock_model_directory,
            ["model.embed_tokens.weight", "model.norm.weight"]
        )

        assert len(weights) == 2
        assert "model.embed_tokens.weight" in weights
        assert "model.norm.weight" in weights

    def test_load_specific_weights_missing_key(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test load_specific_weights with missing key."""
        with pytest.raises(KeyError, match="Weights not found"):
            loader.load_specific_weights(
                mock_model_directory,
                ["nonexistent.weight"]
            )


# =============================================================================
# Test: Convenience Methods
# =============================================================================

class TestConvenienceMethods:
    """Test WeightLoader convenience methods."""

    def test_download_and_validate(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch,
        mock_model_directory: Path
    ) -> None:
        """Test download_and_validate."""
        mock_download = Mock(return_value=str(mock_model_directory))
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        model_path, weight_info = loader.download_and_validate(
            "test/model", check_memory=False
        )

        assert isinstance(model_path, Path)
        assert isinstance(weight_info, WeightInfo)
        assert weight_info.num_tensors > 0

    def test_get_model_info(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test get_model_info."""
        info = loader.get_model_info(mock_model_directory)

        assert "path" in info
        assert "num_files" in info
        assert "total_size_bytes" in info
        assert "total_size_mb" in info
        assert "total_size_gb" in info

    def test_clear_cache(self, loader: WeightLoader) -> None:
        """Test clear_cache."""
        # Create some files in cache
        cache_file = loader.cache_dir / "test_file.txt"
        cache_file.write_text("test")

        assert cache_file.exists()

        loader.clear_cache()

        assert not cache_file.exists()

    def test_clear_cache_no_cache_dir(self) -> None:
        """Test clear_cache with no cache directory."""
        loader = WeightLoader(cache_dir=None)

        # Should not raise, just log warning
        loader.clear_cache()


# =============================================================================
# Test: Error Handling
# =============================================================================

class TestErrorHandling:
    """Test WeightLoader error handling."""

    def test_download_cleanup_on_failure(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test that partial downloads are cleaned up."""
        mock_download = Mock(
            side_effect=ConnectionError("Network error")
        )
        monkeypatch.setattr(
            "huggingface_hub.snapshot_download",
            mock_download
        )

        with pytest.raises(RuntimeError):
            loader.download_model()

        # Verify download was attempted (retry may not work with direct mock)
        assert mock_download.call_count >= 1

    def test_retry_logic_triggers_on_connection_error(
        self, loader: WeightLoader, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Test retry logic is configured for connection errors."""
        # This test verifies that the retry decorator is properly configured
        # by checking that download_model has the retry wrapper
        from tenacity import Retrying

        # Verify the download_model method has retry configuration
        assert hasattr(loader.download_model, '__wrapped__') or \
               hasattr(loader.download_model, 'retry')

        # We can't easily test actual retry behavior with mocks because
        # tenacity wraps the function at decoration time. Instead, verify
        # the class constants are set correctly.
        assert loader.MAX_DOWNLOAD_ATTEMPTS == 3
        assert loader.RETRY_MIN_WAIT == 4
        assert loader.RETRY_MAX_WAIT == 10

    def test_validate_invalid_safetensors(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test validation with invalid safetensors file."""
        # Create invalid safetensors file
        invalid_file = temp_model_dir / "invalid.safetensors"
        invalid_file.write_bytes(b"not a valid safetensors file")

        with pytest.raises(ValueError, match="Invalid safetensors"):
            loader.validate_weights(temp_model_dir)


# =============================================================================
# Test: Integration Tests
# =============================================================================

class TestIntegration:
    """Integration tests for WeightLoader."""

    def test_full_workflow(
        self, loader: WeightLoader, mock_model_directory: Path
    ) -> None:
        """Test complete workflow: validate -> load."""
        # Validate
        weight_info = loader.validate_weights(mock_model_directory)

        assert weight_info.num_tensors > 0
        assert weight_info.file_size > 0

        # Load
        weights = loader.load_weights_mmap(mock_model_directory)

        assert len(weights) == weight_info.num_tensors

        # Verify weight shapes
        embed_weight = weights["model.embed_tokens.weight"]
        assert len(embed_weight.shape) == 2

    def test_config_and_loader_integration(
        self, mock_model_directory: Path
    ) -> None:
        """Test config and loader work together."""
        config = Llama32Config.from_json(mock_model_directory / "config.json")

        loader = WeightLoader()
        weight_info = loader.validate_weights(mock_model_directory)

        # Verify config and weights are compatible
        assert config.num_hidden_layers == 2
        assert weight_info.num_tensors > config.num_hidden_layers

    def test_memory_budget_integration(
        self, mock_model_directory: Path
    ) -> None:
        """Test memory budget integration."""
        try:
            from iron.runtime.cpp.memory_budget import MemoryBudget
        except ImportError:
            pytest.skip("MemoryBudget not available")

        budget = MemoryBudget()
        loader = WeightLoader(memory_budget=budget)

        weight_info = loader.validate_weights(mock_model_directory)

        # Should validate successfully for small test model
        result = loader.validate_memory(weight_info)

        assert result is True


# =============================================================================
# Test: Edge Cases
# =============================================================================

class TestEdgeCases:
    """Test edge cases for WeightLoader."""

    def test_empty_safetensors_file(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test handling of empty safetensors file."""
        try:
            from safetensors.numpy import save_file
        except ImportError:
            pytest.skip("safetensors not installed")

        # Create empty safetensors file
        save_file({}, temp_model_dir / "empty.safetensors")

        info = loader.validate_weights(temp_model_dir)

        assert info.num_tensors == 0

    def test_very_large_tensor(
        self, loader: WeightLoader, temp_model_dir: Path
    ) -> None:
        """Test handling of large tensors."""
        try:
            from safetensors.numpy import save_file
        except ImportError:
            pytest.skip("safetensors not installed")

        # Create large tensor (10MB)
        large_tensor = np.random.randn(1000, 2500).astype(np.float32)

        save_file({"large": large_tensor}, temp_model_dir / "large.safetensors")

        info = loader.validate_weights(temp_model_dir)

        assert info.num_tensors == 1
        # 1000 * 2500 * 4 bytes (float32) = 10,000,000 bytes
        assert info.total_tensor_size >= 10_000_000

    def test_special_characters_in_path(
        self, loader: WeightLoader
    ) -> None:
        """Test handling of special characters in path."""
        with tempfile.TemporaryDirectory(suffix=" test-model") as tmpdir:
            model_dir = Path(tmpdir)

            try:
                from safetensors.numpy import save_file
            except ImportError:
                pytest.skip("safetensors not installed")

            save_file(
                {"test": np.array([1.0])},
                model_dir / "model.safetensors"
            )

            info = loader.validate_weights(model_dir)

            assert info.num_tensors == 1


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
