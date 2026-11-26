# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 13.95 µs | 8.36 µs | ⚪ -40.05% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.12 µs | 7.47 µs | ⚪ +22.02% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 12.39 µs | 2.08 µs | ⚪ -83.22% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.81 µs | 1.19 µs | ⚪ -34.49% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.29 µs | 3.04 µs | ⚪ -58.29% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.44 µs | 2.51 µs | ⚪ -66.30% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 8.52 µs | 2.13 µs | ⚪ -75.01% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.83 µs | 1.75 µs | ⚪ -77.69% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 12.86 µs | 31.42 µs | ⚪ +144.27% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 21.00 µs | 17.53 µs | ⚪ -16.55% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 6.37 µs | 3.58 µs | ⚪ -43.74% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 2.19 µs | 3.84 µs | ⚪ +75.51% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 1.34 µs | 2.31 µs | ⚪ +72.61% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 6.46 µs | 3.37 µs | ⚪ -47.82% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.56 µs | 4.99 µs | ⚪ +9.44% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.18 µs | 3.08 µs | ⚪ +161.88% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 6.48 µs | 13.34 µs | ⚪ +105.80% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 41.80 µs | 37.87 µs | ⚪ -9.40% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 52.81 µs | 86.17 µs | ⚪ +63.17% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 137.52 µs | 100.00 µs | ⚪ -27.28% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 0.87 µs | 7.34 µs | ⚪ +742.14% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.19 GB/s | 0.17 GB/s | 🔴 -8.45% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 88.55 µs | 96.72 µs | 🔴 +9.23% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.29 µs | 1.69 µs | ⚪ +31.15% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.82 µs | 1.43 µs | ⚪ -49.38% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.82 µs | 8.07 µs | ⚪ +111.00% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.57 µs | 2.98 µs | ⚪ +15.82% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.23 µs | 11.57 µs | ⚪ +173.58% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 11.61 µs | 8.84 µs | ⚪ -23.82% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.06 µs | 0.88 µs | ⚪ -17.16% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.56 µs | 1.90 µs | ⚪ +21.93% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.57 µs | 5.98 µs | ⚪ +132.76% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.25 µs | 3.67 µs | ⚪ -55.47% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.73 µs | 1.60 µs | ⚪ +118.31% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 12.56 µs | 1.89 µs | ⚪ -84.93% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.22 µs | 3.32 µs | ⚪ +49.12% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.89 µs | 2.19 µs | ⚪ -62.73% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.91 µs | 1.57 µs | ⚪ +72.93% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.47 µs | 2.51 µs | ⚪ -27.58% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 17.65 µs | 12.23 µs | ⚪ -30.71% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 25.66 µs | 20.82 µs | ⚪ -18.86% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.80 µs | 2.49 µs | ⚪ +38.06% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.17 µs | 3.49 µs | ⚪ -32.55% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.12 µs | 4.68 µs | ⚪ -23.42% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.03 µs | 70.19 µs | ⚪ +1064.76% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 1.79 µs | 12.33 µs | ⚪ +589.51% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 5.51 µs | 3.36 µs | ⚪ -39.04% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 6.19 µs | 11.37 µs | ⚪ +83.73% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 186.33 µs | 32.69 µs | ⚪ -82.46% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 38.64 µs | 36.63 µs | ⚪ -5.20% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 75.08 µs | 18.42 µs | ⚪ -75.47% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 153.04 µs | 131.16 µs | ⚪ -14.29% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 26.15 µs | 50.52 µs | ⚪ +93.20% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 36.14 µs | 40.74 µs | ⚪ +12.73% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 46.31 µs | 65.86 µs | ⚪ +42.21% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 34.53 µs | 67.57 µs | ⚪ +95.71% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 486.18 µs | 1205.19 µs | ⚪ +147.89% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 6993.37 µs | 5217.42 µs | 🟢 -25.39% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 4.32 µs | 6.22 µs | ⚪ +44.00% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 4437.36 µs | 3536.60 µs | 🟢 -20.30% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 4.75 µs | 9.42 µs | ⚪ +98.42% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 4.57 µs | 18.12 µs | ⚪ +296.15% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 642.89 µs | 3.75 µs | ⚪ -99.42% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 11.56 µs | 592.51 µs | ⚪ +5026.60% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4674.25 µs | 5577.37 µs | 🔴 +19.32% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.29 µs | 1.85 µs | ⚪ -43.58% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 7869.65 µs | 6889.32 µs | 🟢 -12.46% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 127.67 µs | 143.41 µs | ⚪ +12.33% |

