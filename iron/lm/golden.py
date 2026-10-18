# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model is judged by: Hugging Face transformers' own model in
float32 (``HuggingFace``), its logits recorded once to a file (``Golden``)
so a test or an accuracy run needs neither torch nor transformers, which
are not IRON's requirements, only to record.
"""

import dataclasses
import hashlib
import os
from pathlib import Path

import numpy as np

#: Set (``pytest --record-goldens`` sets it) to record what a ``Golden`` lacks.
RECORD = "IRON_RECORD_GOLDENS"


class Golden:
    """Logits by token sequence, each the logits after a sequence's last
    token, read from ``path`` (an ``.npz``).

    Args:
        path: The file; it need not exist yet.
        reference: Builds what records a sequence ``path`` lacks (a
            ``HuggingFace``), called once on the first such sequence, and only
            while ``RECORD`` is set; otherwise such a sequence raises
            ``LookupError``.
        inputs: What the reference is built from (a config, weights); the
            file holds their ``fingerprint`` and is refused if they change.

    Raises:
        ValueError: ``path`` was recorded from other ``inputs``.
    """

    def __init__(self, path, reference=None, inputs=()):
        self.path = Path(path)
        self.build = reference if os.environ.get(RECORD) else None
        self.reference = None
        self.fingerprint = fingerprint(*inputs) if inputs else None
        self.rows = self.read()

    def read(self) -> dict:
        """The file's rows; none if it is stale and this records."""
        if not self.path.exists():
            return {}
        with np.load(self.path) as f:
            rows = dict(f)
        held = str(rows.pop("fingerprint", ""))
        if self.fingerprint is None or held == self.fingerprint:
            return rows
        if self.build is not None:
            return {}
        raise ValueError(
            f"{self.path} was recorded from other inputs: re-record it where "
            "transformers is installed (pytest --record-goldens)"
        )

    def logits(self, tokens) -> np.ndarray:
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        key = hashlib.sha256(tokens.tobytes()).hexdigest()[:16]
        if key not in self.rows:
            if self.build is None:
                raise LookupError(
                    f"{self.path} holds no logits for these {tokens.size} tokens: "
                    "record them where transformers is installed (pytest "
                    "--record-goldens)"
                )
            if self.reference is None:
                self.reference = self.build()
            row = np.asarray(self.reference.logits(tokens), np.float32)
            # Another process may have recorded others since this one read.
            self.rows = self.read() | self.rows | {key: row}
            self.write()
        return self.rows[key]

    def write(self):
        """The rows to the file, replaced whole so no reader sees half."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        held = {} if self.fingerprint is None else {"fingerprint": self.fingerprint}
        partial = self.path.with_name(f".{self.path.stem}.{os.getpid()}.npz")
        np.savez_compressed(partial, **self.rows, **held)
        os.replace(partial, self.path)


def fingerprint(*values) -> str:
    """A digest of ``values``, a weights tree's leaves by name (``leaves``):
    arrays by their bytes, shapes and types, anything else by ``repr``.
    """
    from .base import leaves

    digest = hashlib.sha256()
    for name, value in leaves(list(values)):
        digest.update(name.encode())
        if isinstance(value, np.ndarray):
            digest.update(f"{value.dtype}{value.shape}".encode())
            digest.update(np.ascontiguousarray(value).tobytes())
        else:
            digest.update(repr(value).encode())
    return digest.hexdigest()[:16]


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
        state = {k: torch.from_numpy(v) for k, v in flat(weights)}
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
    ``metadata["json"]`` path, the inverse of ``Config.from_checkpoint``:
    a value its ``convert`` built gives its own ``to_json()``. A field that
    is None or not JSON is left out.
    """
    out = {}
    for f in dataclasses.fields(config):
        key, value = f.metadata.get("json"), getattr(config, f.name)
        if hasattr(value, "to_json"):
            value = value.to_json()
        if key is None or not isinstance(value, (bool, int, float, str, tuple, dict)):
            continue
        *path, leaf = key.split(".")
        node = out
        for part in path:
            node = node.setdefault(part, {})
        node[leaf] = list(value) if isinstance(value, tuple) else value
    return out


def flat(tree):
    """``tree``'s arrays by their dotted names, in float32."""
    from .base import leaves

    return ((name, value.astype(np.float32)) for name, value in leaves(tree))
