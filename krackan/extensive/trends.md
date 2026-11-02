# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.61 µs | 6.25 µs | ⚪ +139.76% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 4.48 µs | 11.79 µs | ⚪ +163.03% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 8.29 µs | 2.12 µs | ⚪ -74.36% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Bandwidth` | 44.11 GB/s | 46.53 GB/s | 🟢 +5.50% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency` | 71.55 µs | 67.82 µs | 🟢 -5.21% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Throughput` | 109.91 GOP/s | 115.95 GOP/s | 🟢 +5.50% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.03 µs | 6.67 µs | ⚪ -26.07% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.48 µs | 18.43 µs | ⚪ +643.15% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.11 GB/s | 0.12 GB/s | 🟢 +9.85% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 18.38 µs | 16.74 µs | 🟢 -8.96% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.50 µs | 2.57 µs | ⚪ +71.23% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.90 µs | 2.56 µs | ⚪ -62.92% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 454.91 µs | 22.69 µs | ⚪ -95.01% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 6.87 GB/s | 8.67 GB/s | 🟢 +26.12% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 3661.45 µs | 2903.07 µs | 🟢 -20.71% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 19.22 µs | 434.34 µs | ⚪ +2160.24% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 4692.09 GOP/s | 5917.83 GOP/s | 🟢 +26.12% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.76 µs | 13.68 µs | ⚪ +677.87% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.55 µs | 3.79 µs | ⚪ +144.20% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 9.52 µs | 14.83 µs | ⚪ +55.70% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.12 µs | 4.44 µs | ⚪ +42.22% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.37 µs | 2.77 µs | ⚪ -36.67% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.05 µs | 5.56 µs | ⚪ +170.45% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 3.17 µs | 5.83 µs | ⚪ +84.03% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 16.08 µs | 2.88 µs | ⚪ -82.08% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 70.85 µs | 57.28 µs | ⚪ -19.15% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 102.28 µs | 107.60 µs | ⚪ +5.19% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.28 µs | 17.94 µs | ⚪ +1304.23% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 GB/s | 0.17 GB/s | 🔴 -6.29% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 90.09 µs | 96.14 µs | 🔴 +6.72% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 3.34 µs | 2.04 µs | ⚪ -38.84% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.01 µs | 4.81 µs | ⚪ +378.29% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.10 µs | 8.30 µs | ⚪ +16.85% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.27 µs | 4.58 µs | ⚪ +101.30% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.27 µs | 4.02 µs | ⚪ +23.16% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 60.33 µs | 29.61 µs | ⚪ -50.92% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 7.01 µs | 0.98 µs | ⚪ -86.06% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.70 µs | 1.50 µs | ⚪ -12.04% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 11.12 µs | 2.88 µs | ⚪ -74.13% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.72 µs | 1.69 µs | ⚪ +135.82% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 6.27 µs | 3.92 µs | ⚪ -37.50% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.63 µs | 6.54 µs | ⚪ +41.23% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 3.90 µs | 5.18 µs | ⚪ +32.87% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.97 µs | 3.68 µs | ⚪ +23.76% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.14 µs | 9.99 µs | ⚪ -29.37% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 42.43 µs | 19.51 µs | ⚪ -54.02% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.47 µs | 3.62 µs | ⚪ +46.37% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.14 µs | 2.15 µs | ⚪ -31.42% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.81 µs | 15.28 µs | ⚪ +217.79% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.24 µs | 16.28 µs | ⚪ +58.97% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 10.33 GB/s | 5.50 GB/s | 🔴 -46.79% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 913.47 µs | 1716.80 µs | 🔴 +87.94% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 2355.49 GOP/s | 1253.31 GOP/s | 🔴 -46.79% |

