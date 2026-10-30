# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``word_error_rate``'s normalization and Levenshtein distance, against
known word-edit counts: no NPU, no model.
"""

from iron.applications.whisper.wer import normalize_words, word_error_rate


def test_identical_text_has_no_error():
    text = "The quick brown fox jumps over the lazy dog."
    assert word_error_rate(text, text) == 0.0


def test_one_substitution_in_five_words():
    assert word_error_rate("one two three four five", "one two zero four five") == 0.2


def test_one_deletion_and_one_insertion():
    # hyp drops "three" (a deletion against ref) and adds "six" (an insertion).
    assert word_error_rate("one two three four five", "one two four five six") == 0.4


def test_punctuation_and_case_are_not_aligned():
    assert word_error_rate("Hello, world!", "hello world") == 0.0


def test_abbreviations_expand_before_comparing():
    assert word_error_rate("Mister Smith", "Mr. Smith") == 0.0
    assert word_error_rate("Doctor Who", "Dr. Who") == 0.0


def test_empty_reference_is_the_hypothesis_s_word_count():
    assert word_error_rate("", "one two") == 2.0
    assert word_error_rate("", "") == 0.0


def test_normalize_words_drops_apostrophes_not_words():
    assert normalize_words("don't stop") == ["DONT", "STOP"]
