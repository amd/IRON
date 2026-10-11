# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2 1.7B Instruct's command line: ``python -m iron.applications.llama.smollm2``."""

from iron import lm
from iron.applications.llama.model import SmolLM2Runner

lm.main(SmolLM2Runner, "SmolLM2 1.7B Instruct on the NPU")
