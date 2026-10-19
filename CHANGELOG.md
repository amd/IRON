<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Changelog

Public API changes to IRON, newest first. A pull request that changes the
public API adds its entry under Unreleased.

## Unreleased

### Added

- `Operator.reference_only = True`: an operator that is a declaration plus
  `reference()`, with no kernel. Graphs trace it and references run it;
  compiling it raises, and the device catalog skips it.
- `Experts`: each row through the gated feed-forwards of the experts
  `TopKRouter` chose for it, weighted, on one core over mlir-aie's scalar
  `expert_gate_up` and `expert_down`, streaming every expert each row.
- `SelectiveScan`: Mamba2's state space recurrence over a run of rows,
  from a state to the state after its last valid row, over mlir-aie's
  scalar `selective_scan`, a core per run of heads.
- Application `granite_hybrid` (Granite 4.0-H, dense and MoE, on the host),
  judged by device-free toy goldens.
- Application `resnet` (ResNet-50), judged by a device-free toy golden.
- Applications `smollm3` (SmolLM3 3B), `ministral3` (Ministral 3's text
  decoder, on drawn weights) and `qwen3_moe` (Qwen3-30B-A3B, on the host),
  each judged by a device-free toy golden.
- `iron.param(*shape, dtype=bfloat16)`, a weight a graph declares by shape,
  and `Graph.load_state_dict(tree, path="")`, which binds each one to the tensor at its
  dotted path, cast to its dtype, and raises once, naming every missing,
  extra and wrong-shaped tensor; a param held at two paths is tied, bound
  from its first. A param never bound is named when the graph is traced,
  and a second load is refused. `Graph.draw(seed)` and `Graph.unread()` bind
  them drawn or unwritten.
- Leaf modules in `iron.lm`, graphs that declare their weights as
  transformers names them: `Linear`, `Embedding`, `RMSNorm` and `LayerNorm`.
- Decoder blocks as modules in `iron.lm.blocks`, each built from a config
  and a layer index: `Attention(c, i, norms="", bias=False)`, `GatedMLP(c)`
  and `DecoderLayer(c, i)`, which holds its own `KVCache(c)` and the
  model's `Rope(c)`. `iron.lm` exports `Attention` and `DecoderLayer`.
- `Graph.trace(precision=)`, which `compile(precision=)` passes on instead of
  setting `Graph.precision` while it compiles.
- `iron.lm.testing.load_from_flags`, a model test's `Model.load` at the
  `--random-weights` and `--max-seq-len` pytest was given, its files
  `require`d; `require(staged=False)` skips in CI too.
- `Gather` and `GatherWords`, `Copy`'s gather steps, in `iron.operators`'
  catalog, so a profile that tunes them saves and loads; a test fails on
  any public operator the catalog leaves out.
- `iron.functional` with torch's names: `linear`, `rms_norm`, `layer_norm`,
  `silu`, `gelu(x, approximate=)` and `rope`. `linear` replaces
  `iron.lm.blocks.project`.
- `iron.functional` for CNNs, on channels-last `(H, W, C)` feature maps,
  with torch's signatures: `conv2d`, `max_pool2d`, `interpolate` (2x
  nearest) and `cat` (`dim=-1`). Each pads the map and its rows as its
  steps need, and refuses what it does not compute.
- `iron.functional.causal_conv1d(x, taps, state)`, a depth-wise causal FIR
  over a prompt chunk or a decode step that stages and carries the rows
  before the call itself, its `state` an `F.ConvState(read, write, window,
  tail)`; LFM2's short conv calls it.
- Handle arithmetic in graph bodies: `x + y` and `x * y` record an
  elementwise step, or a rowwise one when a row meets a matrix, in either
  order.
- Model parts in `iron.lm`: `Attention`, `MLP`, `Norm`, `DecoderLayer` and
  `CrossDecoderLayer`, which each config's `layer()` returns. Every part takes
  its weights first, as in `Norm(w, x)`.
- `Model.sanitize(w)`, which renames a checkpoint's modules to the names the
  parts read, once at load.
- `iron.lm.TokenizerJson(path)`, a Hugging Face `tokenizer.json` read
  through `tokenizers`: the encoding every loaded model's `Tokenizer` wraps.
- `iron.lm.Tokenizer(encoding, bos)`, a prompt's tokenizer: called on text
  it gives the ids with `bos` first, and `decode` gives text back. A
  loaded model's `tokenizer` is one, over `tokenizer.json` unless the
  model class opens another.
- Goldens recorded from transformers, with a fingerprint of the config and
  weights they came from. `pytest --record-goldens` (or `IRON_RECORD_GOLDENS`)
  records them.
