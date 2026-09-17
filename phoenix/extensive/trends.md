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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-12.86%)</td><td>0.02 <b>(-22.26%)</b></td><td>0.02 <b>(-32.57%)</b></td><td>0.01 (+2.02%)</td><td>0.01 (-17.96%)</td><td>497.30 (-1.99%)</td><td>363.58 <b>(+25.32%)</b></td><td>346.40 <b>(+48.35%)</b></td><td>256.50 (+14.77%)</td><td>107.80 (-11.78%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.40 (n/a)</td><td>290.12 (n/a)</td><td>233.50 (n/a)</td><td>223.50 (n/a)</td><td>122.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 <b>(+41.04%)</b></td><td>0.02 (+1.08%)</td><td>0.01 (-13.81%)</td><td>0.01 (-9.69%)</td><td>0.01 <b>(+55.07%)</b></td><td>596.90 (+10.74%)</td><td>426.74 (+10.77%)</td><td>485.10 (+16.02%)</td><td>167.90 <b>(-29.10%)</b></td><td>192.23 <b>(+35.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.00 (n/a)</td><td>385.26 (n/a)</td><td>418.10 (n/a)</td><td>236.80 (n/a)</td><td>141.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+1.70%)</td><td>0.02 (-2.25%)</td><td>0.01 (-10.91%)</td><td>0.01 (+14.23%)</td><td>0.01 (-9.29%)</td><td>466.50 (-12.46%)</td><td>376.88 (+0.05%)</td><td>425.50 (+12.24%)</td><td>240.00 (-1.68%)</td><td>105.08 (-16.95%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>376.70 (n/a)</td><td>379.10 (n/a)</td><td>244.10 (n/a)</td><td>126.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(-29.96%)</b></td><td>0.02 (-6.46%)</td><td>0.02 (+12.88%)</td><td>0.01 (+19.12%)</td><td>0.00 <b>(-60.51%)</b></td><td>425.60 (-16.04%)</td><td>308.88 (-3.63%)</td><td>284.30 (-11.41%)</td><td>268.90 <b>(+42.80%)</b></td><td>65.76 <b>(-49.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>320.50 (n/a)</td><td>320.90 (n/a)</td><td>188.30 (n/a)</td><td>129.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-0.35%)</td><td>0.02 (+7.06%)</td><td>0.02 <b>(+22.35%)</b></td><td>0.01 <b>(-23.56%)</b></td><td>0.01 <b>(+45.12%)</b></td><td>648.80 <b>(+30.83%)</b></td><td>424.00 (+2.64%)</td><td>365.00 (-18.27%)</td><td>256.60 (+0.35%)</td><td>183.79 <b>(+96.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.90 (n/a)</td><td>413.08 (n/a)</td><td>446.60 (n/a)</td><td>255.70 (n/a)</td><td>93.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+11.94%)</td><td>0.02 (+0.18%)</td><td>0.01 (-11.85%)</td><td>0.01 <b>(-24.20%)</b></td><td>0.01 <b>(+41.89%)</b></td><td>664.60 <b>(+31.94%)</b></td><td>422.42 (+9.59%)</td><td>471.60 (+13.45%)</td><td>229.50 (-10.67%)</td><td>187.57 <b>(+56.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>503.70 (n/a)</td><td>385.46 (n/a)</td><td>415.70 (n/a)</td><td>256.90 (n/a)</td><td>120.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 <b>(-20.45%)</b></td><td>0.03 (-12.64%)</td><td>0.03 <b>(-26.92%)</b></td><td>0.03 <b>(+43.05%)</b></td><td>0.01 <b>(-62.68%)</b></td><td>425.60 <b>(-30.09%)</b></td><td>388.74 (-0.99%)</td><td>406.00 <b>(+36.84%)</b></td><td>289.80 <b>(+25.73%)</b></td><td>56.35 <b>(-69.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>608.80 (n/a)</td><td>392.64 (n/a)</td><td>296.70 (n/a)</td><td>230.50 (n/a)</td><td>183.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (+4.02%)</td><td>0.04 (+5.57%)</td><td>0.05 (+11.83%)</td><td>0.03 (+5.56%)</td><td>0.01 (+7.94%)</td><td>472.80 (-5.27%)</td><td>329.82 (-4.54%)</td><td>242.90 (-10.57%)</td><td>225.80 (-3.83%)</td><td>129.80 (-0.74%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.10 (n/a)</td><td>345.52 (n/a)</td><td>271.60 (n/a)</td><td>234.80 (n/a)</td><td>130.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (+7.26%)</td><td>0.05 <b>(+45.01%)</b></td><td>0.05 <b>(+78.49%)</b></td><td>0.02 <b>(+32.32%)</b></td><td>0.01 (+0.08%)</td><td>503.70 <b>(-24.43%)</b></td><td>294.38 <b>(-32.70%)</b></td><td>245.70 <b>(-43.98%)</b></td><td>229.20 (-6.75%)</td><td>117.69 <b>(-26.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>666.50 (n/a)</td><td>437.40 (n/a)</td><td>438.60 (n/a)</td><td>245.80 (n/a)</td><td>159.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (-10.01%)</td><td>0.04 (+8.46%)</td><td>0.04 (-9.69%)</td><td>0.04 <b>(+73.74%)</b></td><td>0.00 <b>(-71.32%)</b></td><td>312.20 <b>(-42.44%)</b></td><td>277.82 (-19.66%)</td><td>282.60 (+10.74%)</td><td>237.40 (+11.09%)</td><td>27.15 <b>(-82.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>542.40 (n/a)</td><td>345.82 (n/a)</td><td>255.20 (n/a)</td><td>213.70 (n/a)</td><td>153.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (-9.15%)</td><td>0.03 <b>(-22.75%)</b></td><td>0.02 <b>(-42.04%)</b></td><td>0.02 (-18.09%)</td><td>0.01 (+10.87%)</td><td>603.80 <b>(+22.08%)</b></td><td>447.74 <b>(+33.20%)</b></td><td>503.00 <b>(+72.50%)</b></td><td>288.30 (+10.08%)</td><td>133.95 <b>(+41.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.60 (n/a)</td><td>336.14 (n/a)</td><td>291.60 (n/a)</td><td>261.90 (n/a)</td><td>94.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (+18.40%)</td><td>0.04 (+14.16%)</td><td>0.03 (-13.07%)</td><td>0.02 <b>(+107.65%)</b></td><td>0.01 (-9.84%)</td><td>507.40 <b>(-51.84%)</b></td><td>352.56 <b>(-25.40%)</b></td><td>353.30 (+15.04%)</td><td>239.50 (-15.52%)</td><td>113.77 <b>(-65.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1053.60 (n/a)</td><td>472.62 (n/a)</td><td>307.10 (n/a)</td><td>283.50 (n/a)</td><td>330.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 <b>(+22.42%)</b></td><td>0.08 <b>(+35.22%)</b></td><td>0.09 <b>(+53.39%)</b></td><td>0.05 (-2.05%)</td><td>0.02 <b>(+54.82%)</b></td><td>514.70 (+2.10%)</td><td>315.36 <b>(-22.84%)</b></td><td>272.70 <b>(-34.79%)</b></td><td>230.30 (-18.33%)</td><td>115.02 <b>(+40.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>504.10 (n/a)</td><td>408.72 (n/a)</td><td>418.20 (n/a)</td><td>282.00 (n/a)</td><td>81.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (+14.63%)</td><td>0.07 (-7.01%)</td><td>0.06 (-19.94%)</td><td>0.06 (-8.56%)</td><td>0.02 <b>(+71.75%)</b></td><td>437.30 (+9.38%)</td><td>354.16 (+11.96%)</td><td>391.70 <b>(+24.90%)</b></td><td>227.90 (-12.75%)</td><td>90.80 <b>(+66.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>399.80 (n/a)</td><td>316.34 (n/a)</td><td>313.60 (n/a)</td><td>261.20 (n/a)</td><td>54.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (+0.37%)</td><td>0.08 <b>(-20.97%)</b></td><td>0.08 (-13.15%)</td><td>0.05 <b>(-43.53%)</b></td><td>0.03 <b>(+112.47%)</b></td><td>533.80 <b>(+77.11%)</b></td><td>361.88 <b>(+44.51%)</b></td><td>292.70 (+15.15%)</td><td>204.40 (-0.34%)</td><td>157.74 <b>(+312.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>301.40 (n/a)</td><td>250.42 (n/a)</td><td>254.20 (n/a)</td><td>205.10 (n/a)</td><td>38.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 <b>(+77.94%)</b></td><td>0.07 <b>(+51.72%)</b></td><td>0.07 <b>(+20.82%)</b></td><td>0.05 <b>(+56.92%)</b></td><td>0.02 <b>(+131.14%)</b></td><td>469.20 <b>(-36.27%)</b></td><td>354.92 <b>(-31.98%)</b></td><td>375.60 (-17.23%)</td><td>241.90 <b>(-43.80%)</b></td><td>100.70 <b>(-20.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>736.20 (n/a)</td><td>521.82 (n/a)</td><td>453.80 (n/a)</td><td>430.40 (n/a)</td><td>126.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (-12.67%)</td><td>0.06 (-1.96%)</td><td>0.06 (+11.28%)</td><td>0.05 <b>(+25.87%)</b></td><td>0.01 <b>(-45.31%)</b></td><td>516.70 <b>(-20.56%)</b></td><td>409.42 (-6.32%)</td><td>412.10 (-10.14%)</td><td>294.10 (+14.52%)</td><td>82.09 <b>(-49.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>650.40 (n/a)</td><td>437.06 (n/a)</td><td>458.60 (n/a)</td><td>256.80 (n/a)</td><td>162.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (-8.24%)</td><td>0.09 (+2.88%)</td><td>0.09 (+14.70%)</td><td>0.05 (-12.11%)</td><td>0.02 (-0.42%)</td><td>516.40 (+13.77%)</td><td>309.78 (-0.71%)</td><td>260.20 (-12.80%)</td><td>220.60 (+8.99%)</td><td>118.63 <b>(+31.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>453.90 (n/a)</td><td>312.00 (n/a)</td><td>298.40 (n/a)</td><td>202.40 (n/a)</td><td>90.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (-18.79%)</td><td>0.10 <b>(-27.33%)</b></td><td>0.10 <b>(-30.88%)</b></td><td>0.06 <b>(-27.37%)</b></td><td>0.04 <b>(-20.43%)</b></td><td>830.80 <b>(+37.69%)</b></td><td>525.28 <b>(+38.25%)</b></td><td>513.90 <b>(+44.68%)</b></td><td>297.80 <b>(+23.16%)</b></td><td>195.81 <b>(+35.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>603.40 (n/a)</td><td>379.94 (n/a)</td><td>355.20 (n/a)</td><td>241.80 (n/a)</td><td>144.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 <b>(-22.61%)</b></td><td>0.12 <b>(-28.02%)</b></td><td>0.10 <b>(-41.89%)</b></td><td>0.08 (-16.86%)</td><td>0.04 (-15.34%)</td><td>592.60 <b>(+20.28%)</b></td><td>427.74 <b>(+38.96%)</b></td><td>470.80 <b>(+72.08%)</b></td><td>296.40 <b>(+29.21%)</b></td><td>125.51 (+18.15%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>492.70 (n/a)</td><td>307.82 (n/a)</td><td>273.60 (n/a)</td><td>229.40 (n/a)</td><td>106.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (-14.40%)</td><td>0.10 <b>(-36.25%)</b></td><td>0.10 <b>(-44.55%)</b></td><td>0.06 <b>(-45.61%)</b></td><td>0.04 (+0.27%)</td><td>799.90 <b>(+83.84%)</b></td><td>529.32 <b>(+65.84%)</b></td><td>499.00 <b>(+80.34%)</b></td><td>276.60 (+16.81%)</td><td>189.21 <b>(+105.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>435.10 (n/a)</td><td>319.18 (n/a)</td><td>276.70 (n/a)</td><td>236.80 (n/a)</td><td>92.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (-11.61%)</td><td>0.12 (-17.20%)</td><td>0.10 (-14.12%)</td><td>0.05 <b>(-42.35%)</b></td><td>0.05 (+9.53%)</td><td>978.70 <b>(+73.47%)</b></td><td>515.50 <b>(+34.87%)</b></td><td>482.20 (+16.45%)</td><td>270.00 (+13.16%)</td><td>283.27 <b>(+117.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>564.20 (n/a)</td><td>382.22 (n/a)</td><td>414.10 (n/a)</td><td>238.60 (n/a)</td><td>130.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.19 (-5.93%)</td><td>0.09 <b>(-44.86%)</b></td><td>0.09 <b>(-42.97%)</b></td><td>0.02 <b>(-79.18%)</b></td><td>0.07 <b>(+83.53%)</b></td><td>2089.90 <b>(+380.22%)</b></td><td>1072.88 <b>(+221.36%)</b></td><td>536.30 <b>(+75.32%)</b></td><td>263.90 (+6.28%)</td><td>884.74 <b>(+981.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>435.20 (n/a)</td><td>333.86 (n/a)</td><td>305.90 (n/a)</td><td>248.30 (n/a)</td><td>81.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (+17.52%)</td><td>0.15 <b>(+59.92%)</b></td><td>0.16 <b>(+75.62%)</b></td><td>0.11 <b>(+308.28%)</b></td><td>0.03 <b>(-28.18%)</b></td><td>453.40 <b>(-75.51%)</b></td><td>345.72 <b>(-53.77%)</b></td><td>300.40 <b>(-43.05%)</b></td><td>277.80 (-14.92%)</td><td>81.90 <b>(-86.88%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1851.20 (n/a)</td><td>747.90 (n/a)</td><td>527.50 (n/a)</td><td>326.50 (n/a)</td><td>624.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-16.65%)</td><td>0.01 <b>(-21.31%)</b></td><td>0.01 (-0.40%)</td><td>0.00 <b>(-51.38%)</b></td><td>0.00 (+18.19%)</td><td>1031.00 <b>(+105.67%)</b></td><td>466.98 <b>(+50.39%)</b></td><td>294.50 (+0.37%)</td><td>268.90 (+19.99%)</td><td>323.35 <b>(+189.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.30 (n/a)</td><td>310.52 (n/a)</td><td>293.40 (n/a)</td><td>224.10 (n/a)</td><td>111.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+36.63%)</b></td><td>0.01 (+15.10%)</td><td>0.01 <b>(+35.92%)</b></td><td>0.01 (-8.30%)</td><td>0.00 <b>(+73.22%)</b></td><td>519.90 (+9.06%)</td><td>344.40 (-5.72%)</td><td>298.60 <b>(-26.42%)</b></td><td>169.00 <b>(-26.81%)</b></td><td>136.52 <b>(+40.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.70 (n/a)</td><td>365.28 (n/a)</td><td>405.80 (n/a)</td><td>230.90 (n/a)</td><td>97.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (+9.54%)</td><td>0.01 (+9.72%)</td><td>0.01 (-2.32%)</td><td>0.01 <b>(+27.19%)</b></td><td>0.00 (+1.09%)</td><td>510.80 <b>(-21.38%)</b></td><td>413.82 (-10.73%)</td><td>437.70 (+2.39%)</td><td>256.10 (-8.70%)</td><td>96.95 <b>(-29.74%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>649.70 (n/a)</td><td>463.54 (n/a)</td><td>427.50 (n/a)</td><td>280.50 (n/a)</td><td>137.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (+0.71%)</td><td>0.01 (+8.09%)</td><td>0.01 (-0.57%)</td><td>0.01 (+2.60%)</td><td>0.00 (+11.40%)</td><td>512.80 (-2.55%)</td><td>392.48 (-5.47%)</td><td>440.30 (+0.57%)</td><td>238.20 (-0.71%)</td><td>123.45 (+17.13%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>526.20 (n/a)</td><td>415.20 (n/a)</td><td>437.80 (n/a)</td><td>239.90 (n/a)</td><td>105.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (+6.86%)</td><td>0.01 (+3.18%)</td><td>0.01 (-2.06%)</td><td>0.00 (-6.13%)</td><td>0.00 (+3.75%)</td><td>583.70 (+6.53%)</td><td>362.22 (-2.42%)</td><td>301.60 (+2.10%)</td><td>248.80 (-6.40%)</td><td>136.82 (+6.01%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>547.90 (n/a)</td><td>371.22 (n/a)</td><td>295.40 (n/a)</td><td>265.80 (n/a)</td><td>129.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 <b>(+36.85%)</b></td><td>0.01 (+14.03%)</td><td>0.01 (-3.08%)</td><td>0.00 (-13.68%)</td><td>0.00 <b>(+79.54%)</b></td><td>777.90 (+15.83%)</td><td>483.10 (-5.04%)</td><td>495.60 (+3.19%)</td><td>251.60 <b>(-26.92%)</b></td><td>194.71 <b>(+46.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>671.60 (n/a)</td><td>508.74 (n/a)</td><td>480.30 (n/a)</td><td>344.30 (n/a)</td><td>132.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-15.76%)</td><td>0.02 (-9.10%)</td><td>0.02 (+8.20%)</td><td>0.01 (-11.15%)</td><td>0.01 (+2.65%)</td><td>451.90 (+12.55%)</td><td>327.84 (+12.88%)</td><td>258.80 (-7.57%)</td><td>239.50 (+18.68%)</td><td>109.77 <b>(+39.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>401.50 (n/a)</td><td>290.44 (n/a)</td><td>280.00 (n/a)</td><td>201.80 (n/a)</td><td>78.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+1.32%)</td><td>0.02 (-5.69%)</td><td>0.02 (-4.08%)</td><td>0.01 <b>(+223.95%)</b></td><td>0.01 <b>(-24.28%)</b></td><td>565.60 <b>(-69.13%)</b></td><td>375.46 <b>(-34.31%)</b></td><td>275.30 (+4.24%)</td><td>236.40 (-1.29%)</td><td>160.02 <b>(-77.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1832.30 (n/a)</td><td>571.52 (n/a)</td><td>264.10 (n/a)</td><td>239.50 (n/a)</td><td>704.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-9.92%)</td><td>0.02 (+9.61%)</td><td>0.01 <b>(+23.74%)</b></td><td>0.01 (+14.24%)</td><td>0.01 <b>(-24.86%)</b></td><td>544.80 (-12.47%)</td><td>382.52 (-15.53%)</td><td>370.70 (-19.18%)</td><td>202.30 (+11.03%)</td><td>126.55 <b>(-24.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.40 (n/a)</td><td>452.84 (n/a)</td><td>458.70 (n/a)</td><td>182.20 (n/a)</td><td>166.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+10.32%)</td><td>0.01 (+12.59%)</td><td>0.01 (-7.05%)</td><td>0.01 <b>(+87.34%)</b></td><td>0.00 (-1.83%)</td><td>532.40 <b>(-46.62%)</b></td><td>429.08 (-17.96%)</td><td>483.00 (+7.57%)</td><td>289.70 (-9.36%)</td><td>118.55 <b>(-56.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>997.40 (n/a)</td><td>523.02 (n/a)</td><td>449.00 (n/a)</td><td>319.60 (n/a)</td><td>270.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-9.60%)</td><td>0.01 (+2.04%)</td><td>0.02 <b>(+37.30%)</b></td><td>0.01 (+4.14%)</td><td>0.00 (-8.76%)</td><td>583.30 (-3.98%)</td><td>412.60 (-2.56%)</td><td>326.80 <b>(-27.17%)</b></td><td>302.70 (+10.64%)</td><td>137.28 (+0.18%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.50 (n/a)</td><td>423.44 (n/a)</td><td>448.70 (n/a)</td><td>273.60 (n/a)</td><td>137.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-5.33%)</td><td>0.01 (-12.20%)</td><td>0.01 (-1.88%)</td><td>0.00 <b>(-68.62%)</b></td><td>0.00 <b>(+92.35%)</b></td><td>1906.70 <b>(+218.63%)</b></td><td>779.54 <b>(+50.21%)</b></td><td>530.10 (+1.92%)</td><td>405.20 (+5.63%)</td><td>632.55 <b>(+641.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.40 (n/a)</td><td>518.96 (n/a)</td><td>520.10 (n/a)</td><td>383.60 (n/a)</td><td>85.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(+48.14%)</b></td><td>0.02 (+19.15%)</td><td>0.02 (+8.42%)</td><td>0.02 <b>(+27.71%)</b></td><td>0.01 <b>(+78.48%)</b></td><td>561.10 <b>(-21.70%)</b></td><td>451.74 (-14.80%)</td><td>454.80 (-7.77%)</td><td>304.50 <b>(-32.50%)</b></td><td>95.06 (-11.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>716.60 (n/a)</td><td>530.24 (n/a)</td><td>493.10 (n/a)</td><td>451.10 (n/a)</td><td>107.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 <b>(+35.27%)</b></td><td>0.03 <b>(+44.02%)</b></td><td>0.02 <b>(+22.01%)</b></td><td>0.02 <b>(+76.63%)</b></td><td>0.01 <b>(+43.10%)</b></td><td>564.90 <b>(-43.39%)</b></td><td>416.04 <b>(-30.64%)</b></td><td>486.40 (-18.05%)</td><td>209.80 <b>(-26.05%)</b></td><td>165.85 <b>(-36.18%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>997.80 (n/a)</td><td>599.84 (n/a)</td><td>593.50 (n/a)</td><td>283.70 (n/a)</td><td>259.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (-9.36%)</td><td>0.03 <b>(+20.86%)</b></td><td>0.03 <b>(+60.95%)</b></td><td>0.02 <b>(+20.50%)</b></td><td>0.01 (-16.81%)</td><td>487.40 (-17.01%)</td><td>362.02 (-19.61%)</td><td>302.90 <b>(-37.87%)</b></td><td>276.00 (+10.31%)</td><td>104.04 <b>(-21.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.30 (n/a)</td><td>450.32 (n/a)</td><td>487.50 (n/a)</td><td>250.20 (n/a)</td><td>131.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (+7.00%)</td><td>0.03 (-7.01%)</td><td>0.03 (-13.13%)</td><td>0.02 <b>(+21.85%)</b></td><td>0.01 (-1.54%)</td><td>461.30 (-17.95%)</td><td>339.04 (+4.73%)</td><td>318.70 (+15.14%)</td><td>216.00 (-6.53%)</td><td>101.68 <b>(-25.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>323.74 (n/a)</td><td>276.80 (n/a)</td><td>231.10 (n/a)</td><td>136.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+2.61%)</td><td>0.02 <b>(-20.23%)</b></td><td>0.02 (-19.91%)</td><td>0.00 <b>(-76.40%)</b></td><td>0.01 <b>(+120.32%)</b></td><td>2179.40 <b>(+323.68%)</b></td><td>805.24 <b>(+86.53%)</b></td><td>512.10 <b>(+24.87%)</b></td><td>336.30 (-2.52%)</td><td>773.31 <b>(+898.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>514.40 (n/a)</td><td>431.70 (n/a)</td><td>410.10 (n/a)</td><td>345.00 (n/a)</td><td>77.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(-32.82%)</b></td><td>0.02 (-18.13%)</td><td>0.02 (+14.23%)</td><td>0.02 (+4.56%)</td><td>0.01 <b>(-58.83%)</b></td><td>630.30 (-4.36%)</td><td>508.14 (+8.63%)</td><td>478.60 (-12.46%)</td><td>361.00 <b>(+48.87%)</b></td><td>113.58 <b>(-39.24%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>659.00 (n/a)</td><td>467.78 (n/a)</td><td>546.70 (n/a)</td><td>242.50 (n/a)</td><td>186.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (+9.30%)</td><td>0.06 (-1.35%)</td><td>0.04 (-6.49%)</td><td>0.04 (+2.79%)</td><td>0.03 (+14.47%)</td><td>553.70 (-2.72%)</td><td>409.86 (+4.23%)</td><td>473.60 (+6.93%)</td><td>209.80 (-8.54%)</td><td>156.22 (+9.15%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.20 (n/a)</td><td>393.22 (n/a)</td><td>442.90 (n/a)</td><td>229.40 (n/a)</td><td>143.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (+5.63%)</td><td>0.05 (-14.43%)</td><td>0.04 <b>(-33.52%)</b></td><td>0.04 (+3.01%)</td><td>0.02 (+5.16%)</td><td>540.00 (-2.91%)</td><td>451.72 (+15.77%)</td><td>493.80 <b>(+50.46%)</b></td><td>222.70 (-5.31%)</td><td>130.87 (-13.80%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>556.20 (n/a)</td><td>390.20 (n/a)</td><td>328.20 (n/a)</td><td>235.20 (n/a)</td><td>151.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (+15.72%)</td><td>0.06 (+15.52%)</td><td>0.05 (+7.07%)</td><td>0.03 <b>(+190.88%)</b></td><td>0.03 (-9.73%)</td><td>633.00 <b>(-65.62%)</b></td><td>426.22 <b>(-38.14%)</b></td><td>435.80 (-6.60%)</td><td>215.00 (-13.59%)</td><td>172.08 <b>(-73.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1841.20 (n/a)</td><td>688.98 (n/a)</td><td>466.60 (n/a)</td><td>248.80 (n/a)</td><td>659.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (-6.18%)</td><td>0.05 <b>(-43.11%)</b></td><td>0.04 <b>(-52.88%)</b></td><td>0.03 <b>(-50.93%)</b></td><td>0.02 <b>(+111.81%)</b></td><td>623.80 <b>(+103.79%)</b></td><td>488.88 <b>(+95.55%)</b></td><td>515.60 <b>(+112.27%)</b></td><td>236.50 (+6.58%)</td><td>150.26 <b>(+333.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>306.10 (n/a)</td><td>250.00 (n/a)</td><td>242.90 (n/a)</td><td>221.90 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (+5.61%)</td><td>0.06 (-6.38%)</td><td>0.05 <b>(-22.89%)</b></td><td>0.04 <b>(+32.82%)</b></td><td>0.02 <b>(-22.43%)</b></td><td>543.00 <b>(-24.72%)</b></td><td>396.30 (-5.97%)</td><td>392.30 <b>(+29.69%)</b></td><td>216.40 (-5.34%)</td><td>128.65 <b>(-44.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>721.30 (n/a)</td><td>421.44 (n/a)</td><td>302.50 (n/a)</td><td>228.60 (n/a)</td><td>232.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 <b>(-30.83%)</b></td><td>0.04 (-12.03%)</td><td>0.04 (-4.02%)</td><td>0.03 (+1.01%)</td><td>0.01 <b>(-56.33%)</b></td><td>643.30 (-1.00%)</td><td>528.12 (+7.91%)</td><td>517.20 (+4.21%)</td><td>412.00 <b>(+44.56%)</b></td><td>87.75 <b>(-33.46%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>649.80 (n/a)</td><td>489.40 (n/a)</td><td>496.30 (n/a)</td><td>285.00 (n/a)</td><td>131.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.80 (n/a)</td><td>468.12 (n/a)</td><td>490.60 (n/a)</td><td>283.10 (n/a)</td><td>117.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.00 (n/a)</td><td>357.08 (n/a)</td><td>299.80 (n/a)</td><td>269.70 (n/a)</td><td>94.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>394.88 (n/a)</td><td>295.20 (n/a)</td><td>247.40 (n/a)</td><td>173.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.60 (n/a)</td><td>395.40 (n/a)</td><td>430.20 (n/a)</td><td>270.20 (n/a)</td><td>94.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.10 (n/a)</td><td>429.10 (n/a)</td><td>433.80 (n/a)</td><td>248.80 (n/a)</td><td>135.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>432.36 (n/a)</td><td>477.80 (n/a)</td><td>268.00 (n/a)</td><td>142.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>500.70 (n/a)</td><td>393.62 (n/a)</td><td>461.50 (n/a)</td><td>239.40 (n/a)</td><td>120.37 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.20 (n/a)</td><td>448.14 (n/a)</td><td>499.20 (n/a)</td><td>317.80 (n/a)</td><td>114.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1858.50 (n/a)</td><td>717.22 (n/a)</td><td>481.40 (n/a)</td><td>294.20 (n/a)</td><td>644.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (+19.89%)</td><td>0.13 (+13.56%)</td><td>0.14 <b>(+33.55%)</b></td><td>0.03 <b>(-66.33%)</b></td><td>0.07 <b>(+94.83%)</b></td><td>1785.50 <b>(+197.04%)</b></td><td>618.02 <b>(+37.61%)</b></td><td>344.30 <b>(-25.14%)</b></td><td>251.20 (-16.57%)</td><td>658.10 <b>(+401.64%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>601.10 (n/a)</td><td>449.12 (n/a)</td><td>459.90 (n/a)</td><td>301.10 (n/a)</td><td>131.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>544.00 (n/a)</td><td>355.96 (n/a)</td><td>276.00 (n/a)</td><td>239.00 (n/a)</td><td>143.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2473.20 (n/a)</td><td>843.82 (n/a)</td><td>487.60 (n/a)</td><td>246.80 (n/a)</td><td>917.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.90 (n/a)</td><td>404.06 (n/a)</td><td>420.20 (n/a)</td><td>299.20 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.40 (n/a)</td><td>359.06 (n/a)</td><td>316.60 (n/a)</td><td>201.50 (n/a)</td><td>150.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.30 (n/a)</td><td>408.48 (n/a)</td><td>348.70 (n/a)</td><td>320.70 (n/a)</td><td>111.37 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.90 (n/a)</td><td>453.64 (n/a)</td><td>472.80 (n/a)</td><td>348.90 (n/a)</td><td>85.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>771.50 (n/a)</td><td>416.18 (n/a)</td><td>313.80 (n/a)</td><td>276.60 (n/a)</td><td>206.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>625.60 (n/a)</td><td>424.26 (n/a)</td><td>435.60 (n/a)</td><td>266.00 (n/a)</td><td>158.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>502.50 (n/a)</td><td>424.50 (n/a)</td><td>450.30 (n/a)</td><td>234.20 (n/a)</td><td>110.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1872.40 (n/a)</td><td>774.22 (n/a)</td><td>499.30 (n/a)</td><td>445.70 (n/a)</td><td>615.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>695.40 (n/a)</td><td>473.44 (n/a)</td><td>540.20 (n/a)</td><td>240.10 (n/a)</td><td>185.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>501.20 (n/a)</td><td>433.32 (n/a)</td><td>451.30 (n/a)</td><td>339.40 (n/a)</td><td>65.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>517.90 (n/a)</td><td>348.80 (n/a)</td><td>325.10 (n/a)</td><td>245.80 (n/a)</td><td>103.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.46 (+3.60%)</td><td>3.18 (+14.44%)</td><td>2.66 (+12.45%)</td><td>1.77 (+0.74%)</td><td>1.20 (+17.75%)</td><td>5916.20 (-0.74%)</td><td>3723.34 (-10.59%)</td><td>3947.80 (-11.08%)</td><td>2350.50 (-3.47%)</td><td>1472.78 (+6.27%)</td><td>1827.25 (+3.60%)</td><td>1303.88 (+14.44%)</td><td>1087.93 (+12.45%)</td><td>725.97 (+0.74%)</td><td>492.81 (+17.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.31 (n/a)</td><td>2.78 (n/a)</td><td>2.36 (n/a)</td><td>1.76 (n/a)</td><td>1.02 (n/a)</td><td>5960.20 (n/a)</td><td>4164.16 (n/a)</td><td>4439.50 (n/a)</td><td>2435.10 (n/a)</td><td>1385.87 (n/a)</td><td>1763.74 (n/a)</td><td>1139.37 (n/a)</td><td>967.45 (n/a)</td><td>720.61 (n/a)</td><td>418.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.72 (-4.10%)</td><td>3.32 (+0.09%)</td><td>3.42 (+3.93%)</td><td>2.69 (-1.03%)</td><td>0.40 (-15.57%)</td><td>8772.50 (+1.04%)</td><td>7191.06 (-0.49%)</td><td>6895.10 (-3.79%)</td><td>6350.40 (+4.28%)</td><td>964.08 (-9.36%)</td><td>2113.52 (-4.10%)</td><td>1891.00 (+0.09%)</td><td>1946.58 (+3.93%)</td><td>1529.99 (-1.03%)</td><td>229.82 (-15.57%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.87 (n/a)</td><td>3.32 (n/a)</td><td>3.29 (n/a)</td><td>2.72 (n/a)</td><td>0.48 (n/a)</td><td>8681.80 (n/a)</td><td>7226.16 (n/a)</td><td>7166.40 (n/a)</td><td>6089.90 (n/a)</td><td>1063.63 (n/a)</td><td>2203.94 (n/a)</td><td>1889.29 (n/a)</td><td>1872.89 (n/a)</td><td>1545.97 (n/a)</td><td>272.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.91 (-3.61%)</td><td>3.00 (-5.96%)</td><td>3.21 (+2.78%)</td><td>1.84 <b>(-25.62%)</b></td><td>0.95 <b>(+31.65%)</b></td><td>9110.70 <b>(+34.44%)</b></td><td>6139.88 (+11.90%)</td><td>5233.00 (-2.71%)</td><td>4294.20 (+3.75%)</td><td>2160.33 <b>(+75.45%)</b></td><td>2000.38 (-3.61%)</td><td>1534.11 (-5.96%)</td><td>1641.50 (+2.78%)</td><td>942.84 <b>(-25.62%)</b></td><td>485.94 <b>(+31.65%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.05 (n/a)</td><td>3.19 (n/a)</td><td>3.12 (n/a)</td><td>2.48 (n/a)</td><td>0.72 (n/a)</td><td>6777.00 (n/a)</td><td>5487.16 (n/a)</td><td>5378.70 (n/a)</td><td>4139.00 (n/a)</td><td>1231.31 (n/a)</td><td>2075.35 (n/a)</td><td>1631.30 (n/a)</td><td>1597.03 (n/a)</td><td>1267.51 (n/a)</td><td>369.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.32 <b>(+36.33%)</b></td><td>0.89 <b>(+27.30%)</b></td><td>0.84 (+6.26%)</td><td>0.49 <b>(+95.49%)</b></td><td>0.35 <b>(+25.48%)</b></td><td>936.40 <b>(-48.85%)</b></td><td>593.58 <b>(-28.81%)</b></td><td>542.90 (-5.89%)</td><td>347.10 <b>(-26.66%)</b></td><td>245.65 <b>(-56.61%)</b></td><td>96.66 <b>(+36.33%)</b></td><td>64.74 <b>(+27.30%)</b></td><td>61.80 (+6.26%)</td><td>35.83 <b>(+95.49%)</b></td><td>25.63 <b>(+25.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.97 (n/a)</td><td>0.70 (n/a)</td><td>0.80 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>1830.60 (n/a)</td><td>833.74 (n/a)</td><td>576.90 (n/a)</td><td>473.30 (n/a)</td><td>566.19 (n/a)</td><td>70.90 (n/a)</td><td>50.85 (n/a)</td><td>58.16 (n/a)</td><td>18.33 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.02 <b>(-41.09%)</b></td><td>0.86 <b>(-32.64%)</b></td><td>0.91 <b>(-22.55%)</b></td><td>0.59 <b>(-38.69%)</b></td><td>0.16 <b>(-50.35%)</b></td><td>1115.30 <b>(+63.08%)</b></td><td>792.40 <b>(+46.35%)</b></td><td>718.20 <b>(+29.10%)</b></td><td>640.90 <b>(+69.77%)</b></td><td>186.31 <b>(+42.94%)</b></td><td>104.71 <b>(-41.09%)</b></td><td>87.80 <b>(-32.64%)</b></td><td>93.44 <b>(-22.55%)</b></td><td>60.17 <b>(-38.69%)</b></td><td>16.69 <b>(-50.35%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.74 (n/a)</td><td>1.27 (n/a)</td><td>1.18 (n/a)</td><td>0.96 (n/a)</td><td>0.33 (n/a)</td><td>683.90 (n/a)</td><td>541.44 (n/a)</td><td>556.30 (n/a)</td><td>377.50 (n/a)</td><td>130.34 (n/a)</td><td>177.76 (n/a)</td><td>130.35 (n/a)</td><td>120.64 (n/a)</td><td>98.13 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.85 (+8.48%)</td><td>1.20 <b>(+29.96%)</b></td><td>1.33 <b>(+45.21%)</b></td><td>0.40 <b>(+84.24%)</b></td><td>0.54 (-19.29%)</td><td>1883.00 <b>(-45.72%)</b></td><td>826.64 <b>(-45.93%)</b></td><td>566.10 <b>(-31.13%)</b></td><td>407.80 (-7.82%)</td><td>602.65 <b>(-55.19%)</b></td><td>205.71 (+8.48%)</td><td>133.76 <b>(+29.96%)</b></td><td>148.18 <b>(+45.21%)</b></td><td>44.55 <b>(+84.24%)</b></td><td>59.91 (-19.29%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.70 (n/a)</td><td>0.92 (n/a)</td><td>0.92 (n/a)</td><td>0.22 (n/a)</td><td>0.67 (n/a)</td><td>3469.30 (n/a)</td><td>1528.84 (n/a)</td><td>822.00 (n/a)</td><td>442.40 (n/a)</td><td>1344.92 (n/a)</td><td>189.63 (n/a)</td><td>102.93 (n/a)</td><td>102.05 (n/a)</td><td>24.18 (n/a)</td><td>74.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.49 (+6.85%)</td><td>1.18 (+13.77%)</td><td>1.30 (+12.20%)</td><td>0.58 <b>(+84.76%)</b></td><td>0.37 (-11.64%)</td><td>1814.80 <b>(-45.88%)</b></td><td>1005.16 <b>(-26.44%)</b></td><td>807.70 (-10.88%)</td><td>705.80 (-6.42%)</td><td>463.44 <b>(-58.34%)</b></td><td>190.16 (+6.85%)</td><td>150.48 (+13.77%)</td><td>166.17 (+12.20%)</td><td>73.96 <b>(+84.76%)</b></td><td>47.01 (-11.64%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.39 (n/a)</td><td>1.03 (n/a)</td><td>1.16 (n/a)</td><td>0.31 (n/a)</td><td>0.42 (n/a)</td><td>3353.00 (n/a)</td><td>1366.40 (n/a)</td><td>906.30 (n/a)</td><td>754.20 (n/a)</td><td>1112.56 (n/a)</td><td>177.96 (n/a)</td><td>132.27 (n/a)</td><td>148.09 (n/a)</td><td>40.03 (n/a)</td><td>53.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.88 (-1.06%)</td><td>1.25 <b>(-22.23%)</b></td><td>1.03 <b>(-37.39%)</b></td><td>0.85 <b>(-33.25%)</b></td><td>0.42 <b>(+48.06%)</b></td><td>1231.60 <b>(+49.79%)</b></td><td>913.28 <b>(+35.98%)</b></td><td>1014.10 <b>(+59.73%)</b></td><td>556.50 (+1.07%)</td><td>271.77 <b>(+119.58%)</b></td><td>241.19 (-1.06%)</td><td>159.59 <b>(-22.23%)</b></td><td>132.36 <b>(-37.39%)</b></td><td>108.98 <b>(-33.25%)</b></td><td>54.13 <b>(+48.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.90 (n/a)</td><td>1.60 (n/a)</td><td>1.65 (n/a)</td><td>1.28 (n/a)</td><td>0.29 (n/a)</td><td>822.20 (n/a)</td><td>671.64 (n/a)</td><td>634.90 (n/a)</td><td>550.60 (n/a)</td><td>123.77 (n/a)</td><td>243.77 (n/a)</td><td>205.21 (n/a)</td><td>211.40 (n/a)</td><td>163.25 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.04 (+6.71%)</td><td>1.47 (+10.75%)</td><td>1.34 (+11.20%)</td><td>1.02 (-0.89%)</td><td>0.38 (+9.56%)</td><td>1026.60 (+0.89%)</td><td>753.80 (-9.10%)</td><td>784.00 (-10.06%)</td><td>513.40 (-6.30%)</td><td>189.19 (+6.49%)</td><td>261.41 (+6.71%)</td><td>187.56 (+10.75%)</td><td>171.20 (+11.20%)</td><td>130.74 (-0.89%)</td><td>48.72 (+9.56%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.91 (n/a)</td><td>1.32 (n/a)</td><td>1.20 (n/a)</td><td>1.03 (n/a)</td><td>0.35 (n/a)</td><td>1017.50 (n/a)</td><td>829.26 (n/a)</td><td>871.70 (n/a)</td><td>547.90 (n/a)</td><td>177.67 (n/a)</td><td>244.98 (n/a)</td><td>169.36 (n/a)</td><td>153.97 (n/a)</td><td>131.91 (n/a)</td><td>44.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.70 (+4.03%)</td><td>1.37 (+6.90%)</td><td>1.28 (+5.63%)</td><td>0.97 (-0.39%)</td><td>0.31 <b>(+26.59%)</b></td><td>1078.30 (+0.39%)</td><td>796.94 (-5.14%)</td><td>817.70 (-5.34%)</td><td>618.50 (-3.87%)</td><td>188.80 (+17.96%)</td><td>217.02 (+4.03%)</td><td>175.78 (+6.90%)</td><td>164.14 (+5.63%)</td><td>124.48 (-0.39%)</td><td>39.43 <b>(+26.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.63 (n/a)</td><td>1.28 (n/a)</td><td>1.21 (n/a)</td><td>0.98 (n/a)</td><td>0.24 (n/a)</td><td>1074.10 (n/a)</td><td>840.14 (n/a)</td><td>863.80 (n/a)</td><td>643.40 (n/a)</td><td>160.05 (n/a)</td><td>208.60 (n/a)</td><td>164.43 (n/a)</td><td>155.39 (n/a)</td><td>124.96 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.92 (+13.92%)</td><td>1.53 (+9.47%)</td><td>1.37 (-1.04%)</td><td>1.28 (+19.37%)</td><td>0.28 (+7.95%)</td><td>819.50 (-16.22%)</td><td>704.10 (-8.98%)</td><td>763.80 (+1.05%)</td><td>546.60 (-12.22%)</td><td>121.56 (-19.17%)</td><td>245.55 (+13.92%)</td><td>195.63 (+9.47%)</td><td>175.72 (-1.04%)</td><td>163.79 (+19.37%)</td><td>36.34 (+7.95%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.68 (n/a)</td><td>1.40 (n/a)</td><td>1.39 (n/a)</td><td>1.07 (n/a)</td><td>0.26 (n/a)</td><td>978.20 (n/a)</td><td>773.60 (n/a)</td><td>755.90 (n/a)</td><td>622.70 (n/a)</td><td>150.38 (n/a)</td><td>215.54 (n/a)</td><td>178.70 (n/a)</td><td>177.56 (n/a)</td><td>137.21 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.84 (+2.88%)</td><td>1.25 (-2.85%)</td><td>1.46 (+18.82%)</td><td>0.47 (-10.21%)</td><td>0.54 (+4.87%)</td><td>2220.70 (+11.37%)</td><td>1064.74 (+7.15%)</td><td>717.00 (-15.85%)</td><td>569.30 (-2.80%)</td><td>679.71 (+17.25%)</td><td>235.75 (+2.88%)</td><td>159.45 (-2.85%)</td><td>187.19 (+18.82%)</td><td>60.44 (-10.21%)</td><td>69.44 (+4.87%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.79 (n/a)</td><td>1.28 (n/a)</td><td>1.23 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>1994.00 (n/a)</td><td>993.68 (n/a)</td><td>852.00 (n/a)</td><td>585.70 (n/a)</td><td>579.70 (n/a)</td><td>229.16 (n/a)</td><td>164.12 (n/a)</td><td>157.54 (n/a)</td><td>67.31 (n/a)</td><td>66.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.02 <b>(+57.53%)</b></td><td>0.69 <b>(+55.46%)</b></td><td>0.67 <b>(+41.60%)</b></td><td>0.47 <b>(+218.51%)</b></td><td>0.22 (+18.21%)</td><td>769.90 <b>(-68.60%)</b></td><td>559.88 <b>(-46.91%)</b></td><td>538.00 <b>(-29.38%)</b></td><td>354.80 <b>(-36.52%)</b></td><td>166.36 <b>(-78.87%)</b></td><td>47.28 <b>(+57.53%)</b></td><td>32.31 <b>(+55.46%)</b></td><td>31.18 <b>(+41.60%)</b></td><td>21.79 <b>(+218.51%)</b></td><td>10.14 (+18.21%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.64 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>2452.30 (n/a)</td><td>1054.62 (n/a)</td><td>761.80 (n/a)</td><td>558.90 (n/a)</td><td>787.14 (n/a)</td><td>30.02 (n/a)</td><td>20.79 (n/a)</td><td>22.02 (n/a)</td><td>6.84 (n/a)</td><td>8.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.06 (+4.58%)</td><td>2.40 (+16.43%)</td><td>2.52 <b>(+52.96%)</b></td><td>1.59 (+6.56%)</td><td>0.67 (+0.06%)</td><td>2637.30 (-6.16%)</td><td>1875.52 (-14.88%)</td><td>1666.20 <b>(-34.62%)</b></td><td>1370.10 (-4.38%)</td><td>568.65 (-11.40%)</td><td>783.69 (+4.58%)</td><td>613.81 (+16.43%)</td><td>644.43 <b>(+52.96%)</b></td><td>407.14 (+6.56%)</td><td>171.99 (+0.06%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.93 (n/a)</td><td>2.06 (n/a)</td><td>1.65 (n/a)</td><td>1.49 (n/a)</td><td>0.67 (n/a)</td><td>2810.40 (n/a)</td><td>2203.44 (n/a)</td><td>2548.60 (n/a)</td><td>1432.90 (n/a)</td><td>641.84 (n/a)</td><td>749.33 (n/a)</td><td>527.19 (n/a)</td><td>421.31 (n/a)</td><td>382.06 (n/a)</td><td>171.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.77 <b>(+35.74%)</b></td><td>2.95 <b>(+40.37%)</b></td><td>3.25 <b>(+38.87%)</b></td><td>1.06 <b>(+35.33%)</b></td><td>1.39 <b>(+27.93%)</b></td><td>2465.90 <b>(-26.11%)</b></td><td>1153.22 <b>(-30.39%)</b></td><td>807.40 <b>(-27.99%)</b></td><td>549.30 <b>(-26.33%)</b></td><td>767.81 <b>(-27.78%)</b></td><td>977.42 <b>(+35.74%)</b></td><td>603.39 <b>(+40.37%)</b></td><td>664.91 <b>(+38.87%)</b></td><td>217.71 <b>(+35.33%)</b></td><td>284.49 <b>(+27.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.52 (n/a)</td><td>2.10 (n/a)</td><td>2.34 (n/a)</td><td>0.79 (n/a)</td><td>1.09 (n/a)</td><td>3337.10 (n/a)</td><td>1656.72 (n/a)</td><td>1121.30 (n/a)</td><td>745.60 (n/a)</td><td>1063.20 (n/a)</td><td>720.04 (n/a)</td><td>429.85 (n/a)</td><td>478.79 (n/a)</td><td>160.88 (n/a)</td><td>222.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.34 (-1.23%)</td><td>2.71 (+1.27%)</td><td>2.80 (+6.08%)</td><td>2.00 (-12.12%)</td><td>0.60 <b>(+40.44%)</b></td><td>3924.40 (+13.79%)</td><td>3023.62 (+1.07%)</td><td>2807.10 (-5.74%)</td><td>2357.20 (+1.25%)</td><td>701.95 <b>(+63.26%)</b></td><td>1024.91 (-1.23%)</td><td>833.03 (+1.27%)</td><td>860.64 (+6.08%)</td><td>615.61 (-12.12%)</td><td>184.23 <b>(+40.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.38 (n/a)</td><td>2.68 (n/a)</td><td>2.64 (n/a)</td><td>2.28 (n/a)</td><td>0.43 (n/a)</td><td>3448.70 (n/a)</td><td>2991.60 (n/a)</td><td>2977.90 (n/a)</td><td>2328.20 (n/a)</td><td>429.96 (n/a)</td><td>1037.67 (n/a)</td><td>822.54 (n/a)</td><td>811.29 (n/a)</td><td>700.54 (n/a)</td><td>131.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.50 (n/a)</td><td>314.16 (n/a)</td><td>288.70 (n/a)</td><td>232.90 (n/a)</td><td>110.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.50 (n/a)</td><td>408.58 (n/a)</td><td>469.60 (n/a)</td><td>158.60 (n/a)</td><td>147.64 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.40 (n/a)</td><td>320.14 (n/a)</td><td>272.50 (n/a)</td><td>226.90 (n/a)</td><td>108.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.40 (n/a)</td><td>371.96 (n/a)</td><td>419.70 (n/a)</td><td>214.20 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.20 (n/a)</td><td>444.58 (n/a)</td><td>533.50 (n/a)</td><td>293.90 (n/a)</td><td>132.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.90 (n/a)</td><td>428.66 (n/a)</td><td>445.20 (n/a)</td><td>278.50 (n/a)</td><td>147.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.40 (n/a)</td><td>447.52 (n/a)</td><td>336.60 (n/a)</td><td>291.60 (n/a)</td><td>214.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2084.90 (n/a)</td><td>908.42 (n/a)</td><td>475.70 (n/a)</td><td>224.60 (n/a)</td><td>775.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1869.70 (n/a)</td><td>793.64 (n/a)</td><td>549.20 (n/a)</td><td>221.70 (n/a)</td><td>635.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1042.00 (n/a)</td><td>518.44 (n/a)</td><td>494.80 (n/a)</td><td>209.00 (n/a)</td><td>328.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.80 (n/a)</td><td>416.44 (n/a)</td><td>423.10 (n/a)</td><td>207.00 (n/a)</td><td>172.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.10 (n/a)</td><td>488.60 (n/a)</td><td>458.00 (n/a)</td><td>350.90 (n/a)</td><td>115.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>433.76 (n/a)</td><td>454.40 (n/a)</td><td>304.70 (n/a)</td><td>130.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.70 (n/a)</td><td>438.12 (n/a)</td><td>437.10 (n/a)</td><td>286.60 (n/a)</td><td>105.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.30 (n/a)</td><td>470.08 (n/a)</td><td>515.80 (n/a)</td><td>238.90 (n/a)</td><td>133.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>519.10 (n/a)</td><td>436.56 (n/a)</td><td>490.00 (n/a)</td><td>206.80 (n/a)</td><td>130.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>536.60 (n/a)</td><td>403.76 (n/a)</td><td>506.40 (n/a)</td><td>157.30 (n/a)</td><td>167.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.80 (n/a)</td><td>454.62 (n/a)</td><td>464.00 (n/a)</td><td>241.30 (n/a)</td><td>166.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>702.20 (n/a)</td><td>443.88 (n/a)</td><td>325.60 (n/a)</td><td>245.80 (n/a)</td><td>213.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>497.70 (n/a)</td><td>310.42 (n/a)</td><td>283.10 (n/a)</td><td>207.40 (n/a)</td><td>110.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>567.50 (n/a)</td><td>387.94 (n/a)</td><td>339.10 (n/a)</td><td>211.60 (n/a)</td><td>162.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>594.60 (n/a)</td><td>421.50 (n/a)</td><td>485.80 (n/a)</td><td>207.00 (n/a)</td><td>180.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>597.20 (n/a)</td><td>354.06 (n/a)</td><td>267.60 (n/a)</td><td>240.80 (n/a)</td><td>150.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>486.70 (n/a)</td><td>373.42 (n/a)</td><td>346.50 (n/a)</td><td>264.50 (n/a)</td><td>97.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.46 (-8.16%)</td><td>0.34 (-3.22%)</td><td>0.34 <b>(-20.98%)</b></td><td>0.13 <b>(+40.95%)</b></td><td>0.13 <b>(-21.54%)</b></td><td>1729.30 <b>(-29.05%)</b></td><td>812.24 (-13.44%)</td><td>656.70 <b>(+26.56%)</b></td><td>480.10 (+8.89%)</td><td>518.83 <b>(-38.79%)</b></td><td>19.66 (-8.16%)</td><td>14.30 (-3.22%)</td><td>14.37 <b>(-20.98%)</b></td><td>5.46 <b>(+40.95%)</b></td><td>5.46 <b>(-21.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.43 (n/a)</td><td>0.09 (n/a)</td><td>0.16 (n/a)</td><td>2437.40 (n/a)</td><td>938.34 (n/a)</td><td>518.90 (n/a)</td><td>440.90 (n/a)</td><td>847.64 (n/a)</td><td>21.40 (n/a)</td><td>14.77 (n/a)</td><td>18.19 (n/a)</td><td>3.87 (n/a)</td><td>6.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.49 <b>(-21.45%)</b></td><td>0.38 (-8.41%)</td><td>0.37 <b>(-25.37%)</b></td><td>0.31 <b>(+161.78%)</b></td><td>0.07 <b>(-64.97%)</b></td><td>704.60 <b>(-61.80%)</b></td><td>601.94 <b>(-21.80%)</b></td><td>593.70 <b>(+33.99%)</b></td><td>448.20 <b>(+27.33%)</b></td><td>105.20 <b>(-83.18%)</b></td><td>21.06 <b>(-21.45%)</b></td><td>16.11 (-8.41%)</td><td>15.90 <b>(-25.37%)</b></td><td>13.39 <b>(+161.78%)</b></td><td>3.11 <b>(-64.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.63 (n/a)</td><td>0.41 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>0.21 (n/a)</td><td>1844.40 (n/a)</td><td>769.70 (n/a)</td><td>443.10 (n/a)</td><td>352.00 (n/a)</td><td>625.36 (n/a)</td><td>26.81 (n/a)</td><td>17.59 (n/a)</td><td>21.30 (n/a)</td><td>5.12 (n/a)</td><td>8.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.31 (-0.76%)</td><td>0.31 (+0.78%)</td><td>0.31 (+1.46%)</td><td>0.30 (+0.95%)</td><td>0.00 <b>(-34.56%)</b></td><td>83736.60 (-0.94%)</td><td>82203.30 (-0.79%)</td><td>82064.90 (-1.44%)</td><td>80891.50 (+0.76%)</td><td>1103.58 <b>(-34.59%)</b></td><td>212.38 (-0.76%)</td><td>209.02 (+0.78%)</td><td>209.34 (+1.46%)</td><td>205.17 (+0.95%)</td><td>2.80 <b>(-34.56%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84528.40 (n/a)</td><td>82857.14 (n/a)</td><td>83264.10 (n/a)</td><td>80278.90 (n/a)</td><td>1687.29 (n/a)</td><td>214.00 (n/a)</td><td>207.41 (n/a)</td><td>206.33 (n/a)</td><td>203.24 (n/a)</td><td>4.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.15 (-0.18%)</td><td>1.11 (-2.17%)</td><td>1.09 (-5.03%)</td><td>1.08 (-0.70%)</td><td>0.03 (+16.54%)</td><td>23393.00 (+0.70%)</td><td>22768.66 (+2.24%)</td><td>23127.70 (+5.30%)</td><td>21913.90 (+0.18%)</td><td>681.88 (+17.62%)</td><td>783.97 (-0.18%)</td><td>755.09 (-2.17%)</td><td>742.83 (-5.03%)</td><td>734.40 (-0.70%)</td><td>22.86 (+16.54%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.15 (n/a)</td><td>1.08 (n/a)</td><td>0.03 (n/a)</td><td>23229.70 (n/a)</td><td>22269.32 (n/a)</td><td>21964.50 (n/a)</td><td>21874.30 (n/a)</td><td>579.73 (n/a)</td><td>785.39 (n/a)</td><td>771.87 (n/a)</td><td>782.17 (n/a)</td><td>739.56 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.80 (+0.33%)</td><td>0.78 (-0.89%)</td><td>0.79 (-0.24%)</td><td>0.76 (-3.16%)</td><td>0.02 <b>(+131.39%)</b></td><td>99381.70 (+3.27%)</td><td>96284.86 (+0.92%)</td><td>96070.50 (+0.25%)</td><td>94051.40 (-0.33%)</td><td>1991.66 <b>(+138.88%)</b></td><td>730.66 (+0.33%)</td><td>713.95 (-0.89%)</td><td>715.30 (-0.24%)</td><td>691.47 (-3.16%)</td><td>14.61 <b>(+131.40%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96236.70 (n/a)</td><td>95403.18 (n/a)</td><td>95835.60 (n/a)</td><td>94362.30 (n/a)</td><td>833.76 (n/a)</td><td>728.25 (n/a)</td><td>720.35 (n/a)</td><td>717.06 (n/a)</td><td>714.07 (n/a)</td><td>6.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.78 (+1.34%)</td><td>0.76 (-0.34%)</td><td>0.76 (-0.20%)</td><td>0.74 (-2.20%)</td><td>0.01 <b>(+216.71%)</b></td><td>101864.40 (+2.25%)</td><td>99159.98 (+0.37%)</td><td>98915.60 (+0.20%)</td><td>96846.60 (-1.32%)</td><td>1843.13 <b>(+219.91%)</b></td><td>709.57 (+1.34%)</td><td>693.21 (-0.34%)</td><td>694.73 (-0.20%)</td><td>674.62 (-2.20%)</td><td>12.82 <b>(+216.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99623.10 (n/a)</td><td>98793.76 (n/a)</td><td>98714.60 (n/a)</td><td>98142.50 (n/a)</td><td>576.15 (n/a)</td><td>700.20 (n/a)</td><td>695.60 (n/a)</td><td>696.14 (n/a)</td><td>689.79 (n/a)</td><td>4.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.90 (+0.28%)</td><td>0.89 (+0.14%)</td><td>0.90 (+0.63%)</td><td>0.88 (-0.26%)</td><td>0.01 <b>(+75.14%)</b></td><td>85982.90 (+0.26%)</td><td>84919.80 (-0.13%)</td><td>84313.10 (-0.63%)</td><td>84203.00 (-0.27%)</td><td>904.41 <b>(+75.02%)</b></td><td>816.12 (+0.28%)</td><td>809.30 (+0.14%)</td><td>815.05 (+0.63%)</td><td>799.22 (-0.26%)</td><td>8.59 <b>(+75.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85756.10 (n/a)</td><td>85031.92 (n/a)</td><td>84844.40 (n/a)</td><td>84434.90 (n/a)</td><td>516.75 (n/a)</td><td>813.88 (n/a)</td><td>808.18 (n/a)</td><td>809.95 (n/a)</td><td>801.34 (n/a)</td><td>4.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.55 (+0.85%)</td><td>4.75 <b>(+44.77%)</b></td><td>4.62 <b>(+101.25%)</b></td><td>4.00 <b>(+86.82%)</b></td><td>0.75 <b>(-50.90%)</b></td><td>2230.90 <b>(-46.47%)</b></td><td>1915.10 <b>(-39.54%)</b></td><td>1929.60 <b>(-50.31%)</b></td><td>1605.80 (-0.84%)</td><td>300.24 <b>(-75.34%)</b></td><td>334.33 (+0.85%)</td><td>286.01 <b>(+44.77%)</b></td><td>278.23 <b>(+101.25%)</b></td><td>240.65 <b>(+86.82%)</b></td><td>45.39 <b>(-50.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.50 (n/a)</td><td>3.28 (n/a)</td><td>2.30 (n/a)</td><td>2.14 (n/a)</td><td>1.53 (n/a)</td><td>4167.70 (n/a)</td><td>3167.64 (n/a)</td><td>3883.30 (n/a)</td><td>1619.40 (n/a)</td><td>1217.56 (n/a)</td><td>331.52 (n/a)</td><td>197.56 (n/a)</td><td>138.25 (n/a)</td><td>128.82 (n/a)</td><td>92.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.01 (-3.26%)</td><td>3.70 (+1.41%)</td><td>3.98 (-7.81%)</td><td>2.17 (-1.00%)</td><td>1.20 (-13.12%)</td><td>4116.80 (+1.01%)</td><td>2657.42 (-4.91%)</td><td>2240.30 (+8.47%)</td><td>1780.60 (+3.37%)</td><td>982.76 (-16.51%)</td><td>301.51 (-3.26%)</td><td>222.91 (+1.41%)</td><td>239.65 (-7.81%)</td><td>130.41 (-1.00%)</td><td>72.06 (-13.12%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.17 (n/a)</td><td>3.65 (n/a)</td><td>4.32 (n/a)</td><td>2.19 (n/a)</td><td>1.38 (n/a)</td><td>4075.70 (n/a)</td><td>2794.54 (n/a)</td><td>2065.40 (n/a)</td><td>1722.50 (n/a)</td><td>1177.05 (n/a)</td><td>311.68 (n/a)</td><td>219.81 (n/a)</td><td>259.94 (n/a)</td><td>131.73 (n/a)</td><td>82.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.08 <b>(-29.86%)</b></td><td>3.23 <b>(-27.70%)</b></td><td>3.15 <b>(-29.53%)</b></td><td>2.48 (+13.52%)</td><td>0.68 <b>(-53.37%)</b></td><td>3597.80 (-11.91%)</td><td>2865.24 <b>(+26.50%)</b></td><td>2827.50 <b>(+41.91%)</b></td><td>2182.30 <b>(+42.59%)</b></td><td>603.48 <b>(-42.58%)</b></td><td>246.02 <b>(-29.86%)</b></td><td>194.26 <b>(-27.70%)</b></td><td>189.88 <b>(-29.53%)</b></td><td>149.22 (+13.52%)</td><td>41.21 <b>(-53.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.82 (n/a)</td><td>4.46 (n/a)</td><td>4.47 (n/a)</td><td>2.18 (n/a)</td><td>1.47 (n/a)</td><td>4084.20 (n/a)</td><td>2264.94 (n/a)</td><td>1992.50 (n/a)</td><td>1530.50 (n/a)</td><td>1050.99 (n/a)</td><td>350.78 (n/a)</td><td>268.70 (n/a)</td><td>269.45 (n/a)</td><td>131.45 (n/a)</td><td>88.37 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.59 (-12.36%)</td><td>4.95 (-8.26%)</td><td>5.17 (-11.32%)</td><td>4.36 (-0.54%)</td><td>0.55 <b>(-37.93%)</b></td><td>8003.50 (+0.54%)</td><td>7109.62 (+7.64%)</td><td>6737.80 (+12.76%)</td><td>6239.20 (+14.10%)</td><td>805.47 <b>(-28.79%)</b></td><td>344.19 (-12.36%)</td><td>305.12 (-8.26%)</td><td>318.72 (-11.32%)</td><td>268.32 (-0.54%)</td><td>33.87 <b>(-37.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.38 (n/a)</td><td>5.40 (n/a)</td><td>5.84 (n/a)</td><td>4.38 (n/a)</td><td>0.89 (n/a)</td><td>7960.30 (n/a)</td><td>6604.70 (n/a)</td><td>5975.10 (n/a)</td><td>5468.30 (n/a)</td><td>1131.14 (n/a)</td><td>392.72 (n/a)</td><td>332.60 (n/a)</td><td>359.40 (n/a)</td><td>269.78 (n/a)</td><td>54.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.19 (-14.78%)</td><td>4.39 (-15.15%)</td><td>4.06 <b>(-22.52%)</b></td><td>3.85 (-13.09%)</td><td>0.57 (-9.54%)</td><td>9052.40 (+15.07%)</td><td>8043.90 (+17.99%)</td><td>8581.80 <b>(+29.06%)</b></td><td>6722.60 (+17.35%)</td><td>996.36 <b>(+21.51%)</b></td><td>319.44 (-14.78%)</td><td>270.46 (-15.15%)</td><td>250.24 <b>(-22.52%)</b></td><td>237.23 (-13.09%)</td><td>35.28 (-9.54%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.09 (n/a)</td><td>5.17 (n/a)</td><td>5.24 (n/a)</td><td>4.43 (n/a)</td><td>0.63 (n/a)</td><td>7867.10 (n/a)</td><td>6817.32 (n/a)</td><td>6649.60 (n/a)</td><td>5728.80 (n/a)</td><td>820.00 (n/a)</td><td>374.86 (n/a)</td><td>318.74 (n/a)</td><td>322.95 (n/a)</td><td>272.97 (n/a)</td><td>39.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.50 (-9.02%)</td><td>4.99 (-8.39%)</td><td>4.97 (-7.67%)</td><td>4.27 (-17.42%)</td><td>0.51 <b>(+42.26%)</b></td><td>8168.60 <b>(+21.09%)</b></td><td>7054.16 (+9.75%)</td><td>7012.30 (+8.31%)</td><td>6340.40 (+9.91%)</td><td>747.25 <b>(+88.35%)</b></td><td>338.70 (-9.02%)</td><td>307.07 (-8.39%)</td><td>306.24 (-7.67%)</td><td>262.89 (-17.42%)</td><td>31.26 <b>(+42.26%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.04 (n/a)</td><td>5.44 (n/a)</td><td>5.39 (n/a)</td><td>5.17 (n/a)</td><td>0.36 (n/a)</td><td>6745.90 (n/a)</td><td>6427.46 (n/a)</td><td>6474.40 (n/a)</td><td>5768.80 (n/a)</td><td>396.74 (n/a)</td><td>372.26 (n/a)</td><td>335.19 (n/a)</td><td>331.69 (n/a)</td><td>318.34 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.76 (-3.44%)</td><td>0.75 (-2.85%)</td><td>0.75 (-2.31%)</td><td>0.74 (-2.35%)</td><td>0.01 <b>(-31.48%)</b></td><td>101731.30 (+2.41%)</td><td>100199.04 (+2.92%)</td><td>100176.20 (+2.36%)</td><td>99066.30 (+3.56%)</td><td>1127.00 <b>(-27.24%)</b></td><td>693.67 (-3.44%)</td><td>685.90 (-2.85%)</td><td>685.99 (-2.31%)</td><td>675.50 (-2.35%)</td><td>7.70 <b>(-31.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99340.00 (n/a)</td><td>97354.32 (n/a)</td><td>97862.60 (n/a)</td><td>95661.10 (n/a)</td><td>1548.92 (n/a)</td><td>718.36 (n/a)</td><td>706.01 (n/a)</td><td>702.20 (n/a)</td><td>691.76 (n/a)</td><td>11.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.76 (-2.37%)</td><td>0.75 (-2.33%)</td><td>0.75 (-3.01%)</td><td>0.75 (-0.55%)</td><td>0.01 <b>(-50.55%)</b></td><td>101123.90 (+0.55%)</td><td>100260.52 (+2.37%)</td><td>100330.60 (+3.10%)</td><td>98909.60 (+2.43%)</td><td>857.11 <b>(-49.06%)</b></td><td>694.77 (-2.37%)</td><td>685.45 (-2.33%)</td><td>684.93 (-3.01%)</td><td>679.56 (-0.55%)</td><td>5.89 <b>(-50.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100568.40 (n/a)</td><td>97941.86 (n/a)</td><td>97311.20 (n/a)</td><td>96564.10 (n/a)</td><td>1682.72 (n/a)</td><td>711.65 (n/a)</td><td>701.80 (n/a)</td><td>706.18 (n/a)</td><td>683.31 (n/a)</td><td>11.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.89 (-0.36%)</td><td>0.89 (+2.28%)</td><td>0.89 (+1.20%)</td><td>0.88 (+7.15%)</td><td>0.01 <b>(-81.07%)</b></td><td>85914.10 (-6.67%)</td><td>84930.08 (-2.32%)</td><td>84724.50 (-1.19%)</td><td>84519.20 (+0.37%)</td><td>562.34 <b>(-82.28%)</b></td><td>813.06 (-0.36%)</td><td>809.16 (+2.28%)</td><td>811.09 (+1.20%)</td><td>799.86 (+7.15%)</td><td>5.32 <b>(-81.07%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.82 (n/a)</td><td>0.03 (n/a)</td><td>92054.30 (n/a)</td><td>86950.58 (n/a)</td><td>85743.00 (n/a)</td><td>84210.80 (n/a)</td><td>3173.93 (n/a)</td><td>816.04 (n/a)</td><td>791.15 (n/a)</td><td>801.46 (n/a)</td><td>746.51 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.37 (+19.27%)</td><td>2.95 <b>(+26.91%)</b></td><td>2.32 (-1.11%)</td><td>1.69 <b>(+60.51%)</b></td><td>1.29 <b>(+38.33%)</b></td><td>4759.40 <b>(-37.70%)</b></td><td>3175.14 <b>(-22.16%)</b></td><td>3471.70 (+1.13%)</td><td>1843.10 (-16.15%)</td><td>1287.91 <b>(-38.05%)</b></td><td>1146.97 (+19.27%)</td><td>773.35 <b>(+26.91%)</b></td><td>608.91 (-1.11%)</td><td>444.16 <b>(+60.51%)</b></td><td>337.83 <b>(+38.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.67 (n/a)</td><td>2.32 (n/a)</td><td>2.35 (n/a)</td><td>1.06 (n/a)</td><td>0.93 (n/a)</td><td>7639.40 (n/a)</td><td>4079.00 (n/a)</td><td>3433.00 (n/a)</td><td>2198.20 (n/a)</td><td>2078.95 (n/a)</td><td>961.65 (n/a)</td><td>609.35 (n/a)</td><td>615.76 (n/a)</td><td>276.71 (n/a)</td><td>244.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 <b>(-36.36%)</b></td><td>0.19 (-10.43%)</td><td>0.19 (-2.03%)</td><td>0.16 (+17.37%)</td><td>0.02 <b>(-75.09%)</b></td><td>7639.80 (-14.80%)</td><td>6705.70 (+3.99%)</td><td>6585.80 (+2.07%)</td><td>5925.20 <b>(+57.13%)</b></td><td>653.10 <b>(-64.66%)</b></td><td>11.33 <b>(-36.36%)</b></td><td>10.08 (-10.43%)</td><td>10.19 (-2.03%)</td><td>8.78 (+17.37%)</td><td>0.96 <b>(-75.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>8966.60 (n/a)</td><td>6448.22 (n/a)</td><td>6452.00 (n/a)</td><td>3770.80 (n/a)</td><td>1847.87 (n/a)</td><td>17.80 (n/a)</td><td>11.26 (n/a)</td><td>10.40 (n/a)</td><td>7.48 (n/a)</td><td>3.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.81 (n/a)</td><td>3.65 (n/a)</td><td>3.69 (n/a)</td><td>3.27 (n/a)</td><td>0.22 (n/a)</td><td>3.81 (n/a)</td><td>3.64 (n/a)</td><td>3.69 (n/a)</td><td>3.27 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.67 (-11.79%)</td><td>5.91 (-13.97%)</td><td>5.85 (-19.15%)</td><td>4.96 (-16.86%)</td><td>0.67 (-12.34%)</td><td>6.66 (-11.79%)</td><td>5.91 (-13.97%)</td><td>5.85 (-19.15%)</td><td>4.95 (-16.86%)</td><td>0.67 (-12.34%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>7.56 (n/a)</td><td>6.87 (n/a)</td><td>7.24 (n/a)</td><td>5.96 (n/a)</td><td>0.76 (n/a)</td><td>7.55 (n/a)</td><td>6.87 (n/a)</td><td>7.24 (n/a)</td><td>5.96 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>9.27 <b>(-25.11%)</b></td><td>8.63 (-2.65%)</td><td>8.53 (+4.08%)</td><td>8.16 (+16.87%)</td><td>0.47 <b>(-78.92%)</b></td><td>9.26 <b>(-25.11%)</b></td><td>8.62 (-2.65%)</td><td>8.53 (+4.08%)</td><td>8.16 (+16.87%)</td><td>0.47 <b>(-78.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>12.38 (n/a)</td><td>8.86 (n/a)</td><td>8.20 (n/a)</td><td>6.98 (n/a)</td><td>2.21 (n/a)</td><td>12.37 (n/a)</td><td>8.86 (n/a)</td><td>8.19 (n/a)</td><td>6.98 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.88 (n/a)</td><td>3.70 (n/a)</td><td>3.71 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td><td>3.88 (n/a)</td><td>3.70 (n/a)</td><td>3.71 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.87 (-8.89%)</td><td>5.59 (-17.51%)</td><td>5.69 (-19.84%)</td><td>4.39 <b>(-20.14%)</b></td><td>0.90 (+14.54%)</td><td>6.87 (-8.89%)</td><td>5.58 (-17.51%)</td><td>5.69 (-19.84%)</td><td>4.39 <b>(-20.14%)</b></td><td>0.90 (+14.54%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>7.55 (n/a)</td><td>6.77 (n/a)</td><td>7.10 (n/a)</td><td>5.50 (n/a)</td><td>0.78 (n/a)</td><td>7.54 (n/a)</td><td>6.77 (n/a)</td><td>7.09 (n/a)</td><td>5.49 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>10.35 <b>(-25.83%)</b></td><td>9.06 (-11.96%)</td><td>8.65 (-2.63%)</td><td>8.15 (-0.91%)</td><td>0.98 <b>(-62.72%)</b></td><td>10.35 <b>(-25.83%)</b></td><td>9.06 (-11.96%)</td><td>8.64 (-2.63%)</td><td>8.14 (-0.91%)</td><td>0.98 <b>(-62.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>13.96 (n/a)</td><td>10.29 (n/a)</td><td>8.88 (n/a)</td><td>8.22 (n/a)</td><td>2.62 (n/a)</td><td>13.95 (n/a)</td><td>10.29 (n/a)</td><td>8.87 (n/a)</td><td>8.22 (n/a)</td><td>2.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.99 (-3.26%)</td><td>1.69 <b>(-26.45%)</b></td><td>1.66 <b>(-40.38%)</b></td><td>1.02 (+1.67%)</td><td>0.80 (-11.12%)</td><td>2.99 (-3.26%)</td><td>1.69 <b>(-26.45%)</b></td><td>1.65 <b>(-40.38%)</b></td><td>1.02 (+1.67%)</td><td>0.80 (-11.12%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.10 (n/a)</td><td>2.30 (n/a)</td><td>2.78 (n/a)</td><td>1.00 (n/a)</td><td>0.90 (n/a)</td><td>3.09 (n/a)</td><td>2.29 (n/a)</td><td>2.78 (n/a)</td><td>1.00 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.55 (-4.17%)</td><td>0.37 (+17.22%)</td><td>0.41 <b>(+23.09%)</b></td><td>0.11 <b>(+40.38%)</b></td><td>0.16 <b>(-31.60%)</b></td><td>0.54 (-4.17%)</td><td>0.36 (+17.22%)</td><td>0.40 <b>(+23.09%)</b></td><td>0.11 <b>(+40.38%)</b></td><td>0.16 <b>(-31.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.57 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.56 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.69 (-6.80%)</td><td>0.54 <b>(-20.95%)</b></td><td>0.57 (-18.87%)</td><td>0.39 <b>(-38.02%)</b></td><td>0.14 <b>(+182.48%)</b></td><td>0.68 (-6.80%)</td><td>0.54 <b>(-20.95%)</b></td><td>0.56 (-18.87%)</td><td>0.38 <b>(-38.02%)</b></td><td>0.14 <b>(+182.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.74 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.62 (n/a)</td><td>0.05 (n/a)</td><td>0.73 (n/a)</td><td>0.68 (n/a)</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.72 (+9.70%)</td><td>1.78 (+2.77%)</td><td>1.87 (+1.75%)</td><td>0.44 (-2.89%)</td><td>0.84 (+6.38%)</td><td>2.68 (+9.70%)</td><td>1.75 (+2.77%)</td><td>1.84 (+1.75%)</td><td>0.43 (-2.89%)</td><td>0.83 (+6.38%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.48 (n/a)</td><td>1.73 (n/a)</td><td>1.83 (n/a)</td><td>0.45 (n/a)</td><td>0.79 (n/a)</td><td>2.44 (n/a)</td><td>1.71 (n/a)</td><td>1.80 (n/a)</td><td>0.44 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>350.50 (n/a)</td><td>295.00 (n/a)</td><td>291.50 (n/a)</td><td>214.70 (n/a)</td><td>52.61 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>407.50 (n/a)</td><td>314.58 (n/a)</td><td>282.70 (n/a)</td><td>222.80 (n/a)</td><td>85.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.90 (n/a)</td><td>497.04 (n/a)</td><td>556.60 (n/a)</td><td>353.30 (n/a)</td><td>112.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.50 (n/a)</td><td>435.78 (n/a)</td><td>476.10 (n/a)</td><td>299.20 (n/a)</td><td>98.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.30 (n/a)</td><td>532.36 (n/a)</td><td>559.50 (n/a)</td><td>404.60 (n/a)</td><td>93.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>652.80 (n/a)</td><td>424.60 (n/a)</td><td>376.90 (n/a)</td><td>266.20 (n/a)</td><td>153.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.20 (n/a)</td><td>334.00 (n/a)</td><td>305.90 (n/a)</td><td>231.50 (n/a)</td><td>102.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1884.80 (n/a)</td><td>994.92 (n/a)</td><td>649.70 (n/a)</td><td>204.20 (n/a)</td><td>819.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.80 (n/a)</td><td>312.48 (n/a)</td><td>268.20 (n/a)</td><td>237.00 (n/a)</td><td>88.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>377.60 (n/a)</td><td>378.50 (n/a)</td><td>223.90 (n/a)</td><td>148.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>434.28 (n/a)</td><td>509.10 (n/a)</td><td>255.40 (n/a)</td><td>155.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.00 (n/a)</td><td>410.92 (n/a)</td><td>364.40 (n/a)</td><td>255.60 (n/a)</td><td>145.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>624.40 (n/a)</td><td>418.66 (n/a)</td><td>335.40 (n/a)</td><td>262.40 (n/a)</td><td>165.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>434.14 (n/a)</td><td>444.10 (n/a)</td><td>234.80 (n/a)</td><td>136.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.40 (n/a)</td><td>390.88 (n/a)</td><td>430.70 (n/a)</td><td>259.20 (n/a)</td><td>119.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.70 (n/a)</td><td>484.60 (n/a)</td><td>504.70 (n/a)</td><td>331.70 (n/a)</td><td>102.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>525.70 (n/a)</td><td>493.28 (n/a)</td><td>509.70 (n/a)</td><td>454.60 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.00 (n/a)</td><td>398.08 (n/a)</td><td>417.60 (n/a)</td><td>237.30 (n/a)</td><td>117.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1936.30 (n/a)</td><td>736.64 (n/a)</td><td>506.60 (n/a)</td><td>303.90 (n/a)</td><td>678.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>635.80 (n/a)</td><td>497.92 (n/a)</td><td>515.80 (n/a)</td><td>287.20 (n/a)</td><td>127.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.80 (n/a)</td><td>413.10 (n/a)</td><td>363.60 (n/a)</td><td>261.30 (n/a)</td><td>167.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>514.90 (n/a)</td><td>441.74 (n/a)</td><td>460.10 (n/a)</td><td>353.20 (n/a)</td><td>67.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>581.40 (n/a)</td><td>387.36 (n/a)</td><td>405.30 (n/a)</td><td>209.30 (n/a)</td><td>139.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>611.70 (n/a)</td><td>486.90 (n/a)</td><td>532.50 (n/a)</td><td>363.70 (n/a)</td><td>111.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-1.29%)</td><td>0.01 (+16.55%)</td><td>0.02 (+8.66%)</td><td>0.01 <b>(+96.66%)</b></td><td>0.00 <b>(-43.26%)</b></td><td>376.10 <b>(-49.16%)</b></td><td>281.18 <b>(-24.82%)</b></td><td>267.60 (-7.98%)</td><td>238.90 (+1.31%)</td><td>55.56 <b>(-73.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>739.70 (n/a)</td><td>374.02 (n/a)</td><td>290.80 (n/a)</td><td>235.80 (n/a)</td><td>206.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-0.79%)</td><td>0.01 (-18.96%)</td><td>0.01 <b>(-34.39%)</b></td><td>0.01 <b>(-32.85%)</b></td><td>0.00 <b>(+116.67%)</b></td><td>552.90 <b>(+48.91%)</b></td><td>395.68 <b>(+37.53%)</b></td><td>418.70 <b>(+52.42%)</b></td><td>241.00 (+0.79%)</td><td>149.24 <b>(+200.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>371.30 (n/a)</td><td>287.70 (n/a)</td><td>274.70 (n/a)</td><td>239.10 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+3.90%)</td><td>0.02 <b>(+53.81%)</b></td><td>0.02 <b>(+107.09%)</b></td><td>0.01 <b>(+176.70%)</b></td><td>0.00 <b>(-42.61%)</b></td><td>408.40 <b>(-63.86%)</b></td><td>269.82 <b>(-50.05%)</b></td><td>238.20 <b>(-51.71%)</b></td><td>224.60 (-3.73%)</td><td>77.72 <b>(-78.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1130.10 (n/a)</td><td>540.14 (n/a)</td><td>493.30 (n/a)</td><td>233.30 (n/a)</td><td>360.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+21.80%)</b></td><td>0.01 (+7.01%)</td><td>0.02 (+9.17%)</td><td>0.01 (+2.60%)</td><td>0.00 <b>(+31.05%)</b></td><td>577.90 (-2.55%)</td><td>326.22 (-3.88%)</td><td>264.80 (-8.41%)</td><td>200.00 (-17.86%)</td><td>147.89 (+3.31%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.00 (n/a)</td><td>339.38 (n/a)</td><td>289.10 (n/a)</td><td>243.50 (n/a)</td><td>143.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+85.73%)</b></td><td>0.01 <b>(+100.06%)</b></td><td>0.01 <b>(+92.15%)</b></td><td>0.01 <b>(+361.28%)</b></td><td>0.00 (+15.58%)</td><td>521.40 <b>(-78.32%)</b></td><td>337.14 <b>(-63.07%)</b></td><td>299.70 <b>(-47.95%)</b></td><td>247.20 <b>(-46.17%)</b></td><td>107.08 <b>(-87.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2405.30 (n/a)</td><td>912.96 (n/a)</td><td>575.80 (n/a)</td><td>459.20 (n/a)</td><td>835.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 <b>(+20.43%)</b></td><td>0.01 <b>(+32.18%)</b></td><td>0.01 <b>(+51.03%)</b></td><td>0.01 (+6.28%)</td><td>0.00 <b>(+44.36%)</b></td><td>520.80 (-5.89%)</td><td>378.98 <b>(-23.11%)</b></td><td>360.40 <b>(-33.80%)</b></td><td>294.80 (-16.96%)</td><td>93.51 (+10.25%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.40 (n/a)</td><td>492.90 (n/a)</td><td>544.40 (n/a)</td><td>355.00 (n/a)</td><td>84.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(-20.06%)</b></td><td>0.02 <b>(-23.64%)</b></td><td>0.02 (+7.12%)</td><td>0.00 <b>(-70.61%)</b></td><td>0.01 (+14.33%)</td><td>1879.00 <b>(+240.28%)</b></td><td>793.50 <b>(+96.34%)</b></td><td>433.20 (-6.66%)</td><td>267.10 <b>(+25.11%)</b></td><td>690.58 <b>(+371.42%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.20 (n/a)</td><td>404.14 (n/a)</td><td>464.10 (n/a)</td><td>213.50 (n/a)</td><td>146.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-12.97%)</td><td>0.02 (-12.18%)</td><td>0.03 (-6.42%)</td><td>0.01 (-13.12%)</td><td>0.01 (+2.75%)</td><td>575.40 (+15.10%)</td><td>360.74 (+16.05%)</td><td>284.00 (+6.85%)</td><td>265.10 (+14.91%)</td><td>134.17 <b>(+24.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>310.86 (n/a)</td><td>265.80 (n/a)</td><td>230.70 (n/a)</td><td>108.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-12.91%)</td><td>0.03 (-6.09%)</td><td>0.03 (-6.15%)</td><td>0.02 (-7.91%)</td><td>0.01 (-16.15%)</td><td>439.20 (+8.61%)</td><td>318.02 (+5.30%)</td><td>285.80 (+6.56%)</td><td>244.70 (+14.83%)</td><td>85.83 (-1.71%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>404.40 (n/a)</td><td>302.00 (n/a)</td><td>268.20 (n/a)</td><td>213.10 (n/a)</td><td>87.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-11.54%)</td><td>0.02 (-2.67%)</td><td>0.03 (-4.13%)</td><td>0.01 (+6.03%)</td><td>0.01 (-17.20%)</td><td>596.70 (-5.69%)</td><td>373.56 (-0.66%)</td><td>304.30 (+4.32%)</td><td>255.90 (+13.03%)</td><td>141.00 (-13.58%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.70 (n/a)</td><td>376.06 (n/a)</td><td>291.70 (n/a)</td><td>226.40 (n/a)</td><td>163.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-5.25%)</td><td>0.02 <b>(-29.38%)</b></td><td>0.02 <b>(-47.15%)</b></td><td>0.01 <b>(-28.16%)</b></td><td>0.01 <b>(+23.86%)</b></td><td>626.90 <b>(+39.19%)</b></td><td>483.90 <b>(+49.88%)</b></td><td>534.90 <b>(+89.21%)</b></td><td>253.20 (+5.54%)</td><td>151.77 <b>(+76.65%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.40 (n/a)</td><td>322.86 (n/a)</td><td>282.70 (n/a)</td><td>239.90 (n/a)</td><td>85.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(-33.52%)</b></td><td>0.02 <b>(-28.01%)</b></td><td>0.02 <b>(-38.20%)</b></td><td>0.02 (+7.84%)</td><td>0.00 <b>(-65.78%)</b></td><td>517.20 (-7.26%)</td><td>469.68 <b>(+31.27%)</b></td><td>503.10 <b>(+61.82%)</b></td><td>396.80 <b>(+50.42%)</b></td><td>53.85 <b>(-54.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.70 (n/a)</td><td>357.80 (n/a)</td><td>310.90 (n/a)</td><td>263.80 (n/a)</td><td>117.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-18.34%)</td><td>0.02 (-9.09%)</td><td>0.02 (-18.78%)</td><td>0.02 <b>(+31.53%)</b></td><td>0.01 <b>(-44.60%)</b></td><td>508.00 <b>(-23.97%)</b></td><td>367.64 (-1.96%)</td><td>332.70 <b>(+23.13%)</b></td><td>275.50 <b>(+22.44%)</b></td><td>96.78 <b>(-48.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.20 (n/a)</td><td>374.98 (n/a)</td><td>270.20 (n/a)</td><td>225.00 (n/a)</td><td>187.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+9.91%)</td><td>0.02 (-5.65%)</td><td>0.02 (-11.20%)</td><td>0.02 (-3.40%)</td><td>0.01 (+18.39%)</td><td>498.70 (+3.53%)</td><td>408.30 (+7.24%)</td><td>440.20 (+12.61%)</td><td>239.80 (-9.03%)</td><td>98.51 (+3.23%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.70 (n/a)</td><td>380.72 (n/a)</td><td>390.90 (n/a)</td><td>263.60 (n/a)</td><td>95.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 <b>(+28.83%)</b></td><td>0.06 (-0.98%)</td><td>0.07 (+9.04%)</td><td>0.03 <b>(-52.39%)</b></td><td>0.02 <b>(+427.73%)</b></td><td>599.00 <b>(+110.03%)</b></td><td>311.26 (+17.02%)</td><td>248.10 (-8.28%)</td><td>191.90 <b>(-22.37%)</b></td><td>163.63 <b>(+855.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>285.20 (n/a)</td><td>266.00 (n/a)</td><td>270.50 (n/a)</td><td>247.20 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (+1.55%)</td><td>0.04 (-2.65%)</td><td>0.03 (-6.00%)</td><td>0.01 (-9.56%)</td><td>0.02 (-2.02%)</td><td>2075.00 (+10.57%)</td><td>723.76 (+6.61%)</td><td>502.90 (+6.39%)</td><td>247.00 (-1.52%)</td><td>765.60 (+12.30%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1876.70 (n/a)</td><td>678.88 (n/a)</td><td>472.70 (n/a)</td><td>250.80 (n/a)</td><td>681.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 <b>(+21.43%)</b></td><td>0.06 (+2.56%)</td><td>0.06 (+1.97%)</td><td>0.04 (-8.01%)</td><td>0.02 <b>(+65.70%)</b></td><td>457.70 (+8.72%)</td><td>327.06 (+4.72%)</td><td>276.00 (-1.92%)</td><td>186.50 (-17.66%)</td><td>123.08 <b>(+58.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>421.00 (n/a)</td><td>312.32 (n/a)</td><td>281.40 (n/a)</td><td>226.50 (n/a)</td><td>77.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (-7.70%)</td><td>0.05 (+5.72%)</td><td>0.06 (+11.99%)</td><td>0.04 <b>(+28.39%)</b></td><td>0.01 (-16.82%)</td><td>426.30 <b>(-22.11%)</b></td><td>327.26 (-8.55%)</td><td>270.90 (-10.71%)</td><td>249.40 (+8.34%)</td><td>88.45 <b>(-28.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.30 (n/a)</td><td>357.84 (n/a)</td><td>303.40 (n/a)</td><td>230.20 (n/a)</td><td>124.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (+14.40%)</td><td>0.05 (+17.11%)</td><td>0.04 (-0.47%)</td><td>0.04 <b>(+69.22%)</b></td><td>0.02 (+6.53%)</td><td>458.70 <b>(-40.90%)</b></td><td>348.94 (-19.17%)</td><td>375.80 (+0.48%)</td><td>240.50 (-12.58%)</td><td>100.06 <b>(-49.96%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>776.20 (n/a)</td><td>431.70 (n/a)</td><td>374.00 (n/a)</td><td>275.10 (n/a)</td><td>199.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (+14.64%)</td><td>0.05 (+18.41%)</td><td>0.04 (+3.98%)</td><td>0.03 (-5.29%)</td><td>0.02 <b>(+49.94%)</b></td><td>567.60 (+5.60%)</td><td>394.40 (-10.95%)</td><td>445.20 (-3.82%)</td><td>243.00 (-12.78%)</td><td>136.46 <b>(+38.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>537.50 (n/a)</td><td>442.90 (n/a)</td><td>462.90 (n/a)</td><td>278.60 (n/a)</td><td>98.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 <b>(+37.37%)</b></td><td>0.10 <b>(+43.82%)</b></td><td>0.10 <b>(+51.25%)</b></td><td>0.05 (-18.08%)</td><td>0.04 <b>(+129.78%)</b></td><td>706.70 <b>(+22.08%)</b></td><td>368.20 <b>(-21.86%)</b></td><td>318.90 <b>(-33.89%)</b></td><td>245.00 <b>(-27.21%)</b></td><td>192.68 <b>(+119.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>578.90 (n/a)</td><td>471.18 (n/a)</td><td>482.40 (n/a)</td><td>336.60 (n/a)</td><td>87.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 <b>(+62.42%)</b></td><td>0.09 (+16.28%)</td><td>0.08 (+8.17%)</td><td>0.06 (-5.71%)</td><td>0.03 <b>(+217.04%)</b></td><td>559.20 (+6.05%)</td><td>420.06 (-7.56%)</td><td>435.90 (-7.55%)</td><td>231.10 <b>(-38.44%)</b></td><td>118.63 <b>(+93.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>527.30 (n/a)</td><td>454.42 (n/a)</td><td>471.50 (n/a)</td><td>375.40 (n/a)</td><td>61.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+12.48%)</td><td>0.12 <b>(+29.40%)</b></td><td>0.11 <b>(+53.54%)</b></td><td>0.08 <b>(+39.27%)</b></td><td>0.03 (-19.77%)</td><td>406.50 <b>(-28.19%)</b></td><td>294.22 <b>(-26.97%)</b></td><td>300.50 <b>(-34.89%)</b></td><td>227.40 (-11.10%)</td><td>72.06 <b>(-46.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.10 (n/a)</td><td>402.90 (n/a)</td><td>461.50 (n/a)</td><td>255.80 (n/a)</td><td>135.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (-4.92%)</td><td>0.09 (-9.06%)</td><td>0.08 <b>(-31.99%)</b></td><td>0.06 <b>(+228.57%)</b></td><td>0.03 <b>(-37.60%)</b></td><td>563.80 <b>(-69.57%)</b></td><td>385.26 <b>(-34.11%)</b></td><td>407.60 <b>(+47.04%)</b></td><td>255.60 (+5.19%)</td><td>125.46 <b>(-82.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1852.50 (n/a)</td><td>584.74 (n/a)</td><td>277.20 (n/a)</td><td>243.00 (n/a)</td><td>708.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (+7.36%)</td><td>0.09 <b>(+32.46%)</b></td><td>0.10 <b>(+75.49%)</b></td><td>0.05 (+2.60%)</td><td>0.03 (+16.13%)</td><td>645.80 (-2.54%)</td><td>398.62 <b>(-23.18%)</b></td><td>317.90 <b>(-43.02%)</b></td><td>282.80 (-6.85%)</td><td>153.21 (+5.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>662.60 (n/a)</td><td>518.90 (n/a)</td><td>557.90 (n/a)</td><td>303.60 (n/a)</td><td>145.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-16.83%)</td><td>0.01 (-8.49%)</td><td>0.01 <b>(-21.97%)</b></td><td>0.01 (+6.96%)</td><td>0.00 <b>(-23.30%)</b></td><td>554.10 (-6.50%)</td><td>408.18 (+5.01%)</td><td>396.30 <b>(+28.17%)</b></td><td>289.60 <b>(+20.27%)</b></td><td>121.06 (-18.91%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.60 (n/a)</td><td>388.72 (n/a)</td><td>309.20 (n/a)</td><td>240.80 (n/a)</td><td>149.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-4.73%)</td><td>0.01 (-16.99%)</td><td>0.01 (-12.54%)</td><td>0.01 <b>(-31.33%)</b></td><td>0.00 <b>(+59.60%)</b></td><td>489.30 <b>(+45.63%)</b></td><td>336.34 <b>(+25.61%)</b></td><td>295.50 (+14.36%)</td><td>243.90 (+4.99%)</td><td>95.87 <b>(+141.73%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>336.00 (n/a)</td><td>267.76 (n/a)</td><td>258.40 (n/a)</td><td>232.30 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+4.06%)</td><td>0.01 (-10.59%)</td><td>0.01 (-11.50%)</td><td>0.01 <b>(-23.37%)</b></td><td>0.00 <b>(+20.51%)</b></td><td>625.20 <b>(+30.49%)</b></td><td>443.96 (+17.29%)</td><td>472.10 (+13.00%)</td><td>223.70 (-3.91%)</td><td>151.90 <b>(+42.05%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.10 (n/a)</td><td>378.50 (n/a)</td><td>417.80 (n/a)</td><td>232.80 (n/a)</td><td>106.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-2.85%)</td><td>0.01 (-0.31%)</td><td>0.01 (-1.98%)</td><td>0.01 (+7.31%)</td><td>0.00 (-8.55%)</td><td>461.80 (-6.80%)</td><td>370.08 (-1.27%)</td><td>422.60 (+2.03%)</td><td>242.90 (+2.92%)</td><td>107.44 (-10.33%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.50 (n/a)</td><td>374.84 (n/a)</td><td>414.20 (n/a)</td><td>236.00 (n/a)</td><td>119.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-6.85%)</td><td>0.01 (-13.60%)</td><td>0.01 (-11.23%)</td><td>0.01 (+5.20%)</td><td>0.00 (-12.27%)</td><td>531.60 (-4.94%)</td><td>360.26 (+12.93%)</td><td>306.60 (+12.64%)</td><td>252.90 (+7.34%)</td><td>114.97 (-14.92%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.20 (n/a)</td><td>319.02 (n/a)</td><td>272.20 (n/a)</td><td>235.60 (n/a)</td><td>135.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 <b>(-21.12%)</b></td><td>0.01 (-11.95%)</td><td>0.01 (-7.33%)</td><td>0.01 (-17.83%)</td><td>0.00 (-11.69%)</td><td>553.70 <b>(+21.69%)</b></td><td>338.72 (+14.77%)</td><td>290.40 (+7.92%)</td><td>274.80 <b>(+26.75%)</b></td><td>120.53 <b>(+30.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.00 (n/a)</td><td>295.12 (n/a)</td><td>269.10 (n/a)</td><td>216.80 (n/a)</td><td>92.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-17.23%)</td><td>0.01 <b>(-24.65%)</b></td><td>0.01 <b>(-46.70%)</b></td><td>0.01 (-19.54%)</td><td>0.00 (-12.87%)</td><td>556.10 <b>(+24.27%)</b></td><td>431.40 <b>(+33.71%)</b></td><td>483.50 <b>(+87.62%)</b></td><td>278.00 <b>(+20.82%)</b></td><td>132.61 <b>(+26.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>447.50 (n/a)</td><td>322.64 (n/a)</td><td>257.70 (n/a)</td><td>230.10 (n/a)</td><td>105.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-18.13%)</td><td>0.01 (-10.35%)</td><td>0.01 <b>(-20.63%)</b></td><td>0.01 <b>(+52.23%)</b></td><td>0.00 <b>(-50.53%)</b></td><td>527.70 <b>(-34.32%)</b></td><td>409.50 (-2.25%)</td><td>378.10 <b>(+25.99%)</b></td><td>322.70 <b>(+22.14%)</b></td><td>88.77 <b>(-60.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>803.40 (n/a)</td><td>418.94 (n/a)</td><td>300.10 (n/a)</td><td>264.20 (n/a)</td><td>225.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+22.23%)</b></td><td>0.01 (-2.51%)</td><td>0.01 (+9.21%)</td><td>0.01 <b>(-36.89%)</b></td><td>0.00 <b>(+90.52%)</b></td><td>713.70 <b>(+58.46%)</b></td><td>420.50 (+13.35%)</td><td>367.70 (-8.44%)</td><td>241.70 (-18.18%)</td><td>180.42 <b>(+163.57%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.40 (n/a)</td><td>370.98 (n/a)</td><td>401.60 (n/a)</td><td>295.40 (n/a)</td><td>68.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-19.68%)</td><td>0.01 (-15.22%)</td><td>0.01 <b>(-30.90%)</b></td><td>0.01 (+12.28%)</td><td>0.00 <b>(-49.15%)</b></td><td>513.10 (-10.94%)</td><td>430.86 (+10.06%)</td><td>436.20 <b>(+44.72%)</b></td><td>331.10 <b>(+24.52%)</b></td><td>80.29 <b>(-43.73%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>391.48 (n/a)</td><td>301.40 (n/a)</td><td>265.90 (n/a)</td><td>142.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-13.46%)</td><td>0.01 <b>(-25.92%)</b></td><td>0.01 (-15.40%)</td><td>0.00 <b>(-31.92%)</b></td><td>0.00 (-0.37%)</td><td>942.80 <b>(+46.88%)</b></td><td>691.64 <b>(+41.36%)</b></td><td>653.70 (+18.21%)</td><td>361.70 (+15.52%)</td><td>238.04 <b>(+73.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.90 (n/a)</td><td>489.28 (n/a)</td><td>553.00 (n/a)</td><td>313.10 (n/a)</td><td>137.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(-45.70%)</b></td><td>0.02 <b>(-35.00%)</b></td><td>0.02 <b>(-32.34%)</b></td><td>0.01 <b>(-31.05%)</b></td><td>0.01 <b>(-55.63%)</b></td><td>654.60 <b>(+45.05%)</b></td><td>474.16 <b>(+47.31%)</b></td><td>484.10 <b>(+47.82%)</b></td><td>316.10 <b>(+84.21%)</b></td><td>126.57 <b>(+24.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.30 (n/a)</td><td>321.88 (n/a)</td><td>327.50 (n/a)</td><td>171.60 (n/a)</td><td>101.34 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(-30.93%)</b></td><td>0.02 (-11.86%)</td><td>0.02 <b>(-22.77%)</b></td><td>0.02 <b>(+45.04%)</b></td><td>0.00 <b>(-70.95%)</b></td><td>449.40 <b>(-31.06%)</b></td><td>393.88 (-2.03%)</td><td>393.00 <b>(+29.49%)</b></td><td>332.60 <b>(+44.80%)</b></td><td>52.84 <b>(-71.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.90 (n/a)</td><td>402.04 (n/a)</td><td>303.50 (n/a)</td><td>229.70 (n/a)</td><td>186.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-17.07%)</td><td>0.02 (-18.84%)</td><td>0.01 (-1.46%)</td><td>0.01 (-1.09%)</td><td>0.00 <b>(-44.44%)</b></td><td>616.20 (+1.12%)</td><td>531.46 (+15.29%)</td><td>560.00 (+1.49%)</td><td>348.90 <b>(+20.56%)</b></td><td>109.06 <b>(-30.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>460.96 (n/a)</td><td>551.80 (n/a)</td><td>289.40 (n/a)</td><td>156.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(-34.01%)</b></td><td>0.02 <b>(-33.25%)</b></td><td>0.02 <b>(-35.06%)</b></td><td>0.01 (-10.09%)</td><td>0.00 <b>(-54.33%)</b></td><td>640.70 (+11.23%)</td><td>522.38 <b>(+42.98%)</b></td><td>512.70 <b>(+53.96%)</b></td><td>407.50 <b>(+51.54%)</b></td><td>93.01 <b>(-24.76%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.00 (n/a)</td><td>365.34 (n/a)</td><td>333.00 (n/a)</td><td>268.90 (n/a)</td><td>123.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (+10.70%)</td><td>0.03 <b>(+43.61%)</b></td><td>0.03 <b>(+81.53%)</b></td><td>0.02 <b>(+83.82%)</b></td><td>0.01 <b>(-20.12%)</b></td><td>507.30 <b>(-45.60%)</b></td><td>340.84 <b>(-42.75%)</b></td><td>318.00 <b>(-44.92%)</b></td><td>200.50 (-9.68%)</td><td>117.71 <b>(-62.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>932.50 (n/a)</td><td>595.40 (n/a)</td><td>577.30 (n/a)</td><td>222.00 (n/a)</td><td>317.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (+2.45%)</td><td>0.03 <b>(+29.09%)</b></td><td>0.03 <b>(+45.16%)</b></td><td>0.02 <b>(+81.77%)</b></td><td>0.00 <b>(-44.82%)</b></td><td>362.10 <b>(-44.99%)</b></td><td>282.06 <b>(-29.81%)</b></td><td>272.30 <b>(-31.12%)</b></td><td>230.50 (-2.41%)</td><td>49.19 <b>(-69.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.20 (n/a)</td><td>401.84 (n/a)</td><td>395.30 (n/a)</td><td>236.20 (n/a)</td><td>162.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-17.73%)</td><td>0.02 (+4.20%)</td><td>0.02 (+1.88%)</td><td>0.01 (+1.23%)</td><td>0.01 <b>(-22.23%)</b></td><td>567.80 (-1.22%)</td><td>432.10 (-7.08%)</td><td>521.90 (-1.82%)</td><td>238.80 <b>(+21.59%)</b></td><td>155.42 (+1.18%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.80 (n/a)</td><td>465.02 (n/a)</td><td>531.60 (n/a)</td><td>196.40 (n/a)</td><td>153.61 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-7.62%)</td><td>0.02 (-12.38%)</td><td>0.03 (-0.62%)</td><td>0.01 <b>(-31.31%)</b></td><td>0.01 <b>(+75.92%)</b></td><td>592.90 <b>(+45.57%)</b></td><td>408.06 <b>(+22.58%)</b></td><td>307.50 (+0.62%)</td><td>301.20 (+8.27%)</td><td>144.36 <b>(+166.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>407.30 (n/a)</td><td>332.88 (n/a)</td><td>305.60 (n/a)</td><td>278.20 (n/a)</td><td>54.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-4.37%)</td><td>0.02 (+11.25%)</td><td>0.02 (+11.87%)</td><td>0.01 (-7.86%)</td><td>0.01 (+8.42%)</td><td>659.30 (+8.53%)</td><td>462.46 (-8.07%)</td><td>498.10 (-10.61%)</td><td>290.70 (+4.57%)</td><td>161.38 (+17.94%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.50 (n/a)</td><td>503.04 (n/a)</td><td>557.20 (n/a)</td><td>278.00 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-4.55%)</td><td>0.02 (-14.86%)</td><td>0.02 <b>(-36.04%)</b></td><td>0.01 <b>(-20.70%)</b></td><td>0.01 (-4.41%)</td><td>693.50 <b>(+26.09%)</b></td><td>436.72 (+19.08%)</td><td>475.40 <b>(+56.33%)</b></td><td>243.60 (+4.77%)</td><td>178.30 <b>(+20.50%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>366.76 (n/a)</td><td>304.10 (n/a)</td><td>232.50 (n/a)</td><td>147.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-0.31%)</td><td>0.02 (+7.93%)</td><td>0.02 <b>(+22.74%)</b></td><td>0.01 (-6.46%)</td><td>0.00 <b>(+23.42%)</b></td><td>582.80 (+6.90%)</td><td>437.96 (-5.50%)</td><td>392.30 (-18.54%)</td><td>334.70 (+0.33%)</td><td>112.87 <b>(+33.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>545.20 (n/a)</td><td>463.46 (n/a)</td><td>481.60 (n/a)</td><td>333.60 (n/a)</td><td>84.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+18.22%)</td><td>0.02 <b>(+25.92%)</b></td><td>0.02 <b>(+30.70%)</b></td><td>0.01 (+3.46%)</td><td>0.01 <b>(+39.48%)</b></td><td>655.80 (-3.35%)</td><td>402.90 (-16.91%)</td><td>363.40 <b>(-23.48%)</b></td><td>247.80 (-15.43%)</td><td>164.48 (+16.74%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.50 (n/a)</td><td>484.90 (n/a)</td><td>474.90 (n/a)</td><td>293.00 (n/a)</td><td>140.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (-12.57%)</td><td>0.04 (-13.51%)</td><td>0.05 <b>(-20.06%)</b></td><td>0.03 (-12.26%)</td><td>0.01 (-4.31%)</td><td>547.90 (+13.98%)</td><td>398.08 (+17.04%)</td><td>356.30 <b>(+25.11%)</b></td><td>279.40 (+14.37%)</td><td>128.17 <b>(+23.64%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.70 (n/a)</td><td>340.12 (n/a)</td><td>284.80 (n/a)</td><td>244.30 (n/a)</td><td>103.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (+6.17%)</td><td>0.05 (+16.10%)</td><td>0.05 <b>(+56.44%)</b></td><td>0.03 (-4.11%)</td><td>0.01 (+19.09%)</td><td>544.80 (+4.29%)</td><td>378.04 (-12.15%)</td><td>316.30 <b>(-36.09%)</b></td><td>271.80 (-5.82%)</td><td>122.10 (+14.42%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>522.40 (n/a)</td><td>430.30 (n/a)</td><td>494.90 (n/a)</td><td>288.60 (n/a)</td><td>106.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 <b>(-28.31%)</b></td><td>0.04 <b>(-28.66%)</b></td><td>0.04 <b>(-34.93%)</b></td><td>0.03 (-9.49%)</td><td>0.01 <b>(-44.04%)</b></td><td>509.70 (+10.49%)</td><td>418.82 <b>(+33.36%)</b></td><td>467.90 <b>(+53.71%)</b></td><td>280.10 <b>(+39.49%)</b></td><td>102.57 (-9.12%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>461.30 (n/a)</td><td>314.06 (n/a)</td><td>304.40 (n/a)</td><td>200.80 (n/a)</td><td>112.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (-11.87%)</td><td>0.05 (-19.94%)</td><td>0.04 <b>(-37.13%)</b></td><td>0.02 <b>(-29.88%)</b></td><td>0.02 (+8.58%)</td><td>660.50 <b>(+42.63%)</b></td><td>406.78 <b>(+33.52%)</b></td><td>427.20 <b>(+59.05%)</b></td><td>214.80 (+13.47%)</td><td>174.87 <b>(+68.39%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>463.10 (n/a)</td><td>304.66 (n/a)</td><td>268.60 (n/a)</td><td>189.30 (n/a)</td><td>103.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (-11.09%)</td><td>0.04 <b>(-25.24%)</b></td><td>0.03 <b>(-46.82%)</b></td><td>0.03 (+0.35%)</td><td>0.01 <b>(-35.97%)</b></td><td>511.40 (-0.35%)</td><td>448.42 <b>(+26.58%)</b></td><td>493.90 <b>(+88.01%)</b></td><td>285.50 (+12.45%)</td><td>93.28 <b>(-29.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.20 (n/a)</td><td>354.26 (n/a)</td><td>262.70 (n/a)</td><td>253.90 (n/a)</td><td>132.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (-5.56%)</td><td>0.05 (+9.95%)</td><td>0.04 (-0.91%)</td><td>0.03 <b>(+236.32%)</b></td><td>0.02 <b>(-40.21%)</b></td><td>553.10 <b>(-70.27%)</b></td><td>393.84 <b>(-42.62%)</b></td><td>413.10 (+0.93%)</td><td>250.00 (+5.89%)</td><td>126.81 <b>(-81.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1860.30 (n/a)</td><td>686.40 (n/a)</td><td>409.30 (n/a)</td><td>236.10 (n/a)</td><td>678.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (-13.50%)</td><td>0.04 <b>(-29.79%)</b></td><td>0.03 <b>(-46.84%)</b></td><td>0.01 <b>(-75.35%)</b></td><td>0.02 <b>(+38.38%)</b></td><td>1892.20 <b>(+305.70%)</b></td><td>727.06 <b>(+112.37%)</b></td><td>559.50 <b>(+88.13%)</b></td><td>259.60 (+15.63%)</td><td>670.45 <b>(+516.70%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>466.40 (n/a)</td><td>342.36 (n/a)</td><td>297.40 (n/a)</td><td>224.50 (n/a)</td><td>108.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (+3.46%)</td><td>0.04 (+5.95%)</td><td>0.04 (-6.78%)</td><td>0.03 (+10.44%)</td><td>0.01 (+17.19%)</td><td>584.80 (-9.45%)</td><td>417.70 (-5.11%)</td><td>436.60 (+7.27%)</td><td>308.10 (-3.33%)</td><td>115.30 (-6.88%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>645.80 (n/a)</td><td>440.18 (n/a)</td><td>407.00 (n/a)</td><td>318.70 (n/a)</td><td>123.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (+19.43%)</td><td>0.05 (+19.66%)</td><td>0.04 (+5.46%)</td><td>0.03 <b>(+67.99%)</b></td><td>0.02 <b>(+24.50%)</b></td><td>598.50 <b>(-40.47%)</b></td><td>417.08 (-19.80%)</td><td>437.40 (-5.18%)</td><td>243.00 (-16.26%)</td><td>163.44 <b>(-42.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1005.40 (n/a)</td><td>520.04 (n/a)</td><td>461.30 (n/a)</td><td>290.20 (n/a)</td><td>284.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 <b>(-41.44%)</b></td><td>0.04 (-15.16%)</td><td>0.04 (-11.56%)</td><td>0.03 (+12.65%)</td><td>0.01 <b>(-72.06%)</b></td><td>551.00 (-11.23%)</td><td>421.94 (+2.75%)</td><td>388.50 (+13.07%)</td><td>384.30 <b>(+70.80%)</b></td><td>72.40 <b>(-59.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.70 (n/a)</td><td>410.66 (n/a)</td><td>343.60 (n/a)</td><td>225.00 (n/a)</td><td>180.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (+2.40%)</td><td>0.04 (+2.67%)</td><td>0.04 <b>(+25.75%)</b></td><td>0.03 (+1.59%)</td><td>0.01 (-14.29%)</td><td>558.10 (-1.57%)</td><td>419.68 (-5.14%)</td><td>412.80 <b>(-20.48%)</b></td><td>274.00 (-2.32%)</td><td>112.79 (-17.30%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.00 (n/a)</td><td>442.42 (n/a)</td><td>519.10 (n/a)</td><td>280.50 (n/a)</td><td>136.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (+5.63%)</td><td>0.03 <b>(-30.78%)</b></td><td>0.03 <b>(-42.40%)</b></td><td>0.01 <b>(-72.91%)</b></td><td>0.02 <b>(+63.68%)</b></td><td>2009.40 <b>(+269.17%)</b></td><td>773.98 <b>(+108.71%)</b></td><td>549.60 <b>(+73.59%)</b></td><td>269.30 (-5.34%)</td><td>700.53 <b>(+545.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>544.30 (n/a)</td><td>370.84 (n/a)</td><td>316.60 (n/a)</td><td>284.50 (n/a)</td><td>108.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 <b>(+27.26%)</b></td><td>0.09 (+4.63%)</td><td>0.07 <b>(-41.63%)</b></td><td>0.06 <b>(+242.87%)</b></td><td>0.04 (-7.10%)</td><td>548.30 <b>(-70.83%)</b></td><td>400.92 <b>(-37.18%)</b></td><td>474.40 <b>(+71.33%)</b></td><td>195.40 <b>(-21.43%)</b></td><td>144.51 <b>(-79.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1879.80 (n/a)</td><td>638.24 (n/a)</td><td>276.90 (n/a)</td><td>248.70 (n/a)</td><td>701.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (-8.45%)</td><td>0.11 (+6.78%)</td><td>0.11 (+6.49%)</td><td>0.10 <b>(+64.89%)</b></td><td>0.01 <b>(-74.08%)</b></td><td>315.70 <b>(-39.36%)</b></td><td>295.88 (-12.29%)</td><td>297.50 (-6.09%)</td><td>267.40 (+9.23%)</td><td>18.12 <b>(-83.40%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>520.60 (n/a)</td><td>337.32 (n/a)</td><td>316.80 (n/a)</td><td>244.80 (n/a)</td><td>109.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (-11.69%)</td><td>0.09 (-3.07%)</td><td>0.11 (+16.44%)</td><td>0.04 <b>(-31.80%)</b></td><td>0.03 (+7.31%)</td><td>759.10 <b>(+46.63%)</b></td><td>410.60 (+9.88%)</td><td>312.00 (-14.10%)</td><td>280.90 (+13.22%)</td><td>199.70 <b>(+84.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.70 (n/a)</td><td>373.68 (n/a)</td><td>363.20 (n/a)</td><td>248.10 (n/a)</td><td>107.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (-11.04%)</td><td>0.10 (+6.28%)</td><td>0.11 <b>(+50.58%)</b></td><td>0.05 <b>(-23.43%)</b></td><td>0.03 (-17.46%)</td><td>631.10 <b>(+30.61%)</b></td><td>360.34 (-5.47%)</td><td>297.80 <b>(-33.59%)</b></td><td>278.10 (+12.41%)</td><td>151.63 <b>(+27.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>483.20 (n/a)</td><td>381.18 (n/a)</td><td>448.40 (n/a)</td><td>247.40 (n/a)</td><td>118.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (+17.64%)</td><td>0.10 (-2.43%)</td><td>0.07 <b>(-34.78%)</b></td><td>0.05 (-1.61%)</td><td>0.05 <b>(+20.30%)</b></td><td>614.40 (+1.64%)</td><td>405.20 (+5.30%)</td><td>467.00 <b>(+53.32%)</b></td><td>201.40 (-14.99%)</td><td>172.61 (+1.01%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>604.50 (n/a)</td><td>384.82 (n/a)</td><td>304.60 (n/a)</td><td>236.90 (n/a)</td><td>170.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+3.15%)</td><td>0.10 (+2.01%)</td><td>0.11 (-2.83%)</td><td>0.07 (+13.82%)</td><td>0.03 <b>(-21.07%)</b></td><td>486.60 (-12.15%)</td><td>348.94 (-7.64%)</td><td>306.20 (+2.92%)</td><td>234.60 (-3.06%)</td><td>101.08 <b>(-34.26%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>553.90 (n/a)</td><td>377.80 (n/a)</td><td>297.50 (n/a)</td><td>242.00 (n/a)</td><td>153.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+4.44%)</td><td>0.08 (+3.00%)</td><td>0.07 (-3.19%)</td><td>0.05 <b>(+172.69%)</b></td><td>0.03 <b>(-25.14%)</b></td><td>691.90 <b>(-63.33%)</b></td><td>463.08 <b>(-33.57%)</b></td><td>472.30 (+3.30%)</td><td>239.10 (-4.25%)</td><td>160.95 <b>(-76.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1886.70 (n/a)</td><td>697.12 (n/a)</td><td>457.20 (n/a)</td><td>249.70 (n/a)</td><td>679.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 <b>(+30.61%)</b></td><td>0.08 (-7.13%)</td><td>0.06 (-17.96%)</td><td>0.05 (-7.10%)</td><td>0.04 <b>(+61.52%)</b></td><td>611.40 (+7.64%)</td><td>470.16 (+14.31%)</td><td>521.40 <b>(+21.88%)</b></td><td>229.20 <b>(-23.42%)</b></td><td>144.38 <b>(+29.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>568.00 (n/a)</td><td>411.32 (n/a)</td><td>427.80 (n/a)</td><td>299.30 (n/a)</td><td>111.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (+8.82%)</td><td>0.08 (+3.52%)</td><td>0.07 (+15.56%)</td><td>0.06 (+16.28%)</td><td>0.02 (-16.53%)</td><td>543.60 (-14.00%)</td><td>450.24 (-6.62%)</td><td>457.40 (-13.47%)</td><td>299.80 (-8.09%)</td><td>102.08 <b>(-30.05%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>632.10 (n/a)</td><td>482.16 (n/a)</td><td>528.60 (n/a)</td><td>326.20 (n/a)</td><td>145.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (-4.77%)</td><td>0.08 (-1.25%)</td><td>0.06 (-12.54%)</td><td>0.06 (+7.97%)</td><td>0.03 (-8.89%)</td><td>573.40 (-7.40%)</td><td>444.78 (-1.16%)</td><td>531.00 (+14.34%)</td><td>265.30 (+5.03%)</td><td>147.88 (-12.99%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>619.20 (n/a)</td><td>450.02 (n/a)</td><td>464.40 (n/a)</td><td>252.60 (n/a)</td><td>169.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+0.53%)</td><td>0.09 (-5.24%)</td><td>0.06 <b>(-27.11%)</b></td><td>0.06 (-3.02%)</td><td>0.04 (+16.89%)</td><td>579.50 (+3.13%)</td><td>433.18 (+9.33%)</td><td>520.00 <b>(+37.20%)</b></td><td>240.70 (-0.50%)</td><td>150.65 <b>(+20.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.90 (n/a)</td><td>396.22 (n/a)</td><td>379.00 (n/a)</td><td>241.90 (n/a)</td><td>124.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (+4.92%)</td><td>0.07 (-10.99%)</td><td>0.07 (-19.32%)</td><td>0.02 <b>(-68.80%)</b></td><td>0.04 <b>(+52.35%)</b></td><td>1872.70 <b>(+220.50%)</b></td><td>714.18 <b>(+64.39%)</b></td><td>498.50 <b>(+23.94%)</b></td><td>249.40 (-4.70%)</td><td>664.85 <b>(+358.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.30 (n/a)</td><td>434.44 (n/a)</td><td>402.20 (n/a)</td><td>261.70 (n/a)</td><td>144.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (-7.35%)</td><td>0.08 <b>(+31.47%)</b></td><td>0.08 <b>(+84.49%)</b></td><td>0.05 (+18.10%)</td><td>0.02 <b>(-33.15%)</b></td><td>461.50 (-15.34%)</td><td>322.98 <b>(-30.28%)</b></td><td>291.30 <b>(-45.79%)</b></td><td>216.10 (+7.89%)</td><td>93.82 <b>(-36.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>545.10 (n/a)</td><td>463.26 (n/a)</td><td>537.40 (n/a)</td><td>200.30 (n/a)</td><td>148.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (-17.83%)</td><td>0.17 <b>(+37.58%)</b></td><td>0.17 <b>(+75.83%)</b></td><td>0.13 <b>(+419.32%)</b></td><td>0.02 <b>(-71.76%)</b></td><td>369.90 <b>(-80.75%)</b></td><td>292.60 <b>(-58.23%)</b></td><td>286.90 <b>(-43.12%)</b></td><td>251.10 <b>(+21.72%)</b></td><td>45.77 <b>(-93.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1921.10 (n/a)</td><td>700.48 (n/a)</td><td>504.40 (n/a)</td><td>206.30 (n/a)</td><td>700.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.29 (+16.01%)</td><td>3.29 (+3.94%)</td><td>3.00 (-5.54%)</td><td>2.71 (+6.19%)</td><td>0.65 <b>(+30.86%)</b></td><td>3870.20 (-5.83%)</td><td>3280.88 (-3.00%)</td><td>3494.70 (+5.87%)</td><td>2443.20 (-13.80%)</td><td>589.36 (+7.30%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.70 (n/a)</td><td>3.16 (n/a)</td><td>3.18 (n/a)</td><td>2.55 (n/a)</td><td>0.50 (n/a)</td><td>4109.80 (n/a)</td><td>3382.48 (n/a)</td><td>3301.00 (n/a)</td><td>2834.20 (n/a)</td><td>549.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (-13.76%)</td><td>0.12 <b>(+28.58%)</b></td><td>0.10 <b>(+36.68%)</b></td><td>0.08 <b>(+280.12%)</b></td><td>0.04 <b>(-40.76%)</b></td><td>500.90 <b>(-73.69%)</b></td><td>383.60 <b>(-49.49%)</b></td><td>407.40 <b>(-26.83%)</b></td><td>242.00 (+15.96%)</td><td>118.57 <b>(-82.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1904.20 (n/a)</td><td>759.50 (n/a)</td><td>556.80 (n/a)</td><td>208.70 (n/a)</td><td>669.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(-25.44%)</b></td><td>0.01 (-12.31%)</td><td>0.01 (-10.15%)</td><td>0.01 (-7.11%)</td><td>0.00 <b>(-46.32%)</b></td><td>520.80 (+7.65%)</td><td>388.28 (+7.60%)</td><td>373.90 (+11.31%)</td><td>278.60 <b>(+34.14%)</b></td><td>87.93 <b>(-26.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>483.80 (n/a)</td><td>360.84 (n/a)</td><td>335.90 (n/a)</td><td>207.70 (n/a)</td><td>118.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-16.75%)</td><td>0.01 (-15.96%)</td><td>0.01 (-14.36%)</td><td>0.01 (+2.21%)</td><td>0.00 (-18.21%)</td><td>493.10 (-2.16%)</td><td>357.48 (+16.87%)</td><td>296.80 (+16.76%)</td><td>249.80 <b>(+20.15%)</b></td><td>111.96 (-4.57%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.00 (n/a)</td><td>305.88 (n/a)</td><td>254.20 (n/a)</td><td>207.90 (n/a)</td><td>117.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(+61.38%)</b></td><td>0.02 <b>(+48.79%)</b></td><td>0.02 <b>(+32.27%)</b></td><td>0.01 <b>(+70.22%)</b></td><td>0.01 <b>(+60.04%)</b></td><td>619.90 <b>(-41.25%)</b></td><td>387.96 <b>(-33.79%)</b></td><td>354.80 <b>(-24.40%)</b></td><td>236.40 <b>(-38.05%)</b></td><td>148.81 <b>(-44.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1055.20 (n/a)</td><td>585.96 (n/a)</td><td>469.30 (n/a)</td><td>381.60 (n/a)</td><td>270.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+17.72%)</td><td>0.01 (+13.88%)</td><td>0.02 <b>(+46.13%)</b></td><td>0.01 (+1.36%)</td><td>0.01 <b>(+37.92%)</b></td><td>555.70 (-1.35%)</td><td>365.92 (-6.02%)</td><td>266.40 <b>(-31.57%)</b></td><td>217.80 (-15.02%)</td><td>168.27 <b>(+28.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.30 (n/a)</td><td>389.38 (n/a)</td><td>389.30 (n/a)</td><td>256.30 (n/a)</td><td>130.61 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-4.97%)</td><td>0.01 <b>(-22.60%)</b></td><td>0.01 <b>(-45.52%)</b></td><td>0.01 (-11.91%)</td><td>0.01 (+18.54%)</td><td>584.70 (+13.53%)</td><td>428.56 <b>(+35.72%)</b></td><td>507.80 <b>(+83.52%)</b></td><td>249.10 (+5.19%)</td><td>158.00 <b>(+36.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.00 (n/a)</td><td>315.76 (n/a)</td><td>276.70 (n/a)</td><td>236.80 (n/a)</td><td>115.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-3.29%)</td><td>0.01 (-6.79%)</td><td>0.02 (+11.21%)</td><td>0.00 <b>(-73.32%)</b></td><td>0.01 <b>(+61.09%)</b></td><td>1833.80 <b>(+274.78%)</b></td><td>566.22 <b>(+86.58%)</b></td><td>253.10 (-10.09%)</td><td>232.20 (+3.38%)</td><td>708.68 <b>(+554.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.30 (n/a)</td><td>303.48 (n/a)</td><td>281.50 (n/a)</td><td>224.60 (n/a)</td><td>108.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 <b>(+48.83%)</b></td><td>0.01 (+3.56%)</td><td>0.01 (-7.78%)</td><td>0.01 (-19.03%)</td><td>0.01 <b>(+122.48%)</b></td><td>770.40 <b>(+23.50%)</b></td><td>526.48 (+11.52%)</td><td>552.50 (+8.44%)</td><td>203.30 <b>(-32.82%)</b></td><td>204.58 <b>(+69.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.80 (n/a)</td><td>472.08 (n/a)</td><td>509.50 (n/a)</td><td>302.60 (n/a)</td><td>120.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+36.75%)</b></td><td>0.01 <b>(+35.63%)</b></td><td>0.01 (+4.79%)</td><td>0.01 <b>(+235.45%)</b></td><td>0.00 (-8.02%)</td><td>543.00 <b>(-70.19%)</b></td><td>394.68 <b>(-44.27%)</b></td><td>417.00 (-4.58%)</td><td>262.70 <b>(-26.87%)</b></td><td>109.62 <b>(-82.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1821.60 (n/a)</td><td>708.22 (n/a)</td><td>437.00 (n/a)</td><td>359.20 (n/a)</td><td>624.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+28.34%)</b></td><td>0.01 (+9.23%)</td><td>0.01 (+15.31%)</td><td>0.01 (-3.92%)</td><td>0.00 <b>(+63.60%)</b></td><td>553.80 (+4.10%)</td><td>395.54 (-4.37%)</td><td>377.70 (-13.29%)</td><td>230.80 <b>(-22.08%)</b></td><td>120.35 <b>(+31.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.00 (n/a)</td><td>413.60 (n/a)</td><td>435.60 (n/a)</td><td>296.20 (n/a)</td><td>91.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-2.95%)</td><td>0.01 (-4.16%)</td><td>0.01 (+16.90%)</td><td>0.01 <b>(-23.30%)</b></td><td>0.00 (-14.29%)</td><td>764.10 <b>(+30.37%)</b></td><td>457.68 (+4.35%)</td><td>440.00 (-14.45%)</td><td>279.10 (+3.06%)</td><td>186.79 <b>(+22.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.10 (n/a)</td><td>438.62 (n/a)</td><td>514.30 (n/a)</td><td>270.80 (n/a)</td><td>152.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 <b>(-31.85%)</b></td><td>0.01 <b>(-31.06%)</b></td><td>0.01 <b>(-20.59%)</b></td><td>0.00 <b>(-41.84%)</b></td><td>0.00 <b>(-29.30%)</b></td><td>1152.30 <b>(+71.96%)</b></td><td>623.60 <b>(+50.07%)</b></td><td>482.70 <b>(+25.93%)</b></td><td>409.20 <b>(+46.72%)</b></td><td>304.50 <b>(+91.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>670.10 (n/a)</td><td>415.54 (n/a)</td><td>383.30 (n/a)</td><td>278.90 (n/a)</td><td>158.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+20.39%)</b></td><td>0.01 (+17.76%)</td><td>0.01 <b>(+40.34%)</b></td><td>0.01 <b>(+57.80%)</b></td><td>0.00 (+10.47%)</td><td>663.50 <b>(-36.63%)</b></td><td>444.74 (-19.13%)</td><td>342.70 <b>(-28.74%)</b></td><td>257.10 (-16.96%)</td><td>184.80 <b>(-37.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1047.10 (n/a)</td><td>549.94 (n/a)</td><td>480.90 (n/a)</td><td>309.60 (n/a)</td><td>297.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 <b>(+20.11%)</b></td><td>0.03 (+5.54%)</td><td>0.03 (+18.02%)</td><td>0.01 <b>(-27.21%)</b></td><td>0.01 <b>(+111.25%)</b></td><td>635.20 <b>(+37.40%)</b></td><td>383.32 (+8.39%)</td><td>264.40 (-15.26%)</td><td>233.20 (-16.74%)</td><td>186.13 <b>(+138.27%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>462.30 (n/a)</td><td>353.66 (n/a)</td><td>312.00 (n/a)</td><td>280.10 (n/a)</td><td>78.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (-5.15%)</td><td>0.04 (+4.21%)</td><td>0.04 (-1.70%)</td><td>0.04 <b>(+52.97%)</b></td><td>0.00 <b>(-74.61%)</b></td><td>305.00 <b>(-34.63%)</b></td><td>280.36 (-8.69%)</td><td>278.40 (+1.72%)</td><td>263.00 (+5.41%)</td><td>15.28 <b>(-83.05%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>466.60 (n/a)</td><td>307.04 (n/a)</td><td>273.70 (n/a)</td><td>249.50 (n/a)</td><td>90.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (-2.71%)</td><td>0.02 <b>(-40.57%)</b></td><td>0.01 <b>(-52.31%)</b></td><td>0.01 <b>(-51.42%)</b></td><td>0.01 <b>(+161.74%)</b></td><td>635.80 <b>(+105.83%)</b></td><td>503.32 <b>(+90.77%)</b></td><td>555.10 <b>(+109.71%)</b></td><td>230.90 (+2.80%)</td><td>159.96 <b>(+419.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>308.90 (n/a)</td><td>263.84 (n/a)</td><td>264.70 (n/a)</td><td>224.60 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (+15.48%)</td><td>0.03 <b>(+21.24%)</b></td><td>0.04 <b>(+64.32%)</b></td><td>0.02 <b>(+28.07%)</b></td><td>0.01 (+2.08%)</td><td>546.80 <b>(-21.92%)</b></td><td>374.06 (-19.86%)</td><td>286.90 <b>(-39.15%)</b></td><td>233.50 (-13.39%)</td><td>147.32 <b>(-23.01%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>700.30 (n/a)</td><td>466.78 (n/a)</td><td>471.50 (n/a)</td><td>269.60 (n/a)</td><td>191.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (-19.15%)</td><td>0.02 (-13.23%)</td><td>0.02 (-14.68%)</td><td>0.01 (-7.80%)</td><td>0.01 <b>(-24.97%)</b></td><td>551.70 (+8.47%)</td><td>402.66 (+11.97%)</td><td>424.30 (+17.18%)</td><td>222.50 <b>(+23.68%)</b></td><td>129.70 (+1.09%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>359.60 (n/a)</td><td>362.10 (n/a)</td><td>179.90 (n/a)</td><td>128.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 <b>(+26.50%)</b></td><td>0.03 (+16.05%)</td><td>0.04 <b>(+51.36%)</b></td><td>0.02 (-6.46%)</td><td>0.01 <b>(+36.91%)</b></td><td>611.60 (+6.90%)</td><td>381.32 (-7.55%)</td><td>276.00 <b>(-33.94%)</b></td><td>200.50 <b>(-20.94%)</b></td><td>184.80 <b>(+24.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.10 (n/a)</td><td>412.46 (n/a)</td><td>417.80 (n/a)</td><td>253.60 (n/a)</td><td>148.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 <b>(-22.08%)</b></td><td>0.02 <b>(-32.48%)</b></td><td>0.02 (-13.69%)</td><td>0.00 <b>(-81.03%)</b></td><td>0.01 (-1.19%)</td><td>2431.90 <b>(+427.18%)</b></td><td>839.58 <b>(+134.04%)</b></td><td>484.90 (+15.87%)</td><td>232.30 <b>(+28.34%)</b></td><td>899.93 <b>(+647.05%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.30 (n/a)</td><td>358.74 (n/a)</td><td>418.50 (n/a)</td><td>181.00 (n/a)</td><td>120.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-17.94%)</td><td>0.02 <b>(-28.32%)</b></td><td>0.02 <b>(-33.21%)</b></td><td>0.02 <b>(-25.35%)</b></td><td>0.00 (-5.20%)</td><td>585.10 <b>(+33.95%)</b></td><td>486.94 <b>(+40.63%)</b></td><td>497.10 <b>(+49.73%)</b></td><td>361.90 <b>(+21.85%)</b></td><td>84.54 <b>(+50.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>436.80 (n/a)</td><td>346.26 (n/a)</td><td>332.00 (n/a)</td><td>297.00 (n/a)</td><td>55.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-7.77%)</td><td>0.02 (-11.57%)</td><td>0.02 (-5.31%)</td><td>0.00 <b>(-69.25%)</b></td><td>0.01 (+14.27%)</td><td>1971.60 <b>(+225.19%)</b></td><td>744.76 <b>(+56.29%)</b></td><td>500.60 (+5.61%)</td><td>262.40 (+8.43%)</td><td>693.77 <b>(+365.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.30 (n/a)</td><td>476.52 (n/a)</td><td>474.00 (n/a)</td><td>242.00 (n/a)</td><td>148.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (-16.51%)</td><td>0.02 (-10.47%)</td><td>0.02 (-4.38%)</td><td>0.02 <b>(-21.78%)</b></td><td>0.01 (-4.42%)</td><td>567.10 <b>(+27.84%)</b></td><td>432.76 (+13.91%)</td><td>438.20 (+4.58%)</td><td>294.00 (+19.76%)</td><td>121.69 <b>(+49.46%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.60 (n/a)</td><td>379.90 (n/a)</td><td>419.00 (n/a)</td><td>245.50 (n/a)</td><td>81.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (+10.56%)</td><td>0.02 (+7.41%)</td><td>0.02 (+7.12%)</td><td>0.01 (+16.50%)</td><td>0.01 (+12.01%)</td><td>560.70 (-14.16%)</td><td>468.88 (-6.91%)</td><td>514.20 (-6.64%)</td><td>262.10 (-9.56%)</td><td>120.15 (-12.23%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.20 (n/a)</td><td>503.66 (n/a)</td><td>550.80 (n/a)</td><td>289.80 (n/a)</td><td>136.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 <b>(-27.80%)</b></td><td>0.04 <b>(-27.73%)</b></td><td>0.04 <b>(-37.09%)</b></td><td>0.03 (-10.82%)</td><td>0.01 <b>(-45.91%)</b></td><td>524.00 (+12.13%)</td><td>429.84 <b>(+33.51%)</b></td><td>442.50 <b>(+58.94%)</b></td><td>322.20 <b>(+38.52%)</b></td><td>81.03 (-16.88%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>467.30 (n/a)</td><td>321.96 (n/a)</td><td>278.40 (n/a)</td><td>232.60 (n/a)</td><td>97.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 <b>(-30.55%)</b></td><td>0.06 <b>(-21.35%)</b></td><td>0.05 <b>(-30.48%)</b></td><td>0.04 (-14.37%)</td><td>0.02 <b>(-28.73%)</b></td><td>693.00 (+16.76%)</td><td>477.62 <b>(+23.29%)</b></td><td>543.90 <b>(+43.85%)</b></td><td>283.70 <b>(+44.01%)</b></td><td>183.40 (+9.86%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>593.50 (n/a)</td><td>387.38 (n/a)</td><td>378.10 (n/a)</td><td>197.00 (n/a)</td><td>166.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (+18.29%)</td><td>0.04 (-1.92%)</td><td>0.04 (-11.43%)</td><td>0.02 <b>(-24.81%)</b></td><td>0.02 <b>(+47.17%)</b></td><td>691.50 <b>(+32.98%)</b></td><td>442.24 (+12.40%)</td><td>453.00 (+12.91%)</td><td>217.40 (-15.44%)</td><td>195.03 <b>(+61.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>520.00 (n/a)</td><td>393.44 (n/a)</td><td>401.20 (n/a)</td><td>257.10 (n/a)</td><td>120.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (-15.88%)</td><td>0.05 (-11.72%)</td><td>0.04 (+3.13%)</td><td>0.03 (-13.84%)</td><td>0.02 <b>(-20.91%)</b></td><td>651.10 (+16.06%)</td><td>468.94 (+11.38%)</td><td>483.90 (-3.03%)</td><td>279.00 (+18.88%)</td><td>156.52 (+8.16%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.00 (n/a)</td><td>421.04 (n/a)</td><td>499.00 (n/a)</td><td>234.70 (n/a)</td><td>144.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (+5.69%)</td><td>0.06 <b>(+21.10%)</b></td><td>0.06 <b>(+41.86%)</b></td><td>0.04 <b>(+37.57%)</b></td><td>0.01 <b>(-34.65%)</b></td><td>405.00 <b>(-27.32%)</b></td><td>299.84 <b>(-23.65%)</b></td><td>296.30 <b>(-29.50%)</b></td><td>223.00 (-5.35%)</td><td>66.22 <b>(-52.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.20 (n/a)</td><td>392.74 (n/a)</td><td>420.30 (n/a)</td><td>235.60 (n/a)</td><td>140.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (+6.38%)</td><td>0.05 (-2.97%)</td><td>0.04 (-8.09%)</td><td>0.03 (-12.28%)</td><td>0.02 <b>(+25.24%)</b></td><td>604.20 (+14.00%)</td><td>433.44 (+8.97%)</td><td>465.20 (+8.82%)</td><td>229.00 (-5.99%)</td><td>165.21 <b>(+36.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>530.00 (n/a)</td><td>397.76 (n/a)</td><td>427.50 (n/a)</td><td>243.60 (n/a)</td><td>120.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 <b>(-22.98%)</b></td><td>0.05 (-9.03%)</td><td>0.06 (-7.91%)</td><td>0.03 <b>(+23.69%)</b></td><td>0.01 <b>(-39.27%)</b></td><td>478.60 (-19.14%)</td><td>355.90 (-0.31%)</td><td>295.50 (+8.60%)</td><td>241.10 <b>(+29.83%)</b></td><td>110.06 <b>(-34.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.90 (n/a)</td><td>357.00 (n/a)</td><td>272.10 (n/a)</td><td>185.70 (n/a)</td><td>167.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 <b>(+33.78%)</b></td><td>0.04 <b>(-24.98%)</b></td><td>0.03 <b>(-36.65%)</b></td><td>0.01 <b>(-75.75%)</b></td><td>0.02 <b>(+215.82%)</b></td><td>1862.40 <b>(+312.31%)</b></td><td>743.72 <b>(+99.69%)</b></td><td>541.60 <b>(+57.85%)</b></td><td>240.10 <b>(-25.25%)</b></td><td>638.62 <b>(+967.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>451.70 (n/a)</td><td>372.44 (n/a)</td><td>343.10 (n/a)</td><td>321.20 (n/a)</td><td>59.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (-0.26%)</td><td>0.04 (-2.29%)</td><td>0.03 <b>(-36.69%)</b></td><td>0.03 <b>(+322.31%)</b></td><td>0.02 <b>(-32.57%)</b></td><td>588.90 <b>(-76.32%)</b></td><td>425.20 <b>(-44.43%)</b></td><td>479.60 <b>(+57.97%)</b></td><td>244.80 (+0.25%)</td><td>146.79 <b>(-84.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2487.10 (n/a)</td><td>765.16 (n/a)</td><td>303.60 (n/a)</td><td>244.20 (n/a)</td><td>969.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 <b>(+65.01%)</b></td><td>0.05 <b>(+22.51%)</b></td><td>0.04 (-10.89%)</td><td>0.03 (-4.58%)</td><td>0.02 <b>(+263.38%)</b></td><td>626.90 (+4.80%)</td><td>435.60 (-5.53%)</td><td>479.20 (+12.22%)</td><td>232.00 <b>(-39.41%)</b></td><td>182.50 <b>(+120.24%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>461.08 (n/a)</td><td>427.00 (n/a)</td><td>382.90 (n/a)</td><td>82.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (+6.82%)</td><td>0.03 (-14.75%)</td><td>0.03 <b>(-22.95%)</b></td><td>0.03 (-10.98%)</td><td>0.01 <b>(+21.90%)</b></td><td>635.00 (+12.33%)</td><td>509.82 <b>(+20.38%)</b></td><td>555.80 <b>(+29.77%)</b></td><td>294.80 (-6.38%)</td><td>133.75 <b>(+27.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.30 (n/a)</td><td>423.52 (n/a)</td><td>428.30 (n/a)</td><td>314.90 (n/a)</td><td>104.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 <b>(+28.62%)</b></td><td>0.09 (-8.70%)</td><td>0.07 <b>(-36.21%)</b></td><td>0.07 <b>(+24.77%)</b></td><td>0.03 <b>(+32.70%)</b></td><td>479.20 (-19.85%)</td><td>398.36 (+10.17%)</td><td>459.50 <b>(+56.77%)</b></td><td>221.00 <b>(-22.27%)</b></td><td>109.65 (-18.44%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>597.90 (n/a)</td><td>361.58 (n/a)</td><td>293.10 (n/a)</td><td>284.30 (n/a)</td><td>134.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 <b>(+46.00%)</b></td><td>0.11 (-8.36%)</td><td>0.08 <b>(-38.57%)</b></td><td>0.07 <b>(+37.10%)</b></td><td>0.06 <b>(+52.08%)</b></td><td>492.10 <b>(-27.05%)</b></td><td>365.98 (+10.26%)</td><td>405.10 <b>(+62.76%)</b></td><td>155.10 <b>(-31.52%)</b></td><td>139.13 <b>(-27.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.60 (n/a)</td><td>331.92 (n/a)</td><td>248.90 (n/a)</td><td>226.50 (n/a)</td><td>192.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.29 <b>(+107.48%)</b></td><td>0.13 <b>(+54.67%)</b></td><td>0.11 <b>(+28.35%)</b></td><td>0.02 <b>(-28.31%)</b></td><td>0.10 <b>(+156.26%)</b></td><td>1900.30 <b>(+39.49%)</b></td><td>653.04 (+1.56%)</td><td>380.50 <b>(-22.08%)</b></td><td>142.00 <b>(-51.82%)</b></td><td>712.51 <b>(+71.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1362.30 (n/a)</td><td>643.00 (n/a)</td><td>488.30 (n/a)</td><td>294.70 (n/a)</td><td>416.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (+3.22%)</td><td>0.08 (-10.66%)</td><td>0.07 <b>(-39.21%)</b></td><td>0.06 (+4.86%)</td><td>0.03 (-11.86%)</td><td>542.00 (-4.64%)</td><td>433.26 (+8.46%)</td><td>496.70 <b>(+64.47%)</b></td><td>265.40 (-3.14%)</td><td>117.18 <b>(-21.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>568.40 (n/a)</td><td>399.48 (n/a)</td><td>302.00 (n/a)</td><td>274.00 (n/a)</td><td>148.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (+5.37%)</td><td>0.11 (+12.02%)</td><td>0.08 (-7.26%)</td><td>0.08 <b>(+45.76%)</b></td><td>0.04 (+7.30%)</td><td>512.20 <b>(-31.40%)</b></td><td>413.56 (-12.26%)</td><td>482.10 (+7.83%)</td><td>260.70 (-5.06%)</td><td>122.33 <b>(-28.50%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>746.60 (n/a)</td><td>471.36 (n/a)</td><td>447.10 (n/a)</td><td>274.60 (n/a)</td><td>171.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (+11.54%)</td><td>0.09 (-10.57%)</td><td>0.07 <b>(-35.91%)</b></td><td>0.05 <b>(-23.21%)</b></td><td>0.05 <b>(+40.68%)</b></td><td>687.20 <b>(+30.23%)</b></td><td>430.42 <b>(+23.05%)</b></td><td>489.30 <b>(+56.03%)</b></td><td>208.00 (-10.34%)</td><td>191.66 <b>(+58.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>527.70 (n/a)</td><td>349.78 (n/a)</td><td>313.60 (n/a)</td><td>232.00 (n/a)</td><td>120.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 <b>(+41.59%)</b></td><td>0.11 <b>(+21.87%)</b></td><td>0.07 (-7.14%)</td><td>0.06 (-12.70%)</td><td>0.06 <b>(+121.35%)</b></td><td>617.30 (+14.55%)</td><td>423.32 (-4.70%)</td><td>517.50 (+7.68%)</td><td>199.30 <b>(-29.38%)</b></td><td>188.17 <b>(+78.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>538.90 (n/a)</td><td>444.20 (n/a)</td><td>480.60 (n/a)</td><td>282.20 (n/a)</td><td>105.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (-0.80%)</td><td>0.10 (-9.37%)</td><td>0.07 <b>(-41.70%)</b></td><td>0.06 (+17.57%)</td><td>0.05 (+0.59%)</td><td>523.30 (-14.94%)</td><td>380.94 (+8.27%)</td><td>447.50 <b>(+71.52%)</b></td><td>201.70 (+0.80%)</td><td>150.50 (-14.21%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>615.20 (n/a)</td><td>351.84 (n/a)</td><td>260.90 (n/a)</td><td>200.10 (n/a)</td><td>175.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.23 (+0.43%)</td><td>0.11 (-12.16%)</td><td>0.08 <b>(-42.63%)</b></td><td>0.06 (-2.31%)</td><td>0.07 (+6.97%)</td><td>583.40 (+2.37%)</td><td>415.66 (+16.85%)</td><td>491.40 <b>(+74.26%)</b></td><td>161.90 (-0.43%)</td><td>180.68 (+4.96%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>569.90 (n/a)</td><td>355.72 (n/a)</td><td>282.00 (n/a)</td><td>162.60 (n/a)</td><td>172.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 <b>(-41.39%)</b></td><td>0.05 <b>(-48.41%)</b></td><td>0.06 <b>(-34.47%)</b></td><td>0.01 <b>(-73.82%)</b></td><td>0.03 (-7.64%)</td><td>2437.60 <b>(+281.95%)</b></td><td>1159.76 <b>(+191.48%)</b></td><td>595.60 <b>(+52.60%)</b></td><td>405.70 <b>(+70.61%)</b></td><td>943.72 <b>(+510.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>638.20 (n/a)</td><td>397.88 (n/a)</td><td>390.30 (n/a)</td><td>237.80 (n/a)</td><td>154.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (-5.01%)</td><td>0.07 (+1.94%)</td><td>0.07 (-8.26%)</td><td>0.04 (+18.60%)</td><td>0.02 <b>(-34.71%)</b></td><td>484.10 (-15.68%)</td><td>332.88 (-9.93%)</td><td>292.40 (+9.02%)</td><td>251.20 (+5.28%)</td><td>94.54 <b>(-41.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.10 (n/a)</td><td>369.56 (n/a)</td><td>268.20 (n/a)</td><td>238.60 (n/a)</td><td>161.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (+18.12%)</td><td>0.06 (+2.83%)</td><td>0.04 <b>(-32.87%)</b></td><td>0.04 (+14.04%)</td><td>0.02 <b>(+40.99%)</b></td><td>506.00 (-12.31%)</td><td>390.28 (+0.89%)</td><td>468.90 <b>(+48.95%)</b></td><td>235.80 (-15.33%)</td><td>135.23 (+4.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.00 (n/a)</td><td>386.84 (n/a)</td><td>314.80 (n/a)</td><td>278.50 (n/a)</td><td>129.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (-13.36%)</td><td>0.04 (-17.68%)</td><td>0.04 (-13.03%)</td><td>0.02 <b>(-30.88%)</b></td><td>0.03 (-7.26%)</td><td>1044.30 <b>(+44.68%)</b></td><td>610.60 <b>(+29.09%)</b></td><td>555.20 (+15.00%)</td><td>239.30 (+15.44%)</td><td>290.61 <b>(+59.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>721.80 (n/a)</td><td>473.00 (n/a)</td><td>482.80 (n/a)</td><td>207.30 (n/a)</td><td>182.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (-19.62%)</td><td>0.05 <b>(-21.88%)</b></td><td>0.04 <b>(-41.61%)</b></td><td>0.03 (-4.54%)</td><td>0.01 <b>(-40.00%)</b></td><td>603.80 (+4.75%)</td><td>446.64 <b>(+20.26%)</b></td><td>473.70 <b>(+71.26%)</b></td><td>313.30 <b>(+24.42%)</b></td><td>117.13 <b>(-22.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.40 (n/a)</td><td>371.40 (n/a)</td><td>276.60 (n/a)</td><td>251.80 (n/a)</td><td>150.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (-10.39%)</td><td>0.07 <b>(+33.55%)</b></td><td>0.08 <b>(+61.22%)</b></td><td>0.05 <b>(+60.39%)</b></td><td>0.02 <b>(-42.20%)</b></td><td>393.70 <b>(-37.65%)</b></td><td>285.84 <b>(-32.85%)</b></td><td>259.60 <b>(-37.97%)</b></td><td>217.00 (+11.63%)</td><td>69.78 <b>(-55.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>631.40 (n/a)</td><td>425.70 (n/a)</td><td>418.50 (n/a)</td><td>194.40 (n/a)</td><td>157.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (+16.24%)</td><td>0.07 (+16.51%)</td><td>0.08 (+17.98%)</td><td>0.04 (+10.16%)</td><td>0.02 <b>(+24.65%)</b></td><td>462.20 (-9.23%)</td><td>331.88 (-13.20%)</td><td>267.50 (-15.24%)</td><td>245.50 (-13.98%)</td><td>108.09 (-5.82%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>509.20 (n/a)</td><td>382.34 (n/a)</td><td>315.60 (n/a)</td><td>285.40 (n/a)</td><td>114.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 <b>(+23.59%)</b></td><td>0.08 (+15.63%)</td><td>0.06 (-3.07%)</td><td>0.05 (+12.89%)</td><td>0.03 <b>(+34.41%)</b></td><td>481.20 (-11.41%)</td><td>350.16 (-11.59%)</td><td>385.80 (+3.16%)</td><td>200.00 (-19.09%)</td><td>122.66 (-7.39%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>543.20 (n/a)</td><td>396.08 (n/a)</td><td>374.00 (n/a)</td><td>247.20 (n/a)</td><td>132.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (+7.91%)</td><td>0.06 (-15.18%)</td><td>0.06 (-7.47%)</td><td>0.02 <b>(-55.29%)</b></td><td>0.03 <b>(+54.39%)</b></td><td>1034.20 <b>(+123.66%)</b></td><td>514.54 <b>(+42.15%)</b></td><td>435.80 (+8.06%)</td><td>215.30 (-7.32%)</td><td>307.81 <b>(+235.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>462.40 (n/a)</td><td>361.96 (n/a)</td><td>403.30 (n/a)</td><td>232.30 (n/a)</td><td>91.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (-13.43%)</td><td>0.06 (+0.28%)</td><td>0.05 (+3.30%)</td><td>0.04 (+4.06%)</td><td>0.02 <b>(-24.61%)</b></td><td>567.90 (-3.91%)</td><td>452.18 (-3.52%)</td><td>517.60 (-3.20%)</td><td>282.20 (+15.51%)</td><td>119.95 (-12.58%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.00 (n/a)</td><td>468.70 (n/a)</td><td>534.70 (n/a)</td><td>244.30 (n/a)</td><td>137.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (+12.01%)</td><td>0.06 (-7.64%)</td><td>0.05 (-15.90%)</td><td>0.04 (-16.65%)</td><td>0.03 <b>(+45.55%)</b></td><td>581.00 (+19.99%)</td><td>454.68 (+14.84%)</td><td>476.90 (+18.93%)</td><td>227.30 (-10.72%)</td><td>138.56 <b>(+48.25%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>484.20 (n/a)</td><td>395.94 (n/a)</td><td>401.00 (n/a)</td><td>254.60 (n/a)</td><td>93.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (+10.09%)</td><td>0.08 (+0.95%)</td><td>0.08 (+4.12%)</td><td>0.04 (-9.88%)</td><td>0.03 (+14.39%)</td><td>549.90 (+10.98%)</td><td>363.62 (+1.83%)</td><td>315.00 (-3.93%)</td><td>218.80 (-9.17%)</td><td>140.46 (+17.45%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>495.50 (n/a)</td><td>357.10 (n/a)</td><td>327.90 (n/a)</td><td>240.90 (n/a)</td><td>119.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 <b>(+26.27%)</b></td><td>0.07 <b>(+33.82%)</b></td><td>0.06 <b>(+32.38%)</b></td><td>0.04 (+2.22%)</td><td>0.03 <b>(+58.03%)</b></td><td>598.50 (-2.17%)</td><td>393.02 <b>(-20.63%)</b></td><td>423.30 <b>(-24.45%)</b></td><td>227.00 <b>(-20.82%)</b></td><td>156.22 (+16.72%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>611.80 (n/a)</td><td>495.16 (n/a)</td><td>560.30 (n/a)</td><td>286.70 (n/a)</td><td>133.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 <b>(-22.20%)</b></td><td>0.06 (-7.18%)</td><td>0.06 (+3.83%)</td><td>0.04 (-10.75%)</td><td>0.02 <b>(-24.19%)</b></td><td>520.90 (+12.05%)</td><td>325.92 (+6.36%)</td><td>292.30 (-3.69%)</td><td>233.90 <b>(+28.52%)</b></td><td>116.67 (+10.66%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>464.90 (n/a)</td><td>306.42 (n/a)</td><td>303.50 (n/a)</td><td>182.00 (n/a)</td><td>105.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (+14.67%)</td><td>0.07 <b>(+50.51%)</b></td><td>0.07 <b>(+70.62%)</b></td><td>0.03 <b>(+210.70%)</b></td><td>0.02 (-15.59%)</td><td>605.60 <b>(-67.81%)</b></td><td>314.92 <b>(-53.75%)</b></td><td>251.60 <b>(-41.39%)</b></td><td>217.50 (-12.79%)</td><td>163.46 <b>(-76.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1881.60 (n/a)</td><td>680.86 (n/a)</td><td>429.30 (n/a)</td><td>249.40 (n/a)</td><td>681.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 <b>(+75.41%)</b></td><td>0.05 <b>(+32.25%)</b></td><td>0.04 (+10.60%)</td><td>0.03 <b>(+56.29%)</b></td><td>0.02 <b>(+121.96%)</b></td><td>566.00 <b>(-36.02%)</b></td><td>451.96 <b>(-21.41%)</b></td><td>485.80 (-9.58%)</td><td>229.50 <b>(-42.98%)</b></td><td>130.02 <b>(-28.57%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>884.60 (n/a)</td><td>575.06 (n/a)</td><td>537.30 (n/a)</td><td>402.50 (n/a)</td><td>182.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (-0.52%)</td><td>0.05 (-4.75%)</td><td>0.05 (-12.00%)</td><td>0.03 (+0.94%)</td><td>0.02 (-6.93%)</td><td>550.30 (-0.94%)</td><td>386.52 (+3.08%)</td><td>342.80 (+13.62%)</td><td>229.60 (+0.53%)</td><td>137.37 (-8.30%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>555.50 (n/a)</td><td>374.98 (n/a)</td><td>301.70 (n/a)</td><td>228.40 (n/a)</td><td>149.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (+17.24%)</td><td>0.05 (+3.52%)</td><td>0.04 (-0.53%)</td><td>0.03 (-18.96%)</td><td>0.02 <b>(+46.70%)</b></td><td>605.70 <b>(+23.39%)</b></td><td>405.76 (+2.73%)</td><td>447.20 (+0.52%)</td><td>223.10 (-14.68%)</td><td>147.68 <b>(+49.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>490.90 (n/a)</td><td>394.98 (n/a)</td><td>444.90 (n/a)</td><td>261.50 (n/a)</td><td>98.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (-6.12%)</td><td>0.05 (+3.00%)</td><td>0.04 (+14.44%)</td><td>0.03 (-4.79%)</td><td>0.02 (-13.96%)</td><td>531.70 (+5.04%)</td><td>409.48 (-4.88%)</td><td>419.60 (-12.60%)</td><td>227.10 (+6.52%)</td><td>117.72 (-4.24%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>506.20 (n/a)</td><td>430.48 (n/a)</td><td>480.10 (n/a)</td><td>213.20 (n/a)</td><td>122.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.40 (+17.58%)</td><td>0.25 (-5.73%)</td><td>0.19 <b>(-43.04%)</b></td><td>0.17 (+1.28%)</td><td>0.11 (+19.11%)</td><td>578.20 (-1.26%)</td><td>441.32 (+8.32%)</td><td>527.30 <b>(+75.53%)</b></td><td>243.20 (-14.97%)</td><td>159.39 (+1.90%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>585.60 (n/a)</td><td>407.42 (n/a)</td><td>300.40 (n/a)</td><td>286.00 (n/a)</td><td>156.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.42 (-11.09%)</td><td>0.28 (-9.19%)</td><td>0.32 (+17.38%)</td><td>0.05 <b>(-67.59%)</b></td><td>0.16 (+13.08%)</td><td>1932.70 <b>(+208.59%)</b></td><td>656.90 <b>(+67.97%)</b></td><td>310.50 (-14.81%)</td><td>232.50 (+12.48%)</td><td>726.38 <b>(+296.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>626.30 (n/a)</td><td>391.08 (n/a)</td><td>364.50 (n/a)</td><td>206.70 (n/a)</td><td>183.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.34 (-4.32%)</td><td>0.22 (-15.53%)</td><td>0.21 <b>(-20.52%)</b></td><td>0.09 <b>(-41.58%)</b></td><td>0.10 <b>(+27.82%)</b></td><td>1057.80 <b>(+71.19%)</b></td><td>549.60 <b>(+34.92%)</b></td><td>458.80 <b>(+25.84%)</b></td><td>292.50 (+4.50%)</td><td>311.57 <b>(+125.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>617.90 (n/a)</td><td>407.34 (n/a)</td><td>364.60 (n/a)</td><td>279.90 (n/a)</td><td>137.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.34 (+14.37%)</td><td>0.23 (-1.24%)</td><td>0.24 (-7.35%)</td><td>0.12 <b>(-23.07%)</b></td><td>0.09 <b>(+30.26%)</b></td><td>621.50 <b>(+29.99%)</b></td><td>373.40 (+7.86%)</td><td>312.90 (+7.93%)</td><td>214.40 (-12.56%)</td><td>165.45 <b>(+46.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>478.10 (n/a)</td><td>346.20 (n/a)</td><td>289.90 (n/a)</td><td>245.20 (n/a)</td><td>113.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.27 <b>(+48.83%)</b></td><td>0.15 (-9.71%)</td><td>0.15 (-8.17%)</td><td>0.04 <b>(-73.77%)</b></td><td>0.08 <b>(+458.62%)</b></td><td>1876.80 <b>(+281.23%)</b></td><td>737.86 <b>(+63.82%)</b></td><td>497.90 (+8.90%)</td><td>270.40 <b>(-32.80%)</b></td><td>645.90 <b>(+1515.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>492.30 (n/a)</td><td>450.42 (n/a)</td><td>457.20 (n/a)</td><td>402.40 (n/a)</td><td>39.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.36 <b>(+34.00%)</b></td><td>0.24 <b>(+28.81%)</b></td><td>0.22 <b>(+36.95%)</b></td><td>0.15 (+11.06%)</td><td>0.09 <b>(+54.43%)</b></td><td>496.10 (-9.96%)</td><td>337.72 (-19.36%)</td><td>340.40 <b>(-26.98%)</b></td><td>203.10 <b>(-25.36%)</b></td><td>120.15 (+3.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>551.00 (n/a)</td><td>418.78 (n/a)</td><td>466.20 (n/a)</td><td>272.10 (n/a)</td><td>116.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+4.93%)</td><td>0.11 (+9.01%)</td><td>0.12 (-2.74%)</td><td>0.07 <b>(+24.51%)</b></td><td>0.03 <b>(-27.74%)</b></td><td>496.70 (-19.68%)</td><td>344.40 (-14.27%)</td><td>302.10 (+2.83%)</td><td>266.40 (-4.69%)</td><td>94.00 <b>(-42.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>618.40 (n/a)</td><td>401.72 (n/a)</td><td>293.80 (n/a)</td><td>279.50 (n/a)</td><td>162.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 <b>(+29.31%)</b></td><td>0.11 (+7.34%)</td><td>0.08 (-8.76%)</td><td>0.06 <b>(-23.75%)</b></td><td>0.05 <b>(+138.48%)</b></td><td>576.90 <b>(+31.14%)</b></td><td>401.64 (+5.78%)</td><td>460.90 (+9.61%)</td><td>222.20 <b>(-22.69%)</b></td><td>162.73 <b>(+126.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>439.90 (n/a)</td><td>379.70 (n/a)</td><td>420.50 (n/a)</td><td>287.40 (n/a)</td><td>71.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (+4.04%)</td><td>0.11 (-8.89%)</td><td>0.12 (-4.43%)</td><td>0.06 <b>(-20.45%)</b></td><td>0.04 <b>(+25.66%)</b></td><td>587.20 <b>(+25.71%)</b></td><td>379.30 (+16.86%)</td><td>295.30 (+4.64%)</td><td>232.20 (-3.89%)</td><td>157.44 <b>(+60.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>467.10 (n/a)</td><td>324.58 (n/a)</td><td>282.20 (n/a)</td><td>241.60 (n/a)</td><td>98.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 <b>(+32.19%)</b></td><td>0.07 <b>(+35.67%)</b></td><td>0.08 (+10.58%)</td><td>0.04 <b>(+105.31%)</b></td><td>0.02 (-3.87%)</td><td>1016.80 <b>(-51.29%)</b></td><td>562.64 <b>(-38.01%)</b></td><td>485.90 (-9.57%)</td><td>368.60 <b>(-24.34%)</b></td><td>259.26 <b>(-61.84%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>2087.50 (n/a)</td><td>907.64 (n/a)</td><td>537.30 (n/a)</td><td>487.20 (n/a)</td><td>679.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 <b>(-32.07%)</b></td><td>0.10 (-14.18%)</td><td>0.09 (+6.15%)</td><td>0.06 (-11.40%)</td><td>0.03 <b>(-42.94%)</b></td><td>586.70 (+12.87%)</td><td>403.86 (+7.56%)</td><td>419.20 (-5.78%)</td><td>266.50 <b>(+47.24%)</b></td><td>133.16 (-11.47%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>519.80 (n/a)</td><td>375.48 (n/a)</td><td>444.90 (n/a)</td><td>181.00 (n/a)</td><td>150.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (+6.63%)</td><td>0.11 (+4.86%)</td><td>0.14 (+6.35%)</td><td>0.05 (-7.77%)</td><td>0.04 (+8.33%)</td><td>681.00 (+8.44%)</td><td>389.82 (-2.69%)</td><td>261.90 (-5.96%)</td><td>245.40 (-6.23%)</td><td>194.38 (+7.41%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>628.00 (n/a)</td><td>400.60 (n/a)</td><td>278.50 (n/a)</td><td>261.70 (n/a)</td><td>180.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (-3.03%)</td><td>0.11 (-1.88%)</td><td>0.09 (-18.88%)</td><td>0.08 (+8.59%)</td><td>0.03 (-0.35%)</td><td>525.80 (-7.92%)</td><td>414.22 (+1.34%)</td><td>471.00 <b>(+23.30%)</b></td><td>284.30 (+3.12%)</td><td>116.43 (-8.47%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>571.00 (n/a)</td><td>408.76 (n/a)</td><td>382.00 (n/a)</td><td>275.70 (n/a)</td><td>127.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (-4.55%)</td><td>0.12 (+0.27%)</td><td>0.14 <b>(+48.73%)</b></td><td>0.06 <b>(-27.16%)</b></td><td>0.05 (+19.62%)</td><td>649.50 <b>(+37.29%)</b></td><td>413.66 (+9.08%)</td><td>289.00 <b>(-32.78%)</b></td><td>234.10 (+4.74%)</td><td>198.71 <b>(+78.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>473.10 (n/a)</td><td>379.22 (n/a)</td><td>429.90 (n/a)</td><td>223.50 (n/a)</td><td>111.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (+4.84%)</td><td>0.11 (-0.72%)</td><td>0.08 <b>(-32.03%)</b></td><td>0.07 (+12.14%)</td><td>0.05 (+13.36%)</td><td>563.60 (-10.84%)</td><td>416.30 (+1.89%)</td><td>498.10 <b>(+47.11%)</b></td><td>222.70 (-4.63%)</td><td>158.62 (-5.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>632.10 (n/a)</td><td>408.58 (n/a)</td><td>338.60 (n/a)</td><td>233.50 (n/a)</td><td>168.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (+3.75%)</td><td>0.12 (+17.65%)</td><td>0.15 <b>(+78.58%)</b></td><td>0.07 (+7.19%)</td><td>0.04 (+3.45%)</td><td>563.50 (-6.71%)</td><td>380.76 (-15.10%)</td><td>274.90 <b>(-44.01%)</b></td><td>252.10 (-3.59%)</td><td>158.20 (-4.97%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>604.00 (n/a)</td><td>448.48 (n/a)</td><td>491.00 (n/a)</td><td>261.50 (n/a)</td><td>166.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 <b>(+36.60%)</b></td><td>0.13 (+16.75%)</td><td>0.14 (-4.07%)</td><td>0.07 <b>(+32.95%)</b></td><td>0.06 (+18.34%)</td><td>601.40 <b>(-24.79%)</b></td><td>359.08 (-17.09%)</td><td>294.00 (+4.22%)</td><td>195.30 <b>(-26.80%)</b></td><td>167.35 <b>(-29.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>799.60 (n/a)</td><td>433.12 (n/a)</td><td>282.10 (n/a)</td><td>266.80 (n/a)</td><td>236.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.19 (+16.86%)</td><td>0.13 <b>(+24.31%)</b></td><td>0.13 (+10.04%)</td><td>0.07 <b>(+227.17%)</b></td><td>0.05 (-19.20%)</td><td>576.60 <b>(-69.44%)</b></td><td>355.72 <b>(-46.93%)</b></td><td>303.40 (-9.13%)</td><td>210.90 (-14.44%)</td><td>143.74 <b>(-79.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1886.50 (n/a)</td><td>670.28 (n/a)</td><td>333.90 (n/a)</td><td>246.50 (n/a)</td><td>693.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (+2.35%)</td><td>0.10 (-10.67%)</td><td>0.09 (-17.43%)</td><td>0.07 (-12.36%)</td><td>0.03 <b>(+44.45%)</b></td><td>488.60 (+14.11%)</td><td>373.30 (+17.45%)</td><td>371.80 <b>(+21.11%)</b></td><td>236.20 (-2.32%)</td><td>115.76 <b>(+65.27%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>428.20 (n/a)</td><td>317.84 (n/a)</td><td>307.00 (n/a)</td><td>241.80 (n/a)</td><td>70.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (-6.77%)</td><td>0.07 <b>(-40.41%)</b></td><td>0.06 <b>(-47.20%)</b></td><td>0.02 <b>(-71.81%)</b></td><td>0.04 <b>(+39.49%)</b></td><td>1887.20 <b>(+254.80%)</b></td><td>766.20 <b>(+132.89%)</b></td><td>554.40 <b>(+89.41%)</b></td><td>267.30 (+7.26%)</td><td>642.96 <b>(+454.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>531.90 (n/a)</td><td>329.00 (n/a)</td><td>292.70 (n/a)</td><td>249.20 (n/a)</td><td>115.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 <b>(-36.59%)</b></td><td>0.08 <b>(-26.35%)</b></td><td>0.08 <b>(-26.72%)</b></td><td>0.06 (-6.04%)</td><td>0.01 <b>(-69.41%)</b></td><td>567.10 (+6.42%)</td><td>449.78 <b>(+24.75%)</b></td><td>441.50 <b>(+36.48%)</b></td><td>377.50 <b>(+57.75%)</b></td><td>70.64 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>532.90 (n/a)</td><td>360.54 (n/a)</td><td>323.50 (n/a)</td><td>239.30 (n/a)</td><td>130.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 <b>(+43.49%)</b></td><td>0.11 <b>(+34.19%)</b></td><td>0.11 <b>(+70.88%)</b></td><td>0.06 (-0.87%)</td><td>0.05 <b>(+87.62%)</b></td><td>599.90 (+0.87%)</td><td>380.30 (-17.39%)</td><td>306.80 <b>(-41.48%)</b></td><td>219.00 <b>(-30.32%)</b></td><td>179.97 <b>(+37.96%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>594.70 (n/a)</td><td>460.38 (n/a)</td><td>524.30 (n/a)</td><td>314.30 (n/a)</td><td>130.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (+16.85%)</td><td>0.09 (-11.82%)</td><td>0.07 <b>(-30.72%)</b></td><td>0.04 <b>(-43.09%)</b></td><td>0.04 <b>(+70.21%)</b></td><td>967.40 <b>(+75.73%)</b></td><td>508.48 <b>(+34.11%)</b></td><td>482.90 <b>(+44.32%)</b></td><td>238.00 (-14.42%)</td><td>285.49 <b>(+153.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>550.50 (n/a)</td><td>379.16 (n/a)</td><td>334.60 (n/a)</td><td>278.10 (n/a)</td><td>112.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (+2.95%)</td><td>0.12 <b>(+27.21%)</b></td><td>0.12 <b>(+66.52%)</b></td><td>0.09 <b>(+40.64%)</b></td><td>0.02 <b>(-42.50%)</b></td><td>406.30 <b>(-28.89%)</b></td><td>307.54 <b>(-27.81%)</b></td><td>278.80 <b>(-39.94%)</b></td><td>258.50 (-2.86%)</td><td>61.16 <b>(-59.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>571.40 (n/a)</td><td>426.04 (n/a)</td><td>464.20 (n/a)</td><td>266.10 (n/a)</td><td>149.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.44 (+10.35%)</td><td>0.31 <b>(+24.00%)</b></td><td>0.24 (+4.46%)</td><td>0.22 <b>(+315.36%)</b></td><td>0.10 <b>(-23.10%)</b></td><td>586.90 <b>(-75.92%)</b></td><td>461.36 <b>(-46.77%)</b></td><td>537.90 (-4.27%)</td><td>298.20 (-9.39%)</td><td>138.95 <b>(-84.35%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>0.14 (n/a)</td><td>2437.70 (n/a)</td><td>866.70 (n/a)</td><td>561.90 (n/a)</td><td>329.10 (n/a)</td><td>887.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.44 (+9.02%)</td><td>0.28 (-2.15%)</td><td>0.25 (-3.18%)</td><td>0.18 (-4.87%)</td><td>0.10 (+9.47%)</td><td>722.10 (+5.12%)</td><td>502.86 (+3.07%)</td><td>521.40 (+3.29%)</td><td>297.50 (-8.26%)</td><td>154.09 (+4.96%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>686.90 (n/a)</td><td>487.86 (n/a)</td><td>504.80 (n/a)</td><td>324.30 (n/a)</td><td>146.81 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.27 <b>(-45.92%)</b></td><td>0.24 <b>(-27.75%)</b></td><td>0.24 (-14.27%)</td><td>0.21 (-14.36%)</td><td>0.03 <b>(-73.76%)</b></td><td>635.20 (+16.76%)</td><td>558.52 <b>(+28.94%)</b></td><td>557.40 (+16.64%)</td><td>483.80 <b>(+84.94%)</b></td><td>69.74 <b>(-45.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>544.00 (n/a)</td><td>433.16 (n/a)</td><td>477.90 (n/a)</td><td>261.60 (n/a)</td><td>127.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-11.51%)</td><td>0.02 (+5.07%)</td><td>0.01 (-11.61%)</td><td>0.01 <b>(+74.76%)</b></td><td>0.00 <b>(-71.61%)</b></td><td>292.70 <b>(-42.78%)</b></td><td>266.24 (-15.23%)</td><td>274.40 (+13.15%)</td><td>234.10 (+13.04%)</td><td>24.47 <b>(-81.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.50 (n/a)</td><td>314.08 (n/a)</td><td>242.50 (n/a)</td><td>207.10 (n/a)</td><td>131.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (-11.64%)</td><td>0.01 (-14.32%)</td><td>0.01 (-7.51%)</td><td>0.01 <b>(-37.94%)</b></td><td>0.00 <b>(+30.98%)</b></td><td>555.50 <b>(+61.15%)</b></td><td>325.82 <b>(+24.14%)</b></td><td>277.10 (+8.12%)</td><td>241.70 (+13.21%)</td><td>129.96 <b>(+151.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>344.70 (n/a)</td><td>262.46 (n/a)</td><td>256.30 (n/a)</td><td>213.50 (n/a)</td><td>51.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (-15.32%)</td><td>0.01 (-4.48%)</td><td>0.01 (-3.53%)</td><td>0.01 (+5.21%)</td><td>0.00 <b>(-37.22%)</b></td><td>735.40 (-4.95%)</td><td>466.40 (-4.17%)</td><td>392.80 (+3.64%)</td><td>348.30 (+18.07%)</td><td>161.55 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>773.70 (n/a)</td><td>486.72 (n/a)</td><td>379.00 (n/a)</td><td>295.00 (n/a)</td><td>226.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>7.93 (-18.52%)</td><td>6.99 (+9.94%)</td><td>7.25 <b>(+43.47%)</b></td><td>4.73 <b>(+32.44%)</b></td><td>1.31 <b>(-53.38%)</b></td><td>443.20 <b>(-24.50%)</b></td><td>311.46 (-19.15%)</td><td>289.40 <b>(-30.30%)</b></td><td>264.70 <b>(+22.72%)</b></td><td>74.83 <b>(-53.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.73 (n/a)</td><td>6.35 (n/a)</td><td>5.05 (n/a)</td><td>3.57 (n/a)</td><td>2.81 (n/a)</td><td>587.00 (n/a)</td><td>385.22 (n/a)</td><td>415.20 (n/a)</td><td>215.70 (n/a)</td><td>159.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.52 (+2.97%)</td><td>0.38 (+5.66%)</td><td>0.31 (+11.78%)</td><td>0.26 (+11.32%)</td><td>0.11 (-9.65%)</td><td>498.80 (-10.16%)</td><td>376.00 (-7.67%)</td><td>421.40 (-10.55%)</td><td>255.00 (-2.86%)</td><td>104.77 (-19.78%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.50 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>555.20 (n/a)</td><td>407.24 (n/a)</td><td>471.10 (n/a)</td><td>262.50 (n/a)</td><td>130.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.56 (+9.06%)</td><td>0.38 (-4.35%)</td><td>0.39 (-16.60%)</td><td>0.07 <b>(-73.39%)</b></td><td>0.20 <b>(+52.85%)</b></td><td>2014.80 <b>(+275.83%)</b></td><td>647.54 <b>(+73.62%)</b></td><td>342.60 (+19.92%)</td><td>237.50 (-8.34%)</td><td>767.31 <b>(+451.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>536.10 (n/a)</td><td>372.96 (n/a)</td><td>285.70 (n/a)</td><td>259.10 (n/a)</td><td>139.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.57 <b>(+28.18%)</b></td><td>0.45 <b>(+22.13%)</b></td><td>0.48 <b>(+41.60%)</b></td><td>0.30 (-2.43%)</td><td>0.10 <b>(+51.93%)</b></td><td>434.60 (+2.48%)</td><td>304.90 (-16.27%)</td><td>277.10 <b>(-29.38%)</b></td><td>231.20 <b>(-21.97%)</b></td><td>79.88 <b>(+27.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>424.10 (n/a)</td><td>364.14 (n/a)</td><td>392.40 (n/a)</td><td>296.30 (n/a)</td><td>62.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.58 <b>(+25.14%)</b></td><td>0.38 <b>(+24.43%)</b></td><td>0.36 <b>(+36.94%)</b></td><td>0.27 (+6.07%)</td><td>0.13 <b>(+45.11%)</b></td><td>494.50 (-5.72%)</td><td>375.06 (-16.92%)</td><td>364.60 <b>(-26.96%)</b></td><td>225.90 <b>(-20.09%)</b></td><td>115.85 (+16.12%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>524.50 (n/a)</td><td>451.46 (n/a)</td><td>499.20 (n/a)</td><td>282.70 (n/a)</td><td>99.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.52 (-3.52%)</td><td>0.44 <b>(+27.72%)</b></td><td>0.46 <b>(+55.29%)</b></td><td>0.31 (+12.09%)</td><td>0.08 <b>(-29.24%)</b></td><td>423.00 (-10.80%)</td><td>308.08 <b>(-23.92%)</b></td><td>287.60 <b>(-35.60%)</b></td><td>254.20 (+3.67%)</td><td>65.87 <b>(-28.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.54 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>474.20 (n/a)</td><td>404.92 (n/a)</td><td>446.60 (n/a)</td><td>245.20 (n/a)</td><td>92.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (+6.82%)</td><td>0.01 (+19.33%)</td><td>0.01 (+2.26%)</td><td>0.01 <b>(+56.36%)</b></td><td>0.00 <b>(-63.52%)</b></td><td>323.50 <b>(-36.04%)</b></td><td>289.92 <b>(-21.82%)</b></td><td>294.10 (-2.23%)</td><td>257.70 (-6.39%)</td><td>25.27 <b>(-78.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.80 (n/a)</td><td>370.82 (n/a)</td><td>300.80 (n/a)</td><td>275.30 (n/a)</td><td>117.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 <b>(+27.94%)</b></td><td>0.01 <b>(+38.80%)</b></td><td>0.01 <b>(+34.52%)</b></td><td>0.01 <b>(+42.06%)</b></td><td>0.00 (+0.58%)</td><td>423.80 <b>(-29.60%)</b></td><td>305.42 <b>(-29.78%)</b></td><td>287.30 <b>(-25.65%)</b></td><td>240.70 <b>(-21.85%)</b></td><td>69.66 <b>(-43.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.00 (n/a)</td><td>434.94 (n/a)</td><td>386.40 (n/a)</td><td>308.00 (n/a)</td><td>122.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.00 (+0.00%)</td><td>0.00 (+19.05%)</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+8.18%)</td><td>16687.02 (-7.48%)</td><td>9772.80 <b>(-23.15%)</b></td><td>6530.80 <b>(-59.59%)</b></td><td>5722.76 (-8.31%)</td><td>5135.32 (-9.14%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18036.68 (n/a)</td><td>12717.04 (n/a)</td><td>16161.26 (n/a)</td><td>6241.55 (n/a)</td><td>5651.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+39.13%)</b></td><td>0.00 (+18.18%)</td><td>0.00 <b>(+175.00%)</b></td><td>0.00 <b>(-77.50%)</b></td><td>7334.75 <b>(-64.93%)</b></td><td>6421.46 <b>(-45.79%)</b></td><td>6324.07 (-13.78%)</td><td>5898.48 (+1.10%)</td><td>555.96 <b>(-92.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20911.92 (n/a)</td><td>11844.85 (n/a)</td><td>7335.13 (n/a)</td><td>5834.34 (n/a)</td><td>7351.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (-3.40%)</td><td>0.10 (+0.34%)</td><td>0.09 (+17.58%)</td><td>0.08 (+9.22%)</td><td>0.03 <b>(-23.77%)</b></td><td>27675.94 (-8.42%)</td><td>22136.16 (-4.81%)</td><td>23737.46 (-14.99%)</td><td>14762.81 (+3.56%)</td><td>5833.63 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>30219.41 (n/a)</td><td>23255.75 (n/a)</td><td>27922.02 (n/a)</td><td>14255.48 (n/a)</td><td>7835.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.67 (-14.00%)</td><td>1.31 <b>(-21.56%)</b></td><td>1.19 <b>(-44.70%)</b></td><td>0.30 (-0.48%)</td><td>0.87 <b>(-27.55%)</b></td><td>3514.80 (+0.48%)</td><td>1321.96 (-1.42%)</td><td>879.00 <b>(+80.83%)</b></td><td>392.00 (+16.25%)</td><td>1251.39 (-8.49%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.11 (n/a)</td><td>1.67 (n/a)</td><td>2.16 (n/a)</td><td>0.30 (n/a)</td><td>1.20 (n/a)</td><td>3498.10 (n/a)</td><td>1341.00 (n/a)</td><td>486.10 (n/a)</td><td>337.20 (n/a)</td><td>1367.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.54 (-11.31%)</td><td>2.22 (+4.97%)</td><td>1.96 (+10.55%)</td><td>1.42 (+3.40%)</td><td>0.86 (-18.77%)</td><td>738.80 (-3.29%)</td><td>526.98 (-7.43%)</td><td>534.40 (-9.55%)</td><td>296.60 (+12.78%)</td><td>181.33 (-3.90%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.99 (n/a)</td><td>2.12 (n/a)</td><td>1.77 (n/a)</td><td>1.37 (n/a)</td><td>1.06 (n/a)</td><td>763.90 (n/a)</td><td>569.26 (n/a)</td><td>590.80 (n/a)</td><td>263.00 (n/a)</td><td>188.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.58 (-11.86%)</td><td>2.54 (+12.26%)</td><td>2.75 (+4.67%)</td><td>0.90 <b>(+198.60%)</b></td><td>1.04 <b>(-26.02%)</b></td><td>1165.40 <b>(-66.51%)</b></td><td>526.04 <b>(-49.20%)</b></td><td>381.90 (-4.45%)</td><td>293.10 (+13.47%)</td><td>362.87 <b>(-73.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.06 (n/a)</td><td>2.26 (n/a)</td><td>2.62 (n/a)</td><td>0.30 (n/a)</td><td>1.40 (n/a)</td><td>3480.00 (n/a)</td><td>1035.58 (n/a)</td><td>399.70 (n/a)</td><td>258.30 (n/a)</td><td>1373.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.95 <b>(-23.52%)</b></td><td>2.20 (-16.95%)</td><td>2.11 (-19.43%)</td><td>1.59 (+9.35%)</td><td>0.53 <b>(-42.91%)</b></td><td>658.90 (-8.55%)</td><td>497.48 (+12.73%)</td><td>496.20 <b>(+24.14%)</b></td><td>355.90 <b>(+30.80%)</b></td><td>116.86 <b>(-33.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.85 (n/a)</td><td>2.65 (n/a)</td><td>2.62 (n/a)</td><td>1.46 (n/a)</td><td>0.92 (n/a)</td><td>720.50 (n/a)</td><td>441.30 (n/a)</td><td>399.70 (n/a)</td><td>272.10 (n/a)</td><td>174.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.81 <b>(-33.36%)</b></td><td>2.14 <b>(-30.86%)</b></td><td>2.49 <b>(-28.04%)</b></td><td>0.87 <b>(-43.56%)</b></td><td>0.76 <b>(-24.88%)</b></td><td>2398.30 <b>(+77.18%)</b></td><td>1170.66 <b>(+53.37%)</b></td><td>840.70 <b>(+38.98%)</b></td><td>746.10 <b>(+50.06%)</b></td><td>693.96 <b>(+101.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.22 (n/a)</td><td>3.10 (n/a)</td><td>3.47 (n/a)</td><td>1.55 (n/a)</td><td>1.01 (n/a)</td><td>1353.60 (n/a)</td><td>763.30 (n/a)</td><td>604.90 (n/a)</td><td>497.20 (n/a)</td><td>343.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.86 (+3.69%)</td><td>1.78 <b>(-53.48%)</b></td><td>0.86 <b>(-78.42%)</b></td><td>0.59 (+0.38%)</td><td>2.29 (+12.21%)</td><td>3555.40 (-0.38%)</td><td>2397.40 <b>(+119.37%)</b></td><td>2447.30 <b>(+363.42%)</b></td><td>358.10 (-3.56%)</td><td>1294.10 (-6.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.65 (n/a)</td><td>3.82 (n/a)</td><td>3.97 (n/a)</td><td>0.59 (n/a)</td><td>2.04 (n/a)</td><td>3568.80 (n/a)</td><td>1092.84 (n/a)</td><td>528.10 (n/a)</td><td>371.30 (n/a)</td><td>1387.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.85 <b>(-34.05%)</b></td><td>2.40 <b>(-26.66%)</b></td><td>2.89 (-6.56%)</td><td>0.84 <b>(+44.59%)</b></td><td>1.45 <b>(-22.52%)</b></td><td>2491.80 <b>(-30.84%)</b></td><td>1359.94 (+15.64%)</td><td>725.50 (+7.02%)</td><td>545.10 <b>(+51.63%)</b></td><td>1014.68 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.83 (n/a)</td><td>3.27 (n/a)</td><td>3.09 (n/a)</td><td>0.58 (n/a)</td><td>1.88 (n/a)</td><td>3602.80 (n/a)</td><td>1176.04 (n/a)</td><td>677.90 (n/a)</td><td>359.50 (n/a)</td><td>1362.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.35 (-11.53%)</td><td>2.95 (-12.76%)</td><td>2.62 <b>(-26.07%)</b></td><td>0.59 (+1.66%)</td><td>1.74 (-14.50%)</td><td>3534.90 (-1.63%)</td><td>1226.32 (+4.38%)</td><td>800.10 <b>(+35.27%)</b></td><td>391.70 (+13.01%)</td><td>1302.86 (-4.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>6.05 (n/a)</td><td>3.38 (n/a)</td><td>3.55 (n/a)</td><td>0.58 (n/a)</td><td>2.04 (n/a)</td><td>3593.50 (n/a)</td><td>1174.84 (n/a)</td><td>591.50 (n/a)</td><td>346.60 (n/a)</td><td>1364.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.41 <b>(-42.64%)</b></td><td>2.01 <b>(-46.26%)</b></td><td>2.08 <b>(-41.00%)</b></td><td>0.60 <b>(-45.94%)</b></td><td>1.27 <b>(-37.06%)</b></td><td>3476.50 <b>(+84.97%)</b></td><td>1652.26 <b>(+105.20%)</b></td><td>1008.60 <b>(+69.51%)</b></td><td>614.10 <b>(+74.31%)</b></td><td>1270.79 <b>(+101.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>5.95 (n/a)</td><td>3.73 (n/a)</td><td>3.52 (n/a)</td><td>1.12 (n/a)</td><td>2.02 (n/a)</td><td>1879.50 (n/a)</td><td>805.18 (n/a)</td><td>595.00 (n/a)</td><td>352.30 (n/a)</td><td>629.33 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.62 <b>(-24.02%)</b></td><td>2.86 (-16.47%)</td><td>3.32 (-5.50%)</td><td>0.60 <b>(-70.77%)</b></td><td>1.27 (-3.62%)</td><td>3486.80 <b>(+242.15%)</b></td><td>1188.32 <b>(+69.76%)</b></td><td>630.80 (+5.82%)</td><td>579.20 <b>(+31.61%)</b></td><td>1285.21 <b>(+346.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.77 (n/a)</td><td>3.42 (n/a)</td><td>3.52 (n/a)</td><td>2.06 (n/a)</td><td>1.32 (n/a)</td><td>1019.10 (n/a)</td><td>700.02 (n/a)</td><td>596.10 (n/a)</td><td>440.10 (n/a)</td><td>287.61 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.25 (+7.78%)</td><td>4.53 <b>(+29.15%)</b></td><td>4.43 (+11.56%)</td><td>3.46 <b>(+196.57%)</b></td><td>0.73 <b>(-48.06%)</b></td><td>1213.50 <b>(-66.28%)</b></td><td>947.88 <b>(-38.96%)</b></td><td>946.40 (-10.36%)</td><td>799.00 (-7.22%)</td><td>167.18 <b>(-85.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>4.87 (n/a)</td><td>3.51 (n/a)</td><td>3.97 (n/a)</td><td>1.17 (n/a)</td><td>1.40 (n/a)</td><td>3598.80 (n/a)</td><td>1552.76 (n/a)</td><td>1055.80 (n/a)</td><td>861.20 (n/a)</td><td>1150.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.97 <b>(-36.35%)</b></td><td>2.48 <b>(-62.54%)</b></td><td>1.72 <b>(-76.20%)</b></td><td>1.21 <b>(-36.93%)</b></td><td>1.96 <b>(-34.02%)</b></td><td>3467.90 <b>(+58.56%)</b></td><td>2278.28 <b>(+158.17%)</b></td><td>2438.40 <b>(+320.20%)</b></td><td>702.50 <b>(+57.12%)</b></td><td>995.22 <b>(+35.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.38 (n/a)</td><td>6.63 (n/a)</td><td>7.23 (n/a)</td><td>1.92 (n/a)</td><td>2.98 (n/a)</td><td>2187.10 (n/a)</td><td>882.48 (n/a)</td><td>580.30 (n/a)</td><td>447.10 (n/a)</td><td>737.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.87 (-19.57%)</td><td>3.98 <b>(-32.29%)</b></td><td>4.06 <b>(-37.62%)</b></td><td>1.17 <b>(-33.38%)</b></td><td>2.51 (-8.51%)</td><td>3583.20 <b>(+50.11%)</b></td><td>1655.50 <b>(+67.18%)</b></td><td>1032.80 <b>(+60.30%)</b></td><td>610.50 <b>(+24.34%)</b></td><td>1285.05 <b>(+61.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>8.54 (n/a)</td><td>5.88 (n/a)</td><td>6.51 (n/a)</td><td>1.76 (n/a)</td><td>2.75 (n/a)</td><td>2387.10 (n/a)</td><td>990.26 (n/a)</td><td>644.30 (n/a)</td><td>491.00 (n/a)</td><td>797.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>7.10 <b>(-35.28%)</b></td><td>4.90 (-12.11%)</td><td>4.75 (+8.60%)</td><td>1.72 <b>(+55.06%)</b></td><td>2.12 <b>(-44.31%)</b></td><td>2443.10 <b>(-35.51%)</b></td><td>1103.00 (-18.81%)</td><td>882.20 (-7.92%)</td><td>591.00 <b>(+54.51%)</b></td><td>765.31 <b>(-44.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>10.97 (n/a)</td><td>5.58 (n/a)</td><td>4.38 (n/a)</td><td>1.11 (n/a)</td><td>3.81 (n/a)</td><td>3788.40 (n/a)</td><td>1358.48 (n/a)</td><td>958.10 (n/a)</td><td>382.50 (n/a)</td><td>1390.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>10.28 <b>(+26.53%)</b></td><td>6.22 (-2.24%)</td><td>6.77 (+0.80%)</td><td>1.69 <b>(-56.65%)</b></td><td>3.37 <b>(+117.87%)</b></td><td>2481.50 <b>(+130.69%)</b></td><td>1005.66 <b>(+43.47%)</b></td><td>619.50 (-0.78%)</td><td>408.10 <b>(-20.99%)</b></td><td>855.43 <b>(+293.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>8.12 (n/a)</td><td>6.36 (n/a)</td><td>6.72 (n/a)</td><td>3.90 (n/a)</td><td>1.54 (n/a)</td><td>1075.70 (n/a)</td><td>700.94 (n/a)</td><td>624.40 (n/a)</td><td>516.50 (n/a)</td><td>217.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>9.67 (-0.77%)</td><td>5.98 (-12.88%)</td><td>5.30 <b>(-29.77%)</b></td><td>2.47 (+18.75%)</td><td>2.96 (+4.13%)</td><td>1695.20 (-15.79%)</td><td>887.24 (+7.61%)</td><td>791.70 <b>(+42.39%)</b></td><td>433.80 (+0.77%)</td><td>507.26 <b>(-23.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>9.74 (n/a)</td><td>6.86 (n/a)</td><td>7.54 (n/a)</td><td>2.08 (n/a)</td><td>2.85 (n/a)</td><td>2013.00 (n/a)</td><td>824.48 (n/a)</td><td>556.00 (n/a)</td><td>430.50 (n/a)</td><td>666.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.64 (+2.26%)</td><td>1.27 (+16.54%)</td><td>1.50 <b>(+38.36%)</b></td><td>0.73 (-4.63%)</td><td>0.41 <b>(+25.97%)</b></td><td>718.90 (+4.86%)</td><td>460.14 (-10.75%)</td><td>349.10 <b>(-27.72%)</b></td><td>318.90 (-2.21%)</td><td>177.90 <b>(+26.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.61 (n/a)</td><td>1.09 (n/a)</td><td>1.09 (n/a)</td><td>0.76 (n/a)</td><td>0.33 (n/a)</td><td>685.60 (n/a)</td><td>515.58 (n/a)</td><td>483.00 (n/a)</td><td>326.10 (n/a)</td><td>140.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.81 (+8.34%)</td><td>1.45 <b>(-25.37%)</b></td><td>1.71 <b>(-22.46%)</b></td><td>0.32 <b>(-69.96%)</b></td><td>1.10 <b>(+50.52%)</b></td><td>3280.00 <b>(+232.86%)</b></td><td>1603.86 <b>(+158.07%)</b></td><td>614.70 <b>(+28.98%)</b></td><td>373.10 (-7.69%)</td><td>1517.40 <b>(+460.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>2.59 (n/a)</td><td>1.94 (n/a)</td><td>2.20 (n/a)</td><td>1.06 (n/a)</td><td>0.73 (n/a)</td><td>985.40 (n/a)</td><td>621.48 (n/a)</td><td>476.60 (n/a)</td><td>404.20 (n/a)</td><td>270.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.74 (+3.97%)</td><td>1.84 (+13.22%)</td><td>0.84 <b>(-47.87%)</b></td><td>0.57 (-2.23%)</td><td>1.62 <b>(+31.85%)</b></td><td>3651.20 (+2.28%)</td><td>2186.18 (+7.56%)</td><td>2496.60 <b>(+91.82%)</b></td><td>560.70 (-3.83%)</td><td>1536.87 (+9.66%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>3.60 (n/a)</td><td>1.63 (n/a)</td><td>1.61 (n/a)</td><td>0.59 (n/a)</td><td>1.23 (n/a)</td><td>3569.90 (n/a)</td><td>2032.44 (n/a)</td><td>1301.50 (n/a)</td><td>583.00 (n/a)</td><td>1401.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.76 <b>(+38.33%)</b></td><td>1.19 (+13.82%)</td><td>0.97 (-4.99%)</td><td>0.63 <b>(-28.02%)</b></td><td>0.48 <b>(+188.39%)</b></td><td>828.40 <b>(+38.92%)</b></td><td>505.76 (-0.85%)</td><td>538.30 (+5.26%)</td><td>297.20 <b>(-27.71%)</b></td><td>214.46 <b>(+171.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>1.28 (n/a)</td><td>1.05 (n/a)</td><td>1.03 (n/a)</td><td>0.88 (n/a)</td><td>0.17 (n/a)</td><td>596.30 (n/a)</td><td>510.12 (n/a)</td><td>511.40 (n/a)</td><td>411.10 (n/a)</td><td>79.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 <b>(+33.64%)</b></td><td>0.11 <b>(+23.42%)</b></td><td>0.11 (+13.95%)</td><td>0.06 (-1.28%)</td><td>0.03 <b>(+46.16%)</b></td><td>572.30 (+1.31%)</td><td>334.58 (-15.67%)</td><td>298.60 (-12.23%)</td><td>222.90 <b>(-25.18%)</b></td><td>136.49 <b>(+20.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>564.90 (n/a)</td><td>396.76 (n/a)</td><td>340.20 (n/a)</td><td>297.90 (n/a)</td><td>113.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (+5.98%)</td><td>0.07 (-11.00%)</td><td>0.06 (-8.89%)</td><td>0.05 (-0.01%)</td><td>0.04 (+4.87%)</td><td>618.70 (+0.02%)</td><td>508.68 (+12.10%)</td><td>572.40 (+9.76%)</td><td>229.20 (-5.68%)</td><td>159.75 (-6.85%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>618.60 (n/a)</td><td>453.76 (n/a)</td><td>521.50 (n/a)</td><td>243.00 (n/a)</td><td>171.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.26 (+10.96%)</td><td>0.18 (-4.36%)</td><td>0.16 <b>(-28.75%)</b></td><td>0.12 (-0.91%)</td><td>0.06 (+17.87%)</td><td>551.20 (+0.92%)</td><td>393.06 (+6.24%)</td><td>421.60 <b>(+40.35%)</b></td><td>256.30 (-9.88%)</td><td>122.91 (+6.41%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>546.20 (n/a)</td><td>369.98 (n/a)</td><td>300.40 (n/a)</td><td>284.40 (n/a)</td><td>115.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.31 (+8.86%)</td><td>0.20 (+17.94%)</td><td>0.22 <b>(+55.94%)</b></td><td>0.08 <b>(-35.35%)</b></td><td>0.09 <b>(+43.66%)</b></td><td>774.80 <b>(+54.68%)</b></td><td>405.90 (-2.40%)</td><td>298.70 <b>(-35.86%)</b></td><td>212.20 (-8.14%)</td><td>233.14 <b>(+112.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>500.90 (n/a)</td><td>415.90 (n/a)</td><td>465.70 (n/a)</td><td>231.00 (n/a)</td><td>109.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.26 <b>(+47.54%)</b></td><td>0.15 <b>(+21.31%)</b></td><td>0.11 (+9.88%)</td><td>0.03 <b>(-64.89%)</b></td><td>0.09 <b>(+159.15%)</b></td><td>1982.00 <b>(+184.85%)</b></td><td>743.54 <b>(+30.43%)</b></td><td>582.40 (-8.99%)</td><td>250.70 <b>(-32.21%)</b></td><td>712.02 <b>(+386.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>695.80 (n/a)</td><td>570.06 (n/a)</td><td>639.90 (n/a)</td><td>369.80 (n/a)</td><td>146.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.61 <b>(+44.66%)</b></td><td>0.45 <b>(+25.86%)</b></td><td>0.46 (+16.20%)</td><td>0.23 (-11.88%)</td><td>0.15 <b>(+123.05%)</b></td><td>578.60 (+13.47%)</td><td>326.10 (-13.18%)</td><td>287.90 (-13.93%)</td><td>216.10 <b>(-30.87%)</b></td><td>146.93 <b>(+79.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>509.90 (n/a)</td><td>375.62 (n/a)</td><td>334.50 (n/a)</td><td>312.60 (n/a)</td><td>81.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.33 <b>(-44.01%)</b></td><td>0.23 <b>(-24.69%)</b></td><td>0.25 (+2.91%)</td><td>0.07 <b>(-68.19%)</b></td><td>0.10 <b>(-37.68%)</b></td><td>1936.10 <b>(+214.40%)</b></td><td>779.86 <b>(+59.01%)</b></td><td>526.80 (-2.82%)</td><td>397.50 <b>(+78.57%)</b></td><td>649.59 <b>(+318.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.59 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>615.80 (n/a)</td><td>490.44 (n/a)</td><td>542.10 (n/a)</td><td>222.60 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.45 (-8.40%)</td><td>0.31 (-11.86%)</td><td>0.33 (-1.95%)</td><td>0.14 <b>(-36.93%)</b></td><td>0.14 (+11.88%)</td><td>956.80 <b>(+58.57%)</b></td><td>514.26 <b>(+25.72%)</b></td><td>394.60 (+1.99%)</td><td>291.70 (+9.17%)</td><td>282.80 <b>(+92.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.49 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>603.40 (n/a)</td><td>409.04 (n/a)</td><td>386.90 (n/a)</td><td>267.20 (n/a)</td><td>147.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (+2.65%)</td><td>0.04 (+2.07%)</td><td>0.04 (-1.15%)</td><td>0.03 (+15.09%)</td><td>0.01 (-1.39%)</td><td>519.20 (-13.10%)</td><td>431.10 (-2.89%)</td><td>443.00 (+1.14%)</td><td>280.50 (-2.60%)</td><td>92.16 (-16.91%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>597.50 (n/a)</td><td>443.94 (n/a)</td><td>438.00 (n/a)</td><td>288.00 (n/a)</td><td>110.93 (n/a)</td>
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
