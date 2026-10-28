# Performance trends

**Operators added:** `AXPY`, `Clamp`, `Copy`, `DepthwiseConv1d`, `ElementwiseAdd`, `ElementwiseMul`, `Emit`, `GELU`, `GEMM`, `GEMV`, `LayerNorm`, `Limbs`, `Log`, `MHA`, `Magnitude`, `Merge`, `PatchPositions`, `RMSNorm`, `ReLU`, `Resample`, `ResampleTaps`, `RoPE`, `RowwiseAdd`, `RowwiseMul`, `Sample`, `SiLU`, `Sigmoid`, `Softmax`, `Tanh`, `allocator_planning`, `array_identity`, `bound_rounds_up`, `build`, `build_pages`, `carried_loop`, `carried_values`, `checking`, `ci_results`, `composed_kernel_names`, `composition_identity`, `config`, `conftest_lazy_device`, `conv2d`, `conv2d_graph`, `copy_bounded_view`, `copy_channels`, `copy_gather`, `copy_offset`, `copy_taps`, `declare`, `decoder`, `dispatch`, `dispatch_params`, `elementwise`, `encoder`, `feedback`, `flm.DequantBFP`, `flm.LMHead`, `flm_dequant_layout`, `flm_gemm_bounded_rows`, `flm_gemm_l1`, `full_elf`, `full_elf_dtypes`, `gemm_bounded_k`, `gemm_bounded_rows`, `golden`, `graph`, `graph_dispatch`, `graph_versions`, `host_steps`, `image_patches_graph`, `inline_kernel`, `jit_compile_path`, `judging`, `layer`, `llama_reference`, `lm_host`, `loading`, `log_mel`, `lowering`, `lowering_graph`, `mha_bounded_rows`, `mha_buffer_shapes`, `mha_long_context`, `modules`, `multimodal`, `nested_graphs`, `no_torch_on_import`, `on_npu`, `operators_declared`, `packaging`, `rejected_shapes`, `resample_patch_rows`, `resample_reference_raster`, `rope_angles`, `rope_bounded_rows`, `rope_reference_convention`, `runtime_repeat`, `sample_edge_cases`, `sequence`, `sequence_output_sync`, `softmax_positions`, `swiglu_no_padding`, `test_every_operator_is_in_the_catalog`, `testing`, `timing_gate`, `tracing`, `vectors`, `visualize`, `xclbin`

**Operators dropped:** `axpy`, `dequant`, `elementwise_add`, `elementwise_mul`, `gelu`, `gemm`, `gemv`, `layer_norm`, `leaky_relu`, `mem_copy`, `mha`, `relu`, `repeat`, `rms_norm`, `rope`, `sigmoid`, `silu`, `softmax`, `strided_copy`, `swiglu_decode`, `swiglu_prefill`, `tanh`, `transpose`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `flm/layer` | `gemma4_e2b-global-700` | `Bandwidth` | 28.68 | 44.24 | 🟢 +54.26% |
| `flm/layer` | `gemma4_e2b-global-700` | `Throughput` | 93.37 | 144.04 | 🟢 +54.26% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Bandwidth` | 31.42 | 47.94 | 🟢 +52.59% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency` | 802.48 | 521.51 | 🟢 -35.01% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Throughput` | 97.18 | 148.28 | 🟢 +52.59% |

