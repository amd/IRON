# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 6.54 µs | 13.09 µs | ⚪ +100.26% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 10.45 µs | 4.93 µs | ⚪ -52.85% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.78 µs | 3.90 µs | ⚪ +119.46% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.73 µs | 10.67 µs | ⚪ +517.22% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.62 µs | 4.93 µs | ⚪ +88.70% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 13.13 µs | 2.82 µs | ⚪ -78.49% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 4.41 µs | 3.88 µs | ⚪ -12.13% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.57 µs | 8.07 µs | ⚪ +413.20% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 21.40 µs | 38.68 µs | ⚪ +80.73% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 15.44 µs | 9.41 µs | ⚪ -39.04% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 11.39 µs | 2.29 µs | ⚪ -79.89% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.45 µs | 1.65 µs | ⚪ +14.20% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 3.40 µs | 3.58 µs | ⚪ +5.28% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 5.10 µs | 4.73 µs | ⚪ -7.18% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.05 µs | 2.66 µs | ⚪ -62.27% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.94 µs | 2.46 µs | ⚪ -68.96% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 14.79 µs | 6.40 µs | ⚪ -56.72% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 20.47 µs | 3.90 µs | ⚪ -80.97% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 43.23 µs | 67.58 µs | ⚪ +56.32% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 79.08 µs | 146.11 µs | ⚪ +84.78% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.45 µs | 15.44 µs | ⚪ +530.35% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 GB/s | 0.17 GB/s | 🔴 -7.57% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 89.82 µs | 97.18 µs | 🔴 +8.19% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.70 µs | 1.48 µs | ⚪ -44.97% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.19 µs | 1.45 µs | ⚪ -33.68% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.34 µs | 10.92 µs | ⚪ +151.72% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.30 µs | 18.09 µs | ⚪ +447.82% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.71 µs | 7.04 µs | ⚪ +160.14% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 22.57 µs | 17.48 µs | ⚪ -22.55% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.51 µs | 1.17 µs | ⚪ -22.26% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.13 µs | 2.48 µs | ⚪ -59.48% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 64.61 GB/s | 67.85 GB/s | 🟢 +5.01% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.05 µs | 3.44 µs | ⚪ -71.47% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.15 GOP/s | 16.96 GOP/s | 🟢 +5.01% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.75 µs | 1.99 µs | ⚪ +13.78% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 2.90 µs | 14.89 µs | ⚪ +412.51% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.81 µs | 5.57 µs | ⚪ +15.73% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.05 µs | 2.53 µs | ⚪ -16.96% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.00 µs | 2.41 µs | ⚪ +140.47% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.33 µs | 2.69 µs | ⚪ +15.47% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 10.90 µs | 14.12 µs | ⚪ +29.50% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 32.16 µs | 39.55 µs | ⚪ +22.96% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 12.60 µs | 1.93 µs | ⚪ -84.69% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.04 µs | 3.27 µs | ⚪ +60.04% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.87 µs | 3.79 µs | ⚪ +32.22% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 18.91 µs | 14.69 µs | ⚪ -22.29% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 2.01 µs | 5.32 µs | ⚪ +164.28% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 1.68 µs | 11.20 µs | ⚪ +567.22% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 5.19 µs | 3.24 µs | ⚪ -37.65% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 8.75 µs | 11.92 µs | ⚪ +36.23% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 71.42 µs | 54.84 µs | ⚪ -23.21% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 129.03 µs | 31.35 µs | ⚪ -75.70% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 196.64 µs | 65.90 µs | ⚪ -66.49% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 13.47 µs | 23.17 µs | ⚪ +72.10% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 32.89 µs | 77.02 µs | ⚪ +134.16% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 131.12 µs | 45.39 µs | ⚪ -65.39% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 464.06 µs | 32.82 µs | ⚪ -92.93% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 241.33 µs | 128.55 µs | ⚪ -46.73% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 2.00 µs | 14.70 µs | ⚪ +633.87% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 9.72 µs | 8.47 µs | ⚪ -12.80% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 4741.26 µs | 3525.16 µs | 🟢 -25.65% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 260.50 µs | 2.13 µs | ⚪ -99.18% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency` | 4686.09 µs | 5603.31 µs | 🔴 +19.57% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 2.19 µs | 12.13 µs | ⚪ +453.01% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency` | 5420.53 µs | 6321.39 µs | 🔴 +16.62% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 7.76 µs | 4.36 µs | ⚪ -43.74% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 45.91 µs | 9.25 µs | ⚪ -79.86% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4659.91 µs | 5994.17 µs | 🔴 +28.63% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.39 µs | 173.61 µs | ⚪ +3856.02% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 6913.12 µs | 7660.09 µs | 🔴 +10.81% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 162.79 µs | 20.23 µs | ⚪ -87.57% |

