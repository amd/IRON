# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/llama_3.2_1b</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40] | ✅ | - | - | - |

</details>

## Small

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 193.12 | ✅ | 375.16 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 179.86 | ✅ | 372.26 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 185.98 | ✅ | 789.48 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 193.50 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 166.52 | ✅ | 273.96 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 158.54 | ✅ | 385.26 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 156.42 | ✅ | 432.58 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 168.86 | ✅ | 463.64 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 193.84 | ✅ | 438.78 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 177.16 | ✅ | 445.06 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 201.60 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 225.28 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 159.92 | ✅ | 371.00 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 176.12 | ✅ | 408.86 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 158.32 | ✅ | 376.24 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 165.90 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 149.76 | ✅ | 408.62 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 163.14 | ✅ | 786.92 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 162.70 | ✅ | 399.40 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 190.64 | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 463.18 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 344.42 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 317.10 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 333.50 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 398.02 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 377.86 | ✅ | 640.16 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 331.70 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 990.60 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 621.08 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 1157.06 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 1628.94 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 670.76 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 1082.56 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 708.78 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 461.64 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1393.34 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 176.02 | ✅ | 354.78 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.88 | ✅ | 278.60 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 194.58 | ✅ | 359.56 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 169.04 | ✅ | 664.90 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 164.60 | ✅ | 488.72 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 169.30 | ✅ | 435.12 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.28 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 185.48 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2228.72 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 222.08 | ✅ | 787.86 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 251.54 | ✅ | 957.18 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 47748.80 | ✅ | 82022.86 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 27974.92 | ✅ | 22593.44 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7954.76 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2139.66 | ✅ | 2651.30 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3878.12 | ✅ | 5581.26 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1807.66 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.20 | ✅ | 0.11 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.99 | ✅ | 3.61 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 24.22 | ✅ | 6.09 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 40.48 | ✅ | 10.48 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 41.80 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.53 | ✅ | 3.81 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 23.50 | ✅ | 6.52 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 39.19 | ✅ | 8.52 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 41.78 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 9.15 | ✅ | 2.17 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.92 | ✅ | 0.39 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.25 | ✅ | 0.26 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 17.18 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 12.64 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 8.74 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.43 | ✅ | 1.04 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.22 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.67 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.90 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 157.20 | ✅ | 729.50 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 171.52 | ✅ | 426.26 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 175.46 | ✅ | 545.04 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 181.22 | ✅ | 425.00 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 168.58 | ✅ | 368.64 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 182.98 | ✅ | 390.46 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 194.56 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 240.16 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 169.80 | ✅ | 379.02 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 176.40 | ✅ | 336.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 196.80 | ✅ | 314.60 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 214.38 | ✅ | 449.48 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 190.32 | ✅ | 336.52 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 213.28 | ✅ | 359.86 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 182.70 | ✅ | 380.70 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 203.44 | ✅ | 435.22 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 181.32 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 215.06 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 165.04 | ✅ | 409.84 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 214.80 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 152.86 | ✅ | 292.54 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 155.38 | ✅ | 444.72 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 168.82 | ✅ | 399.98 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 162.50 | ✅ | 445.40 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 184.76 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 171.86 | ✅ | 614.98 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 47493.50 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 169.20 | ✅ | 317.32 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 182.18 | ✅ | 343.08 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 160.60 | ✅ | 426.56 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.08 | ✅ | 444.12 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 206.98 | ✅ | 437.88 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 181.48 | ✅ | 413.76 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 198.14 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 218.26 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 167.10 | ✅ | 303.70 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 153.66 | ✅ | 256.90 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 167.28 | ✅ | 280.28 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 171.76 | ✅ | 310.38 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 185.50 | ✅ | 347.78 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 173.42 | ✅ | 499.98 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 183.88 | ✅ | 451.16 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 192.64 | ✅ | 294.60 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 187.26 | ✅ | 422.38 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 174.72 | ✅ | 353.14 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 206.60 | ✅ | 495.94 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 194.78 | ✅ | 473.40 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 202.16 | ✅ | 465.88 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 189.36 | ✅ | 426.24 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 223.66 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 182.16 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 230.98 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 219.32 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 173.96 | ✅ | 376.34 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 177.70 | ✅ | 353.58 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 170.12 | ✅ | 506.04 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 225.24 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 179.56 | ✅ | 452.72 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 170.64 | ✅ | 427.78 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 199.72 | ✅ | 678.48 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 206.78 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 165.52 | ✅ | 312.22 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 172.32 | ✅ | 535.16 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 141.02 | ✅ | 356.60 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 177.52 | ✅ | 324.34 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 188.28 | ✅ | 345.10 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 205.32 | ✅ | 393.22 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 194.70 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 192.72 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 218.58 | ✅ | 440.46 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 186.66 | ✅ | 404.90 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 189.48 | ✅ | 447.98 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 225.78 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 186.52 | ✅ | 428.20 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 178.38 | ✅ | 429.44 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 169.28 | ✅ | 409.16 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[chunked_transfer] | ✅ | 153.66 | ✅ | 374.74 |
| test_strided_copy[contiguous] | ✅ | 164.32 | ✅ | 441.46 |
| test_strided_copy[four_channels] | ✅ | 167.42 | ✅ | 280.44 |
| test_strided_copy[kv_slot0] | ✅ | 174.58 | ✅ | 366.28 |
| test_strided_copy[kv_slot5] | ✅ | 158.42 | ✅ | 333.00 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 190.10 | ✅ | 441.96 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 174.88 | ✅ | 360.30 |
| test_strided_copy[kv_slot_last] | ✅ | 163.74 | ✅ | 255.28 |
| test_strided_copy[two_channels] | ✅ | 162.00 | ✅ | 368.82 |
| test_strided_copy[two_channels_chunked] | ✅ | 176.36 | ✅ | 361.62 |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 955.67 | ✅ | 12839.75 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1027.66 | ✅ | 15348.50 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2167.31 | ✅ | 25986.49 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 155.28 | ✅ | 364.56 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 162.62 | ✅ | 348.90 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 160.58 | ✅ | 505.38 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 165.78 | ✅ | 423.72 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 172.84 | ✅ | 366.04 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 219.96 | ✅ | 426.26 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 172.84 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 202.20 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 162.44 | ✅ | 500.96 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 184.24 | ✅ | 1125.12 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 155.54 | ✅ | 406.06 |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 213.06 | ✅ | 363.58 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 174.52 | ✅ | 426.74 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 180.22 | ✅ | 376.88 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 194.56 | ✅ | 308.88 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 168.84 | ✅ | 424.00 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 174.80 | ✅ | 422.42 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 198.64 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 219.72 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 166.64 | ✅ | 388.74 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 160.60 | ✅ | 329.82 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 185.60 | ✅ | 294.38 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 184.94 | ✅ | 277.82 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 178.24 | ✅ | 447.74 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 189.70 | ✅ | 352.56 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 184.88 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 184.22 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 173.50 | ✅ | 315.36 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 161.32 | ✅ | 354.16 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 185.04 | ✅ | 361.88 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 165.84 | ✅ | 354.92 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 136.66 | ✅ | 409.42 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 179.50 | ✅ | 309.78 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 197.08 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 180.68 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 179.64 | ✅ | 525.28 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 183.32 | ✅ | 427.74 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 178.88 | ✅ | 529.32 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 149.64 | ✅ | 515.50 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 202.86 | ✅ | 1072.88 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 185.84 | ✅ | 345.72 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 212.22 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 198.08 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 174.32 | ✅ | 466.98 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 172.94 | ✅ | 344.40 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 171.30 | ✅ | 413.82 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 186.82 | ✅ | 392.48 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 189.08 | ✅ | 362.22 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 178.72 | ✅ | 483.10 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 203.00 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 214.88 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 152.08 | ✅ | 327.84 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 191.98 | ✅ | 375.46 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 187.62 | ✅ | 382.52 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 167.80 | ✅ | 429.08 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 169.44 | ✅ | 412.60 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 181.40 | ✅ | 779.54 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 206.46 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 197.88 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 179.82 | ✅ | 451.74 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 164.72 | ✅ | 416.04 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 185.78 | ✅ | 362.02 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 185.40 | ✅ | 339.04 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 202.72 | ✅ | 805.24 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 193.46 | ✅ | 508.14 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 199.34 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 220.30 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 224.72 | ✅ | 409.86 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 181.04 | ✅ | 451.72 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 175.30 | ✅ | 426.22 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 202.84 | ✅ | 488.88 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 166.72 | ✅ | 396.30 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 220.78 | ✅ | 528.12 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 185.46 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 218.90 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 154.44 | ✅ | 468.12 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 171.02 | ✅ | 357.08 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 168.40 | ✅ | 394.88 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 212.64 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 168.32 | ✅ | 395.40 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 176.58 | ✅ | 429.10 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 163.40 | ✅ | 432.36 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 199.88 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 192.26 | ✅ | 393.62 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 180.48 | ✅ | 448.14 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 157.76 | ✅ | 717.22 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 176.04 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 170.42 | ✅ | 618.02 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 177.12 | ✅ | 355.96 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 169.18 | ✅ | 843.82 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 163.52 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 179.96 | ✅ | 404.06 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 189.60 | ✅ | 359.06 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 204.96 | ✅ | 408.48 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 190.10 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 213.64 | ✅ | 453.64 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 204.80 | ✅ | 416.18 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 217.32 | ✅ | 424.26 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 217.90 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 200.22 | ✅ | 424.50 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 205.00 | ✅ | 774.22 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 187.58 | ✅ | 473.44 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 205.12 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 169.34 | ✅ | 433.32 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 189.24 | ✅ | 348.80 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 198.66 | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4200.24 | - | - |
| test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 3723.34 |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 964.76 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4087.54 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1481.86 | ✅ | 7191.06 |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7731.94 | - | - |
| test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 6139.88 |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1508.74 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7712.98 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 467.96 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 375.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 337.68 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 348.22 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 428.86 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 450.54 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 439.56 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 321.90 | ✅ | 593.58 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 404.78 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 792.40 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 826.64 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 1005.16 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 913.28 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 753.80 |
| test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even] | - | - | ✅ | 796.94 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 704.10 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor] | - | - | ✅ | 1064.74 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 559.88 |
| test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | - | - | ✅ | 1875.52 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 425.06 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 696.42 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1153.22 |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 700.04 | ✅ | 3023.62 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32] | - | - | ✅ | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/mm_prebuilt</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 176.24 | ✅ | 314.16 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 171.92 | ✅ | 408.58 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 162.86 | ✅ | 320.14 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 170.52 | ✅ | 371.96 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 158.98 | ✅ | 444.58 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 150.96 | ✅ | 428.66 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 169.86 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 209.72 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 184.70 | ✅ | 447.52 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 202.94 | ✅ | 908.42 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 156.82 | ✅ | 793.64 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 204.04 | ✅ | 518.44 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 155.50 | ✅ | 416.44 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 223.60 | ✅ | 488.60 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 185.70 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 223.20 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 176.48 | ✅ | 433.76 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 141.44 | ✅ | 438.12 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 165.50 | ✅ | 470.08 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 135.68 | ✅ | 436.56 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 181.72 | ✅ | 403.76 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 204.12 | ✅ | 454.62 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 184.04 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 202.62 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 174.28 | ✅ | 443.88 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 183.62 | ✅ | 310.42 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 208.80 | ✅ | 387.94 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 177.92 | ✅ | 421.50 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 192.70 | ✅ | 354.06 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 202.04 | ✅ | 373.42 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 175.96 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 208.58 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 19140.16 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2292.40 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 236.98 | ✅ | 812.24 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 213.02 | ✅ | 601.94 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 47834.04 | ✅ | 82203.30 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1] | ✅ | 118604.84 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 27911.78 | ✅ | 22768.66 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1] | ✅ | 7013.48 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1] | ✅ | 8648.42 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7876.86 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 94840.20 | ✅ | 96284.86 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 103167.04 | ✅ | 99159.98 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 110382.84 | ✅ | 84919.80 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 37505.70 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1254.66 | ✅ | 1915.10 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1433.00 | ✅ | 2657.42 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1396.32 | ✅ | 2865.24 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4533.94 | ✅ | 7109.62 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4657.06 | ✅ | 8043.90 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4736.76 | ✅ | 7054.16 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 94089.96 | ✅ | 100199.04 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 102593.50 | ✅ | 100260.52 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 105923.70 | ✅ | 84930.08 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2458.08 | ✅ | 3175.14 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3110.64 | ✅ | 6705.70 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1548.68 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.19 | ✅ | 0.10 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.24 | ✅ | 3.65 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 24.15 | ✅ | 5.91 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 40.64 | ✅ | 8.63 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 43.24 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.23 | ✅ | 3.70 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 24.50 | ✅ | 5.59 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 41.79 | ✅ | 9.06 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 42.02 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.83 | ✅ | 1.69 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.93 | ✅ | 0.37 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.26 | ✅ | 0.54 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 17.31 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 13.66 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 8.10 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.92 | ✅ | 1.78 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.20 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.59 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.28 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 176.20 | ✅ | 295.00 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 149.34 | ✅ | 314.58 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 175.64 | ✅ | 497.04 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 184.04 | ✅ | 435.78 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 172.00 | ✅ | 532.36 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 162.58 | ✅ | 424.60 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 165.88 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 192.72 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 145.42 | ✅ | 334.00 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 169.14 | ✅ | 994.92 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 172.44 | ✅ | 312.48 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 206.12 | ✅ | 377.60 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 150.78 | ✅ | 434.28 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 189.16 | ✅ | 410.92 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 187.10 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 196.26 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 171.34 | ✅ | 418.66 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 165.44 | ✅ | 434.14 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 166.84 | ✅ | 390.88 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 156.54 | ✅ | 484.60 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 169.96 | ✅ | 493.28 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 198.90 | ✅ | 398.08 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 176.94 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 221.74 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 172.26 | ✅ | 736.64 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 165.34 | ✅ | 497.92 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 176.24 | ✅ | 413.10 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 195.76 | ✅ | 441.74 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 178.34 | ✅ | 387.36 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 203.30 | ✅ | 486.90 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 229.36 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 238.50 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 163.10 | ✅ | 281.18 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 160.26 | ✅ | 395.68 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 161.14 | ✅ | 269.82 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 187.04 | ✅ | 326.22 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 165.42 | ✅ | 337.14 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 178.14 | ✅ | 378.98 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 215.42 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 215.36 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 192.12 | ✅ | 793.50 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 162.60 | ✅ | 360.74 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 181.68 | ✅ | 318.02 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 185.12 | ✅ | 373.56 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 180.82 | ✅ | 483.90 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 184.50 | ✅ | 469.68 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 193.84 | ✅ | 367.64 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 185.04 | ✅ | 408.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 187.32 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 206.72 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 149.60 | ✅ | 311.26 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 163.88 | ✅ | 723.76 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 194.82 | ✅ | 327.06 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 182.42 | ✅ | 327.26 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 174.74 | ✅ | 348.94 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 169.70 | ✅ | 394.40 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 176.56 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 240.60 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 183.90 | ✅ | 368.20 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 159.16 | ✅ | 420.06 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 171.62 | ✅ | 294.22 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 175.04 | ✅ | 385.26 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 167.44 | ✅ | 398.62 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 173.90 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 208.94 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 165.34 | ✅ | 408.18 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 161.52 | ✅ | 336.34 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ❌ | 4746104.65 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 187.06 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 170.24 | ✅ | 443.96 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 157.40 | ✅ | 370.08 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 173.66 | ✅ | 360.26 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 162.04 | ✅ | 338.72 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 173.88 | ✅ | 431.40 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 162.76 | ✅ | 409.50 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 172.56 | ✅ | 420.50 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 164.86 | ✅ | 430.86 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 189.34 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 188.14 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 170.04 | ❌ | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 150.62 | ✅ | 691.64 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 186.74 | ✅ | 474.16 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 190.16 | ✅ | 393.88 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 199.96 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 165.54 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 184.06 | ✅ | 531.46 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 165.38 | ✅ | 522.38 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 153.20 | ✅ | 340.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 164.16 | ✅ | 282.06 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 155.00 | ✅ | 432.10 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 174.62 | ✅ | 408.06 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 147.70 | ✅ | 462.46 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 171.12 | ✅ | 436.72 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 176.14 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 194.70 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 163.82 | ✅ | 437.96 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 152.34 | ✅ | 402.90 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 128.28 | ✅ | 398.08 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 136.86 | ✅ | 378.04 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 188.80 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 187.14 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 167.64 | ✅ | 418.82 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 158.40 | ✅ | 406.78 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 149.66 | ✅ | 448.42 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 157.66 | ✅ | 393.84 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 144.12 | ✅ | 727.06 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 154.98 | ✅ | 417.70 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 158.64 | ✅ | 417.08 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 167.76 | ✅ | 421.94 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 182.86 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 161.36 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 171.82 | ✅ | 419.68 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 171.10 | ✅ | 773.98 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 145.16 | ✅ | 400.92 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 174.28 | ✅ | 295.88 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 217.18 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 187.02 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 158.36 | ✅ | 410.60 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 155.38 | ✅ | 360.34 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 144.42 | ✅ | 405.20 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 158.56 | ✅ | 348.94 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 173.14 | ✅ | 463.08 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 162.50 | ✅ | 470.16 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 158.00 | ✅ | 450.24 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 200.88 | ✅ | 444.78 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 185.44 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 156.20 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 172.60 | ✅ | 433.18 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 176.56 | ✅ | 714.18 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 47522.62 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 47559.72 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 375450.34 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 150.54 | ✅ | 328.08 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 161.92 | ✅ | 412.80 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 175.70 | ✅ | 445.62 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 172.12 | ✅ | 495.68 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 184.08 | ✅ | 538.90 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 177.98 | ✅ | 458.62 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 172.08 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 213.94 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 151.84 | ✅ | 281.32 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.08 | ✅ | 719.38 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 163.04 | ✅ | 434.14 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 161.00 | ✅ | 464.76 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 160.76 | ✅ | 721.42 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 195.30 | ✅ | 465.76 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 184.06 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 200.96 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 155.06 | ✅ | 402.58 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 158.02 | ✅ | 655.14 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 201.14 | ✅ | 348.16 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 165.60 | ✅ | 413.18 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 187.76 | ✅ | 499.28 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 185.72 | ✅ | 454.40 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 165.16 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 250.84 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 144.54 | ✅ | 361.30 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 171.52 | ✅ | 397.84 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 180.30 | ✅ | 708.58 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 155.86 | ✅ | 440.22 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 168.10 | ✅ | 507.54 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 169.50 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 189.44 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 151.66 | ✅ | 322.98 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 165.68 | ✅ | 292.60 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 808.52 | ✅ | 3280.88 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 167.74 | ✅ | 383.60 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 138.78 | ✅ | 388.28 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 159.00 | ✅ | 357.48 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 158.62 | ✅ | 387.96 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 152.96 | ✅ | 365.92 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 168.90 | ✅ | 428.56 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 153.08 | ✅ | 566.22 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 155.40 | ✅ | 526.48 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 168.32 | ✅ | 394.68 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 160.40 | ✅ | 395.54 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 174.06 | ✅ | 457.68 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 162.90 | ✅ | 623.60 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 180.84 | ✅ | 444.74 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 176.88 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 187.76 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 197.48 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 211.86 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 157.86 | ✅ | 383.32 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 180.98 | ✅ | 280.36 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 152.18 | ✅ | 503.32 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 150.38 | ✅ | 374.06 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 158.86 | ✅ | 402.66 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 147.26 | ✅ | 381.32 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 159.92 | ✅ | 839.58 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 193.34 | ✅ | 486.94 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 156.12 | ✅ | 744.76 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 183.64 | ✅ | 432.76 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 181.16 | ✅ | 468.88 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 227.06 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 215.34 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 215.08 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 218.08 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 173.46 | ✅ | 429.84 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 177.02 | ✅ | 477.62 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 174.38 | ✅ | 442.24 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 207.68 | ✅ | 468.94 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 176.68 | ✅ | 299.84 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 180.28 | ✅ | 433.44 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 160.20 | ✅ | 355.90 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 172.88 | ✅ | 743.72 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 166.34 | ✅ | 425.20 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 177.00 | ✅ | 435.60 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 208.66 | ✅ | 509.82 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 199.66 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 167.26 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 184.94 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 196.42 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 168.20 | ✅ | 398.36 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 174.70 | ✅ | 365.98 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 160.40 | ✅ | 653.04 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 168.58 | ✅ | 433.26 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 188.30 | ✅ | 413.56 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 149.30 | ✅ | 430.42 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 188.44 | ✅ | 423.32 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 148.44 | ✅ | 380.94 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 197.70 | ✅ | 415.66 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 174.34 | ✅ | 1159.76 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 213.62 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 203.42 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 200.16 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 223.94 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 171.92 | ✅ | 332.88 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 171.06 | ✅ | 390.28 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 181.76 | ✅ | 610.60 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 183.38 | ✅ | 446.64 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 160.58 | ✅ | 285.84 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 177.16 | ✅ | 331.88 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 182.76 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 189.84 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 179.86 | ✅ | 350.16 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 168.32 | ✅ | 514.54 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 172.56 | ✅ | 452.18 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 165.72 | ✅ | 454.68 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 163.26 | ✅ | 363.62 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 193.18 | ✅ | 393.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 189.92 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 189.98 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 178.36 | ✅ | 325.92 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 189.32 | ✅ | 314.92 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 197.02 | ✅ | 451.96 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 184.00 | ✅ | 386.52 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 175.76 | ✅ | 405.76 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 180.36 | ✅ | 409.48 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 198.80 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 178.16 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 184.06 | ✅ | 441.32 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 197.80 | ✅ | 656.90 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 177.42 | ✅ | 549.60 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 195.56 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 154.44 | ✅ | 373.40 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 184.10 | ✅ | 737.86 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 159.36 | ✅ | 337.72 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 184.16 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 173.32 | ✅ | 344.40 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 167.02 | ✅ | 401.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 171.90 | ✅ | 379.30 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 160.84 | ✅ | 562.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 187.88 | ✅ | 403.86 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 168.88 | ✅ | 389.82 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 214.74 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 204.90 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 162.60 | ✅ | 414.22 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 194.66 | ✅ | 413.66 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 201.42 | ✅ | 416.30 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 183.96 | ✅ | 380.76 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 164.08 | ✅ | 359.08 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 180.88 | ✅ | 355.72 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 170.40 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 197.96 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 178.20 | ✅ | 373.30 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 168.08 | ✅ | 766.20 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 168.12 | ✅ | 449.78 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 195.04 | ✅ | 380.30 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 182.94 | ✅ | 508.48 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 181.36 | ✅ | 307.54 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 184.98 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 170.40 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 168.26 | ✅ | 254.54 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 177.14 | ✅ | 335.44 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 192.50 | ✅ | 316.00 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 143.80 | ✅ | 425.80 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 166.64 | ✅ | 357.02 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 188.54 | ✅ | 399.90 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 188.40 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 204.22 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 162.94 | ✅ | 407.80 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 182.06 | ✅ | 252.78 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 185.22 | ✅ | 441.34 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 180.56 | ✅ | 297.52 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 157.72 | ✅ | 468.14 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 204.54 | ✅ | 465.34 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 190.54 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 219.54 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 178.28 | ✅ | 435.68 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 164.26 | ✅ | 436.70 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 165.52 | ✅ | 347.98 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 165.52 | ✅ | 396.18 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 182.26 | ✅ | 339.58 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 207.36 | ✅ | 389.16 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 176.66 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 233.18 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 172.54 | ✅ | 273.78 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 195.46 | ✅ | 314.62 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 188.16 | ✅ | 394.18 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 172.22 | ✅ | 375.30 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 173.14 | ✅ | 405.10 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 159.70 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 249.68 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 175.14 | ✅ | 404.20 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 146.74 | ✅ | 373.64 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 165.14 | ✅ | 488.00 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 208.86 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 179.64 | ✅ | 414.56 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 191.80 | ✅ | 403.22 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 214.22 | ✅ | 720.62 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 190.30 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 169.08 | ✅ | 389.62 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 199.46 | ✅ | 308.50 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 178.64 | ✅ | 467.10 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 184.58 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 166.54 | ✅ | 335.66 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 187.52 | ✅ | 362.82 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 165.18 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 173.38 | ✅ | 461.36 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 187.62 | ✅ | 502.86 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 179.52 | ✅ | 558.52 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[chunked_transfer] | ✅ | 150.90 | ✅ | 266.24 |
| test_strided_copy[contiguous] | ✅ | 166.38 | ✅ | 325.82 |
| test_strided_copy[four_channels] | ✅ | 166.78 | ✅ | 466.40 |
| test_strided_copy[kv_llama_full] | ✅ | 155.18 | ✅ | 311.46 |
| test_strided_copy[kv_slot0] | ✅ | 149.46 | ✅ | 376.00 |
| test_strided_copy[kv_slot5] | ✅ | 163.64 | ✅ | 647.54 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 160.38 | ✅ | 304.90 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 196.36 | ✅ | 375.06 |
| test_strided_copy[kv_slot_last] | ✅ | 186.94 | ✅ | 308.08 |
| test_strided_copy[two_channels] | ✅ | 146.56 | ✅ | 289.92 |
| test_strided_copy[two_channels_chunked] | ✅ | 145.94 | ✅ | 305.42 |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 970.29 | ✅ | 9772.80 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1032.39 | ✅ | 6421.46 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2174.49 | ✅ | 22136.16 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 144.42 | ✅ | 667.08 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 134.36 | ✅ | 786.84 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 165.94 | ✅ | 774.56 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 172.06 | ✅ | 413.14 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 163.54 | ✅ | 434.26 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 169.64 | ✅ | 425.46 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 189.86 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 194.82 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 163.00 | ✅ | 706.10 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 152.82 | ✅ | 394.14 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 160.26 | ✅ | 383.20 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 168.34 | ✅ | 433.64 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 213.08 | ✅ | 533.04 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 176.10 | ✅ | 427.12 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 169.48 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 196.70 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 149.34 | ✅ | 308.60 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 161.38 | ✅ | 379.74 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 166.10 | ✅ | 496.48 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 188.20 | ✅ | 640.68 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 165.78 | ✅ | 438.28 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 186.96 | ✅ | 407.72 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 173.00 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 195.04 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 183.62 | ✅ | 339.18 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 145.82 | ✅ | 462.80 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 164.14 | ✅ | 502.08 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 157.84 | ✅ | 315.74 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 170.82 | ✅ | 495.60 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 184.86 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 202.56 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 226.84 | ✅ | 1321.96 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 234.88 | ✅ | 526.98 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 213.02 | ✅ | 526.04 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 195.08 | ✅ | 497.48 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 264.04 | ✅ | 1170.66 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 267.32 | ✅ | 2397.40 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 290.90 | ✅ | 1359.94 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 249.06 | ✅ | 1226.32 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 274.84 | ✅ | 1652.26 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 258.72 | ✅ | 1188.32 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 362.86 | ✅ | 947.88 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 357.48 | ✅ | 2278.28 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 367.00 | ✅ | 1655.50 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 317.56 | ✅ | 1103.00 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 319.36 | ✅ | 1005.66 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 340.62 | ✅ | 887.24 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 324.06 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 334.20 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 205.76 | ✅ | 460.14 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 209.90 | ✅ | 1603.86 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 277.46 | ✅ | 2186.18 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 199.96 | ✅ | 505.76 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 161.76 | ✅ | 334.58 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 164.24 | ✅ | 508.68 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 164.10 | ✅ | 393.06 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 169.10 | ✅ | 405.90 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 153.72 | ✅ | 743.54 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 184.02 | ✅ | 326.10 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.76 | ✅ | 779.86 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 192.28 | ✅ | 514.26 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 189.16 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 173.24 | ✅ | 431.10 |

</details>

