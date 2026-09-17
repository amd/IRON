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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+9.99%)</td><td>0.02 <b>(+29.08%)</b></td><td>0.03 <b>(+41.07%)</b></td><td>0.02 <b>(+61.49%)</b></td><td>0.00 <b>(-44.17%)</b></td><td>308.00 <b>(-38.07%)</b></td><td>265.96 <b>(-26.85%)</b></td><td>245.50 <b>(-29.13%)</b></td><td>233.20 (-9.08%)</td><td>34.82 <b>(-67.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>497.30 (n/a)</td><td>363.58 (n/a)</td><td>346.40 (n/a)</td><td>256.50 (n/a)</td><td>107.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(-21.12%)</b></td><td>0.02 <b>(+31.62%)</b></td><td>0.02 <b>(+88.14%)</b></td><td>0.02 <b>(+102.27%)</b></td><td>0.00 <b>(-69.63%)</b></td><td>295.10 <b>(-50.56%)</b></td><td>259.78 <b>(-39.12%)</b></td><td>257.80 <b>(-46.86%)</b></td><td>212.80 <b>(+26.74%)</b></td><td>35.66 <b>(-81.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>426.74 (n/a)</td><td>485.10 (n/a)</td><td>167.90 (n/a)</td><td>192.23 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+0.53%)</td><td>0.02 (-4.66%)</td><td>0.01 (-0.18%)</td><td>0.01 <b>(-58.47%)</b></td><td>0.01 <b>(+55.57%)</b></td><td>1123.40 <b>(+140.81%)</b></td><td>503.14 <b>(+33.50%)</b></td><td>426.30 (+0.19%)</td><td>238.70 (-0.54%)</td><td>363.59 <b>(+246.01%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>466.50 (n/a)</td><td>376.88 (n/a)</td><td>425.50 (n/a)</td><td>240.00 (n/a)</td><td>105.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+26.88%)</b></td><td>0.02 (-18.42%)</td><td>0.01 <b>(-32.08%)</b></td><td>0.00 <b>(-79.82%)</b></td><td>0.01 <b>(+217.85%)</b></td><td>2109.10 <b>(+395.56%)</b></td><td>711.06 <b>(+130.21%)</b></td><td>418.50 <b>(+47.20%)</b></td><td>211.90 <b>(-21.20%)</b></td><td>795.99 <b>(+1110.50%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>425.60 (n/a)</td><td>308.88 (n/a)</td><td>284.30 (n/a)</td><td>268.90 (n/a)</td><td>65.76 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+22.32%)</b></td><td>0.02 (+6.75%)</td><td>0.01 <b>(-23.03%)</b></td><td>0.01 (+8.38%)</td><td>0.01 <b>(+23.54%)</b></td><td>598.60 (-7.74%)</td><td>404.12 (-4.69%)</td><td>474.20 <b>(+29.92%)</b></td><td>209.70 (-18.28%)</td><td>167.66 (-8.77%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.80 (n/a)</td><td>424.00 (n/a)</td><td>365.00 (n/a)</td><td>256.60 (n/a)</td><td>183.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+8.24%)</td><td>0.02 (-3.99%)</td><td>0.01 (+5.47%)</td><td>0.01 (+8.70%)</td><td>0.01 (-2.61%)</td><td>611.40 (-8.00%)</td><td>434.28 (+2.81%)</td><td>447.20 (-5.17%)</td><td>212.00 (-7.63%)</td><td>179.30 (-4.41%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.60 (n/a)</td><td>422.42 (n/a)</td><td>471.60 (n/a)</td><td>229.50 (n/a)</td><td>187.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 <b>(+22.75%)</b></td><td>0.04 (+19.27%)</td><td>0.04 <b>(+28.56%)</b></td><td>0.02 <b>(-35.01%)</b></td><td>0.01 <b>(+138.95%)</b></td><td>654.90 <b>(+53.88%)</b></td><td>365.92 (-5.87%)</td><td>315.80 <b>(-22.22%)</b></td><td>236.10 (-18.53%)</td><td>171.55 <b>(+204.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>425.60 (n/a)</td><td>388.74 (n/a)</td><td>406.00 (n/a)</td><td>289.80 (n/a)</td><td>56.35 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (+10.33%)</td><td>0.04 (-11.22%)</td><td>0.03 <b>(-42.72%)</b></td><td>0.02 <b>(-26.37%)</b></td><td>0.02 (+18.83%)</td><td>642.20 <b>(+35.83%)</b></td><td>393.20 (+19.22%)</td><td>424.00 <b>(+74.56%)</b></td><td>204.60 (-9.39%)</td><td>175.79 <b>(+35.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>329.82 (n/a)</td><td>242.90 (n/a)</td><td>225.80 (n/a)</td><td>129.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (-0.01%)</td><td>0.04 (-2.63%)</td><td>0.05 (-2.48%)</td><td>0.03 (+8.25%)</td><td>0.01 (-8.72%)</td><td>465.30 (-7.62%)</td><td>296.08 (+0.58%)</td><td>252.00 (+2.56%)</td><td>229.20 (+0.00%)</td><td>98.10 (-16.64%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.70 (n/a)</td><td>294.38 (n/a)</td><td>245.70 (n/a)</td><td>229.20 (n/a)</td><td>117.69 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (-0.94%)</td><td>0.04 <b>(-20.86%)</b></td><td>0.03 <b>(-32.48%)</b></td><td>0.02 <b>(-44.40%)</b></td><td>0.01 <b>(+209.42%)</b></td><td>561.50 <b>(+79.85%)</b></td><td>394.58 <b>(+42.03%)</b></td><td>418.50 <b>(+48.09%)</b></td><td>239.70 (+0.97%)</td><td>146.80 <b>(+440.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>312.20 (n/a)</td><td>277.82 (n/a)</td><td>282.60 (n/a)</td><td>237.40 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (+13.21%)</td><td>0.03 (+14.71%)</td><td>0.03 (+16.74%)</td><td>0.02 (+17.43%)</td><td>0.01 (+15.53%)</td><td>514.20 (-14.84%)</td><td>390.82 (-12.71%)</td><td>430.90 (-14.33%)</td><td>254.70 (-11.65%)</td><td>117.34 (-12.40%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>603.80 (n/a)</td><td>447.74 (n/a)</td><td>503.00 (n/a)</td><td>288.30 (n/a)</td><td>133.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (-3.71%)</td><td>0.04 (-5.16%)</td><td>0.04 (+14.45%)</td><td>0.02 (-4.51%)</td><td>0.01 (-7.07%)</td><td>531.30 (+4.71%)</td><td>372.64 (+5.70%)</td><td>308.70 (-12.62%)</td><td>248.70 (+3.84%)</td><td>125.35 (+10.18%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.40 (n/a)</td><td>352.56 (n/a)</td><td>353.30 (n/a)</td><td>239.50 (n/a)</td><td>113.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-6.29%)</td><td>0.08 (-7.56%)</td><td>0.08 (-14.44%)</td><td>0.06 <b>(+29.23%)</b></td><td>0.01 <b>(-37.26%)</b></td><td>398.30 <b>(-22.62%)</b></td><td>323.02 (+2.43%)</td><td>318.70 (+16.87%)</td><td>245.80 (+6.73%)</td><td>56.29 <b>(-51.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>514.70 (n/a)</td><td>315.36 (n/a)</td><td>272.70 (n/a)</td><td>230.30 (n/a)</td><td>115.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-4.98%)</td><td>0.07 (-7.72%)</td><td>0.07 (+5.55%)</td><td>0.04 <b>(-32.87%)</b></td><td>0.03 (+17.23%)</td><td>651.30 <b>(+48.94%)</b></td><td>408.60 (+15.37%)</td><td>371.10 (-5.26%)</td><td>239.80 (+5.22%)</td><td>164.89 <b>(+81.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>437.30 (n/a)</td><td>354.16 (n/a)</td><td>391.70 (n/a)</td><td>227.90 (n/a)</td><td>90.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-16.65%)</td><td>0.07 (-15.63%)</td><td>0.06 <b>(-29.34%)</b></td><td>0.04 (-19.85%)</td><td>0.03 (-18.75%)</td><td>666.00 <b>(+24.77%)</b></td><td>420.82 (+16.29%)</td><td>414.20 <b>(+41.51%)</b></td><td>245.20 (+19.96%)</td><td>170.73 (+8.23%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>533.80 (n/a)</td><td>361.88 (n/a)</td><td>292.70 (n/a)</td><td>204.40 (n/a)</td><td>157.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-1.20%)</td><td>0.06 (-14.93%)</td><td>0.06 (-11.22%)</td><td>0.03 <b>(-52.00%)</b></td><td>0.03 <b>(+46.62%)</b></td><td>977.40 <b>(+108.31%)</b></td><td>506.40 <b>(+42.68%)</b></td><td>423.10 (+12.65%)</td><td>244.80 (+1.20%)</td><td>303.67 <b>(+201.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>469.20 (n/a)</td><td>354.92 (n/a)</td><td>375.60 (n/a)</td><td>241.90 (n/a)</td><td>100.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (+6.95%)</td><td>0.06 (-8.37%)</td><td>0.05 (-15.41%)</td><td>0.04 (-5.62%)</td><td>0.02 <b>(+35.52%)</b></td><td>547.50 (+5.96%)</td><td>458.78 (+12.06%)</td><td>487.20 (+18.22%)</td><td>274.90 (-6.53%)</td><td>106.82 <b>(+30.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>516.70 (n/a)</td><td>409.42 (n/a)</td><td>412.10 (n/a)</td><td>294.10 (n/a)</td><td>82.09 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (-3.78%)</td><td>0.08 (-12.94%)</td><td>0.08 (-11.94%)</td><td>0.05 (+2.92%)</td><td>0.03 (+4.66%)</td><td>501.80 (-2.83%)</td><td>359.40 (+16.02%)</td><td>295.50 (+13.57%)</td><td>229.20 (+3.90%)</td><td>126.26 (+6.43%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>516.40 (n/a)</td><td>309.78 (n/a)</td><td>260.20 (n/a)</td><td>220.60 (n/a)</td><td>118.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (+17.78%)</td><td>0.13 <b>(+21.26%)</b></td><td>0.09 (-1.61%)</td><td>0.08 <b>(+38.46%)</b></td><td>0.05 <b>(+34.62%)</b></td><td>600.00 <b>(-27.78%)</b></td><td>440.54 (-16.13%)</td><td>522.20 (+1.62%)</td><td>252.80 (-15.11%)</td><td>159.38 (-18.60%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>830.80 (n/a)</td><td>525.28 (n/a)</td><td>513.90 (n/a)</td><td>297.80 (n/a)</td><td>195.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 <b>(-25.49%)</b></td><td>0.10 <b>(-22.22%)</b></td><td>0.10 (-8.36%)</td><td>0.08 (-7.84%)</td><td>0.02 <b>(-49.70%)</b></td><td>643.10 (+8.52%)</td><td>526.82 <b>(+23.16%)</b></td><td>513.80 (+9.13%)</td><td>397.80 <b>(+34.21%)</b></td><td>98.27 <b>(-21.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>592.60 (n/a)</td><td>427.74 (n/a)</td><td>470.80 (n/a)</td><td>296.40 (n/a)</td><td>125.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.28 <b>(+55.73%)</b></td><td>0.13 <b>(+22.87%)</b></td><td>0.10 (-2.55%)</td><td>0.08 <b>(+28.89%)</b></td><td>0.08 <b>(+90.25%)</b></td><td>620.60 <b>(-22.42%)</b></td><td>470.08 (-11.19%)</td><td>512.00 (+2.61%)</td><td>177.60 <b>(-35.79%)</b></td><td>172.62 (-8.77%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>799.90 (n/a)</td><td>529.32 (n/a)</td><td>499.00 (n/a)</td><td>276.60 (n/a)</td><td>189.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-16.83%)</td><td>0.12 (-0.14%)</td><td>0.12 (+14.17%)</td><td>0.09 <b>(+74.99%)</b></td><td>0.02 <b>(-56.00%)</b></td><td>559.30 <b>(-42.85%)</b></td><td>433.72 (-15.86%)</td><td>422.30 (-12.42%)</td><td>324.60 <b>(+20.22%)</b></td><td>87.43 <b>(-69.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>978.70 (n/a)</td><td>515.50 (n/a)</td><td>482.20 (n/a)</td><td>270.00 (n/a)</td><td>283.27 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.20 (+9.00%)</td><td>0.13 <b>(+54.04%)</b></td><td>0.09 (-4.26%)</td><td>0.08 <b>(+235.92%)</b></td><td>0.06 (-4.64%)</td><td>622.10 <b>(-70.23%)</b></td><td>447.34 <b>(-58.30%)</b></td><td>560.10 (+4.44%)</td><td>242.10 (-8.26%)</td><td>186.55 <b>(-78.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2089.90 (n/a)</td><td>1072.88 (n/a)</td><td>536.30 (n/a)</td><td>263.90 (n/a)</td><td>884.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-13.56%)</td><td>0.13 (-13.64%)</td><td>0.13 <b>(-20.96%)</b></td><td>0.09 <b>(-21.23%)</b></td><td>0.03 (-19.72%)</td><td>575.60 <b>(+26.95%)</b></td><td>400.06 (+15.72%)</td><td>380.00 <b>(+26.50%)</b></td><td>321.40 (+15.69%)</td><td>101.34 <b>(+23.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>453.40 (n/a)</td><td>345.72 (n/a)</td><td>300.40 (n/a)</td><td>277.80 (n/a)</td><td>81.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (+9.57%)</td><td>0.01 <b>(+22.21%)</b></td><td>0.01 (+13.80%)</td><td>0.00 <b>(+92.62%)</b></td><td>0.00 (-19.28%)</td><td>535.30 <b>(-48.08%)</b></td><td>324.32 <b>(-30.55%)</b></td><td>258.80 (-12.12%)</td><td>245.40 (-8.74%)</td><td>122.51 <b>(-62.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1031.00 (n/a)</td><td>466.98 (n/a)</td><td>294.50 (n/a)</td><td>268.90 (n/a)</td><td>323.35 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 <b>(-33.91%)</b></td><td>0.01 <b>(-30.41%)</b></td><td>0.01 <b>(-34.09%)</b></td><td>0.00 <b>(-51.13%)</b></td><td>0.00 <b>(-26.94%)</b></td><td>1063.80 <b>(+104.62%)</b></td><td>539.08 <b>(+56.53%)</b></td><td>453.00 <b>(+51.71%)</b></td><td>255.70 <b>(+51.30%)</b></td><td>318.19 <b>(+133.08%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.90 (n/a)</td><td>344.40 (n/a)</td><td>298.60 (n/a)</td><td>169.00 (n/a)</td><td>136.52 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (+1.33%)</td><td>0.01 (+8.55%)</td><td>0.01 (+2.13%)</td><td>0.00 (-19.35%)</td><td>0.00 <b>(+33.21%)</b></td><td>633.40 <b>(+24.00%)</b></td><td>404.74 (-2.19%)</td><td>428.60 (-2.08%)</td><td>252.70 (-1.33%)</td><td>155.73 <b>(+60.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.80 (n/a)</td><td>413.82 (n/a)</td><td>437.70 (n/a)</td><td>256.10 (n/a)</td><td>96.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-10.92%)</td><td>0.01 (-1.79%)</td><td>0.01 (+11.28%)</td><td>0.01 (-0.48%)</td><td>0.00 (-18.90%)</td><td>515.30 (+0.49%)</td><td>390.04 (-0.62%)</td><td>395.70 (-10.13%)</td><td>267.40 (+12.26%)</td><td>111.15 (-9.96%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.80 (n/a)</td><td>392.48 (n/a)</td><td>440.30 (n/a)</td><td>238.20 (n/a)</td><td>123.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-4.89%)</td><td>0.01 (-9.89%)</td><td>0.01 <b>(-31.40%)</b></td><td>0.01 (+14.91%)</td><td>0.00 (-11.82%)</td><td>507.90 (-12.99%)</td><td>391.18 (+8.00%)</td><td>439.60 <b>(+45.76%)</b></td><td>261.60 (+5.14%)</td><td>107.05 <b>(-21.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>583.70 (n/a)</td><td>362.22 (n/a)</td><td>301.60 (n/a)</td><td>248.80 (n/a)</td><td>136.82 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+53.36%)</b></td><td>0.01 <b>(+20.23%)</b></td><td>0.00 (-9.03%)</td><td>0.00 (+17.46%)</td><td>0.00 <b>(+87.43%)</b></td><td>662.30 (-14.86%)</td><td>450.20 (-6.81%)</td><td>544.70 (+9.91%)</td><td>164.10 <b>(-34.78%)</b></td><td>198.88 (+2.15%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>777.90 (n/a)</td><td>483.10 (n/a)</td><td>495.60 (n/a)</td><td>251.60 (n/a)</td><td>194.71 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-12.10%)</td><td>0.02 (-13.59%)</td><td>0.02 <b>(-21.14%)</b></td><td>0.01 (-8.90%)</td><td>0.00 <b>(-31.94%)</b></td><td>496.00 (+9.76%)</td><td>366.26 (+11.72%)</td><td>328.20 <b>(+26.82%)</b></td><td>272.50 (+13.78%)</td><td>92.73 (-15.52%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>451.90 (n/a)</td><td>327.84 (n/a)</td><td>258.80 (n/a)</td><td>239.50 (n/a)</td><td>109.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(-21.65%)</b></td><td>0.01 <b>(-23.64%)</b></td><td>0.01 <b>(-37.43%)</b></td><td>0.01 (-10.03%)</td><td>0.00 <b>(-44.09%)</b></td><td>628.70 (+11.16%)</td><td>454.82 <b>(+21.14%)</b></td><td>440.00 <b>(+59.83%)</b></td><td>301.70 <b>(+27.62%)</b></td><td>120.68 <b>(-24.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>375.46 (n/a)</td><td>275.30 (n/a)</td><td>236.40 (n/a)</td><td>160.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 <b>(-54.42%)</b></td><td>0.01 <b>(-42.06%)</b></td><td>0.01 <b>(-32.06%)</b></td><td>0.00 <b>(-73.95%)</b></td><td>0.00 <b>(-40.59%)</b></td><td>2091.30 <b>(+283.87%)</b></td><td>824.90 <b>(+115.65%)</b></td><td>545.60 <b>(+47.18%)</b></td><td>443.80 <b>(+119.38%)</b></td><td>710.32 <b>(+461.28%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>382.52 (n/a)</td><td>370.70 (n/a)</td><td>202.30 (n/a)</td><td>126.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-11.22%)</td><td>0.01 <b>(-20.12%)</b></td><td>0.01 (-11.64%)</td><td>0.01 (-18.78%)</td><td>0.00 (-16.93%)</td><td>655.50 <b>(+23.12%)</b></td><td>534.80 <b>(+24.64%)</b></td><td>546.70 (+13.19%)</td><td>326.30 (+12.63%)</td><td>135.76 (+14.51%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.40 (n/a)</td><td>429.08 (n/a)</td><td>483.00 (n/a)</td><td>289.70 (n/a)</td><td>118.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+55.91%)</b></td><td>0.02 (+12.16%)</td><td>0.01 <b>(-22.93%)</b></td><td>0.01 (-7.34%)</td><td>0.01 <b>(+76.01%)</b></td><td>629.60 (+7.94%)</td><td>395.32 (-4.19%)</td><td>424.00 <b>(+29.74%)</b></td><td>194.10 <b>(-35.88%)</b></td><td>162.85 (+18.62%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.30 (n/a)</td><td>412.60 (n/a)</td><td>326.80 (n/a)</td><td>302.70 (n/a)</td><td>137.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+83.82%)</b></td><td>0.01 <b>(+42.96%)</b></td><td>0.01 (+19.35%)</td><td>0.01 <b>(+200.76%)</b></td><td>0.01 <b>(+65.32%)</b></td><td>634.00 <b>(-66.75%)</b></td><td>462.74 <b>(-40.64%)</b></td><td>444.10 (-16.22%)</td><td>220.50 <b>(-45.58%)</b></td><td>161.51 <b>(-74.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1906.70 (n/a)</td><td>779.54 (n/a)</td><td>530.10 (n/a)</td><td>405.20 (n/a)</td><td>632.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (+10.88%)</td><td>0.03 <b>(+31.54%)</b></td><td>0.04 <b>(+55.68%)</b></td><td>0.02 (+7.93%)</td><td>0.01 <b>(+28.43%)</b></td><td>519.90 (-7.34%)</td><td>349.40 <b>(-22.65%)</b></td><td>292.10 <b>(-35.77%)</b></td><td>274.60 (-9.82%)</td><td>104.53 (+9.96%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>451.74 (n/a)</td><td>454.80 (n/a)</td><td>304.50 (n/a)</td><td>95.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (-14.86%)</td><td>0.03 (+5.33%)</td><td>0.03 <b>(+57.80%)</b></td><td>0.02 (-1.76%)</td><td>0.01 <b>(-36.09%)</b></td><td>575.00 (+1.79%)</td><td>364.30 (-12.44%)</td><td>308.20 <b>(-36.64%)</b></td><td>246.40 (+17.45%)</td><td>127.59 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>416.04 (n/a)</td><td>486.40 (n/a)</td><td>209.80 (n/a)</td><td>165.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (+11.62%)</td><td>0.03 (-14.81%)</td><td>0.02 <b>(-34.68%)</b></td><td>0.01 <b>(-40.97%)</b></td><td>0.01 <b>(+59.22%)</b></td><td>825.60 <b>(+69.39%)</b></td><td>489.88 <b>(+35.32%)</b></td><td>463.70 <b>(+53.09%)</b></td><td>247.30 (-10.40%)</td><td>241.65 <b>(+132.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.40 (n/a)</td><td>362.02 (n/a)</td><td>302.90 (n/a)</td><td>276.00 (n/a)</td><td>104.04 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (-11.39%)</td><td>0.03 (-16.21%)</td><td>0.03 (-3.55%)</td><td>0.01 <b>(-75.71%)</b></td><td>0.01 <b>(+42.62%)</b></td><td>1899.30 <b>(+311.73%)</b></td><td>647.42 <b>(+90.96%)</b></td><td>330.40 (+3.67%)</td><td>243.80 (+12.87%)</td><td>706.13 <b>(+594.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.30 (n/a)</td><td>339.04 (n/a)</td><td>318.70 (n/a)</td><td>216.00 (n/a)</td><td>101.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+41.59%)</b></td><td>0.03 <b>(+50.46%)</b></td><td>0.02 (+5.56%)</td><td>0.02 <b>(+322.52%)</b></td><td>0.01 <b>(+23.09%)</b></td><td>515.80 <b>(-76.33%)</b></td><td>394.92 <b>(-50.96%)</b></td><td>485.20 (-5.25%)</td><td>237.50 <b>(-29.38%)</b></td><td>138.40 <b>(-82.10%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2179.40 (n/a)</td><td>805.24 (n/a)</td><td>512.10 (n/a)</td><td>336.30 (n/a)</td><td>773.31 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+26.51%)</b></td><td>0.03 <b>(+29.16%)</b></td><td>0.03 (+15.36%)</td><td>0.02 <b>(+25.85%)</b></td><td>0.01 <b>(+42.34%)</b></td><td>500.80 <b>(-20.55%)</b></td><td>397.26 <b>(-21.82%)</b></td><td>414.90 (-13.31%)</td><td>285.40 <b>(-20.94%)</b></td><td>97.78 (-13.91%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.30 (n/a)</td><td>508.14 (n/a)</td><td>478.60 (n/a)</td><td>361.00 (n/a)</td><td>113.58 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(-32.23%)</b></td><td>0.05 <b>(-22.50%)</b></td><td>0.05 (+2.96%)</td><td>0.03 (-11.51%)</td><td>0.01 <b>(-48.63%)</b></td><td>625.70 (+13.00%)</td><td>488.30 (+19.14%)</td><td>460.00 (-2.87%)</td><td>309.60 <b>(+47.57%)</b></td><td>135.68 (-13.15%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>553.70 (n/a)</td><td>409.86 (n/a)</td><td>473.60 (n/a)</td><td>209.80 (n/a)</td><td>156.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (-4.78%)</td><td>0.06 <b>(+23.05%)</b></td><td>0.06 <b>(+39.68%)</b></td><td>0.04 (+7.96%)</td><td>0.02 (-18.59%)</td><td>500.10 (-7.39%)</td><td>353.64 <b>(-21.71%)</b></td><td>353.50 <b>(-28.41%)</b></td><td>233.90 (+5.03%)</td><td>106.44 (-18.67%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>540.00 (n/a)</td><td>451.72 (n/a)</td><td>493.80 (n/a)</td><td>222.70 (n/a)</td><td>130.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (-13.39%)</td><td>0.06 (-3.66%)</td><td>0.06 (+14.67%)</td><td>0.03 (-12.75%)</td><td>0.02 (-9.67%)</td><td>725.50 (+14.61%)</td><td>448.66 (+5.26%)</td><td>380.00 (-12.80%)</td><td>248.30 (+15.49%)</td><td>207.32 <b>(+20.48%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>633.00 (n/a)</td><td>426.22 (n/a)</td><td>435.80 (n/a)</td><td>215.00 (n/a)</td><td>172.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 <b>(-46.88%)</b></td><td>0.04 <b>(-23.81%)</b></td><td>0.04 (-7.02%)</td><td>0.02 <b>(-41.91%)</b></td><td>0.01 <b>(-52.39%)</b></td><td>1073.80 <b>(+72.14%)</b></td><td>627.72 <b>(+28.40%)</b></td><td>554.50 (+7.54%)</td><td>445.20 <b>(+88.25%)</b></td><td>256.86 <b>(+70.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.80 (n/a)</td><td>488.88 (n/a)</td><td>515.60 (n/a)</td><td>236.50 (n/a)</td><td>150.26 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 <b>(-20.61%)</b></td><td>0.05 (-17.24%)</td><td>0.05 (-3.53%)</td><td>0.02 <b>(-50.15%)</b></td><td>0.02 (-6.58%)</td><td>1089.40 <b>(+100.63%)</b></td><td>538.28 <b>(+35.83%)</b></td><td>406.60 (+3.65%)</td><td>272.60 <b>(+25.97%)</b></td><td>325.16 <b>(+152.75%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>543.00 (n/a)</td><td>396.30 (n/a)</td><td>392.30 (n/a)</td><td>216.40 (n/a)</td><td>128.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 <b>(+68.91%)</b></td><td>0.06 <b>(+51.06%)</b></td><td>0.07 <b>(+67.15%)</b></td><td>0.03 (-1.06%)</td><td>0.03 <b>(+269.53%)</b></td><td>650.20 (+1.07%)</td><td>405.40 <b>(-23.24%)</b></td><td>309.40 <b>(-40.18%)</b></td><td>243.90 <b>(-40.80%)</b></td><td>192.71 <b>(+119.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>643.30 (n/a)</td><td>528.12 (n/a)</td><td>517.20 (n/a)</td><td>412.00 (n/a)</td><td>87.75 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>525.60 (n/a)</td><td>351.36 (n/a)</td><td>287.20 (n/a)</td><td>249.00 (n/a)</td><td>118.07 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.00 (n/a)</td><td>452.06 (n/a)</td><td>465.80 (n/a)</td><td>270.30 (n/a)</td><td>107.20 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.70 (n/a)</td><td>473.92 (n/a)</td><td>529.20 (n/a)</td><td>204.30 (n/a)</td><td>164.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>555.10 (n/a)</td><td>454.80 (n/a)</td><td>503.40 (n/a)</td><td>261.90 (n/a)</td><td>116.10 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1883.50 (n/a)</td><td>644.44 (n/a)</td><td>391.20 (n/a)</td><td>222.70 (n/a)</td><td>702.14 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.20 (n/a)</td><td>439.86 (n/a)</td><td>505.10 (n/a)</td><td>230.00 (n/a)</td><td>133.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>585.40 (n/a)</td><td>474.24 (n/a)</td><td>493.00 (n/a)</td><td>326.40 (n/a)</td><td>105.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>594.50 (n/a)</td><td>363.78 (n/a)</td><td>270.50 (n/a)</td><td>229.70 (n/a)</td><td>162.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>577.80 (n/a)</td><td>462.72 (n/a)</td><td>469.10 (n/a)</td><td>229.20 (n/a)</td><td>140.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (-5.39%)</td><td>0.15 (+14.16%)</td><td>0.16 (+10.66%)</td><td>0.09 <b>(+230.92%)</b></td><td>0.04 <b>(-47.20%)</b></td><td>539.60 <b>(-69.78%)</b></td><td>343.46 <b>(-44.43%)</b></td><td>311.20 (-9.61%)</td><td>265.50 (+5.69%)</td><td>112.21 <b>(-82.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1785.50 (n/a)</td><td>618.02 (n/a)</td><td>344.30 (n/a)</td><td>251.20 (n/a)</td><td>658.10 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>475.70 (n/a)</td><td>384.26 (n/a)</td><td>430.80 (n/a)</td><td>279.80 (n/a)</td><td>89.56 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2026.90 (n/a)</td><td>695.52 (n/a)</td><td>421.20 (n/a)</td><td>282.20 (n/a)</td><td>747.33 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.90 (n/a)</td><td>390.38 (n/a)</td><td>359.90 (n/a)</td><td>281.60 (n/a)</td><td>105.12 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.00 (n/a)</td><td>411.10 (n/a)</td><td>434.90 (n/a)</td><td>254.30 (n/a)</td><td>147.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.70 (n/a)</td><td>515.88 (n/a)</td><td>557.70 (n/a)</td><td>283.60 (n/a)</td><td>150.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.20 (n/a)</td><td>384.74 (n/a)</td><td>447.10 (n/a)</td><td>265.40 (n/a)</td><td>99.66 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.20 (n/a)</td><td>461.04 (n/a)</td><td>538.90 (n/a)</td><td>238.10 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2408.30 (n/a)</td><td>859.62 (n/a)</td><td>477.70 (n/a)</td><td>429.30 (n/a)</td><td>866.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.60 (n/a)</td><td>421.86 (n/a)</td><td>432.70 (n/a)</td><td>279.30 (n/a)</td><td>89.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>601.40 (n/a)</td><td>337.00 (n/a)</td><td>257.70 (n/a)</td><td>242.50 (n/a)</td><td>152.27 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>525.20 (n/a)</td><td>381.48 (n/a)</td><td>405.50 (n/a)</td><td>202.50 (n/a)</td><td>132.98 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>778.80 (n/a)</td><td>460.16 (n/a)</td><td>451.30 (n/a)</td><td>221.70 (n/a)</td><td>237.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>675.10 (n/a)</td><td>486.88 (n/a)</td><td>473.70 (n/a)</td><td>261.60 (n/a)</td><td>156.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.46 (+0.07%)</td><td>2.46 <b>(-22.79%)</b></td><td>1.92 <b>(-27.58%)</b></td><td>1.74 (-1.87%)</td><td>1.15 (-4.46%)</td><td>6028.80 (+1.90%)</td><td>4823.06 <b>(+29.54%)</b></td><td>5451.20 <b>(+38.08%)</b></td><td>2349.00 (-0.06%)</td><td>1520.17 (+3.22%)</td><td>1828.44 (+0.07%)</td><td>1006.67 <b>(-22.79%)</b></td><td>787.89 <b>(-27.58%)</b></td><td>712.41 (-1.87%)</td><td>470.84 (-4.46%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.46 (n/a)</td><td>3.18 (n/a)</td><td>2.66 (n/a)</td><td>1.77 (n/a)</td><td>1.20 (n/a)</td><td>5916.20 (n/a)</td><td>3723.34 (n/a)</td><td>3947.80 (n/a)</td><td>2350.50 (n/a)</td><td>1472.78 (n/a)</td><td>1827.25 (n/a)</td><td>1303.88 (n/a)</td><td>1087.93 (n/a)</td><td>725.97 (n/a)</td><td>492.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.86 (+3.84%)</td><td>3.29 (-0.96%)</td><td>3.68 (+7.58%)</td><td>2.20 (-18.03%)</td><td>0.69 <b>(+71.66%)</b></td><td>10702.30 <b>(+22.00%)</b></td><td>7488.36 (+4.13%)</td><td>6409.20 (-7.05%)</td><td>6115.70 (-3.70%)</td><td>1925.86 <b>(+99.76%)</b></td><td>2194.66 (+3.84%)</td><td>1872.79 (-0.96%)</td><td>2094.13 (+7.58%)</td><td>1254.11 (-18.03%)</td><td>394.51 <b>(+71.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.72 (n/a)</td><td>3.32 (n/a)</td><td>3.42 (n/a)</td><td>2.69 (n/a)</td><td>0.40 (n/a)</td><td>8772.50 (n/a)</td><td>7191.06 (n/a)</td><td>6895.10 (n/a)</td><td>6350.40 (n/a)</td><td>964.08 (n/a)</td><td>2113.52 (n/a)</td><td>1891.00 (n/a)</td><td>1946.58 (n/a)</td><td>1529.99 (n/a)</td><td>229.82 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.07 (+4.25%)</td><td>3.01 (+0.32%)</td><td>2.85 (-11.04%)</td><td>2.31 <b>(+25.42%)</b></td><td>0.70 <b>(-25.80%)</b></td><td>7264.10 <b>(-20.27%)</b></td><td>5813.50 (-5.32%)</td><td>5882.40 (+12.41%)</td><td>4118.90 (-4.08%)</td><td>1254.21 <b>(-41.94%)</b></td><td>2085.48 (+4.25%)</td><td>1538.97 (+0.32%)</td><td>1460.29 (-11.04%)</td><td>1182.52 <b>(+25.42%)</b></td><td>360.57 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.91 (n/a)</td><td>3.00 (n/a)</td><td>3.21 (n/a)</td><td>1.84 (n/a)</td><td>0.95 (n/a)</td><td>9110.70 (n/a)</td><td>6139.88 (n/a)</td><td>5233.00 (n/a)</td><td>4294.20 (n/a)</td><td>2160.33 (n/a)</td><td>2000.38 (n/a)</td><td>1534.11 (n/a)</td><td>1641.50 (n/a)</td><td>942.84 (n/a)</td><td>485.94 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.89 <b>(-32.86%)</b></td><td>0.70 <b>(-20.57%)</b></td><td>0.68 (-19.65%)</td><td>0.49 (+0.83%)</td><td>0.15 <b>(-57.15%)</b></td><td>928.70 (-0.82%)</td><td>679.12 (+14.41%)</td><td>675.70 <b>(+24.46%)</b></td><td>517.10 <b>(+48.98%)</b></td><td>158.39 <b>(-35.52%)</b></td><td>64.89 <b>(-32.86%)</b></td><td>51.42 <b>(-20.57%)</b></td><td>49.66 (-19.65%)</td><td>36.13 (+0.83%)</td><td>10.98 <b>(-57.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.32 (n/a)</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>936.40 (n/a)</td><td>593.58 (n/a)</td><td>542.90 (n/a)</td><td>347.10 (n/a)</td><td>245.65 (n/a)</td><td>96.66 (n/a)</td><td>64.74 (n/a)</td><td>61.80 (n/a)</td><td>35.83 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.52 <b>(+48.58%)</b></td><td>1.12 <b>(+30.51%)</b></td><td>0.92 (+0.89%)</td><td>0.84 <b>(+43.69%)</b></td><td>0.33 <b>(+105.23%)</b></td><td>776.20 <b>(-30.40%)</b></td><td>626.16 <b>(-20.98%)</b></td><td>711.80 (-0.89%)</td><td>431.30 <b>(-32.70%)</b></td><td>169.84 (-8.84%)</td><td>155.58 <b>(+48.58%)</b></td><td>114.59 <b>(+30.51%)</b></td><td>94.28 (+0.89%)</td><td>86.46 <b>(+43.69%)</b></td><td>34.26 <b>(+105.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.02 (n/a)</td><td>0.86 (n/a)</td><td>0.91 (n/a)</td><td>0.59 (n/a)</td><td>0.16 (n/a)</td><td>1115.30 (n/a)</td><td>792.40 (n/a)</td><td>718.20 (n/a)</td><td>640.90 (n/a)</td><td>186.31 (n/a)</td><td>104.71 (n/a)</td><td>87.80 (n/a)</td><td>93.44 (n/a)</td><td>60.17 (n/a)</td><td>16.69 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.43 <b>(-22.46%)</b></td><td>1.21 (+0.49%)</td><td>1.17 (-11.90%)</td><td>0.98 <b>(+145.84%)</b></td><td>0.17 <b>(-68.26%)</b></td><td>765.90 <b>(-59.33%)</b></td><td>634.34 <b>(-23.26%)</b></td><td>642.60 (+13.51%)</td><td>525.90 <b>(+28.96%)</b></td><td>91.15 <b>(-84.88%)</b></td><td>159.52 <b>(-22.46%)</b></td><td>134.41 (+0.49%)</td><td>130.55 (-11.90%)</td><td>109.52 <b>(+145.84%)</b></td><td>19.01 <b>(-68.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.85 (n/a)</td><td>1.20 (n/a)</td><td>1.33 (n/a)</td><td>0.40 (n/a)</td><td>0.54 (n/a)</td><td>1883.00 (n/a)</td><td>826.64 (n/a)</td><td>566.10 (n/a)</td><td>407.80 (n/a)</td><td>602.65 (n/a)</td><td>205.71 (n/a)</td><td>133.76 (n/a)</td><td>148.18 (n/a)</td><td>44.55 (n/a)</td><td>59.91 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.67 (+12.22%)</td><td>0.89 <b>(-24.54%)</b></td><td>0.74 <b>(-43.14%)</b></td><td>0.47 (-17.97%)</td><td>0.49 <b>(+33.06%)</b></td><td>2212.30 <b>(+21.90%)</b></td><td>1456.16 <b>(+44.87%)</b></td><td>1420.70 <b>(+75.89%)</b></td><td>629.00 (-10.88%)</td><td>661.84 <b>(+42.81%)</b></td><td>213.39 (+12.22%)</td><td>113.55 <b>(-24.54%)</b></td><td>94.48 <b>(-43.14%)</b></td><td>60.67 (-17.97%)</td><td>62.55 <b>(+33.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.49 (n/a)</td><td>1.18 (n/a)</td><td>1.30 (n/a)</td><td>0.58 (n/a)</td><td>0.37 (n/a)</td><td>1814.80 (n/a)</td><td>1005.16 (n/a)</td><td>807.70 (n/a)</td><td>705.80 (n/a)</td><td>463.44 (n/a)</td><td>190.16 (n/a)</td><td>150.48 (n/a)</td><td>166.17 (n/a)</td><td>73.96 (n/a)</td><td>47.01 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.22 (+17.95%)</td><td>1.44 (+15.34%)</td><td>1.33 <b>(+28.19%)</b></td><td>0.89 (+5.10%)</td><td>0.59 <b>(+39.15%)</b></td><td>1171.80 (-4.86%)</td><td>833.98 (-8.68%)</td><td>791.10 <b>(-21.99%)</b></td><td>471.80 (-15.22%)</td><td>328.01 <b>(+20.69%)</b></td><td>284.48 (+17.95%)</td><td>184.07 (+15.34%)</td><td>169.67 <b>(+28.19%)</b></td><td>114.54 (+5.10%)</td><td>75.32 <b>(+39.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.88 (n/a)</td><td>1.25 (n/a)</td><td>1.03 (n/a)</td><td>0.85 (n/a)</td><td>0.42 (n/a)</td><td>1231.60 (n/a)</td><td>913.28 (n/a)</td><td>1014.10 (n/a)</td><td>556.50 (n/a)</td><td>271.77 (n/a)</td><td>241.19 (n/a)</td><td>159.59 (n/a)</td><td>132.36 (n/a)</td><td>108.98 (n/a)</td><td>54.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.11 (+3.43%)</td><td>1.94 <b>(+32.07%)</b></td><td>1.97 <b>(+47.17%)</b></td><td>1.63 <b>(+60.01%)</b></td><td>0.20 <b>(-48.57%)</b></td><td>641.60 <b>(-37.50%)</b></td><td>546.62 <b>(-27.48%)</b></td><td>532.70 <b>(-32.05%)</b></td><td>496.40 (-3.31%)</td><td>59.37 <b>(-68.62%)</b></td><td>270.37 (+3.43%)</td><td>247.71 <b>(+32.07%)</b></td><td>251.97 <b>(+47.17%)</b></td><td>209.20 <b>(+60.01%)</b></td><td>25.06 <b>(-48.57%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.04 (n/a)</td><td>1.47 (n/a)</td><td>1.34 (n/a)</td><td>1.02 (n/a)</td><td>0.38 (n/a)</td><td>1026.60 (n/a)</td><td>753.80 (n/a)</td><td>784.00 (n/a)</td><td>513.40 (n/a)</td><td>189.19 (n/a)</td><td>261.41 (n/a)</td><td>187.56 (n/a)</td><td>171.20 (n/a)</td><td>130.74 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.48 (-12.96%)</td><td>0.89 <b>(-35.49%)</b></td><td>0.84 <b>(-34.28%)</b></td><td>0.44 <b>(-54.40%)</b></td><td>0.45 <b>(+45.72%)</b></td><td>2364.40 <b>(+119.27%)</b></td><td>1479.92 <b>(+85.70%)</b></td><td>1244.20 <b>(+52.16%)</b></td><td>710.50 (+14.87%)</td><td>759.47 <b>(+302.26%)</b></td><td>188.90 (-12.96%)</td><td>113.39 <b>(-35.49%)</b></td><td>107.88 <b>(-34.28%)</b></td><td>56.77 <b>(-54.40%)</b></td><td>57.45 <b>(+45.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.70 (n/a)</td><td>1.37 (n/a)</td><td>1.28 (n/a)</td><td>0.97 (n/a)</td><td>0.31 (n/a)</td><td>1078.30 (n/a)</td><td>796.94 (n/a)</td><td>817.70 (n/a)</td><td>618.50 (n/a)</td><td>188.80 (n/a)</td><td>217.02 (n/a)</td><td>175.78 (n/a)</td><td>164.14 (n/a)</td><td>124.48 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.66 (-13.40%)</td><td>1.01 <b>(-33.61%)</b></td><td>1.10 <b>(-20.15%)</b></td><td>0.35 <b>(-72.69%)</b></td><td>0.48 <b>(+67.33%)</b></td><td>3000.20 <b>(+266.10%)</b></td><td>1351.78 <b>(+91.99%)</b></td><td>956.60 <b>(+25.24%)</b></td><td>631.20 (+15.48%)</td><td>945.47 <b>(+677.81%)</b></td><td>212.64 (-13.40%)</td><td>129.88 <b>(-33.61%)</b></td><td>140.31 <b>(-20.15%)</b></td><td>44.74 <b>(-72.69%)</b></td><td>60.81 <b>(+67.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.92 (n/a)</td><td>1.53 (n/a)</td><td>1.37 (n/a)</td><td>1.28 (n/a)</td><td>0.28 (n/a)</td><td>819.50 (n/a)</td><td>704.10 (n/a)</td><td>763.80 (n/a)</td><td>546.60 (n/a)</td><td>121.56 (n/a)</td><td>245.55 (n/a)</td><td>195.63 (n/a)</td><td>175.72 (n/a)</td><td>163.79 (n/a)</td><td>36.34 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.75 (-5.04%)</td><td>1.41 (+12.95%)</td><td>1.65 (+13.04%)</td><td>0.51 (+7.47%)</td><td>0.52 (-4.47%)</td><td>2066.40 (-6.95%)</td><td>930.58 (-12.60%)</td><td>634.30 (-11.53%)</td><td>599.50 (+5.30%)</td><td>637.19 (-6.26%)</td><td>223.88 (-5.04%)</td><td>180.10 (+12.95%)</td><td>211.60 (+13.04%)</td><td>64.95 (+7.47%)</td><td>66.34 (-4.47%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.84 (n/a)</td><td>1.25 (n/a)</td><td>1.46 (n/a)</td><td>0.47 (n/a)</td><td>0.54 (n/a)</td><td>2220.70 (n/a)</td><td>1064.74 (n/a)</td><td>717.00 (n/a)</td><td>569.30 (n/a)</td><td>679.71 (n/a)</td><td>235.75 (n/a)</td><td>159.45 (n/a)</td><td>187.19 (n/a)</td><td>60.44 (n/a)</td><td>69.44 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.09 (+7.33%)</td><td>0.77 (+11.40%)</td><td>0.78 (+16.11%)</td><td>0.54 (+14.95%)</td><td>0.23 (+6.28%)</td><td>669.80 (-13.00%)</td><td>500.88 (-10.54%)</td><td>463.40 (-13.87%)</td><td>330.60 (-6.82%)</td><td>147.93 (-11.08%)</td><td>50.75 (+7.33%)</td><td>36.00 (+11.40%)</td><td>36.21 (+16.11%)</td><td>25.05 (+14.95%)</td><td>10.78 (+6.28%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.02 (n/a)</td><td>0.69 (n/a)</td><td>0.67 (n/a)</td><td>0.47 (n/a)</td><td>0.22 (n/a)</td><td>769.90 (n/a)</td><td>559.88 (n/a)</td><td>538.00 (n/a)</td><td>354.80 (n/a)</td><td>166.36 (n/a)</td><td>47.28 (n/a)</td><td>32.31 (n/a)</td><td>31.18 (n/a)</td><td>21.79 (n/a)</td><td>10.14 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.98 <b>(-35.26%)</b></td><td>1.59 <b>(-33.67%)</b></td><td>1.68 <b>(-33.42%)</b></td><td>0.93 <b>(-41.41%)</b></td><td>0.42 <b>(-36.91%)</b></td><td>4501.30 <b>(+70.68%)</b></td><td>2841.28 <b>(+51.49%)</b></td><td>2502.70 <b>(+50.20%)</b></td><td>2116.40 <b>(+54.47%)</b></td><td>977.29 <b>(+71.86%)</b></td><td>507.34 <b>(-35.26%)</b></td><td>407.16 <b>(-33.67%)</b></td><td>429.03 <b>(-33.42%)</b></td><td>238.54 <b>(-41.41%)</b></td><td>108.51 <b>(-36.91%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.06 (n/a)</td><td>2.40 (n/a)</td><td>2.52 (n/a)</td><td>1.59 (n/a)</td><td>0.67 (n/a)</td><td>2637.30 (n/a)</td><td>1875.52 (n/a)</td><td>1666.20 (n/a)</td><td>1370.10 (n/a)</td><td>568.65 (n/a)</td><td>783.69 (n/a)</td><td>613.81 (n/a)</td><td>644.43 (n/a)</td><td>407.14 (n/a)</td><td>171.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.64 <b>(-23.65%)</b></td><td>3.14 (+6.48%)</td><td>3.27 (+0.64%)</td><td>2.20 <b>(+107.12%)</b></td><td>0.59 <b>(-57.67%)</b></td><td>1190.60 <b>(-51.72%)</b></td><td>864.38 <b>(-25.05%)</b></td><td>802.30 (-0.63%)</td><td>719.40 <b>(+30.97%)</b></td><td>193.52 <b>(-74.80%)</b></td><td>746.27 <b>(-23.65%)</b></td><td>642.49 (+6.48%)</td><td>669.17 (+0.64%)</td><td>450.94 <b>(+107.12%)</b></td><td>120.43 <b>(-57.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.77 (n/a)</td><td>2.95 (n/a)</td><td>3.25 (n/a)</td><td>1.06 (n/a)</td><td>1.39 (n/a)</td><td>2465.90 (n/a)</td><td>1153.22 (n/a)</td><td>807.40 (n/a)</td><td>549.30 (n/a)</td><td>767.81 (n/a)</td><td>977.42 (n/a)</td><td>603.39 (n/a)</td><td>664.91 (n/a)</td><td>217.71 (n/a)</td><td>284.49 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.01 (-9.90%)</td><td>2.52 (-6.94%)</td><td>2.88 (+2.67%)</td><td>1.58 <b>(-21.08%)</b></td><td>0.62 (+3.44%)</td><td>4972.80 <b>(+26.71%)</b></td><td>3312.70 (+9.56%)</td><td>2734.00 (-2.60%)</td><td>2616.20 (+10.99%)</td><td>1009.14 <b>(+43.76%)</b></td><td>923.46 (-9.90%)</td><td>775.18 (-6.94%)</td><td>883.64 (+2.67%)</td><td>485.83 <b>(-21.08%)</b></td><td>190.56 (+3.44%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.34 (n/a)</td><td>2.71 (n/a)</td><td>2.80 (n/a)</td><td>2.00 (n/a)</td><td>0.60 (n/a)</td><td>3924.40 (n/a)</td><td>3023.62 (n/a)</td><td>2807.10 (n/a)</td><td>2357.20 (n/a)</td><td>701.95 (n/a)</td><td>1024.91 (n/a)</td><td>833.03 (n/a)</td><td>860.64 (n/a)</td><td>615.61 (n/a)</td><td>184.23 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>537.90 (n/a)</td><td>378.40 (n/a)</td><td>414.50 (n/a)</td><td>195.80 (n/a)</td><td>161.18 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.10 (n/a)</td><td>392.52 (n/a)</td><td>442.40 (n/a)</td><td>209.50 (n/a)</td><td>165.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.20 (n/a)</td><td>398.64 (n/a)</td><td>291.70 (n/a)</td><td>265.00 (n/a)</td><td>166.67 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.10 (n/a)</td><td>394.92 (n/a)</td><td>450.00 (n/a)</td><td>187.30 (n/a)</td><td>179.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1047.40 (n/a)</td><td>452.02 (n/a)</td><td>326.60 (n/a)</td><td>267.20 (n/a)</td><td>334.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>704.60 (n/a)</td><td>459.62 (n/a)</td><td>434.00 (n/a)</td><td>284.00 (n/a)</td><td>161.30 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.30 (n/a)</td><td>435.10 (n/a)</td><td>484.20 (n/a)</td><td>233.10 (n/a)</td><td>172.16 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>313.54 (n/a)</td><td>250.90 (n/a)</td><td>226.70 (n/a)</td><td>154.40 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.10 (n/a)</td><td>287.62 (n/a)</td><td>260.00 (n/a)</td><td>179.40 (n/a)</td><td>121.67 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2408.50 (n/a)</td><td>856.42 (n/a)</td><td>480.00 (n/a)</td><td>318.90 (n/a)</td><td>874.64 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2446.10 (n/a)</td><td>876.04 (n/a)</td><td>563.80 (n/a)</td><td>280.20 (n/a)</td><td>886.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.60 (n/a)</td><td>489.60 (n/a)</td><td>482.20 (n/a)</td><td>361.10 (n/a)</td><td>94.61 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.90 (n/a)</td><td>447.38 (n/a)</td><td>501.50 (n/a)</td><td>259.80 (n/a)</td><td>157.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.90 (n/a)</td><td>485.12 (n/a)</td><td>554.90 (n/a)</td><td>226.20 (n/a)</td><td>161.91 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>593.10 (n/a)</td><td>400.78 (n/a)</td><td>381.80 (n/a)</td><td>301.20 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>447.40 (n/a)</td><td>357.92 (n/a)</td><td>356.90 (n/a)</td><td>263.10 (n/a)</td><td>71.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>496.30 (n/a)</td><td>351.80 (n/a)</td><td>310.40 (n/a)</td><td>241.80 (n/a)</td><td>103.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.70 (n/a)</td><td>469.96 (n/a)</td><td>548.60 (n/a)</td><td>261.60 (n/a)</td><td>158.07 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.90 (n/a)</td><td>329.98 (n/a)</td><td>278.10 (n/a)</td><td>227.60 (n/a)</td><td>123.44 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>521.10 (n/a)</td><td>378.06 (n/a)</td><td>306.40 (n/a)</td><td>270.20 (n/a)</td><td>127.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>641.70 (n/a)</td><td>351.62 (n/a)</td><td>306.10 (n/a)</td><td>213.80 (n/a)</td><td>166.69 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>626.50 (n/a)</td><td>458.06 (n/a)</td><td>512.00 (n/a)</td><td>265.70 (n/a)</td><td>151.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1057.40 (n/a)</td><td>569.96 (n/a)</td><td>532.00 (n/a)</td><td>278.70 (n/a)</td><td>292.86 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>615.20 (n/a)</td><td>436.98 (n/a)</td><td>512.40 (n/a)</td><td>185.00 (n/a)</td><td>184.05 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.45 (-2.06%)</td><td>0.33 (-1.71%)</td><td>0.37 (+8.45%)</td><td>0.11 (-10.89%)</td><td>0.13 (-0.25%)</td><td>1940.70 (+12.22%)</td><td>855.24 (+5.29%)</td><td>605.50 (-7.80%)</td><td>490.20 (+2.10%)</td><td>609.80 (+17.53%)</td><td>19.25 (-2.06%)</td><td>14.05 (-1.71%)</td><td>15.59 (+8.45%)</td><td>4.86 (-10.89%)</td><td>5.44 (-0.25%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>1729.30 (n/a)</td><td>812.24 (n/a)</td><td>656.70 (n/a)</td><td>480.10 (n/a)</td><td>518.83 (n/a)</td><td>19.66 (n/a)</td><td>14.30 (n/a)</td><td>14.37 (n/a)</td><td>5.46 (n/a)</td><td>5.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.64 <b>(+28.83%)</b></td><td>0.46 <b>(+21.29%)</b></td><td>0.46 <b>(+22.78%)</b></td><td>0.35 (+11.76%)</td><td>0.11 <b>(+54.79%)</b></td><td>630.40 (-10.53%)</td><td>504.78 (-16.14%)</td><td>483.60 (-18.54%)</td><td>347.90 <b>(-22.38%)</b></td><td>112.49 (+6.92%)</td><td>27.13 <b>(+28.83%)</b></td><td>19.54 <b>(+21.29%)</b></td><td>19.52 <b>(+22.78%)</b></td><td>14.97 (+11.76%)</td><td>4.81 <b>(+54.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>704.60 (n/a)</td><td>601.94 (n/a)</td><td>593.70 (n/a)</td><td>448.20 (n/a)</td><td>105.20 (n/a)</td><td>21.06 (n/a)</td><td>16.11 (n/a)</td><td>15.90 (n/a)</td><td>13.39 (n/a)</td><td>3.11 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.31 (-1.20%)</td><td>0.30 (-0.63%)</td><td>0.30 (-0.71%)</td><td>0.30 (+0.32%)</td><td>0.00 <b>(-46.94%)</b></td><td>83469.90 (-0.32%)</td><td>82719.86 (+0.63%)</td><td>82648.00 (+0.71%)</td><td>81875.90 (+1.22%)</td><td>590.37 <b>(-46.50%)</b></td><td>209.83 (-1.20%)</td><td>207.70 (-0.63%)</td><td>207.87 (-0.71%)</td><td>205.82 (+0.32%)</td><td>1.48 <b>(-46.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83736.60 (n/a)</td><td>82203.30 (n/a)</td><td>82064.90 (n/a)</td><td>80891.50 (n/a)</td><td>1103.58 (n/a)</td><td>212.38 (n/a)</td><td>209.02 (n/a)</td><td>209.34 (n/a)</td><td>205.17 (n/a)</td><td>2.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.16 (+1.39%)</td><td>1.13 (+1.94%)</td><td>1.13 (+3.52%)</td><td>1.11 (+2.74%)</td><td>0.02 <b>(-31.23%)</b></td><td>22769.50 (-2.67%)</td><td>22327.54 (-1.94%)</td><td>22340.90 (-3.40%)</td><td>21614.40 (-1.37%)</td><td>449.77 <b>(-34.04%)</b></td><td>794.83 (+1.39%)</td><td>769.70 (+1.94%)</td><td>768.99 (+3.52%)</td><td>754.51 (+2.74%)</td><td>15.72 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>1.09 (n/a)</td><td>1.08 (n/a)</td><td>0.03 (n/a)</td><td>23393.00 (n/a)</td><td>22768.66 (n/a)</td><td>23127.70 (n/a)</td><td>21913.90 (n/a)</td><td>681.88 (n/a)</td><td>783.97 (n/a)</td><td>755.09 (n/a)</td><td>742.83 (n/a)</td><td>734.40 (n/a)</td><td>22.86 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.80 (+0.03%)</td><td>0.78 (-0.55%)</td><td>0.78 (-1.24%)</td><td>0.76 (-0.23%)</td><td>0.02 (+7.57%)</td><td>99615.30 (+0.24%)</td><td>96818.60 (+0.55%)</td><td>97278.40 (+1.26%)</td><td>94019.50 (-0.03%)</td><td>2139.69 (+7.43%)</td><td>730.91 (+0.03%)</td><td>710.05 (-0.55%)</td><td>706.42 (-1.24%)</td><td>689.85 (-0.23%)</td><td>15.71 (+7.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.02 (n/a)</td><td>99381.70 (n/a)</td><td>96284.86 (n/a)</td><td>96070.50 (n/a)</td><td>94051.40 (n/a)</td><td>1991.66 (n/a)</td><td>730.66 (n/a)</td><td>713.95 (n/a)</td><td>715.30 (n/a)</td><td>691.47 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (-1.05%)</td><td>0.76 (-0.06%)</td><td>0.76 (-0.19%)</td><td>0.74 (+0.35%)</td><td>0.01 <b>(-24.76%)</b></td><td>101505.00 (-0.35%)</td><td>99209.78 (+0.05%)</td><td>99100.60 (+0.19%)</td><td>97878.70 (+1.07%)</td><td>1397.59 <b>(-24.17%)</b></td><td>702.09 (-1.05%)</td><td>692.78 (-0.06%)</td><td>693.43 (-0.19%)</td><td>677.01 (+0.35%)</td><td>9.65 <b>(-24.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101864.40 (n/a)</td><td>99159.98 (n/a)</td><td>98915.60 (n/a)</td><td>96846.60 (n/a)</td><td>1843.13 (n/a)</td><td>709.57 (n/a)</td><td>693.21 (n/a)</td><td>694.73 (n/a)</td><td>674.62 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.90 (+0.01%)</td><td>0.89 (-0.39%)</td><td>0.89 (-0.27%)</td><td>0.87 (-1.13%)</td><td>0.01 <b>(+35.23%)</b></td><td>86965.60 (+1.14%)</td><td>85256.52 (+0.40%)</td><td>84538.20 (+0.27%)</td><td>84191.50 (-0.01%)</td><td>1236.23 <b>(+36.69%)</b></td><td>816.23 (+0.01%)</td><td>806.17 (-0.39%)</td><td>812.88 (-0.27%)</td><td>790.19 (-1.13%)</td><td>11.61 <b>(+35.23%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85982.90 (n/a)</td><td>84919.80 (n/a)</td><td>84313.10 (n/a)</td><td>84203.00 (n/a)</td><td>904.41 (n/a)</td><td>816.12 (n/a)</td><td>809.30 (n/a)</td><td>815.05 (n/a)</td><td>799.22 (n/a)</td><td>8.59 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.51 (-0.65%)</td><td>4.17 (-12.26%)</td><td>3.87 (-16.28%)</td><td>3.50 (-12.46%)</td><td>0.83 (+10.20%)</td><td>2548.30 (+14.23%)</td><td>2200.18 (+14.89%)</td><td>2304.80 (+19.44%)</td><td>1616.30 (+0.65%)</td><td>383.84 <b>(+27.85%)</b></td><td>332.17 (-0.65%)</td><td>250.94 (-12.26%)</td><td>232.93 (-16.28%)</td><td>210.68 (-12.46%)</td><td>50.03 (+10.20%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.55 (n/a)</td><td>4.75 (n/a)</td><td>4.62 (n/a)</td><td>4.00 (n/a)</td><td>0.75 (n/a)</td><td>2230.90 (n/a)</td><td>1915.10 (n/a)</td><td>1929.60 (n/a)</td><td>1605.80 (n/a)</td><td>300.24 (n/a)</td><td>334.33 (n/a)</td><td>286.01 (n/a)</td><td>278.23 (n/a)</td><td>240.65 (n/a)</td><td>45.39 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.25 (-15.14%)</td><td>2.89 <b>(-22.00%)</b></td><td>2.67 <b>(-32.93%)</b></td><td>1.85 (-14.73%)</td><td>0.95 <b>(-20.56%)</b></td><td>4828.00 (+17.28%)</td><td>3361.30 <b>(+26.49%)</b></td><td>3340.00 <b>(+49.09%)</b></td><td>2098.20 (+17.84%)</td><td>1071.57 (+9.04%)</td><td>255.88 (-15.14%)</td><td>173.88 <b>(-22.00%)</b></td><td>160.74 <b>(-32.93%)</b></td><td>111.20 (-14.73%)</td><td>57.24 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.01 (n/a)</td><td>3.70 (n/a)</td><td>3.98 (n/a)</td><td>2.17 (n/a)</td><td>1.20 (n/a)</td><td>4116.80 (n/a)</td><td>2657.42 (n/a)</td><td>2240.30 (n/a)</td><td>1780.60 (n/a)</td><td>982.76 (n/a)</td><td>301.51 (n/a)</td><td>222.91 (n/a)</td><td>239.65 (n/a)</td><td>130.41 (n/a)</td><td>72.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.76 <b>(+41.13%)</b></td><td>4.18 <b>(+29.53%)</b></td><td>4.15 <b>(+31.55%)</b></td><td>1.98 <b>(-20.07%)</b></td><td>1.56 <b>(+127.48%)</b></td><td>4500.90 <b>(+25.10%)</b></td><td>2476.00 (-13.58%)</td><td>2149.30 <b>(-23.99%)</b></td><td>1546.30 <b>(-29.14%)</b></td><td>1207.09 <b>(+100.02%)</b></td><td>347.19 <b>(+41.13%)</b></td><td>251.63 <b>(+29.53%)</b></td><td>249.78 <b>(+31.55%)</b></td><td>119.28 <b>(-20.07%)</b></td><td>93.74 <b>(+127.48%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.08 (n/a)</td><td>3.23 (n/a)</td><td>3.15 (n/a)</td><td>2.48 (n/a)</td><td>0.68 (n/a)</td><td>3597.80 (n/a)</td><td>2865.24 (n/a)</td><td>2827.50 (n/a)</td><td>2182.30 (n/a)</td><td>603.48 (n/a)</td><td>246.02 (n/a)</td><td>194.26 (n/a)</td><td>189.88 (n/a)</td><td>149.22 (n/a)</td><td>41.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.43 (+15.06%)</td><td>5.51 (+11.16%)</td><td>5.42 (+4.73%)</td><td>4.67 (+7.22%)</td><td>0.63 (+14.95%)</td><td>7464.90 (-6.73%)</td><td>6398.70 (-10.00%)</td><td>6433.40 (-4.52%)</td><td>5422.50 (-13.09%)</td><td>733.40 (-8.95%)</td><td>396.04 (+15.06%)</td><td>339.16 (+11.16%)</td><td>333.80 (+4.73%)</td><td>287.68 (+7.22%)</td><td>38.94 (+14.95%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.59 (n/a)</td><td>4.95 (n/a)</td><td>5.17 (n/a)</td><td>4.36 (n/a)</td><td>0.55 (n/a)</td><td>8003.50 (n/a)</td><td>7109.62 (n/a)</td><td>6737.80 (n/a)</td><td>6239.20 (n/a)</td><td>805.47 (n/a)</td><td>344.19 (n/a)</td><td>305.12 (n/a)</td><td>318.72 (n/a)</td><td>268.32 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.19 (+0.08%)</td><td>4.85 (+10.37%)</td><td>4.77 (+17.37%)</td><td>4.49 (+16.52%)</td><td>0.32 <b>(-43.51%)</b></td><td>7768.80 (-14.18%)</td><td>7219.40 (-10.25%)</td><td>7311.50 (-14.80%)</td><td>6717.10 (-0.08%)</td><td>478.78 <b>(-51.95%)</b></td><td>319.70 (+0.08%)</td><td>298.52 (+10.37%)</td><td>293.71 (+17.37%)</td><td>276.43 (+16.52%)</td><td>19.93 <b>(-43.51%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.19 (n/a)</td><td>4.39 (n/a)</td><td>4.06 (n/a)</td><td>3.85 (n/a)</td><td>0.57 (n/a)</td><td>9052.40 (n/a)</td><td>8043.90 (n/a)</td><td>8581.80 (n/a)</td><td>6722.60 (n/a)</td><td>996.36 (n/a)</td><td>319.44 (n/a)</td><td>270.46 (n/a)</td><td>250.24 (n/a)</td><td>237.23 (n/a)</td><td>35.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.02 (+9.44%)</td><td>5.45 (+9.32%)</td><td>5.47 (+10.08%)</td><td>4.92 (+15.24%)</td><td>0.39 <b>(-22.85%)</b></td><td>7088.20 (-13.23%)</td><td>6423.48 (-8.94%)</td><td>6370.10 (-9.16%)</td><td>5793.30 (-8.63%)</td><td>461.02 <b>(-38.30%)</b></td><td>370.68 (+9.44%)</td><td>335.70 (+9.32%)</td><td>337.12 (+10.08%)</td><td>302.97 (+15.24%)</td><td>24.11 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.50 (n/a)</td><td>4.99 (n/a)</td><td>4.97 (n/a)</td><td>4.27 (n/a)</td><td>0.51 (n/a)</td><td>8168.60 (n/a)</td><td>7054.16 (n/a)</td><td>7012.30 (n/a)</td><td>6340.40 (n/a)</td><td>747.25 (n/a)</td><td>338.70 (n/a)</td><td>307.07 (n/a)</td><td>306.24 (n/a)</td><td>262.89 (n/a)</td><td>31.26 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (+1.58%)</td><td>0.76 (+0.39%)</td><td>0.76 (+0.86%)</td><td>0.73 (-1.71%)</td><td>0.02 <b>(+102.16%)</b></td><td>103500.60 (+1.74%)</td><td>99839.40 (-0.36%)</td><td>99318.30 (-0.86%)</td><td>97527.60 (-1.55%)</td><td>2291.42 <b>(+103.32%)</b></td><td>704.62 (+1.58%)</td><td>688.59 (+0.39%)</td><td>691.91 (+0.86%)</td><td>663.95 (-1.71%)</td><td>15.56 <b>(+102.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101731.30 (n/a)</td><td>100199.04 (n/a)</td><td>100176.20 (n/a)</td><td>99066.30 (n/a)</td><td>1127.00 (n/a)</td><td>693.67 (n/a)</td><td>685.90 (n/a)</td><td>685.99 (n/a)</td><td>675.50 (n/a)</td><td>7.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (+1.21%)</td><td>0.76 (+1.33%)</td><td>0.77 (+1.80%)</td><td>0.75 (+0.89%)</td><td>0.01 <b>(+36.76%)</b></td><td>100231.20 (-0.88%)</td><td>98948.08 (-1.31%)</td><td>98557.70 (-1.77%)</td><td>97725.50 (-1.20%)</td><td>1150.68 <b>(+34.25%)</b></td><td>703.19 (+1.21%)</td><td>694.58 (+1.33%)</td><td>697.25 (+1.80%)</td><td>685.61 (+0.89%)</td><td>8.06 <b>(+36.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101123.90 (n/a)</td><td>100260.52 (n/a)</td><td>100330.60 (n/a)</td><td>98909.60 (n/a)</td><td>857.11 (n/a)</td><td>694.77 (n/a)</td><td>685.45 (n/a)</td><td>684.93 (n/a)</td><td>679.56 (n/a)</td><td>5.89 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.90 (+1.01%)</td><td>0.89 (-0.10%)</td><td>0.89 (+0.32%)</td><td>0.87 (-0.69%)</td><td>0.01 <b>(+115.44%)</b></td><td>86512.20 (+0.70%)</td><td>85027.44 (+0.11%)</td><td>84453.30 (-0.32%)</td><td>83676.50 (-1.00%)</td><td>1208.26 <b>(+114.86%)</b></td><td>821.25 (+1.01%)</td><td>808.33 (-0.10%)</td><td>813.70 (+0.32%)</td><td>794.33 (-0.69%)</td><td>11.45 <b>(+115.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85914.10 (n/a)</td><td>84930.08 (n/a)</td><td>84724.50 (n/a)</td><td>84519.20 (n/a)</td><td>562.34 (n/a)</td><td>813.06 (n/a)</td><td>809.16 (n/a)</td><td>811.09 (n/a)</td><td>799.86 (n/a)</td><td>5.32 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.26 (-2.51%)</td><td>2.42 (-17.81%)</td><td>1.94 (-16.36%)</td><td>1.69 (-0.20%)</td><td>1.08 (-15.85%)</td><td>4769.00 (+0.20%)</td><td>3751.46 (+18.15%)</td><td>4150.50 (+19.55%)</td><td>1890.50 (+2.57%)</td><td>1224.31 (-4.94%)</td><td>1118.18 (-2.51%)</td><td>635.64 (-17.81%)</td><td>509.32 (-16.36%)</td><td>443.26 (-0.20%)</td><td>284.30 (-15.85%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.37 (n/a)</td><td>2.95 (n/a)</td><td>2.32 (n/a)</td><td>1.69 (n/a)</td><td>1.29 (n/a)</td><td>4759.40 (n/a)</td><td>3175.14 (n/a)</td><td>3471.70 (n/a)</td><td>1843.10 (n/a)</td><td>1287.91 (n/a)</td><td>1146.97 (n/a)</td><td>773.35 (n/a)</td><td>608.91 (n/a)</td><td>444.16 (n/a)</td><td>337.83 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.22 (+5.57%)</td><td>0.18 (-3.68%)</td><td>0.18 (-6.94%)</td><td>0.15 (-5.76%)</td><td>0.03 <b>(+49.61%)</b></td><td>8106.70 (+6.11%)</td><td>7025.36 (+4.77%)</td><td>7077.20 (+7.46%)</td><td>5612.80 (-5.27%)</td><td>973.29 <b>(+49.03%)</b></td><td>11.96 (+5.57%)</td><td>9.71 (-3.68%)</td><td>9.48 (-6.94%)</td><td>8.28 (-5.76%)</td><td>1.44 <b>(+49.61%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7639.80 (n/a)</td><td>6705.70 (n/a)</td><td>6585.80 (n/a)</td><td>5925.20 (n/a)</td><td>653.10 (n/a)</td><td>11.33 (n/a)</td><td>10.08 (n/a)</td><td>10.19 (n/a)</td><td>8.78 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.94 (n/a)</td><td>3.59 (n/a)</td><td>3.51 (n/a)</td><td>3.39 (n/a)</td><td>0.22 (n/a)</td><td>3.94 (n/a)</td><td>3.59 (n/a)</td><td>3.51 (n/a)</td><td>3.38 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.56 (+13.44%)</td><td>6.51 (+10.21%)</td><td>6.89 (+17.63%)</td><td>4.79 (-3.29%)</td><td>1.17 <b>(+75.49%)</b></td><td>7.56 (+13.44%)</td><td>6.51 (+10.21%)</td><td>6.88 (+17.63%)</td><td>4.79 (-3.29%)</td><td>1.17 <b>(+75.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.67 (n/a)</td><td>5.91 (n/a)</td><td>5.85 (n/a)</td><td>4.96 (n/a)</td><td>0.67 (n/a)</td><td>6.66 (n/a)</td><td>5.91 (n/a)</td><td>5.85 (n/a)</td><td>4.95 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>13.01 <b>(+40.36%)</b></td><td>10.80 <b>(+25.17%)</b></td><td>11.29 <b>(+32.30%)</b></td><td>8.52 (+4.38%)</td><td>1.75 <b>(+274.46%)</b></td><td>13.00 <b>(+40.36%)</b></td><td>10.80 <b>(+25.17%)</b></td><td>11.28 <b>(+32.30%)</b></td><td>8.51 (+4.38%)</td><td>1.75 <b>(+274.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>9.27 (n/a)</td><td>8.63 (n/a)</td><td>8.53 (n/a)</td><td>8.16 (n/a)</td><td>0.47 (n/a)</td><td>9.26 (n/a)</td><td>8.62 (n/a)</td><td>8.53 (n/a)</td><td>8.16 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.82 (n/a)</td><td>3.56 (n/a)</td><td>3.46 (n/a)</td><td>3.44 (n/a)</td><td>0.17 (n/a)</td><td>3.81 (n/a)</td><td>3.56 (n/a)</td><td>3.46 (n/a)</td><td>3.44 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.27 (+5.79%)</td><td>6.43 (+15.18%)</td><td>6.69 (+17.53%)</td><td>5.10 (+16.07%)</td><td>0.84 (-6.67%)</td><td>7.27 (+5.79%)</td><td>6.43 (+15.18%)</td><td>6.68 (+17.53%)</td><td>5.09 (+16.07%)</td><td>0.84 (-6.67%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.87 (n/a)</td><td>5.59 (n/a)</td><td>5.69 (n/a)</td><td>4.39 (n/a)</td><td>0.90 (n/a)</td><td>6.87 (n/a)</td><td>5.58 (n/a)</td><td>5.69 (n/a)</td><td>4.39 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>10.41 (+0.50%)</td><td>9.65 (+6.43%)</td><td>9.84 (+13.83%)</td><td>8.51 (+4.49%)</td><td>0.72 <b>(-26.50%)</b></td><td>10.40 (+0.50%)</td><td>9.64 (+6.43%)</td><td>9.84 (+13.83%)</td><td>8.51 (+4.49%)</td><td>0.72 <b>(-26.50%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>10.35 (n/a)</td><td>9.06 (n/a)</td><td>8.65 (n/a)</td><td>8.15 (n/a)</td><td>0.98 (n/a)</td><td>10.35 (n/a)</td><td>9.06 (n/a)</td><td>8.64 (n/a)</td><td>8.14 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.96 (-1.29%)</td><td>2.76 <b>(+63.58%)</b></td><td>2.75 <b>(+66.00%)</b></td><td>2.61 <b>(+156.80%)</b></td><td>0.12 <b>(-84.43%)</b></td><td>2.95 (-1.29%)</td><td>2.76 <b>(+63.58%)</b></td><td>2.75 <b>(+66.00%)</b></td><td>2.61 <b>(+156.80%)</b></td><td>0.12 <b>(-84.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.99 (n/a)</td><td>1.69 (n/a)</td><td>1.66 (n/a)</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td><td>2.99 (n/a)</td><td>1.69 (n/a)</td><td>1.65 (n/a)</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.51 (-6.99%)</td><td>0.33 (-10.61%)</td><td>0.34 (-15.38%)</td><td>0.13 <b>(+20.59%)</b></td><td>0.13 (-16.24%)</td><td>0.50 (-6.99%)</td><td>0.33 (-10.61%)</td><td>0.34 (-15.38%)</td><td>0.13 <b>(+20.59%)</b></td><td>0.13 (-16.24%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.11 (n/a)</td><td>0.16 (n/a)</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.11 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.62 (-9.27%)</td><td>0.38 <b>(-30.00%)</b></td><td>0.48 (-14.98%)</td><td>0.14 <b>(-63.74%)</b></td><td>0.22 <b>(+58.16%)</b></td><td>0.62 (-9.27%)</td><td>0.38 <b>(-30.00%)</b></td><td>0.48 (-14.98%)</td><td>0.14 <b>(-63.74%)</b></td><td>0.22 <b>(+58.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.69 (n/a)</td><td>0.54 (n/a)</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.14 (n/a)</td><td>0.68 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.38 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.39 (-12.25%)</td><td>1.37 <b>(-23.35%)</b></td><td>1.35 <b>(-27.42%)</b></td><td>0.49 (+10.73%)</td><td>0.74 (-11.33%)</td><td>2.35 (-12.25%)</td><td>1.34 <b>(-23.35%)</b></td><td>1.33 <b>(-27.42%)</b></td><td>0.48 (+10.73%)</td><td>0.73 (-11.33%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.72 (n/a)</td><td>1.78 (n/a)</td><td>1.87 (n/a)</td><td>0.44 (n/a)</td><td>0.84 (n/a)</td><td>2.68 (n/a)</td><td>1.75 (n/a)</td><td>1.84 (n/a)</td><td>0.43 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.50 (n/a)</td><td>394.22 (n/a)</td><td>467.10 (n/a)</td><td>244.60 (n/a)</td><td>126.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.20 (n/a)</td><td>378.96 (n/a)</td><td>301.20 (n/a)</td><td>228.90 (n/a)</td><td>180.35 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.60 (n/a)</td><td>451.30 (n/a)</td><td>492.70 (n/a)</td><td>264.60 (n/a)</td><td>127.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.00 (n/a)</td><td>480.20 (n/a)</td><td>469.90 (n/a)</td><td>426.20 (n/a)</td><td>48.12 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.30 (n/a)</td><td>396.20 (n/a)</td><td>367.60 (n/a)</td><td>290.20 (n/a)</td><td>101.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.10 (n/a)</td><td>457.60 (n/a)</td><td>445.40 (n/a)</td><td>378.80 (n/a)</td><td>56.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.70 (n/a)</td><td>304.30 (n/a)</td><td>297.00 (n/a)</td><td>200.10 (n/a)</td><td>100.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1026.20 (n/a)</td><td>560.60 (n/a)</td><td>535.80 (n/a)</td><td>234.30 (n/a)</td><td>288.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.90 (n/a)</td><td>392.90 (n/a)</td><td>441.20 (n/a)</td><td>218.80 (n/a)</td><td>133.47 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1332.10 (n/a)</td><td>591.96 (n/a)</td><td>526.00 (n/a)</td><td>274.90 (n/a)</td><td>431.91 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>416.96 (n/a)</td><td>434.80 (n/a)</td><td>260.10 (n/a)</td><td>102.59 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.70 (n/a)</td><td>483.52 (n/a)</td><td>462.50 (n/a)</td><td>378.20 (n/a)</td><td>92.76 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.30 (n/a)</td><td>440.82 (n/a)</td><td>459.80 (n/a)</td><td>217.20 (n/a)</td><td>139.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>520.80 (n/a)</td><td>406.48 (n/a)</td><td>456.00 (n/a)</td><td>249.30 (n/a)</td><td>116.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1911.20 (n/a)</td><td>770.96 (n/a)</td><td>520.40 (n/a)</td><td>261.30 (n/a)</td><td>652.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.10 (n/a)</td><td>458.08 (n/a)</td><td>468.40 (n/a)</td><td>330.10 (n/a)</td><td>88.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>560.00 (n/a)</td><td>408.44 (n/a)</td><td>453.30 (n/a)</td><td>203.80 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>618.20 (n/a)</td><td>458.12 (n/a)</td><td>517.40 (n/a)</td><td>275.80 (n/a)</td><td>140.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>657.50 (n/a)</td><td>424.82 (n/a)</td><td>336.40 (n/a)</td><td>277.70 (n/a)</td><td>172.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1826.40 (n/a)</td><td>780.50 (n/a)</td><td>526.80 (n/a)</td><td>407.10 (n/a)</td><td>591.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>819.80 (n/a)</td><td>561.56 (n/a)</td><td>574.70 (n/a)</td><td>225.20 (n/a)</td><td>214.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.20 (n/a)</td><td>446.36 (n/a)</td><td>472.10 (n/a)</td><td>234.60 (n/a)</td><td>126.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1053.40 (n/a)</td><td>590.90 (n/a)</td><td>572.30 (n/a)</td><td>361.40 (n/a)</td><td>276.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>635.50 (n/a)</td><td>474.54 (n/a)</td><td>479.40 (n/a)</td><td>299.80 (n/a)</td><td>133.60 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-8.12%)</td><td>0.01 (-14.81%)</td><td>0.01 (-5.42%)</td><td>0.01 (-19.59%)</td><td>0.00 <b>(+37.45%)</b></td><td>467.80 <b>(+24.38%)</b></td><td>343.26 <b>(+22.08%)</b></td><td>282.90 (+5.72%)</td><td>260.00 (+8.83%)</td><td>101.78 <b>(+83.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>376.10 (n/a)</td><td>281.18 (n/a)</td><td>267.60 (n/a)</td><td>238.90 (n/a)</td><td>55.56 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+0.71%)</td><td>0.01 (+1.76%)</td><td>0.01 (+1.43%)</td><td>0.01 (+4.41%)</td><td>0.00 (-6.94%)</td><td>529.50 (-4.23%)</td><td>380.32 (-3.88%)</td><td>412.80 (-1.41%)</td><td>239.30 (-0.71%)</td><td>131.32 (-12.01%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.90 (n/a)</td><td>395.68 (n/a)</td><td>418.70 (n/a)</td><td>241.00 (n/a)</td><td>149.24 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-6.20%)</td><td>0.01 <b>(-33.56%)</b></td><td>0.01 <b>(-47.24%)</b></td><td>0.00 <b>(-60.65%)</b></td><td>0.01 <b>(+65.11%)</b></td><td>1037.90 <b>(+154.14%)</b></td><td>508.84 <b>(+88.58%)</b></td><td>451.50 <b>(+89.55%)</b></td><td>239.40 (+6.59%)</td><td>322.67 <b>(+315.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>408.40 (n/a)</td><td>269.82 (n/a)</td><td>238.20 (n/a)</td><td>224.60 (n/a)</td><td>77.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 <b>(-29.63%)</b></td><td>0.01 <b>(-23.62%)</b></td><td>0.01 <b>(-40.83%)</b></td><td>0.01 (+17.88%)</td><td>0.00 <b>(-39.08%)</b></td><td>490.30 (-15.16%)</td><td>398.42 <b>(+22.13%)</b></td><td>447.60 <b>(+69.03%)</b></td><td>284.20 <b>(+42.10%)</b></td><td>100.67 <b>(-31.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.90 (n/a)</td><td>326.22 (n/a)</td><td>264.80 (n/a)</td><td>200.00 (n/a)</td><td>147.89 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+0.21%)</td><td>0.01 (-15.21%)</td><td>0.01 <b>(-37.15%)</b></td><td>0.01 (-15.18%)</td><td>0.00 <b>(+45.04%)</b></td><td>614.80 (+17.91%)</td><td>428.32 <b>(+27.05%)</b></td><td>476.80 <b>(+59.09%)</b></td><td>246.70 (-0.20%)</td><td>164.74 <b>(+53.84%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.40 (n/a)</td><td>337.14 (n/a)</td><td>299.70 (n/a)</td><td>247.20 (n/a)</td><td>107.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+28.69%)</b></td><td>0.01 (-5.72%)</td><td>0.01 <b>(-22.83%)</b></td><td>0.01 (-3.63%)</td><td>0.00 <b>(+69.32%)</b></td><td>540.40 (+3.76%)</td><td>425.64 (+12.31%)</td><td>467.00 <b>(+29.58%)</b></td><td>229.10 <b>(-22.29%)</b></td><td>130.92 <b>(+40.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.80 (n/a)</td><td>378.98 (n/a)</td><td>360.40 (n/a)</td><td>294.80 (n/a)</td><td>93.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+32.85%)</b></td><td>0.03 <b>(+54.51%)</b></td><td>0.03 <b>(+48.98%)</b></td><td>0.02 <b>(+250.50%)</b></td><td>0.01 (-7.94%)</td><td>536.10 <b>(-71.47%)</b></td><td>343.34 <b>(-56.73%)</b></td><td>290.80 <b>(-32.87%)</b></td><td>201.00 <b>(-24.75%)</b></td><td>142.90 <b>(-79.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1879.00 (n/a)</td><td>793.50 (n/a)</td><td>433.20 (n/a)</td><td>267.10 (n/a)</td><td>690.58 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+9.74%)</td><td>0.02 (-2.81%)</td><td>0.02 <b>(-23.48%)</b></td><td>0.02 <b>(+22.91%)</b></td><td>0.01 (-15.57%)</td><td>468.20 (-18.63%)</td><td>355.92 (-1.34%)</td><td>371.10 <b>(+30.67%)</b></td><td>241.50 (-8.90%)</td><td>84.89 <b>(-36.73%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>360.74 (n/a)</td><td>284.00 (n/a)</td><td>265.10 (n/a)</td><td>134.17 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+23.77%)</b></td><td>0.03 <b>(+20.32%)</b></td><td>0.03 (+17.00%)</td><td>0.02 <b>(+25.48%)</b></td><td>0.01 (+6.24%)</td><td>350.00 <b>(-20.31%)</b></td><td>260.78 (-18.00%)</td><td>244.30 (-14.52%)</td><td>197.70 (-19.21%)</td><td>60.65 <b>(-29.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>439.20 (n/a)</td><td>318.02 (n/a)</td><td>285.80 (n/a)</td><td>244.70 (n/a)</td><td>85.83 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+5.00%)</td><td>0.02 (-10.42%)</td><td>0.02 (-9.11%)</td><td>0.00 <b>(-67.42%)</b></td><td>0.01 <b>(+49.48%)</b></td><td>1831.50 <b>(+206.94%)</b></td><td>633.86 <b>(+69.68%)</b></td><td>334.80 (+10.02%)</td><td>243.70 (-4.77%)</td><td>674.68 <b>(+378.48%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.70 (n/a)</td><td>373.56 (n/a)</td><td>304.30 (n/a)</td><td>255.90 (n/a)</td><td>141.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+28.67%)</b></td><td>0.02 (+15.78%)</td><td>0.02 <b>(+24.61%)</b></td><td>0.01 (+6.86%)</td><td>0.01 <b>(+42.63%)</b></td><td>586.70 (-6.41%)</td><td>436.30 (-9.84%)</td><td>429.20 (-19.76%)</td><td>196.80 <b>(-22.27%)</b></td><td>154.11 (+1.54%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.90 (n/a)</td><td>483.90 (n/a)</td><td>534.90 (n/a)</td><td>253.20 (n/a)</td><td>151.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+65.92%)</b></td><td>0.02 <b>(+20.80%)</b></td><td>0.02 (-1.10%)</td><td>0.01 <b>(-35.34%)</b></td><td>0.01 <b>(+404.10%)</b></td><td>799.80 <b>(+54.64%)</b></td><td>474.44 (+1.01%)</td><td>508.70 (+1.11%)</td><td>239.20 <b>(-39.72%)</b></td><td>232.34 <b>(+331.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>517.20 (n/a)</td><td>469.68 (n/a)</td><td>503.10 (n/a)</td><td>396.80 (n/a)</td><td>53.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+16.23%)</td><td>0.02 (-6.81%)</td><td>0.02 <b>(-22.37%)</b></td><td>0.01 (-8.75%)</td><td>0.01 <b>(+35.89%)</b></td><td>556.80 (+9.61%)</td><td>407.04 (+10.72%)</td><td>428.60 <b>(+28.82%)</b></td><td>237.00 (-13.97%)</td><td>119.09 <b>(+23.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.00 (n/a)</td><td>367.64 (n/a)</td><td>332.70 (n/a)</td><td>275.50 (n/a)</td><td>96.78 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (+18.46%)</td><td>0.02 (-6.69%)</td><td>0.02 (-18.30%)</td><td>0.01 <b>(-24.96%)</b></td><td>0.01 <b>(+62.85%)</b></td><td>664.60 <b>(+33.27%)</b></td><td>492.78 <b>(+20.69%)</b></td><td>538.80 <b>(+22.40%)</b></td><td>202.40 (-15.60%)</td><td>185.15 <b>(+87.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.70 (n/a)</td><td>408.30 (n/a)</td><td>440.20 (n/a)</td><td>239.80 (n/a)</td><td>98.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (-11.10%)</td><td>0.06 (-3.25%)</td><td>0.06 (-4.87%)</td><td>0.03 (+16.89%)</td><td>0.02 <b>(-22.87%)</b></td><td>512.50 (-14.44%)</td><td>302.58 (-2.79%)</td><td>260.80 (+5.12%)</td><td>215.80 (+12.45%)</td><td>119.22 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.00 (n/a)</td><td>311.26 (n/a)</td><td>248.10 (n/a)</td><td>191.90 (n/a)</td><td>163.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (+3.29%)</td><td>0.05 <b>(+29.98%)</b></td><td>0.06 <b>(+78.48%)</b></td><td>0.03 <b>(+292.00%)</b></td><td>0.02 <b>(-34.19%)</b></td><td>529.30 <b>(-74.49%)</b></td><td>347.40 <b>(-52.00%)</b></td><td>281.80 <b>(-43.97%)</b></td><td>239.10 (-3.20%)</td><td>121.08 <b>(-84.18%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2075.00 (n/a)</td><td>723.76 (n/a)</td><td>502.90 (n/a)</td><td>247.00 (n/a)</td><td>765.60 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (-18.14%)</td><td>0.05 (-5.24%)</td><td>0.06 (+1.84%)</td><td>0.03 <b>(-27.65%)</b></td><td>0.02 (-17.14%)</td><td>632.60 <b>(+38.21%)</b></td><td>349.44 (+6.84%)</td><td>271.00 (-1.81%)</td><td>227.90 <b>(+22.20%)</b></td><td>165.18 <b>(+34.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>457.70 (n/a)</td><td>327.06 (n/a)</td><td>276.00 (n/a)</td><td>186.50 (n/a)</td><td>123.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+14.68%)</td><td>0.05 (+2.24%)</td><td>0.06 (-6.30%)</td><td>0.03 <b>(-21.11%)</b></td><td>0.02 <b>(+35.32%)</b></td><td>540.30 <b>(+26.74%)</b></td><td>335.90 (+2.64%)</td><td>289.10 (+6.72%)</td><td>217.50 (-12.79%)</td><td>129.52 <b>(+46.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>426.30 (n/a)</td><td>327.26 (n/a)</td><td>270.90 (n/a)</td><td>249.40 (n/a)</td><td>88.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (-8.76%)</td><td>0.05 (-9.03%)</td><td>0.04 (-10.96%)</td><td>0.03 (-11.10%)</td><td>0.01 (-6.63%)</td><td>515.90 (+12.47%)</td><td>385.06 (+10.35%)</td><td>422.00 (+12.29%)</td><td>263.60 (+9.60%)</td><td>113.34 (+13.28%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>458.70 (n/a)</td><td>348.94 (n/a)</td><td>375.80 (n/a)</td><td>240.50 (n/a)</td><td>100.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (-11.90%)</td><td>0.04 (-6.24%)</td><td>0.03 (-5.26%)</td><td>0.03 (+14.89%)</td><td>0.01 <b>(-25.14%)</b></td><td>494.00 (-12.97%)</td><td>403.66 (+2.35%)</td><td>470.00 (+5.57%)</td><td>275.80 (+13.50%)</td><td>106.79 <b>(-21.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>567.60 (n/a)</td><td>394.40 (n/a)</td><td>445.20 (n/a)</td><td>243.00 (n/a)</td><td>136.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (-1.29%)</td><td>0.08 (-19.02%)</td><td>0.08 <b>(-21.13%)</b></td><td>0.05 (+6.47%)</td><td>0.03 (-3.89%)</td><td>663.70 (-6.08%)</td><td>446.60 <b>(+21.29%)</b></td><td>404.40 <b>(+26.81%)</b></td><td>248.20 (+1.31%)</td><td>175.17 (-9.09%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>706.70 (n/a)</td><td>368.20 (n/a)</td><td>318.90 (n/a)</td><td>245.00 (n/a)</td><td>192.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (-8.59%)</td><td>0.11 <b>(+24.72%)</b></td><td>0.12 <b>(+56.41%)</b></td><td>0.08 <b>(+31.84%)</b></td><td>0.03 <b>(-22.83%)</b></td><td>424.10 <b>(-24.16%)</b></td><td>324.26 <b>(-22.81%)</b></td><td>278.70 <b>(-36.06%)</b></td><td>252.80 (+9.39%)</td><td>82.97 <b>(-30.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.20 (n/a)</td><td>420.06 (n/a)</td><td>435.90 (n/a)</td><td>231.10 (n/a)</td><td>118.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (-1.56%)</td><td>0.11 (-5.97%)</td><td>0.14 <b>(+26.85%)</b></td><td>0.06 <b>(-23.71%)</b></td><td>0.04 <b>(+59.56%)</b></td><td>532.80 <b>(+31.07%)</b></td><td>345.94 (+17.58%)</td><td>236.90 <b>(-21.16%)</b></td><td>231.00 (+1.58%)</td><td>153.29 <b>(+112.73%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>406.50 (n/a)</td><td>294.22 (n/a)</td><td>300.50 (n/a)</td><td>227.40 (n/a)</td><td>72.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (+3.92%)</td><td>0.09 (-2.00%)</td><td>0.08 (+2.78%)</td><td>0.05 (-11.07%)</td><td>0.04 <b>(+23.49%)</b></td><td>634.00 (+12.45%)</td><td>414.42 (+7.57%)</td><td>396.60 (-2.70%)</td><td>245.90 (-3.79%)</td><td>168.93 <b>(+34.65%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>563.80 (n/a)</td><td>385.26 (n/a)</td><td>407.60 (n/a)</td><td>255.60 (n/a)</td><td>125.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 <b>(-30.90%)</b></td><td>0.07 <b>(-26.59%)</b></td><td>0.07 <b>(-36.85%)</b></td><td>0.05 (+0.62%)</td><td>0.01 <b>(-61.81%)</b></td><td>641.80 (-0.62%)</td><td>503.74 <b>(+26.37%)</b></td><td>503.40 <b>(+58.35%)</b></td><td>409.20 <b>(+44.70%)</b></td><td>86.48 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>645.80 (n/a)</td><td>398.62 (n/a)</td><td>317.90 (n/a)</td><td>282.80 (n/a)</td><td>153.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+18.81%)</td><td>0.01 (+12.26%)</td><td>0.01 (+1.95%)</td><td>0.01 (+14.96%)</td><td>0.00 (+12.33%)</td><td>482.00 (-13.01%)</td><td>361.80 (-11.36%)</td><td>388.70 (-1.92%)</td><td>243.70 (-15.85%)</td><td>100.25 (-17.19%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>408.18 (n/a)</td><td>396.30 (n/a)</td><td>289.60 (n/a)</td><td>121.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-12.61%)</td><td>0.01 (-18.80%)</td><td>0.01 <b>(-33.81%)</b></td><td>0.01 (-4.08%)</td><td>0.00 (-14.16%)</td><td>510.10 (+4.25%)</td><td>411.04 <b>(+22.21%)</b></td><td>446.40 <b>(+51.07%)</b></td><td>279.00 (+14.39%)</td><td>95.33 (-0.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.30 (n/a)</td><td>336.34 (n/a)</td><td>295.50 (n/a)</td><td>243.90 (n/a)</td><td>95.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 <b>(-20.87%)</b></td><td>0.01 (+0.36%)</td><td>0.01 (+16.13%)</td><td>0.01 (-8.10%)</td><td>0.00 <b>(-22.80%)</b></td><td>680.30 (+8.81%)</td><td>434.28 (-2.18%)</td><td>406.50 (-13.90%)</td><td>282.70 <b>(+26.37%)</b></td><td>163.65 (+7.73%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.20 (n/a)</td><td>443.96 (n/a)</td><td>472.10 (n/a)</td><td>223.70 (n/a)</td><td>151.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+12.20%)</td><td>0.01 (+10.17%)</td><td>0.02 <b>(+56.71%)</b></td><td>0.00 <b>(-55.14%)</b></td><td>0.01 <b>(+47.55%)</b></td><td>1029.40 <b>(+122.91%)</b></td><td>423.44 (+14.42%)</td><td>269.70 <b>(-36.18%)</b></td><td>216.50 (-10.87%)</td><td>341.89 <b>(+218.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.80 (n/a)</td><td>370.08 (n/a)</td><td>422.60 (n/a)</td><td>242.90 (n/a)</td><td>107.44 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-3.80%)</td><td>0.01 (+3.50%)</td><td>0.01 (+1.36%)</td><td>0.01 (+8.88%)</td><td>0.00 (-14.74%)</td><td>488.20 (-8.16%)</td><td>340.42 (-5.51%)</td><td>302.50 (-1.34%)</td><td>262.90 (+3.95%)</td><td>92.62 (-19.44%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.60 (n/a)</td><td>360.26 (n/a)</td><td>306.60 (n/a)</td><td>252.90 (n/a)</td><td>114.97 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+17.66%)</td><td>0.01 (-6.91%)</td><td>0.01 (-1.97%)</td><td>0.01 (-3.00%)</td><td>0.00 <b>(+41.19%)</b></td><td>570.90 (+3.11%)</td><td>383.36 (+13.18%)</td><td>296.30 (+2.03%)</td><td>233.60 (-14.99%)</td><td>153.69 <b>(+27.51%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.70 (n/a)</td><td>338.72 (n/a)</td><td>290.40 (n/a)</td><td>274.80 (n/a)</td><td>120.53 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 <b>(-34.47%)</b></td><td>0.01 <b>(-23.25%)</b></td><td>0.01 (-8.16%)</td><td>0.01 (-19.24%)</td><td>0.00 <b>(-57.19%)</b></td><td>688.70 <b>(+23.84%)</b></td><td>531.26 <b>(+23.15%)</b></td><td>526.50 (+8.89%)</td><td>424.30 <b>(+52.63%)</b></td><td>106.46 (-19.72%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.10 (n/a)</td><td>431.40 (n/a)</td><td>483.50 (n/a)</td><td>278.00 (n/a)</td><td>132.61 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (+13.43%)</td><td>0.01 (-0.47%)</td><td>0.01 (-5.65%)</td><td>0.01 (-20.00%)</td><td>0.00 <b>(+59.85%)</b></td><td>659.70 <b>(+25.01%)</b></td><td>436.62 (+6.62%)</td><td>400.70 (+5.98%)</td><td>284.50 (-11.84%)</td><td>154.61 <b>(+74.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.70 (n/a)</td><td>409.50 (n/a)</td><td>378.10 (n/a)</td><td>322.70 (n/a)</td><td>88.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-11.80%)</td><td>0.01 (+10.20%)</td><td>0.01 (+15.88%)</td><td>0.01 <b>(+58.46%)</b></td><td>0.00 <b>(-34.33%)</b></td><td>450.40 <b>(-36.89%)</b></td><td>350.28 (-16.70%)</td><td>317.40 (-13.68%)</td><td>274.00 (+13.36%)</td><td>82.71 <b>(-54.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>713.70 (n/a)</td><td>420.50 (n/a)</td><td>367.70 (n/a)</td><td>241.70 (n/a)</td><td>180.42 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+67.20%)</b></td><td>0.01 <b>(+26.89%)</b></td><td>0.01 (+1.61%)</td><td>0.01 (-17.57%)</td><td>0.01 <b>(+214.27%)</b></td><td>622.50 <b>(+21.32%)</b></td><td>394.04 (-8.55%)</td><td>429.30 (-1.58%)</td><td>198.00 <b>(-40.20%)</b></td><td>173.45 <b>(+116.04%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.10 (n/a)</td><td>430.86 (n/a)</td><td>436.20 (n/a)</td><td>331.10 (n/a)</td><td>80.29 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-0.69%)</td><td>0.01 <b>(+23.69%)</b></td><td>0.01 (+16.79%)</td><td>0.01 <b>(+57.70%)</b></td><td>0.00 <b>(-33.09%)</b></td><td>597.80 <b>(-36.59%)</b></td><td>515.40 <b>(-25.48%)</b></td><td>559.70 (-14.38%)</td><td>364.30 (+0.72%)</td><td>102.11 <b>(-57.10%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>942.80 (n/a)</td><td>691.64 (n/a)</td><td>653.70 (n/a)</td><td>361.70 (n/a)</td><td>238.04 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+26.64%)</b></td><td>0.02 (-5.36%)</td><td>0.01 (-12.70%)</td><td>0.01 <b>(-30.10%)</b></td><td>0.01 <b>(+79.65%)</b></td><td>936.50 <b>(+43.06%)</b></td><td>564.88 (+19.13%)</td><td>554.60 (+14.56%)</td><td>249.60 <b>(-21.04%)</b></td><td>245.70 <b>(+94.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.60 (n/a)</td><td>474.16 (n/a)</td><td>484.10 (n/a)</td><td>316.10 (n/a)</td><td>126.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+19.16%)</td><td>0.02 (+5.83%)</td><td>0.02 (-1.11%)</td><td>0.02 (-15.48%)</td><td>0.01 <b>(+111.81%)</b></td><td>531.70 (+18.31%)</td><td>389.44 (-1.13%)</td><td>397.40 (+1.12%)</td><td>279.10 (-16.09%)</td><td>105.93 <b>(+100.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>449.40 (n/a)</td><td>393.88 (n/a)</td><td>393.00 (n/a)</td><td>332.60 (n/a)</td><td>52.84 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+12.20%)</td><td>0.02 <b>(+26.07%)</b></td><td>0.02 <b>(+53.75%)</b></td><td>0.01 (+1.45%)</td><td>0.01 <b>(+38.02%)</b></td><td>607.30 (-1.44%)</td><td>434.90 (-18.17%)</td><td>364.20 <b>(-34.96%)</b></td><td>311.00 (-10.86%)</td><td>137.10 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.20 (n/a)</td><td>531.46 (n/a)</td><td>560.00 (n/a)</td><td>348.90 (n/a)</td><td>109.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+34.87%)</b></td><td>0.02 (+9.41%)</td><td>0.02 (-4.78%)</td><td>0.01 <b>(-25.59%)</b></td><td>0.01 <b>(+151.96%)</b></td><td>861.00 <b>(+34.38%)</b></td><td>537.16 (+2.83%)</td><td>538.40 (+5.01%)</td><td>302.10 <b>(-25.87%)</b></td><td>225.29 <b>(+142.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.70 (n/a)</td><td>522.38 (n/a)</td><td>512.70 (n/a)</td><td>407.50 (n/a)</td><td>93.01 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(-40.47%)</b></td><td>0.02 <b>(-21.80%)</b></td><td>0.02 (-11.36%)</td><td>0.02 (-7.07%)</td><td>0.00 <b>(-57.28%)</b></td><td>545.90 (+7.61%)</td><td>408.70 (+19.91%)</td><td>358.80 (+12.83%)</td><td>336.90 <b>(+68.03%)</b></td><td>89.89 <b>(-23.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>340.84 (n/a)</td><td>318.00 (n/a)</td><td>200.50 (n/a)</td><td>117.71 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (-0.93%)</td><td>0.03 (-13.25%)</td><td>0.03 (-11.49%)</td><td>0.02 <b>(-22.26%)</b></td><td>0.01 <b>(+63.72%)</b></td><td>465.80 <b>(+28.64%)</b></td><td>343.20 <b>(+21.68%)</b></td><td>307.70 (+13.00%)</td><td>232.70 (+0.95%)</td><td>106.21 <b>(+115.91%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>362.10 (n/a)</td><td>282.06 (n/a)</td><td>272.30 (n/a)</td><td>230.50 (n/a)</td><td>49.19 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (-1.07%)</td><td>0.02 (-1.39%)</td><td>0.02 (+0.25%)</td><td>0.01 (-3.31%)</td><td>0.01 (-1.28%)</td><td>587.20 (+3.42%)</td><td>438.34 (+1.44%)</td><td>520.50 (-0.27%)</td><td>241.30 (+1.05%)</td><td>158.34 (+1.88%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.80 (n/a)</td><td>432.10 (n/a)</td><td>521.90 (n/a)</td><td>238.80 (n/a)</td><td>155.42 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+22.30%)</b></td><td>0.02 (+3.29%)</td><td>0.02 (-15.17%)</td><td>0.02 <b>(+20.50%)</b></td><td>0.01 (-4.27%)</td><td>492.00 (-17.02%)</td><td>382.08 (-6.37%)</td><td>362.40 (+17.85%)</td><td>246.20 (-18.26%)</td><td>96.62 <b>(-33.07%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.90 (n/a)</td><td>408.06 (n/a)</td><td>307.50 (n/a)</td><td>301.20 (n/a)</td><td>144.36 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+19.98%)</td><td>0.03 <b>(+29.27%)</b></td><td>0.03 <b>(+92.53%)</b></td><td>0.01 (+6.26%)</td><td>0.01 <b>(+36.26%)</b></td><td>620.50 (-5.89%)</td><td>375.88 (-18.72%)</td><td>258.70 <b>(-48.06%)</b></td><td>242.30 (-16.65%)</td><td>176.23 (+9.20%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.30 (n/a)</td><td>462.46 (n/a)</td><td>498.10 (n/a)</td><td>290.70 (n/a)</td><td>161.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (+16.08%)</td><td>0.02 (+15.03%)</td><td>0.02 <b>(+32.08%)</b></td><td>0.02 <b>(+36.39%)</b></td><td>0.01 (+3.36%)</td><td>508.50 <b>(-26.68%)</b></td><td>365.46 (-16.32%)</td><td>359.90 <b>(-24.30%)</b></td><td>209.80 (-13.88%)</td><td>121.50 <b>(-31.86%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.50 (n/a)</td><td>436.72 (n/a)</td><td>475.40 (n/a)</td><td>243.60 (n/a)</td><td>178.30 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 <b>(+105.91%)</b></td><td>0.02 <b>(+22.32%)</b></td><td>0.02 (-13.25%)</td><td>0.02 (+14.09%)</td><td>0.01 <b>(+211.19%)</b></td><td>510.80 (-12.35%)</td><td>408.64 (-6.69%)</td><td>452.30 (+15.29%)</td><td>162.50 <b>(-51.45%)</b></td><td>140.43 <b>(+24.42%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.80 (n/a)</td><td>437.96 (n/a)</td><td>392.30 (n/a)</td><td>334.70 (n/a)</td><td>112.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (-14.30%)</td><td>0.02 (-19.71%)</td><td>0.02 <b>(-28.09%)</b></td><td>0.02 <b>(+21.38%)</b></td><td>0.01 <b>(-33.10%)</b></td><td>540.30 (-17.61%)</td><td>469.38 (+16.50%)</td><td>505.30 <b>(+39.05%)</b></td><td>289.20 (+16.71%)</td><td>103.14 <b>(-37.29%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.80 (n/a)</td><td>402.90 (n/a)</td><td>363.40 (n/a)</td><td>247.80 (n/a)</td><td>164.48 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (+11.52%)</td><td>0.05 (+2.42%)</td><td>0.06 <b>(+34.30%)</b></td><td>0.01 <b>(-69.95%)</b></td><td>0.03 <b>(+83.98%)</b></td><td>1823.40 <b>(+232.80%)</b></td><td>629.60 <b>(+58.16%)</b></td><td>265.30 <b>(-25.54%)</b></td><td>250.50 (-10.34%)</td><td>678.89 <b>(+429.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.90 (n/a)</td><td>398.08 (n/a)</td><td>356.30 (n/a)</td><td>279.40 (n/a)</td><td>128.17 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 <b>(+44.78%)</b></td><td>0.06 <b>(+22.80%)</b></td><td>0.06 (+6.85%)</td><td>0.03 (+4.05%)</td><td>0.02 <b>(+54.05%)</b></td><td>523.60 (-3.89%)</td><td>319.96 (-15.36%)</td><td>296.10 (-6.39%)</td><td>187.80 <b>(-30.91%)</b></td><td>127.56 (+4.47%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>378.04 (n/a)</td><td>316.30 (n/a)</td><td>271.80 (n/a)</td><td>122.10 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 <b>(+28.53%)</b></td><td>0.05 (+10.73%)</td><td>0.04 (+12.63%)</td><td>0.03 (+6.36%)</td><td>0.02 <b>(+46.28%)</b></td><td>479.20 (-5.98%)</td><td>387.98 (-7.36%)</td><td>415.40 (-11.22%)</td><td>217.90 <b>(-22.21%)</b></td><td>104.48 (+1.87%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>509.70 (n/a)</td><td>418.82 (n/a)</td><td>467.90 (n/a)</td><td>280.10 (n/a)</td><td>102.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (-11.96%)</td><td>0.05 (+8.79%)</td><td>0.06 <b>(+53.85%)</b></td><td>0.03 <b>(+27.25%)</b></td><td>0.02 <b>(-21.72%)</b></td><td>519.10 <b>(-21.41%)</b></td><td>351.92 (-13.49%)</td><td>277.70 <b>(-35.00%)</b></td><td>243.90 (+13.55%)</td><td>126.30 <b>(-27.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>660.50 (n/a)</td><td>406.78 (n/a)</td><td>427.20 (n/a)</td><td>214.80 (n/a)</td><td>174.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+27.21%)</b></td><td>0.05 <b>(+40.16%)</b></td><td>0.06 <b>(+83.23%)</b></td><td>0.03 (+3.51%)</td><td>0.02 <b>(+72.62%)</b></td><td>494.10 (-3.38%)</td><td>340.98 <b>(-23.96%)</b></td><td>269.60 <b>(-45.41%)</b></td><td>224.50 <b>(-21.37%)</b></td><td>130.77 <b>(+40.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>448.42 (n/a)</td><td>493.90 (n/a)</td><td>285.50 (n/a)</td><td>93.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (+10.70%)</td><td>0.05 (+7.53%)</td><td>0.06 <b>(+44.03%)</b></td><td>0.02 <b>(-45.72%)</b></td><td>0.02 <b>(+50.25%)</b></td><td>1019.00 <b>(+84.23%)</b></td><td>452.08 (+14.79%)</td><td>286.80 <b>(-30.57%)</b></td><td>225.90 (-9.64%)</td><td>331.39 <b>(+161.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.10 (n/a)</td><td>393.84 (n/a)</td><td>413.10 (n/a)</td><td>250.00 (n/a)</td><td>126.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 <b>(+32.19%)</b></td><td>0.05 <b>(+47.72%)</b></td><td>0.05 <b>(+87.14%)</b></td><td>0.03 <b>(+237.58%)</b></td><td>0.02 (-0.37%)</td><td>560.50 <b>(-70.38%)</b></td><td>352.96 <b>(-51.45%)</b></td><td>299.00 <b>(-46.56%)</b></td><td>196.40 <b>(-24.35%)</b></td><td>152.51 <b>(-77.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1892.20 (n/a)</td><td>727.06 (n/a)</td><td>559.50 (n/a)</td><td>259.60 (n/a)</td><td>670.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+23.87%)</b></td><td>0.05 (+9.42%)</td><td>0.04 (+18.51%)</td><td>0.03 (+9.62%)</td><td>0.01 <b>(+33.80%)</b></td><td>533.40 (-8.79%)</td><td>391.52 (-6.27%)</td><td>368.40 (-15.62%)</td><td>248.70 (-19.28%)</td><td>124.56 (+8.03%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.80 (n/a)</td><td>417.70 (n/a)</td><td>436.60 (n/a)</td><td>308.10 (n/a)</td><td>115.30 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (-17.39%)</td><td>0.04 (-16.94%)</td><td>0.03 (-16.01%)</td><td>0.03 (-6.02%)</td><td>0.01 <b>(-36.41%)</b></td><td>636.80 (+6.40%)</td><td>471.12 (+12.96%)</td><td>520.80 (+19.07%)</td><td>294.20 <b>(+21.07%)</b></td><td>135.93 (-16.83%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.50 (n/a)</td><td>417.08 (n/a)</td><td>437.40 (n/a)</td><td>243.00 (n/a)</td><td>163.44 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 <b>(+46.14%)</b></td><td>0.05 <b>(+33.63%)</b></td><td>0.05 <b>(+29.04%)</b></td><td>0.04 <b>(+20.06%)</b></td><td>0.01 <b>(+84.66%)</b></td><td>458.90 (-16.72%)</td><td>321.76 <b>(-23.74%)</b></td><td>301.10 <b>(-22.50%)</b></td><td>263.00 <b>(-31.56%)</b></td><td>78.61 (+8.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>551.00 (n/a)</td><td>421.94 (n/a)</td><td>388.50 (n/a)</td><td>384.30 (n/a)</td><td>72.40 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (-3.55%)</td><td>0.04 (-4.75%)</td><td>0.03 (-18.74%)</td><td>0.03 (-10.51%)</td><td>0.02 <b>(+28.67%)</b></td><td>623.70 (+11.75%)</td><td>465.26 (+10.86%)</td><td>508.00 <b>(+23.06%)</b></td><td>284.00 (+3.65%)</td><td>165.72 <b>(+46.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.10 (n/a)</td><td>419.68 (n/a)</td><td>412.80 (n/a)</td><td>274.00 (n/a)</td><td>112.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+20.19%)</b></td><td>0.04 (+10.99%)</td><td>0.03 (-5.27%)</td><td>0.02 <b>(+102.59%)</b></td><td>0.02 (+16.61%)</td><td>991.90 <b>(-50.64%)</b></td><td>577.24 <b>(-25.42%)</b></td><td>580.20 (+5.57%)</td><td>224.10 (-16.78%)</td><td>281.64 <b>(-59.80%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2009.40 (n/a)</td><td>773.98 (n/a)</td><td>549.60 (n/a)</td><td>269.30 (n/a)</td><td>700.53 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 <b>(-22.15%)</b></td><td>0.11 (+19.70%)</td><td>0.13 <b>(+85.10%)</b></td><td>0.06 (+7.06%)</td><td>0.03 <b>(-36.85%)</b></td><td>512.10 (-6.60%)</td><td>312.94 <b>(-21.94%)</b></td><td>256.30 <b>(-45.97%)</b></td><td>251.00 <b>(+28.45%)</b></td><td>112.55 <b>(-22.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>548.30 (n/a)</td><td>400.92 (n/a)</td><td>474.40 (n/a)</td><td>195.40 (n/a)</td><td>144.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (+0.26%)</td><td>0.11 (-3.33%)</td><td>0.12 (+7.26%)</td><td>0.07 <b>(-30.56%)</b></td><td>0.02 <b>(+196.23%)</b></td><td>454.60 <b>(+44.00%)</b></td><td>317.36 (+7.26%)</td><td>277.40 (-6.76%)</td><td>266.70 (-0.26%)</td><td>78.93 <b>(+335.62%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>315.70 (n/a)</td><td>295.88 (n/a)</td><td>297.50 (n/a)</td><td>267.40 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (+11.33%)</td><td>0.10 (+10.40%)</td><td>0.12 (+10.70%)</td><td>0.05 <b>(+27.22%)</b></td><td>0.03 (+10.90%)</td><td>596.70 <b>(-21.39%)</b></td><td>363.86 (-11.38%)</td><td>281.80 (-9.68%)</td><td>252.40 (-10.15%)</td><td>147.57 <b>(-26.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>759.10 (n/a)</td><td>410.60 (n/a)</td><td>312.00 (n/a)</td><td>280.90 (n/a)</td><td>199.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (+2.15%)</td><td>0.09 (-8.10%)</td><td>0.08 <b>(-25.74%)</b></td><td>0.07 <b>(+27.95%)</b></td><td>0.03 (-3.77%)</td><td>493.30 <b>(-21.83%)</b></td><td>379.48 (+5.31%)</td><td>401.00 <b>(+34.65%)</b></td><td>272.20 (-2.12%)</td><td>102.39 <b>(-32.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>631.10 (n/a)</td><td>360.34 (n/a)</td><td>297.80 (n/a)</td><td>278.10 (n/a)</td><td>151.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (-0.66%)</td><td>0.11 (+12.56%)</td><td>0.11 <b>(+52.72%)</b></td><td>0.06 (+10.13%)</td><td>0.04 (-15.80%)</td><td>557.80 (-9.21%)</td><td>340.42 (-15.99%)</td><td>305.80 <b>(-34.52%)</b></td><td>202.70 (+0.65%)</td><td>138.83 (-19.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>614.40 (n/a)</td><td>405.20 (n/a)</td><td>467.00 (n/a)</td><td>201.40 (n/a)</td><td>172.61 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (-5.94%)</td><td>0.08 (-18.29%)</td><td>0.07 <b>(-38.57%)</b></td><td>0.06 (-5.42%)</td><td>0.03 (+1.55%)</td><td>514.50 (+5.73%)</td><td>431.20 <b>(+23.57%)</b></td><td>498.40 <b>(+62.77%)</b></td><td>249.40 (+6.31%)</td><td>113.70 (+12.48%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>486.60 (n/a)</td><td>348.94 (n/a)</td><td>306.20 (n/a)</td><td>234.60 (n/a)</td><td>101.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 <b>(+30.06%)</b></td><td>0.12 <b>(+48.05%)</b></td><td>0.12 <b>(+70.82%)</b></td><td>0.06 <b>(+29.65%)</b></td><td>0.05 <b>(+62.41%)</b></td><td>533.70 <b>(-22.86%)</b></td><td>340.24 <b>(-26.53%)</b></td><td>276.50 <b>(-41.46%)</b></td><td>183.90 <b>(-23.09%)</b></td><td>169.92 (+5.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>691.90 (n/a)</td><td>463.08 (n/a)</td><td>472.30 (n/a)</td><td>239.10 (n/a)</td><td>160.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (-3.88%)</td><td>0.09 (+16.58%)</td><td>0.07 (+16.61%)</td><td>0.06 (+18.22%)</td><td>0.03 (-5.61%)</td><td>517.10 (-15.42%)</td><td>397.70 (-15.41%)</td><td>447.10 (-14.25%)</td><td>238.40 (+4.01%)</td><td>132.37 (-8.32%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>611.40 (n/a)</td><td>470.16 (n/a)</td><td>521.40 (n/a)</td><td>229.20 (n/a)</td><td>144.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 <b>(+60.41%)</b></td><td>0.10 <b>(+26.00%)</b></td><td>0.07 (-6.76%)</td><td>0.06 (-5.77%)</td><td>0.05 <b>(+149.86%)</b></td><td>576.90 (+6.13%)</td><td>408.78 (-9.21%)</td><td>490.60 (+7.26%)</td><td>186.90 <b>(-37.66%)</b></td><td>167.67 <b>(+64.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>543.60 (n/a)</td><td>450.24 (n/a)</td><td>457.40 (n/a)</td><td>299.80 (n/a)</td><td>102.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (+19.09%)</td><td>0.08 (+2.32%)</td><td>0.07 (+9.24%)</td><td>0.06 (+12.24%)</td><td>0.04 (+13.62%)</td><td>510.90 (-10.90%)</td><td>431.38 (-3.01%)</td><td>486.10 (-8.46%)</td><td>222.80 (-16.02%)</td><td>120.76 (-18.34%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>573.40 (n/a)</td><td>444.78 (n/a)</td><td>531.00 (n/a)</td><td>265.30 (n/a)</td><td>147.88 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (-16.70%)</td><td>0.07 (-13.26%)</td><td>0.06 (-0.08%)</td><td>0.05 (-10.60%)</td><td>0.03 <b>(-24.26%)</b></td><td>648.20 (+11.86%)</td><td>486.18 (+12.24%)</td><td>520.50 (+0.10%)</td><td>288.90 <b>(+20.02%)</b></td><td>153.17 (+1.67%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>579.50 (n/a)</td><td>433.18 (n/a)</td><td>520.00 (n/a)</td><td>240.70 (n/a)</td><td>150.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (-10.16%)</td><td>0.10 <b>(+29.31%)</b></td><td>0.11 <b>(+70.54%)</b></td><td>0.06 <b>(+261.55%)</b></td><td>0.03 <b>(-41.97%)</b></td><td>518.00 <b>(-72.34%)</b></td><td>366.96 <b>(-48.62%)</b></td><td>292.30 <b>(-41.36%)</b></td><td>277.60 (+11.31%)</td><td>111.53 <b>(-83.22%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1872.70 (n/a)</td><td>714.18 (n/a)</td><td>498.50 (n/a)</td><td>249.40 (n/a)</td><td>664.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-8.03%)</td><td>0.08 (+1.68%)</td><td>0.08 (-0.99%)</td><td>0.05 (-6.93%)</td><td>0.02 (-1.84%)</td><td>495.90 (+7.45%)</td><td>320.02 (-0.92%)</td><td>294.20 (+1.00%)</td><td>235.00 (+8.75%)</td><td>106.10 (+13.09%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>461.50 (n/a)</td><td>322.98 (n/a)</td><td>291.30 (n/a)</td><td>216.10 (n/a)</td><td>93.82 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.22 (+10.64%)</td><td>0.16 (-6.01%)</td><td>0.19 (+8.68%)</td><td>0.09 <b>(-34.59%)</b></td><td>0.05 <b>(+131.38%)</b></td><td>565.50 <b>(+52.88%)</b></td><td>343.94 (+17.55%)</td><td>264.00 (-7.98%)</td><td>226.90 (-9.64%)</td><td>142.72 <b>(+211.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>369.90 (n/a)</td><td>292.60 (n/a)</td><td>286.90 (n/a)</td><td>251.10 (n/a)</td><td>45.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.90 (-9.15%)</td><td>3.10 (-5.89%)</td><td>2.69 (-10.22%)</td><td>2.38 (-12.00%)</td><td>0.72 (+10.46%)</td><td>4398.10 (+13.64%)</td><td>3532.32 (+7.66%)</td><td>3892.30 (+11.38%)</td><td>2689.20 (+10.07%)</td><td>780.22 <b>(+32.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>4.29 (n/a)</td><td>3.29 (n/a)</td><td>3.00 (n/a)</td><td>2.71 (n/a)</td><td>0.65 (n/a)</td><td>3870.20 (n/a)</td><td>3280.88 (n/a)</td><td>3494.70 (n/a)</td><td>2443.20 (n/a)</td><td>589.36 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (-4.03%)</td><td>0.11 (-2.99%)</td><td>0.09 (-11.37%)</td><td>0.07 (-14.78%)</td><td>0.04 (+13.22%)</td><td>587.80 (+17.35%)</td><td>409.26 (+6.69%)</td><td>459.70 (+12.84%)</td><td>252.10 (+4.17%)</td><td>149.37 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>500.90 (n/a)</td><td>383.60 (n/a)</td><td>407.40 (n/a)</td><td>242.00 (n/a)</td><td>118.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+26.30%)</b></td><td>0.02 <b>(+29.80%)</b></td><td>0.02 <b>(+45.20%)</b></td><td>0.01 (-0.42%)</td><td>0.01 <b>(+73.45%)</b></td><td>523.00 (+0.42%)</td><td>316.32 (-18.53%)</td><td>257.50 <b>(-31.13%)</b></td><td>220.60 <b>(-20.82%)</b></td><td>123.68 <b>(+40.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.80 (n/a)</td><td>388.28 (n/a)</td><td>373.90 (n/a)</td><td>278.60 (n/a)</td><td>87.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+5.15%)</td><td>0.01 (+6.71%)</td><td>0.01 (+4.63%)</td><td>0.01 (+2.77%)</td><td>0.00 (+0.10%)</td><td>479.80 (-2.70%)</td><td>332.48 (-6.99%)</td><td>283.70 (-4.41%)</td><td>237.50 (-4.92%)</td><td>100.93 (-9.85%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.10 (n/a)</td><td>357.48 (n/a)</td><td>296.80 (n/a)</td><td>249.80 (n/a)</td><td>111.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+2.72%)</td><td>0.02 (+1.70%)</td><td>0.02 (+7.18%)</td><td>0.01 <b>(+22.95%)</b></td><td>0.01 (-2.37%)</td><td>504.20 (-18.66%)</td><td>374.10 (-3.57%)</td><td>331.10 (-6.68%)</td><td>230.20 (-2.62%)</td><td>120.90 (-18.75%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.90 (n/a)</td><td>387.96 (n/a)</td><td>354.80 (n/a)</td><td>236.40 (n/a)</td><td>148.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+4.00%)</td><td>0.01 (-2.74%)</td><td>0.01 (-13.35%)</td><td>0.01 (+7.97%)</td><td>0.00 (-13.46%)</td><td>514.70 (-7.38%)</td><td>355.44 (-2.86%)</td><td>307.40 (+15.39%)</td><td>209.40 (-3.86%)</td><td>125.02 <b>(-25.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.70 (n/a)</td><td>365.92 (n/a)</td><td>266.40 (n/a)</td><td>217.80 (n/a)</td><td>168.27 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+5.65%)</td><td>0.02 (+11.89%)</td><td>0.02 <b>(+72.20%)</b></td><td>0.01 (+0.85%)</td><td>0.01 (-1.38%)</td><td>579.70 (-0.86%)</td><td>381.64 (-10.95%)</td><td>294.90 <b>(-41.93%)</b></td><td>235.80 (-5.34%)</td><td>156.83 (-0.74%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.70 (n/a)</td><td>428.56 (n/a)</td><td>507.80 (n/a)</td><td>249.10 (n/a)</td><td>158.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-9.49%)</td><td>0.01 <b>(-39.97%)</b></td><td>0.01 <b>(-49.68%)</b></td><td>0.00 <b>(-25.69%)</b></td><td>0.01 (-19.09%)</td><td>2467.80 <b>(+34.57%)</b></td><td>869.26 <b>(+53.52%)</b></td><td>503.00 <b>(+98.74%)</b></td><td>256.50 (+10.47%)</td><td>904.92 <b>(+27.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1833.80 (n/a)</td><td>566.22 (n/a)</td><td>253.10 (n/a)</td><td>232.20 (n/a)</td><td>708.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-5.45%)</td><td>0.01 <b>(+23.06%)</b></td><td>0.01 <b>(+35.79%)</b></td><td>0.01 <b>(+45.39%)</b></td><td>0.01 <b>(-23.70%)</b></td><td>529.90 <b>(-31.22%)</b></td><td>386.84 <b>(-26.52%)</b></td><td>406.80 <b>(-26.37%)</b></td><td>215.00 (+5.76%)</td><td>126.10 <b>(-38.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>770.40 (n/a)</td><td>526.48 (n/a)</td><td>552.50 (n/a)</td><td>203.30 (n/a)</td><td>204.58 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (-6.31%)</td><td>0.01 (-6.98%)</td><td>0.01 (-8.94%)</td><td>0.01 (-17.33%)</td><td>0.00 (+19.98%)</td><td>656.80 <b>(+20.96%)</b></td><td>445.10 (+12.77%)</td><td>458.00 (+9.83%)</td><td>280.40 (+6.74%)</td><td>162.39 <b>(+48.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.00 (n/a)</td><td>394.68 (n/a)</td><td>417.00 (n/a)</td><td>262.70 (n/a)</td><td>109.62 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+1.83%)</td><td>0.01 (+2.18%)</td><td>0.01 <b>(-20.19%)</b></td><td>0.01 (-16.95%)</td><td>0.01 <b>(+36.90%)</b></td><td>666.80 <b>(+20.40%)</b></td><td>423.28 (+7.01%)</td><td>473.30 <b>(+25.31%)</b></td><td>226.70 (-1.78%)</td><td>185.75 <b>(+54.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.80 (n/a)</td><td>395.54 (n/a)</td><td>377.70 (n/a)</td><td>230.80 (n/a)</td><td>120.35 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+15.07%)</td><td>0.01 <b>(+27.90%)</b></td><td>0.01 <b>(+51.22%)</b></td><td>0.01 (+19.09%)</td><td>0.00 (+14.39%)</td><td>641.60 (-16.03%)</td><td>358.60 <b>(-21.65%)</b></td><td>290.90 <b>(-33.89%)</b></td><td>242.50 (-13.11%)</td><td>162.20 (-13.16%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>764.10 (n/a)</td><td>457.68 (n/a)</td><td>440.00 (n/a)</td><td>279.10 (n/a)</td><td>186.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (+1.12%)</td><td>0.01 (-8.30%)</td><td>0.01 (-8.18%)</td><td>0.00 <b>(-44.53%)</b></td><td>0.00 <b>(+21.06%)</b></td><td>2077.10 <b>(+80.26%)</b></td><td>828.56 <b>(+32.87%)</b></td><td>525.70 (+8.91%)</td><td>404.70 (-1.10%)</td><td>702.36 <b>(+130.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1152.30 (n/a)</td><td>623.60 (n/a)</td><td>482.70 (n/a)</td><td>409.20 (n/a)</td><td>304.50 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+2.05%)</td><td>0.01 (+7.75%)</td><td>0.01 (-7.45%)</td><td>0.01 <b>(+29.19%)</b></td><td>0.00 (-19.10%)</td><td>513.60 <b>(-22.59%)</b></td><td>384.96 (-13.44%)</td><td>370.30 (+8.05%)</td><td>252.00 (-1.98%)</td><td>107.32 <b>(-41.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.50 (n/a)</td><td>444.74 (n/a)</td><td>342.70 (n/a)</td><td>257.10 (n/a)</td><td>184.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (-14.91%)</td><td>0.02 <b>(-27.79%)</b></td><td>0.02 <b>(-47.51%)</b></td><td>0.01 (-4.00%)</td><td>0.01 <b>(-35.22%)</b></td><td>661.60 (+4.16%)</td><td>486.44 <b>(+26.90%)</b></td><td>503.60 <b>(+90.47%)</b></td><td>274.10 (+17.54%)</td><td>138.18 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.20 (n/a)</td><td>383.32 (n/a)</td><td>264.40 (n/a)</td><td>233.20 (n/a)</td><td>186.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (-12.86%)</td><td>0.03 <b>(-36.61%)</b></td><td>0.03 <b>(-38.07%)</b></td><td>0.02 <b>(-53.94%)</b></td><td>0.01 <b>(+254.64%)</b></td><td>662.30 <b>(+117.15%)</b></td><td>471.26 <b>(+68.09%)</b></td><td>449.60 <b>(+61.49%)</b></td><td>301.80 (+14.75%)</td><td>132.21 <b>(+765.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>305.00 (n/a)</td><td>280.36 (n/a)</td><td>278.40 (n/a)</td><td>263.00 (n/a)</td><td>15.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (-14.06%)</td><td>0.02 (+9.57%)</td><td>0.02 <b>(+29.42%)</b></td><td>0.01 <b>(-40.13%)</b></td><td>0.01 (+2.57%)</td><td>1062.10 <b>(+67.05%)</b></td><td>515.22 (+2.36%)</td><td>428.90 <b>(-22.73%)</b></td><td>268.70 (+16.37%)</td><td>326.12 <b>(+103.88%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.80 (n/a)</td><td>503.32 (n/a)</td><td>555.10 (n/a)</td><td>230.90 (n/a)</td><td>159.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (+7.93%)</td><td>0.03 (-17.76%)</td><td>0.02 <b>(-43.26%)</b></td><td>0.02 (-7.94%)</td><td>0.01 (+12.54%)</td><td>593.90 (+8.61%)</td><td>460.84 <b>(+23.20%)</b></td><td>505.70 <b>(+76.26%)</b></td><td>216.30 (-7.37%)</td><td>147.84 (+0.35%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.80 (n/a)</td><td>374.06 (n/a)</td><td>286.90 (n/a)</td><td>233.50 (n/a)</td><td>147.32 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (+11.87%)</td><td>0.02 (+10.27%)</td><td>0.02 (+12.33%)</td><td>0.01 (-16.57%)</td><td>0.01 <b>(+28.03%)</b></td><td>661.20 (+19.85%)</td><td>390.42 (-3.04%)</td><td>377.70 (-10.98%)</td><td>198.90 (-10.61%)</td><td>179.40 <b>(+38.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.70 (n/a)</td><td>402.66 (n/a)</td><td>424.30 (n/a)</td><td>222.50 (n/a)</td><td>129.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+41.66%)</b></td><td>0.03 (+2.05%)</td><td>0.02 <b>(-33.82%)</b></td><td>0.02 (+17.39%)</td><td>0.02 <b>(+54.47%)</b></td><td>521.00 (-14.81%)</td><td>390.40 (+2.38%)</td><td>417.00 <b>(+51.09%)</b></td><td>141.50 <b>(-29.43%)</b></td><td>152.87 (-17.28%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>381.32 (n/a)</td><td>276.00 (n/a)</td><td>200.50 (n/a)</td><td>184.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(-20.16%)</b></td><td>0.02 <b>(+37.69%)</b></td><td>0.03 <b>(+59.04%)</b></td><td>0.01 <b>(+222.53%)</b></td><td>0.01 <b>(-35.75%)</b></td><td>754.00 <b>(-69.00%)</b></td><td>390.38 <b>(-53.50%)</b></td><td>304.90 <b>(-37.12%)</b></td><td>291.00 <b>(+25.27%)</b></td><td>203.35 <b>(-77.40%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2431.90 (n/a)</td><td>839.58 (n/a)</td><td>484.90 (n/a)</td><td>232.30 (n/a)</td><td>899.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 <b>(+22.88%)</b></td><td>0.02 <b>(+23.75%)</b></td><td>0.02 <b>(+26.81%)</b></td><td>0.02 (+2.96%)</td><td>0.01 <b>(+50.08%)</b></td><td>568.30 (-2.87%)</td><td>402.06 (-17.43%)</td><td>392.00 <b>(-21.14%)</b></td><td>294.50 (-18.62%)</td><td>103.96 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>585.10 (n/a)</td><td>486.94 (n/a)</td><td>497.10 (n/a)</td><td>361.90 (n/a)</td><td>84.54 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (+6.44%)</td><td>0.02 (-2.29%)</td><td>0.02 (+0.64%)</td><td>0.00 (-3.57%)</td><td>0.01 (+10.73%)</td><td>2044.60 (+3.70%)</td><td>787.22 (+5.70%)</td><td>497.40 (-0.64%)</td><td>246.60 (-6.02%)</td><td>718.90 (+3.62%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1971.60 (n/a)</td><td>744.76 (n/a)</td><td>500.60 (n/a)</td><td>262.40 (n/a)</td><td>693.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+29.37%)</b></td><td>0.03 <b>(+20.55%)</b></td><td>0.02 (+14.68%)</td><td>0.02 <b>(+28.92%)</b></td><td>0.01 <b>(+22.87%)</b></td><td>439.90 <b>(-22.43%)</b></td><td>356.88 (-17.53%)</td><td>382.10 (-12.80%)</td><td>227.30 <b>(-22.69%)</b></td><td>90.45 <b>(-25.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>432.76 (n/a)</td><td>438.20 (n/a)</td><td>294.00 (n/a)</td><td>121.69 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(+21.78%)</b></td><td>0.02 <b>(+21.46%)</b></td><td>0.02 (+10.75%)</td><td>0.02 (+11.09%)</td><td>0.01 <b>(+34.11%)</b></td><td>504.80 (-9.97%)</td><td>397.86 (-15.15%)</td><td>464.20 (-9.72%)</td><td>215.20 (-17.89%)</td><td>127.51 (+6.13%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.70 (n/a)</td><td>468.88 (n/a)</td><td>514.20 (n/a)</td><td>262.10 (n/a)</td><td>120.15 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+28.97%)</b></td><td>0.05 <b>(+32.37%)</b></td><td>0.06 <b>(+57.17%)</b></td><td>0.03 (+9.73%)</td><td>0.01 <b>(+83.75%)</b></td><td>477.50 (-8.87%)</td><td>338.30 <b>(-21.30%)</b></td><td>281.60 <b>(-36.36%)</b></td><td>249.90 <b>(-22.44%)</b></td><td>104.94 <b>(+29.51%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>524.00 (n/a)</td><td>429.84 (n/a)</td><td>442.50 (n/a)</td><td>322.20 (n/a)</td><td>81.03 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (+12.10%)</td><td>0.08 <b>(+27.43%)</b></td><td>0.08 <b>(+76.54%)</b></td><td>0.05 <b>(+50.41%)</b></td><td>0.02 <b>(-32.10%)</b></td><td>460.80 <b>(-33.51%)</b></td><td>341.32 <b>(-28.54%)</b></td><td>308.10 <b>(-43.35%)</b></td><td>253.10 (-10.79%)</td><td>81.33 <b>(-55.65%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>693.00 (n/a)</td><td>477.62 (n/a)</td><td>543.90 (n/a)</td><td>283.70 (n/a)</td><td>183.40 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (-8.18%)</td><td>0.05 (+17.95%)</td><td>0.06 <b>(+66.18%)</b></td><td>0.03 (+15.50%)</td><td>0.02 (-13.08%)</td><td>598.70 (-13.42%)</td><td>357.48 (-19.17%)</td><td>272.60 <b>(-39.82%)</b></td><td>236.70 (+8.88%)</td><td>157.30 (-19.35%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>691.50 (n/a)</td><td>442.24 (n/a)</td><td>453.00 (n/a)</td><td>217.40 (n/a)</td><td>195.03 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+5.33%)</td><td>0.06 (+19.21%)</td><td>0.06 <b>(+38.49%)</b></td><td>0.04 (+12.55%)</td><td>0.02 (+13.62%)</td><td>578.50 (-11.15%)</td><td>396.04 (-15.55%)</td><td>349.40 <b>(-27.79%)</b></td><td>264.90 (-5.05%)</td><td>146.42 (-6.46%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.10 (n/a)</td><td>468.94 (n/a)</td><td>483.90 (n/a)</td><td>279.00 (n/a)</td><td>156.52 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 <b>(-39.77%)</b></td><td>0.04 <b>(-32.09%)</b></td><td>0.04 <b>(-33.31%)</b></td><td>0.03 (-19.86%)</td><td>0.01 <b>(-56.85%)</b></td><td>505.40 <b>(+24.79%)</b></td><td>431.64 <b>(+43.96%)</b></td><td>444.30 <b>(+49.95%)</b></td><td>370.20 <b>(+66.01%)</b></td><td>56.99 (-13.93%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>405.00 (n/a)</td><td>299.84 (n/a)</td><td>296.30 (n/a)</td><td>223.00 (n/a)</td><td>66.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (-4.50%)</td><td>0.06 (+13.91%)</td><td>0.07 <b>(+55.32%)</b></td><td>0.03 (+3.14%)</td><td>0.02 (+0.87%)</td><td>585.70 (-3.06%)</td><td>382.26 (-11.81%)</td><td>299.50 <b>(-35.62%)</b></td><td>239.80 (+4.72%)</td><td>167.21 (+1.21%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.20 (n/a)</td><td>433.44 (n/a)</td><td>465.20 (n/a)</td><td>229.00 (n/a)</td><td>165.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (-5.55%)</td><td>0.05 (+5.89%)</td><td>0.06 (+4.80%)</td><td>0.04 (+4.47%)</td><td>0.01 <b>(-21.68%)</b></td><td>458.10 (-4.28%)</td><td>326.14 (-8.36%)</td><td>282.00 (-4.57%)</td><td>255.30 (+5.89%)</td><td>82.79 <b>(-24.77%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>355.90 (n/a)</td><td>295.50 (n/a)</td><td>241.10 (n/a)</td><td>110.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+0.54%)</td><td>0.05 <b>(+41.41%)</b></td><td>0.05 <b>(+38.81%)</b></td><td>0.03 <b>(+231.50%)</b></td><td>0.02 (-13.59%)</td><td>561.80 <b>(-69.83%)</b></td><td>389.16 <b>(-47.67%)</b></td><td>390.10 <b>(-27.97%)</b></td><td>238.80 (-0.54%)</td><td>146.49 <b>(-77.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1862.40 (n/a)</td><td>743.72 (n/a)</td><td>541.60 (n/a)</td><td>240.10 (n/a)</td><td>638.62 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 <b>(+31.82%)</b></td><td>0.06 <b>(+31.96%)</b></td><td>0.05 <b>(+58.54%)</b></td><td>0.03 (-2.03%)</td><td>0.02 <b>(+30.40%)</b></td><td>601.20 (+2.09%)</td><td>333.34 <b>(-21.60%)</b></td><td>302.50 <b>(-36.93%)</b></td><td>185.70 <b>(-24.14%)</b></td><td>158.50 (+7.97%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.90 (n/a)</td><td>425.20 (n/a)</td><td>479.60 (n/a)</td><td>244.80 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (-15.04%)</td><td>0.05 (-3.21%)</td><td>0.05 <b>(+30.17%)</b></td><td>0.03 (-8.41%)</td><td>0.02 <b>(-26.31%)</b></td><td>684.40 (+9.17%)</td><td>428.50 (-1.63%)</td><td>368.10 <b>(-23.18%)</b></td><td>273.10 (+17.72%)</td><td>173.58 (-4.89%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>626.90 (n/a)</td><td>435.60 (n/a)</td><td>479.20 (n/a)</td><td>232.00 (n/a)</td><td>182.50 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (+13.55%)</td><td>0.05 <b>(+41.08%)</b></td><td>0.05 <b>(+66.82%)</b></td><td>0.03 <b>(+21.34%)</b></td><td>0.01 (+14.19%)</td><td>523.40 (-17.57%)</td><td>360.14 <b>(-29.36%)</b></td><td>333.20 <b>(-40.05%)</b></td><td>259.60 (-11.94%)</td><td>111.56 (-16.59%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>635.00 (n/a)</td><td>509.82 (n/a)</td><td>555.80 (n/a)</td><td>294.80 (n/a)</td><td>133.75 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (-5.05%)</td><td>0.10 (+14.36%)</td><td>0.11 <b>(+47.64%)</b></td><td>0.07 (-0.83%)</td><td>0.03 (-19.74%)</td><td>483.20 (+0.83%)</td><td>339.34 (-14.82%)</td><td>311.20 <b>(-32.27%)</b></td><td>232.80 (+5.34%)</td><td>94.94 (-13.41%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>479.20 (n/a)</td><td>398.36 (n/a)</td><td>459.50 (n/a)</td><td>221.00 (n/a)</td><td>109.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 <b>(-33.59%)</b></td><td>0.11 (+1.10%)</td><td>0.11 <b>(+32.73%)</b></td><td>0.08 (+15.62%)</td><td>0.03 <b>(-53.01%)</b></td><td>425.60 (-13.51%)</td><td>320.26 (-12.49%)</td><td>305.20 <b>(-24.66%)</b></td><td>233.50 <b>(+50.55%)</b></td><td>85.73 <b>(-38.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>492.10 (n/a)</td><td>365.98 (n/a)</td><td>405.10 (n/a)</td><td>155.10 (n/a)</td><td>139.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 <b>(-51.55%)</b></td><td>0.10 (-19.03%)</td><td>0.10 (-3.40%)</td><td>0.05 <b>(+143.80%)</b></td><td>0.04 <b>(-62.27%)</b></td><td>779.40 <b>(-58.99%)</b></td><td>458.68 <b>(-29.76%)</b></td><td>393.80 (+3.50%)</td><td>293.20 <b>(+106.48%)</b></td><td>203.38 <b>(-71.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>1900.30 (n/a)</td><td>653.04 (n/a)</td><td>380.50 (n/a)</td><td>142.00 (n/a)</td><td>712.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (+7.02%)</td><td>0.10 <b>(+20.29%)</b></td><td>0.11 <b>(+67.42%)</b></td><td>0.06 (-2.34%)</td><td>0.03 <b>(+21.44%)</b></td><td>555.00 (+2.40%)</td><td>370.98 (-14.37%)</td><td>296.70 <b>(-40.27%)</b></td><td>248.00 (-6.56%)</td><td>137.44 (+17.29%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>542.00 (n/a)</td><td>433.26 (n/a)</td><td>496.70 (n/a)</td><td>265.40 (n/a)</td><td>117.18 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-4.80%)</td><td>0.11 (+3.46%)</td><td>0.14 <b>(+60.61%)</b></td><td>0.04 <b>(-46.61%)</b></td><td>0.05 <b>(+32.06%)</b></td><td>959.40 <b>(+87.31%)</b></td><td>465.06 (+12.45%)</td><td>300.20 <b>(-37.73%)</b></td><td>273.80 (+5.02%)</td><td>294.32 <b>(+140.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>512.20 (n/a)</td><td>413.56 (n/a)</td><td>482.10 (n/a)</td><td>260.70 (n/a)</td><td>122.33 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (-0.49%)</td><td>0.11 (+19.85%)</td><td>0.11 <b>(+61.30%)</b></td><td>0.05 (+7.71%)</td><td>0.04 (-11.17%)</td><td>638.00 (-7.16%)</td><td>346.26 (-19.55%)</td><td>303.30 <b>(-38.01%)</b></td><td>209.10 (+0.53%)</td><td>171.11 (-10.72%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>687.20 (n/a)</td><td>430.42 (n/a)</td><td>489.30 (n/a)</td><td>208.00 (n/a)</td><td>191.66 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-18.90%)</td><td>0.10 (-10.16%)</td><td>0.07 (-2.85%)</td><td>0.05 (-8.68%)</td><td>0.05 (-17.67%)</td><td>675.90 (+9.49%)</td><td>459.54 (+8.56%)</td><td>532.70 (+2.94%)</td><td>245.70 <b>(+23.28%)</b></td><td>197.48 (+4.95%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>617.30 (n/a)</td><td>423.32 (n/a)</td><td>517.50 (n/a)</td><td>199.30 (n/a)</td><td>188.17 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (+8.13%)</td><td>0.11 (+7.72%)</td><td>0.12 <b>(+61.11%)</b></td><td>0.06 (-10.63%)</td><td>0.05 (+7.78%)</td><td>585.50 (+11.89%)</td><td>366.42 (-3.81%)</td><td>277.70 <b>(-37.94%)</b></td><td>186.60 (-7.49%)</td><td>179.11 (+19.01%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>523.30 (n/a)</td><td>380.94 (n/a)</td><td>447.50 (n/a)</td><td>201.70 (n/a)</td><td>150.50 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 <b>(-35.71%)</b></td><td>0.10 (-10.48%)</td><td>0.09 (+13.38%)</td><td>0.06 (+0.35%)</td><td>0.04 <b>(-48.40%)</b></td><td>581.40 (-0.34%)</td><td>407.32 (-2.01%)</td><td>433.40 (-11.80%)</td><td>251.80 <b>(+55.53%)</b></td><td>137.92 <b>(-23.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>583.40 (n/a)</td><td>415.66 (n/a)</td><td>491.40 (n/a)</td><td>161.90 (n/a)</td><td>180.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 <b>(+21.57%)</b></td><td>0.08 <b>(+59.26%)</b></td><td>0.06 (+16.67%)</td><td>0.06 <b>(+331.71%)</b></td><td>0.02 <b>(-37.68%)</b></td><td>564.60 <b>(-76.84%)</b></td><td>453.98 <b>(-60.86%)</b></td><td>510.50 (-14.29%)</td><td>333.70 (-17.75%)</td><td>107.13 <b>(-88.65%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2437.60 (n/a)</td><td>1159.76 (n/a)</td><td>595.60 (n/a)</td><td>405.70 (n/a)</td><td>943.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+0.58%)</td><td>0.07 (+14.32%)</td><td>0.07 (+4.99%)</td><td>0.07 <b>(+59.53%)</b></td><td>0.01 <b>(-61.92%)</b></td><td>303.40 <b>(-37.33%)</b></td><td>276.82 (-16.84%)</td><td>278.50 (-4.75%)</td><td>249.70 (-0.60%)</td><td>22.14 <b>(-76.58%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>484.10 (n/a)</td><td>332.88 (n/a)</td><td>292.40 (n/a)</td><td>251.20 (n/a)</td><td>94.54 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (-5.93%)</td><td>0.07 <b>(+23.88%)</b></td><td>0.08 <b>(+75.67%)</b></td><td>0.06 <b>(+40.13%)</b></td><td>0.01 <b>(-55.31%)</b></td><td>361.10 <b>(-28.64%)</b></td><td>285.76 <b>(-26.78%)</b></td><td>266.90 <b>(-43.08%)</b></td><td>250.60 (+6.28%)</td><td>46.02 <b>(-65.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>506.00 (n/a)</td><td>390.28 (n/a)</td><td>468.90 (n/a)</td><td>235.80 (n/a)</td><td>135.23 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (+5.81%)</td><td>0.05 (+16.40%)</td><td>0.04 (+2.45%)</td><td>0.03 <b>(+65.91%)</b></td><td>0.02 (-5.90%)</td><td>629.40 <b>(-39.73%)</b></td><td>478.06 <b>(-21.71%)</b></td><td>541.90 (-2.40%)</td><td>226.20 (-5.47%)</td><td>157.77 <b>(-45.71%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1044.30 (n/a)</td><td>610.60 (n/a)</td><td>555.20 (n/a)</td><td>239.30 (n/a)</td><td>290.61 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (+4.23%)</td><td>0.05 (-7.00%)</td><td>0.04 (+1.01%)</td><td>0.03 (+0.74%)</td><td>0.01 (+6.65%)</td><td>599.40 (-0.73%)</td><td>483.38 (+8.23%)</td><td>468.90 (-1.01%)</td><td>300.60 (-4.05%)</td><td>123.71 (+5.62%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>603.80 (n/a)</td><td>446.64 (n/a)</td><td>473.70 (n/a)</td><td>313.30 (n/a)</td><td>117.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (+2.92%)</td><td>0.05 <b>(-28.20%)</b></td><td>0.05 <b>(-42.81%)</b></td><td>0.02 <b>(-60.32%)</b></td><td>0.03 <b>(+79.12%)</b></td><td>992.10 <b>(+151.99%)</b></td><td>499.16 <b>(+74.63%)</b></td><td>453.90 <b>(+74.85%)</b></td><td>210.80 (-2.86%)</td><td>303.19 <b>(+334.51%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>393.70 (n/a)</td><td>285.84 (n/a)</td><td>259.60 (n/a)</td><td>217.00 (n/a)</td><td>69.78 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (-0.34%)</td><td>0.05 (-18.04%)</td><td>0.05 <b>(-38.04%)</b></td><td>0.04 <b>(-20.67%)</b></td><td>0.02 (+3.44%)</td><td>582.60 <b>(+26.05%)</b></td><td>414.76 <b>(+24.97%)</b></td><td>431.70 <b>(+61.38%)</b></td><td>246.40 (+0.37%)</td><td>140.65 <b>(+30.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>462.20 (n/a)</td><td>331.88 (n/a)</td><td>267.50 (n/a)</td><td>245.50 (n/a)</td><td>108.09 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-18.15%)</td><td>0.07 (-13.02%)</td><td>0.07 (+15.31%)</td><td>0.04 <b>(-28.69%)</b></td><td>0.03 (-13.43%)</td><td>674.80 <b>(+40.23%)</b></td><td>415.36 (+18.62%)</td><td>334.60 (-13.27%)</td><td>244.40 <b>(+22.20%)</b></td><td>184.54 <b>(+50.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>481.20 (n/a)</td><td>350.16 (n/a)</td><td>385.80 (n/a)</td><td>200.00 (n/a)</td><td>122.66 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 <b>(-21.47%)</b></td><td>0.06 (+4.34%)</td><td>0.05 (-8.53%)</td><td>0.05 <b>(+96.74%)</b></td><td>0.02 <b>(-37.83%)</b></td><td>525.70 <b>(-49.17%)</b></td><td>415.44 (-19.26%)</td><td>476.50 (+9.34%)</td><td>274.10 <b>(+27.31%)</b></td><td>119.56 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1034.20 (n/a)</td><td>514.54 (n/a)</td><td>435.80 (n/a)</td><td>215.30 (n/a)</td><td>307.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (+3.43%)</td><td>0.08 <b>(+37.49%)</b></td><td>0.08 <b>(+75.66%)</b></td><td>0.07 <b>(+55.64%)</b></td><td>0.01 <b>(-44.92%)</b></td><td>364.90 <b>(-35.75%)</b></td><td>311.26 <b>(-31.16%)</b></td><td>294.70 <b>(-43.06%)</b></td><td>272.80 (-3.33%)</td><td>41.04 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.90 (n/a)</td><td>452.18 (n/a)</td><td>517.60 (n/a)</td><td>282.20 (n/a)</td><td>119.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (-1.19%)</td><td>0.07 (+14.58%)</td><td>0.05 (+2.15%)</td><td>0.05 (+11.54%)</td><td>0.03 (-1.44%)</td><td>520.90 (-10.34%)</td><td>394.48 (-13.24%)</td><td>466.80 (-2.12%)</td><td>230.00 (+1.19%)</td><td>131.07 (-5.41%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>581.00 (n/a)</td><td>454.68 (n/a)</td><td>476.90 (n/a)</td><td>227.30 (n/a)</td><td>138.56 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-6.77%)</td><td>0.07 (-13.58%)</td><td>0.06 <b>(-23.94%)</b></td><td>0.04 (-17.18%)</td><td>0.03 (-4.11%)</td><td>663.90 <b>(+20.73%)</b></td><td>426.90 (+17.40%)</td><td>414.10 <b>(+31.46%)</b></td><td>234.70 (+7.27%)</td><td>169.08 <b>(+20.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.90 (n/a)</td><td>363.62 (n/a)</td><td>315.00 (n/a)</td><td>218.80 (n/a)</td><td>140.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (-3.40%)</td><td>0.07 (-9.33%)</td><td>0.06 (+0.62%)</td><td>0.04 (-10.25%)</td><td>0.03 (-10.96%)</td><td>666.80 (+11.41%)</td><td>430.08 (+9.43%)</td><td>420.70 (-0.61%)</td><td>235.00 (+3.52%)</td><td>168.59 (+7.92%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>598.50 (n/a)</td><td>393.02 (n/a)</td><td>423.30 (n/a)</td><td>227.00 (n/a)</td><td>156.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+0.20%)</td><td>0.06 (-2.97%)</td><td>0.06 (-2.66%)</td><td>0.04 (+11.14%)</td><td>0.01 (-16.89%)</td><td>468.70 (-10.02%)</td><td>326.06 (+0.04%)</td><td>300.30 (+2.74%)</td><td>233.40 (-0.21%)</td><td>88.82 <b>(-23.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>520.90 (n/a)</td><td>325.92 (n/a)</td><td>292.30 (n/a)</td><td>233.90 (n/a)</td><td>116.67 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (-11.95%)</td><td>0.05 <b>(-24.61%)</b></td><td>0.06 (-11.36%)</td><td>0.01 <b>(-68.46%)</b></td><td>0.03 <b>(+23.76%)</b></td><td>1920.10 <b>(+217.06%)</b></td><td>640.38 <b>(+103.35%)</b></td><td>283.90 (+12.84%)</td><td>247.00 (+13.56%)</td><td>720.57 <b>(+340.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>314.92 (n/a)</td><td>251.60 (n/a)</td><td>217.50 (n/a)</td><td>163.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 <b>(-31.02%)</b></td><td>0.03 <b>(-24.68%)</b></td><td>0.04 (+2.51%)</td><td>0.01 <b>(-70.83%)</b></td><td>0.02 (-12.84%)</td><td>1940.70 <b>(+242.88%)</b></td><td>781.40 <b>(+72.89%)</b></td><td>473.90 (-2.45%)</td><td>332.70 <b>(+44.97%)</b></td><td>661.95 <b>(+409.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>566.00 (n/a)</td><td>451.96 (n/a)</td><td>485.80 (n/a)</td><td>229.50 (n/a)</td><td>130.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (+2.27%)</td><td>0.05 (-4.83%)</td><td>0.04 <b>(-21.79%)</b></td><td>0.03 (-9.01%)</td><td>0.02 (+16.72%)</td><td>604.80 (+9.90%)</td><td>423.66 (+9.61%)</td><td>438.30 <b>(+27.86%)</b></td><td>224.50 (-2.22%)</td><td>168.03 <b>(+22.32%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.30 (n/a)</td><td>386.52 (n/a)</td><td>342.80 (n/a)</td><td>229.60 (n/a)</td><td>137.37 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(-20.85%)</b></td><td>0.04 (-18.60%)</td><td>0.04 (-0.19%)</td><td>0.02 <b>(-21.70%)</b></td><td>0.02 <b>(-26.01%)</b></td><td>773.60 <b>(+27.72%)</b></td><td>492.26 <b>(+21.32%)</b></td><td>448.10 (+0.20%)</td><td>281.80 <b>(+26.31%)</b></td><td>181.52 <b>(+22.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.70 (n/a)</td><td>405.76 (n/a)</td><td>447.20 (n/a)</td><td>223.10 (n/a)</td><td>147.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (-3.90%)</td><td>0.04 (-18.31%)</td><td>0.04 (-18.13%)</td><td>0.02 <b>(-52.22%)</b></td><td>0.02 <b>(+21.93%)</b></td><td>1112.70 <b>(+109.27%)</b></td><td>583.12 <b>(+42.41%)</b></td><td>512.50 <b>(+22.14%)</b></td><td>236.30 (+4.05%)</td><td>322.32 <b>(+173.81%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>531.70 (n/a)</td><td>409.48 (n/a)</td><td>419.60 (n/a)</td><td>227.10 (n/a)</td><td>117.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.40 (+0.01%)</td><td>0.29 (+15.43%)</td><td>0.27 <b>(+42.83%)</b></td><td>0.19 (+12.32%)</td><td>0.10 (-3.63%)</td><td>514.80 (-10.97%)</td><td>371.82 (-15.75%)</td><td>369.20 <b>(-29.98%)</b></td><td>243.20 (+0.00%)</td><td>128.67 (-19.28%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>578.20 (n/a)</td><td>441.32 (n/a)</td><td>527.30 (n/a)</td><td>243.20 (n/a)</td><td>159.39 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.40 (-5.25%)</td><td>0.31 (+13.71%)</td><td>0.35 (+11.81%)</td><td>0.22 <b>(+324.87%)</b></td><td>0.08 <b>(-47.54%)</b></td><td>454.90 <b>(-76.46%)</b></td><td>335.48 <b>(-48.93%)</b></td><td>277.70 (-10.56%)</td><td>245.30 (+5.51%)</td><td>98.56 <b>(-86.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>0.16 (n/a)</td><td>1932.70 (n/a)</td><td>656.90 (n/a)</td><td>310.50 (n/a)</td><td>232.50 (n/a)</td><td>726.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 <b>(+47.99%)</b></td><td>0.37 <b>(+66.08%)</b></td><td>0.41 <b>(+89.05%)</b></td><td>0.18 <b>(+89.98%)</b></td><td>0.12 (+18.58%)</td><td>556.80 <b>(-47.36%)</b></td><td>303.58 <b>(-44.76%)</b></td><td>242.70 <b>(-47.10%)</b></td><td>197.70 <b>(-32.41%)</b></td><td>144.57 <b>(-53.60%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>1057.80 (n/a)</td><td>549.60 (n/a)</td><td>458.80 (n/a)</td><td>292.50 (n/a)</td><td>311.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.29 (-16.80%)</td><td>0.25 (+9.64%)</td><td>0.26 (+11.82%)</td><td>0.20 <b>(+65.10%)</b></td><td>0.03 <b>(-61.41%)</b></td><td>376.40 <b>(-39.44%)</b></td><td>299.94 (-19.67%)</td><td>279.80 (-10.58%)</td><td>257.70 <b>(+20.20%)</b></td><td>46.65 <b>(-71.80%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>621.50 (n/a)</td><td>373.40 (n/a)</td><td>312.90 (n/a)</td><td>214.40 (n/a)</td><td>165.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.27 (-2.27%)</td><td>0.18 <b>(+23.03%)</b></td><td>0.15 (-1.05%)</td><td>0.12 <b>(+209.97%)</b></td><td>0.07 (-14.23%)</td><td>605.50 <b>(-67.74%)</b></td><td>451.96 <b>(-38.75%)</b></td><td>503.20 (+1.06%)</td><td>276.60 (+2.29%)</td><td>158.57 <b>(-75.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1876.80 (n/a)</td><td>737.86 (n/a)</td><td>497.90 (n/a)</td><td>270.40 (n/a)</td><td>645.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.38 (+4.12%)</td><td>0.24 (-1.40%)</td><td>0.27 <b>(+23.29%)</b></td><td>0.11 <b>(-25.94%)</b></td><td>0.11 <b>(+21.40%)</b></td><td>669.90 <b>(+35.03%)</b></td><td>376.04 (+11.35%)</td><td>276.10 (-18.89%)</td><td>195.00 (-3.99%)</td><td>197.85 <b>(+64.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>496.10 (n/a)</td><td>337.72 (n/a)</td><td>340.40 (n/a)</td><td>203.10 (n/a)</td><td>120.15 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (+6.87%)</td><td>0.12 (+4.23%)</td><td>0.13 (+4.42%)</td><td>0.07 (-8.04%)</td><td>0.03 (+18.58%)</td><td>540.10 (+8.74%)</td><td>338.14 (-1.82%)</td><td>289.30 (-4.24%)</td><td>249.30 (-6.42%)</td><td>117.28 <b>(+24.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>496.70 (n/a)</td><td>344.40 (n/a)</td><td>302.10 (n/a)</td><td>266.40 (n/a)</td><td>94.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-11.14%)</td><td>0.13 <b>(+24.25%)</b></td><td>0.13 <b>(+68.27%)</b></td><td>0.12 <b>(+85.65%)</b></td><td>0.01 <b>(-74.47%)</b></td><td>310.80 <b>(-46.13%)</b></td><td>277.86 <b>(-30.82%)</b></td><td>273.90 <b>(-40.57%)</b></td><td>250.10 (+12.56%)</td><td>26.42 <b>(-83.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>576.90 (n/a)</td><td>401.64 (n/a)</td><td>460.90 (n/a)</td><td>222.20 (n/a)</td><td>162.73 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.17 (+7.06%)</td><td>0.10 (-12.37%)</td><td>0.08 <b>(-33.94%)</b></td><td>0.06 (-2.35%)</td><td>0.04 (+2.81%)</td><td>601.30 (+2.40%)</td><td>426.80 (+12.52%)</td><td>447.00 <b>(+51.37%)</b></td><td>216.90 (-6.59%)</td><td>139.64 (-11.30%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>587.20 (n/a)</td><td>379.30 (n/a)</td><td>295.30 (n/a)</td><td>232.20 (n/a)</td><td>157.44 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.20 <b>(+96.59%)</b></td><td>0.11 <b>(+53.49%)</b></td><td>0.10 <b>(+27.81%)</b></td><td>0.07 <b>(+91.83%)</b></td><td>0.05 <b>(+127.43%)</b></td><td>530.00 <b>(-47.88%)</b></td><td>379.98 <b>(-32.46%)</b></td><td>380.20 <b>(-21.75%)</b></td><td>187.50 <b>(-49.13%)</b></td><td>151.90 <b>(-41.41%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>1016.80 (n/a)</td><td>562.64 (n/a)</td><td>485.90 (n/a)</td><td>368.60 (n/a)</td><td>259.26 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 <b>(-25.00%)</b></td><td>0.08 (-17.15%)</td><td>0.08 (-9.89%)</td><td>0.06 (-0.06%)</td><td>0.02 <b>(-53.86%)</b></td><td>587.10 (+0.07%)</td><td>458.40 (+13.50%)</td><td>465.20 (+10.97%)</td><td>355.30 <b>(+33.32%)</b></td><td>86.29 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>586.70 (n/a)</td><td>403.86 (n/a)</td><td>419.20 (n/a)</td><td>266.50 (n/a)</td><td>133.16 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (+4.85%)</td><td>0.10 (-8.16%)</td><td>0.09 <b>(-36.10%)</b></td><td>0.07 <b>(+36.46%)</b></td><td>0.03 <b>(-22.64%)</b></td><td>499.00 <b>(-26.73%)</b></td><td>387.14 (-0.69%)</td><td>409.80 <b>(+56.47%)</b></td><td>234.10 (-4.60%)</td><td>110.26 <b>(-43.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>681.00 (n/a)</td><td>389.82 (n/a)</td><td>261.90 (n/a)</td><td>245.40 (n/a)</td><td>194.38 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (+6.59%)</td><td>0.10 (-4.43%)</td><td>0.09 (+3.87%)</td><td>0.07 (-13.35%)</td><td>0.04 (+15.72%)</td><td>606.80 (+15.41%)</td><td>449.10 (+8.42%)</td><td>453.40 (-3.74%)</td><td>266.80 (-6.16%)</td><td>155.59 <b>(+33.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>525.80 (n/a)</td><td>414.22 (n/a)</td><td>471.00 (n/a)</td><td>284.30 (n/a)</td><td>116.43 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (-19.31%)</td><td>0.10 (-17.46%)</td><td>0.09 <b>(-38.77%)</b></td><td>0.06 (+0.70%)</td><td>0.03 <b>(-39.99%)</b></td><td>645.00 (-0.69%)</td><td>452.92 (+9.49%)</td><td>472.10 <b>(+63.36%)</b></td><td>290.10 <b>(+23.92%)</b></td><td>135.36 <b>(-31.88%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>649.50 (n/a)</td><td>413.66 (n/a)</td><td>289.00 (n/a)</td><td>234.10 (n/a)</td><td>198.71 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (+5.83%)</td><td>0.12 (+9.20%)</td><td>0.11 <b>(+31.58%)</b></td><td>0.07 (-2.74%)</td><td>0.05 (+1.60%)</td><td>579.50 (+2.82%)</td><td>378.64 (-9.05%)</td><td>378.60 <b>(-23.99%)</b></td><td>210.40 (-5.52%)</td><td>151.95 (-4.20%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>563.60 (n/a)</td><td>416.30 (n/a)</td><td>498.10 (n/a)</td><td>222.70 (n/a)</td><td>158.62 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (+16.37%)</td><td>0.11 (-12.94%)</td><td>0.08 <b>(-48.54%)</b></td><td>0.04 <b>(-45.48%)</b></td><td>0.07 <b>(+48.88%)</b></td><td>1033.50 <b>(+83.41%)</b></td><td>537.58 <b>(+41.19%)</b></td><td>534.30 <b>(+94.36%)</b></td><td>216.60 (-14.08%)</td><td>333.83 <b>(+111.01%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>563.50 (n/a)</td><td>380.76 (n/a)</td><td>274.90 (n/a)</td><td>252.10 (n/a)</td><td>158.20 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 <b>(-24.40%)</b></td><td>0.10 <b>(-23.31%)</b></td><td>0.10 <b>(-28.97%)</b></td><td>0.07 (+4.94%)</td><td>0.03 <b>(-41.23%)</b></td><td>573.10 (-4.71%)</td><td>427.04 (+18.93%)</td><td>413.90 <b>(+40.78%)</b></td><td>258.40 <b>(+32.31%)</b></td><td>118.31 <b>(-29.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>601.40 (n/a)</td><td>359.08 (n/a)</td><td>294.00 (n/a)</td><td>195.30 (n/a)</td><td>167.35 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 <b>(-26.80%)</b></td><td>0.09 <b>(-29.60%)</b></td><td>0.09 <b>(-29.84%)</b></td><td>0.02 <b>(-70.75%)</b></td><td>0.05 (-4.10%)</td><td>1971.40 <b>(+241.90%)</b></td><td>707.68 <b>(+98.94%)</b></td><td>432.50 <b>(+42.55%)</b></td><td>288.10 <b>(+36.61%)</b></td><td>710.73 <b>(+394.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>576.60 (n/a)</td><td>355.72 (n/a)</td><td>303.40 (n/a)</td><td>210.90 (n/a)</td><td>143.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-1.05%)</td><td>0.10 (-0.83%)</td><td>0.09 (-8.72%)</td><td>0.06 <b>(-20.35%)</b></td><td>0.04 <b>(+25.49%)</b></td><td>613.40 <b>(+25.54%)</b></td><td>399.10 (+6.91%)</td><td>407.40 (+9.58%)</td><td>238.70 (+1.06%)</td><td>162.80 <b>(+40.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>488.60 (n/a)</td><td>373.30 (n/a)</td><td>371.80 (n/a)</td><td>236.20 (n/a)</td><td>115.76 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.17 <b>(+27.49%)</b></td><td>0.12 <b>(+69.43%)</b></td><td>0.11 <b>(+73.88%)</b></td><td>0.08 <b>(+344.15%)</b></td><td>0.03 <b>(-24.22%)</b></td><td>424.90 <b>(-77.49%)</b></td><td>318.48 <b>(-58.43%)</b></td><td>318.80 <b>(-42.50%)</b></td><td>209.70 <b>(-21.55%)</b></td><td>76.17 <b>(-88.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1887.20 (n/a)</td><td>766.20 (n/a)</td><td>554.40 (n/a)</td><td>267.30 (n/a)</td><td>642.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 <b>(+54.81%)</b></td><td>0.09 (+16.70%)</td><td>0.07 (-9.54%)</td><td>0.05 <b>(-26.18%)</b></td><td>0.04 <b>(+278.92%)</b></td><td>768.30 <b>(+35.48%)</b></td><td>453.14 (+0.75%)</td><td>488.10 (+10.55%)</td><td>243.80 <b>(-35.42%)</b></td><td>212.87 <b>(+201.37%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>449.78 (n/a)</td><td>441.50 (n/a)</td><td>377.50 (n/a)</td><td>70.64 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (-7.06%)</td><td>0.09 (-16.94%)</td><td>0.08 <b>(-33.26%)</b></td><td>0.06 (+0.35%)</td><td>0.04 <b>(-21.58%)</b></td><td>597.80 (-0.35%)</td><td>431.98 (+13.59%)</td><td>459.80 <b>(+49.87%)</b></td><td>235.70 (+7.63%)</td><td>150.32 (-16.48%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>599.90 (n/a)</td><td>380.30 (n/a)</td><td>306.80 (n/a)</td><td>219.00 (n/a)</td><td>179.97 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 <b>(+20.56%)</b></td><td>0.10 (+13.33%)</td><td>0.10 <b>(+34.88%)</b></td><td>0.05 <b>(+34.97%)</b></td><td>0.05 <b>(+20.97%)</b></td><td>716.70 <b>(-25.91%)</b></td><td>450.54 (-11.39%)</td><td>358.00 <b>(-25.86%)</b></td><td>197.40 (-17.06%)</td><td>233.06 (-18.37%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>967.40 (n/a)</td><td>508.48 (n/a)</td><td>482.90 (n/a)</td><td>238.00 (n/a)</td><td>285.49 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (+14.03%)</td><td>0.12 (+2.79%)</td><td>0.12 (-5.82%)</td><td>0.07 <b>(-22.26%)</b></td><td>0.03 <b>(+71.96%)</b></td><td>522.70 <b>(+28.65%)</b></td><td>318.10 (+3.43%)</td><td>296.00 (+6.17%)</td><td>226.70 (-12.30%)</td><td>120.09 <b>(+96.35%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>406.30 (n/a)</td><td>307.54 (n/a)</td><td>278.80 (n/a)</td><td>258.50 (n/a)</td><td>61.16 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 (+13.64%)</td><td>0.44 <b>(+43.01%)</b></td><td>0.43 <b>(+76.56%)</b></td><td>0.38 <b>(+69.28%)</b></td><td>0.05 <b>(-53.24%)</b></td><td>346.70 <b>(-40.93%)</b></td><td>299.38 <b>(-35.11%)</b></td><td>304.60 <b>(-43.37%)</b></td><td>262.40 (-12.01%)</td><td>33.60 <b>(-75.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>586.90 (n/a)</td><td>461.36 (n/a)</td><td>537.90 (n/a)</td><td>298.20 (n/a)</td><td>138.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.55 <b>(+24.30%)</b></td><td>0.40 <b>(+41.64%)</b></td><td>0.43 <b>(+69.20%)</b></td><td>0.21 (+17.47%)</td><td>0.13 <b>(+33.07%)</b></td><td>614.70 (-14.87%)</td><td>363.78 <b>(-27.66%)</b></td><td>308.10 <b>(-40.91%)</b></td><td>239.30 (-19.56%)</td><td>149.89 (-2.72%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.44 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>722.10 (n/a)</td><td>502.86 (n/a)</td><td>521.40 (n/a)</td><td>297.50 (n/a)</td><td>154.09 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 <b>(+83.77%)</b></td><td>0.41 <b>(+71.13%)</b></td><td>0.41 <b>(+73.29%)</b></td><td>0.29 <b>(+39.54%)</b></td><td>0.08 <b>(+166.03%)</b></td><td>455.20 <b>(-28.34%)</b></td><td>333.66 <b>(-40.26%)</b></td><td>321.70 <b>(-42.29%)</b></td><td>263.20 <b>(-45.60%)</b></td><td>74.05 (+6.19%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>635.20 (n/a)</td><td>558.52 (n/a)</td><td>557.40 (n/a)</td><td>483.80 (n/a)</td><td>69.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-1.66%)</td><td>0.01 (-18.46%)</td><td>0.01 (-6.76%)</td><td>0.01 <b>(-45.90%)</b></td><td>0.00 <b>(+151.70%)</b></td><td>541.00 <b>(+84.83%)</b></td><td>351.34 <b>(+31.96%)</b></td><td>294.30 (+7.25%)</td><td>238.00 (+1.67%)</td><td>119.33 <b>(+387.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>292.70 (n/a)</td><td>266.24 (n/a)</td><td>274.40 (n/a)</td><td>234.10 (n/a)</td><td>24.47 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (-5.24%)</td><td>0.01 (-3.23%)</td><td>0.01 (-2.59%)</td><td>0.01 (+7.78%)</td><td>0.00 (-15.56%)</td><td>515.40 (-7.22%)</td><td>327.84 (+0.62%)</td><td>284.40 (+2.63%)</td><td>255.00 (+5.50%)</td><td>106.68 (-17.91%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.50 (n/a)</td><td>325.82 (n/a)</td><td>277.10 (n/a)</td><td>241.70 (n/a)</td><td>129.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 <b>(+38.77%)</b></td><td>0.01 (-4.56%)</td><td>0.01 <b>(-22.98%)</b></td><td>0.00 <b>(-70.00%)</b></td><td>0.01 <b>(+117.05%)</b></td><td>2451.10 <b>(+233.30%)</b></td><td>829.98 <b>(+77.95%)</b></td><td>510.00 <b>(+29.84%)</b></td><td>251.00 <b>(-27.94%)</b></td><td>917.45 <b>(+467.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>735.40 (n/a)</td><td>466.40 (n/a)</td><td>392.80 (n/a)</td><td>348.30 (n/a)</td><td>161.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.70 (-2.78%)</td><td>5.32 <b>(-23.87%)</b></td><td>4.71 <b>(-35.01%)</b></td><td>4.00 (-15.49%)</td><td>1.43 (+9.42%)</td><td>524.50 (+18.34%)</td><td>414.32 <b>(+33.03%)</b></td><td>445.20 <b>(+53.84%)</b></td><td>272.30 (+2.87%)</td><td>93.97 <b>(+25.58%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>7.93 (n/a)</td><td>6.99 (n/a)</td><td>7.25 (n/a)</td><td>4.73 (n/a)</td><td>1.31 (n/a)</td><td>443.20 (n/a)</td><td>311.46 (n/a)</td><td>289.40 (n/a)</td><td>264.70 (n/a)</td><td>74.83 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.52 (-0.37%)</td><td>0.32 (-15.48%)</td><td>0.31 (-2.37%)</td><td>0.20 <b>(-24.71%)</b></td><td>0.12 (+6.76%)</td><td>662.40 <b>(+32.80%)</b></td><td>458.22 <b>(+21.87%)</b></td><td>431.70 (+2.44%)</td><td>255.90 (+0.35%)</td><td>149.12 <b>(+42.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>498.80 (n/a)</td><td>376.00 (n/a)</td><td>421.40 (n/a)</td><td>255.00 (n/a)</td><td>104.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.46 (-16.82%)</td><td>0.31 (-17.35%)</td><td>0.32 (-17.44%)</td><td>0.06 (-2.22%)</td><td>0.16 (-19.28%)</td><td>2060.60 (+2.27%)</td><td>711.04 (+9.81%)</td><td>414.90 <b>(+21.10%)</b></td><td>285.60 <b>(+20.25%)</b></td><td>759.32 (-1.04%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.56 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td><td>2014.80 (n/a)</td><td>647.54 (n/a)</td><td>342.60 (n/a)</td><td>237.50 (n/a)</td><td>767.31 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.44 <b>(-22.97%)</b></td><td>0.32 <b>(-30.37%)</b></td><td>0.30 <b>(-37.18%)</b></td><td>0.21 <b>(-29.53%)</b></td><td>0.08 (-17.32%)</td><td>616.70 <b>(+41.90%)</b></td><td>442.24 <b>(+45.04%)</b></td><td>441.10 <b>(+59.18%)</b></td><td>300.10 <b>(+29.80%)</b></td><td>118.53 <b>(+48.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>434.60 (n/a)</td><td>304.90 (n/a)</td><td>277.10 (n/a)</td><td>231.20 (n/a)</td><td>79.88 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.60 (+3.43%)</td><td>0.45 (+17.02%)</td><td>0.47 <b>(+28.35%)</b></td><td>0.20 <b>(-26.64%)</b></td><td>0.16 (+18.16%)</td><td>674.10 <b>(+36.32%)</b></td><td>344.22 (-8.22%)</td><td>284.10 <b>(-22.08%)</b></td><td>218.40 (-3.32%)</td><td>187.16 <b>(+61.56%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>494.50 (n/a)</td><td>375.06 (n/a)</td><td>364.60 (n/a)</td><td>225.90 (n/a)</td><td>115.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.57 (+10.42%)</td><td>0.40 (-9.58%)</td><td>0.40 (-12.86%)</td><td>0.31 (-0.72%)</td><td>0.11 <b>(+39.63%)</b></td><td>426.10 (+0.73%)</td><td>347.88 (+12.92%)</td><td>330.00 (+14.74%)</td><td>230.20 (-9.44%)</td><td>81.68 <b>(+24.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>423.00 (n/a)</td><td>308.08 (n/a)</td><td>287.60 (n/a)</td><td>254.20 (n/a)</td><td>65.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+18.77%)</td><td>0.01 (+3.62%)</td><td>0.02 (+7.84%)</td><td>0.01 <b>(-32.28%)</b></td><td>0.00 <b>(+218.47%)</b></td><td>477.70 <b>(+47.67%)</b></td><td>300.00 (+3.48%)</td><td>272.80 (-7.24%)</td><td>217.00 (-15.79%)</td><td>104.09 <b>(+311.85%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>323.50 (n/a)</td><td>289.92 (n/a)</td><td>294.10 (n/a)</td><td>257.70 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (+5.44%)</td><td>0.01 (-9.97%)</td><td>0.01 (-4.28%)</td><td>0.01 <b>(-21.03%)</b></td><td>0.00 <b>(+61.10%)</b></td><td>536.60 <b>(+26.62%)</b></td><td>363.72 (+19.09%)</td><td>300.10 (+4.46%)</td><td>228.30 (-5.15%)</td><td>133.93 <b>(+92.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>423.80 (n/a)</td><td>305.42 (n/a)</td><td>287.30 (n/a)</td><td>240.70 (n/a)</td><td>69.66 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.00 (+0.00%)</td><td>0.00 (-4.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+10.37%)</td><td>18518.64 (+10.98%)</td><td>10710.67 (+9.60%)</td><td>6471.73 (-0.90%)</td><td>5661.55 (-1.07%)</td><td>6497.85 <b>(+26.53%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16687.02 (n/a)</td><td>9772.80 (n/a)</td><td>6530.80 (n/a)</td><td>5722.76 (n/a)</td><td>5135.32 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-51.56%)</b></td><td>0.00 <b>(-61.54%)</b></td><td>0.00 <b>(-63.64%)</b></td><td>0.00 <b>(+198.61%)</b></td><td>21817.34 <b>(+197.45%)</b></td><td>15871.19 <b>(+147.16%)</b></td><td>16820.49 <b>(+165.98%)</b></td><td>6822.26 (+15.66%)</td><td>5488.97 <b>(+887.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>7334.75 (n/a)</td><td>6421.46 (n/a)</td><td>6324.07 (n/a)</td><td>5898.48 (n/a)</td><td>555.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (+12.88%)</td><td>0.09 (-8.27%)</td><td>0.07 (-15.52%)</td><td>0.07 (-4.35%)</td><td>0.04 <b>(+29.59%)</b></td><td>28934.00 (+4.55%)</td><td>24850.20 (+12.26%)</td><td>28095.55 (+18.36%)</td><td>13077.47 (-11.42%)</td><td>6676.64 (+14.45%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27675.94 (n/a)</td><td>22136.16 (n/a)</td><td>23737.46 (n/a)</td><td>14762.81 (n/a)</td><td>5833.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.60 <b>(+34.44%)</b></td><td>1.48 (+13.18%)</td><td>1.45 <b>(+21.54%)</b></td><td>0.30 (+1.35%)</td><td>1.30 <b>(+49.28%)</b></td><td>3468.00 (-1.33%)</td><td>1421.00 (+7.49%)</td><td>723.20 (-17.72%)</td><td>291.60 <b>(-25.61%)</b></td><td>1299.05 (+3.81%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.67 (n/a)</td><td>1.31 (n/a)</td><td>1.19 (n/a)</td><td>0.30 (n/a)</td><td>0.87 (n/a)</td><td>3514.80 (n/a)</td><td>1321.96 (n/a)</td><td>879.00 (n/a)</td><td>392.00 (n/a)</td><td>1251.39 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.27 <b>(+20.72%)</b></td><td>2.10 (-5.58%)</td><td>1.65 (-15.85%)</td><td>1.40 (-1.06%)</td><td>1.22 <b>(+41.37%)</b></td><td>746.70 (+1.07%)</td><td>593.40 (+12.60%)</td><td>635.10 (+18.84%)</td><td>245.70 (-17.16%)</td><td>203.56 (+12.26%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.54 (n/a)</td><td>2.22 (n/a)</td><td>1.96 (n/a)</td><td>1.42 (n/a)</td><td>0.86 (n/a)</td><td>738.80 (n/a)</td><td>526.98 (n/a)</td><td>534.40 (n/a)</td><td>296.60 (n/a)</td><td>181.33 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.15 (-12.06%)</td><td>1.96 <b>(-22.77%)</b></td><td>1.56 <b>(-43.36%)</b></td><td>1.30 <b>(+44.80%)</b></td><td>0.81 <b>(-21.59%)</b></td><td>804.90 <b>(-30.93%)</b></td><td>604.92 (+15.00%)</td><td>674.30 <b>(+76.56%)</b></td><td>333.30 (+13.72%)</td><td>213.55 <b>(-41.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.58 (n/a)</td><td>2.54 (n/a)</td><td>2.75 (n/a)</td><td>0.90 (n/a)</td><td>1.04 (n/a)</td><td>1165.40 (n/a)</td><td>526.04 (n/a)</td><td>381.90 (n/a)</td><td>293.10 (n/a)</td><td>362.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.50 (+18.71%)</td><td>1.74 <b>(-21.04%)</b></td><td>1.55 <b>(-26.59%)</b></td><td>0.30 <b>(-81.20%)</b></td><td>1.15 <b>(+118.73%)</b></td><td>3505.20 <b>(+431.98%)</b></td><td>1149.20 <b>(+131.00%)</b></td><td>675.90 <b>(+36.22%)</b></td><td>299.80 (-15.76%)</td><td>1326.64 <b>(+1035.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.95 (n/a)</td><td>2.20 (n/a)</td><td>2.11 (n/a)</td><td>1.59 (n/a)</td><td>0.53 (n/a)</td><td>658.90 (n/a)</td><td>497.48 (n/a)</td><td>496.20 (n/a)</td><td>355.90 (n/a)</td><td>116.86 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.90 <b>(+38.71%)</b></td><td>2.23 (+4.27%)</td><td>2.08 (-16.53%)</td><td>0.70 (-19.70%)</td><td>1.41 <b>(+85.86%)</b></td><td>2986.70 <b>(+24.53%)</b></td><td>1428.10 <b>(+21.99%)</b></td><td>1007.20 (+19.80%)</td><td>537.90 <b>(-27.91%)</b></td><td>1048.29 <b>(+51.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.81 (n/a)</td><td>2.14 (n/a)</td><td>2.49 (n/a)</td><td>0.87 (n/a)</td><td>0.76 (n/a)</td><td>2398.30 (n/a)</td><td>1170.66 (n/a)</td><td>840.70 (n/a)</td><td>746.10 (n/a)</td><td>693.96 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.20 <b>(-28.33%)</b></td><td>2.80 <b>(+57.71%)</b></td><td>2.94 <b>(+243.50%)</b></td><td>0.58 (-1.29%)</td><td>1.43 <b>(-37.57%)</b></td><td>3601.90 (+1.31%)</td><td>1244.72 <b>(-48.08%)</b></td><td>712.50 <b>(-70.89%)</b></td><td>499.70 <b>(+39.54%)</b></td><td>1325.67 (+2.44%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.86 (n/a)</td><td>1.78 (n/a)</td><td>0.86 (n/a)</td><td>0.59 (n/a)</td><td>2.29 (n/a)</td><td>3555.40 (n/a)</td><td>2397.40 (n/a)</td><td>2447.30 (n/a)</td><td>358.10 (n/a)</td><td>1294.10 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.31 <b>(+38.03%)</b></td><td>3.55 <b>(+48.29%)</b></td><td>4.42 <b>(+52.86%)</b></td><td>0.60 <b>(-28.70%)</b></td><td>1.94 <b>(+33.10%)</b></td><td>3494.50 <b>(+40.24%)</b></td><td>1119.36 (-17.69%)</td><td>474.60 <b>(-34.58%)</b></td><td>394.90 <b>(-27.55%)</b></td><td>1337.25 <b>(+31.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.85 (n/a)</td><td>2.40 (n/a)</td><td>2.89 (n/a)</td><td>0.84 (n/a)</td><td>1.45 (n/a)</td><td>2491.80 (n/a)</td><td>1359.94 (n/a)</td><td>725.50 (n/a)</td><td>545.10 (n/a)</td><td>1014.68 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.87 (+9.62%)</td><td>3.01 (+2.08%)</td><td>3.14 (+19.70%)</td><td>0.60 (+1.17%)</td><td>1.94 (+11.72%)</td><td>3494.10 (-1.15%)</td><td>1233.46 (+0.58%)</td><td>668.40 (-16.46%)</td><td>357.40 (-8.76%)</td><td>1286.60 (-1.25%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.35 (n/a)</td><td>2.95 (n/a)</td><td>2.62 (n/a)</td><td>0.59 (n/a)</td><td>1.74 (n/a)</td><td>3534.90 (n/a)</td><td>1226.32 (n/a)</td><td>800.10 (n/a)</td><td>391.70 (n/a)</td><td>1302.86 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.37 <b>(+86.59%)</b></td><td>3.61 <b>(+79.78%)</b></td><td>3.45 <b>(+65.69%)</b></td><td>1.09 <b>(+80.26%)</b></td><td>1.89 <b>(+48.73%)</b></td><td>1928.60 <b>(-44.52%)</b></td><td>811.52 <b>(-50.88%)</b></td><td>608.70 <b>(-39.65%)</b></td><td>329.10 <b>(-46.41%)</b></td><td>637.18 <b>(-49.86%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.41 (n/a)</td><td>2.01 (n/a)</td><td>2.08 (n/a)</td><td>0.60 (n/a)</td><td>1.27 (n/a)</td><td>3476.50 (n/a)</td><td>1652.26 (n/a)</td><td>1008.60 (n/a)</td><td>614.10 (n/a)</td><td>1270.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>8.27 <b>(+128.48%)</b></td><td>3.42 (+19.66%)</td><td>2.52 <b>(-24.24%)</b></td><td>0.58 (-3.12%)</td><td>2.95 <b>(+131.60%)</b></td><td>3599.00 (+3.22%)</td><td>1263.72 (+6.35%)</td><td>832.60 <b>(+31.99%)</b></td><td>253.50 <b>(-56.23%)</b></td><td>1341.57 (+4.39%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.62 (n/a)</td><td>2.86 (n/a)</td><td>3.32 (n/a)</td><td>0.60 (n/a)</td><td>1.27 (n/a)</td><td>3486.80 (n/a)</td><td>1188.32 (n/a)</td><td>630.80 (n/a)</td><td>579.20 (n/a)</td><td>1285.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.43 (+3.42%)</td><td>2.92 <b>(-35.49%)</b></td><td>2.19 <b>(-50.48%)</b></td><td>1.11 <b>(-67.88%)</b></td><td>1.82 <b>(+149.44%)</b></td><td>3778.40 <b>(+211.36%)</b></td><td>1992.20 <b>(+110.17%)</b></td><td>1911.10 <b>(+101.93%)</b></td><td>772.60 (-3.30%)</td><td>1216.80 <b>(+627.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.25 (n/a)</td><td>4.53 (n/a)</td><td>4.43 (n/a)</td><td>3.46 (n/a)</td><td>0.73 (n/a)</td><td>1213.50 (n/a)</td><td>947.88 (n/a)</td><td>946.40 (n/a)</td><td>799.00 (n/a)</td><td>167.18 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.96 <b>(+33.26%)</b></td><td>4.61 <b>(+85.61%)</b></td><td>5.80 <b>(+237.12%)</b></td><td>1.19 (-1.85%)</td><td>3.00 <b>(+52.75%)</b></td><td>3533.10 (+1.88%)</td><td>1582.02 <b>(-30.56%)</b></td><td>723.30 <b>(-70.34%)</b></td><td>527.10 <b>(-24.97%)</b></td><td>1351.44 <b>(+35.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>5.97 (n/a)</td><td>2.48 (n/a)</td><td>1.72 (n/a)</td><td>1.21 (n/a)</td><td>1.96 (n/a)</td><td>3467.90 (n/a)</td><td>2278.28 (n/a)</td><td>2438.40 (n/a)</td><td>702.50 (n/a)</td><td>995.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.42 (-6.51%)</td><td>4.95 <b>(+24.43%)</b></td><td>6.24 <b>(+53.63%)</b></td><td>1.19 (+1.44%)</td><td>2.23 (-11.42%)</td><td>3532.40 (-1.42%)</td><td>1285.66 <b>(-22.34%)</b></td><td>672.30 <b>(-34.91%)</b></td><td>653.00 (+6.96%)</td><td>1260.19 (-1.93%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>6.87 (n/a)</td><td>3.98 (n/a)</td><td>4.06 (n/a)</td><td>1.17 (n/a)</td><td>2.51 (n/a)</td><td>3583.20 (n/a)</td><td>1655.50 (n/a)</td><td>1032.80 (n/a)</td><td>610.50 (n/a)</td><td>1285.05 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>9.71 <b>(+36.77%)</b></td><td>6.84 <b>(+39.51%)</b></td><td>6.35 <b>(+33.63%)</b></td><td>4.26 <b>(+148.22%)</b></td><td>1.99 (-6.35%)</td><td>984.20 <b>(-59.72%)</b></td><td>659.06 <b>(-40.25%)</b></td><td>660.20 <b>(-25.16%)</b></td><td>432.10 <b>(-26.89%)</b></td><td>204.70 <b>(-73.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>7.10 (n/a)</td><td>4.90 (n/a)</td><td>4.75 (n/a)</td><td>1.72 (n/a)</td><td>2.12 (n/a)</td><td>2443.10 (n/a)</td><td>1103.00 (n/a)</td><td>882.20 (n/a)</td><td>591.00 (n/a)</td><td>765.31 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>10.07 (-2.02%)</td><td>7.10 (+14.15%)</td><td>7.45 (+10.09%)</td><td>3.55 <b>(+110.18%)</b></td><td>2.35 <b>(-30.30%)</b></td><td>1180.70 <b>(-52.42%)</b></td><td>666.00 <b>(-33.77%)</b></td><td>562.70 (-9.17%)</td><td>416.50 (+2.06%)</td><td>297.49 <b>(-65.22%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>10.28 (n/a)</td><td>6.22 (n/a)</td><td>6.77 (n/a)</td><td>1.69 (n/a)</td><td>3.37 (n/a)</td><td>2481.50 (n/a)</td><td>1005.66 (n/a)</td><td>619.50 (n/a)</td><td>408.10 (n/a)</td><td>855.43 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>8.95 (-7.47%)</td><td>5.13 (-14.30%)</td><td>6.01 (+13.44%)</td><td>1.22 <b>(-50.86%)</b></td><td>3.05 (+3.06%)</td><td>3449.40 <b>(+103.48%)</b></td><td>1336.94 <b>(+50.69%)</b></td><td>697.90 (-11.85%)</td><td>468.90 (+8.09%)</td><td>1236.09 <b>(+143.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>9.67 (n/a)</td><td>5.98 (n/a)</td><td>5.30 (n/a)</td><td>2.47 (n/a)</td><td>2.96 (n/a)</td><td>1695.20 (n/a)</td><td>887.24 (n/a)</td><td>791.70 (n/a)</td><td>433.80 (n/a)</td><td>507.26 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.57 (-4.30%)</td><td>1.12 (-11.40%)</td><td>1.10 <b>(-26.43%)</b></td><td>0.64 (-12.17%)</td><td>0.42 (+1.03%)</td><td>818.50 (+13.85%)</td><td>528.88 (+14.94%)</td><td>474.50 <b>(+35.92%)</b></td><td>333.20 (+4.48%)</td><td>211.03 (+18.63%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.64 (n/a)</td><td>1.27 (n/a)</td><td>1.50 (n/a)</td><td>0.73 (n/a)</td><td>0.41 (n/a)</td><td>718.90 (n/a)</td><td>460.14 (n/a)</td><td>349.10 (n/a)</td><td>318.90 (n/a)</td><td>177.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.31 (-17.86%)</td><td>1.59 (+9.79%)</td><td>2.12 <b>(+24.55%)</b></td><td>0.30 (-7.58%)</td><td>0.87 <b>(-20.89%)</b></td><td>3549.10 (+8.20%)</td><td>1191.94 <b>(-25.68%)</b></td><td>493.60 (-19.70%)</td><td>454.20 <b>(+21.74%)</b></td><td>1334.96 (-12.02%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>2.81 (n/a)</td><td>1.45 (n/a)</td><td>1.71 (n/a)</td><td>0.32 (n/a)</td><td>1.10 (n/a)</td><td>3280.00 (n/a)</td><td>1603.86 (n/a)</td><td>614.70 (n/a)</td><td>373.10 (n/a)</td><td>1517.40 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.69 (-1.42%)</td><td>2.23 <b>(+20.76%)</b></td><td>1.99 <b>(+137.20%)</b></td><td>0.58 (+0.19%)</td><td>1.17 <b>(-27.58%)</b></td><td>3644.30 (-0.19%)</td><td>1412.64 <b>(-35.38%)</b></td><td>1052.50 <b>(-57.84%)</b></td><td>568.80 (+1.44%)</td><td>1266.72 (-17.58%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>3.74 (n/a)</td><td>1.84 (n/a)</td><td>0.84 (n/a)</td><td>0.57 (n/a)</td><td>1.62 (n/a)</td><td>3651.20 (n/a)</td><td>2186.18 (n/a)</td><td>2496.60 (n/a)</td><td>560.70 (n/a)</td><td>1536.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.60 (-9.52%)</td><td>1.06 (-11.52%)</td><td>1.06 (+8.76%)</td><td>0.25 <b>(-60.10%)</b></td><td>0.53 (+10.81%)</td><td>2076.40 <b>(+150.65%)</b></td><td>768.36 <b>(+51.92%)</b></td><td>494.90 (-8.06%)</td><td>328.40 (+10.50%)</td><td>738.79 <b>(+244.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>1.76 (n/a)</td><td>1.19 (n/a)</td><td>0.97 (n/a)</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>828.40 (n/a)</td><td>505.76 (n/a)</td><td>538.30 (n/a)</td><td>297.20 (n/a)</td><td>214.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 <b>(-39.02%)</b></td><td>0.07 <b>(-38.73%)</b></td><td>0.07 <b>(-37.54%)</b></td><td>0.04 <b>(-22.16%)</b></td><td>0.02 <b>(-45.62%)</b></td><td>735.20 <b>(+28.46%)</b></td><td>525.08 <b>(+56.94%)</b></td><td>478.00 <b>(+60.08%)</b></td><td>365.60 <b>(+64.02%)</b></td><td>146.19 (+7.11%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.30 (n/a)</td><td>334.58 (n/a)</td><td>298.60 (n/a)</td><td>222.90 (n/a)</td><td>136.49 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (-6.90%)</td><td>0.09 <b>(+21.67%)</b></td><td>0.07 <b>(+30.45%)</b></td><td>0.06 (+18.42%)</td><td>0.03 (-18.10%)</td><td>522.50 (-15.55%)</td><td>398.48 <b>(-21.66%)</b></td><td>438.80 <b>(-23.34%)</b></td><td>246.20 (+7.42%)</td><td>125.09 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>618.70 (n/a)</td><td>508.68 (n/a)</td><td>572.40 (n/a)</td><td>229.20 (n/a)</td><td>159.75 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.26 (+1.04%)</td><td>0.22 (+19.08%)</td><td>0.22 <b>(+42.04%)</b></td><td>0.15 <b>(+26.29%)</b></td><td>0.04 <b>(-31.59%)</b></td><td>436.40 <b>(-20.83%)</b></td><td>314.16 <b>(-20.07%)</b></td><td>296.80 <b>(-29.60%)</b></td><td>253.70 (-1.01%)</td><td>71.25 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>551.20 (n/a)</td><td>393.06 (n/a)</td><td>421.60 (n/a)</td><td>256.30 (n/a)</td><td>122.91 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.27 (-13.02%)</td><td>0.18 (-8.91%)</td><td>0.14 <b>(-36.43%)</b></td><td>0.13 <b>(+58.10%)</b></td><td>0.06 <b>(-30.29%)</b></td><td>490.10 <b>(-36.74%)</b></td><td>390.20 (-3.87%)</td><td>469.80 <b>(+57.28%)</b></td><td>243.90 (+14.94%)</td><td>119.67 <b>(-48.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>774.80 (n/a)</td><td>405.90 (n/a)</td><td>298.70 (n/a)</td><td>212.20 (n/a)</td><td>233.14 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.26 (+1.11%)</td><td>0.15 (+0.69%)</td><td>0.14 <b>(+27.60%)</b></td><td>0.04 (+10.22%)</td><td>0.08 (-13.44%)</td><td>1798.30 (-9.27%)</td><td>676.10 (-9.07%)</td><td>456.40 <b>(-21.63%)</b></td><td>247.90 (-1.12%)</td><td>634.24 (-10.92%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>1982.00 (n/a)</td><td>743.54 (n/a)</td><td>582.40 (n/a)</td><td>250.70 (n/a)</td><td>712.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.62 (+2.53%)</td><td>0.46 (+1.46%)</td><td>0.50 (+8.93%)</td><td>0.34 <b>(+48.68%)</b></td><td>0.12 (-19.33%)</td><td>389.20 <b>(-32.73%)</b></td><td>301.14 (-7.65%)</td><td>264.30 (-8.20%)</td><td>210.70 (-2.50%)</td><td>79.60 <b>(-45.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.61 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>578.60 (n/a)</td><td>326.10 (n/a)</td><td>287.90 (n/a)</td><td>216.10 (n/a)</td><td>146.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.54 <b>(+62.78%)</b></td><td>0.40 <b>(+71.96%)</b></td><td>0.43 <b>(+72.95%)</b></td><td>0.24 <b>(+248.21%)</b></td><td>0.12 <b>(+26.19%)</b></td><td>556.00 <b>(-71.28%)</b></td><td>361.72 <b>(-53.62%)</b></td><td>304.60 <b>(-42.18%)</b></td><td>244.20 <b>(-38.57%)</b></td><td>129.93 <b>(-80.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.10 (n/a)</td><td>1936.10 (n/a)</td><td>779.86 (n/a)</td><td>526.80 (n/a)</td><td>397.50 (n/a)</td><td>649.59 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.48 (+7.52%)</td><td>0.37 (+16.75%)</td><td>0.35 (+5.09%)</td><td>0.24 <b>(+74.04%)</b></td><td>0.10 <b>(-28.78%)</b></td><td>549.80 <b>(-42.54%)</b></td><td>381.84 <b>(-25.75%)</b></td><td>375.50 (-4.84%)</td><td>271.30 (-6.99%)</td><td>110.95 <b>(-60.77%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>956.80 (n/a)</td><td>514.26 (n/a)</td><td>394.60 (n/a)</td><td>291.70 (n/a)</td><td>282.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 <b>(+23.10%)</b></td><td>0.05 <b>(+22.89%)</b></td><td>0.05 <b>(+23.83%)</b></td><td>0.03 (-9.61%)</td><td>0.02 <b>(+55.91%)</b></td><td>574.40 (+10.63%)</td><td>370.00 (-14.17%)</td><td>357.80 (-19.23%)</td><td>227.90 (-18.75%)</td><td>133.97 <b>(+45.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:01:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.20 (n/a)</td><td>431.10 (n/a)</td><td>443.00 (n/a)</td><td>280.50 (n/a)</td><td>92.16 (n/a)</td>
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
