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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.06 (+14.58%)</td><td>0.04 (+10.10%)</td><td>0.05 (+7.33%)</td><td>0.02 (+19.14%)</td><td>0.01 (+11.59%)</td><td>519.40 (-16.06%)</td><td>329.74 (-9.91%)</td><td>271.80 (-6.82%)</td><td>219.90 (-12.70%)</td><td>127.36 (-17.59%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>618.80 (n/a)</td><td>366.02 (n/a)</td><td>291.70 (n/a)</td><td>251.90 (n/a)</td><td>154.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 <b>(+67.87%)</b></td><td>0.03 <b>(+56.98%)</b></td><td>0.03 <b>(+38.74%)</b></td><td>0.02 <b>(+258.48%)</b></td><td>0.01 <b>(+23.47%)</b></td><td>538.80 <b>(-72.10%)</b></td><td>400.54 <b>(-49.25%)</b></td><td>372.70 <b>(-27.92%)</b></td><td>241.40 <b>(-40.42%)</b></td><td>119.62 <b>(-81.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1931.30 (n/a)</td><td>789.30 (n/a)</td><td>517.10 (n/a)</td><td>405.20 (n/a)</td><td>642.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (+13.71%)</td><td>0.04 <b>(+21.55%)</b></td><td>0.04 <b>(+58.72%)</b></td><td>0.02 (+6.26%)</td><td>0.01 (+2.53%)</td><td>507.50 (-5.90%)</td><td>339.84 (-18.75%)</td><td>295.10 <b>(-37.00%)</b></td><td>235.60 (-12.06%)</td><td>114.13 (-14.78%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>418.28 (n/a)</td><td>468.40 (n/a)</td><td>267.90 (n/a)</td><td>133.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (+14.60%)</td><td>0.02 (+0.08%)</td><td>0.02 (+6.21%)</td><td>0.00 <b>(-75.20%)</b></td><td>0.01 <b>(+81.77%)</b></td><td>2080.30 <b>(+303.32%)</b></td><td>627.90 <b>(+85.09%)</b></td><td>287.20 (-5.87%)</td><td>208.20 (-12.74%)</td><td>812.62 <b>(+636.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.80 (n/a)</td><td>339.24 (n/a)</td><td>305.10 (n/a)</td><td>238.60 (n/a)</td><td>110.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (-2.68%)</td><td>0.01 (-13.93%)</td><td>0.01 <b>(-40.66%)</b></td><td>0.01 (+4.16%)</td><td>0.01 (-15.37%)</td><td>508.70 (-3.98%)</td><td>390.00 (+12.20%)</td><td>450.80 <b>(+68.52%)</b></td><td>236.50 (+2.78%)</td><td>121.43 (-15.58%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>347.60 (n/a)</td><td>267.50 (n/a)</td><td>230.10 (n/a)</td><td>143.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 <b>(+33.50%)</b></td><td>0.02 (+11.47%)</td><td>0.02 (+16.04%)</td><td>0.01 (+5.20%)</td><td>0.01 <b>(+65.31%)</b></td><td>620.60 (-4.95%)</td><td>367.84 (-1.37%)</td><td>258.90 (-13.81%)</td><td>201.00 <b>(-25.11%)</b></td><td>191.73 (+18.83%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>652.90 (n/a)</td><td>372.94 (n/a)</td><td>300.40 (n/a)</td><td>268.40 (n/a)</td><td>161.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (+0.86%)</td><td>0.02 <b>(+30.02%)</b></td><td>0.02 <b>(+48.05%)</b></td><td>0.01 (+10.93%)</td><td>0.01 (-7.50%)</td><td>472.00 (-9.85%)</td><td>296.62 <b>(-24.70%)</b></td><td>259.40 <b>(-32.47%)</b></td><td>222.70 (-0.89%)</td><td>102.53 (-17.79%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.60 (n/a)</td><td>393.92 (n/a)</td><td>384.10 (n/a)</td><td>224.70 (n/a)</td><td>124.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (-0.05%)</td><td>0.02 (+3.26%)</td><td>0.02 <b>(+22.14%)</b></td><td>0.01 <b>(-22.77%)</b></td><td>0.01 <b>(+45.91%)</b></td><td>614.30 <b>(+29.49%)</b></td><td>381.24 (+6.67%)</td><td>301.30 (-18.12%)</td><td>232.30 (+0.04%)</td><td>172.91 <b>(+91.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.40 (n/a)</td><td>357.40 (n/a)</td><td>368.00 (n/a)</td><td>232.20 (n/a)</td><td>90.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.01 <b>(-41.97%)</b></td><td>0.01 (-19.63%)</td><td>0.01 (-0.42%)</td><td>0.01 (+11.65%)</td><td>0.00 <b>(-67.69%)</b></td><td>561.70 (-10.44%)</td><td>467.22 (+10.31%)</td><td>484.50 (+0.41%)</td><td>365.60 <b>(+72.29%)</b></td><td>83.23 <b>(-49.11%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>423.56 (n/a)</td><td>482.50 (n/a)</td><td>212.20 (n/a)</td><td>163.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>293.20 (n/a)</td><td>269.22 (n/a)</td><td>280.20 (n/a)</td><td>243.80 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.00 (n/a)</td><td>309.52 (n/a)</td><td>257.70 (n/a)</td><td>242.70 (n/a)</td><td>104.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1077.70 (n/a)</td><td>437.72 (n/a)</td><td>294.40 (n/a)</td><td>248.90 (n/a)</td><td>358.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>345.20 (n/a)</td><td>288.88 (n/a)</td><td>292.90 (n/a)</td><td>238.40 (n/a)</td><td>39.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.50 (n/a)</td><td>358.10 (n/a)</td><td>289.40 (n/a)</td><td>232.40 (n/a)</td><td>149.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>336.10 (n/a)</td><td>281.60 (n/a)</td><td>259.60 (n/a)</td><td>121.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.39 (-6.79%)</td><td>0.81 <b>(-21.24%)</b></td><td>0.74 <b>(-20.67%)</b></td><td>0.45 <b>(-44.49%)</b></td><td>0.34 <b>(+31.27%)</b></td><td>1014.90 <b>(+80.17%)</b></td><td>639.58 <b>(+38.16%)</b></td><td>617.70 <b>(+26.06%)</b></td><td>330.90 (+7.30%)</td><td>243.91 <b>(+158.81%)</b></td><td>101.41 (-6.79%)</td><td>59.51 <b>(-21.24%)</b></td><td>54.32 <b>(-20.67%)</b></td><td>33.06 <b>(-44.49%)</b></td><td>25.18 <b>(+31.27%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.49 (n/a)</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>0.81 (n/a)</td><td>0.26 (n/a)</td><td>563.30 (n/a)</td><td>462.94 (n/a)</td><td>490.00 (n/a)</td><td>308.40 (n/a)</td><td>94.25 (n/a)</td><td>108.79 (n/a)</td><td>75.57 (n/a)</td><td>68.48 (n/a)</td><td>59.56 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.46 (-4.59%)</td><td>1.15 (+15.71%)</td><td>1.34 <b>(+26.63%)</b></td><td>0.26 (-17.83%)</td><td>0.50 (+12.36%)</td><td>2494.60 <b>(+21.71%)</b></td><td>880.34 (+0.36%)</td><td>490.30 <b>(-21.02%)</b></td><td>449.50 (+4.80%)</td><td>902.56 <b>(+35.74%)</b></td><td>149.30 (-4.59%)</td><td>118.14 (+15.71%)</td><td>136.89 <b>(+26.63%)</b></td><td>26.90 (-17.83%)</td><td>51.26 (+12.36%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.53 (n/a)</td><td>1.00 (n/a)</td><td>1.06 (n/a)</td><td>0.32 (n/a)</td><td>0.45 (n/a)</td><td>2049.70 (n/a)</td><td>877.20 (n/a)</td><td>620.80 (n/a)</td><td>428.90 (n/a)</td><td>664.91 (n/a)</td><td>156.48 (n/a)</td><td>102.10 (n/a)</td><td>108.10 (n/a)</td><td>32.74 (n/a)</td><td>45.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.58 (-1.32%)</td><td>1.24 (-7.74%)</td><td>1.15 (-18.83%)</td><td>0.99 (+2.97%)</td><td>0.26 (-8.71%)</td><td>763.00 (-2.89%)</td><td>631.00 (+7.70%)</td><td>655.00 <b>(+23.19%)</b></td><td>476.50 (+1.34%)</td><td>125.04 (-8.28%)</td><td>176.05 (-1.32%)</td><td>137.47 (-7.74%)</td><td>128.08 (-18.83%)</td><td>109.94 (+2.97%)</td><td>28.76 (-8.71%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.60 (n/a)</td><td>1.34 (n/a)</td><td>1.42 (n/a)</td><td>0.96 (n/a)</td><td>0.28 (n/a)</td><td>785.70 (n/a)</td><td>585.90 (n/a)</td><td>531.70 (n/a)</td><td>470.20 (n/a)</td><td>136.33 (n/a)</td><td>178.40 (n/a)</td><td>149.00 (n/a)</td><td>157.78 (n/a)</td><td>106.77 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.56 (-11.00%)</td><td>1.29 (+18.66%)</td><td>1.30 (+6.23%)</td><td>0.96 <b>(+202.72%)</b></td><td>0.25 <b>(-53.25%)</b></td><td>1094.30 <b>(-66.97%)</b></td><td>839.22 <b>(-38.13%)</b></td><td>807.20 (-5.87%)</td><td>673.20 (+12.37%)</td><td>172.04 <b>(-84.54%)</b></td><td>199.38 (-11.00%)</td><td>165.07 (+18.66%)</td><td>166.27 (+6.23%)</td><td>122.65 <b>(+202.72%)</b></td><td>31.62 <b>(-53.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.75 (n/a)</td><td>1.09 (n/a)</td><td>1.22 (n/a)</td><td>0.32 (n/a)</td><td>0.53 (n/a)</td><td>3312.70 (n/a)</td><td>1356.38 (n/a)</td><td>857.50 (n/a)</td><td>599.10 (n/a)</td><td>1112.60 (n/a)</td><td>224.04 (n/a)</td><td>139.11 (n/a)</td><td>156.53 (n/a)</td><td>40.52 (n/a)</td><td>67.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.00 (+5.64%)</td><td>1.52 (+4.19%)</td><td>1.33 (-6.47%)</td><td>1.28 <b>(+31.52%)</b></td><td>0.32 <b>(-27.11%)</b></td><td>818.10 <b>(-23.97%)</b></td><td>712.80 (-8.09%)</td><td>790.90 (+6.92%)</td><td>523.30 (-5.34%)</td><td>130.95 <b>(-44.51%)</b></td><td>256.49 (+5.64%)</td><td>194.20 (+4.19%)</td><td>169.71 (-6.47%)</td><td>164.05 <b>(+31.52%)</b></td><td>40.35 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.90 (n/a)</td><td>1.46 (n/a)</td><td>1.42 (n/a)</td><td>0.97 (n/a)</td><td>0.43 (n/a)</td><td>1076.00 (n/a)</td><td>775.50 (n/a)</td><td>739.70 (n/a)</td><td>552.80 (n/a)</td><td>236.00 (n/a)</td><td>242.80 (n/a)</td><td>186.39 (n/a)</td><td>181.45 (n/a)</td><td>124.74 (n/a)</td><td>55.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.74 <b>(-40.01%)</b></td><td>1.51 (-6.49%)</td><td>1.50 (+3.49%)</td><td>1.30 <b>(+330.78%)</b></td><td>0.21 <b>(-79.18%)</b></td><td>808.30 <b>(-76.79%)</b></td><td>703.66 <b>(-40.73%)</b></td><td>699.50 (-3.38%)</td><td>602.50 <b>(+66.71%)</b></td><td>97.63 <b>(-92.50%)</b></td><td>222.76 <b>(-40.01%)</b></td><td>193.73 (-6.49%)</td><td>191.87 (+3.49%)</td><td>166.06 <b>(+330.78%)</b></td><td>26.91 <b>(-79.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.90 (n/a)</td><td>1.62 (n/a)</td><td>1.45 (n/a)</td><td>0.30 (n/a)</td><td>1.01 (n/a)</td><td>3481.90 (n/a)</td><td>1187.30 (n/a)</td><td>724.00 (n/a)</td><td>361.40 (n/a)</td><td>1301.00 (n/a)</td><td>371.33 (n/a)</td><td>207.17 (n/a)</td><td>185.40 (n/a)</td><td>38.55 (n/a)</td><td>129.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.64 (-10.95%)</td><td>1.16 (-9.41%)</td><td>1.20 (-2.72%)</td><td>0.72 <b>(+39.01%)</b></td><td>0.34 <b>(-39.76%)</b></td><td>1465.60 <b>(-28.07%)</b></td><td>976.74 (-4.25%)</td><td>876.20 (+2.80%)</td><td>640.60 (+12.31%)</td><td>310.11 <b>(-48.69%)</b></td><td>209.53 (-10.95%)</td><td>148.00 (-9.41%)</td><td>153.19 (-2.72%)</td><td>91.58 <b>(+39.01%)</b></td><td>43.38 <b>(-39.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.84 (n/a)</td><td>1.28 (n/a)</td><td>1.23 (n/a)</td><td>0.51 (n/a)</td><td>0.56 (n/a)</td><td>2037.40 (n/a)</td><td>1020.10 (n/a)</td><td>852.30 (n/a)</td><td>570.40 (n/a)</td><td>604.44 (n/a)</td><td>235.30 (n/a)</td><td>163.37 (n/a)</td><td>157.47 (n/a)</td><td>65.88 (n/a)</td><td>72.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.06 (+9.73%)</td><td>0.79 (+11.35%)</td><td>0.69 (+6.35%)</td><td>0.58 (+11.92%)</td><td>0.22 <b>(+25.54%)</b></td><td>623.40 (-10.65%)</td><td>485.12 (-9.03%)</td><td>520.50 (-5.96%)</td><td>340.80 (-8.88%)</td><td>125.66 (+1.50%)</td><td>49.22 (+9.73%)</td><td>36.67 (+11.35%)</td><td>32.24 (+6.35%)</td><td>26.91 (+11.92%)</td><td>10.13 <b>(+25.54%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.96 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.52 (n/a)</td><td>0.17 (n/a)</td><td>697.70 (n/a)</td><td>533.28 (n/a)</td><td>553.50 (n/a)</td><td>374.00 (n/a)</td><td>123.80 (n/a)</td><td>44.86 (n/a)</td><td>32.93 (n/a)</td><td>30.31 (n/a)</td><td>24.05 (n/a)</td><td>8.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.94 (+0.68%)</td><td>2.71 (-14.91%)</td><td>3.59 (+10.93%)</td><td>1.05 <b>(-57.70%)</b></td><td>1.40 <b>(+120.05%)</b></td><td>2486.30 <b>(+136.39%)</b></td><td>1321.18 <b>(+55.13%)</b></td><td>729.30 (-9.85%)</td><td>665.30 (-0.67%)</td><td>861.29 <b>(+394.41%)</b></td><td>806.91 (+0.68%)</td><td>554.50 (-14.91%)</td><td>736.10 (+10.93%)</td><td>215.94 <b>(-57.70%)</b></td><td>287.29 <b>(+120.05%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.91 (n/a)</td><td>3.18 (n/a)</td><td>3.24 (n/a)</td><td>2.49 (n/a)</td><td>0.64 (n/a)</td><td>1051.80 (n/a)</td><td>851.64 (n/a)</td><td>809.00 (n/a)</td><td>669.80 (n/a)</td><td>174.21 (n/a)</td><td>801.49 (n/a)</td><td>651.64 (n/a)</td><td>663.60 (n/a)</td><td>510.43 (n/a)</td><td>130.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.50 (n/a)</td><td>324.26 (n/a)</td><td>288.20 (n/a)</td><td>221.90 (n/a)</td><td>139.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>323.90 (n/a)</td><td>267.40 (n/a)</td><td>232.90 (n/a)</td><td>134.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.00 (n/a)</td><td>328.66 (n/a)</td><td>288.40 (n/a)</td><td>208.00 (n/a)</td><td>123.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>793.50 (n/a)</td><td>477.68 (n/a)</td><td>448.60 (n/a)</td><td>294.60 (n/a)</td><td>199.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.80 (n/a)</td><td>444.98 (n/a)</td><td>442.20 (n/a)</td><td>268.90 (n/a)</td><td>117.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1057.20 (n/a)</td><td>561.64 (n/a)</td><td>473.30 (n/a)</td><td>319.50 (n/a)</td><td>293.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.52 (-13.31%)</td><td>0.38 <b>(-23.06%)</b></td><td>0.41 (-15.41%)</td><td>0.17 <b>(-50.81%)</b></td><td>0.13 <b>(+38.91%)</b></td><td>1289.10 <b>(+103.30%)</b></td><td>678.42 <b>(+45.45%)</b></td><td>541.40 (+18.21%)</td><td>423.10 (+15.35%)</td><td>348.29 <b>(+244.61%)</b></td><td>22.30 (-13.31%)</td><td>16.09 <b>(-23.06%)</b></td><td>17.43 (-15.41%)</td><td>7.32 <b>(-50.81%)</b></td><td>5.52 <b>(+38.91%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.60 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>634.10 (n/a)</td><td>466.42 (n/a)</td><td>458.00 (n/a)</td><td>366.80 (n/a)</td><td>101.07 (n/a)</td><td>25.73 (n/a)</td><td>20.91 (n/a)</td><td>20.61 (n/a)</td><td>14.88 (n/a)</td><td>3.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.64 <b>(+34.15%)</b></td><td>0.49 <b>(+25.55%)</b></td><td>0.45 <b>(+25.38%)</b></td><td>0.40 (+17.67%)</td><td>0.10 <b>(+63.72%)</b></td><td>558.30 (-15.02%)</td><td>462.34 (-19.30%)</td><td>486.10 <b>(-20.25%)</b></td><td>346.60 <b>(-25.46%)</b></td><td>89.42 (+3.74%)</td><td>27.23 <b>(+34.15%)</b></td><td>21.08 <b>(+25.55%)</b></td><td>19.41 <b>(+25.38%)</b></td><td>16.90 (+17.67%)</td><td>4.37 <b>(+63.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>657.00 (n/a)</td><td>572.90 (n/a)</td><td>609.50 (n/a)</td><td>465.00 (n/a)</td><td>86.19 (n/a)</td><td>20.29 (n/a)</td><td>16.79 (n/a)</td><td>15.48 (n/a)</td><td>14.36 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.31 (+0.85%)</td><td>0.31 (+1.65%)</td><td>0.31 (+1.05%)</td><td>0.30 (+3.41%)</td><td>0.00 <b>(-61.56%)</b></td><td>83040.00 (-3.30%)</td><td>82152.00 (-1.64%)</td><td>81907.90 (-1.04%)</td><td>81770.30 (-0.84%)</td><td>516.74 <b>(-63.16%)</b></td><td>210.10 (+0.85%)</td><td>209.13 (+1.65%)</td><td>209.75 (+1.05%)</td><td>206.89 (+3.41%)</td><td>1.31 <b>(-61.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.00 (n/a)</td><td>85872.90 (n/a)</td><td>83521.26 (n/a)</td><td>82764.80 (n/a)</td><td>82463.60 (n/a)</td><td>1402.53 (n/a)</td><td>208.33 (n/a)</td><td>205.74 (n/a)</td><td>207.57 (n/a)</td><td>200.06 (n/a)</td><td>3.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.17 (+1.79%)</td><td>1.15 (+0.96%)</td><td>1.14 (-0.09%)</td><td>1.13 (+2.75%)</td><td>0.01 <b>(-28.59%)</b></td><td>22183.50 (-2.68%)</td><td>21914.70 (-0.96%)</td><td>21986.70 (+0.09%)</td><td>21492.60 (-1.76%)</td><td>257.07 <b>(-32.06%)</b></td><td>799.34 (+1.79%)</td><td>784.03 (+0.96%)</td><td>781.38 (-0.09%)</td><td>774.44 (+2.75%)</td><td>9.29 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.02 (n/a)</td><td>22794.10 (n/a)</td><td>22127.48 (n/a)</td><td>21966.10 (n/a)</td><td>21878.20 (n/a)</td><td>378.41 (n/a)</td><td>785.25 (n/a)</td><td>776.58 (n/a)</td><td>782.11 (n/a)</td><td>753.70 (n/a)</td><td>13.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>4.19 (+13.32%)</td><td>3.16 (+8.30%)</td><td>3.20 (-10.76%)</td><td>1.86 (+17.85%)</td><td>0.87 (-14.72%)</td><td>4328.40 (-15.15%)</td><td>2752.82 (-12.16%)</td><td>2520.80 (+12.06%)</td><td>1924.10 (-11.75%)</td><td>938.05 <b>(-29.72%)</b></td><td>1098.66 (+13.32%)</td><td>828.51 (+8.30%)</td><td>838.60 (-10.76%)</td><td>488.38 (+17.85%)</td><td>229.12 (-14.72%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.70 (n/a)</td><td>2.92 (n/a)</td><td>3.58 (n/a)</td><td>1.58 (n/a)</td><td>1.02 (n/a)</td><td>5101.20 (n/a)</td><td>3133.92 (n/a)</td><td>2249.50 (n/a)</td><td>2180.40 (n/a)</td><td>1334.66 (n/a)</td><td>969.50 (n/a)</td><td>765.02 (n/a)</td><td>939.74 (n/a)</td><td>414.40 (n/a)</td><td>268.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.23 (+6.85%)</td><td>0.21 (+9.02%)</td><td>0.22 (+18.76%)</td><td>0.19 (+3.27%)</td><td>0.02 <b>(+32.43%)</b></td><td>6429.30 (-3.17%)</td><td>5831.20 (-8.08%)</td><td>5560.20 (-15.80%)</td><td>5358.40 (-6.41%)</td><td>491.47 (+19.86%)</td><td>12.52 (+6.85%)</td><td>11.57 (+9.02%)</td><td>12.07 (+18.76%)</td><td>10.44 (+3.27%)</td><td>0.95 <b>(+32.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>6639.80 (n/a)</td><td>6343.88 (n/a)</td><td>6603.50 (n/a)</td><td>5725.40 (n/a)</td><td>410.04 (n/a)</td><td>11.72 (n/a)</td><td>10.62 (n/a)</td><td>10.16 (n/a)</td><td>10.11 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.94 (n/a)</td><td>3.63 (n/a)</td><td>3.64 (n/a)</td><td>3.40 (n/a)</td><td>0.23 (n/a)</td><td>3.94 (n/a)</td><td>3.63 (n/a)</td><td>3.63 (n/a)</td><td>3.40 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>7.62 (+8.73%)</td><td>6.58 (+7.82%)</td><td>7.34 (+14.81%)</td><td>4.56 (-1.41%)</td><td>1.34 <b>(+36.98%)</b></td><td>7.62 (+8.73%)</td><td>6.58 (+7.82%)</td><td>7.34 (+14.81%)</td><td>4.56 (-1.41%)</td><td>1.34 <b>(+36.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>7.01 (n/a)</td><td>6.10 (n/a)</td><td>6.40 (n/a)</td><td>4.63 (n/a)</td><td>0.98 (n/a)</td><td>7.00 (n/a)</td><td>6.10 (n/a)</td><td>6.39 (n/a)</td><td>4.62 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>13.85 (-2.60%)</td><td>10.81 (+9.39%)</td><td>10.27 <b>(+20.76%)</b></td><td>8.21 (-0.52%)</td><td>2.69 (+6.90%)</td><td>13.85 (-2.60%)</td><td>10.81 (+9.39%)</td><td>10.26 <b>(+20.76%)</b></td><td>8.21 (-0.52%)</td><td>2.69 (+6.90%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>14.22 (n/a)</td><td>9.89 (n/a)</td><td>8.50 (n/a)</td><td>8.26 (n/a)</td><td>2.52 (n/a)</td><td>14.22 (n/a)</td><td>9.88 (n/a)</td><td>8.50 (n/a)</td><td>8.25 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.82 (n/a)</td><td>3.67 (n/a)</td><td>3.77 (n/a)</td><td>3.37 (n/a)</td><td>0.18 (n/a)</td><td>3.82 (n/a)</td><td>3.67 (n/a)</td><td>3.77 (n/a)</td><td>3.37 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>7.57 (+9.78%)</td><td>6.93 (+6.39%)</td><td>7.20 (+5.76%)</td><td>5.80 (+6.24%)</td><td>0.76 <b>(+26.25%)</b></td><td>7.57 (+9.78%)</td><td>6.93 (+6.39%)</td><td>7.19 (+5.76%)</td><td>5.80 (+6.24%)</td><td>0.76 <b>(+26.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>6.90 (n/a)</td><td>6.51 (n/a)</td><td>6.81 (n/a)</td><td>5.46 (n/a)</td><td>0.60 (n/a)</td><td>6.89 (n/a)</td><td>6.51 (n/a)</td><td>6.80 (n/a)</td><td>5.46 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>13.76 <b>(+20.25%)</b></td><td>11.56 <b>(+20.13%)</b></td><td>13.41 <b>(+30.12%)</b></td><td>8.32 (+12.43%)</td><td>2.83 <b>(+62.93%)</b></td><td>13.75 <b>(+20.25%)</b></td><td>11.55 <b>(+20.13%)</b></td><td>13.41 <b>(+30.12%)</b></td><td>8.31 (+12.43%)</td><td>2.83 <b>(+62.93%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>11.44 (n/a)</td><td>9.62 (n/a)</td><td>10.31 (n/a)</td><td>7.40 (n/a)</td><td>1.74 (n/a)</td><td>11.43 (n/a)</td><td>9.61 (n/a)</td><td>10.30 (n/a)</td><td>7.39 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.29 (+5.59%)</td><td>2.98 (+10.57%)</td><td>2.99 (+1.72%)</td><td>2.75 <b>(+56.71%)</b></td><td>0.22 <b>(-59.13%)</b></td><td>3.29 (+5.59%)</td><td>2.98 (+10.57%)</td><td>2.99 (+1.72%)</td><td>2.74 <b>(+56.71%)</b></td><td>0.22 <b>(-59.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.12 (n/a)</td><td>2.70 (n/a)</td><td>2.94 (n/a)</td><td>1.75 (n/a)</td><td>0.55 (n/a)</td><td>3.11 (n/a)</td><td>2.69 (n/a)</td><td>2.94 (n/a)</td><td>1.75 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.59 (-4.61%)</td><td>0.47 (+12.99%)</td><td>0.53 (+5.04%)</td><td>0.34 <b>(+354.12%)</b></td><td>0.11 <b>(-46.37%)</b></td><td>0.58 (-4.61%)</td><td>0.47 (+12.99%)</td><td>0.52 (+5.04%)</td><td>0.34 <b>(+354.12%)</b></td><td>0.11 <b>(-46.37%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.61 (n/a)</td><td>0.42 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.60 (n/a)</td><td>0.41 (n/a)</td><td>0.49 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.73 <b>(+46.73%)</b></td><td>0.63 <b>(+91.59%)</b></td><td>0.68 <b>(+84.53%)</b></td><td>0.40 <b>(+428.25%)</b></td><td>0.13 (-14.78%)</td><td>0.72 <b>(+46.73%)</b></td><td>0.62 <b>(+91.59%)</b></td><td>0.68 <b>(+84.53%)</b></td><td>0.40 <b>(+428.25%)</b></td><td>0.13 (-14.78%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.46 (-5.25%)</td><td>1.61 (-10.74%)</td><td>1.92 (-0.84%)</td><td>0.76 <b>(+54.89%)</b></td><td>0.77 (-7.63%)</td><td>2.42 (-5.25%)</td><td>1.58 (-10.74%)</td><td>1.89 (-0.84%)</td><td>0.75 <b>(+54.89%)</b></td><td>0.76 (-7.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.60 (n/a)</td><td>1.80 (n/a)</td><td>1.93 (n/a)</td><td>0.49 (n/a)</td><td>0.83 (n/a)</td><td>2.56 (n/a)</td><td>1.77 (n/a)</td><td>1.90 (n/a)</td><td>0.48 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.00 (n/a)</td><td>358.30 (n/a)</td><td>316.50 (n/a)</td><td>281.20 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1916.10 (n/a)</td><td>703.18 (n/a)</td><td>412.70 (n/a)</td><td>295.30 (n/a)</td><td>687.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.20 (n/a)</td><td>373.00 (n/a)</td><td>268.80 (n/a)</td><td>248.10 (n/a)</td><td>159.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>387.58 (n/a)</td><td>397.90 (n/a)</td><td>234.80 (n/a)</td><td>125.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.70 (n/a)</td><td>319.34 (n/a)</td><td>294.80 (n/a)</td><td>250.30 (n/a)</td><td>87.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.30 (n/a)</td><td>352.62 (n/a)</td><td>274.00 (n/a)</td><td>236.20 (n/a)</td><td>128.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-16.25%)</td><td>0.02 (-7.27%)</td><td>0.03 (+3.28%)</td><td>0.01 (-11.40%)</td><td>0.01 (-13.33%)</td><td>575.10 (+12.85%)</td><td>374.16 (+7.53%)</td><td>286.20 (-3.18%)</td><td>269.50 (+19.41%)</td><td>135.89 (+10.91%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.60 (n/a)</td><td>347.96 (n/a)</td><td>295.60 (n/a)</td><td>225.70 (n/a)</td><td>122.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+6.92%)</td><td>0.02 (-13.15%)</td><td>0.02 <b>(-34.90%)</b></td><td>0.02 (-12.32%)</td><td>0.01 <b>(+38.50%)</b></td><td>538.20 (+14.05%)</td><td>401.62 <b>(+21.28%)</b></td><td>446.80 <b>(+53.65%)</b></td><td>231.30 (-6.47%)</td><td>132.95 <b>(+46.54%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.90 (n/a)</td><td>331.14 (n/a)</td><td>290.80 (n/a)</td><td>247.30 (n/a)</td><td>90.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+15.23%)</td><td>0.03 (+16.73%)</td><td>0.02 (-1.50%)</td><td>0.02 <b>(+115.91%)</b></td><td>0.01 (-5.63%)</td><td>507.10 <b>(-53.69%)</b></td><td>337.12 <b>(-28.79%)</b></td><td>340.00 (+1.52%)</td><td>204.60 (-13.23%)</td><td>126.03 <b>(-64.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1094.90 (n/a)</td><td>473.40 (n/a)</td><td>334.90 (n/a)</td><td>235.80 (n/a)</td><td>356.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+8.18%)</td><td>0.02 (+2.82%)</td><td>0.02 (+6.22%)</td><td>0.01 (-4.03%)</td><td>0.01 (+13.84%)</td><td>595.80 (+4.22%)</td><td>462.02 (-1.06%)</td><td>495.30 (-5.85%)</td><td>221.60 (-7.55%)</td><td>141.54 (+3.20%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>466.98 (n/a)</td><td>526.10 (n/a)</td><td>239.70 (n/a)</td><td>137.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (+11.84%)</td><td>0.03 <b>(+50.19%)</b></td><td>0.03 <b>(+85.07%)</b></td><td>0.01 (-4.91%)</td><td>0.01 <b>(+24.56%)</b></td><td>636.80 (+5.15%)</td><td>335.08 <b>(-30.07%)</b></td><td>265.30 <b>(-45.96%)</b></td><td>241.20 (-10.57%)</td><td>169.01 <b>(+29.64%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.60 (n/a)</td><td>479.16 (n/a)</td><td>490.90 (n/a)</td><td>269.70 (n/a)</td><td>130.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 <b>(+36.35%)</b></td><td>0.01 (-1.31%)</td><td>0.01 (-12.45%)</td><td>0.00 (-5.88%)</td><td>0.01 <b>(+70.25%)</b></td><td>2054.10 (+6.25%)</td><td>1042.72 <b>(+33.29%)</b></td><td>574.70 (+14.23%)</td><td>301.20 <b>(-26.68%)</b></td><td>855.14 <b>(+32.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1933.30 (n/a)</td><td>782.30 (n/a)</td><td>503.10 (n/a)</td><td>410.80 (n/a)</td><td>645.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+10.33%)</td><td>0.02 (-2.46%)</td><td>0.01 (-7.12%)</td><td>0.00 <b>(-59.06%)</b></td><td>0.01 <b>(+30.69%)</b></td><td>1836.40 <b>(+144.23%)</b></td><td>747.30 <b>(+36.30%)</b></td><td>579.40 (+7.66%)</td><td>226.60 (-9.36%)</td><td>626.62 <b>(+213.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>751.90 (n/a)</td><td>548.28 (n/a)</td><td>538.20 (n/a)</td><td>250.00 (n/a)</td><td>199.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 <b>(+26.11%)</b></td><td>0.02 (+0.60%)</td><td>0.02 (+4.33%)</td><td>0.01 <b>(-44.96%)</b></td><td>0.01 <b>(+70.42%)</b></td><td>982.10 <b>(+81.67%)</b></td><td>559.04 <b>(+20.18%)</b></td><td>484.50 (-4.15%)</td><td>200.40 <b>(-20.70%)</b></td><td>290.59 <b>(+140.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.60 (n/a)</td><td>465.16 (n/a)</td><td>505.50 (n/a)</td><td>252.70 (n/a)</td><td>120.93 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-14.66%)</td><td>0.02 <b>(-34.43%)</b></td><td>0.02 <b>(-41.91%)</b></td><td>0.00 <b>(-74.38%)</b></td><td>0.01 <b>(+27.86%)</b></td><td>1980.80 <b>(+290.31%)</b></td><td>687.82 <b>(+135.93%)</b></td><td>421.40 <b>(+72.14%)</b></td><td>241.80 (+17.21%)</td><td>730.15 <b>(+495.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.50 (n/a)</td><td>291.54 (n/a)</td><td>244.80 (n/a)</td><td>206.30 (n/a)</td><td>122.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-3.76%)</td><td>0.03 (+14.16%)</td><td>0.03 (+0.71%)</td><td>0.02 <b>(+34.10%)</b></td><td>0.01 <b>(-35.06%)</b></td><td>419.40 <b>(-25.43%)</b></td><td>306.26 (-17.65%)</td><td>298.30 (-0.70%)</td><td>253.80 (+3.93%)</td><td>66.49 <b>(-49.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>371.88 (n/a)</td><td>300.40 (n/a)</td><td>244.20 (n/a)</td><td>132.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 <b>(+23.36%)</b></td><td>0.03 <b>(+28.72%)</b></td><td>0.03 (+4.11%)</td><td>0.02 <b>(+36.31%)</b></td><td>0.01 (-14.59%)</td><td>424.20 <b>(-26.63%)</b></td><td>284.88 <b>(-27.59%)</b></td><td>273.80 (-3.96%)</td><td>216.90 (-18.95%)</td><td>82.85 <b>(-48.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.20 (n/a)</td><td>393.40 (n/a)</td><td>285.10 (n/a)</td><td>267.60 (n/a)</td><td>162.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-1.28%)</td><td>0.02 (-1.73%)</td><td>0.03 (-0.70%)</td><td>0.01 <b>(-24.70%)</b></td><td>0.01 (+15.04%)</td><td>687.60 <b>(+32.82%)</b></td><td>373.08 (+7.65%)</td><td>304.80 (+0.69%)</td><td>255.30 (+1.31%)</td><td>177.76 <b>(+65.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.70 (n/a)</td><td>346.58 (n/a)</td><td>302.70 (n/a)</td><td>252.00 (n/a)</td><td>107.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-12.96%)</td><td>0.02 <b>(-27.93%)</b></td><td>0.01 <b>(-45.01%)</b></td><td>0.01 (-4.58%)</td><td>0.01 <b>(-26.38%)</b></td><td>637.90 (+4.80%)</td><td>519.84 <b>(+33.51%)</b></td><td>549.70 <b>(+81.84%)</b></td><td>306.10 (+14.90%)</td><td>126.53 (-15.66%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.70 (n/a)</td><td>389.36 (n/a)</td><td>302.30 (n/a)</td><td>266.40 (n/a)</td><td>150.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-2.48%)</td><td>0.02 (-11.86%)</td><td>0.02 <b>(-27.70%)</b></td><td>0.01 (+2.97%)</td><td>0.01 (+14.91%)</td><td>585.80 (-2.88%)</td><td>444.44 (+15.74%)</td><td>475.20 <b>(+38.30%)</b></td><td>272.70 (+2.56%)</td><td>141.31 (+9.73%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.20 (n/a)</td><td>384.00 (n/a)</td><td>343.60 (n/a)</td><td>265.90 (n/a)</td><td>128.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.10 <b>(+24.03%)</b></td><td>0.08 <b>(+22.74%)</b></td><td>0.07 (+3.18%)</td><td>0.06 <b>(+39.55%)</b></td><td>0.02 (-0.21%)</td><td>389.60 <b>(-28.34%)</b></td><td>322.66 <b>(-20.94%)</b></td><td>334.90 (-3.07%)</td><td>242.50 (-19.38%)</td><td>70.04 <b>(-43.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>543.70 (n/a)</td><td>408.10 (n/a)</td><td>345.50 (n/a)</td><td>300.80 (n/a)</td><td>123.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.16 (-3.89%)</td><td>0.09 <b>(-22.65%)</b></td><td>0.08 <b>(-20.06%)</b></td><td>0.02 <b>(-75.05%)</b></td><td>0.06 <b>(+46.74%)</b></td><td>1896.00 <b>(+300.85%)</b></td><td>711.94 <b>(+94.40%)</b></td><td>488.50 <b>(+25.10%)</b></td><td>248.70 (+4.06%)</td><td>676.52 <b>(+547.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>473.00 (n/a)</td><td>366.22 (n/a)</td><td>390.50 (n/a)</td><td>239.00 (n/a)</td><td>104.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (+5.81%)</td><td>0.01 (-14.64%)</td><td>0.01 <b>(-45.87%)</b></td><td>0.01 <b>(-32.44%)</b></td><td>0.01 <b>(+58.60%)</b></td><td>704.20 <b>(+48.03%)</b></td><td>470.10 <b>(+30.52%)</b></td><td>544.00 <b>(+84.72%)</b></td><td>264.00 (-5.51%)</td><td>195.67 <b>(+100.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.70 (n/a)</td><td>360.18 (n/a)</td><td>294.50 (n/a)</td><td>279.40 (n/a)</td><td>97.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (-4.17%)</td><td>0.02 (-13.27%)</td><td>0.02 <b>(-23.86%)</b></td><td>0.02 (+9.87%)</td><td>0.01 <b>(-20.31%)</b></td><td>527.00 (-8.98%)</td><td>386.34 (+10.81%)</td><td>339.60 <b>(+31.32%)</b></td><td>250.30 (+4.34%)</td><td>125.79 (-16.04%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.00 (n/a)</td><td>348.64 (n/a)</td><td>258.60 (n/a)</td><td>239.90 (n/a)</td><td>149.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (-18.98%)</td><td>0.04 (-19.47%)</td><td>0.05 (-1.71%)</td><td>0.02 <b>(-52.92%)</b></td><td>0.01 <b>(+66.52%)</b></td><td>635.50 <b>(+112.40%)</b></td><td>358.88 <b>(+41.25%)</b></td><td>255.50 (+1.75%)</td><td>238.00 <b>(+23.44%)</b></td><td>173.99 <b>(+314.29%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>299.20 (n/a)</td><td>254.08 (n/a)</td><td>251.10 (n/a)</td><td>192.80 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (-2.78%)</td><td>0.03 (-7.94%)</td><td>0.02 <b>(-25.59%)</b></td><td>0.01 (-12.44%)</td><td>0.01 <b>(+20.44%)</b></td><td>576.70 (+14.22%)</td><td>370.40 (+13.68%)</td><td>398.70 <b>(+34.38%)</b></td><td>216.70 (+2.90%)</td><td>144.39 <b>(+31.60%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.90 (n/a)</td><td>325.84 (n/a)</td><td>296.70 (n/a)</td><td>210.60 (n/a)</td><td>109.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 <b>(+24.88%)</b></td><td>0.03 <b>(+32.00%)</b></td><td>0.03 <b>(+37.16%)</b></td><td>0.02 <b>(+44.58%)</b></td><td>0.01 (+11.14%)</td><td>566.70 <b>(-30.83%)</b></td><td>397.22 <b>(-28.14%)</b></td><td>374.10 <b>(-27.10%)</b></td><td>213.80 (-19.93%)</td><td>133.99 <b>(-41.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>819.30 (n/a)</td><td>552.80 (n/a)</td><td>513.20 (n/a)</td><td>267.00 (n/a)</td><td>228.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+3.62%)</td><td>0.02 <b>(-24.40%)</b></td><td>0.02 <b>(-36.10%)</b></td><td>0.01 (+3.03%)</td><td>0.01 (+8.50%)</td><td>570.30 (-2.94%)</td><td>433.06 <b>(+32.75%)</b></td><td>470.20 <b>(+56.47%)</b></td><td>192.70 (-3.51%)</td><td>142.49 (-8.23%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.60 (n/a)</td><td>326.22 (n/a)</td><td>300.50 (n/a)</td><td>199.70 (n/a)</td><td>155.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (-2.89%)</td><td>0.03 (+13.80%)</td><td>0.02 (+15.64%)</td><td>0.02 (+5.65%)</td><td>0.01 (+1.45%)</td><td>583.50 (-5.35%)</td><td>407.76 (-12.84%)</td><td>468.10 (-13.54%)</td><td>234.40 (+2.99%)</td><td>156.04 (-8.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>616.50 (n/a)</td><td>467.82 (n/a)</td><td>541.40 (n/a)</td><td>227.60 (n/a)</td><td>171.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 <b>(+44.95%)</b></td><td>0.02 (-8.94%)</td><td>0.02 <b>(-33.40%)</b></td><td>0.00 <b>(-70.63%)</b></td><td>0.01 <b>(+130.89%)</b></td><td>1898.10 <b>(+240.47%)</b></td><td>720.58 <b>(+72.11%)</b></td><td>528.80 <b>(+50.14%)</b></td><td>205.30 <b>(-31.01%)</b></td><td>674.79 <b>(+452.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.50 (n/a)</td><td>418.68 (n/a)</td><td>352.20 (n/a)</td><td>297.60 (n/a)</td><td>122.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 <b>(+22.94%)</b></td><td>0.02 (-4.70%)</td><td>0.02 <b>(-25.19%)</b></td><td>0.01 (+10.61%)</td><td>0.01 <b>(+39.42%)</b></td><td>651.70 (-9.59%)</td><td>475.94 (+7.96%)</td><td>541.30 <b>(+33.65%)</b></td><td>267.10 (-18.64%)</td><td>159.01 (-1.34%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>720.80 (n/a)</td><td>440.86 (n/a)</td><td>405.00 (n/a)</td><td>328.30 (n/a)</td><td>161.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (+14.96%)</td><td>0.03 (+15.72%)</td><td>0.02 <b>(+32.89%)</b></td><td>0.01 <b>(+103.47%)</b></td><td>0.01 (-16.28%)</td><td>553.10 <b>(-50.85%)</b></td><td>377.70 <b>(-30.37%)</b></td><td>355.50 <b>(-24.76%)</b></td><td>195.70 (-13.02%)</td><td>149.01 <b>(-59.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1125.40 (n/a)</td><td>542.42 (n/a)</td><td>472.50 (n/a)</td><td>225.00 (n/a)</td><td>370.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (+4.72%)</td><td>0.02 (-6.35%)</td><td>0.02 <b>(-33.59%)</b></td><td>0.02 (-1.68%)</td><td>0.01 (+19.94%)</td><td>530.20 (+1.69%)</td><td>407.46 (+9.11%)</td><td>470.30 <b>(+50.59%)</b></td><td>271.10 (-4.51%)</td><td>123.21 (+13.27%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>373.44 (n/a)</td><td>312.30 (n/a)</td><td>283.90 (n/a)</td><td>108.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 <b>(+26.21%)</b></td><td>0.02 <b>(+46.04%)</b></td><td>0.03 <b>(+95.81%)</b></td><td>0.01 (-5.53%)</td><td>0.01 <b>(+67.04%)</b></td><td>792.80 (+5.85%)</td><td>445.64 (-19.66%)</td><td>307.90 <b>(-48.94%)</b></td><td>218.80 <b>(-20.75%)</b></td><td>267.12 <b>(+53.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>749.00 (n/a)</td><td>554.72 (n/a)</td><td>603.00 (n/a)</td><td>276.10 (n/a)</td><td>174.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.47 (+14.94%)</td><td>0.31 (+12.14%)</td><td>0.34 <b>(+38.20%)</b></td><td>0.17 (+3.61%)</td><td>0.12 (+13.87%)</td><td>593.90 (-3.49%)</td><td>365.66 (-9.47%)</td><td>286.00 <b>(-27.65%)</b></td><td>209.90 (-13.01%)</td><td>155.74 (+0.70%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>615.40 (n/a)</td><td>403.92 (n/a)</td><td>395.30 (n/a)</td><td>241.30 (n/a)</td><td>154.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.39 <b>(+39.04%)</b></td><td>0.31 <b>(+59.39%)</b></td><td>0.34 <b>(+93.47%)</b></td><td>0.21 <b>(+29.68%)</b></td><td>0.09 <b>(+83.27%)</b></td><td>472.00 <b>(-22.89%)</b></td><td>344.36 <b>(-34.86%)</b></td><td>291.00 <b>(-48.31%)</b></td><td>251.20 <b>(-28.08%)</b></td><td>110.41 (+6.95%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>612.10 (n/a)</td><td>528.68 (n/a)</td><td>563.00 (n/a)</td><td>349.30 (n/a)</td><td>103.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.33 (-13.95%)</td><td>0.21 <b>(-33.66%)</b></td><td>0.19 <b>(-37.92%)</b></td><td>0.16 <b>(-27.39%)</b></td><td>0.07 (+8.48%)</td><td>614.30 <b>(+37.74%)</b></td><td>500.38 <b>(+55.21%)</b></td><td>512.90 <b>(+61.09%)</b></td><td>297.40 (+16.22%)</td><td>124.85 <b>(+66.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>446.00 (n/a)</td><td>322.38 (n/a)</td><td>318.40 (n/a)</td><td>255.90 (n/a)</td><td>75.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.43 <b>(+81.10%)</b></td><td>0.25 <b>(+47.58%)</b></td><td>0.26 <b>(+58.27%)</b></td><td>0.12 (-11.23%)</td><td>0.12 <b>(+197.97%)</b></td><td>614.30 (+12.63%)</td><td>364.10 <b>(-20.02%)</b></td><td>286.90 <b>(-36.83%)</b></td><td>170.20 <b>(-44.78%)</b></td><td>182.21 <b>(+95.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>545.40 (n/a)</td><td>455.22 (n/a)</td><td>454.20 (n/a)</td><td>308.20 (n/a)</td><td>93.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.25 (-2.91%)</td><td>0.22 (+5.80%)</td><td>0.23 (-4.97%)</td><td>0.15 <b>(+20.34%)</b></td><td>0.04 <b>(-34.50%)</b></td><td>496.40 (-16.91%)</td><td>350.98 (-11.04%)</td><td>317.70 (+5.23%)</td><td>290.90 (+3.01%)</td><td>85.49 <b>(-41.74%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>597.40 (n/a)</td><td>394.52 (n/a)</td><td>301.90 (n/a)</td><td>282.40 (n/a)</td><td>146.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.27 <b>(+48.84%)</b></td><td>0.17 (+14.04%)</td><td>0.15 (+1.24%)</td><td>0.07 <b>(-39.16%)</b></td><td>0.08 <b>(+210.78%)</b></td><td>1038.00 <b>(+64.37%)</b></td><td>532.84 (+7.67%)</td><td>495.40 (-1.22%)</td><td>268.30 <b>(-32.82%)</b></td><td>309.24 <b>(+235.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>631.50 (n/a)</td><td>494.90 (n/a)</td><td>501.50 (n/a)</td><td>399.40 (n/a)</td><td>92.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.47 (-1.17%)</td><td>0.33 (-18.09%)</td><td>0.39 (-7.37%)</td><td>0.19 <b>(-32.42%)</b></td><td>0.13 <b>(+74.86%)</b></td><td>705.50 <b>(+47.97%)</b></td><td>464.00 <b>(+37.24%)</b></td><td>336.40 (+7.96%)</td><td>280.40 (+1.19%)</td><td>208.31 <b>(+163.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.07 (n/a)</td><td>476.80 (n/a)</td><td>338.10 (n/a)</td><td>311.60 (n/a)</td><td>277.10 (n/a)</td><td>79.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.57 (+11.75%)</td><td>0.30 (-17.79%)</td><td>0.24 <b>(-39.30%)</b></td><td>0.22 (+11.05%)</td><td>0.15 (+10.33%)</td><td>608.30 (-9.93%)</td><td>506.72 <b>(+21.02%)</b></td><td>556.50 <b>(+64.74%)</b></td><td>230.70 (-10.51%)</td><td>156.35 (-14.32%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>675.40 (n/a)</td><td>418.70 (n/a)</td><td>337.80 (n/a)</td><td>257.80 (n/a)</td><td>182.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.42 (-16.98%)</td><td>0.32 (-14.22%)</td><td>0.35 (-18.18%)</td><td>0.22 <b>(+65.77%)</b></td><td>0.08 <b>(-41.17%)</b></td><td>589.10 <b>(-39.68%)</b></td><td>432.14 (-1.50%)</td><td>379.20 <b>(+22.20%)</b></td><td>312.60 <b>(+20.46%)</b></td><td>119.03 <b>(-60.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.42 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>976.60 (n/a)</td><td>438.72 (n/a)</td><td>310.30 (n/a)</td><td>259.50 (n/a)</td><td>302.01 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (+5.10%)</td><td>0.01 (-10.28%)</td><td>0.02 (-10.86%)</td><td>0.01 (-18.51%)</td><td>0.00 <b>(+79.49%)</b></td><td>369.20 <b>(+22.70%)</b></td><td>286.90 (+14.27%)</td><td>265.10 (+12.14%)</td><td>221.20 (-4.86%)</td><td>60.27 <b>(+110.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.90 (n/a)</td><td>251.08 (n/a)</td><td>236.40 (n/a)</td><td>232.50 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (+15.00%)</td><td>0.01 <b>(+28.54%)</b></td><td>0.01 <b>(+20.20%)</b></td><td>0.01 <b>(+299.51%)</b></td><td>0.00 (-16.53%)</td><td>483.70 <b>(-74.97%)</b></td><td>343.60 <b>(-48.67%)</b></td><td>294.60 (-16.80%)</td><td>225.70 (-13.03%)</td><td>124.19 <b>(-82.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1932.40 (n/a)</td><td>669.42 (n/a)</td><td>354.10 (n/a)</td><td>259.50 (n/a)</td><td>712.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 <b>(+21.61%)</b></td><td>0.01 <b>(+28.60%)</b></td><td>0.01 <b>(+43.06%)</b></td><td>0.01 (-15.12%)</td><td>0.00 <b>(+83.34%)</b></td><td>531.40 (+17.80%)</td><td>329.06 (-17.92%)</td><td>296.20 <b>(-30.11%)</b></td><td>243.30 (-17.78%)</td><td>117.51 <b>(+83.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>451.10 (n/a)</td><td>400.92 (n/a)</td><td>423.80 (n/a)</td><td>295.90 (n/a)</td><td>63.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.44 <b>(-26.21%)</b></td><td>0.30 (-17.51%)</td><td>0.25 <b>(-29.67%)</b></td><td>0.17 <b>(-21.71%)</b></td><td>0.12 (-12.86%)</td><td>770.00 <b>(+27.72%)</b></td><td>497.66 <b>(+24.71%)</b></td><td>536.80 <b>(+42.20%)</b></td><td>299.10 <b>(+35.52%)</b></td><td>198.01 <b>(+42.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>602.90 (n/a)</td><td>399.06 (n/a)</td><td>377.50 (n/a)</td><td>220.70 (n/a)</td><td>138.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.53 (-5.24%)</td><td>0.46 (+12.20%)</td><td>0.49 (+9.83%)</td><td>0.29 <b>(+28.34%)</b></td><td>0.09 <b>(-42.28%)</b></td><td>448.90 <b>(-22.08%)</b></td><td>302.58 (-19.67%)</td><td>269.70 (-8.95%)</td><td>249.70 (+5.49%)</td><td>82.50 <b>(-50.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>576.10 (n/a)</td><td>376.66 (n/a)</td><td>296.20 (n/a)</td><td>236.70 (n/a)</td><td>166.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.81 <b>(+38.30%)</b></td><td>0.49 <b>(+42.72%)</b></td><td>0.47 <b>(+54.61%)</b></td><td>0.29 <b>(+39.85%)</b></td><td>0.20 <b>(+33.44%)</b></td><td>461.30 <b>(-28.49%)</b></td><td>301.78 <b>(-30.61%)</b></td><td>279.20 <b>(-35.33%)</b></td><td>163.00 <b>(-27.68%)</b></td><td>113.02 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.59 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>645.10 (n/a)</td><td>434.92 (n/a)</td><td>431.70 (n/a)</td><td>225.40 (n/a)</td><td>162.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.51 (+14.97%)</td><td>0.42 (+11.48%)</td><td>0.49 <b>(+34.50%)</b></td><td>0.26 (-8.94%)</td><td>0.12 <b>(+98.97%)</b></td><td>500.60 (+9.80%)</td><td>343.36 (-5.27%)</td><td>270.80 <b>(-25.65%)</b></td><td>260.20 (-13.01%)</td><td>111.51 <b>(+83.15%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.06 (n/a)</td><td>455.90 (n/a)</td><td>362.46 (n/a)</td><td>364.20 (n/a)</td><td>299.10 (n/a)</td><td>60.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.62 (+14.28%)</td><td>0.43 (-6.15%)</td><td>0.46 (-2.09%)</td><td>0.26 <b>(-33.87%)</b></td><td>0.15 <b>(+138.47%)</b></td><td>514.10 <b>(+51.21%)</b></td><td>345.02 (+17.60%)</td><td>285.10 (+2.15%)</td><td>213.10 (-12.52%)</td><td>132.78 <b>(+220.17%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.54 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>340.00 (n/a)</td><td>293.38 (n/a)</td><td>279.10 (n/a)</td><td>243.60 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (-1.46%)</td><td>0.01 (-0.28%)</td><td>0.01 (-7.41%)</td><td>0.01 (+19.06%)</td><td>0.00 <b>(-29.44%)</b></td><td>511.00 (-16.00%)</td><td>341.42 (-6.28%)</td><td>298.80 (+7.99%)</td><td>250.00 (+1.50%)</td><td>102.48 <b>(-35.28%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.30 (n/a)</td><td>364.28 (n/a)</td><td>276.70 (n/a)</td><td>246.30 (n/a)</td><td>158.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.01 <b>(-23.79%)</b></td><td>0.01 <b>(-39.48%)</b></td><td>0.01 <b>(-48.78%)</b></td><td>0.01 <b>(-43.06%)</b></td><td>0.00 <b>(+62.88%)</b></td><td>591.40 <b>(+75.59%)</b></td><td>496.40 <b>(+71.34%)</b></td><td>550.60 <b>(+95.25%)</b></td><td>350.40 <b>(+31.19%)</b></td><td>108.51 <b>(+280.79%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>336.80 (n/a)</td><td>289.72 (n/a)</td><td>282.00 (n/a)</td><td>267.10 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-27.11%)</b></td><td>21787.24 (-2.90%)</td><td>15663.69 (-8.72%)</td><td>16749.45 (-2.91%)</td><td>8098.73 (+14.06%)</td><td>5160.68 (-16.75%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22437.57 (n/a)</td><td>17159.11 (n/a)</td><td>17251.15 (n/a)</td><td>7100.69 (n/a)</td><td>6198.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.00 <b>(-66.67%)</b></td><td>0.00 <b>(-44.12%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-86.33%)</b></td><td>23560.87 (+6.26%)</td><td>21104.47 <b>(+47.40%)</b></td><td>21601.61 <b>(+33.10%)</b></td><td>18233.21 <b>(+166.89%)</b></td><td>2320.96 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22173.59 (n/a)</td><td>14317.42 (n/a)</td><td>16229.00 (n/a)</td><td>6831.76 (n/a)</td><td>5999.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.13 (-3.16%)</td><td>0.09 (-2.01%)</td><td>0.08 (+4.62%)</td><td>0.07 (-0.13%)</td><td>0.02 (-11.81%)</td><td>28289.03 (+0.11%)</td><td>23560.57 (+0.87%)</td><td>25047.14 (-4.51%)</td><td>15906.19 (+3.20%)</td><td>4637.85 (-12.72%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28258.41 (n/a)</td><td>23356.93 (n/a)</td><td>26230.02 (n/a)</td><td>15412.93 (n/a)</td><td>5313.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.82 (-15.53%)</td><td>1.23 (-0.06%)</td><td>1.05 (+13.79%)</td><td>0.78 (+4.91%)</td><td>0.42 <b>(-26.70%)</b></td><td>676.00 (-4.68%)</td><td>466.86 (-5.19%)</td><td>500.70 (-12.11%)</td><td>287.40 (+18.42%)</td><td>153.36 (-17.20%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.16 (n/a)</td><td>1.23 (n/a)</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.58 (n/a)</td><td>709.20 (n/a)</td><td>492.42 (n/a)</td><td>569.70 (n/a)</td><td>242.70 (n/a)</td><td>185.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.37 (-19.36%)</td><td>1.15 (-17.55%)</td><td>1.13 (-8.40%)</td><td>0.31 (-2.20%)</td><td>0.84 (-12.67%)</td><td>3383.90 (+2.24%)</td><td>1582.72 <b>(+26.12%)</b></td><td>928.10 (+9.18%)</td><td>442.50 <b>(+24.02%)</b></td><td>1275.76 (+8.60%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.94 (n/a)</td><td>1.39 (n/a)</td><td>1.23 (n/a)</td><td>0.32 (n/a)</td><td>0.96 (n/a)</td><td>3309.60 (n/a)</td><td>1254.98 (n/a)</td><td>850.10 (n/a)</td><td>356.80 (n/a)</td><td>1174.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.78 (-19.63%)</td><td>1.36 <b>(+25.79%)</b></td><td>1.58 <b>(+66.10%)</b></td><td>0.69 <b>(+148.44%)</b></td><td>0.45 <b>(-36.24%)</b></td><td>755.20 <b>(-59.75%)</b></td><td>434.96 <b>(-41.82%)</b></td><td>332.30 <b>(-39.80%)</b></td><td>295.10 <b>(+24.41%)</b></td><td>191.54 <b>(-70.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.21 (n/a)</td><td>1.08 (n/a)</td><td>0.95 (n/a)</td><td>0.28 (n/a)</td><td>0.70 (n/a)</td><td>1876.20 (n/a)</td><td>747.66 (n/a)</td><td>552.00 (n/a)</td><td>237.20 (n/a)</td><td>644.86 (n/a)</td>
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
