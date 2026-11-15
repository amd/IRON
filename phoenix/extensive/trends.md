# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 339.47 µs | 309.05 µs | ⚪ -8.96% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 822.46 µs | 326.02 µs | ⚪ -60.36% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.80 GB/s | 5.19 GB/s | 🔴 -67.13% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1061.69 µs | 3230.21 µs | 🔴 +204.25% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 16.36 µs | 254.53 µs | ⚪ +1456.28% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.73 µs | 14.32 µs | ⚪ +33.42% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.24 GB/s | 15.17 GB/s | 🔴 -52.94% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1561.03 µs | 3316.94 µs | 🔴 +112.48% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 26.63 µs | 439.21 µs | ⚪ +1549.57% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.37 GOP/s | 2.53 GOP/s | 🔴 -52.94% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.20 GB/s | 27.90 GB/s | 🟢 +83.48% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3310.45 µs | 1804.23 µs | 🟢 -45.50% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 297.57 µs | 259.81 µs | ⚪ -12.69% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.53 GOP/s | 4.65 GOP/s | 🟢 +83.48% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.40 µs | 12.76 µs | ⚪ +189.89% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 31.85 µs | 724.46 µs | ⚪ +2174.59% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 139.21 µs | 825.11 µs | ⚪ +492.70% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 107.99 µs | 319.22 µs | ⚪ +195.59% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 350.33 µs | 300.49 µs | ⚪ -14.23% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 660.81 µs | 419.93 µs | ⚪ -36.45% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 367.88 µs | 560.41 µs | ⚪ +52.33% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.21 GB/s | 10.14 GB/s | 🔴 -64.05% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1189.82 µs | 3309.40 µs | 🔴 +178.14% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.80 µs | 326.08 µs | ⚪ +4693.51% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.30 GOP/s | 15.21 GOP/s | 🔴 -64.05% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.76 GB/s | 29.59 GB/s | 🟢 +203.33% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3439.71 µs | 1133.98 µs | 🟢 -67.03% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 181.31 µs | 13.71 µs | ⚪ -92.44% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 14.63 GOP/s | 44.39 GOP/s | 🟢 +203.33% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 179.33 µs | 425.01 µs | ⚪ +136.99% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 255.39 µs | 178.88 µs | ⚪ -29.96% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 55.58 µs | 73.74 µs | ⚪ +32.67% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 472.72 µs | 5.92 µs | ⚪ -98.75% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 8.58 µs | 10.37 µs | ⚪ +20.97% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 27.69 µs | 9.49 µs | ⚪ -65.73% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 9.63 GB/s | 27.97 GB/s | 🟢 +190.41% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3485.05 µs | 1200.05 µs | 🟢 -65.57% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 549.10 µs | 73.49 µs | ⚪ -86.62% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 9.63 GOP/s | 27.96 GOP/s | 🟢 +190.41% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.77 GB/s | 11.52 GB/s | 🔴 -61.30% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1126.94 µs | 2911.77 µs | 🔴 +158.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.45 µs | 595.36 µs | ⚪ +6201.10% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.77 GOP/s | 11.52 GOP/s | 🔴 -61.30% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.45 µs | 4.41 µs | ⚪ -19.03% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 106.24 µs | 176.55 µs | ⚪ +66.19% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 23.28 µs | 16.13 µs | ⚪ -30.70% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1603.14 µs | 3080.47 µs | 🔴 +92.15% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 496.57 µs | 609.85 µs | ⚪ +22.81% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.60 GB/s | 10.60 GB/s | 🔴 -62.92% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1173.71 µs | 3165.19 µs | 🔴 +169.67% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 27.42 µs | 331.18 µs | ⚪ +1107.97% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.15 GOP/s | 2.65 GOP/s | 🔴 -62.92% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 11.79 µs | 15.67 µs | ⚪ +32.98% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Bandwidth` | 0.09 GB/s | 0.10 GB/s | 🟢 +7.88% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency` | 9112.09 µs | 8446.47 µs | 🟢 -7.30% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 315.85 µs | 78.11 µs | ⚪ -75.27% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Throughput` | 2.30 GOP/s | 2.48 GOP/s | 🟢 +7.88% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.95 GB/s | 10.35 GB/s | 🔴 -35.08% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2104.16 µs | 3241.09 µs | 🔴 +54.03% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 368.21 µs | 312.75 µs | ⚪ -15.06% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 3.99 GOP/s | 2.59 GOP/s | 🔴 -35.08% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.42 GB/s | 11.73 GB/s | 🔴 -60.13% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1140.56 µs | 2860.54 µs | 🔴 +150.80% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 19.24 µs | 732.16 µs | ⚪ +3706.18% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.35 GOP/s | 2.93 GOP/s | 🔴 -60.13% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.49 GB/s | 3.39 GB/s | 🔴 -47.80% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 39.30 µs | 794.54 µs | ⚪ +1921.53% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.62 GOP/s | 0.85 GOP/s | 🔴 -47.80% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.30 GB/s | 29.85 GB/s | 🟢 +164.19% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2969.35 µs | 1123.93 µs | 🟢 -62.15% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 536.12 µs | 5.21 µs | ⚪ -99.03% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.83 GOP/s | 7.46 GOP/s | 🟢 +164.19% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.59 GB/s | 0.49 GB/s | 🔴 -69.14% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1318.24 µs | 4271.76 µs | 🔴 +224.05% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 220.16 µs | 135.74 µs | ⚪ -38.35% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 528.90 µs | 965.74 µs | ⚪ +82.59% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 409.00 µs | 430.06 µs | ⚪ +5.15% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 1481.51 µs | 526.60 µs | ⚪ -64.46% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 597.51 µs | 782.09 µs | ⚪ +30.89% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 630.04 µs | 549.30 µs | ⚪ -12.81% |

