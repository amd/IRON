# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.applications.whisper.long_form`` against amd/IRON#218's own
``transcribe_long``/``segments_of`` inline logic (Giuseppe Capaldo), ported
here verbatim as the oracle: no NPU, no model, random token windows.
"""

import numpy as np
import pytest

from iron.applications.whisper import long_form as lf

EOS = 257
TIMESTAMP_BEGIN = 364
INPUT_STRIDE = 2
SIZE = 3000


def oracle_advance(tokens, size):
    """amd/IRON#218's ``transcribe_long``, the inline computation of one
    window's own advance, verbatim but for the names above.
    """
    text_end = [t for t in tokens if t != EOS]
    is_stamp = [t >= TIMESTAMP_BEGIN for t in text_end]
    single_ending = is_stamp[-2:] == [False, True]
    pairs = [i + 1 for i in range(len(is_stamp) - 1) if is_stamp[i] and is_stamp[i + 1]]
    advance = size
    if pairs and not single_ending:
        last_stamp = text_end[pairs[-1] - 1] - TIMESTAMP_BEGIN
        advance = last_stamp * INPUT_STRIDE
    return advance if advance > 0 else size


def oracle_segments(windows, decode):
    """amd/IRON#218's ``segments_of``, verbatim but for the names above."""
    result = []
    for window in windows:
        offset = window.seek * 0.01
        start, text = None, []
        for token in window.tokens:
            if token >= TIMESTAMP_BEGIN:
                time_s = offset + (token - TIMESTAMP_BEGIN) * 0.02
                if start is None:
                    start = time_s
                elif text:
                    result.append((start, time_s, decode(text).strip()))
                    start, text = time_s, []
                else:
                    start = time_s
            elif token < EOS:
                text.append(token)
        if text:
            result.append((start or offset, None, decode(text).strip()))
    return result


def random_window(rng, length=12):
    """A plausible window: open/text-run/close segments, sometimes
    adjacent, sometimes not, ending in EOS or cut off mid-window.
    """
    tokens, stamp = [], TIMESTAMP_BEGIN
    while len(tokens) < length:
        tokens.append(stamp)
        stamp += int(rng.integers(1, 5))
        for _ in range(int(rng.integers(0, 3))):
            tokens.append(int(rng.integers(0, 200)))
        tokens.append(stamp)
        stamp += int(rng.integers(0, 3))  # sometimes adjacent, sometimes not
    if rng.random() < 0.7:
        tokens.append(EOS)
    return tokens[:length]


@pytest.mark.parametrize("seed", range(50))
def test_seek_advance_matches_the_inline_oracle(seed):
    rng = np.random.default_rng(seed)
    tokens = random_window(rng)
    got = lf.seek_advance(
        tokens,
        SIZE,
        eos=EOS,
        timestamp_begin=TIMESTAMP_BEGIN,
        input_stride=INPUT_STRIDE,
    )
    assert got == oracle_advance(tokens, SIZE)


def test_no_timestamps_advances_the_whole_window():
    tokens = [10, 20, 30, EOS]
    assert (
        lf.seek_advance(
            tokens,
            SIZE,
            eos=EOS,
            timestamp_begin=TIMESTAMP_BEGIN,
            input_stride=INPUT_STRIDE,
        )
        == SIZE
    )


def test_two_adjacent_pairs_advance_to_the_first_close():
    # open1, text, close1=TB+9, open2(adjacent), text, close2=TB+20, eos:
    # the window ends on a normal close (single_ending's own pattern), so
    # amd/IRON#218's own rule advances the whole window regardless of the
    # pair found - matching the oracle is what this checks, not a hand
    # derivation of "the right" answer.
    tokens = [
        TIMESTAMP_BEGIN,
        1,
        2,
        TIMESTAMP_BEGIN + 9,
        TIMESTAMP_BEGIN + 9,
        3,
        TIMESTAMP_BEGIN + 20,
        EOS,
    ]
    got = lf.seek_advance(
        tokens,
        SIZE,
        eos=EOS,
        timestamp_begin=TIMESTAMP_BEGIN,
        input_stride=INPUT_STRIDE,
    )
    assert got == oracle_advance(tokens, SIZE) == SIZE


def test_three_segments_advances_past_the_first_two():
    # Three segments, the first two closing adjacently to the third's
    # open, the third left open at the window's end (no single_ending
    # pattern: the window cuts off mid-text, not right after a close).
    tokens = [
        TIMESTAMP_BEGIN,
        1,
        TIMESTAMP_BEGIN + 9,
        TIMESTAMP_BEGIN + 9,
        2,
        TIMESTAMP_BEGIN + 20,
        TIMESTAMP_BEGIN + 20,
        3,
        4,
    ]
    got = lf.seek_advance(
        tokens,
        SIZE,
        eos=EOS,
        timestamp_begin=TIMESTAMP_BEGIN,
        input_stride=INPUT_STRIDE,
    )
    assert got == oracle_advance(tokens, SIZE)
    assert got == (TIMESTAMP_BEGIN + 20 - TIMESTAMP_BEGIN) * INPUT_STRIDE


def decode(tokens):
    return " ".join(f"t{t}" for t in tokens)


def test_segments_of_matches_the_oracle_where_no_segment_starts_at_zero():
    windows = [
        lf.Window(
            seek=0,
            tokens=[
                TIMESTAMP_BEGIN + 5,
                10,
                11,
                TIMESTAMP_BEGIN + 15,
                TIMESTAMP_BEGIN + 15,
                12,
                TIMESTAMP_BEGIN + 25,
                EOS,
            ],
        ),
    ]
    got = lf.segments_of(
        windows,
        decode,
        eos=EOS,
        timestamp_begin=TIMESTAMP_BEGIN,
        timestamp_seconds=0.02,
        hop_seconds=0.01,
    )
    want = oracle_segments(windows, decode)
    assert got == want
    assert got == [(0.1, 0.3, "t10 t11"), (0.3, 0.5, "t12")]


def test_segments_of_leaves_the_last_segment_open_with_no_end():
    """The first window's first token opening at exactly
    ``timestamp_begin``, text with no closing timestamp: a start of
    0.0 and no end, matching the oracle.
    """
    windows = [lf.Window(seek=0, tokens=[TIMESTAMP_BEGIN, 10, 11])]
    got = lf.segments_of(
        windows,
        decode,
        eos=EOS,
        timestamp_begin=TIMESTAMP_BEGIN,
        timestamp_seconds=0.02,
        hop_seconds=0.01,
    )
    assert got == oracle_segments(windows, decode) == [(0.0, None, "t10 t11")]
