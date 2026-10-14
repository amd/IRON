# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Runner.from_options``: the CLI's own parsing (``add_arguments``'s
flags, ``FLAGS`` among them) and a test's option strings give the same
runner state as constructing one directly, for both ``--random-weights``
and a real tokenizer (skipped without the real checkpoint's). No NPU; the
checkpoint is synthetic, of ``SMALL``'s shape, a concrete ``Config``
instance so no config.json is read.
"""

import argparse

import numpy as np
import pytest

from iron.applications.llama.model import Llama, SPECIAL_TOKENS, tokenizer
from iron.lm import Runner as BaseRunner
from iron.lm.base import FLAGS
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
    assert got.tokenizer.encode("hello") == want.tokenizer.encode("hello")


def test_from_options_refuses_both_a_tokenizer_and_random_weights():
    path = checkpoint(SMALL).path
    with pytest.raises(SystemExit):
        SmallRunner.from_options([str(path), str(path), "--random-weights", "1"])


def test_from_options_refuses_neither():
    path = checkpoint(SMALL).path
    with pytest.raises(SystemExit):
        SmallRunner.from_options([str(path)])
