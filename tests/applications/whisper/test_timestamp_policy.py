# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.applications.whisper.timestamp_policy.step`` against amd/IRON#218's
``TokenPolicy`` (Giuseppe Capaldo), ported here verbatim as the oracle
(https://github.com/amd/IRON/pull/218): no NPU, no model, random logits
walked greedily through both for many simulated windows, plus the named
edge cases its docstring promises (the first step, a timestamp pair, a
lone trailing timestamp, and a forced timestamp).
"""

import numpy as np
import pytest

from iron.applications.whisper import timestamp_policy as tp
from iron.operators.emit import reference as emit_reference

VOCAB = 600
EOS = 257
FIRST_SPECIAL = 358
TIMESTAMP_BEGIN = 364
MAX_INITIAL = 50
SUPPRESS = (1, 2, 7, 90)
BEGIN_SUPPRESS = (5, EOS)

CONFIG = dict(
    suppress_tokens=SUPPRESS,
    begin_suppress_tokens=BEGIN_SUPPRESS,
    first_special_token_id=FIRST_SPECIAL,
    timestamp_begin=TIMESTAMP_BEGIN,
    eos_token_id=EOS,
    max_initial_timestamp_index=MAX_INITIAL,
)


class TokenPolicy:
    """amd/IRON#218's ``TokenPolicy``, timestamps always on, at the
    constants above (a smaller vocabulary, easier to exercise fully).
    """

    def __call__(self, logits, generated):
        logits = np.array(logits, dtype=np.float32, copy=True)
        logits[list(SUPPRESS)] = -np.inf
        if not generated:
            logits[list(BEGIN_SUPPRESS)] = -np.inf
        logits[FIRST_SPECIAL:TIMESTAMP_BEGIN] = -np.inf
        last = len(generated) >= 1 and generated[-1] >= TIMESTAMP_BEGIN
        penultimate = len(generated) < 2 or generated[-2] >= TIMESTAMP_BEGIN
        if last:
            if penultimate:
                logits[TIMESTAMP_BEGIN:] = -np.inf
            else:
                logits[:EOS] = -np.inf
        stamps = [t for t in generated if t >= TIMESTAMP_BEGIN]
        if stamps:
            floor = stamps[-1] if last and not penultimate else stamps[-1] + 1
            logits[TIMESTAMP_BEGIN:floor] = -np.inf
        if not generated:
            logits[:TIMESTAMP_BEGIN] = -np.inf
            logits[TIMESTAMP_BEGIN + MAX_INITIAL + 1 :] = -np.inf
        logprobs = logits - np.logaddexp.reduce(logits)
        timestamp_logprob = np.logaddexp.reduce(logprobs[TIMESTAMP_BEGIN:])
        if timestamp_logprob > logprobs[:TIMESTAMP_BEGIN].max():
            logits[:TIMESTAMP_BEGIN] = -np.inf
        return logits


def walk(logits_of_step, steps):
    """``timestamp_policy.step`` and ``TokenPolicy`` over the same
    ``logits_of_step(k, generated)``, each greedy; asserts their masked
    logits agree exactly at every step. Returns the shared token history.
    """
    oracle = TokenPolicy()
    generated: list[int] = []
    penultimate_is_stamp, last_stamp = tp.initial_state()
    for k in range(steps):
        raw = logits_of_step(k, generated)
        first_step = k == 0
        token = generated[-1] if generated else -1
        want = oracle(raw, generated)
        got, penultimate_is_stamp, last_stamp = tp.step(
            raw,
            first_step=first_step,
            token=token,
            penultimate_is_stamp=penultimate_is_stamp,
            last_stamp=last_stamp,
            **CONFIG,
        )
        assert np.array_equal(want, got), f"step {k}: masks differ"
        generated.append(int(np.argmax(got)))
        if generated[-1] == EOS:
            break
    return generated


def test_is_stamp_row_matches_the_device_free_emit_reference():
    """``is_stamp_row``'s ``Emit`` program, against ``token >=
    timestamp_begin`` over a wide range of token ids, through ``Emit``'s
    own (already verified) reference rather than asserted by hand: the
    device half of ``step``'s ``last``/``penultimate_is_stamp``.
    """
    program = np.array(
        [tp.is_stamp_row(0, 0, timestamp_begin=TIMESTAMP_BEGIN)], dtype=np.int32
    )
    tokens = [0, 1, TIMESTAMP_BEGIN - 1, TIMESTAMP_BEGIN, TIMESTAMP_BEGIN + 1, 50363]
    tokens += list(np.random.default_rng(0).integers(0, 1 << 20, 50))
    for token in tokens:
        planes = np.array([[token], [0]], dtype=np.int32)
        _, state = emit_reference(program, planes, slots=0)
        assert state[0] == int(token >= TIMESTAMP_BEGIN), token


@pytest.mark.parametrize("seed", range(30))
def test_matches_token_policy_over_random_windows(seed):
    rng = np.random.default_rng(seed)
    walk(lambda k, generated: rng.normal(0, 3, VOCAB).astype(np.float32), steps=40)


def test_the_first_step_only_allows_an_early_timestamp():
    rng = np.random.default_rng(0)
    generated = walk(lambda k, generated: rng.normal(0, 3, VOCAB).astype(np.float32), 1)
    assert TIMESTAMP_BEGIN <= generated[0] <= TIMESTAMP_BEGIN + MAX_INITIAL


def test_a_lone_opening_timestamp_forces_text_next():
    """A timestamp followed by nothing yet (``penultimate_is_stamp`` True
    by length alone) bars every other timestamp next, even one favoured
    by far on raw logits: real speech always separates a pair's open and
    close by at least the words between them.
    """

    def logits_of_step(k, generated):
        raw = np.full(VOCAB, -1.0, dtype=np.float32)
        raw[100] = 5.0  # a plain text token
        if k == 0:
            raw[TIMESTAMP_BEGIN + 10] = 10.0  # the opening timestamp
        else:
            raw[TIMESTAMP_BEGIN + 10] = 20.0  # would win if timestamps were allowed
        return raw

    generated = walk(logits_of_step, steps=2)
    assert generated == [TIMESTAMP_BEGIN + 10, 100]


def test_a_closing_timestamp_is_forced_above_the_opening_one():
    """Once a pair's open and close are both drawn (around a text token in
    between), the next timestamp is barred below the last one: the floor.
    """

    def logits_of_step(k, generated):
        raw = np.full(VOCAB, -1.0, dtype=np.float32)
        raw[100] = 5.0
        if k == 0:
            raw[TIMESTAMP_BEGIN + 10] = 10.0  # opens the pair
        elif k == 1:
            pass  # forced to text regardless
        else:
            raw[TIMESTAMP_BEGIN + 3] = 10.0  # below the floor: must be barred
            raw[TIMESTAMP_BEGIN + 12] = 9.0  # at or above it: allowed
        return raw

    generated = walk(logits_of_step, steps=3)
    assert generated == [TIMESTAMP_BEGIN + 10, 100, TIMESTAMP_BEGIN + 12]


def test_a_lone_trailing_timestamp_bars_text_not_a_new_pair():
    """The token right after a pair closes (penultimate not a timestamp,
    last one) must itself be a timestamp (a new pair's opening) or
    end-of-text, not text, however favoured on raw logits.
    """

    def logits_of_step(k, generated):
        raw = np.full(VOCAB, -1.0, dtype=np.float32)
        raw[100] = 5.0
        if k == 0:
            raw[TIMESTAMP_BEGIN + 1] = 10.0  # opens
        elif k == 1:
            pass  # forced to text
        elif k == 2:
            raw[TIMESTAMP_BEGIN + 5] = 10.0  # closes the pair
        else:
            raw[100] = 20.0  # text would win unsuppressed
            raw[TIMESTAMP_BEGIN + 8] = 10.0
        return raw

    generated = walk(logits_of_step, steps=4)
    assert generated[3] >= TIMESTAMP_BEGIN


def test_a_forced_timestamp_overrides_a_narrowly_better_text_token():
    """The timestamps' summed probability beating the best text token's own
    forces a timestamp even where one text token's raw logit is higher.
    """

    def logits_of_step(k, generated):
        raw = np.full(VOCAB, -10.0, dtype=np.float32)
        raw[100] = 5.0  # the single best text token
        raw[TIMESTAMP_BEGIN : TIMESTAMP_BEGIN + 20] = 4.9  # many, each a bit lower
        if k == 0:
            raw[TIMESTAMP_BEGIN + 1] = 10.0  # opens the pair
        elif k == 1:
            pass  # forced to text
        return raw

    generated = walk(logits_of_step, steps=3)
    assert generated[2] >= TIMESTAMP_BEGIN
