# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import gc
import os
import subprocess
import sys
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import torch
import torch.nn.functional as F
from safetensors import safe_open

from iron.common.context import AIEContext
from iron.operators.gelu.op import GELU
from iron.operators.gemm.op import GEMM
from iron.operators.layer_norm.op import LayerNorm
from iron.operators.softmax.op import Softmax

from whisper_common import (
    APP_DIR,
    ARTIFACT_ROOT,
    BLOCKS,
    HEAD_DIM,
    HEADS,
    MLP,
    SCALE,
    SEQ,
    STATE,
    whisper_checkpoint,
)

from whisper_frontend import run_frontend

BLOCK_WEIGHT_MAP = {
    "attn_ln.weight": "self_attn_layer_norm.weight",
    "attn_ln.bias": "self_attn_layer_norm.bias",
    "attn.query.weight": "self_attn.q_proj.weight",
    "attn.query.bias": "self_attn.q_proj.bias",
    "attn.key.weight": "self_attn.k_proj.weight",
    "attn.value.weight": "self_attn.v_proj.weight",
    "attn.value.bias": "self_attn.v_proj.bias",
    "attn.out.weight": "self_attn.out_proj.weight",
    "attn.out.bias": "self_attn.out_proj.bias",
    "mlp_ln.weight": "final_layer_norm.weight",
    "mlp_ln.bias": "final_layer_norm.bias",
    "mlp.0.weight": "fc1.weight",
    "mlp.0.bias": "fc1.bias",
    "mlp.2.weight": "fc2.weight",
    "mlp.2.bias": "fc2.bias",
}


def load_block_weights(
    checkpoint: Path,
    block: int,
) -> dict[str, torch.Tensor]:
    prefix = f"model.encoder.layers.{block}."
    weights = {}

    with safe_open(
        str(checkpoint),
        framework="pt",
        device="cpu",
    ) as handle:
        available = set(handle.keys())

        for local_name, checkpoint_name in BLOCK_WEIGHT_MAP.items():
            full_name = prefix + checkpoint_name

            if full_name not in available:
                raise KeyError(f"Missing checkpoint tensor: {full_name}")

            value = handle.get_tensor(full_name).cpu()

            # Preserve the validated Phoenix weight preparation.
            if local_name.endswith(".weight") and value.ndim == 2:
                value = value.to(torch.float16)
            else:
                value = value.float()

            weights[local_name] = value

    return weights


def make_context(
    build_root: Path,
    name: str,
) -> AIEContext:
    root = build_root / name
    root.mkdir(
        parents=True,
        exist_ok=True,
    )

    context = AIEContext()
    context.build_dir = root
    return context


def split_heads(x: torch.Tensor) -> torch.Tensor:
    return (
        x.reshape(
            SEQ,
            HEADS,
            HEAD_DIM,
        )
        .permute(1, 0, 2)
        .contiguous()
    )


def merge_heads(x: torch.Tensor) -> torch.Tensor:
    return (
        x.permute(1, 0, 2)
        .contiguous()
        .reshape(
            SEQ,
            STATE,
        )
    )


