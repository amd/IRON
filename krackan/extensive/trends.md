# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.11 µs | 8.52 µs | ⚪ +303.67% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.42 µs | 1.95 µs | ⚪ -69.64% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.59 µs | 3.29 µs | ⚪ +106.28% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.23 µs | 17.53 µs | ⚪ +686.19% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 1.14 µs | 6.57 µs | ⚪ +477.57% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.01 µs | 10.23 µs | ⚪ +408.27% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 8.05 µs | 2.39 µs | ⚪ -70.32% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.23 µs | 5.07 µs | ⚪ +57.06% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 8.43 µs | 204.26 µs | ⚪ +2322.71% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 13.79 µs | 9.53 µs | ⚪ -30.88% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.29 µs | 12.32 µs | ⚪ +857.11% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.52 µs | 1.73 µs | ⚪ +13.90% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.16 µs | 10.82 µs | ⚪ +399.68% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.57 µs | 1.69 µs | ⚪ +7.68% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.42 µs | 3.15 µs | ⚪ -28.88% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.87 µs | 2.51 µs | ⚪ -48.50% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 10.40 µs | 11.07 µs | ⚪ +6.40% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 29.73 µs | 39.06 µs | ⚪ +31.39% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.25 µs | 7.99 µs | ⚪ +540.34% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.46 µs | 6.54 µs | ⚪ +347.20% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.55 µs | 1.73 µs | ⚪ +11.63% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.65 µs | 8.81 µs | ⚪ +15.12% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.33 µs | 2.85 µs | ⚪ -61.14% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 35.58 µs | 18.71 µs | ⚪ -47.41% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 11.46 µs | 1.13 µs | ⚪ -90.12% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.38 µs | 2.51 µs | ⚪ +5.48% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.35 µs | 6.28 µs | ⚪ +87.30% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.74 µs | 7.87 µs | ⚪ +110.49% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 2.29 µs | 1.19 µs | ⚪ -47.90% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 18.49 µs | 6.56 µs | ⚪ -64.54% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.24 µs | 3.28 µs | ⚪ -60.18% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 18.46 µs | 2.19 µs | ⚪ -88.14% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.90 µs | 0.83 µs | ⚪ -71.27% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.39 µs | 5.37 µs | ⚪ +22.14% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.67 µs | 25.97 µs | ⚪ +607.37% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.66 µs | 2.62 µs | ⚪ +57.55% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.05 µs | 4.22 µs | ⚪ -58.03% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.73 µs | 3.82 µs | ⚪ +40.05% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 17.83 µs | 16.78 µs | ⚪ -5.92% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 7.36 µs | 11.87 µs | ⚪ +61.27% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 10.93 µs | 18.00 µs | ⚪ +64.79% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 9.14 µs | 6.56 µs | ⚪ -28.18% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 7.00 µs | 10.71 µs | ⚪ +52.96% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 72.69 µs | 221.20 µs | ⚪ +204.29% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 59.50 µs | 79.33 µs | ⚪ +33.31% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 40.68 µs | 154.97 µs | ⚪ +280.99% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 259.38 µs | 125.74 µs | ⚪ -51.52% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 149.23 µs | 61.21 µs | ⚪ -58.99% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 66.28 µs | 147.28 µs | ⚪ +122.23% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 55.48 µs | 101.22 µs | ⚪ +82.45% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 109.14 µs | 235.66 µs | ⚪ +115.92% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 9.55 µs | 2.58 µs | ⚪ -72.98% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 8.06 µs | 4.44 µs | ⚪ -44.84% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 4449.67 µs | 3534.52 µs | 🟢 -20.57% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 8.24 µs | 2.92 µs | ⚪ -64.62% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 4.36 µs | 5.71 µs | ⚪ +30.88% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 355.68 µs | 4.37 µs | ⚪ -98.77% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 8.42 µs | 153.95 µs | ⚪ +1729.22% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.10 µs | 3.40 µs | ⚪ -17.14% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 7.85 µs | 11.40 µs | ⚪ +45.18% |

