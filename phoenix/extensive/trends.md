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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(-40.48%)</b></td><td>0.02 <b>(-34.48%)</b></td><td>0.01 <b>(-44.45%)</b></td><td>0.01 (-12.11%)</td><td>0.00 <b>(-42.95%)</b></td><td>537.70 (+13.77%)</td><td>413.96 <b>(+46.45%)</b></td><td>468.30 <b>(+80.05%)</b></td><td>293.20 <b>(+68.02%)</b></td><td>110.65 (-1.65%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>472.60 (n/a)</td><td>282.66 (n/a)</td><td>260.10 (n/a)</td><td>174.50 (n/a)</td><td>112.50 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (-6.30%)</td><td>0.02 (-8.90%)</td><td>0.02 (+10.20%)</td><td>0.01 <b>(-42.40%)</b></td><td>0.01 <b>(+52.89%)</b></td><td>710.00 <b>(+73.59%)</b></td><td>419.38 <b>(+25.10%)</b></td><td>302.80 (-9.26%)</td><td>243.40 (+6.71%)</td><td>204.82 <b>(+191.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>409.00 (n/a)</td><td>335.24 (n/a)</td><td>333.70 (n/a)</td><td>228.10 (n/a)</td><td>70.29 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+17.30%)</td><td>0.02 <b>(+75.17%)</b></td><td>0.02 <b>(+77.26%)</b></td><td>0.02 <b>(+531.22%)</b></td><td>0.01 <b>(-36.66%)</b></td><td>377.50 <b>(-84.16%)</b></td><td>274.22 <b>(-66.57%)</b></td><td>270.60 <b>(-43.58%)</b></td><td>202.90 (-14.75%)</td><td>67.17 <b>(-92.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2382.60 (n/a)</td><td>820.22 (n/a)</td><td>479.60 (n/a)</td><td>238.00 (n/a)</td><td>883.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-7.50%)</td><td>0.02 (-11.90%)</td><td>0.02 (-2.49%)</td><td>0.01 (-14.16%)</td><td>0.01 <b>(+36.40%)</b></td><td>496.70 (+16.51%)</td><td>362.08 (+18.73%)</td><td>285.50 (+2.55%)</td><td>265.30 (+8.07%)</td><td>119.00 <b>(+68.42%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>426.30 (n/a)</td><td>304.96 (n/a)</td><td>278.40 (n/a)</td><td>245.50 (n/a)</td><td>70.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-3.84%)</td><td>0.02 (+1.42%)</td><td>0.02 (-3.13%)</td><td>0.01 (+8.32%)</td><td>0.01 <b>(-20.26%)</b></td><td>573.20 (-7.68%)</td><td>367.12 (-6.09%)</td><td>302.80 (+3.24%)</td><td>258.50 (+4.02%)</td><td>128.06 <b>(-22.73%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.90 (n/a)</td><td>390.92 (n/a)</td><td>293.30 (n/a)</td><td>248.50 (n/a)</td><td>165.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-13.40%)</td><td>0.02 (-11.99%)</td><td>0.01 (-8.12%)</td><td>0.01 (+16.21%)</td><td>0.01 <b>(-32.44%)</b></td><td>545.40 (-13.95%)</td><td>437.36 (+3.93%)</td><td>500.90 (+8.84%)</td><td>249.80 (+15.43%)</td><td>131.57 <b>(-28.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.80 (n/a)</td><td>420.82 (n/a)</td><td>460.20 (n/a)</td><td>216.40 (n/a)</td><td>183.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (+8.63%)</td><td>0.04 (+16.69%)</td><td>0.04 <b>(+62.48%)</b></td><td>0.02 (+0.35%)</td><td>0.01 (-3.59%)</td><td>535.70 (-0.35%)</td><td>351.62 (-16.00%)</td><td>309.00 <b>(-38.45%)</b></td><td>219.20 (-7.94%)</td><td>123.33 (-13.00%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.60 (n/a)</td><td>418.62 (n/a)</td><td>502.00 (n/a)</td><td>238.10 (n/a)</td><td>141.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-16.56%)</td><td>0.04 (-11.24%)</td><td>0.04 <b>(-28.11%)</b></td><td>0.03 (+15.14%)</td><td>0.01 <b>(-33.21%)</b></td><td>456.90 (-13.14%)</td><td>350.38 (+4.05%)</td><td>342.50 <b>(+39.11%)</b></td><td>234.80 (+19.86%)</td><td>102.93 <b>(-31.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>526.00 (n/a)</td><td>336.74 (n/a)</td><td>246.20 (n/a)</td><td>195.90 (n/a)</td><td>150.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-14.19%)</td><td>0.04 (-4.87%)</td><td>0.03 <b>(-23.07%)</b></td><td>0.03 <b>(+30.00%)</b></td><td>0.01 <b>(-36.47%)</b></td><td>474.70 <b>(-23.08%)</b></td><td>358.04 (-8.70%)</td><td>378.50 <b>(+29.98%)</b></td><td>233.00 (+16.56%)</td><td>106.00 <b>(-48.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>617.10 (n/a)</td><td>392.14 (n/a)</td><td>291.20 (n/a)</td><td>199.90 (n/a)</td><td>206.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-16.21%)</td><td>0.04 (-5.54%)</td><td>0.03 <b>(-43.60%)</b></td><td>0.03 <b>(+328.11%)</b></td><td>0.01 <b>(-49.06%)</b></td><td>455.50 <b>(-76.64%)</b></td><td>371.40 <b>(-42.62%)</b></td><td>445.50 <b>(+77.28%)</b></td><td>238.00 (+19.36%)</td><td>109.08 <b>(-85.38%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1949.90 (n/a)</td><td>647.30 (n/a)</td><td>251.30 (n/a)</td><td>199.40 (n/a)</td><td>746.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (-7.94%)</td><td>0.03 (-12.94%)</td><td>0.03 (-5.78%)</td><td>0.02 (-8.56%)</td><td>0.01 <b>(-20.59%)</b></td><td>574.20 (+9.35%)</td><td>450.90 (+12.91%)</td><td>478.80 (+6.14%)</td><td>295.00 (+8.66%)</td><td>108.17 (-4.10%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>399.34 (n/a)</td><td>451.10 (n/a)</td><td>271.50 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 <b>(+46.92%)</b></td><td>0.04 (+11.04%)</td><td>0.03 (-17.39%)</td><td>0.02 (+2.78%)</td><td>0.02 <b>(+67.66%)</b></td><td>559.50 (-2.71%)</td><td>358.58 (-4.36%)</td><td>358.10 <b>(+21.06%)</b></td><td>176.50 <b>(-31.93%)</b></td><td>144.72 (+7.67%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>374.92 (n/a)</td><td>295.80 (n/a)</td><td>259.30 (n/a)</td><td>134.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 <b>(-21.16%)</b></td><td>0.07 <b>(-22.23%)</b></td><td>0.05 <b>(-45.24%)</b></td><td>0.05 (+10.96%)</td><td>0.02 <b>(-39.43%)</b></td><td>489.80 (-9.88%)</td><td>403.06 (+17.82%)</td><td>462.30 <b>(+82.58%)</b></td><td>249.60 <b>(+26.83%)</b></td><td>102.50 <b>(-33.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>543.50 (n/a)</td><td>342.10 (n/a)</td><td>253.20 (n/a)</td><td>196.80 (n/a)</td><td>153.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-8.06%)</td><td>0.07 <b>(-27.84%)</b></td><td>0.06 <b>(-37.78%)</b></td><td>0.04 <b>(-41.28%)</b></td><td>0.03 <b>(+73.71%)</b></td><td>616.40 <b>(+70.28%)</b></td><td>429.72 <b>(+53.91%)</b></td><td>444.70 <b>(+60.72%)</b></td><td>242.70 (+8.74%)</td><td>162.76 <b>(+214.61%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>362.00 (n/a)</td><td>279.20 (n/a)</td><td>276.70 (n/a)</td><td>223.20 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-0.12%)</td><td>0.07 (-14.52%)</td><td>0.05 <b>(-41.04%)</b></td><td>0.05 (-13.74%)</td><td>0.03 <b>(+23.97%)</b></td><td>543.10 (+15.92%)</td><td>402.22 <b>(+22.22%)</b></td><td>468.10 <b>(+69.60%)</b></td><td>250.80 (+0.12%)</td><td>135.46 <b>(+40.15%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>468.50 (n/a)</td><td>329.10 (n/a)</td><td>276.00 (n/a)</td><td>250.50 (n/a)</td><td>96.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-0.57%)</td><td>0.06 (-8.70%)</td><td>0.05 (-12.71%)</td><td>0.05 (+12.11%)</td><td>0.02 <b>(-21.93%)</b></td><td>481.60 (-10.81%)</td><td>411.54 (+4.12%)</td><td>452.70 (+14.58%)</td><td>247.90 (+0.57%)</td><td>96.47 <b>(-31.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>540.00 (n/a)</td><td>395.26 (n/a)</td><td>395.10 (n/a)</td><td>246.50 (n/a)</td><td>141.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (+3.30%)</td><td>0.06 (-15.71%)</td><td>0.07 (-8.99%)</td><td>0.01 <b>(-77.22%)</b></td><td>0.04 <b>(+87.73%)</b></td><td>2455.20 <b>(+338.98%)</b></td><td>782.84 <b>(+124.80%)</b></td><td>353.50 (+9.88%)</td><td>240.70 (-3.18%)</td><td>947.66 <b>(+664.06%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.30 (n/a)</td><td>348.24 (n/a)</td><td>321.70 (n/a)</td><td>248.60 (n/a)</td><td>124.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-19.31%)</td><td>0.06 <b>(-22.16%)</b></td><td>0.05 <b>(-40.44%)</b></td><td>0.04 (-3.38%)</td><td>0.02 <b>(-26.61%)</b></td><td>550.00 (+3.50%)</td><td>432.50 <b>(+24.87%)</b></td><td>498.00 <b>(+67.85%)</b></td><td>290.10 <b>(+23.92%)</b></td><td>120.03 (-5.73%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>531.40 (n/a)</td><td>346.36 (n/a)</td><td>296.70 (n/a)</td><td>234.10 (n/a)</td><td>127.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 <b>(-31.59%)</b></td><td>0.11 <b>(-27.48%)</b></td><td>0.11 <b>(-30.82%)</b></td><td>0.08 (-16.17%)</td><td>0.02 <b>(-47.87%)</b></td><td>625.00 (+19.30%)</td><td>458.28 <b>(+32.25%)</b></td><td>443.20 <b>(+44.55%)</b></td><td>334.40 <b>(+46.15%)</b></td><td>104.60 (-9.34%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>523.90 (n/a)</td><td>346.52 (n/a)</td><td>306.60 (n/a)</td><td>228.80 (n/a)</td><td>115.37 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (+9.08%)</td><td>0.14 (-1.92%)</td><td>0.13 (-15.29%)</td><td>0.10 (-4.35%)</td><td>0.05 <b>(+35.96%)</b></td><td>516.70 (+4.55%)</td><td>381.54 (+6.25%)</td><td>365.50 (+18.06%)</td><td>251.20 (-8.32%)</td><td>129.42 <b>(+32.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>494.20 (n/a)</td><td>359.08 (n/a)</td><td>309.60 (n/a)</td><td>274.00 (n/a)</td><td>97.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 (+2.76%)</td><td>0.14 (-10.70%)</td><td>0.11 <b>(-32.39%)</b></td><td>0.09 (-0.48%)</td><td>0.06 <b>(+25.34%)</b></td><td>567.30 (+0.48%)</td><td>403.24 (+17.30%)</td><td>467.10 <b>(+47.91%)</b></td><td>208.60 (-2.66%)</td><td>153.03 (+16.25%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>564.60 (n/a)</td><td>343.78 (n/a)</td><td>315.80 (n/a)</td><td>214.30 (n/a)</td><td>131.64 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (-10.83%)</td><td>0.11 <b>(-26.00%)</b></td><td>0.10 <b>(-41.26%)</b></td><td>0.08 (+3.04%)</td><td>0.03 <b>(-27.78%)</b></td><td>581.30 (-2.94%)</td><td>464.22 <b>(+29.33%)</b></td><td>479.40 <b>(+70.24%)</b></td><td>292.40 (+12.16%)</td><td>105.88 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>598.90 (n/a)</td><td>358.94 (n/a)</td><td>281.60 (n/a)</td><td>260.70 (n/a)</td><td>142.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.18 <b>(+38.82%)</b></td><td>0.12 <b>(+30.65%)</b></td><td>0.10 (+3.78%)</td><td>0.10 <b>(+164.83%)</b></td><td>0.04 (-4.72%)</td><td>506.40 <b>(-62.24%)</b></td><td>417.96 <b>(-34.41%)</b></td><td>476.20 (-3.64%)</td><td>271.10 <b>(-27.96%)</b></td><td>104.05 <b>(-74.18%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1341.20 (n/a)</td><td>637.26 (n/a)</td><td>494.20 (n/a)</td><td>376.30 (n/a)</td><td>403.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (+19.25%)</td><td>0.14 <b>(+38.33%)</b></td><td>0.11 <b>(+21.19%)</b></td><td>0.10 <b>(+110.44%)</b></td><td>0.05 (-2.41%)</td><td>496.10 <b>(-52.49%)</b></td><td>394.20 <b>(-34.67%)</b></td><td>450.60 (-17.49%)</td><td>226.60 (-16.14%)</td><td>111.44 <b>(-60.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>1044.10 (n/a)</td><td>603.44 (n/a)</td><td>546.10 (n/a)</td><td>270.20 (n/a)</td><td>280.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-5.75%)</td><td>0.01 (+12.02%)</td><td>0.01 <b>(+28.92%)</b></td><td>0.01 (+18.41%)</td><td>0.00 <b>(-42.79%)</b></td><td>388.20 (-15.55%)</td><td>290.64 (-15.47%)</td><td>273.30 <b>(-22.42%)</b></td><td>245.00 (+6.11%)</td><td>56.54 <b>(-46.04%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.70 (n/a)</td><td>343.82 (n/a)</td><td>352.30 (n/a)</td><td>230.90 (n/a)</td><td>104.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (+7.15%)</td><td>0.01 (-6.33%)</td><td>0.01 <b>(-34.60%)</b></td><td>0.00 (-16.30%)</td><td>0.00 <b>(+24.96%)</b></td><td>594.00 (+19.49%)</td><td>390.76 (+12.68%)</td><td>399.40 <b>(+52.91%)</b></td><td>224.20 (-6.66%)</td><td>166.15 <b>(+26.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.10 (n/a)</td><td>346.78 (n/a)</td><td>261.20 (n/a)</td><td>240.20 (n/a)</td><td>131.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-8.62%)</td><td>0.01 (-12.58%)</td><td>0.01 (-7.71%)</td><td>0.00 <b>(-34.98%)</b></td><td>0.00 <b>(+27.16%)</b></td><td>546.30 <b>(+53.80%)</b></td><td>323.06 <b>(+21.30%)</b></td><td>291.40 (+8.33%)</td><td>228.30 (+9.39%)</td><td>127.88 <b>(+126.20%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>355.20 (n/a)</td><td>266.34 (n/a)</td><td>269.00 (n/a)</td><td>208.70 (n/a)</td><td>56.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 <b>(-23.59%)</b></td><td>0.01 (-6.99%)</td><td>0.01 (+10.65%)</td><td>0.00 <b>(+55.12%)</b></td><td>0.00 <b>(-50.73%)</b></td><td>638.10 <b>(-35.53%)</b></td><td>416.34 (-11.01%)</td><td>378.00 (-9.63%)</td><td>299.50 <b>(+30.90%)</b></td><td>129.43 <b>(-57.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>989.80 (n/a)</td><td>467.84 (n/a)</td><td>418.30 (n/a)</td><td>228.80 (n/a)</td><td>304.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-16.07%)</td><td>0.01 (-19.74%)</td><td>0.01 (-18.38%)</td><td>0.00 <b>(+22.98%)</b></td><td>0.00 <b>(-38.23%)</b></td><td>622.90 (-18.69%)</td><td>488.46 (+12.60%)</td><td>519.20 <b>(+22.54%)</b></td><td>292.00 (+19.14%)</td><td>121.57 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>766.10 (n/a)</td><td>433.82 (n/a)</td><td>423.70 (n/a)</td><td>245.10 (n/a)</td><td>208.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 <b>(-34.28%)</b></td><td>0.01 <b>(-20.22%)</b></td><td>0.01 <b>(-29.64%)</b></td><td>0.00 <b>(+29.06%)</b></td><td>0.00 <b>(-69.81%)</b></td><td>607.90 <b>(-22.52%)</b></td><td>490.88 (+9.79%)</td><td>466.30 <b>(+42.12%)</b></td><td>428.20 <b>(+52.17%)</b></td><td>75.73 <b>(-64.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>784.60 (n/a)</td><td>447.12 (n/a)</td><td>328.10 (n/a)</td><td>281.40 (n/a)</td><td>213.35 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-15.22%)</td><td>0.01 (-11.05%)</td><td>0.01 (+6.43%)</td><td>0.01 (+7.60%)</td><td>0.00 <b>(-39.30%)</b></td><td>526.20 (-7.06%)</td><td>418.14 (+2.68%)</td><td>424.20 (-6.05%)</td><td>258.20 (+17.95%)</td><td>102.94 <b>(-36.15%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.20 (n/a)</td><td>407.22 (n/a)</td><td>451.50 (n/a)</td><td>218.90 (n/a)</td><td>161.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-5.00%)</td><td>0.01 (-5.62%)</td><td>0.01 (-10.15%)</td><td>0.01 (-3.16%)</td><td>0.01 (+0.68%)</td><td>516.20 (+3.26%)</td><td>400.26 (+7.06%)</td><td>471.40 (+11.31%)</td><td>257.60 (+5.27%)</td><td>128.49 (+11.14%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>373.88 (n/a)</td><td>423.50 (n/a)</td><td>244.70 (n/a)</td><td>115.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-0.84%)</td><td>0.02 <b>(+24.14%)</b></td><td>0.02 <b>(+64.94%)</b></td><td>0.01 <b>(+35.81%)</b></td><td>0.00 <b>(-30.37%)</b></td><td>457.00 <b>(-26.36%)</b></td><td>294.32 <b>(-26.60%)</b></td><td>273.00 <b>(-39.37%)</b></td><td>224.60 (+0.85%)</td><td>95.03 <b>(-43.58%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>400.96 (n/a)</td><td>450.30 (n/a)</td><td>222.70 (n/a)</td><td>168.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-2.47%)</td><td>0.02 <b>(+25.58%)</b></td><td>0.02 <b>(+71.85%)</b></td><td>0.01 <b>(+61.03%)</b></td><td>0.00 (-15.21%)</td><td>486.10 <b>(-37.90%)</b></td><td>356.20 <b>(-25.76%)</b></td><td>282.20 <b>(-41.81%)</b></td><td>270.60 (+2.54%)</td><td>111.20 <b>(-45.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>782.80 (n/a)</td><td>479.78 (n/a)</td><td>485.00 (n/a)</td><td>263.90 (n/a)</td><td>202.52 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+37.52%)</b></td><td>0.02 <b>(+42.71%)</b></td><td>0.02 <b>(+74.54%)</b></td><td>0.01 (+7.01%)</td><td>0.01 <b>(+95.04%)</b></td><td>579.30 (-6.55%)</td><td>370.72 <b>(-25.22%)</b></td><td>271.00 <b>(-42.71%)</b></td><td>256.20 <b>(-27.28%)</b></td><td>148.14 <b>(+23.20%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.90 (n/a)</td><td>495.72 (n/a)</td><td>473.00 (n/a)</td><td>352.30 (n/a)</td><td>120.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+16.50%)</td><td>0.01 (+9.72%)</td><td>0.01 (-3.34%)</td><td>0.01 (+18.85%)</td><td>0.00 <b>(+20.06%)</b></td><td>529.60 (-15.86%)</td><td>425.80 (-8.44%)</td><td>486.60 (+3.44%)</td><td>297.10 (-14.16%)</td><td>107.85 (-10.25%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.40 (n/a)</td><td>465.06 (n/a)</td><td>470.40 (n/a)</td><td>346.10 (n/a)</td><td>120.16 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (+0.98%)</td><td>0.03 (+0.56%)</td><td>0.03 (-3.26%)</td><td>0.02 (-4.29%)</td><td>0.01 (-9.82%)</td><td>556.40 (+4.49%)</td><td>358.62 (-2.81%)</td><td>333.60 (+3.38%)</td><td>231.30 (-0.98%)</td><td>131.34 (-9.27%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.50 (n/a)</td><td>369.00 (n/a)</td><td>322.70 (n/a)</td><td>233.60 (n/a)</td><td>144.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 <b>(-23.43%)</b></td><td>0.04 (-9.17%)</td><td>0.04 (-0.97%)</td><td>0.02 (-12.45%)</td><td>0.01 <b>(-20.91%)</b></td><td>536.50 (+14.20%)</td><td>320.98 (+9.71%)</td><td>274.70 (+0.99%)</td><td>245.00 <b>(+30.60%)</b></td><td>122.24 (+16.21%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.80 (n/a)</td><td>292.58 (n/a)</td><td>272.00 (n/a)</td><td>187.60 (n/a)</td><td>105.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-3.53%)</td><td>0.03 (-18.78%)</td><td>0.02 <b>(-57.01%)</b></td><td>0.02 (-0.31%)</td><td>0.01 (+4.55%)</td><td>584.90 (+0.31%)</td><td>438.48 <b>(+26.48%)</b></td><td>562.60 <b>(+132.58%)</b></td><td>232.60 (+3.65%)</td><td>182.13 (+12.93%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>346.68 (n/a)</td><td>241.90 (n/a)</td><td>224.40 (n/a)</td><td>161.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (-10.73%)</td><td>0.04 (+17.46%)</td><td>0.04 <b>(+74.73%)</b></td><td>0.02 <b>(+22.64%)</b></td><td>0.01 <b>(-39.52%)</b></td><td>482.80 (-18.46%)</td><td>317.04 <b>(-24.77%)</b></td><td>289.80 <b>(-42.77%)</b></td><td>234.50 (+12.04%)</td><td>100.58 <b>(-44.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>592.10 (n/a)</td><td>421.44 (n/a)</td><td>506.40 (n/a)</td><td>209.30 (n/a)</td><td>181.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (+13.59%)</td><td>0.03 (-1.23%)</td><td>0.03 <b>(-24.29%)</b></td><td>0.02 <b>(+20.74%)</b></td><td>0.01 (-9.95%)</td><td>498.00 (-17.18%)</td><td>385.60 (-4.40%)</td><td>399.10 <b>(+32.11%)</b></td><td>229.40 (-11.97%)</td><td>99.74 <b>(-39.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.30 (n/a)</td><td>403.34 (n/a)</td><td>302.10 (n/a)</td><td>260.60 (n/a)</td><td>165.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 <b>(-21.83%)</b></td><td>0.02 (-5.99%)</td><td>0.02 (-0.27%)</td><td>0.02 (-2.43%)</td><td>0.01 <b>(-37.23%)</b></td><td>671.10 (+2.49%)</td><td>483.44 (+2.72%)</td><td>482.40 (+0.27%)</td><td>354.40 <b>(+27.94%)</b></td><td>119.42 (-13.32%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>654.80 (n/a)</td><td>470.66 (n/a)</td><td>481.10 (n/a)</td><td>277.00 (n/a)</td><td>137.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (+11.46%)</td><td>0.05 (+19.51%)</td><td>0.05 <b>(+25.32%)</b></td><td>0.03 (+8.94%)</td><td>0.02 <b>(+27.87%)</b></td><td>631.50 (-8.21%)</td><td>425.74 (-14.38%)</td><td>408.40 <b>(-20.20%)</b></td><td>282.10 (-10.27%)</td><td>143.61 (+5.72%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>688.00 (n/a)</td><td>497.22 (n/a)</td><td>511.80 (n/a)</td><td>314.40 (n/a)</td><td>135.84 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (-5.70%)</td><td>0.07 (+13.73%)</td><td>0.07 <b>(+55.00%)</b></td><td>0.05 (+11.99%)</td><td>0.02 <b>(-30.64%)</b></td><td>457.00 (-10.71%)</td><td>319.80 (-17.19%)</td><td>281.00 <b>(-35.49%)</b></td><td>233.70 (+6.03%)</td><td>87.12 <b>(-33.95%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>511.80 (n/a)</td><td>386.20 (n/a)</td><td>435.60 (n/a)</td><td>220.40 (n/a)</td><td>131.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-7.86%)</td><td>0.05 (-7.69%)</td><td>0.04 <b>(-24.25%)</b></td><td>0.03 <b>(+26.69%)</b></td><td>0.02 <b>(-20.79%)</b></td><td>647.40 <b>(-21.07%)</b></td><td>443.98 (-0.35%)</td><td>490.80 <b>(+32.04%)</b></td><td>275.70 (+8.54%)</td><td>159.42 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>820.20 (n/a)</td><td>445.52 (n/a)</td><td>371.70 (n/a)</td><td>254.00 (n/a)</td><td>237.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (+11.07%)</td><td>0.07 <b>(+46.77%)</b></td><td>0.07 <b>(+78.51%)</b></td><td>0.04 (+5.78%)</td><td>0.02 (+3.41%)</td><td>567.70 (-5.46%)</td><td>336.70 <b>(-32.05%)</b></td><td>291.30 <b>(-43.97%)</b></td><td>229.00 (-9.95%)</td><td>135.06 (-4.11%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.50 (n/a)</td><td>495.50 (n/a)</td><td>519.90 (n/a)</td><td>254.30 (n/a)</td><td>140.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (-1.05%)</td><td>0.06 (+4.17%)</td><td>0.06 (-17.67%)</td><td>0.03 <b>(+210.73%)</b></td><td>0.02 <b>(-27.93%)</b></td><td>611.20 <b>(-67.82%)</b></td><td>399.98 <b>(-38.53%)</b></td><td>364.70 <b>(+21.49%)</b></td><td>230.20 (+1.05%)</td><td>156.69 <b>(-77.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1899.40 (n/a)</td><td>650.70 (n/a)</td><td>300.20 (n/a)</td><td>227.80 (n/a)</td><td>708.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-13.90%)</td><td>0.05 (+12.15%)</td><td>0.04 <b>(+23.29%)</b></td><td>0.03 (+3.69%)</td><td>0.02 (-18.11%)</td><td>641.30 (-3.56%)</td><td>475.78 (-13.35%)</td><td>503.60 (-18.89%)</td><td>281.00 (+16.12%)</td><td>170.74 (-2.55%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>665.00 (n/a)</td><td>549.10 (n/a)</td><td>620.90 (n/a)</td><td>242.00 (n/a)</td><td>175.21 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.90 (n/a)</td><td>339.24 (n/a)</td><td>290.60 (n/a)</td><td>187.30 (n/a)</td><td>170.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.30 (n/a)</td><td>401.92 (n/a)</td><td>445.60 (n/a)</td><td>283.90 (n/a)</td><td>105.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.10 (n/a)</td><td>371.20 (n/a)</td><td>254.70 (n/a)</td><td>230.30 (n/a)</td><td>181.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.80 (n/a)</td><td>392.32 (n/a)</td><td>386.30 (n/a)</td><td>291.90 (n/a)</td><td>85.95 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>447.80 (n/a)</td><td>318.30 (n/a)</td><td>279.40 (n/a)</td><td>248.80 (n/a)</td><td>86.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>617.10 (n/a)</td><td>440.48 (n/a)</td><td>464.30 (n/a)</td><td>228.20 (n/a)</td><td>173.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>347.40 (n/a)</td><td>270.96 (n/a)</td><td>271.60 (n/a)</td><td>194.70 (n/a)</td><td>58.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>433.80 (n/a)</td><td>302.80 (n/a)</td><td>242.70 (n/a)</td><td>196.40 (n/a)</td><td>108.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>294.50 (n/a)</td><td>276.74 (n/a)</td><td>280.50 (n/a)</td><td>247.40 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (+10.27%)</td><td>0.17 <b>(+20.29%)</b></td><td>0.18 <b>(+20.43%)</b></td><td>0.10 <b>(+72.58%)</b></td><td>0.04 (-17.17%)</td><td>469.20 <b>(-42.06%)</b></td><td>314.02 <b>(-24.67%)</b></td><td>276.90 (-16.95%)</td><td>240.30 (-9.32%)</td><td>92.86 <b>(-58.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>809.80 (n/a)</td><td>416.88 (n/a)</td><td>333.40 (n/a)</td><td>265.00 (n/a)</td><td>223.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>572.30 (n/a)</td><td>408.06 (n/a)</td><td>352.80 (n/a)</td><td>248.30 (n/a)</td><td>144.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>563.80 (n/a)</td><td>431.38 (n/a)</td><td>440.30 (n/a)</td><td>241.90 (n/a)</td><td>118.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>395.24 (n/a)</td><td>424.00 (n/a)</td><td>280.20 (n/a)</td><td>101.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.60 (n/a)</td><td>435.56 (n/a)</td><td>490.20 (n/a)</td><td>269.80 (n/a)</td><td>155.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.40 (n/a)</td><td>468.06 (n/a)</td><td>505.40 (n/a)</td><td>279.60 (n/a)</td><td>121.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1880.60 (n/a)</td><td>589.38 (n/a)</td><td>277.20 (n/a)</td><td>244.70 (n/a)</td><td>722.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>541.60 (n/a)</td><td>348.70 (n/a)</td><td>258.20 (n/a)</td><td>195.10 (n/a)</td><td>157.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.70 (n/a)</td><td>365.74 (n/a)</td><td>296.50 (n/a)</td><td>275.70 (n/a)</td><td>114.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>684.60 (n/a)</td><td>440.54 (n/a)</td><td>480.20 (n/a)</td><td>256.80 (n/a)</td><td>175.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>612.10 (n/a)</td><td>424.84 (n/a)</td><td>471.90 (n/a)</td><td>201.00 (n/a)</td><td>193.94 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>524.10 (n/a)</td><td>379.90 (n/a)</td><td>409.30 (n/a)</td><td>245.10 (n/a)</td><td>114.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>609.40 (n/a)</td><td>429.28 (n/a)</td><td>505.40 (n/a)</td><td>243.70 (n/a)</td><td>165.47 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>538.60 (n/a)</td><td>375.74 (n/a)</td><td>331.00 (n/a)</td><td>234.70 (n/a)</td><td>148.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.98 <b>(+31.56%)</b></td><td>2.80 (+5.22%)</td><td>2.59 (-6.44%)</td><td>1.73 <b>(-26.11%)</b></td><td>1.12 <b>(+288.98%)</b></td><td>6047.30 <b>(+35.34%)</b></td><td>4281.42 (+7.63%)</td><td>4052.40 (+6.88%)</td><td>2636.60 <b>(-23.99%)</b></td><td>1701.67 <b>(+291.22%)</b></td><td>1628.99 <b>(+31.56%)</b></td><td>1146.92 (+5.22%)</td><td>1059.86 (-6.44%)</td><td>710.23 <b>(-26.11%)</b></td><td>459.65 <b>(+288.98%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.02 (n/a)</td><td>2.66 (n/a)</td><td>2.77 (n/a)</td><td>2.35 (n/a)</td><td>0.29 (n/a)</td><td>4468.10 (n/a)</td><td>3977.92 (n/a)</td><td>3791.40 (n/a)</td><td>3468.80 (n/a)</td><td>434.97 (n/a)</td><td>1238.17 (n/a)</td><td>1090.02 (n/a)</td><td>1132.82 (n/a)</td><td>961.26 (n/a)</td><td>118.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.73 (-0.15%)</td><td>3.31 (+5.95%)</td><td>3.64 (+14.29%)</td><td>2.68 (+6.52%)</td><td>0.52 (+17.72%)</td><td>8789.80 (-6.12%)</td><td>7272.46 (-5.17%)</td><td>6484.90 (-12.50%)</td><td>6333.50 (+0.15%)</td><td>1209.67 (+8.55%)</td><td>2119.17 (-0.15%)</td><td>1884.74 (+5.95%)</td><td>2069.69 (+14.29%)</td><td>1526.98 (+6.52%)</td><td>294.57 (+17.72%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.73 (n/a)</td><td>3.13 (n/a)</td><td>3.18 (n/a)</td><td>2.52 (n/a)</td><td>0.44 (n/a)</td><td>9362.60 (n/a)</td><td>7668.92 (n/a)</td><td>7411.50 (n/a)</td><td>6324.10 (n/a)</td><td>1114.40 (n/a)</td><td>2122.32 (n/a)</td><td>1778.96 (n/a)</td><td>1810.94 (n/a)</td><td>1433.55 (n/a)</td><td>250.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.04 <b>(+26.35%)</b></td><td>3.23 <b>(+22.95%)</b></td><td>3.09 (+11.38%)</td><td>2.34 (+9.57%)</td><td>0.66 <b>(+42.94%)</b></td><td>7158.00 (-8.73%)</td><td>5380.72 (-17.84%)</td><td>5428.20 (-10.22%)</td><td>4155.40 <b>(-20.85%)</b></td><td>1171.18 (-1.06%)</td><td>2067.17 <b>(+26.35%)</b></td><td>1654.72 <b>(+22.95%)</b></td><td>1582.47 (+11.38%)</td><td>1200.05 (+9.57%)</td><td>339.77 <b>(+42.94%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.20 (n/a)</td><td>2.63 (n/a)</td><td>2.77 (n/a)</td><td>2.14 (n/a)</td><td>0.46 (n/a)</td><td>7842.90 (n/a)</td><td>6548.80 (n/a)</td><td>6046.10 (n/a)</td><td>5250.30 (n/a)</td><td>1183.71 (n/a)</td><td>1636.09 (n/a)</td><td>1345.90 (n/a)</td><td>1420.74 (n/a)</td><td>1095.25 (n/a)</td><td>237.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.87 (-0.77%)</td><td>0.75 <b>(+29.29%)</b></td><td>0.73 (+18.63%)</td><td>0.64 <b>(+149.73%)</b></td><td>0.10 <b>(-57.58%)</b></td><td>717.00 <b>(-59.96%)</b></td><td>624.00 <b>(-34.16%)</b></td><td>624.80 (-15.70%)</td><td>524.30 (+0.79%)</td><td>81.87 <b>(-83.68%)</b></td><td>64.00 (-0.77%)</td><td>54.53 <b>(+29.29%)</b></td><td>53.70 (+18.63%)</td><td>46.80 <b>(+149.73%)</b></td><td>7.27 <b>(-57.58%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.88 (n/a)</td><td>0.58 (n/a)</td><td>0.62 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>1790.60 (n/a)</td><td>947.78 (n/a)</td><td>741.20 (n/a)</td><td>520.20 (n/a)</td><td>501.62 (n/a)</td><td>64.50 (n/a)</td><td>42.18 (n/a)</td><td>45.27 (n/a)</td><td>18.74 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.53 (+17.76%)</td><td>1.14 (+5.78%)</td><td>1.15 (-1.40%)</td><td>0.71 (-15.37%)</td><td>0.31 <b>(+60.33%)</b></td><td>919.80 (+18.15%)</td><td>614.20 (-1.55%)</td><td>568.60 (+1.43%)</td><td>428.00 (-15.08%)</td><td>190.89 <b>(+61.50%)</b></td><td>156.79 (+17.76%)</td><td>116.97 (+5.78%)</td><td>118.03 (-1.40%)</td><td>72.96 (-15.37%)</td><td>31.91 <b>(+60.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.30 (n/a)</td><td>1.08 (n/a)</td><td>1.17 (n/a)</td><td>0.84 (n/a)</td><td>0.19 (n/a)</td><td>778.50 (n/a)</td><td>623.84 (n/a)</td><td>560.60 (n/a)</td><td>504.00 (n/a)</td><td>118.20 (n/a)</td><td>133.14 (n/a)</td><td>110.58 (n/a)</td><td>119.71 (n/a)</td><td>86.21 (n/a)</td><td>19.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.68 (+5.53%)</td><td>1.29 (-0.46%)</td><td>1.20 (-7.68%)</td><td>1.05 (+0.77%)</td><td>0.25 (+19.36%)</td><td>719.20 (-0.76%)</td><td>599.20 (+1.12%)</td><td>626.50 (+8.32%)</td><td>448.80 (-5.24%)</td><td>104.81 (+10.48%)</td><td>186.91 (+5.53%)</td><td>143.83 (-0.46%)</td><td>133.91 (-7.68%)</td><td>116.65 (+0.77%)</td><td>27.61 (+19.36%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.59 (n/a)</td><td>1.30 (n/a)</td><td>1.30 (n/a)</td><td>1.04 (n/a)</td><td>0.21 (n/a)</td><td>724.70 (n/a)</td><td>592.56 (n/a)</td><td>578.40 (n/a)</td><td>473.60 (n/a)</td><td>94.87 (n/a)</td><td>177.11 (n/a)</td><td>144.50 (n/a)</td><td>145.04 (n/a)</td><td>115.75 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.63 (+10.01%)</td><td>0.88 <b>(-23.49%)</b></td><td>0.47 <b>(-61.59%)</b></td><td>0.30 <b>(-38.46%)</b></td><td>0.66 <b>(+67.82%)</b></td><td>3525.30 <b>(+62.49%)</b></td><td>1885.92 <b>(+75.58%)</b></td><td>2254.80 <b>(+160.37%)</b></td><td>642.50 (-9.10%)</td><td>1230.58 <b>(+99.63%)</b></td><td>208.91 (+10.01%)</td><td>112.94 <b>(-23.49%)</b></td><td>59.53 <b>(-61.59%)</b></td><td>38.07 <b>(-38.46%)</b></td><td>84.38 <b>(+67.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.48 (n/a)</td><td>1.15 (n/a)</td><td>1.21 (n/a)</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>2169.60 (n/a)</td><td>1074.10 (n/a)</td><td>866.00 (n/a)</td><td>706.80 (n/a)</td><td>616.43 (n/a)</td><td>189.89 (n/a)</td><td>147.62 (n/a)</td><td>154.99 (n/a)</td><td>61.86 (n/a)</td><td>50.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.40 (-19.59%)</td><td>1.09 (-16.42%)</td><td>1.29 (-3.72%)</td><td>0.63 <b>(+48.54%)</b></td><td>0.35 <b>(-34.57%)</b></td><td>1672.70 <b>(-32.68%)</b></td><td>1065.44 (+0.76%)</td><td>815.30 (+3.87%)</td><td>751.40 <b>(+24.36%)</b></td><td>408.07 <b>(-49.21%)</b></td><td>178.63 (-19.59%)</td><td>139.53 (-16.42%)</td><td>164.63 (-3.72%)</td><td>80.24 <b>(+48.54%)</b></td><td>44.77 <b>(-34.57%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.74 (n/a)</td><td>1.30 (n/a)</td><td>1.34 (n/a)</td><td>0.42 (n/a)</td><td>0.53 (n/a)</td><td>2484.60 (n/a)</td><td>1057.36 (n/a)</td><td>784.90 (n/a)</td><td>604.20 (n/a)</td><td>803.48 (n/a)</td><td>222.13 (n/a)</td><td>166.94 (n/a)</td><td>170.99 (n/a)</td><td>54.02 (n/a)</td><td>68.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.33 (+16.34%)</td><td>1.75 <b>(+35.78%)</b></td><td>1.82 <b>(+27.88%)</b></td><td>1.30 <b>(+129.13%)</b></td><td>0.44 <b>(-35.46%)</b></td><td>808.80 <b>(-56.35%)</b></td><td>632.90 <b>(-42.44%)</b></td><td>577.30 <b>(-21.81%)</b></td><td>449.60 (-14.05%)</td><td>162.14 <b>(-76.10%)</b></td><td>298.50 (+16.34%)</td><td>223.58 <b>(+35.78%)</b></td><td>232.48 <b>(+27.88%)</b></td><td>165.95 <b>(+129.13%)</b></td><td>56.84 <b>(-35.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.00 (n/a)</td><td>1.29 (n/a)</td><td>1.42 (n/a)</td><td>0.57 (n/a)</td><td>0.69 (n/a)</td><td>1853.10 (n/a)</td><td>1099.56 (n/a)</td><td>738.30 (n/a)</td><td>523.10 (n/a)</td><td>678.37 (n/a)</td><td>256.58 (n/a)</td><td>164.67 (n/a)</td><td>181.80 (n/a)</td><td>72.43 (n/a)</td><td>88.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.83 (-3.32%)</td><td>1.36 (+5.79%)</td><td>1.16 (-18.10%)</td><td>0.97 <b>(+124.79%)</b></td><td>0.38 <b>(-28.99%)</b></td><td>1081.20 <b>(-55.51%)</b></td><td>820.28 <b>(-22.64%)</b></td><td>903.60 <b>(+22.11%)</b></td><td>571.90 (+3.42%)</td><td>216.81 <b>(-71.96%)</b></td><td>234.68 (-3.32%)</td><td>173.82 (+5.79%)</td><td>148.53 (-18.10%)</td><td>124.14 <b>(+124.79%)</b></td><td>48.67 <b>(-28.99%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.90 (n/a)</td><td>1.28 (n/a)</td><td>1.42 (n/a)</td><td>0.43 (n/a)</td><td>0.54 (n/a)</td><td>2430.40 (n/a)</td><td>1060.36 (n/a)</td><td>740.00 (n/a)</td><td>553.00 (n/a)</td><td>773.26 (n/a)</td><td>242.73 (n/a)</td><td>164.31 (n/a)</td><td>181.37 (n/a)</td><td>55.23 (n/a)</td><td>68.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.97 <b>(+33.83%)</b></td><td>1.15 (-2.40%)</td><td>1.17 (-3.93%)</td><td>0.50 <b>(-38.69%)</b></td><td>0.57 <b>(+130.25%)</b></td><td>2115.60 <b>(+63.09%)</b></td><td>1145.20 <b>(+23.21%)</b></td><td>899.70 (+4.08%)</td><td>533.10 <b>(-25.27%)</b></td><td>630.03 <b>(+179.96%)</b></td><td>251.79 <b>(+33.83%)</b></td><td>146.85 (-2.40%)</td><td>149.18 (-3.93%)</td><td>63.44 <b>(-38.69%)</b></td><td>73.15 <b>(+130.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.47 (n/a)</td><td>1.18 (n/a)</td><td>1.21 (n/a)</td><td>0.81 (n/a)</td><td>0.25 (n/a)</td><td>1297.20 (n/a)</td><td>929.44 (n/a)</td><td>864.40 (n/a)</td><td>713.40 (n/a)</td><td>225.04 (n/a)</td><td>188.14 (n/a)</td><td>150.46 (n/a)</td><td>155.28 (n/a)</td><td>103.47 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.76 (+4.55%)</td><td>1.44 (+2.22%)</td><td>1.58 (+7.22%)</td><td>1.04 (+1.26%)</td><td>0.32 <b>(+27.44%)</b></td><td>1010.60 (-1.24%)</td><td>761.72 (-0.73%)</td><td>665.40 (-6.73%)</td><td>595.90 (-4.35%)</td><td>184.34 (+18.05%)</td><td>225.25 (+4.55%)</td><td>184.09 (+2.22%)</td><td>201.72 (+7.22%)</td><td>132.81 (+1.26%)</td><td>40.95 <b>(+27.44%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.68 (n/a)</td><td>1.41 (n/a)</td><td>1.47 (n/a)</td><td>1.02 (n/a)</td><td>0.25 (n/a)</td><td>1023.30 (n/a)</td><td>767.30 (n/a)</td><td>713.40 (n/a)</td><td>623.00 (n/a)</td><td>156.16 (n/a)</td><td>215.44 (n/a)</td><td>180.10 (n/a)</td><td>188.14 (n/a)</td><td>131.16 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.89 <b>(+32.05%)</b></td><td>0.58 (+11.96%)</td><td>0.51 (-12.73%)</td><td>0.43 <b>(+192.97%)</b></td><td>0.19 (-14.96%)</td><td>833.40 <b>(-65.87%)</b></td><td>666.94 <b>(-31.25%)</b></td><td>713.40 (+14.58%)</td><td>404.50 <b>(-24.27%)</b></td><td>168.73 <b>(-79.57%)</b></td><td>41.48 <b>(+32.05%)</b></td><td>26.87 (+11.96%)</td><td>23.52 (-12.73%)</td><td>20.13 <b>(+192.97%)</b></td><td>8.63 (-14.96%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.67 (n/a)</td><td>0.52 (n/a)</td><td>0.58 (n/a)</td><td>0.15 (n/a)</td><td>0.22 (n/a)</td><td>2441.60 (n/a)</td><td>970.06 (n/a)</td><td>622.60 (n/a)</td><td>534.10 (n/a)</td><td>826.09 (n/a)</td><td>31.41 (n/a)</td><td>24.00 (n/a)</td><td>26.95 (n/a)</td><td>6.87 (n/a)</td><td>10.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.11 (+2.34%)</td><td>2.14 (+11.83%)</td><td>1.89 (-7.90%)</td><td>0.99 (+0.78%)</td><td>0.87 (-2.53%)</td><td>4240.00 (-0.77%)</td><td>2311.88 (-13.68%)</td><td>2213.80 (+8.58%)</td><td>1348.50 (-2.29%)</td><td>1163.57 (-13.85%)</td><td>796.25 (+2.34%)</td><td>548.71 (+11.83%)</td><td>485.03 (-7.90%)</td><td>253.24 (+0.78%)</td><td>222.87 (-2.53%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.04 (n/a)</td><td>1.92 (n/a)</td><td>2.06 (n/a)</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>4273.10 (n/a)</td><td>2678.24 (n/a)</td><td>2038.90 (n/a)</td><td>1380.10 (n/a)</td><td>1350.56 (n/a)</td><td>778.02 (n/a)</td><td>490.64 (n/a)</td><td>526.63 (n/a)</td><td>251.28 (n/a)</td><td>228.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.88 (+7.46%)</td><td>2.71 (-14.95%)</td><td>3.58 (-0.11%)</td><td>1.16 <b>(-44.01%)</b></td><td>1.39 <b>(+108.39%)</b></td><td>2268.70 <b>(+78.58%)</b></td><td>1306.14 <b>(+51.40%)</b></td><td>732.70 (+0.11%)</td><td>675.30 (-6.93%)</td><td>823.65 <b>(+251.23%)</b></td><td>795.05 (+7.46%)</td><td>554.39 (-14.95%)</td><td>732.71 (-0.11%)</td><td>236.64 <b>(-44.01%)</b></td><td>284.74 <b>(+108.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.61 (n/a)</td><td>3.18 (n/a)</td><td>3.58 (n/a)</td><td>2.06 (n/a)</td><td>0.67 (n/a)</td><td>1270.40 (n/a)</td><td>862.68 (n/a)</td><td>731.90 (n/a)</td><td>725.60 (n/a)</td><td>234.50 (n/a)</td><td>739.85 (n/a)</td><td>651.83 (n/a)</td><td>733.49 (n/a)</td><td>422.61 (n/a)</td><td>136.64 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.92 (+2.37%)</td><td>2.18 (-8.52%)</td><td>2.04 <b>(-25.14%)</b></td><td>1.51 (-8.04%)</td><td>0.63 (+8.96%)</td><td>5197.30 (+8.74%)</td><td>3851.12 (+10.76%)</td><td>3859.10 <b>(+33.59%)</b></td><td>2690.60 (-2.32%)</td><td>1089.55 (+16.13%)</td><td>897.92 (+2.37%)</td><td>670.35 (-8.52%)</td><td>626.04 <b>(-25.14%)</b></td><td>464.84 (-8.04%)</td><td>192.35 (+8.96%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.86 (n/a)</td><td>2.39 (n/a)</td><td>2.72 (n/a)</td><td>1.65 (n/a)</td><td>0.57 (n/a)</td><td>4779.50 (n/a)</td><td>3476.90 (n/a)</td><td>2888.70 (n/a)</td><td>2754.40 (n/a)</td><td>938.25 (n/a)</td><td>877.12 (n/a)</td><td>732.81 (n/a)</td><td>836.32 (n/a)</td><td>505.47 (n/a)</td><td>176.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>703.40 (n/a)</td><td>449.88 (n/a)</td><td>409.20 (n/a)</td><td>299.60 (n/a)</td><td>168.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2467.60 (n/a)</td><td>808.40 (n/a)</td><td>470.80 (n/a)</td><td>216.10 (n/a)</td><td>941.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.50 (n/a)</td><td>357.90 (n/a)</td><td>250.80 (n/a)</td><td>196.20 (n/a)</td><td>181.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>527.40 (n/a)</td><td>335.14 (n/a)</td><td>301.10 (n/a)</td><td>173.80 (n/a)</td><td>136.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>328.68 (n/a)</td><td>267.80 (n/a)</td><td>161.00 (n/a)</td><td>148.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1815.70 (n/a)</td><td>697.66 (n/a)</td><td>442.10 (n/a)</td><td>297.60 (n/a)</td><td>632.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.40 (n/a)</td><td>403.40 (n/a)</td><td>305.80 (n/a)</td><td>240.00 (n/a)</td><td>188.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.70 (n/a)</td><td>470.16 (n/a)</td><td>521.30 (n/a)</td><td>244.60 (n/a)</td><td>136.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.30 (n/a)</td><td>390.80 (n/a)</td><td>307.40 (n/a)</td><td>269.60 (n/a)</td><td>134.50 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.80 (n/a)</td><td>385.68 (n/a)</td><td>380.70 (n/a)</td><td>251.50 (n/a)</td><td>128.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>385.68 (n/a)</td><td>400.60 (n/a)</td><td>246.10 (n/a)</td><td>129.97 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>677.60 (n/a)</td><td>522.98 (n/a)</td><td>487.20 (n/a)</td><td>364.70 (n/a)</td><td>142.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2015.30 (n/a)</td><td>1011.02 (n/a)</td><td>548.30 (n/a)</td><td>266.70 (n/a)</td><td>886.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>663.80 (n/a)</td><td>460.50 (n/a)</td><td>400.30 (n/a)</td><td>257.80 (n/a)</td><td>166.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.00 (n/a)</td><td>541.20 (n/a)</td><td>636.70 (n/a)</td><td>236.90 (n/a)</td><td>176.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.50 (n/a)</td><td>453.92 (n/a)</td><td>570.80 (n/a)</td><td>247.40 (n/a)</td><td>180.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.00 (n/a)</td><td>423.50 (n/a)</td><td>462.60 (n/a)</td><td>248.80 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>395.56 (n/a)</td><td>357.00 (n/a)</td><td>254.80 (n/a)</td><td>138.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>593.80 (n/a)</td><td>415.50 (n/a)</td><td>350.90 (n/a)</td><td>299.30 (n/a)</td><td>137.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.20 (n/a)</td><td>421.24 (n/a)</td><td>452.30 (n/a)</td><td>256.50 (n/a)</td><td>132.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>579.70 (n/a)</td><td>374.84 (n/a)</td><td>321.10 (n/a)</td><td>253.60 (n/a)</td><td>141.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>821.40 (n/a)</td><td>507.36 (n/a)</td><td>559.20 (n/a)</td><td>265.00 (n/a)</td><td>226.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>660.70 (n/a)</td><td>507.54 (n/a)</td><td>521.50 (n/a)</td><td>310.80 (n/a)</td><td>137.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.30 (n/a)</td><td>414.12 (n/a)</td><td>477.70 (n/a)</td><td>214.50 (n/a)</td><td>148.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.49 (-4.64%)</td><td>0.34 (-12.30%)</td><td>0.41 <b>(+20.69%)</b></td><td>0.13 <b>(-56.42%)</b></td><td>0.16 <b>(+72.03%)</b></td><td>1681.40 <b>(+129.48%)</b></td><td>853.02 <b>(+42.76%)</b></td><td>538.80 (-17.13%)</td><td>453.80 (+4.85%)</td><td>539.98 <b>(+295.40%)</b></td><td>20.79 (-4.64%)</td><td>14.50 (-12.30%)</td><td>17.52 <b>(+20.69%)</b></td><td>5.61 <b>(-56.42%)</b></td><td>7.02 <b>(+72.03%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>732.70 (n/a)</td><td>597.52 (n/a)</td><td>650.20 (n/a)</td><td>432.80 (n/a)</td><td>136.57 (n/a)</td><td>21.81 (n/a)</td><td>16.54 (n/a)</td><td>14.51 (n/a)</td><td>12.88 (n/a)</td><td>4.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.47 (-18.85%)</td><td>0.32 <b>(-23.28%)</b></td><td>0.33 <b>(-23.50%)</b></td><td>0.13 <b>(-39.95%)</b></td><td>0.12 (-19.10%)</td><td>1669.90 <b>(+66.52%)</b></td><td>826.12 <b>(+37.68%)</b></td><td>665.70 <b>(+30.73%)</b></td><td>468.30 <b>(+23.24%)</b></td><td>479.34 <b>(+86.87%)</b></td><td>20.15 (-18.85%)</td><td>13.69 <b>(-23.28%)</b></td><td>14.18 <b>(-23.50%)</b></td><td>5.65 <b>(-39.95%)</b></td><td>5.18 (-19.10%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.58 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>1002.80 (n/a)</td><td>600.02 (n/a)</td><td>509.20 (n/a)</td><td>380.00 (n/a)</td><td>256.51 (n/a)</td><td>24.84 (n/a)</td><td>17.84 (n/a)</td><td>18.53 (n/a)</td><td>9.41 (n/a)</td><td>6.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.31 (-2.29%)</td><td>0.30 (-1.69%)</td><td>0.30 (-1.90%)</td><td>0.30 (-1.02%)</td><td>0.00 <b>(-27.53%)</b></td><td>84518.30 (+1.03%)</td><td>83051.94 (+1.71%)</td><td>82814.90 (+1.93%)</td><td>82081.00 (+2.34%)</td><td>999.37 <b>(-25.18%)</b></td><td>209.30 (-2.29%)</td><td>206.88 (-1.69%)</td><td>207.45 (-1.90%)</td><td>203.27 (-1.02%)</td><td>2.48 <b>(-27.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>83656.10 (n/a)</td><td>81655.92 (n/a)</td><td>81244.30 (n/a)</td><td>80202.40 (n/a)</td><td>1335.73 (n/a)</td><td>214.21 (n/a)</td><td>210.44 (n/a)</td><td>211.46 (n/a)</td><td>205.36 (n/a)</td><td>3.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.15 (-0.01%)</td><td>1.14 (+1.29%)</td><td>1.14 (+0.32%)</td><td>1.12 (+5.56%)</td><td>0.01 <b>(-67.81%)</b></td><td>22478.20 (-5.26%)</td><td>22118.24 (-1.35%)</td><td>21988.30 (-0.32%)</td><td>21958.40 (+0.01%)</td><td>225.98 <b>(-69.63%)</b></td><td>782.38 (-0.01%)</td><td>776.79 (+1.29%)</td><td>781.32 (+0.32%)</td><td>764.29 (+5.56%)</td><td>7.87 <b>(-67.81%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>1.14 (n/a)</td><td>1.06 (n/a)</td><td>0.04 (n/a)</td><td>23727.10 (n/a)</td><td>22421.32 (n/a)</td><td>22057.80 (n/a)</td><td>21957.10 (n/a)</td><td>743.99 (n/a)</td><td>782.43 (n/a)</td><td>766.88 (n/a)</td><td>778.86 (n/a)</td><td>724.06 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.81 (+2.22%)</td><td>0.80 (+1.98%)</td><td>0.80 (+1.32%)</td><td>0.79 (+2.89%)</td><td>0.00 <b>(-31.91%)</b></td><td>95156.40 (-2.81%)</td><td>94620.74 (-1.95%)</td><td>94867.50 (-1.31%)</td><td>93777.50 (-2.17%)</td><td>559.27 <b>(-35.26%)</b></td><td>732.79 (+2.22%)</td><td>726.28 (+1.98%)</td><td>724.37 (+1.32%)</td><td>722.17 (+2.89%)</td><td>4.31 <b>(-31.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97906.40 (n/a)</td><td>96502.08 (n/a)</td><td>96122.80 (n/a)</td><td>95856.90 (n/a)</td><td>863.93 (n/a)</td><td>716.90 (n/a)</td><td>712.15 (n/a)</td><td>714.91 (n/a)</td><td>701.89 (n/a)</td><td>6.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.78 (+0.53%)</td><td>0.77 (-0.79%)</td><td>0.77 (-0.42%)</td><td>0.75 (-2.63%)</td><td>0.01 <b>(+207.70%)</b></td><td>101090.10 (+2.71%)</td><td>98588.42 (+0.82%)</td><td>98348.30 (+0.42%)</td><td>96517.30 (-0.53%)</td><td>1935.91 <b>(+214.21%)</b></td><td>711.99 (+0.53%)</td><td>697.25 (-0.79%)</td><td>698.74 (-0.42%)</td><td>679.78 (-2.63%)</td><td>13.64 <b>(+207.70%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98427.30 (n/a)</td><td>97787.04 (n/a)</td><td>97939.80 (n/a)</td><td>97030.30 (n/a)</td><td>616.13 (n/a)</td><td>708.23 (n/a)</td><td>702.77 (n/a)</td><td>701.65 (n/a)</td><td>698.17 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.89 (-0.65%)</td><td>0.87 (-0.64%)</td><td>0.89 (+1.36%)</td><td>0.85 (-1.29%)</td><td>0.02 <b>(+57.67%)</b></td><td>88794.30 (+1.31%)</td><td>86455.48 (+0.67%)</td><td>84930.70 (-1.35%)</td><td>84872.40 (+0.65%)</td><td>2128.16 <b>(+60.97%)</b></td><td>809.68 (-0.65%)</td><td>795.24 (-0.64%)</td><td>809.12 (+1.36%)</td><td>773.92 (-1.29%)</td><td>19.40 <b>(+57.67%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.01 (n/a)</td><td>87647.80 (n/a)</td><td>85881.12 (n/a)</td><td>86089.60 (n/a)</td><td>84324.00 (n/a)</td><td>1322.10 (n/a)</td><td>814.95 (n/a)</td><td>800.32 (n/a)</td><td>798.23 (n/a)</td><td>784.04 (n/a)</td><td>12.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.27 <b>(+22.22%)</b></td><td>4.11 <b>(+26.46%)</b></td><td>4.04 (+13.50%)</td><td>2.20 (+1.40%)</td><td>1.20 <b>(+20.40%)</b></td><td>4043.40 (-1.38%)</td><td>2387.20 <b>(-20.05%)</b></td><td>2206.10 (-11.89%)</td><td>1690.90 (-18.18%)</td><td>955.56 (-3.64%)</td><td>317.51 <b>(+22.22%)</b></td><td>247.43 <b>(+26.46%)</b></td><td>243.36 (+13.50%)</td><td>132.78 (+1.40%)</td><td>72.27 <b>(+20.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.31 (n/a)</td><td>3.25 (n/a)</td><td>3.56 (n/a)</td><td>2.17 (n/a)</td><td>1.00 (n/a)</td><td>4099.90 (n/a)</td><td>2985.80 (n/a)</td><td>2503.90 (n/a)</td><td>2066.60 (n/a)</td><td>991.65 (n/a)</td><td>259.78 (n/a)</td><td>195.65 (n/a)</td><td>214.41 (n/a)</td><td>130.95 (n/a)</td><td>60.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.91 <b>(+68.75%)</b></td><td>3.38 <b>(+45.34%)</b></td><td>2.85 <b>(+28.70%)</b></td><td>2.46 (+19.91%)</td><td>1.07 <b>(+218.94%)</b></td><td>3616.60 (-16.60%)</td><td>2835.30 <b>(-27.06%)</b></td><td>3123.00 <b>(-22.30%)</b></td><td>1815.40 <b>(-40.74%)</b></td><td>795.46 <b>(+63.92%)</b></td><td>295.72 <b>(+68.75%)</b></td><td>203.67 <b>(+45.34%)</b></td><td>171.91 <b>(+28.70%)</b></td><td>148.44 (+19.91%)</td><td>64.47 <b>(+218.94%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.91 (n/a)</td><td>2.33 (n/a)</td><td>2.22 (n/a)</td><td>2.06 (n/a)</td><td>0.34 (n/a)</td><td>4336.60 (n/a)</td><td>3886.96 (n/a)</td><td>4019.40 (n/a)</td><td>3063.50 (n/a)</td><td>485.28 (n/a)</td><td>175.25 (n/a)</td><td>140.13 (n/a)</td><td>133.57 (n/a)</td><td>123.80 (n/a)</td><td>20.21 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.17 (-13.08%)</td><td>3.61 (-10.89%)</td><td>4.19 (+0.30%)</td><td>2.13 (+9.36%)</td><td>1.33 <b>(-30.09%)</b></td><td>4187.00 (-8.56%)</td><td>2794.98 (+2.97%)</td><td>2129.50 (-0.30%)</td><td>1724.70 (+15.05%)</td><td>1134.14 (-19.93%)</td><td>311.29 (-13.08%)</td><td>217.74 (-10.89%)</td><td>252.11 (+0.30%)</td><td>128.22 (+9.36%)</td><td>80.11 <b>(-30.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.95 (n/a)</td><td>4.06 (n/a)</td><td>4.17 (n/a)</td><td>1.95 (n/a)</td><td>1.90 (n/a)</td><td>4578.80 (n/a)</td><td>2714.48 (n/a)</td><td>2135.90 (n/a)</td><td>1499.10 (n/a)</td><td>1416.43 (n/a)</td><td>358.13 (n/a)</td><td>244.36 (n/a)</td><td>251.35 (n/a)</td><td>117.25 (n/a)</td><td>114.58 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.86 (-13.49%)</td><td>5.17 (-1.49%)</td><td>5.06 (+6.61%)</td><td>4.78 (+12.42%)</td><td>0.43 <b>(-60.34%)</b></td><td>7297.60 (-11.05%)</td><td>6784.64 (-1.21%)</td><td>6885.70 (-6.20%)</td><td>5947.00 (+15.60%)</td><td>537.86 <b>(-59.42%)</b></td><td>361.10 (-13.49%)</td><td>318.21 (-1.49%)</td><td>311.88 (+6.61%)</td><td>294.27 (+12.42%)</td><td>26.71 <b>(-60.34%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.78 (n/a)</td><td>5.24 (n/a)</td><td>4.75 (n/a)</td><td>4.25 (n/a)</td><td>1.09 (n/a)</td><td>8204.00 (n/a)</td><td>6867.78 (n/a)</td><td>7340.90 (n/a)</td><td>5144.50 (n/a)</td><td>1325.59 (n/a)</td><td>417.43 (n/a)</td><td>323.04 (n/a)</td><td>292.54 (n/a)</td><td>261.76 (n/a)</td><td>67.35 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.11 (-2.89%)</td><td>4.55 (-0.65%)</td><td>4.68 (+3.63%)</td><td>3.88 (+2.50%)</td><td>0.54 (-15.24%)</td><td>8991.90 (-2.44%)</td><td>7757.40 (+0.24%)</td><td>7446.60 (-3.50%)</td><td>6822.50 (+2.97%)</td><td>946.88 (-13.40%)</td><td>314.77 (-2.89%)</td><td>280.06 (-0.65%)</td><td>288.38 (+3.63%)</td><td>238.82 (+2.50%)</td><td>33.12 (-15.24%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.26 (n/a)</td><td>4.58 (n/a)</td><td>4.52 (n/a)</td><td>3.78 (n/a)</td><td>0.63 (n/a)</td><td>9217.20 (n/a)</td><td>7738.88 (n/a)</td><td>7716.70 (n/a)</td><td>6625.50 (n/a)</td><td>1093.35 (n/a)</td><td>324.12 (n/a)</td><td>281.89 (n/a)</td><td>278.29 (n/a)</td><td>232.99 (n/a)</td><td>39.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>6.86 (-4.81%)</td><td>5.46 (-9.81%)</td><td>5.91 (-13.19%)</td><td>3.76 (-10.59%)</td><td>1.36 (-3.08%)</td><td>9276.30 (+11.84%)</td><td>6746.00 (+11.57%)</td><td>5895.10 (+15.19%)</td><td>5085.80 (+5.06%)</td><td>1843.77 (+16.98%)</td><td>422.25 (-4.81%)</td><td>336.57 (-9.81%)</td><td>364.28 (-13.19%)</td><td>231.50 (-10.59%)</td><td>84.01 (-3.08%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.20 (n/a)</td><td>6.06 (n/a)</td><td>6.81 (n/a)</td><td>4.20 (n/a)</td><td>1.41 (n/a)</td><td>8294.20 (n/a)</td><td>6046.26 (n/a)</td><td>5117.70 (n/a)</td><td>4840.90 (n/a)</td><td>1576.08 (n/a)</td><td>443.61 (n/a)</td><td>373.16 (n/a)</td><td>419.62 (n/a)</td><td>258.91 (n/a)</td><td>86.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.79 (-0.21%)</td><td>0.76 (-0.55%)</td><td>0.78 (+1.11%)</td><td>0.73 (-2.06%)</td><td>0.03 <b>(+47.17%)</b></td><td>102946.30 (+2.10%)</td><td>98864.20 (+0.61%)</td><td>96888.20 (-1.10%)</td><td>95567.20 (+0.21%)</td><td>3532.18 <b>(+50.69%)</b></td><td>719.07 (-0.21%)</td><td>695.79 (-0.55%)</td><td>709.27 (+1.11%)</td><td>667.53 (-2.06%)</td><td>24.58 <b>(+47.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>100827.30 (n/a)</td><td>98263.48 (n/a)</td><td>97962.50 (n/a)</td><td>95369.30 (n/a)</td><td>2343.95 (n/a)</td><td>720.56 (n/a)</td><td>699.66 (n/a)</td><td>701.49 (n/a)</td><td>681.56 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.77 (-1.96%)</td><td>0.77 (+1.10%)</td><td>0.77 (+2.46%)</td><td>0.76 (+3.44%)</td><td>0.00 <b>(-80.06%)</b></td><td>99474.20 (-3.33%)</td><td>98458.48 (-1.17%)</td><td>98301.20 (-2.40%)</td><td>97888.00 (+2.00%)</td><td>628.54 <b>(-80.27%)</b></td><td>702.02 (-1.96%)</td><td>697.98 (+1.10%)</td><td>699.07 (+2.46%)</td><td>690.83 (+3.44%)</td><td>4.43 <b>(-80.06%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102901.00 (n/a)</td><td>99619.92 (n/a)</td><td>100715.90 (n/a)</td><td>95968.20 (n/a)</td><td>3185.01 (n/a)</td><td>716.07 (n/a)</td><td>690.39 (n/a)</td><td>682.31 (n/a)</td><td>667.82 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.90 (-0.13%)</td><td>0.89 (+0.81%)</td><td>0.90 (+1.41%)</td><td>0.88 (+1.53%)</td><td>0.01 <b>(-33.51%)</b></td><td>85513.80 (-1.51%)</td><td>84497.50 (-0.81%)</td><td>84042.50 (-1.39%)</td><td>83942.20 (+0.13%)</td><td>706.18 <b>(-34.57%)</b></td><td>818.65 (-0.13%)</td><td>813.32 (+0.81%)</td><td>817.68 (+1.41%)</td><td>803.61 (+1.53%)</td><td>6.77 <b>(-33.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86823.30 (n/a)</td><td>85186.02 (n/a)</td><td>85228.30 (n/a)</td><td>83836.00 (n/a)</td><td>1079.22 (n/a)</td><td>819.69 (n/a)</td><td>806.80 (n/a)</td><td>806.30 (n/a)</td><td>791.49 (n/a)</td><td>10.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.95 (-6.49%)</td><td>2.51 (-15.50%)</td><td>2.22 <b>(-34.75%)</b></td><td>1.45 (-4.69%)</td><td>1.15 (+3.50%)</td><td>5565.40 (+4.92%)</td><td>3812.08 <b>(+22.05%)</b></td><td>3625.50 <b>(+53.27%)</b></td><td>2041.90 (+6.94%)</td><td>1684.39 (+18.99%)</td><td>1035.26 (-6.49%)</td><td>658.68 (-15.50%)</td><td>583.08 <b>(-34.75%)</b></td><td>379.83 (-4.69%)</td><td>301.98 (+3.50%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.22 (n/a)</td><td>2.97 (n/a)</td><td>3.41 (n/a)</td><td>1.52 (n/a)</td><td>1.11 (n/a)</td><td>5304.50 (n/a)</td><td>3123.46 (n/a)</td><td>2365.50 (n/a)</td><td>1909.40 (n/a)</td><td>1415.60 (n/a)</td><td>1107.12 (n/a)</td><td>779.48 (n/a)</td><td>893.66 (n/a)</td><td>398.52 (n/a)</td><td>291.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 <b>(-21.89%)</b></td><td>0.19 (-9.58%)</td><td>0.20 (+0.69%)</td><td>0.15 (-9.51%)</td><td>0.03 <b>(-36.96%)</b></td><td>8306.70 (+10.50%)</td><td>6584.00 (+8.87%)</td><td>6142.70 (-0.69%)</td><td>5247.70 <b>(+28.02%)</b></td><td>1169.31 (-5.16%)</td><td>12.79 <b>(-21.89%)</b></td><td>10.44 (-9.58%)</td><td>10.92 (+0.69%)</td><td>8.08 (-9.51%)</td><td>1.78 <b>(-36.96%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>7517.10 (n/a)</td><td>6047.52 (n/a)</td><td>6185.30 (n/a)</td><td>4099.20 (n/a)</td><td>1232.89 (n/a)</td><td>16.37 (n/a)</td><td>11.55 (n/a)</td><td>10.85 (n/a)</td><td>8.93 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.77 (n/a)</td><td>3.58 (n/a)</td><td>3.57 (n/a)</td><td>3.39 (n/a)</td><td>0.15 (n/a)</td><td>3.77 (n/a)</td><td>3.58 (n/a)</td><td>3.57 (n/a)</td><td>3.39 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.54 (+2.91%)</td><td>6.83 (+9.01%)</td><td>6.78 (-1.96%)</td><td>5.82 (+16.03%)</td><td>0.69 <b>(-38.59%)</b></td><td>7.53 (+2.91%)</td><td>6.82 (+9.01%)</td><td>6.78 (-1.96%)</td><td>5.82 (+16.03%)</td><td>0.69 <b>(-38.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.32 (n/a)</td><td>6.26 (n/a)</td><td>6.92 (n/a)</td><td>5.02 (n/a)</td><td>1.12 (n/a)</td><td>7.32 (n/a)</td><td>6.26 (n/a)</td><td>6.91 (n/a)</td><td>5.01 (n/a)</td><td>1.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>14.00 (+5.69%)</td><td>8.73 (-9.84%)</td><td>7.29 (-15.11%)</td><td>7.04 (-14.81%)</td><td>2.98 <b>(+43.33%)</b></td><td>13.99 (+5.69%)</td><td>8.72 (-9.84%)</td><td>7.29 (-15.11%)</td><td>7.03 (-14.81%)</td><td>2.97 <b>(+43.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>13.24 (n/a)</td><td>9.68 (n/a)</td><td>8.59 (n/a)</td><td>8.26 (n/a)</td><td>2.08 (n/a)</td><td>13.24 (n/a)</td><td>9.68 (n/a)</td><td>8.58 (n/a)</td><td>8.25 (n/a)</td><td>2.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.94 (n/a)</td><td>3.68 (n/a)</td><td>3.72 (n/a)</td><td>3.28 (n/a)</td><td>0.25 (n/a)</td><td>3.94 (n/a)</td><td>3.67 (n/a)</td><td>3.72 (n/a)</td><td>3.28 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.38 (+1.08%)</td><td>6.32 (+0.10%)</td><td>6.26 (-2.31%)</td><td>5.66 (+8.84%)</td><td>0.71 (-16.82%)</td><td>7.38 (+1.08%)</td><td>6.32 (+0.10%)</td><td>6.25 (-2.31%)</td><td>5.66 (+8.84%)</td><td>0.71 (-16.82%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.30 (n/a)</td><td>6.31 (n/a)</td><td>6.40 (n/a)</td><td>5.20 (n/a)</td><td>0.86 (n/a)</td><td>7.30 (n/a)</td><td>6.31 (n/a)</td><td>6.40 (n/a)</td><td>5.20 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>13.94 (+0.52%)</td><td>10.18 (+4.49%)</td><td>9.89 (+2.36%)</td><td>7.52 (+1.30%)</td><td>2.60 (+2.60%)</td><td>13.93 (+0.52%)</td><td>10.17 (+4.49%)</td><td>9.88 (+2.36%)</td><td>7.52 (+1.30%)</td><td>2.60 (+2.60%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>13.87 (n/a)</td><td>9.74 (n/a)</td><td>9.66 (n/a)</td><td>7.42 (n/a)</td><td>2.53 (n/a)</td><td>13.86 (n/a)</td><td>9.73 (n/a)</td><td>9.66 (n/a)</td><td>7.42 (n/a)</td><td>2.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.51 (+12.94%)</td><td>2.73 (+7.93%)</td><td>2.86 (+2.59%)</td><td>1.57 <b>(+30.12%)</b></td><td>0.71 (-6.01%)</td><td>3.50 (+12.94%)</td><td>2.72 (+7.93%)</td><td>2.85 (+2.59%)</td><td>1.57 <b>(+30.12%)</b></td><td>0.71 (-6.01%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.11 (n/a)</td><td>2.53 (n/a)</td><td>2.79 (n/a)</td><td>1.21 (n/a)</td><td>0.75 (n/a)</td><td>3.10 (n/a)</td><td>2.52 (n/a)</td><td>2.78 (n/a)</td><td>1.20 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.38 <b>(-31.81%)</b></td><td>0.18 <b>(-40.30%)</b></td><td>0.12 <b>(-65.85%)</b></td><td>0.08 (+2.25%)</td><td>0.13 <b>(-36.73%)</b></td><td>0.37 <b>(-31.81%)</b></td><td>0.18 <b>(-40.30%)</b></td><td>0.12 <b>(-65.85%)</b></td><td>0.08 (+2.25%)</td><td>0.13 <b>(-36.73%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.56 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.55 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.68 (-1.80%)</td><td>0.52 (-11.47%)</td><td>0.52 (-19.37%)</td><td>0.37 <b>(+24.35%)</b></td><td>0.14 (-15.95%)</td><td>0.67 (-1.80%)</td><td>0.51 (-11.47%)</td><td>0.51 (-19.37%)</td><td>0.37 <b>(+24.35%)</b></td><td>0.14 (-15.95%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.69 (n/a)</td><td>0.59 (n/a)</td><td>0.64 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.68 (n/a)</td><td>0.58 (n/a)</td><td>0.63 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.47 (+3.90%)</td><td>1.90 <b>(+57.36%)</b></td><td>2.29 <b>(+192.37%)</b></td><td>0.46 (-1.36%)</td><td>0.85 (-3.85%)</td><td>2.43 (+3.90%)</td><td>1.87 <b>(+57.36%)</b></td><td>2.25 <b>(+192.37%)</b></td><td>0.45 (-1.36%)</td><td>0.84 (-3.85%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.38 (n/a)</td><td>1.20 (n/a)</td><td>0.78 (n/a)</td><td>0.46 (n/a)</td><td>0.88 (n/a)</td><td>2.34 (n/a)</td><td>1.19 (n/a)</td><td>0.77 (n/a)</td><td>0.46 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.90 (n/a)</td><td>321.98 (n/a)</td><td>275.90 (n/a)</td><td>207.20 (n/a)</td><td>135.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.50 (n/a)</td><td>378.36 (n/a)</td><td>343.20 (n/a)</td><td>220.10 (n/a)</td><td>136.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.10 (n/a)</td><td>433.98 (n/a)</td><td>466.50 (n/a)</td><td>212.40 (n/a)</td><td>142.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1020.50 (n/a)</td><td>506.36 (n/a)</td><td>436.10 (n/a)</td><td>233.70 (n/a)</td><td>299.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.50 (n/a)</td><td>382.44 (n/a)</td><td>411.60 (n/a)</td><td>231.70 (n/a)</td><td>140.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.30 (n/a)</td><td>428.54 (n/a)</td><td>424.50 (n/a)</td><td>180.60 (n/a)</td><td>179.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>769.40 (n/a)</td><td>421.74 (n/a)</td><td>372.30 (n/a)</td><td>279.70 (n/a)</td><td>200.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.00 (n/a)</td><td>371.56 (n/a)</td><td>270.30 (n/a)</td><td>230.40 (n/a)</td><td>179.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.10 (n/a)</td><td>307.56 (n/a)</td><td>260.50 (n/a)</td><td>247.10 (n/a)</td><td>106.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>538.80 (n/a)</td><td>462.44 (n/a)</td><td>474.60 (n/a)</td><td>385.20 (n/a)</td><td>56.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.70 (n/a)</td><td>466.60 (n/a)</td><td>485.90 (n/a)</td><td>298.30 (n/a)</td><td>102.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.10 (n/a)</td><td>406.00 (n/a)</td><td>350.00 (n/a)</td><td>318.00 (n/a)</td><td>105.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>338.52 (n/a)</td><td>287.80 (n/a)</td><td>252.80 (n/a)</td><td>128.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1916.70 (n/a)</td><td>655.56 (n/a)</td><td>275.30 (n/a)</td><td>241.10 (n/a)</td><td>720.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>459.70 (n/a)</td><td>357.04 (n/a)</td><td>336.10 (n/a)</td><td>244.70 (n/a)</td><td>92.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.50 (n/a)</td><td>391.36 (n/a)</td><td>436.20 (n/a)</td><td>271.40 (n/a)</td><td>94.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2028.10 (n/a)</td><td>1065.78 (n/a)</td><td>772.60 (n/a)</td><td>282.70 (n/a)</td><td>869.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.20 (n/a)</td><td>463.74 (n/a)</td><td>476.80 (n/a)</td><td>291.40 (n/a)</td><td>109.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>651.20 (n/a)</td><td>449.48 (n/a)</td><td>506.00 (n/a)</td><td>225.30 (n/a)</td><td>178.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>664.40 (n/a)</td><td>410.32 (n/a)</td><td>288.40 (n/a)</td><td>251.50 (n/a)</td><td>201.09 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>542.60 (n/a)</td><td>367.90 (n/a)</td><td>308.50 (n/a)</td><td>284.20 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>486.90 (n/a)</td><td>376.20 (n/a)</td><td>340.80 (n/a)</td><td>293.50 (n/a)</td><td>89.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>577.50 (n/a)</td><td>521.34 (n/a)</td><td>536.10 (n/a)</td><td>427.90 (n/a)</td><td>58.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>616.70 (n/a)</td><td>440.04 (n/a)</td><td>465.60 (n/a)</td><td>229.50 (n/a)</td><td>141.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-15.56%)</td><td>0.01 (-11.42%)</td><td>0.01 (-8.25%)</td><td>0.01 <b>(-24.36%)</b></td><td>0.00 (-9.08%)</td><td>671.10 <b>(+32.18%)</b></td><td>348.00 (+17.18%)</td><td>285.80 (+9.00%)</td><td>221.70 (+18.43%)</td><td>183.00 <b>(+47.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>507.70 (n/a)</td><td>296.98 (n/a)</td><td>262.20 (n/a)</td><td>187.20 (n/a)</td><td>124.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (+3.95%)</td><td>0.01 (+19.52%)</td><td>0.01 (-4.92%)</td><td>0.01 <b>(+337.47%)</b></td><td>0.00 <b>(-29.23%)</b></td><td>553.10 <b>(-77.14%)</b></td><td>415.24 <b>(-48.32%)</b></td><td>421.50 (+5.19%)</td><td>282.50 (-3.78%)</td><td>121.68 <b>(-86.58%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2419.50 (n/a)</td><td>803.44 (n/a)</td><td>400.70 (n/a)</td><td>293.60 (n/a)</td><td>906.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-15.38%)</td><td>0.01 (-8.52%)</td><td>0.01 (+9.32%)</td><td>0.01 <b>(-21.81%)</b></td><td>0.00 (-6.74%)</td><td>624.00 <b>(+27.90%)</b></td><td>393.82 (+12.35%)</td><td>350.60 (-8.53%)</td><td>245.60 (+18.13%)</td><td>158.64 <b>(+41.00%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.90 (n/a)</td><td>350.54 (n/a)</td><td>383.30 (n/a)</td><td>207.90 (n/a)</td><td>112.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+9.45%)</td><td>0.01 (+0.42%)</td><td>0.01 (+1.61%)</td><td>0.00 <b>(-41.58%)</b></td><td>0.01 <b>(+39.04%)</b></td><td>1001.60 <b>(+71.18%)</b></td><td>511.54 (+16.24%)</td><td>490.60 (-1.58%)</td><td>245.50 (-8.67%)</td><td>306.23 <b>(+105.61%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.10 (n/a)</td><td>440.08 (n/a)</td><td>498.50 (n/a)</td><td>268.80 (n/a)</td><td>148.93 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-3.49%)</td><td>0.01 <b>(-32.51%)</b></td><td>0.01 <b>(-33.91%)</b></td><td>0.00 <b>(-78.23%)</b></td><td>0.01 <b>(+72.36%)</b></td><td>2482.30 <b>(+359.34%)</b></td><td>1103.14 <b>(+204.60%)</b></td><td>535.90 <b>(+51.30%)</b></td><td>252.80 (+3.61%)</td><td>1039.51 <b>(+760.72%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.40 (n/a)</td><td>362.16 (n/a)</td><td>354.20 (n/a)</td><td>244.00 (n/a)</td><td>120.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-0.25%)</td><td>0.01 (+5.27%)</td><td>0.01 (-10.26%)</td><td>0.01 (+12.65%)</td><td>0.00 (-4.31%)</td><td>547.60 (-11.23%)</td><td>424.96 (-6.50%)</td><td>449.10 (+11.44%)</td><td>311.80 (+0.26%)</td><td>105.31 <b>(-21.00%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.90 (n/a)</td><td>454.50 (n/a)</td><td>403.00 (n/a)</td><td>311.00 (n/a)</td><td>133.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (+3.63%)</td><td>0.03 (+8.50%)</td><td>0.03 <b>(+30.34%)</b></td><td>0.02 (-14.00%)</td><td>0.01 <b>(+47.98%)</b></td><td>438.60 (+16.31%)</td><td>288.62 (-4.58%)</td><td>239.30 <b>(-23.25%)</b></td><td>231.20 (-3.51%)</td><td>88.13 <b>(+66.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>377.10 (n/a)</td><td>302.46 (n/a)</td><td>311.80 (n/a)</td><td>239.60 (n/a)</td><td>52.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (-5.56%)</td><td>0.02 <b>(-24.88%)</b></td><td>0.02 <b>(-23.65%)</b></td><td>0.00 <b>(-74.71%)</b></td><td>0.01 <b>(+52.23%)</b></td><td>1926.10 <b>(+295.34%)</b></td><td>705.52 <b>(+102.13%)</b></td><td>386.40 <b>(+30.98%)</b></td><td>274.50 (+5.90%)</td><td>695.15 <b>(+573.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.20 (n/a)</td><td>349.04 (n/a)</td><td>295.00 (n/a)</td><td>259.20 (n/a)</td><td>103.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 <b>(-29.29%)</b></td><td>0.02 (-12.64%)</td><td>0.02 (+10.50%)</td><td>0.01 <b>(+52.49%)</b></td><td>0.00 <b>(-59.59%)</b></td><td>617.80 <b>(-34.42%)</b></td><td>475.82 (-7.45%)</td><td>466.90 (-9.50%)</td><td>320.30 <b>(+41.41%)</b></td><td>108.99 <b>(-61.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>942.10 (n/a)</td><td>514.12 (n/a)</td><td>515.90 (n/a)</td><td>226.50 (n/a)</td><td>286.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+10.86%)</td><td>0.02 (-8.96%)</td><td>0.01 (-15.69%)</td><td>0.00 <b>(-69.40%)</b></td><td>0.01 <b>(+57.29%)</b></td><td>1915.10 <b>(+226.81%)</b></td><td>719.10 <b>(+68.76%)</b></td><td>552.30 (+18.62%)</td><td>243.30 (-9.82%)</td><td>690.27 <b>(+367.93%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.00 (n/a)</td><td>426.10 (n/a)</td><td>465.60 (n/a)</td><td>269.80 (n/a)</td><td>147.52 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (+8.35%)</td><td>0.03 <b>(+28.12%)</b></td><td>0.03 <b>(+65.48%)</b></td><td>0.02 <b>(+20.50%)</b></td><td>0.01 (+1.60%)</td><td>535.00 (-17.02%)</td><td>350.60 <b>(-23.39%)</b></td><td>290.90 <b>(-39.56%)</b></td><td>212.70 (-7.72%)</td><td>132.81 (-17.67%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.70 (n/a)</td><td>457.64 (n/a)</td><td>481.30 (n/a)</td><td>230.50 (n/a)</td><td>161.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(-25.92%)</b></td><td>0.02 (-15.21%)</td><td>0.02 (-0.40%)</td><td>0.01 <b>(-40.65%)</b></td><td>0.01 (-16.46%)</td><td>1042.30 <b>(+68.49%)</b></td><td>580.12 <b>(+24.23%)</b></td><td>488.40 (+0.39%)</td><td>370.60 <b>(+34.96%)</b></td><td>268.89 <b>(+109.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.60 (n/a)</td><td>466.96 (n/a)</td><td>486.50 (n/a)</td><td>274.60 (n/a)</td><td>128.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 <b>(-36.93%)</b></td><td>0.03 (+8.66%)</td><td>0.03 <b>(+78.58%)</b></td><td>0.02 <b>(+26.84%)</b></td><td>0.01 <b>(-65.57%)</b></td><td>433.10 <b>(-21.15%)</b></td><td>306.40 <b>(-23.15%)</b></td><td>279.70 <b>(-44.00%)</b></td><td>257.20 <b>(+58.57%)</b></td><td>72.73 <b>(-57.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>549.30 (n/a)</td><td>398.72 (n/a)</td><td>499.50 (n/a)</td><td>162.20 (n/a)</td><td>169.50 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 <b>(+25.31%)</b></td><td>0.02 <b>(+48.47%)</b></td><td>0.02 <b>(+50.59%)</b></td><td>0.01 <b>(+222.72%)</b></td><td>0.01 (-6.53%)</td><td>675.10 <b>(-69.02%)</b></td><td>408.30 <b>(-50.24%)</b></td><td>355.30 <b>(-33.60%)</b></td><td>272.60 <b>(-20.20%)</b></td><td>158.39 <b>(-79.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2178.80 (n/a)</td><td>820.60 (n/a)</td><td>535.10 (n/a)</td><td>341.60 (n/a)</td><td>763.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-10.93%)</td><td>0.05 <b>(+37.97%)</b></td><td>0.07 <b>(+102.73%)</b></td><td>0.03 <b>(+21.09%)</b></td><td>0.02 (-11.33%)</td><td>542.30 (-17.42%)</td><td>349.70 <b>(-30.16%)</b></td><td>248.80 <b>(-50.67%)</b></td><td>245.60 (+12.25%)</td><td>142.87 (-17.67%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.70 (n/a)</td><td>500.70 (n/a)</td><td>504.40 (n/a)</td><td>218.80 (n/a)</td><td>173.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-16.64%)</td><td>0.04 (-16.43%)</td><td>0.04 <b>(-33.84%)</b></td><td>0.02 <b>(+224.89%)</b></td><td>0.01 <b>(-46.60%)</b></td><td>767.00 <b>(-69.22%)</b></td><td>478.92 <b>(-36.10%)</b></td><td>462.90 <b>(+51.18%)</b></td><td>284.20 (+19.97%)</td><td>178.09 <b>(-81.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2492.00 (n/a)</td><td>749.48 (n/a)</td><td>306.20 (n/a)</td><td>236.90 (n/a)</td><td>977.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 <b>(+25.42%)</b></td><td>0.05 <b>(+28.53%)</b></td><td>0.06 <b>(+98.42%)</b></td><td>0.03 (-1.62%)</td><td>0.02 <b>(+24.01%)</b></td><td>639.20 (+1.64%)</td><td>376.82 (-19.88%)</td><td>279.50 <b>(-49.60%)</b></td><td>221.90 <b>(-20.27%)</b></td><td>174.61 (+4.24%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.90 (n/a)</td><td>470.32 (n/a)</td><td>554.60 (n/a)</td><td>278.30 (n/a)</td><td>167.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (+10.72%)</td><td>0.04 (-6.33%)</td><td>0.03 (+0.36%)</td><td>0.03 (+3.13%)</td><td>0.02 (-1.44%)</td><td>562.60 (-3.03%)</td><td>443.40 (+4.78%)</td><td>474.10 (-0.36%)</td><td>233.10 (-9.69%)</td><td>128.53 (-14.35%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>580.20 (n/a)</td><td>423.16 (n/a)</td><td>475.80 (n/a)</td><td>258.10 (n/a)</td><td>150.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 <b>(+25.92%)</b></td><td>0.05 <b>(+50.37%)</b></td><td>0.06 <b>(+71.87%)</b></td><td>0.01 (+3.37%)</td><td>0.03 <b>(+38.93%)</b></td><td>2389.90 (-3.25%)</td><td>704.40 (-17.14%)</td><td>288.10 <b>(-41.81%)</b></td><td>209.60 <b>(-20.61%)</b></td><td>944.40 (+3.56%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2470.30 (n/a)</td><td>850.06 (n/a)</td><td>495.10 (n/a)</td><td>264.00 (n/a)</td><td>911.97 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-15.25%)</td><td>0.04 (-9.68%)</td><td>0.05 (-1.75%)</td><td>0.03 (-18.82%)</td><td>0.02 (-10.62%)</td><td>599.50 <b>(+23.18%)</b></td><td>410.62 (+12.27%)</td><td>359.30 (+1.78%)</td><td>255.90 (+17.98%)</td><td>147.77 <b>(+29.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>486.70 (n/a)</td><td>365.74 (n/a)</td><td>353.00 (n/a)</td><td>216.90 (n/a)</td><td>114.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-8.25%)</td><td>0.10 (-1.91%)</td><td>0.11 (+3.20%)</td><td>0.05 (-8.04%)</td><td>0.04 (-5.02%)</td><td>598.00 (+8.75%)</td><td>372.48 (+2.18%)</td><td>303.20 (-3.10%)</td><td>245.90 (+8.95%)</td><td>154.07 (+7.50%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>549.90 (n/a)</td><td>364.54 (n/a)</td><td>312.90 (n/a)</td><td>225.70 (n/a)</td><td>143.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 <b>(+26.25%)</b></td><td>0.12 (+1.27%)</td><td>0.11 (-7.80%)</td><td>0.08 (+0.97%)</td><td>0.04 <b>(+54.37%)</b></td><td>429.00 (-0.97%)</td><td>303.74 (+2.17%)</td><td>286.50 (+8.48%)</td><td>195.30 <b>(-20.80%)</b></td><td>93.49 (+19.80%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>433.20 (n/a)</td><td>297.30 (n/a)</td><td>264.10 (n/a)</td><td>246.60 (n/a)</td><td>78.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (+5.75%)</td><td>0.11 (+2.98%)</td><td>0.11 (+4.47%)</td><td>0.07 (-8.38%)</td><td>0.03 (+7.38%)</td><td>461.80 (+9.15%)</td><td>313.20 (-1.94%)</td><td>288.50 (-4.28%)</td><td>209.30 (-5.42%)</td><td>100.52 (+8.77%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>423.10 (n/a)</td><td>319.40 (n/a)</td><td>301.40 (n/a)</td><td>221.30 (n/a)</td><td>92.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-12.24%)</td><td>0.08 <b>(-26.57%)</b></td><td>0.06 <b>(-48.94%)</b></td><td>0.06 (-1.30%)</td><td>0.03 (-6.50%)</td><td>566.50 (+1.32%)</td><td>442.86 <b>(+36.55%)</b></td><td>514.00 <b>(+95.88%)</b></td><td>254.30 (+13.93%)</td><td>147.99 (+8.03%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.10 (n/a)</td><td>324.32 (n/a)</td><td>262.40 (n/a)</td><td>223.20 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (+8.54%)</td><td>0.08 (+13.92%)</td><td>0.08 (+12.59%)</td><td>0.06 (+14.62%)</td><td>0.02 (-3.19%)</td><td>541.60 (-12.76%)</td><td>409.62 (-13.83%)</td><td>435.20 (-11.18%)</td><td>286.80 (-7.87%)</td><td>101.54 <b>(-24.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>620.80 (n/a)</td><td>475.34 (n/a)</td><td>490.00 (n/a)</td><td>311.30 (n/a)</td><td>134.29 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+9.42%)</td><td>0.01 <b>(-29.01%)</b></td><td>0.01 <b>(-30.54%)</b></td><td>0.00 <b>(-69.64%)</b></td><td>0.01 <b>(+191.79%)</b></td><td>986.30 <b>(+229.43%)</b></td><td>456.64 <b>(+85.82%)</b></td><td>351.40 <b>(+43.96%)</b></td><td>193.40 (-8.60%)</td><td>311.90 <b>(+820.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.40 (n/a)</td><td>245.74 (n/a)</td><td>244.10 (n/a)</td><td>211.60 (n/a)</td><td>33.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+7.19%)</td><td>0.01 (-3.23%)</td><td>0.01 (-2.61%)</td><td>0.01 (-19.34%)</td><td>0.00 <b>(+67.34%)</b></td><td>380.60 <b>(+23.97%)</b></td><td>285.98 (+5.82%)</td><td>280.80 (+2.67%)</td><td>211.50 (-6.75%)</td><td>60.66 <b>(+96.49%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>307.00 (n/a)</td><td>270.26 (n/a)</td><td>273.50 (n/a)</td><td>226.80 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+32.01%)</b></td><td>0.01 (+5.30%)</td><td>0.01 <b>(-21.12%)</b></td><td>0.01 <b>(+48.97%)</b></td><td>0.01 (+5.43%)</td><td>420.80 <b>(-32.88%)</b></td><td>308.66 (-11.01%)</td><td>309.90 <b>(+26.75%)</b></td><td>173.50 <b>(-24.24%)</b></td><td>93.14 <b>(-45.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.90 (n/a)</td><td>346.84 (n/a)</td><td>244.50 (n/a)</td><td>229.00 (n/a)</td><td>172.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-5.73%)</td><td>0.01 <b>(-26.47%)</b></td><td>0.01 <b>(-44.29%)</b></td><td>0.01 (-12.23%)</td><td>0.00 (+12.14%)</td><td>507.40 (+13.95%)</td><td>409.24 <b>(+39.50%)</b></td><td>482.30 <b>(+79.49%)</b></td><td>250.50 (+6.05%)</td><td>115.90 <b>(+34.16%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.30 (n/a)</td><td>293.36 (n/a)</td><td>268.70 (n/a)</td><td>236.20 (n/a)</td><td>86.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 <b>(-23.49%)</b></td><td>0.01 (-19.80%)</td><td>0.01 <b>(-29.74%)</b></td><td>0.01 (-18.72%)</td><td>0.00 <b>(-24.46%)</b></td><td>574.70 <b>(+23.04%)</b></td><td>424.24 <b>(+23.74%)</b></td><td>442.30 <b>(+42.31%)</b></td><td>314.00 <b>(+30.67%)</b></td><td>107.15 (+14.76%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.10 (n/a)</td><td>342.84 (n/a)</td><td>310.80 (n/a)</td><td>240.30 (n/a)</td><td>93.37 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+47.83%)</b></td><td>0.01 <b>(+41.00%)</b></td><td>0.01 <b>(+42.14%)</b></td><td>0.01 <b>(+20.52%)</b></td><td>0.00 <b>(+46.20%)</b></td><td>459.60 (-17.02%)</td><td>297.30 <b>(-28.09%)</b></td><td>290.10 <b>(-29.66%)</b></td><td>195.80 <b>(-32.37%)</b></td><td>101.50 (-15.06%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.90 (n/a)</td><td>413.46 (n/a)</td><td>412.40 (n/a)</td><td>289.50 (n/a)</td><td>119.49 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+85.02%)</b></td><td>0.01 (+17.06%)</td><td>0.01 (-9.83%)</td><td>0.01 (+6.82%)</td><td>0.01 <b>(+253.87%)</b></td><td>530.40 (-6.39%)</td><td>441.20 (-2.26%)</td><td>500.00 (+10.89%)</td><td>185.40 <b>(-45.93%)</b></td><td>145.33 <b>(+74.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.60 (n/a)</td><td>451.40 (n/a)</td><td>450.90 (n/a)</td><td>342.90 (n/a)</td><td>83.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+7.39%)</td><td>0.01 (+7.43%)</td><td>0.01 (+13.14%)</td><td>0.01 (+13.12%)</td><td>0.00 (+5.89%)</td><td>497.90 (-11.59%)</td><td>365.42 (-7.11%)</td><td>316.40 (-11.62%)</td><td>268.10 (-6.88%)</td><td>107.02 (-9.50%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.20 (n/a)</td><td>393.40 (n/a)</td><td>358.00 (n/a)</td><td>287.90 (n/a)</td><td>118.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-14.59%)</td><td>0.01 (-13.35%)</td><td>0.01 <b>(-34.31%)</b></td><td>0.01 <b>(+267.34%)</b></td><td>0.00 <b>(-38.66%)</b></td><td>663.30 <b>(-72.78%)</b></td><td>526.76 <b>(-32.48%)</b></td><td>592.40 <b>(+52.25%)</b></td><td>285.30 (+17.07%)</td><td>151.04 <b>(-83.76%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2436.40 (n/a)</td><td>780.14 (n/a)</td><td>389.10 (n/a)</td><td>243.70 (n/a)</td><td>929.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 <b>(-20.90%)</b></td><td>0.01 <b>(-20.22%)</b></td><td>0.01 <b>(-32.36%)</b></td><td>0.01 (+6.03%)</td><td>0.00 <b>(-51.72%)</b></td><td>546.30 (-5.68%)</td><td>448.70 (+17.06%)</td><td>437.90 <b>(+47.84%)</b></td><td>334.00 <b>(+26.42%)</b></td><td>78.28 <b>(-43.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.20 (n/a)</td><td>383.32 (n/a)</td><td>296.20 (n/a)</td><td>264.20 (n/a)</td><td>139.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-1.82%)</td><td>0.01 (-1.96%)</td><td>0.01 (+3.80%)</td><td>0.01 (+3.66%)</td><td>0.00 (-10.03%)</td><td>552.90 (-3.54%)</td><td>413.22 (+0.91%)</td><td>394.60 (-3.64%)</td><td>294.70 (+1.83%)</td><td>95.72 (-11.53%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.20 (n/a)</td><td>409.48 (n/a)</td><td>409.50 (n/a)</td><td>289.40 (n/a)</td><td>108.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (-16.70%)</td><td>0.02 (-12.89%)</td><td>0.02 (-12.25%)</td><td>0.01 (-10.48%)</td><td>0.00 <b>(-22.97%)</b></td><td>559.20 (+11.71%)</td><td>382.06 (+13.71%)</td><td>341.30 (+13.96%)</td><td>319.20 <b>(+20.05%)</b></td><td>99.88 (+4.38%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.60 (n/a)</td><td>336.00 (n/a)</td><td>299.50 (n/a)</td><td>265.90 (n/a)</td><td>95.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+3.41%)</td><td>0.03 (+9.04%)</td><td>0.03 (+15.33%)</td><td>0.01 (-1.33%)</td><td>0.01 (+13.04%)</td><td>655.90 (+1.34%)</td><td>353.28 (-6.05%)</td><td>290.80 (-13.27%)</td><td>252.00 (-3.30%)</td><td>170.30 (+9.78%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.20 (n/a)</td><td>376.02 (n/a)</td><td>335.30 (n/a)</td><td>260.60 (n/a)</td><td>155.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+3.68%)</td><td>0.02 (-1.46%)</td><td>0.03 (-3.90%)</td><td>0.01 (-4.73%)</td><td>0.01 (+1.87%)</td><td>630.60 (+4.96%)</td><td>398.16 (+2.42%)</td><td>282.80 (+4.05%)</td><td>249.80 (-3.55%)</td><td>178.56 (+5.72%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.80 (n/a)</td><td>388.76 (n/a)</td><td>271.80 (n/a)</td><td>259.00 (n/a)</td><td>168.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+12.87%)</td><td>0.02 (-4.93%)</td><td>0.02 (+9.09%)</td><td>0.01 <b>(-45.24%)</b></td><td>0.01 <b>(+60.22%)</b></td><td>1054.00 <b>(+82.64%)</b></td><td>512.54 <b>(+30.60%)</b></td><td>378.40 (-8.33%)</td><td>238.70 (-11.40%)</td><td>339.09 <b>(+167.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.10 (n/a)</td><td>392.46 (n/a)</td><td>412.80 (n/a)</td><td>269.40 (n/a)</td><td>126.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+0.95%)</td><td>0.02 (-3.42%)</td><td>0.02 (-8.65%)</td><td>0.02 (-0.79%)</td><td>0.01 (-3.03%)</td><td>465.30 (+0.80%)</td><td>378.30 (+3.02%)</td><td>390.30 (+9.45%)</td><td>259.70 (-0.95%)</td><td>74.61 (-9.22%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.60 (n/a)</td><td>367.22 (n/a)</td><td>356.60 (n/a)</td><td>262.20 (n/a)</td><td>82.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 <b>(+20.63%)</b></td><td>0.03 <b>(+26.53%)</b></td><td>0.03 <b>(+59.65%)</b></td><td>0.02 (+16.99%)</td><td>0.01 (+0.63%)</td><td>533.70 (-14.53%)</td><td>330.48 <b>(-22.56%)</b></td><td>293.90 <b>(-37.36%)</b></td><td>223.70 (-17.09%)</td><td>119.39 (-19.75%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.40 (n/a)</td><td>426.78 (n/a)</td><td>469.20 (n/a)</td><td>269.80 (n/a)</td><td>148.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+10.50%)</td><td>0.02 <b>(+27.67%)</b></td><td>0.03 <b>(+39.41%)</b></td><td>0.02 <b>(+38.51%)</b></td><td>0.01 (+9.89%)</td><td>543.70 <b>(-27.80%)</b></td><td>364.80 <b>(-23.30%)</b></td><td>313.70 <b>(-28.28%)</b></td><td>241.20 (-9.53%)</td><td>132.96 <b>(-28.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>753.00 (n/a)</td><td>475.60 (n/a)</td><td>437.40 (n/a)</td><td>266.60 (n/a)</td><td>185.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (+18.76%)</td><td>0.03 <b>(+32.06%)</b></td><td>0.03 <b>(+80.48%)</b></td><td>0.01 <b>(+200.84%)</b></td><td>0.01 (+9.38%)</td><td>615.50 <b>(-66.76%)</b></td><td>387.32 <b>(-42.24%)</b></td><td>249.00 <b>(-44.58%)</b></td><td>225.20 (-15.81%)</td><td>201.56 <b>(-69.80%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1851.80 (n/a)</td><td>670.60 (n/a)</td><td>449.30 (n/a)</td><td>267.50 (n/a)</td><td>667.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (+10.58%)</td><td>0.03 <b>(+34.04%)</b></td><td>0.03 <b>(+34.39%)</b></td><td>0.02 <b>(+63.54%)</b></td><td>0.01 (-5.68%)</td><td>516.90 <b>(-38.85%)</b></td><td>292.92 <b>(-31.65%)</b></td><td>235.70 <b>(-25.60%)</b></td><td>221.40 (-9.60%)</td><td>126.00 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>845.30 (n/a)</td><td>428.58 (n/a)</td><td>316.80 (n/a)</td><td>244.90 (n/a)</td><td>243.88 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+4.41%)</td><td>0.02 (-19.57%)</td><td>0.02 <b>(-36.07%)</b></td><td>0.01 <b>(-49.90%)</b></td><td>0.01 <b>(+66.11%)</b></td><td>1068.10 <b>(+99.61%)</b></td><td>510.70 <b>(+53.14%)</b></td><td>456.60 <b>(+56.42%)</b></td><td>240.70 (-4.22%)</td><td>333.73 <b>(+191.05%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.10 (n/a)</td><td>333.48 (n/a)</td><td>291.90 (n/a)</td><td>251.30 (n/a)</td><td>114.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 <b>(-22.54%)</b></td><td>0.02 (-0.07%)</td><td>0.02 (+15.11%)</td><td>0.01 <b>(+273.63%)</b></td><td>0.01 <b>(-56.39%)</b></td><td>611.00 <b>(-73.24%)</b></td><td>440.22 <b>(-42.42%)</b></td><td>431.90 (-13.12%)</td><td>305.00 <b>(+29.13%)</b></td><td>118.71 <b>(-86.16%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2283.00 (n/a)</td><td>764.50 (n/a)</td><td>497.10 (n/a)</td><td>236.20 (n/a)</td><td>857.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+0.64%)</td><td>0.02 (-18.07%)</td><td>0.02 <b>(-26.69%)</b></td><td>0.01 (-17.98%)</td><td>0.01 (-1.07%)</td><td>634.30 <b>(+21.93%)</b></td><td>464.26 <b>(+23.09%)</b></td><td>499.70 <b>(+36.42%)</b></td><td>250.90 (-0.63%)</td><td>140.12 (+14.02%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.20 (n/a)</td><td>377.18 (n/a)</td><td>366.30 (n/a)</td><td>252.50 (n/a)</td><td>122.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (+18.51%)</td><td>0.05 (+3.59%)</td><td>0.03 <b>(-37.79%)</b></td><td>0.03 <b>(+268.14%)</b></td><td>0.02 (+2.60%)</td><td>555.60 <b>(-72.84%)</b></td><td>408.08 <b>(-37.18%)</b></td><td>501.80 <b>(+60.73%)</b></td><td>208.60 (-15.61%)</td><td>168.75 <b>(-78.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2045.40 (n/a)</td><td>649.58 (n/a)</td><td>312.20 (n/a)</td><td>247.20 (n/a)</td><td>781.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (+2.39%)</td><td>0.05 (+1.46%)</td><td>0.05 (-8.13%)</td><td>0.03 (-12.24%)</td><td>0.02 (+2.51%)</td><td>543.20 (+13.95%)</td><td>338.56 (-0.55%)</td><td>306.90 (+8.83%)</td><td>234.90 (-2.33%)</td><td>124.75 (+11.57%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>476.70 (n/a)</td><td>340.42 (n/a)</td><td>282.00 (n/a)</td><td>240.50 (n/a)</td><td>111.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-13.45%)</td><td>0.05 (-10.27%)</td><td>0.06 (-14.15%)</td><td>0.03 (+6.30%)</td><td>0.02 (-12.89%)</td><td>614.70 (-5.92%)</td><td>387.46 (+8.77%)</td><td>283.60 (+16.47%)</td><td>219.10 (+15.56%)</td><td>191.09 (-2.35%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>653.40 (n/a)</td><td>356.22 (n/a)</td><td>243.50 (n/a)</td><td>189.60 (n/a)</td><td>195.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-18.35%)</td><td>0.06 (-3.11%)</td><td>0.06 (-10.77%)</td><td>0.04 <b>(+30.71%)</b></td><td>0.01 <b>(-50.93%)</b></td><td>417.60 <b>(-23.49%)</b></td><td>299.08 (-9.02%)</td><td>292.60 (+12.06%)</td><td>229.90 <b>(+22.48%)</b></td><td>72.42 <b>(-53.39%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.80 (n/a)</td><td>328.74 (n/a)</td><td>261.10 (n/a)</td><td>187.70 (n/a)</td><td>155.36 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 <b>(+21.79%)</b></td><td>0.05 <b>(+31.18%)</b></td><td>0.06 <b>(+69.51%)</b></td><td>0.03 (+3.58%)</td><td>0.02 <b>(+67.71%)</b></td><td>495.30 (-3.45%)</td><td>345.40 (-19.70%)</td><td>276.10 <b>(-41.00%)</b></td><td>239.20 (-17.89%)</td><td>121.28 <b>(+39.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>513.00 (n/a)</td><td>430.12 (n/a)</td><td>468.00 (n/a)</td><td>291.30 (n/a)</td><td>86.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-14.68%)</td><td>0.04 <b>(-25.80%)</b></td><td>0.04 <b>(-35.10%)</b></td><td>0.03 (+2.73%)</td><td>0.01 <b>(-24.62%)</b></td><td>511.40 (-2.66%)</td><td>419.72 <b>(+30.71%)</b></td><td>416.50 <b>(+54.09%)</b></td><td>275.10 (+17.21%)</td><td>93.39 <b>(-20.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>525.40 (n/a)</td><td>321.12 (n/a)</td><td>270.30 (n/a)</td><td>234.70 (n/a)</td><td>117.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-3.66%)</td><td>0.04 (-8.52%)</td><td>0.03 (-17.53%)</td><td>0.03 (-16.75%)</td><td>0.01 <b>(+34.83%)</b></td><td>518.60 <b>(+20.13%)</b></td><td>447.86 (+12.02%)</td><td>512.70 <b>(+21.26%)</b></td><td>314.70 (+3.79%)</td><td>96.04 <b>(+76.99%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>431.70 (n/a)</td><td>399.80 (n/a)</td><td>422.80 (n/a)</td><td>303.20 (n/a)</td><td>54.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (+14.06%)</td><td>0.04 (-2.00%)</td><td>0.04 (-10.75%)</td><td>0.02 <b>(-42.69%)</b></td><td>0.02 <b>(+69.99%)</b></td><td>991.20 <b>(+74.48%)</b></td><td>488.78 <b>(+22.37%)</b></td><td>410.90 (+12.05%)</td><td>251.40 (-12.31%)</td><td>303.31 <b>(+153.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>399.42 (n/a)</td><td>366.70 (n/a)</td><td>286.70 (n/a)</td><td>119.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 <b>(-23.26%)</b></td><td>0.04 (-8.23%)</td><td>0.04 (+1.30%)</td><td>0.03 <b>(+25.91%)</b></td><td>0.01 <b>(-43.71%)</b></td><td>586.80 <b>(-20.57%)</b></td><td>442.32 (-2.68%)</td><td>424.50 (-1.28%)</td><td>316.80 <b>(+30.32%)</b></td><td>125.64 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>738.80 (n/a)</td><td>454.48 (n/a)</td><td>430.00 (n/a)</td><td>243.10 (n/a)</td><td>210.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 <b>(-22.17%)</b></td><td>0.04 (+11.21%)</td><td>0.05 <b>(+37.88%)</b></td><td>0.03 <b>(+59.72%)</b></td><td>0.01 <b>(-31.07%)</b></td><td>612.50 <b>(-37.39%)</b></td><td>435.56 (-19.21%)</td><td>339.10 <b>(-27.48%)</b></td><td>302.90 <b>(+28.46%)</b></td><td>158.46 <b>(-41.98%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>978.30 (n/a)</td><td>539.12 (n/a)</td><td>467.60 (n/a)</td><td>235.80 (n/a)</td><td>273.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 <b>(+23.98%)</b></td><td>0.04 (+8.75%)</td><td>0.05 <b>(+32.72%)</b></td><td>0.03 (+8.04%)</td><td>0.02 <b>(+32.57%)</b></td><td>591.10 (-7.44%)</td><td>417.78 (-4.97%)</td><td>342.60 <b>(-24.65%)</b></td><td>254.10 (-19.33%)</td><td>150.23 (+12.11%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>638.60 (n/a)</td><td>439.62 (n/a)</td><td>454.70 (n/a)</td><td>315.00 (n/a)</td><td>134.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-5.64%)</td><td>0.04 (-4.50%)</td><td>0.04 <b>(-27.94%)</b></td><td>0.02 (-8.77%)</td><td>0.02 (+0.42%)</td><td>774.40 (+9.61%)</td><td>437.52 (+5.49%)</td><td>454.30 <b>(+38.76%)</b></td><td>244.30 (+5.99%)</td><td>215.97 (+6.77%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>706.50 (n/a)</td><td>414.76 (n/a)</td><td>327.40 (n/a)</td><td>230.50 (n/a)</td><td>202.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (+11.41%)</td><td>0.12 (+4.92%)</td><td>0.13 (+2.28%)</td><td>0.08 (+15.05%)</td><td>0.04 <b>(+36.33%)</b></td><td>398.40 (-13.07%)</td><td>288.92 (-1.97%)</td><td>244.90 (-2.24%)</td><td>199.40 (-10.22%)</td><td>100.46 (+5.58%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>458.30 (n/a)</td><td>294.72 (n/a)</td><td>250.50 (n/a)</td><td>222.10 (n/a)</td><td>95.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (+2.70%)</td><td>0.11 (-7.22%)</td><td>0.12 (+2.61%)</td><td>0.07 (-13.74%)</td><td>0.03 <b>(+50.42%)</b></td><td>456.50 (+15.92%)</td><td>330.96 (+12.64%)</td><td>282.10 (-2.52%)</td><td>240.10 (-2.64%)</td><td>102.57 <b>(+71.34%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>393.80 (n/a)</td><td>293.82 (n/a)</td><td>289.40 (n/a)</td><td>246.60 (n/a)</td><td>59.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-10.17%)</td><td>0.09 (-5.18%)</td><td>0.11 (-18.70%)</td><td>0.06 <b>(+312.49%)</b></td><td>0.03 <b>(-43.05%)</b></td><td>591.30 <b>(-75.76%)</b></td><td>388.42 <b>(-46.51%)</b></td><td>300.30 <b>(+23.02%)</b></td><td>256.60 (+11.32%)</td><td>152.91 <b>(-84.13%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2439.20 (n/a)</td><td>726.12 (n/a)</td><td>244.10 (n/a)</td><td>230.50 (n/a)</td><td>963.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-9.20%)</td><td>0.08 <b>(-25.21%)</b></td><td>0.07 <b>(-44.30%)</b></td><td>0.07 (+13.62%)</td><td>0.02 <b>(-29.21%)</b></td><td>483.20 (-11.99%)</td><td>415.96 <b>(+26.73%)</b></td><td>445.90 <b>(+79.51%)</b></td><td>258.00 (+10.16%)</td><td>90.56 <b>(-32.68%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>549.00 (n/a)</td><td>328.22 (n/a)</td><td>248.40 (n/a)</td><td>234.20 (n/a)</td><td>134.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (+4.14%)</td><td>0.09 (-16.84%)</td><td>0.08 <b>(-33.73%)</b></td><td>0.07 (-10.20%)</td><td>0.03 <b>(+28.88%)</b></td><td>469.40 (+11.36%)</td><td>371.46 <b>(+23.94%)</b></td><td>420.80 <b>(+50.88%)</b></td><td>231.10 (-3.99%)</td><td>100.87 <b>(+37.34%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>421.50 (n/a)</td><td>299.70 (n/a)</td><td>278.90 (n/a)</td><td>240.70 (n/a)</td><td>73.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (+1.86%)</td><td>0.10 (-8.35%)</td><td>0.09 <b>(-27.17%)</b></td><td>0.06 (+13.90%)</td><td>0.04 (+6.44%)</td><td>540.30 (-12.20%)</td><td>370.00 (+7.86%)</td><td>376.50 <b>(+37.31%)</b></td><td>240.90 (-1.79%)</td><td>130.94 (-16.09%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.40 (n/a)</td><td>343.04 (n/a)</td><td>274.20 (n/a)</td><td>245.30 (n/a)</td><td>156.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 <b>(+41.74%)</b></td><td>0.12 <b>(+20.17%)</b></td><td>0.12 (+3.20%)</td><td>0.06 (+6.42%)</td><td>0.05 <b>(+37.93%)</b></td><td>541.20 (-6.04%)</td><td>312.86 (-14.71%)</td><td>279.10 (-3.09%)</td><td>174.20 <b>(-29.47%)</b></td><td>138.31 (-4.26%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>576.00 (n/a)</td><td>366.80 (n/a)</td><td>288.00 (n/a)</td><td>247.00 (n/a)</td><td>144.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (-8.84%)</td><td>0.09 <b>(-24.28%)</b></td><td>0.07 <b>(-50.50%)</b></td><td>0.06 <b>(-24.09%)</b></td><td>0.04 (-3.83%)</td><td>580.60 <b>(+31.74%)</b></td><td>425.96 <b>(+35.01%)</b></td><td>493.10 <b>(+102.01%)</b></td><td>234.90 (+9.66%)</td><td>148.46 <b>(+30.83%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>440.70 (n/a)</td><td>315.50 (n/a)</td><td>244.10 (n/a)</td><td>214.20 (n/a)</td><td>113.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (-4.04%)</td><td>0.10 <b>(-25.08%)</b></td><td>0.08 <b>(-37.47%)</b></td><td>0.06 <b>(-40.57%)</b></td><td>0.04 <b>(+87.61%)</b></td><td>547.00 <b>(+68.26%)</b></td><td>381.04 <b>(+46.90%)</b></td><td>398.20 <b>(+59.92%)</b></td><td>223.70 (+4.19%)</td><td>137.66 <b>(+220.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>325.10 (n/a)</td><td>259.38 (n/a)</td><td>249.00 (n/a)</td><td>214.70 (n/a)</td><td>42.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (+2.22%)</td><td>0.09 (-15.22%)</td><td>0.11 (-7.46%)</td><td>0.02 <b>(-70.94%)</b></td><td>0.05 <b>(+36.36%)</b></td><td>1874.20 <b>(+244.14%)</b></td><td>652.52 <b>(+81.62%)</b></td><td>296.60 (+8.05%)</td><td>244.70 (-2.16%)</td><td>693.39 <b>(+394.44%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.60 (n/a)</td><td>359.28 (n/a)</td><td>274.50 (n/a)</td><td>250.10 (n/a)</td><td>140.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 <b>(-29.11%)</b></td><td>0.07 (-10.62%)</td><td>0.07 (+13.22%)</td><td>0.02 <b>(-68.75%)</b></td><td>0.04 (-15.93%)</td><td>1874.50 <b>(+220.04%)</b></td><td>695.08 <b>(+49.67%)</b></td><td>474.40 (-11.67%)</td><td>270.50 <b>(+41.03%)</b></td><td>669.63 <b>(+316.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>585.70 (n/a)</td><td>464.42 (n/a)</td><td>537.10 (n/a)</td><td>191.80 (n/a)</td><td>160.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (-3.47%)</td><td>0.08 <b>(-20.27%)</b></td><td>0.09 (-15.91%)</td><td>0.05 <b>(-24.53%)</b></td><td>0.03 <b>(+36.10%)</b></td><td>671.00 <b>(+32.50%)</b></td><td>446.18 <b>(+35.49%)</b></td><td>348.80 (+18.92%)</td><td>272.90 (+3.61%)</td><td>185.32 <b>(+85.70%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>506.40 (n/a)</td><td>329.32 (n/a)</td><td>293.30 (n/a)</td><td>263.40 (n/a)</td><td>99.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-6.59%)</td><td>0.08 (+15.76%)</td><td>0.08 <b>(+43.57%)</b></td><td>0.05 (+12.03%)</td><td>0.02 <b>(-31.10%)</b></td><td>476.50 (-10.73%)</td><td>317.94 (-18.67%)</td><td>305.10 <b>(-30.34%)</b></td><td>238.60 (+7.04%)</td><td>93.38 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>533.80 (n/a)</td><td>390.92 (n/a)</td><td>438.00 (n/a)</td><td>222.90 (n/a)</td><td>136.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 <b>(+23.09%)</b></td><td>0.15 (-11.81%)</td><td>0.17 (-1.27%)</td><td>0.03 <b>(-83.47%)</b></td><td>0.07 <b>(+641.05%)</b></td><td>1919.40 <b>(+504.92%)</b></td><td>600.04 <b>(+110.22%)</b></td><td>281.60 (+1.26%)</td><td>224.40 (-18.73%)</td><td>738.04 <b>(+4039.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>317.30 (n/a)</td><td>285.44 (n/a)</td><td>278.10 (n/a)</td><td>276.10 (n/a)</td><td>17.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.92 (-10.47%)</td><td>3.03 <b>(-24.34%)</b></td><td>2.71 <b>(-33.02%)</b></td><td>2.34 <b>(-36.79%)</b></td><td>0.68 <b>(+153.60%)</b></td><td>4473.00 <b>(+58.20%)</b></td><td>3593.54 <b>(+36.82%)</b></td><td>3874.40 <b>(+49.30%)</b></td><td>2678.10 (+11.69%)</td><td>757.38 <b>(+337.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.37 (n/a)</td><td>4.01 (n/a)</td><td>4.04 (n/a)</td><td>3.71 (n/a)</td><td>0.27 (n/a)</td><td>2827.50 (n/a)</td><td>2626.54 (n/a)</td><td>2595.10 (n/a)</td><td>2397.70 (n/a)</td><td>172.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 <b>(+25.06%)</b></td><td>0.12 (-18.33%)</td><td>0.10 <b>(-31.51%)</b></td><td>0.06 <b>(-56.33%)</b></td><td>0.05 <b>(+512.97%)</b></td><td>723.00 <b>(+128.94%)</b></td><td>416.82 <b>(+43.54%)</b></td><td>411.40 <b>(+45.99%)</b></td><td>219.10 <b>(-20.04%)</b></td><td>193.47 <b>(+1019.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>315.80 (n/a)</td><td>290.38 (n/a)</td><td>281.80 (n/a)</td><td>274.00 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+3.83%)</td><td>0.02 (+5.22%)</td><td>0.02 (-7.37%)</td><td>0.02 <b>(+53.81%)</b></td><td>0.00 <b>(-38.08%)</b></td><td>304.20 <b>(-35.00%)</b></td><td>276.08 (-9.10%)</td><td>292.90 (+7.96%)</td><td>223.30 (-3.67%)</td><td>34.10 <b>(-63.61%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.00 (n/a)</td><td>303.72 (n/a)</td><td>271.30 (n/a)</td><td>231.80 (n/a)</td><td>93.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+25.83%)</b></td><td>0.01 <b>(+25.73%)</b></td><td>0.01 <b>(+39.62%)</b></td><td>0.01 (-5.66%)</td><td>0.00 <b>(+40.60%)</b></td><td>502.20 (+6.02%)</td><td>313.46 (-18.04%)</td><td>274.90 <b>(-28.37%)</b></td><td>237.70 <b>(-20.53%)</b></td><td>107.08 <b>(+28.95%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.70 (n/a)</td><td>382.44 (n/a)</td><td>383.80 (n/a)</td><td>299.10 (n/a)</td><td>83.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+5.86%)</td><td>0.02 (+1.15%)</td><td>0.02 <b>(+23.92%)</b></td><td>0.01 (-19.71%)</td><td>0.01 (+2.44%)</td><td>642.50 <b>(+24.54%)</b></td><td>389.18 (+1.39%)</td><td>335.00 (-19.30%)</td><td>227.00 (-5.53%)</td><td>168.48 <b>(+24.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>515.90 (n/a)</td><td>383.86 (n/a)</td><td>415.10 (n/a)</td><td>240.30 (n/a)</td><td>134.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-11.81%)</td><td>0.01 (-12.88%)</td><td>0.01 (-15.02%)</td><td>0.01 (-6.14%)</td><td>0.01 (-11.65%)</td><td>674.10 (+6.53%)</td><td>471.54 (+14.64%)</td><td>575.30 (+17.67%)</td><td>222.70 (+13.39%)</td><td>204.65 (+11.02%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.80 (n/a)</td><td>411.32 (n/a)</td><td>488.90 (n/a)</td><td>196.40 (n/a)</td><td>184.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-9.88%)</td><td>0.02 (+9.98%)</td><td>0.02 (+18.99%)</td><td>0.01 (+11.58%)</td><td>0.00 <b>(-28.31%)</b></td><td>559.00 (-10.39%)</td><td>349.28 (-15.35%)</td><td>286.80 (-15.97%)</td><td>268.90 (+10.93%)</td><td>122.39 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.80 (n/a)</td><td>412.60 (n/a)</td><td>341.30 (n/a)</td><td>242.40 (n/a)</td><td>177.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-5.43%)</td><td>0.01 (-12.70%)</td><td>0.01 <b>(-28.72%)</b></td><td>0.01 (-0.23%)</td><td>0.00 (+6.64%)</td><td>525.30 (+0.23%)</td><td>420.22 (+17.57%)</td><td>521.30 <b>(+40.32%)</b></td><td>255.90 (+5.74%)</td><td>141.10 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.10 (n/a)</td><td>357.42 (n/a)</td><td>371.50 (n/a)</td><td>242.00 (n/a)</td><td>115.62 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(-31.45%)</b></td><td>0.01 (-11.83%)</td><td>0.01 (+13.15%)</td><td>0.01 (+7.85%)</td><td>0.00 <b>(-65.40%)</b></td><td>510.40 (-7.28%)</td><td>423.40 (+3.08%)</td><td>417.00 (-11.62%)</td><td>340.00 <b>(+45.86%)</b></td><td>65.72 <b>(-53.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.50 (n/a)</td><td>410.74 (n/a)</td><td>471.80 (n/a)</td><td>233.10 (n/a)</td><td>141.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+10.35%)</td><td>0.01 <b>(+31.32%)</b></td><td>0.01 <b>(+26.20%)</b></td><td>0.01 <b>(+64.85%)</b></td><td>0.00 <b>(-22.86%)</b></td><td>420.70 <b>(-39.34%)</b></td><td>316.42 <b>(-28.52%)</b></td><td>320.30 <b>(-20.76%)</b></td><td>239.70 (-9.38%)</td><td>67.18 <b>(-57.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>693.50 (n/a)</td><td>442.68 (n/a)</td><td>404.20 (n/a)</td><td>264.50 (n/a)</td><td>158.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+4.72%)</td><td>0.01 (-10.10%)</td><td>0.01 <b>(-33.80%)</b></td><td>0.01 (-5.28%)</td><td>0.01 <b>(+32.87%)</b></td><td>567.20 (+5.58%)</td><td>400.76 (+16.53%)</td><td>453.40 <b>(+51.03%)</b></td><td>235.40 (-4.50%)</td><td>144.11 <b>(+24.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.20 (n/a)</td><td>343.90 (n/a)</td><td>300.20 (n/a)</td><td>246.50 (n/a)</td><td>115.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (-12.93%)</td><td>0.01 (-13.06%)</td><td>0.01 (-8.37%)</td><td>0.01 (-1.92%)</td><td>0.00 <b>(-34.63%)</b></td><td>543.90 (+1.97%)</td><td>411.96 (+10.66%)</td><td>401.60 (+9.13%)</td><td>289.30 (+14.85%)</td><td>91.27 <b>(-22.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.40 (n/a)</td><td>372.28 (n/a)</td><td>368.00 (n/a)</td><td>251.90 (n/a)</td><td>117.36 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-9.22%)</td><td>0.01 (-1.33%)</td><td>0.01 (+4.28%)</td><td>0.01 <b>(+23.87%)</b></td><td>0.00 <b>(-32.87%)</b></td><td>504.30 (-19.27%)</td><td>351.54 (-6.24%)</td><td>343.10 (-4.11%)</td><td>255.80 (+10.16%)</td><td>101.56 <b>(-37.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.70 (n/a)</td><td>374.92 (n/a)</td><td>357.80 (n/a)</td><td>232.20 (n/a)</td><td>162.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 <b>(+39.70%)</b></td><td>0.01 <b>(+21.78%)</b></td><td>0.01 <b>(+25.05%)</b></td><td>0.01 (-2.57%)</td><td>0.00 <b>(+110.95%)</b></td><td>605.20 (+2.63%)</td><td>455.02 (-14.53%)</td><td>448.20 <b>(-20.04%)</b></td><td>288.40 <b>(-28.42%)</b></td><td>115.31 <b>(+52.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.70 (n/a)</td><td>532.36 (n/a)</td><td>560.50 (n/a)</td><td>402.90 (n/a)</td><td>75.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (-5.86%)</td><td>0.02 (+16.80%)</td><td>0.02 (+16.94%)</td><td>0.02 <b>(+278.97%)</b></td><td>0.01 <b>(-30.10%)</b></td><td>521.40 <b>(-73.61%)</b></td><td>370.86 <b>(-45.95%)</b></td><td>384.20 (-14.47%)</td><td>241.40 (+6.20%)</td><td>126.42 <b>(-82.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1975.90 (n/a)</td><td>686.14 (n/a)</td><td>449.20 (n/a)</td><td>227.30 (n/a)</td><td>730.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-17.35%)</td><td>0.03 <b>(-29.33%)</b></td><td>0.02 <b>(-53.70%)</b></td><td>0.02 <b>(+223.63%)</b></td><td>0.01 <b>(-41.54%)</b></td><td>588.40 <b>(-69.10%)</b></td><td>439.06 <b>(-22.10%)</b></td><td>526.40 <b>(+116.00%)</b></td><td>252.70 <b>(+20.97%)</b></td><td>152.88 <b>(-79.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1904.20 (n/a)</td><td>563.60 (n/a)</td><td>243.70 (n/a)</td><td>208.90 (n/a)</td><td>749.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 <b>(+69.35%)</b></td><td>0.02 (+15.30%)</td><td>0.02 (+0.14%)</td><td>0.01 (-12.71%)</td><td>0.01 <b>(+208.41%)</b></td><td>697.10 (+14.56%)</td><td>494.80 (-1.57%)</td><td>509.50 (-0.14%)</td><td>218.30 <b>(-40.94%)</b></td><td>174.00 <b>(+92.38%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.50 (n/a)</td><td>502.70 (n/a)</td><td>510.20 (n/a)</td><td>369.60 (n/a)</td><td>90.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (-16.18%)</td><td>0.03 <b>(-29.68%)</b></td><td>0.02 <b>(-45.61%)</b></td><td>0.02 (-11.89%)</td><td>0.01 <b>(-22.95%)</b></td><td>560.90 (+13.50%)</td><td>442.10 <b>(+37.17%)</b></td><td>458.00 <b>(+83.86%)</b></td><td>230.30 (+19.33%)</td><td>127.07 (-6.40%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.20 (n/a)</td><td>322.30 (n/a)</td><td>249.10 (n/a)</td><td>193.00 (n/a)</td><td>135.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 <b>(+32.50%)</b></td><td>0.02 (-16.90%)</td><td>0.03 (-10.77%)</td><td>0.01 <b>(-71.95%)</b></td><td>0.01 <b>(+486.19%)</b></td><td>1068.90 <b>(+256.42%)</b></td><td>485.42 <b>(+74.99%)</b></td><td>311.50 (+12.05%)</td><td>185.30 <b>(-24.55%)</b></td><td>362.53 <b>(+1517.78%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>299.90 (n/a)</td><td>277.40 (n/a)</td><td>278.00 (n/a)</td><td>245.60 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (-4.73%)</td><td>0.03 (+14.55%)</td><td>0.03 <b>(+27.31%)</b></td><td>0.02 (+5.31%)</td><td>0.01 <b>(-23.23%)</b></td><td>476.00 (-5.05%)</td><td>356.28 (-15.18%)</td><td>360.10 <b>(-21.44%)</b></td><td>254.00 (+5.00%)</td><td>82.88 <b>(-21.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.30 (n/a)</td><td>420.06 (n/a)</td><td>458.40 (n/a)</td><td>241.90 (n/a)</td><td>106.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (-18.80%)</td><td>0.02 (+3.82%)</td><td>0.01 (-5.21%)</td><td>0.01 <b>(+134.82%)</b></td><td>0.01 (-19.68%)</td><td>804.40 <b>(-57.41%)</b></td><td>474.52 <b>(-31.24%)</b></td><td>555.10 (+5.51%)</td><td>223.00 <b>(+23.14%)</b></td><td>246.19 <b>(-64.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1888.80 (n/a)</td><td>690.08 (n/a)</td><td>526.10 (n/a)</td><td>181.10 (n/a)</td><td>687.97 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 <b>(+42.90%)</b></td><td>0.03 (-2.26%)</td><td>0.02 <b>(-26.32%)</b></td><td>0.01 <b>(-32.50%)</b></td><td>0.01 <b>(+193.44%)</b></td><td>637.60 <b>(+48.18%)</b></td><td>421.06 (+17.01%)</td><td>463.90 <b>(+35.72%)</b></td><td>211.60 <b>(-30.00%)</b></td><td>169.06 <b>(+194.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>430.30 (n/a)</td><td>359.84 (n/a)</td><td>341.80 (n/a)</td><td>302.30 (n/a)</td><td>57.37 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (-17.51%)</td><td>0.02 (-19.57%)</td><td>0.02 (-6.26%)</td><td>0.01 (+4.06%)</td><td>0.01 <b>(-33.45%)</b></td><td>625.20 (-3.90%)</td><td>497.72 (+13.50%)</td><td>536.40 (+6.68%)</td><td>259.20 <b>(+21.23%)</b></td><td>139.69 <b>(-26.63%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.60 (n/a)</td><td>438.52 (n/a)</td><td>502.80 (n/a)</td><td>213.80 (n/a)</td><td>190.39 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (+8.45%)</td><td>0.03 (+14.18%)</td><td>0.02 <b>(+21.43%)</b></td><td>0.02 (+1.81%)</td><td>0.01 (+10.16%)</td><td>543.40 (-1.77%)</td><td>360.94 (-12.03%)</td><td>384.10 (-17.65%)</td><td>212.00 (-7.79%)</td><td>134.74 (-4.28%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>410.28 (n/a)</td><td>466.40 (n/a)</td><td>229.90 (n/a)</td><td>140.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (+16.75%)</td><td>0.02 (+19.51%)</td><td>0.02 <b>(+27.36%)</b></td><td>0.01 <b>(-24.92%)</b></td><td>0.01 <b>(+59.10%)</b></td><td>802.20 <b>(+33.21%)</b></td><td>430.38 (-7.88%)</td><td>368.30 <b>(-21.47%)</b></td><td>266.60 (-14.33%)</td><td>217.18 <b>(+86.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.20 (n/a)</td><td>467.18 (n/a)</td><td>469.00 (n/a)</td><td>311.20 (n/a)</td><td>116.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (+14.47%)</td><td>0.06 <b>(+21.67%)</b></td><td>0.06 (+15.35%)</td><td>0.03 (-5.80%)</td><td>0.02 <b>(+21.85%)</b></td><td>525.40 (+6.16%)</td><td>308.50 (-15.69%)</td><td>276.10 (-13.31%)</td><td>207.90 (-12.65%)</td><td>126.39 (+12.35%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>494.90 (n/a)</td><td>365.90 (n/a)</td><td>318.50 (n/a)</td><td>238.00 (n/a)</td><td>112.49 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-0.65%)</td><td>0.07 <b>(+29.24%)</b></td><td>0.07 <b>(+55.99%)</b></td><td>0.05 <b>(+261.09%)</b></td><td>0.02 <b>(-38.21%)</b></td><td>525.80 <b>(-72.30%)</b></td><td>360.68 <b>(-49.99%)</b></td><td>331.90 <b>(-35.89%)</b></td><td>250.40 (+0.64%)</td><td>117.40 <b>(-82.75%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1898.50 (n/a)</td><td>721.28 (n/a)</td><td>517.70 (n/a)</td><td>248.80 (n/a)</td><td>680.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 <b>(+37.47%)</b></td><td>0.05 <b>(+21.43%)</b></td><td>0.04 (+5.65%)</td><td>0.03 (-1.25%)</td><td>0.02 <b>(+80.78%)</b></td><td>572.00 (+1.26%)</td><td>413.10 (-10.81%)</td><td>452.70 (-5.35%)</td><td>208.20 <b>(-27.25%)</b></td><td>152.46 <b>(+35.73%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>463.18 (n/a)</td><td>478.30 (n/a)</td><td>286.20 (n/a)</td><td>112.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-4.10%)</td><td>0.06 <b>(+22.60%)</b></td><td>0.07 <b>(+70.89%)</b></td><td>0.03 <b>(+316.85%)</b></td><td>0.02 <b>(-36.30%)</b></td><td>589.60 <b>(-76.01%)</b></td><td>372.38 <b>(-53.83%)</b></td><td>283.50 <b>(-41.47%)</b></td><td>247.90 (+4.25%)</td><td>147.56 <b>(-84.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2457.80 (n/a)</td><td>806.46 (n/a)</td><td>484.40 (n/a)</td><td>237.80 (n/a)</td><td>935.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (+1.90%)</td><td>0.04 <b>(-20.61%)</b></td><td>0.03 <b>(-20.72%)</b></td><td>0.02 <b>(-22.09%)</b></td><td>0.01 (+18.60%)</td><td>684.70 <b>(+28.34%)</b></td><td>499.24 <b>(+30.29%)</b></td><td>494.50 <b>(+26.12%)</b></td><td>288.70 (-1.87%)</td><td>145.44 <b>(+48.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.50 (n/a)</td><td>383.18 (n/a)</td><td>392.10 (n/a)</td><td>294.20 (n/a)</td><td>98.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (+5.53%)</td><td>0.07 (+1.97%)</td><td>0.07 (-4.26%)</td><td>0.05 <b>(+36.02%)</b></td><td>0.02 (-4.96%)</td><td>447.00 <b>(-26.48%)</b></td><td>329.98 (-5.61%)</td><td>300.30 (+4.45%)</td><td>247.90 (-5.24%)</td><td>90.60 <b>(-37.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.00 (n/a)</td><td>349.58 (n/a)</td><td>287.50 (n/a)</td><td>261.60 (n/a)</td><td>145.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-6.49%)</td><td>0.05 (+5.72%)</td><td>0.05 <b>(+31.50%)</b></td><td>0.03 (-2.13%)</td><td>0.01 (-6.16%)</td><td>525.00 (+2.18%)</td><td>382.22 (-5.11%)</td><td>327.40 <b>(-23.95%)</b></td><td>264.30 (+6.92%)</td><td>109.77 (+11.72%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>513.80 (n/a)</td><td>402.80 (n/a)</td><td>430.50 (n/a)</td><td>247.20 (n/a)</td><td>98.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 <b>(+29.54%)</b></td><td>0.05 <b>(+49.98%)</b></td><td>0.07 <b>(+93.96%)</b></td><td>0.03 (-3.14%)</td><td>0.02 <b>(+90.11%)</b></td><td>649.10 (+3.24%)</td><td>382.82 <b>(-27.70%)</b></td><td>278.60 <b>(-48.45%)</b></td><td>263.90 <b>(-22.81%)</b></td><td>169.52 <b>(+46.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>628.70 (n/a)</td><td>529.52 (n/a)</td><td>540.40 (n/a)</td><td>341.90 (n/a)</td><td>115.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (-9.82%)</td><td>0.04 (-17.92%)</td><td>0.03 <b>(-43.09%)</b></td><td>0.03 <b>(+189.69%)</b></td><td>0.02 <b>(-29.98%)</b></td><td>611.40 <b>(-65.48%)</b></td><td>439.90 <b>(-22.81%)</b></td><td>488.10 <b>(+75.70%)</b></td><td>241.30 (+10.89%)</td><td>157.24 <b>(-76.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1771.10 (n/a)</td><td>569.88 (n/a)</td><td>277.80 (n/a)</td><td>217.60 (n/a)</td><td>672.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 <b>(+34.69%)</b></td><td>0.06 <b>(+49.00%)</b></td><td>0.06 <b>(+74.79%)</b></td><td>0.05 <b>(+50.28%)</b></td><td>0.01 (-6.06%)</td><td>389.70 <b>(-33.45%)</b></td><td>319.64 <b>(-34.31%)</b></td><td>296.80 <b>(-42.78%)</b></td><td>276.80 <b>(-25.75%)</b></td><td>48.43 <b>(-53.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>486.62 (n/a)</td><td>518.70 (n/a)</td><td>372.80 (n/a)</td><td>103.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (+0.92%)</td><td>0.04 <b>(+21.51%)</b></td><td>0.05 <b>(+35.95%)</b></td><td>0.03 <b>(+202.16%)</b></td><td>0.01 <b>(-27.55%)</b></td><td>631.90 <b>(-66.90%)</b></td><td>415.38 <b>(-41.67%)</b></td><td>356.70 <b>(-26.45%)</b></td><td>291.10 (-0.89%)</td><td>145.67 <b>(-78.47%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1909.30 (n/a)</td><td>712.16 (n/a)</td><td>485.00 (n/a)</td><td>293.70 (n/a)</td><td>676.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (+1.71%)</td><td>0.10 <b>(+26.73%)</b></td><td>0.11 <b>(+74.08%)</b></td><td>0.07 <b>(+21.76%)</b></td><td>0.03 (-6.67%)</td><td>503.00 (-17.86%)</td><td>356.46 <b>(-23.04%)</b></td><td>298.50 <b>(-42.55%)</b></td><td>251.30 (-1.68%)</td><td>112.47 <b>(-21.94%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>612.40 (n/a)</td><td>463.18 (n/a)</td><td>519.60 (n/a)</td><td>255.60 (n/a)</td><td>144.09 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 <b>(-31.90%)</b></td><td>0.10 (-10.14%)</td><td>0.11 (-0.99%)</td><td>0.07 <b>(+28.71%)</b></td><td>0.02 <b>(-55.74%)</b></td><td>458.20 <b>(-22.30%)</b></td><td>327.60 (+0.50%)</td><td>294.60 (+0.99%)</td><td>287.40 <b>(+46.86%)</b></td><td>73.36 <b>(-52.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>589.70 (n/a)</td><td>325.98 (n/a)</td><td>291.70 (n/a)</td><td>195.70 (n/a)</td><td>153.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (-10.88%)</td><td>0.09 <b>(-22.39%)</b></td><td>0.09 <b>(-24.94%)</b></td><td>0.02 <b>(-68.36%)</b></td><td>0.05 (+18.33%)</td><td>1950.10 <b>(+216.06%)</b></td><td>716.18 <b>(+85.38%)</b></td><td>433.90 <b>(+33.22%)</b></td><td>273.70 (+12.22%)</td><td>703.50 <b>(+338.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>617.00 (n/a)</td><td>386.34 (n/a)</td><td>325.70 (n/a)</td><td>243.90 (n/a)</td><td>160.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (-14.82%)</td><td>0.09 (-16.99%)</td><td>0.11 (+0.96%)</td><td>0.06 (-19.14%)</td><td>0.03 (+4.20%)</td><td>589.70 <b>(+23.68%)</b></td><td>414.72 <b>(+26.08%)</b></td><td>309.60 (-0.93%)</td><td>279.40 (+17.39%)</td><td>160.02 <b>(+63.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>476.80 (n/a)</td><td>328.94 (n/a)</td><td>312.50 (n/a)</td><td>238.00 (n/a)</td><td>98.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 <b>(+30.93%)</b></td><td>0.14 <b>(+32.10%)</b></td><td>0.16 <b>(+81.40%)</b></td><td>0.08 (+6.32%)</td><td>0.05 <b>(+45.31%)</b></td><td>542.50 (-5.93%)</td><td>343.40 <b>(-20.96%)</b></td><td>260.80 <b>(-44.86%)</b></td><td>215.60 <b>(-23.60%)</b></td><td>141.97 (+8.32%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>576.70 (n/a)</td><td>434.46 (n/a)</td><td>473.00 (n/a)</td><td>282.20 (n/a)</td><td>131.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 <b>(+23.18%)</b></td><td>0.10 (+7.57%)</td><td>0.09 (-0.40%)</td><td>0.05 (-11.04%)</td><td>0.04 <b>(+40.71%)</b></td><td>622.50 (+12.41%)</td><td>382.82 (-1.54%)</td><td>370.60 (+0.41%)</td><td>194.80 (-18.80%)</td><td>160.34 <b>(+25.43%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.80 (n/a)</td><td>388.82 (n/a)</td><td>369.10 (n/a)</td><td>239.90 (n/a)</td><td>127.84 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 <b>(-35.45%)</b></td><td>0.10 (-3.41%)</td><td>0.08 (+7.69%)</td><td>0.06 (+2.87%)</td><td>0.04 <b>(-47.15%)</b></td><td>573.40 (-2.80%)</td><td>410.88 (-8.71%)</td><td>466.90 (-7.14%)</td><td>242.70 <b>(+54.88%)</b></td><td>143.14 (-16.86%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>589.90 (n/a)</td><td>450.10 (n/a)</td><td>502.80 (n/a)</td><td>156.70 (n/a)</td><td>172.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 <b>(-21.59%)</b></td><td>0.08 (+6.85%)</td><td>0.08 (+10.01%)</td><td>0.05 <b>(+27.17%)</b></td><td>0.03 <b>(-27.62%)</b></td><td>612.10 <b>(-21.36%)</b></td><td>429.52 (-12.62%)</td><td>427.50 (-9.10%)</td><td>275.30 <b>(+27.51%)</b></td><td>151.46 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>778.40 (n/a)</td><td>491.54 (n/a)</td><td>470.30 (n/a)</td><td>215.90 (n/a)</td><td>201.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (+3.19%)</td><td>0.10 <b>(+21.68%)</b></td><td>0.10 <b>(+39.13%)</b></td><td>0.06 (+7.46%)</td><td>0.04 (+5.77%)</td><td>576.20 (-6.94%)</td><td>396.76 (-17.00%)</td><td>359.10 <b>(-28.12%)</b></td><td>247.10 (-3.10%)</td><td>141.95 (+5.18%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>619.20 (n/a)</td><td>478.00 (n/a)</td><td>499.60 (n/a)</td><td>255.00 (n/a)</td><td>134.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-7.21%)</td><td>0.08 (-6.02%)</td><td>0.07 (-11.93%)</td><td>0.05 (-9.78%)</td><td>0.03 (+3.38%)</td><td>615.60 (+10.84%)</td><td>439.72 (+9.03%)</td><td>469.30 (+13.55%)</td><td>257.40 (+7.74%)</td><td>150.28 <b>(+25.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>555.40 (n/a)</td><td>403.30 (n/a)</td><td>413.30 (n/a)</td><td>238.90 (n/a)</td><td>119.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-7.60%)</td><td>0.06 (-3.49%)</td><td>0.05 <b>(-26.71%)</b></td><td>0.04 (-1.01%)</td><td>0.02 (+9.14%)</td><td>529.20 (+1.03%)</td><td>390.14 (+5.64%)</td><td>438.90 <b>(+36.43%)</b></td><td>247.40 (+8.22%)</td><td>131.78 (+10.67%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.80 (n/a)</td><td>369.32 (n/a)</td><td>321.70 (n/a)</td><td>228.60 (n/a)</td><td>119.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (+1.61%)</td><td>0.04 <b>(-28.76%)</b></td><td>0.04 <b>(-46.81%)</b></td><td>0.02 <b>(-46.48%)</b></td><td>0.02 (+0.06%)</td><td>1148.20 <b>(+86.85%)</b></td><td>584.84 <b>(+54.12%)</b></td><td>488.80 <b>(+88.00%)</b></td><td>242.60 (-1.62%)</td><td>341.07 <b>(+93.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.50 (n/a)</td><td>379.46 (n/a)</td><td>260.00 (n/a)</td><td>246.60 (n/a)</td><td>175.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-3.79%)</td><td>0.06 (+15.93%)</td><td>0.07 <b>(+62.76%)</b></td><td>0.04 (-0.11%)</td><td>0.02 (-9.12%)</td><td>584.30 (+0.10%)</td><td>356.40 (-15.17%)</td><td>302.30 <b>(-38.57%)</b></td><td>247.30 (+3.95%)</td><td>140.15 (-5.24%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>583.70 (n/a)</td><td>420.14 (n/a)</td><td>492.10 (n/a)</td><td>237.90 (n/a)</td><td>147.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (+0.97%)</td><td>0.06 <b>(+21.33%)</b></td><td>0.05 (+16.51%)</td><td>0.04 <b>(+88.98%)</b></td><td>0.02 (-7.03%)</td><td>577.50 <b>(-47.08%)</b></td><td>408.84 <b>(-25.98%)</b></td><td>410.10 (-14.17%)</td><td>231.20 (-0.99%)</td><td>155.31 <b>(-51.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1091.30 (n/a)</td><td>552.30 (n/a)</td><td>477.80 (n/a)</td><td>233.50 (n/a)</td><td>319.93 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (-9.47%)</td><td>0.07 (+12.08%)</td><td>0.08 <b>(+94.94%)</b></td><td>0.03 (-9.89%)</td><td>0.03 (-5.30%)</td><td>638.10 (+10.97%)</td><td>392.62 (-8.08%)</td><td>266.20 <b>(-48.70%)</b></td><td>203.70 (+10.47%)</td><td>210.65 <b>(+21.84%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>575.00 (n/a)</td><td>427.14 (n/a)</td><td>518.90 (n/a)</td><td>184.40 (n/a)</td><td>172.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 <b>(+57.80%)</b></td><td>0.07 <b>(+59.29%)</b></td><td>0.06 <b>(+32.60%)</b></td><td>0.04 <b>(+252.31%)</b></td><td>0.04 <b>(+46.20%)</b></td><td>567.30 <b>(-71.62%)</b></td><td>365.76 <b>(-51.55%)</b></td><td>363.30 <b>(-24.60%)</b></td><td>151.00 <b>(-36.63%)</b></td><td>164.16 <b>(-76.79%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1998.70 (n/a)</td><td>754.90 (n/a)</td><td>481.80 (n/a)</td><td>238.30 (n/a)</td><td>707.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (+17.53%)</td><td>0.09 <b>(+31.26%)</b></td><td>0.09 (+12.97%)</td><td>0.06 <b>(+30.12%)</b></td><td>0.03 (+3.05%)</td><td>430.70 <b>(-23.16%)</b></td><td>286.18 <b>(-26.65%)</b></td><td>275.60 (-11.50%)</td><td>208.70 (-14.89%)</td><td>89.98 <b>(-37.89%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>560.50 (n/a)</td><td>390.14 (n/a)</td><td>311.40 (n/a)</td><td>245.20 (n/a)</td><td>144.88 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 <b>(+22.17%)</b></td><td>0.08 <b>(+34.18%)</b></td><td>0.09 <b>(+44.07%)</b></td><td>0.05 (+8.76%)</td><td>0.02 <b>(+57.83%)</b></td><td>459.60 (-8.06%)</td><td>316.28 <b>(-24.03%)</b></td><td>285.30 <b>(-30.58%)</b></td><td>268.00 (-18.17%)</td><td>80.61 <b>(+23.18%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>416.30 (n/a)</td><td>411.00 (n/a)</td><td>327.50 (n/a)</td><td>65.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (+6.47%)</td><td>0.07 (-0.95%)</td><td>0.05 (-16.74%)</td><td>0.05 <b>(+25.42%)</b></td><td>0.02 (+5.12%)</td><td>529.10 <b>(-20.27%)</b></td><td>417.62 (+0.09%)</td><td>504.80 <b>(+20.10%)</b></td><td>246.80 (-6.09%)</td><td>136.81 (-15.30%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>663.60 (n/a)</td><td>417.24 (n/a)</td><td>420.30 (n/a)</td><td>262.80 (n/a)</td><td>161.52 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (+6.67%)</td><td>0.07 (+10.63%)</td><td>0.09 (+10.00%)</td><td>0.05 <b>(+22.16%)</b></td><td>0.02 (-3.21%)</td><td>512.90 (-18.15%)</td><td>359.18 (-12.48%)</td><td>270.30 (-9.08%)</td><td>264.00 (-6.25%)</td><td>125.66 <b>(-25.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>626.60 (n/a)</td><td>410.38 (n/a)</td><td>297.30 (n/a)</td><td>281.60 (n/a)</td><td>168.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 <b>(-21.81%)</b></td><td>0.05 <b>(-23.38%)</b></td><td>0.05 (-1.06%)</td><td>0.04 (-5.71%)</td><td>0.02 <b>(-46.84%)</b></td><td>607.20 (+6.06%)</td><td>500.64 (+18.42%)</td><td>532.80 (+1.06%)</td><td>300.80 <b>(+27.89%)</b></td><td>124.83 <b>(-26.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>572.50 (n/a)</td><td>422.78 (n/a)</td><td>527.20 (n/a)</td><td>235.20 (n/a)</td><td>170.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (+8.05%)</td><td>0.07 <b>(+31.52%)</b></td><td>0.08 <b>(+92.39%)</b></td><td>0.04 (-13.50%)</td><td>0.02 <b>(+46.47%)</b></td><td>684.60 (+15.60%)</td><td>420.64 (-18.05%)</td><td>298.90 <b>(-48.02%)</b></td><td>280.10 (-7.44%)</td><td>187.12 <b>(+52.25%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.20 (n/a)</td><td>513.28 (n/a)</td><td>575.00 (n/a)</td><td>302.60 (n/a)</td><td>122.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 <b>(+28.79%)</b></td><td>0.06 (+2.25%)</td><td>0.06 (-14.69%)</td><td>0.01 <b>(-70.02%)</b></td><td>0.04 <b>(+64.65%)</b></td><td>1878.60 <b>(+233.50%)</b></td><td>609.66 <b>(+69.56%)</b></td><td>298.40 (+17.20%)</td><td>169.40 <b>(-22.36%)</b></td><td>720.68 <b>(+333.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.30 (n/a)</td><td>359.56 (n/a)</td><td>254.60 (n/a)</td><td>218.20 (n/a)</td><td>166.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-7.65%)</td><td>0.05 (-3.79%)</td><td>0.05 (-19.22%)</td><td>0.04 <b>(+26.34%)</b></td><td>0.01 <b>(-34.05%)</b></td><td>486.70 <b>(-20.84%)</b></td><td>389.52 (-1.80%)</td><td>383.60 <b>(+23.78%)</b></td><td>302.90 (+8.29%)</td><td>82.23 <b>(-43.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.80 (n/a)</td><td>396.64 (n/a)</td><td>309.90 (n/a)</td><td>279.70 (n/a)</td><td>144.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (-10.62%)</td><td>0.06 (+16.71%)</td><td>0.06 <b>(+52.86%)</b></td><td>0.04 <b>(+20.05%)</b></td><td>0.02 <b>(-26.64%)</b></td><td>465.60 (-16.69%)</td><td>325.34 (-19.80%)</td><td>299.50 <b>(-34.58%)</b></td><td>234.70 (+11.87%)</td><td>98.44 <b>(-33.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.90 (n/a)</td><td>405.68 (n/a)</td><td>457.80 (n/a)</td><td>209.80 (n/a)</td><td>147.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 <b>(-27.66%)</b></td><td>0.04 (-8.33%)</td><td>0.04 (+17.99%)</td><td>0.02 (-2.52%)</td><td>0.01 <b>(-41.17%)</b></td><td>777.40 (+2.59%)</td><td>475.78 (+0.72%)</td><td>435.90 (-15.26%)</td><td>307.70 <b>(+38.23%)</b></td><td>182.85 (-11.49%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>757.80 (n/a)</td><td>472.40 (n/a)</td><td>514.40 (n/a)</td><td>222.60 (n/a)</td><td>206.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (-16.25%)</td><td>0.05 <b>(-20.97%)</b></td><td>0.05 <b>(-27.15%)</b></td><td>0.03 (+16.24%)</td><td>0.02 <b>(-23.49%)</b></td><td>584.10 (-13.98%)</td><td>424.44 (+19.55%)</td><td>393.20 <b>(+37.24%)</b></td><td>286.30 (+19.44%)</td><td>139.60 <b>(-24.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>679.00 (n/a)</td><td>355.04 (n/a)</td><td>286.50 (n/a)</td><td>239.70 (n/a)</td><td>183.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 <b>(-20.96%)</b></td><td>0.05 <b>(-24.80%)</b></td><td>0.04 <b>(-37.03%)</b></td><td>0.03 (-3.19%)</td><td>0.02 <b>(-29.53%)</b></td><td>593.10 (+3.31%)</td><td>448.94 <b>(+21.23%)</b></td><td>469.80 <b>(+58.82%)</b></td><td>211.30 <b>(+26.53%)</b></td><td>145.68 <b>(-22.60%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>574.10 (n/a)</td><td>370.32 (n/a)</td><td>295.80 (n/a)</td><td>167.00 (n/a)</td><td>188.21 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.39 (-14.96%)</td><td>0.24 <b>(-22.53%)</b></td><td>0.22 <b>(-28.24%)</b></td><td>0.16 (+1.49%)</td><td>0.09 <b>(-22.02%)</b></td><td>601.90 (-1.47%)</td><td>439.10 <b>(+23.80%)</b></td><td>446.20 <b>(+39.35%)</b></td><td>252.20 (+17.58%)</td><td>124.46 (-18.77%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>610.90 (n/a)</td><td>354.68 (n/a)</td><td>320.20 (n/a)</td><td>214.50 (n/a)</td><td>153.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.39 (-6.13%)</td><td>0.28 (-1.49%)</td><td>0.26 (-4.63%)</td><td>0.19 (+1.04%)</td><td>0.08 (-14.18%)</td><td>509.90 (-1.03%)</td><td>379.90 (-0.66%)</td><td>372.00 (+4.85%)</td><td>250.10 (+6.52%)</td><td>106.65 (-13.28%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>515.20 (n/a)</td><td>382.44 (n/a)</td><td>354.80 (n/a)</td><td>234.80 (n/a)</td><td>122.98 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.35 (-12.80%)</td><td>0.23 <b>(-21.72%)</b></td><td>0.17 <b>(-42.86%)</b></td><td>0.15 <b>(-25.97%)</b></td><td>0.10 <b>(+40.07%)</b></td><td>673.00 <b>(+35.06%)</b></td><td>488.66 <b>(+40.53%)</b></td><td>565.40 <b>(+74.99%)</b></td><td>279.40 (+14.65%)</td><td>190.96 <b>(+103.82%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>498.30 (n/a)</td><td>347.72 (n/a)</td><td>323.10 (n/a)</td><td>243.70 (n/a)</td><td>93.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 <b>(-27.30%)</b></td><td>0.18 <b>(-29.65%)</b></td><td>0.18 <b>(-24.28%)</b></td><td>0.14 (-13.98%)</td><td>0.04 <b>(-35.66%)</b></td><td>527.40 (+16.27%)</td><td>435.82 <b>(+39.52%)</b></td><td>418.30 <b>(+32.04%)</b></td><td>304.10 <b>(+37.54%)</b></td><td>93.43 (+4.67%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>453.60 (n/a)</td><td>312.36 (n/a)</td><td>316.80 (n/a)</td><td>221.10 (n/a)</td><td>89.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (-10.15%)</td><td>0.14 <b>(-21.41%)</b></td><td>0.15 (-2.74%)</td><td>0.04 <b>(-69.17%)</b></td><td>0.07 <b>(+23.11%)</b></td><td>2017.40 <b>(+224.34%)</b></td><td>778.20 <b>(+74.39%)</b></td><td>488.10 (+2.80%)</td><td>335.90 (+11.30%)</td><td>702.14 <b>(+412.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>622.00 (n/a)</td><td>446.24 (n/a)</td><td>474.80 (n/a)</td><td>301.80 (n/a)</td><td>136.94 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.29 (-2.37%)</td><td>0.23 <b>(+54.80%)</b></td><td>0.24 <b>(+91.75%)</b></td><td>0.13 <b>(+331.88%)</b></td><td>0.06 <b>(-36.87%)</b></td><td>566.40 <b>(-76.84%)</b></td><td>352.92 <b>(-59.60%)</b></td><td>308.40 <b>(-47.84%)</b></td><td>251.40 (+2.44%)</td><td>124.98 <b>(-85.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.30 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.10 (n/a)</td><td>2446.10 (n/a)</td><td>873.64 (n/a)</td><td>591.30 (n/a)</td><td>245.40 (n/a)</td><td>890.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (-10.69%)</td><td>0.13 (+1.54%)</td><td>0.13 (+7.57%)</td><td>0.10 (+11.33%)</td><td>0.02 <b>(-30.70%)</b></td><td>384.10 (-10.17%)</td><td>288.06 (-4.41%)</td><td>280.60 (-7.06%)</td><td>224.60 (+11.96%)</td><td>59.67 <b>(-28.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>427.60 (n/a)</td><td>301.34 (n/a)</td><td>301.90 (n/a)</td><td>200.60 (n/a)</td><td>83.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.18 <b>(+21.45%)</b></td><td>0.12 <b>(+21.63%)</b></td><td>0.12 <b>(+56.35%)</b></td><td>0.07 (+9.78%)</td><td>0.05 <b>(+30.41%)</b></td><td>532.50 (-8.91%)</td><td>361.14 (-14.91%)</td><td>295.10 <b>(-36.04%)</b></td><td>208.00 (-17.66%)</td><td>146.79 (+6.00%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.60 (n/a)</td><td>424.44 (n/a)</td><td>461.40 (n/a)</td><td>252.60 (n/a)</td><td>138.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (-8.84%)</td><td>0.10 (-12.89%)</td><td>0.09 <b>(-27.54%)</b></td><td>0.06 (+0.87%)</td><td>0.04 <b>(-26.81%)</b></td><td>599.50 (-0.88%)</td><td>414.00 (+5.86%)</td><td>406.40 <b>(+38.00%)</b></td><td>245.50 (+9.70%)</td><td>146.17 <b>(-24.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>604.80 (n/a)</td><td>391.08 (n/a)</td><td>294.50 (n/a)</td><td>223.80 (n/a)</td><td>193.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (+10.60%)</td><td>0.09 (-11.88%)</td><td>0.07 <b>(-29.20%)</b></td><td>0.03 <b>(-49.49%)</b></td><td>0.05 <b>(+50.00%)</b></td><td>1338.10 <b>(+98.00%)</b></td><td>596.48 <b>(+42.77%)</b></td><td>518.60 <b>(+41.23%)</b></td><td>253.30 (-9.57%)</td><td>435.79 <b>(+171.01%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>675.80 (n/a)</td><td>417.80 (n/a)</td><td>367.20 (n/a)</td><td>280.10 (n/a)</td><td>160.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 <b>(+35.17%)</b></td><td>0.12 <b>(+45.92%)</b></td><td>0.12 <b>(+56.14%)</b></td><td>0.08 <b>(+35.60%)</b></td><td>0.04 <b>(+34.18%)</b></td><td>450.10 <b>(-26.25%)</b></td><td>336.24 <b>(-31.35%)</b></td><td>305.60 <b>(-35.96%)</b></td><td>216.70 <b>(-26.02%)</b></td><td>97.98 <b>(-23.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>610.30 (n/a)</td><td>489.82 (n/a)</td><td>477.20 (n/a)</td><td>292.90 (n/a)</td><td>128.49 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (-8.28%)</td><td>0.10 (-1.44%)</td><td>0.08 (-10.08%)</td><td>0.06 (-12.99%)</td><td>0.03 (+8.20%)</td><td>592.90 (+14.93%)</td><td>403.62 (+4.02%)</td><td>434.00 (+11.20%)</td><td>266.00 (+9.02%)</td><td>137.29 <b>(+26.42%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>515.90 (n/a)</td><td>388.02 (n/a)</td><td>390.30 (n/a)</td><td>244.00 (n/a)</td><td>108.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (-16.55%)</td><td>0.11 (-18.68%)</td><td>0.09 <b>(-40.78%)</b></td><td>0.07 (-3.84%)</td><td>0.03 <b>(-28.89%)</b></td><td>550.00 (+3.99%)</td><td>420.06 (+17.20%)</td><td>468.80 <b>(+68.88%)</b></td><td>286.00 (+19.87%)</td><td>121.84 (-16.23%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>528.90 (n/a)</td><td>358.42 (n/a)</td><td>277.60 (n/a)</td><td>238.60 (n/a)</td><td>145.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (+5.20%)</td><td>0.15 <b>(+21.28%)</b></td><td>0.14 (+16.06%)</td><td>0.13 <b>(+59.67%)</b></td><td>0.01 <b>(-50.01%)</b></td><td>304.00 <b>(-37.37%)</b></td><td>280.98 <b>(-20.41%)</b></td><td>291.40 (-13.84%)</td><td>246.40 (-4.97%)</td><td>24.44 <b>(-70.75%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>485.40 (n/a)</td><td>353.04 (n/a)</td><td>338.20 (n/a)</td><td>259.30 (n/a)</td><td>83.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (-3.03%)</td><td>0.13 <b>(+24.58%)</b></td><td>0.14 <b>(+79.94%)</b></td><td>0.10 <b>(+34.79%)</b></td><td>0.04 <b>(-24.67%)</b></td><td>426.50 <b>(-25.81%)</b></td><td>324.92 <b>(-25.62%)</b></td><td>288.00 <b>(-44.43%)</b></td><td>244.30 (+3.12%)</td><td>91.30 <b>(-43.50%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>574.90 (n/a)</td><td>436.82 (n/a)</td><td>518.30 (n/a)</td><td>236.90 (n/a)</td><td>161.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (-14.94%)</td><td>0.12 (-1.84%)</td><td>0.13 (-7.70%)</td><td>0.07 <b>(+249.60%)</b></td><td>0.04 <b>(-40.18%)</b></td><td>588.60 <b>(-71.40%)</b></td><td>395.54 <b>(-40.49%)</b></td><td>305.90 (+8.32%)</td><td>266.50 (+17.56%)</td><td>154.01 <b>(-80.42%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2057.70 (n/a)</td><td>664.66 (n/a)</td><td>282.40 (n/a)</td><td>226.70 (n/a)</td><td>786.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.23 (+6.03%)</td><td>0.12 (+2.72%)</td><td>0.09 (-5.23%)</td><td>0.07 (+4.84%)</td><td>0.07 (+12.55%)</td><td>572.70 (-4.61%)</td><td>408.32 (+0.45%)</td><td>463.50 (+5.51%)</td><td>177.60 (-5.68%)</td><td>162.21 (+7.21%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>600.40 (n/a)</td><td>406.48 (n/a)</td><td>439.30 (n/a)</td><td>188.30 (n/a)</td><td>151.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.21 <b>(+64.96%)</b></td><td>0.11 <b>(+25.84%)</b></td><td>0.10 (+9.09%)</td><td>0.07 (+12.48%)</td><td>0.06 <b>(+132.30%)</b></td><td>564.50 (-11.09%)</td><td>415.42 (-12.54%)</td><td>420.40 (-8.33%)</td><td>191.30 <b>(-39.37%)</b></td><td>151.71 <b>(+24.78%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>634.90 (n/a)</td><td>474.98 (n/a)</td><td>458.60 (n/a)</td><td>315.50 (n/a)</td><td>121.58 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (+10.49%)</td><td>0.10 <b>(+31.32%)</b></td><td>0.12 <b>(+64.58%)</b></td><td>0.07 (+11.68%)</td><td>0.03 <b>(+29.27%)</b></td><td>521.80 (-10.47%)</td><td>363.96 <b>(-21.68%)</b></td><td>298.40 <b>(-39.24%)</b></td><td>253.70 (-9.49%)</td><td>126.81 (+12.29%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.80 (n/a)</td><td>464.68 (n/a)</td><td>491.10 (n/a)</td><td>280.30 (n/a)</td><td>112.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (-6.66%)</td><td>0.10 (+10.57%)</td><td>0.12 <b>(+59.13%)</b></td><td>0.06 (+0.89%)</td><td>0.03 (-7.27%)</td><td>584.20 (-0.88%)</td><td>375.46 (-10.31%)</td><td>286.30 <b>(-37.16%)</b></td><td>269.90 (+7.15%)</td><td>139.32 (-1.96%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>589.40 (n/a)</td><td>418.64 (n/a)</td><td>455.60 (n/a)</td><td>251.90 (n/a)</td><td>142.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (-5.36%)</td><td>0.11 (-0.27%)</td><td>0.12 (-3.39%)</td><td>0.07 <b>(+20.65%)</b></td><td>0.03 (-12.60%)</td><td>501.00 (-17.12%)</td><td>360.68 (-3.33%)</td><td>300.20 (+3.52%)</td><td>250.80 (+5.69%)</td><td>124.13 <b>(-21.22%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>604.50 (n/a)</td><td>373.10 (n/a)</td><td>290.00 (n/a)</td><td>237.30 (n/a)</td><td>157.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 <b>(-20.97%)</b></td><td>0.08 (-18.07%)</td><td>0.07 (-1.89%)</td><td>0.06 (+14.96%)</td><td>0.03 <b>(-44.22%)</b></td><td>576.20 (-13.00%)</td><td>471.54 (+6.26%)</td><td>500.90 (+1.93%)</td><td>266.30 <b>(+26.51%)</b></td><td>118.96 <b>(-41.95%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>662.30 (n/a)</td><td>443.74 (n/a)</td><td>491.40 (n/a)</td><td>210.50 (n/a)</td><td>204.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (+13.94%)</td><td>0.10 (+5.75%)</td><td>0.08 <b>(-21.92%)</b></td><td>0.06 <b>(+65.72%)</b></td><td>0.03 (-5.40%)</td><td>597.40 <b>(-39.66%)</b></td><td>400.82 (-15.00%)</td><td>423.80 <b>(+28.07%)</b></td><td>262.60 (-12.23%)</td><td>136.38 <b>(-53.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>990.10 (n/a)</td><td>471.58 (n/a)</td><td>330.90 (n/a)</td><td>299.20 (n/a)</td><td>294.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 <b>(-41.01%)</b></td><td>0.07 <b>(-25.39%)</b></td><td>0.05 <b>(-27.60%)</b></td><td>0.03 <b>(-39.02%)</b></td><td>0.03 <b>(-34.56%)</b></td><td>1036.90 <b>(+63.99%)</b></td><td>620.62 <b>(+37.32%)</b></td><td>653.40 <b>(+38.11%)</b></td><td>362.90 <b>(+69.50%)</b></td><td>276.97 <b>(+83.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>632.30 (n/a)</td><td>451.96 (n/a)</td><td>473.10 (n/a)</td><td>214.10 (n/a)</td><td>150.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.50 (+6.09%)</td><td>0.30 (-12.85%)</td><td>0.28 <b>(-29.08%)</b></td><td>0.12 <b>(-41.96%)</b></td><td>0.14 (+17.43%)</td><td>1051.60 <b>(+72.28%)</b></td><td>541.80 <b>(+26.69%)</b></td><td>475.30 <b>(+41.00%)</b></td><td>262.50 (-5.75%)</td><td>305.23 <b>(+86.10%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>610.40 (n/a)</td><td>427.66 (n/a)</td><td>337.10 (n/a)</td><td>278.50 (n/a)</td><td>164.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.41 (-13.27%)</td><td>0.26 <b>(-24.83%)</b></td><td>0.25 <b>(-42.14%)</b></td><td>0.15 (-8.41%)</td><td>0.09 <b>(-28.15%)</b></td><td>883.70 (+9.18%)</td><td>553.60 <b>(+25.93%)</b></td><td>534.60 <b>(+72.84%)</b></td><td>321.80 (+15.30%)</td><td>207.39 (-7.59%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.42 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>809.40 (n/a)</td><td>439.60 (n/a)</td><td>309.30 (n/a)</td><td>279.10 (n/a)</td><td>224.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 <b>(-53.79%)</b></td><td>0.20 <b>(-41.55%)</b></td><td>0.22 (-8.49%)</td><td>0.07 <b>(-68.58%)</b></td><td>0.07 <b>(-51.03%)</b></td><td>1893.20 <b>(+218.29%)</b></td><td>839.88 <b>(+86.85%)</b></td><td>595.50 (+9.27%)</td><td>552.60 <b>(+116.37%)</b></td><td>589.23 <b>(+248.90%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>594.80 (n/a)</td><td>449.50 (n/a)</td><td>545.00 (n/a)</td><td>255.40 (n/a)</td><td>168.88 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+2.51%)</td><td>0.01 (+19.74%)</td><td>0.01 <b>(+32.57%)</b></td><td>0.01 (+16.32%)</td><td>0.00 (-14.69%)</td><td>454.40 (-14.04%)</td><td>313.82 (-18.21%)</td><td>285.20 <b>(-24.57%)</b></td><td>269.70 (-2.46%)</td><td>79.12 <b>(-25.07%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.60 (n/a)</td><td>383.68 (n/a)</td><td>378.10 (n/a)</td><td>276.50 (n/a)</td><td>105.58 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (+11.98%)</td><td>0.01 (+0.57%)</td><td>0.01 (+0.85%)</td><td>0.01 (-19.36%)</td><td>0.00 <b>(+112.01%)</b></td><td>432.50 <b>(+24.00%)</b></td><td>305.98 (+2.55%)</td><td>291.50 (-0.85%)</td><td>244.50 (-10.70%)</td><td>73.94 <b>(+142.91%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>348.80 (n/a)</td><td>298.38 (n/a)</td><td>294.00 (n/a)</td><td>273.80 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+36.21%)</b></td><td>0.01 (-6.40%)</td><td>0.01 (-8.02%)</td><td>0.00 <b>(-52.01%)</b></td><td>0.00 <b>(+119.48%)</b></td><td>1193.00 <b>(+108.38%)</b></td><td>576.58 <b>(+32.09%)</b></td><td>464.60 (+8.73%)</td><td>246.80 <b>(-26.57%)</b></td><td>360.90 <b>(+261.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.50 (n/a)</td><td>436.50 (n/a)</td><td>427.30 (n/a)</td><td>336.10 (n/a)</td><td>99.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.71 (-0.88%)</td><td>6.07 (-3.69%)</td><td>7.30 (+0.69%)</td><td>3.75 <b>(+35.90%)</b></td><td>1.90 (-8.89%)</td><td>559.30 <b>(-26.42%)</b></td><td>379.08 (-2.13%)</td><td>287.20 (-0.69%)</td><td>272.20 (+0.89%)</td><td>135.52 <b>(-35.56%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.78 (n/a)</td><td>6.31 (n/a)</td><td>7.25 (n/a)</td><td>2.76 (n/a)</td><td>2.08 (n/a)</td><td>760.10 (n/a)</td><td>387.32 (n/a)</td><td>289.20 (n/a)</td><td>269.80 (n/a)</td><td>210.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.58 (+1.97%)</td><td>0.38 (-1.22%)</td><td>0.34 (-0.18%)</td><td>0.28 <b>(+24.25%)</b></td><td>0.12 (-11.13%)</td><td>463.70 (-19.52%)</td><td>370.48 (-2.46%)</td><td>386.90 (+0.18%)</td><td>226.00 (-1.95%)</td><td>87.81 <b>(-33.56%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>576.20 (n/a)</td><td>379.84 (n/a)</td><td>386.20 (n/a)</td><td>230.50 (n/a)</td><td>132.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.51 (-1.51%)</td><td>0.35 (+6.89%)</td><td>0.32 <b>(-22.33%)</b></td><td>0.23 <b>(+248.60%)</b></td><td>0.12 <b>(-32.87%)</b></td><td>573.30 <b>(-71.31%)</b></td><td>411.36 <b>(-40.56%)</b></td><td>414.20 <b>(+28.75%)</b></td><td>258.30 (+1.53%)</td><td>135.11 <b>(-81.75%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.52 (n/a)</td><td>0.33 (n/a)</td><td>0.41 (n/a)</td><td>0.07 (n/a)</td><td>0.18 (n/a)</td><td>1998.50 (n/a)</td><td>692.10 (n/a)</td><td>321.70 (n/a)</td><td>254.40 (n/a)</td><td>740.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.48 (-6.16%)</td><td>0.38 (+8.04%)</td><td>0.44 <b>(+38.25%)</b></td><td>0.24 (-7.28%)</td><td>0.11 (+6.56%)</td><td>552.50 (+7.85%)</td><td>377.82 (-5.71%)</td><td>300.90 <b>(-27.67%)</b></td><td>274.80 (+6.55%)</td><td>124.26 <b>(+22.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>512.30 (n/a)</td><td>400.72 (n/a)</td><td>416.00 (n/a)</td><td>257.90 (n/a)</td><td>101.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.34 <b>(-37.36%)</b></td><td>0.26 <b>(-30.64%)</b></td><td>0.26 (-20.00%)</td><td>0.12 <b>(-52.75%)</b></td><td>0.09 <b>(-33.72%)</b></td><td>1147.20 <b>(+111.62%)</b></td><td>596.68 <b>(+51.71%)</b></td><td>513.10 <b>(+24.99%)</b></td><td>392.90 <b>(+59.65%)</b></td><td>312.66 <b>(+140.11%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>542.10 (n/a)</td><td>393.30 (n/a)</td><td>410.50 (n/a)</td><td>246.10 (n/a)</td><td>130.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.44 <b>(-29.87%)</b></td><td>0.33 (-14.31%)</td><td>0.28 (-16.11%)</td><td>0.26 (-1.83%)</td><td>0.08 <b>(-43.36%)</b></td><td>502.60 (+1.86%)</td><td>422.20 (+11.63%)</td><td>470.20 (+19.19%)</td><td>300.00 <b>(+42.59%)</b></td><td>95.89 (-13.73%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.63 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>493.40 (n/a)</td><td>378.22 (n/a)</td><td>394.50 (n/a)</td><td>210.40 (n/a)</td><td>111.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (-7.75%)</td><td>0.01 (-6.13%)</td><td>0.01 <b>(-27.88%)</b></td><td>0.01 (+18.63%)</td><td>0.00 (-12.00%)</td><td>528.20 (-15.70%)</td><td>396.32 (+2.69%)</td><td>455.00 <b>(+38.63%)</b></td><td>253.70 (+8.37%)</td><td>124.53 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.60 (n/a)</td><td>385.92 (n/a)</td><td>328.20 (n/a)</td><td>234.10 (n/a)</td><td>161.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 <b>(+22.73%)</b></td><td>0.01 (+11.31%)</td><td>0.01 (+1.17%)</td><td>0.01 (+5.11%)</td><td>0.00 <b>(+31.44%)</b></td><td>514.30 (-4.86%)</td><td>355.58 (-7.69%)</td><td>303.40 (-1.17%)</td><td>229.10 (-18.53%)</td><td>131.81 (+4.36%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.60 (n/a)</td><td>385.22 (n/a)</td><td>307.00 (n/a)</td><td>281.20 (n/a)</td><td>126.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.00 (-12.50%)</td><td>0.00 (+14.29%)</td><td>0.00 <b>(+66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-28.31%)</b></td><td>16703.39 <b>(-27.49%)</b></td><td>9378.67 <b>(-31.07%)</b></td><td>8298.28 <b>(-48.36%)</b></td><td>5564.44 (+7.38%)</td><td>4384.85 <b>(-41.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23035.14 (n/a)</td><td>13605.68 (n/a)</td><td>16070.90 (n/a)</td><td>5182.08 (n/a)</td><td>7519.35 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.00 (-15.38%)</td><td>0.00 <b>(-34.88%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.67%)</b></td><td>21697.01 (+8.76%)</td><td>17445.67 <b>(+44.38%)</b></td><td>21057.78 <b>(+151.45%)</b></td><td>7530.58 (+16.28%)</td><td>6021.64 (-9.84%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19948.71 (n/a)</td><td>12083.52 (n/a)</td><td>8374.43 (n/a)</td><td>6475.99 (n/a)</td><td>6679.13 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>25278.45 (n/a)</td><td>21678.79 (n/a)</td><td>23343.96 (n/a)</td><td>13014.67 (n/a)</td><td>4928.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>24866.02 (n/a)</td><td>23715.52 (n/a)</td><td>24381.56 (n/a)</td><td>21221.93 (n/a)</td><td>1486.84 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-3.03%)</td><td>0.10 (+3.28%)</td><td>0.09 (+8.02%)</td><td>0.08 (+3.38%)</td><td>0.03 (-8.84%)</td><td>27406.71 (-3.28%)</td><td>21153.91 (-4.07%)</td><td>22243.66 (-7.45%)</td><td>15227.60 (+3.12%)</td><td>4937.71 (-9.41%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28335.16 (n/a)</td><td>22050.70 (n/a)</td><td>24034.92 (n/a)</td><td>14767.00 (n/a)</td><td>5450.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_weight_layout_reaches_both_gemms[b_col_maj_False]

_No metrics available._


### test_weight_layout_reaches_both_gemms[b_col_maj_True]

_No metrics available._


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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.16 (+5.57%)</td><td>2.07 (+19.54%)</td><td>1.82 (-2.41%)</td><td>1.46 <b>(+392.56%)</b></td><td>0.69 <b>(-33.88%)</b></td><td>720.50 <b>(-79.70%)</b></td><td>547.82 <b>(-52.93%)</b></td><td>577.70 (+2.47%)</td><td>331.90 (-5.28%)</td><td>157.50 <b>(-88.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.99 (n/a)</td><td>1.73 (n/a)</td><td>1.86 (n/a)</td><td>0.30 (n/a)</td><td>1.05 (n/a)</td><td>3548.80 (n/a)</td><td>1163.82 (n/a)</td><td>563.80 (n/a)</td><td>350.40 (n/a)</td><td>1350.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.18 (-3.80%)</td><td>2.21 <b>(+48.24%)</b></td><td>2.53 <b>(+121.20%)</b></td><td>1.10 <b>(+259.10%)</b></td><td>0.90 <b>(-22.67%)</b></td><td>951.40 <b>(-72.15%)</b></td><td>559.64 <b>(-56.89%)</b></td><td>413.80 <b>(-54.80%)</b></td><td>330.10 (+3.97%)</td><td>270.37 <b>(-78.20%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.30 (n/a)</td><td>1.49 (n/a)</td><td>1.15 (n/a)</td><td>0.31 (n/a)</td><td>1.16 (n/a)</td><td>3416.60 (n/a)</td><td>1298.14 (n/a)</td><td>915.40 (n/a)</td><td>317.50 (n/a)</td><td>1240.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.37 (-13.15%)</td><td>2.65 <b>(+46.46%)</b></td><td>2.59 <b>(+64.21%)</b></td><td>1.59 <b>(+430.18%)</b></td><td>0.69 <b>(-48.83%)</b></td><td>657.60 <b>(-81.14%)</b></td><td>423.98 <b>(-63.63%)</b></td><td>404.20 <b>(-39.10%)</b></td><td>310.80 (+15.15%)</td><td>137.62 <b>(-89.56%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.88 (n/a)</td><td>1.81 (n/a)</td><td>1.58 (n/a)</td><td>0.30 (n/a)</td><td>1.34 (n/a)</td><td>3486.70 (n/a)</td><td>1165.64 (n/a)</td><td>663.70 (n/a)</td><td>269.90 (n/a)</td><td>1318.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.43 <b>(+35.36%)</b></td><td>2.02 (+6.13%)</td><td>1.99 (+13.08%)</td><td>0.98 <b>(-33.83%)</b></td><td>0.90 <b>(+114.14%)</b></td><td>1074.20 <b>(+51.13%)</b></td><td>609.68 (+6.94%)</td><td>527.40 (-11.57%)</td><td>305.40 <b>(-26.12%)</b></td><td>285.55 <b>(+146.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.54 (n/a)</td><td>1.91 (n/a)</td><td>1.76 (n/a)</td><td>1.48 (n/a)</td><td>0.42 (n/a)</td><td>710.80 (n/a)</td><td>570.12 (n/a)</td><td>596.40 (n/a)</td><td>413.40 (n/a)</td><td>116.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.25 <b>(+32.57%)</b></td><td>2.03 (-10.75%)</td><td>1.53 <b>(-38.61%)</b></td><td>0.58 (-3.72%)</td><td>1.63 <b>(+60.23%)</b></td><td>3619.90 (+3.86%)</td><td>1937.66 <b>(+44.92%)</b></td><td>1366.50 <b>(+62.89%)</b></td><td>493.50 <b>(-24.56%)</b></td><td>1538.00 <b>(+27.36%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.21 (n/a)</td><td>2.27 (n/a)</td><td>2.50 (n/a)</td><td>0.60 (n/a)</td><td>1.02 (n/a)</td><td>3485.40 (n/a)</td><td>1337.08 (n/a)</td><td>838.90 (n/a)</td><td>654.20 (n/a)</td><td>1207.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.46 <b>(+38.67%)</b></td><td>3.56 <b>(+60.78%)</b></td><td>3.54 <b>(+47.52%)</b></td><td>2.57 <b>(+329.00%)</b></td><td>0.71 <b>(-26.92%)</b></td><td>816.50 <b>(-76.69%)</b></td><td>609.14 <b>(-54.90%)</b></td><td>591.90 <b>(-32.21%)</b></td><td>470.40 <b>(-27.89%)</b></td><td>131.51 <b>(-89.10%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.21 (n/a)</td><td>2.22 (n/a)</td><td>2.40 (n/a)</td><td>0.60 (n/a)</td><td>0.97 (n/a)</td><td>3502.80 (n/a)</td><td>1350.78 (n/a)</td><td>873.20 (n/a)</td><td>652.30 (n/a)</td><td>1206.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.08 (-2.65%)</td><td>1.85 <b>(-24.44%)</b></td><td>1.14 <b>(-61.63%)</b></td><td>0.59 (-1.85%)</td><td>1.53 (-2.82%)</td><td>3570.20 (+1.89%)</td><td>1984.44 <b>(+33.24%)</b></td><td>1833.60 <b>(+160.60%)</b></td><td>514.10 (+2.74%)</td><td>1397.34 (+6.76%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.19 (n/a)</td><td>2.44 (n/a)</td><td>2.98 (n/a)</td><td>0.60 (n/a)</td><td>1.58 (n/a)</td><td>3504.10 (n/a)</td><td>1489.32 (n/a)</td><td>703.60 (n/a)</td><td>500.40 (n/a)</td><td>1308.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.81 <b>(-26.74%)</b></td><td>2.65 <b>(-25.12%)</b></td><td>2.71 <b>(-28.78%)</b></td><td>1.00 <b>(+72.95%)</b></td><td>1.43 <b>(-50.74%)</b></td><td>2090.80 <b>(-42.18%)</b></td><td>1035.06 <b>(-38.41%)</b></td><td>773.10 <b>(+40.41%)</b></td><td>436.20 <b>(+36.48%)</b></td><td>644.80 <b>(-63.19%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.56 (n/a)</td><td>3.55 (n/a)</td><td>3.81 (n/a)</td><td>0.58 (n/a)</td><td>2.90 (n/a)</td><td>3616.10 (n/a)</td><td>1680.54 (n/a)</td><td>550.60 (n/a)</td><td>319.60 (n/a)</td><td>1751.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.97 <b>(+36.86%)</b></td><td>4.27 <b>(+88.31%)</b></td><td>3.86 <b>(+78.68%)</b></td><td>3.34 <b>(+468.12%)</b></td><td>1.09 <b>(-28.99%)</b></td><td>627.70 <b>(-82.40%)</b></td><td>514.18 <b>(-66.27%)</b></td><td>543.00 <b>(-44.03%)</b></td><td>351.00 <b>(-26.94%)</b></td><td>114.88 <b>(-90.97%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.37 (n/a)</td><td>2.27 (n/a)</td><td>2.16 (n/a)</td><td>0.59 (n/a)</td><td>1.53 (n/a)</td><td>3566.00 (n/a)</td><td>1524.62 (n/a)</td><td>970.20 (n/a)</td><td>480.40 (n/a)</td><td>1272.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.42 <b>(-26.83%)</b></td><td>1.64 <b>(-64.49%)</b></td><td>0.60 <b>(-86.50%)</b></td><td>0.58 <b>(-82.06%)</b></td><td>2.12 <b>(+25.21%)</b></td><td>3596.30 <b>(+457.48%)</b></td><td>2623.30 <b>(+426.81%)</b></td><td>3470.60 <b>(+640.95%)</b></td><td>387.20 <b>(+36.67%)</b></td><td>1391.62 <b>(+820.21%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.40 (n/a)</td><td>4.61 (n/a)</td><td>4.48 (n/a)</td><td>3.25 (n/a)</td><td>1.69 (n/a)</td><td>645.10 (n/a)</td><td>497.96 (n/a)</td><td>468.40 (n/a)</td><td>283.30 (n/a)</td><td>151.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.48 <b>(-21.46%)</b></td><td>3.03 <b>(-24.03%)</b></td><td>3.55 (-19.12%)</td><td>1.19 (+1.41%)</td><td>1.51 (-14.07%)</td><td>3530.00 (-1.39%)</td><td>1825.20 <b>(+25.79%)</b></td><td>1183.10 <b>(+23.64%)</b></td><td>935.40 <b>(+27.32%)</b></td><td>1147.21 (-4.43%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.71 (n/a)</td><td>3.99 (n/a)</td><td>4.38 (n/a)</td><td>1.17 (n/a)</td><td>1.76 (n/a)</td><td>3579.80 (n/a)</td><td>1451.00 (n/a)</td><td>956.90 (n/a)</td><td>734.70 (n/a)</td><td>1200.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>8.01 (-19.91%)</td><td>5.71 (+2.95%)</td><td>5.79 <b>(+50.92%)</b></td><td>3.58 <b>(+121.57%)</b></td><td>2.04 <b>(-42.15%)</b></td><td>1172.50 <b>(-54.87%)</b></td><td>820.04 <b>(-28.06%)</b></td><td>723.90 <b>(-33.74%)</b></td><td>523.30 <b>(+24.83%)</b></td><td>305.95 <b>(-65.05%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>10.01 (n/a)</td><td>5.55 (n/a)</td><td>3.84 (n/a)</td><td>1.61 (n/a)</td><td>3.53 (n/a)</td><td>2597.80 (n/a)</td><td>1139.82 (n/a)</td><td>1092.50 (n/a)</td><td>419.20 (n/a)</td><td>875.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.87 (-8.69%)</td><td>5.72 (+4.50%)</td><td>5.81 (-3.61%)</td><td>3.52 <b>(+202.62%)</b></td><td>2.17 <b>(-25.64%)</b></td><td>1190.50 <b>(-66.96%)</b></td><td>833.66 <b>(-34.45%)</b></td><td>721.70 (+3.75%)</td><td>533.10 (+9.53%)</td><td>334.21 <b>(-74.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>8.62 (n/a)</td><td>5.47 (n/a)</td><td>6.03 (n/a)</td><td>1.16 (n/a)</td><td>2.92 (n/a)</td><td>3602.80 (n/a)</td><td>1271.80 (n/a)</td><td>695.60 (n/a)</td><td>486.70 (n/a)</td><td>1317.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>9.41 <b>(+38.49%)</b></td><td>6.00 <b>(+30.89%)</b></td><td>6.66 <b>(+70.43%)</b></td><td>3.50 <b>(+73.67%)</b></td><td>2.44 <b>(+21.18%)</b></td><td>1197.60 <b>(-42.42%)</b></td><td>803.38 <b>(-27.49%)</b></td><td>630.10 <b>(-41.32%)</b></td><td>445.50 <b>(-27.80%)</b></td><td>332.68 <b>(-43.74%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.80 (n/a)</td><td>4.59 (n/a)</td><td>3.91 (n/a)</td><td>2.02 (n/a)</td><td>2.01 (n/a)</td><td>2079.90 (n/a)</td><td>1107.98 (n/a)</td><td>1073.80 (n/a)</td><td>617.00 (n/a)</td><td>591.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>9.21 (+12.40%)</td><td>4.53 <b>(+38.81%)</b></td><td>4.01 <b>(+138.19%)</b></td><td>1.17 (+6.39%)</td><td>3.57 (+18.08%)</td><td>3586.30 (-6.01%)</td><td>1835.20 (-18.94%)</td><td>1045.80 <b>(-58.02%)</b></td><td>455.30 (-11.02%)</td><td>1571.51 (+7.34%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>8.20 (n/a)</td><td>3.26 (n/a)</td><td>1.68 (n/a)</td><td>1.10 (n/a)</td><td>3.02 (n/a)</td><td>3815.60 (n/a)</td><td>2264.02 (n/a)</td><td>2491.00 (n/a)</td><td>511.70 (n/a)</td><td>1464.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>6.92 (+1.87%)</td><td>5.93 (+8.63%)</td><td>6.28 (-4.41%)</td><td>4.18 <b>(+276.53%)</b></td><td>1.05 <b>(-56.98%)</b></td><td>1003.70 <b>(-73.44%)</b></td><td>729.24 <b>(-42.53%)</b></td><td>668.10 (+4.62%)</td><td>606.10 (-1.85%)</td><td>158.41 <b>(-88.71%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.79 (n/a)</td><td>5.46 (n/a)</td><td>6.57 (n/a)</td><td>1.11 (n/a)</td><td>2.45 (n/a)</td><td>3779.40 (n/a)</td><td>1268.98 (n/a)</td><td>638.60 (n/a)</td><td>617.50 (n/a)</td><td>1403.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.71 <b>(+33.19%)</b></td><td>1.08 (+7.09%)</td><td>1.16 <b>(+22.52%)</b></td><td>0.15 <b>(-76.54%)</b></td><td>0.58 <b>(+116.21%)</b></td><td>3420.40 <b>(+326.22%)</b></td><td>1017.26 <b>(+83.16%)</b></td><td>450.10 (-18.37%)</td><td>307.20 <b>(-24.91%)</b></td><td>1345.63 <b>(+735.52%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.28 (n/a)</td><td>1.00 (n/a)</td><td>0.95 (n/a)</td><td>0.65 (n/a)</td><td>0.27 (n/a)</td><td>802.50 (n/a)</td><td>555.38 (n/a)</td><td>551.40 (n/a)</td><td>409.10 (n/a)</td><td>161.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.20 (-9.75%)</td><td>1.07 <b>(-33.31%)</b></td><td>0.95 <b>(-45.21%)</b></td><td>0.31 (+1.19%)</td><td>0.82 (+0.03%)</td><td>3378.10 (-1.17%)</td><td>1782.28 <b>(+56.76%)</b></td><td>1104.50 <b>(+82.53%)</b></td><td>476.00 (+10.80%)</td><td>1431.42 (+11.79%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.44 (n/a)</td><td>1.60 (n/a)</td><td>1.73 (n/a)</td><td>0.31 (n/a)</td><td>0.82 (n/a)</td><td>3418.20 (n/a)</td><td>1136.92 (n/a)</td><td>605.10 (n/a)</td><td>429.60 (n/a)</td><td>1280.43 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.78 <b>(-25.22%)</b></td><td>1.57 <b>(-45.27%)</b></td><td>1.17 <b>(-60.21%)</b></td><td>0.60 <b>(-63.35%)</b></td><td>0.89 (+12.37%)</td><td>3471.00 <b>(+172.81%)</b></td><td>1772.58 <b>(+124.30%)</b></td><td>1785.70 <b>(+151.37%)</b></td><td>754.00 <b>(+33.71%)</b></td><td>1073.68 <b>(+280.45%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.72 (n/a)</td><td>2.87 (n/a)</td><td>2.95 (n/a)</td><td>1.65 (n/a)</td><td>0.79 (n/a)</td><td>1272.30 (n/a)</td><td>790.28 (n/a)</td><td>710.40 (n/a)</td><td>563.90 (n/a)</td><td>282.21 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.19 (-14.50%)</td><td>0.97 (+2.48%)</td><td>0.97 (+9.81%)</td><td>0.75 (+10.16%)</td><td>0.15 <b>(-42.05%)</b></td><td>695.00 (-9.22%)</td><td>552.38 (-5.63%)</td><td>538.60 (-8.94%)</td><td>442.20 (+16.95%)</td><td>91.47 <b>(-35.35%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.39 (n/a)</td><td>0.95 (n/a)</td><td>0.89 (n/a)</td><td>0.68 (n/a)</td><td>0.27 (n/a)</td><td>765.60 (n/a)</td><td>585.34 (n/a)</td><td>591.50 (n/a)</td><td>378.10 (n/a)</td><td>141.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (+11.01%)</td><td>0.09 (-15.26%)</td><td>0.07 <b>(-37.86%)</b></td><td>0.07 <b>(-25.59%)</b></td><td>0.03 <b>(+99.12%)</b></td><td>482.70 <b>(+34.38%)</b></td><td>385.32 <b>(+26.98%)</b></td><td>450.30 <b>(+60.94%)</b></td><td>231.30 (-9.93%)</td><td>119.54 <b>(+145.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>359.20 (n/a)</td><td>303.46 (n/a)</td><td>279.80 (n/a)</td><td>256.80 (n/a)</td><td>48.74 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (-2.75%)</td><td>0.08 <b>(-28.93%)</b></td><td>0.07 <b>(-42.37%)</b></td><td>0.05 (+4.64%)</td><td>0.04 (-4.81%)</td><td>666.90 (-4.43%)</td><td>470.28 <b>(+35.12%)</b></td><td>486.00 <b>(+73.51%)</b></td><td>227.40 (+2.85%)</td><td>157.47 <b>(-20.44%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>697.80 (n/a)</td><td>348.04 (n/a)</td><td>280.10 (n/a)</td><td>221.10 (n/a)</td><td>197.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.21 <b>(-25.38%)</b></td><td>0.15 (+11.78%)</td><td>0.13 <b>(+39.44%)</b></td><td>0.11 <b>(+236.66%)</b></td><td>0.04 <b>(-57.79%)</b></td><td>611.60 <b>(-70.30%)</b></td><td>463.58 <b>(-43.19%)</b></td><td>489.50 <b>(-28.28%)</b></td><td>311.00 <b>(+33.99%)</b></td><td>114.99 <b>(-84.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.10 (n/a)</td><td>2059.10 (n/a)</td><td>816.06 (n/a)</td><td>682.50 (n/a)</td><td>232.10 (n/a)</td><td>722.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (-11.20%)</td><td>0.17 (-5.93%)</td><td>0.16 (+7.97%)</td><td>0.13 (-1.90%)</td><td>0.04 <b>(-24.08%)</b></td><td>513.30 (+1.93%)</td><td>412.28 (+4.34%)</td><td>407.50 (-7.39%)</td><td>292.80 (+12.62%)</td><td>86.48 (-11.86%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>503.60 (n/a)</td><td>395.14 (n/a)</td><td>440.00 (n/a)</td><td>260.00 (n/a)</td><td>98.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.23 (-16.43%)</td><td>0.15 (-9.37%)</td><td>0.13 (+3.14%)</td><td>0.08 <b>(-24.52%)</b></td><td>0.07 (-4.82%)</td><td>789.20 <b>(+32.51%)</b></td><td>508.38 (+14.76%)</td><td>497.50 (-3.04%)</td><td>281.30 (+19.65%)</td><td>229.99 <b>(+38.70%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>595.60 (n/a)</td><td>442.98 (n/a)</td><td>513.10 (n/a)</td><td>235.10 (n/a)</td><td>165.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.41 <b>(-27.19%)</b></td><td>0.32 (-2.32%)</td><td>0.30 <b>(+24.24%)</b></td><td>0.22 (+0.48%)</td><td>0.07 <b>(-48.52%)</b></td><td>584.60 (-0.48%)</td><td>433.12 (-5.35%)</td><td>431.60 (-19.52%)</td><td>317.80 <b>(+37.34%)</b></td><td>105.37 <b>(-31.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.57 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>587.40 (n/a)</td><td>457.60 (n/a)</td><td>536.30 (n/a)</td><td>231.40 (n/a)</td><td>153.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.56 (-0.73%)</td><td>0.31 (-4.13%)</td><td>0.27 (+9.07%)</td><td>0.21 (-11.34%)</td><td>0.14 (+3.50%)</td><td>619.20 (+12.79%)</td><td>476.94 (+5.98%)</td><td>477.90 (-8.31%)</td><td>235.20 (+0.73%)</td><td>150.35 (+13.76%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.56 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>549.00 (n/a)</td><td>450.02 (n/a)</td><td>521.20 (n/a)</td><td>233.50 (n/a)</td><td>132.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.61 (-11.77%)</td><td>0.29 <b>(-24.44%)</b></td><td>0.26 (-5.08%)</td><td>0.11 <b>(-45.88%)</b></td><td>0.19 (-6.52%)</td><td>1244.30 <b>(+84.78%)</b></td><td>620.92 <b>(+47.70%)</b></td><td>497.00 (+5.34%)</td><td>216.00 (+13.33%)</td><td>383.77 <b>(+99.09%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.69 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>673.40 (n/a)</td><td>420.38 (n/a)</td><td>471.80 (n/a)</td><td>190.60 (n/a)</td><td>192.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (-15.46%)</td><td>0.03 <b>(-40.70%)</b></td><td>0.03 <b>(-51.71%)</b></td><td>0.01 <b>(-59.16%)</b></td><td>0.01 (-3.47%)</td><td>1191.70 <b>(+144.85%)</b></td><td>646.18 <b>(+87.80%)</b></td><td>568.10 <b>(+107.11%)</b></td><td>298.90 (+18.28%)</td><td>328.81 <b>(+185.86%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>486.70 (n/a)</td><td>344.08 (n/a)</td><td>274.30 (n/a)</td><td>252.70 (n/a)</td><td>115.02 (n/a)</td>
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
