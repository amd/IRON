# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 13.52 µs | 2.15 µs | ⚪ -84.10% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 8.41 µs | 6.75 µs | ⚪ -19.71% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 7.23 µs | 5.07 µs | ⚪ -29.91% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 3.63 µs | 1.27 µs | ⚪ -64.97% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.50 µs | 3.06 µs | ⚪ -64.00% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 12.12 µs | 8.53 µs | ⚪ -29.63% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.68 µs | 5.19 µs | ⚪ +93.69% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.71 µs | 4.15 µs | ⚪ -46.14% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 5.08 µs | 9.04 µs | ⚪ +77.75% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.77 GB/s | 8.79 GB/s | 🔴 -31.15% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1971.03 µs | 2862.89 µs | 🔴 +45.25% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 3.16 µs | 7.88 µs | ⚪ +149.21% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8716.17 GOP/s | 6000.88 GOP/s | 🔴 -31.15% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.62 µs | 14.88 µs | ⚪ +819.85% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 2.95 µs | 15.22 µs | ⚪ +416.70% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 7.05 µs | 10.23 µs | ⚪ +45.04% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.19 µs | 3.05 µs | ⚪ -27.24% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.61 µs | 7.56 µs | ⚪ +14.42% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 11.38 µs | 4.01 µs | ⚪ -64.73% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 7.01 µs | 25.74 µs | ⚪ +267.29% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 29.15 µs | 179.34 µs | ⚪ +515.22% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 64.96 µs | 49.16 µs | ⚪ -24.32% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 62.39 µs | 67.95 µs | ⚪ +8.91% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.07 µs | 2.44 µs | ⚪ +17.91% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 95.67 µs | 100.63 µs | 🔴 +5.19% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.26 µs | 1.93 µs | ⚪ -14.59% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.07 µs | 1.95 µs | ⚪ +82.14% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.67 µs | 2.59 µs | ⚪ -66.25% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.10 µs | 21.42 µs | ⚪ +1852.19% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.64 µs | 10.18 µs | ⚪ +179.66% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 28.18 µs | 19.39 µs | ⚪ -31.20% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 3.31 µs | 1.05 µs | ⚪ -68.34% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.19 µs | 2.97 µs | ⚪ +148.78% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.37 µs | 9.62 µs | ⚪ +30.51% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.30 µs | 7.74 µs | ⚪ +135.00% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.69 µs | 4.05 µs | ⚪ +139.37% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 8.93 µs | 8.34 µs | ⚪ -6.67% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.00 µs | 5.80 µs | ⚪ -17.12% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 12.40 µs | 3.57 µs | ⚪ -71.19% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.39 µs | 2.40 µs | ⚪ +72.61% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.65 µs | 2.25 µs | ⚪ -38.41% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.21 GB/s | 4.78 GB/s | 🟢 +13.44% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 498.12 µs | 439.10 µs | 🟢 -11.85% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.69 µs | 0.96 µs | ⚪ -43.47% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.55 µs | 4.08 µs | ⚪ +59.95% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.19 µs | 6.88 µs | ⚪ +11.15% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 12.37 µs | 14.30 µs | ⚪ +15.59% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.85 µs | 4.01 µs | ⚪ -71.02% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 6.87 µs | 11.66 µs | ⚪ +69.73% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 5.22 µs | 3.85 µs | ⚪ -26.26% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 10.32 µs | 8.32 µs | ⚪ -19.41% |

