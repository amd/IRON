# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Config.from_checkpoint``: the dotted-path lookup and ``convert`` hooks.

Against a real checkpoint's own ``config.json`` (device-free; skipped
outside CI where the checkpoint is not there, failed in CI).
"""

import dataclasses
import json
import re

import pytest

from iron import Precision
from iron.applications.embedding_gemma2.model import Config as EmbeddingGemmaConfig
from iron.applications.gemma4.audio import AudioConfig
from iron.applications.gemma4.vision import VisionConfig
from iron.applications.granite.model import GraniteConfig
from iron.applications.llama.model import Llama3RopeScaling, LlamaConfig
from iron.lm import DecoderConfig
from iron.lm.testing import require, weights_dir
from iron.tests.support.llama_model import REAL_1B

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


@pytest.mark.parametrize(
    "cls",
    [
        LlamaConfig,
        GraniteConfig,
        EmbeddingGemmaConfig,
        AudioConfig,
        VisionConfig,
    ],
    ids=lambda cls: f"{cls.__module__}.{cls.__name__}",
)
def test_from_checkpoint_reads_each_key_and_no_not_json_field(tmp_path, cls):
    """Check that every field is read at its key (``json_key``), its own name or the path it names.

    Under ``json_prefix`` unless the path starts at the root; one the file
    leaves null (each converted one here) keeps its default; a ``not_json``
    field is neither read nor written, even where the file names it.
    """
    fields = dataclasses.fields(cls)
    keys = {cls.json_key(f) for f in fields}
    data, expected, unread = {}, {}, {}
    for f in fields:
        key = cls.json_key(f)
        if key is None:
            if f.name not in keys:
                unread[f.name] = 7
            continue
        value = None if "convert" in f.metadata else 2
        expected[f.name] = f.default if value is None else value
        *parents, leaf = key.split(".")
        node = data
        for part in parents:
            node = node.setdefault(part, {})
        node[leaf] = value
    (tmp_path / "config.json").write_text(json.dumps(data | unread))
    config = cls.from_checkpoint(tmp_path)
    assert {name: getattr(config, name) for name in expected} == expected
    assert 7 not in [getattr(config, name) for name in unread]
    assert not unread.keys() & config.to_json().keys()


def test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for(tmp_path):
    scaling = {"rope_type": "yarn", "factor": 4.0}
    (tmp_path / "config.json").write_text(
        json.dumps(REAL_1B.to_json() | {"rope_scaling": scaling})
    )
    with pytest.raises(ValueError, match=re.escape(f"rope_scaling {scaling}")):
        LlamaConfig.from_checkpoint(tmp_path)


def test_a_sliding_window_some_layers_take_is_refused():
    """Check that ``use_sliding_window`` (Qwen's, SmolLM3's) windows a per-model choice of layers.

    Set, with a window under the context, it is refused.
    """
    with pytest.raises(ValueError, match="use_sliding_window"):
        dataclasses.replace(REAL_1B, sliding_window=64, use_sliding_window=True)
    assert dataclasses.replace(REAL_1B, sliding_window=64).window == 63
    off = dataclasses.replace(REAL_1B, sliding_window=64, use_sliding_window=False)
    assert off.window is None


def test_head_dim_falls_back_and_max_seq_len_is_the_native_context(tmp_path):
    """Check that no ``head_dim`` (Qwen 2.5, Granite, LFM2, Phi-4-mini-instruct) falls back.

    To ``hidden_size // num_attention_heads``; one given is kept.
    """
    fields = dict(
        vocab_size=32,
        hidden_size=1536,
        num_hidden_layers=1,
        num_attention_heads=12,
        num_key_value_heads=2,
        intermediate_size=64,
        rope_theta=1.0,
        max_position_embeddings=40960,
    )
    path = tmp_path / "config.json"
    path.write_text(json.dumps(fields))
    cfg = LlamaConfig.from_checkpoint(path)
    assert (cfg.head_dim, cfg.max_seq_len) == (1536 // 12, 40960)
    path.write_text(json.dumps(fields | {"head_dim": 64}))
    assert LlamaConfig.from_checkpoint(path).head_dim == 64


def test_llama_projects_at_high_from_3b_s_width_unless_given():
    wide = LlamaConfig.from_json(REAL_1B.to_json() | {"hidden_size": 3072})
    assert REAL_1B.precision is Precision.MEDIUM and wide.precision is Precision.HIGH
    given = dataclasses.replace(wide, precision=Precision.MEDIUM)
    assert given.precision is Precision.MEDIUM


def test_a_config_whose_application_states_no_precision_is_refused():
    """Check that ``precision`` is no file's and has no default: each application states its own."""
    data = REAL_1B.to_json() | {"rope_scaling": None}
    with pytest.raises(ValueError, match="DecoderConfig states no precision"):
        DecoderConfig.from_json(data)
    assert LlamaConfig.from_json(data).precision is Precision.MEDIUM


def test_from_checkpoint_names_the_keys_a_config_json_lacks(tmp_path):
    (tmp_path / "config.json").write_text(json.dumps({"vocab_size": 8}))
    with pytest.raises(ValueError, match="lacks .*'hidden_size'"):
        LlamaConfig.from_checkpoint(tmp_path)


@pytest.mark.parametrize(
    "cls,instance",
    [
        (EmbeddingGemmaConfig, EmbeddingGemmaConfig()),
        (AudioConfig, AudioConfig()),
        (VisionConfig, VisionConfig()),
    ],
)
def test_embedding_gemma2_from_checkpoint_is_the_default_instance(cls, instance):
    """Check that every field ``config.json`` names gives today's hand-written default.

    A dotted path, a nested sub-config or a top-level token id; a field it
    does not name (an audio or vision front end's own choice) keeps it too.
    """
    require(EMBEDDING_GEMMA2_DIR / "config.json")
    assert cls.from_checkpoint(EMBEDDING_GEMMA2_DIR) == instance


@pytest.mark.parametrize(
    "config",
    [REAL_1B, EmbeddingGemmaConfig()],
    ids=["llama", "embedding_gemma2"],
)
def test_to_json_is_from_checkpoint_s_inverse(tmp_path, config):
    """Check that a converted field (a ``rope_scaling``) is written as the checkpoint writes it.

    So the file reads back the same config.
    """
    (tmp_path / "config.json").write_text(json.dumps(config.to_json()))
    assert type(config).from_checkpoint(tmp_path) == config