def run_layernorm(
    fn,
    x: torch.Tensor,
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    inp = tensor_class.from_torch(x.to(torch.bfloat16).flatten().contiguous())

    out = tensor_class(
        (SEQ * STATE,),
        dtype=np.dtype("bfloat16"),
    )

    fn(
        inp,
        out,
    )

    result = (
        out.to_torch()
        .float()
        .clone()
        .reshape(
            SEQ,
            STATE,
        )
    )

    del out
    del inp

    return result


def run_gemm(
    fn,
    a: torch.Tensor,
    b: torch.Tensor,
    shape: tuple[int, ...],
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    a_npu = tensor_class.from_torch(a.to(torch.bfloat16).contiguous())

    b_npu = tensor_class.from_torch(b.to(torch.bfloat16).contiguous())

    c_npu = tensor_class(
        shape,
        dtype=np.dtype("bfloat16"),
    )

    fn(
        a_npu,
        b_npu,
        c_npu,
    )

    result = c_npu.to_torch().float().clone()

    del c_npu
    del b_npu
    del a_npu

    return result


def run_attention(
    x: torch.Tensor,
    weights: dict[str, torch.Tensor],
    build_root: Path,
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    ln = LayerNorm(
        size=SEQ * STATE,
        num_aie_columns=1,
        num_channels=1,
        tile_size=STATE,
        context=make_context(
            build_root,
            "ln768",
        ),
    )

    gemm768 = GEMM(
        M=SEQ,
        K=STATE,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "gemm768",
        ),
    )

    score_gemm = GEMM(
        M=SEQ,
        K=HEAD_DIM,
        N=SEQ,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "score-gemm",
        ),
    )

    value_gemm = GEMM(
        M=SEQ,
        K=SEQ,
        N=HEAD_DIM,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "value-gemm",
        ),
    )

    softmax = Softmax(
        rows=HEADS * SEQ,
        cols=SEQ,
        num_aie_columns=1,
        num_channels=1,
        context=make_context(
            build_root,
            "softmax",
        ),
    )

    ln.compile()
    ln_fn = ln.get_callable()

    gemm768.compile()
    gemm768_fn = gemm768.get_callable()

    score_gemm.compile()
    score_gemm_fn = score_gemm.get_callable()

    value_gemm.compile()
    value_gemm_fn = value_gemm.get_callable()

    softmax.compile()
    softmax_fn = softmax.get_callable()

    try:
        bare = run_layernorm(
            ln_fn,
            x,
        )

        normalized = bare * weights["attn_ln.weight"] + weights["attn_ln.bias"]

        def projection(
            weight_name: str,
            bias_name: str | None = None,
        ) -> torch.Tensor:
            result = run_gemm(
                gemm768_fn,
                normalized,
                weights[weight_name].float().T.contiguous(),
                (SEQ, STATE),
            )

            if bias_name is not None:
                result = result + weights[bias_name].float()

            return result

        q = projection(
            "attn.query.weight",
            "attn.query.bias",
        )

        k = projection(
            "attn.key.weight",
        )

        v = projection(
            "attn.value.weight",
            "attn.value.bias",
        )

        qh = split_heads(q)
        kh = split_heads(k)
        vh = split_heads(v)

        scores = torch.empty(
            (HEADS, SEQ, SEQ),
            dtype=torch.float32,
        )

        for head in range(HEADS):
            scores[head] = (
                run_gemm(
                    score_gemm_fn,
                    qh[head],
                    kh[head].transpose(0, 1).contiguous(),
                    (SEQ, SEQ),
                )
                * SCALE
            )

        soft_in = tensor_class.from_torch(
            scores.to(torch.bfloat16).contiguous().flatten()
        )

        soft_out = tensor_class(
            (HEADS * SEQ * SEQ,),
            dtype=np.dtype("bfloat16"),
        )

        softmax_fn(
            soft_in,
            soft_out,
        )

        probs = (
            soft_out.to_torch()
            .float()
            .clone()
            .reshape(
                HEADS,
                SEQ,
                SEQ,
            )
        )

        del soft_out
        del soft_in

        heads = []

        for head in range(HEADS):
            heads.append(
                run_gemm(
                    value_gemm_fn,
                    probs[head],
                    vh[head],
                    (SEQ, HEAD_DIM),
                )
            )

        merged = merge_heads(
            torch.stack(
                heads,
                dim=0,
            )
        )

        projected = run_gemm(
            gemm768_fn,
            merged,
            weights["attn.out.weight"].float().T.contiguous(),
            (SEQ, STATE),
        )

        projected = projected + weights["attn.out.bias"].float()

        return x + projected

    finally:
        del softmax_fn
        del softmax
        del value_gemm_fn
        del value_gemm
        del score_gemm_fn
        del score_gemm
        del gemm768_fn
        del gemm768
        del ln_fn
        del ln

        gc.collect()


