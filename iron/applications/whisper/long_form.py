# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Long-form transcription's host-side bookkeeping, ported from amd/IRON#218's
(Giuseppe Capaldo) ``transcribe_long``/``segments_of``: OpenAI Whisper's
sequential windowed decoding, greedy, without temperature fallback or
conditioning on previous text. Needs only a window's own drawn token ids;
how those ids are drawn (the timestamp rules, on the NPU) is
``timestamp_policy.py``'s own, not yet wired into a window's own decode.
"""

import dataclasses


@dataclasses.dataclass
class Window:
    """One window's own seek (samples from the clip's start) and the
    tokens its call drew, timestamps included, ending in ``eos``.
    """

    seek: int
    tokens: list[int]


def seek_advance(
    tokens: list[int], size: int, *, eos: int, timestamp_begin: int, input_stride: int
) -> int:
    """How far past a window's own ``seek`` the next one starts: the last
    complete timestamp pair's own close, converted from timestamp steps to
    ``size``'s own unit by ``input_stride``; the whole window (``size``)
    where there is no such pair, or where the window ends in a single
    trailing timestamp (closing no pair of its own).

    Args:
        tokens: The window's own drawn tokens, ending in ``eos``.
        size: The window's own extent, samples or frames according to
            what ``input_stride`` converts a timestamp step (0.02 s) to.
    """
    text_end = [t for t in tokens if t != eos]
    is_stamp = [t >= timestamp_begin for t in text_end]
    single_ending = is_stamp[-2:] == [False, True]
    pairs = [i + 1 for i in range(len(is_stamp) - 1) if is_stamp[i] and is_stamp[i + 1]]
    advance = size
    if pairs and not single_ending:
        last_stamp = text_end[pairs[-1] - 1] - timestamp_begin
        advance = last_stamp * input_stride
    return advance if advance > 0 else size


def segments_of(
    windows: list[Window],
    decode,
    *,
    eos: int,
    timestamp_begin: int,
    timestamp_seconds: float,
    hop_seconds: float,
) -> list[tuple[float, float | None, str]]:
    """``(start, end, text)`` of every timestamp-delimited segment in
    ``windows``, in seconds from the clip's start; the last segment of the
    last window has no ``end`` if the window did not close it.

    Args:
        decode: A tokenizer's own ``decode(token_ids) -> str``.
    """
    result = []
    for window in windows:
        offset = window.seek * hop_seconds
        start, text = None, []
        for token in window.tokens:
            if token >= timestamp_begin:
                time_s = offset + (token - timestamp_begin) * timestamp_seconds
                if start is None:
                    start = time_s
                elif text:
                    result.append((start, time_s, decode(text).strip()))
                    start, text = time_s, []
                else:
                    start = time_s
            elif token < eos:
                text.append(token)
        if text:
            result.append((start or offset, None, decode(text).strip()))
    return result
