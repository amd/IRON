# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 14.34 µs | 2.97 µs | ⚪ -79.32% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 10.53 µs | 4.46 µs | ⚪ -57.67% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.00 µs | 1.25 µs | ⚪ -37.35% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.91 µs | 2.12 µs | ⚪ +10.68% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.55 µs | 2.31 µs | ⚪ -72.92% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.84 µs | 8.01 µs | ⚪ -9.46% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 3.32 µs | 4.91 µs | ⚪ +47.95% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.63 µs | 3.38 µs | ⚪ -27.05% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 10.65 GB/s | 9.73 GB/s | 🔴 -8.69% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3248.39 µs | 3557.72 µs | 🔴 +9.52% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 7.75 µs | 37.03 µs | ⚪ +377.54% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5949.82 GOP/s | 5432.51 GOP/s | 🔴 -8.69% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.69 GB/s | 12.81 GB/s | 🟢 +47.41% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2895.79 µs | 1964.40 µs | 🟢 -32.16% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 13.85 µs | 4.75 µs | ⚪ -65.66% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5932.70 GOP/s | 8745.60 GOP/s | 🟢 +47.41% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.40 µs | 7.87 µs | ⚪ +463.03% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.98 µs | 1.80 µs | ⚪ -54.66% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 5.39 µs | 2.20 µs | ⚪ -59.23% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.65 µs | 3.79 µs | ⚪ +129.46% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.56 µs | 6.19 µs | ⚪ +11.35% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.61 µs | 3.06 µs | ⚪ -33.77% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.73 µs | 4.69 µs | ⚪ -18.09% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.95 µs | 3.39 µs | ⚪ -62.15% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 45.41 µs | 81.76 µs | ⚪ +80.04% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 145.09 µs | 128.23 µs | ⚪ -11.62% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.26 µs | 8.50 µs | ⚪ +276.07% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.96 µs | 1.34 µs | ⚪ -54.72% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.25 µs | 1.69 µs | ⚪ -81.71% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.85 µs | 3.81 µs | ⚪ -44.33% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.66 µs | 3.60 µs | ⚪ +116.88% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.56 µs | 8.26 µs | ⚪ +223.31% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 36.36 µs | 12.60 µs | ⚪ -65.33% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 11.12 µs | 1.03 µs | ⚪ -90.76% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.80 µs | 4.82 µs | ⚪ -45.21% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 2.25 µs | 5.84 µs | ⚪ +158.94% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.10 µs | 3.34 µs | ⚪ +59.17% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.82 µs | 2.80 µs | ⚪ +240.29% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.90 µs | 3.84 µs | ⚪ -34.91% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 16.99 µs | 3.14 µs | ⚪ -81.52% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 22.65 µs | 30.62 µs | ⚪ +35.18% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.59 µs | 2.02 µs | ⚪ +27.46% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.53 µs | 2.67 µs | ⚪ +5.31% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.73 µs | 5.49 µs | ⚪ +47.30% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 18.05 µs | 13.31 µs | ⚪ -26.27% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 8.34 µs | 1.29 µs | ⚪ -84.56% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 19.03 µs | 8.29 µs | ⚪ -56.42% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 10.86 µs | 4.32 µs | ⚪ -60.17% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 4.70 µs | 8.02 µs | ⚪ +70.48% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 152.01 µs | 67.06 µs | ⚪ -55.88% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 156.55 µs | 42.37 µs | ⚪ -72.94% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 120.80 µs | 60.16 µs | ⚪ -50.19% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 47.41 µs | 112.59 µs | ⚪ +137.49% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 21.06 µs | 41.17 µs | ⚪ +95.48% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 34.33 µs | 41.64 µs | ⚪ +21.32% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 70.63 µs | 44.97 µs | ⚪ -36.34% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 40.45 µs | 48.33 µs | ⚪ +19.48% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 4220.32 µs | 5114.22 µs | 🔴 +21.18% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 3.46 µs | 2.35 µs | ⚪ -32.02% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 5220.53 µs | 6131.23 µs | 🔴 +17.44% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 5.12 µs | 10.05 µs | ⚪ +96.37% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 3524.48 µs | 4442.95 µs | 🔴 +26.06% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 9.88 µs | 2.51 µs | ⚪ -74.56% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 4.48 µs | 129.14 µs | ⚪ +2780.36% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency` | 6680.29 µs | 5408.66 µs | 🟢 -19.04% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 316.27 µs | 4.26 µs | ⚪ -98.65% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 6.37 µs | 183.19 µs | ⚪ +2774.90% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5995.30 µs | 4665.01 µs | 🟢 -22.19% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.62 µs | 4.30 µs | ⚪ -6.94% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 8.79 µs | 6.71 µs | ⚪ -23.67% |

