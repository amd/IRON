#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper-large-v3-turbo does not fit ``iron.lm.tune.main`` as it stands,
so this module does not call it the way every other model's ``tune.py``
does -- said here plainly, per the skill's own rule to drop what a model
genuinely cannot do rather than silently.

``iron.lm.tune.main`` tunes a ``CausalLM``'s *pair* of versions, a decode
step and a prompt chunk (``calls()`` measures both, at a ladder of
contexts the prompt chunk's own cost grows with). ``WhisperDecoder`` has
no prompt version at all, deliberately (``load()``'s own docstring: no
divisor of ``max_seq_len`` also satisfies ``flm.GEMM``'s row tiling, and
the real prompt is four tokens, far too short to need one) -- there is
only ever a decode step to tune, and no growing context to price it at
(``max_seq_len`` is 448, not the tens of thousands a decoder-only model's
own tuning ladder is built around). ``WhisperEncoder`` is not a
``CausalLM`` at all (one compile a clip, no decode step, no cache), so
none of ``iron.lm.tune`` applies to it either.

What tuning *would* mean here -- measuring each operator design's real
cost on this device and narrowing/packing them with a
``JointNarrowing``/``CostTable`` built directly from ``WhisperEncoder``'s
and ``WhisperDecoder``'s own traced steps, not through ``iron.lm.tune``'s
decode/prompt-pair machinery -- is not attempted in this port: this
model's accuracy gate is not green yet (see README.md, skill-gaps.md),
and tuning a shape whose own correctness is still in question is not a
good use of NPU time. ``profiles/npu2.json`` stays the placeholder empty
profile (no tunable is named, so every operator resolves its own default
against the device) until that gate is green and someone measures this
model's real cost table.
"""

if __name__ == "__main__":
    raise SystemExit(__doc__)
