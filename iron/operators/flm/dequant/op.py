# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    KernelObjectArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
    SourceArtifact,
)
from iron.common.compilation import InstsBinArtifact, XclbinArtifact
from iron.common.device_utils import get_kernel_dir

from iron.operators.flm.dequant.design import (
    BFP16_GROUP,
    COLS,
    CT_K,
    GROUP,
    K_TILE,
    K_TILE_B,
    M_TILE,
    N_TILE,
    S,
    T,
    qw_bytes_for,
)

BFP16_GROUP_BYTES = 9


@dataclass
class DequantBFP(MLIROperator):
    """q4nx weights to bfp16, packed the way ``flm.GEMM`` reads B.

    See README.md for the layout, the parameters and the constraints.
    """

    K: int
    N: int
    tile_n: int = None
    run_out_features: int = None
    run_period_out_features: int = None
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        if self.K % K_TILE_B:
            raise ValueError(f"K ({self.K}) must be a multiple of {K_TILE_B}")
        if self.N % N_TILE:
            raise ValueError(f"N ({self.N}) must be a multiple of {N_TILE}")
        # Resolve tile_n by flm.GEMM's rule, so an unservable shape fails at
        # construction.
        if self.tile_n is None:
            dev = aie_utils.get_current_device()
            single_k_iter = self.K // K_TILE_B <= 1
            self.tile_n = 128 if (dev.arch == AIEArch.AIE2p and single_k_iter) else 64
        if self.tile_n != N_TILE:
            raise NotImplementedError(
                f"flm.GEMM uses tile_n={self.tile_n} at K={self.K}; this operator "
                f"emits the tile_n={N_TILE} order only. Pass tile_n={N_TILE} to both "
                "if that is what you want the GEMM to use."
            )
        MLIROperator.__init__(self, context=self.context)

    @property
    def _config_tag(self) -> str:
        """Everything that reaches the device configuration, and nothing else.

        The interleave moves offsets inside the runtime sequence, so one xclbin
        covers every value of it.
        """
        dev = aie_utils.get_current_device().resolve().name
        return f"tn{self.tile_n}_{dev}"

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape."""
        return f"FLM_DequantBFP_{self._config_tag}"

    @property
    def name(self) -> str:
        """Stem of the instruction stream, which does depend on the shape.

        The build cache keys on filename, and ``iron.operators.Dequant`` would
        otherwise share this stem.
        """
        base = f"FLM_DequantBFP_K{self.K}_N{self.N}"
        if self.run_out_features is not None:
            base = f"{base}_run{self.run_out_features}p{self.run_period_out_features}"
        return f"{base}_{self._config_tag}"

    @property
    def _reference_shape(self) -> tuple[int, int]:
        """The shape the configuration-only module is emitted at. Its runtime
        sequence is discarded; only its device body reaches the xclbin."""
        return 2 * K_TILE_B, N_TILE * COLS

    def packed_size(self) -> int:
        """Bytes the operator writes: 9 per 8 values."""
        return self.K * self.N // BFP16_GROUP * BFP16_GROUP_BYTES

    def quantized_size(self) -> int:
        """Bytes of q4nx input, counting any interleave gap it strides over."""
        return qw_bytes_for(
            self.K, self.N, self.run_out_features, self.run_period_out_features
        )

    def _mlir_artifact(self, filename, K, N):
        return PythonGeneratedMLIRArtifact(
            filename,
            DesignGenerator(
                self.operator_dir / "design.py",
                "dequant_bfp",
                (
                    aie_utils.get_current_device(),
                    K,
                    N,
                    self.tile_n,
                    self.run_out_features,
                    self.run_period_out_features,
                ),
            ),
        )

    def get_mlir_artifact(self):
        return self._mlir_artifact(f"{self.name}.mlir", self.K, self.N)

    def set_up_artifacts(self) -> None:
        kernels = self.get_kernel_artifacts()
        config_mlir = self._mlir_artifact(
            f"{self.config_name}.mlir", *self._reference_shape
        )
        self.xclbin_artifact = XclbinArtifact(
            f"{self.config_name}.xclbin",
            mlir_input=config_mlir,
            dependencies=[config_mlir] + kernels,
        )
        shape_mlir = self.get_mlir_artifact()
        self.insts_artifact = InstsBinArtifact(
            f"{self.name}.bin",
            mlir_input=shape_mlir,
            # aiecc compiles the cores on the way to an instruction stream.
            dependencies=[shape_mlir] + kernels,
        )
        self.add_artifacts([self.xclbin_artifact, self.insts_artifact])

    def get_kernel_artifacts(self):
        dev = aie_utils.get_current_device()
        if dev.arch != AIEArch.AIE2p:
            raise NotImplementedError("bfp16ebs8 exists only on AIE2P")
        return [
            KernelObjectArtifact(
                f"q4nx_dequant_{get_kernel_dir(dev)}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.kernels_dir / "generic" / "q4nx_dequant.cc"
                    )
                ],
                extra_flags=[
                    f"-DQ4NX_M_TILE={M_TILE}",
                    f"-DQ4NX_K_TILE={K_TILE}",
                    f"-DQ4NX_GROUP={GROUP}",
                    f"-DQ4NX_CT_K={CT_K}",
                    f"-DQ4NX_S={S}",
                    f"-DQ4NX_T={T}",
                ],
            )
        ]

    def get_arg_spec(self):
        # Both buffers are declared in bytes: a q4nx block interleaves three
        # tables at 5 bits per weight, and a bfp16 block is 9 bytes for 8.
        return [
            AIERuntimeArgSpec("in", (self.quantized_size(),), dtype=np.uint8),
            AIERuntimeArgSpec("out", (self.packed_size(),), dtype=np.uint8),
        ]

    def reference(self, qw):
        """CPU reference, bit-exact against the device."""
        from iron.operators.flm.dequant.reference import reference

        return reference(qw, self.K, self.N)
