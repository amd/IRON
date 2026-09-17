# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+21.35%)</b></td><td>0.02 <b>(+29.57%)</b></td><td>0.03 <b>(+51.20%)</b></td><td>0.01 (-2.31%)</td><td>0.01 <b>(+40.48%)</b></td><td>507.40 (+2.38%)</td><td>290.12 (-19.51%)</td><td>233.50 <b>(-33.87%)</b></td><td>223.50 (-17.59%)</td><td>122.19 <b>(+27.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.60 (n/a)</td><td>360.42 (n/a)</td><td>353.10 (n/a)</td><td>271.20 (n/a)</td><td>95.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+23.87%)</b></td><td>0.02 (+19.13%)</td><td>0.01 <b>(+21.89%)</b></td><td>0.01 (+2.13%)</td><td>0.01 <b>(+50.29%)</b></td><td>539.00 (-2.09%)</td><td>385.26 (-11.86%)</td><td>418.10 (-17.96%)</td><td>236.80 (-19.26%)</td><td>141.73 (+13.43%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.50 (n/a)</td><td>437.08 (n/a)</td><td>509.60 (n/a)</td><td>293.30 (n/a)</td><td>124.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+48.63%)</b></td><td>0.02 <b>(+35.25%)</b></td><td>0.02 <b>(+36.11%)</b></td><td>0.01 <b>(+23.61%)</b></td><td>0.01 <b>(+91.24%)</b></td><td>532.90 (-19.10%)</td><td>376.70 <b>(-22.54%)</b></td><td>379.10 <b>(-26.53%)</b></td><td>244.10 <b>(-32.72%)</b></td><td>126.53 (+4.60%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>658.70 (n/a)</td><td>486.34 (n/a)</td><td>516.00 (n/a)</td><td>362.80 (n/a)</td><td>120.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+21.22%)</b></td><td>0.02 <b>(+30.94%)</b></td><td>0.02 <b>(+37.67%)</b></td><td>0.01 (+3.43%)</td><td>0.01 <b>(+43.28%)</b></td><td>506.90 (-3.32%)</td><td>320.50 (-19.83%)</td><td>320.90 <b>(-27.37%)</b></td><td>188.30 (-17.52%)</td><td>129.89 (+13.98%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.30 (n/a)</td><td>399.80 (n/a)</td><td>441.80 (n/a)</td><td>228.30 (n/a)</td><td>113.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-7.29%)</td><td>0.02 (-12.83%)</td><td>0.01 <b>(-31.97%)</b></td><td>0.01 <b>(+26.28%)</b></td><td>0.00 <b>(-30.84%)</b></td><td>495.90 <b>(-20.82%)</b></td><td>413.08 (+5.67%)</td><td>446.60 <b>(+47.00%)</b></td><td>255.70 (+7.89%)</td><td>93.44 <b>(-44.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.30 (n/a)</td><td>390.90 (n/a)</td><td>303.80 (n/a)</td><td>237.00 (n/a)</td><td>168.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+15.42%)</td><td>0.02 <b>(+28.73%)</b></td><td>0.01 (+17.24%)</td><td>0.01 (+16.57%)</td><td>0.01 <b>(+39.40%)</b></td><td>503.70 (-14.22%)</td><td>385.46 <b>(-20.28%)</b></td><td>415.70 (-14.71%)</td><td>256.90 (-13.36%)</td><td>120.11 (+2.24%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.20 (n/a)</td><td>483.50 (n/a)</td><td>487.40 (n/a)</td><td>296.50 (n/a)</td><td>117.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (+16.06%)</td><td>0.04 (+9.06%)</td><td>0.04 <b>(+46.74%)</b></td><td>0.02 <b>(-23.91%)</b></td><td>0.02 <b>(+63.95%)</b></td><td>608.80 <b>(+31.43%)</b></td><td>392.64 (+2.29%)</td><td>296.70 <b>(-31.86%)</b></td><td>230.50 (-13.83%)</td><td>183.02 <b>(+90.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>463.20 (n/a)</td><td>383.86 (n/a)</td><td>435.40 (n/a)</td><td>267.50 (n/a)</td><td>95.84 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (+11.89%)</td><td>0.04 <b>(+37.29%)</b></td><td>0.05 <b>(+71.67%)</b></td><td>0.02 (+14.38%)</td><td>0.01 <b>(+28.77%)</b></td><td>499.10 (-12.58%)</td><td>345.52 <b>(-25.11%)</b></td><td>271.60 <b>(-41.75%)</b></td><td>234.80 (-10.65%)</td><td>130.77 (+4.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.90 (n/a)</td><td>461.34 (n/a)</td><td>466.30 (n/a)</td><td>262.80 (n/a)</td><td>125.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (-8.83%)</td><td>0.03 (-10.95%)</td><td>0.03 (+9.81%)</td><td>0.02 (-16.05%)</td><td>0.01 <b>(-24.32%)</b></td><td>666.50 (+19.12%)</td><td>437.40 (+7.85%)</td><td>438.60 (-8.93%)</td><td>245.80 (+9.68%)</td><td>159.26 (-0.28%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>405.58 (n/a)</td><td>481.60 (n/a)</td><td>224.10 (n/a)</td><td>159.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (+10.04%)</td><td>0.04 (-2.18%)</td><td>0.05 (+11.19%)</td><td>0.02 (-0.66%)</td><td>0.02 <b>(+33.27%)</b></td><td>542.40 (+0.67%)</td><td>345.82 (+7.97%)</td><td>255.20 (-10.08%)</td><td>213.70 (-9.10%)</td><td>153.17 <b>(+21.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>320.30 (n/a)</td><td>283.80 (n/a)</td><td>235.10 (n/a)</td><td>125.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(-23.85%)</b></td><td>0.04 (+0.33%)</td><td>0.04 <b>(+47.33%)</b></td><td>0.02 (+9.84%)</td><td>0.01 <b>(-50.23%)</b></td><td>494.60 (-8.96%)</td><td>336.14 (-10.30%)</td><td>291.60 <b>(-32.12%)</b></td><td>261.90 <b>(+31.28%)</b></td><td>94.41 <b>(-37.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>543.30 (n/a)</td><td>374.72 (n/a)</td><td>429.60 (n/a)</td><td>199.50 (n/a)</td><td>150.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (-17.54%)</td><td>0.03 (-8.95%)</td><td>0.04 (+4.56%)</td><td>0.01 <b>(-39.58%)</b></td><td>0.01 (-15.72%)</td><td>1053.60 <b>(+65.50%)</b></td><td>472.62 (+17.24%)</td><td>307.10 (-4.36%)</td><td>283.50 <b>(+21.26%)</b></td><td>330.20 <b>(+70.85%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>636.60 (n/a)</td><td>403.12 (n/a)</td><td>321.10 (n/a)</td><td>233.80 (n/a)</td><td>193.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(-34.64%)</b></td><td>0.06 <b>(-35.77%)</b></td><td>0.06 <b>(-42.05%)</b></td><td>0.05 <b>(-22.21%)</b></td><td>0.01 <b>(-44.51%)</b></td><td>504.10 <b>(+28.56%)</b></td><td>408.72 <b>(+51.62%)</b></td><td>418.20 <b>(+72.52%)</b></td><td>282.00 <b>(+53.01%)</b></td><td>81.75 (+2.96%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>392.10 (n/a)</td><td>269.56 (n/a)</td><td>242.40 (n/a)</td><td>184.30 (n/a)</td><td>79.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (-6.06%)</td><td>0.08 (+17.94%)</td><td>0.08 <b>(+52.70%)</b></td><td>0.06 <b>(+58.51%)</b></td><td>0.01 <b>(-55.86%)</b></td><td>399.80 <b>(-36.92%)</b></td><td>316.34 <b>(-25.08%)</b></td><td>313.60 <b>(-34.50%)</b></td><td>261.20 (+6.44%)</td><td>54.55 <b>(-67.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>633.80 (n/a)</td><td>422.24 (n/a)</td><td>478.80 (n/a)</td><td>245.40 (n/a)</td><td>169.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (+9.18%)</td><td>0.10 <b>(+38.41%)</b></td><td>0.10 <b>(+83.23%)</b></td><td>0.08 <b>(+96.68%)</b></td><td>0.02 <b>(-52.73%)</b></td><td>301.40 <b>(-49.16%)</b></td><td>250.42 <b>(-36.99%)</b></td><td>254.20 <b>(-45.42%)</b></td><td>205.10 (-8.44%)</td><td>38.29 <b>(-76.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>592.80 (n/a)</td><td>397.44 (n/a)</td><td>465.70 (n/a)</td><td>224.00 (n/a)</td><td>162.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 <b>(-31.55%)</b></td><td>0.05 (-19.48%)</td><td>0.05 (+7.37%)</td><td>0.03 <b>(-24.20%)</b></td><td>0.01 <b>(-49.77%)</b></td><td>736.20 <b>(+31.94%)</b></td><td>521.82 (+19.69%)</td><td>453.80 (-6.86%)</td><td>430.40 <b>(+46.10%)</b></td><td>126.38 (+0.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.00 (n/a)</td><td>435.96 (n/a)</td><td>487.20 (n/a)</td><td>294.60 (n/a)</td><td>125.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (-16.13%)</td><td>0.06 (-18.79%)</td><td>0.05 <b>(-37.73%)</b></td><td>0.04 (-12.12%)</td><td>0.02 (-18.48%)</td><td>650.40 (+13.79%)</td><td>437.06 <b>(+20.58%)</b></td><td>458.60 <b>(+60.57%)</b></td><td>256.80 (+19.22%)</td><td>162.60 (+3.88%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>571.60 (n/a)</td><td>362.46 (n/a)</td><td>285.60 (n/a)</td><td>215.40 (n/a)</td><td>156.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (+11.01%)</td><td>0.08 <b>(+45.74%)</b></td><td>0.08 <b>(+46.70%)</b></td><td>0.05 <b>(+190.69%)</b></td><td>0.02 <b>(-28.09%)</b></td><td>453.90 <b>(-65.60%)</b></td><td>312.00 <b>(-47.43%)</b></td><td>298.40 <b>(-31.84%)</b></td><td>202.40 (-9.92%)</td><td>90.56 <b>(-78.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1319.40 (n/a)</td><td>593.54 (n/a)</td><td>437.80 (n/a)</td><td>224.70 (n/a)</td><td>427.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 <b>(-20.41%)</b></td><td>0.14 (-18.58%)</td><td>0.14 <b>(-31.24%)</b></td><td>0.08 <b>(-20.98%)</b></td><td>0.05 <b>(-29.26%)</b></td><td>603.40 <b>(+26.53%)</b></td><td>379.94 (+18.05%)</td><td>355.20 <b>(+45.45%)</b></td><td>241.80 <b>(+25.61%)</b></td><td>144.29 (+3.16%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>476.90 (n/a)</td><td>321.84 (n/a)</td><td>244.20 (n/a)</td><td>192.50 (n/a)</td><td>139.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (-6.80%)</td><td>0.17 (+10.75%)</td><td>0.18 (-8.79%)</td><td>0.10 <b>(+276.75%)</b></td><td>0.04 <b>(-47.20%)</b></td><td>492.70 <b>(-73.46%)</b></td><td>307.82 <b>(-48.35%)</b></td><td>273.60 (+9.66%)</td><td>229.40 (+7.30%)</td><td>106.23 <b>(-85.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1856.20 (n/a)</td><td>595.94 (n/a)</td><td>249.50 (n/a)</td><td>213.80 (n/a)</td><td>709.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (+2.11%)</td><td>0.16 <b>(+27.90%)</b></td><td>0.18 <b>(+85.45%)</b></td><td>0.11 <b>(+89.43%)</b></td><td>0.04 <b>(-31.50%)</b></td><td>435.10 <b>(-47.21%)</b></td><td>319.18 <b>(-32.51%)</b></td><td>276.70 <b>(-46.07%)</b></td><td>236.80 (-2.07%)</td><td>92.12 <b>(-61.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>824.20 (n/a)</td><td>472.96 (n/a)</td><td>513.10 (n/a)</td><td>241.80 (n/a)</td><td>237.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (+4.89%)</td><td>0.14 (-18.10%)</td><td>0.12 <b>(-35.93%)</b></td><td>0.09 <b>(-23.15%)</b></td><td>0.05 <b>(+42.87%)</b></td><td>564.20 <b>(+30.12%)</b></td><td>382.22 <b>(+28.88%)</b></td><td>414.10 <b>(+56.09%)</b></td><td>238.60 (-4.67%)</td><td>130.16 <b>(+67.82%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>433.60 (n/a)</td><td>296.58 (n/a)</td><td>265.30 (n/a)</td><td>250.30 (n/a)</td><td>77.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (+19.94%)</td><td>0.15 <b>(+33.37%)</b></td><td>0.16 <b>(+50.21%)</b></td><td>0.11 (+15.55%)</td><td>0.04 <b>(+30.74%)</b></td><td>435.20 (-13.44%)</td><td>333.86 <b>(-24.22%)</b></td><td>305.90 <b>(-33.41%)</b></td><td>248.30 (-16.62%)</td><td>81.78 (-0.11%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>502.80 (n/a)</td><td>440.54 (n/a)</td><td>459.40 (n/a)</td><td>297.80 (n/a)</td><td>81.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 <b>(-26.17%)</b></td><td>0.09 <b>(-35.22%)</b></td><td>0.09 <b>(-40.61%)</b></td><td>0.03 <b>(-66.95%)</b></td><td>0.04 (-17.90%)</td><td>1851.20 <b>(+202.58%)</b></td><td>747.90 <b>(+89.89%)</b></td><td>527.50 <b>(+68.37%)</b></td><td>326.50 <b>(+35.48%)</b></td><td>624.25 <b>(+272.53%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>611.80 (n/a)</td><td>393.86 (n/a)</td><td>313.30 (n/a)</td><td>241.00 (n/a)</td><td>167.57 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (+13.63%)</td><td>0.01 (+9.01%)</td><td>0.01 (-5.05%)</td><td>0.01 (-7.32%)</td><td>0.00 (+19.49%)</td><td>501.30 (+7.90%)</td><td>310.52 (-6.24%)</td><td>293.40 (+5.31%)</td><td>224.10 (-12.01%)</td><td>111.68 (+18.30%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.60 (n/a)</td><td>331.18 (n/a)</td><td>278.60 (n/a)</td><td>254.70 (n/a)</td><td>94.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (+12.67%)</td><td>0.01 (+1.62%)</td><td>0.01 (+1.24%)</td><td>0.01 (+2.02%)</td><td>0.00 (+7.00%)</td><td>476.70 (-1.97%)</td><td>365.28 (-1.49%)</td><td>405.80 (-1.22%)</td><td>230.90 (-11.23%)</td><td>97.49 (-3.98%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.30 (n/a)</td><td>370.82 (n/a)</td><td>410.80 (n/a)</td><td>260.10 (n/a)</td><td>101.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-14.73%)</td><td>0.01 (-17.27%)</td><td>0.01 <b>(-33.89%)</b></td><td>0.00 <b>(+288.82%)</b></td><td>0.00 <b>(-53.39%)</b></td><td>649.70 <b>(-74.28%)</b></td><td>463.54 <b>(-39.47%)</b></td><td>427.50 <b>(+51.27%)</b></td><td>280.50 (+17.27%)</td><td>137.99 <b>(-86.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2526.20 (n/a)</td><td>765.76 (n/a)</td><td>282.60 (n/a)</td><td>239.20 (n/a)</td><td>991.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-7.82%)</td><td>0.01 <b>(-25.58%)</b></td><td>0.01 <b>(-40.71%)</b></td><td>0.00 (-6.69%)</td><td>0.00 (-9.82%)</td><td>526.20 (+7.17%)</td><td>415.20 <b>(+32.95%)</b></td><td>437.80 <b>(+68.64%)</b></td><td>239.90 (+8.45%)</td><td>105.40 (-4.19%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>312.30 (n/a)</td><td>259.60 (n/a)</td><td>221.20 (n/a)</td><td>110.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-14.39%)</td><td>0.01 (-0.03%)</td><td>0.01 <b>(+22.25%)</b></td><td>0.00 (-1.15%)</td><td>0.00 (-19.80%)</td><td>547.90 (+1.16%)</td><td>371.22 (-2.88%)</td><td>295.40 (-18.19%)</td><td>265.80 (+16.78%)</td><td>129.07 (-9.21%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>541.60 (n/a)</td><td>382.22 (n/a)</td><td>361.10 (n/a)</td><td>227.60 (n/a)</td><td>142.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (+1.12%)</td><td>0.01 (-0.23%)</td><td>0.01 (-0.06%)</td><td>0.00 <b>(+53.67%)</b></td><td>0.00 <b>(-20.91%)</b></td><td>671.60 <b>(-34.92%)</b></td><td>508.74 (-7.78%)</td><td>480.30 (+0.06%)</td><td>344.30 (-1.12%)</td><td>132.53 <b>(-51.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.00 (n/a)</td><td>551.66 (n/a)</td><td>480.00 (n/a)</td><td>348.20 (n/a)</td><td>275.14 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+27.93%)</b></td><td>0.02 <b>(+55.37%)</b></td><td>0.02 <b>(+47.41%)</b></td><td>0.01 <b>(+363.98%)</b></td><td>0.01 <b>(-27.25%)</b></td><td>401.50 <b>(-78.45%)</b></td><td>290.44 <b>(-58.05%)</b></td><td>280.00 <b>(-32.17%)</b></td><td>201.80 <b>(-21.84%)</b></td><td>78.62 <b>(-88.26%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1862.90 (n/a)</td><td>692.34 (n/a)</td><td>412.80 (n/a)</td><td>258.20 (n/a)</td><td>669.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-6.73%)</td><td>0.02 <b>(+29.52%)</b></td><td>0.02 <b>(+85.04%)</b></td><td>0.00 <b>(-71.36%)</b></td><td>0.01 <b>(+36.34%)</b></td><td>1832.30 <b>(+249.21%)</b></td><td>571.52 <b>(+28.47%)</b></td><td>264.10 <b>(-45.95%)</b></td><td>239.50 (+7.21%)</td><td>704.88 <b>(+458.76%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.70 (n/a)</td><td>444.86 (n/a)</td><td>488.60 (n/a)</td><td>223.40 (n/a)</td><td>126.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(+42.56%)</b></td><td>0.01 (-4.13%)</td><td>0.01 (-12.77%)</td><td>0.01 (-13.34%)</td><td>0.01 <b>(+100.98%)</b></td><td>622.40 (+15.39%)</td><td>452.84 (+17.69%)</td><td>458.70 (+14.65%)</td><td>182.20 <b>(-29.87%)</b></td><td>166.59 <b>(+51.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.40 (n/a)</td><td>384.78 (n/a)</td><td>400.10 (n/a)</td><td>259.80 (n/a)</td><td>109.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(+29.94%)</b></td><td>0.01 (+8.09%)</td><td>0.01 (+2.56%)</td><td>0.01 <b>(-38.18%)</b></td><td>0.00 <b>(+125.03%)</b></td><td>997.40 <b>(+61.76%)</b></td><td>523.02 (+4.82%)</td><td>449.00 (-2.50%)</td><td>319.60 <b>(-23.04%)</b></td><td>270.79 <b>(+205.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.60 (n/a)</td><td>498.96 (n/a)</td><td>460.50 (n/a)</td><td>415.30 (n/a)</td><td>88.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(-25.99%)</b></td><td>0.01 (-7.57%)</td><td>0.01 (+0.27%)</td><td>0.01 (-14.84%)</td><td>0.00 <b>(-32.40%)</b></td><td>607.50 (+17.44%)</td><td>423.44 (+4.37%)</td><td>448.70 (-0.27%)</td><td>273.60 <b>(+35.11%)</b></td><td>137.04 (+2.25%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.30 (n/a)</td><td>405.72 (n/a)</td><td>449.90 (n/a)</td><td>202.50 (n/a)</td><td>134.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-19.38%)</td><td>0.01 (-16.87%)</td><td>0.01 (-4.66%)</td><td>0.01 (+0.05%)</td><td>0.00 <b>(-49.48%)</b></td><td>598.40 (-0.05%)</td><td>518.96 (+14.42%)</td><td>520.10 (+4.88%)</td><td>383.60 <b>(+24.02%)</b></td><td>85.35 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.70 (n/a)</td><td>453.54 (n/a)</td><td>495.90 (n/a)</td><td>309.30 (n/a)</td><td>132.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(-42.56%)</b></td><td>0.02 <b>(-38.11%)</b></td><td>0.02 <b>(-40.37%)</b></td><td>0.01 <b>(-36.49%)</b></td><td>0.00 <b>(-58.60%)</b></td><td>716.60 <b>(+57.46%)</b></td><td>530.24 <b>(+57.10%)</b></td><td>493.10 <b>(+67.72%)</b></td><td>451.10 <b>(+74.10%)</b></td><td>107.56 (+17.49%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.10 (n/a)</td><td>337.52 (n/a)</td><td>294.00 (n/a)</td><td>259.10 (n/a)</td><td>91.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+2.57%)</td><td>0.02 <b>(-21.26%)</b></td><td>0.02 <b>(-31.29%)</b></td><td>0.01 <b>(-46.04%)</b></td><td>0.01 <b>(+44.01%)</b></td><td>997.80 <b>(+85.33%)</b></td><td>599.84 <b>(+41.83%)</b></td><td>593.50 <b>(+45.54%)</b></td><td>283.70 (-2.51%)</td><td>259.87 <b>(+144.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.40 (n/a)</td><td>422.94 (n/a)</td><td>407.80 (n/a)</td><td>291.00 (n/a)</td><td>106.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (-18.65%)</td><td>0.03 <b>(-36.13%)</b></td><td>0.02 <b>(-42.51%)</b></td><td>0.02 <b>(-49.85%)</b></td><td>0.01 <b>(+47.33%)</b></td><td>587.30 <b>(+99.42%)</b></td><td>450.32 <b>(+68.37%)</b></td><td>487.50 <b>(+73.98%)</b></td><td>250.20 <b>(+22.95%)</b></td><td>131.77 <b>(+256.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>294.50 (n/a)</td><td>267.46 (n/a)</td><td>280.20 (n/a)</td><td>203.50 (n/a)</td><td>36.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(+57.28%)</b></td><td>0.04 <b>(+64.32%)</b></td><td>0.04 <b>(+83.19%)</b></td><td>0.02 (+3.60%)</td><td>0.01 <b>(+158.93%)</b></td><td>562.20 (-3.47%)</td><td>323.74 <b>(-34.18%)</b></td><td>276.80 <b>(-45.42%)</b></td><td>231.10 <b>(-36.42%)</b></td><td>136.67 <b>(+72.03%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>582.40 (n/a)</td><td>491.82 (n/a)</td><td>507.10 (n/a)</td><td>363.50 (n/a)</td><td>79.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(-45.83%)</b></td><td>0.02 <b>(-30.97%)</b></td><td>0.03 <b>(-33.22%)</b></td><td>0.02 (+12.52%)</td><td>0.00 <b>(-74.22%)</b></td><td>514.40 (-11.13%)</td><td>431.70 (+19.82%)</td><td>410.10 <b>(+49.73%)</b></td><td>345.00 <b>(+84.59%)</b></td><td>77.45 <b>(-58.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>578.80 (n/a)</td><td>360.28 (n/a)</td><td>273.90 (n/a)</td><td>186.90 (n/a)</td><td>187.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 <b>(+24.71%)</b></td><td>0.03 (+1.67%)</td><td>0.02 (-15.77%)</td><td>0.02 <b>(-21.52%)</b></td><td>0.01 <b>(+98.01%)</b></td><td>659.00 <b>(+27.42%)</b></td><td>467.78 (+10.55%)</td><td>546.70 (+18.72%)</td><td>242.50 (-19.83%)</td><td>186.92 <b>(+101.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.20 (n/a)</td><td>423.14 (n/a)</td><td>460.50 (n/a)</td><td>302.50 (n/a)</td><td>92.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (+7.37%)</td><td>0.06 (-13.99%)</td><td>0.05 <b>(-37.64%)</b></td><td>0.04 (-19.44%)</td><td>0.02 <b>(+58.92%)</b></td><td>569.20 <b>(+24.14%)</b></td><td>393.22 <b>(+25.18%)</b></td><td>442.90 <b>(+60.35%)</b></td><td>229.40 (-6.86%)</td><td>143.13 <b>(+69.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>458.50 (n/a)</td><td>314.12 (n/a)</td><td>276.20 (n/a)</td><td>246.30 (n/a)</td><td>84.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(+21.36%)</b></td><td>0.06 <b>(+34.95%)</b></td><td>0.06 <b>(+52.29%)</b></td><td>0.04 <b>(+236.80%)</b></td><td>0.02 (-6.45%)</td><td>556.20 <b>(-70.31%)</b></td><td>390.20 <b>(-45.47%)</b></td><td>328.20 <b>(-34.35%)</b></td><td>235.20 (-17.62%)</td><td>151.83 <b>(-76.93%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1873.40 (n/a)</td><td>715.62 (n/a)</td><td>499.90 (n/a)</td><td>285.50 (n/a)</td><td>658.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (-14.41%)</td><td>0.05 (-1.03%)</td><td>0.04 (-11.74%)</td><td>0.01 (+2.77%)</td><td>0.03 (-7.20%)</td><td>1841.20 (-2.70%)</td><td>688.98 (-0.59%)</td><td>466.60 (+13.31%)</td><td>248.80 (+16.81%)</td><td>659.56 (-3.13%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1892.20 (n/a)</td><td>693.06 (n/a)</td><td>411.80 (n/a)</td><td>213.00 (n/a)</td><td>680.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(+22.19%)</b></td><td>0.09 <b>(+53.20%)</b></td><td>0.09 <b>(+65.76%)</b></td><td>0.07 <b>(+80.61%)</b></td><td>0.01 <b>(-25.52%)</b></td><td>306.10 <b>(-44.63%)</b></td><td>250.00 <b>(-37.25%)</b></td><td>242.90 <b>(-39.68%)</b></td><td>221.90 (-18.15%)</td><td>34.67 <b>(-66.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>552.80 (n/a)</td><td>398.40 (n/a)</td><td>402.70 (n/a)</td><td>271.10 (n/a)</td><td>102.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (-19.49%)</td><td>0.06 <b>(-24.96%)</b></td><td>0.07 (-9.65%)</td><td>0.03 <b>(-55.94%)</b></td><td>0.03 <b>(+59.36%)</b></td><td>721.30 <b>(+126.97%)</b></td><td>421.44 <b>(+62.09%)</b></td><td>302.50 (+10.68%)</td><td>228.60 <b>(+24.24%)</b></td><td>232.49 <b>(+353.53%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>317.80 (n/a)</td><td>260.00 (n/a)</td><td>273.30 (n/a)</td><td>184.00 (n/a)</td><td>51.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+1.74%)</td><td>0.05 (+0.73%)</td><td>0.04 (-13.33%)</td><td>0.03 <b>(+111.97%)</b></td><td>0.02 <b>(-26.52%)</b></td><td>649.80 <b>(-52.82%)</b></td><td>489.40 (-19.80%)</td><td>496.30 (+15.36%)</td><td>285.00 (-1.72%)</td><td>131.89 <b>(-70.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1377.30 (n/a)</td><td>610.26 (n/a)</td><td>430.20 (n/a)</td><td>290.00 (n/a)</td><td>442.49 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.50 (n/a)</td><td>337.70 (n/a)</td><td>314.70 (n/a)</td><td>242.80 (n/a)</td><td>113.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1797.40 (n/a)</td><td>721.34 (n/a)</td><td>590.20 (n/a)</td><td>247.00 (n/a)</td><td>622.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>445.00 (n/a)</td><td>493.50 (n/a)</td><td>271.30 (n/a)</td><td>127.56 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.70 (n/a)</td><td>449.10 (n/a)</td><td>496.50 (n/a)</td><td>284.10 (n/a)</td><td>95.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1886.40 (n/a)</td><td>781.88 (n/a)</td><td>590.80 (n/a)</td><td>220.80 (n/a)</td><td>641.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>647.00 (n/a)</td><td>478.52 (n/a)</td><td>521.40 (n/a)</td><td>223.90 (n/a)</td><td>158.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>641.60 (n/a)</td><td>357.60 (n/a)</td><td>258.90 (n/a)</td><td>235.40 (n/a)</td><td>173.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>585.00 (n/a)</td><td>464.64 (n/a)</td><td>519.10 (n/a)</td><td>234.60 (n/a)</td><td>144.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>753.80 (n/a)</td><td>573.08 (n/a)</td><td>545.30 (n/a)</td><td>395.00 (n/a)</td><td>132.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 <b>(-23.85%)</b></td><td>0.12 <b>(-28.36%)</b></td><td>0.11 <b>(-45.39%)</b></td><td>0.08 (-9.27%)</td><td>0.04 <b>(-33.74%)</b></td><td>601.10 (+10.21%)</td><td>449.12 <b>(+34.31%)</b></td><td>459.90 <b>(+83.15%)</b></td><td>301.10 <b>(+31.31%)</b></td><td>131.19 (-3.53%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>545.40 (n/a)</td><td>334.38 (n/a)</td><td>251.10 (n/a)</td><td>229.30 (n/a)</td><td>135.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2062.60 (n/a)</td><td>705.42 (n/a)</td><td>415.70 (n/a)</td><td>200.50 (n/a)</td><td>767.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>682.70 (n/a)</td><td>492.54 (n/a)</td><td>551.10 (n/a)</td><td>191.00 (n/a)</td><td>186.07 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>363.30 (n/a)</td><td>305.30 (n/a)</td><td>291.60 (n/a)</td><td>271.50 (n/a)</td><td>38.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2461.10 (n/a)</td><td>847.54 (n/a)</td><td>513.00 (n/a)</td><td>283.90 (n/a)</td><td>907.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.90 (n/a)</td><td>503.44 (n/a)</td><td>538.90 (n/a)</td><td>297.10 (n/a)</td><td>117.83 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.50 (n/a)</td><td>359.30 (n/a)</td><td>261.80 (n/a)</td><td>245.50 (n/a)</td><td>144.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1898.80 (n/a)</td><td>700.56 (n/a)</td><td>519.00 (n/a)</td><td>241.40 (n/a)</td><td>688.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1887.40 (n/a)</td><td>704.82 (n/a)</td><td>487.40 (n/a)</td><td>191.30 (n/a)</td><td>673.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1917.00 (n/a)</td><td>679.38 (n/a)</td><td>356.70 (n/a)</td><td>246.10 (n/a)</td><td>707.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>612.70 (n/a)</td><td>360.94 (n/a)</td><td>296.80 (n/a)</td><td>203.10 (n/a)</td><td>156.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>555.90 (n/a)</td><td>401.14 (n/a)</td><td>367.30 (n/a)</td><td>180.50 (n/a)</td><td>152.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>650.30 (n/a)</td><td>384.10 (n/a)</td><td>297.20 (n/a)</td><td>222.70 (n/a)</td><td>182.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1865.60 (n/a)</td><td>734.78 (n/a)</td><td>554.30 (n/a)</td><td>293.70 (n/a)</td><td>646.43 (n/a)</td>
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


