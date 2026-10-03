
# IRON

Tested on `2026_10_03_23_52_54` at commit `b73e3f8`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003]</td><td>✅ 5/5</td><td>720.86</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>318.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003]</td><td>✅ 5/5</td><td>668.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>382.88</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003]</td><td>✅ 5/5</td><td>393.40</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>438.52</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>3743.54</td><td>15.36</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>340.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>351.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>521.30</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>471.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>712.44</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>644.98</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>2241.26</td><td>11.37</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>453.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>453.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>467.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 5/5</td><td>4549.24</td><td>13.24</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>374.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>588.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>554.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 5/5</td><td>5162.74</td><td>11.93</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/layer</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rejects_unknown_configurations[geometry]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unknown_configurations[layer_type]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gelu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>319.56</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>373.44</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>777.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>396.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>428.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>486.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3137.20</td><td>11.72</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>602.20</td><td>0.38</td><td>16.24</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>753.66</td><td>0.37</td><td>15.90</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>82614.80</td><td>0.30</td><td>207.96</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>18660.62</td><td>1.35</td><td>920.67</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1]</td><td>✅ 5/5</td><td>4235.98</td><td>1.93</td><td>505.76</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4]</td><td>✅ 5/5</td><td>6720.62</td><td>0.19</td><td>10.05</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemv</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>348.72</td><td>0.10</td><td>0.10</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>9321.86</td><td>3.60</td><td>3.60</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>5806.14</td><td>5.94</td><td>5.93</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>4284.76</td><td>8.38</td><td>8.37</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>9029.10</td><td>3.72</td><td>3.72</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>4607.50</td><td>7.30</td><td>7.30</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>4133.70</td><td>8.23</td><td>8.23</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>1911.86</td><td>2.54</td><td>2.53</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>1857.92</td><td>0.25</td><td>0.24</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>1398.74</td><td>0.35</td><td>0.34</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>1480.00</td><td>1.46</td><td>1.44</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/layer_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>360.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>271.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>346.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>530.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>324.52</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>430.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>2953.60</td><td>12.64</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>446.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>497.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>412.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>464.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>456.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>488.66</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>587.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>949.76</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>3507.40</td><td>10.95</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mem_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>457.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>311.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>555.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>864.80</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>300.82</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>647.10</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>3873.26</td><td>8.73</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mha</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>459.94</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>414.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>415.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>448.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>391.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>495.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3956.94</td><td>10.61</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/repeat</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>394.00</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>288.80</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>382.48</td><td>0.01</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rms_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>410.48</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>640.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>433.26</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>438.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>330.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>331.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>646.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>498.66</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>411.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>541.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>471.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>3919.88</td><td>8.62</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>3725.64</td><td>9.16</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rope</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>368.46</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>693.80</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>523.02</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>453.16</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>433.20</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>398.76</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>820.74</td><td>10.36</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/sigmoid</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>426.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>387.48</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>373.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>392.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>456.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>495.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3849.14</td><td>9.23</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/silu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>361.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>389.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>873.98</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>4101.70</td><td>8.25</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/softmax</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>3362.30</td><td>2.68</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>847.28</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>492.16</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>466.24</td><td>0.29</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/strided_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_strided_copy[bench_flat_4mi]</td><td>✅ 5/5</td><td>2955.90</td><td>5.96</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>446.32</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>348.14</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>499.56</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>299.92</td><td>0.46</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>355.30</td><td>0.42</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>340.92</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>262.74</td><td>0.51</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>326.90</td><td>0.44</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>372.16</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>526.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>12655.08</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>14139.11</td><td>0.00</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]</td><td>✅ 5/5</td><td>27485.29</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]</td><td>✅ 5/5</td><td>23447.96</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_weight_layout_reaches_both_gemms[b_col_maj_False]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_layout_reaches_both_gemms[b_col_maj_True]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/tanh</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>303.60</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>362.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>399.46</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>501.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>755.82</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>478.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3526.02</td><td>10.71</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/transpose</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_1]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_4]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>579.00</td><td>1.11</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>1074.36</td><td>1.88</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>472.72</td><td>1.27</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>3556.44</td><td>5.44</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

