#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

# Get the directory containing this test file
test_dir = Path(__file__).parent.absolute()

run = f"python3 {test_dir}/inference.py /srv/llama3.2-1b/model.safetensors /srv/llama3.2-1b/tokenizer.model --prompt_len 2048 --num_tokens 40"

checks = []

metrics = [
    ("Total", r"  Total time: (?P<metric>[\d\.e\+-]+) seconds"),
    ("TTFT", r"  Prefill time: (?P<metric>[\d\.e\+-]+) seconds"),
    ("TPS", r"  Tokens per second: (?P<metric>[\d\.e\+-]+)"),
    ("Num Tokens", r"  Tokens generated: (?P<metric>[\d\.e\+-]+)"),
]
