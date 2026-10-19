# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.lm.tune``, device-free: the calls a decoder is timed in on the
toy Llama, the model an application name finds, and the command line."""

import dataclasses

import pytest

from iron.applications.embedding_gemma2 import Multimodal
from iron.applications.llama import Llama
from iron.lm import Encoder, Sampler, tune
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint, small

pytestmark = pytest.mark.usefixtures("npu2")

# Four prompt chunks of context.
LONG = dict(max_seq_len=1024)


def test_a_decoder_is_timed_at_halving_contexts_up_to_the_last():
    model = small(**LONG)
    decode, prompt = tune.calls(model, 5, 3, 1024, 3, Sampler(top_k=8))
    assert decode.values == dict(position=5, token=3)
    assert [p.values["position"] for p in decode.points] == [255, 511, 1023]
    assert [p.values["start"] for p in prompt.points] == [0, 256, 768]
    assert [p.values["rope_start"] for p in prompt.points] == [0, 256, 768]
    for call in decode, prompt:
        assert sum(p.weight for p in call.points) == pytest.approx(1)
        [rows] = call.contents.values()
        assert rows.shape[0] == 1024 and rows.any()


def test_an_application_s_model_is_the_one_naming_its_calls():
    assert tune.application_model("llama") is Llama
    assert tune.application_model("embedding_gemma2") is Multimodal
    with pytest.raises(ValueError, match="no application 'nothing'"):
        tune.application_model("nothing")


class Toy(Llama):
    """The toy at ``LONG``."""

    config = dataclasses.replace(SMALL, **LONG)


@pytest.fixture
def toy(tmp_path, monkeypatch):
    """``Toy`` with a profiles directory holding ``PROFILE``, and the calls
    ``main`` tunes.
    """
    tuned = []
    PROFILE.save(tmp_path / "npu2.json")
    monkeypatch.setattr(Toy, "profile", tmp_path)
    monkeypatch.setattr(tune.tune_cli, "tune", lambda *a: tuned.append(a))
    path = checkpoint(Toy.config).path
    return ["--checkpoint", str(path)], tuned


def test_main_tunes_a_decoder_s_calls_on_its_flags(toy):
    argv, tuned = toy
    tune.main("toy", Toy, [*argv, "--context", "512", "--points", "2"])
    [(args, calls, profiles)] = tuned
    assert [len(c.points) for c in calls] == [2, 2] and args.context == 512


@pytest.mark.parametrize(
    "context, refusal",
    [
        (300, "--context 300 is not whole 256-token chunks within max_seq_len 1024"),
        (2048, "--context 2048 is not whole 256-token chunks"),
    ],
)
def test_main_refuses_a_context_that_is_no_whole_chunks_within_the_caches(
    toy, context, refusal, capsys
):
    argv, tuned = toy
    with pytest.raises(SystemExit):
        tune.main("toy", Toy, [*argv, "--context", str(context)])
    assert refusal in capsys.readouterr().err
    assert not tuned


def test_tuning_is_refused_without_a_profiles_directory(capsys):
    with pytest.raises(SystemExit):
        tune.main("encoder", Encoder, [])
    assert "no profiles directory" in capsys.readouterr().err
