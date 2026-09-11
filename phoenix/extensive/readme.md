
# IRON

Tested on `2026_09_11_19_47_54` at commit `7b55427`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>296.80</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>253.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>339.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>307.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>643.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>408.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>352.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>325.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>383.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>470.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>349.32</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>619.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>330.14</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>300.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>304.74</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>356.34</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>421.24</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>474.86</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]</td><td>✅ 5/5</td><td>344.86</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]</td><td>✅ 5/5</td><td>336.18</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>363.92</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>414.62</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>332.00</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>314.86</td><td>0.17</td><td>n/a</td></tr>
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
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>392.44</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>342.78</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>305.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>538.50</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>395.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>426.36</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>389.14</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>363.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>484.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>457.34</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>558.18</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>471.94</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>308.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>711.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>474.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>485.00</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>430.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>474.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]</td><td>✅ 5/5</td><td>390.74</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>410.66</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>288.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>425.84</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>470.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>394.24</td><td>0.06</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>318.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>434.48</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>397.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>337.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>397.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>484.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>332.10</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>403.42</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>527.88</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]</td><td>✅ 5/5</td><td>400.36</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>407.76</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>429.50</td><td>0.12</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>410.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>327.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>408.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>300.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>410.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>491.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>433.72</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>397.80</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>465.52</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>403.04</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>419.44</td><td>0.13</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>3461.72</td><td>3.30</td><td>1351.33</td></tr>
        <tr><td>test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>7720.40</td><td>3.07</td><td>1749.11</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>4880.16</td><td>3.44</td><td>1761.67</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>466.18</td><td>0.99</td><td>72.72</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>508.60</td><td>1.37</td><td>139.91</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>747.90</td><td>1.13</td><td>125.90</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>863.08</td><td>1.25</td><td>160.03</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>660.50</td><td>1.66</td><td>212.16</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>1283.94</td><td>1.28</td><td>164.09</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>684.98</td><td>1.66</td><td>213.00</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>796.76</td><td>1.37</td><td>175.71</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>1234.56</td><td>1.10</td><td>141.03</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>507.02</td><td>0.83</td><td>38.74</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>2305.08</td><td>1.90</td><td>486.35</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>1370.16</td><td>2.97</td><td>607.82</td></tr>
        <tr><td>test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>2577.30</td><td>3.13</td><td>962.78</td></tr>
        <tr><td>test_gemm_split_leg_windowing[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing_runs[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing_runs[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing_runs[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing_runs[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_windowing_runs[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma16-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>330.48</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>400.80</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>462.36</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>500.84</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>398.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>488.40</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>405.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>402.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>382.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>428.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>375.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>423.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>360.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>348.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>418.44</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>1154.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>424.78</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>691.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>388.00</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>473.22</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>429.06</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>384.44</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>422.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>700.94</td><td>0.08</td><td>n/a</td></tr>
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
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>650.10</td><td>0.39</td><td>16.80</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>985.14</td><td>0.29</td><td>12.57</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>83833.74</td><td>0.30</td><td>205.05</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>22268.92</td><td>1.13</td><td>771.70</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>95970.00</td><td>0.79</td><td>716.23</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>97995.30</td><td>0.77</td><td>701.28</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>84382.10</td><td>0.89</td><td>814.39</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2141.86</td><td>4.27</td><td>256.99</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>3512.66</td><td>2.77</td><td>166.79</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>2837.28</td><td>3.54</td><td>213.33</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>6402.10</td><td>5.56</td><td>342.68</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>6877.16</td><td>5.11</td><td>314.93</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>6211.50</td><td>5.64</td><td>347.67</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>99513.02</td><td>0.76</td><td>690.84</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>99268.06</td><td>0.76</td><td>692.35</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>85860.48</td><td>0.88</td><td>800.42</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]</td><td>✅ 5/5</td><td>4253.02</td><td>2.27</td><td>594.30</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]</td><td>✅ 5/5</td><td>6990.04</td><td>0.19</td><td>10.09</td></tr>
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
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>n/a</td><td>0.07</td><td>0.07</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>n/a</td><td>3.58</td><td>3.57</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>6.25</td><td>6.24</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>n/a</td><td>7.70</td><td>7.69</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>3.60</td><td>3.60</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>6.29</td><td>6.29</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>n/a</td><td>8.43</td><td>8.42</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>2.84</td><td>2.84</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>n/a</td><td>0.23</td><td>0.23</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>n/a</td><td>0.62</td><td>0.61</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>n/a</td><td>1.82</td><td>1.79</td></tr>
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
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>369.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>795.32</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>797.68</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>387.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>729.16</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>483.26</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>390.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>305.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>340.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>382.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>796.88</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>567.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>425.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>423.14</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>440.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>497.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>461.68</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>477.78</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>330.98</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>419.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>501.02</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>403.42</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>385.16</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>338.16</td><td>0.11</td><td>n/a</td></tr>
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
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>336.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>699.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>355.60</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>368.56</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>458.44</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>412.32</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>274.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>383.98</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>322.66</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>349.78</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>406.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>354.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>321.00</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>453.38</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>368.94</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>342.92</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>499.58</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>380.32</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>399.96</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>438.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>375.06</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>270.36</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>403.52</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>341.88</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>451.40</td><td>0.08</td><td>n/a</td></tr>
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
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>433.62</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>368.00</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>498.44</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>343.60</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>809.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>385.04</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>394.14</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>435.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>427.98</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>364.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>435.60</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>514.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>425.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>635.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>560.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>397.38</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>754.52</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>268.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>511.60</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>385.96</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>402.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>351.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>606.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>1145.06</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>392.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>314.36</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>387.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>393.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>389.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>395.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>360.22</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>525.18</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>497.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>335.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>594.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>454.42</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]</td><td>✅ 5/5</td><td>814.08</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]</td><td>✅ 5/5</td><td>380.08</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>326.62</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>409.62</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>357.22</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>385.48</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>403.24</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>378.16</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>505.70</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>394.32</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>465.84</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>549.78</td><td>0.07</td><td>n/a</td></tr>
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
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>283.86</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>367.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>481.92</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>382.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>448.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>716.50</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>319.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>291.94</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>306.34</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>465.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>358.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>451.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>359.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>494.34</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>368.34</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>416.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>728.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>535.22</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>478.02</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>316.24</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>498.70</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>404.22</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>442.64</td><td>0.08</td><td>n/a</td></tr>
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
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>318.02</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>268.30</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>3407.64</td><td>3.16</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>617.64</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>316.16</td><td>0.02</td><td>n/a</td></tr>
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
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>294.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>327.16</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>426.78</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>391.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>432.20</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>352.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>459.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>335.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>423.38</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>437.18</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>401.58</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>343.82</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>669.62</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>397.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>429.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>421.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>418.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>395.02</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>494.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>627.62</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>374.62</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>433.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>372.26</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>366.38</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>327.00</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>360.46</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>368.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>416.16</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>389.10</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>455.78</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>383.24</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>462.62</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>421.40</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]</td><td>✅ 5/5</td><td>334.02</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>833.90</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>425.08</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>362.24</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>487.60</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>313.54</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>374.90</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>522.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>449.60</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>403.04</td><td>0.09</td><td>n/a</td></tr>
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
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>391.88</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>392.98</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>673.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>663.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>391.90</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>356.18</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>304.70</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>462.68</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>393.56</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>437.70</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>440.00</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>390.46</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>820.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>289.32</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>340.68</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>483.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>471.90</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>468.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>715.36</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>337.22</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>502.96</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>404.14</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>410.66</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>963.82</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>435.38</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>361.66</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>432.94</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>350.94</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>329.90</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>311.92</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>317.60</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>404.00</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>365.46</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>376.20</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>739.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>471.20</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>333.70</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>390.42</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>414.34</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>272.24</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>1125.28</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>353.12</td><td>0.11</td><td>n/a</td></tr>
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
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>408.32</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>351.06</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>360.20</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>394.56</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>341.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>801.52</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>370.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>256.02</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>719.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>343.56</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>364.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>482.76</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>394.14</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>346.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>885.52</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>670.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>320.68</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>410.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>1015.98</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>649.72</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>395.96</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>726.30</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>506.10</td><td>0.07</td><td>n/a</td></tr>
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
        <tr><td>test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>331.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>323.64</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>905.40</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>357.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>369.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>461.18</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>309.48</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>469.48</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>577.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>398.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>391.66</td><td>0.09</td><td>n/a</td></tr>
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
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>563.50</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>500.66</td><td>0.29</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>580.10</td><td>0.23</td><td>n/a</td></tr>
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
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>294.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>349.18</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>462.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_llama_full]</td><td>✅ 5/5</td><td>355.66</td><td>6.46</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>299.92</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>413.52</td><td>0.34</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>328.26</td><td>0.42</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>367.64</td><td>0.38</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>419.20</td><td>0.35</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>390.24</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>348.56</td><td>0.01</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>11766.76</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>17356.01</td><td>0.00</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]</td><td>✅ 5/5</td><td>22972.38</td><td>0.10</td><td>n/a</td></tr>
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
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>274.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>429.02</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>430.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>457.80</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>505.18</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>638.42</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>438.80</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>309.10</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>462.50</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>334.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>392.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>432.22</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>468.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>432.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>640.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>361.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>303.82</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>445.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>487.70</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>326.14</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>396.82</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>290.10</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>514.32</td><td>0.07</td><td>n/a</td></tr>
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
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1756.72</td><td>1.15</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1094.16</td><td>2.00</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>577.42</td><td>1.96</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>520.52</td><td>2.21</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>675.12</td><td>3.28</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1115.94</td><td>3.51</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>2348.14</td><td>1.86</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>560.44</td><td>4.13</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1491.90</td><td>2.98</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1150.52</td><td>3.54</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1387.62</td><td>3.48</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1678.96</td><td>4.38</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1634.54</td><td>5.59</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>767.52</td><td>5.87</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1915.98</td><td>4.50</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>590.82</td><td>7.98</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1630.80</td><td>0.75</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>461.32</td><td>2.39</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]</td><td>✅ 5/5</td><td>2019.18</td><td>1.46</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>468.06</td><td>1.22</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>417.80</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>374.30</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>411.96</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>370.04</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>668.16</td><td>0.16</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>314.30</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>411.04</td><td>0.34</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>398.16</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>404.84</td><td>0.05</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

