# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Config.from_checkpoint``: the dotted-path lookup and ``convert`` hooks
against a real ``config.json`` (device-free), and that Llama's and
EmbeddingGemma 2's own give today's hand-written values.
"""

import dataclasses
from pathlib import Path

import pytest

from iron.applications import llama
from iron.applications.embedding_gemma2.config import (
    AudioConfig,
    Config as EmbeddingGemmaConfig,
    VisionConfig,
)
from iron.applications.embedding_gemma2 import model as embedding_gemma2_model
from iron.applications.llama.model import Llama3RopeScaling, LlamaConfig, Runner
from iron.lm import Config, DecoderConfig

LLAMA_CONFIG_JSON = Path(llama.__file__).with_name("config.json")
EMBEDDING_GEMMA2_CONFIG_JSON = Path(embedding_gemma2_model.__file__).with_name(
    "config.json"
)


def test_llama_1b_from_checkpoint_is_runners_config():
    """``Runner.config`` is built from the checkpoint's ``config.json``;
    rebuilding it gives the same instance.
    """
    assert LlamaConfig.from_checkpoint(LLAMA_CONFIG_JSON) == Runner.config


def test_llama_1b_values_are_todays_hand_written_ones():
    c = Runner.config
    assert (c.vocab_size, c.emb_dim, c.n_layers) == (128256, 2048, 16)
    assert (c.n_heads, c.n_kv_groups, c.head_dim) == (32, 8, 64)
    assert (c.hidden_dim, c.max_seq_len, c.rope_base) == (8192, 32768, 500000.0)
    assert c.eps == 1e-5
    assert c.rope_scaling == Llama3RopeScaling(
        factor=32.0,
        low_freq_factor=1.0,
        high_freq_factor=4.0,
        original_max_position_embeddings=8192,
    )


def test_from_checkpoint_takes_either_the_file_or_its_directory():
    assert LlamaConfig.from_checkpoint(
        LLAMA_CONFIG_JSON.parent
    ) == LlamaConfig.from_checkpoint(LLAMA_CONFIG_JSON)


def test_from_checkpoint_leaves_an_unnamed_field_at_its_default():
    # prefill_chunk names no config.json key: an IRON choice.
    assert LlamaConfig.from_checkpoint(LLAMA_CONFIG_JSON).prefill_chunk == 2048


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
    assert cls.from_checkpoint(EMBEDDING_GEMMA2_CONFIG_JSON) == instance


def test_embedding_gemma2_global_layers_are_the_checkpoints_full_attention_ones():
    config = EmbeddingGemmaConfig.from_checkpoint(EMBEDDING_GEMMA2_CONFIG_JSON)
    assert config.global_layers == (5, 11, 17, 23)


def test_decoder_config_adds_the_decoder_fields_to_configs_eps():
    base_fields = {f.name for f in dataclasses.fields(Config)}
    decoder_fields = {f.name for f in dataclasses.fields(DecoderConfig)}
    assert base_fields == {"eps"}
    assert {"vocab_size", "max_seq_len", "rope_scaling"} <= decoder_fields - base_fields
