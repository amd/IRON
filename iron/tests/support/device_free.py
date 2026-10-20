# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Building any model device-free, every weight its own zero in its own
shape: no checkpoint, so no per-model knowledge of its tensors' names.
"""

from types import SimpleNamespace

import numpy as np

from iron.common.graph.compiled import Graph, _Unbound, walk
from iron.lm.checkpoint import nest


class Permissive(SimpleNamespace):
    """A ``weights``-shaped stand-in for ``DeviceFreeWeights``: any
    attribute it is not given is another of its own, so a model's
    ``__init__`` may read ``weights.model.text_model`` or the like, on its
    way to a ``load_state_dict``/``load_layers`` call this never reaches,
    without raising.
    """

    def __getattr__(self, name: str) -> "Permissive":
        return Permissive()


def _zeros(root) -> dict:
    """Every ``_Unbound`` placeholder under ``root``, zeroed in its own
    shape and dtype, by its dotted path from ``root``.
    """
    return {
        n: np.zeros(p.shape, p.dtype)
        for n, p, _, _ in walk(root)
        if isinstance(p, _Unbound)
    }


class DeviceFreeWeights:
    """Mixed in before a ``Graph`` subclass: ``load_state_dict`` ignores
    what it is given and binds every ``param`` it holds to its own zero, in
    its own shape, which ``load_state_dict`` already knows from ``__init__``
    alone. What ``Checkpoint(path).tree("unread")`` gives a real
    checkpoint's names, with none to read.

    ``Encoder.load_layers`` binds each layer directly rather than through
    ``self.load_state_dict``, so it is overridden the same way.
    """

    def load_state_dict(self: Graph, tree, *, path: str = "") -> None:
        super().load_state_dict(nest(_zeros(self)), path=path)

    def load_layers(self, tree, layers: str, norm: str = "") -> None:
        for layer in self.layers:
            layer.load_state_dict(nest(_zeros(layer)))
        if self.final_norm is not None:
            self.final_norm.load_state_dict(nest(_zeros(self.final_norm)))
