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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (+16.86%)</td><td>0.02 (+12.38%)</td><td>0.02 (-1.22%)</td><td>0.02 <b>(+25.99%)</b></td><td>0.01 (-19.11%)</td><td>385.00 <b>(-20.62%)</b></td><td>282.84 (-16.13%)</td><td>274.50 (+1.25%)</td><td>197.00 (-14.42%)</td><td>67.85 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>485.00 (n/a)</td><td>337.24 (n/a)</td><td>271.10 (n/a)</td><td>230.20 (n/a)</td><td>126.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(+75.86%)</b></td><td>0.02 <b>(+48.24%)</b></td><td>0.02 <b>(+28.91%)</b></td><td>0.01 (+11.42%)</td><td>0.01 <b>(+242.64%)</b></td><td>497.30 (-10.25%)</td><td>343.82 <b>(-26.45%)</b></td><td>360.40 <b>(-22.44%)</b></td><td>207.30 <b>(-43.13%)</b></td><td>119.40 <b>(+74.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>467.46 (n/a)</td><td>464.70 (n/a)</td><td>364.50 (n/a)</td><td>68.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+37.00%)</b></td><td>0.02 (+2.94%)</td><td>0.02 (-17.55%)</td><td>0.02 <b>(+21.67%)</b></td><td>0.01 <b>(+64.46%)</b></td><td>361.30 (-17.81%)</td><td>279.02 (-0.33%)</td><td>304.30 <b>(+21.28%)</b></td><td>151.90 <b>(-27.01%)</b></td><td>78.99 (-13.42%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>439.60 (n/a)</td><td>279.94 (n/a)</td><td>250.90 (n/a)</td><td>208.10 (n/a)</td><td>91.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(+30.84%)</b></td><td>0.03 <b>(+49.20%)</b></td><td>0.03 <b>(+65.76%)</b></td><td>0.02 <b>(+81.34%)</b></td><td>0.01 (-16.14%)</td><td>317.60 <b>(-44.85%)</b></td><td>237.82 <b>(-38.50%)</b></td><td>233.20 <b>(-39.68%)</b></td><td>181.40 <b>(-23.59%)</b></td><td>55.33 <b>(-63.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.90 (n/a)</td><td>386.70 (n/a)</td><td>386.60 (n/a)</td><td>237.40 (n/a)</td><td>149.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-16.46%)</td><td>0.02 (-14.86%)</td><td>0.02 (-9.69%)</td><td>0.01 <b>(-36.97%)</b></td><td>0.01 <b>(+21.65%)</b></td><td>622.40 <b>(+58.65%)</b></td><td>356.18 <b>(+25.03%)</b></td><td>293.40 (+10.76%)</td><td>270.50 (+19.69%)</td><td>150.37 <b>(+131.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>392.30 (n/a)</td><td>284.88 (n/a)</td><td>264.90 (n/a)</td><td>226.00 (n/a)</td><td>65.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-14.87%)</td><td>0.02 (+10.25%)</td><td>0.02 <b>(+31.09%)</b></td><td>0.01 (-11.64%)</td><td>0.00 <b>(-23.38%)</b></td><td>561.00 (+13.17%)</td><td>385.08 (-11.05%)</td><td>369.50 <b>(-23.70%)</b></td><td>271.10 (+17.46%)</td><td>116.64 (+2.59%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>495.70 (n/a)</td><td>432.94 (n/a)</td><td>484.30 (n/a)</td><td>230.80 (n/a)</td><td>113.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (+10.51%)</td><td>0.05 (+7.29%)</td><td>0.05 (+6.07%)</td><td>0.02 (+10.28%)</td><td>0.01 (-0.14%)</td><td>519.00 (-9.31%)</td><td>296.46 (-8.02%)</td><td>247.30 (-5.72%)</td><td>207.60 (-9.50%)</td><td>126.10 (-12.44%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.30 (n/a)</td><td>322.30 (n/a)</td><td>262.30 (n/a)</td><td>229.40 (n/a)</td><td>144.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (-0.78%)</td><td>0.05 (+0.66%)</td><td>0.05 (-10.44%)</td><td>0.04 (+19.12%)</td><td>0.01 <b>(-26.02%)</b></td><td>329.70 (-16.04%)</td><td>267.66 (-2.81%)</td><td>270.20 (+11.65%)</td><td>226.00 (+0.76%)</td><td>41.22 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>392.70 (n/a)</td><td>275.40 (n/a)</td><td>242.00 (n/a)</td><td>224.30 (n/a)</td><td>68.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (+4.80%)</td><td>0.04 (-4.83%)</td><td>0.04 (-10.54%)</td><td>0.02 <b>(-24.67%)</b></td><td>0.01 <b>(+23.36%)</b></td><td>679.80 <b>(+32.77%)</b></td><td>339.72 (+13.44%)</td><td>274.00 (+11.79%)</td><td>222.40 (-4.55%)</td><td>191.94 <b>(+60.72%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.00 (n/a)</td><td>299.46 (n/a)</td><td>245.10 (n/a)</td><td>233.00 (n/a)</td><td>119.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (+2.62%)</td><td>0.04 (-2.12%)</td><td>0.04 (+13.35%)</td><td>0.01 <b>(-52.56%)</b></td><td>0.02 <b>(+41.43%)</b></td><td>1121.60 <b>(+110.79%)</b></td><td>471.66 <b>(+28.36%)</b></td><td>279.10 (-11.76%)</td><td>236.60 (-2.55%)</td><td>371.91 <b>(+197.19%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.10 (n/a)</td><td>367.46 (n/a)</td><td>316.30 (n/a)</td><td>242.80 (n/a)</td><td>125.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(-37.40%)</b></td><td>0.03 (-0.01%)</td><td>0.03 <b>(+46.74%)</b></td><td>0.01 <b>(+20.74%)</b></td><td>0.01 <b>(-44.21%)</b></td><td>1056.20 (-17.18%)</td><td>504.16 (-17.10%)</td><td>412.60 <b>(-31.85%)</b></td><td>281.70 <b>(+59.78%)</b></td><td>319.33 <b>(-22.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1275.30 (n/a)</td><td>608.16 (n/a)</td><td>605.40 (n/a)</td><td>176.30 (n/a)</td><td>414.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (+6.77%)</td><td>0.04 <b>(+25.59%)</b></td><td>0.04 <b>(+63.49%)</b></td><td>0.01 <b>(-35.40%)</b></td><td>0.02 (+13.11%)</td><td>995.50 <b>(+54.82%)</b></td><td>404.02 (-7.72%)</td><td>277.50 <b>(-38.84%)</b></td><td>199.20 (-6.35%)</td><td>333.11 <b>(+81.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>643.00 (n/a)</td><td>437.84 (n/a)</td><td>453.70 (n/a)</td><td>212.70 (n/a)</td><td>183.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (+9.84%)</td><td>0.08 <b>(+26.28%)</b></td><td>0.09 <b>(+57.42%)</b></td><td>0.06 <b>(+39.30%)</b></td><td>0.02 (-8.83%)</td><td>427.00 <b>(-28.21%)</b></td><td>319.90 <b>(-24.19%)</b></td><td>268.60 <b>(-36.47%)</b></td><td>229.10 (-8.94%)</td><td>90.73 <b>(-38.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.80 (n/a)</td><td>422.00 (n/a)</td><td>422.80 (n/a)</td><td>251.60 (n/a)</td><td>146.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 <b>(+53.87%)</b></td><td>0.10 (+5.28%)</td><td>0.09 (-7.94%)</td><td>0.04 <b>(-32.22%)</b></td><td>0.04 <b>(+138.94%)</b></td><td>605.20 <b>(+47.50%)</b></td><td>314.16 (+10.90%)</td><td>281.40 (+8.61%)</td><td>152.10 <b>(-35.03%)</b></td><td>171.99 <b>(+135.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>410.30 (n/a)</td><td>283.28 (n/a)</td><td>259.10 (n/a)</td><td>234.10 (n/a)</td><td>73.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (+12.33%)</td><td>0.08 <b>(+20.71%)</b></td><td>0.06 (+2.19%)</td><td>0.05 (+9.17%)</td><td>0.03 <b>(+37.47%)</b></td><td>483.40 (-8.41%)</td><td>350.66 (-14.34%)</td><td>383.60 (-2.14%)</td><td>221.80 (-10.96%)</td><td>118.67 (+7.33%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>527.80 (n/a)</td><td>409.38 (n/a)</td><td>392.00 (n/a)</td><td>249.10 (n/a)</td><td>110.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (-16.55%)</td><td>0.10 (+14.53%)</td><td>0.09 (+13.81%)</td><td>0.08 <b>(+90.33%)</b></td><td>0.02 <b>(-60.13%)</b></td><td>295.00 <b>(-47.46%)</b></td><td>253.52 <b>(-24.72%)</b></td><td>261.60 (-12.16%)</td><td>196.40 (+19.83%)</td><td>37.13 <b>(-75.36%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>561.50 (n/a)</td><td>336.78 (n/a)</td><td>297.80 (n/a)</td><td>163.90 (n/a)</td><td>150.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (+19.51%)</td><td>0.06 (+5.24%)</td><td>0.06 (-5.70%)</td><td>0.05 (+8.46%)</td><td>0.02 <b>(+30.37%)</b></td><td>540.00 (-7.80%)</td><td>413.60 (-3.77%)</td><td>417.10 (+6.05%)</td><td>247.70 (-16.32%)</td><td>109.05 (-5.14%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>585.70 (n/a)</td><td>429.80 (n/a)</td><td>393.30 (n/a)</td><td>296.00 (n/a)</td><td>114.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 <b>(+52.93%)</b></td><td>0.08 <b>(+48.84%)</b></td><td>0.06 (+7.89%)</td><td>0.05 <b>(+239.84%)</b></td><td>0.04 <b>(+40.42%)</b></td><td>541.30 <b>(-70.57%)</b></td><td>380.64 <b>(-47.08%)</b></td><td>414.40 (-7.31%)</td><td>163.40 <b>(-34.59%)</b></td><td>160.53 <b>(-75.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1839.50 (n/a)</td><td>719.32 (n/a)</td><td>447.10 (n/a)</td><td>249.80 (n/a)</td><td>642.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 (-6.12%)</td><td>0.14 (-2.12%)</td><td>0.13 (-10.59%)</td><td>0.09 (-11.97%)</td><td>0.04 (+16.35%)</td><td>547.50 (+13.59%)</td><td>377.00 (+4.92%)</td><td>365.90 (+11.83%)</td><td>265.90 (+6.49%)</td><td>119.20 <b>(+32.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>482.00 (n/a)</td><td>359.32 (n/a)</td><td>327.20 (n/a)</td><td>249.70 (n/a)</td><td>89.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 <b>(+23.12%)</b></td><td>0.14 (-1.71%)</td><td>0.11 <b>(-30.17%)</b></td><td>0.11 (-5.82%)</td><td>0.05 <b>(+87.91%)</b></td><td>453.60 (+6.18%)</td><td>365.76 (+7.05%)</td><td>434.00 <b>(+43.19%)</b></td><td>238.90 (-18.77%)</td><td>103.99 <b>(+67.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>427.20 (n/a)</td><td>341.68 (n/a)</td><td>303.10 (n/a)</td><td>294.10 (n/a)</td><td>62.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 <b>(-26.10%)</b></td><td>0.13 (-14.54%)</td><td>0.15 (+17.13%)</td><td>0.08 (-15.18%)</td><td>0.04 <b>(-36.55%)</b></td><td>630.70 (+17.91%)</td><td>405.02 (+12.71%)</td><td>335.90 (-14.62%)</td><td>285.80 <b>(+35.32%)</b></td><td>142.69 (+6.49%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>534.90 (n/a)</td><td>359.36 (n/a)</td><td>393.40 (n/a)</td><td>211.20 (n/a)</td><td>133.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (+7.76%)</td><td>0.16 (+1.16%)</td><td>0.17 (-3.74%)</td><td>0.08 (+0.07%)</td><td>0.06 (+10.67%)</td><td>582.60 (-0.07%)</td><td>350.78 (+0.49%)</td><td>284.70 (+3.91%)</td><td>217.10 (-7.18%)</td><td>154.60 (+3.90%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>583.00 (n/a)</td><td>349.06 (n/a)</td><td>274.00 (n/a)</td><td>233.90 (n/a)</td><td>148.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (-12.06%)</td><td>0.12 (-13.83%)</td><td>0.14 (+14.70%)</td><td>0.02 <b>(-76.87%)</b></td><td>0.06 <b>(+53.68%)</b></td><td>2072.60 <b>(+332.42%)</b></td><td>694.18 <b>(+86.36%)</b></td><td>356.50 (-12.81%)</td><td>291.60 (+13.73%)</td><td>772.79 <b>(+727.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>479.30 (n/a)</td><td>372.50 (n/a)</td><td>408.90 (n/a)</td><td>256.40 (n/a)</td><td>93.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.22 <b>(+89.58%)</b></td><td>0.15 <b>(+48.44%)</b></td><td>0.14 <b>(+39.23%)</b></td><td>0.12 <b>(+37.01%)</b></td><td>0.04 <b>(+263.33%)</b></td><td>425.00 <b>(-27.00%)</b></td><td>352.74 <b>(-29.62%)</b></td><td>359.60 <b>(-28.18%)</b></td><td>219.30 <b>(-47.26%)</b></td><td>80.19 <b>(+36.02%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>501.18 (n/a)</td><td>500.70 (n/a)</td><td>415.80 (n/a)</td><td>58.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (+5.49%)</td><td>0.01 <b>(+28.53%)</b></td><td>0.01 <b>(+49.48%)</b></td><td>0.01 (+16.52%)</td><td>0.00 (-16.24%)</td><td>439.40 (-14.20%)</td><td>295.12 <b>(-24.68%)</b></td><td>272.60 <b>(-33.10%)</b></td><td>233.90 (-5.23%)</td><td>82.43 <b>(-29.81%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.10 (n/a)</td><td>391.82 (n/a)</td><td>407.50 (n/a)</td><td>246.80 (n/a)</td><td>117.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(+24.24%)</b></td><td>0.01 <b>(+28.01%)</b></td><td>0.01 <b>(+70.67%)</b></td><td>0.00 (-1.37%)</td><td>0.00 <b>(+46.18%)</b></td><td>534.30 (+1.39%)</td><td>335.64 (-16.41%)</td><td>261.30 <b>(-41.40%)</b></td><td>194.50 (-19.53%)</td><td>155.99 <b>(+20.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>527.00 (n/a)</td><td>401.52 (n/a)</td><td>445.90 (n/a)</td><td>241.70 (n/a)</td><td>129.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(+26.97%)</b></td><td>0.01 (-13.65%)</td><td>0.01 (-4.51%)</td><td>0.00 <b>(-60.02%)</b></td><td>0.01 <b>(+912.23%)</b></td><td>626.90 <b>(+150.16%)</b></td><td>365.86 <b>(+53.54%)</b></td><td>251.80 (+4.74%)</td><td>174.80 <b>(-21.23%)</b></td><td>219.86 <b>(+2014.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>250.60 (n/a)</td><td>238.28 (n/a)</td><td>240.40 (n/a)</td><td>221.90 (n/a)</td><td>10.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (+7.36%)</td><td>0.01 (-2.15%)</td><td>0.01 (-11.87%)</td><td>0.01 (-13.93%)</td><td>0.00 <b>(+23.38%)</b></td><td>522.10 (+16.18%)</td><td>348.62 (+4.68%)</td><td>334.90 (+13.49%)</td><td>242.30 (-6.84%)</td><td>104.60 <b>(+36.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.40 (n/a)</td><td>333.02 (n/a)</td><td>295.10 (n/a)</td><td>260.10 (n/a)</td><td>76.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (-1.69%)</td><td>0.01 <b>(-20.53%)</b></td><td>0.00 <b>(-46.77%)</b></td><td>0.00 (-5.83%)</td><td>0.00 (-9.88%)</td><td>661.20 (+6.18%)</td><td>481.74 <b>(+21.35%)</b></td><td>535.10 <b>(+87.89%)</b></td><td>229.70 (+1.73%)</td><td>172.73 (-10.66%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>622.70 (n/a)</td><td>397.00 (n/a)</td><td>284.80 (n/a)</td><td>225.80 (n/a)</td><td>193.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (-0.26%)</td><td>0.01 (+1.66%)</td><td>0.01 (+4.25%)</td><td>0.00 <b>(+57.15%)</b></td><td>0.00 <b>(-22.11%)</b></td><td>676.60 <b>(-36.37%)</b></td><td>485.36 (-11.42%)</td><td>455.40 (-4.09%)</td><td>310.30 (+0.26%)</td><td>135.56 <b>(-54.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1063.30 (n/a)</td><td>547.92 (n/a)</td><td>474.80 (n/a)</td><td>309.50 (n/a)</td><td>297.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-8.07%)</td><td>0.02 (-5.25%)</td><td>0.02 (-10.97%)</td><td>0.01 (-3.40%)</td><td>0.00 (-1.69%)</td><td>464.30 (+3.52%)</td><td>346.20 (+5.87%)</td><td>335.50 (+12.32%)</td><td>257.00 (+8.76%)</td><td>85.92 (+7.89%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.50 (n/a)</td><td>327.00 (n/a)</td><td>298.70 (n/a)</td><td>236.30 (n/a)</td><td>79.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-16.81%)</td><td>0.01 <b>(-28.08%)</b></td><td>0.01 <b>(-47.28%)</b></td><td>0.01 (+2.07%)</td><td>0.00 <b>(-28.37%)</b></td><td>556.30 (-2.03%)</td><td>411.64 <b>(+32.41%)</b></td><td>450.80 <b>(+89.65%)</b></td><td>274.00 <b>(+20.23%)</b></td><td>117.40 (-19.45%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.80 (n/a)</td><td>310.88 (n/a)</td><td>237.70 (n/a)</td><td>227.90 (n/a)</td><td>145.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-12.62%)</td><td>0.02 (+2.33%)</td><td>0.02 <b>(+41.72%)</b></td><td>0.00 <b>(-56.15%)</b></td><td>0.01 (-8.31%)</td><td>1909.40 <b>(+128.04%)</b></td><td>634.34 <b>(+28.32%)</b></td><td>334.20 <b>(-29.45%)</b></td><td>206.60 (+14.40%)</td><td>721.77 <b>(+145.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>837.30 (n/a)</td><td>494.34 (n/a)</td><td>473.70 (n/a)</td><td>180.60 (n/a)</td><td>294.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+6.23%)</td><td>0.01 (-10.93%)</td><td>0.01 <b>(-34.36%)</b></td><td>0.01 <b>(+207.69%)</b></td><td>0.01 (-15.41%)</td><td>784.50 <b>(-67.50%)</b></td><td>467.40 <b>(-35.08%)</b></td><td>444.70 <b>(+52.35%)</b></td><td>212.70 (-5.84%)</td><td>217.40 <b>(-77.10%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2413.80 (n/a)</td><td>719.98 (n/a)</td><td>291.90 (n/a)</td><td>225.90 (n/a)</td><td>949.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-7.51%)</td><td>0.02 <b>(+23.39%)</b></td><td>0.02 <b>(+70.31%)</b></td><td>0.01 (-8.62%)</td><td>0.01 (+4.00%)</td><td>651.30 (+9.43%)</td><td>368.08 (-15.71%)</td><td>280.80 <b>(-41.28%)</b></td><td>227.90 (+8.11%)</td><td>182.21 <b>(+27.92%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.20 (n/a)</td><td>436.68 (n/a)</td><td>478.20 (n/a)</td><td>210.80 (n/a)</td><td>142.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(+35.71%)</b></td><td>0.01 <b>(+25.41%)</b></td><td>0.01 (+10.83%)</td><td>0.01 <b>(+28.99%)</b></td><td>0.00 <b>(+38.17%)</b></td><td>471.60 <b>(-22.49%)</b></td><td>384.02 (-19.90%)</td><td>418.80 (-9.78%)</td><td>274.80 <b>(-26.31%)</b></td><td>89.13 (-19.70%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.40 (n/a)</td><td>479.40 (n/a)</td><td>464.20 (n/a)</td><td>372.90 (n/a)</td><td>110.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (+8.35%)</td><td>0.03 <b>(+41.37%)</b></td><td>0.04 <b>(+40.46%)</b></td><td>0.02 <b>(+385.82%)</b></td><td>0.01 <b>(-50.57%)</b></td><td>424.70 <b>(-79.42%)</b></td><td>311.52 <b>(-57.32%)</b></td><td>284.90 <b>(-28.79%)</b></td><td>242.40 (-7.69%)</td><td>70.36 <b>(-90.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2063.30 (n/a)</td><td>729.84 (n/a)</td><td>400.10 (n/a)</td><td>262.60 (n/a)</td><td>759.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (+0.34%)</td><td>0.04 (+2.48%)</td><td>0.04 (-9.29%)</td><td>0.02 (+7.58%)</td><td>0.01 <b>(-28.40%)</b></td><td>443.60 (-7.06%)</td><td>311.16 (-6.46%)</td><td>285.40 (+10.24%)</td><td>244.20 (-0.37%)</td><td>78.67 <b>(-30.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>477.30 (n/a)</td><td>332.66 (n/a)</td><td>258.90 (n/a)</td><td>245.10 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (+8.83%)</td><td>0.04 <b>(+44.39%)</b></td><td>0.04 <b>(+102.04%)</b></td><td>0.03 <b>(+50.42%)</b></td><td>0.01 <b>(-26.10%)</b></td><td>398.30 <b>(-33.53%)</b></td><td>272.20 <b>(-36.97%)</b></td><td>243.00 <b>(-50.51%)</b></td><td>201.10 (-8.09%)</td><td>76.11 <b>(-53.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.20 (n/a)</td><td>431.84 (n/a)</td><td>491.00 (n/a)</td><td>218.80 (n/a)</td><td>164.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(-33.05%)</b></td><td>0.04 (+15.30%)</td><td>0.04 <b>(+87.25%)</b></td><td>0.02 <b>(+36.40%)</b></td><td>0.01 <b>(-60.34%)</b></td><td>478.10 <b>(-26.68%)</b></td><td>314.52 <b>(-29.92%)</b></td><td>287.60 <b>(-46.60%)</b></td><td>258.50 <b>(+49.34%)</b></td><td>92.56 <b>(-56.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>652.10 (n/a)</td><td>448.82 (n/a)</td><td>538.60 (n/a)</td><td>173.10 (n/a)</td><td>214.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 <b>(+45.05%)</b></td><td>0.04 <b>(+21.34%)</b></td><td>0.04 <b>(+40.26%)</b></td><td>0.02 (+5.69%)</td><td>0.02 <b>(+66.28%)</b></td><td>541.70 (-5.40%)</td><td>332.96 (-10.75%)</td><td>264.70 <b>(-28.69%)</b></td><td>162.90 <b>(-31.06%)</b></td><td>155.01 (+15.18%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.60 (n/a)</td><td>373.06 (n/a)</td><td>371.20 (n/a)</td><td>236.30 (n/a)</td><td>134.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+24.16%)</b></td><td>0.03 <b>(+54.24%)</b></td><td>0.03 <b>(+49.85%)</b></td><td>0.02 <b>(+398.78%)</b></td><td>0.01 <b>(-39.67%)</b></td><td>421.60 <b>(-79.95%)</b></td><td>348.58 <b>(-56.01%)</b></td><td>354.20 <b>(-33.27%)</b></td><td>253.50 (-19.47%)</td><td>60.91 <b>(-91.76%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2103.00 (n/a)</td><td>792.42 (n/a)</td><td>530.80 (n/a)</td><td>314.80 (n/a)</td><td>739.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (-1.03%)</td><td>0.06 (+13.29%)</td><td>0.07 <b>(+53.17%)</b></td><td>0.04 <b>(+41.77%)</b></td><td>0.02 <b>(-25.71%)</b></td><td>497.80 <b>(-29.47%)</b></td><td>352.00 (-18.80%)</td><td>305.90 <b>(-34.72%)</b></td><td>242.40 (+1.04%)</td><td>105.37 <b>(-43.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>705.80 (n/a)</td><td>433.52 (n/a)</td><td>468.60 (n/a)</td><td>239.90 (n/a)</td><td>186.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 <b>(+62.28%)</b></td><td>0.07 (+7.43%)</td><td>0.05 <b>(-34.13%)</b></td><td>0.04 <b>(+21.67%)</b></td><td>0.04 <b>(+118.75%)</b></td><td>474.30 (-17.81%)</td><td>357.92 (+2.64%)</td><td>451.40 <b>(+51.83%)</b></td><td>169.50 <b>(-38.39%)</b></td><td>143.10 (+11.68%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.10 (n/a)</td><td>348.72 (n/a)</td><td>297.30 (n/a)</td><td>275.10 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (-8.79%)</td><td>0.06 <b>(+25.54%)</b></td><td>0.07 <b>(+80.20%)</b></td><td>0.02 <b>(+76.97%)</b></td><td>0.03 (-2.94%)</td><td>1036.30 <b>(-43.49%)</b></td><td>479.08 <b>(-32.23%)</b></td><td>282.40 <b>(-44.50%)</b></td><td>264.00 (+9.63%)</td><td>331.80 <b>(-48.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1833.90 (n/a)</td><td>706.96 (n/a)</td><td>508.80 (n/a)</td><td>240.80 (n/a)</td><td>641.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (+12.05%)</td><td>0.06 (-9.42%)</td><td>0.06 (-6.49%)</td><td>0.03 <b>(-34.60%)</b></td><td>0.03 <b>(+68.86%)</b></td><td>652.40 <b>(+52.89%)</b></td><td>405.38 <b>(+23.94%)</b></td><td>340.10 (+6.95%)</td><td>216.50 (-10.76%)</td><td>180.91 <b>(+137.10%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>426.70 (n/a)</td><td>327.08 (n/a)</td><td>318.00 (n/a)</td><td>242.60 (n/a)</td><td>76.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 <b>(+22.56%)</b></td><td>0.08 <b>(+55.41%)</b></td><td>0.08 <b>(+121.99%)</b></td><td>0.04 <b>(+33.24%)</b></td><td>0.02 (+11.61%)</td><td>483.90 <b>(-24.95%)</b></td><td>301.70 <b>(-37.27%)</b></td><td>250.00 <b>(-54.95%)</b></td><td>199.00 (-18.41%)</td><td>115.39 <b>(-29.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>644.80 (n/a)</td><td>480.98 (n/a)</td><td>555.00 (n/a)</td><td>243.90 (n/a)</td><td>163.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(-20.55%)</b></td><td>0.05 (-7.62%)</td><td>0.05 (+15.10%)</td><td>0.04 <b>(+26.61%)</b></td><td>0.01 <b>(-59.84%)</b></td><td>495.80 <b>(-21.01%)</b></td><td>406.56 (-5.89%)</td><td>430.20 (-13.11%)</td><td>297.40 <b>(+25.86%)</b></td><td>75.41 <b>(-58.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>627.70 (n/a)</td><td>432.02 (n/a)</td><td>495.10 (n/a)</td><td>236.30 (n/a)</td><td>180.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>491.10 (n/a)</td><td>317.28 (n/a)</td><td>247.50 (n/a)</td><td>240.20 (n/a)</td><td>109.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>343.28 (n/a)</td><td>284.30 (n/a)</td><td>212.50 (n/a)</td><td>132.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1909.40 (n/a)</td><td>710.72 (n/a)</td><td>534.10 (n/a)</td><td>250.00 (n/a)</td><td>683.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>408.50 (n/a)</td><td>286.22 (n/a)</td><td>263.60 (n/a)</td><td>237.10 (n/a)</td><td>69.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>481.90 (n/a)</td><td>326.62 (n/a)</td><td>253.40 (n/a)</td><td>229.70 (n/a)</td><td>120.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.20 (n/a)</td><td>405.76 (n/a)</td><td>353.00 (n/a)</td><td>277.00 (n/a)</td><td>146.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>430.40 (n/a)</td><td>307.76 (n/a)</td><td>287.90 (n/a)</td><td>242.40 (n/a)</td><td>74.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>568.70 (n/a)</td><td>363.56 (n/a)</td><td>296.70 (n/a)</td><td>239.70 (n/a)</td><td>141.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>608.00 (n/a)</td><td>419.28 (n/a)</td><td>443.50 (n/a)</td><td>249.20 (n/a)</td><td>154.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 (-5.06%)</td><td>0.15 (-15.16%)</td><td>0.15 (-13.13%)</td><td>0.07 <b>(-35.40%)</b></td><td>0.06 <b>(+27.59%)</b></td><td>729.50 <b>(+54.78%)</b></td><td>395.26 <b>(+29.20%)</b></td><td>330.20 (+15.09%)</td><td>230.90 (+5.34%)</td><td>198.30 <b>(+104.92%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>471.30 (n/a)</td><td>305.94 (n/a)</td><td>286.90 (n/a)</td><td>219.20 (n/a)</td><td>96.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>490.30 (n/a)</td><td>330.88 (n/a)</td><td>288.10 (n/a)</td><td>247.50 (n/a)</td><td>100.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>604.80 (n/a)</td><td>320.98 (n/a)</td><td>244.60 (n/a)</td><td>237.10 (n/a)</td><td>159.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2452.70 (n/a)</td><td>719.04 (n/a)</td><td>270.90 (n/a)</td><td>241.20 (n/a)</td><td>970.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>285.20 (n/a)</td><td>271.54 (n/a)</td><td>278.30 (n/a)</td><td>242.30 (n/a)</td><td>17.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>378.90 (n/a)</td><td>306.08 (n/a)</td><td>294.10 (n/a)</td><td>254.90 (n/a)</td><td>49.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.30 (n/a)</td><td>379.20 (n/a)</td><td>350.10 (n/a)</td><td>273.50 (n/a)</td><td>128.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>565.90 (n/a)</td><td>409.22 (n/a)</td><td>450.60 (n/a)</td><td>225.50 (n/a)</td><td>167.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>572.70 (n/a)</td><td>400.78 (n/a)</td><td>341.80 (n/a)</td><td>307.30 (n/a)</td><td>117.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>510.80 (n/a)</td><td>351.86 (n/a)</td><td>302.50 (n/a)</td><td>257.40 (n/a)</td><td>107.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>579.10 (n/a)</td><td>370.76 (n/a)</td><td>293.90 (n/a)</td><td>243.30 (n/a)</td><td>141.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>586.80 (n/a)</td><td>377.66 (n/a)</td><td>321.80 (n/a)</td><td>259.10 (n/a)</td><td>131.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.30 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>643.10 (n/a)</td><td>436.28 (n/a)</td><td>520.40 (n/a)</td><td>166.00 (n/a)</td><td>220.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>585.10 (n/a)</td><td>384.32 (n/a)</td><td>383.70 (n/a)</td><td>235.50 (n/a)</td><td>132.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.30 (n/a)</td><td>342.82 (n/a)</td><td>273.10 (n/a)</td><td>226.20 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2472.20 (n/a)</td><td>823.16 (n/a)</td><td>501.50 (n/a)</td><td>187.60 (n/a)</td><td>931.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.80 (n/a)</td><td>341.80 (n/a)</td><td>296.10 (n/a)</td><td>248.00 (n/a)</td><td>122.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.30 (n/a)</td><td>393.70 (n/a)</td><td>316.80 (n/a)</td><td>258.10 (n/a)</td><td>151.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.00 (n/a)</td><td>463.04 (n/a)</td><td>438.60 (n/a)</td><td>280.60 (n/a)</td><td>135.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>600.40 (n/a)</td><td>487.58 (n/a)</td><td>549.40 (n/a)</td><td>348.80 (n/a)</td><td>127.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.90 (n/a)</td><td>420.28 (n/a)</td><td>483.00 (n/a)</td><td>248.50 (n/a)</td><td>154.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.40 (n/a)</td><td>355.38 (n/a)</td><td>290.10 (n/a)</td><td>203.80 (n/a)</td><td>153.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.20 (n/a)</td><td>384.58 (n/a)</td><td>313.00 (n/a)</td><td>230.50 (n/a)</td><td>180.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.90 (n/a)</td><td>347.10 (n/a)</td><td>377.00 (n/a)</td><td>206.40 (n/a)</td><td>111.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.40 (n/a)</td><td>364.32 (n/a)</td><td>296.80 (n/a)</td><td>250.90 (n/a)</td><td>126.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.30 (n/a)</td><td>415.08 (n/a)</td><td>485.20 (n/a)</td><td>217.60 (n/a)</td><td>145.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>495.80 (n/a)</td><td>313.78 (n/a)</td><td>275.50 (n/a)</td><td>230.30 (n/a)</td><td>106.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>485.40 (n/a)</td><td>343.22 (n/a)</td><td>308.80 (n/a)</td><td>264.00 (n/a)</td><td>88.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>531.30 (n/a)</td><td>400.82 (n/a)</td><td>457.90 (n/a)</td><td>230.90 (n/a)</td><td>133.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.90 (n/a)</td><td>413.22 (n/a)</td><td>480.90 (n/a)</td><td>258.10 (n/a)</td><td>133.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.90 (n/a)</td><td>406.14 (n/a)</td><td>388.30 (n/a)</td><td>248.70 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1870.30 (n/a)</td><td>748.10 (n/a)</td><td>364.70 (n/a)</td><td>281.40 (n/a)</td><td>685.10 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1890.80 (n/a)</td><td>1236.44 (n/a)</td><td>1815.70 (n/a)</td><td>291.80 (n/a)</td><td>859.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>519.30 (n/a)</td><td>371.78 (n/a)</td><td>318.20 (n/a)</td><td>314.10 (n/a)</td><td>88.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.60 (n/a)</td><td>441.28 (n/a)</td><td>485.30 (n/a)</td><td>254.40 (n/a)</td><td>104.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>469.70 (n/a)</td><td>334.70 (n/a)</td><td>301.50 (n/a)</td><td>244.00 (n/a)</td><td>95.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>464.30 (n/a)</td><td>355.08 (n/a)</td><td>367.40 (n/a)</td><td>260.30 (n/a)</td><td>82.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>652.40 (n/a)</td><td>407.04 (n/a)</td><td>387.60 (n/a)</td><td>284.80 (n/a)</td><td>146.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.57 (+0.50%)</td><td>0.39 (+2.60%)</td><td>0.38 (+13.24%)</td><td>0.12 <b>(-24.73%)</b></td><td>0.18 (+12.37%)</td><td>1798.80 <b>(+32.86%)</b></td><td>762.68 (+9.30%)</td><td>574.80 (-11.69%)</td><td>389.20 (-0.49%)</td><td>590.54 <b>(+51.95%)</b></td><td>24.25 (+0.50%)</td><td>16.84 (+2.60%)</td><td>16.42 (+13.24%)</td><td>5.25 <b>(-24.73%)</b></td><td>7.83 (+12.37%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>1353.90 (n/a)</td><td>697.76 (n/a)</td><td>650.90 (n/a)</td><td>391.10 (n/a)</td><td>388.63 (n/a)</td><td>24.13 (n/a)</td><td>16.41 (n/a)</td><td>14.50 (n/a)</td><td>6.97 (n/a)</td><td>6.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.50 (-3.20%)</td><td>0.35 (-6.29%)</td><td>0.38 (-0.48%)</td><td>0.12 <b>(-48.29%)</b></td><td>0.14 <b>(+38.33%)</b></td><td>1881.20 <b>(+93.40%)</b></td><td>818.48 <b>(+28.68%)</b></td><td>580.50 (+0.48%)</td><td>445.90 (+3.31%)</td><td>598.03 <b>(+196.58%)</b></td><td>21.17 (-3.20%)</td><td>14.89 (-6.29%)</td><td>16.26 (-0.48%)</td><td>5.02 <b>(-48.29%)</b></td><td>6.00 <b>(+38.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>972.70 (n/a)</td><td>636.08 (n/a)</td><td>577.70 (n/a)</td><td>431.60 (n/a)</td><td>201.64 (n/a)</td><td>21.86 (n/a)</td><td>15.89 (n/a)</td><td>16.34 (n/a)</td><td>9.70 (n/a)</td><td>4.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (+0.39%)</td><td>0.30 (-0.54%)</td><td>0.30 (-0.72%)</td><td>0.30 (-0.65%)</td><td>0.00 <b>(+34.68%)</b></td><td>83931.40 (+0.66%)</td><td>82841.70 (+0.55%)</td><td>82880.10 (+0.73%)</td><td>81290.40 (-0.38%)</td><td>1080.84 <b>(+35.29%)</b></td><td>211.34 (+0.39%)</td><td>207.41 (-0.54%)</td><td>207.29 (-0.72%)</td><td>204.69 (-0.65%)</td><td>2.72 <b>(+34.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83382.00 (n/a)</td><td>82388.52 (n/a)</td><td>82281.60 (n/a)</td><td>81604.50 (n/a)</td><td>798.88 (n/a)</td><td>210.53 (n/a)</td><td>208.54 (n/a)</td><td>208.79 (n/a)</td><td>206.04 (n/a)</td><td>2.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>1.02 (+0.21%)</td><td>1.00 (+0.20%)</td><td>1.00 (-0.39%)</td><td>0.98 (+1.57%)</td><td>0.02 <b>(-30.94%)</b></td><td>25651.00 (-1.55%)</td><td>25183.80 (-0.23%)</td><td>25196.50 (+0.39%)</td><td>24558.20 (-0.21%)</td><td>410.68 <b>(-32.24%)</b></td><td>699.56 (+0.21%)</td><td>682.33 (+0.20%)</td><td>681.83 (-0.39%)</td><td>669.75 (+1.57%)</td><td>11.22 <b>(-30.94%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.02 (n/a)</td><td>26054.10 (n/a)</td><td>25240.78 (n/a)</td><td>25098.40 (n/a)</td><td>24610.20 (n/a)</td><td>606.08 (n/a)</td><td>698.08 (n/a)</td><td>680.95 (n/a)</td><td>684.50 (n/a)</td><td>659.39 (n/a)</td><td>16.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.82 (-0.28%)</td><td>0.80 (-1.89%)</td><td>0.81 (-0.69%)</td><td>0.76 (-5.59%)</td><td>0.03 <b>(+200.41%)</b></td><td>99608.90 (+5.93%)</td><td>94641.78 (+2.00%)</td><td>93314.20 (+0.70%)</td><td>91887.00 (+0.28%)</td><td>3088.25 <b>(+219.87%)</b></td><td>747.87 (-0.28%)</td><td>726.70 (-1.89%)</td><td>736.43 (-0.69%)</td><td>689.89 (-5.59%)</td><td>23.13 <b>(+200.41%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94035.80 (n/a)</td><td>92786.72 (n/a)</td><td>92665.80 (n/a)</td><td>91630.00 (n/a)</td><td>965.48 (n/a)</td><td>749.97 (n/a)</td><td>740.68 (n/a)</td><td>741.58 (n/a)</td><td>730.78 (n/a)</td><td>7.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.77 (-0.56%)</td><td>0.76 (+0.13%)</td><td>0.76 (+0.40%)</td><td>0.76 (+0.19%)</td><td>0.00 <b>(-25.12%)</b></td><td>99967.30 (-0.19%)</td><td>98927.18 (-0.14%)</td><td>98742.00 (-0.40%)</td><td>98469.60 (+0.56%)</td><td>604.80 <b>(-24.76%)</b></td><td>697.88 (-0.56%)</td><td>694.67 (+0.13%)</td><td>695.95 (+0.40%)</td><td>687.42 (+0.19%)</td><td>4.22 <b>(-25.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100161.10 (n/a)</td><td>99062.94 (n/a)</td><td>99135.80 (n/a)</td><td>97918.70 (n/a)</td><td>803.87 (n/a)</td><td>701.80 (n/a)</td><td>693.73 (n/a)</td><td>693.18 (n/a)</td><td>686.09 (n/a)</td><td>5.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.80 (-0.09%)</td><td>0.79 (-0.16%)</td><td>0.79 (-0.41%)</td><td>0.79 (-0.03%)</td><td>0.01 (-8.71%)</td><td>95749.80 (+0.03%)</td><td>95033.66 (+0.16%)</td><td>95203.60 (+0.41%)</td><td>94274.20 (+0.09%)</td><td>601.64 (-8.62%)</td><td>728.93 (-0.09%)</td><td>723.13 (-0.16%)</td><td>721.82 (-0.41%)</td><td>717.70 (-0.03%)</td><td>4.58 (-8.72%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95719.10 (n/a)</td><td>94883.72 (n/a)</td><td>94812.20 (n/a)</td><td>94189.40 (n/a)</td><td>658.37 (n/a)</td><td>729.59 (n/a)</td><td>724.28 (n/a)</td><td>724.80 (n/a)</td><td>717.93 (n/a)</td><td>5.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.95 <b>(-26.19%)</b></td><td>2.90 (-19.56%)</td><td>2.76 <b>(-20.58%)</b></td><td>2.16 (-0.34%)</td><td>0.79 <b>(-35.66%)</b></td><td>4118.20 (+0.34%)</td><td>3259.92 (+19.75%)</td><td>3231.00 <b>(+25.91%)</b></td><td>2258.60 <b>(+35.48%)</b></td><td>856.98 (-9.53%)</td><td>237.70 <b>(-26.19%)</b></td><td>174.61 (-19.56%)</td><td>166.16 <b>(-20.58%)</b></td><td>130.36 (-0.34%)</td><td>47.69 <b>(-35.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.35 (n/a)</td><td>3.60 (n/a)</td><td>3.47 (n/a)</td><td>2.17 (n/a)</td><td>1.23 (n/a)</td><td>4104.20 (n/a)</td><td>2722.28 (n/a)</td><td>2566.10 (n/a)</td><td>1667.10 (n/a)</td><td>947.21 (n/a)</td><td>322.03 (n/a)</td><td>217.05 (n/a)</td><td>209.21 (n/a)</td><td>130.81 (n/a)</td><td>74.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.84 <b>(-20.25%)</b></td><td>2.78 <b>(-27.40%)</b></td><td>2.49 <b>(-41.70%)</b></td><td>2.07 (-0.49%)</td><td>0.78 <b>(-32.20%)</b></td><td>4312.30 (+0.49%)</td><td>3404.66 <b>(+32.49%)</b></td><td>3582.80 <b>(+71.53%)</b></td><td>2320.10 <b>(+25.40%)</b></td><td>886.92 (-13.42%)</td><td>231.40 <b>(-20.25%)</b></td><td>167.42 <b>(-27.40%)</b></td><td>149.85 <b>(-41.70%)</b></td><td>124.50 (-0.49%)</td><td>47.15 <b>(-32.20%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.82 (n/a)</td><td>3.83 (n/a)</td><td>4.27 (n/a)</td><td>2.08 (n/a)</td><td>1.15 (n/a)</td><td>4291.30 (n/a)</td><td>2569.66 (n/a)</td><td>2088.70 (n/a)</td><td>1850.20 (n/a)</td><td>1024.35 (n/a)</td><td>290.17 (n/a)</td><td>230.61 (n/a)</td><td>257.03 (n/a)</td><td>125.11 (n/a)</td><td>69.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.42 <b>(+32.99%)</b></td><td>4.00 <b>(+25.22%)</b></td><td>3.70 (+19.28%)</td><td>2.18 (+6.65%)</td><td>1.34 <b>(+56.48%)</b></td><td>4095.60 (-6.24%)</td><td>2484.20 (-16.60%)</td><td>2408.50 (-16.17%)</td><td>1645.30 <b>(-24.81%)</b></td><td>990.11 (+10.85%)</td><td>326.31 <b>(+32.99%)</b></td><td>240.88 <b>(+25.22%)</b></td><td>222.90 (+19.28%)</td><td>131.09 (+6.65%)</td><td>80.90 <b>(+56.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.07 (n/a)</td><td>3.19 (n/a)</td><td>3.10 (n/a)</td><td>2.04 (n/a)</td><td>0.86 (n/a)</td><td>4368.10 (n/a)</td><td>2978.72 (n/a)</td><td>2873.00 (n/a)</td><td>2188.10 (n/a)</td><td>893.22 (n/a)</td><td>245.36 (n/a)</td><td>192.37 (n/a)</td><td>186.87 (n/a)</td><td>122.91 (n/a)</td><td>51.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.66 (+2.51%)</td><td>5.62 (+4.28%)</td><td>5.68 (+13.12%)</td><td>4.16 (-16.01%)</td><td>0.95 <b>(+43.93%)</b></td><td>8385.60 (+19.06%)</td><td>6363.00 (-2.62%)</td><td>6137.00 (-11.60%)</td><td>5235.60 (-2.45%)</td><td>1223.64 <b>(+69.98%)</b></td><td>410.17 (+2.51%)</td><td>346.42 (+4.28%)</td><td>349.92 (+13.12%)</td><td>256.09 (-16.01%)</td><td>58.62 <b>(+43.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.50 (n/a)</td><td>5.39 (n/a)</td><td>5.02 (n/a)</td><td>4.95 (n/a)</td><td>0.66 (n/a)</td><td>7043.30 (n/a)</td><td>6534.52 (n/a)</td><td>6942.40 (n/a)</td><td>5367.10 (n/a)</td><td>719.87 (n/a)</td><td>400.12 (n/a)</td><td>332.22 (n/a)</td><td>309.33 (n/a)</td><td>304.90 (n/a)</td><td>40.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.55 (-9.92%)</td><td>4.71 (-8.88%)</td><td>4.38 (-9.19%)</td><td>4.15 (-4.16%)</td><td>0.67 (-19.71%)</td><td>8409.30 (+4.34%)</td><td>7518.30 (+9.24%)</td><td>7959.40 (+10.12%)</td><td>6282.80 (+11.02%)</td><td>1016.24 (-4.87%)</td><td>341.80 (-9.92%)</td><td>290.07 (-8.88%)</td><td>269.81 (-9.19%)</td><td>255.37 (-4.16%)</td><td>41.09 (-19.71%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.16 (n/a)</td><td>5.17 (n/a)</td><td>4.82 (n/a)</td><td>4.33 (n/a)</td><td>0.83 (n/a)</td><td>8059.80 (n/a)</td><td>6882.60 (n/a)</td><td>7228.10 (n/a)</td><td>5659.20 (n/a)</td><td>1068.23 (n/a)</td><td>379.47 (n/a)</td><td>318.35 (n/a)</td><td>297.10 (n/a)</td><td>266.44 (n/a)</td><td>51.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.80 (-0.28%)</td><td>5.18 (+5.48%)</td><td>5.18 (+4.70%)</td><td>4.52 <b>(+26.99%)</b></td><td>0.57 <b>(-33.48%)</b></td><td>7721.90 <b>(-21.25%)</b></td><td>6792.78 (-6.96%)</td><td>6730.10 (-4.49%)</td><td>6010.40 (+0.28%)</td><td>758.22 <b>(-49.13%)</b></td><td>357.30 (-0.28%)</td><td>319.29 (+5.48%)</td><td>319.09 (+4.70%)</td><td>278.10 <b>(+26.99%)</b></td><td>35.33 <b>(-33.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.82 (n/a)</td><td>4.91 (n/a)</td><td>4.95 (n/a)</td><td>3.56 (n/a)</td><td>0.86 (n/a)</td><td>9805.90 (n/a)</td><td>7301.14 (n/a)</td><td>7046.70 (n/a)</td><td>5993.70 (n/a)</td><td>1490.47 (n/a)</td><td>358.29 (n/a)</td><td>302.71 (n/a)</td><td>304.75 (n/a)</td><td>219.00 (n/a)</td><td>53.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.78 (-0.08%)</td><td>0.77 (+1.77%)</td><td>0.77 (+1.42%)</td><td>0.76 (+3.20%)</td><td>0.01 <b>(-57.88%)</b></td><td>99545.00 (-3.10%)</td><td>98450.58 (-1.78%)</td><td>98574.20 (-1.40%)</td><td>96914.10 (+0.08%)</td><td>954.29 <b>(-59.28%)</b></td><td>709.08 (-0.08%)</td><td>698.06 (+1.77%)</td><td>697.13 (+1.42%)</td><td>690.34 (+3.20%)</td><td>6.81 <b>(-57.88%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102731.40 (n/a)</td><td>100232.70 (n/a)</td><td>99977.90 (n/a)</td><td>96837.20 (n/a)</td><td>2343.32 (n/a)</td><td>709.64 (n/a)</td><td>685.90 (n/a)</td><td>687.35 (n/a)</td><td>668.92 (n/a)</td><td>16.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.78 (+0.96%)</td><td>0.75 (-1.17%)</td><td>0.75 (-1.28%)</td><td>0.72 (-4.09%)</td><td>0.02 <b>(+180.71%)</b></td><td>104853.40 (+4.26%)</td><td>100571.72 (+1.25%)</td><td>100666.70 (+1.29%)</td><td>96932.50 (-0.95%)</td><td>3108.38 <b>(+189.67%)</b></td><td>708.94 (+0.96%)</td><td>683.81 (-1.17%)</td><td>682.64 (-1.28%)</td><td>655.39 (-4.09%)</td><td>21.03 <b>(+180.71%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100567.80 (n/a)</td><td>99330.92 (n/a)</td><td>99381.90 (n/a)</td><td>97866.30 (n/a)</td><td>1073.09 (n/a)</td><td>702.18 (n/a)</td><td>691.89 (n/a)</td><td>691.47 (n/a)</td><td>683.32 (n/a)</td><td>7.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.81 (-0.89%)</td><td>0.80 (+0.48%)</td><td>0.80 (+0.40%)</td><td>0.80 (+1.38%)</td><td>0.00 <b>(-73.78%)</b></td><td>94344.80 (-1.36%)</td><td>93970.78 (-0.48%)</td><td>93955.80 (-0.40%)</td><td>93685.00 (+0.90%)</td><td>275.55 <b>(-73.89%)</b></td><td>733.52 (-0.89%)</td><td>731.29 (+0.48%)</td><td>731.40 (+0.40%)</td><td>728.39 (+1.38%)</td><td>2.14 <b>(-73.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95644.80 (n/a)</td><td>94426.88 (n/a)</td><td>94330.10 (n/a)</td><td>92850.50 (n/a)</td><td>1055.45 (n/a)</td><td>740.11 (n/a)</td><td>727.83 (n/a)</td><td>728.50 (n/a)</td><td>718.49 (n/a)</td><td>8.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.37 (-2.46%)</td><td>2.60 (+1.81%)</td><td>3.14 <b>(+28.60%)</b></td><td>1.58 (-5.75%)</td><td>0.93 (+7.03%)</td><td>5113.40 (+6.10%)</td><td>3503.32 (+0.99%)</td><td>2565.40 <b>(-22.24%)</b></td><td>2389.90 (+2.52%)</td><td>1428.54 <b>(+20.87%)</b></td><td>884.51 (-2.46%)</td><td>682.68 (+1.81%)</td><td>824.00 <b>(+28.60%)</b></td><td>413.41 (-5.75%)</td><td>243.31 (+7.03%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.46 (n/a)</td><td>2.56 (n/a)</td><td>2.44 (n/a)</td><td>1.67 (n/a)</td><td>0.87 (n/a)</td><td>4819.30 (n/a)</td><td>3468.88 (n/a)</td><td>3299.20 (n/a)</td><td>2331.20 (n/a)</td><td>1181.92 (n/a)</td><td>906.79 (n/a)</td><td>670.58 (n/a)</td><td>640.74 (n/a)</td><td>438.63 (n/a)</td><td>227.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (-14.78%)</td><td>0.18 (-15.24%)</td><td>0.17 (-18.51%)</td><td>0.14 (-18.35%)</td><td>0.03 (-16.45%)</td><td>8991.90 <b>(+22.48%)</b></td><td>7180.48 (+17.87%)</td><td>7144.00 <b>(+22.71%)</b></td><td>5313.20 (+17.35%)</td><td>1310.71 (+16.61%)</td><td>12.63 (-14.78%)</td><td>9.62 (-15.24%)</td><td>9.39 (-18.51%)</td><td>7.46 (-18.35%)</td><td>1.88 (-16.45%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>7341.60 (n/a)</td><td>6091.64 (n/a)</td><td>5821.90 (n/a)</td><td>4527.80 (n/a)</td><td>1124.04 (n/a)</td><td>14.82 (n/a)</td><td>11.34 (n/a)</td><td>11.53 (n/a)</td><td>9.14 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.82 (n/a)</td><td>3.72 (n/a)</td><td>3.79 (n/a)</td><td>3.59 (n/a)</td><td>0.11 (n/a)</td><td>3.82 (n/a)</td><td>3.72 (n/a)</td><td>3.79 (n/a)</td><td>3.58 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.70 (+2.03%)</td><td>6.91 (+3.60%)</td><td>7.26 (+3.23%)</td><td>5.19 (-9.30%)</td><td>1.03 (+19.04%)</td><td>7.69 (+2.03%)</td><td>6.91 (+3.60%)</td><td>7.25 (+3.23%)</td><td>5.18 (-9.30%)</td><td>1.03 (+19.04%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.55 (n/a)</td><td>6.67 (n/a)</td><td>7.03 (n/a)</td><td>5.72 (n/a)</td><td>0.87 (n/a)</td><td>7.54 (n/a)</td><td>6.67 (n/a)</td><td>7.03 (n/a)</td><td>5.71 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>12.54 (-8.13%)</td><td>9.33 (-8.19%)</td><td>8.21 (-19.34%)</td><td>8.00 <b>(+30.41%)</b></td><td>1.94 <b>(-35.28%)</b></td><td>12.53 (-8.13%)</td><td>9.33 (-8.19%)</td><td>8.20 (-19.34%)</td><td>7.99 <b>(+30.41%)</b></td><td>1.93 <b>(-35.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>13.65 (n/a)</td><td>10.17 (n/a)</td><td>10.18 (n/a)</td><td>6.13 (n/a)</td><td>2.99 (n/a)</td><td>13.64 (n/a)</td><td>10.16 (n/a)</td><td>10.17 (n/a)</td><td>6.13 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.82 (n/a)</td><td>3.59 (n/a)</td><td>3.62 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td><td>3.82 (n/a)</td><td>3.59 (n/a)</td><td>3.61 (n/a)</td><td>3.32 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.77 (-8.61%)</td><td>6.19 (-3.13%)</td><td>6.57 (+1.11%)</td><td>5.46 (+4.28%)</td><td>0.63 <b>(-35.77%)</b></td><td>6.77 (-8.61%)</td><td>6.18 (-3.13%)</td><td>6.56 (+1.11%)</td><td>5.45 (+4.28%)</td><td>0.63 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.41 (n/a)</td><td>6.39 (n/a)</td><td>6.50 (n/a)</td><td>5.23 (n/a)</td><td>0.98 (n/a)</td><td>7.40 (n/a)</td><td>6.38 (n/a)</td><td>6.49 (n/a)</td><td>5.23 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>14.00 (+4.08%)</td><td>11.55 <b>(+25.21%)</b></td><td>13.41 <b>(+58.75%)</b></td><td>8.31 (+13.06%)</td><td>2.95 <b>(+22.51%)</b></td><td>13.99 (+4.08%)</td><td>11.54 <b>(+25.21%)</b></td><td>13.41 <b>(+58.75%)</b></td><td>8.31 (+13.06%)</td><td>2.95 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>13.45 (n/a)</td><td>9.22 (n/a)</td><td>8.45 (n/a)</td><td>7.35 (n/a)</td><td>2.41 (n/a)</td><td>13.44 (n/a)</td><td>9.22 (n/a)</td><td>8.44 (n/a)</td><td>7.35 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.06 (+2.85%)</td><td>1.82 <b>(-24.69%)</b></td><td>1.18 <b>(-57.15%)</b></td><td>1.06 <b>(-30.34%)</b></td><td>0.97 <b>(+55.49%)</b></td><td>3.06 (+2.85%)</td><td>1.81 <b>(-24.69%)</b></td><td>1.18 <b>(-57.15%)</b></td><td>1.05 <b>(-30.34%)</b></td><td>0.96 <b>(+55.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.98 (n/a)</td><td>2.41 (n/a)</td><td>2.75 (n/a)</td><td>1.51 (n/a)</td><td>0.62 (n/a)</td><td>2.97 (n/a)</td><td>2.41 (n/a)</td><td>2.75 (n/a)</td><td>1.51 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.62 (+11.26%)</td><td>0.32 (-12.97%)</td><td>0.25 <b>(-24.02%)</b></td><td>0.09 (+13.89%)</td><td>0.20 (+2.08%)</td><td>0.61 (+11.26%)</td><td>0.31 (-12.97%)</td><td>0.25 <b>(-24.02%)</b></td><td>0.09 (+13.89%)</td><td>0.20 (+2.08%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.55 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.76 (+3.34%)</td><td>0.37 <b>(-23.34%)</b></td><td>0.31 <b>(-52.07%)</b></td><td>0.08 (+4.72%)</td><td>0.25 (-12.31%)</td><td>0.75 (+3.34%)</td><td>0.36 <b>(-23.34%)</b></td><td>0.30 <b>(-52.07%)</b></td><td>0.08 (+4.72%)</td><td>0.25 (-12.31%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.74 (n/a)</td><td>0.48 (n/a)</td><td>0.64 (n/a)</td><td>0.07 (n/a)</td><td>0.28 (n/a)</td><td>0.73 (n/a)</td><td>0.47 (n/a)</td><td>0.64 (n/a)</td><td>0.07 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.83 (+5.59%)</td><td>2.11 <b>(+33.32%)</b></td><td>2.40 <b>(+61.27%)</b></td><td>1.36 <b>(+201.94%)</b></td><td>0.65 <b>(-27.53%)</b></td><td>2.79 (+5.59%)</td><td>2.07 <b>(+33.32%)</b></td><td>2.36 <b>(+61.27%)</b></td><td>1.34 <b>(+201.94%)</b></td><td>0.64 <b>(-27.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.68 (n/a)</td><td>1.58 (n/a)</td><td>1.49 (n/a)</td><td>0.45 (n/a)</td><td>0.90 (n/a)</td><td>2.64 (n/a)</td><td>1.56 (n/a)</td><td>1.46 (n/a)</td><td>0.44 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.30 (n/a)</td><td>342.30 (n/a)</td><td>307.30 (n/a)</td><td>215.30 (n/a)</td><td>123.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.60 (n/a)</td><td>339.68 (n/a)</td><td>340.30 (n/a)</td><td>235.20 (n/a)</td><td>102.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1932.20 (n/a)</td><td>707.86 (n/a)</td><td>416.80 (n/a)</td><td>275.30 (n/a)</td><td>689.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.70 (n/a)</td><td>396.74 (n/a)</td><td>318.10 (n/a)</td><td>240.30 (n/a)</td><td>158.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.40 (n/a)</td><td>421.58 (n/a)</td><td>467.80 (n/a)</td><td>246.70 (n/a)</td><td>145.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.70 (n/a)</td><td>418.20 (n/a)</td><td>377.90 (n/a)</td><td>340.70 (n/a)</td><td>82.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.70 (n/a)</td><td>349.48 (n/a)</td><td>290.30 (n/a)</td><td>247.20 (n/a)</td><td>107.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.50 (n/a)</td><td>334.52 (n/a)</td><td>244.60 (n/a)</td><td>228.30 (n/a)</td><td>132.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2421.30 (n/a)</td><td>739.70 (n/a)</td><td>366.00 (n/a)</td><td>218.10 (n/a)</td><td>944.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.20 (n/a)</td><td>383.78 (n/a)</td><td>269.10 (n/a)</td><td>223.40 (n/a)</td><td>181.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.80 (n/a)</td><td>350.12 (n/a)</td><td>301.40 (n/a)</td><td>245.60 (n/a)</td><td>105.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>451.64 (n/a)</td><td>467.80 (n/a)</td><td>280.40 (n/a)</td><td>128.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.70 (n/a)</td><td>369.90 (n/a)</td><td>336.20 (n/a)</td><td>309.70 (n/a)</td><td>72.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.00 (n/a)</td><td>443.68 (n/a)</td><td>488.30 (n/a)</td><td>243.80 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.20 (n/a)</td><td>384.48 (n/a)</td><td>369.00 (n/a)</td><td>242.10 (n/a)</td><td>152.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>429.60 (n/a)</td><td>319.90 (n/a)</td><td>278.90 (n/a)</td><td>261.00 (n/a)</td><td>71.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>488.70 (n/a)</td><td>370.88 (n/a)</td><td>374.40 (n/a)</td><td>267.30 (n/a)</td><td>93.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1911.50 (n/a)</td><td>721.92 (n/a)</td><td>458.70 (n/a)</td><td>273.20 (n/a)</td><td>671.10 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>567.90 (n/a)</td><td>384.16 (n/a)</td><td>390.50 (n/a)</td><td>268.90 (n/a)</td><td>117.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>310.60 (n/a)</td><td>281.78 (n/a)</td><td>301.50 (n/a)</td><td>237.60 (n/a)</td><td>33.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>607.50 (n/a)</td><td>380.06 (n/a)</td><td>291.70 (n/a)</td><td>265.90 (n/a)</td><td>152.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>585.70 (n/a)</td><td>370.40 (n/a)</td><td>255.50 (n/a)</td><td>230.20 (n/a)</td><td>180.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>623.40 (n/a)</td><td>487.40 (n/a)</td><td>485.80 (n/a)</td><td>297.60 (n/a)</td><td>125.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>684.70 (n/a)</td><td>436.36 (n/a)</td><td>380.60 (n/a)</td><td>280.30 (n/a)</td><td>159.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(+29.30%)</b></td><td>0.01 (+3.62%)</td><td>0.01 <b>(-26.31%)</b></td><td>0.01 (-11.61%)</td><td>0.01 <b>(+108.96%)</b></td><td>578.60 (+13.14%)</td><td>419.94 (+8.34%)</td><td>507.20 <b>(+35.69%)</b></td><td>213.20 <b>(-22.67%)</b></td><td>165.30 <b>(+85.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.40 (n/a)</td><td>387.62 (n/a)</td><td>373.80 (n/a)</td><td>275.70 (n/a)</td><td>89.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-33.79%)</b></td><td>0.01 <b>(-26.70%)</b></td><td>0.01 <b>(-26.39%)</b></td><td>0.01 (-6.49%)</td><td>0.00 <b>(-52.40%)</b></td><td>554.00 (+6.95%)</td><td>459.42 <b>(+24.32%)</b></td><td>480.00 <b>(+35.82%)</b></td><td>291.20 <b>(+51.04%)</b></td><td>99.75 <b>(-31.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>369.56 (n/a)</td><td>353.40 (n/a)</td><td>192.80 (n/a)</td><td>145.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-12.12%)</td><td>0.01 (-9.79%)</td><td>0.01 (-3.45%)</td><td>0.01 <b>(+226.63%)</b></td><td>0.00 <b>(-40.02%)</b></td><td>582.70 <b>(-69.38%)</b></td><td>490.70 <b>(-29.41%)</b></td><td>549.30 (+3.58%)</td><td>251.50 (+13.80%)</td><td>138.71 <b>(-79.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.20 (n/a)</td><td>695.18 (n/a)</td><td>530.30 (n/a)</td><td>221.00 (n/a)</td><td>691.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (-3.52%)</td><td>0.01 (-18.85%)</td><td>0.01 <b>(-41.69%)</b></td><td>0.01 (+8.12%)</td><td>0.00 <b>(-26.70%)</b></td><td>546.30 (-7.52%)</td><td>465.56 (+17.38%)</td><td>504.70 <b>(+71.49%)</b></td><td>291.80 (+3.66%)</td><td>104.88 <b>(-29.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.70 (n/a)</td><td>396.62 (n/a)</td><td>294.30 (n/a)</td><td>281.50 (n/a)</td><td>148.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+13.30%)</td><td>0.01 (+10.54%)</td><td>0.01 (-2.80%)</td><td>0.01 <b>(+23.86%)</b></td><td>0.00 <b>(+24.83%)</b></td><td>530.60 (-19.26%)</td><td>413.86 (-7.93%)</td><td>458.90 (+2.87%)</td><td>234.90 (-11.72%)</td><td>131.96 (-5.56%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>657.20 (n/a)</td><td>449.50 (n/a)</td><td>446.10 (n/a)</td><td>266.10 (n/a)</td><td>139.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+6.87%)</td><td>0.01 (+2.80%)</td><td>0.01 (-12.54%)</td><td>0.01 (-2.37%)</td><td>0.01 (+15.80%)</td><td>625.60 (+2.42%)</td><td>479.70 (+1.72%)</td><td>582.00 (+14.34%)</td><td>209.30 (-6.44%)</td><td>181.23 (+19.91%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.80 (n/a)</td><td>471.60 (n/a)</td><td>509.00 (n/a)</td><td>223.70 (n/a)</td><td>151.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (+2.10%)</td><td>0.02 <b>(-27.04%)</b></td><td>0.02 <b>(-44.66%)</b></td><td>0.01 (-19.22%)</td><td>0.01 <b>(+21.91%)</b></td><td>601.80 <b>(+23.78%)</b></td><td>487.86 <b>(+42.46%)</b></td><td>519.20 <b>(+80.72%)</b></td><td>256.60 (-2.06%)</td><td>136.48 <b>(+41.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.20 (n/a)</td><td>342.46 (n/a)</td><td>287.30 (n/a)</td><td>262.00 (n/a)</td><td>96.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (-1.77%)</td><td>0.03 (-2.33%)</td><td>0.03 (-16.55%)</td><td>0.02 (-3.11%)</td><td>0.01 <b>(-23.59%)</b></td><td>517.10 (+3.21%)</td><td>323.82 (-1.88%)</td><td>287.90 (+19.81%)</td><td>225.80 (+1.80%)</td><td>113.18 (-15.15%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.00 (n/a)</td><td>330.04 (n/a)</td><td>240.30 (n/a)</td><td>221.80 (n/a)</td><td>133.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(-41.91%)</b></td><td>0.03 (-6.14%)</td><td>0.03 <b>(+26.93%)</b></td><td>0.02 (+18.69%)</td><td>0.01 <b>(-66.88%)</b></td><td>480.00 (-15.75%)</td><td>334.86 (-9.64%)</td><td>307.90 <b>(-21.21%)</b></td><td>267.50 <b>(+72.14%)</b></td><td>83.87 <b>(-48.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>569.70 (n/a)</td><td>370.60 (n/a)</td><td>390.80 (n/a)</td><td>155.40 (n/a)</td><td>161.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-12.33%)</td><td>0.02 <b>(+39.42%)</b></td><td>0.03 <b>(+107.25%)</b></td><td>0.01 <b>(+31.66%)</b></td><td>0.01 <b>(-25.75%)</b></td><td>663.20 <b>(-24.04%)</b></td><td>376.60 <b>(-33.68%)</b></td><td>293.40 <b>(-51.75%)</b></td><td>278.60 (+14.09%)</td><td>163.30 <b>(-30.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>873.10 (n/a)</td><td>567.84 (n/a)</td><td>608.10 (n/a)</td><td>244.20 (n/a)</td><td>233.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(-38.87%)</b></td><td>0.02 (-12.25%)</td><td>0.02 (+13.62%)</td><td>0.02 <b>(+35.91%)</b></td><td>0.01 <b>(-62.37%)</b></td><td>522.50 <b>(-26.43%)</b></td><td>403.50 (-7.78%)</td><td>406.10 (-11.99%)</td><td>298.30 <b>(+63.63%)</b></td><td>100.68 <b>(-55.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>710.20 (n/a)</td><td>437.54 (n/a)</td><td>461.40 (n/a)</td><td>182.30 (n/a)</td><td>224.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(-21.91%)</b></td><td>0.02 (-15.91%)</td><td>0.02 <b>(-21.04%)</b></td><td>0.01 (-10.57%)</td><td>0.01 <b>(-36.77%)</b></td><td>651.10 (+11.83%)</td><td>474.96 (+13.47%)</td><td>458.90 <b>(+26.63%)</b></td><td>310.40 <b>(+28.05%)</b></td><td>121.59 (-15.57%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>418.56 (n/a)</td><td>362.40 (n/a)</td><td>242.40 (n/a)</td><td>144.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(-21.16%)</b></td><td>0.02 (-5.36%)</td><td>0.02 (+6.28%)</td><td>0.01 (-3.17%)</td><td>0.00 <b>(-36.61%)</b></td><td>662.20 (+3.28%)</td><td>457.92 (+2.12%)</td><td>438.80 (-5.90%)</td><td>348.50 <b>(+26.87%)</b></td><td>120.94 (-11.98%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.20 (n/a)</td><td>448.40 (n/a)</td><td>466.30 (n/a)</td><td>274.70 (n/a)</td><td>137.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+8.52%)</td><td>0.02 (-10.00%)</td><td>0.01 <b>(-24.55%)</b></td><td>0.01 (+0.29%)</td><td>0.00 (+3.94%)</td><td>635.40 (-0.28%)</td><td>526.20 (+10.85%)</td><td>568.40 <b>(+32.53%)</b></td><td>333.60 (-7.87%)</td><td>116.05 (-7.62%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.20 (n/a)</td><td>474.68 (n/a)</td><td>428.90 (n/a)</td><td>362.10 (n/a)</td><td>125.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(-42.45%)</b></td><td>0.04 <b>(-21.92%)</b></td><td>0.03 (+2.53%)</td><td>0.03 <b>(+28.07%)</b></td><td>0.01 <b>(-60.85%)</b></td><td>518.10 <b>(-21.91%)</b></td><td>445.42 (+2.18%)</td><td>502.00 (-2.45%)</td><td>250.90 <b>(+73.75%)</b></td><td>111.47 <b>(-46.85%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>663.50 (n/a)</td><td>435.92 (n/a)</td><td>514.60 (n/a)</td><td>144.40 (n/a)</td><td>209.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(-24.14%)</b></td><td>0.04 (+5.26%)</td><td>0.04 (+10.63%)</td><td>0.03 <b>(+103.19%)</b></td><td>0.00 <b>(-68.98%)</b></td><td>502.40 <b>(-50.78%)</b></td><td>433.20 (-19.66%)</td><td>439.80 (-9.62%)</td><td>370.30 <b>(+31.83%)</b></td><td>54.24 <b>(-80.98%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1020.80 (n/a)</td><td>539.20 (n/a)</td><td>486.60 (n/a)</td><td>280.90 (n/a)</td><td>285.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (-17.53%)</td><td>0.05 (-3.68%)</td><td>0.04 (-17.14%)</td><td>0.03 (-15.89%)</td><td>0.02 (-11.91%)</td><td>602.90 (+18.87%)</td><td>394.78 (+5.43%)</td><td>444.00 <b>(+20.68%)</b></td><td>212.00 <b>(+21.21%)</b></td><td>163.80 <b>(+24.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>507.20 (n/a)</td><td>374.44 (n/a)</td><td>367.90 (n/a)</td><td>174.90 (n/a)</td><td>131.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (-5.42%)</td><td>0.04 (-2.95%)</td><td>0.04 (+1.05%)</td><td>0.02 <b>(-42.84%)</b></td><td>0.02 (+17.15%)</td><td>1033.30 <b>(+74.93%)</b></td><td>490.18 (+18.68%)</td><td>418.10 (-1.04%)</td><td>246.00 (+5.72%)</td><td>319.02 <b>(+118.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.70 (n/a)</td><td>413.04 (n/a)</td><td>422.50 (n/a)</td><td>232.70 (n/a)</td><td>146.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+3.35%)</td><td>0.05 (-3.09%)</td><td>0.05 (-7.95%)</td><td>0.03 (-7.83%)</td><td>0.02 (+9.76%)</td><td>545.30 (+8.50%)</td><td>381.32 (+5.06%)</td><td>332.30 (+8.63%)</td><td>245.90 (-3.23%)</td><td>130.52 (+15.20%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.60 (n/a)</td><td>362.94 (n/a)</td><td>305.90 (n/a)</td><td>254.10 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 <b>(-30.56%)</b></td><td>0.04 (-0.25%)</td><td>0.04 (+17.09%)</td><td>0.03 (-3.79%)</td><td>0.01 <b>(-41.97%)</b></td><td>633.40 (+3.94%)</td><td>436.36 (-6.06%)</td><td>429.00 (-14.59%)</td><td>304.90 <b>(+43.96%)</b></td><td>136.72 (-10.47%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>609.40 (n/a)</td><td>464.52 (n/a)</td><td>502.30 (n/a)</td><td>211.80 (n/a)</td><td>152.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (+7.83%)</td><td>0.10 (-3.14%)</td><td>0.11 (-2.98%)</td><td>0.05 <b>(-30.91%)</b></td><td>0.03 <b>(+62.57%)</b></td><td>603.20 <b>(+44.72%)</b></td><td>368.88 (+10.90%)</td><td>301.20 (+3.08%)</td><td>252.70 (-7.27%)</td><td>145.37 <b>(+116.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>416.80 (n/a)</td><td>332.62 (n/a)</td><td>292.20 (n/a)</td><td>272.50 (n/a)</td><td>67.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 <b>(-20.39%)</b></td><td>0.11 <b>(+36.70%)</b></td><td>0.12 <b>(+71.57%)</b></td><td>0.07 <b>(+298.35%)</b></td><td>0.02 <b>(-53.36%)</b></td><td>467.40 <b>(-74.89%)</b></td><td>319.30 <b>(-53.73%)</b></td><td>277.10 <b>(-41.70%)</b></td><td>249.20 <b>(+25.60%)</b></td><td>89.62 <b>(-86.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1861.70 (n/a)</td><td>690.12 (n/a)</td><td>475.30 (n/a)</td><td>198.40 (n/a)</td><td>665.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (-8.43%)</td><td>0.07 (-18.32%)</td><td>0.06 (-11.32%)</td><td>0.01 <b>(-77.56%)</b></td><td>0.05 <b>(+30.46%)</b></td><td>2396.80 <b>(+345.67%)</b></td><td>807.84 <b>(+103.47%)</b></td><td>506.60 (+12.78%)</td><td>244.60 (+9.20%)</td><td>898.78 <b>(+594.17%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>537.80 (n/a)</td><td>397.04 (n/a)</td><td>449.20 (n/a)</td><td>224.00 (n/a)</td><td>129.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (-12.21%)</td><td>0.09 (-18.66%)</td><td>0.08 <b>(-36.81%)</b></td><td>0.07 <b>(+120.66%)</b></td><td>0.02 <b>(-45.90%)</b></td><td>499.10 <b>(-54.68%)</b></td><td>394.72 (-7.42%)</td><td>417.40 <b>(+58.23%)</b></td><td>275.90 (+13.91%)</td><td>100.53 <b>(-73.38%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1101.40 (n/a)</td><td>426.34 (n/a)</td><td>263.80 (n/a)</td><td>242.20 (n/a)</td><td>377.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 <b>(-24.34%)</b></td><td>0.06 <b>(-37.63%)</b></td><td>0.06 (-18.38%)</td><td>0.02 <b>(-66.91%)</b></td><td>0.04 (+1.96%)</td><td>1912.50 <b>(+202.23%)</b></td><td>1003.72 <b>(+139.00%)</b></td><td>547.20 <b>(+22.50%)</b></td><td>288.00 <b>(+32.17%)</b></td><td>789.23 <b>(+384.25%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>632.80 (n/a)</td><td>419.96 (n/a)</td><td>446.70 (n/a)</td><td>217.90 (n/a)</td><td>162.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (-18.81%)</td><td>0.01 <b>(-21.29%)</b></td><td>0.01 <b>(-24.64%)</b></td><td>0.01 (-11.08%)</td><td>0.00 (-13.65%)</td><td>494.10 (+12.45%)</td><td>392.00 <b>(+27.32%)</b></td><td>386.30 <b>(+32.70%)</b></td><td>295.80 <b>(+23.20%)</b></td><td>97.36 (+19.77%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.40 (n/a)</td><td>307.88 (n/a)</td><td>291.10 (n/a)</td><td>240.10 (n/a)</td><td>81.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-9.55%)</td><td>0.01 <b>(-25.59%)</b></td><td>0.01 <b>(-24.64%)</b></td><td>0.01 <b>(-47.74%)</b></td><td>0.00 <b>(+159.40%)</b></td><td>543.70 <b>(+91.31%)</b></td><td>360.46 <b>(+43.09%)</b></td><td>332.90 <b>(+32.74%)</b></td><td>253.40 (+10.56%)</td><td>112.66 <b>(+456.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>284.20 (n/a)</td><td>251.92 (n/a)</td><td>250.80 (n/a)</td><td>229.20 (n/a)</td><td>20.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-9.89%)</td><td>0.01 <b>(-20.53%)</b></td><td>0.01 <b>(-31.11%)</b></td><td>0.01 (-2.31%)</td><td>0.00 <b>(-26.10%)</b></td><td>540.70 (+2.37%)</td><td>420.14 <b>(+21.75%)</b></td><td>427.10 <b>(+45.17%)</b></td><td>269.70 (+10.99%)</td><td>107.28 (-13.66%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>345.08 (n/a)</td><td>294.20 (n/a)</td><td>243.00 (n/a)</td><td>124.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+5.37%)</td><td>0.01 (-1.84%)</td><td>0.01 (+8.17%)</td><td>0.01 (-11.46%)</td><td>0.00 (+8.74%)</td><td>510.20 (+12.95%)</td><td>327.30 (+3.79%)</td><td>292.10 (-7.53%)</td><td>221.40 (-5.10%)</td><td>110.14 <b>(+24.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>451.70 (n/a)</td><td>315.34 (n/a)</td><td>315.90 (n/a)</td><td>233.30 (n/a)</td><td>88.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-8.70%)</td><td>0.01 <b>(-24.71%)</b></td><td>0.01 <b>(-38.66%)</b></td><td>0.01 <b>(-24.74%)</b></td><td>0.00 (+3.33%)</td><td>606.80 <b>(+32.87%)</b></td><td>417.38 <b>(+38.31%)</b></td><td>465.20 <b>(+63.00%)</b></td><td>237.00 (+9.57%)</td><td>149.60 <b>(+51.25%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.70 (n/a)</td><td>301.78 (n/a)</td><td>285.40 (n/a)</td><td>216.30 (n/a)</td><td>98.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-3.91%)</td><td>0.01 (-5.53%)</td><td>0.01 (+5.77%)</td><td>0.01 (-7.78%)</td><td>0.00 (+2.21%)</td><td>510.10 (+8.44%)</td><td>361.48 (+7.64%)</td><td>294.60 (-5.46%)</td><td>251.40 (+4.06%)</td><td>122.59 <b>(+21.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>470.40 (n/a)</td><td>335.82 (n/a)</td><td>311.60 (n/a)</td><td>241.60 (n/a)</td><td>100.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-38.42%)</b></td><td>0.01 <b>(-29.21%)</b></td><td>0.01 (-16.31%)</td><td>0.01 (-11.71%)</td><td>0.00 <b>(-64.09%)</b></td><td>649.70 (+13.27%)</td><td>500.18 <b>(+28.91%)</b></td><td>506.20 (+19.50%)</td><td>381.30 <b>(+62.39%)</b></td><td>102.92 <b>(-29.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.60 (n/a)</td><td>388.02 (n/a)</td><td>423.60 (n/a)</td><td>234.80 (n/a)</td><td>145.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-7.86%)</td><td>0.01 (-4.91%)</td><td>0.01 <b>(-29.93%)</b></td><td>0.01 <b>(+26.15%)</b></td><td>0.00 <b>(-28.56%)</b></td><td>455.80 <b>(-20.73%)</b></td><td>369.16 (-1.51%)</td><td>419.00 <b>(+42.71%)</b></td><td>267.20 (+8.57%)</td><td>89.81 <b>(-40.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.00 (n/a)</td><td>374.82 (n/a)</td><td>293.60 (n/a)</td><td>246.10 (n/a)</td><td>150.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-3.78%)</td><td>0.01 (-9.07%)</td><td>0.01 (-4.76%)</td><td>0.00 <b>(-42.11%)</b></td><td>0.01 (+8.78%)</td><td>954.00 <b>(+72.73%)</b></td><td>495.88 <b>(+22.17%)</b></td><td>463.40 (+4.98%)</td><td>254.90 (+3.91%)</td><td>285.54 <b>(+87.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.30 (n/a)</td><td>405.88 (n/a)</td><td>441.40 (n/a)</td><td>245.30 (n/a)</td><td>152.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-22.32%)</b></td><td>0.01 <b>(-24.24%)</b></td><td>0.01 (-17.49%)</td><td>0.00 <b>(-59.44%)</b></td><td>0.00 (+11.86%)</td><td>1032.50 <b>(+146.54%)</b></td><td>488.02 <b>(+53.92%)</b></td><td>324.70 <b>(+21.20%)</b></td><td>291.80 <b>(+28.72%)</b></td><td>312.18 <b>(+246.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>418.80 (n/a)</td><td>317.06 (n/a)</td><td>267.90 (n/a)</td><td>226.70 (n/a)</td><td>90.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-39.19%)</b></td><td>0.01 (-19.54%)</td><td>0.01 (-5.10%)</td><td>0.01 (-6.73%)</td><td>0.00 <b>(-65.50%)</b></td><td>614.30 (+7.21%)</td><td>473.08 (+11.78%)</td><td>474.40 (+5.38%)</td><td>364.50 <b>(+64.49%)</b></td><td>92.38 <b>(-41.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.00 (n/a)</td><td>423.22 (n/a)</td><td>450.20 (n/a)</td><td>221.60 (n/a)</td><td>156.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (-11.61%)</td><td>0.01 (-19.82%)</td><td>0.01 <b>(-28.45%)</b></td><td>0.00 <b>(-66.37%)</b></td><td>0.00 <b>(+23.25%)</b></td><td>1884.50 <b>(+197.33%)</b></td><td>703.30 <b>(+73.51%)</b></td><td>481.50 <b>(+39.77%)</b></td><td>288.70 (+13.13%)</td><td>667.55 <b>(+342.10%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.80 (n/a)</td><td>405.34 (n/a)</td><td>344.50 (n/a)</td><td>255.20 (n/a)</td><td>151.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 <b>(+59.30%)</b></td><td>0.03 (-5.36%)</td><td>0.03 (-15.63%)</td><td>0.02 <b>(-31.73%)</b></td><td>0.01 <b>(+282.99%)</b></td><td>533.70 <b>(+46.50%)</b></td><td>357.10 <b>(+24.13%)</b></td><td>321.00 (+18.54%)</td><td>164.00 <b>(-37.21%)</b></td><td>151.46 <b>(+251.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>364.30 (n/a)</td><td>287.68 (n/a)</td><td>270.80 (n/a)</td><td>261.20 (n/a)</td><td>43.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (+11.95%)</td><td>0.03 (+10.00%)</td><td>0.03 (+6.59%)</td><td>0.02 <b>(+21.03%)</b></td><td>0.01 (+1.95%)</td><td>513.70 (-17.39%)</td><td>357.60 (-11.47%)</td><td>268.30 (-6.19%)</td><td>231.30 (-10.66%)</td><td>142.29 <b>(-20.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.80 (n/a)</td><td>403.94 (n/a)</td><td>286.00 (n/a)</td><td>258.90 (n/a)</td><td>179.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-4.29%)</td><td>0.02 (-13.07%)</td><td>0.02 <b>(-37.93%)</b></td><td>0.01 (-17.85%)</td><td>0.01 <b>(+25.40%)</b></td><td>556.00 <b>(+21.74%)</b></td><td>417.16 <b>(+21.42%)</b></td><td>471.30 <b>(+61.13%)</b></td><td>254.70 (+4.47%)</td><td>149.83 <b>(+46.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.70 (n/a)</td><td>343.58 (n/a)</td><td>292.50 (n/a)</td><td>243.80 (n/a)</td><td>102.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-0.87%)</td><td>0.03 (-12.30%)</td><td>0.03 (-9.29%)</td><td>0.02 <b>(-23.83%)</b></td><td>0.01 <b>(+26.25%)</b></td><td>527.20 <b>(+31.31%)</b></td><td>332.60 (+19.07%)</td><td>265.50 (+10.26%)</td><td>238.50 (+0.85%)</td><td>119.34 <b>(+68.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>401.50 (n/a)</td><td>279.32 (n/a)</td><td>240.80 (n/a)</td><td>236.50 (n/a)</td><td>70.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (-1.11%)</td><td>0.02 (-7.06%)</td><td>0.03 (-3.49%)</td><td>0.01 (-7.73%)</td><td>0.01 (-8.01%)</td><td>577.60 (+8.39%)</td><td>368.34 (+6.98%)</td><td>296.30 (+3.60%)</td><td>227.50 (+1.11%)</td><td>142.01 (+4.57%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>344.32 (n/a)</td><td>286.00 (n/a)</td><td>225.00 (n/a)</td><td>135.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-7.23%)</td><td>0.02 <b>(-26.09%)</b></td><td>0.02 <b>(-34.79%)</b></td><td>0.01 (-11.04%)</td><td>0.01 (-9.20%)</td><td>596.40 (+12.40%)</td><td>439.16 <b>(+35.18%)</b></td><td>423.80 <b>(+53.38%)</b></td><td>259.90 (+7.80%)</td><td>133.35 (+10.19%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.60 (n/a)</td><td>324.86 (n/a)</td><td>276.30 (n/a)</td><td>241.10 (n/a)</td><td>121.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (+12.25%)</td><td>0.02 (+2.08%)</td><td>0.02 <b>(-20.78%)</b></td><td>0.01 (-1.03%)</td><td>0.01 <b>(+47.30%)</b></td><td>564.50 (+1.04%)</td><td>434.26 (+3.85%)</td><td>514.40 <b>(+26.23%)</b></td><td>244.80 (-10.92%)</td><td>149.14 <b>(+37.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.70 (n/a)</td><td>418.18 (n/a)</td><td>407.50 (n/a)</td><td>274.80 (n/a)</td><td>108.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-16.51%)</td><td>0.02 (+4.28%)</td><td>0.03 <b>(+40.16%)</b></td><td>0.01 (+0.73%)</td><td>0.01 <b>(-26.88%)</b></td><td>582.80 (-0.73%)</td><td>370.40 (-6.98%)</td><td>305.60 <b>(-28.65%)</b></td><td>299.60 (+19.74%)</td><td>121.77 (-9.92%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.10 (n/a)</td><td>398.20 (n/a)</td><td>428.30 (n/a)</td><td>250.20 (n/a)</td><td>135.17 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+40.90%)</b></td><td>0.02 (+4.63%)</td><td>0.02 (-5.80%)</td><td>0.00 <b>(-70.51%)</b></td><td>0.01 <b>(+162.02%)</b></td><td>1935.60 <b>(+239.04%)</b></td><td>702.18 <b>(+53.27%)</b></td><td>491.30 (+6.16%)</td><td>234.00 <b>(-29.03%)</b></td><td>701.35 <b>(+568.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.90 (n/a)</td><td>458.12 (n/a)</td><td>462.80 (n/a)</td><td>329.70 (n/a)</td><td>104.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-17.79%)</td><td>0.02 (-4.77%)</td><td>0.02 (-18.54%)</td><td>0.02 <b>(+115.76%)</b></td><td>0.00 <b>(-61.58%)</b></td><td>488.10 <b>(-53.65%)</b></td><td>378.50 (-19.23%)</td><td>375.00 <b>(+22.75%)</b></td><td>302.40 <b>(+21.64%)</b></td><td>74.57 <b>(-78.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1053.10 (n/a)</td><td>468.60 (n/a)</td><td>305.50 (n/a)</td><td>248.60 (n/a)</td><td>340.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (+5.01%)</td><td>0.02 (+5.35%)</td><td>0.02 (+10.94%)</td><td>0.02 <b>(+94.34%)</b></td><td>0.01 <b>(-34.96%)</b></td><td>529.90 <b>(-48.54%)</b></td><td>460.38 (-18.42%)</td><td>519.30 (-9.86%)</td><td>290.40 (-4.76%)</td><td>102.25 <b>(-65.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1029.80 (n/a)</td><td>564.32 (n/a)</td><td>576.10 (n/a)</td><td>304.90 (n/a)</td><td>295.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-8.29%)</td><td>0.02 (-8.40%)</td><td>0.02 <b>(-26.90%)</b></td><td>0.01 <b>(+90.38%)</b></td><td>0.01 <b>(-38.13%)</b></td><td>556.40 <b>(-47.47%)</b></td><td>420.60 (-11.48%)</td><td>448.90 <b>(+36.82%)</b></td><td>269.90 (+9.05%)</td><td>118.17 <b>(-65.16%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1059.30 (n/a)</td><td>475.16 (n/a)</td><td>328.10 (n/a)</td><td>247.50 (n/a)</td><td>339.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (-1.82%)</td><td>0.05 (-15.53%)</td><td>0.05 <b>(-25.33%)</b></td><td>0.03 (-12.82%)</td><td>0.02 <b>(+20.48%)</b></td><td>507.40 (+14.69%)</td><td>349.22 <b>(+25.12%)</b></td><td>324.50 <b>(+33.92%)</b></td><td>189.60 (+1.83%)</td><td>139.39 <b>(+41.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>442.40 (n/a)</td><td>279.10 (n/a)</td><td>242.30 (n/a)</td><td>186.20 (n/a)</td><td>98.81 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+5.69%)</td><td>0.06 (+19.34%)</td><td>0.06 <b>(+28.54%)</b></td><td>0.04 <b>(+58.57%)</b></td><td>0.01 <b>(-35.61%)</b></td><td>391.60 <b>(-36.94%)</b></td><td>295.16 <b>(-24.58%)</b></td><td>271.80 <b>(-22.21%)</b></td><td>223.20 (-5.38%)</td><td>68.11 <b>(-59.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.00 (n/a)</td><td>391.36 (n/a)</td><td>349.40 (n/a)</td><td>235.90 (n/a)</td><td>168.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+2.16%)</td><td>0.04 <b>(-26.83%)</b></td><td>0.03 <b>(-41.64%)</b></td><td>0.02 <b>(-59.75%)</b></td><td>0.02 <b>(+60.75%)</b></td><td>1045.40 <b>(+148.43%)</b></td><td>523.44 <b>(+64.97%)</b></td><td>483.60 <b>(+71.37%)</b></td><td>244.60 (-2.12%)</td><td>310.67 <b>(+306.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>420.80 (n/a)</td><td>317.30 (n/a)</td><td>282.20 (n/a)</td><td>249.90 (n/a)</td><td>76.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+8.96%)</td><td>0.04 (-14.52%)</td><td>0.03 <b>(-41.00%)</b></td><td>0.03 (+14.92%)</td><td>0.02 (+3.63%)</td><td>546.20 (-12.98%)</td><td>442.94 (+14.18%)</td><td>491.80 <b>(+69.53%)</b></td><td>223.20 (-8.19%)</td><td>126.62 <b>(-23.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.70 (n/a)</td><td>387.94 (n/a)</td><td>290.10 (n/a)</td><td>243.10 (n/a)</td><td>165.33 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+7.99%)</td><td>0.05 (-10.98%)</td><td>0.03 <b>(-36.98%)</b></td><td>0.03 (-9.64%)</td><td>0.02 (+19.00%)</td><td>525.00 (+10.67%)</td><td>397.66 (+16.70%)</td><td>473.30 <b>(+58.67%)</b></td><td>218.90 (-7.40%)</td><td>140.84 <b>(+23.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>474.40 (n/a)</td><td>340.76 (n/a)</td><td>298.30 (n/a)</td><td>236.40 (n/a)</td><td>114.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 <b>(+30.97%)</b></td><td>0.05 (-13.59%)</td><td>0.05 <b>(-22.85%)</b></td><td>0.02 <b>(-45.47%)</b></td><td>0.03 <b>(+108.94%)</b></td><td>812.50 <b>(+83.41%)</b></td><td>413.08 <b>(+39.01%)</b></td><td>347.80 <b>(+29.63%)</b></td><td>186.50 <b>(-23.63%)</b></td><td>239.71 <b>(+191.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>443.00 (n/a)</td><td>297.16 (n/a)</td><td>268.30 (n/a)</td><td>244.20 (n/a)</td><td>82.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (-0.60%)</td><td>0.05 (+12.23%)</td><td>0.04 (+7.03%)</td><td>0.03 (-13.39%)</td><td>0.02 <b>(+27.39%)</b></td><td>611.00 (+15.48%)</td><td>402.22 (-5.64%)</td><td>444.00 (-6.57%)</td><td>242.40 (+0.58%)</td><td>158.73 <b>(+40.39%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.10 (n/a)</td><td>426.26 (n/a)</td><td>475.20 (n/a)</td><td>241.00 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-16.60%)</td><td>0.04 (-13.24%)</td><td>0.04 (-11.19%)</td><td>0.01 <b>(-72.39%)</b></td><td>0.02 (+11.49%)</td><td>2074.80 <b>(+262.28%)</b></td><td>705.72 <b>(+71.81%)</b></td><td>430.60 (+12.60%)</td><td>280.20 (+19.90%)</td><td>768.71 <b>(+396.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.70 (n/a)</td><td>410.76 (n/a)</td><td>382.40 (n/a)</td><td>233.70 (n/a)</td><td>154.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-17.26%)</td><td>0.04 <b>(-31.75%)</b></td><td>0.03 <b>(-41.54%)</b></td><td>0.03 (+1.15%)</td><td>0.01 <b>(-29.62%)</b></td><td>623.40 (-1.14%)</td><td>490.08 <b>(+38.36%)</b></td><td>517.40 <b>(+71.04%)</b></td><td>274.70 <b>(+20.85%)</b></td><td>128.98 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.60 (n/a)</td><td>354.20 (n/a)</td><td>302.50 (n/a)</td><td>227.30 (n/a)</td><td>165.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-13.45%)</td><td>0.04 (-3.07%)</td><td>0.04 (+7.33%)</td><td>0.03 (-13.09%)</td><td>0.01 (-14.44%)</td><td>539.80 (+15.05%)</td><td>389.22 (+2.60%)</td><td>394.60 (-6.82%)</td><td>290.00 (+15.54%)</td><td>104.09 (+6.98%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>469.20 (n/a)</td><td>379.36 (n/a)</td><td>423.50 (n/a)</td><td>251.00 (n/a)</td><td>97.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 <b>(+27.11%)</b></td><td>0.04 (-2.51%)</td><td>0.03 <b>(-20.72%)</b></td><td>0.02 <b>(-31.45%)</b></td><td>0.02 <b>(+129.88%)</b></td><td>760.10 <b>(+45.89%)</b></td><td>491.82 (+13.79%)</td><td>525.50 <b>(+26.14%)</b></td><td>268.60 <b>(-21.32%)</b></td><td>189.04 <b>(+153.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>521.00 (n/a)</td><td>432.22 (n/a)</td><td>416.60 (n/a)</td><td>341.40 (n/a)</td><td>74.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+1.59%)</td><td>0.04 (-13.49%)</td><td>0.03 <b>(-48.00%)</b></td><td>0.03 (-17.45%)</td><td>0.02 <b>(+29.09%)</b></td><td>654.30 <b>(+21.14%)</b></td><td>449.48 <b>(+25.45%)</b></td><td>538.40 <b>(+92.29%)</b></td><td>237.90 (-1.57%)</td><td>194.76 <b>(+43.01%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.10 (n/a)</td><td>358.30 (n/a)</td><td>280.00 (n/a)</td><td>241.70 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (+5.56%)</td><td>0.09 (-8.38%)</td><td>0.08 <b>(-25.66%)</b></td><td>0.04 <b>(-30.83%)</b></td><td>0.04 <b>(+34.32%)</b></td><td>761.10 <b>(+44.59%)</b></td><td>444.00 <b>(+20.93%)</b></td><td>404.40 <b>(+34.53%)</b></td><td>230.10 (-5.23%)</td><td>219.22 <b>(+72.36%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>526.40 (n/a)</td><td>367.14 (n/a)</td><td>300.60 (n/a)</td><td>242.80 (n/a)</td><td>127.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (-2.32%)</td><td>0.11 (-9.90%)</td><td>0.12 (-4.96%)</td><td>0.05 <b>(-48.04%)</b></td><td>0.03 <b>(+84.95%)</b></td><td>695.60 <b>(+92.47%)</b></td><td>355.02 <b>(+25.80%)</b></td><td>267.50 (+5.23%)</td><td>251.60 (+2.36%)</td><td>191.25 <b>(+284.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>361.40 (n/a)</td><td>282.20 (n/a)</td><td>254.20 (n/a)</td><td>245.80 (n/a)</td><td>49.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (+0.52%)</td><td>0.09 (-5.62%)</td><td>0.07 <b>(-23.75%)</b></td><td>0.05 (+0.89%)</td><td>0.03 (+17.30%)</td><td>602.90 (-0.89%)</td><td>414.78 (+8.60%)</td><td>467.70 <b>(+31.16%)</b></td><td>245.70 (-0.53%)</td><td>148.25 (+7.63%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.30 (n/a)</td><td>381.94 (n/a)</td><td>356.60 (n/a)</td><td>247.00 (n/a)</td><td>137.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (-17.54%)</td><td>0.09 <b>(-20.00%)</b></td><td>0.08 <b>(-37.43%)</b></td><td>0.06 (+1.01%)</td><td>0.03 <b>(-27.90%)</b></td><td>538.40 (-0.99%)</td><td>385.64 (+18.88%)</td><td>395.90 <b>(+59.83%)</b></td><td>238.00 <b>(+21.30%)</b></td><td>118.69 (-16.40%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>543.80 (n/a)</td><td>324.40 (n/a)</td><td>247.70 (n/a)</td><td>196.20 (n/a)</td><td>141.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (-15.69%)</td><td>0.09 (+13.48%)</td><td>0.07 <b>(+20.03%)</b></td><td>0.05 (-6.87%)</td><td>0.03 (-19.16%)</td><td>636.20 (+7.38%)</td><td>416.72 (-13.98%)</td><td>444.60 (-16.69%)</td><td>272.00 (+18.62%)</td><td>149.56 (+0.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.50 (n/a)</td><td>484.42 (n/a)</td><td>533.70 (n/a)</td><td>229.30 (n/a)</td><td>148.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 <b>(-23.49%)</b></td><td>0.09 (-15.11%)</td><td>0.08 (+5.98%)</td><td>0.07 (+7.34%)</td><td>0.03 <b>(-41.92%)</b></td><td>484.40 (-6.85%)</td><td>393.70 (+5.07%)</td><td>430.10 (-5.64%)</td><td>222.20 <b>(+30.71%)</b></td><td>106.27 <b>(-33.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>520.00 (n/a)</td><td>374.70 (n/a)</td><td>455.80 (n/a)</td><td>170.00 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (+4.07%)</td><td>0.09 (-9.29%)</td><td>0.07 (-1.66%)</td><td>0.06 (+1.93%)</td><td>0.03 (-11.16%)</td><td>511.40 (-1.88%)</td><td>413.22 (+7.29%)</td><td>470.50 (+1.69%)</td><td>226.50 (-3.90%)</td><td>117.27 (-13.43%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>521.20 (n/a)</td><td>385.14 (n/a)</td><td>462.70 (n/a)</td><td>235.70 (n/a)</td><td>135.47 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 <b>(+30.63%)</b></td><td>0.11 (+12.44%)</td><td>0.11 (-10.90%)</td><td>0.07 <b>(+21.64%)</b></td><td>0.04 (+17.64%)</td><td>442.00 (-17.78%)</td><td>322.30 (-11.84%)</td><td>300.50 (+12.25%)</td><td>198.60 <b>(-23.44%)</b></td><td>111.36 <b>(-20.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.60 (n/a)</td><td>365.60 (n/a)</td><td>267.70 (n/a)</td><td>259.40 (n/a)</td><td>140.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 <b>(-21.85%)</b></td><td>0.08 <b>(-21.13%)</b></td><td>0.07 <b>(-44.18%)</b></td><td>0.06 (-3.39%)</td><td>0.03 <b>(-34.45%)</b></td><td>572.60 (+3.51%)</td><td>421.64 (+18.09%)</td><td>447.20 <b>(+79.17%)</b></td><td>283.50 <b>(+27.93%)</b></td><td>130.91 (-19.76%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>553.20 (n/a)</td><td>357.06 (n/a)</td><td>249.60 (n/a)</td><td>221.60 (n/a)</td><td>163.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (-14.62%)</td><td>0.08 <b>(-35.92%)</b></td><td>0.06 <b>(-50.49%)</b></td><td>0.05 <b>(-47.13%)</b></td><td>0.03 <b>(+87.86%)</b></td><td>651.60 <b>(+89.14%)</b></td><td>475.78 <b>(+73.78%)</b></td><td>520.60 <b>(+102.02%)</b></td><td>283.90 (+17.12%)</td><td>174.27 <b>(+308.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>344.50 (n/a)</td><td>273.78 (n/a)</td><td>257.70 (n/a)</td><td>242.40 (n/a)</td><td>42.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (-8.29%)</td><td>0.08 (-9.32%)</td><td>0.07 <b>(-22.99%)</b></td><td>0.05 (-19.07%)</td><td>0.02 (+16.03%)</td><td>616.40 <b>(+23.58%)</b></td><td>455.84 (+12.82%)</td><td>494.70 <b>(+29.84%)</b></td><td>332.10 (+9.06%)</td><td>122.28 <b>(+41.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>498.80 (n/a)</td><td>404.04 (n/a)</td><td>381.00 (n/a)</td><td>304.50 (n/a)</td><td>86.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 <b>(-20.33%)</b></td><td>0.08 <b>(-28.58%)</b></td><td>0.07 <b>(-35.16%)</b></td><td>0.06 (-13.32%)</td><td>0.02 (-18.96%)</td><td>576.20 (+15.36%)</td><td>454.98 <b>(+38.83%)</b></td><td>474.10 <b>(+54.23%)</b></td><td>272.80 <b>(+25.54%)</b></td><td>110.88 (+5.82%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.50 (n/a)</td><td>327.72 (n/a)</td><td>307.40 (n/a)</td><td>217.30 (n/a)</td><td>104.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (-8.02%)</td><td>0.05 <b>(-23.56%)</b></td><td>0.05 <b>(-37.41%)</b></td><td>0.01 (-8.61%)</td><td>0.03 <b>(-21.13%)</b></td><td>2094.50 (+9.42%)</td><td>780.10 (+19.26%)</td><td>476.20 <b>(+59.80%)</b></td><td>303.50 (+8.74%)</td><td>742.16 (+4.62%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1914.20 (n/a)</td><td>654.14 (n/a)</td><td>298.00 (n/a)</td><td>279.10 (n/a)</td><td>709.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.20 (+18.82%)</td><td>0.15 (+13.22%)</td><td>0.17 <b>(+40.73%)</b></td><td>0.10 (+1.37%)</td><td>0.04 <b>(+42.38%)</b></td><td>500.70 (-1.34%)</td><td>357.96 (-8.38%)</td><td>296.40 <b>(-28.94%)</b></td><td>249.90 (-15.83%)</td><td>117.74 <b>(+28.70%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>507.50 (n/a)</td><td>390.72 (n/a)</td><td>417.10 (n/a)</td><td>296.90 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.15 <b>(+28.26%)</b></td><td>3.44 <b>(+21.40%)</b></td><td>3.61 <b>(+36.75%)</b></td><td>2.64 (+2.65%)</td><td>0.75 <b>(+130.89%)</b></td><td>3978.00 (-2.58%)</td><td>3180.70 (-15.04%)</td><td>2906.60 <b>(-26.88%)</b></td><td>2528.30 <b>(-22.03%)</b></td><td>732.73 <b>(+76.75%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.23 (n/a)</td><td>2.83 (n/a)</td><td>2.64 (n/a)</td><td>2.57 (n/a)</td><td>0.33 (n/a)</td><td>4083.50 (n/a)</td><td>3743.96 (n/a)</td><td>3974.90 (n/a)</td><td>3242.80 (n/a)</td><td>414.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 (+17.53%)</td><td>0.14 <b>(+49.99%)</b></td><td>0.16 <b>(+82.34%)</b></td><td>0.06 <b>(+115.98%)</b></td><td>0.04 (-2.77%)</td><td>633.60 <b>(-53.70%)</b></td><td>336.30 <b>(-43.44%)</b></td><td>262.10 <b>(-45.16%)</b></td><td>250.60 (-14.91%)</td><td>166.43 <b>(-62.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1368.50 (n/a)</td><td>594.56 (n/a)</td><td>477.90 (n/a)</td><td>294.50 (n/a)</td><td>441.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-17.88%)</td><td>0.02 (-8.06%)</td><td>0.02 (-2.70%)</td><td>0.01 <b>(-28.31%)</b></td><td>0.00 (+0.65%)</td><td>536.70 <b>(+39.48%)</b></td><td>318.68 (+13.01%)</td><td>277.80 (+2.77%)</td><td>239.20 <b>(+21.79%)</b></td><td>123.08 <b>(+81.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>384.80 (n/a)</td><td>282.00 (n/a)</td><td>270.30 (n/a)</td><td>196.40 (n/a)</td><td>67.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+4.70%)</td><td>0.01 <b>(+27.13%)</b></td><td>0.01 <b>(+46.74%)</b></td><td>0.01 <b>(+20.09%)</b></td><td>0.00 (+13.54%)</td><td>472.80 (-16.72%)</td><td>348.70 <b>(-20.84%)</b></td><td>314.60 <b>(-31.85%)</b></td><td>254.50 (-4.50%)</td><td>104.42 (-4.31%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.70 (n/a)</td><td>440.48 (n/a)</td><td>461.60 (n/a)</td><td>266.50 (n/a)</td><td>109.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-16.26%)</td><td>0.02 (+2.11%)</td><td>0.02 (+16.66%)</td><td>0.01 (+14.68%)</td><td>0.01 <b>(-21.69%)</b></td><td>569.60 (-12.80%)</td><td>402.96 (-5.59%)</td><td>374.70 (-14.28%)</td><td>268.50 (+19.39%)</td><td>132.89 (-15.95%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.20 (n/a)</td><td>426.84 (n/a)</td><td>437.10 (n/a)</td><td>224.90 (n/a)</td><td>158.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-15.78%)</td><td>0.01 (+3.09%)</td><td>0.01 (+6.22%)</td><td>0.01 <b>(+20.23%)</b></td><td>0.00 <b>(-38.08%)</b></td><td>427.30 (-16.84%)</td><td>331.38 (-10.26%)</td><td>330.30 (-5.84%)</td><td>221.90 (+18.73%)</td><td>79.86 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>513.80 (n/a)</td><td>369.28 (n/a)</td><td>350.80 (n/a)</td><td>186.90 (n/a)</td><td>132.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-39.83%)</b></td><td>0.01 (-8.12%)</td><td>0.01 (+4.10%)</td><td>0.01 <b>(+86.90%)</b></td><td>0.00 <b>(-69.30%)</b></td><td>576.50 <b>(-46.49%)</b></td><td>475.10 (-13.68%)</td><td>501.00 (-3.93%)</td><td>380.20 <b>(+66.17%)</b></td><td>85.43 <b>(-73.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1077.40 (n/a)</td><td>550.42 (n/a)</td><td>521.50 (n/a)</td><td>228.80 (n/a)</td><td>323.47 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(+34.15%)</b></td><td>0.01 <b>(+28.64%)</b></td><td>0.01 <b>(+63.04%)</b></td><td>0.00 <b>(-75.52%)</b></td><td>0.01 <b>(+172.16%)</b></td><td>1992.10 <b>(+308.38%)</b></td><td>600.10 <b>(+48.53%)</b></td><td>274.50 <b>(-38.66%)</b></td><td>217.50 <b>(-25.46%)</b></td><td>778.67 <b>(+808.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.80 (n/a)</td><td>404.02 (n/a)</td><td>447.50 (n/a)</td><td>291.80 (n/a)</td><td>85.66 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-3.77%)</td><td>0.01 (-0.46%)</td><td>0.01 (-0.72%)</td><td>0.01 (+2.23%)</td><td>0.00 (-7.59%)</td><td>590.70 (-2.19%)</td><td>449.08 (-0.38%)</td><td>467.10 (+0.73%)</td><td>268.40 (+3.91%)</td><td>118.98 (-4.28%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.90 (n/a)</td><td>450.80 (n/a)</td><td>463.70 (n/a)</td><td>258.30 (n/a)</td><td>124.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(+22.82%)</b></td><td>0.01 (-9.19%)</td><td>0.01 (-13.63%)</td><td>0.00 <b>(-49.36%)</b></td><td>0.00 <b>(+139.37%)</b></td><td>1034.90 <b>(+97.50%)</b></td><td>575.54 <b>(+29.77%)</b></td><td>539.40 (+15.78%)</td><td>273.60 (-18.60%)</td><td>286.19 <b>(+293.46%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.00 (n/a)</td><td>443.52 (n/a)</td><td>465.90 (n/a)</td><td>336.10 (n/a)</td><td>72.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-2.69%)</td><td>0.01 (-6.28%)</td><td>0.01 <b>(-21.24%)</b></td><td>0.01 (+1.68%)</td><td>0.00 (-4.88%)</td><td>592.00 (-1.64%)</td><td>448.28 (+5.41%)</td><td>459.40 <b>(+26.94%)</b></td><td>255.20 (+2.78%)</td><td>142.38 (-7.45%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.90 (n/a)</td><td>425.28 (n/a)</td><td>361.90 (n/a)</td><td>248.30 (n/a)</td><td>153.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (-12.10%)</td><td>0.01 (+1.63%)</td><td>0.01 <b>(+23.60%)</b></td><td>0.01 <b>(+31.96%)</b></td><td>0.00 <b>(-38.64%)</b></td><td>473.20 <b>(-24.23%)</b></td><td>379.80 (-9.51%)</td><td>379.90 (-19.10%)</td><td>263.10 (+13.75%)</td><td>88.42 <b>(-44.46%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.50 (n/a)</td><td>419.72 (n/a)</td><td>469.60 (n/a)</td><td>231.30 (n/a)</td><td>159.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-39.81%)</b></td><td>0.01 (-0.75%)</td><td>0.01 (+18.12%)</td><td>0.01 <b>(+24.07%)</b></td><td>0.00 <b>(-65.94%)</b></td><td>545.10 (-19.40%)</td><td>443.36 (-13.16%)</td><td>469.00 (-15.33%)</td><td>342.70 <b>(+66.20%)</b></td><td>87.67 <b>(-51.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.30 (n/a)</td><td>510.52 (n/a)</td><td>553.90 (n/a)</td><td>206.20 (n/a)</td><td>181.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (+19.44%)</td><td>0.01 (+14.82%)</td><td>0.01 (+14.00%)</td><td>0.01 (-8.07%)</td><td>0.00 <b>(+50.65%)</b></td><td>619.00 (+8.79%)</td><td>407.14 (-10.11%)</td><td>389.90 (-12.28%)</td><td>309.10 (-16.28%)</td><td>124.44 <b>(+43.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.00 (n/a)</td><td>452.94 (n/a)</td><td>444.50 (n/a)</td><td>369.20 (n/a)</td><td>86.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+20.88%)</b></td><td>0.03 <b>(+45.34%)</b></td><td>0.03 <b>(+76.65%)</b></td><td>0.02 <b>(+26.37%)</b></td><td>0.01 (+2.23%)</td><td>430.60 <b>(-20.86%)</b></td><td>293.40 <b>(-32.63%)</b></td><td>276.60 <b>(-43.40%)</b></td><td>217.40 (-17.28%)</td><td>81.82 <b>(-30.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.10 (n/a)</td><td>435.50 (n/a)</td><td>488.70 (n/a)</td><td>262.80 (n/a)</td><td>117.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (-1.44%)</td><td>0.04 (+12.25%)</td><td>0.04 <b>(+36.26%)</b></td><td>0.02 (+10.96%)</td><td>0.01 (-0.85%)</td><td>506.50 (-9.88%)</td><td>342.64 (-11.59%)</td><td>274.30 <b>(-26.60%)</b></td><td>261.40 (+1.48%)</td><td>107.54 (-11.09%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.00 (n/a)</td><td>387.54 (n/a)</td><td>373.70 (n/a)</td><td>257.60 (n/a)</td><td>120.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 <b>(-56.60%)</b></td><td>0.01 <b>(-37.58%)</b></td><td>0.02 (-11.75%)</td><td>0.00 <b>(-60.10%)</b></td><td>0.01 <b>(-51.29%)</b></td><td>2124.00 <b>(+150.59%)</b></td><td>841.60 <b>(+77.46%)</b></td><td>527.60 (+13.32%)</td><td>505.10 <b>(+130.43%)</b></td><td>716.96 <b>(+194.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>847.60 (n/a)</td><td>474.26 (n/a)</td><td>465.60 (n/a)</td><td>219.20 (n/a)</td><td>243.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+21.29%)</b></td><td>0.03 (-5.57%)</td><td>0.02 (-1.89%)</td><td>0.02 (-11.25%)</td><td>0.01 <b>(+49.63%)</b></td><td>508.10 (+12.69%)</td><td>410.26 (+9.81%)</td><td>424.70 (+1.92%)</td><td>234.70 (-17.53%)</td><td>105.15 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.90 (n/a)</td><td>373.60 (n/a)</td><td>416.70 (n/a)</td><td>284.60 (n/a)</td><td>78.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (-3.02%)</td><td>0.02 (-13.18%)</td><td>0.02 (+7.15%)</td><td>0.01 (-0.60%)</td><td>0.01 <b>(-27.82%)</b></td><td>614.10 (+0.61%)</td><td>457.00 (+5.06%)</td><td>472.70 (-6.67%)</td><td>236.80 (+3.14%)</td><td>137.18 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.40 (n/a)</td><td>434.98 (n/a)</td><td>506.50 (n/a)</td><td>229.60 (n/a)</td><td>191.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (-9.08%)</td><td>0.03 (+18.78%)</td><td>0.02 <b>(+28.77%)</b></td><td>0.02 <b>(+27.60%)</b></td><td>0.01 <b>(-35.21%)</b></td><td>481.30 <b>(-21.63%)</b></td><td>381.78 <b>(-22.18%)</b></td><td>417.10 <b>(-22.34%)</b></td><td>255.50 (+9.99%)</td><td>87.97 <b>(-43.01%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>614.10 (n/a)</td><td>490.58 (n/a)</td><td>537.10 (n/a)</td><td>232.30 (n/a)</td><td>154.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(-44.75%)</b></td><td>0.02 <b>(-33.63%)</b></td><td>0.02 (-14.09%)</td><td>0.01 <b>(-21.46%)</b></td><td>0.01 <b>(-58.02%)</b></td><td>674.40 <b>(+27.32%)</b></td><td>493.10 <b>(+32.40%)</b></td><td>523.90 (+16.40%)</td><td>283.90 <b>(+80.94%)</b></td><td>152.30 (-7.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>529.70 (n/a)</td><td>372.42 (n/a)</td><td>450.10 (n/a)</td><td>156.90 (n/a)</td><td>164.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(-24.95%)</b></td><td>0.02 (-4.84%)</td><td>0.02 (+4.05%)</td><td>0.02 (-0.77%)</td><td>0.01 <b>(-40.71%)</b></td><td>576.20 (+0.79%)</td><td>405.84 (-1.08%)</td><td>424.30 (-3.90%)</td><td>262.40 <b>(+33.27%)</b></td><td>116.88 (-13.93%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>571.70 (n/a)</td><td>410.28 (n/a)</td><td>441.50 (n/a)</td><td>196.90 (n/a)</td><td>135.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 <b>(-23.37%)</b></td><td>0.02 (+2.48%)</td><td>0.02 <b>(-20.41%)</b></td><td>0.02 <b>(+250.10%)</b></td><td>0.01 <b>(-65.32%)</b></td><td>537.00 <b>(-71.44%)</b></td><td>384.58 <b>(-57.18%)</b></td><td>358.70 <b>(+25.64%)</b></td><td>276.60 <b>(+30.47%)</b></td><td>103.98 <b>(-88.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1880.20 (n/a)</td><td>898.08 (n/a)</td><td>285.50 (n/a)</td><td>212.00 (n/a)</td><td>892.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (+5.81%)</td><td>0.02 (+11.95%)</td><td>0.02 <b>(+27.83%)</b></td><td>0.01 <b>(-20.83%)</b></td><td>0.01 (+13.57%)</td><td>799.10 <b>(+26.30%)</b></td><td>448.06 (-5.38%)</td><td>413.30 <b>(-21.77%)</b></td><td>230.20 (-5.46%)</td><td>216.22 <b>(+46.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.70 (n/a)</td><td>473.56 (n/a)</td><td>528.30 (n/a)</td><td>243.50 (n/a)</td><td>148.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 <b>(+33.05%)</b></td><td>0.02 <b>(+35.12%)</b></td><td>0.02 <b>(+45.83%)</b></td><td>0.02 <b>(+46.05%)</b></td><td>0.01 (+15.95%)</td><td>467.20 <b>(-31.53%)</b></td><td>363.24 <b>(-27.94%)</b></td><td>360.00 <b>(-31.43%)</b></td><td>232.60 <b>(-24.85%)</b></td><td>96.27 <b>(-39.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.30 (n/a)</td><td>504.08 (n/a)</td><td>525.00 (n/a)</td><td>309.50 (n/a)</td><td>159.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(-20.15%)</b></td><td>0.05 <b>(-22.30%)</b></td><td>0.05 <b>(-26.34%)</b></td><td>0.03 (-5.19%)</td><td>0.02 (-13.44%)</td><td>571.80 (+5.48%)</td><td>391.62 <b>(+28.42%)</b></td><td>337.00 <b>(+35.78%)</b></td><td>247.70 <b>(+25.23%)</b></td><td>153.10 (+10.69%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.10 (n/a)</td><td>304.96 (n/a)</td><td>248.20 (n/a)</td><td>197.80 (n/a)</td><td>138.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 <b>(+26.56%)</b></td><td>0.09 <b>(+31.42%)</b></td><td>0.09 <b>(+63.78%)</b></td><td>0.05 (+13.72%)</td><td>0.03 (+18.71%)</td><td>494.50 (-12.06%)</td><td>311.20 <b>(-23.92%)</b></td><td>282.70 <b>(-38.95%)</b></td><td>195.00 <b>(-20.99%)</b></td><td>112.16 (-13.09%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>562.30 (n/a)</td><td>409.04 (n/a)</td><td>463.10 (n/a)</td><td>246.80 (n/a)</td><td>129.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-10.50%)</td><td>0.04 (-18.29%)</td><td>0.04 <b>(-41.69%)</b></td><td>0.03 (-2.93%)</td><td>0.02 (-15.53%)</td><td>574.60 (+3.03%)</td><td>412.80 (+19.89%)</td><td>468.00 <b>(+71.49%)</b></td><td>261.00 (+11.73%)</td><td>135.29 (-4.19%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>557.70 (n/a)</td><td>344.32 (n/a)</td><td>272.90 (n/a)</td><td>233.60 (n/a)</td><td>141.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 <b>(+50.16%)</b></td><td>0.06 (+13.68%)</td><td>0.04 (-4.01%)</td><td>0.04 <b>(+31.98%)</b></td><td>0.03 <b>(+57.63%)</b></td><td>518.40 <b>(-24.23%)</b></td><td>420.80 (-9.53%)</td><td>480.60 (+4.16%)</td><td>181.00 <b>(-33.41%)</b></td><td>139.47 <b>(-22.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>684.20 (n/a)</td><td>465.12 (n/a)</td><td>461.40 (n/a)</td><td>271.80 (n/a)</td><td>179.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+13.53%)</td><td>0.04 (-15.05%)</td><td>0.03 <b>(-39.58%)</b></td><td>0.03 (-13.28%)</td><td>0.02 <b>(+58.61%)</b></td><td>634.40 (+15.32%)</td><td>494.58 <b>(+27.19%)</b></td><td>584.20 <b>(+65.50%)</b></td><td>240.30 (-11.91%)</td><td>166.31 <b>(+58.36%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>550.10 (n/a)</td><td>388.84 (n/a)</td><td>353.00 (n/a)</td><td>272.80 (n/a)</td><td>105.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (-4.51%)</td><td>0.06 (+6.66%)</td><td>0.06 <b>(+33.87%)</b></td><td>0.04 (+19.17%)</td><td>0.03 <b>(-21.22%)</b></td><td>577.30 (-16.08%)</td><td>383.72 (-16.74%)</td><td>371.10 <b>(-25.32%)</b></td><td>199.90 (+4.71%)</td><td>156.30 <b>(-33.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>687.90 (n/a)</td><td>460.86 (n/a)</td><td>496.90 (n/a)</td><td>190.90 (n/a)</td><td>233.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(-21.99%)</b></td><td>0.06 (+5.76%)</td><td>0.06 (-4.13%)</td><td>0.05 <b>(+41.24%)</b></td><td>0.01 <b>(-60.61%)</b></td><td>361.60 <b>(-29.20%)</b></td><td>273.10 (-18.66%)</td><td>262.50 (+4.29%)</td><td>225.00 <b>(+28.21%)</b></td><td>52.44 <b>(-66.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>510.70 (n/a)</td><td>335.76 (n/a)</td><td>251.70 (n/a)</td><td>175.50 (n/a)</td><td>156.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(-20.19%)</b></td><td>0.05 (-4.23%)</td><td>0.04 (+8.38%)</td><td>0.03 (-19.29%)</td><td>0.02 <b>(-29.24%)</b></td><td>628.60 <b>(+23.91%)</b></td><td>422.20 (+2.06%)</td><td>419.60 (-7.72%)</td><td>254.50 <b>(+25.31%)</b></td><td>139.81 (+15.75%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>507.30 (n/a)</td><td>413.68 (n/a)</td><td>454.70 (n/a)</td><td>203.10 (n/a)</td><td>120.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+6.02%)</td><td>0.05 <b>(+24.61%)</b></td><td>0.06 <b>(+41.21%)</b></td><td>0.03 <b>(+268.09%)</b></td><td>0.02 <b>(-24.19%)</b></td><td>523.70 <b>(-72.83%)</b></td><td>353.10 <b>(-47.50%)</b></td><td>293.10 <b>(-29.17%)</b></td><td>224.20 (-5.68%)</td><td>128.73 <b>(-81.83%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1927.50 (n/a)</td><td>672.52 (n/a)</td><td>413.80 (n/a)</td><td>237.70 (n/a)</td><td>708.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 <b>(+57.66%)</b></td><td>0.05 (+19.09%)</td><td>0.04 (+3.15%)</td><td>0.03 (+3.57%)</td><td>0.01 <b>(+185.55%)</b></td><td>574.90 (-3.44%)</td><td>428.14 (-11.73%)</td><td>436.10 (-3.07%)</td><td>275.70 <b>(-36.58%)</b></td><td>114.60 <b>(+71.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>595.40 (n/a)</td><td>485.06 (n/a)</td><td>449.90 (n/a)</td><td>434.70 (n/a)</td><td>66.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (+5.21%)</td><td>0.04 <b>(+28.30%)</b></td><td>0.04 <b>(+51.76%)</b></td><td>0.03 (-2.26%)</td><td>0.01 (+13.14%)</td><td>634.90 (+2.32%)</td><td>437.68 <b>(-21.25%)</b></td><td>395.60 <b>(-34.11%)</b></td><td>336.10 (-4.95%)</td><td>125.06 (+10.01%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>620.50 (n/a)</td><td>555.80 (n/a)</td><td>600.40 (n/a)</td><td>353.60 (n/a)</td><td>113.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (+5.14%)</td><td>0.11 <b>(+31.27%)</b></td><td>0.12 <b>(+25.21%)</b></td><td>0.10 <b>(+61.08%)</b></td><td>0.01 <b>(-45.50%)</b></td><td>342.40 <b>(-37.93%)</b></td><td>291.14 <b>(-28.26%)</b></td><td>284.40 <b>(-20.13%)</b></td><td>249.80 (-4.87%)</td><td>37.49 <b>(-68.91%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.60 (n/a)</td><td>405.82 (n/a)</td><td>356.10 (n/a)</td><td>262.60 (n/a)</td><td>120.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 <b>(+40.85%)</b></td><td>0.11 <b>(+26.90%)</b></td><td>0.11 <b>(+33.62%)</b></td><td>0.08 <b>(+27.77%)</b></td><td>0.04 <b>(+41.26%)</b></td><td>421.20 <b>(-21.74%)</b></td><td>322.42 <b>(-20.67%)</b></td><td>307.40 <b>(-25.17%)</b></td><td>177.70 <b>(-29.01%)</b></td><td>102.18 <b>(-22.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>538.20 (n/a)</td><td>406.44 (n/a)</td><td>410.80 (n/a)</td><td>250.30 (n/a)</td><td>131.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 <b>(+20.24%)</b></td><td>0.11 (+3.92%)</td><td>0.09 (+9.83%)</td><td>0.08 <b>(+36.32%)</b></td><td>0.04 (-4.07%)</td><td>492.50 <b>(-26.65%)</b></td><td>408.86 (-8.63%)</td><td>448.60 (-8.95%)</td><td>224.70 (-16.84%)</td><td>108.77 <b>(-37.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>671.40 (n/a)</td><td>447.46 (n/a)</td><td>492.70 (n/a)</td><td>270.20 (n/a)</td><td>174.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (+17.58%)</td><td>0.10 <b>(+46.94%)</b></td><td>0.10 <b>(+60.85%)</b></td><td>0.08 <b>(+153.99%)</b></td><td>0.02 <b>(-25.80%)</b></td><td>418.40 <b>(-60.62%)</b></td><td>340.86 <b>(-40.20%)</b></td><td>313.10 <b>(-37.84%)</b></td><td>256.20 (-14.94%)</td><td>69.89 <b>(-75.79%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1062.60 (n/a)</td><td>569.96 (n/a)</td><td>503.70 (n/a)</td><td>301.20 (n/a)</td><td>288.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 <b>(+87.91%)</b></td><td>0.11 <b>(+33.62%)</b></td><td>0.09 (+4.35%)</td><td>0.08 (+7.11%)</td><td>0.05 <b>(+315.02%)</b></td><td>538.40 (-6.63%)</td><td>395.08 (-18.11%)</td><td>440.10 (-4.18%)</td><td>218.10 <b>(-46.77%)</b></td><td>126.78 <b>(+99.71%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>576.60 (n/a)</td><td>482.48 (n/a)</td><td>459.30 (n/a)</td><td>409.70 (n/a)</td><td>63.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (-18.43%)</td><td>0.07 <b>(-20.66%)</b></td><td>0.06 (-17.12%)</td><td>0.05 <b>(-20.16%)</b></td><td>0.03 <b>(-21.13%)</b></td><td>673.20 <b>(+25.25%)</b></td><td>506.94 <b>(+24.22%)</b></td><td>528.00 <b>(+20.63%)</b></td><td>264.40 <b>(+22.58%)</b></td><td>149.56 (+9.86%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>537.50 (n/a)</td><td>408.10 (n/a)</td><td>437.70 (n/a)</td><td>215.70 (n/a)</td><td>136.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 <b>(+24.64%)</b></td><td>0.09 <b>(+21.87%)</b></td><td>0.07 (+14.64%)</td><td>0.01 <b>(-67.28%)</b></td><td>0.06 <b>(+74.75%)</b></td><td>2467.30 <b>(+205.62%)</b></td><td>821.34 <b>(+40.24%)</b></td><td>526.00 (-12.78%)</td><td>232.10 (-19.77%)</td><td>932.85 <b>(+377.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>807.30 (n/a)</td><td>585.66 (n/a)</td><td>603.10 (n/a)</td><td>289.30 (n/a)</td><td>195.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (-8.28%)</td><td>0.08 (-13.06%)</td><td>0.06 (-5.48%)</td><td>0.05 (-15.84%)</td><td>0.04 (-4.02%)</td><td>636.10 (+18.81%)</td><td>492.38 (+16.83%)</td><td>517.30 (+5.81%)</td><td>232.40 (+9.01%)</td><td>155.59 (+19.49%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>535.40 (n/a)</td><td>421.44 (n/a)</td><td>488.90 (n/a)</td><td>213.20 (n/a)</td><td>130.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 <b>(+94.32%)</b></td><td>0.11 <b>(+56.54%)</b></td><td>0.10 <b>(+46.45%)</b></td><td>0.08 (+15.79%)</td><td>0.03 <b>(+451.51%)</b></td><td>489.10 (-13.63%)</td><td>344.58 <b>(-32.12%)</b></td><td>352.50 <b>(-31.71%)</b></td><td>238.30 <b>(-48.54%)</b></td><td>99.65 <b>(+141.72%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>566.30 (n/a)</td><td>507.66 (n/a)</td><td>516.20 (n/a)</td><td>463.10 (n/a)</td><td>41.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 <b>(+68.26%)</b></td><td>0.09 <b>(+31.73%)</b></td><td>0.07 (+7.34%)</td><td>0.05 (-7.37%)</td><td>0.05 <b>(+221.45%)</b></td><td>650.80 (+7.96%)</td><td>422.94 (-11.49%)</td><td>440.50 (-6.83%)</td><td>211.50 <b>(-40.57%)</b></td><td>187.94 <b>(+103.98%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>602.80 (n/a)</td><td>477.86 (n/a)</td><td>472.80 (n/a)</td><td>355.90 (n/a)</td><td>92.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (-4.30%)</td><td>0.05 (+1.73%)</td><td>0.05 (+7.97%)</td><td>0.04 (+14.75%)</td><td>0.02 (-7.80%)</td><td>559.30 (-12.85%)</td><td>418.36 (-3.62%)</td><td>412.10 (-7.39%)</td><td>278.40 (+4.50%)</td><td>138.34 (-12.44%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>641.80 (n/a)</td><td>434.06 (n/a)</td><td>445.00 (n/a)</td><td>266.40 (n/a)</td><td>158.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (+8.01%)</td><td>0.06 (-3.89%)</td><td>0.07 (+0.67%)</td><td>0.04 (-8.12%)</td><td>0.02 <b>(+28.32%)</b></td><td>526.20 (+8.83%)</td><td>372.90 (+9.18%)</td><td>309.50 (-0.64%)</td><td>216.90 (-7.39%)</td><td>139.21 <b>(+38.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>483.50 (n/a)</td><td>341.56 (n/a)</td><td>311.50 (n/a)</td><td>234.20 (n/a)</td><td>100.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (+3.12%)</td><td>0.05 (-6.79%)</td><td>0.04 (-10.67%)</td><td>0.04 (-3.66%)</td><td>0.02 (+3.93%)</td><td>534.30 (+3.81%)</td><td>416.84 (+8.77%)</td><td>492.40 (+11.93%)</td><td>243.70 (-3.02%)</td><td>133.56 (+12.47%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>514.70 (n/a)</td><td>383.22 (n/a)</td><td>439.90 (n/a)</td><td>251.30 (n/a)</td><td>118.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 <b>(+20.25%)</b></td><td>0.06 <b>(+27.75%)</b></td><td>0.07 <b>(+65.11%)</b></td><td>0.04 <b>(+103.52%)</b></td><td>0.02 (-3.47%)</td><td>522.30 <b>(-50.86%)</b></td><td>368.52 <b>(-30.55%)</b></td><td>296.70 <b>(-39.44%)</b></td><td>229.40 (-16.85%)</td><td>133.90 <b>(-57.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1062.90 (n/a)</td><td>530.62 (n/a)</td><td>489.90 (n/a)</td><td>275.90 (n/a)</td><td>316.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-19.40%)</td><td>0.05 (+3.81%)</td><td>0.05 (+15.83%)</td><td>0.03 (-10.01%)</td><td>0.01 <b>(-22.15%)</b></td><td>639.70 (+11.12%)</td><td>449.52 (-4.86%)</td><td>439.00 (-13.67%)</td><td>320.80 <b>(+24.10%)</b></td><td>134.97 (+9.60%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.70 (n/a)</td><td>472.46 (n/a)</td><td>508.50 (n/a)</td><td>258.50 (n/a)</td><td>123.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (+2.74%)</td><td>0.05 (-4.68%)</td><td>0.05 (+3.20%)</td><td>0.03 (-6.33%)</td><td>0.03 (+7.73%)</td><td>610.50 (+6.75%)</td><td>454.20 (+7.68%)</td><td>438.60 (-3.09%)</td><td>183.00 (-2.66%)</td><td>173.49 (+9.30%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>571.90 (n/a)</td><td>421.80 (n/a)</td><td>452.60 (n/a)</td><td>188.00 (n/a)</td><td>158.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (+15.43%)</td><td>0.08 <b>(+31.67%)</b></td><td>0.08 <b>(+32.78%)</b></td><td>0.06 <b>(+41.82%)</b></td><td>0.02 (-2.28%)</td><td>408.70 <b>(-29.49%)</b></td><td>303.72 <b>(-25.71%)</b></td><td>289.10 <b>(-24.69%)</b></td><td>244.20 (-13.37%)</td><td>65.32 <b>(-40.61%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>579.60 (n/a)</td><td>408.84 (n/a)</td><td>383.90 (n/a)</td><td>281.90 (n/a)</td><td>109.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (+14.99%)</td><td>0.07 (+19.84%)</td><td>0.07 <b>(+52.89%)</b></td><td>0.04 (+7.70%)</td><td>0.03 (+17.53%)</td><td>566.50 (-7.15%)</td><td>380.92 (-15.48%)</td><td>329.90 <b>(-34.60%)</b></td><td>251.90 (-13.05%)</td><td>143.35 (-2.10%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>610.10 (n/a)</td><td>450.66 (n/a)</td><td>504.40 (n/a)</td><td>289.70 (n/a)</td><td>146.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (-2.97%)</td><td>0.06 (+16.35%)</td><td>0.06 <b>(+26.24%)</b></td><td>0.05 (+18.22%)</td><td>0.02 (-9.86%)</td><td>505.10 (-15.41%)</td><td>399.78 (-15.62%)</td><td>418.00 <b>(-20.79%)</b></td><td>293.60 (+3.05%)</td><td>96.96 <b>(-20.61%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>597.10 (n/a)</td><td>473.78 (n/a)</td><td>527.70 (n/a)</td><td>284.90 (n/a)</td><td>122.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 <b>(+28.89%)</b></td><td>0.06 (+1.17%)</td><td>0.06 <b>(-22.48%)</b></td><td>0.04 (-12.79%)</td><td>0.02 <b>(+67.78%)</b></td><td>612.00 (+14.67%)</td><td>421.06 (+5.02%)</td><td>443.30 <b>(+29.02%)</b></td><td>248.20 <b>(-22.41%)</b></td><td>146.14 <b>(+47.83%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>400.94 (n/a)</td><td>343.60 (n/a)</td><td>319.90 (n/a)</td><td>98.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 <b>(+72.04%)</b></td><td>0.08 <b>(+69.93%)</b></td><td>0.08 <b>(+68.79%)</b></td><td>0.05 <b>(+41.51%)</b></td><td>0.02 <b>(+158.00%)</b></td><td>448.60 <b>(-29.33%)</b></td><td>323.06 <b>(-39.32%)</b></td><td>315.40 <b>(-40.75%)</b></td><td>242.80 <b>(-41.89%)</b></td><td>82.62 (+6.98%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>634.80 (n/a)</td><td>532.42 (n/a)</td><td>532.30 (n/a)</td><td>417.80 (n/a)</td><td>77.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (-12.77%)</td><td>0.07 (+0.79%)</td><td>0.07 (+1.11%)</td><td>0.04 (-6.56%)</td><td>0.02 <b>(-21.16%)</b></td><td>622.60 (+7.01%)</td><td>397.64 (-3.14%)</td><td>350.60 (-1.10%)</td><td>305.00 (+14.66%)</td><td>131.99 (-6.69%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.80 (n/a)</td><td>410.52 (n/a)</td><td>354.50 (n/a)</td><td>266.00 (n/a)</td><td>141.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 <b>(+52.71%)</b></td><td>0.07 <b>(+84.57%)</b></td><td>0.07 <b>(+123.55%)</b></td><td>0.05 <b>(+87.66%)</b></td><td>0.01 (+7.09%)</td><td>359.60 <b>(-46.72%)</b></td><td>278.90 <b>(-48.37%)</b></td><td>270.00 <b>(-55.27%)</b></td><td>204.20 <b>(-34.53%)</b></td><td>55.92 <b>(-62.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>674.90 (n/a)</td><td>540.20 (n/a)</td><td>603.60 (n/a)</td><td>311.90 (n/a)</td><td>150.22 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+17.17%)</td><td>0.05 (+13.08%)</td><td>0.04 (-4.05%)</td><td>0.04 (+14.45%)</td><td>0.02 <b>(+52.52%)</b></td><td>523.60 (-12.63%)</td><td>398.08 (-8.29%)</td><td>466.60 (+4.22%)</td><td>256.50 (-14.67%)</td><td>122.96 (+10.89%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>599.30 (n/a)</td><td>434.06 (n/a)</td><td>447.70 (n/a)</td><td>300.60 (n/a)</td><td>110.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (+2.49%)</td><td>0.05 (+2.44%)</td><td>0.05 (+19.35%)</td><td>0.03 (-15.40%)</td><td>0.02 (-0.67%)</td><td>626.30 (+18.21%)</td><td>402.18 (-1.96%)</td><td>396.30 (-16.22%)</td><td>224.00 (-2.44%)</td><td>152.81 (+9.09%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.80 (n/a)</td><td>410.24 (n/a)</td><td>473.00 (n/a)</td><td>229.60 (n/a)</td><td>140.07 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (-9.14%)</td><td>0.05 (+17.80%)</td><td>0.04 (+10.72%)</td><td>0.04 <b>(+99.10%)</b></td><td>0.02 <b>(-29.74%)</b></td><td>526.30 <b>(-49.78%)</b></td><td>413.58 <b>(-26.59%)</b></td><td>464.30 (-9.67%)</td><td>257.40 (+10.05%)</td><td>118.38 <b>(-60.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1048.00 (n/a)</td><td>563.40 (n/a)</td><td>514.00 (n/a)</td><td>233.90 (n/a)</td><td>296.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (+3.02%)</td><td>0.04 (-6.40%)</td><td>0.03 <b>(-40.79%)</b></td><td>0.03 <b>(+260.71%)</b></td><td>0.02 <b>(-37.75%)</b></td><td>681.40 <b>(-72.28%)</b></td><td>537.34 <b>(-39.86%)</b></td><td>571.00 <b>(+68.88%)</b></td><td>275.50 (-2.92%)</td><td>169.41 <b>(-81.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2457.90 (n/a)</td><td>893.52 (n/a)</td><td>338.10 (n/a)</td><td>283.80 (n/a)</td><td>937.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 <b>(+47.21%)</b></td><td>0.08 <b>(+59.72%)</b></td><td>0.07 <b>(+82.87%)</b></td><td>0.06 <b>(+64.90%)</b></td><td>0.02 (+15.26%)</td><td>305.90 <b>(-39.35%)</b></td><td>242.20 <b>(-39.68%)</b></td><td>248.70 <b>(-45.33%)</b></td><td>164.90 <b>(-32.06%)</b></td><td>50.75 <b>(-55.10%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>504.40 (n/a)</td><td>401.50 (n/a)</td><td>454.90 (n/a)</td><td>242.70 (n/a)</td><td>113.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.41 <b>(-22.12%)</b></td><td>0.33 (+12.74%)</td><td>0.36 <b>(+64.02%)</b></td><td>0.21 <b>(+22.96%)</b></td><td>0.08 <b>(-51.11%)</b></td><td>466.20 (-18.67%)</td><td>309.96 <b>(-23.10%)</b></td><td>276.20 <b>(-39.03%)</b></td><td>241.40 <b>(+28.40%)</b></td><td>90.55 <b>(-48.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.52 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>573.20 (n/a)</td><td>403.06 (n/a)</td><td>453.00 (n/a)</td><td>188.00 (n/a)</td><td>175.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.37 (+15.37%)</td><td>0.26 (-5.18%)</td><td>0.22 <b>(-30.32%)</b></td><td>0.17 (-15.87%)</td><td>0.09 <b>(+64.87%)</b></td><td>573.70 (+18.85%)</td><td>411.98 (+11.64%)</td><td>457.10 <b>(+43.52%)</b></td><td>262.20 (-13.32%)</td><td>133.02 <b>(+64.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>482.70 (n/a)</td><td>369.02 (n/a)</td><td>318.50 (n/a)</td><td>302.50 (n/a)</td><td>80.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (+8.45%)</td><td>0.19 (-1.44%)</td><td>0.17 (-0.40%)</td><td>0.10 <b>(-39.47%)</b></td><td>0.08 <b>(+49.75%)</b></td><td>1031.00 <b>(+65.22%)</b></td><td>588.30 (+12.51%)</td><td>575.50 (+0.40%)</td><td>312.50 (-7.79%)</td><td>270.38 <b>(+141.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>624.00 (n/a)</td><td>522.90 (n/a)</td><td>573.20 (n/a)</td><td>338.90 (n/a)</td><td>112.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (+12.66%)</td><td>0.21 (+16.83%)</td><td>0.18 (+2.50%)</td><td>0.16 <b>(+25.82%)</b></td><td>0.07 (+10.25%)</td><td>470.20 <b>(-20.52%)</b></td><td>370.08 (-15.33%)</td><td>415.50 (-2.44%)</td><td>237.20 (-11.26%)</td><td>102.82 <b>(-22.94%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>591.60 (n/a)</td><td>437.10 (n/a)</td><td>425.90 (n/a)</td><td>267.30 (n/a)</td><td>133.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.24 <b>(-21.39%)</b></td><td>0.18 (+6.67%)</td><td>0.16 (+11.58%)</td><td>0.13 (+2.67%)</td><td>0.05 <b>(-29.89%)</b></td><td>579.20 (-2.59%)</td><td>426.80 (-9.92%)</td><td>454.90 (-10.38%)</td><td>303.30 <b>(+27.22%)</b></td><td>120.38 (-12.50%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>594.60 (n/a)</td><td>473.78 (n/a)</td><td>507.60 (n/a)</td><td>238.40 (n/a)</td><td>137.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.26 (-17.07%)</td><td>0.19 (-13.44%)</td><td>0.17 (-4.33%)</td><td>0.14 (-4.92%)</td><td>0.04 <b>(-40.16%)</b></td><td>526.50 (+5.17%)</td><td>412.84 (+10.31%)</td><td>423.40 (+4.52%)</td><td>288.50 <b>(+20.61%)</b></td><td>85.64 <b>(-25.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>500.60 (n/a)</td><td>374.26 (n/a)</td><td>405.10 (n/a)</td><td>239.20 (n/a)</td><td>114.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 <b>(-21.19%)</b></td><td>0.12 <b>(+33.53%)</b></td><td>0.13 <b>(+83.08%)</b></td><td>0.07 <b>(+41.53%)</b></td><td>0.03 <b>(-43.92%)</b></td><td>502.60 <b>(-29.34%)</b></td><td>318.16 <b>(-35.06%)</b></td><td>279.50 <b>(-45.38%)</b></td><td>243.70 <b>(+26.86%)</b></td><td>107.63 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>711.30 (n/a)</td><td>489.90 (n/a)</td><td>511.70 (n/a)</td><td>192.10 (n/a)</td><td>203.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 <b>(-28.39%)</b></td><td>0.10 (-6.92%)</td><td>0.09 <b>(-25.81%)</b></td><td>0.08 <b>(+44.86%)</b></td><td>0.02 <b>(-54.48%)</b></td><td>453.60 <b>(-30.97%)</b></td><td>384.18 (-6.23%)</td><td>430.70 <b>(+34.76%)</b></td><td>283.80 <b>(+39.60%)</b></td><td>79.68 <b>(-57.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>657.10 (n/a)</td><td>409.70 (n/a)</td><td>319.60 (n/a)</td><td>203.30 (n/a)</td><td>186.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (+3.74%)</td><td>0.09 (+3.11%)</td><td>0.08 (-0.06%)</td><td>0.04 <b>(-46.41%)</b></td><td>0.04 <b>(+60.77%)</b></td><td>1008.30 <b>(+86.62%)</b></td><td>513.94 (+15.11%)</td><td>489.50 (+0.06%)</td><td>264.90 (-3.60%)</td><td>299.65 <b>(+192.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>540.30 (n/a)</td><td>446.46 (n/a)</td><td>489.20 (n/a)</td><td>274.80 (n/a)</td><td>102.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (-12.39%)</td><td>0.10 (-9.25%)</td><td>0.09 <b>(-27.17%)</b></td><td>0.07 (+8.02%)</td><td>0.04 <b>(-24.50%)</b></td><td>542.20 (-7.43%)</td><td>395.36 (+3.55%)</td><td>414.60 <b>(+37.33%)</b></td><td>240.40 (+14.15%)</td><td>123.15 <b>(-25.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>585.70 (n/a)</td><td>381.80 (n/a)</td><td>301.90 (n/a)</td><td>210.60 (n/a)</td><td>165.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.20 <b>(+145.46%)</b></td><td>0.09 <b>(+44.13%)</b></td><td>0.08 <b>(+21.41%)</b></td><td>0.06 (+3.73%)</td><td>0.06 <b>(+484.67%)</b></td><td>633.80 (-3.59%)</td><td>476.58 (-16.75%)</td><td>473.30 (-17.63%)</td><td>186.10 <b>(-59.25%)</b></td><td>180.72 <b>(+118.69%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>657.40 (n/a)</td><td>572.48 (n/a)</td><td>574.60 (n/a)</td><td>456.70 (n/a)</td><td>82.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 <b>(+48.75%)</b></td><td>0.11 <b>(+28.33%)</b></td><td>0.11 <b>(+29.38%)</b></td><td>0.07 (+10.68%)</td><td>0.05 <b>(+98.64%)</b></td><td>501.20 (-9.64%)</td><td>356.12 (-17.28%)</td><td>330.60 <b>(-22.72%)</b></td><td>193.90 <b>(-32.77%)</b></td><td>117.32 <b>(+23.12%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>430.50 (n/a)</td><td>427.80 (n/a)</td><td>288.40 (n/a)</td><td>95.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (-12.71%)</td><td>0.12 (-1.05%)</td><td>0.14 (+2.58%)</td><td>0.08 <b>(+22.40%)</b></td><td>0.03 <b>(-23.55%)</b></td><td>502.30 (-18.30%)</td><td>366.22 (-3.99%)</td><td>296.30 (-2.53%)</td><td>267.50 (+14.56%)</td><td>112.12 <b>(-28.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>614.80 (n/a)</td><td>381.44 (n/a)</td><td>304.00 (n/a)</td><td>233.50 (n/a)</td><td>156.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (-17.76%)</td><td>0.10 (-2.15%)</td><td>0.09 (+10.58%)</td><td>0.07 (+17.73%)</td><td>0.03 <b>(-37.08%)</b></td><td>611.10 (-15.07%)</td><td>434.14 (-7.89%)</td><td>454.80 (-9.56%)</td><td>299.80 <b>(+21.57%)</b></td><td>132.75 <b>(-36.09%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>719.50 (n/a)</td><td>471.34 (n/a)</td><td>502.90 (n/a)</td><td>246.60 (n/a)</td><td>207.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (-4.66%)</td><td>0.10 (-19.49%)</td><td>0.09 <b>(-28.94%)</b></td><td>0.07 (-0.03%)</td><td>0.04 (-11.44%)</td><td>598.00 (+0.03%)</td><td>453.80 <b>(+22.00%)</b></td><td>465.90 <b>(+40.71%)</b></td><td>239.70 (+4.90%)</td><td>150.38 (-3.10%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>597.80 (n/a)</td><td>371.96 (n/a)</td><td>331.10 (n/a)</td><td>228.50 (n/a)</td><td>155.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (-15.73%)</td><td>0.09 (+9.49%)</td><td>0.09 <b>(+20.62%)</b></td><td>0.02 (-1.12%)</td><td>0.05 (-9.02%)</td><td>1947.90 (+1.13%)</td><td>702.80 (-6.46%)</td><td>465.50 (-17.10%)</td><td>291.50 (+18.64%)</td><td>702.32 (+4.76%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1926.10 (n/a)</td><td>751.30 (n/a)</td><td>561.50 (n/a)</td><td>245.70 (n/a)</td><td>670.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 <b>(+52.88%)</b></td><td>0.10 <b>(+31.93%)</b></td><td>0.09 (+6.07%)</td><td>0.08 <b>(+87.45%)</b></td><td>0.02 (+18.06%)</td><td>542.30 <b>(-46.66%)</b></td><td>444.88 <b>(-27.76%)</b></td><td>457.90 (-5.72%)</td><td>294.70 <b>(-34.60%)</b></td><td>92.00 <b>(-61.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>1016.60 (n/a)</td><td>615.82 (n/a)</td><td>485.70 (n/a)</td><td>450.60 (n/a)</td><td>236.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 <b>(+35.63%)</b></td><td>0.10 (-1.20%)</td><td>0.08 (-4.52%)</td><td>0.08 (-11.37%)</td><td>0.05 <b>(+96.60%)</b></td><td>543.80 (+12.84%)</td><td>451.60 (+9.64%)</td><td>491.00 (+4.71%)</td><td>214.00 <b>(-26.26%)</b></td><td>134.97 <b>(+51.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>481.90 (n/a)</td><td>411.90 (n/a)</td><td>468.90 (n/a)</td><td>290.20 (n/a)</td><td>88.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 <b>(-46.14%)</b></td><td>0.05 <b>(-60.68%)</b></td><td>0.07 <b>(-55.17%)</b></td><td>0.02 <b>(-74.72%)</b></td><td>0.03 (-19.50%)</td><td>1991.80 <b>(+295.51%)</b></td><td>1057.68 <b>(+262.27%)</b></td><td>535.20 <b>(+123.00%)</b></td><td>387.50 <b>(+85.58%)</b></td><td>801.95 <b>(+551.19%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>503.60 (n/a)</td><td>291.96 (n/a)</td><td>240.00 (n/a)</td><td>208.80 (n/a)</td><td>123.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (-17.44%)</td><td>0.12 (+13.78%)</td><td>0.13 (+5.92%)</td><td>0.07 <b>(+93.62%)</b></td><td>0.03 <b>(-46.04%)</b></td><td>513.50 <b>(-48.35%)</b></td><td>322.58 <b>(-31.55%)</b></td><td>273.70 (-5.59%)</td><td>249.40 <b>(+21.13%)</b></td><td>109.98 <b>(-66.39%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>994.20 (n/a)</td><td>471.28 (n/a)</td><td>289.90 (n/a)</td><td>205.90 (n/a)</td><td>327.19 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 <b>(-47.17%)</b></td><td>0.06 <b>(-35.65%)</b></td><td>0.06 <b>(-24.36%)</b></td><td>0.03 <b>(-49.84%)</b></td><td>0.01 <b>(-40.32%)</b></td><td>995.40 <b>(+99.36%)</b></td><td>664.66 <b>(+57.79%)</b></td><td>572.10 <b>(+32.19%)</b></td><td>535.80 <b>(+89.26%)</b></td><td>194.18 <b>(+135.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>499.30 (n/a)</td><td>421.22 (n/a)</td><td>432.80 (n/a)</td><td>283.10 (n/a)</td><td>82.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (+12.99%)</td><td>0.08 (+4.02%)</td><td>0.09 (+17.35%)</td><td>0.03 <b>(-48.09%)</b></td><td>0.04 <b>(+131.43%)</b></td><td>1111.00 <b>(+92.65%)</b></td><td>581.66 <b>(+21.89%)</b></td><td>408.80 (-14.80%)</td><td>295.40 (-11.48%)</td><td>357.89 <b>(+287.48%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>576.70 (n/a)</td><td>477.20 (n/a)</td><td>479.80 (n/a)</td><td>333.70 (n/a)</td><td>92.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 <b>(+113.30%)</b></td><td>0.09 <b>(+25.42%)</b></td><td>0.07 (-13.17%)</td><td>0.05 (+3.89%)</td><td>0.06 <b>(+281.12%)</b></td><td>662.80 (-3.75%)</td><td>463.58 (-6.25%)</td><td>521.60 (+15.17%)</td><td>181.90 <b>(-53.11%)</b></td><td>179.25 <b>(+52.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>688.60 (n/a)</td><td>494.50 (n/a)</td><td>452.90 (n/a)</td><td>387.90 (n/a)</td><td>117.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (-19.92%)</td><td>0.08 (-14.52%)</td><td>0.07 (-9.18%)</td><td>0.06 (-13.90%)</td><td>0.03 <b>(-25.22%)</b></td><td>624.00 (+16.16%)</td><td>453.34 (+14.80%)</td><td>477.00 (+10.11%)</td><td>302.00 <b>(+24.90%)</b></td><td>136.48 (+6.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.20 (n/a)</td><td>394.90 (n/a)</td><td>433.20 (n/a)</td><td>241.80 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.29 <b>(-27.35%)</b></td><td>0.23 (-11.48%)</td><td>0.22 (-3.70%)</td><td>0.19 (+19.15%)</td><td>0.04 <b>(-62.97%)</b></td><td>694.90 (-16.06%)</td><td>574.24 (+3.11%)</td><td>588.70 (+3.85%)</td><td>456.10 <b>(+37.63%)</b></td><td>86.94 <b>(-56.71%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>827.90 (n/a)</td><td>556.90 (n/a)</td><td>566.90 (n/a)</td><td>331.40 (n/a)</td><td>200.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.37 <b>(-26.92%)</b></td><td>0.27 (-13.59%)</td><td>0.25 (+6.77%)</td><td>0.22 (-4.31%)</td><td>0.06 <b>(-52.10%)</b></td><td>594.30 (+4.50%)</td><td>497.22 (+7.97%)</td><td>525.00 (-6.33%)</td><td>357.00 <b>(+36.83%)</b></td><td>92.98 <b>(-36.19%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>568.70 (n/a)</td><td>460.52 (n/a)</td><td>560.50 (n/a)</td><td>260.90 (n/a)</td><td>145.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.43 (-9.07%)</td><td>0.26 (-16.74%)</td><td>0.23 (-2.96%)</td><td>0.20 (-5.49%)</td><td>0.09 <b>(-29.16%)</b></td><td>663.60 (+5.82%)</td><td>534.28 (+13.43%)</td><td>564.20 (+3.05%)</td><td>304.70 (+9.96%)</td><td>135.04 <b>(-22.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>627.10 (n/a)</td><td>471.02 (n/a)</td><td>547.50 (n/a)</td><td>277.10 (n/a)</td><td>173.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-29.32%)</b></td><td>0.01 (-2.16%)</td><td>0.01 <b>(+31.32%)</b></td><td>0.01 (+16.85%)</td><td>0.00 <b>(-46.76%)</b></td><td>512.00 (-14.42%)</td><td>363.56 (-5.51%)</td><td>304.60 <b>(-23.85%)</b></td><td>295.10 <b>(+41.53%)</b></td><td>94.54 <b>(-35.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.30 (n/a)</td><td>384.74 (n/a)</td><td>400.00 (n/a)</td><td>208.50 (n/a)</td><td>147.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+4.58%)</td><td>0.01 (+2.54%)</td><td>0.01 (+5.70%)</td><td>0.01 <b>(-24.74%)</b></td><td>0.00 <b>(+48.02%)</b></td><td>520.10 <b>(+32.88%)</b></td><td>314.40 (+2.99%)</td><td>274.70 (-5.37%)</td><td>222.80 (-4.38%)</td><td>117.90 <b>(+100.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>391.40 (n/a)</td><td>305.26 (n/a)</td><td>290.30 (n/a)</td><td>233.00 (n/a)</td><td>58.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+17.76%)</td><td>0.01 (+5.52%)</td><td>0.01 (+9.45%)</td><td>0.01 (-17.79%)</td><td>0.00 <b>(+86.93%)</b></td><td>527.50 <b>(+21.63%)</b></td><td>359.50 (-0.43%)</td><td>303.60 (-8.64%)</td><td>257.60 (-15.07%)</td><td>111.95 <b>(+92.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>433.70 (n/a)</td><td>361.06 (n/a)</td><td>332.30 (n/a)</td><td>303.30 (n/a)</td><td>58.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>9.01 (+13.20%)</td><td>7.81 <b>(+35.31%)</b></td><td>7.73 <b>(+26.22%)</b></td><td>6.61 <b>(+115.84%)</b></td><td>0.94 <b>(-53.28%)</b></td><td>317.40 <b>(-53.68%)</b></td><td>271.74 <b>(-33.73%)</b></td><td>271.50 <b>(-20.75%)</b></td><td>232.90 (-11.68%)</td><td>33.00 <b>(-80.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.96 (n/a)</td><td>5.77 (n/a)</td><td>6.12 (n/a)</td><td>3.06 (n/a)</td><td>2.01 (n/a)</td><td>685.20 (n/a)</td><td>410.02 (n/a)</td><td>342.60 (n/a)</td><td>263.70 (n/a)</td><td>173.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.53 (-4.32%)</td><td>0.33 (-18.47%)</td><td>0.32 <b>(-28.80%)</b></td><td>0.15 <b>(-42.54%)</b></td><td>0.14 (+9.62%)</td><td>854.20 <b>(+74.01%)</b></td><td>468.60 <b>(+32.29%)</b></td><td>413.70 <b>(+40.48%)</b></td><td>247.20 (+4.48%)</td><td>228.01 <b>(+99.38%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>490.90 (n/a)</td><td>354.22 (n/a)</td><td>294.50 (n/a)</td><td>236.60 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.67 <b>(+23.29%)</b></td><td>0.40 (-7.97%)</td><td>0.34 <b>(-25.84%)</b></td><td>0.21 (-18.12%)</td><td>0.19 <b>(+64.24%)</b></td><td>629.50 <b>(+22.14%)</b></td><td>398.44 <b>(+20.60%)</b></td><td>393.60 <b>(+34.84%)</b></td><td>198.30 (-18.90%)</td><td>177.14 <b>(+59.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>515.40 (n/a)</td><td>330.38 (n/a)</td><td>291.90 (n/a)</td><td>244.50 (n/a)</td><td>110.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.45 <b>(-24.29%)</b></td><td>0.38 (-3.52%)</td><td>0.41 <b>(+24.05%)</b></td><td>0.23 (+4.70%)</td><td>0.09 <b>(-48.15%)</b></td><td>572.10 (-4.49%)</td><td>371.76 (-6.02%)</td><td>324.10 (-19.38%)</td><td>290.50 <b>(+32.11%)</b></td><td>116.19 <b>(-30.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.60 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>599.00 (n/a)</td><td>395.56 (n/a)</td><td>402.00 (n/a)</td><td>219.90 (n/a)</td><td>166.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.61 (+8.76%)</td><td>0.36 (+7.00%)</td><td>0.40 <b>(+35.73%)</b></td><td>0.07 <b>(-60.54%)</b></td><td>0.20 <b>(+39.61%)</b></td><td>1890.30 <b>(+153.39%)</b></td><td>648.64 <b>(+41.61%)</b></td><td>326.40 <b>(-26.34%)</b></td><td>216.70 (-8.02%)</td><td>702.54 <b>(+265.56%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.56 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>746.00 (n/a)</td><td>458.04 (n/a)</td><td>443.10 (n/a)</td><td>235.60 (n/a)</td><td>192.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.70 (+12.21%)</td><td>0.53 (+15.66%)</td><td>0.52 (+11.38%)</td><td>0.41 <b>(+72.79%)</b></td><td>0.10 <b>(-25.53%)</b></td><td>321.00 <b>(-42.13%)</b></td><td>254.68 (-19.88%)</td><td>252.50 (-10.21%)</td><td>190.00 (-10.88%)</td><td>47.48 <b>(-64.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.62 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>554.70 (n/a)</td><td>317.88 (n/a)</td><td>281.20 (n/a)</td><td>213.20 (n/a)</td><td>135.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (+5.30%)</td><td>0.01 (-2.49%)</td><td>0.01 (+4.53%)</td><td>0.01 <b>(-33.11%)</b></td><td>0.01 <b>(+52.78%)</b></td><td>818.90 <b>(+49.52%)</b></td><td>419.62 (+18.91%)</td><td>297.10 (-4.32%)</td><td>227.60 (-5.05%)</td><td>247.98 <b>(+108.18%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.70 (n/a)</td><td>352.90 (n/a)</td><td>310.50 (n/a)</td><td>239.70 (n/a)</td><td>119.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 <b>(-31.75%)</b></td><td>0.01 <b>(-30.02%)</b></td><td>0.01 <b>(-32.71%)</b></td><td>0.01 (+2.35%)</td><td>0.00 <b>(-52.76%)</b></td><td>481.80 (-2.29%)</td><td>412.20 <b>(+34.11%)</b></td><td>424.50 <b>(+48.63%)</b></td><td>292.50 <b>(+46.54%)</b></td><td>72.08 <b>(-36.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.10 (n/a)</td><td>307.36 (n/a)</td><td>285.60 (n/a)</td><td>199.60 (n/a)</td><td>113.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.00 (+16.67%)</td><td>0.00 (+5.88%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+37.58%)</b></td><td>20396.68 (+13.14%)</td><td>14766.60 (+12.46%)</td><td>19433.64 <b>(+55.41%)</b></td><td>5876.91 <b>(-20.65%)</b></td><td>7148.54 <b>(+52.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18027.77 (n/a)</td><td>13130.72 (n/a)</td><td>12504.96 (n/a)</td><td>7406.46 (n/a)</td><td>4673.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.00 (-18.18%)</td><td>0.00 <b>(-22.86%)</b></td><td>0.00 (-16.67%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (-11.58%)</td><td>22547.57 <b>(+37.72%)</b></td><td>17280.07 <b>(+34.96%)</b></td><td>17610.24 <b>(+25.18%)</b></td><td>9569.62 <b>(+25.68%)</b></td><td>4822.53 <b>(+38.56%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16371.66 (n/a)</td><td>12803.93 (n/a)</td><td>14068.39 (n/a)</td><td>7614.33 (n/a)</td><td>3480.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (-5.70%)</td><td>0.09 (-13.67%)</td><td>0.08 (-8.90%)</td><td>0.07 (-0.84%)</td><td>0.02 <b>(-21.65%)</b></td><td>29637.33 (+0.92%)</td><td>25428.51 (+13.27%)</td><td>27696.78 (+9.74%)</td><td>16465.11 (+6.06%)</td><td>5304.02 (-14.95%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29367.27 (n/a)</td><td>22449.32 (n/a)</td><td>25239.64 (n/a)</td><td>15525.01 (n/a)</td><td>6236.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.55 (-3.22%)</td><td>1.41 <b>(-22.71%)</b></td><td>1.34 <b>(-39.48%)</b></td><td>0.33 <b>(-41.79%)</b></td><td>0.79 (-6.27%)</td><td>3223.10 <b>(+71.80%)</b></td><td>1182.00 <b>(+49.31%)</b></td><td>782.00 <b>(+65.22%)</b></td><td>411.90 (+3.31%)</td><td>1151.63 <b>(+85.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.63 (n/a)</td><td>1.82 (n/a)</td><td>2.22 (n/a)</td><td>0.56 (n/a)</td><td>0.84 (n/a)</td><td>1876.10 (n/a)</td><td>791.62 (n/a)</td><td>473.30 (n/a)</td><td>398.70 (n/a)</td><td>622.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.82 <b>(+92.26%)</b></td><td>1.92 (+16.73%)</td><td>1.41 (-19.16%)</td><td>0.30 <b>(-44.08%)</b></td><td>1.71 <b>(+95.59%)</b></td><td>3439.50 <b>(+78.83%)</b></td><td>1159.78 <b>(+30.89%)</b></td><td>742.60 <b>(+23.70%)</b></td><td>217.80 <b>(-47.98%)</b></td><td>1295.28 <b>(+103.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.50 (n/a)</td><td>1.65 (n/a)</td><td>1.75 (n/a)</td><td>0.55 (n/a)</td><td>0.87 (n/a)</td><td>1923.30 (n/a)</td><td>886.10 (n/a)</td><td>600.30 (n/a)</td><td>418.70 (n/a)</td><td>635.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.68 (-7.84%)</td><td>1.80 (+9.52%)</td><td>1.73 (+6.77%)</td><td>1.00 <b>(+206.85%)</b></td><td>0.60 <b>(-34.99%)</b></td><td>1049.00 <b>(-67.41%)</b></td><td>644.40 <b>(-41.34%)</b></td><td>605.40 (-6.36%)</td><td>391.20 (+8.49%)</td><td>243.84 <b>(-79.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.91 (n/a)</td><td>1.64 (n/a)</td><td>1.62 (n/a)</td><td>0.33 (n/a)</td><td>0.92 (n/a)</td><td>3218.80 (n/a)</td><td>1098.62 (n/a)</td><td>646.50 (n/a)</td><td>360.60 (n/a)</td><td>1192.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.62 <b>(+41.55%)</b></td><td>2.90 <b>(+123.91%)</b></td><td>2.75 <b>(+93.17%)</b></td><td>1.83 <b>(+526.26%)</b></td><td>0.74 (-18.45%)</td><td>572.20 <b>(-84.03%)</b></td><td>384.18 <b>(-73.50%)</b></td><td>380.90 <b>(-48.23%)</b></td><td>289.90 <b>(-29.34%)</b></td><td>114.80 <b>(-91.32%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.56 (n/a)</td><td>1.30 (n/a)</td><td>1.43 (n/a)</td><td>0.29 (n/a)</td><td>0.91 (n/a)</td><td>3583.40 (n/a)</td><td>1449.62 (n/a)</td><td>735.80 (n/a)</td><td>410.30 (n/a)</td><td>1322.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.57 <b>(+27.83%)</b></td><td>3.15 <b>(+36.84%)</b></td><td>3.55 <b>(+86.19%)</b></td><td>0.58 (-0.30%)</td><td>1.53 <b>(+20.28%)</b></td><td>3626.30 (+0.30%)</td><td>1175.82 (-15.99%)</td><td>590.10 <b>(-46.30%)</b></td><td>458.70 <b>(-21.78%)</b></td><td>1371.86 (+8.45%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.58 (n/a)</td><td>2.30 (n/a)</td><td>1.91 (n/a)</td><td>0.58 (n/a)</td><td>1.27 (n/a)</td><td>3615.50 (n/a)</td><td>1399.58 (n/a)</td><td>1098.80 (n/a)</td><td>586.40 (n/a)</td><td>1264.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.74 <b>(+54.87%)</b></td><td>3.74 <b>(+21.55%)</b></td><td>3.43 (+5.54%)</td><td>2.49 (+19.14%)</td><td>1.25 <b>(+85.89%)</b></td><td>841.00 (-16.06%)</td><td>607.02 (-14.87%)</td><td>611.00 (-5.26%)</td><td>365.20 <b>(-35.43%)</b></td><td>178.54 (-1.15%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.71 (n/a)</td><td>3.08 (n/a)</td><td>3.25 (n/a)</td><td>2.09 (n/a)</td><td>0.67 (n/a)</td><td>1001.90 (n/a)</td><td>713.08 (n/a)</td><td>644.90 (n/a)</td><td>565.60 (n/a)</td><td>180.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.82 (+15.47%)</td><td>3.21 (-12.47%)</td><td>2.22 <b>(-42.42%)</b></td><td>0.85 <b>(-68.70%)</b></td><td>2.10 <b>(+125.60%)</b></td><td>2481.40 <b>(+219.44%)</b></td><td>1033.66 <b>(+72.15%)</b></td><td>946.00 <b>(+73.67%)</b></td><td>360.40 (-13.41%)</td><td>857.37 <b>(+483.26%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.04 (n/a)</td><td>3.67 (n/a)</td><td>3.85 (n/a)</td><td>2.70 (n/a)</td><td>0.93 (n/a)</td><td>776.80 (n/a)</td><td>600.44 (n/a)</td><td>544.70 (n/a)</td><td>416.20 (n/a)</td><td>147.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.11 <b>(+158.01%)</b></td><td>4.41 <b>(+148.91%)</b></td><td>3.75 <b>(+90.97%)</b></td><td>2.92 <b>(+390.63%)</b></td><td>1.67 <b>(+65.11%)</b></td><td>717.30 <b>(-79.62%)</b></td><td>523.84 <b>(-69.57%)</b></td><td>558.90 <b>(-47.63%)</b></td><td>294.90 <b>(-61.24%)</b></td><td>165.18 <b>(-86.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.76 (n/a)</td><td>1.77 (n/a)</td><td>1.97 (n/a)</td><td>0.60 (n/a)</td><td>1.01 (n/a)</td><td>3519.30 (n/a)</td><td>1721.20 (n/a)</td><td>1067.30 (n/a)</td><td>760.80 (n/a)</td><td>1230.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.40 (+12.56%)</td><td>3.47 (+11.71%)</td><td>3.47 <b>(+32.67%)</b></td><td>2.01 (-18.10%)</td><td>1.49 <b>(+50.76%)</b></td><td>1044.30 <b>(+22.11%)</b></td><td>708.90 (-1.50%)</td><td>604.70 <b>(-24.62%)</b></td><td>388.30 (-11.16%)</td><td>310.57 <b>(+78.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>4.80 (n/a)</td><td>3.10 (n/a)</td><td>2.61 (n/a)</td><td>2.45 (n/a)</td><td>0.99 (n/a)</td><td>855.20 (n/a)</td><td>719.72 (n/a)</td><td>802.20 (n/a)</td><td>437.10 (n/a)</td><td>173.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.92 <b>(-20.14%)</b></td><td>3.11 (-10.51%)</td><td>4.25 <b>(+34.74%)</b></td><td>0.59 <b>(-68.43%)</b></td><td>2.08 <b>(+28.27%)</b></td><td>3561.80 <b>(+216.77%)</b></td><td>1360.86 <b>(+93.93%)</b></td><td>492.90 <b>(-25.78%)</b></td><td>426.50 <b>(+25.22%)</b></td><td>1375.29 <b>(+379.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.16 (n/a)</td><td>3.48 (n/a)</td><td>3.16 (n/a)</td><td>1.87 (n/a)</td><td>1.62 (n/a)</td><td>1124.40 (n/a)</td><td>701.74 (n/a)</td><td>664.10 (n/a)</td><td>340.60 (n/a)</td><td>286.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.96 (-11.35%)</td><td>3.52 (+13.38%)</td><td>3.88 (+19.96%)</td><td>1.19 <b>(-29.56%)</b></td><td>1.40 (-12.01%)</td><td>3536.50 <b>(+41.97%)</b></td><td>1537.18 (-6.62%)</td><td>1080.90 (-16.64%)</td><td>845.50 (+12.79%)</td><td>1123.57 <b>(+46.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>5.60 (n/a)</td><td>3.10 (n/a)</td><td>3.23 (n/a)</td><td>1.68 (n/a)</td><td>1.59 (n/a)</td><td>2491.00 (n/a)</td><td>1646.12 (n/a)</td><td>1296.60 (n/a)</td><td>749.60 (n/a)</td><td>764.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>8.50 <b>(+25.44%)</b></td><td>5.30 <b>(+40.13%)</b></td><td>5.22 <b>(+146.57%)</b></td><td>1.27 <b>(-24.32%)</b></td><td>3.15 (+18.07%)</td><td>3295.20 <b>(+32.14%)</b></td><td>1281.98 <b>(-21.79%)</b></td><td>803.40 <b>(-59.45%)</b></td><td>493.30 <b>(-20.28%)</b></td><td>1173.28 <b>(+23.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.78 (n/a)</td><td>3.78 (n/a)</td><td>2.12 (n/a)</td><td>1.68 (n/a)</td><td>2.67 (n/a)</td><td>2493.70 (n/a)</td><td>1639.22 (n/a)</td><td>1981.10 (n/a)</td><td>618.80 (n/a)</td><td>946.99 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.94 <b>(+23.65%)</b></td><td>5.17 <b>(+36.45%)</b></td><td>5.76 <b>(+58.08%)</b></td><td>1.33 <b>(-23.22%)</b></td><td>2.87 <b>(+70.80%)</b></td><td>3148.30 <b>(+30.25%)</b></td><td>1256.26 (-4.48%)</td><td>728.20 <b>(-36.74%)</b></td><td>528.60 (-19.11%)</td><td>1106.16 <b>(+68.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>6.42 (n/a)</td><td>3.79 (n/a)</td><td>3.64 (n/a)</td><td>1.74 (n/a)</td><td>1.68 (n/a)</td><td>2417.10 (n/a)</td><td>1315.14 (n/a)</td><td>1151.10 (n/a)</td><td>653.50 (n/a)</td><td>655.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>9.62 (+4.71%)</td><td>5.66 (-9.46%)</td><td>6.92 (+6.07%)</td><td>1.12 <b>(-68.03%)</b></td><td>4.20 <b>(+94.67%)</b></td><td>3744.40 <b>(+212.76%)</b></td><td>1697.44 <b>(+127.15%)</b></td><td>605.80 (-5.73%)</td><td>436.10 (-4.51%)</td><td>1654.23 <b>(+474.54%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>9.18 (n/a)</td><td>6.25 (n/a)</td><td>6.53 (n/a)</td><td>3.50 (n/a)</td><td>2.16 (n/a)</td><td>1197.20 (n/a)</td><td>747.28 (n/a)</td><td>642.60 (n/a)</td><td>456.70 (n/a)</td><td>287.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.17 (-19.43%)</td><td>5.80 (+7.84%)</td><td>6.70 <b>(+20.79%)</b></td><td>1.97 <b>(+67.80%)</b></td><td>2.16 <b>(-24.88%)</b></td><td>2128.80 <b>(-40.40%)</b></td><td>923.20 <b>(-27.38%)</b></td><td>626.00 (-17.22%)</td><td>585.00 <b>(+24.12%)</b></td><td>674.38 <b>(-48.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>8.90 (n/a)</td><td>5.38 (n/a)</td><td>5.55 (n/a)</td><td>1.17 (n/a)</td><td>2.87 (n/a)</td><td>3572.10 (n/a)</td><td>1271.20 (n/a)</td><td>756.20 (n/a)</td><td>471.30 (n/a)</td><td>1297.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.97 (-4.00%)</td><td>5.17 (+18.85%)</td><td>4.39 (-19.75%)</td><td>4.26 <b>(+265.95%)</b></td><td>1.21 <b>(-55.67%)</b></td><td>983.90 <b>(-72.67%)</b></td><td>843.92 <b>(-47.71%)</b></td><td>956.50 <b>(+24.61%)</b></td><td>601.40 (+4.17%)</td><td>175.64 <b>(-86.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>7.27 (n/a)</td><td>4.35 (n/a)</td><td>5.46 (n/a)</td><td>1.16 (n/a)</td><td>2.74 (n/a)</td><td>3600.70 (n/a)</td><td>1614.04 (n/a)</td><td>767.60 (n/a)</td><td>577.30 (n/a)</td><td>1350.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>1.70 (+0.15%)</td><td>0.91 <b>(-31.04%)</b></td><td>0.82 <b>(-40.73%)</b></td><td>0.15 <b>(-74.82%)</b></td><td>0.73 <b>(+68.77%)</b></td><td>3385.00 <b>(+297.07%)</b></td><td>1316.12 <b>(+190.52%)</b></td><td>642.80 <b>(+68.71%)</b></td><td>308.80 (-0.13%)</td><td>1332.79 <b>(+487.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.70 (n/a)</td><td>1.33 (n/a)</td><td>1.38 (n/a)</td><td>0.62 (n/a)</td><td>0.43 (n/a)</td><td>852.50 (n/a)</td><td>453.02 (n/a)</td><td>381.00 (n/a)</td><td>309.20 (n/a)</td><td>226.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.61 (+6.74%)</td><td>1.95 (+8.37%)</td><td>1.72 (+13.62%)</td><td>1.48 <b>(+25.83%)</b></td><td>0.53 (-10.59%)</td><td>708.90 <b>(-20.53%)</b></td><td>570.10 (-10.43%)</td><td>610.10 (-11.99%)</td><td>401.90 (-6.32%)</td><td>145.65 <b>(-28.01%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>2.44 (n/a)</td><td>1.80 (n/a)</td><td>1.51 (n/a)</td><td>1.18 (n/a)</td><td>0.60 (n/a)</td><td>892.00 (n/a)</td><td>636.46 (n/a)</td><td>693.20 (n/a)</td><td>429.00 (n/a)</td><td>202.31 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.75 (-1.69%)</td><td>1.72 <b>(-37.86%)</b></td><td>1.07 <b>(-67.17%)</b></td><td>0.60 <b>(-31.01%)</b></td><td>1.36 (+18.05%)</td><td>3479.40 <b>(+44.94%)</b></td><td>1974.00 <b>(+95.25%)</b></td><td>1956.40 <b>(+204.64%)</b></td><td>558.50 (+1.71%)</td><td>1286.10 <b>(+64.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>3.82 (n/a)</td><td>2.76 (n/a)</td><td>3.27 (n/a)</td><td>0.87 (n/a)</td><td>1.15 (n/a)</td><td>2400.60 (n/a)</td><td>1011.00 (n/a)</td><td>642.20 (n/a)</td><td>549.10 (n/a)</td><td>783.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.07 <b>(+21.76%)</b></td><td>1.46 <b>(+26.14%)</b></td><td>1.46 <b>(+44.90%)</b></td><td>0.95 <b>(+22.05%)</b></td><td>0.40 (+11.06%)</td><td>553.40 (-18.06%)</td><td>381.12 <b>(-21.59%)</b></td><td>358.20 <b>(-31.00%)</b></td><td>253.00 (-17.88%)</td><td>108.66 <b>(-22.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>1.70 (n/a)</td><td>1.16 (n/a)</td><td>1.01 (n/a)</td><td>0.78 (n/a)</td><td>0.36 (n/a)</td><td>675.40 (n/a)</td><td>486.08 (n/a)</td><td>519.10 (n/a)</td><td>308.10 (n/a)</td><td>140.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (+15.03%)</td><td>0.11 <b>(+30.90%)</b></td><td>0.10 <b>(+39.02%)</b></td><td>0.08 <b>(+24.37%)</b></td><td>0.02 (-4.88%)</td><td>416.20 (-19.59%)</td><td>314.92 <b>(-25.02%)</b></td><td>318.60 <b>(-28.07%)</b></td><td>233.80 (-13.09%)</td><td>66.73 <b>(-31.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>517.60 (n/a)</td><td>420.00 (n/a)</td><td>442.90 (n/a)</td><td>269.00 (n/a)</td><td>97.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (-3.18%)</td><td>0.08 (-19.42%)</td><td>0.07 <b>(-27.38%)</b></td><td>0.05 (-19.36%)</td><td>0.03 (+14.59%)</td><td>667.40 <b>(+24.01%)</b></td><td>465.98 <b>(+28.76%)</b></td><td>460.20 <b>(+37.70%)</b></td><td>248.80 (+3.28%)</td><td>153.60 <b>(+37.25%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>538.20 (n/a)</td><td>361.90 (n/a)</td><td>334.20 (n/a)</td><td>240.90 (n/a)</td><td>111.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.26 (-7.98%)</td><td>0.20 (+11.25%)</td><td>0.20 <b>(+25.82%)</b></td><td>0.14 (-1.09%)</td><td>0.04 <b>(-23.22%)</b></td><td>482.60 (+1.11%)</td><td>343.40 (-11.78%)</td><td>319.90 <b>(-20.52%)</b></td><td>252.90 (+8.68%)</td><td>85.73 (-7.95%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>477.30 (n/a)</td><td>389.24 (n/a)</td><td>402.50 (n/a)</td><td>232.70 (n/a)</td><td>93.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (-2.62%)</td><td>0.15 (-7.08%)</td><td>0.13 (-8.12%)</td><td>0.12 (-7.15%)</td><td>0.04 (-1.28%)</td><td>540.40 (+7.71%)</td><td>448.64 (+7.80%)</td><td>496.10 (+8.84%)</td><td>284.20 (+2.71%)</td><td>102.36 (+4.81%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>501.70 (n/a)</td><td>416.16 (n/a)</td><td>455.80 (n/a)</td><td>276.70 (n/a)</td><td>97.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.29 (-19.16%)</td><td>0.19 (-10.27%)</td><td>0.15 <b>(-26.80%)</b></td><td>0.12 (-8.58%)</td><td>0.08 (-11.46%)</td><td>535.50 (+9.37%)</td><td>381.56 (+12.03%)</td><td>425.80 <b>(+36.61%)</b></td><td>228.10 <b>(+23.70%)</b></td><td>137.89 (+14.25%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>489.60 (n/a)</td><td>340.60 (n/a)</td><td>311.70 (n/a)</td><td>184.40 (n/a)</td><td>120.69 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.43 (-18.95%)</td><td>0.26 <b>(-27.95%)</b></td><td>0.21 <b>(-50.22%)</b></td><td>0.20 (-5.46%)</td><td>0.10 <b>(-29.14%)</b></td><td>667.60 (+5.77%)</td><td>543.46 <b>(+32.27%)</b></td><td>632.50 <b>(+100.86%)</b></td><td>304.50 <b>(+23.38%)</b></td><td>161.61 (-8.82%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.53 (n/a)</td><td>0.37 (n/a)</td><td>0.42 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>631.20 (n/a)</td><td>410.88 (n/a)</td><td>314.90 (n/a)</td><td>246.80 (n/a)</td><td>177.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.30 <b>(-42.46%)</b></td><td>0.27 <b>(-30.53%)</b></td><td>0.27 <b>(-37.18%)</b></td><td>0.24 (+4.54%)</td><td>0.02 <b>(-79.98%)</b></td><td>549.00 (-4.36%)</td><td>494.98 <b>(+31.64%)</b></td><td>487.10 <b>(+59.18%)</b></td><td>434.00 <b>(+73.81%)</b></td><td>44.91 <b>(-67.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>574.00 (n/a)</td><td>376.02 (n/a)</td><td>306.00 (n/a)</td><td>249.70 (n/a)</td><td>136.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.52 (+4.64%)</td><td>0.34 (-4.36%)</td><td>0.25 <b>(-30.87%)</b></td><td>0.22 (-9.07%)</td><td>0.14 <b>(+22.37%)</b></td><td>607.60 (+9.97%)</td><td>439.46 (+8.59%)</td><td>519.00 <b>(+44.65%)</b></td><td>253.30 (-4.45%)</td><td>159.61 (+18.54%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>552.50 (n/a)</td><td>404.68 (n/a)</td><td>358.80 (n/a)</td><td>265.10 (n/a)</td><td>134.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (-18.93%)</td><td>0.05 (+19.71%)</td><td>0.06 <b>(+45.39%)</b></td><td>0.03 <b>(+47.67%)</b></td><td>0.01 <b>(-39.12%)</b></td><td>477.10 <b>(-32.28%)</b></td><td>353.96 <b>(-23.35%)</b></td><td>297.30 <b>(-31.21%)</b></td><td>283.20 <b>(+23.40%)</b></td><td>90.18 <b>(-47.65%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:02:17</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>704.50 (n/a)</td><td>461.80 (n/a)</td><td>432.20 (n/a)</td><td>229.50 (n/a)</td><td>172.26 (n/a)</td>
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
