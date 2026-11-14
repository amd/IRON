# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 8.52 µs | 9.47 µs | ⚪ +11.25% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1.95 µs | 11.35 µs | ⚪ +482.35% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.29 µs | 3.89 µs | ⚪ +18.28% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 17.53 µs | 4.86 µs | ⚪ -72.25% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.57 µs | 8.44 µs | ⚪ +28.47% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.23 µs | 5.89 µs | ⚪ -42.43% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.39 µs | 5.14 µs | ⚪ +115.11% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.07 µs | 0.81 µs | ⚪ -84.10% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 204.26 µs | 6.45 µs | ⚪ -96.84% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 9.53 µs | 42.16 µs | ⚪ +342.32% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 12.32 µs | 14.27 µs | ⚪ +15.86% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.73 µs | 15.78 µs | ⚪ +812.64% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 10.82 µs | 2.38 µs | ⚪ -77.95% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.69 µs | 8.24 µs | ⚪ +388.07% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.15 µs | 7.14 µs | ⚪ +127.03% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.51 µs | 4.72 µs | ⚪ +88.17% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 11.07 µs | 11.78 µs | ⚪ +6.43% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 30.76 µs | 41.69 µs | ⚪ +35.55% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 39.06 µs | 61.14 µs | ⚪ +56.51% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 7.99 µs | 1.96 µs | ⚪ -75.40% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.54 µs | 2.61 µs | ⚪ -60.03% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.65 GB/s | 0.77 GB/s | 🟢 +19.49% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 79.08 µs | 66.18 µs | 🟢 -16.31% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.73 µs | 3.03 µs | ⚪ +75.12% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.81 µs | 4.81 µs | ⚪ -45.43% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.85 µs | 7.45 µs | ⚪ +161.50% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.84 µs | 5.49 µs | ⚪ +197.83% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 18.71 µs | 8.93 µs | ⚪ -52.29% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.13 µs | 2.02 µs | ⚪ +78.84% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.28 µs | 11.47 µs | ⚪ +82.74% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.87 µs | 6.95 µs | ⚪ -11.65% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.19 µs | 9.33 µs | ⚪ +682.22% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 6.56 µs | 1.88 µs | ⚪ -71.35% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.28 µs | 7.38 µs | ⚪ +125.05% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.19 µs | 4.16 µs | ⚪ +89.88% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.83 µs | 1.70 µs | ⚪ +104.69% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.37 µs | 3.28 µs | ⚪ -38.84% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 25.97 µs | 3.05 µs | ⚪ -88.28% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 24.17 µs | 16.07 µs | ⚪ -33.51% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.62 µs | 1.20 µs | ⚪ -54.27% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.22 µs | 2.47 µs | ⚪ -41.33% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.82 µs | 4.47 µs | ⚪ +17.07% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 16.78 µs | 6.94 µs | ⚪ -58.61% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 11.87 µs | 13.58 µs | ⚪ +14.39% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 18.00 µs | 2.64 µs | ⚪ -85.34% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 6.56 µs | 7.45 µs | ⚪ +13.58% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 10.71 µs | 3.75 µs | ⚪ -64.95% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 79.33 µs | 153.29 µs | ⚪ +93.24% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 154.97 µs | 80.40 µs | ⚪ -48.12% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 125.74 µs | 36.70 µs | ⚪ -70.81% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 61.21 µs | 24.51 µs | ⚪ -59.96% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 147.28 µs | 176.70 µs | ⚪ +19.97% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 101.22 µs | 85.70 µs | ⚪ -15.33% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 235.66 µs | 52.29 µs | ⚪ -77.81% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 2.58 µs | 399.63 µs | ⚪ +15389.59% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 5214.88 µs | 5989.84 µs | 🔴 +14.86% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 4.44 µs | 172.31 µs | ⚪ +3777.87% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.92 µs | 763.51 µs | ⚪ +26087.93% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 5.71 µs | 3.83 µs | ⚪ -32.98% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 4.37 µs | 27.67 µs | ⚪ +533.35% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 153.95 µs | 544.73 µs | ⚪ +253.84% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4665.51 µs | 5994.68 µs | 🔴 +28.49% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.40 µs | 4.30 µs | ⚪ +26.58% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 11.40 µs | 6.43 µs | ⚪ -43.56% |

