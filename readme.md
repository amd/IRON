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
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 182.02 | ✅ | 329.74 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 180.74 | ✅ | 400.54 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 197.46 | ✅ | 339.84 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 185.44 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 159.72 | ✅ | 627.90 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 129.62 | ✅ | 390.00 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 172.46 | ✅ | 367.84 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 150.92 | ✅ | 296.62 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 148.70 | ✅ | 381.24 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 178.02 | ✅ | 467.22 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 147.40 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 200.08 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 173.26 | ✅ | 269.22 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 144.94 | ✅ | 309.52 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 174.32 | ✅ | 437.72 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 174.28 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 132.64 | ✅ | 288.88 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 141.82 | ✅ | 358.10 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 154.48 | ✅ | 336.10 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 169.36 | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 401.12 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 325.52 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 336.56 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 292.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 387.68 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 216.70 | ✅ | 639.58 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 318.96 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 880.34 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 631.00 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 839.22 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 712.80 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 703.66 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 976.74 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 485.12 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 406.28 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1321.18 |
| test_gemm_split_leg_windowing[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 176.18 | ✅ | 324.26 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 189.48 | ✅ | 323.90 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 211.54 | ✅ | 328.66 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 210.22 | ✅ | 477.68 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 181.58 | ✅ | 444.98 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 174.68 | ✅ | 561.64 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 185.44 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 238.46 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2191.96 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 225.68 | ✅ | 678.42 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 216.26 | ✅ | 462.34 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 47826.26 | ✅ | 82152.00 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 27932.50 | ✅ | 21914.70 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7796.64 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2106.52 | ✅ | 2752.82 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3210.22 | ✅ | 5831.20 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1409.72 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.21 | ✅ | 0.09 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.65 | ✅ | 3.63 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 24.58 | ✅ | 6.58 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 40.64 | ✅ | 10.81 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 40.74 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.60 | ✅ | 3.67 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 24.43 | ✅ | 6.93 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 38.95 | ✅ | 11.56 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 44.74 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.94 | ✅ | 2.98 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.89 | ✅ | 0.47 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.15 | ✅ | 0.63 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 17.56 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 13.21 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 7.74 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.28 | ✅ | 1.61 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.17 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.41 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.30 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 159.22 | ✅ | 358.30 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 160.38 | ✅ | 703.18 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 192.60 | ✅ | 373.00 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 168.48 | ✅ | 387.58 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 168.96 | ✅ | 319.34 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 171.32 | ✅ | 352.62 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 166.52 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.88 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 146.90 | ✅ | 374.16 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 152.50 | ✅ | 401.62 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 147.46 | ✅ | 337.12 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 150.44 | ✅ | 462.02 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 153.36 | ✅ | 335.08 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 155.86 | ✅ | 1042.72 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 145.94 | ✅ | 747.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 157.52 | ✅ | 559.04 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 169.74 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 195.16 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 154.50 | ✅ | 687.82 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 209.40 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 155.32 | ✅ | 306.26 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 169.16 | ✅ | 284.88 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 147.24 | ✅ | 373.08 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 159.82 | ✅ | 519.84 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 182.26 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 192.04 | ✅ | 444.44 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 47537.18 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 151.30 | ✅ | 343.30 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 146.96 | ✅ | 431.96 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 164.54 | ✅ | 323.60 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 150.30 | ✅ | 387.06 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 158.32 | ✅ | 486.34 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 169.50 | ✅ | 443.88 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.44 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 204.32 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 165.36 | ✅ | 322.66 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 185.38 | ✅ | 711.94 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 166.72 | ✅ | 470.10 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 169.34 | ✅ | 386.34 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 182.44 | ✅ | 358.88 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 164.24 | ✅ | 370.40 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 149.94 | ✅ | 397.22 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 224.24 | ✅ | 433.06 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 154.22 | ✅ | 407.76 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 177.02 | ✅ | 720.58 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 161.04 | ✅ | 475.94 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 187.84 | ✅ | 377.70 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 188.58 | ✅ | 407.46 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 164.84 | ✅ | 445.64 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 217.18 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 163.16 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 207.12 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 197.96 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 145.06 | ✅ | 365.66 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 155.88 | ✅ | 344.36 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 158.24 | ✅ | 500.38 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 189.90 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 145.50 | ✅ | 364.10 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 152.76 | ✅ | 350.98 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 149.02 | ✅ | 532.84 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 154.56 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 164.24 | ✅ | 297.06 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 158.74 | ✅ | 356.32 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.26 | ✅ | 449.00 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 172.56 | ✅ | 318.02 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 155.12 | ✅ | 379.84 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.76 | ✅ | 348.12 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 157.44 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 178.28 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 183.76 | ✅ | 353.44 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 189.34 | ✅ | 268.84 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.78 | ✅ | 324.82 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 154.24 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 216.66 | ✅ | 464.00 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 197.00 | ✅ | 506.72 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 195.78 | ✅ | 432.14 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[chunked_transfer] | ✅ | 161.26 | ✅ | 286.90 |
| test_strided_copy[contiguous] | ✅ | 157.44 | ✅ | 343.60 |
| test_strided_copy[four_channels] | ✅ | 217.26 | ✅ | 329.06 |
| test_strided_copy[kv_slot0] | ✅ | 157.18 | ✅ | 497.66 |
| test_strided_copy[kv_slot5] | ✅ | 166.52 | ✅ | 302.58 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 190.04 | ✅ | 301.78 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 180.18 | ✅ | 343.36 |
| test_strided_copy[kv_slot_last] | ✅ | 159.94 | ✅ | 345.02 |
| test_strided_copy[two_channels] | ✅ | 167.18 | ✅ | 341.42 |
| test_strided_copy[two_channels_chunked] | ✅ | 159.50 | ✅ | 496.40 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 967.25 | ✅ | 15663.69 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1024.64 | ✅ | 21104.47 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2194.56 | ✅ | 23560.57 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 262.04 | ✅ | 327.22 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 170.52 | ✅ | 398.08 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 176.08 | ✅ | 432.10 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 210.04 | ✅ | 809.84 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 169.08 | ✅ | 344.34 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 161.28 | ✅ | 373.00 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 177.88 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 254.76 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.18 | ✅ | 466.86 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 252.12 | ✅ | 1582.72 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 210.62 | ✅ | 434.96 |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 165.42 | ✅ | 397.98 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 154.74 | ✅ | 348.10 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 191.40 | ✅ | 338.68 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 163.36 | ✅ | 400.44 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 185.28 | ✅ | 440.70 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 183.90 | ✅ | 349.14 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 218.60 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 231.94 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 188.34 | ✅ | 442.48 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 196.66 | ✅ | 352.98 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 161.34 | ✅ | 333.68 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 185.26 | ✅ | 416.88 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 157.28 | ✅ | 407.00 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 189.30 | ✅ | 760.62 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 216.24 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 205.36 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 169.98 | ✅ | 469.02 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 159.78 | ✅ | 312.64 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 195.84 | ✅ | 403.96 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 170.48 | ✅ | 419.98 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 188.66 | ✅ | 319.22 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 187.48 | ✅ | 508.48 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 237.60 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 199.46 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 197.14 | ✅ | 449.22 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 192.00 | ✅ | 313.64 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 176.66 | ✅ | 306.62 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 167.88 | ✅ | 784.58 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 194.06 | ✅ | 407.88 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 194.06 | ✅ | 356.84 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 172.68 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 182.40 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 172.90 | ✅ | 294.72 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 167.10 | ✅ | 419.16 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 191.60 | ✅ | 317.40 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 185.78 | ✅ | 384.90 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 190.64 | ✅ | 395.70 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 181.98 | ✅ | 360.20 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 174.98 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 229.34 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 171.30 | ✅ | 343.88 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 197.70 | ✅ | 388.96 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 209.22 | ✅ | 338.34 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 162.22 | ✅ | 365.16 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 176.36 | ✅ | 608.04 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 184.88 | ✅ | 405.48 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 175.82 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 195.22 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 170.92 | ✅ | 291.78 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 195.02 | ✅ | 790.52 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 171.54 | ✅ | 382.88 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 162.68 | ✅ | 467.36 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 175.64 | ✅ | 371.70 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 194.22 | ✅ | 340.40 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 168.52 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 202.28 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 173.98 | ✅ | 298.98 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 199.58 | ✅ | 376.92 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 201.74 | ✅ | 356.20 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 198.52 | ✅ | 445.06 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 191.78 | ✅ | 555.90 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 198.22 | ✅ | 671.22 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 185.56 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 214.52 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 161.52 | ✅ | 306.68 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 166.92 | ✅ | 446.20 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 197.76 | ✅ | 407.28 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 196.60 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 209.72 | ✅ | 393.82 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 182.80 | ✅ | 365.02 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 208.48 | ✅ | 301.60 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 184.10 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 177.78 | ✅ | 304.50 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 172.26 | ✅ | 329.06 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 163.50 | ✅ | 337.88 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 199.94 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 164.14 | ✅ | 299.40 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 168.26 | ✅ | 385.22 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 188.98 | ✅ | 375.74 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 191.06 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 172.62 | ✅ | 366.40 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 183.96 | ✅ | 442.96 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 214.28 | ✅ | 731.32 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 207.48 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 176.32 | ✅ | 303.16 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 203.00 | ✅ | 354.16 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 195.64 | ✅ | 372.90 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 208.92 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 163.26 | ✅ | 438.24 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 194.56 | ✅ | 645.86 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 204.18 | ✅ | 307.26 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 188.00 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 173.58 | ✅ | 407.36 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 163.34 | ✅ | 297.20 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 183.98 | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4012.56 | - | - |
| test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 3461.52 |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 741.64 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4053.84 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1070.06 | ✅ | 7121.84 |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7740.14 | - | - |
| test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 4771.98 |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1263.96 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 6736.34 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 365.64 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 331.54 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 295.48 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 320.64 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 385.06 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 318.80 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 347.56 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 240.88 | ✅ | 652.46 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 323.98 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1246.54 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 784.20 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 827.82 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 642.78 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 711.10 |
| test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even] | - | - | ✅ | 885.36 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 833.14 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor] | - | - | ✅ | 703.96 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 572.48 |
| test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | - | - | ✅ | 2391.86 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 378.02 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 640.14 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1340.44 |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 559.56 | ✅ | 2371.46 |
| test_gemm_split_leg_windowing[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_windowing_runs[iter4] | ✅ | - | ✅ | - |
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
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 180.28 | ✅ | 307.08 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 162.04 | ✅ | 306.66 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 155.50 | ✅ | 647.90 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 174.08 | ✅ | 540.40 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 179.86 | ✅ | 342.90 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 184.84 | ✅ | 378.32 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 219.94 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 222.54 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 161.04 | ✅ | 259.50 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 174.38 | ✅ | 368.30 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 175.90 | ✅ | 359.62 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 183.16 | ✅ | 416.50 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 177.86 | ✅ | 351.58 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 190.18 | ✅ | 442.14 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 193.34 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 209.80 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 170.36 | ✅ | 342.92 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 176.02 | ✅ | 634.72 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 189.86 | ✅ | 334.12 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 168.76 | ✅ | 453.12 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 184.02 | ✅ | 392.52 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 198.98 | ✅ | 743.42 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 183.48 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 208.18 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 173.46 | ✅ | 435.20 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 213.38 | ✅ | 376.46 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 167.16 | ✅ | 393.36 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 186.12 | ✅ | 431.52 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 178.86 | ✅ | 500.74 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 176.40 | ✅ | 417.84 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 215.46 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 266.42 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 19135.78 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1] | ✅ | 2259.78 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 203.54 | ✅ | 390.00 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1] | ✅ | 208.46 | ✅ | 481.82 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 47730.36 | ✅ | 82463.70 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1] | ✅ | 118446.96 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 27820.66 | ✅ | 22296.34 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1] | ✅ | 7159.96 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1] | ✅ | 8331.60 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 7768.00 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 94803.16 | ✅ | 95171.90 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 103344.94 | ✅ | 98421.68 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 110384.38 | ✅ | 84749.44 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 37346.58 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1271.68 | ✅ | 3143.68 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1522.66 | ✅ | 3208.36 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 1350.30 | ✅ | 2584.74 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4315.42 | ✅ | 6002.66 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4776.40 | ✅ | 7958.94 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 4865.86 | ✅ | 6595.18 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 93999.78 | ✅ | 100075.02 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 102595.94 | ✅ | 98631.28 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1] | ✅ | 105854.18 | ✅ | 84783.38 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1] | ✅ | 2259.54 | ✅ | 3342.72 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4] | ✅ | 3578.10 | ✅ | 6102.66 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1] | ✅ | 1523.54 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.21 | ✅ | 0.09 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 12.06 | ✅ | 3.77 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 23.32 | ✅ | 6.55 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 39.31 | ✅ | 9.22 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 41.64 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 11.41 | ✅ | 3.60 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 23.78 | ✅ | 6.81 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 36.79 | ✅ | 12.08 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 40.10 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 8.34 | ✅ | 2.01 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 0.98 | ✅ | 0.44 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 1.19 | ✅ | 0.66 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 16.14 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 13.48 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 8.01 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 5.40 | ✅ | 2.01 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 0.21 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 13.02 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 12.32 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 162.22 | ✅ | 311.00 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 149.92 | ✅ | 331.10 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 168.60 | ✅ | 380.72 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 169.68 | ✅ | 424.56 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 185.62 | ✅ | 422.22 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 189.08 | ✅ | 449.08 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 184.44 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 219.48 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 178.92 | ✅ | 319.68 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 174.20 | ✅ | 413.16 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 189.24 | ✅ | 487.92 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 184.56 | ✅ | 467.06 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.52 | ✅ | 414.88 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 188.52 | ✅ | 408.32 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 198.44 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 203.08 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 179.16 | ✅ | 464.98 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 190.76 | ✅ | 422.72 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 174.14 | ✅ | 423.16 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 173.70 | ✅ | 436.14 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 184.60 | ✅ | 490.10 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 184.66 | ✅ | 555.04 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 182.36 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 269.82 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 198.58 | ✅ | 422.34 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 209.70 | ✅ | 760.24 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 151.72 | ✅ | 469.82 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 177.20 | ✅ | 407.44 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 172.88 | ✅ | 339.78 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 183.00 | ✅ | 453.82 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 241.44 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 203.70 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 171.62 | ✅ | 246.12 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 160.28 | ✅ | 297.12 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 163.78 | ✅ | 379.46 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 151.90 | ✅ | 496.58 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 199.42 | ✅ | 345.20 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 198.92 | ✅ | 504.94 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 180.90 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 211.24 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 175.16 | ✅ | 277.84 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 145.94 | ✅ | 377.82 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 175.32 | ✅ | 359.04 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 154.86 | ✅ | 335.50 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 166.84 | ✅ | 407.46 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 184.14 | ✅ | 345.66 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 178.78 | ✅ | 432.34 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 198.52 | ✅ | 807.88 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 182.66 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 204.32 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 160.40 | ✅ | 351.04 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 175.16 | ✅ | 343.02 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 161.38 | ✅ | 390.78 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 171.56 | ✅ | 387.26 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 183.10 | ✅ | 345.92 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 174.78 | ✅ | 564.94 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 168.28 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 219.32 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 174.48 | ✅ | 393.30 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 205.46 | ✅ | 296.20 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 189.48 | ✅ | 349.44 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 172.30 | ✅ | 302.84 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 197.02 | ✅ | 439.54 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 184.82 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 242.30 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 161.74 | ✅ | 303.04 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 175.02 | ✅ | 277.22 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 189.90 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 208.82 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 169.76 | ✅ | 425.60 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 149.50 | ✅ | 403.80 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 144.78 | ✅ | 574.08 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 174.22 | ✅ | 352.94 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 178.48 | ✅ | 400.10 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 168.24 | ✅ | 463.36 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 198.46 | ✅ | 417.72 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 182.76 | ✅ | 450.90 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 222.46 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 199.88 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 176.82 | ✅ | 375.32 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 173.76 | ✅ | 793.94 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 161.54 | ✅ | 276.50 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 160.56 | ✅ | 432.74 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 234.12 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 217.48 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 162.20 | ✅ | 496.60 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 151.52 | ✅ | 383.22 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 175.18 | ✅ | 339.14 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 170.28 | ✅ | 341.64 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 195.62 | ✅ | 402.82 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 171.66 | ✅ | 415.66 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 179.22 | ✅ | 306.02 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 182.94 | ✅ | 499.62 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 177.60 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 172.28 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 178.38 | ✅ | 418.04 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 186.16 | ✅ | 441.20 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 192.46 | ✅ | 399.08 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 189.02 | ✅ | 384.60 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 228.32 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 222.34 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 198.78 | ✅ | 339.22 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 205.10 | ✅ | 448.52 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 207.36 | ✅ | 347.96 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 169.06 | ✅ | 626.20 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 161.62 | ✅ | 446.64 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 187.04 | ✅ | 826.56 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 182.36 | ✅ | 536.70 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 171.24 | ✅ | 369.82 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 188.20 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 188.82 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 197.70 | ✅ | 316.42 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 176.92 | ✅ | 315.96 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 219.20 | ✅ | 286.54 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 184.46 | ✅ | 306.14 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 223.84 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 185.34 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 190.74 | ✅ | 676.52 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 183.60 | ✅ | 617.08 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 174.78 | ✅ | 305.86 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 203.44 | ✅ | 335.24 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 172.66 | ✅ | 380.86 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 161.32 | ✅ | 441.78 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 168.50 | ✅ | 570.52 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 185.78 | ✅ | 338.30 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 190.46 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 186.44 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 183.92 | ✅ | 540.18 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 190.10 | ✅ | 688.94 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 47518.84 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 47420.28 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 375436.24 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 136.76 | ✅ | 287.22 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 159.62 | ✅ | 349.08 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 160.88 | ✅ | 345.54 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 180.90 | ✅ | 318.98 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 196.88 | ✅ | 506.86 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 200.06 | ✅ | 432.58 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 171.42 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 213.62 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 166.60 | ✅ | 351.58 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 175.86 | ✅ | 350.28 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 159.76 | ✅ | 303.16 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 190.56 | ✅ | 421.40 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 164.88 | ✅ | 465.34 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 199.84 | ✅ | 353.50 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 191.72 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 209.54 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 163.08 | ✅ | 386.60 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 167.00 | ✅ | 309.70 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 184.40 | ✅ | 380.26 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 181.70 | ✅ | 434.22 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 180.18 | ✅ | 406.94 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 162.08 | ✅ | 434.18 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 164.96 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 183.66 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 153.36 | ✅ | 428.70 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 153.48 | ✅ | 453.08 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 158.52 | ✅ | 360.34 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 150.06 | ✅ | 335.02 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 181.06 | ✅ | 439.72 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 176.98 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 211.90 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 182.60 | ✅ | 271.52 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 185.12 | ✅ | 333.30 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 828.46 | ✅ | 3189.52 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 160.60 | ✅ | 288.42 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 143.70 | ✅ | 322.94 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 182.98 | ✅ | 394.70 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 159.92 | ✅ | 301.80 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 168.00 | ✅ | 422.10 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 168.30 | ✅ | 347.36 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 172.66 | ✅ | 340.20 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 177.50 | ✅ | 363.94 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 191.60 | ✅ | 373.96 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 167.92 | ✅ | 496.66 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 163.86 | ✅ | 466.24 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 176.08 | ✅ | 380.08 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 184.38 | ✅ | 479.42 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 205.84 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 175.90 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 193.80 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 224.14 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 179.82 | ✅ | 430.54 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 157.64 | ✅ | 511.70 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 172.66 | ✅ | 315.12 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 185.06 | ✅ | 463.64 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 166.96 | ✅ | 356.38 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 159.26 | ✅ | 460.78 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 177.84 | ✅ | 365.16 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 170.98 | ✅ | 451.28 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 170.28 | ✅ | 425.00 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 157.64 | ✅ | 391.50 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 185.08 | ✅ | 651.52 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 205.16 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 183.94 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 198.06 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 213.88 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 175.90 | ✅ | 308.94 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 202.52 | ✅ | 388.10 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 198.96 | ✅ | 319.02 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 189.20 | ✅ | 366.98 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 158.38 | ✅ | 377.36 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 186.60 | ✅ | 478.06 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 197.30 | ✅ | 380.56 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 184.72 | ✅ | 417.00 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 196.62 | ✅ | 510.26 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 219.94 | ✅ | 438.66 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 171.30 | ✅ | 712.54 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 222.32 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 184.48 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 236.86 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 224.04 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 188.72 | ✅ | 322.42 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 162.74 | ✅ | 372.34 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 202.86 | ✅ | 411.72 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 179.88 | ✅ | 460.58 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 166.30 | ✅ | 449.54 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 170.82 | ✅ | 571.10 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 195.96 | ✅ | 477.42 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 177.02 | ✅ | 418.38 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 178.76 | ✅ | 431.26 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 189.90 | ✅ | 419.70 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 215.78 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 212.24 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 200.32 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 227.18 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 172.84 | ✅ | 658.42 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 154.82 | ✅ | 384.18 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 156.20 | ✅ | 740.14 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 190.94 | ✅ | 448.30 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 207.06 | ✅ | 420.78 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 167.48 | ✅ | 432.12 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 175.28 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 197.72 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 164.26 | ✅ | 277.46 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 175.90 | ✅ | 515.94 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 178.90 | ✅ | 526.58 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 178.84 | ✅ | 694.68 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 158.72 | ✅ | 364.20 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 157.92 | ✅ | 423.28 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 172.84 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 164.16 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 153.76 | ✅ | 437.46 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 169.20 | ✅ | 354.50 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 143.74 | ✅ | 455.32 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 148.02 | ✅ | 356.68 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 166.62 | ✅ | 368.68 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 170.88 | ✅ | 498.66 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 208.78 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 167.20 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 170.54 | ✅ | 459.66 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 164.72 | ✅ | 346.34 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 170.26 | ✅ | 678.44 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 146.84 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 169.34 | ✅ | 340.38 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 150.92 | ✅ | 521.10 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 168.12 | ✅ | 396.62 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 179.98 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 160.62 | ✅ | 393.24 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 182.58 | ✅ | 503.52 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 153.36 | ✅ | 367.68 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 159.44 | ✅ | 426.28 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 183.60 | ✅ | 618.14 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 190.78 | ✅ | 488.18 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 185.08 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 177.78 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 220.40 | ✅ | 453.02 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 159.12 | ✅ | 354.48 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 148.50 | ✅ | 379.52 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 156.78 | ✅ | 386.38 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 164.60 | ✅ | 444.94 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 143.74 | ✅ | 457.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 147.70 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 157.30 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 160.84 | ✅ | 479.72 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 193.82 | ✅ | 351.82 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 144.52 | ✅ | 869.96 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 149.62 | ✅ | 403.14 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 152.34 | ✅ | 335.80 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 175.02 | ✅ | 431.98 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 162.44 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 162.52 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 158.68 | ✅ | 447.76 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 143.20 | ✅ | 378.26 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 172.04 | ✅ | 354.48 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 164.20 | ✅ | 606.90 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 172.16 | ✅ | 480.90 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 184.76 | ✅ | 430.94 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 172.68 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 207.26 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 183.52 | ✅ | 427.94 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 167.98 | ✅ | 401.24 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 198.66 | ✅ | 688.56 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 172.24 | ✅ | 395.52 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 184.86 | ✅ | 400.94 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 200.94 | ✅ | 458.18 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 193.92 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 229.18 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 172.54 | ✅ | 401.12 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 163.12 | ✅ | 414.04 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 162.00 | ✅ | 401.14 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 187.30 | ✅ | 403.48 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 185.26 | ✅ | 309.20 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 198.36 | ✅ | 495.72 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 173.02 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 221.04 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 167.72 | ✅ | 439.62 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 181.94 | ✅ | 456.04 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 187.02 | ✅ | 426.66 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 182.24 | ✅ | 762.02 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 169.04 | ✅ | 404.54 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 192.34 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 200.38 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 167.92 | ✅ | 462.42 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 172.98 | ✅ | 503.26 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 202.86 | ✅ | 757.40 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 191.16 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 191.80 | ✅ | 410.40 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 183.86 | ✅ | 551.66 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.62 | ✅ | 390.28 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 182.16 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 195.82 | ✅ | 299.28 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 182.20 | ✅ | 395.26 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 187.92 | ✅ | 422.48 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 216.42 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 192.48 | ✅ | 365.80 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 184.46 | ✅ | 734.82 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 225.66 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 170.12 | ✅ | 455.42 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 155.34 | ✅ | 475.42 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 170.36 | ✅ | 468.76 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[chunked_transfer] | ✅ | 175.68 | ✅ | 385.46 |
| test_strided_copy[contiguous] | ✅ | 175.20 | ✅ | 314.50 |
| test_strided_copy[four_channels] | ✅ | 176.32 | ✅ | 414.88 |
| test_strided_copy[kv_llama_full] | ✅ | 177.58 | ✅ | 339.28 |
| test_strided_copy[kv_slot0] | ✅ | 159.00 | ✅ | 365.00 |
| test_strided_copy[kv_slot5] | ✅ | 149.56 | ✅ | 316.60 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 169.40 | ✅ | 410.38 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 161.62 | ✅ | 322.50 |
| test_strided_copy[kv_slot_last] | ✅ | 169.40 | ✅ | 314.64 |
| test_strided_copy[two_channels] | ✅ | 145.84 | ✅ | 333.30 |
| test_strided_copy[two_channels_chunked] | ✅ | 181.74 | ✅ | 388.66 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 957.96 | ✅ | 13180.15 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1029.68 | ✅ | 16126.55 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False] | ✅ | 2168.52 | ✅ | 20167.87 |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 211.68 | ✅ | 338.26 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 170.12 | ✅ | 815.88 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 170.42 | ✅ | 381.46 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 197.12 | ✅ | 371.12 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 181.02 | ✅ | 348.44 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 191.08 | ✅ | 874.66 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 166.62 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 214.68 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 157.32 | ✅ | 800.30 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 197.38 | ✅ | 357.96 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 177.42 | ✅ | 419.80 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 180.90 | ✅ | 428.50 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 172.14 | ✅ | 475.52 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 175.54 | ✅ | 466.10 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 193.22 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 239.48 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 179.00 | ✅ | 361.20 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 183.04 | ✅ | 368.78 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 181.64 | ✅ | 356.06 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 184.52 | ✅ | 421.62 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 194.20 | ✅ | 400.72 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 182.74 | ✅ | 486.66 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 193.02 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 218.96 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 162.38 | ✅ | 397.94 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 167.30 | ✅ | 477.66 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 159.04 | ✅ | 390.88 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 174.64 | ✅ | 395.82 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 195.32 | ✅ | 432.96 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 200.38 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 213.18 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 224.66 | ✅ | 580.70 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 227.02 | ✅ | 551.04 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 202.54 | ✅ | 489.56 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 207.38 | ✅ | 764.88 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 254.72 | ✅ | 1829.34 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 250.30 | ✅ | 1058.52 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 249.90 | ✅ | 1216.32 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 237.48 | ✅ | 1720.62 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 252.18 | ✅ | 610.58 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 275.52 | ✅ | 697.08 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 395.14 | ✅ | 1576.10 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 366.84 | ✅ | 1737.48 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 350.20 | ✅ | 703.96 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 314.76 | ✅ | 755.32 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 311.42 | ✅ | 1415.72 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 321.94 | ✅ | 582.52 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 307.90 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 320.38 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 191.02 | ✅ | 392.06 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 202.80 | ✅ | 1164.04 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 261.28 | ✅ | 894.58 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 171.24 | ✅ | 352.94 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 190.24 | ✅ | 438.86 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 189.76 | ✅ | 487.28 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 169.26 | ✅ | 430.94 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 198.10 | ✅ | 373.28 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 189.14 | ✅ | 461.60 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 149.04 | ✅ | 370.38 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 165.94 | ✅ | 424.18 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 195.68 | ✅ | 618.98 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 218.96 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 157.56 | ✅ | 348.02 |

</details>

