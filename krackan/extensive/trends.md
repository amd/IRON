# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 12.19 µs | 9.88 µs | ⚪ -18.90% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.66 µs | 3.29 µs | ⚪ -9.98% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.39 µs | 2.05 µs | ⚪ -14.27% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 0.89 µs | 3.63 µs | ⚪ +307.17% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.24 µs | 4.80 µs | ⚪ -33.76% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 3.21 µs | 2.65 µs | ⚪ -17.33% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.63 µs | 5.09 µs | ⚪ -9.54% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 12.37 µs | 663.22 µs | ⚪ +5262.40% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 13.32 µs | 81.95 µs | ⚪ +515.19% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.42 µs | 14.52 µs | ⚪ +920.59% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 8.32 µs | 3.16 µs | ⚪ -62.01% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 16.87 µs | 7.69 µs | ⚪ -54.39% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 5.75 µs | 2.89 µs | ⚪ -49.70% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.52 µs | 5.26 µs | ⚪ +49.70% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.38 µs | 2.40 µs | ⚪ +74.17% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 12.80 µs | 9.41 µs | ⚪ -26.46% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.42 µs | 3.21 µs | ⚪ -6.14% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 125.68 µs | 96.56 µs | ⚪ -23.17% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.06 µs | 3.30 µs | ⚪ +60.31% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 GB/s | 0.17 GB/s | 🔴 -6.14% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 89.66 µs | 95.53 µs | 🔴 +6.54% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.26 µs | 2.56 µs | ⚪ +13.27% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 16.36 µs | 1.78 µs | ⚪ -89.13% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.90 µs | 3.18 µs | ⚪ -53.89% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.01 µs | 3.54 µs | ⚪ +17.49% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.56 µs | 3.75 µs | ⚪ +140.05% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 18.31 µs | 69.36 µs | ⚪ +278.74% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 3.84 µs | 6.25 µs | ⚪ +62.69% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.85 µs | 2.52 µs | ⚪ -11.46% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.64 µs | 6.39 µs | ⚪ +37.67% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.17 µs | 8.52 µs | ⚪ +18.80% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.47 µs | 0.76 µs | ⚪ -48.09% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 5.93 µs | 9.72 µs | ⚪ +63.98% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.38 µs | 9.12 µs | ⚪ +282.57% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.65 µs | 4.53 µs | ⚪ +71.11% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.58 µs | 3.76 µs | ⚪ +5.05% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 10.21 µs | 11.80 µs | ⚪ +15.50% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 22.22 µs | 34.78 µs | ⚪ +56.55% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.70 µs | 1.17 µs | ⚪ -31.00% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.72 µs | 3.30 µs | ⚪ -50.90% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.90 µs | 11.35 µs | ⚪ +43.68% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 85.38 µs | 15.03 µs | ⚪ -82.39% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.77 µs | 2.94 µs | ⚪ -78.69% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 12.53 µs | 8.72 µs | ⚪ -30.41% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 2.08 µs | 6.76 µs | ⚪ +224.36% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 6.66 µs | 4.03 µs | ⚪ -39.56% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 75.34 µs | 55.34 µs | ⚪ -26.55% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 336.69 µs | 79.24 µs | ⚪ -76.47% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 37.29 µs | 70.54 µs | ⚪ +89.20% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 41.77 µs | 94.48 µs | ⚪ +126.21% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 48.81 µs | 34.91 µs | ⚪ -28.48% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 123.38 µs | 26.51 µs | ⚪ -78.51% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 61.18 µs | 109.56 µs | ⚪ +79.07% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 4256.75 µs | 5107.66 µs | 🔴 +19.99% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 61.57 µs | 2.87 µs | ⚪ -95.35% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 4.84 µs | 758.97 µs | ⚪ +15584.51% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 3525.11 µs | 4445.63 µs | 🔴 +26.11% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.43 µs | 2.23 µs | ⚪ -8.42% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 11.77 µs | 5.20 µs | ⚪ -55.77% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency` | 6502.87 µs | 5420.73 µs | 🟢 -16.64% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 493.17 µs | 8.46 µs | ⚪ -98.28% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency` | 8230.57 µs | 7326.82 µs | 🟢 -10.98% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 32.93 µs | 9.32 µs | ⚪ -71.70% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 2.07 µs | 3.80 µs | ⚪ +83.76% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 477.89 µs | 25.43 µs | ⚪ -94.68% |

