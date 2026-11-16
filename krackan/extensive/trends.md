# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.27 µs | 6.54 µs | ⚪ +100.14% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 20.03 µs | 10.45 µs | ⚪ -47.80% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.94 µs | 1.78 µs | ⚪ -8.30% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.68 µs | 1.73 µs | ⚪ -35.41% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.13 µs | 2.62 µs | ⚪ -67.85% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.21 µs | 13.13 µs | ⚪ +17.21% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 8.83 µs | 4.41 µs | ⚪ -50.03% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.57 µs | 1.57 µs | ⚪ -65.62% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 11.68 GB/s | 10.69 GB/s | 🔴 -8.55% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 2961.47 µs | 3238.45 µs | 🔴 +9.35% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 11.44 µs | 21.40 µs | ⚪ +87.14% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 6526.26 GOP/s | 5968.10 GOP/s | 🔴 -8.55% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.81 GB/s | 8.77 GB/s | 🔴 -31.54% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1965.21 µs | 2870.47 µs | 🔴 +46.06% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 4.13 µs | 15.44 µs | ⚪ +273.61% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8742.01 GOP/s | 5985.03 GOP/s | 🔴 -31.54% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 2.66 µs | 11.39 µs | ⚪ +327.26% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 2.38 µs | 1.45 µs | ⚪ -39.30% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 1.97 µs | 3.40 µs | ⚪ +72.13% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 5.72 µs | 5.10 µs | ⚪ -10.94% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.91 µs | 7.05 µs | ⚪ +80.39% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.51 µs | 7.94 µs | ⚪ +126.11% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 7.64 µs | 14.79 µs | ⚪ +93.51% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.38 µs | 20.47 µs | ⚪ +367.05% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 52.26 µs | 43.23 µs | ⚪ -17.28% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 116.90 µs | 79.08 µs | ⚪ -32.35% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 10.78 µs | 2.45 µs | ⚪ -77.26% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +7.73% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 96.76 µs | 89.82 µs | 🟢 -7.18% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.93 µs | 2.70 µs | ⚪ +39.75% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 12.71 µs | 2.19 µs | ⚪ -82.78% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.85 µs | 4.34 µs | ⚪ -25.84% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.90 µs | 3.30 µs | ⚪ -32.61% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 11.15 µs | 2.71 µs | ⚪ -75.74% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 14.04 µs | 22.57 µs | ⚪ +60.81% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 26.01 µs | 1.51 µs | ⚪ -94.20% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.69 µs | 2.47 µs | ⚪ +46.55% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.32 µs | 12.05 µs | ⚪ +90.57% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 2.36 µs | 1.75 µs | ⚪ -25.75% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 14.64 µs | 2.90 µs | ⚪ -80.15% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.26 µs | 4.81 µs | ⚪ -23.07% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.53 µs | 3.05 µs | ⚪ -13.64% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.74 µs | 1.00 µs | ⚪ -42.35% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.19 µs | 2.33 µs | ⚪ +6.17% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 16.14 µs | 10.90 µs | ⚪ -32.45% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 28.41 µs | 32.16 µs | ⚪ +13.19% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.99 µs | 12.60 µs | ⚪ +531.85% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.63 µs | 2.04 µs | ⚪ -73.22% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.76 µs | 2.87 µs | ⚪ -23.84% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 180.93 µs | 18.91 µs | ⚪ -89.55% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 3.31 µs | 2.01 µs | ⚪ -39.21% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 15.13 µs | 1.68 µs | ⚪ -88.91% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 7.58 µs | 5.19 µs | ⚪ -31.53% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 5.04 µs | 8.75 µs | ⚪ +73.50% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 58.76 µs | 71.42 µs | ⚪ +21.54% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 52.12 µs | 129.03 µs | ⚪ +147.55% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 184.01 µs | 196.64 µs | ⚪ +6.86% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 23.77 µs | 13.47 µs | ⚪ -43.35% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 188.88 µs | 32.89 µs | ⚪ -82.59% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 58.44 µs | 131.12 µs | ⚪ +124.36% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 74.22 µs | 464.06 µs | ⚪ +525.24% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 145.22 µs | 241.33 µs | ⚪ +66.19% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 5.41 µs | 2.00 µs | ⚪ -62.94% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 8.22 µs | 9.72 µs | ⚪ +18.23% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 3.05 µs | 260.50 µs | ⚪ +8450.80% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 5.35 µs | 2.19 µs | ⚪ -58.96% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 3.66 µs | 7.76 µs | ⚪ +112.06% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 369.40 µs | 45.91 µs | ⚪ -87.57% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.02 µs | 4.39 µs | ⚪ +45.27% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 6.02 µs | 162.79 µs | ⚪ +2603.55% |

