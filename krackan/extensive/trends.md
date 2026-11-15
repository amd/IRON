# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 9.47 µs | 3.27 µs | ⚪ -65.52% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 11.35 µs | 20.03 µs | ⚪ +76.51% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.89 µs | 1.94 µs | ⚪ -50.13% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 4.86 µs | 2.68 µs | ⚪ -45.00% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.89 µs | 11.21 µs | ⚪ +90.21% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.14 µs | 8.83 µs | ⚪ +71.82% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 0.81 µs | 4.57 µs | ⚪ +466.73% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 10.68 GB/s | 11.68 GB/s | 🟢 +9.45% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3241.29 µs | 2961.47 µs | 🟢 -8.63% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 6.45 µs | 11.44 µs | ⚪ +77.25% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5962.86 GOP/s | 6526.26 GOP/s | 🟢 +9.45% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.89 GB/s | 12.81 GB/s | 🟢 +44.08% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2831.41 µs | 1965.21 µs | 🟢 -30.59% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 42.16 µs | 4.13 µs | ⚪ -90.20% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 6067.60 GOP/s | 8742.01 GOP/s | 🟢 +44.08% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 14.27 µs | 2.66 µs | ⚪ -81.33% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 15.78 µs | 2.38 µs | ⚪ -84.88% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.38 µs | 1.97 µs | ⚪ -17.24% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 8.24 µs | 5.72 µs | ⚪ -30.58% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.14 µs | 3.91 µs | ⚪ -45.30% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.72 µs | 3.51 µs | ⚪ -25.67% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 11.78 µs | 7.64 µs | ⚪ -35.09% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 41.69 µs | 4.38 µs | ⚪ -89.49% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 61.14 µs | 52.26 µs | ⚪ -14.51% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 100.25 µs | 116.90 µs | ⚪ +16.61% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.96 µs | 10.78 µs | ⚪ +448.65% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 GB/s | 0.17 GB/s | 🔴 -8.09% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 88.93 µs | 96.76 µs | 🔴 +8.80% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.61 µs | 1.93 µs | ⚪ -26.25% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 3.03 µs | 12.71 µs | ⚪ +320.18% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.81 µs | 5.85 µs | ⚪ +21.66% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.45 µs | 4.90 µs | ⚪ -34.27% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.49 µs | 11.15 µs | ⚪ +103.10% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 8.93 µs | 14.04 µs | ⚪ +57.24% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.02 µs | 26.01 µs | ⚪ +1184.54% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.60 µs | 1.69 µs | ⚪ -35.17% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 11.47 µs | 6.31 µs | ⚪ -44.98% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.95 µs | 6.32 µs | ⚪ -9.02% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 9.33 µs | 2.36 µs | ⚪ -74.75% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.88 µs | 14.64 µs | ⚪ +679.21% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.38 µs | 6.26 µs | ⚪ -15.26% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.16 µs | 3.53 µs | ⚪ -15.17% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.28 µs | 2.19 µs | ⚪ -33.13% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.05 µs | 16.14 µs | ⚪ +429.83% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 16.07 µs | 28.41 µs | ⚪ +76.80% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.20 µs | 1.99 µs | ⚪ +66.44% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.47 µs | 7.63 µs | ⚪ +208.51% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.47 µs | 3.76 µs | ⚪ -15.81% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.94 µs | 180.93 µs | ⚪ +2505.81% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.58 µs | 3.31 µs | ⚪ -75.61% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 2.64 µs | 15.13 µs | ⚪ +473.26% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 3.75 µs | 5.04 µs | ⚪ +34.45% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 220.71 µs | 58.76 µs | ⚪ -73.38% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 153.29 µs | 52.12 µs | ⚪ -66.00% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 80.40 µs | 184.01 µs | ⚪ +128.88% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 36.70 µs | 23.77 µs | ⚪ -35.24% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 24.51 µs | 188.88 µs | ⚪ +670.72% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 176.70 µs | 58.44 µs | ⚪ -66.93% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 85.70 µs | 74.22 µs | ⚪ -13.40% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 52.29 µs | 145.22 µs | ⚪ +177.69% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 399.63 µs | 5.41 µs | ⚪ -98.65% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 172.31 µs | 8.22 µs | ⚪ -95.23% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 763.51 µs | 3.05 µs | ⚪ -99.60% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 3.83 µs | 5.35 µs | ⚪ +39.66% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 27.67 µs | 3.66 µs | ⚪ -86.78% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 544.73 µs | 369.40 µs | ⚪ -32.19% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5994.68 µs | 4668.93 µs | 🟢 -22.12% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.30 µs | 3.02 µs | ⚪ -29.72% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 6.43 µs | 6.02 µs | ⚪ -6.38% |

