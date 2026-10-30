# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Word error rate against a reference transcript, OpenAI Whisper's own
normalization: upper-cased, three common abbreviations expanded, then
everything but letters, digits, apostrophes and spaces dropped and the
apostrophes themselves removed, before splitting on spaces. Numbers and
punctuation are not otherwise aligned.
"""

import re

_EXPANSIONS = (("MR.", "MISTER"), ("MRS.", "MISSUS"), ("DR.", "DOCTOR"))


def normalize_words(text: str) -> list[str]:
    """``text``'s words, normalized for scoring."""
    text = text.upper()
    for short, long in _EXPANSIONS:
        text = text.replace(short, long)
    return re.sub(r"[^A-Z0-9' ]", " ", text).replace("'", "").split()


def word_error_rate(reference: str, hypothesis: str) -> float:
    """``hypothesis`` against ``reference``: their normalized words'
    Levenshtein distance over the reference's word count (1 with none).
    """
    ref, hyp = normalize_words(reference), normalize_words(hypothesis)
    row = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        prev, row[0] = row[0], i
        for j, h in enumerate(hyp, 1):
            prev, row[j] = row[j], min(row[j] + 1, row[j - 1] + 1, prev + (r != h))
    return row[-1] / max(len(ref), 1)
