# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Dict

import aie.utils as aie_utils
from aie.utils.npukernel import NPUKernel

from iron.common import (
    AIERuntimeArgSpec,
    DesignGenerator,
    InstsBinArtifact,
    MLIROperator,
    PythonGeneratedMLIRArtifact,
    RemoteFileArtifact,
)

from iron.operators.flm.packing import pack_b
from iron.operators.flm.gemm.design import Epilogue, K_TILE, S, T
from iron.operators.flm.mm_prebuilt.design import MIN_K, MIN_M, N_TILE

# The FastFlowLM revision the overlay is taken from. A commit SHA rather than
# a branch, so the digest below stays valid.
FASTFLOWLM_COMMIT = "f81eba7140decef5e4eda670d02a91b9d6402ee9"
XCLBIN_PATH = "src/xclbins/Gemma4-E4B-IT-NPU2/mm.xclbin"
XCLBIN_URL = (
    f"https://raw.githubusercontent.com/ROCm/FastFlowLM/{FASTFLOWLM_COMMIT}/"
    f"{XCLBIN_PATH}"
)
XCLBIN_SHA256 = "6f1e5507b84d4545536c9b8281002d0e0e10ed241f8593cb4db50eee63876e5f"
XCLBIN_KERNEL_NAME = "MLIR_AIE"

# The overlay's k slice. Its B layout is fixed by the shipped binary, so unlike
# flm.gemm this is not a tuning knob.
CT_K = K_TILE


@dataclass
class MMPrebuilt(MLIROperator):
    """bf16 GEMM running FastFlowLM's shipped ``mm`` overlay unmodified.

    The overlay is downloaded rather than built: it exists only as a binary
    xclbin. This operator supplies the other half of a dispatch -- the runtime
    parameters and the shim DMA transfers -- so that the shipped kernel can be
    measured against :class:`iron.operators.flm.GEMM`, the IRON port of it, at
    the same shapes and on the same inputs.

    NPU2 only: the overlay is built for the 8-column grid.

    B must be pre-packed; use :meth:`pack_B`.

    Note the epilogue here is selected through a RUNTIME parameter, because one
    overlay serves every projection in a model. ``flm.GEMM`` bakes it in at
    compile time instead, which is what lets its inner loop be branch-free; the
    cost is one build per activation rather than one build for all of them.
    """

    M: int
    K: int
    N: int
    # Activation, selected through a runtime parameter rather than at compile
    # time as in flm.GEMM.
    epilogue: Epilogue = Epilogue.NONE
    # Optional (min, max) applied after the activation.
    clamp: tuple[float, float] | None = None
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "epilogue": "epi",
    }

    def __post_init__(self):
        for name, value, unit in (
            ("M", self.M, MIN_M),
            ("K", self.K, MIN_K),
            ("N", self.N, N_TILE),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")
        self.epilogue = Epilogue(self.epilogue)
        if self.clamp is not None and self.clamp[0] > self.clamp[1]:
            raise ValueError(
                f"clamp min ({self.clamp[0]}) must be <= max ({self.clamp[1]})"
            )
        device = aie_utils.get_current_device()
        if device.resolve().name != "npu2" or device.cols < 8:
            raise NotImplementedError(
                "flm.MMPrebuilt runs a prebuilt NPU2 overlay and needs the 8 "
                f"columns of NPU2 (aie2p); got {device.resolve().name!r} with "
                f"{device.cols} columns"
            )

        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        """Artifact stem. Prefixed for the same reason as flm.GEMM's."""
        return f"FLM_{super().name}"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "mm_prebuilt",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "M": self.M,
                    "K": self.K,
                    "N": self.N,
                    "epilogue": self.epilogue,
                    "clamp": self.clamp,
                },
            ),
        )

    def get_kernel_artifacts(self):
        # None to build: every core program is inside the downloaded xclbin.
        return []

    def set_up_artifacts(self) -> None:
        mlir_artifact = self.get_mlir_artifact()
        self.insts_artifact = InstsBinArtifact(
            f"{self.name}.bin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact],
        )
        self.xclbin_artifact = RemoteFileArtifact(
            f"flm_mm_{FASTFLOWLM_COMMIT[:8]}.xclbin",
            url=XCLBIN_URL,
            sha256=XCLBIN_SHA256,
        )
        self.add_artifacts([self.insts_artifact, self.xclbin_artifact])

    def get_callable(self) -> Callable[..., Any]:
        npu_kernel = NPUKernel(
            xclbin_path=self.xclbin_artifact.filename,
            kernel_name=XCLBIN_KERNEL_NAME,
            insts_path=self.insts_artifact.filename,
        )
        handle = aie_utils.DefaultNPURuntime.load(npu_kernel)

        def call(*args):
            return aie_utils.DefaultNPURuntime.run(handle, list(args))

        return call

    def pack_B(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into the order the B
        transfers read. Returns a flat bf16 tensor.

        NOT the same layout ``flm.GEMM.pack_B`` produces: the overlay's own
        loop nest sweeps the two within-block k axes in the opposite order
        from ``mm_fused_mmul_2x2``'s, so this needs ``overlay_order`` -- see
        ``pack_b``'s docstring.
        """
        return pack_b(
            B, k_tile=K_TILE, n_tile=N_TILE, s=S, t=T, ct_k=CT_K, overlay_order=True
        )

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # A
            # B, pre-packed by pack_B -- same element count, different order.
            AIERuntimeArgSpec("in", (self.K, self.N)),  # B (weights)
            AIERuntimeArgSpec("out", (self.M, self.N)),  # C
        ]

    def reference(self, A, B):
        """CPU reference: ``C = epilogue(A @ B)``."""
        from iron.operators.flm.gemm.reference import reference

        return reference(A, B, self.epilogue, self.clamp)
