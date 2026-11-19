# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1.96 µs | 11.18 µs | ⚪ +470.62% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1.83 µs | 6.58 µs | ⚪ +259.99% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.48 µs | 0.97 µs | ⚪ -34.59% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.13 µs | 2.34 µs | ⚪ +10.12% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.01 µs | 7.29 µs | ⚪ -19.09% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.58 µs | 9.66 µs | ⚪ -16.57% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.96 µs | 1.13 µs | ⚪ -61.70% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.95 µs | 8.03 µs | ⚪ +172.57% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 15.83 µs | 395.11 µs | ⚪ +2395.93% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 22.87 µs | 10.52 µs | ⚪ -53.99% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.02 µs | 3.79 µs | ⚪ +25.60% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 7.84 µs | 1.73 µs | ⚪ -77.90% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 8.17 µs | 5.53 µs | ⚪ -32.32% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 6.00 µs | 12.27 µs | ⚪ +104.59% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.96 µs | 5.27 µs | ⚪ -11.59% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.17 µs | 3.64 µs | ⚪ -12.75% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 8.11 µs | 11.31 µs | ⚪ +39.48% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 23.53 µs | 32.03 µs | ⚪ +36.10% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 43.89 µs | 23.18 µs | ⚪ -47.19% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 146.12 µs | 80.62 µs | ⚪ -44.83% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.09 µs | 1.08 µs | ⚪ -48.42% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.66 µs | 1.51 µs | ⚪ -43.24% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.69 GB/s | 0.64 GB/s | 🔴 -8.27% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 73.70 µs | 80.35 µs | 🔴 +9.02% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 0.91 µs | 2.09 µs | ⚪ +130.32% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.88 µs | 3.59 µs | ⚪ +24.53% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.99 µs | 6.56 µs | ⚪ +119.29% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.32 µs | 2.67 µs | ⚪ -19.60% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 23.10 µs | 8.43 µs | ⚪ -63.53% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.98 µs | 2.27 µs | ⚪ +131.18% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.54 µs | 3.51 µs | ⚪ +128.35% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.80 µs | 4.08 µs | ⚪ -29.65% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.62 µs | 4.36 µs | ⚪ +66.21% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 7.46 µs | 3.34 µs | ⚪ -55.23% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.69 µs | 6.75 µs | ⚪ +298.73% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.42 µs | 3.07 µs | ⚪ -58.67% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.22 µs | 3.72 µs | ⚪ -11.87% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.67 µs | 1.31 µs | ⚪ +94.79% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.59 µs | 2.27 µs | ⚪ +43.28% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 12.67 µs | 14.04 µs | ⚪ +10.84% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 32.17 µs | 23.10 µs | ⚪ -28.17% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 3.11 µs | 1.56 µs | ⚪ -49.68% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.92 µs | 3.15 µs | ⚪ -46.86% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.17 µs | 4.04 µs | ⚪ +27.48% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 11.69 µs | 10.96 µs | ⚪ -6.25% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 1.77 µs | 8.52 µs | ⚪ +381.57% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 16.06 µs | 9.76 µs | ⚪ -39.21% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 5.80 µs | 8.55 µs | ⚪ +47.45% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 7.14 µs | 8.42 µs | ⚪ +17.90% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 15.20 µs | 26.72 µs | ⚪ +75.81% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 30.26 µs | 188.68 µs | ⚪ +523.58% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 20.30 µs | 80.22 µs | ⚪ +295.22% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 108.37 µs | 47.88 µs | ⚪ -55.82% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 34.20 µs | 38.94 µs | ⚪ +13.85% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 29.12 µs | 334.16 µs | ⚪ +1047.71% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 40.16 µs | 56.32 µs | ⚪ +40.24% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 388.21 µs | 73.20 µs | ⚪ -81.14% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 5904.41 µs | 4205.70 µs | 🟢 -28.77% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 12.02 µs | 4.82 µs | ⚪ -59.90% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 5211.33 µs | 6562.92 µs | 🔴 +25.94% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 5.40 µs | 434.13 µs | ⚪ +7938.72% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 3524.74 µs | 4443.48 µs | 🔴 +26.07% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.69 µs | 3.34 µs | ⚪ +24.22% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency` | 5602.28 µs | 4678.62 µs | 🟢 -16.49% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 4.67 µs | 3.42 µs | ⚪ -26.83% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 606.49 µs | 3.80 µs | ⚪ -99.37% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 7.63 µs | 14.14 µs | ⚪ +85.35% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4665.80 µs | 5577.77 µs | 🔴 +19.55% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.30 µs | 3.03 µs | ⚪ -8.07% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 13.30 µs | 10.25 µs | ⚪ -22.96% |