### test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.31 (+4.59%)</td><td>2.78 <b>(-27.07%)</b></td><td>2.36 <b>(-42.03%)</b></td><td>1.76 <b>(-35.86%)</b></td><td>1.02 <b>(+70.50%)</b></td><td>5960.20 <b>(+55.90%)</b></td><td>4164.16 <b>(+47.68%)</b></td><td>4439.50 <b>(+72.49%)</b></td><td>2435.10 (-4.39%)</td><td>1385.87 <b>(+147.02%)</b></td><td>1763.74 (+4.59%)</td><td>1139.37 <b>(-27.07%)</b></td><td>967.45 <b>(-42.03%)</b></td><td>720.61 <b>(-35.86%)</b></td><td>418.52 <b>(+70.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.12 (n/a)</td><td>3.81 (n/a)</td><td>4.07 (n/a)</td><td>2.74 (n/a)</td><td>0.60 (n/a)</td><td>3823.00 (n/a)</td><td>2819.64 (n/a)</td><td>2573.80 (n/a)</td><td>2546.90 (n/a)</td><td>561.05 (n/a)</td><td>1686.36 (n/a)</td><td>1562.30 (n/a)</td><td>1668.74 (n/a)</td><td>1123.45 (n/a)</td><td>245.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.87 (+1.31%)</td><td>3.32 (-9.88%)</td><td>3.29 (-11.00%)</td><td>2.72 <b>(-24.19%)</b></td><td>0.48 <b>(+414.78%)</b></td><td>8681.80 <b>(+31.91%)</b></td><td>7226.16 (+12.81%)</td><td>7166.40 (+12.36%)</td><td>6089.90 (-1.29%)</td><td>1063.63 <b>(+564.88%)</b></td><td>2203.94 (+1.31%)</td><td>1889.29 (-9.88%)</td><td>1872.89 (-11.00%)</td><td>1545.97 <b>(-24.19%)</b></td><td>272.21 <b>(+414.78%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.82 (n/a)</td><td>3.68 (n/a)</td><td>3.70 (n/a)</td><td>3.58 (n/a)</td><td>0.09 (n/a)</td><td>6581.80 (n/a)</td><td>6405.68 (n/a)</td><td>6378.00 (n/a)</td><td>6169.40 (n/a)</td><td>159.97 (n/a)</td><td>2175.53 (n/a)</td><td>2096.35 (n/a)</td><td>2104.40 (n/a)</td><td>2039.22 (n/a)</td><td>52.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.05 (-0.96%)</td><td>3.19 (-6.83%)</td><td>3.12 (-18.32%)</td><td>2.48 (+4.20%)</td><td>0.72 (+0.69%)</td><td>6777.00 (-4.03%)</td><td>5487.16 (+7.35%)</td><td>5378.70 <b>(+22.43%)</b></td><td>4139.00 (+0.97%)</td><td>1231.31 (-0.44%)</td><td>2075.35 (-0.96%)</td><td>1631.30 (-6.83%)</td><td>1597.03 (-18.32%)</td><td>1267.51 (+4.20%)</td><td>369.10 (+0.69%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.09 (n/a)</td><td>3.42 (n/a)</td><td>3.82 (n/a)</td><td>2.38 (n/a)</td><td>0.72 (n/a)</td><td>7061.50 (n/a)</td><td>5111.52 (n/a)</td><td>4393.20 (n/a)</td><td>4099.20 (n/a)</td><td>1236.75 (n/a)</td><td>2095.53 (n/a)</td><td>1750.86 (n/a)</td><td>1955.29 (n/a)</td><td>1216.45 (n/a)</td><td>366.58 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.97 (+1.18%)</td><td>0.70 (-3.44%)</td><td>0.80 (+18.74%)</td><td>0.25 <b>(-55.22%)</b></td><td>0.28 <b>(+57.52%)</b></td><td>1830.60 <b>(+123.33%)</b></td><td>833.74 <b>(+24.90%)</b></td><td>576.90 (-15.78%)</td><td>473.30 (-1.17%)</td><td>566.19 <b>(+264.81%)</b></td><td>70.90 (+1.18%)</td><td>50.85 (-3.44%)</td><td>58.16 (+18.74%)</td><td>18.33 <b>(-55.22%)</b></td><td>20.42 <b>(+57.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.96 (n/a)</td><td>0.72 (n/a)</td><td>0.67 (n/a)</td><td>0.56 (n/a)</td><td>0.18 (n/a)</td><td>819.70 (n/a)</td><td>667.50 (n/a)</td><td>685.00 (n/a)</td><td>478.90 (n/a)</td><td>155.20 (n/a)</td><td>70.07 (n/a)</td><td>52.66 (n/a)</td><td>48.98 (n/a)</td><td>40.94 (n/a)</td><td>12.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.74 <b>(+30.32%)</b></td><td>1.27 (+19.72%)</td><td>1.18 (+9.83%)</td><td>0.96 <b>(+20.58%)</b></td><td>0.33 <b>(+50.02%)</b></td><td>683.90 (-17.06%)</td><td>541.44 (-15.20%)</td><td>556.30 (-8.94%)</td><td>377.50 <b>(-23.27%)</b></td><td>130.34 (-4.01%)</td><td>177.76 <b>(+30.32%)</b></td><td>130.35 (+19.72%)</td><td>120.64 (+9.83%)</td><td>98.13 <b>(+20.58%)</b></td><td>33.62 <b>(+50.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.33 (n/a)</td><td>1.06 (n/a)</td><td>1.07 (n/a)</td><td>0.79 (n/a)</td><td>0.22 (n/a)</td><td>824.60 (n/a)</td><td>638.50 (n/a)</td><td>610.90 (n/a)</td><td>492.00 (n/a)</td><td>135.78 (n/a)</td><td>136.40 (n/a)</td><td>108.88 (n/a)</td><td>109.85 (n/a)</td><td>81.38 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.70 (+6.14%)</td><td>0.92 (+8.98%)</td><td>0.92 <b>(+23.92%)</b></td><td>0.22 (-3.73%)</td><td>0.67 (+15.52%)</td><td>3469.30 (+3.87%)</td><td>1528.84 (+5.32%)</td><td>822.00 (-19.30%)</td><td>442.40 (-5.77%)</td><td>1344.92 (+13.75%)</td><td>189.63 (+6.14%)</td><td>102.93 (+8.98%)</td><td>102.05 <b>(+23.92%)</b></td><td>24.18 (-3.73%)</td><td>74.23 (+15.52%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.61 (n/a)</td><td>0.85 (n/a)</td><td>0.74 (n/a)</td><td>0.23 (n/a)</td><td>0.58 (n/a)</td><td>3340.00 (n/a)</td><td>1451.64 (n/a)</td><td>1018.60 (n/a)</td><td>469.50 (n/a)</td><td>1182.34 (n/a)</td><td>178.67 (n/a)</td><td>94.44 (n/a)</td><td>82.35 (n/a)</td><td>25.12 (n/a)</td><td>64.26 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.39 (-7.57%)</td><td>1.03 (-7.78%)</td><td>1.16 (-3.78%)</td><td>0.31 <b>(-36.63%)</b></td><td>0.42 (+9.63%)</td><td>3353.00 <b>(+57.81%)</b></td><td>1366.40 <b>(+25.39%)</b></td><td>906.30 (+3.93%)</td><td>754.20 (+8.19%)</td><td>1112.56 <b>(+90.05%)</b></td><td>177.96 (-7.57%)</td><td>132.27 (-7.78%)</td><td>148.09 (-3.78%)</td><td>40.03 <b>(-36.63%)</b></td><td>53.20 (+9.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.50 (n/a)</td><td>1.12 (n/a)</td><td>1.20 (n/a)</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>2124.70 (n/a)</td><td>1089.72 (n/a)</td><td>872.00 (n/a)</td><td>697.10 (n/a)</td><td>585.42 (n/a)</td><td>192.53 (n/a)</td><td>143.43 (n/a)</td><td>153.91 (n/a)</td><td>63.17 (n/a)</td><td>48.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.90 (+6.87%)</td><td>1.60 <b>(+28.05%)</b></td><td>1.65 <b>(+26.58%)</b></td><td>1.28 <b>(+122.48%)</b></td><td>0.29 <b>(-38.14%)</b></td><td>822.20 <b>(-55.05%)</b></td><td>671.64 <b>(-31.26%)</b></td><td>634.90 <b>(-21.00%)</b></td><td>550.60 (-6.42%)</td><td>123.77 <b>(-75.14%)</b></td><td>243.77 (+6.87%)</td><td>205.21 <b>(+28.05%)</b></td><td>211.40 <b>(+26.58%)</b></td><td>163.25 <b>(+122.48%)</b></td><td>36.56 <b>(-38.14%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.78 (n/a)</td><td>1.25 (n/a)</td><td>1.30 (n/a)</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>1829.20 (n/a)</td><td>977.10 (n/a)</td><td>803.70 (n/a)</td><td>588.40 (n/a)</td><td>497.94 (n/a)</td><td>228.10 (n/a)</td><td>160.26 (n/a)</td><td>167.01 (n/a)</td><td>73.38 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.91 (-1.11%)</td><td>1.32 (-4.03%)</td><td>1.20 (-13.30%)</td><td>1.03 <b>(+62.19%)</b></td><td>0.35 <b>(-27.02%)</b></td><td>1017.50 <b>(-38.34%)</b></td><td>829.26 (-5.47%)</td><td>871.70 (+15.33%)</td><td>547.90 (+1.13%)</td><td>177.67 <b>(-59.80%)</b></td><td>244.98 (-1.11%)</td><td>169.36 (-4.03%)</td><td>153.97 (-13.30%)</td><td>131.91 <b>(+62.19%)</b></td><td>44.47 <b>(-27.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.94 (n/a)</td><td>1.38 (n/a)</td><td>1.39 (n/a)</td><td>0.64 (n/a)</td><td>0.48 (n/a)</td><td>1650.20 (n/a)</td><td>877.28 (n/a)</td><td>755.80 (n/a)</td><td>541.80 (n/a)</td><td>441.99 (n/a)</td><td>247.73 (n/a)</td><td>176.47 (n/a)</td><td>177.59 (n/a)</td><td>81.33 (n/a)</td><td>60.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.63 (-1.41%)</td><td>1.28 (-11.64%)</td><td>1.21 <b>(-21.49%)</b></td><td>0.98 (-17.90%)</td><td>0.24 <b>(+21.03%)</b></td><td>1074.10 <b>(+21.81%)</b></td><td>840.14 (+14.60%)</td><td>863.80 <b>(+27.39%)</b></td><td>643.40 (+1.42%)</td><td>160.05 <b>(+49.10%)</b></td><td>208.60 (-1.41%)</td><td>164.43 (-11.64%)</td><td>155.39 <b>(-21.49%)</b></td><td>124.96 (-17.90%)</td><td>31.14 <b>(+21.03%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.65 (n/a)</td><td>1.45 (n/a)</td><td>1.55 (n/a)</td><td>1.19 (n/a)</td><td>0.20 (n/a)</td><td>881.80 (n/a)</td><td>733.08 (n/a)</td><td>678.10 (n/a)</td><td>634.40 (n/a)</td><td>107.35 (n/a)</td><td>211.58 (n/a)</td><td>186.09 (n/a)</td><td>197.92 (n/a)</td><td>152.21 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.68 (+3.36%)</td><td>1.40 (+11.03%)</td><td>1.39 (-4.96%)</td><td>1.07 <b>(+124.23%)</b></td><td>0.26 <b>(-44.01%)</b></td><td>978.20 <b>(-55.40%)</b></td><td>773.60 <b>(-24.59%)</b></td><td>755.90 (+5.22%)</td><td>622.70 (-3.26%)</td><td>150.38 <b>(-77.22%)</b></td><td>215.54 (+3.36%)</td><td>178.70 (+11.03%)</td><td>177.56 (-4.96%)</td><td>137.21 <b>(+124.23%)</b></td><td>33.67 <b>(-44.01%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.63 (n/a)</td><td>1.26 (n/a)</td><td>1.46 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>2193.40 (n/a)</td><td>1025.88 (n/a)</td><td>718.40 (n/a)</td><td>643.70 (n/a)</td><td>660.11 (n/a)</td><td>208.53 (n/a)</td><td>160.95 (n/a)</td><td>186.84 (n/a)</td><td>61.19 (n/a)</td><td>60.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.79 <b>(+21.55%)</b></td><td>1.28 (+2.39%)</td><td>1.23 (+1.57%)</td><td>0.53 <b>(-54.67%)</b></td><td>0.52 <b>(+300.76%)</b></td><td>1994.00 <b>(+120.62%)</b></td><td>993.68 (+17.75%)</td><td>852.00 (-1.54%)</td><td>585.70 (-17.73%)</td><td>579.70 <b>(+636.60%)</b></td><td>229.16 <b>(+21.55%)</b></td><td>164.12 (+2.39%)</td><td>157.54 (+1.57%)</td><td>67.31 <b>(-54.67%)</b></td><td>66.22 <b>(+300.76%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.47 (n/a)</td><td>1.25 (n/a)</td><td>1.21 (n/a)</td><td>1.16 (n/a)</td><td>0.13 (n/a)</td><td>903.80 (n/a)</td><td>843.86 (n/a)</td><td>865.30 (n/a)</td><td>711.90 (n/a)</td><td>78.70 (n/a)</td><td>188.54 (n/a)</td><td>160.28 (n/a)</td><td>155.11 (n/a)</td><td>148.50 (n/a)</td><td>16.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.64 <b>(-23.78%)</b></td><td>0.45 <b>(-23.76%)</b></td><td>0.47 (-12.93%)</td><td>0.15 <b>(-62.72%)</b></td><td>0.18 (-1.51%)</td><td>2452.30 <b>(+168.25%)</b></td><td>1054.62 <b>(+58.32%)</b></td><td>761.80 (+14.83%)</td><td>558.90 <b>(+31.20%)</b></td><td>787.14 <b>(+288.55%)</b></td><td>30.02 <b>(-23.78%)</b></td><td>20.79 <b>(-23.76%)</b></td><td>22.02 (-12.93%)</td><td>6.84 <b>(-62.72%)</b></td><td>8.58 (-1.51%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.85 (n/a)</td><td>0.59 (n/a)</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>914.20 (n/a)</td><td>666.12 (n/a)</td><td>663.40 (n/a)</td><td>426.00 (n/a)</td><td>202.58 (n/a)</td><td>39.38 (n/a)</td><td>27.26 (n/a)</td><td>25.29 (n/a)</td><td>18.35 (n/a)</td><td>8.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.93 (-1.51%)</td><td>2.06 (-7.62%)</td><td>1.65 <b>(-35.30%)</b></td><td>1.49 (+8.94%)</td><td>0.67 (-3.89%)</td><td>2810.40 (-8.20%)</td><td>2203.44 (+6.85%)</td><td>2548.60 <b>(+54.57%)</b></td><td>1432.90 (+1.53%)</td><td>641.84 (-11.87%)</td><td>749.33 (-1.51%)</td><td>527.19 (-7.62%)</td><td>421.31 <b>(-35.30%)</b></td><td>382.06 (+8.94%)</td><td>171.89 (-3.89%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.97 (n/a)</td><td>2.23 (n/a)</td><td>2.54 (n/a)</td><td>1.37 (n/a)</td><td>0.70 (n/a)</td><td>3061.60 (n/a)</td><td>2062.16 (n/a)</td><td>1648.80 (n/a)</td><td>1411.30 (n/a)</td><td>728.27 (n/a)</td><td>760.81 (n/a)</td><td>570.68 (n/a)</td><td>651.21 (n/a)</td><td>350.72 (n/a)</td><td>178.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.52 (-10.88%)</td><td>2.10 <b>(-33.36%)</b></td><td>2.34 <b>(-33.44%)</b></td><td>0.79 <b>(-27.72%)</b></td><td>1.09 (-8.67%)</td><td>3337.10 <b>(+38.34%)</b></td><td>1656.72 <b>(+56.56%)</b></td><td>1121.30 <b>(+50.25%)</b></td><td>745.60 (+12.20%)</td><td>1063.20 <b>(+40.06%)</b></td><td>720.04 (-10.88%)</td><td>429.85 <b>(-33.36%)</b></td><td>478.79 <b>(-33.44%)</b></td><td>160.88 <b>(-27.72%)</b></td><td>222.38 (-8.67%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.94 (n/a)</td><td>3.15 (n/a)</td><td>3.51 (n/a)</td><td>1.09 (n/a)</td><td>1.19 (n/a)</td><td>2412.20 (n/a)</td><td>1058.22 (n/a)</td><td>746.30 (n/a)</td><td>664.50 (n/a)</td><td>759.12 (n/a)</td><td>807.92 (n/a)</td><td>645.08 (n/a)</td><td>719.36 (n/a)</td><td>222.56 (n/a)</td><td>243.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.38 (+7.22%)</td><td>2.68 (+9.65%)</td><td>2.64 <b>(+29.08%)</b></td><td>2.28 (+12.61%)</td><td>0.43 <b>(-23.92%)</b></td><td>3448.70 (-11.19%)</td><td>2991.60 (-10.71%)</td><td>2977.90 <b>(-22.53%)</b></td><td>2328.20 (-6.73%)</td><td>429.96 <b>(-39.12%)</b></td><td>1037.67 (+7.22%)</td><td>822.54 (+9.65%)</td><td>811.29 <b>(+29.08%)</b></td><td>700.54 (+12.61%)</td><td>131.18 <b>(-23.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.15 (n/a)</td><td>2.44 (n/a)</td><td>2.05 (n/a)</td><td>2.03 (n/a)</td><td>0.56 (n/a)</td><td>3883.40 (n/a)</td><td>3350.28 (n/a)</td><td>3843.80 (n/a)</td><td>2496.30 (n/a)</td><td>706.22 (n/a)</td><td>967.78 (n/a)</td><td>750.16 (n/a)</td><td>628.52 (n/a)</td><td>622.12 (n/a)</td><td>172.41 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma16]

_No metrics available._


### test_gemm_tile_options[tn128-ma32]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma16]

_No metrics available._


### test_gemm_tile_options[tn16-ma32]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma16]

_No metrics available._


### test_gemm_tile_options[tn32-ma32]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32]

