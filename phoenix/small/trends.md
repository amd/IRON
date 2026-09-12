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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (+8.13%)</td><td>0.04 (+4.67%)</td><td>0.05 (+10.86%)</td><td>0.01 <b>(-73.16%)</b></td><td>0.02 <b>(+53.58%)</b></td><td>1935.40 <b>(+272.62%)</b></td><td>575.08 <b>(+74.40%)</b></td><td>245.20 (-9.79%)</td><td>203.30 (-7.55%)</td><td>760.66 <b>(+497.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.40 (n/a)</td><td>329.74 (n/a)</td><td>271.80 (n/a)</td><td>219.90 (n/a)</td><td>127.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (+5.82%)</td><td>0.05 <b>(+53.79%)</b></td><td>0.05 <b>(+60.30%)</b></td><td>0.04 <b>(+89.79%)</b></td><td>0.00 <b>(-60.34%)</b></td><td>283.90 <b>(-47.31%)</b></td><td>241.86 <b>(-39.62%)</b></td><td>232.50 <b>(-37.62%)</b></td><td>228.10 (-5.51%)</td><td>23.59 <b>(-80.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>400.54 (n/a)</td><td>372.70 (n/a)</td><td>241.40 (n/a)</td><td>119.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.07 <b>(+32.97%)</b></td><td>0.05 (+15.86%)</td><td>0.05 (+18.12%)</td><td>0.02 <b>(-23.94%)</b></td><td>0.02 <b>(+56.37%)</b></td><td>667.30 <b>(+31.49%)</b></td><td>328.42 (-3.36%)</td><td>249.80 (-15.35%)</td><td>177.20 <b>(-24.79%)</b></td><td>194.33 <b>(+70.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.50 (n/a)</td><td>339.84 (n/a)</td><td>295.10 (n/a)</td><td>235.60 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (+7.46%)</td><td>0.02 (+9.50%)</td><td>0.02 (-4.30%)</td><td>0.01 <b>(+296.83%)</b></td><td>0.01 <b>(-26.84%)</b></td><td>524.20 <b>(-74.80%)</b></td><td>319.24 <b>(-49.16%)</b></td><td>300.10 (+4.49%)</td><td>193.80 (-6.92%)</td><td>123.88 <b>(-84.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2080.30 (n/a)</td><td>627.90 (n/a)</td><td>287.20 (n/a)</td><td>208.20 (n/a)</td><td>812.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (+1.27%)</td><td>0.02 (+1.94%)</td><td>0.01 (+11.75%)</td><td>0.01 (-0.97%)</td><td>0.01 (-4.03%)</td><td>513.60 (+0.96%)</td><td>379.06 (-2.81%)</td><td>403.40 (-10.51%)</td><td>233.50 (-1.27%)</td><td>114.65 (-5.59%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.70 (n/a)</td><td>390.00 (n/a)</td><td>450.80 (n/a)</td><td>236.50 (n/a)</td><td>121.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 <b>(+40.52%)</b></td><td>0.02 (+0.00%)</td><td>0.01 <b>(-37.69%)</b></td><td>0.01 <b>(+40.90%)</b></td><td>0.01 <b>(+37.22%)</b></td><td>440.50 <b>(-29.02%)</b></td><td>360.94 (-1.88%)</td><td>415.50 <b>(+60.49%)</b></td><td>143.10 <b>(-28.81%)</b></td><td>124.06 <b>(-35.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>367.84 (n/a)</td><td>258.90 (n/a)</td><td>201.00 (n/a)</td><td>191.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (-8.50%)</td><td>0.01 <b>(-37.23%)</b></td><td>0.01 <b>(-44.12%)</b></td><td>0.01 <b>(-30.79%)</b></td><td>0.01 (+12.58%)</td><td>682.00 <b>(+44.49%)</b></td><td>503.96 <b>(+69.90%)</b></td><td>464.30 <b>(+78.99%)</b></td><td>243.40 (+9.30%)</td><td>180.94 <b>(+76.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.00 (n/a)</td><td>296.62 (n/a)</td><td>259.40 (n/a)</td><td>222.70 (n/a)</td><td>102.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (-5.81%)</td><td>0.01 (-9.41%)</td><td>0.01 <b>(-33.81%)</b></td><td>0.01 <b>(+29.44%)</b></td><td>0.00 <b>(-28.26%)</b></td><td>474.60 <b>(-22.74%)</b></td><td>387.50 (+1.64%)</td><td>455.10 <b>(+51.05%)</b></td><td>246.70 (+6.20%)</td><td>105.98 <b>(-38.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.30 (n/a)</td><td>381.24 (n/a)</td><td>301.30 (n/a)</td><td>232.30 (n/a)</td><td>172.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (+14.31%)</td><td>0.01 (-8.17%)</td><td>0.01 (-10.21%)</td><td>0.01 <b>(-29.88%)</b></td><td>0.00 <b>(+76.05%)</b></td><td>801.10 <b>(+42.62%)</b></td><td>544.84 (+16.61%)</td><td>539.60 (+11.37%)</td><td>319.80 (-12.53%)</td><td>181.57 <b>(+118.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.70 (n/a)</td><td>467.22 (n/a)</td><td>484.50 (n/a)</td><td>365.60 (n/a)</td><td>83.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.00 (n/a)</td><td>346.98 (n/a)</td><td>317.70 (n/a)</td><td>242.80 (n/a)</td><td>113.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>580.30 (n/a)</td><td>424.48 (n/a)</td><td>508.80 (n/a)</td><td>210.20 (n/a)</td><td>176.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.00 (n/a)</td><td>500.88 (n/a)</td><td>551.70 (n/a)</td><td>234.90 (n/a)</td><td>161.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>643.80 (n/a)</td><td>399.34 (n/a)</td><td>354.30 (n/a)</td><td>205.20 (n/a)</td><td>175.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>336.26 (n/a)</td><td>291.60 (n/a)</td><td>214.80 (n/a)</td><td>131.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.90 (n/a)</td><td>417.40 (n/a)</td><td>454.50 (n/a)</td><td>266.30 (n/a)</td><td>119.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.14 (-17.87%)</td><td>0.83 (+2.48%)</td><td>0.77 (+4.05%)</td><td>0.66 <b>(+45.56%)</b></td><td>0.18 <b>(-47.02%)</b></td><td>697.20 <b>(-31.30%)</b></td><td>568.74 (-11.08%)</td><td>593.60 (-3.90%)</td><td>402.90 <b>(+21.76%)</b></td><td>107.68 <b>(-55.85%)</b></td><td>83.28 (-17.87%)</td><td>60.99 (+2.48%)</td><td>56.53 (+4.05%)</td><td>48.12 <b>(+45.56%)</b></td><td>13.34 <b>(-47.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.39 (n/a)</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>1014.90 (n/a)</td><td>639.58 (n/a)</td><td>617.70 (n/a)</td><td>330.90 (n/a)</td><td>243.91 (n/a)</td><td>101.41 (n/a)</td><td>59.51 (n/a)</td><td>54.32 (n/a)</td><td>33.06 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.19 (-18.09%)</td><td>0.98 (-15.07%)</td><td>1.00 <b>(-25.24%)</b></td><td>0.64 <b>(+142.69%)</b></td><td>0.22 <b>(-56.69%)</b></td><td>1027.90 <b>(-58.79%)</b></td><td>702.24 <b>(-20.23%)</b></td><td>655.80 <b>(+33.75%)</b></td><td>548.80 <b>(+22.09%)</b></td><td>191.56 <b>(-78.78%)</b></td><td>122.29 (-18.09%)</td><td>100.34 (-15.07%)</td><td>102.34 <b>(-25.24%)</b></td><td>65.29 <b>(+142.69%)</b></td><td>22.20 <b>(-56.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.46 (n/a)</td><td>1.15 (n/a)</td><td>1.34 (n/a)</td><td>0.26 (n/a)</td><td>0.50 (n/a)</td><td>2494.60 (n/a)</td><td>880.34 (n/a)</td><td>490.30 (n/a)</td><td>449.50 (n/a)</td><td>902.56 (n/a)</td><td>149.30 (n/a)</td><td>118.14 (n/a)</td><td>136.89 (n/a)</td><td>26.90 (n/a)</td><td>51.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.62 (+2.62%)</td><td>1.44 (+16.38%)</td><td>1.47 <b>(+28.05%)</b></td><td>1.23 <b>(+24.66%)</b></td><td>0.15 <b>(-42.58%)</b></td><td>612.10 (-19.78%)</td><td>528.94 (-16.17%)</td><td>511.50 <b>(-21.91%)</b></td><td>464.30 (-2.56%)</td><td>56.39 <b>(-54.90%)</b></td><td>180.66 (+2.62%)</td><td>160.00 (+16.38%)</td><td>164.00 <b>(+28.05%)</b></td><td>137.06 <b>(+24.66%)</b></td><td>16.51 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.58 (n/a)</td><td>1.24 (n/a)</td><td>1.15 (n/a)</td><td>0.99 (n/a)</td><td>0.26 (n/a)</td><td>763.00 (n/a)</td><td>631.00 (n/a)</td><td>655.00 (n/a)</td><td>476.50 (n/a)</td><td>125.04 (n/a)</td><td>176.05 (n/a)</td><td>137.47 (n/a)</td><td>128.08 (n/a)</td><td>109.94 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.63 (+4.87%)</td><td>1.12 (-12.91%)</td><td>1.19 (-8.61%)</td><td>0.50 <b>(-47.58%)</b></td><td>0.41 <b>(+65.55%)</b></td><td>2087.80 <b>(+90.79%)</b></td><td>1090.96 <b>(+30.00%)</b></td><td>883.30 (+9.43%)</td><td>641.90 (-4.65%)</td><td>571.82 <b>(+232.37%)</b></td><td>209.08 (+4.87%)</td><td>143.77 (-12.91%)</td><td>151.96 (-8.61%)</td><td>64.29 <b>(-47.58%)</b></td><td>52.35 <b>(+65.55%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.56 (n/a)</td><td>1.29 (n/a)</td><td>1.30 (n/a)</td><td>0.96 (n/a)</td><td>0.25 (n/a)</td><td>1094.30 (n/a)</td><td>839.22 (n/a)</td><td>807.20 (n/a)</td><td>673.20 (n/a)</td><td>172.04 (n/a)</td><td>199.38 (n/a)</td><td>165.07 (n/a)</td><td>166.27 (n/a)</td><td>122.65 (n/a)</td><td>31.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.37 (+18.40%)</td><td>1.56 (+3.04%)</td><td>1.57 (+18.48%)</td><td>0.82 <b>(-36.27%)</b></td><td>0.56 <b>(+76.59%)</b></td><td>1283.70 <b>(+56.91%)</b></td><td>754.60 (+5.86%)</td><td>667.50 (-15.60%)</td><td>442.00 (-15.54%)</td><td>315.72 <b>(+141.10%)</b></td><td>303.69 (+18.40%)</td><td>200.10 (+3.04%)</td><td>201.07 (+18.48%)</td><td>104.56 <b>(-36.27%)</b></td><td>71.25 <b>(+76.59%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.00 (n/a)</td><td>1.52 (n/a)</td><td>1.33 (n/a)</td><td>1.28 (n/a)</td><td>0.32 (n/a)</td><td>818.10 (n/a)</td><td>712.80 (n/a)</td><td>790.90 (n/a)</td><td>523.30 (n/a)</td><td>130.95 (n/a)</td><td>256.49 (n/a)</td><td>194.20 (n/a)</td><td>169.71 (n/a)</td><td>164.05 (n/a)</td><td>40.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.51 <b>(+44.27%)</b></td><td>1.37 (-9.79%)</td><td>1.36 (-9.09%)</td><td>0.29 <b>(-77.29%)</b></td><td>1.07 <b>(+409.18%)</b></td><td>3559.40 <b>(+340.36%)</b></td><td>1740.54 <b>(+147.36%)</b></td><td>769.50 (+10.01%)</td><td>417.60 <b>(-30.69%)</b></td><td>1644.59 <b>(+1584.47%)</b></td><td>321.37 <b>(+44.27%)</b></td><td>174.75 (-9.79%)</td><td>174.42 (-9.09%)</td><td>37.71 <b>(-77.29%)</b></td><td>137.04 <b>(+409.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.74 (n/a)</td><td>1.51 (n/a)</td><td>1.50 (n/a)</td><td>1.30 (n/a)</td><td>0.21 (n/a)</td><td>808.30 (n/a)</td><td>703.66 (n/a)</td><td>699.50 (n/a)</td><td>602.50 (n/a)</td><td>97.63 (n/a)</td><td>222.76 (n/a)</td><td>193.73 (n/a)</td><td>191.87 (n/a)</td><td>166.06 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.94 (+18.77%)</td><td>1.56 <b>(+34.79%)</b></td><td>1.48 <b>(+23.85%)</b></td><td>1.22 <b>(+71.02%)</b></td><td>0.29 (-14.71%)</td><td>857.00 <b>(-41.53%)</b></td><td>691.34 <b>(-29.22%)</b></td><td>707.40 (-19.27%)</td><td>539.30 (-15.81%)</td><td>126.20 <b>(-59.30%)</b></td><td>248.85 (+18.77%)</td><td>199.50 <b>(+34.79%)</b></td><td>189.73 <b>(+23.85%)</b></td><td>156.62 <b>(+71.02%)</b></td><td>37.00 (-14.71%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.64 (n/a)</td><td>1.16 (n/a)</td><td>1.20 (n/a)</td><td>0.72 (n/a)</td><td>0.34 (n/a)</td><td>1465.60 (n/a)</td><td>976.74 (n/a)</td><td>876.20 (n/a)</td><td>640.60 (n/a)</td><td>310.11 (n/a)</td><td>209.53 (n/a)</td><td>148.00 (n/a)</td><td>153.19 (n/a)</td><td>91.58 (n/a)</td><td>43.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.11 (+4.85%)</td><td>0.71 (-9.70%)</td><td>0.62 (-10.94%)</td><td>0.52 (-10.29%)</td><td>0.24 (+9.94%)</td><td>694.90 (+11.47%)</td><td>545.52 (+12.45%)</td><td>584.40 (+12.28%)</td><td>325.10 (-4.61%)</td><td>147.23 (+17.17%)</td><td>51.61 (+4.85%)</td><td>33.11 (-9.70%)</td><td>28.71 (-10.94%)</td><td>24.14 (-10.29%)</td><td>11.14 (+9.94%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.06 (n/a)</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.58 (n/a)</td><td>0.22 (n/a)</td><td>623.40 (n/a)</td><td>485.12 (n/a)</td><td>520.50 (n/a)</td><td>340.80 (n/a)</td><td>125.66 (n/a)</td><td>49.22 (n/a)</td><td>36.67 (n/a)</td><td>32.24 (n/a)</td><td>26.91 (n/a)</td><td>10.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>4.24 (+7.65%)</td><td>2.99 (+10.47%)</td><td>3.22 (-10.45%)</td><td>1.07 (+1.35%)</td><td>1.20 (-14.17%)</td><td>2453.20 (-1.33%)</td><td>1109.72 (-16.01%)</td><td>814.40 (+11.67%)</td><td>618.10 (-7.09%)</td><td>760.71 (-11.68%)</td><td>868.64 (+7.65%)</td><td>612.57 (+10.47%)</td><td>659.21 (-10.45%)</td><td>218.84 (+1.35%)</td><td>246.58 (-14.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.94 (n/a)</td><td>2.71 (n/a)</td><td>3.59 (n/a)</td><td>1.05 (n/a)</td><td>1.40 (n/a)</td><td>2486.30 (n/a)</td><td>1321.18 (n/a)</td><td>729.30 (n/a)</td><td>665.30 (n/a)</td><td>861.29 (n/a)</td><td>806.91 (n/a)</td><td>554.50 (n/a)</td><td>736.10 (n/a)</td><td>215.94 (n/a)</td><td>287.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.80 (n/a)</td><td>348.24 (n/a)</td><td>337.90 (n/a)</td><td>229.50 (n/a)</td><td>114.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.10 (n/a)</td><td>390.30 (n/a)</td><td>394.20 (n/a)</td><td>234.30 (n/a)</td><td>159.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.50 (n/a)</td><td>429.80 (n/a)</td><td>422.80 (n/a)</td><td>347.20 (n/a)</td><td>87.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1823.10 (n/a)</td><td>687.74 (n/a)</td><td>485.50 (n/a)</td><td>292.20 (n/a)</td><td>641.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>385.52 (n/a)</td><td>429.20 (n/a)</td><td>216.90 (n/a)</td><td>140.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.10 (n/a)</td><td>424.84 (n/a)</td><td>419.50 (n/a)</td><td>240.10 (n/a)</td><td>135.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.56 (+7.63%)</td><td>0.48 <b>(+27.41%)</b></td><td>0.50 <b>(+23.53%)</b></td><td>0.37 <b>(+116.70%)</b></td><td>0.07 <b>(-44.46%)</b></td><td>594.90 <b>(-53.85%)</b></td><td>469.60 <b>(-30.78%)</b></td><td>438.30 (-19.04%)</td><td>393.10 (-7.09%)</td><td>77.56 <b>(-77.73%)</b></td><td>24.00 (+7.63%)</td><td>20.50 <b>(+27.41%)</b></td><td>21.53 <b>(+23.53%)</b></td><td>15.86 <b>(+116.70%)</b></td><td>3.07 <b>(-44.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>1289.10 (n/a)</td><td>678.42 (n/a)</td><td>541.40 (n/a)</td><td>423.10 (n/a)</td><td>348.29 (n/a)</td><td>22.30 (n/a)</td><td>16.09 (n/a)</td><td>17.43 (n/a)</td><td>7.32 (n/a)</td><td>5.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.57 (-11.05%)</td><td>0.45 (-8.63%)</td><td>0.40 (-11.89%)</td><td>0.38 (-4.63%)</td><td>0.09 (-11.25%)</td><td>585.50 (+4.87%)</td><td>505.14 (+9.26%)</td><td>551.80 (+13.52%)</td><td>389.70 (+12.44%)</td><td>94.63 (+5.84%)</td><td>24.22 (-11.05%)</td><td>19.26 (-8.63%)</td><td>17.10 (-11.89%)</td><td>16.12 (-4.63%)</td><td>3.87 (-11.25%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.64 (n/a)</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.10 (n/a)</td><td>558.30 (n/a)</td><td>462.34 (n/a)</td><td>486.10 (n/a)</td><td>346.60 (n/a)</td><td>89.42 (n/a)</td><td>27.23 (n/a)</td><td>21.08 (n/a)</td><td>19.41 (n/a)</td><td>16.90 (n/a)</td><td>4.37 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.31 (+1.51%)</td><td>0.31 (+0.03%)</td><td>0.31 (-0.28%)</td><td>0.30 (-0.03%)</td><td>0.00 <b>(+97.60%)</b></td><td>83063.20 (+0.03%)</td><td>82138.60 (-0.02%)</td><td>82139.80 (+0.28%)</td><td>80551.80 (-1.49%)</td><td>1005.26 <b>(+94.54%)</b></td><td>213.28 (+1.51%)</td><td>209.18 (+0.03%)</td><td>209.15 (-0.28%)</td><td>206.83 (-0.03%)</td><td>2.58 <b>(+97.60%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83040.00 (n/a)</td><td>82152.00 (n/a)</td><td>81907.90 (n/a)</td><td>81770.30 (n/a)</td><td>516.74 (n/a)</td><td>210.10 (n/a)</td><td>209.13 (n/a)</td><td>209.75 (n/a)</td><td>206.89 (n/a)</td><td>1.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.16 (-0.77%)</td><td>1.15 (+0.10%)</td><td>1.15 (+0.36%)</td><td>1.14 (+0.73%)</td><td>0.01 <b>(-46.04%)</b></td><td>22021.90 (-0.73%)</td><td>21891.10 (-0.11%)</td><td>21906.80 (-0.36%)</td><td>21659.60 (+0.78%)</td><td>138.99 <b>(-45.94%)</b></td><td>793.17 (-0.77%)</td><td>784.81 (+0.10%)</td><td>784.22 (+0.36%)</td><td>780.13 (+0.73%)</td><td>5.01 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.17 (n/a)</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>0.01 (n/a)</td><td>22183.50 (n/a)</td><td>21914.70 (n/a)</td><td>21986.70 (n/a)</td><td>21492.60 (n/a)</td><td>257.07 (n/a)</td><td>799.34 (n/a)</td><td>784.03 (n/a)</td><td>781.38 (n/a)</td><td>774.44 (n/a)</td><td>9.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.44 <b>(-41.72%)</b></td><td>1.97 <b>(-37.66%)</b></td><td>2.08 <b>(-34.89%)</b></td><td>1.38 <b>(-26.12%)</b></td><td>0.43 <b>(-50.77%)</b></td><td>5858.90 <b>(+35.36%)</b></td><td>4272.48 <b>(+55.20%)</b></td><td>3871.50 <b>(+53.58%)</b></td><td>3301.20 <b>(+71.57%)</b></td><td>1039.27 (+10.79%)</td><td>640.35 <b>(-41.72%)</b></td><td>516.47 <b>(-37.66%)</b></td><td>546.03 <b>(-34.89%)</b></td><td>360.81 <b>(-26.12%)</b></td><td>112.80 <b>(-50.77%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>4.19 (n/a)</td><td>3.16 (n/a)</td><td>3.20 (n/a)</td><td>1.86 (n/a)</td><td>0.87 (n/a)</td><td>4328.40 (n/a)</td><td>2752.82 (n/a)</td><td>2520.80 (n/a)</td><td>1924.10 (n/a)</td><td>938.05 (n/a)</td><td>1098.66 (n/a)</td><td>828.51 (n/a)</td><td>838.60 (n/a)</td><td>488.38 (n/a)</td><td>229.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.27 (+16.62%)</td><td>0.23 (+5.81%)</td><td>0.25 (+11.99%)</td><td>0.17 (-11.26%)</td><td>0.05 <b>(+167.55%)</b></td><td>7245.10 (+12.69%)</td><td>5691.38 (-2.40%)</td><td>4964.80 (-10.71%)</td><td>4594.90 (-14.25%)</td><td>1271.57 <b>(+158.73%)</b></td><td>14.61 (+16.62%)</td><td>12.25 (+5.81%)</td><td>13.52 (+11.99%)</td><td>9.26 (-11.26%)</td><td>2.54 <b>(+167.55%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>6429.30 (n/a)</td><td>5831.20 (n/a)</td><td>5560.20 (n/a)</td><td>5358.40 (n/a)</td><td>491.47 (n/a)</td><td>12.52 (n/a)</td><td>11.57 (n/a)</td><td>12.07 (n/a)</td><td>10.44 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.75 (n/a)</td><td>3.34 (n/a)</td><td>0.22 (n/a)</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.75 (n/a)</td><td>3.34 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>5.94 <b>(-22.05%)</b></td><td>5.75 (-12.56%)</td><td>5.67 <b>(-22.73%)</b></td><td>5.59 <b>(+22.44%)</b></td><td>0.17 <b>(-87.70%)</b></td><td>5.94 <b>(-22.05%)</b></td><td>5.75 (-12.56%)</td><td>5.67 <b>(-22.73%)</b></td><td>5.58 <b>(+22.44%)</b></td><td>0.17 <b>(-87.70%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>7.62 (n/a)</td><td>6.58 (n/a)</td><td>7.34 (n/a)</td><td>4.56 (n/a)</td><td>1.34 (n/a)</td><td>7.62 (n/a)</td><td>6.58 (n/a)</td><td>7.34 (n/a)</td><td>4.56 (n/a)</td><td>1.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>13.81 (-0.31%)</td><td>10.50 (-2.88%)</td><td>9.73 (-5.24%)</td><td>8.21 (-0.07%)</td><td>2.10 <b>(-21.77%)</b></td><td>13.80 (-0.31%)</td><td>10.50 (-2.88%)</td><td>9.72 (-5.24%)</td><td>8.20 (-0.07%)</td><td>2.10 <b>(-21.77%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>13.85 (n/a)</td><td>10.81 (n/a)</td><td>10.27 (n/a)</td><td>8.21 (n/a)</td><td>2.69 (n/a)</td><td>13.85 (n/a)</td><td>10.81 (n/a)</td><td>10.26 (n/a)</td><td>8.21 (n/a)</td><td>2.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>3.84 (n/a)</td><td>3.76 (n/a)</td><td>3.75 (n/a)</td><td>3.69 (n/a)</td><td>0.06 (n/a)</td><td>3.84 (n/a)</td><td>3.76 (n/a)</td><td>3.75 (n/a)</td><td>3.68 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>7.43 (-1.87%)</td><td>6.98 (+0.66%)</td><td>6.80 (-5.49%)</td><td>6.68 (+15.13%)</td><td>0.33 <b>(-56.29%)</b></td><td>7.43 (-1.87%)</td><td>6.97 (+0.66%)</td><td>6.80 (-5.49%)</td><td>6.68 (+15.13%)</td><td>0.33 <b>(-56.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>7.57 (n/a)</td><td>6.93 (n/a)</td><td>7.20 (n/a)</td><td>5.80 (n/a)</td><td>0.76 (n/a)</td><td>7.57 (n/a)</td><td>6.93 (n/a)</td><td>7.19 (n/a)</td><td>5.80 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>13.92 (+1.16%)</td><td>10.40 (-9.97%)</td><td>8.60 <b>(-35.85%)</b></td><td>7.90 (-4.97%)</td><td>2.97 (+4.99%)</td><td>13.91 (+1.16%)</td><td>10.40 (-9.97%)</td><td>8.60 <b>(-35.85%)</b></td><td>7.90 (-4.97%)</td><td>2.97 (+4.99%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>13.76 (n/a)</td><td>11.56 (n/a)</td><td>13.41 (n/a)</td><td>8.32 (n/a)</td><td>2.83 (n/a)</td><td>13.75 (n/a)</td><td>11.55 (n/a)</td><td>13.41 (n/a)</td><td>8.31 (n/a)</td><td>2.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.70 (-17.92%)</td><td>2.16 <b>(-27.76%)</b></td><td>2.36 <b>(-21.21%)</b></td><td>1.41 <b>(-48.65%)</b></td><td>0.57 <b>(+157.09%)</b></td><td>2.70 (-17.92%)</td><td>2.15 <b>(-27.76%)</b></td><td>2.35 <b>(-21.21%)</b></td><td>1.41 <b>(-48.65%)</b></td><td>0.57 <b>(+157.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>3.29 (n/a)</td><td>2.98 (n/a)</td><td>2.99 (n/a)</td><td>2.75 (n/a)</td><td>0.22 (n/a)</td><td>3.29 (n/a)</td><td>2.98 (n/a)</td><td>2.99 (n/a)</td><td>2.74 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.51 (-13.69%)</td><td>0.40 (-15.08%)</td><td>0.40 <b>(-24.64%)</b></td><td>0.32 (-6.80%)</td><td>0.07 <b>(-40.29%)</b></td><td>0.50 (-13.69%)</td><td>0.40 (-15.08%)</td><td>0.39 <b>(-24.64%)</b></td><td>0.32 (-6.80%)</td><td>0.06 <b>(-40.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.81 (+11.21%)</td><td>0.49 <b>(-22.15%)</b></td><td>0.71 (+4.44%)</td><td>0.08 <b>(-80.86%)</b></td><td>0.38 <b>(+187.60%)</b></td><td>0.80 (+11.21%)</td><td>0.49 <b>(-22.15%)</b></td><td>0.71 (+4.44%)</td><td>0.08 <b>(-80.86%)</b></td><td>0.38 <b>(+187.60%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.73 (n/a)</td><td>0.63 (n/a)</td><td>0.68 (n/a)</td><td>0.40 (n/a)</td><td>0.13 (n/a)</td><td>0.72 (n/a)</td><td>0.62 (n/a)</td><td>0.68 (n/a)</td><td>0.40 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.50 (+1.70%)</td><td>1.58 (-1.50%)</td><td>1.60 (-16.69%)</td><td>0.73 (-4.11%)</td><td>0.67 (-12.57%)</td><td>2.46 (+1.70%)</td><td>1.56 (-1.50%)</td><td>1.57 (-16.69%)</td><td>0.72 (-4.11%)</td><td>0.66 (-12.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.46 (n/a)</td><td>1.61 (n/a)</td><td>1.92 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>2.42 (n/a)</td><td>1.58 (n/a)</td><td>1.89 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>334.30 (n/a)</td><td>300.10 (n/a)</td><td>270.30 (n/a)</td><td>92.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>393.36 (n/a)</td><td>442.00 (n/a)</td><td>223.00 (n/a)</td><td>133.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.60 (n/a)</td><td>416.12 (n/a)</td><td>437.00 (n/a)</td><td>203.10 (n/a)</td><td>128.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.20 (n/a)</td><td>354.02 (n/a)</td><td>298.10 (n/a)</td><td>234.20 (n/a)</td><td>139.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.50 (n/a)</td><td>447.18 (n/a)</td><td>560.70 (n/a)</td><td>234.30 (n/a)</td><td>195.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>433.50 (n/a)</td><td>388.90 (n/a)</td><td>312.30 (n/a)</td><td>108.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (+11.31%)</td><td>0.03 (+17.49%)</td><td>0.03 (+12.07%)</td><td>0.01 (+3.81%)</td><td>0.01 (+6.74%)</td><td>554.10 (-3.65%)</td><td>319.66 (-14.57%)</td><td>255.40 (-10.76%)</td><td>242.10 (-10.17%)</td><td>132.71 (-2.34%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>374.16 (n/a)</td><td>286.20 (n/a)</td><td>269.50 (n/a)</td><td>135.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 <b>(-21.03%)</b></td><td>0.02 (-11.76%)</td><td>0.02 (+13.55%)</td><td>0.01 <b>(-48.87%)</b></td><td>0.01 (-11.00%)</td><td>1052.70 <b>(+95.60%)</b></td><td>502.16 <b>(+25.03%)</b></td><td>393.50 (-11.93%)</td><td>292.90 <b>(+26.63%)</b></td><td>313.16 <b>(+135.55%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.20 (n/a)</td><td>401.62 (n/a)</td><td>446.80 (n/a)</td><td>231.30 (n/a)</td><td>132.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (-16.25%)</td><td>0.02 (-13.78%)</td><td>0.02 (-1.66%)</td><td>0.01 (-13.42%)</td><td>0.01 (-18.55%)</td><td>585.70 (+15.50%)</td><td>389.08 (+15.41%)</td><td>345.80 (+1.71%)</td><td>244.30 (+19.40%)</td><td>147.08 (+16.70%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.10 (n/a)</td><td>337.12 (n/a)</td><td>340.00 (n/a)</td><td>204.60 (n/a)</td><td>126.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (-7.97%)</td><td>0.02 (+5.11%)</td><td>0.02 (+13.41%)</td><td>0.01 (+5.94%)</td><td>0.01 (-17.89%)</td><td>562.40 (-5.61%)</td><td>426.16 (-7.76%)</td><td>436.80 (-11.81%)</td><td>240.80 (+8.66%)</td><td>128.21 (-9.41%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.80 (n/a)</td><td>462.02 (n/a)</td><td>495.30 (n/a)</td><td>221.60 (n/a)</td><td>141.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (+13.28%)</td><td>0.03 (-4.12%)</td><td>0.03 (-12.92%)</td><td>0.02 <b>(+24.40%)</b></td><td>0.01 (+14.37%)</td><td>511.90 (-19.61%)</td><td>344.02 (+2.67%)</td><td>304.60 (+14.81%)</td><td>212.90 (-11.73%)</td><td>130.95 <b>(-22.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.80 (n/a)</td><td>335.08 (n/a)</td><td>265.30 (n/a)</td><td>241.20 (n/a)</td><td>169.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 <b>(+32.20%)</b></td><td>0.02 <b>(+42.98%)</b></td><td>0.02 (+16.34%)</td><td>0.01 <b>(+240.48%)</b></td><td>0.01 (-11.49%)</td><td>603.30 <b>(-70.63%)</b></td><td>454.68 <b>(-56.39%)</b></td><td>493.90 (-14.06%)</td><td>227.90 <b>(-24.34%)</b></td><td>138.89 <b>(-83.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2054.10 (n/a)</td><td>1042.72 (n/a)</td><td>574.70 (n/a)</td><td>301.20 (n/a)</td><td>855.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 <b>(-22.11%)</b></td><td>0.02 (+6.90%)</td><td>0.02 <b>(+23.83%)</b></td><td>0.00 <b>(-21.88%)</b></td><td>0.01 (-17.03%)</td><td>2350.80 <b>(+28.01%)</b></td><td>787.64 (+5.40%)</td><td>467.90 (-19.24%)</td><td>291.00 <b>(+28.42%)</b></td><td>878.71 <b>(+40.23%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1836.40 (n/a)</td><td>747.30 (n/a)</td><td>579.40 (n/a)</td><td>226.60 (n/a)</td><td>626.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 <b>(-49.60%)</b></td><td>0.02 (-17.71%)</td><td>0.01 (-12.15%)</td><td>0.01 <b>(+61.10%)</b></td><td>0.00 <b>(-77.78%)</b></td><td>609.70 <b>(-37.92%)</b></td><td>528.18 (-5.52%)</td><td>551.50 (+13.83%)</td><td>397.60 <b>(+98.40%)</b></td><td>81.39 <b>(-71.99%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>982.10 (n/a)</td><td>559.04 (n/a)</td><td>484.50 (n/a)</td><td>200.40 (n/a)</td><td>290.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (-5.75%)</td><td>0.02 <b>(+22.59%)</b></td><td>0.03 <b>(+44.47%)</b></td><td>0.01 <b>(+240.88%)</b></td><td>0.01 <b>(-36.11%)</b></td><td>581.10 <b>(-70.66%)</b></td><td>359.02 <b>(-47.80%)</b></td><td>291.70 <b>(-30.78%)</b></td><td>256.50 (+6.08%)</td><td>134.20 <b>(-81.62%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1980.80 (n/a)</td><td>687.82 (n/a)</td><td>421.40 (n/a)</td><td>241.80 (n/a)</td><td>730.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 <b>(+23.33%)</b></td><td>0.03 (-2.14%)</td><td>0.03 (-1.66%)</td><td>0.02 <b>(-23.20%)</b></td><td>0.01 <b>(+84.32%)</b></td><td>546.10 <b>(+30.21%)</b></td><td>337.08 (+10.06%)</td><td>303.30 (+1.68%)</td><td>205.80 (-18.91%)</td><td>130.22 <b>(+95.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>419.40 (n/a)</td><td>306.26 (n/a)</td><td>298.30 (n/a)</td><td>253.80 (n/a)</td><td>66.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (-4.13%)</td><td>0.02 (-18.45%)</td><td>0.02 (-18.12%)</td><td>0.02 (-13.15%)</td><td>0.01 (+2.70%)</td><td>488.40 (+15.13%)</td><td>353.72 <b>(+24.16%)</b></td><td>334.40 <b>(+22.13%)</b></td><td>226.30 (+4.33%)</td><td>100.35 <b>(+21.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>424.20 (n/a)</td><td>284.88 (n/a)</td><td>273.80 (n/a)</td><td>216.90 (n/a)</td><td>82.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 <b>(+20.97%)</b></td><td>0.03 (+6.86%)</td><td>0.03 (+9.07%)</td><td>0.02 <b>(+26.35%)</b></td><td>0.01 <b>(+40.77%)</b></td><td>544.20 <b>(-20.86%)</b></td><td>360.76 (-3.30%)</td><td>279.50 (-8.30%)</td><td>211.00 (-17.35%)</td><td>161.77 (-8.99%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.60 (n/a)</td><td>373.08 (n/a)</td><td>304.80 (n/a)</td><td>255.30 (n/a)</td><td>177.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 <b>(+79.44%)</b></td><td>0.03 <b>(+68.59%)</b></td><td>0.03 <b>(+89.48%)</b></td><td>0.02 <b>(+27.34%)</b></td><td>0.01 <b>(+116.74%)</b></td><td>500.90 <b>(-21.48%)</b></td><td>329.48 <b>(-36.62%)</b></td><td>290.10 <b>(-47.23%)</b></td><td>170.60 <b>(-44.27%)</b></td><td>126.57 (+0.03%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>519.84 (n/a)</td><td>549.70 (n/a)</td><td>306.10 (n/a)</td><td>126.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (+3.02%)</td><td>0.02 (+19.61%)</td><td>0.02 <b>(+40.36%)</b></td><td>0.02 <b>(+21.86%)</b></td><td>0.01 <b>(-21.81%)</b></td><td>480.70 (-17.94%)</td><td>354.38 <b>(-20.26%)</b></td><td>338.50 <b>(-28.77%)</b></td><td>264.70 (-2.93%)</td><td>86.54 <b>(-38.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.80 (n/a)</td><td>444.44 (n/a)</td><td>475.20 (n/a)</td><td>272.70 (n/a)</td><td>141.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.10 (-2.90%)</td><td>0.08 (+0.77%)</td><td>0.08 (+7.89%)</td><td>0.06 (+2.02%)</td><td>0.01 <b>(-30.58%)</b></td><td>381.90 (-1.98%)</td><td>313.60 (-2.81%)</td><td>310.40 (-7.32%)</td><td>249.70 (+2.97%)</td><td>48.42 <b>(-30.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>389.60 (n/a)</td><td>322.66 (n/a)</td><td>334.90 (n/a)</td><td>242.50 (n/a)</td><td>70.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.16 (-0.85%)</td><td>0.10 (+3.19%)</td><td>0.07 (-12.13%)</td><td>0.02 (-1.52%)</td><td>0.06 (+13.42%)</td><td>1925.20 (+1.54%)</td><td>727.74 (+2.22%)</td><td>555.90 (+13.80%)</td><td>250.80 (+0.84%)</td><td>692.45 (+2.35%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1896.00 (n/a)</td><td>711.94 (n/a)</td><td>488.50 (n/a)</td><td>248.70 (n/a)</td><td>676.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (+4.65%)</td><td>0.02 <b>(+29.95%)</b></td><td>0.02 <b>(+84.64%)</b></td><td>0.01 <b>(+78.68%)</b></td><td>0.00 <b>(-45.52%)</b></td><td>394.10 <b>(-44.04%)</b></td><td>316.98 <b>(-32.57%)</b></td><td>294.60 <b>(-45.85%)</b></td><td>252.30 (-4.43%)</td><td>63.40 <b>(-67.60%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>704.20 (n/a)</td><td>470.10 (n/a)</td><td>544.00 (n/a)</td><td>264.00 (n/a)</td><td>195.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (+8.42%)</td><td>0.03 <b>(+25.64%)</b></td><td>0.03 <b>(+35.62%)</b></td><td>0.01 (-11.12%)</td><td>0.01 (+19.80%)</td><td>592.90 (+12.50%)</td><td>319.44 (-17.32%)</td><td>250.40 <b>(-26.27%)</b></td><td>230.90 (-7.75%)</td><td>154.07 <b>(+22.49%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>386.34 (n/a)</td><td>339.60 (n/a)</td><td>250.30 (n/a)</td><td>125.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (+16.31%)</td><td>0.04 (+3.75%)</td><td>0.04 (-15.58%)</td><td>0.03 <b>(+49.66%)</b></td><td>0.01 <b>(-22.58%)</b></td><td>424.60 <b>(-33.19%)</b></td><td>314.12 (-12.47%)</td><td>302.70 (+18.47%)</td><td>204.60 (-14.03%)</td><td>79.61 <b>(-54.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>635.50 (n/a)</td><td>358.88 (n/a)</td><td>255.50 (n/a)</td><td>238.00 (n/a)</td><td>173.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (-10.59%)</td><td>0.03 (+4.68%)</td><td>0.03 <b>(+31.75%)</b></td><td>0.02 <b>(+32.30%)</b></td><td>0.01 <b>(-34.31%)</b></td><td>435.90 <b>(-24.41%)</b></td><td>328.54 (-11.30%)</td><td>302.60 <b>(-24.10%)</b></td><td>242.30 (+11.81%)</td><td>84.46 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.70 (n/a)</td><td>370.40 (n/a)</td><td>398.70 (n/a)</td><td>216.70 (n/a)</td><td>144.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (+8.63%)</td><td>0.03 (+8.73%)</td><td>0.02 (-14.01%)</td><td>0.02 (+6.01%)</td><td>0.01 <b>(+25.22%)</b></td><td>534.60 (-5.66%)</td><td>382.28 (-3.76%)</td><td>435.10 (+16.31%)</td><td>196.80 (-7.95%)</td><td>150.44 (+12.27%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>397.22 (n/a)</td><td>374.10 (n/a)</td><td>213.80 (n/a)</td><td>133.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (-8.48%)</td><td>0.03 <b>(+45.28%)</b></td><td>0.03 <b>(+95.01%)</b></td><td>0.02 <b>(+26.99%)</b></td><td>0.01 <b>(-29.04%)</b></td><td>449.10 <b>(-21.25%)</b></td><td>277.50 <b>(-35.92%)</b></td><td>241.10 <b>(-48.72%)</b></td><td>210.60 (+9.29%)</td><td>98.43 <b>(-30.92%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.30 (n/a)</td><td>433.06 (n/a)</td><td>470.20 (n/a)</td><td>192.70 (n/a)</td><td>142.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 <b>(-22.12%)</b></td><td>0.03 (-10.25%)</td><td>0.02 (+2.01%)</td><td>0.02 (+8.49%)</td><td>0.01 <b>(-41.31%)</b></td><td>537.90 (-7.81%)</td><td>419.98 (+3.00%)</td><td>458.90 (-1.97%)</td><td>300.90 <b>(+28.37%)</b></td><td>109.48 <b>(-29.84%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.50 (n/a)</td><td>407.76 (n/a)</td><td>468.10 (n/a)</td><td>234.40 (n/a)</td><td>156.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (+7.64%)</td><td>0.03 <b>(+70.63%)</b></td><td>0.03 <b>(+111.69%)</b></td><td>0.02 <b>(+379.81%)</b></td><td>0.01 <b>(-38.63%)</b></td><td>395.60 <b>(-79.16%)</b></td><td>267.44 <b>(-62.89%)</b></td><td>249.80 <b>(-52.76%)</b></td><td>190.80 (-7.06%)</td><td>77.45 <b>(-88.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1898.10 (n/a)</td><td>720.58 (n/a)</td><td>528.80 (n/a)</td><td>205.30 (n/a)</td><td>674.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 <b>(+26.78%)</b></td><td>0.03 <b>(+24.22%)</b></td><td>0.02 <b>(+22.77%)</b></td><td>0.02 <b>(+27.68%)</b></td><td>0.01 <b>(+27.62%)</b></td><td>510.40 <b>(-21.68%)</b></td><td>384.02 (-19.31%)</td><td>440.90 (-18.55%)</td><td>210.70 <b>(-21.12%)</b></td><td>127.21 (-20.00%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.70 (n/a)</td><td>475.94 (n/a)</td><td>541.30 (n/a)</td><td>267.10 (n/a)</td><td>159.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (-7.77%)</td><td>0.02 (-16.84%)</td><td>0.02 <b>(-22.78%)</b></td><td>0.00 <b>(-77.09%)</b></td><td>0.01 <b>(+25.10%)</b></td><td>2413.90 <b>(+336.43%)</b></td><td>787.06 <b>(+108.38%)</b></td><td>460.40 <b>(+29.51%)</b></td><td>212.20 (+8.43%)</td><td>920.92 <b>(+518.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.10 (n/a)</td><td>377.70 (n/a)</td><td>355.50 (n/a)</td><td>195.70 (n/a)</td><td>149.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (+10.69%)</td><td>0.03 (+9.84%)</td><td>0.03 <b>(+34.65%)</b></td><td>0.02 (+3.35%)</td><td>0.01 (-2.45%)</td><td>513.00 (-3.24%)</td><td>366.58 (-10.03%)</td><td>349.30 <b>(-25.73%)</b></td><td>244.90 (-9.66%)</td><td>109.70 (-10.96%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.20 (n/a)</td><td>407.46 (n/a)</td><td>470.30 (n/a)</td><td>271.10 (n/a)</td><td>123.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (+6.29%)</td><td>0.02 (-17.35%)</td><td>0.02 <b>(-41.03%)</b></td><td>0.01 (+19.57%)</td><td>0.01 (-10.36%)</td><td>663.00 (-16.37%)</td><td>482.40 (+8.25%)</td><td>522.20 <b>(+69.60%)</b></td><td>205.80 (-5.94%)</td><td>169.50 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>792.80 (n/a)</td><td>445.64 (n/a)</td><td>307.90 (n/a)</td><td>218.80 (n/a)</td><td>267.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.57 <b>(+22.37%)</b></td><td>0.35 (+13.76%)</td><td>0.32 (-7.46%)</td><td>0.17 (+2.35%)</td><td>0.15 <b>(+22.83%)</b></td><td>580.30 (-2.29%)</td><td>327.26 (-10.50%)</td><td>309.10 (+8.08%)</td><td>171.50 (-18.29%)</td><td>152.92 (-1.81%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>593.90 (n/a)</td><td>365.66 (n/a)</td><td>286.00 (n/a)</td><td>209.90 (n/a)</td><td>155.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.39 (-1.50%)</td><td>0.32 (+5.19%)</td><td>0.36 (+5.13%)</td><td>0.18 (-14.57%)</td><td>0.08 (-8.10%)</td><td>552.60 (+17.08%)</td><td>328.54 (-4.59%)</td><td>276.80 (-4.88%)</td><td>255.00 (+1.51%)</td><td>125.79 (+13.93%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>472.00 (n/a)</td><td>344.36 (n/a)</td><td>291.00 (n/a)</td><td>251.20 (n/a)</td><td>110.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.42 <b>(+27.87%)</b></td><td>0.31 <b>(+47.00%)</b></td><td>0.36 <b>(+89.38%)</b></td><td>0.16 (+2.70%)</td><td>0.12 <b>(+76.57%)</b></td><td>598.10 (-2.64%)</td><td>372.60 <b>(-25.54%)</b></td><td>270.80 <b>(-47.20%)</b></td><td>232.60 <b>(-21.79%)</b></td><td>172.45 <b>(+38.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>614.30 (n/a)</td><td>500.38 (n/a)</td><td>512.90 (n/a)</td><td>297.40 (n/a)</td><td>124.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.28 <b>(-34.92%)</b></td><td>0.23 (-6.63%)</td><td>0.26 (-0.28%)</td><td>0.12 (+2.02%)</td><td>0.06 <b>(-49.10%)</b></td><td>602.20 (-1.97%)</td><td>348.02 (-4.42%)</td><td>287.80 (+0.31%)</td><td>261.50 <b>(+53.64%)</b></td><td>142.91 <b>(-21.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>614.30 (n/a)</td><td>364.10 (n/a)</td><td>286.90 (n/a)</td><td>170.20 (n/a)</td><td>182.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.33 <b>(+31.59%)</b></td><td>0.22 (+1.79%)</td><td>0.23 (-1.01%)</td><td>0.13 (-11.24%)</td><td>0.08 <b>(+79.93%)</b></td><td>559.30 (+12.67%)</td><td>367.56 (+4.72%)</td><td>320.90 (+1.01%)</td><td>221.10 <b>(-23.99%)</b></td><td>133.18 <b>(+55.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>496.40 (n/a)</td><td>350.98 (n/a)</td><td>317.70 (n/a)</td><td>290.90 (n/a)</td><td>85.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.31 (+11.03%)</td><td>0.26 <b>(+46.22%)</b></td><td>0.29 <b>(+92.36%)</b></td><td>0.15 <b>(+107.63%)</b></td><td>0.07 <b>(-21.97%)</b></td><td>499.90 <b>(-51.84%)</b></td><td>311.26 <b>(-41.58%)</b></td><td>257.50 <b>(-48.02%)</b></td><td>241.70 (-9.91%)</td><td>109.10 <b>(-64.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1038.00 (n/a)</td><td>532.84 (n/a)</td><td>495.40 (n/a)</td><td>268.30 (n/a)</td><td>309.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.44 (-5.91%)</td><td>0.30 (-9.62%)</td><td>0.26 <b>(-34.37%)</b></td><td>0.25 <b>(+35.02%)</b></td><td>0.08 <b>(-37.58%)</b></td><td>522.50 <b>(-25.94%)</b></td><td>461.86 (-0.46%)</td><td>512.60 <b>(+52.38%)</b></td><td>298.00 (+6.28%)</td><td>95.87 <b>(-53.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>705.50 (n/a)</td><td>464.00 (n/a)</td><td>336.40 (n/a)</td><td>280.40 (n/a)</td><td>208.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.64 (+11.78%)</td><td>0.29 (-2.94%)</td><td>0.23 (-3.97%)</td><td>0.08 <b>(-63.46%)</b></td><td>0.21 <b>(+37.35%)</b></td><td>1664.40 <b>(+173.61%)</b></td><td>708.26 <b>(+39.77%)</b></td><td>579.50 (+4.13%)</td><td>206.40 (-10.53%)</td><td>560.22 <b>(+258.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.57 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>608.30 (n/a)</td><td>506.72 (n/a)</td><td>556.50 (n/a)</td><td>230.70 (n/a)</td><td>156.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.42 (-0.66%)</td><td>0.32 (+0.70%)</td><td>0.37 (+6.43%)</td><td>0.21 (-3.71%)</td><td>0.09 (+8.33%)</td><td>611.80 (+3.85%)</td><td>434.54 (+0.56%)</td><td>356.30 (-6.04%)</td><td>314.70 (+0.67%)</td><td>133.78 (+12.39%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>589.10 (n/a)</td><td>432.14 (n/a)</td><td>379.20 (n/a)</td><td>312.60 (n/a)</td><td>119.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (+11.69%)</td><td>0.01 (-17.22%)</td><td>0.01 <b>(-35.85%)</b></td><td>0.01 <b>(-36.90%)</b></td><td>0.01 <b>(+98.01%)</b></td><td>585.20 <b>(+58.50%)</b></td><td>398.48 <b>(+38.89%)</b></td><td>413.40 <b>(+55.94%)</b></td><td>198.10 (-10.44%)</td><td>169.62 <b>(+181.46%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>369.20 (n/a)</td><td>286.90 (n/a)</td><td>265.10 (n/a)</td><td>221.20 (n/a)</td><td>60.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (-9.21%)</td><td>0.01 (-7.60%)</td><td>0.01 (+3.51%)</td><td>0.01 (-12.98%)</td><td>0.00 (-2.40%)</td><td>555.80 (+14.91%)</td><td>379.68 (+10.50%)</td><td>284.60 (-3.39%)</td><td>248.50 (+10.10%)</td><td>153.89 <b>(+23.92%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.70 (n/a)</td><td>343.60 (n/a)</td><td>294.60 (n/a)</td><td>225.70 (n/a)</td><td>124.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (-8.44%)</td><td>0.01 <b>(-27.07%)</b></td><td>0.01 <b>(-34.16%)</b></td><td>0.01 (-13.33%)</td><td>0.00 (-8.56%)</td><td>613.10 (+15.37%)</td><td>449.88 <b>(+36.72%)</b></td><td>449.90 <b>(+51.89%)</b></td><td>265.80 (+9.25%)</td><td>125.41 (+6.72%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.40 (n/a)</td><td>329.06 (n/a)</td><td>296.20 (n/a)</td><td>243.30 (n/a)</td><td>117.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.55 <b>(+23.52%)</b></td><td>0.44 <b>(+44.36%)</b></td><td>0.49 <b>(+100.73%)</b></td><td>0.15 (-9.98%)</td><td>0.16 <b>(+30.96%)</b></td><td>855.40 (+11.09%)</td><td>379.36 <b>(-23.77%)</b></td><td>267.40 <b>(-50.19%)</b></td><td>242.20 (-19.02%)</td><td>266.56 <b>(+34.62%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>770.00 (n/a)</td><td>497.66 (n/a)</td><td>536.80 (n/a)</td><td>299.10 (n/a)</td><td>198.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.50 (-6.02%)</td><td>0.39 (-13.81%)</td><td>0.48 (-2.88%)</td><td>0.06 <b>(-78.11%)</b></td><td>0.19 <b>(+98.71%)</b></td><td>2050.20 <b>(+356.72%)</b></td><td>632.38 <b>(+109.00%)</b></td><td>277.70 (+2.97%)</td><td>265.70 (+6.41%)</td><td>792.67 <b>(+860.77%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>448.90 (n/a)</td><td>302.58 (n/a)</td><td>269.70 (n/a)</td><td>249.70 (n/a)</td><td>82.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.59 <b>(-26.78%)</b></td><td>0.38 <b>(-23.38%)</b></td><td>0.29 <b>(-39.29%)</b></td><td>0.26 (-8.70%)</td><td>0.15 <b>(-26.60%)</b></td><td>505.30 (+9.54%)</td><td>387.80 <b>(+28.50%)</b></td><td>459.90 <b>(+64.72%)</b></td><td>222.50 <b>(+36.50%)</b></td><td>127.29 (+12.62%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.81 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>461.30 (n/a)</td><td>301.78 (n/a)</td><td>279.20 (n/a)</td><td>163.00 (n/a)</td><td>113.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.56 (+10.54%)</td><td>0.39 (-5.55%)</td><td>0.44 (-10.43%)</td><td>0.24 (-9.08%)</td><td>0.14 (+18.81%)</td><td>550.60 (+9.99%)</td><td>377.50 (+9.94%)</td><td>302.30 (+11.63%)</td><td>235.40 (-9.53%)</td><td>144.65 <b>(+29.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>500.60 (n/a)</td><td>343.36 (n/a)</td><td>270.80 (n/a)</td><td>260.20 (n/a)</td><td>111.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.49 <b>(-21.02%)</b></td><td>0.34 <b>(-21.14%)</b></td><td>0.36 <b>(-23.37%)</b></td><td>0.07 <b>(-72.79%)</b></td><td>0.16 (+6.45%)</td><td>1889.30 <b>(+267.50%)</b></td><td>645.26 <b>(+87.02%)</b></td><td>372.00 <b>(+30.48%)</b></td><td>269.80 <b>(+26.61%)</b></td><td>697.55 <b>(+425.33%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.62 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>514.10 (n/a)</td><td>345.02 (n/a)</td><td>285.10 (n/a)</td><td>213.10 (n/a)</td><td>132.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (-5.67%)</td><td>0.01 (-7.32%)</td><td>0.01 (-8.77%)</td><td>0.01 (+5.96%)</td><td>0.00 (-3.77%)</td><td>482.20 (-5.64%)</td><td>367.14 (+7.53%)</td><td>327.50 (+9.61%)</td><td>265.00 (+6.00%)</td><td>99.14 (-3.26%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.00 (n/a)</td><td>341.42 (n/a)</td><td>298.80 (n/a)</td><td>250.00 (n/a)</td><td>102.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 <b>(+52.08%)</b></td><td>0.01 <b>(+55.79%)</b></td><td>0.01 <b>(+82.37%)</b></td><td>0.01 <b>(+30.40%)</b></td><td>0.00 <b>(+47.61%)</b></td><td>453.60 <b>(-23.30%)</b></td><td>319.80 <b>(-35.58%)</b></td><td>301.90 <b>(-45.17%)</b></td><td>230.40 <b>(-34.25%)</b></td><td>81.90 <b>(-24.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.40 (n/a)</td><td>496.40 (n/a)</td><td>550.60 (n/a)</td><td>350.40 (n/a)</td><td>108.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.00 <b>(+60.00%)</b></td><td>0.00 <b>(+28.57%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+92.51%)</b></td><td>19965.95 (-8.36%)</td><td>14588.16 (-6.87%)</td><td>15380.78 (-8.17%)</td><td>5444.28 <b>(-32.78%)</b></td><td>5460.65 (+5.81%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21787.24 (n/a)</td><td>15663.69 (n/a)</td><td>16749.45 (n/a)</td><td>8098.73 (n/a)</td><td>5160.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.00 <b>(+175.00%)</b></td><td>0.00 <b>(+78.95%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 <b>(+664.85%)</b></td><td>22280.55 (-5.43%)</td><td>15290.52 <b>(-27.55%)</b></td><td>17644.14 (-18.32%)</td><td>7223.64 <b>(-60.38%)</b></td><td>7013.44 <b>(+202.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23560.87 (n/a)</td><td>21104.47 (n/a)</td><td>21601.61 (n/a)</td><td>18233.21 (n/a)</td><td>2320.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.15 (+16.31%)</td><td>0.11 (+18.89%)</td><td>0.09 (+5.50%)</td><td>0.08 (+14.17%)</td><td>0.03 <b>(+47.23%)</b></td><td>24794.05 (-12.35%)</td><td>20400.77 (-13.41%)</td><td>23748.63 (-5.18%)</td><td>13677.08 (-14.01%)</td><td>5528.03 (+19.19%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28289.03 (n/a)</td><td>23560.57 (n/a)</td><td>25047.14 (n/a)</td><td>15906.19 (n/a)</td><td>4637.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.82 (-0.08%)</td><td>1.31 (+6.08%)</td><td>1.43 <b>(+36.32%)</b></td><td>0.76 (-1.84%)</td><td>0.42 (-0.50%)</td><td>688.70 (+1.88%)</td><td>442.30 (-5.26%)</td><td>367.30 <b>(-26.64%)</b></td><td>287.60 (+0.07%)</td><td>162.53 (+5.98%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.82 (n/a)</td><td>1.23 (n/a)</td><td>1.05 (n/a)</td><td>0.78 (n/a)</td><td>0.42 (n/a)</td><td>676.00 (n/a)</td><td>466.86 (n/a)</td><td>500.70 (n/a)</td><td>287.40 (n/a)</td><td>153.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.89 <b>(+21.83%)</b></td><td>1.96 <b>(+70.74%)</b></td><td>2.29 <b>(+102.28%)</b></td><td>0.32 (+1.85%)</td><td>1.02 <b>(+21.47%)</b></td><td>3322.40 (-1.82%)</td><td>1034.16 <b>(-34.66%)</b></td><td>458.80 <b>(-50.57%)</b></td><td>363.20 (-17.92%)</td><td>1283.10 (+0.58%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>2.37 (n/a)</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>0.31 (n/a)</td><td>0.84 (n/a)</td><td>3383.90 (n/a)</td><td>1582.72 (n/a)</td><td>928.10 (n/a)</td><td>442.50 (n/a)</td><td>1275.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.59 (-10.32%)</td><td>1.43 (+5.59%)</td><td>1.40 (-11.18%)</td><td>1.24 <b>(+78.99%)</b></td><td>0.14 <b>(-67.85%)</b></td><td>421.90 <b>(-44.13%)</b></td><td>368.48 (-15.28%)</td><td>374.20 (+12.61%)</td><td>329.00 (+11.49%)</td><td>37.60 <b>(-80.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:08:57</td><td>1.78 (n/a)</td><td>1.36 (n/a)</td><td>1.58 (n/a)</td><td>0.69 (n/a)</td><td>0.45 (n/a)</td><td>755.20 (n/a)</td><td>434.96 (n/a)</td><td>332.30 (n/a)</td><td>295.10 (n/a)</td><td>191.54 (n/a)</td>
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
