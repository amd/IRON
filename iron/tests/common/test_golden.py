# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Golden``: what it records, when, and the file it refuses."""

import dataclasses

import numpy as np
import pytest

from iron.lm.golden import RECORD, Golden, HuggingFace, fingerprint
from iron.tests.support.llama_model import SMALL, checkpoint
from iron.tests.support.llama_reference import OnHost

TOKENS = np.arange(4)
TOY = dataclasses.replace(SMALL, num_hidden_layers=1)


def model(seed):
    return OnHost(TOY, checkpoint(TOY).tree("random", seed))


def test_it_records_only_while_asked_and_reads_back_without_the_reference(
    tmp_path, monkeypatch
):
    path = tmp_path / "golden.npz"
    expected = np.array(model(2).logits(TOKENS), np.float32)
    monkeypatch.delenv(RECORD, raising=False)
    with pytest.raises(FileNotFoundError, match=f"{path} is missing"):
        Golden(path, lambda: model(2), (TOY, 2)).logits(TOKENS)
    monkeypatch.setenv(RECORD, "1")
    np.testing.assert_array_equal(
        Golden(path, lambda: model(2), (TOY, 2)).logits(TOKENS), expected
    )
    assert [p.name for p in tmp_path.iterdir()] == ["golden.npz"]
    monkeypatch.delenv(RECORD)
    np.testing.assert_array_equal(Golden(path, None, (TOY, 2)).logits(TOKENS), expected)
    with pytest.raises(LookupError, match="holds no logits"):
        Golden(path, None, (TOY, 2)).logits(TOKENS + 1)


def test_a_file_of_other_inputs_is_refused_and_rerecorded(tmp_path, monkeypatch):
    path = tmp_path / "golden.npz"
    monkeypatch.setenv(RECORD, "1")
    Golden(path, lambda: model(2), (TOY, 2)).logits(TOKENS)
    Golden(path, lambda: model(2), (TOY, 2)).logits(TOKENS + 1)
    monkeypatch.delenv(RECORD)
    with pytest.raises(ValueError, match="other inputs"):
        Golden(path, lambda: model(3), (TOY, 3))
    monkeypatch.setenv(RECORD, "1")
    golden = Golden(path, lambda: model(3), (TOY, 3))
    np.testing.assert_array_equal(
        golden.logits(TOKENS), np.array(model(3).logits(TOKENS), np.float32)
    )
    assert len(Golden(path, None, (TOY, 3)).rows) == 1


def test_a_weight_the_model_does_not_hold_is_refused():
    pytest.importorskip("transformers")
    weights = checkpoint(SMALL).tree("random")
    weights.model.extra = np.zeros(1, np.float32)
    with pytest.raises(ValueError, match=r"hold \['model.extra'\]"):
        HuggingFace.build("llama", SMALL, weights)


def test_a_field_added_at_its_default_keeps_the_fingerprint():
    @dataclasses.dataclass(frozen=True)
    class Before:
        width: int
        eps: float = 1e-5

    @dataclasses.dataclass(frozen=True)
    class After(Before):
        window: int | None = None

    After.__name__ = "Before"
    assert fingerprint(After(8)) == fingerprint(Before(8))
    assert fingerprint(After(8, window=4)) != fingerprint(Before(8))
    assert fingerprint(Before(8, eps=1e-6)) != fingerprint(Before(8))
