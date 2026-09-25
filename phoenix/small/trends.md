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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (-2.68%)</td><td>0.04 (+5.40%)</td><td>0.04 <b>(+34.97%)</b></td><td>0.02 (+2.67%)</td><td>0.01 <b>(-30.76%)</b></td><td>522.60 (-2.61%)</td><td>351.28 (-10.42%)</td><td>341.90 <b>(-25.92%)</b></td><td>246.40 (+2.80%)</td><td>105.06 <b>(-24.77%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.60 (n/a)</td><td>392.12 (n/a)</td><td>461.50 (n/a)</td><td>239.70 (n/a)</td><td>139.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (+2.16%)</td><td>0.03 <b>(-29.98%)</b></td><td>0.03 <b>(-41.76%)</b></td><td>0.01 <b>(-78.30%)</b></td><td>0.02 <b>(+39.78%)</b></td><td>2395.20 <b>(+360.88%)</b></td><td>797.92 <b>(+135.62%)</b></td><td>465.00 <b>(+71.71%)</b></td><td>236.50 (-2.11%)</td><td>897.94 <b>(+648.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.70 (n/a)</td><td>338.64 (n/a)</td><td>270.80 (n/a)</td><td>241.60 (n/a)</td><td>120.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (+2.18%)</td><td>0.03 (-4.93%)</td><td>0.03 (-4.97%)</td><td>0.02 (+18.85%)</td><td>0.01 <b>(-24.56%)</b></td><td>548.50 (-15.86%)</td><td>405.36 (-2.70%)</td><td>411.00 (+5.22%)</td><td>241.00 (-2.15%)</td><td>114.70 <b>(-36.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>651.90 (n/a)</td><td>416.60 (n/a)</td><td>390.60 (n/a)</td><td>246.30 (n/a)</td><td>180.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (-15.43%)</td><td>0.01 (-13.33%)</td><td>0.01 (-9.78%)</td><td>0.01 (+2.54%)</td><td>0.00 <b>(-43.67%)</b></td><td>521.70 (-2.47%)</td><td>392.60 (+6.86%)</td><td>377.60 (+10.86%)</td><td>273.20 (+18.22%)</td><td>95.33 <b>(-33.44%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.90 (n/a)</td><td>367.40 (n/a)</td><td>340.60 (n/a)</td><td>231.10 (n/a)</td><td>143.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (-11.14%)</td><td>0.02 (-9.61%)</td><td>0.02 (+5.07%)</td><td>0.01 <b>(-44.30%)</b></td><td>0.01 <b>(+24.15%)</b></td><td>760.80 <b>(+79.52%)</b></td><td>371.66 <b>(+27.30%)</b></td><td>240.50 (-4.83%)</td><td>218.60 (+12.51%)</td><td>230.10 <b>(+142.17%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>423.80 (n/a)</td><td>291.96 (n/a)</td><td>252.70 (n/a)</td><td>194.30 (n/a)</td><td>95.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+6.59%)</td><td>0.02 (+12.33%)</td><td>0.02 (+17.35%)</td><td>0.01 (-18.95%)</td><td>0.01 <b>(+29.65%)</b></td><td>651.70 <b>(+23.36%)</b></td><td>312.80 (-2.66%)</td><td>238.40 (-14.77%)</td><td>201.90 (-6.22%)</td><td>190.14 <b>(+55.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>528.30 (n/a)</td><td>321.36 (n/a)</td><td>279.70 (n/a)</td><td>215.30 (n/a)</td><td>122.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+15.99%)</td><td>0.02 (+13.82%)</td><td>0.02 <b>(+23.47%)</b></td><td>0.01 <b>(+32.22%)</b></td><td>0.01 (+3.41%)</td><td>538.20 <b>(-24.37%)</b></td><td>370.16 (-15.69%)</td><td>309.40 (-19.01%)</td><td>208.40 (-13.78%)</td><td>140.80 <b>(-29.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>711.60 (n/a)</td><td>439.04 (n/a)</td><td>382.00 (n/a)</td><td>241.70 (n/a)</td><td>198.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 <b>(-41.03%)</b></td><td>0.01 (-12.77%)</td><td>0.02 (+16.79%)</td><td>0.01 <b>(-32.76%)</b></td><td>0.01 <b>(-48.19%)</b></td><td>864.50 <b>(+48.72%)</b></td><td>430.70 (+8.00%)</td><td>329.70 (-14.39%)</td><td>263.70 <b>(+69.58%)</b></td><td>247.15 <b>(+34.65%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>398.80 (n/a)</td><td>385.10 (n/a)</td><td>155.50 (n/a)</td><td>183.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (-1.48%)</td><td>0.01 (-15.17%)</td><td>0.01 (-17.23%)</td><td>0.01 <b>(-27.80%)</b></td><td>0.00 <b>(+46.59%)</b></td><td>659.40 <b>(+38.50%)</b></td><td>494.72 <b>(+26.37%)</b></td><td>520.10 <b>(+20.81%)</b></td><td>297.30 (+1.50%)</td><td>167.47 <b>(+113.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.10 (n/a)</td><td>391.48 (n/a)</td><td>430.50 (n/a)</td><td>292.90 (n/a)</td><td>78.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>658.60 (n/a)</td><td>325.44 (n/a)</td><td>253.10 (n/a)</td><td>193.80 (n/a)</td><td>189.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.60 (n/a)</td><td>337.80 (n/a)</td><td>296.70 (n/a)</td><td>257.00 (n/a)</td><td>116.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.80 (n/a)</td><td>383.30 (n/a)</td><td>295.90 (n/a)</td><td>279.30 (n/a)</td><td>143.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>306.50 (n/a)</td><td>263.74 (n/a)</td><td>298.00 (n/a)</td><td>186.30 (n/a)</td><td>53.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>333.16 (n/a)</td><td>286.20 (n/a)</td><td>239.80 (n/a)</td><td>103.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>676.00 (n/a)</td><td>466.12 (n/a)</td><td>564.20 (n/a)</td><td>214.20 (n/a)</td><td>208.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.94 (-4.40%)</td><td>0.71 (-2.94%)</td><td>0.63 (-9.31%)</td><td>0.51 (-18.15%)</td><td>0.18 <b>(+23.55%)</b></td><td>899.10 <b>(+22.19%)</b></td><td>681.58 (+5.53%)</td><td>728.20 (+10.27%)</td><td>489.50 (+4.59%)</td><td>166.43 <b>(+59.07%)</b></td><td>68.55 (-4.40%)</td><td>51.74 (-2.94%)</td><td>46.08 (-9.31%)</td><td>37.32 (-18.15%)</td><td>13.01 <b>(+23.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.98 (n/a)</td><td>0.73 (n/a)</td><td>0.69 (n/a)</td><td>0.62 (n/a)</td><td>0.14 (n/a)</td><td>735.80 (n/a)</td><td>645.88 (n/a)</td><td>660.40 (n/a)</td><td>468.00 (n/a)</td><td>104.63 (n/a)</td><td>71.70 (n/a)</td><td>53.31 (n/a)</td><td>50.81 (n/a)</td><td>45.60 (n/a)</td><td>10.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.33 (-4.94%)</td><td>0.98 (+0.74%)</td><td>0.88 <b>(-23.34%)</b></td><td>0.87 <b>(+220.31%)</b></td><td>0.20 <b>(-55.91%)</b></td><td>755.80 <b>(-68.78%)</b></td><td>684.88 <b>(-28.46%)</b></td><td>742.90 <b>(+30.45%)</b></td><td>494.10 (+5.19%)</td><td>111.25 <b>(-86.55%)</b></td><td>135.82 (-4.94%)</td><td>100.59 (+0.74%)</td><td>90.33 <b>(-23.34%)</b></td><td>88.80 <b>(+220.31%)</b></td><td>20.12 <b>(-55.91%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.40 (n/a)</td><td>0.98 (n/a)</td><td>1.15 (n/a)</td><td>0.27 (n/a)</td><td>0.45 (n/a)</td><td>2420.70 (n/a)</td><td>957.30 (n/a)</td><td>569.50 (n/a)</td><td>469.70 (n/a)</td><td>827.34 (n/a)</td><td>142.88 (n/a)</td><td>99.85 (n/a)</td><td>117.83 (n/a)</td><td>27.72 (n/a)</td><td>45.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.44 (-3.55%)</td><td>1.19 (-4.39%)</td><td>1.23 (-4.62%)</td><td>0.90 (-5.79%)</td><td>0.20 (+3.33%)</td><td>837.50 (+6.15%)</td><td>649.30 (+4.98%)</td><td>611.00 (+4.86%)</td><td>524.40 (+3.70%)</td><td>120.63 (+13.10%)</td><td>159.98 (-3.55%)</td><td>132.53 (-4.39%)</td><td>137.30 (-4.62%)</td><td>100.16 (-5.79%)</td><td>22.69 (+3.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.49 (n/a)</td><td>1.25 (n/a)</td><td>1.29 (n/a)</td><td>0.96 (n/a)</td><td>0.20 (n/a)</td><td>789.00 (n/a)</td><td>618.50 (n/a)</td><td>582.70 (n/a)</td><td>505.70 (n/a)</td><td>106.65 (n/a)</td><td>165.87 (n/a)</td><td>138.62 (n/a)</td><td>143.96 (n/a)</td><td>106.32 (n/a)</td><td>21.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.77 <b>(+25.29%)</b></td><td>1.22 <b>(+36.20%)</b></td><td>1.18 (+1.12%)</td><td>0.88 <b>(+216.40%)</b></td><td>0.36 <b>(-27.46%)</b></td><td>1198.30 <b>(-68.39%)</b></td><td>915.32 <b>(-46.93%)</b></td><td>888.70 (-1.11%)</td><td>593.20 <b>(-20.18%)</b></td><td>250.43 <b>(-81.00%)</b></td><td>226.25 <b>(+25.29%)</b></td><td>156.57 <b>(+36.20%)</b></td><td>151.03 (+1.12%)</td><td>112.01 <b>(+216.40%)</b></td><td>46.37 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.41 (n/a)</td><td>0.90 (n/a)</td><td>1.17 (n/a)</td><td>0.28 (n/a)</td><td>0.50 (n/a)</td><td>3791.30 (n/a)</td><td>1724.80 (n/a)</td><td>898.70 (n/a)</td><td>743.20 (n/a)</td><td>1318.26 (n/a)</td><td>180.59 (n/a)</td><td>114.96 (n/a)</td><td>149.35 (n/a)</td><td>35.40 (n/a)</td><td>63.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.09 (+10.26%)</td><td>1.69 (+7.01%)</td><td>1.94 <b>(+25.47%)</b></td><td>1.00 <b>(-22.41%)</b></td><td>0.46 <b>(+108.62%)</b></td><td>1046.40 <b>(+28.88%)</b></td><td>670.02 (-0.76%)</td><td>540.20 <b>(-20.30%)</b></td><td>501.60 (-9.29%)</td><td>228.50 <b>(+143.78%)</b></td><td>267.58 (+10.26%)</td><td>216.02 (+7.01%)</td><td>248.46 <b>(+25.47%)</b></td><td>128.27 <b>(-22.41%)</b></td><td>58.47 <b>(+108.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.90 (n/a)</td><td>1.58 (n/a)</td><td>1.55 (n/a)</td><td>1.29 (n/a)</td><td>0.22 (n/a)</td><td>811.90 (n/a)</td><td>675.16 (n/a)</td><td>677.80 (n/a)</td><td>553.00 (n/a)</td><td>93.73 (n/a)</td><td>242.69 (n/a)</td><td>201.87 (n/a)</td><td>198.02 (n/a)</td><td>165.32 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.05 (-5.76%)</td><td>1.59 (-16.89%)</td><td>1.49 (-16.21%)</td><td>1.25 <b>(-29.13%)</b></td><td>0.35 <b>(+74.74%)</b></td><td>836.20 <b>(+41.11%)</b></td><td>683.14 <b>(+23.82%)</b></td><td>704.90 (+19.35%)</td><td>511.60 (+6.12%)</td><td>142.63 <b>(+158.98%)</b></td><td>262.37 (-5.76%)</td><td>203.88 (-16.89%)</td><td>190.40 (-16.21%)</td><td>160.50 <b>(-29.13%)</b></td><td>44.66 <b>(+74.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.18 (n/a)</td><td>1.92 (n/a)</td><td>1.78 (n/a)</td><td>1.77 (n/a)</td><td>0.20 (n/a)</td><td>592.60 (n/a)</td><td>551.70 (n/a)</td><td>590.60 (n/a)</td><td>482.10 (n/a)</td><td>55.07 (n/a)</td><td>278.41 (n/a)</td><td>245.31 (n/a)</td><td>227.24 (n/a)</td><td>226.47 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.53 (+3.91%)</td><td>1.21 (+5.68%)</td><td>1.21 (+1.40%)</td><td>1.00 <b>(+97.98%)</b></td><td>0.21 <b>(-46.81%)</b></td><td>1050.30 <b>(-49.49%)</b></td><td>888.20 (-17.01%)</td><td>864.60 (-1.38%)</td><td>683.50 (-3.76%)</td><td>140.99 <b>(-75.39%)</b></td><td>196.37 (+3.91%)</td><td>154.45 (+5.68%)</td><td>155.24 (+1.40%)</td><td>127.80 <b>(+97.98%)</b></td><td>26.52 <b>(-46.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.48 (n/a)</td><td>1.14 (n/a)</td><td>1.20 (n/a)</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>2079.30 (n/a)</td><td>1070.26 (n/a)</td><td>876.70 (n/a)</td><td>710.20 (n/a)</td><td>572.98 (n/a)</td><td>188.98 (n/a)</td><td>146.15 (n/a)</td><td>153.10 (n/a)</td><td>64.55 (n/a)</td><td>49.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.88 <b>(+20.01%)</b></td><td>0.60 (+2.66%)</td><td>0.54 (-9.60%)</td><td>0.40 (+5.92%)</td><td>0.18 <b>(+27.37%)</b></td><td>909.80 (-5.58%)</td><td>642.94 (-1.37%)</td><td>664.00 (+10.61%)</td><td>410.90 (-16.69%)</td><td>185.59 (-2.02%)</td><td>40.83 <b>(+20.01%)</b></td><td>27.98 (+2.66%)</td><td>25.27 (-9.60%)</td><td>18.44 (+5.92%)</td><td>8.44 <b>(+27.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.73 (n/a)</td><td>0.59 (n/a)</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td><td>963.60 (n/a)</td><td>651.86 (n/a)</td><td>600.30 (n/a)</td><td>493.20 (n/a)</td><td>189.42 (n/a)</td><td>34.02 (n/a)</td><td>27.25 (n/a)</td><td>27.95 (n/a)</td><td>17.41 (n/a)</td><td>6.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.72 (-6.45%)</td><td>1.94 (-12.14%)</td><td>2.18 (-12.45%)</td><td>1.11 (-4.64%)</td><td>0.67 (-2.25%)</td><td>2369.10 (+4.87%)</td><td>1516.18 (+14.52%)</td><td>1201.30 (+14.22%)</td><td>963.80 (+6.89%)</td><td>595.33 (+7.87%)</td><td>557.05 (-6.45%)</td><td>396.34 (-12.14%)</td><td>446.92 (-12.45%)</td><td>226.62 (-4.64%)</td><td>137.32 (-2.25%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.91 (n/a)</td><td>2.20 (n/a)</td><td>2.49 (n/a)</td><td>1.16 (n/a)</td><td>0.69 (n/a)</td><td>2259.10 (n/a)</td><td>1323.92 (n/a)</td><td>1051.70 (n/a)</td><td>901.70 (n/a)</td><td>551.90 (n/a)</td><td>595.43 (n/a)</td><td>451.08 (n/a)</td><td>510.50 (n/a)</td><td>237.65 (n/a)</td><td>140.48 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.60 (n/a)</td><td>425.70 (n/a)</td><td>468.70 (n/a)</td><td>244.80 (n/a)</td><td>116.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>376.92 (n/a)</td><td>292.20 (n/a)</td><td>278.50 (n/a)</td><td>139.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>432.54 (n/a)</td><td>502.60 (n/a)</td><td>241.40 (n/a)</td><td>162.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>474.10 (n/a)</td><td>392.22 (n/a)</td><td>416.00 (n/a)</td><td>289.00 (n/a)</td><td>72.76 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1086.50 (n/a)</td><td>550.38 (n/a)</td><td>442.90 (n/a)</td><td>240.00 (n/a)</td><td>321.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.30 (n/a)</td><td>459.80 (n/a)</td><td>531.40 (n/a)</td><td>289.70 (n/a)</td><td>142.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.46 (-15.82%)</td><td>0.29 <b>(-37.52%)</b></td><td>0.28 <b>(-45.44%)</b></td><td>0.13 <b>(-63.19%)</b></td><td>0.12 <b>(+33.61%)</b></td><td>1694.80 <b>(+171.65%)</b></td><td>897.04 <b>(+83.23%)</b></td><td>793.80 <b>(+83.28%)</b></td><td>485.80 (+18.81%)</td><td>465.61 <b>(+367.76%)</b></td><td>19.43 (-15.82%)</td><td>12.42 <b>(-37.52%)</b></td><td>11.89 <b>(-45.44%)</b></td><td>5.57 <b>(-63.19%)</b></td><td>4.99 <b>(+33.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>623.90 (n/a)</td><td>489.58 (n/a)</td><td>433.10 (n/a)</td><td>408.90 (n/a)</td><td>99.54 (n/a)</td><td>23.08 (n/a)</td><td>19.88 (n/a)</td><td>21.79 (n/a)</td><td>15.13 (n/a)</td><td>3.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.58 <b>(+23.40%)</b></td><td>0.45 (+6.37%)</td><td>0.40 (-5.20%)</td><td>0.36 (-0.23%)</td><td>0.10 <b>(+132.79%)</b></td><td>616.20 (+0.23%)</td><td>513.32 (-3.01%)</td><td>555.60 (+5.49%)</td><td>378.70 (-18.96%)</td><td>110.29 <b>(+90.41%)</b></td><td>24.92 <b>(+23.40%)</b></td><td>19.14 (+6.37%)</td><td>16.98 (-5.20%)</td><td>15.31 (-0.23%)</td><td>4.44 <b>(+132.79%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.04 (n/a)</td><td>614.80 (n/a)</td><td>529.24 (n/a)</td><td>526.70 (n/a)</td><td>467.30 (n/a)</td><td>57.92 (n/a)</td><td>20.20 (n/a)</td><td>18.00 (n/a)</td><td>17.92 (n/a)</td><td>15.35 (n/a)</td><td>1.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.30 (-2.74%)</td><td>0.30 (-1.59%)</td><td>0.30 (-1.71%)</td><td>0.30 (+0.01%)</td><td>0.00 <b>(-67.59%)</b></td><td>84159.20 (-0.01%)</td><td>83462.70 (+1.60%)</td><td>83295.90 (+1.74%)</td><td>83117.40 (+2.81%)</td><td>406.31 <b>(-66.76%)</b></td><td>206.69 (-2.74%)</td><td>205.84 (-1.59%)</td><td>206.25 (-1.71%)</td><td>204.14 (+0.01%)</td><td>1.00 <b>(-67.59%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84163.80 (n/a)</td><td>82144.92 (n/a)</td><td>81868.40 (n/a)</td><td>80843.80 (n/a)</td><td>1222.20 (n/a)</td><td>212.51 (n/a)</td><td>209.18 (n/a)</td><td>209.85 (n/a)</td><td>204.12 (n/a)</td><td>3.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.15 (-1.48%)</td><td>1.11 (-2.72%)</td><td>1.12 (-2.77%)</td><td>1.04 (-6.09%)</td><td>0.04 <b>(+86.25%)</b></td><td>24133.40 (+6.48%)</td><td>22714.18 (+2.89%)</td><td>22542.50 (+2.85%)</td><td>21862.80 (+1.50%)</td><td>935.29 <b>(+100.50%)</b></td><td>785.80 (-1.48%)</td><td>757.36 (-2.72%)</td><td>762.11 (-2.77%)</td><td>711.87 (-6.09%)</td><td>30.52 <b>(+86.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22664.60 (n/a)</td><td>22075.86 (n/a)</td><td>21917.00 (n/a)</td><td>21539.20 (n/a)</td><td>466.48 (n/a)</td><td>797.61 (n/a)</td><td>778.50 (n/a)</td><td>783.86 (n/a)</td><td>758.00 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>3.81 (-5.97%)</td><td>3.01 (+12.58%)</td><td>3.53 <b>(+69.91%)</b></td><td>1.41 <b>(-22.11%)</b></td><td>1.01 (-0.91%)</td><td>5732.30 <b>(+28.39%)</b></td><td>3077.74 (-8.16%)</td><td>2282.10 <b>(-41.15%)</b></td><td>2115.20 (+6.34%)</td><td>1531.08 <b>(+37.29%)</b></td><td>999.40 (-5.97%)</td><td>789.28 (+12.58%)</td><td>926.32 <b>(+69.91%)</b></td><td>368.77 <b>(-22.11%)</b></td><td>264.03 (-0.91%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>4.05 (n/a)</td><td>2.67 (n/a)</td><td>2.08 (n/a)</td><td>1.81 (n/a)</td><td>1.02 (n/a)</td><td>4464.70 (n/a)</td><td>3351.30 (n/a)</td><td>3877.50 (n/a)</td><td>1989.00 (n/a)</td><td>1115.24 (n/a)</td><td>1062.81 (n/a)</td><td>701.08 (n/a)</td><td>545.18 (n/a)</td><td>473.48 (n/a)</td><td>266.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.33 (+2.88%)</td><td>0.21 (+3.38%)</td><td>0.19 (-2.25%)</td><td>0.17 (+15.61%)</td><td>0.06 (-1.67%)</td><td>7171.70 (-13.50%)</td><td>6160.32 (-4.23%)</td><td>6642.60 (+2.31%)</td><td>3814.50 (-2.80%)</td><td>1343.69 (-16.48%)</td><td>17.59 (+2.88%)</td><td>11.49 (+3.38%)</td><td>10.10 (-2.25%)</td><td>9.36 (+15.61%)</td><td>3.44 (-1.67%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8291.20 (n/a)</td><td>6432.66 (n/a)</td><td>6492.90 (n/a)</td><td>3924.20 (n/a)</td><td>1608.81 (n/a)</td><td>17.10 (n/a)</td><td>11.12 (n/a)</td><td>10.34 (n/a)</td><td>8.09 (n/a)</td><td>3.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>3.82 (n/a)</td><td>3.67 (n/a)</td><td>3.75 (n/a)</td><td>3.43 (n/a)</td><td>0.18 (n/a)</td><td>3.82 (n/a)</td><td>3.67 (n/a)</td><td>3.75 (n/a)</td><td>3.43 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>7.52 (+2.79%)</td><td>6.60 (+5.98%)</td><td>6.52 (+9.55%)</td><td>5.87 (+9.84%)</td><td>0.61 <b>(-27.14%)</b></td><td>7.51 (+2.79%)</td><td>6.60 (+5.98%)</td><td>6.51 (+9.55%)</td><td>5.86 (+9.84%)</td><td>0.61 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>7.31 (n/a)</td><td>6.23 (n/a)</td><td>5.95 (n/a)</td><td>5.34 (n/a)</td><td>0.84 (n/a)</td><td>7.31 (n/a)</td><td>6.23 (n/a)</td><td>5.94 (n/a)</td><td>5.34 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>11.28 (-19.25%)</td><td>8.93 (-6.50%)</td><td>8.51 (+0.40%)</td><td>7.81 (+5.36%)</td><td>1.35 <b>(-47.71%)</b></td><td>11.28 (-19.25%)</td><td>8.93 (-6.50%)</td><td>8.50 (+0.40%)</td><td>7.80 (+5.36%)</td><td>1.35 <b>(-47.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>13.97 (n/a)</td><td>9.56 (n/a)</td><td>8.47 (n/a)</td><td>7.41 (n/a)</td><td>2.58 (n/a)</td><td>13.96 (n/a)</td><td>9.55 (n/a)</td><td>8.47 (n/a)</td><td>7.40 (n/a)</td><td>2.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>3.88 (n/a)</td><td>3.77 (n/a)</td><td>3.83 (n/a)</td><td>3.57 (n/a)</td><td>0.14 (n/a)</td><td>3.88 (n/a)</td><td>3.76 (n/a)</td><td>3.83 (n/a)</td><td>3.56 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>7.32 (+2.74%)</td><td>6.37 (-2.25%)</td><td>6.59 (-0.08%)</td><td>5.34 (-5.43%)</td><td>0.90 <b>(+50.21%)</b></td><td>7.32 (+2.74%)</td><td>6.36 (-2.25%)</td><td>6.59 (-0.08%)</td><td>5.34 (-5.43%)</td><td>0.90 <b>(+50.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>7.13 (n/a)</td><td>6.51 (n/a)</td><td>6.60 (n/a)</td><td>5.65 (n/a)</td><td>0.60 (n/a)</td><td>7.12 (n/a)</td><td>6.51 (n/a)</td><td>6.59 (n/a)</td><td>5.65 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>13.79 (+1.85%)</td><td>10.50 (+7.23%)</td><td>9.19 (+7.80%)</td><td>7.87 (-1.22%)</td><td>2.90 <b>(+22.53%)</b></td><td>13.78 (+1.85%)</td><td>10.49 (+7.23%)</td><td>9.18 (+7.80%)</td><td>7.87 (-1.22%)</td><td>2.89 <b>(+22.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>13.54 (n/a)</td><td>9.79 (n/a)</td><td>8.52 (n/a)</td><td>7.97 (n/a)</td><td>2.36 (n/a)</td><td>13.53 (n/a)</td><td>9.78 (n/a)</td><td>8.52 (n/a)</td><td>7.96 (n/a)</td><td>2.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.97 <b>(+24.91%)</b></td><td>2.01 <b>(+27.81%)</b></td><td>1.70 (+16.45%)</td><td>1.02 (-0.26%)</td><td>0.80 <b>(+33.62%)</b></td><td>2.96 <b>(+24.91%)</b></td><td>2.01 <b>(+27.81%)</b></td><td>1.70 (+16.45%)</td><td>1.02 (-0.26%)</td><td>0.79 <b>(+33.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.38 (n/a)</td><td>1.57 (n/a)</td><td>1.46 (n/a)</td><td>1.02 (n/a)</td><td>0.60 (n/a)</td><td>2.37 (n/a)</td><td>1.57 (n/a)</td><td>1.46 (n/a)</td><td>1.02 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.56 (+7.53%)</td><td>0.44 <b>(+43.51%)</b></td><td>0.53 <b>(+93.07%)</b></td><td>0.08 <b>(-29.20%)</b></td><td>0.21 <b>(+34.95%)</b></td><td>0.55 (+7.53%)</td><td>0.44 <b>(+43.51%)</b></td><td>0.52 <b>(+93.07%)</b></td><td>0.07 <b>(-29.20%)</b></td><td>0.20 <b>(+34.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.52 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>0.15 (n/a)</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.77 <b>(+90.14%)</b></td><td>0.26 (+0.93%)</td><td>0.08 <b>(-75.90%)</b></td><td>0.08 (-2.86%)</td><td>0.30 <b>(+88.22%)</b></td><td>0.76 <b>(+90.14%)</b></td><td>0.25 (+0.93%)</td><td>0.08 <b>(-75.90%)</b></td><td>0.08 (-2.86%)</td><td>0.29 <b>(+88.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.56 (+2.89%)</td><td>1.17 (-11.17%)</td><td>0.79 (-5.11%)</td><td>0.42 (-2.66%)</td><td>0.91 (-10.98%)</td><td>2.52 (+2.89%)</td><td>1.15 (-11.17%)</td><td>0.78 (-5.11%)</td><td>0.41 (-2.66%)</td><td>0.90 (-10.98%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.49 (n/a)</td><td>1.31 (n/a)</td><td>0.83 (n/a)</td><td>0.43 (n/a)</td><td>1.03 (n/a)</td><td>2.45 (n/a)</td><td>1.29 (n/a)</td><td>0.82 (n/a)</td><td>0.42 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>456.82 (n/a)</td><td>510.30 (n/a)</td><td>241.70 (n/a)</td><td>120.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.30 (n/a)</td><td>386.24 (n/a)</td><td>322.70 (n/a)</td><td>271.00 (n/a)</td><td>140.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>480.40 (n/a)</td><td>428.98 (n/a)</td><td>456.70 (n/a)</td><td>313.50 (n/a)</td><td>68.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.40 (n/a)</td><td>424.76 (n/a)</td><td>431.10 (n/a)</td><td>322.00 (n/a)</td><td>95.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.20 (n/a)</td><td>402.94 (n/a)</td><td>421.80 (n/a)</td><td>286.30 (n/a)</td><td>100.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1837.50 (n/a)</td><td>740.14 (n/a)</td><td>451.70 (n/a)</td><td>254.10 (n/a)</td><td>645.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (+11.75%)</td><td>0.03 <b>(+38.53%)</b></td><td>0.03 <b>(+74.84%)</b></td><td>0.02 <b>(+40.53%)</b></td><td>0.01 (-3.30%)</td><td>475.30 <b>(-28.84%)</b></td><td>292.68 <b>(-30.63%)</b></td><td>246.20 <b>(-42.80%)</b></td><td>221.80 (-10.53%)</td><td>104.89 <b>(-35.47%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.90 (n/a)</td><td>421.90 (n/a)</td><td>430.40 (n/a)</td><td>247.90 (n/a)</td><td>162.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+18.15%)</td><td>0.03 (+6.59%)</td><td>0.02 (-7.35%)</td><td>0.02 <b>(+41.36%)</b></td><td>0.01 (+15.08%)</td><td>471.20 <b>(-29.26%)</b></td><td>352.40 (-8.00%)</td><td>333.80 (+7.92%)</td><td>236.70 (-15.34%)</td><td>112.55 <b>(-30.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.10 (n/a)</td><td>383.04 (n/a)</td><td>309.30 (n/a)</td><td>279.60 (n/a)</td><td>162.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 <b>(+25.97%)</b></td><td>0.03 <b>(+31.38%)</b></td><td>0.03 <b>(+79.43%)</b></td><td>0.02 <b>(+26.73%)</b></td><td>0.01 <b>(+32.36%)</b></td><td>510.80 <b>(-21.09%)</b></td><td>359.18 <b>(-22.45%)</b></td><td>272.20 <b>(-44.28%)</b></td><td>245.80 <b>(-20.61%)</b></td><td>135.30 (-8.47%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.30 (n/a)</td><td>463.16 (n/a)</td><td>488.50 (n/a)</td><td>309.60 (n/a)</td><td>147.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-9.07%)</td><td>0.02 (-5.16%)</td><td>0.02 <b>(-25.95%)</b></td><td>0.02 (+19.36%)</td><td>0.01 <b>(-29.43%)</b></td><td>447.00 (-16.21%)</td><td>362.04 (-1.45%)</td><td>414.30 <b>(+35.04%)</b></td><td>256.40 (+9.95%)</td><td>91.07 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.50 (n/a)</td><td>367.38 (n/a)</td><td>306.80 (n/a)</td><td>233.20 (n/a)</td><td>146.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-9.60%)</td><td>0.02 (-5.73%)</td><td>0.03 (+9.71%)</td><td>0.01 (-10.70%)</td><td>0.01 (+5.39%)</td><td>551.20 (+11.99%)</td><td>379.38 (+9.53%)</td><td>296.10 (-8.86%)</td><td>252.50 (+10.60%)</td><td>144.38 <b>(+34.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.20 (n/a)</td><td>346.38 (n/a)</td><td>324.90 (n/a)</td><td>228.30 (n/a)</td><td>107.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 <b>(-50.23%)</b></td><td>0.01 <b>(-27.48%)</b></td><td>0.01 (-7.03%)</td><td>0.01 <b>(-43.12%)</b></td><td>0.00 <b>(-53.94%)</b></td><td>1058.80 <b>(+75.82%)</b></td><td>651.00 <b>(+36.07%)</b></td><td>549.90 (+7.55%)</td><td>531.80 <b>(+100.91%)</b></td><td>228.36 <b>(+78.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.20 (n/a)</td><td>478.44 (n/a)</td><td>511.30 (n/a)</td><td>264.70 (n/a)</td><td>128.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+15.45%)</td><td>0.03 <b>(+42.10%)</b></td><td>0.03 <b>(+45.18%)</b></td><td>0.02 <b>(+40.33%)</b></td><td>0.01 (-3.42%)</td><td>428.80 <b>(-28.75%)</b></td><td>303.36 <b>(-31.20%)</b></td><td>287.80 <b>(-31.12%)</b></td><td>246.00 (-13.38%)</td><td>73.00 <b>(-37.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.80 (n/a)</td><td>440.96 (n/a)</td><td>417.80 (n/a)</td><td>284.00 (n/a)</td><td>116.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+3.15%)</td><td>0.02 <b>(+22.48%)</b></td><td>0.02 <b>(+38.26%)</b></td><td>0.01 (+10.37%)</td><td>0.01 (-7.16%)</td><td>547.90 (-9.39%)</td><td>388.70 (-19.82%)</td><td>392.90 <b>(-27.67%)</b></td><td>277.20 (-3.04%)</td><td>106.30 (-18.55%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.70 (n/a)</td><td>484.78 (n/a)</td><td>543.20 (n/a)</td><td>285.90 (n/a)</td><td>130.52 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-15.78%)</td><td>0.03 (-4.04%)</td><td>0.03 (+5.91%)</td><td>0.01 (-19.62%)</td><td>0.01 (-9.90%)</td><td>579.00 <b>(+24.41%)</b></td><td>358.10 (+5.62%)</td><td>290.60 (-5.56%)</td><td>239.50 (+18.74%)</td><td>142.69 <b>(+26.47%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.40 (n/a)</td><td>339.04 (n/a)</td><td>307.70 (n/a)</td><td>201.70 (n/a)</td><td>112.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 <b>(-21.62%)</b></td><td>0.02 (+16.59%)</td><td>0.02 (-3.39%)</td><td>0.02 <b>(+321.59%)</b></td><td>0.01 <b>(-35.20%)</b></td><td>496.20 <b>(-76.28%)</b></td><td>378.32 <b>(-47.72%)</b></td><td>450.20 (+3.49%)</td><td>227.60 <b>(+27.58%)</b></td><td>134.72 <b>(-82.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2092.00 (n/a)</td><td>723.62 (n/a)</td><td>435.00 (n/a)</td><td>178.40 (n/a)</td><td>774.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 <b>(+44.93%)</b></td><td>0.03 <b>(+48.34%)</b></td><td>0.03 <b>(+71.57%)</b></td><td>0.02 (-4.27%)</td><td>0.01 <b>(+139.23%)</b></td><td>496.80 (+4.46%)</td><td>294.26 <b>(-28.10%)</b></td><td>245.00 <b>(-41.71%)</b></td><td>225.10 <b>(-31.01%)</b></td><td>114.37 <b>(+78.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>475.60 (n/a)</td><td>409.28 (n/a)</td><td>420.30 (n/a)</td><td>326.30 (n/a)</td><td>64.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-17.54%)</td><td>0.02 (-4.95%)</td><td>0.03 (+18.44%)</td><td>0.01 (-13.35%)</td><td>0.01 (-9.29%)</td><td>604.30 (+15.41%)</td><td>377.90 (+7.11%)</td><td>307.00 (-15.57%)</td><td>246.30 <b>(+21.27%)</b></td><td>155.29 <b>(+27.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.60 (n/a)</td><td>352.82 (n/a)</td><td>363.60 (n/a)</td><td>203.10 (n/a)</td><td>122.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-8.18%)</td><td>0.02 (+15.12%)</td><td>0.03 <b>(+61.71%)</b></td><td>0.01 (-8.66%)</td><td>0.01 <b>(+21.15%)</b></td><td>619.40 (+9.47%)</td><td>401.86 (-5.84%)</td><td>276.30 <b>(-38.16%)</b></td><td>252.60 (+8.93%)</td><td>192.98 <b>(+57.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.80 (n/a)</td><td>426.80 (n/a)</td><td>446.80 (n/a)</td><td>231.90 (n/a)</td><td>122.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 <b>(+25.03%)</b></td><td>0.02 (+1.11%)</td><td>0.02 (-7.77%)</td><td>0.01 <b>(-20.99%)</b></td><td>0.01 <b>(+192.67%)</b></td><td>649.50 <b>(+26.56%)</b></td><td>462.66 (+5.93%)</td><td>473.40 (+8.43%)</td><td>306.80 <b>(-20.02%)</b></td><td>142.05 <b>(+186.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>513.20 (n/a)</td><td>436.74 (n/a)</td><td>436.60 (n/a)</td><td>383.60 (n/a)</td><td>49.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.08 <b>(-22.80%)</b></td><td>0.06 <b>(-26.99%)</b></td><td>0.05 <b>(-42.89%)</b></td><td>0.05 (-13.21%)</td><td>0.02 <b>(-32.72%)</b></td><td>521.60 (+15.22%)</td><td>426.98 <b>(+33.56%)</b></td><td>467.10 <b>(+75.07%)</b></td><td>294.30 <b>(+29.53%)</b></td><td>106.85 (+1.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>452.70 (n/a)</td><td>319.68 (n/a)</td><td>266.80 (n/a)</td><td>227.20 (n/a)</td><td>105.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.14 (-10.44%)</td><td>0.12 (-5.50%)</td><td>0.14 (-0.73%)</td><td>0.08 (+3.32%)</td><td>0.03 (-13.01%)</td><td>541.90 (-3.21%)</td><td>372.12 (+4.19%)</td><td>301.40 (+0.74%)</td><td>296.40 (+11.64%)</td><td>109.33 (-10.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>559.90 (n/a)</td><td>357.16 (n/a)</td><td>299.20 (n/a)</td><td>265.50 (n/a)</td><td>121.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+5.58%)</td><td>0.02 (+9.03%)</td><td>0.02 (+8.64%)</td><td>0.01 <b>(+163.79%)</b></td><td>0.01 (-17.54%)</td><td>555.30 <b>(-62.09%)</b></td><td>358.74 <b>(-32.53%)</b></td><td>280.50 (-7.97%)</td><td>246.50 (-5.27%)</td><td>140.95 <b>(-73.05%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1464.90 (n/a)</td><td>531.74 (n/a)</td><td>304.80 (n/a)</td><td>260.20 (n/a)</td><td>523.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+3.72%)</td><td>0.03 <b>(+48.53%)</b></td><td>0.03 <b>(+74.18%)</b></td><td>0.02 <b>(+409.94%)</b></td><td>0.00 <b>(-57.23%)</b></td><td>366.00 <b>(-80.39%)</b></td><td>291.94 <b>(-57.77%)</b></td><td>299.70 <b>(-42.60%)</b></td><td>240.30 (-3.57%)</td><td>50.99 <b>(-92.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1866.40 (n/a)</td><td>691.24 (n/a)</td><td>522.10 (n/a)</td><td>249.20 (n/a)</td><td>669.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (+4.82%)</td><td>0.03 (+4.77%)</td><td>0.03 <b>(+21.51%)</b></td><td>0.02 (-5.65%)</td><td>0.01 (+1.87%)</td><td>592.50 (+5.99%)</td><td>427.94 (-4.40%)</td><td>430.20 (-17.70%)</td><td>285.10 (-4.62%)</td><td>134.00 (+1.48%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.00 (n/a)</td><td>447.62 (n/a)</td><td>522.70 (n/a)</td><td>298.90 (n/a)</td><td>132.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (+4.27%)</td><td>0.02 (-4.02%)</td><td>0.03 (+7.11%)</td><td>0.01 (-3.19%)</td><td>0.01 <b>(+37.20%)</b></td><td>598.30 (+3.30%)</td><td>395.20 (+12.12%)</td><td>264.50 (-6.64%)</td><td>256.20 (-4.08%)</td><td>183.07 <b>(+38.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.20 (n/a)</td><td>352.48 (n/a)</td><td>283.30 (n/a)</td><td>267.10 (n/a)</td><td>132.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-15.73%)</td><td>0.03 <b>(+29.40%)</b></td><td>0.03 <b>(+40.65%)</b></td><td>0.02 <b>(+287.53%)</b></td><td>0.00 <b>(-66.80%)</b></td><td>500.70 <b>(-74.20%)</b></td><td>399.56 <b>(-47.44%)</b></td><td>368.00 <b>(-28.90%)</b></td><td>346.40 (+18.67%)</td><td>62.17 <b>(-90.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1940.40 (n/a)</td><td>760.20 (n/a)</td><td>517.60 (n/a)</td><td>291.90 (n/a)</td><td>671.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 <b>(+23.17%)</b></td><td>0.03 (+1.39%)</td><td>0.03 (-3.53%)</td><td>0.00 <b>(-69.20%)</b></td><td>0.02 <b>(+41.34%)</b></td><td>1927.40 <b>(+224.64%)</b></td><td>611.52 <b>(+62.72%)</b></td><td>311.70 (+3.66%)</td><td>181.90 (-18.83%)</td><td>740.09 <b>(+324.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.70 (n/a)</td><td>375.80 (n/a)</td><td>300.70 (n/a)</td><td>224.10 (n/a)</td><td>174.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (+1.99%)</td><td>0.03 (+7.62%)</td><td>0.03 (+13.14%)</td><td>0.01 <b>(-28.45%)</b></td><td>0.01 <b>(+44.30%)</b></td><td>740.30 <b>(+39.76%)</b></td><td>419.68 (+1.28%)</td><td>347.20 (-11.61%)</td><td>270.50 (-1.96%)</td><td>196.38 <b>(+87.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.70 (n/a)</td><td>414.38 (n/a)</td><td>392.80 (n/a)</td><td>275.90 (n/a)</td><td>104.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 <b>(+24.00%)</b></td><td>0.02 (+18.12%)</td><td>0.02 (-11.78%)</td><td>0.00 <b>(-28.21%)</b></td><td>0.01 <b>(+53.83%)</b></td><td>2424.40 <b>(+39.30%)</b></td><td>799.72 (+14.67%)</td><td>525.20 (+13.36%)</td><td>245.10 (-19.35%)</td><td>919.03 <b>(+55.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1740.40 (n/a)</td><td>697.38 (n/a)</td><td>463.30 (n/a)</td><td>303.90 (n/a)</td><td>590.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+5.38%)</td><td>0.02 (+10.49%)</td><td>0.02 (+15.28%)</td><td>0.02 (+1.13%)</td><td>0.00 <b>(+20.17%)</b></td><td>588.80 (-1.11%)</td><td>483.08 (-9.05%)</td><td>471.40 (-13.25%)</td><td>405.80 (-5.10%)</td><td>72.41 (+16.44%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>595.40 (n/a)</td><td>531.12 (n/a)</td><td>543.40 (n/a)</td><td>427.60 (n/a)</td><td>62.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (-4.05%)</td><td>0.02 (+3.72%)</td><td>0.01 (-17.55%)</td><td>0.01 <b>(+210.07%)</b></td><td>0.01 <b>(-30.39%)</b></td><td>657.40 <b>(-67.75%)</b></td><td>505.92 <b>(-34.06%)</b></td><td>593.60 <b>(+21.29%)</b></td><td>302.90 (+4.23%)</td><td>176.66 <b>(-75.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2038.50 (n/a)</td><td>767.24 (n/a)</td><td>489.40 (n/a)</td><td>290.60 (n/a)</td><td>731.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (+19.45%)</td><td>0.02 (+10.46%)</td><td>0.02 (-9.66%)</td><td>0.02 <b>(+239.40%)</b></td><td>0.01 (-1.47%)</td><td>560.60 <b>(-70.54%)</b></td><td>469.70 <b>(-33.69%)</b></td><td>505.50 (+10.69%)</td><td>233.20 (-16.30%)</td><td>134.40 <b>(-80.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1902.60 (n/a)</td><td>708.30 (n/a)</td><td>456.70 (n/a)</td><td>278.60 (n/a)</td><td>672.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 <b>(-38.04%)</b></td><td>0.01 <b>(-31.79%)</b></td><td>0.02 <b>(-20.71%)</b></td><td>0.00 <b>(-71.37%)</b></td><td>0.01 (-0.45%)</td><td>1980.10 <b>(+249.29%)</b></td><td>808.86 <b>(+87.04%)</b></td><td>521.10 <b>(+26.14%)</b></td><td>458.50 <b>(+61.39%)</b></td><td>658.11 <b>(+478.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>432.46 (n/a)</td><td>413.10 (n/a)</td><td>284.10 (n/a)</td><td>113.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.38 (+17.33%)</td><td>0.31 <b>(+22.25%)</b></td><td>0.33 (+14.26%)</td><td>0.24 <b>(+33.45%)</b></td><td>0.06 (-11.56%)</td><td>406.60 <b>(-25.06%)</b></td><td>323.22 <b>(-20.60%)</b></td><td>294.20 (-12.47%)</td><td>260.80 (-14.77%)</td><td>63.62 <b>(-44.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>542.60 (n/a)</td><td>407.06 (n/a)</td><td>336.10 (n/a)</td><td>306.00 (n/a)</td><td>114.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.44 <b>(+31.17%)</b></td><td>0.27 (+16.77%)</td><td>0.22 (+2.17%)</td><td>0.17 (-8.91%)</td><td>0.11 <b>(+84.31%)</b></td><td>583.90 (+9.78%)</td><td>409.84 (-7.51%)</td><td>448.10 (-2.12%)</td><td>221.60 <b>(-23.74%)</b></td><td>144.80 <b>(+59.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>531.90 (n/a)</td><td>443.12 (n/a)</td><td>457.80 (n/a)</td><td>290.60 (n/a)</td><td>90.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.34 <b>(+36.77%)</b></td><td>0.26 <b>(+29.92%)</b></td><td>0.27 <b>(+46.93%)</b></td><td>0.15 (-4.01%)</td><td>0.08 <b>(+96.50%)</b></td><td>643.00 (+4.18%)</td><td>416.82 (-18.65%)</td><td>363.90 <b>(-31.94%)</b></td><td>290.60 <b>(-26.89%)</b></td><td>145.90 <b>(+49.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>617.20 (n/a)</td><td>512.38 (n/a)</td><td>534.70 (n/a)</td><td>397.50 (n/a)</td><td>97.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.29 (-9.46%)</td><td>0.20 (-10.40%)</td><td>0.18 <b>(-22.84%)</b></td><td>0.12 (-14.29%)</td><td>0.07 (-0.54%)</td><td>617.30 (+16.67%)</td><td>423.30 (+13.69%)</td><td>406.50 <b>(+29.58%)</b></td><td>258.10 (+10.49%)</td><td>157.63 <b>(+20.63%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>529.10 (n/a)</td><td>372.34 (n/a)</td><td>313.70 (n/a)</td><td>233.60 (n/a)</td><td>130.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.28 <b>(+89.43%)</b></td><td>0.16 <b>(+43.22%)</b></td><td>0.14 (+2.30%)</td><td>0.04 (-0.04%)</td><td>0.10 <b>(+104.67%)</b></td><td>1922.10 (+0.04%)</td><td>733.50 (-13.43%)</td><td>514.30 (-2.24%)</td><td>262.30 <b>(-47.21%)</b></td><td>683.18 (+11.52%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1921.40 (n/a)</td><td>847.26 (n/a)</td><td>526.10 (n/a)</td><td>496.90 (n/a)</td><td>612.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.31 <b>(+25.69%)</b></td><td>0.18 (+14.53%)</td><td>0.15 (+4.78%)</td><td>0.13 (+13.71%)</td><td>0.08 <b>(+40.15%)</b></td><td>557.90 (-12.06%)</td><td>457.62 (-10.50%)</td><td>504.30 (-4.56%)</td><td>236.30 <b>(-20.41%)</b></td><td>127.81 (-4.71%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>634.40 (n/a)</td><td>511.28 (n/a)</td><td>528.40 (n/a)</td><td>296.90 (n/a)</td><td>134.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.42 <b>(-22.49%)</b></td><td>0.31 <b>(-27.66%)</b></td><td>0.32 <b>(-27.17%)</b></td><td>0.21 <b>(-21.04%)</b></td><td>0.09 (-14.50%)</td><td>615.00 <b>(+26.65%)</b></td><td>451.30 <b>(+39.70%)</b></td><td>408.70 <b>(+37.29%)</b></td><td>310.70 <b>(+29.03%)</b></td><td>132.22 <b>(+37.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>485.60 (n/a)</td><td>323.06 (n/a)</td><td>297.70 (n/a)</td><td>240.80 (n/a)</td><td>95.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.43 (-9.23%)</td><td>0.31 (-15.31%)</td><td>0.25 <b>(-42.15%)</b></td><td>0.19 <b>(+167.97%)</b></td><td>0.11 <b>(-33.44%)</b></td><td>678.90 <b>(-62.68%)</b></td><td>471.08 <b>(-22.14%)</b></td><td>526.40 <b>(+72.87%)</b></td><td>306.60 (+10.17%)</td><td>160.34 <b>(-76.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.43 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1819.20 (n/a)</td><td>605.00 (n/a)</td><td>304.50 (n/a)</td><td>278.30 (n/a)</td><td>678.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.41 (-13.30%)</td><td>0.30 (-15.10%)</td><td>0.30 <b>(-26.85%)</b></td><td>0.17 (-7.58%)</td><td>0.10 <b>(-21.86%)</b></td><td>761.20 (+8.20%)</td><td>484.66 (+14.33%)</td><td>443.70 <b>(+36.69%)</b></td><td>322.40 (+15.35%)</td><td>179.10 (-2.22%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>703.50 (n/a)</td><td>423.90 (n/a)</td><td>324.60 (n/a)</td><td>279.50 (n/a)</td><td>183.16 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+3.29%)</td><td>0.01 (+10.19%)</td><td>0.02 (+15.40%)</td><td>0.00 <b>(-55.15%)</b></td><td>0.01 <b>(+25.05%)</b></td><td>1845.60 <b>(+122.98%)</b></td><td>578.00 <b>(+36.86%)</b></td><td>270.30 (-13.34%)</td><td>232.90 (-3.20%)</td><td>708.83 <b>(+192.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>827.70 (n/a)</td><td>422.34 (n/a)</td><td>311.90 (n/a)</td><td>240.60 (n/a)</td><td>242.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+7.93%)</td><td>0.01 (-11.11%)</td><td>0.01 (-8.65%)</td><td>0.01 <b>(-25.63%)</b></td><td>0.00 <b>(+34.42%)</b></td><td>569.70 <b>(+34.46%)</b></td><td>361.60 <b>(+20.82%)</b></td><td>301.00 (+9.45%)</td><td>208.70 (-7.37%)</td><td>147.83 <b>(+76.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>423.70 (n/a)</td><td>299.30 (n/a)</td><td>275.00 (n/a)</td><td>225.30 (n/a)</td><td>83.98 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+5.73%)</td><td>0.01 <b>(+28.36%)</b></td><td>0.01 <b>(+45.60%)</b></td><td>0.01 <b>(+44.14%)</b></td><td>0.00 (-6.93%)</td><td>391.70 <b>(-30.62%)</b></td><td>309.08 <b>(-24.11%)</b></td><td>274.00 <b>(-31.33%)</b></td><td>242.60 (-5.42%)</td><td>72.98 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.60 (n/a)</td><td>407.26 (n/a)</td><td>399.00 (n/a)</td><td>256.50 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.48 (-9.72%)</td><td>0.32 <b>(-23.75%)</b></td><td>0.33 (-11.27%)</td><td>0.07 <b>(-78.64%)</b></td><td>0.17 <b>(+74.57%)</b></td><td>1936.10 <b>(+368.11%)</b></td><td>688.06 <b>(+106.56%)</b></td><td>397.10 (+12.68%)</td><td>273.70 (+10.76%)</td><td>705.38 <b>(+867.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>413.60 (n/a)</td><td>333.10 (n/a)</td><td>352.40 (n/a)</td><td>247.10 (n/a)</td><td>72.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.58 (-1.36%)</td><td>0.40 (-8.93%)</td><td>0.44 (-19.23%)</td><td>0.24 <b>(+37.49%)</b></td><td>0.14 <b>(-25.78%)</b></td><td>539.70 <b>(-27.27%)</b></td><td>361.14 (-1.99%)</td><td>297.50 <b>(+23.80%)</b></td><td>226.80 (+1.39%)</td><td>129.19 <b>(-41.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.55 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>742.10 (n/a)</td><td>368.46 (n/a)</td><td>240.30 (n/a)</td><td>223.70 (n/a)</td><td>221.98 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.51 (-1.20%)</td><td>0.41 (+7.36%)</td><td>0.46 (+15.56%)</td><td>0.30 <b>(+46.37%)</b></td><td>0.10 <b>(-22.09%)</b></td><td>444.90 <b>(-31.68%)</b></td><td>342.50 (-12.49%)</td><td>286.40 (-13.47%)</td><td>259.70 (+1.21%)</td><td>92.33 <b>(-43.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>651.20 (n/a)</td><td>391.38 (n/a)</td><td>331.00 (n/a)</td><td>256.60 (n/a)</td><td>162.98 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.55 (+7.54%)</td><td>0.47 <b>(+29.75%)</b></td><td>0.48 <b>(+64.79%)</b></td><td>0.38 <b>(+69.95%)</b></td><td>0.08 <b>(-38.98%)</b></td><td>347.30 <b>(-41.16%)</b></td><td>290.48 <b>(-29.06%)</b></td><td>274.30 <b>(-39.31%)</b></td><td>241.50 (-7.01%)</td><td>52.38 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>590.20 (n/a)</td><td>409.48 (n/a)</td><td>452.00 (n/a)</td><td>259.70 (n/a)</td><td>143.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.39 <b>(-31.16%)</b></td><td>0.32 <b>(-26.34%)</b></td><td>0.30 <b>(-31.93%)</b></td><td>0.29 (+10.47%)</td><td>0.04 <b>(-60.08%)</b></td><td>462.90 (-9.48%)</td><td>417.06 <b>(+28.54%)</b></td><td>436.20 <b>(+46.92%)</b></td><td>337.10 <b>(+45.30%)</b></td><td>53.13 <b>(-50.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>511.40 (n/a)</td><td>324.46 (n/a)</td><td>296.90 (n/a)</td><td>232.00 (n/a)</td><td>107.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (+9.08%)</td><td>0.01 (+7.69%)</td><td>0.01 (+12.73%)</td><td>0.01 (-14.26%)</td><td>0.00 <b>(+39.34%)</b></td><td>500.20 (+16.62%)</td><td>332.36 (-4.25%)</td><td>303.20 (-11.29%)</td><td>245.20 (-8.30%)</td><td>99.17 <b>(+55.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>428.90 (n/a)</td><td>347.12 (n/a)</td><td>341.80 (n/a)</td><td>267.40 (n/a)</td><td>63.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (-6.58%)</td><td>0.01 (+5.57%)</td><td>0.01 <b>(+35.62%)</b></td><td>0.01 (-15.64%)</td><td>0.00 (-16.29%)</td><td>516.40 (+18.55%)</td><td>312.62 (-5.65%)</td><td>281.10 <b>(-26.26%)</b></td><td>233.30 (+7.02%)</td><td>116.39 (+15.06%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>435.60 (n/a)</td><td>331.34 (n/a)</td><td>381.20 (n/a)</td><td>218.00 (n/a)</td><td>101.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.00 <b>(+75.00%)</b></td><td>0.00 <b>(+53.85%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+162.20%)</b></td><td>18823.11 (-7.83%)</td><td>13121.55 <b>(-21.45%)</b></td><td>16264.61 (-6.13%)</td><td>6104.24 <b>(-41.54%)</b></td><td>6356.79 <b>(+63.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20422.69 (n/a)</td><td>16705.37 (n/a)</td><td>17326.83 (n/a)</td><td>10441.56 (n/a)</td><td>3895.14 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.00 <b>(+27.27%)</b></td><td>0.00 <b>(+23.81%)</b></td><td>0.00 <b>(+22.22%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+53.94%)</b></td><td>19205.41 (+2.92%)</td><td>9495.82 (-10.96%)</td><td>7761.48 (-17.62%)</td><td>5705.77 <b>(-23.16%)</b></td><td>5580.40 <b>(+21.79%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18660.83 (n/a)</td><td>10664.50 (n/a)</td><td>9421.47 (n/a)</td><td>7425.83 (n/a)</td><td>4582.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.13 (-13.50%)</td><td>0.10 <b>(-23.72%)</b></td><td>0.08 <b>(-38.41%)</b></td><td>0.08 <b>(-26.63%)</b></td><td>0.03 <b>(+59.38%)</b></td><td>27881.83 <b>(+36.28%)</b></td><td>22892.05 <b>(+36.64%)</b></td><td>26566.32 <b>(+62.22%)</b></td><td>16450.24 (+15.59%)</td><td>5721.85 <b>(+143.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>20459.71 (n/a)</td><td>16753.40 (n/a)</td><td>16376.48 (n/a)</td><td>14231.58 (n/a)</td><td>2345.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.14 (-3.36%)</td><td>0.10 (-1.49%)</td><td>0.09 (+12.31%)</td><td>0.07 (-1.64%)</td><td>0.03 (-14.57%)</td><td>29206.82 (+1.65%)</td><td>22512.77 (-0.60%)</td><td>23949.87 (-10.98%)</td><td>15190.10 (+3.49%)</td><td>6457.60 (-9.55%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>28732.28 (n/a)</td><td>22647.72 (n/a)</td><td>26903.25 (n/a)</td><td>14678.08 (n/a)</td><td>7139.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.51 (-15.26%)</td><td>1.06 (-9.60%)</td><td>1.42 (+3.07%)</td><td>0.16 <b>(-43.70%)</b></td><td>0.60 (-0.59%)</td><td>3347.80 <b>(+77.62%)</b></td><td>1026.70 <b>(+46.78%)</b></td><td>368.90 (-2.97%)</td><td>346.20 (+18.00%)</td><td>1307.04 <b>(+94.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.79 (n/a)</td><td>1.17 (n/a)</td><td>1.38 (n/a)</td><td>0.28 (n/a)</td><td>0.60 (n/a)</td><td>1884.80 (n/a)</td><td>699.46 (n/a)</td><td>380.20 (n/a)</td><td>293.40 (n/a)</td><td>673.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.27 (-18.47%)</td><td>1.86 (+18.20%)</td><td>1.70 (+11.74%)</td><td>1.40 <b>(+153.79%)</b></td><td>0.39 <b>(-56.25%)</b></td><td>747.50 <b>(-60.60%)</b></td><td>584.74 <b>(-36.03%)</b></td><td>618.30 (-10.50%)</td><td>461.00 <b>(+22.67%)</b></td><td>121.34 <b>(-80.16%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.79 (n/a)</td><td>1.57 (n/a)</td><td>1.52 (n/a)</td><td>0.55 (n/a)</td><td>0.88 (n/a)</td><td>1897.00 (n/a)</td><td>914.14 (n/a)</td><td>690.80 (n/a)</td><td>375.80 (n/a)</td><td>611.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.72 (+4.36%)</td><td>1.08 (-8.13%)</td><td>1.21 (+15.32%)</td><td>0.22 <b>(-71.78%)</b></td><td>0.59 <b>(+60.81%)</b></td><td>2423.30 <b>(+254.34%)</b></td><td>835.36 <b>(+73.64%)</b></td><td>431.70 (-13.28%)</td><td>305.30 (-4.17%)</td><td>898.11 <b>(+503.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.65 (n/a)</td><td>1.18 (n/a)</td><td>1.05 (n/a)</td><td>0.77 (n/a)</td><td>0.37 (n/a)</td><td>683.90 (n/a)</td><td>481.10 (n/a)</td><td>497.80 (n/a)</td><td>318.60 (n/a)</td><td>148.93 (n/a)</td>
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
