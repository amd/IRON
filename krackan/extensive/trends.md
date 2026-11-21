# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.55 µs | 11.18 µs | ⚪ +338.36% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 5.97 µs | 11.15 µs | ⚪ +86.92% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.46 µs | 2.91 µs | ⚪ +17.91% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.40 µs | 2.64 µs | ⚪ +9.88% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 14.11 µs | 10.91 µs | ⚪ -22.66% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.74 µs | 5.76 µs | ⚪ -25.56% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.25 µs | 1.94 µs | ⚪ +55.43% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.03 µs | 8.49 µs | ⚪ +110.43% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 786.67 µs | 5.06 µs | ⚪ -99.36% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 24.62 µs | 11.94 µs | ⚪ -51.49% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 22.66 µs | 16.87 µs | ⚪ -25.54% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.46 µs | 9.80 µs | ⚪ +183.20% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 5.64 µs | 6.14 µs | ⚪ +8.77% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 2.04 µs | 2.30 µs | ⚪ +13.02% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.64 µs | 4.30 µs | ⚪ -23.72% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.05 µs | 3.94 µs | ⚪ +29.03% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 6.86 µs | 5.79 µs | ⚪ -15.62% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 208.01 µs | 3.86 µs | ⚪ -98.14% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 76.06 µs | 53.98 µs | ⚪ -29.03% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 113.17 µs | 99.33 µs | ⚪ -12.23% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 4.00 µs | 3.47 µs | ⚪ -13.16% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.61 µs | 5.19 µs | ⚪ +222.76% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 4.25 µs | 3.10 µs | ⚪ -27.20% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.62 µs | 6.80 µs | ⚪ +87.71% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.90 µs | 1.23 µs | ⚪ -35.56% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.56 µs | 7.16 µs | ⚪ +28.84% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 9.21 µs | 31.17 µs | ⚪ +238.61% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.25 µs | 1.00 µs | ⚪ -55.46% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.66 µs | 3.65 µs | ⚪ +120.03% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.24 µs | 3.13 µs | ⚪ +39.33% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.89 µs | 8.07 µs | ⚪ +179.67% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.30 µs | 1.06 µs | ⚪ -18.57% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 9.26 µs | 6.63 µs | ⚪ -28.41% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.40 µs | 8.72 µs | ⚪ +156.79% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.91 µs | 4.79 µs | ⚪ +64.81% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.95 µs | 2.23 µs | ⚪ +14.13% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.37 µs | 2.77 µs | ⚪ -36.69% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 11.06 µs | 6.31 µs | ⚪ -42.93% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.06 µs | 31.37 µs | ⚪ +2867.41% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.42 µs | 2.96 µs | ⚪ -45.38% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.44 µs | 3.96 µs | ⚪ -38.44% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 13.13 µs | 15.70 µs | ⚪ +19.58% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 3.83 µs | 15.43 µs | ⚪ +303.21% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 7.63 µs | 19.21 µs | ⚪ +151.58% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 12.10 µs | 4.73 µs | ⚪ -60.93% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 54.32 µs | 24.93 µs | ⚪ -54.10% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 61.58 µs | 54.18 µs | ⚪ -12.02% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 111.66 µs | 19.14 µs | ⚪ -82.86% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 38.20 µs | 42.34 µs | ⚪ +10.84% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 251.61 µs | 25.82 µs | ⚪ -89.74% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 76.74 µs | 361.44 µs | ⚪ +371.01% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 70.05 µs | 53.20 µs | ⚪ -24.06% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 79.29 µs | 38.76 µs | ⚪ -51.11% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 3.27 µs | 2.09 µs | ⚪ -36.14% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 10.74 µs | 380.80 µs | ⚪ +3445.49% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency` | 3674.59 µs | 4445.73 µs | 🔴 +20.99% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 157.34 µs | 2.60 µs | ⚪ -98.35% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 507.59 µs | 5.02 µs | ⚪ -99.01% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 373.04 µs | 709.50 µs | ⚪ +90.20% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 6.66 µs | 241.09 µs | ⚪ +3521.37% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 4666.89 µs | 5994.48 µs | 🔴 +28.45% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.59 µs | 4.04 µs | ⚪ +12.55% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 7674.77 µs | 6774.35 µs | 🟢 -11.73% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 16.91 µs | 21.73 µs | ⚪ +28.51% |

