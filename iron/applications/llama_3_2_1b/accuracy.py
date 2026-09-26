# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The NPU against the float32 CPU reference, teacher-forced.

Its own entry point because the reference is torch (:mod:`.reference`) and
the NPU application is not. Run with
``python -m iron.applications.llama_3_2_1b.accuracy WEIGHTS TOKENIZER``.
"""

import logging

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
    kl = [k for k, _ in results]
    print(f"[Accuracy] Prefill KL: {kl[0]:.6f}")
    if len(kl) > 1:
        print(f"[Accuracy] Decode max KL: {max(kl[1:]):.6f}")
    print(f"[Accuracy] Top-1 mismatches: {sum(not t for _, t in results)}")


if __name__ == "__main__":
    main()
