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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-7.71%)</td><td>0.02 (-17.62%)</td><td>0.02 (-11.60%)</td><td>0.01 (-6.55%)</td><td>0.01 (+12.12%)</td><td>653.10 (+7.00%)</td><td>422.90 <b>(+28.63%)</b></td><td>308.00 (+13.15%)</td><td>232.80 (+8.33%)</td><td>209.16 <b>(+30.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.40 (n/a)</td><td>328.76 (n/a)</td><td>272.20 (n/a)</td><td>214.90 (n/a)</td><td>160.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-19.25%)</td><td>0.02 (-16.20%)</td><td>0.02 (-18.08%)</td><td>0.01 (+7.00%)</td><td>0.00 <b>(-39.19%)</b></td><td>513.70 (-6.55%)</td><td>409.06 (+13.70%)</td><td>382.50 <b>(+22.05%)</b></td><td>299.10 <b>(+23.80%)</b></td><td>90.60 <b>(-28.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.70 (n/a)</td><td>359.78 (n/a)</td><td>313.40 (n/a)</td><td>241.60 (n/a)</td><td>125.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-5.23%)</td><td>0.02 (+6.74%)</td><td>0.02 <b>(+58.78%)</b></td><td>0.01 <b>(-20.24%)</b></td><td>0.01 (-4.50%)</td><td>589.50 <b>(+25.37%)</b></td><td>349.30 (-4.69%)</td><td>273.80 <b>(-37.01%)</b></td><td>228.30 (+5.55%)</td><td>146.74 <b>(+26.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>470.20 (n/a)</td><td>366.48 (n/a)</td><td>434.70 (n/a)</td><td>216.30 (n/a)</td><td>115.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-14.84%)</td><td>0.01 <b>(-40.12%)</b></td><td>0.01 <b>(-46.36%)</b></td><td>0.00 <b>(-78.97%)</b></td><td>0.01 <b>(+21.44%)</b></td><td>2423.10 <b>(+375.58%)</b></td><td>821.24 <b>(+167.98%)</b></td><td>465.90 <b>(+86.43%)</b></td><td>253.20 (+17.44%)</td><td>901.54 <b>(+657.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>509.50 (n/a)</td><td>306.46 (n/a)</td><td>249.90 (n/a)</td><td>215.60 (n/a)</td><td>118.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+26.14%)</b></td><td>0.02 (-0.89%)</td><td>0.02 (-4.51%)</td><td>0.01 (-6.05%)</td><td>0.01 <b>(+63.75%)</b></td><td>660.50 (+6.43%)</td><td>385.60 (+14.00%)</td><td>290.90 (+4.72%)</td><td>183.60 <b>(-20.69%)</b></td><td>212.81 <b>(+33.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>338.26 (n/a)</td><td>277.80 (n/a)</td><td>231.50 (n/a)</td><td>159.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 <b>(+49.92%)</b></td><td>0.02 (-5.59%)</td><td>0.01 <b>(-38.48%)</b></td><td>0.01 <b>(-39.51%)</b></td><td>0.01 <b>(+82.25%)</b></td><td>1098.90 <b>(+65.32%)</b></td><td>549.30 <b>(+33.30%)</b></td><td>490.00 <b>(+62.52%)</b></td><td>149.00 <b>(-33.27%)</b></td><td>343.29 <b>(+75.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.70 (n/a)</td><td>412.08 (n/a)</td><td>301.50 (n/a)</td><td>223.30 (n/a)</td><td>196.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-14.98%)</td><td>0.04 (+10.01%)</td><td>0.05 <b>(+26.81%)</b></td><td>0.03 <b>(+38.66%)</b></td><td>0.01 <b>(-51.91%)</b></td><td>402.20 <b>(-27.88%)</b></td><td>287.78 <b>(-20.46%)</b></td><td>254.70 <b>(-21.15%)</b></td><td>239.60 (+17.62%)</td><td>67.71 <b>(-58.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>557.70 (n/a)</td><td>361.82 (n/a)</td><td>323.00 (n/a)</td><td>203.70 (n/a)</td><td>163.88 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (+1.52%)</td><td>0.05 (+15.61%)</td><td>0.05 <b>(+45.94%)</b></td><td>0.02 <b>(-23.14%)</b></td><td>0.02 (+9.47%)</td><td>622.40 <b>(+30.10%)</b></td><td>309.68 (-8.07%)</td><td>229.70 <b>(-31.49%)</b></td><td>210.00 (-1.50%)</td><td>176.35 <b>(+49.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.40 (n/a)</td><td>336.88 (n/a)</td><td>335.30 (n/a)</td><td>213.20 (n/a)</td><td>117.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-6.32%)</td><td>0.04 (+3.51%)</td><td>0.05 (-13.58%)</td><td>0.02 <b>(+372.06%)</b></td><td>0.01 <b>(-44.60%)</b></td><td>516.80 <b>(-78.82%)</b></td><td>337.72 <b>(-54.04%)</b></td><td>267.00 (+15.73%)</td><td>224.50 (+6.75%)</td><td>129.03 <b>(-86.64%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2439.60 (n/a)</td><td>734.88 (n/a)</td><td>230.70 (n/a)</td><td>210.30 (n/a)</td><td>965.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-10.96%)</td><td>0.04 <b>(+36.10%)</b></td><td>0.05 <b>(+88.09%)</b></td><td>0.02 <b>(+208.83%)</b></td><td>0.02 <b>(-23.19%)</b></td><td>603.00 <b>(-67.62%)</b></td><td>361.84 <b>(-49.02%)</b></td><td>260.00 <b>(-46.84%)</b></td><td>234.00 (+12.28%)</td><td>167.22 <b>(-74.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1862.30 (n/a)</td><td>709.80 (n/a)</td><td>489.10 (n/a)</td><td>208.40 (n/a)</td><td>663.83 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (+18.16%)</td><td>0.03 (-5.35%)</td><td>0.03 <b>(-26.10%)</b></td><td>0.02 (+0.18%)</td><td>0.01 (+17.27%)</td><td>620.70 (-0.18%)</td><td>447.04 (+6.06%)</td><td>490.00 <b>(+35.32%)</b></td><td>225.30 (-15.36%)</td><td>145.79 (-9.37%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>621.80 (n/a)</td><td>421.50 (n/a)</td><td>362.10 (n/a)</td><td>266.20 (n/a)</td><td>160.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-10.41%)</td><td>0.03 (-10.64%)</td><td>0.04 (+5.86%)</td><td>0.00 <b>(-74.89%)</b></td><td>0.02 (+13.98%)</td><td>2475.80 <b>(+298.29%)</b></td><td>753.02 <b>(+94.15%)</b></td><td>278.50 (-5.53%)</td><td>243.20 (+11.61%)</td><td>968.99 <b>(+405.02%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>621.60 (n/a)</td><td>387.86 (n/a)</td><td>294.80 (n/a)</td><td>217.90 (n/a)</td><td>191.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (-10.45%)</td><td>0.07 (-13.53%)</td><td>0.08 (-0.19%)</td><td>0.04 <b>(-37.16%)</b></td><td>0.02 <b>(+62.82%)</b></td><td>625.30 <b>(+59.15%)</b></td><td>393.80 <b>(+26.58%)</b></td><td>299.00 (+0.20%)</td><td>270.50 (+11.68%)</td><td>160.54 <b>(+177.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>392.90 (n/a)</td><td>311.10 (n/a)</td><td>298.40 (n/a)</td><td>242.20 (n/a)</td><td>57.83 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 <b>(-25.95%)</b></td><td>0.08 (-16.04%)</td><td>0.09 (-8.35%)</td><td>0.04 (-15.15%)</td><td>0.03 (-19.52%)</td><td>607.20 (+17.86%)</td><td>355.34 (+19.11%)</td><td>271.70 (+9.12%)</td><td>242.00 <b>(+35.04%)</b></td><td>154.18 (+19.88%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>515.20 (n/a)</td><td>298.34 (n/a)</td><td>249.00 (n/a)</td><td>179.20 (n/a)</td><td>128.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (-11.08%)</td><td>0.06 (-10.66%)</td><td>0.06 <b>(-21.57%)</b></td><td>0.05 <b>(+35.59%)</b></td><td>0.01 <b>(-42.57%)</b></td><td>510.20 <b>(-26.25%)</b></td><td>409.36 (+3.99%)</td><td>404.00 <b>(+27.49%)</b></td><td>328.50 (+12.46%)</td><td>75.60 <b>(-55.07%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>691.80 (n/a)</td><td>393.64 (n/a)</td><td>316.90 (n/a)</td><td>292.10 (n/a)</td><td>168.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (+5.14%)</td><td>0.06 (-17.20%)</td><td>0.05 <b>(-40.74%)</b></td><td>0.04 (-0.76%)</td><td>0.02 (-5.51%)</td><td>572.50 (+0.77%)</td><td>448.60 (+17.47%)</td><td>481.70 <b>(+68.72%)</b></td><td>236.70 (-4.86%)</td><td>128.17 (-17.77%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>568.10 (n/a)</td><td>381.90 (n/a)</td><td>285.50 (n/a)</td><td>248.80 (n/a)</td><td>155.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (+4.50%)</td><td>0.08 (+17.06%)</td><td>0.09 <b>(+37.78%)</b></td><td>0.05 (+11.48%)</td><td>0.02 (-11.14%)</td><td>508.70 (-10.30%)</td><td>321.56 (-16.53%)</td><td>281.60 <b>(-27.44%)</b></td><td>237.30 (-4.31%)</td><td>108.09 (-17.04%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.10 (n/a)</td><td>385.26 (n/a)</td><td>388.10 (n/a)</td><td>248.00 (n/a)</td><td>130.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 <b>(+38.84%)</b></td><td>0.07 (+17.98%)</td><td>0.06 (-4.86%)</td><td>0.03 <b>(+131.46%)</b></td><td>0.04 <b>(+29.93%)</b></td><td>782.80 <b>(-56.80%)</b></td><td>452.24 <b>(-32.16%)</b></td><td>439.60 (+5.09%)</td><td>192.20 <b>(-27.99%)</b></td><td>215.16 <b>(-66.59%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1811.90 (n/a)</td><td>666.64 (n/a)</td><td>418.30 (n/a)</td><td>266.90 (n/a)</td><td>643.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.19 (-13.30%)</td><td>0.16 (+3.43%)</td><td>0.17 (-13.41%)</td><td>0.13 <b>(+42.51%)</b></td><td>0.02 <b>(-63.05%)</b></td><td>383.10 <b>(-29.84%)</b></td><td>303.52 (-15.82%)</td><td>289.00 (+15.51%)</td><td>262.20 (+15.35%)</td><td>48.21 <b>(-70.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>546.00 (n/a)</td><td>360.54 (n/a)</td><td>250.20 (n/a)</td><td>227.30 (n/a)</td><td>165.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (-14.17%)</td><td>0.13 <b>(-27.27%)</b></td><td>0.12 <b>(-40.49%)</b></td><td>0.08 <b>(-20.12%)</b></td><td>0.04 (-5.65%)</td><td>611.40 <b>(+25.21%)</b></td><td>423.16 <b>(+39.61%)</b></td><td>422.80 <b>(+68.04%)</b></td><td>280.90 (+16.51%)</td><td>138.40 <b>(+31.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>488.30 (n/a)</td><td>303.10 (n/a)</td><td>251.60 (n/a)</td><td>241.10 (n/a)</td><td>105.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.23 (-5.43%)</td><td>0.12 <b>(-37.45%)</b></td><td>0.09 <b>(-53.24%)</b></td><td>0.09 <b>(-40.15%)</b></td><td>0.06 <b>(+79.68%)</b></td><td>554.00 <b>(+67.07%)</b></td><td>452.28 <b>(+77.69%)</b></td><td>534.70 <b>(+113.88%)</b></td><td>215.10 (+5.70%)</td><td>145.97 <b>(+209.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>331.60 (n/a)</td><td>254.54 (n/a)</td><td>250.00 (n/a)</td><td>203.50 (n/a)</td><td>47.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (-15.23%)</td><td>0.13 <b>(-34.90%)</b></td><td>0.10 <b>(-47.51%)</b></td><td>0.08 <b>(-55.82%)</b></td><td>0.05 <b>(+229.23%)</b></td><td>635.90 <b>(+126.38%)</b></td><td>429.64 <b>(+71.79%)</b></td><td>474.00 <b>(+90.51%)</b></td><td>268.00 (+17.96%)</td><td>157.46 <b>(+703.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>280.90 (n/a)</td><td>250.10 (n/a)</td><td>248.80 (n/a)</td><td>227.20 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 <b>(-31.36%)</b></td><td>0.09 (-16.89%)</td><td>0.08 (-19.68%)</td><td>0.07 (-5.23%)</td><td>0.03 <b>(-41.28%)</b></td><td>696.90 (+5.51%)</td><td>559.48 (+14.42%)</td><td>651.10 <b>(+24.49%)</b></td><td>353.30 <b>(+45.69%)</b></td><td>155.56 (-4.00%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>660.50 (n/a)</td><td>488.96 (n/a)</td><td>523.00 (n/a)</td><td>242.50 (n/a)</td><td>162.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 <b>(-26.38%)</b></td><td>0.11 <b>(-38.59%)</b></td><td>0.11 <b>(-46.09%)</b></td><td>0.08 <b>(-37.87%)</b></td><td>0.03 (-18.16%)</td><td>641.30 <b>(+60.97%)</b></td><td>473.80 <b>(+65.16%)</b></td><td>466.90 <b>(+85.50%)</b></td><td>321.80 <b>(+35.84%)</b></td><td>116.60 <b>(+74.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>398.40 (n/a)</td><td>286.88 (n/a)</td><td>251.70 (n/a)</td><td>236.90 (n/a)</td><td>66.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (+10.72%)</td><td>0.01 (-8.52%)</td><td>0.01 (-6.55%)</td><td>0.01 (-11.89%)</td><td>0.00 <b>(+37.38%)</b></td><td>511.60 (+13.51%)</td><td>353.64 (+15.37%)</td><td>315.30 (+7.03%)</td><td>194.70 (-9.69%)</td><td>128.04 <b>(+41.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.70 (n/a)</td><td>306.52 (n/a)</td><td>294.60 (n/a)</td><td>215.60 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 <b>(+22.95%)</b></td><td>0.01 (-9.52%)</td><td>0.01 (-18.68%)</td><td>0.00 (-12.78%)</td><td>0.00 <b>(+41.48%)</b></td><td>738.90 (+14.65%)</td><td>504.42 (+17.01%)</td><td>514.50 <b>(+22.97%)</b></td><td>230.90 (-18.64%)</td><td>180.59 <b>(+22.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>644.50 (n/a)</td><td>431.08 (n/a)</td><td>418.40 (n/a)</td><td>283.80 (n/a)</td><td>147.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-4.26%)</td><td>0.01 (-9.99%)</td><td>0.01 (-13.91%)</td><td>0.01 <b>(+32.35%)</b></td><td>0.00 <b>(-24.74%)</b></td><td>492.60 <b>(-24.45%)</b></td><td>349.92 (+2.74%)</td><td>315.50 (+16.16%)</td><td>243.30 (+4.47%)</td><td>102.66 <b>(-41.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>652.00 (n/a)</td><td>340.58 (n/a)</td><td>271.60 (n/a)</td><td>232.90 (n/a)</td><td>176.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-0.63%)</td><td>0.01 (+10.95%)</td><td>0.01 (+0.94%)</td><td>0.01 <b>(+50.17%)</b></td><td>0.00 <b>(-24.78%)</b></td><td>438.70 <b>(-33.41%)</b></td><td>347.08 (-15.98%)</td><td>327.70 (-0.94%)</td><td>252.60 (+0.64%)</td><td>84.86 <b>(-48.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>658.80 (n/a)</td><td>413.10 (n/a)</td><td>330.80 (n/a)</td><td>251.00 (n/a)</td><td>166.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-5.96%)</td><td>0.01 (-11.24%)</td><td>0.01 (+0.39%)</td><td>0.00 <b>(-50.96%)</b></td><td>0.00 <b>(+52.94%)</b></td><td>1051.30 <b>(+103.94%)</b></td><td>565.36 <b>(+26.88%)</b></td><td>461.70 (-0.39%)</td><td>335.80 (+6.33%)</td><td>282.37 <b>(+272.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.50 (n/a)</td><td>445.58 (n/a)</td><td>463.50 (n/a)</td><td>315.80 (n/a)</td><td>75.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (+3.57%)</td><td>0.01 (+19.62%)</td><td>0.01 <b>(+42.54%)</b></td><td>0.00 <b>(+23.05%)</b></td><td>0.00 (-0.34%)</td><td>559.70 (-18.73%)</td><td>382.16 (-17.43%)</td><td>314.90 <b>(-29.85%)</b></td><td>232.00 (-3.45%)</td><td>138.26 (-14.06%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>688.70 (n/a)</td><td>462.82 (n/a)</td><td>448.90 (n/a)</td><td>240.30 (n/a)</td><td>160.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+12.47%)</td><td>0.02 <b>(+20.43%)</b></td><td>0.02 (+13.54%)</td><td>0.01 (+14.22%)</td><td>0.01 (-10.75%)</td><td>518.80 (-12.45%)</td><td>309.22 <b>(-20.75%)</b></td><td>260.60 (-11.90%)</td><td>219.70 (-11.09%)</td><td>119.73 <b>(-27.53%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.60 (n/a)</td><td>390.16 (n/a)</td><td>295.80 (n/a)</td><td>247.10 (n/a)</td><td>165.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-16.45%)</td><td>0.01 (-15.74%)</td><td>0.01 <b>(-47.40%)</b></td><td>0.01 <b>(+219.69%)</b></td><td>0.01 <b>(-42.50%)</b></td><td>567.60 <b>(-68.72%)</b></td><td>405.66 <b>(-30.69%)</b></td><td>454.60 <b>(+90.13%)</b></td><td>239.30 (+19.65%)</td><td>139.00 <b>(-79.96%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1814.50 (n/a)</td><td>585.30 (n/a)</td><td>239.10 (n/a)</td><td>200.00 (n/a)</td><td>693.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (+4.19%)</td><td>0.02 (-6.30%)</td><td>0.02 (+3.13%)</td><td>0.00 <b>(-48.38%)</b></td><td>0.01 <b>(+29.07%)</b></td><td>1072.20 <b>(+93.71%)</b></td><td>464.94 <b>(+34.87%)</b></td><td>249.80 (-3.03%)</td><td>200.70 (-4.02%)</td><td>368.29 <b>(+135.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.50 (n/a)</td><td>344.74 (n/a)</td><td>257.60 (n/a)</td><td>209.10 (n/a)</td><td>156.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+6.00%)</td><td>0.02 (-10.01%)</td><td>0.01 <b>(-24.26%)</b></td><td>0.01 <b>(-32.94%)</b></td><td>0.01 <b>(+39.40%)</b></td><td>795.70 <b>(+49.12%)</b></td><td>420.68 <b>(+24.17%)</b></td><td>406.80 <b>(+32.04%)</b></td><td>225.60 (-5.65%)</td><td>225.54 <b>(+92.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.60 (n/a)</td><td>338.78 (n/a)</td><td>308.10 (n/a)</td><td>239.10 (n/a)</td><td>117.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-13.42%)</td><td>0.01 (-7.77%)</td><td>0.01 (-8.69%)</td><td>0.01 (-6.00%)</td><td>0.01 (-12.82%)</td><td>612.30 (+6.38%)</td><td>429.38 (+7.39%)</td><td>370.50 (+9.52%)</td><td>265.60 (+15.53%)</td><td>166.92 (+4.55%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>399.82 (n/a)</td><td>338.30 (n/a)</td><td>229.90 (n/a)</td><td>159.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-8.17%)</td><td>0.01 (+19.09%)</td><td>0.01 <b>(+50.07%)</b></td><td>0.01 <b>(+49.20%)</b></td><td>0.00 <b>(-39.70%)</b></td><td>491.30 <b>(-32.98%)</b></td><td>402.74 <b>(-21.54%)</b></td><td>361.80 <b>(-33.36%)</b></td><td>323.30 (+8.89%)</td><td>78.12 <b>(-53.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>733.10 (n/a)</td><td>513.28 (n/a)</td><td>542.90 (n/a)</td><td>296.90 (n/a)</td><td>167.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (+18.27%)</td><td>0.04 (+18.77%)</td><td>0.04 (+15.21%)</td><td>0.02 (+11.46%)</td><td>0.01 (+10.12%)</td><td>544.80 (-10.29%)</td><td>312.96 (-15.92%)</td><td>271.90 (-13.19%)</td><td>207.20 (-15.43%)</td><td>132.55 (-9.95%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.30 (n/a)</td><td>372.20 (n/a)</td><td>313.20 (n/a)</td><td>245.00 (n/a)</td><td>147.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-13.56%)</td><td>0.03 (-2.35%)</td><td>0.03 <b>(+48.35%)</b></td><td>0.00 <b>(-80.97%)</b></td><td>0.02 (+17.61%)</td><td>2470.60 <b>(+425.44%)</b></td><td>716.60 <b>(+93.96%)</b></td><td>311.70 <b>(-32.59%)</b></td><td>240.00 (+15.72%)</td><td>981.13 <b>(+641.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.20 (n/a)</td><td>369.46 (n/a)</td><td>462.40 (n/a)</td><td>207.40 (n/a)</td><td>132.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 <b>(+38.02%)</b></td><td>0.03 <b>(+22.56%)</b></td><td>0.04 <b>(+66.62%)</b></td><td>0.01 <b>(-40.79%)</b></td><td>0.02 <b>(+77.35%)</b></td><td>1055.50 <b>(+68.91%)</b></td><td>448.52 (+4.94%)</td><td>272.40 <b>(-40.00%)</b></td><td>188.80 <b>(-27.55%)</b></td><td>354.59 <b>(+138.23%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.90 (n/a)</td><td>427.42 (n/a)</td><td>454.00 (n/a)</td><td>260.60 (n/a)</td><td>148.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-12.67%)</td><td>0.02 (-8.02%)</td><td>0.02 (-0.93%)</td><td>0.02 (-6.86%)</td><td>0.01 (-17.40%)</td><td>588.70 (+7.35%)</td><td>457.52 (+7.44%)</td><td>455.70 (+0.93%)</td><td>265.20 (+14.51%)</td><td>126.00 (+4.95%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.40 (n/a)</td><td>425.82 (n/a)</td><td>451.50 (n/a)</td><td>231.60 (n/a)</td><td>120.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-2.93%)</td><td>0.03 <b>(+22.25%)</b></td><td>0.03 <b>(+47.78%)</b></td><td>0.02 (+7.63%)</td><td>0.01 (+1.15%)</td><td>545.40 (-7.09%)</td><td>383.50 (-18.06%)</td><td>337.00 <b>(-32.33%)</b></td><td>270.80 (+3.00%)</td><td>125.94 (+0.28%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>468.00 (n/a)</td><td>498.00 (n/a)</td><td>262.90 (n/a)</td><td>125.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-9.60%)</td><td>0.03 (-1.00%)</td><td>0.02 (+3.69%)</td><td>0.02 (-9.03%)</td><td>0.01 (-8.88%)</td><td>632.20 (+9.93%)</td><td>429.12 (+0.49%)</td><td>474.80 (-3.55%)</td><td>260.20 (+10.63%)</td><td>154.05 (+5.13%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>427.04 (n/a)</td><td>492.30 (n/a)</td><td>235.20 (n/a)</td><td>146.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 <b>(+21.83%)</b></td><td>0.06 (+14.44%)</td><td>0.05 (+8.86%)</td><td>0.03 (+4.02%)</td><td>0.03 (+19.44%)</td><td>645.00 (-3.86%)</td><td>404.98 (-12.52%)</td><td>387.40 (-8.13%)</td><td>204.00 (-17.91%)</td><td>168.72 (-12.60%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>670.90 (n/a)</td><td>462.92 (n/a)</td><td>421.70 (n/a)</td><td>248.50 (n/a)</td><td>193.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 <b>(+33.62%)</b></td><td>0.06 (-6.66%)</td><td>0.05 <b>(-35.42%)</b></td><td>0.03 (-18.27%)</td><td>0.03 <b>(+63.19%)</b></td><td>608.40 <b>(+22.34%)</b></td><td>427.70 (+14.85%)</td><td>464.70 <b>(+54.85%)</b></td><td>200.40 <b>(-25.17%)</b></td><td>150.05 <b>(+31.04%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.30 (n/a)</td><td>372.40 (n/a)</td><td>300.10 (n/a)</td><td>267.80 (n/a)</td><td>114.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (-14.44%)</td><td>0.06 (+0.23%)</td><td>0.05 (+17.30%)</td><td>0.04 (-5.79%)</td><td>0.02 <b>(-28.02%)</b></td><td>596.00 (+6.16%)</td><td>390.92 (-5.26%)</td><td>396.50 (-14.75%)</td><td>270.40 (+16.90%)</td><td>132.13 (-14.71%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>561.40 (n/a)</td><td>412.64 (n/a)</td><td>465.10 (n/a)</td><td>231.30 (n/a)</td><td>154.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (+7.36%)</td><td>0.05 (+5.80%)</td><td>0.04 (+5.10%)</td><td>0.04 (+9.80%)</td><td>0.03 (+8.34%)</td><td>536.70 (-8.93%)</td><td>448.88 (-5.21%)</td><td>520.50 (-4.84%)</td><td>189.30 (-6.84%)</td><td>146.79 (-6.80%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>589.30 (n/a)</td><td>473.56 (n/a)</td><td>547.00 (n/a)</td><td>203.20 (n/a)</td><td>157.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(-29.39%)</b></td><td>0.05 (-0.37%)</td><td>0.05 <b>(+27.33%)</b></td><td>0.04 (+14.92%)</td><td>0.01 <b>(-49.92%)</b></td><td>557.20 (-12.99%)</td><td>445.42 (-9.72%)</td><td>452.40 <b>(-21.46%)</b></td><td>300.90 <b>(+41.60%)</b></td><td>115.12 <b>(-33.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>640.40 (n/a)</td><td>493.40 (n/a)</td><td>576.00 (n/a)</td><td>212.50 (n/a)</td><td>173.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (+13.78%)</td><td>0.06 (-6.02%)</td><td>0.05 (-15.55%)</td><td>0.04 <b>(-26.83%)</b></td><td>0.02 <b>(+137.72%)</b></td><td>594.00 <b>(+36.65%)</b></td><td>428.52 (+17.61%)</td><td>433.20 (+18.43%)</td><td>258.00 (-12.10%)</td><td>156.81 <b>(+188.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>434.70 (n/a)</td><td>364.36 (n/a)</td><td>365.80 (n/a)</td><td>293.50 (n/a)</td><td>54.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>521.60 (n/a)</td><td>387.98 (n/a)</td><td>445.50 (n/a)</td><td>231.80 (n/a)</td><td>142.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.90 (n/a)</td><td>470.76 (n/a)</td><td>508.90 (n/a)</td><td>251.20 (n/a)</td><td>124.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>696.70 (n/a)</td><td>456.90 (n/a)</td><td>510.40 (n/a)</td><td>271.80 (n/a)</td><td>175.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>755.50 (n/a)</td><td>459.58 (n/a)</td><td>438.00 (n/a)</td><td>295.90 (n/a)</td><td>183.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>560.50 (n/a)</td><td>494.08 (n/a)</td><td>516.50 (n/a)</td><td>423.50 (n/a)</td><td>63.88 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1000.20 (n/a)</td><td>602.14 (n/a)</td><td>538.40 (n/a)</td><td>442.60 (n/a)</td><td>228.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>570.30 (n/a)</td><td>400.58 (n/a)</td><td>437.40 (n/a)</td><td>227.70 (n/a)</td><td>131.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>682.60 (n/a)</td><td>496.92 (n/a)</td><td>500.70 (n/a)</td><td>274.20 (n/a)</td><td>147.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>482.40 (n/a)</td><td>365.66 (n/a)</td><td>337.10 (n/a)</td><td>264.60 (n/a)</td><td>107.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (-10.37%)</td><td>0.14 <b>(-20.96%)</b></td><td>0.16 (-14.83%)</td><td>0.07 <b>(-32.35%)</b></td><td>0.05 <b>(+23.30%)</b></td><td>705.50 <b>(+47.81%)</b></td><td>414.60 <b>(+36.10%)</b></td><td>305.50 (+17.41%)</td><td>278.20 (+11.55%)</td><td>185.35 <b>(+90.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>477.30 (n/a)</td><td>304.62 (n/a)</td><td>260.20 (n/a)</td><td>249.40 (n/a)</td><td>97.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>536.00 (n/a)</td><td>385.98 (n/a)</td><td>305.30 (n/a)</td><td>281.70 (n/a)</td><td>123.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>602.90 (n/a)</td><td>510.00 (n/a)</td><td>550.10 (n/a)</td><td>359.60 (n/a)</td><td>94.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>456.80 (n/a)</td><td>376.28 (n/a)</td><td>406.10 (n/a)</td><td>229.70 (n/a)</td><td>90.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>301.80 (n/a)</td><td>266.30 (n/a)</td><td>233.60 (n/a)</td><td>97.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>497.30 (n/a)</td><td>335.50 (n/a)</td><td>343.00 (n/a)</td><td>205.00 (n/a)</td><td>113.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>611.40 (n/a)</td><td>345.98 (n/a)</td><td>273.60 (n/a)</td><td>205.70 (n/a)</td><td>165.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.80 (n/a)</td><td>408.06 (n/a)</td><td>446.00 (n/a)</td><td>250.60 (n/a)</td><td>151.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>723.70 (n/a)</td><td>472.88 (n/a)</td><td>452.90 (n/a)</td><td>264.80 (n/a)</td><td>183.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>612.50 (n/a)</td><td>375.44 (n/a)</td><td>261.70 (n/a)</td><td>208.90 (n/a)</td><td>183.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>531.70 (n/a)</td><td>449.74 (n/a)</td><td>463.20 (n/a)</td><td>323.30 (n/a)</td><td>83.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>709.00 (n/a)</td><td>361.78 (n/a)</td><td>249.70 (n/a)</td><td>207.70 (n/a)</td><td>213.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>589.30 (n/a)</td><td>423.50 (n/a)</td><td>412.30 (n/a)</td><td>270.70 (n/a)</td><td>128.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>608.50 (n/a)</td><td>412.50 (n/a)</td><td>373.70 (n/a)</td><td>289.90 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.47 (-2.44%)</td><td>3.15 (+4.06%)</td><td>3.32 (-0.48%)</td><td>2.69 (+14.47%)</td><td>0.36 <b>(-33.67%)</b></td><td>3900.00 (-12.64%)</td><td>3368.96 (-5.52%)</td><td>3155.30 (+0.48%)</td><td>3024.90 (+2.50%)</td><td>404.24 <b>(-41.18%)</b></td><td>1419.87 (-2.44%)</td><td>1289.04 (+4.06%)</td><td>1361.19 (-0.48%)</td><td>1101.28 (+14.47%)</td><td>147.84 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.55 (n/a)</td><td>3.02 (n/a)</td><td>3.34 (n/a)</td><td>2.35 (n/a)</td><td>0.54 (n/a)</td><td>4464.30 (n/a)</td><td>3565.86 (n/a)</td><td>3140.10 (n/a)</td><td>2951.10 (n/a)</td><td>687.24 (n/a)</td><td>1455.37 (n/a)</td><td>1238.75 (n/a)</td><td>1367.77 (n/a)</td><td>962.07 (n/a)</td><td>222.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.35 (-5.87%)</td><td>3.02 (-8.45%)</td><td>2.97 (-13.66%)</td><td>2.83 (-4.16%)</td><td>0.19 <b>(-33.04%)</b></td><td>8334.60 (+4.34%)</td><td>7846.62 (+8.88%)</td><td>7951.00 (+15.82%)</td><td>7050.60 (+6.23%)</td><td>477.73 <b>(-27.07%)</b></td><td>1903.64 (-5.87%)</td><td>1715.90 (-8.45%)</td><td>1688.06 (-13.66%)</td><td>1610.36 (-4.16%)</td><td>110.75 <b>(-33.04%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.55 (n/a)</td><td>3.29 (n/a)</td><td>3.44 (n/a)</td><td>2.95 (n/a)</td><td>0.29 (n/a)</td><td>7988.10 (n/a)</td><td>7206.94 (n/a)</td><td>6865.10 (n/a)</td><td>6637.00 (n/a)</td><td>655.04 (n/a)</td><td>2022.26 (n/a)</td><td>1874.36 (n/a)</td><td>1955.07 (n/a)</td><td>1680.22 (n/a)</td><td>165.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.87 (-6.64%)</td><td>3.22 (-11.23%)</td><td>3.40 (-7.89%)</td><td>2.65 (-6.74%)</td><td>0.51 (+5.99%)</td><td>6328.90 (+7.23%)</td><td>5314.88 (+13.15%)</td><td>4931.80 (+8.57%)</td><td>4339.40 (+7.11%)</td><td>852.53 <b>(+20.68%)</b></td><td>1979.53 (-6.64%)</td><td>1649.49 (-11.23%)</td><td>1741.76 (-7.89%)</td><td>1357.26 (-6.74%)</td><td>260.50 (+5.99%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.14 (n/a)</td><td>3.63 (n/a)</td><td>3.69 (n/a)</td><td>2.84 (n/a)</td><td>0.48 (n/a)</td><td>5902.40 (n/a)</td><td>4697.04 (n/a)</td><td>4542.70 (n/a)</td><td>4051.40 (n/a)</td><td>706.46 (n/a)</td><td>2120.24 (n/a)</td><td>1858.21 (n/a)</td><td>1890.95 (n/a)</td><td>1455.34 (n/a)</td><td>245.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.08 (+9.64%)</td><td>0.88 (+8.84%)</td><td>0.89 (+10.93%)</td><td>0.75 <b>(+21.00%)</b></td><td>0.13 (-3.51%)</td><td>614.40 (-17.35%)</td><td>532.30 (-8.78%)</td><td>515.40 (-9.85%)</td><td>425.00 (-8.80%)</td><td>77.01 <b>(-26.93%)</b></td><td>78.96 (+9.64%)</td><td>64.16 (+8.84%)</td><td>65.10 (+10.93%)</td><td>54.61 <b>(+21.00%)</b></td><td>9.78 (-3.51%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.98 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.62 (n/a)</td><td>0.14 (n/a)</td><td>743.40 (n/a)</td><td>583.54 (n/a)</td><td>571.70 (n/a)</td><td>466.00 (n/a)</td><td>105.39 (n/a)</td><td>72.01 (n/a)</td><td>58.95 (n/a)</td><td>58.69 (n/a)</td><td>45.14 (n/a)</td><td>10.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.52 <b>(-25.23%)</b></td><td>1.19 (+9.60%)</td><td>1.08 <b>(+22.60%)</b></td><td>0.74 <b>(+85.26%)</b></td><td>0.33 <b>(-53.75%)</b></td><td>886.40 <b>(-46.02%)</b></td><td>593.46 <b>(-34.11%)</b></td><td>604.00 (-18.43%)</td><td>431.40 <b>(+33.73%)</b></td><td>186.16 <b>(-68.54%)</b></td><td>155.55 <b>(-25.23%)</b></td><td>121.41 (+9.60%)</td><td>111.10 <b>(+22.60%)</b></td><td>75.71 <b>(+85.26%)</b></td><td>34.11 <b>(-53.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.03 (n/a)</td><td>1.08 (n/a)</td><td>0.88 (n/a)</td><td>0.40 (n/a)</td><td>0.72 (n/a)</td><td>1642.20 (n/a)</td><td>900.66 (n/a)</td><td>740.50 (n/a)</td><td>322.60 (n/a)</td><td>591.68 (n/a)</td><td>208.05 (n/a)</td><td>110.78 (n/a)</td><td>90.62 (n/a)</td><td>40.87 (n/a)</td><td>73.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.89 (+4.81%)</td><td>0.97 <b>(-22.35%)</b></td><td>0.86 <b>(-37.71%)</b></td><td>0.21 (-0.00%)</td><td>0.60 (-1.02%)</td><td>3527.30 (+0.00%)</td><td>1284.80 (+15.52%)</td><td>872.50 <b>(+60.53%)</b></td><td>399.00 (-4.59%)</td><td>1269.09 (-6.09%)</td><td>210.26 (+4.81%)</td><td>107.74 <b>(-22.35%)</b></td><td>96.15 <b>(-37.71%)</b></td><td>23.78 (-0.00%)</td><td>66.95 (-1.02%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.80 (n/a)</td><td>1.25 (n/a)</td><td>1.39 (n/a)</td><td>0.21 (n/a)</td><td>0.61 (n/a)</td><td>3527.20 (n/a)</td><td>1112.18 (n/a)</td><td>543.50 (n/a)</td><td>418.20 (n/a)</td><td>1351.38 (n/a)</td><td>200.60 (n/a)</td><td>138.75 (n/a)</td><td>154.36 (n/a)</td><td>23.78 (n/a)</td><td>67.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.92 (+11.00%)</td><td>1.31 (+5.06%)</td><td>1.17 (+17.14%)</td><td>1.09 <b>(+22.52%)</b></td><td>0.35 (-11.74%)</td><td>957.90 (-18.38%)</td><td>835.88 (-7.78%)</td><td>893.80 (-14.63%)</td><td>545.20 (-9.91%)</td><td>165.02 <b>(-36.16%)</b></td><td>246.16 (+11.00%)</td><td>167.53 (+5.06%)</td><td>150.16 (+17.14%)</td><td>140.12 <b>(+22.52%)</b></td><td>44.19 (-11.74%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.73 (n/a)</td><td>1.25 (n/a)</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.39 (n/a)</td><td>1173.60 (n/a)</td><td>906.36 (n/a)</td><td>1047.00 (n/a)</td><td>605.20 (n/a)</td><td>258.49 (n/a)</td><td>221.77 (n/a)</td><td>159.45 (n/a)</td><td>128.19 (n/a)</td><td>114.36 (n/a)</td><td>50.07 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.22 (-16.45%)</td><td>1.43 (-13.00%)</td><td>1.35 (-5.47%)</td><td>1.06 (+1.04%)</td><td>0.47 <b>(-24.15%)</b></td><td>987.60 (-1.02%)</td><td>789.48 (+11.97%)</td><td>775.40 (+5.80%)</td><td>473.20 (+19.68%)</td><td>209.19 (-6.89%)</td><td>283.61 (-16.45%)</td><td>182.44 (-13.00%)</td><td>173.10 (-5.47%)</td><td>135.91 (+1.04%)</td><td>60.10 <b>(-24.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.65 (n/a)</td><td>1.64 (n/a)</td><td>1.43 (n/a)</td><td>1.05 (n/a)</td><td>0.62 (n/a)</td><td>997.80 (n/a)</td><td>705.08 (n/a)</td><td>732.90 (n/a)</td><td>395.40 (n/a)</td><td>224.68 (n/a)</td><td>339.45 (n/a)</td><td>209.71 (n/a)</td><td>183.12 (n/a)</td><td>134.51 (n/a)</td><td>79.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.22 (-7.54%)</td><td>1.55 <b>(-20.27%)</b></td><td>1.31 <b>(-40.34%)</b></td><td>1.10 (-19.74%)</td><td>0.46 (-4.26%)</td><td>957.30 <b>(+24.60%)</b></td><td>723.36 <b>(+26.66%)</b></td><td>799.90 <b>(+67.62%)</b></td><td>472.30 (+8.15%)</td><td>193.65 <b>(+25.62%)</b></td><td>284.16 (-7.54%)</td><td>197.86 <b>(-20.27%)</b></td><td>167.80 <b>(-40.34%)</b></td><td>140.21 (-19.74%)</td><td>58.51 (-4.26%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.40 (n/a)</td><td>1.94 (n/a)</td><td>2.20 (n/a)</td><td>1.36 (n/a)</td><td>0.48 (n/a)</td><td>768.30 (n/a)</td><td>571.12 (n/a)</td><td>477.20 (n/a)</td><td>436.70 (n/a)</td><td>154.16 (n/a)</td><td>307.32 (n/a)</td><td>248.17 (n/a)</td><td>281.28 (n/a)</td><td>174.70 (n/a)</td><td>61.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.06 (-2.63%)</td><td>1.22 (-16.61%)</td><td>0.98 <b>(-32.26%)</b></td><td>0.78 <b>(-20.70%)</b></td><td>0.50 (+19.82%)</td><td>1340.80 <b>(+26.11%)</b></td><td>961.16 <b>(+25.63%)</b></td><td>1068.20 <b>(+47.62%)</b></td><td>509.30 (+2.70%)</td><td>312.91 <b>(+49.60%)</b></td><td>263.52 (-2.63%)</td><td>155.76 (-16.61%)</td><td>125.65 <b>(-32.26%)</b></td><td>100.11 <b>(-20.70%)</b></td><td>64.41 (+19.82%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.11 (n/a)</td><td>1.46 (n/a)</td><td>1.45 (n/a)</td><td>0.99 (n/a)</td><td>0.42 (n/a)</td><td>1063.20 (n/a)</td><td>765.08 (n/a)</td><td>723.60 (n/a)</td><td>495.90 (n/a)</td><td>209.17 (n/a)</td><td>270.64 (n/a)</td><td>186.77 (n/a)</td><td>185.49 (n/a)</td><td>126.24 (n/a)</td><td>53.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.95 (+10.62%)</td><td>1.29 (+14.58%)</td><td>1.21 (-0.99%)</td><td>0.48 (+6.71%)</td><td>0.55 (-8.35%)</td><td>2188.40 (-6.28%)</td><td>1023.80 (-18.67%)</td><td>869.60 (+1.00%)</td><td>537.80 (-9.61%)</td><td>667.32 (-15.75%)</td><td>249.55 (+10.62%)</td><td>165.25 (+14.58%)</td><td>154.34 (-0.99%)</td><td>61.33 (+6.71%)</td><td>70.78 (-8.35%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.76 (n/a)</td><td>1.13 (n/a)</td><td>1.22 (n/a)</td><td>0.45 (n/a)</td><td>0.60 (n/a)</td><td>2335.10 (n/a)</td><td>1258.88 (n/a)</td><td>861.00 (n/a)</td><td>595.00 (n/a)</td><td>792.04 (n/a)</td><td>225.59 (n/a)</td><td>144.22 (n/a)</td><td>155.88 (n/a)</td><td>57.48 (n/a)</td><td>77.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.86 (+3.36%)</td><td>1.05 <b>(-35.97%)</b></td><td>0.76 <b>(-54.56%)</b></td><td>0.57 <b>(-60.98%)</b></td><td>0.55 <b>(+307.17%)</b></td><td>1833.80 <b>(+156.26%)</b></td><td>1205.50 <b>(+88.31%)</b></td><td>1381.20 <b>(+120.08%)</b></td><td>563.00 (-3.25%)</td><td>527.27 <b>(+886.31%)</b></td><td>238.41 (+3.36%)</td><td>134.97 <b>(-35.97%)</b></td><td>97.17 <b>(-54.56%)</b></td><td>73.19 <b>(-60.98%)</b></td><td>70.00 <b>(+307.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.80 (n/a)</td><td>1.65 (n/a)</td><td>1.67 (n/a)</td><td>1.47 (n/a)</td><td>0.13 (n/a)</td><td>715.60 (n/a)</td><td>640.18 (n/a)</td><td>627.60 (n/a)</td><td>581.90 (n/a)</td><td>53.46 (n/a)</td><td>230.65 (n/a)</td><td>210.80 (n/a)</td><td>213.86 (n/a)</td><td>187.55 (n/a)</td><td>17.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.34 <b>(+57.70%)</b></td><td>0.75 <b>(+29.58%)</b></td><td>0.64 (+13.30%)</td><td>0.54 <b>(+198.64%)</b></td><td>0.33 (+19.05%)</td><td>663.60 <b>(-66.51%)</b></td><td>533.72 <b>(-37.24%)</b></td><td>565.20 (-11.74%)</td><td>268.50 <b>(-36.58%)</b></td><td>153.78 <b>(-76.33%)</b></td><td>62.48 <b>(+57.70%)</b></td><td>34.97 <b>(+29.58%)</b></td><td>29.68 (+13.30%)</td><td>25.28 <b>(+198.64%)</b></td><td>15.49 (+19.05%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.85 (n/a)</td><td>0.58 (n/a)</td><td>0.56 (n/a)</td><td>0.18 (n/a)</td><td>0.28 (n/a)</td><td>1981.70 (n/a)</td><td>850.40 (n/a)</td><td>640.40 (n/a)</td><td>423.40 (n/a)</td><td>649.73 (n/a)</td><td>39.62 (n/a)</td><td>26.98 (n/a)</td><td>26.20 (n/a)</td><td>8.47 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.18 (+0.11%)</td><td>2.60 (-7.42%)</td><td>2.83 (-7.08%)</td><td>1.93 (+12.08%)</td><td>0.58 (-5.94%)</td><td>2173.90 (-10.79%)</td><td>1683.80 (+6.75%)</td><td>1479.80 (+7.62%)</td><td>1318.90 (-0.11%)</td><td>399.54 (-17.02%)</td><td>814.14 (+0.11%)</td><td>665.58 (-7.42%)</td><td>725.60 (-7.08%)</td><td>493.91 (+12.08%)</td><td>147.40 (-5.94%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.18 (n/a)</td><td>2.81 (n/a)</td><td>3.05 (n/a)</td><td>1.72 (n/a)</td><td>0.61 (n/a)</td><td>2436.70 (n/a)</td><td>1577.40 (n/a)</td><td>1375.00 (n/a)</td><td>1320.30 (n/a)</td><td>481.50 (n/a)</td><td>813.24 (n/a)</td><td>718.91 (n/a)</td><td>780.88 (n/a)</td><td>440.66 (n/a)</td><td>156.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.89 <b>(+42.49%)</b></td><td>2.94 <b>(+72.51%)</b></td><td>3.27 <b>(+201.65%)</b></td><td>0.73 (+3.43%)</td><td>1.52 <b>(+23.66%)</b></td><td>3567.80 (-3.31%)</td><td>1352.08 <b>(-41.10%)</b></td><td>801.20 <b>(-66.85%)</b></td><td>536.20 <b>(-29.83%)</b></td><td>1253.86 (-9.08%)</td><td>1001.23 <b>(+42.49%)</b></td><td>602.75 <b>(+72.51%)</b></td><td>670.09 <b>(+201.65%)</b></td><td>150.48 (+3.43%)</td><td>311.65 <b>(+23.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.43 (n/a)</td><td>1.71 (n/a)</td><td>1.08 (n/a)</td><td>0.71 (n/a)</td><td>1.23 (n/a)</td><td>3690.10 (n/a)</td><td>2295.62 (n/a)</td><td>2416.80 (n/a)</td><td>764.10 (n/a)</td><td>1379.05 (n/a)</td><td>702.65 (n/a)</td><td>349.39 (n/a)</td><td>222.14 (n/a)</td><td>145.49 (n/a)</td><td>252.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.43 (-7.46%)</td><td>2.76 (-7.73%)</td><td>2.95 (-10.79%)</td><td>1.58 (-17.90%)</td><td>0.72 (-11.86%)</td><td>4967.80 <b>(+21.80%)</b></td><td>3076.40 (+9.02%)</td><td>2668.30 (+12.09%)</td><td>2295.10 (+8.06%)</td><td>1089.49 <b>(+24.42%)</b></td><td>1052.65 (-7.46%)</td><td>847.00 (-7.73%)</td><td>905.40 (-10.79%)</td><td>486.32 (-17.90%)</td><td>221.56 (-11.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.70 (n/a)</td><td>2.99 (n/a)</td><td>3.30 (n/a)</td><td>1.93 (n/a)</td><td>0.82 (n/a)</td><td>4078.60 (n/a)</td><td>2821.82 (n/a)</td><td>2380.40 (n/a)</td><td>2123.90 (n/a)</td><td>875.67 (n/a)</td><td>1137.47 (n/a)</td><td>918.00 (n/a)</td><td>1014.91 (n/a)</td><td>592.33 (n/a)</td><td>251.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>681.20 (n/a)</td><td>469.28 (n/a)</td><td>510.20 (n/a)</td><td>240.80 (n/a)</td><td>205.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2532.10 (n/a)</td><td>834.74 (n/a)</td><td>465.30 (n/a)</td><td>293.30 (n/a)</td><td>953.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.40 (n/a)</td><td>404.30 (n/a)</td><td>444.00 (n/a)</td><td>278.80 (n/a)</td><td>109.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>411.92 (n/a)</td><td>463.00 (n/a)</td><td>225.00 (n/a)</td><td>141.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>710.50 (n/a)</td><td>479.20 (n/a)</td><td>447.60 (n/a)</td><td>299.60 (n/a)</td><td>155.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.50 (n/a)</td><td>468.78 (n/a)</td><td>486.70 (n/a)</td><td>245.70 (n/a)</td><td>136.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>685.10 (n/a)</td><td>347.28 (n/a)</td><td>304.90 (n/a)</td><td>180.70 (n/a)</td><td>196.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.70 (n/a)</td><td>388.94 (n/a)</td><td>444.50 (n/a)</td><td>199.50 (n/a)</td><td>163.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>322.96 (n/a)</td><td>246.50 (n/a)</td><td>192.60 (n/a)</td><td>156.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.40 (n/a)</td><td>423.18 (n/a)</td><td>456.90 (n/a)</td><td>216.50 (n/a)</td><td>179.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.20 (n/a)</td><td>417.98 (n/a)</td><td>373.40 (n/a)</td><td>244.00 (n/a)</td><td>146.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.20 (n/a)</td><td>459.66 (n/a)</td><td>501.10 (n/a)</td><td>197.40 (n/a)</td><td>158.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>429.68 (n/a)</td><td>480.90 (n/a)</td><td>287.20 (n/a)</td><td>103.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>618.10 (n/a)</td><td>500.46 (n/a)</td><td>479.60 (n/a)</td><td>411.30 (n/a)</td><td>93.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>602.30 (n/a)</td><td>369.38 (n/a)</td><td>304.40 (n/a)</td><td>190.60 (n/a)</td><td>196.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2446.20 (n/a)</td><td>766.38 (n/a)</td><td>447.60 (n/a)</td><td>194.70 (n/a)</td><td>946.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>483.50 (n/a)</td><td>337.02 (n/a)</td><td>281.40 (n/a)</td><td>192.00 (n/a)</td><td>129.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.80 (n/a)</td><td>342.90 (n/a)</td><td>341.30 (n/a)</td><td>247.10 (n/a)</td><td>94.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>512.60 (n/a)</td><td>345.52 (n/a)</td><td>325.10 (n/a)</td><td>243.00 (n/a)</td><td>99.85 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>999.10 (n/a)</td><td>615.54 (n/a)</td><td>509.00 (n/a)</td><td>496.90 (n/a)</td><td>216.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>716.10 (n/a)</td><td>605.18 (n/a)</td><td>617.80 (n/a)</td><td>509.50 (n/a)</td><td>76.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>578.80 (n/a)</td><td>468.06 (n/a)</td><td>461.30 (n/a)</td><td>322.60 (n/a)</td><td>97.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>577.80 (n/a)</td><td>379.12 (n/a)</td><td>285.90 (n/a)</td><td>201.10 (n/a)</td><td>177.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2009.80 (n/a)</td><td>972.66 (n/a)</td><td>394.10 (n/a)</td><td>242.80 (n/a)</td><td>875.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 <b>(+20.42%)</b></td><td>0.43 (-0.37%)</td><td>0.35 <b>(-23.94%)</b></td><td>0.32 <b>(+122.17%)</b></td><td>0.19 (+6.94%)</td><td>682.90 <b>(-54.99%)</b></td><td>572.46 (-13.72%)</td><td>632.10 <b>(+31.47%)</b></td><td>286.80 (-16.97%)</td><td>163.31 <b>(-66.08%)</b></td><td>32.91 <b>(+20.42%)</b></td><td>18.34 (-0.37%)</td><td>14.93 <b>(-23.94%)</b></td><td>13.82 <b>(+122.17%)</b></td><td>8.18 (+6.94%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.64 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>1517.10 (n/a)</td><td>663.50 (n/a)</td><td>480.80 (n/a)</td><td>345.40 (n/a)</td><td>481.39 (n/a)</td><td>27.33 (n/a)</td><td>18.41 (n/a)</td><td>19.63 (n/a)</td><td>6.22 (n/a)</td><td>7.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.60 <b>(+35.87%)</b></td><td>0.43 <b>(+40.49%)</b></td><td>0.54 <b>(+93.07%)</b></td><td>0.12 <b>(-47.01%)</b></td><td>0.20 <b>(+112.80%)</b></td><td>1862.80 <b>(+88.70%)</b></td><td>738.72 (-4.58%)</td><td>411.60 <b>(-48.21%)</b></td><td>368.30 <b>(-26.40%)</b></td><td>639.39 <b>(+188.95%)</b></td><td>25.62 <b>(+35.87%)</b></td><td>18.42 <b>(+40.49%)</b></td><td>22.93 <b>(+93.07%)</b></td><td>5.07 <b>(-47.01%)</b></td><td>8.67 <b>(+112.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>987.20 (n/a)</td><td>774.16 (n/a)</td><td>794.70 (n/a)</td><td>500.40 (n/a)</td><td>221.28 (n/a)</td><td>18.86 (n/a)</td><td>13.11 (n/a)</td><td>11.87 (n/a)</td><td>9.56 (n/a)</td><td>4.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.31 (-0.73%)</td><td>0.31 (-0.19%)</td><td>0.31 (-0.34%)</td><td>0.30 (+0.73%)</td><td>0.00 <b>(-32.18%)</b></td><td>83155.10 (-0.72%)</td><td>82246.44 (+0.18%)</td><td>82090.90 (+0.34%)</td><td>81459.60 (+0.74%)</td><td>744.18 <b>(-32.25%)</b></td><td>210.90 (-0.73%)</td><td>208.90 (-0.19%)</td><td>209.28 (-0.34%)</td><td>206.60 (+0.73%)</td><td>1.89 <b>(-32.18%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83760.40 (n/a)</td><td>82097.74 (n/a)</td><td>81809.70 (n/a)</td><td>80861.30 (n/a)</td><td>1098.36 (n/a)</td><td>212.46 (n/a)</td><td>209.29 (n/a)</td><td>210.00 (n/a)</td><td>205.11 (n/a)</td><td>2.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.15 (-0.11%)</td><td>1.09 (-4.22%)</td><td>1.14 (-0.62%)</td><td>0.96 (-13.39%)</td><td>0.08 <b>(+422.25%)</b></td><td>26158.20 (+15.46%)</td><td>23197.62 (+4.88%)</td><td>22122.50 (+0.63%)</td><td>21914.80 (+0.11%)</td><td>1845.91 <b>(+498.01%)</b></td><td>783.94 (-0.11%)</td><td>744.13 (-4.22%)</td><td>776.58 (-0.62%)</td><td>656.77 (-13.39%)</td><td>55.70 <b>(+422.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22656.20 (n/a)</td><td>22117.40 (n/a)</td><td>21984.20 (n/a)</td><td>21890.90 (n/a)</td><td>308.68 (n/a)</td><td>784.79 (n/a)</td><td>776.88 (n/a)</td><td>781.46 (n/a)</td><td>758.29 (n/a)</td><td>10.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.80 (-0.46%)</td><td>0.78 (-1.80%)</td><td>0.78 (-2.29%)</td><td>0.77 (-2.16%)</td><td>0.01 <b>(+99.80%)</b></td><td>97712.50 (+2.21%)</td><td>96284.34 (+1.85%)</td><td>96542.10 (+2.34%)</td><td>94333.50 (+0.46%)</td><td>1316.49 <b>(+104.75%)</b></td><td>728.47 (-0.46%)</td><td>713.82 (-1.80%)</td><td>711.81 (-2.29%)</td><td>703.28 (-2.16%)</td><td>9.82 <b>(+99.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95598.70 (n/a)</td><td>94539.66 (n/a)</td><td>94335.40 (n/a)</td><td>93897.90 (n/a)</td><td>642.97 (n/a)</td><td>731.85 (n/a)</td><td>726.91 (n/a)</td><td>728.46 (n/a)</td><td>718.83 (n/a)</td><td>4.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 (-1.27%)</td><td>0.77 (-0.74%)</td><td>0.77 (-1.05%)</td><td>0.76 (+1.25%)</td><td>0.00 <b>(-65.73%)</b></td><td>99119.30 (-1.24%)</td><td>98451.18 (+0.73%)</td><td>98381.00 (+1.06%)</td><td>97754.10 (+1.29%)</td><td>521.23 <b>(-65.81%)</b></td><td>702.98 (-1.27%)</td><td>698.02 (-0.74%)</td><td>698.50 (-1.05%)</td><td>693.30 (+1.25%)</td><td>3.70 <b>(-65.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100361.50 (n/a)</td><td>97738.32 (n/a)</td><td>97350.80 (n/a)</td><td>96510.70 (n/a)</td><td>1524.57 (n/a)</td><td>712.04 (n/a)</td><td>703.23 (n/a)</td><td>705.90 (n/a)</td><td>684.72 (n/a)</td><td>10.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.90 (+1.81%)</td><td>0.89 (+1.34%)</td><td>0.89 (+1.24%)</td><td>0.87 (+1.15%)</td><td>0.01 <b>(+26.95%)</b></td><td>86660.70 (-1.14%)</td><td>85159.36 (-1.31%)</td><td>84878.10 (-1.23%)</td><td>84187.00 (-1.78%)</td><td>977.78 <b>(+23.22%)</b></td><td>816.27 (+1.81%)</td><td>807.04 (+1.34%)</td><td>809.63 (+1.24%)</td><td>792.97 (+1.15%)</td><td>9.20 <b>(+26.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.01 (n/a)</td><td>87657.60 (n/a)</td><td>86293.14 (n/a)</td><td>85934.40 (n/a)</td><td>85710.20 (n/a)</td><td>793.53 (n/a)</td><td>801.77 (n/a)</td><td>796.40 (n/a)</td><td>799.67 (n/a)</td><td>783.95 (n/a)</td><td>7.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.54 (-13.54%)</td><td>2.91 (-11.75%)</td><td>2.35 (-4.17%)</td><td>1.83 (-16.37%)</td><td>1.14 (-19.03%)</td><td>4858.30 (+19.57%)</td><td>3428.56 (+11.28%)</td><td>3788.50 (+4.35%)</td><td>1964.70 (+15.66%)</td><td>1196.95 (+6.88%)</td><td>273.25 (-13.54%)</td><td>175.34 (-11.75%)</td><td>141.71 (-4.17%)</td><td>110.51 (-16.37%)</td><td>68.66 (-19.03%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.25 (n/a)</td><td>3.30 (n/a)</td><td>2.45 (n/a)</td><td>2.19 (n/a)</td><td>1.41 (n/a)</td><td>4063.10 (n/a)</td><td>3081.10 (n/a)</td><td>3630.50 (n/a)</td><td>1698.70 (n/a)</td><td>1119.88 (n/a)</td><td>316.05 (n/a)</td><td>198.67 (n/a)</td><td>147.88 (n/a)</td><td>132.13 (n/a)</td><td>84.80 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.71 (+2.95%)</td><td>3.41 (-16.71%)</td><td>3.49 (-17.92%)</td><td>2.21 <b>(-22.22%)</b></td><td>1.15 <b>(+59.81%)</b></td><td>4033.90 <b>(+28.57%)</b></td><td>2888.12 <b>(+28.37%)</b></td><td>2556.70 <b>(+21.83%)</b></td><td>1892.70 (-2.87%)</td><td>1018.24 <b>(+102.64%)</b></td><td>283.65 (+2.95%)</td><td>205.17 (-16.71%)</td><td>209.99 (-17.92%)</td><td>133.09 <b>(-22.22%)</b></td><td>69.19 <b>(+59.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.57 (n/a)</td><td>4.09 (n/a)</td><td>4.25 (n/a)</td><td>2.84 (n/a)</td><td>0.72 (n/a)</td><td>3137.60 (n/a)</td><td>2249.80 (n/a)</td><td>2098.60 (n/a)</td><td>1948.60 (n/a)</td><td>502.49 (n/a)</td><td>275.52 (n/a)</td><td>246.34 (n/a)</td><td>255.82 (n/a)</td><td>171.11 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.45 (+19.72%)</td><td>3.23 (+10.03%)</td><td>2.23 (-0.16%)</td><td>2.04 (-6.04%)</td><td>1.52 <b>(+42.29%)</b></td><td>4366.50 (+6.43%)</td><td>3227.96 (-3.13%)</td><td>4003.40 (+0.17%)</td><td>1635.40 (-16.47%)</td><td>1249.05 <b>(+23.52%)</b></td><td>328.27 (+19.72%)</td><td>194.28 (+10.03%)</td><td>134.10 (-0.16%)</td><td>122.95 (-6.04%)</td><td>91.67 <b>(+42.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.55 (n/a)</td><td>2.93 (n/a)</td><td>2.23 (n/a)</td><td>2.17 (n/a)</td><td>1.07 (n/a)</td><td>4102.70 (n/a)</td><td>3332.40 (n/a)</td><td>3996.80 (n/a)</td><td>1957.90 (n/a)</td><td>1011.25 (n/a)</td><td>274.20 (n/a)</td><td>176.58 (n/a)</td><td>134.33 (n/a)</td><td>130.86 (n/a)</td><td>64.43 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.34 (+2.73%)</td><td>5.21 (-6.29%)</td><td>4.86 (-16.41%)</td><td>4.55 (-5.51%)</td><td>0.77 <b>(+24.22%)</b></td><td>7667.90 (+5.83%)</td><td>6806.66 (+7.37%)</td><td>7166.90 (+19.63%)</td><td>5498.10 (-2.66%)</td><td>944.56 <b>(+28.27%)</b></td><td>390.58 (+2.73%)</td><td>320.78 (-6.29%)</td><td>299.64 (-16.41%)</td><td>280.06 (-5.51%)</td><td>47.72 <b>(+24.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.17 (n/a)</td><td>5.56 (n/a)</td><td>5.82 (n/a)</td><td>4.81 (n/a)</td><td>0.62 (n/a)</td><td>7245.40 (n/a)</td><td>6339.30 (n/a)</td><td>5990.90 (n/a)</td><td>5648.10 (n/a)</td><td>736.38 (n/a)</td><td>380.22 (n/a)</td><td>342.32 (n/a)</td><td>358.46 (n/a)</td><td>296.39 (n/a)</td><td>38.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.45 (-6.32%)</td><td>5.35 (+13.13%)</td><td>5.36 (+6.17%)</td><td>5.27 <b>(+50.85%)</b></td><td>0.07 <b>(-92.49%)</b></td><td>6617.90 <b>(-33.71%)</b></td><td>6512.14 (-14.35%)</td><td>6505.00 (-5.81%)</td><td>6394.20 (+6.75%)</td><td>82.20 <b>(-94.77%)</b></td><td>335.85 (-6.32%)</td><td>329.81 (+13.13%)</td><td>330.13 (+6.17%)</td><td>324.50 <b>(+50.85%)</b></td><td>4.17 <b>(-92.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.82 (n/a)</td><td>4.73 (n/a)</td><td>5.05 (n/a)</td><td>3.49 (n/a)</td><td>0.90 (n/a)</td><td>9982.90 (n/a)</td><td>7603.34 (n/a)</td><td>6906.30 (n/a)</td><td>5989.90 (n/a)</td><td>1570.90 (n/a)</td><td>358.52 (n/a)</td><td>291.53 (n/a)</td><td>310.95 (n/a)</td><td>215.12 (n/a)</td><td>55.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.91 (-2.78%)</td><td>5.74 (+14.13%)</td><td>5.24 <b>(+21.92%)</b></td><td>4.58 (+14.03%)</td><td>1.03 (-19.93%)</td><td>7618.10 (-12.30%)</td><td>6229.96 (-14.08%)</td><td>6657.10 (-17.98%)</td><td>5047.10 (+2.85%)</td><td>1101.85 <b>(-30.18%)</b></td><td>425.48 (-2.78%)</td><td>353.67 (+14.13%)</td><td>322.58 <b>(+21.92%)</b></td><td>281.89 (+14.03%)</td><td>63.70 (-19.93%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.11 (n/a)</td><td>5.03 (n/a)</td><td>4.30 (n/a)</td><td>4.01 (n/a)</td><td>1.29 (n/a)</td><td>8686.60 (n/a)</td><td>7251.10 (n/a)</td><td>8116.20 (n/a)</td><td>4907.10 (n/a)</td><td>1578.13 (n/a)</td><td>437.63 (n/a)</td><td>309.88 (n/a)</td><td>264.59 (n/a)</td><td>247.22 (n/a)</td><td>79.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.78 (-2.46%)</td><td>0.77 (+0.21%)</td><td>0.77 (-0.56%)</td><td>0.77 (+3.05%)</td><td>0.00 <b>(-77.52%)</b></td><td>98656.40 (-2.96%)</td><td>98093.26 (-0.27%)</td><td>98280.60 (+0.56%)</td><td>97294.90 (+2.52%)</td><td>611.22 <b>(-77.67%)</b></td><td>706.30 (-2.46%)</td><td>700.57 (+0.21%)</td><td>699.22 (-0.56%)</td><td>696.55 (+3.05%)</td><td>4.37 <b>(-77.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101661.30 (n/a)</td><td>98355.34 (n/a)</td><td>97733.70 (n/a)</td><td>94902.20 (n/a)</td><td>2737.73 (n/a)</td><td>724.11 (n/a)</td><td>699.12 (n/a)</td><td>703.13 (n/a)</td><td>675.96 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 (-1.11%)</td><td>0.76 (+0.65%)</td><td>0.76 (-0.63%)</td><td>0.75 (+7.06%)</td><td>0.01 <b>(-76.74%)</b></td><td>100133.00 (-6.59%)</td><td>99469.94 (-0.76%)</td><td>99786.10 (+0.63%)</td><td>97977.70 (+1.12%)</td><td>873.20 <b>(-78.26%)</b></td><td>701.38 (-1.11%)</td><td>690.90 (+0.65%)</td><td>688.67 (-0.63%)</td><td>686.28 (+7.06%)</td><td>6.12 <b>(-76.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.70 (n/a)</td><td>0.03 (n/a)</td><td>107201.60 (n/a)</td><td>100229.54 (n/a)</td><td>99157.50 (n/a)</td><td>96891.00 (n/a)</td><td>4015.81 (n/a)</td><td>709.24 (n/a)</td><td>686.46 (n/a)</td><td>693.03 (n/a)</td><td>641.03 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.89 (+0.15%)</td><td>0.88 (-0.68%)</td><td>0.88 (-1.16%)</td><td>0.88 (-0.38%)</td><td>0.01 <b>(+55.31%)</b></td><td>86107.20 (+0.38%)</td><td>85634.62 (+0.68%)</td><td>86018.60 (+1.18%)</td><td>84386.30 (-0.15%)</td><td>721.46 <b>(+55.46%)</b></td><td>814.34 (+0.15%)</td><td>802.52 (-0.68%)</td><td>798.89 (-1.16%)</td><td>798.07 (-0.38%)</td><td>6.83 <b>(+55.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>85779.60 (n/a)</td><td>85053.34 (n/a)</td><td>85017.10 (n/a)</td><td>84509.30 (n/a)</td><td>464.09 (n/a)</td><td>813.16 (n/a)</td><td>807.98 (n/a)</td><td>808.30 (n/a)</td><td>801.12 (n/a)</td><td>4.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.72 <b>(+53.01%)</b></td><td>2.80 <b>(+39.06%)</b></td><td>3.02 <b>(+41.30%)</b></td><td>1.70 <b>(+23.06%)</b></td><td>0.82 <b>(+76.18%)</b></td><td>4745.30 (-18.74%)</td><td>3118.26 <b>(-25.75%)</b></td><td>2673.50 <b>(-29.23%)</b></td><td>2167.40 <b>(-34.64%)</b></td><td>1053.85 (-3.07%)</td><td>975.32 <b>(+53.01%)</b></td><td>734.73 <b>(+39.06%)</b></td><td>790.70 <b>(+41.30%)</b></td><td>445.48 <b>(+23.06%)</b></td><td>214.61 <b>(+76.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.43 (n/a)</td><td>2.01 (n/a)</td><td>2.13 (n/a)</td><td>1.38 (n/a)</td><td>0.46 (n/a)</td><td>5839.50 (n/a)</td><td>4199.48 (n/a)</td><td>3777.70 (n/a)</td><td>3316.30 (n/a)</td><td>1087.20 (n/a)</td><td>637.43 (n/a)</td><td>528.34 (n/a)</td><td>559.58 (n/a)</td><td>362.00 (n/a)</td><td>121.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.24 (-12.95%)</td><td>0.19 (-4.26%)</td><td>0.19 (+3.69%)</td><td>0.17 (-7.02%)</td><td>0.03 <b>(-29.11%)</b></td><td>7474.70 (+7.55%)</td><td>6520.52 (+3.43%)</td><td>6633.40 (-3.56%)</td><td>5244.60 (+14.88%)</td><td>898.74 (-12.27%)</td><td>12.80 (-12.95%)</td><td>10.46 (-4.26%)</td><td>10.12 (+3.69%)</td><td>8.98 (-7.02%)</td><td>1.54 <b>(-29.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>6950.10 (n/a)</td><td>6304.14 (n/a)</td><td>6878.10 (n/a)</td><td>4565.20 (n/a)</td><td>1024.49 (n/a)</td><td>14.70 (n/a)</td><td>10.93 (n/a)</td><td>9.76 (n/a)</td><td>9.66 (n/a)</td><td>2.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.84 (n/a)</td><td>3.76 (n/a)</td><td>3.76 (n/a)</td><td>3.71 (n/a)</td><td>0.05 (n/a)</td><td>3.83 (n/a)</td><td>3.76 (n/a)</td><td>3.75 (n/a)</td><td>3.71 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.31 (-3.30%)</td><td>6.81 (+10.11%)</td><td>6.85 (+15.33%)</td><td>6.38 <b>(+49.05%)</b></td><td>0.34 <b>(-73.84%)</b></td><td>7.30 (-3.30%)</td><td>6.81 (+10.11%)</td><td>6.85 (+15.33%)</td><td>6.38 <b>(+49.05%)</b></td><td>0.34 <b>(-73.84%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.56 (n/a)</td><td>6.19 (n/a)</td><td>5.94 (n/a)</td><td>4.28 (n/a)</td><td>1.32 (n/a)</td><td>7.55 (n/a)</td><td>6.19 (n/a)</td><td>5.94 (n/a)</td><td>4.28 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>13.46 (+4.10%)</td><td>11.01 (+18.59%)</td><td>11.22 <b>(+30.76%)</b></td><td>8.22 (+6.44%)</td><td>2.24 (+8.05%)</td><td>13.45 (+4.10%)</td><td>11.00 (+18.59%)</td><td>11.21 <b>(+30.76%)</b></td><td>8.21 (+6.44%)</td><td>2.24 (+8.05%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>12.93 (n/a)</td><td>9.29 (n/a)</td><td>8.58 (n/a)</td><td>7.72 (n/a)</td><td>2.08 (n/a)</td><td>12.92 (n/a)</td><td>9.28 (n/a)</td><td>8.58 (n/a)</td><td>7.72 (n/a)</td><td>2.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.80 (n/a)</td><td>3.67 (n/a)</td><td>3.75 (n/a)</td><td>3.49 (n/a)</td><td>0.15 (n/a)</td><td>3.80 (n/a)</td><td>3.67 (n/a)</td><td>3.75 (n/a)</td><td>3.49 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.97 (-2.07%)</td><td>6.31 (+6.87%)</td><td>6.38 (+12.49%)</td><td>5.62 (+5.06%)</td><td>0.56 (-19.80%)</td><td>6.97 (-2.07%)</td><td>6.30 (+6.87%)</td><td>6.38 (+12.49%)</td><td>5.62 (+5.06%)</td><td>0.56 (-19.80%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>7.12 (n/a)</td><td>5.90 (n/a)</td><td>5.67 (n/a)</td><td>5.35 (n/a)</td><td>0.70 (n/a)</td><td>7.12 (n/a)</td><td>5.90 (n/a)</td><td>5.67 (n/a)</td><td>5.34 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>14.06 (+11.54%)</td><td>9.68 (+0.21%)</td><td>8.19 (-0.48%)</td><td>7.63 (-2.75%)</td><td>2.71 <b>(+22.43%)</b></td><td>14.05 (+11.54%)</td><td>9.67 (+0.21%)</td><td>8.19 (-0.48%)</td><td>7.62 (-2.75%)</td><td>2.71 <b>(+22.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>12.60 (n/a)</td><td>9.66 (n/a)</td><td>8.23 (n/a)</td><td>7.84 (n/a)</td><td>2.21 (n/a)</td><td>12.60 (n/a)</td><td>9.65 (n/a)</td><td>8.22 (n/a)</td><td>7.84 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.75 (-10.86%)</td><td>1.66 <b>(-36.24%)</b></td><td>1.17 <b>(-59.58%)</b></td><td>1.02 <b>(-35.19%)</b></td><td>0.81 <b>(+26.98%)</b></td><td>2.75 (-10.86%)</td><td>1.65 <b>(-36.24%)</b></td><td>1.17 <b>(-59.58%)</b></td><td>1.02 <b>(-35.19%)</b></td><td>0.81 <b>(+26.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.09 (n/a)</td><td>2.60 (n/a)</td><td>2.91 (n/a)</td><td>1.57 (n/a)</td><td>0.64 (n/a)</td><td>3.08 (n/a)</td><td>2.59 (n/a)</td><td>2.90 (n/a)</td><td>1.57 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.51 (-10.46%)</td><td>0.33 <b>(+25.60%)</b></td><td>0.35 <b>(+64.41%)</b></td><td>0.08 (+3.31%)</td><td>0.16 <b>(-26.05%)</b></td><td>0.50 (-10.46%)</td><td>0.33 <b>(+25.60%)</b></td><td>0.34 <b>(+64.41%)</b></td><td>0.07 (+3.31%)</td><td>0.16 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.57 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td><td>0.56 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.65 (-17.35%)</td><td>0.41 (-6.77%)</td><td>0.44 (-6.33%)</td><td>0.08 (+1.36%)</td><td>0.22 <b>(-22.41%)</b></td><td>0.64 (-17.35%)</td><td>0.41 (-6.77%)</td><td>0.43 (-6.33%)</td><td>0.08 (+1.36%)</td><td>0.22 <b>(-22.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.78 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.28 (n/a)</td><td>0.78 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.94 <b>(-27.27%)</b></td><td>1.38 <b>(-29.93%)</b></td><td>1.59 <b>(-31.88%)</b></td><td>0.45 (+3.67%)</td><td>0.59 <b>(-35.42%)</b></td><td>1.91 <b>(-27.27%)</b></td><td>1.36 <b>(-29.93%)</b></td><td>1.57 <b>(-31.88%)</b></td><td>0.45 (+3.67%)</td><td>0.58 <b>(-35.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.66 (n/a)</td><td>1.97 (n/a)</td><td>2.34 (n/a)</td><td>0.44 (n/a)</td><td>0.91 (n/a)</td><td>2.62 (n/a)</td><td>1.94 (n/a)</td><td>2.30 (n/a)</td><td>0.43 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.10 (n/a)</td><td>345.98 (n/a)</td><td>254.40 (n/a)</td><td>241.80 (n/a)</td><td>148.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.00 (n/a)</td><td>282.12 (n/a)</td><td>246.90 (n/a)</td><td>216.80 (n/a)</td><td>86.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.30 (n/a)</td><td>405.94 (n/a)</td><td>503.30 (n/a)</td><td>198.30 (n/a)</td><td>176.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.60 (n/a)</td><td>358.34 (n/a)</td><td>244.90 (n/a)</td><td>232.60 (n/a)</td><td>161.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>371.36 (n/a)</td><td>417.30 (n/a)</td><td>200.80 (n/a)</td><td>131.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.90 (n/a)</td><td>360.80 (n/a)</td><td>306.50 (n/a)</td><td>249.60 (n/a)</td><td>108.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.90 (n/a)</td><td>410.74 (n/a)</td><td>461.00 (n/a)</td><td>250.50 (n/a)</td><td>130.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.90 (n/a)</td><td>376.58 (n/a)</td><td>271.50 (n/a)</td><td>227.80 (n/a)</td><td>179.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>321.00 (n/a)</td><td>260.40 (n/a)</td><td>246.10 (n/a)</td><td>138.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>360.42 (n/a)</td><td>298.60 (n/a)</td><td>269.70 (n/a)</td><td>121.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.20 (n/a)</td><td>449.90 (n/a)</td><td>529.20 (n/a)</td><td>242.30 (n/a)</td><td>173.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>440.12 (n/a)</td><td>475.00 (n/a)</td><td>245.70 (n/a)</td><td>139.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>522.80 (n/a)</td><td>333.80 (n/a)</td><td>298.70 (n/a)</td><td>255.10 (n/a)</td><td>107.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1063.30 (n/a)</td><td>563.60 (n/a)</td><td>514.50 (n/a)</td><td>258.00 (n/a)</td><td>300.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>517.80 (n/a)</td><td>327.30 (n/a)</td><td>287.80 (n/a)</td><td>248.70 (n/a)</td><td>110.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>406.18 (n/a)</td><td>430.50 (n/a)</td><td>244.50 (n/a)</td><td>96.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>499.00 (n/a)</td><td>377.90 (n/a)</td><td>383.80 (n/a)</td><td>244.80 (n/a)</td><td>92.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1971.10 (n/a)</td><td>752.08 (n/a)</td><td>484.60 (n/a)</td><td>241.20 (n/a)</td><td>700.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1818.60 (n/a)</td><td>729.72 (n/a)</td><td>537.80 (n/a)</td><td>284.30 (n/a)</td><td>630.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.30 (n/a)</td><td>408.30 (n/a)</td><td>461.30 (n/a)</td><td>256.80 (n/a)</td><td>122.39 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.50 (n/a)</td><td>417.06 (n/a)</td><td>376.80 (n/a)</td><td>287.90 (n/a)</td><td>136.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>505.30 (n/a)</td><td>315.76 (n/a)</td><td>277.40 (n/a)</td><td>234.10 (n/a)</td><td>108.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>685.30 (n/a)</td><td>502.14 (n/a)</td><td>503.90 (n/a)</td><td>253.90 (n/a)</td><td>184.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>768.00 (n/a)</td><td>449.62 (n/a)</td><td>345.20 (n/a)</td><td>252.00 (n/a)</td><td>217.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-3.03%)</td><td>0.01 (-14.31%)</td><td>0.01 <b>(-28.85%)</b></td><td>0.01 (+9.63%)</td><td>0.00 (-7.17%)</td><td>528.80 (-8.78%)</td><td>402.04 (+14.61%)</td><td>440.40 <b>(+40.52%)</b></td><td>245.50 (+3.11%)</td><td>118.44 (-13.91%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.70 (n/a)</td><td>350.78 (n/a)</td><td>313.40 (n/a)</td><td>238.10 (n/a)</td><td>137.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-1.75%)</td><td>0.01 (+15.91%)</td><td>0.01 <b>(+54.71%)</b></td><td>0.01 (+5.08%)</td><td>0.00 (+0.52%)</td><td>645.00 (-4.83%)</td><td>417.28 (-11.96%)</td><td>319.10 <b>(-35.37%)</b></td><td>229.70 (+1.77%)</td><td>183.70 (+13.36%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>677.70 (n/a)</td><td>473.96 (n/a)</td><td>493.70 (n/a)</td><td>225.70 (n/a)</td><td>162.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+3.93%)</td><td>0.01 (+7.52%)</td><td>0.01 <b>(+47.64%)</b></td><td>0.00 <b>(-74.29%)</b></td><td>0.01 <b>(+80.71%)</b></td><td>1952.90 <b>(+288.95%)</b></td><td>631.14 <b>(+54.65%)</b></td><td>303.30 <b>(-32.27%)</b></td><td>269.90 (-3.78%)</td><td>739.70 <b>(+604.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.10 (n/a)</td><td>408.12 (n/a)</td><td>447.80 (n/a)</td><td>280.50 (n/a)</td><td>105.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+4.19%)</td><td>0.01 <b>(+22.46%)</b></td><td>0.01 <b>(+86.65%)</b></td><td>0.00 <b>(-71.41%)</b></td><td>0.01 <b>(+60.69%)</b></td><td>2234.00 <b>(+249.77%)</b></td><td>695.70 <b>(+47.41%)</b></td><td>277.60 <b>(-46.42%)</b></td><td>233.50 (-4.03%)</td><td>866.35 <b>(+479.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>638.70 (n/a)</td><td>471.96 (n/a)</td><td>518.10 (n/a)</td><td>243.30 (n/a)</td><td>149.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-5.00%)</td><td>0.01 (+18.91%)</td><td>0.02 <b>(+44.99%)</b></td><td>0.01 (+4.01%)</td><td>0.00 (-14.00%)</td><td>551.80 (-3.85%)</td><td>317.64 (-17.43%)</td><td>270.80 <b>(-31.02%)</b></td><td>235.60 (+5.27%)</td><td>131.85 (-5.77%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.90 (n/a)</td><td>384.70 (n/a)</td><td>392.60 (n/a)</td><td>223.80 (n/a)</td><td>139.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-13.89%)</td><td>0.01 (+10.31%)</td><td>0.01 <b>(+46.33%)</b></td><td>0.01 (-9.00%)</td><td>0.00 <b>(-20.18%)</b></td><td>622.50 (+9.90%)</td><td>407.98 (-10.92%)</td><td>352.30 <b>(-31.67%)</b></td><td>256.70 (+16.10%)</td><td>151.06 (+7.39%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.40 (n/a)</td><td>458.00 (n/a)</td><td>515.60 (n/a)</td><td>221.10 (n/a)</td><td>140.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+55.84%)</b></td><td>0.02 <b>(+38.20%)</b></td><td>0.02 <b>(+20.62%)</b></td><td>0.02 (+6.63%)</td><td>0.01 <b>(+195.75%)</b></td><td>515.20 (-6.22%)</td><td>357.12 <b>(-22.61%)</b></td><td>355.60 (-17.09%)</td><td>244.70 <b>(-35.84%)</b></td><td>116.42 <b>(+64.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.40 (n/a)</td><td>461.44 (n/a)</td><td>428.90 (n/a)</td><td>381.40 (n/a)</td><td>70.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(-24.60%)</b></td><td>0.02 <b>(-24.00%)</b></td><td>0.03 (-4.24%)</td><td>0.00 <b>(-84.59%)</b></td><td>0.01 <b>(+108.00%)</b></td><td>1924.20 <b>(+548.97%)</b></td><td>612.78 <b>(+130.61%)</b></td><td>286.60 (+4.41%)</td><td>267.70 <b>(+32.66%)</b></td><td>733.20 <b>(+1819.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.50 (n/a)</td><td>265.72 (n/a)</td><td>274.50 (n/a)</td><td>201.80 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+21.42%)</b></td><td>0.02 (+10.61%)</td><td>0.03 <b>(+41.81%)</b></td><td>0.01 <b>(-28.06%)</b></td><td>0.01 <b>(+62.21%)</b></td><td>752.40 <b>(+39.00%)</b></td><td>436.42 (+3.15%)</td><td>319.50 <b>(-29.49%)</b></td><td>234.10 (-17.63%)</td><td>228.84 <b>(+88.84%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.30 (n/a)</td><td>423.10 (n/a)</td><td>453.10 (n/a)</td><td>284.20 (n/a)</td><td>121.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (+8.92%)</td><td>0.02 <b>(-21.94%)</b></td><td>0.02 <b>(-40.96%)</b></td><td>0.01 <b>(-27.54%)</b></td><td>0.01 <b>(+87.39%)</b></td><td>590.70 <b>(+38.01%)</b></td><td>434.66 <b>(+41.94%)</b></td><td>479.70 <b>(+69.39%)</b></td><td>240.30 (-8.18%)</td><td>162.92 <b>(+135.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>428.00 (n/a)</td><td>306.22 (n/a)</td><td>283.20 (n/a)</td><td>261.70 (n/a)</td><td>69.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 <b>(+26.50%)</b></td><td>0.03 <b>(+20.34%)</b></td><td>0.03 <b>(+23.95%)</b></td><td>0.02 (-3.68%)</td><td>0.01 <b>(+31.22%)</b></td><td>458.40 (+3.83%)</td><td>286.78 (-14.85%)</td><td>266.20 (-19.31%)</td><td>180.10 <b>(-20.94%)</b></td><td>104.57 (+8.78%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.50 (n/a)</td><td>336.80 (n/a)</td><td>329.90 (n/a)</td><td>227.80 (n/a)</td><td>96.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(-42.88%)</b></td><td>0.02 <b>(-24.34%)</b></td><td>0.02 (-11.07%)</td><td>0.01 (-13.19%)</td><td>0.00 <b>(-75.96%)</b></td><td>596.40 (+15.20%)</td><td>524.46 <b>(+25.60%)</b></td><td>510.70 (+12.44%)</td><td>464.90 <b>(+75.10%)</b></td><td>50.17 <b>(-50.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.70 (n/a)</td><td>417.58 (n/a)</td><td>454.20 (n/a)</td><td>265.50 (n/a)</td><td>101.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-15.39%)</td><td>0.02 (-18.38%)</td><td>0.02 <b>(-36.37%)</b></td><td>0.01 (-13.76%)</td><td>0.01 (-15.53%)</td><td>607.70 (+15.95%)</td><td>443.58 <b>(+21.76%)</b></td><td>498.50 <b>(+57.16%)</b></td><td>290.50 (+18.19%)</td><td>135.83 (+9.73%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.10 (n/a)</td><td>364.30 (n/a)</td><td>317.20 (n/a)</td><td>245.80 (n/a)</td><td>123.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (+6.52%)</td><td>0.02 (+2.82%)</td><td>0.02 (+5.66%)</td><td>0.01 (-4.44%)</td><td>0.01 (+5.46%)</td><td>634.80 (+4.63%)</td><td>435.30 (-2.07%)</td><td>454.10 (-5.36%)</td><td>282.30 (-6.12%)</td><td>137.37 (+5.97%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.70 (n/a)</td><td>444.50 (n/a)</td><td>479.80 (n/a)</td><td>300.70 (n/a)</td><td>129.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+17.01%)</td><td>0.06 (+12.81%)</td><td>0.06 (+2.80%)</td><td>0.05 <b>(+70.43%)</b></td><td>0.01 <b>(-30.94%)</b></td><td>320.70 <b>(-41.33%)</b></td><td>269.84 (-16.68%)</td><td>262.70 (-2.74%)</td><td>222.00 (-14.52%)</td><td>42.37 <b>(-66.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>546.60 (n/a)</td><td>323.86 (n/a)</td><td>270.10 (n/a)</td><td>259.70 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+5.22%)</td><td>0.06 (+16.43%)</td><td>0.06 (+14.77%)</td><td>0.04 (+5.29%)</td><td>0.01 (-0.08%)</td><td>448.50 (-5.02%)</td><td>301.32 (-14.71%)</td><td>285.40 (-12.88%)</td><td>229.00 (-4.94%)</td><td>87.82 (-10.92%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.20 (n/a)</td><td>353.28 (n/a)</td><td>327.60 (n/a)</td><td>240.90 (n/a)</td><td>98.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (-0.41%)</td><td>0.05 (-8.65%)</td><td>0.05 (-9.07%)</td><td>0.04 <b>(+21.06%)</b></td><td>0.01 <b>(-22.95%)</b></td><td>405.30 (-17.39%)</td><td>323.36 (+5.68%)</td><td>303.40 (+9.97%)</td><td>240.90 (+0.42%)</td><td>64.98 <b>(-37.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>490.60 (n/a)</td><td>305.98 (n/a)</td><td>275.90 (n/a)</td><td>239.90 (n/a)</td><td>104.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+0.14%)</td><td>0.05 (+7.04%)</td><td>0.06 (-0.45%)</td><td>0.03 (+4.95%)</td><td>0.01 (-16.31%)</td><td>489.40 (-4.71%)</td><td>320.56 (-10.26%)</td><td>290.20 (+0.45%)</td><td>237.90 (-0.13%)</td><td>104.07 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.60 (n/a)</td><td>357.22 (n/a)</td><td>288.90 (n/a)</td><td>238.20 (n/a)</td><td>136.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(+25.01%)</b></td><td>0.05 (+2.42%)</td><td>0.04 <b>(-23.91%)</b></td><td>0.02 <b>(-21.00%)</b></td><td>0.02 <b>(+93.44%)</b></td><td>659.60 <b>(+26.58%)</b></td><td>422.66 (+9.83%)</td><td>450.60 <b>(+31.45%)</b></td><td>219.50 (-19.98%)</td><td>181.87 <b>(+85.83%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>521.10 (n/a)</td><td>384.82 (n/a)</td><td>342.80 (n/a)</td><td>274.30 (n/a)</td><td>97.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-0.07%)</td><td>0.04 (-9.17%)</td><td>0.04 (-13.00%)</td><td>0.03 (-6.89%)</td><td>0.01 (-1.33%)</td><td>539.60 (+7.40%)</td><td>437.92 (+10.06%)</td><td>448.00 (+14.93%)</td><td>304.80 (+0.07%)</td><td>84.44 (+1.13%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.40 (n/a)</td><td>397.88 (n/a)</td><td>389.80 (n/a)</td><td>304.60 (n/a)</td><td>83.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+17.73%)</td><td>0.09 (+16.21%)</td><td>0.07 (-3.16%)</td><td>0.05 (-9.15%)</td><td>0.04 <b>(+50.05%)</b></td><td>660.10 (+10.09%)</td><td>414.28 (-7.48%)</td><td>444.20 (+3.28%)</td><td>228.80 (-15.04%)</td><td>173.51 <b>(+36.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>599.60 (n/a)</td><td>447.76 (n/a)</td><td>430.10 (n/a)</td><td>269.30 (n/a)</td><td>127.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+9.12%)</td><td>0.07 <b>(-31.20%)</b></td><td>0.06 <b>(-50.21%)</b></td><td>0.04 <b>(-32.59%)</b></td><td>0.04 <b>(+36.45%)</b></td><td>769.30 <b>(+48.34%)</b></td><td>531.60 <b>(+59.48%)</b></td><td>565.30 <b>(+100.82%)</b></td><td>228.80 (-8.37%)</td><td>199.74 <b>(+75.02%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.60 (n/a)</td><td>333.34 (n/a)</td><td>281.50 (n/a)</td><td>249.70 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+5.47%)</td><td>0.07 (-18.97%)</td><td>0.06 (-12.92%)</td><td>0.02 <b>(-69.33%)</b></td><td>0.05 <b>(+28.61%)</b></td><td>2077.40 <b>(+226.02%)</b></td><td>761.62 <b>(+79.96%)</b></td><td>511.40 (+14.84%)</td><td>226.80 (-5.18%)</td><td>745.67 <b>(+357.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>637.20 (n/a)</td><td>423.22 (n/a)</td><td>445.30 (n/a)</td><td>239.20 (n/a)</td><td>162.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (-12.97%)</td><td>0.07 (-18.89%)</td><td>0.06 (-8.42%)</td><td>0.04 (-18.37%)</td><td>0.03 (-14.00%)</td><td>803.70 <b>(+22.52%)</b></td><td>588.14 <b>(+23.01%)</b></td><td>589.40 (+9.19%)</td><td>266.00 (+14.90%)</td><td>219.38 (+16.95%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>656.00 (n/a)</td><td>478.14 (n/a)</td><td>539.80 (n/a)</td><td>231.50 (n/a)</td><td>187.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 <b>(-31.80%)</b></td><td>0.07 (-14.05%)</td><td>0.07 (-6.55%)</td><td>0.06 <b>(+29.07%)</b></td><td>0.01 <b>(-66.21%)</b></td><td>531.60 <b>(-22.52%)</b></td><td>474.08 (+5.66%)</td><td>501.20 (+7.00%)</td><td>372.00 <b>(+46.63%)</b></td><td>62.86 <b>(-61.58%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>686.10 (n/a)</td><td>448.68 (n/a)</td><td>468.40 (n/a)</td><td>253.70 (n/a)</td><td>163.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+4.81%)</td><td>0.01 (+8.59%)</td><td>0.02 <b>(+23.49%)</b></td><td>0.01 (+11.98%)</td><td>0.00 <b>(+24.89%)</b></td><td>537.30 (-10.70%)</td><td>364.60 (-5.33%)</td><td>268.10 (-19.00%)</td><td>255.90 (-4.59%)</td><td>143.40 (+4.80%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.70 (n/a)</td><td>385.12 (n/a)</td><td>331.00 (n/a)</td><td>268.20 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+23.30%)</b></td><td>0.02 <b>(+35.46%)</b></td><td>0.02 <b>(+23.21%)</b></td><td>0.01 <b>(+71.05%)</b></td><td>0.00 <b>(-47.00%)</b></td><td>300.50 <b>(-41.53%)</b></td><td>256.76 <b>(-29.14%)</b></td><td>248.40 (-18.82%)</td><td>239.20 (-18.92%)</td><td>25.01 <b>(-73.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.90 (n/a)</td><td>362.34 (n/a)</td><td>306.00 (n/a)</td><td>295.00 (n/a)</td><td>95.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-19.94%)</td><td>0.01 (-7.54%)</td><td>0.01 (-9.53%)</td><td>0.01 <b>(+33.71%)</b></td><td>0.00 <b>(-47.30%)</b></td><td>455.80 <b>(-25.21%)</b></td><td>367.84 (-1.00%)</td><td>325.00 (+10.54%)</td><td>291.10 <b>(+24.88%)</b></td><td>78.73 <b>(-49.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.40 (n/a)</td><td>371.54 (n/a)</td><td>294.00 (n/a)</td><td>233.10 (n/a)</td><td>156.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+30.31%)</b></td><td>0.01 (-13.46%)</td><td>0.01 <b>(-41.07%)</b></td><td>0.01 <b>(-28.40%)</b></td><td>0.01 <b>(+171.37%)</b></td><td>554.60 <b>(+39.70%)</b></td><td>399.34 <b>(+30.70%)</b></td><td>481.10 <b>(+69.70%)</b></td><td>209.40 <b>(-23.27%)</b></td><td>150.58 <b>(+187.61%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>397.00 (n/a)</td><td>305.54 (n/a)</td><td>283.50 (n/a)</td><td>272.90 (n/a)</td><td>52.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 <b>(-36.48%)</b></td><td>0.01 <b>(-40.99%)</b></td><td>0.01 <b>(-48.92%)</b></td><td>0.01 (-5.35%)</td><td>0.00 <b>(-59.19%)</b></td><td>605.10 (+5.66%)</td><td>475.34 <b>(+54.66%)</b></td><td>474.10 <b>(+95.75%)</b></td><td>344.20 <b>(+57.46%)</b></td><td>93.55 <b>(-37.35%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.70 (n/a)</td><td>307.34 (n/a)</td><td>242.20 (n/a)</td><td>218.60 (n/a)</td><td>149.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+1.37%)</td><td>0.01 (+3.48%)</td><td>0.02 (+7.73%)</td><td>0.01 <b>(+42.06%)</b></td><td>0.00 (-16.29%)</td><td>390.90 <b>(-29.62%)</b></td><td>306.40 (-7.52%)</td><td>268.30 (-7.16%)</td><td>235.40 (-1.34%)</td><td>70.61 <b>(-44.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.40 (n/a)</td><td>331.32 (n/a)</td><td>289.00 (n/a)</td><td>238.60 (n/a)</td><td>127.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 <b>(-38.64%)</b></td><td>0.01 <b>(-36.83%)</b></td><td>0.01 <b>(-35.13%)</b></td><td>0.01 <b>(-38.07%)</b></td><td>0.00 <b>(-43.74%)</b></td><td>764.80 <b>(+61.45%)</b></td><td>545.84 <b>(+57.01%)</b></td><td>523.70 <b>(+54.12%)</b></td><td>396.90 <b>(+62.93%)</b></td><td>136.90 <b>(+51.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.70 (n/a)</td><td>347.64 (n/a)</td><td>339.80 (n/a)</td><td>243.60 (n/a)</td><td>90.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-13.53%)</td><td>0.01 (-4.62%)</td><td>0.01 <b>(+21.45%)</b></td><td>0.01 (-9.65%)</td><td>0.00 (-12.79%)</td><td>650.70 (+10.68%)</td><td>419.70 (+4.87%)</td><td>359.50 (-17.66%)</td><td>278.00 (+15.64%)</td><td>157.76 (+13.93%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.90 (n/a)</td><td>400.22 (n/a)</td><td>436.60 (n/a)</td><td>240.40 (n/a)</td><td>138.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+11.50%)</td><td>0.01 (+1.64%)</td><td>0.01 (-10.44%)</td><td>0.01 (+2.51%)</td><td>0.00 <b>(+28.17%)</b></td><td>536.60 (-2.45%)</td><td>381.72 (+1.80%)</td><td>338.40 (+11.65%)</td><td>247.40 (-10.30%)</td><td>140.31 (+16.50%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.10 (n/a)</td><td>374.98 (n/a)</td><td>303.10 (n/a)</td><td>275.80 (n/a)</td><td>120.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-8.35%)</td><td>0.01 (+15.51%)</td><td>0.01 <b>(+36.91%)</b></td><td>0.01 (+1.81%)</td><td>0.00 <b>(-20.53%)</b></td><td>495.50 (-1.78%)</td><td>324.92 (-15.26%)</td><td>302.30 <b>(-26.96%)</b></td><td>252.90 (+9.10%)</td><td>98.11 (-10.33%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.50 (n/a)</td><td>383.44 (n/a)</td><td>413.90 (n/a)</td><td>231.80 (n/a)</td><td>109.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>681.90 (n/a)</td><td>415.28 (n/a)</td><td>316.40 (n/a)</td><td>276.90 (n/a)</td><td>177.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-10.29%)</td><td>0.01 (-7.19%)</td><td>0.01 <b>(+20.27%)</b></td><td>0.00 <b>(-35.87%)</b></td><td>0.00 (-7.57%)</td><td>899.30 <b>(+55.94%)</b></td><td>488.54 (+12.96%)</td><td>401.00 (-16.86%)</td><td>289.40 (+11.48%)</td><td>240.04 <b>(+71.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.70 (n/a)</td><td>432.48 (n/a)</td><td>482.30 (n/a)</td><td>259.60 (n/a)</td><td>139.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (+11.36%)</td><td>0.03 (+9.61%)</td><td>0.02 (-18.17%)</td><td>0.02 <b>(+84.80%)</b></td><td>0.01 <b>(-26.98%)</b></td><td>399.40 <b>(-45.89%)</b></td><td>334.76 (-17.82%)</td><td>361.70 <b>(+22.20%)</b></td><td>239.30 (-10.21%)</td><td>72.80 <b>(-63.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>738.10 (n/a)</td><td>407.36 (n/a)</td><td>296.00 (n/a)</td><td>266.50 (n/a)</td><td>199.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (+8.00%)</td><td>0.02 (+5.70%)</td><td>0.02 (+3.11%)</td><td>0.01 (-2.55%)</td><td>0.01 (+5.79%)</td><td>584.80 (+2.61%)</td><td>378.40 (-5.22%)</td><td>376.90 (-3.01%)</td><td>219.40 (-7.39%)</td><td>140.84 (-1.67%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>399.26 (n/a)</td><td>388.60 (n/a)</td><td>236.90 (n/a)</td><td>143.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-16.65%)</td><td>0.03 (-5.73%)</td><td>0.03 (-8.73%)</td><td>0.01 (+4.15%)</td><td>0.01 <b>(-29.28%)</b></td><td>565.60 (-3.99%)</td><td>335.66 (-0.01%)</td><td>296.20 (+9.58%)</td><td>224.90 (+19.95%)</td><td>134.03 (-16.10%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.10 (n/a)</td><td>335.70 (n/a)</td><td>270.30 (n/a)</td><td>187.50 (n/a)</td><td>159.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+33.58%)</b></td><td>0.02 (+13.10%)</td><td>0.02 (-0.83%)</td><td>0.01 <b>(+28.78%)</b></td><td>0.01 <b>(+44.66%)</b></td><td>570.30 <b>(-22.34%)</b></td><td>442.24 (-11.02%)</td><td>470.60 (+0.84%)</td><td>279.80 <b>(-25.13%)</b></td><td>109.06 <b>(-22.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>734.40 (n/a)</td><td>497.02 (n/a)</td><td>466.70 (n/a)</td><td>373.70 (n/a)</td><td>140.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-4.60%)</td><td>0.02 <b>(-23.02%)</b></td><td>0.02 <b>(-27.77%)</b></td><td>0.01 <b>(-49.02%)</b></td><td>0.01 <b>(+50.23%)</b></td><td>902.10 <b>(+96.15%)</b></td><td>465.12 <b>(+48.36%)</b></td><td>395.30 <b>(+38.46%)</b></td><td>268.60 (+4.80%)</td><td>254.57 <b>(+207.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.90 (n/a)</td><td>313.50 (n/a)</td><td>285.50 (n/a)</td><td>256.30 (n/a)</td><td>82.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 <b>(+132.89%)</b></td><td>0.03 <b>(+78.28%)</b></td><td>0.03 <b>(+77.76%)</b></td><td>0.02 <b>(+52.26%)</b></td><td>0.01 <b>(+263.52%)</b></td><td>495.50 <b>(-34.33%)</b></td><td>336.30 <b>(-39.25%)</b></td><td>285.90 <b>(-43.75%)</b></td><td>197.30 <b>(-57.06%)</b></td><td>124.00 (+4.19%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>754.50 (n/a)</td><td>553.60 (n/a)</td><td>508.30 (n/a)</td><td>459.50 (n/a)</td><td>119.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-2.70%)</td><td>0.02 <b>(-26.59%)</b></td><td>0.03 (-10.13%)</td><td>0.00 <b>(-76.59%)</b></td><td>0.01 <b>(+127.82%)</b></td><td>1806.40 <b>(+327.15%)</b></td><td>699.94 <b>(+118.55%)</b></td><td>319.20 (+11.26%)</td><td>270.60 (+2.77%)</td><td>653.81 <b>(+877.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>422.90 (n/a)</td><td>320.26 (n/a)</td><td>286.90 (n/a)</td><td>263.30 (n/a)</td><td>66.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(-21.24%)</b></td><td>0.02 (+6.49%)</td><td>0.02 <b>(+21.52%)</b></td><td>0.01 (+16.63%)</td><td>0.01 <b>(-25.05%)</b></td><td>1025.70 (-14.26%)</td><td>500.30 (-12.92%)</td><td>378.40 (-17.70%)</td><td>301.70 <b>(+26.98%)</b></td><td>300.31 (-17.95%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1196.30 (n/a)</td><td>574.54 (n/a)</td><td>459.80 (n/a)</td><td>237.60 (n/a)</td><td>366.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (+14.80%)</td><td>0.02 (-8.90%)</td><td>0.01 <b>(-27.53%)</b></td><td>0.01 <b>(-22.18%)</b></td><td>0.01 <b>(+43.87%)</b></td><td>781.70 <b>(+28.51%)</b></td><td>547.18 (+19.26%)</td><td>591.30 <b>(+37.99%)</b></td><td>233.60 (-12.90%)</td><td>201.56 <b>(+44.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>458.80 (n/a)</td><td>428.50 (n/a)</td><td>268.20 (n/a)</td><td>139.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(-20.54%)</b></td><td>0.02 (-13.42%)</td><td>0.02 (+12.08%)</td><td>0.01 (+7.48%)</td><td>0.01 <b>(-41.78%)</b></td><td>591.30 (-6.97%)</td><td>436.50 (+7.16%)</td><td>386.80 (-10.77%)</td><td>301.80 <b>(+25.85%)</b></td><td>126.48 <b>(-23.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.60 (n/a)</td><td>407.34 (n/a)</td><td>433.50 (n/a)</td><td>239.80 (n/a)</td><td>166.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-11.07%)</td><td>0.02 (-12.69%)</td><td>0.02 (-10.65%)</td><td>0.01 (-15.08%)</td><td>0.01 (-12.39%)</td><td>672.90 (+17.76%)</td><td>447.76 (+14.82%)</td><td>386.60 (+11.93%)</td><td>311.70 (+12.45%)</td><td>150.06 (+18.46%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>389.96 (n/a)</td><td>345.40 (n/a)</td><td>277.20 (n/a)</td><td>126.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+23.72%)</b></td><td>0.02 (+7.77%)</td><td>0.02 (+1.16%)</td><td>0.01 (+0.51%)</td><td>0.01 <b>(+69.91%)</b></td><td>586.60 (-0.51%)</td><td>432.14 (-2.46%)</td><td>424.80 (-1.14%)</td><td>282.70 (-19.18%)</td><td>139.33 <b>(+40.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.60 (n/a)</td><td>443.02 (n/a)</td><td>429.70 (n/a)</td><td>349.80 (n/a)</td><td>99.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+4.90%)</td><td>0.06 (+5.31%)</td><td>0.06 (-0.97%)</td><td>0.04 <b>(+30.48%)</b></td><td>0.01 <b>(-20.57%)</b></td><td>435.10 <b>(-23.36%)</b></td><td>303.14 (-9.28%)</td><td>280.30 (+0.97%)</td><td>249.90 (-4.65%)</td><td>75.95 <b>(-42.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.70 (n/a)</td><td>334.14 (n/a)</td><td>277.60 (n/a)</td><td>262.10 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (-7.25%)</td><td>0.06 (-6.70%)</td><td>0.06 (-10.90%)</td><td>0.05 (-2.00%)</td><td>0.00 <b>(-30.24%)</b></td><td>308.90 (+2.05%)</td><td>287.58 (+6.68%)</td><td>290.40 (+12.25%)</td><td>254.00 (+7.81%)</td><td>22.73 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>302.70 (n/a)</td><td>269.56 (n/a)</td><td>258.70 (n/a)</td><td>235.60 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (-9.14%)</td><td>0.05 (-6.78%)</td><td>0.05 (-12.57%)</td><td>0.03 (+9.50%)</td><td>0.01 (-19.93%)</td><td>519.10 (-8.67%)</td><td>364.96 (+3.48%)</td><td>347.90 (+14.37%)</td><td>245.00 (+10.06%)</td><td>106.46 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>568.40 (n/a)</td><td>352.68 (n/a)</td><td>304.20 (n/a)</td><td>222.60 (n/a)</td><td>135.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (-0.18%)</td><td>0.05 (-16.98%)</td><td>0.04 <b>(-35.09%)</b></td><td>0.03 (-12.87%)</td><td>0.02 <b>(+38.50%)</b></td><td>543.30 (+14.77%)</td><td>403.96 <b>(+27.37%)</b></td><td>453.50 <b>(+54.04%)</b></td><td>243.30 (+0.16%)</td><td>137.75 <b>(+51.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.40 (n/a)</td><td>317.16 (n/a)</td><td>294.40 (n/a)</td><td>242.90 (n/a)</td><td>91.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+12.02%)</td><td>0.04 (-2.48%)</td><td>0.04 (-13.92%)</td><td>0.02 <b>(-29.10%)</b></td><td>0.02 <b>(+39.38%)</b></td><td>685.70 <b>(+41.03%)</b></td><td>415.68 (+10.04%)</td><td>416.20 (+16.16%)</td><td>246.90 (-10.74%)</td><td>173.80 <b>(+68.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.20 (n/a)</td><td>377.74 (n/a)</td><td>358.30 (n/a)</td><td>276.60 (n/a)</td><td>102.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (-4.87%)</td><td>0.04 <b>(-32.48%)</b></td><td>0.04 <b>(-40.21%)</b></td><td>0.03 <b>(-49.35%)</b></td><td>0.02 <b>(+169.89%)</b></td><td>584.60 <b>(+97.43%)</b></td><td>426.40 <b>(+62.35%)</b></td><td>425.00 <b>(+67.26%)</b></td><td>244.00 (+5.13%)</td><td>138.80 <b>(+461.28%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>296.10 (n/a)</td><td>262.64 (n/a)</td><td>254.10 (n/a)</td><td>232.10 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 <b>(-37.42%)</b></td><td>0.03 <b>(-22.99%)</b></td><td>0.03 (-17.92%)</td><td>0.03 <b>(+98.89%)</b></td><td>0.01 <b>(-74.21%)</b></td><td>607.40 <b>(-49.72%)</b></td><td>529.86 (-4.50%)</td><td>572.70 <b>(+21.83%)</b></td><td>399.70 <b>(+59.82%)</b></td><td>87.98 <b>(-77.61%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1208.10 (n/a)</td><td>554.84 (n/a)</td><td>470.10 (n/a)</td><td>250.10 (n/a)</td><td>392.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (+2.07%)</td><td>0.05 <b>(-20.33%)</b></td><td>0.04 <b>(-29.73%)</b></td><td>0.04 <b>(-34.36%)</b></td><td>0.01 <b>(+381.34%)</b></td><td>460.80 <b>(+52.33%)</b></td><td>370.90 <b>(+30.04%)</b></td><td>401.10 <b>(+42.33%)</b></td><td>269.50 (-2.04%)</td><td>75.78 <b>(+605.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>302.50 (n/a)</td><td>285.22 (n/a)</td><td>281.80 (n/a)</td><td>275.10 (n/a)</td><td>10.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 <b>(-20.96%)</b></td><td>0.04 (-15.72%)</td><td>0.04 <b>(-28.58%)</b></td><td>0.03 (-0.34%)</td><td>0.01 (-12.60%)</td><td>531.80 (+0.36%)</td><td>406.32 (+18.63%)</td><td>426.10 <b>(+40.03%)</b></td><td>266.00 <b>(+26.49%)</b></td><td>129.39 (+9.07%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.90 (n/a)</td><td>342.52 (n/a)</td><td>304.30 (n/a)</td><td>210.30 (n/a)</td><td>118.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 <b>(+73.49%)</b></td><td>0.06 <b>(+56.76%)</b></td><td>0.06 <b>(+60.90%)</b></td><td>0.03 (+4.49%)</td><td>0.02 <b>(+140.01%)</b></td><td>525.70 (-4.28%)</td><td>311.68 <b>(-30.61%)</b></td><td>292.80 <b>(-37.86%)</b></td><td>174.40 <b>(-42.35%)</b></td><td>130.11 <b>(+42.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>549.20 (n/a)</td><td>449.20 (n/a)</td><td>471.20 (n/a)</td><td>302.50 (n/a)</td><td>91.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+4.42%)</td><td>0.04 (+15.77%)</td><td>0.04 <b>(+37.87%)</b></td><td>0.03 (+0.94%)</td><td>0.02 (+4.79%)</td><td>607.10 (-0.93%)</td><td>421.10 (-12.25%)</td><td>372.60 <b>(-27.45%)</b></td><td>224.50 (-4.22%)</td><td>163.18 (+11.70%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.80 (n/a)</td><td>479.90 (n/a)</td><td>513.60 (n/a)</td><td>234.40 (n/a)</td><td>146.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(-60.77%)</b></td><td>0.03 <b>(-30.39%)</b></td><td>0.03 (+2.58%)</td><td>0.03 (+6.42%)</td><td>0.00 <b>(-96.04%)</b></td><td>509.40 (-6.03%)</td><td>489.44 <b>(+20.30%)</b></td><td>482.30 (-2.53%)</td><td>474.00 <b>(+154.98%)</b></td><td>14.75 <b>(-90.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>542.10 (n/a)</td><td>406.84 (n/a)</td><td>494.80 (n/a)</td><td>185.90 (n/a)</td><td>162.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (-15.57%)</td><td>0.09 (-7.01%)</td><td>0.06 (-19.14%)</td><td>0.06 (-0.59%)</td><td>0.04 (-4.19%)</td><td>545.50 (+0.61%)</td><td>422.52 (+9.67%)</td><td>519.00 <b>(+23.66%)</b></td><td>242.90 (+18.43%)</td><td>156.70 (+19.05%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>542.20 (n/a)</td><td>385.26 (n/a)</td><td>419.70 (n/a)</td><td>205.10 (n/a)</td><td>131.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 <b>(+26.11%)</b></td><td>0.13 <b>(+35.53%)</b></td><td>0.13 <b>(+23.96%)</b></td><td>0.11 <b>(+75.38%)</b></td><td>0.02 <b>(-27.75%)</b></td><td>302.20 <b>(-42.98%)</b></td><td>256.72 <b>(-29.70%)</b></td><td>256.10 (-19.31%)</td><td>209.90 <b>(-20.70%)</b></td><td>35.09 <b>(-67.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>530.00 (n/a)</td><td>365.18 (n/a)</td><td>317.40 (n/a)</td><td>264.70 (n/a)</td><td>108.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 <b>(-29.09%)</b></td><td>0.08 <b>(-32.47%)</b></td><td>0.11 <b>(-24.68%)</b></td><td>0.01 <b>(-81.02%)</b></td><td>0.04 (+5.07%)</td><td>2426.30 <b>(+427.00%)</b></td><td>755.56 <b>(+157.10%)</b></td><td>306.50 <b>(+32.80%)</b></td><td>272.00 <b>(+41.08%)</b></td><td>937.31 <b>(+721.32%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>460.40 (n/a)</td><td>293.88 (n/a)</td><td>230.80 (n/a)</td><td>192.80 (n/a)</td><td>114.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (-19.96%)</td><td>0.09 <b>(-27.11%)</b></td><td>0.06 <b>(-40.98%)</b></td><td>0.05 <b>(-22.43%)</b></td><td>0.04 (-4.94%)</td><td>674.90 <b>(+28.92%)</b></td><td>447.02 <b>(+43.31%)</b></td><td>515.50 <b>(+69.41%)</b></td><td>238.70 <b>(+24.97%)</b></td><td>184.91 <b>(+43.33%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>523.50 (n/a)</td><td>311.92 (n/a)</td><td>304.30 (n/a)</td><td>191.00 (n/a)</td><td>129.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (+19.87%)</td><td>0.09 (+0.63%)</td><td>0.07 (-8.83%)</td><td>0.06 (+13.73%)</td><td>0.05 (+16.02%)</td><td>530.80 (-12.08%)</td><td>407.96 (+0.43%)</td><td>488.40 (+9.68%)</td><td>188.60 (-16.55%)</td><td>154.46 (-6.33%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>603.70 (n/a)</td><td>406.22 (n/a)</td><td>445.30 (n/a)</td><td>226.00 (n/a)</td><td>164.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 <b>(+29.50%)</b></td><td>0.09 (-12.96%)</td><td>0.08 <b>(-34.72%)</b></td><td>0.02 <b>(-71.96%)</b></td><td>0.06 <b>(+63.96%)</b></td><td>1884.40 <b>(+256.69%)</b></td><td>661.50 <b>(+82.11%)</b></td><td>423.80 <b>(+53.16%)</b></td><td>190.80 <b>(-22.78%)</b></td><td>694.16 <b>(+389.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.30 (n/a)</td><td>363.24 (n/a)</td><td>276.70 (n/a)</td><td>247.10 (n/a)</td><td>141.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 <b>(+38.71%)</b></td><td>0.10 (+2.71%)</td><td>0.07 <b>(-41.30%)</b></td><td>0.06 (-12.83%)</td><td>0.06 <b>(+108.07%)</b></td><td>521.30 (+14.72%)</td><td>385.70 (+12.90%)</td><td>489.80 <b>(+70.37%)</b></td><td>180.60 <b>(-27.90%)</b></td><td>171.21 <b>(+73.59%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>454.40 (n/a)</td><td>341.62 (n/a)</td><td>287.50 (n/a)</td><td>250.50 (n/a)</td><td>98.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.19 <b>(+63.91%)</b></td><td>0.09 (-17.00%)</td><td>0.07 <b>(-39.02%)</b></td><td>0.05 <b>(-49.79%)</b></td><td>0.06 <b>(+1274.33%)</b></td><td>623.60 <b>(+99.17%)</b></td><td>435.74 <b>(+46.62%)</b></td><td>487.10 <b>(+64.01%)</b></td><td>172.20 <b>(-39.00%)</b></td><td>167.55 <b>(+1422.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>313.10 (n/a)</td><td>297.18 (n/a)</td><td>297.00 (n/a)</td><td>282.30 (n/a)</td><td>11.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+19.26%)</td><td>0.10 <b>(+45.15%)</b></td><td>0.13 <b>(+107.65%)</b></td><td>0.05 <b>(+195.05%)</b></td><td>0.04 <b>(+20.75%)</b></td><td>630.60 <b>(-66.11%)</b></td><td>384.58 <b>(-45.15%)</b></td><td>243.00 <b>(-51.83%)</b></td><td>236.90 (-16.17%)</td><td>198.89 <b>(-69.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1860.60 (n/a)</td><td>701.10 (n/a)</td><td>504.50 (n/a)</td><td>282.60 (n/a)</td><td>655.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+14.27%)</td><td>0.09 <b>(+20.45%)</b></td><td>0.07 (+13.14%)</td><td>0.06 (-6.60%)</td><td>0.03 <b>(+35.38%)</b></td><td>586.50 (+7.06%)</td><td>398.68 (-13.44%)</td><td>442.90 (-11.61%)</td><td>239.20 (-12.51%)</td><td>140.75 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.80 (n/a)</td><td>460.60 (n/a)</td><td>501.10 (n/a)</td><td>273.40 (n/a)</td><td>112.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 <b>(+71.02%)</b></td><td>0.08 <b>(+48.56%)</b></td><td>0.09 <b>(+48.52%)</b></td><td>0.05 <b>(+43.99%)</b></td><td>0.02 <b>(+95.80%)</b></td><td>680.80 <b>(-30.56%)</b></td><td>442.12 <b>(-30.86%)</b></td><td>374.40 <b>(-32.66%)</b></td><td>306.60 <b>(-41.52%)</b></td><td>151.57 <b>(-21.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>980.40 (n/a)</td><td>639.44 (n/a)</td><td>556.00 (n/a)</td><td>524.30 (n/a)</td><td>192.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (+3.92%)</td><td>0.09 (+9.24%)</td><td>0.09 (-4.64%)</td><td>0.06 <b>(+81.24%)</b></td><td>0.03 <b>(-24.13%)</b></td><td>561.30 <b>(-44.83%)</b></td><td>403.12 <b>(-21.00%)</b></td><td>369.20 (+4.89%)</td><td>281.70 (-3.76%)</td><td>128.24 <b>(-58.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1017.40 (n/a)</td><td>510.30 (n/a)</td><td>352.00 (n/a)</td><td>292.70 (n/a)</td><td>309.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (-8.81%)</td><td>0.07 (-7.82%)</td><td>0.07 (-8.79%)</td><td>0.04 (+0.90%)</td><td>0.02 (+0.65%)</td><td>575.50 (-0.88%)</td><td>402.74 (+9.47%)</td><td>347.30 (+9.63%)</td><td>270.00 (+9.67%)</td><td>141.30 (+7.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.60 (n/a)</td><td>367.90 (n/a)</td><td>316.80 (n/a)</td><td>246.20 (n/a)</td><td>131.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (+9.38%)</td><td>0.12 (-18.37%)</td><td>0.09 <b>(-45.01%)</b></td><td>0.07 <b>(-35.40%)</b></td><td>0.05 <b>(+169.99%)</b></td><td>662.10 <b>(+54.80%)</b></td><td>477.54 <b>(+39.18%)</b></td><td>572.80 <b>(+81.84%)</b></td><td>277.80 (-8.59%)</td><td>183.31 <b>(+258.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>427.70 (n/a)</td><td>343.12 (n/a)</td><td>315.00 (n/a)</td><td>303.90 (n/a)</td><td>51.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.15 (-4.04%)</td><td>2.91 (-17.26%)</td><td>2.63 <b>(-29.81%)</b></td><td>2.49 (-5.92%)</td><td>0.70 (+2.79%)</td><td>4212.80 (+6.29%)</td><td>3729.06 <b>(+21.34%)</b></td><td>3982.50 <b>(+42.48%)</b></td><td>2525.40 (+4.21%)</td><td>687.33 (+9.18%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.33 (n/a)</td><td>3.52 (n/a)</td><td>3.75 (n/a)</td><td>2.65 (n/a)</td><td>0.68 (n/a)</td><td>3963.60 (n/a)</td><td>3073.22 (n/a)</td><td>2795.20 (n/a)</td><td>2423.30 (n/a)</td><td>629.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 <b>(+22.91%)</b></td><td>0.13 (+18.81%)</td><td>0.15 (+10.35%)</td><td>0.08 (+15.53%)</td><td>0.05 (+19.25%)</td><td>512.40 (-13.45%)</td><td>340.24 (-15.92%)</td><td>272.50 (-9.38%)</td><td>227.20 (-18.65%)</td><td>128.87 (-16.37%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>592.00 (n/a)</td><td>404.66 (n/a)</td><td>300.70 (n/a)</td><td>279.30 (n/a)</td><td>154.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+14.38%)</td><td>0.02 <b>(+23.62%)</b></td><td>0.02 (+11.74%)</td><td>0.01 <b>(+50.88%)</b></td><td>0.00 (-19.32%)</td><td>356.10 <b>(-33.71%)</b></td><td>274.74 <b>(-22.03%)</b></td><td>270.60 (-10.52%)</td><td>234.90 (-12.58%)</td><td>48.67 <b>(-54.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.20 (n/a)</td><td>352.38 (n/a)</td><td>302.40 (n/a)</td><td>268.70 (n/a)</td><td>107.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+14.93%)</td><td>0.01 (+9.45%)</td><td>0.02 (+3.18%)</td><td>0.01 (-3.75%)</td><td>0.00 <b>(+28.15%)</b></td><td>549.70 (+3.89%)</td><td>322.38 (-5.74%)</td><td>273.00 (-3.09%)</td><td>239.50 (-12.97%)</td><td>130.04 (+19.41%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.10 (n/a)</td><td>342.02 (n/a)</td><td>281.70 (n/a)</td><td>275.20 (n/a)</td><td>108.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-2.39%)</td><td>0.02 (-5.36%)</td><td>0.02 (+6.72%)</td><td>0.01 (-9.00%)</td><td>0.01 <b>(+23.65%)</b></td><td>557.20 (+9.88%)</td><td>354.56 (+10.06%)</td><td>278.80 (-6.29%)</td><td>244.90 (+2.47%)</td><td>139.68 <b>(+29.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.10 (n/a)</td><td>322.16 (n/a)</td><td>297.50 (n/a)</td><td>239.00 (n/a)</td><td>107.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-9.10%)</td><td>0.02 <b>(+30.03%)</b></td><td>0.02 <b>(+92.15%)</b></td><td>0.01 (-7.09%)</td><td>0.01 (-11.50%)</td><td>576.80 (+7.63%)</td><td>288.02 <b>(-23.07%)</b></td><td>229.10 <b>(-47.96%)</b></td><td>196.30 (+10.03%)</td><td>162.52 (+11.10%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>535.90 (n/a)</td><td>374.38 (n/a)</td><td>440.20 (n/a)</td><td>178.40 (n/a)</td><td>146.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+25.36%)</b></td><td>0.02 (+13.96%)</td><td>0.02 (-2.44%)</td><td>0.01 <b>(+22.79%)</b></td><td>0.01 (+12.96%)</td><td>439.70 (-18.56%)</td><td>332.16 (-13.59%)</td><td>312.50 (+2.49%)</td><td>213.60 <b>(-20.24%)</b></td><td>101.20 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.90 (n/a)</td><td>384.40 (n/a)</td><td>304.90 (n/a)</td><td>267.80 (n/a)</td><td>135.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+38.66%)</b></td><td>0.02 <b>(+49.17%)</b></td><td>0.02 <b>(+69.37%)</b></td><td>0.01 <b>(+78.79%)</b></td><td>0.00 (-0.67%)</td><td>369.00 <b>(-44.07%)</b></td><td>269.00 <b>(-39.24%)</b></td><td>243.50 <b>(-40.97%)</b></td><td>174.80 <b>(-27.86%)</b></td><td>78.91 <b>(-59.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.80 (n/a)</td><td>442.70 (n/a)</td><td>412.50 (n/a)</td><td>242.30 (n/a)</td><td>196.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+123.89%)</b></td><td>0.01 <b>(+23.97%)</b></td><td>0.01 (+6.02%)</td><td>0.00 <b>(-54.93%)</b></td><td>0.01 <b>(+617.81%)</b></td><td>1263.90 <b>(+121.85%)</b></td><td>590.78 (+13.38%)</td><td>517.70 (-5.68%)</td><td>192.90 <b>(-55.33%)</b></td><td>400.13 <b>(+612.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.70 (n/a)</td><td>521.04 (n/a)</td><td>548.90 (n/a)</td><td>431.80 (n/a)</td><td>56.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+64.54%)</b></td><td>0.01 (+4.72%)</td><td>0.02 (+5.12%)</td><td>0.01 <b>(-39.17%)</b></td><td>0.01 <b>(+257.78%)</b></td><td>656.40 <b>(+64.39%)</b></td><td>364.52 <b>(+20.44%)</b></td><td>262.60 (-4.86%)</td><td>160.90 <b>(-39.21%)</b></td><td>207.18 <b>(+269.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>399.30 (n/a)</td><td>302.66 (n/a)</td><td>276.00 (n/a)</td><td>264.70 (n/a)</td><td>56.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-1.02%)</td><td>0.01 <b>(-29.58%)</b></td><td>0.01 <b>(-40.78%)</b></td><td>0.00 <b>(-65.28%)</b></td><td>0.01 <b>(+36.51%)</b></td><td>1752.20 <b>(+188.05%)</b></td><td>730.54 <b>(+89.61%)</b></td><td>580.30 <b>(+68.89%)</b></td><td>263.80 (+1.03%)</td><td>587.95 <b>(+323.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.30 (n/a)</td><td>385.28 (n/a)</td><td>343.60 (n/a)</td><td>261.10 (n/a)</td><td>138.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (-3.95%)</td><td>0.01 (+15.13%)</td><td>0.01 <b>(+76.25%)</b></td><td>0.01 <b>(+36.02%)</b></td><td>0.00 <b>(-20.18%)</b></td><td>586.50 <b>(-26.49%)</b></td><td>369.88 <b>(-20.57%)</b></td><td>291.80 <b>(-43.26%)</b></td><td>245.70 (+4.11%)</td><td>148.75 <b>(-34.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>797.80 (n/a)</td><td>465.68 (n/a)</td><td>514.30 (n/a)</td><td>236.00 (n/a)</td><td>228.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 <b>(-21.51%)</b></td><td>0.01 (-4.53%)</td><td>0.01 (-11.40%)</td><td>0.01 <b>(+32.18%)</b></td><td>0.00 <b>(-65.00%)</b></td><td>457.80 <b>(-24.34%)</b></td><td>411.14 (-4.13%)</td><td>435.80 (+12.87%)</td><td>355.10 <b>(+27.41%)</b></td><td>49.65 <b>(-67.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.10 (n/a)</td><td>428.86 (n/a)</td><td>386.10 (n/a)</td><td>278.70 (n/a)</td><td>152.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (+13.56%)</td><td>0.01 (+13.84%)</td><td>0.01 (+12.98%)</td><td>0.01 (+7.26%)</td><td>0.00 (+18.18%)</td><td>543.90 (-6.77%)</td><td>420.74 (-11.62%)</td><td>432.90 (-11.49%)</td><td>281.70 (-11.94%)</td><td>95.69 (-1.53%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.40 (n/a)</td><td>476.06 (n/a)</td><td>489.10 (n/a)</td><td>319.90 (n/a)</td><td>97.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 <b>(+20.35%)</b></td><td>0.03 (+1.57%)</td><td>0.03 (+15.24%)</td><td>0.02 <b>(-29.08%)</b></td><td>0.01 <b>(+178.96%)</b></td><td>484.70 <b>(+41.02%)</b></td><td>323.56 (+8.53%)</td><td>242.60 (-13.23%)</td><td>217.20 (-16.91%)</td><td>125.01 <b>(+227.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>343.70 (n/a)</td><td>298.12 (n/a)</td><td>279.60 (n/a)</td><td>261.40 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (-7.14%)</td><td>0.04 (+10.35%)</td><td>0.04 <b>(+56.15%)</b></td><td>0.02 (+0.98%)</td><td>0.01 (-8.70%)</td><td>511.50 (-0.97%)</td><td>361.14 (-10.11%)</td><td>302.60 <b>(-35.96%)</b></td><td>243.10 (+7.71%)</td><td>125.31 (-0.63%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.50 (n/a)</td><td>401.76 (n/a)</td><td>472.50 (n/a)</td><td>225.70 (n/a)</td><td>126.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (+1.22%)</td><td>0.03 (+17.78%)</td><td>0.03 <b>(+96.58%)</b></td><td>0.02 (+9.71%)</td><td>0.01 (-7.32%)</td><td>546.10 (-8.85%)</td><td>371.54 (-17.66%)</td><td>280.10 <b>(-49.13%)</b></td><td>228.70 (-1.17%)</td><td>153.58 (-13.98%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.10 (n/a)</td><td>451.22 (n/a)</td><td>550.60 (n/a)</td><td>231.40 (n/a)</td><td>178.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (-0.26%)</td><td>0.02 <b>(-21.43%)</b></td><td>0.02 <b>(-42.33%)</b></td><td>0.01 <b>(-47.16%)</b></td><td>0.01 <b>(+29.11%)</b></td><td>1059.80 <b>(+89.22%)</b></td><td>552.80 <b>(+50.82%)</b></td><td>550.50 <b>(+73.39%)</b></td><td>228.40 (+0.26%)</td><td>324.43 <b>(+135.84%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.10 (n/a)</td><td>366.52 (n/a)</td><td>317.50 (n/a)</td><td>227.80 (n/a)</td><td>137.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (+10.18%)</td><td>0.03 (+8.95%)</td><td>0.03 <b>(+24.02%)</b></td><td>0.01 (+3.57%)</td><td>0.01 <b>(+28.33%)</b></td><td>649.20 (-3.45%)</td><td>373.60 (-2.81%)</td><td>248.80 (-19.35%)</td><td>223.40 (-9.22%)</td><td>196.88 (+10.35%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.40 (n/a)</td><td>384.40 (n/a)</td><td>308.50 (n/a)</td><td>246.10 (n/a)</td><td>178.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 <b>(+30.96%)</b></td><td>0.03 <b>(+25.29%)</b></td><td>0.02 (-0.74%)</td><td>0.02 (-3.53%)</td><td>0.02 <b>(+102.70%)</b></td><td>624.90 (+3.67%)</td><td>431.58 (-8.70%)</td><td>516.50 (+0.74%)</td><td>220.70 <b>(-23.66%)</b></td><td>192.21 <b>(+55.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.80 (n/a)</td><td>472.70 (n/a)</td><td>512.70 (n/a)</td><td>289.10 (n/a)</td><td>123.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-19.67%)</td><td>0.02 (-8.40%)</td><td>0.02 (+4.63%)</td><td>0.01 <b>(-25.54%)</b></td><td>0.01 <b>(-26.15%)</b></td><td>808.20 <b>(+34.30%)</b></td><td>498.42 (+8.31%)</td><td>470.80 (-4.44%)</td><td>289.60 <b>(+24.45%)</b></td><td>190.13 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.80 (n/a)</td><td>460.16 (n/a)</td><td>492.70 (n/a)</td><td>232.70 (n/a)</td><td>145.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (-9.81%)</td><td>0.02 (+3.63%)</td><td>0.02 (+13.48%)</td><td>0.01 (-6.70%)</td><td>0.01 (-19.04%)</td><td>620.50 (+7.17%)</td><td>448.70 (-4.67%)</td><td>440.60 (-11.88%)</td><td>305.00 (+10.87%)</td><td>117.91 (+2.45%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>579.00 (n/a)</td><td>470.68 (n/a)</td><td>500.00 (n/a)</td><td>275.10 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+47.67%)</b></td><td>0.02 <b>(+26.77%)</b></td><td>0.02 (+8.75%)</td><td>0.02 (-2.19%)</td><td>0.01 <b>(+242.66%)</b></td><td>495.90 (+2.25%)</td><td>377.18 (-13.41%)</td><td>422.70 (-8.03%)</td><td>235.80 <b>(-32.28%)</b></td><td>127.80 <b>(+137.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>485.00 (n/a)</td><td>435.60 (n/a)</td><td>459.60 (n/a)</td><td>348.20 (n/a)</td><td>53.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(+40.37%)</b></td><td>0.03 <b>(+83.89%)</b></td><td>0.03 <b>(+64.97%)</b></td><td>0.03 <b>(+445.73%)</b></td><td>0.00 <b>(-56.79%)</b></td><td>355.10 <b>(-81.68%)</b></td><td>321.00 <b>(-59.79%)</b></td><td>324.10 <b>(-39.39%)</b></td><td>280.10 <b>(-28.76%)</b></td><td>32.60 <b>(-94.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1938.10 (n/a)</td><td>798.32 (n/a)</td><td>534.70 (n/a)</td><td>393.20 (n/a)</td><td>643.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 <b>(-34.37%)</b></td><td>0.02 <b>(-20.07%)</b></td><td>0.02 (-16.94%)</td><td>0.01 (-17.56%)</td><td>0.01 <b>(-39.73%)</b></td><td>682.90 <b>(+21.30%)</b></td><td>445.12 (+18.29%)</td><td>357.90 <b>(+20.38%)</b></td><td>290.80 <b>(+52.33%)</b></td><td>171.85 (+3.57%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.00 (n/a)</td><td>376.30 (n/a)</td><td>297.30 (n/a)</td><td>190.90 (n/a)</td><td>165.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(-33.67%)</b></td><td>0.06 (+18.34%)</td><td>0.06 <b>(+87.20%)</b></td><td>0.05 <b>(+85.85%)</b></td><td>0.01 <b>(-77.26%)</b></td><td>299.90 <b>(-46.20%)</b></td><td>265.24 <b>(-32.79%)</b></td><td>265.40 <b>(-46.59%)</b></td><td>233.30 <b>(+50.81%)</b></td><td>31.49 <b>(-82.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>557.40 (n/a)</td><td>394.66 (n/a)</td><td>496.90 (n/a)</td><td>154.70 (n/a)</td><td>176.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (-18.11%)</td><td>0.08 (+2.60%)</td><td>0.09 (+13.14%)</td><td>0.03 <b>(-30.70%)</b></td><td>0.03 (-16.93%)</td><td>777.50 <b>(+44.30%)</b></td><td>371.06 (+0.75%)</td><td>282.10 (-11.60%)</td><td>230.20 <b>(+22.12%)</b></td><td>229.40 <b>(+45.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>538.80 (n/a)</td><td>368.28 (n/a)</td><td>319.10 (n/a)</td><td>188.50 (n/a)</td><td>157.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+0.54%)</td><td>0.05 (+19.11%)</td><td>0.05 <b>(+69.47%)</b></td><td>0.03 <b>(+34.40%)</b></td><td>0.01 (-19.91%)</td><td>484.90 <b>(-25.59%)</b></td><td>361.92 <b>(-21.50%)</b></td><td>316.20 <b>(-41.01%)</b></td><td>244.80 (-0.53%)</td><td>112.43 <b>(-36.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.70 (n/a)</td><td>461.02 (n/a)</td><td>536.00 (n/a)</td><td>246.10 (n/a)</td><td>176.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 <b>(+41.99%)</b></td><td>0.06 <b>(+20.99%)</b></td><td>0.05 (+13.04%)</td><td>0.04 (-6.59%)</td><td>0.02 <b>(+160.14%)</b></td><td>535.40 (+7.04%)</td><td>381.28 (-12.35%)</td><td>382.80 (-11.55%)</td><td>246.20 <b>(-29.56%)</b></td><td>113.52 <b>(+95.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>500.20 (n/a)</td><td>435.00 (n/a)</td><td>432.80 (n/a)</td><td>349.50 (n/a)</td><td>58.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (+3.05%)</td><td>0.05 (+10.02%)</td><td>0.05 <b>(+21.55%)</b></td><td>0.03 (-3.08%)</td><td>0.01 (+13.38%)</td><td>478.60 (+3.17%)</td><td>361.78 (-8.03%)</td><td>350.60 (-17.72%)</td><td>259.20 (-2.96%)</td><td>93.35 (+13.62%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>463.90 (n/a)</td><td>393.38 (n/a)</td><td>426.10 (n/a)</td><td>267.10 (n/a)</td><td>82.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(-22.92%)</b></td><td>0.04 (-4.90%)</td><td>0.04 (-0.48%)</td><td>0.03 <b>(+26.78%)</b></td><td>0.01 <b>(-43.11%)</b></td><td>627.40 <b>(-21.12%)</b></td><td>508.12 (-4.44%)</td><td>530.70 (+0.49%)</td><td>312.20 <b>(+29.76%)</b></td><td>119.59 <b>(-39.61%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>795.40 (n/a)</td><td>531.72 (n/a)</td><td>528.10 (n/a)</td><td>240.60 (n/a)</td><td>198.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (-19.27%)</td><td>0.04 (-1.68%)</td><td>0.06 <b>(+48.74%)</b></td><td>0.01 <b>(-70.01%)</b></td><td>0.02 (+16.66%)</td><td>1898.20 <b>(+233.43%)</b></td><td>636.08 <b>(+56.56%)</b></td><td>290.10 <b>(-32.75%)</b></td><td>262.10 <b>(+23.87%)</b></td><td>709.63 <b>(+420.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.30 (n/a)</td><td>406.28 (n/a)</td><td>431.40 (n/a)</td><td>211.60 (n/a)</td><td>136.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+0.24%)</td><td>0.04 (-7.75%)</td><td>0.04 (-6.94%)</td><td>0.03 (-13.86%)</td><td>0.02 (+10.16%)</td><td>609.10 (+16.09%)</td><td>464.46 (+11.59%)</td><td>511.40 (+7.46%)</td><td>267.60 (-0.26%)</td><td>152.27 <b>(+29.35%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>524.70 (n/a)</td><td>416.22 (n/a)</td><td>475.90 (n/a)</td><td>268.30 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+0.64%)</td><td>0.05 (+12.37%)</td><td>0.06 <b>(+59.85%)</b></td><td>0.03 (-0.15%)</td><td>0.02 (+9.71%)</td><td>490.40 (+0.14%)</td><td>340.46 (-9.47%)</td><td>274.20 <b>(-37.44%)</b></td><td>236.20 (-0.63%)</td><td>123.84 (+10.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>489.70 (n/a)</td><td>376.06 (n/a)</td><td>438.30 (n/a)</td><td>237.70 (n/a)</td><td>111.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+11.90%)</td><td>0.05 (+18.95%)</td><td>0.05 <b>(+46.91%)</b></td><td>0.03 <b>(+42.89%)</b></td><td>0.01 <b>(-23.81%)</b></td><td>553.20 <b>(-30.02%)</b></td><td>404.50 <b>(-23.42%)</b></td><td>396.80 <b>(-31.94%)</b></td><td>261.70 (-10.62%)</td><td>105.08 <b>(-51.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>790.50 (n/a)</td><td>528.24 (n/a)</td><td>583.00 (n/a)</td><td>292.80 (n/a)</td><td>214.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (-11.10%)</td><td>0.04 <b>(-28.49%)</b></td><td>0.03 <b>(-38.54%)</b></td><td>0.03 <b>(-33.32%)</b></td><td>0.02 <b>(+30.14%)</b></td><td>651.40 <b>(+49.95%)</b></td><td>474.56 <b>(+50.24%)</b></td><td>498.00 <b>(+62.69%)</b></td><td>255.10 (+12.48%)</td><td>160.90 <b>(+115.57%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>434.40 (n/a)</td><td>315.86 (n/a)</td><td>306.10 (n/a)</td><td>226.80 (n/a)</td><td>74.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (-2.69%)</td><td>0.11 (-17.17%)</td><td>0.11 (-13.53%)</td><td>0.07 <b>(-39.95%)</b></td><td>0.03 <b>(+116.42%)</b></td><td>478.50 <b>(+66.55%)</b></td><td>327.26 <b>(+26.85%)</b></td><td>299.60 (+15.63%)</td><td>232.40 (+2.74%)</td><td>92.91 <b>(+282.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>287.30 (n/a)</td><td>257.98 (n/a)</td><td>259.10 (n/a)</td><td>226.20 (n/a)</td><td>24.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 <b>(+23.48%)</b></td><td>0.10 (-9.83%)</td><td>0.08 <b>(-27.42%)</b></td><td>0.06 (-6.34%)</td><td>0.04 <b>(+36.31%)</b></td><td>590.00 (+6.77%)</td><td>376.14 (+14.88%)</td><td>391.20 <b>(+37.79%)</b></td><td>206.30 (-19.03%)</td><td>142.31 (+12.22%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>552.60 (n/a)</td><td>327.42 (n/a)</td><td>283.90 (n/a)</td><td>254.80 (n/a)</td><td>126.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 <b>(-47.55%)</b></td><td>0.08 <b>(-37.36%)</b></td><td>0.09 <b>(-35.96%)</b></td><td>0.06 <b>(-26.73%)</b></td><td>0.01 <b>(-71.00%)</b></td><td>680.80 <b>(+36.46%)</b></td><td>523.96 <b>(+46.97%)</b></td><td>473.90 <b>(+56.14%)</b></td><td>450.00 <b>(+90.68%)</b></td><td>95.79 <b>(-27.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>498.90 (n/a)</td><td>356.52 (n/a)</td><td>303.50 (n/a)</td><td>236.00 (n/a)</td><td>131.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (-8.27%)</td><td>0.09 <b>(+31.97%)</b></td><td>0.10 <b>(+44.13%)</b></td><td>0.07 <b>(+397.28%)</b></td><td>0.02 <b>(-44.79%)</b></td><td>481.30 <b>(-79.89%)</b></td><td>367.82 <b>(-54.68%)</b></td><td>344.50 <b>(-30.63%)</b></td><td>275.70 (+9.02%)</td><td>93.28 <b>(-89.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2393.20 (n/a)</td><td>811.64 (n/a)</td><td>496.60 (n/a)</td><td>252.90 (n/a)</td><td>890.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.22 <b>(+117.00%)</b></td><td>0.13 <b>(+55.23%)</b></td><td>0.09 (+17.99%)</td><td>0.08 (+11.31%)</td><td>0.06 <b>(+423.21%)</b></td><td>510.30 (-10.16%)</td><td>378.18 <b>(-25.67%)</b></td><td>439.30 (-15.24%)</td><td>187.60 <b>(-53.92%)</b></td><td>147.20 <b>(+124.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>568.00 (n/a)</td><td>508.76 (n/a)</td><td>518.30 (n/a)</td><td>407.10 (n/a)</td><td>65.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (-3.36%)</td><td>0.10 (-2.07%)</td><td>0.10 (-4.46%)</td><td>0.08 (+8.70%)</td><td>0.02 <b>(-25.74%)</b></td><td>401.10 (-8.00%)</td><td>328.26 (+0.44%)</td><td>330.90 (+4.65%)</td><td>263.70 (+3.49%)</td><td>49.96 <b>(-29.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>436.00 (n/a)</td><td>326.82 (n/a)</td><td>316.20 (n/a)</td><td>254.80 (n/a)</td><td>71.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (+16.48%)</td><td>0.12 <b>(+21.70%)</b></td><td>0.13 <b>(+46.66%)</b></td><td>0.08 <b>(+34.53%)</b></td><td>0.03 <b>(+20.65%)</b></td><td>450.80 <b>(-25.67%)</b></td><td>338.98 (-17.87%)</td><td>276.60 <b>(-31.82%)</b></td><td>248.50 (-14.16%)</td><td>99.29 (-19.61%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>606.50 (n/a)</td><td>412.72 (n/a)</td><td>405.70 (n/a)</td><td>289.50 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 <b>(-24.50%)</b></td><td>0.08 <b>(-22.15%)</b></td><td>0.07 (-1.35%)</td><td>0.02 <b>(-74.23%)</b></td><td>0.04 (-8.52%)</td><td>2061.10 <b>(+288.08%)</b></td><td>705.18 <b>(+88.91%)</b></td><td>457.20 (+1.37%)</td><td>255.10 <b>(+32.45%)</b></td><td>763.89 <b>(+415.46%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>531.10 (n/a)</td><td>373.28 (n/a)</td><td>451.00 (n/a)</td><td>192.60 (n/a)</td><td>148.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (-9.45%)</td><td>0.10 (+15.85%)</td><td>0.10 <b>(+31.87%)</b></td><td>0.07 (+3.38%)</td><td>0.02 (-15.75%)</td><td>512.60 (-3.28%)</td><td>381.68 (-14.94%)</td><td>368.70 <b>(-24.17%)</b></td><td>292.20 (+10.43%)</td><td>95.89 (-8.70%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>530.00 (n/a)</td><td>448.72 (n/a)</td><td>486.20 (n/a)</td><td>264.60 (n/a)</td><td>105.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 <b>(+32.65%)</b></td><td>0.09 (+15.06%)</td><td>0.08 (-13.85%)</td><td>0.06 <b>(+255.53%)</b></td><td>0.04 (-3.99%)</td><td>517.10 <b>(-71.88%)</b></td><td>387.38 <b>(-39.58%)</b></td><td>427.00 (+16.06%)</td><td>220.60 <b>(-24.61%)</b></td><td>121.37 <b>(-81.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1838.60 (n/a)</td><td>641.10 (n/a)</td><td>367.90 (n/a)</td><td>292.60 (n/a)</td><td>670.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 <b>(+46.47%)</b></td><td>0.07 <b>(+51.35%)</b></td><td>0.08 <b>(+74.17%)</b></td><td>0.05 <b>(+22.58%)</b></td><td>0.02 <b>(+69.60%)</b></td><td>436.30 (-18.42%)</td><td>296.82 <b>(-32.59%)</b></td><td>268.10 <b>(-42.59%)</b></td><td>226.80 <b>(-31.71%)</b></td><td>82.59 (-1.28%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>534.80 (n/a)</td><td>440.34 (n/a)</td><td>467.00 (n/a)</td><td>332.10 (n/a)</td><td>83.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (+0.20%)</td><td>0.06 (+4.92%)</td><td>0.06 (+9.93%)</td><td>0.04 (-5.51%)</td><td>0.02 (-2.15%)</td><td>533.90 (+5.83%)</td><td>353.70 (-4.99%)</td><td>371.70 (-9.03%)</td><td>225.30 (-0.22%)</td><td>123.73 (+0.66%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>504.50 (n/a)</td><td>372.28 (n/a)</td><td>408.60 (n/a)</td><td>225.80 (n/a)</td><td>122.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (-1.94%)</td><td>0.07 (+8.09%)</td><td>0.07 <b>(+20.80%)</b></td><td>0.04 (-10.99%)</td><td>0.02 (+3.13%)</td><td>539.60 (+12.35%)</td><td>336.08 (-6.25%)</td><td>277.90 (-17.22%)</td><td>242.10 (+1.98%)</td><td>122.05 (+16.38%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>480.30 (n/a)</td><td>358.50 (n/a)</td><td>335.70 (n/a)</td><td>237.40 (n/a)</td><td>104.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (+16.87%)</td><td>0.05 (+4.59%)</td><td>0.05 (+0.46%)</td><td>0.04 (+6.12%)</td><td>0.02 (+6.30%)</td><td>549.50 (-5.76%)</td><td>409.54 (-5.01%)</td><td>450.00 (-0.46%)</td><td>241.60 (-14.45%)</td><td>126.75 (-11.56%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>583.10 (n/a)</td><td>431.14 (n/a)</td><td>452.10 (n/a)</td><td>282.40 (n/a)</td><td>143.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(-37.97%)</b></td><td>0.06 (+3.02%)</td><td>0.06 <b>(+45.19%)</b></td><td>0.04 <b>(+48.49%)</b></td><td>0.02 <b>(-58.00%)</b></td><td>516.40 <b>(-32.65%)</b></td><td>386.96 (-19.62%)</td><td>357.10 <b>(-31.13%)</b></td><td>278.80 <b>(+61.25%)</b></td><td>109.66 <b>(-49.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>766.70 (n/a)</td><td>481.40 (n/a)</td><td>518.50 (n/a)</td><td>172.90 (n/a)</td><td>219.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 <b>(-33.67%)</b></td><td>0.04 (-16.64%)</td><td>0.04 (-4.83%)</td><td>0.04 (-12.44%)</td><td>0.01 <b>(-60.58%)</b></td><td>582.50 (+14.19%)</td><td>507.64 (+15.30%)</td><td>506.80 (+5.08%)</td><td>409.20 <b>(+50.77%)</b></td><td>68.24 <b>(-30.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>510.10 (n/a)</td><td>440.26 (n/a)</td><td>482.30 (n/a)</td><td>271.40 (n/a)</td><td>97.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (-3.21%)</td><td>0.09 (+7.67%)</td><td>0.09 (+1.07%)</td><td>0.08 <b>(+59.16%)</b></td><td>0.01 <b>(-54.17%)</b></td><td>322.60 <b>(-37.18%)</b></td><td>279.10 (-12.78%)</td><td>279.50 (-1.06%)</td><td>249.00 (+3.32%)</td><td>31.11 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>513.50 (n/a)</td><td>320.00 (n/a)</td><td>282.50 (n/a)</td><td>241.00 (n/a)</td><td>111.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (-14.32%)</td><td>0.05 <b>(-35.68%)</b></td><td>0.05 <b>(-41.33%)</b></td><td>0.01 <b>(-73.31%)</b></td><td>0.03 <b>(+31.87%)</b></td><td>1949.20 <b>(+274.63%)</b></td><td>739.42 <b>(+128.48%)</b></td><td>505.40 <b>(+70.46%)</b></td><td>247.50 (+16.69%)</td><td>690.48 <b>(+495.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>520.30 (n/a)</td><td>323.62 (n/a)</td><td>296.50 (n/a)</td><td>212.10 (n/a)</td><td>115.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (-14.02%)</td><td>0.06 (-9.05%)</td><td>0.05 (+0.55%)</td><td>0.05 (+15.14%)</td><td>0.02 <b>(-35.62%)</b></td><td>545.90 (-13.16%)</td><td>424.20 (+1.57%)</td><td>458.50 (-0.54%)</td><td>279.80 (+16.34%)</td><td>121.49 <b>(-28.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>628.60 (n/a)</td><td>417.66 (n/a)</td><td>461.00 (n/a)</td><td>240.50 (n/a)</td><td>170.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (-12.77%)</td><td>0.06 <b>(-24.84%)</b></td><td>0.05 <b>(-36.57%)</b></td><td>0.04 <b>(-21.27%)</b></td><td>0.02 (-16.35%)</td><td>592.30 <b>(+27.02%)</b></td><td>455.60 <b>(+33.14%)</b></td><td>453.20 <b>(+57.63%)</b></td><td>298.10 (+14.61%)</td><td>119.53 <b>(+22.79%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>466.30 (n/a)</td><td>342.20 (n/a)</td><td>287.50 (n/a)</td><td>260.10 (n/a)</td><td>97.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 <b>(-31.81%)</b></td><td>0.08 <b>(+29.21%)</b></td><td>0.09 <b>(+83.07%)</b></td><td>0.05 <b>(+296.75%)</b></td><td>0.02 <b>(-53.75%)</b></td><td>465.10 <b>(-74.80%)</b></td><td>334.88 <b>(-52.32%)</b></td><td>264.70 <b>(-45.38%)</b></td><td>247.50 <b>(+46.62%)</b></td><td>108.17 <b>(-83.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>1845.40 (n/a)</td><td>702.34 (n/a)</td><td>484.60 (n/a)</td><td>168.80 (n/a)</td><td>655.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (-8.52%)</td><td>0.05 (-17.80%)</td><td>0.05 <b>(-21.19%)</b></td><td>0.04 (-18.32%)</td><td>0.01 (-5.38%)</td><td>596.50 <b>(+22.43%)</b></td><td>470.10 <b>(+22.20%)</b></td><td>469.90 <b>(+26.90%)</b></td><td>315.80 (+9.31%)</td><td>100.74 (+19.42%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>487.20 (n/a)</td><td>384.70 (n/a)</td><td>370.30 (n/a)</td><td>288.90 (n/a)</td><td>84.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (+2.46%)</td><td>0.06 (+13.50%)</td><td>0.06 (+10.74%)</td><td>0.03 (-2.59%)</td><td>0.02 (-2.93%)</td><td>696.90 (+2.67%)</td><td>370.60 (-12.82%)</td><td>303.00 (-9.69%)</td><td>244.80 (-2.39%)</td><td>188.36 (-2.68%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>678.80 (n/a)</td><td>425.10 (n/a)</td><td>335.50 (n/a)</td><td>250.80 (n/a)</td><td>193.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 <b>(+27.19%)</b></td><td>0.07 <b>(+61.87%)</b></td><td>0.07 <b>(+80.52%)</b></td><td>0.04 <b>(+47.25%)</b></td><td>0.01 (+12.98%)</td><td>423.40 <b>(-32.08%)</b></td><td>293.76 <b>(-39.19%)</b></td><td>271.40 <b>(-44.61%)</b></td><td>241.40 <b>(-21.39%)</b></td><td>75.16 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>623.40 (n/a)</td><td>483.04 (n/a)</td><td>490.00 (n/a)</td><td>307.10 (n/a)</td><td>118.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+1.06%)</td><td>0.04 (-1.07%)</td><td>0.04 (+2.94%)</td><td>0.03 <b>(+136.88%)</b></td><td>0.01 <b>(-34.82%)</b></td><td>566.20 <b>(-57.78%)</b></td><td>476.64 <b>(-20.51%)</b></td><td>512.30 (-2.86%)</td><td>279.60 (-1.06%)</td><td>114.55 <b>(-73.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1341.20 (n/a)</td><td>599.64 (n/a)</td><td>527.40 (n/a)</td><td>282.60 (n/a)</td><td>432.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(+41.82%)</b></td><td>0.04 (+14.89%)</td><td>0.04 (+13.43%)</td><td>0.01 <b>(-60.45%)</b></td><td>0.03 <b>(+109.06%)</b></td><td>2526.20 <b>(+152.85%)</b></td><td>810.14 <b>(+48.82%)</b></td><td>419.40 (-11.84%)</td><td>259.10 <b>(-29.50%)</b></td><td>967.27 <b>(+272.37%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>999.10 (n/a)</td><td>544.36 (n/a)</td><td>475.70 (n/a)</td><td>367.50 (n/a)</td><td>259.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (-16.48%)</td><td>0.05 (-3.70%)</td><td>0.05 <b>(+24.14%)</b></td><td>0.03 (-14.85%)</td><td>0.01 <b>(-32.57%)</b></td><td>673.10 (+17.43%)</td><td>423.94 (-0.08%)</td><td>366.60 (-19.45%)</td><td>294.60 (+19.71%)</td><td>146.71 (-1.62%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.20 (n/a)</td><td>424.30 (n/a)</td><td>455.10 (n/a)</td><td>246.10 (n/a)</td><td>149.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (+16.64%)</td><td>0.06 <b>(+30.43%)</b></td><td>0.06 <b>(+51.31%)</b></td><td>0.04 <b>(+36.01%)</b></td><td>0.02 (+15.27%)</td><td>496.20 <b>(-26.47%)</b></td><td>360.74 <b>(-24.02%)</b></td><td>311.30 <b>(-33.91%)</b></td><td>251.10 (-14.27%)</td><td>113.56 <b>(-24.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>674.80 (n/a)</td><td>474.78 (n/a)</td><td>471.00 (n/a)</td><td>292.90 (n/a)</td><td>150.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.36 (+11.40%)</td><td>0.28 (+4.19%)</td><td>0.25 (-14.90%)</td><td>0.19 (+18.01%)</td><td>0.07 (-4.53%)</td><td>506.90 (-15.26%)</td><td>374.44 (-6.04%)</td><td>388.30 (+17.49%)</td><td>269.60 (-10.25%)</td><td>93.02 <b>(-27.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>598.20 (n/a)</td><td>398.50 (n/a)</td><td>330.50 (n/a)</td><td>300.40 (n/a)</td><td>127.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.45 <b>(+94.70%)</b></td><td>0.24 <b>(+20.56%)</b></td><td>0.19 (-10.35%)</td><td>0.17 <b>(+22.26%)</b></td><td>0.12 <b>(+204.55%)</b></td><td>586.20 (-18.20%)</td><td>466.16 (-8.80%)</td><td>522.80 (+11.54%)</td><td>218.00 <b>(-48.63%)</b></td><td>148.75 <b>(+22.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>716.60 (n/a)</td><td>511.14 (n/a)</td><td>468.70 (n/a)</td><td>424.40 (n/a)</td><td>121.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.36 <b>(-39.44%)</b></td><td>0.25 (-9.85%)</td><td>0.23 (+10.36%)</td><td>0.15 (-5.58%)</td><td>0.09 <b>(-47.99%)</b></td><td>650.70 (+5.91%)</td><td>435.48 (+0.38%)</td><td>432.40 (-9.39%)</td><td>276.40 <b>(+65.11%)</b></td><td>159.21 (-7.01%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.59 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>614.40 (n/a)</td><td>433.84 (n/a)</td><td>477.20 (n/a)</td><td>167.40 (n/a)</td><td>171.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.31 (-0.86%)</td><td>0.20 (-2.67%)</td><td>0.20 <b>(+28.98%)</b></td><td>0.09 <b>(-40.94%)</b></td><td>0.10 <b>(+34.38%)</b></td><td>816.30 <b>(+69.32%)</b></td><td>467.46 (+18.98%)</td><td>371.80 <b>(-22.48%)</b></td><td>237.80 (+0.85%)</td><td>258.33 <b>(+111.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>482.10 (n/a)</td><td>392.90 (n/a)</td><td>479.60 (n/a)</td><td>235.80 (n/a)</td><td>121.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.28 (-12.25%)</td><td>0.23 (-2.75%)</td><td>0.24 (-3.59%)</td><td>0.16 (+10.90%)</td><td>0.04 <b>(-43.82%)</b></td><td>455.20 (-9.83%)</td><td>333.52 (-3.87%)</td><td>313.40 (+3.74%)</td><td>267.30 (+13.94%)</td><td>74.95 <b>(-40.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>504.80 (n/a)</td><td>346.96 (n/a)</td><td>302.10 (n/a)</td><td>234.60 (n/a)</td><td>126.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.29 (+8.78%)</td><td>0.15 (-15.12%)</td><td>0.13 (-13.59%)</td><td>0.07 <b>(-47.95%)</b></td><td>0.08 <b>(+35.38%)</b></td><td>1066.40 <b>(+92.11%)</b></td><td>586.12 <b>(+33.64%)</b></td><td>557.80 (+15.73%)</td><td>255.70 (-8.09%)</td><td>296.93 <b>(+130.61%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>555.10 (n/a)</td><td>438.58 (n/a)</td><td>482.00 (n/a)</td><td>278.20 (n/a)</td><td>128.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (-0.43%)</td><td>0.10 (+6.66%)</td><td>0.11 (-11.61%)</td><td>0.09 <b>(+60.33%)</b></td><td>0.02 <b>(-50.93%)</b></td><td>415.80 <b>(-37.62%)</b></td><td>357.84 (-13.78%)</td><td>348.80 (+13.14%)</td><td>307.00 (+0.43%)</td><td>52.32 <b>(-67.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>666.60 (n/a)</td><td>415.04 (n/a)</td><td>308.30 (n/a)</td><td>305.70 (n/a)</td><td>160.99 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+10.36%)</td><td>0.09 (+5.92%)</td><td>0.08 (+13.45%)</td><td>0.05 (-18.91%)</td><td>0.04 <b>(+24.00%)</b></td><td>756.30 <b>(+23.32%)</b></td><td>452.68 (-0.26%)</td><td>453.60 (-11.85%)</td><td>267.30 (-9.39%)</td><td>198.93 <b>(+37.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>613.30 (n/a)</td><td>453.88 (n/a)</td><td>514.60 (n/a)</td><td>295.00 (n/a)</td><td>144.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (+18.39%)</td><td>0.12 <b>(+28.96%)</b></td><td>0.12 <b>(+58.01%)</b></td><td>0.08 (+10.70%)</td><td>0.03 <b>(+23.03%)</b></td><td>443.50 (-9.66%)</td><td>339.14 <b>(-21.43%)</b></td><td>300.60 <b>(-36.72%)</b></td><td>220.70 (-15.54%)</td><td>99.00 (+2.06%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>490.90 (n/a)</td><td>431.66 (n/a)</td><td>475.00 (n/a)</td><td>261.30 (n/a)</td><td>97.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (+6.62%)</td><td>0.11 (+0.83%)</td><td>0.12 (+2.89%)</td><td>0.06 (+3.04%)</td><td>0.04 (+19.84%)</td><td>615.10 (-2.95%)</td><td>399.90 (+3.16%)</td><td>296.50 (-2.82%)</td><td>239.00 (-6.20%)</td><td>178.51 (+13.66%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>633.80 (n/a)</td><td>387.64 (n/a)</td><td>305.10 (n/a)</td><td>254.80 (n/a)</td><td>157.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (-5.01%)</td><td>0.10 (-0.66%)</td><td>0.07 (-10.19%)</td><td>0.06 (+3.02%)</td><td>0.04 (-4.08%)</td><td>652.10 (-2.93%)</td><td>444.22 (-0.92%)</td><td>496.00 (+11.36%)</td><td>262.90 (+5.29%)</td><td>173.09 (-7.90%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>671.80 (n/a)</td><td>448.34 (n/a)</td><td>445.40 (n/a)</td><td>249.70 (n/a)</td><td>187.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (-15.68%)</td><td>0.09 <b>(-25.68%)</b></td><td>0.08 <b>(-38.01%)</b></td><td>0.02 <b>(-72.16%)</b></td><td>0.05 (+9.25%)</td><td>2054.20 <b>(+259.25%)</b></td><td>711.56 <b>(+100.36%)</b></td><td>437.00 <b>(+61.31%)</b></td><td>260.00 (+18.61%)</td><td>758.07 <b>(+389.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>571.80 (n/a)</td><td>355.14 (n/a)</td><td>270.90 (n/a)</td><td>219.20 (n/a)</td><td>154.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 <b>(+58.78%)</b></td><td>0.11 <b>(+45.42%)</b></td><td>0.09 (+2.86%)</td><td>0.08 <b>(+266.20%)</b></td><td>0.04 <b>(+23.78%)</b></td><td>527.40 <b>(-72.69%)</b></td><td>409.90 <b>(-45.93%)</b></td><td>465.00 (-2.78%)</td><td>253.60 <b>(-37.03%)</b></td><td>130.40 <b>(-80.18%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1931.30 (n/a)</td><td>758.10 (n/a)</td><td>478.30 (n/a)</td><td>402.70 (n/a)</td><td>657.80 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (-6.34%)</td><td>0.11 (-17.59%)</td><td>0.14 (-4.07%)</td><td>0.02 <b>(-71.05%)</b></td><td>0.06 <b>(+30.02%)</b></td><td>2498.10 <b>(+245.47%)</b></td><td>762.78 <b>(+107.41%)</b></td><td>300.20 (+4.24%)</td><td>269.20 (+6.74%)</td><td>972.71 <b>(+385.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>723.10 (n/a)</td><td>367.76 (n/a)</td><td>288.00 (n/a)</td><td>252.20 (n/a)</td><td>200.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 <b>(+23.04%)</b></td><td>0.12 <b>(+29.82%)</b></td><td>0.09 (+9.94%)</td><td>0.08 (-1.24%)</td><td>0.05 <b>(+75.72%)</b></td><td>542.70 (+1.25%)</td><td>383.24 (-17.70%)</td><td>446.40 (-9.05%)</td><td>238.60 (-18.73%)</td><td>136.28 <b>(+38.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>536.00 (n/a)</td><td>465.64 (n/a)</td><td>490.80 (n/a)</td><td>293.60 (n/a)</td><td>98.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (+3.46%)</td><td>0.11 (-2.20%)</td><td>0.08 (-13.87%)</td><td>0.07 (+3.45%)</td><td>0.04 (+7.11%)</td><td>582.90 (-3.33%)</td><td>438.36 (+3.67%)</td><td>528.50 (+16.10%)</td><td>252.30 (-3.33%)</td><td>155.52 (+4.88%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>603.00 (n/a)</td><td>422.86 (n/a)</td><td>455.20 (n/a)</td><td>261.00 (n/a)</td><td>148.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 <b>(+80.31%)</b></td><td>0.10 (+16.09%)</td><td>0.08 (-2.21%)</td><td>0.07 (-2.35%)</td><td>0.04 <b>(+389.96%)</b></td><td>549.50 (+2.40%)</td><td>461.76 (-5.15%)</td><td>520.30 (+2.26%)</td><td>233.50 <b>(-44.55%)</b></td><td>131.46 <b>(+170.57%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>536.60 (n/a)</td><td>486.84 (n/a)</td><td>508.80 (n/a)</td><td>421.10 (n/a)</td><td>48.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (+2.42%)</td><td>0.12 (+4.75%)</td><td>0.10 (-3.38%)</td><td>0.07 (-3.98%)</td><td>0.05 (+15.05%)</td><td>561.00 (+4.14%)</td><td>395.92 (-2.36%)</td><td>427.00 (+3.49%)</td><td>239.90 (-2.36%)</td><td>143.30 (+8.10%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>538.70 (n/a)</td><td>405.48 (n/a)</td><td>412.60 (n/a)</td><td>245.70 (n/a)</td><td>132.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (+7.82%)</td><td>0.10 (+1.84%)</td><td>0.11 (+2.32%)</td><td>0.07 (+3.01%)</td><td>0.03 <b>(+32.21%)</b></td><td>468.10 (-2.92%)</td><td>361.48 (+0.28%)</td><td>311.60 (-2.26%)</td><td>279.00 (-7.25%)</td><td>96.82 <b>(+23.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>482.20 (n/a)</td><td>360.48 (n/a)</td><td>318.80 (n/a)</td><td>300.80 (n/a)</td><td>78.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (+13.17%)</td><td>0.08 (-10.71%)</td><td>0.07 (-13.46%)</td><td>0.05 (-5.89%)</td><td>0.03 (+17.88%)</td><td>671.40 (+6.25%)</td><td>513.30 (+14.45%)</td><td>529.40 (+15.54%)</td><td>266.40 (-11.64%)</td><td>155.11 (+9.58%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>631.90 (n/a)</td><td>448.50 (n/a)</td><td>458.20 (n/a)</td><td>301.50 (n/a)</td><td>141.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (-5.32%)</td><td>0.11 (-5.88%)</td><td>0.11 (-16.17%)</td><td>0.07 (-7.96%)</td><td>0.03 (-4.46%)</td><td>515.60 (+8.66%)</td><td>356.58 (+6.21%)</td><td>323.70 (+19.27%)</td><td>236.00 (+5.59%)</td><td>119.84 (+5.00%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>474.50 (n/a)</td><td>335.74 (n/a)</td><td>271.40 (n/a)</td><td>223.50 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 <b>(-49.51%)</b></td><td>0.06 <b>(-39.12%)</b></td><td>0.07 (+1.51%)</td><td>0.02 <b>(-69.98%)</b></td><td>0.02 <b>(-41.77%)</b></td><td>1793.40 <b>(+233.10%)</b></td><td>784.24 <b>(+86.93%)</b></td><td>506.70 (-1.48%)</td><td>477.20 <b>(+98.09%)</b></td><td>567.57 <b>(+289.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>538.40 (n/a)</td><td>419.54 (n/a)</td><td>514.30 (n/a)</td><td>240.90 (n/a)</td><td>145.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (+4.77%)</td><td>0.09 (+1.67%)</td><td>0.07 (-15.77%)</td><td>0.05 <b>(+198.32%)</b></td><td>0.03 <b>(-21.91%)</b></td><td>633.20 <b>(-66.48%)</b></td><td>453.22 <b>(-31.94%)</b></td><td>505.40 (+18.72%)</td><td>267.10 (-4.57%)</td><td>157.05 <b>(-77.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1888.90 (n/a)</td><td>665.96 (n/a)</td><td>425.70 (n/a)</td><td>279.90 (n/a)</td><td>687.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (+6.86%)</td><td>0.07 (-17.46%)</td><td>0.07 (-6.22%)</td><td>0.02 <b>(-72.19%)</b></td><td>0.04 <b>(+35.54%)</b></td><td>1996.80 <b>(+259.52%)</b></td><td>734.54 <b>(+73.96%)</b></td><td>470.50 (+6.64%)</td><td>268.60 (-6.44%)</td><td>711.07 <b>(+445.87%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>555.40 (n/a)</td><td>422.24 (n/a)</td><td>441.20 (n/a)</td><td>287.10 (n/a)</td><td>130.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.49 (+3.05%)</td><td>0.34 (-6.34%)</td><td>0.29 <b>(-37.41%)</b></td><td>0.26 <b>(+23.03%)</b></td><td>0.11 <b>(-25.54%)</b></td><td>513.70 (-18.72%)</td><td>408.18 (-1.60%)</td><td>448.90 <b>(+59.75%)</b></td><td>267.00 (-2.98%)</td><td>113.25 <b>(-39.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.47 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>632.00 (n/a)</td><td>414.80 (n/a)</td><td>281.00 (n/a)</td><td>275.20 (n/a)</td><td>188.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.46 <b>(+41.78%)</b></td><td>0.32 <b>(+26.55%)</b></td><td>0.27 (+14.80%)</td><td>0.24 <b>(+21.37%)</b></td><td>0.09 <b>(+70.04%)</b></td><td>535.30 (-17.61%)</td><td>433.76 (-19.16%)</td><td>487.00 (-12.90%)</td><td>287.70 <b>(-29.45%)</b></td><td>107.04 (-0.47%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>649.70 (n/a)</td><td>536.56 (n/a)</td><td>559.10 (n/a)</td><td>407.80 (n/a)</td><td>107.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.53 (-2.41%)</td><td>0.37 (+14.13%)</td><td>0.28 (+16.74%)</td><td>0.22 (+10.19%)</td><td>0.15 (-4.48%)</td><td>594.40 (-9.24%)</td><td>406.16 (-15.42%)</td><td>463.80 (-14.33%)</td><td>245.40 (+2.51%)</td><td>151.04 <b>(-20.46%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.55 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>654.90 (n/a)</td><td>480.22 (n/a)</td><td>541.40 (n/a)</td><td>239.40 (n/a)</td><td>189.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+56.43%)</b></td><td>0.01 <b>(+30.18%)</b></td><td>0.01 (+10.59%)</td><td>0.01 (+10.71%)</td><td>0.00 <b>(+198.03%)</b></td><td>418.50 (-9.67%)</td><td>313.20 (-18.12%)</td><td>318.20 (-9.58%)</td><td>212.50 <b>(-36.07%)</b></td><td>95.99 <b>(+69.03%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.30 (n/a)</td><td>382.50 (n/a)</td><td>351.90 (n/a)</td><td>332.40 (n/a)</td><td>56.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (+14.28%)</td><td>0.01 (+17.39%)</td><td>0.02 (+11.33%)</td><td>0.01 (-8.18%)</td><td>0.00 (+14.51%)</td><td>616.60 (+8.90%)</td><td>334.00 (-12.26%)</td><td>266.60 (-10.18%)</td><td>240.00 (-12.50%)</td><td>158.97 (+18.11%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.20 (n/a)</td><td>380.66 (n/a)</td><td>296.80 (n/a)</td><td>274.30 (n/a)</td><td>134.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+32.65%)</b></td><td>0.01 <b>(+28.52%)</b></td><td>0.01 <b>(+46.41%)</b></td><td>0.01 (+18.28%)</td><td>0.00 <b>(+65.59%)</b></td><td>562.10 (-15.46%)</td><td>379.42 (-17.41%)</td><td>280.10 <b>(-31.68%)</b></td><td>243.90 <b>(-24.61%)</b></td><td>160.65 (+10.88%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>664.90 (n/a)</td><td>459.38 (n/a)</td><td>410.00 (n/a)</td><td>323.50 (n/a)</td><td>144.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>8.79 (-0.87%)</td><td>6.88 (+2.92%)</td><td>7.26 (-2.53%)</td><td>3.47 (-12.35%)</td><td>2.01 (+1.45%)</td><td>604.40 (+14.10%)</td><td>339.52 (-0.70%)</td><td>289.10 (+2.59%)</td><td>238.70 (+0.89%)</td><td>149.67 <b>(+24.57%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>8.87 (n/a)</td><td>6.68 (n/a)</td><td>7.44 (n/a)</td><td>3.96 (n/a)</td><td>1.98 (n/a)</td><td>529.70 (n/a)</td><td>341.92 (n/a)</td><td>281.80 (n/a)</td><td>236.60 (n/a)</td><td>120.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.67 (-7.45%)</td><td>0.48 (-4.57%)</td><td>0.57 (+12.87%)</td><td>0.23 <b>(-30.14%)</b></td><td>0.18 <b>(+26.39%)</b></td><td>566.90 <b>(+43.12%)</b></td><td>318.70 (+14.22%)</td><td>233.60 (-11.41%)</td><td>198.00 (+8.02%)</td><td>152.63 <b>(+98.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.72 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.14 (n/a)</td><td>396.10 (n/a)</td><td>279.02 (n/a)</td><td>263.70 (n/a)</td><td>183.30 (n/a)</td><td>76.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.58 (+8.71%)</td><td>0.48 (+19.49%)</td><td>0.54 (+10.02%)</td><td>0.26 (+3.50%)</td><td>0.13 (-7.27%)</td><td>508.20 (-3.38%)</td><td>298.26 (-18.46%)</td><td>245.80 (-9.13%)</td><td>229.70 (-8.01%)</td><td>118.39 (-17.32%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.49 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>526.00 (n/a)</td><td>365.78 (n/a)</td><td>270.50 (n/a)</td><td>249.70 (n/a)</td><td>143.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.53 (+5.47%)</td><td>0.44 (+15.72%)</td><td>0.51 (+13.61%)</td><td>0.32 <b>(+49.65%)</b></td><td>0.11 (-16.85%)</td><td>414.30 <b>(-33.18%)</b></td><td>316.02 (-18.79%)</td><td>257.50 (-12.00%)</td><td>249.80 (-5.16%)</td><td>85.40 <b>(-46.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>620.00 (n/a)</td><td>389.14 (n/a)</td><td>292.60 (n/a)</td><td>263.40 (n/a)</td><td>158.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.56 (+15.78%)</td><td>0.42 (+19.15%)</td><td>0.46 (+3.12%)</td><td>0.27 <b>(+126.74%)</b></td><td>0.13 <b>(-26.26%)</b></td><td>481.10 <b>(-55.89%)</b></td><td>344.58 <b>(-32.79%)</b></td><td>286.20 (-3.05%)</td><td>235.10 (-13.63%)</td><td>113.19 <b>(-68.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.45 (n/a)</td><td>0.12 (n/a)</td><td>0.17 (n/a)</td><td>1090.80 (n/a)</td><td>512.72 (n/a)</td><td>295.20 (n/a)</td><td>272.20 (n/a)</td><td>357.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.64 <b>(+29.90%)</b></td><td>0.51 <b>(+29.63%)</b></td><td>0.50 <b>(+29.78%)</b></td><td>0.40 <b>(+47.94%)</b></td><td>0.09 (+1.16%)</td><td>331.90 <b>(-32.42%)</b></td><td>266.76 <b>(-24.44%)</b></td><td>264.00 <b>(-22.94%)</b></td><td>205.50 <b>(-23.03%)</b></td><td>44.99 <b>(-48.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>491.10 (n/a)</td><td>353.06 (n/a)</td><td>342.60 (n/a)</td><td>267.00 (n/a)</td><td>87.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 <b>(+26.38%)</b></td><td>0.01 (+8.61%)</td><td>0.01 (-5.34%)</td><td>0.01 (+4.59%)</td><td>0.01 <b>(+35.07%)</b></td><td>723.70 (-4.39%)</td><td>425.14 (-3.55%)</td><td>374.20 (+5.65%)</td><td>222.10 <b>(-20.88%)</b></td><td>206.06 (+3.23%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>756.90 (n/a)</td><td>440.78 (n/a)</td><td>354.20 (n/a)</td><td>280.70 (n/a)</td><td>199.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (-12.91%)</td><td>0.01 (-1.61%)</td><td>0.01 (-9.42%)</td><td>0.01 <b>(+48.10%)</b></td><td>0.00 <b>(-70.92%)</b></td><td>333.60 <b>(-32.47%)</b></td><td>305.02 (-4.15%)</td><td>299.40 (+10.40%)</td><td>278.20 (+14.82%)</td><td>21.94 <b>(-78.37%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.00 (n/a)</td><td>318.22 (n/a)</td><td>271.20 (n/a)</td><td>242.30 (n/a)</td><td>101.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.00 <b>(-62.50%)</b></td><td>0.00 <b>(-47.62%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-83.33%)</b></td><td>22035.99 (+9.01%)</td><td>18632.01 <b>(+38.25%)</b></td><td>19035.50 <b>(+20.59%)</b></td><td>14801.57 <b>(+189.92%)</b></td><td>2737.83 <b>(-60.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20215.49 (n/a)</td><td>13476.99 (n/a)</td><td>15784.77 (n/a)</td><td>5105.37 (n/a)</td><td>7002.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.00 (-16.67%)</td><td>0.00 (-8.33%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (-1.98%)</td><td>22520.44 <b>(+30.09%)</b></td><td>15168.15 (+14.39%)</td><td>16093.07 (-2.23%)</td><td>7815.52 (+15.83%)</td><td>6792.07 <b>(+33.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17311.09 (n/a)</td><td>13260.14 (n/a)</td><td>16460.05 (n/a)</td><td>6747.20 (n/a)</td><td>5095.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 <b>(+25.99%)</b></td><td>0.10 (+4.69%)</td><td>0.08 (-3.83%)</td><td>0.07 (+0.95%)</td><td>0.03 <b>(+50.25%)</b></td><td>28213.40 (-0.93%)</td><td>23078.94 (-2.46%)</td><td>25316.44 (+3.93%)</td><td>14917.12 <b>(-20.59%)</b></td><td>5198.55 (+16.46%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28477.79 (n/a)</td><td>23660.22 (n/a)</td><td>24359.21 (n/a)</td><td>18785.56 (n/a)</td><td>4463.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.68 (-9.35%)</td><td>1.52 <b>(-29.06%)</b></td><td>1.57 <b>(-22.95%)</b></td><td>0.32 <b>(-79.94%)</b></td><td>0.84 <b>(+46.99%)</b></td><td>3300.90 <b>(+398.63%)</b></td><td>1153.12 <b>(+122.70%)</b></td><td>668.90 <b>(+29.78%)</b></td><td>391.80 (+10.30%)</td><td>1209.09 <b>(+821.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.95 (n/a)</td><td>2.14 (n/a)</td><td>2.03 (n/a)</td><td>1.58 (n/a)</td><td>0.57 (n/a)</td><td>662.00 (n/a)</td><td>517.78 (n/a)</td><td>515.40 (n/a)</td><td>355.20 (n/a)</td><td>131.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.98 (-1.17%)</td><td>1.28 <b>(-37.42%)</b></td><td>1.06 <b>(-37.21%)</b></td><td>0.30 <b>(-79.17%)</b></td><td>1.09 <b>(+64.31%)</b></td><td>3493.40 <b>(+380.06%)</b></td><td>1590.62 <b>(+188.20%)</b></td><td>990.60 <b>(+59.29%)</b></td><td>351.80 (+1.18%)</td><td>1344.28 <b>(+747.64%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.02 (n/a)</td><td>2.05 (n/a)</td><td>1.69 (n/a)</td><td>1.44 (n/a)</td><td>0.67 (n/a)</td><td>727.70 (n/a)</td><td>551.92 (n/a)</td><td>621.90 (n/a)</td><td>347.70 (n/a)</td><td>158.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.58 (+15.96%)</td><td>2.08 (+18.34%)</td><td>1.84 (+10.06%)</td><td>1.62 <b>(+22.43%)</b></td><td>0.45 <b>(+20.37%)</b></td><td>647.30 (-18.32%)</td><td>523.76 (-15.51%)</td><td>569.20 (-9.15%)</td><td>406.70 (-13.76%)</td><td>108.75 (-17.64%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.22 (n/a)</td><td>1.75 (n/a)</td><td>1.67 (n/a)</td><td>1.32 (n/a)</td><td>0.38 (n/a)</td><td>792.50 (n/a)</td><td>619.92 (n/a)</td><td>626.50 (n/a)</td><td>471.60 (n/a)</td><td>132.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.18 (-5.39%)</td><td>1.85 (-10.21%)</td><td>1.53 <b>(-29.88%)</b></td><td>1.39 <b>(+361.05%)</b></td><td>0.75 <b>(-35.28%)</b></td><td>752.30 <b>(-78.31%)</b></td><td>619.30 <b>(-40.97%)</b></td><td>684.30 <b>(+42.62%)</b></td><td>329.80 (+5.71%)</td><td>166.81 <b>(-87.71%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.36 (n/a)</td><td>2.06 (n/a)</td><td>2.19 (n/a)</td><td>0.30 (n/a)</td><td>1.15 (n/a)</td><td>3468.50 (n/a)</td><td>1049.04 (n/a)</td><td>479.80 (n/a)</td><td>312.00 (n/a)</td><td>1356.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.67 <b>(-23.77%)</b></td><td>2.53 (-13.07%)</td><td>2.83 (-1.02%)</td><td>0.60 (-2.32%)</td><td>1.28 (-17.84%)</td><td>3512.10 (+2.37%)</td><td>1294.86 (+8.17%)</td><td>741.10 (+1.02%)</td><td>570.80 <b>(+31.16%)</b></td><td>1254.98 (-0.18%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>4.82 (n/a)</td><td>2.91 (n/a)</td><td>2.86 (n/a)</td><td>0.61 (n/a)</td><td>1.55 (n/a)</td><td>3430.70 (n/a)</td><td>1197.08 (n/a)</td><td>733.60 (n/a)</td><td>435.20 (n/a)</td><td>1257.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.92 (-13.17%)</td><td>3.29 <b>(+28.58%)</b></td><td>3.03 <b>(+20.69%)</b></td><td>2.31 <b>(+298.85%)</b></td><td>1.05 <b>(-50.71%)</b></td><td>908.10 <b>(-74.93%)</b></td><td>686.12 <b>(-61.62%)</b></td><td>691.40 (-17.15%)</td><td>426.00 (+15.17%)</td><td>194.21 <b>(-88.07%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.67 (n/a)</td><td>2.56 (n/a)</td><td>2.51 (n/a)</td><td>0.58 (n/a)</td><td>2.13 (n/a)</td><td>3621.90 (n/a)</td><td>1787.48 (n/a)</td><td>834.50 (n/a)</td><td>369.90 (n/a)</td><td>1627.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.38 <b>(+30.91%)</b></td><td>3.87 <b>(+34.93%)</b></td><td>2.95 (+18.45%)</td><td>0.58 (-1.50%)</td><td>2.70 (+13.12%)</td><td>3632.40 (+1.52%)</td><td>1156.42 <b>(-33.72%)</b></td><td>710.00 (-15.58%)</td><td>284.30 <b>(-23.62%)</b></td><td>1401.22 (-15.34%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.64 (n/a)</td><td>2.87 (n/a)</td><td>2.49 (n/a)</td><td>0.59 (n/a)</td><td>2.39 (n/a)</td><td>3578.10 (n/a)</td><td>1744.68 (n/a)</td><td>841.00 (n/a)</td><td>372.20 (n/a)</td><td>1655.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.07 <b>(-38.32%)</b></td><td>2.70 (-19.43%)</td><td>2.53 (-5.42%)</td><td>0.61 (+5.38%)</td><td>1.37 <b>(-39.69%)</b></td><td>3421.50 (-5.10%)</td><td>1232.20 (+2.13%)</td><td>829.90 (+5.72%)</td><td>515.40 <b>(+62.13%)</b></td><td>1233.22 (-9.25%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.60 (n/a)</td><td>3.35 (n/a)</td><td>2.67 (n/a)</td><td>0.58 (n/a)</td><td>2.27 (n/a)</td><td>3605.50 (n/a)</td><td>1206.52 (n/a)</td><td>785.00 (n/a)</td><td>317.90 (n/a)</td><td>1358.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.22 (-5.07%)</td><td>4.22 (-10.75%)</td><td>3.72 <b>(-26.90%)</b></td><td>2.43 (-4.05%)</td><td>1.86 <b>(+24.25%)</b></td><td>863.40 (+4.21%)</td><td>583.98 (+18.59%)</td><td>563.20 <b>(+36.80%)</b></td><td>337.20 (+5.34%)</td><td>250.41 <b>(+25.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.55 (n/a)</td><td>4.72 (n/a)</td><td>5.09 (n/a)</td><td>2.53 (n/a)</td><td>1.49 (n/a)</td><td>828.50 (n/a)</td><td>492.44 (n/a)</td><td>411.70 (n/a)</td><td>320.10 (n/a)</td><td>199.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.19 <b>(+36.08%)</b></td><td>2.52 (-17.17%)</td><td>1.99 <b>(-42.80%)</b></td><td>0.62 <b>(-65.86%)</b></td><td>1.71 <b>(+103.57%)</b></td><td>3407.90 <b>(+192.90%)</b></td><td>1341.30 <b>(+80.33%)</b></td><td>1052.00 <b>(+74.84%)</b></td><td>404.40 <b>(-26.51%)</b></td><td>1191.79 <b>(+364.57%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.81 (n/a)</td><td>3.05 (n/a)</td><td>3.49 (n/a)</td><td>1.80 (n/a)</td><td>0.84 (n/a)</td><td>1163.50 (n/a)</td><td>743.80 (n/a)</td><td>601.70 (n/a)</td><td>550.30 (n/a)</td><td>256.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.35 (-6.44%)</td><td>3.95 <b>(+24.55%)</b></td><td>4.08 <b>(+21.39%)</b></td><td>1.14 (+3.04%)</td><td>1.67 (-8.85%)</td><td>3672.00 (-2.95%)</td><td>1466.96 <b>(-20.85%)</b></td><td>1026.90 (-17.62%)</td><td>783.80 (+6.87%)</td><td>1237.92 (-1.53%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>5.72 (n/a)</td><td>3.17 (n/a)</td><td>3.36 (n/a)</td><td>1.11 (n/a)</td><td>1.84 (n/a)</td><td>3783.50 (n/a)</td><td>1853.50 (n/a)</td><td>1246.50 (n/a)</td><td>733.40 (n/a)</td><td>1257.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.57 (-18.59%)</td><td>3.57 <b>(-46.51%)</b></td><td>3.30 <b>(-50.56%)</b></td><td>1.10 <b>(-64.92%)</b></td><td>2.70 (+11.38%)</td><td>3825.50 <b>(+185.04%)</b></td><td>2018.18 <b>(+177.23%)</b></td><td>1272.00 <b>(+102.26%)</b></td><td>554.40 <b>(+22.85%)</b></td><td>1547.40 <b>(+329.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>9.29 (n/a)</td><td>6.67 (n/a)</td><td>6.67 (n/a)</td><td>3.13 (n/a)</td><td>2.42 (n/a)</td><td>1342.10 (n/a)</td><td>727.98 (n/a)</td><td>628.90 (n/a)</td><td>451.30 (n/a)</td><td>359.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.84 <b>(-35.32%)</b></td><td>3.63 <b>(-34.18%)</b></td><td>3.42 <b>(-43.22%)</b></td><td>1.98 (+14.96%)</td><td>1.40 <b>(-59.07%)</b></td><td>2122.20 (-13.01%)</td><td>1301.74 (+9.20%)</td><td>1227.10 <b>(+76.13%)</b></td><td>718.30 <b>(+54.61%)</b></td><td>513.15 <b>(-43.38%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>9.03 (n/a)</td><td>5.52 (n/a)</td><td>6.02 (n/a)</td><td>1.72 (n/a)</td><td>3.43 (n/a)</td><td>2439.70 (n/a)</td><td>1192.08 (n/a)</td><td>696.70 (n/a)</td><td>464.60 (n/a)</td><td>906.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>9.30 (-18.77%)</td><td>3.13 <b>(-31.15%)</b></td><td>1.96 (-7.33%)</td><td>1.13 (-3.76%)</td><td>3.48 <b>(-22.63%)</b></td><td>3720.80 (+3.91%)</td><td>2395.82 (+19.74%)</td><td>2141.10 (+7.91%)</td><td>451.00 <b>(+23.09%)</b></td><td>1359.57 (-10.25%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>11.45 (n/a)</td><td>4.54 (n/a)</td><td>2.11 (n/a)</td><td>1.17 (n/a)</td><td>4.50 (n/a)</td><td>3580.90 (n/a)</td><td>2000.92 (n/a)</td><td>1984.10 (n/a)</td><td>366.40 (n/a)</td><td>1514.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>10.96 (+9.58%)</td><td>7.61 (+6.19%)</td><td>7.79 (+15.28%)</td><td>4.14 (-1.34%)</td><td>3.31 <b>(+37.90%)</b></td><td>1012.40 (+1.36%)</td><td>656.62 (+1.60%)</td><td>538.10 (-13.25%)</td><td>382.70 (-8.75%)</td><td>307.93 <b>(+31.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>10.00 (n/a)</td><td>7.16 (n/a)</td><td>6.76 (n/a)</td><td>4.20 (n/a)</td><td>2.40 (n/a)</td><td>998.80 (n/a)</td><td>646.30 (n/a)</td><td>620.30 (n/a)</td><td>419.40 (n/a)</td><td>234.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>9.26 <b>(+36.47%)</b></td><td>5.61 <b>(+44.02%)</b></td><td>6.66 <b>(+77.47%)</b></td><td>1.11 (-10.97%)</td><td>3.12 (+16.29%)</td><td>3791.30 (+12.32%)</td><td>1302.08 <b>(-28.41%)</b></td><td>629.80 <b>(-43.65%)</b></td><td>453.10 <b>(-26.73%)</b></td><td>1408.20 (-0.47%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>6.78 (n/a)</td><td>3.90 (n/a)</td><td>3.75 (n/a)</td><td>1.24 (n/a)</td><td>2.69 (n/a)</td><td>3375.50 (n/a)</td><td>1818.68 (n/a)</td><td>1117.60 (n/a)</td><td>618.40 (n/a)</td><td>1414.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.71 (+0.88%)</td><td>1.43 (+2.20%)</td><td>1.51 (+1.50%)</td><td>0.91 (+11.01%)</td><td>0.33 (-0.99%)</td><td>573.10 (-9.92%)</td><td>386.46 (-3.28%)</td><td>347.10 (-1.48%)</td><td>306.40 (-0.87%)</td><td>110.91 (-17.01%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.70 (n/a)</td><td>1.40 (n/a)</td><td>1.49 (n/a)</td><td>0.82 (n/a)</td><td>0.34 (n/a)</td><td>636.20 (n/a)</td><td>399.58 (n/a)</td><td>352.30 (n/a)</td><td>309.10 (n/a)</td><td>133.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.45 (+0.21%)</td><td>1.74 (+11.23%)</td><td>1.63 (+5.87%)</td><td>1.37 <b>(+347.14%)</b></td><td>0.43 <b>(-52.32%)</b></td><td>765.20 <b>(-77.63%)</b></td><td>628.84 <b>(-46.76%)</b></td><td>644.10 (-5.54%)</td><td>428.50 (-0.21%)</td><td>134.06 <b>(-89.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>2.44 (n/a)</td><td>1.56 (n/a)</td><td>1.54 (n/a)</td><td>0.31 (n/a)</td><td>0.91 (n/a)</td><td>3421.30 (n/a)</td><td>1181.16 (n/a)</td><td>681.90 (n/a)</td><td>429.40 (n/a)</td><td>1269.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.22 (-11.45%)</td><td>2.04 (+11.36%)</td><td>2.21 (+3.48%)</td><td>0.83 <b>(+43.95%)</b></td><td>1.16 (-9.56%)</td><td>2513.10 <b>(-30.53%)</b></td><td>1455.72 <b>(-24.74%)</b></td><td>948.30 (-3.35%)</td><td>651.30 (+12.94%)</td><td>959.95 <b>(-36.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>3.64 (n/a)</td><td>1.83 (n/a)</td><td>2.14 (n/a)</td><td>0.58 (n/a)</td><td>1.28 (n/a)</td><td>3617.70 (n/a)</td><td>1934.38 (n/a)</td><td>981.20 (n/a)</td><td>576.70 (n/a)</td><td>1513.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.73 (+5.22%)</td><td>1.40 <b>(+33.31%)</b></td><td>1.70 <b>(+68.68%)</b></td><td>0.89 <b>(+25.41%)</b></td><td>0.42 (+19.24%)</td><td>591.50 <b>(-20.26%)</b></td><td>407.52 <b>(-24.32%)</b></td><td>309.10 <b>(-40.72%)</b></td><td>303.80 (-4.97%)</td><td>140.07 (-9.37%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>1.64 (n/a)</td><td>1.05 (n/a)</td><td>1.01 (n/a)</td><td>0.71 (n/a)</td><td>0.35 (n/a)</td><td>741.80 (n/a)</td><td>538.48 (n/a)</td><td>521.40 (n/a)</td><td>319.70 (n/a)</td><td>154.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (+5.82%)</td><td>0.08 (-15.30%)</td><td>0.07 <b>(-24.24%)</b></td><td>0.05 (+1.27%)</td><td>0.03 (+15.69%)</td><td>600.50 (-1.25%)</td><td>458.78 <b>(+20.06%)</b></td><td>448.60 <b>(+31.98%)</b></td><td>238.20 (-5.48%)</td><td>143.83 (+2.96%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.10 (n/a)</td><td>382.12 (n/a)</td><td>339.90 (n/a)</td><td>252.00 (n/a)</td><td>139.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 <b>(+46.77%)</b></td><td>0.09 <b>(+32.74%)</b></td><td>0.11 <b>(+36.60%)</b></td><td>0.06 (+16.72%)</td><td>0.03 <b>(+95.07%)</b></td><td>591.50 (-14.33%)</td><td>391.40 <b>(-20.40%)</b></td><td>307.40 <b>(-26.79%)</b></td><td>270.40 <b>(-31.87%)</b></td><td>146.34 (+15.11%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>690.40 (n/a)</td><td>491.68 (n/a)</td><td>419.90 (n/a)</td><td>396.90 (n/a)</td><td>127.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.21 <b>(-22.00%)</b></td><td>0.17 (-16.44%)</td><td>0.14 <b>(-32.83%)</b></td><td>0.14 (-7.09%)</td><td>0.04 <b>(-25.08%)</b></td><td>479.90 (+7.63%)</td><td>406.36 (+18.31%)</td><td>456.00 <b>(+48.87%)</b></td><td>317.00 <b>(+28.18%)</b></td><td>81.09 (-1.65%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>445.90 (n/a)</td><td>343.48 (n/a)</td><td>306.30 (n/a)</td><td>247.30 (n/a)</td><td>82.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 <b>(-28.47%)</b></td><td>0.13 (-19.58%)</td><td>0.13 (+0.72%)</td><td>0.11 (+3.29%)</td><td>0.03 <b>(-60.79%)</b></td><td>589.50 (-3.19%)</td><td>504.16 (+11.53%)</td><td>508.30 (-0.72%)</td><td>360.30 <b>(+39.81%)</b></td><td>87.92 <b>(-48.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>608.90 (n/a)</td><td>452.04 (n/a)</td><td>512.00 (n/a)</td><td>257.70 (n/a)</td><td>171.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.32 <b>(+68.73%)</b></td><td>0.16 (+4.26%)</td><td>0.12 <b>(-22.40%)</b></td><td>0.12 (+4.16%)</td><td>0.09 <b>(+218.64%)</b></td><td>542.90 (-4.00%)</td><td>459.62 (+7.47%)</td><td>532.20 <b>(+28.86%)</b></td><td>206.00 <b>(-40.72%)</b></td><td>143.93 <b>(+72.58%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>565.50 (n/a)</td><td>427.66 (n/a)</td><td>413.00 (n/a)</td><td>347.50 (n/a)</td><td>83.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.47 (+4.38%)</td><td>0.39 <b>(+38.91%)</b></td><td>0.42 <b>(+67.91%)</b></td><td>0.27 <b>(+41.17%)</b></td><td>0.09 (-8.84%)</td><td>477.40 <b>(-29.17%)</b></td><td>354.36 <b>(-30.07%)</b></td><td>312.90 <b>(-40.46%)</b></td><td>281.40 (-4.22%)</td><td>88.60 <b>(-35.18%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>674.00 (n/a)</td><td>506.76 (n/a)</td><td>525.50 (n/a)</td><td>293.80 (n/a)</td><td>136.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.26 <b>(-45.70%)</b></td><td>0.21 <b>(-23.33%)</b></td><td>0.22 (-13.79%)</td><td>0.13 <b>(-31.91%)</b></td><td>0.05 <b>(-56.96%)</b></td><td>985.40 <b>(+46.88%)</b></td><td>650.12 <b>(+25.39%)</b></td><td>604.10 (+15.99%)</td><td>513.30 <b>(+84.18%)</b></td><td>191.60 <b>(+29.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>670.90 (n/a)</td><td>518.46 (n/a)</td><td>520.80 (n/a)</td><td>278.70 (n/a)</td><td>147.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.54 (-4.83%)</td><td>0.36 <b>(+21.54%)</b></td><td>0.39 <b>(+43.14%)</b></td><td>0.07 (+8.29%)</td><td>0.20 (+10.82%)</td><td>1902.10 (-7.66%)</td><td>645.34 (-12.48%)</td><td>332.70 <b>(-30.15%)</b></td><td>241.80 (+5.04%)</td><td>710.66 (-4.83%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.57 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.06 (n/a)</td><td>0.18 (n/a)</td><td>2059.90 (n/a)</td><td>737.38 (n/a)</td><td>476.30 (n/a)</td><td>230.20 (n/a)</td><td>746.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 <b>(-35.44%)</b></td><td>0.03 <b>(-29.54%)</b></td><td>0.03 <b>(-34.50%)</b></td><td>0.03 (-9.93%)</td><td>0.01 <b>(-64.35%)</b></td><td>620.10 (+11.03%)</td><td>496.14 <b>(+31.91%)</b></td><td>472.20 <b>(+52.67%)</b></td><td>397.30 <b>(+54.89%)</b></td><td>82.94 <b>(-38.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:08:13</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.50 (n/a)</td><td>376.12 (n/a)</td><td>309.30 (n/a)</td><td>256.50 (n/a)</td><td>134.56 (n/a)</td>
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
