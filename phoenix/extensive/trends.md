# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 15.24 GB/s | 32.04 GB/s | 🟢 +110.22% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3302.09 µs | 1570.79 µs | 🟢 -52.43% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 594.22 µs | 27.50 µs | ⚪ -95.37% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.08 GOP/s | 10.68 GOP/s | 🟢 +110.22% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 9.09 µs | 1171.96 µs | ⚪ +12790.01% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 93.17 µs | 538.14 µs | ⚪ +477.57% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 6.21 µs | 30.63 µs | ⚪ +393.09% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 478.90 µs | 398.63 µs | ⚪ -16.76% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 564.40 µs | 329.21 µs | ⚪ -41.67% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 8.15 µs | 6.95 µs | ⚪ -14.79% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.54 GB/s | 16.80 GB/s | 🟢 +59.46% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3184.90 µs | 1997.29 µs | 🟢 -37.29% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 280.91 µs | 235.21 µs | ⚪ -16.27% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.63 GOP/s | 4.20 GOP/s | 🟢 +59.46% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 711.76 µs | 464.71 µs | ⚪ -34.71% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 385.73 µs | 125.98 µs | ⚪ -67.34% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 156.62 µs | 370.74 µs | ⚪ +136.71% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 13.92 µs | 26.76 µs | ⚪ +92.27% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 227.91 µs | 376.26 µs | ⚪ +65.09% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 22.16 µs | 902.01 µs | ⚪ +3969.99% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 280.71 µs | 396.98 µs | ⚪ +41.42% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 253.65 µs | 378.64 µs | ⚪ +49.28% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 385.59 µs | 421.28 µs | ⚪ +9.26% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 124.19 µs | 170.20 µs | ⚪ +37.05% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 165.39 µs | 139.13 µs | ⚪ -15.87% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 122.60 µs | 200.87 µs | ⚪ +63.84% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.47 µs | 3.74 µs | ⚪ -42.26% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.07 GB/s | 13.70 GB/s | 🔴 -51.18% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 18.31 µs | 1019.34 µs | ⚪ +5467.42% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.06 GOP/s | 13.70 GOP/s | 🔴 -51.18% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 535.72 µs | 402.84 µs | ⚪ -24.80% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 931.89 µs | 18.64 µs | ⚪ -98.00% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 192.00 µs | 244.16 µs | ⚪ +27.17% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 47.28 µs | 65.60 µs | ⚪ +38.74% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 13.03 µs | 55.92 µs | ⚪ +329.20% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 540.15 µs | 975.11 µs | ⚪ +80.53% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 927.35 µs | 23.27 µs | ⚪ -97.49% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 9.21 µs | 210.99 µs | ⚪ +2190.28% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 256.55 µs | 103.38 µs | ⚪ -59.70% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 687.75 µs | 399.56 µs | ⚪ -41.90% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.50 GB/s | 29.71 GB/s | 🟢 +158.35% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2917.65 µs | 1129.34 µs | 🟢 -61.29% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 850.33 µs | 24.68 µs | ⚪ -97.10% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.88 GOP/s | 7.43 GOP/s | 🟢 +158.35% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 453.49 µs | 313.89 µs | ⚪ -30.78% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 11.50 µs | 39.36 µs | ⚪ +242.40% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 1.34 GB/s | 🟢 +171.45% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4254.09 µs | 1567.14 µs | 🟢 -63.16% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 557.86 µs | 1149.03 µs | ⚪ +105.97% |