- `iron.Precision` and a `precision` tunable on GEMM and flm.ProjectionGEMM,
  with `torch.set_float32_matmul_precision`'s levels. `Graph.precision` and
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
- `field(array=True)` and `Auto(array=True)`: an operator's `Array` is
  generated from its declarations, so a field is declared once.
- `Config.norm()`, the kind of norm a config's layers and final norm share,
  and `Model.final_norm`, the module that final norm reads.
- `DecoderLayer.block(x, pre, f, post)`, one residual block; each layer is
  its list of blocks.
- `Model.renames`, a class-level table of checkpoint module renames applied
  before `sanitize`, `renamed(tree, renames)`, which applies one to a copy
  of a tree, and `leaves(tree)`, each weight of a tree by its dotted name.
- `Config.to_json()`, `from_checkpoint`'s inverse: the fields as
  `config.json` names them, which `HuggingFace.build` configures
  transformers from.
- `HuggingFace.model_class`, the transformers auto class a subclass loads
  and builds (`AutoModelForCausalLM` by default).
- `iron.lm.testing.assert_close`, the one check of a model's logits against
  its reference: within `LOGITS` (5%) of the largest, and the same argmax
  where the reference's top two lie further apart than that.
- `Model.loaded()`, the hook `Model.load_versions` hands the compiled
  versions to.
- `BuiltArray.program()`, a built array alone with its operator's own
  sequence, as a `Program`.
- `Model.load(path, seed=, max_seq_len=, full_elf=)`: the model of a
  Hugging Face repository's files, a local directory or a repository id
  downloaded once, fitted, compiled and loaded, its tokenizer as
  `model.tokenizer`; `Model.from_checkpoint` is the same, not yet loaded.
  The model class names its `config` and `hugging_face`; `fit`,
  `default_config`, `tune_arguments` and `tune_calls` are its classmethods,
  and `prompt` and `cpu_reference` its methods. Each application's package exports its model class.
- `lm.main(Model)`, a model's command line, whose positional argument is
  the path or repository id `load` takes.
- `OnHost.generate`, which draws on the host.
- `Model.generate(prompt, max_tokens, sampler=None)`: text in gives text
  out, token ids give ids, and a list of `{"role", "content"}` messages is
  rendered by the checkpoint's `chat_template` (`Tokenizer.chat`, which
  needs jinja2: `pip install 'iron[models]'`), each special token it writes its id and
  the BOS first once; `sampler=None` is greedy.
  `Model.stream` yields the same pieces as they are drawn, and
  `model.stats` holds the last call's `ttft` and `tokens_per_s`.
- `--prompt TEXT` on a model's command line.
- `-v` on a model's command line and `python -m iron.lm.tune`, which logs
  iron's INFO lines, such as each compile's.
- `repr` of a graph names its traced shapes; of a compiled version, its
  inputs, packaging and build directory; of a `Profile`, its operators; of
  a model, its `max_seq_len` and whether it is loaded.
- `repr` of an operator's `declaration` lists its fields, tunables with the
  values each is searched over, members with their symbolic shapes, and the
  array tier its cores are built from.

### Changed

