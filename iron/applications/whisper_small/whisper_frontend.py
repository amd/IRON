# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import gc
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import torch
import torch.nn.functional as F
from safetensors import safe_open

from iron.common.context import AIEContext
from iron.operators.gelu.op import GELU
from iron.operators.gemm.op import GEMM

from whisper_common import FRAMES, MELS, SEQ, STATE

K1_REAL = 3 * MELS
K1_PAD = 256
K2 = 3 * STATE
CONV2_M_PAD = 128


def make_context(
    build_root: Path,
    name: str,
) -> AIEContext:
    path = build_root / name

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    context = AIEContext()
    context.build_dir = path

    return context


def load_frontend_weights(
    checkpoint: Path,
) -> tuple[torch.Tensor, ...]:
    with safe_open(
        str(checkpoint),
        framework="pt",
        device="cpu",
    ) as handle:
        w1 = handle.get_tensor("model.encoder.conv1.weight").cpu()

        b1 = handle.get_tensor("model.encoder.conv1.bias").float().cpu()

        w2 = handle.get_tensor("model.encoder.conv2.weight").cpu()

        b2 = handle.get_tensor("model.encoder.conv2.bias").float().cpu()
        positions = (
            handle.get_tensor("model.encoder.embed_positions.weight")
            .float()
            .cpu()[:SEQ]
        )

    return w1, b1, w2, b2, positions


def run_gelu(
    x: torch.Tensor,
    size: int,
    tile_size: int,
    context: AIEContext,
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    op = GELU(
        size=size,
        num_aie_columns=1,
        num_channels=1,
        tile_size=tile_size,
        context=context,
    )

    op.compile()
    fn = op.get_callable()

    try:
        inp = tensor_class.from_torch(x.to(torch.bfloat16).flatten().contiguous())

        out = tensor_class(
            (size,),
            dtype=np.dtype("bfloat16"),
        )

        fn(
            inp,
            out,
        )

        result = out.to_torch().float().clone()

        del out
        del inp

        return result

    finally:
        del fn
        del op
        gc.collect()


def run_frontend(
    mel: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> torch.Tensor:
    if mel.shape != (1, MELS, FRAMES):
        raise ValueError(
            f"Expected mel shape {(1, MELS, FRAMES)}, " f"got {tuple(mel.shape)}"
        )

    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    w1, b1, w2, b2, positions = load_frontend_weights(checkpoint)

    # ========================================================
    # Conv1
    # ========================================================

    mel_bf16 = mel.to(torch.bfloat16)
    xt = mel_bf16[0].T

    xpad = F.pad(
        xt.float(),
        (0, 0, 1, 1),
    )

    a1_real = torch.stack(
        [
            torch.cat(
                (
                    xpad[t],
                    xpad[t + 1],
                    xpad[t + 2],
                )
            )
            for t in range(FRAMES)
        ]
    ).to(torch.bfloat16)

    b1_real = (
        w1.float()
        .permute(2, 1, 0)
        .contiguous()
        .reshape(
            K1_REAL,
            STATE,
        )
        .to(torch.bfloat16)
    )

    a1 = torch.zeros(
        (
            FRAMES,
            K1_PAD,
        ),
        dtype=torch.bfloat16,
    )

    a1[:, :K1_REAL] = a1_real

    b1_gemm = torch.zeros(
        (
            K1_PAD,
            STATE,
        ),
        dtype=torch.bfloat16,
    )

    b1_gemm[:K1_REAL] = b1_real

    conv1 = GEMM(
        M=FRAMES,
        K=K1_PAD,
        N=STATE,
        num_aie_columns=1,
        tile_m=32,
        tile_k=32,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "conv1",
        ),
    )

    conv1.compile()
    conv1_fn = conv1.get_callable()

    try:
        a1_npu = tensor_class.from_torch(a1)
        b1_npu = tensor_class.from_torch(b1_gemm)

        c1_npu = tensor_class(
            (
                FRAMES,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        conv1_fn(
            a1_npu,
            b1_npu,
            c1_npu,
        )

        conv1_tm = c1_npu.to_torch().float().clone() + b1

        del c1_npu
        del b1_npu
        del a1_npu

    finally:
        del conv1_fn
        del conv1
        gc.collect()

    # ========================================================
    # GELU1
    # ========================================================

    gelu1_tm = run_gelu(
        conv1_tm,
        size=FRAMES * STATE,
        tile_size=8192,
        context=make_context(
            build_root,
            "gelu1",
        ),
    ).reshape(
        FRAMES,
        STATE,
    )

    # ========================================================
    # Conv2
    # ========================================================

    gelu1_out = gelu1_tm.T.unsqueeze(0).contiguous()

    x2 = gelu1_out.to(torch.bfloat16)
    xt2 = x2[0].T

    xpad2 = F.pad(
        xt2.float(),
        (0, 0, 1, 1),
    )

    a2_logical = torch.stack(
        [
            torch.cat(
                (
                    xpad2[2 * o],
                    xpad2[2 * o + 1],
                    xpad2[2 * o + 2],
                )
            )
            for o in range(SEQ)
        ]
    ).to(torch.bfloat16)

    a2 = torch.zeros(
        (
            CONV2_M_PAD,
            K2,
        ),
        dtype=torch.bfloat16,
    )

    a2[:SEQ] = a2_logical

    b2_gemm = (
        w2.float()
        .permute(2, 1, 0)
        .contiguous()
        .reshape(
            K2,
            STATE,
        )
        .to(torch.bfloat16)
    )

    conv2 = GEMM(
        M=CONV2_M_PAD,
        K=K2,
        N=STATE,
        num_aie_columns=1,
        tile_m=32,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "conv2",
        ),
    )

    conv2.compile()
    conv2_fn = conv2.get_callable()

    try:
        a2_npu = tensor_class.from_torch(a2)
        b2_npu = tensor_class.from_torch(b2_gemm)

        c2_npu = tensor_class(
            (
                CONV2_M_PAD,
                STATE,
            ),
            dtype=np.dtype("bfloat16"),
        )

        conv2_fn(
            a2_npu,
            b2_npu,
            c2_npu,
        )

        conv2_gemm = c2_npu.to_torch().float().clone()[:SEQ].contiguous()

        conv2_tm = conv2_gemm + b2

        del c2_npu
        del b2_npu
        del a2_npu

    finally:
        del conv2_fn
        del conv2
        gc.collect()

    # ========================================================
    # GELU2
    # ========================================================

    tokens = run_gelu(
        conv2_tm,
        size=SEQ * STATE,
        tile_size=STATE,
        context=make_context(
            build_root,
            "gelu2",
        ),
    ).reshape(
        SEQ,
        STATE,
    )

    return tokens + positions
