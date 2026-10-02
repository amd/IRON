# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron.kernels import FlmGemma4DecodeGeometry

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    KernelObjectArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.flm.layer.design import (
    LAYER_TYPES,
    RTP_ADDRESSES,
    arg_sizes,
    layer_kernels,
)


@dataclass
class DecodeLayer(MLIROperator):
    """One Gemma 4 decode layer for one token, as FastFlowLM's engine drives it.

    See README.md for the parameters, the buffers and the dispatch parameters.
    """

    geometry: FlmGemma4DecodeGeometry
    layer_type: str
    context: object = field(default=None, repr=False)
    _kernel_fns: dict = field(default=None, init=False, repr=False, compare=False)

    def __post_init__(self):
        if self.geometry not in RTP_ADDRESSES:
            raise ValueError(
                "geometry must be aie.iron.kernels.FLM_GEMMA4_E2B_DECODE or "
                f"FLM_GEMMA4_E4B_DECODE, not {self.geometry!r}"
            )
        if self.layer_type not in LAYER_TYPES:
            raise ValueError(
                f"layer_type must be one of {LAYER_TYPES}, not {self.layer_type!r}"
            )
        dev = aie_utils.get_current_device()
        if dev.arch != AIEArch.AIE2p:
            raise NotImplementedError("the flm_gemma4_decode kernels are AIE2P only")
        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        return f"FLM_DecodeLayer_{self.geometry.name}_{self.layer_type}_{dev}"

    def _kernels(self):
        """layer_kernels(geometry), built once for the MLIR and the kernel objects."""
        if self._kernel_fns is None:
            self._kernel_fns = layer_kernels(self.geometry)
        return self._kernel_fns

    def get_dispatch_params(self):
        return {"context_len": np.int32, "max_l": np.int32}

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "decode_layer",
                (
                    aie_utils.get_current_device(),
                    self.geometry,
                    RTP_ADDRESSES[self.geometry],
                    self.layer_type,
                ),
                {"kernels": self._kernels()},
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(fn) for fn in self._kernels().values()]

    def get_arg_spec(self):
        sizes = arg_sizes(self.geometry)
        return [
            AIERuntimeArgSpec("inout", (sizes["x"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["proj"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["rms"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["rope_rms"],), dtype=bfloat16),
            AIERuntimeArgSpec("inout", (sizes["kv"],), dtype=bfloat16),
        ]
