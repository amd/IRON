# Performance trends

**Operators added:** `lm_server`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 10.53 µs | 11.45 µs | ⚪ +8.76% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 11.09 µs | 5.39 µs | ⚪ -51.34% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.35 µs | 5.24 µs | ⚪ +56.36% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 4.05 µs | 2.58 µs | ⚪ -36.22% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.52 µs | 10.81 µs | ⚪ -6.21% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.31 µs | 2.45 µs | ⚪ +5.83% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.22 µs | 2.72 µs | ⚪ +22.32% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.12 µs | 4.89 µs | ⚪ +130.36% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 6.90 GB/s | 12.87 GB/s | 🟢 +86.63% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 3649.38 µs | 1955.43 µs | 🟢 -46.42% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 35.91 µs | 6.75 µs | ⚪ -81.19% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 4707.61 GOP/s | 8785.74 GOP/s | 🟢 +86.63% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 14.25 µs | 2.64 µs | ⚪ -81.47% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 17.00 µs | 3.52 µs | ⚪ -79.31% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 8.73 µs | 2.28 µs | ⚪ -73.93% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 8.36 µs | 3.92 µs | ⚪ -53.12% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.40 µs | 5.74 µs | ⚪ +68.76% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.46 µs | 2.01 µs | ⚪ -54.82% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 10.80 µs | 5.16 µs | ⚪ -52.20% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 25.69 µs | 4.78 µs | ⚪ -81.38% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 44.89 µs | 28.98 µs | ⚪ -35.44% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.11 µs | 1.48 µs | ⚪ +33.45% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.86 µs | 1.75 µs | ⚪ -5.65% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.72 GB/s | 0.64 GB/s | 🔴 -10.17% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 71.45 µs | 79.54 µs | 🔴 +11.32% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.62 µs | 1.37 µs | ⚪ -47.70% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.61 µs | 6.11 µs | ⚪ +32.35% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.44 µs | 2.41 µs | ⚪ -62.58% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 30.30 µs | 58.90 µs | ⚪ +94.38% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 11.80 µs | 1.78 µs | ⚪ -84.93% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.74 µs | 1.45 µs | ⚪ -16.61% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.77 µs | 8.15 µs | ⚪ +70.82% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.57 µs | 8.37 µs | ⚪ -38.32% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.50 µs | 2.16 µs | ⚪ +44.49% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 7.12 µs | 4.98 µs | ⚪ -30.03% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.37 µs | 3.87 µs | ⚪ +14.73% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.99 µs | 1.75 µs | ⚪ +76.17% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.34 µs | 1.82 µs | ⚪ -78.20% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.53 µs | 6.92 µs | ⚪ -52.38% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 2.24 µs | 9.87 µs | ⚪ +339.77% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 8.41 µs | 13.88 µs | ⚪ +65.08% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 17.58 µs | 5.08 µs | ⚪ -71.11% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 5.23 µs | 11.71 µs | ⚪ +123.72% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 23.51 µs | 57.63 µs | ⚪ +145.10% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 29.98 µs | 43.64 µs | ⚪ +45.58% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 35.68 µs | 121.87 µs | ⚪ +241.54% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 26.15 µs | 145.02 µs | ⚪ +454.46% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 75.30 µs | 69.97 µs | ⚪ -7.08% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 84.08 µs | 69.63 µs | ⚪ -17.19% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 28.20 µs | 40.51 µs | ⚪ +43.62% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 26.66 µs | 190.34 µs | ⚪ +614.07% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 4199.28 µs | 4995.45 µs | 🔴 +18.96% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 2.56 µs | 0.64 µs | ⚪ -74.94% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 6983.49 µs | 6130.15 µs | 🟢 -12.22% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 13.91 µs | 11.83 µs | ⚪ -14.95% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 3534.93 µs | 4995.22 µs | 🔴 +41.31% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.32 µs | 1.50 µs | ⚪ -35.45% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 6.24 µs | 4.83 µs | ⚪ -22.57% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 727.96 µs | 5.00 µs | ⚪ -99.31% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 6.17 µs | 208.03 µs | ⚪ +3273.29% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5578.45 µs | 5993.39 µs | 🔴 +7.44% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.88 µs | 4.56 µs | ⚪ -6.38% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 11.03 µs | 6.68 µs | ⚪ -39.44% |

