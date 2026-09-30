# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import kernels

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

GEOMETRIES = {
    "GEMMA4_E2B": kernels.FLM_GEMMA4_E2B_DECODE,
    "GEMMA4_E4B": kernels.FLM_GEMMA4_E4B_DECODE,
}


@dataclass
class DecodeLayer(MLIROperator):
    """One Gemma 4 decode layer for one token, as FastFlowLM's engine drives it.

    See README.md for the parameters, the buffers and the dispatch parameters.
    """

    model: str
    layer_type: str
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        if self.model not in GEOMETRIES:
            raise ValueError(
                f"model must be one of {sorted(GEOMETRIES)}, not {self.model!r}"
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
    def geometry(self):
        return GEOMETRIES[self.model]

    @property
    def name(self) -> str:
        dev = aie_utils.get_current_device().resolve().name
        return f"FLM_DecodeLayer_{self.model}_{self.layer_type}_{dev}"

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
                    RTP_ADDRESSES[self.model],
                    self.layer_type,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact.from_extern(fn)
            for fn in layer_kernels(self.geometry).values()
        ]

    def get_arg_spec(self):
        sizes = arg_sizes(self.geometry)
        return [
            AIERuntimeArgSpec("inout", (sizes["x"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["proj"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["rms"],), dtype=bfloat16),
            AIERuntimeArgSpec("in", (sizes["rope_rms"],), dtype=bfloat16),
            AIERuntimeArgSpec("inout", (sizes["kv"],), dtype=bfloat16),
        ]
