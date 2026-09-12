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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+4.57%)</td><td>0.02 (-9.08%)</td><td>0.02 (-17.87%)</td><td>0.01 (+13.33%)</td><td>0.01 (-17.91%)</td><td>475.30 (-11.77%)</td><td>386.14 (+4.46%)</td><td>407.20 <b>(+21.77%)</b></td><td>227.30 (-4.38%)</td><td>96.57 <b>(-32.24%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.70 (n/a)</td><td>369.64 (n/a)</td><td>334.40 (n/a)</td><td>237.70 (n/a)</td><td>142.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-12.00%)</td><td>0.02 <b>(-26.70%)</b></td><td>0.01 <b>(-31.73%)</b></td><td>0.00 <b>(-78.78%)</b></td><td>0.01 <b>(+57.11%)</b></td><td>2021.50 <b>(+371.21%)</b></td><td>690.10 <b>(+120.39%)</b></td><td>414.20 <b>(+46.46%)</b></td><td>271.50 (+13.65%)</td><td>749.13 <b>(+796.64%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>429.00 (n/a)</td><td>313.12 (n/a)</td><td>282.80 (n/a)</td><td>238.90 (n/a)</td><td>83.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(-43.78%)</b></td><td>0.01 <b>(-41.14%)</b></td><td>0.01 <b>(-51.80%)</b></td><td>0.01 (-9.61%)</td><td>0.00 <b>(-71.39%)</b></td><td>610.00 (+10.63%)</td><td>509.94 <b>(+50.74%)</b></td><td>486.10 <b>(+107.47%)</b></td><td>395.90 <b>(+77.85%)</b></td><td>92.43 <b>(-39.71%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.40 (n/a)</td><td>338.30 (n/a)</td><td>234.30 (n/a)</td><td>222.60 (n/a)</td><td>153.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 <b>(-44.24%)</b></td><td>0.01 <b>(-42.20%)</b></td><td>0.01 <b>(-38.70%)</b></td><td>0.01 <b>(-43.48%)</b></td><td>0.00 <b>(-43.10%)</b></td><td>1067.60 <b>(+76.93%)</b></td><td>572.48 <b>(+73.64%)</b></td><td>443.20 <b>(+63.12%)</b></td><td>425.20 <b>(+79.33%)</b></td><td>278.18 <b>(+79.48%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.40 (n/a)</td><td>329.70 (n/a)</td><td>271.70 (n/a)</td><td>237.10 (n/a)</td><td>154.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(+38.18%)</b></td><td>0.02 (+9.64%)</td><td>0.01 <b>(-22.98%)</b></td><td>0.01 (-1.43%)</td><td>0.01 <b>(+85.50%)</b></td><td>607.80 (+1.45%)</td><td>423.80 (+1.94%)</td><td>467.40 <b>(+29.83%)</b></td><td>213.00 <b>(-27.62%)</b></td><td>186.24 <b>(+37.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.10 (n/a)</td><td>415.74 (n/a)</td><td>360.00 (n/a)</td><td>294.30 (n/a)</td><td>135.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(+24.10%)</b></td><td>0.02 (-7.02%)</td><td>0.01 <b>(-37.08%)</b></td><td>0.01 (+12.21%)</td><td>0.01 <b>(+40.14%)</b></td><td>686.10 (-10.87%)</td><td>417.84 (+11.41%)</td><td>473.80 <b>(+58.94%)</b></td><td>200.40 (-19.42%)</td><td>199.13 (-10.24%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>769.80 (n/a)</td><td>375.04 (n/a)</td><td>298.10 (n/a)</td><td>248.70 (n/a)</td><td>221.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (+12.34%)</td><td>0.04 (-15.74%)</td><td>0.04 <b>(-20.05%)</b></td><td>0.02 <b>(-35.50%)</b></td><td>0.02 <b>(+90.32%)</b></td><td>621.40 <b>(+55.04%)</b></td><td>378.24 <b>(+40.38%)</b></td><td>288.80 <b>(+25.08%)</b></td><td>202.20 (-11.00%)</td><td>198.28 <b>(+165.63%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>400.80 (n/a)</td><td>269.44 (n/a)</td><td>230.90 (n/a)</td><td>227.20 (n/a)</td><td>74.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 <b>(+30.62%)</b></td><td>0.03 (-10.96%)</td><td>0.02 <b>(-42.09%)</b></td><td>0.01 <b>(-69.09%)</b></td><td>0.02 <b>(+98.99%)</b></td><td>1897.40 <b>(+223.57%)</b></td><td>729.02 <b>(+75.81%)</b></td><td>608.70 <b>(+72.68%)</b></td><td>214.40 <b>(-23.46%)</b></td><td>676.98 <b>(+391.42%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.40 (n/a)</td><td>414.66 (n/a)</td><td>352.50 (n/a)</td><td>280.10 (n/a)</td><td>137.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 <b>(+38.27%)</b></td><td>0.04 <b>(+24.05%)</b></td><td>0.04 (+18.16%)</td><td>0.03 <b>(+20.01%)</b></td><td>0.02 <b>(+28.21%)</b></td><td>464.50 (-16.68%)</td><td>312.72 (-19.74%)</td><td>314.60 (-15.36%)</td><td>175.90 <b>(-27.67%)</b></td><td>111.91 <b>(-23.08%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.50 (n/a)</td><td>389.62 (n/a)</td><td>371.70 (n/a)</td><td>243.20 (n/a)</td><td>145.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (-15.58%)</td><td>0.04 (-9.28%)</td><td>0.03 (-12.31%)</td><td>0.02 (+6.64%)</td><td>0.01 <b>(-24.91%)</b></td><td>521.50 (-6.24%)</td><td>371.42 (+4.76%)</td><td>382.20 (+14.02%)</td><td>232.90 (+18.46%)</td><td>122.35 (-17.42%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>556.20 (n/a)</td><td>354.54 (n/a)</td><td>335.20 (n/a)</td><td>196.60 (n/a)</td><td>148.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (+19.22%)</td><td>0.03 (+2.43%)</td><td>0.03 (+12.65%)</td><td>0.02 (+1.61%)</td><td>0.01 (+11.55%)</td><td>559.70 (-1.60%)</td><td>431.66 (-2.05%)</td><td>448.90 (-11.21%)</td><td>245.20 (-16.14%)</td><td>129.04 (-4.42%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>440.68 (n/a)</td><td>505.60 (n/a)</td><td>292.40 (n/a)</td><td>135.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (+20.00%)</td><td>0.04 (+19.87%)</td><td>0.04 <b>(+36.15%)</b></td><td>0.02 (+11.34%)</td><td>0.02 (+15.81%)</td><td>589.40 (-10.19%)</td><td>374.86 (-16.35%)</td><td>349.90 <b>(-26.54%)</b></td><td>218.40 (-16.67%)</td><td>157.85 (-10.67%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>448.12 (n/a)</td><td>476.30 (n/a)</td><td>262.10 (n/a)</td><td>176.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (+17.21%)</td><td>0.09 (+8.89%)</td><td>0.09 (+12.77%)</td><td>0.05 (-1.22%)</td><td>0.02 <b>(+27.56%)</b></td><td>449.60 (+1.24%)</td><td>299.72 (-6.43%)</td><td>268.00 (-11.32%)</td><td>212.20 (-14.68%)</td><td>90.34 (+14.88%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>444.10 (n/a)</td><td>320.32 (n/a)</td><td>302.20 (n/a)</td><td>248.70 (n/a)</td><td>78.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (-9.31%)</td><td>0.07 (-18.18%)</td><td>0.07 <b>(-20.47%)</b></td><td>0.04 <b>(-21.35%)</b></td><td>0.03 (+10.57%)</td><td>669.10 <b>(+27.13%)</b></td><td>429.74 <b>(+30.14%)</b></td><td>340.00 <b>(+25.74%)</b></td><td>260.10 (+10.26%)</td><td>191.90 <b>(+57.86%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.30 (n/a)</td><td>330.22 (n/a)</td><td>270.40 (n/a)</td><td>235.90 (n/a)</td><td>121.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 <b>(+28.72%)</b></td><td>0.07 (+16.62%)</td><td>0.05 (+1.72%)</td><td>0.04 (-12.12%)</td><td>0.03 <b>(+77.71%)</b></td><td>661.40 (+13.80%)</td><td>438.66 (-3.63%)</td><td>483.80 (-1.69%)</td><td>214.30 <b>(-22.33%)</b></td><td>193.93 <b>(+54.45%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.20 (n/a)</td><td>455.16 (n/a)</td><td>492.10 (n/a)</td><td>275.90 (n/a)</td><td>125.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 <b>(+43.03%)</b></td><td>0.08 <b>(+50.10%)</b></td><td>0.06 <b>(+28.32%)</b></td><td>0.05 (+17.64%)</td><td>0.04 <b>(+71.65%)</b></td><td>498.90 (-14.99%)</td><td>357.80 <b>(-28.36%)</b></td><td>430.80 <b>(-22.07%)</b></td><td>179.80 <b>(-30.09%)</b></td><td>146.24 (+5.78%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>586.90 (n/a)</td><td>499.42 (n/a)</td><td>552.80 (n/a)</td><td>257.20 (n/a)</td><td>138.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 <b>(-31.11%)</b></td><td>0.05 <b>(-21.50%)</b></td><td>0.05 (-18.51%)</td><td>0.04 <b>(+48.97%)</b></td><td>0.01 <b>(-66.72%)</b></td><td>579.70 <b>(-32.87%)</b></td><td>497.14 (+8.95%)</td><td>518.30 <b>(+22.73%)</b></td><td>376.00 <b>(+45.17%)</b></td><td>75.27 <b>(-68.90%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>863.60 (n/a)</td><td>456.32 (n/a)</td><td>422.30 (n/a)</td><td>259.00 (n/a)</td><td>242.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (+9.71%)</td><td>0.06 (-12.23%)</td><td>0.06 (-15.50%)</td><td>0.04 (-12.93%)</td><td>0.03 (+14.90%)</td><td>600.70 (+14.83%)</td><td>445.24 (+16.65%)</td><td>434.70 (+18.32%)</td><td>235.70 (-8.82%)</td><td>139.87 (+16.53%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.10 (n/a)</td><td>381.70 (n/a)</td><td>367.40 (n/a)</td><td>258.50 (n/a)</td><td>120.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 <b>(-37.11%)</b></td><td>0.16 (-0.60%)</td><td>0.17 <b>(+49.45%)</b></td><td>0.10 <b>(+61.26%)</b></td><td>0.05 <b>(-54.96%)</b></td><td>476.60 <b>(-37.99%)</b></td><td>341.60 (-19.03%)</td><td>297.40 <b>(-33.08%)</b></td><td>246.10 <b>(+58.98%)</b></td><td>107.45 <b>(-54.14%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.10 (n/a)</td><td>768.60 (n/a)</td><td>421.90 (n/a)</td><td>444.40 (n/a)</td><td>154.80 (n/a)</td><td>234.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (-14.82%)</td><td>0.12 <b>(-26.77%)</b></td><td>0.11 <b>(-38.63%)</b></td><td>0.09 <b>(-24.63%)</b></td><td>0.03 (-7.61%)</td><td>560.30 <b>(+32.68%)</b></td><td>422.20 <b>(+38.22%)</b></td><td>446.10 <b>(+62.93%)</b></td><td>293.80 (+17.43%)</td><td>104.36 <b>(+43.41%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>422.30 (n/a)</td><td>305.46 (n/a)</td><td>273.80 (n/a)</td><td>250.20 (n/a)</td><td>72.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 <b>(+23.74%)</b></td><td>0.15 (-9.65%)</td><td>0.09 <b>(-50.27%)</b></td><td>0.05 <b>(-48.58%)</b></td><td>0.11 <b>(+66.04%)</b></td><td>1012.50 <b>(+94.49%)</b></td><td>513.10 <b>(+48.00%)</b></td><td>574.10 <b>(+101.09%)</b></td><td>160.80 (-19.20%)</td><td>340.46 <b>(+132.93%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>520.60 (n/a)</td><td>346.70 (n/a)</td><td>285.50 (n/a)</td><td>199.00 (n/a)</td><td>146.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.23 <b>(+23.09%)</b></td><td>0.15 (+2.29%)</td><td>0.12 <b>(-23.90%)</b></td><td>0.09 (-7.03%)</td><td>0.06 <b>(+54.32%)</b></td><td>545.40 (+7.55%)</td><td>384.02 (+3.93%)</td><td>416.00 <b>(+31.40%)</b></td><td>215.10 (-18.77%)</td><td>141.90 <b>(+30.10%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>507.10 (n/a)</td><td>369.50 (n/a)</td><td>316.60 (n/a)</td><td>264.80 (n/a)</td><td>109.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (+1.55%)</td><td>0.12 (-17.57%)</td><td>0.09 <b>(-24.04%)</b></td><td>0.08 (-5.15%)</td><td>0.07 (+15.55%)</td><td>605.20 (+5.44%)</td><td>477.18 <b>(+26.55%)</b></td><td>523.20 <b>(+31.66%)</b></td><td>204.50 (-1.54%)</td><td>160.77 (+16.29%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>574.00 (n/a)</td><td>377.08 (n/a)</td><td>397.40 (n/a)</td><td>207.70 (n/a)</td><td>138.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 (+2.41%)</td><td>0.14 (-2.95%)</td><td>0.11 <b>(-28.33%)</b></td><td>0.08 (+14.43%)</td><td>0.06 (+14.26%)</td><td>591.60 (-12.60%)</td><td>411.16 (+3.78%)</td><td>440.70 <b>(+39.55%)</b></td><td>241.90 (-2.38%)</td><td>157.14 (-9.24%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>676.90 (n/a)</td><td>396.20 (n/a)</td><td>315.80 (n/a)</td><td>247.80 (n/a)</td><td>173.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 <b>(+59.36%)</b></td><td>0.01 <b>(+60.16%)</b></td><td>0.01 <b>(+90.54%)</b></td><td>0.01 (+2.16%)</td><td>0.00 <b>(+117.27%)</b></td><td>515.90 (-2.11%)</td><td>299.22 <b>(-32.81%)</b></td><td>245.20 <b>(-47.53%)</b></td><td>191.30 <b>(-37.26%)</b></td><td>126.95 <b>(+45.65%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>527.00 (n/a)</td><td>445.34 (n/a)</td><td>467.30 (n/a)</td><td>304.90 (n/a)</td><td>87.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (-2.41%)</td><td>0.01 (+11.24%)</td><td>0.01 <b>(+57.88%)</b></td><td>0.00 <b>(-68.98%)</b></td><td>0.00 (+19.48%)</td><td>2473.80 <b>(+222.32%)</b></td><td>710.50 <b>(+62.46%)</b></td><td>290.80 <b>(-36.67%)</b></td><td>237.50 (+2.46%)</td><td>986.01 <b>(+358.15%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>767.50 (n/a)</td><td>437.34 (n/a)</td><td>459.20 (n/a)</td><td>231.80 (n/a)</td><td>215.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (-0.50%)</td><td>0.01 (+3.52%)</td><td>0.01 (+4.31%)</td><td>0.00 (-8.41%)</td><td>0.00 (+7.00%)</td><td>549.00 (+9.19%)</td><td>345.18 (-1.98%)</td><td>269.40 (-4.13%)</td><td>239.60 (+0.50%)</td><td>136.45 (+9.68%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.80 (n/a)</td><td>352.14 (n/a)</td><td>281.00 (n/a)</td><td>238.40 (n/a)</td><td>124.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (+10.25%)</td><td>0.01 <b>(+40.34%)</b></td><td>0.01 <b>(+69.00%)</b></td><td>0.00 (+0.32%)</td><td>0.00 (+7.65%)</td><td>552.20 (-0.32%)</td><td>336.56 <b>(-28.05%)</b></td><td>291.60 <b>(-40.83%)</b></td><td>244.50 (-9.28%)</td><td>123.56 (+7.41%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>554.00 (n/a)</td><td>467.74 (n/a)</td><td>492.80 (n/a)</td><td>269.50 (n/a)</td><td>115.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (+9.71%)</td><td>0.01 (-9.34%)</td><td>0.01 <b>(-29.81%)</b></td><td>0.00 <b>(-27.39%)</b></td><td>0.00 <b>(+35.27%)</b></td><td>818.00 <b>(+37.71%)</b></td><td>446.50 <b>(+23.12%)</b></td><td>387.20 <b>(+42.51%)</b></td><td>240.80 (-8.86%)</td><td>241.62 <b>(+66.40%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>594.00 (n/a)</td><td>362.64 (n/a)</td><td>271.70 (n/a)</td><td>264.20 (n/a)</td><td>145.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 <b>(-21.93%)</b></td><td>0.01 (+4.33%)</td><td>0.01 <b>(+54.16%)</b></td><td>0.01 <b>(+25.55%)</b></td><td>0.00 <b>(-52.93%)</b></td><td>477.30 <b>(-20.34%)</b></td><td>377.28 (-14.05%)</td><td>341.80 <b>(-35.13%)</b></td><td>306.40 <b>(+28.09%)</b></td><td>80.16 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>599.20 (n/a)</td><td>438.94 (n/a)</td><td>526.90 (n/a)</td><td>239.20 (n/a)</td><td>166.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(-27.94%)</b></td><td>0.02 (+17.10%)</td><td>0.02 <b>(+70.97%)</b></td><td>0.02 <b>(+79.37%)</b></td><td>0.00 <b>(-82.71%)</b></td><td>281.70 <b>(-44.25%)</b></td><td>260.46 <b>(-29.21%)</b></td><td>261.80 <b>(-41.50%)</b></td><td>235.20 <b>(+38.76%)</b></td><td>20.08 <b>(-87.07%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>505.30 (n/a)</td><td>367.92 (n/a)</td><td>447.50 (n/a)</td><td>169.50 (n/a)</td><td>155.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(+34.14%)</b></td><td>0.02 <b>(+33.17%)</b></td><td>0.02 <b>(+54.85%)</b></td><td>0.01 <b>(+20.67%)</b></td><td>0.01 <b>(+31.55%)</b></td><td>414.40 (-17.14%)</td><td>269.74 <b>(-24.26%)</b></td><td>240.00 <b>(-35.41%)</b></td><td>196.50 <b>(-25.43%)</b></td><td>84.84 (-11.53%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>356.12 (n/a)</td><td>371.60 (n/a)</td><td>263.50 (n/a)</td><td>95.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(+22.03%)</b></td><td>0.02 <b>(+33.01%)</b></td><td>0.02 <b>(+83.76%)</b></td><td>0.01 <b>(-26.51%)</b></td><td>0.01 <b>(+86.88%)</b></td><td>634.50 <b>(+36.07%)</b></td><td>349.72 (-13.61%)</td><td>235.00 <b>(-45.58%)</b></td><td>205.30 (-18.08%)</td><td>186.52 <b>(+111.36%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.30 (n/a)</td><td>404.82 (n/a)</td><td>431.80 (n/a)</td><td>250.60 (n/a)</td><td>88.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+2.03%)</td><td>0.02 (+5.68%)</td><td>0.01 (+17.01%)</td><td>0.01 (-6.41%)</td><td>0.01 (-5.99%)</td><td>605.40 (+6.85%)</td><td>385.86 (-7.14%)</td><td>420.40 (-14.54%)</td><td>229.60 (-2.01%)</td><td>153.75 (-5.09%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.60 (n/a)</td><td>415.52 (n/a)</td><td>491.90 (n/a)</td><td>234.30 (n/a)</td><td>161.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-7.93%)</td><td>0.01 (-2.17%)</td><td>0.01 (-18.01%)</td><td>0.01 (+17.98%)</td><td>0.00 <b>(-29.19%)</b></td><td>472.80 (-15.24%)</td><td>375.92 (-3.96%)</td><td>396.30 <b>(+21.94%)</b></td><td>268.30 (+8.62%)</td><td>90.85 <b>(-39.02%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>391.40 (n/a)</td><td>325.00 (n/a)</td><td>247.00 (n/a)</td><td>148.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+15.29%)</td><td>0.02 <b>(+26.03%)</b></td><td>0.02 <b>(+59.76%)</b></td><td>0.01 (-7.57%)</td><td>0.00 <b>(+25.11%)</b></td><td>612.60 (+8.19%)</td><td>370.56 (-18.43%)</td><td>305.00 <b>(-37.41%)</b></td><td>265.70 (-13.28%)</td><td>141.58 (+19.17%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.20 (n/a)</td><td>454.26 (n/a)</td><td>487.30 (n/a)</td><td>306.40 (n/a)</td><td>118.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-1.56%)</td><td>0.03 (-6.21%)</td><td>0.03 (-1.86%)</td><td>0.02 (+8.92%)</td><td>0.01 (-9.12%)</td><td>520.70 (-8.20%)</td><td>352.16 (+4.32%)</td><td>309.20 (+1.88%)</td><td>248.20 (+1.55%)</td><td>108.63 (-17.49%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.20 (n/a)</td><td>337.58 (n/a)</td><td>303.50 (n/a)</td><td>244.40 (n/a)</td><td>131.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-18.44%)</td><td>0.03 (-16.32%)</td><td>0.04 (-12.17%)</td><td>0.01 <b>(-41.47%)</b></td><td>0.01 (-3.94%)</td><td>761.30 <b>(+70.89%)</b></td><td>403.12 <b>(+28.58%)</b></td><td>280.40 (+13.89%)</td><td>245.00 <b>(+22.62%)</b></td><td>219.85 <b>(+82.26%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.50 (n/a)</td><td>313.52 (n/a)</td><td>246.20 (n/a)</td><td>199.80 (n/a)</td><td>120.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (-3.01%)</td><td>0.04 (+6.81%)</td><td>0.04 (+9.93%)</td><td>0.02 (-6.20%)</td><td>0.01 (-6.30%)</td><td>507.70 (+6.61%)</td><td>297.88 (-6.08%)</td><td>250.40 (-9.01%)</td><td>231.80 (+3.11%)</td><td>117.74 (+9.48%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.20 (n/a)</td><td>317.16 (n/a)</td><td>275.20 (n/a)</td><td>224.80 (n/a)</td><td>107.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-6.18%)</td><td>0.03 (-0.27%)</td><td>0.02 (-0.12%)</td><td>0.02 (+14.32%)</td><td>0.01 (-18.60%)</td><td>515.20 (-12.51%)</td><td>406.92 (-2.74%)</td><td>436.40 (+0.11%)</td><td>298.00 (+6.58%)</td><td>102.00 <b>(-23.19%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>418.40 (n/a)</td><td>435.90 (n/a)</td><td>279.60 (n/a)</td><td>132.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-12.49%)</td><td>0.03 (-3.47%)</td><td>0.04 (+14.65%)</td><td>0.02 <b>(-29.72%)</b></td><td>0.01 (-4.50%)</td><td>606.50 <b>(+42.27%)</b></td><td>340.98 (+7.52%)</td><td>273.00 (-12.78%)</td><td>262.60 (+14.27%)</td><td>148.86 <b>(+66.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>426.30 (n/a)</td><td>317.12 (n/a)</td><td>313.00 (n/a)</td><td>229.80 (n/a)</td><td>89.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-12.27%)</td><td>0.03 (+9.78%)</td><td>0.03 <b>(+36.49%)</b></td><td>0.02 (+9.36%)</td><td>0.01 <b>(-23.18%)</b></td><td>470.70 (-8.55%)</td><td>374.22 (-10.76%)</td><td>338.70 <b>(-26.74%)</b></td><td>292.90 (+13.97%)</td><td>86.14 (-15.15%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.70 (n/a)</td><td>419.36 (n/a)</td><td>462.30 (n/a)</td><td>257.00 (n/a)</td><td>101.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 <b>(+42.09%)</b></td><td>0.06 <b>(+29.51%)</b></td><td>0.05 <b>(+28.27%)</b></td><td>0.03 (-18.37%)</td><td>0.03 <b>(+200.22%)</b></td><td>668.10 <b>(+22.50%)</b></td><td>435.62 (-10.70%)</td><td>401.80 <b>(-22.04%)</b></td><td>250.20 <b>(-29.60%)</b></td><td>195.09 <b>(+156.48%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>545.40 (n/a)</td><td>487.80 (n/a)</td><td>515.40 (n/a)</td><td>355.40 (n/a)</td><td>76.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (-0.14%)</td><td>0.07 <b>(+37.72%)</b></td><td>0.07 <b>(+71.28%)</b></td><td>0.05 <b>(+49.04%)</b></td><td>0.01 <b>(-39.87%)</b></td><td>386.70 <b>(-32.90%)</b></td><td>300.80 <b>(-32.78%)</b></td><td>299.60 <b>(-41.62%)</b></td><td>247.80 (+0.16%)</td><td>55.74 <b>(-60.53%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.30 (n/a)</td><td>447.48 (n/a)</td><td>513.20 (n/a)</td><td>247.40 (n/a)</td><td>141.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (-5.35%)</td><td>0.06 (+0.27%)</td><td>0.08 <b>(+67.45%)</b></td><td>0.01 <b>(-71.89%)</b></td><td>0.03 <b>(+25.18%)</b></td><td>2011.90 <b>(+255.77%)</b></td><td>632.22 <b>(+67.07%)</b></td><td>250.80 <b>(-40.29%)</b></td><td>232.20 (+5.64%)</td><td>775.32 <b>(+416.45%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>565.50 (n/a)</td><td>378.42 (n/a)</td><td>420.00 (n/a)</td><td>219.80 (n/a)</td><td>150.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (+10.08%)</td><td>0.06 (+5.81%)</td><td>0.08 (+2.03%)</td><td>0.03 (+0.55%)</td><td>0.02 (+4.66%)</td><td>611.90 (-0.55%)</td><td>378.02 (-5.74%)</td><td>268.60 (-2.01%)</td><td>241.40 (-9.15%)</td><td>171.18 (-5.49%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.30 (n/a)</td><td>401.06 (n/a)</td><td>274.10 (n/a)</td><td>265.70 (n/a)</td><td>181.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (+5.32%)</td><td>0.07 <b>(+55.69%)</b></td><td>0.09 <b>(+131.06%)</b></td><td>0.05 <b>(+30.88%)</b></td><td>0.02 (-2.39%)</td><td>463.10 <b>(-23.59%)</b></td><td>311.18 <b>(-37.71%)</b></td><td>243.20 <b>(-56.72%)</b></td><td>240.30 (-5.02%)</td><td>100.92 <b>(-28.96%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.10 (n/a)</td><td>499.58 (n/a)</td><td>561.90 (n/a)</td><td>253.00 (n/a)</td><td>142.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 <b>(+35.31%)</b></td><td>0.06 <b>(+34.90%)</b></td><td>0.07 <b>(+71.42%)</b></td><td>0.04 (+17.94%)</td><td>0.02 <b>(+79.14%)</b></td><td>594.20 (-15.21%)</td><td>412.62 <b>(-21.45%)</b></td><td>320.70 <b>(-41.66%)</b></td><td>277.20 <b>(-26.08%)</b></td><td>158.52 (+19.30%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>700.80 (n/a)</td><td>525.28 (n/a)</td><td>549.70 (n/a)</td><td>375.00 (n/a)</td><td>132.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.60 (n/a)</td><td>426.70 (n/a)</td><td>449.90 (n/a)</td><td>305.50 (n/a)</td><td>104.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.90 (n/a)</td><td>355.94 (n/a)</td><td>362.40 (n/a)</td><td>265.00 (n/a)</td><td>85.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.20 (n/a)</td><td>471.74 (n/a)</td><td>505.00 (n/a)</td><td>284.20 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.20 (n/a)</td><td>381.86 (n/a)</td><td>307.60 (n/a)</td><td>280.10 (n/a)</td><td>137.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.40 (n/a)</td><td>399.96 (n/a)</td><td>453.10 (n/a)</td><td>261.20 (n/a)</td><td>106.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.00 (n/a)</td><td>460.30 (n/a)</td><td>488.90 (n/a)</td><td>305.50 (n/a)</td><td>141.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>491.50 (n/a)</td><td>351.28 (n/a)</td><td>304.30 (n/a)</td><td>252.00 (n/a)</td><td>104.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>601.60 (n/a)</td><td>414.82 (n/a)</td><td>398.90 (n/a)</td><td>236.90 (n/a)</td><td>148.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>597.40 (n/a)</td><td>451.26 (n/a)</td><td>525.30 (n/a)</td><td>213.30 (n/a)</td><td>166.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 (+6.70%)</td><td>0.15 <b>(+31.79%)</b></td><td>0.17 <b>(+69.38%)</b></td><td>0.09 (+16.03%)</td><td>0.05 (+14.04%)</td><td>531.30 (-13.81%)</td><td>355.84 <b>(-23.31%)</b></td><td>283.00 <b>(-40.96%)</b></td><td>247.50 (-6.25%)</td><td>126.86 (-2.62%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>616.40 (n/a)</td><td>463.98 (n/a)</td><td>479.30 (n/a)</td><td>264.00 (n/a)</td><td>130.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>580.80 (n/a)</td><td>463.08 (n/a)</td><td>488.60 (n/a)</td><td>320.90 (n/a)</td><td>115.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>607.40 (n/a)</td><td>490.78 (n/a)</td><td>541.10 (n/a)</td><td>277.30 (n/a)</td><td>130.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.40 (n/a)</td><td>320.94 (n/a)</td><td>297.00 (n/a)</td><td>269.30 (n/a)</td><td>80.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.50 (n/a)</td><td>334.08 (n/a)</td><td>290.50 (n/a)</td><td>227.50 (n/a)</td><td>158.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1907.40 (n/a)</td><td>710.70 (n/a)</td><td>508.50 (n/a)</td><td>273.60 (n/a)</td><td>677.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>569.30 (n/a)</td><td>414.48 (n/a)</td><td>458.20 (n/a)</td><td>247.70 (n/a)</td><td>141.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.00 (n/a)</td><td>453.78 (n/a)</td><td>473.40 (n/a)</td><td>287.80 (n/a)</td><td>155.78 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.10 (n/a)</td><td>450.76 (n/a)</td><td>505.60 (n/a)</td><td>282.50 (n/a)</td><td>127.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>635.20 (n/a)</td><td>454.10 (n/a)</td><td>455.20 (n/a)</td><td>261.60 (n/a)</td><td>152.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>585.40 (n/a)</td><td>388.18 (n/a)</td><td>350.10 (n/a)</td><td>228.00 (n/a)</td><td>152.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>675.70 (n/a)</td><td>551.84 (n/a)</td><td>633.50 (n/a)</td><td>277.00 (n/a)</td><td>164.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>485.10 (n/a)</td><td>389.88 (n/a)</td><td>456.30 (n/a)</td><td>259.90 (n/a)</td><td>108.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>1822.90 (n/a)</td><td>627.78 (n/a)</td><td>312.60 (n/a)</td><td>196.20 (n/a)</td><td>681.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.51 (+7.02%)</td><td>3.42 (-9.10%)</td><td>3.58 (-9.94%)</td><td>2.29 (-14.88%)</td><td>0.92 <b>(+50.25%)</b></td><td>4586.40 (+17.48%)</td><td>3266.84 (+14.05%)</td><td>2928.60 (+11.04%)</td><td>2324.60 (-6.56%)</td><td>941.79 <b>(+60.92%)</b></td><td>1847.59 (+7.02%)</td><td>1400.14 (-9.10%)</td><td>1466.58 (-9.94%)</td><td>936.46 (-14.88%)</td><td>375.83 <b>(+50.25%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.22 (n/a)</td><td>3.76 (n/a)</td><td>3.98 (n/a)</td><td>2.69 (n/a)</td><td>0.61 (n/a)</td><td>3903.90 (n/a)</td><td>2864.36 (n/a)</td><td>2637.40 (n/a)</td><td>2487.70 (n/a)</td><td>585.27 (n/a)</td><td>1726.47 (n/a)</td><td>1540.26 (n/a)</td><td>1628.50 (n/a)</td><td>1100.17 (n/a)</td><td>250.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.45 (-4.42%)</td><td>3.19 (-1.91%)</td><td>3.20 (-0.52%)</td><td>2.86 (-0.14%)</td><td>0.26 (-10.52%)</td><td>8239.10 (+0.14%)</td><td>7431.54 (+1.84%)</td><td>7366.20 (+0.52%)</td><td>6829.40 (+4.63%)</td><td>620.50 (-6.95%)</td><td>1965.31 (-4.42%)</td><td>1816.03 (-1.91%)</td><td>1822.07 (-0.52%)</td><td>1629.04 (-0.14%)</td><td>149.54 (-10.52%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.61 (n/a)</td><td>3.25 (n/a)</td><td>3.22 (n/a)</td><td>2.87 (n/a)</td><td>0.29 (n/a)</td><td>8227.40 (n/a)</td><td>7297.44 (n/a)</td><td>7327.80 (n/a)</td><td>6527.20 (n/a)</td><td>666.86 (n/a)</td><td>2056.30 (n/a)</td><td>1851.44 (n/a)</td><td>1831.63 (n/a)</td><td>1631.36 (n/a)</td><td>167.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.67 (-4.27%)</td><td>3.31 (-3.42%)</td><td>3.36 (-6.11%)</td><td>2.83 (-7.72%)</td><td>0.31 (-9.78%)</td><td>5930.30 (+8.37%)</td><td>5103.90 (+3.47%)</td><td>4998.70 (+6.50%)</td><td>4572.90 (+4.46%)</td><td>502.81 (+1.78%)</td><td>1878.43 (-4.27%)</td><td>1695.29 (-3.42%)</td><td>1718.43 (-6.11%)</td><td>1448.47 (-7.72%)</td><td>156.39 (-9.78%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.83 (n/a)</td><td>3.43 (n/a)</td><td>3.57 (n/a)</td><td>3.07 (n/a)</td><td>0.34 (n/a)</td><td>5472.30 (n/a)</td><td>4932.62 (n/a)</td><td>4693.40 (n/a)</td><td>4377.70 (n/a)</td><td>494.00 (n/a)</td><td>1962.20 (n/a)</td><td>1755.32 (n/a)</td><td>1830.22 (n/a)</td><td>1569.71 (n/a)</td><td>173.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.48 (+9.22%)</td><td>0.85 (-13.51%)</td><td>0.81 <b>(-21.98%)</b></td><td>0.14 <b>(-80.41%)</b></td><td>0.49 <b>(+80.77%)</b></td><td>3299.20 <b>(+410.40%)</b></td><td>1039.30 <b>(+110.59%)</b></td><td>563.80 <b>(+28.17%)</b></td><td>309.40 (-8.46%)</td><td>1268.37 <b>(+836.20%)</b></td><td>108.44 (+9.22%)</td><td>62.51 (-13.51%)</td><td>59.51 <b>(-21.98%)</b></td><td>10.17 <b>(-80.41%)</b></td><td>35.81 <b>(+80.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.36 (n/a)</td><td>0.99 (n/a)</td><td>1.04 (n/a)</td><td>0.71 (n/a)</td><td>0.27 (n/a)</td><td>646.40 (n/a)</td><td>493.52 (n/a)</td><td>439.90 (n/a)</td><td>338.00 (n/a)</td><td>135.48 (n/a)</td><td>99.28 (n/a)</td><td>72.28 (n/a)</td><td>76.28 (n/a)</td><td>51.91 (n/a)</td><td>19.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.71 (+15.76%)</td><td>0.90 (-17.20%)</td><td>0.87 <b>(-37.95%)</b></td><td>0.19 <b>(-42.98%)</b></td><td>0.54 (+9.88%)</td><td>3485.20 <b>(+75.37%)</b></td><td>1228.40 <b>(+48.39%)</b></td><td>756.50 <b>(+61.16%)</b></td><td>384.00 (-13.61%)</td><td>1273.90 <b>(+92.31%)</b></td><td>174.78 (+15.76%)</td><td>92.59 (-17.20%)</td><td>88.72 <b>(-37.95%)</b></td><td>19.26 <b>(-42.98%)</b></td><td>55.78 (+9.88%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.47 (n/a)</td><td>1.09 (n/a)</td><td>1.40 (n/a)</td><td>0.33 (n/a)</td><td>0.50 (n/a)</td><td>1987.30 (n/a)</td><td>827.82 (n/a)</td><td>469.40 (n/a)</td><td>444.50 (n/a)</td><td>662.42 (n/a)</td><td>150.99 (n/a)</td><td>111.83 (n/a)</td><td>142.98 (n/a)</td><td>33.77 (n/a)</td><td>50.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.50 (-18.51%)</td><td>1.13 <b>(-30.75%)</b></td><td>1.09 <b>(-30.40%)</b></td><td>0.69 <b>(-52.05%)</b></td><td>0.30 <b>(+74.13%)</b></td><td>1096.00 <b>(+108.56%)</b></td><td>717.28 <b>(+53.24%)</b></td><td>688.80 <b>(+43.68%)</b></td><td>501.40 <b>(+22.71%)</b></td><td>227.99 <b>(+364.55%)</b></td><td>167.30 (-18.51%)</td><td>125.23 <b>(-30.75%)</b></td><td>121.79 <b>(-30.40%)</b></td><td>76.54 <b>(-52.05%)</b></td><td>33.64 <b>(+74.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.84 (n/a)</td><td>1.62 (n/a)</td><td>1.57 (n/a)</td><td>1.43 (n/a)</td><td>0.17 (n/a)</td><td>525.50 (n/a)</td><td>468.08 (n/a)</td><td>479.40 (n/a)</td><td>408.60 (n/a)</td><td>49.08 (n/a)</td><td>205.32 (n/a)</td><td>180.84 (n/a)</td><td>175.00 (n/a)</td><td>159.62 (n/a)</td><td>19.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.85 (-0.06%)</td><td>1.50 (+4.04%)</td><td>1.48 (+10.51%)</td><td>1.17 (+7.11%)</td><td>0.32 (-5.24%)</td><td>894.20 (-6.64%)</td><td>728.16 (-4.47%)</td><td>710.90 (-9.51%)</td><td>565.70 (+0.05%)</td><td>157.41 (-9.51%)</td><td>237.24 (-0.06%)</td><td>191.43 (+4.04%)</td><td>188.80 (+10.51%)</td><td>150.09 (+7.11%)</td><td>41.30 (-5.24%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.85 (n/a)</td><td>1.44 (n/a)</td><td>1.33 (n/a)</td><td>1.09 (n/a)</td><td>0.34 (n/a)</td><td>957.80 (n/a)</td><td>762.22 (n/a)</td><td>785.60 (n/a)</td><td>565.40 (n/a)</td><td>173.95 (n/a)</td><td>237.39 (n/a)</td><td>183.99 (n/a)</td><td>170.85 (n/a)</td><td>140.13 (n/a)</td><td>43.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.61 <b>(-31.15%)</b></td><td>1.17 <b>(-46.03%)</b></td><td>1.16 <b>(-47.29%)</b></td><td>0.80 <b>(-57.91%)</b></td><td>0.32 <b>(+88.74%)</b></td><td>1317.10 <b>(+137.57%)</b></td><td>948.66 <b>(+95.64%)</b></td><td>900.60 <b>(+89.72%)</b></td><td>651.80 <b>(+45.23%)</b></td><td>260.05 <b>(+542.22%)</b></td><td>205.92 <b>(-31.15%)</b></td><td>150.15 <b>(-46.03%)</b></td><td>149.04 <b>(-47.29%)</b></td><td>101.90 <b>(-57.91%)</b></td><td>40.45 <b>(+88.74%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.34 (n/a)</td><td>2.17 (n/a)</td><td>2.21 (n/a)</td><td>1.89 (n/a)</td><td>0.17 (n/a)</td><td>554.40 (n/a)</td><td>484.90 (n/a)</td><td>474.70 (n/a)</td><td>448.80 (n/a)</td><td>40.49 (n/a)</td><td>299.06 (n/a)</td><td>278.23 (n/a)</td><td>282.76 (n/a)</td><td>242.10 (n/a)</td><td>21.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.38 (-3.20%)</td><td>1.80 (+7.27%)</td><td>2.02 (+15.19%)</td><td>1.02 <b>(+245.57%)</b></td><td>0.60 <b>(-32.47%)</b></td><td>1024.60 <b>(-71.06%)</b></td><td>647.06 <b>(-43.32%)</b></td><td>518.10 (-13.20%)</td><td>440.30 (+3.31%)</td><td>252.45 <b>(-81.25%)</b></td><td>304.83 (-3.20%)</td><td>230.82 (+7.27%)</td><td>259.04 (+15.19%)</td><td>130.99 <b>(+245.57%)</b></td><td>76.24 <b>(-32.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.46 (n/a)</td><td>1.68 (n/a)</td><td>1.76 (n/a)</td><td>0.30 (n/a)</td><td>0.88 (n/a)</td><td>3540.70 (n/a)</td><td>1141.58 (n/a)</td><td>596.90 (n/a)</td><td>426.20 (n/a)</td><td>1346.39 (n/a)</td><td>314.91 (n/a)</td><td>215.18 (n/a)</td><td>224.88 (n/a)</td><td>37.91 (n/a)</td><td>112.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.83 (-4.59%)</td><td>1.11 (-4.70%)</td><td>1.29 (+7.91%)</td><td>0.29 (-1.86%)</td><td>0.69 (+13.68%)</td><td>3573.90 (+1.90%)</td><td>1553.08 (+14.69%)</td><td>814.20 (-7.32%)</td><td>571.80 (+4.80%)</td><td>1303.97 (+6.69%)</td><td>234.72 (-4.59%)</td><td>141.77 (-4.70%)</td><td>164.86 (+7.91%)</td><td>37.55 (-1.86%)</td><td>88.06 (+13.68%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.92 (n/a)</td><td>1.16 (n/a)</td><td>1.19 (n/a)</td><td>0.30 (n/a)</td><td>0.61 (n/a)</td><td>3507.30 (n/a)</td><td>1354.14 (n/a)</td><td>878.50 (n/a)</td><td>545.60 (n/a)</td><td>1222.25 (n/a)</td><td>246.01 (n/a)</td><td>148.76 (n/a)</td><td>152.78 (n/a)</td><td>38.27 (n/a)</td><td>77.47 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.55 (-14.91%)</td><td>1.14 <b>(-28.03%)</b></td><td>1.25 <b>(-25.59%)</b></td><td>0.30 <b>(-75.80%)</b></td><td>0.49 <b>(+105.75%)</b></td><td>3494.90 <b>(+313.21%)</b></td><td>1326.30 <b>(+96.41%)</b></td><td>839.20 <b>(+34.38%)</b></td><td>677.10 (+17.53%)</td><td>1214.58 <b>(+997.23%)</b></td><td>198.24 (-14.91%)</td><td>145.91 <b>(-28.03%)</b></td><td>159.93 <b>(-25.59%)</b></td><td>38.40 <b>(-75.80%)</b></td><td>62.48 <b>(+105.75%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.82 (n/a)</td><td>1.58 (n/a)</td><td>1.68 (n/a)</td><td>1.24 (n/a)</td><td>0.24 (n/a)</td><td>845.80 (n/a)</td><td>675.26 (n/a)</td><td>624.50 (n/a)</td><td>576.10 (n/a)</td><td>110.70 (n/a)</td><td>232.97 (n/a)</td><td>202.73 (n/a)</td><td>214.93 (n/a)</td><td>158.69 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.73 (-17.60%)</td><td>1.15 <b>(-20.34%)</b></td><td>1.23 (-0.69%)</td><td>0.46 <b>(-60.88%)</b></td><td>0.46 (+19.37%)</td><td>2260.40 <b>(+155.59%)</b></td><td>1113.18 <b>(+45.77%)</b></td><td>855.70 (+0.71%)</td><td>606.60 <b>(+21.37%)</b></td><td>659.56 <b>(+303.33%)</b></td><td>221.27 (-17.60%)</td><td>146.72 <b>(-20.34%)</b></td><td>156.86 (-0.69%)</td><td>59.38 <b>(-60.88%)</b></td><td>59.17 (+19.37%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.10 (n/a)</td><td>1.44 (n/a)</td><td>1.23 (n/a)</td><td>1.19 (n/a)</td><td>0.39 (n/a)</td><td>884.40 (n/a)</td><td>763.68 (n/a)</td><td>849.70 (n/a)</td><td>499.80 (n/a)</td><td>163.53 (n/a)</td><td>268.54 (n/a)</td><td>184.17 (n/a)</td><td>157.95 (n/a)</td><td>151.77 (n/a)</td><td>49.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.19 (+2.89%)</td><td>0.84 (-5.30%)</td><td>0.83 (-16.87%)</td><td>0.60 <b>(+30.07%)</b></td><td>0.22 (-15.93%)</td><td>598.90 <b>(-23.12%)</b></td><td>450.20 (+0.36%)</td><td>433.30 <b>(+20.29%)</b></td><td>303.60 (-2.79%)</td><td>111.33 <b>(-41.27%)</b></td><td>55.26 (+2.89%)</td><td>39.26 (-5.30%)</td><td>38.72 (-16.87%)</td><td>28.01 <b>(+30.07%)</b></td><td>10.35 (-15.93%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.15 (n/a)</td><td>0.89 (n/a)</td><td>1.00 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>779.00 (n/a)</td><td>448.58 (n/a)</td><td>360.20 (n/a)</td><td>312.30 (n/a)</td><td>189.54 (n/a)</td><td>53.71 (n/a)</td><td>41.46 (n/a)</td><td>46.58 (n/a)</td><td>21.54 (n/a)</td><td>12.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.14 (-1.09%)</td><td>2.49 (-6.01%)</td><td>2.57 (-10.58%)</td><td>1.63 (-8.21%)</td><td>0.54 (-1.63%)</td><td>2578.30 (+8.95%)</td><td>1763.62 (+6.81%)</td><td>1634.50 (+11.83%)</td><td>1335.10 (+1.10%)</td><td>473.57 (+11.98%)</td><td>804.26 (-1.09%)</td><td>638.20 (-6.01%)</td><td>656.93 (-10.58%)</td><td>416.45 (-8.21%)</td><td>139.45 (-1.63%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.18 (n/a)</td><td>2.65 (n/a)</td><td>2.87 (n/a)</td><td>1.77 (n/a)</td><td>0.55 (n/a)</td><td>2366.60 (n/a)</td><td>1651.20 (n/a)</td><td>1461.60 (n/a)</td><td>1320.60 (n/a)</td><td>422.91 (n/a)</td><td>813.08 (n/a)</td><td>679.00 (n/a)</td><td>734.64 (n/a)</td><td>453.70 (n/a)</td><td>141.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.56 (-18.41%)</td><td>2.54 <b>(-24.90%)</b></td><td>2.67 <b>(-34.45%)</b></td><td>1.16 (-3.47%)</td><td>0.88 <b>(-32.71%)</b></td><td>2263.10 (+3.59%)</td><td>1195.44 <b>(+21.87%)</b></td><td>982.20 <b>(+52.56%)</b></td><td>736.40 <b>(+22.55%)</b></td><td>611.07 (-10.13%)</td><td>729.02 (-18.41%)</td><td>519.92 <b>(-24.90%)</b></td><td>546.60 <b>(-34.45%)</b></td><td>237.22 (-3.47%)</td><td>181.11 <b>(-32.71%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.36 (n/a)</td><td>3.38 (n/a)</td><td>4.07 (n/a)</td><td>1.20 (n/a)</td><td>1.31 (n/a)</td><td>2184.60 (n/a)</td><td>980.90 (n/a)</td><td>643.80 (n/a)</td><td>600.90 (n/a)</td><td>679.94 (n/a)</td><td>893.50 (n/a)</td><td>692.33 (n/a)</td><td>833.86 (n/a)</td><td>245.76 (n/a)</td><td>269.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.37 (-10.65%)</td><td>2.64 (-18.36%)</td><td>2.70 (-9.66%)</td><td>1.72 <b>(-38.63%)</b></td><td>0.63 <b>(+39.33%)</b></td><td>4577.80 <b>(+62.94%)</b></td><td>3140.18 <b>(+27.25%)</b></td><td>2917.70 (+10.70%)</td><td>2333.90 (+11.92%)</td><td>874.50 <b>(+164.90%)</b></td><td>1035.16 (-10.65%)</td><td>811.40 (-18.36%)</td><td>828.01 (-9.66%)</td><td>527.75 <b>(-38.63%)</b></td><td>192.73 <b>(+39.33%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.77 (n/a)</td><td>3.24 (n/a)</td><td>2.98 (n/a)</td><td>2.80 (n/a)</td><td>0.45 (n/a)</td><td>2809.50 (n/a)</td><td>2467.64 (n/a)</td><td>2635.80 (n/a)</td><td>2085.30 (n/a)</td><td>330.13 (n/a)</td><td>1158.53 (n/a)</td><td>993.82 (n/a)</td><td>916.59 (n/a)</td><td>859.91 (n/a)</td><td>138.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.60 (n/a)</td><td>325.02 (n/a)</td><td>296.10 (n/a)</td><td>248.60 (n/a)</td><td>83.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.00 (n/a)</td><td>503.64 (n/a)</td><td>478.20 (n/a)</td><td>387.20 (n/a)</td><td>85.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.20 (n/a)</td><td>442.76 (n/a)</td><td>488.70 (n/a)</td><td>295.50 (n/a)</td><td>142.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.70 (n/a)</td><td>359.88 (n/a)</td><td>312.00 (n/a)</td><td>272.00 (n/a)</td><td>112.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.00 (n/a)</td><td>421.08 (n/a)</td><td>509.00 (n/a)</td><td>203.90 (n/a)</td><td>154.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1924.10 (n/a)</td><td>719.14 (n/a)</td><td>465.70 (n/a)</td><td>275.20 (n/a)</td><td>678.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.60 (n/a)</td><td>411.78 (n/a)</td><td>318.70 (n/a)</td><td>286.10 (n/a)</td><td>165.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.60 (n/a)</td><td>431.02 (n/a)</td><td>418.90 (n/a)</td><td>243.90 (n/a)</td><td>143.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.80 (n/a)</td><td>373.88 (n/a)</td><td>295.70 (n/a)</td><td>276.00 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.60 (n/a)</td><td>352.54 (n/a)</td><td>275.90 (n/a)</td><td>217.70 (n/a)</td><td>163.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.50 (n/a)</td><td>428.54 (n/a)</td><td>431.10 (n/a)</td><td>238.70 (n/a)</td><td>119.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.50 (n/a)</td><td>414.06 (n/a)</td><td>405.20 (n/a)</td><td>246.20 (n/a)</td><td>134.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>679.20 (n/a)</td><td>487.36 (n/a)</td><td>530.30 (n/a)</td><td>296.30 (n/a)</td><td>180.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>505.80 (n/a)</td><td>547.00 (n/a)</td><td>337.30 (n/a)</td><td>102.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>720.10 (n/a)</td><td>568.52 (n/a)</td><td>559.50 (n/a)</td><td>440.30 (n/a)</td><td>119.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.30 (n/a)</td><td>468.06 (n/a)</td><td>478.40 (n/a)</td><td>289.80 (n/a)</td><td>108.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>507.40 (n/a)</td><td>399.42 (n/a)</td><td>485.10 (n/a)</td><td>203.30 (n/a)</td><td>138.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1056.00 (n/a)</td><td>489.60 (n/a)</td><td>382.20 (n/a)</td><td>228.20 (n/a)</td><td>335.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>670.60 (n/a)</td><td>529.22 (n/a)</td><td>493.40 (n/a)</td><td>438.40 (n/a)</td><td>91.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>652.10 (n/a)</td><td>417.18 (n/a)</td><td>298.30 (n/a)</td><td>277.70 (n/a)</td><td>175.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>494.90 (n/a)</td><td>414.90 (n/a)</td><td>416.60 (n/a)</td><td>262.60 (n/a)</td><td>93.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1807.60 (n/a)</td><td>712.34 (n/a)</td><td>565.00 (n/a)</td><td>254.10 (n/a)</td><td>640.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>624.90 (n/a)</td><td>437.28 (n/a)</td><td>468.00 (n/a)</td><td>225.70 (n/a)</td><td>173.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1075.80 (n/a)</td><td>558.98 (n/a)</td><td>507.70 (n/a)</td><td>262.20 (n/a)</td><td>308.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.49 (-5.66%)</td><td>0.32 <b>(-26.07%)</b></td><td>0.34 <b>(-21.51%)</b></td><td>0.12 <b>(-62.31%)</b></td><td>0.13 <b>(+92.54%)</b></td><td>1787.80 <b>(+165.33%)</b></td><td>866.40 <b>(+63.50%)</b></td><td>654.70 <b>(+27.40%)</b></td><td>453.00 (+5.99%)</td><td>531.16 <b>(+480.40%)</b></td><td>20.83 (-5.66%)</td><td>13.46 <b>(-26.07%)</b></td><td>14.41 <b>(-21.51%)</b></td><td>5.28 <b>(-62.31%)</b></td><td>5.68 <b>(+92.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>673.80 (n/a)</td><td>529.92 (n/a)</td><td>513.90 (n/a)</td><td>427.40 (n/a)</td><td>91.52 (n/a)</td><td>22.08 (n/a)</td><td>18.21 (n/a)</td><td>18.36 (n/a)</td><td>14.01 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (+0.72%)</td><td>0.43 (+0.56%)</td><td>0.41 (-15.54%)</td><td>0.33 <b>(+39.72%)</b></td><td>0.10 <b>(-28.13%)</b></td><td>674.80 <b>(-28.43%)</b></td><td>536.80 (-6.76%)</td><td>546.10 (+18.41%)</td><td>379.10 (-0.71%)</td><td>109.52 <b>(-51.47%)</b></td><td>24.89 (+0.72%)</td><td>18.24 (+0.56%)</td><td>17.28 (-15.54%)</td><td>13.98 <b>(+39.72%)</b></td><td>4.14 <b>(-28.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.48 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>942.90 (n/a)</td><td>575.74 (n/a)</td><td>461.20 (n/a)</td><td>381.80 (n/a)</td><td>225.69 (n/a)</td><td>24.72 (n/a)</td><td>18.14 (n/a)</td><td>20.46 (n/a)</td><td>10.01 (n/a)</td><td>5.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 (+1.24%)</td><td>0.30 (+0.90%)</td><td>0.30 (+0.41%)</td><td>0.30 (+2.41%)</td><td>0.00 <b>(-31.54%)</b></td><td>84014.00 (-2.36%)</td><td>82622.50 (-0.90%)</td><td>82643.50 (-0.41%)</td><td>81238.70 (-1.22%)</td><td>1015.22 <b>(-34.13%)</b></td><td>211.47 (+1.24%)</td><td>207.96 (+0.90%)</td><td>207.88 (+0.41%)</td><td>204.49 (+2.41%)</td><td>2.56 <b>(-31.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86041.70 (n/a)</td><td>83376.92 (n/a)</td><td>82981.50 (n/a)</td><td>82244.10 (n/a)</td><td>1541.34 (n/a)</td><td>208.89 (n/a)</td><td>206.11 (n/a)</td><td>207.03 (n/a)</td><td>199.67 (n/a)</td><td>3.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.15 (-1.94%)</td><td>1.13 (-1.00%)</td><td>1.14 (-0.35%)</td><td>1.10 (-1.96%)</td><td>0.02 (+3.67%)</td><td>22909.20 (+2.00%)</td><td>22260.94 (+1.01%)</td><td>22028.70 (+0.35%)</td><td>21905.00 (+1.98%)</td><td>431.79 (+7.49%)</td><td>784.29 (-1.94%)</td><td>771.98 (-1.00%)</td><td>779.89 (-0.35%)</td><td>749.91 (-1.96%)</td><td>14.80 (+3.67%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>0.02 (n/a)</td><td>22459.90 (n/a)</td><td>22038.34 (n/a)</td><td>21951.50 (n/a)</td><td>21479.80 (n/a)</td><td>401.72 (n/a)</td><td>799.82 (n/a)</td><td>779.75 (n/a)</td><td>782.63 (n/a)</td><td>764.91 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.80 (+0.63%)</td><td>0.79 (+0.02%)</td><td>0.79 (+0.05%)</td><td>0.76 (-1.70%)</td><td>0.02 <b>(+78.84%)</b></td><td>99196.30 (+1.73%)</td><td>95509.78 (+0.01%)</td><td>95178.10 (-0.05%)</td><td>93801.90 (-0.62%)</td><td>2154.25 <b>(+80.90%)</b></td><td>732.60 (+0.63%)</td><td>719.79 (+0.02%)</td><td>722.01 (+0.05%)</td><td>692.76 (-1.70%)</td><td>15.86 <b>(+78.84%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97509.90 (n/a)</td><td>95498.30 (n/a)</td><td>95222.70 (n/a)</td><td>94390.60 (n/a)</td><td>1190.83 (n/a)</td><td>728.03 (n/a)</td><td>719.68 (n/a)</td><td>721.67 (n/a)</td><td>704.74 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.78 (-0.15%)</td><td>0.78 (+0.66%)</td><td>0.78 (+1.14%)</td><td>0.77 (+0.97%)</td><td>0.00 <b>(-38.73%)</b></td><td>98136.80 (-0.96%)</td><td>97292.54 (-0.66%)</td><td>97150.90 (-1.13%)</td><td>96662.50 (+0.15%)</td><td>594.82 <b>(-39.16%)</b></td><td>710.92 (-0.15%)</td><td>706.34 (+0.66%)</td><td>707.35 (+1.14%)</td><td>700.24 (+0.97%)</td><td>4.31 <b>(-38.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99090.50 (n/a)</td><td>97938.96 (n/a)</td><td>98257.00 (n/a)</td><td>96517.20 (n/a)</td><td>977.74 (n/a)</td><td>711.99 (n/a)</td><td>701.71 (n/a)</td><td>699.38 (n/a)</td><td>693.50 (n/a)</td><td>7.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.89 (-0.36%)</td><td>0.89 (+0.10%)</td><td>0.89 (-0.68%)</td><td>0.88 (+1.48%)</td><td>0.01 <b>(-50.89%)</b></td><td>85828.20 (-1.46%)</td><td>85034.56 (-0.11%)</td><td>85127.20 (+0.69%)</td><td>84368.50 (+0.36%)</td><td>586.37 <b>(-51.53%)</b></td><td>814.52 (-0.36%)</td><td>808.17 (+0.10%)</td><td>807.26 (-0.68%)</td><td>800.66 (+1.48%)</td><td>5.57 <b>(-50.89%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>87097.50 (n/a)</td><td>85126.94 (n/a)</td><td>84546.30 (n/a)</td><td>84065.00 (n/a)</td><td>1209.68 (n/a)</td><td>817.46 (n/a)</td><td>807.39 (n/a)</td><td>812.80 (n/a)</td><td>788.99 (n/a)</td><td>11.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>5.39 (-4.50%)</td><td>3.57 (-12.76%)</td><td>3.34 (-18.66%)</td><td>2.55 (+18.20%)</td><td>1.12 (-11.72%)</td><td>3488.50 (-15.40%)</td><td>2667.80 (+10.62%)</td><td>2672.40 <b>(+22.94%)</b></td><td>1652.70 (+4.71%)</td><td>709.88 <b>(-28.37%)</b></td><td>324.84 (-4.50%)</td><td>215.18 (-12.76%)</td><td>200.90 (-18.66%)</td><td>153.90 (+18.20%)</td><td>67.22 (-11.72%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.65 (n/a)</td><td>4.09 (n/a)</td><td>4.10 (n/a)</td><td>2.16 (n/a)</td><td>1.26 (n/a)</td><td>4123.40 (n/a)</td><td>2411.62 (n/a)</td><td>2173.80 (n/a)</td><td>1578.30 (n/a)</td><td>990.98 (n/a)</td><td>340.16 (n/a)</td><td>246.65 (n/a)</td><td>246.98 (n/a)</td><td>130.20 (n/a)</td><td>76.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.23 (-10.54%)</td><td>2.86 (+3.55%)</td><td>2.70 (+18.78%)</td><td>2.17 (-0.30%)</td><td>0.84 <b>(-23.90%)</b></td><td>4110.30 (+0.30%)</td><td>3310.34 (-6.20%)</td><td>3306.40 (-15.81%)</td><td>2105.80 (+11.78%)</td><td>829.22 (-11.67%)</td><td>254.95 (-10.54%)</td><td>172.15 (+3.55%)</td><td>162.37 (+18.78%)</td><td>130.62 (-0.30%)</td><td>50.78 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.73 (n/a)</td><td>2.76 (n/a)</td><td>2.27 (n/a)</td><td>2.17 (n/a)</td><td>1.11 (n/a)</td><td>4098.10 (n/a)</td><td>3529.30 (n/a)</td><td>3927.20 (n/a)</td><td>1883.80 (n/a)</td><td>938.72 (n/a)</td><td>284.99 (n/a)</td><td>166.24 (n/a)</td><td>136.71 (n/a)</td><td>131.00 (n/a)</td><td>66.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.29 <b>(-27.41%)</b></td><td>3.07 <b>(-29.14%)</b></td><td>2.67 <b>(-39.53%)</b></td><td>2.16 (-1.65%)</td><td>0.89 <b>(-34.09%)</b></td><td>4119.80 (+1.67%)</td><td>3095.60 <b>(+34.65%)</b></td><td>3341.40 <b>(+65.36%)</b></td><td>2076.10 <b>(+37.76%)</b></td><td>834.62 (-16.80%)</td><td>258.60 <b>(-27.41%)</b></td><td>184.79 <b>(-29.14%)</b></td><td>160.67 <b>(-39.53%)</b></td><td>130.31 (-1.65%)</td><td>53.42 <b>(-34.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.91 (n/a)</td><td>4.33 (n/a)</td><td>4.41 (n/a)</td><td>2.20 (n/a)</td><td>1.35 (n/a)</td><td>4052.00 (n/a)</td><td>2299.04 (n/a)</td><td>2020.70 (n/a)</td><td>1507.00 (n/a)</td><td>1003.16 (n/a)</td><td>356.25 (n/a)</td><td>260.79 (n/a)</td><td>265.69 (n/a)</td><td>132.49 (n/a)</td><td>81.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.72 (+1.24%)</td><td>5.55 (-5.38%)</td><td>5.32 (-14.87%)</td><td>4.53 (+2.15%)</td><td>0.95 (+8.00%)</td><td>7694.10 (-2.10%)</td><td>6427.04 (+5.91%)</td><td>6556.30 (+17.47%)</td><td>5190.80 (-1.23%)</td><td>1081.93 (+1.94%)</td><td>413.71 (+1.24%)</td><td>342.01 (-5.38%)</td><td>327.54 (-14.87%)</td><td>279.11 (+2.15%)</td><td>58.75 (+8.00%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.63 (n/a)</td><td>5.87 (n/a)</td><td>6.25 (n/a)</td><td>4.44 (n/a)</td><td>0.88 (n/a)</td><td>7859.30 (n/a)</td><td>6068.46 (n/a)</td><td>5581.20 (n/a)</td><td>5255.40 (n/a)</td><td>1061.33 (n/a)</td><td>408.62 (n/a)</td><td>361.45 (n/a)</td><td>384.77 (n/a)</td><td>273.24 (n/a)</td><td>54.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.31 (+17.31%)</td><td>4.65 (-3.42%)</td><td>4.29 (-17.45%)</td><td>3.82 (-4.82%)</td><td>1.00 <b>(+60.83%)</b></td><td>9120.90 (+5.06%)</td><td>7737.54 (+5.38%)</td><td>8122.20 <b>(+21.14%)</b></td><td>5522.20 (-14.76%)</td><td>1422.19 <b>(+42.00%)</b></td><td>388.88 (+17.31%)</td><td>286.52 (-3.42%)</td><td>264.40 (-17.45%)</td><td>235.45 (-4.82%)</td><td>61.63 <b>(+60.83%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.38 (n/a)</td><td>4.82 (n/a)</td><td>5.20 (n/a)</td><td>4.02 (n/a)</td><td>0.62 (n/a)</td><td>8681.30 (n/a)</td><td>7342.38 (n/a)</td><td>6704.70 (n/a)</td><td>6478.30 (n/a)</td><td>1001.56 (n/a)</td><td>331.49 (n/a)</td><td>296.65 (n/a)</td><td>320.29 (n/a)</td><td>247.37 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.92 (-2.97%)</td><td>5.79 (+3.93%)</td><td>6.11 (+3.76%)</td><td>3.99 (-8.09%)</td><td>1.12 (-5.62%)</td><td>8746.00 (+8.80%)</td><td>6249.26 (-3.84%)</td><td>5707.50 (-3.63%)</td><td>5040.00 (+3.06%)</td><td>1468.64 (+4.54%)</td><td>426.09 (-2.97%)</td><td>356.52 (+3.93%)</td><td>376.26 (+3.76%)</td><td>245.54 (-8.09%)</td><td>69.26 (-5.62%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.13 (n/a)</td><td>5.57 (n/a)</td><td>5.89 (n/a)</td><td>4.34 (n/a)</td><td>1.19 (n/a)</td><td>8038.40 (n/a)</td><td>6498.72 (n/a)</td><td>5922.30 (n/a)</td><td>4890.40 (n/a)</td><td>1404.83 (n/a)</td><td>439.12 (n/a)</td><td>343.03 (n/a)</td><td>362.61 (n/a)</td><td>267.15 (n/a)</td><td>73.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.79 (+1.96%)</td><td>0.76 (-0.16%)</td><td>0.76 (-0.27%)</td><td>0.74 (-0.72%)</td><td>0.02 <b>(+70.00%)</b></td><td>101878.00 (+0.72%)</td><td>98955.12 (+0.19%)</td><td>98850.60 (+0.27%)</td><td>95467.70 (-1.93%)</td><td>2387.87 <b>(+67.16%)</b></td><td>719.82 (+1.96%)</td><td>694.78 (-0.16%)</td><td>695.19 (-0.27%)</td><td>674.53 (-0.72%)</td><td>16.89 <b>(+70.00%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101149.40 (n/a)</td><td>98762.56 (n/a)</td><td>98587.00 (n/a)</td><td>97342.30 (n/a)</td><td>1428.45 (n/a)</td><td>705.96 (n/a)</td><td>695.92 (n/a)</td><td>697.04 (n/a)</td><td>679.39 (n/a)</td><td>9.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.78 (+2.84%)</td><td>0.76 (+1.60%)</td><td>0.76 (+1.68%)</td><td>0.75 (+1.22%)</td><td>0.01 <b>(+99.79%)</b></td><td>100033.00 (-1.21%)</td><td>98843.64 (-1.56%)</td><td>98908.80 (-1.65%)</td><td>96570.00 (-2.76%)</td><td>1392.32 <b>(+91.96%)</b></td><td>711.60 (+2.84%)</td><td>695.35 (+1.60%)</td><td>694.78 (+1.68%)</td><td>686.97 (+1.22%)</td><td>9.91 <b>(+99.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101255.00 (n/a)</td><td>100412.68 (n/a)</td><td>100573.10 (n/a)</td><td>99314.10 (n/a)</td><td>725.31 (n/a)</td><td>691.94 (n/a)</td><td>684.40 (n/a)</td><td>683.28 (n/a)</td><td>678.68 (n/a)</td><td>4.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.90 (+1.42%)</td><td>0.89 (+1.21%)</td><td>0.90 (+1.33%)</td><td>0.89 (+1.24%)</td><td>0.01 <b>(+21.72%)</b></td><td>85293.70 (-1.22%)</td><td>84452.20 (-1.19%)</td><td>84278.20 (-1.31%)</td><td>83502.30 (-1.40%)</td><td>799.71 (+18.76%)</td><td>822.96 (+1.42%)</td><td>813.77 (+1.21%)</td><td>815.39 (+1.33%)</td><td>805.68 (+1.24%)</td><td>7.70 <b>(+21.71%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86347.80 (n/a)</td><td>85471.28 (n/a)</td><td>85396.50 (n/a)</td><td>84684.10 (n/a)</td><td>673.41 (n/a)</td><td>811.48 (n/a)</td><td>804.05 (n/a)</td><td>804.71 (n/a)</td><td>795.84 (n/a)</td><td>6.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.16 (+3.72%)</td><td>2.55 (+12.78%)</td><td>2.27 (+11.29%)</td><td>1.55 (+10.96%)</td><td>0.97 (-5.43%)</td><td>5190.80 (-9.88%)</td><td>3505.38 (-13.80%)</td><td>3554.00 (-10.14%)</td><td>1939.90 (-3.58%)</td><td>1171.86 (-17.71%)</td><td>1089.72 (+3.72%)</td><td>667.49 (+12.78%)</td><td>594.80 (+11.29%)</td><td>407.24 (+10.96%)</td><td>255.64 (-5.43%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.01 (n/a)</td><td>2.26 (n/a)</td><td>2.04 (n/a)</td><td>1.40 (n/a)</td><td>1.03 (n/a)</td><td>5759.70 (n/a)</td><td>4066.62 (n/a)</td><td>3955.10 (n/a)</td><td>2012.00 (n/a)</td><td>1424.11 (n/a)</td><td>1050.68 (n/a)</td><td>591.83 (n/a)</td><td>534.48 (n/a)</td><td>367.02 (n/a)</td><td>270.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (+5.74%)</td><td>0.20 (-1.94%)</td><td>0.19 (+3.01%)</td><td>0.16 (-12.63%)</td><td>0.03 <b>(+26.66%)</b></td><td>7806.40 (+14.46%)</td><td>6376.14 (+2.79%)</td><td>6394.80 (-2.92%)</td><td>5113.80 (-5.43%)</td><td>977.12 <b>(+38.06%)</b></td><td>13.12 (+5.74%)</td><td>10.72 (-1.94%)</td><td>10.49 (+3.01%)</td><td>8.60 (-12.63%)</td><td>1.64 <b>(+26.66%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6820.40 (n/a)</td><td>6203.28 (n/a)</td><td>6587.00 (n/a)</td><td>5407.20 (n/a)</td><td>707.77 (n/a)</td><td>12.41 (n/a)</td><td>10.94 (n/a)</td><td>10.19 (n/a)</td><td>9.84 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.71 (n/a)</td><td>3.51 (n/a)</td><td>3.51 (n/a)</td><td>3.32 (n/a)</td><td>0.18 (n/a)</td><td>3.71 (n/a)</td><td>3.51 (n/a)</td><td>3.51 (n/a)</td><td>3.32 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.44 (-13.28%)</td><td>5.90 (-6.88%)</td><td>5.77 (-0.01%)</td><td>5.65 (+1.30%)</td><td>0.32 <b>(-64.07%)</b></td><td>6.43 (-13.28%)</td><td>5.90 (-6.88%)</td><td>5.77 (-0.01%)</td><td>5.65 (+1.30%)</td><td>0.32 <b>(-64.07%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.42 (n/a)</td><td>6.34 (n/a)</td><td>5.77 (n/a)</td><td>5.58 (n/a)</td><td>0.90 (n/a)</td><td>7.42 (n/a)</td><td>6.34 (n/a)</td><td>5.77 (n/a)</td><td>5.57 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>13.47 (+0.27%)</td><td>9.45 (-10.77%)</td><td>9.30 (-6.83%)</td><td>6.36 (-18.21%)</td><td>2.60 (-1.43%)</td><td>13.46 (+0.27%)</td><td>9.45 (-10.77%)</td><td>9.29 (-6.83%)</td><td>6.36 (-18.21%)</td><td>2.60 (-1.43%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>13.44 (n/a)</td><td>10.60 (n/a)</td><td>9.98 (n/a)</td><td>7.78 (n/a)</td><td>2.64 (n/a)</td><td>13.43 (n/a)</td><td>10.59 (n/a)</td><td>9.97 (n/a)</td><td>7.78 (n/a)</td><td>2.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.90 (n/a)</td><td>3.62 (n/a)</td><td>3.69 (n/a)</td><td>3.24 (n/a)</td><td>0.25 (n/a)</td><td>3.90 (n/a)</td><td>3.62 (n/a)</td><td>3.69 (n/a)</td><td>3.24 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.58 (+5.37%)</td><td>6.33 (+0.24%)</td><td>6.14 (-0.95%)</td><td>5.38 (-5.25%)</td><td>0.87 <b>(+32.59%)</b></td><td>7.57 (+5.37%)</td><td>6.32 (+0.24%)</td><td>6.13 (-0.95%)</td><td>5.38 (-5.25%)</td><td>0.87 <b>(+32.59%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.19 (n/a)</td><td>6.31 (n/a)</td><td>6.20 (n/a)</td><td>5.68 (n/a)</td><td>0.66 (n/a)</td><td>7.18 (n/a)</td><td>6.31 (n/a)</td><td>6.19 (n/a)</td><td>5.68 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>13.46 <b>(+59.00%)</b></td><td>11.06 <b>(+36.10%)</b></td><td>12.18 <b>(+48.85%)</b></td><td>8.27 (+7.20%)</td><td>2.53 <b>(+645.50%)</b></td><td>13.45 <b>(+59.00%)</b></td><td>11.05 <b>(+36.10%)</b></td><td>12.17 <b>(+48.85%)</b></td><td>8.26 (+7.20%)</td><td>2.52 <b>(+645.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>8.47 (n/a)</td><td>8.13 (n/a)</td><td>8.18 (n/a)</td><td>7.71 (n/a)</td><td>0.34 (n/a)</td><td>8.46 (n/a)</td><td>8.12 (n/a)</td><td>8.18 (n/a)</td><td>7.71 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.73 (-12.41%)</td><td>2.24 (+12.83%)</td><td>2.56 <b>(+50.94%)</b></td><td>1.18 (+18.45%)</td><td>0.66 <b>(-27.66%)</b></td><td>2.73 (-12.41%)</td><td>2.24 (+12.83%)</td><td>2.56 <b>(+50.94%)</b></td><td>1.18 (+18.45%)</td><td>0.66 <b>(-27.66%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.12 (n/a)</td><td>1.99 (n/a)</td><td>1.70 (n/a)</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td><td>3.11 (n/a)</td><td>1.98 (n/a)</td><td>1.70 (n/a)</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.46 (-11.95%)</td><td>0.29 (+18.01%)</td><td>0.33 <b>(+135.28%)</b></td><td>0.07 (-3.78%)</td><td>0.15 <b>(-23.54%)</b></td><td>0.45 (-11.95%)</td><td>0.29 (+18.01%)</td><td>0.33 <b>(+135.28%)</b></td><td>0.07 (-3.78%)</td><td>0.14 <b>(-23.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.52 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.51 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.49 <b>(-23.73%)</b></td><td>0.34 (-13.17%)</td><td>0.39 (-13.46%)</td><td>0.07 (-1.32%)</td><td>0.17 (-18.12%)</td><td>0.48 <b>(-23.73%)</b></td><td>0.34 (-13.17%)</td><td>0.38 (-13.46%)</td><td>0.07 (-1.32%)</td><td>0.17 (-18.12%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.64 (n/a)</td><td>0.39 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.63 (n/a)</td><td>0.39 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.25 <b>(+55.64%)</b></td><td>1.53 <b>(+101.22%)</b></td><td>1.60 <b>(+154.93%)</b></td><td>0.77 <b>(+81.94%)</b></td><td>0.60 <b>(+41.46%)</b></td><td>2.21 <b>(+55.64%)</b></td><td>1.51 <b>(+101.22%)</b></td><td>1.58 <b>(+154.93%)</b></td><td>0.76 <b>(+81.94%)</b></td><td>0.59 <b>(+41.46%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.44 (n/a)</td><td>0.76 (n/a)</td><td>0.63 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>1.42 (n/a)</td><td>0.75 (n/a)</td><td>0.62 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2520.40 (n/a)</td><td>1124.42 (n/a)</td><td>544.80 (n/a)</td><td>273.10 (n/a)</td><td>1061.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1972.20 (n/a)</td><td>747.52 (n/a)</td><td>616.40 (n/a)</td><td>216.00 (n/a)</td><td>712.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.50 (n/a)</td><td>496.20 (n/a)</td><td>477.00 (n/a)</td><td>434.40 (n/a)</td><td>60.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.50 (n/a)</td><td>440.76 (n/a)</td><td>465.60 (n/a)</td><td>273.60 (n/a)</td><td>114.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.90 (n/a)</td><td>476.56 (n/a)</td><td>553.30 (n/a)</td><td>161.90 (n/a)</td><td>176.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.20 (n/a)</td><td>479.84 (n/a)</td><td>499.70 (n/a)</td><td>280.80 (n/a)</td><td>139.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.10 (n/a)</td><td>338.64 (n/a)</td><td>276.10 (n/a)</td><td>231.60 (n/a)</td><td>109.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.00 (n/a)</td><td>469.50 (n/a)</td><td>504.20 (n/a)</td><td>348.80 (n/a)</td><td>114.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.00 (n/a)</td><td>494.38 (n/a)</td><td>516.20 (n/a)</td><td>351.80 (n/a)</td><td>89.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.20 (n/a)</td><td>473.70 (n/a)</td><td>471.30 (n/a)</td><td>262.60 (n/a)</td><td>134.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.90 (n/a)</td><td>454.86 (n/a)</td><td>472.90 (n/a)</td><td>279.00 (n/a)</td><td>111.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.20 (n/a)</td><td>525.88 (n/a)</td><td>548.40 (n/a)</td><td>387.80 (n/a)</td><td>100.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>669.90 (n/a)</td><td>458.94 (n/a)</td><td>502.50 (n/a)</td><td>207.30 (n/a)</td><td>192.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>418.70 (n/a)</td><td>314.26 (n/a)</td><td>291.30 (n/a)</td><td>231.10 (n/a)</td><td>82.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2451.50 (n/a)</td><td>849.10 (n/a)</td><td>470.10 (n/a)</td><td>329.40 (n/a)</td><td>899.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.80 (n/a)</td><td>450.54 (n/a)</td><td>507.50 (n/a)</td><td>207.10 (n/a)</td><td>140.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>554.80 (n/a)</td><td>432.34 (n/a)</td><td>489.40 (n/a)</td><td>240.20 (n/a)</td><td>130.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>613.30 (n/a)</td><td>481.66 (n/a)</td><td>515.40 (n/a)</td><td>279.20 (n/a)</td><td>134.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>666.40 (n/a)</td><td>478.30 (n/a)</td><td>628.70 (n/a)</td><td>217.90 (n/a)</td><td>228.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>541.20 (n/a)</td><td>475.94 (n/a)</td><td>515.90 (n/a)</td><td>299.00 (n/a)</td><td>99.78 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>536.60 (n/a)</td><td>334.88 (n/a)</td><td>298.40 (n/a)</td><td>262.10 (n/a)</td><td>114.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.20 (n/a)</td><td>468.64 (n/a)</td><td>525.20 (n/a)</td><td>301.30 (n/a)</td><td>121.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>558.70 (n/a)</td><td>427.74 (n/a)</td><td>435.80 (n/a)</td><td>286.30 (n/a)</td><td>100.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>601.70 (n/a)</td><td>431.58 (n/a)</td><td>432.20 (n/a)</td><td>285.20 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-12.80%)</td><td>0.01 (-11.42%)</td><td>0.01 (-15.42%)</td><td>0.01 <b>(+26.57%)</b></td><td>0.00 <b>(-57.40%)</b></td><td>332.00 <b>(-21.01%)</b></td><td>299.38 (+8.16%)</td><td>295.00 (+18.24%)</td><td>258.70 (+14.67%)</td><td>30.10 <b>(-62.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>420.30 (n/a)</td><td>276.80 (n/a)</td><td>249.50 (n/a)</td><td>225.60 (n/a)</td><td>80.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-0.10%)</td><td>0.01 (+11.71%)</td><td>0.01 (-8.76%)</td><td>0.01 <b>(+430.78%)</b></td><td>0.00 <b>(-46.82%)</b></td><td>464.20 <b>(-81.16%)</b></td><td>301.06 <b>(-57.14%)</b></td><td>281.20 (+9.63%)</td><td>238.10 (+0.13%)</td><td>93.86 <b>(-90.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2464.10 (n/a)</td><td>702.42 (n/a)</td><td>256.50 (n/a)</td><td>237.80 (n/a)</td><td>985.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(-28.47%)</b></td><td>0.01 (-7.82%)</td><td>0.01 <b>(+21.85%)</b></td><td>0.01 (+16.41%)</td><td>0.00 <b>(-52.08%)</b></td><td>438.40 (-14.09%)</td><td>361.70 (-4.91%)</td><td>362.30 (-17.94%)</td><td>229.10 <b>(+39.78%)</b></td><td>82.25 <b>(-45.27%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>510.30 (n/a)</td><td>380.38 (n/a)</td><td>441.50 (n/a)</td><td>163.90 (n/a)</td><td>150.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 <b>(-28.21%)</b></td><td>0.01 <b>(-20.82%)</b></td><td>0.01 <b>(-25.48%)</b></td><td>0.01 <b>(-30.18%)</b></td><td>0.00 <b>(-36.47%)</b></td><td>660.70 <b>(+43.23%)</b></td><td>414.18 <b>(+23.55%)</b></td><td>381.70 <b>(+34.21%)</b></td><td>276.90 <b>(+39.29%)</b></td><td>145.80 <b>(+24.00%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.30 (n/a)</td><td>335.22 (n/a)</td><td>284.40 (n/a)</td><td>198.80 (n/a)</td><td>117.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-1.95%)</td><td>0.01 (-17.55%)</td><td>0.01 (-10.09%)</td><td>0.01 <b>(-34.08%)</b></td><td>0.00 (+4.78%)</td><td>682.40 <b>(+51.71%)</b></td><td>452.12 <b>(+25.60%)</b></td><td>451.70 (+11.23%)</td><td>268.10 (+1.98%)</td><td>150.41 <b>(+67.68%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.80 (n/a)</td><td>359.98 (n/a)</td><td>406.10 (n/a)</td><td>262.90 (n/a)</td><td>89.70 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+33.80%)</b></td><td>0.01 (-11.41%)</td><td>0.01 <b>(-28.34%)</b></td><td>0.01 <b>(-25.33%)</b></td><td>0.01 <b>(+139.20%)</b></td><td>576.00 <b>(+33.92%)</b></td><td>413.98 <b>(+25.24%)</b></td><td>456.60 <b>(+39.55%)</b></td><td>200.70 <b>(-25.25%)</b></td><td>140.32 <b>(+123.04%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>430.10 (n/a)</td><td>330.54 (n/a)</td><td>327.20 (n/a)</td><td>268.50 (n/a)</td><td>62.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 <b>(-22.74%)</b></td><td>0.02 <b>(-31.18%)</b></td><td>0.03 (-17.41%)</td><td>0.01 <b>(-51.68%)</b></td><td>0.01 <b>(+38.00%)</b></td><td>630.00 <b>(+106.90%)</b></td><td>394.58 <b>(+65.89%)</b></td><td>294.80 <b>(+21.07%)</b></td><td>224.90 <b>(+29.40%)</b></td><td>184.04 <b>(+291.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.50 (n/a)</td><td>237.86 (n/a)</td><td>243.50 (n/a)</td><td>173.80 (n/a)</td><td>46.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(-25.33%)</b></td><td>0.02 (-11.97%)</td><td>0.02 (-12.93%)</td><td>0.01 (-11.99%)</td><td>0.01 <b>(-23.97%)</b></td><td>558.80 (+13.62%)</td><td>437.10 (+12.86%)</td><td>488.10 (+14.87%)</td><td>296.60 <b>(+33.97%)</b></td><td>123.71 (+18.19%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.80 (n/a)</td><td>387.30 (n/a)</td><td>424.90 (n/a)</td><td>221.40 (n/a)</td><td>104.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-1.87%)</td><td>0.03 (+9.05%)</td><td>0.03 (+8.69%)</td><td>0.02 (+3.56%)</td><td>0.01 (-3.29%)</td><td>525.70 (-3.43%)</td><td>336.68 (-9.20%)</td><td>288.00 (-7.99%)</td><td>240.70 (+1.91%)</td><td>118.36 (-8.18%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>370.80 (n/a)</td><td>313.00 (n/a)</td><td>236.20 (n/a)</td><td>128.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+2.07%)</td><td>0.02 (+8.41%)</td><td>0.02 (+0.59%)</td><td>0.01 <b>(+95.48%)</b></td><td>0.01 (-15.05%)</td><td>567.40 <b>(-48.85%)</b></td><td>448.28 <b>(-20.01%)</b></td><td>485.60 (-0.57%)</td><td>235.90 (-2.03%)</td><td>125.11 <b>(-61.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1109.20 (n/a)</td><td>560.42 (n/a)</td><td>488.40 (n/a)</td><td>240.80 (n/a)</td><td>326.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 <b>(+20.66%)</b></td><td>0.03 (+8.00%)</td><td>0.02 (+4.63%)</td><td>0.02 (+14.58%)</td><td>0.02 <b>(+22.28%)</b></td><td>495.40 (-12.72%)</td><td>353.34 (-5.81%)</td><td>374.60 (-4.44%)</td><td>150.40 (-17.13%)</td><td>149.34 (-8.39%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.60 (n/a)</td><td>375.14 (n/a)</td><td>392.00 (n/a)</td><td>181.50 (n/a)</td><td>163.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(-47.80%)</b></td><td>0.02 <b>(-27.80%)</b></td><td>0.02 (-17.94%)</td><td>0.01 <b>(+42.75%)</b></td><td>0.01 <b>(-68.25%)</b></td><td>553.10 <b>(-29.95%)</b></td><td>463.90 (+9.42%)</td><td>500.20 <b>(+21.88%)</b></td><td>302.40 <b>(+91.63%)</b></td><td>105.24 <b>(-56.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>789.60 (n/a)</td><td>423.96 (n/a)</td><td>410.40 (n/a)</td><td>157.80 (n/a)</td><td>239.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(-23.99%)</b></td><td>0.02 (-9.16%)</td><td>0.03 (+2.01%)</td><td>0.00 <b>(-57.48%)</b></td><td>0.01 (-13.91%)</td><td>1843.50 <b>(+135.17%)</b></td><td>636.52 <b>(+39.12%)</b></td><td>292.50 (-1.94%)</td><td>254.60 <b>(+31.58%)</b></td><td>682.85 <b>(+143.80%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>783.90 (n/a)</td><td>457.52 (n/a)</td><td>298.30 (n/a)</td><td>193.50 (n/a)</td><td>280.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+13.04%)</td><td>0.02 (+7.22%)</td><td>0.02 (+3.37%)</td><td>0.01 <b>(+37.97%)</b></td><td>0.01 (+6.15%)</td><td>754.50 <b>(-27.52%)</b></td><td>525.64 (-10.24%)</td><td>470.20 (-3.25%)</td><td>302.90 (-11.56%)</td><td>179.44 <b>(-34.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1041.00 (n/a)</td><td>585.60 (n/a)</td><td>486.00 (n/a)</td><td>342.50 (n/a)</td><td>272.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (-19.35%)</td><td>0.05 <b>(-27.84%)</b></td><td>0.05 <b>(-31.24%)</b></td><td>0.03 (-8.25%)</td><td>0.01 <b>(-22.81%)</b></td><td>548.90 (+9.00%)</td><td>385.12 <b>(+35.49%)</b></td><td>338.90 <b>(+45.45%)</b></td><td>270.80 <b>(+23.99%)</b></td><td>122.79 (-0.03%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>503.60 (n/a)</td><td>284.24 (n/a)</td><td>233.00 (n/a)</td><td>218.40 (n/a)</td><td>122.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 <b>(-40.11%)</b></td><td>0.04 <b>(-33.34%)</b></td><td>0.03 <b>(-48.10%)</b></td><td>0.03 (+18.17%)</td><td>0.01 <b>(-57.62%)</b></td><td>632.50 (-15.37%)</td><td>481.56 <b>(+25.27%)</b></td><td>525.40 <b>(+92.67%)</b></td><td>297.60 <b>(+67.00%)</b></td><td>129.84 <b>(-43.55%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>747.40 (n/a)</td><td>384.42 (n/a)</td><td>272.70 (n/a)</td><td>178.20 (n/a)</td><td>230.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 <b>(-23.35%)</b></td><td>0.04 (-9.87%)</td><td>0.04 (+10.21%)</td><td>0.03 (-2.20%)</td><td>0.01 <b>(-44.59%)</b></td><td>582.40 (+2.27%)</td><td>429.90 (+3.25%)</td><td>447.70 (-9.26%)</td><td>310.20 <b>(+30.45%)</b></td><td>109.03 <b>(-26.78%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.50 (n/a)</td><td>416.36 (n/a)</td><td>493.40 (n/a)</td><td>237.80 (n/a)</td><td>148.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (-0.08%)</td><td>0.03 (-17.81%)</td><td>0.03 (-18.48%)</td><td>0.02 <b>(-29.33%)</b></td><td>0.02 <b>(+25.77%)</b></td><td>748.40 <b>(+41.50%)</b></td><td>543.00 <b>(+29.88%)</b></td><td>556.20 <b>(+22.67%)</b></td><td>273.70 (+0.07%)</td><td>188.36 <b>(+74.80%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>418.08 (n/a)</td><td>453.40 (n/a)</td><td>273.50 (n/a)</td><td>107.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+9.70%)</td><td>0.04 (-3.75%)</td><td>0.04 (-3.06%)</td><td>0.01 <b>(-68.26%)</b></td><td>0.03 <b>(+48.88%)</b></td><td>2397.80 <b>(+215.04%)</b></td><td>815.68 <b>(+79.95%)</b></td><td>452.80 (+3.14%)</td><td>209.00 (-8.81%)</td><td>911.04 <b>(+335.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>761.10 (n/a)</td><td>453.28 (n/a)</td><td>439.00 (n/a)</td><td>229.20 (n/a)</td><td>209.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+19.00%)</td><td>0.05 <b>(+21.24%)</b></td><td>0.05 <b>(+51.43%)</b></td><td>0.02 <b>(-44.26%)</b></td><td>0.02 <b>(+66.65%)</b></td><td>1055.60 <b>(+79.40%)</b></td><td>454.60 (+4.14%)</td><td>303.90 <b>(-33.96%)</b></td><td>213.30 (-15.99%)</td><td>346.66 <b>(+178.03%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.40 (n/a)</td><td>436.54 (n/a)</td><td>460.20 (n/a)</td><td>253.90 (n/a)</td><td>124.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (+3.49%)</td><td>0.12 <b>(+30.10%)</b></td><td>0.12 <b>(+45.80%)</b></td><td>0.08 (+13.74%)</td><td>0.03 (-8.09%)</td><td>420.00 (-12.08%)</td><td>293.62 <b>(-24.26%)</b></td><td>279.30 <b>(-31.41%)</b></td><td>228.50 (-3.38%)</td><td>76.52 (-17.81%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>477.70 (n/a)</td><td>387.66 (n/a)</td><td>407.20 (n/a)</td><td>236.50 (n/a)</td><td>93.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (+5.47%)</td><td>0.11 (+13.04%)</td><td>0.11 (+2.46%)</td><td>0.09 <b>(+51.20%)</b></td><td>0.01 <b>(-39.44%)</b></td><td>351.10 <b>(-33.87%)</b></td><td>298.92 (-15.19%)</td><td>306.20 (-2.39%)</td><td>262.70 (-5.16%)</td><td>37.18 <b>(-64.08%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>530.90 (n/a)</td><td>352.44 (n/a)</td><td>313.70 (n/a)</td><td>277.00 (n/a)</td><td>103.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 <b>(-35.78%)</b></td><td>0.08 (-12.62%)</td><td>0.08 <b>(+23.73%)</b></td><td>0.06 (+0.97%)</td><td>0.01 <b>(-67.76%)</b></td><td>559.60 (-0.97%)</td><td>439.58 (+1.67%)</td><td>429.00 (-19.18%)</td><td>367.50 <b>(+55.72%)</b></td><td>77.55 <b>(-52.18%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>565.10 (n/a)</td><td>432.36 (n/a)</td><td>530.80 (n/a)</td><td>236.00 (n/a)</td><td>162.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (+4.72%)</td><td>0.09 (-15.83%)</td><td>0.07 <b>(-25.67%)</b></td><td>0.06 <b>(-21.31%)</b></td><td>0.04 (+14.72%)</td><td>593.40 <b>(+27.09%)</b></td><td>424.66 <b>(+23.53%)</b></td><td>448.30 <b>(+34.54%)</b></td><td>211.40 (-4.52%)</td><td>147.10 <b>(+31.19%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>466.90 (n/a)</td><td>343.78 (n/a)</td><td>333.20 (n/a)</td><td>221.40 (n/a)</td><td>112.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (-4.43%)</td><td>0.07 (-19.34%)</td><td>0.07 (-6.06%)</td><td>0.04 <b>(-29.84%)</b></td><td>0.03 (-1.71%)</td><td>775.30 <b>(+42.52%)</b></td><td>531.00 <b>(+28.22%)</b></td><td>495.90 (+6.46%)</td><td>298.60 (+4.66%)</td><td>186.71 <b>(+55.43%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.00 (n/a)</td><td>414.14 (n/a)</td><td>465.80 (n/a)</td><td>285.30 (n/a)</td><td>120.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-0.24%)</td><td>0.01 <b>(-22.51%)</b></td><td>0.01 <b>(-35.56%)</b></td><td>0.01 (-17.35%)</td><td>0.00 (+16.48%)</td><td>662.40 <b>(+21.01%)</b></td><td>444.42 <b>(+33.74%)</b></td><td>453.20 <b>(+55.21%)</b></td><td>229.40 (+0.26%)</td><td>158.61 <b>(+26.97%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.40 (n/a)</td><td>332.30 (n/a)</td><td>292.00 (n/a)</td><td>228.80 (n/a)</td><td>124.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+8.16%)</td><td>0.01 (+3.22%)</td><td>0.01 <b>(+26.48%)</b></td><td>0.01 <b>(-25.22%)</b></td><td>0.00 <b>(+53.59%)</b></td><td>598.60 <b>(+33.74%)</b></td><td>382.84 (+5.62%)</td><td>294.20 <b>(-20.94%)</b></td><td>225.90 (-7.57%)</td><td>159.31 <b>(+99.82%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>447.60 (n/a)</td><td>362.46 (n/a)</td><td>372.10 (n/a)</td><td>244.40 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-0.52%)</td><td>0.01 (-11.63%)</td><td>0.01 <b>(-42.01%)</b></td><td>0.01 <b>(+33.25%)</b></td><td>0.00 (-11.19%)</td><td>521.70 <b>(-24.95%)</b></td><td>415.12 (+7.30%)</td><td>514.10 <b>(+72.46%)</b></td><td>237.60 (+0.55%)</td><td>141.65 <b>(-27.26%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>695.10 (n/a)</td><td>386.88 (n/a)</td><td>298.10 (n/a)</td><td>236.30 (n/a)</td><td>194.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+9.43%)</td><td>0.01 (-9.22%)</td><td>0.01 (-12.85%)</td><td>0.01 <b>(-27.83%)</b></td><td>0.00 <b>(+191.08%)</b></td><td>442.30 <b>(+38.57%)</b></td><td>319.72 (+15.88%)</td><td>307.10 (+14.76%)</td><td>236.40 (-8.62%)</td><td>86.49 <b>(+253.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>319.20 (n/a)</td><td>275.90 (n/a)</td><td>267.60 (n/a)</td><td>258.70 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+2.07%)</td><td>0.01 <b>(+30.52%)</b></td><td>0.01 <b>(+33.66%)</b></td><td>0.01 <b>(+308.79%)</b></td><td>0.00 <b>(-36.84%)</b></td><td>464.80 <b>(-75.54%)</b></td><td>316.72 <b>(-51.77%)</b></td><td>294.00 <b>(-25.17%)</b></td><td>238.30 (-2.01%)</td><td>94.23 <b>(-86.55%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1900.10 (n/a)</td><td>656.64 (n/a)</td><td>392.90 (n/a)</td><td>243.20 (n/a)</td><td>700.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+0.48%)</td><td>0.01 (-15.94%)</td><td>0.01 <b>(-42.57%)</b></td><td>0.01 (+1.26%)</td><td>0.00 (-0.33%)</td><td>516.20 (-1.24%)</td><td>397.22 (+18.96%)</td><td>459.60 <b>(+74.16%)</b></td><td>238.10 (-0.46%)</td><td>121.66 (+0.00%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.70 (n/a)</td><td>333.90 (n/a)</td><td>263.90 (n/a)</td><td>239.20 (n/a)</td><td>121.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (-3.26%)</td><td>0.01 (-12.94%)</td><td>0.01 (-2.55%)</td><td>0.01 <b>(-37.18%)</b></td><td>0.00 <b>(+75.12%)</b></td><td>687.70 <b>(+59.19%)</b></td><td>406.74 <b>(+24.96%)</b></td><td>310.00 (+2.62%)</td><td>289.90 (+3.39%)</td><td>169.09 <b>(+176.08%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.00 (n/a)</td><td>325.50 (n/a)</td><td>302.10 (n/a)</td><td>280.40 (n/a)</td><td>61.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(-24.44%)</b></td><td>0.01 (-6.54%)</td><td>0.01 (-3.33%)</td><td>0.01 (+14.66%)</td><td>0.00 <b>(-37.39%)</b></td><td>473.30 (-12.79%)</td><td>385.36 (-1.47%)</td><td>462.60 (+3.44%)</td><td>235.70 <b>(+32.34%)</b></td><td>114.87 <b>(-24.23%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>391.10 (n/a)</td><td>447.20 (n/a)</td><td>178.10 (n/a)</td><td>151.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-16.59%)</td><td>0.01 (+13.61%)</td><td>0.01 <b>(+59.62%)</b></td><td>0.01 (+4.21%)</td><td>0.00 <b>(-25.34%)</b></td><td>614.00 (-4.03%)</td><td>399.94 (-15.81%)</td><td>313.40 <b>(-37.36%)</b></td><td>244.60 (+19.84%)</td><td>160.04 (-5.76%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.80 (n/a)</td><td>475.04 (n/a)</td><td>500.30 (n/a)</td><td>204.10 (n/a)</td><td>169.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+85.05%)</b></td><td>0.01 <b>(+44.88%)</b></td><td>0.01 (+4.93%)</td><td>0.01 <b>(+26.25%)</b></td><td>0.00 <b>(+308.93%)</b></td><td>479.80 <b>(-20.80%)</b></td><td>378.78 <b>(-24.25%)</b></td><td>454.60 (-4.70%)</td><td>229.50 <b>(-45.96%)</b></td><td>127.14 <b>(+77.42%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.80 (n/a)</td><td>500.06 (n/a)</td><td>477.00 (n/a)</td><td>424.70 (n/a)</td><td>71.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+35.87%)</b></td><td>0.01 (+9.78%)</td><td>0.01 (-9.56%)</td><td>0.01 (-3.00%)</td><td>0.00 <b>(+67.73%)</b></td><td>574.00 (+3.09%)</td><td>410.52 (-4.84%)</td><td>428.00 (+10.57%)</td><td>249.80 <b>(-26.40%)</b></td><td>128.70 <b>(+25.07%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.80 (n/a)</td><td>431.40 (n/a)</td><td>387.10 (n/a)</td><td>339.40 (n/a)</td><td>102.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (+10.74%)</td><td>0.01 (-14.01%)</td><td>0.01 <b>(-21.64%)</b></td><td>0.01 <b>(-29.91%)</b></td><td>0.00 <b>(+78.90%)</b></td><td>617.10 <b>(+42.68%)</b></td><td>450.06 <b>(+22.45%)</b></td><td>438.70 <b>(+27.60%)</b></td><td>283.70 (-9.71%)</td><td>127.30 <b>(+125.37%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.50 (n/a)</td><td>367.54 (n/a)</td><td>343.80 (n/a)</td><td>314.20 (n/a)</td><td>56.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-1.25%)</td><td>0.03 (+6.80%)</td><td>0.03 (+1.80%)</td><td>0.02 (+17.83%)</td><td>0.00 <b>(-30.48%)</b></td><td>452.30 (-15.14%)</td><td>323.66 (-10.19%)</td><td>301.50 (-1.76%)</td><td>264.20 (+1.26%)</td><td>74.15 <b>(-36.75%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.00 (n/a)</td><td>360.40 (n/a)</td><td>306.90 (n/a)</td><td>260.90 (n/a)</td><td>117.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-7.57%)</td><td>0.02 (-18.61%)</td><td>0.02 (-17.48%)</td><td>0.00 <b>(-77.97%)</b></td><td>0.01 <b>(+62.44%)</b></td><td>2023.40 <b>(+353.88%)</b></td><td>699.84 <b>(+95.55%)</b></td><td>451.70 <b>(+21.16%)</b></td><td>267.90 (+8.20%)</td><td>745.03 <b>(+749.45%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.80 (n/a)</td><td>357.88 (n/a)</td><td>372.80 (n/a)</td><td>247.60 (n/a)</td><td>87.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 <b>(+40.57%)</b></td><td>0.02 (+12.75%)</td><td>0.02 <b>(-21.52%)</b></td><td>0.01 <b>(+30.36%)</b></td><td>0.01 <b>(+55.06%)</b></td><td>568.80 <b>(-23.29%)</b></td><td>426.16 (-8.37%)</td><td>474.50 <b>(+27.42%)</b></td><td>203.10 <b>(-28.86%)</b></td><td>156.67 (-15.86%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>741.50 (n/a)</td><td>465.08 (n/a)</td><td>372.40 (n/a)</td><td>285.50 (n/a)</td><td>186.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+9.99%)</td><td>0.02 (+18.81%)</td><td>0.03 <b>(+51.61%)</b></td><td>0.01 (+10.72%)</td><td>0.01 (-5.89%)</td><td>613.30 (-9.69%)</td><td>361.64 (-17.33%)</td><td>301.80 <b>(-34.05%)</b></td><td>255.00 (-9.09%)</td><td>145.02 (-12.16%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.10 (n/a)</td><td>437.44 (n/a)</td><td>457.60 (n/a)</td><td>280.50 (n/a)</td><td>165.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+15.72%)</td><td>0.02 (+3.74%)</td><td>0.02 (-18.79%)</td><td>0.01 (+1.09%)</td><td>0.01 <b>(+25.48%)</b></td><td>623.70 (-1.06%)</td><td>420.44 (-1.18%)</td><td>421.20 <b>(+23.16%)</b></td><td>244.20 (-13.56%)</td><td>156.14 (+3.38%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.40 (n/a)</td><td>425.48 (n/a)</td><td>342.00 (n/a)</td><td>282.50 (n/a)</td><td>151.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(+38.56%)</b></td><td>0.03 <b>(+56.71%)</b></td><td>0.03 <b>(+82.27%)</b></td><td>0.02 (+13.07%)</td><td>0.01 <b>(+89.63%)</b></td><td>523.60 (-11.57%)</td><td>316.16 <b>(-32.92%)</b></td><td>242.50 <b>(-45.14%)</b></td><td>238.00 <b>(-27.84%)</b></td><td>123.38 (+15.38%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.10 (n/a)</td><td>471.34 (n/a)</td><td>442.00 (n/a)</td><td>329.80 (n/a)</td><td>106.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-10.75%)</td><td>0.02 (+6.18%)</td><td>0.02 (+18.14%)</td><td>0.02 (+7.33%)</td><td>0.01 <b>(-23.82%)</b></td><td>495.10 (-6.83%)</td><td>397.40 (-8.44%)</td><td>402.80 (-15.36%)</td><td>263.40 (+12.04%)</td><td>100.67 (-12.54%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>434.02 (n/a)</td><td>475.90 (n/a)</td><td>235.10 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 <b>(+29.10%)</b></td><td>0.02 (-0.45%)</td><td>0.02 <b>(-23.21%)</b></td><td>0.01 (-10.97%)</td><td>0.01 <b>(+58.60%)</b></td><td>552.40 (+12.32%)</td><td>396.42 (+6.77%)</td><td>403.20 <b>(+30.19%)</b></td><td>219.70 <b>(-22.53%)</b></td><td>141.30 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.80 (n/a)</td><td>371.30 (n/a)</td><td>309.70 (n/a)</td><td>283.60 (n/a)</td><td>102.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+17.97%)</td><td>0.02 (+6.47%)</td><td>0.03 <b>(+21.35%)</b></td><td>0.00 <b>(-69.84%)</b></td><td>0.01 <b>(+97.75%)</b></td><td>1884.00 <b>(+231.57%)</b></td><td>617.90 <b>(+54.13%)</b></td><td>292.90 (-17.59%)</td><td>246.60 (-15.23%)</td><td>709.41 <b>(+513.01%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.20 (n/a)</td><td>400.90 (n/a)</td><td>355.40 (n/a)</td><td>290.90 (n/a)</td><td>115.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-5.02%)</td><td>0.02 (-4.11%)</td><td>0.03 (+5.22%)</td><td>0.01 <b>(-30.95%)</b></td><td>0.01 <b>(+25.12%)</b></td><td>663.50 <b>(+44.84%)</b></td><td>377.24 (+12.22%)</td><td>270.80 (-4.95%)</td><td>252.10 (+5.30%)</td><td>175.68 <b>(+80.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.10 (n/a)</td><td>336.16 (n/a)</td><td>284.90 (n/a)</td><td>239.40 (n/a)</td><td>97.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+9.01%)</td><td>0.02 (+3.32%)</td><td>0.01 <b>(-25.94%)</b></td><td>0.01 <b>(+177.95%)</b></td><td>0.01 (-18.68%)</td><td>704.70 <b>(-64.02%)</b></td><td>487.52 <b>(-32.77%)</b></td><td>553.10 <b>(+35.03%)</b></td><td>247.10 (-8.24%)</td><td>177.43 <b>(-74.92%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1958.80 (n/a)</td><td>725.12 (n/a)</td><td>409.60 (n/a)</td><td>269.30 (n/a)</td><td>707.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-8.45%)</td><td>0.02 (-17.76%)</td><td>0.01 <b>(-23.30%)</b></td><td>0.01 <b>(+44.33%)</b></td><td>0.01 <b>(-30.38%)</b></td><td>708.50 <b>(-30.71%)</b></td><td>571.60 (+4.31%)</td><td>645.20 <b>(+30.37%)</b></td><td>281.60 (+9.23%)</td><td>172.28 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1022.50 (n/a)</td><td>547.96 (n/a)</td><td>494.90 (n/a)</td><td>257.80 (n/a)</td><td>318.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+1.15%)</td><td>0.04 (-18.36%)</td><td>0.04 <b>(-34.33%)</b></td><td>0.01 <b>(-64.91%)</b></td><td>0.02 <b>(+77.65%)</b></td><td>1356.50 <b>(+184.98%)</b></td><td>547.32 <b>(+69.22%)</b></td><td>443.30 <b>(+52.28%)</b></td><td>245.90 (-1.17%)</td><td>462.91 <b>(+395.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>323.44 (n/a)</td><td>291.10 (n/a)</td><td>248.80 (n/a)</td><td>93.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+16.07%)</td><td>0.06 <b>(+46.37%)</b></td><td>0.07 <b>(+93.59%)</b></td><td>0.04 <b>(+30.48%)</b></td><td>0.02 (+19.20%)</td><td>416.30 <b>(-23.36%)</b></td><td>303.82 <b>(-31.64%)</b></td><td>245.90 <b>(-48.35%)</b></td><td>229.10 (-13.84%)</td><td>88.64 (-15.83%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>543.20 (n/a)</td><td>444.42 (n/a)</td><td>476.10 (n/a)</td><td>265.90 (n/a)</td><td>105.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+4.20%)</td><td>0.06 <b>(+46.12%)</b></td><td>0.06 <b>(+107.69%)</b></td><td>0.03 <b>(+313.21%)</b></td><td>0.01 <b>(-40.74%)</b></td><td>507.70 <b>(-75.80%)</b></td><td>312.20 <b>(-58.17%)</b></td><td>258.60 <b>(-51.85%)</b></td><td>246.00 (-4.06%)</td><td>111.44 <b>(-85.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2097.80 (n/a)</td><td>746.36 (n/a)</td><td>537.10 (n/a)</td><td>256.40 (n/a)</td><td>770.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 <b>(+35.76%)</b></td><td>0.06 <b>(+28.75%)</b></td><td>0.07 <b>(+44.14%)</b></td><td>0.03 (+12.56%)</td><td>0.02 <b>(+75.61%)</b></td><td>535.90 (-11.17%)</td><td>326.42 (-17.21%)</td><td>233.70 <b>(-30.61%)</b></td><td>219.60 <b>(-26.33%)</b></td><td>143.28 (+11.58%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>394.26 (n/a)</td><td>336.80 (n/a)</td><td>298.10 (n/a)</td><td>128.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+10.99%)</td><td>0.05 (+11.48%)</td><td>0.06 <b>(+50.94%)</b></td><td>0.03 (-9.11%)</td><td>0.02 <b>(+30.71%)</b></td><td>565.60 (+10.02%)</td><td>359.66 (-4.95%)</td><td>273.40 <b>(-33.75%)</b></td><td>227.60 (-9.90%)</td><td>155.35 <b>(+36.14%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.10 (n/a)</td><td>378.38 (n/a)</td><td>412.70 (n/a)</td><td>252.60 (n/a)</td><td>114.11 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+16.23%)</td><td>0.06 <b>(+43.64%)</b></td><td>0.07 <b>(+80.25%)</b></td><td>0.04 <b>(+43.65%)</b></td><td>0.01 (-14.30%)</td><td>409.90 <b>(-30.38%)</b></td><td>289.98 <b>(-33.76%)</b></td><td>247.20 <b>(-44.52%)</b></td><td>242.80 (-13.96%)</td><td>71.51 <b>(-49.26%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.80 (n/a)</td><td>437.76 (n/a)</td><td>445.60 (n/a)</td><td>282.20 (n/a)</td><td>140.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 <b>(+34.37%)</b></td><td>0.06 <b>(+48.39%)</b></td><td>0.07 <b>(+112.64%)</b></td><td>0.04 <b>(+38.64%)</b></td><td>0.02 (+7.48%)</td><td>437.50 <b>(-27.86%)</b></td><td>297.64 <b>(-35.51%)</b></td><td>251.00 <b>(-52.98%)</b></td><td>202.20 <b>(-25.61%)</b></td><td>95.05 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.50 (n/a)</td><td>461.50 (n/a)</td><td>533.80 (n/a)</td><td>271.80 (n/a)</td><td>162.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+17.48%)</td><td>0.05 <b>(+28.80%)</b></td><td>0.04 (+19.90%)</td><td>0.04 <b>(+41.83%)</b></td><td>0.01 (-0.30%)</td><td>436.60 <b>(-29.49%)</b></td><td>349.04 <b>(-24.81%)</b></td><td>370.00 (-16.59%)</td><td>236.50 (-14.90%)</td><td>81.09 <b>(-41.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>619.20 (n/a)</td><td>464.18 (n/a)</td><td>443.60 (n/a)</td><td>277.90 (n/a)</td><td>137.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 <b>(-20.81%)</b></td><td>0.04 <b>(-26.68%)</b></td><td>0.03 <b>(-41.64%)</b></td><td>0.02 (-10.43%)</td><td>0.02 (-19.88%)</td><td>693.90 (+11.65%)</td><td>491.60 <b>(+34.85%)</b></td><td>502.80 <b>(+71.31%)</b></td><td>273.00 <b>(+26.27%)</b></td><td>182.58 (+11.97%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.50 (n/a)</td><td>364.56 (n/a)</td><td>293.50 (n/a)</td><td>216.20 (n/a)</td><td>163.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+13.37%)</td><td>0.06 <b>(+26.35%)</b></td><td>0.06 <b>(+33.86%)</b></td><td>0.04 (+16.74%)</td><td>0.01 (-0.81%)</td><td>458.90 (-14.35%)</td><td>310.26 <b>(-22.07%)</b></td><td>285.80 <b>(-25.28%)</b></td><td>243.80 (-11.79%)</td><td>86.73 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>535.80 (n/a)</td><td>398.12 (n/a)</td><td>382.50 (n/a)</td><td>276.40 (n/a)</td><td>113.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (-13.94%)</td><td>0.03 (-19.73%)</td><td>0.03 <b>(-23.08%)</b></td><td>0.03 (-16.78%)</td><td>0.01 (-2.82%)</td><td>610.80 <b>(+20.17%)</b></td><td>516.48 <b>(+25.63%)</b></td><td>551.30 <b>(+30.02%)</b></td><td>380.80 (+16.17%)</td><td>99.27 <b>(+38.64%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>508.30 (n/a)</td><td>411.10 (n/a)</td><td>424.00 (n/a)</td><td>327.80 (n/a)</td><td>71.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 <b>(+27.29%)</b></td><td>0.05 <b>(+46.42%)</b></td><td>0.06 <b>(+96.45%)</b></td><td>0.01 <b>(-64.56%)</b></td><td>0.02 <b>(+95.84%)</b></td><td>1761.60 <b>(+182.17%)</b></td><td>572.46 (+10.99%)</td><td>285.90 <b>(-49.09%)</b></td><td>231.10 <b>(-21.45%)</b></td><td>665.76 <b>(+382.31%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>624.30 (n/a)</td><td>515.78 (n/a)</td><td>561.60 (n/a)</td><td>294.20 (n/a)</td><td>138.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 <b>(+90.52%)</b></td><td>0.09 <b>(+43.36%)</b></td><td>0.07 (+13.93%)</td><td>0.07 (+19.51%)</td><td>0.03 <b>(+478.66%)</b></td><td>487.00 (-16.32%)</td><td>381.42 <b>(-24.40%)</b></td><td>439.50 (-12.22%)</td><td>245.90 <b>(-47.50%)</b></td><td>116.31 <b>(+151.96%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>582.00 (n/a)</td><td>504.50 (n/a)</td><td>500.70 (n/a)</td><td>468.40 (n/a)</td><td>46.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 <b>(-34.90%)</b></td><td>0.08 <b>(-20.07%)</b></td><td>0.08 (-13.45%)</td><td>0.06 (-7.57%)</td><td>0.02 <b>(-57.13%)</b></td><td>589.60 (+8.20%)</td><td>440.74 (+14.95%)</td><td>431.30 (+15.54%)</td><td>320.30 <b>(+53.62%)</b></td><td>98.65 <b>(-30.04%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>544.90 (n/a)</td><td>383.42 (n/a)</td><td>373.30 (n/a)</td><td>208.50 (n/a)</td><td>141.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (+0.22%)</td><td>0.08 (+0.57%)</td><td>0.11 <b>(+56.91%)</b></td><td>0.01 <b>(-76.55%)</b></td><td>0.04 <b>(+45.98%)</b></td><td>2501.10 <b>(+326.52%)</b></td><td>769.72 <b>(+77.33%)</b></td><td>304.70 <b>(-36.28%)</b></td><td>273.90 (-0.22%)</td><td>970.81 <b>(+581.74%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>586.40 (n/a)</td><td>434.06 (n/a)</td><td>478.20 (n/a)</td><td>274.50 (n/a)</td><td>142.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (+12.47%)</td><td>0.09 (-1.14%)</td><td>0.07 <b>(-26.47%)</b></td><td>0.06 (-6.68%)</td><td>0.03 <b>(+39.02%)</b></td><td>548.40 (+7.15%)</td><td>393.60 (+5.58%)</td><td>450.70 <b>(+36.00%)</b></td><td>237.00 (-11.10%)</td><td>131.84 <b>(+26.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>511.80 (n/a)</td><td>372.80 (n/a)</td><td>331.40 (n/a)</td><td>266.60 (n/a)</td><td>104.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (+17.52%)</td><td>0.12 <b>(+24.99%)</b></td><td>0.14 <b>(+79.82%)</b></td><td>0.06 (-5.49%)</td><td>0.04 <b>(+36.50%)</b></td><td>551.50 (+5.81%)</td><td>323.46 (-15.69%)</td><td>229.90 <b>(-44.40%)</b></td><td>219.80 (-14.91%)</td><td>146.15 <b>(+23.80%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>521.20 (n/a)</td><td>383.66 (n/a)</td><td>413.50 (n/a)</td><td>258.30 (n/a)</td><td>118.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (+1.68%)</td><td>0.09 (+11.62%)</td><td>0.13 <b>(+102.92%)</b></td><td>0.02 <b>(-71.36%)</b></td><td>0.05 <b>(+39.53%)</b></td><td>2006.10 <b>(+249.19%)</b></td><td>645.04 <b>(+46.14%)</b></td><td>261.40 <b>(-50.72%)</b></td><td>251.70 (-1.64%)</td><td>765.37 <b>(+374.60%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>574.50 (n/a)</td><td>441.38 (n/a)</td><td>530.40 (n/a)</td><td>255.90 (n/a)</td><td>161.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 <b>(+24.32%)</b></td><td>0.11 (+19.17%)</td><td>0.13 <b>(+23.79%)</b></td><td>0.05 (+5.96%)</td><td>0.04 <b>(+33.37%)</b></td><td>631.80 (-5.63%)</td><td>362.52 (-12.57%)</td><td>254.90 (-19.23%)</td><td>219.00 (-19.57%)</td><td>179.45 (+1.95%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>669.50 (n/a)</td><td>414.66 (n/a)</td><td>315.60 (n/a)</td><td>272.30 (n/a)</td><td>176.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (+5.58%)</td><td>0.09 (-6.10%)</td><td>0.09 (-10.79%)</td><td>0.05 (-19.86%)</td><td>0.04 <b>(+52.12%)</b></td><td>617.90 <b>(+24.78%)</b></td><td>396.04 (+14.65%)</td><td>371.70 (+12.09%)</td><td>249.80 (-5.31%)</td><td>157.40 <b>(+70.14%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>495.20 (n/a)</td><td>345.44 (n/a)</td><td>331.60 (n/a)</td><td>263.80 (n/a)</td><td>92.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (+15.21%)</td><td>0.07 (-11.37%)</td><td>0.06 <b>(-23.45%)</b></td><td>0.01 <b>(-77.63%)</b></td><td>0.05 <b>(+88.52%)</b></td><td>2467.10 <b>(+347.10%)</b></td><td>836.44 <b>(+95.59%)</b></td><td>558.90 <b>(+30.65%)</b></td><td>253.50 (-13.18%)</td><td>924.31 <b>(+649.34%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>551.80 (n/a)</td><td>427.66 (n/a)</td><td>427.80 (n/a)</td><td>292.00 (n/a)</td><td>123.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 <b>(+26.07%)</b></td><td>0.10 (+15.71%)</td><td>0.08 (+19.02%)</td><td>0.07 <b>(+44.15%)</b></td><td>0.04 (+14.29%)</td><td>465.60 <b>(-30.62%)</b></td><td>370.06 (-16.80%)</td><td>387.70 (-15.99%)</td><td>192.20 <b>(-20.68%)</b></td><td>109.44 <b>(-37.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>671.10 (n/a)</td><td>444.78 (n/a)</td><td>461.50 (n/a)</td><td>242.30 (n/a)</td><td>176.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 <b>(+56.55%)</b></td><td>0.09 <b>(+80.79%)</b></td><td>0.10 <b>(+46.86%)</b></td><td>0.07 <b>(+282.05%)</b></td><td>0.02 <b>(-25.35%)</b></td><td>488.70 <b>(-73.82%)</b></td><td>360.80 <b>(-58.34%)</b></td><td>337.80 <b>(-31.91%)</b></td><td>278.80 <b>(-36.11%)</b></td><td>82.63 <b>(-86.66%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1866.90 (n/a)</td><td>866.12 (n/a)</td><td>496.10 (n/a)</td><td>436.40 (n/a)</td><td>619.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (-14.99%)</td><td>0.08 <b>(-20.91%)</b></td><td>0.11 (+9.79%)</td><td>0.02 <b>(-64.27%)</b></td><td>0.05 <b>(+31.75%)</b></td><td>2022.70 <b>(+179.88%)</b></td><td>787.28 <b>(+102.65%)</b></td><td>307.40 (-8.92%)</td><td>262.80 (+17.64%)</td><td>766.28 <b>(+288.38%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>722.70 (n/a)</td><td>388.50 (n/a)</td><td>337.50 (n/a)</td><td>223.40 (n/a)</td><td>197.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (+7.82%)</td><td>0.08 (-17.07%)</td><td>0.07 <b>(-26.26%)</b></td><td>0.06 <b>(-30.70%)</b></td><td>0.03 <b>(+137.73%)</b></td><td>420.30 <b>(+44.28%)</b></td><td>327.04 <b>(+27.86%)</b></td><td>344.00 <b>(+35.65%)</b></td><td>204.10 (-7.27%)</td><td>87.71 <b>(+216.57%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>291.30 (n/a)</td><td>255.78 (n/a)</td><td>253.60 (n/a)</td><td>220.10 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 <b>(+20.15%)</b></td><td>0.13 (-16.32%)</td><td>0.12 <b>(-23.66%)</b></td><td>0.02 <b>(-79.03%)</b></td><td>0.08 <b>(+85.66%)</b></td><td>2161.00 <b>(+376.83%)</b></td><td>710.78 <b>(+109.63%)</b></td><td>406.20 <b>(+30.99%)</b></td><td>205.80 (-16.78%)</td><td>817.20 <b>(+736.58%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>453.20 (n/a)</td><td>339.06 (n/a)</td><td>310.10 (n/a)</td><td>247.30 (n/a)</td><td>97.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.19 (-2.38%)</td><td>3.46 (-3.68%)</td><td>3.64 (+0.76%)</td><td>2.01 <b>(-23.43%)</b></td><td>0.84 (+18.80%)</td><td>5226.30 <b>(+30.59%)</b></td><td>3246.62 (+7.50%)</td><td>2883.90 (-0.75%)</td><td>2504.30 (+2.44%)</td><td>1118.01 <b>(+72.39%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.29 (n/a)</td><td>3.59 (n/a)</td><td>3.61 (n/a)</td><td>2.62 (n/a)</td><td>0.71 (n/a)</td><td>4002.00 (n/a)</td><td>3020.24 (n/a)</td><td>2905.80 (n/a)</td><td>2444.60 (n/a)</td><td>648.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (-0.28%)</td><td>0.12 (+5.08%)</td><td>0.14 (+11.40%)</td><td>0.05 <b>(-27.12%)</b></td><td>0.05 (+17.33%)</td><td>772.70 <b>(+37.22%)</b></td><td>401.92 (+2.51%)</td><td>288.60 (-10.23%)</td><td>240.80 (+0.25%)</td><td>223.32 <b>(+49.80%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>563.10 (n/a)</td><td>392.06 (n/a)</td><td>321.50 (n/a)</td><td>240.20 (n/a)</td><td>149.08 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+8.57%)</td><td>0.02 (-6.58%)</td><td>0.02 (+1.96%)</td><td>0.01 <b>(-36.97%)</b></td><td>0.00 <b>(+190.68%)</b></td><td>549.10 <b>(+58.65%)</b></td><td>354.04 (+14.29%)</td><td>308.20 (-1.91%)</td><td>253.10 (-7.90%)</td><td>116.91 <b>(+341.72%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>346.10 (n/a)</td><td>309.76 (n/a)</td><td>314.20 (n/a)</td><td>274.80 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+33.02%)</b></td><td>0.02 <b>(+62.68%)</b></td><td>0.02 <b>(+87.68%)</b></td><td>0.01 <b>(+267.86%)</b></td><td>0.01 (-13.65%)</td><td>467.40 <b>(-72.82%)</b></td><td>267.84 <b>(-57.74%)</b></td><td>237.10 <b>(-46.72%)</b></td><td>187.00 <b>(-24.84%)</b></td><td>114.10 <b>(-81.51%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1719.50 (n/a)</td><td>633.74 (n/a)</td><td>445.00 (n/a)</td><td>248.80 (n/a)</td><td>616.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+5.28%)</td><td>0.02 (+7.16%)</td><td>0.01 (+10.19%)</td><td>0.00 <b>(-71.17%)</b></td><td>0.01 <b>(+50.72%)</b></td><td>1919.00 <b>(+246.83%)</b></td><td>664.10 <b>(+49.37%)</b></td><td>413.40 (-9.24%)</td><td>217.20 (-4.99%)</td><td>711.50 <b>(+446.24%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>444.60 (n/a)</td><td>455.50 (n/a)</td><td>228.60 (n/a)</td><td>130.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+0.20%)</td><td>0.01 <b>(+33.26%)</b></td><td>0.02 <b>(+65.35%)</b></td><td>0.01 <b>(+20.23%)</b></td><td>0.00 <b>(-28.56%)</b></td><td>387.70 (-16.82%)</td><td>286.12 <b>(-27.85%)</b></td><td>267.60 <b>(-39.51%)</b></td><td>228.20 (-0.17%)</td><td>61.56 <b>(-37.93%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.10 (n/a)</td><td>396.58 (n/a)</td><td>442.40 (n/a)</td><td>228.60 (n/a)</td><td>99.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (+8.95%)</td><td>0.02 <b>(+27.43%)</b></td><td>0.02 <b>(+46.11%)</b></td><td>0.01 <b>(+308.17%)</b></td><td>0.01 <b>(-28.05%)</b></td><td>607.70 <b>(-75.50%)</b></td><td>375.46 <b>(-55.85%)</b></td><td>314.30 <b>(-31.57%)</b></td><td>218.30 (-8.20%)</td><td>163.85 <b>(-82.61%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2480.40 (n/a)</td><td>850.34 (n/a)</td><td>459.30 (n/a)</td><td>237.80 (n/a)</td><td>942.35 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+21.37%)</b></td><td>0.01 (-9.17%)</td><td>0.01 (-8.30%)</td><td>0.01 <b>(-51.33%)</b></td><td>0.01 <b>(+230.15%)</b></td><td>606.40 <b>(+105.49%)</b></td><td>336.56 <b>(+27.15%)</b></td><td>290.90 (+9.03%)</td><td>188.80 (-17.63%)</td><td>162.47 <b>(+478.71%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>295.10 (n/a)</td><td>264.70 (n/a)</td><td>266.80 (n/a)</td><td>229.20 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-16.63%)</td><td>0.01 <b>(-24.85%)</b></td><td>0.01 <b>(-42.07%)</b></td><td>0.01 (+5.96%)</td><td>0.00 <b>(-31.55%)</b></td><td>525.40 (-5.62%)</td><td>421.68 <b>(+23.94%)</b></td><td>457.30 <b>(+72.63%)</b></td><td>240.60 (+19.94%)</td><td>108.99 <b>(-28.25%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.70 (n/a)</td><td>340.24 (n/a)</td><td>264.90 (n/a)</td><td>200.60 (n/a)</td><td>151.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-11.89%)</td><td>0.01 (-5.16%)</td><td>0.01 (-5.47%)</td><td>0.01 (-1.96%)</td><td>0.00 (-14.53%)</td><td>583.80 (+1.99%)</td><td>412.50 (+3.67%)</td><td>454.20 (+5.78%)</td><td>257.60 (+13.48%)</td><td>135.34 (-2.58%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.40 (n/a)</td><td>397.90 (n/a)</td><td>429.40 (n/a)</td><td>227.00 (n/a)</td><td>138.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-8.38%)</td><td>0.01 (-12.66%)</td><td>0.01 (-14.51%)</td><td>0.01 (-17.40%)</td><td>0.01 (-2.82%)</td><td>652.70 <b>(+21.07%)</b></td><td>446.92 (+17.86%)</td><td>468.60 (+16.97%)</td><td>241.20 (+9.19%)</td><td>181.31 <b>(+29.52%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.10 (n/a)</td><td>379.18 (n/a)</td><td>400.60 (n/a)</td><td>220.90 (n/a)</td><td>139.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-2.68%)</td><td>0.01 (+4.72%)</td><td>0.01 <b>(+22.48%)</b></td><td>0.01 (-6.85%)</td><td>0.00 (-8.90%)</td><td>614.10 (+7.34%)</td><td>395.68 (-6.06%)</td><td>397.70 (-18.35%)</td><td>251.80 (+2.73%)</td><td>148.40 (-2.78%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.10 (n/a)</td><td>421.20 (n/a)</td><td>487.10 (n/a)</td><td>245.10 (n/a)</td><td>152.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 <b>(+34.70%)</b></td><td>0.01 (+16.59%)</td><td>0.01 (-17.33%)</td><td>0.01 <b>(+106.06%)</b></td><td>0.01 (+19.52%)</td><td>596.50 <b>(-51.47%)</b></td><td>383.20 <b>(-25.66%)</b></td><td>429.90 <b>(+20.96%)</b></td><td>211.50 <b>(-25.76%)</b></td><td>156.50 <b>(-61.10%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1229.20 (n/a)</td><td>515.50 (n/a)</td><td>355.40 (n/a)</td><td>284.90 (n/a)</td><td>402.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 <b>(-36.09%)</b></td><td>0.01 (-9.60%)</td><td>0.01 (-1.74%)</td><td>0.01 <b>(+200.23%)</b></td><td>0.00 <b>(-77.18%)</b></td><td>627.90 <b>(-66.69%)</b></td><td>515.40 <b>(-27.58%)</b></td><td>517.30 (+1.77%)</td><td>433.50 <b>(+56.50%)</b></td><td>73.84 <b>(-88.91%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1885.00 (n/a)</td><td>711.72 (n/a)</td><td>508.30 (n/a)</td><td>277.00 (n/a)</td><td>665.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-5.29%)</td><td>0.02 (-16.89%)</td><td>0.03 (-11.98%)</td><td>0.01 <b>(-36.35%)</b></td><td>0.01 <b>(+72.63%)</b></td><td>557.10 <b>(+57.11%)</b></td><td>364.06 <b>(+29.15%)</b></td><td>313.60 (+13.62%)</td><td>254.70 (+5.60%)</td><td>129.15 <b>(+181.39%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>354.60 (n/a)</td><td>281.90 (n/a)</td><td>276.00 (n/a)</td><td>241.20 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (-12.32%)</td><td>0.03 (+3.17%)</td><td>0.03 (+1.72%)</td><td>0.02 (+9.11%)</td><td>0.01 (-18.28%)</td><td>562.70 (-8.36%)</td><td>398.28 (-5.98%)</td><td>415.90 (-1.68%)</td><td>228.10 (+14.05%)</td><td>137.80 (-8.51%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>614.00 (n/a)</td><td>423.60 (n/a)</td><td>423.00 (n/a)</td><td>200.00 (n/a)</td><td>150.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-10.21%)</td><td>0.02 <b>(-22.57%)</b></td><td>0.02 <b>(-42.78%)</b></td><td>0.01 <b>(-20.55%)</b></td><td>0.01 (+3.55%)</td><td>557.80 <b>(+25.86%)</b></td><td>439.78 <b>(+32.34%)</b></td><td>501.90 <b>(+74.76%)</b></td><td>274.30 (+11.37%)</td><td>125.58 <b>(+43.17%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.20 (n/a)</td><td>332.30 (n/a)</td><td>287.20 (n/a)</td><td>246.30 (n/a)</td><td>87.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (-13.28%)</td><td>0.04 (-9.15%)</td><td>0.04 (+1.79%)</td><td>0.02 <b>(-34.40%)</b></td><td>0.01 (+0.65%)</td><td>633.80 <b>(+52.43%)</b></td><td>317.58 (+18.77%)</td><td>243.90 (-1.77%)</td><td>200.40 (+15.30%)</td><td>178.43 <b>(+91.29%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>415.80 (n/a)</td><td>267.40 (n/a)</td><td>248.30 (n/a)</td><td>173.80 (n/a)</td><td>93.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (+9.34%)</td><td>0.02 (-8.14%)</td><td>0.02 <b>(-31.92%)</b></td><td>0.01 (-9.64%)</td><td>0.01 (+3.92%)</td><td>621.40 (+10.67%)</td><td>413.22 (+9.12%)</td><td>408.70 <b>(+46.91%)</b></td><td>230.10 (-8.51%)</td><td>156.15 (+1.85%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>378.70 (n/a)</td><td>278.20 (n/a)</td><td>251.50 (n/a)</td><td>153.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (+14.73%)</td><td>0.03 (+8.44%)</td><td>0.04 (+5.09%)</td><td>0.02 (+14.49%)</td><td>0.01 (+3.39%)</td><td>524.10 (-12.66%)</td><td>342.86 (-9.84%)</td><td>247.10 (-4.85%)</td><td>210.00 (-12.83%)</td><td>152.00 (-16.67%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.10 (n/a)</td><td>380.30 (n/a)</td><td>259.70 (n/a)</td><td>240.90 (n/a)</td><td>182.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (-9.38%)</td><td>0.02 <b>(-21.07%)</b></td><td>0.02 <b>(-37.43%)</b></td><td>0.01 (-17.61%)</td><td>0.01 (+11.12%)</td><td>571.40 <b>(+21.37%)</b></td><td>410.02 <b>(+30.84%)</b></td><td>459.10 <b>(+59.85%)</b></td><td>267.00 (+10.33%)</td><td>132.07 <b>(+40.53%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.80 (n/a)</td><td>313.38 (n/a)</td><td>287.20 (n/a)</td><td>242.00 (n/a)</td><td>93.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (+12.83%)</td><td>0.03 (-6.96%)</td><td>0.02 <b>(-29.38%)</b></td><td>0.02 (-19.62%)</td><td>0.01 <b>(+108.81%)</b></td><td>510.80 <b>(+24.40%)</b></td><td>371.76 (+17.50%)</td><td>435.90 <b>(+41.62%)</b></td><td>220.10 (-11.36%)</td><td>129.82 <b>(+119.68%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>410.60 (n/a)</td><td>316.38 (n/a)</td><td>307.80 (n/a)</td><td>248.30 (n/a)</td><td>59.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+12.88%)</td><td>0.02 (-6.95%)</td><td>0.02 <b>(-36.63%)</b></td><td>0.01 (+2.85%)</td><td>0.01 <b>(+21.64%)</b></td><td>584.90 (-2.76%)</td><td>416.30 (+10.07%)</td><td>463.20 <b>(+57.82%)</b></td><td>235.00 (-11.39%)</td><td>148.56 (+4.03%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.50 (n/a)</td><td>378.22 (n/a)</td><td>293.50 (n/a)</td><td>265.20 (n/a)</td><td>142.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 <b>(-28.82%)</b></td><td>0.02 <b>(-37.96%)</b></td><td>0.02 <b>(-31.13%)</b></td><td>0.01 <b>(-72.11%)</b></td><td>0.01 (+1.91%)</td><td>1810.20 <b>(+258.60%)</b></td><td>736.24 <b>(+109.48%)</b></td><td>494.30 <b>(+45.21%)</b></td><td>337.60 <b>(+40.49%)</b></td><td>606.73 <b>(+483.33%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.80 (n/a)</td><td>351.46 (n/a)</td><td>340.40 (n/a)</td><td>240.30 (n/a)</td><td>104.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (+0.74%)</td><td>0.02 (-6.03%)</td><td>0.02 <b>(-26.04%)</b></td><td>0.02 <b>(+21.89%)</b></td><td>0.01 <b>(-21.54%)</b></td><td>494.40 (-17.97%)</td><td>413.42 (-0.11%)</td><td>460.40 <b>(+35.21%)</b></td><td>254.90 (-0.74%)</td><td>96.21 <b>(-41.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.70 (n/a)</td><td>413.88 (n/a)</td><td>340.50 (n/a)</td><td>256.80 (n/a)</td><td>163.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (-9.55%)</td><td>0.05 (-11.27%)</td><td>0.04 (-18.83%)</td><td>0.03 (-4.99%)</td><td>0.01 (+3.11%)</td><td>500.80 (+5.25%)</td><td>371.92 (+14.01%)</td><td>380.20 <b>(+23.20%)</b></td><td>254.50 (+10.56%)</td><td>106.94 (+14.81%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>475.80 (n/a)</td><td>326.22 (n/a)</td><td>308.60 (n/a)</td><td>230.20 (n/a)</td><td>93.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (+17.95%)</td><td>0.08 (+12.68%)</td><td>0.08 <b>(+52.02%)</b></td><td>0.05 (-3.26%)</td><td>0.03 (+12.14%)</td><td>500.50 (+3.37%)</td><td>344.50 (-10.24%)</td><td>304.50 <b>(-34.23%)</b></td><td>206.80 (-15.21%)</td><td>127.12 (+2.35%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>484.20 (n/a)</td><td>383.82 (n/a)</td><td>463.00 (n/a)</td><td>243.90 (n/a)</td><td>124.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+17.21%)</td><td>0.05 (+13.60%)</td><td>0.06 (+9.80%)</td><td>0.03 (+3.46%)</td><td>0.02 <b>(+27.02%)</b></td><td>550.90 (-3.33%)</td><td>343.76 (-9.76%)</td><td>275.20 (-8.93%)</td><td>237.20 (-14.68%)</td><td>136.82 (+3.92%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>380.92 (n/a)</td><td>302.20 (n/a)</td><td>278.00 (n/a)</td><td>131.65 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (-5.56%)</td><td>0.06 (+3.64%)</td><td>0.07 (+11.22%)</td><td>0.02 <b>(-50.36%)</b></td><td>0.03 <b>(+35.93%)</b></td><td>1057.00 <b>(+101.45%)</b></td><td>428.70 <b>(+20.26%)</b></td><td>278.70 (-10.10%)</td><td>246.90 (+5.87%)</td><td>351.87 <b>(+202.94%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>524.70 (n/a)</td><td>356.48 (n/a)</td><td>310.00 (n/a)</td><td>233.20 (n/a)</td><td>116.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (+8.91%)</td><td>0.04 (-8.36%)</td><td>0.04 (+1.89%)</td><td>0.01 <b>(-55.07%)</b></td><td>0.02 <b>(+53.70%)</b></td><td>1131.00 <b>(+122.55%)</b></td><td>550.34 <b>(+32.48%)</b></td><td>450.10 (-1.85%)</td><td>239.30 (-8.17%)</td><td>345.14 <b>(+223.15%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>508.20 (n/a)</td><td>415.40 (n/a)</td><td>458.60 (n/a)</td><td>260.60 (n/a)</td><td>106.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (+2.72%)</td><td>0.05 (-8.88%)</td><td>0.04 (-6.37%)</td><td>0.04 (+4.31%)</td><td>0.02 (-5.73%)</td><td>529.40 (-4.13%)</td><td>437.76 (+7.61%)</td><td>479.00 (+6.80%)</td><td>238.80 (-2.65%)</td><td>116.68 (-14.73%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>552.20 (n/a)</td><td>406.82 (n/a)</td><td>448.50 (n/a)</td><td>245.30 (n/a)</td><td>136.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (+14.50%)</td><td>0.05 <b>(+42.23%)</b></td><td>0.04 (+1.49%)</td><td>0.03 <b>(+234.25%)</b></td><td>0.02 (-18.01%)</td><td>586.70 <b>(-70.08%)</b></td><td>388.86 <b>(-60.45%)</b></td><td>421.80 (-1.47%)</td><td>189.50 (-12.67%)</td><td>147.04 <b>(-83.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1961.10 (n/a)</td><td>983.24 (n/a)</td><td>428.10 (n/a)</td><td>217.00 (n/a)</td><td>869.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (-4.18%)</td><td>0.06 (+2.50%)</td><td>0.06 (+10.83%)</td><td>0.03 (-5.65%)</td><td>0.02 (+4.70%)</td><td>573.50 (+5.99%)</td><td>364.48 (-0.77%)</td><td>304.40 (-9.78%)</td><td>243.70 (+4.37%)</td><td>138.66 (+14.24%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.10 (n/a)</td><td>367.30 (n/a)</td><td>337.40 (n/a)</td><td>233.50 (n/a)</td><td>121.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 <b>(+35.68%)</b></td><td>0.04 (-1.93%)</td><td>0.03 <b>(-20.67%)</b></td><td>0.03 (+0.80%)</td><td>0.02 <b>(+84.39%)</b></td><td>593.10 (-0.79%)</td><td>464.74 (+12.97%)</td><td>540.40 <b>(+26.06%)</b></td><td>193.70 <b>(-26.29%)</b></td><td>168.41 <b>(+34.37%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>411.40 (n/a)</td><td>428.70 (n/a)</td><td>262.80 (n/a)</td><td>125.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 <b>(-22.98%)</b></td><td>0.05 (+4.85%)</td><td>0.06 <b>(+41.74%)</b></td><td>0.04 <b>(+27.77%)</b></td><td>0.01 <b>(-43.49%)</b></td><td>523.80 <b>(-21.73%)</b></td><td>360.28 (-13.14%)</td><td>300.90 <b>(-29.45%)</b></td><td>293.60 <b>(+29.80%)</b></td><td>99.87 <b>(-42.59%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>669.20 (n/a)</td><td>414.80 (n/a)</td><td>426.50 (n/a)</td><td>226.20 (n/a)</td><td>173.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (-8.46%)</td><td>0.04 (+6.81%)</td><td>0.03 (-0.47%)</td><td>0.03 <b>(+122.74%)</b></td><td>0.01 <b>(-28.14%)</b></td><td>611.70 <b>(-55.11%)</b></td><td>463.80 <b>(-23.06%)</b></td><td>477.00 (+0.48%)</td><td>319.60 (+9.23%)</td><td>134.30 <b>(-68.92%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1362.60 (n/a)</td><td>602.82 (n/a)</td><td>474.70 (n/a)</td><td>292.60 (n/a)</td><td>432.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (+18.17%)</td><td>0.09 (+1.04%)</td><td>0.08 <b>(-28.88%)</b></td><td>0.06 (+7.51%)</td><td>0.03 (+7.57%)</td><td>591.50 (-6.98%)</td><td>400.56 (-2.25%)</td><td>429.00 <b>(+40.61%)</b></td><td>238.70 (-15.35%)</td><td>135.67 (-15.54%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.90 (n/a)</td><td>409.76 (n/a)</td><td>305.10 (n/a)</td><td>282.00 (n/a)</td><td>160.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 <b>(+27.56%)</b></td><td>0.09 (-0.16%)</td><td>0.07 <b>(-20.03%)</b></td><td>0.05 (-16.63%)</td><td>0.04 <b>(+98.45%)</b></td><td>644.10 (+19.94%)</td><td>430.46 (+9.62%)</td><td>480.30 <b>(+25.05%)</b></td><td>238.40 <b>(-21.60%)</b></td><td>162.65 <b>(+79.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>537.00 (n/a)</td><td>392.70 (n/a)</td><td>384.10 (n/a)</td><td>304.10 (n/a)</td><td>90.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.19 <b>(+23.64%)</b></td><td>0.13 <b>(+52.31%)</b></td><td>0.16 <b>(+87.12%)</b></td><td>0.07 <b>(+292.55%)</b></td><td>0.06 <b>(+23.99%)</b></td><td>627.70 <b>(-74.53%)</b></td><td>390.66 <b>(-53.00%)</b></td><td>250.10 <b>(-46.56%)</b></td><td>215.80 (-19.15%)</td><td>212.63 <b>(-76.83%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2464.10 (n/a)</td><td>831.24 (n/a)</td><td>468.00 (n/a)</td><td>266.90 (n/a)</td><td>917.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (-1.82%)</td><td>0.09 (+2.28%)</td><td>0.08 (+7.51%)</td><td>0.05 <b>(+25.31%)</b></td><td>0.03 (-3.78%)</td><td>621.20 <b>(-20.21%)</b></td><td>422.50 (-5.21%)</td><td>386.40 (-6.98%)</td><td>268.70 (+1.86%)</td><td>161.87 <b>(-21.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>778.50 (n/a)</td><td>445.72 (n/a)</td><td>415.40 (n/a)</td><td>263.80 (n/a)</td><td>206.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (+0.15%)</td><td>0.11 (+6.74%)</td><td>0.10 (-10.05%)</td><td>0.09 <b>(+25.84%)</b></td><td>0.02 <b>(-28.81%)</b></td><td>443.00 <b>(-20.54%)</b></td><td>382.70 (-10.10%)</td><td>417.40 (+11.19%)</td><td>289.40 (-0.14%)</td><td>65.68 <b>(-46.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>557.50 (n/a)</td><td>425.70 (n/a)</td><td>375.40 (n/a)</td><td>289.80 (n/a)</td><td>123.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (-10.11%)</td><td>0.08 <b>(-25.74%)</b></td><td>0.07 <b>(-48.27%)</b></td><td>0.06 <b>(-21.39%)</b></td><td>0.03 (-10.96%)</td><td>587.60 <b>(+27.21%)</b></td><td>442.62 <b>(+35.51%)</b></td><td>501.00 <b>(+93.29%)</b></td><td>264.30 (+11.24%)</td><td>131.75 <b>(+23.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.90 (n/a)</td><td>326.64 (n/a)</td><td>259.20 (n/a)</td><td>237.60 (n/a)</td><td>106.45 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.18 <b>(+46.59%)</b></td><td>0.09 <b>(+25.85%)</b></td><td>0.08 (-10.78%)</td><td>0.06 <b>(+293.45%)</b></td><td>0.05 <b>(+20.84%)</b></td><td>608.50 <b>(-74.58%)</b></td><td>458.08 <b>(-45.18%)</b></td><td>481.00 (+12.10%)</td><td>209.30 <b>(-31.80%)</b></td><td>151.29 <b>(-82.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2394.00 (n/a)</td><td>835.62 (n/a)</td><td>429.10 (n/a)</td><td>306.90 (n/a)</td><td>878.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (-2.66%)</td><td>0.07 (-16.38%)</td><td>0.07 <b>(-30.20%)</b></td><td>0.05 (-10.59%)</td><td>0.03 (+19.67%)</td><td>645.50 (+11.85%)</td><td>478.20 <b>(+23.37%)</b></td><td>498.00 <b>(+43.27%)</b></td><td>297.60 (+2.73%)</td><td>148.72 <b>(+32.32%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>577.10 (n/a)</td><td>387.60 (n/a)</td><td>347.60 (n/a)</td><td>289.70 (n/a)</td><td>112.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (+5.22%)</td><td>0.10 <b>(+20.90%)</b></td><td>0.08 <b>(+20.51%)</b></td><td>0.07 (+14.49%)</td><td>0.04 (+0.62%)</td><td>560.70 (-12.65%)</td><td>406.44 (-18.75%)</td><td>476.20 (-17.01%)</td><td>218.30 (-4.96%)</td><td>143.34 (-14.11%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>641.90 (n/a)</td><td>500.26 (n/a)</td><td>573.80 (n/a)</td><td>229.70 (n/a)</td><td>166.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (+3.64%)</td><td>0.07 (-9.60%)</td><td>0.07 (+3.13%)</td><td>0.05 (-17.62%)</td><td>0.03 (+16.17%)</td><td>674.50 <b>(+21.38%)</b></td><td>503.68 (+14.73%)</td><td>462.80 (-3.04%)</td><td>289.60 (-3.50%)</td><td>165.62 <b>(+43.44%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>555.70 (n/a)</td><td>439.02 (n/a)</td><td>477.30 (n/a)</td><td>300.10 (n/a)</td><td>115.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 <b>(+22.39%)</b></td><td>0.07 <b>(+60.23%)</b></td><td>0.07 <b>(+107.58%)</b></td><td>0.04 <b>(+367.25%)</b></td><td>0.02 <b>(-33.08%)</b></td><td>523.20 <b>(-78.60%)</b></td><td>326.62 <b>(-61.93%)</b></td><td>293.60 <b>(-51.82%)</b></td><td>241.60 (-18.30%)</td><td>112.62 <b>(-87.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2444.50 (n/a)</td><td>857.94 (n/a)</td><td>609.40 (n/a)</td><td>295.70 (n/a)</td><td>901.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 <b>(-26.04%)</b></td><td>0.06 (-11.58%)</td><td>0.07 (-3.51%)</td><td>0.03 (-19.53%)</td><td>0.02 (-15.05%)</td><td>600.60 <b>(+24.27%)</b></td><td>394.70 (+17.00%)</td><td>312.90 (+3.64%)</td><td>238.50 <b>(+35.20%)</b></td><td>177.12 <b>(+47.49%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>483.30 (n/a)</td><td>337.34 (n/a)</td><td>301.90 (n/a)</td><td>176.40 (n/a)</td><td>120.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (-7.04%)</td><td>0.04 (-9.33%)</td><td>0.03 (-17.55%)</td><td>0.01 <b>(-56.24%)</b></td><td>0.02 (+15.28%)</td><td>2428.20 <b>(+128.54%)</b></td><td>865.00 <b>(+53.14%)</b></td><td>600.00 <b>(+21.29%)</b></td><td>297.60 (+7.55%)</td><td>884.04 <b>(+200.13%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1062.50 (n/a)</td><td>564.86 (n/a)</td><td>494.70 (n/a)</td><td>276.70 (n/a)</td><td>294.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (+9.57%)</td><td>0.06 (-12.93%)</td><td>0.04 <b>(-44.60%)</b></td><td>0.03 <b>(-28.96%)</b></td><td>0.03 <b>(+37.72%)</b></td><td>742.90 <b>(+40.78%)</b></td><td>451.66 <b>(+29.35%)</b></td><td>460.20 <b>(+80.47%)</b></td><td>227.90 (-8.73%)</td><td>225.22 <b>(+67.89%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>527.70 (n/a)</td><td>349.18 (n/a)</td><td>255.00 (n/a)</td><td>249.70 (n/a)</td><td>134.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (-2.62%)</td><td>0.05 (+10.75%)</td><td>0.04 (+16.73%)</td><td>0.04 (+4.03%)</td><td>0.02 (-13.73%)</td><td>568.20 (-3.87%)</td><td>441.24 (-11.70%)</td><td>460.30 (-14.33%)</td><td>275.70 (+2.72%)</td><td>115.82 (-13.40%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.10 (n/a)</td><td>499.70 (n/a)</td><td>537.30 (n/a)</td><td>268.40 (n/a)</td><td>133.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 <b>(-33.35%)</b></td><td>0.04 <b>(-24.70%)</b></td><td>0.03 <b>(-21.78%)</b></td><td>0.02 <b>(-36.24%)</b></td><td>0.01 <b>(-37.27%)</b></td><td>1066.20 <b>(+56.86%)</b></td><td>643.52 <b>(+32.26%)</b></td><td>631.00 <b>(+27.84%)</b></td><td>364.50 <b>(+50.06%)</b></td><td>260.43 <b>(+58.27%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>679.70 (n/a)</td><td>486.54 (n/a)</td><td>493.60 (n/a)</td><td>242.90 (n/a)</td><td>164.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+4.99%)</td><td>0.07 (+18.32%)</td><td>0.08 <b>(+53.54%)</b></td><td>0.04 (+2.47%)</td><td>0.02 <b>(+30.38%)</b></td><td>574.20 (-2.41%)</td><td>407.78 (-12.51%)</td><td>326.80 <b>(-34.86%)</b></td><td>290.40 (-4.76%)</td><td>143.77 <b>(+22.66%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>588.40 (n/a)</td><td>466.08 (n/a)</td><td>501.70 (n/a)</td><td>304.90 (n/a)</td><td>117.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (-11.75%)</td><td>0.07 (+19.32%)</td><td>0.07 <b>(+55.79%)</b></td><td>0.04 <b>(+219.35%)</b></td><td>0.02 <b>(-40.44%)</b></td><td>582.30 <b>(-68.69%)</b></td><td>374.84 <b>(-45.83%)</b></td><td>333.00 <b>(-35.81%)</b></td><td>250.50 (+13.30%)</td><td>136.70 <b>(-79.61%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1859.60 (n/a)</td><td>691.96 (n/a)</td><td>518.80 (n/a)</td><td>221.10 (n/a)</td><td>670.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 <b>(+22.42%)</b></td><td>0.05 (-11.49%)</td><td>0.04 <b>(-32.37%)</b></td><td>0.01 <b>(-69.32%)</b></td><td>0.03 <b>(+122.73%)</b></td><td>1820.60 <b>(+225.98%)</b></td><td>724.94 <b>(+71.79%)</b></td><td>604.90 <b>(+47.86%)</b></td><td>242.70 (-18.31%)</td><td>636.70 <b>(+499.32%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>558.50 (n/a)</td><td>421.98 (n/a)</td><td>409.10 (n/a)</td><td>297.10 (n/a)</td><td>106.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 <b>(+28.27%)</b></td><td>0.06 <b>(+31.35%)</b></td><td>0.06 <b>(+29.24%)</b></td><td>0.04 <b>(+70.64%)</b></td><td>0.02 (+17.23%)</td><td>591.30 <b>(-41.40%)</b></td><td>414.76 <b>(-27.33%)</b></td><td>382.50 <b>(-22.62%)</b></td><td>266.00 <b>(-22.04%)</b></td><td>129.94 <b>(-49.31%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1009.00 (n/a)</td><td>570.78 (n/a)</td><td>494.30 (n/a)</td><td>341.20 (n/a)</td><td>256.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (+6.15%)</td><td>0.07 (+12.51%)</td><td>0.08 <b>(+50.71%)</b></td><td>0.05 (+2.90%)</td><td>0.02 (-3.77%)</td><td>534.00 (-2.82%)</td><td>363.86 (-12.46%)</td><td>322.50 <b>(-33.64%)</b></td><td>240.00 (-5.81%)</td><td>128.23 (-9.79%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>549.50 (n/a)</td><td>415.66 (n/a)</td><td>486.00 (n/a)</td><td>254.80 (n/a)</td><td>142.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (-9.08%)</td><td>0.07 (+1.81%)</td><td>0.06 (-5.96%)</td><td>0.04 <b>(+327.23%)</b></td><td>0.02 <b>(-44.38%)</b></td><td>551.50 <b>(-76.59%)</b></td><td>392.02 <b>(-47.10%)</b></td><td>383.30 (+6.35%)</td><td>254.70 (+9.97%)</td><td>126.98 <b>(-86.05%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2356.10 (n/a)</td><td>741.00 (n/a)</td><td>360.40 (n/a)</td><td>231.60 (n/a)</td><td>910.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (-7.39%)</td><td>0.05 (+6.76%)</td><td>0.05 <b>(+23.64%)</b></td><td>0.04 (+11.00%)</td><td>0.01 <b>(-25.07%)</b></td><td>479.80 (-9.90%)</td><td>395.04 (-10.44%)</td><td>401.70 (-19.13%)</td><td>246.30 (+7.98%)</td><td>90.68 <b>(-27.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.50 (n/a)</td><td>441.10 (n/a)</td><td>496.70 (n/a)</td><td>228.10 (n/a)</td><td>125.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+5.84%)</td><td>0.06 <b>(+23.91%)</b></td><td>0.07 <b>(+66.35%)</b></td><td>0.03 (-5.77%)</td><td>0.02 (-0.16%)</td><td>590.80 (+6.13%)</td><td>334.16 (-18.84%)</td><td>265.90 <b>(-39.88%)</b></td><td>242.50 (-5.53%)</td><td>145.55 (+6.56%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>556.70 (n/a)</td><td>411.72 (n/a)</td><td>442.30 (n/a)</td><td>256.70 (n/a)</td><td>136.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+17.90%)</td><td>0.07 <b>(+39.97%)</b></td><td>0.07 <b>(+80.92%)</b></td><td>0.04 <b>(+34.52%)</b></td><td>0.01 (-14.15%)</td><td>427.10 <b>(-25.67%)</b></td><td>294.10 <b>(-31.43%)</b></td><td>256.60 <b>(-44.73%)</b></td><td>241.70 (-15.19%)</td><td>76.29 <b>(-41.97%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.60 (n/a)</td><td>428.88 (n/a)</td><td>464.30 (n/a)</td><td>285.00 (n/a)</td><td>131.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (+8.94%)</td><td>0.05 <b>(+24.28%)</b></td><td>0.06 <b>(+83.78%)</b></td><td>0.03 (-4.73%)</td><td>0.02 <b>(+24.05%)</b></td><td>595.40 (+4.97%)</td><td>385.30 (-16.18%)</td><td>288.30 <b>(-45.58%)</b></td><td>241.40 (-8.21%)</td><td>161.37 (+19.21%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>567.20 (n/a)</td><td>459.66 (n/a)</td><td>529.80 (n/a)</td><td>263.00 (n/a)</td><td>135.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (-19.77%)</td><td>0.05 (+13.34%)</td><td>0.06 <b>(+59.48%)</b></td><td>0.03 (-0.63%)</td><td>0.02 <b>(-23.43%)</b></td><td>619.50 (+0.62%)</td><td>403.58 (-14.59%)</td><td>333.00 <b>(-37.30%)</b></td><td>250.80 <b>(+24.65%)</b></td><td>168.08 (+2.10%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>615.70 (n/a)</td><td>472.54 (n/a)</td><td>531.10 (n/a)</td><td>201.20 (n/a)</td><td>164.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (-14.09%)</td><td>0.04 <b>(-24.44%)</b></td><td>0.04 <b>(-36.98%)</b></td><td>0.03 (-14.96%)</td><td>0.02 (-6.71%)</td><td>600.80 (+17.57%)</td><td>476.22 <b>(+33.80%)</b></td><td>515.20 <b>(+58.67%)</b></td><td>269.80 (+16.39%)</td><td>131.44 <b>(+22.91%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>511.00 (n/a)</td><td>355.92 (n/a)</td><td>324.70 (n/a)</td><td>231.80 (n/a)</td><td>106.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.35 (-16.59%)</td><td>0.31 <b>(+33.43%)</b></td><td>0.34 <b>(+72.42%)</b></td><td>0.18 <b>(+362.18%)</b></td><td>0.07 <b>(-50.83%)</b></td><td>533.10 <b>(-78.36%)</b></td><td>336.60 <b>(-58.21%)</b></td><td>292.00 <b>(-42.01%)</b></td><td>280.50 (+19.92%)</td><td>109.96 <b>(-88.24%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.42 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.14 (n/a)</td><td>2463.70 (n/a)</td><td>805.38 (n/a)</td><td>503.50 (n/a)</td><td>233.90 (n/a)</td><td>935.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.37 <b>(-27.24%)</b></td><td>0.29 (-17.00%)</td><td>0.29 (-19.49%)</td><td>0.22 <b>(+51.45%)</b></td><td>0.06 <b>(-56.17%)</b></td><td>455.30 <b>(-33.97%)</b></td><td>355.84 (+3.77%)</td><td>341.20 <b>(+24.25%)</b></td><td>267.00 <b>(+37.42%)</b></td><td>71.70 <b>(-63.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>689.50 (n/a)</td><td>342.92 (n/a)</td><td>274.60 (n/a)</td><td>194.30 (n/a)</td><td>197.86 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.30 <b>(-23.67%)</b></td><td>0.24 (+5.57%)</td><td>0.24 <b>(+24.97%)</b></td><td>0.19 <b>(+25.27%)</b></td><td>0.05 <b>(-49.61%)</b></td><td>510.80 <b>(-20.16%)</b></td><td>422.28 (-11.69%)</td><td>402.90 (-20.00%)</td><td>325.20 <b>(+31.02%)</b></td><td>85.09 <b>(-40.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.40 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>639.80 (n/a)</td><td>478.20 (n/a)</td><td>503.60 (n/a)</td><td>248.20 (n/a)</td><td>142.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.34 <b>(+23.19%)</b></td><td>0.23 <b>(+21.63%)</b></td><td>0.24 <b>(+48.03%)</b></td><td>0.12 (-8.14%)</td><td>0.10 <b>(+57.51%)</b></td><td>592.30 (+8.86%)</td><td>372.94 (-10.61%)</td><td>308.50 <b>(-32.44%)</b></td><td>218.40 (-18.81%)</td><td>169.63 <b>(+39.36%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>544.10 (n/a)</td><td>417.22 (n/a)</td><td>456.60 (n/a)</td><td>269.00 (n/a)</td><td>121.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.30 (+9.66%)</td><td>0.25 (+18.14%)</td><td>0.26 (+8.13%)</td><td>0.16 <b>(+32.15%)</b></td><td>0.05 <b>(-26.96%)</b></td><td>451.10 <b>(-24.32%)</b></td><td>307.42 <b>(-20.78%)</b></td><td>279.60 (-7.54%)</td><td>243.90 (-8.79%)</td><td>82.66 <b>(-45.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>596.10 (n/a)</td><td>388.06 (n/a)</td><td>302.40 (n/a)</td><td>267.40 (n/a)</td><td>152.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 <b>(+39.63%)</b></td><td>0.17 (-3.80%)</td><td>0.15 (-10.90%)</td><td>0.04 <b>(-66.62%)</b></td><td>0.10 <b>(+141.87%)</b></td><td>1825.60 <b>(+199.62%)</b></td><td>689.28 <b>(+56.31%)</b></td><td>501.10 (+12.23%)</td><td>240.60 <b>(-28.37%)</b></td><td>645.54 <b>(+487.81%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>609.30 (n/a)</td><td>440.98 (n/a)</td><td>446.50 (n/a)</td><td>335.90 (n/a)</td><td>109.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (-13.60%)</td><td>0.10 (-18.99%)</td><td>0.10 (-19.74%)</td><td>0.07 (-12.34%)</td><td>0.03 (+0.31%)</td><td>547.70 (+14.08%)</td><td>398.50 <b>(+25.09%)</b></td><td>360.40 <b>(+24.62%)</b></td><td>288.20 (+15.74%)</td><td>115.99 <b>(+25.51%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>480.10 (n/a)</td><td>318.58 (n/a)</td><td>289.20 (n/a)</td><td>249.00 (n/a)</td><td>92.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (-13.97%)</td><td>0.08 (-6.10%)</td><td>0.08 (+6.08%)</td><td>0.06 (+16.69%)</td><td>0.03 <b>(-33.10%)</b></td><td>629.00 (-14.31%)</td><td>475.84 (-2.80%)</td><td>479.80 (-5.74%)</td><td>296.50 (+16.23%)</td><td>152.40 <b>(-29.45%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>734.00 (n/a)</td><td>489.56 (n/a)</td><td>509.00 (n/a)</td><td>255.10 (n/a)</td><td>216.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (+8.71%)</td><td>0.12 <b>(+21.89%)</b></td><td>0.12 <b>(+61.96%)</b></td><td>0.07 <b>(+22.51%)</b></td><td>0.04 (+10.31%)</td><td>514.90 (-18.37%)</td><td>351.50 (-18.18%)</td><td>295.50 <b>(-38.26%)</b></td><td>223.30 (-7.99%)</td><td>140.22 (-12.48%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>630.80 (n/a)</td><td>429.58 (n/a)</td><td>478.60 (n/a)</td><td>242.70 (n/a)</td><td>160.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (-0.79%)</td><td>0.09 <b>(-34.11%)</b></td><td>0.07 <b>(-47.38%)</b></td><td>0.06 <b>(-49.09%)</b></td><td>0.04 <b>(+260.78%)</b></td><td>593.40 <b>(+96.43%)</b></td><td>457.68 <b>(+68.23%)</b></td><td>508.10 <b>(+90.01%)</b></td><td>248.20 (+0.81%)</td><td>147.14 <b>(+621.21%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>302.10 (n/a)</td><td>272.06 (n/a)</td><td>267.40 (n/a)</td><td>246.20 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 <b>(-22.52%)</b></td><td>0.08 (-1.38%)</td><td>0.07 (-3.17%)</td><td>0.06 <b>(+64.84%)</b></td><td>0.02 <b>(-42.80%)</b></td><td>668.10 <b>(-39.33%)</b></td><td>491.78 (-13.32%)</td><td>527.60 (+3.27%)</td><td>317.40 <b>(+29.02%)</b></td><td>136.86 <b>(-57.02%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1101.20 (n/a)</td><td>567.36 (n/a)</td><td>510.90 (n/a)</td><td>246.00 (n/a)</td><td>318.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (+8.12%)</td><td>0.08 <b>(-24.75%)</b></td><td>0.07 <b>(-42.51%)</b></td><td>0.02 <b>(-75.36%)</b></td><td>0.05 <b>(+47.85%)</b></td><td>2433.20 <b>(+305.80%)</b></td><td>808.40 <b>(+122.98%)</b></td><td>513.00 <b>(+73.96%)</b></td><td>237.90 (-7.54%)</td><td>916.74 <b>(+532.49%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>599.60 (n/a)</td><td>362.54 (n/a)</td><td>294.90 (n/a)</td><td>257.30 (n/a)</td><td>144.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (-19.04%)</td><td>0.11 (-15.66%)</td><td>0.11 <b>(-26.15%)</b></td><td>0.06 (-17.26%)</td><td>0.04 (-18.78%)</td><td>647.60 <b>(+20.87%)</b></td><td>412.42 (+17.94%)</td><td>381.80 <b>(+35.39%)</b></td><td>269.40 <b>(+23.52%)</b></td><td>152.28 (+16.98%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>535.80 (n/a)</td><td>349.70 (n/a)</td><td>282.00 (n/a)</td><td>218.10 (n/a)</td><td>130.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (+9.97%)</td><td>0.14 <b>(+45.39%)</b></td><td>0.16 <b>(+75.90%)</b></td><td>0.08 (+11.69%)</td><td>0.04 (+11.62%)</td><td>486.10 (-10.46%)</td><td>302.60 <b>(-30.88%)</b></td><td>252.20 <b>(-43.15%)</b></td><td>242.30 (-9.05%)</td><td>103.86 (-4.49%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>542.90 (n/a)</td><td>437.80 (n/a)</td><td>443.60 (n/a)</td><td>266.40 (n/a)</td><td>108.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (-3.62%)</td><td>0.13 (+12.01%)</td><td>0.14 (-1.51%)</td><td>0.08 <b>(+307.47%)</b></td><td>0.03 <b>(-48.08%)</b></td><td>498.30 <b>(-75.46%)</b></td><td>339.04 <b>(-48.66%)</b></td><td>297.40 (+1.54%)</td><td>249.80 (+3.74%)</td><td>98.96 <b>(-87.17%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2030.60 (n/a)</td><td>660.36 (n/a)</td><td>292.90 (n/a)</td><td>240.80 (n/a)</td><td>771.47 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (-4.76%)</td><td>0.11 (-7.42%)</td><td>0.08 <b>(-23.25%)</b></td><td>0.06 (-19.74%)</td><td>0.04 (+10.36%)</td><td>636.50 <b>(+24.61%)</b></td><td>432.08 (+11.69%)</td><td>483.30 <b>(+30.27%)</b></td><td>260.20 (+5.00%)</td><td>156.32 <b>(+30.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>510.80 (n/a)</td><td>386.86 (n/a)</td><td>371.00 (n/a)</td><td>247.80 (n/a)</td><td>119.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 <b>(+21.63%)</b></td><td>0.08 (-0.93%)</td><td>0.08 (+3.94%)</td><td>0.04 (-16.30%)</td><td>0.04 <b>(+24.06%)</b></td><td>1067.70 (+19.47%)</td><td>587.24 (+6.55%)</td><td>511.00 (-3.78%)</td><td>288.70 (-17.80%)</td><td>288.53 <b>(+30.57%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>893.70 (n/a)</td><td>551.16 (n/a)</td><td>531.10 (n/a)</td><td>351.20 (n/a)</td><td>220.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (-10.11%)</td><td>0.10 (+3.08%)</td><td>0.09 (-1.21%)</td><td>0.07 (+8.45%)</td><td>0.04 (-1.38%)</td><td>575.40 (-7.79%)</td><td>442.48 (-2.85%)</td><td>479.10 (+1.23%)</td><td>291.20 (+11.23%)</td><td>143.10 (+0.47%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>624.00 (n/a)</td><td>455.46 (n/a)</td><td>473.30 (n/a)</td><td>261.80 (n/a)</td><td>142.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (-4.66%)</td><td>0.09 (-1.98%)</td><td>0.10 <b>(+20.24%)</b></td><td>0.05 <b>(-20.73%)</b></td><td>0.03 (+17.65%)</td><td>667.30 <b>(+26.14%)</b></td><td>420.30 (+7.38%)</td><td>341.40 (-16.85%)</td><td>277.70 (+4.87%)</td><td>169.43 <b>(+56.18%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>529.00 (n/a)</td><td>391.42 (n/a)</td><td>410.60 (n/a)</td><td>264.80 (n/a)</td><td>108.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 <b>(+51.83%)</b></td><td>0.10 <b>(+37.62%)</b></td><td>0.10 <b>(+46.64%)</b></td><td>0.07 (+9.79%)</td><td>0.03 <b>(+178.16%)</b></td><td>533.60 (-8.93%)</td><td>378.72 <b>(-21.56%)</b></td><td>332.50 <b>(-31.81%)</b></td><td>246.20 <b>(-34.14%)</b></td><td>132.62 <b>(+76.46%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>585.90 (n/a)</td><td>482.82 (n/a)</td><td>487.60 (n/a)</td><td>373.80 (n/a)</td><td>75.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 <b>(-37.97%)</b></td><td>0.10 (-11.86%)</td><td>0.12 <b>(+58.33%)</b></td><td>0.06 (-16.03%)</td><td>0.04 <b>(-42.32%)</b></td><td>602.90 (+19.08%)</td><td>394.92 (+5.52%)</td><td>286.40 <b>(-36.85%)</b></td><td>271.50 <b>(+61.22%)</b></td><td>161.44 (+2.59%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>506.30 (n/a)</td><td>374.26 (n/a)</td><td>453.50 (n/a)</td><td>168.40 (n/a)</td><td>157.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (-10.99%)</td><td>0.11 (-2.93%)</td><td>0.11 (-4.97%)</td><td>0.08 (+8.07%)</td><td>0.02 <b>(-35.70%)</b></td><td>456.40 (-7.46%)</td><td>326.42 (-1.04%)</td><td>303.00 (+5.24%)</td><td>261.70 (+12.37%)</td><td>75.05 <b>(-29.85%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>493.20 (n/a)</td><td>329.84 (n/a)</td><td>287.90 (n/a)</td><td>232.90 (n/a)</td><td>106.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (-12.97%)</td><td>0.06 (-14.78%)</td><td>0.07 (+4.13%)</td><td>0.02 <b>(-68.70%)</b></td><td>0.03 (+12.74%)</td><td>2028.10 <b>(+219.49%)</b></td><td>797.94 <b>(+57.71%)</b></td><td>532.90 (-3.96%)</td><td>311.50 (+14.90%)</td><td>697.90 <b>(+390.60%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>634.80 (n/a)</td><td>505.96 (n/a)</td><td>554.90 (n/a)</td><td>271.10 (n/a)</td><td>142.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (+12.74%)</td><td>0.11 (+6.09%)</td><td>0.12 <b>(+28.23%)</b></td><td>0.05 (-7.24%)</td><td>0.05 (+13.33%)</td><td>650.30 (+7.79%)</td><td>396.80 (-1.49%)</td><td>302.70 <b>(-22.02%)</b></td><td>209.70 (-11.29%)</td><td>197.97 (+17.73%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>603.30 (n/a)</td><td>402.82 (n/a)</td><td>388.20 (n/a)</td><td>236.40 (n/a)</td><td>168.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (+18.26%)</td><td>0.34 (-8.29%)</td><td>0.28 <b>(-33.38%)</b></td><td>0.13 <b>(-38.93%)</b></td><td>0.17 <b>(+45.67%)</b></td><td>994.20 <b>(+63.74%)</b></td><td>495.74 <b>(+26.31%)</b></td><td>474.00 <b>(+50.09%)</b></td><td>226.40 (-15.43%)</td><td>298.52 <b>(+106.17%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>607.20 (n/a)</td><td>392.48 (n/a)</td><td>315.80 (n/a)</td><td>267.70 (n/a)</td><td>144.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.46 <b>(+46.87%)</b></td><td>0.21 (-7.75%)</td><td>0.20 (-9.23%)</td><td>0.05 <b>(-70.35%)</b></td><td>0.16 <b>(+220.37%)</b></td><td>2415.90 <b>(+237.32%)</b></td><td>1147.60 <b>(+90.72%)</b></td><td>654.80 (+10.18%)</td><td>286.00 <b>(-31.90%)</b></td><td>939.21 <b>(+714.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>716.20 (n/a)</td><td>601.72 (n/a)</td><td>594.30 (n/a)</td><td>420.00 (n/a)</td><td>115.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (-5.22%)</td><td>0.34 <b>(+21.81%)</b></td><td>0.27 (+5.97%)</td><td>0.26 <b>(+45.26%)</b></td><td>0.10 (-17.77%)</td><td>496.40 <b>(-31.15%)</b></td><td>413.72 <b>(-21.65%)</b></td><td>486.20 (-5.63%)</td><td>290.10 (+5.53%)</td><td>106.24 <b>(-35.73%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.48 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>721.00 (n/a)</td><td>528.06 (n/a)</td><td>515.20 (n/a)</td><td>274.90 (n/a)</td><td>165.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-5.99%)</td><td>0.01 <b>(-20.38%)</b></td><td>0.01 <b>(-26.61%)</b></td><td>0.01 <b>(-39.44%)</b></td><td>0.00 <b>(+75.83%)</b></td><td>509.80 <b>(+65.09%)</b></td><td>388.58 <b>(+36.27%)</b></td><td>411.10 <b>(+36.26%)</b></td><td>229.50 (+6.40%)</td><td>127.37 <b>(+224.23%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>308.80 (n/a)</td><td>285.16 (n/a)</td><td>301.70 (n/a)</td><td>215.70 (n/a)</td><td>39.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-16.65%)</td><td>0.01 (-19.50%)</td><td>0.01 (-7.63%)</td><td>0.01 (-14.01%)</td><td>0.00 (-6.55%)</td><td>558.60 (+16.28%)</td><td>373.76 <b>(+26.43%)</b></td><td>290.70 (+8.27%)</td><td>254.70 (+19.97%)</td><td>138.84 <b>(+28.16%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.40 (n/a)</td><td>295.62 (n/a)</td><td>268.50 (n/a)</td><td>212.30 (n/a)</td><td>108.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (-13.31%)</td><td>0.01 (+8.23%)</td><td>0.01 <b>(+30.92%)</b></td><td>0.01 <b>(+23.07%)</b></td><td>0.00 <b>(-34.41%)</b></td><td>521.40 (-18.73%)</td><td>351.68 (-12.95%)</td><td>312.50 <b>(-23.61%)</b></td><td>276.00 (+15.34%)</td><td>98.11 <b>(-35.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.60 (n/a)</td><td>404.02 (n/a)</td><td>409.10 (n/a)</td><td>239.30 (n/a)</td><td>152.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.90 <b>(-29.19%)</b></td><td>6.38 (-6.58%)</td><td>6.27 (+4.53%)</td><td>5.03 <b>(+37.40%)</b></td><td>1.09 <b>(-62.39%)</b></td><td>416.90 <b>(-27.23%)</b></td><td>336.68 (-4.92%)</td><td>334.40 (-4.35%)</td><td>265.60 <b>(+41.28%)</b></td><td>57.38 <b>(-60.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>11.16 (n/a)</td><td>6.83 (n/a)</td><td>6.00 (n/a)</td><td>3.66 (n/a)</td><td>2.89 (n/a)</td><td>572.90 (n/a)</td><td>354.12 (n/a)</td><td>349.60 (n/a)</td><td>188.00 (n/a)</td><td>147.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.55 (-8.35%)</td><td>0.47 (+16.41%)</td><td>0.50 <b>(+32.86%)</b></td><td>0.34 <b>(+22.29%)</b></td><td>0.08 <b>(-36.77%)</b></td><td>392.50 (-18.23%)</td><td>287.34 (-17.95%)</td><td>263.30 <b>(-24.73%)</b></td><td>240.70 (+9.11%)</td><td>60.46 <b>(-41.14%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.60 (n/a)</td><td>0.41 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>480.00 (n/a)</td><td>350.18 (n/a)</td><td>349.80 (n/a)</td><td>220.60 (n/a)</td><td>102.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (+18.94%)</td><td>0.39 (+11.05%)</td><td>0.31 <b>(-26.61%)</b></td><td>0.27 <b>(+301.59%)</b></td><td>0.15 (-8.62%)</td><td>492.00 <b>(-75.10%)</b></td><td>376.66 <b>(-41.77%)</b></td><td>428.40 <b>(+36.26%)</b></td><td>228.40 (-15.91%)</td><td>129.76 <b>(-82.56%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1976.00 (n/a)</td><td>646.80 (n/a)</td><td>314.40 (n/a)</td><td>271.60 (n/a)</td><td>743.85 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.55 (+3.63%)</td><td>0.37 (+5.32%)</td><td>0.30 (+11.06%)</td><td>0.24 (-2.97%)</td><td>0.13 (-2.73%)</td><td>556.10 (+3.06%)</td><td>392.98 (-6.26%)</td><td>434.80 (-9.96%)</td><td>238.30 (-3.48%)</td><td>129.18 (-8.52%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>539.60 (n/a)</td><td>419.24 (n/a)</td><td>482.90 (n/a)</td><td>246.90 (n/a)</td><td>141.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.48 (+5.71%)</td><td>0.37 (-5.23%)</td><td>0.36 (-3.31%)</td><td>0.21 <b>(-33.81%)</b></td><td>0.12 <b>(+119.98%)</b></td><td>623.30 <b>(+51.10%)</b></td><td>397.56 (+14.50%)</td><td>367.40 (+3.41%)</td><td>273.00 (-5.41%)</td><td>146.22 <b>(+202.38%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>412.50 (n/a)</td><td>347.20 (n/a)</td><td>355.30 (n/a)</td><td>288.60 (n/a)</td><td>48.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (+15.82%)</td><td>0.47 <b>(+20.12%)</b></td><td>0.52 (+17.41%)</td><td>0.23 (+2.85%)</td><td>0.14 <b>(+22.47%)</b></td><td>575.70 (-2.77%)</td><td>315.54 (-14.40%)</td><td>256.30 (-14.82%)</td><td>226.00 (-13.67%)</td><td>146.26 (+8.27%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.44 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>592.10 (n/a)</td><td>368.60 (n/a)</td><td>300.90 (n/a)</td><td>261.80 (n/a)</td><td>135.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-1.90%)</td><td>0.01 (+5.19%)</td><td>0.01 (+6.84%)</td><td>0.01 (+7.71%)</td><td>0.00 (-3.82%)</td><td>450.20 (-7.16%)</td><td>314.88 (-5.67%)</td><td>273.60 (-6.40%)</td><td>239.60 (+1.91%)</td><td>87.16 (-10.60%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.90 (n/a)</td><td>333.80 (n/a)</td><td>292.30 (n/a)</td><td>235.10 (n/a)</td><td>97.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (-12.48%)</td><td>0.01 (-7.00%)</td><td>0.01 (-3.88%)</td><td>0.01 (-11.06%)</td><td>0.00 (-10.94%)</td><td>614.70 (+12.42%)</td><td>372.76 (+7.98%)</td><td>307.70 (+4.02%)</td><td>224.70 (+14.29%)</td><td>156.38 (+15.02%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.80 (n/a)</td><td>345.22 (n/a)</td><td>295.80 (n/a)</td><td>196.60 (n/a)</td><td>135.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 (-13.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-40.00%)</b></td><td>23475.17 (-1.09%)</td><td>18258.74 (-0.96%)</td><td>20819.46 (-2.30%)</td><td>8681.71 <b>(+47.75%)</b></td><td>5942.38 (-19.91%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23734.84 (n/a)</td><td>18436.34 (n/a)</td><td>21309.47 (n/a)</td><td>5875.93 (n/a)</td><td>7419.25 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.00 <b>(+27.27%)</b></td><td>0.00 <b>(+70.00%)</b></td><td>0.00 <b>(+140.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+24.62%)</b></td><td>15945.70 <b>(-29.27%)</b></td><td>9039.86 <b>(-44.32%)</b></td><td>6868.75 <b>(-60.63%)</b></td><td>5761.33 <b>(-21.68%)</b></td><td>4151.98 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22543.35 (n/a)</td><td>16236.29 (n/a)</td><td>17448.61 (n/a)</td><td>7356.13 (n/a)</td><td>5983.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (-15.44%)</td><td>0.10 (-19.02%)</td><td>0.09 <b>(-29.01%)</b></td><td>0.07 (-11.00%)</td><td>0.02 <b>(-35.24%)</b></td><td>28824.41 (+12.41%)</td><td>22743.56 <b>(+20.03%)</b></td><td>22799.64 <b>(+40.86%)</b></td><td>16438.36 (+18.30%)</td><td>4401.45 (-17.97%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>25642.24 (n/a)</td><td>18948.67 (n/a)</td><td>16186.29 (n/a)</td><td>13895.47 (n/a)</td><td>5365.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.94 <b>(+83.66%)</b></td><td>1.92 <b>(+50.02%)</b></td><td>2.38 <b>(+72.25%)</b></td><td>0.30 <b>(-40.52%)</b></td><td>1.02 <b>(+131.28%)</b></td><td>3469.40 <b>(+68.12%)</b></td><td>1073.02 (+8.94%)</td><td>440.20 <b>(-41.95%)</b></td><td>357.00 <b>(-45.55%)</b></td><td>1344.31 <b>(+122.23%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.60 (n/a)</td><td>1.28 (n/a)</td><td>1.38 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>2063.70 (n/a)</td><td>985.00 (n/a)</td><td>758.30 (n/a)</td><td>655.70 (n/a)</td><td>604.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.97 (+3.61%)</td><td>2.42 <b>(+41.09%)</b></td><td>2.57 <b>(+63.80%)</b></td><td>1.18 (+3.14%)</td><td>0.73 (+8.05%)</td><td>889.90 (-3.04%)</td><td>488.18 <b>(-27.67%)</b></td><td>408.20 <b>(-38.96%)</b></td><td>352.50 (-3.50%)</td><td>227.19 (+10.66%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.87 (n/a)</td><td>1.71 (n/a)</td><td>1.57 (n/a)</td><td>1.14 (n/a)</td><td>0.68 (n/a)</td><td>917.80 (n/a)</td><td>674.96 (n/a)</td><td>668.70 (n/a)</td><td>365.30 (n/a)</td><td>205.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.80 <b>(-33.08%)</b></td><td>1.71 <b>(-36.14%)</b></td><td>1.42 <b>(-40.25%)</b></td><td>0.52 <b>(-69.59%)</b></td><td>0.96 (-7.37%)</td><td>2035.70 <b>(+228.82%)</b></td><td>882.16 <b>(+100.91%)</b></td><td>738.40 <b>(+67.36%)</b></td><td>375.00 <b>(+49.40%)</b></td><td>677.12 <b>(+338.15%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.18 (n/a)</td><td>2.67 (n/a)</td><td>2.38 (n/a)</td><td>1.69 (n/a)</td><td>1.03 (n/a)</td><td>619.10 (n/a)</td><td>439.08 (n/a)</td><td>441.20 (n/a)</td><td>251.00 (n/a)</td><td>154.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.54 <b>(+94.22%)</b></td><td>2.42 <b>(+77.83%)</b></td><td>2.61 <b>(+70.59%)</b></td><td>1.46 <b>(+149.75%)</b></td><td>0.83 <b>(+65.73%)</b></td><td>717.00 <b>(-59.96%)</b></td><td>478.88 <b>(-47.55%)</b></td><td>401.90 <b>(-41.38%)</b></td><td>296.00 <b>(-48.51%)</b></td><td>173.46 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.82 (n/a)</td><td>1.36 (n/a)</td><td>1.53 (n/a)</td><td>0.59 (n/a)</td><td>0.50 (n/a)</td><td>1790.70 (n/a)</td><td>913.06 (n/a)</td><td>685.60 (n/a)</td><td>574.90 (n/a)</td><td>506.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.87 (-12.16%)</td><td>2.11 <b>(-25.79%)</b></td><td>1.86 <b>(-35.62%)</b></td><td>0.58 <b>(-67.26%)</b></td><td>1.59 <b>(+42.66%)</b></td><td>3606.40 <b>(+205.39%)</b></td><td>1867.92 <b>(+123.51%)</b></td><td>1127.00 <b>(+55.32%)</b></td><td>541.70 (+13.85%)</td><td>1551.48 <b>(+378.59%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.41 (n/a)</td><td>2.85 (n/a)</td><td>2.89 (n/a)</td><td>1.78 (n/a)</td><td>1.12 (n/a)</td><td>1180.90 (n/a)</td><td>835.72 (n/a)</td><td>725.60 (n/a)</td><td>475.80 (n/a)</td><td>324.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.40 <b>(-47.34%)</b></td><td>1.49 <b>(-63.19%)</b></td><td>1.09 <b>(-78.12%)</b></td><td>0.58 (+3.51%)</td><td>1.17 <b>(-48.33%)</b></td><td>3599.90 (-3.39%)</td><td>2127.72 <b>(+92.40%)</b></td><td>1930.40 <b>(+357.01%)</b></td><td>617.60 <b>(+89.91%)</b></td><td>1301.76 (-11.40%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.45 (n/a)</td><td>4.06 (n/a)</td><td>4.96 (n/a)</td><td>0.56 (n/a)</td><td>2.26 (n/a)</td><td>3726.10 (n/a)</td><td>1105.86 (n/a)</td><td>422.40 (n/a)</td><td>325.20 (n/a)</td><td>1469.33 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>5.46 (-10.53%)</td><td>3.77 (+13.85%)</td><td>4.37 (+11.60%)</td><td>0.59 <b>(-38.42%)</b></td><td>1.98 (-4.34%)</td><td>3525.70 <b>(+62.39%)</b></td><td>1088.78 (+10.92%)</td><td>480.10 (-10.38%)</td><td>384.40 (+11.78%)</td><td>1366.39 <b>(+78.05%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.10 (n/a)</td><td>3.31 (n/a)</td><td>3.91 (n/a)</td><td>0.97 (n/a)</td><td>2.07 (n/a)</td><td>2171.10 (n/a)</td><td>981.60 (n/a)</td><td>535.70 (n/a)</td><td>343.90 (n/a)</td><td>767.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.43 <b>(+71.21%)</b></td><td>3.43 <b>(+81.47%)</b></td><td>2.70 <b>(+35.67%)</b></td><td>2.60 <b>(+335.53%)</b></td><td>1.68 <b>(+25.30%)</b></td><td>807.90 <b>(-77.04%)</b></td><td>691.14 <b>(-63.25%)</b></td><td>775.50 <b>(-26.29%)</b></td><td>326.00 <b>(-41.59%)</b></td><td>205.54 <b>(-86.01%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.76 (n/a)</td><td>1.89 (n/a)</td><td>1.99 (n/a)</td><td>0.60 (n/a)</td><td>1.34 (n/a)</td><td>3518.70 (n/a)</td><td>1880.84 (n/a)</td><td>1052.10 (n/a)</td><td>558.10 (n/a)</td><td>1468.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.80 (-2.80%)</td><td>2.00 <b>(-29.52%)</b></td><td>1.59 <b>(-47.40%)</b></td><td>0.62 <b>(-28.29%)</b></td><td>1.40 (+16.93%)</td><td>3359.00 <b>(+39.44%)</b></td><td>1665.82 <b>(+67.00%)</b></td><td>1322.90 <b>(+90.13%)</b></td><td>551.50 (+2.87%)</td><td>1201.34 <b>(+51.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.91 (n/a)</td><td>2.83 (n/a)</td><td>3.01 (n/a)</td><td>0.87 (n/a)</td><td>1.19 (n/a)</td><td>2408.90 (n/a)</td><td>997.48 (n/a)</td><td>695.80 (n/a)</td><td>536.10 (n/a)</td><td>794.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.34 (-0.73%)</td><td>4.38 (+9.98%)</td><td>3.63 (-8.83%)</td><td>2.69 <b>(+33.71%)</b></td><td>1.55 (-5.64%)</td><td>779.20 <b>(-25.21%)</b></td><td>529.00 (-13.36%)</td><td>577.70 (+9.68%)</td><td>330.60 (+0.73%)</td><td>182.79 <b>(-33.28%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.39 (n/a)</td><td>3.99 (n/a)</td><td>3.98 (n/a)</td><td>2.01 (n/a)</td><td>1.65 (n/a)</td><td>1041.90 (n/a)</td><td>610.54 (n/a)</td><td>526.70 (n/a)</td><td>328.20 (n/a)</td><td>273.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.90 (-7.89%)</td><td>3.29 (-11.85%)</td><td>2.73 <b>(-26.58%)</b></td><td>1.95 (-7.85%)</td><td>1.45 <b>(+26.83%)</b></td><td>2150.80 (+8.52%)</td><td>1484.86 <b>(+21.03%)</b></td><td>1537.40 <b>(+36.21%)</b></td><td>855.70 (+8.56%)</td><td>610.27 <b>(+35.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.32 (n/a)</td><td>3.74 (n/a)</td><td>3.72 (n/a)</td><td>2.12 (n/a)</td><td>1.15 (n/a)</td><td>1981.90 (n/a)</td><td>1226.82 (n/a)</td><td>1128.70 (n/a)</td><td>788.20 (n/a)</td><td>448.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>8.15 (+8.65%)</td><td>6.15 (-1.86%)</td><td>6.33 (+7.35%)</td><td>3.98 <b>(-31.34%)</b></td><td>1.51 <b>(+107.87%)</b></td><td>1054.90 <b>(+45.64%)</b></td><td>720.44 (+6.65%)</td><td>663.00 (-6.84%)</td><td>514.60 (-7.96%)</td><td>203.07 <b>(+188.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.50 (n/a)</td><td>6.27 (n/a)</td><td>5.89 (n/a)</td><td>5.79 (n/a)</td><td>0.73 (n/a)</td><td>724.30 (n/a)</td><td>675.52 (n/a)</td><td>711.70 (n/a)</td><td>559.10 (n/a)</td><td>70.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.63 (-12.39%)</td><td>5.29 (-19.35%)</td><td>5.90 (-19.27%)</td><td>1.94 <b>(-47.48%)</b></td><td>2.11 (-10.21%)</td><td>2164.20 <b>(+90.39%)</b></td><td>993.88 <b>(+37.31%)</b></td><td>710.50 <b>(+23.87%)</b></td><td>549.80 (+14.14%)</td><td>662.91 <b>(+122.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>8.71 (n/a)</td><td>6.56 (n/a)</td><td>7.31 (n/a)</td><td>3.69 (n/a)</td><td>2.35 (n/a)</td><td>1136.70 (n/a)</td><td>723.84 (n/a)</td><td>573.60 (n/a)</td><td>481.70 (n/a)</td><td>297.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>10.68 (+4.50%)</td><td>7.03 (-3.25%)</td><td>6.43 (-5.54%)</td><td>4.95 (-12.28%)</td><td>2.16 <b>(+24.14%)</b></td><td>847.90 (+14.00%)</td><td>635.76 (+5.91%)</td><td>651.80 (+5.86%)</td><td>392.90 (-4.29%)</td><td>163.48 <b>(+34.55%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>10.22 (n/a)</td><td>7.26 (n/a)</td><td>6.81 (n/a)</td><td>5.64 (n/a)</td><td>1.74 (n/a)</td><td>743.80 (n/a)</td><td>600.28 (n/a)</td><td>615.70 (n/a)</td><td>410.50 (n/a)</td><td>121.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>9.33 (-6.73%)</td><td>4.75 <b>(-27.41%)</b></td><td>4.15 <b>(-41.06%)</b></td><td>1.17 <b>(-72.52%)</b></td><td>3.40 <b>(+42.63%)</b></td><td>3575.60 <b>(+263.93%)</b></td><td>1526.82 <b>(+114.26%)</b></td><td>1011.60 <b>(+69.65%)</b></td><td>449.80 (+7.22%)</td><td>1295.03 <b>(+410.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>10.00 (n/a)</td><td>6.54 (n/a)</td><td>7.03 (n/a)</td><td>4.27 (n/a)</td><td>2.38 (n/a)</td><td>982.50 (n/a)</td><td>712.60 (n/a)</td><td>596.30 (n/a)</td><td>419.50 (n/a)</td><td>253.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>9.01 (-5.00%)</td><td>5.91 (-2.99%)</td><td>6.84 (+4.49%)</td><td>2.05 <b>(+75.03%)</b></td><td>2.90 (-4.22%)</td><td>2050.50 <b>(-42.87%)</b></td><td>952.44 (-19.78%)</td><td>613.30 (-4.29%)</td><td>465.50 (+5.25%)</td><td>662.40 <b>(-50.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>9.48 (n/a)</td><td>6.10 (n/a)</td><td>6.55 (n/a)</td><td>1.17 (n/a)</td><td>3.03 (n/a)</td><td>3589.00 (n/a)</td><td>1187.24 (n/a)</td><td>640.80 (n/a)</td><td>442.30 (n/a)</td><td>1345.29 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.63 (+1.61%)</td><td>1.20 <b>(+29.23%)</b></td><td>1.31 <b>(+85.04%)</b></td><td>0.72 <b>(+200.29%)</b></td><td>0.37 <b>(-33.04%)</b></td><td>726.00 <b>(-66.70%)</b></td><td>479.72 <b>(-45.35%)</b></td><td>398.70 <b>(-45.95%)</b></td><td>321.70 (-1.56%)</td><td>169.17 <b>(-77.61%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.60 (n/a)</td><td>0.93 (n/a)</td><td>0.71 (n/a)</td><td>0.24 (n/a)</td><td>0.56 (n/a)</td><td>2180.20 (n/a)</td><td>877.86 (n/a)</td><td>737.70 (n/a)</td><td>326.80 (n/a)</td><td>755.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.57 (+5.90%)</td><td>1.86 (+7.37%)</td><td>2.33 (+15.94%)</td><td>0.30 (-0.20%)</td><td>0.97 (+11.13%)</td><td>3462.90 (+0.20%)</td><td>1083.76 (-2.06%)</td><td>449.20 (-13.73%)</td><td>407.30 (-5.56%)</td><td>1335.12 (+1.36%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.43 (n/a)</td><td>1.73 (n/a)</td><td>2.01 (n/a)</td><td>0.30 (n/a)</td><td>0.87 (n/a)</td><td>3456.00 (n/a)</td><td>1106.50 (n/a)</td><td>520.70 (n/a)</td><td>431.30 (n/a)</td><td>1317.19 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.98 <b>(+29.95%)</b></td><td>2.51 <b>(+38.67%)</b></td><td>3.26 <b>(+51.20%)</b></td><td>0.61 (+3.73%)</td><td>1.54 <b>(+32.74%)</b></td><td>3415.80 (-3.59%)</td><td>1409.84 <b>(-25.85%)</b></td><td>643.90 <b>(-33.86%)</b></td><td>526.70 <b>(-23.05%)</b></td><td>1254.91 (-15.83%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.06 (n/a)</td><td>1.81 (n/a)</td><td>2.15 (n/a)</td><td>0.59 (n/a)</td><td>1.16 (n/a)</td><td>3543.10 (n/a)</td><td>1901.40 (n/a)</td><td>973.50 (n/a)</td><td>684.50 (n/a)</td><td>1490.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.25 <b>(-44.06%)</b></td><td>0.89 (-16.80%)</td><td>0.93 (+10.44%)</td><td>0.28 <b>(-60.62%)</b></td><td>0.38 <b>(-41.28%)</b></td><td>1881.80 <b>(+153.95%)</b></td><td>789.32 <b>(+34.23%)</b></td><td>563.50 (-9.45%)</td><td>420.80 <b>(+78.76%)</b></td><td>616.67 <b>(+199.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.23 (n/a)</td><td>1.07 (n/a)</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>741.00 (n/a)</td><td>588.02 (n/a)</td><td>622.30 (n/a)</td><td>235.40 (n/a)</td><td>205.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (+19.27%)</td><td>0.12 (+17.41%)</td><td>0.12 (-6.86%)</td><td>0.11 <b>(+109.06%)</b></td><td>0.02 <b>(-44.09%)</b></td><td>303.90 <b>(-52.16%)</b></td><td>273.08 <b>(-24.64%)</b></td><td>277.10 (+7.36%)</td><td>206.20 (-16.18%)</td><td>39.79 <b>(-76.65%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>635.30 (n/a)</td><td>362.38 (n/a)</td><td>258.10 (n/a)</td><td>246.00 (n/a)</td><td>170.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (-16.96%)</td><td>0.08 (-18.23%)</td><td>0.06 <b>(-44.79%)</b></td><td>0.05 (+16.06%)</td><td>0.03 <b>(-24.09%)</b></td><td>610.00 (-13.83%)</td><td>443.24 (+13.60%)</td><td>517.40 <b>(+81.16%)</b></td><td>262.80 <b>(+20.44%)</b></td><td>157.12 <b>(-23.96%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>707.90 (n/a)</td><td>390.16 (n/a)</td><td>285.60 (n/a)</td><td>218.20 (n/a)</td><td>206.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.23 (-9.28%)</td><td>0.16 (-2.51%)</td><td>0.14 <b>(-28.66%)</b></td><td>0.12 <b>(+364.87%)</b></td><td>0.04 <b>(-53.48%)</b></td><td>541.00 <b>(-78.49%)</b></td><td>436.78 <b>(-45.15%)</b></td><td>483.20 <b>(+40.18%)</b></td><td>289.40 (+10.21%)</td><td>100.73 <b>(-89.60%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>0.09 (n/a)</td><td>2514.80 (n/a)</td><td>796.38 (n/a)</td><td>344.70 (n/a)</td><td>262.60 (n/a)</td><td>968.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.21 <b>(-26.72%)</b></td><td>0.16 <b>(-26.24%)</b></td><td>0.15 <b>(-32.18%)</b></td><td>0.13 (+9.54%)</td><td>0.03 <b>(-51.03%)</b></td><td>488.60 (-8.72%)</td><td>421.10 <b>(+27.32%)</b></td><td>440.30 <b>(+47.45%)</b></td><td>305.90 <b>(+36.50%)</b></td><td>70.12 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>535.30 (n/a)</td><td>330.74 (n/a)</td><td>298.60 (n/a)</td><td>224.10 (n/a)</td><td>122.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (-12.59%)</td><td>0.17 (-11.75%)</td><td>0.16 (+9.06%)</td><td>0.13 (+10.64%)</td><td>0.04 <b>(-43.17%)</b></td><td>501.00 (-9.62%)</td><td>409.58 (+5.27%)</td><td>409.50 (-8.31%)</td><td>276.70 (+14.43%)</td><td>85.70 <b>(-38.26%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>554.30 (n/a)</td><td>389.06 (n/a)</td><td>446.60 (n/a)</td><td>241.80 (n/a)</td><td>138.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (+7.84%)</td><td>0.31 (+14.00%)</td><td>0.26 (+1.10%)</td><td>0.20 <b>(+272.24%)</b></td><td>0.13 (-17.09%)</td><td>663.00 <b>(-73.13%)</b></td><td>480.20 <b>(-42.89%)</b></td><td>505.70 (-1.10%)</td><td>290.10 (-7.29%)</td><td>180.05 <b>(-80.38%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>2467.80 (n/a)</td><td>840.90 (n/a)</td><td>511.30 (n/a)</td><td>312.90 (n/a)</td><td>917.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.44 (-18.52%)</td><td>0.33 (-9.75%)</td><td>0.31 (+1.91%)</td><td>0.21 (-16.82%)</td><td>0.10 <b>(-22.84%)</b></td><td>610.00 <b>(+20.24%)</b></td><td>426.22 (+9.14%)</td><td>421.50 (-1.86%)</td><td>294.80 <b>(+22.73%)</b></td><td>131.78 (+8.01%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>507.30 (n/a)</td><td>390.54 (n/a)</td><td>429.50 (n/a)</td><td>240.20 (n/a)</td><td>122.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (-17.48%)</td><td>0.33 (-11.99%)</td><td>0.29 (-2.30%)</td><td>0.28 (+9.10%)</td><td>0.07 <b>(-47.08%)</b></td><td>474.80 (-8.32%)</td><td>414.02 (+6.32%)</td><td>445.10 (+2.35%)</td><td>291.50 <b>(+21.21%)</b></td><td>72.89 <b>(-42.25%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>517.90 (n/a)</td><td>389.42 (n/a)</td><td>434.90 (n/a)</td><td>240.50 (n/a)</td><td>126.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (-2.60%)</td><td>0.05 (-5.87%)</td><td>0.04 <b>(-35.25%)</b></td><td>0.04 <b>(+38.80%)</b></td><td>0.01 (-14.90%)</td><td>462.60 <b>(-27.96%)</b></td><td>384.30 (+1.06%)</td><td>457.40 <b>(+54.42%)</b></td><td>264.10 (+2.68%)</td><td>104.22 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>642.10 (n/a)</td><td>380.26 (n/a)</td><td>296.20 (n/a)</td><td>257.20 (n/a)</td><td>161.85 (n/a)</td>
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
