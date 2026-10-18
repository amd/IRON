# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Model.load`` up to the device: ``main()``'s command line handing its
path and flags to ``from_checkpoint``, its ``-v``, the model
``from_checkpoint`` builds with drawn weights or a real tokenizer (skipped
without the real checkpoint's), the context ``fit`` chooses, the BOS, and the golden
beside a checkpoint. No NPU (the fit tests trace under a bound npu2, as
Llama's profile is per device); the checkpoint is synthetic, of
``SMALL``'s shape, a concrete ``Config`` instance so no config.json is
read.
"""

import argparse
import dataclasses
import logging
import shutil
import struct
import sys

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.llama.model import Llama
from iron.lm import Checkpoint, Model, main
from iron.lm.cli import parse_args
from iron.lm.golden import RECORD
from iron.lm.testing import require, weights_dir
from iron.tests.common.llama_model import SMALL, checkpoint

TOKENIZER = weights_dir("llama3.2-1b") / "tokenizer.json"


class Small(Llama):
    """Llama at ``SMALL``'s shape: a concrete ``Config``, not a class, so
    ``default_config`` returns it unchanged and reads no checkpoint.
    """

    config = SMALL
    bos = 1


def _directory(path, config=SMALL):
    """``path``, holding ``config``'s checkpoint as ``model.safetensors``."""
    (path / "model.safetensors").symlink_to(checkpoint(config).path)
    return path


def test_main_takes_the_path_and_flags_load_takes(monkeypatch):
    """The command line's positional argument is ``load``'s path, and its
    ``--random-weights``/``--max-seq-len`` its ``seed``/``max_seq_len``.
    """
    given = {}

    def from_checkpoint(cls, path, **kwargs):
        given.update(path=path, **kwargs)
        raise SystemExit

    monkeypatch.setattr(Small, "from_checkpoint", classmethod(from_checkpoint))
    argv = ["model", "org/repo", "--random-weights", "7", "--max-seq-len", "64"]
    monkeypatch.setattr(sys, "argv", argv)
    with pytest.raises(SystemExit):
        main(Small)
    assert given == dict(path="org/repo", seed=7, max_seq_len=64)


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


def test_from_checkpoint_draws_its_weights_at_a_seed(tmp_path):
    directory = _directory(tmp_path)
    model = Small.from_checkpoint(directory, seed=7)
    assert model.config == SMALL
    assert model.seed == 7
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
    assert model.seed is None
    want = [model.bos, *Model.open_tokenizer(TOKENIZER).encode("hello")]
    assert model.tokenizer("hello") == want


def test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it(tmp_path):
    directory = _directory(tmp_path)
    lowered = Small.from_checkpoint(directory, seed=1, max_seq_len=128)
    assert lowered.config.max_seq_len == 128
    with pytest.raises(ValueError, match="past the model's 256"):
        Small.from_checkpoint(directory, seed=1, max_seq_len=512)


def _held(config, length: int) -> int:
    """What the model holds at ``length`` positions: its arena, traced."""
    config = dataclasses.replace(config, max_seq_len=length)
    model = Llama(config, checkpoint(config).tree("unread"))
    model.profile = None
    return sum(model.trace(**model.shapes()[0]).pinned.values())


def test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks(npu2):
    """1024 native positions in 256-row chunks: a budget one byte short of
    a context takes the next shorter whole chunks.
    """
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    path = checkpoint(config).path
    assert Small.fit(config, path, budget=_held(config, 1024)) == config
    short = Small.fit(config, path, budget=_held(config, 1024) - 1)
    assert short.max_seq_len == 768
    assert Small.fit(config, path, budget=_held(config, 512)).max_seq_len == 512
    with pytest.raises(ValueError, match="do not fit"):
        Small.fit(config, path, budget=_held(config, 256) - 1)


def test_a_model_fits_its_context_with_no_device_bound(tmp_path):
    """``fit`` traces the model, whose profile is per device; it measures
    what the model holds, which needs none.
    """

    class Native(Small):
        config = dataclasses.replace(SMALL, max_seq_len=1024)

    directory = _directory(tmp_path, Native.config)
    with aie_utils.set_current_device(None):
        assert Native.from_checkpoint(directory, seed=1).config == Native.config


def test_fit_says_what_it_chose_and_how_to_ask_for_more(caplog):
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    path = checkpoint(config).path
    with caplog.at_level(logging.INFO, logger="iron.lm.model"):
        Small.fit(config, path, budget=_held(config, 1024))
        Small.fit(config, path, budget=_held(config, 512))
    native, short = caplog.records
    assert native.levelno == logging.INFO and "native context" in native.message
    assert short.levelno == logging.WARNING
    assert "max_seq_len 512, not the native 1024" in short.message
    assert "--max-seq-len asks for up to 1024" in short.message


def test_a_model_s_bos_is_its_checkpoint_s_unless_it_names_one(tmp_path):
    """The checkpoint's ``config.json``'s, else its
    ``generation_config.json``'s.
    """

    class FromCheckpoint(Small):
        bos = Model.bos

    directory = _directory(tmp_path)
    (directory / "config.json").write_text('{"bos_token_id": 7}')
    assert FromCheckpoint.from_checkpoint(directory, seed=1).bos == 7
    (directory / "config.json").write_text("{}")
    (directory / "generation_config.json").write_text('{"bos_token_id": 8}')
    assert FromCheckpoint.from_checkpoint(directory, seed=1).bos == 8
    (directory / "generation_config.json").unlink()
    with pytest.raises(KeyError, match="names no bos_token_id"):
        FromCheckpoint.from_checkpoint(directory, seed=1).bos
    bos = Small.from_checkpoint(directory, seed=1).bos
    assert bos == 1


def _golden(path):
    """The golden beside the checkpoint at ``path`` (``cpu_reference``)."""
    model = Small(SMALL, Checkpoint(path).tree("unread"))
    model.checkpoint = Checkpoint(path)
    return model.cpu_reference()


@pytest.mark.parametrize("change", ["config", "first weight", "last weight"])
def test_a_checkpoint_s_golden_is_refused_once_it_changes(
    tmp_path, monkeypatch, change
):
    """A fine-tune keeps every name and shape: the bytes at either end of a
    tensor tell it from its base.
    """
    monkeypatch.delenv(RECORD, raising=False)
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
