# Performance trends

**Operators added:** `SelectiveScan`, `generation`, `pre_push_hook`

**Operators dropped:** `visualize`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 4.45 | 5.90 | 🔴 +32.67% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 5.92 | 2.30 | 🟢 -61.05% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 5.68 | 4.38 | 🟢 -22.88% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 18.53 | 1.04 | 🟢 -94.38% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 1.95 | 8.34 | 🔴 +326.61% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.00 | 2.44 | 🔴 +22.32% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.11 | 0.12 | 🟢 +5.52% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 18.20 | 17.25 | 🟢 -5.23% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.26 | 5.02 | 🔴 +122.13% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 13.61 | 6.89 | 🟢 -49.38% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 6.98 | 8.10 | 🔴 +16.09% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 13.71 | 2.80 | 🟢 -79.61% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 4.18 | 10.41 | 🔴 +149.27% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 3.53 | 4.21 | 🔴 +19.32% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.03 | 7.20 | 🔴 +78.77% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 12.88 | 9.65 | 🟢 -25.08% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.81 | 5.81 | 🔴 +106.60% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 8.07 | 7.37 | 🟢 -8.74% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.74 | 185.60 | 🔴 +3815.99% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 144.15 | 37.38 | 🟢 -74.07% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.97 | 5.99 | 🔴 +101.53% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.01 | 1.59 | 🟢 -73.50% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.11 | 6.85 | 🔴 +12.21% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.97 | 1.97 | 🟢 -33.57% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.13 | 8.44 | 🔴 +295.34% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 21.81 | 31.85 | 🔴 +46.03% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.87 | 0.39 | 🟢 -55.73% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.94 | 2.93 | 🔴 +50.80% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.70 | 4.98 | 🟢 -12.48% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.30 | 7.31 | 🟢 -11.93% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.77 | 5.48 | 🔴 +610.18% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.17 | 3.24 | 🟢 -47.44% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 3.06 | 1.30 | 🟢 -57.43% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.29 | 4.45 | 🔴 +94.09% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 4.77 | 5.43 | 🔴 +13.74% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Bandwidth` | 4.72 | 4.47 | 🔴 -5.27% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency` | 1111.74 | 1173.64 | 🔴 +5.57% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Throughput` | 1931.64 | 1829.77 | 🔴 -5.27% |