def run_mlp(
    x: torch.Tensor,
    weights: dict[str, torch.Tensor],
    build_root: Path,
) -> torch.Tensor:
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS

    ln = LayerNorm(
        size=SEQ * STATE,
        num_aie_columns=1,
        num_channels=1,
        tile_size=STATE,
        context=make_context(
            build_root,
            "mlp-ln768",
        ),
    )

    fc1 = GEMM(
        M=SEQ,
        K=STATE,
        N=MLP,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "mlp-fc1",
        ),
    )

    gelu = GELU(
        size=SEQ * MLP,
        num_aie_columns=1,
        num_channels=1,
        tile_size=8192,
        context=make_context(
            build_root,
            "mlp-gelu",
        ),
    )

    fc2 = GEMM(
        M=SEQ,
        K=MLP,
        N=STATE,
        num_aie_columns=1,
        tile_m=16,
        tile_k=64,
        tile_n=64,
        prio_accuracy=True,
        emulate_bf16_mmul_with_bfp16=False,
        context=make_context(
            build_root,
            "mlp-fc2",
        ),
    )

    ln.compile()
    ln_fn = ln.get_callable()

    fc1.compile()
    fc1_fn = fc1.get_callable()

    gelu.compile()
    gelu_fn = gelu.get_callable()

    fc2.compile()
    fc2_fn = fc2.get_callable()

    try:
        bare = run_layernorm(
            ln_fn,
            x,
        )

        normalized = bare * weights["mlp_ln.weight"] + weights["mlp_ln.bias"]

        up = run_gemm(
            fc1_fn,
            normalized,
            weights["mlp.0.weight"].float().T.contiguous(),
            (SEQ, MLP),
        )

        up = up + weights["mlp.0.bias"].float()

        gelu_in = tensor_class.from_torch(up.to(torch.bfloat16).flatten().contiguous())

        gelu_out = tensor_class(
            (SEQ * MLP,),
            dtype=np.dtype("bfloat16"),
        )

        gelu_fn(
            gelu_in,
            gelu_out,
        )

        activation = (
            gelu_out.to_torch()
            .float()
            .clone()
            .reshape(
                SEQ,
                MLP,
            )
        )

        del gelu_out
        del gelu_in

        down = run_gemm(
            fc2_fn,
            activation,
            weights["mlp.2.weight"].float().T.contiguous(),
            (SEQ, STATE),
        )

        down = down + weights["mlp.2.bias"].float()

        return x + down

    finally:
        del fc2_fn
        del fc2
        del gelu_fn
        del gelu
        del fc1_fn
        del fc1
        del ln_fn
        del ln

        gc.collect()


