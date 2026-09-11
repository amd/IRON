# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (+3.33%)</td><td>0.05 (-3.41%)</td><td>0.05 (+1.19%)</td><td>0.04 (-13.07%)</td><td>0.01 <b>(+249.77%)</b></td><td>300.40 (+15.05%)</td><td>259.80 (+4.58%)</td><td>244.90 (-1.17%)</td><td>231.50 (-3.26%)</td><td>30.89 <b>(+288.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>261.10 (n/a)</td><td>248.42 (n/a)</td><td>247.80 (n/a)</td><td>239.30 (n/a)</td><td>7.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (+0.37%)</td><td>0.04 (+6.05%)</td><td>0.05 (-5.04%)</td><td>0.03 (+15.78%)</td><td>0.01 <b>(-30.93%)</b></td><td>395.70 (-13.62%)</td><td>287.72 (-10.24%)</td><td>260.20 (+5.30%)</td><td>230.30 (-0.39%)</td><td>65.92 <b>(-39.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>458.10 (n/a)</td><td>320.54 (n/a)</td><td>247.10 (n/a)</td><td>231.20 (n/a)</td><td>109.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (+19.30%)</td><td>0.04 (-5.06%)</td><td>0.04 (-1.83%)</td><td>0.02 <b>(-24.46%)</b></td><td>0.02 <b>(+77.01%)</b></td><td>617.50 <b>(+32.37%)</b></td><td>391.94 <b>(+20.32%)</b></td><td>339.40 (+1.86%)</td><td>198.70 (-16.20%)</td><td>185.80 <b>(+105.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>466.50 (n/a)</td><td>325.76 (n/a)</td><td>333.20 (n/a)</td><td>237.10 (n/a)</td><td>90.21 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-4.29%)</td><td>0.02 (-11.67%)</td><td>0.02 (-7.66%)</td><td>0.01 (+0.55%)</td><td>0.00 (-4.34%)</td><td>509.40 (-0.55%)</td><td>346.98 (+12.41%)</td><td>291.20 (+8.29%)</td><td>232.80 (+4.49%)</td><td>111.49 (-4.36%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.20 (n/a)</td><td>308.66 (n/a)</td><td>268.90 (n/a)</td><td>222.80 (n/a)</td><td>116.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-19.89%)</td><td>0.01 (+0.58%)</td><td>0.01 (+8.24%)</td><td>0.01 <b>(+398.79%)</b></td><td>0.00 <b>(-62.79%)</b></td><td>492.50 <b>(-79.95%)</b></td><td>402.60 <b>(-49.44%)</b></td><td>439.50 (-7.63%)</td><td>286.00 <b>(+24.84%)</b></td><td>91.38 <b>(-90.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2456.50 (n/a)</td><td>796.28 (n/a)</td><td>475.80 (n/a)</td><td>229.10 (n/a)</td><td>941.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (+6.96%)</td><td>0.02 (+9.05%)</td><td>0.02 (-2.31%)</td><td>0.01 (+8.75%)</td><td>0.00 (-15.38%)</td><td>459.00 (-8.03%)</td><td>295.46 (-10.93%)</td><td>270.10 (+2.35%)</td><td>225.30 (-6.51%)</td><td>93.58 <b>(-20.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>499.10 (n/a)</td><td>331.70 (n/a)</td><td>263.90 (n/a)</td><td>241.00 (n/a)</td><td>117.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 <b>(-30.04%)</b></td><td>0.01 <b>(-26.29%)</b></td><td>0.01 (-15.06%)</td><td>0.00 <b>(-79.15%)</b></td><td>0.01 (+9.68%)</td><td>2400.60 <b>(+379.64%)</b></td><td>1046.30 <b>(+181.51%)</b></td><td>441.80 (+17.72%)</td><td>232.70 <b>(+42.94%)</b></td><td>1031.46 <b>(+698.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>500.50 (n/a)</td><td>371.68 (n/a)</td><td>375.30 (n/a)</td><td>162.80 (n/a)</td><td>129.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-7.89%)</td><td>0.02 <b>(+41.75%)</b></td><td>0.02 <b>(+66.98%)</b></td><td>0.01 <b>(+286.23%)</b></td><td>0.01 <b>(-26.06%)</b></td><td>517.90 <b>(-74.11%)</b></td><td>366.58 <b>(-51.76%)</b></td><td>275.00 <b>(-40.11%)</b></td><td>263.50 (+8.57%)</td><td>135.53 <b>(-80.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2000.40 (n/a)</td><td>759.94 (n/a)</td><td>459.20 (n/a)</td><td>242.70 (n/a)</td><td>710.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-9.75%)</td><td>0.01 <b>(-31.38%)</b></td><td>0.01 (-11.87%)</td><td>0.00 <b>(-78.90%)</b></td><td>0.01 <b>(+88.10%)</b></td><td>2030.30 <b>(+373.93%)</b></td><td>764.40 <b>(+117.37%)</b></td><td>418.00 (+13.49%)</td><td>314.00 (+10.80%)</td><td>717.86 <b>(+1023.77%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>428.40 (n/a)</td><td>351.66 (n/a)</td><td>368.30 (n/a)</td><td>283.40 (n/a)</td><td>63.88 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>634.10 (n/a)</td><td>500.58 (n/a)</td><td>538.90 (n/a)</td><td>247.70 (n/a)</td><td>148.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>699.20 (n/a)</td><td>532.46 (n/a)</td><td>492.90 (n/a)</td><td>410.50 (n/a)</td><td>128.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>636.00 (n/a)</td><td>430.48 (n/a)</td><td>386.10 (n/a)</td><td>255.80 (n/a)</td><td>169.52 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.20 (n/a)</td><td>379.46 (n/a)</td><td>354.90 (n/a)</td><td>215.70 (n/a)</td><td>140.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>635.70 (n/a)</td><td>419.84 (n/a)</td><td>435.50 (n/a)</td><td>265.80 (n/a)</td><td>145.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>598.40 (n/a)</td><td>523.24 (n/a)</td><td>537.30 (n/a)</td><td>435.20 (n/a)</td><td>67.70 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/gemm</summary>


### test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]

_No metrics available._


### test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]

_No metrics available._