_No metrics available._


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.90 (n/a)</td><td>347.80 (n/a)</td><td>297.50 (n/a)</td><td>277.20 (n/a)</td><td>124.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.10 (n/a)</td><td>420.06 (n/a)</td><td>331.20 (n/a)</td><td>295.70 (n/a)</td><td>154.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>621.70 (n/a)</td><td>402.48 (n/a)</td><td>414.90 (n/a)</td><td>229.60 (n/a)</td><td>155.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.60 (n/a)</td><td>403.28 (n/a)</td><td>300.40 (n/a)</td><td>245.50 (n/a)</td><td>182.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.80 (n/a)</td><td>479.16 (n/a)</td><td>537.40 (n/a)</td><td>241.00 (n/a)</td><td>135.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.50 (n/a)</td><td>366.66 (n/a)</td><td>343.30 (n/a)</td><td>254.70 (n/a)</td><td>96.31 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.00 (n/a)</td><td>359.86 (n/a)</td><td>319.50 (n/a)</td><td>273.20 (n/a)</td><td>100.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.00 (n/a)</td><td>372.24 (n/a)</td><td>414.10 (n/a)</td><td>222.60 (n/a)</td><td>129.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.80 (n/a)</td><td>389.40 (n/a)</td><td>295.10 (n/a)</td><td>201.30 (n/a)</td><td>202.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.40 (n/a)</td><td>378.56 (n/a)</td><td>339.20 (n/a)</td><td>267.40 (n/a)</td><td>96.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.90 (n/a)</td><td>428.00 (n/a)</td><td>485.10 (n/a)</td><td>223.10 (n/a)</td><td>170.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.90 (n/a)</td><td>504.74 (n/a)</td><td>507.80 (n/a)</td><td>398.10 (n/a)</td><td>85.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>636.90 (n/a)</td><td>475.16 (n/a)</td><td>507.50 (n/a)</td><td>286.10 (n/a)</td><td>128.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.70 (n/a)</td><td>436.52 (n/a)</td><td>464.20 (n/a)</td><td>258.40 (n/a)</td><td>152.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>545.70 (n/a)</td><td>392.12 (n/a)</td><td>365.00 (n/a)</td><td>273.30 (n/a)</td><td>100.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.40 (n/a)</td><td>487.06 (n/a)</td><td>546.30 (n/a)</td><td>208.10 (n/a)</td><td>162.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>501.20 (n/a)</td><td>359.16 (n/a)</td><td>376.50 (n/a)</td><td>237.20 (n/a)</td><td>106.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>602.60 (n/a)</td><td>452.38 (n/a)</td><td>436.10 (n/a)</td><td>292.60 (n/a)</td><td>130.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>669.20 (n/a)</td><td>475.62 (n/a)</td><td>421.30 (n/a)</td><td>307.40 (n/a)</td><td>180.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.70 (n/a)</td><td>486.68 (n/a)</td><td>556.70 (n/a)</td><td>270.90 (n/a)</td><td>159.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>566.40 (n/a)</td><td>425.94 (n/a)</td><td>397.50 (n/a)</td><td>312.00 (n/a)</td><td>111.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>536.00 (n/a)</td><td>420.66 (n/a)</td><td>488.70 (n/a)</td><td>275.40 (n/a)</td><td>126.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.70 (n/a)</td><td>402.40 (n/a)</td><td>442.70 (n/a)</td><td>240.70 (n/a)</td><td>123.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>537.90 (n/a)</td><td>408.46 (n/a)</td><td>461.00 (n/a)</td><td>218.60 (n/a)</td><td>130.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (-4.68%)</td><td>0.35 <b>(-28.97%)</b></td><td>0.43 (-17.02%)</td><td>0.09 <b>(-79.39%)</b></td><td>0.16 <b>(+281.31%)</b></td><td>2437.40 <b>(+385.05%)</b></td><td>938.34 <b>(+105.46%)</b></td><td>518.90 <b>(+20.51%)</b></td><td>440.90 (+4.90%)</td><td>847.64 <b>(+1953.77%)</b></td><td>21.40 (-4.68%)</td><td>14.77 <b>(-28.97%)</b></td><td>18.19 (-17.02%)</td><td>3.87 <b>(-79.39%)</b></td><td>6.96 <b>(+281.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.53 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.04 (n/a)</td><td>502.50 (n/a)</td><td>456.70 (n/a)</td><td>430.60 (n/a)</td><td>420.30 (n/a)</td><td>41.27 (n/a)</td><td>22.46 (n/a)</td><td>20.80 (n/a)</td><td>21.92 (n/a)</td><td>18.78 (n/a)</td><td>1.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.63 (+0.45%)</td><td>0.41 (-14.41%)</td><td>0.50 (+11.49%)</td><td>0.12 <b>(-69.04%)</b></td><td>0.21 <b>(+97.56%)</b></td><td>1844.40 <b>(+223.01%)</b></td><td>769.70 <b>(+61.61%)</b></td><td>443.10 (-10.30%)</td><td>352.00 (-0.45%)</td><td>625.36 <b>(+538.95%)</b></td><td>26.81 (+0.45%)</td><td>17.59 (-14.41%)</td><td>21.30 (+11.49%)</td><td>5.12 <b>(-69.04%)</b></td><td>8.88 <b>(+97.56%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.11 (n/a)</td><td>571.00 (n/a)</td><td>476.26 (n/a)</td><td>494.00 (n/a)</td><td>353.60 (n/a)</td><td>97.87 (n/a)</td><td>26.69 (n/a)</td><td>20.55 (n/a)</td><td>19.10 (n/a)</td><td>16.53 (n/a)</td><td>4.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.31 (+1.40%)</td><td>0.30 (+0.19%)</td><td>0.30 (+0.02%)</td><td>0.30 (-0.52%)</td><td>0.01 <b>(+49.93%)</b></td><td>84528.40 (+0.52%)</td><td>82857.14 (-0.17%)</td><td>83264.10 (-0.02%)</td><td>80278.90 (-1.38%)</td><td>1687.29 <b>(+48.41%)</b></td><td>214.00 (+1.40%)</td><td>207.41 (+0.19%)</td><td>206.33 (+0.02%)</td><td>203.24 (-0.52%)</td><td>4.28 <b>(+49.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84090.70 (n/a)</td><td>82995.22 (n/a)</td><td>83276.80 (n/a)</td><td>81400.40 (n/a)</td><td>1136.93 (n/a)</td><td>211.05 (n/a)</td><td>207.03 (n/a)</td><td>206.30 (n/a)</td><td>204.30 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.15 (+1.70%)</td><td>1.13 (+3.93%)</td><td>1.15 (+4.35%)</td><td>1.08 (+6.37%)</td><td>0.03 <b>(-39.78%)</b></td><td>23229.70 (-5.98%)</td><td>22269.32 (-3.88%)</td><td>21964.50 (-4.17%)</td><td>21874.30 (-1.67%)</td><td>579.73 <b>(-44.17%)</b></td><td>785.39 (+1.70%)</td><td>771.87 (+3.93%)</td><td>782.17 (+4.35%)</td><td>739.56 (+6.37%)</td><td>19.62 <b>(-39.78%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.13 (n/a)</td><td>1.09 (n/a)</td><td>1.10 (n/a)</td><td>1.02 (n/a)</td><td>0.05 (n/a)</td><td>24708.40 (n/a)</td><td>23168.98 (n/a)</td><td>22919.30 (n/a)</td><td>22245.10 (n/a)</td><td>1038.39 (n/a)</td><td>772.30 (n/a)</td><td>742.67 (n/a)</td><td>749.58 (n/a)</td><td>695.31 (n/a)</td><td>32.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.80 (-0.77%)</td><td>0.79 (-0.46%)</td><td>0.79 (-1.16%)</td><td>0.78 (+0.56%)</td><td>0.01 <b>(-36.00%)</b></td><td>96236.70 (-0.56%)</td><td>95403.18 (+0.46%)</td><td>95835.60 (+1.17%)</td><td>94362.30 (+0.78%)</td><td>833.76 <b>(-35.88%)</b></td><td>728.25 (-0.77%)</td><td>720.35 (-0.46%)</td><td>717.06 (-1.16%)</td><td>714.07 (+0.56%)</td><td>6.31 <b>(-36.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96780.20 (n/a)</td><td>94969.30 (n/a)</td><td>94727.40 (n/a)</td><td>93635.00 (n/a)</td><td>1300.23 (n/a)</td><td>733.91 (n/a)</td><td>723.70 (n/a)</td><td>725.44 (n/a)</td><td>710.06 (n/a)</td><td>9.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.77 (-1.47%)</td><td>0.76 (+0.26%)</td><td>0.76 (-0.88%)</td><td>0.76 (+3.09%)</td><td>0.00 <b>(-76.80%)</b></td><td>99623.10 (-3.00%)</td><td>98793.76 (-0.31%)</td><td>98714.60 (+0.88%)</td><td>98142.50 (+1.49%)</td><td>576.15 <b>(-77.16%)</b></td><td>700.20 (-1.47%)</td><td>695.60 (+0.26%)</td><td>696.14 (-0.88%)</td><td>689.79 (+3.09%)</td><td>4.05 <b>(-76.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102705.60 (n/a)</td><td>99098.36 (n/a)</td><td>97850.40 (n/a)</td><td>96699.00 (n/a)</td><td>2522.96 (n/a)</td><td>710.65 (n/a)</td><td>693.80 (n/a)</td><td>702.29 (n/a)</td><td>669.09 (n/a)</td><td>17.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.89 (-0.46%)</td><td>0.89 (-0.04%)</td><td>0.89 (+0.18%)</td><td>0.88 (+0.34%)</td><td>0.01 <b>(-33.07%)</b></td><td>85756.10 (-0.33%)</td><td>85031.92 (+0.04%)</td><td>84844.40 (-0.18%)</td><td>84434.90 (+0.46%)</td><td>516.75 <b>(-32.96%)</b></td><td>813.88 (-0.46%)</td><td>808.18 (-0.04%)</td><td>809.95 (+0.18%)</td><td>801.34 (+0.34%)</td><td>4.90 <b>(-33.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>86043.90 (n/a)</td><td>85001.58 (n/a)</td><td>85001.20 (n/a)</td><td>84047.50 (n/a)</td><td>770.79 (n/a)</td><td>817.63 (n/a)</td><td>808.50 (n/a)</td><td>808.45 (n/a)</td><td>798.66 (n/a)</td><td>7.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.50 (+11.56%)</td><td>3.28 (+1.21%)</td><td>2.30 (-18.17%)</td><td>2.14 (-2.29%)</td><td>1.53 <b>(+26.70%)</b></td><td>4167.70 (+2.34%)</td><td>3167.64 (+3.72%)</td><td>3883.30 <b>(+22.21%)</b></td><td>1619.40 (-10.36%)</td><td>1217.56 (+17.86%)</td><td>331.52 (+11.56%)</td><td>197.56 (+1.21%)</td><td>138.25 (-18.17%)</td><td>128.82 (-2.29%)</td><td>92.46 <b>(+26.70%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.93 (n/a)</td><td>3.24 (n/a)</td><td>2.80 (n/a)</td><td>2.19 (n/a)</td><td>1.21 (n/a)</td><td>4072.30 (n/a)</td><td>3054.02 (n/a)</td><td>3177.50 (n/a)</td><td>1806.60 (n/a)</td><td>1033.04 (n/a)</td><td>297.17 (n/a)</td><td>195.19 (n/a)</td><td>168.96 (n/a)</td><td>131.83 (n/a)</td><td>72.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.17 <b>(+24.48%)</b></td><td>3.65 <b>(+25.99%)</b></td><td>4.32 <b>(+51.11%)</b></td><td>2.19 (+6.10%)</td><td>1.38 <b>(+75.89%)</b></td><td>4075.70 (-5.75%)</td><td>2794.54 (-13.87%)</td><td>2065.40 <b>(-33.82%)</b></td><td>1722.50 (-19.67%)</td><td>1177.05 <b>(+47.77%)</b></td><td>311.68 <b>(+24.48%)</b></td><td>219.81 <b>(+25.99%)</b></td><td>259.94 <b>(+51.11%)</b></td><td>131.73 (+6.10%)</td><td>82.94 <b>(+75.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.16 (n/a)</td><td>2.90 (n/a)</td><td>2.86 (n/a)</td><td>2.06 (n/a)</td><td>0.78 (n/a)</td><td>4324.20 (n/a)</td><td>3244.38 (n/a)</td><td>3121.10 (n/a)</td><td>2144.20 (n/a)</td><td>796.52 (n/a)</td><td>250.38 (n/a)</td><td>174.47 (n/a)</td><td>172.01 (n/a)</td><td>124.15 (n/a)</td><td>47.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.82 (+2.66%)</td><td>4.46 (+14.15%)</td><td>4.47 (+19.66%)</td><td>2.18 (+3.89%)</td><td>1.47 (-8.02%)</td><td>4084.20 (-3.75%)</td><td>2264.94 (-14.36%)</td><td>1992.50 (-16.43%)</td><td>1530.50 (-2.59%)</td><td>1050.99 (-8.50%)</td><td>350.78 (+2.66%)</td><td>268.70 (+14.15%)</td><td>269.45 (+19.66%)</td><td>131.45 (+3.89%)</td><td>88.37 (-8.02%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.67 (n/a)</td><td>3.91 (n/a)</td><td>3.74 (n/a)</td><td>2.10 (n/a)</td><td>1.59 (n/a)</td><td>4243.30 (n/a)</td><td>2644.70 (n/a)</td><td>2384.20 (n/a)</td><td>1571.20 (n/a)</td><td>1148.65 (n/a)</td><td>341.69 (n/a)</td><td>235.39 (n/a)</td><td>225.18 (n/a)</td><td>126.52 (n/a)</td><td>96.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.38 (-5.06%)</td><td>5.40 (-4.09%)</td><td>5.84 (+2.99%)</td><td>4.38 (-4.37%)</td><td>0.89 (+3.06%)</td><td>7960.30 (+4.57%)</td><td>6604.70 (+4.65%)</td><td>5975.10 (-2.90%)</td><td>5468.30 (+5.33%)</td><td>1131.14 (+15.70%)</td><td>392.72 (-5.06%)</td><td>332.60 (-4.09%)</td><td>359.40 (+2.99%)</td><td>269.78 (-4.37%)</td><td>54.57 (+3.06%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.72 (n/a)</td><td>5.63 (n/a)</td><td>5.67 (n/a)</td><td>4.58 (n/a)</td><td>0.86 (n/a)</td><td>7612.70 (n/a)</td><td>6311.52 (n/a)</td><td>6153.50 (n/a)</td><td>5191.50 (n/a)</td><td>977.64 (n/a)</td><td>413.65 (n/a)</td><td>346.77 (n/a)</td><td>348.99 (n/a)</td><td>282.09 (n/a)</td><td>52.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.09 (+7.92%)</td><td>5.17 (+8.91%)</td><td>5.24 (+14.38%)</td><td>4.43 (+10.54%)</td><td>0.63 (+2.54%)</td><td>7867.10 (-9.54%)</td><td>6817.32 (-8.32%)</td><td>6649.60 (-12.57%)</td><td>5728.80 (-7.34%)</td><td>820.00 (-13.32%)</td><td>374.86 (+7.92%)</td><td>318.74 (+8.91%)</td><td>322.95 (+14.38%)</td><td>272.97 (+10.54%)</td><td>39.00 (+2.54%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.64 (n/a)</td><td>4.75 (n/a)</td><td>4.58 (n/a)</td><td>4.01 (n/a)</td><td>0.62 (n/a)</td><td>8696.30 (n/a)</td><td>7435.70 (n/a)</td><td>7605.60 (n/a)</td><td>6182.70 (n/a)</td><td>945.98 (n/a)</td><td>347.34 (n/a)</td><td>292.65 (n/a)</td><td>282.35 (n/a)</td><td>246.94 (n/a)</td><td>38.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.04 (+0.22%)</td><td>5.44 (+4.68%)</td><td>5.39 (+9.13%)</td><td>5.17 (+17.49%)</td><td>0.36 <b>(-46.27%)</b></td><td>6745.90 (-14.89%)</td><td>6427.46 (-5.39%)</td><td>6474.40 (-8.36%)</td><td>5768.80 (-0.22%)</td><td>396.74 <b>(-53.97%)</b></td><td>372.26 (+0.22%)</td><td>335.19 (+4.68%)</td><td>331.69 (+9.13%)</td><td>318.34 (+17.49%)</td><td>21.97 <b>(-46.27%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.03 (n/a)</td><td>5.20 (n/a)</td><td>4.93 (n/a)</td><td>4.40 (n/a)</td><td>0.66 (n/a)</td><td>7926.10 (n/a)</td><td>6793.98 (n/a)</td><td>7065.40 (n/a)</td><td>5781.30 (n/a)</td><td>862.02 (n/a)</td><td>371.45 (n/a)</td><td>320.22 (n/a)</td><td>303.94 (n/a)</td><td>270.94 (n/a)</td><td>40.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.79 (+1.78%)</td><td>0.78 (+2.76%)</td><td>0.77 (+3.03%)</td><td>0.76 (+2.39%)</td><td>0.01 (-14.76%)</td><td>99340.00 (-2.34%)</td><td>97354.32 (-2.70%)</td><td>97862.60 (-2.94%)</td><td>95661.10 (-1.74%)</td><td>1548.92 (-18.52%)</td><td>718.36 (+1.78%)</td><td>706.01 (+2.76%)</td><td>702.20 (+3.03%)</td><td>691.76 (+2.39%)</td><td>11.23 (-14.76%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101718.30 (n/a)</td><td>100051.90 (n/a)</td><td>100828.30 (n/a)</td><td>97359.70 (n/a)</td><td>1901.08 (n/a)</td><td>705.83 (n/a)</td><td>687.04 (n/a)</td><td>681.55 (n/a)</td><td>675.59 (n/a)</td><td>13.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.78 (+2.93%)</td><td>0.77 (+3.58%)</td><td>0.78 (+2.62%)</td><td>0.75 (+4.59%)</td><td>0.01 <b>(-31.41%)</b></td><td>100568.40 (-4.39%)</td><td>97941.86 (-3.49%)</td><td>97311.20 (-2.55%)</td><td>96564.10 (-2.85%)</td><td>1682.72 <b>(-36.17%)</b></td><td>711.65 (+2.93%)</td><td>701.80 (+3.58%)</td><td>706.18 (+2.62%)</td><td>683.31 (+4.59%)</td><td>11.92 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.76 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>105182.50 (n/a)</td><td>101480.32 (n/a)</td><td>99857.70 (n/a)</td><td>99397.90 (n/a)</td><td>2636.13 (n/a)</td><td>691.36 (n/a)</td><td>677.53 (n/a)</td><td>688.17 (n/a)</td><td>653.34 (n/a)</td><td>17.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.90 (+0.26%)</td><td>0.87 (-1.91%)</td><td>0.88 (-0.83%)</td><td>0.82 (-5.68%)</td><td>0.03 <b>(+206.22%)</b></td><td>92054.30 (+6.02%)</td><td>86950.58 (+2.04%)</td><td>85743.00 (+0.84%)</td><td>84210.80 (-0.25%)</td><td>3173.93 <b>(+224.34%)</b></td><td>816.04 (+0.26%)</td><td>791.15 (-1.91%)</td><td>801.46 (-0.83%)</td><td>746.51 (-5.68%)</td><td>28.08 <b>(+206.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86824.70 (n/a)</td><td>85211.06 (n/a)</td><td>85028.10 (n/a)</td><td>84425.80 (n/a)</td><td>978.59 (n/a)</td><td>813.96 (n/a)</td><td>806.55 (n/a)</td><td>808.20 (n/a)</td><td>791.47 (n/a)</td><td>9.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.67 (+2.89%)</td><td>2.32 (-8.51%)</td><td>2.35 (+1.82%)</td><td>1.06 <b>(-33.12%)</b></td><td>0.93 (-3.14%)</td><td>7639.40 <b>(+49.51%)</b></td><td>4079.00 (+14.29%)</td><td>3433.00 (-1.79%)</td><td>2198.20 (-2.81%)</td><td>2078.95 <b>(+56.90%)</b></td><td>961.65 (+2.89%)</td><td>609.35 (-8.51%)</td><td>615.76 (+1.82%)</td><td>276.71 <b>(-33.12%)</b></td><td>244.22 (-3.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.56 (n/a)</td><td>2.54 (n/a)</td><td>2.31 (n/a)</td><td>1.58 (n/a)</td><td>0.96 (n/a)</td><td>5109.60 (n/a)</td><td>3569.08 (n/a)</td><td>3495.40 (n/a)</td><td>2261.80 (n/a)</td><td>1324.98 (n/a)</td><td>934.63 (n/a)</td><td>666.00 (n/a)</td><td>604.77 (n/a)</td><td>413.72 (n/a)</td><td>252.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.33 <b>(+56.06%)</b></td><td>0.21 (+7.90%)</td><td>0.19 (-0.71%)</td><td>0.14 (-15.23%)</td><td>0.07 <b>(+292.25%)</b></td><td>8966.60 (+17.96%)</td><td>6448.22 (-0.54%)</td><td>6452.00 (+0.72%)</td><td>3770.80 <b>(-35.92%)</b></td><td>1847.87 <b>(+176.91%)</b></td><td>17.80 <b>(+56.06%)</b></td><td>11.26 (+7.90%)</td><td>10.40 (-0.71%)</td><td>7.48 (-15.23%)</td><td>3.87 <b>(+292.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7601.10 (n/a)</td><td>6483.00 (n/a)</td><td>6405.90 (n/a)</td><td>5884.60 (n/a)</td><td>667.33 (n/a)</td><td>11.40 (n/a)</td><td>10.43 (n/a)</td><td>10.48 (n/a)</td><td>8.83 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.95 (n/a)</td><td>3.79 (n/a)</td><td>3.82 (n/a)</td><td>3.48 (n/a)</td><td>0.19 (n/a)</td><td>3.95 (n/a)</td><td>3.79 (n/a)</td><td>3.81 (n/a)</td><td>3.48 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>7.56 (-0.38%)</td><td>6.87 (+3.33%)</td><td>7.24 (+4.78%)</td><td>5.96 (+4.83%)</td><td>0.76 (+0.97%)</td><td>7.55 (-0.38%)</td><td>6.87 (+3.33%)</td><td>7.24 (+4.78%)</td><td>5.96 (+4.83%)</td><td>0.76 (+0.97%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.59 (n/a)</td><td>6.65 (n/a)</td><td>6.91 (n/a)</td><td>5.69 (n/a)</td><td>0.75 (n/a)</td><td>7.58 (n/a)</td><td>6.65 (n/a)</td><td>6.90 (n/a)</td><td>5.68 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>12.38 (-11.95%)</td><td>8.86 <b>(-22.68%)</b></td><td>8.20 <b>(-39.50%)</b></td><td>6.98 (-5.10%)</td><td>2.21 <b>(-32.42%)</b></td><td>12.37 (-11.95%)</td><td>8.86 <b>(-22.68%)</b></td><td>8.19 <b>(-39.50%)</b></td><td>6.98 (-5.10%)</td><td>2.21 <b>(-32.42%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>14.06 (n/a)</td><td>11.46 (n/a)</td><td>13.55 (n/a)</td><td>7.36 (n/a)</td><td>3.27 (n/a)</td><td>14.05 (n/a)</td><td>11.46 (n/a)</td><td>13.54 (n/a)</td><td>7.35 (n/a)</td><td>3.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.93 (n/a)</td><td>3.82 (n/a)</td><td>3.79 (n/a)</td><td>3.69 (n/a)</td><td>0.11 (n/a)</td><td>3.93 (n/a)</td><td>3.82 (n/a)</td><td>3.79 (n/a)</td><td>3.68 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>7.55 (-1.58%)</td><td>6.77 (-0.93%)</td><td>7.10 (-1.62%)</td><td>5.50 (+7.97%)</td><td>0.78 <b>(-22.78%)</b></td><td>7.54 (-1.58%)</td><td>6.77 (-0.93%)</td><td>7.09 (-1.62%)</td><td>5.49 (+7.97%)</td><td>0.78 <b>(-22.78%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.67 (n/a)</td><td>6.84 (n/a)</td><td>7.22 (n/a)</td><td>5.09 (n/a)</td><td>1.02 (n/a)</td><td>7.66 (n/a)</td><td>6.83 (n/a)</td><td>7.21 (n/a)</td><td>5.09 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>13.96 <b>(+40.13%)</b></td><td>10.29 (+17.39%)</td><td>8.88 (+1.44%)</td><td>8.22 (+7.03%)</td><td>2.62 <b>(+182.78%)</b></td><td>13.95 <b>(+40.13%)</b></td><td>10.29 (+17.39%)</td><td>8.87 (+1.44%)</td><td>8.22 (+7.03%)</td><td>2.62 <b>(+182.78%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.96 (n/a)</td><td>8.77 (n/a)</td><td>8.75 (n/a)</td><td>7.68 (n/a)</td><td>0.93 (n/a)</td><td>9.96 (n/a)</td><td>8.76 (n/a)</td><td>8.75 (n/a)</td><td>7.68 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.10 (-2.06%)</td><td>2.30 (+3.55%)</td><td>2.78 (-2.77%)</td><td>1.00 (-2.92%)</td><td>0.90 (-16.80%)</td><td>3.09 (-2.06%)</td><td>2.29 (+3.55%)</td><td>2.78 (-2.77%)</td><td>1.00 (-2.92%)</td><td>0.90 (-16.80%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.16 (n/a)</td><td>2.22 (n/a)</td><td>2.86 (n/a)</td><td>1.03 (n/a)</td><td>1.08 (n/a)</td><td>3.15 (n/a)</td><td>2.21 (n/a)</td><td>2.86 (n/a)</td><td>1.03 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.57 (+0.62%)</td><td>0.32 <b>(-24.97%)</b></td><td>0.33 <b>(-36.56%)</b></td><td>0.08 <b>(-44.15%)</b></td><td>0.24 <b>(+26.50%)</b></td><td>0.56 (+0.62%)</td><td>0.31 <b>(-24.97%)</b></td><td>0.32 <b>(-36.56%)</b></td><td>0.08 <b>(-44.15%)</b></td><td>0.23 <b>(+26.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>0.19 (n/a)</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.51 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.74 (-5.02%)</td><td>0.69 <b>(+48.27%)</b></td><td>0.70 <b>(+43.59%)</b></td><td>0.62 <b>(+679.82%)</b></td><td>0.05 <b>(-80.07%)</b></td><td>0.73 (-5.02%)</td><td>0.68 <b>(+48.27%)</b></td><td>0.69 <b>(+43.59%)</b></td><td>0.61 <b>(+679.82%)</b></td><td>0.05 <b>(-80.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.77 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.48 (-5.94%)</td><td>1.73 <b>(+26.68%)</b></td><td>1.83 <b>(+115.66%)</b></td><td>0.45 <b>(-42.38%)</b></td><td>0.79 (-4.30%)</td><td>2.44 (-5.94%)</td><td>1.71 <b>(+26.68%)</b></td><td>1.80 <b>(+115.66%)</b></td><td>0.44 <b>(-42.38%)</b></td><td>0.78 (-4.30%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.64 (n/a)</td><td>1.37 (n/a)</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.82 (n/a)</td><td>2.59 (n/a)</td><td>1.35 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.81 (n/a)</td>
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


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.60 (n/a)</td><td>405.26 (n/a)</td><td>440.50 (n/a)</td><td>215.60 (n/a)</td><td>148.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.40 (n/a)</td><td>396.80 (n/a)</td><td>438.90 (n/a)</td><td>233.60 (n/a)</td><td>99.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.80 (n/a)</td><td>398.94 (n/a)</td><td>434.70 (n/a)</td><td>184.00 (n/a)</td><td>167.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>355.24 (n/a)</td><td>313.70 (n/a)</td><td>252.70 (n/a)</td><td>114.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.00 (n/a)</td><td>405.60 (n/a)</td><td>330.30 (n/a)</td><td>190.30 (n/a)</td><td>190.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.60 (n/a)</td><td>379.92 (n/a)</td><td>398.60 (n/a)</td><td>242.90 (n/a)</td><td>133.71 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.80 (n/a)</td><td>455.12 (n/a)</td><td>545.90 (n/a)</td><td>203.20 (n/a)</td><td>173.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>371.32 (n/a)</td><td>340.10 (n/a)</td><td>205.30 (n/a)</td><td>161.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.20 (n/a)</td><td>433.62 (n/a)</td><td>380.80 (n/a)</td><td>246.10 (n/a)</td><td>158.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.70 (n/a)</td><td>481.68 (n/a)</td><td>456.40 (n/a)</td><td>334.60 (n/a)</td><td>119.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>520.30 (n/a)</td><td>464.24 (n/a)</td><td>492.40 (n/a)</td><td>339.40 (n/a)</td><td>71.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1906.00 (n/a)</td><td>766.96 (n/a)</td><td>564.80 (n/a)</td><td>289.60 (n/a)</td><td>648.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>470.00 (n/a)</td><td>335.98 (n/a)</td><td>261.80 (n/a)</td><td>224.10 (n/a)</td><td>121.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.20 (n/a)</td><td>330.64 (n/a)</td><td>271.60 (n/a)</td><td>229.50 (n/a)</td><td>128.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>538.50 (n/a)</td><td>353.34 (n/a)</td><td>257.40 (n/a)</td><td>219.20 (n/a)</td><td>158.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.00 (n/a)</td><td>510.32 (n/a)</td><td>523.80 (n/a)</td><td>367.30 (n/a)</td><td>99.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.20 (n/a)</td><td>413.10 (n/a)</td><td>476.90 (n/a)</td><td>274.70 (n/a)</td><td>119.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>621.70 (n/a)</td><td>488.42 (n/a)</td><td>534.20 (n/a)</td><td>276.20 (n/a)</td><td>130.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>909.60 (n/a)</td><td>495.88 (n/a)</td><td>314.50 (n/a)</td><td>296.00 (n/a)</td><td>275.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1981.40 (n/a)</td><td>837.56 (n/a)</td><td>615.20 (n/a)</td><td>385.00 (n/a)</td><td>647.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>469.90 (n/a)</td><td>375.30 (n/a)</td><td>450.70 (n/a)</td><td>240.80 (n/a)</td><td>118.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>565.80 (n/a)</td><td>390.62 (n/a)</td><td>347.00 (n/a)</td><td>269.50 (n/a)</td><td>131.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>570.70 (n/a)</td><td>353.04 (n/a)</td><td>317.30 (n/a)</td><td>225.70 (n/a)</td><td>129.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>565.70 (n/a)</td><td>399.40 (n/a)</td><td>368.40 (n/a)</td><td>274.80 (n/a)</td><td>117.03 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(+26.46%)</b></td><td>0.01 (+17.06%)</td><td>0.01 <b>(+31.49%)</b></td><td>0.01 <b>(-37.90%)</b></td><td>0.00 <b>(+148.36%)</b></td><td>739.70 <b>(+61.01%)</b></td><td>374.02 (-1.84%)</td><td>290.80 <b>(-23.93%)</b></td><td>235.80 <b>(-20.93%)</b></td><td>206.41 <b>(+254.42%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.40 (n/a)</td><td>381.02 (n/a)</td><td>382.30 (n/a)</td><td>298.20 (n/a)</td><td>58.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+3.84%)</td><td>0.01 (+13.89%)</td><td>0.01 (+0.51%)</td><td>0.01 <b>(+54.97%)</b></td><td>0.00 <b>(-46.82%)</b></td><td>371.30 <b>(-35.47%)</b></td><td>287.70 (-19.48%)</td><td>274.70 (-0.51%)</td><td>239.10 (-3.71%)</td><td>49.72 <b>(-64.98%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.40 (n/a)</td><td>357.30 (n/a)</td><td>276.10 (n/a)</td><td>248.30 (n/a)</td><td>141.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+3.25%)</td><td>0.01 (+5.65%)</td><td>0.01 (-3.37%)</td><td>0.00 <b>(-48.69%)</b></td><td>0.01 <b>(+43.19%)</b></td><td>1130.10 <b>(+94.91%)</b></td><td>540.14 (+17.52%)</td><td>493.30 (+3.48%)</td><td>233.30 (-3.15%)</td><td>360.36 <b>(+177.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.80 (n/a)</td><td>459.60 (n/a)</td><td>476.70 (n/a)</td><td>240.90 (n/a)</td><td>129.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-6.11%)</td><td>0.01 <b>(+50.71%)</b></td><td>0.01 <b>(+72.90%)</b></td><td>0.01 <b>(+309.32%)</b></td><td>0.00 <b>(-35.65%)</b></td><td>593.00 <b>(-75.57%)</b></td><td>339.38 <b>(-59.30%)</b></td><td>289.10 <b>(-42.17%)</b></td><td>243.50 (+6.47%)</td><td>143.15 <b>(-84.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2427.20 (n/a)</td><td>833.92 (n/a)</td><td>499.90 (n/a)</td><td>228.70 (n/a)</td><td>899.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 <b>(-66.50%)</b></td><td>0.01 <b>(-44.83%)</b></td><td>0.01 (-17.96%)</td><td>0.00 <b>(-75.68%)</b></td><td>0.00 <b>(-66.71%)</b></td><td>2405.30 <b>(+311.30%)</b></td><td>912.96 <b>(+105.86%)</b></td><td>575.80 <b>(+21.91%)</b></td><td>459.20 <b>(+198.38%)</b></td><td>835.91 <b>(+394.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.80 (n/a)</td><td>443.48 (n/a)</td><td>472.30 (n/a)</td><td>153.90 (n/a)</td><td>169.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 <b>(-38.53%)</b></td><td>0.01 (-14.59%)</td><td>0.01 (-11.43%)</td><td>0.01 <b>(+22.38%)</b></td><td>0.00 <b>(-64.84%)</b></td><td>553.40 (-18.29%)</td><td>492.90 (+4.46%)</td><td>544.40 (+12.90%)</td><td>355.00 <b>(+62.62%)</b></td><td>84.82 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.30 (n/a)</td><td>471.84 (n/a)</td><td>482.20 (n/a)</td><td>218.30 (n/a)</td><td>165.03 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+5.92%)</td><td>0.02 (-0.77%)</td><td>0.02 (-19.57%)</td><td>0.01 (+1.09%)</td><td>0.01 (+13.51%)</td><td>552.20 (-1.09%)</td><td>404.14 (+2.81%)</td><td>464.10 <b>(+24.36%)</b></td><td>213.50 (-5.57%)</td><td>146.49 (+3.84%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.30 (n/a)</td><td>393.08 (n/a)</td><td>373.20 (n/a)</td><td>226.10 (n/a)</td><td>141.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (-11.83%)</td><td>0.03 (-3.41%)</td><td>0.03 (+3.10%)</td><td>0.02 (+7.48%)</td><td>0.01 <b>(-20.64%)</b></td><td>499.90 (-6.96%)</td><td>310.86 (+0.10%)</td><td>265.80 (-2.99%)</td><td>230.70 (+13.42%)</td><td>108.12 (-17.35%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>310.54 (n/a)</td><td>274.00 (n/a)</td><td>203.40 (n/a)</td><td>130.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+14.91%)</td><td>0.03 <b>(+21.63%)</b></td><td>0.03 <b>(+23.18%)</b></td><td>0.02 <b>(+59.66%)</b></td><td>0.01 (-12.17%)</td><td>404.40 <b>(-37.37%)</b></td><td>302.00 <b>(-23.61%)</b></td><td>268.20 (-18.83%)</td><td>213.10 (-12.95%)</td><td>87.32 <b>(-49.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.70 (n/a)</td><td>395.34 (n/a)</td><td>330.40 (n/a)</td><td>244.80 (n/a)</td><td>172.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+0.91%)</td><td>0.02 (+6.76%)</td><td>0.03 <b>(+52.52%)</b></td><td>0.01 <b>(-22.06%)</b></td><td>0.01 (+7.22%)</td><td>632.70 <b>(+28.28%)</b></td><td>376.06 (-2.79%)</td><td>291.70 <b>(-34.43%)</b></td><td>226.40 (-0.92%)</td><td>163.16 <b>(+36.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.20 (n/a)</td><td>386.86 (n/a)</td><td>444.90 (n/a)</td><td>228.50 (n/a)</td><td>119.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-7.13%)</td><td>0.03 (+9.50%)</td><td>0.03 <b>(+28.04%)</b></td><td>0.02 <b>(+35.77%)</b></td><td>0.01 <b>(-24.18%)</b></td><td>450.40 <b>(-26.35%)</b></td><td>322.86 (-13.56%)</td><td>282.70 <b>(-21.88%)</b></td><td>239.90 (+7.68%)</td><td>85.91 <b>(-40.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.50 (n/a)</td><td>373.50 (n/a)</td><td>361.90 (n/a)</td><td>222.80 (n/a)</td><td>145.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (+0.59%)</td><td>0.02 (+10.02%)</td><td>0.03 <b>(+41.95%)</b></td><td>0.01 (-11.91%)</td><td>0.01 (-4.67%)</td><td>557.70 (+13.52%)</td><td>357.80 (-8.81%)</td><td>310.90 <b>(-29.57%)</b></td><td>263.80 (-0.60%)</td><td>117.13 (+12.30%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.30 (n/a)</td><td>392.36 (n/a)</td><td>441.40 (n/a)</td><td>265.40 (n/a)</td><td>104.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 <b>(+22.93%)</b></td><td>0.03 <b>(+52.31%)</b></td><td>0.03 <b>(+73.41%)</b></td><td>0.01 <b>(+260.34%)</b></td><td>0.01 (+9.07%)</td><td>668.20 <b>(-72.25%)</b></td><td>374.98 <b>(-54.51%)</b></td><td>270.20 <b>(-42.34%)</b></td><td>225.00 (-18.66%)</td><td>187.28 <b>(-78.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2407.90 (n/a)</td><td>824.24 (n/a)</td><td>468.60 (n/a)</td><td>276.60 (n/a)</td><td>890.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (+8.41%)</td><td>0.02 (+16.19%)</td><td>0.02 <b>(+33.84%)</b></td><td>0.02 <b>(+27.51%)</b></td><td>0.01 (-8.50%)</td><td>481.70 <b>(-21.57%)</b></td><td>380.72 (-16.57%)</td><td>390.90 <b>(-25.29%)</b></td><td>263.60 (-7.77%)</td><td>95.42 <b>(-31.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>456.34 (n/a)</td><td>523.20 (n/a)</td><td>285.80 (n/a)</td><td>139.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 <b>(-31.69%)</b></td><td>0.06 (+7.03%)</td><td>0.06 (+12.36%)</td><td>0.06 <b>(+71.66%)</b></td><td>0.00 <b>(-83.09%)</b></td><td>285.20 <b>(-41.75%)</b></td><td>266.00 (-16.67%)</td><td>270.50 (-10.99%)</td><td>247.20 <b>(+46.45%)</b></td><td>17.12 <b>(-85.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>489.60 (n/a)</td><td>319.22 (n/a)</td><td>303.90 (n/a)</td><td>168.80 (n/a)</td><td>115.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+16.89%)</td><td>0.04 (-6.06%)</td><td>0.03 <b>(-20.54%)</b></td><td>0.01 <b>(-65.57%)</b></td><td>0.02 <b>(+90.69%)</b></td><td>1876.70 <b>(+190.42%)</b></td><td>678.88 <b>(+64.96%)</b></td><td>472.70 <b>(+25.85%)</b></td><td>250.80 (-14.46%)</td><td>681.74 <b>(+372.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>646.20 (n/a)</td><td>411.54 (n/a)</td><td>375.60 (n/a)</td><td>293.20 (n/a)</td><td>144.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+2.02%)</td><td>0.06 <b>(+37.64%)</b></td><td>0.06 <b>(+69.08%)</b></td><td>0.04 <b>(+43.43%)</b></td><td>0.01 <b>(-26.01%)</b></td><td>421.00 <b>(-30.29%)</b></td><td>312.32 <b>(-31.91%)</b></td><td>281.40 <b>(-40.86%)</b></td><td>226.50 (-1.99%)</td><td>77.51 <b>(-45.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>603.90 (n/a)</td><td>458.66 (n/a)</td><td>475.80 (n/a)</td><td>231.10 (n/a)</td><td>141.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+5.06%)</td><td>0.05 (+3.10%)</td><td>0.05 <b>(+32.15%)</b></td><td>0.03 (-8.68%)</td><td>0.02 (-8.54%)</td><td>547.30 (+9.50%)</td><td>357.84 (-3.87%)</td><td>303.40 <b>(-24.32%)</b></td><td>230.20 (-4.84%)</td><td>124.39 (+1.45%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>499.80 (n/a)</td><td>372.24 (n/a)</td><td>400.90 (n/a)</td><td>241.90 (n/a)</td><td>122.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (+9.61%)</td><td>0.04 (+14.93%)</td><td>0.04 (+15.14%)</td><td>0.02 <b>(+141.95%)</b></td><td>0.01 (-19.65%)</td><td>776.20 <b>(-58.67%)</b></td><td>431.70 <b>(-36.43%)</b></td><td>374.00 (-13.14%)</td><td>275.10 (-8.79%)</td><td>199.94 <b>(-70.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1877.90 (n/a)</td><td>679.08 (n/a)</td><td>430.60 (n/a)</td><td>301.60 (n/a)</td><td>673.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (+3.42%)</td><td>0.04 <b>(+20.77%)</b></td><td>0.04 (+12.69%)</td><td>0.03 <b>(+246.82%)</b></td><td>0.01 <b>(-34.56%)</b></td><td>537.50 <b>(-71.17%)</b></td><td>442.90 <b>(-40.39%)</b></td><td>462.90 (-11.27%)</td><td>278.60 (-3.30%)</td><td>98.52 <b>(-84.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1864.20 (n/a)</td><td>743.04 (n/a)</td><td>521.70 (n/a)</td><td>288.10 (n/a)</td><td>637.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 <b>(-22.44%)</b></td><td>0.07 (-11.56%)</td><td>0.07 (-8.95%)</td><td>0.06 (-2.53%)</td><td>0.02 <b>(-41.49%)</b></td><td>578.90 (+2.59%)</td><td>471.18 (+9.10%)</td><td>482.40 (+9.84%)</td><td>336.60 <b>(+28.92%)</b></td><td>87.78 <b>(-21.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>564.30 (n/a)</td><td>431.86 (n/a)</td><td>439.20 (n/a)</td><td>261.10 (n/a)</td><td>112.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(-27.38%)</b></td><td>0.07 (-14.48%)</td><td>0.07 (+0.83%)</td><td>0.06 (-1.66%)</td><td>0.01 <b>(-61.77%)</b></td><td>527.30 (+1.70%)</td><td>454.42 (+10.41%)</td><td>471.50 (-0.82%)</td><td>375.40 <b>(+37.71%)</b></td><td>61.44 <b>(-46.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.50 (n/a)</td><td>411.58 (n/a)</td><td>475.40 (n/a)</td><td>272.60 (n/a)</td><td>115.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-1.62%)</td><td>0.09 (-4.31%)</td><td>0.07 (-2.81%)</td><td>0.06 (-13.33%)</td><td>0.03 (+0.07%)</td><td>566.10 (+15.39%)</td><td>402.90 (+5.71%)</td><td>461.50 (+2.90%)</td><td>255.80 (+1.67%)</td><td>135.22 (+14.72%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>490.60 (n/a)</td><td>381.12 (n/a)</td><td>448.50 (n/a)</td><td>251.60 (n/a)</td><td>117.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-2.81%)</td><td>0.10 <b>(+28.56%)</b></td><td>0.12 <b>(+64.14%)</b></td><td>0.02 <b>(-63.15%)</b></td><td>0.05 <b>(+37.71%)</b></td><td>1852.50 <b>(+171.35%)</b></td><td>584.74 <b>(+25.46%)</b></td><td>277.20 <b>(-39.08%)</b></td><td>243.00 (+2.88%)</td><td>708.92 <b>(+345.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>682.70 (n/a)</td><td>466.06 (n/a)</td><td>455.00 (n/a)</td><td>236.20 (n/a)</td><td>159.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 <b>(-32.98%)</b></td><td>0.07 <b>(-24.53%)</b></td><td>0.06 (-9.84%)</td><td>0.05 (-9.43%)</td><td>0.02 <b>(-46.56%)</b></td><td>662.60 (+10.40%)</td><td>518.90 <b>(+22.04%)</b></td><td>557.90 (+10.89%)</td><td>303.60 <b>(+49.26%)</b></td><td>145.05 (-12.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>600.20 (n/a)</td><td>425.20 (n/a)</td><td>503.10 (n/a)</td><td>203.40 (n/a)</td><td>166.01 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+1.60%)</td><td>0.01 <b>(-22.86%)</b></td><td>0.01 (-12.00%)</td><td>0.01 <b>(-50.52%)</b></td><td>0.00 <b>(+276.93%)</b></td><td>592.60 <b>(+102.11%)</b></td><td>388.72 <b>(+44.37%)</b></td><td>309.20 (+13.63%)</td><td>240.80 (-1.59%)</td><td>149.28 <b>(+676.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>293.20 (n/a)</td><td>269.26 (n/a)</td><td>272.10 (n/a)</td><td>244.70 (n/a)</td><td>19.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-0.79%)</td><td>0.02 (+10.49%)</td><td>0.02 (+3.86%)</td><td>0.01 <b>(+31.26%)</b></td><td>0.00 <b>(-46.84%)</b></td><td>336.00 <b>(-23.81%)</b></td><td>267.76 (-13.95%)</td><td>258.40 (-3.73%)</td><td>232.30 (+0.78%)</td><td>39.66 <b>(-57.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>441.00 (n/a)</td><td>311.16 (n/a)</td><td>268.40 (n/a)</td><td>230.50 (n/a)</td><td>92.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-0.88%)</td><td>0.01 <b>(-20.27%)</b></td><td>0.01 <b>(-34.46%)</b></td><td>0.01 <b>(-23.79%)</b></td><td>0.00 <b>(+30.74%)</b></td><td>479.10 <b>(+31.22%)</b></td><td>378.50 <b>(+30.87%)</b></td><td>417.80 <b>(+52.59%)</b></td><td>232.80 (+0.91%)</td><td>106.94 <b>(+76.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>365.10 (n/a)</td><td>289.22 (n/a)</td><td>273.80 (n/a)</td><td>230.70 (n/a)</td><td>60.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(-36.60%)</b></td><td>0.01 <b>(-26.04%)</b></td><td>0.01 <b>(-34.83%)</b></td><td>0.01 (+9.37%)</td><td>0.00 <b>(-40.85%)</b></td><td>495.50 (-8.58%)</td><td>374.84 <b>(+25.47%)</b></td><td>414.20 <b>(+53.41%)</b></td><td>236.00 <b>(+57.75%)</b></td><td>119.82 (-18.06%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.00 (n/a)</td><td>298.76 (n/a)</td><td>270.00 (n/a)</td><td>149.60 (n/a)</td><td>146.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+9.93%)</td><td>0.01 <b>(+36.44%)</b></td><td>0.02 <b>(+23.00%)</b></td><td>0.01 <b>(+255.71%)</b></td><td>0.00 <b>(-25.20%)</b></td><td>559.20 <b>(-71.89%)</b></td><td>319.02 <b>(-52.56%)</b></td><td>272.20 (-18.70%)</td><td>235.60 (-9.03%)</td><td>135.13 <b>(-81.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1989.20 (n/a)</td><td>672.50 (n/a)</td><td>334.80 (n/a)</td><td>259.00 (n/a)</td><td>739.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+12.19%)</td><td>0.01 (+3.63%)</td><td>0.02 (+4.90%)</td><td>0.01 (-4.77%)</td><td>0.00 (+18.47%)</td><td>455.00 (+5.01%)</td><td>295.12 (-1.89%)</td><td>269.10 (-4.68%)</td><td>216.80 (-10.86%)</td><td>92.13 (+17.97%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>433.30 (n/a)</td><td>300.80 (n/a)</td><td>282.30 (n/a)</td><td>243.20 (n/a)</td><td>78.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+7.02%)</td><td>0.01 (-1.33%)</td><td>0.02 (+7.67%)</td><td>0.01 (+3.50%)</td><td>0.00 <b>(+34.46%)</b></td><td>447.50 (-3.37%)</td><td>322.64 (+4.39%)</td><td>257.70 (-7.10%)</td><td>230.10 (-6.58%)</td><td>105.07 (+19.55%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.10 (n/a)</td><td>309.06 (n/a)</td><td>277.40 (n/a)</td><td>246.30 (n/a)</td><td>87.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-5.74%)</td><td>0.01 (-0.86%)</td><td>0.01 <b>(+44.58%)</b></td><td>0.01 <b>(-32.41%)</b></td><td>0.00 (-0.46%)</td><td>803.40 <b>(+47.96%)</b></td><td>418.94 (+7.37%)</td><td>300.10 <b>(-30.84%)</b></td><td>264.20 (+6.10%)</td><td>225.68 <b>(+69.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.00 (n/a)</td><td>390.20 (n/a)</td><td>433.90 (n/a)</td><td>249.00 (n/a)</td><td>133.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-10.67%)</td><td>0.01 (-8.28%)</td><td>0.01 (-16.70%)</td><td>0.01 <b>(+24.28%)</b></td><td>0.00 <b>(-33.88%)</b></td><td>450.40 (-19.54%)</td><td>370.98 (+4.32%)</td><td>401.60 <b>(+20.06%)</b></td><td>295.40 (+11.94%)</td><td>68.45 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.80 (n/a)</td><td>355.62 (n/a)</td><td>334.50 (n/a)</td><td>263.90 (n/a)</td><td>120.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-8.93%)</td><td>0.01 (-17.07%)</td><td>0.01 (-3.31%)</td><td>0.01 <b>(-33.12%)</b></td><td>0.00 <b>(+35.34%)</b></td><td>576.10 <b>(+49.52%)</b></td><td>391.48 <b>(+28.76%)</b></td><td>301.40 (+3.43%)</td><td>265.90 (+9.79%)</td><td>142.68 <b>(+128.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>385.30 (n/a)</td><td>304.04 (n/a)</td><td>291.40 (n/a)</td><td>242.20 (n/a)</td><td>62.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

_No metrics available._


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-5.29%)</td><td>0.01 (-5.81%)</td><td>0.01 (-3.36%)</td><td>0.01 (-8.49%)</td><td>0.00 (-6.95%)</td><td>641.90 (+9.30%)</td><td>489.28 (+6.01%)</td><td>553.00 (+3.48%)</td><td>313.10 (+5.60%)</td><td>137.10 (+5.78%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.30 (n/a)</td><td>461.54 (n/a)</td><td>534.40 (n/a)</td><td>296.50 (n/a)</td><td>129.60 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(+62.70%)</b></td><td>0.03 <b>(+31.61%)</b></td><td>0.03 <b>(+52.07%)</b></td><td>0.02 (+14.86%)</td><td>0.01 <b>(+60.17%)</b></td><td>451.30 (-12.94%)</td><td>321.88 <b>(-22.48%)</b></td><td>327.50 <b>(-34.25%)</b></td><td>171.60 <b>(-38.56%)</b></td><td>101.34 (-17.91%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.40 (n/a)</td><td>415.24 (n/a)</td><td>498.10 (n/a)</td><td>279.30 (n/a)</td><td>123.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (-0.21%)</td><td>0.02 (-17.02%)</td><td>0.03 (-8.27%)</td><td>0.01 <b>(-35.57%)</b></td><td>0.01 <b>(+68.13%)</b></td><td>651.90 <b>(+55.21%)</b></td><td>402.04 <b>(+36.04%)</b></td><td>303.50 (+9.02%)</td><td>229.70 (+0.17%)</td><td>186.21 <b>(+156.61%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>420.00 (n/a)</td><td>295.52 (n/a)</td><td>278.40 (n/a)</td><td>229.30 (n/a)</td><td>72.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 <b>(-25.56%)</b></td><td>0.02 (-6.53%)</td><td>0.01 (-0.66%)</td><td>0.01 (-7.01%)</td><td>0.01 <b>(-25.30%)</b></td><td>609.40 (+7.53%)</td><td>460.96 (+3.50%)</td><td>551.80 (+0.66%)</td><td>289.40 <b>(+34.35%)</b></td><td>156.85 (-1.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>445.36 (n/a)</td><td>548.20 (n/a)</td><td>215.40 (n/a)</td><td>158.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-11.20%)</td><td>0.02 (+15.67%)</td><td>0.02 <b>(+30.10%)</b></td><td>0.01 (-0.69%)</td><td>0.01 (-18.46%)</td><td>576.00 (+0.70%)</td><td>365.34 (-14.74%)</td><td>333.00 <b>(-23.13%)</b></td><td>268.90 (+12.60%)</td><td>123.63 (+1.22%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>428.50 (n/a)</td><td>433.20 (n/a)</td><td>238.80 (n/a)</td><td>122.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+19.30%)</td><td>0.02 (-9.39%)</td><td>0.01 <b>(-30.96%)</b></td><td>0.01 (+12.88%)</td><td>0.01 <b>(+37.03%)</b></td><td>932.50 (-11.41%)</td><td>595.40 (+18.72%)</td><td>577.30 <b>(+44.83%)</b></td><td>222.00 (-16.16%)</td><td>317.31 (+0.07%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1052.60 (n/a)</td><td>501.50 (n/a)</td><td>398.60 (n/a)</td><td>264.80 (n/a)</td><td>317.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (+12.15%)</td><td>0.02 (-7.70%)</td><td>0.02 (-9.45%)</td><td>0.01 <b>(-35.54%)</b></td><td>0.01 <b>(+56.30%)</b></td><td>658.20 <b>(+55.13%)</b></td><td>401.84 (+17.71%)</td><td>395.30 (+10.42%)</td><td>236.20 (-10.83%)</td><td>162.46 <b>(+124.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>424.30 (n/a)</td><td>341.38 (n/a)</td><td>358.00 (n/a)</td><td>264.90 (n/a)</td><td>72.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+10.49%)</td><td>0.02 (-9.13%)</td><td>0.02 (-14.40%)</td><td>0.01 (+8.32%)</td><td>0.01 (+12.39%)</td><td>574.80 (-7.68%)</td><td>465.02 (+10.59%)</td><td>531.60 (+16.81%)</td><td>196.40 (-9.49%)</td><td>153.61 (-9.87%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.60 (n/a)</td><td>420.48 (n/a)</td><td>455.10 (n/a)</td><td>217.00 (n/a)</td><td>170.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-10.18%)</td><td>0.03 <b>(+25.10%)</b></td><td>0.03 <b>(+57.96%)</b></td><td>0.02 <b>(+168.17%)</b></td><td>0.00 <b>(-63.63%)</b></td><td>407.30 <b>(-62.70%)</b></td><td>332.88 <b>(-38.36%)</b></td><td>305.60 <b>(-36.69%)</b></td><td>278.20 (+11.32%)</td><td>54.25 <b>(-84.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1092.10 (n/a)</td><td>540.02 (n/a)</td><td>482.70 (n/a)</td><td>249.90 (n/a)</td><td>340.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-10.78%)</td><td>0.02 <b>(-29.28%)</b></td><td>0.01 <b>(-47.97%)</b></td><td>0.01 (-15.76%)</td><td>0.01 (-19.94%)</td><td>607.50 (+18.72%)</td><td>503.04 <b>(+38.59%)</b></td><td>557.20 <b>(+92.20%)</b></td><td>278.00 (+12.05%)</td><td>136.84 (+1.06%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.70 (n/a)</td><td>362.98 (n/a)</td><td>289.90 (n/a)</td><td>248.10 (n/a)</td><td>135.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+13.69%)</td><td>0.03 (-13.13%)</td><td>0.03 (-9.92%)</td><td>0.01 <b>(-44.73%)</b></td><td>0.01 <b>(+467.60%)</b></td><td>550.00 <b>(+80.92%)</b></td><td>366.76 <b>(+30.15%)</b></td><td>304.10 (+11.03%)</td><td>232.50 (-12.03%)</td><td>147.97 <b>(+809.51%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>304.00 (n/a)</td><td>281.80 (n/a)</td><td>273.90 (n/a)</td><td>264.30 (n/a)</td><td>16.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-10.85%)</td><td>0.02 (-10.45%)</td><td>0.02 (-4.88%)</td><td>0.02 (+8.76%)</td><td>0.00 <b>(-32.74%)</b></td><td>545.20 (-8.06%)</td><td>463.46 (+8.11%)</td><td>481.60 (+5.13%)</td><td>333.60 (+12.17%)</td><td>84.48 <b>(-29.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.00 (n/a)</td><td>428.70 (n/a)</td><td>458.10 (n/a)</td><td>297.40 (n/a)</td><td>119.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-9.19%)</td><td>0.02 (-2.20%)</td><td>0.02 (-0.76%)</td><td>0.01 <b>(+55.55%)</b></td><td>0.01 <b>(-40.54%)</b></td><td>678.50 <b>(-35.71%)</b></td><td>484.90 (-16.05%)</td><td>474.90 (+0.76%)</td><td>293.00 (+10.11%)</td><td>140.90 <b>(-58.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1055.40 (n/a)</td><td>577.60 (n/a)</td><td>471.30 (n/a)</td><td>266.10 (n/a)</td><td>337.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+0.51%)</td><td>0.05 (+3.02%)</td><td>0.06 (+11.97%)</td><td>0.03 <b>(+20.92%)</b></td><td>0.01 (-2.41%)</td><td>480.70 (-17.29%)</td><td>340.12 (-4.71%)</td><td>284.80 (-10.69%)</td><td>244.30 (-0.49%)</td><td>103.66 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>581.20 (n/a)</td><td>356.94 (n/a)</td><td>318.90 (n/a)</td><td>245.50 (n/a)</td><td>132.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (-15.62%)</td><td>0.04 <b>(-31.79%)</b></td><td>0.03 <b>(-43.87%)</b></td><td>0.03 <b>(-36.16%)</b></td><td>0.01 <b>(+52.12%)</b></td><td>522.40 <b>(+56.64%)</b></td><td>430.30 <b>(+53.19%)</b></td><td>494.90 <b>(+78.15%)</b></td><td>288.60 (+18.52%)</td><td>106.71 <b>(+190.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>333.50 (n/a)</td><td>280.90 (n/a)</td><td>277.80 (n/a)</td><td>243.50 (n/a)</td><td>36.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (+9.52%)</td><td>0.06 (+5.57%)</td><td>0.05 (-19.06%)</td><td>0.04 <b>(+34.17%)</b></td><td>0.02 (-4.03%)</td><td>461.30 <b>(-25.48%)</b></td><td>314.06 (-10.68%)</td><td>304.40 <b>(+23.54%)</b></td><td>200.80 (-8.69%)</td><td>112.86 <b>(-35.11%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>619.00 (n/a)</td><td>351.62 (n/a)</td><td>246.40 (n/a)</td><td>219.90 (n/a)</td><td>173.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(+25.85%)</b></td><td>0.06 (+18.47%)</td><td>0.06 <b>(+52.92%)</b></td><td>0.04 (+2.44%)</td><td>0.02 (+12.62%)</td><td>463.10 (-2.38%)</td><td>304.66 (-15.56%)</td><td>268.60 <b>(-34.60%)</b></td><td>189.30 <b>(-20.53%)</b></td><td>103.85 (-7.26%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>474.40 (n/a)</td><td>360.82 (n/a)</td><td>410.70 (n/a)</td><td>238.20 (n/a)</td><td>111.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 <b>(-24.57%)</b></td><td>0.05 (-16.55%)</td><td>0.06 (+0.23%)</td><td>0.03 (-13.39%)</td><td>0.02 (-5.62%)</td><td>513.20 (+15.46%)</td><td>354.26 <b>(+22.99%)</b></td><td>262.70 (-0.23%)</td><td>253.90 <b>(+32.58%)</b></td><td>132.08 <b>(+38.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>444.50 (n/a)</td><td>288.04 (n/a)</td><td>263.30 (n/a)</td><td>191.50 (n/a)</td><td>95.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+2.06%)</td><td>0.04 <b>(-35.15%)</b></td><td>0.04 <b>(-40.36%)</b></td><td>0.01 <b>(-83.04%)</b></td><td>0.03 <b>(+279.66%)</b></td><td>1860.30 <b>(+489.64%)</b></td><td>686.40 <b>(+164.57%)</b></td><td>409.30 <b>(+67.68%)</b></td><td>236.10 (-2.03%)</td><td>678.97 <b>(+2036.26%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>315.50 (n/a)</td><td>259.44 (n/a)</td><td>244.10 (n/a)</td><td>241.00 (n/a)</td><td>31.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+8.83%)</td><td>0.05 (-17.51%)</td><td>0.06 (-15.84%)</td><td>0.04 <b>(-36.05%)</b></td><td>0.02 <b>(+213.76%)</b></td><td>466.40 <b>(+56.41%)</b></td><td>342.36 <b>(+30.66%)</b></td><td>297.40 (+18.82%)</td><td>224.50 (-8.14%)</td><td>108.71 <b>(+378.66%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>298.20 (n/a)</td><td>262.02 (n/a)</td><td>250.30 (n/a)</td><td>244.40 (n/a)</td><td>22.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(-34.19%)</b></td><td>0.04 <b>(-25.37%)</b></td><td>0.04 <b>(-25.50%)</b></td><td>0.03 (-6.16%)</td><td>0.01 <b>(-53.66%)</b></td><td>645.80 (+6.57%)</td><td>440.18 <b>(+22.68%)</b></td><td>407.00 <b>(+34.23%)</b></td><td>318.70 <b>(+51.98%)</b></td><td>123.83 <b>(-22.72%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.00 (n/a)</td><td>358.80 (n/a)</td><td>303.20 (n/a)</td><td>209.70 (n/a)</td><td>160.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 <b>(+25.16%)</b></td><td>0.04 (+12.10%)</td><td>0.04 (+15.77%)</td><td>0.02 <b>(-33.78%)</b></td><td>0.02 <b>(+85.01%)</b></td><td>1005.40 <b>(+51.01%)</b></td><td>520.04 (+2.00%)</td><td>461.30 (-13.61%)</td><td>290.20 <b>(-20.10%)</b></td><td>284.31 <b>(+136.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.80 (n/a)</td><td>509.86 (n/a)</td><td>534.00 (n/a)</td><td>363.20 (n/a)</td><td>120.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+8.44%)</td><td>0.05 (-16.75%)</td><td>0.05 <b>(-20.10%)</b></td><td>0.03 <b>(-21.39%)</b></td><td>0.02 <b>(+51.14%)</b></td><td>620.70 <b>(+27.22%)</b></td><td>410.66 <b>(+32.07%)</b></td><td>343.60 <b>(+25.13%)</b></td><td>225.00 (-7.79%)</td><td>180.08 <b>(+79.57%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>310.94 (n/a)</td><td>274.60 (n/a)</td><td>244.00 (n/a)</td><td>100.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (-6.83%)</td><td>0.04 (+15.21%)</td><td>0.03 (+4.27%)</td><td>0.03 <b>(+33.76%)</b></td><td>0.01 (-11.87%)</td><td>567.00 <b>(-25.24%)</b></td><td>442.42 (-16.22%)</td><td>519.10 (-4.10%)</td><td>280.50 (+7.31%)</td><td>136.39 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>758.40 (n/a)</td><td>528.06 (n/a)</td><td>541.30 (n/a)</td><td>261.40 (n/a)</td><td>179.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (-6.53%)</td><td>0.05 (-4.61%)</td><td>0.05 (+2.22%)</td><td>0.03 (-17.21%)</td><td>0.01 (+10.35%)</td><td>544.30 <b>(+20.79%)</b></td><td>370.84 (+6.99%)</td><td>316.60 (-2.16%)</td><td>284.50 (+7.00%)</td><td>108.51 <b>(+41.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>450.60 (n/a)</td><td>346.60 (n/a)</td><td>323.60 (n/a)</td><td>265.90 (n/a)</td><td>76.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-3.11%)</td><td>0.09 (-15.38%)</td><td>0.12 (-0.28%)</td><td>0.02 <b>(-72.91%)</b></td><td>0.05 <b>(+51.14%)</b></td><td>1879.80 <b>(+269.09%)</b></td><td>638.24 <b>(+90.21%)</b></td><td>276.90 (+0.29%)</td><td>248.70 (+3.20%)</td><td>701.97 <b>(+500.45%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>509.30 (n/a)</td><td>335.54 (n/a)</td><td>276.10 (n/a)</td><td>241.00 (n/a)</td><td>116.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-4.96%)</td><td>0.10 (-14.32%)</td><td>0.10 (-16.21%)</td><td>0.06 <b>(-35.02%)</b></td><td>0.03 <b>(+62.04%)</b></td><td>520.60 <b>(+53.89%)</b></td><td>337.32 <b>(+22.94%)</b></td><td>316.80 (+19.32%)</td><td>244.80 (+5.20%)</td><td>109.14 <b>(+166.56%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>338.30 (n/a)</td><td>274.38 (n/a)</td><td>265.50 (n/a)</td><td>232.70 (n/a)</td><td>40.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-3.51%)</td><td>0.09 <b>(-21.13%)</b></td><td>0.09 <b>(-31.59%)</b></td><td>0.06 (-5.46%)</td><td>0.03 (-6.65%)</td><td>517.70 (+5.76%)</td><td>373.68 <b>(+25.98%)</b></td><td>363.20 <b>(+46.16%)</b></td><td>248.10 (+3.63%)</td><td>107.99 (-0.19%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>489.50 (n/a)</td><td>296.62 (n/a)</td><td>248.50 (n/a)</td><td>239.40 (n/a)</td><td>108.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-6.97%)</td><td>0.09 <b>(-26.14%)</b></td><td>0.07 <b>(-42.35%)</b></td><td>0.07 <b>(-35.55%)</b></td><td>0.03 <b>(+132.86%)</b></td><td>483.20 <b>(+55.17%)</b></td><td>381.18 <b>(+46.69%)</b></td><td>448.40 <b>(+73.46%)</b></td><td>247.40 (+7.52%)</td><td>118.53 <b>(+278.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>311.40 (n/a)</td><td>259.86 (n/a)</td><td>258.50 (n/a)</td><td>230.10 (n/a)</td><td>31.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+5.14%)</td><td>0.10 (+17.14%)</td><td>0.11 <b>(+31.86%)</b></td><td>0.05 (-3.94%)</td><td>0.04 <b>(+36.77%)</b></td><td>604.50 (+4.10%)</td><td>384.82 (-8.42%)</td><td>304.60 <b>(-24.15%)</b></td><td>236.90 (-4.90%)</td><td>170.88 <b>(+39.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.70 (n/a)</td><td>420.22 (n/a)</td><td>401.60 (n/a)</td><td>249.10 (n/a)</td><td>122.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (-9.76%)</td><td>0.10 (-16.36%)</td><td>0.11 (-8.39%)</td><td>0.06 (-13.56%)</td><td>0.04 (+19.79%)</td><td>553.90 (+15.69%)</td><td>377.80 <b>(+26.26%)</b></td><td>297.50 (+9.17%)</td><td>242.00 (+10.81%)</td><td>153.76 <b>(+49.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>478.80 (n/a)</td><td>299.22 (n/a)</td><td>272.50 (n/a)</td><td>218.40 (n/a)</td><td>102.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 <b>(+54.22%)</b></td><td>0.08 (+6.38%)</td><td>0.07 (-7.78%)</td><td>0.02 <b>(-69.97%)</b></td><td>0.05 <b>(+233.01%)</b></td><td>1886.70 <b>(+232.99%)</b></td><td>697.12 <b>(+49.91%)</b></td><td>457.20 (+8.42%)</td><td>249.70 <b>(-35.18%)</b></td><td>679.07 <b>(+640.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>566.60 (n/a)</td><td>465.04 (n/a)</td><td>421.70 (n/a)</td><td>385.20 (n/a)</td><td>91.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 <b>(-21.95%)</b></td><td>0.08 <b>(-21.90%)</b></td><td>0.08 <b>(-30.82%)</b></td><td>0.06 <b>(-32.03%)</b></td><td>0.02 (-3.62%)</td><td>568.00 <b>(+47.15%)</b></td><td>411.32 <b>(+30.83%)</b></td><td>427.80 <b>(+44.58%)</b></td><td>299.30 <b>(+28.13%)</b></td><td>111.83 <b>(+66.08%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>386.00 (n/a)</td><td>314.40 (n/a)</td><td>295.90 (n/a)</td><td>233.60 (n/a)</td><td>67.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 <b>(-37.49%)</b></td><td>0.07 <b>(-20.10%)</b></td><td>0.06 <b>(-25.08%)</b></td><td>0.05 (-13.73%)</td><td>0.02 <b>(-38.41%)</b></td><td>632.10 (+15.92%)</td><td>482.16 <b>(+22.01%)</b></td><td>528.60 <b>(+33.48%)</b></td><td>326.20 <b>(+59.98%)</b></td><td>145.93 (+18.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>545.30 (n/a)</td><td>395.18 (n/a)</td><td>396.00 (n/a)</td><td>203.90 (n/a)</td><td>123.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-0.72%)</td><td>0.08 <b>(-21.06%)</b></td><td>0.07 <b>(-33.91%)</b></td><td>0.05 (-14.51%)</td><td>0.03 <b>(+27.25%)</b></td><td>619.20 (+16.98%)</td><td>450.02 <b>(+34.58%)</b></td><td>464.40 <b>(+51.32%)</b></td><td>252.60 (+0.72%)</td><td>169.96 <b>(+50.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>529.30 (n/a)</td><td>334.38 (n/a)</td><td>306.90 (n/a)</td><td>250.80 (n/a)</td><td>113.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+9.64%)</td><td>0.09 (+6.72%)</td><td>0.09 (+1.10%)</td><td>0.06 (+18.06%)</td><td>0.03 (-5.83%)</td><td>561.90 (-15.30%)</td><td>396.22 (-10.01%)</td><td>379.00 (-1.10%)</td><td>241.90 (-8.82%)</td><td>124.66 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>663.40 (n/a)</td><td>440.28 (n/a)</td><td>383.20 (n/a)</td><td>265.30 (n/a)</td><td>174.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (+0.05%)</td><td>0.08 (-19.64%)</td><td>0.08 <b>(-30.61%)</b></td><td>0.06 <b>(+59.56%)</b></td><td>0.03 <b>(-23.98%)</b></td><td>584.30 <b>(-37.33%)</b></td><td>434.44 (+7.38%)</td><td>402.20 <b>(+44.11%)</b></td><td>261.70 (-0.04%)</td><td>144.91 <b>(-50.90%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>932.30 (n/a)</td><td>404.60 (n/a)</td><td>279.10 (n/a)</td><td>261.80 (n/a)</td><td>295.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (+11.48%)</td><td>0.06 <b>(-30.68%)</b></td><td>0.05 <b>(-47.64%)</b></td><td>0.05 <b>(-32.93%)</b></td><td>0.03 <b>(+109.74%)</b></td><td>545.10 <b>(+49.10%)</b></td><td>463.26 <b>(+63.37%)</b></td><td>537.40 <b>(+90.97%)</b></td><td>200.30 (-10.26%)</td><td>148.84 <b>(+174.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>365.60 (n/a)</td><td>283.56 (n/a)</td><td>281.40 (n/a)</td><td>223.20 (n/a)</td><td>54.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.24 (+14.88%)</td><td>0.12 (-16.81%)</td><td>0.10 <b>(-32.26%)</b></td><td>0.03 <b>(-76.00%)</b></td><td>0.08 <b>(+127.62%)</b></td><td>1921.10 <b>(+316.63%)</b></td><td>700.48 <b>(+103.33%)</b></td><td>504.40 <b>(+47.61%)</b></td><td>206.30 (-12.95%)</td><td>700.50 <b>(+771.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>461.10 (n/a)</td><td>344.50 (n/a)</td><td>341.70 (n/a)</td><td>237.00 (n/a)</td><td>80.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.70 (-10.93%)</td><td>3.16 (+1.81%)</td><td>3.18 (+5.96%)</td><td>2.55 (-4.19%)</td><td>0.50 (-17.66%)</td><td>4109.80 (+4.38%)</td><td>3382.48 (-2.28%)</td><td>3301.00 (-5.63%)</td><td>2834.20 (+12.27%)</td><td>549.25 (-3.08%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.15 (n/a)</td><td>3.11 (n/a)</td><td>3.00 (n/a)</td><td>2.66 (n/a)</td><td>0.61 (n/a)</td><td>3937.40 (n/a)</td><td>3461.26 (n/a)</td><td>3497.90 (n/a)</td><td>2524.40 (n/a)</td><td>566.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (+5.50%)</td><td>0.09 <b>(-29.96%)</b></td><td>0.07 <b>(-52.64%)</b></td><td>0.02 <b>(-67.51%)</b></td><td>0.07 (+14.03%)</td><td>1904.20 <b>(+207.77%)</b></td><td>759.50 <b>(+94.28%)</b></td><td>556.80 <b>(+111.15%)</b></td><td>208.70 (-5.18%)</td><td>669.82 <b>(+224.45%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>618.70 (n/a)</td><td>390.94 (n/a)</td><td>263.70 (n/a)</td><td>220.10 (n/a)</td><td>206.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+7.46%)</td><td>0.02 (-16.05%)</td><td>0.02 (-13.42%)</td><td>0.01 <b>(-33.97%)</b></td><td>0.01 <b>(+116.10%)</b></td><td>483.80 <b>(+51.47%)</b></td><td>360.84 <b>(+29.52%)</b></td><td>335.90 (+15.51%)</td><td>207.70 (-6.94%)</td><td>118.94 <b>(+225.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>319.40 (n/a)</td><td>278.60 (n/a)</td><td>290.80 (n/a)</td><td>223.20 (n/a)</td><td>36.56 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+16.39%)</td><td>0.01 (+0.16%)</td><td>0.02 (-1.18%)</td><td>0.01 (-1.14%)</td><td>0.00 (+18.86%)</td><td>504.00 (+1.16%)</td><td>305.88 (+1.51%)</td><td>254.20 (+1.19%)</td><td>207.90 (-14.09%)</td><td>117.32 (+5.96%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.20 (n/a)</td><td>301.34 (n/a)</td><td>251.20 (n/a)</td><td>242.00 (n/a)</td><td>110.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(-36.67%)</b></td><td>0.01 <b>(-30.73%)</b></td><td>0.01 <b>(-36.14%)</b></td><td>0.01 <b>(+88.58%)</b></td><td>0.00 <b>(-57.53%)</b></td><td>1055.20 <b>(-46.97%)</b></td><td>585.96 (-10.00%)</td><td>469.30 <b>(+56.59%)</b></td><td>381.60 <b>(+57.95%)</b></td><td>270.21 <b>(-64.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1989.80 (n/a)</td><td>651.10 (n/a)</td><td>299.70 (n/a)</td><td>241.60 (n/a)</td><td>753.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-5.19%)</td><td>0.01 (-9.00%)</td><td>0.01 (-8.25%)</td><td>0.01 (-14.97%)</td><td>0.00 (-2.00%)</td><td>563.30 (+17.60%)</td><td>389.38 (+11.52%)</td><td>389.30 (+8.99%)</td><td>256.30 (+5.47%)</td><td>130.61 <b>(+23.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.00 (n/a)</td><td>349.16 (n/a)</td><td>357.20 (n/a)</td><td>243.00 (n/a)</td><td>105.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+0.68%)</td><td>0.02 <b>(+29.63%)</b></td><td>0.02 <b>(+62.43%)</b></td><td>0.01 (-0.22%)</td><td>0.00 (+4.46%)</td><td>515.00 (+0.21%)</td><td>315.76 <b>(-22.10%)</b></td><td>276.70 <b>(-38.43%)</b></td><td>236.80 (-0.67%)</td><td>115.80 (+9.39%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.90 (n/a)</td><td>405.32 (n/a)</td><td>449.40 (n/a)</td><td>238.40 (n/a)</td><td>105.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+2.58%)</td><td>0.01 (+8.09%)</td><td>0.01 (-4.74%)</td><td>0.01 (-5.73%)</td><td>0.00 (-7.49%)</td><td>489.30 (+6.07%)</td><td>303.48 (-8.79%)</td><td>281.50 (+5.00%)</td><td>224.60 (-2.48%)</td><td>108.26 (-7.34%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.30 (n/a)</td><td>332.72 (n/a)</td><td>268.10 (n/a)</td><td>230.30 (n/a)</td><td>116.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(-21.33%)</b></td><td>0.01 <b>(-37.39%)</b></td><td>0.01 <b>(-51.41%)</b></td><td>0.01 (-17.80%)</td><td>0.00 <b>(-29.99%)</b></td><td>623.80 <b>(+21.67%)</b></td><td>472.08 <b>(+55.87%)</b></td><td>509.50 <b>(+105.78%)</b></td><td>302.60 <b>(+27.09%)</b></td><td>120.86 (+2.38%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.70 (n/a)</td><td>302.86 (n/a)</td><td>247.60 (n/a)</td><td>238.10 (n/a)</td><td>118.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 <b>(-32.12%)</b></td><td>0.01 <b>(-36.53%)</b></td><td>0.01 <b>(-30.89%)</b></td><td>0.00 <b>(-74.72%)</b></td><td>0.00 (+12.97%)</td><td>1821.60 <b>(+295.57%)</b></td><td>708.22 <b>(+111.67%)</b></td><td>437.00 <b>(+44.70%)</b></td><td>359.20 <b>(+47.33%)</b></td><td>624.11 <b>(+626.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.50 (n/a)</td><td>334.58 (n/a)</td><td>302.00 (n/a)</td><td>243.80 (n/a)</td><td>85.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-17.40%)</td><td>0.01 (-16.33%)</td><td>0.01 <b>(-27.88%)</b></td><td>0.01 (+13.67%)</td><td>0.00 <b>(-33.23%)</b></td><td>532.00 (-12.04%)</td><td>413.60 (+13.75%)</td><td>435.60 <b>(+38.68%)</b></td><td>296.20 <b>(+21.05%)</b></td><td>91.72 <b>(-34.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.80 (n/a)</td><td>363.62 (n/a)</td><td>314.10 (n/a)</td><td>244.70 (n/a)</td><td>140.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-11.76%)</td><td>0.01 <b>(-25.66%)</b></td><td>0.01 <b>(-46.05%)</b></td><td>0.01 (-8.34%)</td><td>0.00 (+7.67%)</td><td>586.10 (+9.10%)</td><td>438.62 <b>(+38.19%)</b></td><td>514.30 <b>(+85.33%)</b></td><td>270.80 (+13.31%)</td><td>152.13 <b>(+22.24%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.20 (n/a)</td><td>317.40 (n/a)</td><td>277.50 (n/a)</td><td>239.00 (n/a)</td><td>124.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (-17.80%)</td><td>0.01 <b>(+23.89%)</b></td><td>0.01 <b>(+42.93%)</b></td><td>0.01 <b>(+62.94%)</b></td><td>0.00 <b>(-33.42%)</b></td><td>670.10 <b>(-38.62%)</b></td><td>415.54 <b>(-30.11%)</b></td><td>383.30 <b>(-30.03%)</b></td><td>278.90 <b>(+21.68%)</b></td><td>158.94 <b>(-49.08%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1091.80 (n/a)</td><td>594.54 (n/a)</td><td>547.80 (n/a)</td><td>229.20 (n/a)</td><td>312.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 <b>(-25.14%)</b></td><td>0.01 (-15.49%)</td><td>0.01 <b>(-26.31%)</b></td><td>0.00 <b>(-35.32%)</b></td><td>0.00 <b>(-22.19%)</b></td><td>1047.10 <b>(+54.60%)</b></td><td>549.94 <b>(+20.44%)</b></td><td>480.90 <b>(+35.69%)</b></td><td>309.60 <b>(+33.56%)</b></td><td>297.08 <b>(+46.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>677.30 (n/a)</td><td>456.62 (n/a)</td><td>354.40 (n/a)</td><td>231.80 (n/a)</td><td>202.65 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-17.66%)</td><td>0.02 (-19.26%)</td><td>0.03 (-17.86%)</td><td>0.02 (-6.38%)</td><td>0.00 <b>(-23.75%)</b></td><td>462.30 (+6.82%)</td><td>353.66 <b>(+22.23%)</b></td><td>312.00 <b>(+21.73%)</b></td><td>280.10 <b>(+21.47%)</b></td><td>78.12 (-4.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>432.80 (n/a)</td><td>289.34 (n/a)</td><td>256.30 (n/a)</td><td>230.60 (n/a)</td><td>81.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (-8.16%)</td><td>0.04 (-1.73%)</td><td>0.04 (+2.00%)</td><td>0.03 (+1.44%)</td><td>0.01 (-14.45%)</td><td>466.60 (-1.42%)</td><td>307.04 (+0.49%)</td><td>273.70 (-1.97%)</td><td>249.50 (+8.90%)</td><td>90.13 (-7.76%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.30 (n/a)</td><td>305.54 (n/a)</td><td>279.20 (n/a)</td><td>229.10 (n/a)</td><td>97.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+1.71%)</td><td>0.03 <b>(+37.09%)</b></td><td>0.03 <b>(+75.16%)</b></td><td>0.03 <b>(+111.51%)</b></td><td>0.00 <b>(-67.71%)</b></td><td>308.90 <b>(-52.72%)</b></td><td>263.84 <b>(-38.94%)</b></td><td>264.70 <b>(-42.92%)</b></td><td>224.60 (-1.71%)</td><td>30.79 <b>(-84.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.30 (n/a)</td><td>432.10 (n/a)</td><td>463.70 (n/a)</td><td>228.50 (n/a)</td><td>192.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (-10.01%)</td><td>0.03 (-14.99%)</td><td>0.02 <b>(-33.12%)</b></td><td>0.01 (-5.47%)</td><td>0.01 (-4.92%)</td><td>700.30 (+5.79%)</td><td>466.78 (+18.08%)</td><td>471.50 <b>(+49.54%)</b></td><td>269.60 (+11.13%)</td><td>191.36 (+7.48%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>662.00 (n/a)</td><td>395.32 (n/a)</td><td>315.30 (n/a)</td><td>242.60 (n/a)</td><td>178.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (+8.07%)</td><td>0.03 <b>(-23.13%)</b></td><td>0.02 <b>(-34.78%)</b></td><td>0.02 <b>(-29.86%)</b></td><td>0.01 <b>(+38.45%)</b></td><td>508.60 <b>(+42.54%)</b></td><td>359.60 <b>(+40.34%)</b></td><td>362.10 <b>(+53.37%)</b></td><td>179.90 (-7.46%)</td><td>128.31 <b>(+83.55%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>356.80 (n/a)</td><td>256.24 (n/a)</td><td>236.10 (n/a)</td><td>194.40 (n/a)</td><td>69.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 <b>(-25.19%)</b></td><td>0.03 <b>(-30.51%)</b></td><td>0.02 <b>(-33.86%)</b></td><td>0.02 <b>(-25.99%)</b></td><td>0.01 (-14.46%)</td><td>572.10 <b>(+35.12%)</b></td><td>412.46 <b>(+48.25%)</b></td><td>417.80 <b>(+51.21%)</b></td><td>253.60 <b>(+33.68%)</b></td><td>148.49 <b>(+58.01%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>423.40 (n/a)</td><td>278.22 (n/a)</td><td>276.30 (n/a)</td><td>189.70 (n/a)</td><td>93.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(+29.78%)</b></td><td>0.03 (+11.33%)</td><td>0.02 (-6.03%)</td><td>0.02 <b>(+21.18%)</b></td><td>0.01 <b>(+42.01%)</b></td><td>461.30 (-17.48%)</td><td>358.74 (-7.55%)</td><td>418.50 (+6.41%)</td><td>181.00 <b>(-22.95%)</b></td><td>120.46 (-7.34%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.00 (n/a)</td><td>388.02 (n/a)</td><td>393.30 (n/a)</td><td>234.90 (n/a)</td><td>130.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (-16.66%)</td><td>0.03 (+10.22%)</td><td>0.03 <b>(+29.43%)</b></td><td>0.02 <b>(+43.08%)</b></td><td>0.00 <b>(-61.87%)</b></td><td>436.80 <b>(-30.10%)</b></td><td>346.26 (-19.79%)</td><td>332.00 <b>(-22.75%)</b></td><td>297.00 <b>(+20.00%)</b></td><td>55.99 <b>(-67.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.90 (n/a)</td><td>431.70 (n/a)</td><td>429.80 (n/a)</td><td>247.50 (n/a)</td><td>173.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (+9.55%)</td><td>0.02 (-16.82%)</td><td>0.02 <b>(-36.58%)</b></td><td>0.01 (+16.00%)</td><td>0.01 (-7.33%)</td><td>606.30 (-13.79%)</td><td>476.52 (+14.67%)</td><td>474.00 <b>(+57.68%)</b></td><td>242.00 (-8.75%)</td><td>148.98 <b>(-24.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>703.30 (n/a)</td><td>415.56 (n/a)</td><td>300.60 (n/a)</td><td>265.20 (n/a)</td><td>197.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (+19.84%)</td><td>0.03 (+19.01%)</td><td>0.02 (+8.92%)</td><td>0.02 <b>(+28.98%)</b></td><td>0.01 (+19.23%)</td><td>443.60 <b>(-22.46%)</b></td><td>379.90 (-16.16%)</td><td>419.00 (-8.19%)</td><td>245.50 (-16.55%)</td><td>81.42 <b>(-20.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.10 (n/a)</td><td>453.12 (n/a)</td><td>456.40 (n/a)</td><td>294.20 (n/a)</td><td>102.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (+11.81%)</td><td>0.02 (+3.10%)</td><td>0.01 (-1.78%)</td><td>0.01 <b>(+58.92%)</b></td><td>0.01 (-10.25%)</td><td>653.20 <b>(-37.08%)</b></td><td>503.66 (-11.18%)</td><td>550.80 (+1.81%)</td><td>289.80 (-10.56%)</td><td>136.89 <b>(-51.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1038.20 (n/a)</td><td>567.08 (n/a)</td><td>541.00 (n/a)</td><td>324.00 (n/a)</td><td>284.42 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+9.69%)</td><td>0.05 (+5.25%)</td><td>0.06 (+8.10%)</td><td>0.04 (-13.15%)</td><td>0.01 <b>(+56.10%)</b></td><td>467.30 (+15.16%)</td><td>321.96 (-1.17%)</td><td>278.40 (-7.51%)</td><td>232.60 (-8.86%)</td><td>97.48 <b>(+62.85%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>405.80 (n/a)</td><td>325.76 (n/a)</td><td>301.00 (n/a)</td><td>255.20 (n/a)</td><td>59.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (+19.68%)</td><td>0.07 (-3.48%)</td><td>0.06 <b>(-30.38%)</b></td><td>0.04 (-4.15%)</td><td>0.03 <b>(+20.58%)</b></td><td>593.50 (+4.34%)</td><td>387.38 (+6.78%)</td><td>378.10 <b>(+43.60%)</b></td><td>197.00 (-16.45%)</td><td>166.94 (+6.26%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>568.80 (n/a)</td><td>362.78 (n/a)</td><td>263.30 (n/a)</td><td>235.80 (n/a)</td><td>157.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (-10.09%)</td><td>0.05 (-10.63%)</td><td>0.04 <b>(-22.25%)</b></td><td>0.03 (-2.87%)</td><td>0.01 (-12.52%)</td><td>520.00 (+2.97%)</td><td>393.44 (+10.48%)</td><td>401.20 <b>(+28.63%)</b></td><td>257.10 (+11.20%)</td><td>120.88 (-2.08%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>505.00 (n/a)</td><td>356.12 (n/a)</td><td>311.90 (n/a)</td><td>231.20 (n/a)</td><td>123.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (-1.99%)</td><td>0.05 (-3.13%)</td><td>0.04 (-12.82%)</td><td>0.04 (-2.99%)</td><td>0.02 (+3.70%)</td><td>561.00 (+3.09%)</td><td>421.04 (+4.76%)</td><td>499.00 (+14.69%)</td><td>234.70 (+2.04%)</td><td>144.71 (+10.02%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>544.20 (n/a)</td><td>401.92 (n/a)</td><td>435.10 (n/a)</td><td>230.00 (n/a)</td><td>131.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (-4.88%)</td><td>0.05 (+7.08%)</td><td>0.04 <b>(+20.66%)</b></td><td>0.03 (+4.29%)</td><td>0.02 (-9.38%)</td><td>557.20 (-4.11%)</td><td>392.74 (-9.41%)</td><td>420.30 (-17.12%)</td><td>235.60 (+5.08%)</td><td>140.46 (-14.10%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.10 (n/a)</td><td>433.54 (n/a)</td><td>507.10 (n/a)</td><td>224.20 (n/a)</td><td>163.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (+9.17%)</td><td>0.06 (-0.74%)</td><td>0.05 (-2.14%)</td><td>0.04 (-5.07%)</td><td>0.02 (+17.97%)</td><td>530.00 (+5.35%)</td><td>397.76 (+2.97%)</td><td>427.50 (+2.17%)</td><td>243.60 (-8.39%)</td><td>120.63 (+16.36%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.10 (n/a)</td><td>386.28 (n/a)</td><td>418.40 (n/a)</td><td>265.90 (n/a)</td><td>103.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (+18.68%)</td><td>0.05 (-2.23%)</td><td>0.06 (-10.56%)</td><td>0.03 (-15.29%)</td><td>0.02 <b>(+24.03%)</b></td><td>591.90 (+18.05%)</td><td>357.00 (+8.08%)</td><td>272.10 (+11.79%)</td><td>185.70 (-15.74%)</td><td>167.98 <b>(+27.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>501.40 (n/a)</td><td>330.30 (n/a)</td><td>243.40 (n/a)</td><td>220.40 (n/a)</td><td>132.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (-12.72%)</td><td>0.05 (+17.06%)</td><td>0.05 <b>(+42.40%)</b></td><td>0.04 <b>(+202.23%)</b></td><td>0.01 <b>(-64.21%)</b></td><td>451.70 <b>(-66.91%)</b></td><td>372.44 <b>(-36.59%)</b></td><td>343.10 <b>(-29.76%)</b></td><td>321.20 (+14.55%)</td><td>59.83 <b>(-86.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1365.00 (n/a)</td><td>587.34 (n/a)</td><td>488.50 (n/a)</td><td>280.40 (n/a)</td><td>447.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (-4.81%)</td><td>0.04 (-12.89%)</td><td>0.05 (-3.72%)</td><td>0.01 <b>(-80.47%)</b></td><td>0.03 <b>(+64.19%)</b></td><td>2487.10 <b>(+412.07%)</b></td><td>765.16 <b>(+118.94%)</b></td><td>303.60 (+3.87%)</td><td>244.20 (+5.03%)</td><td>969.15 <b>(+782.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>485.70 (n/a)</td><td>349.48 (n/a)</td><td>292.30 (n/a)</td><td>232.50 (n/a)</td><td>109.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(-38.35%)</b></td><td>0.04 (-9.00%)</td><td>0.04 (+5.86%)</td><td>0.03 (+1.23%)</td><td>0.01 <b>(-66.45%)</b></td><td>598.20 (-1.22%)</td><td>461.08 (+0.46%)</td><td>427.00 (-5.53%)</td><td>382.90 <b>(+62.25%)</b></td><td>82.86 <b>(-43.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>458.98 (n/a)</td><td>452.00 (n/a)</td><td>236.00 (n/a)</td><td>147.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (-10.57%)</td><td>0.04 (-3.45%)</td><td>0.04 (-3.11%)</td><td>0.03 (-1.65%)</td><td>0.01 <b>(-25.34%)</b></td><td>565.30 (+1.67%)</td><td>423.52 (+0.36%)</td><td>428.30 (+3.23%)</td><td>314.90 (+11.83%)</td><td>104.88 (-19.66%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>422.02 (n/a)</td><td>414.90 (n/a)</td><td>281.60 (n/a)</td><td>130.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (-8.63%)</td><td>0.10 (+14.06%)</td><td>0.11 <b>(+61.90%)</b></td><td>0.05 (-9.52%)</td><td>0.03 (-16.59%)</td><td>597.90 (+10.54%)</td><td>361.58 (-13.56%)</td><td>293.10 <b>(-38.24%)</b></td><td>284.30 (+9.47%)</td><td>134.45 (+1.44%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.90 (n/a)</td><td>418.30 (n/a)</td><td>474.60 (n/a)</td><td>259.70 (n/a)</td><td>132.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+6.23%)</td><td>0.12 (+13.73%)</td><td>0.13 (+16.78%)</td><td>0.05 <b>(-30.83%)</b></td><td>0.04 <b>(+35.65%)</b></td><td>674.60 <b>(+44.58%)</b></td><td>331.92 (-3.04%)</td><td>248.90 (-14.35%)</td><td>226.50 (-5.86%)</td><td>192.74 <b>(+84.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>466.60 (n/a)</td><td>342.34 (n/a)</td><td>290.60 (n/a)</td><td>240.60 (n/a)</td><td>104.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 <b>(-21.27%)</b></td><td>0.08 <b>(-38.78%)</b></td><td>0.08 <b>(-37.97%)</b></td><td>0.03 <b>(-67.77%)</b></td><td>0.04 (+15.53%)</td><td>1362.30 <b>(+210.25%)</b></td><td>643.00 <b>(+98.32%)</b></td><td>488.30 <b>(+61.21%)</b></td><td>294.70 <b>(+27.03%)</b></td><td>416.53 <b>(+388.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>439.10 (n/a)</td><td>324.22 (n/a)</td><td>302.90 (n/a)</td><td>232.00 (n/a)</td><td>85.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 <b>(-23.34%)</b></td><td>0.09 (-12.10%)</td><td>0.11 (-17.36%)</td><td>0.06 <b>(+137.22%)</b></td><td>0.03 <b>(-45.34%)</b></td><td>568.40 <b>(-57.84%)</b></td><td>399.48 <b>(-20.86%)</b></td><td>302.00 <b>(+20.99%)</b></td><td>274.00 <b>(+30.48%)</b></td><td>148.89 <b>(-69.21%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1348.30 (n/a)</td><td>504.78 (n/a)</td><td>249.60 (n/a)</td><td>210.00 (n/a)</td><td>483.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (-7.63%)</td><td>0.10 (+2.33%)</td><td>0.09 (+13.58%)</td><td>0.05 <b>(+74.67%)</b></td><td>0.03 <b>(-30.39%)</b></td><td>746.60 <b>(-42.75%)</b></td><td>471.36 (-19.79%)</td><td>447.10 (-11.97%)</td><td>274.60 (+8.24%)</td><td>171.09 <b>(-58.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1304.00 (n/a)</td><td>587.64 (n/a)</td><td>507.90 (n/a)</td><td>253.70 (n/a)</td><td>416.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+13.34%)</td><td>0.10 (+9.92%)</td><td>0.10 <b>(+26.58%)</b></td><td>0.06 (-2.09%)</td><td>0.03 (+11.86%)</td><td>527.70 (+2.13%)</td><td>349.78 (-7.83%)</td><td>313.60 <b>(-20.99%)</b></td><td>232.00 (-11.79%)</td><td>120.99 (+6.79%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.70 (n/a)</td><td>379.50 (n/a)</td><td>396.90 (n/a)</td><td>263.00 (n/a)</td><td>113.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-14.54%)</td><td>0.09 (-16.42%)</td><td>0.08 (-16.92%)</td><td>0.07 (-6.93%)</td><td>0.03 <b>(-23.49%)</b></td><td>538.90 (+7.46%)</td><td>444.20 (+17.30%)</td><td>480.60 <b>(+20.36%)</b></td><td>282.20 (+17.00%)</td><td>105.52 (-4.29%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.50 (n/a)</td><td>378.70 (n/a)</td><td>399.30 (n/a)</td><td>241.20 (n/a)</td><td>110.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 <b>(+21.28%)</b></td><td>0.11 <b>(+46.85%)</b></td><td>0.13 <b>(+108.28%)</b></td><td>0.05 (-4.06%)</td><td>0.05 <b>(+37.41%)</b></td><td>615.20 (+4.24%)</td><td>351.84 <b>(-27.17%)</b></td><td>260.90 <b>(-51.99%)</b></td><td>200.10 (-17.55%)</td><td>175.42 <b>(+24.78%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.20 (n/a)</td><td>483.12 (n/a)</td><td>543.40 (n/a)</td><td>242.70 (n/a)</td><td>140.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.23 <b>(+45.61%)</b></td><td>0.13 (+18.89%)</td><td>0.13 <b>(+36.49%)</b></td><td>0.06 (-12.90%)</td><td>0.06 <b>(+90.66%)</b></td><td>569.90 (+14.81%)</td><td>355.72 (-4.31%)</td><td>282.00 <b>(-26.73%)</b></td><td>162.60 <b>(-31.33%)</b></td><td>172.14 <b>(+58.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>496.40 (n/a)</td><td>371.76 (n/a)</td><td>384.90 (n/a)</td><td>236.80 (n/a)</td><td>108.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+19.92%)</td><td>0.09 (+14.25%)</td><td>0.08 (+14.68%)</td><td>0.05 (-6.99%)</td><td>0.03 <b>(+21.14%)</b></td><td>638.20 (+7.51%)</td><td>397.88 (-10.60%)</td><td>390.30 (-12.80%)</td><td>237.80 (-16.62%)</td><td>154.65 (+6.44%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>593.60 (n/a)</td><td>445.08 (n/a)</td><td>447.60 (n/a)</td><td>285.20 (n/a)</td><td>145.29 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (+1.21%)</td><td>0.06 (-0.31%)</td><td>0.08 (+1.52%)</td><td>0.04 (-11.10%)</td><td>0.02 (+18.78%)</td><td>574.10 (+12.50%)</td><td>369.56 (+5.16%)</td><td>268.20 (-1.51%)</td><td>238.60 (-1.20%)</td><td>161.65 <b>(+29.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>510.30 (n/a)</td><td>351.42 (n/a)</td><td>272.30 (n/a)</td><td>241.50 (n/a)</td><td>124.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (-1.04%)</td><td>0.06 (-1.79%)</td><td>0.07 (+7.92%)</td><td>0.04 (-17.47%)</td><td>0.02 <b>(+23.64%)</b></td><td>577.00 <b>(+21.17%)</b></td><td>386.84 (+5.46%)</td><td>314.80 (-7.33%)</td><td>278.50 (+1.05%)</td><td>129.10 <b>(+48.24%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>476.20 (n/a)</td><td>366.82 (n/a)</td><td>339.70 (n/a)</td><td>275.60 (n/a)</td><td>87.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (+17.32%)</td><td>0.05 (-1.94%)</td><td>0.04 (-0.50%)</td><td>0.03 <b>(-22.97%)</b></td><td>0.03 <b>(+36.76%)</b></td><td>721.80 <b>(+29.82%)</b></td><td>473.00 (+9.14%)</td><td>482.80 (+0.50%)</td><td>207.30 (-14.80%)</td><td>182.16 <b>(+35.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>556.00 (n/a)</td><td>433.38 (n/a)</td><td>480.40 (n/a)</td><td>243.30 (n/a)</td><td>134.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 <b>(+50.03%)</b></td><td>0.06 <b>(+47.83%)</b></td><td>0.07 <b>(+76.47%)</b></td><td>0.04 (+9.42%)</td><td>0.02 <b>(+166.94%)</b></td><td>576.40 (-8.61%)</td><td>371.40 <b>(-25.95%)</b></td><td>276.60 <b>(-43.32%)</b></td><td>251.80 <b>(-33.35%)</b></td><td>150.86 <b>(+60.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>630.70 (n/a)</td><td>501.56 (n/a)</td><td>488.00 (n/a)</td><td>377.80 (n/a)</td><td>94.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 <b>(+27.12%)</b></td><td>0.06 (+14.61%)</td><td>0.05 (+6.75%)</td><td>0.03 <b>(+195.10%)</b></td><td>0.03 (+4.98%)</td><td>631.40 <b>(-66.11%)</b></td><td>425.70 <b>(-37.18%)</b></td><td>418.50 (-6.31%)</td><td>194.40 <b>(-21.33%)</b></td><td>157.89 <b>(-76.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1863.30 (n/a)</td><td>677.68 (n/a)</td><td>446.70 (n/a)</td><td>247.10 (n/a)</td><td>671.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (-13.34%)</td><td>0.06 (+0.88%)</td><td>0.06 <b>(+52.59%)</b></td><td>0.04 (+5.24%)</td><td>0.02 <b>(-28.53%)</b></td><td>509.20 (-4.98%)</td><td>382.34 (-5.07%)</td><td>315.60 <b>(-34.45%)</b></td><td>285.40 (+15.41%)</td><td>114.78 (-16.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>535.90 (n/a)</td><td>402.78 (n/a)</td><td>481.50 (n/a)</td><td>247.30 (n/a)</td><td>137.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (+0.29%)</td><td>0.07 (+1.30%)</td><td>0.07 (+5.56%)</td><td>0.05 (-11.96%)</td><td>0.02 (+19.63%)</td><td>543.20 (+13.59%)</td><td>396.08 (+2.42%)</td><td>374.00 (-5.27%)</td><td>247.20 (-0.28%)</td><td>132.44 <b>(+39.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>478.20 (n/a)</td><td>386.72 (n/a)</td><td>394.80 (n/a)</td><td>247.90 (n/a)</td><td>94.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (+10.60%)</td><td>0.07 (+7.03%)</td><td>0.06 (+5.58%)</td><td>0.05 <b>(+28.04%)</b></td><td>0.02 (-5.76%)</td><td>462.40 <b>(-21.89%)</b></td><td>361.96 (-9.47%)</td><td>403.30 (-5.28%)</td><td>232.30 (-9.58%)</td><td>91.74 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.00 (n/a)</td><td>399.82 (n/a)</td><td>425.80 (n/a)</td><td>256.90 (n/a)</td><td>134.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (-12.81%)</td><td>0.06 <b>(-24.02%)</b></td><td>0.05 <b>(-39.96%)</b></td><td>0.04 (-11.75%)</td><td>0.02 (-17.01%)</td><td>591.00 (+13.33%)</td><td>468.70 <b>(+28.70%)</b></td><td>534.70 <b>(+66.52%)</b></td><td>244.30 (+14.69%)</td><td>137.21 (-2.82%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>521.50 (n/a)</td><td>364.18 (n/a)</td><td>321.10 (n/a)</td><td>213.00 (n/a)</td><td>141.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (+4.98%)</td><td>0.07 (-1.36%)</td><td>0.06 <b>(-24.18%)</b></td><td>0.05 <b>(+409.13%)</b></td><td>0.02 <b>(-43.97%)</b></td><td>484.20 <b>(-80.36%)</b></td><td>395.94 <b>(-46.63%)</b></td><td>401.00 <b>(+31.86%)</b></td><td>254.60 (-4.75%)</td><td>93.46 <b>(-90.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2465.40 (n/a)</td><td>741.92 (n/a)</td><td>304.10 (n/a)</td><td>267.30 (n/a)</td><td>964.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (+2.87%)</td><td>0.08 (+19.41%)</td><td>0.07 (-0.27%)</td><td>0.05 <b>(+273.77%)</b></td><td>0.02 <b>(-26.46%)</b></td><td>495.50 <b>(-73.25%)</b></td><td>357.10 <b>(-45.02%)</b></td><td>327.90 (+0.28%)</td><td>240.90 (-2.78%)</td><td>119.59 <b>(-82.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1852.20 (n/a)</td><td>649.46 (n/a)</td><td>327.00 (n/a)</td><td>247.80 (n/a)</td><td>679.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (-12.97%)</td><td>0.05 <b>(-33.83%)</b></td><td>0.04 <b>(-48.60%)</b></td><td>0.04 <b>(-26.35%)</b></td><td>0.02 (+9.03%)</td><td>611.80 <b>(+35.77%)</b></td><td>495.16 <b>(+56.35%)</b></td><td>560.30 <b>(+94.55%)</b></td><td>286.70 (+14.91%)</td><td>133.84 <b>(+65.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>450.60 (n/a)</td><td>316.70 (n/a)</td><td>288.00 (n/a)</td><td>249.50 (n/a)</td><td>80.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 <b>(+50.68%)</b></td><td>0.07 <b>(+32.06%)</b></td><td>0.06 <b>(+34.70%)</b></td><td>0.04 (+15.51%)</td><td>0.02 <b>(+44.94%)</b></td><td>464.90 (-13.43%)</td><td>306.42 <b>(-23.10%)</b></td><td>303.50 <b>(-25.76%)</b></td><td>182.00 <b>(-33.63%)</b></td><td>105.43 (-13.53%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.00 (n/a)</td><td>398.44 (n/a)</td><td>408.80 (n/a)</td><td>274.20 (n/a)</td><td>121.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (+9.25%)</td><td>0.04 (-14.49%)</td><td>0.04 <b>(-29.21%)</b></td><td>0.01 <b>(-66.07%)</b></td><td>0.03 <b>(+39.44%)</b></td><td>1881.60 <b>(+194.74%)</b></td><td>680.86 <b>(+71.23%)</b></td><td>429.30 <b>(+41.26%)</b></td><td>249.40 (-8.48%)</td><td>681.96 <b>(+314.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.40 (n/a)</td><td>397.64 (n/a)</td><td>303.90 (n/a)</td><td>272.50 (n/a)</td><td>164.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 <b>(-32.72%)</b></td><td>0.03 <b>(-31.76%)</b></td><td>0.03 <b>(-30.81%)</b></td><td>0.02 <b>(-34.23%)</b></td><td>0.01 <b>(-45.01%)</b></td><td>884.60 <b>(+52.05%)</b></td><td>575.06 <b>(+43.08%)</b></td><td>537.30 <b>(+44.55%)</b></td><td>402.50 <b>(+48.63%)</b></td><td>182.03 <b>(+34.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.80 (n/a)</td><td>401.92 (n/a)</td><td>371.70 (n/a)</td><td>270.80 (n/a)</td><td>135.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (+15.70%)</td><td>0.06 <b>(+23.08%)</b></td><td>0.06 <b>(+42.27%)</b></td><td>0.03 (+1.35%)</td><td>0.02 <b>(+42.98%)</b></td><td>555.50 (-1.33%)</td><td>374.98 (-13.89%)</td><td>301.70 <b>(-29.71%)</b></td><td>228.40 (-13.58%)</td><td>149.80 <b>(+34.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>435.46 (n/a)</td><td>429.20 (n/a)</td><td>264.30 (n/a)</td><td>111.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 <b>(-27.87%)</b></td><td>0.05 <b>(-27.94%)</b></td><td>0.04 <b>(-38.42%)</b></td><td>0.04 (-7.09%)</td><td>0.01 <b>(-31.86%)</b></td><td>490.90 (+7.63%)</td><td>394.98 <b>(+35.46%)</b></td><td>444.90 <b>(+62.43%)</b></td><td>261.50 <b>(+38.65%)</b></td><td>98.50 (-1.49%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>456.10 (n/a)</td><td>291.58 (n/a)</td><td>273.90 (n/a)</td><td>188.60 (n/a)</td><td>99.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 <b>(+37.75%)</b></td><td>0.05 (+7.97%)</td><td>0.04 (-13.29%)</td><td>0.04 <b>(+59.06%)</b></td><td>0.02 <b>(+32.03%)</b></td><td>506.20 <b>(-37.13%)</b></td><td>430.48 (-9.60%)</td><td>480.10 (+15.33%)</td><td>213.20 <b>(-27.41%)</b></td><td>122.94 <b>(-41.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>805.20 (n/a)</td><td>476.20 (n/a)</td><td>416.30 (n/a)</td><td>293.70 (n/a)</td><td>208.44 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.34 (-1.17%)</td><td>0.27 (+4.22%)</td><td>0.33 (+3.47%)</td><td>0.17 <b>(+42.76%)</b></td><td>0.09 (-16.00%)</td><td>585.60 <b>(-29.95%)</b></td><td>407.42 (-11.65%)</td><td>300.40 (-3.35%)</td><td>286.00 (+1.17%)</td><td>156.43 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>836.00 (n/a)</td><td>461.16 (n/a)</td><td>310.80 (n/a)</td><td>282.70 (n/a)</td><td>245.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.48 <b>(+21.31%)</b></td><td>0.30 (+14.58%)</td><td>0.27 <b>(+20.14%)</b></td><td>0.16 <b>(+20.67%)</b></td><td>0.14 <b>(+26.27%)</b></td><td>626.30 (-17.13%)</td><td>391.08 (-10.71%)</td><td>364.50 (-16.76%)</td><td>206.70 (-17.55%)</td><td>183.10 (-10.55%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>755.80 (n/a)</td><td>437.98 (n/a)</td><td>437.90 (n/a)</td><td>250.70 (n/a)</td><td>204.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.35 (-12.10%)</td><td>0.26 (+2.65%)</td><td>0.27 (+12.27%)</td><td>0.16 (-12.69%)</td><td>0.08 (-9.97%)</td><td>617.90 (+14.53%)</td><td>407.34 (-2.13%)</td><td>364.60 (-10.94%)</td><td>279.90 (+13.78%)</td><td>137.99 (+17.27%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>539.50 (n/a)</td><td>416.22 (n/a)</td><td>409.40 (n/a)</td><td>246.00 (n/a)</td><td>117.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.30 (-4.77%)</td><td>0.23 (+7.00%)</td><td>0.25 <b>(+36.99%)</b></td><td>0.15 (+4.19%)</td><td>0.07 (-2.32%)</td><td>478.10 (-4.02%)</td><td>346.20 (-6.47%)</td><td>289.90 <b>(-27.00%)</b></td><td>245.20 (+5.01%)</td><td>113.19 (+2.24%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>498.10 (n/a)</td><td>370.14 (n/a)</td><td>397.10 (n/a)</td><td>233.50 (n/a)</td><td>110.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 <b>(-41.07%)</b></td><td>0.16 <b>(-27.68%)</b></td><td>0.16 <b>(-36.66%)</b></td><td>0.15 <b>(+27.31%)</b></td><td>0.01 <b>(-82.95%)</b></td><td>492.30 <b>(-21.46%)</b></td><td>450.42 <b>(+20.14%)</b></td><td>457.20 <b>(+57.87%)</b></td><td>402.40 <b>(+69.72%)</b></td><td>39.97 <b>(-76.61%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>626.80 (n/a)</td><td>374.92 (n/a)</td><td>289.60 (n/a)</td><td>237.10 (n/a)</td><td>170.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.27 (-10.31%)</td><td>0.19 (-13.72%)</td><td>0.16 <b>(-37.40%)</b></td><td>0.13 (-1.09%)</td><td>0.06 <b>(-20.49%)</b></td><td>551.00 (+1.10%)</td><td>418.78 (+12.26%)</td><td>466.20 <b>(+59.77%)</b></td><td>272.10 (+11.47%)</td><td>116.08 (-15.04%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>545.00 (n/a)</td><td>373.06 (n/a)</td><td>291.80 (n/a)</td><td>244.10 (n/a)</td><td>136.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-14.30%)</td><td>0.10 (-12.33%)</td><td>0.13 (+8.91%)</td><td>0.06 (-16.06%)</td><td>0.04 (+8.00%)</td><td>618.40 (+19.13%)</td><td>401.72 (+19.08%)</td><td>293.80 (-8.19%)</td><td>279.50 (+16.70%)</td><td>162.45 <b>(+45.27%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>519.10 (n/a)</td><td>337.36 (n/a)</td><td>320.00 (n/a)</td><td>239.50 (n/a)</td><td>111.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 <b>(-27.22%)</b></td><td>0.10 (-2.44%)</td><td>0.09 (+10.73%)</td><td>0.08 <b>(+27.99%)</b></td><td>0.02 <b>(-56.33%)</b></td><td>439.90 <b>(-21.87%)</b></td><td>379.70 (-8.29%)</td><td>420.50 (-9.71%)</td><td>287.40 <b>(+37.45%)</b></td><td>71.78 <b>(-53.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>563.00 (n/a)</td><td>414.00 (n/a)</td><td>465.70 (n/a)</td><td>209.10 (n/a)</td><td>153.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (+1.46%)</td><td>0.12 (+6.16%)</td><td>0.13 (+2.16%)</td><td>0.08 (+6.87%)</td><td>0.03 (-1.00%)</td><td>467.10 (-6.43%)</td><td>324.58 (-6.69%)</td><td>282.20 (-2.12%)</td><td>241.60 (-1.43%)</td><td>98.38 (-11.83%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.20 (n/a)</td><td>347.84 (n/a)</td><td>288.30 (n/a)</td><td>245.10 (n/a)</td><td>111.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 <b>(-50.60%)</b></td><td>0.05 <b>(-53.95%)</b></td><td>0.07 <b>(-47.01%)</b></td><td>0.02 <b>(-75.84%)</b></td><td>0.02 <b>(-33.96%)</b></td><td>2087.50 <b>(+313.94%)</b></td><td>907.64 <b>(+165.90%)</b></td><td>537.30 <b>(+88.72%)</b></td><td>487.20 <b>(+102.41%)</b></td><td>679.41 <b>(+467.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>504.30 (n/a)</td><td>341.34 (n/a)</td><td>284.70 (n/a)</td><td>240.70 (n/a)</td><td>119.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 <b>(+35.01%)</b></td><td>0.12 (+19.37%)</td><td>0.08 (+18.68%)</td><td>0.07 (+5.26%)</td><td>0.06 <b>(+42.76%)</b></td><td>519.80 (-4.99%)</td><td>375.48 (-12.47%)</td><td>444.90 (-15.74%)</td><td>181.00 <b>(-25.94%)</b></td><td>150.41 (-1.49%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>547.10 (n/a)</td><td>428.98 (n/a)</td><td>528.00 (n/a)</td><td>244.40 (n/a)</td><td>152.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (-7.77%)</td><td>0.11 (-11.74%)</td><td>0.13 (+8.32%)</td><td>0.06 (-10.07%)</td><td>0.04 <b>(+21.50%)</b></td><td>628.00 (+11.19%)</td><td>400.60 <b>(+20.16%)</b></td><td>278.50 (-7.66%)</td><td>261.70 (+8.45%)</td><td>180.97 <b>(+36.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>564.80 (n/a)</td><td>333.40 (n/a)</td><td>301.60 (n/a)</td><td>241.30 (n/a)</td><td>132.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (-9.07%)</td><td>0.11 (-15.35%)</td><td>0.11 (-16.27%)</td><td>0.07 (-19.53%)</td><td>0.03 (-0.12%)</td><td>571.00 <b>(+24.27%)</b></td><td>408.76 <b>(+20.64%)</b></td><td>382.00 (+19.41%)</td><td>275.70 (+9.97%)</td><td>127.21 <b>(+39.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>459.50 (n/a)</td><td>338.82 (n/a)</td><td>319.90 (n/a)</td><td>250.70 (n/a)</td><td>91.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (+14.00%)</td><td>0.12 (-4.89%)</td><td>0.10 <b>(-30.43%)</b></td><td>0.09 (+4.47%)</td><td>0.04 <b>(+21.80%)</b></td><td>473.10 (-4.27%)</td><td>379.22 (+6.90%)</td><td>429.90 <b>(+43.73%)</b></td><td>223.50 (-12.28%)</td><td>111.25 (+3.43%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>494.20 (n/a)</td><td>354.74 (n/a)</td><td>299.10 (n/a)</td><td>254.80 (n/a)</td><td>107.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (-14.55%)</td><td>0.11 (-15.62%)</td><td>0.12 (-13.81%)</td><td>0.06 (-10.92%)</td><td>0.05 (-19.39%)</td><td>632.10 (+12.27%)</td><td>408.58 (+16.26%)</td><td>338.60 (+16.04%)</td><td>233.50 (+17.04%)</td><td>168.43 (+7.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>563.00 (n/a)</td><td>351.44 (n/a)</td><td>291.80 (n/a)</td><td>199.50 (n/a)</td><td>156.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 (-5.35%)</td><td>0.10 (-10.90%)</td><td>0.08 <b>(-24.28%)</b></td><td>0.07 (-8.42%)</td><td>0.04 (+3.75%)</td><td>604.00 (+9.18%)</td><td>448.48 (+15.15%)</td><td>491.00 <b>(+32.10%)</b></td><td>261.50 (+5.66%)</td><td>166.47 <b>(+20.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>553.20 (n/a)</td><td>389.48 (n/a)</td><td>371.70 (n/a)</td><td>247.50 (n/a)</td><td>137.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (-6.73%)</td><td>0.12 (+2.53%)</td><td>0.15 <b>(+52.26%)</b></td><td>0.05 <b>(-29.84%)</b></td><td>0.05 <b>(+23.72%)</b></td><td>799.60 <b>(+42.53%)</b></td><td>433.12 (+8.27%)</td><td>282.10 <b>(-34.32%)</b></td><td>266.80 (+7.19%)</td><td>236.41 <b>(+82.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>561.00 (n/a)</td><td>400.04 (n/a)</td><td>429.50 (n/a)</td><td>248.90 (n/a)</td><td>129.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.17 <b>(+44.50%)</b></td><td>0.10 (+13.87%)</td><td>0.12 (+14.07%)</td><td>0.02 <b>(-46.59%)</b></td><td>0.06 <b>(+93.36%)</b></td><td>1886.50 <b>(+87.25%)</b></td><td>670.28 <b>(+29.23%)</b></td><td>333.90 (-12.34%)</td><td>246.50 <b>(-30.80%)</b></td><td>693.60 <b>(+150.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>1007.50 (n/a)</td><td>518.68 (n/a)</td><td>380.90 (n/a)</td><td>356.20 (n/a)</td><td>276.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (-4.76%)</td><td>0.11 (+4.72%)</td><td>0.11 (+18.96%)</td><td>0.08 (+1.28%)</td><td>0.02 <b>(-27.22%)</b></td><td>428.20 (-1.27%)</td><td>317.84 (-7.22%)</td><td>307.00 (-15.94%)</td><td>241.80 (+4.99%)</td><td>70.04 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>433.70 (n/a)</td><td>342.58 (n/a)</td><td>365.20 (n/a)</td><td>230.30 (n/a)</td><td>92.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (+5.65%)</td><td>0.11 (+15.66%)</td><td>0.12 <b>(+25.79%)</b></td><td>0.07 (+16.59%)</td><td>0.03 (-8.37%)</td><td>531.90 (-14.24%)</td><td>329.00 (-15.60%)</td><td>292.70 <b>(-20.51%)</b></td><td>249.20 (-5.36%)</td><td>115.96 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>620.20 (n/a)</td><td>389.80 (n/a)</td><td>368.20 (n/a)</td><td>263.30 (n/a)</td><td>145.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (+3.99%)</td><td>0.11 (+10.81%)</td><td>0.11 <b>(+36.37%)</b></td><td>0.07 (-2.93%)</td><td>0.04 (+17.64%)</td><td>532.90 (+3.02%)</td><td>360.54 (-7.38%)</td><td>323.50 <b>(-26.68%)</b></td><td>239.30 (-3.86%)</td><td>130.80 (+15.88%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>517.30 (n/a)</td><td>389.26 (n/a)</td><td>441.20 (n/a)</td><td>248.90 (n/a)</td><td>112.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 <b>(-22.03%)</b></td><td>0.08 <b>(-21.03%)</b></td><td>0.07 <b>(-41.42%)</b></td><td>0.06 (+6.79%)</td><td>0.03 <b>(-27.55%)</b></td><td>594.70 (-6.36%)</td><td>460.38 <b>(+21.27%)</b></td><td>524.30 <b>(+70.73%)</b></td><td>314.30 <b>(+28.23%)</b></td><td>130.45 (-17.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.10 (n/a)</td><td>379.64 (n/a)</td><td>307.10 (n/a)</td><td>245.10 (n/a)</td><td>158.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-5.24%)</td><td>0.10 <b>(+20.90%)</b></td><td>0.10 <b>(+46.98%)</b></td><td>0.06 (+2.49%)</td><td>0.03 (-12.58%)</td><td>550.50 (-2.43%)</td><td>379.16 (-18.40%)</td><td>334.60 <b>(-31.95%)</b></td><td>278.10 (+5.54%)</td><td>112.41 (-6.51%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>564.20 (n/a)</td><td>464.68 (n/a)</td><td>491.70 (n/a)</td><td>263.50 (n/a)</td><td>120.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (+4.26%)</td><td>0.09 <b>(+38.53%)</b></td><td>0.08 (+18.95%)</td><td>0.06 <b>(+230.26%)</b></td><td>0.04 (-19.73%)</td><td>571.40 <b>(-69.72%)</b></td><td>426.04 <b>(-49.34%)</b></td><td>464.20 (-15.92%)</td><td>266.10 (-4.07%)</td><td>149.38 <b>(-77.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1887.20 (n/a)</td><td>841.04 (n/a)</td><td>552.10 (n/a)</td><td>277.40 (n/a)</td><td>667.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.40 <b>(-33.02%)</b></td><td>0.25 (-18.60%)</td><td>0.23 (-0.06%)</td><td>0.05 <b>(-74.02%)</b></td><td>0.14 (-16.36%)</td><td>2437.70 <b>(+284.98%)</b></td><td>866.70 <b>(+75.11%)</b></td><td>561.90 (+0.05%)</td><td>329.10 <b>(+49.32%)</b></td><td>887.56 <b>(+452.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.59 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>633.20 (n/a)</td><td>494.96 (n/a)</td><td>561.60 (n/a)</td><td>220.40 (n/a)</td><td>160.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.40 <b>(-27.92%)</b></td><td>0.29 <b>(-20.26%)</b></td><td>0.26 <b>(-29.88%)</b></td><td>0.19 <b>(+50.04%)</b></td><td>0.09 <b>(-45.44%)</b></td><td>686.90 <b>(-33.35%)</b></td><td>487.86 (+4.42%)</td><td>504.80 <b>(+42.64%)</b></td><td>324.30 <b>(+38.71%)</b></td><td>146.81 <b>(-54.55%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>1030.60 (n/a)</td><td>467.20 (n/a)</td><td>353.90 (n/a)</td><td>233.80 (n/a)</td><td>323.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (+0.45%)</td><td>0.33 (+5.26%)</td><td>0.27 (+2.02%)</td><td>0.24 <b>(+34.39%)</b></td><td>0.11 (-12.81%)</td><td>544.00 <b>(-25.59%)</b></td><td>433.16 (-9.68%)</td><td>477.90 (-1.97%)</td><td>261.60 (-0.46%)</td><td>127.48 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.50 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>731.10 (n/a)</td><td>479.56 (n/a)</td><td>487.50 (n/a)</td><td>262.80 (n/a)</td><td>187.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 <b>(+25.24%)</b></td><td>0.01 <b>(+36.02%)</b></td><td>0.02 <b>(+84.07%)</b></td><td>0.01 <b>(+28.62%)</b></td><td>0.01 <b>(+32.58%)</b></td><td>511.50 <b>(-22.24%)</b></td><td>314.08 <b>(-25.49%)</b></td><td>242.50 <b>(-45.68%)</b></td><td>207.10 <b>(-20.16%)</b></td><td>131.86 (-16.39%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>657.80 (n/a)</td><td>421.50 (n/a)</td><td>446.40 (n/a)</td><td>259.40 (n/a)</td><td>157.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (+10.80%)</td><td>0.02 (+1.81%)</td><td>0.02 (+0.42%)</td><td>0.01 (-10.33%)</td><td>0.00 <b>(+81.44%)</b></td><td>344.70 (+11.52%)</td><td>262.46 (+0.14%)</td><td>256.30 (-0.39%)</td><td>213.50 (-9.76%)</td><td>51.67 <b>(+81.57%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>309.10 (n/a)</td><td>262.08 (n/a)</td><td>257.30 (n/a)</td><td>236.60 (n/a)</td><td>28.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 <b>(-25.33%)</b></td><td>0.01 (-18.21%)</td><td>0.01 (+2.61%)</td><td>0.01 <b>(-39.35%)</b></td><td>0.00 (-1.42%)</td><td>773.70 <b>(+64.90%)</b></td><td>486.72 <b>(+32.77%)</b></td><td>379.00 (-2.52%)</td><td>295.00 <b>(+33.91%)</b></td><td>226.95 <b>(+109.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.20 (n/a)</td><td>366.58 (n/a)</td><td>388.80 (n/a)</td><td>220.30 (n/a)</td><td>108.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.73 (+5.33%)</td><td>6.35 (-17.11%)</td><td>5.05 <b>(-36.41%)</b></td><td>3.57 <b>(-39.61%)</b></td><td>2.81 <b>(+123.06%)</b></td><td>587.00 <b>(+65.59%)</b></td><td>385.22 <b>(+37.56%)</b></td><td>415.20 <b>(+57.27%)</b></td><td>215.70 (-5.06%)</td><td>159.35 <b>(+225.28%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.23 (n/a)</td><td>7.67 (n/a)</td><td>7.95 (n/a)</td><td>5.92 (n/a)</td><td>1.26 (n/a)</td><td>354.50 (n/a)</td><td>280.04 (n/a)</td><td>264.00 (n/a)</td><td>227.20 (n/a)</td><td>48.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (-1.27%)</td><td>0.36 (-18.00%)</td><td>0.28 <b>(-35.08%)</b></td><td>0.24 <b>(-37.91%)</b></td><td>0.12 <b>(+137.80%)</b></td><td>555.20 <b>(+61.07%)</b></td><td>407.24 <b>(+32.36%)</b></td><td>471.10 <b>(+54.05%)</b></td><td>262.50 (+1.27%)</td><td>130.60 <b>(+263.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.05 (n/a)</td><td>344.70 (n/a)</td><td>307.68 (n/a)</td><td>305.80 (n/a)</td><td>259.20 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.51 (-2.96%)</td><td>0.39 (-4.48%)</td><td>0.46 (-0.41%)</td><td>0.25 (-8.53%)</td><td>0.13 (-0.28%)</td><td>536.10 (+9.34%)</td><td>372.96 (+5.85%)</td><td>285.70 (+0.39%)</td><td>259.10 (+3.06%)</td><td>139.20 (+12.52%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>490.30 (n/a)</td><td>352.36 (n/a)</td><td>284.60 (n/a)</td><td>251.40 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.45 <b>(-20.31%)</b></td><td>0.37 (-19.23%)</td><td>0.34 <b>(-29.90%)</b></td><td>0.31 (-1.69%)</td><td>0.07 <b>(-25.13%)</b></td><td>424.10 (+1.73%)</td><td>364.14 <b>(+22.34%)</b></td><td>392.40 <b>(+42.64%)</b></td><td>296.30 <b>(+25.44%)</b></td><td>62.72 (-10.47%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>416.90 (n/a)</td><td>297.64 (n/a)</td><td>275.10 (n/a)</td><td>236.20 (n/a)</td><td>70.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.47 <b>(-21.24%)</b></td><td>0.31 <b>(-39.05%)</b></td><td>0.26 <b>(-46.59%)</b></td><td>0.25 <b>(-45.36%)</b></td><td>0.09 <b>(+69.28%)</b></td><td>524.50 <b>(+83.01%)</b></td><td>451.46 <b>(+71.57%)</b></td><td>499.20 <b>(+87.18%)</b></td><td>282.70 <b>(+27.00%)</b></td><td>99.77 <b>(+285.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.59 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.05 (n/a)</td><td>286.60 (n/a)</td><td>263.14 (n/a)</td><td>266.70 (n/a)</td><td>222.60 (n/a)</td><td>25.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.54 (-13.80%)</td><td>0.35 <b>(-23.26%)</b></td><td>0.30 <b>(-26.55%)</b></td><td>0.28 (-10.82%)</td><td>0.11 (-17.92%)</td><td>474.20 (+12.13%)</td><td>404.92 <b>(+29.19%)</b></td><td>446.60 <b>(+36.16%)</b></td><td>245.20 (+15.99%)</td><td>92.29 (+4.87%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.62 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.13 (n/a)</td><td>422.90 (n/a)</td><td>313.44 (n/a)</td><td>328.00 (n/a)</td><td>211.40 (n/a)</td><td>88.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-9.98%)</td><td>0.01 (-13.93%)</td><td>0.01 (-7.95%)</td><td>0.01 (-2.15%)</td><td>0.00 (+6.31%)</td><td>505.80 (+2.20%)</td><td>370.82 (+17.83%)</td><td>300.80 (+8.63%)</td><td>275.30 (+11.10%)</td><td>117.68 (+15.75%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.90 (n/a)</td><td>314.72 (n/a)</td><td>276.90 (n/a)</td><td>247.80 (n/a)</td><td>101.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (-18.87%)</td><td>0.01 (-12.67%)</td><td>0.01 (+0.95%)</td><td>0.01 (-6.72%)</td><td>0.00 <b>(-33.56%)</b></td><td>602.00 (+7.19%)</td><td>434.94 (+10.26%)</td><td>386.40 (-0.95%)</td><td>308.00 <b>(+23.25%)</b></td><td>122.55 (-9.23%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.60 (n/a)</td><td>394.48 (n/a)</td><td>390.10 (n/a)</td><td>249.90 (n/a)</td><td>135.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.00 (+0.00%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+2.20%)</td><td>18036.68 (-5.01%)</td><td>12717.04 (+4.09%)</td><td>16161.26 <b>(+62.15%)</b></td><td>6241.55 (+9.41%)</td><td>5651.63 (-1.35%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18987.08 (n/a)</td><td>12217.26 (n/a)</td><td>9966.58 (n/a)</td><td>5704.51 (n/a)</td><td>5729.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.00 (+7.69%)</td><td>0.00 <b>(+58.62%)</b></td><td>0.00 <b>(+175.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+20.95%)</b></td><td>20911.92 (-2.50%)</td><td>11844.85 <b>(-30.27%)</b></td><td>7335.13 <b>(-61.12%)</b></td><td>5834.34 (-6.31%)</td><td>7351.38 <b>(+20.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21447.14 (n/a)</td><td>16986.69 (n/a)</td><td>18864.81 (n/a)</td><td>6226.98 (n/a)</td><td>6119.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (+3.66%)</td><td>0.10 (+0.76%)</td><td>0.08 (-0.92%)</td><td>0.07 (-1.70%)</td><td>0.04 (+2.74%)</td><td>30219.41 (+1.78%)</td><td>23255.75 (-0.37%)</td><td>27922.02 (+0.95%)</td><td>14255.48 (-3.56%)</td><td>7835.57 (+1.07%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>29690.55 (n/a)</td><td>23341.72 (n/a)</td><td>27660.49 (n/a)</td><td>14781.02 (n/a)</td><td>7752.70 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.11 (+9.97%)</td><td>1.67 (-5.17%)</td><td>2.16 <b>(+30.11%)</b></td><td>0.30 (+0.71%)</td><td>1.20 <b>(+21.86%)</b></td><td>3498.10 (-0.70%)</td><td>1341.00 (+19.02%)</td><td>486.10 <b>(-23.13%)</b></td><td>337.20 (-9.06%)</td><td>1367.49 (+1.58%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.83 (n/a)</td><td>1.76 (n/a)</td><td>1.66 (n/a)</td><td>0.30 (n/a)</td><td>0.99 (n/a)</td><td>3522.90 (n/a)</td><td>1126.68 (n/a)</td><td>632.40 (n/a)</td><td>370.80 (n/a)</td><td>1346.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>2.72 (-5.32%)</td><td>1.79 (-2.96%)</td><td>1.83 (+9.94%)</td><td>1.17 (+0.84%)</td><td>0.64 (+0.92%)</td><td>893.10 (-0.83%)</td><td>648.00 (+4.66%)</td><td>572.10 (-9.05%)</td><td>385.80 (+5.61%)</td><td>222.03 (+15.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (n/a)</td><td>1.84 (n/a)</td><td>1.67 (n/a)</td><td>1.16 (n/a)</td><td>0.63 (n/a)</td><td>900.60 (n/a)</td><td>619.16 (n/a)</td><td>629.00 (n/a)</td><td>365.30 (n/a)</td><td>192.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.99 (+9.71%)</td><td>2.12 (-4.91%)</td><td>1.77 (+3.04%)</td><td>1.37 (-15.11%)</td><td>1.06 <b>(+22.60%)</b></td><td>763.90 (+17.79%)</td><td>569.26 (+9.44%)</td><td>590.80 (-2.96%)</td><td>263.00 (-8.87%)</td><td>188.68 (+18.52%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.63 (n/a)</td><td>2.22 (n/a)</td><td>1.72 (n/a)</td><td>1.62 (n/a)</td><td>0.87 (n/a)</td><td>648.50 (n/a)</td><td>520.18 (n/a)</td><td>608.80 (n/a)</td><td>288.60 (n/a)</td><td>159.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.20 (-4.35%)</td><td>2.02 (+1.57%)</td><td>2.01 (+13.57%)</td><td>1.35 (+14.36%)</td><td>0.74 (-9.77%)</td><td>777.00 (-12.55%)</td><td>569.10 (-3.57%)</td><td>522.10 (-11.96%)</td><td>327.30 (+4.54%)</td><td>180.13 (-12.93%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.35 (n/a)</td><td>1.99 (n/a)</td><td>1.77 (n/a)</td><td>1.18 (n/a)</td><td>0.81 (n/a)</td><td>888.50 (n/a)</td><td>590.16 (n/a)</td><td>593.00 (n/a)</td><td>313.10 (n/a)</td><td>206.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.06 (-2.35%)</td><td>2.26 (+2.12%)</td><td>2.62 (+12.85%)</td><td>0.30 (+0.91%)</td><td>1.40 (-0.15%)</td><td>3480.00 (-0.91%)</td><td>1035.58 (-1.15%)</td><td>399.70 (-11.39%)</td><td>258.30 (+2.38%)</td><td>1373.91 (-0.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.16 (n/a)</td><td>2.21 (n/a)</td><td>2.32 (n/a)</td><td>0.30 (n/a)</td><td>1.40 (n/a)</td><td>3511.80 (n/a)</td><td>1047.58 (n/a)</td><td>451.10 (n/a)</td><td>252.30 (n/a)</td><td>1383.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.00 <b>(-20.24%)</b></td><td>2.12 (-0.61%)</td><td>1.78 (-1.19%)</td><td>1.26 (-19.13%)</td><td>0.76 (-17.59%)</td><td>835.20 <b>(+23.66%)</b></td><td>549.46 (+1.09%)</td><td>588.30 (+1.20%)</td><td>349.00 <b>(+25.36%)</b></td><td>198.89 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.77 (n/a)</td><td>2.13 (n/a)</td><td>1.80 (n/a)</td><td>1.55 (n/a)</td><td>0.92 (n/a)</td><td>675.40 (n/a)</td><td>543.54 (n/a)</td><td>581.30 (n/a)</td><td>278.40 (n/a)</td><td>153.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.85 (-10.01%)</td><td>2.65 (+0.97%)</td><td>2.62 <b>(+36.08%)</b></td><td>1.46 (-14.44%)</td><td>0.92 <b>(-20.61%)</b></td><td>720.50 (+16.87%)</td><td>441.30 (-3.61%)</td><td>399.70 <b>(-26.51%)</b></td><td>272.10 (+11.11%)</td><td>174.98 (+3.17%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.28 (n/a)</td><td>2.63 (n/a)</td><td>1.93 (n/a)</td><td>1.70 (n/a)</td><td>1.16 (n/a)</td><td>616.50 (n/a)</td><td>457.84 (n/a)</td><td>543.90 (n/a)</td><td>244.90 (n/a)</td><td>169.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.42 (+15.72%)</td><td>2.00 (-15.76%)</td><td>1.92 (-16.79%)</td><td>0.30 <b>(-83.18%)</b></td><td>1.19 <b>(+164.52%)</b></td><td>3483.00 <b>(+494.67%)</b></td><td>1075.72 <b>(+136.07%)</b></td><td>546.40 <b>(+20.19%)</b></td><td>307.00 (-13.57%)</td><td>1352.93 <b>(+1418.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.95 (n/a)</td><td>2.37 (n/a)</td><td>2.31 (n/a)</td><td>1.79 (n/a)</td><td>0.45 (n/a)</td><td>585.70 (n/a)</td><td>455.68 (n/a)</td><td>454.60 (n/a)</td><td>355.20 (n/a)</td><td>89.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.22 (+13.21%)</td><td>3.10 <b>(+30.80%)</b></td><td>3.47 (+14.61%)</td><td>1.55 <b>(+159.30%)</b></td><td>1.01 <b>(-27.55%)</b></td><td>1353.60 <b>(-61.44%)</b></td><td>763.30 <b>(-47.02%)</b></td><td>604.90 (-12.75%)</td><td>497.20 (-11.67%)</td><td>343.89 <b>(-72.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.73 (n/a)</td><td>2.37 (n/a)</td><td>3.02 (n/a)</td><td>0.60 (n/a)</td><td>1.40 (n/a)</td><td>3510.00 (n/a)</td><td>1440.80 (n/a)</td><td>693.30 (n/a)</td><td>562.90 (n/a)</td><td>1265.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.27 (+5.01%)</td><td>2.38 (-0.41%)</td><td>2.30 <b>(-23.02%)</b></td><td>0.85 <b>(+44.01%)</b></td><td>1.22 <b>(-27.53%)</b></td><td>2480.30 <b>(-30.56%)</b></td><td>1151.68 <b>(-35.14%)</b></td><td>912.40 <b>(+29.90%)</b></td><td>491.60 (-4.77%)</td><td>766.82 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.06 (n/a)</td><td>2.39 (n/a)</td><td>2.99 (n/a)</td><td>0.59 (n/a)</td><td>1.69 (n/a)</td><td>3572.00 (n/a)</td><td>1775.74 (n/a)</td><td>702.40 (n/a)</td><td>516.20 (n/a)</td><td>1618.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.65 (-2.74%)</td><td>3.82 <b>(+50.64%)</b></td><td>3.97 <b>(+62.14%)</b></td><td>0.59 (-0.95%)</td><td>2.04 (-4.91%)</td><td>3568.80 (+0.96%)</td><td>1092.84 <b>(-36.30%)</b></td><td>528.10 <b>(-38.32%)</b></td><td>371.30 (+2.82%)</td><td>1387.73 (-7.90%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.81 (n/a)</td><td>2.53 (n/a)</td><td>2.45 (n/a)</td><td>0.59 (n/a)</td><td>2.14 (n/a)</td><td>3535.00 (n/a)</td><td>1715.62 (n/a)</td><td>856.20 (n/a)</td><td>361.10 (n/a)</td><td>1506.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.35 <b>(+62.04%)</b></td><td>3.73 <b>(+74.69%)</b></td><td>3.84 <b>(+33.01%)</b></td><td>1.65 <b>(+179.02%)</b></td><td>1.65 (+16.55%)</td><td>1269.90 <b>(-64.16%)</b></td><td>687.54 <b>(-61.85%)</b></td><td>545.90 <b>(-24.82%)</b></td><td>392.20 <b>(-38.29%)</b></td><td>371.48 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.30 (n/a)</td><td>2.13 (n/a)</td><td>2.89 (n/a)</td><td>0.59 (n/a)</td><td>1.41 (n/a)</td><td>3543.40 (n/a)</td><td>1802.06 (n/a)</td><td>726.10 (n/a)</td><td>635.60 (n/a)</td><td>1555.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.83 <b>(+20.34%)</b></td><td>3.27 (+3.34%)</td><td>3.09 (-12.52%)</td><td>0.58 <b>(-30.41%)</b></td><td>1.88 <b>(+26.92%)</b></td><td>3602.80 <b>(+43.69%)</b></td><td>1176.04 <b>(+21.87%)</b></td><td>677.90 (+14.32%)</td><td>359.50 (-16.90%)</td><td>1362.88 <b>(+56.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.85 (n/a)</td><td>3.16 (n/a)</td><td>3.54 (n/a)</td><td>0.84 (n/a)</td><td>1.48 (n/a)</td><td>2507.30 (n/a)</td><td>964.98 (n/a)</td><td>593.00 (n/a)</td><td>432.60 (n/a)</td><td>868.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.95 (-15.99%)</td><td>4.07 <b>(+21.39%)</b></td><td>4.13 <b>(+23.08%)</b></td><td>3.21 <b>(+439.17%)</b></td><td>0.83 <b>(-56.43%)</b></td><td>652.90 <b>(-81.45%)</b></td><td>533.80 <b>(-53.45%)</b></td><td>507.60 (-18.76%)</td><td>423.60 (+19.02%)</td><td>110.95 <b>(-91.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.89 (n/a)</td><td>3.35 (n/a)</td><td>3.36 (n/a)</td><td>0.60 (n/a)</td><td>1.90 (n/a)</td><td>3520.50 (n/a)</td><td>1146.74 (n/a)</td><td>624.80 (n/a)</td><td>355.90 (n/a)</td><td>1332.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.05 (+17.75%)</td><td>3.38 (+16.51%)</td><td>3.55 <b>(+29.28%)</b></td><td>0.58 (-0.97%)</td><td>2.04 (+15.61%)</td><td>3593.50 (+0.98%)</td><td>1174.84 (-6.64%)</td><td>591.50 <b>(-22.66%)</b></td><td>346.60 (-15.07%)</td><td>1364.44 (+4.28%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.14 (n/a)</td><td>2.90 (n/a)</td><td>2.74 (n/a)</td><td>0.59 (n/a)</td><td>1.76 (n/a)</td><td>3558.60 (n/a)</td><td>1258.40 (n/a)</td><td>764.80 (n/a)</td><td>408.10 (n/a)</td><td>1308.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.47 (-3.67%)</td><td>3.39 (-10.38%)</td><td>2.67 <b>(-49.85%)</b></td><td>1.75 <b>(+199.68%)</b></td><td>1.54 <b>(-37.16%)</b></td><td>1197.20 <b>(-66.63%)</b></td><td>729.76 <b>(-38.72%)</b></td><td>786.90 <b>(+99.42%)</b></td><td>383.50 (+3.82%)</td><td>323.98 <b>(-76.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.68 (n/a)</td><td>3.79 (n/a)</td><td>5.31 (n/a)</td><td>0.58 (n/a)</td><td>2.45 (n/a)</td><td>3587.70 (n/a)</td><td>1190.90 (n/a)</td><td>394.60 (n/a)</td><td>369.40 (n/a)</td><td>1389.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.95 (-6.16%)</td><td>3.73 (+14.75%)</td><td>3.52 <b>(+21.68%)</b></td><td>1.12 <b>(+89.03%)</b></td><td>2.02 (-2.30%)</td><td>1879.50 <b>(-47.10%)</b></td><td>805.18 <b>(-32.16%)</b></td><td>595.00 (-17.83%)</td><td>352.30 (+6.56%)</td><td>629.33 <b>(-52.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.34 (n/a)</td><td>3.25 (n/a)</td><td>2.90 (n/a)</td><td>0.59 (n/a)</td><td>2.07 (n/a)</td><td>3553.00 (n/a)</td><td>1186.94 (n/a)</td><td>724.10 (n/a)</td><td>330.60 (n/a)</td><td>1333.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.96 <b>(+23.76%)</b></td><td>3.51 (+6.96%)</td><td>2.99 <b>(-26.20%)</b></td><td>1.55 <b>(+163.99%)</b></td><td>1.64 (-1.15%)</td><td>1350.70 <b>(-62.12%)</b></td><td>726.38 <b>(-37.04%)</b></td><td>702.50 <b>(+35.51%)</b></td><td>352.00 (-19.21%)</td><td>379.90 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.81 (n/a)</td><td>3.28 (n/a)</td><td>4.05 (n/a)</td><td>0.59 (n/a)</td><td>1.66 (n/a)</td><td>3565.60 (n/a)</td><td>1153.72 (n/a)</td><td>518.40 (n/a)</td><td>435.70 (n/a)</td><td>1352.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.77 (-19.56%)</td><td>3.42 (+5.33%)</td><td>3.52 (-11.92%)</td><td>2.06 <b>(+257.94%)</b></td><td>1.32 <b>(-47.78%)</b></td><td>1019.10 <b>(-72.06%)</b></td><td>700.02 <b>(-58.61%)</b></td><td>596.10 (+13.54%)</td><td>440.10 <b>(+24.32%)</b></td><td>287.61 <b>(-83.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.92 (n/a)</td><td>3.25 (n/a)</td><td>3.99 (n/a)</td><td>0.57 (n/a)</td><td>2.53 (n/a)</td><td>3647.80 (n/a)</td><td>1691.08 (n/a)</td><td>525.00 (n/a)</td><td>354.00 (n/a)</td><td>1730.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.28 <b>(+28.71%)</b></td><td>3.36 (+19.70%)</td><td>3.13 (-12.45%)</td><td>0.60 (+2.21%)</td><td>1.86 (+17.42%)</td><td>3522.30 (-2.17%)</td><td>1147.98 (-11.03%)</td><td>670.40 (+14.21%)</td><td>396.90 <b>(-22.31%)</b></td><td>1334.91 (+0.60%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.10 (n/a)</td><td>2.81 (n/a)</td><td>3.57 (n/a)</td><td>0.58 (n/a)</td><td>1.59 (n/a)</td><td>3600.30 (n/a)</td><td>1290.32 (n/a)</td><td>587.00 (n/a)</td><td>510.90 (n/a)</td><td>1326.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.87 <b>(+20.67%)</b></td><td>3.51 <b>(+45.39%)</b></td><td>3.97 <b>(+133.73%)</b></td><td>1.17 (+2.78%)</td><td>1.40 (-6.05%)</td><td>3598.80 (-2.70%)</td><td>1552.76 <b>(-34.54%)</b></td><td>1055.80 <b>(-57.22%)</b></td><td>861.20 (-17.13%)</td><td>1150.83 (-12.07%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.04 (n/a)</td><td>2.41 (n/a)</td><td>1.70 (n/a)</td><td>1.13 (n/a)</td><td>1.50 (n/a)</td><td>3698.70 (n/a)</td><td>2372.06 (n/a)</td><td>2467.80 (n/a)</td><td>1039.20 (n/a)</td><td>1308.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.37 (+1.85%)</td><td>3.79 (-0.55%)</td><td>4.04 (-3.64%)</td><td>1.21 (-1.35%)</td><td>1.55 (+0.44%)</td><td>3452.90 (+1.37%)</td><td>1457.76 (+0.94%)</td><td>1037.80 (+3.78%)</td><td>781.10 (-1.81%)</td><td>1120.90 (+1.67%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.27 (n/a)</td><td>3.82 (n/a)</td><td>4.19 (n/a)</td><td>1.23 (n/a)</td><td>1.54 (n/a)</td><td>3406.10 (n/a)</td><td>1444.20 (n/a)</td><td>1000.00 (n/a)</td><td>795.50 (n/a)</td><td>1102.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.38 (+12.88%)</td><td>6.63 <b>(+27.36%)</b></td><td>7.23 (+13.84%)</td><td>1.92 <b>(+70.87%)</b></td><td>2.98 (+1.03%)</td><td>2187.10 <b>(-41.47%)</b></td><td>882.48 <b>(-35.10%)</b></td><td>580.30 (-12.16%)</td><td>447.10 (-11.40%)</td><td>737.11 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>8.31 (n/a)</td><td>5.20 (n/a)</td><td>6.35 (n/a)</td><td>1.12 (n/a)</td><td>2.95 (n/a)</td><td>3737.00 (n/a)</td><td>1359.66 (n/a)</td><td>660.60 (n/a)</td><td>504.60 (n/a)</td><td>1365.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.72 (+12.22%)</td><td>5.54 (-13.52%)</td><td>4.21 <b>(-37.76%)</b></td><td>2.86 <b>(-24.46%)</b></td><td>2.53 <b>(+57.48%)</b></td><td>1466.70 <b>(+32.37%)</b></td><td>897.28 <b>(+28.02%)</b></td><td>995.70 <b>(+60.67%)</b></td><td>480.80 (-10.90%)</td><td>401.00 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.77 (n/a)</td><td>6.41 (n/a)</td><td>6.77 (n/a)</td><td>3.79 (n/a)</td><td>1.61 (n/a)</td><td>1108.00 (n/a)</td><td>700.90 (n/a)</td><td>619.70 (n/a)</td><td>539.60 (n/a)</td><td>234.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>8.54 (+9.35%)</td><td>5.88 (+2.11%)</td><td>6.51 (+11.24%)</td><td>1.76 (+4.37%)</td><td>2.75 (+11.52%)</td><td>2387.10 (-4.18%)</td><td>990.26 (-1.27%)</td><td>644.30 (-10.10%)</td><td>491.00 (-8.55%)</td><td>797.08 (-4.72%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.81 (n/a)</td><td>5.76 (n/a)</td><td>5.85 (n/a)</td><td>1.68 (n/a)</td><td>2.46 (n/a)</td><td>2491.30 (n/a)</td><td>1002.98 (n/a)</td><td>716.70 (n/a)</td><td>536.90 (n/a)</td><td>836.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.21 <b>(-20.35%)</b></td><td>4.99 (-10.67%)</td><td>4.41 <b>(-29.75%)</b></td><td>3.49 <b>(+84.64%)</b></td><td>1.46 <b>(-56.57%)</b></td><td>1200.90 <b>(-45.84%)</b></td><td>895.24 <b>(-21.47%)</b></td><td>950.80 <b>(+42.36%)</b></td><td>581.60 <b>(+25.56%)</b></td><td>239.06 <b>(-71.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.05 (n/a)</td><td>5.59 (n/a)</td><td>6.28 (n/a)</td><td>1.89 (n/a)</td><td>3.37 (n/a)</td><td>2217.30 (n/a)</td><td>1139.96 (n/a)</td><td>667.90 (n/a)</td><td>463.20 (n/a)</td><td>831.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>10.97 (+5.33%)</td><td>5.58 (-18.10%)</td><td>4.38 <b>(-34.66%)</b></td><td>1.11 <b>(-74.58%)</b></td><td>3.81 <b>(+48.45%)</b></td><td>3788.40 <b>(+293.35%)</b></td><td>1358.48 <b>(+96.74%)</b></td><td>958.10 <b>(+53.03%)</b></td><td>382.50 (-5.04%)</td><td>1390.59 <b>(+448.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>10.41 (n/a)</td><td>6.81 (n/a)</td><td>6.70 (n/a)</td><td>4.35 (n/a)</td><td>2.57 (n/a)</td><td>963.10 (n/a)</td><td>690.50 (n/a)</td><td>626.10 (n/a)</td><td>402.80 (n/a)</td><td>253.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>11.34 <b>(+46.16%)</b></td><td>4.97 (-6.08%)</td><td>3.94 <b>(-42.29%)</b></td><td>1.67 <b>(+45.76%)</b></td><td>3.70 <b>(+33.91%)</b></td><td>2516.70 <b>(-31.40%)</b></td><td>1216.70 (-6.92%)</td><td>1063.80 <b>(+73.29%)</b></td><td>369.70 <b>(-31.59%)</b></td><td>787.40 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.76 (n/a)</td><td>5.29 (n/a)</td><td>6.83 (n/a)</td><td>1.14 (n/a)</td><td>2.76 (n/a)</td><td>3668.40 (n/a)</td><td>1307.10 (n/a)</td><td>613.90 (n/a)</td><td>540.40 (n/a)</td><td>1339.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>8.12 (-12.62%)</td><td>6.36 (-15.53%)</td><td>6.72 (-6.15%)</td><td>3.90 <b>(-39.51%)</b></td><td>1.54 <b>(+24.28%)</b></td><td>1075.70 <b>(+65.31%)</b></td><td>700.94 <b>(+23.23%)</b></td><td>624.40 (+6.55%)</td><td>516.50 (+14.45%)</td><td>217.23 <b>(+144.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.29 (n/a)</td><td>7.53 (n/a)</td><td>7.16 (n/a)</td><td>6.45 (n/a)</td><td>1.24 (n/a)</td><td>650.70 (n/a)</td><td>568.82 (n/a)</td><td>586.00 (n/a)</td><td>451.30 (n/a)</td><td>88.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.78 <b>(-24.93%)</b></td><td>5.95 (+16.74%)</td><td>6.18 (+9.78%)</td><td>3.89 <b>(+182.61%)</b></td><td>1.55 <b>(-56.33%)</b></td><td>1079.20 <b>(-64.61%)</b></td><td>749.56 <b>(-44.63%)</b></td><td>678.20 (-8.92%)</td><td>539.00 <b>(+33.22%)</b></td><td>217.01 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>10.37 (n/a)</td><td>5.10 (n/a)</td><td>5.63 (n/a)</td><td>1.38 (n/a)</td><td>3.55 (n/a)</td><td>3049.80 (n/a)</td><td>1353.78 (n/a)</td><td>744.60 (n/a)</td><td>404.60 (n/a)</td><td>1095.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.74 (+4.18%)</td><td>6.86 (+8.26%)</td><td>7.54 (+12.57%)</td><td>2.08 <b>(-51.15%)</b></td><td>2.85 <b>(+37.92%)</b></td><td>2013.00 <b>(+104.72%)</b></td><td>824.48 (+14.65%)</td><td>556.00 (-11.17%)</td><td>430.50 (-4.01%)</td><td>666.83 <b>(+193.93%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.35 (n/a)</td><td>6.34 (n/a)</td><td>6.70 (n/a)</td><td>4.27 (n/a)</td><td>2.06 (n/a)</td><td>983.30 (n/a)</td><td>719.14 (n/a)</td><td>625.90 (n/a)</td><td>448.50 (n/a)</td><td>226.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.34 (-15.31%)</td><td>5.95 (+5.52%)</td><td>7.42 <b>(+69.24%)</b></td><td>1.15 <b>(-66.33%)</b></td><td>3.09 (+16.03%)</td><td>3646.90 <b>(+196.98%)</b></td><td>1228.06 <b>(+42.12%)</b></td><td>564.90 <b>(-40.92%)</b></td><td>502.70 (+18.06%)</td><td>1363.09 <b>(+313.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.85 (n/a)</td><td>5.64 (n/a)</td><td>4.39 (n/a)</td><td>3.42 (n/a)</td><td>2.66 (n/a)</td><td>1228.00 (n/a)</td><td>864.10 (n/a)</td><td>956.10 (n/a)</td><td>425.80 (n/a)</td><td>329.75 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.61 (-3.08%)</td><td>1.09 (-10.86%)</td><td>1.09 (+1.28%)</td><td>0.76 (-19.00%)</td><td>0.33 (+6.11%)</td><td>685.60 <b>(+23.46%)</b></td><td>515.58 (+14.27%)</td><td>483.00 (-1.27%)</td><td>326.10 (+3.16%)</td><td>140.23 <b>(+34.66%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.66 (n/a)</td><td>1.22 (n/a)</td><td>1.07 (n/a)</td><td>0.94 (n/a)</td><td>0.31 (n/a)</td><td>555.30 (n/a)</td><td>451.18 (n/a)</td><td>489.20 (n/a)</td><td>316.10 (n/a)</td><td>104.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.59 <b>(-20.80%)</b></td><td>1.94 <b>(+47.45%)</b></td><td>2.20 <b>(+63.37%)</b></td><td>1.06 <b>(+257.83%)</b></td><td>0.73 <b>(-39.78%)</b></td><td>985.40 <b>(-72.05%)</b></td><td>621.48 <b>(-65.09%)</b></td><td>476.60 <b>(-38.80%)</b></td><td>404.20 <b>(+26.27%)</b></td><td>270.53 <b>(-83.03%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.28 (n/a)</td><td>1.32 (n/a)</td><td>1.35 (n/a)</td><td>0.30 (n/a)</td><td>1.22 (n/a)</td><td>3526.10 (n/a)</td><td>1780.26 (n/a)</td><td>778.70 (n/a)</td><td>320.10 (n/a)</td><td>1594.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.60 (+2.64%)</td><td>1.63 <b>(-33.46%)</b></td><td>1.61 <b>(-31.82%)</b></td><td>0.59 <b>(-23.07%)</b></td><td>1.23 (+11.77%)</td><td>3569.90 <b>(+29.99%)</b></td><td>2032.44 <b>(+75.45%)</b></td><td>1301.50 <b>(+46.68%)</b></td><td>583.00 (-2.56%)</td><td>1401.48 <b>(+55.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.50 (n/a)</td><td>2.45 (n/a)</td><td>2.36 (n/a)</td><td>0.76 (n/a)</td><td>1.10 (n/a)</td><td>2746.30 (n/a)</td><td>1158.40 (n/a)</td><td>887.30 (n/a)</td><td>598.30 (n/a)</td><td>900.45 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.97 (+19.29%)</td><td>1.41 <b>(+26.75%)</b></td><td>1.28 <b>(+31.21%)</b></td><td>0.79 <b>(+38.25%)</b></td><td>0.48 (-2.22%)</td><td>660.60 <b>(-27.67%)</b></td><td>412.38 <b>(-25.88%)</b></td><td>410.70 <b>(-23.79%)</b></td><td>265.60 (-16.16%)</td><td>157.56 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.66 (n/a)</td><td>1.11 (n/a)</td><td>0.97 (n/a)</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>913.30 (n/a)</td><td>556.40 (n/a)</td><td>538.90 (n/a)</td><td>316.80 (n/a)</td><td>252.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.28 <b>(-32.73%)</b></td><td>1.05 (+0.81%)</td><td>1.03 (+19.24%)</td><td>0.88 <b>(+27.32%)</b></td><td>0.17 <b>(-65.73%)</b></td><td>596.30 <b>(-21.46%)</b></td><td>510.12 (-10.57%)</td><td>511.40 (-16.14%)</td><td>411.10 <b>(+48.63%)</b></td><td>79.04 <b>(-56.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.90 (n/a)</td><td>1.04 (n/a)</td><td>0.86 (n/a)</td><td>0.69 (n/a)</td><td>0.49 (n/a)</td><td>759.20 (n/a)</td><td>570.40 (n/a)</td><td>609.80 (n/a)</td><td>276.60 (n/a)</td><td>181.70 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.59 (-19.93%)</td><td>1.24 (-13.53%)</td><td>1.30 (-11.39%)</td><td>0.90 (-2.42%)</td><td>0.31 <b>(-21.60%)</b></td><td>579.40 (+2.48%)</td><td>447.26 (+14.39%)</td><td>401.80 (+12.83%)</td><td>329.80 <b>(+24.88%)</b></td><td>116.43 (+2.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.99 (n/a)</td><td>1.43 (n/a)</td><td>1.47 (n/a)</td><td>0.93 (n/a)</td><td>0.39 (n/a)</td><td>565.40 (n/a)</td><td>390.98 (n/a)</td><td>356.10 (n/a)</td><td>264.10 (n/a)</td><td>113.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 <b>(-24.65%)</b></td><td>0.09 (-18.32%)</td><td>0.10 (-14.64%)</td><td>0.06 (-4.96%)</td><td>0.02 <b>(-40.24%)</b></td><td>564.90 (+5.22%)</td><td>396.76 (+16.13%)</td><td>340.20 (+17.15%)</td><td>297.90 <b>(+32.69%)</b></td><td>113.46 (-15.15%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>536.90 (n/a)</td><td>341.66 (n/a)</td><td>290.40 (n/a)</td><td>224.50 (n/a)</td><td>133.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+0.75%)</td><td>0.12 <b>(+25.51%)</b></td><td>0.12 <b>(+36.03%)</b></td><td>0.10 <b>(+67.75%)</b></td><td>0.01 <b>(-56.00%)</b></td><td>322.90 <b>(-40.38%)</b></td><td>280.66 <b>(-26.79%)</b></td><td>278.40 <b>(-26.49%)</b></td><td>240.50 (-0.78%)</td><td>34.05 <b>(-73.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>541.60 (n/a)</td><td>383.36 (n/a)</td><td>378.70 (n/a)</td><td>242.40 (n/a)</td><td>129.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (-1.09%)</td><td>0.08 <b>(-23.85%)</b></td><td>0.06 <b>(-44.74%)</b></td><td>0.05 (-8.70%)</td><td>0.04 (+18.98%)</td><td>618.60 (+9.53%)</td><td>453.76 <b>(+37.63%)</b></td><td>521.50 <b>(+80.95%)</b></td><td>243.00 (+1.12%)</td><td>171.49 <b>(+27.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>564.80 (n/a)</td><td>329.70 (n/a)</td><td>288.20 (n/a)</td><td>240.30 (n/a)</td><td>134.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+12.42%)</td><td>0.09 (+6.12%)</td><td>0.09 <b>(+32.18%)</b></td><td>0.05 (-19.76%)</td><td>0.04 <b>(+26.65%)</b></td><td>658.70 <b>(+24.61%)</b></td><td>423.32 (+0.01%)</td><td>375.60 <b>(-24.35%)</b></td><td>222.20 (-11.05%)</td><td>180.07 <b>(+38.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.60 (n/a)</td><td>423.26 (n/a)</td><td>496.50 (n/a)</td><td>249.80 (n/a)</td><td>130.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.23 (+4.57%)</td><td>0.19 (+15.72%)</td><td>0.22 <b>(+51.22%)</b></td><td>0.12 (+10.24%)</td><td>0.05 (-1.38%)</td><td>546.20 (-9.28%)</td><td>369.98 (-14.41%)</td><td>300.40 <b>(-33.88%)</b></td><td>284.40 (-4.37%)</td><td>115.51 (-11.98%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>602.10 (n/a)</td><td>432.26 (n/a)</td><td>454.30 (n/a)</td><td>297.40 (n/a)</td><td>131.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (+10.69%)</td><td>0.18 (+9.40%)</td><td>0.12 (-5.48%)</td><td>0.12 (+8.59%)</td><td>0.09 <b>(+30.24%)</b></td><td>567.10 (-7.91%)</td><td>430.14 (-3.32%)</td><td>556.40 (+5.80%)</td><td>222.80 (-9.69%)</td><td>180.68 (+12.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>615.80 (n/a)</td><td>444.90 (n/a)</td><td>525.90 (n/a)</td><td>246.70 (n/a)</td><td>160.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.28 (+8.45%)</td><td>0.17 (-15.53%)</td><td>0.14 <b>(-35.73%)</b></td><td>0.13 (-2.84%)</td><td>0.06 (+18.34%)</td><td>500.90 (+2.94%)</td><td>415.90 <b>(+20.45%)</b></td><td>465.70 <b>(+55.60%)</b></td><td>231.00 (-7.78%)</td><td>109.79 (+8.09%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>486.60 (n/a)</td><td>345.28 (n/a)</td><td>299.30 (n/a)</td><td>250.50 (n/a)</td><td>101.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.27 (+14.48%)</td><td>0.16 <b>(-20.48%)</b></td><td>0.13 <b>(-41.15%)</b></td><td>0.10 <b>(-23.64%)</b></td><td>0.07 <b>(+65.25%)</b></td><td>644.20 <b>(+30.96%)</b></td><td>476.14 <b>(+36.29%)</b></td><td>513.00 <b>(+69.92%)</b></td><td>242.90 (-12.66%)</td><td>162.21 <b>(+84.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>491.90 (n/a)</td><td>349.36 (n/a)</td><td>301.90 (n/a)</td><td>278.10 (n/a)</td><td>87.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 <b>(-37.72%)</b></td><td>0.12 <b>(-34.69%)</b></td><td>0.10 <b>(-32.79%)</b></td><td>0.09 (-7.50%)</td><td>0.04 <b>(-58.67%)</b></td><td>695.80 (+8.11%)</td><td>570.06 <b>(+36.46%)</b></td><td>639.90 <b>(+48.78%)</b></td><td>369.80 <b>(+60.57%)</b></td><td>146.46 <b>(-20.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>643.60 (n/a)</td><td>417.76 (n/a)</td><td>430.10 (n/a)</td><td>230.30 (n/a)</td><td>185.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.26 (-13.49%)</td><td>0.20 (+7.41%)</td><td>0.18 <b>(+23.46%)</b></td><td>0.13 (+6.95%)</td><td>0.06 <b>(-24.32%)</b></td><td>491.00 (-6.49%)</td><td>354.42 (-10.52%)</td><td>354.40 (-18.99%)</td><td>249.10 (+15.59%)</td><td>101.36 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>525.10 (n/a)</td><td>396.10 (n/a)</td><td>437.50 (n/a)</td><td>215.50 (n/a)</td><td>126.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.42 <b>(-22.26%)</b></td><td>0.36 (-12.23%)</td><td>0.39 (-12.47%)</td><td>0.26 (+0.27%)</td><td>0.07 <b>(-47.77%)</b></td><td>509.90 (-0.27%)</td><td>375.62 (+7.63%)</td><td>334.50 (+14.24%)</td><td>312.60 <b>(+28.64%)</b></td><td>81.77 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>511.30 (n/a)</td><td>348.98 (n/a)</td><td>292.80 (n/a)</td><td>243.00 (n/a)</td><td>120.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.44 (-3.31%)</td><td>0.34 (+7.72%)</td><td>0.31 (+19.91%)</td><td>0.23 (+4.85%)</td><td>0.09 (-14.01%)</td><td>569.00 (-4.63%)</td><td>406.64 (-9.41%)</td><td>422.50 (-16.60%)</td><td>295.50 (+3.43%)</td><td>112.84 (-17.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>596.60 (n/a)</td><td>448.86 (n/a)</td><td>506.60 (n/a)</td><td>285.70 (n/a)</td><td>136.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.59 (+5.47%)</td><td>0.31 <b>(-25.24%)</b></td><td>0.24 <b>(-48.98%)</b></td><td>0.21 (-0.28%)</td><td>0.16 (+9.31%)</td><td>615.80 (+0.28%)</td><td>490.44 <b>(+35.01%)</b></td><td>542.10 <b>(+95.99%)</b></td><td>222.60 (-5.16%)</td><td>155.35 (-2.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.47 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>614.10 (n/a)</td><td>363.26 (n/a)</td><td>276.60 (n/a)</td><td>234.70 (n/a)</td><td>159.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.37 (-17.09%)</td><td>0.27 (-11.22%)</td><td>0.25 <b>(-26.39%)</b></td><td>0.20 <b>(+189.58%)</b></td><td>0.07 <b>(-53.11%)</b></td><td>646.10 <b>(-65.47%)</b></td><td>506.90 <b>(-25.38%)</b></td><td>524.90 <b>(+35.84%)</b></td><td>350.80 <b>(+20.59%)</b></td><td>130.20 <b>(-80.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1871.10 (n/a)</td><td>679.34 (n/a)</td><td>386.40 (n/a)</td><td>290.90 (n/a)</td><td>674.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.49 (+17.13%)</td><td>0.36 (+15.72%)</td><td>0.34 <b>(+20.42%)</b></td><td>0.22 (-18.26%)</td><td>0.12 <b>(+96.92%)</b></td><td>603.40 <b>(+22.34%)</b></td><td>409.04 (-6.71%)</td><td>386.90 (-16.96%)</td><td>267.20 (-14.63%)</td><td>147.00 <b>(+105.23%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>493.20 (n/a)</td><td>438.48 (n/a)</td><td>465.90 (n/a)</td><td>313.00 (n/a)</td><td>71.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.54 (-13.61%)</td><td>0.37 (-2.01%)</td><td>0.30 (+4.69%)</td><td>0.25 (+11.13%)</td><td>0.12 <b>(-30.23%)</b></td><td>519.80 (-10.01%)</td><td>390.46 (-5.87%)</td><td>433.60 (-4.49%)</td><td>244.10 (+15.74%)</td><td>118.23 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.62 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>577.60 (n/a)</td><td>414.82 (n/a)</td><td>454.00 (n/a)</td><td>210.90 (n/a)</td><td>169.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (+3.13%)</td><td>0.04 (+4.96%)</td><td>0.04 (+4.68%)</td><td>0.03 (+4.58%)</td><td>0.01 (-1.80%)</td><td>597.50 (-4.38%)</td><td>443.94 (-5.42%)</td><td>438.00 (-4.47%)</td><td>288.00 (-3.03%)</td><td>110.93 (-9.97%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>624.90 (n/a)</td><td>469.40 (n/a)</td><td>458.50 (n/a)</td><td>297.00 (n/a)</td><td>123.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 <b>(+53.54%)</b></td><td>0.06 <b>(+34.40%)</b></td><td>0.06 <b>(+46.03%)</b></td><td>0.03 (-6.25%)</td><td>0.03 <b>(+108.82%)</b></td><td>608.00 (+6.69%)</td><td>347.14 (-16.43%)</td><td>276.80 <b>(-31.50%)</b></td><td>171.70 <b>(-34.86%)</b></td><td>168.16 <b>(+52.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>415.38 (n/a)</td><td>404.10 (n/a)</td><td>263.60 (n/a)</td><td>110.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>