- `iron.lm`'s leaf modules take `torch.nn`'s names and defaults:
  `Linear(in_features, out_features, bias=True)`,
  `Embedding(num_embeddings, embedding_dim)`, `RMSNorm(normalized_shape,
  eps=None)` (the dtype's machine epsilon) and `LayerNorm(normalized_shape,
  eps=1e-5)`, holding those as attributes.
- `Tokenizer.chat` puts the BOS where the chat template writes it, and only
  there, as transformers' `apply_chat_template` does; it no longer adds one.
  The template may call `strftime_now` and writes `tokenizer_config.json`'s
  `bos_token` where it has one; `Model.load` reads the template from
  `chat_template.jinja` when `tokenizer_config.json` has none.
- `CausalLM` builds its modules, `model` (a `Decoder` of `layer_class`
  layers, `DecoderLayer` by default) and `lm_head` (the embedding where
  tied), and binds them to the checkpoint's tree with `Graph.load_state_dict`. A
  model with `layer_class = None` reads `config.layer(i)` as before, its
  caches in `caches`, a `KVCache` per attention layer, in place of `keys`
  and `values`. The RoPE table is `CausalLM.rope`, a `Rope`, whose `rows`
  replaces `CausalLM.angles` and whose `long_past` replaces
  `CausalLM.long_past`.
- Qwen 2, Qwen3 and Granite name their layers, `Qwen2Layer`, `Qwen3Layer`
  and `GraniteLayer`, in place of `Qwen3Config.attention` and
  `GraniteConfig.attention` and `layer`.
- The layer descriptions a config's `layer()` returns, `iron.lm.Attention`
  and `DecoderLayer`, are `AttentionSpec` and `DecoderLayerSpec`, leaving
  the names to the modules that own their weights.
- `YOLOXNano` is written in `iron.functional`'s CNN functions, and returns
  each scale's predictions as `(H, W, 144)`, not `(H, W * 144)`.
- `Model.generate` and `stream` stop after the first of `Model.eos` they
  draw, the eos token included, as Hugging Face's `generate` does:
  `max_tokens` is a cap. `Model.eos` is the checkpoint's `eos_token_id`, one
  or a list, from its `generation_config.json` or else its `config.json`.
- `LayerNorm` takes an optional `weight=` row, as `RMSNorm` does: weighted,
  a second core per (column, channel) multiplies each normalized row by it.
  Both share `iron.common.WeightedRowwise`, and `F.layer_norm` passes its
  weight to the one `LayerNorm` step, leaving the bias a `RowwiseAdd` step.
  A weighted `LayerNorm`'s row is at most 4096 elements (8192 before), since
  the multiplying core holds the weight row beside each line; its tolerance
  scales the first kernel's atol by the weight.
- An operand of an `Elementwise` or `Rowwise` operator that gives no `per=`
  is split over every core, `per=(num_aie_columns, num_channels)`.
- A `field(derive=...)` field is held to its formula: a value given that
  disagrees raises `ValueError`, and `Operator.check_derived` is removed.
  `field(derive=..., held=False)` is one a given value overrides.
- A name or layer missing from a `Checkpoint.tree()` raises an error naming
  its dotted path, the checkpoint file and what the module does have.
- A compiled graph refuses an input numpy would not cast to its dtype
  (`same_kind`): float ids into an int32 input raise rather than truncate.
- Compiling, loading or tuning with no NPU found raises a `RuntimeError`
  saying how to compile without one, not an `AttributeError` on `None`.
- `Golden.logits` raises `FileNotFoundError` naming the file when there is
  none to read, and `LookupError` only for a file that lacks the sequence.
- `F.linear` refuses an `x` that is neither `(in,)` nor `(rows, in)`.
- `MHA.COLUMNS` and `iron.operators.mha.Columns` are `MHA.PACKED_PIPELINES`,
  the most pipelines one query packed takes by array width: the build placed
  nothing by the other columns.
- `iron.lm.base` is split into `iron.lm.config`, `checkpoint`, `model` and
  `cli`.
- An operator declares with aie.iron's markers: `In`, `Out` and `InOut`
  come from `aie.iron` (`x = In(M, K, obj_shape=...)`), and every field is
  annotated `CompileTime[T]` or `DispatchTime[T]` from `aie.iron`, which
  the declaration reads: `M: CompileTime[int] = field()`,
  `tile: CompileTime[int] = Auto()`,
  `n: DispatchTime[np.int32] = field(init=False)`. A field annotated with
  neither, with a marker inside a union (`CompileTime[int] | None`; write
  `CompileTime[int | None]`), or declared without `field()`/`Auto()` is
  refused, as is a dispatch value given any other `field()` option.
- `Param(...)` is `field(...)`, with the same options.
- `iron.operators.flm`'s GEMM is `ProjectionGEMM`, so it is not confused
  with `iron.operators.GEMM`; a profile names it `"flm.ProjectionGEMM"`.
- An operand's element shape is `obj_shape=`, not `obj_type=`:
  `In(M, K, obj_shape=(tile, K))`. aie.iron's `ObjectFifo(obj_type=)` keeps
  its name, since there it is an `np.ndarray` type.
- `Model.load(release=, full_elf=, dev=)`, which compiles and loads a
  model's versions, is `Model.load_versions`: `CausalLM.load` is the
  classmethod above.
- `Sampler(temperature, top_k, rng=None)` is `Sampler(temperature, top_k,
  seed=SEED)`.
- `Runner.encode(text)` is `model.tokenizer(text)`.
- GEMM's `dtype_in` and `dtype_out` are `input_dtype` and `output_dtype`,
  the names its kernel factory (`aie.iron.kernels.linalg.mm`) takes.
- An operator's nested `Array` annotates only the library's views it reads
  (`dev`, `buffers`, `inputs`, `outputs`); an annotation of a field or member
  is refused. A field the array reads that no stream names is declared
  `field(array=True)` or `Auto(array=True)`.
- `F.rms_norm(input, normalized_shape, weight=None, eps=None)` and
  `F.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-5)`
  take torch's arguments in torch's order; `eps=None` is the input dtype's
  epsilon, as torch's. A `normalized_shape` other than the input's last
  axis is refused.
- `F.linear(precision=)` is the one way to ask for an accurate projection: at
  `Precision.HIGHEST` several rows run core GEMM, whose float32 sums round
  once, where they ran flm.ProjectionGEMM before, asked for by the call or by
  a graph's `precision` raising flm.ProjectionGEMM to it, which hands over
  (`Operator.at_precision`); one row, a GEMV that rounds once, takes any
  precision. `Attention` and `MLP` take `precision` in place of `accurate`.
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
- `generate(tokens, num_tokens, sample)` is `generate(prompt, max_tokens,
  sampler=None)`, and returns the answer alone, not a tuple with the
  timings; `Multimodal.generate` takes `raw=` by keyword. The old names
  are gone, with no aliases.
- A model's command line streams the text it draws, and neither echoes
  `prompt.txt` nor prints the host loop's text under `--compare-host`.
- `Sampler` defaults to temperature 0.7 and top-k 50, a model CLI's
  `--temperature` and `--top-k` take those defaults, and with no `rng` it
  draws from one seeded at `SEED`.
- `Checkpoint.tree("random")` draws a bias about zero, not one.

- `Operand.count`, `Operator.device()` and `Operator.configuration()` are
  `Operand.lanes`, `Operator.array_device()` and
  `Operator.xclbin_operator()`.
- `In`, `Out` and `InOut` are plain operands, not aie.iron's kernel-argument
  markers.
- `resolved(dev)` resolves for the device given, bound only while it
  resolves and not recorded on the result, instead of probing for an NPU,
  and an unresolved `Auto()` tile raises instead of becoming a 0-d fifo.
- RoPE's `method_type` is `two_halves`, a flag.
- flm.ProjectionGEMM takes `epilogue="silu"` and `"sigmoid"`, which a SiLU or
  Sigmoid finish applied before.
- IRON requires Python 3.11.
- An `Encoder`'s per-call row count is `rows`, as a causal model's is.
- `Model.bos` is read from the checkpoint's `config.json`, else its
  `generation_config.json`, unless the model class names one; with neither
  naming `bos_token_id` it raises a `KeyError`.
- `HuggingFace.build` refuses a weight the model does not hold, as it
  refuses one the model lacks.
- `Golden.logits` keys on the tokens and any clip or image array beside
  them, and a checkpoint's `golden.npz` is fingerprinted with its
  `config.json` and `Checkpoint.fingerprint()`, each tensor's name, type,
  shape and the bytes at either end; one recorded before must be recorded
  again.
- `Config.from_checkpoint` names the missing `config.json` keys, and an
  encoder refuses a token outside its vocabulary.
- A config field is read from and written to `config.json` at its own name
  unless its `metadata["json"]` names another key; `iron.lm.not_json(default)`
  declares one `config.json` does not set.
- idefics3 vision, Whisper and Phi-4 config fields take `config.json`'s
  names: `hidden_size`, `patch_size`, `encoder_attention_heads`,
  `encoder_ffn_dim`, `num_mel_bins`, `max_source_positions` and
  `max_position_embeddings`.

### Removed

- Llama's tiktoken tokenizer, `SPECIAL_TOKENS` and `tokenizer()`: Llama
  reads its checkpoint's `tokenizer.json` like every model, and tiktoken is
  no longer a dependency.
- `iron.common`'s `In`, `Out`, `InOut` and `DispatchTime`; import the
  markers from `aie.iron`.
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
- GEMM's `emulate_bf16_mmul_with_bfp16` and `prio_accuracy`, and
  flm.ProjectionGEMM's and MHA's `emulate_bf16_mmul_with_bfp16`, replaced by
  `precision`.
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
- `generate_on_host(show=)`, and its timings: it returns the tokens drawn.
- `Runner`, its `runner` back-pointer and `VLMRunner`: the model class is
  what loads (`Model.load`); idefics3's whole model is `SmolVLM`. A model's
  command line takes the checkpoint's directory or repository id, not
  the weights' and tokenizer's paths.
- `Runner.sizes` and `--size`, `F.linear`'s `k_tile` and `tile_n`, and
  Whisper's `Runner`.
- `Operand.runtime`; an operand finds the running sequence itself.
- Operator fusion, one operator's step run in another's cores, until it is
  done as dataflow: `compile(fold=)` and `iron.common.graph.fold`; `Chain`,
  `Link`, `Finish` and `Prepare`; `Operator`'s `finish`, `prepare` and
  `placements` fields, `fold`, `prefold`, `on_array`, `placed`, `copies_to`,
  `at_line`, `finish_inputs` and `prepare_inputs`; an operand's `finish=`,
  `prepare=` and `feed=`; and flm.ProjectionGEMM's clamp. Image fusion, several
  operators' arrays in one full ELF, stays.