def run_encoder_block(
    block: int,
    x: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> torch.Tensor:
    if not 0 <= block < 12:
        raise ValueError(f"block must be 0..11, got {block}")

    if x.shape != (SEQ, STATE):
        raise ValueError(
            f"Expected input shape {(SEQ, STATE)}, " f"got {tuple(x.shape)}"
        )

    weights = load_block_weights(
        checkpoint,
        block,
    )

    x = run_attention(
        x.float(),
        weights,
        build_root,
    )

    x = run_mlp(
        x,
        weights,
        build_root,
    )

    return x


def run_final_layernorm(
    x: torch.Tensor,
    checkpoint: Path,
    build_root: Path,
) -> torch.Tensor:
    """Run Whisper's final encoder LayerNorm on the NPU."""

    if x.shape != (SEQ, STATE):
        raise ValueError(
            f"Expected input shape {(SEQ, STATE)}, " f"got {tuple(x.shape)}"
        )

    with safe_open(
        str(checkpoint),
        framework="pt",
        device="cpu",
    ) as handle:
        gamma = handle.get_tensor("model.encoder.layer_norm.weight").float().cpu()

        beta = handle.get_tensor("model.encoder.layer_norm.bias").float().cpu()

    op = LayerNorm(
        size=SEQ * STATE,
        num_aie_columns=1,
        num_channels=1,
        tile_size=STATE,
        context=make_context(
            build_root,
            "ln768",
        ),
    )

    op.compile()
    fn = op.get_callable()

    try:
        bare = run_layernorm(
            fn,
            x,
        )

        return bare * gamma + beta

    finally:
        del fn
        del op

        gc.collect()


FRONTEND_REFERENCE = ARTIFACT_ROOT / "whisper-small-frontend-reference-128.pt"

ENCODER_REFERENCE = ARTIFACT_ROOT / "whisper-small-encoder-reference-frontend128.pt"


def run_reference_script(
    script: str,
    *args: str | Path,
) -> None:
    """Run one FP32 reference generator."""

    command = [
        sys.executable,
        str(APP_DIR / script),
        *(str(arg) for arg in args),
    ]

    print()
    print("=" * 88)
    print("RUN:")
    print(" ".join(command))
    print("=" * 88)
    print()

    subprocess.run(
        command,
        check=True,
    )


def prepare_reference(
    wav: Path,
) -> None:
    """Generate the real-audio FP32 frontend and encoder oracle."""

    # Validate checkpoint configuration before spawning children.
    checkpoint = whisper_checkpoint()

    print(
        "Whisper checkpoint:",
        checkpoint,
    )

    wav = wav.expanduser()

    if not wav.is_file():
        raise FileNotFoundError(f"Whisper validation WAV not found: {wav}")

    print(
        "Validation WAV:",
        wav,
    )

    run_reference_script(
        "whisper_reference_frontend.py",
        "--wav",
        wav,
    )

    if not FRONTEND_REFERENCE.is_file():
        raise FileNotFoundError(
            f"Frontend reference was not created: " f"{FRONTEND_REFERENCE}"
        )

    run_reference_script(
        "whisper_reference_encoder.py",
    )

    if not ENCODER_REFERENCE.is_file():
        raise FileNotFoundError(
            f"Encoder reference was not created: " f"{ENCODER_REFERENCE}"
        )

    print()
    print("Reference preparation: PASS")


def run_phoenix(
    frontend_reference: Path | None = None,
    encoder_reference: Path | None = None,
    output_root: Path | None = None,
) -> None:
    """Run the Phoenix frontend and complete Whisper encoder."""

    whisper_checkpoint()

    frontend_reference = (
        frontend_reference.resolve()
        if frontend_reference is not None
        else FRONTEND_REFERENCE
    )

    encoder_reference = (
        encoder_reference.resolve()
        if encoder_reference is not None
        else ENCODER_REFERENCE
    )

    output_root = output_root.resolve() if output_root is not None else ARTIFACT_ROOT

    output_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    if not frontend_reference.is_file():
        raise FileNotFoundError(
            "Frontend reference is missing. "
            "Run with --prepare-reference or --all first."
        )

    if not encoder_reference.is_file():
        raise FileNotFoundError(
            "Encoder reference is missing. "
            "Run with --prepare-reference or --all first."
        )

    # ========================================================
    # Phoenix frontend
    # ========================================================

    checkpoint = whisper_checkpoint()

    frontend = torch.load(
        frontend_reference,
        map_location="cpu",
        weights_only=True,
    )

    if "mel" not in frontend:
        raise KeyError("Frontend reference does not contain a " "'mel' tensor")

    x = run_frontend(
        mel=frontend["mel"].float(),
        checkpoint=checkpoint,
        build_root=output_root / "frontend",
    )

    # ========================================================
    # Transformer encoder
    # ========================================================

    for block in range(BLOCKS):
        print()
        print("#" * 88)
        print(f"PHOENIX WHISPER ENCODER BLOCK " f"{block}/{BLOCKS - 1}")
        print("#" * 88)

        x = run_encoder_block(
            block=block,
            x=x,
            checkpoint=checkpoint,
            build_root=output_root / f"block{block}",
        )

    # ========================================================
    # Final encoder LayerNorm
    # ========================================================

    x = run_final_layernorm(
        x=x,
        checkpoint=checkpoint,
        build_root=output_root / "final-layernorm",
    )

    reference = torch.load(
        encoder_reference,
        map_location="cpu",
        weights_only=True,
    )

    if "encoder_output" not in reference:
        raise KeyError(
            "Encoder reference does not contain an " "'encoder_output' tensor"
        )

    expected = reference["encoder_output"].float()

    if expected.shape != x.shape:
        raise ValueError(
            f"Encoder reference shape {tuple(expected.shape)} "
            f"does not match output shape {tuple(x.shape)}"
        )

    error = x.float() - expected

    rmse = torch.sqrt((error * error).mean()).item()

    reference_norm = torch.linalg.vector_norm(expected).item()

    error_norm = torch.linalg.vector_norm(error).item()

    nrmse = error_norm / reference_norm if reference_norm != 0 else float("nan")

    cosine = F.cosine_similarity(
        x.float().flatten().unsqueeze(0),
        expected.flatten().unsqueeze(0),
    ).item()

    print()
    print("Final encoder vs FP32 reference")
    print(
        "  NRMSE % :",
        100.0 * nrmse,
    )
    print(
        "  RMSE    :",
        rmse,
    )
    print(
        "  cosine  :",
        cosine,
    )

    encoder_output = output_root / "encoder-output.pt"

    torch.save(
        {
            "output": x.cpu(),
        },
        encoder_output,
    )

    print()
    print(
        "Encoder output:",
        encoder_output,
    )

    print()
    print("=" * 88)
    print("PHOENIX WHISPER FRONTEND128 ENCODER: COMPLETE")
    print("=" * 88)


def main() -> None:

    parser = argparse.ArgumentParser(
        description=("Whisper-small Phoenix/NPU1 encoder validation.")
    )

    mode = parser.add_mutually_exclusive_group(required=True)

    mode.add_argument(
        "--prepare-reference",
        action="store_true",
        help=("Generate real-audio FP32 frontend and " "encoder reference artifacts."),
    )

    mode.add_argument(
        "--run",
        action="store_true",
        help=(
            "Run the Phoenix frontend and complete "
            "12-block encoder against existing references."
        ),
    )

    mode.add_argument(
        "--all",
        action="store_true",
        help=(
            "Generate references and then run the complete "
            "Phoenix encoder validation."
        ),
    )

    parser.add_argument(
        "--wav",
        type=Path,
        default=None,
        help=(
            "16-kHz mono PCM16 WAV used to generate "
            "the FP32 validation references. "
            "Defaults to WHISPER_TEST_WAV."
        ),
    )

    parser.add_argument(
        "--frontend-reference",
        type=Path,
        default=None,
        help=("Optional FP32 frontend reference artifact."),
    )

    parser.add_argument(
        "--encoder-reference",
        type=Path,
        default=None,
        help=("Optional FP32 encoder reference artifact."),
    )

    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help=("Optional root directory for Phoenix encoder artifacts."),
    )

    args = parser.parse_args()

    wav = args.wav

    if wav is None:
        wav_value = os.environ.get("WHISPER_TEST_WAV")

        if wav_value:
            wav = Path(wav_value)

    ARTIFACT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    if args.prepare_reference:
        if wav is None:
            parser.error("--prepare-reference requires --wav " "or WHISPER_TEST_WAV")

        prepare_reference(wav)
        return

    if args.run:
        run_phoenix(
            frontend_reference=args.frontend_reference,
            encoder_reference=args.encoder_reference,
            output_root=args.output_root,
        )
        return

    if args.all:
        if wav is None:
            parser.error("--all requires --wav " "or WHISPER_TEST_WAV")

        prepare_reference(wav)
        run_phoenix()
        return


if __name__ == "__main__":
    main()