### test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.32 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>1127.20 (n/a)</td><td>692.34 (n/a)</td><td>699.60 (n/a)</td><td>346.40 (n/a)</td><td>284.31 (n/a)</td><td>96.86 (n/a)</td><td>56.00 (n/a)</td><td>47.96 (n/a)</td><td>29.77 (n/a)</td><td>25.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.63 (n/a)</td><td>1.24 (n/a)</td><td>1.35 (n/a)</td><td>0.90 (n/a)</td><td>0.33 (n/a)</td><td>731.10 (n/a)</td><td>559.44 (n/a)</td><td>486.70 (n/a)</td><td>402.80 (n/a)</td><td>155.71 (n/a)</td><td>166.62 (n/a)</td><td>127.39 (n/a)</td><td>137.87 (n/a)</td><td>91.80 (n/a)</td><td>33.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.51 (n/a)</td><td>1.14 (n/a)</td><td>1.22 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>1776.70 (n/a)</td><td>814.40 (n/a)</td><td>620.20 (n/a)</td><td>497.50 (n/a)</td><td>540.45 (n/a)</td><td>168.61 (n/a)</td><td>127.40 (n/a)</td><td>135.26 (n/a)</td><td>47.21 (n/a)</td><td>46.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.76 (n/a)</td><td>1.41 (n/a)</td><td>1.37 (n/a)</td><td>1.02 (n/a)</td><td>0.34 (n/a)</td><td>1029.80 (n/a)</td><td>781.18 (n/a)</td><td>767.60 (n/a)</td><td>594.40 (n/a)</td><td>193.60 (n/a)</td><td>225.81 (n/a)</td><td>180.48 (n/a)</td><td>174.86 (n/a)</td><td>130.33 (n/a)</td><td>44.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.32 (n/a)</td><td>1.81 (n/a)</td><td>1.74 (n/a)</td><td>1.25 (n/a)</td><td>0.42 (n/a)</td><td>836.80 (n/a)</td><td>607.42 (n/a)</td><td>603.00 (n/a)</td><td>452.80 (n/a)</td><td>149.96 (n/a)</td><td>296.44 (n/a)</td><td>231.29 (n/a)</td><td>222.58 (n/a)</td><td>160.39 (n/a)</td><td>53.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.40 (n/a)</td><td>1.45 (n/a)</td><td>1.30 (n/a)</td><td>0.91 (n/a)</td><td>0.57 (n/a)</td><td>1147.40 (n/a)</td><td>803.08 (n/a)</td><td>804.10 (n/a)</td><td>437.40 (n/a)</td><td>259.04 (n/a)</td><td>306.86 (n/a)</td><td>184.97 (n/a)</td><td>166.92 (n/a)</td><td>116.98 (n/a)</td><td>72.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.91 (n/a)</td><td>1.15 (n/a)</td><td>1.57 (n/a)</td><td>0.29 (n/a)</td><td>0.79 (n/a)</td><td>3662.90 (n/a)</td><td>1785.62 (n/a)</td><td>667.10 (n/a)</td><td>549.10 (n/a)</td><td>1606.62 (n/a)</td><td>244.44 (n/a)</td><td>147.11 (n/a)</td><td>201.18 (n/a)</td><td>36.64 (n/a)</td><td>100.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.66 (n/a)</td><td>0.77 (n/a)</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.51 (n/a)</td><td>890.00 (n/a)</td><td>592.38 (n/a)</td><td>612.70 (n/a)</td><td>216.90 (n/a)</td><td>249.93 (n/a)</td><td>77.36 (n/a)</td><td>35.78 (n/a)</td><td>27.38 (n/a)</td><td>18.85 (n/a)</td><td>23.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>3.97 (n/a)</td><td>3.28 (n/a)</td><td>3.58 (n/a)</td><td>2.43 (n/a)</td><td>0.71 (n/a)</td><td>1079.30 (n/a)</td><td>834.02 (n/a)</td><td>733.20 (n/a)</td><td>661.10 (n/a)</td><td>194.93 (n/a)</td><td>812.05 (n/a)</td><td>670.89 (n/a)</td><td>732.24 (n/a)</td><td>497.45 (n/a)</td><td>145.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_windowing[iter0]

_No metrics available._


### test_gemm_split_leg_windowing[iter1]

_No metrics available._


### test_gemm_split_leg_windowing[iter2]

_No metrics available._


### test_gemm_split_leg_windowing[iter3]

_No metrics available._


### test_gemm_split_leg_windowing[iter4]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter0]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter1]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter2]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter3]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter4]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>654.20 (n/a)</td><td>538.62 (n/a)</td><td>573.80 (n/a)</td><td>334.80 (n/a)</td><td>123.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.30 (n/a)</td><td>429.90 (n/a)</td><td>449.90 (n/a)</td><td>224.00 (n/a)</td><td>168.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.60 (n/a)</td><td>409.20 (n/a)</td><td>298.90 (n/a)</td><td>273.90 (n/a)</td><td>173.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1050.80 (n/a)</td><td>623.88 (n/a)</td><td>599.30 (n/a)</td><td>333.10 (n/a)</td><td>263.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.30 (n/a)</td><td>441.66 (n/a)</td><td>495.00 (n/a)</td><td>264.80 (n/a)</td><td>152.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>754.40 (n/a)</td><td>564.76 (n/a)</td><td>601.10 (n/a)</td><td>277.80 (n/a)</td><td>183.72 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.61 (-11.97%)</td><td>0.50 (+11.71%)</td><td>0.53 <b>(+34.06%)</b></td><td>0.33 <b>(+67.64%)</b></td><td>0.10 <b>(-47.13%)</b></td><td>671.40 <b>(-40.35%)</b></td><td>459.72 <b>(-22.74%)</b></td><td>418.60 <b>(-25.41%)</b></td><td>363.70 (+13.59%)</td><td>121.24 <b>(-62.11%)</b></td><td>25.95 (-11.97%)</td><td>21.45 (+11.71%)</td><td>22.54 <b>(+34.06%)</b></td><td>14.06 <b>(+67.64%)</b></td><td>4.43 <b>(-47.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.69 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>1125.60 (n/a)</td><td>595.02 (n/a)</td><td>561.20 (n/a)</td><td>320.20 (n/a)</td><td>319.93 (n/a)</td><td>29.48 (n/a)</td><td>19.20 (n/a)</td><td>16.82 (n/a)</td><td>8.38 (n/a)</td><td>8.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.57 (+1.79%)</td><td>0.44 (+10.11%)</td><td>0.43 <b>(+25.17%)</b></td><td>0.28 (-5.68%)</td><td>0.12 (+5.90%)</td><td>792.80 (+6.02%)</td><td>538.08 (-8.48%)</td><td>512.00 <b>(-20.10%)</b></td><td>387.70 (-1.77%)</td><td>165.25 (+8.17%)</td><td>24.34 (+1.79%)</td><td>18.78 (+10.11%)</td><td>18.43 <b>(+25.17%)</b></td><td>11.90 (-5.68%)</td><td>5.19 (+5.90%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>747.80 (n/a)</td><td>587.94 (n/a)</td><td>640.80 (n/a)</td><td>394.70 (n/a)</td><td>152.77 (n/a)</td><td>23.91 (n/a)</td><td>17.06 (n/a)</td><td>14.73 (n/a)</td><td>12.62 (n/a)</td><td>4.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.31 (+0.86%)</td><td>0.31 (+2.34%)</td><td>0.31 (+2.11%)</td><td>0.30 (+3.16%)</td><td>0.01 <b>(-28.03%)</b></td><td>84511.80 (-3.06%)</td><td>81970.98 (-2.31%)</td><td>81492.10 (-2.07%)</td><td>80996.00 (-0.86%)</td><td>1466.14 <b>(-30.90%)</b></td><td>212.11 (+0.86%)</td><td>209.64 (+2.34%)</td><td>210.82 (+2.11%)</td><td>203.28 (+3.16%)</td><td>3.67 <b>(-28.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87179.40 (n/a)</td><td>83910.20 (n/a)</td><td>83210.90 (n/a)</td><td>81696.00 (n/a)</td><td>2121.70 (n/a)</td><td>210.29 (n/a)</td><td>204.84 (n/a)</td><td>206.46 (n/a)</td><td>197.06 (n/a)</td><td>5.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.17 (+13.34%)</td><td>1.14 (+18.33%)</td><td>1.15 (+13.34%)</td><td>1.11 <b>(+41.48%)</b></td><td>0.03 <b>(-73.56%)</b></td><td>22719.90 <b>(-29.32%)</b></td><td>22098.94 (-16.34%)</td><td>21945.10 (-11.77%)</td><td>21422.00 (-11.77%)</td><td>529.69 <b>(-83.73%)</b></td><td>801.97 (+13.34%)</td><td>777.76 (+18.33%)</td><td>782.86 (+13.34%)</td><td>756.16 <b>(+41.48%)</b></td><td>18.65 <b>(-73.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>1.04 (n/a)</td><td>0.96 (n/a)</td><td>1.01 (n/a)</td><td>0.78 (n/a)</td><td>0.10 (n/a)</td><td>32143.60 (n/a)</td><td>26415.86 (n/a)</td><td>24872.70 (n/a)</td><td>24279.30 (n/a)</td><td>3256.15 (n/a)</td><td>707.59 (n/a)</td><td>657.31 (n/a)</td><td>690.71 (n/a)</td><td>534.47 (n/a)</td><td>70.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>4.07 (+16.15%)</td><td>3.32 (+11.75%)</td><td>3.81 (+16.61%)</td><td>1.74 (+16.96%)</td><td>0.99 (+17.51%)</td><td>4640.30 (-14.50%)</td><td>2695.82 (-10.79%)</td><td>2113.20 (-14.24%)</td><td>1979.70 (-13.90%)</td><td>1129.34 (-16.32%)</td><td>1067.78 (+16.15%)</td><td>869.50 (+11.75%)</td><td>1000.35 (+16.61%)</td><td>455.56 (+16.96%)</td><td>259.69 (+17.51%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.51 (n/a)</td><td>2.97 (n/a)</td><td>3.27 (n/a)</td><td>1.49 (n/a)</td><td>0.84 (n/a)</td><td>5427.40 (n/a)</td><td>3021.88 (n/a)</td><td>2464.10 (n/a)</td><td>2299.40 (n/a)</td><td>1349.56 (n/a)</td><td>919.32 (n/a)</td><td>778.11 (n/a)</td><td>857.89 (n/a)</td><td>389.50 (n/a)</td><td>221.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.26 <b>(+31.25%)</b></td><td>0.21 (+15.51%)</td><td>0.21 (+14.93%)</td><td>0.17 (+3.47%)</td><td>0.03 <b>(+168.86%)</b></td><td>7252.00 (-3.35%)</td><td>6030.58 (-12.20%)</td><td>5891.00 (-12.99%)</td><td>4826.80 <b>(-23.81%)</b></td><td>878.83 <b>(+95.99%)</b></td><td>13.90 <b>(+31.25%)</b></td><td>11.32 (+15.51%)</td><td>11.39 (+14.93%)</td><td>9.25 (+3.47%)</td><td>1.70 <b>(+168.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>7503.70 (n/a)</td><td>6868.82 (n/a)</td><td>6770.30 (n/a)</td><td>6335.30 (n/a)</td><td>448.40 (n/a)</td><td>10.59 (n/a)</td><td>9.80 (n/a)</td><td>9.91 (n/a)</td><td>8.94 (n/a)</td><td>0.63 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemv</summary>


