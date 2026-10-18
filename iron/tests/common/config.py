# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Config.from_checkpoint``: the dotted-path lookup and ``convert`` hooks
against a real checkpoint's own ``config.json`` (device-free; skipped
outside CI where the checkpoint is not there, failed in CI), and that
``DecoderConfig`` adds the decoder-only fields to ``Config``'s ``eps``.
"""

import dataclasses
import json

import pytest

from iron.applications.embedding_gemma2.config import (
    AudioConfig,
    Config as EmbeddingGemmaConfig,
    VisionConfig,
)
from iron.applications.llama.model import Llama3RopeScaling, LlamaConfig
from iron.lm import Config, DecoderConfig
from iron.lm.testing import require, weights_dir

LLAMA_DIR = weights_dir("llama3.2-1b")
EMBEDDING_GEMMA2_DIR = weights_dir("embeddinggemma-2")


def test_llama_1b_from_checkpoint_is_its_published_shape():
    require(LLAMA_DIR / "config.json")
    c = LlamaConfig.from_checkpoint(LLAMA_DIR)
    assert (c.vocab_size, c.hidden_size, c.num_hidden_layers) == (128256, 2048, 16)
    assert (c.num_attention_heads, c.num_key_value_heads, c.head_dim) == (32, 8, 64)
    assert (c.intermediate_size, c.rope_theta) == (8192, 500000.0)
    assert c.eps == 1e-5
    assert c.max_seq_len == 131072
    assert c.rope_scaling == Llama3RopeScaling(
        factor=32.0,
        low_freq_factor=1.0,
        high_freq_factor=4.0,
        original_max_position_embeddings=8192,
    )


def test_from_checkpoint_takes_either_the_file_or_its_directory():
    require(LLAMA_DIR / "config.json")
    assert LlamaConfig.from_checkpoint(LLAMA_DIR) == LlamaConfig.from_checkpoint(
        LLAMA_DIR / "config.json"
    )


def test_from_checkpoint_leaves_an_unnamed_field_at_its_default():
    require(LLAMA_DIR / "config.json")
    # prefill_chunk names no config.json key: an IRON choice.
    assert LlamaConfig.from_checkpoint(LLAMA_DIR).prefill_chunk == 2048


def test_from_checkpoint_reads_null_as_the_fields_default(tmp_path):
    """SmolLM2's config.json writes rope_scaling null: no scaling."""
    fields = dict(
        vocab_size=32,
        hidden_size=64,
        num_hidden_layers=1,
        num_attention_heads=2,
        num_key_value_heads=2,
        intermediate_size=128,
        rope_theta=130000.0,
        max_position_embeddings=8192,
        rope_scaling=None,
    )
    (tmp_path / "config.json").write_text(json.dumps(fields))
    assert LlamaConfig.from_checkpoint(tmp_path).rope_scaling is None


def test_from_checkpoint_raises_with_no_config_json_beside_the_path(tmp_path):
    with pytest.raises(FileNotFoundError):
        LlamaConfig.from_checkpoint(tmp_path / "model.safetensors")


@pytest.mark.parametrize(
    "cls,instance",
    [
        (EmbeddingGemmaConfig, EmbeddingGemmaConfig()),
        (AudioConfig, AudioConfig()),
        (VisionConfig, VisionConfig()),
    ],
)
def test_embedding_gemma2_from_checkpoint_is_the_default_instance(cls, instance):
    """Every field ``config.json`` names (a dotted path, a nested sub-config
    or a top-level token id) gives today's hand-written default; a field it
    does not name (an audio or vision front end's own choice) keeps it too.
    """
    require(EMBEDDING_GEMMA2_DIR / "config.json")
    assert cls.from_checkpoint(EMBEDDING_GEMMA2_DIR) == instance


def test_embedding_gemma2_global_layers_are_the_checkpoints_full_attention_ones():
    require(EMBEDDING_GEMMA2_DIR / "config.json")
    config = EmbeddingGemmaConfig.from_checkpoint(EMBEDDING_GEMMA2_DIR)
    assert config.global_layers == (5, 11, 17, 23)


def test_decoder_config_adds_the_decoder_fields_to_configs_eps():
    base_fields = {f.name for f in dataclasses.fields(Config)}
    decoder_fields = {f.name for f in dataclasses.fields(DecoderConfig)}
    assert base_fields == {"eps"}
    assert {"vocab_size", "max_seq_len", "rope_scaling"} <= decoder_fields - base_fields
