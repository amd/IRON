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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-14.48%)</td><td>0.02 (-3.15%)</td><td>0.02 (-19.46%)</td><td>0.01 <b>(+35.49%)</b></td><td>0.00 <b>(-45.12%)</b></td><td>457.90 <b>(-26.19%)</b></td><td>358.50 (-8.78%)</td><td>345.00 <b>(+24.19%)</b></td><td>264.20 (+16.95%)</td><td>84.63 <b>(-54.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.40 (n/a)</td><td>393.00 (n/a)</td><td>277.80 (n/a)</td><td>225.90 (n/a)</td><td>185.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-11.17%)</td><td>0.02 <b>(-25.27%)</b></td><td>0.02 (-14.28%)</td><td>0.01 <b>(-58.19%)</b></td><td>0.01 <b>(+79.72%)</b></td><td>757.30 <b>(+139.12%)</b></td><td>420.50 <b>(+55.36%)</b></td><td>308.30 (+16.65%)</td><td>239.00 (+12.58%)</td><td>212.56 <b>(+384.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>316.70 (n/a)</td><td>270.66 (n/a)</td><td>264.30 (n/a)</td><td>212.30 (n/a)</td><td>43.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-41.89%)</b></td><td>0.02 <b>(-29.78%)</b></td><td>0.01 <b>(-32.28%)</b></td><td>0.01 (-3.90%)</td><td>0.01 <b>(-45.04%)</b></td><td>497.50 (+4.06%)</td><td>388.92 <b>(+34.05%)</b></td><td>442.90 <b>(+47.63%)</b></td><td>260.80 <b>(+72.15%)</b></td><td>118.27 (-3.81%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>478.10 (n/a)</td><td>290.14 (n/a)</td><td>300.00 (n/a)</td><td>151.50 (n/a)</td><td>122.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-0.06%)</td><td>0.02 <b>(-29.14%)</b></td><td>0.01 <b>(-35.84%)</b></td><td>0.01 <b>(-31.90%)</b></td><td>0.00 <b>(+70.68%)</b></td><td>534.70 <b>(+46.81%)</b></td><td>425.92 <b>(+47.06%)</b></td><td>422.30 <b>(+55.83%)</b></td><td>269.80 (+0.04%)</td><td>100.64 <b>(+141.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>364.20 (n/a)</td><td>289.62 (n/a)</td><td>271.00 (n/a)</td><td>269.70 (n/a)</td><td>41.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+13.75%)</td><td>0.02 (+14.39%)</td><td>0.02 <b>(+24.87%)</b></td><td>0.01 (+1.11%)</td><td>0.01 <b>(+29.17%)</b></td><td>511.90 (-1.10%)</td><td>347.46 (-10.66%)</td><td>271.80 (-19.89%)</td><td>261.00 (-12.06%)</td><td>115.02 (+8.26%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.60 (n/a)</td><td>388.94 (n/a)</td><td>339.30 (n/a)</td><td>296.80 (n/a)</td><td>106.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-16.59%)</td><td>0.02 <b>(-20.87%)</b></td><td>0.02 (-15.97%)</td><td>0.01 <b>(-53.11%)</b></td><td>0.01 <b>(+53.30%)</b></td><td>620.10 <b>(+113.31%)</b></td><td>343.86 <b>(+38.87%)</b></td><td>283.90 (+18.99%)</td><td>237.90 (+19.91%)</td><td>156.06 <b>(+321.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>290.70 (n/a)</td><td>247.62 (n/a)</td><td>238.60 (n/a)</td><td>198.40 (n/a)</td><td>37.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (-12.46%)</td><td>0.03 <b>(-35.21%)</b></td><td>0.02 <b>(-42.70%)</b></td><td>0.01 <b>(-76.27%)</b></td><td>0.02 <b>(+49.70%)</b></td><td>1928.50 <b>(+321.35%)</b></td><td>716.80 <b>(+135.28%)</b></td><td>503.90 <b>(+74.48%)</b></td><td>245.60 (+14.23%)</td><td>689.64 <b>(+652.00%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>457.70 (n/a)</td><td>304.66 (n/a)</td><td>288.80 (n/a)</td><td>215.00 (n/a)</td><td>91.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (+9.05%)</td><td>0.03 (-7.17%)</td><td>0.03 <b>(-41.40%)</b></td><td>0.02 <b>(+266.99%)</b></td><td>0.01 <b>(-34.83%)</b></td><td>567.30 <b>(-72.75%)</b></td><td>454.00 <b>(-35.87%)</b></td><td>488.80 <b>(+70.61%)</b></td><td>242.20 (-8.33%)</td><td>123.78 <b>(-84.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2082.00 (n/a)</td><td>707.98 (n/a)</td><td>286.50 (n/a)</td><td>264.20 (n/a)</td><td>783.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (-15.01%)</td><td>0.03 <b>(-24.70%)</b></td><td>0.03 <b>(-32.22%)</b></td><td>0.03 (-4.61%)</td><td>0.01 (-17.42%)</td><td>487.90 (+4.81%)</td><td>397.48 <b>(+31.35%)</b></td><td>389.50 <b>(+47.54%)</b></td><td>266.20 (+17.68%)</td><td>92.94 (-1.41%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>465.50 (n/a)</td><td>302.60 (n/a)</td><td>264.00 (n/a)</td><td>226.20 (n/a)</td><td>94.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(+23.73%)</b></td><td>0.04 (+6.07%)</td><td>0.04 (-9.55%)</td><td>0.02 (+1.87%)</td><td>0.01 (+15.37%)</td><td>496.10 (-1.84%)</td><td>356.98 (-5.44%)</td><td>325.70 (+10.56%)</td><td>234.10 (-19.19%)</td><td>107.41 (-7.33%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.40 (n/a)</td><td>377.50 (n/a)</td><td>294.60 (n/a)</td><td>289.70 (n/a)</td><td>115.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (+4.94%)</td><td>0.04 (-2.76%)</td><td>0.04 (-7.63%)</td><td>0.02 (-10.20%)</td><td>0.01 <b>(+21.23%)</b></td><td>557.80 (+11.36%)</td><td>391.16 (+7.41%)</td><td>346.50 (+8.25%)</td><td>240.10 (-4.68%)</td><td>153.22 <b>(+30.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.90 (n/a)</td><td>364.16 (n/a)</td><td>320.10 (n/a)</td><td>251.90 (n/a)</td><td>117.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (-1.60%)</td><td>0.03 (-14.78%)</td><td>0.02 <b>(-38.86%)</b></td><td>0.02 (+16.00%)</td><td>0.01 (-5.04%)</td><td>553.80 (-13.79%)</td><td>448.48 (+14.43%)</td><td>504.70 <b>(+63.55%)</b></td><td>241.60 (+1.60%)</td><td>132.04 (-18.81%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.40 (n/a)</td><td>391.94 (n/a)</td><td>308.60 (n/a)</td><td>237.80 (n/a)</td><td>162.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (-1.81%)</td><td>0.07 <b>(-21.05%)</b></td><td>0.06 <b>(-41.97%)</b></td><td>0.04 (-9.23%)</td><td>0.03 (-12.13%)</td><td>582.10 (+10.16%)</td><td>415.04 <b>(+24.50%)</b></td><td>443.60 <b>(+72.27%)</b></td><td>231.40 (+1.85%)</td><td>133.76 (-1.34%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>528.40 (n/a)</td><td>333.36 (n/a)</td><td>257.50 (n/a)</td><td>227.20 (n/a)</td><td>135.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(-22.68%)</b></td><td>0.05 <b>(-32.38%)</b></td><td>0.04 <b>(-45.74%)</b></td><td>0.01 <b>(-75.28%)</b></td><td>0.03 <b>(+21.32%)</b></td><td>1942.00 <b>(+304.50%)</b></td><td>740.74 <b>(+113.81%)</b></td><td>559.90 <b>(+84.30%)</b></td><td>296.20 <b>(+29.34%)</b></td><td>686.43 <b>(+496.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>480.10 (n/a)</td><td>346.44 (n/a)</td><td>303.80 (n/a)</td><td>229.00 (n/a)</td><td>115.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (-18.27%)</td><td>0.05 <b>(-38.13%)</b></td><td>0.05 <b>(-45.05%)</b></td><td>0.01 <b>(-70.90%)</b></td><td>0.04 (+4.96%)</td><td>1807.30 <b>(+243.66%)</b></td><td>738.96 <b>(+119.63%)</b></td><td>514.20 <b>(+82.02%)</b></td><td>225.20 <b>(+22.39%)</b></td><td>616.30 <b>(+358.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>525.90 (n/a)</td><td>336.46 (n/a)</td><td>282.50 (n/a)</td><td>184.00 (n/a)</td><td>134.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 <b>(+21.14%)</b></td><td>0.07 (+11.94%)</td><td>0.06 (-6.05%)</td><td>0.04 <b>(+71.75%)</b></td><td>0.03 (+4.12%)</td><td>584.50 <b>(-41.78%)</b></td><td>403.24 (-19.98%)</td><td>433.00 (+6.44%)</td><td>201.30 (-17.47%)</td><td>152.44 <b>(-50.58%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1003.90 (n/a)</td><td>503.92 (n/a)</td><td>406.80 (n/a)</td><td>243.90 (n/a)</td><td>308.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (+9.02%)</td><td>0.06 (-15.92%)</td><td>0.05 <b>(-35.49%)</b></td><td>0.04 <b>(-20.20%)</b></td><td>0.02 <b>(+32.83%)</b></td><td>607.10 <b>(+25.33%)</b></td><td>442.94 <b>(+25.00%)</b></td><td>453.80 <b>(+54.99%)</b></td><td>257.20 (-8.27%)</td><td>145.92 <b>(+56.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>484.40 (n/a)</td><td>354.36 (n/a)</td><td>292.80 (n/a)</td><td>280.40 (n/a)</td><td>93.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(-21.14%)</b></td><td>0.06 <b>(-27.71%)</b></td><td>0.05 <b>(-37.27%)</b></td><td>0.05 (-17.83%)</td><td>0.02 <b>(-23.48%)</b></td><td>530.40 <b>(+21.71%)</b></td><td>439.02 <b>(+37.32%)</b></td><td>464.50 <b>(+59.40%)</b></td><td>288.00 <b>(+26.82%)</b></td><td>91.49 (+10.93%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>435.80 (n/a)</td><td>319.70 (n/a)</td><td>291.40 (n/a)</td><td>227.10 (n/a)</td><td>82.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.21 (-7.11%)</td><td>0.15 (-5.57%)</td><td>0.12 <b>(-31.39%)</b></td><td>0.09 (+4.27%)</td><td>0.05 (-10.49%)</td><td>552.00 (-4.08%)</td><td>370.84 (+2.57%)</td><td>398.20 <b>(+45.75%)</b></td><td>232.00 (+7.66%)</td><td>132.38 (-15.15%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>575.50 (n/a)</td><td>361.54 (n/a)</td><td>273.20 (n/a)</td><td>215.50 (n/a)</td><td>156.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (-5.12%)</td><td>0.14 (-12.47%)</td><td>0.17 (-1.41%)</td><td>0.08 <b>(-24.48%)</b></td><td>0.04 <b>(+39.14%)</b></td><td>588.00 <b>(+32.40%)</b></td><td>376.84 <b>(+20.13%)</b></td><td>294.50 (+1.41%)</td><td>280.90 (+5.40%)</td><td>134.12 <b>(+81.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>444.10 (n/a)</td><td>313.70 (n/a)</td><td>290.40 (n/a)</td><td>266.50 (n/a)</td><td>73.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.33 <b>(+80.25%)</b></td><td>0.16 <b>(+36.77%)</b></td><td>0.10 (-9.44%)</td><td>0.08 <b>(+224.34%)</b></td><td>0.11 <b>(+61.78%)</b></td><td>581.70 <b>(-69.17%)</b></td><td>409.90 <b>(-40.44%)</b></td><td>514.10 (+10.42%)</td><td>150.60 <b>(-44.51%)</b></td><td>198.40 <b>(-70.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1886.70 (n/a)</td><td>688.16 (n/a)</td><td>465.60 (n/a)</td><td>271.40 (n/a)</td><td>680.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 (-17.44%)</td><td>0.15 (-13.52%)</td><td>0.18 (-11.06%)</td><td>0.02 <b>(-75.17%)</b></td><td>0.07 (+0.78%)</td><td>2063.60 <b>(+302.81%)</b></td><td>630.26 <b>(+88.68%)</b></td><td>276.90 (+12.47%)</td><td>244.10 <b>(+21.14%)</b></td><td>801.47 <b>(+413.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>512.30 (n/a)</td><td>334.04 (n/a)</td><td>246.20 (n/a)</td><td>201.50 (n/a)</td><td>156.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.22 (-15.50%)</td><td>0.13 (-18.46%)</td><td>0.11 (+1.22%)</td><td>0.09 <b>(+23.16%)</b></td><td>0.05 <b>(-40.02%)</b></td><td>555.80 (-18.80%)</td><td>423.80 (+4.62%)</td><td>435.10 (-1.20%)</td><td>221.30 (+18.34%)</td><td>125.64 <b>(-40.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>684.50 (n/a)</td><td>405.10 (n/a)</td><td>440.40 (n/a)</td><td>187.00 (n/a)</td><td>212.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 (+0.36%)</td><td>0.15 (+8.00%)</td><td>0.18 <b>(+20.34%)</b></td><td>0.09 <b>(+20.52%)</b></td><td>0.06 (-6.39%)</td><td>548.10 (-17.03%)</td><td>366.04 (-10.90%)</td><td>278.60 (-16.91%)</td><td>241.30 (-0.33%)</td><td>153.31 <b>(-20.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>660.60 (n/a)</td><td>410.82 (n/a)</td><td>335.30 (n/a)</td><td>242.10 (n/a)</td><td>192.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-17.89%)</td><td>0.01 (-5.45%)</td><td>0.01 (-9.22%)</td><td>0.01 <b>(+25.67%)</b></td><td>0.00 <b>(-45.24%)</b></td><td>402.40 <b>(-20.43%)</b></td><td>292.64 (-1.61%)</td><td>270.40 (+10.14%)</td><td>236.40 <b>(+21.79%)</b></td><td>63.81 <b>(-47.68%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.70 (n/a)</td><td>297.42 (n/a)</td><td>245.50 (n/a)</td><td>194.10 (n/a)</td><td>121.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-0.69%)</td><td>0.01 (-1.35%)</td><td>0.01 (-10.47%)</td><td>0.00 (-9.25%)</td><td>0.00 (-10.98%)</td><td>556.40 (+10.20%)</td><td>342.80 (+0.02%)</td><td>291.30 (+11.69%)</td><td>233.80 (+0.69%)</td><td>128.97 (-0.17%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.90 (n/a)</td><td>342.72 (n/a)</td><td>260.80 (n/a)</td><td>232.20 (n/a)</td><td>129.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(+37.70%)</b></td><td>0.01 <b>(+39.71%)</b></td><td>0.01 <b>(+46.41%)</b></td><td>0.01 <b>(+22.35%)</b></td><td>0.00 <b>(+53.18%)</b></td><td>485.10 (-18.26%)</td><td>302.14 <b>(-26.53%)</b></td><td>267.70 <b>(-31.69%)</b></td><td>199.00 <b>(-27.37%)</b></td><td>110.01 (-5.97%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>593.50 (n/a)</td><td>411.22 (n/a)</td><td>391.90 (n/a)</td><td>274.00 (n/a)</td><td>116.99 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (+8.76%)</td><td>0.01 (-18.18%)</td><td>0.01 (-2.29%)</td><td>0.00 <b>(-72.54%)</b></td><td>0.00 <b>(+65.70%)</b></td><td>1902.40 <b>(+264.10%)</b></td><td>729.02 <b>(+81.12%)</b></td><td>440.80 (+2.35%)</td><td>254.60 (-8.05%)</td><td>672.41 <b>(+518.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.50 (n/a)</td><td>402.50 (n/a)</td><td>430.70 (n/a)</td><td>276.90 (n/a)</td><td>108.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(-34.32%)</b></td><td>0.01 <b>(-29.75%)</b></td><td>0.01 <b>(-32.21%)</b></td><td>0.00 (-15.33%)</td><td>0.00 <b>(-48.68%)</b></td><td>590.10 (+18.11%)</td><td>467.18 <b>(+35.57%)</b></td><td>450.50 <b>(+47.51%)</b></td><td>349.50 <b>(+52.29%)</b></td><td>114.05 (-6.21%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.60 (n/a)</td><td>344.60 (n/a)</td><td>305.40 (n/a)</td><td>229.50 (n/a)</td><td>121.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-0.87%)</td><td>0.01 (+3.20%)</td><td>0.01 <b>(+27.74%)</b></td><td>0.00 <b>(+20.22%)</b></td><td>0.00 <b>(-24.53%)</b></td><td>564.70 (-16.82%)</td><td>400.22 (-8.54%)</td><td>367.40 <b>(-21.71%)</b></td><td>269.30 (+0.90%)</td><td>117.08 <b>(-31.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>678.90 (n/a)</td><td>437.58 (n/a)</td><td>469.30 (n/a)</td><td>266.90 (n/a)</td><td>170.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-1.32%)</td><td>0.02 (+3.19%)</td><td>0.02 (+3.28%)</td><td>0.01 <b>(+24.45%)</b></td><td>0.01 (-19.68%)</td><td>604.00 (-19.64%)</td><td>354.52 (-11.91%)</td><td>290.50 (-3.17%)</td><td>221.50 (+1.33%)</td><td>157.13 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>751.60 (n/a)</td><td>402.46 (n/a)</td><td>300.00 (n/a)</td><td>218.60 (n/a)</td><td>229.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-24.55%)</b></td><td>0.01 <b>(-38.17%)</b></td><td>0.01 <b>(-46.59%)</b></td><td>0.00 <b>(-75.80%)</b></td><td>0.01 (+17.97%)</td><td>1931.60 <b>(+313.26%)</b></td><td>704.78 <b>(+142.46%)</b></td><td>497.40 <b>(+87.20%)</b></td><td>264.90 <b>(+32.52%)</b></td><td>696.75 <b>(+553.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>467.40 (n/a)</td><td>290.68 (n/a)</td><td>265.70 (n/a)</td><td>199.90 (n/a)</td><td>106.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-32.24%)</b></td><td>0.01 <b>(-20.39%)</b></td><td>0.01 (+1.72%)</td><td>0.01 <b>(-25.68%)</b></td><td>0.00 <b>(-46.41%)</b></td><td>633.40 <b>(+34.57%)</b></td><td>445.88 <b>(+21.47%)</b></td><td>417.70 (-1.69%)</td><td>323.00 <b>(+47.56%)</b></td><td>115.79 (+9.51%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>470.70 (n/a)</td><td>367.08 (n/a)</td><td>424.90 (n/a)</td><td>218.90 (n/a)</td><td>105.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+13.31%)</td><td>0.02 (+4.44%)</td><td>0.01 (-16.68%)</td><td>0.01 (-1.69%)</td><td>0.01 <b>(+28.20%)</b></td><td>517.50 (+1.71%)</td><td>368.30 (-0.63%)</td><td>431.50 <b>(+20.03%)</b></td><td>205.90 (-11.74%)</td><td>136.72 (+10.09%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.80 (n/a)</td><td>370.62 (n/a)</td><td>359.50 (n/a)</td><td>233.30 (n/a)</td><td>124.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+11.73%)</td><td>0.02 <b>(+30.65%)</b></td><td>0.02 <b>(+43.69%)</b></td><td>0.01 <b>(+20.68%)</b></td><td>0.01 (+13.31%)</td><td>533.20 (-17.14%)</td><td>371.18 <b>(-22.80%)</b></td><td>332.90 <b>(-30.40%)</b></td><td>205.00 (-10.52%)</td><td>152.57 (-6.78%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.50 (n/a)</td><td>480.80 (n/a)</td><td>478.30 (n/a)</td><td>229.10 (n/a)</td><td>163.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+6.08%)</td><td>0.01 (+8.06%)</td><td>0.01 (+1.82%)</td><td>0.01 (-4.28%)</td><td>0.00 <b>(+45.07%)</b></td><td>533.10 (+4.47%)</td><td>407.86 (-4.59%)</td><td>445.30 (-1.79%)</td><td>291.70 (-5.72%)</td><td>109.30 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.30 (n/a)</td><td>427.46 (n/a)</td><td>453.40 (n/a)</td><td>309.40 (n/a)</td><td>79.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-4.23%)</td><td>0.04 (-0.47%)</td><td>0.04 (-2.34%)</td><td>0.02 <b>(-24.50%)</b></td><td>0.01 (-5.19%)</td><td>629.20 <b>(+32.46%)</b></td><td>329.62 (+3.61%)</td><td>282.00 (+2.40%)</td><td>179.40 (+4.42%)</td><td>173.13 <b>(+37.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>475.00 (n/a)</td><td>318.12 (n/a)</td><td>275.40 (n/a)</td><td>171.80 (n/a)</td><td>125.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (-7.83%)</td><td>0.03 (+2.13%)</td><td>0.04 (+3.15%)</td><td>0.02 <b>(+31.35%)</b></td><td>0.01 <b>(-21.29%)</b></td><td>444.40 <b>(-23.86%)</b></td><td>336.90 (-6.57%)</td><td>285.80 (-3.05%)</td><td>256.80 (+8.49%)</td><td>90.51 <b>(-35.14%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.70 (n/a)</td><td>360.58 (n/a)</td><td>294.80 (n/a)</td><td>236.70 (n/a)</td><td>139.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (+9.62%)</td><td>0.03 (-13.45%)</td><td>0.04 (-6.14%)</td><td>0.02 <b>(-31.26%)</b></td><td>0.01 <b>(+138.73%)</b></td><td>546.50 <b>(+45.46%)</b></td><td>377.36 <b>(+27.86%)</b></td><td>297.60 (+6.51%)</td><td>242.60 (-8.76%)</td><td>148.18 <b>(+226.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>375.70 (n/a)</td><td>295.14 (n/a)</td><td>279.40 (n/a)</td><td>265.90 (n/a)</td><td>45.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 <b>(+26.94%)</b></td><td>0.04 (+6.81%)</td><td>0.03 (-16.42%)</td><td>0.02 <b>(+27.94%)</b></td><td>0.02 (+11.09%)</td><td>548.50 <b>(-21.83%)</b></td><td>344.76 (-9.87%)</td><td>303.10 (+19.66%)</td><td>183.60 <b>(-21.20%)</b></td><td>146.53 <b>(-28.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>701.70 (n/a)</td><td>382.50 (n/a)</td><td>253.30 (n/a)</td><td>233.00 (n/a)</td><td>203.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 <b>(+41.48%)</b></td><td>0.04 (+13.45%)</td><td>0.04 (+3.65%)</td><td>0.02 <b>(-21.05%)</b></td><td>0.02 <b>(+57.58%)</b></td><td>611.10 <b>(+26.68%)</b></td><td>335.04 (-3.54%)</td><td>255.00 (-3.52%)</td><td>177.40 <b>(-29.32%)</b></td><td>171.75 <b>(+42.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.40 (n/a)</td><td>347.34 (n/a)</td><td>264.30 (n/a)</td><td>251.00 (n/a)</td><td>120.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (-9.32%)</td><td>0.03 (-12.49%)</td><td>0.02 <b>(-31.05%)</b></td><td>0.02 <b>(+247.63%)</b></td><td>0.01 <b>(-37.51%)</b></td><td>620.00 <b>(-71.23%)</b></td><td>437.20 <b>(-34.09%)</b></td><td>452.10 <b>(+45.04%)</b></td><td>277.90 (+10.28%)</td><td>144.80 <b>(-82.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2155.20 (n/a)</td><td>663.36 (n/a)</td><td>311.70 (n/a)</td><td>252.00 (n/a)</td><td>834.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 <b>(+31.79%)</b></td><td>0.08 (+12.00%)</td><td>0.07 (-6.78%)</td><td>0.04 (-10.05%)</td><td>0.03 <b>(+41.98%)</b></td><td>546.80 (+11.18%)</td><td>307.38 (-5.76%)</td><td>283.20 (+7.27%)</td><td>159.40 <b>(-24.13%)</b></td><td>144.20 <b>(+20.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>491.80 (n/a)</td><td>326.18 (n/a)</td><td>264.00 (n/a)</td><td>210.10 (n/a)</td><td>119.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 <b>(-36.60%)</b></td><td>0.05 <b>(-33.13%)</b></td><td>0.05 <b>(-44.87%)</b></td><td>0.02 <b>(+117.97%)</b></td><td>0.02 <b>(-55.25%)</b></td><td>886.20 <b>(-54.12%)</b></td><td>502.36 (-14.33%)</td><td>466.40 <b>(+81.41%)</b></td><td>321.70 <b>(+57.70%)</b></td><td>224.31 <b>(-70.20%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1931.60 (n/a)</td><td>586.40 (n/a)</td><td>257.10 (n/a)</td><td>204.00 (n/a)</td><td>752.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (-18.10%)</td><td>0.05 (-12.19%)</td><td>0.05 (+4.82%)</td><td>0.04 <b>(+27.04%)</b></td><td>0.01 <b>(-56.05%)</b></td><td>477.80 <b>(-21.29%)</b></td><td>430.26 (+1.32%)</td><td>463.90 (-4.59%)</td><td>299.90 <b>(+22.11%)</b></td><td>74.14 <b>(-55.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>607.00 (n/a)</td><td>424.66 (n/a)</td><td>486.20 (n/a)</td><td>245.60 (n/a)</td><td>167.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (+5.68%)</td><td>0.06 (-4.28%)</td><td>0.06 (-4.97%)</td><td>0.03 (+4.35%)</td><td>0.02 (+15.74%)</td><td>620.60 (-4.17%)</td><td>399.06 (+5.79%)</td><td>345.20 (+5.24%)</td><td>243.20 (-5.37%)</td><td>152.30 (-1.47%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.60 (n/a)</td><td>377.22 (n/a)</td><td>328.00 (n/a)</td><td>257.00 (n/a)</td><td>154.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(+30.32%)</b></td><td>0.07 <b>(+22.84%)</b></td><td>0.07 <b>(+52.62%)</b></td><td>0.03 (-17.41%)</td><td>0.03 <b>(+70.01%)</b></td><td>683.40 <b>(+21.08%)</b></td><td>378.06 (-10.08%)</td><td>299.30 <b>(-34.48%)</b></td><td>221.30 <b>(-23.27%)</b></td><td>188.13 <b>(+65.19%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.40 (n/a)</td><td>420.46 (n/a)</td><td>456.80 (n/a)</td><td>288.40 (n/a)</td><td>113.88 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(+41.00%)</b></td><td>0.06 <b>(+36.53%)</b></td><td>0.05 <b>(+35.71%)</b></td><td>0.03 (+2.96%)</td><td>0.03 <b>(+76.27%)</b></td><td>610.90 (-2.88%)</td><td>387.52 <b>(-21.08%)</b></td><td>401.00 <b>(-26.30%)</b></td><td>206.70 <b>(-29.07%)</b></td><td>159.53 <b>(+23.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.00 (n/a)</td><td>491.00 (n/a)</td><td>544.10 (n/a)</td><td>291.40 (n/a)</td><td>129.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>349.10 (n/a)</td><td>298.50 (n/a)</td><td>308.10 (n/a)</td><td>228.90 (n/a)</td><td>44.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2057.50 (n/a)</td><td>658.10 (n/a)</td><td>257.60 (n/a)</td><td>216.90 (n/a)</td><td>792.66 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.80 (n/a)</td><td>393.44 (n/a)</td><td>297.40 (n/a)</td><td>259.40 (n/a)</td><td>155.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>555.10 (n/a)</td><td>338.12 (n/a)</td><td>274.50 (n/a)</td><td>234.60 (n/a)</td><td>131.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>508.40 (n/a)</td><td>340.80 (n/a)</td><td>259.30 (n/a)</td><td>202.80 (n/a)</td><td>144.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>577.20 (n/a)</td><td>371.84 (n/a)</td><td>249.70 (n/a)</td><td>240.50 (n/a)</td><td>172.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>419.70 (n/a)</td><td>294.06 (n/a)</td><td>263.70 (n/a)</td><td>245.50 (n/a)</td><td>72.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>701.60 (n/a)</td><td>398.58 (n/a)</td><td>247.60 (n/a)</td><td>219.40 (n/a)</td><td>226.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>314.70 (n/a)</td><td>265.34 (n/a)</td><td>251.80 (n/a)</td><td>239.60 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 <b>(-21.95%)</b></td><td>0.12 <b>(-29.10%)</b></td><td>0.10 <b>(-44.25%)</b></td><td>0.08 (-13.46%)</td><td>0.04 (-14.20%)</td><td>593.30 (+15.56%)</td><td>430.50 <b>(+40.65%)</b></td><td>470.30 <b>(+79.37%)</b></td><td>285.90 <b>(+28.15%)</b></td><td>131.85 (+12.34%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>513.40 (n/a)</td><td>306.08 (n/a)</td><td>262.20 (n/a)</td><td>223.10 (n/a)</td><td>117.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>580.60 (n/a)</td><td>481.06 (n/a)</td><td>537.60 (n/a)</td><td>228.30 (n/a)</td><td>144.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>1944.90 (n/a)</td><td>711.78 (n/a)</td><td>513.00 (n/a)</td><td>187.00 (n/a)</td><td>708.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.40 (n/a)</td><td>424.16 (n/a)</td><td>379.40 (n/a)</td><td>300.80 (n/a)</td><td>116.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>490.70 (n/a)</td><td>351.68 (n/a)</td><td>271.70 (n/a)</td><td>247.80 (n/a)</td><td>122.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.40 (n/a)</td><td>477.32 (n/a)</td><td>484.30 (n/a)</td><td>249.50 (n/a)</td><td>149.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.50 (n/a)</td><td>355.76 (n/a)</td><td>287.20 (n/a)</td><td>263.90 (n/a)</td><td>113.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>647.80 (n/a)</td><td>476.18 (n/a)</td><td>425.70 (n/a)</td><td>388.10 (n/a)</td><td>103.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>809.90 (n/a)</td><td>472.40 (n/a)</td><td>461.70 (n/a)</td><td>245.30 (n/a)</td><td>209.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>516.50 (n/a)</td><td>387.12 (n/a)</td><td>419.50 (n/a)</td><td>260.70 (n/a)</td><td>113.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>496.20 (n/a)</td><td>365.22 (n/a)</td><td>291.20 (n/a)</td><td>268.30 (n/a)</td><td>119.31 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>532.10 (n/a)</td><td>432.68 (n/a)</td><td>431.20 (n/a)</td><td>285.50 (n/a)</td><td>102.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>546.00 (n/a)</td><td>373.12 (n/a)</td><td>339.70 (n/a)</td><td>229.70 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>586.50 (n/a)</td><td>421.62 (n/a)</td><td>412.80 (n/a)</td><td>192.90 (n/a)</td><td>148.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.16 (+1.13%)</td><td>3.33 (+13.71%)</td><td>3.48 <b>(+45.86%)</b></td><td>1.89 (+7.31%)</td><td>0.90 (-16.30%)</td><td>5558.80 (-6.81%)</td><td>3407.72 (-14.56%)</td><td>3014.30 <b>(-31.44%)</b></td><td>2520.30 (-1.12%)</td><td>1242.54 (-13.69%)</td><td>1704.13 (+1.13%)</td><td>1365.81 (+13.71%)</td><td>1424.85 <b>(+45.86%)</b></td><td>772.64 (+7.31%)</td><td>368.83 (-16.30%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.11 (n/a)</td><td>2.93 (n/a)</td><td>2.38 (n/a)</td><td>1.76 (n/a)</td><td>1.08 (n/a)</td><td>5965.10 (n/a)</td><td>3988.32 (n/a)</td><td>4396.70 (n/a)</td><td>2548.90 (n/a)</td><td>1439.64 (n/a)</td><td>1685.06 (n/a)</td><td>1201.10 (n/a)</td><td>976.86 (n/a)</td><td>720.02 (n/a)</td><td>440.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.84 (+0.27%)</td><td>3.65 (+18.90%)</td><td>3.71 (+12.20%)</td><td>3.40 <b>(+82.42%)</b></td><td>0.17 <b>(-77.84%)</b></td><td>6930.80 <b>(-45.18%)</b></td><td>6474.84 <b>(-20.91%)</b></td><td>6363.30 (-10.87%)</td><td>6146.40 (-0.27%)</td><td>302.75 <b>(-88.34%)</b></td><td>2183.69 (+0.27%)</td><td>2076.47 (+18.90%)</td><td>2109.26 (+12.20%)</td><td>1936.54 <b>(+82.42%)</b></td><td>95.00 <b>(-77.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.83 (n/a)</td><td>3.07 (n/a)</td><td>3.30 (n/a)</td><td>1.87 (n/a)</td><td>0.75 (n/a)</td><td>12643.40 (n/a)</td><td>8186.32 (n/a)</td><td>7139.40 (n/a)</td><td>6163.00 (n/a)</td><td>2596.04 (n/a)</td><td>2177.80 (n/a)</td><td>1746.42 (n/a)</td><td>1879.97 (n/a)</td><td>1061.56 (n/a)</td><td>428.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.87 (-0.22%)</td><td>3.18 (-11.01%)</td><td>3.22 (-11.50%)</td><td>2.54 <b>(-21.17%)</b></td><td>0.48 <b>(+66.25%)</b></td><td>6609.10 <b>(+26.85%)</b></td><td>5374.14 (+13.84%)</td><td>5207.00 (+12.99%)</td><td>4339.80 (+0.21%)</td><td>818.42 <b>(+112.25%)</b></td><td>1979.34 (-0.22%)</td><td>1627.72 (-11.01%)</td><td>1649.69 (-11.50%)</td><td>1299.70 <b>(-21.17%)</b></td><td>243.80 <b>(+66.25%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.87 (n/a)</td><td>3.57 (n/a)</td><td>3.64 (n/a)</td><td>3.22 (n/a)</td><td>0.29 (n/a)</td><td>5210.20 (n/a)</td><td>4720.78 (n/a)</td><td>4608.30 (n/a)</td><td>4330.50 (n/a)</td><td>385.60 (n/a)</td><td>1983.61 (n/a)</td><td>1829.18 (n/a)</td><td>1864.01 (n/a)</td><td>1648.68 (n/a)</td><td>146.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.98 (+11.26%)</td><td>0.69 (-11.29%)</td><td>0.68 (-19.80%)</td><td>0.44 <b>(-30.15%)</b></td><td>0.20 <b>(+71.76%)</b></td><td>1041.50 <b>(+43.18%)</b></td><td>708.76 (+18.47%)</td><td>674.60 <b>(+24.67%)</b></td><td>470.30 (-10.13%)</td><td>213.69 <b>(+126.81%)</b></td><td>71.34 (+11.26%)</td><td>50.70 (-11.29%)</td><td>49.74 (-19.80%)</td><td>32.22 <b>(-30.15%)</b></td><td>14.45 <b>(+71.76%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.88 (n/a)</td><td>0.78 (n/a)</td><td>0.85 (n/a)</td><td>0.63 (n/a)</td><td>0.12 (n/a)</td><td>727.40 (n/a)</td><td>598.24 (n/a)</td><td>541.10 (n/a)</td><td>523.30 (n/a)</td><td>94.22 (n/a)</td><td>64.12 (n/a)</td><td>57.15 (n/a)</td><td>62.02 (n/a)</td><td>46.13 (n/a)</td><td>8.41 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.22 <b>(-24.37%)</b></td><td>1.02 (-16.39%)</td><td>0.96 <b>(-30.48%)</b></td><td>0.73 (+13.09%)</td><td>0.21 <b>(-50.21%)</b></td><td>892.80 (-11.58%)</td><td>666.88 (+10.05%)</td><td>683.70 <b>(+43.85%)</b></td><td>536.20 <b>(+32.20%)</b></td><td>146.12 <b>(-42.83%)</b></td><td>125.15 <b>(-24.37%)</b></td><td>104.28 (-16.39%)</td><td>98.16 <b>(-30.48%)</b></td><td>75.17 (+13.09%)</td><td>21.10 <b>(-50.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.62 (n/a)</td><td>1.22 (n/a)</td><td>1.38 (n/a)</td><td>0.65 (n/a)</td><td>0.41 (n/a)</td><td>1009.70 (n/a)</td><td>605.98 (n/a)</td><td>475.30 (n/a)</td><td>405.60 (n/a)</td><td>255.62 (n/a)</td><td>165.48 (n/a)</td><td>124.72 (n/a)</td><td>141.19 (n/a)</td><td>66.47 (n/a)</td><td>42.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.48 (-14.54%)</td><td>1.27 (-12.02%)</td><td>1.35 (+0.54%)</td><td>0.97 <b>(-23.11%)</b></td><td>0.21 (+8.59%)</td><td>774.70 <b>(+30.07%)</b></td><td>608.52 (+14.91%)</td><td>556.40 (-0.54%)</td><td>510.50 (+17.01%)</td><td>111.94 <b>(+64.67%)</b></td><td>164.31 (-14.54%)</td><td>141.34 (-12.02%)</td><td>150.76 (+0.54%)</td><td>108.29 <b>(-23.11%)</b></td><td>23.82 (+8.59%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.73 (n/a)</td><td>1.44 (n/a)</td><td>1.35 (n/a)</td><td>1.27 (n/a)</td><td>0.20 (n/a)</td><td>595.60 (n/a)</td><td>529.58 (n/a)</td><td>559.40 (n/a)</td><td>436.30 (n/a)</td><td>67.98 (n/a)</td><td>192.27 (n/a)</td><td>160.65 (n/a)</td><td>149.95 (n/a)</td><td>140.84 (n/a)</td><td>21.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.59 (-7.83%)</td><td>1.37 (+10.48%)</td><td>1.44 <b>(+22.34%)</b></td><td>1.15 <b>(+65.45%)</b></td><td>0.21 <b>(-46.62%)</b></td><td>915.20 <b>(-39.56%)</b></td><td>778.00 (-16.07%)</td><td>730.40 (-18.26%)</td><td>657.70 (+8.50%)</td><td>120.52 <b>(-65.63%)</b></td><td>204.08 (-7.83%)</td><td>175.78 (+10.48%)</td><td>183.76 <b>(+22.34%)</b></td><td>146.65 <b>(+65.45%)</b></td><td>26.36 <b>(-46.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.73 (n/a)</td><td>1.24 (n/a)</td><td>1.17 (n/a)</td><td>0.69 (n/a)</td><td>0.39 (n/a)</td><td>1514.20 (n/a)</td><td>926.96 (n/a)</td><td>893.60 (n/a)</td><td>606.20 (n/a)</td><td>350.68 (n/a)</td><td>221.42 (n/a)</td><td>159.11 (n/a)</td><td>150.21 (n/a)</td><td>88.64 (n/a)</td><td>49.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.86 (-13.99%)</td><td>1.58 (-3.78%)</td><td>1.47 <b>(-25.14%)</b></td><td>1.32 <b>(+329.42%)</b></td><td>0.22 <b>(-70.70%)</b></td><td>793.90 <b>(-76.71%)</b></td><td>676.50 <b>(-39.17%)</b></td><td>711.70 <b>(+33.58%)</b></td><td>565.20 (+16.27%)</td><td>94.66 <b>(-92.64%)</b></td><td>237.49 (-13.99%)</td><td>201.62 (-3.78%)</td><td>188.59 <b>(-25.14%)</b></td><td>169.07 <b>(+329.42%)</b></td><td>28.78 <b>(-70.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.16 (n/a)</td><td>1.64 (n/a)</td><td>1.97 (n/a)</td><td>0.31 (n/a)</td><td>0.77 (n/a)</td><td>3409.00 (n/a)</td><td>1112.16 (n/a)</td><td>532.80 (n/a)</td><td>486.10 (n/a)</td><td>1285.23 (n/a)</td><td>276.10 (n/a)</td><td>209.53 (n/a)</td><td>251.92 (n/a)</td><td>39.37 (n/a)</td><td>98.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.01 (-15.14%)</td><td>1.61 (+6.21%)</td><td>1.63 (+9.16%)</td><td>1.03 <b>(+138.47%)</b></td><td>0.42 <b>(-40.43%)</b></td><td>1021.10 <b>(-58.06%)</b></td><td>693.20 <b>(-28.76%)</b></td><td>642.30 (-8.39%)</td><td>522.50 (+17.84%)</td><td>207.57 <b>(-74.82%)</b></td><td>256.89 (-15.14%)</td><td>206.25 (+6.21%)</td><td>208.96 (+9.16%)</td><td>131.45 <b>(+138.47%)</b></td><td>53.74 <b>(-40.43%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.36 (n/a)</td><td>1.52 (n/a)</td><td>1.50 (n/a)</td><td>0.43 (n/a)</td><td>0.70 (n/a)</td><td>2434.90 (n/a)</td><td>973.06 (n/a)</td><td>701.10 (n/a)</td><td>443.40 (n/a)</td><td>824.26 (n/a)</td><td>302.71 (n/a)</td><td>194.19 (n/a)</td><td>191.43 (n/a)</td><td>55.12 (n/a)</td><td>90.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.87 <b>(-21.15%)</b></td><td>1.33 <b>(-34.92%)</b></td><td>1.68 <b>(-23.06%)</b></td><td>0.50 <b>(-70.82%)</b></td><td>0.64 <b>(+119.36%)</b></td><td>2110.20 <b>(+242.73%)</b></td><td>1037.62 <b>(+99.39%)</b></td><td>623.90 <b>(+29.95%)</b></td><td>559.60 <b>(+26.84%)</b></td><td>678.83 <b>(+782.71%)</b></td><td>239.86 <b>(-21.15%)</b></td><td>170.73 <b>(-34.92%)</b></td><td>215.12 <b>(-23.06%)</b></td><td>63.61 <b>(-70.82%)</b></td><td>82.01 <b>(+119.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.38 (n/a)</td><td>2.05 (n/a)</td><td>2.18 (n/a)</td><td>1.70 (n/a)</td><td>0.29 (n/a)</td><td>615.70 (n/a)</td><td>520.40 (n/a)</td><td>480.10 (n/a)</td><td>441.20 (n/a)</td><td>76.90 (n/a)</td><td>304.22 (n/a)</td><td>262.33 (n/a)</td><td>279.58 (n/a)</td><td>217.98 (n/a)</td><td>37.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.62 (+0.72%)</td><td>1.10 (+0.24%)</td><td>1.25 <b>(+28.70%)</b></td><td>0.30 <b>(-36.62%)</b></td><td>0.55 (+12.30%)</td><td>3545.10 <b>(+57.78%)</b></td><td>1407.46 (+19.79%)</td><td>842.10 <b>(-22.30%)</b></td><td>645.80 (-0.71%)</td><td>1224.41 <b>(+88.17%)</b></td><td>207.84 (+0.72%)</td><td>140.47 (+0.24%)</td><td>159.38 <b>(+28.70%)</b></td><td>37.86 <b>(-36.62%)</b></td><td>70.59 (+12.30%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.61 (n/a)</td><td>1.09 (n/a)</td><td>0.97 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>2246.90 (n/a)</td><td>1174.90 (n/a)</td><td>1083.80 (n/a)</td><td>650.40 (n/a)</td><td>650.70 (n/a)</td><td>206.35 (n/a)</td><td>140.13 (n/a)</td><td>123.84 (n/a)</td><td>59.74 (n/a)</td><td>62.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.96 (+12.25%)</td><td>1.29 (+17.43%)</td><td>1.27 (-15.46%)</td><td>0.63 <b>(+111.35%)</b></td><td>0.53 <b>(-21.34%)</b></td><td>1655.40 <b>(-52.69%)</b></td><td>954.22 <b>(-39.61%)</b></td><td>825.40 (+18.29%)</td><td>534.80 (-10.93%)</td><td>450.20 <b>(-65.68%)</b></td><td>250.95 (+12.25%)</td><td>165.02 (+17.43%)</td><td>162.62 (-15.46%)</td><td>81.08 <b>(+111.35%)</b></td><td>68.02 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.75 (n/a)</td><td>1.10 (n/a)</td><td>1.50 (n/a)</td><td>0.30 (n/a)</td><td>0.68 (n/a)</td><td>3498.70 (n/a)</td><td>1579.98 (n/a)</td><td>697.80 (n/a)</td><td>600.40 (n/a)</td><td>1311.61 (n/a)</td><td>223.56 (n/a)</td><td>140.52 (n/a)</td><td>192.36 (n/a)</td><td>38.36 (n/a)</td><td>86.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.84 (-4.66%)</td><td>0.52 <b>(-23.80%)</b></td><td>0.41 <b>(-44.77%)</b></td><td>0.37 <b>(-26.08%)</b></td><td>0.21 <b>(+25.07%)</b></td><td>986.40 <b>(+35.29%)</b></td><td>768.94 <b>(+38.91%)</b></td><td>872.80 <b>(+81.08%)</b></td><td>428.60 (+4.89%)</td><td>249.85 <b>(+77.85%)</b></td><td>39.15 (-4.66%)</td><td>24.27 <b>(-23.80%)</b></td><td>19.22 <b>(-44.77%)</b></td><td>17.01 <b>(-26.08%)</b></td><td>9.60 <b>(+25.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.88 (n/a)</td><td>0.68 (n/a)</td><td>0.75 (n/a)</td><td>0.49 (n/a)</td><td>0.16 (n/a)</td><td>729.10 (n/a)</td><td>553.56 (n/a)</td><td>482.00 (n/a)</td><td>408.60 (n/a)</td><td>140.49 (n/a)</td><td>41.06 (n/a)</td><td>31.85 (n/a)</td><td>34.81 (n/a)</td><td>23.01 (n/a)</td><td>7.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.04 (-1.25%)</td><td>1.82 (-9.49%)</td><td>1.61 (-16.20%)</td><td>1.10 (+11.43%)</td><td>0.78 (-3.07%)</td><td>3815.10 (-10.26%)</td><td>2622.76 (+8.20%)</td><td>2608.90 (+19.33%)</td><td>1377.90 (+1.27%)</td><td>969.91 (-13.94%)</td><td>779.26 (-1.25%)</td><td>465.75 (-9.49%)</td><td>411.57 (-16.20%)</td><td>281.45 (+11.43%)</td><td>199.07 (-3.07%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.08 (n/a)</td><td>2.01 (n/a)</td><td>1.92 (n/a)</td><td>0.99 (n/a)</td><td>0.80 (n/a)</td><td>4251.20 (n/a)</td><td>2424.08 (n/a)</td><td>2186.20 (n/a)</td><td>1360.60 (n/a)</td><td>1126.97 (n/a)</td><td>789.14 (n/a)</td><td>514.57 (n/a)</td><td>491.14 (n/a)</td><td>252.57 (n/a)</td><td>205.38 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.60 (+0.44%)</td><td>2.50 (+19.76%)</td><td>3.30 <b>(+146.91%)</b></td><td>0.80 (+18.78%)</td><td>1.37 (-0.47%)</td><td>3268.40 (-15.81%)</td><td>1533.86 (-17.98%)</td><td>794.60 <b>(-59.50%)</b></td><td>727.70 (-0.42%)</td><td>1141.82 (-11.52%)</td><td>737.81 (+0.44%)</td><td>511.71 (+19.76%)</td><td>675.63 <b>(+146.91%)</b></td><td>164.26 (+18.78%)</td><td>280.53 (-0.47%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.59 (n/a)</td><td>2.09 (n/a)</td><td>1.34 (n/a)</td><td>0.68 (n/a)</td><td>1.38 (n/a)</td><td>3882.30 (n/a)</td><td>1870.20 (n/a)</td><td>1962.00 (n/a)</td><td>730.80 (n/a)</td><td>1290.55 (n/a)</td><td>734.60 (n/a)</td><td>427.28 (n/a)</td><td>273.63 (n/a)</td><td>138.29 (n/a)</td><td>281.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.21 (-2.23%)</td><td>2.75 (+2.05%)</td><td>2.99 (+9.53%)</td><td>1.67 (-16.24%)</td><td>0.62 <b>(+36.01%)</b></td><td>4702.40 (+19.39%)</td><td>3028.70 (+1.19%)</td><td>2629.40 (-8.70%)</td><td>2447.30 (+2.29%)</td><td>946.44 <b>(+66.29%)</b></td><td>987.19 (-2.23%)</td><td>845.35 (+2.05%)</td><td>918.82 (+9.53%)</td><td>513.77 (-16.24%)</td><td>191.85 <b>(+36.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.29 (n/a)</td><td>2.70 (n/a)</td><td>2.73 (n/a)</td><td>2.00 (n/a)</td><td>0.46 (n/a)</td><td>3938.60 (n/a)</td><td>2992.94 (n/a)</td><td>2879.90 (n/a)</td><td>2392.60 (n/a)</td><td>569.14 (n/a)</td><td>1009.74 (n/a)</td><td>828.35 (n/a)</td><td>838.89 (n/a)</td><td>613.40 (n/a)</td><td>141.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.00 (n/a)</td><td>320.34 (n/a)</td><td>281.40 (n/a)</td><td>244.50 (n/a)</td><td>126.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1082.20 (n/a)</td><td>560.72 (n/a)</td><td>549.20 (n/a)</td><td>243.30 (n/a)</td><td>333.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.30 (n/a)</td><td>377.70 (n/a)</td><td>301.20 (n/a)</td><td>268.90 (n/a)</td><td>133.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.20 (n/a)</td><td>408.50 (n/a)</td><td>452.30 (n/a)</td><td>282.30 (n/a)</td><td>92.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.70 (n/a)</td><td>444.78 (n/a)</td><td>501.60 (n/a)</td><td>198.20 (n/a)</td><td>142.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.50 (n/a)</td><td>422.48 (n/a)</td><td>432.20 (n/a)</td><td>278.00 (n/a)</td><td>114.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.60 (n/a)</td><td>445.60 (n/a)</td><td>448.30 (n/a)</td><td>267.40 (n/a)</td><td>119.99 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.70 (n/a)</td><td>412.50 (n/a)</td><td>374.30 (n/a)</td><td>283.70 (n/a)</td><td>136.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.20 (n/a)</td><td>463.00 (n/a)</td><td>512.00 (n/a)</td><td>221.20 (n/a)</td><td>159.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>709.50 (n/a)</td><td>541.46 (n/a)</td><td>600.10 (n/a)</td><td>224.20 (n/a)</td><td>188.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.80 (n/a)</td><td>447.84 (n/a)</td><td>461.80 (n/a)</td><td>301.90 (n/a)</td><td>118.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1987.10 (n/a)</td><td>711.04 (n/a)</td><td>469.80 (n/a)</td><td>206.60 (n/a)</td><td>731.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.60 (n/a)</td><td>449.18 (n/a)</td><td>516.20 (n/a)</td><td>254.00 (n/a)</td><td>176.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>661.60 (n/a)</td><td>430.52 (n/a)</td><td>314.40 (n/a)</td><td>301.20 (n/a)</td><td>170.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>555.90 (n/a)</td><td>391.20 (n/a)</td><td>435.70 (n/a)</td><td>184.80 (n/a)</td><td>167.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.20 (n/a)</td><td>361.02 (n/a)</td><td>290.80 (n/a)</td><td>267.90 (n/a)</td><td>116.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.60 (n/a)</td><td>375.30 (n/a)</td><td>290.20 (n/a)</td><td>244.80 (n/a)</td><td>143.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2419.70 (n/a)</td><td>858.22 (n/a)</td><td>492.60 (n/a)</td><td>292.10 (n/a)</td><td>880.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>886.30 (n/a)</td><td>556.80 (n/a)</td><td>548.40 (n/a)</td><td>297.20 (n/a)</td><td>243.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>357.70 (n/a)</td><td>308.46 (n/a)</td><td>301.90 (n/a)</td><td>275.50 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>673.20 (n/a)</td><td>361.20 (n/a)</td><td>301.60 (n/a)</td><td>212.60 (n/a)</td><td>180.88 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.10 (n/a)</td><td>372.18 (n/a)</td><td>286.20 (n/a)</td><td>272.00 (n/a)</td><td>139.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.30 (n/a)</td><td>384.60 (n/a)</td><td>299.80 (n/a)</td><td>259.30 (n/a)</td><td>147.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>589.30 (n/a)</td><td>382.44 (n/a)</td><td>381.00 (n/a)</td><td>210.20 (n/a)</td><td>153.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.60 <b>(+23.69%)</b></td><td>0.50 <b>(+22.55%)</b></td><td>0.52 <b>(+26.70%)</b></td><td>0.34 (+4.84%)</td><td>0.10 <b>(+57.03%)</b></td><td>645.20 (-4.61%)</td><td>456.02 (-16.87%)</td><td>422.60 <b>(-21.07%)</b></td><td>368.80 (-19.14%)</td><td>109.90 <b>(+25.58%)</b></td><td>25.59 <b>(+23.69%)</b></td><td>21.50 <b>(+22.55%)</b></td><td>22.33 <b>(+26.70%)</b></td><td>14.63 (+4.84%)</td><td>4.20 <b>(+57.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>676.40 (n/a)</td><td>548.58 (n/a)</td><td>535.40 (n/a)</td><td>456.10 (n/a)</td><td>87.51 (n/a)</td><td>20.69 (n/a)</td><td>17.54 (n/a)</td><td>17.63 (n/a)</td><td>13.95 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.56 (-12.21%)</td><td>0.39 (+0.05%)</td><td>0.40 (+1.94%)</td><td>0.09 <b>(-27.61%)</b></td><td>0.19 (+5.00%)</td><td>2445.60 <b>(+38.14%)</b></td><td>888.62 (+16.57%)</td><td>556.90 (-1.90%)</td><td>392.40 (+13.90%)</td><td>877.34 <b>(+53.13%)</b></td><td>24.05 (-12.21%)</td><td>16.63 (+0.05%)</td><td>16.95 (+1.94%)</td><td>3.86 <b>(-27.61%)</b></td><td>8.29 (+5.00%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.64 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.12 (n/a)</td><td>0.18 (n/a)</td><td>1770.40 (n/a)</td><td>762.30 (n/a)</td><td>567.70 (n/a)</td><td>344.50 (n/a)</td><td>572.93 (n/a)</td><td>27.39 (n/a)</td><td>16.62 (n/a)</td><td>16.62 (n/a)</td><td>5.33 (n/a)</td><td>7.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.31 (-0.91%)</td><td>0.31 (-0.03%)</td><td>0.31 (+0.05%)</td><td>0.30 (+0.08%)</td><td>0.00 (-16.52%)</td><td>84282.20 (-0.08%)</td><td>82439.40 (+0.02%)</td><td>82390.40 (-0.05%)</td><td>81199.40 (+0.91%)</td><td>1203.07 (-15.77%)</td><td>211.58 (-0.91%)</td><td>208.43 (-0.03%)</td><td>208.52 (+0.05%)</td><td>203.84 (+0.08%)</td><td>3.02 (-16.52%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84352.70 (n/a)</td><td>82420.52 (n/a)</td><td>82433.20 (n/a)</td><td>80463.50 (n/a)</td><td>1428.32 (n/a)</td><td>213.51 (n/a)</td><td>208.49 (n/a)</td><td>208.41 (n/a)</td><td>203.67 (n/a)</td><td>3.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.15 (+0.16%)</td><td>1.14 (-0.05%)</td><td>1.14 (-0.12%)</td><td>1.11 (-1.32%)</td><td>0.02 <b>(+57.33%)</b></td><td>22606.10 (+1.34%)</td><td>22092.02 (+0.06%)</td><td>22028.90 (+0.12%)</td><td>21800.00 (-0.16%)</td><td>313.79 <b>(+59.25%)</b></td><td>788.07 (+0.16%)</td><td>777.77 (-0.05%)</td><td>779.88 (-0.12%)</td><td>759.96 (-1.32%)</td><td>10.92 <b>(+57.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>0.01 (n/a)</td><td>22306.90 (n/a)</td><td>22079.24 (n/a)</td><td>22002.90 (n/a)</td><td>21835.70 (n/a)</td><td>197.05 (n/a)</td><td>786.78 (n/a)</td><td>778.15 (n/a)</td><td>780.80 (n/a)</td><td>770.16 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.80 (-0.02%)</td><td>0.79 (+0.68%)</td><td>0.79 (+1.01%)</td><td>0.78 (+0.90%)</td><td>0.01 <b>(-28.59%)</b></td><td>97237.40 (-0.89%)</td><td>95687.10 (-0.69%)</td><td>95152.20 (-1.00%)</td><td>94597.40 (+0.02%)</td><td>1110.11 <b>(-29.29%)</b></td><td>726.44 (-0.02%)</td><td>718.25 (+0.68%)</td><td>722.21 (+1.01%)</td><td>706.72 (+0.90%)</td><td>8.29 <b>(-28.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98111.30 (n/a)</td><td>96347.94 (n/a)</td><td>96116.20 (n/a)</td><td>94580.60 (n/a)</td><td>1569.88 (n/a)</td><td>726.57 (n/a)</td><td>713.39 (n/a)</td><td>714.96 (n/a)</td><td>700.42 (n/a)</td><td>11.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.78 (+0.32%)</td><td>0.77 (+0.59%)</td><td>0.77 (+0.71%)</td><td>0.75 (-0.72%)</td><td>0.01 <b>(+39.54%)</b></td><td>100105.00 (+0.72%)</td><td>97820.92 (-0.58%)</td><td>97524.20 (-0.70%)</td><td>96761.20 (-0.32%)</td><td>1342.60 <b>(+40.13%)</b></td><td>710.20 (+0.32%)</td><td>702.61 (+0.59%)</td><td>704.64 (+0.71%)</td><td>686.47 (-0.72%)</td><td>9.51 <b>(+39.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99388.60 (n/a)</td><td>98391.12 (n/a)</td><td>98213.90 (n/a)</td><td>97074.90 (n/a)</td><td>958.10 (n/a)</td><td>707.90 (n/a)</td><td>698.48 (n/a)</td><td>699.69 (n/a)</td><td>691.42 (n/a)</td><td>6.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.89 (-0.14%)</td><td>0.89 (-0.04%)</td><td>0.89 (+0.28%)</td><td>0.88 (+0.04%)</td><td>0.01 (-13.77%)</td><td>86259.10 (-0.04%)</td><td>85214.20 (+0.03%)</td><td>85031.80 (-0.28%)</td><td>84530.00 (+0.14%)</td><td>638.47 (-13.53%)</td><td>812.96 (-0.14%)</td><td>806.47 (-0.04%)</td><td>808.16 (+0.28%)</td><td>796.66 (+0.04%)</td><td>6.01 (-13.77%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86293.70 (n/a)</td><td>85184.94 (n/a)</td><td>85270.30 (n/a)</td><td>84409.30 (n/a)</td><td>738.41 (n/a)</td><td>814.12 (n/a)</td><td>806.76 (n/a)</td><td>805.90 (n/a)</td><td>796.34 (n/a)</td><td>6.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.57 (-2.40%)</td><td>3.99 <b>(-21.94%)</b></td><td>3.56 <b>(-32.77%)</b></td><td>2.14 <b>(-48.75%)</b></td><td>1.51 <b>(+150.70%)</b></td><td>4167.90 <b>(+95.12%)</b></td><td>2538.42 <b>(+43.94%)</b></td><td>2502.40 <b>(+48.74%)</b></td><td>1601.10 (+2.46%)</td><td>1056.35 <b>(+363.18%)</b></td><td>335.32 (-2.40%)</td><td>240.54 <b>(-21.94%)</b></td><td>214.55 <b>(-32.77%)</b></td><td>128.81 <b>(-48.75%)</b></td><td>90.95 <b>(+150.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.70 (n/a)</td><td>5.12 (n/a)</td><td>5.30 (n/a)</td><td>4.17 (n/a)</td><td>0.60 (n/a)</td><td>2136.10 (n/a)</td><td>1763.54 (n/a)</td><td>1682.40 (n/a)</td><td>1562.60 (n/a)</td><td>228.07 (n/a)</td><td>343.57 (n/a)</td><td>308.16 (n/a)</td><td>319.10 (n/a)</td><td>251.33 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.60 (+1.23%)</td><td>3.49 (+10.92%)</td><td>3.46 (+10.29%)</td><td>2.12 (-0.29%)</td><td>0.93 (-6.04%)</td><td>4206.40 (+0.29%)</td><td>2738.30 (-10.69%)</td><td>2573.30 (-9.33%)</td><td>1938.30 (-1.22%)</td><td>877.84 (-6.19%)</td><td>276.98 (+1.23%)</td><td>209.95 (+10.92%)</td><td>208.63 (+10.29%)</td><td>127.63 (-0.29%)</td><td>55.76 (-6.04%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.54 (n/a)</td><td>3.14 (n/a)</td><td>3.14 (n/a)</td><td>2.13 (n/a)</td><td>0.99 (n/a)</td><td>4194.10 (n/a)</td><td>3065.96 (n/a)</td><td>2838.00 (n/a)</td><td>1962.30 (n/a)</td><td>935.78 (n/a)</td><td>273.60 (n/a)</td><td>189.28 (n/a)</td><td>189.17 (n/a)</td><td>128.01 (n/a)</td><td>59.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.89 (+4.91%)</td><td>3.98 (-14.47%)</td><td>4.06 (-2.79%)</td><td>2.18 <b>(-43.09%)</b></td><td>1.32 <b>(+55.00%)</b></td><td>4094.20 <b>(+75.72%)</b></td><td>2480.22 <b>(+26.19%)</b></td><td>2197.40 (+2.87%)</td><td>1512.80 (-4.68%)</td><td>963.74 <b>(+180.48%)</b></td><td>354.89 (+4.91%)</td><td>239.76 (-14.47%)</td><td>244.32 (-2.79%)</td><td>131.13 <b>(-43.09%)</b></td><td>79.74 <b>(+55.00%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.62 (n/a)</td><td>4.65 (n/a)</td><td>4.17 (n/a)</td><td>3.83 (n/a)</td><td>0.85 (n/a)</td><td>2330.00 (n/a)</td><td>1965.54 (n/a)</td><td>2136.10 (n/a)</td><td>1587.10 (n/a)</td><td>343.60 (n/a)</td><td>338.27 (n/a)</td><td>280.32 (n/a)</td><td>251.34 (n/a)</td><td>230.41 (n/a)</td><td>51.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>6.72 (+11.65%)</td><td>5.44 (-1.40%)</td><td>5.40 (-0.93%)</td><td>3.98 <b>(-22.49%)</b></td><td>1.07 <b>(+189.62%)</b></td><td>8770.80 <b>(+29.01%)</b></td><td>6622.92 (+4.50%)</td><td>6456.00 (+0.93%)</td><td>5185.20 (-10.44%)</td><td>1401.99 <b>(+235.33%)</b></td><td>414.16 (+11.65%)</td><td>335.28 (-1.40%)</td><td>332.63 (-0.93%)</td><td>244.84 <b>(-22.49%)</b></td><td>66.02 <b>(+189.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.02 (n/a)</td><td>5.52 (n/a)</td><td>5.45 (n/a)</td><td>5.13 (n/a)</td><td>0.37 (n/a)</td><td>6798.50 (n/a)</td><td>6337.98 (n/a)</td><td>6396.20 (n/a)</td><td>5789.50 (n/a)</td><td>418.09 (n/a)</td><td>370.93 (n/a)</td><td>340.03 (n/a)</td><td>335.75 (n/a)</td><td>315.87 (n/a)</td><td>22.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.35 (-2.21%)</td><td>4.76 (+4.21%)</td><td>4.67 (+3.83%)</td><td>4.04 (+16.48%)</td><td>0.53 <b>(-30.04%)</b></td><td>8627.10 (-14.15%)</td><td>7399.32 (-5.33%)</td><td>7467.40 (-3.69%)</td><td>6514.70 (+2.26%)</td><td>844.10 <b>(-39.84%)</b></td><td>329.64 (-2.21%)</td><td>293.18 (+4.21%)</td><td>287.58 (+3.83%)</td><td>248.92 (+16.48%)</td><td>32.51 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.47 (n/a)</td><td>4.57 (n/a)</td><td>4.50 (n/a)</td><td>3.47 (n/a)</td><td>0.75 (n/a)</td><td>10049.20 (n/a)</td><td>7816.28 (n/a)</td><td>7753.50 (n/a)</td><td>6370.60 (n/a)</td><td>1403.02 (n/a)</td><td>337.09 (n/a)</td><td>281.34 (n/a)</td><td>276.97 (n/a)</td><td>213.70 (n/a)</td><td>46.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.03 (+7.40%)</td><td>5.67 (-1.07%)</td><td>5.05 (-16.30%)</td><td>4.24 (+6.31%)</td><td>1.27 <b>(+26.34%)</b></td><td>8226.70 (-5.94%)</td><td>6394.74 (+1.93%)</td><td>6901.00 (+19.48%)</td><td>4957.30 (-6.89%)</td><td>1408.22 (+0.81%)</td><td>433.20 (+7.40%)</td><td>349.47 (-1.07%)</td><td>311.18 (-16.30%)</td><td>261.04 (+6.31%)</td><td>78.13 <b>(+26.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.55 (n/a)</td><td>5.74 (n/a)</td><td>6.04 (n/a)</td><td>3.99 (n/a)</td><td>1.00 (n/a)</td><td>8746.10 (n/a)</td><td>6273.92 (n/a)</td><td>5776.10 (n/a)</td><td>5324.30 (n/a)</td><td>1396.85 (n/a)</td><td>403.34 (n/a)</td><td>353.26 (n/a)</td><td>371.79 (n/a)</td><td>245.54 (n/a)</td><td>61.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.76 (-1.24%)</td><td>0.74 (-0.94%)</td><td>0.75 (-1.70%)</td><td>0.68 (-4.39%)</td><td>0.03 (+12.61%)</td><td>110868.60 (+4.59%)</td><td>102485.80 (+0.99%)</td><td>101104.80 (+1.72%)</td><td>98769.60 (+1.25%)</td><td>4786.52 (+19.79%)</td><td>695.76 (-1.24%)</td><td>671.64 (-0.94%)</td><td>679.69 (-1.70%)</td><td>619.83 (-4.39%)</td><td>29.73 (+12.61%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.03 (n/a)</td><td>106004.40 (n/a)</td><td>101483.68 (n/a)</td><td>99390.60 (n/a)</td><td>97547.30 (n/a)</td><td>3995.64 (n/a)</td><td>704.47 (n/a)</td><td>677.98 (n/a)</td><td>691.41 (n/a)</td><td>648.27 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.78 (-0.01%)</td><td>0.75 (-1.16%)</td><td>0.75 (-0.77%)</td><td>0.73 (-2.73%)</td><td>0.02 <b>(+70.44%)</b></td><td>103765.10 (+2.80%)</td><td>100253.26 (+1.21%)</td><td>100330.80 (+0.78%)</td><td>97347.20 (+0.01%)</td><td>2563.46 <b>(+75.33%)</b></td><td>705.92 (-0.01%)</td><td>685.82 (-1.16%)</td><td>684.93 (-0.77%)</td><td>662.26 (-2.73%)</td><td>17.46 <b>(+70.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100936.90 (n/a)</td><td>99053.78 (n/a)</td><td>99558.90 (n/a)</td><td>97340.20 (n/a)</td><td>1462.05 (n/a)</td><td>705.97 (n/a)</td><td>693.88 (n/a)</td><td>690.24 (n/a)</td><td>680.82 (n/a)</td><td>10.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.89 (-0.04%)</td><td>0.89 (+0.80%)</td><td>0.89 (+0.55%)</td><td>0.88 (+3.23%)</td><td>0.00 <b>(-73.73%)</b></td><td>85402.80 (-3.13%)</td><td>84957.84 (-0.82%)</td><td>84921.00 (-0.55%)</td><td>84384.50 (+0.04%)</td><td>380.39 <b>(-74.61%)</b></td><td>814.36 (-0.04%)</td><td>808.88 (+0.80%)</td><td>809.22 (+0.55%)</td><td>804.65 (+3.23%)</td><td>3.63 <b>(-73.73%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.02 (n/a)</td><td>88162.90 (n/a)</td><td>85656.82 (n/a)</td><td>85388.40 (n/a)</td><td>84351.70 (n/a)</td><td>1498.08 (n/a)</td><td>814.68 (n/a)</td><td>802.46 (n/a)</td><td>804.79 (n/a)</td><td>779.46 (n/a)</td><td>13.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.00 (-18.82%)</td><td>2.43 (+4.20%)</td><td>2.73 <b>(+28.94%)</b></td><td>1.62 (+1.99%)</td><td>0.63 <b>(-26.24%)</b></td><td>4980.40 (-1.95%)</td><td>3527.64 (-6.88%)</td><td>2949.50 <b>(-22.44%)</b></td><td>2682.90 <b>(+23.19%)</b></td><td>1028.76 (-12.41%)</td><td>787.91 (-18.82%)</td><td>637.49 (+4.20%)</td><td>716.71 <b>(+28.94%)</b></td><td>424.45 (+1.99%)</td><td>165.01 <b>(-26.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.70 (n/a)</td><td>2.33 (n/a)</td><td>2.12 (n/a)</td><td>1.59 (n/a)</td><td>0.85 (n/a)</td><td>5079.60 (n/a)</td><td>3788.26 (n/a)</td><td>3803.10 (n/a)</td><td>2177.90 (n/a)</td><td>1174.52 (n/a)</td><td>970.61 (n/a)</td><td>611.82 (n/a)</td><td>555.84 (n/a)</td><td>416.16 (n/a)</td><td>223.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.26 (+2.45%)</td><td>0.21 (+2.94%)</td><td>0.20 (+4.73%)</td><td>0.17 (+5.53%)</td><td>0.03 (-18.35%)</td><td>7288.60 (-5.24%)</td><td>6062.78 (-3.91%)</td><td>6079.10 (-4.52%)</td><td>4862.20 (-2.39%)</td><td>886.26 <b>(-24.52%)</b></td><td>13.80 (+2.45%)</td><td>11.26 (+2.94%)</td><td>11.04 (+4.73%)</td><td>9.21 (+5.53%)</td><td>1.69 (-18.35%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>7691.60 (n/a)</td><td>6309.16 (n/a)</td><td>6366.80 (n/a)</td><td>4981.50 (n/a)</td><td>1174.16 (n/a)</td><td>13.47 (n/a)</td><td>10.94 (n/a)</td><td>10.54 (n/a)</td><td>8.72 (n/a)</td><td>2.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.78 (n/a)</td><td>3.56 (n/a)</td><td>3.48 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td><td>3.78 (n/a)</td><td>3.55 (n/a)</td><td>3.48 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.53 (+1.56%)</td><td>6.90 (+2.55%)</td><td>6.75 (-5.82%)</td><td>6.63 (+18.00%)</td><td>0.36 <b>(-54.10%)</b></td><td>7.53 (+1.56%)</td><td>6.90 (+2.55%)</td><td>6.74 (-5.82%)</td><td>6.63 (+18.00%)</td><td>0.36 <b>(-54.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.42 (n/a)</td><td>6.73 (n/a)</td><td>7.17 (n/a)</td><td>5.62 (n/a)</td><td>0.79 (n/a)</td><td>7.41 (n/a)</td><td>6.73 (n/a)</td><td>7.16 (n/a)</td><td>5.62 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>13.53 (-2.36%)</td><td>10.12 (-6.95%)</td><td>9.36 (-4.95%)</td><td>7.15 (-16.83%)</td><td>2.68 (+10.54%)</td><td>13.52 (-2.36%)</td><td>10.11 (-6.95%)</td><td>9.36 (-4.95%)</td><td>7.15 (-16.83%)</td><td>2.68 (+10.54%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>13.86 (n/a)</td><td>10.87 (n/a)</td><td>9.85 (n/a)</td><td>8.60 (n/a)</td><td>2.43 (n/a)</td><td>13.85 (n/a)</td><td>10.87 (n/a)</td><td>9.85 (n/a)</td><td>8.59 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.71 (n/a)</td><td>3.64 (n/a)</td><td>3.64 (n/a)</td><td>3.55 (n/a)</td><td>0.06 (n/a)</td><td>3.70 (n/a)</td><td>3.63 (n/a)</td><td>3.64 (n/a)</td><td>3.55 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.40 (-1.71%)</td><td>6.58 (-2.13%)</td><td>6.56 (-2.19%)</td><td>6.04 (+6.25%)</td><td>0.56 (-17.97%)</td><td>7.39 (-1.71%)</td><td>6.57 (-2.13%)</td><td>6.56 (-2.19%)</td><td>6.03 (+6.25%)</td><td>0.56 (-17.97%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.52 (n/a)</td><td>6.72 (n/a)</td><td>6.71 (n/a)</td><td>5.68 (n/a)</td><td>0.68 (n/a)</td><td>7.52 (n/a)</td><td>6.72 (n/a)</td><td>6.70 (n/a)</td><td>5.68 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>14.29 (+3.48%)</td><td>10.36 <b>(-20.82%)</b></td><td>9.53 <b>(-30.32%)</b></td><td>7.13 <b>(-34.98%)</b></td><td>3.32 <b>(+175.46%)</b></td><td>14.28 (+3.48%)</td><td>10.35 <b>(-20.82%)</b></td><td>9.52 <b>(-30.32%)</b></td><td>7.13 <b>(-34.98%)</b></td><td>3.32 <b>(+175.46%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>13.81 (n/a)</td><td>13.08 (n/a)</td><td>13.68 (n/a)</td><td>10.97 (n/a)</td><td>1.20 (n/a)</td><td>13.80 (n/a)</td><td>13.07 (n/a)</td><td>13.67 (n/a)</td><td>10.96 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.82 (-3.02%)</td><td>1.99 <b>(+24.43%)</b></td><td>1.74 <b>(+45.86%)</b></td><td>0.94 (-6.10%)</td><td>0.81 (+3.75%)</td><td>2.82 (-3.02%)</td><td>1.99 <b>(+24.43%)</b></td><td>1.74 <b>(+45.86%)</b></td><td>0.94 (-6.10%)</td><td>0.81 (+3.75%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.91 (n/a)</td><td>1.60 (n/a)</td><td>1.19 (n/a)</td><td>1.00 (n/a)</td><td>0.78 (n/a)</td><td>2.91 (n/a)</td><td>1.60 (n/a)</td><td>1.19 (n/a)</td><td>1.00 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.53 (-4.78%)</td><td>0.17 <b>(-44.01%)</b></td><td>0.08 <b>(-75.59%)</b></td><td>0.08 (-2.27%)</td><td>0.20 (+15.47%)</td><td>0.52 (-4.78%)</td><td>0.17 <b>(-44.01%)</b></td><td>0.08 <b>(-75.59%)</b></td><td>0.07 (-2.27%)</td><td>0.20 (+15.47%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.56 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td><td>0.55 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.75 (+8.67%)</td><td>0.57 <b>(+35.68%)</b></td><td>0.65 <b>(+60.65%)</b></td><td>0.28 <b>(+265.80%)</b></td><td>0.19 <b>(-25.05%)</b></td><td>0.74 (+8.67%)</td><td>0.56 <b>(+35.68%)</b></td><td>0.65 <b>(+60.65%)</b></td><td>0.28 <b>(+265.80%)</b></td><td>0.18 <b>(-25.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.69 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.68 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.48 <b>(+56.14%)</b></td><td>1.65 <b>(+70.50%)</b></td><td>1.83 <b>(+108.65%)</b></td><td>0.72 <b>(+71.93%)</b></td><td>0.86 <b>(+53.90%)</b></td><td>2.44 <b>(+56.14%)</b></td><td>1.63 <b>(+70.50%)</b></td><td>1.80 <b>(+108.65%)</b></td><td>0.71 <b>(+71.93%)</b></td><td>0.85 <b>(+53.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.59 (n/a)</td><td>0.97 (n/a)</td><td>0.88 (n/a)</td><td>0.42 (n/a)</td><td>0.56 (n/a)</td><td>1.56 (n/a)</td><td>0.95 (n/a)</td><td>0.86 (n/a)</td><td>0.41 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.80 (n/a)</td><td>354.88 (n/a)</td><td>316.20 (n/a)</td><td>289.80 (n/a)</td><td>106.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1042.90 (n/a)</td><td>466.92 (n/a)</td><td>277.40 (n/a)</td><td>215.60 (n/a)</td><td>351.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.50 (n/a)</td><td>346.38 (n/a)</td><td>312.60 (n/a)</td><td>229.70 (n/a)</td><td>100.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.40 (n/a)</td><td>437.60 (n/a)</td><td>467.10 (n/a)</td><td>247.60 (n/a)</td><td>112.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.60 (n/a)</td><td>438.22 (n/a)</td><td>411.30 (n/a)</td><td>300.60 (n/a)</td><td>108.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>694.40 (n/a)</td><td>511.10 (n/a)</td><td>624.20 (n/a)</td><td>254.30 (n/a)</td><td>193.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.30 (n/a)</td><td>355.86 (n/a)</td><td>306.30 (n/a)</td><td>276.20 (n/a)</td><td>101.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>397.60 (n/a)</td><td>381.50 (n/a)</td><td>233.10 (n/a)</td><td>131.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>408.52 (n/a)</td><td>433.00 (n/a)</td><td>238.30 (n/a)</td><td>141.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.50 (n/a)</td><td>496.92 (n/a)</td><td>516.50 (n/a)</td><td>400.50 (n/a)</td><td>87.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>444.58 (n/a)</td><td>438.50 (n/a)</td><td>238.00 (n/a)</td><td>132.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>509.30 (n/a)</td><td>422.04 (n/a)</td><td>382.50 (n/a)</td><td>359.50 (n/a)</td><td>73.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.90 (n/a)</td><td>388.48 (n/a)</td><td>310.50 (n/a)</td><td>230.50 (n/a)</td><td>156.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.60 (n/a)</td><td>422.48 (n/a)</td><td>462.00 (n/a)</td><td>278.30 (n/a)</td><td>137.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>669.00 (n/a)</td><td>429.92 (n/a)</td><td>407.00 (n/a)</td><td>249.80 (n/a)</td><td>173.35 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.00 (n/a)</td><td>351.56 (n/a)</td><td>314.40 (n/a)</td><td>234.40 (n/a)</td><td>119.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>493.90 (n/a)</td><td>437.26 (n/a)</td><td>479.20 (n/a)</td><td>301.60 (n/a)</td><td>79.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2041.90 (n/a)</td><td>791.24 (n/a)</td><td>523.40 (n/a)</td><td>364.70 (n/a)</td><td>702.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>562.00 (n/a)</td><td>356.38 (n/a)</td><td>306.70 (n/a)</td><td>269.90 (n/a)</td><td>117.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>672.60 (n/a)</td><td>477.24 (n/a)</td><td>517.80 (n/a)</td><td>256.20 (n/a)</td><td>182.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>784.10 (n/a)</td><td>454.02 (n/a)</td><td>345.10 (n/a)</td><td>256.00 (n/a)</td><td>238.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>645.90 (n/a)</td><td>473.02 (n/a)</td><td>535.40 (n/a)</td><td>243.20 (n/a)</td><td>190.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>489.70 (n/a)</td><td>365.08 (n/a)</td><td>331.00 (n/a)</td><td>273.00 (n/a)</td><td>94.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>801.10 (n/a)</td><td>479.68 (n/a)</td><td>444.40 (n/a)</td><td>250.90 (n/a)</td><td>209.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-13.12%)</td><td>0.01 <b>(-41.75%)</b></td><td>0.01 <b>(-48.43%)</b></td><td>0.01 <b>(-52.98%)</b></td><td>0.00 <b>(+294.95%)</b></td><td>601.30 <b>(+112.70%)</b></td><td>486.12 <b>(+83.36%)</b></td><td>519.50 <b>(+93.92%)</b></td><td>285.10 (+15.10%)</td><td>119.69 <b>(+810.85%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>282.70 (n/a)</td><td>265.12 (n/a)</td><td>267.90 (n/a)</td><td>247.70 (n/a)</td><td>13.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(-23.88%)</b></td><td>0.01 <b>(+23.34%)</b></td><td>0.01 <b>(+38.18%)</b></td><td>0.01 <b>(+401.25%)</b></td><td>0.00 <b>(-52.10%)</b></td><td>503.50 <b>(-80.05%)</b></td><td>393.98 <b>(-54.24%)</b></td><td>403.20 <b>(-27.63%)</b></td><td>283.80 <b>(+31.39%)</b></td><td>104.71 <b>(-88.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2524.00 (n/a)</td><td>860.88 (n/a)</td><td>557.10 (n/a)</td><td>216.00 (n/a)</td><td>941.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-35.53%)</b></td><td>0.01 <b>(-24.36%)</b></td><td>0.02 (+1.59%)</td><td>0.01 <b>(-24.50%)</b></td><td>0.00 <b>(-22.03%)</b></td><td>575.90 <b>(+32.45%)</b></td><td>377.98 <b>(+35.66%)</b></td><td>271.40 (-1.56%)</td><td>259.00 <b>(+55.09%)</b></td><td>153.74 <b>(+56.09%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>434.80 (n/a)</td><td>278.62 (n/a)</td><td>275.70 (n/a)</td><td>167.00 (n/a)</td><td>98.49 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+22.14%)</b></td><td>0.01 (-15.42%)</td><td>0.01 <b>(-26.22%)</b></td><td>0.01 <b>(-31.62%)</b></td><td>0.00 <b>(+138.77%)</b></td><td>635.70 <b>(+46.24%)</b></td><td>486.88 <b>(+31.66%)</b></td><td>490.50 <b>(+35.53%)</b></td><td>233.30 (-18.11%)</td><td>158.78 <b>(+176.53%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>434.70 (n/a)</td><td>369.80 (n/a)</td><td>361.90 (n/a)</td><td>284.90 (n/a)</td><td>57.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(-21.74%)</b></td><td>0.01 (-10.97%)</td><td>0.01 <b>(-37.43%)</b></td><td>0.01 <b>(+311.83%)</b></td><td>0.00 <b>(-65.84%)</b></td><td>467.90 <b>(-75.72%)</b></td><td>389.56 <b>(-38.69%)</b></td><td>416.20 <b>(+59.83%)</b></td><td>291.00 <b>(+27.80%)</b></td><td>80.08 <b>(-89.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1926.90 (n/a)</td><td>635.40 (n/a)</td><td>260.40 (n/a)</td><td>227.70 (n/a)</td><td>732.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(-20.20%)</b></td><td>0.01 (-10.29%)</td><td>0.01 <b>(-23.40%)</b></td><td>0.01 <b>(+206.78%)</b></td><td>0.00 <b>(-60.29%)</b></td><td>613.30 <b>(-67.40%)</b></td><td>528.44 <b>(-23.85%)</b></td><td>553.70 <b>(+30.56%)</b></td><td>377.90 <b>(+25.34%)</b></td><td>89.24 <b>(-86.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1881.50 (n/a)</td><td>693.94 (n/a)</td><td>424.10 (n/a)</td><td>301.50 (n/a)</td><td>666.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-28.43%)</b></td><td>0.02 <b>(-27.02%)</b></td><td>0.02 <b>(-28.02%)</b></td><td>0.02 (-7.11%)</td><td>0.01 <b>(-37.05%)</b></td><td>491.60 (+7.67%)</td><td>388.10 <b>(+33.24%)</b></td><td>355.10 <b>(+38.93%)</b></td><td>287.60 <b>(+39.68%)</b></td><td>90.44 (-6.84%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.60 (n/a)</td><td>291.28 (n/a)</td><td>255.60 (n/a)</td><td>205.90 (n/a)</td><td>97.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(+46.40%)</b></td><td>0.03 (+9.93%)</td><td>0.03 (+6.98%)</td><td>0.02 (-13.60%)</td><td>0.01 <b>(+96.28%)</b></td><td>515.40 (+15.74%)</td><td>346.14 (-1.07%)</td><td>303.50 (-6.53%)</td><td>179.30 <b>(-31.70%)</b></td><td>132.08 <b>(+51.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.30 (n/a)</td><td>349.88 (n/a)</td><td>324.70 (n/a)</td><td>262.50 (n/a)</td><td>87.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(+35.52%)</b></td><td>0.04 <b>(+22.93%)</b></td><td>0.03 (+1.06%)</td><td>0.03 <b>(+82.75%)</b></td><td>0.01 (+8.54%)</td><td>295.30 <b>(-45.29%)</b></td><td>242.78 <b>(-22.89%)</b></td><td>265.30 (-1.08%)</td><td>162.60 <b>(-26.23%)</b></td><td>51.50 <b>(-60.02%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>314.86 (n/a)</td><td>268.20 (n/a)</td><td>220.40 (n/a)</td><td>128.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(+42.32%)</b></td><td>0.03 (+14.12%)</td><td>0.03 (+10.16%)</td><td>0.02 (+11.32%)</td><td>0.01 <b>(+50.17%)</b></td><td>511.40 (-10.17%)</td><td>345.42 (-8.96%)</td><td>290.90 (-9.24%)</td><td>188.00 <b>(-29.75%)</b></td><td>132.83 (+0.16%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.30 (n/a)</td><td>379.40 (n/a)</td><td>320.50 (n/a)</td><td>267.60 (n/a)</td><td>132.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(+24.11%)</b></td><td>0.03 <b>(+49.01%)</b></td><td>0.03 <b>(+66.51%)</b></td><td>0.02 <b>(+51.39%)</b></td><td>0.01 (+4.33%)</td><td>437.20 <b>(-33.95%)</b></td><td>313.24 <b>(-35.48%)</b></td><td>290.20 <b>(-39.93%)</b></td><td>203.50 (-19.41%)</td><td>90.41 <b>(-40.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.90 (n/a)</td><td>485.52 (n/a)</td><td>483.10 (n/a)</td><td>252.50 (n/a)</td><td>153.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-23.03%)</b></td><td>0.02 (-16.93%)</td><td>0.02 (-10.30%)</td><td>0.01 <b>(-44.80%)</b></td><td>0.01 <b>(-23.15%)</b></td><td>1176.10 <b>(+81.16%)</b></td><td>532.96 <b>(+29.36%)</b></td><td>405.60 (+11.49%)</td><td>281.30 <b>(+29.93%)</b></td><td>363.89 <b>(+98.73%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.20 (n/a)</td><td>412.00 (n/a)</td><td>363.80 (n/a)</td><td>216.50 (n/a)</td><td>183.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-19.61%)</td><td>0.02 (+1.71%)</td><td>0.02 (+0.62%)</td><td>0.01 (-6.06%)</td><td>0.01 <b>(-22.79%)</b></td><td>798.50 (+6.44%)</td><td>474.68 (-3.99%)</td><td>496.00 (-0.62%)</td><td>259.70 <b>(+24.38%)</b></td><td>211.90 (+9.12%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>750.20 (n/a)</td><td>494.40 (n/a)</td><td>499.10 (n/a)</td><td>208.80 (n/a)</td><td>194.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-23.49%)</b></td><td>0.02 (-7.58%)</td><td>0.02 (+18.46%)</td><td>0.01 <b>(+51.63%)</b></td><td>0.00 <b>(-60.49%)</b></td><td>653.60 <b>(-34.05%)</b></td><td>501.98 (-9.07%)</td><td>490.00 (-15.58%)</td><td>372.60 <b>(+30.69%)</b></td><td>104.30 <b>(-63.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>991.00 (n/a)</td><td>552.08 (n/a)</td><td>580.40 (n/a)</td><td>285.10 (n/a)</td><td>285.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 <b>(-20.39%)</b></td><td>0.04 <b>(-36.53%)</b></td><td>0.03 <b>(-43.04%)</b></td><td>0.03 <b>(-29.08%)</b></td><td>0.01 (+2.87%)</td><td>517.30 <b>(+40.99%)</b></td><td>459.86 <b>(+60.78%)</b></td><td>499.20 <b>(+75.59%)</b></td><td>296.00 <b>(+25.58%)</b></td><td>92.31 <b>(+77.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>366.90 (n/a)</td><td>286.02 (n/a)</td><td>284.30 (n/a)</td><td>235.70 (n/a)</td><td>51.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-18.84%)</td><td>0.04 <b>(-21.68%)</b></td><td>0.04 (-19.66%)</td><td>0.01 <b>(-68.91%)</b></td><td>0.02 (-0.91%)</td><td>1855.20 <b>(+221.69%)</b></td><td>687.68 <b>(+72.80%)</b></td><td>446.60 <b>(+24.47%)</b></td><td>278.80 <b>(+23.25%)</b></td><td>661.27 <b>(+296.92%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.70 (n/a)</td><td>397.96 (n/a)</td><td>358.80 (n/a)</td><td>226.20 (n/a)</td><td>166.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(+24.33%)</b></td><td>0.04 (-5.15%)</td><td>0.04 (-1.35%)</td><td>0.01 <b>(-53.08%)</b></td><td>0.01 <b>(+176.74%)</b></td><td>1106.00 <b>(+113.14%)</b></td><td>536.92 <b>(+26.02%)</b></td><td>415.50 (+1.37%)</td><td>299.00 (-19.56%)</td><td>323.47 <b>(+431.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>518.90 (n/a)</td><td>426.06 (n/a)</td><td>409.90 (n/a)</td><td>371.70 (n/a)</td><td>60.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-0.75%)</td><td>0.05 (+15.94%)</td><td>0.05 <b>(+69.07%)</b></td><td>0.03 (-4.60%)</td><td>0.01 (-5.82%)</td><td>591.70 (+4.82%)</td><td>391.68 (-14.46%)</td><td>319.50 <b>(-40.84%)</b></td><td>272.10 (+0.78%)</td><td>132.23 (-3.54%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>457.90 (n/a)</td><td>540.10 (n/a)</td><td>270.00 (n/a)</td><td>137.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(-36.50%)</b></td><td>0.03 <b>(-36.56%)</b></td><td>0.03 <b>(-35.89%)</b></td><td>0.02 <b>(-29.86%)</b></td><td>0.01 <b>(-44.01%)</b></td><td>769.10 <b>(+42.56%)</b></td><td>577.24 <b>(+54.96%)</b></td><td>588.60 <b>(+55.96%)</b></td><td>435.50 <b>(+57.50%)</b></td><td>137.67 <b>(+27.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.50 (n/a)</td><td>372.50 (n/a)</td><td>377.40 (n/a)</td><td>276.50 (n/a)</td><td>108.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 <b>(+64.41%)</b></td><td>0.04 <b>(+20.36%)</b></td><td>0.03 (-9.25%)</td><td>0.02 <b>(+212.74%)</b></td><td>0.02 <b>(+40.88%)</b></td><td>716.80 <b>(-68.03%)</b></td><td>540.62 <b>(-34.95%)</b></td><td>539.70 (+10.19%)</td><td>242.70 <b>(-39.17%)</b></td><td>190.25 <b>(-75.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2241.80 (n/a)</td><td>831.10 (n/a)</td><td>489.80 (n/a)</td><td>399.00 (n/a)</td><td>791.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 <b>(-35.28%)</b></td><td>0.09 (-9.41%)</td><td>0.10 (+11.82%)</td><td>0.05 (-5.18%)</td><td>0.02 <b>(-49.59%)</b></td><td>662.10 (+5.46%)</td><td>398.86 (+0.74%)</td><td>339.80 (-10.58%)</td><td>298.10 <b>(+54.54%)</b></td><td>150.13 (-13.85%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>627.80 (n/a)</td><td>395.92 (n/a)</td><td>380.00 (n/a)</td><td>192.90 (n/a)</td><td>174.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (-7.42%)</td><td>0.09 (-10.80%)</td><td>0.10 (-14.00%)</td><td>0.05 (-19.77%)</td><td>0.03 (+2.26%)</td><td>653.20 <b>(+24.63%)</b></td><td>396.50 (+15.23%)</td><td>319.00 (+16.25%)</td><td>286.20 (+8.04%)</td><td>155.74 <b>(+38.68%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.10 (n/a)</td><td>344.08 (n/a)</td><td>274.40 (n/a)</td><td>264.90 (n/a)</td><td>112.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (+4.52%)</td><td>0.10 (-0.85%)</td><td>0.11 (+18.94%)</td><td>0.05 <b>(-24.63%)</b></td><td>0.03 <b>(+47.35%)</b></td><td>608.50 <b>(+32.69%)</b></td><td>373.46 (+7.87%)</td><td>295.70 (-15.92%)</td><td>260.30 (-4.34%)</td><td>149.06 <b>(+90.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>458.60 (n/a)</td><td>346.22 (n/a)</td><td>351.70 (n/a)</td><td>272.10 (n/a)</td><td>78.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 <b>(+28.28%)</b></td><td>0.09 (-6.27%)</td><td>0.08 <b>(-29.30%)</b></td><td>0.06 (-1.98%)</td><td>0.04 <b>(+54.38%)</b></td><td>506.80 (+2.01%)</td><td>388.68 (+11.12%)</td><td>424.30 <b>(+41.43%)</b></td><td>213.60 <b>(-22.07%)</b></td><td>114.22 (+19.90%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>496.80 (n/a)</td><td>349.78 (n/a)</td><td>300.00 (n/a)</td><td>274.10 (n/a)</td><td>95.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(-25.22%)</b></td><td>0.07 <b>(-23.21%)</b></td><td>0.07 <b>(-21.17%)</b></td><td>0.05 <b>(-25.26%)</b></td><td>0.02 <b>(-31.10%)</b></td><td>624.90 <b>(+33.81%)</b></td><td>477.52 <b>(+29.33%)</b></td><td>473.90 <b>(+26.85%)</b></td><td>341.30 <b>(+33.74%)</b></td><td>100.81 <b>(+22.87%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>467.00 (n/a)</td><td>369.22 (n/a)</td><td>373.60 (n/a)</td><td>255.20 (n/a)</td><td>82.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+9.46%)</td><td>0.01 <b>(+21.80%)</b></td><td>0.01 <b>(+20.14%)</b></td><td>0.01 <b>(+168.42%)</b></td><td>0.00 <b>(-36.07%)</b></td><td>423.60 <b>(-62.74%)</b></td><td>324.56 <b>(-35.86%)</b></td><td>295.60 (-16.76%)</td><td>227.10 (-8.65%)</td><td>80.53 <b>(-78.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1136.90 (n/a)</td><td>506.02 (n/a)</td><td>355.10 (n/a)</td><td>248.60 (n/a)</td><td>367.67 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-4.00%)</td><td>0.01 (-8.45%)</td><td>0.01 (-8.06%)</td><td>0.01 (+7.04%)</td><td>0.00 (-5.89%)</td><td>478.30 (-6.56%)</td><td>353.16 (+8.46%)</td><td>285.70 (+8.76%)</td><td>266.80 (+4.14%)</td><td>103.90 (-5.61%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.90 (n/a)</td><td>325.62 (n/a)</td><td>262.70 (n/a)</td><td>256.20 (n/a)</td><td>110.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(-23.67%)</b></td><td>0.01 <b>(-28.50%)</b></td><td>0.01 <b>(-41.93%)</b></td><td>0.01 (-5.98%)</td><td>0.00 <b>(-38.03%)</b></td><td>528.60 (+6.36%)</td><td>459.38 <b>(+33.88%)</b></td><td>507.00 <b>(+72.21%)</b></td><td>292.90 <b>(+30.99%)</b></td><td>98.88 (-16.94%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.00 (n/a)</td><td>343.14 (n/a)</td><td>294.40 (n/a)</td><td>223.60 (n/a)</td><td>119.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+35.61%)</b></td><td>0.01 (+13.88%)</td><td>0.01 <b>(+29.09%)</b></td><td>0.01 <b>(-28.28%)</b></td><td>0.00 <b>(+150.17%)</b></td><td>634.40 <b>(+39.43%)</b></td><td>398.44 (-1.08%)</td><td>325.70 <b>(-22.54%)</b></td><td>219.50 <b>(-26.27%)</b></td><td>169.31 <b>(+171.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.00 (n/a)</td><td>402.78 (n/a)</td><td>420.50 (n/a)</td><td>297.70 (n/a)</td><td>62.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+19.91%)</td><td>0.01 (-5.86%)</td><td>0.01 (+6.99%)</td><td>0.00 <b>(-71.94%)</b></td><td>0.01 <b>(+60.19%)</b></td><td>1850.60 <b>(+256.36%)</b></td><td>645.14 <b>(+71.24%)</b></td><td>401.60 (-6.54%)</td><td>182.30 (-16.61%)</td><td>684.09 <b>(+435.39%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.30 (n/a)</td><td>376.74 (n/a)</td><td>429.70 (n/a)</td><td>218.60 (n/a)</td><td>127.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+29.69%)</b></td><td>0.01 (+14.82%)</td><td>0.01 <b>(+29.30%)</b></td><td>0.01 <b>(-22.77%)</b></td><td>0.00 <b>(+165.51%)</b></td><td>547.80 <b>(+29.50%)</b></td><td>372.02 (-3.47%)</td><td>314.40 <b>(-22.66%)</b></td><td>227.90 <b>(-22.88%)</b></td><td>145.19 <b>(+183.25%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>423.00 (n/a)</td><td>385.40 (n/a)</td><td>406.50 (n/a)</td><td>295.50 (n/a)</td><td>51.26 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(+38.90%)</b></td><td>0.01 (-12.47%)</td><td>0.01 <b>(-35.31%)</b></td><td>0.00 <b>(-55.63%)</b></td><td>0.01 <b>(+107.57%)</b></td><td>1285.30 <b>(+125.41%)</b></td><td>543.36 <b>(+62.61%)</b></td><td>467.70 <b>(+54.56%)</b></td><td>160.20 <b>(-28.00%)</b></td><td>436.96 <b>(+220.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.20 (n/a)</td><td>334.14 (n/a)</td><td>302.60 (n/a)</td><td>222.50 (n/a)</td><td>136.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+0.37%)</td><td>0.01 (-9.97%)</td><td>0.01 <b>(-35.60%)</b></td><td>0.01 <b>(+63.45%)</b></td><td>0.00 (-15.09%)</td><td>600.40 <b>(-38.82%)</b></td><td>418.66 (-3.63%)</td><td>465.20 <b>(+55.27%)</b></td><td>241.00 (-0.37%)</td><td>150.62 <b>(-51.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>981.40 (n/a)</td><td>434.42 (n/a)</td><td>299.60 (n/a)</td><td>241.90 (n/a)</td><td>311.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+57.25%)</b></td><td>0.01 <b>(+26.92%)</b></td><td>0.01 (+14.96%)</td><td>0.01 (+3.80%)</td><td>0.00 <b>(+171.56%)</b></td><td>530.40 (-3.65%)</td><td>403.34 (-15.00%)</td><td>426.10 (-13.01%)</td><td>234.50 <b>(-36.40%)</b></td><td>129.91 <b>(+69.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.50 (n/a)</td><td>474.50 (n/a)</td><td>489.80 (n/a)</td><td>368.70 (n/a)</td><td>76.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+43.43%)</b></td><td>0.01 (+16.06%)</td><td>0.01 (-6.92%)</td><td>0.01 (+18.59%)</td><td>0.01 <b>(+77.23%)</b></td><td>504.60 (-15.68%)</td><td>408.14 (-8.73%)</td><td>449.00 (+7.44%)</td><td>187.20 <b>(-30.28%)</b></td><td>127.73 (-0.64%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.40 (n/a)</td><td>447.20 (n/a)</td><td>417.90 (n/a)</td><td>268.50 (n/a)</td><td>128.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-3.89%)</td><td>0.01 (+6.27%)</td><td>0.01 (+10.18%)</td><td>0.01 <b>(-22.64%)</b></td><td>0.00 <b>(+27.79%)</b></td><td>809.50 <b>(+29.27%)</b></td><td>486.06 (-0.83%)</td><td>426.90 (-9.25%)</td><td>344.90 (+4.04%)</td><td>192.40 <b>(+72.72%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.20 (n/a)</td><td>490.12 (n/a)</td><td>470.40 (n/a)</td><td>331.50 (n/a)</td><td>111.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+13.34%)</td><td>0.03 <b>(+27.91%)</b></td><td>0.02 (+14.48%)</td><td>0.02 <b>(+113.27%)</b></td><td>0.01 <b>(-23.06%)</b></td><td>458.70 <b>(-53.11%)</b></td><td>341.06 <b>(-33.25%)</b></td><td>329.40 (-12.63%)</td><td>245.20 (-11.77%)</td><td>93.31 <b>(-68.19%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>978.20 (n/a)</td><td>510.94 (n/a)</td><td>377.00 (n/a)</td><td>277.90 (n/a)</td><td>293.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (+5.28%)</td><td>0.03 <b>(+35.54%)</b></td><td>0.03 <b>(+36.53%)</b></td><td>0.03 <b>(+142.90%)</b></td><td>0.00 <b>(-43.28%)</b></td><td>320.20 <b>(-58.84%)</b></td><td>272.18 <b>(-35.30%)</b></td><td>266.00 <b>(-26.76%)</b></td><td>229.00 (-5.02%)</td><td>43.53 <b>(-79.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>777.90 (n/a)</td><td>420.66 (n/a)</td><td>363.20 (n/a)</td><td>241.10 (n/a)</td><td>209.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+6.33%)</td><td>0.02 <b>(+26.91%)</b></td><td>0.03 <b>(+88.76%)</b></td><td>0.01 <b>(-41.44%)</b></td><td>0.01 <b>(+56.08%)</b></td><td>1076.50 <b>(+70.79%)</b></td><td>499.18 (-4.10%)</td><td>305.00 <b>(-47.01%)</b></td><td>271.50 (-5.93%)</td><td>343.97 <b>(+154.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.30 (n/a)</td><td>520.52 (n/a)</td><td>575.60 (n/a)</td><td>288.60 (n/a)</td><td>135.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-21.62%)</b></td><td>0.02 (-3.01%)</td><td>0.02 (+2.34%)</td><td>0.02 <b>(+93.72%)</b></td><td>0.01 <b>(-47.81%)</b></td><td>482.40 <b>(-48.38%)</b></td><td>365.28 (-15.58%)</td><td>355.70 (-2.31%)</td><td>276.00 <b>(+27.54%)</b></td><td>90.59 <b>(-68.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>934.50 (n/a)</td><td>432.70 (n/a)</td><td>364.10 (n/a)</td><td>216.40 (n/a)</td><td>288.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-35.10%)</b></td><td>0.02 <b>(-25.08%)</b></td><td>0.02 (-11.50%)</td><td>0.01 (-2.78%)</td><td>0.00 <b>(-63.97%)</b></td><td>592.10 (+2.85%)</td><td>476.88 <b>(+21.42%)</b></td><td>464.20 (+13.00%)</td><td>370.90 <b>(+54.09%)</b></td><td>90.29 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>392.74 (n/a)</td><td>410.80 (n/a)</td><td>240.70 (n/a)</td><td>147.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (-12.91%)</td><td>0.03 <b>(+32.18%)</b></td><td>0.03 <b>(+75.72%)</b></td><td>0.02 (+18.74%)</td><td>0.01 <b>(-36.15%)</b></td><td>476.90 (-15.79%)</td><td>301.98 <b>(-29.92%)</b></td><td>268.30 <b>(-43.10%)</b></td><td>234.00 (+14.82%)</td><td>98.91 <b>(-33.45%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.30 (n/a)</td><td>430.92 (n/a)</td><td>471.50 (n/a)</td><td>203.80 (n/a)</td><td>148.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-7.47%)</td><td>0.02 (-12.60%)</td><td>0.02 <b>(-30.20%)</b></td><td>0.02 <b>(+20.04%)</b></td><td>0.01 <b>(-21.03%)</b></td><td>445.50 (-16.68%)</td><td>355.80 (+9.58%)</td><td>402.40 <b>(+43.25%)</b></td><td>236.30 (+8.05%)</td><td>93.55 <b>(-27.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>324.70 (n/a)</td><td>280.90 (n/a)</td><td>218.70 (n/a)</td><td>129.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(-32.54%)</b></td><td>0.02 <b>(-28.63%)</b></td><td>0.02 (-2.50%)</td><td>0.00 <b>(-72.14%)</b></td><td>0.01 (-14.02%)</td><td>2056.60 <b>(+258.92%)</b></td><td>761.94 <b>(+88.25%)</b></td><td>462.80 (+2.57%)</td><td>349.10 <b>(+48.24%)</b></td><td>725.61 <b>(+438.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.00 (n/a)</td><td>404.74 (n/a)</td><td>451.20 (n/a)</td><td>235.50 (n/a)</td><td>134.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+0.55%)</td><td>0.02 (+10.67%)</td><td>0.02 (+4.52%)</td><td>0.01 <b>(+236.15%)</b></td><td>0.01 <b>(-33.40%)</b></td><td>566.90 <b>(-70.25%)</b></td><td>387.70 <b>(-41.77%)</b></td><td>371.60 (-4.33%)</td><td>241.90 (-0.53%)</td><td>129.00 <b>(-81.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1905.80 (n/a)</td><td>665.84 (n/a)</td><td>388.40 (n/a)</td><td>243.20 (n/a)</td><td>701.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-37.54%)</b></td><td>0.03 (-14.26%)</td><td>0.03 (+2.26%)</td><td>0.02 <b>(+27.75%)</b></td><td>0.01 <b>(-55.25%)</b></td><td>425.70 <b>(-21.73%)</b></td><td>326.06 (+4.16%)</td><td>279.00 (-2.21%)</td><td>242.20 <b>(+60.08%)</b></td><td>83.49 <b>(-41.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>313.04 (n/a)</td><td>285.30 (n/a)</td><td>151.30 (n/a)</td><td>142.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+15.25%)</td><td>0.02 (+13.81%)</td><td>0.02 (+4.53%)</td><td>0.02 (+5.40%)</td><td>0.01 <b>(+28.71%)</b></td><td>478.90 (-5.11%)</td><td>399.16 (-10.31%)</td><td>457.10 (-4.33%)</td><td>242.00 (-13.23%)</td><td>104.97 (+12.14%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.70 (n/a)</td><td>445.02 (n/a)</td><td>477.80 (n/a)</td><td>278.90 (n/a)</td><td>93.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-16.97%)</td><td>0.03 (+18.53%)</td><td>0.03 (+11.86%)</td><td>0.02 <b>(+421.01%)</b></td><td>0.00 <b>(-69.63%)</b></td><td>376.90 <b>(-80.81%)</b></td><td>303.44 <b>(-52.74%)</b></td><td>297.50 (-10.61%)</td><td>259.70 <b>(+20.40%)</b></td><td>46.11 <b>(-93.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1963.70 (n/a)</td><td>642.04 (n/a)</td><td>332.80 (n/a)</td><td>215.70 (n/a)</td><td>742.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (+1.41%)</td><td>0.06 (+2.71%)</td><td>0.06 (-0.06%)</td><td>0.04 <b>(+20.56%)</b></td><td>0.01 <b>(-24.34%)</b></td><td>392.20 (-17.06%)</td><td>291.54 (-5.53%)</td><td>271.40 (+0.07%)</td><td>239.40 (-1.36%)</td><td>59.03 <b>(-37.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.90 (n/a)</td><td>308.60 (n/a)</td><td>271.20 (n/a)</td><td>242.70 (n/a)</td><td>94.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (+6.38%)</td><td>0.07 <b>(+21.57%)</b></td><td>0.07 <b>(+20.05%)</b></td><td>0.06 <b>(+67.93%)</b></td><td>0.00 <b>(-65.18%)</b></td><td>269.20 <b>(-40.46%)</b></td><td>246.30 <b>(-21.62%)</b></td><td>238.20 (-16.71%)</td><td>230.30 (-6.00%)</td><td>16.95 <b>(-80.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>452.10 (n/a)</td><td>314.22 (n/a)</td><td>286.00 (n/a)</td><td>245.00 (n/a)</td><td>85.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-14.66%)</td><td>0.04 (+1.69%)</td><td>0.04 <b>(+30.43%)</b></td><td>0.01 (-14.06%)</td><td>0.02 (-19.30%)</td><td>2427.40 (+16.36%)</td><td>780.56 (+2.10%)</td><td>367.20 <b>(-23.32%)</b></td><td>285.40 (+17.16%)</td><td>923.24 <b>(+21.21%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2086.20 (n/a)</td><td>764.52 (n/a)</td><td>478.90 (n/a)</td><td>243.60 (n/a)</td><td>761.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (+12.63%)</td><td>0.05 (+13.19%)</td><td>0.06 <b>(+71.32%)</b></td><td>0.01 <b>(-72.53%)</b></td><td>0.02 <b>(+72.23%)</b></td><td>1890.00 <b>(+264.02%)</b></td><td>599.60 <b>(+49.62%)</b></td><td>269.80 <b>(-41.64%)</b></td><td>237.50 (-11.21%)</td><td>722.56 <b>(+517.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.20 (n/a)</td><td>400.74 (n/a)</td><td>462.30 (n/a)</td><td>267.50 (n/a)</td><td>116.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-1.83%)</td><td>0.04 (-5.07%)</td><td>0.04 (-4.50%)</td><td>0.02 <b>(-27.10%)</b></td><td>0.01 (+19.81%)</td><td>683.80 <b>(+37.20%)</b></td><td>430.12 (+10.53%)</td><td>406.00 (+4.69%)</td><td>286.10 (+1.85%)</td><td>164.71 <b>(+59.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>498.40 (n/a)</td><td>389.16 (n/a)</td><td>387.80 (n/a)</td><td>280.90 (n/a)</td><td>103.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (+19.40%)</td><td>0.06 (-8.54%)</td><td>0.06 (+0.70%)</td><td>0.04 <b>(-33.60%)</b></td><td>0.02 <b>(+355.46%)</b></td><td>434.10 <b>(+50.57%)</b></td><td>312.82 <b>(+20.32%)</b></td><td>256.20 (-0.66%)</td><td>203.60 (-16.21%)</td><td>112.12 <b>(+518.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>288.30 (n/a)</td><td>259.98 (n/a)</td><td>257.90 (n/a)</td><td>243.00 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-5.95%)</td><td>0.05 <b>(+27.54%)</b></td><td>0.05 <b>(+56.53%)</b></td><td>0.03 (+9.95%)</td><td>0.01 (-13.43%)</td><td>557.40 (-9.06%)</td><td>350.04 <b>(-22.73%)</b></td><td>306.20 <b>(-36.12%)</b></td><td>276.30 (+6.35%)</td><td>117.70 (-8.40%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.90 (n/a)</td><td>453.02 (n/a)</td><td>479.30 (n/a)</td><td>259.80 (n/a)</td><td>128.49 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+41.18%)</b></td><td>0.04 (-11.85%)</td><td>0.04 <b>(-33.94%)</b></td><td>0.03 (-7.39%)</td><td>0.02 <b>(+130.93%)</b></td><td>508.10 (+7.97%)</td><td>427.42 <b>(+23.40%)</b></td><td>465.20 <b>(+51.38%)</b></td><td>208.30 <b>(-29.15%)</b></td><td>125.01 <b>(+69.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>470.60 (n/a)</td><td>346.38 (n/a)</td><td>307.30 (n/a)</td><td>294.00 (n/a)</td><td>73.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-9.27%)</td><td>0.04 (-14.48%)</td><td>0.05 (+1.71%)</td><td>0.01 <b>(-81.12%)</b></td><td>0.02 <b>(+76.85%)</b></td><td>2477.90 <b>(+429.69%)</b></td><td>763.50 <b>(+114.84%)</b></td><td>343.60 (-1.69%)</td><td>279.20 (+10.23%)</td><td>959.66 <b>(+1039.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>467.80 (n/a)</td><td>355.38 (n/a)</td><td>349.50 (n/a)</td><td>253.30 (n/a)</td><td>84.23 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-17.02%)</td><td>0.05 (-1.04%)</td><td>0.05 (+7.20%)</td><td>0.04 <b>(+26.81%)</b></td><td>0.01 <b>(-40.87%)</b></td><td>468.00 <b>(-21.13%)</b></td><td>352.98 (-5.56%)</td><td>348.50 (-6.72%)</td><td>263.10 <b>(+20.52%)</b></td><td>77.76 <b>(-44.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.40 (n/a)</td><td>373.78 (n/a)</td><td>373.60 (n/a)</td><td>218.30 (n/a)</td><td>138.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(-28.05%)</b></td><td>0.03 <b>(-37.91%)</b></td><td>0.03 <b>(-43.70%)</b></td><td>0.01 <b>(-58.91%)</b></td><td>0.01 <b>(-24.19%)</b></td><td>1298.70 <b>(+143.38%)</b></td><td>653.54 <b>(+75.36%)</b></td><td>546.20 <b>(+77.63%)</b></td><td>357.20 <b>(+38.99%)</b></td><td>369.59 <b>(+179.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.60 (n/a)</td><td>372.68 (n/a)</td><td>307.50 (n/a)</td><td>257.00 (n/a)</td><td>132.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (+2.08%)</td><td>0.05 (+18.82%)</td><td>0.05 <b>(+42.61%)</b></td><td>0.03 <b>(+132.34%)</b></td><td>0.01 <b>(-24.22%)</b></td><td>561.80 <b>(-56.96%)</b></td><td>394.80 <b>(-31.75%)</b></td><td>321.70 <b>(-29.90%)</b></td><td>278.40 (-2.04%)</td><td>136.63 <b>(-67.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1305.40 (n/a)</td><td>578.50 (n/a)</td><td>458.90 (n/a)</td><td>284.20 (n/a)</td><td>421.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (+11.47%)</td><td>0.11 (+17.05%)</td><td>0.11 <b>(+44.86%)</b></td><td>0.07 (+3.16%)</td><td>0.03 (+13.16%)</td><td>491.90 (-3.07%)</td><td>331.98 (-13.82%)</td><td>286.90 <b>(-30.98%)</b></td><td>230.80 (-10.26%)</td><td>108.82 (+0.68%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>507.50 (n/a)</td><td>385.20 (n/a)</td><td>415.70 (n/a)</td><td>257.20 (n/a)</td><td>108.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (-13.52%)</td><td>0.12 <b>(+23.39%)</b></td><td>0.14 <b>(+31.08%)</b></td><td>0.08 <b>(+25.01%)</b></td><td>0.03 <b>(-35.35%)</b></td><td>417.70 <b>(-20.01%)</b></td><td>280.82 <b>(-24.41%)</b></td><td>241.70 <b>(-23.73%)</b></td><td>238.60 (+15.66%)</td><td>77.35 <b>(-42.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>522.20 (n/a)</td><td>371.52 (n/a)</td><td>316.90 (n/a)</td><td>206.30 (n/a)</td><td>134.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (-14.34%)</td><td>0.09 (-2.62%)</td><td>0.07 <b>(-32.28%)</b></td><td>0.06 <b>(+92.00%)</b></td><td>0.03 <b>(-29.40%)</b></td><td>524.10 <b>(-47.91%)</b></td><td>396.98 (-15.19%)</td><td>467.30 <b>(+47.65%)</b></td><td>259.90 (+16.76%)</td><td>126.68 <b>(-60.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1006.20 (n/a)</td><td>468.06 (n/a)</td><td>316.50 (n/a)</td><td>222.60 (n/a)</td><td>321.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 <b>(+22.90%)</b></td><td>0.11 (+17.18%)</td><td>0.11 <b>(+24.27%)</b></td><td>0.05 (-18.04%)</td><td>0.03 <b>(+59.63%)</b></td><td>597.60 <b>(+22.01%)</b></td><td>335.22 (-8.38%)</td><td>298.30 (-19.51%)</td><td>222.80 (-18.63%)</td><td>150.03 <b>(+73.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>489.80 (n/a)</td><td>365.88 (n/a)</td><td>370.60 (n/a)</td><td>273.80 (n/a)</td><td>86.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 <b>(+40.26%)</b></td><td>0.11 <b>(+32.25%)</b></td><td>0.11 <b>(+83.23%)</b></td><td>0.04 <b>(-24.24%)</b></td><td>0.04 <b>(+46.59%)</b></td><td>759.70 <b>(+31.98%)</b></td><td>376.22 (-16.83%)</td><td>296.40 <b>(-45.42%)</b></td><td>197.30 <b>(-28.72%)</b></td><td>221.82 <b>(+47.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.60 (n/a)</td><td>452.34 (n/a)</td><td>543.10 (n/a)</td><td>276.80 (n/a)</td><td>150.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (-4.37%)</td><td>0.11 (+9.30%)</td><td>0.12 <b>(+34.37%)</b></td><td>0.06 (+10.39%)</td><td>0.03 (+8.69%)</td><td>523.80 (-9.42%)</td><td>345.56 (-7.47%)</td><td>266.00 <b>(-25.59%)</b></td><td>242.30 (+4.57%)</td><td>130.65 (-0.28%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>578.30 (n/a)</td><td>373.46 (n/a)</td><td>357.50 (n/a)</td><td>231.70 (n/a)</td><td>131.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(-30.07%)</b></td><td>0.07 (-18.40%)</td><td>0.07 (+5.28%)</td><td>0.03 <b>(-38.58%)</b></td><td>0.03 <b>(-36.35%)</b></td><td>1064.30 <b>(+62.84%)</b></td><td>577.28 <b>(+21.83%)</b></td><td>495.20 (-5.02%)</td><td>312.90 <b>(+43.01%)</b></td><td>285.04 <b>(+58.46%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>653.60 (n/a)</td><td>473.84 (n/a)</td><td>521.40 (n/a)</td><td>218.80 (n/a)</td><td>179.88 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (+2.15%)</td><td>0.10 <b>(+37.19%)</b></td><td>0.12 <b>(+87.99%)</b></td><td>0.06 (+6.18%)</td><td>0.04 (+4.62%)</td><td>586.60 (-5.81%)</td><td>358.60 <b>(-26.39%)</b></td><td>280.20 <b>(-46.80%)</b></td><td>226.30 (-2.12%)</td><td>155.64 (+4.31%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>622.80 (n/a)</td><td>487.14 (n/a)</td><td>526.70 (n/a)</td><td>231.20 (n/a)</td><td>149.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 <b>(+22.83%)</b></td><td>0.10 (+12.25%)</td><td>0.10 <b>(+44.97%)</b></td><td>0.05 <b>(-28.12%)</b></td><td>0.05 <b>(+75.99%)</b></td><td>681.00 <b>(+39.12%)</b></td><td>410.38 (+4.74%)</td><td>312.70 <b>(-31.02%)</b></td><td>211.20 (-18.58%)</td><td>223.31 <b>(+102.89%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>489.50 (n/a)</td><td>391.82 (n/a)</td><td>453.30 (n/a)</td><td>259.40 (n/a)</td><td>110.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (-0.36%)</td><td>0.10 (-7.54%)</td><td>0.09 (-15.98%)</td><td>0.06 (-16.70%)</td><td>0.03 <b>(+21.80%)</b></td><td>517.10 <b>(+20.06%)</b></td><td>363.58 (+12.26%)</td><td>346.20 (+19.05%)</td><td>238.70 (+0.38%)</td><td>121.89 <b>(+42.14%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>430.70 (n/a)</td><td>323.88 (n/a)</td><td>290.80 (n/a)</td><td>237.80 (n/a)</td><td>85.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (-2.99%)</td><td>0.09 (+4.78%)</td><td>0.10 <b>(+53.19%)</b></td><td>0.06 (-3.54%)</td><td>0.03 (-8.86%)</td><td>574.00 (+3.67%)</td><td>412.40 (-5.25%)</td><td>341.60 <b>(-34.72%)</b></td><td>285.30 (+3.07%)</td><td>145.23 (+2.06%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.70 (n/a)</td><td>435.26 (n/a)</td><td>523.30 (n/a)</td><td>276.80 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (+9.95%)</td><td>0.08 (-4.46%)</td><td>0.06 (-14.51%)</td><td>0.05 (+1.93%)</td><td>0.03 (+4.12%)</td><td>612.70 (-1.89%)</td><td>463.52 (+3.84%)</td><td>516.10 (+16.95%)</td><td>252.50 (-9.07%)</td><td>139.88 (-10.43%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.50 (n/a)</td><td>446.36 (n/a)</td><td>441.30 (n/a)</td><td>277.70 (n/a)</td><td>156.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(-30.18%)</b></td><td>0.08 (-13.20%)</td><td>0.09 (+0.65%)</td><td>0.05 (+1.34%)</td><td>0.02 <b>(-31.64%)</b></td><td>497.30 (-1.33%)</td><td>337.70 (+11.15%)</td><td>278.20 (-0.64%)</td><td>245.40 <b>(+43.26%)</b></td><td>112.82 (-7.40%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>504.00 (n/a)</td><td>303.82 (n/a)</td><td>280.00 (n/a)</td><td>171.30 (n/a)</td><td>121.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.21 (+13.26%)</td><td>0.16 <b>(+21.13%)</b></td><td>0.17 <b>(+40.05%)</b></td><td>0.10 (+0.09%)</td><td>0.04 (+6.34%)</td><td>490.50 (-0.10%)</td><td>319.14 (-17.28%)</td><td>287.80 <b>(-28.59%)</b></td><td>230.10 (-11.74%)</td><td>99.63 (-1.18%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>491.00 (n/a)</td><td>385.82 (n/a)</td><td>403.00 (n/a)</td><td>260.70 (n/a)</td><td>100.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.14 (-0.98%)</td><td>3.19 (-13.28%)</td><td>3.10 (-17.29%)</td><td>2.54 (-17.25%)</td><td>0.69 <b>(+34.40%)</b></td><td>4132.00 <b>(+20.84%)</b></td><td>3404.14 (+17.63%)</td><td>3381.10 <b>(+20.90%)</b></td><td>2535.30 (+0.99%)</td><td>703.88 <b>(+70.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.18 (n/a)</td><td>3.68 (n/a)</td><td>3.75 (n/a)</td><td>3.07 (n/a)</td><td>0.51 (n/a)</td><td>3419.40 (n/a)</td><td>2893.84 (n/a)</td><td>2796.70 (n/a)</td><td>2510.40 (n/a)</td><td>412.87 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (-6.81%)</td><td>0.13 (-0.75%)</td><td>0.14 (+4.99%)</td><td>0.05 <b>(-47.50%)</b></td><td>0.04 <b>(+44.95%)</b></td><td>849.70 <b>(+90.47%)</b></td><td>398.68 (+17.13%)</td><td>300.00 (-4.73%)</td><td>255.00 (+7.32%)</td><td>253.18 <b>(+218.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>446.10 (n/a)</td><td>340.38 (n/a)</td><td>314.90 (n/a)</td><td>237.60 (n/a)</td><td>79.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-8.00%)</td><td>0.02 (-1.76%)</td><td>0.02 (-9.56%)</td><td>0.02 <b>(+23.23%)</b></td><td>0.00 <b>(-57.09%)</b></td><td>309.00 (-18.86%)</td><td>285.72 (-1.88%)</td><td>291.90 (+10.57%)</td><td>242.50 (+8.70%)</td><td>25.44 <b>(-63.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>380.80 (n/a)</td><td>291.18 (n/a)</td><td>264.00 (n/a)</td><td>223.10 (n/a)</td><td>69.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-3.21%)</td><td>0.01 (-13.68%)</td><td>0.01 (-19.00%)</td><td>0.01 (-19.30%)</td><td>0.00 (-3.47%)</td><td>620.30 <b>(+23.94%)</b></td><td>419.36 (+17.73%)</td><td>390.30 <b>(+23.47%)</b></td><td>257.70 (+3.29%)</td><td>150.24 <b>(+25.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.50 (n/a)</td><td>356.20 (n/a)</td><td>316.10 (n/a)</td><td>249.50 (n/a)</td><td>119.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+6.97%)</td><td>0.02 (+19.89%)</td><td>0.01 <b>(+26.13%)</b></td><td>0.01 <b>(+34.29%)</b></td><td>0.01 (+1.50%)</td><td>540.80 <b>(-25.53%)</b></td><td>381.96 (-19.98%)</td><td>429.60 <b>(-20.71%)</b></td><td>241.30 (-6.51%)</td><td>132.59 <b>(-31.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>726.20 (n/a)</td><td>477.32 (n/a)</td><td>541.80 (n/a)</td><td>258.10 (n/a)</td><td>193.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-1.22%)</td><td>0.01 <b>(+41.03%)</b></td><td>0.01 <b>(+85.74%)</b></td><td>0.01 <b>(+280.97%)</b></td><td>0.00 <b>(-38.78%)</b></td><td>521.50 <b>(-73.75%)</b></td><td>332.48 <b>(-54.16%)</b></td><td>285.20 <b>(-46.16%)</b></td><td>238.70 (+1.23%)</td><td>111.41 <b>(-84.46%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1986.70 (n/a)</td><td>725.26 (n/a)</td><td>529.70 (n/a)</td><td>235.80 (n/a)</td><td>716.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+0.20%)</td><td>0.01 (+2.52%)</td><td>0.01 <b>(-21.83%)</b></td><td>0.01 <b>(+228.12%)</b></td><td>0.01 <b>(-25.21%)</b></td><td>587.70 <b>(-69.52%)</b></td><td>436.64 <b>(-34.97%)</b></td><td>473.70 <b>(+27.92%)</b></td><td>267.20 (-0.22%)</td><td>154.50 <b>(-78.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1928.40 (n/a)</td><td>671.40 (n/a)</td><td>370.30 (n/a)</td><td>267.80 (n/a)</td><td>709.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+0.26%)</td><td>0.01 (+11.43%)</td><td>0.01 <b>(+72.33%)</b></td><td>0.01 (-4.47%)</td><td>0.00 (-11.49%)</td><td>619.00 (+4.68%)</td><td>377.72 (-12.35%)</td><td>299.90 <b>(-41.97%)</b></td><td>245.60 (-0.24%)</td><td>158.92 (-4.61%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.30 (n/a)</td><td>430.92 (n/a)</td><td>516.80 (n/a)</td><td>246.20 (n/a)</td><td>166.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-2.28%)</td><td>0.01 (+11.08%)</td><td>0.01 (+18.99%)</td><td>0.01 <b>(+78.23%)</b></td><td>0.01 (-6.07%)</td><td>1006.40 <b>(-43.89%)</b></td><td>517.54 <b>(-26.14%)</b></td><td>472.00 (-15.95%)</td><td>250.20 (+2.37%)</td><td>305.17 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1793.60 (n/a)</td><td>700.68 (n/a)</td><td>561.60 (n/a)</td><td>244.40 (n/a)</td><td>627.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+5.39%)</td><td>0.01 <b>(+21.47%)</b></td><td>0.01 <b>(+51.20%)</b></td><td>0.01 (-6.60%)</td><td>0.00 (+8.72%)</td><td>627.70 (+7.08%)</td><td>377.04 (-16.48%)</td><td>342.00 <b>(-33.86%)</b></td><td>237.30 (-5.12%)</td><td>157.28 (+7.60%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.20 (n/a)</td><td>451.42 (n/a)</td><td>517.10 (n/a)</td><td>250.10 (n/a)</td><td>146.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+5.69%)</td><td>0.01 (-19.76%)</td><td>0.01 <b>(-31.40%)</b></td><td>0.01 (-16.49%)</td><td>0.01 <b>(+21.56%)</b></td><td>589.20 (+19.76%)</td><td>446.76 <b>(+29.64%)</b></td><td>455.00 <b>(+45.79%)</b></td><td>217.80 (-5.35%)</td><td>139.48 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.00 (n/a)</td><td>344.62 (n/a)</td><td>312.10 (n/a)</td><td>230.10 (n/a)</td><td>110.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+39.67%)</b></td><td>0.01 <b>(+24.03%)</b></td><td>0.01 <b>(+45.26%)</b></td><td>0.01 (-11.40%)</td><td>0.00 <b>(+191.47%)</b></td><td>635.80 (+12.87%)</td><td>425.14 (-9.47%)</td><td>318.00 <b>(-31.15%)</b></td><td>270.90 <b>(-28.41%)</b></td><td>181.14 <b>(+143.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.30 (n/a)</td><td>469.60 (n/a)</td><td>461.90 (n/a)</td><td>378.40 (n/a)</td><td>74.31 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (-3.65%)</td><td>0.01 <b>(-21.69%)</b></td><td>0.01 <b>(-25.49%)</b></td><td>0.01 <b>(-27.16%)</b></td><td>0.01 (+18.53%)</td><td>599.70 <b>(+37.29%)</b></td><td>470.10 <b>(+36.40%)</b></td><td>491.50 <b>(+34.22%)</b></td><td>210.20 (+3.80%)</td><td>154.49 <b>(+58.93%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>436.80 (n/a)</td><td>344.64 (n/a)</td><td>366.20 (n/a)</td><td>202.50 (n/a)</td><td>97.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 <b>(+33.51%)</b></td><td>0.01 <b>(+54.10%)</b></td><td>0.01 <b>(+36.26%)</b></td><td>0.01 <b>(+207.06%)</b></td><td>0.00 <b>(-35.15%)</b></td><td>616.70 <b>(-67.43%)</b></td><td>447.48 <b>(-47.69%)</b></td><td>416.90 <b>(-26.60%)</b></td><td>375.30 <b>(-25.10%)</b></td><td>96.32 <b>(-83.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1893.60 (n/a)</td><td>855.40 (n/a)</td><td>568.00 (n/a)</td><td>501.10 (n/a)</td><td>592.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-27.10%)</b></td><td>0.02 (-3.39%)</td><td>0.02 (+4.15%)</td><td>0.01 <b>(+121.35%)</b></td><td>0.01 <b>(-44.40%)</b></td><td>807.20 <b>(-54.82%)</b></td><td>525.78 <b>(-28.37%)</b></td><td>518.10 (-3.98%)</td><td>255.10 <b>(+37.15%)</b></td><td>196.01 <b>(-68.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1786.80 (n/a)</td><td>733.98 (n/a)</td><td>539.60 (n/a)</td><td>186.00 (n/a)</td><td>613.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (-18.15%)</td><td>0.03 <b>(-40.84%)</b></td><td>0.02 <b>(-54.05%)</b></td><td>0.02 <b>(-30.79%)</b></td><td>0.01 (-5.23%)</td><td>696.40 <b>(+44.48%)</b></td><td>507.02 <b>(+74.10%)</b></td><td>523.10 <b>(+117.60%)</b></td><td>255.50 <b>(+22.19%)</b></td><td>161.49 <b>(+46.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.00 (n/a)</td><td>291.22 (n/a)</td><td>240.40 (n/a)</td><td>209.10 (n/a)</td><td>109.99 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(+39.80%)</b></td><td>0.03 <b>(+62.57%)</b></td><td>0.03 <b>(+86.14%)</b></td><td>0.01 (-9.29%)</td><td>0.01 <b>(+91.95%)</b></td><td>621.60 (+10.23%)</td><td>321.54 <b>(-32.12%)</b></td><td>275.60 <b>(-46.29%)</b></td><td>214.40 <b>(-28.46%)</b></td><td>170.65 <b>(+59.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.90 (n/a)</td><td>473.72 (n/a)</td><td>513.10 (n/a)</td><td>299.70 (n/a)</td><td>107.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (-0.62%)</td><td>0.03 (-7.24%)</td><td>0.03 (-9.93%)</td><td>0.02 (-10.26%)</td><td>0.01 (-1.68%)</td><td>606.70 (+11.44%)</td><td>364.44 (+8.78%)</td><td>293.60 (+11.04%)</td><td>201.50 (+0.65%)</td><td>162.46 (+11.16%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>335.04 (n/a)</td><td>264.40 (n/a)</td><td>200.20 (n/a)</td><td>146.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(+30.56%)</b></td><td>0.02 (+9.22%)</td><td>0.02 (+11.24%)</td><td>0.01 <b>(+212.57%)</b></td><td>0.01 (+1.82%)</td><td>795.30 <b>(-68.01%)</b></td><td>536.78 <b>(-37.57%)</b></td><td>518.10 (-10.10%)</td><td>228.90 <b>(-23.42%)</b></td><td>220.12 <b>(-76.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2486.00 (n/a)</td><td>859.78 (n/a)</td><td>576.30 (n/a)</td><td>298.90 (n/a)</td><td>921.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (+8.93%)</td><td>0.02 (-5.13%)</td><td>0.02 (-16.12%)</td><td>0.02 (+14.64%)</td><td>0.01 (+5.20%)</td><td>546.30 (-12.77%)</td><td>454.90 (+4.53%)</td><td>505.00 (+19.22%)</td><td>262.80 (-8.18%)</td><td>118.21 (-15.47%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>626.30 (n/a)</td><td>435.18 (n/a)</td><td>423.60 (n/a)</td><td>286.20 (n/a)</td><td>139.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (+1.39%)</td><td>0.02 (-17.25%)</td><td>0.01 <b>(-23.61%)</b></td><td>0.01 (-12.58%)</td><td>0.01 (+11.63%)</td><td>676.90 (+14.40%)</td><td>525.66 <b>(+25.12%)</b></td><td>595.00 <b>(+30.91%)</b></td><td>236.90 (-1.37%)</td><td>172.18 (+19.76%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>420.14 (n/a)</td><td>454.50 (n/a)</td><td>240.20 (n/a)</td><td>143.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (-14.03%)</td><td>0.02 (-6.12%)</td><td>0.02 (-3.38%)</td><td>0.02 (-2.13%)</td><td>0.00 <b>(-27.50%)</b></td><td>544.70 (+2.20%)</td><td>465.78 (+4.89%)</td><td>481.40 (+3.50%)</td><td>340.00 (+16.32%)</td><td>82.84 (-10.95%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>444.08 (n/a)</td><td>465.10 (n/a)</td><td>292.30 (n/a)</td><td>93.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 <b>(-28.33%)</b></td><td>0.02 <b>(-33.01%)</b></td><td>0.02 (-2.38%)</td><td>0.00 <b>(-73.97%)</b></td><td>0.01 <b>(-24.15%)</b></td><td>2094.50 <b>(+284.17%)</b></td><td>787.12 <b>(+94.57%)</b></td><td>509.10 (+2.43%)</td><td>294.90 <b>(+39.50%)</b></td><td>738.16 <b>(+358.02%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.20 (n/a)</td><td>404.54 (n/a)</td><td>497.00 (n/a)</td><td>211.40 (n/a)</td><td>161.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 <b>(+25.74%)</b></td><td>0.03 <b>(+22.21%)</b></td><td>0.02 (+2.04%)</td><td>0.02 (+6.86%)</td><td>0.01 <b>(+64.81%)</b></td><td>576.50 (-6.41%)</td><td>405.90 (-12.29%)</td><td>454.20 (-2.01%)</td><td>224.80 <b>(-20.48%)</b></td><td>154.72 <b>(+24.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.00 (n/a)</td><td>462.78 (n/a)</td><td>463.50 (n/a)</td><td>282.70 (n/a)</td><td>124.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (+11.24%)</td><td>0.02 (-12.39%)</td><td>0.02 (-18.09%)</td><td>0.01 <b>(-23.52%)</b></td><td>0.01 <b>(+47.20%)</b></td><td>633.50 <b>(+30.75%)</b></td><td>451.38 <b>(+23.45%)</b></td><td>455.30 <b>(+22.10%)</b></td><td>211.10 (-10.09%)</td><td>156.63 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.50 (n/a)</td><td>365.64 (n/a)</td><td>372.90 (n/a)</td><td>234.80 (n/a)</td><td>95.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+27.84%)</b></td><td>0.05 (-10.13%)</td><td>0.03 <b>(-38.49%)</b></td><td>0.03 <b>(-32.92%)</b></td><td>0.03 <b>(+148.32%)</b></td><td>646.40 <b>(+49.08%)</b></td><td>438.72 <b>(+33.98%)</b></td><td>494.80 <b>(+62.55%)</b></td><td>197.10 <b>(-21.75%)</b></td><td>201.74 <b>(+188.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>433.60 (n/a)</td><td>327.46 (n/a)</td><td>304.40 (n/a)</td><td>251.90 (n/a)</td><td>69.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 <b>(+46.45%)</b></td><td>0.09 <b>(+95.28%)</b></td><td>0.09 <b>(+122.08%)</b></td><td>0.08 <b>(+108.63%)</b></td><td>0.01 (-12.08%)</td><td>327.10 <b>(-52.07%)</b></td><td>277.80 <b>(-51.40%)</b></td><td>282.50 <b>(-54.97%)</b></td><td>226.20 <b>(-31.70%)</b></td><td>42.29 <b>(-70.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>682.50 (n/a)</td><td>571.64 (n/a)</td><td>627.40 (n/a)</td><td>331.20 (n/a)</td><td>143.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (+5.71%)</td><td>0.04 <b>(-29.65%)</b></td><td>0.03 <b>(-52.63%)</b></td><td>0.01 <b>(-71.29%)</b></td><td>0.03 <b>(+60.39%)</b></td><td>2012.10 <b>(+248.29%)</b></td><td>736.04 <b>(+129.27%)</b></td><td>594.50 <b>(+111.12%)</b></td><td>219.10 (-5.40%)</td><td>735.27 <b>(+404.96%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.70 (n/a)</td><td>321.04 (n/a)</td><td>281.60 (n/a)</td><td>231.60 (n/a)</td><td>145.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(+23.40%)</b></td><td>0.06 (+13.31%)</td><td>0.07 <b>(+24.60%)</b></td><td>0.04 (-8.43%)</td><td>0.02 <b>(+61.41%)</b></td><td>538.50 (+9.23%)</td><td>357.58 (-5.45%)</td><td>289.10 (-19.74%)</td><td>212.80 (-18.93%)</td><td>141.99 <b>(+46.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>493.00 (n/a)</td><td>378.20 (n/a)</td><td>360.20 (n/a)</td><td>262.50 (n/a)</td><td>97.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-5.65%)</td><td>0.04 <b>(-25.09%)</b></td><td>0.03 <b>(-47.62%)</b></td><td>0.02 <b>(-46.73%)</b></td><td>0.03 (+11.00%)</td><td>1027.70 <b>(+87.71%)</b></td><td>537.26 <b>(+55.17%)</b></td><td>512.10 <b>(+90.94%)</b></td><td>202.10 (+6.03%)</td><td>322.91 <b>(+105.42%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>547.50 (n/a)</td><td>346.24 (n/a)</td><td>268.20 (n/a)</td><td>190.60 (n/a)</td><td>157.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-19.69%)</td><td>0.05 (+3.22%)</td><td>0.07 <b>(+61.89%)</b></td><td>0.01 <b>(-72.48%)</b></td><td>0.03 (+16.61%)</td><td>1962.60 <b>(+263.38%)</b></td><td>664.72 <b>(+52.46%)</b></td><td>284.90 <b>(-38.24%)</b></td><td>258.30 <b>(+24.48%)</b></td><td>735.29 <b>(+448.42%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>540.10 (n/a)</td><td>436.00 (n/a)</td><td>461.30 (n/a)</td><td>207.50 (n/a)</td><td>134.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+21.00%)</b></td><td>0.05 (+11.07%)</td><td>0.06 (+4.49%)</td><td>0.03 (+9.83%)</td><td>0.02 (+17.11%)</td><td>530.80 (-8.95%)</td><td>355.14 (-9.91%)</td><td>284.50 (-4.31%)</td><td>203.40 (-17.35%)</td><td>141.53 (-12.31%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.00 (n/a)</td><td>394.20 (n/a)</td><td>297.30 (n/a)</td><td>246.10 (n/a)</td><td>161.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+34.98%)</b></td><td>0.04 (-3.89%)</td><td>0.04 (-0.41%)</td><td>0.02 <b>(-34.39%)</b></td><td>0.02 <b>(+135.13%)</b></td><td>817.80 <b>(+52.43%)</b></td><td>518.66 (+18.89%)</td><td>463.50 (+0.41%)</td><td>241.30 <b>(-25.91%)</b></td><td>215.04 <b>(+160.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>436.24 (n/a)</td><td>461.60 (n/a)</td><td>325.70 (n/a)</td><td>82.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+54.61%)</b></td><td>0.04 (+0.60%)</td><td>0.03 <b>(-30.91%)</b></td><td>0.03 (-12.27%)</td><td>0.02 <b>(+135.53%)</b></td><td>646.00 (+13.99%)</td><td>468.88 (+11.84%)</td><td>545.50 <b>(+44.73%)</b></td><td>216.30 <b>(-35.32%)</b></td><td>176.57 <b>(+74.96%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>419.24 (n/a)</td><td>376.90 (n/a)</td><td>334.40 (n/a)</td><td>100.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (+18.12%)</td><td>0.06 <b>(+28.75%)</b></td><td>0.07 <b>(+59.80%)</b></td><td>0.04 (+6.61%)</td><td>0.01 (+8.17%)</td><td>505.20 (-6.20%)</td><td>323.48 <b>(-22.35%)</b></td><td>282.40 <b>(-37.43%)</b></td><td>244.80 (-15.35%)</td><td>104.43 (-7.04%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.60 (n/a)</td><td>416.60 (n/a)</td><td>451.30 (n/a)</td><td>289.20 (n/a)</td><td>112.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 <b>(+44.69%)</b></td><td>0.04 (+12.46%)</td><td>0.03 (-5.36%)</td><td>0.03 (-7.75%)</td><td>0.02 <b>(+159.41%)</b></td><td>655.00 (+8.39%)</td><td>495.52 (-2.17%)</td><td>542.90 (+5.66%)</td><td>263.00 <b>(-30.90%)</b></td><td>169.65 <b>(+103.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>604.30 (n/a)</td><td>506.52 (n/a)</td><td>513.80 (n/a)</td><td>380.60 (n/a)</td><td>83.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 <b>(+32.31%)</b></td><td>0.09 (+13.12%)</td><td>0.06 (-17.34%)</td><td>0.05 <b>(+171.08%)</b></td><td>0.05 <b>(+23.16%)</b></td><td>681.20 <b>(-63.11%)</b></td><td>477.04 <b>(-29.28%)</b></td><td>567.50 <b>(+20.98%)</b></td><td>208.90 <b>(-24.42%)</b></td><td>223.72 <b>(-66.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1846.60 (n/a)</td><td>674.58 (n/a)</td><td>469.10 (n/a)</td><td>276.40 (n/a)</td><td>662.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (-0.69%)</td><td>0.10 (+0.46%)</td><td>0.10 <b>(+20.92%)</b></td><td>0.06 (+0.29%)</td><td>0.03 (-19.50%)</td><td>515.90 (-0.29%)</td><td>346.34 (-2.99%)</td><td>314.30 (-17.29%)</td><td>237.80 (+0.68%)</td><td>103.64 (-11.53%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.40 (n/a)</td><td>357.02 (n/a)</td><td>380.00 (n/a)</td><td>236.20 (n/a)</td><td>117.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (-3.62%)</td><td>0.10 (-8.36%)</td><td>0.13 (+6.23%)</td><td>0.02 <b>(-70.76%)</b></td><td>0.06 <b>(+59.85%)</b></td><td>1904.20 <b>(+241.99%)</b></td><td>681.20 <b>(+70.73%)</b></td><td>316.30 (-5.86%)</td><td>268.70 (+3.75%)</td><td>700.09 <b>(+428.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>556.80 (n/a)</td><td>399.00 (n/a)</td><td>336.00 (n/a)</td><td>259.00 (n/a)</td><td>132.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(-26.07%)</b></td><td>0.06 <b>(-26.76%)</b></td><td>0.06 (-8.31%)</td><td>0.02 (+17.31%)</td><td>0.03 <b>(-36.92%)</b></td><td>1873.60 (-14.76%)</td><td>800.52 (+7.18%)</td><td>515.30 (+9.06%)</td><td>375.00 <b>(+35.23%)</b></td><td>617.13 <b>(-24.55%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2198.00 (n/a)</td><td>746.90 (n/a)</td><td>472.50 (n/a)</td><td>277.30 (n/a)</td><td>817.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 <b>(+22.10%)</b></td><td>0.11 (+2.86%)</td><td>0.09 (-14.93%)</td><td>0.08 <b>(+22.72%)</b></td><td>0.04 (+14.53%)</td><td>494.60 (-18.52%)</td><td>405.32 (-3.49%)</td><td>454.20 (+17.55%)</td><td>239.50 (-18.09%)</td><td>108.76 <b>(-20.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>607.00 (n/a)</td><td>419.98 (n/a)</td><td>386.40 (n/a)</td><td>292.40 (n/a)</td><td>137.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (-17.01%)</td><td>0.07 (+5.01%)</td><td>0.08 (+5.38%)</td><td>0.05 <b>(+61.91%)</b></td><td>0.02 <b>(-36.51%)</b></td><td>643.00 <b>(-38.24%)</b></td><td>469.02 (-15.35%)</td><td>419.90 (-5.11%)</td><td>356.40 <b>(+20.53%)</b></td><td>127.09 <b>(-56.02%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1041.10 (n/a)</td><td>554.04 (n/a)</td><td>442.50 (n/a)</td><td>295.70 (n/a)</td><td>288.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(-38.88%)</b></td><td>0.07 (-15.36%)</td><td>0.07 (-2.41%)</td><td>0.05 <b>(+262.38%)</b></td><td>0.02 <b>(-68.69%)</b></td><td>675.50 <b>(-72.41%)</b></td><td>536.68 <b>(-34.94%)</b></td><td>542.10 (+2.48%)</td><td>382.00 <b>(+63.60%)</b></td><td>122.80 <b>(-86.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2448.00 (n/a)</td><td>824.92 (n/a)</td><td>529.00 (n/a)</td><td>233.50 (n/a)</td><td>920.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (-5.76%)</td><td>0.08 (-11.64%)</td><td>0.07 (-6.78%)</td><td>0.06 (+6.83%)</td><td>0.03 (-7.89%)</td><td>584.10 (-6.39%)</td><td>466.18 (+11.50%)</td><td>476.30 (+7.27%)</td><td>245.10 (+6.15%)</td><td>137.65 (-8.23%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>624.00 (n/a)</td><td>418.10 (n/a)</td><td>444.00 (n/a)</td><td>230.90 (n/a)</td><td>150.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (+4.93%)</td><td>0.10 (+1.65%)</td><td>0.09 (+4.58%)</td><td>0.06 (-4.23%)</td><td>0.04 (+12.74%)</td><td>576.50 (+4.42%)</td><td>433.00 (+0.92%)</td><td>425.70 (-4.38%)</td><td>228.40 (-4.67%)</td><td>146.75 (+16.55%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>552.10 (n/a)</td><td>429.06 (n/a)</td><td>445.20 (n/a)</td><td>239.60 (n/a)</td><td>125.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 <b>(+26.88%)</b></td><td>0.10 <b>(+64.56%)</b></td><td>0.09 <b>(+47.06%)</b></td><td>0.06 <b>(+294.13%)</b></td><td>0.03 (-13.15%)</td><td>517.50 <b>(-74.63%)</b></td><td>347.66 <b>(-55.99%)</b></td><td>351.20 <b>(-31.99%)</b></td><td>252.90 <b>(-21.19%)</b></td><td>105.97 <b>(-84.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2039.70 (n/a)</td><td>790.04 (n/a)</td><td>516.40 (n/a)</td><td>320.90 (n/a)</td><td>706.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 <b>(-22.01%)</b></td><td>0.08 (+11.52%)</td><td>0.07 (+17.44%)</td><td>0.07 <b>(+86.10%)</b></td><td>0.01 <b>(-68.12%)</b></td><td>299.10 <b>(-46.26%)</b></td><td>274.16 <b>(-25.28%)</b></td><td>287.30 (-14.85%)</td><td>214.30 <b>(+28.25%)</b></td><td>34.56 <b>(-79.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>556.60 (n/a)</td><td>366.90 (n/a)</td><td>337.40 (n/a)</td><td>167.10 (n/a)</td><td>167.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (+4.89%)</td><td>0.05 (+0.44%)</td><td>0.05 (+11.16%)</td><td>0.04 (-10.77%)</td><td>0.02 (+15.98%)</td><td>536.60 (+12.07%)</td><td>413.72 (+1.66%)</td><td>405.70 (-10.04%)</td><td>244.00 (-4.69%)</td><td>114.48 <b>(+22.19%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>478.80 (n/a)</td><td>406.96 (n/a)</td><td>451.00 (n/a)</td><td>256.00 (n/a)</td><td>93.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 <b>(-46.48%)</b></td><td>0.04 (-15.05%)</td><td>0.04 (-6.65%)</td><td>0.03 <b>(+198.13%)</b></td><td>0.01 <b>(-75.16%)</b></td><td>651.00 <b>(-66.46%)</b></td><td>499.50 <b>(-27.93%)</b></td><td>504.00 (+7.14%)</td><td>414.60 <b>(+86.84%)</b></td><td>95.92 <b>(-86.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1940.90 (n/a)</td><td>693.04 (n/a)</td><td>470.40 (n/a)</td><td>221.90 (n/a)</td><td>705.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-2.21%)</td><td>0.05 (-9.92%)</td><td>0.04 (-13.96%)</td><td>0.03 (-7.44%)</td><td>0.02 (+7.42%)</td><td>612.50 (+8.04%)</td><td>497.14 (+13.37%)</td><td>552.80 (+16.21%)</td><td>271.20 (+2.26%)</td><td>143.94 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>566.90 (n/a)</td><td>438.50 (n/a)</td><td>475.70 (n/a)</td><td>265.20 (n/a)</td><td>118.49 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (+3.88%)</td><td>0.05 (-18.82%)</td><td>0.04 <b>(-41.26%)</b></td><td>0.03 <b>(-25.43%)</b></td><td>0.02 <b>(+22.54%)</b></td><td>681.30 <b>(+34.11%)</b></td><td>469.18 <b>(+33.24%)</b></td><td>508.60 <b>(+70.21%)</b></td><td>239.20 (-3.74%)</td><td>195.91 <b>(+61.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>508.00 (n/a)</td><td>352.14 (n/a)</td><td>298.80 (n/a)</td><td>248.50 (n/a)</td><td>121.68 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-2.62%)</td><td>0.06 (-2.98%)</td><td>0.06 <b>(-24.77%)</b></td><td>0.03 (+1.25%)</td><td>0.02 <b>(-24.86%)</b></td><td>612.20 (-1.24%)</td><td>364.54 (-3.14%)</td><td>339.50 <b>(+32.93%)</b></td><td>248.80 (+2.68%)</td><td>145.44 (-18.49%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>619.90 (n/a)</td><td>376.36 (n/a)</td><td>255.40 (n/a)</td><td>242.30 (n/a)</td><td>178.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (+2.74%)</td><td>0.06 (-16.37%)</td><td>0.05 <b>(-32.72%)</b></td><td>0.01 <b>(-77.48%)</b></td><td>0.03 <b>(+64.49%)</b></td><td>2516.20 <b>(+344.17%)</b></td><td>807.16 <b>(+109.01%)</b></td><td>464.70 <b>(+48.61%)</b></td><td>276.60 (-2.64%)</td><td>960.50 <b>(+661.58%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>566.50 (n/a)</td><td>386.18 (n/a)</td><td>312.70 (n/a)</td><td>284.10 (n/a)</td><td>126.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-17.39%)</td><td>0.06 (-7.99%)</td><td>0.06 <b>(-21.37%)</b></td><td>0.05 (+11.05%)</td><td>0.02 <b>(-37.32%)</b></td><td>537.00 (-9.96%)</td><td>405.78 (+0.80%)</td><td>437.10 <b>(+27.17%)</b></td><td>297.10 <b>(+21.07%)</b></td><td>102.35 <b>(-36.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>596.40 (n/a)</td><td>402.56 (n/a)</td><td>343.70 (n/a)</td><td>245.40 (n/a)</td><td>162.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (-5.67%)</td><td>0.06 (-15.09%)</td><td>0.06 <b>(-22.65%)</b></td><td>0.05 (-6.01%)</td><td>0.02 (-13.74%)</td><td>510.00 (+6.38%)</td><td>404.68 (+16.64%)</td><td>412.20 <b>(+29.30%)</b></td><td>266.30 (+6.01%)</td><td>99.25 (-1.23%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>479.40 (n/a)</td><td>346.94 (n/a)</td><td>318.80 (n/a)</td><td>251.20 (n/a)</td><td>100.48 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (-13.26%)</td><td>0.07 (-10.82%)</td><td>0.08 (-12.38%)</td><td>0.04 (-8.48%)</td><td>0.02 (-19.10%)</td><td>605.60 (+9.25%)</td><td>413.94 (+9.29%)</td><td>305.20 (+14.14%)</td><td>291.50 (+15.26%)</td><td>157.04 (-1.67%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>554.30 (n/a)</td><td>378.76 (n/a)</td><td>267.40 (n/a)</td><td>252.90 (n/a)</td><td>159.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (-4.18%)</td><td>0.06 (-5.49%)</td><td>0.05 (-14.23%)</td><td>0.05 (+7.44%)</td><td>0.02 (-9.88%)</td><td>522.80 (-6.93%)</td><td>433.66 (+4.18%)</td><td>468.10 (+16.59%)</td><td>267.60 (+4.37%)</td><td>97.70 (-15.91%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.70 (n/a)</td><td>416.28 (n/a)</td><td>401.50 (n/a)</td><td>256.40 (n/a)</td><td>116.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (+1.16%)</td><td>0.06 <b>(-20.67%)</b></td><td>0.06 <b>(-32.08%)</b></td><td>0.03 <b>(-22.41%)</b></td><td>0.03 <b>(+20.57%)</b></td><td>763.70 <b>(+28.87%)</b></td><td>464.86 <b>(+34.01%)</b></td><td>422.90 <b>(+47.25%)</b></td><td>241.80 (-1.14%)</td><td>204.94 <b>(+45.35%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.60 (n/a)</td><td>346.88 (n/a)</td><td>287.20 (n/a)</td><td>244.60 (n/a)</td><td>141.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (-0.89%)</td><td>0.05 (-15.44%)</td><td>0.05 <b>(-24.99%)</b></td><td>0.03 <b>(-27.22%)</b></td><td>0.02 (+15.44%)</td><td>645.00 <b>(+37.41%)</b></td><td>416.16 <b>(+24.62%)</b></td><td>405.30 <b>(+33.32%)</b></td><td>247.80 (+0.90%)</td><td>160.67 <b>(+61.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>469.40 (n/a)</td><td>333.94 (n/a)</td><td>304.00 (n/a)</td><td>245.60 (n/a)</td><td>99.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (-9.89%)</td><td>0.04 (-19.19%)</td><td>0.04 <b>(-44.15%)</b></td><td>0.03 <b>(+38.10%)</b></td><td>0.01 <b>(-45.96%)</b></td><td>591.00 <b>(-27.59%)</b></td><td>453.38 (+4.46%)</td><td>478.70 <b>(+79.02%)</b></td><td>283.90 (+10.99%)</td><td>113.72 <b>(-55.06%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>816.20 (n/a)</td><td>434.02 (n/a)</td><td>267.40 (n/a)</td><td>255.80 (n/a)</td><td>253.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (+18.39%)</td><td>0.05 <b>(-22.32%)</b></td><td>0.05 <b>(-21.85%)</b></td><td>0.03 <b>(-53.16%)</b></td><td>0.02 <b>(+422.61%)</b></td><td>591.60 <b>(+113.50%)</b></td><td>384.14 <b>(+46.89%)</b></td><td>337.50 <b>(+27.94%)</b></td><td>205.10 (-15.53%)</td><td>153.01 <b>(+851.77%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>277.10 (n/a)</td><td>261.52 (n/a)</td><td>263.80 (n/a)</td><td>242.80 (n/a)</td><td>16.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 <b>(-26.84%)</b></td><td>0.05 (-14.48%)</td><td>0.04 (-8.21%)</td><td>0.03 (+2.84%)</td><td>0.01 <b>(-41.43%)</b></td><td>547.40 (-2.75%)</td><td>427.42 (+8.56%)</td><td>459.60 (+8.94%)</td><td>300.90 <b>(+36.71%)</b></td><td>117.32 <b>(-23.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>562.90 (n/a)</td><td>393.72 (n/a)</td><td>421.90 (n/a)</td><td>220.10 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (+4.18%)</td><td>0.05 (+19.83%)</td><td>0.04 (-4.37%)</td><td>0.04 <b>(+310.89%)</b></td><td>0.02 <b>(-24.54%)</b></td><td>483.30 <b>(-75.66%)</b></td><td>388.64 <b>(-44.76%)</b></td><td>449.50 (+4.56%)</td><td>229.20 (-4.02%)</td><td>111.44 <b>(-84.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1985.70 (n/a)</td><td>703.54 (n/a)</td><td>429.90 (n/a)</td><td>238.80 (n/a)</td><td>721.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (+8.35%)</td><td>0.05 (+0.92%)</td><td>0.04 (-18.71%)</td><td>0.04 (+2.57%)</td><td>0.01 <b>(+54.15%)</b></td><td>471.50 (-2.50%)</td><td>396.74 (+2.27%)</td><td>469.80 <b>(+23.02%)</b></td><td>280.90 (-7.72%)</td><td>101.07 <b>(+40.76%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>483.60 (n/a)</td><td>387.94 (n/a)</td><td>381.90 (n/a)</td><td>304.40 (n/a)</td><td>71.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.38 (-5.69%)</td><td>0.27 (-5.29%)</td><td>0.27 (-12.77%)</td><td>0.18 <b>(+31.48%)</b></td><td>0.08 <b>(-20.89%)</b></td><td>537.10 <b>(-23.95%)</b></td><td>394.64 (-1.10%)</td><td>361.80 (+14.64%)</td><td>259.60 (+6.05%)</td><td>122.02 <b>(-35.09%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>706.20 (n/a)</td><td>399.02 (n/a)</td><td>315.60 (n/a)</td><td>244.80 (n/a)</td><td>187.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.36 <b>(+33.34%)</b></td><td>0.22 (+3.51%)</td><td>0.20 (-3.34%)</td><td>0.15 <b>(+24.42%)</b></td><td>0.09 <b>(+34.90%)</b></td><td>646.50 (-19.63%)</td><td>497.56 (-2.32%)</td><td>490.50 (+3.46%)</td><td>269.70 <b>(-25.02%)</b></td><td>153.94 (-15.91%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>804.40 (n/a)</td><td>509.40 (n/a)</td><td>474.10 (n/a)</td><td>359.70 (n/a)</td><td>183.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.43 (+1.31%)</td><td>0.28 (-14.51%)</td><td>0.23 <b>(-30.60%)</b></td><td>0.16 (-19.43%)</td><td>0.11 <b>(+36.18%)</b></td><td>618.00 <b>(+24.12%)</b></td><td>397.74 <b>(+24.91%)</b></td><td>428.70 <b>(+44.10%)</b></td><td>230.90 (-1.28%)</td><td>158.00 <b>(+51.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>497.90 (n/a)</td><td>318.42 (n/a)</td><td>297.50 (n/a)</td><td>233.90 (n/a)</td><td>104.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.26 (-7.89%)</td><td>0.18 (-18.04%)</td><td>0.14 <b>(-32.51%)</b></td><td>0.14 (-18.87%)</td><td>0.06 <b>(+23.45%)</b></td><td>545.50 <b>(+23.25%)</b></td><td>436.90 <b>(+27.64%)</b></td><td>524.40 <b>(+48.18%)</b></td><td>281.20 (+8.57%)</td><td>132.29 <b>(+71.85%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>442.60 (n/a)</td><td>342.30 (n/a)</td><td>353.90 (n/a)</td><td>259.00 (n/a)</td><td>76.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.29 (+4.06%)</td><td>0.24 (+13.60%)</td><td>0.25 (+4.56%)</td><td>0.15 (+15.76%)</td><td>0.05 (-18.44%)</td><td>488.80 (-13.61%)</td><td>325.90 (-14.96%)</td><td>291.50 (-4.36%)</td><td>256.90 (-3.89%)</td><td>92.68 <b>(-28.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>565.80 (n/a)</td><td>383.24 (n/a)</td><td>304.80 (n/a)</td><td>267.30 (n/a)</td><td>130.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 <b>(+86.77%)</b></td><td>0.27 <b>(+25.83%)</b></td><td>0.25 (+17.02%)</td><td>0.12 <b>(-33.20%)</b></td><td>0.14 <b>(+254.73%)</b></td><td>632.60 <b>(+49.69%)</b></td><td>334.02 (-3.86%)</td><td>298.40 (-14.55%)</td><td>143.70 <b>(-46.46%)</b></td><td>179.80 <b>(+185.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>422.60 (n/a)</td><td>347.44 (n/a)</td><td>349.20 (n/a)</td><td>268.40 (n/a)</td><td>62.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 <b>(-20.59%)</b></td><td>0.09 <b>(-23.03%)</b></td><td>0.11 (-19.29%)</td><td>0.06 (-7.03%)</td><td>0.03 (-12.39%)</td><td>617.40 (+7.56%)</td><td>431.44 <b>(+30.01%)</b></td><td>341.50 <b>(+23.91%)</b></td><td>304.50 <b>(+25.93%)</b></td><td>156.45 (+13.57%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.00 (n/a)</td><td>331.84 (n/a)</td><td>275.60 (n/a)</td><td>241.80 (n/a)</td><td>137.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (-7.87%)</td><td>0.10 (+8.14%)</td><td>0.11 <b>(+44.77%)</b></td><td>0.06 (-10.60%)</td><td>0.02 (-19.26%)</td><td>610.60 (+11.87%)</td><td>393.94 (-8.81%)</td><td>334.30 <b>(-30.93%)</b></td><td>319.20 (+8.57%)</td><td>124.17 (+0.58%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>545.80 (n/a)</td><td>431.98 (n/a)</td><td>484.00 (n/a)</td><td>294.00 (n/a)</td><td>123.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 <b>(+25.42%)</b></td><td>0.10 (+15.56%)</td><td>0.08 (-3.24%)</td><td>0.06 (-9.95%)</td><td>0.05 <b>(+83.66%)</b></td><td>618.80 (+11.06%)</td><td>415.04 (-3.71%)</td><td>487.60 (+3.35%)</td><td>219.10 <b>(-20.27%)</b></td><td>173.01 <b>(+59.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>557.20 (n/a)</td><td>431.04 (n/a)</td><td>471.80 (n/a)</td><td>274.80 (n/a)</td><td>108.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 <b>(+40.39%)</b></td><td>0.11 (+13.62%)</td><td>0.12 <b>(+40.01%)</b></td><td>0.06 (+2.55%)</td><td>0.06 <b>(+49.07%)</b></td><td>634.70 (-2.49%)</td><td>387.60 (-6.00%)</td><td>307.00 <b>(-28.59%)</b></td><td>185.10 <b>(-28.78%)</b></td><td>179.45 (+12.46%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>650.90 (n/a)</td><td>412.32 (n/a)</td><td>429.90 (n/a)</td><td>259.90 (n/a)</td><td>159.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (+5.65%)</td><td>0.10 (-6.58%)</td><td>0.11 (-4.17%)</td><td>0.07 (-17.35%)</td><td>0.02 <b>(+43.31%)</b></td><td>542.20 <b>(+21.00%)</b></td><td>380.16 (+10.35%)</td><td>338.10 (+4.35%)</td><td>281.90 (-5.34%)</td><td>103.87 <b>(+66.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>448.10 (n/a)</td><td>344.50 (n/a)</td><td>324.00 (n/a)</td><td>297.80 (n/a)</td><td>62.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (+2.17%)</td><td>0.09 (-10.17%)</td><td>0.08 <b>(-25.42%)</b></td><td>0.07 (+4.24%)</td><td>0.03 (-4.35%)</td><td>519.80 (-4.08%)</td><td>431.44 (+9.83%)</td><td>460.30 <b>(+34.08%)</b></td><td>262.20 (-2.13%)</td><td>106.26 (-14.00%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>541.90 (n/a)</td><td>392.84 (n/a)</td><td>343.30 (n/a)</td><td>267.90 (n/a)</td><td>123.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (+13.24%)</td><td>0.10 (-17.00%)</td><td>0.10 <b>(-28.15%)</b></td><td>0.05 <b>(-44.64%)</b></td><td>0.04 <b>(+102.83%)</b></td><td>758.90 <b>(+80.65%)</b></td><td>457.46 <b>(+37.08%)</b></td><td>417.60 <b>(+39.15%)</b></td><td>249.50 (-11.71%)</td><td>204.17 <b>(+226.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>420.10 (n/a)</td><td>333.72 (n/a)</td><td>300.10 (n/a)</td><td>282.60 (n/a)</td><td>62.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(-45.83%)</b></td><td>0.07 <b>(-40.88%)</b></td><td>0.07 <b>(-52.71%)</b></td><td>0.04 <b>(+67.39%)</b></td><td>0.02 <b>(-67.27%)</b></td><td>1131.90 <b>(-40.26%)</b></td><td>658.98 (+4.63%)</td><td>559.80 <b>(+111.48%)</b></td><td>468.50 <b>(+84.59%)</b></td><td>271.35 <b>(-61.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1894.70 (n/a)</td><td>629.84 (n/a)</td><td>264.70 (n/a)</td><td>253.80 (n/a)</td><td>713.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.27 <b>(+69.25%)</b></td><td>0.15 <b>(+41.35%)</b></td><td>0.15 <b>(+60.06%)</b></td><td>0.08 (-4.22%)</td><td>0.08 <b>(+142.07%)</b></td><td>545.30 (+4.40%)</td><td>338.58 (-18.62%)</td><td>274.90 <b>(-37.54%)</b></td><td>154.10 <b>(-40.91%)</b></td><td>159.72 <b>(+59.63%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>522.30 (n/a)</td><td>416.04 (n/a)</td><td>440.10 (n/a)</td><td>260.80 (n/a)</td><td>100.06 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.19 <b>(+98.32%)</b></td><td>0.10 (+18.98%)</td><td>0.08 (-3.44%)</td><td>0.06 (+3.37%)</td><td>0.05 <b>(+266.84%)</b></td><td>639.30 (-3.27%)</td><td>489.02 (-3.51%)</td><td>523.10 (+3.56%)</td><td>210.70 <b>(-49.57%)</b></td><td>175.57 <b>(+77.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>660.90 (n/a)</td><td>506.80 (n/a)</td><td>505.10 (n/a)</td><td>417.80 (n/a)</td><td>98.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (+12.97%)</td><td>0.11 (-0.04%)</td><td>0.10 (-7.16%)</td><td>0.07 (-13.20%)</td><td>0.04 <b>(+45.55%)</b></td><td>549.40 (+15.20%)</td><td>397.36 (+4.29%)</td><td>407.50 (+7.72%)</td><td>261.00 (-11.50%)</td><td>122.08 <b>(+47.14%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>476.90 (n/a)</td><td>381.02 (n/a)</td><td>378.30 (n/a)</td><td>294.90 (n/a)</td><td>82.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 <b>(-20.76%)</b></td><td>0.11 (+4.73%)</td><td>0.13 <b>(+58.95%)</b></td><td>0.07 (+11.37%)</td><td>0.04 <b>(-27.13%)</b></td><td>620.70 (-10.21%)</td><td>407.46 (-10.38%)</td><td>313.70 <b>(-37.08%)</b></td><td>274.20 <b>(+26.24%)</b></td><td>162.54 (-16.61%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>691.30 (n/a)</td><td>454.66 (n/a)</td><td>498.60 (n/a)</td><td>217.20 (n/a)</td><td>194.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (-1.04%)</td><td>0.11 (+16.35%)</td><td>0.12 <b>(+50.22%)</b></td><td>0.05 (-17.64%)</td><td>0.03 (+3.01%)</td><td>713.70 <b>(+21.42%)</b></td><td>372.48 (-10.62%)</td><td>295.90 <b>(-33.42%)</b></td><td>272.50 (+1.04%)</td><td>191.25 <b>(+38.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.80 (n/a)</td><td>416.76 (n/a)</td><td>444.40 (n/a)</td><td>269.70 (n/a)</td><td>138.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (-9.65%)</td><td>0.10 <b>(+38.51%)</b></td><td>0.11 <b>(+57.08%)</b></td><td>0.07 <b>(+128.83%)</b></td><td>0.02 <b>(-60.33%)</b></td><td>471.00 <b>(-56.30%)</b></td><td>346.74 <b>(-45.93%)</b></td><td>321.30 <b>(-36.33%)</b></td><td>288.70 (+10.70%)</td><td>71.53 <b>(-81.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1077.80 (n/a)</td><td>641.26 (n/a)</td><td>504.60 (n/a)</td><td>260.80 (n/a)</td><td>386.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (+10.50%)</td><td>0.08 (-3.86%)</td><td>0.07 (-6.03%)</td><td>0.05 <b>(-29.96%)</b></td><td>0.02 <b>(+218.45%)</b></td><td>674.50 <b>(+42.78%)</b></td><td>482.22 (+8.32%)</td><td>476.00 (+6.42%)</td><td>360.70 (-9.51%)</td><td>119.31 <b>(+324.93%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>472.40 (n/a)</td><td>445.18 (n/a)</td><td>447.30 (n/a)</td><td>398.60 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(-24.59%)</b></td><td>0.06 <b>(-24.43%)</b></td><td>0.07 (-11.39%)</td><td>0.02 <b>(-66.86%)</b></td><td>0.03 (+17.56%)</td><td>1847.10 <b>(+201.72%)</b></td><td>749.02 <b>(+70.95%)</b></td><td>497.50 (+12.84%)</td><td>385.80 <b>(+32.62%)</b></td><td>617.60 <b>(+424.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>612.20 (n/a)</td><td>438.14 (n/a)</td><td>440.90 (n/a)</td><td>290.90 (n/a)</td><td>117.81 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.18 <b>(+27.69%)</b></td><td>0.12 (+18.78%)</td><td>0.11 (+9.85%)</td><td>0.08 <b>(+47.09%)</b></td><td>0.04 (+11.82%)</td><td>444.70 <b>(-32.02%)</b></td><td>325.82 (-19.18%)</td><td>304.70 (-8.96%)</td><td>195.70 <b>(-21.69%)</b></td><td>93.83 <b>(-42.70%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>654.20 (n/a)</td><td>403.14 (n/a)</td><td>334.70 (n/a)</td><td>249.90 (n/a)</td><td>163.77 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 <b>(-34.44%)</b></td><td>0.08 <b>(-24.96%)</b></td><td>0.08 <b>(-35.62%)</b></td><td>0.06 (+5.52%)</td><td>0.01 <b>(-66.23%)</b></td><td>582.40 (-5.22%)</td><td>471.08 (+18.83%)</td><td>462.60 <b>(+55.29%)</b></td><td>367.60 <b>(+52.53%)</b></td><td>79.57 <b>(-53.10%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>614.50 (n/a)</td><td>396.42 (n/a)</td><td>297.90 (n/a)</td><td>241.00 (n/a)</td><td>169.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.46 (+14.73%)</td><td>0.29 (-6.08%)</td><td>0.29 (+15.09%)</td><td>0.10 <b>(-54.42%)</b></td><td>0.13 <b>(+46.36%)</b></td><td>1288.20 <b>(+119.38%)</b></td><td>583.36 <b>(+28.38%)</b></td><td>447.00 (-13.10%)</td><td>284.70 (-12.83%)</td><td>400.34 <b>(+234.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>587.20 (n/a)</td><td>454.40 (n/a)</td><td>514.40 (n/a)</td><td>326.60 (n/a)</td><td>119.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.53 <b>(+21.98%)</b></td><td>0.34 <b>(+28.28%)</b></td><td>0.36 <b>(+72.21%)</b></td><td>0.20 (-4.73%)</td><td>0.14 <b>(+40.97%)</b></td><td>658.30 (+4.96%)</td><td>435.20 (-17.73%)</td><td>362.90 <b>(-41.93%)</b></td><td>249.30 (-18.02%)</td><td>178.17 <b>(+23.36%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.43 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>627.20 (n/a)</td><td>529.00 (n/a)</td><td>624.90 (n/a)</td><td>304.10 (n/a)</td><td>144.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 (-8.39%)</td><td>0.39 <b>(+26.55%)</b></td><td>0.40 <b>(+63.82%)</b></td><td>0.28 (+17.14%)</td><td>0.10 <b>(-29.83%)</b></td><td>473.90 (-14.64%)</td><td>359.16 <b>(-25.28%)</b></td><td>326.50 <b>(-38.95%)</b></td><td>258.40 (+9.17%)</td><td>93.99 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.55 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>555.20 (n/a)</td><td>480.70 (n/a)</td><td>534.80 (n/a)</td><td>236.70 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-4.15%)</td><td>0.01 (-8.93%)</td><td>0.01 (-14.79%)</td><td>0.01 (-11.88%)</td><td>0.00 (-1.52%)</td><td>511.40 (+13.49%)</td><td>353.76 (+10.52%)</td><td>340.10 (+17.36%)</td><td>275.10 (+4.32%)</td><td>92.32 (+19.97%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.60 (n/a)</td><td>320.08 (n/a)</td><td>289.80 (n/a)</td><td>263.70 (n/a)</td><td>76.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+16.64%)</td><td>0.01 (+7.39%)</td><td>0.01 (+8.17%)</td><td>0.01 (-7.46%)</td><td>0.00 <b>(+31.94%)</b></td><td>547.10 (+8.06%)</td><td>334.82 (-3.44%)</td><td>276.10 (-7.57%)</td><td>228.80 (-14.28%)</td><td>128.29 <b>(+27.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.30 (n/a)</td><td>346.76 (n/a)</td><td>298.70 (n/a)</td><td>266.90 (n/a)</td><td>101.01 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (+5.90%)</td><td>0.01 (+6.97%)</td><td>0.01 (-7.62%)</td><td>0.01 (+12.11%)</td><td>0.00 <b>(-21.23%)</b></td><td>475.40 (-10.81%)</td><td>330.18 (-9.97%)</td><td>306.30 (+8.27%)</td><td>253.40 (-5.55%)</td><td>86.69 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.00 (n/a)</td><td>366.74 (n/a)</td><td>282.90 (n/a)</td><td>268.30 (n/a)</td><td>124.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>10.97 (+6.13%)</td><td>7.67 (-4.38%)</td><td>8.06 (+2.41%)</td><td>3.69 <b>(-37.72%)</b></td><td>2.94 <b>(+74.54%)</b></td><td>569.00 <b>(+60.60%)</b></td><td>318.80 (+17.53%)</td><td>260.20 (-2.33%)</td><td>191.30 (-5.76%)</td><td>153.84 <b>(+166.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>10.34 (n/a)</td><td>8.02 (n/a)</td><td>7.88 (n/a)</td><td>5.92 (n/a)</td><td>1.68 (n/a)</td><td>354.30 (n/a)</td><td>271.24 (n/a)</td><td>266.40 (n/a)</td><td>203.00 (n/a)</td><td>57.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.49 (-14.54%)</td><td>0.34 <b>(-29.48%)</b></td><td>0.30 <b>(-37.28%)</b></td><td>0.23 <b>(-44.21%)</b></td><td>0.12 <b>(+58.37%)</b></td><td>579.60 <b>(+79.22%)</b></td><td>420.84 <b>(+52.68%)</b></td><td>441.60 <b>(+59.42%)</b></td><td>267.50 (+17.02%)</td><td>136.69 <b>(+225.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.08 (n/a)</td><td>323.40 (n/a)</td><td>275.64 (n/a)</td><td>277.00 (n/a)</td><td>228.60 (n/a)</td><td>41.97 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.58 (-1.38%)</td><td>0.47 (-3.59%)</td><td>0.42 (-11.61%)</td><td>0.40 (-7.08%)</td><td>0.08 <b>(+37.39%)</b></td><td>326.40 (+7.62%)</td><td>285.64 (+4.99%)</td><td>315.50 (+13.16%)</td><td>227.20 (+1.43%)</td><td>46.87 <b>(+52.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.59 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.06 (n/a)</td><td>303.30 (n/a)</td><td>272.06 (n/a)</td><td>278.80 (n/a)</td><td>224.00 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.61 (+15.50%)</td><td>0.42 (+4.53%)</td><td>0.37 (-11.34%)</td><td>0.26 (+7.30%)</td><td>0.16 <b>(+24.12%)</b></td><td>518.00 (-6.80%)</td><td>352.70 (-2.23%)</td><td>359.90 (+12.79%)</td><td>216.40 (-13.41%)</td><td>130.54 (-0.32%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>555.80 (n/a)</td><td>360.76 (n/a)</td><td>319.10 (n/a)</td><td>249.90 (n/a)</td><td>130.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.49 (+4.95%)</td><td>0.34 (+1.98%)</td><td>0.29 (-0.93%)</td><td>0.21 (-15.54%)</td><td>0.13 <b>(+47.79%)</b></td><td>621.50 (+18.40%)</td><td>437.20 (+4.66%)</td><td>456.90 (+0.93%)</td><td>271.10 (-4.71%)</td><td>158.29 <b>(+60.07%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.46 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>524.90 (n/a)</td><td>417.72 (n/a)</td><td>452.70 (n/a)</td><td>284.50 (n/a)</td><td>98.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 (-13.73%)</td><td>0.38 (-13.75%)</td><td>0.42 (-8.20%)</td><td>0.25 (-15.97%)</td><td>0.10 (-6.30%)</td><td>529.70 (+19.01%)</td><td>369.18 (+17.31%)</td><td>314.20 (+8.95%)</td><td>260.30 (+15.89%)</td><td>111.01 <b>(+29.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>445.10 (n/a)</td><td>314.70 (n/a)</td><td>288.40 (n/a)</td><td>224.60 (n/a)</td><td>85.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 <b>(+23.15%)</b></td><td>0.01 (+1.20%)</td><td>0.01 (-9.69%)</td><td>0.00 <b>(-73.26%)</b></td><td>0.01 <b>(+115.68%)</b></td><td>1940.70 <b>(+274.00%)</b></td><td>682.26 <b>(+62.82%)</b></td><td>490.60 (+10.74%)</td><td>225.40 (-18.80%)</td><td>714.28 <b>(+566.96%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.90 (n/a)</td><td>419.02 (n/a)</td><td>443.00 (n/a)</td><td>277.60 (n/a)</td><td>107.10 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (-14.99%)</td><td>0.01 (-16.85%)</td><td>0.01 <b>(-35.13%)</b></td><td>0.01 (+6.62%)</td><td>0.00 <b>(-42.36%)</b></td><td>537.40 (-6.21%)</td><td>417.30 (+10.60%)</td><td>420.60 <b>(+54.18%)</b></td><td>288.80 (+17.64%)</td><td>99.91 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.00 (n/a)</td><td>377.30 (n/a)</td><td>272.80 (n/a)</td><td>245.50 (n/a)</td><td>160.02 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.00 (+0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-5.99%)</td><td>16536.32 (-17.62%)</td><td>13184.46 (-0.55%)</td><td>14834.15 (+16.31%)</td><td>5894.38 (-6.16%)</td><td>4198.18 <b>(-26.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20073.30 (n/a)</td><td>13256.90 (n/a)</td><td>12753.57 (n/a)</td><td>6281.02 (n/a)</td><td>5679.58 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+30.56%)</b></td><td>0.00 <b>(+140.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+39.74%)</b></td><td>22688.14 (-1.34%)</td><td>11954.37 (-18.43%)</td><td>6766.77 <b>(-61.60%)</b></td><td>5896.34 (-10.44%)</td><td>7929.99 (+13.22%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22995.17 (n/a)</td><td>14655.61 (n/a)</td><td>17621.14 (n/a)</td><td>6584.00 (n/a)</td><td>7003.90 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (+3.37%)</td><td>0.10 (+14.37%)</td><td>0.08 (+5.28%)</td><td>0.07 (+6.90%)</td><td>0.03 (+16.63%)</td><td>28185.36 (-6.51%)</td><td>22595.87 (-11.42%)</td><td>25661.19 (-5.09%)</td><td>15556.05 (-3.27%)</td><td>6043.46 (+8.17%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30149.47 (n/a)</td><td>25509.68 (n/a)</td><td>27037.34 (n/a)</td><td>16081.15 (n/a)</td><td>5587.24 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.07 (+13.60%)</td><td>1.35 (-8.50%)</td><td>1.34 (-3.99%)</td><td>0.31 (+4.61%)</td><td>1.15 (+6.56%)</td><td>3419.10 (-4.41%)</td><td>1692.54 <b>(+21.25%)</b></td><td>780.90 (+4.15%)</td><td>341.20 (-11.95%)</td><td>1537.31 (+13.70%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.71 (n/a)</td><td>1.48 (n/a)</td><td>1.40 (n/a)</td><td>0.29 (n/a)</td><td>1.08 (n/a)</td><td>3576.90 (n/a)</td><td>1395.94 (n/a)</td><td>749.80 (n/a)</td><td>387.50 (n/a)</td><td>1352.11 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.15 <b>(+37.77%)</b></td><td>2.14 <b>(+58.51%)</b></td><td>1.86 (+13.22%)</td><td>1.54 <b>(+425.05%)</b></td><td>0.64 <b>(-35.97%)</b></td><td>681.40 <b>(-80.95%)</b></td><td>520.08 <b>(-69.55%)</b></td><td>564.00 (-11.68%)</td><td>332.70 <b>(-27.42%)</b></td><td>134.31 <b>(-91.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.29 (n/a)</td><td>1.35 (n/a)</td><td>1.64 (n/a)</td><td>0.29 (n/a)</td><td>0.99 (n/a)</td><td>3577.70 (n/a)</td><td>1707.88 (n/a)</td><td>638.60 (n/a)</td><td>458.40 (n/a)</td><td>1626.50 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.29 <b>(-34.12%)</b></td><td>1.53 <b>(-21.32%)</b></td><td>1.59 (-13.61%)</td><td>0.55 <b>(+83.57%)</b></td><td>0.63 <b>(-46.02%)</b></td><td>1909.70 <b>(-45.52%)</b></td><td>865.96 <b>(-20.30%)</b></td><td>661.10 (+15.76%)</td><td>457.00 <b>(+51.78%)</b></td><td>589.91 <b>(-56.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.48 (n/a)</td><td>1.95 (n/a)</td><td>1.84 (n/a)</td><td>0.30 (n/a)</td><td>1.16 (n/a)</td><td>3505.60 (n/a)</td><td>1086.50 (n/a)</td><td>571.10 (n/a)</td><td>301.10 (n/a)</td><td>1358.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.72 <b>(-30.21%)</b></td><td>1.50 <b>(-42.11%)</b></td><td>1.37 <b>(-44.77%)</b></td><td>0.61 <b>(-59.64%)</b></td><td>0.79 (-9.75%)</td><td>1724.00 <b>(+147.81%)</b></td><td>886.36 <b>(+99.62%)</b></td><td>766.60 <b>(+81.06%)</b></td><td>385.60 <b>(+43.29%)</b></td><td>511.05 <b>(+222.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.90 (n/a)</td><td>2.60 (n/a)</td><td>2.48 (n/a)</td><td>1.51 (n/a)</td><td>0.87 (n/a)</td><td>695.70 (n/a)</td><td>444.02 (n/a)</td><td>423.40 (n/a)</td><td>269.10 (n/a)</td><td>158.43 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.08 (-11.70%)</td><td>2.45 <b>(-24.54%)</b></td><td>3.33 (+7.62%)</td><td>0.59 <b>(-76.99%)</b></td><td>1.60 <b>(+94.12%)</b></td><td>3565.90 <b>(+334.65%)</b></td><td>1543.58 <b>(+128.99%)</b></td><td>629.20 (-7.07%)</td><td>513.90 (+13.24%)</td><td>1374.29 <b>(+850.43%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.62 (n/a)</td><td>3.25 (n/a)</td><td>3.10 (n/a)</td><td>2.56 (n/a)</td><td>0.82 (n/a)</td><td>820.40 (n/a)</td><td>674.08 (n/a)</td><td>677.10 (n/a)</td><td>453.80 (n/a)</td><td>144.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.35 <b>(-47.18%)</b></td><td>2.59 (+12.02%)</td><td>3.04 <b>(+174.24%)</b></td><td>0.59 (+0.50%)</td><td>1.15 <b>(-53.12%)</b></td><td>3550.00 (-0.50%)</td><td>1257.90 <b>(-37.30%)</b></td><td>689.70 <b>(-63.53%)</b></td><td>625.30 <b>(+89.31%)</b></td><td>1282.92 (-15.45%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.35 (n/a)</td><td>2.31 (n/a)</td><td>1.11 (n/a)</td><td>0.59 (n/a)</td><td>2.45 (n/a)</td><td>3567.80 (n/a)</td><td>2006.30 (n/a)</td><td>1891.30 (n/a)</td><td>330.30 (n/a)</td><td>1517.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>6.04 (+12.83%)</td><td>4.27 <b>(+78.77%)</b></td><td>4.10 <b>(+65.33%)</b></td><td>2.71 <b>(+355.35%)</b></td><td>1.23 <b>(-37.49%)</b></td><td>773.50 <b>(-78.04%)</b></td><td>526.46 <b>(-70.63%)</b></td><td>511.10 <b>(-39.51%)</b></td><td>347.50 (-11.37%)</td><td>158.99 <b>(-89.87%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.35 (n/a)</td><td>2.39 (n/a)</td><td>2.48 (n/a)</td><td>0.60 (n/a)</td><td>1.97 (n/a)</td><td>3522.20 (n/a)</td><td>1792.64 (n/a)</td><td>845.00 (n/a)</td><td>392.10 (n/a)</td><td>1570.09 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.67 (+14.67%)</td><td>4.71 (+3.32%)</td><td>3.84 (-10.76%)</td><td>2.57 (-8.83%)</td><td>2.24 <b>(+47.62%)</b></td><td>815.50 (+9.68%)</td><td>530.48 (+5.53%)</td><td>546.20 (+12.04%)</td><td>273.40 (-12.79%)</td><td>232.61 <b>(+38.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.69 (n/a)</td><td>4.56 (n/a)</td><td>4.30 (n/a)</td><td>2.82 (n/a)</td><td>1.51 (n/a)</td><td>743.50 (n/a)</td><td>502.68 (n/a)</td><td>487.50 (n/a)</td><td>313.50 (n/a)</td><td>167.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.41 <b>(+22.15%)</b></td><td>2.83 (+8.33%)</td><td>3.07 (+5.02%)</td><td>0.58 <b>(-31.82%)</b></td><td>1.40 <b>(+22.28%)</b></td><td>3636.50 <b>(+46.68%)</b></td><td>1234.80 (+15.72%)</td><td>682.80 (-4.78%)</td><td>476.10 (-18.13%)</td><td>1346.21 <b>(+67.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.61 (n/a)</td><td>2.62 (n/a)</td><td>2.92 (n/a)</td><td>0.85 (n/a)</td><td>1.14 (n/a)</td><td>2479.20 (n/a)</td><td>1067.10 (n/a)</td><td>717.10 (n/a)</td><td>581.50 (n/a)</td><td>804.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.48 <b>(+29.29%)</b></td><td>3.13 (+3.77%)</td><td>2.66 (-0.46%)</td><td>2.03 (-1.52%)</td><td>1.36 <b>(+61.43%)</b></td><td>1030.60 (+1.55%)</td><td>748.70 (+1.43%)</td><td>787.60 (+0.46%)</td><td>382.70 <b>(-22.66%)</b></td><td>236.70 (+19.46%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.24 (n/a)</td><td>3.02 (n/a)</td><td>2.67 (n/a)</td><td>2.07 (n/a)</td><td>0.84 (n/a)</td><td>1014.90 (n/a)</td><td>738.14 (n/a)</td><td>784.00 (n/a)</td><td>494.80 (n/a)</td><td>198.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.23 (-0.58%)</td><td>4.37 <b>(+22.00%)</b></td><td>4.16 (+6.42%)</td><td>3.35 <b>(+193.90%)</b></td><td>0.78 <b>(-48.32%)</b></td><td>1253.10 <b>(-65.98%)</b></td><td>985.96 <b>(-36.55%)</b></td><td>1007.40 (-6.03%)</td><td>802.00 (+0.58%)</td><td>182.78 <b>(-84.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.26 (n/a)</td><td>3.58 (n/a)</td><td>3.91 (n/a)</td><td>1.14 (n/a)</td><td>1.51 (n/a)</td><td>3682.90 (n/a)</td><td>1554.00 (n/a)</td><td>1072.10 (n/a)</td><td>797.40 (n/a)</td><td>1198.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.76 (-1.56%)</td><td>4.96 (-12.80%)</td><td>5.18 (-10.47%)</td><td>1.75 <b>(-56.29%)</b></td><td>2.14 <b>(+45.40%)</b></td><td>2391.30 <b>(+128.81%)</b></td><td>1080.26 <b>(+39.18%)</b></td><td>809.00 (+11.69%)</td><td>540.40 (+1.58%)</td><td>743.55 <b>(+280.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.88 (n/a)</td><td>5.69 (n/a)</td><td>5.79 (n/a)</td><td>4.01 (n/a)</td><td>1.47 (n/a)</td><td>1045.10 (n/a)</td><td>776.18 (n/a)</td><td>724.30 (n/a)</td><td>532.00 (n/a)</td><td>195.55 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.71 <b>(+31.82%)</b></td><td>6.28 <b>(+78.66%)</b></td><td>6.54 <b>(+63.50%)</b></td><td>3.62 <b>(+231.15%)</b></td><td>1.66 (-13.09%)</td><td>1158.00 <b>(-69.80%)</b></td><td>720.20 <b>(-57.77%)</b></td><td>641.60 <b>(-38.84%)</b></td><td>543.80 <b>(-24.15%)</b></td><td>253.84 <b>(-80.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.85 (n/a)</td><td>3.52 (n/a)</td><td>4.00 (n/a)</td><td>1.09 (n/a)</td><td>1.91 (n/a)</td><td>3834.60 (n/a)</td><td>1705.62 (n/a)</td><td>1049.00 (n/a)</td><td>716.90 (n/a)</td><td>1289.07 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>9.56 (-4.91%)</td><td>5.53 (+5.92%)</td><td>4.08 <b>(-23.19%)</b></td><td>1.74 <b>(+38.56%)</b></td><td>3.35 (+4.46%)</td><td>2408.70 <b>(-27.83%)</b></td><td>1098.00 (-13.94%)</td><td>1028.90 <b>(+30.19%)</b></td><td>438.60 (+5.15%)</td><td>794.56 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>10.06 (n/a)</td><td>5.22 (n/a)</td><td>5.31 (n/a)</td><td>1.26 (n/a)</td><td>3.21 (n/a)</td><td>3337.60 (n/a)</td><td>1275.90 (n/a)</td><td>790.30 (n/a)</td><td>417.10 (n/a)</td><td>1176.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>8.77 (-6.12%)</td><td>6.77 <b>(+38.88%)</b></td><td>7.66 <b>(+95.26%)</b></td><td>3.21 <b>(+180.58%)</b></td><td>2.14 <b>(-40.82%)</b></td><td>1304.80 <b>(-64.36%)</b></td><td>704.24 <b>(-54.88%)</b></td><td>547.60 <b>(-48.78%)</b></td><td>478.50 (+6.52%)</td><td>341.08 <b>(-74.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>9.34 (n/a)</td><td>4.87 (n/a)</td><td>3.92 (n/a)</td><td>1.15 (n/a)</td><td>3.62 (n/a)</td><td>3660.90 (n/a)</td><td>1560.74 (n/a)</td><td>1069.20 (n/a)</td><td>449.20 (n/a)</td><td>1345.86 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>9.70 (+1.04%)</td><td>5.77 <b>(-26.35%)</b></td><td>4.85 <b>(-29.23%)</b></td><td>1.72 <b>(-73.64%)</b></td><td>3.11 <b>(+102.51%)</b></td><td>2444.90 <b>(+279.41%)</b></td><td>1034.86 <b>(+87.71%)</b></td><td>865.00 <b>(+41.32%)</b></td><td>432.30 (-1.03%)</td><td>814.58 <b>(+703.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>9.60 (n/a)</td><td>7.83 (n/a)</td><td>6.85 (n/a)</td><td>6.51 (n/a)</td><td>1.54 (n/a)</td><td>644.40 (n/a)</td><td>551.30 (n/a)</td><td>612.10 (n/a)</td><td>436.80 (n/a)</td><td>101.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.91 (-0.10%)</td><td>1.25 (+3.78%)</td><td>0.98 <b>(-25.69%)</b></td><td>0.88 <b>(+42.17%)</b></td><td>0.47 (-16.13%)</td><td>598.80 <b>(-29.67%)</b></td><td>461.86 (-12.62%)</td><td>536.50 <b>(+34.56%)</b></td><td>275.20 (+0.11%)</td><td>148.48 <b>(-43.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.91 (n/a)</td><td>1.21 (n/a)</td><td>1.32 (n/a)</td><td>0.62 (n/a)</td><td>0.56 (n/a)</td><td>851.40 (n/a)</td><td>528.56 (n/a)</td><td>398.70 (n/a)</td><td>274.90 (n/a)</td><td>264.57 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.86 (+0.89%)</td><td>2.05 (+12.59%)</td><td>2.41 <b>(+33.66%)</b></td><td>0.29 (-2.67%)</td><td>1.02 (+5.26%)</td><td>3618.70 (+2.74%)</td><td>1063.82 (-3.41%)</td><td>436.00 <b>(-25.18%)</b></td><td>366.70 (-0.89%)</td><td>1428.88 (+5.31%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.83 (n/a)</td><td>1.82 (n/a)</td><td>1.80 (n/a)</td><td>0.30 (n/a)</td><td>0.97 (n/a)</td><td>3522.20 (n/a)</td><td>1101.38 (n/a)</td><td>582.70 (n/a)</td><td>370.00 (n/a)</td><td>1356.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.08 <b>(+48.89%)</b></td><td>1.75 (+10.67%)</td><td>0.59 <b>(-40.69%)</b></td><td>0.57 (-4.16%)</td><td>1.66 <b>(+55.88%)</b></td><td>3670.90 (+4.34%)</td><td>2409.28 <b>(+25.56%)</b></td><td>3564.00 <b>(+68.60%)</b></td><td>514.10 <b>(-32.83%)</b></td><td>1642.23 <b>(+39.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.74 (n/a)</td><td>1.59 (n/a)</td><td>0.99 (n/a)</td><td>0.60 (n/a)</td><td>1.06 (n/a)</td><td>3518.10 (n/a)</td><td>1918.76 (n/a)</td><td>2113.90 (n/a)</td><td>765.40 (n/a)</td><td>1174.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.21 <b>(+112.04%)</b></td><td>1.05 <b>(+49.58%)</b></td><td>0.95 <b>(+41.32%)</b></td><td>0.26 <b>(+20.93%)</b></td><td>0.71 <b>(+117.27%)</b></td><td>1997.10 (-17.30%)</td><td>791.32 <b>(-22.45%)</b></td><td>552.10 <b>(-29.25%)</b></td><td>237.60 <b>(-52.85%)</b></td><td>692.13 (-12.88%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.04 (n/a)</td><td>0.70 (n/a)</td><td>0.67 (n/a)</td><td>0.22 (n/a)</td><td>0.33 (n/a)</td><td>2415.00 (n/a)</td><td>1020.44 (n/a)</td><td>780.30 (n/a)</td><td>503.90 (n/a)</td><td>794.45 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (+10.22%)</td><td>0.09 (-15.15%)</td><td>0.08 <b>(-27.34%)</b></td><td>0.05 <b>(-22.76%)</b></td><td>0.04 <b>(+54.82%)</b></td><td>601.60 <b>(+29.46%)</b></td><td>411.62 <b>(+26.65%)</b></td><td>415.20 <b>(+37.62%)</b></td><td>232.30 (-9.26%)</td><td>149.17 <b>(+77.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>464.70 (n/a)</td><td>325.00 (n/a)</td><td>301.70 (n/a)</td><td>256.00 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (-11.61%)</td><td>0.07 (+4.13%)</td><td>0.06 (+5.91%)</td><td>0.06 (+5.35%)</td><td>0.01 <b>(-27.61%)</b></td><td>573.40 (-5.07%)</td><td>466.24 (-6.31%)</td><td>506.80 (-5.59%)</td><td>354.80 (+13.14%)</td><td>91.45 <b>(-22.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>604.00 (n/a)</td><td>497.62 (n/a)</td><td>536.80 (n/a)</td><td>313.60 (n/a)</td><td>118.62 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.25 <b>(-30.00%)</b></td><td>0.19 (-10.57%)</td><td>0.22 <b>(+26.05%)</b></td><td>0.11 (-7.37%)</td><td>0.06 <b>(-36.27%)</b></td><td>618.60 (+7.96%)</td><td>396.34 (+5.67%)</td><td>298.30 <b>(-20.66%)</b></td><td>261.30 <b>(+42.86%)</b></td><td>158.16 (-1.27%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>573.00 (n/a)</td><td>375.08 (n/a)</td><td>376.00 (n/a)</td><td>182.90 (n/a)</td><td>160.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.27 (-19.67%)</td><td>0.19 (-8.54%)</td><td>0.15 (-11.76%)</td><td>0.11 <b>(-22.89%)</b></td><td>0.08 (-6.18%)</td><td>617.90 <b>(+29.67%)</b></td><td>406.62 (+12.85%)</td><td>433.80 (+13.32%)</td><td>238.80 <b>(+24.50%)</b></td><td>164.89 <b>(+37.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.34 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>476.50 (n/a)</td><td>360.32 (n/a)</td><td>382.80 (n/a)</td><td>191.80 (n/a)</td><td>120.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 <b>(-51.97%)</b></td><td>0.15 (-17.05%)</td><td>0.15 (+14.99%)</td><td>0.11 (+11.83%)</td><td>0.02 <b>(-77.40%)</b></td><td>576.00 (-10.57%)</td><td>459.98 (+1.89%)</td><td>437.00 (-13.03%)</td><td>387.70 <b>(+108.22%)</b></td><td>78.21 <b>(-55.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>644.10 (n/a)</td><td>451.46 (n/a)</td><td>502.50 (n/a)</td><td>186.20 (n/a)</td><td>176.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.57 (-0.73%)</td><td>0.37 (-15.75%)</td><td>0.32 <b>(-34.14%)</b></td><td>0.26 <b>(+26.28%)</b></td><td>0.13 (-11.60%)</td><td>504.70 <b>(-20.82%)</b></td><td>378.26 (+12.21%)</td><td>410.10 <b>(+51.83%)</b></td><td>229.10 (+0.75%)</td><td>109.25 <b>(-35.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>637.40 (n/a)</td><td>337.10 (n/a)</td><td>270.10 (n/a)</td><td>227.40 (n/a)</td><td>169.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.50 <b>(+63.72%)</b></td><td>0.34 <b>(+32.37%)</b></td><td>0.32 <b>(+31.46%)</b></td><td>0.21 (-3.56%)</td><td>0.12 <b>(+239.29%)</b></td><td>634.00 (+3.70%)</td><td>433.40 (-17.16%)</td><td>414.20 <b>(-23.93%)</b></td><td>262.40 <b>(-38.92%)</b></td><td>155.91 <b>(+117.17%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>611.40 (n/a)</td><td>523.18 (n/a)</td><td>544.50 (n/a)</td><td>429.60 (n/a)</td><td>71.79 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.37 <b>(+31.13%)</b></td><td>0.26 (-2.50%)</td><td>0.23 (-12.26%)</td><td>0.19 (-19.76%)</td><td>0.07 <b>(+334.87%)</b></td><td>677.80 <b>(+24.62%)</b></td><td>535.00 (+7.64%)</td><td>565.80 (+13.98%)</td><td>350.40 <b>(-23.74%)</b></td><td>124.54 <b>(+299.84%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>543.90 (n/a)</td><td>497.04 (n/a)</td><td>496.40 (n/a)</td><td>459.50 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 <b>(+36.97%)</b></td><td>0.06 <b>(+54.24%)</b></td><td>0.06 <b>(+67.38%)</b></td><td>0.05 <b>(+64.13%)</b></td><td>0.01 (+10.95%)</td><td>334.90 <b>(-39.08%)</b></td><td>268.78 <b>(-36.34%)</b></td><td>255.00 <b>(-40.25%)</b></td><td>210.70 <b>(-26.99%)</b></td><td>48.00 <b>(-48.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.70 (n/a)</td><td>422.20 (n/a)</td><td>426.80 (n/a)</td><td>288.60 (n/a)</td><td>93.73 (n/a)</td>
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
