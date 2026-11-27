# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 8.36 µs | 14.34 µs | ⚪ +71.47% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 7.47 µs | 10.53 µs | ⚪ +40.99% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.19 µs | 1.91 µs | ⚪ +61.15% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.04 µs | 8.55 µs | ⚪ +181.12% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.51 µs | 8.84 µs | ⚪ +252.46% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.13 µs | 3.32 µs | ⚪ +56.01% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.75 µs | 4.63 µs | ⚪ +164.79% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 31.42 µs | 7.75 µs | ⚪ -75.32% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 17.53 µs | 13.85 µs | ⚪ -21.01% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.58 µs | 1.40 µs | ⚪ -60.99% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.31 µs | 5.39 µs | ⚪ +133.58% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.37 µs | 1.65 µs | ⚪ -50.98% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.99 µs | 5.56 µs | ⚪ +11.23% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.08 µs | 4.61 µs | ⚪ +49.76% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 13.34 µs | 5.73 µs | ⚪ -57.04% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 37.87 µs | 8.95 µs | ⚪ -76.38% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 86.17 µs | 45.41 µs | ⚪ -47.30% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 100.00 µs | 145.09 µs | ⚪ +45.09% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 7.34 µs | 2.26 µs | ⚪ -69.24% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +8.00% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 96.72 µs | 89.56 µs | 🟢 -7.41% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.69 µs | 2.96 µs | ⚪ +75.60% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.43 µs | 9.25 µs | ⚪ +548.00% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.07 µs | 6.85 µs | ⚪ -15.10% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.98 µs | 1.66 µs | ⚪ -44.27% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 11.57 µs | 2.56 µs | ⚪ -77.91% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 8.84 µs | 36.36 µs | ⚪ +311.20% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.88 µs | 11.12 µs | ⚪ +1168.89% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.90 µs | 2.11 µs | ⚪ +11.32% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.67 µs | 8.80 µs | ⚪ +139.57% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.60 µs | 2.25 µs | ⚪ +41.05% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.89 µs | 8.65 µs | ⚪ +357.00% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.57 µs | 0.82 µs | ⚪ -47.63% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.51 µs | 5.90 µs | ⚪ +134.51% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.93 GB/s | 4.63 GB/s | 🔴 -5.98% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 425.72 µs | 452.79 µs | 🔴 +6.36% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 12.23 µs | 16.99 µs | ⚪ +38.96% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 20.82 µs | 22.65 µs | ⚪ +8.81% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.49 µs | 1.59 µs | ⚪ -36.22% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.49 µs | 2.53 µs | ⚪ -27.30% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.68 µs | 3.73 µs | ⚪ -20.42% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 70.19 µs | 18.05 µs | ⚪ -74.28% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 12.33 µs | 8.34 µs | ⚪ -32.34% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 3.36 µs | 19.03 µs | ⚪ +466.94% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 4.75 µs | 10.86 µs | ⚪ +128.62% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 11.37 µs | 4.70 µs | ⚪ -58.61% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 32.69 µs | 152.01 µs | ⚪ +365.05% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 36.63 µs | 156.55 µs | ⚪ +327.39% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 18.42 µs | 120.80 µs | ⚪ +555.81% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 131.16 µs | 47.41 µs | ⚪ -63.85% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 50.52 µs | 21.06 µs | ⚪ -58.31% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 40.74 µs | 34.33 µs | ⚪ -15.74% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 65.86 µs | 70.63 µs | ⚪ +7.26% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 67.57 µs | 40.45 µs | ⚪ -40.13% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 1205.19 µs | 3.46 µs | ⚪ -99.71% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 6.22 µs | 5.12 µs | ⚪ -17.65% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 18.12 µs | 4.48 µs | ⚪ -75.26% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency` | 5405.03 µs | 6680.29 µs | 🔴 +23.59% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 3.75 µs | 316.27 µs | ⚪ +8329.28% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 592.51 µs | 6.37 µs | ⚪ -98.92% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5577.37 µs | 5995.30 µs | 🔴 +7.49% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 1.85 µs | 4.62 µs | ⚪ +149.08% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 143.41 µs | 8.79 µs | ⚪ -93.87% |

