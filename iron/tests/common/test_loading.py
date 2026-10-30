# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model.load`` up to the device: the command line's ``-v``.

The model ``from_checkpoint`` builds with drawn weights or a real
tokenizer (skipped without the real checkpoint's), the context ``fit``
chooses, and the golden beside a checkpoint. No NPU (the fit tests record
under a bound npu2, as Llama's profile is per device); the checkpoint is
synthetic, of ``SMALL``'s shape, a concrete ``Config`` instance so no
config.json is read.
"""

import argparse
import dataclasses
import logging
import os
import shutil
import struct
import subprocess
import sys

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.llama.model import Llama
from iron.lm import Checkpoint
from iron.lm.cli import parse_args
from iron.lm.golden import RECORD
from iron.lm.model import TokenizerJson
from iron.lm.testing import require, weights_dir
from iron.tests.support.llama_model import SMALL, checkpoint

TOKENIZER = weights_dir("llama3.2-1b") / "tokenizer.json"


class Small(Llama):
    """Llama at ``SMALL``'s shape: a concrete ``Config``, not a class.

    So ``default_config`` returns it unchanged and reads no checkpoint.
    """

    config = SMALL


def _directory(path, config=SMALL):
    """``path``, holding ``config``'s checkpoint as ``model.safetensors``."""
    (path / "model.safetensors").symlink_to(checkpoint(config).path)
    return path


def test_v_shows_iron_s_info_lines(caplog):
    """``-v`` shows a compile's "compiling for" line, an INFO of iron's."""
    iron_logger = logging.getLogger("iron")
    level = iron_logger.level
    try:
        parse_args(argparse.ArgumentParser(), ["-v"])
        logging.getLogger("iron.common.graph.compiled").info("Small: compiling for")
    finally:
        iron_logger.setLevel(level)
    assert "compiling for" in caplog.text


@pytest.mark.parametrize("rounds", [0, 1])
def test_check_determinism_needs_two_rounds_before_any_load(tmp_path, rounds):
    result = subprocess.run(
        [sys.executable, "-m", "iron.applications.llama.model", str(tmp_path)]
        + ["--check-determinism", str(rounds)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 2, result.stderr
    assert "--check-determinism compares rounds: give 2 or more" in result.stderr


def test_from_checkpoint_draws_its_weights_at_a_seed(tmp_path):
    directory = _directory(tmp_path)
    model = Small.from_checkpoint(directory, random_weights=7)
    assert model.config == SMALL
    assert model.random_weights == 7
    assert model.tokenizer is None
    np.testing.assert_array_equal(
        model.weights.model.embed_tokens.weight,
        Checkpoint(directory / "model.safetensors")
        .tree("random", 7)
        .model.embed_tokens.weight,
    )


def test_from_checkpoint_opens_the_tokenizer_beside_it(tmp_path):
    require(TOKENIZER)
    directory = _directory(tmp_path)
    (directory / "tokenizer.json").symlink_to(TOKENIZER)
    model = Small.from_checkpoint(directory)
    assert model.random_weights is None
    begin = TokenizerJson(TOKENIZER).encode("<|begin_of_text|>")
    assert model.tokenizer("hello") == [
        *begin,
        *TokenizerJson(TOKENIZER).encode("hello"),
    ]


# The ids transformers' tokenizer("Hello world") puts before the text's
# (and any after it), read off each checkpoint's AutoTokenizer.
LEADS = [
    ("llama3.2-1b", [128000], []),
    ("gemma-4-e2b-it", [], []),
]


@pytest.mark.parametrize("name, lead, tail", LEADS, ids=[n for n, *_ in LEADS])
def test_a_prompt_begins_as_the_tokenizer_begins_a_text(name, lead, tail):
    """Only the special tokens before the text.

    A BOS where the tokenizer puts one, none where it puts none, nothing
    it puts after.
    """
    path = weights_dir(name) / "tokenizer.json"
    require(path, staged=False)
    encoding = TokenizerJson(path)
    text = encoding.encode("Hello world")
    assert encoding.prompt("Hello world") == [*lead, *text]
    hf = pytest.importorskip("tokenizers").Tokenizer.from_file(str(path))
    assert hf.encode("Hello world").ids == [*lead, *text, *tail]


def test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it(tmp_path):
    directory = _directory(tmp_path)
    lowered = Small.from_checkpoint(directory, random_weights=1, max_seq_len=128)
    assert (lowered.config.max_seq_len, lowered.config.prefill_chunk) == (128, 128)
    with pytest.raises(ValueError, match="past the model's 256"):
        Small.from_checkpoint(directory, random_weights=1, max_seq_len=512)


def _held(config, length: int) -> int:
    """Return what the model holds at ``length`` positions: its arena, recorded."""
    config = dataclasses.replace(config, max_seq_len=length)
    model = Llama(config, checkpoint(config).tree("unread"))
    model.profile = None
    return sum(model.record(**model.shapes()[0]).pinned.values())


def test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks(npu2, caplog):
    """1024 native positions in 256-row chunks.

    A budget one byte short of a context takes the next shorter whole
    chunks, logging what it chose and, short, how to ask for more.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    path = checkpoint(config).path
    assert Small.fit(config, path, budget=_held(config, 512)).max_seq_len == 512
    with pytest.raises(ValueError, match="do not fit"):
        Small.fit(config, path, budget=_held(config, 256) - 1)
    caplog.clear()
    with caplog.at_level(logging.INFO, logger="iron.lm.model"):
        assert Small.fit(config, path, budget=_held(config, 1024)) == config
        short = Small.fit(config, path, budget=_held(config, 1024) - 1)
    assert short.max_seq_len == 768
    native, short_log = caplog.records
    assert native.levelno == logging.INFO and "native context" in native.message
    assert short_log.levelno == logging.WARNING
    assert "max_seq_len 768, not the native 1024" in short_log.message
    assert "--max-seq-len asks for up to 1024" in short_log.message


def test_a_model_fits_its_context_with_no_device_bound(tmp_path):
    """``fit`` records the model, whose profile is per device.

    It measures what the model holds, which needs none.
    """

    class Native(Small):
        config = dataclasses.replace(SMALL, max_seq_len=1024)

    directory = _directory(tmp_path, Native.config)
    with aie_utils.set_current_device(None):
        assert (
            Native.from_checkpoint(directory, random_weights=1).config == Native.config
        )


def _golden(path):
    """Return the golden beside the checkpoint at ``path`` (``cpu_reference``)."""
    model = Small(SMALL, Checkpoint(path).tree("unread"))
    model.checkpoint = Checkpoint(path)
    return model.cpu_reference()


@pytest.mark.parametrize("change", ["config", "first weight", "last weight"])
def test_a_checkpoint_s_golden_is_refused_once_it_changes(tmp_path, change):
    """A fine-tune keeps every name and shape.

    The bytes at either end of a tensor tell it from its base.
    """
    if os.environ.get(RECORD):
        pytest.skip("recording rewrites a changed golden rather than refusing it")
    path = tmp_path / "model.safetensors"
    shutil.copy(checkpoint(SMALL).path, path)
    (tmp_path / "config.json").write_text('{"bos_token_id": 7}')
    golden = _golden(path)
    golden.rows = {"key": np.zeros(1, np.float32)}
    golden.write()
    assert _golden(path).rows.keys() == {"key"}
    if change == "config":
        (tmp_path / "config.json").write_text('{"bos_token_id": 8}')
    else:
        with open(path, "r+b") as f:
            (length,) = struct.unpack("<Q", f.read(8))
            f.seek(8 + length if change == "first weight" else path.stat().st_size - 1)
            f.write(b"\x01")
    with pytest.raises(ValueError, match="other inputs"):
        _golden(path)
