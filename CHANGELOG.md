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

- A test that importing `iron`, `iron.functional`, `iron.lm`, the operators
  and every application asks for neither torch nor transformers; only
  recording a golden needs them.

- `Operator.replace`, `dataclasses.replace` that also keeps the fields a
  resolve computes (`Auto(init=False)`), and checks the result as
  construction does.
- `Param(array=True)` and `Auto(array=True)`: an operator's `Array` is
  generated from its declarations, so a field is declared once.
- `Config.norm()`, the kind of norm a config's layers and final norm share,
  and `Model.final_norm`, the module that final norm reads.
- `DecoderLayer.block(x, pre, f, post)`, one residual block; each layer is
  its list of blocks.
- `Model.renames`, a class-level table of checkpoint module renames applied
  before `sanitize`, and `leaves(tree)`, each weight of a tree by its dotted
  name.
- `iron.lm.testing.assert_close`, the one check of a model's logits against
  its reference: within `LOGITS` (5%) of the largest, and the same argmax
  where the reference's top two lie further apart than that.
- `Model.loaded()`, the hook `Model.load` hands the compiled versions to;
  `Runner.build()` makes the model `npu()` loads.
- `BuiltArray.program()`, a built array alone with its operator's own
  sequence, as a `Program`.

### Changed

- `F.rms_norm(input, normalized_shape, weight=None, eps=None)` and
  `F.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-5)`
  take torch's arguments in torch's order; `eps=None` is the input dtype's
  epsilon, as torch's. A `normalized_shape` other than the input's last
  axis is refused.
- `F.linear(precision=)` is the one way to ask for an accurate projection:
  at `Precision.HIGHEST` several rows run core GEMM, whose float32 sums
  round once, where they ran flm.GEMM before, whether asked for by the call
  or by `Graph.precision`; one row, a GEMV that rounds once, takes any
  precision.
  `Attention` and `MLP` take `precision` in place of `accurate`.
- `HuggingFaceWhisper` and `HuggingFaceVLM` move to their applications'
  `hugging_face.py`, as EmbeddingGemma 2's builders are, which only tests
  and golden recording import.
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
- `Checkpoint.tree("random")` draws a bias about zero, not one.
- `Runner.npu()` takes only `full_elf`.

- `Operand.count`, `Operator.device()` and `Operator.configuration()` are
  `Operand.lanes`, `Operator.array_device()` and
  `Operator.xclbin_operator()`.
- `In`, `Out` and `InOut` are plain operands, not aie.iron's kernel-argument
  markers.
- `resolved(dev)` resolves for the device given, bound only while it
  resolves and not recorded on the result, instead of probing for an NPU,
  and an unresolved `Auto()` tile raises instead of becoming a 0-d fifo.
- RoPE's `method_type` is `two_halves`, a flag.
- flm.GEMM takes `epilogue="silu"` and `"sigmoid"`, which a SiLU or Sigmoid
  finish applied before.
- IRON requires Python 3.11.
- An `Encoder`'s per-call row count is `rows`, as a causal model's is.
- `Runner.bos` is read from the checkpoint's `config.json` unless a runner
  names one; a file without `bos_token_id` raises a `KeyError` naming it.
- `HuggingFace.build` refuses a weight the model does not hold, as it
  refuses one the model lacks.
- `Golden.logits` keys on the tokens and any clip or image array beside
  them, and a checkpoint's `golden.npz` is fingerprinted with its
  `config.json` and `Checkpoint.fingerprint()`, each tensor's name, type,
  shape and the bytes at either end; one recorded before must be recorded
  again.
- `Config.from_checkpoint` names the missing `config.json` keys, and an
  encoder refuses a token outside its vocabulary.
- idefics3 vision, Whisper and Phi-4 config fields take `config.json`'s
  names: `hidden_size`, `patch_size`, `encoder_attention_heads`,
  `encoder_ffn_dim`, `num_mel_bins`, `max_source_positions` and
  `max_position_embeddings`.

### Removed

- `F.linear(accurate=)`, `Attention(accurate=)`, `MLP(accurate=)` and
  `iron.functional.ACCURATE`; pass `precision=Precision.HIGHEST`.
- `Phi4Config.max_position_embeddings`: LongRoPE's amplitude scale is set
  from `max_seq_len` as the checkpoint gives it, and kept when a caller
  lowers it.
- gemma4_flm's GEMM and dequant exploration and `build.py --only`; the
  application is one example.
- `Layer`, the numpy `Oracle`, `EncoderDecoderOracle` and `widen`. Models are
  judged by transformers' goldens or the graph's reference.
- Mamba-2 and mixture-of-experts layers, which only the Oracle ran.
  `TopKRouter` stays.
- GEMM's `emulate_bf16_mmul_with_bfp16` and `prio_accuracy`, and flm.GEMM's
  and MHA's `emulate_bf16_mmul_with_bfp16`, replaced by `precision`.
- `compile(tuner=)`, `CompiledGraph.tuning`, `Model.load(tuner=)`,
  `Runner.tables`, `--cost-table`, and the `Tuner`, `Tuning` and `Prices`
  interfaces.
- `Auto(derived=True)`, replaced by `Auto(init=False)`; a caller can no
  longer give MHA's `B_kv`.
- `Profile.lookup`, `Operator.from_operands`, `Operator.value_buffer`, and
  the `AutoSpec` and `ParamSpec` exports from `iron.common`.
- The `ReduceMax`, `LeakyReLU`, `Repeat` and `Dequant` operators and
  `swiglu_prefill_stream`; flm's `Shipped` overlay is a test helper, not a
  catalog operator.
- GEMM's `round_conv_even` and `use_scalar`, `DequantBFP`'s `tile_n`,
  `decode_layer`'s `sliding_window`, and `lm_head`'s and `prefill_attn`'s
  `trace_size`.
- `Derived`; computed weights live in `sanitize`'s output or on the model.
- `CausalLM.head` and `Encoder.norm()` overrides, replaced by `final_norm`;
  `CausalLM.embed`.
- `Runner.sizes` and `--size`, `F.linear`'s `k_tile` and `tile_n`, and
  Whisper's `Runner`.
- `Operand.runtime`; an operand finds the running sequence itself.
- Operator fusion, one operator's step run in another's cores, until it is
  done as dataflow: `compile(fold=)` and `iron.common.graph.fold`; `Chain`,
  `Link`, `Finish` and `Prepare`; `Operator`'s `finish`, `prepare` and
  `placements` fields, `fold`, `prefold`, `on_array`, `placed`, `copies_to`,
  `at_line`, `finish_inputs` and `prepare_inputs`; an operand's `finish=`,
  `prepare=` and `feed=`; and flm.GEMM's clamp. Image fusion, several
  operators' arrays in one full ELF, stays.
