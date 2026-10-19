<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Changelog

Public API changes to IRON, newest first. A pull request that changes the
public API adds its entry under Unreleased.

## Unreleased

### Added

- Qwen3-Reranker (`Qwen3Reranker.score`: "yes" over "no" after its model
  card's prompt) and Qwen3-Embedding (`Qwen3Embedding.embed`: the last
  token's unit-length final hidden state, one compile up to a prompt
  chunk), each with a toy golden; `NoCache(causal=True)` attends back
  only, the embedder's.
- `CausalConv1d`, a depth-wise causal convolution whose rows before a call
  are a `Checkpoints` state, shared by Granite 4.0-H's Mamba, Qwen3.5's
  Gated DeltaNet and LFM2's short conv; and `Weights`, named weights read
  from a checkpoint and computed with elsewhere, from Granite 4.0-H.
- `Config.json_prefix`, the object of `config.json` a config's fields are
  read from: `"text_config."` for EmbeddingGemma 2's text encoder, SmolVLM's
  text model and Gemma 4, `"audio_config."` and `"vision_config."` for
  EmbeddingGemma 2's towers. A field's `metadata["json"]` path is under it,
  or from the file's root after a `/` (`Config.json_key`).
- `DecoderLayer.norm`, the class its norms are built from: `RMSNorm`, or
  Whisper's decoder's `LayerNorm`.
- `CausalLM.rope_row(n, begin)`: the RoPE table row a prompt chunk reads
  first, which a caller writing the `rope_start` value itself passes.
- `SandwichLayer` (Gemma's: each block's output normed again before its
  residual) and `PleLayer` (Gemma 4's: a per-layer input gated in, the sum
  scaled by `layer_scalar`). EmbeddingGemma 2's text and vision layers are
  built on them, and its audio tower's conformer layers are modules.
