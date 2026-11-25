# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Device-independent whole-clip Whisper transcript and timing checks."""

import numpy as np

from iron.applications.whisper.model import normalize_words, word_error_rate

# Strix's timestamp near-tie changes one word and drifts by up to 0.4 s.
# Permit that one substitution and 0.5 s, but no omitted/duplicated words.
MAX_WER = 0.02
MAX_WORD_ERRORS = 1
MAX_TIME_ERROR = 0.5


def check_long_form(actual, expected, duration_s):
    """Compare whole transcripts and text-aligned segment boundaries, not NPU seeks."""
    ref = normalize_words(expected["text"])
    got = normalize_words(actual["text"])
    assert ref and len(got) == len(ref), "missing or duplicated transcript words"
    wer = word_error_rate(expected["text"], actual["text"])
    substitutions = sum(a != b for a, b in zip(ref, got))
    assert wer <= MAX_WER, f"WER {wer} > {MAX_WER}"
    # Equal counts plus this cap reject omissions, duplicates and multiword drift.
    assert substitutions <= MAX_WORD_ERRORS, f"{substitutions} word substitutions"

    def indexed_segments(result):
        segments = []
        words = []
        previous = 0.0
        for index, (start, end, text) in enumerate(result["segments"]):
            part = normalize_words(text)
            if not part:
                continue
            if end is None:
                assert (
                    index == len(result["segments"]) - 1
                ), "only the final text segment may end at clip duration"
                end = duration_s
            end = min(end, duration_s)
            assert np.isfinite([start, end]).all() and 0 <= start <= end
            assert start >= previous, "overlapping or reversed timestamp segments"
            segments.append((len(words), len(words) + len(part), start, end))
            words.extend(part)
            previous = end
        assert words == normalize_words(
            result["text"]
        ), "segments lose or repeat speech"
        assert segments, "no timestamped speech"
        return segments

    reference = indexed_segments(expected)
    observed = indexed_segments(actual)
    worst = 0.0
    for source, target in ((observed, reference), (reference, observed)):
        for first, last, start, end in source:
            for word, time, is_end in ((first, start, False), (last, end, True)):
                containing = [
                    (a, b, lo, hi)
                    for a, b, lo, hi in target
                    if (a < word <= b if is_end else a <= word < b)
                ]
                assert len(containing) == 1
                a, b, lo, hi = containing[0]
                if is_end and word == b:
                    lo = hi
                elif not is_end and word == a:
                    hi = lo
                error = max(lo - time, time - hi, 0)
                worst = max(worst, error)
    assert worst <= MAX_TIME_ERROR, f"segment boundary drift {worst} s"
    return wer, worst
