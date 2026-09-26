# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The NPU against the float32 CPU reference, teacher-forced.

Its own entry point because the reference is torch (:mod:`.reference`) and
the NPU application is not. Run with
``python -m iron.applications.llama_3_2_1b.accuracy WEIGHTS TOKENIZER``.
"""

import logging

import numpy as np

from . import harness
from .npu import setup
from .reference import ReferenceForward


def main():
    logging.basicConfig(level=logging.DEBUG)
    parser = harness.argument_parser(
        "Compare each step's logits against an fp32 CPU reference, feeding both "
        "the reference's greedy token"
    )
    args = parser.parse_args()
    config, state, _, npu = setup(args)
    results = harness.check_accuracy(
        config,
        state,
        npu.forward,
        config,
        harness.LlamaModelState(config),
        ReferenceForward(config),
        args.num_tokens,
    )
    # Over every step, prefill and decode alike: one step's KL depends as much
    # on how confident the reference is at that position as on the NPU.
    kl = np.array([k for k, _ in results])
    print(f"[Accuracy] Mean KL: {kl.mean():.6f}")
    print(f"[Accuracy] P90 KL: {np.percentile(kl, 90):.6f}")
    print(f"[Accuracy] Max KL: {kl.max():.6f} (step {kl.argmax()})")
    print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")


if __name__ == "__main__":
    main()
