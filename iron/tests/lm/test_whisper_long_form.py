# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whole-clip checks tolerate near-ties without accepting lost speech or bad times."""

import copy

import pytest

from iron.tests.support.whisper import check_long_form


def transcript():
    words = [f"word{i}" for i in range(100)]
    return {
        "text": " ".join(words),
        "segments": [
            (i / 10, (i + 10) / 10, " ".join(words[i : i + 10]))
            for i in range(0, 100, 10)
        ],
    }


def test_near_tie_substitution_and_timestamp_drift():
    expected = transcript()
    actual = copy.deepcopy(expected)
    actual["text"] = actual["text"].replace("word25", "replacement")
    actual["segments"] = [
        (a + 0.4, b + 0.4, text.replace("word25", "replacement"))
        for a, b, text in actual["segments"]
    ]
    wer, drift = check_long_form(actual, expected, duration_s=10.0)
    assert wer == 0.01
    assert drift == pytest.approx(0.4)


def test_segmentation_can_change_without_changing_words_or_times():
    expected = transcript()
    actual = copy.deepcopy(expected)
    a, _, first = actual["segments"].pop(0)
    _, b, second = actual["segments"].pop(0)
    actual["segments"].insert(0, (a, b, first + " " + second))
    assert check_long_form(actual, expected, duration_s=10.0) == (0.0, 0.0)


def test_final_timestamp_is_clamped_to_clip_duration():
    expected = transcript()
    actual = copy.deepcopy(expected)
    actual["segments"][-1] = (9.0, 10.4, actual["segments"][-1][2])
    assert check_long_form(actual, expected, duration_s=10.0) == (0.0, 0.0)


@pytest.mark.parametrize(
    "fault", ["drop", "duplicate", "replace", "shift", "reverse", "missing", "swap"]
)
def test_bad_transcripts_and_timestamps_fail(fault):
    expected = transcript()
    actual = copy.deepcopy(expected)
    if fault == "drop":
        actual["text"] = " ".join(actual["text"].split()[:-10])
        actual["segments"].pop()
    elif fault == "duplicate":
        actual["text"] += " " + actual["segments"][-1][2]
        actual["segments"].append((10, 11, actual["segments"][-1][2]))
    elif fault == "replace":
        actual["text"] = actual["text"].replace("word", "wrong")
        actual["segments"] = [
            (a, b, text.replace("word", "wrong")) for a, b, text in actual["segments"]
        ]
    elif fault == "shift":
        actual["segments"] = [
            (a + 0.6, b + 0.6, text) for a, b, text in actual["segments"]
        ]
    elif fault == "reverse":
        a, b, text = actual["segments"][1]
        actual["segments"][1] = (b, a, text)
    elif fault == "missing":
        a, _, text = actual["segments"][1]
        actual["segments"][1] = (a, None, text)
    else:
        actual["segments"][1], actual["segments"][2] = (
            actual["segments"][2],
            actual["segments"][1],
        )
    with pytest.raises(AssertionError):
        check_long_form(actual, expected, duration_s=10.0)
