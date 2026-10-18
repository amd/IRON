# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Golden``: what it records, when, and the file it refuses."""

from types import SimpleNamespace

import numpy as np
import pytest

from iron.lm.golden import RECORD, Golden, HuggingFace
from iron.tests.common.llama_model import SMALL, checkpoint

TOKENS = np.arange(4)


def reference(scale):
    return lambda: SimpleNamespace(logits=lambda tokens: tokens * scale)


def test_it_records_only_while_asked_and_reads_back_without_the_reference(
    tmp_path, monkeypatch
):
    path = tmp_path / "golden.npz"
    monkeypatch.delenv(RECORD, raising=False)
    with pytest.raises(LookupError):
        Golden(path, reference(2), (2,)).logits(TOKENS)
    monkeypatch.setenv(RECORD, "1")
    np.testing.assert_array_equal(
        Golden(path, reference(2), (2,)).logits(TOKENS), TOKENS * 2
    )
    assert [p.name for p in tmp_path.iterdir()] == ["golden.npz"]
    monkeypatch.delenv(RECORD)
    np.testing.assert_array_equal(Golden(path, None, (2,)).logits(TOKENS), TOKENS * 2)


def test_a_file_of_other_inputs_is_refused_and_rerecorded(tmp_path, monkeypatch):
    path = tmp_path / "golden.npz"
    monkeypatch.setenv(RECORD, "1")
    Golden(path, reference(2), (2,)).logits(TOKENS)
    Golden(path, reference(2), (2,)).logits(TOKENS + 1)
    monkeypatch.delenv(RECORD)
    with pytest.raises(ValueError, match="other inputs"):
        Golden(path, reference(3), (3,))
    monkeypatch.setenv(RECORD, "1")
    golden = Golden(path, reference(3), (3,))
    np.testing.assert_array_equal(golden.logits(TOKENS), TOKENS * 3)
    assert len(Golden(path, None, (3,)).rows) == 1


def test_a_weight_the_model_does_not_hold_is_refused():
    pytest.importorskip("transformers")
    weights = checkpoint(SMALL).tree("random")
    weights.model.extra = np.zeros(1, np.float32)
    with pytest.raises(ValueError, match=r"hold \['model.extra'\]"):
        HuggingFace.build("llama", SMALL, weights)
