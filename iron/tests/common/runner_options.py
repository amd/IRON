# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Runner.from_options``: the CLI's own parsing (``add_arguments``'s
flags, ``FLAGS`` among them) and a test's option strings give the same
runner state as constructing one directly, for both ``--random-weights``
and a real tokenizer (skipped without the real checkpoint's). No NPU (the
fit tests trace under a bound npu2, as Llama's profile is per device); the
checkpoint is synthetic, of ``SMALL``'s shape, a concrete ``Config``
instance so no config.json is read.
"""

import argparse
import dataclasses
import logging
import shutil
import struct

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.llama.model import Llama, SPECIAL_TOKENS, tokenizer
from iron.lm import Runner as BaseRunner
from iron.lm.base import FLAGS
from iron.lm.golden import RECORD
from iron.lm.testing import require, weights_dir
from iron.tests.common.llama_model import SMALL, checkpoint

TOKENIZER = weights_dir("llama3.2-1b") / "tokenizer.model"


class SmallRunner(BaseRunner):
    """A runner of ``SMALL``'s shape: a concrete ``Config``, not a class, so
    ``default_config`` returns it unchanged and reads no checkpoint.
    """

    config = SMALL
    model = Llama
    open_tokenizer = staticmethod(tokenizer)
    bos = SPECIAL_TOKENS["<|begin_of_text|>"]


def test_add_arguments_reads_flags_the_same_as_conftests_pytest_options():
    """``Runner.add_arguments``'s ``--random-weights``/``--max-seq-len`` are
    ``FLAGS``, the same tuple ``conftest.py``'s ``pytest_addoption`` reads.
    """
    parser = argparse.ArgumentParser()
    SmallRunner.add_arguments(parser)
    args = parser.parse_args(["weights.safetensors", "--random-weights", "7"])
    assert args.random_weights == 7 and args.tokenizer_path is None
    args = parser.parse_args(
        ["weights.safetensors", "tok.model", "--max-seq-len", "64"]
    )
    assert args.max_seq_len == 64 and args.random_weights is None
    assert {f[0] for f, _ in FLAGS} == {"--random-weights", "--max-seq-len"}


def test_from_options_with_random_weights_matches_direct_construction():
    path = checkpoint(SMALL).path
    want = SmallRunner(path, seed=7)
    got = SmallRunner.from_options([str(path), "--random-weights", "7"])
    assert got.config == want.config == SMALL
    assert got.seed == want.seed == 7
    assert got.tokenizer is want.tokenizer is None
    np.testing.assert_array_equal(
        got.weights.model.embed_tokens.weight, want.weights.model.embed_tokens.weight
    )


def test_from_options_with_a_tokenizer_matches_direct_construction():
    require(TOKENIZER)
    path = checkpoint(SMALL).path
    want = SmallRunner(path, TOKENIZER)
    got = SmallRunner.from_options([str(path), str(TOKENIZER)])
    assert got.config == want.config == SMALL
    assert got.seed is want.seed is None
    assert got.tokenizer("hello") == want.tokenizer("hello")


def test_from_options_refuses_both_a_tokenizer_and_random_weights():
    path = checkpoint(SMALL).path
    with pytest.raises(SystemExit):
        SmallRunner.from_options([str(path), str(path), "--random-weights", "1"])


def test_from_options_refuses_neither():
    path = checkpoint(SMALL).path
    with pytest.raises(SystemExit):
        SmallRunner.from_options([str(path)])


def test_from_options_lowers_the_context_and_refuses_to_raise_it():
    path = checkpoint(SMALL).path
    lowered = SmallRunner.from_options(
        [str(path), "--random-weights", "1", "--max-seq-len", "128"]
    )
    assert lowered.config.max_seq_len == 128
    with pytest.raises(SystemExit):
        SmallRunner.from_options(
            [str(path), "--random-weights", "1", "--max-seq-len", "512"]
        )


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
    assert SmallRunner.fit(config, path, budget=_held(config, 1024)) == config
    short = SmallRunner.fit(config, path, budget=_held(config, 1024) - 1)
    assert short.max_seq_len == 768
    assert SmallRunner.fit(config, path, budget=_held(config, 512)).max_seq_len == 512
    with pytest.raises(ValueError, match="do not fit"):
        SmallRunner.fit(config, path, budget=_held(config, 256) - 1)


def test_a_runner_fits_its_context_with_no_device_bound():
    """``fit`` traces the model, whose profile is per device; it measures
    what the model holds, which needs none.
    """

    class Native(SmallRunner):
        config = dataclasses.replace(SMALL, max_seq_len=1024)

    with aie_utils.set_current_device(None):
        assert Native(checkpoint(Native.config).path, seed=1).config == Native.config


def test_fit_says_what_it_chose_and_how_to_ask_for_more(caplog):
    config = dataclasses.replace(SMALL, max_seq_len=1024)
    path = checkpoint(config).path
    with caplog.at_level(logging.INFO, logger="iron.lm.base"):
        SmallRunner.fit(config, path, budget=_held(config, 1024))
        SmallRunner.fit(config, path, budget=_held(config, 512))
    native, short = caplog.records
    assert native.levelno == logging.INFO and "native context" in native.message
    assert short.levelno == logging.WARNING
    assert "max_seq_len 512, not the native 1024" in short.message
    assert "--max-seq-len asks for up to 1024" in short.message


def test_a_runner_s_bos_is_its_checkpoint_s_unless_it_names_one(tmp_path):
    class FromCheckpoint(SmallRunner):
        bos = BaseRunner.bos

    path = tmp_path / "model.safetensors"
    path.symlink_to(checkpoint(SMALL).path)
    (tmp_path / "config.json").write_text('{"bos_token_id": 7}')
    assert FromCheckpoint(path, seed=1).bos == 7
    (tmp_path / "config.json").write_text("{}")
    with pytest.raises(KeyError, match="config.json has no bos_token_id"):
        FromCheckpoint(path, seed=1).bos
    assert SmallRunner(path, seed=1).bos == SPECIAL_TOKENS["<|begin_of_text|>"]


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
    golden = SmallRunner(path).reference()
    golden.rows = {"key": np.zeros(1, np.float32)}
    golden.write()
    assert SmallRunner(path).reference().rows.keys() == {"key"}
    if change == "config":
        (tmp_path / "config.json").write_text('{"bos_token_id": 8}')
    else:
        with open(path, "r+b") as f:
            (length,) = struct.unpack("<Q", f.read(8))
            f.seek(8 + length if change == "first weight" else path.stat().st_size - 1)
            f.write(b"\x01")
    with pytest.raises(ValueError, match="other inputs"):
        SmallRunner(path).reference()
