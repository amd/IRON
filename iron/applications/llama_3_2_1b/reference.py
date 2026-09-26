# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The float32 CPU reference, as a forward pass: the one place torch runs.

:class:`ReferenceForward` is :meth:`.model.Llama.forward` behind the
harness's ``forward_pass(config, state)`` protocol, numpy in and out, so
:func:`.harness.check_accuracy` compares it with the NPU without either side
knowing what the other computes in. It reads the same weights and the same
RoPE table as the NPU (``config.weights``, ``config.angles``), so a KL
between them is the NPU's arithmetic and nothing else.
"""

import numpy as np
import torch

from .harness import LlamaConfig, LlamaModelState
from .model import Llama


class ReferenceForward:
    """:meth:`Llama.forward` in float32, as a ``forward_pass``: the oracle
    :func:`.harness.check_accuracy` judges the NPU against.

    The plain forward keeps no cache, so this keeps the token history
    instead and runs all of it each call: a prompt starts a new history, a
    single token extends it. The logits at the last position of a causal
    pass are what a cached decode produces for that token.
    """

    def __init__(self, config: LlamaConfig):
        self.model = Llama.from_weights(config, config.weights, dtype=torch.float32)
        # float32 whatever the table's dtype: a bf16 table widens exactly.
        self.angles = torch.from_numpy(np.asarray(config.angles, dtype=np.float32))
        self.tokens = np.empty(0, dtype=np.int64)

    def __call__(
        self, config: LlamaConfig, state: LlamaModelState
    ) -> tuple[np.ndarray, LlamaModelState]:
        batch, seq_len = state.token_ids.shape
        assert batch == 1
        new = np.asarray(state.token_ids, dtype=np.int64).reshape(-1)
        self.tokens = new if seq_len > 1 else np.concatenate([self.tokens, new])
        state.num_preceding_tokens = self.tokens.shape[0]
        logits = self.model(torch.from_numpy(self.tokens), self.angles)[-1]
        return logits.numpy().reshape(1, 1, -1), state
