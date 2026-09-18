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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (-14.14%)</td><td>0.04 (-11.27%)</td><td>0.04 (-15.55%)</td><td>0.03 (-7.99%)</td><td>0.01 <b>(-28.77%)</b></td><td>478.60 (+8.70%)</td><td>359.60 (+10.58%)</td><td>325.30 (+18.42%)</td><td>293.80 (+16.49%)</td><td>78.30 (-10.14%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>440.30 (n/a)</td><td>325.18 (n/a)</td><td>274.70 (n/a)</td><td>252.20 (n/a)</td><td>87.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 <b>(+23.57%)</b></td><td>0.03 (+6.01%)</td><td>0.03 (-14.53%)</td><td>0.02 (-8.20%)</td><td>0.01 <b>(+100.52%)</b></td><td>538.00 (+8.93%)</td><td>390.56 (+0.61%)</td><td>430.60 (+16.98%)</td><td>246.30 (-19.09%)</td><td>125.62 <b>(+69.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.90 (n/a)</td><td>388.18 (n/a)</td><td>368.10 (n/a)</td><td>304.40 (n/a)</td><td>74.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (-13.79%)</td><td>0.03 (+7.00%)</td><td>0.03 (+18.95%)</td><td>0.02 (-16.43%)</td><td>0.01 (-17.70%)</td><td>611.50 (+19.67%)</td><td>385.28 (-6.38%)</td><td>366.60 (-15.92%)</td><td>271.30 (+15.99%)</td><td>133.45 <b>(+26.32%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.00 (n/a)</td><td>411.52 (n/a)</td><td>436.00 (n/a)</td><td>233.90 (n/a)</td><td>105.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (+4.64%)</td><td>0.02 <b>(+51.02%)</b></td><td>0.02 <b>(+85.04%)</b></td><td>0.01 <b>(+53.49%)</b></td><td>0.01 (-12.99%)</td><td>424.90 <b>(-34.84%)</b></td><td>266.44 <b>(-39.23%)</b></td><td>261.80 <b>(-45.95%)</b></td><td>187.70 (-4.43%)</td><td>96.63 <b>(-45.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.10 (n/a)</td><td>438.44 (n/a)</td><td>484.40 (n/a)</td><td>196.40 (n/a)</td><td>176.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 <b>(+32.84%)</b></td><td>0.02 (+10.58%)</td><td>0.01 <b>(-29.70%)</b></td><td>0.01 (+2.52%)</td><td>0.01 <b>(+52.05%)</b></td><td>548.30 (-2.46%)</td><td>348.66 (-3.58%)</td><td>399.00 <b>(+42.25%)</b></td><td>168.90 <b>(-24.73%)</b></td><td>155.56 (+4.75%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.10 (n/a)</td><td>361.62 (n/a)</td><td>280.50 (n/a)</td><td>224.40 (n/a)</td><td>148.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 <b>(+23.24%)</b></td><td>0.02 (+5.57%)</td><td>0.01 <b>(-22.16%)</b></td><td>0.01 (-19.09%)</td><td>0.01 <b>(+65.48%)</b></td><td>587.80 <b>(+23.59%)</b></td><td>366.80 (+5.86%)</td><td>380.00 <b>(+28.47%)</b></td><td>194.90 (-18.86%)</td><td>173.01 <b>(+45.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>475.60 (n/a)</td><td>346.50 (n/a)</td><td>295.80 (n/a)</td><td>240.20 (n/a)</td><td>118.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (+6.52%)</td><td>0.02 (+4.98%)</td><td>0.02 (+5.46%)</td><td>0.01 (+7.42%)</td><td>0.01 <b>(+28.38%)</b></td><td>577.70 (-6.91%)</td><td>359.02 (-1.51%)</td><td>288.50 (-5.19%)</td><td>229.70 (-6.13%)</td><td>154.89 (+3.46%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.60 (n/a)</td><td>364.54 (n/a)</td><td>304.30 (n/a)</td><td>244.70 (n/a)</td><td>149.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (+2.56%)</td><td>0.01 (-9.21%)</td><td>0.01 <b>(-23.25%)</b></td><td>0.01 <b>(+29.04%)</b></td><td>0.00 (-6.14%)</td><td>452.60 <b>(-22.50%)</b></td><td>383.78 (+6.72%)</td><td>407.90 <b>(+30.32%)</b></td><td>239.20 (-2.49%)</td><td>83.51 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>584.00 (n/a)</td><td>359.62 (n/a)</td><td>313.00 (n/a)</td><td>245.30 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 <b>(+25.05%)</b></td><td>0.01 (+12.29%)</td><td>0.01 <b>(+20.70%)</b></td><td>0.01 (+16.25%)</td><td>0.00 <b>(+29.08%)</b></td><td>539.80 (-13.98%)</td><td>426.40 (-10.38%)</td><td>434.90 (-17.15%)</td><td>246.70 <b>(-20.01%)</b></td><td>110.69 (-14.75%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.50 (n/a)</td><td>475.78 (n/a)</td><td>524.90 (n/a)</td><td>308.40 (n/a)</td><td>129.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>454.70 (n/a)</td><td>290.74 (n/a)</td><td>274.70 (n/a)</td><td>200.00 (n/a)</td><td>103.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>435.50 (n/a)</td><td>319.50 (n/a)</td><td>275.20 (n/a)</td><td>214.50 (n/a)</td><td>98.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.40 (n/a)</td><td>400.04 (n/a)</td><td>468.90 (n/a)</td><td>251.60 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>456.20 (n/a)</td><td>321.56 (n/a)</td><td>286.40 (n/a)</td><td>246.70 (n/a)</td><td>86.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>373.72 (n/a)</td><td>363.70 (n/a)</td><td>245.50 (n/a)</td><td>124.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>381.30 (n/a)</td><td>282.22 (n/a)</td><td>249.80 (n/a)</td><td>246.00 (n/a)</td><td>57.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.00 (+13.61%)</td><td>0.74 (+6.08%)</td><td>0.69 (-9.15%)</td><td>0.61 <b>(+31.18%)</b></td><td>0.15 (-6.44%)</td><td>752.90 <b>(-23.76%)</b></td><td>637.74 (-7.77%)</td><td>664.40 (+10.09%)</td><td>459.60 (-11.97%)</td><td>110.66 <b>(-40.47%)</b></td><td>73.01 (+13.61%)</td><td>54.14 (+6.08%)</td><td>50.51 (-9.15%)</td><td>44.57 <b>(+31.18%)</b></td><td>11.10 (-6.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.88 (n/a)</td><td>0.70 (n/a)</td><td>0.76 (n/a)</td><td>0.46 (n/a)</td><td>0.16 (n/a)</td><td>987.60 (n/a)</td><td>691.46 (n/a)</td><td>603.50 (n/a)</td><td>522.10 (n/a)</td><td>185.90 (n/a)</td><td>64.27 (n/a)</td><td>51.04 (n/a)</td><td>55.60 (n/a)</td><td>33.97 (n/a)</td><td>11.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.31 (-10.09%)</td><td>0.80 (-10.16%)</td><td>0.88 (+12.42%)</td><td>0.19 <b>(-57.27%)</b></td><td>0.41 (+2.64%)</td><td>3468.60 <b>(+134.02%)</b></td><td>1279.22 <b>(+46.02%)</b></td><td>748.10 (-11.05%)</td><td>499.40 (+11.22%)</td><td>1235.34 <b>(+207.11%)</b></td><td>134.39 (-10.09%)</td><td>81.45 (-10.16%)</td><td>89.71 (+12.42%)</td><td>19.35 <b>(-57.27%)</b></td><td>42.01 (+2.64%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.46 (n/a)</td><td>0.89 (n/a)</td><td>0.78 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>1482.20 (n/a)</td><td>876.06 (n/a)</td><td>841.00 (n/a)</td><td>449.00 (n/a)</td><td>402.25 (n/a)</td><td>149.47 (n/a)</td><td>90.67 (n/a)</td><td>79.80 (n/a)</td><td>45.28 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.35 (+4.25%)</td><td>0.97 (-1.13%)</td><td>1.13 (+16.96%)</td><td>0.21 <b>(-63.17%)</b></td><td>0.44 <b>(+66.85%)</b></td><td>3569.20 <b>(+171.53%)</b></td><td>1240.50 <b>(+49.82%)</b></td><td>669.00 (-14.49%)</td><td>557.30 (-4.08%)</td><td>1304.00 <b>(+357.90%)</b></td><td>150.52 (+4.25%)</td><td>108.00 (-1.13%)</td><td>125.40 (+16.96%)</td><td>23.50 <b>(-63.17%)</b></td><td>49.52 <b>(+66.85%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.30 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.57 (n/a)</td><td>0.27 (n/a)</td><td>1314.50 (n/a)</td><td>828.00 (n/a)</td><td>782.40 (n/a)</td><td>581.00 (n/a)</td><td>284.78 (n/a)</td><td>144.38 (n/a)</td><td>109.23 (n/a)</td><td>107.22 (n/a)</td><td>63.82 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.73 (+12.89%)</td><td>1.29 <b>(+46.32%)</b></td><td>1.24 <b>(+157.92%)</b></td><td>1.04 <b>(+125.88%)</b></td><td>0.26 <b>(-54.12%)</b></td><td>1009.00 <b>(-55.73%)</b></td><td>833.08 <b>(-48.40%)</b></td><td>847.00 <b>(-61.23%)</b></td><td>605.20 (-11.42%)</td><td>145.60 <b>(-82.63%)</b></td><td>221.77 (+12.89%)</td><td>165.70 <b>(+46.32%)</b></td><td>158.46 <b>(+157.92%)</b></td><td>133.02 <b>(+125.88%)</b></td><td>33.28 <b>(-54.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.53 (n/a)</td><td>0.88 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.57 (n/a)</td><td>2279.10 (n/a)</td><td>1614.54 (n/a)</td><td>2184.70 (n/a)</td><td>683.20 (n/a)</td><td>838.39 (n/a)</td><td>196.44 (n/a)</td><td>113.24 (n/a)</td><td>61.44 (n/a)</td><td>58.89 (n/a)</td><td>72.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.36 <b>(+31.88%)</b></td><td>1.53 <b>(+25.52%)</b></td><td>1.37 (+4.28%)</td><td>0.95 <b>(+220.92%)</b></td><td>0.53 (-5.07%)</td><td>1102.40 <b>(-68.84%)</b></td><td>747.10 <b>(-42.31%)</b></td><td>762.90 (-4.11%)</td><td>443.60 <b>(-24.18%)</b></td><td>240.58 <b>(-80.86%)</b></td><td>302.55 <b>(+31.88%)</b></td><td>196.10 <b>(+25.52%)</b></td><td>175.93 (+4.28%)</td><td>121.76 <b>(+220.92%)</b></td><td>67.25 (-5.07%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.79 (n/a)</td><td>1.22 (n/a)</td><td>1.32 (n/a)</td><td>0.30 (n/a)</td><td>0.55 (n/a)</td><td>3537.60 (n/a)</td><td>1294.98 (n/a)</td><td>795.60 (n/a)</td><td>585.10 (n/a)</td><td>1256.72 (n/a)</td><td>229.41 (n/a)</td><td>156.24 (n/a)</td><td>168.71 (n/a)</td><td>37.94 (n/a)</td><td>70.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.25 (-4.53%)</td><td>1.47 (-14.69%)</td><td>1.30 (-11.26%)</td><td>0.30 <b>(-77.04%)</b></td><td>0.80 <b>(+61.83%)</b></td><td>3521.80 <b>(+335.60%)</b></td><td>1216.78 <b>(+87.34%)</b></td><td>806.40 (+12.69%)</td><td>466.70 (+4.76%)</td><td>1299.33 <b>(+663.85%)</b></td><td>287.61 (-4.53%)</td><td>187.52 (-14.69%)</td><td>166.44 (-11.26%)</td><td>38.11 <b>(-77.04%)</b></td><td>102.11 <b>(+61.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.35 (n/a)</td><td>1.72 (n/a)</td><td>1.47 (n/a)</td><td>1.30 (n/a)</td><td>0.49 (n/a)</td><td>808.50 (n/a)</td><td>649.50 (n/a)</td><td>715.60 (n/a)</td><td>445.50 (n/a)</td><td>170.10 (n/a)</td><td>301.24 (n/a)</td><td>219.80 (n/a)</td><td>187.56 (n/a)</td><td>166.01 (n/a)</td><td>63.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.47 (+16.14%)</td><td>1.14 <b>(+47.45%)</b></td><td>1.22 <b>(+92.73%)</b></td><td>0.49 <b>(+48.27%)</b></td><td>0.40 (-7.66%)</td><td>2159.00 <b>(-32.56%)</b></td><td>1080.38 <b>(-38.84%)</b></td><td>860.20 <b>(-48.12%)</b></td><td>714.10 (-13.90%)</td><td>609.73 <b>(-38.93%)</b></td><td>187.95 (+16.14%)</td><td>146.51 <b>(+47.45%)</b></td><td>156.02 <b>(+92.73%)</b></td><td>62.17 <b>(+48.27%)</b></td><td>50.60 (-7.66%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.26 (n/a)</td><td>0.78 (n/a)</td><td>0.63 (n/a)</td><td>0.33 (n/a)</td><td>0.43 (n/a)</td><td>3201.20 (n/a)</td><td>1766.46 (n/a)</td><td>1657.90 (n/a)</td><td>829.40 (n/a)</td><td>998.34 (n/a)</td><td>161.83 (n/a)</td><td>99.36 (n/a)</td><td>80.96 (n/a)</td><td>41.93 (n/a)</td><td>54.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.64 (-16.81%)</td><td>0.56 (-8.08%)</td><td>0.57 (+1.48%)</td><td>0.47 (-9.31%)</td><td>0.07 <b>(-38.02%)</b></td><td>764.70 (+10.27%)</td><td>652.32 (+7.62%)</td><td>631.00 (-1.47%)</td><td>560.30 <b>(+20.18%)</b></td><td>78.66 (-17.66%)</td><td>29.94 (-16.81%)</td><td>26.01 (-8.08%)</td><td>26.59 (+1.48%)</td><td>21.94 (-9.31%)</td><td>3.06 <b>(-38.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.77 (n/a)</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.52 (n/a)</td><td>0.11 (n/a)</td><td>693.50 (n/a)</td><td>606.12 (n/a)</td><td>640.40 (n/a)</td><td>466.20 (n/a)</td><td>95.53 (n/a)</td><td>35.99 (n/a)</td><td>28.30 (n/a)</td><td>26.20 (n/a)</td><td>24.19 (n/a)</td><td>4.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.59 (-2.93%)</td><td>2.89 <b>(+22.30%)</b></td><td>3.33 <b>(+46.33%)</b></td><td>1.62 <b>(+44.32%)</b></td><td>0.87 <b>(-29.03%)</b></td><td>1616.70 <b>(-30.71%)</b></td><td>997.68 <b>(-30.04%)</b></td><td>786.10 <b>(-31.66%)</b></td><td>729.50 (+3.01%)</td><td>381.06 <b>(-51.41%)</b></td><td>735.94 (-2.93%)</td><td>591.57 <b>(+22.30%)</b></td><td>682.98 <b>(+46.33%)</b></td><td>332.08 <b>(+44.32%)</b></td><td>178.14 <b>(-29.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.70 (n/a)</td><td>2.36 (n/a)</td><td>2.28 (n/a)</td><td>1.12 (n/a)</td><td>1.23 (n/a)</td><td>2333.30 (n/a)</td><td>1425.98 (n/a)</td><td>1150.30 (n/a)</td><td>708.20 (n/a)</td><td>784.31 (n/a)</td><td>758.13 (n/a)</td><td>483.72 (n/a)</td><td>466.74 (n/a)</td><td>230.09 (n/a)</td><td>251.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_bounds[iter0]

_No metrics available._


### test_gemm_split_leg_bounds[iter1]

_No metrics available._


### test_gemm_split_leg_bounds[iter2]

_No metrics available._


### test_gemm_split_leg_bounds[iter3]

_No metrics available._


### test_gemm_split_leg_bounds[iter4]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter0]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter1]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter2]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter3]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter4]

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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>429.52 (n/a)</td><td>516.20 (n/a)</td><td>258.30 (n/a)</td><td>133.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>382.12 (n/a)</td><td>341.20 (n/a)</td><td>208.30 (n/a)</td><td>145.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1859.50 (n/a)</td><td>627.60 (n/a)</td><td>251.20 (n/a)</td><td>239.80 (n/a)</td><td>700.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.40 (n/a)</td><td>372.58 (n/a)</td><td>307.20 (n/a)</td><td>229.50 (n/a)</td><td>135.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.30 (n/a)</td><td>368.62 (n/a)</td><td>292.60 (n/a)</td><td>183.70 (n/a)</td><td>180.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.60 (n/a)</td><td>461.66 (n/a)</td><td>366.80 (n/a)</td><td>308.10 (n/a)</td><td>166.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.53 (-9.47%)</td><td>0.43 (+5.83%)</td><td>0.47 (+2.49%)</td><td>0.32 <b>(+51.56%)</b></td><td>0.10 <b>(-29.07%)</b></td><td>684.80 <b>(-34.02%)</b></td><td>535.82 (-12.27%)</td><td>468.10 (-2.42%)</td><td>421.10 (+10.47%)</td><td>133.72 <b>(-49.03%)</b></td><td>22.41 (-9.47%)</td><td>18.47 (+5.83%)</td><td>20.16 (+2.49%)</td><td>13.78 <b>(+51.56%)</b></td><td>4.29 <b>(-29.07%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.58 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>1037.90 (n/a)</td><td>610.78 (n/a)</td><td>479.70 (n/a)</td><td>381.20 (n/a)</td><td>262.35 (n/a)</td><td>24.76 (n/a)</td><td>17.45 (n/a)</td><td>19.67 (n/a)</td><td>9.09 (n/a)</td><td>6.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.57 (-10.49%)</td><td>0.33 <b>(-25.22%)</b></td><td>0.34 (-19.60%)</td><td>0.12 <b>(-64.05%)</b></td><td>0.16 <b>(+41.68%)</b></td><td>1919.90 <b>(+178.21%)</b></td><td>874.92 <b>(+67.34%)</b></td><td>646.20 <b>(+24.36%)</b></td><td>391.30 (+11.70%)</td><td>602.72 <b>(+395.35%)</b></td><td>24.12 (-10.49%)</td><td>14.16 <b>(-25.22%)</b></td><td>14.60 (-19.60%)</td><td>4.92 <b>(-64.05%)</b></td><td>6.94 <b>(+41.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.63 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>690.10 (n/a)</td><td>522.84 (n/a)</td><td>519.60 (n/a)</td><td>350.30 (n/a)</td><td>121.67 (n/a)</td><td>26.94 (n/a)</td><td>18.94 (n/a)</td><td>18.16 (n/a)</td><td>13.67 (n/a)</td><td>4.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.31 (-0.13%)</td><td>0.30 (-0.37%)</td><td>0.30 (-0.39%)</td><td>0.29 (-2.38%)</td><td>0.01 <b>(+51.33%)</b></td><td>86093.60 (+2.43%)</td><td>83085.62 (+0.40%)</td><td>83004.80 (+0.39%)</td><td>81475.40 (+0.13%)</td><td>1885.13 <b>(+54.88%)</b></td><td>210.86 (-0.13%)</td><td>206.86 (-0.37%)</td><td>206.97 (-0.39%)</td><td>199.55 (-2.38%)</td><td>4.62 <b>(+51.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84048.60 (n/a)</td><td>82756.48 (n/a)</td><td>82679.10 (n/a)</td><td>81369.10 (n/a)</td><td>1217.14 (n/a)</td><td>211.14 (n/a)</td><td>207.63 (n/a)</td><td>207.79 (n/a)</td><td>204.40 (n/a)</td><td>3.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.15 (+0.11%)</td><td>1.11 (-2.76%)</td><td>1.14 (-0.21%)</td><td>0.96 (-12.91%)</td><td>0.08 <b>(+338.56%)</b></td><td>26149.80 (+14.83%)</td><td>22851.20 (+3.31%)</td><td>22007.00 (+0.21%)</td><td>21899.20 (-0.11%)</td><td>1848.09 <b>(+404.79%)</b></td><td>784.50 (+0.11%)</td><td>755.38 (-2.76%)</td><td>780.65 (-0.21%)</td><td>656.98 (-12.91%)</td><td>55.18 <b>(+338.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22773.10 (n/a)</td><td>22119.70 (n/a)</td><td>21961.30 (n/a)</td><td>21922.80 (n/a)</td><td>366.11 (n/a)</td><td>783.65 (n/a)</td><td>776.84 (n/a)</td><td>782.28 (n/a)</td><td>754.39 (n/a)</td><td>12.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.98 (-4.40%)</td><td>2.75 (-1.44%)</td><td>2.18 (-12.63%)</td><td>2.02 <b>(+42.92%)</b></td><td>0.91 <b>(-24.15%)</b></td><td>3984.60 <b>(-30.03%)</b></td><td>3171.70 (-6.66%)</td><td>3700.90 (+14.45%)</td><td>2024.20 (+4.60%)</td><td>925.39 <b>(-40.50%)</b></td><td>1044.34 (-4.40%)</td><td>722.04 (-1.44%)</td><td>571.20 (-12.63%)</td><td>530.53 <b>(+42.92%)</b></td><td>239.09 <b>(-24.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>4.17 (n/a)</td><td>2.79 (n/a)</td><td>2.49 (n/a)</td><td>1.42 (n/a)</td><td>1.20 (n/a)</td><td>5694.80 (n/a)</td><td>3398.16 (n/a)</td><td>3233.50 (n/a)</td><td>1935.20 (n/a)</td><td>1555.34 (n/a)</td><td>1092.36 (n/a)</td><td>732.57 (n/a)</td><td>653.76 (n/a)</td><td>371.20 (n/a)</td><td>315.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.24 (+5.38%)</td><td>0.23 (+17.43%)</td><td>0.23 (+17.16%)</td><td>0.22 <b>(+40.02%)</b></td><td>0.01 <b>(-60.70%)</b></td><td>5682.00 <b>(-28.58%)</b></td><td>5399.10 (-16.08%)</td><td>5346.30 (-14.65%)</td><td>5087.30 (-5.11%)</td><td>250.49 <b>(-73.70%)</b></td><td>13.19 (+5.38%)</td><td>12.45 (+17.43%)</td><td>12.55 (+17.16%)</td><td>11.81 <b>(+40.02%)</b></td><td>0.58 <b>(-60.70%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>7955.80 (n/a)</td><td>6433.74 (n/a)</td><td>6263.90 (n/a)</td><td>5361.10 (n/a)</td><td>952.44 (n/a)</td><td>12.52 (n/a)</td><td>10.60 (n/a)</td><td>10.71 (n/a)</td><td>8.44 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.71 (n/a)</td><td>3.53 (n/a)</td><td>3.50 (n/a)</td><td>3.33 (n/a)</td><td>0.16 (n/a)</td><td>3.70 (n/a)</td><td>3.53 (n/a)</td><td>3.50 (n/a)</td><td>3.33 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>7.52 (+19.90%)</td><td>7.20 <b>(+26.29%)</b></td><td>7.45 <b>(+30.11%)</b></td><td>6.57 <b>(+30.02%)</b></td><td>0.43 (-0.71%)</td><td>7.52 (+19.90%)</td><td>7.20 <b>(+26.29%)</b></td><td>7.45 <b>(+30.11%)</b></td><td>6.56 <b>(+30.02%)</b></td><td>0.43 (-0.71%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>6.28 (n/a)</td><td>5.70 (n/a)</td><td>5.73 (n/a)</td><td>5.05 (n/a)</td><td>0.44 (n/a)</td><td>6.27 (n/a)</td><td>5.70 (n/a)</td><td>5.73 (n/a)</td><td>5.05 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>13.33 (+0.04%)</td><td>10.58 <b>(+23.48%)</b></td><td>11.46 <b>(+53.91%)</b></td><td>8.21 (+16.90%)</td><td>2.28 (-14.79%)</td><td>13.33 (+0.04%)</td><td>10.57 <b>(+23.48%)</b></td><td>11.45 <b>(+53.91%)</b></td><td>8.21 (+16.90%)</td><td>2.28 (-14.79%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>13.33 (n/a)</td><td>8.57 (n/a)</td><td>7.44 (n/a)</td><td>7.02 (n/a)</td><td>2.67 (n/a)</td><td>13.32 (n/a)</td><td>8.56 (n/a)</td><td>7.44 (n/a)</td><td>7.02 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.96 (n/a)</td><td>3.77 (n/a)</td><td>3.69 (n/a)</td><td>3.62 (n/a)</td><td>0.15 (n/a)</td><td>3.96 (n/a)</td><td>3.77 (n/a)</td><td>3.69 (n/a)</td><td>3.62 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>6.64 (-11.96%)</td><td>6.28 (+1.81%)</td><td>6.43 (+8.89%)</td><td>5.72 (+0.92%)</td><td>0.36 <b>(-53.25%)</b></td><td>6.64 (-11.96%)</td><td>6.28 (+1.81%)</td><td>6.43 (+8.89%)</td><td>5.72 (+0.92%)</td><td>0.36 <b>(-53.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>7.55 (n/a)</td><td>6.17 (n/a)</td><td>5.91 (n/a)</td><td>5.67 (n/a)</td><td>0.78 (n/a)</td><td>7.54 (n/a)</td><td>6.17 (n/a)</td><td>5.90 (n/a)</td><td>5.67 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>13.14 (-5.46%)</td><td>10.20 (-11.84%)</td><td>8.56 <b>(-30.46%)</b></td><td>8.01 (-12.06%)</td><td>2.63 <b>(+38.57%)</b></td><td>13.13 (-5.46%)</td><td>10.19 (-11.84%)</td><td>8.55 <b>(-30.46%)</b></td><td>8.00 (-12.06%)</td><td>2.63 <b>(+38.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>13.90 (n/a)</td><td>11.57 (n/a)</td><td>12.30 (n/a)</td><td>9.11 (n/a)</td><td>1.90 (n/a)</td><td>13.89 (n/a)</td><td>11.56 (n/a)</td><td>12.30 (n/a)</td><td>9.10 (n/a)</td><td>1.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.19 (+9.57%)</td><td>2.06 (+18.03%)</td><td>1.73 <b>(+49.93%)</b></td><td>1.10 (+12.33%)</td><td>0.93 (-3.29%)</td><td>3.19 (+9.57%)</td><td>2.06 (+18.03%)</td><td>1.72 <b>(+49.93%)</b></td><td>1.10 (+12.33%)</td><td>0.93 (-3.29%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.92 (n/a)</td><td>1.75 (n/a)</td><td>1.15 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>2.91 (n/a)</td><td>1.74 (n/a)</td><td>1.15 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.54 (-3.47%)</td><td>0.39 (-10.29%)</td><td>0.47 (-13.57%)</td><td>0.08 <b>(-43.05%)</b></td><td>0.20 (+5.69%)</td><td>0.53 (-3.47%)</td><td>0.38 (-10.29%)</td><td>0.46 (-13.57%)</td><td>0.07 <b>(-43.05%)</b></td><td>0.19 (+5.69%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.54 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.53 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.68 (-9.00%)</td><td>0.45 (-12.03%)</td><td>0.65 <b>(+38.92%)</b></td><td>0.08 <b>(-73.15%)</b></td><td>0.31 <b>(+54.09%)</b></td><td>0.67 (-9.00%)</td><td>0.44 (-12.03%)</td><td>0.65 <b>(+38.92%)</b></td><td>0.08 <b>(-73.15%)</b></td><td>0.30 <b>(+54.09%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.75 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.74 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.81 (+14.75%)</td><td>1.18 <b>(-36.33%)</b></td><td>0.48 <b>(-78.56%)</b></td><td>0.45 (+4.23%)</td><td>1.06 <b>(+27.03%)</b></td><td>2.77 (+14.75%)</td><td>1.16 <b>(-36.33%)</b></td><td>0.47 <b>(-78.56%)</b></td><td>0.44 (+4.23%)</td><td>1.04 <b>(+27.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.45 (n/a)</td><td>1.86 (n/a)</td><td>2.22 (n/a)</td><td>0.43 (n/a)</td><td>0.83 (n/a)</td><td>2.41 (n/a)</td><td>1.83 (n/a)</td><td>2.18 (n/a)</td><td>0.43 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>326.16 (n/a)</td><td>326.20 (n/a)</td><td>199.60 (n/a)</td><td>120.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.70 (n/a)</td><td>396.26 (n/a)</td><td>483.20 (n/a)</td><td>226.10 (n/a)</td><td>137.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>426.78 (n/a)</td><td>378.10 (n/a)</td><td>279.10 (n/a)</td><td>123.42 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>408.86 (n/a)</td><td>465.90 (n/a)</td><td>225.60 (n/a)</td><td>147.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.60 (n/a)</td><td>475.60 (n/a)</td><td>536.60 (n/a)</td><td>189.20 (n/a)</td><td>172.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1099.80 (n/a)</td><td>665.68 (n/a)</td><td>551.20 (n/a)</td><td>496.40 (n/a)</td><td>248.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 <b>(+23.32%)</b></td><td>0.03 <b>(+45.45%)</b></td><td>0.03 <b>(+60.78%)</b></td><td>0.02 <b>(+28.35%)</b></td><td>0.01 <b>(+27.01%)</b></td><td>491.90 <b>(-22.09%)</b></td><td>310.30 <b>(-30.88%)</b></td><td>290.50 <b>(-37.81%)</b></td><td>223.20 (-18.90%)</td><td>108.11 (-16.52%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.40 (n/a)</td><td>448.96 (n/a)</td><td>467.10 (n/a)</td><td>275.20 (n/a)</td><td>129.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-7.77%)</td><td>0.02 <b>(-21.83%)</b></td><td>0.02 (-15.72%)</td><td>0.00 <b>(-77.89%)</b></td><td>0.01 <b>(+88.01%)</b></td><td>1915.30 <b>(+352.36%)</b></td><td>641.36 <b>(+109.51%)</b></td><td>345.40 (+18.65%)</td><td>255.70 (+8.39%)</td><td>714.20 <b>(+901.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>423.40 (n/a)</td><td>306.12 (n/a)</td><td>291.10 (n/a)</td><td>235.90 (n/a)</td><td>71.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 <b>(+30.60%)</b></td><td>0.03 (-10.25%)</td><td>0.02 (-19.42%)</td><td>0.01 <b>(-46.41%)</b></td><td>0.01 <b>(+413.09%)</b></td><td>590.70 <b>(+86.64%)</b></td><td>386.56 <b>(+31.48%)</b></td><td>369.00 <b>(+24.12%)</b></td><td>205.30 <b>(-23.42%)</b></td><td>170.66 <b>(+634.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>316.50 (n/a)</td><td>294.00 (n/a)</td><td>297.30 (n/a)</td><td>268.10 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (+9.29%)</td><td>0.02 (-8.89%)</td><td>0.02 (+3.20%)</td><td>0.00 <b>(-71.39%)</b></td><td>0.01 <b>(+48.79%)</b></td><td>1932.60 <b>(+249.48%)</b></td><td>675.26 <b>(+76.85%)</b></td><td>413.90 (-3.11%)</td><td>201.50 (-8.49%)</td><td>716.29 <b>(+424.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>381.82 (n/a)</td><td>427.20 (n/a)</td><td>220.20 (n/a)</td><td>136.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-6.79%)</td><td>0.03 (+7.51%)</td><td>0.03 <b>(+39.02%)</b></td><td>0.01 (-17.53%)</td><td>0.01 (-14.20%)</td><td>547.80 <b>(+21.25%)</b></td><td>328.30 (-6.93%)</td><td>292.40 <b>(-28.09%)</b></td><td>246.10 (+7.28%)</td><td>124.44 (+18.73%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.80 (n/a)</td><td>352.74 (n/a)</td><td>406.60 (n/a)</td><td>229.40 (n/a)</td><td>104.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 <b>(-49.57%)</b></td><td>0.02 (-14.16%)</td><td>0.03 <b>(+65.38%)</b></td><td>0.00 <b>(-68.96%)</b></td><td>0.01 <b>(-42.85%)</b></td><td>1932.50 <b>(+222.14%)</b></td><td>642.92 <b>(+49.76%)</b></td><td>304.90 <b>(-39.54%)</b></td><td>296.60 <b>(+98.26%)</b></td><td>721.71 <b>(+270.78%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>599.90 (n/a)</td><td>429.30 (n/a)</td><td>504.30 (n/a)</td><td>149.60 (n/a)</td><td>194.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (-7.04%)</td><td>0.03 (+9.39%)</td><td>0.03 (+13.09%)</td><td>0.02 (+5.43%)</td><td>0.01 (-12.30%)</td><td>479.30 (-5.16%)</td><td>324.70 (-10.81%)</td><td>278.90 (-11.57%)</td><td>234.00 (+7.59%)</td><td>104.79 (-16.45%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.40 (n/a)</td><td>364.04 (n/a)</td><td>315.40 (n/a)</td><td>217.50 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-19.00%)</td><td>0.02 (-15.19%)</td><td>0.02 (-13.31%)</td><td>0.01 <b>(-40.21%)</b></td><td>0.01 (+8.42%)</td><td>1060.50 <b>(+67.24%)</b></td><td>571.30 <b>(+31.85%)</b></td><td>526.80 (+15.35%)</td><td>308.70 <b>(+23.48%)</b></td><td>308.46 <b>(+113.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.10 (n/a)</td><td>433.28 (n/a)</td><td>456.70 (n/a)</td><td>250.00 (n/a)</td><td>144.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (+18.68%)</td><td>0.03 (+16.86%)</td><td>0.03 (+5.45%)</td><td>0.02 (+14.56%)</td><td>0.01 (+11.55%)</td><td>422.90 (-12.71%)</td><td>294.22 (-14.62%)</td><td>278.80 (-5.17%)</td><td>236.30 (-15.73%)</td><td>75.24 (-14.55%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.50 (n/a)</td><td>344.60 (n/a)</td><td>294.00 (n/a)</td><td>280.40 (n/a)</td><td>88.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (+16.40%)</td><td>0.02 <b>(+51.51%)</b></td><td>0.02 (+15.94%)</td><td>0.02 <b>(+289.18%)</b></td><td>0.01 (-5.17%)</td><td>520.80 <b>(-74.30%)</b></td><td>406.38 <b>(-51.11%)</b></td><td>481.90 (-13.75%)</td><td>263.70 (-14.10%)</td><td>130.38 <b>(-81.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2026.60 (n/a)</td><td>831.20 (n/a)</td><td>558.70 (n/a)</td><td>307.00 (n/a)</td><td>691.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-3.39%)</td><td>0.02 <b>(-24.39%)</b></td><td>0.02 <b>(-22.87%)</b></td><td>0.02 <b>(-43.74%)</b></td><td>0.01 <b>(+225.04%)</b></td><td>524.20 <b>(+77.76%)</b></td><td>390.74 <b>(+38.15%)</b></td><td>379.50 <b>(+29.65%)</b></td><td>270.60 (+3.52%)</td><td>92.33 <b>(+488.20%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>294.90 (n/a)</td><td>282.84 (n/a)</td><td>292.70 (n/a)</td><td>261.40 (n/a)</td><td>15.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 <b>(-25.09%)</b></td><td>0.02 (-17.24%)</td><td>0.02 (+0.59%)</td><td>0.01 (+3.50%)</td><td>0.01 <b>(-44.76%)</b></td><td>575.00 (-3.39%)</td><td>424.68 (+7.18%)</td><td>412.90 (-0.58%)</td><td>249.50 <b>(+33.49%)</b></td><td>124.08 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.20 (n/a)</td><td>396.24 (n/a)</td><td>415.30 (n/a)</td><td>186.90 (n/a)</td><td>179.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 <b>(+27.60%)</b></td><td>0.02 (+18.65%)</td><td>0.03 <b>(+46.63%)</b></td><td>0.01 (-10.67%)</td><td>0.01 <b>(+73.65%)</b></td><td>613.70 (+11.95%)</td><td>381.50 (-8.02%)</td><td>292.80 <b>(-31.78%)</b></td><td>225.60 <b>(-21.61%)</b></td><td>166.47 <b>(+58.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.20 (n/a)</td><td>414.78 (n/a)</td><td>429.20 (n/a)</td><td>287.80 (n/a)</td><td>104.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (+9.10%)</td><td>0.02 (+11.43%)</td><td>0.02 (+14.70%)</td><td>0.02 <b>(+20.35%)</b></td><td>0.01 (-6.27%)</td><td>536.80 (-16.90%)</td><td>448.96 (-12.51%)</td><td>476.40 (-12.81%)</td><td>292.20 (-8.34%)</td><td>93.99 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.00 (n/a)</td><td>513.18 (n/a)</td><td>546.40 (n/a)</td><td>318.80 (n/a)</td><td>140.05 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

_No metrics available._


### test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

_No metrics available._


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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.10 (-12.55%)</td><td>0.07 (-12.45%)</td><td>0.08 (-13.17%)</td><td>0.05 (+1.86%)</td><td>0.02 (-11.08%)</td><td>503.30 (-1.83%)</td><td>353.92 (+12.70%)</td><td>321.00 (+15.18%)</td><td>255.50 (+14.32%)</td><td>104.25 (-8.20%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>512.70 (n/a)</td><td>314.04 (n/a)</td><td>278.70 (n/a)</td><td>223.50 (n/a)</td><td>113.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.15 (-4.41%)</td><td>0.10 (-3.30%)</td><td>0.08 (+0.57%)</td><td>0.07 (-17.04%)</td><td>0.04 (+0.68%)</td><td>625.80 <b>(+20.55%)</b></td><td>464.90 (+5.25%)</td><td>482.20 (-0.56%)</td><td>264.30 (+4.63%)</td><td>140.23 <b>(+27.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>519.10 (n/a)</td><td>441.70 (n/a)</td><td>484.90 (n/a)</td><td>252.60 (n/a)</td><td>110.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (-19.43%)</td><td>0.01 (-18.90%)</td><td>0.02 (+0.86%)</td><td>0.01 <b>(-20.34%)</b></td><td>0.01 (-15.91%)</td><td>698.80 <b>(+25.53%)</b></td><td>454.48 <b>(+26.50%)</b></td><td>335.40 (-0.86%)</td><td>273.90 <b>(+24.11%)</b></td><td>203.37 <b>(+42.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.70 (n/a)</td><td>359.26 (n/a)</td><td>338.30 (n/a)</td><td>220.70 (n/a)</td><td>142.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (+8.60%)</td><td>0.03 (+17.82%)</td><td>0.03 <b>(+77.03%)</b></td><td>0.01 (-6.09%)</td><td>0.01 (+14.75%)</td><td>553.20 (+6.49%)</td><td>360.34 (-13.07%)</td><td>282.40 <b>(-43.52%)</b></td><td>227.40 (-7.90%)</td><td>144.16 (+11.23%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.50 (n/a)</td><td>414.50 (n/a)</td><td>500.00 (n/a)</td><td>246.90 (n/a)</td><td>129.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (-13.77%)</td><td>0.04 (+10.87%)</td><td>0.04 (-0.21%)</td><td>0.02 <b>(+214.69%)</b></td><td>0.01 <b>(-38.25%)</b></td><td>611.20 <b>(-68.22%)</b></td><td>345.34 <b>(-44.67%)</b></td><td>301.40 (+0.23%)</td><td>242.20 (+16.00%)</td><td>151.19 <b>(-79.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1923.50 (n/a)</td><td>624.14 (n/a)</td><td>300.70 (n/a)</td><td>208.80 (n/a)</td><td>729.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-15.91%)</td><td>0.02 (-14.23%)</td><td>0.02 <b>(-22.77%)</b></td><td>0.02 (+1.53%)</td><td>0.00 <b>(-34.45%)</b></td><td>504.30 (-1.50%)</td><td>423.74 (+12.59%)</td><td>461.00 <b>(+29.49%)</b></td><td>299.00 (+18.89%)</td><td>81.38 <b>(-25.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.00 (n/a)</td><td>376.34 (n/a)</td><td>356.00 (n/a)</td><td>251.50 (n/a)</td><td>109.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (+6.18%)</td><td>0.03 (+9.56%)</td><td>0.02 (-19.59%)</td><td>0.02 (+1.79%)</td><td>0.01 <b>(+35.51%)</b></td><td>527.40 (-1.75%)</td><td>371.86 (-4.56%)</td><td>423.80 <b>(+24.35%)</b></td><td>224.20 (-5.80%)</td><td>139.25 (+12.17%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>389.64 (n/a)</td><td>340.80 (n/a)</td><td>238.00 (n/a)</td><td>124.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-10.96%)</td><td>0.02 (-3.45%)</td><td>0.02 (+2.95%)</td><td>0.02 (+3.51%)</td><td>0.01 <b>(-20.55%)</b></td><td>536.70 (-3.38%)</td><td>426.38 (+1.00%)</td><td>449.10 (-2.88%)</td><td>297.30 (+12.32%)</td><td>110.77 (-13.18%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.50 (n/a)</td><td>422.14 (n/a)</td><td>462.40 (n/a)</td><td>264.70 (n/a)</td><td>127.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 <b>(+86.70%)</b></td><td>0.03 <b>(+32.31%)</b></td><td>0.03 <b>(+31.30%)</b></td><td>0.01 <b>(-64.01%)</b></td><td>0.02 <b>(+287.02%)</b></td><td>1673.50 <b>(+177.90%)</b></td><td>594.20 <b>(+22.31%)</b></td><td>350.80 <b>(-23.82%)</b></td><td>201.50 <b>(-46.44%)</b></td><td>610.27 <b>(+538.39%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>602.20 (n/a)</td><td>485.80 (n/a)</td><td>460.50 (n/a)</td><td>376.20 (n/a)</td><td>95.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (-14.64%)</td><td>0.02 <b>(+24.09%)</b></td><td>0.02 <b>(+42.38%)</b></td><td>0.01 <b>(+72.58%)</b></td><td>0.01 <b>(-38.38%)</b></td><td>568.60 <b>(-42.06%)</b></td><td>367.52 <b>(-30.09%)</b></td><td>333.60 <b>(-29.77%)</b></td><td>273.60 (+17.12%)</td><td>118.25 <b>(-57.28%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>981.40 (n/a)</td><td>525.68 (n/a)</td><td>475.00 (n/a)</td><td>233.60 (n/a)</td><td>276.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 <b>(-27.06%)</b></td><td>0.02 (-5.61%)</td><td>0.02 (+8.17%)</td><td>0.02 (+1.82%)</td><td>0.01 <b>(-47.77%)</b></td><td>606.80 (-1.78%)</td><td>485.12 (-2.54%)</td><td>504.10 (-7.56%)</td><td>310.00 <b>(+37.11%)</b></td><td>112.63 <b>(-27.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.80 (n/a)</td><td>497.74 (n/a)</td><td>545.30 (n/a)</td><td>226.10 (n/a)</td><td>155.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 <b>(-38.64%)</b></td><td>0.02 (-5.91%)</td><td>0.02 (+19.96%)</td><td>0.01 (+5.53%)</td><td>0.00 <b>(-66.49%)</b></td><td>606.70 (-5.23%)</td><td>482.24 (-5.32%)</td><td>486.00 (-16.64%)</td><td>381.00 <b>(+62.96%)</b></td><td>88.68 <b>(-47.87%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.20 (n/a)</td><td>509.36 (n/a)</td><td>583.00 (n/a)</td><td>233.80 (n/a)</td><td>170.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (+1.20%)</td><td>0.02 (+3.44%)</td><td>0.02 (+5.90%)</td><td>0.00 <b>(-75.21%)</b></td><td>0.01 <b>(+62.65%)</b></td><td>2436.80 <b>(+303.44%)</b></td><td>827.34 <b>(+58.45%)</b></td><td>546.50 (-5.56%)</td><td>291.30 (-1.19%)</td><td>907.95 <b>(+596.64%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>522.14 (n/a)</td><td>578.70 (n/a)</td><td>294.80 (n/a)</td><td>130.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 <b>(-28.26%)</b></td><td>0.02 (-10.43%)</td><td>0.02 (-2.91%)</td><td>0.01 (-7.82%)</td><td>0.00 <b>(-47.04%)</b></td><td>626.70 (+8.48%)</td><td>482.74 (+5.65%)</td><td>499.70 (+2.99%)</td><td>329.60 <b>(+39.42%)</b></td><td>109.50 (-16.68%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.70 (n/a)</td><td>456.92 (n/a)</td><td>485.20 (n/a)</td><td>236.40 (n/a)</td><td>131.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.39 (+5.69%)</td><td>0.30 (-0.86%)</td><td>0.35 (+14.99%)</td><td>0.17 <b>(-25.55%)</b></td><td>0.11 <b>(+93.48%)</b></td><td>586.80 <b>(+34.31%)</b></td><td>381.28 (+12.03%)</td><td>277.40 (-13.01%)</td><td>253.60 (-5.37%)</td><td>163.50 <b>(+140.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>436.90 (n/a)</td><td>340.34 (n/a)</td><td>318.90 (n/a)</td><td>268.00 (n/a)</td><td>67.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.35 (-8.28%)</td><td>0.27 (-10.14%)</td><td>0.28 (-12.77%)</td><td>0.17 (-16.69%)</td><td>0.07 (-7.11%)</td><td>588.80 <b>(+20.04%)</b></td><td>389.70 (+12.16%)</td><td>350.00 (+14.64%)</td><td>277.50 (+9.04%)</td><td>123.31 <b>(+23.54%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>490.50 (n/a)</td><td>347.44 (n/a)</td><td>305.30 (n/a)</td><td>254.50 (n/a)</td><td>99.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.41 (+10.07%)</td><td>0.29 (+12.17%)</td><td>0.33 <b>(+29.78%)</b></td><td>0.17 (-5.05%)</td><td>0.11 <b>(+28.96%)</b></td><td>588.10 (+5.32%)</td><td>389.44 (-6.45%)</td><td>301.50 <b>(-22.95%)</b></td><td>242.20 (-9.12%)</td><td>165.52 <b>(+21.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>558.40 (n/a)</td><td>416.30 (n/a)</td><td>391.30 (n/a)</td><td>266.50 (n/a)</td><td>135.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.29 (-0.70%)</td><td>0.23 (+0.32%)</td><td>0.26 (+5.68%)</td><td>0.16 (-4.46%)</td><td>0.06 (+11.10%)</td><td>468.20 (+4.67%)</td><td>349.68 (+1.26%)</td><td>286.80 (-5.38%)</td><td>254.50 (+0.67%)</td><td>106.96 (+16.64%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>447.30 (n/a)</td><td>345.32 (n/a)</td><td>303.10 (n/a)</td><td>252.80 (n/a)</td><td>91.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.29 (-5.65%)</td><td>0.23 (+15.53%)</td><td>0.28 <b>(+76.81%)</b></td><td>0.13 (-8.30%)</td><td>0.08 (+4.28%)</td><td>563.10 (+9.06%)</td><td>353.46 (-12.07%)</td><td>266.10 <b>(-43.44%)</b></td><td>253.10 (+5.99%)</td><td>139.28 (+13.25%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>516.30 (n/a)</td><td>402.00 (n/a)</td><td>470.50 (n/a)</td><td>238.80 (n/a)</td><td>122.98 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.24 (-19.76%)</td><td>0.18 (-12.78%)</td><td>0.16 (-11.55%)</td><td>0.12 <b>(-22.11%)</b></td><td>0.05 (-18.68%)</td><td>625.00 <b>(+28.39%)</b></td><td>437.60 (+14.39%)</td><td>464.00 (+13.06%)</td><td>306.30 <b>(+24.61%)</b></td><td>132.28 <b>(+20.06%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>486.80 (n/a)</td><td>382.56 (n/a)</td><td>410.40 (n/a)</td><td>245.80 (n/a)</td><td>110.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.31 <b>(-43.40%)</b></td><td>0.18 <b>(-50.44%)</b></td><td>0.20 <b>(-44.17%)</b></td><td>0.07 <b>(-73.70%)</b></td><td>0.11 (-9.97%)</td><td>2012.40 <b>(+280.27%)</b></td><td>1087.76 <b>(+175.66%)</b></td><td>661.80 <b>(+79.16%)</b></td><td>419.60 <b>(+76.67%)</b></td><td>756.34 <b>(+562.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.55 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>529.20 (n/a)</td><td>394.60 (n/a)</td><td>369.40 (n/a)</td><td>237.50 (n/a)</td><td>114.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.44 <b>(+44.76%)</b></td><td>0.32 <b>(+61.54%)</b></td><td>0.27 <b>(+20.39%)</b></td><td>0.25 <b>(+189.69%)</b></td><td>0.08 (-4.61%)</td><td>522.50 <b>(-65.48%)</b></td><td>436.22 <b>(-47.16%)</b></td><td>480.20 (-16.95%)</td><td>295.40 <b>(-30.92%)</b></td><td>102.51 <b>(-77.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>1513.70 (n/a)</td><td>825.48 (n/a)</td><td>578.20 (n/a)</td><td>427.60 (n/a)</td><td>450.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.46 (+18.62%)</td><td>0.31 (+15.50%)</td><td>0.27 (+14.69%)</td><td>0.18 (-13.39%)</td><td>0.12 <b>(+59.35%)</b></td><td>722.20 (+15.46%)</td><td>481.28 (-7.44%)</td><td>489.70 (-12.80%)</td><td>283.30 (-15.68%)</td><td>177.92 <b>(+56.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>625.50 (n/a)</td><td>519.96 (n/a)</td><td>561.60 (n/a)</td><td>336.00 (n/a)</td><td>113.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (+18.06%)</td><td>0.01 (+16.28%)</td><td>0.01 (+12.45%)</td><td>0.01 <b>(+44.45%)</b></td><td>0.00 (+13.77%)</td><td>496.70 <b>(-30.76%)</b></td><td>351.04 (-16.24%)</td><td>330.00 (-11.08%)</td><td>241.90 (-15.30%)</td><td>114.40 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>717.40 (n/a)</td><td>419.08 (n/a)</td><td>371.10 (n/a)</td><td>285.60 (n/a)</td><td>176.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (-12.30%)</td><td>0.01 (-3.61%)</td><td>0.01 (-15.87%)</td><td>0.01 <b>(+56.48%)</b></td><td>0.00 <b>(-81.54%)</b></td><td>298.70 <b>(-36.09%)</b></td><td>281.40 (-3.51%)</td><td>280.90 (+18.87%)</td><td>261.60 (+13.99%)</td><td>13.79 <b>(-86.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.40 (n/a)</td><td>291.64 (n/a)</td><td>236.30 (n/a)</td><td>229.50 (n/a)</td><td>102.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (+17.64%)</td><td>0.01 (+13.77%)</td><td>0.01 (+6.04%)</td><td>0.01 (+18.57%)</td><td>0.00 (+11.60%)</td><td>478.90 (-15.67%)</td><td>353.80 (-12.58%)</td><td>307.90 (-5.70%)</td><td>262.20 (-14.98%)</td><td>100.42 (-17.73%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.90 (n/a)</td><td>404.70 (n/a)</td><td>326.50 (n/a)</td><td>308.40 (n/a)</td><td>122.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.67 <b>(+35.09%)</b></td><td>0.43 (-6.28%)</td><td>0.33 <b>(-24.98%)</b></td><td>0.21 <b>(-52.24%)</b></td><td>0.21 <b>(+593.93%)</b></td><td>642.00 <b>(+109.39%)</b></td><td>380.36 <b>(+30.32%)</b></td><td>404.50 <b>(+33.28%)</b></td><td>196.90 <b>(-25.98%)</b></td><td>184.82 <b>(+877.28%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.03 (n/a)</td><td>306.60 (n/a)</td><td>291.86 (n/a)</td><td>303.50 (n/a)</td><td>266.00 (n/a)</td><td>18.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.47 (-15.17%)</td><td>0.38 (-14.97%)</td><td>0.33 <b>(-27.31%)</b></td><td>0.30 (-4.16%)</td><td>0.08 (-1.75%)</td><td>435.20 (+4.34%)</td><td>364.08 (+18.10%)</td><td>405.00 <b>(+37.57%)</b></td><td>281.60 (+17.87%)</td><td>74.48 (+13.60%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>417.10 (n/a)</td><td>308.28 (n/a)</td><td>294.40 (n/a)</td><td>238.90 (n/a)</td><td>65.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.48 (-11.39%)</td><td>0.30 <b>(-30.09%)</b></td><td>0.31 <b>(-29.84%)</b></td><td>0.15 <b>(-42.54%)</b></td><td>0.12 <b>(+24.22%)</b></td><td>852.30 <b>(+74.05%)</b></td><td>509.22 <b>(+56.61%)</b></td><td>429.40 <b>(+42.52%)</b></td><td>278.10 (+12.87%)</td><td>223.65 <b>(+135.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>489.70 (n/a)</td><td>325.16 (n/a)</td><td>301.30 (n/a)</td><td>246.40 (n/a)</td><td>95.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.57 (+5.42%)</td><td>0.39 <b>(-20.97%)</b></td><td>0.32 <b>(-34.35%)</b></td><td>0.24 <b>(-45.66%)</b></td><td>0.16 <b>(+263.41%)</b></td><td>553.80 <b>(+84.05%)</b></td><td>390.76 <b>(+44.14%)</b></td><td>411.40 <b>(+52.31%)</b></td><td>232.80 (-5.13%)</td><td>151.47 <b>(+512.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.04 (n/a)</td><td>300.90 (n/a)</td><td>271.10 (n/a)</td><td>270.10 (n/a)</td><td>245.40 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.62 <b>(+29.22%)</b></td><td>0.48 <b>(+28.43%)</b></td><td>0.50 <b>(+42.06%)</b></td><td>0.26 (-18.03%)</td><td>0.14 <b>(+105.50%)</b></td><td>513.50 <b>(+22.00%)</b></td><td>304.58 (-16.40%)</td><td>265.10 <b>(-29.61%)</b></td><td>212.10 <b>(-22.59%)</b></td><td>120.94 <b>(+105.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>420.90 (n/a)</td><td>364.34 (n/a)</td><td>376.60 (n/a)</td><td>274.00 (n/a)</td><td>58.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (-9.49%)</td><td>0.01 (-1.34%)</td><td>0.01 <b>(+31.71%)</b></td><td>0.01 (-16.25%)</td><td>0.00 (+1.07%)</td><td>516.50 (+19.39%)</td><td>366.84 (+3.09%)</td><td>300.10 <b>(-24.06%)</b></td><td>268.30 (+10.50%)</td><td>110.46 <b>(+33.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.60 (n/a)</td><td>355.86 (n/a)</td><td>395.20 (n/a)</td><td>242.80 (n/a)</td><td>82.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.01 (-2.50%)</td><td>0.01 <b>(+31.72%)</b></td><td>0.01 <b>(+37.73%)</b></td><td>0.01 <b>(+73.22%)</b></td><td>0.00 <b>(-72.06%)</b></td><td>331.50 <b>(-42.27%)</b></td><td>301.90 <b>(-27.83%)</b></td><td>298.50 <b>(-27.41%)</b></td><td>284.30 (+2.56%)</td><td>17.95 <b>(-82.95%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.20 (n/a)</td><td>418.32 (n/a)</td><td>411.20 (n/a)</td><td>277.20 (n/a)</td><td>105.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.83%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-16.24%)</td><td>19972.52 (-10.19%)</td><td>12984.47 (+9.28%)</td><td>13998.81 <b>(+101.68%)</b></td><td>5773.07 (+0.37%)</td><td>6034.63 <b>(-24.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22239.00 (n/a)</td><td>11881.83 (n/a)</td><td>6941.04 (n/a)</td><td>5751.93 (n/a)</td><td>7952.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.00 (+20.00%)</td><td>0.00 (+16.13%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+32.81%)</b></td><td>20630.54 (-10.83%)</td><td>14191.21 (-6.33%)</td><td>17666.55 (+15.65%)</td><td>6661.56 <b>(-21.47%)</b></td><td>6433.26 (+5.38%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23135.54 (n/a)</td><td>15150.23 (n/a)</td><td>15276.17 (n/a)</td><td>8482.60 (n/a)</td><td>6105.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.16 (+4.83%)</td><td>0.11 (+17.32%)</td><td>0.08 (+7.15%)</td><td>0.07 (+6.61%)</td><td>0.04 <b>(+22.40%)</b></td><td>29528.24 (-6.23%)</td><td>21722.14 (-12.27%)</td><td>25004.94 (-6.67%)</td><td>13239.53 (-4.61%)</td><td>7537.48 (+9.79%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>31491.52 (n/a)</td><td>24760.08 (n/a)</td><td>26791.93 (n/a)</td><td>13879.13 (n/a)</td><td>6865.51 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns]

_No metrics available._


### test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_1]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_2]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_4]

_No metrics available._


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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.52 <b>(+35.51%)</b></td><td>0.97 <b>(+121.19%)</b></td><td>1.38 <b>(+748.75%)</b></td><td>0.15 (-3.55%)</td><td>0.69 <b>(+61.95%)</b></td><td>3437.30 (+3.68%)</td><td>1274.56 <b>(-43.18%)</b></td><td>380.60 <b>(-88.22%)</b></td><td>345.00 <b>(-26.20%)</b></td><td>1372.84 (-4.17%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.12 (n/a)</td><td>0.44 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.42 (n/a)</td><td>3315.40 (n/a)</td><td>2243.12 (n/a)</td><td>3230.40 (n/a)</td><td>467.50 (n/a)</td><td>1432.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.95 (-11.59%)</td><td>1.81 (-16.04%)</td><td>1.85 (-16.40%)</td><td>0.32 <b>(-69.40%)</b></td><td>1.11 (+16.57%)</td><td>3280.50 <b>(+226.78%)</b></td><td>1103.48 <b>(+88.08%)</b></td><td>566.50 (+19.62%)</td><td>355.40 (+13.11%)</td><td>1239.40 <b>(+326.39%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.34 (n/a)</td><td>2.15 (n/a)</td><td>2.21 (n/a)</td><td>1.04 (n/a)</td><td>0.96 (n/a)</td><td>1003.90 (n/a)</td><td>586.70 (n/a)</td><td>473.60 (n/a)</td><td>314.20 (n/a)</td><td>290.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.07 (+0.36%)</td><td>1.17 (-11.04%)</td><td>0.91 <b>(-24.95%)</b></td><td>0.61 (-8.92%)</td><td>0.62 (+7.07%)</td><td>853.70 (+9.80%)</td><td>554.38 (+17.31%)</td><td>576.10 <b>(+33.23%)</b></td><td>253.70 (-0.35%)</td><td>258.22 (+19.20%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.06 (n/a)</td><td>1.31 (n/a)</td><td>1.21 (n/a)</td><td>0.67 (n/a)</td><td>0.58 (n/a)</td><td>777.50 (n/a)</td><td>472.58 (n/a)</td><td>432.40 (n/a)</td><td>254.60 (n/a)</td><td>216.63 (n/a)</td>
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
