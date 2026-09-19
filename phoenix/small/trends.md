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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.06 <b>(+31.91%)</b></td><td>0.03 (-2.86%)</td><td>0.03 <b>(-31.67%)</b></td><td>0.02 <b>(-29.91%)</b></td><td>0.02 <b>(+129.40%)</b></td><td>638.90 <b>(+42.68%)</b></td><td>426.46 (+17.86%)</td><td>488.40 <b>(+46.36%)</b></td><td>207.40 <b>(-24.17%)</b></td><td>176.47 <b>(+134.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>447.80 (n/a)</td><td>361.84 (n/a)</td><td>333.70 (n/a)</td><td>273.50 (n/a)</td><td>75.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.07 <b>(+55.78%)</b></td><td>0.04 (+18.46%)</td><td>0.04 <b>(+29.83%)</b></td><td>0.02 (-4.84%)</td><td>0.02 <b>(+103.30%)</b></td><td>596.70 (+5.07%)</td><td>373.04 (-1.26%)</td><td>283.00 <b>(-22.99%)</b></td><td>171.30 <b>(-35.79%)</b></td><td>199.34 <b>(+59.73%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.90 (n/a)</td><td>377.80 (n/a)</td><td>367.50 (n/a)</td><td>266.80 (n/a)</td><td>124.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (-2.27%)</td><td>0.04 (+1.30%)</td><td>0.04 (-7.47%)</td><td>0.02 (-11.47%)</td><td>0.01 (-14.23%)</td><td>561.90 (+12.94%)</td><td>348.62 (-2.72%)</td><td>310.00 (+8.05%)</td><td>243.00 (+2.32%)</td><td>123.30 (-0.56%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.50 (n/a)</td><td>358.38 (n/a)</td><td>286.90 (n/a)</td><td>237.50 (n/a)</td><td>124.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (-6.52%)</td><td>0.02 <b>(+33.49%)</b></td><td>0.02 <b>(+71.64%)</b></td><td>0.01 <b>(+47.41%)</b></td><td>0.00 <b>(-32.75%)</b></td><td>446.40 <b>(-32.16%)</b></td><td>328.16 <b>(-31.61%)</b></td><td>300.50 <b>(-41.73%)</b></td><td>241.20 (+6.96%)</td><td>86.45 <b>(-49.17%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.00 (n/a)</td><td>479.82 (n/a)</td><td>515.70 (n/a)</td><td>225.50 (n/a)</td><td>170.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 <b>(+50.31%)</b></td><td>0.02 (+7.16%)</td><td>0.01 <b>(-34.48%)</b></td><td>0.01 (+8.37%)</td><td>0.01 <b>(+76.81%)</b></td><td>457.20 (-7.73%)</td><td>336.80 (+0.32%)</td><td>407.10 <b>(+52.64%)</b></td><td>168.50 <b>(-33.45%)</b></td><td>127.27 (+14.77%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.50 (n/a)</td><td>335.74 (n/a)</td><td>266.70 (n/a)</td><td>253.20 (n/a)</td><td>110.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (-8.84%)</td><td>0.02 (-3.24%)</td><td>0.01 (+10.29%)</td><td>0.01 <b>(+28.87%)</b></td><td>0.00 <b>(-41.28%)</b></td><td>446.80 <b>(-22.40%)</b></td><td>359.26 (-5.37%)</td><td>388.10 (-9.32%)</td><td>249.50 (+9.72%)</td><td>79.31 <b>(-46.36%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.80 (n/a)</td><td>379.64 (n/a)</td><td>428.00 (n/a)</td><td>227.40 (n/a)</td><td>147.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (-18.58%)</td><td>0.01 <b>(-33.94%)</b></td><td>0.01 <b>(-28.57%)</b></td><td>0.00 <b>(-79.22%)</b></td><td>0.01 (+15.82%)</td><td>2441.30 <b>(+381.23%)</b></td><td>892.38 <b>(+131.79%)</b></td><td>602.40 <b>(+40.00%)</b></td><td>299.70 <b>(+22.83%)</b></td><td>882.99 <b>(+638.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>385.00 (n/a)</td><td>430.30 (n/a)</td><td>244.00 (n/a)</td><td>119.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (-2.72%)</td><td>0.01 <b>(-28.39%)</b></td><td>0.01 <b>(-49.55%)</b></td><td>0.01 <b>(-41.88%)</b></td><td>0.01 <b>(+94.73%)</b></td><td>637.90 <b>(+72.08%)</b></td><td>475.02 <b>(+59.81%)</b></td><td>572.30 <b>(+98.16%)</b></td><td>236.60 (+2.78%)</td><td>185.53 <b>(+257.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>370.70 (n/a)</td><td>297.24 (n/a)</td><td>288.80 (n/a)</td><td>230.20 (n/a)</td><td>51.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.01 <b>(-44.70%)</b></td><td>0.01 (-19.26%)</td><td>0.01 (-8.72%)</td><td>0.01 <b>(+57.84%)</b></td><td>0.00 <b>(-83.02%)</b></td><td>585.70 <b>(-36.65%)</b></td><td>505.42 (+0.06%)</td><td>491.90 (+9.55%)</td><td>438.00 <b>(+80.84%)</b></td><td>53.83 <b>(-80.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>924.50 (n/a)</td><td>505.10 (n/a)</td><td>449.00 (n/a)</td><td>242.20 (n/a)</td><td>272.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.90 (n/a)</td><td>359.18 (n/a)</td><td>291.10 (n/a)</td><td>223.50 (n/a)</td><td>149.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>294.00 (n/a)</td><td>262.40 (n/a)</td><td>258.70 (n/a)</td><td>239.70 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1053.70 (n/a)</td><td>435.08 (n/a)</td><td>294.40 (n/a)</td><td>263.50 (n/a)</td><td>346.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>320.80 (n/a)</td><td>285.28 (n/a)</td><td>285.80 (n/a)</td><td>224.50 (n/a)</td><td>38.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>573.10 (n/a)</td><td>323.68 (n/a)</td><td>268.20 (n/a)</td><td>201.20 (n/a)</td><td>148.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.20 (n/a)</td><td>450.98 (n/a)</td><td>476.80 (n/a)</td><td>268.70 (n/a)</td><td>108.75 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.24 <b>(+80.71%)</b></td><td>0.75 <b>(+20.79%)</b></td><td>0.65 (+2.45%)</td><td>0.51 (-0.27%)</td><td>0.28 <b>(+321.48%)</b></td><td>906.90 (+0.27%)</td><td>667.46 (-10.51%)</td><td>703.40 (-2.39%)</td><td>369.80 <b>(-44.66%)</b></td><td>193.73 <b>(+111.87%)</b></td><td>90.74 <b>(+80.71%)</b></td><td>54.92 <b>(+20.79%)</b></td><td>47.71 (+2.45%)</td><td>37.00 (-0.27%)</td><td>20.78 <b>(+321.48%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.69 (n/a)</td><td>0.62 (n/a)</td><td>0.64 (n/a)</td><td>0.51 (n/a)</td><td>0.07 (n/a)</td><td>904.50 (n/a)</td><td>745.84 (n/a)</td><td>720.60 (n/a)</td><td>668.20 (n/a)</td><td>91.44 (n/a)</td><td>50.22 (n/a)</td><td>45.47 (n/a)</td><td>46.56 (n/a)</td><td>37.10 (n/a)</td><td>4.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.82 <b>(+57.02%)</b></td><td>1.28 <b>(+53.32%)</b></td><td>1.16 <b>(+29.74%)</b></td><td>0.88 <b>(+374.24%)</b></td><td>0.36 (-4.98%)</td><td>747.60 <b>(-78.91%)</b></td><td>543.90 <b>(-56.18%)</b></td><td>562.90 <b>(-22.92%)</b></td><td>360.60 <b>(-36.32%)</b></td><td>147.41 <b>(-88.58%)</b></td><td>186.08 <b>(+57.02%)</b></td><td>131.24 <b>(+53.32%)</b></td><td>119.22 <b>(+29.74%)</b></td><td>89.77 <b>(+374.24%)</b></td><td>37.20 (-4.98%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.16 (n/a)</td><td>0.84 (n/a)</td><td>0.90 (n/a)</td><td>0.18 (n/a)</td><td>0.38 (n/a)</td><td>3545.40 (n/a)</td><td>1241.26 (n/a)</td><td>730.30 (n/a)</td><td>566.30 (n/a)</td><td>1290.33 (n/a)</td><td>118.51 (n/a)</td><td>85.59 (n/a)</td><td>91.90 (n/a)</td><td>18.93 (n/a)</td><td>39.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.51 (-5.89%)</td><td>0.98 (-14.83%)</td><td>0.84 <b>(-21.38%)</b></td><td>0.66 <b>(-32.12%)</b></td><td>0.35 <b>(+36.29%)</b></td><td>1137.70 <b>(+47.31%)</b></td><td>845.52 <b>(+24.77%)</b></td><td>902.10 <b>(+27.20%)</b></td><td>499.10 (+6.26%)</td><td>266.66 <b>(+119.67%)</b></td><td>168.09 (-5.89%)</td><td>108.93 (-14.83%)</td><td>92.99 <b>(-21.38%)</b></td><td>73.73 <b>(-32.12%)</b></td><td>39.36 <b>(+36.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.60 (n/a)</td><td>1.15 (n/a)</td><td>1.06 (n/a)</td><td>0.98 (n/a)</td><td>0.26 (n/a)</td><td>772.30 (n/a)</td><td>677.66 (n/a)</td><td>709.20 (n/a)</td><td>469.70 (n/a)</td><td>121.39 (n/a)</td><td>178.60 (n/a)</td><td>127.91 (n/a)</td><td>118.28 (n/a)</td><td>108.62 (n/a)</td><td>28.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.59 (-9.95%)</td><td>0.95 (-9.01%)</td><td>1.14 <b>(+39.32%)</b></td><td>0.30 <b>(-43.43%)</b></td><td>0.54 (+0.48%)</td><td>3491.90 <b>(+76.79%)</b></td><td>1613.90 <b>(+30.86%)</b></td><td>921.40 <b>(-28.22%)</b></td><td>658.40 (+11.05%)</td><td>1203.94 <b>(+106.86%)</b></td><td>203.86 (-9.95%)</td><td>121.79 (-9.01%)</td><td>145.67 <b>(+39.32%)</b></td><td>38.44 <b>(-43.43%)</b></td><td>69.17 (+0.48%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.77 (n/a)</td><td>1.05 (n/a)</td><td>0.82 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>1975.20 (n/a)</td><td>1233.28 (n/a)</td><td>1283.70 (n/a)</td><td>592.90 (n/a)</td><td>582.02 (n/a)</td><td>226.38 (n/a)</td><td>133.85 (n/a)</td><td>104.56 (n/a)</td><td>67.95 (n/a)</td><td>68.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.36 <b>(-25.66%)</b></td><td>0.96 <b>(-31.70%)</b></td><td>1.30 (+0.30%)</td><td>0.31 <b>(-73.58%)</b></td><td>0.52 <b>(+87.55%)</b></td><td>3432.90 <b>(+278.45%)</b></td><td>1579.18 <b>(+106.12%)</b></td><td>807.60 (-0.30%)</td><td>773.30 <b>(+34.53%)</b></td><td>1183.06 <b>(+767.92%)</b></td><td>173.57 <b>(-25.66%)</b></td><td>123.03 <b>(-31.70%)</b></td><td>166.20 (+0.30%)</td><td>39.10 <b>(-73.58%)</b></td><td>65.99 <b>(+87.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.82 (n/a)</td><td>1.41 (n/a)</td><td>1.29 (n/a)</td><td>1.16 (n/a)</td><td>0.27 (n/a)</td><td>907.10 (n/a)</td><td>766.16 (n/a)</td><td>810.00 (n/a)</td><td>574.80 (n/a)</td><td>136.31 (n/a)</td><td>233.49 (n/a)</td><td>180.15 (n/a)</td><td>165.70 (n/a)</td><td>147.96 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>2.16 (+2.91%)</td><td>1.62 (+10.35%)</td><td>1.65 <b>(+25.55%)</b></td><td>0.93 (-11.20%)</td><td>0.51 (+8.06%)</td><td>1129.70 (+12.62%)</td><td>712.70 (-7.93%)</td><td>637.00 <b>(-20.36%)</b></td><td>486.10 (-2.84%)</td><td>263.07 (+14.10%)</td><td>276.10 (+2.91%)</td><td>206.97 (+10.35%)</td><td>210.70 <b>(+25.55%)</b></td><td>118.81 (-11.20%)</td><td>65.00 (+8.06%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.10 (n/a)</td><td>1.47 (n/a)</td><td>1.31 (n/a)</td><td>1.05 (n/a)</td><td>0.47 (n/a)</td><td>1003.10 (n/a)</td><td>774.08 (n/a)</td><td>799.80 (n/a)</td><td>500.30 (n/a)</td><td>230.56 (n/a)</td><td>268.28 (n/a)</td><td>187.55 (n/a)</td><td>167.82 (n/a)</td><td>133.80 (n/a)</td><td>60.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.84 (+16.16%)</td><td>0.94 <b>(-31.37%)</b></td><td>0.49 <b>(-66.08%)</b></td><td>0.30 <b>(-67.87%)</b></td><td>0.76 <b>(+191.67%)</b></td><td>3521.30 <b>(+211.26%)</b></td><td>1916.76 <b>(+141.66%)</b></td><td>2127.10 <b>(+194.78%)</b></td><td>571.00 (-13.92%)</td><td>1304.80 <b>(+577.77%)</b></td><td>235.05 (+16.16%)</td><td>120.54 <b>(-31.37%)</b></td><td>63.10 <b>(-66.08%)</b></td><td>38.12 <b>(-67.87%)</b></td><td>97.17 <b>(+191.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.58 (n/a)</td><td>1.37 (n/a)</td><td>1.45 (n/a)</td><td>0.93 (n/a)</td><td>0.26 (n/a)</td><td>1131.30 (n/a)</td><td>793.16 (n/a)</td><td>721.60 (n/a)</td><td>663.30 (n/a)</td><td>192.51 (n/a)</td><td>202.35 (n/a)</td><td>175.65 (n/a)</td><td>186.00 (n/a)</td><td>118.64 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.90 (+12.23%)</td><td>0.65 (+2.31%)</td><td>0.52 <b>(-27.43%)</b></td><td>0.47 <b>(+25.83%)</b></td><td>0.20 (+5.78%)</td><td>768.40 <b>(-20.53%)</b></td><td>597.34 (-3.90%)</td><td>689.40 <b>(+37.80%)</b></td><td>400.20 (-10.89%)</td><td>165.95 <b>(-25.25%)</b></td><td>41.92 (+12.23%)</td><td>30.13 (+2.31%)</td><td>24.34 <b>(-27.43%)</b></td><td>21.83 <b>(+25.83%)</b></td><td>9.22 (+5.78%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.80 (n/a)</td><td>0.63 (n/a)</td><td>0.72 (n/a)</td><td>0.37 (n/a)</td><td>0.19 (n/a)</td><td>966.90 (n/a)</td><td>621.56 (n/a)</td><td>500.30 (n/a)</td><td>449.10 (n/a)</td><td>221.99 (n/a)</td><td>37.35 (n/a)</td><td>29.45 (n/a)</td><td>33.54 (n/a)</td><td>17.35 (n/a)</td><td>8.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>4.07 (+17.89%)</td><td>2.90 <b>(+33.27%)</b></td><td>2.67 (+11.32%)</td><td>1.28 <b>(+86.65%)</b></td><td>1.15 (-5.90%)</td><td>2049.80 <b>(-46.42%)</b></td><td>1075.74 <b>(-38.71%)</b></td><td>982.10 (-10.17%)</td><td>643.30 (-15.18%)</td><td>573.21 <b>(-56.21%)</b></td><td>834.50 (+17.89%)</td><td>593.40 <b>(+33.27%)</b></td><td>546.64 (+11.32%)</td><td>261.92 <b>(+86.65%)</b></td><td>235.32 (-5.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.46 (n/a)</td><td>2.17 (n/a)</td><td>2.40 (n/a)</td><td>0.69 (n/a)</td><td>1.22 (n/a)</td><td>3825.90 (n/a)</td><td>1755.22 (n/a)</td><td>1093.30 (n/a)</td><td>758.40 (n/a)</td><td>1309.04 (n/a)</td><td>707.88 (n/a)</td><td>445.28 (n/a)</td><td>491.04 (n/a)</td><td>140.33 (n/a)</td><td>250.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.90 (n/a)</td><td>454.76 (n/a)</td><td>529.50 (n/a)</td><td>279.00 (n/a)</td><td>159.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2478.30 (n/a)</td><td>928.12 (n/a)</td><td>565.80 (n/a)</td><td>259.00 (n/a)</td><td>925.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.30 (n/a)</td><td>395.52 (n/a)</td><td>459.60 (n/a)</td><td>214.60 (n/a)</td><td>132.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1003.90 (n/a)</td><td>503.18 (n/a)</td><td>414.10 (n/a)</td><td>272.60 (n/a)</td><td>291.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.00 (n/a)</td><td>425.20 (n/a)</td><td>486.70 (n/a)</td><td>248.20 (n/a)</td><td>153.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>411.46 (n/a)</td><td>397.90 (n/a)</td><td>291.50 (n/a)</td><td>106.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.55 (-13.23%)</td><td>0.37 (-18.39%)</td><td>0.37 <b>(-23.03%)</b></td><td>0.17 <b>(-46.75%)</b></td><td>0.14 (+6.53%)</td><td>1295.00 <b>(+87.79%)</b></td><td>692.66 <b>(+33.57%)</b></td><td>602.20 <b>(+29.92%)</b></td><td>399.00 (+15.25%)</td><td>349.27 <b>(+138.64%)</b></td><td>23.66 (-13.23%)</td><td>15.86 (-18.39%)</td><td>15.67 <b>(-23.03%)</b></td><td>7.29 <b>(-46.75%)</b></td><td>5.92 (+6.53%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.64 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.13 (n/a)</td><td>689.60 (n/a)</td><td>518.58 (n/a)</td><td>463.50 (n/a)</td><td>346.20 (n/a)</td><td>146.36 (n/a)</td><td>27.26 (n/a)</td><td>19.43 (n/a)</td><td>20.36 (n/a)</td><td>13.69 (n/a)</td><td>5.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.60 (+3.44%)</td><td>0.43 (-3.61%)</td><td>0.41 (-3.11%)</td><td>0.34 (-5.53%)</td><td>0.10 (+11.35%)</td><td>658.30 (+5.85%)</td><td>530.04 (+4.44%)</td><td>544.30 (+3.20%)</td><td>365.70 (-3.33%)</td><td>106.57 (+10.39%)</td><td>25.80 (+3.44%)</td><td>18.49 (-3.61%)</td><td>17.34 (-3.11%)</td><td>14.33 (-5.53%)</td><td>4.35 (+11.35%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>621.90 (n/a)</td><td>507.50 (n/a)</td><td>527.40 (n/a)</td><td>378.30 (n/a)</td><td>96.54 (n/a)</td><td>24.95 (n/a)</td><td>19.18 (n/a)</td><td>17.89 (n/a)</td><td>15.17 (n/a)</td><td>3.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.31 (-1.33%)</td><td>0.30 (-1.84%)</td><td>0.30 (-1.46%)</td><td>0.30 (-2.82%)</td><td>0.01 <b>(+93.38%)</b></td><td>85232.60 (+2.90%)</td><td>83185.76 (+1.90%)</td><td>82684.10 (+1.49%)</td><td>81656.20 (+1.35%)</td><td>1684.88 <b>(+101.33%)</b></td><td>210.39 (-1.33%)</td><td>206.59 (-1.84%)</td><td>207.78 (-1.46%)</td><td>201.56 (-2.82%)</td><td>4.16 <b>(+93.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82829.70 (n/a)</td><td>81633.18 (n/a)</td><td>81474.10 (n/a)</td><td>80569.10 (n/a)</td><td>836.86 (n/a)</td><td>213.23 (n/a)</td><td>210.47 (n/a)</td><td>210.86 (n/a)</td><td>207.41 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.15 (-1.36%)</td><td>1.14 (+0.81%)</td><td>1.15 (+0.04%)</td><td>1.10 (+2.74%)</td><td>0.02 <b>(-44.41%)</b></td><td>22853.70 (-2.66%)</td><td>22110.34 (-0.87%)</td><td>21919.30 (-0.04%)</td><td>21885.00 (+1.38%)</td><td>418.12 <b>(-45.19%)</b></td><td>785.01 (-1.36%)</td><td>777.22 (+0.81%)</td><td>783.78 (+0.04%)</td><td>751.73 (+2.74%)</td><td>14.35 <b>(-44.41%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.17 (n/a)</td><td>1.13 (n/a)</td><td>1.15 (n/a)</td><td>1.07 (n/a)</td><td>0.04 (n/a)</td><td>23478.80 (n/a)</td><td>22304.34 (n/a)</td><td>21928.50 (n/a)</td><td>21586.50 (n/a)</td><td>762.82 (n/a)</td><td>795.86 (n/a)</td><td>770.95 (n/a)</td><td>783.45 (n/a)</td><td>731.72 (n/a)</td><td>25.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>4.19 (+11.20%)</td><td>2.90 <b>(+25.89%)</b></td><td>2.62 <b>(+42.33%)</b></td><td>1.93 <b>(+35.21%)</b></td><td>0.98 (+3.91%)</td><td>4180.50 <b>(-26.04%)</b></td><td>3035.26 <b>(-22.77%)</b></td><td>3080.20 <b>(-29.74%)</b></td><td>1923.30 (-10.07%)</td><td>971.19 <b>(-29.39%)</b></td><td>1099.13 (+11.20%)</td><td>761.01 <b>(+25.89%)</b></td><td>686.29 <b>(+42.33%)</b></td><td>505.66 <b>(+35.21%)</b></td><td>256.42 (+3.91%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.77 (n/a)</td><td>2.31 (n/a)</td><td>1.84 (n/a)</td><td>1.43 (n/a)</td><td>0.94 (n/a)</td><td>5652.30 (n/a)</td><td>3930.34 (n/a)</td><td>4384.00 (n/a)</td><td>2138.60 (n/a)</td><td>1375.39 (n/a)</td><td>988.47 (n/a)</td><td>604.49 (n/a)</td><td>482.19 (n/a)</td><td>374.00 (n/a)</td><td>246.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.21 (+0.75%)</td><td>0.20 (+2.84%)</td><td>0.19 (+0.05%)</td><td>0.19 (+4.78%)</td><td>0.01 (-16.57%)</td><td>6504.20 (-4.56%)</td><td>6254.52 (-2.86%)</td><td>6410.80 (-0.05%)</td><td>5800.70 (-0.74%)</td><td>306.89 <b>(-20.68%)</b></td><td>11.57 (+0.75%)</td><td>10.75 (+2.84%)</td><td>10.47 (+0.05%)</td><td>10.32 (+4.78%)</td><td>0.54 (-16.57%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>6815.30 (n/a)</td><td>6438.68 (n/a)</td><td>6413.90 (n/a)</td><td>5844.00 (n/a)</td><td>386.88 (n/a)</td><td>11.48 (n/a)</td><td>10.45 (n/a)</td><td>10.46 (n/a)</td><td>9.85 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.87 (n/a)</td><td>3.63 (n/a)</td><td>3.61 (n/a)</td><td>3.42 (n/a)</td><td>0.16 (n/a)</td><td>3.87 (n/a)</td><td>3.63 (n/a)</td><td>3.61 (n/a)</td><td>3.42 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>7.16 (+6.87%)</td><td>6.35 (+6.58%)</td><td>6.54 (+13.21%)</td><td>5.68 (+8.48%)</td><td>0.61 (-3.16%)</td><td>7.16 (+6.87%)</td><td>6.35 (+6.58%)</td><td>6.54 (+13.21%)</td><td>5.68 (+8.48%)</td><td>0.61 (-3.16%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>6.70 (n/a)</td><td>5.96 (n/a)</td><td>5.78 (n/a)</td><td>5.24 (n/a)</td><td>0.63 (n/a)</td><td>6.70 (n/a)</td><td>5.96 (n/a)</td><td>5.77 (n/a)</td><td>5.23 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>10.60 (+7.35%)</td><td>8.89 (+2.79%)</td><td>8.42 (-6.02%)</td><td>7.23 (+1.99%)</td><td>1.38 <b>(+25.81%)</b></td><td>10.59 (+7.35%)</td><td>8.89 (+2.79%)</td><td>8.41 (-6.02%)</td><td>7.23 (+1.99%)</td><td>1.37 <b>(+25.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>9.87 (n/a)</td><td>8.65 (n/a)</td><td>8.96 (n/a)</td><td>7.09 (n/a)</td><td>1.09 (n/a)</td><td>9.87 (n/a)</td><td>8.64 (n/a)</td><td>8.95 (n/a)</td><td>7.09 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.93 (n/a)</td><td>3.66 (n/a)</td><td>3.72 (n/a)</td><td>3.40 (n/a)</td><td>0.22 (n/a)</td><td>3.92 (n/a)</td><td>3.65 (n/a)</td><td>3.72 (n/a)</td><td>3.39 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>7.61 (+7.78%)</td><td>6.92 (+11.96%)</td><td>7.16 (+11.07%)</td><td>5.74 (+18.66%)</td><td>0.75 <b>(-21.88%)</b></td><td>7.61 (+7.78%)</td><td>6.92 (+11.96%)</td><td>7.15 (+11.07%)</td><td>5.73 (+18.66%)</td><td>0.75 <b>(-21.88%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>7.06 (n/a)</td><td>6.18 (n/a)</td><td>6.44 (n/a)</td><td>4.83 (n/a)</td><td>0.96 (n/a)</td><td>7.06 (n/a)</td><td>6.18 (n/a)</td><td>6.44 (n/a)</td><td>4.83 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>12.95 (-5.71%)</td><td>9.47 (-4.22%)</td><td>8.35 (-9.15%)</td><td>7.45 (-8.95%)</td><td>2.43 (+9.35%)</td><td>12.94 (-5.71%)</td><td>9.47 (-4.22%)</td><td>8.34 (-9.15%)</td><td>7.44 (-8.95%)</td><td>2.43 (+9.35%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>13.74 (n/a)</td><td>9.89 (n/a)</td><td>9.19 (n/a)</td><td>8.18 (n/a)</td><td>2.22 (n/a)</td><td>13.73 (n/a)</td><td>9.89 (n/a)</td><td>9.18 (n/a)</td><td>8.17 (n/a)</td><td>2.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.00 (-5.64%)</td><td>2.29 (-1.49%)</td><td>2.75 (-1.96%)</td><td>1.01 (-18.65%)</td><td>0.89 (+0.52%)</td><td>2.99 (-5.64%)</td><td>2.28 (-1.49%)</td><td>2.74 (-1.96%)</td><td>1.01 (-18.65%)</td><td>0.89 (+0.52%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.18 (n/a)</td><td>2.32 (n/a)</td><td>2.80 (n/a)</td><td>1.24 (n/a)</td><td>0.88 (n/a)</td><td>3.17 (n/a)</td><td>2.32 (n/a)</td><td>2.80 (n/a)</td><td>1.24 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.58 (+3.30%)</td><td>0.48 (+7.62%)</td><td>0.50 (+9.31%)</td><td>0.34 (+0.20%)</td><td>0.09 (-15.10%)</td><td>0.58 (+3.30%)</td><td>0.47 (+7.62%)</td><td>0.49 (+9.31%)</td><td>0.33 (+0.20%)</td><td>0.09 (-15.10%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.82 (+10.33%)</td><td>0.40 (-13.46%)</td><td>0.47 <b>(+39.61%)</b></td><td>0.08 <b>(-67.49%)</b></td><td>0.30 <b>(+24.47%)</b></td><td>0.81 (+10.33%)</td><td>0.39 (-13.46%)</td><td>0.47 <b>(+39.61%)</b></td><td>0.08 <b>(-67.49%)</b></td><td>0.30 <b>(+24.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.75 (n/a)</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.74 (n/a)</td><td>0.46 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.78 <b>(-31.22%)</b></td><td>1.07 <b>(-40.00%)</b></td><td>1.19 <b>(-50.13%)</b></td><td>0.43 (-2.01%)</td><td>0.61 <b>(-36.54%)</b></td><td>1.75 <b>(-31.22%)</b></td><td>1.06 <b>(-40.00%)</b></td><td>1.18 <b>(-50.13%)</b></td><td>0.42 (-2.01%)</td><td>0.60 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.58 (n/a)</td><td>1.79 (n/a)</td><td>2.40 (n/a)</td><td>0.44 (n/a)</td><td>0.96 (n/a)</td><td>2.54 (n/a)</td><td>1.76 (n/a)</td><td>2.36 (n/a)</td><td>0.43 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.90 (n/a)</td><td>348.20 (n/a)</td><td>331.40 (n/a)</td><td>268.90 (n/a)</td><td>93.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>742.30 (n/a)</td><td>489.30 (n/a)</td><td>441.20 (n/a)</td><td>297.50 (n/a)</td><td>195.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1169.30 (n/a)</td><td>528.56 (n/a)</td><td>470.00 (n/a)</td><td>229.60 (n/a)</td><td>374.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.00 (n/a)</td><td>392.56 (n/a)</td><td>348.10 (n/a)</td><td>245.40 (n/a)</td><td>169.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.60 (n/a)</td><td>379.84 (n/a)</td><td>456.50 (n/a)</td><td>243.60 (n/a)</td><td>123.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.20 (n/a)</td><td>372.56 (n/a)</td><td>356.60 (n/a)</td><td>270.70 (n/a)</td><td>98.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (+13.86%)</td><td>0.03 <b>(+30.78%)</b></td><td>0.03 <b>(+54.12%)</b></td><td>0.02 <b>(+50.35%)</b></td><td>0.01 (-3.84%)</td><td>425.60 <b>(-33.49%)</b></td><td>324.80 <b>(-26.75%)</b></td><td>280.60 <b>(-35.12%)</b></td><td>236.40 (-12.18%)</td><td>92.44 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.90 (n/a)</td><td>443.42 (n/a)</td><td>432.50 (n/a)</td><td>269.20 (n/a)</td><td>156.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+2.66%)</td><td>0.03 (-1.68%)</td><td>0.03 (-4.92%)</td><td>0.02 (+9.64%)</td><td>0.01 (-3.57%)</td><td>403.60 (-8.79%)</td><td>278.72 (+0.20%)</td><td>261.60 (+5.19%)</td><td>193.20 (-2.57%)</td><td>79.07 (-17.36%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.50 (n/a)</td><td>278.16 (n/a)</td><td>248.70 (n/a)</td><td>198.30 (n/a)</td><td>95.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (-2.89%)</td><td>0.03 (-10.24%)</td><td>0.03 (-18.34%)</td><td>0.02 (+13.05%)</td><td>0.01 <b>(-27.32%)</b></td><td>454.20 (-11.55%)</td><td>312.78 (+6.03%)</td><td>294.00 <b>(+22.45%)</b></td><td>229.00 (+2.97%)</td><td>83.86 <b>(-32.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.50 (n/a)</td><td>295.00 (n/a)</td><td>240.10 (n/a)</td><td>222.40 (n/a)</td><td>123.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (+9.13%)</td><td>0.02 (-9.35%)</td><td>0.03 (-10.51%)</td><td>0.01 (-1.77%)</td><td>0.01 <b>(+20.51%)</b></td><td>562.20 (+1.81%)</td><td>373.72 (+13.54%)</td><td>299.10 (+11.73%)</td><td>236.90 (-8.39%)</td><td>144.10 (+14.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.20 (n/a)</td><td>329.16 (n/a)</td><td>267.70 (n/a)</td><td>258.60 (n/a)</td><td>126.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (-10.64%)</td><td>0.02 <b>(-25.44%)</b></td><td>0.02 <b>(-45.56%)</b></td><td>0.01 <b>(-29.85%)</b></td><td>0.01 <b>(+34.96%)</b></td><td>594.60 <b>(+42.56%)</b></td><td>425.50 <b>(+47.23%)</b></td><td>514.60 <b>(+83.65%)</b></td><td>229.40 (+11.90%)</td><td>164.42 <b>(+107.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>417.10 (n/a)</td><td>289.00 (n/a)</td><td>280.20 (n/a)</td><td>205.00 (n/a)</td><td>79.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 <b>(+38.21%)</b></td><td>0.02 (+15.42%)</td><td>0.01 (-14.80%)</td><td>0.01 (-1.93%)</td><td>0.01 <b>(+82.61%)</b></td><td>590.80 (+1.95%)</td><td>434.62 (-2.13%)</td><td>557.20 (+17.35%)</td><td>208.90 <b>(-27.64%)</b></td><td>192.85 <b>(+38.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>444.10 (n/a)</td><td>474.80 (n/a)</td><td>288.70 (n/a)</td><td>138.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+8.95%)</td><td>0.02 (-1.17%)</td><td>0.01 (-14.80%)</td><td>0.01 <b>(-21.05%)</b></td><td>0.01 <b>(+46.36%)</b></td><td>643.80 <b>(+26.66%)</b></td><td>457.98 (+13.04%)</td><td>565.40 (+17.38%)</td><td>233.10 (-8.23%)</td><td>201.46 <b>(+61.77%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.30 (n/a)</td><td>405.14 (n/a)</td><td>481.70 (n/a)</td><td>254.00 (n/a)</td><td>124.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-2.23%)</td><td>0.02 (+3.78%)</td><td>0.02 (+17.84%)</td><td>0.01 (-17.51%)</td><td>0.01 (+8.80%)</td><td>685.70 <b>(+21.23%)</b></td><td>466.70 (-0.46%)</td><td>434.80 (-15.13%)</td><td>283.60 (+2.27%)</td><td>161.04 <b>(+43.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>468.88 (n/a)</td><td>512.30 (n/a)</td><td>277.30 (n/a)</td><td>112.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-12.07%)</td><td>0.03 (-19.22%)</td><td>0.03 (-18.35%)</td><td>0.02 <b>(-37.89%)</b></td><td>0.01 <b>(+83.42%)</b></td><td>464.70 <b>(+61.02%)</b></td><td>323.92 <b>(+27.88%)</b></td><td>299.20 <b>(+22.47%)</b></td><td>265.30 (+13.72%)</td><td>80.14 <b>(+252.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>288.60 (n/a)</td><td>253.30 (n/a)</td><td>244.30 (n/a)</td><td>233.30 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (+9.07%)</td><td>0.02 (-3.61%)</td><td>0.02 (-16.45%)</td><td>0.02 (+10.03%)</td><td>0.01 (+0.95%)</td><td>529.80 (-9.11%)</td><td>408.76 (+2.58%)</td><td>445.80 (+19.71%)</td><td>255.40 (-8.33%)</td><td>106.77 (-15.93%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.90 (n/a)</td><td>398.46 (n/a)</td><td>372.40 (n/a)</td><td>278.60 (n/a)</td><td>127.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 <b>(+41.63%)</b></td><td>0.03 <b>(+31.88%)</b></td><td>0.03 <b>(+48.31%)</b></td><td>0.01 (+10.00%)</td><td>0.01 <b>(+63.22%)</b></td><td>617.90 (-9.11%)</td><td>369.76 (-17.81%)</td><td>258.10 <b>(-32.56%)</b></td><td>203.90 <b>(-29.40%)</b></td><td>189.59 (+8.35%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.80 (n/a)</td><td>449.90 (n/a)</td><td>382.70 (n/a)</td><td>288.80 (n/a)</td><td>174.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 <b>(+67.51%)</b></td><td>0.02 (+11.18%)</td><td>0.01 (-13.45%)</td><td>0.01 (-19.16%)</td><td>0.01 <b>(+321.36%)</b></td><td>670.80 <b>(+23.72%)</b></td><td>491.48 (+1.50%)</td><td>548.10 (+15.54%)</td><td>240.60 <b>(-40.31%)</b></td><td>169.34 <b>(+197.91%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>542.20 (n/a)</td><td>484.20 (n/a)</td><td>474.40 (n/a)</td><td>403.10 (n/a)</td><td>56.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-15.85%)</td><td>0.03 (+15.86%)</td><td>0.03 (+11.08%)</td><td>0.03 <b>(+69.10%)</b></td><td>0.00 <b>(-84.03%)</b></td><td>300.30 <b>(-40.85%)</b></td><td>277.90 <b>(-21.42%)</b></td><td>274.70 (-9.96%)</td><td>265.10 (+18.83%)</td><td>13.41 <b>(-89.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.70 (n/a)</td><td>353.64 (n/a)</td><td>305.10 (n/a)</td><td>223.10 (n/a)</td><td>122.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 <b>(+114.86%)</b></td><td>0.02 <b>(+89.31%)</b></td><td>0.02 <b>(+34.96%)</b></td><td>0.02 <b>(+312.56%)</b></td><td>0.01 <b>(+61.24%)</b></td><td>468.30 <b>(-75.76%)</b></td><td>379.38 <b>(-55.90%)</b></td><td>437.10 <b>(-25.90%)</b></td><td>213.90 <b>(-53.46%)</b></td><td>111.99 <b>(-81.83%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1932.00 (n/a)</td><td>860.34 (n/a)</td><td>589.90 (n/a)</td><td>459.60 (n/a)</td><td>616.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.12 <b>(+22.71%)</b></td><td>0.09 (+19.10%)</td><td>0.09 (-2.62%)</td><td>0.08 <b>(+58.24%)</b></td><td>0.02 <b>(-31.83%)</b></td><td>307.80 <b>(-36.81%)</b></td><td>274.60 <b>(-20.95%)</b></td><td>280.20 (+2.67%)</td><td>209.50 (-18.51%)</td><td>39.58 <b>(-65.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>487.10 (n/a)</td><td>347.36 (n/a)</td><td>272.90 (n/a)</td><td>257.10 (n/a)</td><td>113.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.14 (-10.05%)</td><td>0.11 (-16.31%)</td><td>0.12 (-17.63%)</td><td>0.08 (-19.00%)</td><td>0.02 (+5.27%)</td><td>516.10 <b>(+23.44%)</b></td><td>383.68 <b>(+20.85%)</b></td><td>355.80 <b>(+21.43%)</b></td><td>300.90 (+11.20%)</td><td>83.79 <b>(+42.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>418.10 (n/a)</td><td>317.48 (n/a)</td><td>293.00 (n/a)</td><td>270.60 (n/a)</td><td>58.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (+8.59%)</td><td>0.02 (+5.60%)</td><td>0.01 <b>(-21.60%)</b></td><td>0.01 <b>(+25.47%)</b></td><td>0.01 (-10.14%)</td><td>508.70 <b>(-20.30%)</b></td><td>362.08 (-11.81%)</td><td>352.00 <b>(+27.54%)</b></td><td>232.30 (-7.93%)</td><td>124.73 <b>(-36.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.30 (n/a)</td><td>410.56 (n/a)</td><td>276.00 (n/a)</td><td>252.30 (n/a)</td><td>196.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-17.31%)</td><td>0.03 (-2.85%)</td><td>0.03 (+3.31%)</td><td>0.01 (+3.26%)</td><td>0.01 (-19.99%)</td><td>552.70 (-3.17%)</td><td>318.38 (+0.03%)</td><td>262.50 (-3.17%)</td><td>247.00 <b>(+20.96%)</b></td><td>131.23 (-9.60%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.80 (n/a)</td><td>318.28 (n/a)</td><td>271.10 (n/a)</td><td>204.20 (n/a)</td><td>145.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.06 (+0.94%)</td><td>0.04 (+7.35%)</td><td>0.05 (+9.09%)</td><td>0.02 <b>(-21.86%)</b></td><td>0.01 (+15.44%)</td><td>654.80 <b>(+27.99%)</b></td><td>324.18 (-0.10%)</td><td>243.00 (-8.30%)</td><td>218.90 (-0.95%)</td><td>185.54 <b>(+54.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.60 (n/a)</td><td>324.52 (n/a)</td><td>265.00 (n/a)</td><td>221.00 (n/a)</td><td>119.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+8.76%)</td><td>0.02 (-14.97%)</td><td>0.02 <b>(-34.42%)</b></td><td>0.00 <b>(-75.54%)</b></td><td>0.01 <b>(+73.70%)</b></td><td>1990.90 <b>(+308.81%)</b></td><td>693.44 <b>(+92.04%)</b></td><td>472.90 <b>(+52.50%)</b></td><td>227.90 (-8.07%)</td><td>735.66 <b>(+548.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.00 (n/a)</td><td>361.10 (n/a)</td><td>310.10 (n/a)</td><td>247.90 (n/a)</td><td>113.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 <b>(+21.99%)</b></td><td>0.02 (-4.26%)</td><td>0.02 (+9.99%)</td><td>0.00 <b>(-76.24%)</b></td><td>0.02 <b>(+94.19%)</b></td><td>2420.00 <b>(+320.87%)</b></td><td>946.32 <b>(+92.05%)</b></td><td>495.30 (-9.09%)</td><td>220.30 (-18.04%)</td><td>912.21 <b>(+618.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.00 (n/a)</td><td>492.74 (n/a)</td><td>544.80 (n/a)</td><td>268.80 (n/a)</td><td>126.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+3.26%)</td><td>0.03 (+7.71%)</td><td>0.03 <b>(+26.62%)</b></td><td>0.02 (+5.69%)</td><td>0.01 (-6.13%)</td><td>460.80 (-5.40%)</td><td>331.98 (-8.48%)</td><td>296.30 <b>(-21.03%)</b></td><td>232.20 (-3.17%)</td><td>103.37 (-11.07%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>362.76 (n/a)</td><td>375.20 (n/a)</td><td>239.80 (n/a)</td><td>116.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (-11.04%)</td><td>0.03 <b>(+26.95%)</b></td><td>0.04 <b>(+89.64%)</b></td><td>0.02 (+11.97%)</td><td>0.01 <b>(-22.93%)</b></td><td>523.80 (-10.69%)</td><td>341.30 <b>(-26.63%)</b></td><td>281.20 <b>(-47.26%)</b></td><td>194.00 (+12.46%)</td><td>144.41 (-15.97%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>586.50 (n/a)</td><td>465.18 (n/a)</td><td>533.20 (n/a)</td><td>172.50 (n/a)</td><td>171.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+5.32%)</td><td>0.03 (-2.93%)</td><td>0.02 (-9.65%)</td><td>0.01 (-19.92%)</td><td>0.01 (+9.42%)</td><td>679.40 <b>(+24.87%)</b></td><td>393.04 (+7.34%)</td><td>336.50 (+10.65%)</td><td>207.20 (-5.04%)</td><td>195.08 <b>(+23.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>366.16 (n/a)</td><td>304.10 (n/a)</td><td>218.20 (n/a)</td><td>158.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-9.57%)</td><td>0.02 (+1.45%)</td><td>0.02 (-12.98%)</td><td>0.02 <b>(+248.19%)</b></td><td>0.01 <b>(-40.40%)</b></td><td>570.60 <b>(-71.28%)</b></td><td>472.02 <b>(-35.71%)</b></td><td>500.80 (+14.89%)</td><td>271.40 (+10.59%)</td><td>117.40 <b>(-83.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1986.70 (n/a)</td><td>734.26 (n/a)</td><td>435.90 (n/a)</td><td>245.40 (n/a)</td><td>715.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (+9.92%)</td><td>0.03 (+15.89%)</td><td>0.02 <b>(-36.73%)</b></td><td>0.02 <b>(+278.50%)</b></td><td>0.01 <b>(-25.81%)</b></td><td>499.80 <b>(-73.58%)</b></td><td>366.14 <b>(-49.49%)</b></td><td>419.40 <b>(+58.03%)</b></td><td>211.30 (-9.00%)</td><td>135.92 <b>(-81.20%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1891.70 (n/a)</td><td>724.90 (n/a)</td><td>265.40 (n/a)</td><td>232.20 (n/a)</td><td>723.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-8.53%)</td><td>0.03 <b>(+22.54%)</b></td><td>0.03 <b>(+67.10%)</b></td><td>0.02 <b>(+23.98%)</b></td><td>0.01 <b>(-44.55%)</b></td><td>452.60 (-19.34%)</td><td>316.70 <b>(-25.25%)</b></td><td>286.80 <b>(-40.16%)</b></td><td>272.10 (+9.32%)</td><td>76.35 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>423.70 (n/a)</td><td>479.30 (n/a)</td><td>248.90 (n/a)</td><td>152.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (-0.13%)</td><td>0.02 <b>(+29.86%)</b></td><td>0.03 <b>(+70.88%)</b></td><td>0.02 <b>(+240.86%)</b></td><td>0.01 <b>(-40.78%)</b></td><td>503.80 <b>(-70.66%)</b></td><td>377.34 <b>(-45.67%)</b></td><td>314.50 <b>(-41.47%)</b></td><td>292.10 (+0.14%)</td><td>106.58 <b>(-81.96%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1717.30 (n/a)</td><td>694.54 (n/a)</td><td>537.30 (n/a)</td><td>291.70 (n/a)</td><td>590.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.42 (+3.14%)</td><td>0.26 <b>(-22.32%)</b></td><td>0.19 <b>(-44.98%)</b></td><td>0.15 (-10.53%)</td><td>0.12 <b>(+23.71%)</b></td><td>635.10 (+11.77%)</td><td>443.22 <b>(+35.66%)</b></td><td>519.50 <b>(+81.77%)</b></td><td>234.40 (-3.06%)</td><td>174.19 <b>(+27.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>568.20 (n/a)</td><td>326.72 (n/a)</td><td>285.80 (n/a)</td><td>241.80 (n/a)</td><td>137.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.62 <b>(+46.24%)</b></td><td>0.27 (-6.77%)</td><td>0.19 <b>(-23.57%)</b></td><td>0.18 (-0.09%)</td><td>0.19 <b>(+70.67%)</b></td><td>549.10 (+0.09%)</td><td>455.86 <b>(+20.15%)</b></td><td>526.30 <b>(+30.86%)</b></td><td>159.10 <b>(-31.60%)</b></td><td>166.29 (+19.55%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>548.60 (n/a)</td><td>379.40 (n/a)</td><td>402.20 (n/a)</td><td>232.60 (n/a)</td><td>139.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.36 (-10.72%)</td><td>0.26 (-2.72%)</td><td>0.35 <b>(+65.46%)</b></td><td>0.04 <b>(-73.26%)</b></td><td>0.15 <b>(+22.99%)</b></td><td>2417.90 <b>(+273.94%)</b></td><td>760.90 <b>(+75.72%)</b></td><td>280.40 <b>(-39.57%)</b></td><td>270.10 (+11.98%)</td><td>934.66 <b>(+424.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>646.60 (n/a)</td><td>433.02 (n/a)</td><td>464.00 (n/a)</td><td>241.20 (n/a)</td><td>178.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.29 (+2.11%)</td><td>0.19 (+3.68%)</td><td>0.22 (+12.63%)</td><td>0.03 <b>(-72.56%)</b></td><td>0.10 <b>(+42.92%)</b></td><td>2411.80 <b>(+264.38%)</b></td><td>740.38 <b>(+67.78%)</b></td><td>329.90 (-11.20%)</td><td>251.70 (-2.06%)</td><td>935.78 <b>(+469.12%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>661.90 (n/a)</td><td>441.28 (n/a)</td><td>371.50 (n/a)</td><td>257.00 (n/a)</td><td>164.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.27 (-7.55%)</td><td>0.17 <b>(-37.96%)</b></td><td>0.15 <b>(-43.80%)</b></td><td>0.13 <b>(-47.33%)</b></td><td>0.06 <b>(+210.77%)</b></td><td>557.70 <b>(+89.89%)</b></td><td>468.72 <b>(+71.86%)</b></td><td>494.70 <b>(+77.95%)</b></td><td>272.80 (+8.17%)</td><td>113.30 <b>(+515.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>293.70 (n/a)</td><td>272.74 (n/a)</td><td>278.00 (n/a)</td><td>252.20 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.35 (+17.53%)</td><td>0.19 <b>(-27.75%)</b></td><td>0.14 <b>(-48.24%)</b></td><td>0.07 <b>(-63.51%)</b></td><td>0.11 <b>(+196.09%)</b></td><td>1013.10 <b>(+174.03%)</b></td><td>515.04 <b>(+79.34%)</b></td><td>523.40 <b>(+93.21%)</b></td><td>213.40 (-14.91%)</td><td>310.14 <b>(+558.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>369.70 (n/a)</td><td>287.18 (n/a)</td><td>270.90 (n/a)</td><td>250.80 (n/a)</td><td>47.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.47 (-14.34%)</td><td>0.32 (-0.50%)</td><td>0.27 (+9.80%)</td><td>0.22 (+9.27%)</td><td>0.11 <b>(-27.26%)</b></td><td>589.10 (-8.48%)</td><td>446.42 (-5.37%)</td><td>489.80 (-8.93%)</td><td>276.60 (+16.76%)</td><td>134.10 <b>(-23.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.55 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>643.70 (n/a)</td><td>471.76 (n/a)</td><td>537.80 (n/a)</td><td>236.90 (n/a)</td><td>175.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.41 <b>(-24.18%)</b></td><td>0.25 (-13.29%)</td><td>0.23 (+19.88%)</td><td>0.17 <b>(+26.93%)</b></td><td>0.09 <b>(-45.80%)</b></td><td>759.60 <b>(-21.22%)</b></td><td>565.80 (-2.70%)</td><td>567.90 (-16.57%)</td><td>318.40 <b>(+31.90%)</b></td><td>160.17 <b>(-45.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.54 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>964.20 (n/a)</td><td>581.52 (n/a)</td><td>680.70 (n/a)</td><td>241.40 (n/a)</td><td>292.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.48 <b>(+20.02%)</b></td><td>0.28 (-8.32%)</td><td>0.21 <b>(-23.11%)</b></td><td>0.16 <b>(-30.09%)</b></td><td>0.14 <b>(+74.94%)</b></td><td>797.80 <b>(+43.05%)</b></td><td>553.82 <b>(+23.27%)</b></td><td>612.20 <b>(+30.06%)</b></td><td>272.00 (-16.67%)</td><td>230.67 <b>(+110.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>557.70 (n/a)</td><td>449.26 (n/a)</td><td>470.70 (n/a)</td><td>326.40 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (+0.30%)</td><td>0.01 (-7.71%)</td><td>0.01 (-3.82%)</td><td>0.01 <b>(-21.02%)</b></td><td>0.00 <b>(+103.58%)</b></td><td>459.00 <b>(+26.62%)</b></td><td>342.82 (+12.66%)</td><td>309.20 (+3.97%)</td><td>266.70 (-0.30%)</td><td>87.03 <b>(+147.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>362.50 (n/a)</td><td>304.30 (n/a)</td><td>297.40 (n/a)</td><td>267.50 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.01 <b>(-22.78%)</b></td><td>0.01 <b>(-20.88%)</b></td><td>0.01 (-12.83%)</td><td>0.00 <b>(-72.48%)</b></td><td>0.00 <b>(+32.72%)</b></td><td>1911.90 <b>(+263.41%)</b></td><td>629.56 <b>(+97.70%)</b></td><td>310.30 (+14.71%)</td><td>296.00 <b>(+29.54%)</b></td><td>716.92 <b>(+504.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.10 (n/a)</td><td>318.44 (n/a)</td><td>270.50 (n/a)</td><td>228.50 (n/a)</td><td>118.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 <b>(+44.26%)</b></td><td>0.01 <b>(+94.43%)</b></td><td>0.01 <b>(+200.89%)</b></td><td>0.01 <b>(+249.52%)</b></td><td>0.00 (-9.24%)</td><td>570.00 <b>(-71.39%)</b></td><td>357.30 <b>(-62.70%)</b></td><td>280.40 <b>(-66.76%)</b></td><td>248.60 <b>(-30.69%)</b></td><td>135.49 <b>(-80.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1992.30 (n/a)</td><td>957.98 (n/a)</td><td>843.60 (n/a)</td><td>358.70 (n/a)</td><td>678.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.57 (+7.56%)</td><td>0.43 (+5.67%)</td><td>0.45 (-0.83%)</td><td>0.27 (-1.51%)</td><td>0.12 (+10.34%)</td><td>490.90 (+1.53%)</td><td>325.46 (-4.56%)</td><td>291.70 (+0.83%)</td><td>231.80 (-7.02%)</td><td>101.81 (+5.34%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>483.50 (n/a)</td><td>341.00 (n/a)</td><td>289.30 (n/a)</td><td>249.30 (n/a)</td><td>96.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.53 (-4.56%)</td><td>0.44 (+1.51%)</td><td>0.47 (+11.79%)</td><td>0.31 (-0.43%)</td><td>0.09 <b>(-21.65%)</b></td><td>428.80 (+0.42%)</td><td>308.46 (-3.18%)</td><td>283.60 (-10.54%)</td><td>248.50 (+4.81%)</td><td>72.97 (-12.82%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>427.00 (n/a)</td><td>318.58 (n/a)</td><td>317.00 (n/a)</td><td>237.10 (n/a)</td><td>83.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.68 <b>(+36.51%)</b></td><td>0.35 (-3.60%)</td><td>0.28 (-14.24%)</td><td>0.07 <b>(-70.85%)</b></td><td>0.24 <b>(+124.05%)</b></td><td>1762.30 <b>(+243.06%)</b></td><td>655.82 <b>(+68.70%)</b></td><td>472.40 (+16.61%)</td><td>193.10 <b>(-26.77%)</b></td><td>637.10 <b>(+495.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>513.70 (n/a)</td><td>388.76 (n/a)</td><td>405.10 (n/a)</td><td>263.70 (n/a)</td><td>106.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.44 (-19.67%)</td><td>0.34 <b>(-22.56%)</b></td><td>0.29 <b>(-38.13%)</b></td><td>0.27 (+5.18%)</td><td>0.08 <b>(-24.54%)</b></td><td>491.30 (-4.93%)</td><td>404.16 <b>(+25.84%)</b></td><td>452.10 <b>(+61.64%)</b></td><td>297.40 <b>(+24.49%)</b></td><td>91.88 (-17.56%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>516.80 (n/a)</td><td>321.16 (n/a)</td><td>279.70 (n/a)</td><td>238.90 (n/a)</td><td>111.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.71 (+6.88%)</td><td>0.50 (+19.52%)</td><td>0.51 <b>(+53.43%)</b></td><td>0.25 (-0.93%)</td><td>0.17 (-2.35%)</td><td>522.00 (+0.95%)</td><td>294.74 (-16.47%)</td><td>258.60 <b>(-34.81%)</b></td><td>185.00 (-6.42%)</td><td>131.03 (+2.68%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.67 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>517.10 (n/a)</td><td>352.84 (n/a)</td><td>396.70 (n/a)</td><td>197.70 (n/a)</td><td>127.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 <b>(+21.59%)</b></td><td>0.01 <b>(+50.86%)</b></td><td>0.01 <b>(+60.17%)</b></td><td>0.01 <b>(+43.98%)</b></td><td>0.00 (-5.29%)</td><td>408.10 <b>(-30.54%)</b></td><td>301.72 <b>(-35.28%)</b></td><td>293.70 <b>(-37.56%)</b></td><td>244.90 (-17.76%)</td><td>63.20 <b>(-42.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.50 (n/a)</td><td>466.18 (n/a)</td><td>470.40 (n/a)</td><td>297.80 (n/a)</td><td>109.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (-9.53%)</td><td>0.01 (-13.73%)</td><td>0.01 <b>(-29.00%)</b></td><td>0.01 (+10.15%)</td><td>0.00 (-14.30%)</td><td>467.30 (-9.21%)</td><td>352.12 (+12.94%)</td><td>389.40 <b>(+40.88%)</b></td><td>239.70 (+10.56%)</td><td>95.35 (-19.75%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.70 (n/a)</td><td>311.78 (n/a)</td><td>276.40 (n/a)</td><td>216.80 (n/a)</td><td>118.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.00 <b>(-71.43%)</b></td><td>0.00 <b>(-41.18%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-100.00%)</b></td><td>22680.85 (+12.63%)</td><td>18589.20 <b>(+31.39%)</b></td><td>17947.82 <b>(+28.31%)</b></td><td>16744.67 <b>(+198.47%)</b></td><td>2366.65 <b>(-56.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20137.04 (n/a)</td><td>14147.93 (n/a)</td><td>13987.56 (n/a)</td><td>5610.25 (n/a)</td><td>5410.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.00 (-15.38%)</td><td>0.00 <b>(-24.49%)</b></td><td>0.00 <b>(-40.00%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+13.97%)</td><td>19375.92 <b>(+22.04%)</b></td><td>12972.22 <b>(+42.06%)</b></td><td>12898.60 <b>(+64.51%)</b></td><td>7423.59 (+18.53%)</td><td>5542.64 <b>(+44.46%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>15876.32 (n/a)</td><td>9131.71 (n/a)</td><td>7840.45 (n/a)</td><td>6263.10 (n/a)</td><td>3836.85 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.13 (+6.56%)</td><td>0.09 (-6.22%)</td><td>0.08 (-3.13%)</td><td>0.07 (-1.26%)</td><td>0.03 (+1.31%)</td><td>29845.02 (+1.28%)</td><td>24742.09 (+6.25%)</td><td>26042.96 (+3.24%)</td><td>15555.27 (-6.17%)</td><td>5408.98 (-7.30%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29467.27 (n/a)</td><td>23285.89 (n/a)</td><td>25225.82 (n/a)</td><td>16577.63 (n/a)</td><td>5834.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.14 (+0.72%)</td><td>0.11 <b>(+21.46%)</b></td><td>0.13 <b>(+66.33%)</b></td><td>0.07 (-4.51%)</td><td>0.04 <b>(+35.09%)</b></td><td>30028.66 (+4.74%)</td><td>21145.71 (-13.36%)</td><td>15717.66 <b>(-39.91%)</b></td><td>15051.64 (-0.75%)</td><td>7960.37 <b>(+47.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28670.00 (n/a)</td><td>24407.66 (n/a)</td><td>26158.32 (n/a)</td><td>15164.87 (n/a)</td><td>5399.22 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.09 <b>(-41.54%)</b></td><td>0.08 <b>(-26.45%)</b></td><td>0.08 (-5.72%)</td><td>0.07 (+0.28%)</td><td>0.01 <b>(-78.49%)</b></td><td>29471.13 (-0.19%)</td><td>26636.50 <b>(+22.62%)</b></td><td>26497.60 (+5.97%)</td><td>22637.65 <b>(+70.99%)</b></td><td>2927.42 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>29528.24 (n/a)</td><td>21722.14 (n/a)</td><td>25004.94 (n/a)</td><td>13239.53 (n/a)</td><td>7537.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_weight_layout_reaches_both_gemms[b_col_maj_False]

_No metrics available._


### test_weight_layout_reaches_both_gemms[b_col_maj_True]

_No metrics available._


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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.82 <b>(+20.27%)</b></td><td>1.25 (+15.84%)</td><td>1.46 <b>(+47.93%)</b></td><td>0.21 <b>(-68.18%)</b></td><td>0.68 <b>(+82.09%)</b></td><td>2486.80 <b>(+214.27%)</b></td><td>795.48 <b>(+48.05%)</b></td><td>359.40 <b>(-32.41%)</b></td><td>287.50 (-16.86%)</td><td>951.59 <b>(+407.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.52 (n/a)</td><td>1.08 (n/a)</td><td>0.99 (n/a)</td><td>0.66 (n/a)</td><td>0.37 (n/a)</td><td>791.30 (n/a)</td><td>537.30 (n/a)</td><td>531.70 (n/a)</td><td>345.80 (n/a)</td><td>187.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.03 (+16.71%)</td><td>2.11 (+1.28%)</td><td>2.29 (+2.11%)</td><td>1.38 <b>(+26.57%)</b></td><td>0.70 (+18.10%)</td><td>758.20 <b>(-20.99%)</b></td><td>543.66 (-1.76%)</td><td>458.00 (-2.07%)</td><td>346.40 (-14.32%)</td><td>184.78 (-19.71%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.59 (n/a)</td><td>2.09 (n/a)</td><td>2.24 (n/a)</td><td>1.09 (n/a)</td><td>0.59 (n/a)</td><td>959.60 (n/a)</td><td>553.40 (n/a)</td><td>467.70 (n/a)</td><td>404.30 (n/a)</td><td>230.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.66 (-16.37%)</td><td>1.46 (+7.55%)</td><td>1.54 <b>(+36.26%)</b></td><td>0.96 (+16.80%)</td><td>0.28 <b>(-46.02%)</b></td><td>544.00 (-14.37%)</td><td>374.80 (-13.78%)</td><td>340.30 <b>(-26.61%)</b></td><td>315.90 (+19.57%)</td><td>95.13 <b>(-39.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.98 (n/a)</td><td>1.35 (n/a)</td><td>1.13 (n/a)</td><td>0.83 (n/a)</td><td>0.52 (n/a)</td><td>635.30 (n/a)</td><td>434.70 (n/a)</td><td>463.70 (n/a)</td><td>264.20 (n/a)</td><td>157.78 (n/a)</td>
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
