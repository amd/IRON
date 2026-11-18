# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 13.09 µs | 1.96 µs | ⚪ -85.04% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 4.93 µs | 1.83 µs | ⚪ -62.90% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.90 µs | 1.48 µs | ⚪ -62.13% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 10.67 µs | 2.13 µs | ⚪ -80.04% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.93 µs | 9.01 µs | ⚪ +82.55% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.82 µs | 11.58 µs | ⚪ +309.79% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 3.88 µs | 2.96 µs | ⚪ -23.78% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.07 µs | 2.95 µs | ⚪ -63.49% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 38.68 µs | 15.83 µs | ⚪ -59.07% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 9.41 µs | 22.87 µs | ⚪ +142.95% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 2.29 µs | 3.02 µs | ⚪ +31.71% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.65 µs | 7.84 µs | ⚪ +374.29% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 3.58 µs | 8.17 µs | ⚪ +128.45% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.73 µs | 6.00 µs | ⚪ +26.80% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.66 µs | 5.96 µs | ⚪ +124.14% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.46 µs | 4.17 µs | ⚪ +69.12% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 6.40 µs | 8.11 µs | ⚪ +26.61% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.90 µs | 23.53 µs | ⚪ +503.91% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 67.58 µs | 43.89 µs | ⚪ -35.05% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 15.44 µs | 2.09 µs | ⚪ -86.47% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.48 µs | 2.66 µs | ⚪ +79.67% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.65 GB/s | 0.69 GB/s | 🟢 +7.63% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 79.33 µs | 73.70 µs | 🟢 -7.09% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.45 µs | 0.91 µs | ⚪ -37.53% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 10.92 µs | 2.88 µs | ⚪ -73.62% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 18.09 µs | 2.99 µs | ⚪ -83.47% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.04 µs | 3.32 µs | ⚪ -52.81% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 17.48 µs | 23.10 µs | ⚪ +32.15% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.17 µs | 0.98 µs | ⚪ -16.25% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.50 µs | 1.54 µs | ⚪ -38.60% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.48 µs | 5.80 µs | ⚪ +133.31% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.44 µs | 2.62 µs | ⚪ -23.63% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.99 µs | 7.46 µs | ⚪ +275.19% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 14.89 µs | 1.69 µs | ⚪ -88.63% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.57 µs | 7.42 µs | ⚪ +33.18% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.53 µs | 4.22 µs | ⚪ +66.75% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.41 µs | 0.67 µs | ⚪ -72.13% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.69 µs | 1.59 µs | ⚪ -41.00% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.12 µs | 12.67 µs | ⚪ -10.25% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 39.55 µs | 32.17 µs | ⚪ -18.66% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.93 µs | 3.11 µs | ⚪ +61.02% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.27 µs | 5.92 µs | ⚪ +80.97% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.79 µs | 3.17 µs | ⚪ -16.29% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 14.69 µs | 11.69 µs | ⚪ -20.42% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 5.32 µs | 1.77 µs | ⚪ -66.76% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 11.20 µs | 16.06 µs | ⚪ +43.45% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 3.24 µs | 5.80 µs | ⚪ +79.14% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 11.92 µs | 7.14 µs | ⚪ -40.13% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 54.84 µs | 15.20 µs | ⚪ -72.28% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 65.90 µs | 20.30 µs | ⚪ -69.20% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 23.17 µs | 108.37 µs | ⚪ +367.63% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 77.02 µs | 34.20 µs | ⚪ -55.59% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 45.39 µs | 29.12 µs | ⚪ -35.85% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 32.82 µs | 40.16 µs | ⚪ +22.38% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 128.55 µs | 388.21 µs | ⚪ +201.99% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 4220.75 µs | 5904.41 µs | 🔴 +39.89% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 14.70 µs | 12.02 µs | ⚪ -18.26% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 6128.35 µs | 5211.33 µs | 🟢 -14.96% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 8.47 µs | 5.40 µs | ⚪ -36.28% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.13 µs | 2.69 µs | ⚪ +26.32% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 12.13 µs | 4.67 µs | ⚪ -61.52% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 4.36 µs | 606.49 µs | ⚪ +13800.85% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 9.25 µs | 7.63 µs | ⚪ -17.50% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5994.17 µs | 4665.80 µs | 🟢 -22.16% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 173.61 µs | 3.30 µs | ⚪ -98.10% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 7660.09 µs | 6759.18 µs | 🟢 -11.76% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 20.23 µs | 13.30 µs | ⚪ -34.24% |

