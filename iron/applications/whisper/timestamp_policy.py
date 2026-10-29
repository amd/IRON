# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A reference for Whisper's timestamp decoding rules, amd/IRON#218's
``TokenPolicy`` (Giuseppe Capaldo) recast as a per-step update over two
carried scalars rather than the whole generated-so-far list: this step's
input token and those two are enough to reproduce every rule bit for bit,
since timestamps come in monotonically increasing pairs.

``TokenPolicy`` reads ``generated``, every token this window has drawn, to
decide:

- whether the last token was a timestamp (``generated[-1]``: this step's
  own input, ``token``, needs no state of its own) and the one before
  it (``generated[-2]``: ``penultimate_is_stamp``, carried from the last
  step's own ``last``, True with fewer than two tokens drawn, matching
  ``len(generated) < 2``);
- the monotonic floor, the highest timestamp drawn so far (``stamps[-1]``:
  ``last_stamp``, carried, refreshed each step with ``token`` where it is
  itself a timestamp, ``NO_STAMP`` with none yet).

A forced timestamp (the drawn probability mass above ``timestamp_begin``
exceeding the best text token's) needs no state at all: a step's own
``logits`` already hold both.
"""

import numpy as np

#: No timestamp drawn yet this window (``stamps`` empty in TokenPolicy).
NO_STAMP = -1


def initial_state() -> tuple[bool, int]:
    """``(penultimate_is_stamp, last_stamp)`` before any token of a window
    is drawn, for the window's first generated token's own call
    (``step``'s ``first_step=True``, which does not read them).
    """
    return True, NO_STAMP


def step(
    logits: np.ndarray,
    *,
    first_step: bool,
    token: int,
    penultimate_is_stamp: bool,
    last_stamp: int,
    suppress_tokens,
    begin_suppress_tokens,
    first_special_token_id: int,
    timestamp_begin: int,
    eos_token_id: int,
    max_initial_timestamp_index: int,
) -> tuple[np.ndarray, bool, int]:
    """``logits`` (float, one row, ``-inf`` already at anything a sampler
    must never draw: ``Whisper.sampled``'s own suppression is applied
    first on the device) suppressed as ``TokenPolicy`` would with
    timestamps on, and the state carried into the step after.

    Args:
        first_step: Whether this call draws the window's first generated
            token (``not generated``): the window's own prompt chunk.
        token: The token just drawn, this step's input; ignored at
            ``first_step``, which has none.
        penultimate_is_stamp: The call two steps back's own ``last``;
            ``initial_state``'s before the second token is drawn.
        last_stamp: The highest timestamp token drawn so far this window;
            ``initial_state``'s (``NO_STAMP``) before any is.

    Returns:
        ``(logits, penultimate_is_stamp', last_stamp')``, the pair carried
        into the step after.
    """
    logits = np.array(logits, dtype=np.float32, copy=True)
    logits[list(suppress_tokens)] = -np.inf
    if first_step:
        logits[list(begin_suppress_tokens)] = -np.inf
    logits[first_special_token_id:timestamp_begin] = -np.inf

    last = (not first_step) and token >= timestamp_begin
    if last:
        if penultimate_is_stamp:
            logits[timestamp_begin:] = -np.inf
        else:
            logits[:eos_token_id] = -np.inf
    # last_stamp, as carried, is stamps[-1] over every token before token
    # (this step's own input): refreshed here with token itself, since
    # token is the newest one TokenPolicy's stamps[-1] would see at this
    # decision, a timestamp drawn between two calls, not within one.
    current_stamp = token if last else last_stamp
    if current_stamp != NO_STAMP:
        floor = (
            current_stamp if (last and not penultimate_is_stamp) else current_stamp + 1
        )
        logits[timestamp_begin:floor] = -np.inf
    if first_step:
        logits[:timestamp_begin] = -np.inf
        logits[timestamp_begin + max_initial_timestamp_index + 1 :] = -np.inf

    logprobs = logits - np.logaddexp.reduce(logits)
    timestamp_logprob = np.logaddexp.reduce(logprobs[timestamp_begin:])
    if timestamp_logprob > logprobs[:timestamp_begin].max():
        logits[:timestamp_begin] = -np.inf

    # first_step's own draw is read as the step after's own token, its own
    # last, not carried from here: that step's penultimate_is_stamp is
    # True by length alone (generated will hold one token, matching
    # TokenPolicy's len(generated) < 2), regardless of what first_step drew.
    next_penultimate = True if first_step else last
    return logits, next_penultimate, current_stamp
