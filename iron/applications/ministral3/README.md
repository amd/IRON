<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Ministral 3's text decoder

Mistral AI's Ministral 3 text decoder, `Ministral3` in `model.py`, whose
docstring says how it differs from Llama: YaRN's RoPE and Llama 4's query
temperature past the trained context. Its device-free test is
`tests/applications/ministral3/reference/`.

The released checkpoints
([`mistralai/Ministral-3-3B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512)
and its siblings, Apache-2.0) are Mistral 3's vision-language model: the
text config under `text_config`, the text weights nested under the
model's. `Ministral3` reads both of transformers' nestings and leaves the
vision tower unread. It refuses the Instruct checkpoints, which are FP8.
No real checkpoint has been loaded yet; the tests use synthetic ones.
