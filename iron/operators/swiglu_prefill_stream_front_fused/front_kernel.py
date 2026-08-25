from collections.abc import Sequence
from dataclasses import dataclass

from snaxc.ir.tsl import Stride, TiledStride, TiledStridedLayout
from xdsl.dialects.builtin import (
    AnyDenseElement,
    FunctionType,
)
from xdsl.dialects.func import CallOp
from xdsl.irdl import Operation

from stream.compiler.dialects.stream import ComputationNodeOp
from stream.compiler.kernels.aie_kernel import MAC_ROWS_BFP16, AIEKernelWithZeroing


# TODO
@dataclass
class SwigluFrontFusedKernel(AIEKernelWithZeroing):
    m: int
    k: int
    n: int

    @property
    def zero_name(self) -> str:
        # TODO actually write this kernel
        return f"swiglu_fused_zero_{self.m}_{self.k}_{self.n}"

    def zero_type(self, op: ComputationNodeOp) -> FunctionType:
        return FunctionType.from_lists(inputs=[op.inputs[2].type], outputs=[])

    @property
    def linkwith_name(self) -> str:
        # TODO actually write this kernel
        return f"swiglu_fused_core_{self.m}_{self.k}_{self.n}"

    @property
    def function_name(self) -> str:
        return f"swiglu_front_fused_{self.m}_{self.k}_{self.n}"

    def operand_layouts(self) -> Sequence[TiledStridedLayout]:
        # TODO rework?
        # Intrinsic dimensions of the MAC the kernel was built for. mm.cc takes
        # 8x8x8 when bf16 matmuls are emulated on the bfp16 MACs and 4x8x8 when
        # they are not, so this has to agree with how the object was compiled.
        r = 8  # ~m
        s = 8  # ~k
        t = 8  # ~n
        # Tiled kernel dimensions:
        mt = self.m // r
        kt = self.k // s
        nt = self.n // t
        return [
            # A: mxk, tiles of rxs
            TiledStridedLayout(
                [
                    TiledStride([Stride(r * s * kt, mt), Stride(s, r)]),
                    TiledStride([Stride(r * s, kt), Stride(1, s)]),
                ]
            ),
            # B: kxn, tiles of sxt
            TiledStridedLayout(
                [
                    TiledStride([Stride(s * t * nt, kt), Stride(t, s)]),
                    TiledStride([Stride(s * t, nt), Stride(1, t)]),
                ]
            ),
            # C: mxn, tiles of rxt
            TiledStridedLayout(
                [
                    TiledStride([Stride(r * t * nt, mt), Stride(t, r)]),
                    TiledStride([Stride(r * t, nt), Stride(1, t)]),
                ]
            ),
        ]

    def function_type(self, op: ComputationNodeOp) -> FunctionType:
        assert op.output is not None
        return FunctionType.from_lists(
            inputs=[op.inputs[0].type]  # A
            + [op.inputs[1].type]  # b
            + [op.inputs[2].type],  # c
            outputs=[],
        )

    def function_call(self, op: ComputationNodeOp) -> Sequence[Operation]:
        assert op.output is not None
        return [
            CallOp(self.function_name, [op.inputs[0], op.inputs[1], op.inputs[2]], []),
        ]
