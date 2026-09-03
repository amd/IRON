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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+1.49%)</td><td>0.02 (-6.43%)</td><td>0.02 (+0.34%)</td><td>0.01 <b>(-25.49%)</b></td><td>0.01 <b>(+55.31%)</b></td><td>580.00 <b>(+34.23%)</b></td><td>378.90 (+14.95%)</td><td>297.10 (-0.34%)</td><td>257.50 (-1.49%)</td><td>146.52 <b>(+102.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.10 (n/a)</td><td>329.62 (n/a)</td><td>298.10 (n/a)</td><td>261.40 (n/a)</td><td>72.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+3.55%)</td><td>0.02 (+16.30%)</td><td>0.02 (+15.17%)</td><td>0.01 (+0.70%)</td><td>0.01 <b>(+26.04%)</b></td><td>512.00 (-0.70%)</td><td>375.04 (-10.75%)</td><td>396.10 (-13.17%)</td><td>235.80 (-3.44%)</td><td>130.69 <b>(+22.38%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.60 (n/a)</td><td>420.20 (n/a)</td><td>456.20 (n/a)</td><td>244.20 (n/a)</td><td>106.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-0.56%)</td><td>0.02 (-16.18%)</td><td>0.01 <b>(-39.70%)</b></td><td>0.01 <b>(-20.02%)</b></td><td>0.01 (+12.54%)</td><td>635.60 <b>(+25.02%)</b></td><td>431.98 <b>(+23.68%)</b></td><td>460.20 <b>(+65.84%)</b></td><td>267.90 (+0.56%)</td><td>152.64 <b>(+39.15%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.40 (n/a)</td><td>349.26 (n/a)</td><td>277.50 (n/a)</td><td>266.40 (n/a)</td><td>109.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+2.06%)</td><td>0.01 (-4.84%)</td><td>0.01 (-14.78%)</td><td>0.01 <b>(+115.48%)</b></td><td>0.00 <b>(-31.53%)</b></td><td>507.40 <b>(-53.59%)</b></td><td>446.50 (-12.77%)</td><td>485.50 (+17.33%)</td><td>266.90 (-2.02%)</td><td>100.90 <b>(-70.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1093.30 (n/a)</td><td>511.88 (n/a)</td><td>413.80 (n/a)</td><td>272.40 (n/a)</td><td>337.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-17.30%)</td><td>0.02 (+4.17%)</td><td>0.02 <b>(+61.84%)</b></td><td>0.01 (-5.36%)</td><td>0.01 <b>(-26.82%)</b></td><td>607.00 (+5.68%)</td><td>383.74 (-8.65%)</td><td>313.30 <b>(-38.21%)</b></td><td>253.80 <b>(+20.91%)</b></td><td>149.78 (-8.43%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.40 (n/a)</td><td>420.06 (n/a)</td><td>507.00 (n/a)</td><td>209.90 (n/a)</td><td>163.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (+4.29%)</td><td>0.02 (-9.33%)</td><td>0.01 (-7.56%)</td><td>0.01 (-19.91%)</td><td>0.01 (+11.48%)</td><td>754.20 <b>(+24.87%)</b></td><td>497.76 (+16.56%)</td><td>535.30 (+8.19%)</td><td>162.60 (-4.13%)</td><td>214.01 (+17.86%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>427.04 (n/a)</td><td>494.80 (n/a)</td><td>169.60 (n/a)</td><td>181.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(-21.46%)</b></td><td>0.05 (-3.66%)</td><td>0.05 (+6.55%)</td><td>0.03 <b>(+23.68%)</b></td><td>0.01 <b>(-45.38%)</b></td><td>407.10 (-19.15%)</td><td>283.98 (-4.82%)</td><td>270.80 (-6.14%)</td><td>229.30 <b>(+27.32%)</b></td><td>72.99 <b>(-43.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>503.50 (n/a)</td><td>298.36 (n/a)</td><td>288.50 (n/a)</td><td>180.10 (n/a)</td><td>128.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(-26.52%)</b></td><td>0.04 (+9.90%)</td><td>0.04 <b>(+53.09%)</b></td><td>0.02 (+2.16%)</td><td>0.01 <b>(-33.23%)</b></td><td>621.80 (-2.12%)</td><td>370.40 (-13.70%)</td><td>287.30 <b>(-34.69%)</b></td><td>252.50 <b>(+36.05%)</b></td><td>156.26 (-3.85%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>635.30 (n/a)</td><td>429.22 (n/a)</td><td>439.90 (n/a)</td><td>185.60 (n/a)</td><td>162.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(+20.42%)</b></td><td>0.04 <b>(+56.32%)</b></td><td>0.05 <b>(+91.65%)</b></td><td>0.02 <b>(+266.50%)</b></td><td>0.01 (+5.44%)</td><td>568.10 <b>(-72.72%)</b></td><td>362.50 <b>(-53.07%)</b></td><td>267.30 <b>(-47.82%)</b></td><td>236.30 (-16.94%)</td><td>152.71 <b>(-79.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2082.10 (n/a)</td><td>772.46 (n/a)</td><td>512.30 (n/a)</td><td>284.50 (n/a)</td><td>738.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (-2.05%)</td><td>0.04 (+10.36%)</td><td>0.05 <b>(+30.82%)</b></td><td>0.03 (+14.34%)</td><td>0.01 (+1.35%)</td><td>478.10 (-12.55%)</td><td>329.94 (-9.86%)</td><td>261.60 <b>(-23.58%)</b></td><td>230.10 (+2.09%)</td><td>118.59 (-8.95%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.70 (n/a)</td><td>366.02 (n/a)</td><td>342.30 (n/a)</td><td>225.40 (n/a)</td><td>130.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (-15.75%)</td><td>0.04 (-2.54%)</td><td>0.04 (-0.18%)</td><td>0.02 (+12.56%)</td><td>0.01 <b>(-28.12%)</b></td><td>547.40 (-11.17%)</td><td>369.72 (-5.97%)</td><td>324.10 (+0.15%)</td><td>203.90 (+18.68%)</td><td>136.40 <b>(-25.66%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>616.20 (n/a)</td><td>393.20 (n/a)</td><td>323.60 (n/a)</td><td>171.80 (n/a)</td><td>183.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(-30.90%)</b></td><td>0.04 (-0.68%)</td><td>0.03 <b>(+23.67%)</b></td><td>0.03 <b>(+33.32%)</b></td><td>0.01 <b>(-47.46%)</b></td><td>472.20 <b>(-24.99%)</b></td><td>374.14 (-15.28%)</td><td>435.10 (-19.14%)</td><td>242.40 <b>(+44.72%)</b></td><td>113.03 <b>(-44.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>629.50 (n/a)</td><td>441.62 (n/a)</td><td>538.10 (n/a)</td><td>167.50 (n/a)</td><td>204.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+4.67%)</td><td>0.08 (+14.40%)</td><td>0.09 <b>(+52.36%)</b></td><td>0.04 <b>(-25.41%)</b></td><td>0.02 (+14.64%)</td><td>594.00 <b>(+34.06%)</b></td><td>329.72 (-8.44%)</td><td>266.90 <b>(-34.37%)</b></td><td>238.40 (-4.45%)</td><td>149.57 <b>(+53.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>443.10 (n/a)</td><td>360.12 (n/a)</td><td>406.70 (n/a)</td><td>249.50 (n/a)</td><td>97.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 <b>(-31.15%)</b></td><td>0.07 (+7.62%)</td><td>0.07 <b>(+37.84%)</b></td><td>0.04 (+19.75%)</td><td>0.02 <b>(-52.46%)</b></td><td>559.70 (-16.49%)</td><td>382.84 (-17.65%)</td><td>353.90 <b>(-27.45%)</b></td><td>275.60 <b>(+45.28%)</b></td><td>112.63 <b>(-34.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>670.20 (n/a)</td><td>464.88 (n/a)</td><td>487.80 (n/a)</td><td>189.70 (n/a)</td><td>172.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 <b>(+40.15%)</b></td><td>0.08 (+19.63%)</td><td>0.08 (+17.93%)</td><td>0.04 (-1.09%)</td><td>0.04 <b>(+75.82%)</b></td><td>569.10 (+1.10%)</td><td>367.42 (-8.97%)</td><td>319.60 (-15.20%)</td><td>188.50 <b>(-28.65%)</b></td><td>159.54 <b>(+29.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>562.90 (n/a)</td><td>403.62 (n/a)</td><td>376.90 (n/a)</td><td>264.20 (n/a)</td><td>123.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+1.25%)</td><td>0.08 (+2.07%)</td><td>0.08 (-8.71%)</td><td>0.05 (+11.22%)</td><td>0.02 <b>(-26.05%)</b></td><td>473.70 (-10.10%)</td><td>331.48 (-7.76%)</td><td>295.90 (+9.51%)</td><td>241.20 (-1.27%)</td><td>93.93 <b>(-34.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>526.90 (n/a)</td><td>359.38 (n/a)</td><td>270.20 (n/a)</td><td>244.30 (n/a)</td><td>143.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (-17.24%)</td><td>0.05 <b>(-23.83%)</b></td><td>0.04 <b>(-34.60%)</b></td><td>0.01 <b>(-66.86%)</b></td><td>0.03 <b>(+36.44%)</b></td><td>1947.90 <b>(+201.72%)</b></td><td>835.16 <b>(+92.72%)</b></td><td>580.70 <b>(+52.90%)</b></td><td>302.60 <b>(+20.85%)</b></td><td>690.94 <b>(+344.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>645.60 (n/a)</td><td>433.36 (n/a)</td><td>379.80 (n/a)</td><td>250.40 (n/a)</td><td>155.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (-9.56%)</td><td>0.07 (-15.50%)</td><td>0.06 <b>(-22.41%)</b></td><td>0.04 (-18.19%)</td><td>0.02 (+10.77%)</td><td>576.30 <b>(+22.23%)</b></td><td>403.38 <b>(+21.57%)</b></td><td>388.10 <b>(+28.89%)</b></td><td>278.50 (+10.56%)</td><td>124.43 <b>(+43.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>471.50 (n/a)</td><td>331.80 (n/a)</td><td>301.10 (n/a)</td><td>251.90 (n/a)</td><td>86.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.22 (-8.73%)</td><td>0.15 <b>(+22.54%)</b></td><td>0.12 (+5.61%)</td><td>0.09 <b>(+258.34%)</b></td><td>0.06 <b>(-25.10%)</b></td><td>530.20 <b>(-72.09%)</b></td><td>377.42 <b>(-45.41%)</b></td><td>425.80 (-5.31%)</td><td>219.60 (+9.58%)</td><td>136.74 <b>(-80.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1899.90 (n/a)</td><td>691.32 (n/a)</td><td>449.70 (n/a)</td><td>200.40 (n/a)</td><td>685.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (-19.78%)</td><td>0.12 (-7.20%)</td><td>0.10 (-0.69%)</td><td>0.08 (-12.87%)</td><td>0.05 <b>(-25.89%)</b></td><td>642.00 (+14.77%)</td><td>475.38 (+5.41%)</td><td>499.40 (+0.69%)</td><td>263.10 <b>(+24.63%)</b></td><td>157.35 (+12.47%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>559.40 (n/a)</td><td>450.98 (n/a)</td><td>496.00 (n/a)</td><td>211.10 (n/a)</td><td>139.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (+5.99%)</td><td>0.16 <b>(+29.73%)</b></td><td>0.17 <b>(+81.11%)</b></td><td>0.12 <b>(+56.51%)</b></td><td>0.03 <b>(-35.81%)</b></td><td>410.20 <b>(-36.11%)</b></td><td>315.70 <b>(-29.13%)</b></td><td>282.50 <b>(-44.79%)</b></td><td>261.20 (-5.64%)</td><td>66.22 <b>(-58.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>642.00 (n/a)</td><td>445.44 (n/a)</td><td>511.70 (n/a)</td><td>276.80 (n/a)</td><td>160.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.20 (-16.95%)</td><td>0.14 (+18.42%)</td><td>0.11 (+4.28%)</td><td>0.09 <b>(+63.29%)</b></td><td>0.05 <b>(-25.66%)</b></td><td>535.20 <b>(-38.76%)</b></td><td>393.02 <b>(-25.23%)</b></td><td>444.60 (-4.10%)</td><td>244.30 <b>(+20.40%)</b></td><td>136.84 <b>(-45.16%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>873.90 (n/a)</td><td>525.66 (n/a)</td><td>463.60 (n/a)</td><td>202.90 (n/a)</td><td>249.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.23 (-8.57%)</td><td>0.16 (+2.10%)</td><td>0.20 <b>(+42.44%)</b></td><td>0.08 (-11.78%)</td><td>0.07 (+4.51%)</td><td>623.20 (+13.35%)</td><td>373.14 (+3.62%)</td><td>245.00 <b>(-29.80%)</b></td><td>210.30 (+9.36%)</td><td>194.57 <b>(+32.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>549.80 (n/a)</td><td>360.12 (n/a)</td><td>349.00 (n/a)</td><td>192.30 (n/a)</td><td>146.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (+7.10%)</td><td>0.15 <b>(+38.42%)</b></td><td>0.17 <b>(+86.35%)</b></td><td>0.10 <b>(+20.03%)</b></td><td>0.04 (-10.99%)</td><td>477.40 (-16.70%)</td><td>340.92 <b>(-29.84%)</b></td><td>294.80 <b>(-46.33%)</b></td><td>252.10 (-6.63%)</td><td>91.16 <b>(-28.83%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>573.10 (n/a)</td><td>485.90 (n/a)</td><td>549.30 (n/a)</td><td>270.00 (n/a)</td><td>128.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (+4.45%)</td><td>0.01 (-10.99%)</td><td>0.01 (-5.05%)</td><td>0.00 <b>(-35.48%)</b></td><td>0.00 <b>(+58.20%)</b></td><td>553.40 <b>(+54.97%)</b></td><td>349.54 <b>(+22.39%)</b></td><td>287.00 (+5.28%)</td><td>215.10 (-4.27%)</td><td>140.74 <b>(+137.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>357.10 (n/a)</td><td>285.60 (n/a)</td><td>272.60 (n/a)</td><td>224.70 (n/a)</td><td>59.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (-9.83%)</td><td>0.01 <b>(-25.61%)</b></td><td>0.01 <b>(-31.64%)</b></td><td>0.00 (-19.17%)</td><td>0.00 (-2.00%)</td><td>574.40 <b>(+23.71%)</b></td><td>424.46 <b>(+35.69%)</b></td><td>414.50 <b>(+46.31%)</b></td><td>269.10 (+10.92%)</td><td>109.12 <b>(+23.98%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.30 (n/a)</td><td>312.82 (n/a)</td><td>283.30 (n/a)</td><td>242.60 (n/a)</td><td>88.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (-15.63%)</td><td>0.01 <b>(-23.37%)</b></td><td>0.01 <b>(-35.54%)</b></td><td>0.00 (-13.27%)</td><td>0.00 <b>(-24.38%)</b></td><td>555.10 (+15.29%)</td><td>423.62 <b>(+27.84%)</b></td><td>437.40 <b>(+55.11%)</b></td><td>269.80 (+18.49%)</td><td>102.18 (-3.39%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.50 (n/a)</td><td>331.38 (n/a)</td><td>282.00 (n/a)</td><td>227.70 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-23.61%)</b></td><td>0.01 (-17.62%)</td><td>0.01 <b>(-25.15%)</b></td><td>0.00 (-11.46%)</td><td>0.00 <b>(-22.65%)</b></td><td>545.70 (+12.93%)</td><td>396.58 <b>(+20.03%)</b></td><td>366.00 <b>(+33.58%)</b></td><td>273.40 <b>(+30.88%)</b></td><td>126.03 (+11.28%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.20 (n/a)</td><td>330.40 (n/a)</td><td>274.00 (n/a)</td><td>208.90 (n/a)</td><td>113.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-21.57%)</b></td><td>0.00 <b>(-49.70%)</b></td><td>0.00 <b>(-54.75%)</b></td><td>0.00 <b>(-74.70%)</b></td><td>0.00 (+0.03%)</td><td>1957.10 <b>(+295.21%)</b></td><td>881.66 <b>(+165.67%)</b></td><td>566.10 <b>(+120.96%)</b></td><td>298.80 <b>(+27.53%)</b></td><td>655.39 <b>(+432.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.20 (n/a)</td><td>331.86 (n/a)</td><td>256.20 (n/a)</td><td>234.30 (n/a)</td><td>123.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(+22.21%)</b></td><td>0.01 (-2.84%)</td><td>0.01 (-12.01%)</td><td>0.00 (+2.83%)</td><td>0.00 <b>(+44.83%)</b></td><td>556.00 (-2.75%)</td><td>469.24 (+4.92%)</td><td>503.70 (+13.65%)</td><td>296.70 (-18.17%)</td><td>100.75 (+13.37%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>571.70 (n/a)</td><td>447.24 (n/a)</td><td>443.20 (n/a)</td><td>362.60 (n/a)</td><td>88.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+18.08%)</td><td>0.01 (-12.09%)</td><td>0.01 <b>(-33.27%)</b></td><td>0.01 (+12.98%)</td><td>0.01 <b>(+20.72%)</b></td><td>571.30 (-11.48%)</td><td>429.46 (+13.76%)</td><td>442.30 <b>(+49.83%)</b></td><td>225.00 (-15.32%)</td><td>131.32 (-16.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.40 (n/a)</td><td>377.50 (n/a)</td><td>295.20 (n/a)</td><td>265.70 (n/a)</td><td>156.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-15.04%)</td><td>0.01 <b>(-36.68%)</b></td><td>0.01 <b>(-41.31%)</b></td><td>0.00 <b>(-68.94%)</b></td><td>0.01 (+3.90%)</td><td>1930.90 <b>(+221.98%)</b></td><td>753.22 <b>(+117.64%)</b></td><td>499.10 <b>(+70.40%)</b></td><td>229.00 (+17.74%)</td><td>677.43 <b>(+318.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>346.08 (n/a)</td><td>292.90 (n/a)</td><td>194.50 (n/a)</td><td>161.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+11.45%)</td><td>0.02 (+17.47%)</td><td>0.02 <b>(+36.61%)</b></td><td>0.01 (-6.27%)</td><td>0.01 <b>(+42.45%)</b></td><td>615.50 (+6.69%)</td><td>376.08 (-9.10%)</td><td>302.70 <b>(-26.81%)</b></td><td>231.30 (-10.28%)</td><td>161.55 <b>(+41.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.90 (n/a)</td><td>413.72 (n/a)</td><td>413.60 (n/a)</td><td>257.80 (n/a)</td><td>114.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(+82.71%)</b></td><td>0.01 <b>(+60.12%)</b></td><td>0.01 (+3.09%)</td><td>0.01 <b>(+380.36%)</b></td><td>0.01 <b>(+35.19%)</b></td><td>517.80 <b>(-79.18%)</b></td><td>398.44 <b>(-55.19%)</b></td><td>468.70 (-2.98%)</td><td>233.60 <b>(-45.28%)</b></td><td>132.96 <b>(-85.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2487.40 (n/a)</td><td>889.16 (n/a)</td><td>483.10 (n/a)</td><td>426.90 (n/a)</td><td>896.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-1.25%)</td><td>0.01 (-14.18%)</td><td>0.01 (-16.90%)</td><td>0.01 (-5.40%)</td><td>0.01 (+5.48%)</td><td>632.60 (+5.72%)</td><td>469.96 (+18.84%)</td><td>493.90 <b>(+20.35%)</b></td><td>241.90 (+1.30%)</td><td>158.51 (+13.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.40 (n/a)</td><td>395.44 (n/a)</td><td>410.40 (n/a)</td><td>238.80 (n/a)</td><td>139.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+14.03%)</td><td>0.01 (-15.31%)</td><td>0.01 <b>(-32.48%)</b></td><td>0.01 (-19.28%)</td><td>0.00 <b>(+52.96%)</b></td><td>628.30 <b>(+23.90%)</b></td><td>507.38 <b>(+22.58%)</b></td><td>541.30 <b>(+48.10%)</b></td><td>305.90 (-12.30%)</td><td>125.85 <b>(+59.55%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.10 (n/a)</td><td>413.92 (n/a)</td><td>365.50 (n/a)</td><td>348.80 (n/a)</td><td>78.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(-32.00%)</b></td><td>0.03 <b>(-30.40%)</b></td><td>0.02 <b>(-39.19%)</b></td><td>0.02 <b>(-38.35%)</b></td><td>0.01 (-10.93%)</td><td>545.60 <b>(+62.19%)</b></td><td>436.66 <b>(+48.52%)</b></td><td>505.60 <b>(+64.42%)</b></td><td>293.60 <b>(+47.09%)</b></td><td>119.74 <b>(+119.28%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>336.40 (n/a)</td><td>294.00 (n/a)</td><td>307.50 (n/a)</td><td>199.60 (n/a)</td><td>54.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (-6.22%)</td><td>0.03 (-3.86%)</td><td>0.02 (-13.35%)</td><td>0.02 (-10.51%)</td><td>0.01 (+14.97%)</td><td>601.70 (+11.76%)</td><td>461.98 (+8.53%)</td><td>548.00 (+15.39%)</td><td>275.00 (+6.63%)</td><td>163.08 <b>(+35.57%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.40 (n/a)</td><td>425.68 (n/a)</td><td>474.90 (n/a)</td><td>257.90 (n/a)</td><td>120.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+21.76%)</b></td><td>0.03 <b>(+41.22%)</b></td><td>0.04 <b>(+75.24%)</b></td><td>0.02 (+13.84%)</td><td>0.01 <b>(+39.32%)</b></td><td>527.20 (-12.16%)</td><td>343.54 <b>(-27.40%)</b></td><td>280.00 <b>(-42.95%)</b></td><td>241.90 (-17.86%)</td><td>123.05 (-0.26%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>473.22 (n/a)</td><td>490.80 (n/a)</td><td>294.50 (n/a)</td><td>123.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(+25.12%)</b></td><td>0.02 (-15.36%)</td><td>0.02 <b>(-37.80%)</b></td><td>0.01 (-16.17%)</td><td>0.01 <b>(+55.78%)</b></td><td>718.00 (+19.29%)</td><td>500.26 <b>(+28.08%)</b></td><td>513.20 <b>(+60.78%)</b></td><td>214.50 <b>(-20.08%)</b></td><td>183.27 <b>(+33.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.90 (n/a)</td><td>390.58 (n/a)</td><td>319.20 (n/a)</td><td>268.40 (n/a)</td><td>137.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (-12.74%)</td><td>0.03 (-9.97%)</td><td>0.02 (-9.21%)</td><td>0.02 <b>(-24.57%)</b></td><td>0.01 (+5.24%)</td><td>611.60 <b>(+32.58%)</b></td><td>428.52 (+17.40%)</td><td>461.80 (+10.16%)</td><td>237.20 (+14.59%)</td><td>166.18 <b>(+60.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.30 (n/a)</td><td>365.00 (n/a)</td><td>419.20 (n/a)</td><td>207.00 (n/a)</td><td>103.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+40.88%)</b></td><td>0.02 (-1.38%)</td><td>0.02 (-15.60%)</td><td>0.02 (-6.18%)</td><td>0.01 <b>(+186.16%)</b></td><td>596.60 (+6.59%)</td><td>509.02 (+7.84%)</td><td>562.70 (+18.49%)</td><td>287.90 <b>(-29.00%)</b></td><td>126.82 <b>(+109.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>559.70 (n/a)</td><td>472.02 (n/a)</td><td>474.90 (n/a)</td><td>405.50 (n/a)</td><td>60.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (-5.72%)</td><td>0.06 (-6.88%)</td><td>0.07 (-0.55%)</td><td>0.03 (-10.02%)</td><td>0.02 (+9.70%)</td><td>651.50 (+11.14%)</td><td>391.76 (+10.16%)</td><td>298.90 (+0.54%)</td><td>272.30 (+6.08%)</td><td>160.15 <b>(+20.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>586.20 (n/a)</td><td>355.64 (n/a)</td><td>297.30 (n/a)</td><td>256.70 (n/a)</td><td>132.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 <b>(+33.20%)</b></td><td>0.06 <b>(+25.72%)</b></td><td>0.06 <b>(+41.46%)</b></td><td>0.03 (-0.16%)</td><td>0.03 <b>(+66.12%)</b></td><td>657.30 (+0.15%)</td><td>403.36 (-12.14%)</td><td>332.80 <b>(-29.30%)</b></td><td>197.10 <b>(-24.91%)</b></td><td>191.40 <b>(+35.43%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>656.30 (n/a)</td><td>459.10 (n/a)</td><td>470.70 (n/a)</td><td>262.50 (n/a)</td><td>141.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (-1.71%)</td><td>0.06 (-4.43%)</td><td>0.07 (-0.64%)</td><td>0.04 (+0.48%)</td><td>0.02 (-2.37%)</td><td>488.40 (-0.47%)</td><td>356.72 (+4.62%)</td><td>305.30 (+0.66%)</td><td>228.40 (+1.74%)</td><td>112.92 (+2.22%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>490.70 (n/a)</td><td>340.98 (n/a)</td><td>303.30 (n/a)</td><td>224.50 (n/a)</td><td>110.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+7.39%)</td><td>0.07 <b>(+24.91%)</b></td><td>0.07 <b>(+53.13%)</b></td><td>0.04 (+4.98%)</td><td>0.02 (+12.83%)</td><td>540.30 (-4.76%)</td><td>359.50 (-18.10%)</td><td>300.60 <b>(-34.69%)</b></td><td>218.30 (-6.87%)</td><td>138.22 (+12.08%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.30 (n/a)</td><td>438.94 (n/a)</td><td>460.30 (n/a)</td><td>234.40 (n/a)</td><td>123.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+12.52%)</td><td>0.06 (+11.56%)</td><td>0.07 <b>(+39.05%)</b></td><td>0.04 (+10.25%)</td><td>0.02 (+9.30%)</td><td>512.40 (-9.29%)</td><td>363.64 (-9.74%)</td><td>314.70 <b>(-28.09%)</b></td><td>217.50 (-11.15%)</td><td>138.71 (-1.69%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.90 (n/a)</td><td>402.90 (n/a)</td><td>437.60 (n/a)</td><td>244.80 (n/a)</td><td>141.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(-29.85%)</b></td><td>0.04 (-18.62%)</td><td>0.04 (-19.29%)</td><td>0.03 (-12.60%)</td><td>0.01 <b>(-41.98%)</b></td><td>609.40 (+14.42%)</td><td>512.76 (+19.77%)</td><td>551.70 <b>(+23.89%)</b></td><td>371.50 <b>(+42.56%)</b></td><td>104.55 (-0.41%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>532.60 (n/a)</td><td>428.12 (n/a)</td><td>445.30 (n/a)</td><td>260.60 (n/a)</td><td>104.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>806.70 (n/a)</td><td>464.24 (n/a)</td><td>405.30 (n/a)</td><td>274.20 (n/a)</td><td>218.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.50 (n/a)</td><td>520.74 (n/a)</td><td>543.50 (n/a)</td><td>283.30 (n/a)</td><td>145.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.70 (n/a)</td><td>463.96 (n/a)</td><td>551.30 (n/a)</td><td>212.60 (n/a)</td><td>199.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>373.74 (n/a)</td><td>379.80 (n/a)</td><td>232.60 (n/a)</td><td>139.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>638.50 (n/a)</td><td>504.58 (n/a)</td><td>608.50 (n/a)</td><td>235.40 (n/a)</td><td>176.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.60 (n/a)</td><td>427.96 (n/a)</td><td>522.00 (n/a)</td><td>248.00 (n/a)</td><td>151.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>553.70 (n/a)</td><td>383.14 (n/a)</td><td>430.80 (n/a)</td><td>240.70 (n/a)</td><td>138.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>531.20 (n/a)</td><td>354.38 (n/a)</td><td>293.60 (n/a)</td><td>258.20 (n/a)</td><td>120.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>614.70 (n/a)</td><td>376.98 (n/a)</td><td>327.10 (n/a)</td><td>207.10 (n/a)</td><td>157.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 (+16.53%)</td><td>0.15 (-15.18%)</td><td>0.16 (-6.93%)</td><td>0.08 <b>(-50.42%)</b></td><td>0.05 <b>(+475.86%)</b></td><td>617.40 <b>(+101.70%)</b></td><td>379.26 <b>(+32.59%)</b></td><td>312.20 (+7.43%)</td><td>229.60 (-14.17%)</td><td>154.96 <b>(+923.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>306.10 (n/a)</td><td>286.04 (n/a)</td><td>290.60 (n/a)</td><td>267.50 (n/a)</td><td>15.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>658.50 (n/a)</td><td>501.06 (n/a)</td><td>521.20 (n/a)</td><td>310.10 (n/a)</td><td>126.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1856.00 (n/a)</td><td>763.74 (n/a)</td><td>494.70 (n/a)</td><td>459.00 (n/a)</td><td>610.99 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.60 (n/a)</td><td>324.04 (n/a)</td><td>281.10 (n/a)</td><td>257.90 (n/a)</td><td>102.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.50 (n/a)</td><td>361.90 (n/a)</td><td>360.60 (n/a)</td><td>234.60 (n/a)</td><td>115.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.90 (n/a)</td><td>456.04 (n/a)</td><td>462.10 (n/a)</td><td>294.30 (n/a)</td><td>159.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>304.20 (n/a)</td><td>252.60 (n/a)</td><td>251.20 (n/a)</td><td>194.00 (n/a)</td><td>40.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>598.70 (n/a)</td><td>393.94 (n/a)</td><td>294.00 (n/a)</td><td>235.40 (n/a)</td><td>180.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>692.50 (n/a)</td><td>406.82 (n/a)</td><td>300.80 (n/a)</td><td>249.00 (n/a)</td><td>194.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>261.70 (n/a)</td><td>236.60 (n/a)</td><td>238.70 (n/a)</td><td>201.60 (n/a)</td><td>22.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>576.20 (n/a)</td><td>353.56 (n/a)</td><td>281.30 (n/a)</td><td>209.50 (n/a)</td><td>166.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>333.74 (n/a)</td><td>291.70 (n/a)</td><td>254.00 (n/a)</td><td>101.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1924.90 (n/a)</td><td>862.82 (n/a)</td><td>472.20 (n/a)</td><td>409.90 (n/a)</td><td>651.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>631.90 (n/a)</td><td>453.06 (n/a)</td><td>472.40 (n/a)</td><td>296.10 (n/a)</td><td>146.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>400.30 (n/a)</td><td>336.86 (n/a)</td><td>343.90 (n/a)</td><td>268.50 (n/a)</td><td>57.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.80 (n/a)</td><td>365.02 (n/a)</td><td>280.50 (n/a)</td><td>241.40 (n/a)</td><td>152.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.20 (n/a)</td><td>357.86 (n/a)</td><td>411.90 (n/a)</td><td>242.80 (n/a)</td><td>92.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>380.70 (n/a)</td><td>408.70 (n/a)</td><td>221.50 (n/a)</td><td>142.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.60 (n/a)</td><td>416.02 (n/a)</td><td>317.40 (n/a)</td><td>223.60 (n/a)</td><td>195.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.90 (n/a)</td><td>409.24 (n/a)</td><td>420.50 (n/a)</td><td>236.50 (n/a)</td><td>141.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.30 (n/a)</td><td>375.12 (n/a)</td><td>386.30 (n/a)</td><td>222.30 (n/a)</td><td>126.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.20 (n/a)</td><td>358.00 (n/a)</td><td>277.40 (n/a)</td><td>217.60 (n/a)</td><td>165.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.40 (n/a)</td><td>416.48 (n/a)</td><td>487.70 (n/a)</td><td>223.20 (n/a)</td><td>170.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>352.06 (n/a)</td><td>312.20 (n/a)</td><td>242.50 (n/a)</td><td>141.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2363.80 (n/a)</td><td>808.06 (n/a)</td><td>461.10 (n/a)</td><td>243.50 (n/a)</td><td>881.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>431.22 (n/a)</td><td>484.20 (n/a)</td><td>212.20 (n/a)</td><td>141.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.30 (n/a)</td><td>336.50 (n/a)</td><td>315.90 (n/a)</td><td>244.20 (n/a)</td><td>88.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>604.50 (n/a)</td><td>427.88 (n/a)</td><td>367.90 (n/a)</td><td>276.10 (n/a)</td><td>139.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1019.90 (n/a)</td><td>518.88 (n/a)</td><td>440.60 (n/a)</td><td>248.60 (n/a)</td><td>315.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.60 (n/a)</td><td>385.92 (n/a)</td><td>306.10 (n/a)</td><td>238.40 (n/a)</td><td>163.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>663.70 (n/a)</td><td>434.80 (n/a)</td><td>479.60 (n/a)</td><td>241.60 (n/a)</td><td>178.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>440.64 (n/a)</td><td>446.70 (n/a)</td><td>333.30 (n/a)</td><td>101.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>533.90 (n/a)</td><td>396.00 (n/a)</td><td>323.00 (n/a)</td><td>274.40 (n/a)</td><td>126.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>650.90 (n/a)</td><td>418.66 (n/a)</td><td>288.10 (n/a)</td><td>247.50 (n/a)</td><td>205.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>289.90 (n/a)</td><td>271.04 (n/a)</td><td>276.10 (n/a)</td><td>247.30 (n/a)</td><td>18.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>430.60 (n/a)</td><td>305.42 (n/a)</td><td>272.00 (n/a)</td><td>238.90 (n/a)</td><td>75.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>632.00 (n/a)</td><td>425.72 (n/a)</td><td>410.80 (n/a)</td><td>261.70 (n/a)</td><td>159.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>569.20 (n/a)</td><td>383.48 (n/a)</td><td>331.30 (n/a)</td><td>323.30 (n/a)</td><td>104.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.48 (-17.71%)</td><td>0.33 (-3.21%)</td><td>0.37 (+2.67%)</td><td>0.16 (+6.82%)</td><td>0.15 (-16.78%)</td><td>1348.60 (-6.38%)</td><td>824.88 (-1.69%)</td><td>595.10 (-2.60%)</td><td>465.10 <b>(+21.53%)</b></td><td>424.37 (-9.32%)</td><td>20.29 (-17.71%)</td><td>13.98 (-3.21%)</td><td>15.86 (+2.67%)</td><td>7.00 (+6.82%)</td><td>6.25 (-16.78%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.58 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>1440.50 (n/a)</td><td>839.04 (n/a)</td><td>611.00 (n/a)</td><td>382.70 (n/a)</td><td>467.99 (n/a)</td><td>24.66 (n/a)</td><td>14.44 (n/a)</td><td>15.45 (n/a)</td><td>6.55 (n/a)</td><td>7.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.54 (+6.63%)</td><td>0.45 <b>(+37.19%)</b></td><td>0.45 <b>(+42.02%)</b></td><td>0.36 <b>(+86.83%)</b></td><td>0.08 <b>(-26.93%)</b></td><td>617.70 <b>(-46.47%)</b></td><td>509.90 <b>(-31.99%)</b></td><td>490.00 <b>(-29.59%)</b></td><td>410.40 (-6.24%)</td><td>97.98 <b>(-62.81%)</b></td><td>22.99 (+6.63%)</td><td>19.06 <b>(+37.19%)</b></td><td>19.26 <b>(+42.02%)</b></td><td>15.28 <b>(+86.83%)</b></td><td>3.60 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>1154.00 (n/a)</td><td>749.76 (n/a)</td><td>695.90 (n/a)</td><td>437.70 (n/a)</td><td>263.48 (n/a)</td><td>21.56 (n/a)</td><td>13.89 (n/a)</td><td>13.56 (n/a)</td><td>8.18 (n/a)</td><td>4.93 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.31 (-0.56%)</td><td>0.30 (-1.02%)</td><td>0.30 (-1.93%)</td><td>0.29 (-1.81%)</td><td>0.01 <b>(+34.89%)</b></td><td>85893.40 (+1.85%)</td><td>82819.76 (+1.06%)</td><td>83484.30 (+1.96%)</td><td>80397.60 (+0.56%)</td><td>2269.85 <b>(+37.49%)</b></td><td>213.69 (-0.56%)</td><td>207.56 (-1.02%)</td><td>205.79 (-1.93%)</td><td>200.01 (-1.81%)</td><td>5.67 <b>(+34.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84336.20 (n/a)</td><td>81953.16 (n/a)</td><td>81876.40 (n/a)</td><td>79949.80 (n/a)</td><td>1650.96 (n/a)</td><td>214.88 (n/a)</td><td>209.70 (n/a)</td><td>209.83 (n/a)</td><td>203.71 (n/a)</td><td>4.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.04 (+1.11%)</td><td>1.00 (+0.97%)</td><td>0.99 (-1.37%)</td><td>0.96 (+5.61%)</td><td>0.03 <b>(-33.08%)</b></td><td>26128.70 (-5.31%)</td><td>25166.54 (-1.06%)</td><td>25357.50 (+1.39%)</td><td>24206.80 (-1.10%)</td><td>765.46 <b>(-38.08%)</b></td><td>709.71 (+1.11%)</td><td>683.15 (+0.97%)</td><td>677.51 (-1.37%)</td><td>657.51 (+5.61%)</td><td>20.83 <b>(-33.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.03 (n/a)</td><td>0.99 (n/a)</td><td>1.01 (n/a)</td><td>0.91 (n/a)</td><td>0.05 (n/a)</td><td>27593.40 (n/a)</td><td>25437.36 (n/a)</td><td>25010.30 (n/a)</td><td>24474.90 (n/a)</td><td>1236.19 (n/a)</td><td>701.94 (n/a)</td><td>676.59 (n/a)</td><td>686.91 (n/a)</td><td>622.61 (n/a)</td><td>31.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.82 (-0.08%)</td><td>0.82 (+0.51%)</td><td>0.81 (+0.02%)</td><td>0.81 (+1.49%)</td><td>0.00 <b>(-52.68%)</b></td><td>93063.70 (-1.47%)</td><td>92636.60 (-0.52%)</td><td>92840.30 (-0.02%)</td><td>91951.70 (+0.08%)</td><td>474.03 <b>(-53.36%)</b></td><td>747.34 (-0.08%)</td><td>741.83 (+0.51%)</td><td>740.19 (+0.02%)</td><td>738.41 (+1.49%)</td><td>3.81 <b>(-52.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.01 (n/a)</td><td>94452.50 (n/a)</td><td>93117.04 (n/a)</td><td>92859.20 (n/a)</td><td>91876.90 (n/a)</td><td>1016.36 (n/a)</td><td>747.95 (n/a)</td><td>738.06 (n/a)</td><td>740.04 (n/a)</td><td>727.56 (n/a)</td><td>8.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.78 (+0.45%)</td><td>0.78 (+1.34%)</td><td>0.78 (+1.74%)</td><td>0.76 (+1.31%)</td><td>0.01 (-13.18%)</td><td>98955.50 (-1.30%)</td><td>97410.40 (-1.32%)</td><td>97131.80 (-1.71%)</td><td>96452.00 (-0.45%)</td><td>1086.58 (-14.75%)</td><td>712.47 (+0.45%)</td><td>705.53 (+1.34%)</td><td>707.49 (+1.74%)</td><td>694.45 (+1.31%)</td><td>7.83 (-13.18%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100254.80 (n/a)</td><td>98714.30 (n/a)</td><td>98820.00 (n/a)</td><td>96890.40 (n/a)</td><td>1274.62 (n/a)</td><td>709.25 (n/a)</td><td>696.24 (n/a)</td><td>695.40 (n/a)</td><td>685.45 (n/a)</td><td>9.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.80 (-0.20%)</td><td>0.80 (+0.28%)</td><td>0.80 (+0.49%)</td><td>0.79 (+0.38%)</td><td>0.00 <b>(-35.77%)</b></td><td>95422.70 (-0.38%)</td><td>94913.04 (-0.29%)</td><td>94832.90 (-0.49%)</td><td>94460.40 (+0.20%)</td><td>368.88 <b>(-35.83%)</b></td><td>727.49 (-0.20%)</td><td>724.03 (+0.28%)</td><td>724.64 (+0.49%)</td><td>720.16 (+0.38%)</td><td>2.81 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95785.00 (n/a)</td><td>95184.88 (n/a)</td><td>95297.40 (n/a)</td><td>94274.30 (n/a)</td><td>574.82 (n/a)</td><td>728.93 (n/a)</td><td>721.98 (n/a)</td><td>721.11 (n/a)</td><td>717.43 (n/a)</td><td>4.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.04 (-10.51%)</td><td>2.91 (-17.55%)</td><td>2.23 <b>(-43.18%)</b></td><td>2.14 (-4.22%)</td><td>0.99 (+2.65%)</td><td>4170.80 (+4.41%)</td><td>3338.94 <b>(+23.19%)</b></td><td>3999.70 <b>(+75.99%)</b></td><td>2207.50 (+11.75%)</td><td>1009.39 (+18.49%)</td><td>243.21 (-10.51%)</td><td>175.16 (-17.55%)</td><td>134.23 <b>(-43.18%)</b></td><td>128.72 (-4.22%)</td><td>59.44 (+2.65%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.51 (n/a)</td><td>3.53 (n/a)</td><td>3.92 (n/a)</td><td>2.23 (n/a)</td><td>0.96 (n/a)</td><td>3994.60 (n/a)</td><td>2710.34 (n/a)</td><td>2272.70 (n/a)</td><td>1975.40 (n/a)</td><td>851.87 (n/a)</td><td>271.78 (n/a)</td><td>212.45 (n/a)</td><td>236.22 (n/a)</td><td>134.40 (n/a)</td><td>57.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.94 (-16.52%)</td><td>2.48 <b>(-24.08%)</b></td><td>2.18 (-16.88%)</td><td>1.79 <b>(-20.13%)</b></td><td>0.84 <b>(-30.41%)</b></td><td>4981.70 <b>(+25.20%)</b></td><td>3862.90 <b>(+27.46%)</b></td><td>4079.20 <b>(+20.31%)</b></td><td>2262.50 (+19.79%)</td><td>991.05 (-1.86%)</td><td>237.29 (-16.52%)</td><td>149.14 <b>(-24.08%)</b></td><td>131.61 (-16.88%)</td><td>107.77 <b>(-20.13%)</b></td><td>50.63 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.72 (n/a)</td><td>3.26 (n/a)</td><td>2.63 (n/a)</td><td>2.24 (n/a)</td><td>1.21 (n/a)</td><td>3979.00 (n/a)</td><td>3030.66 (n/a)</td><td>3390.70 (n/a)</td><td>1888.70 (n/a)</td><td>1009.84 (n/a)</td><td>284.25 (n/a)</td><td>196.43 (n/a)</td><td>158.34 (n/a)</td><td>134.92 (n/a)</td><td>72.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.03 (-7.81%)</td><td>3.63 (-16.86%)</td><td>4.00 (-18.89%)</td><td>2.15 (-1.53%)</td><td>1.14 (-14.65%)</td><td>4150.30 (+1.56%)</td><td>2689.04 (+17.56%)</td><td>2230.30 <b>(+23.29%)</b></td><td>1773.40 (+8.47%)</td><td>959.44 (-6.79%)</td><td>302.73 (-7.81%)</td><td>218.70 (-16.86%)</td><td>240.71 (-18.89%)</td><td>129.36 (-1.53%)</td><td>68.54 (-14.65%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.45 (n/a)</td><td>4.37 (n/a)</td><td>4.93 (n/a)</td><td>2.18 (n/a)</td><td>1.33 (n/a)</td><td>4086.70 (n/a)</td><td>2287.42 (n/a)</td><td>1809.00 (n/a)</td><td>1634.90 (n/a)</td><td>1029.38 (n/a)</td><td>328.37 (n/a)</td><td>263.05 (n/a)</td><td>296.77 (n/a)</td><td>131.37 (n/a)</td><td>80.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.15 (-9.82%)</td><td>5.41 (-7.48%)</td><td>5.44 (-9.95%)</td><td>4.82 (-1.90%)</td><td>0.53 <b>(-32.03%)</b></td><td>7239.30 (+1.93%)</td><td>6489.82 (+7.33%)</td><td>6405.80 (+11.05%)</td><td>5670.60 (+10.89%)</td><td>626.27 <b>(-23.65%)</b></td><td>378.71 (-9.82%)</td><td>333.41 (-7.48%)</td><td>335.24 (-9.95%)</td><td>296.64 (-1.90%)</td><td>32.61 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.82 (n/a)</td><td>5.85 (n/a)</td><td>6.04 (n/a)</td><td>4.91 (n/a)</td><td>0.78 (n/a)</td><td>7102.10 (n/a)</td><td>6046.46 (n/a)</td><td>5768.40 (n/a)</td><td>5113.90 (n/a)</td><td>820.29 (n/a)</td><td>419.93 (n/a)</td><td>360.35 (n/a)</td><td>372.29 (n/a)</td><td>302.37 (n/a)</td><td>47.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.09 (-4.96%)</td><td>4.18 (-3.70%)</td><td>4.09 (-7.49%)</td><td>3.63 (-0.93%)</td><td>0.54 <b>(-23.12%)</b></td><td>9603.00 (+0.94%)</td><td>8448.80 (+2.98%)</td><td>8517.40 (+8.10%)</td><td>6855.50 (+5.22%)</td><td>998.80 <b>(-22.93%)</b></td><td>313.25 (-4.96%)</td><td>257.32 (-3.70%)</td><td>252.13 (-7.49%)</td><td>223.63 (-0.93%)</td><td>33.44 <b>(-23.12%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.35 (n/a)</td><td>4.34 (n/a)</td><td>4.42 (n/a)</td><td>3.66 (n/a)</td><td>0.71 (n/a)</td><td>9513.80 (n/a)</td><td>8204.28 (n/a)</td><td>7879.20 (n/a)</td><td>6515.50 (n/a)</td><td>1295.97 (n/a)</td><td>329.59 (n/a)</td><td>267.21 (n/a)</td><td>272.55 (n/a)</td><td>225.72 (n/a)</td><td>43.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.48 (-3.80%)</td><td>5.88 (+18.19%)</td><td>6.00 <b>(+32.78%)</b></td><td>5.14 (+16.18%)</td><td>0.63 <b>(-36.53%)</b></td><td>6788.50 (-13.93%)</td><td>5990.46 (-16.76%)</td><td>5807.80 <b>(-24.69%)</b></td><td>5380.30 (+3.95%)</td><td>656.92 <b>(-42.57%)</b></td><td>399.14 (-3.80%)</td><td>361.89 (+18.19%)</td><td>369.76 <b>(+32.78%)</b></td><td>316.34 (+16.18%)</td><td>38.81 <b>(-36.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.74 (n/a)</td><td>4.97 (n/a)</td><td>4.52 (n/a)</td><td>4.42 (n/a)</td><td>0.99 (n/a)</td><td>7886.80 (n/a)</td><td>7196.34 (n/a)</td><td>7711.60 (n/a)</td><td>5176.00 (n/a)</td><td>1143.80 (n/a)</td><td>414.89 (n/a)</td><td>306.18 (n/a)</td><td>278.48 (n/a)</td><td>272.29 (n/a)</td><td>61.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.77 (-2.12%)</td><td>0.77 (+1.31%)</td><td>0.77 (+2.10%)</td><td>0.76 (+4.41%)</td><td>0.01 <b>(-77.12%)</b></td><td>99145.70 (-4.22%)</td><td>98219.86 (-1.35%)</td><td>98065.70 (-2.06%)</td><td>97604.10 (+2.16%)</td><td>651.37 <b>(-77.60%)</b></td><td>704.06 (-2.12%)</td><td>699.67 (+1.31%)</td><td>700.75 (+2.10%)</td><td>693.12 (+4.41%)</td><td>4.63 <b>(-77.12%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103513.60 (n/a)</td><td>99568.74 (n/a)</td><td>100129.70 (n/a)</td><td>95536.60 (n/a)</td><td>2908.27 (n/a)</td><td>719.30 (n/a)</td><td>690.64 (n/a)</td><td>686.30 (n/a)</td><td>663.87 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.78 (+0.72%)</td><td>0.76 (+0.13%)</td><td>0.76 (-1.20%)</td><td>0.75 (+2.10%)</td><td>0.01 <b>(-27.93%)</b></td><td>100306.60 (-2.06%)</td><td>99285.44 (-0.15%)</td><td>99862.30 (+1.21%)</td><td>96900.10 (-0.71%)</td><td>1383.73 <b>(-30.07%)</b></td><td>709.18 (+0.72%)</td><td>692.25 (+0.13%)</td><td>688.14 (-1.20%)</td><td>685.09 (+2.10%)</td><td>9.80 <b>(-27.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>102416.60 (n/a)</td><td>99432.80 (n/a)</td><td>98667.40 (n/a)</td><td>97596.60 (n/a)</td><td>1978.67 (n/a)</td><td>704.12 (n/a)</td><td>691.33 (n/a)</td><td>696.48 (n/a)</td><td>670.98 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.81 (-0.00%)</td><td>0.80 (-0.14%)</td><td>0.80 (+0.07%)</td><td>0.80 (-0.65%)</td><td>0.01 <b>(+99.31%)</b></td><td>94596.00 (+0.65%)</td><td>93874.04 (+0.15%)</td><td>93836.80 (-0.07%)</td><td>93237.40 (+0.00%)</td><td>625.10 <b>(+100.54%)</b></td><td>737.04 (-0.00%)</td><td>732.07 (-0.14%)</td><td>732.33 (+0.07%)</td><td>726.45 (-0.65%)</td><td>4.87 <b>(+99.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>93981.80 (n/a)</td><td>93736.52 (n/a)</td><td>93902.60 (n/a)</td><td>93236.50 (n/a)</td><td>311.72 (n/a)</td><td>737.04 (n/a)</td><td>733.12 (n/a)</td><td>731.82 (n/a)</td><td>731.20 (n/a)</td><td>2.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.52 (+2.56%)</td><td>2.66 <b>(+45.33%)</b></td><td>2.62 <b>(+64.15%)</b></td><td>1.37 <b>(+27.01%)</b></td><td>0.86 (-8.32%)</td><td>5883.70 <b>(-21.27%)</b></td><td>3397.32 <b>(-34.22%)</b></td><td>3081.00 <b>(-39.08%)</b></td><td>2290.00 (-2.50%)</td><td>1458.84 <b>(-25.33%)</b></td><td>923.13 (+2.56%)</td><td>696.86 <b>(+45.33%)</b></td><td>686.11 <b>(+64.15%)</b></td><td>359.29 <b>(+27.01%)</b></td><td>225.54 (-8.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.43 (n/a)</td><td>1.83 (n/a)</td><td>1.59 (n/a)</td><td>1.08 (n/a)</td><td>0.94 (n/a)</td><td>7472.90 (n/a)</td><td>5165.04 (n/a)</td><td>5057.50 (n/a)</td><td>2348.60 (n/a)</td><td>1953.81 (n/a)</td><td>900.07 (n/a)</td><td>479.49 (n/a)</td><td>417.98 (n/a)</td><td>282.88 (n/a)</td><td>246.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 (-8.26%)</td><td>0.18 (-9.01%)</td><td>0.19 (-2.21%)</td><td>0.13 <b>(-28.76%)</b></td><td>0.03 <b>(+62.44%)</b></td><td>9780.60 <b>(+40.36%)</b></td><td>7170.38 (+12.67%)</td><td>6415.20 (+2.26%)</td><td>5917.80 (+9.00%)</td><td>1578.36 <b>(+149.14%)</b></td><td>11.34 (-8.26%)</td><td>9.68 (-9.01%)</td><td>10.46 (-2.21%)</td><td>6.86 <b>(-28.76%)</b></td><td>1.81 <b>(+62.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>6968.00 (n/a)</td><td>6364.20 (n/a)</td><td>6273.70 (n/a)</td><td>5429.00 (n/a)</td><td>633.52 (n/a)</td><td>12.36 (n/a)</td><td>10.63 (n/a)</td><td>10.70 (n/a)</td><td>9.63 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.76 (n/a)</td><td>3.43 (n/a)</td><td>3.46 (n/a)</td><td>3.05 (n/a)</td><td>0.25 (n/a)</td><td>3.76 (n/a)</td><td>3.43 (n/a)</td><td>3.46 (n/a)</td><td>3.05 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.28 (-0.07%)</td><td>6.49 (-2.79%)</td><td>6.63 (-5.61%)</td><td>5.64 (-0.18%)</td><td>0.74 (+4.89%)</td><td>7.28 (-0.07%)</td><td>6.49 (-2.79%)</td><td>6.63 (-5.61%)</td><td>5.64 (-0.18%)</td><td>0.74 (+4.89%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.29 (n/a)</td><td>6.68 (n/a)</td><td>7.02 (n/a)</td><td>5.65 (n/a)</td><td>0.71 (n/a)</td><td>7.28 (n/a)</td><td>6.67 (n/a)</td><td>7.02 (n/a)</td><td>5.65 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>11.03 (-14.45%)</td><td>9.12 (-7.91%)</td><td>9.46 (+0.13%)</td><td>7.59 (-7.32%)</td><td>1.47 (-16.89%)</td><td>11.02 (-14.45%)</td><td>9.11 (-7.91%)</td><td>9.45 (+0.13%)</td><td>7.58 (-7.32%)</td><td>1.46 (-16.89%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>12.89 (n/a)</td><td>9.90 (n/a)</td><td>9.44 (n/a)</td><td>8.18 (n/a)</td><td>1.76 (n/a)</td><td>12.88 (n/a)</td><td>9.90 (n/a)</td><td>9.44 (n/a)</td><td>8.18 (n/a)</td><td>1.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.91 (n/a)</td><td>3.73 (n/a)</td><td>3.76 (n/a)</td><td>3.39 (n/a)</td><td>0.21 (n/a)</td><td>3.90 (n/a)</td><td>3.73 (n/a)</td><td>3.75 (n/a)</td><td>3.39 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.22 (+10.45%)</td><td>6.36 (+3.88%)</td><td>6.15 (+2.45%)</td><td>5.87 (+3.62%)</td><td>0.54 <b>(+54.78%)</b></td><td>7.22 (+10.45%)</td><td>6.36 (+3.88%)</td><td>6.15 (+2.45%)</td><td>5.87 (+3.62%)</td><td>0.54 <b>(+54.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.54 (n/a)</td><td>6.12 (n/a)</td><td>6.00 (n/a)</td><td>5.67 (n/a)</td><td>0.35 (n/a)</td><td>6.54 (n/a)</td><td>6.12 (n/a)</td><td>6.00 (n/a)</td><td>5.66 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>9.52 <b>(-31.89%)</b></td><td>8.55 (-7.33%)</td><td>8.52 (+5.91%)</td><td>7.17 (-7.76%)</td><td>0.90 <b>(-66.29%)</b></td><td>9.51 <b>(-31.89%)</b></td><td>8.54 (-7.33%)</td><td>8.52 (+5.91%)</td><td>7.16 (-7.76%)</td><td>0.90 <b>(-66.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>13.97 (n/a)</td><td>9.22 (n/a)</td><td>8.05 (n/a)</td><td>7.77 (n/a)</td><td>2.67 (n/a)</td><td>13.96 (n/a)</td><td>9.22 (n/a)</td><td>8.04 (n/a)</td><td>7.77 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.98 (-3.16%)</td><td>1.74 <b>(-40.02%)</b></td><td>1.07 <b>(-62.43%)</b></td><td>1.04 <b>(-62.77%)</b></td><td>0.94 <b>(+732.53%)</b></td><td>2.97 (-3.16%)</td><td>1.73 <b>(-40.02%)</b></td><td>1.07 <b>(-62.43%)</b></td><td>1.04 <b>(-62.77%)</b></td><td>0.94 <b>(+732.52%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.08 (n/a)</td><td>2.90 (n/a)</td><td>2.86 (n/a)</td><td>2.79 (n/a)</td><td>0.11 (n/a)</td><td>3.07 (n/a)</td><td>2.89 (n/a)</td><td>2.85 (n/a)</td><td>2.79 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.54 (+6.02%)</td><td>0.32 (-11.48%)</td><td>0.37 (-9.48%)</td><td>0.08 (-0.62%)</td><td>0.23 <b>(+40.68%)</b></td><td>0.53 (+6.02%)</td><td>0.31 (-11.48%)</td><td>0.36 (-9.48%)</td><td>0.07 (-0.62%)</td><td>0.23 <b>(+40.68%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>0.17 (n/a)</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.72 (+5.91%)</td><td>0.59 (+8.75%)</td><td>0.64 (-3.30%)</td><td>0.30 (-12.46%)</td><td>0.17 (-5.81%)</td><td>0.71 (+5.91%)</td><td>0.58 (+8.75%)</td><td>0.63 (-3.30%)</td><td>0.30 (-12.46%)</td><td>0.16 (-5.81%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.68 (n/a)</td><td>0.54 (n/a)</td><td>0.66 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.67 (n/a)</td><td>0.53 (n/a)</td><td>0.65 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.60 (+8.34%)</td><td>1.73 <b>(+35.25%)</b></td><td>1.61 (+11.94%)</td><td>0.85 <b>(+90.49%)</b></td><td>0.65 <b>(-22.47%)</b></td><td>2.56 (+8.34%)</td><td>1.70 <b>(+35.25%)</b></td><td>1.58 (+11.94%)</td><td>0.84 <b>(+90.49%)</b></td><td>0.64 <b>(-22.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.40 (n/a)</td><td>1.28 (n/a)</td><td>1.44 (n/a)</td><td>0.45 (n/a)</td><td>0.84 (n/a)</td><td>2.36 (n/a)</td><td>1.26 (n/a)</td><td>1.41 (n/a)</td><td>0.44 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.80 (n/a)</td><td>338.38 (n/a)</td><td>293.00 (n/a)</td><td>213.50 (n/a)</td><td>106.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.40 (n/a)</td><td>450.58 (n/a)</td><td>451.90 (n/a)</td><td>301.90 (n/a)</td><td>92.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1938.80 (n/a)</td><td>705.32 (n/a)</td><td>409.80 (n/a)</td><td>323.10 (n/a)</td><td>693.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.80 (n/a)</td><td>451.98 (n/a)</td><td>426.70 (n/a)</td><td>248.10 (n/a)</td><td>137.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.00 (n/a)</td><td>356.96 (n/a)</td><td>343.20 (n/a)</td><td>276.40 (n/a)</td><td>64.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.50 (n/a)</td><td>398.44 (n/a)</td><td>433.70 (n/a)</td><td>233.40 (n/a)</td><td>111.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.40 (n/a)</td><td>434.04 (n/a)</td><td>409.40 (n/a)</td><td>269.70 (n/a)</td><td>151.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.30 (n/a)</td><td>369.66 (n/a)</td><td>387.30 (n/a)</td><td>278.10 (n/a)</td><td>83.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.30 (n/a)</td><td>430.68 (n/a)</td><td>513.10 (n/a)</td><td>246.80 (n/a)</td><td>152.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.20 (n/a)</td><td>482.34 (n/a)</td><td>483.30 (n/a)</td><td>287.90 (n/a)</td><td>141.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.80 (n/a)</td><td>384.00 (n/a)</td><td>289.90 (n/a)</td><td>251.80 (n/a)</td><td>158.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.20 (n/a)</td><td>404.98 (n/a)</td><td>330.10 (n/a)</td><td>288.40 (n/a)</td><td>138.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.90 (n/a)</td><td>341.36 (n/a)</td><td>279.40 (n/a)</td><td>261.40 (n/a)</td><td>101.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>528.60 (n/a)</td><td>395.24 (n/a)</td><td>405.90 (n/a)</td><td>249.10 (n/a)</td><td>122.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.50 (n/a)</td><td>402.64 (n/a)</td><td>303.50 (n/a)</td><td>266.10 (n/a)</td><td>168.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1302.00 (n/a)</td><td>516.06 (n/a)</td><td>387.40 (n/a)</td><td>198.50 (n/a)</td><td>451.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.50 (n/a)</td><td>430.60 (n/a)</td><td>486.10 (n/a)</td><td>218.40 (n/a)</td><td>124.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1017.10 (n/a)</td><td>591.26 (n/a)</td><td>523.00 (n/a)</td><td>343.80 (n/a)</td><td>255.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>554.50 (n/a)</td><td>439.34 (n/a)</td><td>523.10 (n/a)</td><td>267.30 (n/a)</td><td>141.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>712.00 (n/a)</td><td>496.86 (n/a)</td><td>529.00 (n/a)</td><td>274.00 (n/a)</td><td>159.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.60 (n/a)</td><td>419.84 (n/a)</td><td>506.40 (n/a)</td><td>276.40 (n/a)</td><td>128.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>992.20 (n/a)</td><td>582.54 (n/a)</td><td>480.10 (n/a)</td><td>430.60 (n/a)</td><td>232.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1861.10 (n/a)</td><td>693.62 (n/a)</td><td>512.20 (n/a)</td><td>276.30 (n/a)</td><td>663.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1912.00 (n/a)</td><td>709.02 (n/a)</td><td>484.30 (n/a)</td><td>255.50 (n/a)</td><td>683.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+3.51%)</td><td>0.01 (+16.42%)</td><td>0.01 (+14.57%)</td><td>0.01 (+3.87%)</td><td>0.00 (+10.73%)</td><td>482.10 (-3.73%)</td><td>373.00 (-13.27%)</td><td>430.30 (-12.72%)</td><td>240.10 (-3.38%)</td><td>110.58 (+2.61%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.80 (n/a)</td><td>430.06 (n/a)</td><td>493.00 (n/a)</td><td>248.50 (n/a)</td><td>107.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-5.16%)</td><td>0.01 (+14.61%)</td><td>0.01 <b>(+44.13%)</b></td><td>0.01 (-8.66%)</td><td>0.00 (-10.47%)</td><td>566.90 (+9.48%)</td><td>341.38 (-13.08%)</td><td>288.00 <b>(-30.64%)</b></td><td>269.60 (+5.44%)</td><td>127.28 (+6.21%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.80 (n/a)</td><td>392.74 (n/a)</td><td>415.20 (n/a)</td><td>255.70 (n/a)</td><td>119.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (-5.66%)</td><td>0.01 (-7.91%)</td><td>0.01 (+2.74%)</td><td>0.01 (+11.49%)</td><td>0.00 <b>(-30.09%)</b></td><td>529.90 (-10.31%)</td><td>432.16 (+4.58%)</td><td>423.30 (-2.67%)</td><td>304.40 (+6.03%)</td><td>90.53 <b>(-28.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.80 (n/a)</td><td>413.24 (n/a)</td><td>434.90 (n/a)</td><td>287.10 (n/a)</td><td>127.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+0.63%)</td><td>0.01 (+0.64%)</td><td>0.01 (-0.92%)</td><td>0.01 (+2.15%)</td><td>0.00 (+8.55%)</td><td>578.60 (-2.10%)</td><td>436.44 (+0.98%)</td><td>506.40 (+0.92%)</td><td>261.60 (-0.65%)</td><td>152.02 (+7.12%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.00 (n/a)</td><td>432.22 (n/a)</td><td>501.80 (n/a)</td><td>263.30 (n/a)</td><td>141.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-14.44%)</td><td>0.01 (+5.42%)</td><td>0.01 <b>(+25.28%)</b></td><td>0.01 (+10.51%)</td><td>0.01 <b>(-25.93%)</b></td><td>579.50 (-9.51%)</td><td>372.50 (-12.37%)</td><td>343.20 <b>(-20.19%)</b></td><td>199.80 (+16.91%)</td><td>149.76 (-19.57%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.40 (n/a)</td><td>425.10 (n/a)</td><td>430.00 (n/a)</td><td>170.90 (n/a)</td><td>186.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+14.22%)</td><td>0.01 (+11.65%)</td><td>0.01 (-3.06%)</td><td>0.01 (+10.88%)</td><td>0.00 <b>(+20.29%)</b></td><td>531.70 (-9.80%)</td><td>421.30 (-9.64%)</td><td>480.70 (+3.15%)</td><td>251.60 (-12.46%)</td><td>117.74 (-6.51%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.50 (n/a)</td><td>466.24 (n/a)</td><td>466.00 (n/a)</td><td>287.40 (n/a)</td><td>125.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 <b>(+25.24%)</b></td><td>0.02 <b>(+60.20%)</b></td><td>0.02 <b>(+41.13%)</b></td><td>0.01 <b>(+336.71%)</b></td><td>0.01 (-9.18%)</td><td>575.60 <b>(-77.10%)</b></td><td>400.90 <b>(-57.78%)</b></td><td>358.40 <b>(-29.13%)</b></td><td>258.30 <b>(-20.15%)</b></td><td>140.56 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2513.80 (n/a)</td><td>949.64 (n/a)</td><td>505.70 (n/a)</td><td>323.50 (n/a)</td><td>900.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-6.01%)</td><td>0.02 (-10.81%)</td><td>0.02 <b>(-37.18%)</b></td><td>0.02 <b>(+32.74%)</b></td><td>0.01 <b>(-40.55%)</b></td><td>505.10 <b>(-24.67%)</b></td><td>387.68 (-0.89%)</td><td>420.80 <b>(+59.21%)</b></td><td>259.90 (+6.39%)</td><td>96.54 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.50 (n/a)</td><td>391.18 (n/a)</td><td>264.30 (n/a)</td><td>244.30 (n/a)</td><td>196.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+26.13%)</b></td><td>0.02 (+19.97%)</td><td>0.03 <b>(+35.89%)</b></td><td>0.01 (-15.67%)</td><td>0.01 <b>(+79.37%)</b></td><td>630.30 (+18.59%)</td><td>388.04 (-9.32%)</td><td>314.90 <b>(-26.41%)</b></td><td>230.30 <b>(-20.72%)</b></td><td>161.57 <b>(+77.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>531.50 (n/a)</td><td>427.92 (n/a)</td><td>427.90 (n/a)</td><td>290.50 (n/a)</td><td>91.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-10.35%)</td><td>0.02 (-13.99%)</td><td>0.02 <b>(-32.34%)</b></td><td>0.02 (+15.40%)</td><td>0.01 <b>(-27.50%)</b></td><td>535.20 (-13.34%)</td><td>376.70 (+8.25%)</td><td>392.30 <b>(+47.76%)</b></td><td>242.50 (+11.55%)</td><td>114.97 <b>(-31.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.60 (n/a)</td><td>347.98 (n/a)</td><td>265.50 (n/a)</td><td>217.40 (n/a)</td><td>166.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+1.28%)</td><td>0.02 (-3.53%)</td><td>0.02 (-11.49%)</td><td>0.01 (-7.08%)</td><td>0.01 (+13.85%)</td><td>553.00 (+7.61%)</td><td>427.64 (+7.40%)</td><td>526.60 (+12.98%)</td><td>239.20 (-1.24%)</td><td>152.41 <b>(+23.96%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.90 (n/a)</td><td>398.16 (n/a)</td><td>466.10 (n/a)</td><td>242.20 (n/a)</td><td>122.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-13.33%)</td><td>0.02 (-19.13%)</td><td>0.02 <b>(-46.86%)</b></td><td>0.01 (-5.24%)</td><td>0.01 <b>(-22.26%)</b></td><td>1075.90 (+5.52%)</td><td>538.40 (+14.83%)</td><td>498.60 <b>(+88.15%)</b></td><td>285.30 (+15.37%)</td><td>320.64 (-3.55%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1019.60 (n/a)</td><td>468.88 (n/a)</td><td>265.00 (n/a)</td><td>247.30 (n/a)</td><td>332.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (+6.77%)</td><td>0.02 (-7.62%)</td><td>0.03 (+3.65%)</td><td>0.01 <b>(-32.61%)</b></td><td>0.01 <b>(+45.70%)</b></td><td>738.70 <b>(+48.36%)</b></td><td>451.92 <b>(+27.80%)</b></td><td>291.10 (-3.51%)</td><td>215.40 (-6.35%)</td><td>257.58 <b>(+117.10%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.90 (n/a)</td><td>353.62 (n/a)</td><td>301.70 (n/a)</td><td>230.00 (n/a)</td><td>118.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-12.27%)</td><td>0.02 (-5.16%)</td><td>0.01 (-19.91%)</td><td>0.01 <b>(+109.40%)</b></td><td>0.01 <b>(-36.06%)</b></td><td>652.10 <b>(-52.24%)</b></td><td>550.24 (-12.85%)</td><td>625.80 <b>(+24.86%)</b></td><td>335.60 (+13.96%)</td><td>134.99 <b>(-68.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1365.40 (n/a)</td><td>631.38 (n/a)</td><td>501.20 (n/a)</td><td>294.50 (n/a)</td><td>422.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+4.92%)</td><td>0.05 (+7.33%)</td><td>0.05 <b>(+20.05%)</b></td><td>0.03 (+1.87%)</td><td>0.01 (+7.18%)</td><td>475.60 (-1.84%)</td><td>352.28 (-6.48%)</td><td>319.90 (-16.71%)</td><td>270.60 (-4.72%)</td><td>85.45 (+2.49%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.50 (n/a)</td><td>376.70 (n/a)</td><td>384.10 (n/a)</td><td>284.00 (n/a)</td><td>83.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (-2.16%)</td><td>0.05 <b>(+20.27%)</b></td><td>0.06 <b>(+68.51%)</b></td><td>0.03 <b>(+59.31%)</b></td><td>0.02 <b>(-26.23%)</b></td><td>509.00 <b>(-37.23%)</b></td><td>361.62 <b>(-26.20%)</b></td><td>294.30 <b>(-40.65%)</b></td><td>255.40 (+2.20%)</td><td>122.23 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>810.90 (n/a)</td><td>490.00 (n/a)</td><td>495.90 (n/a)</td><td>249.90 (n/a)</td><td>237.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-1.50%)</td><td>0.05 (+5.22%)</td><td>0.04 (+5.16%)</td><td>0.03 (-7.55%)</td><td>0.02 (+10.28%)</td><td>584.60 (+8.16%)</td><td>397.32 (-2.47%)</td><td>420.00 (-4.91%)</td><td>241.00 (+1.52%)</td><td>140.75 <b>(+20.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.50 (n/a)</td><td>407.38 (n/a)</td><td>441.70 (n/a)</td><td>237.40 (n/a)</td><td>116.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 <b>(+41.60%)</b></td><td>0.05 <b>(+34.06%)</b></td><td>0.06 <b>(+69.39%)</b></td><td>0.03 (+8.16%)</td><td>0.02 <b>(+143.00%)</b></td><td>540.80 (-7.54%)</td><td>369.68 (-18.95%)</td><td>276.10 <b>(-40.95%)</b></td><td>247.20 <b>(-29.37%)</b></td><td>143.19 <b>(+63.87%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>456.14 (n/a)</td><td>467.60 (n/a)</td><td>350.00 (n/a)</td><td>87.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+0.40%)</td><td>0.05 (+11.60%)</td><td>0.04 <b>(+21.25%)</b></td><td>0.03 (+5.68%)</td><td>0.02 (-3.96%)</td><td>540.60 (-5.39%)</td><td>377.92 (-11.81%)</td><td>407.30 (-17.53%)</td><td>241.50 (-0.37%)</td><td>121.43 (-12.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.40 (n/a)</td><td>428.52 (n/a)</td><td>493.90 (n/a)</td><td>242.40 (n/a)</td><td>138.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(+35.83%)</b></td><td>0.04 <b>(+25.17%)</b></td><td>0.04 (+18.97%)</td><td>0.02 <b>(+231.45%)</b></td><td>0.01 (+3.46%)</td><td>764.20 <b>(-69.83%)</b></td><td>497.66 <b>(-43.80%)</b></td><td>435.40 (-15.93%)</td><td>275.30 <b>(-26.37%)</b></td><td>185.05 <b>(-79.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2532.70 (n/a)</td><td>885.54 (n/a)</td><td>517.90 (n/a)</td><td>373.90 (n/a)</td><td>923.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 <b>(+20.89%)</b></td><td>0.10 <b>(+28.14%)</b></td><td>0.10 <b>(+39.36%)</b></td><td>0.06 (-0.20%)</td><td>0.03 <b>(+58.30%)</b></td><td>564.30 (+0.21%)</td><td>361.62 (-17.78%)</td><td>336.60 <b>(-28.23%)</b></td><td>237.70 (-17.26%)</td><td>135.07 <b>(+31.57%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>563.10 (n/a)</td><td>439.80 (n/a)</td><td>469.00 (n/a)</td><td>287.30 (n/a)</td><td>102.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 <b>(+32.08%)</b></td><td>0.08 <b>(+28.91%)</b></td><td>0.07 <b>(+25.75%)</b></td><td>0.06 <b>(+75.33%)</b></td><td>0.02 (+0.25%)</td><td>570.90 <b>(-42.96%)</b></td><td>441.78 <b>(-26.50%)</b></td><td>440.80 <b>(-20.46%)</b></td><td>310.00 <b>(-24.28%)</b></td><td>93.28 <b>(-59.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1000.90 (n/a)</td><td>601.08 (n/a)</td><td>554.20 (n/a)</td><td>409.40 (n/a)</td><td>232.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (-5.19%)</td><td>0.09 (-4.65%)</td><td>0.07 (-6.62%)</td><td>0.06 (-10.75%)</td><td>0.03 (+13.43%)</td><td>538.30 (+12.05%)</td><td>417.04 (+7.54%)</td><td>461.10 (+7.08%)</td><td>282.60 (+5.49%)</td><td>124.65 <b>(+29.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>480.40 (n/a)</td><td>387.80 (n/a)</td><td>430.60 (n/a)</td><td>267.90 (n/a)</td><td>96.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (-0.69%)</td><td>0.08 (+14.51%)</td><td>0.08 (+10.57%)</td><td>0.02 (+9.92%)</td><td>0.04 (+8.31%)</td><td>1894.80 (-9.02%)</td><td>660.10 (-11.05%)</td><td>430.90 (-9.55%)</td><td>252.70 (+0.68%)</td><td>695.81 (-7.94%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2082.70 (n/a)</td><td>742.12 (n/a)</td><td>476.40 (n/a)</td><td>251.00 (n/a)</td><td>755.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (+2.16%)</td><td>0.08 (-0.17%)</td><td>0.07 (-5.29%)</td><td>0.06 (+0.98%)</td><td>0.03 (+2.39%)</td><td>581.60 (-0.97%)</td><td>431.68 (+0.12%)</td><td>448.10 (+5.58%)</td><td>239.10 (-2.13%)</td><td>142.94 (-2.90%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.30 (n/a)</td><td>431.16 (n/a)</td><td>424.40 (n/a)</td><td>244.30 (n/a)</td><td>147.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(+24.38%)</b></td><td>0.01 (+1.85%)</td><td>0.01 (-7.47%)</td><td>0.01 (-18.50%)</td><td>0.01 <b>(+40.89%)</b></td><td>587.00 <b>(+22.70%)</b></td><td>342.46 (+4.56%)</td><td>298.00 (+8.09%)</td><td>188.50 (-19.58%)</td><td>150.83 <b>(+43.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.40 (n/a)</td><td>327.54 (n/a)</td><td>275.70 (n/a)</td><td>234.40 (n/a)</td><td>105.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+4.29%)</td><td>0.02 (-3.30%)</td><td>0.02 (+5.56%)</td><td>0.01 <b>(-24.87%)</b></td><td>0.00 <b>(+94.98%)</b></td><td>374.90 <b>(+33.13%)</b></td><td>270.62 (+6.91%)</td><td>238.00 (-5.29%)</td><td>208.70 (-4.09%)</td><td>65.94 <b>(+151.70%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>281.60 (n/a)</td><td>253.12 (n/a)</td><td>251.30 (n/a)</td><td>217.60 (n/a)</td><td>26.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(+28.98%)</b></td><td>0.01 (+17.58%)</td><td>0.01 <b>(+43.67%)</b></td><td>0.01 (-4.19%)</td><td>0.01 <b>(+57.85%)</b></td><td>533.10 (+4.37%)</td><td>344.12 (-9.24%)</td><td>281.50 <b>(-30.39%)</b></td><td>203.10 <b>(-22.48%)</b></td><td>139.75 <b>(+35.88%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.80 (n/a)</td><td>379.16 (n/a)</td><td>404.40 (n/a)</td><td>262.00 (n/a)</td><td>102.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+1.16%)</td><td>0.01 (+8.45%)</td><td>0.01 (+4.24%)</td><td>0.01 <b>(+20.07%)</b></td><td>0.00 (-3.01%)</td><td>376.90 (-16.73%)</td><td>299.16 (-8.88%)</td><td>289.00 (-4.08%)</td><td>231.80 (-1.15%)</td><td>67.66 <b>(-21.52%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>452.60 (n/a)</td><td>328.32 (n/a)</td><td>301.30 (n/a)</td><td>234.50 (n/a)</td><td>86.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(+23.28%)</b></td><td>0.01 <b>(+24.97%)</b></td><td>0.02 <b>(+70.42%)</b></td><td>0.01 (-4.89%)</td><td>0.00 <b>(+65.51%)</b></td><td>501.20 (+5.14%)</td><td>333.00 (-14.48%)</td><td>262.20 <b>(-41.32%)</b></td><td>219.50 (-18.88%)</td><td>133.09 <b>(+41.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.70 (n/a)</td><td>389.36 (n/a)</td><td>446.80 (n/a)</td><td>270.60 (n/a)</td><td>94.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+2.86%)</td><td>0.01 (+10.76%)</td><td>0.02 (+7.98%)</td><td>0.01 (-15.36%)</td><td>0.01 (+10.60%)</td><td>744.30 (+18.16%)</td><td>344.70 (-3.63%)</td><td>248.20 (-7.39%)</td><td>217.30 (-2.77%)</td><td>224.18 <b>(+34.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.90 (n/a)</td><td>357.70 (n/a)</td><td>268.00 (n/a)</td><td>223.50 (n/a)</td><td>166.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-8.38%)</td><td>0.01 (+19.57%)</td><td>0.01 <b>(+63.48%)</b></td><td>0.01 <b>(+115.83%)</b></td><td>0.00 <b>(-43.45%)</b></td><td>507.00 <b>(-53.67%)</b></td><td>349.90 <b>(-34.50%)</b></td><td>279.80 <b>(-38.83%)</b></td><td>269.40 (+9.16%)</td><td>106.65 <b>(-69.56%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1094.30 (n/a)</td><td>534.16 (n/a)</td><td>457.40 (n/a)</td><td>246.80 (n/a)</td><td>350.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-15.66%)</td><td>0.01 (+6.69%)</td><td>0.02 (+14.54%)</td><td>0.01 <b>(+29.48%)</b></td><td>0.00 <b>(-43.61%)</b></td><td>395.90 <b>(-22.77%)</b></td><td>299.68 (-13.43%)</td><td>261.50 (-12.69%)</td><td>250.80 (+18.58%)</td><td>64.09 <b>(-50.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.60 (n/a)</td><td>346.18 (n/a)</td><td>299.50 (n/a)</td><td>211.50 (n/a)</td><td>130.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-6.53%)</td><td>0.01 (+6.00%)</td><td>0.01 (+12.81%)</td><td>0.01 (-5.30%)</td><td>0.00 (-3.64%)</td><td>610.30 (+5.61%)</td><td>390.68 (-5.75%)</td><td>390.60 (-11.35%)</td><td>256.80 (+6.96%)</td><td>144.93 (+3.86%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>577.90 (n/a)</td><td>414.50 (n/a)</td><td>440.60 (n/a)</td><td>240.10 (n/a)</td><td>139.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-32.38%)</b></td><td>0.01 <b>(-30.45%)</b></td><td>0.01 <b>(-40.81%)</b></td><td>0.01 (+7.03%)</td><td>0.00 <b>(-57.13%)</b></td><td>578.80 (-6.57%)</td><td>431.62 <b>(+30.68%)</b></td><td>427.70 <b>(+68.98%)</b></td><td>354.90 <b>(+47.87%)</b></td><td>91.54 <b>(-43.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.50 (n/a)</td><td>330.28 (n/a)</td><td>253.10 (n/a)</td><td>240.00 (n/a)</td><td>162.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (+5.01%)</td><td>0.01 (-11.81%)</td><td>0.01 <b>(-25.54%)</b></td><td>0.01 (+1.94%)</td><td>0.00 <b>(+26.50%)</b></td><td>565.50 (-1.89%)</td><td>492.60 (+16.35%)</td><td>562.20 <b>(+34.27%)</b></td><td>276.20 (-4.79%)</td><td>124.62 (+17.82%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.40 (n/a)</td><td>423.38 (n/a)</td><td>418.70 (n/a)</td><td>290.10 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (-11.86%)</td><td>0.01 (-9.81%)</td><td>0.01 <b>(-39.40%)</b></td><td>0.01 <b>(+214.67%)</b></td><td>0.00 <b>(-40.07%)</b></td><td>617.40 <b>(-68.22%)</b></td><td>470.66 <b>(-29.46%)</b></td><td>521.20 <b>(+64.99%)</b></td><td>289.30 (+13.45%)</td><td>149.13 <b>(-79.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1942.80 (n/a)</td><td>667.24 (n/a)</td><td>315.90 (n/a)</td><td>255.00 (n/a)</td><td>721.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+1.15%)</td><td>0.03 <b>(+22.19%)</b></td><td>0.03 <b>(+59.37%)</b></td><td>0.02 <b>(+23.97%)</b></td><td>0.01 <b>(-27.05%)</b></td><td>473.00 (-19.34%)</td><td>312.22 <b>(-23.86%)</b></td><td>280.10 <b>(-37.24%)</b></td><td>234.10 (-1.14%)</td><td>96.19 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.40 (n/a)</td><td>410.08 (n/a)</td><td>446.30 (n/a)</td><td>236.80 (n/a)</td><td>156.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+20.93%)</b></td><td>0.03 (+6.32%)</td><td>0.03 (+9.15%)</td><td>0.02 (+11.18%)</td><td>0.01 <b>(+47.00%)</b></td><td>491.50 (-10.06%)</td><td>332.70 (-2.02%)</td><td>268.70 (-8.39%)</td><td>212.30 (-17.30%)</td><td>128.27 (+8.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.50 (n/a)</td><td>339.56 (n/a)</td><td>293.30 (n/a)</td><td>256.70 (n/a)</td><td>118.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-7.96%)</td><td>0.03 (+17.68%)</td><td>0.03 <b>(+65.76%)</b></td><td>0.01 (+2.52%)</td><td>0.01 <b>(-20.44%)</b></td><td>571.90 (-2.46%)</td><td>331.06 (-17.49%)</td><td>276.60 <b>(-39.67%)</b></td><td>263.70 (+8.61%)</td><td>134.77 (-8.16%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.30 (n/a)</td><td>401.22 (n/a)</td><td>458.50 (n/a)</td><td>242.80 (n/a)</td><td>146.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (+5.34%)</td><td>0.03 (+15.99%)</td><td>0.03 (+3.74%)</td><td>0.02 <b>(+28.82%)</b></td><td>0.01 <b>(-25.20%)</b></td><td>371.70 <b>(-22.38%)</b></td><td>276.62 (-17.58%)</td><td>259.40 (-3.60%)</td><td>230.50 (-5.07%)</td><td>58.68 <b>(-45.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.90 (n/a)</td><td>335.64 (n/a)</td><td>269.10 (n/a)</td><td>242.80 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-16.36%)</td><td>0.02 (-9.57%)</td><td>0.02 (+0.86%)</td><td>0.01 (-15.21%)</td><td>0.01 (-8.39%)</td><td>566.20 (+17.96%)</td><td>403.68 (+12.25%)</td><td>399.60 (-0.84%)</td><td>255.90 (+19.52%)</td><td>143.31 <b>(+27.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.00 (n/a)</td><td>359.62 (n/a)</td><td>403.00 (n/a)</td><td>214.10 (n/a)</td><td>112.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+22.25%)</b></td><td>0.03 (-13.28%)</td><td>0.02 <b>(-21.68%)</b></td><td>0.02 <b>(-24.87%)</b></td><td>0.01 <b>(+102.25%)</b></td><td>502.60 <b>(+33.10%)</b></td><td>366.86 <b>(+26.56%)</b></td><td>346.80 <b>(+27.69%)</b></td><td>196.20 (-18.22%)</td><td>131.53 <b>(+131.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>377.60 (n/a)</td><td>289.86 (n/a)</td><td>271.60 (n/a)</td><td>239.90 (n/a)</td><td>56.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 <b>(-23.03%)</b></td><td>0.02 <b>(-25.59%)</b></td><td>0.02 <b>(-31.71%)</b></td><td>0.01 <b>(-22.24%)</b></td><td>0.01 <b>(-20.44%)</b></td><td>637.90 <b>(+28.61%)</b></td><td>475.78 <b>(+34.80%)</b></td><td>489.50 <b>(+46.43%)</b></td><td>318.70 <b>(+29.92%)</b></td><td>131.12 <b>(+31.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.00 (n/a)</td><td>352.96 (n/a)</td><td>334.30 (n/a)</td><td>245.30 (n/a)</td><td>99.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-1.43%)</td><td>0.02 (-18.53%)</td><td>0.02 <b>(-45.29%)</b></td><td>0.02 (-4.52%)</td><td>0.01 (+2.56%)</td><td>503.50 (+4.74%)</td><td>392.18 <b>(+24.64%)</b></td><td>444.60 <b>(+82.81%)</b></td><td>239.80 (+1.48%)</td><td>126.63 (+15.98%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.70 (n/a)</td><td>314.64 (n/a)</td><td>243.20 (n/a)</td><td>236.30 (n/a)</td><td>109.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+7.49%)</td><td>0.02 (-8.77%)</td><td>0.02 <b>(-24.12%)</b></td><td>0.01 (-1.45%)</td><td>0.01 (+13.34%)</td><td>586.60 (+1.47%)</td><td>420.40 (+12.06%)</td><td>466.30 <b>(+31.76%)</b></td><td>235.00 (-7.00%)</td><td>146.90 (+9.59%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>375.14 (n/a)</td><td>353.90 (n/a)</td><td>252.70 (n/a)</td><td>134.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-16.76%)</td><td>0.02 <b>(-24.22%)</b></td><td>0.02 <b>(-38.17%)</b></td><td>0.02 <b>(-23.11%)</b></td><td>0.01 (+8.66%)</td><td>544.60 <b>(+30.07%)</b></td><td>388.88 <b>(+36.70%)</b></td><td>434.80 <b>(+61.76%)</b></td><td>253.30 <b>(+20.16%)</b></td><td>123.54 <b>(+54.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>418.70 (n/a)</td><td>284.48 (n/a)</td><td>268.80 (n/a)</td><td>210.80 (n/a)</td><td>79.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-16.63%)</td><td>0.02 (-2.13%)</td><td>0.02 (+10.55%)</td><td>0.01 (-14.48%)</td><td>0.01 (-10.91%)</td><td>610.50 (+16.93%)</td><td>425.38 (+3.63%)</td><td>400.00 (-9.54%)</td><td>257.70 (+19.92%)</td><td>162.08 <b>(+26.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.10 (n/a)</td><td>410.48 (n/a)</td><td>442.20 (n/a)</td><td>214.90 (n/a)</td><td>127.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-15.71%)</td><td>0.02 (-3.91%)</td><td>0.02 (+8.53%)</td><td>0.02 <b>(+21.89%)</b></td><td>0.01 <b>(-39.68%)</b></td><td>493.70 (-17.95%)</td><td>421.48 (-4.94%)</td><td>476.70 (-7.87%)</td><td>269.10 (+18.65%)</td><td>95.87 <b>(-42.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.70 (n/a)</td><td>443.36 (n/a)</td><td>517.40 (n/a)</td><td>226.80 (n/a)</td><td>165.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 <b>(-33.02%)</b></td><td>0.04 <b>(-26.65%)</b></td><td>0.04 <b>(-20.48%)</b></td><td>0.03 <b>(-20.02%)</b></td><td>0.01 <b>(-47.93%)</b></td><td>616.60 <b>(+25.05%)</b></td><td>472.20 <b>(+32.57%)</b></td><td>465.00 <b>(+25.78%)</b></td><td>357.20 <b>(+49.33%)</b></td><td>94.66 (-1.03%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>493.10 (n/a)</td><td>356.18 (n/a)</td><td>369.70 (n/a)</td><td>239.20 (n/a)</td><td>95.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 <b>(+24.09%)</b></td><td>0.06 (+8.10%)</td><td>0.06 (+1.60%)</td><td>0.03 (-14.01%)</td><td>0.02 <b>(+52.00%)</b></td><td>492.90 (+16.30%)</td><td>322.92 (-3.13%)</td><td>291.50 (-1.59%)</td><td>203.00 (-19.41%)</td><td>113.22 <b>(+38.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>423.80 (n/a)</td><td>333.34 (n/a)</td><td>296.20 (n/a)</td><td>251.90 (n/a)</td><td>81.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (-19.20%)</td><td>0.05 (-19.60%)</td><td>0.06 (-7.82%)</td><td>0.03 <b>(-49.30%)</b></td><td>0.01 <b>(+55.88%)</b></td><td>588.60 <b>(+97.25%)</b></td><td>341.42 <b>(+34.07%)</b></td><td>280.20 (+8.48%)</td><td>270.60 <b>(+23.79%)</b></td><td>138.60 <b>(+297.21%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>298.40 (n/a)</td><td>254.66 (n/a)</td><td>258.30 (n/a)</td><td>218.60 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (+3.46%)</td><td>0.06 (-6.04%)</td><td>0.06 (+2.04%)</td><td>0.03 <b>(-36.58%)</b></td><td>0.02 <b>(+64.50%)</b></td><td>623.90 <b>(+57.67%)</b></td><td>338.36 (+17.58%)</td><td>267.10 (-1.98%)</td><td>218.40 (-3.36%)</td><td>164.15 <b>(+156.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>395.70 (n/a)</td><td>287.76 (n/a)</td><td>272.50 (n/a)</td><td>226.00 (n/a)</td><td>63.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-5.43%)</td><td>0.05 (+1.81%)</td><td>0.05 (-2.79%)</td><td>0.04 (+4.43%)</td><td>0.01 (-8.72%)</td><td>452.20 (-4.24%)</td><td>328.02 (-2.91%)</td><td>303.40 (+2.88%)</td><td>227.70 (+5.71%)</td><td>94.47 (-8.64%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>472.20 (n/a)</td><td>337.86 (n/a)</td><td>294.90 (n/a)</td><td>215.40 (n/a)</td><td>103.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (+12.89%)</td><td>0.06 (-9.11%)</td><td>0.05 <b>(-26.86%)</b></td><td>0.04 (+14.71%)</td><td>0.02 (+14.42%)</td><td>405.60 (-12.83%)</td><td>315.56 (+9.49%)</td><td>349.70 <b>(+36.71%)</b></td><td>198.10 (-11.40%)</td><td>82.00 (-17.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>465.30 (n/a)</td><td>288.20 (n/a)</td><td>255.80 (n/a)</td><td>223.60 (n/a)</td><td>99.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-1.32%)</td><td>0.05 (+3.25%)</td><td>0.06 (+2.94%)</td><td>0.03 (+7.71%)</td><td>0.02 (+1.25%)</td><td>487.50 (-7.14%)</td><td>354.80 (-3.20%)</td><td>291.70 (-2.83%)</td><td>242.60 (+1.34%)</td><td>120.58 (-2.90%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.00 (n/a)</td><td>366.54 (n/a)</td><td>300.20 (n/a)</td><td>239.40 (n/a)</td><td>124.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+4.01%)</td><td>0.05 <b>(+30.48%)</b></td><td>0.05 <b>(+39.42%)</b></td><td>0.03 <b>(+51.77%)</b></td><td>0.02 (+1.35%)</td><td>572.00 <b>(-34.11%)</b></td><td>367.36 <b>(-27.01%)</b></td><td>335.20 <b>(-28.27%)</b></td><td>250.00 (-3.85%)</td><td>135.93 <b>(-39.55%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>868.10 (n/a)</td><td>503.28 (n/a)</td><td>467.30 (n/a)</td><td>260.00 (n/a)</td><td>224.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+16.54%)</td><td>0.04 (+7.69%)</td><td>0.03 (+1.33%)</td><td>0.02 <b>(-44.07%)</b></td><td>0.02 <b>(+93.74%)</b></td><td>1053.20 <b>(+78.81%)</b></td><td>519.84 (+15.57%)</td><td>468.20 (-1.31%)</td><td>244.60 (-14.18%)</td><td>327.32 <b>(+196.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>589.00 (n/a)</td><td>449.82 (n/a)</td><td>474.40 (n/a)</td><td>285.00 (n/a)</td><td>110.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+15.49%)</td><td>0.05 (+15.23%)</td><td>0.05 <b>(+30.05%)</b></td><td>0.03 (+6.57%)</td><td>0.02 <b>(+31.67%)</b></td><td>477.60 (-6.15%)</td><td>345.18 (-11.10%)</td><td>306.40 <b>(-23.11%)</b></td><td>238.10 (-13.42%)</td><td>109.59 (+10.85%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>508.90 (n/a)</td><td>388.28 (n/a)</td><td>398.50 (n/a)</td><td>275.00 (n/a)</td><td>98.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+6.04%)</td><td>0.03 (-15.84%)</td><td>0.03 (-11.75%)</td><td>0.02 <b>(-42.81%)</b></td><td>0.02 <b>(+34.77%)</b></td><td>1032.50 <b>(+74.85%)</b></td><td>563.76 <b>(+33.26%)</b></td><td>514.20 (+13.31%)</td><td>273.30 (-5.69%)</td><td>283.72 <b>(+134.48%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.50 (n/a)</td><td>423.06 (n/a)</td><td>453.80 (n/a)</td><td>289.80 (n/a)</td><td>121.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+17.64%)</td><td>0.04 (+8.61%)</td><td>0.03 (+4.44%)</td><td>0.02 (-18.73%)</td><td>0.02 <b>(+41.44%)</b></td><td>762.80 <b>(+23.05%)</b></td><td>514.40 (-0.81%)</td><td>546.70 (-4.26%)</td><td>245.10 (-14.98%)</td><td>198.20 <b>(+50.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>619.90 (n/a)</td><td>518.62 (n/a)</td><td>571.00 (n/a)</td><td>288.30 (n/a)</td><td>131.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (-11.51%)</td><td>0.12 (+6.19%)</td><td>0.13 <b>(+21.65%)</b></td><td>0.06 <b>(-26.67%)</b></td><td>0.03 (+18.04%)</td><td>516.50 <b>(+36.35%)</b></td><td>308.36 (-1.66%)</td><td>261.90 (-17.80%)</td><td>248.70 (+12.99%)</td><td>116.58 <b>(+89.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>378.80 (n/a)</td><td>313.56 (n/a)</td><td>318.60 (n/a)</td><td>220.10 (n/a)</td><td>61.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (+0.21%)</td><td>0.10 <b>(-22.31%)</b></td><td>0.07 <b>(-39.96%)</b></td><td>0.06 <b>(-43.69%)</b></td><td>0.04 <b>(+179.32%)</b></td><td>530.80 <b>(+77.58%)</b></td><td>388.88 <b>(+44.37%)</b></td><td>463.60 <b>(+66.52%)</b></td><td>224.80 (-0.22%)</td><td>139.73 <b>(+391.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>298.90 (n/a)</td><td>269.36 (n/a)</td><td>278.40 (n/a)</td><td>225.30 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 <b>(-21.05%)</b></td><td>0.07 (-16.67%)</td><td>0.07 (-11.69%)</td><td>0.06 (-4.80%)</td><td>0.01 <b>(-48.81%)</b></td><td>595.50 (+5.04%)</td><td>480.22 (+13.02%)</td><td>470.60 (+13.23%)</td><td>350.20 <b>(+26.65%)</b></td><td>91.09 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.90 (n/a)</td><td>424.88 (n/a)</td><td>415.60 (n/a)</td><td>276.50 (n/a)</td><td>139.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (-11.64%)</td><td>0.08 <b>(-21.17%)</b></td><td>0.10 (-10.49%)</td><td>0.02 <b>(-73.78%)</b></td><td>0.05 <b>(+30.17%)</b></td><td>1925.60 <b>(+281.46%)</b></td><td>667.04 <b>(+97.38%)</b></td><td>324.70 (+11.73%)</td><td>246.60 (+13.17%)</td><td>712.01 <b>(+496.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>504.80 (n/a)</td><td>337.94 (n/a)</td><td>290.60 (n/a)</td><td>217.90 (n/a)</td><td>119.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 <b>(+107.82%)</b></td><td>0.09 <b>(+60.09%)</b></td><td>0.07 (+17.89%)</td><td>0.06 <b>(+101.03%)</b></td><td>0.04 <b>(+145.57%)</b></td><td>555.50 <b>(-50.26%)</b></td><td>408.30 <b>(-35.28%)</b></td><td>444.10 (-15.18%)</td><td>225.30 <b>(-51.88%)</b></td><td>154.31 <b>(-43.40%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1116.70 (n/a)</td><td>630.84 (n/a)</td><td>523.60 (n/a)</td><td>468.20 (n/a)</td><td>272.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-15.31%)</td><td>0.08 (-17.38%)</td><td>0.06 (-5.80%)</td><td>0.05 (-4.03%)</td><td>0.03 <b>(-24.70%)</b></td><td>602.60 (+4.18%)</td><td>480.42 (+14.31%)</td><td>536.40 (+6.15%)</td><td>237.20 (+18.07%)</td><td>142.29 (-15.19%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>578.40 (n/a)</td><td>420.28 (n/a)</td><td>505.30 (n/a)</td><td>200.90 (n/a)</td><td>167.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 <b>(+77.87%)</b></td><td>0.08 (+2.24%)</td><td>0.05 <b>(-37.03%)</b></td><td>0.05 (-11.09%)</td><td>0.06 <b>(+197.99%)</b></td><td>645.60 (+12.47%)</td><td>524.20 <b>(+20.14%)</b></td><td>623.20 <b>(+58.82%)</b></td><td>171.70 <b>(-43.78%)</b></td><td>200.03 <b>(+75.35%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>574.00 (n/a)</td><td>436.34 (n/a)</td><td>392.40 (n/a)</td><td>305.40 (n/a)</td><td>114.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 <b>(+30.54%)</b></td><td>0.10 <b>(+43.59%)</b></td><td>0.11 <b>(+74.95%)</b></td><td>0.07 (+6.90%)</td><td>0.02 <b>(+49.88%)</b></td><td>496.70 (-6.46%)</td><td>328.74 <b>(-28.96%)</b></td><td>294.00 <b>(-42.85%)</b></td><td>262.40 <b>(-23.39%)</b></td><td>95.04 (+11.23%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>531.00 (n/a)</td><td>462.74 (n/a)</td><td>514.40 (n/a)</td><td>342.50 (n/a)</td><td>85.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 <b>(-22.16%)</b></td><td>0.09 (-14.25%)</td><td>0.08 <b>(-20.95%)</b></td><td>0.06 (+17.92%)</td><td>0.02 <b>(-51.62%)</b></td><td>528.20 (-15.19%)</td><td>391.32 (+2.24%)</td><td>396.40 <b>(+26.48%)</b></td><td>283.00 <b>(+28.46%)</b></td><td>98.42 <b>(-46.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>622.80 (n/a)</td><td>382.76 (n/a)</td><td>313.40 (n/a)</td><td>220.30 (n/a)</td><td>184.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (-15.24%)</td><td>0.06 <b>(-37.49%)</b></td><td>0.06 <b>(-52.36%)</b></td><td>0.01 <b>(-77.44%)</b></td><td>0.04 (+9.73%)</td><td>2478.70 <b>(+343.18%)</b></td><td>874.18 <b>(+143.78%)</b></td><td>580.90 <b>(+109.94%)</b></td><td>265.20 (+17.97%)</td><td>906.68 <b>(+535.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>559.30 (n/a)</td><td>358.60 (n/a)</td><td>276.70 (n/a)</td><td>224.80 (n/a)</td><td>142.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (+18.18%)</td><td>0.10 (+12.94%)</td><td>0.10 <b>(+40.44%)</b></td><td>0.05 (-10.41%)</td><td>0.03 <b>(+37.03%)</b></td><td>600.60 (+11.64%)</td><td>380.68 (-7.39%)</td><td>321.30 <b>(-28.79%)</b></td><td>236.70 (-15.37%)</td><td>143.64 <b>(+35.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>538.00 (n/a)</td><td>411.04 (n/a)</td><td>451.20 (n/a)</td><td>279.70 (n/a)</td><td>106.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 <b>(+51.04%)</b></td><td>0.09 <b>(+25.50%)</b></td><td>0.07 (-4.27%)</td><td>0.05 (+5.61%)</td><td>0.04 <b>(+118.59%)</b></td><td>605.70 (-5.31%)</td><td>420.82 (-12.38%)</td><td>484.60 (+4.46%)</td><td>213.50 <b>(-33.78%)</b></td><td>160.91 <b>(+36.69%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>639.70 (n/a)</td><td>480.30 (n/a)</td><td>463.90 (n/a)</td><td>322.40 (n/a)</td><td>117.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 <b>(+28.32%)</b></td><td>0.09 (-1.66%)</td><td>0.09 (-0.76%)</td><td>0.05 <b>(-40.45%)</b></td><td>0.02 <b>(+543.63%)</b></td><td>500.00 <b>(+67.95%)</b></td><td>309.82 (+10.26%)</td><td>283.10 (+0.78%)</td><td>209.00 <b>(-22.07%)</b></td><td>111.34 <b>(+800.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>297.70 (n/a)</td><td>281.00 (n/a)</td><td>280.90 (n/a)</td><td>268.20 (n/a)</td><td>12.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (-6.57%)</td><td>0.13 (-13.92%)</td><td>0.12 (-19.56%)</td><td>0.09 (+0.14%)</td><td>0.03 (-5.62%)</td><td>547.30 (-0.15%)</td><td>409.02 (+15.50%)</td><td>403.50 <b>(+24.35%)</b></td><td>303.20 (+7.02%)</td><td>105.25 (-4.72%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>548.10 (n/a)</td><td>354.14 (n/a)</td><td>324.50 (n/a)</td><td>283.30 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.86 (-5.44%)</td><td>3.21 (-8.12%)</td><td>3.22 (-13.07%)</td><td>2.55 (-4.66%)</td><td>0.46 <b>(-25.73%)</b></td><td>4104.10 (+4.89%)</td><td>3321.36 (+7.73%)</td><td>3253.70 (+15.04%)</td><td>2719.60 (+5.76%)</td><td>496.97 (-15.59%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.08 (n/a)</td><td>3.50 (n/a)</td><td>3.71 (n/a)</td><td>2.68 (n/a)</td><td>0.62 (n/a)</td><td>3912.70 (n/a)</td><td>3083.00 (n/a)</td><td>2828.40 (n/a)</td><td>2571.60 (n/a)</td><td>588.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (-14.20%)</td><td>0.13 (+4.21%)</td><td>0.13 (-8.89%)</td><td>0.10 <b>(+48.35%)</b></td><td>0.02 <b>(-60.85%)</b></td><td>397.00 <b>(-32.59%)</b></td><td>320.68 (-13.99%)</td><td>314.50 (+9.73%)</td><td>272.30 (+16.57%)</td><td>47.39 <b>(-69.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>588.90 (n/a)</td><td>372.82 (n/a)</td><td>286.60 (n/a)</td><td>233.60 (n/a)</td><td>154.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+0.03%)</td><td>0.02 (+16.07%)</td><td>0.02 (+9.41%)</td><td>0.02 <b>(+41.00%)</b></td><td>0.00 <b>(-54.52%)</b></td><td>294.70 <b>(-29.07%)</b></td><td>265.56 (-16.39%)</td><td>269.70 (-8.61%)</td><td>237.60 (-0.04%)</td><td>21.51 <b>(-68.13%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>415.50 (n/a)</td><td>317.62 (n/a)</td><td>295.10 (n/a)</td><td>237.70 (n/a)</td><td>67.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(+31.95%)</b></td><td>0.01 (+13.66%)</td><td>0.01 (-11.67%)</td><td>0.01 (+10.47%)</td><td>0.00 <b>(+45.90%)</b></td><td>620.80 (-9.48%)</td><td>464.26 (-10.34%)</td><td>512.60 (+13.21%)</td><td>284.30 <b>(-24.21%)</b></td><td>130.45 (-5.71%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>685.80 (n/a)</td><td>517.80 (n/a)</td><td>452.80 (n/a)</td><td>375.10 (n/a)</td><td>138.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+2.75%)</td><td>0.02 (-15.21%)</td><td>0.01 (-8.88%)</td><td>0.01 (-12.65%)</td><td>0.01 (-6.38%)</td><td>589.70 (+14.48%)</td><td>445.44 (+16.61%)</td><td>465.30 (+9.74%)</td><td>225.90 (-2.67%)</td><td>133.81 (-1.95%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>381.98 (n/a)</td><td>424.00 (n/a)</td><td>232.10 (n/a)</td><td>136.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 (+12.85%)</td><td>0.01 <b>(+21.17%)</b></td><td>0.01 (+5.25%)</td><td>0.01 <b>(+77.90%)</b></td><td>0.00 (+8.38%)</td><td>628.60 <b>(-43.78%)</b></td><td>469.18 <b>(-22.24%)</b></td><td>489.80 (-4.99%)</td><td>273.40 (-11.41%)</td><td>161.31 <b>(-46.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1118.20 (n/a)</td><td>603.34 (n/a)</td><td>515.50 (n/a)</td><td>308.60 (n/a)</td><td>304.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-33.14%)</b></td><td>0.01 <b>(-31.98%)</b></td><td>0.01 <b>(-36.34%)</b></td><td>0.01 (-8.15%)</td><td>0.00 <b>(-62.47%)</b></td><td>545.80 (+8.88%)</td><td>464.46 <b>(+37.35%)</b></td><td>460.40 <b>(+57.08%)</b></td><td>356.30 <b>(+49.58%)</b></td><td>73.96 <b>(-37.07%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>501.30 (n/a)</td><td>338.16 (n/a)</td><td>293.10 (n/a)</td><td>238.20 (n/a)</td><td>117.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-7.22%)</td><td>0.01 (-0.55%)</td><td>0.01 (+18.69%)</td><td>0.01 (+4.13%)</td><td>0.00 <b>(-28.62%)</b></td><td>507.60 (-3.95%)</td><td>380.88 (-5.15%)</td><td>396.60 (-15.74%)</td><td>248.50 (+7.81%)</td><td>102.32 <b>(-28.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.50 (n/a)</td><td>401.54 (n/a)</td><td>470.70 (n/a)</td><td>230.50 (n/a)</td><td>142.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-11.71%)</td><td>0.01 (-12.20%)</td><td>0.01 <b>(-31.76%)</b></td><td>0.01 (-2.65%)</td><td>0.00 (-14.19%)</td><td>620.80 (+2.71%)</td><td>421.82 (+11.28%)</td><td>456.50 <b>(+46.55%)</b></td><td>271.40 (+13.27%)</td><td>146.54 (-6.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>379.06 (n/a)</td><td>311.50 (n/a)</td><td>239.60 (n/a)</td><td>156.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-7.97%)</td><td>0.01 (-3.01%)</td><td>0.01 (+0.71%)</td><td>0.01 (+13.14%)</td><td>0.00 (-16.40%)</td><td>583.80 (-11.61%)</td><td>460.52 (-0.17%)</td><td>473.80 (-0.71%)</td><td>259.60 (+8.66%)</td><td>122.44 (-19.01%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>660.50 (n/a)</td><td>461.30 (n/a)</td><td>477.20 (n/a)</td><td>238.90 (n/a)</td><td>151.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+7.81%)</td><td>0.01 (-9.02%)</td><td>0.01 (-9.97%)</td><td>0.01 <b>(-33.00%)</b></td><td>0.01 <b>(+40.04%)</b></td><td>758.20 <b>(+49.25%)</b></td><td>475.86 (+20.00%)</td><td>457.20 (+11.05%)</td><td>229.20 (-7.24%)</td><td>192.07 <b>(+90.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.00 (n/a)</td><td>396.56 (n/a)</td><td>411.70 (n/a)</td><td>247.10 (n/a)</td><td>100.59 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(-29.32%)</b></td><td>0.01 (-16.84%)</td><td>0.01 (-10.04%)</td><td>0.01 <b>(-22.54%)</b></td><td>0.01 <b>(-35.01%)</b></td><td>687.10 <b>(+29.11%)</b></td><td>473.30 (+15.62%)</td><td>498.30 (+11.15%)</td><td>215.40 <b>(+41.43%)</b></td><td>189.09 <b>(+26.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>532.20 (n/a)</td><td>409.36 (n/a)</td><td>448.30 (n/a)</td><td>152.30 (n/a)</td><td>148.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-7.69%)</td><td>0.01 <b>(+20.49%)</b></td><td>0.02 <b>(+90.51%)</b></td><td>0.01 (-2.61%)</td><td>0.00 <b>(-24.45%)</b></td><td>643.60 (+2.68%)</td><td>363.14 <b>(-21.79%)</b></td><td>289.50 <b>(-47.51%)</b></td><td>247.00 (+8.33%)</td><td>161.29 (-14.79%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.80 (n/a)</td><td>464.34 (n/a)</td><td>551.50 (n/a)</td><td>228.00 (n/a)</td><td>189.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-29.67%)</b></td><td>0.01 (-12.56%)</td><td>0.01 (-7.42%)</td><td>0.01 (-8.41%)</td><td>0.00 <b>(-50.89%)</b></td><td>676.20 (+9.19%)</td><td>539.20 (+8.53%)</td><td>557.80 (+8.02%)</td><td>389.30 <b>(+42.18%)</b></td><td>105.99 <b>(-22.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.30 (n/a)</td><td>496.80 (n/a)</td><td>516.40 (n/a)</td><td>273.80 (n/a)</td><td>136.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (+5.37%)</td><td>0.02 (+14.58%)</td><td>0.02 (+9.41%)</td><td>0.01 <b>(+151.65%)</b></td><td>0.01 (-19.51%)</td><td>752.40 <b>(-60.26%)</b></td><td>473.32 <b>(-35.80%)</b></td><td>456.40 (-8.59%)</td><td>254.30 (-5.11%)</td><td>178.36 <b>(-72.96%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1893.40 (n/a)</td><td>737.28 (n/a)</td><td>499.30 (n/a)</td><td>268.00 (n/a)</td><td>659.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(+21.22%)</b></td><td>0.04 (-0.94%)</td><td>0.04 (+8.42%)</td><td>0.02 (-13.28%)</td><td>0.02 <b>(+69.76%)</b></td><td>557.70 (+15.32%)</td><td>357.08 (+12.65%)</td><td>280.50 (-7.76%)</td><td>191.50 (-17.53%)</td><td>167.14 <b>(+68.40%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>483.60 (n/a)</td><td>316.98 (n/a)</td><td>304.10 (n/a)</td><td>232.20 (n/a)</td><td>99.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (-1.39%)</td><td>0.03 (+13.69%)</td><td>0.03 (+1.04%)</td><td>0.02 <b>(+319.95%)</b></td><td>0.01 <b>(-38.56%)</b></td><td>447.90 <b>(-76.19%)</b></td><td>314.50 <b>(-48.51%)</b></td><td>297.20 (-1.03%)</td><td>218.20 (+1.39%)</td><td>95.97 <b>(-86.56%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1881.00 (n/a)</td><td>610.84 (n/a)</td><td>300.30 (n/a)</td><td>215.20 (n/a)</td><td>714.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (+2.88%)</td><td>0.02 <b>(-25.10%)</b></td><td>0.02 <b>(-28.50%)</b></td><td>0.00 <b>(-50.63%)</b></td><td>0.01 (+11.55%)</td><td>2068.70 <b>(+102.54%)</b></td><td>848.42 <b>(+68.02%)</b></td><td>674.20 <b>(+39.85%)</b></td><td>234.80 (-2.81%)</td><td>712.26 <b>(+129.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1021.40 (n/a)</td><td>504.96 (n/a)</td><td>482.10 (n/a)</td><td>241.60 (n/a)</td><td>310.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-1.82%)</td><td>0.02 (+14.79%)</td><td>0.02 (-7.06%)</td><td>0.02 <b>(+273.64%)</b></td><td>0.01 <b>(-24.80%)</b></td><td>520.30 <b>(-73.23%)</b></td><td>414.62 <b>(-40.92%)</b></td><td>492.20 (+7.58%)</td><td>245.00 (+1.83%)</td><td>131.41 <b>(-81.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1943.90 (n/a)</td><td>701.74 (n/a)</td><td>457.50 (n/a)</td><td>240.60 (n/a)</td><td>701.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 (-0.10%)</td><td>0.03 (-7.05%)</td><td>0.02 <b>(-38.43%)</b></td><td>0.02 (+10.07%)</td><td>0.01 (+0.42%)</td><td>599.00 (-9.15%)</td><td>407.64 (+5.40%)</td><td>453.60 <b>(+62.41%)</b></td><td>240.30 (+0.13%)</td><td>161.41 (-13.85%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>659.30 (n/a)</td><td>386.74 (n/a)</td><td>279.30 (n/a)</td><td>240.00 (n/a)</td><td>187.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-17.18%)</td><td>0.02 <b>(-23.43%)</b></td><td>0.02 <b>(-29.96%)</b></td><td>0.01 <b>(-24.12%)</b></td><td>0.01 (-17.64%)</td><td>720.60 <b>(+31.78%)</b></td><td>489.20 <b>(+30.45%)</b></td><td>474.50 <b>(+42.79%)</b></td><td>272.90 <b>(+20.75%)</b></td><td>161.21 <b>(+23.24%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.80 (n/a)</td><td>375.00 (n/a)</td><td>332.30 (n/a)</td><td>226.00 (n/a)</td><td>130.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.04 <b>(+27.10%)</b></td><td>0.03 <b>(+25.96%)</b></td><td>0.02 (+17.81%)</td><td>0.01 (-16.22%)</td><td>0.01 <b>(+89.19%)</b></td><td>621.10 (+19.35%)</td><td>387.04 (-10.53%)</td><td>382.00 (-15.13%)</td><td>208.70 <b>(-21.33%)</b></td><td>176.16 <b>(+74.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>432.58 (n/a)</td><td>450.10 (n/a)</td><td>265.30 (n/a)</td><td>100.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 (-4.85%)</td><td>0.02 (+6.69%)</td><td>0.02 (+7.97%)</td><td>0.01 <b>(+68.56%)</b></td><td>0.01 <b>(-25.73%)</b></td><td>609.40 <b>(-40.67%)</b></td><td>479.10 (-16.47%)</td><td>490.20 (-7.39%)</td><td>281.30 (+5.08%)</td><td>121.55 <b>(-56.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1027.20 (n/a)</td><td>573.58 (n/a)</td><td>529.30 (n/a)</td><td>267.70 (n/a)</td><td>280.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.03 <b>(+30.75%)</b></td><td>0.02 <b>(+23.17%)</b></td><td>0.02 (+15.29%)</td><td>0.02 (+15.26%)</td><td>0.01 <b>(+54.71%)</b></td><td>566.90 (-13.24%)</td><td>430.68 (-17.44%)</td><td>452.40 (-13.27%)</td><td>295.70 <b>(-23.53%)</b></td><td>100.88 (+1.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.40 (n/a)</td><td>521.64 (n/a)</td><td>521.60 (n/a)</td><td>386.70 (n/a)</td><td>98.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(-59.30%)</b></td><td>0.01 <b>(-44.38%)</b></td><td>0.02 (-9.31%)</td><td>0.00 <b>(-71.61%)</b></td><td>0.01 <b>(-48.46%)</b></td><td>2422.30 <b>(+252.18%)</b></td><td>1105.72 <b>(+124.52%)</b></td><td>531.90 (+10.28%)</td><td>473.00 <b>(+145.71%)</b></td><td>867.18 <b>(+348.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.80 (n/a)</td><td>492.48 (n/a)</td><td>482.30 (n/a)</td><td>192.50 (n/a)</td><td>193.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+9.84%)</td><td>0.05 <b>(+42.82%)</b></td><td>0.05 <b>(+60.71%)</b></td><td>0.04 <b>(+32.74%)</b></td><td>0.01 (-15.49%)</td><td>460.60 <b>(-24.66%)</b></td><td>325.00 <b>(-32.25%)</b></td><td>310.60 <b>(-37.78%)</b></td><td>253.20 (-8.95%)</td><td>79.95 <b>(-36.09%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.40 (n/a)</td><td>479.72 (n/a)</td><td>499.20 (n/a)</td><td>278.10 (n/a)</td><td>125.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+2.00%)</td><td>0.08 (+8.38%)</td><td>0.09 (+15.11%)</td><td>0.05 (+4.41%)</td><td>0.02 (+9.51%)</td><td>501.10 (-4.22%)</td><td>341.52 (-7.08%)</td><td>266.40 (-13.14%)</td><td>245.50 (-1.96%)</td><td>116.77 (-0.73%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.20 (n/a)</td><td>367.54 (n/a)</td><td>306.70 (n/a)</td><td>250.40 (n/a)</td><td>117.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (+6.57%)</td><td>0.05 (+7.41%)</td><td>0.07 (+12.40%)</td><td>0.01 (-4.06%)</td><td>0.03 (+13.99%)</td><td>1992.70 (+4.23%)</td><td>627.44 (+1.34%)</td><td>245.40 (-11.05%)</td><td>192.70 (-6.14%)</td><td>771.05 (+5.98%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1911.80 (n/a)</td><td>619.14 (n/a)</td><td>275.90 (n/a)</td><td>205.30 (n/a)</td><td>727.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 <b>(+26.07%)</b></td><td>0.07 <b>(+54.45%)</b></td><td>0.08 <b>(+116.67%)</b></td><td>0.05 <b>(+37.87%)</b></td><td>0.02 (-11.03%)</td><td>433.80 <b>(-27.47%)</b></td><td>289.80 <b>(-38.97%)</b></td><td>268.70 <b>(-53.85%)</b></td><td>230.50 <b>(-20.68%)</b></td><td>83.20 <b>(-48.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.10 (n/a)</td><td>474.84 (n/a)</td><td>582.20 (n/a)</td><td>290.60 (n/a)</td><td>161.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (+16.19%)</td><td>0.05 (+5.71%)</td><td>0.05 <b>(+27.71%)</b></td><td>0.01 <b>(-70.92%)</b></td><td>0.03 <b>(+58.08%)</b></td><td>1944.70 <b>(+243.89%)</b></td><td>638.28 <b>(+57.32%)</b></td><td>356.20 <b>(-21.70%)</b></td><td>202.50 (-13.94%)</td><td>736.28 <b>(+423.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>565.50 (n/a)</td><td>405.72 (n/a)</td><td>454.90 (n/a)</td><td>235.30 (n/a)</td><td>140.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (+16.55%)</td><td>0.06 <b>(+37.46%)</b></td><td>0.07 <b>(+72.65%)</b></td><td>0.04 <b>(+209.26%)</b></td><td>0.02 (-5.47%)</td><td>577.10 <b>(-67.67%)</b></td><td>369.30 <b>(-45.96%)</b></td><td>284.80 <b>(-42.07%)</b></td><td>239.30 (-14.20%)</td><td>158.10 <b>(-74.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1784.80 (n/a)</td><td>683.32 (n/a)</td><td>491.60 (n/a)</td><td>278.90 (n/a)</td><td>627.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (+8.56%)</td><td>0.05 (+5.29%)</td><td>0.04 (+3.45%)</td><td>0.03 (+4.92%)</td><td>0.02 (+12.81%)</td><td>508.50 (-4.70%)</td><td>398.52 (-3.82%)</td><td>461.40 (-3.35%)</td><td>251.90 (-7.86%)</td><td>130.48 (+1.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.60 (n/a)</td><td>414.36 (n/a)</td><td>477.40 (n/a)</td><td>273.40 (n/a)</td><td>127.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+9.07%)</td><td>0.05 (+16.88%)</td><td>0.05 <b>(+48.09%)</b></td><td>0.04 (+3.48%)</td><td>0.01 (+15.49%)</td><td>515.80 (-3.35%)</td><td>394.68 (-13.77%)</td><td>352.60 <b>(-32.48%)</b></td><td>290.60 (-8.33%)</td><td>101.69 (+2.71%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>457.72 (n/a)</td><td>522.20 (n/a)</td><td>317.00 (n/a)</td><td>99.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(+54.44%)</b></td><td>0.04 <b>(+31.81%)</b></td><td>0.06 <b>(+64.32%)</b></td><td>0.01 <b>(-71.98%)</b></td><td>0.02 <b>(+542.29%)</b></td><td>1952.00 <b>(+256.92%)</b></td><td>636.36 <b>(+31.26%)</b></td><td>295.80 <b>(-39.14%)</b></td><td>271.90 <b>(-35.26%)</b></td><td>736.39 <b>(+1500.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>546.90 (n/a)</td><td>484.82 (n/a)</td><td>486.00 (n/a)</td><td>420.00 (n/a)</td><td>46.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-3.03%)</td><td>0.04 (-18.78%)</td><td>0.04 <b>(-27.53%)</b></td><td>0.03 (-15.90%)</td><td>0.02 (-5.39%)</td><td>614.80 (+18.92%)</td><td>454.68 <b>(+23.18%)</b></td><td>461.30 <b>(+37.99%)</b></td><td>264.30 (+3.12%)</td><td>125.96 (+8.90%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>517.00 (n/a)</td><td>369.12 (n/a)</td><td>334.30 (n/a)</td><td>256.30 (n/a)</td><td>115.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.05 (+2.21%)</td><td>0.04 (+8.72%)</td><td>0.04 (+10.73%)</td><td>0.03 (+9.49%)</td><td>0.01 (+1.51%)</td><td>610.80 (-8.66%)</td><td>471.50 (-8.20%)</td><td>452.20 (-9.69%)</td><td>338.70 (-2.17%)</td><td>113.00 (-6.60%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>668.70 (n/a)</td><td>513.60 (n/a)</td><td>500.70 (n/a)</td><td>346.20 (n/a)</td><td>120.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (-18.39%)</td><td>0.10 <b>(+34.30%)</b></td><td>0.11 <b>(+76.54%)</b></td><td>0.07 <b>(+132.09%)</b></td><td>0.02 <b>(-48.86%)</b></td><td>463.80 <b>(-56.91%)</b></td><td>345.38 <b>(-38.79%)</b></td><td>293.80 <b>(-43.36%)</b></td><td>280.70 <b>(+22.58%)</b></td><td>82.92 <b>(-73.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1076.40 (n/a)</td><td>564.26 (n/a)</td><td>518.70 (n/a)</td><td>229.00 (n/a)</td><td>310.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 <b>(+30.42%)</b></td><td>0.08 (+0.41%)</td><td>0.06 (-15.12%)</td><td>0.05 <b>(-21.88%)</b></td><td>0.04 <b>(+90.59%)</b></td><td>666.00 <b>(+28.03%)</b></td><td>459.08 (+10.88%)</td><td>519.20 (+17.81%)</td><td>238.00 <b>(-23.32%)</b></td><td>181.52 <b>(+90.70%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>520.20 (n/a)</td><td>414.02 (n/a)</td><td>440.70 (n/a)</td><td>310.40 (n/a)</td><td>95.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (+8.26%)</td><td>0.11 (+12.53%)</td><td>0.10 (+11.64%)</td><td>0.07 (-0.44%)</td><td>0.04 <b>(+29.23%)</b></td><td>622.60 (+0.44%)</td><td>441.30 (-6.44%)</td><td>427.80 (-10.43%)</td><td>251.20 (-7.65%)</td><td>169.83 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>619.90 (n/a)</td><td>471.68 (n/a)</td><td>477.60 (n/a)</td><td>272.00 (n/a)</td><td>129.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 <b>(-23.87%)</b></td><td>0.06 <b>(-31.23%)</b></td><td>0.06 (-7.94%)</td><td>0.02 <b>(-67.21%)</b></td><td>0.04 (-15.01%)</td><td>1925.10 <b>(+204.94%)</b></td><td>789.92 <b>(+84.92%)</b></td><td>548.10 (+8.64%)</td><td>300.30 <b>(+31.36%)</b></td><td>659.51 <b>(+275.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>631.30 (n/a)</td><td>427.16 (n/a)</td><td>504.50 (n/a)</td><td>228.60 (n/a)</td><td>175.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.17 (+16.78%)</td><td>0.11 (+17.06%)</td><td>0.09 (+12.06%)</td><td>0.05 (-11.22%)</td><td>0.05 <b>(+48.01%)</b></td><td>778.00 (+12.62%)</td><td>445.12 (-7.24%)</td><td>435.10 (-10.77%)</td><td>245.40 (-14.38%)</td><td>210.26 <b>(+44.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>690.80 (n/a)</td><td>479.86 (n/a)</td><td>487.60 (n/a)</td><td>286.60 (n/a)</td><td>145.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 (+3.26%)</td><td>0.09 (+14.90%)</td><td>0.10 <b>(+39.98%)</b></td><td>0.06 (+15.23%)</td><td>0.02 (-1.04%)</td><td>509.90 (-13.22%)</td><td>374.82 (-13.81%)</td><td>339.40 <b>(-28.56%)</b></td><td>267.80 (-3.15%)</td><td>105.63 (-13.97%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.60 (n/a)</td><td>434.86 (n/a)</td><td>475.10 (n/a)</td><td>276.50 (n/a)</td><td>122.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+19.51%)</td><td>0.08 (+7.20%)</td><td>0.08 (-3.66%)</td><td>0.06 (-3.17%)</td><td>0.02 <b>(+54.82%)</b></td><td>637.70 (+3.27%)</td><td>471.60 (-4.85%)</td><td>477.70 (+3.80%)</td><td>351.10 (-16.33%)</td><td>107.22 <b>(+33.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>617.50 (n/a)</td><td>495.66 (n/a)</td><td>460.20 (n/a)</td><td>419.60 (n/a)</td><td>80.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-9.10%)</td><td>0.10 (+19.79%)</td><td>0.11 <b>(+96.54%)</b></td><td>0.07 <b>(+387.60%)</b></td><td>0.03 <b>(-46.04%)</b></td><td>503.10 <b>(-79.49%)</b></td><td>365.76 <b>(-56.39%)</b></td><td>299.90 <b>(-49.11%)</b></td><td>226.20 (+10.02%)</td><td>128.34 <b>(-86.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2453.00 (n/a)</td><td>838.72 (n/a)</td><td>589.30 (n/a)</td><td>205.60 (n/a)</td><td>928.45 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.12 <b>(-22.39%)</b></td><td>0.08 (-2.50%)</td><td>0.08 (+17.36%)</td><td>0.06 (+13.87%)</td><td>0.02 <b>(-42.59%)</b></td><td>587.30 (-12.17%)</td><td>480.18 (-5.01%)</td><td>474.80 (-14.79%)</td><td>303.60 <b>(+28.86%)</b></td><td>113.70 <b>(-29.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>668.70 (n/a)</td><td>505.50 (n/a)</td><td>557.20 (n/a)</td><td>235.60 (n/a)</td><td>161.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (-13.68%)</td><td>0.08 (-14.36%)</td><td>0.09 (-17.85%)</td><td>0.05 (-17.96%)</td><td>0.02 (-16.96%)</td><td>679.00 <b>(+21.88%)</b></td><td>441.90 (+16.52%)</td><td>384.20 <b>(+21.74%)</b></td><td>309.10 (+15.81%)</td><td>147.89 (+18.74%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>557.10 (n/a)</td><td>379.24 (n/a)</td><td>315.60 (n/a)</td><td>266.90 (n/a)</td><td>124.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (-2.79%)</td><td>0.05 (+1.05%)</td><td>0.05 (+17.31%)</td><td>0.03 (-6.56%)</td><td>0.02 (-2.51%)</td><td>654.30 (+7.02%)</td><td>431.62 (-0.47%)</td><td>412.40 (-14.78%)</td><td>237.70 (+2.86%)</td><td>173.35 (+8.52%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.40 (n/a)</td><td>433.64 (n/a)</td><td>483.90 (n/a)</td><td>231.10 (n/a)</td><td>159.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 <b>(-25.25%)</b></td><td>0.06 <b>(-24.55%)</b></td><td>0.07 (-8.59%)</td><td>0.03 (-13.65%)</td><td>0.02 <b>(-26.69%)</b></td><td>589.20 (+15.80%)</td><td>389.98 <b>(+30.58%)</b></td><td>310.00 (+9.42%)</td><td>265.80 <b>(+33.77%)</b></td><td>142.70 (+14.05%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>508.80 (n/a)</td><td>298.66 (n/a)</td><td>283.30 (n/a)</td><td>198.70 (n/a)</td><td>125.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 <b>(+32.51%)</b></td><td>0.05 (-6.08%)</td><td>0.04 <b>(-27.93%)</b></td><td>0.04 (+2.77%)</td><td>0.02 <b>(+77.34%)</b></td><td>557.40 (-2.69%)</td><td>476.28 (+13.58%)</td><td>532.80 <b>(+38.75%)</b></td><td>227.10 <b>(-24.53%)</b></td><td>139.99 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>572.80 (n/a)</td><td>419.32 (n/a)</td><td>384.00 (n/a)</td><td>300.90 (n/a)</td><td>112.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 (-11.53%)</td><td>0.05 <b>(-23.82%)</b></td><td>0.04 <b>(-37.21%)</b></td><td>0.03 <b>(-22.62%)</b></td><td>0.02 (-7.04%)</td><td>643.40 <b>(+29.25%)</b></td><td>471.36 <b>(+32.45%)</b></td><td>497.70 <b>(+59.26%)</b></td><td>233.70 (+13.06%)</td><td>149.31 (+17.48%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.80 (n/a)</td><td>355.88 (n/a)</td><td>312.50 (n/a)</td><td>206.70 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(-20.90%)</b></td><td>0.04 (-15.37%)</td><td>0.04 (-4.68%)</td><td>0.02 <b>(-44.61%)</b></td><td>0.01 (+3.86%)</td><td>1073.90 <b>(+80.52%)</b></td><td>589.12 <b>(+28.38%)</b></td><td>497.10 (+4.92%)</td><td>371.90 <b>(+26.41%)</b></td><td>282.14 <b>(+162.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>594.90 (n/a)</td><td>458.90 (n/a)</td><td>473.80 (n/a)</td><td>294.20 (n/a)</td><td>107.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+12.74%)</td><td>0.05 (+8.63%)</td><td>0.05 (-4.00%)</td><td>0.04 <b>(+34.14%)</b></td><td>0.01 (+1.61%)</td><td>471.50 <b>(-25.44%)</b></td><td>407.26 (-9.09%)</td><td>450.40 (+4.16%)</td><td>320.10 (-11.31%)</td><td>72.05 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>632.40 (n/a)</td><td>448.00 (n/a)</td><td>432.40 (n/a)</td><td>360.90 (n/a)</td><td>109.02 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 <b>(+57.66%)</b></td><td>0.08 <b>(+71.62%)</b></td><td>0.09 <b>(+90.68%)</b></td><td>0.04 <b>(+231.33%)</b></td><td>0.03 <b>(+33.53%)</b></td><td>615.10 <b>(-69.82%)</b></td><td>371.16 <b>(-53.57%)</b></td><td>271.30 <b>(-47.54%)</b></td><td>244.10 <b>(-36.58%)</b></td><td>161.30 <b>(-76.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2038.10 (n/a)</td><td>799.46 (n/a)</td><td>517.20 (n/a)</td><td>384.90 (n/a)</td><td>698.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (+19.23%)</td><td>0.07 (-8.18%)</td><td>0.06 <b>(-21.63%)</b></td><td>0.05 (-14.27%)</td><td>0.02 <b>(+57.72%)</b></td><td>518.30 (+16.66%)</td><td>405.14 (+13.01%)</td><td>419.60 <b>(+27.58%)</b></td><td>237.50 (-16.14%)</td><td>102.88 <b>(+40.10%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>444.30 (n/a)</td><td>358.50 (n/a)</td><td>328.90 (n/a)</td><td>283.20 (n/a)</td><td>73.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.11 (-1.99%)</td><td>0.07 (+2.67%)</td><td>0.06 (+0.84%)</td><td>0.05 (+13.55%)</td><td>0.03 (-2.17%)</td><td>541.60 (-11.92%)</td><td>398.34 (-4.03%)</td><td>444.90 (-0.82%)</td><td>221.40 (+2.03%)</td><td>153.26 (-9.49%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>614.90 (n/a)</td><td>415.08 (n/a)</td><td>448.60 (n/a)</td><td>217.00 (n/a)</td><td>169.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.10 (-13.42%)</td><td>0.07 (+1.11%)</td><td>0.08 <b>(+35.23%)</b></td><td>0.04 (-0.39%)</td><td>0.03 (-12.18%)</td><td>588.40 (+0.39%)</td><td>384.62 (-2.20%)</td><td>298.60 <b>(-26.07%)</b></td><td>234.30 (+15.53%)</td><td>175.67 (+4.07%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>586.10 (n/a)</td><td>393.28 (n/a)</td><td>403.90 (n/a)</td><td>202.80 (n/a)</td><td>168.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.09 <b>(-28.22%)</b></td><td>0.07 (+5.05%)</td><td>0.07 <b>(+44.63%)</b></td><td>0.05 <b>(+272.64%)</b></td><td>0.02 <b>(-57.67%)</b></td><td>522.90 <b>(-73.16%)</b></td><td>380.48 <b>(-45.04%)</b></td><td>332.50 <b>(-30.86%)</b></td><td>276.70 <b>(+39.33%)</b></td><td>113.02 <b>(-84.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>1948.40 (n/a)</td><td>692.30 (n/a)</td><td>480.90 (n/a)</td><td>198.60 (n/a)</td><td>720.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 (-14.95%)</td><td>0.06 (-1.00%)</td><td>0.05 (-0.77%)</td><td>0.04 (+3.49%)</td><td>0.01 <b>(-35.45%)</b></td><td>597.80 (-3.38%)</td><td>452.70 (-4.04%)</td><td>458.50 (+0.79%)</td><td>314.60 (+17.61%)</td><td>104.27 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>618.70 (n/a)</td><td>471.78 (n/a)</td><td>454.90 (n/a)</td><td>267.50 (n/a)</td><td>149.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-3.15%)</td><td>0.05 (-14.16%)</td><td>0.06 (-10.47%)</td><td>0.04 (-4.29%)</td><td>0.01 (+9.67%)</td><td>492.80 (+4.47%)</td><td>367.64 (+18.23%)</td><td>303.60 (+11.70%)</td><td>274.10 (+3.24%)</td><td>107.44 (+19.45%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.70 (n/a)</td><td>310.96 (n/a)</td><td>271.80 (n/a)</td><td>265.50 (n/a)</td><td>89.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-12.24%)</td><td>0.05 (+9.20%)</td><td>0.04 (-1.80%)</td><td>0.03 (+4.95%)</td><td>0.02 (-6.95%)</td><td>533.40 (-4.72%)</td><td>401.52 (-8.75%)</td><td>458.20 (+1.84%)</td><td>263.90 (+13.95%)</td><td>127.80 (+1.78%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.80 (n/a)</td><td>440.02 (n/a)</td><td>449.90 (n/a)</td><td>231.60 (n/a)</td><td>125.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-19.53%)</td><td>0.04 <b>(-32.50%)</b></td><td>0.04 <b>(-37.10%)</b></td><td>0.03 <b>(-37.29%)</b></td><td>0.01 (-4.63%)</td><td>676.20 <b>(+59.48%)</b></td><td>456.18 <b>(+53.59%)</b></td><td>472.00 <b>(+58.98%)</b></td><td>281.60 <b>(+24.27%)</b></td><td>148.43 <b>(+88.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>424.00 (n/a)</td><td>297.02 (n/a)</td><td>296.90 (n/a)</td><td>226.60 (n/a)</td><td>78.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 <b>(+20.68%)</b></td><td>0.03 (-16.14%)</td><td>0.03 (-10.18%)</td><td>0.01 <b>(-67.72%)</b></td><td>0.02 <b>(+142.51%)</b></td><td>1830.10 <b>(+209.82%)</b></td><td>847.70 <b>(+70.19%)</b></td><td>581.10 (+11.32%)</td><td>294.80 (-17.14%)</td><td>617.46 <b>(+543.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.70 (n/a)</td><td>498.10 (n/a)</td><td>522.00 (n/a)</td><td>355.80 (n/a)</td><td>95.99 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-2.10%)</td><td>0.05 (+19.93%)</td><td>0.05 <b>(+21.33%)</b></td><td>0.04 <b>(+40.71%)</b></td><td>0.01 <b>(-28.69%)</b></td><td>436.50 <b>(-28.93%)</b></td><td>350.32 <b>(-20.08%)</b></td><td>362.10 (-17.57%)</td><td>280.50 (+2.15%)</td><td>64.18 <b>(-48.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>438.32 (n/a)</td><td>439.30 (n/a)</td><td>274.60 (n/a)</td><td>124.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.07 (-10.01%)</td><td>0.05 (-6.64%)</td><td>0.04 (-7.45%)</td><td>0.03 (-6.89%)</td><td>0.02 (-2.41%)</td><td>573.80 (+7.41%)</td><td>430.94 (+8.20%)</td><td>442.80 (+8.05%)</td><td>282.40 (+11.14%)</td><td>141.07 (+14.88%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>534.20 (n/a)</td><td>398.28 (n/a)</td><td>409.80 (n/a)</td><td>254.10 (n/a)</td><td>122.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.39 (+0.18%)</td><td>0.34 <b>(+22.11%)</b></td><td>0.34 (+19.66%)</td><td>0.31 <b>(+69.41%)</b></td><td>0.03 <b>(-60.95%)</b></td><td>316.30 <b>(-40.97%)</b></td><td>292.44 <b>(-23.05%)</b></td><td>292.10 (-16.42%)</td><td>254.60 (-0.20%)</td><td>25.76 <b>(-77.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>535.80 (n/a)</td><td>380.02 (n/a)</td><td>349.50 (n/a)</td><td>255.10 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.32 (-10.26%)</td><td>0.23 (+5.15%)</td><td>0.21 <b>(-26.07%)</b></td><td>0.16 <b>(+218.13%)</b></td><td>0.06 <b>(-53.86%)</b></td><td>604.90 <b>(-68.57%)</b></td><td>454.54 <b>(-42.51%)</b></td><td>474.30 <b>(+35.28%)</b></td><td>307.40 (+11.42%)</td><td>118.76 <b>(-83.45%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.28 (n/a)</td><td>0.05 (n/a)</td><td>0.14 (n/a)</td><td>1924.40 (n/a)</td><td>790.68 (n/a)</td><td>350.60 (n/a)</td><td>275.90 (n/a)</td><td>717.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.34 (-7.29%)</td><td>0.22 (-17.89%)</td><td>0.19 <b>(-30.89%)</b></td><td>0.15 (-15.39%)</td><td>0.08 (-6.16%)</td><td>649.30 (+18.18%)</td><td>480.62 <b>(+22.81%)</b></td><td>509.00 <b>(+44.73%)</b></td><td>289.40 (+7.86%)</td><td>150.62 (+18.78%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>549.40 (n/a)</td><td>391.34 (n/a)</td><td>351.70 (n/a)</td><td>268.30 (n/a)</td><td>126.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.26 (-15.39%)</td><td>0.17 <b>(-23.20%)</b></td><td>0.14 <b>(-23.55%)</b></td><td>0.03 <b>(-82.83%)</b></td><td>0.10 <b>(+69.70%)</b></td><td>2460.20 <b>(+482.30%)</b></td><td>814.04 <b>(+128.38%)</b></td><td>511.40 <b>(+30.83%)</b></td><td>282.90 (+18.17%)</td><td>927.92 <b>(+1067.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>422.50 (n/a)</td><td>356.44 (n/a)</td><td>390.90 (n/a)</td><td>239.40 (n/a)</td><td>79.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.17 <b>(-30.65%)</b></td><td>0.15 (-5.05%)</td><td>0.14 (+0.85%)</td><td>0.13 <b>(+30.47%)</b></td><td>0.02 <b>(-68.72%)</b></td><td>550.00 <b>(-23.36%)</b></td><td>501.80 (-1.86%)</td><td>535.00 (-0.83%)</td><td>440.30 <b>(+44.17%)</b></td><td>53.71 <b>(-64.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>717.60 (n/a)</td><td>511.30 (n/a)</td><td>539.50 (n/a)</td><td>305.40 (n/a)</td><td>151.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.25 (-9.60%)</td><td>0.14 <b>(-22.55%)</b></td><td>0.13 (-17.66%)</td><td>0.04 <b>(-45.11%)</b></td><td>0.08 (-14.67%)</td><td>1971.00 <b>(+82.16%)</b></td><td>790.68 <b>(+47.44%)</b></td><td>570.30 <b>(+21.44%)</b></td><td>295.90 (+10.62%)</td><td>676.48 <b>(+101.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>1082.00 (n/a)</td><td>536.28 (n/a)</td><td>469.60 (n/a)</td><td>267.50 (n/a)</td><td>335.04 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (-10.20%)</td><td>0.12 (+6.78%)</td><td>0.13 <b>(+67.01%)</b></td><td>0.08 (+14.45%)</td><td>0.03 <b>(-25.34%)</b></td><td>471.70 (-12.62%)</td><td>345.30 (-11.02%)</td><td>273.50 <b>(-40.13%)</b></td><td>253.10 (+11.35%)</td><td>110.51 <b>(-22.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>539.80 (n/a)</td><td>388.06 (n/a)</td><td>456.80 (n/a)</td><td>227.30 (n/a)</td><td>142.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (+3.60%)</td><td>0.10 <b>(+21.65%)</b></td><td>0.12 <b>(+53.25%)</b></td><td>0.06 <b>(+41.72%)</b></td><td>0.04 (-2.26%)</td><td>633.80 <b>(-29.44%)</b></td><td>403.26 <b>(-22.24%)</b></td><td>302.10 <b>(-34.74%)</b></td><td>258.60 (-3.47%)</td><td>173.64 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>898.20 (n/a)</td><td>518.60 (n/a)</td><td>462.90 (n/a)</td><td>267.90 (n/a)</td><td>257.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.21 <b>(+33.46%)</b></td><td>0.12 (-5.27%)</td><td>0.11 <b>(-28.30%)</b></td><td>0.05 <b>(-21.97%)</b></td><td>0.06 <b>(+51.78%)</b></td><td>680.10 <b>(+28.18%)</b></td><td>389.54 (+17.58%)</td><td>350.90 <b>(+39.47%)</b></td><td>175.50 <b>(-25.10%)</b></td><td>196.91 <b>(+50.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>530.60 (n/a)</td><td>331.30 (n/a)</td><td>251.60 (n/a)</td><td>234.30 (n/a)</td><td>130.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (-3.90%)</td><td>0.11 (+10.26%)</td><td>0.12 <b>(+52.06%)</b></td><td>0.02 (+8.78%)</td><td>0.06 (+1.57%)</td><td>1836.40 (-8.07%)</td><td>617.18 (-9.41%)</td><td>297.80 <b>(-34.25%)</b></td><td>235.80 (+4.06%)</td><td>688.73 (-7.42%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1997.50 (n/a)</td><td>681.26 (n/a)</td><td>452.90 (n/a)</td><td>226.60 (n/a)</td><td>743.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-5.52%)</td><td>0.09 (-10.46%)</td><td>0.08 (+5.65%)</td><td>0.06 (-9.62%)</td><td>0.03 (-16.33%)</td><td>575.90 (+10.64%)</td><td>441.86 (+9.92%)</td><td>441.90 (-5.33%)</td><td>265.40 (+5.82%)</td><td>133.30 (+1.87%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>520.50 (n/a)</td><td>401.98 (n/a)</td><td>466.80 (n/a)</td><td>250.80 (n/a)</td><td>130.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-7.55%)</td><td>0.09 (+1.17%)</td><td>0.06 <b>(-27.51%)</b></td><td>0.05 (+16.42%)</td><td>0.04 (+10.66%)</td><td>676.80 (-14.10%)</td><td>492.32 (+1.82%)</td><td>613.10 <b>(+37.93%)</b></td><td>265.10 (+8.16%)</td><td>201.96 (+2.07%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>787.90 (n/a)</td><td>483.52 (n/a)</td><td>444.50 (n/a)</td><td>245.10 (n/a)</td><td>197.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 <b>(-26.72%)</b></td><td>0.12 <b>(-27.80%)</b></td><td>0.10 <b>(-35.31%)</b></td><td>0.07 (-9.51%)</td><td>0.04 <b>(-26.27%)</b></td><td>593.30 (+10.50%)</td><td>391.94 <b>(+34.04%)</b></td><td>397.00 <b>(+54.60%)</b></td><td>252.10 <b>(+36.49%)</b></td><td>138.18 (-1.30%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>536.90 (n/a)</td><td>292.40 (n/a)</td><td>256.80 (n/a)</td><td>184.70 (n/a)</td><td>139.99 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 <b>(+35.85%)</b></td><td>0.13 <b>(+53.08%)</b></td><td>0.13 <b>(+86.14%)</b></td><td>0.10 <b>(+70.46%)</b></td><td>0.04 (+18.29%)</td><td>429.40 <b>(-41.34%)</b></td><td>333.22 <b>(-36.73%)</b></td><td>306.70 <b>(-46.29%)</b></td><td>214.20 <b>(-26.39%)</b></td><td>92.99 <b>(-44.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>732.00 (n/a)</td><td>526.68 (n/a)</td><td>571.00 (n/a)</td><td>291.00 (n/a)</td><td>166.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 <b>(+24.83%)</b></td><td>0.13 <b>(+27.58%)</b></td><td>0.12 <b>(+66.67%)</b></td><td>0.09 <b>(+47.35%)</b></td><td>0.04 (-9.94%)</td><td>462.00 <b>(-32.14%)</b></td><td>341.40 <b>(-27.02%)</b></td><td>330.50 <b>(-40.00%)</b></td><td>219.20 (-19.88%)</td><td>96.31 <b>(-46.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>680.80 (n/a)</td><td>467.82 (n/a)</td><td>550.80 (n/a)</td><td>273.60 (n/a)</td><td>181.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.18 <b>(+100.65%)</b></td><td>0.12 <b>(+43.96%)</b></td><td>0.14 <b>(+63.86%)</b></td><td>0.02 <b>(-70.75%)</b></td><td>0.06 <b>(+964.99%)</b></td><td>1907.30 <b>(+241.93%)</b></td><td>625.34 <b>(+23.57%)</b></td><td>301.80 <b>(-38.98%)</b></td><td>231.80 <b>(-50.15%)</b></td><td>720.05 <b>(+1887.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>506.06 (n/a)</td><td>494.60 (n/a)</td><td>465.00 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.16 (+4.19%)</td><td>0.11 (+4.42%)</td><td>0.09 (+7.00%)</td><td>0.06 (-4.22%)</td><td>0.05 (+12.06%)</td><td>641.90 (+4.41%)</td><td>444.32 (-1.86%)</td><td>480.10 (-6.56%)</td><td>254.20 (-4.00%)</td><td>180.83 (+8.10%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>614.80 (n/a)</td><td>452.74 (n/a)</td><td>513.80 (n/a)</td><td>264.80 (n/a)</td><td>167.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 <b>(-26.83%)</b></td><td>0.08 <b>(-22.05%)</b></td><td>0.08 (-0.25%)</td><td>0.04 <b>(-31.02%)</b></td><td>0.04 <b>(-33.77%)</b></td><td>1082.20 <b>(+44.97%)</b></td><td>584.66 <b>(+26.09%)</b></td><td>513.50 (+0.23%)</td><td>300.70 <b>(+36.68%)</b></td><td>294.63 <b>(+42.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>746.50 (n/a)</td><td>463.68 (n/a)</td><td>512.30 (n/a)</td><td>220.00 (n/a)</td><td>207.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-5.90%)</td><td>0.09 (-15.05%)</td><td>0.08 <b>(-34.85%)</b></td><td>0.05 (-9.40%)</td><td>0.04 (-9.87%)</td><td>658.70 (+10.39%)</td><td>424.80 (+16.68%)</td><td>459.90 <b>(+53.45%)</b></td><td>244.90 (+6.29%)</td><td>162.89 (+4.48%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>596.70 (n/a)</td><td>364.06 (n/a)</td><td>299.70 (n/a)</td><td>230.40 (n/a)</td><td>155.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (+2.35%)</td><td>0.10 (+3.06%)</td><td>0.11 (+11.66%)</td><td>0.07 (+6.83%)</td><td>0.03 (-0.51%)</td><td>492.30 (-6.39%)</td><td>361.30 (-3.27%)</td><td>309.30 (-10.43%)</td><td>253.40 (-2.31%)</td><td>112.61 (-4.22%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>525.90 (n/a)</td><td>373.52 (n/a)</td><td>345.30 (n/a)</td><td>259.40 (n/a)</td><td>117.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (-5.04%)</td><td>0.08 (+8.71%)</td><td>0.07 (-0.88%)</td><td>0.06 <b>(+218.69%)</b></td><td>0.03 <b>(-32.13%)</b></td><td>593.00 <b>(-68.62%)</b></td><td>476.36 <b>(-34.73%)</b></td><td>515.90 (+0.88%)</td><td>273.60 (+5.31%)</td><td>127.39 <b>(-80.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1889.80 (n/a)</td><td>729.80 (n/a)</td><td>511.40 (n/a)</td><td>259.80 (n/a)</td><td>657.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.19 (+15.85%)</td><td>0.09 (-8.02%)</td><td>0.07 (+2.23%)</td><td>0.06 (-6.35%)</td><td>0.06 (+19.50%)</td><td>625.90 (+6.79%)</td><td>486.24 (+11.90%)</td><td>533.40 (-2.18%)</td><td>182.70 (-13.70%)</td><td>177.28 (-0.72%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>586.10 (n/a)</td><td>434.54 (n/a)</td><td>545.30 (n/a)</td><td>211.70 (n/a)</td><td>178.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.13 (-5.43%)</td><td>0.10 <b>(+34.49%)</b></td><td>0.09 <b>(+22.09%)</b></td><td>0.06 <b>(+217.93%)</b></td><td>0.03 <b>(-26.60%)</b></td><td>540.90 <b>(-68.55%)</b></td><td>382.66 <b>(-45.23%)</b></td><td>398.60 (-18.10%)</td><td>262.50 (+5.76%)</td><td>120.60 <b>(-79.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1719.80 (n/a)</td><td>698.68 (n/a)</td><td>486.70 (n/a)</td><td>248.20 (n/a)</td><td>583.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.08 <b>(-46.15%)</b></td><td>0.07 (-12.01%)</td><td>0.06 (-12.61%)</td><td>0.06 <b>(+226.64%)</b></td><td>0.01 <b>(-82.71%)</b></td><td>574.20 <b>(-69.39%)</b></td><td>520.58 <b>(-27.07%)</b></td><td>552.30 (+14.42%)</td><td>439.80 <b>(+85.65%)</b></td><td>58.35 <b>(-91.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1875.70 (n/a)</td><td>713.76 (n/a)</td><td>482.70 (n/a)</td><td>236.90 (n/a)</td><td>660.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.47 <b>(-21.25%)</b></td><td>0.32 (-5.92%)</td><td>0.26 (+1.01%)</td><td>0.21 (+0.70%)</td><td>0.11 <b>(-32.73%)</b></td><td>615.60 (-0.69%)</td><td>451.84 (-0.97%)</td><td>512.60 (-0.99%)</td><td>276.30 <b>(+26.98%)</b></td><td>143.83 (-19.74%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.60 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>619.90 (n/a)</td><td>456.28 (n/a)</td><td>517.70 (n/a)</td><td>217.60 (n/a)</td><td>179.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.39 <b>(-27.00%)</b></td><td>0.31 (-1.88%)</td><td>0.30 (+14.30%)</td><td>0.20 (-7.93%)</td><td>0.08 <b>(-33.52%)</b></td><td>643.30 (+8.61%)</td><td>458.86 (-1.08%)</td><td>437.90 (-12.51%)</td><td>335.40 <b>(+36.95%)</b></td><td>133.69 (+1.50%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.54 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>592.30 (n/a)</td><td>463.88 (n/a)</td><td>500.50 (n/a)</td><td>244.90 (n/a)</td><td>131.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.50 <b>(+23.47%)</b></td><td>0.38 <b>(+47.34%)</b></td><td>0.42 <b>(+57.82%)</b></td><td>0.22 <b>(+81.24%)</b></td><td>0.13 <b>(+27.40%)</b></td><td>584.00 <b>(-44.82%)</b></td><td>379.64 <b>(-34.83%)</b></td><td>312.30 <b>(-36.63%)</b></td><td>260.40 (-19.03%)</td><td>144.93 <b>(-48.12%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>1058.40 (n/a)</td><td>582.54 (n/a)</td><td>492.80 (n/a)</td><td>321.60 (n/a)</td><td>279.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (-4.90%)</td><td>0.01 (-1.29%)</td><td>0.01 (+2.35%)</td><td>0.01 (+6.46%)</td><td>0.00 (-18.64%)</td><td>492.30 (-6.09%)</td><td>397.24 (-1.56%)</td><td>447.40 (-2.29%)</td><td>270.10 (+5.14%)</td><td>100.77 (-18.64%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.20 (n/a)</td><td>403.54 (n/a)</td><td>457.90 (n/a)</td><td>256.90 (n/a)</td><td>123.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.01 <b>(-25.14%)</b></td><td>0.01 (-16.73%)</td><td>0.01 <b>(-23.07%)</b></td><td>0.01 <b>(+27.24%)</b></td><td>0.00 <b>(-48.17%)</b></td><td>443.00 <b>(-21.40%)</b></td><td>369.06 (+11.76%)</td><td>373.70 <b>(+29.98%)</b></td><td>289.90 <b>(+33.59%)</b></td><td>68.13 <b>(-49.41%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.60 (n/a)</td><td>330.24 (n/a)</td><td>287.50 (n/a)</td><td>217.00 (n/a)</td><td>134.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+11.39%)</td><td>0.01 (+12.77%)</td><td>0.01 <b>(+38.15%)</b></td><td>0.01 (+4.43%)</td><td>0.00 <b>(+20.05%)</b></td><td>497.40 (-4.24%)</td><td>351.72 (-10.14%)</td><td>299.00 <b>(-27.60%)</b></td><td>263.60 (-10.22%)</td><td>100.91 (+7.38%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.40 (n/a)</td><td>391.40 (n/a)</td><td>413.00 (n/a)</td><td>293.60 (n/a)</td><td>93.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.83 (-3.13%)</td><td>6.95 (-5.11%)</td><td>7.78 (-2.31%)</td><td>3.16 <b>(-21.61%)</b></td><td>2.28 (+12.28%)</td><td>663.60 <b>(+27.57%)</b></td><td>348.14 (+11.33%)</td><td>269.70 (+2.35%)</td><td>237.70 (+3.26%)</td><td>179.17 <b>(+49.60%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>9.11 (n/a)</td><td>7.32 (n/a)</td><td>7.96 (n/a)</td><td>4.03 (n/a)</td><td>2.03 (n/a)</td><td>520.20 (n/a)</td><td>312.70 (n/a)</td><td>263.50 (n/a)</td><td>230.20 (n/a)</td><td>119.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.52 (-17.70%)</td><td>0.44 (-7.27%)</td><td>0.48 (-2.81%)</td><td>0.32 (+16.03%)</td><td>0.09 <b>(-33.88%)</b></td><td>410.80 (-13.82%)</td><td>311.12 (+3.49%)</td><td>273.10 (+2.90%)</td><td>253.30 <b>(+21.49%)</b></td><td>67.14 <b>(-34.87%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.63 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>476.70 (n/a)</td><td>300.64 (n/a)</td><td>265.40 (n/a)</td><td>208.50 (n/a)</td><td>103.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.59 (-4.78%)</td><td>0.42 (+4.31%)</td><td>0.55 <b>(+38.61%)</b></td><td>0.07 <b>(-69.66%)</b></td><td>0.22 <b>(+38.23%)</b></td><td>1926.80 <b>(+229.65%)</b></td><td>604.42 <b>(+61.48%)</b></td><td>239.90 <b>(-27.85%)</b></td><td>222.50 (+5.05%)</td><td>742.57 <b>(+387.15%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.62 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>584.50 (n/a)</td><td>374.30 (n/a)</td><td>332.50 (n/a)</td><td>211.80 (n/a)</td><td>152.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.57 (-14.77%)</td><td>0.45 (+5.79%)</td><td>0.47 (+3.07%)</td><td>0.26 <b>(+21.79%)</b></td><td>0.11 <b>(-37.54%)</b></td><td>506.70 (-17.89%)</td><td>317.68 (-14.26%)</td><td>278.80 (-2.99%)</td><td>231.20 (+17.30%)</td><td>108.31 <b>(-37.57%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.67 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>617.10 (n/a)</td><td>370.52 (n/a)</td><td>287.40 (n/a)</td><td>197.10 (n/a)</td><td>173.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.60 (-2.53%)</td><td>0.45 (-4.11%)</td><td>0.49 (+7.34%)</td><td>0.20 <b>(-43.30%)</b></td><td>0.15 <b>(+50.53%)</b></td><td>675.20 <b>(+76.38%)</b></td><td>342.94 (+17.42%)</td><td>271.10 (-6.81%)</td><td>218.80 (+2.58%)</td><td>187.34 <b>(+201.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.62 (n/a)</td><td>0.47 (n/a)</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>382.80 (n/a)</td><td>292.06 (n/a)</td><td>290.90 (n/a)</td><td>213.30 (n/a)</td><td>62.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.55 (+2.94%)</td><td>0.40 (-12.59%)</td><td>0.44 (-11.18%)</td><td>0.26 (-14.30%)</td><td>0.12 <b>(+35.08%)</b></td><td>512.10 (+16.70%)</td><td>357.46 (+19.26%)</td><td>300.90 (+12.61%)</td><td>241.60 (-2.85%)</td><td>118.64 <b>(+51.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>438.80 (n/a)</td><td>299.72 (n/a)</td><td>267.20 (n/a)</td><td>248.70 (n/a)</td><td>78.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 <b>(+28.08%)</b></td><td>0.01 <b>(+36.60%)</b></td><td>0.02 <b>(+53.91%)</b></td><td>0.01 <b>(+33.60%)</b></td><td>0.00 (+9.60%)</td><td>459.90 <b>(-25.15%)</b></td><td>294.84 <b>(-27.98%)</b></td><td>269.00 <b>(-35.02%)</b></td><td>223.80 <b>(-21.91%)</b></td><td>94.40 <b>(-29.23%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.40 (n/a)</td><td>409.40 (n/a)</td><td>414.00 (n/a)</td><td>286.60 (n/a)</td><td>133.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.02 (+2.26%)</td><td>0.01 (-5.89%)</td><td>0.01 <b>(-34.96%)</b></td><td>0.01 (+17.12%)</td><td>0.00 (+9.83%)</td><td>513.80 (-14.62%)</td><td>379.00 (+6.08%)</td><td>439.10 <b>(+53.75%)</b></td><td>230.60 (-2.25%)</td><td>132.67 (-12.29%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.80 (n/a)</td><td>357.28 (n/a)</td><td>285.60 (n/a)</td><td>235.90 (n/a)</td><td>151.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.00 (+20.00%)</td><td>0.00 (+14.29%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.03%)</b></td><td>20026.59 (-4.59%)</td><td>14392.45 (-7.12%)</td><td>15538.62 (-7.43%)</td><td>6654.60 (-13.76%)</td><td>5015.45 (+1.23%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20990.00 (n/a)</td><td>15496.55 (n/a)</td><td>16785.78 (n/a)</td><td>7715.93 (n/a)</td><td>4954.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.00 <b>(-38.46%)</b></td><td>0.00 (-9.68%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-52.62%)</b></td><td>18534.09 (-10.79%)</td><td>15350.10 (-5.53%)</td><td>17579.26 (+1.10%)</td><td>10155.64 <b>(+65.79%)</b></td><td>3987.11 <b>(-33.28%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20775.88 (n/a)</td><td>16247.85 (n/a)</td><td>17387.87 (n/a)</td><td>6125.44 (n/a)</td><td>5975.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.15 (+13.05%)</td><td>0.10 (-4.99%)</td><td>0.08 (-14.22%)</td><td>0.07 (-7.99%)</td><td>0.03 <b>(+30.93%)</b></td><td>29857.70 (+8.61%)</td><td>23765.74 (+8.13%)</td><td>26742.93 (+16.58%)</td><td>13834.25 (-11.56%)</td><td>6364.39 <b>(+21.86%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27490.69 (n/a)</td><td>21977.91 (n/a)</td><td>22938.65 (n/a)</td><td>15642.08 (n/a)</td><td>5222.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.87 (-2.97%)</td><td>1.74 (-4.27%)</td><td>1.68 (-0.16%)</td><td>0.52 (-8.59%)</td><td>0.96 (+5.48%)</td><td>2007.50 (+9.40%)</td><td>871.06 (+9.76%)</td><td>623.00 (+0.18%)</td><td>364.80 (+3.05%)</td><td>673.70 (+12.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.96 (n/a)</td><td>1.81 (n/a)</td><td>1.69 (n/a)</td><td>0.57 (n/a)</td><td>0.91 (n/a)</td><td>1835.00 (n/a)</td><td>793.62 (n/a)</td><td>621.90 (n/a)</td><td>354.00 (n/a)</td><td>599.78 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.04 <b>(+47.70%)</b></td><td>1.67 <b>(+38.56%)</b></td><td>1.44 <b>(+23.97%)</b></td><td>0.31 (+2.46%)</td><td>1.42 <b>(+39.93%)</b></td><td>3433.60 (-2.40%)</td><td>1228.46 <b>(-31.42%)</b></td><td>727.20 (-19.33%)</td><td>259.30 <b>(-32.32%)</b></td><td>1264.67 (-19.15%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.74 (n/a)</td><td>1.21 (n/a)</td><td>1.16 (n/a)</td><td>0.30 (n/a)</td><td>1.01 (n/a)</td><td>3518.20 (n/a)</td><td>1791.22 (n/a)</td><td>901.50 (n/a)</td><td>383.10 (n/a)</td><td>1564.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.19 (-8.97%)</td><td>2.10 (+11.47%)</td><td>1.88 <b>(+26.57%)</b></td><td>1.36 <b>(+20.76%)</b></td><td>0.69 <b>(-28.23%)</b></td><td>768.40 (-17.20%)</td><td>539.10 (-17.07%)</td><td>557.80 <b>(-20.99%)</b></td><td>328.90 (+9.85%)</td><td>161.91 <b>(-33.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.50 (n/a)</td><td>1.89 (n/a)</td><td>1.49 (n/a)</td><td>1.13 (n/a)</td><td>0.96 (n/a)</td><td>928.00 (n/a)</td><td>650.04 (n/a)</td><td>706.00 (n/a)</td><td>299.40 (n/a)</td><td>243.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.69 <b>(+29.76%)</b></td><td>2.27 (+5.43%)</td><td>1.73 (+15.57%)</td><td>1.51 <b>(+38.52%)</b></td><td>1.35 (+8.25%)</td><td>694.40 <b>(-27.82%)</b></td><td>549.58 (-13.13%)</td><td>605.50 (-13.48%)</td><td>223.70 <b>(-22.94%)</b></td><td>186.06 <b>(-41.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.61 (n/a)</td><td>2.15 (n/a)</td><td>1.50 (n/a)</td><td>1.09 (n/a)</td><td>1.25 (n/a)</td><td>962.00 (n/a)</td><td>632.68 (n/a)</td><td>699.80 (n/a)</td><td>290.30 (n/a)</td><td>319.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>3.82 (-8.11%)</td><td>2.46 <b>(-26.68%)</b></td><td>2.59 <b>(-32.17%)</b></td><td>0.60 <b>(-74.98%)</b></td><td>1.29 <b>(+59.03%)</b></td><td>3521.00 <b>(+299.70%)</b></td><td>1323.48 <b>(+101.05%)</b></td><td>809.20 <b>(+47.42%)</b></td><td>549.70 (+8.83%)</td><td>1249.15 <b>(+617.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.15 (n/a)</td><td>3.36 (n/a)</td><td>3.82 (n/a)</td><td>2.38 (n/a)</td><td>0.81 (n/a)</td><td>880.90 (n/a)</td><td>658.28 (n/a)</td><td>548.90 (n/a)</td><td>505.10 (n/a)</td><td>174.10 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>5.03 (-13.08%)</td><td>3.74 (-3.96%)</td><td>3.87 (-10.83%)</td><td>1.91 <b>(+231.48%)</b></td><td>1.25 <b>(-37.57%)</b></td><td>1096.60 <b>(-69.83%)</b></td><td>632.26 <b>(-42.09%)</b></td><td>541.90 (+12.15%)</td><td>417.00 (+15.03%)</td><td>276.43 <b>(-80.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.79 (n/a)</td><td>3.89 (n/a)</td><td>4.34 (n/a)</td><td>0.58 (n/a)</td><td>2.00 (n/a)</td><td>3635.10 (n/a)</td><td>1091.84 (n/a)</td><td>483.20 (n/a)</td><td>362.50 (n/a)</td><td>1423.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.49 <b>(-20.20%)</b></td><td>3.01 (-4.67%)</td><td>2.75 <b>(-21.76%)</b></td><td>1.96 <b>(+225.69%)</b></td><td>0.94 <b>(-59.31%)</b></td><td>1067.70 <b>(-69.30%)</b></td><td>748.32 <b>(-46.89%)</b></td><td>762.60 <b>(+27.80%)</b></td><td>466.60 <b>(+25.30%)</b></td><td>219.54 <b>(-84.09%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.63 (n/a)</td><td>3.16 (n/a)</td><td>3.51 (n/a)</td><td>0.60 (n/a)</td><td>2.31 (n/a)</td><td>3477.40 (n/a)</td><td>1409.10 (n/a)</td><td>596.70 (n/a)</td><td>372.40 (n/a)</td><td>1379.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.19 (+11.13%)</td><td>2.52 <b>(-29.58%)</b></td><td>1.60 <b>(-49.36%)</b></td><td>0.60 <b>(-78.06%)</b></td><td>2.39 <b>(+104.58%)</b></td><td>3515.10 <b>(+355.68%)</b></td><td>1842.80 <b>(+194.07%)</b></td><td>1310.70 <b>(+97.45%)</b></td><td>338.60 (-10.02%)</td><td>1547.35 <b>(+873.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.57 (n/a)</td><td>3.58 (n/a)</td><td>3.16 (n/a)</td><td>2.72 (n/a)</td><td>1.17 (n/a)</td><td>771.40 (n/a)</td><td>626.66 (n/a)</td><td>663.80 (n/a)</td><td>376.30 (n/a)</td><td>158.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.38 <b>(+83.43%)</b></td><td>3.73 <b>(+53.29%)</b></td><td>3.02 <b>(+69.15%)</b></td><td>0.61 <b>(-28.86%)</b></td><td>2.72 <b>(+85.72%)</b></td><td>3429.90 <b>(+40.57%)</b></td><td>1160.60 (-3.98%)</td><td>695.50 <b>(-40.88%)</b></td><td>284.20 <b>(-45.48%)</b></td><td>1300.86 <b>(+65.20%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.02 (n/a)</td><td>2.43 (n/a)</td><td>1.78 (n/a)</td><td>0.86 (n/a)</td><td>1.47 (n/a)</td><td>2440.00 (n/a)</td><td>1208.68 (n/a)</td><td>1176.40 (n/a)</td><td>521.30 (n/a)</td><td>787.46 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.16 <b>(+71.40%)</b></td><td>3.28 <b>(+25.56%)</b></td><td>2.77 (-0.73%)</td><td>0.61 (+3.90%)</td><td>2.39 <b>(+75.26%)</b></td><td>3420.40 (-3.75%)</td><td>1181.64 (-7.89%)</td><td>758.30 (+0.74%)</td><td>292.90 <b>(-41.65%)</b></td><td>1266.43 (-1.23%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.18 (n/a)</td><td>2.61 (n/a)</td><td>2.79 (n/a)</td><td>0.59 (n/a)</td><td>1.36 (n/a)</td><td>3553.70 (n/a)</td><td>1282.86 (n/a)</td><td>752.70 (n/a)</td><td>502.00 (n/a)</td><td>1282.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>4.56 (-19.61%)</td><td>3.92 (+3.32%)</td><td>3.99 (-0.82%)</td><td>3.06 <b>(+152.43%)</b></td><td>0.54 <b>(-66.72%)</b></td><td>1368.50 <b>(-60.38%)</b></td><td>1089.40 <b>(-25.69%)</b></td><td>1052.40 (+0.81%)</td><td>920.70 <b>(+24.39%)</b></td><td>166.48 <b>(-85.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.67 (n/a)</td><td>3.79 (n/a)</td><td>4.02 (n/a)</td><td>1.21 (n/a)</td><td>1.61 (n/a)</td><td>3454.40 (n/a)</td><td>1466.00 (n/a)</td><td>1043.90 (n/a)</td><td>740.20 (n/a)</td><td>1120.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.80 <b>(+25.46%)</b></td><td>3.85 <b>(-40.03%)</b></td><td>3.90 <b>(-39.12%)</b></td><td>1.17 <b>(-80.17%)</b></td><td>3.09 <b>(+538.93%)</b></td><td>3587.30 <b>(+404.26%)</b></td><td>1874.54 <b>(+185.29%)</b></td><td>1074.70 <b>(+64.25%)</b></td><td>476.60 <b>(-20.29%)</b></td><td>1411.94 <b>(+2760.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.01 (n/a)</td><td>6.41 (n/a)</td><td>6.41 (n/a)</td><td>5.90 (n/a)</td><td>0.48 (n/a)</td><td>711.40 (n/a)</td><td>657.06 (n/a)</td><td>654.30 (n/a)</td><td>597.90 (n/a)</td><td>49.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>6.26 (-15.68%)</td><td>3.78 (-15.16%)</td><td>3.49 (-12.16%)</td><td>1.67 <b>(+38.28%)</b></td><td>2.18 (-8.02%)</td><td>2508.30 <b>(-27.68%)</b></td><td>1518.92 (+9.56%)</td><td>1201.30 (+13.86%)</td><td>669.90 (+18.61%)</td><td>917.91 <b>(-22.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.43 (n/a)</td><td>4.45 (n/a)</td><td>3.98 (n/a)</td><td>1.21 (n/a)</td><td>2.37 (n/a)</td><td>3468.50 (n/a)</td><td>1386.34 (n/a)</td><td>1055.10 (n/a)</td><td>564.80 (n/a)</td><td>1188.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>7.90 (+0.78%)</td><td>4.41 (-4.53%)</td><td>4.62 (+11.91%)</td><td>1.25 (-1.44%)</td><td>2.92 (+12.82%)</td><td>3344.90 (+1.46%)</td><td>1570.16 (+16.68%)</td><td>908.40 (-10.64%)</td><td>531.00 (-0.77%)</td><td>1252.35 (+11.21%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.84 (n/a)</td><td>4.62 (n/a)</td><td>4.13 (n/a)</td><td>1.27 (n/a)</td><td>2.59 (n/a)</td><td>3296.70 (n/a)</td><td>1345.74 (n/a)</td><td>1016.60 (n/a)</td><td>535.10 (n/a)</td><td>1126.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.81 (-6.34%)</td><td>4.79 <b>(-28.75%)</b></td><td>5.05 <b>(-22.94%)</b></td><td>1.20 <b>(-72.72%)</b></td><td>2.79 <b>(+56.15%)</b></td><td>3509.70 <b>(+266.55%)</b></td><td>1358.84 <b>(+105.26%)</b></td><td>830.10 <b>(+29.76%)</b></td><td>476.10 (+6.77%)</td><td>1229.37 <b>(+565.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>9.41 (n/a)</td><td>6.72 (n/a)</td><td>6.56 (n/a)</td><td>4.38 (n/a)</td><td>1.79 (n/a)</td><td>957.50 (n/a)</td><td>662.00 (n/a)</td><td>639.70 (n/a)</td><td>445.90 (n/a)</td><td>184.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>8.44 <b>(-21.13%)</b></td><td>5.30 <b>(+32.54%)</b></td><td>4.51 <b>(+80.43%)</b></td><td>1.71 <b>(+47.03%)</b></td><td>2.81 <b>(-27.66%)</b></td><td>2452.10 <b>(-31.98%)</b></td><td>1092.10 <b>(-40.35%)</b></td><td>929.30 <b>(-44.58%)</b></td><td>497.10 <b>(+26.78%)</b></td><td>797.38 <b>(-35.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>10.70 (n/a)</td><td>4.00 (n/a)</td><td>2.50 (n/a)</td><td>1.16 (n/a)</td><td>3.88 (n/a)</td><td>3605.20 (n/a)</td><td>1830.74 (n/a)</td><td>1676.80 (n/a)</td><td>392.10 (n/a)</td><td>1238.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.66 (+0.99%)</td><td>1.21 <b>(+36.34%)</b></td><td>1.12 (+18.96%)</td><td>0.75 <b>(+352.44%)</b></td><td>0.40 <b>(-26.10%)</b></td><td>700.20 <b>(-77.90%)</b></td><td>473.38 <b>(-55.73%)</b></td><td>467.90 (-15.95%)</td><td>315.60 (-0.97%)</td><td>161.26 <b>(-86.40%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.65 (n/a)</td><td>0.89 (n/a)</td><td>0.94 (n/a)</td><td>0.17 (n/a)</td><td>0.54 (n/a)</td><td>3168.20 (n/a)</td><td>1069.42 (n/a)</td><td>556.70 (n/a)</td><td>318.70 (n/a)</td><td>1186.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>1.50 <b>(-40.87%)</b></td><td>1.05 <b>(-46.47%)</b></td><td>1.27 <b>(-43.76%)</b></td><td>0.45 (+6.33%)</td><td>0.50 <b>(-42.89%)</b></td><td>2311.40 (-5.95%)</td><td>1287.02 <b>(+50.85%)</b></td><td>825.50 <b>(+77.79%)</b></td><td>698.60 <b>(+69.11%)</b></td><td>755.15 (-15.91%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.54 (n/a)</td><td>1.96 (n/a)</td><td>2.26 (n/a)</td><td>0.43 (n/a)</td><td>0.88 (n/a)</td><td>2457.70 (n/a)</td><td>853.20 (n/a)</td><td>464.30 (n/a)</td><td>413.10 (n/a)</td><td>897.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.78 (-18.59%)</td><td>1.60 <b>(-40.75%)</b></td><td>1.76 <b>(-36.71%)</b></td><td>0.58 <b>(-65.27%)</b></td><td>0.88 <b>(+24.04%)</b></td><td>3616.70 <b>(+187.91%)</b></td><td>1784.80 <b>(+115.40%)</b></td><td>1191.00 <b>(+58.00%)</b></td><td>754.00 <b>(+22.84%)</b></td><td>1179.98 <b>(+352.39%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.42 (n/a)</td><td>2.71 (n/a)</td><td>2.78 (n/a)</td><td>1.67 (n/a)</td><td>0.71 (n/a)</td><td>1256.20 (n/a)</td><td>828.60 (n/a)</td><td>753.80 (n/a)</td><td>613.80 (n/a)</td><td>260.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>2.85 <b>(+47.37%)</b></td><td>1.42 (-6.72%)</td><td>0.93 <b>(-42.82%)</b></td><td>0.87 (-18.41%)</td><td>0.85 <b>(+121.46%)</b></td><td>604.50 <b>(+22.57%)</b></td><td>454.84 <b>(+25.20%)</b></td><td>560.70 <b>(+74.89%)</b></td><td>184.10 <b>(-32.17%)</b></td><td>188.27 <b>(+90.95%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.93 (n/a)</td><td>1.53 (n/a)</td><td>1.64 (n/a)</td><td>1.06 (n/a)</td><td>0.38 (n/a)</td><td>493.20 (n/a)</td><td>363.28 (n/a)</td><td>320.60 (n/a)</td><td>271.40 (n/a)</td><td>98.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (-9.75%)</td><td>0.08 <b>(-39.30%)</b></td><td>0.07 <b>(-41.55%)</b></td><td>0.05 <b>(-58.99%)</b></td><td>0.03 <b>(+144.61%)</b></td><td>673.20 <b>(+143.82%)</b></td><td>458.88 <b>(+83.52%)</b></td><td>440.50 <b>(+71.07%)</b></td><td>237.20 (+10.84%)</td><td>157.19 <b>(+525.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>276.10 (n/a)</td><td>250.04 (n/a)</td><td>257.50 (n/a)</td><td>214.00 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 (+5.56%)</td><td>0.09 (-11.05%)</td><td>0.09 (-19.84%)</td><td>0.07 (-11.18%)</td><td>0.03 <b>(+31.98%)</b></td><td>500.80 (+12.59%)</td><td>377.68 (+16.60%)</td><td>366.60 <b>(+24.78%)</b></td><td>235.00 (-5.28%)</td><td>113.50 <b>(+43.73%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>444.80 (n/a)</td><td>323.90 (n/a)</td><td>293.80 (n/a)</td><td>248.10 (n/a)</td><td>78.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.24 (-8.30%)</td><td>0.17 (-17.96%)</td><td>0.14 <b>(-34.29%)</b></td><td>0.10 (-9.23%)</td><td>0.06 (-0.18%)</td><td>638.50 (+10.16%)</td><td>434.62 <b>(+22.87%)</b></td><td>452.90 <b>(+52.18%)</b></td><td>278.20 (+9.06%)</td><td>145.31 (+10.85%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>579.60 (n/a)</td><td>353.72 (n/a)</td><td>297.60 (n/a)</td><td>255.10 (n/a)</td><td>131.08 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.14 <b>(-35.58%)</b></td><td>0.12 <b>(-31.96%)</b></td><td>0.14 <b>(-27.04%)</b></td><td>0.06 <b>(-46.78%)</b></td><td>0.03 (-17.61%)</td><td>1064.70 <b>(+87.88%)</b></td><td>619.88 <b>(+54.00%)</b></td><td>484.10 <b>(+37.06%)</b></td><td>465.50 <b>(+55.27%)</b></td><td>255.05 <b>(+138.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>566.70 (n/a)</td><td>402.52 (n/a)</td><td>353.20 (n/a)</td><td>299.80 (n/a)</td><td>106.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.23 (-9.01%)</td><td>0.17 (-4.57%)</td><td>0.15 (+5.79%)</td><td>0.12 (-6.79%)</td><td>0.05 (-19.86%)</td><td>545.50 (+7.28%)</td><td>407.58 (+2.64%)</td><td>433.60 (-5.47%)</td><td>286.80 (+9.89%)</td><td>108.66 (-7.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>508.50 (n/a)</td><td>397.08 (n/a)</td><td>458.70 (n/a)</td><td>261.00 (n/a)</td><td>117.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.51 (-0.18%)</td><td>0.31 <b>(-32.20%)</b></td><td>0.26 <b>(-47.80%)</b></td><td>0.20 <b>(-35.10%)</b></td><td>0.12 <b>(+42.88%)</b></td><td>649.80 <b>(+54.05%)</b></td><td>465.94 <b>(+56.81%)</b></td><td>504.60 <b>(+91.57%)</b></td><td>256.70 (+0.16%)</td><td>144.85 <b>(+105.69%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>421.80 (n/a)</td><td>297.14 (n/a)</td><td>263.40 (n/a)</td><td>256.30 (n/a)</td><td>70.42 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.35 <b>(-28.91%)</b></td><td>0.27 (-18.55%)</td><td>0.28 <b>(-34.00%)</b></td><td>0.15 <b>(+22.22%)</b></td><td>0.09 <b>(-53.84%)</b></td><td>848.50 (-18.18%)</td><td>539.36 (-7.00%)</td><td>467.30 <b>(+51.52%)</b></td><td>372.00 <b>(+40.70%)</b></td><td>200.54 <b>(-50.50%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.43 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>1037.00 (n/a)</td><td>579.98 (n/a)</td><td>308.40 (n/a)</td><td>264.40 (n/a)</td><td>405.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.49 (-4.23%)</td><td>0.30 (-14.31%)</td><td>0.28 (-7.66%)</td><td>0.20 (-18.51%)</td><td>0.11 (+0.04%)</td><td>654.80 <b>(+22.71%)</b></td><td>484.86 (+18.68%)</td><td>463.90 (+8.29%)</td><td>269.80 (+4.41%)</td><td>151.41 <b>(+24.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>533.60 (n/a)</td><td>408.56 (n/a)</td><td>428.40 (n/a)</td><td>258.40 (n/a)</td><td>121.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:18:58</td><td>0.06 (+19.00%)</td><td>0.04 (+19.91%)</td><td>0.04 (+6.56%)</td><td>0.03 (+12.19%)</td><td>0.01 <b>(+56.18%)</b></td><td>576.50 (-10.87%)</td><td>427.42 (-13.31%)</td><td>457.70 (-6.15%)</td><td>278.80 (-15.97%)</td><td>132.80 (+17.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>646.80 (n/a)</td><td>493.04 (n/a)</td><td>487.70 (n/a)</td><td>331.80 (n/a)</td><td>113.20 (n/a)</td>
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
