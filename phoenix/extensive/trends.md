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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 <b>(+20.77%)</b></td><td>0.02 <b>(+26.45%)</b></td><td>0.02 <b>(+56.48%)</b></td><td>0.01 (-11.26%)</td><td>0.01 <b>(+22.22%)</b></td><td>610.40 (+12.68%)</td><td>328.76 (-17.39%)</td><td>272.20 <b>(-36.10%)</b></td><td>214.90 (-17.19%)</td><td>160.10 <b>(+28.21%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>397.98 (n/a)</td><td>426.00 (n/a)</td><td>259.50 (n/a)</td><td>124.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (+11.11%)</td><td>0.02 (+0.83%)</td><td>0.02 (+4.26%)</td><td>0.01 (-9.37%)</td><td>0.01 <b>(+39.57%)</b></td><td>549.70 (+10.34%)</td><td>359.78 (+3.36%)</td><td>313.40 (-4.07%)</td><td>241.60 (-9.99%)</td><td>125.93 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.20 (n/a)</td><td>348.10 (n/a)</td><td>326.70 (n/a)</td><td>268.40 (n/a)</td><td>91.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-11.47%)</td><td>0.02 (-11.72%)</td><td>0.01 <b>(-37.83%)</b></td><td>0.01 (+5.59%)</td><td>0.01 (-19.03%)</td><td>470.20 (-5.30%)</td><td>366.48 (+8.21%)</td><td>434.70 <b>(+60.88%)</b></td><td>216.30 (+12.95%)</td><td>115.63 (-19.23%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>338.68 (n/a)</td><td>270.20 (n/a)</td><td>191.50 (n/a)</td><td>143.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (+13.62%)</td><td>0.02 <b>(+22.67%)</b></td><td>0.02 (+14.11%)</td><td>0.01 <b>(+23.17%)</b></td><td>0.01 (-10.06%)</td><td>509.50 (-18.82%)</td><td>306.46 <b>(-23.47%)</b></td><td>249.90 (-12.38%)</td><td>215.60 (-12.00%)</td><td>118.94 <b>(-34.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.60 (n/a)</td><td>400.44 (n/a)</td><td>285.20 (n/a)</td><td>245.00 (n/a)</td><td>182.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (+3.41%)</td><td>0.02 <b>(+28.22%)</b></td><td>0.02 <b>(+77.63%)</b></td><td>0.01 (+4.24%)</td><td>0.01 (-8.20%)</td><td>620.60 (-4.07%)</td><td>338.26 <b>(-23.24%)</b></td><td>277.80 <b>(-43.70%)</b></td><td>231.50 (-3.34%)</td><td>159.58 (-5.19%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.90 (n/a)</td><td>440.70 (n/a)</td><td>493.40 (n/a)</td><td>239.50 (n/a)</td><td>168.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-1.64%)</td><td>0.02 (-10.78%)</td><td>0.02 (-1.86%)</td><td>0.01 (-19.96%)</td><td>0.01 (+4.94%)</td><td>664.70 <b>(+24.94%)</b></td><td>412.08 (+18.03%)</td><td>301.50 (+1.89%)</td><td>223.30 (+1.64%)</td><td>196.06 <b>(+40.44%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>532.00 (n/a)</td><td>349.14 (n/a)</td><td>295.90 (n/a)</td><td>219.70 (n/a)</td><td>139.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (+0.58%)</td><td>0.04 <b>(+27.17%)</b></td><td>0.04 <b>(+49.65%)</b></td><td>0.02 (+0.22%)</td><td>0.02 (+12.08%)</td><td>557.70 (-0.21%)</td><td>361.82 (-18.23%)</td><td>323.00 <b>(-33.17%)</b></td><td>203.70 (-0.59%)</td><td>163.88 (+19.57%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>558.90 (n/a)</td><td>442.48 (n/a)</td><td>483.30 (n/a)</td><td>204.90 (n/a)</td><td>137.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (+4.51%)</td><td>0.04 (+5.97%)</td><td>0.04 (-9.60%)</td><td>0.03 (+4.03%)</td><td>0.01 (+14.58%)</td><td>478.40 (-3.88%)</td><td>336.88 (-4.56%)</td><td>335.30 (+10.62%)</td><td>213.20 (-4.31%)</td><td>117.98 (-1.92%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.70 (n/a)</td><td>352.98 (n/a)</td><td>303.10 (n/a)</td><td>222.80 (n/a)</td><td>120.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-5.95%)</td><td>0.04 (-4.34%)</td><td>0.05 <b>(+33.68%)</b></td><td>0.01 <b>(-78.45%)</b></td><td>0.02 <b>(+69.43%)</b></td><td>2439.60 <b>(+364.07%)</b></td><td>734.88 <b>(+120.23%)</b></td><td>230.70 <b>(-25.19%)</b></td><td>210.30 (+6.32%)</td><td>965.84 <b>(+680.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.70 (n/a)</td><td>333.68 (n/a)</td><td>308.40 (n/a)</td><td>197.80 (n/a)</td><td>123.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(+29.48%)</b></td><td>0.03 (-8.12%)</td><td>0.03 (+1.08%)</td><td>0.01 <b>(-73.03%)</b></td><td>0.02 <b>(+101.48%)</b></td><td>1862.30 <b>(+270.75%)</b></td><td>709.80 <b>(+70.26%)</b></td><td>489.10 (-1.07%)</td><td>208.40 <b>(-22.76%)</b></td><td>663.83 <b>(+491.83%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.30 (n/a)</td><td>416.88 (n/a)</td><td>494.40 (n/a)</td><td>269.80 (n/a)</td><td>112.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 <b>(-20.85%)</b></td><td>0.03 (-6.61%)</td><td>0.03 <b>(+20.64%)</b></td><td>0.02 (-10.74%)</td><td>0.01 <b>(-26.18%)</b></td><td>621.80 (+12.04%)</td><td>421.50 (+3.56%)</td><td>362.10 (-17.12%)</td><td>266.20 <b>(+26.34%)</b></td><td>160.87 (+2.01%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>555.00 (n/a)</td><td>407.00 (n/a)</td><td>436.90 (n/a)</td><td>210.70 (n/a)</td><td>157.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(+69.34%)</b></td><td>0.04 <b>(+67.52%)</b></td><td>0.04 <b>(+65.81%)</b></td><td>0.02 <b>(+210.11%)</b></td><td>0.02 <b>(+65.09%)</b></td><td>621.60 <b>(-67.76%)</b></td><td>387.86 <b>(-49.01%)</b></td><td>294.80 <b>(-39.69%)</b></td><td>217.90 <b>(-40.95%)</b></td><td>191.87 <b>(-70.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1927.80 (n/a)</td><td>760.62 (n/a)</td><td>488.80 (n/a)</td><td>369.00 (n/a)</td><td>657.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(+22.84%)</b></td><td>0.08 <b>(+38.03%)</b></td><td>0.08 <b>(+51.00%)</b></td><td>0.06 <b>(+65.88%)</b></td><td>0.01 <b>(-32.58%)</b></td><td>392.90 <b>(-39.72%)</b></td><td>311.10 <b>(-33.67%)</b></td><td>298.40 <b>(-33.78%)</b></td><td>242.20 (-18.59%)</td><td>57.83 <b>(-66.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>651.80 (n/a)</td><td>469.02 (n/a)</td><td>450.60 (n/a)</td><td>297.50 (n/a)</td><td>173.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 <b>(+29.20%)</b></td><td>0.09 (+11.65%)</td><td>0.10 (+18.81%)</td><td>0.05 (-8.62%)</td><td>0.03 <b>(+63.33%)</b></td><td>515.20 (+9.43%)</td><td>298.34 (-4.57%)</td><td>249.00 (-15.82%)</td><td>179.20 <b>(-22.63%)</b></td><td>128.61 <b>(+39.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>470.80 (n/a)</td><td>312.64 (n/a)</td><td>295.80 (n/a)</td><td>231.60 (n/a)</td><td>92.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 <b>(-21.96%)</b></td><td>0.07 (-0.57%)</td><td>0.08 <b>(+57.63%)</b></td><td>0.04 <b>(-23.97%)</b></td><td>0.02 <b>(-34.05%)</b></td><td>691.80 <b>(+31.52%)</b></td><td>393.64 (-2.55%)</td><td>316.90 <b>(-36.56%)</b></td><td>292.10 <b>(+28.17%)</b></td><td>168.26 (+14.17%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>526.00 (n/a)</td><td>403.96 (n/a)</td><td>499.50 (n/a)</td><td>227.90 (n/a)</td><td>147.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (+12.28%)</td><td>0.07 (+13.90%)</td><td>0.09 <b>(+58.95%)</b></td><td>0.04 (-3.99%)</td><td>0.03 <b>(+20.18%)</b></td><td>568.10 (+4.16%)</td><td>381.90 (-9.07%)</td><td>285.50 <b>(-37.07%)</b></td><td>248.80 (-10.95%)</td><td>155.86 (+17.88%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.40 (n/a)</td><td>419.98 (n/a)</td><td>453.70 (n/a)</td><td>279.40 (n/a)</td><td>132.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (-13.25%)</td><td>0.07 (-18.77%)</td><td>0.06 <b>(-31.90%)</b></td><td>0.04 (+0.68%)</td><td>0.02 (-10.76%)</td><td>567.10 (-0.67%)</td><td>385.26 <b>(+20.69%)</b></td><td>388.10 <b>(+46.84%)</b></td><td>248.00 (+15.30%)</td><td>130.30 (-8.90%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>570.90 (n/a)</td><td>319.22 (n/a)</td><td>264.30 (n/a)</td><td>215.10 (n/a)</td><td>143.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (-6.23%)</td><td>0.06 (-5.33%)</td><td>0.06 (+7.43%)</td><td>0.01 <b>(-52.55%)</b></td><td>0.03 (-4.54%)</td><td>1811.90 <b>(+110.74%)</b></td><td>666.64 <b>(+31.10%)</b></td><td>418.30 (-6.92%)</td><td>266.90 (+6.63%)</td><td>643.92 <b>(+150.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>859.80 (n/a)</td><td>508.48 (n/a)</td><td>449.40 (n/a)</td><td>250.30 (n/a)</td><td>257.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.22 (+1.14%)</td><td>0.16 <b>(+29.93%)</b></td><td>0.20 <b>(+96.62%)</b></td><td>0.09 (+11.35%)</td><td>0.06 (+18.16%)</td><td>546.00 (-10.20%)</td><td>360.54 (-19.74%)</td><td>250.20 <b>(-49.15%)</b></td><td>227.30 (-1.13%)</td><td>165.38 (+14.37%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>608.00 (n/a)</td><td>449.22 (n/a)</td><td>492.00 (n/a)</td><td>229.90 (n/a)</td><td>144.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (+3.41%)</td><td>0.17 (+5.97%)</td><td>0.20 (+13.10%)</td><td>0.10 (-4.66%)</td><td>0.04 <b>(+24.80%)</b></td><td>488.30 (+4.88%)</td><td>303.10 (-3.36%)</td><td>251.60 (-11.60%)</td><td>241.10 (-3.29%)</td><td>105.57 <b>(+21.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>465.60 (n/a)</td><td>313.64 (n/a)</td><td>284.60 (n/a)</td><td>249.30 (n/a)</td><td>86.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.24 (+5.50%)</td><td>0.20 (+15.78%)</td><td>0.20 (+15.57%)</td><td>0.15 <b>(+37.91%)</b></td><td>0.03 <b>(-26.50%)</b></td><td>331.60 <b>(-27.49%)</b></td><td>254.54 (-16.99%)</td><td>250.00 (-13.46%)</td><td>203.50 (-5.17%)</td><td>47.11 <b>(-49.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>457.30 (n/a)</td><td>306.62 (n/a)</td><td>288.90 (n/a)</td><td>214.60 (n/a)</td><td>93.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.22 <b>(+35.46%)</b></td><td>0.20 <b>(+107.37%)</b></td><td>0.20 <b>(+124.41%)</b></td><td>0.17 <b>(+638.94%)</b></td><td>0.01 <b>(-69.91%)</b></td><td>280.90 <b>(-86.47%)</b></td><td>250.10 <b>(-68.12%)</b></td><td>248.80 <b>(-55.44%)</b></td><td>227.20 <b>(-26.16%)</b></td><td>19.59 <b>(-97.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2075.70 (n/a)</td><td>784.58 (n/a)</td><td>558.40 (n/a)</td><td>307.70 (n/a)</td><td>729.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (+0.31%)</td><td>0.11 (-18.10%)</td><td>0.09 <b>(-21.59%)</b></td><td>0.07 (-9.08%)</td><td>0.05 (-11.00%)</td><td>660.50 (+9.99%)</td><td>488.96 (+19.88%)</td><td>523.00 <b>(+27.53%)</b></td><td>242.50 (-0.33%)</td><td>162.04 (-1.26%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>600.50 (n/a)</td><td>407.88 (n/a)</td><td>410.10 (n/a)</td><td>243.30 (n/a)</td><td>164.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.21 (+6.01%)</td><td>0.18 <b>(+22.96%)</b></td><td>0.20 <b>(+51.91%)</b></td><td>0.12 (+8.19%)</td><td>0.03 (-6.23%)</td><td>398.40 (-7.59%)</td><td>286.88 (-19.61%)</td><td>251.70 <b>(-34.18%)</b></td><td>236.90 (-5.69%)</td><td>66.63 (-19.26%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>431.10 (n/a)</td><td>356.84 (n/a)</td><td>382.40 (n/a)</td><td>251.20 (n/a)</td><td>82.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (+13.10%)</td><td>0.01 (-0.60%)</td><td>0.01 (-6.27%)</td><td>0.01 (-10.60%)</td><td>0.00 <b>(+52.26%)</b></td><td>450.70 (+11.86%)</td><td>306.52 (+4.00%)</td><td>294.60 (+6.70%)</td><td>215.60 (-11.57%)</td><td>90.41 <b>(+45.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>402.90 (n/a)</td><td>294.72 (n/a)</td><td>276.10 (n/a)</td><td>243.80 (n/a)</td><td>62.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-15.32%)</td><td>0.01 (-7.42%)</td><td>0.01 (+19.16%)</td><td>0.00 (-9.81%)</td><td>0.00 <b>(-30.35%)</b></td><td>644.50 (+10.87%)</td><td>431.08 (+2.84%)</td><td>418.40 (-16.09%)</td><td>283.80 (+18.05%)</td><td>147.01 (-7.43%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>581.30 (n/a)</td><td>419.16 (n/a)</td><td>498.60 (n/a)</td><td>240.40 (n/a)</td><td>158.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (+3.49%)</td><td>0.01 (+4.85%)</td><td>0.01 <b>(+23.10%)</b></td><td>0.00 <b>(-43.51%)</b></td><td>0.00 <b>(+83.80%)</b></td><td>652.00 <b>(+77.03%)</b></td><td>340.58 (+7.30%)</td><td>271.60 (-18.78%)</td><td>232.90 (-3.40%)</td><td>176.78 <b>(+221.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>368.30 (n/a)</td><td>317.40 (n/a)</td><td>334.40 (n/a)</td><td>241.10 (n/a)</td><td>54.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-4.42%)</td><td>0.01 (-4.60%)</td><td>0.01 <b>(+33.48%)</b></td><td>0.00 <b>(-25.21%)</b></td><td>0.00 (-4.31%)</td><td>658.80 <b>(+33.71%)</b></td><td>413.10 (+7.33%)</td><td>330.80 <b>(-25.09%)</b></td><td>251.00 (+4.63%)</td><td>166.08 <b>(+35.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.70 (n/a)</td><td>384.90 (n/a)</td><td>441.60 (n/a)</td><td>239.90 (n/a)</td><td>122.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 <b>(-36.76%)</b></td><td>0.01 <b>(-27.48%)</b></td><td>0.01 <b>(-40.64%)</b></td><td>0.01 <b>(+31.92%)</b></td><td>0.00 <b>(-68.21%)</b></td><td>515.50 <b>(-24.20%)</b></td><td>445.58 (+12.61%)</td><td>463.50 <b>(+68.48%)</b></td><td>315.80 <b>(+58.14%)</b></td><td>75.75 <b>(-65.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>680.10 (n/a)</td><td>395.70 (n/a)</td><td>275.10 (n/a)</td><td>199.70 (n/a)</td><td>218.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (+8.39%)</td><td>0.01 (-19.68%)</td><td>0.01 <b>(-34.78%)</b></td><td>0.00 <b>(-22.90%)</b></td><td>0.00 (+12.78%)</td><td>688.70 <b>(+29.72%)</b></td><td>462.82 <b>(+28.49%)</b></td><td>448.90 <b>(+53.37%)</b></td><td>240.30 (-7.72%)</td><td>160.89 <b>(+30.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>530.90 (n/a)</td><td>360.20 (n/a)</td><td>292.70 (n/a)</td><td>260.40 (n/a)</td><td>123.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-6.73%)</td><td>0.02 (-10.09%)</td><td>0.02 (-9.37%)</td><td>0.01 (-13.09%)</td><td>0.01 (-3.00%)</td><td>592.60 (+15.05%)</td><td>390.16 (+13.46%)</td><td>295.80 (+10.33%)</td><td>247.10 (+7.20%)</td><td>165.22 <b>(+22.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>343.88 (n/a)</td><td>268.10 (n/a)</td><td>230.50 (n/a)</td><td>134.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-0.77%)</td><td>0.02 (-3.24%)</td><td>0.02 (-1.58%)</td><td>0.00 <b>(-58.62%)</b></td><td>0.01 (+10.56%)</td><td>1814.50 <b>(+141.68%)</b></td><td>585.30 <b>(+50.48%)</b></td><td>239.10 (+1.61%)</td><td>200.00 (+0.81%)</td><td>693.65 <b>(+185.62%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>750.80 (n/a)</td><td>388.96 (n/a)</td><td>235.30 (n/a)</td><td>198.40 (n/a)</td><td>242.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (+14.64%)</td><td>0.02 (+4.91%)</td><td>0.02 (+10.40%)</td><td>0.01 (-11.83%)</td><td>0.01 <b>(+35.63%)</b></td><td>553.50 (+13.42%)</td><td>344.74 (+1.89%)</td><td>257.60 (-9.42%)</td><td>209.10 (-12.77%)</td><td>156.08 <b>(+37.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>488.00 (n/a)</td><td>338.34 (n/a)</td><td>284.40 (n/a)</td><td>239.70 (n/a)</td><td>113.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+7.99%)</td><td>0.02 (+7.58%)</td><td>0.02 (-1.25%)</td><td>0.01 (+6.81%)</td><td>0.00 (+6.11%)</td><td>533.60 (-6.37%)</td><td>338.78 (-7.22%)</td><td>308.10 (+1.25%)</td><td>239.10 (-7.40%)</td><td>117.00 (-7.55%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.90 (n/a)</td><td>365.16 (n/a)</td><td>304.30 (n/a)</td><td>258.20 (n/a)</td><td>126.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-21.33%)</b></td><td>0.01 <b>(+22.52%)</b></td><td>0.02 <b>(+76.35%)</b></td><td>0.01 <b>(+95.49%)</b></td><td>0.01 <b>(-39.02%)</b></td><td>575.60 <b>(-48.84%)</b></td><td>399.82 <b>(-34.24%)</b></td><td>338.30 <b>(-43.29%)</b></td><td>229.90 <b>(+27.09%)</b></td><td>159.66 <b>(-52.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1125.10 (n/a)</td><td>608.04 (n/a)</td><td>596.50 (n/a)</td><td>180.90 (n/a)</td><td>337.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-7.72%)</td><td>0.01 <b>(-20.13%)</b></td><td>0.01 <b>(-31.12%)</b></td><td>0.01 <b>(-25.53%)</b></td><td>0.00 (-8.12%)</td><td>733.10 <b>(+34.29%)</b></td><td>513.28 <b>(+26.59%)</b></td><td>542.90 <b>(+45.20%)</b></td><td>296.90 (+8.36%)</td><td>167.60 <b>(+26.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.90 (n/a)</td><td>405.48 (n/a)</td><td>373.90 (n/a)</td><td>274.00 (n/a)</td><td>132.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (+6.24%)</td><td>0.03 (-13.23%)</td><td>0.03 (-6.00%)</td><td>0.02 <b>(-47.29%)</b></td><td>0.01 <b>(+278.58%)</b></td><td>607.30 <b>(+89.72%)</b></td><td>372.20 <b>(+27.56%)</b></td><td>313.20 (+6.39%)</td><td>245.00 (-5.88%)</td><td>147.19 <b>(+589.03%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>320.10 (n/a)</td><td>291.78 (n/a)</td><td>294.40 (n/a)</td><td>260.30 (n/a)</td><td>21.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (+9.30%)</td><td>0.03 <b>(+23.39%)</b></td><td>0.02 (-11.87%)</td><td>0.02 <b>(+417.88%)</b></td><td>0.01 (-17.04%)</td><td>470.20 <b>(-80.69%)</b></td><td>369.46 <b>(-53.26%)</b></td><td>462.40 (+13.47%)</td><td>207.40 (-8.51%)</td><td>132.32 <b>(-85.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2435.20 (n/a)</td><td>790.52 (n/a)</td><td>407.50 (n/a)</td><td>226.70 (n/a)</td><td>930.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (-11.32%)</td><td>0.03 (-12.03%)</td><td>0.02 (-15.16%)</td><td>0.02 (-12.68%)</td><td>0.01 (-18.16%)</td><td>624.90 (+14.51%)</td><td>427.42 (+11.63%)</td><td>454.00 (+17.86%)</td><td>260.60 (+12.77%)</td><td>148.84 (+3.99%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.70 (n/a)</td><td>382.88 (n/a)</td><td>385.20 (n/a)</td><td>231.10 (n/a)</td><td>143.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (+3.52%)</td><td>0.03 (+5.46%)</td><td>0.02 <b>(+26.50%)</b></td><td>0.02 (+9.81%)</td><td>0.01 (-7.80%)</td><td>548.40 (-8.92%)</td><td>425.82 (-8.89%)</td><td>451.50 <b>(-20.96%)</b></td><td>231.60 (-3.38%)</td><td>120.05 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.10 (n/a)</td><td>467.36 (n/a)</td><td>571.20 (n/a)</td><td>239.70 (n/a)</td><td>162.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (-11.86%)</td><td>0.02 <b>(-24.58%)</b></td><td>0.02 <b>(-40.30%)</b></td><td>0.02 (-3.21%)</td><td>0.01 <b>(-26.15%)</b></td><td>587.00 (+3.33%)</td><td>468.00 <b>(+25.91%)</b></td><td>498.00 <b>(+67.51%)</b></td><td>262.90 (+13.47%)</td><td>125.59 (-19.14%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>371.70 (n/a)</td><td>297.30 (n/a)</td><td>231.70 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (+19.24%)</td><td>0.03 (-14.58%)</td><td>0.02 <b>(-40.72%)</b></td><td>0.02 (-12.64%)</td><td>0.01 <b>(+63.63%)</b></td><td>575.10 (+14.47%)</td><td>427.04 <b>(+25.45%)</b></td><td>492.30 <b>(+68.65%)</b></td><td>235.20 (-16.15%)</td><td>146.54 <b>(+56.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>340.40 (n/a)</td><td>291.90 (n/a)</td><td>280.50 (n/a)</td><td>93.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (-6.50%)</td><td>0.05 <b>(-27.09%)</b></td><td>0.05 <b>(-28.45%)</b></td><td>0.03 <b>(-45.03%)</b></td><td>0.02 <b>(+63.58%)</b></td><td>670.90 <b>(+81.91%)</b></td><td>462.92 <b>(+54.83%)</b></td><td>421.70 <b>(+39.77%)</b></td><td>248.50 (+6.97%)</td><td>193.06 <b>(+240.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>368.80 (n/a)</td><td>298.98 (n/a)</td><td>301.70 (n/a)</td><td>232.30 (n/a)</td><td>56.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (-9.18%)</td><td>0.06 (-6.61%)</td><td>0.07 (-8.91%)</td><td>0.04 <b>(+29.22%)</b></td><td>0.02 <b>(-31.09%)</b></td><td>497.30 <b>(-22.61%)</b></td><td>372.40 (-1.20%)</td><td>300.10 (+9.81%)</td><td>267.80 (+10.07%)</td><td>114.51 <b>(-35.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.60 (n/a)</td><td>376.92 (n/a)</td><td>273.30 (n/a)</td><td>243.30 (n/a)</td><td>177.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (-3.77%)</td><td>0.06 (-10.80%)</td><td>0.05 <b>(-37.58%)</b></td><td>0.04 (-2.38%)</td><td>0.02 (+12.22%)</td><td>561.40 (+2.43%)</td><td>412.64 (+15.85%)</td><td>465.10 <b>(+60.21%)</b></td><td>231.30 (+3.91%)</td><td>154.92 (+17.13%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>548.10 (n/a)</td><td>356.20 (n/a)</td><td>290.30 (n/a)</td><td>222.60 (n/a)</td><td>132.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (+14.16%)</td><td>0.05 (-5.92%)</td><td>0.04 (-11.51%)</td><td>0.04 (+8.48%)</td><td>0.03 (+13.88%)</td><td>589.30 (-7.81%)</td><td>473.56 (+6.40%)</td><td>547.00 (+13.02%)</td><td>203.20 (-12.41%)</td><td>157.51 (-12.25%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>639.20 (n/a)</td><td>445.06 (n/a)</td><td>484.00 (n/a)</td><td>232.00 (n/a)</td><td>179.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(+33.63%)</b></td><td>0.05 (+12.40%)</td><td>0.04 (-14.68%)</td><td>0.03 <b>(+57.61%)</b></td><td>0.03 <b>(+43.94%)</b></td><td>640.40 <b>(-36.55%)</b></td><td>493.40 (-11.24%)</td><td>576.00 (+17.19%)</td><td>212.50 <b>(-25.15%)</b></td><td>173.74 <b>(-36.32%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1009.30 (n/a)</td><td>555.90 (n/a)</td><td>491.50 (n/a)</td><td>283.90 (n/a)</td><td>272.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(+51.31%)</b></td><td>0.06 <b>(+60.14%)</b></td><td>0.06 <b>(+36.01%)</b></td><td>0.05 <b>(+203.50%)</b></td><td>0.01 <b>(-28.41%)</b></td><td>434.70 <b>(-67.05%)</b></td><td>364.36 <b>(-45.72%)</b></td><td>365.80 <b>(-26.47%)</b></td><td>293.50 <b>(-33.91%)</b></td><td>54.36 <b>(-85.22%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1319.20 (n/a)</td><td>671.22 (n/a)</td><td>497.50 (n/a)</td><td>444.10 (n/a)</td><td>367.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>319.28 (n/a)</td><td>265.30 (n/a)</td><td>237.30 (n/a)</td><td>126.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.50 (n/a)</td><td>404.28 (n/a)</td><td>437.70 (n/a)</td><td>239.30 (n/a)</td><td>127.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1018.10 (n/a)</td><td>514.80 (n/a)</td><td>480.90 (n/a)</td><td>241.40 (n/a)</td><td>318.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>674.70 (n/a)</td><td>451.92 (n/a)</td><td>469.90 (n/a)</td><td>237.10 (n/a)</td><td>202.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>426.12 (n/a)</td><td>382.90 (n/a)</td><td>238.10 (n/a)</td><td>149.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>657.60 (n/a)</td><td>402.58 (n/a)</td><td>294.10 (n/a)</td><td>244.30 (n/a)</td><td>192.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>649.40 (n/a)</td><td>422.42 (n/a)</td><td>445.50 (n/a)</td><td>232.30 (n/a)</td><td>163.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>583.70 (n/a)</td><td>381.46 (n/a)</td><td>284.70 (n/a)</td><td>231.20 (n/a)</td><td>173.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>598.70 (n/a)</td><td>388.60 (n/a)</td><td>276.20 (n/a)</td><td>248.80 (n/a)</td><td>171.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (-3.01%)</td><td>0.17 (-1.17%)</td><td>0.19 (+0.63%)</td><td>0.10 (-5.28%)</td><td>0.04 (-0.38%)</td><td>477.30 (+5.57%)</td><td>304.62 (+1.74%)</td><td>260.20 (-0.61%)</td><td>249.40 (+3.10%)</td><td>97.10 (+10.23%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>452.10 (n/a)</td><td>299.40 (n/a)</td><td>261.80 (n/a)</td><td>241.90 (n/a)</td><td>88.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>506.80 (n/a)</td><td>342.74 (n/a)</td><td>252.70 (n/a)</td><td>218.60 (n/a)</td><td>140.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>721.30 (n/a)</td><td>378.90 (n/a)</td><td>295.20 (n/a)</td><td>237.80 (n/a)</td><td>195.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>400.96 (n/a)</td><td>392.80 (n/a)</td><td>259.30 (n/a)</td><td>146.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.50 (n/a)</td><td>404.96 (n/a)</td><td>407.70 (n/a)</td><td>272.20 (n/a)</td><td>85.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1053.10 (n/a)</td><td>501.12 (n/a)</td><td>462.40 (n/a)</td><td>217.70 (n/a)</td><td>329.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>621.70 (n/a)</td><td>403.58 (n/a)</td><td>455.60 (n/a)</td><td>223.30 (n/a)</td><td>163.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.60 (n/a)</td><td>362.08 (n/a)</td><td>332.30 (n/a)</td><td>244.80 (n/a)</td><td>97.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>518.30 (n/a)</td><td>449.18 (n/a)</td><td>435.00 (n/a)</td><td>371.70 (n/a)</td><td>56.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>518.80 (n/a)</td><td>393.46 (n/a)</td><td>408.80 (n/a)</td><td>265.30 (n/a)</td><td>97.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>469.90 (n/a)</td><td>353.38 (n/a)</td><td>351.10 (n/a)</td><td>238.70 (n/a)</td><td>87.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>619.90 (n/a)</td><td>432.30 (n/a)</td><td>462.30 (n/a)</td><td>250.20 (n/a)</td><td>138.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>519.80 (n/a)</td><td>376.84 (n/a)</td><td>433.00 (n/a)</td><td>200.70 (n/a)</td><td>128.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>606.80 (n/a)</td><td>451.02 (n/a)</td><td>547.20 (n/a)</td><td>210.40 (n/a)</td><td>175.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.55 (-18.87%)</td><td>3.02 (-4.40%)</td><td>3.34 (+17.88%)</td><td>2.35 (-7.89%)</td><td>0.54 <b>(-30.42%)</b></td><td>4464.30 (+8.57%)</td><td>3565.86 (+3.01%)</td><td>3140.10 (-15.17%)</td><td>2951.10 <b>(+23.25%)</b></td><td>687.24 (-8.32%)</td><td>1455.37 (-18.87%)</td><td>1238.75 (-4.40%)</td><td>1367.77 (+17.88%)</td><td>962.07 (-7.89%)</td><td>222.89 <b>(-30.42%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.38 (n/a)</td><td>3.16 (n/a)</td><td>2.83 (n/a)</td><td>2.55 (n/a)</td><td>0.78 (n/a)</td><td>4111.90 (n/a)</td><td>3461.52 (n/a)</td><td>3701.60 (n/a)</td><td>2394.40 (n/a)</td><td>749.60 (n/a)</td><td>1793.79 (n/a)</td><td>1295.74 (n/a)</td><td>1160.31 (n/a)</td><td>1044.52 (n/a)</td><td>320.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.55 (+0.27%)</td><td>3.29 (-0.73%)</td><td>3.44 (+4.87%)</td><td>2.95 (-6.11%)</td><td>0.29 <b>(+80.12%)</b></td><td>7988.10 (+6.51%)</td><td>7206.94 (+1.19%)</td><td>6865.10 (-4.64%)</td><td>6637.00 (-0.27%)</td><td>655.04 <b>(+92.08%)</b></td><td>2022.26 (+0.27%)</td><td>1874.36 (-0.73%)</td><td>1955.07 (+4.87%)</td><td>1680.22 (-6.11%)</td><td>165.41 <b>(+80.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.55 (n/a)</td><td>3.32 (n/a)</td><td>3.28 (n/a)</td><td>3.15 (n/a)</td><td>0.16 (n/a)</td><td>7499.70 (n/a)</td><td>7121.84 (n/a)</td><td>7199.50 (n/a)</td><td>6654.70 (n/a)</td><td>341.02 (n/a)</td><td>2016.89 (n/a)</td><td>1888.11 (n/a)</td><td>1864.26 (n/a)</td><td>1789.63 (n/a)</td><td>91.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.14 (+7.50%)</td><td>3.63 (+2.71%)</td><td>3.69 (+4.23%)</td><td>2.84 (-11.35%)</td><td>0.48 <b>(+72.56%)</b></td><td>5902.40 (+12.80%)</td><td>4697.04 (-1.57%)</td><td>4542.70 (-4.06%)</td><td>4051.40 (-6.98%)</td><td>706.46 <b>(+87.00%)</b></td><td>2120.24 (+7.50%)</td><td>1858.21 (+2.71%)</td><td>1890.95 (+4.23%)</td><td>1455.34 (-11.35%)</td><td>245.77 <b>(+72.56%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.85 (n/a)</td><td>3.53 (n/a)</td><td>3.54 (n/a)</td><td>3.21 (n/a)</td><td>0.28 (n/a)</td><td>5232.60 (n/a)</td><td>4771.98 (n/a)</td><td>4734.90 (n/a)</td><td>4355.30 (n/a)</td><td>377.78 (n/a)</td><td>1972.28 (n/a)</td><td>1809.09 (n/a)</td><td>1814.18 (n/a)</td><td>1641.62 (n/a)</td><td>142.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.98 <b>(-22.49%)</b></td><td>0.81 (+0.68%)</td><td>0.80 (+11.31%)</td><td>0.62 <b>(+44.69%)</b></td><td>0.14 <b>(-56.19%)</b></td><td>743.40 <b>(-30.89%)</b></td><td>583.54 (-10.56%)</td><td>571.70 (-10.17%)</td><td>466.00 <b>(+29.01%)</b></td><td>105.39 <b>(-60.82%)</b></td><td>72.01 <b>(-22.49%)</b></td><td>58.95 (+0.68%)</td><td>58.69 (+11.31%)</td><td>45.14 <b>(+44.69%)</b></td><td>10.13 <b>(-56.19%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.27 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>1075.60 (n/a)</td><td>652.46 (n/a)</td><td>636.40 (n/a)</td><td>361.20 (n/a)</td><td>269.02 (n/a)</td><td>92.90 (n/a)</td><td>58.55 (n/a)</td><td>52.72 (n/a)</td><td>31.20 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.03 <b>(+76.61%)</b></td><td>1.08 <b>(+34.21%)</b></td><td>0.88 (-8.76%)</td><td>0.40 <b>(+108.86%)</b></td><td>0.72 <b>(+92.49%)</b></td><td>1642.20 <b>(-52.12%)</b></td><td>900.66 <b>(-27.75%)</b></td><td>740.50 (+9.59%)</td><td>322.60 <b>(-43.37%)</b></td><td>591.68 <b>(-51.75%)</b></td><td>208.05 <b>(+76.61%)</b></td><td>110.78 <b>(+34.21%)</b></td><td>90.62 (-8.76%)</td><td>40.87 <b>(+108.86%)</b></td><td>73.75 <b>(+92.49%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.15 (n/a)</td><td>0.81 (n/a)</td><td>0.97 (n/a)</td><td>0.19 (n/a)</td><td>0.37 (n/a)</td><td>3429.90 (n/a)</td><td>1246.54 (n/a)</td><td>675.70 (n/a)</td><td>569.70 (n/a)</td><td>1226.17 (n/a)</td><td>117.80 (n/a)</td><td>82.54 (n/a)</td><td>99.32 (n/a)</td><td>19.57 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.80 <b>(+49.12%)</b></td><td>1.25 <b>(+25.58%)</b></td><td>1.39 <b>(+36.56%)</b></td><td>0.21 <b>(-71.14%)</b></td><td>0.61 <b>(+215.18%)</b></td><td>3527.20 <b>(+246.52%)</b></td><td>1112.18 <b>(+41.82%)</b></td><td>543.50 <b>(-26.77%)</b></td><td>418.20 <b>(-32.94%)</b></td><td>1351.38 <b>(+734.00%)</b></td><td>200.60 <b>(+49.12%)</b></td><td>138.75 <b>(+25.58%)</b></td><td>154.36 <b>(+36.56%)</b></td><td>23.78 <b>(-71.14%)</b></td><td>67.65 <b>(+215.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.21 (n/a)</td><td>0.99 (n/a)</td><td>1.02 (n/a)</td><td>0.74 (n/a)</td><td>0.19 (n/a)</td><td>1017.90 (n/a)</td><td>784.20 (n/a)</td><td>742.20 (n/a)</td><td>623.60 (n/a)</td><td>162.04 (n/a)</td><td>134.53 (n/a)</td><td>110.49 (n/a)</td><td>113.03 (n/a)</td><td>82.41 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.73 (-10.34%)</td><td>1.25 (-8.34%)</td><td>1.00 (-17.15%)</td><td>0.89 (+1.12%)</td><td>0.39 (-2.95%)</td><td>1173.60 (-1.10%)</td><td>906.36 (+9.49%)</td><td>1047.00 <b>(+20.71%)</b></td><td>605.20 (+11.54%)</td><td>258.49 (+5.50%)</td><td>221.77 (-10.34%)</td><td>159.45 (-8.34%)</td><td>128.19 (-17.15%)</td><td>114.36 (+1.12%)</td><td>50.07 (-2.95%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.93 (n/a)</td><td>1.36 (n/a)</td><td>1.21 (n/a)</td><td>0.88 (n/a)</td><td>0.40 (n/a)</td><td>1186.70 (n/a)</td><td>827.82 (n/a)</td><td>867.40 (n/a)</td><td>542.60 (n/a)</td><td>245.02 (n/a)</td><td>247.35 (n/a)</td><td>173.97 (n/a)</td><td>154.73 (n/a)</td><td>113.10 (n/a)</td><td>51.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.65 (+6.66%)</td><td>1.64 (-5.03%)</td><td>1.43 (-4.05%)</td><td>1.05 <b>(-21.94%)</b></td><td>0.62 <b>(+26.72%)</b></td><td>997.80 <b>(+28.10%)</b></td><td>705.08 (+9.69%)</td><td>732.90 (+4.22%)</td><td>395.40 (-6.24%)</td><td>224.68 <b>(+43.97%)</b></td><td>339.45 (+6.66%)</td><td>209.71 (-5.03%)</td><td>183.12 (-4.05%)</td><td>134.51 <b>(-21.94%)</b></td><td>79.23 <b>(+26.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.49 (n/a)</td><td>1.73 (n/a)</td><td>1.49 (n/a)</td><td>1.35 (n/a)</td><td>0.49 (n/a)</td><td>778.90 (n/a)</td><td>642.78 (n/a)</td><td>703.20 (n/a)</td><td>421.70 (n/a)</td><td>156.06 (n/a)</td><td>318.25 (n/a)</td><td>220.81 (n/a)</td><td>190.86 (n/a)</td><td>172.31 (n/a)</td><td>62.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.40 <b>(+20.27%)</b></td><td>1.94 <b>(+22.88%)</b></td><td>2.20 <b>(+31.87%)</b></td><td>1.36 <b>(+28.79%)</b></td><td>0.48 (+9.46%)</td><td>768.30 <b>(-22.35%)</b></td><td>571.12 (-19.68%)</td><td>477.20 <b>(-24.16%)</b></td><td>436.70 (-16.87%)</td><td>154.16 <b>(-27.39%)</b></td><td>307.32 <b>(+20.27%)</b></td><td>248.17 <b>(+22.88%)</b></td><td>281.28 <b>(+31.87%)</b></td><td>174.70 <b>(+28.79%)</b></td><td>61.12 (+9.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.00 (n/a)</td><td>1.58 (n/a)</td><td>1.67 (n/a)</td><td>1.06 (n/a)</td><td>0.44 (n/a)</td><td>989.50 (n/a)</td><td>711.10 (n/a)</td><td>629.20 (n/a)</td><td>525.30 (n/a)</td><td>212.30 (n/a)</td><td>255.53 (n/a)</td><td>201.97 (n/a)</td><td>213.30 (n/a)</td><td>135.65 (n/a)</td><td>55.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.11 <b>(+27.38%)</b></td><td>1.46 (+18.11%)</td><td>1.45 <b>(+20.92%)</b></td><td>0.99 (+6.29%)</td><td>0.42 <b>(+44.71%)</b></td><td>1063.20 (-5.92%)</td><td>765.08 (-13.59%)</td><td>723.60 (-17.29%)</td><td>495.90 <b>(-21.50%)</b></td><td>209.17 (+5.64%)</td><td>270.64 <b>(+27.38%)</b></td><td>186.77 (+18.11%)</td><td>185.49 <b>(+20.92%)</b></td><td>126.24 (+6.29%)</td><td>53.76 <b>(+44.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.66 (n/a)</td><td>1.24 (n/a)</td><td>1.20 (n/a)</td><td>0.93 (n/a)</td><td>0.29 (n/a)</td><td>1130.10 (n/a)</td><td>885.36 (n/a)</td><td>874.90 (n/a)</td><td>631.70 (n/a)</td><td>198.00 (n/a)</td><td>212.46 (n/a)</td><td>158.14 (n/a)</td><td>153.40 (n/a)</td><td>118.77 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.76 (+8.33%)</td><td>1.13 (-12.16%)</td><td>1.22 (-0.96%)</td><td>0.45 <b>(-58.54%)</b></td><td>0.60 <b>(+188.69%)</b></td><td>2335.10 <b>(+141.23%)</b></td><td>1258.88 <b>(+51.10%)</b></td><td>861.00 (+0.96%)</td><td>595.00 (-7.68%)</td><td>792.04 <b>(+550.97%)</b></td><td>225.59 (+8.33%)</td><td>144.22 (-12.16%)</td><td>155.88 (-0.96%)</td><td>57.48 <b>(-58.54%)</b></td><td>77.22 <b>(+188.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.63 (n/a)</td><td>1.28 (n/a)</td><td>1.23 (n/a)</td><td>1.08 (n/a)</td><td>0.21 (n/a)</td><td>968.00 (n/a)</td><td>833.14 (n/a)</td><td>852.80 (n/a)</td><td>644.50 (n/a)</td><td>121.67 (n/a)</td><td>208.24 (n/a)</td><td>164.20 (n/a)</td><td>157.39 (n/a)</td><td>138.65 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.80 <b>(-24.97%)</b></td><td>1.65 (+3.11%)</td><td>1.67 <b>(+26.78%)</b></td><td>1.47 <b>(+23.66%)</b></td><td>0.13 <b>(-73.69%)</b></td><td>715.60 (-19.14%)</td><td>640.18 (-9.06%)</td><td>627.60 <b>(-21.13%)</b></td><td>581.90 <b>(+33.28%)</b></td><td>53.46 <b>(-71.61%)</b></td><td>230.65 <b>(-24.97%)</b></td><td>210.80 (+3.11%)</td><td>213.86 <b>(+26.78%)</b></td><td>187.55 <b>(+23.66%)</b></td><td>17.19 <b>(-73.69%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.40 (n/a)</td><td>1.60 (n/a)</td><td>1.32 (n/a)</td><td>1.18 (n/a)</td><td>0.51 (n/a)</td><td>885.00 (n/a)</td><td>703.96 (n/a)</td><td>795.70 (n/a)</td><td>436.60 (n/a)</td><td>188.28 (n/a)</td><td>307.41 (n/a)</td><td>204.44 (n/a)</td><td>168.68 (n/a)</td><td>151.66 (n/a)</td><td>65.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.85 (-13.72%)</td><td>0.58 (-17.50%)</td><td>0.56 <b>(-23.28%)</b></td><td>0.18 <b>(-54.00%)</b></td><td>0.28 (+16.10%)</td><td>1981.70 <b>(+117.41%)</b></td><td>850.40 <b>(+48.55%)</b></td><td>640.40 <b>(+30.35%)</b></td><td>423.40 (+15.90%)</td><td>649.73 <b>(+190.55%)</b></td><td>39.62 (-13.72%)</td><td>26.98 (-17.50%)</td><td>26.20 <b>(-23.28%)</b></td><td>8.47 <b>(-54.00%)</b></td><td>13.01 (+16.10%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.99 (n/a)</td><td>0.70 (n/a)</td><td>0.73 (n/a)</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>911.50 (n/a)</td><td>572.48 (n/a)</td><td>491.30 (n/a)</td><td>365.30 (n/a)</td><td>223.62 (n/a)</td><td>45.92 (n/a)</td><td>32.71 (n/a)</td><td>34.15 (n/a)</td><td>18.41 (n/a)</td><td>11.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.18 (+11.44%)</td><td>2.81 <b>(+42.19%)</b></td><td>3.05 <b>(+66.44%)</b></td><td>1.72 <b>(+53.59%)</b></td><td>0.61 (-16.46%)</td><td>2436.70 <b>(-34.89%)</b></td><td>1577.40 <b>(-34.05%)</b></td><td>1375.00 <b>(-39.92%)</b></td><td>1320.30 (-10.26%)</td><td>481.50 <b>(-48.40%)</b></td><td>813.24 (+11.44%)</td><td>718.91 <b>(+42.19%)</b></td><td>780.88 <b>(+66.44%)</b></td><td>440.66 <b>(+53.59%)</b></td><td>156.71 (-16.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.85 (n/a)</td><td>1.97 (n/a)</td><td>1.83 (n/a)</td><td>1.12 (n/a)</td><td>0.73 (n/a)</td><td>3742.60 (n/a)</td><td>2391.86 (n/a)</td><td>2288.60 (n/a)</td><td>1471.30 (n/a)</td><td>933.23 (n/a)</td><td>729.77 (n/a)</td><td>505.59 (n/a)</td><td>469.16 (n/a)</td><td>286.90 (n/a)</td><td>187.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.43 (-3.93%)</td><td>1.71 <b>(-24.62%)</b></td><td>1.08 <b>(-50.06%)</b></td><td>0.71 <b>(-37.13%)</b></td><td>1.23 <b>(+34.76%)</b></td><td>3690.10 <b>(+59.06%)</b></td><td>2295.62 <b>(+71.26%)</b></td><td>2416.80 <b>(+100.23%)</b></td><td>764.10 (+4.09%)</td><td>1379.05 <b>(+127.27%)</b></td><td>702.65 (-3.93%)</td><td>349.39 <b>(-24.62%)</b></td><td>222.14 <b>(-50.06%)</b></td><td>145.49 <b>(-37.13%)</b></td><td>252.01 <b>(+34.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.57 (n/a)</td><td>2.26 (n/a)</td><td>2.17 (n/a)</td><td>1.13 (n/a)</td><td>0.91 (n/a)</td><td>2319.90 (n/a)</td><td>1340.44 (n/a)</td><td>1207.00 (n/a)</td><td>734.10 (n/a)</td><td>606.79 (n/a)</td><td>731.36 (n/a)</td><td>463.52 (n/a)</td><td>444.82 (n/a)</td><td>231.42 (n/a)</td><td>187.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.70 (-2.18%)</td><td>2.99 (-10.65%)</td><td>3.30 (+0.49%)</td><td>1.93 <b>(-32.90%)</b></td><td>0.82 <b>(+140.88%)</b></td><td>4078.60 <b>(+49.03%)</b></td><td>2821.82 (+18.99%)</td><td>2380.40 (-0.48%)</td><td>2123.90 (+2.22%)</td><td>875.67 <b>(+255.56%)</b></td><td>1137.47 (-2.18%)</td><td>918.00 (-10.65%)</td><td>1014.91 (+0.49%)</td><td>592.33 <b>(-32.90%)</b></td><td>251.36 <b>(+140.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.79 (n/a)</td><td>3.34 (n/a)</td><td>3.29 (n/a)</td><td>2.87 (n/a)</td><td>0.34 (n/a)</td><td>2736.70 (n/a)</td><td>2371.46 (n/a)</td><td>2392.00 (n/a)</td><td>2077.70 (n/a)</td><td>246.28 (n/a)</td><td>1162.81 (n/a)</td><td>1027.39 (n/a)</td><td>1009.99 (n/a)</td><td>882.79 (n/a)</td><td>104.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.80 (n/a)</td><td>307.36 (n/a)</td><td>290.00 (n/a)</td><td>211.10 (n/a)</td><td>95.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.10 (n/a)</td><td>418.14 (n/a)</td><td>472.90 (n/a)</td><td>235.10 (n/a)</td><td>148.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1853.20 (n/a)</td><td>641.82 (n/a)</td><td>279.80 (n/a)</td><td>242.30 (n/a)</td><td>691.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.80 (n/a)</td><td>357.70 (n/a)</td><td>262.80 (n/a)</td><td>253.70 (n/a)</td><td>136.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.90 (n/a)</td><td>434.92 (n/a)</td><td>514.60 (n/a)</td><td>198.90 (n/a)</td><td>202.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>683.50 (n/a)</td><td>442.46 (n/a)</td><td>319.00 (n/a)</td><td>240.50 (n/a)</td><td>216.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>308.70 (n/a)</td><td>276.88 (n/a)</td><td>263.70 (n/a)</td><td>255.30 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.60 (n/a)</td><td>348.44 (n/a)</td><td>361.00 (n/a)</td><td>230.30 (n/a)</td><td>111.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.90 (n/a)</td><td>343.96 (n/a)</td><td>252.50 (n/a)</td><td>220.60 (n/a)</td><td>145.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.40 (n/a)</td><td>366.68 (n/a)</td><td>317.10 (n/a)</td><td>243.90 (n/a)</td><td>128.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.20 (n/a)</td><td>308.94 (n/a)</td><td>289.90 (n/a)</td><td>224.50 (n/a)</td><td>100.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.20 (n/a)</td><td>464.08 (n/a)</td><td>503.90 (n/a)</td><td>203.60 (n/a)</td><td>163.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.60 (n/a)</td><td>337.96 (n/a)</td><td>284.70 (n/a)</td><td>246.40 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>555.20 (n/a)</td><td>367.16 (n/a)</td><td>298.60 (n/a)</td><td>230.90 (n/a)</td><td>149.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>474.50 (n/a)</td><td>324.62 (n/a)</td><td>259.30 (n/a)</td><td>225.40 (n/a)</td><td>111.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1003.30 (n/a)</td><td>512.90 (n/a)</td><td>442.30 (n/a)</td><td>277.80 (n/a)</td><td>297.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.10 (n/a)</td><td>437.96 (n/a)</td><td>419.60 (n/a)</td><td>308.80 (n/a)</td><td>94.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1934.30 (n/a)</td><td>739.78 (n/a)</td><td>523.70 (n/a)</td><td>304.30 (n/a)</td><td>676.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>579.10 (n/a)</td><td>408.86 (n/a)</td><td>435.00 (n/a)</td><td>268.40 (n/a)</td><td>134.37 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>550.10 (n/a)</td><td>336.64 (n/a)</td><td>302.00 (n/a)</td><td>251.10 (n/a)</td><td>121.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2486.40 (n/a)</td><td>763.76 (n/a)</td><td>301.40 (n/a)</td><td>228.70 (n/a)</td><td>970.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>586.70 (n/a)</td><td>459.22 (n/a)</td><td>502.20 (n/a)</td><td>233.00 (n/a)</td><td>142.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>565.80 (n/a)</td><td>478.22 (n/a)</td><td>513.80 (n/a)</td><td>335.40 (n/a)</td><td>93.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>630.30 (n/a)</td><td>425.38 (n/a)</td><td>420.20 (n/a)</td><td>288.00 (n/a)</td><td>141.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.64 (+1.82%)</td><td>0.43 <b>(-25.11%)</b></td><td>0.46 <b>(-26.66%)</b></td><td>0.15 <b>(-68.17%)</b></td><td>0.18 <b>(+134.59%)</b></td><td>1517.10 <b>(+214.16%)</b></td><td>663.50 <b>(+70.13%)</b></td><td>480.80 <b>(+36.36%)</b></td><td>345.40 (-1.76%)</td><td>481.39 <b>(+734.02%)</b></td><td>27.33 (+1.82%)</td><td>18.41 <b>(-25.11%)</b></td><td>19.63 <b>(-26.66%)</b></td><td>6.22 <b>(-68.17%)</b></td><td>7.65 <b>(+134.59%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.63 (n/a)</td><td>0.58 (n/a)</td><td>0.63 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>482.90 (n/a)</td><td>390.00 (n/a)</td><td>352.60 (n/a)</td><td>351.60 (n/a)</td><td>57.72 (n/a)</td><td>26.84 (n/a)</td><td>24.58 (n/a)</td><td>26.77 (n/a)</td><td>19.54 (n/a)</td><td>3.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.44 (-16.64%)</td><td>0.31 <b>(-34.08%)</b></td><td>0.28 <b>(-43.92%)</b></td><td>0.22 <b>(-43.31%)</b></td><td>0.10 <b>(+52.12%)</b></td><td>987.20 <b>(+76.38%)</b></td><td>774.16 <b>(+60.67%)</b></td><td>794.70 <b>(+78.30%)</b></td><td>500.40 (+19.97%)</td><td>221.28 <b>(+227.79%)</b></td><td>18.86 (-16.64%)</td><td>13.11 <b>(-34.08%)</b></td><td>11.87 <b>(-43.92%)</b></td><td>9.56 <b>(-43.31%)</b></td><td>4.08 <b>(+52.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>559.70 (n/a)</td><td>481.82 (n/a)</td><td>445.70 (n/a)</td><td>417.10 (n/a)</td><td>67.51 (n/a)</td><td>22.62 (n/a)</td><td>19.89 (n/a)</td><td>21.17 (n/a)</td><td>16.86 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (+0.52%)</td><td>0.31 (+0.42%)</td><td>0.31 (-0.30%)</td><td>0.30 (+2.51%)</td><td>0.00 <b>(-41.80%)</b></td><td>83760.40 (-2.45%)</td><td>82097.74 (-0.44%)</td><td>81809.70 (+0.30%)</td><td>80861.30 (-0.51%)</td><td>1098.36 <b>(-43.52%)</b></td><td>212.46 (+0.52%)</td><td>209.29 (+0.42%)</td><td>210.00 (-0.30%)</td><td>205.11 (+2.51%)</td><td>2.78 <b>(-41.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85862.70 (n/a)</td><td>82463.70 (n/a)</td><td>81566.50 (n/a)</td><td>81278.70 (n/a)</td><td>1944.66 (n/a)</td><td>211.37 (n/a)</td><td>208.42 (n/a)</td><td>210.62 (n/a)</td><td>200.09 (n/a)</td><td>4.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.15 (+0.06%)</td><td>1.14 (+0.79%)</td><td>1.14 (+0.82%)</td><td>1.11 (+1.78%)</td><td>0.02 <b>(-32.34%)</b></td><td>22656.20 (-1.75%)</td><td>22117.40 (-0.80%)</td><td>21984.20 (-0.82%)</td><td>21890.90 (-0.06%)</td><td>308.68 <b>(-33.50%)</b></td><td>784.79 (+0.06%)</td><td>776.88 (+0.79%)</td><td>781.46 (+0.82%)</td><td>758.29 (+1.78%)</td><td>10.67 <b>(-32.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.09 (n/a)</td><td>0.02 (n/a)</td><td>23060.40 (n/a)</td><td>22296.34 (n/a)</td><td>22165.00 (n/a)</td><td>21905.00 (n/a)</td><td>464.20 (n/a)</td><td>784.29 (n/a)</td><td>770.79 (n/a)</td><td>775.09 (n/a)</td><td>744.99 (n/a)</td><td>15.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.80 (+0.23%)</td><td>0.80 (+0.67%)</td><td>0.80 (+0.82%)</td><td>0.79 (+0.68%)</td><td>0.01 (-17.21%)</td><td>95598.70 (-0.67%)</td><td>94539.66 (-0.66%)</td><td>94335.40 (-0.81%)</td><td>93897.90 (-0.23%)</td><td>642.97 (-17.86%)</td><td>731.85 (+0.23%)</td><td>726.91 (+0.67%)</td><td>728.46 (+0.82%)</td><td>718.83 (+0.68%)</td><td>4.92 (-17.21%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96247.70 (n/a)</td><td>95171.90 (n/a)</td><td>95109.90 (n/a)</td><td>94112.60 (n/a)</td><td>782.82 (n/a)</td><td>730.18 (n/a)</td><td>722.10 (n/a)</td><td>722.53 (n/a)</td><td>713.99 (n/a)</td><td>5.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (-0.04%)</td><td>0.77 (+0.70%)</td><td>0.78 (+1.52%)</td><td>0.75 (-0.49%)</td><td>0.01 (-0.94%)</td><td>100361.50 (+0.49%)</td><td>97738.32 (-0.69%)</td><td>97350.80 (-1.50%)</td><td>96510.70 (+0.04%)</td><td>1524.57 (-0.22%)</td><td>712.04 (-0.04%)</td><td>703.23 (+0.70%)</td><td>705.90 (+1.52%)</td><td>684.72 (-0.49%)</td><td>10.79 (-0.94%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99868.70 (n/a)</td><td>98421.68 (n/a)</td><td>98835.40 (n/a)</td><td>96468.70 (n/a)</td><td>1528.01 (n/a)</td><td>712.35 (n/a)</td><td>698.35 (n/a)</td><td>695.29 (n/a)</td><td>688.10 (n/a)</td><td>10.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.88 (-1.81%)</td><td>0.87 (-1.79%)</td><td>0.88 (-1.78%)</td><td>0.86 (-2.03%)</td><td>0.01 (+7.00%)</td><td>87657.60 (+2.08%)</td><td>86293.14 (+1.82%)</td><td>85934.40 (+1.81%)</td><td>85710.20 (+1.84%)</td><td>793.53 (+11.36%)</td><td>801.77 (-1.81%)</td><td>796.40 (-1.79%)</td><td>799.67 (-1.78%)</td><td>783.95 (-2.03%)</td><td>7.25 (+7.00%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85874.30 (n/a)</td><td>84749.44 (n/a)</td><td>84406.40 (n/a)</td><td>84160.30 (n/a)</td><td>712.58 (n/a)</td><td>816.53 (n/a)</td><td>810.90 (n/a)</td><td>814.15 (n/a)</td><td>800.23 (n/a)</td><td>6.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.25 <b>(+28.16%)</b></td><td>3.30 (+7.62%)</td><td>2.45 (-13.33%)</td><td>2.19 (+2.37%)</td><td>1.41 <b>(+47.37%)</b></td><td>4063.10 (-2.31%)</td><td>3081.10 (-1.99%)</td><td>3630.50 (+15.38%)</td><td>1698.70 <b>(-21.97%)</b></td><td>1119.88 (+17.45%)</td><td>316.05 <b>(+28.16%)</b></td><td>198.67 (+7.62%)</td><td>147.88 (-13.33%)</td><td>132.13 (+2.37%)</td><td>84.80 <b>(+47.37%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.09 (n/a)</td><td>3.06 (n/a)</td><td>2.83 (n/a)</td><td>2.14 (n/a)</td><td>0.96 (n/a)</td><td>4159.20 (n/a)</td><td>3143.68 (n/a)</td><td>3146.60 (n/a)</td><td>2177.10 (n/a)</td><td>953.47 (n/a)</td><td>246.60 (n/a)</td><td>184.61 (n/a)</td><td>170.62 (n/a)</td><td>129.08 (n/a)</td><td>57.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.57 (-0.03%)</td><td>4.09 <b>(+36.89%)</b></td><td>4.25 <b>(+56.74%)</b></td><td>2.84 <b>(+30.76%)</b></td><td>0.72 <b>(-26.50%)</b></td><td>3137.60 <b>(-23.53%)</b></td><td>2249.80 <b>(-29.88%)</b></td><td>2098.60 <b>(-36.20%)</b></td><td>1948.60 (+0.04%)</td><td>502.49 <b>(-42.84%)</b></td><td>275.52 (-0.03%)</td><td>246.34 <b>(+36.89%)</b></td><td>255.82 <b>(+56.74%)</b></td><td>171.11 <b>(+30.76%)</b></td><td>43.29 <b>(-26.50%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.58 (n/a)</td><td>2.99 (n/a)</td><td>2.71 (n/a)</td><td>2.17 (n/a)</td><td>0.98 (n/a)</td><td>4102.80 (n/a)</td><td>3208.36 (n/a)</td><td>3289.30 (n/a)</td><td>1947.90 (n/a)</td><td>879.13 (n/a)</td><td>275.61 (n/a)</td><td>179.95 (n/a)</td><td>163.22 (n/a)</td><td>130.86 (n/a)</td><td>58.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.55 <b>(-22.35%)</b></td><td>2.93 <b>(-25.91%)</b></td><td>2.23 <b>(-35.58%)</b></td><td>2.17 (-1.49%)</td><td>1.07 <b>(-33.42%)</b></td><td>4102.70 (+1.51%)</td><td>3332.40 <b>(+28.93%)</b></td><td>3996.80 <b>(+55.23%)</b></td><td>1957.90 <b>(+28.78%)</b></td><td>1011.25 (-4.08%)</td><td>274.20 <b>(-22.35%)</b></td><td>176.58 <b>(-25.91%)</b></td><td>134.33 <b>(-35.58%)</b></td><td>130.86 (-1.49%)</td><td>64.43 <b>(-33.42%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.86 (n/a)</td><td>3.96 (n/a)</td><td>3.46 (n/a)</td><td>2.21 (n/a)</td><td>1.61 (n/a)</td><td>4041.70 (n/a)</td><td>2584.74 (n/a)</td><td>2574.80 (n/a)</td><td>1520.30 (n/a)</td><td>1054.29 (n/a)</td><td>353.14 (n/a)</td><td>238.31 (n/a)</td><td>208.51 (n/a)</td><td>132.83 (n/a)</td><td>96.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.17 (-9.40%)</td><td>5.56 (-5.13%)</td><td>5.82 (+1.26%)</td><td>4.81 (-7.03%)</td><td>0.62 (+0.86%)</td><td>7245.40 (+7.56%)</td><td>6339.30 (+5.61%)</td><td>5990.90 (-1.24%)</td><td>5648.10 (+10.38%)</td><td>736.38 <b>(+21.58%)</b></td><td>380.22 (-9.40%)</td><td>342.32 (-5.13%)</td><td>358.46 (+1.26%)</td><td>296.39 (-7.03%)</td><td>38.41 (+0.86%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.81 (n/a)</td><td>5.86 (n/a)</td><td>5.75 (n/a)</td><td>5.18 (n/a)</td><td>0.62 (n/a)</td><td>6736.30 (n/a)</td><td>6002.66 (n/a)</td><td>6066.40 (n/a)</td><td>5116.90 (n/a)</td><td>605.68 (n/a)</td><td>419.69 (n/a)</td><td>360.82 (n/a)</td><td>354.00 (n/a)</td><td>318.79 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.82 (+1.05%)</td><td>4.73 (+4.19%)</td><td>5.05 (+4.70%)</td><td>3.49 (-1.77%)</td><td>0.90 (-5.40%)</td><td>9982.90 (+1.80%)</td><td>7603.34 (-4.47%)</td><td>6906.30 (-4.49%)</td><td>5989.90 (-1.04%)</td><td>1570.90 (-7.68%)</td><td>358.52 (+1.05%)</td><td>291.53 (+4.19%)</td><td>310.95 (+4.70%)</td><td>215.12 (-1.77%)</td><td>55.58 (-5.40%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.76 (n/a)</td><td>4.54 (n/a)</td><td>4.82 (n/a)</td><td>3.56 (n/a)</td><td>0.95 (n/a)</td><td>9806.00 (n/a)</td><td>7958.94 (n/a)</td><td>7231.00 (n/a)</td><td>6052.70 (n/a)</td><td>1701.58 (n/a)</td><td>354.80 (n/a)</td><td>279.80 (n/a)</td><td>296.98 (n/a)</td><td>219.00 (n/a)</td><td>58.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.11 (-0.60%)</td><td>5.03 (-9.08%)</td><td>4.30 (-14.65%)</td><td>4.01 (-7.58%)</td><td>1.29 (-4.01%)</td><td>8686.60 (+8.21%)</td><td>7251.10 (+9.95%)</td><td>8116.20 (+17.16%)</td><td>4907.10 (+0.61%)</td><td>1578.13 (+3.84%)</td><td>437.63 (-0.60%)</td><td>309.88 (-9.08%)</td><td>264.59 (-14.65%)</td><td>247.22 (-7.58%)</td><td>79.55 (-4.01%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.15 (n/a)</td><td>5.53 (n/a)</td><td>5.03 (n/a)</td><td>4.34 (n/a)</td><td>1.35 (n/a)</td><td>8027.80 (n/a)</td><td>6595.18 (n/a)</td><td>6927.30 (n/a)</td><td>4877.40 (n/a)</td><td>1519.72 (n/a)</td><td>440.29 (n/a)</td><td>340.82 (n/a)</td><td>310.00 (n/a)</td><td>267.51 (n/a)</td><td>82.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.80 (+1.96%)</td><td>0.77 (+1.75%)</td><td>0.77 (+2.45%)</td><td>0.74 (+1.28%)</td><td>0.02 (+1.82%)</td><td>101661.30 (-1.27%)</td><td>98355.34 (-1.72%)</td><td>97733.70 (-2.39%)</td><td>94902.20 (-1.92%)</td><td>2737.73 (-1.41%)</td><td>724.11 (+1.96%)</td><td>699.12 (+1.75%)</td><td>703.13 (+2.45%)</td><td>675.96 (+1.28%)</td><td>19.46 (+1.82%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102965.40 (n/a)</td><td>100075.02 (n/a)</td><td>100131.10 (n/a)</td><td>96762.50 (n/a)</td><td>2776.78 (n/a)</td><td>710.19 (n/a)</td><td>687.10 (n/a)</td><td>686.29 (n/a)</td><td>667.40 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (+0.29%)</td><td>0.75 (-1.48%)</td><td>0.76 (-0.54%)</td><td>0.70 (-6.97%)</td><td>0.03 <b>(+290.34%)</b></td><td>107201.60 (+7.50%)</td><td>100229.54 (+1.62%)</td><td>99157.50 (+0.54%)</td><td>96891.00 (-0.29%)</td><td>4015.81 <b>(+322.69%)</b></td><td>709.24 (+0.29%)</td><td>686.46 (-1.48%)</td><td>693.03 (-0.54%)</td><td>641.03 (-6.97%)</td><td>26.32 <b>(+290.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99724.40 (n/a)</td><td>98631.28 (n/a)</td><td>98626.60 (n/a)</td><td>97175.50 (n/a)</td><td>950.07 (n/a)</td><td>707.17 (n/a)</td><td>696.78 (n/a)</td><td>696.76 (n/a)</td><td>689.09 (n/a)</td><td>6.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.89 (-0.49%)</td><td>0.89 (-0.32%)</td><td>0.89 (-0.72%)</td><td>0.88 (+0.10%)</td><td>0.00 <b>(-36.47%)</b></td><td>85779.60 (-0.10%)</td><td>85053.34 (+0.32%)</td><td>85017.10 (+0.73%)</td><td>84509.30 (+0.49%)</td><td>464.09 <b>(-36.18%)</b></td><td>813.16 (-0.49%)</td><td>807.98 (-0.32%)</td><td>808.30 (-0.72%)</td><td>801.12 (+0.10%)</td><td>4.40 <b>(-36.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85865.40 (n/a)</td><td>84783.38 (n/a)</td><td>84401.50 (n/a)</td><td>84095.50 (n/a)</td><td>727.22 (n/a)</td><td>817.16 (n/a)</td><td>810.58 (n/a)</td><td>814.20 (n/a)</td><td>800.32 (n/a)</td><td>6.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.43 <b>(-44.46%)</b></td><td>2.01 <b>(-24.40%)</b></td><td>2.13 (-14.79%)</td><td>1.38 (-18.62%)</td><td>0.46 <b>(-54.89%)</b></td><td>5839.50 <b>(+22.88%)</b></td><td>4199.48 <b>(+25.63%)</b></td><td>3777.70 (+17.35%)</td><td>3316.30 <b>(+80.05%)</b></td><td>1087.20 (+0.79%)</td><td>637.43 <b>(-44.46%)</b></td><td>528.34 <b>(-24.40%)</b></td><td>559.58 (-14.79%)</td><td>362.00 (-18.62%)</td><td>121.81 <b>(-54.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.38 (n/a)</td><td>2.66 (n/a)</td><td>2.50 (n/a)</td><td>1.70 (n/a)</td><td>1.03 (n/a)</td><td>4752.20 (n/a)</td><td>3342.72 (n/a)</td><td>3219.10 (n/a)</td><td>1841.90 (n/a)</td><td>1078.66 (n/a)</td><td>1147.70 (n/a)</td><td>698.86 (n/a)</td><td>656.67 (n/a)</td><td>444.84 (n/a)</td><td>270.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 <b>(+21.74%)</b></td><td>0.20 (-1.15%)</td><td>0.18 (-9.76%)</td><td>0.18 (-2.63%)</td><td>0.04 <b>(+144.85%)</b></td><td>6950.10 (+2.70%)</td><td>6304.14 (+3.30%)</td><td>6878.10 (+10.81%)</td><td>4565.20 (-17.86%)</td><td>1024.49 <b>(+108.18%)</b></td><td>14.70 <b>(+21.74%)</b></td><td>10.93 (-1.15%)</td><td>9.76 (-9.76%)</td><td>9.66 (-2.63%)</td><td>2.17 <b>(+144.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6767.50 (n/a)</td><td>6102.66 (n/a)</td><td>6207.10 (n/a)</td><td>5557.70 (n/a)</td><td>492.13 (n/a)</td><td>12.07 (n/a)</td><td>11.05 (n/a)</td><td>10.81 (n/a)</td><td>9.92 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.79 (n/a)</td><td>3.61 (n/a)</td><td>3.58 (n/a)</td><td>3.47 (n/a)</td><td>0.12 (n/a)</td><td>3.78 (n/a)</td><td>3.61 (n/a)</td><td>3.58 (n/a)</td><td>3.47 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.56 (-1.38%)</td><td>6.19 (-5.46%)</td><td>5.94 (-11.34%)</td><td>4.28 <b>(-24.81%)</b></td><td>1.32 <b>(+64.74%)</b></td><td>7.55 (-1.38%)</td><td>6.19 (-5.46%)</td><td>5.94 (-11.34%)</td><td>4.28 <b>(-24.81%)</b></td><td>1.32 <b>(+64.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.66 (n/a)</td><td>6.55 (n/a)</td><td>6.70 (n/a)</td><td>5.70 (n/a)</td><td>0.80 (n/a)</td><td>7.66 (n/a)</td><td>6.54 (n/a)</td><td>6.70 (n/a)</td><td>5.69 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>12.93 (+6.26%)</td><td>9.29 (+0.71%)</td><td>8.58 (-5.67%)</td><td>7.72 (+9.45%)</td><td>2.08 (-1.39%)</td><td>12.92 (+6.26%)</td><td>9.28 (+0.71%)</td><td>8.58 (-5.67%)</td><td>7.72 (+9.45%)</td><td>2.08 (-1.39%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>12.17 (n/a)</td><td>9.22 (n/a)</td><td>9.10 (n/a)</td><td>7.05 (n/a)</td><td>2.11 (n/a)</td><td>12.16 (n/a)</td><td>9.21 (n/a)</td><td>9.09 (n/a)</td><td>7.05 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.82 (n/a)</td><td>3.57 (n/a)</td><td>3.51 (n/a)</td><td>3.31 (n/a)</td><td>0.21 (n/a)</td><td>3.82 (n/a)</td><td>3.57 (n/a)</td><td>3.50 (n/a)</td><td>3.31 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.12 (-4.09%)</td><td>5.90 (-13.30%)</td><td>5.67 (-15.29%)</td><td>5.35 (-16.97%)</td><td>0.70 <b>(+80.87%)</b></td><td>7.12 (-4.09%)</td><td>5.90 (-13.30%)</td><td>5.67 (-15.29%)</td><td>5.34 (-16.97%)</td><td>0.70 <b>(+80.87%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.42 (n/a)</td><td>6.81 (n/a)</td><td>6.70 (n/a)</td><td>6.44 (n/a)</td><td>0.39 (n/a)</td><td>7.42 (n/a)</td><td>6.80 (n/a)</td><td>6.69 (n/a)</td><td>6.44 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>12.60 (-12.77%)</td><td>9.66 <b>(-20.07%)</b></td><td>8.23 <b>(-37.61%)</b></td><td>7.84 (-13.05%)</td><td>2.21 (-10.73%)</td><td>12.60 (-12.77%)</td><td>9.65 <b>(-20.07%)</b></td><td>8.22 <b>(-37.61%)</b></td><td>7.84 (-13.05%)</td><td>2.21 (-10.73%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>14.45 (n/a)</td><td>12.08 (n/a)</td><td>13.19 (n/a)</td><td>9.02 (n/a)</td><td>2.48 (n/a)</td><td>14.44 (n/a)</td><td>12.07 (n/a)</td><td>13.18 (n/a)</td><td>9.02 (n/a)</td><td>2.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.09 (-4.19%)</td><td>2.60 <b>(+29.11%)</b></td><td>2.91 <b>(+72.48%)</b></td><td>1.57 <b>(+53.86%)</b></td><td>0.64 <b>(-40.48%)</b></td><td>3.08 (-4.19%)</td><td>2.59 <b>(+29.11%)</b></td><td>2.90 <b>(+72.48%)</b></td><td>1.57 <b>(+53.86%)</b></td><td>0.64 <b>(-40.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.23 (n/a)</td><td>2.01 (n/a)</td><td>1.68 (n/a)</td><td>1.02 (n/a)</td><td>1.08 (n/a)</td><td>3.22 (n/a)</td><td>2.01 (n/a)</td><td>1.68 (n/a)</td><td>1.02 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.57 (+3.34%)</td><td>0.26 <b>(-39.81%)</b></td><td>0.21 <b>(-58.51%)</b></td><td>0.07 <b>(-48.92%)</b></td><td>0.21 <b>(+27.90%)</b></td><td>0.56 (+3.34%)</td><td>0.26 <b>(-39.81%)</b></td><td>0.21 <b>(-58.51%)</b></td><td>0.07 <b>(-48.92%)</b></td><td>0.21 <b>(+27.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.51 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.50 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (+5.20%)</td><td>0.44 <b>(-32.41%)</b></td><td>0.47 <b>(-27.31%)</b></td><td>0.08 <b>(-85.90%)</b></td><td>0.28 <b>(+302.12%)</b></td><td>0.78 (+5.20%)</td><td>0.44 <b>(-32.41%)</b></td><td>0.46 <b>(-27.31%)</b></td><td>0.08 <b>(-85.90%)</b></td><td>0.28 <b>(+302.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.75 (n/a)</td><td>0.66 (n/a)</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.07 (n/a)</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.66 (-3.73%)</td><td>1.97 (-1.88%)</td><td>2.34 <b>(+21.62%)</b></td><td>0.44 <b>(-59.34%)</b></td><td>0.91 <b>(+41.88%)</b></td><td>2.62 (-3.73%)</td><td>1.94 (-1.88%)</td><td>2.30 <b>(+21.62%)</b></td><td>0.43 <b>(-59.34%)</b></td><td>0.90 <b>(+41.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.77 (n/a)</td><td>2.01 (n/a)</td><td>1.92 (n/a)</td><td>1.08 (n/a)</td><td>0.64 (n/a)</td><td>2.72 (n/a)</td><td>1.97 (n/a)</td><td>1.89 (n/a)</td><td>1.06 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1935.50 (n/a)</td><td>701.36 (n/a)</td><td>376.40 (n/a)</td><td>300.30 (n/a)</td><td>700.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>418.90 (n/a)</td><td>320.46 (n/a)</td><td>297.00 (n/a)</td><td>225.70 (n/a)</td><td>74.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.90 (n/a)</td><td>349.38 (n/a)</td><td>299.50 (n/a)</td><td>256.90 (n/a)</td><td>95.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.40 (n/a)</td><td>360.64 (n/a)</td><td>310.40 (n/a)</td><td>297.10 (n/a)</td><td>103.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.80 (n/a)</td><td>304.28 (n/a)</td><td>300.70 (n/a)</td><td>210.20 (n/a)</td><td>105.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.30 (n/a)</td><td>501.16 (n/a)</td><td>506.10 (n/a)</td><td>316.70 (n/a)</td><td>115.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.70 (n/a)</td><td>417.98 (n/a)</td><td>432.20 (n/a)</td><td>267.90 (n/a)</td><td>145.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.90 (n/a)</td><td>363.52 (n/a)</td><td>300.00 (n/a)</td><td>233.90 (n/a)</td><td>150.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.00 (n/a)</td><td>380.86 (n/a)</td><td>334.10 (n/a)</td><td>231.20 (n/a)</td><td>154.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.70 (n/a)</td><td>394.86 (n/a)</td><td>343.20 (n/a)</td><td>268.30 (n/a)</td><td>131.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>485.90 (n/a)</td><td>368.16 (n/a)</td><td>314.50 (n/a)</td><td>257.80 (n/a)</td><td>109.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.00 (n/a)</td><td>459.12 (n/a)</td><td>443.40 (n/a)</td><td>326.20 (n/a)</td><td>102.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.50 (n/a)</td><td>471.56 (n/a)</td><td>514.50 (n/a)</td><td>192.60 (n/a)</td><td>162.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>591.90 (n/a)</td><td>414.46 (n/a)</td><td>509.00 (n/a)</td><td>184.90 (n/a)</td><td>186.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2010.10 (n/a)</td><td>661.84 (n/a)</td><td>304.80 (n/a)</td><td>215.60 (n/a)</td><td>764.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>564.90 (n/a)</td><td>386.24 (n/a)</td><td>330.30 (n/a)</td><td>239.70 (n/a)</td><td>147.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>509.10 (n/a)</td><td>432.46 (n/a)</td><td>481.80 (n/a)</td><td>270.70 (n/a)</td><td>96.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.90 (n/a)</td><td>485.26 (n/a)</td><td>526.60 (n/a)</td><td>210.90 (n/a)</td><td>166.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1886.60 (n/a)</td><td>609.18 (n/a)</td><td>305.70 (n/a)</td><td>260.60 (n/a)</td><td>714.46 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>612.70 (n/a)</td><td>433.10 (n/a)</td><td>479.50 (n/a)</td><td>261.40 (n/a)</td><td>143.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>638.10 (n/a)</td><td>394.06 (n/a)</td><td>322.90 (n/a)</td><td>268.50 (n/a)</td><td>149.56 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.10 (n/a)</td><td>430.74 (n/a)</td><td>413.90 (n/a)</td><td>240.50 (n/a)</td><td>128.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>856.60 (n/a)</td><td>545.46 (n/a)</td><td>531.50 (n/a)</td><td>275.30 (n/a)</td><td>264.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>554.20 (n/a)</td><td>365.24 (n/a)</td><td>312.80 (n/a)</td><td>295.60 (n/a)</td><td>109.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-33.98%)</b></td><td>0.01 <b>(-26.52%)</b></td><td>0.01 <b>(-23.04%)</b></td><td>0.01 <b>(-48.80%)</b></td><td>0.00 (-19.58%)</td><td>579.70 <b>(+95.32%)</b></td><td>350.78 <b>(+42.52%)</b></td><td>313.40 <b>(+29.93%)</b></td><td>238.10 <b>(+51.46%)</b></td><td>137.58 <b>(+141.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>296.80 (n/a)</td><td>246.12 (n/a)</td><td>241.20 (n/a)</td><td>157.20 (n/a)</td><td>57.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-16.18%)</td><td>0.01 <b>(-36.83%)</b></td><td>0.01 <b>(-51.83%)</b></td><td>0.01 <b>(-21.14%)</b></td><td>0.00 (-8.77%)</td><td>677.70 <b>(+26.82%)</b></td><td>473.96 <b>(+59.52%)</b></td><td>493.70 <b>(+107.61%)</b></td><td>225.70 (+19.29%)</td><td>162.05 (+17.92%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.40 (n/a)</td><td>297.12 (n/a)</td><td>237.80 (n/a)</td><td>189.20 (n/a)</td><td>137.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-15.37%)</td><td>0.01 (-16.60%)</td><td>0.01 <b>(-39.80%)</b></td><td>0.01 <b>(+29.78%)</b></td><td>0.00 <b>(-41.35%)</b></td><td>502.10 <b>(-22.94%)</b></td><td>408.12 (+7.55%)</td><td>447.80 <b>(+66.16%)</b></td><td>280.50 (+18.16%)</td><td>105.03 <b>(-43.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.60 (n/a)</td><td>379.46 (n/a)</td><td>269.50 (n/a)</td><td>237.40 (n/a)</td><td>186.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-2.62%)</td><td>0.01 (-9.71%)</td><td>0.01 <b>(-27.89%)</b></td><td>0.01 <b>(+69.24%)</b></td><td>0.00 (-17.41%)</td><td>638.70 <b>(-40.91%)</b></td><td>471.96 (-4.96%)</td><td>518.10 <b>(+38.68%)</b></td><td>243.30 (+2.70%)</td><td>149.41 <b>(-55.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1080.90 (n/a)</td><td>496.58 (n/a)</td><td>373.60 (n/a)</td><td>236.90 (n/a)</td><td>338.45 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+6.09%)</td><td>0.01 (-8.54%)</td><td>0.01 (-18.83%)</td><td>0.01 (-3.52%)</td><td>0.00 (+11.68%)</td><td>573.90 (+3.65%)</td><td>384.70 (+11.44%)</td><td>392.60 <b>(+23.19%)</b></td><td>223.80 (-5.73%)</td><td>139.93 (+8.84%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.70 (n/a)</td><td>345.20 (n/a)</td><td>318.70 (n/a)</td><td>237.40 (n/a)</td><td>128.56 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-6.55%)</td><td>0.01 (-3.04%)</td><td>0.01 (+6.40%)</td><td>0.01 <b>(+52.48%)</b></td><td>0.00 <b>(-21.80%)</b></td><td>566.40 <b>(-34.42%)</b></td><td>458.00 (-9.30%)</td><td>515.60 (-6.02%)</td><td>221.10 (+7.02%)</td><td>140.66 <b>(-45.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>863.70 (n/a)</td><td>504.94 (n/a)</td><td>548.60 (n/a)</td><td>206.60 (n/a)</td><td>257.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-40.93%)</b></td><td>0.02 <b>(-39.65%)</b></td><td>0.02 <b>(-37.19%)</b></td><td>0.01 <b>(-39.49%)</b></td><td>0.00 <b>(-36.73%)</b></td><td>549.40 <b>(+65.28%)</b></td><td>461.44 <b>(+66.08%)</b></td><td>428.90 <b>(+59.21%)</b></td><td>381.40 <b>(+69.29%)</b></td><td>70.66 <b>(+80.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>332.40 (n/a)</td><td>277.84 (n/a)</td><td>269.40 (n/a)</td><td>225.30 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (-14.27%)</td><td>0.03 (+19.41%)</td><td>0.03 <b>(+20.35%)</b></td><td>0.03 <b>(+93.14%)</b></td><td>0.01 <b>(-60.62%)</b></td><td>296.50 <b>(-48.23%)</b></td><td>265.72 <b>(-29.67%)</b></td><td>274.50 (-16.89%)</td><td>201.80 (+16.65%)</td><td>38.21 <b>(-77.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.70 (n/a)</td><td>377.82 (n/a)</td><td>330.30 (n/a)</td><td>173.00 (n/a)</td><td>172.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-15.13%)</td><td>0.02 (-15.19%)</td><td>0.02 <b>(-29.12%)</b></td><td>0.02 (-11.76%)</td><td>0.01 (-11.66%)</td><td>541.30 (+13.34%)</td><td>423.10 (+17.84%)</td><td>453.10 <b>(+41.11%)</b></td><td>284.20 (+17.83%)</td><td>121.18 (+11.46%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.60 (n/a)</td><td>359.04 (n/a)</td><td>321.10 (n/a)</td><td>241.20 (n/a)</td><td>108.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-13.17%)</td><td>0.03 (+2.89%)</td><td>0.03 (+7.15%)</td><td>0.02 (+18.69%)</td><td>0.00 <b>(-43.77%)</b></td><td>428.00 (-15.75%)</td><td>306.22 (-8.73%)</td><td>283.20 (-6.69%)</td><td>261.70 (+15.18%)</td><td>69.11 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.00 (n/a)</td><td>335.50 (n/a)</td><td>303.50 (n/a)</td><td>227.20 (n/a)</td><td>119.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 <b>(-36.21%)</b></td><td>0.03 (-3.80%)</td><td>0.02 <b>(+59.67%)</b></td><td>0.02 <b>(+28.47%)</b></td><td>0.01 <b>(-58.50%)</b></td><td>441.50 <b>(-22.16%)</b></td><td>336.80 (-17.34%)</td><td>329.90 <b>(-37.38%)</b></td><td>227.80 <b>(+56.78%)</b></td><td>96.13 <b>(-51.97%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>567.20 (n/a)</td><td>407.46 (n/a)</td><td>526.80 (n/a)</td><td>145.30 (n/a)</td><td>200.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-9.17%)</td><td>0.02 <b>(-21.42%)</b></td><td>0.02 <b>(-42.51%)</b></td><td>0.02 (-4.71%)</td><td>0.01 <b>(-31.74%)</b></td><td>517.70 (+4.95%)</td><td>417.58 <b>(+20.81%)</b></td><td>454.20 <b>(+73.96%)</b></td><td>265.50 (+10.07%)</td><td>101.67 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.30 (n/a)</td><td>345.66 (n/a)</td><td>261.10 (n/a)</td><td>241.20 (n/a)</td><td>133.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (+0.45%)</td><td>0.02 (+12.38%)</td><td>0.03 <b>(+61.06%)</b></td><td>0.02 (+13.13%)</td><td>0.01 (-18.71%)</td><td>524.10 (-11.60%)</td><td>364.30 (-15.74%)</td><td>317.20 <b>(-37.91%)</b></td><td>245.80 (-0.45%)</td><td>123.79 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.90 (n/a)</td><td>432.34 (n/a)</td><td>510.90 (n/a)</td><td>246.90 (n/a)</td><td>165.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-13.68%)</td><td>0.02 (+10.00%)</td><td>0.02 (+18.50%)</td><td>0.01 <b>(+279.53%)</b></td><td>0.01 <b>(-46.24%)</b></td><td>606.70 <b>(-73.65%)</b></td><td>444.50 <b>(-44.98%)</b></td><td>479.80 (-15.60%)</td><td>300.70 (+15.88%)</td><td>129.63 <b>(-84.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2302.40 (n/a)</td><td>807.88 (n/a)</td><td>568.50 (n/a)</td><td>259.50 (n/a)</td><td>849.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-20.34%)</b></td><td>0.05 (+1.39%)</td><td>0.06 (+9.23%)</td><td>0.03 (-5.01%)</td><td>0.01 <b>(-36.45%)</b></td><td>546.60 (+5.28%)</td><td>323.86 (-7.74%)</td><td>270.10 (-8.44%)</td><td>259.70 <b>(+25.52%)</b></td><td>124.65 (-17.75%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>519.20 (n/a)</td><td>351.04 (n/a)</td><td>295.00 (n/a)</td><td>206.90 (n/a)</td><td>151.56 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+0.13%)</td><td>0.05 (-7.22%)</td><td>0.05 (-13.33%)</td><td>0.03 <b>(+30.06%)</b></td><td>0.01 (-11.67%)</td><td>472.20 <b>(-23.11%)</b></td><td>353.28 (+2.99%)</td><td>327.60 (+15.39%)</td><td>240.90 (-0.12%)</td><td>98.59 <b>(-35.57%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.10 (n/a)</td><td>343.02 (n/a)</td><td>283.90 (n/a)</td><td>241.20 (n/a)</td><td>153.01 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+6.56%)</td><td>0.06 (+18.92%)</td><td>0.06 (+8.61%)</td><td>0.03 <b>(+30.91%)</b></td><td>0.01 <b>(-22.35%)</b></td><td>490.60 <b>(-23.62%)</b></td><td>305.98 <b>(-21.70%)</b></td><td>275.90 (-7.94%)</td><td>239.90 (-6.14%)</td><td>104.56 <b>(-39.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.30 (n/a)</td><td>390.78 (n/a)</td><td>299.70 (n/a)</td><td>255.60 (n/a)</td><td>173.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+2.48%)</td><td>0.05 (+5.19%)</td><td>0.06 (+4.61%)</td><td>0.03 (+18.07%)</td><td>0.02 (-4.95%)</td><td>513.60 (-15.32%)</td><td>357.22 (-7.76%)</td><td>288.90 (-4.40%)</td><td>238.20 (-2.46%)</td><td>136.95 (-18.80%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.50 (n/a)</td><td>387.26 (n/a)</td><td>302.20 (n/a)</td><td>244.20 (n/a)</td><td>168.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-25.99%)</b></td><td>0.04 (-19.60%)</td><td>0.05 <b>(-28.44%)</b></td><td>0.03 (+0.11%)</td><td>0.01 <b>(-51.52%)</b></td><td>521.10 (-0.12%)</td><td>384.82 (+11.25%)</td><td>342.80 <b>(+39.75%)</b></td><td>274.30 <b>(+35.06%)</b></td><td>97.87 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>521.70 (n/a)</td><td>345.92 (n/a)</td><td>245.30 (n/a)</td><td>203.10 (n/a)</td><td>159.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 <b>(-20.77%)</b></td><td>0.04 (+12.41%)</td><td>0.04 <b>(+58.52%)</b></td><td>0.03 <b>(+103.59%)</b></td><td>0.01 <b>(-59.03%)</b></td><td>502.40 <b>(-50.88%)</b></td><td>397.88 <b>(-29.57%)</b></td><td>389.80 <b>(-36.92%)</b></td><td>304.60 <b>(+26.23%)</b></td><td>83.50 <b>(-73.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1022.90 (n/a)</td><td>564.94 (n/a)</td><td>617.90 (n/a)</td><td>241.30 (n/a)</td><td>312.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (-9.43%)</td><td>0.08 (-15.19%)</td><td>0.08 (-3.23%)</td><td>0.05 (-9.47%)</td><td>0.03 <b>(-25.59%)</b></td><td>599.60 (+10.46%)</td><td>447.76 (+13.85%)</td><td>430.10 (+3.34%)</td><td>269.30 (+10.41%)</td><td>127.38 (-7.86%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>542.80 (n/a)</td><td>393.30 (n/a)</td><td>416.20 (n/a)</td><td>243.90 (n/a)</td><td>138.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 <b>(-25.51%)</b></td><td>0.11 (-14.41%)</td><td>0.12 (-4.15%)</td><td>0.06 (-0.58%)</td><td>0.03 <b>(-28.07%)</b></td><td>518.60 (+0.58%)</td><td>333.34 (+12.54%)</td><td>281.50 (+4.34%)</td><td>249.70 <b>(+34.25%)</b></td><td>114.13 (-10.84%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>515.60 (n/a)</td><td>296.20 (n/a)</td><td>269.80 (n/a)</td><td>186.00 (n/a)</td><td>128.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (+3.14%)</td><td>0.09 (-10.61%)</td><td>0.07 <b>(-28.77%)</b></td><td>0.05 <b>(-30.05%)</b></td><td>0.04 <b>(+45.50%)</b></td><td>637.20 <b>(+42.97%)</b></td><td>423.22 <b>(+21.11%)</b></td><td>445.30 <b>(+40.38%)</b></td><td>239.20 (-3.08%)</td><td>162.86 <b>(+87.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>445.70 (n/a)</td><td>349.44 (n/a)</td><td>317.20 (n/a)</td><td>246.80 (n/a)</td><td>87.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (-15.58%)</td><td>0.08 <b>(-32.44%)</b></td><td>0.06 <b>(-49.39%)</b></td><td>0.05 <b>(-23.52%)</b></td><td>0.04 (+6.00%)</td><td>656.00 <b>(+30.73%)</b></td><td>478.14 <b>(+57.89%)</b></td><td>539.80 <b>(+97.58%)</b></td><td>231.50 (+18.47%)</td><td>187.59 <b>(+59.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>501.80 (n/a)</td><td>302.84 (n/a)</td><td>273.20 (n/a)</td><td>195.40 (n/a)</td><td>117.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (-10.47%)</td><td>0.08 (-4.70%)</td><td>0.07 (+1.00%)</td><td>0.05 (-1.72%)</td><td>0.03 (-16.97%)</td><td>686.10 (+1.75%)</td><td>448.68 (+2.08%)</td><td>468.40 (-0.97%)</td><td>253.70 (+11.66%)</td><td>163.63 (-4.71%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.30 (n/a)</td><td>439.54 (n/a)</td><td>473.00 (n/a)</td><td>227.20 (n/a)</td><td>171.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-9.15%)</td><td>0.01 (-18.25%)</td><td>0.01 (-18.37%)</td><td>0.01 <b>(-24.93%)</b></td><td>0.00 (+14.50%)</td><td>601.70 <b>(+33.21%)</b></td><td>385.12 <b>(+27.09%)</b></td><td>331.00 <b>(+22.50%)</b></td><td>268.20 (+10.10%)</td><td>136.84 <b>(+61.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>451.70 (n/a)</td><td>303.04 (n/a)</td><td>270.20 (n/a)</td><td>243.60 (n/a)</td><td>84.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-15.17%)</td><td>0.01 <b>(-20.40%)</b></td><td>0.01 (-11.92%)</td><td>0.01 <b>(-38.31%)</b></td><td>0.00 <b>(+79.58%)</b></td><td>513.90 <b>(+62.06%)</b></td><td>362.34 <b>(+30.70%)</b></td><td>306.00 (+13.54%)</td><td>295.00 (+17.86%)</td><td>95.49 <b>(+236.10%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>317.10 (n/a)</td><td>277.22 (n/a)</td><td>269.50 (n/a)</td><td>250.30 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(+26.41%)</b></td><td>0.01 (+18.92%)</td><td>0.01 <b>(+26.13%)</b></td><td>0.01 (+0.14%)</td><td>0.00 <b>(+36.12%)</b></td><td>609.40 (-0.15%)</td><td>371.54 (-12.70%)</td><td>294.00 <b>(-20.71%)</b></td><td>233.10 <b>(-20.88%)</b></td><td>156.05 (+9.21%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.30 (n/a)</td><td>425.60 (n/a)</td><td>370.80 (n/a)</td><td>294.60 (n/a)</td><td>142.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-15.84%)</td><td>0.01 (+17.61%)</td><td>0.01 <b>(+25.82%)</b></td><td>0.01 <b>(+67.64%)</b></td><td>0.00 <b>(-57.10%)</b></td><td>397.00 <b>(-40.35%)</b></td><td>305.54 <b>(-24.33%)</b></td><td>283.50 <b>(-20.52%)</b></td><td>272.90 (+18.86%)</td><td>52.36 <b>(-69.63%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>665.60 (n/a)</td><td>403.80 (n/a)</td><td>356.70 (n/a)</td><td>229.60 (n/a)</td><td>172.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+9.83%)</td><td>0.02 <b>(+62.53%)</b></td><td>0.02 <b>(+114.59%)</b></td><td>0.01 <b>(+83.33%)</b></td><td>0.00 (-12.61%)</td><td>572.70 <b>(-45.45%)</b></td><td>307.34 <b>(-46.46%)</b></td><td>242.20 <b>(-53.40%)</b></td><td>218.60 (-8.95%)</td><td>149.33 <b>(-53.56%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1049.90 (n/a)</td><td>574.08 (n/a)</td><td>519.70 (n/a)</td><td>240.10 (n/a)</td><td>321.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+7.13%)</td><td>0.01 (+8.97%)</td><td>0.01 (+15.45%)</td><td>0.01 (-9.39%)</td><td>0.00 (+10.50%)</td><td>555.40 (+10.37%)</td><td>331.32 (-6.13%)</td><td>289.00 (-13.37%)</td><td>238.60 (-6.69%)</td><td>127.15 <b>(+25.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.20 (n/a)</td><td>352.94 (n/a)</td><td>333.60 (n/a)</td><td>255.70 (n/a)</td><td>101.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-18.72%)</td><td>0.01 (-5.70%)</td><td>0.01 <b>(-23.33%)</b></td><td>0.01 <b>(+64.43%)</b></td><td>0.00 <b>(-49.50%)</b></td><td>473.70 <b>(-39.18%)</b></td><td>347.64 (-13.11%)</td><td>339.80 <b>(+30.44%)</b></td><td>243.60 <b>(+23.03%)</b></td><td>90.32 <b>(-62.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>778.90 (n/a)</td><td>400.10 (n/a)</td><td>260.50 (n/a)</td><td>198.00 (n/a)</td><td>243.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+9.80%)</td><td>0.01 (+10.38%)</td><td>0.01 (+9.22%)</td><td>0.01 <b>(+27.39%)</b></td><td>0.00 (-5.28%)</td><td>587.90 <b>(-21.50%)</b></td><td>400.22 (-13.63%)</td><td>436.60 (-8.43%)</td><td>240.40 (-8.90%)</td><td>138.47 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>748.90 (n/a)</td><td>463.36 (n/a)</td><td>476.80 (n/a)</td><td>263.90 (n/a)</td><td>198.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-19.19%)</td><td>0.01 (+8.73%)</td><td>0.01 <b>(+48.33%)</b></td><td>0.01 (-0.40%)</td><td>0.00 <b>(-25.05%)</b></td><td>550.10 (+0.40%)</td><td>374.98 (-10.23%)</td><td>303.10 <b>(-32.58%)</b></td><td>275.80 <b>(+23.73%)</b></td><td>120.44 (-2.60%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.90 (n/a)</td><td>417.72 (n/a)</td><td>449.60 (n/a)</td><td>222.90 (n/a)</td><td>123.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+0.94%)</td><td>0.01 (+13.63%)</td><td>0.01 (+15.05%)</td><td>0.01 <b>(+22.55%)</b></td><td>0.00 (-10.38%)</td><td>504.50 (-18.39%)</td><td>383.44 (-14.96%)</td><td>413.90 (-13.08%)</td><td>231.80 (-0.94%)</td><td>109.41 <b>(-25.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.20 (n/a)</td><td>450.90 (n/a)</td><td>476.20 (n/a)</td><td>234.00 (n/a)</td><td>146.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 <b>(-22.76%)</b></td><td>0.01 (-9.18%)</td><td>0.01 (+14.24%)</td><td>0.01 (-18.41%)</td><td>0.00 (-18.35%)</td><td>681.90 <b>(+22.56%)</b></td><td>415.28 (+10.65%)</td><td>316.40 (-12.45%)</td><td>276.90 <b>(+29.45%)</b></td><td>177.28 <b>(+25.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.40 (n/a)</td><td>375.32 (n/a)</td><td>361.40 (n/a)</td><td>213.90 (n/a)</td><td>141.07 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+16.08%)</td><td>0.01 (+15.76%)</td><td>0.01 (-1.91%)</td><td>0.01 <b>(+314.82%)</b></td><td>0.00 (-18.09%)</td><td>576.70 <b>(-75.90%)</b></td><td>432.48 <b>(-45.53%)</b></td><td>482.30 (+1.94%)</td><td>259.60 (-13.87%)</td><td>139.91 <b>(-84.41%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2392.50 (n/a)</td><td>793.94 (n/a)</td><td>473.10 (n/a)</td><td>301.40 (n/a)</td><td>897.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-15.42%)</td><td>0.02 <b>(-22.20%)</b></td><td>0.03 (-2.80%)</td><td>0.01 <b>(-59.62%)</b></td><td>0.01 <b>(+129.87%)</b></td><td>738.10 <b>(+147.68%)</b></td><td>407.36 <b>(+47.33%)</b></td><td>296.00 (+2.88%)</td><td>266.50 (+18.23%)</td><td>199.18 <b>(+578.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>298.00 (n/a)</td><td>276.50 (n/a)</td><td>287.70 (n/a)</td><td>225.40 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 <b>(+32.08%)</b></td><td>0.02 (+15.90%)</td><td>0.02 (+5.94%)</td><td>0.01 (-4.26%)</td><td>0.01 <b>(+84.59%)</b></td><td>569.90 (+4.45%)</td><td>399.26 (-7.74%)</td><td>388.60 (-5.61%)</td><td>236.90 <b>(-24.29%)</b></td><td>143.24 <b>(+43.42%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>545.60 (n/a)</td><td>432.74 (n/a)</td><td>411.70 (n/a)</td><td>312.90 (n/a)</td><td>99.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 <b>(+57.01%)</b></td><td>0.03 <b>(+55.11%)</b></td><td>0.03 <b>(+111.51%)</b></td><td>0.01 (+13.80%)</td><td>0.01 <b>(+62.35%)</b></td><td>589.10 (-12.13%)</td><td>335.70 <b>(-32.40%)</b></td><td>270.30 <b>(-52.72%)</b></td><td>187.50 <b>(-36.31%)</b></td><td>159.75 (-5.41%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.40 (n/a)</td><td>496.60 (n/a)</td><td>571.70 (n/a)</td><td>294.40 (n/a)</td><td>168.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-37.00%)</b></td><td>0.02 <b>(-27.47%)</b></td><td>0.02 <b>(-31.05%)</b></td><td>0.01 <b>(-20.66%)</b></td><td>0.00 <b>(-53.16%)</b></td><td>734.40 <b>(+26.06%)</b></td><td>497.02 <b>(+29.70%)</b></td><td>466.70 <b>(+45.03%)</b></td><td>373.70 <b>(+58.75%)</b></td><td>140.10 (-4.89%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.60 (n/a)</td><td>383.22 (n/a)</td><td>321.80 (n/a)</td><td>235.40 (n/a)</td><td>147.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 <b>(-28.57%)</b></td><td>0.03 (-0.45%)</td><td>0.03 (+2.30%)</td><td>0.02 (+8.25%)</td><td>0.01 <b>(-51.15%)</b></td><td>459.90 (-7.63%)</td><td>313.50 (-7.56%)</td><td>285.50 (-2.26%)</td><td>256.30 <b>(+39.98%)</b></td><td>82.84 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.90 (n/a)</td><td>339.14 (n/a)</td><td>292.10 (n/a)</td><td>183.10 (n/a)</td><td>128.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-49.00%)</b></td><td>0.02 <b>(-42.55%)</b></td><td>0.02 <b>(-42.87%)</b></td><td>0.01 <b>(-29.31%)</b></td><td>0.00 <b>(-68.52%)</b></td><td>754.50 <b>(+41.48%)</b></td><td>553.60 <b>(+62.04%)</b></td><td>508.30 <b>(+75.03%)</b></td><td>459.50 <b>(+96.12%)</b></td><td>119.02 (-7.91%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>341.64 (n/a)</td><td>290.40 (n/a)</td><td>234.30 (n/a)</td><td>129.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-16.59%)</td><td>0.03 (+13.55%)</td><td>0.03 <b>(+55.96%)</b></td><td>0.02 <b>(+40.71%)</b></td><td>0.00 <b>(-50.05%)</b></td><td>422.90 <b>(-28.94%)</b></td><td>320.26 <b>(-20.50%)</b></td><td>286.90 <b>(-35.87%)</b></td><td>263.30 (+19.90%)</td><td>66.87 <b>(-56.33%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.10 (n/a)</td><td>402.82 (n/a)</td><td>447.40 (n/a)</td><td>219.60 (n/a)</td><td>153.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-3.13%)</td><td>0.02 (-15.01%)</td><td>0.02 (-14.22%)</td><td>0.01 <b>(-53.45%)</b></td><td>0.01 (+17.62%)</td><td>1196.30 <b>(+114.81%)</b></td><td>574.54 <b>(+38.22%)</b></td><td>459.80 (+16.58%)</td><td>237.60 (+3.21%)</td><td>366.00 <b>(+162.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.90 (n/a)</td><td>415.66 (n/a)</td><td>394.40 (n/a)</td><td>230.20 (n/a)</td><td>139.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-13.12%)</td><td>0.02 <b>(-31.38%)</b></td><td>0.02 <b>(-29.67%)</b></td><td>0.01 <b>(-25.14%)</b></td><td>0.01 (-1.86%)</td><td>608.30 <b>(+33.57%)</b></td><td>458.80 <b>(+49.92%)</b></td><td>428.50 <b>(+42.17%)</b></td><td>268.20 (+15.11%)</td><td>139.92 <b>(+55.25%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.40 (n/a)</td><td>306.02 (n/a)</td><td>301.40 (n/a)</td><td>233.00 (n/a)</td><td>90.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 <b>(+20.84%)</b></td><td>0.02 <b>(+27.67%)</b></td><td>0.02 (+3.26%)</td><td>0.01 <b>(+20.32%)</b></td><td>0.01 <b>(+47.58%)</b></td><td>635.60 (-16.88%)</td><td>407.34 (-18.47%)</td><td>433.50 (-3.17%)</td><td>239.80 (-17.25%)</td><td>166.03 (-5.90%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>764.70 (n/a)</td><td>499.62 (n/a)</td><td>447.70 (n/a)</td><td>289.80 (n/a)</td><td>176.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-11.30%)</td><td>0.02 (+5.98%)</td><td>0.02 <b>(+38.13%)</b></td><td>0.01 (-3.04%)</td><td>0.01 (-13.38%)</td><td>571.40 (+3.12%)</td><td>389.96 (-6.72%)</td><td>345.40 <b>(-27.60%)</b></td><td>277.20 (+12.73%)</td><td>126.67 (-0.29%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.10 (n/a)</td><td>418.04 (n/a)</td><td>477.10 (n/a)</td><td>245.90 (n/a)</td><td>127.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-27.44%)</b></td><td>0.02 (-11.90%)</td><td>0.02 (-2.66%)</td><td>0.01 (+13.71%)</td><td>0.00 <b>(-57.80%)</b></td><td>589.60 (-12.05%)</td><td>443.02 (+0.41%)</td><td>429.70 (+2.73%)</td><td>349.80 <b>(+37.83%)</b></td><td>99.21 <b>(-48.10%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.40 (n/a)</td><td>441.20 (n/a)</td><td>418.30 (n/a)</td><td>253.80 (n/a)</td><td>191.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-6.88%)</td><td>0.05 (+16.23%)</td><td>0.06 <b>(+35.57%)</b></td><td>0.03 (+11.87%)</td><td>0.01 (-14.69%)</td><td>567.70 (-10.61%)</td><td>334.14 (-16.27%)</td><td>277.60 <b>(-26.23%)</b></td><td>262.10 (+7.37%)</td><td>131.33 (-15.21%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.10 (n/a)</td><td>399.08 (n/a)</td><td>376.30 (n/a)</td><td>244.10 (n/a)</td><td>154.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+16.29%)</td><td>0.06 <b>(+31.96%)</b></td><td>0.06 <b>(+24.72%)</b></td><td>0.05 <b>(+87.39%)</b></td><td>0.01 <b>(-52.79%)</b></td><td>302.70 <b>(-46.63%)</b></td><td>269.56 <b>(-29.91%)</b></td><td>258.70 (-19.83%)</td><td>235.60 (-14.01%)</td><td>30.08 <b>(-77.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.20 (n/a)</td><td>384.60 (n/a)</td><td>322.70 (n/a)</td><td>274.00 (n/a)</td><td>132.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+15.80%)</td><td>0.05 (+1.62%)</td><td>0.05 (-3.72%)</td><td>0.03 (-17.84%)</td><td>0.02 <b>(+46.07%)</b></td><td>568.40 <b>(+21.71%)</b></td><td>352.68 (+3.97%)</td><td>304.20 (+3.86%)</td><td>222.60 (-13.65%)</td><td>135.34 <b>(+56.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>467.00 (n/a)</td><td>339.22 (n/a)</td><td>292.90 (n/a)</td><td>257.80 (n/a)</td><td>86.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(+22.75%)</b></td><td>0.05 <b>(+42.71%)</b></td><td>0.06 <b>(+57.08%)</b></td><td>0.03 (+12.01%)</td><td>0.01 <b>(+26.24%)</b></td><td>473.40 (-10.71%)</td><td>317.16 <b>(-29.29%)</b></td><td>294.40 <b>(-36.33%)</b></td><td>242.90 (-18.54%)</td><td>91.14 (-3.54%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>530.20 (n/a)</td><td>448.52 (n/a)</td><td>462.40 (n/a)</td><td>298.20 (n/a)</td><td>94.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-9.99%)</td><td>0.05 (-9.40%)</td><td>0.05 (-16.59%)</td><td>0.03 (-2.07%)</td><td>0.01 (-17.00%)</td><td>486.20 (+2.12%)</td><td>377.74 (+8.56%)</td><td>358.30 (+19.87%)</td><td>276.60 (+11.13%)</td><td>102.96 (-6.34%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.10 (n/a)</td><td>347.96 (n/a)</td><td>298.90 (n/a)</td><td>248.90 (n/a)</td><td>109.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (-4.70%)</td><td>0.06 (+18.14%)</td><td>0.06 (+4.75%)</td><td>0.06 <b>(+612.01%)</b></td><td>0.01 <b>(-77.43%)</b></td><td>296.10 <b>(-85.96%)</b></td><td>262.64 <b>(-58.06%)</b></td><td>254.10 (-4.55%)</td><td>232.10 (+4.93%)</td><td>24.73 <b>(-97.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2108.40 (n/a)</td><td>626.20 (n/a)</td><td>266.20 (n/a)</td><td>221.20 (n/a)</td><td>828.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(+21.57%)</b></td><td>0.04 (+6.92%)</td><td>0.03 (-10.45%)</td><td>0.01 <b>(-53.97%)</b></td><td>0.02 <b>(+132.18%)</b></td><td>1208.10 <b>(+117.25%)</b></td><td>554.84 <b>(+24.23%)</b></td><td>470.10 (+11.66%)</td><td>250.10 (-17.76%)</td><td>392.98 <b>(+276.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.10 (n/a)</td><td>446.64 (n/a)</td><td>421.00 (n/a)</td><td>304.10 (n/a)</td><td>104.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(+59.90%)</b></td><td>0.06 <b>(+111.22%)</b></td><td>0.06 <b>(+80.29%)</b></td><td>0.05 <b>(+561.15%)</b></td><td>0.00 <b>(-82.62%)</b></td><td>302.50 <b>(-84.88%)</b></td><td>285.22 <b>(-65.49%)</b></td><td>281.80 <b>(-44.54%)</b></td><td>275.10 <b>(-37.46%)</b></td><td>10.74 <b>(-98.39%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2000.00 (n/a)</td><td>826.56 (n/a)</td><td>508.10 (n/a)</td><td>439.90 (n/a)</td><td>666.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (+10.33%)</td><td>0.05 <b>(+28.59%)</b></td><td>0.05 <b>(+62.22%)</b></td><td>0.03 <b>(+110.80%)</b></td><td>0.02 <b>(-22.03%)</b></td><td>529.90 <b>(-52.56%)</b></td><td>342.52 <b>(-36.18%)</b></td><td>304.30 <b>(-38.36%)</b></td><td>210.30 (-9.35%)</td><td>118.63 <b>(-66.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1117.10 (n/a)</td><td>536.70 (n/a)</td><td>493.70 (n/a)</td><td>232.00 (n/a)</td><td>349.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 <b>(-21.55%)</b></td><td>0.04 <b>(-24.05%)</b></td><td>0.03 <b>(-40.93%)</b></td><td>0.03 (+9.12%)</td><td>0.01 <b>(-46.24%)</b></td><td>549.20 (-8.36%)</td><td>449.20 <b>(+21.46%)</b></td><td>471.20 <b>(+69.31%)</b></td><td>302.50 <b>(+27.48%)</b></td><td>91.23 <b>(-40.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.30 (n/a)</td><td>369.82 (n/a)</td><td>278.30 (n/a)</td><td>237.30 (n/a)</td><td>153.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(-21.40%)</b></td><td>0.04 <b>(-32.10%)</b></td><td>0.03 <b>(-39.61%)</b></td><td>0.03 <b>(-23.69%)</b></td><td>0.02 (-9.91%)</td><td>612.80 <b>(+31.05%)</b></td><td>479.90 <b>(+51.67%)</b></td><td>513.60 <b>(+65.57%)</b></td><td>234.40 <b>(+27.18%)</b></td><td>146.08 <b>(+44.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>467.60 (n/a)</td><td>316.42 (n/a)</td><td>310.20 (n/a)</td><td>184.30 (n/a)</td><td>101.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 <b>(+40.18%)</b></td><td>0.05 (-10.58%)</td><td>0.03 <b>(-41.70%)</b></td><td>0.03 (-19.24%)</td><td>0.03 <b>(+138.03%)</b></td><td>542.10 <b>(+23.82%)</b></td><td>406.84 <b>(+28.76%)</b></td><td>494.80 <b>(+71.51%)</b></td><td>185.90 <b>(-28.69%)</b></td><td>162.63 <b>(+121.00%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>437.80 (n/a)</td><td>315.96 (n/a)</td><td>288.50 (n/a)</td><td>260.70 (n/a)</td><td>73.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (+18.91%)</td><td>0.10 (-17.90%)</td><td>0.08 <b>(-32.22%)</b></td><td>0.06 <b>(-37.06%)</b></td><td>0.04 <b>(+133.38%)</b></td><td>542.20 <b>(+58.86%)</b></td><td>385.26 <b>(+34.45%)</b></td><td>419.70 <b>(+47.52%)</b></td><td>205.10 (-15.91%)</td><td>131.63 <b>(+209.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>341.30 (n/a)</td><td>286.54 (n/a)</td><td>284.50 (n/a)</td><td>243.90 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (-10.69%)</td><td>0.10 (-17.89%)</td><td>0.10 (-16.41%)</td><td>0.06 (-2.32%)</td><td>0.03 (-17.50%)</td><td>530.00 (+2.38%)</td><td>365.18 (+19.29%)</td><td>317.40 (+19.64%)</td><td>264.70 (+11.97%)</td><td>108.82 (-8.58%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.70 (n/a)</td><td>306.14 (n/a)</td><td>265.30 (n/a)</td><td>236.40 (n/a)</td><td>119.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 <b>(+28.26%)</b></td><td>0.12 <b>(+54.13%)</b></td><td>0.14 <b>(+91.50%)</b></td><td>0.07 <b>(+305.79%)</b></td><td>0.04 (-10.33%)</td><td>460.40 <b>(-75.36%)</b></td><td>293.88 <b>(-56.56%)</b></td><td>230.80 <b>(-47.78%)</b></td><td>192.80 <b>(-22.04%)</b></td><td>114.12 <b>(-83.16%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1868.40 (n/a)</td><td>676.52 (n/a)</td><td>442.00 (n/a)</td><td>247.30 (n/a)</td><td>677.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 <b>(+28.95%)</b></td><td>0.12 <b>(+20.77%)</b></td><td>0.11 (-2.50%)</td><td>0.06 <b>(+276.03%)</b></td><td>0.04 (-10.27%)</td><td>523.50 <b>(-73.41%)</b></td><td>311.92 <b>(-49.45%)</b></td><td>304.30 (+2.56%)</td><td>191.00 <b>(-22.48%)</b></td><td>129.01 <b>(-82.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1968.60 (n/a)</td><td>617.08 (n/a)</td><td>296.70 (n/a)</td><td>246.40 (n/a)</td><td>755.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (-14.54%)</td><td>0.09 (-18.95%)</td><td>0.07 <b>(-34.21%)</b></td><td>0.05 <b>(-22.46%)</b></td><td>0.04 (+17.54%)</td><td>603.70 <b>(+28.97%)</b></td><td>406.22 <b>(+32.81%)</b></td><td>445.30 <b>(+51.98%)</b></td><td>226.00 (+16.98%)</td><td>164.91 <b>(+65.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>468.10 (n/a)</td><td>305.86 (n/a)</td><td>293.00 (n/a)</td><td>193.20 (n/a)</td><td>99.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (-13.20%)</td><td>0.10 (-2.62%)</td><td>0.12 (+15.18%)</td><td>0.06 (-14.45%)</td><td>0.03 (+15.75%)</td><td>528.30 (+16.88%)</td><td>363.24 (+8.35%)</td><td>276.70 (-13.18%)</td><td>247.10 (+15.20%)</td><td>141.91 <b>(+63.06%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>452.00 (n/a)</td><td>335.24 (n/a)</td><td>318.70 (n/a)</td><td>214.50 (n/a)</td><td>87.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 <b>(-21.78%)</b></td><td>0.10 (+2.73%)</td><td>0.11 <b>(+36.65%)</b></td><td>0.07 <b>(+31.70%)</b></td><td>0.03 <b>(-38.03%)</b></td><td>454.40 <b>(-24.08%)</b></td><td>341.62 (-10.30%)</td><td>287.50 <b>(-26.83%)</b></td><td>250.50 <b>(+27.87%)</b></td><td>98.63 <b>(-36.00%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>598.50 (n/a)</td><td>380.86 (n/a)</td><td>392.90 (n/a)</td><td>195.90 (n/a)</td><td>154.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (+2.70%)</td><td>0.11 <b>(+40.75%)</b></td><td>0.11 <b>(+45.22%)</b></td><td>0.10 <b>(+93.42%)</b></td><td>0.00 <b>(-81.04%)</b></td><td>313.10 <b>(-48.30%)</b></td><td>297.18 <b>(-32.73%)</b></td><td>297.00 <b>(-31.15%)</b></td><td>282.30 (-2.62%)</td><td>11.01 <b>(-90.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>441.78 (n/a)</td><td>431.40 (n/a)</td><td>289.90 (n/a)</td><td>113.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(-30.73%)</b></td><td>0.07 <b>(-38.34%)</b></td><td>0.06 <b>(-51.55%)</b></td><td>0.02 (+2.60%)</td><td>0.04 <b>(-35.32%)</b></td><td>1860.60 (-2.54%)</td><td>701.10 <b>(+22.89%)</b></td><td>504.50 <b>(+106.34%)</b></td><td>282.60 <b>(+44.40%)</b></td><td>655.81 (-12.41%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1909.10 (n/a)</td><td>570.52 (n/a)</td><td>244.50 (n/a)</td><td>195.70 (n/a)</td><td>748.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (-15.20%)</td><td>0.08 <b>(-29.25%)</b></td><td>0.07 <b>(-41.65%)</b></td><td>0.06 (+8.16%)</td><td>0.03 <b>(-20.79%)</b></td><td>547.80 (-7.54%)</td><td>460.60 <b>(+36.15%)</b></td><td>501.10 <b>(+71.37%)</b></td><td>273.40 (+17.95%)</td><td>112.75 <b>(-22.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.50 (n/a)</td><td>338.30 (n/a)</td><td>292.40 (n/a)</td><td>231.80 (n/a)</td><td>144.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-37.49%)</b></td><td>0.05 (-17.47%)</td><td>0.06 (+0.04%)</td><td>0.03 <b>(-22.14%)</b></td><td>0.01 <b>(-44.49%)</b></td><td>980.40 <b>(+28.44%)</b></td><td>639.44 (+18.38%)</td><td>556.00 (-0.04%)</td><td>524.30 <b>(+59.95%)</b></td><td>192.89 <b>(+20.32%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>763.30 (n/a)</td><td>540.18 (n/a)</td><td>556.20 (n/a)</td><td>327.80 (n/a)</td><td>160.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (-7.16%)</td><td>0.08 (-1.46%)</td><td>0.09 (+1.00%)</td><td>0.03 <b>(+101.21%)</b></td><td>0.04 (-15.29%)</td><td>1017.40 <b>(-50.30%)</b></td><td>510.30 <b>(-25.93%)</b></td><td>352.00 (-0.98%)</td><td>292.70 (+7.73%)</td><td>309.02 <b>(-59.52%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2047.00 (n/a)</td><td>688.94 (n/a)</td><td>355.50 (n/a)</td><td>271.70 (n/a)</td><td>763.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (-7.25%)</td><td>0.07 <b>(-20.53%)</b></td><td>0.08 (-11.24%)</td><td>0.04 <b>(-47.97%)</b></td><td>0.02 <b>(+88.29%)</b></td><td>580.60 <b>(+92.19%)</b></td><td>367.90 <b>(+35.50%)</b></td><td>316.80 (+12.66%)</td><td>246.20 (+7.84%)</td><td>131.01 <b>(+298.81%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>302.10 (n/a)</td><td>271.52 (n/a)</td><td>281.20 (n/a)</td><td>228.30 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 <b>(-23.34%)</b></td><td>0.15 (-11.80%)</td><td>0.16 <b>(-20.95%)</b></td><td>0.11 (+17.99%)</td><td>0.02 <b>(-65.71%)</b></td><td>427.70 (-15.26%)</td><td>343.12 (+2.95%)</td><td>315.00 <b>(+26.51%)</b></td><td>303.90 <b>(+30.43%)</b></td><td>51.15 <b>(-60.90%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>504.70 (n/a)</td><td>333.30 (n/a)</td><td>249.00 (n/a)</td><td>233.00 (n/a)</td><td>130.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.33 (+0.89%)</td><td>3.52 (+3.69%)</td><td>3.75 (+15.15%)</td><td>2.65 (+2.29%)</td><td>0.68 (-0.96%)</td><td>3963.60 (-2.24%)</td><td>3073.22 (-3.65%)</td><td>2795.20 (-13.16%)</td><td>2423.30 (-0.88%)</td><td>629.52 (-1.98%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.29 (n/a)</td><td>3.40 (n/a)</td><td>3.26 (n/a)</td><td>2.59 (n/a)</td><td>0.69 (n/a)</td><td>4054.40 (n/a)</td><td>3189.52 (n/a)</td><td>3218.80 (n/a)</td><td>2444.90 (n/a)</td><td>642.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 (-13.12%)</td><td>0.11 <b>(-22.74%)</b></td><td>0.14 (-10.25%)</td><td>0.07 <b>(-35.61%)</b></td><td>0.04 <b>(+52.68%)</b></td><td>592.00 <b>(+55.30%)</b></td><td>404.66 <b>(+40.30%)</b></td><td>300.70 (+11.41%)</td><td>279.30 (+15.08%)</td><td>154.10 <b>(+173.98%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>381.20 (n/a)</td><td>288.42 (n/a)</td><td>269.90 (n/a)</td><td>242.70 (n/a)</td><td>56.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-15.91%)</td><td>0.02 (-13.90%)</td><td>0.02 (-17.77%)</td><td>0.01 (+8.83%)</td><td>0.00 <b>(-34.86%)</b></td><td>537.20 (-8.12%)</td><td>352.38 (+9.12%)</td><td>302.40 <b>(+21.59%)</b></td><td>268.70 (+18.95%)</td><td>107.63 <b>(-28.27%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.70 (n/a)</td><td>322.94 (n/a)</td><td>248.70 (n/a)</td><td>225.90 (n/a)</td><td>150.05 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (+2.04%)</td><td>0.01 (+15.31%)</td><td>0.01 <b>(+34.63%)</b></td><td>0.01 (-2.62%)</td><td>0.00 (+0.12%)</td><td>529.10 (+2.70%)</td><td>342.02 (-13.35%)</td><td>281.70 <b>(-25.71%)</b></td><td>275.20 (-1.99%)</td><td>108.90 (-1.24%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.20 (n/a)</td><td>394.70 (n/a)</td><td>379.20 (n/a)</td><td>280.80 (n/a)</td><td>110.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-9.43%)</td><td>0.02 (-9.84%)</td><td>0.02 (-17.66%)</td><td>0.01 (+5.42%)</td><td>0.01 <b>(-21.75%)</b></td><td>507.10 (-5.14%)</td><td>322.16 (+6.75%)</td><td>297.50 <b>(+21.43%)</b></td><td>239.00 (+10.39%)</td><td>107.54 (-18.82%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.60 (n/a)</td><td>301.80 (n/a)</td><td>245.00 (n/a)</td><td>216.50 (n/a)</td><td>132.47 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+6.63%)</td><td>0.01 (+10.23%)</td><td>0.01 (+6.95%)</td><td>0.01 (+10.94%)</td><td>0.01 (+2.83%)</td><td>535.90 (-9.86%)</td><td>374.38 (-11.31%)</td><td>440.20 (-6.50%)</td><td>178.40 (-6.25%)</td><td>146.28 (-15.88%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>422.10 (n/a)</td><td>470.80 (n/a)</td><td>190.30 (n/a)</td><td>173.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-21.87%)</b></td><td>0.01 (-11.17%)</td><td>0.02 (+15.17%)</td><td>0.01 (-12.42%)</td><td>0.00 <b>(-25.11%)</b></td><td>539.90 (+14.19%)</td><td>384.40 (+10.66%)</td><td>304.90 (-13.16%)</td><td>267.80 <b>(+28.01%)</b></td><td>135.71 (+10.45%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>347.36 (n/a)</td><td>351.10 (n/a)</td><td>209.20 (n/a)</td><td>122.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+0.06%)</td><td>0.01 (-15.35%)</td><td>0.01 <b>(-29.69%)</b></td><td>0.01 <b>(-20.47%)</b></td><td>0.00 <b>(+40.31%)</b></td><td>659.80 <b>(+25.75%)</b></td><td>442.70 <b>(+30.13%)</b></td><td>412.50 <b>(+42.24%)</b></td><td>242.30 (-0.08%)</td><td>196.12 <b>(+74.47%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.70 (n/a)</td><td>340.20 (n/a)</td><td>290.00 (n/a)</td><td>242.50 (n/a)</td><td>112.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 <b>(-40.66%)</b></td><td>0.01 <b>(-35.05%)</b></td><td>0.01 <b>(-37.99%)</b></td><td>0.01 (+3.19%)</td><td>0.00 <b>(-72.83%)</b></td><td>569.70 (-3.10%)</td><td>521.04 <b>(+43.17%)</b></td><td>548.90 <b>(+61.25%)</b></td><td>431.80 <b>(+68.47%)</b></td><td>56.16 <b>(-57.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.90 (n/a)</td><td>363.94 (n/a)</td><td>340.40 (n/a)</td><td>256.30 (n/a)</td><td>131.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (-6.56%)</td><td>0.01 (+18.50%)</td><td>0.01 <b>(+21.52%)</b></td><td>0.01 <b>(+24.56%)</b></td><td>0.00 <b>(-36.03%)</b></td><td>399.30 (-19.71%)</td><td>302.66 (-19.07%)</td><td>276.00 (-17.71%)</td><td>264.70 (+7.04%)</td><td>56.12 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.30 (n/a)</td><td>373.96 (n/a)</td><td>335.40 (n/a)</td><td>247.30 (n/a)</td><td>104.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(+31.91%)</b></td><td>0.01 <b>(+28.71%)</b></td><td>0.01 <b>(+29.02%)</b></td><td>0.01 <b>(+31.06%)</b></td><td>0.00 <b>(+29.88%)</b></td><td>608.30 <b>(-23.70%)</b></td><td>385.28 <b>(-22.43%)</b></td><td>343.60 <b>(-22.51%)</b></td><td>261.10 <b>(-24.19%)</b></td><td>138.75 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>797.20 (n/a)</td><td>496.66 (n/a)</td><td>443.40 (n/a)</td><td>344.40 (n/a)</td><td>183.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(+26.75%)</b></td><td>0.01 (+11.35%)</td><td>0.01 (+2.06%)</td><td>0.01 (-18.96%)</td><td>0.01 <b>(+54.34%)</b></td><td>797.80 <b>(+23.40%)</b></td><td>465.68 (-0.12%)</td><td>514.30 (-2.00%)</td><td>236.00 <b>(-21.12%)</b></td><td>228.81 <b>(+48.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>646.50 (n/a)</td><td>466.24 (n/a)</td><td>524.80 (n/a)</td><td>299.20 (n/a)</td><td>154.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+0.11%)</td><td>0.01 (-9.11%)</td><td>0.01 (-18.95%)</td><td>0.01 (-9.63%)</td><td>0.00 (+9.09%)</td><td>605.10 (+10.64%)</td><td>428.86 (+12.83%)</td><td>386.10 <b>(+23.39%)</b></td><td>278.70 (-0.11%)</td><td>152.13 <b>(+24.63%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.90 (n/a)</td><td>380.08 (n/a)</td><td>312.90 (n/a)</td><td>279.00 (n/a)</td><td>122.06 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (+4.72%)</td><td>0.01 (-1.21%)</td><td>0.01 (+9.61%)</td><td>0.01 (+5.92%)</td><td>0.00 (-12.41%)</td><td>583.40 (-5.58%)</td><td>476.06 (-0.70%)</td><td>489.10 (-8.78%)</td><td>319.90 (-4.51%)</td><td>97.17 <b>(-22.39%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.90 (n/a)</td><td>479.42 (n/a)</td><td>536.20 (n/a)</td><td>335.00 (n/a)</td><td>125.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 <b>(-20.58%)</b></td><td>0.03 <b>(+23.46%)</b></td><td>0.03 <b>(+72.78%)</b></td><td>0.02 <b>(+74.41%)</b></td><td>0.00 <b>(-69.16%)</b></td><td>343.70 <b>(-42.67%)</b></td><td>298.12 <b>(-30.76%)</b></td><td>279.60 <b>(-42.12%)</b></td><td>261.40 <b>(+25.92%)</b></td><td>38.18 <b>(-78.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.50 (n/a)</td><td>430.54 (n/a)</td><td>483.10 (n/a)</td><td>207.60 (n/a)</td><td>174.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 <b>(+43.85%)</b></td><td>0.03 <b>(+32.08%)</b></td><td>0.03 (+0.06%)</td><td>0.02 <b>(+27.86%)</b></td><td>0.01 <b>(+70.69%)</b></td><td>516.50 <b>(-21.79%)</b></td><td>401.76 <b>(-21.49%)</b></td><td>472.50 (-0.06%)</td><td>225.70 <b>(-30.49%)</b></td><td>126.11 (-7.14%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.40 (n/a)</td><td>511.70 (n/a)</td><td>472.80 (n/a)</td><td>324.70 (n/a)</td><td>135.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 <b>(-22.00%)</b></td><td>0.02 <b>(-26.82%)</b></td><td>0.01 <b>(-43.00%)</b></td><td>0.01 (-19.18%)</td><td>0.01 (-8.78%)</td><td>599.10 <b>(+23.73%)</b></td><td>451.22 <b>(+43.19%)</b></td><td>550.60 <b>(+75.41%)</b></td><td>231.40 <b>(+28.20%)</b></td><td>178.54 <b>(+52.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.20 (n/a)</td><td>315.12 (n/a)</td><td>313.90 (n/a)</td><td>180.50 (n/a)</td><td>117.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (+0.22%)</td><td>0.03 <b>(+20.24%)</b></td><td>0.03 <b>(+66.29%)</b></td><td>0.02 (+16.67%)</td><td>0.01 (-12.51%)</td><td>560.10 (-14.28%)</td><td>366.52 <b>(-20.95%)</b></td><td>317.50 <b>(-39.86%)</b></td><td>227.80 (-0.22%)</td><td>137.57 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>653.40 (n/a)</td><td>463.64 (n/a)</td><td>527.90 (n/a)</td><td>228.30 (n/a)</td><td>181.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-4.40%)</td><td>0.02 (-4.61%)</td><td>0.03 (-3.43%)</td><td>0.01 (-10.60%)</td><td>0.01 (+6.08%)</td><td>672.40 (+11.86%)</td><td>384.40 (+7.86%)</td><td>308.50 (+3.56%)</td><td>246.10 (+4.59%)</td><td>178.42 <b>(+20.05%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.10 (n/a)</td><td>356.38 (n/a)</td><td>297.90 (n/a)</td><td>235.30 (n/a)</td><td>148.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (-11.55%)</td><td>0.02 (-4.23%)</td><td>0.02 (-10.73%)</td><td>0.02 (-3.65%)</td><td>0.01 (-18.72%)</td><td>602.80 (+3.79%)</td><td>472.70 (+2.59%)</td><td>512.70 (+12.02%)</td><td>289.10 (+13.06%)</td><td>123.57 (-3.56%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.80 (n/a)</td><td>460.78 (n/a)</td><td>457.70 (n/a)</td><td>255.70 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (+6.50%)</td><td>0.02 (-17.99%)</td><td>0.02 <b>(-27.30%)</b></td><td>0.01 (-19.98%)</td><td>0.01 (+14.21%)</td><td>601.80 <b>(+24.98%)</b></td><td>460.16 <b>(+26.02%)</b></td><td>492.70 <b>(+37.55%)</b></td><td>232.70 (-6.09%)</td><td>145.03 <b>(+27.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.50 (n/a)</td><td>365.16 (n/a)</td><td>358.20 (n/a)</td><td>247.80 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (-13.43%)</td><td>0.02 (-12.27%)</td><td>0.02 (-0.64%)</td><td>0.02 (+15.03%)</td><td>0.01 <b>(-34.81%)</b></td><td>579.00 (-13.06%)</td><td>470.68 (+4.30%)</td><td>500.00 (+0.64%)</td><td>275.10 (+15.54%)</td><td>115.10 <b>(-37.23%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.00 (n/a)</td><td>451.28 (n/a)</td><td>496.80 (n/a)</td><td>238.10 (n/a)</td><td>183.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-22.22%)</b></td><td>0.02 (-6.07%)</td><td>0.02 (-6.06%)</td><td>0.02 (+8.21%)</td><td>0.00 <b>(-54.01%)</b></td><td>485.00 (-7.58%)</td><td>435.60 (+2.49%)</td><td>459.60 (+6.44%)</td><td>348.20 <b>(+28.58%)</b></td><td>53.86 <b>(-43.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.80 (n/a)</td><td>425.00 (n/a)</td><td>431.80 (n/a)</td><td>270.80 (n/a)</td><td>95.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 <b>(-36.91%)</b></td><td>0.02 <b>(-40.09%)</b></td><td>0.02 <b>(-21.34%)</b></td><td>0.00 <b>(-69.13%)</b></td><td>0.01 <b>(-27.46%)</b></td><td>1938.10 <b>(+223.99%)</b></td><td>798.32 <b>(+103.91%)</b></td><td>534.70 <b>(+27.13%)</b></td><td>393.20 <b>(+58.48%)</b></td><td>643.04 <b>(+345.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>391.50 (n/a)</td><td>420.60 (n/a)</td><td>248.10 (n/a)</td><td>144.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 <b>(+80.75%)</b></td><td>0.03 <b>(+63.78%)</b></td><td>0.03 <b>(+94.20%)</b></td><td>0.01 <b>(+138.88%)</b></td><td>0.01 <b>(+70.41%)</b></td><td>563.00 <b>(-58.14%)</b></td><td>376.30 <b>(-42.24%)</b></td><td>297.30 <b>(-48.50%)</b></td><td>190.90 <b>(-44.67%)</b></td><td>165.92 <b>(-58.78%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1345.00 (n/a)</td><td>651.52 (n/a)</td><td>577.30 (n/a)</td><td>345.00 (n/a)</td><td>402.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 <b>(+65.85%)</b></td><td>0.05 (-5.40%)</td><td>0.03 <b>(-47.52%)</b></td><td>0.03 (-17.13%)</td><td>0.03 <b>(+167.40%)</b></td><td>557.40 <b>(+20.68%)</b></td><td>394.66 <b>(+27.75%)</b></td><td>496.90 <b>(+90.53%)</b></td><td>154.70 <b>(-39.71%)</b></td><td>176.96 <b>(+100.42%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.90 (n/a)</td><td>308.94 (n/a)</td><td>260.80 (n/a)</td><td>256.60 (n/a)</td><td>88.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 <b>(+54.30%)</b></td><td>0.08 (+16.39%)</td><td>0.08 (+2.82%)</td><td>0.05 (-3.46%)</td><td>0.04 <b>(+102.06%)</b></td><td>538.80 (+3.58%)</td><td>368.28 (-5.11%)</td><td>319.10 (-2.74%)</td><td>188.50 <b>(-35.20%)</b></td><td>157.37 <b>(+43.74%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>520.20 (n/a)</td><td>388.10 (n/a)</td><td>328.10 (n/a)</td><td>290.90 (n/a)</td><td>109.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+1.11%)</td><td>0.04 <b>(-23.10%)</b></td><td>0.03 <b>(-44.17%)</b></td><td>0.03 <b>(-32.73%)</b></td><td>0.02 <b>(+67.76%)</b></td><td>651.70 <b>(+48.65%)</b></td><td>461.02 <b>(+44.51%)</b></td><td>536.00 <b>(+79.14%)</b></td><td>246.10 (-1.09%)</td><td>176.19 <b>(+138.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.40 (n/a)</td><td>319.02 (n/a)</td><td>299.20 (n/a)</td><td>248.80 (n/a)</td><td>73.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-46.73%)</b></td><td>0.05 <b>(-24.87%)</b></td><td>0.05 (+1.06%)</td><td>0.04 (-6.50%)</td><td>0.01 <b>(-76.20%)</b></td><td>500.20 (+6.95%)</td><td>435.00 (+18.54%)</td><td>432.80 (-1.05%)</td><td>349.50 <b>(+87.70%)</b></td><td>58.06 <b>(-54.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>467.70 (n/a)</td><td>366.98 (n/a)</td><td>437.40 (n/a)</td><td>186.20 (n/a)</td><td>127.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-9.58%)</td><td>0.04 (-9.43%)</td><td>0.04 (-6.52%)</td><td>0.04 <b>(+23.64%)</b></td><td>0.01 <b>(-34.38%)</b></td><td>463.90 (-19.11%)</td><td>393.38 (+4.25%)</td><td>426.10 (+6.98%)</td><td>267.10 (+10.60%)</td><td>82.16 <b>(-38.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.50 (n/a)</td><td>377.36 (n/a)</td><td>398.30 (n/a)</td><td>241.50 (n/a)</td><td>133.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (+15.82%)</td><td>0.04 (-2.25%)</td><td>0.04 (+0.33%)</td><td>0.03 <b>(-26.67%)</b></td><td>0.02 <b>(+46.42%)</b></td><td>795.40 <b>(+36.39%)</b></td><td>531.72 (+11.22%)</td><td>528.10 (-0.32%)</td><td>240.60 (-13.67%)</td><td>198.03 <b>(+64.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>583.20 (n/a)</td><td>478.06 (n/a)</td><td>529.80 (n/a)</td><td>278.70 (n/a)</td><td>120.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (+11.21%)</td><td>0.05 (-5.16%)</td><td>0.04 <b>(-27.67%)</b></td><td>0.03 (-3.45%)</td><td>0.02 (+16.28%)</td><td>569.30 (+3.58%)</td><td>406.28 (+6.76%)</td><td>431.40 <b>(+38.22%)</b></td><td>211.60 (-10.07%)</td><td>136.42 (-1.03%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>549.60 (n/a)</td><td>380.56 (n/a)</td><td>312.10 (n/a)</td><td>235.30 (n/a)</td><td>137.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(+33.10%)</b></td><td>0.05 (+6.44%)</td><td>0.04 (-8.12%)</td><td>0.04 (-10.08%)</td><td>0.02 <b>(+153.44%)</b></td><td>524.70 (+11.19%)</td><td>416.22 (-0.19%)</td><td>475.90 (+8.83%)</td><td>268.30 <b>(-24.87%)</b></td><td>117.71 <b>(+117.38%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.90 (n/a)</td><td>417.00 (n/a)</td><td>437.30 (n/a)</td><td>357.10 (n/a)</td><td>54.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 <b>(+25.37%)</b></td><td>0.05 <b>(+37.09%)</b></td><td>0.04 <b>(+25.91%)</b></td><td>0.03 <b>(+28.14%)</b></td><td>0.02 <b>(+33.68%)</b></td><td>489.70 <b>(-21.96%)</b></td><td>376.06 <b>(-26.30%)</b></td><td>438.30 <b>(-20.57%)</b></td><td>237.70 <b>(-20.23%)</b></td><td>111.71 (-14.78%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.50 (n/a)</td><td>510.26 (n/a)</td><td>551.80 (n/a)</td><td>298.00 (n/a)</td><td>131.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-11.80%)</td><td>0.04 (-10.36%)</td><td>0.03 <b>(-23.32%)</b></td><td>0.02 <b>(-23.52%)</b></td><td>0.02 (+17.28%)</td><td>790.50 <b>(+30.75%)</b></td><td>528.24 <b>(+20.42%)</b></td><td>583.00 <b>(+30.43%)</b></td><td>292.80 (+13.40%)</td><td>214.50 <b>(+74.73%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.60 (n/a)</td><td>438.66 (n/a)</td><td>447.00 (n/a)</td><td>258.20 (n/a)</td><td>122.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+9.41%)</td><td>0.05 <b>(+51.88%)</b></td><td>0.05 <b>(+52.64%)</b></td><td>0.04 <b>(+333.98%)</b></td><td>0.01 <b>(-40.00%)</b></td><td>434.40 <b>(-76.96%)</b></td><td>315.86 <b>(-55.67%)</b></td><td>306.10 <b>(-34.48%)</b></td><td>226.80 (-8.59%)</td><td>74.64 <b>(-88.75%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1885.10 (n/a)</td><td>712.54 (n/a)</td><td>467.20 (n/a)</td><td>248.10 (n/a)</td><td>663.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (-11.74%)</td><td>0.13 (+9.32%)</td><td>0.13 <b>(+23.41%)</b></td><td>0.11 <b>(+96.03%)</b></td><td>0.01 <b>(-72.44%)</b></td><td>287.30 <b>(-48.99%)</b></td><td>257.98 (-19.99%)</td><td>259.10 (-18.98%)</td><td>226.20 (+13.33%)</td><td>24.27 <b>(-83.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>563.20 (n/a)</td><td>322.42 (n/a)</td><td>319.80 (n/a)</td><td>199.60 (n/a)</td><td>147.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (-5.85%)</td><td>0.11 (+6.87%)</td><td>0.12 (-6.75%)</td><td>0.06 (+7.31%)</td><td>0.03 <b>(-26.65%)</b></td><td>552.60 (-6.81%)</td><td>327.42 (-12.06%)</td><td>283.90 (+7.25%)</td><td>254.80 (+6.21%)</td><td>126.81 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>593.00 (n/a)</td><td>372.34 (n/a)</td><td>264.70 (n/a)</td><td>239.90 (n/a)</td><td>166.90 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 <b>(+20.19%)</b></td><td>0.13 <b>(+21.81%)</b></td><td>0.13 <b>(+49.35%)</b></td><td>0.08 (+3.34%)</td><td>0.04 <b>(+56.64%)</b></td><td>498.90 (-3.22%)</td><td>356.52 (-13.41%)</td><td>303.50 <b>(-33.03%)</b></td><td>236.00 (-16.81%)</td><td>131.76 <b>(+31.94%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>515.50 (n/a)</td><td>411.72 (n/a)</td><td>453.20 (n/a)</td><td>283.70 (n/a)</td><td>99.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (+16.01%)</td><td>0.07 (-5.03%)</td><td>0.07 (-4.57%)</td><td>0.01 <b>(-76.58%)</b></td><td>0.04 <b>(+97.24%)</b></td><td>2393.20 <b>(+327.05%)</b></td><td>811.64 <b>(+76.22%)</b></td><td>496.60 (+4.79%)</td><td>252.90 (-13.77%)</td><td>890.34 <b>(+788.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>560.40 (n/a)</td><td>460.58 (n/a)</td><td>473.90 (n/a)</td><td>293.30 (n/a)</td><td>100.16 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(-22.95%)</b></td><td>0.08 (-14.57%)</td><td>0.08 (-3.44%)</td><td>0.07 (-0.51%)</td><td>0.01 <b>(-52.56%)</b></td><td>568.00 (+0.51%)</td><td>508.76 (+13.17%)</td><td>518.30 (+3.56%)</td><td>407.10 <b>(+29.77%)</b></td><td>65.49 <b>(-37.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>565.10 (n/a)</td><td>449.54 (n/a)</td><td>500.50 (n/a)</td><td>313.70 (n/a)</td><td>104.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 <b>(+80.73%)</b></td><td>0.10 <b>(+76.65%)</b></td><td>0.10 <b>(+78.30%)</b></td><td>0.08 <b>(+67.72%)</b></td><td>0.02 <b>(+111.04%)</b></td><td>436.00 <b>(-40.38%)</b></td><td>326.82 <b>(-42.77%)</b></td><td>316.20 <b>(-43.91%)</b></td><td>254.80 <b>(-44.67%)</b></td><td>71.04 <b>(-30.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>731.30 (n/a)</td><td>571.10 (n/a)</td><td>563.70 (n/a)</td><td>460.50 (n/a)</td><td>102.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (+0.56%)</td><td>0.10 (+15.63%)</td><td>0.09 <b>(+21.13%)</b></td><td>0.06 (-0.24%)</td><td>0.03 (-1.27%)</td><td>606.50 (+0.23%)</td><td>412.72 (-13.55%)</td><td>405.70 (-17.44%)</td><td>289.50 (-0.55%)</td><td>123.51 (+1.11%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>605.10 (n/a)</td><td>477.42 (n/a)</td><td>491.40 (n/a)</td><td>291.10 (n/a)</td><td>122.16 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 <b>(+47.53%)</b></td><td>0.10 <b>(+21.32%)</b></td><td>0.07 (-3.44%)</td><td>0.06 (+8.75%)</td><td>0.05 <b>(+80.38%)</b></td><td>531.10 (-8.03%)</td><td>373.28 (-10.78%)</td><td>451.00 (+3.56%)</td><td>192.60 <b>(-32.21%)</b></td><td>148.19 (+16.36%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>577.50 (n/a)</td><td>418.38 (n/a)</td><td>435.50 (n/a)</td><td>284.10 (n/a)</td><td>127.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 <b>(-42.40%)</b></td><td>0.09 <b>(-22.34%)</b></td><td>0.08 <b>(-26.23%)</b></td><td>0.07 <b>(+31.23%)</b></td><td>0.03 <b>(-61.66%)</b></td><td>530.00 <b>(-23.80%)</b></td><td>448.72 (+4.05%)</td><td>486.20 <b>(+35.55%)</b></td><td>264.60 <b>(+73.62%)</b></td><td>105.02 <b>(-51.34%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.08 (n/a)</td><td>695.50 (n/a)</td><td>431.26 (n/a)</td><td>358.70 (n/a)</td><td>152.40 (n/a)</td><td>215.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (+13.74%)</td><td>0.08 (+0.71%)</td><td>0.09 (+14.67%)</td><td>0.02 <b>(-71.89%)</b></td><td>0.04 <b>(+136.64%)</b></td><td>1838.60 <b>(+255.77%)</b></td><td>641.10 <b>(+52.75%)</b></td><td>367.90 (-12.78%)</td><td>292.60 (-12.08%)</td><td>670.18 <b>(+736.85%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>516.80 (n/a)</td><td>419.70 (n/a)</td><td>421.80 (n/a)</td><td>332.80 (n/a)</td><td>80.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-26.48%)</b></td><td>0.05 (-14.90%)</td><td>0.04 <b>(-38.35%)</b></td><td>0.04 <b>(+274.01%)</b></td><td>0.01 <b>(-67.68%)</b></td><td>534.80 <b>(-73.27%)</b></td><td>440.34 <b>(-33.12%)</b></td><td>467.00 <b>(+62.21%)</b></td><td>332.10 <b>(+36.00%)</b></td><td>83.66 <b>(-88.93%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2000.40 (n/a)</td><td>658.42 (n/a)</td><td>287.90 (n/a)</td><td>244.20 (n/a)</td><td>756.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 <b>(+23.98%)</b></td><td>0.06 (+9.02%)</td><td>0.05 (+4.65%)</td><td>0.04 (-5.08%)</td><td>0.02 <b>(+63.06%)</b></td><td>504.50 (+5.35%)</td><td>372.28 (-3.10%)</td><td>408.60 (-4.47%)</td><td>225.80 (-19.33%)</td><td>122.92 <b>(+40.04%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>478.90 (n/a)</td><td>384.18 (n/a)</td><td>427.70 (n/a)</td><td>279.90 (n/a)</td><td>87.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 <b>(+20.23%)</b></td><td>0.06 <b>(+50.37%)</b></td><td>0.06 <b>(+51.11%)</b></td><td>0.04 <b>(+294.79%)</b></td><td>0.02 (-15.38%)</td><td>480.30 <b>(-74.67%)</b></td><td>358.50 <b>(-51.56%)</b></td><td>335.70 <b>(-33.83%)</b></td><td>237.40 (-16.82%)</td><td>104.87 <b>(-83.95%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1896.30 (n/a)</td><td>740.14 (n/a)</td><td>507.30 (n/a)</td><td>285.40 (n/a)</td><td>653.37 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+5.82%)</td><td>0.05 (-9.99%)</td><td>0.05 <b>(-33.68%)</b></td><td>0.04 <b>(+77.12%)</b></td><td>0.02 (-13.68%)</td><td>583.10 <b>(-43.54%)</b></td><td>431.14 (-3.83%)</td><td>452.10 <b>(+50.80%)</b></td><td>282.40 (-5.49%)</td><td>143.31 <b>(-56.14%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1032.80 (n/a)</td><td>448.30 (n/a)</td><td>299.80 (n/a)</td><td>298.80 (n/a)</td><td>326.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(+62.38%)</b></td><td>0.05 (+6.40%)</td><td>0.04 (-17.11%)</td><td>0.03 <b>(-26.78%)</b></td><td>0.04 <b>(+161.57%)</b></td><td>766.70 <b>(+36.57%)</b></td><td>481.40 (+14.41%)</td><td>518.50 <b>(+20.64%)</b></td><td>172.90 <b>(-38.43%)</b></td><td>219.05 <b>(+105.50%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>420.78 (n/a)</td><td>429.80 (n/a)</td><td>280.80 (n/a)</td><td>106.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 <b>(-21.70%)</b></td><td>0.05 (-12.40%)</td><td>0.04 (+9.23%)</td><td>0.04 (+18.83%)</td><td>0.01 <b>(-45.88%)</b></td><td>510.10 (-15.85%)</td><td>440.26 (+1.88%)</td><td>482.30 (-8.46%)</td><td>271.40 <b>(+27.72%)</b></td><td>97.82 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>606.20 (n/a)</td><td>432.12 (n/a)</td><td>526.90 (n/a)</td><td>212.50 (n/a)</td><td>174.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (-3.57%)</td><td>0.08 (-7.88%)</td><td>0.09 (-2.28%)</td><td>0.05 <b>(-37.00%)</b></td><td>0.02 <b>(+90.79%)</b></td><td>513.50 <b>(+58.73%)</b></td><td>320.00 (+15.33%)</td><td>282.50 (+2.36%)</td><td>241.00 (+3.70%)</td><td>111.08 <b>(+228.53%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>323.50 (n/a)</td><td>277.46 (n/a)</td><td>276.00 (n/a)</td><td>232.40 (n/a)</td><td>33.81 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(+68.32%)</b></td><td>0.08 <b>(+66.16%)</b></td><td>0.08 <b>(+64.79%)</b></td><td>0.05 <b>(+22.23%)</b></td><td>0.02 <b>(+101.80%)</b></td><td>520.30 (-18.18%)</td><td>323.62 <b>(-37.28%)</b></td><td>296.50 <b>(-39.32%)</b></td><td>212.10 <b>(-40.59%)</b></td><td>115.86 (+2.77%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>635.90 (n/a)</td><td>515.94 (n/a)</td><td>488.60 (n/a)</td><td>357.00 (n/a)</td><td>112.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(-21.86%)</b></td><td>0.07 (+4.15%)</td><td>0.05 (+7.10%)</td><td>0.04 <b>(+75.70%)</b></td><td>0.03 <b>(-27.72%)</b></td><td>628.60 <b>(-43.08%)</b></td><td>417.66 <b>(-20.68%)</b></td><td>461.00 (-6.64%)</td><td>240.50 <b>(+27.93%)</b></td><td>170.96 <b>(-51.66%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1104.40 (n/a)</td><td>526.58 (n/a)</td><td>493.80 (n/a)</td><td>188.00 (n/a)</td><td>353.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (-15.35%)</td><td>0.08 <b>(+27.49%)</b></td><td>0.09 <b>(+74.44%)</b></td><td>0.05 <b>(+292.66%)</b></td><td>0.02 <b>(-49.55%)</b></td><td>466.30 <b>(-74.53%)</b></td><td>342.20 <b>(-50.74%)</b></td><td>287.50 <b>(-42.67%)</b></td><td>260.10 (+18.12%)</td><td>97.34 <b>(-85.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1831.10 (n/a)</td><td>694.68 (n/a)</td><td>501.50 (n/a)</td><td>220.20 (n/a)</td><td>656.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 (+2.47%)</td><td>0.06 (-19.91%)</td><td>0.05 (-14.15%)</td><td>0.01 <b>(-75.00%)</b></td><td>0.05 <b>(+33.64%)</b></td><td>1845.40 <b>(+299.96%)</b></td><td>702.34 <b>(+92.84%)</b></td><td>484.60 (+16.49%)</td><td>168.80 (-2.37%)</td><td>655.06 <b>(+472.67%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>461.40 (n/a)</td><td>364.20 (n/a)</td><td>416.00 (n/a)</td><td>172.90 (n/a)</td><td>114.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (-12.20%)</td><td>0.07 (+1.06%)</td><td>0.07 <b>(+34.32%)</b></td><td>0.05 (+17.88%)</td><td>0.01 <b>(-45.56%)</b></td><td>487.20 (-15.17%)</td><td>384.70 (-9.11%)</td><td>370.30 <b>(-25.55%)</b></td><td>288.90 (+13.92%)</td><td>84.35 <b>(-44.61%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>574.30 (n/a)</td><td>423.28 (n/a)</td><td>497.40 (n/a)</td><td>253.60 (n/a)</td><td>152.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (+7.56%)</td><td>0.05 (+12.19%)</td><td>0.05 <b>(+23.30%)</b></td><td>0.03 (-11.43%)</td><td>0.02 <b>(+44.80%)</b></td><td>678.80 (+12.89%)</td><td>425.10 (-2.83%)</td><td>335.50 (-18.90%)</td><td>250.80 (-7.04%)</td><td>193.54 <b>(+57.42%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>601.30 (n/a)</td><td>437.46 (n/a)</td><td>413.70 (n/a)</td><td>269.80 (n/a)</td><td>122.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(-28.94%)</b></td><td>0.04 <b>(-28.69%)</b></td><td>0.04 <b>(-28.68%)</b></td><td>0.03 <b>(-21.99%)</b></td><td>0.01 <b>(-38.27%)</b></td><td>623.40 <b>(+28.19%)</b></td><td>483.04 <b>(+36.26%)</b></td><td>490.00 <b>(+40.20%)</b></td><td>307.10 <b>(+40.74%)</b></td><td>118.93 (+6.64%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>486.30 (n/a)</td><td>354.50 (n/a)</td><td>349.50 (n/a)</td><td>218.20 (n/a)</td><td>111.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (-10.03%)</td><td>0.04 (-4.96%)</td><td>0.03 (-6.20%)</td><td>0.01 <b>(-57.13%)</b></td><td>0.02 <b>(+30.40%)</b></td><td>1341.20 <b>(+133.25%)</b></td><td>599.64 <b>(+31.70%)</b></td><td>527.40 (+6.61%)</td><td>282.60 (+11.13%)</td><td>432.31 <b>(+252.10%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.00 (n/a)</td><td>455.32 (n/a)</td><td>494.70 (n/a)</td><td>254.30 (n/a)</td><td>122.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 <b>(-41.54%)</b></td><td>0.04 <b>(-31.56%)</b></td><td>0.04 <b>(-26.83%)</b></td><td>0.02 <b>(-49.85%)</b></td><td>0.01 <b>(-34.54%)</b></td><td>999.10 <b>(+99.42%)</b></td><td>544.36 <b>(+52.62%)</b></td><td>475.70 <b>(+36.66%)</b></td><td>367.50 <b>(+71.01%)</b></td><td>259.76 <b>(+136.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.00 (n/a)</td><td>356.68 (n/a)</td><td>348.10 (n/a)</td><td>214.90 (n/a)</td><td>109.91 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (-0.03%)</td><td>0.05 (-12.39%)</td><td>0.04 <b>(-38.32%)</b></td><td>0.03 (-4.47%)</td><td>0.02 (+2.29%)</td><td>573.20 (+4.67%)</td><td>424.30 (+15.09%)</td><td>455.10 <b>(+62.13%)</b></td><td>246.10 (+0.04%)</td><td>149.13 (+6.58%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.60 (n/a)</td><td>368.68 (n/a)</td><td>280.70 (n/a)</td><td>246.00 (n/a)</td><td>139.92 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 <b>(+33.29%)</b></td><td>0.04 (+11.21%)</td><td>0.04 (+16.64%)</td><td>0.03 (-14.90%)</td><td>0.01 <b>(+91.53%)</b></td><td>674.80 (+17.50%)</td><td>474.78 (-4.79%)</td><td>471.00 (-14.27%)</td><td>292.90 <b>(-24.96%)</b></td><td>150.26 <b>(+66.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>498.66 (n/a)</td><td>549.40 (n/a)</td><td>390.30 (n/a)</td><td>90.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.33 (-7.83%)</td><td>0.26 (+9.46%)</td><td>0.30 <b>(+30.95%)</b></td><td>0.16 (+12.61%)</td><td>0.07 <b>(-23.47%)</b></td><td>598.20 (-11.19%)</td><td>398.50 (-13.31%)</td><td>330.50 <b>(-23.62%)</b></td><td>300.40 (+8.53%)</td><td>127.70 <b>(-27.64%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>673.60 (n/a)</td><td>459.66 (n/a)</td><td>432.70 (n/a)</td><td>276.80 (n/a)</td><td>176.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.23 <b>(-35.41%)</b></td><td>0.20 <b>(-33.95%)</b></td><td>0.21 <b>(-40.15%)</b></td><td>0.14 <b>(-27.21%)</b></td><td>0.04 <b>(-48.15%)</b></td><td>716.60 <b>(+37.36%)</b></td><td>511.14 <b>(+47.58%)</b></td><td>468.70 <b>(+67.09%)</b></td><td>424.40 <b>(+54.83%)</b></td><td>121.45 (+13.33%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>521.70 (n/a)</td><td>346.34 (n/a)</td><td>280.50 (n/a)</td><td>274.10 (n/a)</td><td>107.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.59 <b>(+70.39%)</b></td><td>0.28 <b>(+23.57%)</b></td><td>0.21 (-0.44%)</td><td>0.16 <b>(+197.76%)</b></td><td>0.18 <b>(+48.52%)</b></td><td>614.40 <b>(-66.41%)</b></td><td>433.84 <b>(-36.05%)</b></td><td>477.20 (+0.44%)</td><td>167.40 <b>(-41.30%)</b></td><td>171.20 <b>(-73.71%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>0.12 (n/a)</td><td>1829.30 (n/a)</td><td>678.44 (n/a)</td><td>475.10 (n/a)</td><td>285.20 (n/a)</td><td>651.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (-2.74%)</td><td>0.21 (-15.68%)</td><td>0.15 <b>(-40.88%)</b></td><td>0.15 <b>(+29.59%)</b></td><td>0.07 (-0.74%)</td><td>482.10 <b>(-22.84%)</b></td><td>392.90 (+15.43%)</td><td>479.60 <b>(+69.17%)</b></td><td>235.80 (+2.83%)</td><td>121.92 <b>(-24.12%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>624.80 (n/a)</td><td>340.38 (n/a)</td><td>283.50 (n/a)</td><td>229.30 (n/a)</td><td>160.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (-0.02%)</td><td>0.24 <b>(+21.94%)</b></td><td>0.24 <b>(+60.58%)</b></td><td>0.15 <b>(+119.62%)</b></td><td>0.08 <b>(-24.64%)</b></td><td>504.80 <b>(-54.47%)</b></td><td>346.96 <b>(-33.42%)</b></td><td>302.10 <b>(-37.72%)</b></td><td>234.60 (+0.04%)</td><td>126.35 <b>(-64.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>1108.70 (n/a)</td><td>521.10 (n/a)</td><td>485.10 (n/a)</td><td>234.50 (n/a)</td><td>353.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 (-10.89%)</td><td>0.18 (-15.40%)</td><td>0.15 <b>(-23.67%)</b></td><td>0.13 <b>(+30.09%)</b></td><td>0.06 <b>(-24.63%)</b></td><td>555.10 <b>(-23.13%)</b></td><td>438.58 (+10.58%)</td><td>482.00 <b>(+30.98%)</b></td><td>278.20 (+12.22%)</td><td>128.76 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>722.10 (n/a)</td><td>396.62 (n/a)</td><td>368.00 (n/a)</td><td>247.90 (n/a)</td><td>192.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(-26.58%)</b></td><td>0.10 (-7.19%)</td><td>0.12 <b>(+45.01%)</b></td><td>0.06 (-18.93%)</td><td>0.03 <b>(-28.36%)</b></td><td>666.60 <b>(+23.35%)</b></td><td>415.04 (+5.54%)</td><td>308.30 <b>(-31.04%)</b></td><td>305.70 <b>(+36.23%)</b></td><td>160.99 (+14.85%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>540.40 (n/a)</td><td>393.24 (n/a)</td><td>447.10 (n/a)</td><td>224.40 (n/a)</td><td>140.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (-17.23%)</td><td>0.09 (+5.48%)</td><td>0.07 (-3.13%)</td><td>0.06 <b>(+22.37%)</b></td><td>0.03 <b>(-21.90%)</b></td><td>613.30 (-18.28%)</td><td>453.88 (-9.86%)</td><td>514.60 (+3.23%)</td><td>295.00 <b>(+20.80%)</b></td><td>144.63 <b>(-23.58%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>750.50 (n/a)</td><td>503.52 (n/a)</td><td>498.50 (n/a)</td><td>244.20 (n/a)</td><td>189.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (+6.61%)</td><td>0.09 (-15.77%)</td><td>0.08 <b>(-36.06%)</b></td><td>0.08 (+16.72%)</td><td>0.03 (+3.15%)</td><td>490.90 (-14.33%)</td><td>431.66 (+17.40%)</td><td>475.00 <b>(+56.40%)</b></td><td>261.30 (-6.21%)</td><td>97.00 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>573.00 (n/a)</td><td>367.68 (n/a)</td><td>303.70 (n/a)</td><td>278.60 (n/a)</td><td>121.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (+19.22%)</td><td>0.11 (+15.12%)</td><td>0.12 <b>(+41.41%)</b></td><td>0.06 (-5.92%)</td><td>0.04 <b>(+36.47%)</b></td><td>633.80 (+6.29%)</td><td>387.64 (-9.06%)</td><td>305.10 <b>(-29.28%)</b></td><td>254.80 (-16.13%)</td><td>157.06 <b>(+28.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>596.30 (n/a)</td><td>426.28 (n/a)</td><td>431.40 (n/a)</td><td>303.80 (n/a)</td><td>122.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 <b>(+74.14%)</b></td><td>0.10 <b>(+47.96%)</b></td><td>0.08 <b>(+20.64%)</b></td><td>0.05 <b>(+52.48%)</b></td><td>0.04 <b>(+135.06%)</b></td><td>671.80 <b>(-34.41%)</b></td><td>448.34 <b>(-27.47%)</b></td><td>445.40 (-17.10%)</td><td>249.70 <b>(-42.58%)</b></td><td>187.94 (-19.29%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>1024.30 (n/a)</td><td>618.14 (n/a)</td><td>537.30 (n/a)</td><td>434.90 (n/a)</td><td>232.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 <b>(+60.84%)</b></td><td>0.12 <b>(+51.18%)</b></td><td>0.14 <b>(+83.65%)</b></td><td>0.06 (+10.08%)</td><td>0.05 <b>(+141.14%)</b></td><td>571.80 (-9.15%)</td><td>355.14 <b>(-27.25%)</b></td><td>270.90 <b>(-45.55%)</b></td><td>219.20 <b>(-37.83%)</b></td><td>154.97 <b>(+38.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>629.40 (n/a)</td><td>488.18 (n/a)</td><td>497.50 (n/a)</td><td>352.60 (n/a)</td><td>111.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(-28.88%)</b></td><td>0.08 <b>(-22.76%)</b></td><td>0.09 (+6.31%)</td><td>0.02 <b>(-68.80%)</b></td><td>0.03 (-0.59%)</td><td>1931.30 <b>(+220.44%)</b></td><td>758.10 <b>(+67.34%)</b></td><td>478.30 (-5.94%)</td><td>402.70 <b>(+40.61%)</b></td><td>657.80 <b>(+394.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>602.70 (n/a)</td><td>453.02 (n/a)</td><td>508.50 (n/a)</td><td>286.40 (n/a)</td><td>133.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (+0.93%)</td><td>0.13 (+4.86%)</td><td>0.14 (+2.73%)</td><td>0.06 <b>(-33.43%)</b></td><td>0.04 <b>(+24.99%)</b></td><td>723.10 <b>(+50.21%)</b></td><td>367.76 (+3.75%)</td><td>288.00 (-2.64%)</td><td>252.20 (-0.90%)</td><td>200.17 <b>(+88.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>481.40 (n/a)</td><td>354.48 (n/a)</td><td>295.80 (n/a)</td><td>254.50 (n/a)</td><td>106.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 <b>(-22.88%)</b></td><td>0.09 <b>(-25.66%)</b></td><td>0.08 <b>(-38.37%)</b></td><td>0.08 <b>(+23.37%)</b></td><td>0.03 <b>(-43.06%)</b></td><td>536.00 (-18.94%)</td><td>465.64 <b>(+22.69%)</b></td><td>490.80 <b>(+62.25%)</b></td><td>293.60 <b>(+29.68%)</b></td><td>98.05 <b>(-43.89%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>661.20 (n/a)</td><td>379.52 (n/a)</td><td>302.50 (n/a)</td><td>226.40 (n/a)</td><td>174.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (-3.69%)</td><td>0.11 (-5.54%)</td><td>0.09 (-5.96%)</td><td>0.07 (-19.18%)</td><td>0.04 (+10.51%)</td><td>603.00 <b>(+23.74%)</b></td><td>422.86 (+9.44%)</td><td>455.20 (+6.33%)</td><td>261.00 (+3.82%)</td><td>148.29 <b>(+33.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>487.30 (n/a)</td><td>386.38 (n/a)</td><td>428.10 (n/a)</td><td>251.40 (n/a)</td><td>111.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 <b>(-41.69%)</b></td><td>0.08 <b>(-22.18%)</b></td><td>0.08 <b>(-29.07%)</b></td><td>0.08 <b>(+49.12%)</b></td><td>0.01 <b>(-80.41%)</b></td><td>536.60 <b>(-32.94%)</b></td><td>486.84 (+9.42%)</td><td>508.80 <b>(+40.98%)</b></td><td>421.10 <b>(+71.53%)</b></td><td>48.59 <b>(-78.08%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>800.20 (n/a)</td><td>444.94 (n/a)</td><td>360.90 (n/a)</td><td>245.50 (n/a)</td><td>221.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (-15.01%)</td><td>0.11 (+3.04%)</td><td>0.10 <b>(+32.85%)</b></td><td>0.08 (+19.45%)</td><td>0.04 <b>(-30.59%)</b></td><td>538.70 (-16.29%)</td><td>405.48 (-11.43%)</td><td>412.60 <b>(-24.72%)</b></td><td>245.70 (+17.67%)</td><td>132.56 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>643.50 (n/a)</td><td>457.80 (n/a)</td><td>548.10 (n/a)</td><td>208.80 (n/a)</td><td>190.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(-36.73%)</b></td><td>0.10 (+14.04%)</td><td>0.11 <b>(+68.44%)</b></td><td>0.07 <b>(+30.27%)</b></td><td>0.02 <b>(-64.46%)</b></td><td>482.20 <b>(-23.24%)</b></td><td>360.48 <b>(-24.86%)</b></td><td>318.80 <b>(-40.63%)</b></td><td>300.80 <b>(+58.07%)</b></td><td>78.29 <b>(-54.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>628.20 (n/a)</td><td>479.72 (n/a)</td><td>537.00 (n/a)</td><td>190.30 (n/a)</td><td>171.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (-14.60%)</td><td>0.08 <b>(-22.79%)</b></td><td>0.08 <b>(-36.02%)</b></td><td>0.06 (-2.73%)</td><td>0.03 (-12.34%)</td><td>631.90 (+2.81%)</td><td>448.50 <b>(+27.48%)</b></td><td>458.20 <b>(+56.33%)</b></td><td>301.50 (+17.09%)</td><td>141.55 (-4.68%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>614.60 (n/a)</td><td>351.82 (n/a)</td><td>293.10 (n/a)</td><td>257.50 (n/a)</td><td>148.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 <b>(+74.49%)</b></td><td>0.11 <b>(+76.90%)</b></td><td>0.13 <b>(+66.57%)</b></td><td>0.07 <b>(+420.24%)</b></td><td>0.04 (+16.34%)</td><td>474.50 <b>(-80.78%)</b></td><td>335.74 <b>(-61.41%)</b></td><td>271.40 <b>(-39.96%)</b></td><td>223.50 <b>(-42.68%)</b></td><td>114.13 <b>(-87.30%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2468.70 (n/a)</td><td>869.96 (n/a)</td><td>452.00 (n/a)</td><td>389.90 (n/a)</td><td>898.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (-5.19%)</td><td>0.09 (-2.15%)</td><td>0.07 (-18.94%)</td><td>0.06 (+5.15%)</td><td>0.04 (+4.88%)</td><td>538.40 (-4.89%)</td><td>419.54 (+4.07%)</td><td>514.30 <b>(+23.36%)</b></td><td>240.90 (+5.47%)</td><td>145.76 (+10.28%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>566.10 (n/a)</td><td>403.14 (n/a)</td><td>416.90 (n/a)</td><td>228.40 (n/a)</td><td>132.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(-42.84%)</b></td><td>0.08 <b>(-31.12%)</b></td><td>0.08 <b>(-34.58%)</b></td><td>0.02 <b>(-74.05%)</b></td><td>0.04 <b>(-28.69%)</b></td><td>1888.90 <b>(+285.41%)</b></td><td>665.96 <b>(+98.32%)</b></td><td>425.70 <b>(+52.85%)</b></td><td>279.90 <b>(+74.94%)</b></td><td>687.65 <b>(+385.07%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>490.10 (n/a)</td><td>335.80 (n/a)</td><td>278.50 (n/a)</td><td>160.00 (n/a)</td><td>141.76 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 <b>(+35.09%)</b></td><td>0.09 (+10.84%)</td><td>0.08 (-1.03%)</td><td>0.06 (-17.64%)</td><td>0.03 <b>(+448.70%)</b></td><td>555.40 <b>(+21.43%)</b></td><td>422.24 (-2.25%)</td><td>441.20 (+1.03%)</td><td>287.10 <b>(-25.97%)</b></td><td>130.26 <b>(+383.19%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>457.40 (n/a)</td><td>431.98 (n/a)</td><td>436.70 (n/a)</td><td>387.80 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.48 (+13.51%)</td><td>0.37 <b>(+21.44%)</b></td><td>0.47 <b>(+66.65%)</b></td><td>0.21 (-10.42%)</td><td>0.14 <b>(+79.79%)</b></td><td>632.00 (+11.64%)</td><td>414.80 (-8.92%)</td><td>281.00 <b>(-40.00%)</b></td><td>275.20 (-11.91%)</td><td>188.14 <b>(+71.92%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>566.10 (n/a)</td><td>455.42 (n/a)</td><td>468.30 (n/a)</td><td>312.40 (n/a)</td><td>109.43 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.32 <b>(-26.39%)</b></td><td>0.25 (-15.03%)</td><td>0.23 (-5.05%)</td><td>0.20 (-7.65%)</td><td>0.05 <b>(-44.93%)</b></td><td>649.70 (+8.28%)</td><td>536.56 (+12.86%)</td><td>559.10 (+5.33%)</td><td>407.80 <b>(+35.84%)</b></td><td>107.54 <b>(-20.54%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>600.00 (n/a)</td><td>475.42 (n/a)</td><td>530.80 (n/a)</td><td>300.20 (n/a)</td><td>135.33 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.55 (-16.28%)</td><td>0.32 (-2.23%)</td><td>0.24 (-5.62%)</td><td>0.20 (-11.44%)</td><td>0.15 (-16.63%)</td><td>654.90 (+12.91%)</td><td>480.22 (+2.44%)</td><td>541.40 (+5.95%)</td><td>239.40 (+19.40%)</td><td>189.89 <b>(+22.72%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.65 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>580.00 (n/a)</td><td>468.76 (n/a)</td><td>511.00 (n/a)</td><td>200.50 (n/a)</td><td>154.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-17.51%)</td><td>0.01 (-5.69%)</td><td>0.01 (-10.65%)</td><td>0.01 <b>(+24.13%)</b></td><td>0.00 <b>(-55.71%)</b></td><td>463.30 (-19.44%)</td><td>382.50 (-0.77%)</td><td>351.90 (+11.93%)</td><td>332.40 <b>(+21.23%)</b></td><td>56.79 <b>(-56.63%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.10 (n/a)</td><td>385.46 (n/a)</td><td>314.40 (n/a)</td><td>274.20 (n/a)</td><td>130.95 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 <b>(-31.40%)</b></td><td>0.01 <b>(-22.64%)</b></td><td>0.01 (+2.48%)</td><td>0.01 (+0.39%)</td><td>0.00 <b>(-39.50%)</b></td><td>566.20 (-0.39%)</td><td>380.66 <b>(+21.04%)</b></td><td>296.80 (-2.43%)</td><td>274.30 <b>(+45.75%)</b></td><td>134.59 (-12.14%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.40 (n/a)</td><td>314.50 (n/a)</td><td>304.20 (n/a)</td><td>188.20 (n/a)</td><td>153.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 <b>(-23.07%)</b></td><td>0.01 (-11.11%)</td><td>0.01 (+11.49%)</td><td>0.01 (-16.19%)</td><td>0.00 <b>(-27.56%)</b></td><td>664.90 (+19.33%)</td><td>459.38 (+10.73%)</td><td>410.00 (-10.30%)</td><td>323.50 <b>(+29.97%)</b></td><td>144.89 (+12.58%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.20 (n/a)</td><td>414.88 (n/a)</td><td>457.10 (n/a)</td><td>248.90 (n/a)</td><td>128.69 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>8.87 <b>(-26.97%)</b></td><td>6.68 (-7.46%)</td><td>7.44 <b>(+37.75%)</b></td><td>3.96 (-9.91%)</td><td>1.98 <b>(-41.16%)</b></td><td>529.70 (+11.00%)</td><td>341.92 (+0.78%)</td><td>281.80 <b>(-27.41%)</b></td><td>236.60 <b>(+36.92%)</b></td><td>120.15 (-9.74%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>12.14 (n/a)</td><td>7.22 (n/a)</td><td>5.40 (n/a)</td><td>4.40 (n/a)</td><td>3.37 (n/a)</td><td>477.20 (n/a)</td><td>339.28 (n/a)</td><td>388.20 (n/a)</td><td>172.80 (n/a)</td><td>133.12 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.72 <b>(+37.94%)</b></td><td>0.50 <b>(+24.47%)</b></td><td>0.50 (+3.13%)</td><td>0.33 <b>(+38.13%)</b></td><td>0.14 (+2.62%)</td><td>396.10 <b>(-27.60%)</b></td><td>279.02 <b>(-23.56%)</b></td><td>263.70 (-3.02%)</td><td>183.30 <b>(-27.49%)</b></td><td>76.77 <b>(-45.79%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.49 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>547.10 (n/a)</td><td>365.00 (n/a)</td><td>271.90 (n/a)</td><td>252.80 (n/a)</td><td>141.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.53 (-2.97%)</td><td>0.40 (-8.69%)</td><td>0.49 (+9.20%)</td><td>0.25 (-8.85%)</td><td>0.14 <b>(+28.31%)</b></td><td>526.00 (+9.70%)</td><td>365.78 (+15.53%)</td><td>270.50 (-8.43%)</td><td>249.70 (+3.05%)</td><td>143.19 <b>(+48.51%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>479.50 (n/a)</td><td>316.60 (n/a)</td><td>295.40 (n/a)</td><td>242.30 (n/a)</td><td>96.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.50 (+6.50%)</td><td>0.38 (+10.52%)</td><td>0.45 <b>(+55.62%)</b></td><td>0.21 (-11.10%)</td><td>0.13 <b>(+25.89%)</b></td><td>620.00 (+12.50%)</td><td>389.14 (-5.18%)</td><td>292.60 <b>(-35.73%)</b></td><td>263.40 (-6.13%)</td><td>158.47 <b>(+36.20%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>551.10 (n/a)</td><td>410.38 (n/a)</td><td>455.30 (n/a)</td><td>280.60 (n/a)</td><td>116.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.49 (-12.08%)</td><td>0.35 (-19.46%)</td><td>0.45 (+0.15%)</td><td>0.12 <b>(-54.94%)</b></td><td>0.17 <b>(+67.55%)</b></td><td>1090.80 <b>(+121.93%)</b></td><td>512.72 <b>(+58.98%)</b></td><td>295.20 (-0.14%)</td><td>272.20 (+13.75%)</td><td>357.57 <b>(+266.80%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>491.50 (n/a)</td><td>322.50 (n/a)</td><td>295.60 (n/a)</td><td>239.30 (n/a)</td><td>97.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.49 (-11.99%)</td><td>0.39 (-12.01%)</td><td>0.39 (-17.01%)</td><td>0.27 (-5.87%)</td><td>0.09 (-19.74%)</td><td>491.10 (+6.25%)</td><td>353.06 (+12.21%)</td><td>342.60 <b>(+20.46%)</b></td><td>267.00 (+13.62%)</td><td>87.04 (-3.88%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.11 (n/a)</td><td>462.20 (n/a)</td><td>314.64 (n/a)</td><td>284.40 (n/a)</td><td>235.00 (n/a)</td><td>90.55 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (-2.69%)</td><td>0.01 (-15.47%)</td><td>0.01 (-10.74%)</td><td>0.01 <b>(-46.84%)</b></td><td>0.00 <b>(+73.96%)</b></td><td>756.90 <b>(+88.10%)</b></td><td>440.78 <b>(+32.25%)</b></td><td>354.20 (+12.05%)</td><td>280.70 (+2.78%)</td><td>199.61 <b>(+227.05%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>402.40 (n/a)</td><td>333.30 (n/a)</td><td>316.10 (n/a)</td><td>273.10 (n/a)</td><td>61.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (+2.87%)</td><td>0.01 <b>(+22.17%)</b></td><td>0.02 <b>(+55.18%)</b></td><td>0.01 (+3.28%)</td><td>0.00 (-0.38%)</td><td>494.00 (-3.18%)</td><td>318.22 (-18.12%)</td><td>271.20 <b>(-35.57%)</b></td><td>242.30 (-2.77%)</td><td>101.46 (+0.34%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.20 (n/a)</td><td>388.66 (n/a)</td><td>420.90 (n/a)</td><td>249.20 (n/a)</td><td>101.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (-4.55%)</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>20215.49 (-15.71%)</td><td>13476.99 (+2.25%)</td><td>15784.77 <b>(+129.86%)</b></td><td>5105.37 (-19.09%)</td><td>7002.64 <b>(-22.13%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23982.72 (n/a)</td><td>13180.15 (n/a)</td><td>6867.10 (n/a)</td><td>6309.89 (n/a)</td><td>8992.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+110.59%)</b></td><td>17311.09 (-12.23%)</td><td>13260.14 (-17.77%)</td><td>16460.05 (-3.96%)</td><td>6747.20 <b>(-31.51%)</b></td><td>5095.22 <b>(+37.17%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19723.19 (n/a)</td><td>16126.55 (n/a)</td><td>17139.32 (n/a)</td><td>9851.57 (n/a)</td><td>3714.41 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 <b>(-30.55%)</b></td><td>0.09 (-17.66%)</td><td>0.09 (-18.62%)</td><td>0.07 (-8.91%)</td><td>0.02 <b>(-45.74%)</b></td><td>28477.79 (+9.73%)</td><td>23660.22 (+17.32%)</td><td>24359.21 <b>(+22.84%)</b></td><td>18785.56 <b>(+43.91%)</b></td><td>4463.65 (-17.50%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>25953.47 (n/a)</td><td>20167.87 (n/a)</td><td>19830.76 (n/a)</td><td>13053.73 (n/a)</td><td>5410.44 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.95 (+6.62%)</td><td>2.14 (+6.65%)</td><td>2.03 (+2.25%)</td><td>1.58 <b>(+22.69%)</b></td><td>0.57 (-18.43%)</td><td>662.00 (-18.49%)</td><td>517.78 (-10.84%)</td><td>515.40 (-2.18%)</td><td>355.20 (-6.21%)</td><td>131.20 <b>(-37.49%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.77 (n/a)</td><td>2.01 (n/a)</td><td>1.99 (n/a)</td><td>1.29 (n/a)</td><td>0.70 (n/a)</td><td>812.20 (n/a)</td><td>580.70 (n/a)</td><td>526.90 (n/a)</td><td>378.70 (n/a)</td><td>209.88 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.02 (-7.45%)</td><td>2.05 (-8.14%)</td><td>1.69 <b>(-32.00%)</b></td><td>1.44 <b>(+20.60%)</b></td><td>0.67 <b>(-27.12%)</b></td><td>727.70 (-17.08%)</td><td>551.92 (+0.16%)</td><td>621.90 <b>(+47.06%)</b></td><td>347.70 (+8.05%)</td><td>158.59 <b>(-37.31%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.26 (n/a)</td><td>2.23 (n/a)</td><td>2.48 (n/a)</td><td>1.19 (n/a)</td><td>0.91 (n/a)</td><td>877.60 (n/a)</td><td>551.04 (n/a)</td><td>422.90 (n/a)</td><td>321.80 (n/a)</td><td>252.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.22 <b>(-29.25%)</b></td><td>1.75 <b>(-21.91%)</b></td><td>1.67 (-18.43%)</td><td>1.32 <b>(-23.70%)</b></td><td>0.38 <b>(-35.35%)</b></td><td>792.50 <b>(+31.06%)</b></td><td>619.92 <b>(+26.63%)</b></td><td>626.50 <b>(+22.60%)</b></td><td>471.60 <b>(+41.32%)</b></td><td>132.05 (+17.50%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.14 (n/a)</td><td>2.25 (n/a)</td><td>2.05 (n/a)</td><td>1.73 (n/a)</td><td>0.58 (n/a)</td><td>604.70 (n/a)</td><td>489.56 (n/a)</td><td>511.00 (n/a)</td><td>333.70 (n/a)</td><td>112.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.36 <b>(+109.01%)</b></td><td>2.06 <b>(+45.77%)</b></td><td>2.19 <b>(+44.87%)</b></td><td>0.30 <b>(-69.18%)</b></td><td>1.15 <b>(+362.55%)</b></td><td>3468.50 <b>(+224.49%)</b></td><td>1049.04 <b>(+37.15%)</b></td><td>479.80 <b>(-30.97%)</b></td><td>312.00 <b>(-52.15%)</b></td><td>1356.79 <b>(+689.45%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.61 (n/a)</td><td>1.42 (n/a)</td><td>1.51 (n/a)</td><td>0.98 (n/a)</td><td>0.25 (n/a)</td><td>1068.90 (n/a)</td><td>764.88 (n/a)</td><td>695.10 (n/a)</td><td>652.10 (n/a)</td><td>171.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.82 <b>(+48.80%)</b></td><td>2.91 <b>(+80.25%)</b></td><td>2.86 <b>(+156.67%)</b></td><td>0.61 (+3.91%)</td><td>1.55 <b>(+45.77%)</b></td><td>3430.70 (-3.76%)</td><td>1197.08 <b>(-34.56%)</b></td><td>733.60 <b>(-61.04%)</b></td><td>435.20 <b>(-32.79%)</b></td><td>1257.24 (+10.75%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.24 (n/a)</td><td>1.61 (n/a)</td><td>1.11 (n/a)</td><td>0.59 (n/a)</td><td>1.06 (n/a)</td><td>3564.90 (n/a)</td><td>1829.34 (n/a)</td><td>1882.90 (n/a)</td><td>647.50 (n/a)</td><td>1135.21 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.67 <b>(+27.72%)</b></td><td>2.56 (-2.76%)</td><td>2.51 <b>(+23.38%)</b></td><td>0.58 <b>(-40.20%)</b></td><td>2.13 <b>(+50.41%)</b></td><td>3621.90 <b>(+67.22%)</b></td><td>1787.48 <b>(+68.87%)</b></td><td>834.50 (-18.95%)</td><td>369.90 <b>(-21.70%)</b></td><td>1627.57 <b>(+141.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.44 (n/a)</td><td>2.63 (n/a)</td><td>2.04 (n/a)</td><td>0.97 (n/a)</td><td>1.42 (n/a)</td><td>2165.90 (n/a)</td><td>1058.52 (n/a)</td><td>1029.60 (n/a)</td><td>472.40 (n/a)</td><td>674.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.64 (+7.77%)</td><td>2.87 (-2.18%)</td><td>2.49 <b>(-25.92%)</b></td><td>0.59 (-4.30%)</td><td>2.39 <b>(+39.15%)</b></td><td>3578.10 (+4.50%)</td><td>1744.68 <b>(+43.44%)</b></td><td>841.00 <b>(+34.99%)</b></td><td>372.20 (-7.21%)</td><td>1655.21 <b>(+32.02%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.23 (n/a)</td><td>2.93 (n/a)</td><td>3.37 (n/a)</td><td>0.61 (n/a)</td><td>1.72 (n/a)</td><td>3424.10 (n/a)</td><td>1216.32 (n/a)</td><td>623.00 (n/a)</td><td>401.10 (n/a)</td><td>1253.78 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.60 (-0.16%)</td><td>3.35 (+0.21%)</td><td>2.67 (+6.46%)</td><td>0.58 (-1.07%)</td><td>2.27 <b>(-24.29%)</b></td><td>3605.50 (+1.08%)</td><td>1206.52 <b>(-29.88%)</b></td><td>785.00 (-6.06%)</td><td>317.90 (+0.16%)</td><td>1358.98 (-19.77%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.61 (n/a)</td><td>3.34 (n/a)</td><td>2.51 (n/a)</td><td>0.59 (n/a)</td><td>3.00 (n/a)</td><td>3567.00 (n/a)</td><td>1720.62 (n/a)</td><td>835.60 (n/a)</td><td>317.40 (n/a)</td><td>1693.80 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.55 <b>(+44.22%)</b></td><td>4.72 <b>(+29.16%)</b></td><td>5.09 <b>(+22.89%)</b></td><td>2.53 (+7.48%)</td><td>1.49 <b>(+59.45%)</b></td><td>828.50 (-6.96%)</td><td>492.44 (-19.35%)</td><td>411.70 (-18.64%)</td><td>320.10 <b>(-30.67%)</b></td><td>199.11 (+9.00%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.54 (n/a)</td><td>3.66 (n/a)</td><td>4.14 (n/a)</td><td>2.36 (n/a)</td><td>0.94 (n/a)</td><td>890.50 (n/a)</td><td>610.58 (n/a)</td><td>506.00 (n/a)</td><td>461.70 (n/a)</td><td>182.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.81 <b>(-40.88%)</b></td><td>3.05 (-16.35%)</td><td>3.49 (+11.22%)</td><td>1.80 (+1.81%)</td><td>0.84 <b>(-53.83%)</b></td><td>1163.50 (-1.79%)</td><td>743.80 (+6.70%)</td><td>601.70 (-10.09%)</td><td>550.30 <b>(+69.17%)</b></td><td>256.54 <b>(-22.29%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.45 (n/a)</td><td>3.64 (n/a)</td><td>3.13 (n/a)</td><td>1.77 (n/a)</td><td>1.82 (n/a)</td><td>1184.70 (n/a)</td><td>697.08 (n/a)</td><td>669.20 (n/a)</td><td>325.30 (n/a)</td><td>330.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.72 (+13.65%)</td><td>3.17 (-2.07%)</td><td>3.36 (+0.99%)</td><td>1.11 <b>(-35.60%)</b></td><td>1.84 <b>(+22.69%)</b></td><td>3783.50 <b>(+55.27%)</b></td><td>1853.50 (+17.60%)</td><td>1246.50 (-0.98%)</td><td>733.40 (-12.00%)</td><td>1257.18 <b>(+61.35%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.03 (n/a)</td><td>3.24 (n/a)</td><td>3.33 (n/a)</td><td>1.72 (n/a)</td><td>1.50 (n/a)</td><td>2436.70 (n/a)</td><td>1576.10 (n/a)</td><td>1258.90 (n/a)</td><td>833.40 (n/a)</td><td>779.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>9.29 <b>(+60.06%)</b></td><td>6.67 <b>(+88.28%)</b></td><td>6.67 <b>(+71.10%)</b></td><td>3.13 <b>(+168.63%)</b></td><td>2.42 (+17.83%)</td><td>1342.10 <b>(-62.77%)</b></td><td>727.98 <b>(-58.10%)</b></td><td>628.90 <b>(-41.56%)</b></td><td>451.30 <b>(-37.53%)</b></td><td>359.91 <b>(-71.43%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.81 (n/a)</td><td>3.54 (n/a)</td><td>3.90 (n/a)</td><td>1.16 (n/a)</td><td>2.06 (n/a)</td><td>3605.20 (n/a)</td><td>1737.48 (n/a)</td><td>1076.10 (n/a)</td><td>722.40 (n/a)</td><td>1259.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>9.03 (-11.02%)</td><td>5.52 (-16.99%)</td><td>6.02 (-3.89%)</td><td>1.72 <b>(-52.46%)</b></td><td>3.43 <b>(+46.15%)</b></td><td>2439.70 <b>(+110.34%)</b></td><td>1192.08 <b>(+69.34%)</b></td><td>696.70 (+4.03%)</td><td>464.60 (+12.41%)</td><td>906.28 <b>(+227.48%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>10.15 (n/a)</td><td>6.65 (n/a)</td><td>6.26 (n/a)</td><td>3.62 (n/a)</td><td>2.35 (n/a)</td><td>1159.90 (n/a)</td><td>703.96 (n/a)</td><td>669.70 (n/a)</td><td>413.30 (n/a)</td><td>276.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>11.45 (+14.01%)</td><td>4.54 <b>(-27.63%)</b></td><td>2.11 <b>(-67.88%)</b></td><td>1.17 <b>(-70.62%)</b></td><td>4.50 <b>(+80.10%)</b></td><td>3580.90 <b>(+240.36%)</b></td><td>2000.92 <b>(+164.91%)</b></td><td>1984.10 <b>(+211.38%)</b></td><td>366.40 (-12.28%)</td><td>1514.86 <b>(+434.88%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>10.04 (n/a)</td><td>6.27 (n/a)</td><td>6.58 (n/a)</td><td>3.99 (n/a)</td><td>2.50 (n/a)</td><td>1052.10 (n/a)</td><td>755.32 (n/a)</td><td>637.20 (n/a)</td><td>417.70 (n/a)</td><td>283.22 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>10.00 (+2.90%)</td><td>7.16 <b>(+26.97%)</b></td><td>6.76 (+3.68%)</td><td>4.20 <b>(+264.73%)</b></td><td>2.40 <b>(-36.86%)</b></td><td>998.80 <b>(-72.58%)</b></td><td>646.30 <b>(-54.35%)</b></td><td>620.30 (-3.55%)</td><td>419.40 (-2.80%)</td><td>234.15 <b>(-83.01%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>9.72 (n/a)</td><td>5.64 (n/a)</td><td>6.52 (n/a)</td><td>1.15 (n/a)</td><td>3.80 (n/a)</td><td>3643.10 (n/a)</td><td>1415.72 (n/a)</td><td>643.10 (n/a)</td><td>431.50 (n/a)</td><td>1377.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.78 <b>(-22.12%)</b></td><td>3.90 <b>(-47.02%)</b></td><td>3.75 <b>(-49.04%)</b></td><td>1.24 <b>(-78.60%)</b></td><td>2.69 <b>(+129.43%)</b></td><td>3375.50 <b>(+367.39%)</b></td><td>1818.68 <b>(+212.21%)</b></td><td>1117.60 <b>(+96.21%)</b></td><td>618.40 <b>(+28.41%)</b></td><td>1414.81 <b>(+1362.76%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>8.71 (n/a)</td><td>7.35 (n/a)</td><td>7.36 (n/a)</td><td>5.81 (n/a)</td><td>1.17 (n/a)</td><td>722.20 (n/a)</td><td>582.52 (n/a)</td><td>569.60 (n/a)</td><td>481.60 (n/a)</td><td>96.72 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.70 (-0.24%)</td><td>1.40 (-0.02%)</td><td>1.49 (+1.61%)</td><td>0.82 (-13.73%)</td><td>0.34 (+6.10%)</td><td>636.20 (+15.90%)</td><td>399.58 (+1.92%)</td><td>352.30 (-1.59%)</td><td>309.10 (+0.26%)</td><td>133.64 <b>(+32.99%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.70 (n/a)</td><td>1.40 (n/a)</td><td>1.46 (n/a)</td><td>0.96 (n/a)</td><td>0.32 (n/a)</td><td>548.90 (n/a)</td><td>392.06 (n/a)</td><td>358.00 (n/a)</td><td>308.30 (n/a)</td><td>100.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.44 (-0.73%)</td><td>1.56 (+2.47%)</td><td>1.54 (-3.57%)</td><td>0.31 (+0.91%)</td><td>0.91 (+16.80%)</td><td>3421.30 (-0.90%)</td><td>1181.16 (+1.47%)</td><td>681.90 (+3.70%)</td><td>429.40 (+0.73%)</td><td>1269.86 (-1.02%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.46 (n/a)</td><td>1.53 (n/a)</td><td>1.59 (n/a)</td><td>0.30 (n/a)</td><td>0.78 (n/a)</td><td>3452.30 (n/a)</td><td>1164.04 (n/a)</td><td>657.60 (n/a)</td><td>426.30 (n/a)</td><td>1282.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.64 (-4.76%)</td><td>1.83 <b>(-38.73%)</b></td><td>2.14 <b>(-37.63%)</b></td><td>0.58 <b>(-43.43%)</b></td><td>1.28 (+13.68%)</td><td>3617.70 <b>(+76.76%)</b></td><td>1934.38 <b>(+116.23%)</b></td><td>981.20 <b>(+60.33%)</b></td><td>576.70 (+4.99%)</td><td>1513.02 <b>(+134.26%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.82 (n/a)</td><td>2.99 (n/a)</td><td>3.43 (n/a)</td><td>1.02 (n/a)</td><td>1.13 (n/a)</td><td>2046.70 (n/a)</td><td>894.58 (n/a)</td><td>612.00 (n/a)</td><td>549.30 (n/a)</td><td>645.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.64 (-14.60%)</td><td>1.05 <b>(-32.18%)</b></td><td>1.01 <b>(-36.89%)</b></td><td>0.71 <b>(-32.18%)</b></td><td>0.35 (+7.50%)</td><td>741.80 <b>(+47.45%)</b></td><td>538.48 <b>(+52.57%)</b></td><td>521.40 <b>(+58.48%)</b></td><td>319.70 (+17.11%)</td><td>154.55 <b>(+72.83%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.92 (n/a)</td><td>1.55 (n/a)</td><td>1.59 (n/a)</td><td>1.04 (n/a)</td><td>0.33 (n/a)</td><td>503.10 (n/a)</td><td>352.94 (n/a)</td><td>329.00 (n/a)</td><td>273.00 (n/a)</td><td>89.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (-2.31%)</td><td>0.09 (+8.96%)</td><td>0.10 <b>(+53.67%)</b></td><td>0.05 (+2.62%)</td><td>0.03 <b>(-22.88%)</b></td><td>608.10 (-2.55%)</td><td>382.12 (-12.93%)</td><td>339.90 <b>(-34.92%)</b></td><td>252.00 (+2.36%)</td><td>139.70 (-17.75%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>624.00 (n/a)</td><td>438.86 (n/a)</td><td>522.30 (n/a)</td><td>246.20 (n/a)</td><td>169.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 <b>(-27.24%)</b></td><td>0.07 (-2.44%)</td><td>0.08 <b>(+24.87%)</b></td><td>0.05 (-18.60%)</td><td>0.02 <b>(-34.04%)</b></td><td>690.40 <b>(+22.85%)</b></td><td>491.68 (+0.90%)</td><td>419.90 (-19.93%)</td><td>396.90 <b>(+37.43%)</b></td><td>127.14 (+13.12%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>562.00 (n/a)</td><td>487.28 (n/a)</td><td>524.40 (n/a)</td><td>288.80 (n/a)</td><td>112.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 (+8.58%)</td><td>0.20 <b>(+21.59%)</b></td><td>0.21 <b>(+65.05%)</b></td><td>0.15 (+18.00%)</td><td>0.05 (-12.39%)</td><td>445.90 (-15.26%)</td><td>343.48 <b>(-20.30%)</b></td><td>306.30 <b>(-39.41%)</b></td><td>247.30 (-7.90%)</td><td>82.44 <b>(-32.62%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>526.20 (n/a)</td><td>430.94 (n/a)</td><td>505.50 (n/a)</td><td>268.50 (n/a)</td><td>122.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.25 (+4.87%)</td><td>0.17 (-10.95%)</td><td>0.13 <b>(-29.30%)</b></td><td>0.11 (-12.53%)</td><td>0.07 <b>(+42.27%)</b></td><td>608.90 (+14.33%)</td><td>452.04 <b>(+21.10%)</b></td><td>512.00 <b>(+41.44%)</b></td><td>257.70 (-4.63%)</td><td>171.19 <b>(+59.28%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>532.60 (n/a)</td><td>373.28 (n/a)</td><td>362.00 (n/a)</td><td>270.20 (n/a)</td><td>107.48 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.19 (-16.21%)</td><td>0.16 (+5.24%)</td><td>0.16 (+15.50%)</td><td>0.12 (-0.69%)</td><td>0.03 <b>(-37.38%)</b></td><td>565.50 (+0.69%)</td><td>427.66 (-7.35%)</td><td>413.00 (-13.42%)</td><td>347.50 (+19.33%)</td><td>83.40 (-18.77%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>561.60 (n/a)</td><td>461.60 (n/a)</td><td>477.00 (n/a)</td><td>291.20 (n/a)</td><td>102.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.45 (+0.33%)</td><td>0.28 <b>(-25.05%)</b></td><td>0.25 <b>(-40.80%)</b></td><td>0.19 <b>(-25.29%)</b></td><td>0.10 (+10.74%)</td><td>674.00 <b>(+33.86%)</b></td><td>506.76 <b>(+36.82%)</b></td><td>525.50 <b>(+68.92%)</b></td><td>293.80 (-0.31%)</td><td>136.69 <b>(+41.00%)</b></td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>503.50 (n/a)</td><td>370.38 (n/a)</td><td>311.10 (n/a)</td><td>294.70 (n/a)</td><td>96.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.47 (-7.03%)</td><td>0.28 (-18.77%)</td><td>0.25 (-12.66%)</td><td>0.20 (-11.88%)</td><td>0.11 (-10.77%)</td><td>670.90 (+13.48%)</td><td>518.46 <b>(+22.23%)</b></td><td>520.80 (+14.51%)</td><td>278.70 (+7.56%)</td><td>147.98 (+4.45%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>591.20 (n/a)</td><td>424.18 (n/a)</td><td>454.80 (n/a)</td><td>259.10 (n/a)</td><td>141.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.57 (+1.36%)</td><td>0.30 <b>(-20.80%)</b></td><td>0.28 <b>(-39.60%)</b></td><td>0.06 (-8.82%)</td><td>0.18 (-5.69%)</td><td>2059.90 (+9.68%)</td><td>737.38 (+19.13%)</td><td>476.30 <b>(+65.55%)</b></td><td>230.20 (-1.33%)</td><td>746.70 (+5.60%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.46 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td><td>1878.10 (n/a)</td><td>618.98 (n/a)</td><td>287.70 (n/a)</td><td>233.30 (n/a)</td><td>707.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (-12.64%)</td><td>0.05 (-10.83%)</td><td>0.05 (-17.63%)</td><td>0.03 (-7.89%)</td><td>0.02 <b>(-22.74%)</b></td><td>558.50 (+8.55%)</td><td>376.12 (+8.07%)</td><td>309.30 <b>(+21.44%)</b></td><td>256.50 (+14.46%)</td><td>134.56 (-7.95%)</td>
</tr>
<tr>
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.50 (n/a)</td><td>348.02 (n/a)</td><td>254.70 (n/a)</td><td>224.10 (n/a)</td><td>146.18 (n/a)</td>
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
