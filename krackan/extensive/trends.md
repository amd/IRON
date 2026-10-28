# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.23 | 3.78 | 🔴 +17.07% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 2.48 | 1.58 | 🟢 -36.35% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.93 | 3.72 | 🟢 -5.36% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 0.76 | 3.88 | 🔴 +412.29% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.20 | 3.51 | 🟢 -16.60% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.21 | 2.55 | 🟢 -20.74% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.17 | 0.12 | 🔴 -26.24% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 11.77 | 15.96 | 🔴 +35.57% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.28 | 1.43 | 🟢 -37.14% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.44 | 1.24 | 🟢 -77.27% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.83 | 12.83 | 🟢 +45.23% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2849.36 | 1961.97 | 🟢 -31.14% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 10.02 | 72.35 | 🔴 +621.80% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 6029.38 | 8756.45 | 🟢 +45.23% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 17.79 | 2.57 | 🟢 -85.58% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 10.96 | 1.02 | 🟢 -90.68% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 7.35 | 1.98 | 🟢 -73.06% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.26 | 1.17 | 🟢 -72.60% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1.97 | 3.46 | 🔴 +75.60% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.59 | 2.20 | 🔴 +38.39% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 3.39 | 1.84 | 🟢 -45.71% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 24.47 | 26.05 | 🔴 +6.47% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 46.18 | 22.62 | 🟢 -51.03% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 42.88 | 14.75 | 🟢 -65.61% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.07 | 1.36 | 🔴 +27.10% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.13 | 1.21 | 🔴 +7.11% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.61 | 0.69 | 🟢 -73.56% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.58 | 2.88 | 🟢 -19.70% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.00 | 3.13 | 🔴 +56.40% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.27 | 3.64 | 🔴 +11.16% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 22.18 | 68.85 | 🔴 +210.46% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.33 | 1.68 | 🟢 -27.97% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 9.73 | 6.85 | 🟢 -29.59% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.99 | 4.90 | 🔴 +22.82% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.13 | 8.41 | 🔴 +168.48% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.78 | 1.41 | 🔴 +81.91% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.90 | 2.35 | 🟢 -60.07% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.97 | 5.11 | 🔴 +72.00% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.98 | 1.85 | 🔴 +88.75% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.58 | 3.36 | 🔴 +112.92% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 4.51 | 2.34 | 🟢 -48.06% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Bandwidth` | 127.67 | 66.82 | 🔴 -47.66% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency` | 1975.32 | 3774.26 | 🔴 +91.07% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 88.82 | 25.36 | 🟢 -71.44% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Throughput` | 407.68 | 213.37 | 🔴 -47.66% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.56 | 13.81 | 🔴 +30.74% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Bandwidth` | 41.83 | 44.61 | 🟢 +6.63% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency` | 597.64 | 560.50 | 🟢 -6.21% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Throughput` | 129.40 | 137.97 | 🟢 +6.63% |

