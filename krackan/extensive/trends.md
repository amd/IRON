# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.75 µs | 9.48 µs | ⚪ +244.21% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.65 µs | 6.28 µs | ⚪ -5.50% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.52 µs | 4.17 µs | ⚪ -7.86% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.30 µs | 10.76 µs | ⚪ +368.05% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.08 µs | 6.70 µs | ⚪ -33.51% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.72 µs | 16.56 µs | ⚪ +54.48% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.94 µs | 0.82 µs | ⚪ -72.07% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.00 µs | 7.04 µs | ⚪ +40.82% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 9.87 GB/s | 10.67 GB/s | 🟢 +8.03% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3504.39 µs | 3244.03 µs | 🟢 -7.43% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 29.61 µs | 5.94 µs | ⚪ -79.95% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5515.18 GOP/s | 5957.83 GOP/s | 🟢 +8.03% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 16.61 µs | 202.12 µs | ⚪ +1116.77% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 15.40 µs | 14.21 µs | ⚪ -7.75% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 13.43 µs | 3.15 µs | ⚪ -76.54% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 6.44 µs | 10.85 µs | ⚪ +68.59% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 5.36 µs | 3.93 µs | ⚪ -26.62% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.36 µs | 3.62 µs | ⚪ -50.81% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.81 µs | 3.17 µs | ⚪ +74.61% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 4.03 µs | 8.80 µs | ⚪ +118.55% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 30.17 µs | 15.36 µs | ⚪ -49.10% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 58.40 µs | 84.75 µs | ⚪ +45.11% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.12 µs | 1.57 µs | ⚪ -25.77% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.32 µs | 3.39 µs | ⚪ +45.72% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 71.44 µs | 67.69 µs | 🟢 -5.24% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 0.95 µs | 1.84 µs | ⚪ +93.32% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.55 µs | 3.54 µs | ⚪ -45.98% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.36 µs | 3.66 µs | ⚪ +55.01% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.01 µs | 8.79 µs | ⚪ +191.91% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 35.71 µs | 26.16 µs | ⚪ -26.75% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.72 µs | 13.80 µs | ⚪ +1826.31% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.14 µs | 1.41 µs | ⚪ -34.20% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.32 µs | 6.76 µs | ⚪ +56.50% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.73 µs | 1.43 µs | ⚪ -75.06% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.71 µs | 1.15 µs | ⚪ +61.21% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.96 µs | 8.10 µs | ⚪ +174.04% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.75 µs | 23.10 µs | ⚪ +1217.66% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.36 µs | 1.22 µs | ⚪ -10.31% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.80 µs | 3.49 µs | ⚪ -39.80% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 3.74 GB/s | 4.78 GB/s | 🟢 +27.91% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 560.68 µs | 438.35 µs | 🟢 -21.82% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 6.04 µs | 11.74 µs | ⚪ +94.29% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 21.68 µs | 32.76 µs | ⚪ +51.12% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 7.54 µs | 1.61 µs | ⚪ -78.62% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.73 µs | 8.26 µs | ⚪ +22.63% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.73 µs | 4.77 µs | ⚪ +74.71% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.12 µs | 12.86 µs | ⚪ +27.14% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.02 µs | 3.95 µs | ⚪ -69.65% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 10.30 µs | 4.74 µs | ⚪ -53.99% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 4.66 µs | 4.05 µs | ⚪ -13.11% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 13.09 µs | 5.22 µs | ⚪ -60.17% |

