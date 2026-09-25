# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
import subprocess
import sys
from pathlib import Path

from whisper_common import (
    APP_DIR,
    ARTIFACT_ROOT,
    BLOCKS,
    whisper_checkpoint,
)

FRONTEND_REFERENCE = ARTIFACT_ROOT / "whisper-small-frontend-reference-128.pt"

ENCODER_REFERENCE = ARTIFACT_ROOT / "whisper-small-encoder-reference-frontend128.pt"

FRONTEND_OUTPUT = ARTIFACT_ROOT / "frontend-128-phoenix" / "frontend-output.pt"


def run_script(
    script: str,
    *args: str | Path,
) -> None:
    """Run one Whisper stage in a fresh Python process."""

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


def prepare_reference() -> None:
    """Generate the deterministic FP32 frontend and encoder oracle."""

    # Validate checkpoint configuration before spawning children.
    checkpoint = whisper_checkpoint()

    print(
        "Whisper checkpoint:",
        checkpoint,
    )

    run_script(
        "whisper_reference_frontend.py",
    )

    if not FRONTEND_REFERENCE.is_file():
        raise FileNotFoundError(
            f"Frontend reference was not created: " f"{FRONTEND_REFERENCE}"
        )

    run_script(
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
    frontend_output: Path | None = None,
    output_root: Path | None = None,
) -> None:
    """Run 12 isolated Phoenix encoder blocks and final LayerNorm."""

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

    if frontend_output is None:

        run_script(
            "whisper_frontend.py",
            "--reference",
            frontend_reference,
        )

        frontend_output = FRONTEND_OUTPUT

    else:
        frontend_output = frontend_output.resolve()

    if not frontend_output.is_file():
        raise FileNotFoundError(
            f"Phoenix frontend output missing: " f"{frontend_output}"
        )

    previous = frontend_output
    previous_key = "block0_input"

    # ========================================================
    # Transformer blocks
    #
    # Each block is intentionally a fresh Python process.
    # On the tested Phoenix/XRT stack this prevents accumulation
    # of independently loaded cached XRT kernel handles.
    # ========================================================

    for block in range(BLOCKS):

        print()
        print("#" * 88)
        print(f"PHOENIX WHISPER ENCODER BLOCK {block}/{BLOCKS - 1}")
        print("#" * 88)

        run_script(
            "whisper_encoder_block.py",
            "--block",
            str(block),
            "--input-mode",
            "phoenix",
            "--input",
            previous,
            "--input-key",
            previous_key,
            "--reference",
            encoder_reference,
            "--output-root",
            output_root / f"block{block}",
        )

        produced = output_root / f"block{block}" / f"block{block}-output.pt"

        if not produced.is_file():
            raise FileNotFoundError(f"Block {block} output missing: " f"{produced}")

        previous = produced
        previous_key = "output"

        print(
            "Block output:",
            produced,
        )

    # ========================================================
    # Final encoder LayerNorm
    # ========================================================

    run_script(
        "whisper_final_layernorm.py",
        "--input",
        previous,
        "--reference",
        encoder_reference,
        "--output-root",
        output_root / "final-layernorm",
    )

    # ========================================================
    # Depth analysis
    # ========================================================

    if output_root == ARTIFACT_ROOT:
        run_script(
            "whisper_depth_analysis.py",
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
        help=(
            "Generate deterministic FP32 frontend and " "encoder reference artifacts."
        ),
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
        "--frontend-output",
        type=Path,
        default=None,
        help=(
            "Use an existing Phoenix frontend output and "
            "skip rerunning the frontend."
        ),
    )

    parser.add_argument(
        "--output-root",
        type=Path,
        default=None,
        help=("Optional root directory for Phoenix encoder artifacts."),
    )

    args = parser.parse_args()

    ARTIFACT_ROOT.mkdir(
        parents=True,
        exist_ok=True,
    )

    if args.prepare_reference:
        prepare_reference()
        return

    if args.run:
        run_phoenix(
            frontend_reference=args.frontend_reference,
            encoder_reference=args.encoder_reference,
            frontend_output=args.frontend_output,
            output_root=args.output_root,
        )
        return

    if args.all:
        prepare_reference()
        run_phoenix()
        return


if __name__ == "__main__":
    main()
