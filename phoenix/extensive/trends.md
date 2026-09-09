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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (+2.81%)</td><td>0.02 (-12.36%)</td><td>0.02 (-0.17%)</td><td>0.01 <b>(-37.36%)</b></td><td>0.01 <b>(+225.83%)</b></td><td>485.00 <b>(+59.64%)</b></td><td>337.24 <b>(+25.94%)</b></td><td>271.10 (+0.15%)</td><td>230.20 (-2.75%)</td><td>126.00 <b>(+413.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>303.80 (n/a)</td><td>267.78 (n/a)</td><td>270.70 (n/a)</td><td>236.70 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(-36.60%)</b></td><td>0.01 <b>(-34.60%)</b></td><td>0.01 <b>(-43.63%)</b></td><td>0.01 (-12.46%)</td><td>0.00 <b>(-69.17%)</b></td><td>554.10 (+14.22%)</td><td>467.46 <b>(+39.89%)</b></td><td>464.70 <b>(+77.43%)</b></td><td>364.50 <b>(+57.72%)</b></td><td>68.40 <b>(-46.00%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>334.16 (n/a)</td><td>261.90 (n/a)</td><td>231.10 (n/a)</td><td>126.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (+15.38%)</td><td>0.02 <b>(+63.13%)</b></td><td>0.02 <b>(+118.60%)</b></td><td>0.01 <b>(+32.13%)</b></td><td>0.01 (-10.49%)</td><td>439.60 <b>(-24.32%)</b></td><td>279.94 <b>(-41.41%)</b></td><td>250.90 <b>(-54.25%)</b></td><td>208.10 (-13.33%)</td><td>91.24 <b>(-35.65%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.90 (n/a)</td><td>477.82 (n/a)</td><td>548.40 (n/a)</td><td>240.10 (n/a)</td><td>141.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(-22.41%)</b></td><td>0.02 (-10.32%)</td><td>0.02 (+11.78%)</td><td>0.01 (-14.91%)</td><td>0.01 <b>(-24.80%)</b></td><td>575.90 (+17.51%)</td><td>386.70 (+8.05%)</td><td>386.60 (-10.53%)</td><td>237.40 <b>(+28.88%)</b></td><td>149.65 (+5.88%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>490.10 (n/a)</td><td>357.88 (n/a)</td><td>432.10 (n/a)</td><td>184.20 (n/a)</td><td>141.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(+23.21%)</b></td><td>0.02 <b>(+40.22%)</b></td><td>0.02 <b>(+77.65%)</b></td><td>0.02 <b>(+51.01%)</b></td><td>0.00 <b>(-21.98%)</b></td><td>392.30 <b>(-33.79%)</b></td><td>284.88 <b>(-32.88%)</b></td><td>264.90 <b>(-43.72%)</b></td><td>226.00 (-18.82%)</td><td>65.00 <b>(-53.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.50 (n/a)</td><td>424.44 (n/a)</td><td>470.70 (n/a)</td><td>278.40 (n/a)</td><td>140.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (+1.82%)</td><td>0.02 <b>(-33.97%)</b></td><td>0.01 <b>(-44.73%)</b></td><td>0.01 <b>(-43.38%)</b></td><td>0.01 <b>(+245.42%)</b></td><td>495.70 <b>(+76.66%)</b></td><td>432.94 <b>(+64.64%)</b></td><td>484.30 <b>(+80.91%)</b></td><td>230.80 (-1.79%)</td><td>113.69 <b>(+484.28%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>280.60 (n/a)</td><td>262.96 (n/a)</td><td>267.70 (n/a)</td><td>235.00 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+45.68%)</b></td><td>0.04 <b>(+96.25%)</b></td><td>0.05 <b>(+121.60%)</b></td><td>0.02 <b>(+220.67%)</b></td><td>0.01 <b>(+24.50%)</b></td><td>572.30 <b>(-68.82%)</b></td><td>322.30 <b>(-58.28%)</b></td><td>262.30 <b>(-54.88%)</b></td><td>229.40 <b>(-31.36%)</b></td><td>144.02 <b>(-76.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1835.30 (n/a)</td><td>772.50 (n/a)</td><td>581.30 (n/a)</td><td>334.20 (n/a)</td><td>602.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (+18.64%)</td><td>0.05 <b>(+22.07%)</b></td><td>0.05 <b>(+28.03%)</b></td><td>0.03 (+8.66%)</td><td>0.01 (+11.80%)</td><td>392.70 (-7.99%)</td><td>275.40 (-18.11%)</td><td>242.00 <b>(-21.91%)</b></td><td>224.30 (-15.71%)</td><td>68.34 (-10.89%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>426.80 (n/a)</td><td>336.32 (n/a)</td><td>309.90 (n/a)</td><td>266.10 (n/a)</td><td>76.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (-17.59%)</td><td>0.04 (+2.19%)</td><td>0.05 (+8.79%)</td><td>0.02 (-3.47%)</td><td>0.01 <b>(-27.54%)</b></td><td>512.00 (+3.58%)</td><td>299.46 (-5.79%)</td><td>245.10 (-8.10%)</td><td>233.00 <b>(+21.35%)</b></td><td>119.43 (-7.36%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>494.30 (n/a)</td><td>317.88 (n/a)</td><td>266.70 (n/a)</td><td>192.00 (n/a)</td><td>128.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (+9.64%)</td><td>0.04 (+13.22%)</td><td>0.04 <b>(+38.23%)</b></td><td>0.02 (+10.53%)</td><td>0.01 (-1.74%)</td><td>532.10 (-9.52%)</td><td>367.46 (-13.14%)</td><td>316.30 <b>(-27.67%)</b></td><td>242.80 (-8.79%)</td><td>125.14 (-14.74%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.10 (n/a)</td><td>423.06 (n/a)</td><td>437.30 (n/a)</td><td>266.20 (n/a)</td><td>146.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 <b>(+40.61%)</b></td><td>0.03 (-19.71%)</td><td>0.02 <b>(-52.83%)</b></td><td>0.01 <b>(-64.34%)</b></td><td>0.02 <b>(+125.58%)</b></td><td>1275.30 <b>(+180.47%)</b></td><td>608.16 <b>(+76.33%)</b></td><td>605.40 <b>(+111.97%)</b></td><td>176.30 <b>(-28.88%)</b></td><td>414.54 <b>(+309.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>454.70 (n/a)</td><td>344.90 (n/a)</td><td>285.60 (n/a)</td><td>247.90 (n/a)</td><td>101.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (-3.54%)</td><td>0.03 (+1.20%)</td><td>0.03 (-2.74%)</td><td>0.02 (-18.80%)</td><td>0.02 (+7.37%)</td><td>643.00 <b>(+23.16%)</b></td><td>437.84 (+4.75%)</td><td>453.70 (+2.83%)</td><td>212.70 (+3.65%)</td><td>183.97 <b>(+48.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>522.10 (n/a)</td><td>417.98 (n/a)</td><td>441.20 (n/a)</td><td>205.20 (n/a)</td><td>123.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (-1.20%)</td><td>0.06 (-3.80%)</td><td>0.06 (+11.72%)</td><td>0.04 (-8.18%)</td><td>0.02 (-8.00%)</td><td>594.80 (+8.90%)</td><td>422.00 (+3.34%)</td><td>422.80 (-10.48%)</td><td>251.60 (+1.21%)</td><td>146.43 (+4.41%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>546.20 (n/a)</td><td>408.38 (n/a)</td><td>472.30 (n/a)</td><td>248.60 (n/a)</td><td>140.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (+2.50%)</td><td>0.09 (+18.95%)</td><td>0.09 (+16.08%)</td><td>0.06 <b>(+27.06%)</b></td><td>0.02 (-16.78%)</td><td>410.30 <b>(-21.29%)</b></td><td>283.28 (-18.77%)</td><td>259.10 (-13.83%)</td><td>234.10 (-2.42%)</td><td>73.03 <b>(-35.80%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.30 (n/a)</td><td>348.72 (n/a)</td><td>300.70 (n/a)</td><td>239.90 (n/a)</td><td>113.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (-9.04%)</td><td>0.06 (-2.54%)</td><td>0.06 <b>(+25.35%)</b></td><td>0.05 (+10.31%)</td><td>0.02 <b>(-28.54%)</b></td><td>527.80 (-9.33%)</td><td>409.38 (-3.99%)</td><td>392.00 <b>(-20.23%)</b></td><td>249.10 (+9.93%)</td><td>110.56 <b>(-29.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>582.10 (n/a)</td><td>426.40 (n/a)</td><td>491.40 (n/a)</td><td>226.60 (n/a)</td><td>157.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 <b>(+44.74%)</b></td><td>0.09 (+14.34%)</td><td>0.08 (-0.50%)</td><td>0.04 (-8.86%)</td><td>0.04 <b>(+63.43%)</b></td><td>561.50 (+9.73%)</td><td>336.78 (-6.10%)</td><td>297.80 (+0.51%)</td><td>163.90 <b>(-30.90%)</b></td><td>150.70 (+18.50%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>511.70 (n/a)</td><td>358.66 (n/a)</td><td>296.30 (n/a)</td><td>237.20 (n/a)</td><td>127.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(+25.57%)</b></td><td>0.06 <b>(+43.79%)</b></td><td>0.06 <b>(+54.01%)</b></td><td>0.04 <b>(+149.93%)</b></td><td>0.02 (-9.80%)</td><td>585.70 <b>(-59.98%)</b></td><td>429.80 <b>(-40.03%)</b></td><td>393.30 <b>(-35.07%)</b></td><td>296.00 <b>(-20.37%)</b></td><td>114.96 <b>(-73.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1463.70 (n/a)</td><td>716.74 (n/a)</td><td>605.70 (n/a)</td><td>371.70 (n/a)</td><td>429.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (-3.37%)</td><td>0.05 (-19.92%)</td><td>0.05 (+11.94%)</td><td>0.01 <b>(-69.13%)</b></td><td>0.03 (+16.07%)</td><td>1839.50 <b>(+223.97%)</b></td><td>719.32 <b>(+71.06%)</b></td><td>447.10 (-10.67%)</td><td>249.80 (+3.48%)</td><td>642.11 <b>(+330.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>567.80 (n/a)</td><td>420.50 (n/a)</td><td>500.50 (n/a)</td><td>241.40 (n/a)</td><td>149.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.20 (+6.65%)</td><td>0.14 (+5.66%)</td><td>0.15 <b>(+38.46%)</b></td><td>0.10 (+1.55%)</td><td>0.04 (-13.52%)</td><td>482.00 (-1.53%)</td><td>359.32 (-7.30%)</td><td>327.20 <b>(-27.77%)</b></td><td>249.70 (-6.23%)</td><td>89.77 (-17.13%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>489.50 (n/a)</td><td>387.62 (n/a)</td><td>453.00 (n/a)</td><td>266.30 (n/a)</td><td>108.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 <b>(+28.80%)</b></td><td>0.15 <b>(+36.77%)</b></td><td>0.16 <b>(+45.94%)</b></td><td>0.12 <b>(+24.51%)</b></td><td>0.02 <b>(+61.25%)</b></td><td>427.20 (-19.67%)</td><td>341.68 <b>(-26.24%)</b></td><td>303.10 <b>(-31.49%)</b></td><td>294.10 <b>(-22.36%)</b></td><td>62.03 (-3.39%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>531.80 (n/a)</td><td>463.22 (n/a)</td><td>442.40 (n/a)</td><td>378.80 (n/a)</td><td>64.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.23 (+9.75%)</td><td>0.15 (+14.60%)</td><td>0.12 <b>(-23.04%)</b></td><td>0.09 <b>(+254.90%)</b></td><td>0.06 <b>(-22.47%)</b></td><td>534.90 <b>(-71.83%)</b></td><td>359.36 <b>(-45.42%)</b></td><td>393.40 <b>(+29.96%)</b></td><td>211.20 (-8.89%)</td><td>133.99 <b>(-81.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1898.50 (n/a)</td><td>658.36 (n/a)</td><td>302.70 (n/a)</td><td>231.80 (n/a)</td><td>709.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.21 (-5.81%)</td><td>0.16 <b>(+24.99%)</b></td><td>0.18 <b>(+67.45%)</b></td><td>0.08 (+10.82%)</td><td>0.05 (-3.06%)</td><td>583.00 (-9.77%)</td><td>349.06 <b>(-20.24%)</b></td><td>274.00 <b>(-40.28%)</b></td><td>233.90 (+6.17%)</td><td>148.79 (-3.32%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>646.10 (n/a)</td><td>437.66 (n/a)</td><td>458.80 (n/a)</td><td>220.30 (n/a)</td><td>153.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 (-0.94%)</td><td>0.14 (+1.81%)</td><td>0.12 (-0.00%)</td><td>0.10 (+11.30%)</td><td>0.04 (-16.83%)</td><td>479.30 (-10.16%)</td><td>372.50 (-4.77%)</td><td>408.90 (+0.02%)</td><td>256.40 (+0.94%)</td><td>93.39 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>533.50 (n/a)</td><td>391.14 (n/a)</td><td>408.80 (n/a)</td><td>254.00 (n/a)</td><td>123.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 <b>(-43.41%)</b></td><td>0.10 <b>(-23.76%)</b></td><td>0.10 (-12.90%)</td><td>0.08 (-17.54%)</td><td>0.01 <b>(-72.65%)</b></td><td>582.20 <b>(+21.27%)</b></td><td>501.18 <b>(+24.09%)</b></td><td>500.70 (+14.81%)</td><td>415.80 <b>(+76.71%)</b></td><td>58.96 <b>(-38.90%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>480.10 (n/a)</td><td>403.90 (n/a)</td><td>436.10 (n/a)</td><td>235.30 (n/a)</td><td>96.49 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-0.52%)</td><td>0.01 (-17.33%)</td><td>0.01 <b>(-28.06%)</b></td><td>0.01 (-18.46%)</td><td>0.00 <b>(+51.12%)</b></td><td>512.10 <b>(+22.63%)</b></td><td>391.82 <b>(+27.26%)</b></td><td>407.50 <b>(+38.98%)</b></td><td>246.80 (+0.53%)</td><td>117.44 <b>(+81.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>417.60 (n/a)</td><td>307.90 (n/a)</td><td>293.20 (n/a)</td><td>245.50 (n/a)</td><td>64.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-6.53%)</td><td>0.01 <b>(-21.01%)</b></td><td>0.01 <b>(-34.42%)</b></td><td>0.00 (-4.44%)</td><td>0.00 (+5.83%)</td><td>527.00 (+4.65%)</td><td>401.52 <b>(+28.92%)</b></td><td>445.90 <b>(+52.50%)</b></td><td>241.70 (+6.99%)</td><td>129.11 (+15.65%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.60 (n/a)</td><td>311.44 (n/a)</td><td>292.40 (n/a)</td><td>225.90 (n/a)</td><td>111.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(+33.79%)</b></td><td>0.01 <b>(+61.48%)</b></td><td>0.01 <b>(+44.83%)</b></td><td>0.01 <b>(+116.83%)</b></td><td>0.00 <b>(-71.44%)</b></td><td>250.60 <b>(-53.89%)</b></td><td>238.28 <b>(-41.35%)</b></td><td>240.40 <b>(-30.96%)</b></td><td>221.90 <b>(-25.26%)</b></td><td>10.40 <b>(-90.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>543.50 (n/a)</td><td>406.26 (n/a)</td><td>348.20 (n/a)</td><td>296.90 (n/a)</td><td>109.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-12.78%)</td><td>0.01 (+7.43%)</td><td>0.01 <b>(+32.98%)</b></td><td>0.01 <b>(+29.57%)</b></td><td>0.00 <b>(-43.05%)</b></td><td>449.40 <b>(-22.81%)</b></td><td>333.02 (-14.32%)</td><td>295.10 <b>(-24.82%)</b></td><td>260.10 (+14.63%)</td><td>76.38 <b>(-47.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>582.20 (n/a)</td><td>388.68 (n/a)</td><td>392.50 (n/a)</td><td>226.90 (n/a)</td><td>146.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(+24.27%)</b></td><td>0.01 <b>(+20.56%)</b></td><td>0.01 <b>(+53.94%)</b></td><td>0.00 (-8.78%)</td><td>0.00 <b>(+77.97%)</b></td><td>622.70 (+9.63%)</td><td>397.00 (-6.76%)</td><td>284.80 <b>(-35.04%)</b></td><td>225.80 (-19.53%)</td><td>193.34 <b>(+68.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>568.00 (n/a)</td><td>425.78 (n/a)</td><td>438.40 (n/a)</td><td>280.60 (n/a)</td><td>114.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(-22.74%)</b></td><td>0.01 (-6.49%)</td><td>0.01 (+14.56%)</td><td>0.00 <b>(-43.75%)</b></td><td>0.00 <b>(-20.44%)</b></td><td>1063.30 <b>(+77.78%)</b></td><td>547.92 (+13.46%)</td><td>474.80 (-12.70%)</td><td>309.50 <b>(+29.44%)</b></td><td>297.51 <b>(+109.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>598.10 (n/a)</td><td>482.94 (n/a)</td><td>543.90 (n/a)</td><td>239.10 (n/a)</td><td>142.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+2.78%)</td><td>0.02 <b>(+27.70%)</b></td><td>0.02 <b>(+62.17%)</b></td><td>0.01 <b>(+106.55%)</b></td><td>0.00 <b>(-39.64%)</b></td><td>448.50 <b>(-51.58%)</b></td><td>327.00 <b>(-34.15%)</b></td><td>298.70 <b>(-38.34%)</b></td><td>236.30 (-2.72%)</td><td>79.63 <b>(-70.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>926.30 (n/a)</td><td>496.60 (n/a)</td><td>484.40 (n/a)</td><td>242.90 (n/a)</td><td>269.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+9.17%)</td><td>0.02 (+12.08%)</td><td>0.02 <b>(+23.17%)</b></td><td>0.01 (-16.78%)</td><td>0.01 <b>(+43.48%)</b></td><td>567.80 <b>(+20.17%)</b></td><td>310.88 (-4.70%)</td><td>237.70 (-18.79%)</td><td>227.90 (-8.40%)</td><td>145.74 <b>(+59.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.50 (n/a)</td><td>326.22 (n/a)</td><td>292.70 (n/a)</td><td>248.80 (n/a)</td><td>91.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (+2.97%)</td><td>0.02 <b>(-28.09%)</b></td><td>0.01 <b>(-51.05%)</b></td><td>0.01 <b>(-43.06%)</b></td><td>0.01 <b>(+60.13%)</b></td><td>837.30 <b>(+75.65%)</b></td><td>494.34 <b>(+79.29%)</b></td><td>473.70 <b>(+104.27%)</b></td><td>180.60 (-2.85%)</td><td>294.15 <b>(+155.67%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>476.70 (n/a)</td><td>275.72 (n/a)</td><td>231.90 (n/a)</td><td>185.90 (n/a)</td><td>115.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+10.91%)</td><td>0.02 (+18.22%)</td><td>0.02 <b>(+65.36%)</b></td><td>0.00 <b>(-77.26%)</b></td><td>0.01 <b>(+73.21%)</b></td><td>2413.80 <b>(+339.83%)</b></td><td>719.98 <b>(+62.84%)</b></td><td>291.90 <b>(-39.52%)</b></td><td>225.90 (-9.86%)</td><td>949.29 <b>(+664.26%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.80 (n/a)</td><td>442.14 (n/a)</td><td>482.60 (n/a)</td><td>250.60 (n/a)</td><td>124.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-18.12%)</td><td>0.01 <b>(-21.31%)</b></td><td>0.01 <b>(-36.45%)</b></td><td>0.01 (+3.33%)</td><td>0.01 <b>(-25.64%)</b></td><td>595.20 (-3.22%)</td><td>436.68 (+17.93%)</td><td>478.20 <b>(+57.35%)</b></td><td>210.80 <b>(+22.13%)</b></td><td>142.44 <b>(-21.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.00 (n/a)</td><td>370.30 (n/a)</td><td>303.90 (n/a)</td><td>172.60 (n/a)</td><td>180.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(-30.14%)</b></td><td>0.01 (-18.89%)</td><td>0.01 (-10.74%)</td><td>0.01 (+7.80%)</td><td>0.00 <b>(-51.74%)</b></td><td>608.40 (-7.23%)</td><td>479.40 (+13.55%)</td><td>464.20 (+12.04%)</td><td>372.90 <b>(+43.15%)</b></td><td>110.99 <b>(-33.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.80 (n/a)</td><td>422.18 (n/a)</td><td>414.30 (n/a)</td><td>260.50 (n/a)</td><td>166.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-14.02%)</td><td>0.02 <b>(-30.07%)</b></td><td>0.03 <b>(-25.84%)</b></td><td>0.01 <b>(-77.47%)</b></td><td>0.01 <b>(+63.44%)</b></td><td>2063.30 <b>(+343.91%)</b></td><td>729.84 <b>(+132.30%)</b></td><td>400.10 <b>(+34.85%)</b></td><td>262.60 (+16.30%)</td><td>759.05 <b>(+740.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.80 (n/a)</td><td>314.18 (n/a)</td><td>296.70 (n/a)</td><td>225.80 (n/a)</td><td>90.27 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-15.95%)</td><td>0.03 (+14.51%)</td><td>0.04 <b>(+57.07%)</b></td><td>0.02 <b>(+26.04%)</b></td><td>0.01 <b>(-24.25%)</b></td><td>477.30 <b>(-20.66%)</b></td><td>332.66 (-18.05%)</td><td>258.90 <b>(-36.34%)</b></td><td>245.10 (+18.98%)</td><td>113.06 <b>(-29.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.60 (n/a)</td><td>405.92 (n/a)</td><td>406.70 (n/a)</td><td>206.00 (n/a)</td><td>161.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+35.70%)</b></td><td>0.03 (+13.02%)</td><td>0.02 (-6.97%)</td><td>0.02 (-5.09%)</td><td>0.01 <b>(+106.06%)</b></td><td>599.20 (+5.36%)</td><td>431.84 (-1.99%)</td><td>491.00 (+7.49%)</td><td>218.80 <b>(-26.31%)</b></td><td>164.00 <b>(+67.36%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.70 (n/a)</td><td>440.62 (n/a)</td><td>456.80 (n/a)</td><td>296.90 (n/a)</td><td>98.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 <b>(+56.43%)</b></td><td>0.03 <b>(+32.60%)</b></td><td>0.02 (-11.64%)</td><td>0.02 (+17.34%)</td><td>0.02 <b>(+103.68%)</b></td><td>652.10 (-14.78%)</td><td>448.82 (-12.34%)</td><td>538.60 (+13.18%)</td><td>173.10 <b>(-36.08%)</b></td><td>214.76 (+19.48%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>765.20 (n/a)</td><td>512.00 (n/a)</td><td>475.90 (n/a)</td><td>270.80 (n/a)</td><td>179.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 <b>(+27.16%)</b></td><td>0.03 <b>(+24.37%)</b></td><td>0.03 (+12.11%)</td><td>0.02 (-0.17%)</td><td>0.01 <b>(+62.58%)</b></td><td>572.60 (+0.17%)</td><td>373.06 (-15.61%)</td><td>371.20 (-10.81%)</td><td>236.30 <b>(-21.36%)</b></td><td>134.59 <b>(+22.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.60 (n/a)</td><td>442.06 (n/a)</td><td>416.20 (n/a)</td><td>300.50 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(+43.72%)</b></td><td>0.02 (+9.29%)</td><td>0.02 (+7.86%)</td><td>0.00 <b>(-62.40%)</b></td><td>0.01 <b>(+188.58%)</b></td><td>2103.00 <b>(+165.97%)</b></td><td>792.42 <b>(+34.23%)</b></td><td>530.80 (-7.28%)</td><td>314.80 <b>(-30.42%)</b></td><td>739.53 <b>(+494.46%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>790.70 (n/a)</td><td>590.36 (n/a)</td><td>572.50 (n/a)</td><td>452.40 (n/a)</td><td>124.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (-7.78%)</td><td>0.06 (-12.11%)</td><td>0.04 <b>(-36.05%)</b></td><td>0.03 <b>(-22.61%)</b></td><td>0.02 (+4.27%)</td><td>705.80 <b>(+29.22%)</b></td><td>433.52 (+18.27%)</td><td>468.60 <b>(+56.36%)</b></td><td>239.90 (+8.45%)</td><td>186.43 <b>(+34.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.20 (n/a)</td><td>366.54 (n/a)</td><td>299.70 (n/a)</td><td>221.20 (n/a)</td><td>139.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-12.25%)</td><td>0.06 (+11.83%)</td><td>0.07 <b>(+63.37%)</b></td><td>0.04 (-7.27%)</td><td>0.02 <b>(-28.78%)</b></td><td>577.10 (+7.85%)</td><td>348.72 (-13.85%)</td><td>297.30 <b>(-38.80%)</b></td><td>275.10 (+13.96%)</td><td>128.13 (-7.69%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>535.10 (n/a)</td><td>404.78 (n/a)</td><td>485.80 (n/a)</td><td>241.40 (n/a)</td><td>138.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (-16.20%)</td><td>0.05 <b>(-30.99%)</b></td><td>0.04 <b>(-41.15%)</b></td><td>0.01 <b>(-69.59%)</b></td><td>0.03 (+4.96%)</td><td>1833.90 <b>(+228.89%)</b></td><td>706.96 <b>(+97.75%)</b></td><td>508.80 <b>(+69.94%)</b></td><td>240.80 (+19.33%)</td><td>641.41 <b>(+344.96%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>557.60 (n/a)</td><td>357.50 (n/a)</td><td>299.40 (n/a)</td><td>201.80 (n/a)</td><td>144.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+22.75%)</b></td><td>0.07 <b>(+38.58%)</b></td><td>0.07 <b>(+44.16%)</b></td><td>0.05 <b>(+138.90%)</b></td><td>0.02 <b>(-20.40%)</b></td><td>426.70 <b>(-58.15%)</b></td><td>327.08 <b>(-37.28%)</b></td><td>318.00 <b>(-30.64%)</b></td><td>242.60 (-18.54%)</td><td>76.30 <b>(-73.74%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1019.50 (n/a)</td><td>521.52 (n/a)</td><td>458.50 (n/a)</td><td>297.80 (n/a)</td><td>290.53 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+24.33%)</b></td><td>0.05 (+4.33%)</td><td>0.04 (-14.25%)</td><td>0.03 (-10.13%)</td><td>0.02 <b>(+62.66%)</b></td><td>644.80 (+11.27%)</td><td>480.98 (+2.63%)</td><td>555.00 (+16.62%)</td><td>243.90 (-19.58%)</td><td>163.70 <b>(+41.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>468.64 (n/a)</td><td>475.90 (n/a)</td><td>303.30 (n/a)</td><td>115.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (-8.04%)</td><td>0.06 (+13.61%)</td><td>0.04 (+5.31%)</td><td>0.03 (+2.17%)</td><td>0.03 (+4.15%)</td><td>627.70 (-2.12%)</td><td>432.02 (-9.79%)</td><td>495.10 (-5.04%)</td><td>236.30 (+8.74%)</td><td>180.96 (+11.22%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>641.30 (n/a)</td><td>478.90 (n/a)</td><td>521.40 (n/a)</td><td>217.30 (n/a)</td><td>162.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>398.80 (n/a)</td><td>285.86 (n/a)</td><td>264.50 (n/a)</td><td>243.90 (n/a)</td><td>64.53 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>451.10 (n/a)</td><td>312.16 (n/a)</td><td>298.70 (n/a)</td><td>223.40 (n/a)</td><td>91.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>534.00 (n/a)</td><td>406.76 (n/a)</td><td>492.30 (n/a)</td><td>233.30 (n/a)</td><td>152.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>321.00 (n/a)</td><td>282.70 (n/a)</td><td>227.80 (n/a)</td><td>109.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>483.30 (n/a)</td><td>353.16 (n/a)</td><td>326.70 (n/a)</td><td>225.40 (n/a)</td><td>111.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>577.60 (n/a)</td><td>408.48 (n/a)</td><td>438.60 (n/a)</td><td>247.90 (n/a)</td><td>146.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>659.20 (n/a)</td><td>383.06 (n/a)</td><td>294.00 (n/a)</td><td>196.90 (n/a)</td><td>188.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2501.80 (n/a)</td><td>885.68 (n/a)</td><td>554.20 (n/a)</td><td>399.90 (n/a)</td><td>906.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>506.00 (n/a)</td><td>377.88 (n/a)</td><td>351.70 (n/a)</td><td>259.60 (n/a)</td><td>106.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.22 (+19.67%)</td><td>0.17 <b>(+29.00%)</b></td><td>0.17 <b>(+42.20%)</b></td><td>0.10 (+18.60%)</td><td>0.04 (-7.67%)</td><td>471.30 (-15.69%)</td><td>305.94 <b>(-25.25%)</b></td><td>286.90 <b>(-29.66%)</b></td><td>219.20 (-16.46%)</td><td>96.77 <b>(-31.03%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>559.00 (n/a)</td><td>409.30 (n/a)</td><td>407.90 (n/a)</td><td>262.40 (n/a)</td><td>140.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>632.30 (n/a)</td><td>438.98 (n/a)</td><td>439.60 (n/a)</td><td>283.80 (n/a)</td><td>127.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>495.80 (n/a)</td><td>403.86 (n/a)</td><td>467.10 (n/a)</td><td>257.30 (n/a)</td><td>105.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>312.60 (n/a)</td><td>269.40 (n/a)</td><td>272.60 (n/a)</td><td>234.30 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2033.70 (n/a)</td><td>683.84 (n/a)</td><td>369.90 (n/a)</td><td>260.20 (n/a)</td><td>758.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.60 (n/a)</td><td>412.34 (n/a)</td><td>463.60 (n/a)</td><td>242.30 (n/a)</td><td>143.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>355.80 (n/a)</td><td>270.20 (n/a)</td><td>251.00 (n/a)</td><td>149.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.50 (n/a)</td><td>430.14 (n/a)</td><td>491.40 (n/a)</td><td>221.20 (n/a)</td><td>119.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>413.44 (n/a)</td><td>442.70 (n/a)</td><td>278.90 (n/a)</td><td>106.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>355.60 (n/a)</td><td>294.14 (n/a)</td><td>308.10 (n/a)</td><td>242.10 (n/a)</td><td>50.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.60 (n/a)</td><td>362.94 (n/a)</td><td>339.00 (n/a)</td><td>270.50 (n/a)</td><td>112.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>758.20 (n/a)</td><td>474.00 (n/a)</td><td>417.90 (n/a)</td><td>262.70 (n/a)</td><td>216.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>362.30 (n/a)</td><td>294.20 (n/a)</td><td>265.50 (n/a)</td><td>244.60 (n/a)</td><td>56.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>571.80 (n/a)</td><td>425.74 (n/a)</td><td>495.30 (n/a)</td><td>229.70 (n/a)</td><td>162.71 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1949.30 (n/a)</td><td>679.10 (n/a)</td><td>375.90 (n/a)</td><td>306.80 (n/a)</td><td>712.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>691.40 (n/a)</td><td>415.76 (n/a)</td><td>447.40 (n/a)</td><td>175.40 (n/a)</td><td>196.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.80 (n/a)</td><td>329.98 (n/a)</td><td>328.90 (n/a)</td><td>233.40 (n/a)</td><td>79.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.20 (n/a)</td><td>423.08 (n/a)</td><td>426.90 (n/a)</td><td>302.80 (n/a)</td><td>83.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.60 (n/a)</td><td>368.86 (n/a)</td><td>331.70 (n/a)</td><td>269.30 (n/a)</td><td>99.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.00 (n/a)</td><td>488.42 (n/a)</td><td>497.90 (n/a)</td><td>387.00 (n/a)</td><td>70.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.80 (n/a)</td><td>403.68 (n/a)</td><td>346.70 (n/a)</td><td>228.80 (n/a)</td><td>160.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.90 (n/a)</td><td>405.38 (n/a)</td><td>403.50 (n/a)</td><td>261.60 (n/a)</td><td>124.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.50 (n/a)</td><td>370.80 (n/a)</td><td>290.60 (n/a)</td><td>205.20 (n/a)</td><td>182.22 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.10 (n/a)</td><td>378.34 (n/a)</td><td>404.50 (n/a)</td><td>239.50 (n/a)</td><td>128.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>406.40 (n/a)</td><td>295.92 (n/a)</td><td>280.30 (n/a)</td><td>232.50 (n/a)</td><td>69.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.30 (n/a)</td><td>439.70 (n/a)</td><td>468.40 (n/a)</td><td>248.90 (n/a)</td><td>145.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>347.00 (n/a)</td><td>292.48 (n/a)</td><td>283.10 (n/a)</td><td>259.10 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>617.50 (n/a)</td><td>411.30 (n/a)</td><td>460.50 (n/a)</td><td>228.80 (n/a)</td><td>166.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>587.50 (n/a)</td><td>458.24 (n/a)</td><td>480.10 (n/a)</td><td>314.60 (n/a)</td><td>118.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2032.90 (n/a)</td><td>798.12 (n/a)</td><td>565.30 (n/a)</td><td>282.60 (n/a)</td><td>700.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>340.98 (n/a)</td><td>316.80 (n/a)</td><td>235.40 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.60 (n/a)</td><td>412.82 (n/a)</td><td>464.60 (n/a)</td><td>218.10 (n/a)</td><td>130.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>782.80 (n/a)</td><td>472.30 (n/a)</td><td>326.80 (n/a)</td><td>256.70 (n/a)</td><td>258.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>520.30 (n/a)</td><td>368.70 (n/a)</td><td>379.00 (n/a)</td><td>228.00 (n/a)</td><td>125.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>635.80 (n/a)</td><td>435.04 (n/a)</td><td>516.60 (n/a)</td><td>229.20 (n/a)</td><td>175.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>602.10 (n/a)</td><td>424.34 (n/a)</td><td>470.20 (n/a)</td><td>245.80 (n/a)</td><td>157.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2039.70 (n/a)</td><td>1087.40 (n/a)</td><td>477.10 (n/a)</td><td>438.00 (n/a)</td><td>855.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>627.70 (n/a)</td><td>453.20 (n/a)</td><td>423.40 (n/a)</td><td>311.40 (n/a)</td><td>150.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.57 <b>(+22.91%)</b></td><td>0.38 (-0.35%)</td><td>0.34 <b>(-21.32%)</b></td><td>0.16 <b>(-23.87%)</b></td><td>0.16 <b>(+58.29%)</b></td><td>1353.90 <b>(+31.34%)</b></td><td>697.76 (+12.12%)</td><td>650.90 <b>(+27.10%)</b></td><td>391.10 (-18.64%)</td><td>388.63 <b>(+66.18%)</b></td><td>24.13 <b>(+22.91%)</b></td><td>16.41 (-0.35%)</td><td>14.50 <b>(-21.32%)</b></td><td>6.97 <b>(-23.87%)</b></td><td>6.97 <b>(+58.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>1030.80 (n/a)</td><td>622.32 (n/a)</td><td>512.10 (n/a)</td><td>480.70 (n/a)</td><td>233.85 (n/a)</td><td>19.63 (n/a)</td><td>16.47 (n/a)</td><td>18.43 (n/a)</td><td>9.16 (n/a)</td><td>4.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.51 (-6.63%)</td><td>0.37 (-19.38%)</td><td>0.38 (-16.77%)</td><td>0.23 <b>(-37.37%)</b></td><td>0.10 <b>(+50.44%)</b></td><td>972.70 <b>(+59.67%)</b></td><td>636.08 <b>(+30.46%)</b></td><td>577.70 <b>(+20.15%)</b></td><td>431.60 (+7.10%)</td><td>201.64 <b>(+164.33%)</b></td><td>21.86 (-6.63%)</td><td>15.89 (-19.38%)</td><td>16.34 (-16.77%)</td><td>9.70 <b>(-37.37%)</b></td><td>4.33 <b>(+50.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>609.20 (n/a)</td><td>487.56 (n/a)</td><td>480.80 (n/a)</td><td>403.00 (n/a)</td><td>76.28 (n/a)</td><td>23.42 (n/a)</td><td>19.71 (n/a)</td><td>19.63 (n/a)</td><td>15.49 (n/a)</td><td>2.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (-0.94%)</td><td>0.31 (+0.95%)</td><td>0.31 (+1.82%)</td><td>0.30 (+1.30%)</td><td>0.00 <b>(-45.48%)</b></td><td>83382.00 (-1.29%)</td><td>82388.52 (-0.96%)</td><td>82281.60 (-1.79%)</td><td>81604.50 (+0.95%)</td><td>798.88 <b>(-45.67%)</b></td><td>210.53 (-0.94%)</td><td>208.54 (+0.95%)</td><td>208.79 (+1.82%)</td><td>206.04 (+1.30%)</td><td>2.02 <b>(-45.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84467.50 (n/a)</td><td>83188.90 (n/a)</td><td>83781.20 (n/a)</td><td>80839.70 (n/a)</td><td>1470.52 (n/a)</td><td>212.52 (n/a)</td><td>206.57 (n/a)</td><td>205.06 (n/a)</td><td>203.39 (n/a)</td><td>3.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.02 (-0.67%)</td><td>1.00 (-0.41%)</td><td>1.00 (-0.80%)</td><td>0.97 (+2.15%)</td><td>0.02 <b>(-26.35%)</b></td><td>26054.10 (-2.10%)</td><td>25240.78 (+0.37%)</td><td>25098.40 (+0.81%)</td><td>24610.20 (+0.68%)</td><td>606.08 <b>(-28.01%)</b></td><td>698.08 (-0.67%)</td><td>680.95 (-0.41%)</td><td>684.50 (-0.80%)</td><td>659.39 (+2.15%)</td><td>16.24 <b>(-26.35%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.95 (n/a)</td><td>0.03 (n/a)</td><td>26613.40 (n/a)</td><td>25148.40 (n/a)</td><td>24896.80 (n/a)</td><td>24444.30 (n/a)</td><td>841.95 (n/a)</td><td>702.82 (n/a)</td><td>683.73 (n/a)</td><td>690.04 (n/a)</td><td>645.53 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.82 (-0.22%)</td><td>0.81 (+1.40%)</td><td>0.81 (+0.69%)</td><td>0.80 (+3.99%)</td><td>0.01 <b>(-59.92%)</b></td><td>94035.80 (-3.84%)</td><td>92786.72 (-1.43%)</td><td>92665.80 (-0.68%)</td><td>91630.00 (+0.22%)</td><td>965.48 <b>(-61.43%)</b></td><td>749.97 (-0.22%)</td><td>740.68 (+1.40%)</td><td>741.58 (+0.69%)</td><td>730.78 (+3.99%)</td><td>7.70 <b>(-59.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.77 (n/a)</td><td>0.02 (n/a)</td><td>97789.70 (n/a)</td><td>94129.70 (n/a)</td><td>93302.50 (n/a)</td><td>91432.40 (n/a)</td><td>2503.19 (n/a)</td><td>751.59 (n/a)</td><td>730.46 (n/a)</td><td>736.52 (n/a)</td><td>702.73 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.77 (-0.97%)</td><td>0.76 (-0.21%)</td><td>0.76 (-0.46%)</td><td>0.75 (+0.05%)</td><td>0.01 <b>(-40.40%)</b></td><td>100161.10 (-0.05%)</td><td>99062.94 (+0.20%)</td><td>99135.80 (+0.47%)</td><td>97918.70 (+0.98%)</td><td>803.87 <b>(-39.97%)</b></td><td>701.80 (-0.97%)</td><td>693.73 (-0.21%)</td><td>693.18 (-0.46%)</td><td>686.09 (+0.05%)</td><td>5.63 <b>(-40.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100206.20 (n/a)</td><td>98862.76 (n/a)</td><td>98675.60 (n/a)</td><td>96971.60 (n/a)</td><td>1339.17 (n/a)</td><td>708.66 (n/a)</td><td>695.20 (n/a)</td><td>696.42 (n/a)</td><td>685.78 (n/a)</td><td>9.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.80 (+0.13%)</td><td>0.80 (+0.25%)</td><td>0.80 (-0.11%)</td><td>0.79 (+1.17%)</td><td>0.01 <b>(-36.31%)</b></td><td>95719.10 (-1.15%)</td><td>94883.72 (-0.26%)</td><td>94812.20 (+0.11%)</td><td>94189.40 (-0.13%)</td><td>658.37 <b>(-37.15%)</b></td><td>729.59 (+0.13%)</td><td>724.28 (+0.25%)</td><td>724.80 (-0.11%)</td><td>717.93 (+1.17%)</td><td>5.02 <b>(-36.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96836.70 (n/a)</td><td>95128.98 (n/a)</td><td>94704.00 (n/a)</td><td>94309.70 (n/a)</td><td>1047.58 (n/a)</td><td>728.66 (n/a)</td><td>722.45 (n/a)</td><td>725.62 (n/a)</td><td>709.64 (n/a)</td><td>7.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.35 (-6.53%)</td><td>3.60 (-16.63%)</td><td>3.47 <b>(-33.85%)</b></td><td>2.17 (-2.49%)</td><td>1.23 <b>(-23.90%)</b></td><td>4104.20 (+2.55%)</td><td>2722.28 (+14.20%)</td><td>2566.10 <b>(+51.17%)</b></td><td>1667.10 (+6.98%)</td><td>947.21 (-13.24%)</td><td>322.03 (-6.53%)</td><td>217.05 (-16.63%)</td><td>209.21 <b>(-33.85%)</b></td><td>130.81 (-2.49%)</td><td>74.11 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.72 (n/a)</td><td>4.32 (n/a)</td><td>5.25 (n/a)</td><td>2.23 (n/a)</td><td>1.62 (n/a)</td><td>4002.10 (n/a)</td><td>2383.88 (n/a)</td><td>1697.50 (n/a)</td><td>1558.30 (n/a)</td><td>1091.70 (n/a)</td><td>344.52 (n/a)</td><td>260.36 (n/a)</td><td>316.28 (n/a)</td><td>134.15 (n/a)</td><td>97.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.82 <b>(+77.82%)</b></td><td>3.83 <b>(+68.56%)</b></td><td>4.27 <b>(+95.19%)</b></td><td>2.08 (+1.88%)</td><td>1.15 <b>(+344.78%)</b></td><td>4291.30 (-1.84%)</td><td>2569.66 <b>(-35.14%)</b></td><td>2088.70 <b>(-48.77%)</b></td><td>1850.20 <b>(-43.76%)</b></td><td>1024.35 <b>(+149.53%)</b></td><td>290.17 <b>(+77.82%)</b></td><td>230.61 <b>(+68.56%)</b></td><td>257.03 <b>(+95.19%)</b></td><td>125.11 (+1.88%)</td><td>69.54 <b>(+344.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.71 (n/a)</td><td>2.27 (n/a)</td><td>2.19 (n/a)</td><td>2.04 (n/a)</td><td>0.26 (n/a)</td><td>4371.90 (n/a)</td><td>3961.66 (n/a)</td><td>4077.10 (n/a)</td><td>3289.90 (n/a)</td><td>410.51 (n/a)</td><td>163.19 (n/a)</td><td>136.81 (n/a)</td><td>131.68 (n/a)</td><td>122.80 (n/a)</td><td>15.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.07 <b>(-23.59%)</b></td><td>3.19 (-18.13%)</td><td>3.10 <b>(-24.60%)</b></td><td>2.04 (-4.77%)</td><td>0.86 <b>(-41.68%)</b></td><td>4368.10 (+5.00%)</td><td>2978.72 (+14.01%)</td><td>2873.00 <b>(+32.62%)</b></td><td>2188.10 <b>(+30.88%)</b></td><td>893.22 (-19.41%)</td><td>245.36 <b>(-23.59%)</b></td><td>192.37 (-18.13%)</td><td>186.87 <b>(-24.60%)</b></td><td>122.91 (-4.77%)</td><td>51.70 <b>(-41.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.33 (n/a)</td><td>3.90 (n/a)</td><td>4.11 (n/a)</td><td>2.14 (n/a)</td><td>1.47 (n/a)</td><td>4159.90 (n/a)</td><td>2612.66 (n/a)</td><td>2166.30 (n/a)</td><td>1671.90 (n/a)</td><td>1108.38 (n/a)</td><td>321.11 (n/a)</td><td>234.97 (n/a)</td><td>247.83 (n/a)</td><td>129.06 (n/a)</td><td>88.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.50 (-0.38%)</td><td>5.39 (+6.08%)</td><td>5.02 (+6.05%)</td><td>4.95 (+12.81%)</td><td>0.66 <b>(-21.09%)</b></td><td>7043.30 (-11.36%)</td><td>6534.52 (-6.48%)</td><td>6942.40 (-5.71%)</td><td>5367.10 (+0.38%)</td><td>719.87 <b>(-27.38%)</b></td><td>400.12 (-0.38%)</td><td>332.22 (+6.08%)</td><td>309.33 (+6.05%)</td><td>304.90 (+12.81%)</td><td>40.73 <b>(-21.09%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.52 (n/a)</td><td>5.08 (n/a)</td><td>4.74 (n/a)</td><td>4.39 (n/a)</td><td>0.84 (n/a)</td><td>7945.60 (n/a)</td><td>6987.42 (n/a)</td><td>7362.70 (n/a)</td><td>5346.80 (n/a)</td><td>991.27 (n/a)</td><td>401.64 (n/a)</td><td>313.16 (n/a)</td><td>291.67 (n/a)</td><td>270.27 (n/a)</td><td>51.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.16 (+10.45%)</td><td>5.17 (+5.14%)</td><td>4.82 (-1.62%)</td><td>4.33 (+9.40%)</td><td>0.83 <b>(+24.91%)</b></td><td>8059.80 (-8.59%)</td><td>6882.60 (-4.47%)</td><td>7228.10 (+1.65%)</td><td>5659.20 (-9.46%)</td><td>1068.23 (+2.48%)</td><td>379.47 (+10.45%)</td><td>318.35 (+5.14%)</td><td>297.10 (-1.62%)</td><td>266.44 (+9.40%)</td><td>51.18 <b>(+24.91%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.58 (n/a)</td><td>4.92 (n/a)</td><td>4.90 (n/a)</td><td>3.95 (n/a)</td><td>0.67 (n/a)</td><td>8817.30 (n/a)</td><td>7204.44 (n/a)</td><td>7110.80 (n/a)</td><td>6250.60 (n/a)</td><td>1042.37 (n/a)</td><td>343.56 (n/a)</td><td>302.79 (n/a)</td><td>302.00 (n/a)</td><td>243.55 (n/a)</td><td>40.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.82 (-10.55%)</td><td>4.91 (-13.33%)</td><td>4.95 (-14.29%)</td><td>3.56 <b>(-27.24%)</b></td><td>0.86 <b>(+26.76%)</b></td><td>9805.90 <b>(+37.43%)</b></td><td>7301.14 (+17.38%)</td><td>7046.70 (+16.67%)</td><td>5993.70 (+11.80%)</td><td>1490.47 <b>(+97.76%)</b></td><td>358.29 (-10.55%)</td><td>302.71 (-13.33%)</td><td>304.75 (-14.29%)</td><td>219.00 <b>(-27.24%)</b></td><td>53.11 <b>(+26.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.50 (n/a)</td><td>5.67 (n/a)</td><td>5.77 (n/a)</td><td>4.89 (n/a)</td><td>0.68 (n/a)</td><td>7135.20 (n/a)</td><td>6220.24 (n/a)</td><td>6039.80 (n/a)</td><td>5361.20 (n/a)</td><td>753.67 (n/a)</td><td>400.56 (n/a)</td><td>349.29 (n/a)</td><td>355.56 (n/a)</td><td>300.97 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.78 (-1.01%)</td><td>0.75 (-0.98%)</td><td>0.76 (-1.65%)</td><td>0.73 (+3.70%)</td><td>0.02 <b>(-45.29%)</b></td><td>102731.40 (-3.57%)</td><td>100232.70 (+0.88%)</td><td>99977.90 (+1.68%)</td><td>96837.20 (+1.02%)</td><td>2343.32 <b>(-46.64%)</b></td><td>709.64 (-1.01%)</td><td>685.90 (-0.98%)</td><td>687.35 (-1.65%)</td><td>668.92 (+3.70%)</td><td>16.17 <b>(-45.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.71 (n/a)</td><td>0.03 (n/a)</td><td>106529.80 (n/a)</td><td>99353.62 (n/a)</td><td>98326.60 (n/a)</td><td>95860.10 (n/a)</td><td>4391.67 (n/a)</td><td>716.87 (n/a)</td><td>692.71 (n/a)</td><td>698.89 (n/a)</td><td>645.07 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.77 (+1.12%)</td><td>0.76 (+1.35%)</td><td>0.76 (+0.72%)</td><td>0.75 (+2.59%)</td><td>0.01 <b>(-30.95%)</b></td><td>100567.80 (-2.52%)</td><td>99330.92 (-1.35%)</td><td>99381.90 (-0.71%)</td><td>97866.30 (-1.10%)</td><td>1073.09 <b>(-33.54%)</b></td><td>702.18 (+1.12%)</td><td>691.89 (+1.35%)</td><td>691.47 (+0.72%)</td><td>683.32 (+2.59%)</td><td>7.49 <b>(-30.95%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.01 (n/a)</td><td>103171.20 (n/a)</td><td>100685.70 (n/a)</td><td>100096.70 (n/a)</td><td>98957.80 (n/a)</td><td>1614.64 (n/a)</td><td>694.43 (n/a)</td><td>682.65 (n/a)</td><td>686.53 (n/a)</td><td>666.07 (n/a)</td><td>10.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.81 (-0.32%)</td><td>0.80 (-1.03%)</td><td>0.80 (-1.16%)</td><td>0.79 (-0.91%)</td><td>0.01 (+18.06%)</td><td>95644.80 (+0.92%)</td><td>94426.88 (+1.04%)</td><td>94330.10 (+1.18%)</td><td>92850.50 (+0.32%)</td><td>1055.45 (+19.43%)</td><td>740.11 (-0.32%)</td><td>727.83 (-1.03%)</td><td>728.50 (-1.16%)</td><td>718.49 (-0.91%)</td><td>8.17 (+18.06%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94770.00 (n/a)</td><td>93450.44 (n/a)</td><td>93233.90 (n/a)</td><td>92556.70 (n/a)</td><td>883.76 (n/a)</td><td>742.46 (n/a)</td><td>735.41 (n/a)</td><td>737.07 (n/a)</td><td>725.12 (n/a)</td><td>6.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.46 (-7.65%)</td><td>2.56 (-11.00%)</td><td>2.44 <b>(-27.84%)</b></td><td>1.67 (-3.13%)</td><td>0.87 (-12.02%)</td><td>4819.30 (+3.23%)</td><td>3468.88 (+10.43%)</td><td>3299.20 <b>(+38.59%)</b></td><td>2331.20 (+8.28%)</td><td>1181.92 (-3.73%)</td><td>906.79 (-7.65%)</td><td>670.58 (-11.00%)</td><td>640.74 <b>(-27.84%)</b></td><td>438.63 (-3.13%)</td><td>227.32 (-12.02%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.74 (n/a)</td><td>2.87 (n/a)</td><td>3.39 (n/a)</td><td>1.73 (n/a)</td><td>0.99 (n/a)</td><td>4668.40 (n/a)</td><td>3141.14 (n/a)</td><td>2380.50 (n/a)</td><td>2152.90 (n/a)</td><td>1227.65 (n/a)</td><td>981.90 (n/a)</td><td>753.47 (n/a)</td><td>888.00 (n/a)</td><td>452.81 (n/a)</td><td>258.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (+5.69%)</td><td>0.21 (+2.61%)</td><td>0.21 (+8.60%)</td><td>0.17 (-6.08%)</td><td>0.04 <b>(+32.17%)</b></td><td>7341.60 (+6.47%)</td><td>6091.64 (-1.26%)</td><td>5821.90 (-7.92%)</td><td>4527.80 (-5.39%)</td><td>1124.04 <b>(+38.35%)</b></td><td>14.82 (+5.69%)</td><td>11.34 (+2.61%)</td><td>11.53 (+8.60%)</td><td>9.14 (-6.08%)</td><td>2.25 <b>(+32.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>6895.60 (n/a)</td><td>6169.26 (n/a)</td><td>6322.70 (n/a)</td><td>4785.70 (n/a)</td><td>812.45 (n/a)</td><td>14.02 (n/a)</td><td>11.06 (n/a)</td><td>10.61 (n/a)</td><td>9.73 (n/a)</td><td>1.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.68 (n/a)</td><td>3.40 (n/a)</td><td>0.20 (n/a)</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.68 (n/a)</td><td>3.40 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.55 (+4.96%)</td><td>6.67 (+2.31%)</td><td>7.03 (+3.70%)</td><td>5.72 (+0.17%)</td><td>0.87 <b>(+25.52%)</b></td><td>7.54 (+4.96%)</td><td>6.67 (+2.31%)</td><td>7.03 (+3.70%)</td><td>5.71 (+0.17%)</td><td>0.87 <b>(+25.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.19 (n/a)</td><td>6.52 (n/a)</td><td>6.78 (n/a)</td><td>5.71 (n/a)</td><td>0.69 (n/a)</td><td>7.18 (n/a)</td><td>6.52 (n/a)</td><td>6.78 (n/a)</td><td>5.70 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>13.65 (+5.28%)</td><td>10.17 (+10.41%)</td><td>10.18 <b>(+21.43%)</b></td><td>6.13 <b>(-22.21%)</b></td><td>2.99 <b>(+41.55%)</b></td><td>13.64 (+5.28%)</td><td>10.16 (+10.41%)</td><td>10.17 <b>(+21.43%)</b></td><td>6.13 <b>(-22.21%)</b></td><td>2.99 <b>(+41.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>12.97 (n/a)</td><td>9.21 (n/a)</td><td>8.38 (n/a)</td><td>7.88 (n/a)</td><td>2.11 (n/a)</td><td>12.96 (n/a)</td><td>9.20 (n/a)</td><td>8.38 (n/a)</td><td>7.88 (n/a)</td><td>2.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.72 (n/a)</td><td>3.52 (n/a)</td><td>3.50 (n/a)</td><td>3.39 (n/a)</td><td>0.13 (n/a)</td><td>3.72 (n/a)</td><td>3.51 (n/a)</td><td>3.50 (n/a)</td><td>3.39 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.41 (+15.45%)</td><td>6.39 (+4.20%)</td><td>6.50 (+3.41%)</td><td>5.23 (-9.51%)</td><td>0.98 <b>(+232.06%)</b></td><td>7.40 (+15.45%)</td><td>6.38 (+4.20%)</td><td>6.49 (+3.41%)</td><td>5.23 (-9.51%)</td><td>0.98 <b>(+232.06%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.42 (n/a)</td><td>6.13 (n/a)</td><td>6.28 (n/a)</td><td>5.78 (n/a)</td><td>0.29 (n/a)</td><td>6.41 (n/a)</td><td>6.12 (n/a)</td><td>6.28 (n/a)</td><td>5.78 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>13.45 (+4.51%)</td><td>9.22 (-6.02%)</td><td>8.45 (-1.30%)</td><td>7.35 (-11.30%)</td><td>2.41 <b>(+20.72%)</b></td><td>13.44 (+4.51%)</td><td>9.22 (-6.02%)</td><td>8.44 (-1.30%)</td><td>7.35 (-11.30%)</td><td>2.41 <b>(+20.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>12.87 (n/a)</td><td>9.81 (n/a)</td><td>8.56 (n/a)</td><td>8.29 (n/a)</td><td>1.99 (n/a)</td><td>12.86 (n/a)</td><td>9.81 (n/a)</td><td>8.56 (n/a)</td><td>8.29 (n/a)</td><td>1.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.98 (+0.81%)</td><td>2.41 <b>(+28.65%)</b></td><td>2.75 <b>(+69.51%)</b></td><td>1.51 <b>(+47.62%)</b></td><td>0.62 <b>(-32.31%)</b></td><td>2.97 (+0.81%)</td><td>2.41 <b>(+28.65%)</b></td><td>2.75 <b>(+69.51%)</b></td><td>1.51 <b>(+47.62%)</b></td><td>0.62 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.95 (n/a)</td><td>1.88 (n/a)</td><td>1.62 (n/a)</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td><td>2.95 (n/a)</td><td>1.87 (n/a)</td><td>1.62 (n/a)</td><td>1.02 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 (+8.10%)</td><td>0.36 <b>(+26.92%)</b></td><td>0.33 (+18.54%)</td><td>0.08 (+2.76%)</td><td>0.19 (-9.41%)</td><td>0.55 (+8.10%)</td><td>0.36 <b>(+26.92%)</b></td><td>0.33 (+18.54%)</td><td>0.08 (+2.76%)</td><td>0.19 (-9.41%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.52 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.74 (+8.80%)</td><td>0.48 (-0.57%)</td><td>0.64 <b>(+40.15%)</b></td><td>0.07 <b>(-80.06%)</b></td><td>0.28 <b>(+130.63%)</b></td><td>0.73 (+8.80%)</td><td>0.47 (-0.57%)</td><td>0.64 <b>(+40.15%)</b></td><td>0.07 <b>(-80.06%)</b></td><td>0.28 <b>(+130.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.68 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.12 (n/a)</td><td>0.67 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.68 (-4.94%)</td><td>1.58 <b>(-26.79%)</b></td><td>1.49 <b>(-38.22%)</b></td><td>0.45 <b>(-70.63%)</b></td><td>0.90 <b>(+54.37%)</b></td><td>2.64 (-4.94%)</td><td>1.56 <b>(-26.79%)</b></td><td>1.46 <b>(-38.22%)</b></td><td>0.44 <b>(-70.63%)</b></td><td>0.89 <b>(+54.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.82 (n/a)</td><td>2.16 (n/a)</td><td>2.41 (n/a)</td><td>1.54 (n/a)</td><td>0.58 (n/a)</td><td>2.78 (n/a)</td><td>2.13 (n/a)</td><td>2.37 (n/a)</td><td>1.51 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.20 (n/a)</td><td>365.46 (n/a)</td><td>396.90 (n/a)</td><td>242.50 (n/a)</td><td>92.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>297.90 (n/a)</td><td>251.02 (n/a)</td><td>244.70 (n/a)</td><td>223.50 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.90 (n/a)</td><td>316.10 (n/a)</td><td>307.50 (n/a)</td><td>226.00 (n/a)</td><td>92.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.60 (n/a)</td><td>321.52 (n/a)</td><td>265.00 (n/a)</td><td>249.70 (n/a)</td><td>136.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>358.98 (n/a)</td><td>268.20 (n/a)</td><td>194.50 (n/a)</td><td>170.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>956.90 (n/a)</td><td>539.28 (n/a)</td><td>343.40 (n/a)</td><td>263.20 (n/a)</td><td>342.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>379.00 (n/a)</td><td>292.68 (n/a)</td><td>279.50 (n/a)</td><td>240.10 (n/a)</td><td>51.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.40 (n/a)</td><td>382.98 (n/a)</td><td>453.30 (n/a)</td><td>269.20 (n/a)</td><td>99.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.40 (n/a)</td><td>353.34 (n/a)</td><td>270.10 (n/a)</td><td>220.60 (n/a)</td><td>177.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>400.30 (n/a)</td><td>315.06 (n/a)</td><td>278.40 (n/a)</td><td>244.10 (n/a)</td><td>74.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.10 (n/a)</td><td>371.40 (n/a)</td><td>337.50 (n/a)</td><td>247.30 (n/a)</td><td>124.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1764.60 (n/a)</td><td>713.44 (n/a)</td><td>596.10 (n/a)</td><td>248.40 (n/a)</td><td>616.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>526.50 (n/a)</td><td>355.58 (n/a)</td><td>322.00 (n/a)</td><td>253.20 (n/a)</td><td>110.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.60 (n/a)</td><td>474.02 (n/a)</td><td>527.70 (n/a)</td><td>233.80 (n/a)</td><td>148.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>754.70 (n/a)</td><td>390.06 (n/a)</td><td>302.40 (n/a)</td><td>224.00 (n/a)</td><td>214.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>960.10 (n/a)</td><td>533.24 (n/a)</td><td>585.70 (n/a)</td><td>222.30 (n/a)</td><td>310.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1965.40 (n/a)</td><td>677.12 (n/a)</td><td>394.70 (n/a)</td><td>202.60 (n/a)</td><td>727.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.50 (n/a)</td><td>484.26 (n/a)</td><td>477.50 (n/a)</td><td>363.70 (n/a)</td><td>91.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>676.80 (n/a)</td><td>441.98 (n/a)</td><td>447.90 (n/a)</td><td>234.10 (n/a)</td><td>165.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>751.90 (n/a)</td><td>428.66 (n/a)</td><td>373.50 (n/a)</td><td>200.00 (n/a)</td><td>224.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>604.50 (n/a)</td><td>402.06 (n/a)</td><td>339.20 (n/a)</td><td>252.60 (n/a)</td><td>155.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>571.00 (n/a)</td><td>425.18 (n/a)</td><td>408.50 (n/a)</td><td>307.20 (n/a)</td><td>119.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>484.90 (n/a)</td><td>418.02 (n/a)</td><td>459.20 (n/a)</td><td>263.20 (n/a)</td><td>89.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>498.82 (n/a)</td><td>526.70 (n/a)</td><td>297.00 (n/a)</td><td>122.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-13.33%)</td><td>0.01 (-15.34%)</td><td>0.01 <b>(-30.19%)</b></td><td>0.01 (+4.53%)</td><td>0.00 <b>(-41.12%)</b></td><td>511.40 (-4.32%)</td><td>387.62 (+10.44%)</td><td>373.80 <b>(+43.27%)</b></td><td>275.70 (+15.40%)</td><td>89.25 <b>(-34.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.50 (n/a)</td><td>350.98 (n/a)</td><td>260.90 (n/a)</td><td>238.90 (n/a)</td><td>136.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+25.16%)</b></td><td>0.01 (-9.15%)</td><td>0.01 <b>(-21.46%)</b></td><td>0.01 (-11.51%)</td><td>0.01 <b>(+84.35%)</b></td><td>518.00 (+13.00%)</td><td>369.56 <b>(+20.83%)</b></td><td>353.40 <b>(+27.35%)</b></td><td>192.80 <b>(-20.10%)</b></td><td>145.72 <b>(+67.60%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.40 (n/a)</td><td>305.84 (n/a)</td><td>277.50 (n/a)</td><td>241.30 (n/a)</td><td>86.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+18.62%)</td><td>0.01 <b>(-20.04%)</b></td><td>0.01 <b>(-48.27%)</b></td><td>0.00 <b>(-75.48%)</b></td><td>0.01 <b>(+92.85%)</b></td><td>1903.20 <b>(+307.80%)</b></td><td>695.18 <b>(+103.47%)</b></td><td>530.30 <b>(+93.33%)</b></td><td>221.00 (-15.71%)</td><td>691.98 <b>(+579.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.70 (n/a)</td><td>341.66 (n/a)</td><td>274.30 (n/a)</td><td>262.20 (n/a)</td><td>101.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-0.63%)</td><td>0.01 <b>(+24.93%)</b></td><td>0.01 <b>(+48.46%)</b></td><td>0.01 <b>(+28.43%)</b></td><td>0.00 (+5.33%)</td><td>590.70 <b>(-22.13%)</b></td><td>396.62 <b>(-20.92%)</b></td><td>294.30 <b>(-32.64%)</b></td><td>281.50 (+0.61%)</td><td>148.73 (-19.52%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>758.60 (n/a)</td><td>501.52 (n/a)</td><td>436.90 (n/a)</td><td>279.80 (n/a)</td><td>184.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+4.01%)</td><td>0.01 (+2.58%)</td><td>0.01 (+15.31%)</td><td>0.01 <b>(-20.01%)</b></td><td>0.00 (+12.29%)</td><td>657.20 <b>(+25.01%)</b></td><td>449.50 (-0.21%)</td><td>446.10 (-13.28%)</td><td>266.10 (-3.87%)</td><td>139.72 <b>(+30.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.70 (n/a)</td><td>450.46 (n/a)</td><td>514.40 (n/a)</td><td>276.80 (n/a)</td><td>106.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+61.25%)</b></td><td>0.01 (+9.63%)</td><td>0.01 (-7.68%)</td><td>0.01 (-13.24%)</td><td>0.00 <b>(+249.66%)</b></td><td>610.80 (+15.27%)</td><td>471.60 (+2.14%)</td><td>509.00 (+8.32%)</td><td>223.70 <b>(-37.98%)</b></td><td>151.14 <b>(+144.34%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.90 (n/a)</td><td>461.72 (n/a)</td><td>469.90 (n/a)</td><td>360.70 (n/a)</td><td>61.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-4.91%)</td><td>0.03 (+12.79%)</td><td>0.03 <b>(+61.12%)</b></td><td>0.02 (+8.87%)</td><td>0.01 <b>(-20.31%)</b></td><td>486.20 (-8.14%)</td><td>342.46 (-14.26%)</td><td>287.30 <b>(-37.93%)</b></td><td>262.00 (+5.18%)</td><td>96.55 <b>(-22.35%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.30 (n/a)</td><td>399.40 (n/a)</td><td>462.90 (n/a)</td><td>249.10 (n/a)</td><td>124.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (+14.06%)</td><td>0.03 <b>(+24.50%)</b></td><td>0.03 <b>(+57.11%)</b></td><td>0.02 <b>(+26.64%)</b></td><td>0.01 <b>(+36.24%)</b></td><td>501.00 <b>(-21.04%)</b></td><td>330.04 (-17.47%)</td><td>240.30 <b>(-36.34%)</b></td><td>221.80 (-12.30%)</td><td>133.40 (-7.91%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.50 (n/a)</td><td>399.88 (n/a)</td><td>377.50 (n/a)</td><td>252.90 (n/a)</td><td>144.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+44.41%)</b></td><td>0.03 (+1.12%)</td><td>0.02 <b>(-24.83%)</b></td><td>0.01 (-10.82%)</td><td>0.02 <b>(+99.73%)</b></td><td>569.70 (+12.12%)</td><td>370.60 (+12.35%)</td><td>390.80 <b>(+33.02%)</b></td><td>155.40 <b>(-30.75%)</b></td><td>161.73 <b>(+46.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.10 (n/a)</td><td>329.86 (n/a)</td><td>293.80 (n/a)</td><td>224.40 (n/a)</td><td>110.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-10.69%)</td><td>0.02 (-18.18%)</td><td>0.01 <b>(-29.92%)</b></td><td>0.01 <b>(+133.78%)</b></td><td>0.01 <b>(-26.53%)</b></td><td>873.10 <b>(-57.23%)</b></td><td>567.84 (-18.71%)</td><td>608.10 <b>(+42.71%)</b></td><td>244.20 (+11.97%)</td><td>233.28 <b>(-69.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2041.20 (n/a)</td><td>698.52 (n/a)</td><td>426.10 (n/a)</td><td>218.10 (n/a)</td><td>760.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 <b>(+122.76%)</b></td><td>0.02 <b>(+52.01%)</b></td><td>0.02 <b>(+23.07%)</b></td><td>0.01 (-10.17%)</td><td>0.01 <b>(+303.78%)</b></td><td>710.20 (+11.32%)</td><td>437.54 (-17.60%)</td><td>461.40 (-18.74%)</td><td>182.30 <b>(-55.12%)</b></td><td>224.39 <b>(+101.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.00 (n/a)</td><td>531.00 (n/a)</td><td>567.80 (n/a)</td><td>406.20 (n/a)</td><td>111.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-11.86%)</td><td>0.02 <b>(+20.37%)</b></td><td>0.02 <b>(+35.79%)</b></td><td>0.01 <b>(+230.84%)</b></td><td>0.01 <b>(-35.99%)</b></td><td>582.20 <b>(-69.78%)</b></td><td>418.56 <b>(-43.45%)</b></td><td>362.40 <b>(-26.34%)</b></td><td>242.40 (+13.48%)</td><td>144.02 <b>(-78.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1926.30 (n/a)</td><td>740.16 (n/a)</td><td>492.00 (n/a)</td><td>213.60 (n/a)</td><td>677.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-18.57%)</td><td>0.02 (-16.93%)</td><td>0.02 <b>(-22.52%)</b></td><td>0.01 (-3.53%)</td><td>0.01 <b>(-31.10%)</b></td><td>641.20 (+3.67%)</td><td>448.40 (+14.32%)</td><td>466.30 <b>(+29.06%)</b></td><td>274.70 <b>(+22.80%)</b></td><td>137.41 (-13.94%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.50 (n/a)</td><td>392.22 (n/a)</td><td>361.30 (n/a)</td><td>223.70 (n/a)</td><td>159.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+1.38%)</td><td>0.02 (+2.66%)</td><td>0.02 (+17.70%)</td><td>0.01 (-4.39%)</td><td>0.00 (+14.40%)</td><td>637.20 (+4.60%)</td><td>474.68 (-1.17%)</td><td>428.90 (-15.04%)</td><td>362.10 (-1.34%)</td><td>125.61 <b>(+20.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.20 (n/a)</td><td>480.30 (n/a)</td><td>504.80 (n/a)</td><td>367.00 (n/a)</td><td>104.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 <b>(+68.84%)</b></td><td>0.05 (-0.79%)</td><td>0.03 <b>(-49.18%)</b></td><td>0.02 (-10.46%)</td><td>0.04 <b>(+102.41%)</b></td><td>663.50 (+11.68%)</td><td>435.92 (+19.76%)</td><td>514.60 <b>(+96.71%)</b></td><td>144.40 <b>(-40.77%)</b></td><td>209.75 <b>(+34.04%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.10 (n/a)</td><td>363.98 (n/a)</td><td>261.60 (n/a)</td><td>243.80 (n/a)</td><td>156.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (-13.06%)</td><td>0.04 <b>(-33.82%)</b></td><td>0.03 <b>(-40.99%)</b></td><td>0.02 <b>(-46.09%)</b></td><td>0.02 (+3.79%)</td><td>1020.80 <b>(+85.50%)</b></td><td>539.20 <b>(+65.71%)</b></td><td>486.60 <b>(+69.49%)</b></td><td>280.90 (+15.03%)</td><td>285.24 <b>(+123.41%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>550.30 (n/a)</td><td>325.38 (n/a)</td><td>287.10 (n/a)</td><td>244.20 (n/a)</td><td>127.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+69.25%)</b></td><td>0.05 (+18.29%)</td><td>0.04 (+14.66%)</td><td>0.03 (+7.17%)</td><td>0.03 <b>(+114.32%)</b></td><td>507.20 (-6.68%)</td><td>374.44 (-8.11%)</td><td>367.90 (-12.80%)</td><td>174.90 <b>(-40.89%)</b></td><td>131.56 <b>(+20.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>543.50 (n/a)</td><td>407.50 (n/a)</td><td>421.90 (n/a)</td><td>295.90 (n/a)</td><td>109.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+5.96%)</td><td>0.04 (+14.56%)</td><td>0.04 (+13.09%)</td><td>0.03 (+12.36%)</td><td>0.02 (+8.14%)</td><td>590.70 (-11.00%)</td><td>413.04 (-12.18%)</td><td>422.50 (-11.57%)</td><td>232.70 (-5.64%)</td><td>146.15 (-3.57%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>663.70 (n/a)</td><td>470.30 (n/a)</td><td>477.80 (n/a)</td><td>246.60 (n/a)</td><td>151.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (-8.05%)</td><td>0.05 (+11.03%)</td><td>0.05 <b>(+54.66%)</b></td><td>0.03 <b>(+23.46%)</b></td><td>0.01 <b>(-28.94%)</b></td><td>502.60 (-19.00%)</td><td>362.94 (-16.82%)</td><td>305.90 <b>(-35.34%)</b></td><td>254.10 (+8.73%)</td><td>113.30 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.50 (n/a)</td><td>436.32 (n/a)</td><td>473.10 (n/a)</td><td>233.70 (n/a)</td><td>175.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(+47.25%)</b></td><td>0.04 (+11.80%)</td><td>0.03 (-2.53%)</td><td>0.03 (-2.05%)</td><td>0.02 <b>(+112.97%)</b></td><td>609.40 (+2.09%)</td><td>464.52 (-1.96%)</td><td>502.30 (+2.59%)</td><td>211.80 <b>(-32.07%)</b></td><td>152.71 <b>(+41.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>473.80 (n/a)</td><td>489.60 (n/a)</td><td>311.80 (n/a)</td><td>107.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (-8.03%)</td><td>0.10 <b>(+31.00%)</b></td><td>0.11 <b>(+73.55%)</b></td><td>0.08 <b>(+51.01%)</b></td><td>0.02 <b>(-39.21%)</b></td><td>416.80 <b>(-33.78%)</b></td><td>332.62 <b>(-29.02%)</b></td><td>292.20 <b>(-42.38%)</b></td><td>272.50 (+8.74%)</td><td>67.20 <b>(-54.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>629.40 (n/a)</td><td>468.64 (n/a)</td><td>507.10 (n/a)</td><td>250.60 (n/a)</td><td>146.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (+15.43%)</td><td>0.08 (-13.30%)</td><td>0.07 (-10.31%)</td><td>0.02 <b>(-69.27%)</b></td><td>0.05 <b>(+40.19%)</b></td><td>1861.70 <b>(+225.42%)</b></td><td>690.12 <b>(+68.31%)</b></td><td>475.30 (+11.49%)</td><td>198.40 (-13.36%)</td><td>665.32 <b>(+328.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>572.10 (n/a)</td><td>410.02 (n/a)</td><td>426.30 (n/a)</td><td>229.00 (n/a)</td><td>155.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (+9.98%)</td><td>0.09 (+8.56%)</td><td>0.07 (+10.50%)</td><td>0.06 <b>(+48.67%)</b></td><td>0.04 (-12.70%)</td><td>537.80 <b>(-32.74%)</b></td><td>397.04 (-15.87%)</td><td>449.20 (-9.51%)</td><td>224.00 (-9.09%)</td><td>129.48 <b>(-42.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>799.60 (n/a)</td><td>471.94 (n/a)</td><td>496.40 (n/a)</td><td>246.40 (n/a)</td><td>227.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (-0.45%)</td><td>0.11 (+16.38%)</td><td>0.12 <b>(+44.50%)</b></td><td>0.03 <b>(-53.13%)</b></td><td>0.04 <b>(+49.01%)</b></td><td>1101.40 <b>(+113.37%)</b></td><td>426.34 (+11.74%)</td><td>263.80 <b>(-30.78%)</b></td><td>242.20 (+0.41%)</td><td>377.62 <b>(+232.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.20 (n/a)</td><td>381.56 (n/a)</td><td>381.10 (n/a)</td><td>241.20 (n/a)</td><td>113.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 <b>(+22.81%)</b></td><td>0.09 (+12.72%)</td><td>0.07 (+0.84%)</td><td>0.05 (+5.52%)</td><td>0.04 <b>(+28.59%)</b></td><td>632.80 (-5.24%)</td><td>419.96 (-9.20%)</td><td>446.70 (-0.82%)</td><td>217.90 (-18.57%)</td><td>162.98 (-4.02%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>667.80 (n/a)</td><td>462.52 (n/a)</td><td>450.40 (n/a)</td><td>267.60 (n/a)</td><td>169.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-10.65%)</td><td>0.01 (+14.92%)</td><td>0.01 <b>(+42.38%)</b></td><td>0.01 <b>(+38.81%)</b></td><td>0.00 <b>(-39.27%)</b></td><td>439.40 <b>(-27.96%)</b></td><td>307.88 <b>(-21.20%)</b></td><td>291.10 <b>(-29.77%)</b></td><td>240.10 (+11.88%)</td><td>81.28 <b>(-49.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.90 (n/a)</td><td>390.72 (n/a)</td><td>414.50 (n/a)</td><td>214.60 (n/a)</td><td>161.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+10.13%)</td><td>0.02 (+15.90%)</td><td>0.02 (+9.22%)</td><td>0.01 <b>(+43.40%)</b></td><td>0.00 <b>(-47.08%)</b></td><td>284.20 <b>(-30.26%)</b></td><td>251.92 (-15.71%)</td><td>250.80 (-8.47%)</td><td>229.20 (-9.19%)</td><td>20.26 <b>(-67.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>407.50 (n/a)</td><td>298.88 (n/a)</td><td>274.00 (n/a)</td><td>252.40 (n/a)</td><td>62.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(-25.46%)</b></td><td>0.01 (+19.29%)</td><td>0.01 <b>(+60.66%)</b></td><td>0.01 <b>(+22.36%)</b></td><td>0.00 <b>(-38.61%)</b></td><td>528.20 (-18.29%)</td><td>345.08 <b>(-24.81%)</b></td><td>294.20 <b>(-37.76%)</b></td><td>243.00 <b>(+34.11%)</b></td><td>124.25 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.40 (n/a)</td><td>458.92 (n/a)</td><td>472.70 (n/a)</td><td>181.20 (n/a)</td><td>180.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+3.42%)</td><td>0.01 (+5.58%)</td><td>0.01 (-14.22%)</td><td>0.01 (+13.29%)</td><td>0.00 (-15.21%)</td><td>451.70 (-11.74%)</td><td>315.34 (-8.85%)</td><td>315.90 (+16.57%)</td><td>233.30 (-3.32%)</td><td>88.20 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.80 (n/a)</td><td>345.94 (n/a)</td><td>271.00 (n/a)</td><td>241.30 (n/a)</td><td>125.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+27.40%)</b></td><td>0.01 <b>(+36.58%)</b></td><td>0.01 <b>(+68.17%)</b></td><td>0.01 <b>(+22.28%)</b></td><td>0.00 (+11.70%)</td><td>456.70 (-18.21%)</td><td>301.78 <b>(-28.06%)</b></td><td>285.40 <b>(-40.53%)</b></td><td>216.30 <b>(-21.52%)</b></td><td>98.91 <b>(-26.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.40 (n/a)</td><td>419.48 (n/a)</td><td>479.90 (n/a)</td><td>275.60 (n/a)</td><td>134.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+12.78%)</td><td>0.01 (+4.73%)</td><td>0.01 (-6.70%)</td><td>0.01 (-1.39%)</td><td>0.00 <b>(+27.82%)</b></td><td>470.40 (+1.42%)</td><td>335.82 (-2.51%)</td><td>311.60 (+7.19%)</td><td>241.60 (-11.34%)</td><td>100.77 (+13.49%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.80 (n/a)</td><td>344.46 (n/a)</td><td>290.70 (n/a)</td><td>272.50 (n/a)</td><td>88.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+22.73%)</b></td><td>0.01 <b>(+31.32%)</b></td><td>0.01 (+11.00%)</td><td>0.01 <b>(+33.96%)</b></td><td>0.00 <b>(+38.87%)</b></td><td>573.60 <b>(-25.35%)</b></td><td>388.02 <b>(-22.85%)</b></td><td>423.60 (-9.91%)</td><td>234.80 (-18.50%)</td><td>145.86 <b>(-21.35%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>768.40 (n/a)</td><td>502.94 (n/a)</td><td>470.20 (n/a)</td><td>288.10 (n/a)</td><td>185.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+59.16%)</b></td><td>0.01 <b>(+122.63%)</b></td><td>0.01 <b>(+126.91%)</b></td><td>0.01 <b>(+321.58%)</b></td><td>0.00 (+17.08%)</td><td>575.00 <b>(-76.28%)</b></td><td>374.82 <b>(-69.06%)</b></td><td>293.60 <b>(-55.93%)</b></td><td>246.10 <b>(-37.19%)</b></td><td>150.13 <b>(-83.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2424.10 (n/a)</td><td>1211.52 (n/a)</td><td>666.20 (n/a)</td><td>391.80 (n/a)</td><td>936.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-1.58%)</td><td>0.01 (+8.58%)</td><td>0.01 (+3.13%)</td><td>0.01 (-3.68%)</td><td>0.00 <b>(+26.15%)</b></td><td>552.30 (+3.82%)</td><td>405.88 (-3.04%)</td><td>441.40 (-3.03%)</td><td>245.30 (+1.62%)</td><td>152.62 <b>(+31.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.00 (n/a)</td><td>418.62 (n/a)</td><td>455.20 (n/a)</td><td>241.40 (n/a)</td><td>115.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+16.50%)</td><td>0.01 (+8.18%)</td><td>0.02 (+5.06%)</td><td>0.01 (+17.62%)</td><td>0.00 (+18.83%)</td><td>418.80 (-14.98%)</td><td>317.06 (-7.05%)</td><td>267.90 (-4.83%)</td><td>226.70 (-14.16%)</td><td>90.09 (-7.65%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.60 (n/a)</td><td>341.10 (n/a)</td><td>281.50 (n/a)</td><td>264.10 (n/a)</td><td>97.55 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+81.21%)</b></td><td>0.01 <b>(+34.95%)</b></td><td>0.01 (+17.23%)</td><td>0.01 (+4.41%)</td><td>0.00 <b>(+257.50%)</b></td><td>573.00 (-4.23%)</td><td>423.22 (-16.91%)</td><td>450.20 (-14.69%)</td><td>221.60 <b>(-44.82%)</b></td><td>156.90 <b>(+97.45%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.30 (n/a)</td><td>509.34 (n/a)</td><td>527.70 (n/a)</td><td>401.60 (n/a)</td><td>79.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+11.05%)</td><td>0.01 (+16.38%)</td><td>0.01 (+3.33%)</td><td>0.01 <b>(+205.54%)</b></td><td>0.00 <b>(-22.22%)</b></td><td>633.80 <b>(-67.27%)</b></td><td>405.34 <b>(-41.02%)</b></td><td>344.50 (-3.23%)</td><td>255.20 (-9.95%)</td><td>151.00 <b>(-78.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1936.60 (n/a)</td><td>687.20 (n/a)</td><td>356.00 (n/a)</td><td>283.40 (n/a)</td><td>704.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (+0.99%)</td><td>0.03 <b>(+28.49%)</b></td><td>0.03 <b>(+59.74%)</b></td><td>0.02 <b>(+27.75%)</b></td><td>0.00 <b>(-41.24%)</b></td><td>364.30 <b>(-21.72%)</b></td><td>287.68 <b>(-25.22%)</b></td><td>270.80 <b>(-37.40%)</b></td><td>261.20 (-0.99%)</td><td>43.05 <b>(-54.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.40 (n/a)</td><td>384.70 (n/a)</td><td>432.60 (n/a)</td><td>263.80 (n/a)</td><td>94.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-8.28%)</td><td>0.02 <b>(-23.86%)</b></td><td>0.03 (-14.24%)</td><td>0.01 <b>(-39.70%)</b></td><td>0.01 <b>(+69.94%)</b></td><td>621.80 <b>(+65.86%)</b></td><td>403.94 <b>(+47.55%)</b></td><td>286.00 (+16.59%)</td><td>258.90 (+9.06%)</td><td>179.31 <b>(+208.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>374.90 (n/a)</td><td>273.76 (n/a)</td><td>245.30 (n/a)</td><td>237.40 (n/a)</td><td>58.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(+73.89%)</b></td><td>0.03 <b>(+63.47%)</b></td><td>0.03 <b>(+49.59%)</b></td><td>0.02 <b>(+443.40%)</b></td><td>0.01 (+2.92%)</td><td>456.70 <b>(-81.60%)</b></td><td>343.58 <b>(-59.45%)</b></td><td>292.50 <b>(-33.16%)</b></td><td>243.80 <b>(-42.49%)</b></td><td>102.08 <b>(-88.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2481.90 (n/a)</td><td>847.38 (n/a)</td><td>437.60 (n/a)</td><td>423.90 (n/a)</td><td>913.83 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-2.57%)</td><td>0.03 (+4.17%)</td><td>0.03 (+16.65%)</td><td>0.02 (-9.24%)</td><td>0.01 (+5.87%)</td><td>401.50 (+10.15%)</td><td>279.32 (-3.14%)</td><td>240.80 (-14.28%)</td><td>236.50 (+2.65%)</td><td>70.66 <b>(+21.66%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.50 (n/a)</td><td>288.38 (n/a)</td><td>280.90 (n/a)</td><td>230.40 (n/a)</td><td>58.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (+5.75%)</td><td>0.03 (+0.54%)</td><td>0.03 (-7.46%)</td><td>0.02 (-3.17%)</td><td>0.01 (+9.38%)</td><td>532.90 (+3.28%)</td><td>344.32 (+0.99%)</td><td>286.00 (+8.09%)</td><td>225.00 (-5.42%)</td><td>135.80 (+6.99%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.00 (n/a)</td><td>340.94 (n/a)</td><td>264.60 (n/a)</td><td>237.90 (n/a)</td><td>126.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-15.44%)</td><td>0.03 (-2.43%)</td><td>0.03 (-5.07%)</td><td>0.02 (-5.62%)</td><td>0.01 <b>(-21.66%)</b></td><td>530.60 (+5.95%)</td><td>324.86 (-0.27%)</td><td>276.30 (+5.34%)</td><td>241.10 (+18.24%)</td><td>121.02 (-4.38%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>325.74 (n/a)</td><td>262.30 (n/a)</td><td>203.90 (n/a)</td><td>126.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-13.81%)</td><td>0.02 <b>(-26.84%)</b></td><td>0.02 <b>(-37.07%)</b></td><td>0.01 (-8.08%)</td><td>0.01 <b>(-21.93%)</b></td><td>558.70 (+8.78%)</td><td>418.18 <b>(+33.84%)</b></td><td>407.50 <b>(+58.87%)</b></td><td>274.80 (+16.05%)</td><td>108.63 (-5.61%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.60 (n/a)</td><td>312.44 (n/a)</td><td>256.50 (n/a)</td><td>236.80 (n/a)</td><td>115.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-18.82%)</td><td>0.02 (-15.42%)</td><td>0.02 <b>(-26.33%)</b></td><td>0.01 (-5.77%)</td><td>0.01 <b>(-21.28%)</b></td><td>587.10 (+6.13%)</td><td>398.20 (+15.49%)</td><td>428.30 <b>(+35.75%)</b></td><td>250.20 <b>(+23.19%)</b></td><td>135.17 (-1.27%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>344.80 (n/a)</td><td>315.50 (n/a)</td><td>203.10 (n/a)</td><td>136.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+2.91%)</td><td>0.02 (+11.85%)</td><td>0.02 (+10.26%)</td><td>0.01 (+11.13%)</td><td>0.00 (-0.51%)</td><td>570.90 (-10.01%)</td><td>458.12 (-11.10%)</td><td>462.80 (-9.31%)</td><td>329.70 (-2.83%)</td><td>104.94 (-11.83%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.40 (n/a)</td><td>515.30 (n/a)</td><td>510.30 (n/a)</td><td>339.30 (n/a)</td><td>119.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-9.68%)</td><td>0.02 (-3.53%)</td><td>0.03 <b>(+47.40%)</b></td><td>0.01 <b>(-49.69%)</b></td><td>0.01 (+2.96%)</td><td>1053.10 <b>(+98.77%)</b></td><td>468.60 <b>(+20.39%)</b></td><td>305.50 <b>(-32.16%)</b></td><td>248.60 (+10.69%)</td><td>340.65 <b>(+128.36%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>389.24 (n/a)</td><td>450.30 (n/a)</td><td>224.60 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(-47.25%)</b></td><td>0.02 <b>(-33.82%)</b></td><td>0.01 <b>(-51.99%)</b></td><td>0.01 (-10.99%)</td><td>0.01 <b>(-48.19%)</b></td><td>1029.80 (+12.35%)</td><td>564.32 <b>(+30.43%)</b></td><td>576.10 <b>(+108.28%)</b></td><td>304.90 <b>(+89.61%)</b></td><td>295.51 (-2.44%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>916.60 (n/a)</td><td>432.66 (n/a)</td><td>276.60 (n/a)</td><td>160.80 (n/a)</td><td>302.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(-26.53%)</b></td><td>0.02 (-1.61%)</td><td>0.02 <b>(+37.56%)</b></td><td>0.01 <b>(-45.32%)</b></td><td>0.01 (-17.65%)</td><td>1059.30 <b>(+82.89%)</b></td><td>475.16 (+12.98%)</td><td>328.10 <b>(-27.30%)</b></td><td>247.50 <b>(+36.06%)</b></td><td>339.15 <b>(+110.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.20 (n/a)</td><td>420.56 (n/a)</td><td>451.30 (n/a)</td><td>181.90 (n/a)</td><td>160.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (+4.72%)</td><td>0.06 (+8.45%)</td><td>0.07 (+7.99%)</td><td>0.04 (+10.20%)</td><td>0.02 (-4.30%)</td><td>442.40 (-9.25%)</td><td>279.10 (-9.53%)</td><td>242.30 (-7.41%)</td><td>186.20 (-4.46%)</td><td>98.81 (-15.38%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.50 (n/a)</td><td>308.50 (n/a)</td><td>261.70 (n/a)</td><td>194.90 (n/a)</td><td>116.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+0.82%)</td><td>0.05 (+8.25%)</td><td>0.05 (+3.64%)</td><td>0.03 <b>(+200.34%)</b></td><td>0.02 <b>(-21.67%)</b></td><td>621.00 <b>(-66.71%)</b></td><td>391.36 <b>(-38.79%)</b></td><td>349.40 (-3.53%)</td><td>235.90 (-0.80%)</td><td>168.51 <b>(-75.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1865.30 (n/a)</td><td>639.36 (n/a)</td><td>362.20 (n/a)</td><td>237.80 (n/a)</td><td>692.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+3.68%)</td><td>0.05 <b>(+20.99%)</b></td><td>0.06 <b>(+49.65%)</b></td><td>0.04 <b>(+35.00%)</b></td><td>0.01 <b>(-20.39%)</b></td><td>420.80 <b>(-25.93%)</b></td><td>317.30 <b>(-21.10%)</b></td><td>282.20 <b>(-33.19%)</b></td><td>249.90 (-3.55%)</td><td>76.37 <b>(-41.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>568.10 (n/a)</td><td>402.16 (n/a)</td><td>422.40 (n/a)</td><td>259.10 (n/a)</td><td>130.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 <b>(-20.07%)</b></td><td>0.05 (-2.42%)</td><td>0.06 <b>(+52.79%)</b></td><td>0.03 (-12.02%)</td><td>0.02 <b>(-25.61%)</b></td><td>627.70 (+13.67%)</td><td>387.94 (-0.63%)</td><td>290.10 <b>(-34.56%)</b></td><td>243.10 <b>(+25.05%)</b></td><td>165.33 (+6.43%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>552.20 (n/a)</td><td>390.40 (n/a)</td><td>443.30 (n/a)</td><td>194.40 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+8.78%)</td><td>0.05 <b>(+35.95%)</b></td><td>0.05 <b>(+63.58%)</b></td><td>0.03 (+17.78%)</td><td>0.02 (+16.23%)</td><td>474.40 (-15.10%)</td><td>340.76 <b>(-25.74%)</b></td><td>298.30 <b>(-38.86%)</b></td><td>236.40 (-8.09%)</td><td>114.16 (-3.08%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.80 (n/a)</td><td>458.86 (n/a)</td><td>487.90 (n/a)</td><td>257.20 (n/a)</td><td>117.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+8.80%)</td><td>0.06 <b>(+32.83%)</b></td><td>0.06 <b>(+42.90%)</b></td><td>0.04 <b>(+20.65%)</b></td><td>0.01 (-0.15%)</td><td>443.00 (-17.12%)</td><td>297.16 <b>(-25.53%)</b></td><td>268.30 <b>(-30.02%)</b></td><td>244.20 (-8.09%)</td><td>82.36 <b>(-20.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.50 (n/a)</td><td>399.04 (n/a)</td><td>383.40 (n/a)</td><td>265.70 (n/a)</td><td>103.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 <b>(-35.08%)</b></td><td>0.04 (-16.48%)</td><td>0.03 <b>(-31.47%)</b></td><td>0.03 <b>(+259.15%)</b></td><td>0.02 <b>(-57.06%)</b></td><td>529.10 <b>(-72.16%)</b></td><td>426.26 <b>(-33.18%)</b></td><td>475.20 <b>(+45.90%)</b></td><td>241.00 <b>(+54.09%)</b></td><td>113.06 <b>(-84.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1900.40 (n/a)</td><td>637.94 (n/a)</td><td>325.70 (n/a)</td><td>156.40 (n/a)</td><td>715.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (-15.33%)</td><td>0.05 <b>(-23.33%)</b></td><td>0.04 <b>(-36.78%)</b></td><td>0.03 (+2.47%)</td><td>0.02 <b>(-31.72%)</b></td><td>572.70 (-2.42%)</td><td>410.76 <b>(+20.44%)</b></td><td>382.40 <b>(+58.21%)</b></td><td>233.70 (+18.09%)</td><td>154.74 (-13.76%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>586.90 (n/a)</td><td>341.04 (n/a)</td><td>241.70 (n/a)</td><td>197.90 (n/a)</td><td>179.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 <b>(-30.89%)</b></td><td>0.05 (-6.53%)</td><td>0.05 (-4.94%)</td><td>0.03 (-3.95%)</td><td>0.02 <b>(-36.37%)</b></td><td>630.60 (+4.11%)</td><td>354.20 (-0.21%)</td><td>302.50 (+5.18%)</td><td>227.30 <b>(+44.68%)</b></td><td>165.19 (-4.63%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>605.70 (n/a)</td><td>354.96 (n/a)</td><td>287.60 (n/a)</td><td>157.10 (n/a)</td><td>173.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 <b>(-27.42%)</b></td><td>0.05 <b>(-20.06%)</b></td><td>0.04 <b>(-35.46%)</b></td><td>0.03 (+19.73%)</td><td>0.01 <b>(-49.48%)</b></td><td>469.20 (-16.48%)</td><td>379.36 (+9.29%)</td><td>423.50 <b>(+54.96%)</b></td><td>251.00 <b>(+37.84%)</b></td><td>97.30 <b>(-43.65%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>561.80 (n/a)</td><td>347.12 (n/a)</td><td>273.30 (n/a)</td><td>182.10 (n/a)</td><td>172.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (+0.96%)</td><td>0.04 (+6.09%)</td><td>0.04 (+10.38%)</td><td>0.03 (+17.04%)</td><td>0.01 (-9.79%)</td><td>521.00 (-14.56%)</td><td>432.22 (-6.66%)</td><td>416.60 (-9.40%)</td><td>341.40 (-0.96%)</td><td>74.43 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>609.80 (n/a)</td><td>463.08 (n/a)</td><td>459.80 (n/a)</td><td>344.70 (n/a)</td><td>96.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+7.54%)</td><td>0.05 <b>(+22.16%)</b></td><td>0.06 <b>(+42.37%)</b></td><td>0.03 (+7.87%)</td><td>0.02 <b>(+22.06%)</b></td><td>540.10 (-7.29%)</td><td>358.30 (-16.22%)</td><td>280.00 <b>(-29.75%)</b></td><td>241.70 (-7.00%)</td><td>136.18 (+3.67%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.60 (n/a)</td><td>427.68 (n/a)</td><td>398.60 (n/a)</td><td>259.90 (n/a)</td><td>131.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (+3.30%)</td><td>0.10 (-10.70%)</td><td>0.11 (-11.51%)</td><td>0.06 (-12.34%)</td><td>0.03 <b>(+24.74%)</b></td><td>526.40 (+14.06%)</td><td>367.14 (+16.48%)</td><td>300.60 (+13.01%)</td><td>242.80 (-3.23%)</td><td>127.19 <b>(+43.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.50 (n/a)</td><td>315.20 (n/a)</td><td>266.00 (n/a)</td><td>250.90 (n/a)</td><td>88.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (+10.12%)</td><td>0.12 <b>(+24.68%)</b></td><td>0.13 (+18.92%)</td><td>0.09 <b>(+41.54%)</b></td><td>0.02 <b>(-26.18%)</b></td><td>361.40 <b>(-29.36%)</b></td><td>282.20 <b>(-23.04%)</b></td><td>254.20 (-15.91%)</td><td>245.80 (-9.20%)</td><td>49.77 <b>(-53.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>511.60 (n/a)</td><td>366.68 (n/a)</td><td>302.30 (n/a)</td><td>270.70 (n/a)</td><td>107.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (-0.41%)</td><td>0.09 (+4.90%)</td><td>0.09 <b>(+25.43%)</b></td><td>0.05 (+2.40%)</td><td>0.03 <b>(-21.98%)</b></td><td>608.30 (-2.34%)</td><td>381.94 (-9.10%)</td><td>356.60 <b>(-20.28%)</b></td><td>247.00 (+0.45%)</td><td>137.74 (-16.26%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>622.90 (n/a)</td><td>420.16 (n/a)</td><td>447.30 (n/a)</td><td>245.90 (n/a)</td><td>164.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 <b>(+26.05%)</b></td><td>0.12 (+12.97%)</td><td>0.13 (+14.61%)</td><td>0.06 (-2.28%)</td><td>0.04 <b>(+35.48%)</b></td><td>543.80 (+2.31%)</td><td>324.40 (-7.60%)</td><td>247.70 (-12.75%)</td><td>196.20 <b>(-20.66%)</b></td><td>141.97 (+13.78%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>531.50 (n/a)</td><td>351.08 (n/a)</td><td>283.90 (n/a)</td><td>247.30 (n/a)</td><td>124.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (+17.96%)</td><td>0.08 (-12.01%)</td><td>0.06 (-15.10%)</td><td>0.06 (-5.52%)</td><td>0.04 <b>(+26.89%)</b></td><td>592.50 (+5.84%)</td><td>484.42 (+18.05%)</td><td>533.70 (+17.79%)</td><td>229.30 (-15.23%)</td><td>148.80 (+15.46%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.80 (n/a)</td><td>410.36 (n/a)</td><td>453.10 (n/a)</td><td>270.50 (n/a)</td><td>128.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 <b>(+53.83%)</b></td><td>0.11 (+12.78%)</td><td>0.07 (-12.46%)</td><td>0.06 (-16.47%)</td><td>0.06 <b>(+168.40%)</b></td><td>520.00 (+19.71%)</td><td>374.70 (+3.87%)</td><td>455.80 (+14.24%)</td><td>170.00 <b>(-34.99%)</b></td><td>158.75 <b>(+115.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>434.40 (n/a)</td><td>360.74 (n/a)</td><td>399.00 (n/a)</td><td>261.50 (n/a)</td><td>73.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (-3.42%)</td><td>0.10 (+3.72%)</td><td>0.07 (-13.13%)</td><td>0.06 (+9.80%)</td><td>0.04 (+7.21%)</td><td>521.20 (-8.93%)</td><td>385.14 (-2.91%)</td><td>462.70 (+15.10%)</td><td>235.70 (+3.56%)</td><td>135.47 (-3.17%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>572.30 (n/a)</td><td>396.68 (n/a)</td><td>402.00 (n/a)</td><td>227.60 (n/a)</td><td>139.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (+14.70%)</td><td>0.10 (+19.72%)</td><td>0.12 <b>(+55.86%)</b></td><td>0.06 (+8.60%)</td><td>0.03 <b>(+47.14%)</b></td><td>537.60 (-7.93%)</td><td>365.60 (-12.49%)</td><td>267.70 <b>(-35.85%)</b></td><td>259.40 (-12.84%)</td><td>140.68 (+19.58%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>583.90 (n/a)</td><td>417.80 (n/a)</td><td>417.30 (n/a)</td><td>297.60 (n/a)</td><td>117.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 <b>(+80.71%)</b></td><td>0.11 <b>(+52.45%)</b></td><td>0.13 <b>(+95.74%)</b></td><td>0.06 (-6.61%)</td><td>0.04 <b>(+468.70%)</b></td><td>553.20 (+7.08%)</td><td>357.06 <b>(-24.03%)</b></td><td>249.60 <b>(-48.92%)</b></td><td>221.60 <b>(-44.66%)</b></td><td>163.16 <b>(+248.75%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>516.60 (n/a)</td><td>470.00 (n/a)</td><td>488.60 (n/a)</td><td>400.40 (n/a)</td><td>46.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (+11.01%)</td><td>0.12 <b>(+32.99%)</b></td><td>0.13 <b>(+29.31%)</b></td><td>0.10 <b>(+63.39%)</b></td><td>0.02 <b>(-39.10%)</b></td><td>344.50 <b>(-38.79%)</b></td><td>273.78 <b>(-29.51%)</b></td><td>257.70 <b>(-22.68%)</b></td><td>242.40 (-9.92%)</td><td>42.68 <b>(-66.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.80 (n/a)</td><td>388.40 (n/a)</td><td>333.30 (n/a)</td><td>269.10 (n/a)</td><td>128.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (-8.28%)</td><td>0.08 (+15.28%)</td><td>0.09 <b>(+35.15%)</b></td><td>0.07 <b>(+36.97%)</b></td><td>0.02 <b>(-32.29%)</b></td><td>498.80 <b>(-27.00%)</b></td><td>404.04 (-17.58%)</td><td>381.00 <b>(-26.01%)</b></td><td>304.50 (+9.02%)</td><td>86.58 <b>(-41.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>683.30 (n/a)</td><td>490.22 (n/a)</td><td>514.90 (n/a)</td><td>279.30 (n/a)</td><td>147.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 <b>(+103.73%)</b></td><td>0.11 <b>(+63.07%)</b></td><td>0.11 <b>(+58.93%)</b></td><td>0.07 <b>(+21.40%)</b></td><td>0.03 <b>(+320.07%)</b></td><td>499.50 (-17.62%)</td><td>327.72 <b>(-34.79%)</b></td><td>307.40 <b>(-37.09%)</b></td><td>217.30 <b>(-50.93%)</b></td><td>104.79 <b>(+70.88%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>606.30 (n/a)</td><td>502.56 (n/a)</td><td>488.60 (n/a)</td><td>442.80 (n/a)</td><td>61.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (-16.20%)</td><td>0.06 <b>(-27.65%)</b></td><td>0.08 (-17.48%)</td><td>0.01 <b>(-74.13%)</b></td><td>0.03 <b>(+38.02%)</b></td><td>1914.20 <b>(+286.47%)</b></td><td>654.14 <b>(+115.80%)</b></td><td>298.00 <b>(+21.19%)</b></td><td>279.10 (+19.32%)</td><td>709.41 <b>(+541.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>495.30 (n/a)</td><td>303.12 (n/a)</td><td>245.90 (n/a)</td><td>233.90 (n/a)</td><td>110.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 <b>(-29.05%)</b></td><td>0.13 <b>(-21.14%)</b></td><td>0.12 <b>(-32.89%)</b></td><td>0.10 (-17.78%)</td><td>0.03 <b>(-34.93%)</b></td><td>507.50 <b>(+21.62%)</b></td><td>390.72 <b>(+23.91%)</b></td><td>417.10 <b>(+49.02%)</b></td><td>296.90 <b>(+40.98%)</b></td><td>91.49 (-0.06%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>417.30 (n/a)</td><td>315.32 (n/a)</td><td>279.90 (n/a)</td><td>210.60 (n/a)</td><td>91.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.23 <b>(-26.27%)</b></td><td>2.83 (-11.14%)</td><td>2.64 (-2.68%)</td><td>2.57 (-1.09%)</td><td>0.33 <b>(-58.65%)</b></td><td>4083.50 (+1.10%)</td><td>3743.96 (+8.84%)</td><td>3974.90 (+2.75%)</td><td>3242.80 <b>(+35.63%)</b></td><td>414.57 <b>(-44.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.39 (n/a)</td><td>3.18 (n/a)</td><td>2.71 (n/a)</td><td>2.60 (n/a)</td><td>0.79 (n/a)</td><td>4039.20 (n/a)</td><td>3440.02 (n/a)</td><td>3868.50 (n/a)</td><td>2390.90 (n/a)</td><td>745.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 <b>(-27.31%)</b></td><td>0.09 <b>(-37.25%)</b></td><td>0.09 <b>(-44.91%)</b></td><td>0.03 <b>(-59.97%)</b></td><td>0.04 (-2.24%)</td><td>1368.50 <b>(+149.82%)</b></td><td>594.56 <b>(+91.58%)</b></td><td>477.90 <b>(+81.50%)</b></td><td>294.50 <b>(+37.55%)</b></td><td>441.98 <b>(+227.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>547.80 (n/a)</td><td>310.34 (n/a)</td><td>263.30 (n/a)</td><td>214.10 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(+25.62%)</b></td><td>0.02 <b>(+23.52%)</b></td><td>0.02 (+9.08%)</td><td>0.01 <b>(+29.78%)</b></td><td>0.00 (+2.48%)</td><td>384.80 <b>(-22.95%)</b></td><td>282.00 <b>(-21.34%)</b></td><td>270.30 (-8.34%)</td><td>196.40 <b>(-20.42%)</b></td><td>67.74 <b>(-39.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.40 (n/a)</td><td>358.50 (n/a)</td><td>294.90 (n/a)</td><td>246.80 (n/a)</td><td>111.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-0.30%)</td><td>0.01 (-14.04%)</td><td>0.01 <b>(-27.33%)</b></td><td>0.01 <b>(+104.84%)</b></td><td>0.00 <b>(-34.38%)</b></td><td>567.70 <b>(-51.18%)</b></td><td>440.48 (-8.04%)</td><td>461.60 <b>(+37.59%)</b></td><td>266.50 (+0.30%)</td><td>109.12 <b>(-71.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1162.90 (n/a)</td><td>478.98 (n/a)</td><td>335.50 (n/a)</td><td>265.70 (n/a)</td><td>384.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 <b>(+26.47%)</b></td><td>0.02 (+2.42%)</td><td>0.01 (+0.13%)</td><td>0.01 (-5.40%)</td><td>0.01 <b>(+39.18%)</b></td><td>653.20 (+5.70%)</td><td>426.84 (+1.96%)</td><td>437.10 (-0.14%)</td><td>224.90 <b>(-20.92%)</b></td><td>158.11 (+17.33%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.00 (n/a)</td><td>418.64 (n/a)</td><td>437.70 (n/a)</td><td>284.40 (n/a)</td><td>134.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+44.26%)</b></td><td>0.01 (-1.42%)</td><td>0.01 <b>(-20.02%)</b></td><td>0.01 (+19.03%)</td><td>0.01 <b>(+56.50%)</b></td><td>513.80 (-15.99%)</td><td>369.28 (+4.81%)</td><td>350.80 <b>(+25.02%)</b></td><td>186.90 <b>(-30.68%)</b></td><td>132.39 (-9.86%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.60 (n/a)</td><td>352.34 (n/a)</td><td>280.60 (n/a)</td><td>269.60 (n/a)</td><td>146.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+36.19%)</b></td><td>0.01 (+10.05%)</td><td>0.01 (-8.43%)</td><td>0.00 <b>(-34.62%)</b></td><td>0.01 <b>(+93.13%)</b></td><td>1077.40 <b>(+52.95%)</b></td><td>550.42 (+9.39%)</td><td>521.50 (+9.21%)</td><td>228.80 <b>(-26.55%)</b></td><td>323.47 <b>(+121.27%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>704.40 (n/a)</td><td>503.16 (n/a)</td><td>477.50 (n/a)</td><td>311.50 (n/a)</td><td>146.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(+40.46%)</b></td><td>0.01 <b>(+20.47%)</b></td><td>0.01 (+9.60%)</td><td>0.01 (+7.20%)</td><td>0.00 <b>(+143.35%)</b></td><td>487.80 (-6.71%)</td><td>404.02 (-14.48%)</td><td>447.50 (-8.77%)</td><td>291.80 <b>(-28.79%)</b></td><td>85.66 <b>(+61.93%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.90 (n/a)</td><td>472.44 (n/a)</td><td>490.50 (n/a)</td><td>409.80 (n/a)</td><td>52.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-18.06%)</td><td>0.01 <b>(-21.51%)</b></td><td>0.01 <b>(-40.96%)</b></td><td>0.01 <b>(+22.33%)</b></td><td>0.00 <b>(-39.34%)</b></td><td>603.90 (-18.26%)</td><td>450.80 (+10.83%)</td><td>463.70 <b>(+69.36%)</b></td><td>258.30 <b>(+22.01%)</b></td><td>124.31 <b>(-44.75%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>738.80 (n/a)</td><td>406.76 (n/a)</td><td>273.80 (n/a)</td><td>211.70 (n/a)</td><td>224.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(-25.62%)</b></td><td>0.01 <b>(-29.75%)</b></td><td>0.01 <b>(-38.44%)</b></td><td>0.01 (-10.11%)</td><td>0.00 <b>(-42.16%)</b></td><td>524.00 (+11.25%)</td><td>443.52 <b>(+38.76%)</b></td><td>465.90 <b>(+62.45%)</b></td><td>336.10 <b>(+34.44%)</b></td><td>72.74 (-17.79%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.00 (n/a)</td><td>319.62 (n/a)</td><td>286.80 (n/a)</td><td>250.00 (n/a)</td><td>88.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+43.04%)</b></td><td>0.01 <b>(+43.47%)</b></td><td>0.01 <b>(+55.49%)</b></td><td>0.01 <b>(+67.18%)</b></td><td>0.00 <b>(+49.47%)</b></td><td>601.90 <b>(-40.19%)</b></td><td>425.28 <b>(-30.28%)</b></td><td>361.90 <b>(-35.69%)</b></td><td>248.30 <b>(-30.10%)</b></td><td>153.84 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1006.30 (n/a)</td><td>609.96 (n/a)</td><td>562.70 (n/a)</td><td>355.20 (n/a)</td><td>239.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+11.17%)</td><td>0.01 (-1.88%)</td><td>0.01 <b>(-24.82%)</b></td><td>0.01 (-1.05%)</td><td>0.00 (+7.43%)</td><td>624.50 (+1.07%)</td><td>419.72 (+1.96%)</td><td>469.60 <b>(+33.03%)</b></td><td>231.30 (-10.04%)</td><td>159.19 (-5.22%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.90 (n/a)</td><td>411.66 (n/a)</td><td>353.00 (n/a)</td><td>257.10 (n/a)</td><td>167.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-13.74%)</td><td>0.01 (-12.99%)</td><td>0.01 (-10.11%)</td><td>0.01 <b>(+192.42%)</b></td><td>0.01 <b>(-28.18%)</b></td><td>676.30 <b>(-65.80%)</b></td><td>510.52 <b>(-26.87%)</b></td><td>553.90 (+11.25%)</td><td>206.20 (+15.91%)</td><td>181.11 <b>(-75.25%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1977.60 (n/a)</td><td>698.10 (n/a)</td><td>497.90 (n/a)</td><td>177.90 (n/a)</td><td>731.83 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 <b>(-31.23%)</b></td><td>0.01 (-13.38%)</td><td>0.01 (-16.06%)</td><td>0.01 (-1.67%)</td><td>0.00 <b>(-51.88%)</b></td><td>569.00 (+1.70%)</td><td>452.94 (+9.07%)</td><td>444.50 (+19.11%)</td><td>369.20 <b>(+45.41%)</b></td><td>86.49 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.50 (n/a)</td><td>415.26 (n/a)</td><td>373.20 (n/a)</td><td>253.90 (n/a)</td><td>130.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-16.21%)</td><td>0.02 (-11.10%)</td><td>0.02 (-12.36%)</td><td>0.02 (+8.64%)</td><td>0.01 <b>(-26.38%)</b></td><td>544.10 (-7.95%)</td><td>435.50 (+8.01%)</td><td>488.70 (+14.13%)</td><td>262.80 (+19.35%)</td><td>117.67 (-16.79%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.10 (n/a)</td><td>403.22 (n/a)</td><td>428.20 (n/a)</td><td>220.20 (n/a)</td><td>141.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (+6.16%)</td><td>0.03 (-4.10%)</td><td>0.03 <b>(-20.27%)</b></td><td>0.02 (-2.02%)</td><td>0.01 (-1.02%)</td><td>562.00 (+2.05%)</td><td>387.54 (+3.77%)</td><td>373.70 <b>(+25.44%)</b></td><td>257.60 (-5.81%)</td><td>120.96 (-3.50%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>550.70 (n/a)</td><td>373.46 (n/a)</td><td>297.90 (n/a)</td><td>273.50 (n/a)</td><td>125.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (+4.57%)</td><td>0.02 (-9.48%)</td><td>0.02 (-15.20%)</td><td>0.01 <b>(-38.75%)</b></td><td>0.01 <b>(+24.70%)</b></td><td>847.60 <b>(+63.28%)</b></td><td>474.26 <b>(+23.32%)</b></td><td>465.60 (+17.93%)</td><td>219.20 (-4.36%)</td><td>243.84 <b>(+86.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.10 (n/a)</td><td>384.58 (n/a)</td><td>394.80 (n/a)</td><td>229.20 (n/a)</td><td>130.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-9.43%)</td><td>0.03 (+16.70%)</td><td>0.02 (+1.62%)</td><td>0.02 <b>(+44.47%)</b></td><td>0.01 <b>(-33.59%)</b></td><td>450.90 <b>(-30.79%)</b></td><td>373.60 <b>(-20.25%)</b></td><td>416.70 (-1.58%)</td><td>284.60 (+10.40%)</td><td>78.12 <b>(-51.59%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>651.50 (n/a)</td><td>468.44 (n/a)</td><td>423.40 (n/a)</td><td>257.80 (n/a)</td><td>161.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-18.99%)</td><td>0.02 (-6.61%)</td><td>0.02 (-18.22%)</td><td>0.01 (-1.28%)</td><td>0.01 (-7.47%)</td><td>610.40 (+1.29%)</td><td>434.98 (+8.23%)</td><td>506.50 <b>(+22.28%)</b></td><td>229.60 <b>(+23.44%)</b></td><td>191.28 (+10.44%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.60 (n/a)</td><td>401.90 (n/a)</td><td>414.20 (n/a)</td><td>186.00 (n/a)</td><td>173.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-0.56%)</td><td>0.02 <b>(-27.15%)</b></td><td>0.02 <b>(-44.35%)</b></td><td>0.02 (+0.83%)</td><td>0.01 (-2.54%)</td><td>614.10 (-0.82%)</td><td>490.58 <b>(+36.33%)</b></td><td>537.10 <b>(+79.69%)</b></td><td>232.30 (+0.56%)</td><td>154.35 (-4.61%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.20 (n/a)</td><td>359.86 (n/a)</td><td>298.90 (n/a)</td><td>231.00 (n/a)</td><td>161.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+71.67%)</b></td><td>0.03 <b>(+23.53%)</b></td><td>0.02 <b>(-33.66%)</b></td><td>0.02 <b>(+23.77%)</b></td><td>0.02 <b>(+80.11%)</b></td><td>529.70 (-19.20%)</td><td>372.42 (-13.69%)</td><td>450.10 <b>(+50.74%)</b></td><td>156.90 <b>(-41.74%)</b></td><td>164.89 (-16.72%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.60 (n/a)</td><td>431.48 (n/a)</td><td>298.60 (n/a)</td><td>269.30 (n/a)</td><td>197.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+40.77%)</b></td><td>0.03 <b>(+21.05%)</b></td><td>0.02 (-2.90%)</td><td>0.02 <b>(+331.28%)</b></td><td>0.01 (+8.97%)</td><td>571.70 <b>(-76.81%)</b></td><td>410.28 <b>(-48.48%)</b></td><td>441.50 (+2.99%)</td><td>196.90 <b>(-28.97%)</b></td><td>135.79 <b>(-85.50%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2465.70 (n/a)</td><td>796.40 (n/a)</td><td>428.70 (n/a)</td><td>277.20 (n/a)</td><td>936.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 <b>(+32.76%)</b></td><td>0.02 (+16.29%)</td><td>0.03 <b>(+96.30%)</b></td><td>0.00 <b>(-69.10%)</b></td><td>0.02 <b>(+148.97%)</b></td><td>1880.20 <b>(+223.61%)</b></td><td>898.08 <b>(+90.52%)</b></td><td>285.50 <b>(-49.05%)</b></td><td>212.00 <b>(-24.66%)</b></td><td>892.28 <b>(+554.22%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.00 (n/a)</td><td>471.38 (n/a)</td><td>560.40 (n/a)</td><td>281.40 (n/a)</td><td>136.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (-3.86%)</td><td>0.02 (-7.64%)</td><td>0.02 (-19.77%)</td><td>0.01 (-6.79%)</td><td>0.01 (-1.42%)</td><td>632.70 (+7.29%)</td><td>473.56 (+8.76%)</td><td>528.30 <b>(+24.63%)</b></td><td>243.50 (+4.02%)</td><td>148.06 (+5.17%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>435.40 (n/a)</td><td>423.90 (n/a)</td><td>234.10 (n/a)</td><td>140.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (-11.57%)</td><td>0.02 (-18.65%)</td><td>0.02 (-19.86%)</td><td>0.01 <b>(-32.31%)</b></td><td>0.01 <b>(+20.13%)</b></td><td>682.30 <b>(+47.72%)</b></td><td>504.08 <b>(+29.42%)</b></td><td>525.00 <b>(+24.79%)</b></td><td>309.50 (+13.08%)</td><td>159.83 <b>(+99.88%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.90 (n/a)</td><td>389.50 (n/a)</td><td>420.70 (n/a)</td><td>273.70 (n/a)</td><td>79.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(+26.25%)</b></td><td>0.06 <b>(+44.02%)</b></td><td>0.07 <b>(+82.89%)</b></td><td>0.03 (+4.25%)</td><td>0.02 <b>(+37.78%)</b></td><td>542.10 (-4.09%)</td><td>304.96 <b>(-27.63%)</b></td><td>248.20 <b>(-45.33%)</b></td><td>197.80 <b>(-20.82%)</b></td><td>138.31 (+13.11%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.20 (n/a)</td><td>421.40 (n/a)</td><td>454.00 (n/a)</td><td>249.80 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (-2.00%)</td><td>0.07 (+1.62%)</td><td>0.05 (+5.50%)</td><td>0.04 (+14.05%)</td><td>0.02 (-17.58%)</td><td>562.30 (-12.32%)</td><td>409.04 (-6.66%)</td><td>463.10 (-5.20%)</td><td>246.80 (+2.03%)</td><td>129.05 <b>(-25.04%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>641.30 (n/a)</td><td>438.24 (n/a)</td><td>488.50 (n/a)</td><td>241.90 (n/a)</td><td>172.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (-7.53%)</td><td>0.05 (+16.75%)</td><td>0.06 (+6.18%)</td><td>0.03 <b>(+257.86%)</b></td><td>0.02 <b>(-33.38%)</b></td><td>557.70 <b>(-72.06%)</b></td><td>344.32 <b>(-48.97%)</b></td><td>272.90 (-5.80%)</td><td>233.60 (+8.15%)</td><td>141.21 <b>(-81.28%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1995.90 (n/a)</td><td>674.78 (n/a)</td><td>289.70 (n/a)</td><td>216.00 (n/a)</td><td>754.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-12.63%)</td><td>0.05 (-15.48%)</td><td>0.04 (-2.03%)</td><td>0.03 (-16.75%)</td><td>0.02 (-17.38%)</td><td>684.20 <b>(+20.14%)</b></td><td>465.12 (+18.25%)</td><td>461.40 (+2.08%)</td><td>271.80 (+14.49%)</td><td>179.56 <b>(+21.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.50 (n/a)</td><td>393.32 (n/a)</td><td>452.00 (n/a)</td><td>237.40 (n/a)</td><td>147.72 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 <b>(-22.76%)</b></td><td>0.04 (+4.17%)</td><td>0.05 <b>(+37.94%)</b></td><td>0.03 (+8.44%)</td><td>0.01 <b>(-44.81%)</b></td><td>550.10 (-7.79%)</td><td>388.84 (-11.33%)</td><td>353.00 <b>(-27.50%)</b></td><td>272.80 <b>(+29.47%)</b></td><td>105.02 <b>(-29.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>596.60 (n/a)</td><td>438.54 (n/a)</td><td>486.90 (n/a)</td><td>210.70 (n/a)</td><td>149.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 <b>(+42.63%)</b></td><td>0.06 (+19.03%)</td><td>0.04 (+3.67%)</td><td>0.03 (-10.14%)</td><td>0.03 <b>(+97.01%)</b></td><td>687.90 (+11.27%)</td><td>460.86 (+0.03%)</td><td>496.90 (-3.53%)</td><td>190.90 <b>(-29.87%)</b></td><td>233.37 <b>(+61.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.20 (n/a)</td><td>460.70 (n/a)</td><td>515.10 (n/a)</td><td>272.20 (n/a)</td><td>144.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+80.87%)</b></td><td>0.06 <b>(+50.22%)</b></td><td>0.07 <b>(+65.29%)</b></td><td>0.03 <b>(+20.74%)</b></td><td>0.03 <b>(+154.89%)</b></td><td>510.70 (-17.17%)</td><td>335.76 <b>(-25.10%)</b></td><td>251.70 <b>(-39.50%)</b></td><td>175.50 <b>(-44.71%)</b></td><td>156.97 <b>(+27.95%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>616.60 (n/a)</td><td>448.28 (n/a)</td><td>416.00 (n/a)</td><td>317.40 (n/a)</td><td>122.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+90.22%)</b></td><td>0.05 <b>(+25.59%)</b></td><td>0.04 (-0.98%)</td><td>0.04 (+13.05%)</td><td>0.02 <b>(+276.64%)</b></td><td>507.30 (-11.54%)</td><td>413.68 (-12.58%)</td><td>454.70 (+0.98%)</td><td>203.10 <b>(-47.44%)</b></td><td>120.79 <b>(+63.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.50 (n/a)</td><td>473.20 (n/a)</td><td>450.30 (n/a)</td><td>386.40 (n/a)</td><td>73.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (+0.53%)</td><td>0.04 (-15.33%)</td><td>0.04 <b>(-32.42%)</b></td><td>0.01 <b>(-69.39%)</b></td><td>0.02 <b>(+20.56%)</b></td><td>1927.50 <b>(+226.64%)</b></td><td>672.52 <b>(+72.26%)</b></td><td>413.80 <b>(+47.94%)</b></td><td>237.70 (-0.50%)</td><td>708.46 <b>(+307.74%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.10 (n/a)</td><td>390.40 (n/a)</td><td>279.70 (n/a)</td><td>238.90 (n/a)</td><td>173.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 <b>(-57.01%)</b></td><td>0.04 <b>(-24.89%)</b></td><td>0.04 (-0.03%)</td><td>0.03 (+2.55%)</td><td>0.00 <b>(-82.77%)</b></td><td>595.40 (-2.49%)</td><td>485.06 (+14.27%)</td><td>449.90 (+0.02%)</td><td>434.70 <b>(+132.58%)</b></td><td>66.76 <b>(-58.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>610.60 (n/a)</td><td>424.50 (n/a)</td><td>449.80 (n/a)</td><td>186.90 (n/a)</td><td>160.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 <b>(+27.27%)</b></td><td>0.03 (+3.04%)</td><td>0.03 (-7.79%)</td><td>0.03 (-1.69%)</td><td>0.01 <b>(+125.60%)</b></td><td>620.50 (+1.72%)</td><td>555.80 (+0.51%)</td><td>600.40 (+8.43%)</td><td>353.60 <b>(-21.42%)</b></td><td>113.68 <b>(+78.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>610.00 (n/a)</td><td>552.96 (n/a)</td><td>553.70 (n/a)</td><td>450.00 (n/a)</td><td>63.72 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (-1.32%)</td><td>0.09 (-8.73%)</td><td>0.09 (-13.64%)</td><td>0.06 (-2.97%)</td><td>0.03 (-14.87%)</td><td>551.60 (+3.06%)</td><td>405.82 (+6.95%)</td><td>356.10 (+15.80%)</td><td>262.60 (+1.31%)</td><td>120.57 (-11.27%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>535.20 (n/a)</td><td>379.44 (n/a)</td><td>307.50 (n/a)</td><td>259.20 (n/a)</td><td>135.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 <b>(-31.19%)</b></td><td>0.09 (-8.93%)</td><td>0.08 <b>(+45.71%)</b></td><td>0.06 (+17.87%)</td><td>0.03 <b>(-51.50%)</b></td><td>538.20 (-15.16%)</td><td>406.44 (-10.69%)</td><td>410.80 <b>(-31.36%)</b></td><td>250.30 <b>(+45.35%)</b></td><td>131.68 <b>(-42.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>634.40 (n/a)</td><td>455.10 (n/a)</td><td>598.50 (n/a)</td><td>172.20 (n/a)</td><td>229.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (-6.19%)</td><td>0.10 (+2.66%)</td><td>0.08 (+18.46%)</td><td>0.06 (+0.99%)</td><td>0.04 (-15.52%)</td><td>671.40 (-0.97%)</td><td>447.46 (-7.71%)</td><td>492.70 (-15.59%)</td><td>270.20 (+6.59%)</td><td>174.83 (-16.32%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>678.00 (n/a)</td><td>484.82 (n/a)</td><td>583.70 (n/a)</td><td>253.50 (n/a)</td><td>208.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 <b>(-35.17%)</b></td><td>0.07 <b>(-34.68%)</b></td><td>0.07 <b>(-40.50%)</b></td><td>0.03 <b>(-41.38%)</b></td><td>0.03 <b>(-40.33%)</b></td><td>1062.60 <b>(+70.59%)</b></td><td>569.96 <b>(+50.94%)</b></td><td>503.70 <b>(+68.07%)</b></td><td>301.20 <b>(+54.22%)</b></td><td>288.63 <b>(+61.09%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>622.90 (n/a)</td><td>377.60 (n/a)</td><td>299.70 (n/a)</td><td>195.30 (n/a)</td><td>179.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 <b>(-38.66%)</b></td><td>0.09 (+5.68%)</td><td>0.09 <b>(+23.01%)</b></td><td>0.07 <b>(+335.46%)</b></td><td>0.01 <b>(-79.28%)</b></td><td>576.60 <b>(-77.04%)</b></td><td>482.48 <b>(-45.03%)</b></td><td>459.30 (-18.69%)</td><td>409.70 <b>(+63.03%)</b></td><td>63.48 <b>(-93.12%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2510.90 (n/a)</td><td>877.78 (n/a)</td><td>564.90 (n/a)</td><td>251.30 (n/a)</td><td>922.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (+0.98%)</td><td>0.09 (+5.30%)</td><td>0.07 (+11.50%)</td><td>0.06 <b>(+101.37%)</b></td><td>0.04 <b>(-23.37%)</b></td><td>537.50 <b>(-50.34%)</b></td><td>408.10 <b>(-22.34%)</b></td><td>437.70 (-10.31%)</td><td>215.70 (-0.96%)</td><td>136.13 <b>(-60.51%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1082.40 (n/a)</td><td>525.50 (n/a)</td><td>488.00 (n/a)</td><td>217.80 (n/a)</td><td>344.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 <b>(-36.40%)</b></td><td>0.07 <b>(-36.55%)</b></td><td>0.06 <b>(-23.15%)</b></td><td>0.05 <b>(-27.59%)</b></td><td>0.03 <b>(-44.47%)</b></td><td>807.30 <b>(+38.12%)</b></td><td>585.66 <b>(+47.50%)</b></td><td>603.10 <b>(+30.15%)</b></td><td>289.30 <b>(+57.23%)</b></td><td>195.37 (+14.86%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>584.50 (n/a)</td><td>397.06 (n/a)</td><td>463.40 (n/a)</td><td>184.00 (n/a)</td><td>170.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 <b>(+45.69%)</b></td><td>0.09 <b>(+42.71%)</b></td><td>0.07 (+17.77%)</td><td>0.06 <b>(+236.56%)</b></td><td>0.04 (+15.71%)</td><td>535.40 <b>(-70.29%)</b></td><td>421.44 <b>(-44.98%)</b></td><td>488.90 (-15.09%)</td><td>213.20 <b>(-31.34%)</b></td><td>130.21 <b>(-78.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1801.90 (n/a)</td><td>765.94 (n/a)</td><td>575.80 (n/a)</td><td>310.50 (n/a)</td><td>600.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(-46.50%)</b></td><td>0.07 (-12.17%)</td><td>0.07 (+5.53%)</td><td>0.07 (+18.51%)</td><td>0.01 <b>(-84.80%)</b></td><td>566.30 (-15.62%)</td><td>507.66 (+0.85%)</td><td>516.20 (-5.25%)</td><td>463.10 <b>(+86.96%)</b></td><td>41.22 <b>(-75.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>671.10 (n/a)</td><td>503.40 (n/a)</td><td>544.80 (n/a)</td><td>247.70 (n/a)</td><td>167.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(-34.00%)</b></td><td>0.07 (+5.65%)</td><td>0.07 <b>(+23.66%)</b></td><td>0.05 <b>(+214.26%)</b></td><td>0.01 <b>(-68.42%)</b></td><td>602.80 <b>(-68.18%)</b></td><td>477.86 <b>(-37.27%)</b></td><td>472.80 (-19.12%)</td><td>355.90 <b>(+51.51%)</b></td><td>92.14 <b>(-85.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1894.50 (n/a)</td><td>761.78 (n/a)</td><td>584.60 (n/a)</td><td>234.90 (n/a)</td><td>650.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-7.66%)</td><td>0.05 (-5.29%)</td><td>0.05 (-1.18%)</td><td>0.03 (-3.19%)</td><td>0.02 (-12.53%)</td><td>641.80 (+3.28%)</td><td>434.06 (+3.79%)</td><td>445.00 (+1.21%)</td><td>266.40 (+8.29%)</td><td>158.00 (-1.52%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.40 (n/a)</td><td>418.20 (n/a)</td><td>439.70 (n/a)</td><td>246.00 (n/a)</td><td>160.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (+19.43%)</td><td>0.06 <b>(+23.39%)</b></td><td>0.07 <b>(+37.32%)</b></td><td>0.04 (+4.50%)</td><td>0.02 <b>(+35.68%)</b></td><td>483.50 (-4.30%)</td><td>341.56 (-17.20%)</td><td>311.50 <b>(-27.19%)</b></td><td>234.20 (-16.30%)</td><td>100.84 (+10.09%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>505.20 (n/a)</td><td>412.52 (n/a)</td><td>427.80 (n/a)</td><td>279.80 (n/a)</td><td>91.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (+15.32%)</td><td>0.06 <b>(+40.53%)</b></td><td>0.05 (+6.85%)</td><td>0.04 <b>(+260.57%)</b></td><td>0.02 (-7.83%)</td><td>514.70 <b>(-72.27%)</b></td><td>383.22 <b>(-47.18%)</b></td><td>439.90 (-6.40%)</td><td>251.30 (-13.29%)</td><td>118.76 <b>(-81.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1855.90 (n/a)</td><td>725.54 (n/a)</td><td>470.00 (n/a)</td><td>289.80 (n/a)</td><td>639.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (-16.66%)</td><td>0.05 <b>(-33.00%)</b></td><td>0.04 <b>(-43.00%)</b></td><td>0.02 <b>(-55.99%)</b></td><td>0.02 <b>(+23.54%)</b></td><td>1062.90 <b>(+127.26%)</b></td><td>530.62 <b>(+75.13%)</b></td><td>489.90 <b>(+75.47%)</b></td><td>275.90 <b>(+20.01%)</b></td><td>316.00 <b>(+228.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>467.70 (n/a)</td><td>302.98 (n/a)</td><td>279.20 (n/a)</td><td>229.90 (n/a)</td><td>96.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-4.20%)</td><td>0.05 (-3.92%)</td><td>0.04 (-12.60%)</td><td>0.04 <b>(+234.94%)</b></td><td>0.02 <b>(-42.05%)</b></td><td>575.70 <b>(-70.14%)</b></td><td>472.46 <b>(-34.72%)</b></td><td>508.50 (+14.42%)</td><td>258.50 (+4.36%)</td><td>123.15 <b>(-82.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1928.20 (n/a)</td><td>723.76 (n/a)</td><td>444.40 (n/a)</td><td>247.70 (n/a)</td><td>701.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (+3.65%)</td><td>0.06 (-6.61%)</td><td>0.05 <b>(-25.20%)</b></td><td>0.04 (+10.83%)</td><td>0.03 (+10.65%)</td><td>571.90 (-9.77%)</td><td>421.80 (+8.71%)</td><td>452.60 <b>(+33.67%)</b></td><td>188.00 (-3.54%)</td><td>158.73 (-3.37%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>633.80 (n/a)</td><td>388.02 (n/a)</td><td>338.60 (n/a)</td><td>194.90 (n/a)</td><td>164.27 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (-19.66%)</td><td>0.06 (-6.44%)</td><td>0.06 (+18.27%)</td><td>0.04 (-5.82%)</td><td>0.02 <b>(-39.28%)</b></td><td>579.60 (+6.17%)</td><td>408.84 (+1.19%)</td><td>383.90 (-15.44%)</td><td>281.90 <b>(+24.46%)</b></td><td>109.98 (-18.69%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>545.90 (n/a)</td><td>404.04 (n/a)</td><td>454.00 (n/a)</td><td>226.50 (n/a)</td><td>135.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-17.92%)</td><td>0.06 (-17.22%)</td><td>0.05 <b>(-42.74%)</b></td><td>0.04 (+4.37%)</td><td>0.02 <b>(-27.90%)</b></td><td>610.10 (-4.19%)</td><td>450.66 (+12.82%)</td><td>504.40 <b>(+74.65%)</b></td><td>289.70 <b>(+21.83%)</b></td><td>146.43 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>636.80 (n/a)</td><td>399.44 (n/a)</td><td>288.80 (n/a)</td><td>237.80 (n/a)</td><td>187.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(+40.55%)</b></td><td>0.06 <b>(+26.31%)</b></td><td>0.05 (-0.49%)</td><td>0.04 <b>(+214.37%)</b></td><td>0.02 (-4.64%)</td><td>597.10 <b>(-68.19%)</b></td><td>473.78 <b>(-38.11%)</b></td><td>527.70 (+0.50%)</td><td>284.90 <b>(-28.85%)</b></td><td>122.14 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1877.10 (n/a)</td><td>765.56 (n/a)</td><td>525.10 (n/a)</td><td>400.40 (n/a)</td><td>626.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(-23.95%)</b></td><td>0.06 (+2.87%)</td><td>0.07 <b>(+43.23%)</b></td><td>0.05 <b>(+34.66%)</b></td><td>0.01 <b>(-48.39%)</b></td><td>533.70 <b>(-25.73%)</b></td><td>400.94 (-12.89%)</td><td>343.60 <b>(-30.19%)</b></td><td>319.90 <b>(+31.48%)</b></td><td>98.86 <b>(-48.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>718.60 (n/a)</td><td>460.28 (n/a)</td><td>492.20 (n/a)</td><td>243.30 (n/a)</td><td>191.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 <b>(-43.62%)</b></td><td>0.05 <b>(-29.40%)</b></td><td>0.05 (-16.54%)</td><td>0.04 (-7.80%)</td><td>0.01 <b>(-71.27%)</b></td><td>634.80 (+8.48%)</td><td>532.42 <b>(+29.61%)</b></td><td>532.30 (+19.83%)</td><td>417.80 <b>(+77.41%)</b></td><td>77.22 <b>(-44.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>585.20 (n/a)</td><td>410.78 (n/a)</td><td>444.20 (n/a)</td><td>235.50 (n/a)</td><td>140.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(-36.35%)</b></td><td>0.07 <b>(-23.86%)</b></td><td>0.07 (-15.56%)</td><td>0.04 (-13.26%)</td><td>0.02 <b>(-40.33%)</b></td><td>581.80 (+15.30%)</td><td>410.52 <b>(+27.09%)</b></td><td>354.50 (+18.40%)</td><td>266.00 <b>(+57.12%)</b></td><td>141.45 (+15.05%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>504.60 (n/a)</td><td>323.02 (n/a)</td><td>299.40 (n/a)</td><td>169.30 (n/a)</td><td>122.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 <b>(-22.20%)</b></td><td>0.04 <b>(-35.41%)</b></td><td>0.03 <b>(-51.02%)</b></td><td>0.03 <b>(-23.13%)</b></td><td>0.01 <b>(-22.21%)</b></td><td>674.90 <b>(+30.09%)</b></td><td>540.20 <b>(+54.80%)</b></td><td>603.60 <b>(+104.19%)</b></td><td>311.90 <b>(+28.57%)</b></td><td>150.22 <b>(+28.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>518.80 (n/a)</td><td>348.96 (n/a)</td><td>295.60 (n/a)</td><td>242.60 (n/a)</td><td>116.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (-15.90%)</td><td>0.04 <b>(-24.79%)</b></td><td>0.04 <b>(-33.35%)</b></td><td>0.03 <b>(-26.16%)</b></td><td>0.01 (-5.82%)</td><td>599.30 <b>(+35.44%)</b></td><td>434.06 <b>(+34.82%)</b></td><td>447.70 <b>(+50.03%)</b></td><td>300.60 (+18.91%)</td><td>110.89 <b>(+48.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>442.50 (n/a)</td><td>321.96 (n/a)</td><td>298.40 (n/a)</td><td>252.80 (n/a)</td><td>74.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (-2.43%)</td><td>0.05 (-12.03%)</td><td>0.04 <b>(-34.48%)</b></td><td>0.03 (-5.34%)</td><td>0.02 (+9.23%)</td><td>529.80 (+5.64%)</td><td>410.24 (+16.73%)</td><td>473.00 <b>(+52.63%)</b></td><td>229.60 (+2.50%)</td><td>140.07 (+19.26%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.50 (n/a)</td><td>351.44 (n/a)</td><td>309.90 (n/a)</td><td>224.00 (n/a)</td><td>117.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (+4.42%)</td><td>0.04 (-2.62%)</td><td>0.04 (+8.56%)</td><td>0.02 <b>(-42.84%)</b></td><td>0.02 (+19.89%)</td><td>1048.00 <b>(+74.96%)</b></td><td>563.40 (+15.01%)</td><td>514.00 (-7.90%)</td><td>233.90 (-4.22%)</td><td>296.43 <b>(+107.15%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.00 (n/a)</td><td>489.88 (n/a)</td><td>558.10 (n/a)</td><td>244.20 (n/a)</td><td>143.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 <b>(-27.07%)</b></td><td>0.04 <b>(-35.24%)</b></td><td>0.05 (-13.69%)</td><td>0.01 <b>(-80.02%)</b></td><td>0.03 <b>(+34.75%)</b></td><td>2457.90 <b>(+400.49%)</b></td><td>893.52 <b>(+181.03%)</b></td><td>338.10 (+15.87%)</td><td>283.80 <b>(+37.10%)</b></td><td>937.38 <b>(+745.55%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>491.10 (n/a)</td><td>317.94 (n/a)</td><td>291.80 (n/a)</td><td>207.00 (n/a)</td><td>110.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (+8.99%)</td><td>0.05 (+2.62%)</td><td>0.04 (-4.55%)</td><td>0.04 <b>(+20.58%)</b></td><td>0.02 (+4.90%)</td><td>504.40 (-17.08%)</td><td>401.50 (-3.53%)</td><td>454.90 (+4.79%)</td><td>242.70 (-8.24%)</td><td>113.02 (-17.16%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.30 (n/a)</td><td>416.18 (n/a)</td><td>434.10 (n/a)</td><td>264.50 (n/a)</td><td>136.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.52 (+13.52%)</td><td>0.30 (+4.07%)</td><td>0.22 <b>(-23.02%)</b></td><td>0.17 <b>(+22.63%)</b></td><td>0.16 <b>(+33.02%)</b></td><td>573.20 (-18.45%)</td><td>403.06 (+0.73%)</td><td>453.00 <b>(+29.91%)</b></td><td>188.00 (-11.94%)</td><td>175.86 (-4.57%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>702.90 (n/a)</td><td>400.14 (n/a)</td><td>348.70 (n/a)</td><td>213.50 (n/a)</td><td>184.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.32 (+1.08%)</td><td>0.28 <b>(+37.81%)</b></td><td>0.31 <b>(+50.61%)</b></td><td>0.20 <b>(+403.53%)</b></td><td>0.05 <b>(-46.07%)</b></td><td>482.70 <b>(-80.14%)</b></td><td>369.02 <b>(-55.30%)</b></td><td>318.50 <b>(-33.60%)</b></td><td>302.50 (-1.05%)</td><td>80.90 <b>(-91.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>2430.50 (n/a)</td><td>825.64 (n/a)</td><td>479.70 (n/a)</td><td>305.70 (n/a)</td><td>900.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.29 (-16.47%)</td><td>0.20 (-2.31%)</td><td>0.17 (-8.45%)</td><td>0.16 <b>(+218.28%)</b></td><td>0.05 <b>(-50.21%)</b></td><td>624.00 <b>(-68.58%)</b></td><td>522.90 <b>(-30.10%)</b></td><td>573.20 (+9.24%)</td><td>338.90 (+19.71%)</td><td>112.13 <b>(-83.98%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>0.11 (n/a)</td><td>1986.10 (n/a)</td><td>748.12 (n/a)</td><td>524.70 (n/a)</td><td>283.10 (n/a)</td><td>699.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (-8.36%)</td><td>0.18 (-15.63%)</td><td>0.17 (-18.79%)</td><td>0.12 (-17.25%)</td><td>0.06 (-6.84%)</td><td>591.60 <b>(+20.86%)</b></td><td>437.10 (+19.50%)</td><td>425.90 <b>(+23.13%)</b></td><td>267.30 (+9.15%)</td><td>133.43 <b>(+21.09%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>489.50 (n/a)</td><td>365.76 (n/a)</td><td>345.90 (n/a)</td><td>244.90 (n/a)</td><td>110.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (+19.17%)</td><td>0.17 (-4.10%)</td><td>0.15 (-11.14%)</td><td>0.12 (-6.78%)</td><td>0.08 <b>(+47.08%)</b></td><td>594.60 (+7.27%)</td><td>473.78 (+9.24%)</td><td>507.60 (+12.52%)</td><td>238.40 (-16.09%)</td><td>137.59 <b>(+22.88%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>554.30 (n/a)</td><td>433.72 (n/a)</td><td>451.10 (n/a)</td><td>284.10 (n/a)</td><td>111.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (+18.59%)</td><td>0.21 <b>(+20.89%)</b></td><td>0.18 (+11.45%)</td><td>0.15 (+10.41%)</td><td>0.07 <b>(+48.89%)</b></td><td>500.60 (-9.43%)</td><td>374.26 (-14.22%)</td><td>405.10 (-10.26%)</td><td>239.20 (-15.69%)</td><td>114.70 (+18.58%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>552.70 (n/a)</td><td>436.32 (n/a)</td><td>451.40 (n/a)</td><td>283.70 (n/a)</td><td>96.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 <b>(+22.88%)</b></td><td>0.09 (+2.48%)</td><td>0.07 (-12.47%)</td><td>0.05 <b>(+239.86%)</b></td><td>0.06 (-5.72%)</td><td>711.30 <b>(-70.58%)</b></td><td>489.90 <b>(-39.49%)</b></td><td>511.70 (+14.24%)</td><td>192.10 (-18.60%)</td><td>203.96 <b>(-77.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2417.40 (n/a)</td><td>809.62 (n/a)</td><td>447.90 (n/a)</td><td>236.00 (n/a)</td><td>918.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 <b>(+32.61%)</b></td><td>0.11 (+15.53%)</td><td>0.12 <b>(+51.43%)</b></td><td>0.06 (-1.08%)</td><td>0.05 <b>(+45.35%)</b></td><td>657.10 (+1.09%)</td><td>409.70 (-7.40%)</td><td>319.60 <b>(-33.95%)</b></td><td>203.30 <b>(-24.56%)</b></td><td>186.91 (+19.95%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>650.00 (n/a)</td><td>442.44 (n/a)</td><td>483.90 (n/a)</td><td>269.50 (n/a)</td><td>155.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (-2.86%)</td><td>0.09 (-16.50%)</td><td>0.08 <b>(-28.24%)</b></td><td>0.07 (+1.44%)</td><td>0.03 (-14.47%)</td><td>540.30 (-1.42%)</td><td>446.46 (+17.32%)</td><td>489.20 <b>(+39.33%)</b></td><td>274.80 (+2.92%)</td><td>102.60 (-15.25%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>548.10 (n/a)</td><td>380.56 (n/a)</td><td>351.10 (n/a)</td><td>267.00 (n/a)</td><td>121.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 <b>(+25.53%)</b></td><td>0.11 (+11.39%)</td><td>0.12 <b>(+35.99%)</b></td><td>0.06 (-1.78%)</td><td>0.05 <b>(+27.88%)</b></td><td>585.70 (+1.81%)</td><td>381.80 (-6.09%)</td><td>301.90 <b>(-26.47%)</b></td><td>210.60 <b>(-20.32%)</b></td><td>165.37 (+16.25%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>575.30 (n/a)</td><td>406.56 (n/a)</td><td>410.60 (n/a)</td><td>264.30 (n/a)</td><td>142.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 <b>(-51.47%)</b></td><td>0.07 <b>(-38.20%)</b></td><td>0.06 <b>(-46.54%)</b></td><td>0.06 (+11.24%)</td><td>0.01 <b>(-78.30%)</b></td><td>657.40 (-10.11%)</td><td>572.48 <b>(+37.09%)</b></td><td>574.60 <b>(+87.04%)</b></td><td>456.70 <b>(+106.00%)</b></td><td>82.64 <b>(-60.64%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>731.30 (n/a)</td><td>417.58 (n/a)</td><td>307.20 (n/a)</td><td>221.70 (n/a)</td><td>209.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (-15.14%)</td><td>0.09 (-19.72%)</td><td>0.09 (-15.96%)</td><td>0.07 (-14.40%)</td><td>0.02 (-16.89%)</td><td>554.70 (+16.80%)</td><td>430.50 <b>(+24.07%)</b></td><td>427.80 (+19.00%)</td><td>288.40 (+17.86%)</td><td>95.29 (+10.16%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>474.90 (n/a)</td><td>346.98 (n/a)</td><td>359.50 (n/a)</td><td>244.70 (n/a)</td><td>86.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 (-2.43%)</td><td>0.12 (-15.89%)</td><td>0.13 (-5.16%)</td><td>0.07 <b>(-25.02%)</b></td><td>0.04 (+19.22%)</td><td>614.80 <b>(+33.36%)</b></td><td>381.44 <b>(+25.95%)</b></td><td>304.00 (+5.45%)</td><td>233.50 (+2.50%)</td><td>156.46 <b>(+65.88%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>461.00 (n/a)</td><td>302.86 (n/a)</td><td>288.30 (n/a)</td><td>227.80 (n/a)</td><td>94.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (-4.39%)</td><td>0.10 (-7.42%)</td><td>0.08 (-11.36%)</td><td>0.06 <b>(-21.11%)</b></td><td>0.05 (+6.42%)</td><td>719.50 <b>(+26.76%)</b></td><td>471.34 (+13.36%)</td><td>502.90 (+12.81%)</td><td>246.60 (+4.62%)</td><td>207.71 <b>(+32.45%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>567.60 (n/a)</td><td>415.78 (n/a)</td><td>445.80 (n/a)</td><td>235.70 (n/a)</td><td>156.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 <b>(+37.06%)</b></td><td>0.13 <b>(+28.24%)</b></td><td>0.12 <b>(+39.48%)</b></td><td>0.07 (-10.82%)</td><td>0.05 <b>(+111.73%)</b></td><td>597.80 (+12.12%)</td><td>371.96 (-14.51%)</td><td>331.10 <b>(-28.30%)</b></td><td>228.50 <b>(-27.04%)</b></td><td>155.19 <b>(+69.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>533.20 (n/a)</td><td>435.10 (n/a)</td><td>461.80 (n/a)</td><td>313.20 (n/a)</td><td>91.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (+12.99%)</td><td>0.08 (-10.39%)</td><td>0.07 (-8.07%)</td><td>0.02 <b>(-71.37%)</b></td><td>0.05 <b>(+72.11%)</b></td><td>1926.10 <b>(+249.31%)</b></td><td>751.30 <b>(+62.82%)</b></td><td>561.50 (+8.78%)</td><td>245.70 (-11.49%)</td><td>670.38 <b>(+490.89%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>551.40 (n/a)</td><td>461.44 (n/a)</td><td>516.20 (n/a)</td><td>277.60 (n/a)</td><td>113.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(-45.78%)</b></td><td>0.07 <b>(-42.35%)</b></td><td>0.08 <b>(-21.71%)</b></td><td>0.04 <b>(-54.60%)</b></td><td>0.02 <b>(-44.38%)</b></td><td>1016.60 <b>(+120.28%)</b></td><td>615.82 <b>(+77.31%)</b></td><td>485.70 <b>(+27.71%)</b></td><td>450.60 <b>(+84.45%)</b></td><td>236.78 <b>(+142.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>461.50 (n/a)</td><td>347.32 (n/a)</td><td>380.30 (n/a)</td><td>244.30 (n/a)</td><td>97.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (-10.26%)</td><td>0.10 (-16.35%)</td><td>0.09 <b>(-41.71%)</b></td><td>0.08 (+11.56%)</td><td>0.03 <b>(-35.40%)</b></td><td>481.90 (-10.38%)</td><td>411.90 (+13.38%)</td><td>468.90 <b>(+71.57%)</b></td><td>290.20 (+11.40%)</td><td>88.98 <b>(-32.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>537.70 (n/a)</td><td>363.28 (n/a)</td><td>273.30 (n/a)</td><td>260.50 (n/a)</td><td>131.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (+18.73%)</td><td>0.13 (+7.43%)</td><td>0.15 (+13.67%)</td><td>0.07 <b>(-35.70%)</b></td><td>0.04 <b>(+201.94%)</b></td><td>503.60 <b>(+55.53%)</b></td><td>291.96 (+2.49%)</td><td>240.00 (-12.02%)</td><td>208.80 (-15.77%)</td><td>123.15 <b>(+295.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>323.80 (n/a)</td><td>284.88 (n/a)</td><td>272.80 (n/a)</td><td>247.90 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (+2.56%)</td><td>0.10 (-3.61%)</td><td>0.12 <b>(+22.32%)</b></td><td>0.04 <b>(-43.63%)</b></td><td>0.05 (+19.68%)</td><td>994.20 <b>(+77.38%)</b></td><td>471.28 <b>(+22.97%)</b></td><td>289.90 (-18.25%)</td><td>205.90 (-2.51%)</td><td>327.19 <b>(+104.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>560.50 (n/a)</td><td>383.26 (n/a)</td><td>354.60 (n/a)</td><td>211.20 (n/a)</td><td>160.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (-7.69%)</td><td>0.09 (-2.80%)</td><td>0.08 (+0.60%)</td><td>0.07 <b>(+29.82%)</b></td><td>0.02 <b>(-32.45%)</b></td><td>499.30 <b>(-22.97%)</b></td><td>421.22 (-3.20%)</td><td>432.80 (-0.57%)</td><td>283.10 (+8.34%)</td><td>82.62 <b>(-45.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>648.20 (n/a)</td><td>435.14 (n/a)</td><td>435.30 (n/a)</td><td>261.30 (n/a)</td><td>151.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 <b>(+26.23%)</b></td><td>0.08 (+10.34%)</td><td>0.07 (+0.26%)</td><td>0.06 (+8.88%)</td><td>0.02 <b>(+42.83%)</b></td><td>576.70 (-8.17%)</td><td>477.20 (-8.48%)</td><td>479.80 (-0.25%)</td><td>333.70 <b>(-20.79%)</b></td><td>92.36 (-1.96%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>628.00 (n/a)</td><td>521.44 (n/a)</td><td>481.00 (n/a)</td><td>421.30 (n/a)</td><td>94.21 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 <b>(-43.93%)</b></td><td>0.07 <b>(-36.82%)</b></td><td>0.08 <b>(-35.42%)</b></td><td>0.05 <b>(-34.43%)</b></td><td>0.01 <b>(-52.15%)</b></td><td>688.60 <b>(+52.51%)</b></td><td>494.50 <b>(+55.00%)</b></td><td>452.90 <b>(+54.84%)</b></td><td>387.90 <b>(+78.34%)</b></td><td>117.43 <b>(+32.27%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>451.50 (n/a)</td><td>319.04 (n/a)</td><td>292.50 (n/a)</td><td>217.50 (n/a)</td><td>88.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (-18.01%)</td><td>0.10 (-8.42%)</td><td>0.08 (-19.35%)</td><td>0.06 <b>(+20.18%)</b></td><td>0.03 <b>(-25.39%)</b></td><td>537.20 (-16.80%)</td><td>394.90 (+2.56%)</td><td>433.20 <b>(+23.98%)</b></td><td>241.80 <b>(+21.94%)</b></td><td>128.13 <b>(-25.70%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>645.70 (n/a)</td><td>385.06 (n/a)</td><td>349.40 (n/a)</td><td>198.30 (n/a)</td><td>172.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.40 <b>(+35.55%)</b></td><td>0.26 (+12.98%)</td><td>0.23 (+4.60%)</td><td>0.16 <b>(-23.74%)</b></td><td>0.10 <b>(+182.79%)</b></td><td>827.90 <b>(+31.12%)</b></td><td>556.90 (-2.69%)</td><td>566.90 (-4.40%)</td><td>331.40 <b>(-26.21%)</b></td><td>200.83 <b>(+170.66%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>631.40 (n/a)</td><td>572.32 (n/a)</td><td>593.00 (n/a)</td><td>449.10 (n/a)</td><td>74.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.50 (+10.00%)</td><td>0.32 (+17.01%)</td><td>0.23 (-3.73%)</td><td>0.23 (+17.16%)</td><td>0.12 (+14.02%)</td><td>568.70 (-14.65%)</td><td>460.52 (-13.64%)</td><td>560.50 (+3.87%)</td><td>260.90 (-9.09%)</td><td>145.72 (-2.30%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>666.30 (n/a)</td><td>533.26 (n/a)</td><td>539.60 (n/a)</td><td>287.00 (n/a)</td><td>149.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.47 (+12.46%)</td><td>0.32 (-4.97%)</td><td>0.24 <b>(-30.41%)</b></td><td>0.21 (-8.88%)</td><td>0.13 <b>(+65.69%)</b></td><td>627.10 (+9.73%)</td><td>471.02 (+13.99%)</td><td>547.50 <b>(+43.70%)</b></td><td>277.10 (-11.07%)</td><td>173.31 <b>(+60.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>571.50 (n/a)</td><td>413.20 (n/a)</td><td>381.00 (n/a)</td><td>311.60 (n/a)</td><td>108.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+35.62%)</b></td><td>0.01 (-4.98%)</td><td>0.01 <b>(-26.61%)</b></td><td>0.01 (-15.55%)</td><td>0.00 <b>(+87.53%)</b></td><td>598.30 (+18.40%)</td><td>384.74 (+13.81%)</td><td>400.00 <b>(+36.24%)</b></td><td>208.50 <b>(-26.27%)</b></td><td>147.11 <b>(+56.03%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.30 (n/a)</td><td>338.04 (n/a)</td><td>293.60 (n/a)</td><td>282.80 (n/a)</td><td>94.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (-6.49%)</td><td>0.01 (-5.36%)</td><td>0.01 (-0.42%)</td><td>0.01 <b>(+34.34%)</b></td><td>0.00 <b>(-40.26%)</b></td><td>391.40 <b>(-25.58%)</b></td><td>305.26 (-1.52%)</td><td>290.30 (+0.42%)</td><td>233.00 (+6.93%)</td><td>58.75 <b>(-53.19%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.90 (n/a)</td><td>309.96 (n/a)</td><td>289.10 (n/a)</td><td>217.90 (n/a)</td><td>125.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (-17.33%)</td><td>0.01 (+4.34%)</td><td>0.01 <b>(+37.45%)</b></td><td>0.01 <b>(+22.47%)</b></td><td>0.00 <b>(-55.79%)</b></td><td>433.70 (-18.34%)</td><td>361.06 (-11.41%)</td><td>332.30 <b>(-27.25%)</b></td><td>303.30 <b>(+20.93%)</b></td><td>58.24 <b>(-56.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.10 (n/a)</td><td>407.58 (n/a)</td><td>456.80 (n/a)</td><td>250.80 (n/a)</td><td>132.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.96 <b>(+21.62%)</b></td><td>5.77 (+9.93%)</td><td>6.12 <b>(+34.61%)</b></td><td>3.06 <b>(-26.12%)</b></td><td>2.01 <b>(+71.64%)</b></td><td>685.20 <b>(+35.36%)</b></td><td>410.02 (-1.19%)</td><td>342.60 <b>(-25.72%)</b></td><td>263.70 (-17.77%)</td><td>173.04 <b>(+99.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.54 (n/a)</td><td>5.25 (n/a)</td><td>4.55 (n/a)</td><td>4.15 (n/a)</td><td>1.17 (n/a)</td><td>506.20 (n/a)</td><td>414.96 (n/a)</td><td>461.20 (n/a)</td><td>320.70 (n/a)</td><td>86.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 (-2.35%)</td><td>0.40 <b>(+20.88%)</b></td><td>0.45 <b>(+75.03%)</b></td><td>0.27 <b>(+288.83%)</b></td><td>0.12 <b>(-42.94%)</b></td><td>490.90 <b>(-74.28%)</b></td><td>354.22 <b>(-48.96%)</b></td><td>294.50 <b>(-42.87%)</b></td><td>236.60 (+2.42%)</td><td>114.36 <b>(-83.58%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.57 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td><td>1908.60 (n/a)</td><td>694.02 (n/a)</td><td>515.50 (n/a)</td><td>231.00 (n/a)</td><td>696.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.54 (+5.18%)</td><td>0.43 (+3.29%)</td><td>0.45 (+5.38%)</td><td>0.26 (+14.02%)</td><td>0.12 (+0.37%)</td><td>515.40 (-12.30%)</td><td>330.38 (-4.78%)</td><td>291.90 (-5.10%)</td><td>244.50 (-4.90%)</td><td>110.75 (-19.13%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>587.70 (n/a)</td><td>346.96 (n/a)</td><td>307.60 (n/a)</td><td>257.10 (n/a)</td><td>136.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.60 (+12.30%)</td><td>0.39 (+11.75%)</td><td>0.33 (+16.44%)</td><td>0.22 (-8.72%)</td><td>0.17 <b>(+41.23%)</b></td><td>599.00 (+9.55%)</td><td>395.56 (-3.94%)</td><td>402.00 (-14.12%)</td><td>219.90 (-10.97%)</td><td>166.99 <b>(+33.68%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>546.80 (n/a)</td><td>411.78 (n/a)</td><td>468.10 (n/a)</td><td>247.00 (n/a)</td><td>124.92 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 <b>(+20.42%)</b></td><td>0.33 (-16.37%)</td><td>0.30 <b>(-29.11%)</b></td><td>0.18 <b>(-47.56%)</b></td><td>0.15 <b>(+163.05%)</b></td><td>746.00 <b>(+90.70%)</b></td><td>458.04 <b>(+36.27%)</b></td><td>443.10 <b>(+41.07%)</b></td><td>235.60 (-16.98%)</td><td>192.18 <b>(+302.30%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>391.20 (n/a)</td><td>336.12 (n/a)</td><td>314.10 (n/a)</td><td>283.80 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.62 <b>(+23.73%)</b></td><td>0.46 <b>(+21.15%)</b></td><td>0.47 <b>(+37.45%)</b></td><td>0.24 (-18.75%)</td><td>0.14 <b>(+54.60%)</b></td><td>554.70 <b>(+23.08%)</b></td><td>317.88 (-12.15%)</td><td>281.20 <b>(-27.24%)</b></td><td>213.20 (-19.18%)</td><td>135.44 <b>(+68.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>450.70 (n/a)</td><td>361.84 (n/a)</td><td>386.50 (n/a)</td><td>263.80 (n/a)</td><td>80.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (+3.80%)</td><td>0.01 (+6.78%)</td><td>0.01 (+15.88%)</td><td>0.01 (-13.96%)</td><td>0.00 <b>(+21.62%)</b></td><td>547.70 (+16.21%)</td><td>352.90 (-3.29%)</td><td>310.50 (-13.70%)</td><td>239.70 (-3.66%)</td><td>119.12 <b>(+43.57%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.30 (n/a)</td><td>364.92 (n/a)</td><td>359.80 (n/a)</td><td>248.80 (n/a)</td><td>82.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 <b>(+21.53%)</b></td><td>0.01 (+8.82%)</td><td>0.01 (+2.62%)</td><td>0.01 (+5.97%)</td><td>0.00 <b>(+23.41%)</b></td><td>493.10 (-5.63%)</td><td>307.36 (-6.75%)</td><td>285.60 (-2.56%)</td><td>199.60 (-17.72%)</td><td>113.56 (-1.48%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.50 (n/a)</td><td>329.62 (n/a)</td><td>293.10 (n/a)</td><td>242.60 (n/a)</td><td>115.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+54.55%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+274.17%)</b></td><td>18027.77 (-18.13%)</td><td>13130.72 <b>(-26.64%)</b></td><td>12504.96 <b>(-27.30%)</b></td><td>7406.46 <b>(-54.35%)</b></td><td>4673.56 <b>(+98.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22019.68 (n/a)</td><td>17899.81 (n/a)</td><td>17201.35 (n/a)</td><td>16226.00 (n/a)</td><td>2351.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.00 <b>(+120.00%)</b></td><td>0.00 <b>(+66.67%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+424.40%)</b></td><td>16371.66 <b>(-25.35%)</b></td><td>12803.93 <b>(-32.83%)</b></td><td>14068.39 <b>(-28.07%)</b></td><td>7614.33 <b>(-49.66%)</b></td><td>3480.41 <b>(+37.58%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21930.00 (n/a)</td><td>19061.53 (n/a)</td><td>19557.26 (n/a)</td><td>15126.21 (n/a)</td><td>2529.83 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 <b>(+20.20%)</b></td><td>0.10 (+10.22%)</td><td>0.08 (-4.81%)</td><td>0.07 (-1.92%)</td><td>0.03 <b>(+76.44%)</b></td><td>29367.27 (+1.88%)</td><td>22449.32 (-5.49%)</td><td>25239.64 (+5.09%)</td><td>15525.01 (-16.76%)</td><td>6236.35 <b>(+43.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28825.72 (n/a)</td><td>23754.39 (n/a)</td><td>24016.84 (n/a)</td><td>18650.20 (n/a)</td><td>4354.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.63 (-11.11%)</td><td>1.82 (-8.75%)</td><td>2.22 <b>(+28.50%)</b></td><td>0.56 <b>(-52.29%)</b></td><td>0.84 (+0.32%)</td><td>1876.10 <b>(+109.60%)</b></td><td>791.62 <b>(+30.59%)</b></td><td>473.30 <b>(-22.18%)</b></td><td>398.70 (+12.50%)</td><td>622.06 <b>(+154.41%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.96 (n/a)</td><td>2.00 (n/a)</td><td>1.72 (n/a)</td><td>1.17 (n/a)</td><td>0.84 (n/a)</td><td>895.10 (n/a)</td><td>606.18 (n/a)</td><td>608.20 (n/a)</td><td>354.40 (n/a)</td><td>244.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.50 <b>(-31.14%)</b></td><td>1.65 (-13.58%)</td><td>1.75 (+4.56%)</td><td>0.55 <b>(+81.76%)</b></td><td>0.87 <b>(-28.60%)</b></td><td>1923.30 <b>(-44.98%)</b></td><td>886.10 (-19.87%)</td><td>600.30 (-4.37%)</td><td>418.70 <b>(+45.23%)</b></td><td>635.95 <b>(-52.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.64 (n/a)</td><td>1.91 (n/a)</td><td>1.67 (n/a)</td><td>0.30 (n/a)</td><td>1.22 (n/a)</td><td>3495.70 (n/a)</td><td>1105.82 (n/a)</td><td>627.70 (n/a)</td><td>288.30 (n/a)</td><td>1344.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.91 <b>(-33.14%)</b></td><td>1.64 <b>(-29.14%)</b></td><td>1.62 <b>(-23.89%)</b></td><td>0.33 <b>(-71.61%)</b></td><td>0.92 <b>(-24.71%)</b></td><td>3218.80 <b>(+252.17%)</b></td><td>1098.62 <b>(+100.30%)</b></td><td>646.50 <b>(+31.40%)</b></td><td>360.60 <b>(+49.56%)</b></td><td>1192.34 <b>(+376.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.35 (n/a)</td><td>2.32 (n/a)</td><td>2.13 (n/a)</td><td>1.15 (n/a)</td><td>1.23 (n/a)</td><td>914.00 (n/a)</td><td>548.48 (n/a)</td><td>492.00 (n/a)</td><td>241.10 (n/a)</td><td>250.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.56 <b>(-43.69%)</b></td><td>1.30 <b>(-40.75%)</b></td><td>1.43 (-4.25%)</td><td>0.29 (-4.03%)</td><td>0.91 <b>(-48.59%)</b></td><td>3583.40 (+4.20%)</td><td>1449.62 <b>(+29.05%)</b></td><td>735.80 (+4.44%)</td><td>410.30 <b>(+77.62%)</b></td><td>1322.23 (-0.36%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.54 (n/a)</td><td>2.19 (n/a)</td><td>1.49 (n/a)</td><td>0.30 (n/a)</td><td>1.76 (n/a)</td><td>3438.90 (n/a)</td><td>1123.30 (n/a)</td><td>704.50 (n/a)</td><td>231.00 (n/a)</td><td>1327.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.58 <b>(+50.74%)</b></td><td>2.30 <b>(+63.11%)</b></td><td>1.91 <b>(+74.65%)</b></td><td>0.58 (-1.03%)</td><td>1.27 <b>(+66.76%)</b></td><td>3615.50 (+1.04%)</td><td>1399.58 <b>(-27.11%)</b></td><td>1098.80 <b>(-42.74%)</b></td><td>586.40 <b>(-33.66%)</b></td><td>1264.96 (+16.72%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.37 (n/a)</td><td>1.41 (n/a)</td><td>1.09 (n/a)</td><td>0.59 (n/a)</td><td>0.76 (n/a)</td><td>3578.20 (n/a)</td><td>1920.08 (n/a)</td><td>1919.10 (n/a)</td><td>883.90 (n/a)</td><td>1083.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.71 <b>(-42.13%)</b></td><td>3.08 (+16.38%)</td><td>3.25 <b>(+78.56%)</b></td><td>2.09 <b>(+239.77%)</b></td><td>0.67 <b>(-72.73%)</b></td><td>1001.90 <b>(-70.57%)</b></td><td>713.08 <b>(-59.61%)</b></td><td>644.90 <b>(-43.99%)</b></td><td>565.60 <b>(+72.81%)</b></td><td>180.63 <b>(-88.10%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.41 (n/a)</td><td>2.64 (n/a)</td><td>1.82 (n/a)</td><td>0.62 (n/a)</td><td>2.46 (n/a)</td><td>3404.40 (n/a)</td><td>1765.60 (n/a)</td><td>1151.50 (n/a)</td><td>327.30 (n/a)</td><td>1517.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.04 <b>(-33.33%)</b></td><td>3.67 (+7.68%)</td><td>3.85 <b>(+36.02%)</b></td><td>2.70 <b>(+171.95%)</b></td><td>0.93 <b>(-63.01%)</b></td><td>776.80 <b>(-63.23%)</b></td><td>600.44 <b>(-36.73%)</b></td><td>544.70 <b>(-26.48%)</b></td><td>416.20 <b>(+49.98%)</b></td><td>147.00 <b>(-79.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.56 (n/a)</td><td>3.41 (n/a)</td><td>2.83 (n/a)</td><td>0.99 (n/a)</td><td>2.52 (n/a)</td><td>2112.40 (n/a)</td><td>949.08 (n/a)</td><td>740.90 (n/a)</td><td>277.50 (n/a)</td><td>706.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.76 <b>(-48.39%)</b></td><td>1.77 <b>(-50.97%)</b></td><td>1.97 <b>(-51.83%)</b></td><td>0.60 <b>(-65.70%)</b></td><td>1.01 <b>(-31.61%)</b></td><td>3519.30 <b>(+191.57%)</b></td><td>1721.20 <b>(+150.31%)</b></td><td>1067.30 <b>(+107.61%)</b></td><td>760.80 <b>(+93.79%)</b></td><td>1230.44 <b>(+261.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.34 (n/a)</td><td>3.62 (n/a)</td><td>4.08 (n/a)</td><td>1.74 (n/a)</td><td>1.48 (n/a)</td><td>1207.00 (n/a)</td><td>687.62 (n/a)</td><td>514.10 (n/a)</td><td>392.60 (n/a)</td><td>340.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.80 (-19.98%)</td><td>3.10 <b>(+79.60%)</b></td><td>2.61 <b>(+330.74%)</b></td><td>2.45 <b>(+307.59%)</b></td><td>0.99 <b>(-58.73%)</b></td><td>855.20 <b>(-75.47%)</b></td><td>719.72 <b>(-72.95%)</b></td><td>802.20 <b>(-76.79%)</b></td><td>437.10 <b>(+24.96%)</b></td><td>173.91 <b>(-87.17%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.00 (n/a)</td><td>1.73 (n/a)</td><td>0.61 (n/a)</td><td>0.60 (n/a)</td><td>2.39 (n/a)</td><td>3485.80 (n/a)</td><td>2660.58 (n/a)</td><td>3455.60 (n/a)</td><td>349.80 (n/a)</td><td>1355.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.16 <b>(+32.60%)</b></td><td>3.48 (+10.65%)</td><td>3.16 (-1.95%)</td><td>1.87 <b>(+215.82%)</b></td><td>1.62 (-2.11%)</td><td>1124.40 <b>(-68.33%)</b></td><td>701.74 <b>(-40.46%)</b></td><td>664.10 (+1.98%)</td><td>340.60 <b>(-24.58%)</b></td><td>286.71 <b>(-78.50%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.64 (n/a)</td><td>3.14 (n/a)</td><td>3.22 (n/a)</td><td>0.59 (n/a)</td><td>1.66 (n/a)</td><td>3550.90 (n/a)</td><td>1178.70 (n/a)</td><td>651.20 (n/a)</td><td>451.60 (n/a)</td><td>1333.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.60 (+7.81%)</td><td>3.10 (-15.28%)</td><td>3.23 (-12.23%)</td><td>1.68 (-4.48%)</td><td>1.59 <b>(+26.83%)</b></td><td>2491.00 (+4.68%)</td><td>1646.12 <b>(+25.95%)</b></td><td>1296.60 (+13.94%)</td><td>749.60 (-7.24%)</td><td>764.49 <b>(+23.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.19 (n/a)</td><td>3.66 (n/a)</td><td>3.69 (n/a)</td><td>1.76 (n/a)</td><td>1.25 (n/a)</td><td>2379.60 (n/a)</td><td>1306.96 (n/a)</td><td>1138.00 (n/a)</td><td>808.10 (n/a)</td><td>619.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.78 (-12.07%)</td><td>3.78 <b>(-34.24%)</b></td><td>2.12 <b>(-64.45%)</b></td><td>1.68 <b>(-51.61%)</b></td><td>2.67 <b>(+33.55%)</b></td><td>2493.70 <b>(+106.64%)</b></td><td>1639.22 <b>(+101.41%)</b></td><td>1981.10 <b>(+181.33%)</b></td><td>618.80 (+13.73%)</td><td>946.99 <b>(+209.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.71 (n/a)</td><td>5.75 (n/a)</td><td>5.96 (n/a)</td><td>3.48 (n/a)</td><td>2.00 (n/a)</td><td>1206.80 (n/a)</td><td>813.86 (n/a)</td><td>704.20 (n/a)</td><td>544.10 (n/a)</td><td>305.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.42 (-0.95%)</td><td>3.79 (-14.66%)</td><td>3.64 (-8.41%)</td><td>1.74 (-0.58%)</td><td>1.68 (-11.67%)</td><td>2417.10 (+0.58%)</td><td>1315.14 (+12.14%)</td><td>1151.10 (+9.18%)</td><td>653.50 (+0.96%)</td><td>655.90 (-8.27%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.48 (n/a)</td><td>4.44 (n/a)</td><td>3.98 (n/a)</td><td>1.75 (n/a)</td><td>1.90 (n/a)</td><td>2403.20 (n/a)</td><td>1172.78 (n/a)</td><td>1054.30 (n/a)</td><td>647.30 (n/a)</td><td>715.00 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>9.18 (-10.71%)</td><td>6.25 (-9.83%)</td><td>6.53 (-6.27%)</td><td>3.50 (-5.41%)</td><td>2.16 (-7.68%)</td><td>1197.20 (+5.73%)</td><td>747.28 (+10.90%)</td><td>642.60 (+6.69%)</td><td>456.70 (+11.99%)</td><td>287.92 (+6.12%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>10.29 (n/a)</td><td>6.93 (n/a)</td><td>6.96 (n/a)</td><td>3.70 (n/a)</td><td>2.34 (n/a)</td><td>1132.30 (n/a)</td><td>673.86 (n/a)</td><td>602.30 (n/a)</td><td>407.80 (n/a)</td><td>271.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>8.90 (+1.65%)</td><td>5.38 <b>(+38.08%)</b></td><td>5.55 <b>(+46.69%)</b></td><td>1.17 (+0.71%)</td><td>2.87 (-4.39%)</td><td>3572.10 (-0.70%)</td><td>1271.20 <b>(-27.08%)</b></td><td>756.20 <b>(-31.82%)</b></td><td>471.30 (-1.63%)</td><td>1297.83 (+1.52%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>8.76 (n/a)</td><td>3.89 (n/a)</td><td>3.78 (n/a)</td><td>1.17 (n/a)</td><td>3.00 (n/a)</td><td>3597.40 (n/a)</td><td>1743.28 (n/a)</td><td>1109.20 (n/a)</td><td>479.10 (n/a)</td><td>1278.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.27 (-13.14%)</td><td>4.35 (-18.86%)</td><td>5.46 (+14.69%)</td><td>1.16 <b>(-31.38%)</b></td><td>2.74 (-2.66%)</td><td>3600.70 <b>(+45.73%)</b></td><td>1614.04 <b>(+48.63%)</b></td><td>767.60 (-12.80%)</td><td>577.30 (+15.14%)</td><td>1350.05 <b>(+66.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>8.36 (n/a)</td><td>5.36 (n/a)</td><td>4.76 (n/a)</td><td>1.70 (n/a)</td><td>2.81 (n/a)</td><td>2470.80 (n/a)</td><td>1085.96 (n/a)</td><td>880.30 (n/a)</td><td>501.40 (n/a)</td><td>809.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.70 (+7.09%)</td><td>1.33 (+10.63%)</td><td>1.38 <b>(+29.37%)</b></td><td>0.62 <b>(-30.05%)</b></td><td>0.43 <b>(+29.15%)</b></td><td>852.50 <b>(+42.96%)</b></td><td>453.02 (-2.49%)</td><td>381.00 <b>(-22.70%)</b></td><td>309.20 (-6.64%)</td><td>226.88 <b>(+85.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.58 (n/a)</td><td>1.20 (n/a)</td><td>1.06 (n/a)</td><td>0.88 (n/a)</td><td>0.33 (n/a)</td><td>596.30 (n/a)</td><td>464.60 (n/a)</td><td>492.90 (n/a)</td><td>331.20 (n/a)</td><td>122.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.44 (-19.77%)</td><td>1.80 <b>(+43.04%)</b></td><td>1.51 <b>(+55.42%)</b></td><td>1.18 <b>(+290.81%)</b></td><td>0.60 <b>(-44.95%)</b></td><td>892.00 <b>(-74.41%)</b></td><td>636.46 <b>(-57.81%)</b></td><td>693.20 <b>(-35.66%)</b></td><td>429.00 <b>(+24.64%)</b></td><td>202.31 <b>(-83.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.05 (n/a)</td><td>1.26 (n/a)</td><td>0.97 (n/a)</td><td>0.30 (n/a)</td><td>1.09 (n/a)</td><td>3486.10 (n/a)</td><td>1508.68 (n/a)</td><td>1077.40 (n/a)</td><td>344.20 (n/a)</td><td>1243.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.82 (+2.85%)</td><td>2.76 <b>(+20.08%)</b></td><td>3.27 <b>(+38.28%)</b></td><td>0.87 <b>(+47.04%)</b></td><td>1.15 (+2.90%)</td><td>2400.60 <b>(-31.99%)</b></td><td>1011.00 <b>(-24.92%)</b></td><td>642.20 <b>(-27.69%)</b></td><td>549.10 (-2.76%)</td><td>783.67 <b>(-36.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.71 (n/a)</td><td>2.30 (n/a)</td><td>2.36 (n/a)</td><td>0.59 (n/a)</td><td>1.12 (n/a)</td><td>3529.80 (n/a)</td><td>1346.60 (n/a)</td><td>888.10 (n/a)</td><td>564.70 (n/a)</td><td>1229.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.70 (-6.88%)</td><td>1.16 (-4.41%)</td><td>1.01 (+10.31%)</td><td>0.78 (-13.34%)</td><td>0.36 (-17.11%)</td><td>675.40 (+15.39%)</td><td>486.08 (+2.57%)</td><td>519.10 (-9.34%)</td><td>308.10 (+7.39%)</td><td>140.88 (-3.81%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.83 (n/a)</td><td>1.21 (n/a)</td><td>0.92 (n/a)</td><td>0.90 (n/a)</td><td>0.44 (n/a)</td><td>585.30 (n/a)</td><td>473.88 (n/a)</td><td>572.60 (n/a)</td><td>286.90 (n/a)</td><td>146.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (-4.20%)</td><td>0.08 <b>(-24.95%)</b></td><td>0.07 <b>(-38.14%)</b></td><td>0.06 (-10.00%)</td><td>0.02 (+1.98%)</td><td>517.60 (+11.12%)</td><td>420.00 <b>(+34.08%)</b></td><td>442.90 <b>(+61.70%)</b></td><td>269.00 (+4.38%)</td><td>97.63 (+12.37%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>465.80 (n/a)</td><td>313.24 (n/a)</td><td>273.90 (n/a)</td><td>257.70 (n/a)</td><td>86.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (+5.65%)</td><td>0.10 (+14.60%)</td><td>0.10 (-6.74%)</td><td>0.06 <b>(+351.47%)</b></td><td>0.03 <b>(-39.63%)</b></td><td>538.20 <b>(-77.85%)</b></td><td>361.90 <b>(-52.24%)</b></td><td>334.20 (+7.22%)</td><td>240.90 (-5.34%)</td><td>111.92 <b>(-88.08%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2429.80 (n/a)</td><td>757.76 (n/a)</td><td>311.70 (n/a)</td><td>254.50 (n/a)</td><td>939.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (-13.61%)</td><td>0.18 (-18.88%)</td><td>0.16 <b>(-30.69%)</b></td><td>0.14 (+1.18%)</td><td>0.06 <b>(-28.05%)</b></td><td>477.30 (-1.16%)</td><td>389.24 (+16.98%)</td><td>402.50 <b>(+44.27%)</b></td><td>232.70 (+15.77%)</td><td>93.13 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>482.90 (n/a)</td><td>332.74 (n/a)</td><td>279.00 (n/a)</td><td>201.00 (n/a)</td><td>126.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.24 (-4.73%)</td><td>0.17 (-4.17%)</td><td>0.14 (-16.59%)</td><td>0.13 (+13.35%)</td><td>0.05 (-9.60%)</td><td>501.70 (-11.78%)</td><td>416.16 (+2.94%)</td><td>455.80 (+19.88%)</td><td>276.70 (+4.97%)</td><td>97.67 (-14.93%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>568.70 (n/a)</td><td>404.26 (n/a)</td><td>380.20 (n/a)</td><td>263.60 (n/a)</td><td>114.81 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.36 <b>(+27.64%)</b></td><td>0.22 (-2.73%)</td><td>0.21 (-15.39%)</td><td>0.13 <b>(+27.35%)</b></td><td>0.09 <b>(+23.74%)</b></td><td>489.60 <b>(-21.48%)</b></td><td>340.60 (+1.43%)</td><td>311.70 (+18.20%)</td><td>184.40 <b>(-21.67%)</b></td><td>120.69 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>623.50 (n/a)</td><td>335.80 (n/a)</td><td>263.70 (n/a)</td><td>235.40 (n/a)</td><td>163.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.53 <b>(-21.31%)</b></td><td>0.37 (-3.87%)</td><td>0.42 <b>(+33.82%)</b></td><td>0.21 (-1.43%)</td><td>0.14 <b>(-28.72%)</b></td><td>631.20 (+1.46%)</td><td>410.88 (-2.25%)</td><td>314.90 <b>(-25.27%)</b></td><td>246.80 <b>(+27.09%)</b></td><td>177.24 (-8.01%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.67 (n/a)</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>622.10 (n/a)</td><td>420.34 (n/a)</td><td>421.40 (n/a)</td><td>194.20 (n/a)</td><td>192.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.52 (+9.88%)</td><td>0.38 (-0.58%)</td><td>0.43 (+1.22%)</td><td>0.23 (-16.12%)</td><td>0.12 (+19.56%)</td><td>574.00 (+19.24%)</td><td>376.02 (+3.91%)</td><td>306.00 (-1.19%)</td><td>249.70 (-9.00%)</td><td>136.67 <b>(+30.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>481.40 (n/a)</td><td>361.86 (n/a)</td><td>309.70 (n/a)</td><td>274.40 (n/a)</td><td>104.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.49 (-7.99%)</td><td>0.35 (-13.30%)</td><td>0.37 <b>(-24.40%)</b></td><td>0.24 (-2.81%)</td><td>0.11 (-13.35%)</td><td>552.50 (+2.89%)</td><td>404.68 (+14.07%)</td><td>358.80 <b>(+32.30%)</b></td><td>265.10 (+8.69%)</td><td>134.64 (+2.40%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.48 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>537.00 (n/a)</td><td>354.78 (n/a)</td><td>271.20 (n/a)</td><td>243.90 (n/a)</td><td>131.49 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (-1.45%)</td><td>0.04 (-6.09%)</td><td>0.04 (+9.89%)</td><td>0.02 (-0.97%)</td><td>0.02 (-4.94%)</td><td>704.50 (+0.97%)</td><td>461.80 (+4.90%)</td><td>432.20 (-9.01%)</td><td>229.50 (+1.46%)</td><td>172.26 (-4.79%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>697.70 (n/a)</td><td>440.22 (n/a)</td><td>475.00 (n/a)</td><td>226.20 (n/a)</td><td>180.92 (n/a)</td>
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
