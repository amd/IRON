# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Unit tests for KVCacheManager.

This module contains comprehensive tests for the KV cache manager
component including block allocation, KV read/write, and sequence management.

COVERAGE TARGET:
- 20+ tests for KV cache management
- >90% line coverage
- All acceptance criteria verified

TEST CATEGORIES:
1. Initialization tests
2. Sequence lifecycle tests
3. KV write/read tests
4. Context reading tests
5. Block management tests
6. Statistics tests
7. Edge case tests
8. Multi-sequence tests
"""

from __future__ import annotations

import pytest
import numpy as np

from iron.generation.kv_manager import KVCacheManager, SequenceInfo
from iron.models.llama32.config import Llama32Config

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
        num_hidden_layers=4,
        num_attention_heads=4,
        num_key_value_heads=2,
        head_dim=32,
        max_position_embeddings=512,
        block_size=16,
        rms_norm_eps=1e-5,
    )


@pytest.fixture
def kv_manager(sample_config: Llama32Config) -> KVCacheManager:
    """Create a KVCacheManager for testing."""
    return KVCacheManager(sample_config, max_sequences=8, max_blocks_per_sequence=32)


@pytest.fixture
def sample_prompt() -> list[int]:
    """Create a sample prompt."""
    return [10, 20, 30, 40, 50]


@pytest.fixture
def sample_kv_vectors(sample_config: Llama32Config) -> tuple[np.ndarray, np.ndarray]:
    """Create sample KV vectors."""
    key = np.random.randn(
        sample_config.num_attention_heads, sample_config.head_dim
    ).astype(np.float32)
    value = np.random.randn(
        sample_config.num_attention_heads, sample_config.head_dim
    ).astype(np.float32)
    return key, value


# =============================================================================
# Test Categories
# =============================================================================

# -----------------------------------------------------------------------------
# Category 1: Initialization Tests
# -----------------------------------------------------------------------------


class TestInitialization:
    """Tests for KVCacheManager initialization."""

    def test_init_with_defaults(self, sample_config):
        """Test initialization with default parameters."""
        manager = KVCacheManager(sample_config)
        assert manager.config is sample_config
        assert manager.max_sequences == 16
        assert len(manager.sequences) == 0

    def test_init_with_custom_params(self, sample_config):
        """Test initialization with custom parameters."""
        manager = KVCacheManager(
            sample_config, max_sequences=4, max_blocks_per_sequence=16
        )
        assert manager.max_sequences == 4
        assert manager.max_blocks_per_sequence == 16

    def test_init_empty_sequences(self, sample_config):
        """Test that initialization starts with no sequences."""
        manager = KVCacheManager(sample_config)
        assert len(manager) == 0


# -----------------------------------------------------------------------------
# Category 2: Sequence Lifecycle Tests
# -----------------------------------------------------------------------------


class TestSequenceLifecycle:
    """Tests for sequence lifecycle management."""

    def test_start_sequence_returns_id(self, kv_manager, sample_prompt):
        """Test that start_sequence returns a sequence ID."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        assert isinstance(seq_id, int)
        assert seq_id > 0

    def test_start_sequence_increments_id(self, kv_manager, sample_prompt):
        """Test that sequence IDs increment."""
        id1 = kv_manager.start_sequence(sample_prompt)
        id2 = kv_manager.start_sequence(sample_prompt)
        assert id2 > id1

    def test_start_sequence_allocates_blocks(self, kv_manager, sample_prompt):
        """Test that starting a sequence allocates blocks."""
        seq_id = kv_manager.start_sequence(sample_prompt, max_new_tokens=100)
        info = kv_manager.get_sequence_info(seq_id)
        assert len(info.kv_blocks) > 0

    def test_start_sequence_records_prompt_length(self, kv_manager, sample_prompt):
        """Test that prompt length is recorded."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        info = kv_manager.get_sequence_info(seq_id)
        assert info.prompt_length == len(sample_prompt)
        assert info.current_length == len(sample_prompt)

    def test_end_sequence_removes(self, kv_manager, sample_prompt):
        """Test that end_sequence removes the sequence."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        assert seq_id in kv_manager
        kv_manager.end_sequence(seq_id)
        assert seq_id not in kv_manager

    def test_end_sequence_frees_blocks(self, kv_manager, sample_prompt):
        """Test that ending a sequence frees blocks."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        initial_blocks = len(kv_manager._allocated_blocks)

        kv_manager.end_sequence(seq_id)

        assert len(kv_manager._allocated_blocks) < initial_blocks

    def test_end_unknown_sequence_warns(self, kv_manager):
        """Test that ending unknown sequence is handled gracefully."""
        # Should not raise, just log warning
        kv_manager.end_sequence(99999)

    def test_append_token_updates_length(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test that append_token updates sequence length."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        initial_length = kv_manager.get_sequence_info(seq_id).current_length

        key, value = sample_kv_vectors
        kv_manager.append_token(seq_id, token_id=100, key=key, value=value, layer=0)

        new_length = kv_manager.get_sequence_info(seq_id).current_length
        assert new_length == initial_length + 1

    def test_append_token_records_token(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test that append_token records the token."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        kv_manager.append_token(seq_id, token_id=42, key=key, value=value, layer=0)

        info = kv_manager.get_sequence_info(seq_id)
        assert 42 in info.generated_tokens


# -----------------------------------------------------------------------------
# Category 3: KV Write/Read Tests
# -----------------------------------------------------------------------------


class TestKVWriteRead:
    """Tests for KV write and read operations."""

    def test_write_kv_stores_data(self, kv_manager, sample_prompt, sample_kv_vectors):
        """Test that write_kv stores data."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        kv_manager.write_kv(seq_id, position=0, key=key, value=value, layer=0)

        # Verify data is stored
        stored_key, stored_value = kv_manager.read_kv(seq_id, position=0, layer=0)
        np.testing.assert_array_almost_equal(key, stored_key)
        np.testing.assert_array_almost_equal(value, stored_value)

    def test_write_kv_unknown_sequence_raises(self, kv_manager, sample_kv_vectors):
        """Test that write_kv to unknown sequence raises."""
        key, value = sample_kv_vectors
        with pytest.raises(ValueError, match="Unknown sequence"):
            kv_manager.write_kv(99999, position=0, key=key, value=value, layer=0)

    def test_write_kv_invalid_layer_raises(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test that write_kv with invalid layer raises."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        with pytest.raises(ValueError, match="Invalid layer"):
            kv_manager.write_kv(seq_id, position=0, key=key, value=value, layer=999)

    def test_read_kv_unknown_sequence_raises(self, kv_manager, sample_prompt):
        """Test that read_kv from unknown sequence raises."""
        with pytest.raises(ValueError, match="Unknown sequence"):
            kv_manager.read_kv(99999, position=0, layer=0)

    def test_read_kv_missing_entry_raises(self, kv_manager, sample_prompt):
        """Test that read_kv from missing entry raises."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        # Don't write, just read
        with pytest.raises(KeyError):
            kv_manager.read_kv(seq_id, position=0, layer=0)

    def test_write_kv_multiple_layers(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test writing KV to multiple layers."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        for layer in range(kv_manager.config.num_hidden_layers):
            kv_manager.write_kv(
                seq_id, position=layer, key=key, value=value, layer=layer
            )

        # Verify all layers
        for layer in range(kv_manager.config.num_hidden_layers):
            stored_key, stored_value = kv_manager.read_kv(
                seq_id, position=layer, layer=layer
            )
            np.testing.assert_array_almost_equal(key, stored_key)


# -----------------------------------------------------------------------------
# Category 4: Context Reading Tests
# -----------------------------------------------------------------------------


class TestContextReading:
    """Tests for KV context reading."""

    def test_read_kv_context_returns_arrays(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test that read_kv_context returns arrays."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        # Write some context
        for i in range(5):
            kv_manager.write_kv(seq_id, position=i, key=key, value=value, layer=0)

        # Update position
        kv_manager.sequences[seq_id].current_length = 5

        keys, values = kv_manager.read_kv_context(seq_id, context_length=5, layer=0)

        assert isinstance(keys, np.ndarray)
        assert isinstance(values, np.ndarray)
        assert keys.shape[0] == 5

    def test_read_kv_context_shape(self, kv_manager, sample_prompt, sample_kv_vectors):
        """Test that read_kv_context returns correct shape."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        key, value = sample_kv_vectors

        for i in range(10):
            kv_manager.write_kv(seq_id, position=i, key=key, value=value, layer=0)

        kv_manager.sequences[seq_id].current_length = 10

        keys, values = kv_manager.read_kv_context(seq_id, context_length=10, layer=0)

        expected_shape = (
            10,
            kv_manager.config.num_attention_heads,
            kv_manager.config.head_dim,
        )
        assert keys.shape == expected_shape
        assert values.shape == expected_shape

    def test_read_kv_context_empty_raises(self, kv_manager, sample_prompt):
        """Test that read_kv_context with empty context raises."""
        seq_id = kv_manager.start_sequence(sample_prompt)

        with pytest.raises(ValueError, match="context_length must be positive"):
            kv_manager.read_kv_context(seq_id, context_length=0, layer=0)


# -----------------------------------------------------------------------------
# Category 5: Block Management Tests
# -----------------------------------------------------------------------------


class TestBlockManagement:
    """Tests for block allocation and management."""

    def test_calculate_blocks_needed(self, kv_manager):
        """Test block calculation."""
        # With block_size=16
        assert kv_manager._calculate_blocks_needed(1) == 1
        assert kv_manager._calculate_blocks_needed(16) == 1
        assert kv_manager._calculate_blocks_needed(17) == 2
        assert kv_manager._calculate_blocks_needed(32) == 2

    def test_allocate_blocks_returns_list(self, kv_manager):
        """Test that allocate_blocks returns a list."""
        blocks = kv_manager._allocate_blocks(5)
        assert isinstance(blocks, list)
        assert len(blocks) == 5

    def test_allocate_blocks_unique_ids(self, kv_manager):
        """Test that allocated block IDs are unique."""
        blocks1 = kv_manager._allocate_blocks(3)
        blocks2 = kv_manager._allocate_blocks(3)

        # All IDs should be unique
        all_blocks = blocks1 + blocks2
        assert len(all_blocks) == len(set(all_blocks))

    def test_free_block_removes_allocation(self, kv_manager):
        """Test that freeing a block removes it."""
        blocks = kv_manager._allocate_blocks(2)
        initial_count = len(kv_manager._allocated_blocks)

        kv_manager._free_block(blocks[0])

        assert len(kv_manager._allocated_blocks) == initial_count - 1

    def test_max_sequences_reached_raises(self, kv_manager, sample_prompt):
        """Test that exceeding max_sequences raises."""
        # Start max_sequences sequences
        for _ in range(kv_manager.max_sequences):
            kv_manager.start_sequence(sample_prompt)

        # Next one should raise
        with pytest.raises(RuntimeError, match="Maximum sequences"):
            kv_manager.start_sequence(sample_prompt)


# -----------------------------------------------------------------------------
# Category 6: Statistics Tests
# -----------------------------------------------------------------------------


class TestStatistics:
    """Tests for cache statistics."""

    def test_get_stats_returns_dict(self, kv_manager, sample_prompt):
        """Test that get_stats returns a dictionary."""
        kv_manager.start_sequence(sample_prompt)
        stats = kv_manager.get_stats()

        assert isinstance(stats, dict)
        assert "active_sequences" in stats
        assert "allocated_blocks" in stats

    def test_get_stats_active_sequences(self, kv_manager, sample_prompt):
        """Test that stats track active sequences."""
        assert kv_manager.get_stats()["active_sequences"] == 0

        kv_manager.start_sequence(sample_prompt)
        assert kv_manager.get_stats()["active_sequences"] == 1

        kv_manager.start_sequence(sample_prompt)
        assert kv_manager.get_stats()["active_sequences"] == 2

    def test_get_stats_peak_blocks(self, kv_manager, sample_prompt):
        """Test that stats track peak blocks."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        peak_before = kv_manager.get_stats()["peak_blocks"]

        kv_manager.end_sequence(seq_id)
        peak_after = kv_manager.get_stats()["peak_blocks"]

        # Peak should remain the same
        assert peak_after >= peak_before


# -----------------------------------------------------------------------------
# Category 7: Multi-Sequence Tests
# -----------------------------------------------------------------------------


class TestMultiSequence:
    """Tests for multi-sequence management."""

    def test_multiple_sequences_independent(
        self, kv_manager, sample_prompt, sample_kv_vectors
    ):
        """Test that multiple sequences are independent."""
        id1 = kv_manager.start_sequence(sample_prompt)
        id2 = kv_manager.start_sequence([100, 200, 300])

        key1, value1 = sample_kv_vectors
        key2 = np.ones_like(sample_kv_vectors[0])
        value2 = np.zeros_like(sample_kv_vectors[1])

        # Write different data to each sequence
        kv_manager.write_kv(id1, position=0, key=key1, value=value1, layer=0)
        kv_manager.write_kv(id2, position=0, key=key2, value=value2, layer=0)

        # Verify independence
        stored_key1, _ = kv_manager.read_kv(id1, position=0, layer=0)
        stored_key2, _ = kv_manager.read_kv(id2, position=0, layer=0)

        np.testing.assert_array_almost_equal(key1, stored_key1)
        np.testing.assert_array_almost_equal(key2, stored_key2)

    def test_get_all_sequences(self, kv_manager, sample_prompt):
        """Test getting all active sequences."""
        ids = []
        for _ in range(3):
            ids.append(kv_manager.start_sequence(sample_prompt))

        active = kv_manager.get_all_sequences()
        assert set(active) == set(ids)

    def test_sequence_info(self, kv_manager, sample_prompt):
        """Test getting sequence info."""
        seq_id = kv_manager.start_sequence(sample_prompt, max_new_tokens=50)
        info = kv_manager.get_sequence_info(seq_id)

        assert isinstance(info, SequenceInfo)
        assert info.sequence_id == seq_id
        assert info.prompt_length == len(sample_prompt)


# -----------------------------------------------------------------------------
# Category 8: Edge Case Tests
# -----------------------------------------------------------------------------


class TestEdgeCases:
    """Tests for edge cases."""

    def test_clear_removes_all(self, kv_manager, sample_prompt):
        """Test that clear removes all sequences."""
        for _ in range(3):
            kv_manager.start_sequence(sample_prompt)

        kv_manager.clear()

        assert len(kv_manager) == 0
        assert len(kv_manager._allocated_blocks) == 0

    def test_len_returns_count(self, kv_manager, sample_prompt):
        """Test that len returns sequence count."""
        assert len(kv_manager) == 0

        kv_manager.start_sequence(sample_prompt)
        assert len(kv_manager) == 1

        kv_manager.start_sequence(sample_prompt)
        assert len(kv_manager) == 2

    def test_contains_check(self, kv_manager, sample_prompt):
        """Test membership check."""
        seq_id = kv_manager.start_sequence(sample_prompt)

        assert seq_id in kv_manager
        assert 99999 not in kv_manager

    def test_repr(self, kv_manager, sample_prompt):
        """Test string representation."""
        kv_manager.start_sequence(sample_prompt)
        repr_str = repr(kv_manager)

        assert "KVCacheManager" in repr_str
        assert "sequences=" in repr_str

    def test_sequence_info_str(self, kv_manager, sample_prompt):
        """Test SequenceInfo string representation."""
        seq_id = kv_manager.start_sequence(sample_prompt)
        info = kv_manager.get_sequence_info(seq_id)
        info_str = str(info)

        assert "SequenceInfo" in info_str
        assert str(seq_id) in info_str

    def test_update_timestamp(self, kv_manager, sample_prompt):
        """Test that append_token updates timestamp."""
        import time

        seq_id = kv_manager.start_sequence(sample_prompt)
        info = kv_manager.get_sequence_info(seq_id)
        ts_before = info.updated_at

        time.sleep(0.01)  # Small delay

        key, value = np.zeros(10), np.zeros(10)
        kv_manager.append_token(seq_id, 42, key, value, layer=0)

        info = kv_manager.get_sequence_info(seq_id)
        assert info.updated_at > ts_before


# -----------------------------------------------------------------------------
# Category 9: SequenceInfo Tests
# -----------------------------------------------------------------------------


class TestSequenceInfo:
    """Tests for SequenceInfo dataclass."""

    def test_num_generated(self):
        """Test num_generated property."""
        info = SequenceInfo(sequence_id=1, generated_tokens=[1, 2, 3, 4, 5])
        assert info.num_generated == 5

    def test_total_blocks(self):
        """Test total_blocks property."""
        info = SequenceInfo(sequence_id=1, kv_blocks=[0, 1, 2, 3])
        assert info.total_blocks == 4

    def test_default_values(self):
        """Test default values."""
        info = SequenceInfo(sequence_id=1)
        assert info.current_length == 0
        assert info.prompt_length == 0
        assert len(info.generated_tokens) == 0
        assert info.is_complete is False


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