### test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>3.81 (n/a)</td><td>3.57 (n/a)</td><td>3.56 (n/a)</td><td>3.39 (n/a)</td><td>0.18 (n/a)</td><td>3.81 (n/a)</td><td>3.57 (n/a)</td><td>3.56 (n/a)</td><td>3.39 (n/a)</td><td>0.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>7.64 (+6.91%)</td><td>6.55 (+1.02%)</td><td>6.22 (-2.41%)</td><td>5.67 (-5.56%)</td><td>0.95 <b>(+84.83%)</b></td><td>7.63 (+6.91%)</td><td>6.54 (+1.02%)</td><td>6.21 (-2.41%)</td><td>5.66 (-5.56%)</td><td>0.95 <b>(+84.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>7.15 (n/a)</td><td>6.48 (n/a)</td><td>6.37 (n/a)</td><td>6.00 (n/a)</td><td>0.52 (n/a)</td><td>7.14 (n/a)</td><td>6.48 (n/a)</td><td>6.37 (n/a)</td><td>6.00 (n/a)</td><td>0.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>13.29 (+4.45%)</td><td>11.32 <b>(+20.83%)</b></td><td>12.35 <b>(+28.78%)</b></td><td>8.42 (+15.86%)</td><td>2.00 (-10.00%)</td><td>13.29 (+4.45%)</td><td>11.31 <b>(+20.83%)</b></td><td>12.35 <b>(+28.78%)</b></td><td>8.41 (+15.86%)</td><td>2.00 (-10.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>12.73 (n/a)</td><td>9.37 (n/a)</td><td>9.59 (n/a)</td><td>7.26 (n/a)</td><td>2.23 (n/a)</td><td>12.72 (n/a)</td><td>9.36 (n/a)</td><td>9.59 (n/a)</td><td>7.26 (n/a)</td><td>2.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>3.95 (n/a)</td><td>3.64 (n/a)</td><td>3.68 (n/a)</td><td>3.40 (n/a)</td><td>0.23 (n/a)</td><td>3.95 (n/a)</td><td>3.64 (n/a)</td><td>3.67 (n/a)</td><td>3.39 (n/a)</td><td>0.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>7.45 (+6.65%)</td><td>6.55 (+0.87%)</td><td>7.23 (+7.43%)</td><td>4.99 (-15.55%)</td><td>1.14 <b>(+121.99%)</b></td><td>7.44 (+6.65%)</td><td>6.54 (+0.87%)</td><td>7.22 (+7.43%)</td><td>4.98 (-15.55%)</td><td>1.14 <b>(+121.99%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>6.98 (n/a)</td><td>6.49 (n/a)</td><td>6.73 (n/a)</td><td>5.91 (n/a)</td><td>0.52 (n/a)</td><td>6.98 (n/a)</td><td>6.49 (n/a)</td><td>6.72 (n/a)</td><td>5.90 (n/a)</td><td>0.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>14.02 (+1.34%)</td><td>11.05 (+16.76%)</td><td>9.72 (+13.04%)</td><td>8.22 (+10.94%)</td><td>2.70 (+1.15%)</td><td>14.01 (+1.34%)</td><td>11.04 (+16.76%)</td><td>9.72 (+13.04%)</td><td>8.22 (+10.94%)</td><td>2.70 (+1.15%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>13.83 (n/a)</td><td>9.46 (n/a)</td><td>8.60 (n/a)</td><td>7.41 (n/a)</td><td>2.67 (n/a)</td><td>13.83 (n/a)</td><td>9.46 (n/a)</td><td>8.60 (n/a)</td><td>7.41 (n/a)</td><td>2.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.88 (-4.51%)</td><td>2.09 (-10.05%)</td><td>2.34 (-15.06%)</td><td>1.17 (-3.60%)</td><td>0.83 (-1.15%)</td><td>2.88 (-4.51%)</td><td>2.09 (-10.05%)</td><td>2.33 (-15.06%)</td><td>1.17 (-3.60%)</td><td>0.82 (-1.15%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.02 (n/a)</td><td>2.32 (n/a)</td><td>2.75 (n/a)</td><td>1.22 (n/a)</td><td>0.83 (n/a)</td><td>3.01 (n/a)</td><td>2.32 (n/a)</td><td>2.75 (n/a)</td><td>1.21 (n/a)</td><td>0.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.55 (+2.66%)</td><td>0.36 <b>(+26.84%)</b></td><td>0.32 (-11.95%)</td><td>0.12 <b>(+64.82%)</b></td><td>0.17 (-15.85%)</td><td>0.54 (+2.66%)</td><td>0.36 <b>(+26.84%)</b></td><td>0.32 (-11.95%)</td><td>0.12 <b>(+64.82%)</b></td><td>0.17 (-15.85%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.54 (n/a)</td><td>0.29 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.53 (n/a)</td><td>0.28 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.66 (-11.30%)</td><td>0.35 (-17.80%)</td><td>0.35 (-3.99%)</td><td>0.08 (-0.04%)</td><td>0.27 (+1.82%)</td><td>0.65 (-11.30%)</td><td>0.34 (-17.80%)</td><td>0.34 (-3.99%)</td><td>0.08 (-0.04%)</td><td>0.27 (+1.82%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.74 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.73 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>0.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.27 (-10.00%)</td><td>1.39 (-10.16%)</td><td>1.72 <b>(+26.52%)</b></td><td>0.44 <b>(-37.04%)</b></td><td>0.76 (+1.53%)</td><td>2.23 (-10.00%)</td><td>1.37 (-10.16%)</td><td>1.69 <b>(+26.52%)</b></td><td>0.44 <b>(-37.04%)</b></td><td>0.75 (+1.53%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.52 (n/a)</td><td>1.55 (n/a)</td><td>1.36 (n/a)</td><td>0.70 (n/a)</td><td>0.75 (n/a)</td><td>2.48 (n/a)</td><td>1.52 (n/a)</td><td>1.33 (n/a)</td><td>0.69 (n/a)</td><td>0.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

