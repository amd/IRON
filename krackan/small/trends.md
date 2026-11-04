# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 10.78 µs | 1.84 µs | ⚪ -82.95% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 2.20 µs | 6.99 µs | ⚪ +217.74% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.97 µs | 4.78 µs | ⚪ +142.69% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.51 µs | 1.32 µs | ⚪ -47.49% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.49 µs | 4.53 µs | ⚪ -56.83% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.09 µs | 2.74 µs | ⚪ -11.34% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.26 µs | 8.38 µs | ⚪ +15.40% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.37 GB/s | 12.75 GB/s | 🟢 +52.27% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 3004.88 µs | 1973.39 µs | 🟢 -34.33% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 16.40 µs | 4.39 µs | ⚪ -73.24% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5717.32 GOP/s | 8705.76 GOP/s | 🟢 +52.27% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.58 µs | 16.66 µs | ⚪ +365.15% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.57 µs | 14.05 µs | ⚪ +793.04% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 8.12 µs | 15.43 µs | ⚪ +90.11% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.11 µs | 4.81 µs | ⚪ +17.20% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 9.03 µs | 6.28 µs | ⚪ -30.50% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.67 µs | 2.56 µs | ⚪ -66.56% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 6.38 µs | 3.99 µs | ⚪ -37.39% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 30.19 µs | 44.85 µs | ⚪ +48.55% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 41.73 µs | 46.47 µs | ⚪ +11.36% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.87 µs | 3.67 µs | ⚪ +95.68% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.08 µs | 1.25 µs | ⚪ -39.90% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.11 µs | 0.70 µs | ⚪ -66.82% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.02 µs | 6.50 µs | ⚪ +115.60% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.96 µs | 10.18 µs | ⚪ +157.31% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 13.81 µs | 19.09 µs | ⚪ +38.21% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.94 µs | 12.15 µs | ⚪ +313.14% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Bandwidth` | 60.16 GB/s | 56.06 GB/s | 🔴 -6.83% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency` | 139.57 µs | 149.79 µs | 🔴 +7.33% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.31 µs | 2.65 µs | ⚪ -20.00% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Throughput` | 45.08 GOP/s | 42.00 GOP/s | 🔴 -6.83% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.35 µs | 8.13 µs | ⚪ +245.74% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.50 µs | 7.34 µs | ⚪ +109.72% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.85 µs | 3.47 µs | ⚪ +307.75% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 2.85 µs | 2.59 µs | ⚪ -8.95% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.15 µs | 5.08 µs | ⚪ +61.64% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.78 µs | 2.45 µs | ⚪ -68.52% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.25 µs | 3.04 µs | ⚪ +143.77% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.97 µs | 7.97 µs | ⚪ +100.63% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 8.04 µs | 4.19 µs | ⚪ -47.94% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 12.80 µs | 14.84 µs | ⚪ +15.97% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 6.39 µs | 5.07 µs | ⚪ -20.61% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 1.98 µs | 3.81 µs | ⚪ +92.40% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 3.13 µs | 11.69 µs | ⚪ +273.37% |

