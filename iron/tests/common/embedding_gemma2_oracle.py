# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's own ``sandwich_layer`` (``iron.applications.
embedding_gemma2.oracle``), against a hand-assembled version of the same
formula on fixed random inputs. No NPU.
"""

import dataclasses

import numpy as np

from iron.lm import Oracle
from iron.applications.embedding_gemma2.config import AudioConfig
from iron.applications.embedding_gemma2.oracle import sandwich_layer


def test_sandwich_layer_matches_hand_assembled_attention_and_geglu():
    rng = np.random.default_rng(5)
    n, E, H, G, D, F = 4, 6, 2, 1, 4, 5
    x = rng.standard_normal((n, E)).astype(np.float32)
    angles = rng.standard_normal((n, D)).astype(np.float32)
    weights = {
        name: rng.standard_normal(shape).astype(np.float32)
        for name, shape in {
            "q_proj": (H * D, E),
            "k_proj": (G * D, E),
            "v_proj": (G * D, E),
            "o_proj": (E, H * D),
            "q_norm": (D,),
            "k_norm": (D,),
            "gate": (F, E),
            "up": (F, E),
            "down": (E, F),
        }.items()
    }
    norms = tuple(rng.standard_normal(E).astype(np.float32) for _ in range(4))

    # sandwich_layer reads its query head count from config.n_heads.
    oracle = Oracle(dataclasses.replace(AudioConfig(eps=1e-6), n_heads=H))
    got = sandwich_layer(
        oracle,
        x,
        [angles],
        q_proj=weights["q_proj"],
        k_proj=weights["k_proj"],
        v_proj=weights["v_proj"],
        o_proj=weights["o_proj"],
        q_norm=weights["q_norm"],
        k_norm=weights["k_norm"],
        norms=norms,
        gate=weights["gate"],
        up=weights["up"],
        down=weights["down"],
        groups=G,
        head_dim=D,
    )

    def rms(x, w):
        return x / np.sqrt(np.mean(x * x, -1, keepdims=True) + 1e-6) * w

    h = rms(x, norms[0])
    q = Oracle.rotate(
        rms((h @ weights["q_proj"].T).reshape(n, H, D), weights["q_norm"]), [angles]
    )
    k = Oracle.rotate(
        rms((h @ weights["k_proj"].T).reshape(n, G, D), weights["k_norm"]), [angles]
    )
    v = rms((h @ weights["v_proj"].T).reshape(n, G, D), np.float32(1))
    a = oracle.attend(q, k, v, scale=1.0) @ weights["o_proj"].T
    x2 = x + rms(a, norms[1])
    h2 = rms(x2, norms[2])
    gelu = Oracle.gelu_tanh(h2 @ weights["gate"].T)
    f = (gelu * (h2 @ weights["up"].T)) @ weights["down"].T
    want = x2 + rms(f, norms[3])
    np.testing.assert_allclose(got, want, rtol=1e-5, atol=1e-6)
