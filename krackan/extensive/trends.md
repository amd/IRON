# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 8.09 µs | 12.19 µs | ⚪ +50.74% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 7.57 µs | 3.66 µs | ⚪ -51.73% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.57 µs | 2.39 µs | ⚪ +52.34% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.44 µs | 0.89 µs | ⚪ -63.44% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.77 µs | 7.24 µs | ⚪ -17.48% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.40 µs | 9.59 µs | ⚪ +14.19% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 4.03 µs | 3.21 µs | ⚪ -20.27% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.32 µs | 5.63 µs | ⚪ +325.57% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 25.01 µs | 12.37 µs | ⚪ -50.54% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 8.64 µs | 1.42 µs | ⚪ -83.53% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 15.43 µs | 16.87 µs | ⚪ +9.31% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 15.62 µs | 5.75 µs | ⚪ -63.22% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.50 µs | 3.52 µs | ⚪ -36.05% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.24 µs | 1.38 µs | ⚪ -73.68% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 8.48 µs | 12.80 µs | ⚪ +50.91% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.70 µs | 3.42 µs | ⚪ +26.70% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 167.94 µs | 125.68 µs | ⚪ -25.16% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 7.05 µs | 2.06 µs | ⚪ -70.78% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +9.05% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 97.78 µs | 89.66 µs | 🟢 -8.30% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.63 µs | 2.26 µs | ⚪ +39.10% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.06 µs | 16.36 µs | ⚪ +694.58% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.24 µs | 3.01 µs | ⚪ +34.16% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.48 µs | 1.56 µs | ⚪ -37.09% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 16.81 µs | 18.31 µs | ⚪ +8.94% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 5.42 µs | 3.84 µs | ⚪ -29.10% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.28 µs | 2.85 µs | ⚪ +24.53% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.93 µs | 4.64 µs | ⚪ -47.98% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.14 µs | 7.17 µs | ⚪ +16.82% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.38 µs | 1.47 µs | ⚪ +6.57% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 11.82 µs | 5.93 µs | ⚪ -49.87% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.21 µs | 2.38 µs | ⚪ -25.62% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.32 µs | 2.65 µs | ⚪ +101.10% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.04 µs | 2.05 µs | ⚪ +98.02% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.49 µs | 3.58 µs | ⚪ +139.93% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.03 µs | 10.21 µs | ⚪ +237.06% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 30.64 µs | 22.22 µs | ⚪ -27.49% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.20 µs | 1.70 µs | ⚪ +41.90% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.56 µs | 6.72 µs | ⚪ -11.13% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.08 µs | 7.90 µs | ⚪ +156.45% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 143.74 µs | 85.38 µs | ⚪ -40.60% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 10.94 µs | 13.77 µs | ⚪ +25.82% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 2.47 µs | 12.53 µs | ⚪ +407.55% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 3.97 µs | 2.08 µs | ⚪ -47.55% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 4.11 µs | 6.66 µs | ⚪ +62.01% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 88.62 µs | 75.34 µs | ⚪ -14.98% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 34.31 µs | 336.69 µs | ⚪ +881.35% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 35.07 µs | 37.29 µs | ⚪ +6.31% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 30.47 µs | 41.77 µs | ⚪ +37.09% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 26.59 µs | 48.81 µs | ⚪ +83.57% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 178.30 µs | 123.38 µs | ⚪ -30.80% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 112.17 µs | 49.06 µs | ⚪ -56.26% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 296.49 µs | 61.18 µs | ⚪ -79.37% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 3.19 µs | 61.57 µs | ⚪ +1829.27% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 6992.36 µs | 5212.98 µs | 🟢 -25.45% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 5.83 µs | 4.84 µs | ⚪ -17.01% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 4446.64 µs | 3525.11 µs | 🟢 -20.72% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.82 µs | 2.43 µs | ⚪ -13.82% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 3.44 µs | 11.77 µs | ⚪ +242.43% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 350.62 µs | 493.17 µs | ⚪ +40.66% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 337.51 µs | 32.93 µs | ⚪ -90.24% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4657.28 µs | 5582.08 µs | 🔴 +19.86% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.77 µs | 2.07 µs | ⚪ -56.61% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 212.60 µs | 477.89 µs | ⚪ +124.78% |