_No metrics available._


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

_No metrics available._


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

_No metrics available._


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>301.40 (n/a)</td><td>274.18 (n/a)</td><td>272.60 (n/a)</td><td>247.50 (n/a)</td><td>20.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.20 (n/a)</td><td>513.42 (n/a)</td><td>492.90 (n/a)</td><td>434.60 (n/a)</td><td>74.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.70 (n/a)</td><td>410.82 (n/a)</td><td>405.90 (n/a)</td><td>220.50 (n/a)</td><td>182.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1962.60 (n/a)</td><td>712.36 (n/a)</td><td>522.30 (n/a)</td><td>179.60 (n/a)</td><td>724.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>481.50 (n/a)</td><td>362.46 (n/a)</td><td>462.30 (n/a)</td><td>143.50 (n/a)</td><td>153.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.70 (n/a)</td><td>435.30 (n/a)</td><td>477.70 (n/a)</td><td>280.30 (n/a)</td><td>125.03 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-15.52%)</td><td>0.02 <b>(-36.65%)</b></td><td>0.02 <b>(-29.20%)</b></td><td>0.00 <b>(-74.44%)</b></td><td>0.01 <b>(+65.32%)</b></td><td>1946.60 <b>(+291.20%)</b></td><td>952.32 <b>(+196.89%)</b></td><td>383.40 <b>(+41.22%)</b></td><td>278.60 (+18.35%)</td><td>868.60 <b>(+705.99%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.60 (n/a)</td><td>320.76 (n/a)</td><td>271.50 (n/a)</td><td>235.40 (n/a)</td><td>107.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-13.53%)</td><td>0.02 <b>(-29.77%)</b></td><td>0.02 <b>(-37.50%)</b></td><td>0.00 <b>(-71.56%)</b></td><td>0.01 (+19.15%)</td><td>1736.30 <b>(+251.62%)</b></td><td>677.42 <b>(+93.46%)</b></td><td>443.60 <b>(+60.03%)</b></td><td>295.40 (+15.66%)</td><td>600.66 <b>(+422.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.80 (n/a)</td><td>350.16 (n/a)</td><td>277.20 (n/a)</td><td>255.40 (n/a)</td><td>114.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-11.79%)</td><td>0.02 (-4.42%)</td><td>0.02 (+13.22%)</td><td>0.01 <b>(-20.75%)</b></td><td>0.01 (-4.89%)</td><td>573.70 <b>(+26.17%)</b></td><td>379.30 (+6.29%)</td><td>349.30 (-11.68%)</td><td>260.60 (+13.35%)</td><td>131.22 <b>(+30.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.70 (n/a)</td><td>356.84 (n/a)</td><td>395.50 (n/a)</td><td>229.90 (n/a)</td><td>100.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-12.15%)</td><td>0.03 (-6.53%)</td><td>0.03 (-3.14%)</td><td>0.02 (-10.60%)</td><td>0.00 <b>(-29.08%)</b></td><td>456.80 (+11.85%)</td><td>323.76 (+5.21%)</td><td>299.30 (+3.24%)</td><td>262.10 (+13.86%)</td><td>76.53 (-4.20%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>408.40 (n/a)</td><td>307.72 (n/a)</td><td>289.90 (n/a)</td><td>230.20 (n/a)</td><td>79.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-9.94%)</td><td>0.02 <b>(-27.25%)</b></td><td>0.02 <b>(-44.70%)</b></td><td>0.01 <b>(-25.40%)</b></td><td>0.01 <b>(+27.35%)</b></td><td>566.10 <b>(+34.05%)</b></td><td>430.44 <b>(+43.48%)</b></td><td>489.70 <b>(+80.83%)</b></td><td>283.60 (+11.04%)</td><td>125.72 <b>(+80.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.30 (n/a)</td><td>300.00 (n/a)</td><td>270.80 (n/a)</td><td>255.40 (n/a)</td><td>69.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 <b>(-59.06%)</b></td><td>0.01 <b>(-53.03%)</b></td><td>0.01 <b>(-53.88%)</b></td><td>0.01 <b>(-57.47%)</b></td><td>0.00 <b>(-61.99%)</b></td><td>1003.70 <b>(+135.17%)</b></td><td>709.44 <b>(+109.89%)</b></td><td>750.40 <b>(+116.82%)</b></td><td>474.50 <b>(+144.34%)</b></td><td>204.88 <b>(+115.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>426.80 (n/a)</td><td>338.00 (n/a)</td><td>346.10 (n/a)</td><td>194.20 (n/a)</td><td>94.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-2.68%)</td><td>0.02 (+2.54%)</td><td>0.02 (+14.62%)</td><td>0.02 (+7.18%)</td><td>0.01 (-14.79%)</td><td>525.40 (-6.71%)</td><td>403.70 (-5.95%)</td><td>452.90 (-12.75%)</td><td>251.80 (+2.73%)</td><td>120.31 (-19.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.20 (n/a)</td><td>429.22 (n/a)</td><td>519.10 (n/a)</td><td>245.10 (n/a)</td><td>149.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (+0.29%)</td><td>0.02 (-10.02%)</td><td>0.02 (+15.18%)</td><td>0.01 <b>(-35.97%)</b></td><td>0.01 (+3.94%)</td><td>963.10 <b>(+56.17%)</b></td><td>542.94 (+18.87%)</td><td>461.90 (-13.18%)</td><td>292.40 (-0.27%)</td><td>265.36 <b>(+75.15%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.70 (n/a)</td><td>456.74 (n/a)</td><td>532.00 (n/a)</td><td>293.20 (n/a)</td><td>151.51 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (+7.19%)</td><td>0.03 (+13.82%)</td><td>0.03 (+11.27%)</td><td>0.02 <b>(+295.41%)</b></td><td>0.01 <b>(-27.17%)</b></td><td>528.20 <b>(-74.71%)</b></td><td>346.96 <b>(-47.63%)</b></td><td>272.00 (-10.14%)</td><td>231.30 (-6.73%)</td><td>127.37 <b>(-84.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2088.70 (n/a)</td><td>662.56 (n/a)</td><td>302.70 (n/a)</td><td>248.00 (n/a)</td><td>799.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-7.48%)</td><td>0.02 (+2.72%)</td><td>0.03 (+14.53%)</td><td>0.01 (+3.65%)</td><td>0.01 (-5.46%)</td><td>558.40 (-3.52%)</td><td>386.96 (-3.80%)</td><td>288.60 (-12.68%)</td><td>284.50 (+8.09%)</td><td>137.60 (-7.61%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.80 (n/a)</td><td>402.24 (n/a)</td><td>330.50 (n/a)</td><td>263.20 (n/a)</td><td>148.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (+13.03%)</td><td>0.02 (+19.32%)</td><td>0.02 (+13.39%)</td><td>0.01 <b>(+310.88%)</b></td><td>0.01 (-18.88%)</td><td>591.50 <b>(-75.66%)</b></td><td>412.32 <b>(-48.47%)</b></td><td>386.40 (-11.82%)</td><td>250.80 (-11.53%)</td><td>158.79 <b>(-82.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2430.40 (n/a)</td><td>800.12 (n/a)</td><td>438.20 (n/a)</td><td>283.50 (n/a)</td><td>918.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (+0.09%)</td><td>0.03 (+18.45%)</td><td>0.03 <b>(+84.18%)</b></td><td>0.01 (+5.61%)</td><td>0.01 (-5.42%)</td><td>569.70 (-5.32%)</td><td>361.22 (-17.76%)</td><td>279.90 <b>(-45.70%)</b></td><td>238.40 (-0.13%)</td><td>153.06 (-12.54%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.70 (n/a)</td><td>439.22 (n/a)</td><td>515.50 (n/a)</td><td>238.70 (n/a)</td><td>175.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (+6.61%)</td><td>0.02 (+14.25%)</td><td>0.02 (+2.22%)</td><td>0.01 (-9.05%)</td><td>0.01 <b>(+34.25%)</b></td><td>568.80 (+9.96%)</td><td>391.08 (-7.47%)</td><td>443.70 (-2.18%)</td><td>230.60 (-6.18%)</td><td>145.27 <b>(+38.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.30 (n/a)</td><td>422.64 (n/a)</td><td>453.60 (n/a)</td><td>245.80 (n/a)</td><td>105.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 <b>(-24.56%)</b></td><td>0.02 (-14.17%)</td><td>0.02 (-0.31%)</td><td>0.01 (-16.61%)</td><td>0.00 <b>(-30.46%)</b></td><td>659.20 (+19.90%)</td><td>506.40 (+15.62%)</td><td>468.60 (+0.32%)</td><td>427.40 <b>(+32.57%)</b></td><td>97.74 (+10.84%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.80 (n/a)</td><td>437.98 (n/a)</td><td>467.10 (n/a)</td><td>322.40 (n/a)</td><td>88.18 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.10 (-9.45%)</td><td>0.07 (-11.84%)</td><td>0.09 (+0.47%)</td><td>0.04 (+2.67%)</td><td>0.03 (+1.99%)</td><td>576.00 (-2.62%)</td><td>374.12 (+14.10%)</td><td>274.80 (-0.47%)</td><td>258.30 (+10.43%)</td><td>152.59 (+1.98%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>591.50 (n/a)</td><td>327.88 (n/a)</td><td>276.10 (n/a)</td><td>233.90 (n/a)</td><td>149.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.23 <b>(+39.89%)</b></td><td>0.14 (+2.17%)</td><td>0.14 (+1.53%)</td><td>0.08 (+1.38%)</td><td>0.06 <b>(+85.04%)</b></td><td>489.60 (-1.37%)</td><td>338.50 (+6.98%)</td><td>284.70 (-1.49%)</td><td>178.00 <b>(-28.51%)</b></td><td>143.13 <b>(+39.28%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>496.40 (n/a)</td><td>316.42 (n/a)</td><td>289.00 (n/a)</td><td>249.00 (n/a)</td><td>102.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-11.04%)</td><td>0.01 <b>(-20.30%)</b></td><td>0.02 <b>(+22.81%)</b></td><td>0.00 <b>(-70.24%)</b></td><td>0.01 <b>(+47.77%)</b></td><td>1838.50 <b>(+236.04%)</b></td><td>898.22 <b>(+139.28%)</b></td><td>292.00 (-18.57%)</td><td>256.90 (+12.43%)</td><td>851.53 <b>(+498.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.10 (n/a)</td><td>375.38 (n/a)</td><td>358.60 (n/a)</td><td>228.50 (n/a)</td><td>142.36 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 <b>(-22.34%)</b></td><td>0.02 (-10.52%)</td><td>0.02 (-14.38%)</td><td>0.00 <b>(-71.51%)</b></td><td>0.01 (-5.34%)</td><td>2366.70 <b>(+250.99%)</b></td><td>731.30 <b>(+73.36%)</b></td><td>337.90 (+16.80%)</td><td>251.60 <b>(+28.76%)</b></td><td>917.63 <b>(+296.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.30 (n/a)</td><td>421.84 (n/a)</td><td>289.30 (n/a)</td><td>195.40 (n/a)</td><td>231.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (+0.99%)</td><td>0.04 (-16.25%)</td><td>0.04 (+0.20%)</td><td>0.02 <b>(-35.02%)</b></td><td>0.02 <b>(+50.06%)</b></td><td>634.90 <b>(+53.92%)</b></td><td>403.02 <b>(+34.28%)</b></td><td>310.70 (-0.19%)</td><td>217.90 (-0.95%)</td><td>184.63 <b>(+145.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>412.50 (n/a)</td><td>300.14 (n/a)</td><td>311.30 (n/a)</td><td>220.00 (n/a)</td><td>75.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-6.67%)</td><td>0.02 (-10.08%)</td><td>0.02 (-2.97%)</td><td>0.01 (+2.65%)</td><td>0.01 <b>(-26.17%)</b></td><td>592.60 (-2.58%)</td><td>477.90 (+5.13%)</td><td>543.60 (+3.07%)</td><td>280.00 (+7.16%)</td><td>133.63 <b>(-21.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>454.58 (n/a)</td><td>527.40 (n/a)</td><td>261.30 (n/a)</td><td>170.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 <b>(+41.13%)</b></td><td>0.03 (+16.73%)</td><td>0.02 (-8.99%)</td><td>0.02 <b>(+38.41%)</b></td><td>0.02 <b>(+64.73%)</b></td><td>656.10 <b>(-27.75%)</b></td><td>451.32 (-7.05%)</td><td>504.80 (+9.86%)</td><td>173.60 <b>(-29.14%)</b></td><td>220.51 (-13.36%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>908.10 (n/a)</td><td>485.54 (n/a)</td><td>459.50 (n/a)</td><td>245.00 (n/a)</td><td>254.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (+4.21%)</td><td>0.02 <b>(+27.68%)</b></td><td>0.03 <b>(+60.64%)</b></td><td>0.02 <b>(+20.86%)</b></td><td>0.01 (-0.07%)</td><td>537.30 (-17.26%)</td><td>360.72 <b>(-22.52%)</b></td><td>298.40 <b>(-37.76%)</b></td><td>266.20 (-4.04%)</td><td>111.94 (-16.62%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.40 (n/a)</td><td>465.54 (n/a)</td><td>479.40 (n/a)</td><td>277.40 (n/a)</td><td>134.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 <b>(+25.51%)</b></td><td>0.02 (+4.07%)</td><td>0.02 (+4.40%)</td><td>0.02 (+7.95%)</td><td>0.01 <b>(+26.41%)</b></td><td>542.00 (-7.37%)</td><td>454.24 (-2.71%)</td><td>530.20 (-4.21%)</td><td>237.80 <b>(-20.34%)</b></td><td>130.96 (-7.73%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.10 (n/a)</td><td>466.88 (n/a)</td><td>553.50 (n/a)</td><td>298.50 (n/a)</td><td>141.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (+10.31%)</td><td>0.03 (+5.18%)</td><td>0.03 (+8.62%)</td><td>0.01 <b>(-66.79%)</b></td><td>0.01 <b>(+72.06%)</b></td><td>1571.90 <b>(+201.13%)</b></td><td>527.74 <b>(+47.13%)</b></td><td>275.70 (-7.95%)</td><td>232.00 (-9.38%)</td><td>584.29 <b>(+413.19%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.00 (n/a)</td><td>358.70 (n/a)</td><td>299.50 (n/a)</td><td>256.00 (n/a)</td><td>113.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 <b>(-28.40%)</b></td><td>0.03 (+12.46%)</td><td>0.03 <b>(+55.16%)</b></td><td>0.02 (+16.61%)</td><td>0.01 <b>(-44.86%)</b></td><td>505.10 (-14.24%)</td><td>370.34 (-19.67%)</td><td>316.30 <b>(-35.55%)</b></td><td>266.80 <b>(+39.69%)</b></td><td>114.15 <b>(-29.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.00 (n/a)</td><td>461.04 (n/a)</td><td>490.80 (n/a)</td><td>191.00 (n/a)</td><td>162.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (-5.27%)</td><td>0.02 (+1.77%)</td><td>0.03 (+12.14%)</td><td>0.01 (-12.20%)</td><td>0.01 (-0.29%)</td><td>662.10 (+13.90%)</td><td>386.32 (-0.10%)</td><td>301.00 (-10.81%)</td><td>279.30 (+5.56%)</td><td>162.74 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>386.70 (n/a)</td><td>337.50 (n/a)</td><td>264.60 (n/a)</td><td>135.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 <b>(-47.07%)</b></td><td>0.02 <b>(-39.32%)</b></td><td>0.02 (-15.42%)</td><td>0.00 <b>(-68.47%)</b></td><td>0.01 <b>(-45.52%)</b></td><td>1875.80 <b>(+217.13%)</b></td><td>726.38 <b>(+96.50%)</b></td><td>485.90 (+18.22%)</td><td>307.40 <b>(+88.94%)</b></td><td>647.18 <b>(+292.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>591.50 (n/a)</td><td>369.66 (n/a)</td><td>411.00 (n/a)</td><td>162.70 (n/a)</td><td>165.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (+0.12%)</td><td>0.02 (+1.32%)</td><td>0.02 (+5.58%)</td><td>0.01 (+17.97%)</td><td>0.01 (-13.98%)</td><td>665.10 (-15.24%)</td><td>486.42 (-6.34%)</td><td>472.00 (-5.28%)</td><td>279.30 (-0.14%)</td><td>143.07 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>784.70 (n/a)</td><td>519.36 (n/a)</td><td>498.30 (n/a)</td><td>279.70 (n/a)</td><td>205.30 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.40 (+8.29%)</td><td>0.29 (+9.37%)</td><td>0.33 <b>(+48.87%)</b></td><td>0.16 (-16.65%)</td><td>0.10 (+19.26%)</td><td>601.90 (+19.97%)</td><td>376.92 (-4.92%)</td><td>294.20 <b>(-32.83%)</b></td><td>246.00 (-7.66%)</td><td>150.35 <b>(+33.64%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>501.70 (n/a)</td><td>396.42 (n/a)</td><td>438.00 (n/a)</td><td>266.40 (n/a)</td><td>112.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.34 (+1.52%)</td><td>0.25 (+15.39%)</td><td>0.25 <b>(+22.01%)</b></td><td>0.17 (+1.72%)</td><td>0.08 <b>(+20.05%)</b></td><td>579.90 (-1.70%)</td><td>425.14 (-11.11%)</td><td>393.60 (-18.05%)</td><td>290.60 (-1.49%)</td><td>140.51 (+17.26%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>589.90 (n/a)</td><td>478.28 (n/a)</td><td>480.30 (n/a)</td><td>295.00 (n/a)</td><td>119.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.39 <b>(+22.30%)</b></td><td>0.25 (+7.94%)</td><td>0.21 (-14.71%)</td><td>0.16 (-5.17%)</td><td>0.11 <b>(+73.44%)</b></td><td>611.60 (+5.45%)</td><td>444.46 (+0.60%)</td><td>466.60 (+17.24%)</td><td>249.60 (-18.24%)</td><td>172.06 <b>(+48.01%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>580.00 (n/a)</td><td>441.82 (n/a)</td><td>398.00 (n/a)</td><td>305.30 (n/a)</td><td>116.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.17 <b>(-38.72%)</b></td><td>0.16 (-12.45%)</td><td>0.16 (-1.31%)</td><td>0.14 <b>(+25.88%)</b></td><td>0.01 <b>(-76.62%)</b></td><td>523.70 <b>(-20.56%)</b></td><td>471.82 (+5.19%)</td><td>456.90 (+1.33%)</td><td>427.10 <b>(+63.20%)</b></td><td>45.17 <b>(-68.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>659.20 (n/a)</td><td>448.52 (n/a)</td><td>450.90 (n/a)</td><td>261.70 (n/a)</td><td>144.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.37 (+19.43%)</td><td>0.19 (+13.28%)</td><td>0.15 (+2.32%)</td><td>0.12 <b>(+295.56%)</b></td><td>0.11 (-1.97%)</td><td>632.50 <b>(-74.72%)</b></td><td>461.64 <b>(-44.99%)</b></td><td>482.60 (-2.27%)</td><td>197.00 (-16.28%)</td><td>160.42 <b>(-82.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.11 (n/a)</td><td>2502.10 (n/a)</td><td>839.18 (n/a)</td><td>493.80 (n/a)</td><td>235.30 (n/a)</td><td>941.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.31 (+9.65%)</td><td>0.20 <b>(+24.47%)</b></td><td>0.16 (+9.47%)</td><td>0.15 <b>(+320.14%)</b></td><td>0.07 <b>(-33.43%)</b></td><td>482.70 <b>(-76.20%)</b></td><td>391.78 <b>(-48.35%)</b></td><td>456.50 (-8.65%)</td><td>240.70 (-8.79%)</td><td>106.97 <b>(-85.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>2027.90 (n/a)</td><td>758.52 (n/a)</td><td>499.70 (n/a)</td><td>263.90 (n/a)</td><td>730.74 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/softmax</summary>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.42 (-5.11%)</td><td>0.31 (+6.46%)</td><td>0.24 (+2.70%)</td><td>0.23 <b>(+28.32%)</b></td><td>0.10 (-19.67%)</td><td>558.40 <b>(-22.07%)</b></td><td>453.70 (-11.68%)</td><td>540.80 (-2.63%)</td><td>310.60 (+5.40%)</td><td>130.19 <b>(-34.05%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>716.50 (n/a)</td><td>513.68 (n/a)</td><td>555.40 (n/a)</td><td>294.70 (n/a)</td><td>197.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.48 (-11.52%)</td><td>0.30 (+5.70%)</td><td>0.27 (-6.31%)</td><td>0.06 (+18.50%)</td><td>0.16 (-7.60%)</td><td>2046.50 (-15.61%)</td><td>726.08 (-12.41%)</td><td>479.60 (+6.74%)</td><td>271.80 (+13.01%)</td><td>745.88 (-17.23%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.55 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>0.18 (n/a)</td><td>2425.00 (n/a)</td><td>828.96 (n/a)</td><td>449.30 (n/a)</td><td>240.50 (n/a)</td><td>901.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.48 (+0.53%)</td><td>0.34 (-2.19%)</td><td>0.31 (-2.41%)</td><td>0.24 (+12.85%)</td><td>0.11 (-3.65%)</td><td>541.80 (-11.38%)</td><td>410.62 (+1.11%)</td><td>424.80 (+2.46%)</td><td>274.80 (-0.51%)</td><td>119.43 (-12.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>611.40 (n/a)</td><td>406.12 (n/a)</td><td>414.60 (n/a)</td><td>276.20 (n/a)</td><td>135.72 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.01 <b>(-25.31%)</b></td><td>0.01 <b>(-34.98%)</b></td><td>0.01 <b>(-35.45%)</b></td><td>0.01 <b>(-43.14%)</b></td><td>0.00 <b>(+26.03%)</b></td><td>549.20 <b>(+75.86%)</b></td><td>428.78 <b>(+60.56%)</b></td><td>397.80 <b>(+54.91%)</b></td><td>295.70 <b>(+33.86%)</b></td><td>114.58 <b>(+209.76%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>312.30 (n/a)</td><td>267.06 (n/a)</td><td>256.80 (n/a)</td><td>220.90 (n/a)</td><td>36.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-1.63%)</td><td>0.01 (+10.51%)</td><td>0.01 <b>(+23.46%)</b></td><td>0.01 (+7.59%)</td><td>0.00 (-4.44%)</td><td>455.40 (-7.04%)</td><td>339.28 (-10.15%)</td><td>296.50 (-18.99%)</td><td>271.70 (+1.65%)</td><td>81.06 (-11.75%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.90 (n/a)</td><td>377.60 (n/a)</td><td>366.00 (n/a)</td><td>267.30 (n/a)</td><td>91.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.01 <b>(-31.06%)</b></td><td>0.01 <b>(-25.26%)</b></td><td>0.01 <b>(-39.98%)</b></td><td>0.01 (+8.98%)</td><td>0.00 <b>(-70.97%)</b></td><td>491.00 (-8.24%)</td><td>422.20 (+18.28%)</td><td>423.40 <b>(+66.63%)</b></td><td>338.10 <b>(+45.05%)</b></td><td>57.68 <b>(-62.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.10 (n/a)</td><td>356.96 (n/a)</td><td>254.10 (n/a)</td><td>233.10 (n/a)</td><td>154.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.64 (-1.77%)</td><td>0.38 (-14.27%)</td><td>0.33 <b>(-35.82%)</b></td><td>0.25 (+15.40%)</td><td>0.16 (-6.10%)</td><td>534.80 (-13.34%)</td><td>391.02 (+12.97%)</td><td>401.10 <b>(+55.83%)</b></td><td>207.80 (+1.81%)</td><td>137.72 (-17.88%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.65 (n/a)</td><td>0.45 (n/a)</td><td>0.51 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>617.10 (n/a)</td><td>346.14 (n/a)</td><td>257.40 (n/a)</td><td>204.10 (n/a)</td><td>167.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.60 (+10.37%)</td><td>0.43 (-11.84%)</td><td>0.43 (-13.69%)</td><td>0.22 <b>(-48.00%)</b></td><td>0.16 <b>(+201.24%)</b></td><td>604.90 <b>(+92.34%)</b></td><td>347.96 <b>(+28.52%)</b></td><td>306.40 (+15.84%)</td><td>218.60 (-9.41%)</td><td>156.93 <b>(+422.09%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.55 (n/a)</td><td>0.49 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.05 (n/a)</td><td>314.50 (n/a)</td><td>270.74 (n/a)</td><td>264.50 (n/a)</td><td>241.30 (n/a)</td><td>30.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.43 (-15.00%)</td><td>0.30 (-15.28%)</td><td>0.31 (-14.15%)</td><td>0.21 (-5.20%)</td><td>0.08 <b>(-28.12%)</b></td><td>617.90 (+5.48%)</td><td>459.78 (+14.48%)</td><td>428.70 (+16.49%)</td><td>308.30 (+17.67%)</td><td>118.96 (-11.11%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>585.80 (n/a)</td><td>401.64 (n/a)</td><td>368.00 (n/a)</td><td>262.00 (n/a)</td><td>133.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.54 <b>(-24.91%)</b></td><td>0.36 <b>(-28.70%)</b></td><td>0.30 <b>(-41.69%)</b></td><td>0.24 (-11.13%)</td><td>0.13 <b>(-25.31%)</b></td><td>556.50 (+12.54%)</td><td>408.88 <b>(+37.73%)</b></td><td>444.60 <b>(+71.53%)</b></td><td>245.90 <b>(+33.13%)</b></td><td>133.63 (+8.97%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.72 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>494.50 (n/a)</td><td>296.86 (n/a)</td><td>259.20 (n/a)</td><td>184.70 (n/a)</td><td>122.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.49 <b>(-35.23%)</b></td><td>0.34 (-17.86%)</td><td>0.31 (-4.54%)</td><td>0.23 (+14.89%)</td><td>0.10 <b>(-55.75%)</b></td><td>583.10 (-12.96%)</td><td>413.70 (+2.57%)</td><td>421.20 (+4.75%)</td><td>268.90 <b>(+54.45%)</b></td><td>121.93 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.76 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.24 (n/a)</td><td>669.90 (n/a)</td><td>403.32 (n/a)</td><td>402.10 (n/a)</td><td>174.10 (n/a)</td><td>204.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (-9.74%)</td><td>0.02 (+10.06%)</td><td>0.02 (+19.93%)</td><td>0.01 <b>(+34.21%)</b></td><td>0.00 <b>(-56.50%)</b></td><td>309.10 <b>(-25.50%)</b></td><td>264.16 (-13.40%)</td><td>258.20 (-16.63%)</td><td>234.70 (+10.76%)</td><td>29.47 <b>(-63.53%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>414.90 (n/a)</td><td>305.04 (n/a)</td><td>309.70 (n/a)</td><td>211.90 (n/a)</td><td>80.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (+14.05%)</td><td>0.01 (-4.94%)</td><td>0.01 (-14.00%)</td><td>0.01 (-2.56%)</td><td>0.00 (+12.47%)</td><td>509.10 (+2.62%)</td><td>325.18 (+6.05%)</td><td>292.40 (+16.26%)</td><td>209.90 (-12.32%)</td><td>111.53 (+2.91%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>306.62 (n/a)</td><td>251.50 (n/a)</td><td>239.40 (n/a)</td><td>108.37 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_decode</summary>


### test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+83.71%)</b></td><td>22438.09 (+1.73%)</td><td>15398.37 (-13.34%)</td><td>15497.74 (-16.38%)</td><td>6320.78 <b>(-38.73%)</b></td><td>5826.48 <b>(+25.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22057.54 (n/a)</td><td>17768.95 (n/a)</td><td>18534.29 (n/a)</td><td>10316.17 (n/a)</td><td>4629.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.00 (-7.14%)</td><td>0.00 (-2.27%)</td><td>0.00 <b>(+42.86%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-10.94%)</td><td>22094.93 (+15.66%)</td><td>12417.20 (+7.81%)</td><td>8056.24 <b>(-26.46%)</b></td><td>6178.47 (+5.02%)</td><td>7588.41 <b>(+29.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19102.96 (n/a)</td><td>11517.88 (n/a)</td><td>10955.05 (n/a)</td><td>5883.28 (n/a)</td><td>5881.21 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.14 (-9.47%)</td><td>0.09 <b>(-20.24%)</b></td><td>0.08 <b>(-31.90%)</b></td><td>0.07 (-9.47%)</td><td>0.03 (-17.54%)</td><td>29260.95 (+10.54%)</td><td>23435.79 <b>(+24.03%)</b></td><td>25437.21 <b>(+46.81%)</b></td><td>15448.07 (+10.47%)</td><td>5273.26 (-0.88%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>26471.86 (n/a)</td><td>18895.09 (n/a)</td><td>17326.94 (n/a)</td><td>13983.85 (n/a)</td><td>5319.99 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.54 <b>(-20.79%)</b></td><td>1.05 (-18.68%)</td><td>0.97 <b>(-33.90%)</b></td><td>0.56 <b>(-20.44%)</b></td><td>0.42 <b>(-24.17%)</b></td><td>941.50 <b>(+25.70%)</b></td><td>576.10 (+18.78%)</td><td>542.70 <b>(+51.30%)</b></td><td>340.20 <b>(+26.23%)</b></td><td>248.06 (+6.63%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>1.95 (n/a)</td><td>1.29 (n/a)</td><td>1.46 (n/a)</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>749.00 (n/a)</td><td>485.00 (n/a)</td><td>358.70 (n/a)</td><td>269.50 (n/a)</td><td>232.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.78 (-1.52%)</td><td>1.36 <b>(-37.20%)</b></td><td>1.51 <b>(-35.19%)</b></td><td>0.33 <b>(-75.00%)</b></td><td>0.99 <b>(+63.69%)</b></td><td>3145.90 <b>(+300.04%)</b></td><td>1389.18 <b>(+165.88%)</b></td><td>694.60 <b>(+54.29%)</b></td><td>376.70 (+1.54%)</td><td>1190.61 <b>(+600.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.83 (n/a)</td><td>2.16 (n/a)</td><td>2.33 (n/a)</td><td>1.33 (n/a)</td><td>0.61 (n/a)</td><td>786.40 (n/a)</td><td>522.48 (n/a)</td><td>450.20 (n/a)</td><td>371.00 (n/a)</td><td>169.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.58 (-2.67%)</td><td>1.21 (+5.65%)</td><td>1.29 <b>(+41.89%)</b></td><td>0.66 <b>(-20.05%)</b></td><td>0.38 (-2.53%)</td><td>792.90 <b>(+25.08%)</b></td><td>479.12 (-3.80%)</td><td>406.80 <b>(-29.52%)</b></td><td>331.10 (+2.76%)</td><td>189.18 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>633.90 (n/a)</td><td>498.02 (n/a)</td><td>577.20 (n/a)</td><td>322.20 (n/a)</td><td>149.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.29 <b>(-38.32%)</b></td><td>0.98 <b>(-36.33%)</b></td><td>0.93 <b>(-43.88%)</b></td><td>0.79 (-8.50%)</td><td>0.19 <b>(-59.79%)</b></td><td>666.50 (+9.28%)</td><td>549.64 <b>(+47.06%)</b></td><td>563.80 <b>(+78.19%)</b></td><td>407.70 <b>(+62.11%)</b></td><td>92.68 <b>(-34.16%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.09 (n/a)</td><td>1.54 (n/a)</td><td>1.66 (n/a)</td><td>0.86 (n/a)</td><td>0.46 (n/a)</td><td>609.90 (n/a)</td><td>373.74 (n/a)</td><td>316.40 (n/a)</td><td>251.50 (n/a)</td><td>140.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.75 (-15.44%)</td><td>1.32 (-0.50%)</td><td>1.36 <b>(+22.47%)</b></td><td>0.77 (-19.20%)</td><td>0.36 <b>(-21.75%)</b></td><td>678.10 <b>(+23.76%)</b></td><td>430.02 (-0.09%)</td><td>385.10 (-18.34%)</td><td>300.10 (+18.29%)</td><td>146.96 (+19.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (n/a)</td><td>1.32 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>0.46 (n/a)</td><td>547.90 (n/a)</td><td>430.40 (n/a)</td><td>471.60 (n/a)</td><td>253.70 (n/a)</td><td>123.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>
