<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Changelog

Public API changes to IRON, newest first. A pull request that changes the
public API adds its entry under Unreleased.

## Unreleased

### Added

- `iron.functional` with torch's names: `linear`, `rms_norm`, `layer_norm`,
  `silu`, `gelu(x, approximate=)` and `rope`. `linear` replaces
  `iron.lm.blocks.project`.
- Handle arithmetic in graph bodies: `x + y` and `x * y` record an
  elementwise step, or a rowwise one when a row meets a matrix, in either
  order.
- Model parts in `iron.lm`: `Attention`, `MLP`, `Norm`, `DecoderLayer` and
  `CrossDecoderLayer`, which each config's `layer()` returns. Every part takes
  its weights first, as in `Norm(w, x)`.
- `Model.sanitize(w)`, which renames a checkpoint's modules to the names the
  parts read, once at load.
- `iron.lm.Tokenizer`, which reads `tokenizer.json` for every runner.
- Goldens recorded from transformers, with a fingerprint of the config and
  weights they came from. `pytest --record-goldens` (or `IRON_RECORD_GOLDENS`)
  records them.
- `iron.Precision` and a `precision` tunable on GEMM and flm.GEMM, with
  `torch.set_float32_matmul_precision`'s levels. `Graph.precision` and
  `compile(precision=)` set a floor.
- `python -m iron.lm.tune <application>`, which writes the fastest admissible
  setting of each operator shape to `profiles/<device>.json`.

- `SECURITY.md`, Dependabot for GitHub Actions, the OpenSSF Scorecard
  workflow and actionlint in the lint job, following mlir-aie's CI
  security baseline.

- Autotune skips GEMM settings whose matmul kernel alone, by mlir-aie's
  nightly cycles, is slower than the fastest setting timed.

### Changed

- Config fields use `config.json`'s names: `hidden_size`,
  `num_hidden_layers`, `num_attention_heads`, `num_key_value_heads`,
  `intermediate_size`, `rope_theta`, `num_experts_per_tok` and
  `norm_topk_prob` replace `emb_dim`, `n_layers`, `n_heads`, `n_kv_groups`,
  `hidden_dim`, `rope_base`, `experts_per_token` and `normalize_top_k`.
- `CausalLM` owns the head (final norm, then the tied embedding or
  `lm_head`, chosen by `tie_word_embeddings`).
- `F.gelu` refuses the exact form, which no operator computes, instead of
  computing the tanh form.
- `Attention` requires `eps` when a q, k or v norm is set.
- `F.linear` refuses a tunable of the operator its row count does not choose.
- A missing golden fails `check_accuracy` instead of skipping it, and a golden
  whose fingerprint no longer matches is refused.
- `CausalLM.generate` times the first token from the call.
- `Runner.npu()` takes only `full_elf`.

### Removed

- `Layer`, the numpy `Oracle`, `EncoderDecoderOracle` and `widen`. Models are
  judged by transformers' goldens or the graph's reference.
- Mamba-2 and mixture-of-experts layers, which only the Oracle ran.
  `TopKRouter` stays.
- GEMM's `emulate_bf16_mmul_with_bfp16` and `prio_accuracy`, and flm.GEMM's
  and MHA's `emulate_bf16_mmul_with_bfp16`, replaced by `precision`.
- `compile(tuner=)`, `CompiledGraph.tuning`, `Model.load(tuner=)`,
  `Runner.tables`, `--cost-table`, and the `Tuner`, `Tuning` and `Prices`
  interfaces.
