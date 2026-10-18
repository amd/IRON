# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model is judged by: Hugging Face transformers' own model in
float32 (``HuggingFace``), its logits recorded once to a file (``Golden``)
so a test or an accuracy run needs neither torch nor transformers, which
are not IRON's requirements, only to record.
"""

import dataclasses
import hashlib
from pathlib import Path

import numpy as np


class Golden:
    """Logits by token sequence, each the logits after a sequence's last
    token, read from ``path`` (an ``.npz``).

    Args:
        path: The file; it need not exist yet.
        reference: Builds what records a sequence ``path`` lacks (a
            ``HuggingFace``), called on the first such sequence; None
            records nothing, and such a sequence raises ``LookupError``.
    """

    def __init__(self, path, reference=None):
        self.path = Path(path)
        self.rows = dict(np.load(self.path)) if self.path.exists() else {}
        self.reference = reference

    def logits(self, tokens) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        key = hashlib.sha256(tokens.tobytes()).hexdigest()[:16]
        if key not in self.rows:
            if self.reference is None:
                raise LookupError(
                    f"{self.path} holds no logits for these {tokens.size} tokens: "
                    "record them where transformers is installed (pytest "
                    "--record-goldens)"
                )
            if callable(self.reference):
                self.reference = self.reference()
            self.rows[key] = np.asarray(self.reference.logits(tokens), np.float32)
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # Another process may have recorded others since this one read.
            if self.path.exists():
                self.rows = dict(np.load(self.path)) | self.rows
            np.savez_compressed(self.path, **self.rows)
        return self.rows[key]


class HuggingFace:
    """transformers' own causal model in float32: a checkpoint directory's
    (``load``) or one built from an IRON config and a weights tree
    (``build``).
    """

    def __init__(self, model):
        self.model = model.eval()

    @classmethod
    def load(cls, directory) -> "HuggingFace":
        import torch
        import transformers

        return cls(
            transformers.AutoModelForCausalLM.from_pretrained(
                directory, dtype=torch.float32
            )
        )

    @classmethod
    def build(cls, model_type: str, config, weights, **json) -> "HuggingFace":
        """``model_type``'s model on ``config``'s fields as its
        ``config.json`` names them, and ``json``'s, over ``weights``.

        Raises:
            ValueError: ``weights`` lacks a parameter the model holds.
        """
        import torch
        import transformers

        hf = transformers.AutoConfig.for_model(
            model_type, **(config_json(config) | json)
        )
        model = transformers.AutoModelForCausalLM.from_config(hf, dtype=torch.float32)
        state = {k: torch.from_numpy(v) for k, v in _flat(weights)}
        missing, _ = model.load_state_dict(state, strict=False)
        if model.config.tie_word_embeddings:
            missing = [k for k in missing if k != "lm_head.weight"]
        if missing:
            raise ValueError(f"the weights lack {missing}")
        return cls(model)

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, float32."""
        import torch

        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        return out.logits[0, -1].numpy()


def config_json(config) -> dict:
    """``config``'s fields as its ``config.json`` names them: each field's
    ``metadata["json"]`` path, the inverse of ``Config.from_checkpoint``.
    A field that is None or not JSON is left out.
    """
    out = {}
    for f in dataclasses.fields(config):
        key, value = f.metadata.get("json"), getattr(config, f.name)
        if key is None or not isinstance(value, (bool, int, float, str, tuple)):
            continue
        *path, leaf = key.split(".")
        node = out
        for part in path:
            node = node.setdefault(part, {})
        node[leaf] = list(value) if isinstance(value, tuple) else value
    return out


def _flat(tree, prefix=""):
    """``tree``'s arrays by their dotted names, in float32."""
    items = enumerate(tree) if isinstance(tree, list) else vars(tree).items()
    for name, value in items:
        if isinstance(value, np.ndarray):
            yield f"{prefix}{name}", value.astype(np.float32)
        else:
            yield from _flat(value, f"{prefix}{name}.")
