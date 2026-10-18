# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
import functools

from aie.dialects._aie_enum_gen import AIEArch
from aie.iron.kernels import FlmGemma4DecodeGeometry
from ml_dtypes import bfloat16

from iron.common import DispatchTime, In, InOut, Operator, Param, Unresolvable
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

    geometry: FlmGemma4DecodeGeometry = Param()
    layer_type: LayerType | str = Param()
    x_len: int = Param(derive=lambda op: arg_sizes(op.geometry)["x"], repr=False)
    proj_len: int = Param(derive=lambda op: arg_sizes(op.geometry)["proj"], repr=False)
    rms_len: int = Param(derive=lambda op: arg_sizes(op.geometry)["rms"], repr=False)
    rope_rms_len: int = Param(
        derive=lambda op: arg_sizes(op.geometry)["rope_rms"], repr=False
    )
    kv_len: int = Param(derive=lambda op: arg_sizes(op.geometry)["kv"], repr=False)

    # The runtime sequence's argument order.
    x = InOut(x_len, dtype=bfloat16)
    proj = In(proj_len, dtype=bfloat16)
    rms = In(rms_len, dtype=bfloat16)
    rope_rms = In(rope_rms_len, dtype=bfloat16)
    kv = InOut(kv_len, dtype=bfloat16)
    context_len = DispatchTime()
    max_l = DispatchTime()

    def validate(self) -> None:
        if self.geometry not in RTP_ADDRESSES:
            raise ValueError(
                "DecodeLayer: geometry must be aie.iron.kernels.FLM_GEMMA4_E2B_DECODE or "
                f"FLM_GEMMA4_E4B_DECODE, not {self.geometry!r}"
            )
        if self.layer_type not in LayerType:
            raise ValueError(
                f"DecodeLayer: layer_type must be one of {', '.join(LayerType)}, "
                f"not {self.layer_type!r}"
            )
        self.layer_type = LayerType(self.layer_type)
        self.check_derived("x_len", "proj_len", "rms_len", "rope_rms_len", "kv_len")

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
