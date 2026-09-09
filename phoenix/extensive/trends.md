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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+8.80%)</td><td>0.02 <b>(+27.75%)</b></td><td>0.02 (+9.76%)</td><td>0.02 <b>(+90.90%)</b></td><td>0.00 <b>(-65.66%)</b></td><td>303.80 <b>(-47.62%)</b></td><td>267.78 <b>(-29.33%)</b></td><td>270.70 (-8.89%)</td><td>236.70 (-8.08%)</td><td>24.52 <b>(-83.26%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.00 (n/a)</td><td>378.90 (n/a)</td><td>297.10 (n/a)</td><td>257.50 (n/a)</td><td>146.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+2.05%)</td><td>0.02 (+12.06%)</td><td>0.02 <b>(+51.21%)</b></td><td>0.01 (+5.55%)</td><td>0.01 (+0.96%)</td><td>485.10 (-5.25%)</td><td>334.16 (-10.90%)</td><td>261.90 <b>(-33.88%)</b></td><td>231.10 (-1.99%)</td><td>126.66 (-3.08%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.00 (n/a)</td><td>375.04 (n/a)</td><td>396.10 (n/a)</td><td>235.80 (n/a)</td><td>130.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+11.56%)</td><td>0.01 (-9.27%)</td><td>0.01 (-16.07%)</td><td>0.01 (+9.42%)</td><td>0.01 (+10.64%)</td><td>580.90 (-8.61%)</td><td>477.82 (+10.61%)</td><td>548.40 (+19.17%)</td><td>240.10 (-10.38%)</td><td>141.78 (-7.11%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.60 (n/a)</td><td>431.98 (n/a)</td><td>460.20 (n/a)</td><td>267.90 (n/a)</td><td>152.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+44.91%)</b></td><td>0.02 <b>(+37.77%)</b></td><td>0.01 (+12.35%)</td><td>0.01 (+3.53%)</td><td>0.01 <b>(+101.50%)</b></td><td>490.10 (-3.41%)</td><td>357.88 (-19.85%)</td><td>432.10 (-11.00%)</td><td>184.20 <b>(-30.99%)</b></td><td>141.34 <b>(+40.09%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.40 (n/a)</td><td>446.50 (n/a)</td><td>485.50 (n/a)</td><td>266.90 (n/a)</td><td>100.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-8.85%)</td><td>0.02 (-10.63%)</td><td>0.01 <b>(-33.44%)</b></td><td>0.01 (+2.45%)</td><td>0.01 (-5.92%)</td><td>592.50 (-2.39%)</td><td>424.44 (+10.61%)</td><td>470.70 <b>(+50.24%)</b></td><td>278.40 (+9.69%)</td><td>140.14 (-6.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.00 (n/a)</td><td>383.74 (n/a)</td><td>313.30 (n/a)</td><td>253.80 (n/a)</td><td>149.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(-30.79%)</b></td><td>0.02 <b>(+44.47%)</b></td><td>0.02 <b>(+99.97%)</b></td><td>0.02 <b>(+168.74%)</b></td><td>0.00 <b>(-85.17%)</b></td><td>280.60 <b>(-62.80%)</b></td><td>262.96 <b>(-47.17%)</b></td><td>267.70 <b>(-49.99%)</b></td><td>235.00 <b>(+44.53%)</b></td><td>19.46 <b>(-90.91%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>754.20 (n/a)</td><td>497.76 (n/a)</td><td>535.30 (n/a)</td><td>162.60 (n/a)</td><td>214.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(-31.40%)</b></td><td>0.02 <b>(-51.82%)</b></td><td>0.02 <b>(-53.41%)</b></td><td>0.01 <b>(-77.82%)</b></td><td>0.01 (+11.03%)</td><td>1835.30 <b>(+350.82%)</b></td><td>772.50 <b>(+172.03%)</b></td><td>581.30 <b>(+114.66%)</b></td><td>334.20 <b>(+45.75%)</b></td><td>602.89 <b>(+725.95%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>407.10 (n/a)</td><td>283.98 (n/a)</td><td>270.80 (n/a)</td><td>229.30 (n/a)</td><td>72.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (-5.08%)</td><td>0.04 (+2.12%)</td><td>0.04 (-7.27%)</td><td>0.03 <b>(+45.71%)</b></td><td>0.01 <b>(-33.05%)</b></td><td>426.80 <b>(-31.36%)</b></td><td>336.32 (-9.20%)</td><td>309.90 (+7.87%)</td><td>266.10 (+5.39%)</td><td>76.69 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>621.80 (n/a)</td><td>370.40 (n/a)</td><td>287.30 (n/a)</td><td>252.50 (n/a)</td><td>156.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 <b>(+23.04%)</b></td><td>0.04 (+13.66%)</td><td>0.05 (+0.24%)</td><td>0.02 (+14.94%)</td><td>0.02 (+17.08%)</td><td>494.30 (-12.99%)</td><td>317.88 (-12.31%)</td><td>266.70 (-0.22%)</td><td>192.00 (-18.75%)</td><td>128.92 (-15.58%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>362.50 (n/a)</td><td>267.30 (n/a)</td><td>236.30 (n/a)</td><td>152.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (-13.58%)</td><td>0.03 <b>(-21.25%)</b></td><td>0.03 <b>(-40.17%)</b></td><td>0.02 (-18.70%)</td><td>0.01 (-9.91%)</td><td>588.10 <b>(+23.01%)</b></td><td>423.06 <b>(+28.22%)</b></td><td>437.30 <b>(+67.16%)</b></td><td>266.20 (+15.69%)</td><td>146.78 <b>(+23.77%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.10 (n/a)</td><td>329.94 (n/a)</td><td>261.60 (n/a)</td><td>230.10 (n/a)</td><td>118.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (-17.75%)</td><td>0.04 (+1.72%)</td><td>0.04 (+13.51%)</td><td>0.03 <b>(+20.38%)</b></td><td>0.01 <b>(-29.88%)</b></td><td>454.70 (-16.93%)</td><td>344.90 (-6.71%)</td><td>285.60 (-11.88%)</td><td>247.90 <b>(+21.58%)</b></td><td>101.13 <b>(-25.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.40 (n/a)</td><td>369.72 (n/a)</td><td>324.10 (n/a)</td><td>203.90 (n/a)</td><td>136.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (+18.17%)</td><td>0.03 (-7.89%)</td><td>0.03 (-1.38%)</td><td>0.02 (-9.57%)</td><td>0.02 <b>(+25.22%)</b></td><td>522.10 (+10.57%)</td><td>417.98 (+11.72%)</td><td>441.20 (+1.40%)</td><td>205.20 (-15.35%)</td><td>123.58 (+9.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>472.20 (n/a)</td><td>374.14 (n/a)</td><td>435.10 (n/a)</td><td>242.40 (n/a)</td><td>113.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (-4.11%)</td><td>0.07 (-19.33%)</td><td>0.05 <b>(-43.48%)</b></td><td>0.04 (+8.75%)</td><td>0.03 (+4.81%)</td><td>546.20 (-8.05%)</td><td>408.38 <b>(+23.86%)</b></td><td>472.30 <b>(+76.96%)</b></td><td>248.60 (+4.28%)</td><td>140.25 (-6.24%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.00 (n/a)</td><td>329.72 (n/a)</td><td>266.90 (n/a)</td><td>238.40 (n/a)</td><td>149.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+14.87%)</td><td>0.08 (+11.42%)</td><td>0.08 (+17.68%)</td><td>0.05 (+7.37%)</td><td>0.02 <b>(+23.69%)</b></td><td>521.30 (-6.86%)</td><td>348.72 (-8.91%)</td><td>300.70 (-15.03%)</td><td>239.90 (-12.95%)</td><td>113.75 (+1.00%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.70 (n/a)</td><td>382.84 (n/a)</td><td>353.90 (n/a)</td><td>275.60 (n/a)</td><td>112.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (-16.81%)</td><td>0.07 (-15.92%)</td><td>0.05 <b>(-34.97%)</b></td><td>0.04 (-2.25%)</td><td>0.03 (-17.69%)</td><td>582.10 (+2.28%)</td><td>426.40 (+16.05%)</td><td>491.40 <b>(+53.75%)</b></td><td>226.60 <b>(+20.21%)</b></td><td>157.59 (-1.22%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>569.10 (n/a)</td><td>367.42 (n/a)</td><td>319.60 (n/a)</td><td>188.50 (n/a)</td><td>159.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+1.71%)</td><td>0.08 (-3.99%)</td><td>0.08 (-0.12%)</td><td>0.05 (-7.42%)</td><td>0.02 <b>(+23.60%)</b></td><td>511.70 (+8.02%)</td><td>358.66 (+8.20%)</td><td>296.30 (+0.14%)</td><td>237.20 (-1.66%)</td><td>127.17 <b>(+35.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>473.70 (n/a)</td><td>331.48 (n/a)</td><td>295.90 (n/a)</td><td>241.20 (n/a)</td><td>93.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (-18.58%)</td><td>0.04 (-12.42%)</td><td>0.04 (-4.13%)</td><td>0.02 <b>(+33.07%)</b></td><td>0.02 <b>(-44.00%)</b></td><td>1463.70 <b>(-24.86%)</b></td><td>716.74 (-14.18%)</td><td>605.70 (+4.31%)</td><td>371.70 <b>(+22.84%)</b></td><td>429.91 <b>(-37.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1947.90 (n/a)</td><td>835.16 (n/a)</td><td>580.70 (n/a)</td><td>302.60 (n/a)</td><td>690.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+15.37%)</td><td>0.07 (+0.57%)</td><td>0.05 <b>(-22.46%)</b></td><td>0.04 (+1.50%)</td><td>0.03 <b>(+38.24%)</b></td><td>567.80 (-1.47%)</td><td>420.50 (+4.24%)</td><td>500.50 <b>(+28.96%)</b></td><td>241.40 (-13.32%)</td><td>149.08 (+19.81%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.30 (n/a)</td><td>403.38 (n/a)</td><td>388.10 (n/a)</td><td>278.50 (n/a)</td><td>124.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (-17.53%)</td><td>0.14 (-7.52%)</td><td>0.11 (-6.00%)</td><td>0.10 (+8.32%)</td><td>0.04 <b>(-29.37%)</b></td><td>489.50 (-7.68%)</td><td>387.62 (+2.70%)</td><td>453.00 (+6.39%)</td><td>266.30 <b>(+21.27%)</b></td><td>108.32 <b>(-20.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>530.20 (n/a)</td><td>377.42 (n/a)</td><td>425.80 (n/a)</td><td>219.60 (n/a)</td><td>136.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 <b>(-30.53%)</b></td><td>0.11 (-6.33%)</td><td>0.11 (+12.90%)</td><td>0.09 <b>(+20.71%)</b></td><td>0.02 <b>(-66.26%)</b></td><td>531.80 (-17.17%)</td><td>463.22 (-2.56%)</td><td>442.40 (-11.41%)</td><td>378.80 <b>(+43.98%)</b></td><td>64.20 <b>(-59.20%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>642.00 (n/a)</td><td>475.38 (n/a)</td><td>499.40 (n/a)</td><td>263.10 (n/a)</td><td>157.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.21 (+12.65%)</td><td>0.13 (-16.18%)</td><td>0.16 (-6.68%)</td><td>0.03 <b>(-78.39%)</b></td><td>0.08 <b>(+154.99%)</b></td><td>1898.50 <b>(+362.82%)</b></td><td>658.36 <b>(+108.54%)</b></td><td>302.70 (+7.15%)</td><td>231.80 (-11.26%)</td><td>709.18 <b>(+971.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>410.20 (n/a)</td><td>315.70 (n/a)</td><td>282.50 (n/a)</td><td>261.20 (n/a)</td><td>66.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.22 (+10.89%)</td><td>0.13 (-9.12%)</td><td>0.11 (-3.11%)</td><td>0.08 (-17.16%)</td><td>0.06 (+4.45%)</td><td>646.10 <b>(+20.72%)</b></td><td>437.66 (+11.36%)</td><td>458.80 (+3.19%)</td><td>220.30 (-9.82%)</td><td>153.91 (+12.47%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>535.20 (n/a)</td><td>393.02 (n/a)</td><td>444.60 (n/a)</td><td>244.30 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (-17.20%)</td><td>0.14 (-14.96%)</td><td>0.12 <b>(-40.08%)</b></td><td>0.09 (+16.82%)</td><td>0.05 <b>(-35.89%)</b></td><td>533.50 (-14.39%)</td><td>391.14 (+4.82%)</td><td>408.80 <b>(+66.86%)</b></td><td>254.00 <b>(+20.78%)</b></td><td>123.06 <b>(-36.75%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>623.20 (n/a)</td><td>373.14 (n/a)</td><td>245.00 (n/a)</td><td>210.30 (n/a)</td><td>194.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.21 (+7.13%)</td><td>0.13 (-14.35%)</td><td>0.11 <b>(-32.41%)</b></td><td>0.10 (-0.56%)</td><td>0.04 <b>(+20.86%)</b></td><td>480.10 (+0.57%)</td><td>403.90 (+18.47%)</td><td>436.10 <b>(+47.93%)</b></td><td>235.30 (-6.66%)</td><td>96.49 (+5.85%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>477.40 (n/a)</td><td>340.92 (n/a)</td><td>294.80 (n/a)</td><td>252.10 (n/a)</td><td>91.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (-12.37%)</td><td>0.01 (+3.82%)</td><td>0.01 (-2.10%)</td><td>0.01 <b>(+32.54%)</b></td><td>0.00 <b>(-48.08%)</b></td><td>417.60 <b>(-24.54%)</b></td><td>307.90 (-11.91%)</td><td>293.20 (+2.16%)</td><td>245.50 (+14.13%)</td><td>64.59 <b>(-54.11%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>553.40 (n/a)</td><td>349.54 (n/a)</td><td>287.00 (n/a)</td><td>215.10 (n/a)</td><td>140.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (+19.13%)</td><td>0.01 <b>(+38.94%)</b></td><td>0.01 <b>(+41.73%)</b></td><td>0.01 (+14.06%)</td><td>0.00 <b>(+29.10%)</b></td><td>503.60 (-12.33%)</td><td>311.44 <b>(-26.63%)</b></td><td>292.40 <b>(-29.46%)</b></td><td>225.90 (-16.05%)</td><td>111.64 (+2.30%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>574.40 (n/a)</td><td>424.46 (n/a)</td><td>414.50 (n/a)</td><td>269.10 (n/a)</td><td>109.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (-9.12%)</td><td>0.01 (+4.33%)</td><td>0.01 <b>(+25.62%)</b></td><td>0.00 (+2.15%)</td><td>0.00 (-7.97%)</td><td>543.50 (-2.09%)</td><td>406.26 (-4.10%)</td><td>348.20 <b>(-20.39%)</b></td><td>296.90 (+10.04%)</td><td>109.75 (+7.41%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>555.10 (n/a)</td><td>423.62 (n/a)</td><td>437.40 (n/a)</td><td>269.80 (n/a)</td><td>102.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(+20.52%)</b></td><td>0.01 (+6.25%)</td><td>0.01 (-6.74%)</td><td>0.00 (-6.27%)</td><td>0.00 <b>(+34.38%)</b></td><td>582.20 (+6.69%)</td><td>388.68 (-1.99%)</td><td>392.50 (+7.24%)</td><td>226.90 (-17.01%)</td><td>146.37 (+16.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>545.70 (n/a)</td><td>396.58 (n/a)</td><td>366.00 (n/a)</td><td>273.40 (n/a)</td><td>126.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (+6.49%)</td><td>0.01 <b>(+49.31%)</b></td><td>0.01 <b>(+29.12%)</b></td><td>0.00 <b>(+244.57%)</b></td><td>0.00 <b>(-32.71%)</b></td><td>568.00 <b>(-70.98%)</b></td><td>425.78 <b>(-51.71%)</b></td><td>438.40 <b>(-22.56%)</b></td><td>280.60 (-6.09%)</td><td>114.70 <b>(-82.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1957.10 (n/a)</td><td>881.66 (n/a)</td><td>566.10 (n/a)</td><td>298.80 (n/a)</td><td>655.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(+24.09%)</b></td><td>0.01 (+3.35%)</td><td>0.00 (-7.40%)</td><td>0.00 (-7.05%)</td><td>0.00 <b>(+64.22%)</b></td><td>598.10 (+7.57%)</td><td>482.94 (+2.92%)</td><td>543.90 (+7.98%)</td><td>239.10 (-19.41%)</td><td>142.03 <b>(+40.97%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>556.00 (n/a)</td><td>469.24 (n/a)</td><td>503.70 (n/a)</td><td>296.70 (n/a)</td><td>100.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-7.35%)</td><td>0.01 (-3.05%)</td><td>0.01 (-8.70%)</td><td>0.01 <b>(-38.33%)</b></td><td>0.01 (+13.85%)</td><td>926.30 <b>(+62.14%)</b></td><td>496.60 (+15.63%)</td><td>484.40 (+9.52%)</td><td>242.90 (+7.96%)</td><td>269.89 <b>(+105.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.30 (n/a)</td><td>429.46 (n/a)</td><td>442.30 (n/a)</td><td>225.00 (n/a)</td><td>131.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-7.97%)</td><td>0.02 <b>(+51.37%)</b></td><td>0.02 <b>(+70.50%)</b></td><td>0.01 <b>(+308.65%)</b></td><td>0.00 <b>(-45.74%)</b></td><td>472.50 <b>(-75.53%)</b></td><td>326.22 <b>(-56.69%)</b></td><td>292.70 <b>(-41.35%)</b></td><td>248.80 (+8.65%)</td><td>91.10 <b>(-86.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1930.90 (n/a)</td><td>753.22 (n/a)</td><td>499.10 (n/a)</td><td>229.00 (n/a)</td><td>677.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+24.39%)</b></td><td>0.02 <b>(+32.23%)</b></td><td>0.02 <b>(+30.57%)</b></td><td>0.01 <b>(+29.11%)</b></td><td>0.01 (+6.32%)</td><td>476.70 <b>(-22.55%)</b></td><td>275.72 <b>(-26.69%)</b></td><td>231.90 <b>(-23.39%)</b></td><td>185.90 (-19.63%)</td><td>115.05 <b>(-28.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.50 (n/a)</td><td>376.08 (n/a)</td><td>302.70 (n/a)</td><td>231.30 (n/a)</td><td>161.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-6.76%)</td><td>0.01 (-11.98%)</td><td>0.01 (-2.90%)</td><td>0.01 (-5.65%)</td><td>0.00 (-16.25%)</td><td>548.80 (+5.99%)</td><td>442.14 (+10.97%)</td><td>482.60 (+2.97%)</td><td>250.60 (+7.28%)</td><td>124.21 (-6.58%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.80 (n/a)</td><td>398.44 (n/a)</td><td>468.70 (n/a)</td><td>233.60 (n/a)</td><td>132.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+40.12%)</b></td><td>0.02 <b>(+37.66%)</b></td><td>0.02 <b>(+62.54%)</b></td><td>0.01 (+2.86%)</td><td>0.01 <b>(+58.27%)</b></td><td>615.00 (-2.78%)</td><td>370.30 <b>(-21.21%)</b></td><td>303.90 <b>(-38.47%)</b></td><td>172.60 <b>(-28.65%)</b></td><td>180.67 (+13.98%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.60 (n/a)</td><td>469.96 (n/a)</td><td>493.90 (n/a)</td><td>241.90 (n/a)</td><td>158.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+17.41%)</td><td>0.01 <b>(+27.66%)</b></td><td>0.01 <b>(+30.64%)</b></td><td>0.01 (-4.20%)</td><td>0.01 <b>(+52.12%)</b></td><td>655.80 (+4.38%)</td><td>422.18 (-16.79%)</td><td>414.30 <b>(-23.46%)</b></td><td>260.50 (-14.84%)</td><td>166.57 <b>(+32.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.30 (n/a)</td><td>507.38 (n/a)</td><td>541.30 (n/a)</td><td>305.90 (n/a)</td><td>125.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(+30.04%)</b></td><td>0.04 <b>(+37.22%)</b></td><td>0.04 <b>(+70.38%)</b></td><td>0.02 (+17.38%)</td><td>0.01 (+10.28%)</td><td>464.80 (-14.81%)</td><td>314.18 <b>(-28.05%)</b></td><td>296.70 <b>(-41.32%)</b></td><td>225.80 <b>(-23.09%)</b></td><td>90.27 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.60 (n/a)</td><td>436.66 (n/a)</td><td>505.60 (n/a)</td><td>293.60 (n/a)</td><td>119.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(+33.52%)</b></td><td>0.03 (+17.04%)</td><td>0.03 <b>(+34.75%)</b></td><td>0.02 (+0.02%)</td><td>0.01 <b>(+31.83%)</b></td><td>601.60 (-0.02%)</td><td>405.92 (-12.13%)</td><td>406.70 <b>(-25.78%)</b></td><td>206.00 <b>(-25.09%)</b></td><td>161.11 (-1.21%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.70 (n/a)</td><td>461.98 (n/a)</td><td>548.00 (n/a)</td><td>275.00 (n/a)</td><td>163.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (-18.53%)</td><td>0.02 <b>(-25.50%)</b></td><td>0.02 <b>(-38.69%)</b></td><td>0.02 (-7.29%)</td><td>0.01 <b>(-38.36%)</b></td><td>568.70 (+7.87%)</td><td>440.62 <b>(+28.26%)</b></td><td>456.80 <b>(+63.14%)</b></td><td>296.90 <b>(+22.74%)</b></td><td>98.00 <b>(-20.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.20 (n/a)</td><td>343.54 (n/a)</td><td>280.00 (n/a)</td><td>241.90 (n/a)</td><td>123.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(-20.78%)</b></td><td>0.02 (-7.30%)</td><td>0.02 (+7.82%)</td><td>0.01 (-6.17%)</td><td>0.01 <b>(-31.09%)</b></td><td>765.20 (+6.57%)</td><td>512.00 (+2.35%)</td><td>475.90 (-7.27%)</td><td>270.80 <b>(+26.25%)</b></td><td>179.75 (-1.92%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>718.00 (n/a)</td><td>500.26 (n/a)</td><td>513.20 (n/a)</td><td>214.50 (n/a)</td><td>183.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(-21.07%)</b></td><td>0.03 (-11.26%)</td><td>0.03 (+10.96%)</td><td>0.02 (+6.99%)</td><td>0.01 <b>(-45.84%)</b></td><td>571.60 (-6.54%)</td><td>442.06 (+3.16%)</td><td>416.20 (-9.87%)</td><td>300.50 <b>(+26.69%)</b></td><td>109.55 <b>(-34.08%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.60 (n/a)</td><td>428.52 (n/a)</td><td>461.80 (n/a)</td><td>237.20 (n/a)</td><td>166.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-36.37%)</b></td><td>0.02 (-17.30%)</td><td>0.02 (-1.72%)</td><td>0.01 <b>(-24.55%)</b></td><td>0.00 <b>(-55.56%)</b></td><td>790.70 <b>(+32.53%)</b></td><td>590.36 (+15.98%)</td><td>572.50 (+1.74%)</td><td>452.40 <b>(+57.14%)</b></td><td>124.40 (-1.91%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>596.60 (n/a)</td><td>509.02 (n/a)</td><td>562.70 (n/a)</td><td>287.90 (n/a)</td><td>126.82 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 <b>(+23.11%)</b></td><td>0.06 (+7.43%)</td><td>0.07 (-0.25%)</td><td>0.04 (+19.28%)</td><td>0.02 <b>(+21.36%)</b></td><td>546.20 (-16.16%)</td><td>366.54 (-6.44%)</td><td>299.70 (+0.27%)</td><td>221.20 (-18.77%)</td><td>139.11 (-13.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.50 (n/a)</td><td>391.76 (n/a)</td><td>298.90 (n/a)</td><td>272.30 (n/a)</td><td>160.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (-18.35%)</td><td>0.06 (-7.51%)</td><td>0.04 <b>(-31.49%)</b></td><td>0.04 <b>(+22.83%)</b></td><td>0.02 <b>(-23.95%)</b></td><td>535.10 (-18.59%)</td><td>404.78 (+0.35%)</td><td>485.80 <b>(+45.97%)</b></td><td>241.40 <b>(+22.48%)</b></td><td>138.80 <b>(-27.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>657.30 (n/a)</td><td>403.36 (n/a)</td><td>332.80 (n/a)</td><td>197.10 (n/a)</td><td>191.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+13.20%)</td><td>0.07 (+4.65%)</td><td>0.07 (+1.96%)</td><td>0.04 (-12.42%)</td><td>0.03 <b>(+29.81%)</b></td><td>557.60 (+14.17%)</td><td>357.50 (+0.22%)</td><td>299.40 (-1.93%)</td><td>201.80 (-11.65%)</td><td>144.15 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>488.40 (n/a)</td><td>356.72 (n/a)</td><td>305.30 (n/a)</td><td>228.40 (n/a)</td><td>112.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 <b>(-26.69%)</b></td><td>0.05 <b>(-26.18%)</b></td><td>0.05 <b>(-34.44%)</b></td><td>0.02 <b>(-47.00%)</b></td><td>0.02 (-18.15%)</td><td>1019.50 <b>(+88.69%)</b></td><td>521.52 <b>(+45.07%)</b></td><td>458.50 <b>(+52.53%)</b></td><td>297.80 <b>(+36.42%)</b></td><td>290.53 <b>(+110.19%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>540.30 (n/a)</td><td>359.50 (n/a)</td><td>300.60 (n/a)</td><td>218.30 (n/a)</td><td>138.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 <b>(-28.27%)</b></td><td>0.05 <b>(-26.97%)</b></td><td>0.04 <b>(-33.87%)</b></td><td>0.04 (-11.58%)</td><td>0.01 <b>(-43.82%)</b></td><td>579.50 (+13.10%)</td><td>468.64 <b>(+28.87%)</b></td><td>475.90 <b>(+51.22%)</b></td><td>303.30 <b>(+39.45%)</b></td><td>115.98 (-16.39%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>512.40 (n/a)</td><td>363.64 (n/a)</td><td>314.70 (n/a)</td><td>217.50 (n/a)</td><td>138.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 <b>(+70.99%)</b></td><td>0.05 (+19.39%)</td><td>0.04 (+5.82%)</td><td>0.03 (-4.97%)</td><td>0.03 <b>(+173.64%)</b></td><td>641.30 (+5.23%)</td><td>478.90 (-6.60%)</td><td>521.40 (-5.49%)</td><td>217.30 <b>(-41.51%)</b></td><td>162.71 <b>(+55.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>512.76 (n/a)</td><td>551.70 (n/a)</td><td>371.50 (n/a)</td><td>104.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>343.70 (n/a)</td><td>255.26 (n/a)</td><td>242.80 (n/a)</td><td>173.90 (n/a)</td><td>62.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.90 (n/a)</td><td>406.44 (n/a)</td><td>407.10 (n/a)</td><td>267.10 (n/a)</td><td>95.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.80 (n/a)</td><td>404.56 (n/a)</td><td>424.70 (n/a)</td><td>256.90 (n/a)</td><td>125.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>405.60 (n/a)</td><td>298.70 (n/a)</td><td>276.30 (n/a)</td><td>241.20 (n/a)</td><td>63.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.80 (n/a)</td><td>360.70 (n/a)</td><td>287.00 (n/a)</td><td>236.10 (n/a)</td><td>129.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.10 (n/a)</td><td>387.60 (n/a)</td><td>451.00 (n/a)</td><td>246.40 (n/a)</td><td>116.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>482.50 (n/a)</td><td>362.54 (n/a)</td><td>297.90 (n/a)</td><td>285.30 (n/a)</td><td>100.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>443.30 (n/a)</td><td>389.80 (n/a)</td><td>426.80 (n/a)</td><td>313.30 (n/a)</td><td>61.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>622.30 (n/a)</td><td>376.38 (n/a)</td><td>311.80 (n/a)</td><td>240.40 (n/a)</td><td>161.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (-12.49%)</td><td>0.13 (-9.05%)</td><td>0.12 <b>(-23.46%)</b></td><td>0.09 (+10.45%)</td><td>0.05 (-10.11%)</td><td>559.00 (-9.46%)</td><td>409.30 (+7.92%)</td><td>407.90 <b>(+30.65%)</b></td><td>262.40 (+14.29%)</td><td>140.30 (-9.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>617.40 (n/a)</td><td>379.26 (n/a)</td><td>312.20 (n/a)</td><td>229.60 (n/a)</td><td>154.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>537.70 (n/a)</td><td>387.20 (n/a)</td><td>380.40 (n/a)</td><td>245.10 (n/a)</td><td>137.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1097.40 (n/a)</td><td>515.18 (n/a)</td><td>409.30 (n/a)</td><td>278.50 (n/a)</td><td>337.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.40 (n/a)</td><td>336.60 (n/a)</td><td>280.80 (n/a)</td><td>256.50 (n/a)</td><td>90.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.60 (n/a)</td><td>348.50 (n/a)</td><td>257.90 (n/a)</td><td>236.30 (n/a)</td><td>138.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>360.30 (n/a)</td><td>299.48 (n/a)</td><td>294.40 (n/a)</td><td>265.50 (n/a)</td><td>37.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>364.70 (n/a)</td><td>285.66 (n/a)</td><td>288.90 (n/a)</td><td>232.30 (n/a)</td><td>52.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>992.60 (n/a)</td><td>571.70 (n/a)</td><td>543.90 (n/a)</td><td>256.60 (n/a)</td><td>264.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>631.30 (n/a)</td><td>542.68 (n/a)</td><td>617.90 (n/a)</td><td>297.90 (n/a)</td><td>141.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>521.00 (n/a)</td><td>343.24 (n/a)</td><td>304.70 (n/a)</td><td>203.00 (n/a)</td><td>132.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1088.30 (n/a)</td><td>574.14 (n/a)</td><td>524.50 (n/a)</td><td>242.00 (n/a)</td><td>316.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>297.00 (n/a)</td><td>245.80 (n/a)</td><td>249.20 (n/a)</td><td>200.20 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>655.40 (n/a)</td><td>424.72 (n/a)</td><td>417.90 (n/a)</td><td>257.90 (n/a)</td><td>171.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>618.90 (n/a)</td><td>455.18 (n/a)</td><td>443.80 (n/a)</td><td>292.60 (n/a)</td><td>126.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.40 (n/a)</td><td>358.84 (n/a)</td><td>362.20 (n/a)</td><td>240.50 (n/a)</td><td>110.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1044.40 (n/a)</td><td>593.62 (n/a)</td><td>553.50 (n/a)</td><td>268.90 (n/a)</td><td>281.72 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.60 (n/a)</td><td>382.74 (n/a)</td><td>386.90 (n/a)</td><td>239.80 (n/a)</td><td>87.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>448.90 (n/a)</td><td>281.14 (n/a)</td><td>244.00 (n/a)</td><td>149.30 (n/a)</td><td>111.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.30 (n/a)</td><td>356.02 (n/a)</td><td>294.70 (n/a)</td><td>244.10 (n/a)</td><td>125.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.70 (n/a)</td><td>427.74 (n/a)</td><td>368.40 (n/a)</td><td>305.60 (n/a)</td><td>123.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.50 (n/a)</td><td>317.88 (n/a)</td><td>280.60 (n/a)</td><td>243.60 (n/a)</td><td>78.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>431.28 (n/a)</td><td>485.20 (n/a)</td><td>245.70 (n/a)</td><td>146.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.50 (n/a)</td><td>326.02 (n/a)</td><td>286.50 (n/a)</td><td>248.20 (n/a)</td><td>121.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2426.50 (n/a)</td><td>992.82 (n/a)</td><td>518.30 (n/a)</td><td>464.80 (n/a)</td><td>837.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.50 (n/a)</td><td>487.22 (n/a)</td><td>488.20 (n/a)</td><td>408.50 (n/a)</td><td>52.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.30 (n/a)</td><td>465.40 (n/a)</td><td>478.40 (n/a)</td><td>244.60 (n/a)</td><td>149.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.00 (n/a)</td><td>438.90 (n/a)</td><td>463.60 (n/a)</td><td>277.70 (n/a)</td><td>152.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.20 (n/a)</td><td>329.22 (n/a)</td><td>302.50 (n/a)</td><td>186.30 (n/a)</td><td>114.33 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.40 (n/a)</td><td>441.68 (n/a)</td><td>423.80 (n/a)</td><td>259.50 (n/a)</td><td>126.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.60 (n/a)</td><td>363.54 (n/a)</td><td>243.60 (n/a)</td><td>211.20 (n/a)</td><td>180.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.30 (n/a)</td><td>370.64 (n/a)</td><td>351.90 (n/a)</td><td>236.90 (n/a)</td><td>143.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>492.60 (n/a)</td><td>401.78 (n/a)</td><td>469.30 (n/a)</td><td>264.00 (n/a)</td><td>105.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1080.50 (n/a)</td><td>515.88 (n/a)</td><td>401.60 (n/a)</td><td>278.20 (n/a)</td><td>322.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.30 (n/a)</td><td>316.94 (n/a)</td><td>274.20 (n/a)</td><td>217.20 (n/a)</td><td>115.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>639.60 (n/a)</td><td>430.14 (n/a)</td><td>442.00 (n/a)</td><td>279.50 (n/a)</td><td>151.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1921.30 (n/a)</td><td>629.18 (n/a)</td><td>300.70 (n/a)</td><td>185.10 (n/a)</td><td>728.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>627.20 (n/a)</td><td>440.88 (n/a)</td><td>405.90 (n/a)</td><td>295.40 (n/a)</td><td>155.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1833.00 (n/a)</td><td>701.94 (n/a)</td><td>464.00 (n/a)</td><td>280.80 (n/a)</td><td>647.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (-3.25%)</td><td>0.39 (+17.80%)</td><td>0.43 (+16.20%)</td><td>0.21 <b>(+30.84%)</b></td><td>0.10 <b>(-29.63%)</b></td><td>1030.80 <b>(-23.57%)</b></td><td>622.32 <b>(-24.56%)</b></td><td>512.10 (-13.95%)</td><td>480.70 (+3.35%)</td><td>233.85 <b>(-44.89%)</b></td><td>19.63 (-3.25%)</td><td>16.47 (+17.80%)</td><td>18.43 (+16.20%)</td><td>9.16 <b>(+30.84%)</b></td><td>4.40 <b>(-29.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.48 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>1348.60 (n/a)</td><td>824.88 (n/a)</td><td>595.10 (n/a)</td><td>465.10 (n/a)</td><td>424.37 (n/a)</td><td>20.29 (n/a)</td><td>13.98 (n/a)</td><td>15.86 (n/a)</td><td>7.00 (n/a)</td><td>6.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.55 (+1.84%)</td><td>0.46 (+3.43%)</td><td>0.46 (+1.90%)</td><td>0.36 (+1.38%)</td><td>0.07 (-20.00%)</td><td>609.20 (-1.38%)</td><td>487.56 (-4.38%)</td><td>480.80 (-1.88%)</td><td>403.00 (-1.80%)</td><td>76.28 <b>(-22.15%)</b></td><td>23.42 (+1.84%)</td><td>19.71 (+3.43%)</td><td>19.63 (+1.90%)</td><td>15.49 (+1.38%)</td><td>2.88 (-20.00%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>617.70 (n/a)</td><td>509.90 (n/a)</td><td>490.00 (n/a)</td><td>410.40 (n/a)</td><td>97.98 (n/a)</td><td>22.99 (n/a)</td><td>19.06 (n/a)</td><td>19.26 (n/a)</td><td>15.28 (n/a)</td><td>3.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.31 (-0.55%)</td><td>0.30 (-0.48%)</td><td>0.30 (-0.35%)</td><td>0.30 (+1.69%)</td><td>0.01 <b>(-34.69%)</b></td><td>84467.50 (-1.66%)</td><td>83188.90 (+0.45%)</td><td>83781.20 (+0.36%)</td><td>80839.70 (+0.55%)</td><td>1470.52 <b>(-35.22%)</b></td><td>212.52 (-0.55%)</td><td>206.57 (-0.48%)</td><td>205.06 (-0.35%)</td><td>203.39 (+1.69%)</td><td>3.70 <b>(-34.69%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85893.40 (n/a)</td><td>82819.76 (n/a)</td><td>83484.30 (n/a)</td><td>80397.60 (n/a)</td><td>2269.85 (n/a)</td><td>213.69 (n/a)</td><td>207.56 (n/a)</td><td>205.79 (n/a)</td><td>200.01 (n/a)</td><td>5.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.03 (-0.97%)</td><td>1.00 (+0.08%)</td><td>1.01 (+1.85%)</td><td>0.95 (-1.82%)</td><td>0.03 (+5.85%)</td><td>26613.40 (+1.86%)</td><td>25148.40 (-0.07%)</td><td>24896.80 (-1.82%)</td><td>24444.30 (+0.98%)</td><td>841.95 (+9.99%)</td><td>702.82 (-0.97%)</td><td>683.73 (+0.08%)</td><td>690.04 (+1.85%)</td><td>645.53 (-1.82%)</td><td>22.05 (+5.85%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.04 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.03 (n/a)</td><td>26128.70 (n/a)</td><td>25166.54 (n/a)</td><td>25357.50 (n/a)</td><td>24206.80 (n/a)</td><td>765.46 (n/a)</td><td>709.71 (n/a)</td><td>683.15 (n/a)</td><td>677.51 (n/a)</td><td>657.51 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.83 (+0.57%)</td><td>0.80 (-1.53%)</td><td>0.81 (-0.50%)</td><td>0.77 (-4.83%)</td><td>0.02 <b>(+404.64%)</b></td><td>97789.70 (+5.08%)</td><td>94129.70 (+1.61%)</td><td>93302.50 (+0.50%)</td><td>91432.40 (-0.56%)</td><td>2503.19 <b>(+428.07%)</b></td><td>751.59 (+0.57%)</td><td>730.46 (-1.53%)</td><td>736.52 (-0.50%)</td><td>702.73 (-4.83%)</td><td>19.21 <b>(+404.65%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.00 (n/a)</td><td>93063.70 (n/a)</td><td>92636.60 (n/a)</td><td>92840.30 (n/a)</td><td>91951.70 (n/a)</td><td>474.03 (n/a)</td><td>747.34 (n/a)</td><td>741.83 (n/a)</td><td>740.19 (n/a)</td><td>738.41 (n/a)</td><td>3.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.78 (-0.54%)</td><td>0.76 (-1.46%)</td><td>0.77 (-1.56%)</td><td>0.75 (-1.25%)</td><td>0.01 <b>(+20.67%)</b></td><td>100206.20 (+1.26%)</td><td>98862.76 (+1.49%)</td><td>98675.60 (+1.59%)</td><td>96971.60 (+0.54%)</td><td>1339.17 <b>(+23.25%)</b></td><td>708.66 (-0.54%)</td><td>695.20 (-1.46%)</td><td>696.42 (-1.56%)</td><td>685.78 (-1.25%)</td><td>9.45 <b>(+20.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>98955.50 (n/a)</td><td>97410.40 (n/a)</td><td>97131.80 (n/a)</td><td>96452.00 (n/a)</td><td>1086.58 (n/a)</td><td>712.47 (n/a)</td><td>705.53 (n/a)</td><td>707.49 (n/a)</td><td>694.45 (n/a)</td><td>7.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.80 (+0.16%)</td><td>0.79 (-0.22%)</td><td>0.80 (+0.14%)</td><td>0.78 (-1.46%)</td><td>0.01 <b>(+180.30%)</b></td><td>96836.70 (+1.48%)</td><td>95128.98 (+0.23%)</td><td>94704.00 (-0.14%)</td><td>94309.70 (-0.16%)</td><td>1047.58 <b>(+183.99%)</b></td><td>728.66 (+0.16%)</td><td>722.45 (-0.22%)</td><td>725.62 (+0.14%)</td><td>709.64 (-1.46%)</td><td>7.88 <b>(+180.30%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95422.70 (n/a)</td><td>94913.04 (n/a)</td><td>94832.90 (n/a)</td><td>94460.40 (n/a)</td><td>368.88 (n/a)</td><td>727.49 (n/a)</td><td>724.03 (n/a)</td><td>724.64 (n/a)</td><td>720.16 (n/a)</td><td>2.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.72 <b>(+41.66%)</b></td><td>4.32 <b>(+48.64%)</b></td><td>5.25 <b>(+135.62%)</b></td><td>2.23 (+4.21%)</td><td>1.62 <b>(+63.85%)</b></td><td>4002.10 (-4.04%)</td><td>2383.88 <b>(-28.60%)</b></td><td>1697.50 <b>(-57.56%)</b></td><td>1558.30 <b>(-29.41%)</b></td><td>1091.70 (+8.15%)</td><td>344.52 <b>(+41.66%)</b></td><td>260.36 <b>(+48.64%)</b></td><td>316.28 <b>(+135.62%)</b></td><td>134.15 (+4.21%)</td><td>97.40 <b>(+63.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.04 (n/a)</td><td>2.91 (n/a)</td><td>2.23 (n/a)</td><td>2.14 (n/a)</td><td>0.99 (n/a)</td><td>4170.80 (n/a)</td><td>3338.94 (n/a)</td><td>3999.70 (n/a)</td><td>2207.50 (n/a)</td><td>1009.39 (n/a)</td><td>243.21 (n/a)</td><td>175.16 (n/a)</td><td>134.23 (n/a)</td><td>128.72 (n/a)</td><td>59.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.71 <b>(-31.23%)</b></td><td>2.27 (-8.27%)</td><td>2.19 (+0.05%)</td><td>2.04 (+13.95%)</td><td>0.26 <b>(-69.12%)</b></td><td>4371.90 (-12.24%)</td><td>3961.66 (+2.56%)</td><td>4077.10 (-0.05%)</td><td>3289.90 <b>(+45.41%)</b></td><td>410.51 <b>(-58.58%)</b></td><td>163.19 <b>(-31.23%)</b></td><td>136.81 (-8.27%)</td><td>131.68 (+0.05%)</td><td>122.80 (+13.95%)</td><td>15.63 <b>(-69.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.94 (n/a)</td><td>2.48 (n/a)</td><td>2.18 (n/a)</td><td>1.79 (n/a)</td><td>0.84 (n/a)</td><td>4981.70 (n/a)</td><td>3862.90 (n/a)</td><td>4079.20 (n/a)</td><td>2262.50 (n/a)</td><td>991.05 (n/a)</td><td>237.29 (n/a)</td><td>149.14 (n/a)</td><td>131.61 (n/a)</td><td>107.77 (n/a)</td><td>50.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.33 (+6.07%)</td><td>3.90 (+7.44%)</td><td>4.11 (+2.95%)</td><td>2.14 (-0.23%)</td><td>1.47 <b>(+29.35%)</b></td><td>4159.90 (+0.23%)</td><td>2612.66 (-2.84%)</td><td>2166.30 (-2.87%)</td><td>1671.90 (-5.72%)</td><td>1108.38 (+15.52%)</td><td>321.11 (+6.07%)</td><td>234.97 (+7.44%)</td><td>247.83 (+2.95%)</td><td>129.06 (-0.23%)</td><td>88.66 <b>(+29.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.03 (n/a)</td><td>3.63 (n/a)</td><td>4.00 (n/a)</td><td>2.15 (n/a)</td><td>1.14 (n/a)</td><td>4150.30 (n/a)</td><td>2689.04 (n/a)</td><td>2230.30 (n/a)</td><td>1773.40 (n/a)</td><td>959.44 (n/a)</td><td>302.73 (n/a)</td><td>218.70 (n/a)</td><td>240.71 (n/a)</td><td>129.36 (n/a)</td><td>68.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.52 (+6.06%)</td><td>5.08 (-6.07%)</td><td>4.74 (-13.00%)</td><td>4.39 (-8.89%)</td><td>0.84 <b>(+58.29%)</b></td><td>7945.60 (+9.76%)</td><td>6987.42 (+7.67%)</td><td>7362.70 (+14.94%)</td><td>5346.80 (-5.71%)</td><td>991.27 <b>(+58.28%)</b></td><td>401.64 (+6.06%)</td><td>313.16 (-6.07%)</td><td>291.67 (-13.00%)</td><td>270.27 (-8.89%)</td><td>51.61 <b>(+58.29%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.15 (n/a)</td><td>5.41 (n/a)</td><td>5.44 (n/a)</td><td>4.82 (n/a)</td><td>0.53 (n/a)</td><td>7239.30 (n/a)</td><td>6489.82 (n/a)</td><td>6405.80 (n/a)</td><td>5670.60 (n/a)</td><td>626.27 (n/a)</td><td>378.71 (n/a)</td><td>333.41 (n/a)</td><td>335.24 (n/a)</td><td>296.64 (n/a)</td><td>32.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.58 (+9.68%)</td><td>4.92 (+17.67%)</td><td>4.90 (+19.78%)</td><td>3.95 (+8.91%)</td><td>0.67 <b>(+22.51%)</b></td><td>8817.30 (-8.18%)</td><td>7204.44 (-14.73%)</td><td>7110.80 (-16.51%)</td><td>6250.60 (-8.82%)</td><td>1042.37 (+4.36%)</td><td>343.56 (+9.68%)</td><td>302.79 (+17.67%)</td><td>302.00 (+19.78%)</td><td>243.55 (+8.91%)</td><td>40.97 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.09 (n/a)</td><td>4.18 (n/a)</td><td>4.09 (n/a)</td><td>3.63 (n/a)</td><td>0.54 (n/a)</td><td>9603.00 (n/a)</td><td>8448.80 (n/a)</td><td>8517.40 (n/a)</td><td>6855.50 (n/a)</td><td>998.80 (n/a)</td><td>313.25 (n/a)</td><td>257.32 (n/a)</td><td>252.13 (n/a)</td><td>223.63 (n/a)</td><td>33.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.50 (+0.36%)</td><td>5.67 (-3.48%)</td><td>5.77 (-3.84%)</td><td>4.89 (-4.86%)</td><td>0.68 (+7.97%)</td><td>7135.20 (+5.11%)</td><td>6220.24 (+3.84%)</td><td>6039.80 (+3.99%)</td><td>5361.20 (-0.35%)</td><td>753.67 (+14.73%)</td><td>400.56 (+0.36%)</td><td>349.29 (-3.48%)</td><td>355.56 (-3.84%)</td><td>300.97 (-4.86%)</td><td>41.90 (+7.97%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.48 (n/a)</td><td>5.88 (n/a)</td><td>6.00 (n/a)</td><td>5.14 (n/a)</td><td>0.63 (n/a)</td><td>6788.50 (n/a)</td><td>5990.46 (n/a)</td><td>5807.80 (n/a)</td><td>5380.30 (n/a)</td><td>656.92 (n/a)</td><td>399.14 (n/a)</td><td>361.89 (n/a)</td><td>369.76 (n/a)</td><td>316.34 (n/a)</td><td>38.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.79 (+1.82%)</td><td>0.76 (-1.00%)</td><td>0.77 (-0.27%)</td><td>0.71 (-6.93%)</td><td>0.03 <b>(+538.75%)</b></td><td>106529.80 (+7.45%)</td><td>99353.62 (+1.15%)</td><td>98326.60 (+0.27%)</td><td>95860.10 (-1.79%)</td><td>4391.67 <b>(+574.22%)</b></td><td>716.87 (+1.82%)</td><td>692.71 (-1.00%)</td><td>698.89 (-0.27%)</td><td>645.07 (-6.93%)</td><td>29.56 <b>(+538.75%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99145.70 (n/a)</td><td>98219.86 (n/a)</td><td>98065.70 (n/a)</td><td>97604.10 (n/a)</td><td>651.37 (n/a)</td><td>704.06 (n/a)</td><td>699.67 (n/a)</td><td>700.75 (n/a)</td><td>693.12 (n/a)</td><td>4.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.76 (-2.08%)</td><td>0.75 (-1.39%)</td><td>0.75 (-0.23%)</td><td>0.73 (-2.78%)</td><td>0.01 (+10.69%)</td><td>103171.20 (+2.86%)</td><td>100685.70 (+1.41%)</td><td>100096.70 (+0.23%)</td><td>98957.80 (+2.12%)</td><td>1614.64 (+16.69%)</td><td>694.43 (-2.08%)</td><td>682.65 (-1.39%)</td><td>686.53 (-0.23%)</td><td>666.07 (-2.78%)</td><td>10.85 (+10.69%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100306.60 (n/a)</td><td>99285.44 (n/a)</td><td>99862.30 (n/a)</td><td>96900.10 (n/a)</td><td>1383.73 (n/a)</td><td>709.18 (n/a)</td><td>692.25 (n/a)</td><td>688.14 (n/a)</td><td>685.09 (n/a)</td><td>9.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.82 (+0.74%)</td><td>0.81 (+0.46%)</td><td>0.81 (+0.65%)</td><td>0.80 (-0.18%)</td><td>0.01 <b>(+42.06%)</b></td><td>94770.00 (+0.18%)</td><td>93450.44 (-0.45%)</td><td>93233.90 (-0.64%)</td><td>92556.70 (-0.73%)</td><td>883.76 <b>(+41.38%)</b></td><td>742.46 (+0.74%)</td><td>735.41 (+0.46%)</td><td>737.07 (+0.65%)</td><td>725.12 (-0.18%)</td><td>6.92 <b>(+42.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94596.00 (n/a)</td><td>93874.04 (n/a)</td><td>93836.80 (n/a)</td><td>93237.40 (n/a)</td><td>625.10 (n/a)</td><td>737.04 (n/a)</td><td>732.07 (n/a)</td><td>732.33 (n/a)</td><td>726.45 (n/a)</td><td>4.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.74 (+6.37%)</td><td>2.87 (+8.12%)</td><td>3.39 <b>(+29.43%)</b></td><td>1.73 <b>(+26.03%)</b></td><td>0.99 (+14.56%)</td><td>4668.40 <b>(-20.66%)</b></td><td>3141.14 (-7.54%)</td><td>2380.50 <b>(-22.74%)</b></td><td>2152.90 (-5.99%)</td><td>1227.65 (-15.85%)</td><td>981.90 (+6.37%)</td><td>753.47 (+8.12%)</td><td>888.00 <b>(+29.43%)</b></td><td>452.81 <b>(+26.03%)</b></td><td>258.37 (+14.56%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.52 (n/a)</td><td>2.66 (n/a)</td><td>2.62 (n/a)</td><td>1.37 (n/a)</td><td>0.86 (n/a)</td><td>5883.70 (n/a)</td><td>3397.32 (n/a)</td><td>3081.00 (n/a)</td><td>2290.00 (n/a)</td><td>1458.84 (n/a)</td><td>923.13 (n/a)</td><td>696.86 (n/a)</td><td>686.11 (n/a)</td><td>359.29 (n/a)</td><td>225.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 <b>(+23.66%)</b></td><td>0.21 (+14.28%)</td><td>0.20 (+1.46%)</td><td>0.18 <b>(+41.84%)</b></td><td>0.03 (-5.86%)</td><td>6895.60 <b>(-29.50%)</b></td><td>6169.26 (-13.96%)</td><td>6322.70 (-1.44%)</td><td>4785.70 (-19.13%)</td><td>812.45 <b>(-48.53%)</b></td><td>14.02 <b>(+23.66%)</b></td><td>11.06 (+14.28%)</td><td>10.61 (+1.46%)</td><td>9.73 <b>(+41.84%)</b></td><td>1.70 (-5.86%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>9780.60 (n/a)</td><td>7170.38 (n/a)</td><td>6415.20 (n/a)</td><td>5917.80 (n/a)</td><td>1578.36 (n/a)</td><td>11.34 (n/a)</td><td>9.68 (n/a)</td><td>10.46 (n/a)</td><td>6.86 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.80 (n/a)</td><td>3.69 (n/a)</td><td>3.69 (n/a)</td><td>3.57 (n/a)</td><td>0.09 (n/a)</td><td>3.79 (n/a)</td><td>3.69 (n/a)</td><td>3.69 (n/a)</td><td>3.57 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.19 (-1.27%)</td><td>6.52 (+0.46%)</td><td>6.78 (+2.29%)</td><td>5.71 (+1.14%)</td><td>0.69 (-6.78%)</td><td>7.18 (-1.27%)</td><td>6.52 (+0.46%)</td><td>6.78 (+2.29%)</td><td>5.70 (+1.14%)</td><td>0.69 (-6.78%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.28 (n/a)</td><td>6.49 (n/a)</td><td>6.63 (n/a)</td><td>5.64 (n/a)</td><td>0.74 (n/a)</td><td>7.28 (n/a)</td><td>6.49 (n/a)</td><td>6.63 (n/a)</td><td>5.64 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>12.97 (+17.59%)</td><td>9.21 (+0.96%)</td><td>8.38 (-11.37%)</td><td>7.88 (+3.93%)</td><td>2.11 <b>(+44.18%)</b></td><td>12.96 (+17.59%)</td><td>9.20 (+0.96%)</td><td>8.38 (-11.37%)</td><td>7.88 (+3.93%)</td><td>2.11 <b>(+44.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>11.03 (n/a)</td><td>9.12 (n/a)</td><td>9.46 (n/a)</td><td>7.59 (n/a)</td><td>1.47 (n/a)</td><td>11.02 (n/a)</td><td>9.11 (n/a)</td><td>9.45 (n/a)</td><td>7.58 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.92 (n/a)</td><td>3.68 (n/a)</td><td>3.65 (n/a)</td><td>3.49 (n/a)</td><td>0.16 (n/a)</td><td>3.92 (n/a)</td><td>3.67 (n/a)</td><td>3.65 (n/a)</td><td>3.49 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.42 (-11.17%)</td><td>6.13 (-3.65%)</td><td>6.28 (+2.14%)</td><td>5.78 (-1.51%)</td><td>0.29 <b>(-45.73%)</b></td><td>6.41 (-11.17%)</td><td>6.12 (-3.65%)</td><td>6.28 (+2.14%)</td><td>5.78 (-1.51%)</td><td>0.29 <b>(-45.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.22 (n/a)</td><td>6.36 (n/a)</td><td>6.15 (n/a)</td><td>5.87 (n/a)</td><td>0.54 (n/a)</td><td>7.22 (n/a)</td><td>6.36 (n/a)</td><td>6.15 (n/a)</td><td>5.87 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>12.87 <b>(+35.23%)</b></td><td>9.81 (+14.84%)</td><td>8.56 (+0.46%)</td><td>8.29 (+15.67%)</td><td>1.99 <b>(+121.53%)</b></td><td>12.86 <b>(+35.23%)</b></td><td>9.81 (+14.84%)</td><td>8.56 (+0.46%)</td><td>8.29 (+15.67%)</td><td>1.99 <b>(+121.53%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>9.52 (n/a)</td><td>8.55 (n/a)</td><td>8.52 (n/a)</td><td>7.17 (n/a)</td><td>0.90 (n/a)</td><td>9.51 (n/a)</td><td>8.54 (n/a)</td><td>8.52 (n/a)</td><td>7.16 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.95 (-0.80%)</td><td>1.88 (+7.96%)</td><td>1.62 <b>(+51.21%)</b></td><td>1.03 (-1.28%)</td><td>0.92 (-2.67%)</td><td>2.95 (-0.80%)</td><td>1.87 (+7.96%)</td><td>1.62 <b>(+51.21%)</b></td><td>1.02 (-1.28%)</td><td>0.92 (-2.67%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.98 (n/a)</td><td>1.74 (n/a)</td><td>1.07 (n/a)</td><td>1.04 (n/a)</td><td>0.94 (n/a)</td><td>2.97 (n/a)</td><td>1.73 (n/a)</td><td>1.07 (n/a)</td><td>1.04 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.52 (-4.18%)</td><td>0.29 (-9.92%)</td><td>0.28 <b>(-22.68%)</b></td><td>0.07 (-2.04%)</td><td>0.21 (-7.78%)</td><td>0.51 (-4.18%)</td><td>0.28 (-9.92%)</td><td>0.28 <b>(-22.68%)</b></td><td>0.07 (-2.04%)</td><td>0.21 (-7.78%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td><td>0.53 (n/a)</td><td>0.31 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.68 (-5.41%)</td><td>0.48 (-17.78%)</td><td>0.46 <b>(-28.00%)</b></td><td>0.37 <b>(+24.77%)</b></td><td>0.12 <b>(-25.77%)</b></td><td>0.67 (-5.41%)</td><td>0.48 (-17.78%)</td><td>0.45 <b>(-28.00%)</b></td><td>0.37 <b>(+24.77%)</b></td><td>0.12 <b>(-25.77%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.64 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.71 (n/a)</td><td>0.58 (n/a)</td><td>0.63 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.82 (+8.54%)</td><td>2.16 <b>(+24.83%)</b></td><td>2.41 <b>(+49.43%)</b></td><td>1.54 <b>(+80.92%)</b></td><td>0.58 (-10.07%)</td><td>2.78 (+8.54%)</td><td>2.13 <b>(+24.83%)</b></td><td>2.37 <b>(+49.43%)</b></td><td>1.51 <b>(+80.92%)</b></td><td>0.57 (-10.07%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.60 (n/a)</td><td>1.73 (n/a)</td><td>1.61 (n/a)</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>2.56 (n/a)</td><td>1.70 (n/a)</td><td>1.58 (n/a)</td><td>0.84 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.20 (n/a)</td><td>358.28 (n/a)</td><td>302.70 (n/a)</td><td>245.10 (n/a)</td><td>122.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.50 (n/a)</td><td>420.24 (n/a)</td><td>385.20 (n/a)</td><td>289.70 (n/a)</td><td>127.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.70 (n/a)</td><td>437.84 (n/a)</td><td>456.10 (n/a)</td><td>233.70 (n/a)</td><td>142.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.70 (n/a)</td><td>445.14 (n/a)</td><td>448.90 (n/a)</td><td>289.60 (n/a)</td><td>96.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.00 (n/a)</td><td>414.06 (n/a)</td><td>404.40 (n/a)</td><td>278.70 (n/a)</td><td>103.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.30 (n/a)</td><td>395.60 (n/a)</td><td>301.10 (n/a)</td><td>262.70 (n/a)</td><td>156.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.90 (n/a)</td><td>347.56 (n/a)</td><td>299.30 (n/a)</td><td>251.90 (n/a)</td><td>159.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.30 (n/a)</td><td>503.84 (n/a)</td><td>516.30 (n/a)</td><td>286.40 (n/a)</td><td>143.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.40 (n/a)</td><td>297.14 (n/a)</td><td>263.50 (n/a)</td><td>216.40 (n/a)</td><td>84.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>941.40 (n/a)</td><td>553.36 (n/a)</td><td>589.30 (n/a)</td><td>229.80 (n/a)</td><td>265.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>817.10 (n/a)</td><td>490.12 (n/a)</td><td>492.10 (n/a)</td><td>267.60 (n/a)</td><td>212.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>990.80 (n/a)</td><td>546.06 (n/a)</td><td>475.80 (n/a)</td><td>274.10 (n/a)</td><td>269.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>840.10 (n/a)</td><td>498.16 (n/a)</td><td>510.00 (n/a)</td><td>234.90 (n/a)</td><td>243.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>767.40 (n/a)</td><td>432.72 (n/a)</td><td>402.30 (n/a)</td><td>232.10 (n/a)</td><td>208.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>550.80 (n/a)</td><td>457.08 (n/a)</td><td>478.40 (n/a)</td><td>292.10 (n/a)</td><td>97.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>780.90 (n/a)</td><td>512.18 (n/a)</td><td>460.70 (n/a)</td><td>261.10 (n/a)</td><td>200.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>739.00 (n/a)</td><td>455.80 (n/a)</td><td>464.40 (n/a)</td><td>242.20 (n/a)</td><td>206.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1366.60 (n/a)</td><td>600.12 (n/a)</td><td>406.00 (n/a)</td><td>351.50 (n/a)</td><td>431.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>509.00 (n/a)</td><td>362.10 (n/a)</td><td>318.40 (n/a)</td><td>276.10 (n/a)</td><td>93.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>613.40 (n/a)</td><td>504.34 (n/a)</td><td>540.30 (n/a)</td><td>317.10 (n/a)</td><td>118.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>560.30 (n/a)</td><td>421.72 (n/a)</td><td>410.60 (n/a)</td><td>288.40 (n/a)</td><td>123.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.50 (n/a)</td><td>443.04 (n/a)</td><td>456.50 (n/a)</td><td>229.90 (n/a)</td><td>164.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>577.00 (n/a)</td><td>469.96 (n/a)</td><td>493.90 (n/a)</td><td>240.20 (n/a)</td><td>133.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>613.60 (n/a)</td><td>479.52 (n/a)</td><td>506.60 (n/a)</td><td>268.20 (n/a)</td><td>143.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+0.47%)</td><td>0.01 (+9.41%)</td><td>0.02 <b>(+64.94%)</b></td><td>0.01 (-9.81%)</td><td>0.00 (+11.48%)</td><td>534.50 (+10.87%)</td><td>350.98 (-5.90%)</td><td>260.90 <b>(-39.37%)</b></td><td>238.90 (-0.50%)</td><td>136.79 <b>(+23.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.10 (n/a)</td><td>373.00 (n/a)</td><td>430.30 (n/a)</td><td>240.10 (n/a)</td><td>110.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+11.73%)</td><td>0.01 (+8.42%)</td><td>0.01 (+3.79%)</td><td>0.01 <b>(+23.66%)</b></td><td>0.00 (-8.53%)</td><td>458.40 (-19.14%)</td><td>305.84 (-10.41%)</td><td>277.50 (-3.65%)</td><td>241.30 (-10.50%)</td><td>86.94 <b>(-31.69%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.90 (n/a)</td><td>341.38 (n/a)</td><td>288.00 (n/a)</td><td>269.60 (n/a)</td><td>127.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+16.08%)</td><td>0.01 <b>(+29.94%)</b></td><td>0.01 <b>(+54.29%)</b></td><td>0.01 (+13.55%)</td><td>0.00 <b>(+50.34%)</b></td><td>466.70 (-11.93%)</td><td>341.66 <b>(-20.94%)</b></td><td>274.30 <b>(-35.20%)</b></td><td>262.20 (-13.86%)</td><td>101.86 (+12.51%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.90 (n/a)</td><td>432.16 (n/a)</td><td>423.30 (n/a)</td><td>304.40 (n/a)</td><td>90.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (-6.48%)</td><td>0.01 (-13.08%)</td><td>0.01 (+15.90%)</td><td>0.01 <b>(-23.73%)</b></td><td>0.00 (-14.72%)</td><td>758.60 <b>(+31.11%)</b></td><td>501.52 (+14.91%)</td><td>436.90 (-13.72%)</td><td>279.80 (+6.96%)</td><td>184.81 <b>(+21.57%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.60 (n/a)</td><td>436.44 (n/a)</td><td>506.40 (n/a)</td><td>261.60 (n/a)</td><td>152.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-27.82%)</b></td><td>0.01 <b>(-23.42%)</b></td><td>0.01 <b>(-33.28%)</b></td><td>0.01 (+10.23%)</td><td>0.00 <b>(-43.22%)</b></td><td>525.70 (-9.28%)</td><td>450.46 <b>(+20.93%)</b></td><td>514.40 <b>(+49.88%)</b></td><td>276.80 <b>(+38.54%)</b></td><td>106.68 <b>(-28.77%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>372.50 (n/a)</td><td>343.20 (n/a)</td><td>199.80 (n/a)</td><td>149.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-30.24%)</b></td><td>0.01 (-14.24%)</td><td>0.01 (+2.29%)</td><td>0.01 (+0.33%)</td><td>0.00 <b>(-61.87%)</b></td><td>529.90 (-0.34%)</td><td>461.72 (+9.59%)</td><td>469.90 (-2.25%)</td><td>360.70 <b>(+43.36%)</b></td><td>61.86 <b>(-47.46%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.70 (n/a)</td><td>421.30 (n/a)</td><td>480.70 (n/a)</td><td>251.60 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+3.66%)</td><td>0.02 (-0.37%)</td><td>0.02 <b>(-22.59%)</b></td><td>0.02 (+8.75%)</td><td>0.01 (+3.22%)</td><td>529.30 (-8.04%)</td><td>399.40 (-0.37%)</td><td>462.90 <b>(+29.16%)</b></td><td>249.10 (-3.56%)</td><td>124.35 (-11.53%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>400.90 (n/a)</td><td>358.40 (n/a)</td><td>258.30 (n/a)</td><td>140.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+2.76%)</td><td>0.02 (+0.67%)</td><td>0.02 (+11.48%)</td><td>0.01 <b>(-20.38%)</b></td><td>0.01 (+17.71%)</td><td>634.50 <b>(+25.62%)</b></td><td>399.88 (+3.15%)</td><td>377.50 (-10.29%)</td><td>252.90 (-2.69%)</td><td>144.86 <b>(+50.05%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.10 (n/a)</td><td>387.68 (n/a)</td><td>420.80 (n/a)</td><td>259.90 (n/a)</td><td>96.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+2.64%)</td><td>0.03 (+12.01%)</td><td>0.03 (+7.18%)</td><td>0.02 <b>(+24.06%)</b></td><td>0.01 (-13.13%)</td><td>508.10 (-19.39%)</td><td>329.86 (-14.99%)</td><td>293.80 (-6.70%)</td><td>224.40 (-2.56%)</td><td>110.52 <b>(-31.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.30 (n/a)</td><td>388.04 (n/a)</td><td>314.90 (n/a)</td><td>230.30 (n/a)</td><td>161.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+11.16%)</td><td>0.02 (-9.84%)</td><td>0.02 (-7.93%)</td><td>0.00 <b>(-73.78%)</b></td><td>0.01 <b>(+75.56%)</b></td><td>2041.20 <b>(+281.39%)</b></td><td>698.52 <b>(+85.43%)</b></td><td>426.10 (+8.62%)</td><td>218.10 (-10.06%)</td><td>760.70 <b>(+561.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>376.70 (n/a)</td><td>392.30 (n/a)</td><td>242.50 (n/a)</td><td>114.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-41.12%)</b></td><td>0.02 <b>(-26.30%)</b></td><td>0.01 (-7.26%)</td><td>0.01 (-13.31%)</td><td>0.00 <b>(-60.96%)</b></td><td>638.00 (+15.37%)</td><td>531.00 <b>(+24.17%)</b></td><td>567.80 (+7.82%)</td><td>406.20 <b>(+69.82%)</b></td><td>111.46 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>427.64 (n/a)</td><td>526.60 (n/a)</td><td>239.20 (n/a)</td><td>152.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(+33.55%)</b></td><td>0.02 (-5.58%)</td><td>0.02 (+1.32%)</td><td>0.00 <b>(-44.15%)</b></td><td>0.01 <b>(+41.13%)</b></td><td>1926.30 <b>(+79.04%)</b></td><td>740.16 <b>(+37.47%)</b></td><td>492.00 (-1.32%)</td><td>213.60 <b>(-25.13%)</b></td><td>677.17 <b>(+111.19%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1075.90 (n/a)</td><td>538.40 (n/a)</td><td>498.60 (n/a)</td><td>285.30 (n/a)</td><td>320.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (-3.71%)</td><td>0.02 (+1.97%)</td><td>0.02 (-19.45%)</td><td>0.01 (+19.43%)</td><td>0.01 <b>(-20.06%)</b></td><td>618.50 (-16.27%)</td><td>392.22 (-13.21%)</td><td>361.30 <b>(+24.12%)</b></td><td>223.70 (+3.85%)</td><td>159.66 <b>(-38.01%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>738.70 (n/a)</td><td>451.92 (n/a)</td><td>291.10 (n/a)</td><td>215.40 (n/a)</td><td>257.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-8.56%)</td><td>0.02 (+11.80%)</td><td>0.02 <b>(+23.96%)</b></td><td>0.01 (+7.03%)</td><td>0.00 <b>(-21.56%)</b></td><td>609.20 (-6.58%)</td><td>480.30 (-12.71%)</td><td>504.80 (-19.34%)</td><td>367.00 (+9.36%)</td><td>104.15 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.10 (n/a)</td><td>550.24 (n/a)</td><td>625.80 (n/a)</td><td>335.60 (n/a)</td><td>134.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+11.02%)</td><td>0.05 (+5.37%)</td><td>0.06 <b>(+22.32%)</b></td><td>0.03 (-19.94%)</td><td>0.02 <b>(+67.99%)</b></td><td>594.10 <b>(+24.92%)</b></td><td>363.98 (+3.32%)</td><td>261.60 (-18.22%)</td><td>243.80 (-9.90%)</td><td>156.48 <b>(+83.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>475.60 (n/a)</td><td>352.28 (n/a)</td><td>319.90 (n/a)</td><td>270.60 (n/a)</td><td>85.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+4.57%)</td><td>0.05 (+11.36%)</td><td>0.06 (+2.48%)</td><td>0.03 (-7.51%)</td><td>0.01 (-0.83%)</td><td>550.30 (+8.11%)</td><td>325.38 (-10.02%)</td><td>287.10 (-2.45%)</td><td>244.20 (-4.39%)</td><td>127.68 (+4.46%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>509.00 (n/a)</td><td>361.62 (n/a)</td><td>294.30 (n/a)</td><td>255.40 (n/a)</td><td>122.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (-18.56%)</td><td>0.04 (-7.05%)</td><td>0.04 (-0.43%)</td><td>0.03 (+7.56%)</td><td>0.01 <b>(-31.07%)</b></td><td>543.50 (-7.03%)</td><td>407.50 (+2.56%)</td><td>421.90 (+0.45%)</td><td>295.90 <b>(+22.78%)</b></td><td>109.02 <b>(-22.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.60 (n/a)</td><td>397.32 (n/a)</td><td>420.00 (n/a)</td><td>241.00 (n/a)</td><td>140.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+0.26%)</td><td>0.04 <b>(-21.70%)</b></td><td>0.03 <b>(-42.22%)</b></td><td>0.02 (-18.52%)</td><td>0.02 (-4.93%)</td><td>663.70 <b>(+22.73%)</b></td><td>470.30 <b>(+27.22%)</b></td><td>477.80 <b>(+73.05%)</b></td><td>246.60 (-0.24%)</td><td>151.56 (+5.84%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.80 (n/a)</td><td>369.68 (n/a)</td><td>276.10 (n/a)</td><td>247.20 (n/a)</td><td>143.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+3.34%)</td><td>0.04 (-7.44%)</td><td>0.03 (-13.91%)</td><td>0.03 (-12.87%)</td><td>0.02 <b>(+25.60%)</b></td><td>620.50 (+14.78%)</td><td>436.32 (+15.45%)</td><td>473.10 (+16.16%)</td><td>233.70 (-3.23%)</td><td>175.13 <b>(+44.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.60 (n/a)</td><td>377.92 (n/a)</td><td>407.30 (n/a)</td><td>241.50 (n/a)</td><td>121.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 (-11.71%)</td><td>0.04 (-1.75%)</td><td>0.03 (-11.08%)</td><td>0.03 <b>(+28.02%)</b></td><td>0.01 <b>(-32.18%)</b></td><td>596.90 <b>(-21.89%)</b></td><td>473.80 (-4.79%)</td><td>489.60 (+12.45%)</td><td>311.80 (+13.26%)</td><td>107.88 <b>(-41.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>764.20 (n/a)</td><td>497.66 (n/a)</td><td>435.40 (n/a)</td><td>275.30 (n/a)</td><td>185.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-5.15%)</td><td>0.08 <b>(-22.83%)</b></td><td>0.06 <b>(-33.63%)</b></td><td>0.05 (-10.35%)</td><td>0.03 (-7.40%)</td><td>629.40 (+11.54%)</td><td>468.64 <b>(+29.59%)</b></td><td>507.10 <b>(+50.65%)</b></td><td>250.60 (+5.43%)</td><td>146.51 (+8.47%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>564.30 (n/a)</td><td>361.62 (n/a)</td><td>336.60 (n/a)</td><td>237.70 (n/a)</td><td>135.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 <b>(+35.38%)</b></td><td>0.09 (+18.37%)</td><td>0.08 (+3.39%)</td><td>0.06 (-0.22%)</td><td>0.04 <b>(+115.50%)</b></td><td>572.10 (+0.21%)</td><td>410.02 (-7.19%)</td><td>426.30 (-3.29%)</td><td>229.00 <b>(-26.13%)</b></td><td>155.45 <b>(+66.64%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>570.90 (n/a)</td><td>441.78 (n/a)</td><td>440.80 (n/a)</td><td>310.00 (n/a)</td><td>93.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (+14.69%)</td><td>0.08 (-0.96%)</td><td>0.07 (-7.11%)</td><td>0.04 <b>(-32.68%)</b></td><td>0.04 <b>(+46.41%)</b></td><td>799.60 <b>(+48.54%)</b></td><td>471.94 (+13.16%)</td><td>496.40 (+7.66%)</td><td>246.40 (-12.81%)</td><td>227.13 <b>(+82.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>538.30 (n/a)</td><td>417.04 (n/a)</td><td>461.10 (n/a)</td><td>282.60 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (+4.80%)</td><td>0.09 (+11.71%)</td><td>0.09 (+13.05%)</td><td>0.06 <b>(+267.09%)</b></td><td>0.03 <b>(-33.34%)</b></td><td>516.20 <b>(-72.76%)</b></td><td>381.56 <b>(-42.20%)</b></td><td>381.10 (-11.56%)</td><td>241.20 (-4.55%)</td><td>113.59 <b>(-83.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1894.80 (n/a)</td><td>660.10 (n/a)</td><td>430.90 (n/a)</td><td>252.70 (n/a)</td><td>695.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (-10.65%)</td><td>0.08 (-5.70%)</td><td>0.07 (-0.52%)</td><td>0.05 (-12.90%)</td><td>0.03 (-7.44%)</td><td>667.80 (+14.82%)</td><td>462.52 (+7.14%)</td><td>450.40 (+0.51%)</td><td>267.60 (+11.92%)</td><td>169.81 (+18.80%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>581.60 (n/a)</td><td>431.68 (n/a)</td><td>448.10 (n/a)</td><td>239.10 (n/a)</td><td>142.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-12.16%)</td><td>0.01 (-11.53%)</td><td>0.01 <b>(-28.12%)</b></td><td>0.01 (-3.76%)</td><td>0.01 (-3.40%)</td><td>609.90 (+3.90%)</td><td>390.72 (+14.09%)</td><td>414.50 <b>(+39.09%)</b></td><td>214.60 (+13.85%)</td><td>161.01 (+6.75%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>342.46 (n/a)</td><td>298.00 (n/a)</td><td>188.50 (n/a)</td><td>150.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-17.32%)</td><td>0.01 (-10.69%)</td><td>0.01 (-13.11%)</td><td>0.01 (-8.01%)</td><td>0.00 <b>(-29.69%)</b></td><td>407.50 (+8.70%)</td><td>298.88 (+10.44%)</td><td>274.00 (+15.13%)</td><td>252.40 <b>(+20.94%)</b></td><td>62.13 (-5.77%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>374.90 (n/a)</td><td>270.62 (n/a)</td><td>238.00 (n/a)</td><td>208.70 (n/a)</td><td>65.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+12.13%)</td><td>0.01 (-19.19%)</td><td>0.01 <b>(-40.45%)</b></td><td>0.01 (-17.52%)</td><td>0.01 <b>(+30.73%)</b></td><td>646.40 <b>(+21.25%)</b></td><td>458.92 <b>(+33.36%)</b></td><td>472.70 <b>(+67.92%)</b></td><td>181.20 (-10.78%)</td><td>180.90 <b>(+29.45%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.10 (n/a)</td><td>344.12 (n/a)</td><td>281.50 (n/a)</td><td>203.10 (n/a)</td><td>139.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-3.95%)</td><td>0.01 (-8.64%)</td><td>0.02 (+6.64%)</td><td>0.01 <b>(-26.35%)</b></td><td>0.00 <b>(+30.21%)</b></td><td>511.80 <b>(+35.79%)</b></td><td>345.94 (+15.64%)</td><td>271.00 (-6.23%)</td><td>241.30 (+4.10%)</td><td>125.06 <b>(+84.85%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>376.90 (n/a)</td><td>299.16 (n/a)</td><td>289.00 (n/a)</td><td>231.80 (n/a)</td><td>67.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-20.37%)</b></td><td>0.01 <b>(-22.59%)</b></td><td>0.01 <b>(-45.38%)</b></td><td>0.01 (-10.25%)</td><td>0.00 <b>(-22.98%)</b></td><td>558.40 (+11.41%)</td><td>419.48 <b>(+25.97%)</b></td><td>479.90 <b>(+83.03%)</b></td><td>275.60 <b>(+25.56%)</b></td><td>134.24 (+0.86%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.20 (n/a)</td><td>333.00 (n/a)</td><td>262.20 (n/a)</td><td>219.50 (n/a)</td><td>133.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-20.26%)</b></td><td>0.01 (-14.27%)</td><td>0.01 (-14.63%)</td><td>0.01 <b>(+60.46%)</b></td><td>0.00 <b>(-44.38%)</b></td><td>463.80 <b>(-37.69%)</b></td><td>344.46 (-0.07%)</td><td>290.70 (+17.12%)</td><td>272.50 <b>(+25.40%)</b></td><td>88.79 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>744.30 (n/a)</td><td>344.70 (n/a)</td><td>248.20 (n/a)</td><td>217.30 (n/a)</td><td>224.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (-6.51%)</td><td>0.01 <b>(-27.16%)</b></td><td>0.01 <b>(-40.50%)</b></td><td>0.01 <b>(-34.02%)</b></td><td>0.00 (+4.11%)</td><td>768.40 <b>(+51.56%)</b></td><td>502.94 <b>(+43.74%)</b></td><td>470.20 <b>(+68.05%)</b></td><td>288.10 (+6.94%)</td><td>185.46 <b>(+73.90%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.00 (n/a)</td><td>349.90 (n/a)</td><td>279.80 (n/a)</td><td>269.40 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-35.98%)</b></td><td>0.01 <b>(-60.89%)</b></td><td>0.01 <b>(-60.75%)</b></td><td>0.00 <b>(-83.67%)</b></td><td>0.00 <b>(+37.23%)</b></td><td>2424.10 <b>(+512.30%)</b></td><td>1211.52 <b>(+304.27%)</b></td><td>666.20 <b>(+154.76%)</b></td><td>391.80 <b>(+56.22%)</b></td><td>936.39 <b>(+1361.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>395.90 (n/a)</td><td>299.68 (n/a)</td><td>261.50 (n/a)</td><td>250.80 (n/a)</td><td>64.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+6.40%)</td><td>0.01 (-8.85%)</td><td>0.01 (-14.20%)</td><td>0.01 (+14.72%)</td><td>0.00 (-5.56%)</td><td>532.00 (-12.83%)</td><td>418.62 (+7.15%)</td><td>455.20 (+16.54%)</td><td>241.40 (-6.00%)</td><td>115.86 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.30 (n/a)</td><td>390.68 (n/a)</td><td>390.60 (n/a)</td><td>256.80 (n/a)</td><td>144.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(+34.38%)</b></td><td>0.01 <b>(+29.68%)</b></td><td>0.01 <b>(+51.93%)</b></td><td>0.01 (+17.51%)</td><td>0.00 <b>(+66.99%)</b></td><td>492.60 (-14.89%)</td><td>341.10 <b>(-20.97%)</b></td><td>281.50 <b>(-34.18%)</b></td><td>264.10 <b>(-25.58%)</b></td><td>97.55 (+6.57%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.80 (n/a)</td><td>431.62 (n/a)</td><td>427.70 (n/a)</td><td>354.90 (n/a)</td><td>91.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-31.23%)</b></td><td>0.01 (-8.56%)</td><td>0.01 (+6.54%)</td><td>0.01 (-5.49%)</td><td>0.00 <b>(-58.78%)</b></td><td>598.30 (+5.80%)</td><td>509.34 (+3.40%)</td><td>527.70 (-6.14%)</td><td>401.60 <b>(+45.40%)</b></td><td>79.46 <b>(-36.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.50 (n/a)</td><td>492.60 (n/a)</td><td>562.20 (n/a)</td><td>276.20 (n/a)</td><td>124.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (+2.07%)</td><td>0.01 (+0.56%)</td><td>0.01 <b>(+46.42%)</b></td><td>0.00 <b>(-68.12%)</b></td><td>0.00 <b>(+41.63%)</b></td><td>1936.60 <b>(+213.67%)</b></td><td>687.20 <b>(+46.01%)</b></td><td>356.00 <b>(-31.70%)</b></td><td>283.40 (-2.04%)</td><td>704.12 <b>(+372.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.40 (n/a)</td><td>470.66 (n/a)</td><td>521.20 (n/a)</td><td>289.30 (n/a)</td><td>149.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (-11.28%)</td><td>0.02 (-19.44%)</td><td>0.02 <b>(-35.26%)</b></td><td>0.02 (+1.62%)</td><td>0.01 (-11.63%)</td><td>465.40 (-1.61%)</td><td>384.70 <b>(+23.21%)</b></td><td>432.60 <b>(+54.44%)</b></td><td>263.80 (+12.69%)</td><td>94.39 (-1.87%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.00 (n/a)</td><td>312.22 (n/a)</td><td>280.10 (n/a)</td><td>234.10 (n/a)</td><td>96.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (-10.59%)</td><td>0.03 (+11.74%)</td><td>0.03 (+9.52%)</td><td>0.02 <b>(+31.10%)</b></td><td>0.01 <b>(-45.45%)</b></td><td>374.90 <b>(-23.72%)</b></td><td>273.76 (-17.72%)</td><td>245.30 (-8.71%)</td><td>237.40 (+11.82%)</td><td>58.12 <b>(-54.69%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.50 (n/a)</td><td>332.70 (n/a)</td><td>268.70 (n/a)</td><td>212.30 (n/a)</td><td>128.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-37.78%)</b></td><td>0.02 <b>(-42.33%)</b></td><td>0.02 <b>(-36.79%)</b></td><td>0.00 <b>(-76.96%)</b></td><td>0.01 (-3.52%)</td><td>2481.90 <b>(+333.97%)</b></td><td>847.38 <b>(+155.96%)</b></td><td>437.60 <b>(+58.21%)</b></td><td>423.90 <b>(+60.75%)</b></td><td>913.83 <b>(+578.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.90 (n/a)</td><td>331.06 (n/a)</td><td>276.60 (n/a)</td><td>263.70 (n/a)</td><td>134.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+0.05%)</td><td>0.03 (-4.04%)</td><td>0.03 (-7.65%)</td><td>0.02 (+2.00%)</td><td>0.01 (+1.53%)</td><td>364.50 (-1.94%)</td><td>288.38 (+4.25%)</td><td>280.90 (+8.29%)</td><td>230.40 (-0.04%)</td><td>58.08 (-1.03%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>371.70 (n/a)</td><td>276.62 (n/a)</td><td>259.40 (n/a)</td><td>230.50 (n/a)</td><td>58.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+7.56%)</td><td>0.03 (+17.51%)</td><td>0.03 <b>(+51.00%)</b></td><td>0.02 (+9.72%)</td><td>0.01 (+3.97%)</td><td>516.00 (-8.87%)</td><td>340.94 (-15.54%)</td><td>264.60 <b>(-33.78%)</b></td><td>237.90 (-7.03%)</td><td>126.92 (-11.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.20 (n/a)</td><td>403.68 (n/a)</td><td>399.60 (n/a)</td><td>255.90 (n/a)</td><td>143.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (-3.77%)</td><td>0.03 (+11.72%)</td><td>0.03 <b>(+32.19%)</b></td><td>0.02 (+0.37%)</td><td>0.01 (-5.26%)</td><td>500.80 (-0.36%)</td><td>325.74 (-11.21%)</td><td>262.30 <b>(-24.37%)</b></td><td>203.90 (+3.92%)</td><td>126.56 (-3.78%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.60 (n/a)</td><td>366.86 (n/a)</td><td>346.80 (n/a)</td><td>196.20 (n/a)</td><td>131.53 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+34.56%)</b></td><td>0.03 <b>(+54.51%)</b></td><td>0.03 <b>(+90.86%)</b></td><td>0.02 <b>(+24.21%)</b></td><td>0.01 <b>(+40.13%)</b></td><td>513.60 (-19.49%)</td><td>312.44 <b>(-34.33%)</b></td><td>256.50 <b>(-47.60%)</b></td><td>236.80 <b>(-25.70%)</b></td><td>115.09 (-12.23%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>475.78 (n/a)</td><td>489.50 (n/a)</td><td>318.70 (n/a)</td><td>131.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+18.06%)</td><td>0.03 (+16.11%)</td><td>0.03 <b>(+40.89%)</b></td><td>0.01 (-8.98%)</td><td>0.01 (+17.73%)</td><td>553.20 (+9.87%)</td><td>344.80 (-12.08%)</td><td>315.50 <b>(-29.04%)</b></td><td>203.10 (-15.30%)</td><td>136.91 (+8.12%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.50 (n/a)</td><td>392.18 (n/a)</td><td>444.60 (n/a)</td><td>239.80 (n/a)</td><td>126.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-30.74%)</b></td><td>0.02 <b>(-23.65%)</b></td><td>0.02 (-8.61%)</td><td>0.01 (-7.54%)</td><td>0.00 <b>(-48.71%)</b></td><td>634.40 (+8.15%)</td><td>515.30 <b>(+22.57%)</b></td><td>510.30 (+9.44%)</td><td>339.30 <b>(+44.38%)</b></td><td>119.02 (-18.98%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.60 (n/a)</td><td>420.40 (n/a)</td><td>466.30 (n/a)</td><td>235.00 (n/a)</td><td>146.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+12.80%)</td><td>0.02 (+5.53%)</td><td>0.02 (-3.44%)</td><td>0.02 (+2.80%)</td><td>0.01 <b>(+37.03%)</b></td><td>529.80 (-2.72%)</td><td>389.24 (+0.09%)</td><td>450.30 (+3.56%)</td><td>224.60 (-11.33%)</td><td>149.17 <b>(+20.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.60 (n/a)</td><td>388.88 (n/a)</td><td>434.80 (n/a)</td><td>253.30 (n/a)</td><td>123.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(+60.24%)</b></td><td>0.03 <b>(+23.68%)</b></td><td>0.03 <b>(+44.63%)</b></td><td>0.01 <b>(-33.40%)</b></td><td>0.02 <b>(+94.36%)</b></td><td>916.60 <b>(+50.14%)</b></td><td>432.66 (+1.71%)</td><td>276.60 <b>(-30.85%)</b></td><td>160.80 <b>(-37.60%)</b></td><td>302.89 <b>(+86.88%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.50 (n/a)</td><td>425.38 (n/a)</td><td>400.00 (n/a)</td><td>257.70 (n/a)</td><td>162.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(+47.96%)</b></td><td>0.02 (+13.22%)</td><td>0.02 (+5.63%)</td><td>0.01 (-14.77%)</td><td>0.01 <b>(+116.75%)</b></td><td>579.20 (+17.32%)</td><td>420.56 (-0.22%)</td><td>451.30 (-5.33%)</td><td>181.90 <b>(-32.40%)</b></td><td>160.94 <b>(+67.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.70 (n/a)</td><td>421.48 (n/a)</td><td>476.70 (n/a)</td><td>269.10 (n/a)</td><td>95.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(+83.24%)</b></td><td>0.06 <b>(+64.48%)</b></td><td>0.06 <b>(+77.69%)</b></td><td>0.03 <b>(+26.47%)</b></td><td>0.02 <b>(+181.97%)</b></td><td>487.50 <b>(-20.94%)</b></td><td>308.50 <b>(-34.67%)</b></td><td>261.70 <b>(-43.72%)</b></td><td>194.90 <b>(-45.44%)</b></td><td>116.76 <b>(+23.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>616.60 (n/a)</td><td>472.20 (n/a)</td><td>465.00 (n/a)</td><td>357.20 (n/a)</td><td>94.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (-14.65%)</td><td>0.04 (-19.64%)</td><td>0.05 (-19.51%)</td><td>0.01 <b>(-73.58%)</b></td><td>0.03 <b>(+36.84%)</b></td><td>1865.30 <b>(+278.43%)</b></td><td>639.36 <b>(+97.99%)</b></td><td>362.20 <b>(+24.25%)</b></td><td>237.80 (+17.14%)</td><td>692.92 <b>(+511.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>492.90 (n/a)</td><td>322.92 (n/a)</td><td>291.50 (n/a)</td><td>203.00 (n/a)</td><td>113.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (+4.44%)</td><td>0.04 (-15.11%)</td><td>0.04 <b>(-33.66%)</b></td><td>0.03 (+3.62%)</td><td>0.02 (+7.65%)</td><td>568.10 (-3.48%)</td><td>402.16 (+17.79%)</td><td>422.40 <b>(+50.75%)</b></td><td>259.10 (-4.25%)</td><td>130.28 (-6.00%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.60 (n/a)</td><td>341.42 (n/a)</td><td>280.20 (n/a)</td><td>270.60 (n/a)</td><td>138.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (+12.37%)</td><td>0.05 (-10.95%)</td><td>0.04 <b>(-39.76%)</b></td><td>0.03 (+12.97%)</td><td>0.02 <b>(+27.63%)</b></td><td>552.20 (-11.49%)</td><td>390.40 (+15.38%)</td><td>443.30 <b>(+65.97%)</b></td><td>194.40 (-10.99%)</td><td>155.35 (-5.36%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.90 (n/a)</td><td>338.36 (n/a)</td><td>267.10 (n/a)</td><td>218.40 (n/a)</td><td>164.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (-11.46%)</td><td>0.04 <b>(-27.62%)</b></td><td>0.03 <b>(-37.81%)</b></td><td>0.03 (-19.08%)</td><td>0.01 (-4.53%)</td><td>558.80 <b>(+23.57%)</b></td><td>458.86 <b>(+39.89%)</b></td><td>487.90 <b>(+60.81%)</b></td><td>257.20 (+12.96%)</td><td>117.78 <b>(+24.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>452.20 (n/a)</td><td>328.02 (n/a)</td><td>303.40 (n/a)</td><td>227.70 (n/a)</td><td>94.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 <b>(-25.46%)</b></td><td>0.04 <b>(-21.49%)</b></td><td>0.04 (-8.79%)</td><td>0.03 <b>(-24.11%)</b></td><td>0.01 <b>(-29.72%)</b></td><td>534.50 <b>(+31.78%)</b></td><td>399.04 <b>(+26.45%)</b></td><td>383.40 (+9.64%)</td><td>265.70 <b>(+34.12%)</b></td><td>103.86 <b>(+26.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>405.60 (n/a)</td><td>315.56 (n/a)</td><td>349.70 (n/a)</td><td>198.10 (n/a)</td><td>82.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 <b>(+55.05%)</b></td><td>0.05 (-1.24%)</td><td>0.05 (-10.45%)</td><td>0.01 <b>(-74.35%)</b></td><td>0.04 <b>(+124.19%)</b></td><td>1900.40 <b>(+289.83%)</b></td><td>637.94 <b>(+79.80%)</b></td><td>325.70 (+11.66%)</td><td>156.40 <b>(-35.53%)</b></td><td>715.73 <b>(+493.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.50 (n/a)</td><td>354.80 (n/a)</td><td>291.70 (n/a)</td><td>242.60 (n/a)</td><td>120.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(+26.36%)</b></td><td>0.06 (+19.31%)</td><td>0.07 <b>(+38.67%)</b></td><td>0.03 (-2.54%)</td><td>0.03 <b>(+59.54%)</b></td><td>586.90 (+2.60%)</td><td>341.04 (-7.16%)</td><td>241.70 <b>(-27.89%)</b></td><td>197.90 <b>(-20.84%)</b></td><td>179.42 <b>(+31.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.00 (n/a)</td><td>367.36 (n/a)</td><td>335.20 (n/a)</td><td>250.00 (n/a)</td><td>135.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 <b>(+55.73%)</b></td><td>0.06 <b>(+36.56%)</b></td><td>0.06 <b>(+62.83%)</b></td><td>0.03 <b>(+73.89%)</b></td><td>0.03 <b>(+36.14%)</b></td><td>605.70 <b>(-42.49%)</b></td><td>354.96 <b>(-31.72%)</b></td><td>287.60 <b>(-38.57%)</b></td><td>157.10 <b>(-35.77%)</b></td><td>173.21 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1053.20 (n/a)</td><td>519.84 (n/a)</td><td>468.20 (n/a)</td><td>244.60 (n/a)</td><td>327.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 <b>(+30.73%)</b></td><td>0.06 (+11.83%)</td><td>0.06 (+12.09%)</td><td>0.03 (-14.99%)</td><td>0.03 <b>(+71.00%)</b></td><td>561.80 (+17.63%)</td><td>347.12 (+0.56%)</td><td>273.30 (-10.80%)</td><td>182.10 <b>(-23.52%)</b></td><td>172.68 <b>(+57.57%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>477.60 (n/a)</td><td>345.18 (n/a)</td><td>306.40 (n/a)</td><td>238.10 (n/a)</td><td>109.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(-20.72%)</b></td><td>0.04 (+5.02%)</td><td>0.04 (+11.82%)</td><td>0.03 <b>(+69.31%)</b></td><td>0.01 <b>(-53.49%)</b></td><td>609.80 <b>(-40.94%)</b></td><td>463.08 (-17.86%)</td><td>459.80 (-10.58%)</td><td>344.70 <b>(+26.13%)</b></td><td>96.48 <b>(-65.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1032.50 (n/a)</td><td>563.76 (n/a)</td><td>514.20 (n/a)</td><td>273.30 (n/a)</td><td>283.72 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 (-5.71%)</td><td>0.04 (+12.18%)</td><td>0.04 <b>(+37.17%)</b></td><td>0.03 <b>(+30.93%)</b></td><td>0.01 <b>(-22.70%)</b></td><td>582.60 <b>(-23.62%)</b></td><td>427.68 (-16.86%)</td><td>398.60 <b>(-27.09%)</b></td><td>259.90 (+6.04%)</td><td>131.37 <b>(-33.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>762.80 (n/a)</td><td>514.40 (n/a)</td><td>546.70 (n/a)</td><td>245.10 (n/a)</td><td>198.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-0.86%)</td><td>0.11 (-4.77%)</td><td>0.12 (-1.55%)</td><td>0.07 (+11.93%)</td><td>0.03 (-13.58%)</td><td>461.50 (-10.65%)</td><td>315.20 (+2.22%)</td><td>266.00 (+1.57%)</td><td>250.90 (+0.88%)</td><td>88.58 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.50 (n/a)</td><td>308.36 (n/a)</td><td>261.90 (n/a)</td><td>248.70 (n/a)</td><td>116.58 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (-16.96%)</td><td>0.10 (-0.22%)</td><td>0.11 <b>(+53.36%)</b></td><td>0.06 (+3.76%)</td><td>0.03 <b>(-35.72%)</b></td><td>511.60 (-3.62%)</td><td>366.68 (-5.71%)</td><td>302.30 <b>(-34.79%)</b></td><td>270.70 <b>(+20.42%)</b></td><td>107.31 <b>(-23.20%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>530.80 (n/a)</td><td>388.88 (n/a)</td><td>463.60 (n/a)</td><td>224.80 (n/a)</td><td>139.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 <b>(+42.39%)</b></td><td>0.09 <b>(+27.03%)</b></td><td>0.07 (+5.21%)</td><td>0.05 (-4.40%)</td><td>0.04 <b>(+156.30%)</b></td><td>622.90 (+4.60%)</td><td>420.16 (-12.51%)</td><td>447.30 (-4.95%)</td><td>245.90 <b>(-29.78%)</b></td><td>164.47 <b>(+80.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>595.50 (n/a)</td><td>480.22 (n/a)</td><td>470.60 (n/a)</td><td>350.20 (n/a)</td><td>91.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-0.29%)</td><td>0.10 <b>(+21.58%)</b></td><td>0.12 (+14.36%)</td><td>0.06 <b>(+262.33%)</b></td><td>0.03 <b>(-30.81%)</b></td><td>531.50 <b>(-72.40%)</b></td><td>351.08 <b>(-47.37%)</b></td><td>283.90 (-12.57%)</td><td>247.30 (+0.28%)</td><td>124.78 <b>(-82.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1925.60 (n/a)</td><td>667.04 (n/a)</td><td>324.70 (n/a)</td><td>246.60 (n/a)</td><td>712.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (-16.70%)</td><td>0.09 (-5.21%)</td><td>0.07 (-1.98%)</td><td>0.06 (-0.76%)</td><td>0.03 <b>(-25.28%)</b></td><td>559.80 (+0.77%)</td><td>410.36 (+0.50%)</td><td>453.10 (+2.03%)</td><td>270.50 <b>(+20.06%)</b></td><td>128.87 (-16.49%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>555.50 (n/a)</td><td>408.30 (n/a)</td><td>444.10 (n/a)</td><td>225.30 (n/a)</td><td>154.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-9.29%)</td><td>0.09 <b>(+23.48%)</b></td><td>0.08 <b>(+34.45%)</b></td><td>0.08 <b>(+38.74%)</b></td><td>0.02 <b>(-39.06%)</b></td><td>434.40 <b>(-27.91%)</b></td><td>360.74 <b>(-24.91%)</b></td><td>399.00 <b>(-25.62%)</b></td><td>261.50 (+10.24%)</td><td>73.52 <b>(-48.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>602.60 (n/a)</td><td>480.42 (n/a)</td><td>536.40 (n/a)</td><td>237.20 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 <b>(-24.56%)</b></td><td>0.09 (+13.76%)</td><td>0.08 <b>(+55.03%)</b></td><td>0.06 (+12.81%)</td><td>0.04 <b>(-42.37%)</b></td><td>572.30 (-11.35%)</td><td>396.68 <b>(-24.33%)</b></td><td>402.00 <b>(-35.49%)</b></td><td>227.60 <b>(+32.56%)</b></td><td>139.90 <b>(-30.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>645.60 (n/a)</td><td>524.20 (n/a)</td><td>623.20 (n/a)</td><td>171.70 (n/a)</td><td>200.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (-11.82%)</td><td>0.08 <b>(-20.38%)</b></td><td>0.08 <b>(-29.53%)</b></td><td>0.06 (-14.93%)</td><td>0.02 (+1.05%)</td><td>583.90 (+17.56%)</td><td>417.80 <b>(+27.09%)</b></td><td>417.30 <b>(+41.94%)</b></td><td>297.60 (+13.41%)</td><td>117.64 <b>(+23.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>496.70 (n/a)</td><td>328.74 (n/a)</td><td>294.00 (n/a)</td><td>262.40 (n/a)</td><td>95.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(-29.33%)</b></td><td>0.07 <b>(-20.18%)</b></td><td>0.07 (-18.87%)</td><td>0.06 (+2.23%)</td><td>0.01 <b>(-66.07%)</b></td><td>516.60 (-2.20%)</td><td>470.00 <b>(+20.11%)</b></td><td>488.60 <b>(+23.26%)</b></td><td>400.40 <b>(+41.48%)</b></td><td>46.78 <b>(-52.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>528.20 (n/a)</td><td>391.32 (n/a)</td><td>396.40 (n/a)</td><td>283.00 (n/a)</td><td>98.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (-1.43%)</td><td>0.09 <b>(+42.66%)</b></td><td>0.10 <b>(+74.29%)</b></td><td>0.06 <b>(+340.38%)</b></td><td>0.03 <b>(-30.72%)</b></td><td>562.80 <b>(-77.29%)</b></td><td>388.40 <b>(-55.57%)</b></td><td>333.30 <b>(-42.62%)</b></td><td>269.10 (+1.47%)</td><td>128.19 <b>(-85.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2478.70 (n/a)</td><td>874.18 (n/a)</td><td>580.90 (n/a)</td><td>265.20 (n/a)</td><td>906.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.12 (-15.27%)</td><td>0.07 <b>(-23.54%)</b></td><td>0.06 <b>(-37.61%)</b></td><td>0.05 (-12.10%)</td><td>0.03 (-17.80%)</td><td>683.30 (+13.77%)</td><td>490.22 <b>(+28.77%)</b></td><td>514.90 <b>(+60.26%)</b></td><td>279.30 (+18.00%)</td><td>147.97 (+3.01%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.60 (n/a)</td><td>380.68 (n/a)</td><td>321.30 (n/a)</td><td>236.70 (n/a)</td><td>143.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 <b>(-51.79%)</b></td><td>0.07 <b>(-26.89%)</b></td><td>0.07 (-0.82%)</td><td>0.05 (-0.10%)</td><td>0.01 <b>(-82.42%)</b></td><td>606.30 (+0.10%)</td><td>502.56 (+19.42%)</td><td>488.60 (+0.83%)</td><td>442.80 <b>(+107.40%)</b></td><td>61.32 <b>(-61.89%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>605.70 (n/a)</td><td>420.82 (n/a)</td><td>484.60 (n/a)</td><td>213.50 (n/a)</td><td>160.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (-10.64%)</td><td>0.09 (+1.87%)</td><td>0.10 (+15.11%)</td><td>0.05 (+0.95%)</td><td>0.02 (-5.98%)</td><td>495.30 (-0.94%)</td><td>303.12 (-2.16%)</td><td>245.90 (-13.14%)</td><td>233.90 (+11.91%)</td><td>110.60 (-0.66%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>500.00 (n/a)</td><td>309.82 (n/a)</td><td>283.10 (n/a)</td><td>209.00 (n/a)</td><td>111.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.23 <b>(+43.96%)</b></td><td>0.17 <b>(+31.76%)</b></td><td>0.18 <b>(+44.16%)</b></td><td>0.12 <b>(+31.17%)</b></td><td>0.05 <b>(+50.92%)</b></td><td>417.30 <b>(-23.75%)</b></td><td>315.32 <b>(-22.91%)</b></td><td>279.90 <b>(-30.63%)</b></td><td>210.60 <b>(-30.54%)</b></td><td>91.54 (-13.03%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>547.30 (n/a)</td><td>409.02 (n/a)</td><td>403.50 (n/a)</td><td>303.20 (n/a)</td><td>105.25 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.39 (+13.75%)</td><td>3.18 (-0.85%)</td><td>2.71 (-15.89%)</td><td>2.60 (+1.61%)</td><td>0.79 <b>(+71.57%)</b></td><td>4039.20 (-1.58%)</td><td>3440.02 (+3.57%)</td><td>3868.50 (+18.90%)</td><td>2390.90 (-12.09%)</td><td>745.58 <b>(+50.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.86 (n/a)</td><td>3.21 (n/a)</td><td>3.22 (n/a)</td><td>2.55 (n/a)</td><td>0.46 (n/a)</td><td>4104.10 (n/a)</td><td>3321.36 (n/a)</td><td>3253.70 (n/a)</td><td>2719.60 (n/a)</td><td>496.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 <b>(+27.21%)</b></td><td>0.15 (+13.11%)</td><td>0.16 (+19.48%)</td><td>0.07 <b>(-27.53%)</b></td><td>0.04 <b>(+146.70%)</b></td><td>547.80 <b>(+37.98%)</b></td><td>310.34 (-3.22%)</td><td>263.30 (-16.28%)</td><td>214.10 <b>(-21.37%)</b></td><td>134.91 <b>(+184.65%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>397.00 (n/a)</td><td>320.68 (n/a)</td><td>314.50 (n/a)</td><td>272.30 (n/a)</td><td>47.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-3.70%)</td><td>0.02 <b>(-20.60%)</b></td><td>0.02 (-8.54%)</td><td>0.01 <b>(-40.98%)</b></td><td>0.00 <b>(+184.48%)</b></td><td>499.40 <b>(+69.46%)</b></td><td>358.50 <b>(+35.00%)</b></td><td>294.90 (+9.34%)</td><td>246.80 (+3.87%)</td><td>111.94 <b>(+420.45%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>294.70 (n/a)</td><td>265.56 (n/a)</td><td>269.70 (n/a)</td><td>237.60 (n/a)</td><td>21.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+7.01%)</td><td>0.01 <b>(+21.31%)</b></td><td>0.01 <b>(+52.79%)</b></td><td>0.00 <b>(-46.62%)</b></td><td>0.00 <b>(+55.00%)</b></td><td>1162.90 <b>(+87.32%)</b></td><td>478.98 (+3.17%)</td><td>335.50 <b>(-34.55%)</b></td><td>265.70 (-6.54%)</td><td>384.46 <b>(+194.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.80 (n/a)</td><td>464.26 (n/a)</td><td>512.60 (n/a)</td><td>284.30 (n/a)</td><td>130.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(-20.58%)</b></td><td>0.02 (+3.50%)</td><td>0.01 (+6.30%)</td><td>0.01 (-4.59%)</td><td>0.00 <b>(-27.12%)</b></td><td>618.00 (+4.80%)</td><td>418.64 (-6.02%)</td><td>437.70 (-5.93%)</td><td>284.40 <b>(+25.90%)</b></td><td>134.76 (+0.71%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.70 (n/a)</td><td>445.44 (n/a)</td><td>465.30 (n/a)</td><td>225.90 (n/a)</td><td>133.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+1.42%)</td><td>0.01 <b>(+31.56%)</b></td><td>0.01 <b>(+74.56%)</b></td><td>0.01 (+2.78%)</td><td>0.00 (-3.69%)</td><td>611.60 (-2.70%)</td><td>352.34 <b>(-24.90%)</b></td><td>280.60 <b>(-42.71%)</b></td><td>269.60 (-1.39%)</td><td>146.87 (-8.95%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.60 (n/a)</td><td>469.18 (n/a)</td><td>489.80 (n/a)</td><td>273.40 (n/a)</td><td>161.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+14.37%)</td><td>0.01 (-2.86%)</td><td>0.01 (-3.60%)</td><td>0.01 <b>(-22.53%)</b></td><td>0.00 <b>(+76.90%)</b></td><td>704.40 <b>(+29.06%)</b></td><td>503.16 (+8.33%)</td><td>477.50 (+3.71%)</td><td>311.50 (-12.57%)</td><td>146.19 <b>(+97.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.80 (n/a)</td><td>464.46 (n/a)</td><td>460.40 (n/a)</td><td>356.30 (n/a)</td><td>73.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-39.37%)</b></td><td>0.01 <b>(-23.58%)</b></td><td>0.01 (-19.14%)</td><td>0.01 (-2.93%)</td><td>0.00 <b>(-69.91%)</b></td><td>522.90 (+3.01%)</td><td>472.44 <b>(+24.04%)</b></td><td>490.50 <b>(+23.68%)</b></td><td>409.80 <b>(+64.91%)</b></td><td>52.90 <b>(-48.30%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.60 (n/a)</td><td>380.88 (n/a)</td><td>396.60 (n/a)</td><td>248.50 (n/a)</td><td>102.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(+28.21%)</b></td><td>0.02 (+16.57%)</td><td>0.02 <b>(+66.76%)</b></td><td>0.01 (-15.96%)</td><td>0.01 <b>(+51.30%)</b></td><td>738.80 (+19.01%)</td><td>406.76 (-3.57%)</td><td>273.80 <b>(-40.02%)</b></td><td>211.70 <b>(-22.00%)</b></td><td>224.98 <b>(+53.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.80 (n/a)</td><td>421.82 (n/a)</td><td>456.50 (n/a)</td><td>271.40 (n/a)</td><td>146.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+3.84%)</td><td>0.01 <b>(+39.84%)</b></td><td>0.01 <b>(+65.21%)</b></td><td>0.01 <b>(+23.93%)</b></td><td>0.00 (-15.53%)</td><td>471.00 (-19.32%)</td><td>319.62 <b>(-30.60%)</b></td><td>286.80 <b>(-39.47%)</b></td><td>250.00 (-3.70%)</td><td>88.48 <b>(-27.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.80 (n/a)</td><td>460.52 (n/a)</td><td>473.80 (n/a)</td><td>259.60 (n/a)</td><td>122.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 <b>(-35.48%)</b></td><td>0.01 <b>(-25.14%)</b></td><td>0.01 (-18.74%)</td><td>0.00 <b>(-24.66%)</b></td><td>0.00 <b>(-43.64%)</b></td><td>1006.30 <b>(+32.72%)</b></td><td>609.96 <b>(+28.18%)</b></td><td>562.70 <b>(+23.08%)</b></td><td>355.20 <b>(+54.97%)</b></td><td>239.43 <b>(+24.66%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>758.20 (n/a)</td><td>475.86 (n/a)</td><td>457.20 (n/a)</td><td>229.20 (n/a)</td><td>192.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-16.21%)</td><td>0.01 (+10.47%)</td><td>0.01 <b>(+41.15%)</b></td><td>0.01 (+11.20%)</td><td>0.00 (-18.42%)</td><td>617.90 (-10.07%)</td><td>411.66 (-13.02%)</td><td>353.00 <b>(-29.16%)</b></td><td>257.10 (+19.36%)</td><td>167.96 (-11.17%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.10 (n/a)</td><td>473.30 (n/a)</td><td>498.30 (n/a)</td><td>215.40 (n/a)</td><td>189.09 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+38.86%)</b></td><td>0.01 (-12.50%)</td><td>0.01 <b>(-41.86%)</b></td><td>0.00 <b>(-67.46%)</b></td><td>0.01 <b>(+104.87%)</b></td><td>1977.60 <b>(+207.27%)</b></td><td>698.10 <b>(+92.24%)</b></td><td>497.90 <b>(+71.99%)</b></td><td>177.90 <b>(-27.98%)</b></td><td>731.83 <b>(+353.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.60 (n/a)</td><td>363.14 (n/a)</td><td>289.50 (n/a)</td><td>247.00 (n/a)</td><td>161.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(+53.34%)</b></td><td>0.01 <b>(+36.73%)</b></td><td>0.01 <b>(+49.48%)</b></td><td>0.01 <b>(+20.85%)</b></td><td>0.00 <b>(+113.32%)</b></td><td>559.50 (-17.26%)</td><td>415.26 <b>(-22.99%)</b></td><td>373.20 <b>(-33.09%)</b></td><td>253.90 <b>(-34.78%)</b></td><td>130.58 <b>(+23.20%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>676.20 (n/a)</td><td>539.20 (n/a)</td><td>557.80 (n/a)</td><td>389.30 (n/a)</td><td>105.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+15.49%)</td><td>0.02 (+16.97%)</td><td>0.02 (+6.56%)</td><td>0.01 <b>(+27.29%)</b></td><td>0.01 (+17.57%)</td><td>591.10 <b>(-21.44%)</b></td><td>403.22 (-14.81%)</td><td>428.20 (-6.18%)</td><td>220.20 (-13.41%)</td><td>141.42 <b>(-20.71%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>752.40 (n/a)</td><td>473.32 (n/a)</td><td>456.40 (n/a)</td><td>254.30 (n/a)</td><td>178.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(-29.98%)</b></td><td>0.04 (-12.91%)</td><td>0.04 (-5.86%)</td><td>0.02 (+1.27%)</td><td>0.01 <b>(-42.09%)</b></td><td>550.70 (-1.26%)</td><td>373.46 (+4.59%)</td><td>297.90 (+6.20%)</td><td>273.50 <b>(+42.82%)</b></td><td>125.35 <b>(-25.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>557.70 (n/a)</td><td>357.08 (n/a)</td><td>280.50 (n/a)</td><td>191.50 (n/a)</td><td>167.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (-4.82%)</td><td>0.02 (-15.61%)</td><td>0.02 <b>(-24.73%)</b></td><td>0.02 (-13.72%)</td><td>0.01 (+7.38%)</td><td>519.10 (+15.90%)</td><td>384.58 <b>(+22.28%)</b></td><td>394.80 <b>(+32.84%)</b></td><td>229.20 (+5.04%)</td><td>130.54 <b>(+36.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>447.90 (n/a)</td><td>314.50 (n/a)</td><td>297.20 (n/a)</td><td>218.20 (n/a)</td><td>95.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (-8.91%)</td><td>0.02 <b>(+24.69%)</b></td><td>0.02 <b>(+59.22%)</b></td><td>0.02 <b>(+217.55%)</b></td><td>0.01 <b>(-34.22%)</b></td><td>651.50 <b>(-68.51%)</b></td><td>468.44 <b>(-44.79%)</b></td><td>423.40 <b>(-37.20%)</b></td><td>257.80 (+9.80%)</td><td>161.37 <b>(-77.34%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2068.70 (n/a)</td><td>848.42 (n/a)</td><td>674.20 (n/a)</td><td>234.80 (n/a)</td><td>712.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(+31.72%)</b></td><td>0.02 (+12.49%)</td><td>0.02 (+18.84%)</td><td>0.01 (-13.67%)</td><td>0.01 <b>(+55.16%)</b></td><td>602.60 (+15.82%)</td><td>401.90 (-3.07%)</td><td>414.20 (-15.85%)</td><td>186.00 <b>(-24.08%)</b></td><td>173.20 <b>(+31.80%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>414.62 (n/a)</td><td>492.20 (n/a)</td><td>245.00 (n/a)</td><td>131.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 (+4.03%)</td><td>0.03 (+12.17%)</td><td>0.03 <b>(+51.73%)</b></td><td>0.02 (-3.26%)</td><td>0.01 (-5.59%)</td><td>619.20 (+3.37%)</td><td>359.86 (-11.72%)</td><td>298.90 <b>(-34.10%)</b></td><td>231.00 (-3.87%)</td><td>161.80 (+0.24%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.00 (n/a)</td><td>407.64 (n/a)</td><td>453.60 (n/a)</td><td>240.30 (n/a)</td><td>161.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (+1.36%)</td><td>0.02 <b>(+20.19%)</b></td><td>0.03 <b>(+58.90%)</b></td><td>0.01 (+9.92%)</td><td>0.01 <b>(+26.34%)</b></td><td>655.60 (-9.02%)</td><td>431.48 (-11.80%)</td><td>298.60 <b>(-37.07%)</b></td><td>269.30 (-1.32%)</td><td>197.99 <b>(+22.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>720.60 (n/a)</td><td>489.20 (n/a)</td><td>474.50 (n/a)</td><td>272.90 (n/a)</td><td>161.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(-24.71%)</b></td><td>0.02 <b>(-25.83%)</b></td><td>0.02 (-10.89%)</td><td>0.00 <b>(-74.81%)</b></td><td>0.01 (-15.45%)</td><td>2465.70 <b>(+296.99%)</b></td><td>796.40 <b>(+105.77%)</b></td><td>428.70 (+12.23%)</td><td>277.20 <b>(+32.82%)</b></td><td>936.52 <b>(+431.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.10 (n/a)</td><td>387.04 (n/a)</td><td>382.00 (n/a)</td><td>208.70 (n/a)</td><td>176.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 (-0.02%)</td><td>0.02 (+3.06%)</td><td>0.01 (-12.52%)</td><td>0.01 (+4.89%)</td><td>0.01 (+6.68%)</td><td>581.00 (-4.66%)</td><td>471.38 (-1.61%)</td><td>560.40 (+14.32%)</td><td>281.40 (+0.04%)</td><td>136.39 (+12.21%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>479.10 (n/a)</td><td>490.20 (n/a)</td><td>281.30 (n/a)</td><td>121.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(+26.31%)</b></td><td>0.02 (+4.89%)</td><td>0.02 (+6.74%)</td><td>0.02 (-3.87%)</td><td>0.01 <b>(+68.04%)</b></td><td>589.70 (+4.02%)</td><td>435.40 (+1.10%)</td><td>423.90 (-6.30%)</td><td>234.10 <b>(-20.83%)</b></td><td>140.78 <b>(+39.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>430.68 (n/a)</td><td>452.40 (n/a)</td><td>295.70 (n/a)</td><td>100.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.03 <b>(+72.82%)</b></td><td>0.02 <b>(+92.74%)</b></td><td>0.02 <b>(+26.41%)</b></td><td>0.02 <b>(+424.47%)</b></td><td>0.01 <b>(-21.05%)</b></td><td>461.90 <b>(-80.93%)</b></td><td>389.50 <b>(-64.77%)</b></td><td>420.70 <b>(-20.91%)</b></td><td>273.70 <b>(-42.14%)</b></td><td>79.96 <b>(-90.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2422.30 (n/a)</td><td>1105.72 (n/a)</td><td>531.90 (n/a)</td><td>473.00 (n/a)</td><td>867.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+1.38%)</td><td>0.04 (-19.68%)</td><td>0.04 <b>(-31.59%)</b></td><td>0.03 (-18.51%)</td><td>0.01 <b>(+34.91%)</b></td><td>565.20 <b>(+22.71%)</b></td><td>421.40 <b>(+29.66%)</b></td><td>454.00 <b>(+46.17%)</b></td><td>249.80 (-1.34%)</td><td>122.28 <b>(+52.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>460.60 (n/a)</td><td>325.00 (n/a)</td><td>310.60 (n/a)</td><td>253.20 (n/a)</td><td>79.95 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+1.50%)</td><td>0.06 (-17.29%)</td><td>0.05 <b>(-45.46%)</b></td><td>0.04 <b>(-21.87%)</b></td><td>0.03 <b>(+20.32%)</b></td><td>641.30 <b>(+27.98%)</b></td><td>438.24 <b>(+28.32%)</b></td><td>488.50 <b>(+83.37%)</b></td><td>241.90 (-1.47%)</td><td>172.15 <b>(+47.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.10 (n/a)</td><td>341.52 (n/a)</td><td>266.40 (n/a)</td><td>245.50 (n/a)</td><td>116.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (-10.80%)</td><td>0.05 (-13.53%)</td><td>0.06 (-15.29%)</td><td>0.01 (-0.16%)</td><td>0.03 (-11.41%)</td><td>1995.90 (+0.16%)</td><td>674.78 (+7.54%)</td><td>289.70 (+18.05%)</td><td>216.00 (+12.09%)</td><td>754.21 (-2.18%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1992.70 (n/a)</td><td>627.44 (n/a)</td><td>245.40 (n/a)</td><td>192.70 (n/a)</td><td>771.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (-2.92%)</td><td>0.06 <b>(-20.38%)</b></td><td>0.05 <b>(-40.56%)</b></td><td>0.04 <b>(-23.83%)</b></td><td>0.02 <b>(+46.08%)</b></td><td>569.50 <b>(+31.28%)</b></td><td>393.32 <b>(+35.72%)</b></td><td>452.00 <b>(+68.22%)</b></td><td>237.40 (+2.99%)</td><td>147.72 <b>(+77.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>433.80 (n/a)</td><td>289.80 (n/a)</td><td>268.70 (n/a)</td><td>230.50 (n/a)</td><td>83.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (-3.90%)</td><td>0.04 (-10.59%)</td><td>0.03 <b>(-26.83%)</b></td><td>0.03 <b>(+225.99%)</b></td><td>0.02 <b>(-26.82%)</b></td><td>596.60 <b>(-69.32%)</b></td><td>438.54 <b>(-31.29%)</b></td><td>486.90 <b>(+36.69%)</b></td><td>210.70 (+4.05%)</td><td>149.35 <b>(-79.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1944.70 (n/a)</td><td>638.28 (n/a)</td><td>356.20 (n/a)</td><td>202.50 (n/a)</td><td>736.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (-12.10%)</td><td>0.05 <b>(-23.17%)</b></td><td>0.04 <b>(-44.72%)</b></td><td>0.03 (-6.65%)</td><td>0.02 <b>(-25.59%)</b></td><td>618.20 (+7.12%)</td><td>460.70 <b>(+24.75%)</b></td><td>515.10 <b>(+80.86%)</b></td><td>272.20 (+13.75%)</td><td>144.30 (-8.73%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.10 (n/a)</td><td>369.30 (n/a)</td><td>284.80 (n/a)</td><td>239.30 (n/a)</td><td>158.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(-20.65%)</b></td><td>0.04 (-14.82%)</td><td>0.04 (+10.92%)</td><td>0.03 (-17.53%)</td><td>0.01 <b>(-39.15%)</b></td><td>616.60 <b>(+21.26%)</b></td><td>448.28 (+12.49%)</td><td>416.00 (-9.84%)</td><td>317.40 <b>(+26.00%)</b></td><td>122.67 (-5.98%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>508.50 (n/a)</td><td>398.52 (n/a)</td><td>461.40 (n/a)</td><td>251.90 (n/a)</td><td>130.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.05 <b>(-24.78%)</b></td><td>0.04 (-19.25%)</td><td>0.04 <b>(-21.69%)</b></td><td>0.03 (-10.06%)</td><td>0.01 <b>(-49.64%)</b></td><td>573.50 (+11.19%)</td><td>473.20 (+19.89%)</td><td>450.30 <b>(+27.71%)</b></td><td>386.40 <b>(+32.97%)</b></td><td>73.96 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>515.80 (n/a)</td><td>394.68 (n/a)</td><td>352.60 (n/a)</td><td>290.60 (n/a)</td><td>101.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+13.81%)</td><td>0.05 (+8.55%)</td><td>0.06 (+5.77%)</td><td>0.03 <b>(+230.81%)</b></td><td>0.02 (-10.19%)</td><td>590.10 <b>(-69.77%)</b></td><td>390.40 <b>(-38.65%)</b></td><td>279.70 (-5.44%)</td><td>238.90 (-12.14%)</td><td>173.75 <b>(-76.40%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1952.00 (n/a)</td><td>636.36 (n/a)</td><td>295.80 (n/a)</td><td>271.90 (n/a)</td><td>736.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 <b>(+41.43%)</b></td><td>0.05 (+17.12%)</td><td>0.04 (+2.56%)</td><td>0.03 (+0.68%)</td><td>0.03 <b>(+81.03%)</b></td><td>610.60 (-0.68%)</td><td>424.50 (-6.64%)</td><td>449.80 (-2.49%)</td><td>186.90 <b>(-29.28%)</b></td><td>160.14 <b>(+27.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.80 (n/a)</td><td>454.68 (n/a)</td><td>461.30 (n/a)</td><td>264.30 (n/a)</td><td>125.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.04 <b>(-24.72%)</b></td><td>0.03 (-17.68%)</td><td>0.03 (-18.33%)</td><td>0.03 (+0.13%)</td><td>0.00 <b>(-56.54%)</b></td><td>610.00 (-0.13%)</td><td>552.96 (+17.28%)</td><td>553.70 <b>(+22.45%)</b></td><td>450.00 <b>(+32.86%)</b></td><td>63.72 <b>(-43.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>610.80 (n/a)</td><td>471.50 (n/a)</td><td>452.20 (n/a)</td><td>338.70 (n/a)</td><td>113.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (+8.28%)</td><td>0.10 (-3.82%)</td><td>0.11 (-4.44%)</td><td>0.06 (-13.35%)</td><td>0.03 <b>(+45.23%)</b></td><td>535.20 (+15.39%)</td><td>379.44 (+9.86%)</td><td>307.50 (+4.66%)</td><td>259.20 (-7.66%)</td><td>135.89 <b>(+63.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>463.80 (n/a)</td><td>345.38 (n/a)</td><td>293.80 (n/a)</td><td>280.70 (n/a)</td><td>82.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.19 <b>(+38.21%)</b></td><td>0.10 (+16.86%)</td><td>0.05 (-13.26%)</td><td>0.05 (+4.98%)</td><td>0.06 <b>(+67.03%)</b></td><td>634.40 (-4.74%)</td><td>455.10 (-0.87%)</td><td>598.50 (+15.27%)</td><td>172.20 <b>(-27.65%)</b></td><td>229.54 <b>(+26.46%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.00 (n/a)</td><td>459.08 (n/a)</td><td>519.20 (n/a)</td><td>238.00 (n/a)</td><td>181.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (-0.89%)</td><td>0.10 (-3.40%)</td><td>0.07 <b>(-26.71%)</b></td><td>0.06 (-8.17%)</td><td>0.05 (+19.95%)</td><td>678.00 (+8.90%)</td><td>484.82 (+9.86%)</td><td>583.70 <b>(+36.44%)</b></td><td>253.50 (+0.92%)</td><td>208.93 <b>(+23.02%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>622.60 (n/a)</td><td>441.30 (n/a)</td><td>427.80 (n/a)</td><td>251.20 (n/a)</td><td>169.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 <b>(+53.77%)</b></td><td>0.10 <b>(+67.06%)</b></td><td>0.11 <b>(+82.89%)</b></td><td>0.05 <b>(+209.06%)</b></td><td>0.05 <b>(+30.96%)</b></td><td>622.90 <b>(-67.64%)</b></td><td>377.60 <b>(-52.20%)</b></td><td>299.70 <b>(-45.32%)</b></td><td>195.30 <b>(-34.97%)</b></td><td>179.17 <b>(-72.83%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1925.10 (n/a)</td><td>789.92 (n/a)</td><td>548.10 (n/a)</td><td>300.30 (n/a)</td><td>659.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (-2.36%)</td><td>0.08 <b>(-24.84%)</b></td><td>0.07 <b>(-22.97%)</b></td><td>0.02 <b>(-69.01%)</b></td><td>0.05 (+14.63%)</td><td>2510.90 <b>(+222.74%)</b></td><td>877.78 <b>(+97.20%)</b></td><td>564.90 <b>(+29.83%)</b></td><td>251.30 (+2.40%)</td><td>922.17 <b>(+338.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>778.00 (n/a)</td><td>445.12 (n/a)</td><td>435.10 (n/a)</td><td>245.40 (n/a)</td><td>210.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 <b>(+22.96%)</b></td><td>0.09 (-7.97%)</td><td>0.07 <b>(-30.45%)</b></td><td>0.03 <b>(-52.89%)</b></td><td>0.05 <b>(+98.05%)</b></td><td>1082.40 <b>(+112.28%)</b></td><td>525.50 <b>(+40.20%)</b></td><td>488.00 <b>(+43.78%)</b></td><td>217.80 (-18.67%)</td><td>344.71 <b>(+226.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>509.90 (n/a)</td><td>374.82 (n/a)</td><td>339.40 (n/a)</td><td>267.80 (n/a)</td><td>105.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.20 <b>(+90.85%)</b></td><td>0.11 <b>(+38.24%)</b></td><td>0.08 (+3.08%)</td><td>0.06 (+9.10%)</td><td>0.06 <b>(+235.66%)</b></td><td>584.50 (-8.34%)</td><td>397.06 (-15.81%)</td><td>463.40 (-2.99%)</td><td>184.00 <b>(-47.59%)</b></td><td>170.09 <b>(+58.64%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>637.70 (n/a)</td><td>471.60 (n/a)</td><td>477.70 (n/a)</td><td>351.10 (n/a)</td><td>107.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 <b>(-27.16%)</b></td><td>0.06 <b>(-38.33%)</b></td><td>0.06 <b>(-47.93%)</b></td><td>0.02 <b>(-72.08%)</b></td><td>0.03 (-2.02%)</td><td>1801.90 <b>(+258.16%)</b></td><td>765.94 <b>(+109.41%)</b></td><td>575.80 <b>(+92.00%)</b></td><td>310.50 <b>(+37.27%)</b></td><td>600.68 <b>(+368.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.10 (n/a)</td><td>365.76 (n/a)</td><td>299.90 (n/a)</td><td>226.20 (n/a)</td><td>128.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 <b>(+22.56%)</b></td><td>0.08 (+2.37%)</td><td>0.07 (-12.85%)</td><td>0.05 (-12.49%)</td><td>0.04 <b>(+61.57%)</b></td><td>671.10 (+14.27%)</td><td>503.40 (+4.84%)</td><td>544.80 (+14.74%)</td><td>247.70 (-18.41%)</td><td>167.60 <b>(+47.41%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.30 (n/a)</td><td>480.18 (n/a)</td><td>474.80 (n/a)</td><td>303.60 (n/a)</td><td>113.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 <b>(+31.59%)</b></td><td>0.07 (-16.39%)</td><td>0.06 <b>(-34.28%)</b></td><td>0.02 <b>(-64.16%)</b></td><td>0.04 <b>(+98.08%)</b></td><td>1894.50 <b>(+179.01%)</b></td><td>761.78 <b>(+72.39%)</b></td><td>584.60 <b>(+52.16%)</b></td><td>234.90 <b>(-24.01%)</b></td><td>650.88 <b>(+340.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>679.00 (n/a)</td><td>441.90 (n/a)</td><td>384.20 (n/a)</td><td>309.10 (n/a)</td><td>147.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (-3.37%)</td><td>0.06 (+2.27%)</td><td>0.05 (-6.20%)</td><td>0.03 (+5.31%)</td><td>0.02 (-0.91%)</td><td>621.40 (-5.03%)</td><td>418.20 (-3.11%)</td><td>439.70 (+6.62%)</td><td>246.00 (+3.49%)</td><td>160.44 (-7.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>654.30 (n/a)</td><td>431.62 (n/a)</td><td>412.40 (n/a)</td><td>237.70 (n/a)</td><td>173.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (-5.00%)</td><td>0.05 (-10.23%)</td><td>0.05 <b>(-27.54%)</b></td><td>0.04 (+16.63%)</td><td>0.01 <b>(-28.51%)</b></td><td>505.20 (-14.26%)</td><td>412.52 (+5.78%)</td><td>427.80 <b>(+38.00%)</b></td><td>279.80 (+5.27%)</td><td>91.60 <b>(-35.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.20 (n/a)</td><td>389.98 (n/a)</td><td>310.00 (n/a)</td><td>265.80 (n/a)</td><td>142.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 <b>(-21.62%)</b></td><td>0.04 (-14.43%)</td><td>0.04 (+13.36%)</td><td>0.01 <b>(-69.97%)</b></td><td>0.02 (-8.27%)</td><td>1855.90 <b>(+232.96%)</b></td><td>725.54 <b>(+52.33%)</b></td><td>470.00 (-11.79%)</td><td>289.80 <b>(+27.61%)</b></td><td>639.65 <b>(+356.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>557.40 (n/a)</td><td>476.28 (n/a)</td><td>532.80 (n/a)</td><td>227.10 (n/a)</td><td>139.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 (+1.62%)</td><td>0.07 <b>(+47.45%)</b></td><td>0.07 <b>(+78.24%)</b></td><td>0.04 <b>(+37.55%)</b></td><td>0.02 (-19.17%)</td><td>467.70 <b>(-27.31%)</b></td><td>302.98 <b>(-35.72%)</b></td><td>279.20 <b>(-43.90%)</b></td><td>229.90 (-1.63%)</td><td>96.29 <b>(-35.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>643.40 (n/a)</td><td>471.36 (n/a)</td><td>497.70 (n/a)</td><td>233.70 (n/a)</td><td>149.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(+50.16%)</b></td><td>0.05 <b>(+23.08%)</b></td><td>0.05 (+11.85%)</td><td>0.01 <b>(-44.31%)</b></td><td>0.03 <b>(+126.37%)</b></td><td>1928.20 <b>(+79.55%)</b></td><td>723.76 <b>(+22.85%)</b></td><td>444.40 (-10.60%)</td><td>247.70 <b>(-33.40%)</b></td><td>701.34 <b>(+148.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1073.90 (n/a)</td><td>589.12 (n/a)</td><td>497.10 (n/a)</td><td>371.90 (n/a)</td><td>282.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 <b>(+64.24%)</b></td><td>0.06 (+18.72%)</td><td>0.06 <b>(+33.03%)</b></td><td>0.03 <b>(-25.61%)</b></td><td>0.03 <b>(+180.25%)</b></td><td>633.80 <b>(+34.42%)</b></td><td>388.02 (-4.72%)</td><td>338.60 <b>(-24.82%)</b></td><td>194.90 <b>(-39.11%)</b></td><td>164.27 <b>(+128.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>407.26 (n/a)</td><td>450.40 (n/a)</td><td>320.10 (n/a)</td><td>72.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 (+7.77%)</td><td>0.07 (-9.95%)</td><td>0.05 <b>(-40.26%)</b></td><td>0.05 (+12.68%)</td><td>0.03 (+0.24%)</td><td>545.90 (-11.25%)</td><td>404.04 (+8.86%)</td><td>454.00 <b>(+67.34%)</b></td><td>226.50 (-7.21%)</td><td>135.26 (-16.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>615.10 (n/a)</td><td>371.16 (n/a)</td><td>271.30 (n/a)</td><td>244.10 (n/a)</td><td>161.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (-0.10%)</td><td>0.07 (+11.52%)</td><td>0.09 <b>(+45.30%)</b></td><td>0.04 (-18.60%)</td><td>0.03 <b>(+34.42%)</b></td><td>636.80 <b>(+22.86%)</b></td><td>399.44 (-1.41%)</td><td>288.80 <b>(-31.17%)</b></td><td>237.80 (+0.13%)</td><td>187.54 <b>(+82.29%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>518.30 (n/a)</td><td>405.14 (n/a)</td><td>419.60 (n/a)</td><td>237.50 (n/a)</td><td>102.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.06 <b>(-44.69%)</b></td><td>0.04 <b>(-38.17%)</b></td><td>0.05 (-15.28%)</td><td>0.01 <b>(-71.15%)</b></td><td>0.02 <b>(-38.47%)</b></td><td>1877.10 <b>(+246.58%)</b></td><td>765.56 <b>(+92.19%)</b></td><td>525.10 (+18.03%)</td><td>400.40 <b>(+80.85%)</b></td><td>626.38 <b>(+308.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>541.60 (n/a)</td><td>398.34 (n/a)</td><td>444.90 (n/a)</td><td>221.40 (n/a)</td><td>153.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (-3.70%)</td><td>0.06 (-16.87%)</td><td>0.05 <b>(-39.32%)</b></td><td>0.03 (-18.12%)</td><td>0.03 (-9.11%)</td><td>718.60 <b>(+22.13%)</b></td><td>460.28 (+19.67%)</td><td>492.20 <b>(+64.84%)</b></td><td>243.30 (+3.84%)</td><td>191.93 (+9.26%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>588.40 (n/a)</td><td>384.62 (n/a)</td><td>298.60 (n/a)</td><td>234.30 (n/a)</td><td>175.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.10 (+17.46%)</td><td>0.07 (-3.66%)</td><td>0.06 <b>(-25.15%)</b></td><td>0.04 (-10.66%)</td><td>0.03 <b>(+33.55%)</b></td><td>585.20 (+11.91%)</td><td>410.78 (+7.96%)</td><td>444.20 <b>(+33.59%)</b></td><td>235.50 (-14.89%)</td><td>140.05 <b>(+23.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>522.90 (n/a)</td><td>380.48 (n/a)</td><td>332.50 (n/a)</td><td>276.70 (n/a)</td><td>113.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 <b>(+85.77%)</b></td><td>0.09 <b>(+52.03%)</b></td><td>0.08 <b>(+53.13%)</b></td><td>0.05 (+18.46%)</td><td>0.04 <b>(+161.52%)</b></td><td>504.60 (-15.59%)</td><td>323.02 <b>(-28.65%)</b></td><td>299.40 <b>(-34.70%)</b></td><td>169.30 <b>(-46.19%)</b></td><td>122.95 (+17.91%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>452.70 (n/a)</td><td>458.50 (n/a)</td><td>314.60 (n/a)</td><td>104.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 (+12.97%)</td><td>0.06 (+7.17%)</td><td>0.06 (+2.69%)</td><td>0.04 (-5.00%)</td><td>0.02 (+19.12%)</td><td>518.80 (+5.28%)</td><td>348.96 (-5.08%)</td><td>295.60 (-2.64%)</td><td>242.60 (-11.49%)</td><td>116.71 (+8.63%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>492.80 (n/a)</td><td>367.64 (n/a)</td><td>303.60 (n/a)</td><td>274.10 (n/a)</td><td>107.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+4.40%)</td><td>0.06 (+18.00%)</td><td>0.06 <b>(+53.54%)</b></td><td>0.04 <b>(+20.53%)</b></td><td>0.01 <b>(-31.70%)</b></td><td>442.50 (-17.04%)</td><td>321.96 (-19.81%)</td><td>298.40 <b>(-34.88%)</b></td><td>252.80 (-4.21%)</td><td>74.66 <b>(-41.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.40 (n/a)</td><td>401.52 (n/a)</td><td>458.20 (n/a)</td><td>263.90 (n/a)</td><td>127.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(+25.71%)</b></td><td>0.06 <b>(+30.23%)</b></td><td>0.06 <b>(+52.32%)</b></td><td>0.04 <b>(+34.82%)</b></td><td>0.02 <b>(+28.86%)</b></td><td>501.50 <b>(-25.84%)</b></td><td>351.44 <b>(-22.96%)</b></td><td>309.90 <b>(-34.34%)</b></td><td>224.00 <b>(-20.45%)</b></td><td>117.45 <b>(-20.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>676.20 (n/a)</td><td>456.18 (n/a)</td><td>472.00 (n/a)</td><td>281.60 (n/a)</td><td>148.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(+20.73%)</b></td><td>0.04 <b>(+30.77%)</b></td><td>0.03 (+4.13%)</td><td>0.03 <b>(+205.52%)</b></td><td>0.02 (-7.56%)</td><td>599.00 <b>(-67.27%)</b></td><td>489.88 <b>(-42.21%)</b></td><td>558.10 (-3.96%)</td><td>244.20 (-17.16%)</td><td>143.10 <b>(-76.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1830.10 (n/a)</td><td>847.70 (n/a)</td><td>581.10 (n/a)</td><td>294.80 (n/a)</td><td>617.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.09 <b>(+35.52%)</b></td><td>0.06 (+17.13%)</td><td>0.06 <b>(+24.07%)</b></td><td>0.04 (-11.12%)</td><td>0.02 <b>(+100.68%)</b></td><td>491.10 (+12.51%)</td><td>317.94 (-9.24%)</td><td>291.80 (-19.41%)</td><td>207.00 <b>(-26.20%)</b></td><td>110.86 <b>(+72.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>436.50 (n/a)</td><td>350.32 (n/a)</td><td>362.10 (n/a)</td><td>280.50 (n/a)</td><td>64.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 (+6.73%)</td><td>0.05 (+2.97%)</td><td>0.04 (+1.98%)</td><td>0.03 (-5.67%)</td><td>0.02 (-1.16%)</td><td>608.30 (+6.01%)</td><td>416.18 (-3.43%)</td><td>434.10 (-1.96%)</td><td>264.50 (-6.34%)</td><td>136.43 (-3.28%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.80 (n/a)</td><td>430.94 (n/a)</td><td>442.80 (n/a)</td><td>282.40 (n/a)</td><td>141.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (+19.28%)</td><td>0.29 (-15.70%)</td><td>0.28 (-16.26%)</td><td>0.14 <b>(-55.00%)</b></td><td>0.12 <b>(+275.96%)</b></td><td>702.90 <b>(+122.23%)</b></td><td>400.14 <b>(+36.83%)</b></td><td>348.70 (+19.38%)</td><td>213.50 (-16.14%)</td><td>184.29 <b>(+615.31%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.03 (n/a)</td><td>316.30 (n/a)</td><td>292.44 (n/a)</td><td>292.10 (n/a)</td><td>254.60 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.32 (+0.54%)</td><td>0.20 (-12.68%)</td><td>0.20 (-1.13%)</td><td>0.04 <b>(-75.11%)</b></td><td>0.10 <b>(+60.22%)</b></td><td>2430.50 <b>(+301.80%)</b></td><td>825.64 <b>(+81.64%)</b></td><td>479.70 (+1.14%)</td><td>305.70 (-0.55%)</td><td>900.26 <b>(+658.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>604.90 (n/a)</td><td>454.54 (n/a)</td><td>474.30 (n/a)</td><td>307.40 (n/a)</td><td>118.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.35 (+2.23%)</td><td>0.20 (-9.88%)</td><td>0.19 (-3.00%)</td><td>0.05 <b>(-67.31%)</b></td><td>0.11 <b>(+37.24%)</b></td><td>1986.10 <b>(+205.88%)</b></td><td>748.12 <b>(+55.66%)</b></td><td>524.70 (+3.08%)</td><td>283.10 (-2.18%)</td><td>699.97 <b>(+364.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>649.30 (n/a)</td><td>480.62 (n/a)</td><td>509.00 (n/a)</td><td>289.40 (n/a)</td><td>150.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.30 (+15.51%)</td><td>0.22 <b>(+30.39%)</b></td><td>0.21 <b>(+47.86%)</b></td><td>0.15 <b>(+402.60%)</b></td><td>0.07 <b>(-32.02%)</b></td><td>489.50 <b>(-80.10%)</b></td><td>365.76 <b>(-55.07%)</b></td><td>345.90 <b>(-32.36%)</b></td><td>244.90 (-13.43%)</td><td>110.19 <b>(-88.13%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.10 (n/a)</td><td>2460.20 (n/a)</td><td>814.04 (n/a)</td><td>511.40 (n/a)</td><td>282.90 (n/a)</td><td>927.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 <b>(+54.95%)</b></td><td>0.18 <b>(+21.74%)</b></td><td>0.16 (+18.59%)</td><td>0.13 (-0.77%)</td><td>0.05 <b>(+216.39%)</b></td><td>554.30 (+0.78%)</td><td>433.72 (-13.57%)</td><td>451.10 (-15.68%)</td><td>284.10 <b>(-35.48%)</b></td><td>111.96 <b>(+108.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>550.00 (n/a)</td><td>501.80 (n/a)</td><td>535.00 (n/a)</td><td>440.30 (n/a)</td><td>53.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.26 (+4.30%)</td><td>0.18 <b>(+27.36%)</b></td><td>0.16 <b>(+26.33%)</b></td><td>0.13 <b>(+256.60%)</b></td><td>0.05 <b>(-38.90%)</b></td><td>552.70 <b>(-71.96%)</b></td><td>436.32 <b>(-44.82%)</b></td><td>451.40 <b>(-20.85%)</b></td><td>283.70 (-4.12%)</td><td>96.73 <b>(-85.70%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1971.00 (n/a)</td><td>790.68 (n/a)</td><td>570.30 (n/a)</td><td>295.90 (n/a)</td><td>676.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (+7.25%)</td><td>0.09 <b>(-21.12%)</b></td><td>0.08 <b>(-38.93%)</b></td><td>0.02 <b>(-80.49%)</b></td><td>0.06 <b>(+82.85%)</b></td><td>2417.40 <b>(+412.49%)</b></td><td>809.62 <b>(+134.47%)</b></td><td>447.90 <b>(+63.77%)</b></td><td>236.00 (-6.76%)</td><td>918.09 <b>(+730.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>471.70 (n/a)</td><td>345.30 (n/a)</td><td>273.50 (n/a)</td><td>253.10 (n/a)</td><td>110.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (-4.07%)</td><td>0.09 (-11.49%)</td><td>0.08 <b>(-37.58%)</b></td><td>0.06 (-2.49%)</td><td>0.03 (-12.52%)</td><td>650.00 (+2.56%)</td><td>442.44 (+9.72%)</td><td>483.90 <b>(+60.18%)</b></td><td>269.50 (+4.22%)</td><td>155.82 (-10.26%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>633.80 (n/a)</td><td>403.26 (n/a)</td><td>302.10 (n/a)</td><td>258.60 (n/a)</td><td>173.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 <b>(-34.25%)</b></td><td>0.10 (-10.68%)</td><td>0.11 (-0.03%)</td><td>0.07 <b>(+24.09%)</b></td><td>0.03 <b>(-48.68%)</b></td><td>548.10 (-19.41%)</td><td>380.56 (-2.31%)</td><td>351.10 (+0.06%)</td><td>267.00 <b>(+52.14%)</b></td><td>121.06 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>680.10 (n/a)</td><td>389.54 (n/a)</td><td>350.90 (n/a)</td><td>175.50 (n/a)</td><td>196.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (-10.78%)</td><td>0.10 (-5.44%)</td><td>0.09 <b>(-27.45%)</b></td><td>0.06 <b>(+219.20%)</b></td><td>0.04 <b>(-37.38%)</b></td><td>575.30 <b>(-68.67%)</b></td><td>406.56 <b>(-34.13%)</b></td><td>410.60 <b>(+37.88%)</b></td><td>264.30 (+12.09%)</td><td>142.25 <b>(-79.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1836.40 (n/a)</td><td>617.18 (n/a)</td><td>297.80 (n/a)</td><td>235.80 (n/a)</td><td>688.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (+19.74%)</td><td>0.11 (+16.87%)</td><td>0.12 <b>(+43.85%)</b></td><td>0.05 <b>(-21.25%)</b></td><td>0.05 <b>(+48.91%)</b></td><td>731.30 <b>(+26.98%)</b></td><td>417.58 (-5.49%)</td><td>307.20 <b>(-30.48%)</b></td><td>221.70 (-16.47%)</td><td>209.97 <b>(+57.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.90 (n/a)</td><td>441.86 (n/a)</td><td>441.90 (n/a)</td><td>265.40 (n/a)</td><td>133.30 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (+8.30%)</td><td>0.11 <b>(+25.67%)</b></td><td>0.10 <b>(+70.57%)</b></td><td>0.08 <b>(+42.53%)</b></td><td>0.03 <b>(-35.32%)</b></td><td>474.90 <b>(-29.83%)</b></td><td>346.98 <b>(-29.52%)</b></td><td>359.50 <b>(-41.36%)</b></td><td>244.70 (-7.70%)</td><td>86.50 <b>(-57.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>676.80 (n/a)</td><td>492.32 (n/a)</td><td>613.10 (n/a)</td><td>265.10 (n/a)</td><td>201.96 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 (+10.65%)</td><td>0.14 <b>(+25.09%)</b></td><td>0.14 <b>(+37.71%)</b></td><td>0.09 <b>(+28.72%)</b></td><td>0.04 (-6.73%)</td><td>461.00 <b>(-22.30%)</b></td><td>302.86 <b>(-22.73%)</b></td><td>288.30 <b>(-27.38%)</b></td><td>227.80 (-9.64%)</td><td>94.32 <b>(-31.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>593.30 (n/a)</td><td>391.94 (n/a)</td><td>397.00 (n/a)</td><td>252.10 (n/a)</td><td>138.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (-9.13%)</td><td>0.11 (-14.44%)</td><td>0.09 <b>(-31.19%)</b></td><td>0.07 <b>(-24.35%)</b></td><td>0.05 (+19.55%)</td><td>567.60 <b>(+32.18%)</b></td><td>415.78 <b>(+24.78%)</b></td><td>445.80 <b>(+45.35%)</b></td><td>235.70 (+10.04%)</td><td>156.82 <b>(+68.65%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>429.40 (n/a)</td><td>333.22 (n/a)</td><td>306.70 (n/a)</td><td>214.20 (n/a)</td><td>92.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 <b>(-30.03%)</b></td><td>0.10 <b>(-23.82%)</b></td><td>0.09 <b>(-28.44%)</b></td><td>0.08 (-13.35%)</td><td>0.02 <b>(-41.91%)</b></td><td>533.20 (+15.41%)</td><td>435.10 <b>(+27.45%)</b></td><td>461.80 <b>(+39.73%)</b></td><td>313.20 <b>(+42.88%)</b></td><td>91.74 (-4.75%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>462.00 (n/a)</td><td>341.40 (n/a)</td><td>330.50 (n/a)</td><td>219.20 (n/a)</td><td>96.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.15 (-16.51%)</td><td>0.09 (-19.02%)</td><td>0.08 <b>(-41.52%)</b></td><td>0.07 <b>(+245.89%)</b></td><td>0.03 <b>(-49.34%)</b></td><td>551.40 <b>(-71.09%)</b></td><td>461.44 <b>(-26.21%)</b></td><td>516.20 <b>(+71.04%)</b></td><td>277.60 (+19.76%)</td><td>113.45 <b>(-84.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1907.30 (n/a)</td><td>625.34 (n/a)</td><td>301.80 (n/a)</td><td>231.80 (n/a)</td><td>720.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.17 (+4.04%)</td><td>0.13 (+17.42%)</td><td>0.11 <b>(+26.26%)</b></td><td>0.09 <b>(+39.09%)</b></td><td>0.04 <b>(-21.45%)</b></td><td>461.50 <b>(-28.10%)</b></td><td>347.32 <b>(-21.83%)</b></td><td>380.30 <b>(-20.79%)</b></td><td>244.30 (-3.89%)</td><td>97.78 <b>(-45.93%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>641.90 (n/a)</td><td>444.32 (n/a)</td><td>480.10 (n/a)</td><td>254.20 (n/a)</td><td>180.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 (+15.46%)</td><td>0.12 <b>(+49.67%)</b></td><td>0.15 <b>(+87.89%)</b></td><td>0.08 <b>(+101.28%)</b></td><td>0.04 (+11.08%)</td><td>537.70 <b>(-50.31%)</b></td><td>363.28 <b>(-37.86%)</b></td><td>273.30 <b>(-46.78%)</b></td><td>260.50 (-13.37%)</td><td>131.63 <b>(-55.32%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1082.20 (n/a)</td><td>584.66 (n/a)</td><td>513.50 (n/a)</td><td>300.70 (n/a)</td><td>294.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.14 (-1.21%)</td><td>0.12 <b>(+33.23%)</b></td><td>0.13 <b>(+68.62%)</b></td><td>0.11 <b>(+103.41%)</b></td><td>0.01 <b>(-63.05%)</b></td><td>323.80 <b>(-50.84%)</b></td><td>284.88 <b>(-32.94%)</b></td><td>272.80 <b>(-40.68%)</b></td><td>247.90 (+1.22%)</td><td>31.13 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>658.70 (n/a)</td><td>424.80 (n/a)</td><td>459.90 (n/a)</td><td>244.90 (n/a)</td><td>162.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 <b>(+20.00%)</b></td><td>0.11 (+1.67%)</td><td>0.10 (-12.78%)</td><td>0.06 (-12.17%)</td><td>0.05 <b>(+49.61%)</b></td><td>560.50 (+13.85%)</td><td>383.26 (+6.08%)</td><td>354.60 (+14.65%)</td><td>211.20 (-16.65%)</td><td>160.30 <b>(+42.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>492.30 (n/a)</td><td>361.30 (n/a)</td><td>309.30 (n/a)</td><td>253.40 (n/a)</td><td>112.61 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (+4.70%)</td><td>0.09 (+11.96%)</td><td>0.08 (+18.50%)</td><td>0.05 (-8.52%)</td><td>0.03 (+11.93%)</td><td>648.20 (+9.31%)</td><td>435.14 (-8.65%)</td><td>435.30 (-15.62%)</td><td>261.30 (-4.50%)</td><td>151.28 (+18.75%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>593.00 (n/a)</td><td>476.36 (n/a)</td><td>515.90 (n/a)</td><td>273.60 (n/a)</td><td>127.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.08 <b>(-56.63%)</b></td><td>0.07 <b>(-22.23%)</b></td><td>0.07 (+10.88%)</td><td>0.06 (-0.33%)</td><td>0.01 <b>(-79.14%)</b></td><td>628.00 (+0.34%)</td><td>521.44 (+7.24%)</td><td>481.00 (-9.82%)</td><td>421.30 <b>(+130.60%)</b></td><td>94.21 <b>(-46.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>625.90 (n/a)</td><td>486.24 (n/a)</td><td>533.40 (n/a)</td><td>182.70 (n/a)</td><td>177.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.16 <b>(+20.66%)</b></td><td>0.12 (+17.20%)</td><td>0.12 <b>(+36.29%)</b></td><td>0.08 (+19.82%)</td><td>0.03 (-1.89%)</td><td>451.50 (-16.53%)</td><td>319.04 (-16.63%)</td><td>292.50 <b>(-26.62%)</b></td><td>217.50 (-17.14%)</td><td>88.78 <b>(-26.38%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.90 (n/a)</td><td>382.66 (n/a)</td><td>398.60 (n/a)</td><td>262.50 (n/a)</td><td>120.60 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.18 <b>(+121.83%)</b></td><td>0.11 <b>(+56.84%)</b></td><td>0.10 <b>(+58.09%)</b></td><td>0.05 (-11.07%)</td><td>0.05 <b>(+482.21%)</b></td><td>645.70 (+12.45%)</td><td>385.06 <b>(-26.03%)</b></td><td>349.40 <b>(-36.74%)</b></td><td>198.30 <b>(-54.91%)</b></td><td>172.47 <b>(+195.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>574.20 (n/a)</td><td>520.58 (n/a)</td><td>552.30 (n/a)</td><td>439.80 (n/a)</td><td>58.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.29 <b>(-38.48%)</b></td><td>0.23 <b>(-26.97%)</b></td><td>0.22 (-13.57%)</td><td>0.21 (-2.49%)</td><td>0.03 <b>(-69.36%)</b></td><td>631.40 (+2.57%)</td><td>572.32 <b>(+26.66%)</b></td><td>593.00 (+15.68%)</td><td>449.10 <b>(+62.54%)</b></td><td>74.20 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>615.60 (n/a)</td><td>451.84 (n/a)</td><td>512.60 (n/a)</td><td>276.30 (n/a)</td><td>143.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.46 (+16.88%)</td><td>0.27 (-11.75%)</td><td>0.24 (-18.85%)</td><td>0.20 (-3.44%)</td><td>0.11 <b>(+26.11%)</b></td><td>666.30 (+3.58%)</td><td>533.26 (+16.21%)</td><td>539.60 <b>(+23.22%)</b></td><td>287.00 (-14.43%)</td><td>149.14 (+11.56%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>643.30 (n/a)</td><td>458.86 (n/a)</td><td>437.90 (n/a)</td><td>335.40 (n/a)</td><td>133.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.42 (-16.42%)</td><td>0.33 (-13.09%)</td><td>0.34 (-18.04%)</td><td>0.23 (+2.19%)</td><td>0.08 <b>(-37.82%)</b></td><td>571.50 (-2.14%)</td><td>413.20 (+8.84%)</td><td>381.00 <b>(+22.00%)</b></td><td>311.60 (+19.66%)</td><td>108.05 <b>(-25.45%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>584.00 (n/a)</td><td>379.64 (n/a)</td><td>312.30 (n/a)</td><td>260.40 (n/a)</td><td>144.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.01 (-4.49%)</td><td>0.01 (+16.16%)</td><td>0.01 <b>(+52.40%)</b></td><td>0.01 (-2.57%)</td><td>0.00 (-14.93%)</td><td>505.30 (+2.64%)</td><td>338.04 (-14.90%)</td><td>293.60 <b>(-34.38%)</b></td><td>282.80 (+4.70%)</td><td>94.28 (-6.44%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.30 (n/a)</td><td>397.24 (n/a)</td><td>447.40 (n/a)</td><td>270.10 (n/a)</td><td>100.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 <b>(+33.06%)</b></td><td>0.01 <b>(+27.85%)</b></td><td>0.01 <b>(+29.26%)</b></td><td>0.01 (-15.77%)</td><td>0.00 <b>(+103.04%)</b></td><td>525.90 (+18.71%)</td><td>309.96 (-16.01%)</td><td>289.10 <b>(-22.64%)</b></td><td>217.90 <b>(-24.84%)</b></td><td>125.52 <b>(+84.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>443.00 (n/a)</td><td>369.06 (n/a)</td><td>373.70 (n/a)</td><td>289.90 (n/a)</td><td>68.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (+5.12%)</td><td>0.01 (-10.28%)</td><td>0.01 <b>(-34.55%)</b></td><td>0.01 (-6.34%)</td><td>0.00 <b>(+28.06%)</b></td><td>531.10 (+6.78%)</td><td>407.58 (+15.88%)</td><td>456.80 <b>(+52.78%)</b></td><td>250.80 (-4.86%)</td><td>132.42 <b>(+31.23%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.40 (n/a)</td><td>351.72 (n/a)</td><td>299.00 (n/a)</td><td>263.60 (n/a)</td><td>100.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.54 <b>(-25.88%)</b></td><td>5.25 <b>(-24.39%)</b></td><td>4.55 <b>(-41.52%)</b></td><td>4.15 <b>(+31.10%)</b></td><td>1.17 <b>(-48.79%)</b></td><td>506.20 <b>(-23.72%)</b></td><td>414.96 (+19.19%)</td><td>461.20 <b>(+71.00%)</b></td><td>320.70 <b>(+34.92%)</b></td><td>86.94 <b>(-51.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.83 (n/a)</td><td>6.95 (n/a)</td><td>7.78 (n/a)</td><td>3.16 (n/a)</td><td>2.28 (n/a)</td><td>663.60 (n/a)</td><td>348.14 (n/a)</td><td>269.70 (n/a)</td><td>237.70 (n/a)</td><td>179.17 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.57 (+9.66%)</td><td>0.33 <b>(-23.82%)</b></td><td>0.26 <b>(-47.03%)</b></td><td>0.07 <b>(-78.47%)</b></td><td>0.22 <b>(+153.96%)</b></td><td>1908.60 <b>(+364.61%)</b></td><td>694.02 <b>(+123.07%)</b></td><td>515.50 <b>(+88.76%)</b></td><td>231.00 (-8.80%)</td><td>696.46 <b>(+937.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>410.80 (n/a)</td><td>311.12 (n/a)</td><td>273.10 (n/a)</td><td>253.30 (n/a)</td><td>67.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.51 (-13.48%)</td><td>0.42 (-0.99%)</td><td>0.43 <b>(-22.00%)</b></td><td>0.22 <b>(+227.85%)</b></td><td>0.11 <b>(-48.23%)</b></td><td>587.70 <b>(-69.50%)</b></td><td>346.96 <b>(-42.60%)</b></td><td>307.60 <b>(+28.22%)</b></td><td>257.10 (+15.55%)</td><td>136.94 <b>(-81.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.55 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td><td>1926.80 (n/a)</td><td>604.42 (n/a)</td><td>239.90 (n/a)</td><td>222.50 (n/a)</td><td>742.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.53 (-6.38%)</td><td>0.35 <b>(-21.51%)</b></td><td>0.28 <b>(-40.43%)</b></td><td>0.24 (-7.33%)</td><td>0.12 (+8.28%)</td><td>546.80 (+7.91%)</td><td>411.78 <b>(+29.62%)</b></td><td>468.10 <b>(+67.90%)</b></td><td>247.00 (+6.83%)</td><td>124.92 (+15.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>506.70 (n/a)</td><td>317.68 (n/a)</td><td>278.80 (n/a)</td><td>231.20 (n/a)</td><td>108.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.47 <b>(-22.88%)</b></td><td>0.40 (-11.22%)</td><td>0.42 (-13.71%)</td><td>0.34 <b>(+72.62%)</b></td><td>0.06 <b>(-63.42%)</b></td><td>391.20 <b>(-42.06%)</b></td><td>336.12 (-1.99%)</td><td>314.10 (+15.86%)</td><td>283.80 <b>(+29.71%)</b></td><td>47.77 <b>(-74.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.60 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>675.20 (n/a)</td><td>342.94 (n/a)</td><td>271.10 (n/a)</td><td>218.80 (n/a)</td><td>187.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.50 (-8.43%)</td><td>0.38 (-5.19%)</td><td>0.34 <b>(-22.15%)</b></td><td>0.29 (+13.62%)</td><td>0.09 <b>(-26.76%)</b></td><td>450.70 (-11.99%)</td><td>361.84 (+1.23%)</td><td>386.50 <b>(+28.45%)</b></td><td>263.80 (+9.19%)</td><td>80.43 <b>(-32.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.55 (n/a)</td><td>0.40 (n/a)</td><td>0.44 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>512.10 (n/a)</td><td>357.46 (n/a)</td><td>300.90 (n/a)</td><td>241.60 (n/a)</td><td>118.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-10.06%)</td><td>0.01 <b>(-20.55%)</b></td><td>0.01 <b>(-25.25%)</b></td><td>0.01 (-2.41%)</td><td>0.00 (-16.78%)</td><td>471.30 (+2.48%)</td><td>364.92 <b>(+23.77%)</b></td><td>359.80 <b>(+33.75%)</b></td><td>248.80 (+11.17%)</td><td>82.97 (-12.11%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.90 (n/a)</td><td>294.84 (n/a)</td><td>269.00 (n/a)</td><td>223.80 (n/a)</td><td>94.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.02 (-4.93%)</td><td>0.01 (+10.81%)</td><td>0.01 <b>(+49.81%)</b></td><td>0.01 (-1.66%)</td><td>0.00 <b>(-21.68%)</b></td><td>522.50 (+1.69%)</td><td>329.62 (-13.03%)</td><td>293.10 <b>(-33.25%)</b></td><td>242.60 (+5.20%)</td><td>115.27 (-13.11%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.80 (n/a)</td><td>379.00 (n/a)</td><td>439.10 (n/a)</td><td>230.60 (n/a)</td><td>132.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(-31.25%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-72.78%)</b></td><td>22019.68 (+9.95%)</td><td>17899.81 <b>(+24.37%)</b></td><td>17201.35 (+10.70%)</td><td>16226.00 <b>(+143.83%)</b></td><td>2351.35 <b>(-53.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20026.59 (n/a)</td><td>14392.45 (n/a)</td><td>15538.62 (n/a)</td><td>6654.60 (n/a)</td><td>5015.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.00 <b>(-37.50%)</b></td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-75.38%)</b></td><td>21930.00 (+18.32%)</td><td>19061.53 <b>(+24.18%)</b></td><td>19557.26 (+11.25%)</td><td>15126.21 <b>(+48.94%)</b></td><td>2529.83 <b>(-36.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18534.09 (n/a)</td><td>15350.10 (n/a)</td><td>17579.26 (n/a)</td><td>10155.64 (n/a)</td><td>3987.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.11 <b>(-25.86%)</b></td><td>0.09 (-4.68%)</td><td>0.09 (+11.35%)</td><td>0.07 (+3.70%)</td><td>0.02 <b>(-48.91%)</b></td><td>28825.72 (-3.46%)</td><td>23754.39 (-0.05%)</td><td>24016.84 (-10.19%)</td><td>18650.20 <b>(+34.81%)</b></td><td>4354.71 <b>(-31.58%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29857.70 (n/a)</td><td>23765.74 (n/a)</td><td>26742.93 (n/a)</td><td>13834.25 (n/a)</td><td>6364.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.96 (+2.94%)</td><td>2.00 (+14.92%)</td><td>1.72 (+2.43%)</td><td>1.17 <b>(+124.28%)</b></td><td>0.84 (-12.86%)</td><td>895.10 <b>(-55.41%)</b></td><td>606.18 <b>(-30.41%)</b></td><td>608.20 (-2.38%)</td><td>354.40 (-2.85%)</td><td>244.51 <b>(-63.71%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.87 (n/a)</td><td>1.74 (n/a)</td><td>1.68 (n/a)</td><td>0.52 (n/a)</td><td>0.96 (n/a)</td><td>2007.50 (n/a)</td><td>871.06 (n/a)</td><td>623.00 (n/a)</td><td>364.80 (n/a)</td><td>673.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.64 (-10.05%)</td><td>1.91 (+14.15%)</td><td>1.67 (+15.86%)</td><td>0.30 (-1.78%)</td><td>1.22 (-13.58%)</td><td>3495.70 (+1.81%)</td><td>1105.82 (-9.98%)</td><td>627.70 (-13.68%)</td><td>288.30 (+11.18%)</td><td>1344.91 (+6.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.04 (n/a)</td><td>1.67 (n/a)</td><td>1.44 (n/a)</td><td>0.31 (n/a)</td><td>1.42 (n/a)</td><td>3433.60 (n/a)</td><td>1228.46 (n/a)</td><td>727.20 (n/a)</td><td>259.30 (n/a)</td><td>1264.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.35 <b>(+36.41%)</b></td><td>2.32 (+10.13%)</td><td>2.13 (+13.37%)</td><td>1.15 (-15.92%)</td><td>1.23 <b>(+78.39%)</b></td><td>914.00 (+18.95%)</td><td>548.48 (+1.74%)</td><td>492.00 (-11.80%)</td><td>241.10 <b>(-26.70%)</b></td><td>250.12 <b>(+54.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.19 (n/a)</td><td>2.10 (n/a)</td><td>1.88 (n/a)</td><td>1.36 (n/a)</td><td>0.69 (n/a)</td><td>768.40 (n/a)</td><td>539.10 (n/a)</td><td>557.80 (n/a)</td><td>328.90 (n/a)</td><td>161.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.54 (-3.17%)</td><td>2.19 (-3.70%)</td><td>1.49 (-14.04%)</td><td>0.30 <b>(-79.81%)</b></td><td>1.76 <b>(+30.11%)</b></td><td>3438.90 <b>(+395.23%)</b></td><td>1123.30 <b>(+104.39%)</b></td><td>704.50 (+16.35%)</td><td>231.00 (+3.26%)</td><td>1327.00 <b>(+613.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.69 (n/a)</td><td>2.27 (n/a)</td><td>1.73 (n/a)</td><td>1.51 (n/a)</td><td>1.35 (n/a)</td><td>694.40 (n/a)</td><td>549.58 (n/a)</td><td>605.50 (n/a)</td><td>223.70 (n/a)</td><td>186.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>2.37 <b>(-37.81%)</b></td><td>1.41 <b>(-42.69%)</b></td><td>1.09 <b>(-57.83%)</b></td><td>0.59 (-1.60%)</td><td>0.76 <b>(-41.07%)</b></td><td>3578.20 (+1.62%)</td><td>1920.08 <b>(+45.08%)</b></td><td>1919.10 <b>(+137.16%)</b></td><td>883.90 <b>(+60.80%)</b></td><td>1083.79 (-13.24%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.82 (n/a)</td><td>2.46 (n/a)</td><td>2.59 (n/a)</td><td>0.60 (n/a)</td><td>1.29 (n/a)</td><td>3521.00 (n/a)</td><td>1323.48 (n/a)</td><td>809.20 (n/a)</td><td>549.70 (n/a)</td><td>1249.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.41 <b>(+27.40%)</b></td><td>2.64 <b>(-29.31%)</b></td><td>1.82 <b>(-52.94%)</b></td><td>0.62 <b>(-67.79%)</b></td><td>2.46 <b>(+96.85%)</b></td><td>3404.40 <b>(+210.45%)</b></td><td>1765.60 <b>(+179.25%)</b></td><td>1151.50 <b>(+112.49%)</b></td><td>327.30 <b>(-21.51%)</b></td><td>1517.46 <b>(+448.95%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.03 (n/a)</td><td>3.74 (n/a)</td><td>3.87 (n/a)</td><td>1.91 (n/a)</td><td>1.25 (n/a)</td><td>1096.60 (n/a)</td><td>632.26 (n/a)</td><td>541.90 (n/a)</td><td>417.00 (n/a)</td><td>276.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.56 <b>(+68.15%)</b></td><td>3.41 (+13.14%)</td><td>2.83 (+2.92%)</td><td>0.99 <b>(-49.46%)</b></td><td>2.52 <b>(+167.78%)</b></td><td>2112.40 <b>(+97.85%)</b></td><td>949.08 <b>(+26.83%)</b></td><td>740.90 (-2.85%)</td><td>277.50 <b>(-40.53%)</b></td><td>706.56 <b>(+221.84%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.49 (n/a)</td><td>3.01 (n/a)</td><td>2.75 (n/a)</td><td>1.96 (n/a)</td><td>0.94 (n/a)</td><td>1067.70 (n/a)</td><td>748.32 (n/a)</td><td>762.60 (n/a)</td><td>466.60 (n/a)</td><td>219.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.34 (-13.77%)</td><td>3.62 <b>(+43.43%)</b></td><td>4.08 <b>(+154.95%)</b></td><td>1.74 <b>(+191.23%)</b></td><td>1.48 <b>(-38.02%)</b></td><td>1207.00 <b>(-65.66%)</b></td><td>687.62 <b>(-62.69%)</b></td><td>514.10 <b>(-60.78%)</b></td><td>392.60 (+15.95%)</td><td>340.05 <b>(-78.02%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.19 (n/a)</td><td>2.52 (n/a)</td><td>1.60 (n/a)</td><td>0.60 (n/a)</td><td>2.39 (n/a)</td><td>3515.10 (n/a)</td><td>1842.80 (n/a)</td><td>1310.70 (n/a)</td><td>338.60 (n/a)</td><td>1547.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.00 (-18.75%)</td><td>1.73 <b>(-53.65%)</b></td><td>0.61 <b>(-79.87%)</b></td><td>0.60 (-1.60%)</td><td>2.39 (-12.34%)</td><td>3485.80 (+1.63%)</td><td>2660.58 <b>(+129.24%)</b></td><td>3455.60 <b>(+396.85%)</b></td><td>349.80 <b>(+23.08%)</b></td><td>1355.35 (+4.19%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.38 (n/a)</td><td>3.73 (n/a)</td><td>3.02 (n/a)</td><td>0.61 (n/a)</td><td>2.72 (n/a)</td><td>3429.90 (n/a)</td><td>1160.60 (n/a)</td><td>695.50 (n/a)</td><td>284.20 (n/a)</td><td>1300.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>4.64 <b>(-35.14%)</b></td><td>3.14 (-4.27%)</td><td>3.22 (+16.45%)</td><td>0.59 (-3.68%)</td><td>1.66 <b>(-30.48%)</b></td><td>3550.90 (+3.82%)</td><td>1178.70 (-0.25%)</td><td>651.20 (-14.12%)</td><td>451.60 <b>(+54.18%)</b></td><td>1333.25 (+5.28%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.16 (n/a)</td><td>3.28 (n/a)</td><td>2.77 (n/a)</td><td>0.61 (n/a)</td><td>2.39 (n/a)</td><td>3420.40 (n/a)</td><td>1181.64 (n/a)</td><td>758.30 (n/a)</td><td>292.90 (n/a)</td><td>1266.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>5.19 (+13.93%)</td><td>3.66 (-6.49%)</td><td>3.69 (-7.52%)</td><td>1.76 <b>(-42.49%)</b></td><td>1.25 <b>(+133.34%)</b></td><td>2379.60 <b>(+73.88%)</b></td><td>1306.96 (+19.97%)</td><td>1138.00 (+8.13%)</td><td>808.10 (-12.23%)</td><td>619.11 <b>(+271.88%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.56 (n/a)</td><td>3.92 (n/a)</td><td>3.99 (n/a)</td><td>3.06 (n/a)</td><td>0.54 (n/a)</td><td>1368.50 (n/a)</td><td>1089.40 (n/a)</td><td>1052.40 (n/a)</td><td>920.70 (n/a)</td><td>166.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>7.71 (-12.41%)</td><td>5.75 <b>(+49.44%)</b></td><td>5.96 <b>(+52.61%)</b></td><td>3.48 <b>(+197.26%)</b></td><td>2.00 <b>(-35.26%)</b></td><td>1206.80 <b>(-66.36%)</b></td><td>813.86 <b>(-56.58%)</b></td><td>704.20 <b>(-34.47%)</b></td><td>544.10 (+14.16%)</td><td>305.77 <b>(-78.34%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.80 (n/a)</td><td>3.85 (n/a)</td><td>3.90 (n/a)</td><td>1.17 (n/a)</td><td>3.09 (n/a)</td><td>3587.30 (n/a)</td><td>1874.54 (n/a)</td><td>1074.70 (n/a)</td><td>476.60 (n/a)</td><td>1411.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>6.48 (+3.49%)</td><td>4.44 (+17.46%)</td><td>3.98 (+13.94%)</td><td>1.75 (+4.38%)</td><td>1.90 (-12.90%)</td><td>2403.20 (-4.19%)</td><td>1172.78 <b>(-22.79%)</b></td><td>1054.30 (-12.24%)</td><td>647.30 (-3.37%)</td><td>715.00 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.26 (n/a)</td><td>3.78 (n/a)</td><td>3.49 (n/a)</td><td>1.67 (n/a)</td><td>2.18 (n/a)</td><td>2508.30 (n/a)</td><td>1518.92 (n/a)</td><td>1201.30 (n/a)</td><td>669.90 (n/a)</td><td>917.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>10.29 <b>(+30.21%)</b></td><td>6.93 <b>(+56.98%)</b></td><td>6.96 <b>(+50.83%)</b></td><td>3.70 <b>(+195.40%)</b></td><td>2.34 (-19.97%)</td><td>1132.30 <b>(-66.15%)</b></td><td>673.86 <b>(-57.08%)</b></td><td>602.30 <b>(-33.70%)</b></td><td>407.80 <b>(-23.20%)</b></td><td>271.33 <b>(-78.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.90 (n/a)</td><td>4.41 (n/a)</td><td>4.62 (n/a)</td><td>1.25 (n/a)</td><td>2.92 (n/a)</td><td>3344.90 (n/a)</td><td>1570.16 (n/a)</td><td>908.40 (n/a)</td><td>531.00 (n/a)</td><td>1252.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>8.76 (-0.63%)</td><td>3.89 (-18.65%)</td><td>3.78 <b>(-25.17%)</b></td><td>1.17 (-2.44%)</td><td>3.00 (+7.57%)</td><td>3597.40 (+2.50%)</td><td>1743.28 <b>(+28.29%)</b></td><td>1109.20 <b>(+33.62%)</b></td><td>479.10 (+0.63%)</td><td>1278.40 (+3.99%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.81 (n/a)</td><td>4.79 (n/a)</td><td>5.05 (n/a)</td><td>1.20 (n/a)</td><td>2.79 (n/a)</td><td>3509.70 (n/a)</td><td>1358.84 (n/a)</td><td>830.10 (n/a)</td><td>476.10 (n/a)</td><td>1229.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>8.36 (-0.86%)</td><td>5.36 (+1.13%)</td><td>4.76 (+5.56%)</td><td>1.70 (-0.76%)</td><td>2.81 (+0.26%)</td><td>2470.80 (+0.76%)</td><td>1085.96 (-0.56%)</td><td>880.30 (-5.27%)</td><td>501.40 (+0.87%)</td><td>809.11 (+1.47%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.44 (n/a)</td><td>5.30 (n/a)</td><td>4.51 (n/a)</td><td>1.71 (n/a)</td><td>2.81 (n/a)</td><td>2452.10 (n/a)</td><td>1092.10 (n/a)</td><td>929.30 (n/a)</td><td>497.10 (n/a)</td><td>797.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.58 (-4.71%)</td><td>1.20 (-1.30%)</td><td>1.06 (-5.06%)</td><td>0.88 (+17.42%)</td><td>0.33 (-16.65%)</td><td>596.30 (-14.84%)</td><td>464.60 (-1.85%)</td><td>492.90 (+5.34%)</td><td>331.20 (+4.94%)</td><td>122.44 <b>(-24.07%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.66 (n/a)</td><td>1.21 (n/a)</td><td>1.12 (n/a)</td><td>0.75 (n/a)</td><td>0.40 (n/a)</td><td>700.20 (n/a)</td><td>473.38 (n/a)</td><td>467.90 (n/a)</td><td>315.60 (n/a)</td><td>161.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.05 <b>(+102.98%)</b></td><td>1.26 (+19.93%)</td><td>0.97 <b>(-23.38%)</b></td><td>0.30 <b>(-33.70%)</b></td><td>1.09 <b>(+115.54%)</b></td><td>3486.10 <b>(+50.82%)</b></td><td>1508.68 (+17.22%)</td><td>1077.40 <b>(+30.51%)</b></td><td>344.20 <b>(-50.73%)</b></td><td>1243.16 <b>(+64.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.50 (n/a)</td><td>1.05 (n/a)</td><td>1.27 (n/a)</td><td>0.45 (n/a)</td><td>0.50 (n/a)</td><td>2311.40 (n/a)</td><td>1287.02 (n/a)</td><td>825.50 (n/a)</td><td>698.60 (n/a)</td><td>755.15 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>3.71 <b>(+33.51%)</b></td><td>2.30 <b>(+43.40%)</b></td><td>2.36 <b>(+34.10%)</b></td><td>0.59 (+2.46%)</td><td>1.12 <b>(+27.48%)</b></td><td>3529.80 (-2.40%)</td><td>1346.60 <b>(-24.55%)</b></td><td>888.10 <b>(-25.43%)</b></td><td>564.70 <b>(-25.11%)</b></td><td>1229.06 (+4.16%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.78 (n/a)</td><td>1.60 (n/a)</td><td>1.76 (n/a)</td><td>0.58 (n/a)</td><td>0.88 (n/a)</td><td>3616.70 (n/a)</td><td>1784.80 (n/a)</td><td>1191.00 (n/a)</td><td>754.00 (n/a)</td><td>1179.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>1.83 <b>(-35.81%)</b></td><td>1.21 (-14.73%)</td><td>0.92 (-2.07%)</td><td>0.90 (+3.29%)</td><td>0.44 <b>(-48.65%)</b></td><td>585.30 (-3.18%)</td><td>473.88 (+4.19%)</td><td>572.60 (+2.12%)</td><td>286.90 <b>(+55.84%)</b></td><td>146.46 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.85 (n/a)</td><td>1.42 (n/a)</td><td>0.93 (n/a)</td><td>0.87 (n/a)</td><td>0.85 (n/a)</td><td>604.50 (n/a)</td><td>454.84 (n/a)</td><td>560.70 (n/a)</td><td>184.10 (n/a)</td><td>188.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-7.97%)</td><td>0.11 <b>(+36.73%)</b></td><td>0.12 <b>(+60.79%)</b></td><td>0.07 <b>(+44.50%)</b></td><td>0.02 <b>(-32.48%)</b></td><td>465.80 <b>(-30.81%)</b></td><td>313.24 <b>(-31.74%)</b></td><td>273.90 <b>(-37.82%)</b></td><td>257.70 (+8.64%)</td><td>86.89 <b>(-44.73%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>673.20 (n/a)</td><td>458.88 (n/a)</td><td>440.50 (n/a)</td><td>237.20 (n/a)</td><td>157.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.13 (-7.63%)</td><td>0.08 (-9.76%)</td><td>0.11 (+17.61%)</td><td>0.01 <b>(-79.39%)</b></td><td>0.05 <b>(+50.11%)</b></td><td>2429.80 <b>(+385.18%)</b></td><td>757.76 <b>(+100.64%)</b></td><td>311.70 (-14.98%)</td><td>254.50 (+8.30%)</td><td>939.29 <b>(+727.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>500.80 (n/a)</td><td>377.68 (n/a)</td><td>366.60 (n/a)</td><td>235.00 (n/a)</td><td>113.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.33 <b>(+38.36%)</b></td><td>0.22 <b>(+33.83%)</b></td><td>0.23 <b>(+62.36%)</b></td><td>0.14 <b>(+32.22%)</b></td><td>0.08 <b>(+46.02%)</b></td><td>482.90 <b>(-24.37%)</b></td><td>332.74 <b>(-23.44%)</b></td><td>279.00 <b>(-38.40%)</b></td><td>201.00 <b>(-27.75%)</b></td><td>126.87 (-12.69%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>638.50 (n/a)</td><td>434.62 (n/a)</td><td>452.90 (n/a)</td><td>278.20 (n/a)</td><td>145.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.25 <b>(+76.56%)</b></td><td>0.17 <b>(+48.57%)</b></td><td>0.17 <b>(+27.34%)</b></td><td>0.12 <b>(+87.22%)</b></td><td>0.05 <b>(+50.43%)</b></td><td>568.70 <b>(-46.59%)</b></td><td>404.26 <b>(-34.78%)</b></td><td>380.20 <b>(-21.46%)</b></td><td>263.60 <b>(-43.37%)</b></td><td>114.81 <b>(-54.98%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>1064.70 (n/a)</td><td>619.88 (n/a)</td><td>484.10 (n/a)</td><td>465.50 (n/a)</td><td>255.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.28 <b>(+21.86%)</b></td><td>0.22 <b>(+30.08%)</b></td><td>0.25 <b>(+64.44%)</b></td><td>0.11 (-12.50%)</td><td>0.07 <b>(+49.53%)</b></td><td>623.50 (+14.30%)</td><td>335.80 (-17.61%)</td><td>263.70 <b>(-39.18%)</b></td><td>235.40 (-17.92%)</td><td>163.56 <b>(+50.52%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>545.50 (n/a)</td><td>407.58 (n/a)</td><td>433.60 (n/a)</td><td>286.80 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.67 <b>(+32.21%)</b></td><td>0.38 <b>(+23.38%)</b></td><td>0.31 (+19.75%)</td><td>0.21 (+4.45%)</td><td>0.20 <b>(+67.16%)</b></td><td>622.10 (-4.26%)</td><td>420.34 (-9.79%)</td><td>421.40 (-16.49%)</td><td>194.20 <b>(-24.35%)</b></td><td>192.68 <b>(+33.02%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>649.80 (n/a)</td><td>465.94 (n/a)</td><td>504.60 (n/a)</td><td>256.70 (n/a)</td><td>144.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.48 <b>(+35.58%)</b></td><td>0.39 <b>(+44.11%)</b></td><td>0.42 <b>(+50.87%)</b></td><td>0.27 <b>(+76.24%)</b></td><td>0.10 <b>(+20.64%)</b></td><td>481.40 <b>(-43.26%)</b></td><td>361.86 <b>(-32.91%)</b></td><td>309.70 <b>(-33.73%)</b></td><td>274.40 <b>(-26.24%)</b></td><td>104.64 <b>(-47.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>848.50 (n/a)</td><td>539.36 (n/a)</td><td>467.30 (n/a)</td><td>372.00 (n/a)</td><td>200.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.54 (+10.63%)</td><td>0.41 <b>(+37.13%)</b></td><td>0.48 <b>(+71.05%)</b></td><td>0.24 <b>(+21.94%)</b></td><td>0.13 (+15.99%)</td><td>537.00 (-17.99%)</td><td>354.78 <b>(-26.83%)</b></td><td>271.20 <b>(-41.54%)</b></td><td>243.90 (-9.60%)</td><td>131.49 (-13.16%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>654.80 (n/a)</td><td>484.86 (n/a)</td><td>463.90 (n/a)</td><td>269.80 (n/a)</td><td>151.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-08 23:47:29</td><td>0.07 <b>(+23.24%)</b></td><td>0.04 (+3.44%)</td><td>0.03 (-3.64%)</td><td>0.02 (-17.37%)</td><td>0.02 <b>(+38.45%)</b></td><td>697.70 <b>(+21.02%)</b></td><td>440.22 (+2.99%)</td><td>475.00 (+3.78%)</td><td>226.20 (-18.87%)</td><td>180.92 <b>(+36.23%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>576.50 (n/a)</td><td>427.42 (n/a)</td><td>457.70 (n/a)</td><td>278.80 (n/a)</td><td>132.80 (n/a)</td>
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