- `Linear(precision=)`, and `Config.precision`, every projection's in
  `Attention`, `MLP` and `GatedMLP` (None: `F.linear`'s).
- `iron.lm.checkpoint.subtree(tree, **modules)`: a tree of a checkpoint's
  modules at new names, as a model loads part of a checkpoint.
- `Session(model)`: one conversation over a `CausalLM`'s loaded versions,
  with `logits(tokens)`, `draw(...)`, `forget`, `resume` and `prompt_ids`,
  which move there from `CausalLM`. Several sessions share one compiled
  model; `model.session` is the one `logits` and `generate` run in, and
  `model.holder` the one whose tokens the caches hold. The versions a
  session calls are `decode_step`, `prompt_chunk`, `placed_chunk` and
  `placeholders`, as `use` takes them.
- `Operator.reference_only = True`: an operator that is a declaration plus
  `reference()`, with no kernel. Graphs record it and references run it;
  compiling it raises, and the device catalog skips it.
- `Experts`: each row through the gated feed-forwards of the experts
  `TopKRouter` chose for it, weighted, on one core over mlir-aie's scalar
  `experts`, streaming every expert each row.
- `SelectiveScan`: Mamba2's state space recurrence over a run of rows,
  from a state to the state after its last valid row, over mlir-aie's
  scalar `selective_scan`, a core per run of heads.
- `GatedDeltaRule`: Gated DeltaNet's recurrence over a run of rows, as
  Qwen3.5 calls it, over mlir-aie's scalar `gated_delta_rule`, a core per
  run of value heads.
- Application `granite_hybrid` (Granite 4.0-H, dense and MoE, on the host),
  judged by device-free toy goldens.
- Application `resnet` (ResNet-50), judged by a device-free toy golden.
- `F.max_pool2d` takes a `stride` (torch's default, the window).
- `BatchNorm2d`, torch's weights and running statistics, which `fold`
  folds into the conv before it at load, for YOLOX and ResNet alike.
- `Conv2d`'s gathered patches pad to whole 64-pixel GEMM tiles, and
  `flm.ProjectionGEMM` narrows its default n tile where K is short of its
  k chunk, so ResNet-50's 7x7 to 28x28 maps and 64-channel 1x1 convs build.
- Application `qwen3_5` (Qwen3.5's text decoder), judged by a device-free
  toy golden.
- `RMSNorm.plus_one(module)`: every `RMSNorm` of a loaded module scaling by
  `1 + weight`, as Gemma's and Qwen3.5's do.
- `Attention.output(o, x)`, the block's output from its heads: `o_proj`,
  or a model's own, as Qwen3.5's gates it.
- Applications `gemma3` (Gemma 3 1B) and `gemma4` (Gemma 4 E2B's text
  decoder), each judged by a device-free toy golden, their sliding layers
  within Hugging Face's window.
- `MHA` takes a window of any width, and windows one query packed (a
  decode step), on mlir-aie PR #50 at 3a4a9e0b8 or later.
- `Call.ids` and `Call.embeddings`, a call's token ids and the embedding
  rows its layers start from, which `CausalLM.layer` may read.
- Applications `smollm3` (SmolLM3 3B), `ministral3` (Ministral 3's text
  decoder, on drawn weights) and `qwen3_moe` (Qwen3-30B-A3B, on the host),
  each judged by a device-free toy golden.
- `iron.param(*shape, dtype=bfloat16)`, a weight a graph declares by shape,
  and `Graph.load_state_dict(tree, *, path="")`, which binds each one to the tensor at its
  dotted path, cast to its dtype, and raises once, naming every missing,
  extra and wrong-shaped tensor; a param held at two paths is tied, bound
  from its first. A param never loaded is named when the graph is recorded,
  and a second load is refused. `Graph.draw(seed)` and `Graph.unread()` bind
  them drawn or unwritten.
- Leaf modules in `iron.lm`, graphs that declare their weights as
  transformers names them, with `torch.nn`'s arguments, defaults and
  attribute names: `Linear(in_features, out_features, bias=True)`,
  `Embedding(num_embeddings, embedding_dim)`, `RMSNorm(normalized_shape,
  eps=None)` (the dtype's machine epsilon) and `LayerNorm(normalized_shape,
  eps=1e-5)`.
- Decoder blocks as modules in `iron.lm.blocks`, each built from a config
  and a layer index: `Attention(c, i, norms="", o_bias=False)`,
  `GatedMLP(c)` and `DecoderLayer(c, i, self_attn=None, mlp=None,
  cache=None)`, which holds its own `KVCache(c)` and the model's `Rope(c)`,
  and a model's own attention, feed-forward and memory where given. Their
  projections are biased where the config's `attention_bias` and
  `mlp_bias` say, o where `o_bias` does (`DecoderLayer`'s by
  `attention_bias`, as transformers' Llama; Qwen 2's `Qwen2Layer` keeps o
  unbiased); a subclass with fused projections builds them in
  `projections(c)`.
  `iron.lm` exports `Attention`, `GatedMLP` and `DecoderLayer`.
- `KVCache(c, window=None)`: the cache attends within `window` positions
  before a query, as `MHA` counts them (Hugging Face's `sliding_window`
  minus one).
- Per-layer RoPE: each `DecoderLayer` turns q and k by the rows its
  `rope` keys in `Call.ropes` (the model's `rotary_emb`, copied once a
  call per distinct `Rope`, unless a model sets another key; None for
  none). `Rope(c, q_scale=None)` scales a table of q's own,
  and `Rope.rows` and `Attention`'s angles are a (q, k) pair.
- `Attention(norms="v")` RMS-norms each head of v, unweighted; a layer
  that holds another layer's `KVCache` and sets `k_proj` and `v_proj` to
  None attends over that cache, projecting and writing no keys or values.
- Encoder and cross-attention blocks as modules: `NoCache(window=None)`,
  attention both ways over a call's own rows; `CrossCache(c, rows)`, an
  encoder's keys and values, written once an encoding and attended over
  their first `source` rows; `CrossAttention(c, i)`, which projects only q
  a call and the keys and values once (`keys_values`); `MLP(c)`, the plain
  `fc2(act(fc1(x)))`; `EncoderLayer(c, i)`, SigLIP's and Whisper's
  pre-LayerNorm layer over a `NoCache`; and `CrossDecoderLayer(c, i)`,
  `DecoderLayer` with `encoder_attn` over the `CrossCache` an
  `EncoderDecoder` gives it. `CausalLM.decoder_class` is the `Decoder` it
  builds (Whisper's adds its position table and a LayerNorm).
- `Linear.split(x, *rows)`, a fused projection's outputs: one `F.linear`
  per run of the weight's rows.
- `Graph.record(precision=)`, which `compile(precision=)` passes on instead of
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
- `Model.final_norm`, the module a model's final norm reads.
- `Model.renames`, a class-level table of checkpoint module renames applied
  at load, `renamed(tree, renames)`, which applies one to a copy
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
  The model class names its `config` and `hugging_face`; `fit` and
  `default_config` are its classmethods,
  and `prompt` and `cpu_reference` its methods. Each application's package exports its model class.
- `lm.main(Model)`, a model's command line, whose positional argument is
  the path or repository id `load` takes.
- `OnHost.generate`, which draws on the host.
- `Model.generate(prompt, max_tokens, sampler=None)`: text in gives text
  out, token ids give ids, and a list of `{"role", "content"}` messages is
  rendered by the checkpoint's `chat_template` (`Tokenizer.chat`, which
  needs jinja2, the `models` extra), each special token it writes its id and
  the BOS first once; `sampler=None` is greedy.
  `Model.stream` yields the same pieces as they are drawn, and
  `model.stats` holds the last call's `ttft` and `tokens_per_s`.
- `--prompt TEXT` on a model's command line.
- `-v` on a model's command line and `python -m iron.lm.tune`, which logs
  iron's INFO lines, such as each compile's.
- `repr` of a graph names its recorded shapes; of a compiled version, its
  inputs, packaging and build directory; of a `Profile`, its operators; of
  a model, its `max_seq_len` and whether it is loaded.
- `repr` of an operator's `declaration` lists its fields, tunables with the
  values each is searched over, members with their symbolic shapes, and the
  key's parameters its cores are built from.
- flm.DequantBFP and flm.LMHead declare `Testing` cases, so the catalog runs
  them; `DecodeLayer.reference()` and `DecodeLayer.dims`, a typed `LayerDims`
  with the layer type's dimensions, weight blob and KV rows; and
  `python -m iron.operators.flm.goldens record|check`, bitwise NPU2 goldens
  of the flm operators.

### Changed

- EmbeddingGemma 2's audio and vision towers, `AudioTower` and
  `VisionTower` with their `AudioConfig` and `VisionConfig`, are Gemma 4's
  and move to `iron.applications.gemma4.audio` and `.vision`; a tower built
  alone has no profile until given one. Its text `Config` and `PROFILES`
  move into `embedding_gemma2.model`, and `embedding_gemma2.config` goes.
- The `models` extra installs what `Model.load` imports: huggingface_hub
  and tokenizers as well as jinja2. A missing one fails naming the extra
  (`pip install -e '.[models]'` from a checkout).
- `iron.operators` imports every operator on import, with no lazy
  loading or `.pyi` stubs. `iron.operators.CATALOG` maps each operator's
  profile name to its class (flm's as `"flm.<name>"`); `__all__` holds
  bare names only, and `catalog_name` is gone.
- `compile(coresident=)` packs on an xclbin too (NPU1): steps that run back
  to back on one pack are one dispatch, its arrays and one sequence running
  the steps' in turn (`Runtime.merge`), cut where it would pass the kernel
  more than 16 buffers. A design taking a per-call value packs with none
  there, and `check=True` with `coresident` raises.
- `KVCache` within a window keeps only a ring of the last `ring` positions
  (a window and a chunk, to a power of two), each held twice so the
  positions a call reads are one run, copied to `staged` for `MHA`: a
  decode step streams its window, not the context. A windowed cache is in
  `CausalLM.recurrent`, so a call stays within a chunk and restarts where
  the ring still holds the window before it (`KVCache.restart`).
- A per-call bound (`x[:n]`) may be clamped (`iron.clamp(p + 1, hi=W)`),
  and a run may start at a wrapped value (`x[s % R : s % R + W]`), on
  mlir-aie's `Affine` taking a constant after its wrap (PR #50 at
  eac7fd99c or later).
- EmbeddingGemma 2's configs take Hugging Face's names where they differ
  only in name (`Config.embedding_dim`, `AudioConfig.attention_logit_cap`)
  and drop the fields nothing read (`bos`, `eos`, `pad`, `video_token`,
  `video_tokens`, `output_dim`, `fft`, `max_hz`, `mel_floor`, `pad_to`).
- `SelectiveScan` and `GatedDeltaRule` compile with
  `--reclaim-runtime-bds`, so a 2048-row prefill lowers.
- An operator's output declared `Out(like=x)` (mlir-aie's) takes the shape
  and valid rows the call gave `x`, as the elementwise operators' outputs
  do; a flat output no longer takes its first operand's shape by matching
  its size, except a copy of a view (`accept_views`), which takes the view's.
- `Image.prepare()` and `Image.link()` are private; `compile()` builds.
- `Operator.per_call_gather` is gone: a gather by input ids is `Copy`'s alone.
- `Handle` is a frozen record of `buffer` (a `Buffer`, which every handle
  on it shares), `shape`, `dtype`, `valid` (was `bounds`) and `layout`:
  `Dense(offset)`, `Strided(tap, offset, repeat, length, window)` or
  `Gather(rows)`, in place of `parent`, `start`, `tap`, `index_by`,
  `gather_by`, `repeat`, `length` and `window`. `Handle.whole(shape, dtype,
  name, role)` makes a new buffer's handle.
- Image composition is named for what it makes, so "fused" means only
  kernel fusion: `Composition` in `iron.common.image.compose` (was `Fusion`
  in `fusion`), `FullELF` and `PerStep` in `iron.common.image.link` (were
  `FusedImage` and `XclbinChain` in `fused`), `PerStepCallable`
  (`StepCallable`) and `Image` (`OperatorSequence`).
- `Image(recording, packaging)` takes `FullELF(coresident, reconfigure,
  commands, shared_words)` or `PerStep(check)`, as `packaging.plan` picks,
  in place of those keywords and `full_elf=`.
- `Value` is mlir-aie's `PerCallMember` bound to one operator, so a
  declared `per_call()` and the value a build gives a device parameter are
  one type; `op.value(name)` returns it, and an extent attribute still reads
  as its number. `iron.common.declare.value.Bound` is gone.
- Graph capture is recording, so "trace" means only hardware event tracing:
  `Graph.record()` (was `trace()`), `Recording` (`TracedGraph`), `Step`
  (`TracedStep`), `Recorder` (`Tracer`) and `graph_recorder`
  (`graph_tracer`), in `iron.common.graph.record` (`trace`).
- The autotuner's matmul bound holds on npu2_1col too: it reads the core
  clock by architecture (mlir-aie's `dev.core_mhz`), not by device name.
- `EncodeStep.angles` is `EncodeStep.ropes`: the (q, k) angles each
  layer's `rope` names, as `Call.ropes` holds a decoder's.
- An operator declares itself with mlir-aie's declaration
  (`aie.utils.compile.jit.params`): `param()` for a compile-time parameter,
  `tunable()` for one resolution or the tuner picks, `per_call()` for a
  per-call value (`per_call(bounds=X)` for an extent) and mlir-aie's
  `Select`; `Operator` is mlir-aie's library operator underneath, and
  `Unresolvable` is mlir-aie's.
- `op.replace(**changes)` copies an operator, in place of
  `dataclasses.replace(op, ...)`; `Operator.shim_columns` and
  `Operator.call_operands` are classmethods, off `declaration`.
- A graph's per-call values and their expressions are taplib's `PerCall`
  and `Affine` (`aie.helpers.taplib`): `marker` replaces `kind`, and an
  expression prints as itself (`pos + 1`).
- `iron.lm.testing.assert_close(..., share=LOGITS)`: a test's own bound,
  a share of the largest logit (ResNet's toy holds 2%).
- `Experts` leaves its hidden and width tile check to mlir-aie's
  `moe.experts`, which makes the same one.
- `GraniteHybridConfig.rope_theta` defaults to transformers' 10000.0 under
  `position_embedding_type="rope"`.
- A checkpoint's tensors at indices (`nn.ParameterList`'s) read as a list
  of those tensors: a single zero is no longer taken for an empty module,
  and a longer tensor no longer raises.
- `resolve_columns` and `shim_columns` raise `Unresolvable` where not even
  one column's streams fit the shim DMA budget, in place of returning 1.
- An `Elementwise` operand is split over every core only where it says
  `per=CORES` (`iron.common.elementwise.CORES`); an operand without `per=` is
  one lane.
- `iron.tune.autotune.Call`, a recorded graph's call as the tuner times it,
  is `Timed`, so `Call` names only `iron.lm.Call`.
- A tunable's `domain=` is a tuple, an `Enum` or a function
  `(op, dev, start) -> tuple`, such as mlir-aie's `widths` and `divisors`,
  which replace `Width` and `Divisors`; a tunable is searched only where its
  domain says so, a `per=` count or an `Enum` included.
- `Call` replaces `DecodeStep`: one call's values, keyword-only, built once in
  `CausalLM.body` and handed whole to `forward(x, call)`, `Rope.rows(call)`,
  `KVCache.attend(call, ...)` and `Checkpoints.at(call)`, in place of their
  keyword lists. LongRoPE's stacked table and `table_start` moved out of
  `Rope`, `CausalLM` and `DecoderConfig.long_angles` into Phi-4's
  `Phi4Config.angles` and `LongRopeTable`, which Phi-4's
  `CausalLM.rotary(config)` returns; `Rope.table_start(n)` is 0.
- A decoder's tuning calls are `iron.lm.tune.calls(model, position, token,
  context, points, sampler)`, on the flags `iron.lm.tune.arguments` adds;
  `contexts` moved with them. `CausalLM.tune_calls` and `tune_arguments`,
  the hook every model is tuned through, build the decoder on unread
  weights and call them, refusing a `--context` that is not whole prompt
  chunks within `max_seq_len`.
- `Tokenizer.chat` puts the BOS where the chat template writes it, and only
  there, as transformers' `apply_chat_template` does; it no longer adds one.
  The template may call `strftime_now` and writes `tokenizer_config.json`'s
  `bos_token` where it has one; `Model.load` reads the template from
  `chat_template.jinja` when `tokenizer_config.json` has none.
- `CausalLM` builds its modules, `model` (a `Decoder` of `layer_class`
  layers, `DecoderLayer` by default) and `lm_head` (the embedding where
  tied), and binds them to the checkpoint's tree with `Graph.load_state_dict`.
  The RoPE table is `CausalLM.rotary_emb`, a `Rope`, whose `rows`
  replaces `CausalLM.angles` and whose `long_past` replaces
  `CausalLM.long_past`.
- Phi-4 and LFM2 are built from modules: `Phi4Layer`, whose fused
  `qkv_proj` and `gate_up_proj` are one `Linear` each, and `Lfm2Layer`,
  whose conv layers hold a `ShortConv` that owns its `Checkpoints` state
  and derives its taps when it loads, in place of `Phi4.sanitize`,
  `Lfm2.sanitize` and `Lfm2Config.attention`. `CausalLM.recurrent` is
  the list of `Checkpoints` the model's modules hold. `Model.renames`
  keys match a run of names anywhere in a path, and a model with a
  `layer_class` renames its whole tree before loading. `Attention` turns
  only the config's `rotary_dim` columns.
- Qwen3 and Granite name their layers, `Qwen3Layer` and `GraniteLayer`,
  in place of `Qwen3Config.attention` and `GraniteConfig.attention` and
  `layer`; Granite's sets
  `Attention.scaling` and `DecoderLayer.residual_multiplier`. Qwen3
  reads `DecoderConfig`, and `Qwen3Config` is gone; Qwen 2 reads
  `Qwen2Config`, whose `attention_bias` is set.
- `DecoderConfig` reads `attention_bias`, `mlp_bias`, `sliding_window`
  and `use_sliding_window` from `config.json`. Each `DecoderLayer`'s cache
  attends within `sliding_window` (`DecoderConfig.window`). A config
  refuses at load a `rope_scaling` it builds no table for (any but
  `"default"`; `LlamaConfig`'s, any but `"llama3"`) and a set
  `use_sliding_window`, which windows only some layers.
- `Encoder` and `Tower` build their layers from `layer_class`
  (`EncoderLayer` by default), `Encoder(config, max_tokens)` and
  `Tower(config, max_tokens, soft_rows)`, a subclass loading them.
  `EncoderDecoder(config, weights, encoder)` builds `CrossDecoderLayer`s,
  each holding a `CrossCache`, in place of `cross_keys` and `cross_values`.
  Whisper and SmolVLM (its text model and vision tower) are built from
  modules.
- `SmolVLMTextConfig` reads every field under `text_config`
  (`Config.json_prefix`): a nested `rope_scaling` is refused at load, and
  a nested window is honoured.
- `YOLOXNano` is written in `iron.functional`'s CNN functions on modules
  that load the checkpoint's tree, and returns each scale's predictions as
  `(H, W, 144)`, not `(H, W * 144)`. SmolVLM's patch embed is `F.conv2d`.
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

- `Tower.front`: a tower's `body` builds its own rows.
- An operator's nested `Array` class and `array_config()`: its `build()`,
  `kernel()` and `scalars()` are on the operator itself, and `layout()`
  (mlir-aie's) is the operator as its cores see it.
- YOLOX's `folded` and `padded`: its modules fold and pad their own weights.
- `iron.common.field`, `Auto`, `Extent` and `Select`, and `Value(words=)`:
  mlir-aie's `param`, `tunable`, `per_call` and `Select`, and IRON's
  `Block(words)` for a shipped image's block of words, replace them.
- `iron.common.image.packaging.dispatches_full_elf(dev)`: mlir-aie's
  `dev.dispatches_full_elf` replaces it.
- `iron.tune.autotune.CORE_MHZ`: the bound reads mlir-aie's `dev.core_mhz`,
  times `CLOCK_HEADROOM`.
- `iron.tune.measure.others` and `wait_idle`: mlir-aie's
  `aie.utils.benchmark.other_npu_users` and `wait_idle` replace them.
- `iron.tune.measure.CPU_WAIT_US` and `Awake`: mlir-aie's
  `aie.utils.benchmark.CPU_WAIT_US` and `CompletionCores` replace them.
- `PerStep.KERNELS` (`XclbinChain`'s, before its rename): mlir-aie's
  `CompilableDesign.chain` splits a chain at the hardware context's kernel
  limit.
- `field(probe=)`: the tuner times each distinct value of such a field, as
  it does every other (Clamp's `low` and `high`).
- `CausalLM`'s `layer_class = None` path: its `decoder=` argument,
  `caches`, `attend`, `final_norm`, and `Call.angles` (a layer reads
  its own `Rope`'s rows in `Call.ropes`). Also `Encoder.attend`'s
  MHA (it is `NoCache.attend`), `EncoderDecoder.cross` and `layer`,
  `Config.layer`, `DecoderConfig.attention` and `layer`.
- Llama's tiktoken tokenizer, `SPECIAL_TOKENS` and `tokenizer()`: Llama
  reads its checkpoint's `tokenizer.json` like every model, and tiktoken is
  no longer a dependency.
- flm's `layer_dims` and `weight_layout`, replaced by `LayerDims`;
  `dequant.op.dequantize` and `qw_bytes_for`, replaced by
  `q4nx.dequantize(DequantBFP.grid(qw))` and `DequantBFP.quantized_size()`;
  and `q4nx.parts`, folded into `q4nx.unpack`.
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
- `Derived`; a module derives a tensor in its own `load_state_dict`.
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
