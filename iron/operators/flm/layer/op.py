# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import functools

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron import CompileTime, DispatchTime, In, InOut
from aie.iron.kernels import FlmGemma4DecodeGeometry
from ml_dtypes import bfloat16

from iron.common import Operator, Unresolvable, field
from iron.operators.flm.layer.design import (
    RTP_ADDRESSES,
    LayerType,
    arg_sizes,
    decode_layer,
    layer_kernels,
)


class DecodeLayer(Operator):
    """One Gemma 4 decode layer for one token, as FastFlowLM's engine drives it.

    See README.md for the parameters, the buffers and the dispatch parameters.
    """

    geometry: CompileTime[FlmGemma4DecodeGeometry] = field()
    layer_type: CompileTime[LayerType | str] = field()
    x_len: CompileTime[int] = field(
        derive=lambda op: arg_sizes(op.geometry)["x"], repr=False
    )
    proj_len: CompileTime[int] = field(
        derive=lambda op: arg_sizes(op.geometry)["proj"], repr=False
    )
    rms_len: CompileTime[int] = field(
        derive=lambda op: arg_sizes(op.geometry)["rms"], repr=False
    )
    rope_rms_len: CompileTime[int] = field(
        derive=lambda op: arg_sizes(op.geometry)["rope_rms"], repr=False
    )
    kv_len: CompileTime[int] = field(
        derive=lambda op: arg_sizes(op.geometry)["kv"], repr=False
    )

    # The runtime sequence's argument order.
    x = InOut(x_len, dtype=bfloat16)
    proj = In(proj_len, dtype=bfloat16)
    rms = In(rms_len, dtype=bfloat16)
    rope_rms = In(rope_rms_len, dtype=bfloat16)
    kv = InOut(kv_len, dtype=bfloat16)
    context_len: DispatchTime[np.int32] = field(init=False)
    max_l: DispatchTime[np.int32] = field(init=False)

    def validate(self) -> None:
        if self.geometry not in RTP_ADDRESSES:
            raise ValueError(
                f"DecodeLayer: geometry ({self.geometry!r}) must be "
                "aie.iron.kernels.FLM_GEMMA4_E2B_DECODE or FLM_GEMMA4_E4B_DECODE"
            )
        try:
            self.layer_type = LayerType(self.layer_type)
        except ValueError:
            raise ValueError(
                f"DecodeLayer: layer_type ({self.layer_type!r}) must be one of "
                f"{', '.join(LayerType)}"
            ) from None

    def resolve(self, dev):
        if dev is None or dev.arch != AIEArch.AIE2p:
            raise Unresolvable(
                "DecodeLayer: the flm_gemma4_decode kernels are AIE2P only"
            )
        return dataclasses.replace(self)

    def xclbin_operator(self):
        # The four layer types share one array; they differ in their sequences.
        return dataclasses.replace(self, layer_type=LayerType.GLOBAL)

    def exported_design(self):
        return functools.partial(
            decode_layer,
            self.dev,
            self.geometry,
            RTP_ADDRESSES[self.geometry],
            self.layer_type,
            kernels=layer_kernels(self.geometry),
        )
