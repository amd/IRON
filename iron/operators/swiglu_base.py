# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16

from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from aie.utils.npukernel import NPUKernel


def chain_swiglu_artifacts(op, sub_ops):
    """Chain xclbin artifacts for a SwiGLU operator's sub-operators.

    Handles the shared xclbin chaining pattern: each sub-operator's xclbin is
    linked to the previous one via xclbin_input/dependencies, with sequential
    kernel IDs. The final xclbin becomes the combined xclbin for the operator.

    All xclbin/insts artifacts are stored on ``op`` as ``{name}_xclbin`` and
    ``{name}_insts`` attributes (e.g. ``gemv_1_xclbin``, ``silu_insts``).

    Args:
        op: The SwiGLU operator instance (SwiGLUDecode or SwiGLUPrefill).
        sub_ops: List of ``(name, kernel_id, sub_operator)`` tuples in chain
            order.  *name* is used for xclbin-instance-name and the attribute
            prefix; *kernel_id* is the hex kernel ID string (e.g. ``"0x901"``).
    """
    artifacts = []
    prev_xclbin = None

    for name, kernel_id, sub_op in sub_ops:
        xclbin, insts = sub_op.get_artifacts(prefix=f"swiglu_{name}_")
        xclbin.extra_flags += [
            f"--xclbin-instance-name=swiglu_{name}",
            f"--xclbin-kernel-id={kernel_id}",
        ]
        xclbin.kernel_name = f"swiglu_{name}"
        if prev_xclbin is not None:
            xclbin.xclbin_input = prev_xclbin
            xclbin.dependencies.add(prev_xclbin)

        # Only the insts are appended for intermediate steps; the xclbin is
        # pulled in as a dependency of the next xclbin in the chain.
        artifacts.append(insts)
        setattr(op, f"{name}_xclbin", xclbin)
        setattr(op, f"{name}_insts", insts)
        prev_xclbin = xclbin

    # The last xclbin in the chain is the combined xclbin.
    artifacts.append(prev_xclbin)
    op.combined_xclbin = prev_xclbin
    op.add_artifacts(artifacts)


class _SwiGLUCallable:
    """Base callable for SwiGLU decode/prefill operators.

    Handles the shared 5-step execution pattern:
      1. matmul(weights_1, input) -> left
      2. matmul(weights_2, input) -> right   (reuses matmul_1 kernel)
      3. SiLU(left) -> left_swished
      4. EltwiseMul(left_swished, right) -> intermediate
      5. matmul(weights_3, intermediate) -> output

    Subclasses provide the matmul argument order (GEMV vs GEMM) and
    buffer configuration via __init__ parameters.
    """

    def __init__(
        self,
        op,
        matmul_1_prefix,
        matmul_2_prefix,
        transpose_weights,
        intermediate_shape,
    ):
        """
        Args:
            op: The parent SwiGLU operator with compiled artifacts.
            matmul_1_prefix: Attribute prefix for the first matmul (e.g. "gemv_1" or "gemm_1").
            matmul_2_prefix: Attribute prefix for the second matmul (e.g. "gemv_2" or "gemm_2").
            transpose_weights: Whether to transpose weights before uploading.
            intermediate_shape: Shape tuple for intermediate buffers.
        """

        def create_callable(xclbin_path, kernel_name, insts_artifact):
            return NPUKernel(
                xclbin_path=xclbin_path,
                kernel_name=kernel_name,
                insts_path=insts_artifact.filename,
            )

        combined = op.combined_xclbin.filename
        self.matmul_1_callable = create_callable(
            combined,
            getattr(op, f"{matmul_1_prefix}_xclbin").kernel_name,
            getattr(op, f"{matmul_1_prefix}_insts"),
        )
        self.silu_callable = create_callable(
            combined,
            op.silu_xclbin.kernel_name,
            op.silu_insts,
        )
        self.eltwise_mul_callable = create_callable(
            combined,
            op.eltwise_mul_xclbin.kernel_name,
            op.eltwise_mul_insts,
        )
        self.matmul_2_callable = create_callable(
            combined,
            getattr(op, f"{matmul_2_prefix}_xclbin").kernel_name,
            getattr(op, f"{matmul_2_prefix}_insts"),
        )

        # Allocate and upload weights
        w_fn = (lambda w: w.T) if transpose_weights else (lambda w: w)
        self.weights_1 = XRTTensor.from_torch(w_fn(op.weights_1))
        self.weights_2 = XRTTensor.from_torch(w_fn(op.weights_2))
        self.weights_3 = XRTTensor.from_torch(w_fn(op.weights_3))

        # Allocate intermediate buffers
        self.left = XRTTensor(intermediate_shape, dtype=bfloat16)
        self.right = XRTTensor(intermediate_shape, dtype=bfloat16)
        self.left_swished = XRTTensor(intermediate_shape, dtype=bfloat16)
        self.intermediate = XRTTensor(intermediate_shape, dtype=bfloat16)

    def _call_matmul(self, matmul_callable, weight, input_buf, output_buf):
        """Call a matmul kernel. Subclasses override for GEMV vs GEMM arg order."""
        raise NotImplementedError

    def __call__(self, input_buf, output_buf):
        # Sync input in case caller wrote to it via torch_view() between calls.
        # Weights and internal buffers stay on device; the XRT runtime syncs all
        # args to device automatically before each kernel invocation.
        input_buf.to("npu")

        # 1. matmul(weights_1, input) -> left
        self._call_matmul(self.matmul_1_callable, self.weights_1, input_buf, self.left)

        # 2. matmul(weights_2, input) -> right
        # Reuses matmul_1 kernel: both gate and up projections share the same config.
        self._call_matmul(self.matmul_1_callable, self.weights_2, input_buf, self.right)

        # 3. SiLU(left) -> left_swished
        self.silu_callable(self.left, self.left_swished)

        # 4. EltwiseMul(left_swished, right) -> intermediate
        self.eltwise_mul_callable(self.left_swished, self.right, self.intermediate)

        # 5. matmul(weights_3, intermediate) -> output
        self._call_matmul(
            self.matmul_2_callable, self.weights_3, self.intermediate, output_buf
        )
