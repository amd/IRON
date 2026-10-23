# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a model is judged by: Hugging Face transformers' own model in
float32 (``HuggingFace``), its logits recorded once to a file (``Golden``)
so a test or an accuracy run needs neither torch nor transformers, which
are not IRON's requirements, only to record.
"""

# torch and transformers: only recording imports them.
# pyright: reportMissingImports=false

import dataclasses
import hashlib
import os
from pathlib import Path
from typing import Any

import numpy as np

#: Set (``pytest --record-goldens`` sets it) to record what a ``Golden`` lacks.
RECORD = "IRON_RECORD_GOLDENS"


class Golden:
    """Logits by token sequence and any arrays beside it (a clip, an
    image), each the logits after a sequence's last token, read from
    ``path`` (an ``.npz``).

    Args:
        path: The file; it need not exist yet.
        reference: Builds what records a sequence ``path`` lacks (a
            ``HuggingFace``), called once on the first such sequence, and only
            while ``RECORD`` is set; otherwise such a sequence raises
            ``LookupError``, or ``FileNotFoundError`` naming ``path`` where
            there is no file.
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

    def logits(self, tokens, *arrays) -> np.ndarray:
        """The logits after ``tokens`` given ``arrays``, which the
        reference's ``logits`` takes after them.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        digest = hashlib.sha256(tokens.tobytes())
        for array in map(np.ascontiguousarray, arrays):
            digest.update(f"{array.dtype}{array.shape}".encode() + array.tobytes())
        key = digest.hexdigest()[:16]
        if key not in self.rows:
            if self.build is None and not self.path.exists():
                raise FileNotFoundError(
                    f"{self.path} is missing: record it where torch and "
                    "transformers are installed (pytest --record-goldens) and "
                    "install it at that path"
                )
            if self.build is None:
                raise LookupError(
                    f"{self.path} holds no logits for these {tokens.size} tokens: "
                    "record them where transformers is installed (pytest "
                    "--record-goldens)"
                )
            if self.reference is None:
                self.reference = self.build()
            # A copy: a reference's row may view its whole forward's logits.
            row = np.array(self.reference.logits(tokens, *arrays), np.float32)
            # Another process may have recorded others since this one read.
            self.rows = self.read() | self.rows | {key: row}
            self.write()
        return self.rows[key]

    def write(self):
        """The rows to the file, replaced whole so no reader sees half."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        held: dict[str, Any] = (
            {} if self.fingerprint is None else {"fingerprint": self.fingerprint}
        )
        partial = self.path.with_name(f".{self.path.stem}.{os.getpid()}.npz")
        np.savez_compressed(partial, **self.rows, **held)
        os.replace(partial, self.path)


def fingerprint(*values) -> str:
    """A digest of ``values``, a weights tree's leaves by name (``leaves``):
    arrays by their bytes, shapes and types, anything else by ``repr``.
    """
    from .checkpoint import leaves

    digest = hashlib.sha256()
    for name, value in leaves(list(values)):
        digest.update(name.encode())
        if isinstance(value, np.ndarray):
            digest.update(f"{value.dtype}{value.shape}".encode())
            digest.update(np.ascontiguousarray(value).tobytes())
        else:
            digest.update(_text(value).encode())
    return digest.hexdigest()[:16]


def _text(value) -> str:
    """``repr(value)``, but a dataclass names only its fields off their
    defaults, so a field added with a default changes no fingerprint. A
    changed default changes no fingerprint either: a golden recorded under
    the old default is still accepted for a config left at the new one.
    """
    if not dataclasses.is_dataclass(value) or isinstance(value, type):
        return repr(value)
    changed = [
        f"{f.name}={_text(getattr(value, f.name))}"
        for f in dataclasses.fields(value)
        if not _is_default(f, getattr(value, f.name))
    ]
    return f"{type(value).__name__}({', '.join(changed)})"


def _is_default(field: dataclasses.Field, value) -> bool:
    if field.default is not dataclasses.MISSING:
        default = field.default
    elif field.default_factory is not dataclasses.MISSING:
        default = field.default_factory()
    else:
        return False
    try:
        return type(value) is type(default) and bool(value == default)
    except (TypeError, ValueError):
        return False


class HuggingFace:
    """transformers' own model in float32, of the auto class
    ``model_class`` names (a causal model's by default): a checkpoint
    directory's (``load``) or one built from an IRON config and a weights
    tree (``build``). A model of another kind subclasses it for its class
    and its ``logits``.
    """

    model_class = "AutoModelForCausalLM"

    def __init__(self, model):
        self.model = model.eval()

    @classmethod
    def load(cls, directory) -> "HuggingFace":
        import torch
        import transformers

        auto = getattr(transformers, cls.model_class)
        return cls(auto.from_pretrained(directory, dtype=torch.float32))

    @classmethod
    def build(cls, model_type: str, config, weights, **json) -> "HuggingFace":
        """``model_type``'s model on ``config``'s fields as its
        ``config.json`` names them, ``json``'s merged in, over ``weights`` named as
        the model's checkpoints name them: written to a checkpoint and
        loaded, so transformers renames (and stacks) them as it loads one.

        Raises:
            ValueError: ``weights`` lacks a parameter the model holds, other
                than one tied to another, or holds one it does not.
        """
        import tempfile

        import torch
        import transformers
        from safetensors.torch import save_file

        hf = transformers.AutoConfig.for_model(
            model_type, **_merged(config.to_json(), json)
        )
        auto = getattr(transformers, cls.model_class)
        with tempfile.TemporaryDirectory() as directory:
            hf.save_pretrained(directory)
            state = {k: torch.from_numpy(v) for k, v in flat(weights)}
            save_file(state, f"{directory}/model.safetensors")
            model, info = auto.from_pretrained(
                directory, dtype=torch.float32, output_loading_info=True
            )
        missing, unexpected = info["missing_keys"], info["unexpected_keys"]
        if missing or unexpected:
            raise ValueError(
                f"{model_type}: the weights lack {sorted(missing)} and hold "
                f"{sorted(unexpected)}, which the model does not"
            )
        return cls(model)

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens``, float32."""
        import torch

        with torch.no_grad():
            out = self.model(torch.tensor([list(tokens)]), use_cache=False)
        return out.logits[0, -1].numpy()


def _merged(a: dict, b: dict) -> dict:
    """``a`` with ``b``'s keys, an object in both merged key by key."""
    return a | {
        k: _merged(a[k], v) if isinstance(v, dict) and isinstance(a.get(k), dict) else v
        for k, v in b.items()
    }


def flat(tree):
    """``tree``'s arrays by their dotted names, in float32."""
    from .checkpoint import leaves

    return ((name, value.astype(np.float32)) for name, value in leaves(tree))
