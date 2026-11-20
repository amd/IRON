# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 11.18 µs | 2.55 µs | ⚪ -77.19% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.58 µs | 5.97 µs | ⚪ -9.37% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 0.97 µs | 2.46 µs | ⚪ +154.99% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.29 µs | 14.11 µs | ⚪ +93.55% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.66 µs | 7.74 µs | ⚪ -19.87% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.13 µs | 1.25 µs | ⚪ +10.20% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.03 µs | 4.03 µs | ⚪ -49.78% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 395.11 µs | 786.67 µs | ⚪ +99.10% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 10.52 µs | 24.62 µs | ⚪ +134.00% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.79 µs | 22.66 µs | ⚪ +498.23% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.73 µs | 3.46 µs | ⚪ +99.74% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 12.27 µs | 2.04 µs | ⚪ -83.38% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.27 µs | 5.64 µs | ⚪ +6.94% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.64 µs | 3.05 µs | ⚪ -16.09% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 11.31 µs | 6.86 µs | ⚪ -39.34% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 32.03 µs | 208.01 µs | ⚪ +549.39% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 23.18 µs | 76.06 µs | ⚪ +228.09% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 80.62 µs | 113.17 µs | ⚪ +40.38% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.08 µs | 4.00 µs | ⚪ +271.04% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +9.23% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 97.30 µs | 89.07 µs | 🟢 -8.45% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.51 µs | 1.61 µs | ⚪ +6.31% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.09 µs | 4.25 µs | ⚪ +103.59% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.56 µs | 1.90 µs | ⚪ -70.97% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.67 µs | 5.56 µs | ⚪ +108.09% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 8.43 µs | 9.21 µs | ⚪ +9.26% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.51 µs | 1.66 µs | ⚪ -52.80% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.08 µs | 2.24 µs | ⚪ -44.97% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.36 µs | 2.89 µs | ⚪ -33.86% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 3.34 µs | 1.30 µs | ⚪ -61.16% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 6.75 µs | 9.26 µs | ⚪ +37.10% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.07 µs | 3.40 µs | ⚪ +10.78% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.72 µs | 2.91 µs | ⚪ -21.83% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.31 µs | 1.95 µs | ⚪ +49.35% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.27 µs | 4.37 µs | ⚪ +92.04% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.04 µs | 11.06 µs | ⚪ -21.23% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 23.10 µs | 24.89 µs | ⚪ +7.72% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.56 µs | 1.06 µs | ⚪ -32.37% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.15 µs | 5.42 µs | ⚪ +72.27% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.04 µs | 6.44 µs | ⚪ +59.23% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.96 µs | 13.13 µs | ⚪ +19.78% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 8.52 µs | 3.83 µs | ⚪ -55.07% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 9.76 µs | 7.63 µs | ⚪ -21.81% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 8.55 µs | 11.13 µs | ⚪ +30.18% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 8.42 µs | 12.10 µs | ⚪ +43.79% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 26.72 µs | 54.32 µs | ⚪ +103.28% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 188.68 µs | 61.58 µs | ⚪ -67.36% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 80.22 µs | 111.66 µs | ⚪ +39.19% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 47.88 µs | 38.20 µs | ⚪ -20.21% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 38.94 µs | 251.61 µs | ⚪ +546.08% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 334.16 µs | 76.74 µs | ⚪ -77.04% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 56.32 µs | 70.05 µs | ⚪ +24.38% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 73.20 µs | 79.29 µs | ⚪ +8.31% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 4.82 µs | 3.27 µs | ⚪ -32.14% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 434.13 µs | 10.74 µs | ⚪ -97.53% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 4443.48 µs | 3674.59 µs | 🟢 -17.30% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 3.34 µs | 157.34 µs | ⚪ +4608.66% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency` | 4678.62 µs | 5990.32 µs | 🔴 +28.04% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 3.42 µs | 507.59 µs | ⚪ +14756.96% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency` | 5409.53 µs | 6624.50 µs | 🔴 +22.46% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 3.80 µs | 373.04 µs | ⚪ +9710.28% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 14.14 µs | 6.66 µs | ⚪ -52.92% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5577.77 µs | 4666.89 µs | 🟢 -16.33% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.03 µs | 3.59 µs | ⚪ +18.35% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 6771.42 µs | 7674.77 µs | 🔴 +13.34% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 10.25 µs | 16.91 µs | ⚪ +64.95% |

