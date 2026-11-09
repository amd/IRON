# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.15 µs | 3.83 µs | ⚪ +78.11% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.75 µs | 4.10 µs | ⚪ -39.23% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 5.07 µs | 3.00 µs | ⚪ -40.82% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.27 µs | 2.01 µs | ⚪ +57.88% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.06 µs | 2.68 µs | ⚪ -12.60% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.53 µs | 12.23 µs | ⚪ +43.40% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.19 µs | 3.49 µs | ⚪ -32.73% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.15 µs | 1.70 µs | ⚪ -58.99% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 10.69 GB/s | 10.15 GB/s | 🔴 -5.08% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3236.49 µs | 3409.69 µs | 🔴 +5.35% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 9.04 µs | 5.91 µs | ⚪ -34.66% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5971.70 GOP/s | 5668.36 GOP/s | 🔴 -5.08% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 7.88 µs | 9.65 µs | ⚪ +22.51% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 14.88 µs | 5.71 µs | ⚪ -61.62% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 15.22 µs | 5.63 µs | ⚪ -63.00% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 10.23 µs | 2.67 µs | ⚪ -73.90% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.05 µs | 11.56 µs | ⚪ +278.96% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.56 µs | 4.73 µs | ⚪ -37.38% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.01 µs | 5.64 µs | ⚪ +40.57% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 25.74 µs | 12.23 µs | ⚪ -52.47% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 179.34 µs | 37.93 µs | ⚪ -78.85% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 49.16 µs | 17.51 µs | ⚪ -64.39% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 67.95 µs | 171.15 µs | ⚪ +151.88% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.44 µs | 3.94 µs | ⚪ +61.61% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.93 µs | 2.86 µs | ⚪ +48.14% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.59 µs | 5.99 µs | ⚪ +131.29% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 21.42 µs | 1.71 µs | ⚪ -92.02% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 19.39 µs | 25.92 µs | ⚪ +33.69% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.05 µs | 1.15 µs | ⚪ +9.55% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.97 µs | 2.23 µs | ⚪ -24.65% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.62 µs | 14.38 µs | ⚪ +49.40% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.74 µs | 3.98 µs | ⚪ -48.58% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 4.05 µs | 1.96 µs | ⚪ -51.68% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 8.34 µs | 10.44 µs | ⚪ +25.23% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.57 µs | 1.77 µs | ⚪ -50.35% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.40 µs | 1.84 µs | ⚪ -23.54% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.25 µs | 1.37 µs | ⚪ -39.20% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.78 GB/s | 3.18 GB/s | 🔴 -33.48% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 439.10 µs | 660.06 µs | 🔴 +50.32% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 21.65 µs | 24.22 µs | ⚪ +11.90% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 0.96 µs | 2.44 µs | ⚪ +154.91% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.08 µs | 8.16 µs | ⚪ +100.11% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 14.30 µs | 11.89 µs | ⚪ -16.85% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 4.01 µs | 11.53 µs | ⚪ +187.24% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 11.66 µs | 10.12 µs | ⚪ -13.15% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 3.85 µs | 2.96 µs | ⚪ -23.15% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 8.32 µs | 9.98 µs | ⚪ +19.93% |

