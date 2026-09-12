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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-12.42%)</td><td>0.02 (-1.19%)</td><td>0.01 (-4.41%)</td><td>0.01 (-12.25%)</td><td>0.01 (-1.63%)</td><td>541.70 (+13.97%)</td><td>397.98 (+3.07%)</td><td>426.00 (+4.62%)</td><td>259.50 (+14.17%)</td><td>124.87 <b>(+29.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>475.30 (n/a)</td><td>386.14 (n/a)</td><td>407.20 (n/a)</td><td>227.30 (n/a)</td><td>96.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+1.16%)</td><td>0.02 <b>(+21.96%)</b></td><td>0.02 <b>(+26.79%)</b></td><td>0.01 <b>(+305.77%)</b></td><td>0.00 <b>(-48.20%)</b></td><td>498.20 <b>(-75.35%)</b></td><td>348.10 <b>(-49.56%)</b></td><td>326.70 <b>(-21.13%)</b></td><td>268.40 (-1.14%)</td><td>91.42 <b>(-87.80%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2021.50 (n/a)</td><td>690.10 (n/a)</td><td>414.20 (n/a)</td><td>271.50 (n/a)</td><td>749.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(+106.72%)</b></td><td>0.02 <b>(+69.10%)</b></td><td>0.02 <b>(+79.87%)</b></td><td>0.01 <b>(+22.86%)</b></td><td>0.01 <b>(+270.87%)</b></td><td>496.50 (-18.61%)</td><td>338.68 <b>(-33.58%)</b></td><td>270.20 <b>(-44.41%)</b></td><td>191.50 <b>(-51.63%)</b></td><td>143.15 <b>(+54.88%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.00 (n/a)</td><td>509.94 (n/a)</td><td>486.10 (n/a)</td><td>395.90 (n/a)</td><td>92.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(+73.59%)</b></td><td>0.02 <b>(+47.55%)</b></td><td>0.02 <b>(+55.38%)</b></td><td>0.01 <b>(+70.13%)</b></td><td>0.01 <b>(+93.95%)</b></td><td>627.60 <b>(-41.21%)</b></td><td>400.44 <b>(-30.05%)</b></td><td>285.20 <b>(-35.65%)</b></td><td>245.00 <b>(-42.38%)</b></td><td>182.93 <b>(-34.24%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1067.60 (n/a)</td><td>572.48 (n/a)</td><td>443.20 (n/a)</td><td>425.20 (n/a)</td><td>278.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-11.06%)</td><td>0.02 (-8.90%)</td><td>0.01 (-5.28%)</td><td>0.01 (-6.05%)</td><td>0.01 <b>(-22.12%)</b></td><td>646.90 (+6.43%)</td><td>440.70 (+3.99%)</td><td>493.40 (+5.56%)</td><td>239.50 (+12.44%)</td><td>168.32 (-9.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.80 (n/a)</td><td>423.80 (n/a)</td><td>467.40 (n/a)</td><td>213.00 (n/a)</td><td>186.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-8.78%)</td><td>0.02 (+9.73%)</td><td>0.02 <b>(+60.14%)</b></td><td>0.01 <b>(+28.96%)</b></td><td>0.01 <b>(-22.05%)</b></td><td>532.00 <b>(-22.46%)</b></td><td>349.14 (-16.44%)</td><td>295.90 <b>(-37.55%)</b></td><td>219.70 (+9.63%)</td><td>139.61 <b>(-29.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>686.10 (n/a)</td><td>417.84 (n/a)</td><td>473.80 (n/a)</td><td>200.40 (n/a)</td><td>199.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-1.31%)</td><td>0.03 <b>(-21.39%)</b></td><td>0.03 <b>(-40.24%)</b></td><td>0.02 (+11.18%)</td><td>0.02 (-16.29%)</td><td>558.90 (-10.06%)</td><td>442.48 (+16.98%)</td><td>483.30 <b>(+67.35%)</b></td><td>204.90 (+1.34%)</td><td>137.05 <b>(-30.88%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>621.40 (n/a)</td><td>378.24 (n/a)</td><td>288.80 (n/a)</td><td>202.20 (n/a)</td><td>198.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-3.78%)</td><td>0.04 <b>(+33.01%)</b></td><td>0.04 <b>(+100.84%)</b></td><td>0.02 <b>(+281.26%)</b></td><td>0.01 <b>(-36.13%)</b></td><td>497.70 <b>(-73.77%)</b></td><td>352.98 <b>(-51.58%)</b></td><td>303.10 <b>(-50.21%)</b></td><td>222.80 (+3.92%)</td><td>120.29 <b>(-82.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1897.40 (n/a)</td><td>729.02 (n/a)</td><td>608.70 (n/a)</td><td>214.40 (n/a)</td><td>676.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-11.09%)</td><td>0.04 (-7.04%)</td><td>0.04 (+1.99%)</td><td>0.02 (-11.64%)</td><td>0.01 (-15.31%)</td><td>525.70 (+13.18%)</td><td>333.68 (+6.70%)</td><td>308.40 (-1.97%)</td><td>197.80 (+12.45%)</td><td>123.72 (+10.55%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>464.50 (n/a)</td><td>312.72 (n/a)</td><td>314.60 (n/a)</td><td>175.90 (n/a)</td><td>111.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (-13.67%)</td><td>0.03 (-13.14%)</td><td>0.02 <b>(-22.68%)</b></td><td>0.02 (+3.83%)</td><td>0.01 <b>(-22.47%)</b></td><td>502.30 (-3.68%)</td><td>416.88 (+12.24%)</td><td>494.40 <b>(+29.36%)</b></td><td>269.80 (+15.84%)</td><td>112.17 (-8.33%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.50 (n/a)</td><td>371.42 (n/a)</td><td>382.20 (n/a)</td><td>232.90 (n/a)</td><td>122.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (+16.41%)</td><td>0.03 (+12.30%)</td><td>0.03 (+2.74%)</td><td>0.02 (+0.85%)</td><td>0.02 <b>(+37.47%)</b></td><td>555.00 (-0.84%)</td><td>407.00 (-5.71%)</td><td>436.90 (-2.67%)</td><td>210.70 (-14.07%)</td><td>157.70 <b>(+22.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.70 (n/a)</td><td>431.66 (n/a)</td><td>448.90 (n/a)</td><td>245.20 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(-40.80%)</b></td><td>0.02 <b>(-39.65%)</b></td><td>0.03 <b>(-28.42%)</b></td><td>0.01 <b>(-69.42%)</b></td><td>0.01 <b>(-33.91%)</b></td><td>1927.80 <b>(+227.08%)</b></td><td>760.62 <b>(+102.91%)</b></td><td>488.80 <b>(+39.70%)</b></td><td>369.00 <b>(+68.96%)</b></td><td>657.20 <b>(+316.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>589.40 (n/a)</td><td>374.86 (n/a)</td><td>349.90 (n/a)</td><td>218.40 (n/a)</td><td>157.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 <b>(-28.68%)</b></td><td>0.06 <b>(-32.58%)</b></td><td>0.05 <b>(-40.53%)</b></td><td>0.04 <b>(-31.02%)</b></td><td>0.02 (-1.48%)</td><td>651.80 <b>(+44.97%)</b></td><td>469.02 <b>(+56.49%)</b></td><td>450.60 <b>(+68.13%)</b></td><td>297.50 <b>(+40.20%)</b></td><td>173.33 <b>(+91.86%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>449.60 (n/a)</td><td>299.72 (n/a)</td><td>268.00 (n/a)</td><td>212.20 (n/a)</td><td>90.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (+12.33%)</td><td>0.08 <b>(+24.92%)</b></td><td>0.08 (+14.95%)</td><td>0.05 <b>(+42.11%)</b></td><td>0.02 <b>(-25.87%)</b></td><td>470.80 <b>(-29.64%)</b></td><td>312.64 <b>(-27.25%)</b></td><td>295.80 (-13.00%)</td><td>231.60 (-10.96%)</td><td>92.48 <b>(-51.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>669.10 (n/a)</td><td>429.74 (n/a)</td><td>340.00 (n/a)</td><td>260.10 (n/a)</td><td>191.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (-5.96%)</td><td>0.07 (+2.35%)</td><td>0.05 (-3.15%)</td><td>0.05 <b>(+25.74%)</b></td><td>0.03 (-13.76%)</td><td>526.00 <b>(-20.47%)</b></td><td>403.96 (-7.91%)</td><td>499.50 (+3.25%)</td><td>227.90 (+6.35%)</td><td>147.38 <b>(-24.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>661.40 (n/a)</td><td>438.66 (n/a)</td><td>483.80 (n/a)</td><td>214.30 (n/a)</td><td>193.93 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 <b>(-35.63%)</b></td><td>0.06 <b>(-21.51%)</b></td><td>0.05 (-5.06%)</td><td>0.05 (-8.53%)</td><td>0.02 <b>(-45.10%)</b></td><td>545.40 (+9.32%)</td><td>419.98 (+17.38%)</td><td>453.70 (+5.32%)</td><td>279.40 <b>(+55.39%)</b></td><td>132.22 (-9.58%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>498.90 (n/a)</td><td>357.80 (n/a)</td><td>430.80 (n/a)</td><td>179.80 (n/a)</td><td>146.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 <b>(+74.78%)</b></td><td>0.09 <b>(+70.64%)</b></td><td>0.09 <b>(+96.13%)</b></td><td>0.04 (+1.54%)</td><td>0.03 <b>(+199.38%)</b></td><td>570.90 (-1.52%)</td><td>319.22 <b>(-35.79%)</b></td><td>264.30 <b>(-49.01%)</b></td><td>215.10 <b>(-42.79%)</b></td><td>143.03 <b>(+90.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>579.70 (n/a)</td><td>497.14 (n/a)</td><td>518.30 (n/a)</td><td>376.00 (n/a)</td><td>75.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (-5.84%)</td><td>0.06 (-2.61%)</td><td>0.05 (-3.25%)</td><td>0.03 <b>(-30.13%)</b></td><td>0.03 (+16.90%)</td><td>859.80 <b>(+43.13%)</b></td><td>508.48 (+14.20%)</td><td>449.40 (+3.38%)</td><td>250.30 (+6.19%)</td><td>257.04 <b>(+83.78%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>600.70 (n/a)</td><td>445.24 (n/a)</td><td>434.70 (n/a)</td><td>235.70 (n/a)</td><td>139.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.21 (+7.05%)</td><td>0.12 <b>(-20.93%)</b></td><td>0.10 <b>(-39.56%)</b></td><td>0.08 <b>(-21.61%)</b></td><td>0.05 (+18.09%)</td><td>608.00 <b>(+27.57%)</b></td><td>449.22 <b>(+31.50%)</b></td><td>492.00 <b>(+65.43%)</b></td><td>229.90 (-6.58%)</td><td>144.61 <b>(+34.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>476.60 (n/a)</td><td>341.60 (n/a)</td><td>297.40 (n/a)</td><td>246.10 (n/a)</td><td>107.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (+17.83%)</td><td>0.16 <b>(+34.09%)</b></td><td>0.17 <b>(+56.75%)</b></td><td>0.11 <b>(+20.34%)</b></td><td>0.03 (+10.11%)</td><td>465.60 (-16.90%)</td><td>313.64 <b>(-25.71%)</b></td><td>284.60 <b>(-36.20%)</b></td><td>249.30 (-15.15%)</td><td>86.73 (-16.89%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>560.30 (n/a)</td><td>422.20 (n/a)</td><td>446.10 (n/a)</td><td>293.80 (n/a)</td><td>104.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.23 <b>(-25.08%)</b></td><td>0.17 (+15.88%)</td><td>0.17 <b>(+98.69%)</b></td><td>0.11 <b>(+121.41%)</b></td><td>0.05 <b>(-58.17%)</b></td><td>457.30 <b>(-54.83%)</b></td><td>306.62 <b>(-40.24%)</b></td><td>288.90 <b>(-49.68%)</b></td><td>214.60 <b>(+33.46%)</b></td><td>93.01 <b>(-72.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.11 (n/a)</td><td>1012.50 (n/a)</td><td>513.10 (n/a)</td><td>574.10 (n/a)</td><td>160.80 (n/a)</td><td>340.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 <b>(-30.09%)</b></td><td>0.10 <b>(-34.51%)</b></td><td>0.09 <b>(-25.50%)</b></td><td>0.02 <b>(-73.72%)</b></td><td>0.05 (-17.38%)</td><td>2075.70 <b>(+280.58%)</b></td><td>784.58 <b>(+104.31%)</b></td><td>558.40 <b>(+34.23%)</b></td><td>307.70 <b>(+43.05%)</b></td><td>729.47 <b>(+414.08%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>545.40 (n/a)</td><td>384.02 (n/a)</td><td>416.00 (n/a)</td><td>215.10 (n/a)</td><td>141.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (-15.93%)</td><td>0.14 (+14.99%)</td><td>0.12 <b>(+27.59%)</b></td><td>0.08 (+0.79%)</td><td>0.06 (-13.47%)</td><td>600.50 (-0.78%)</td><td>407.88 (-14.52%)</td><td>410.10 <b>(-21.62%)</b></td><td>243.30 (+18.97%)</td><td>164.11 (+2.08%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>605.20 (n/a)</td><td>477.18 (n/a)</td><td>523.20 (n/a)</td><td>204.50 (n/a)</td><td>160.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (-3.67%)</td><td>0.14 (+5.80%)</td><td>0.13 (+15.25%)</td><td>0.11 <b>(+37.24%)</b></td><td>0.04 <b>(-35.17%)</b></td><td>431.10 <b>(-27.13%)</b></td><td>356.84 (-13.21%)</td><td>382.40 (-13.23%)</td><td>251.20 (+3.84%)</td><td>82.53 <b>(-47.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>591.60 (n/a)</td><td>411.16 (n/a)</td><td>440.70 (n/a)</td><td>241.90 (n/a)</td><td>157.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 <b>(-21.52%)</b></td><td>0.01 (-6.45%)</td><td>0.01 (-11.19%)</td><td>0.01 <b>(+28.03%)</b></td><td>0.00 <b>(-50.18%)</b></td><td>402.90 <b>(-21.90%)</b></td><td>294.72 (-1.50%)</td><td>276.10 (+12.60%)</td><td>243.80 <b>(+27.44%)</b></td><td>62.05 <b>(-51.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.90 (n/a)</td><td>299.22 (n/a)</td><td>245.20 (n/a)</td><td>191.30 (n/a)</td><td>126.95 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-1.20%)</td><td>0.01 (-10.73%)</td><td>0.01 <b>(-41.68%)</b></td><td>0.00 <b>(+325.59%)</b></td><td>0.00 <b>(-22.69%)</b></td><td>581.30 <b>(-76.50%)</b></td><td>419.16 <b>(-41.00%)</b></td><td>498.60 <b>(+71.46%)</b></td><td>240.40 (+1.22%)</td><td>158.81 <b>(-83.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2473.80 (n/a)</td><td>710.50 (n/a)</td><td>290.80 (n/a)</td><td>237.50 (n/a)</td><td>986.01 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-0.61%)</td><td>0.01 (+0.13%)</td><td>0.01 (-19.43%)</td><td>0.01 <b>(+49.05%)</b></td><td>0.00 <b>(-42.84%)</b></td><td>368.30 <b>(-32.91%)</b></td><td>317.40 (-8.05%)</td><td>334.40 <b>(+24.13%)</b></td><td>241.10 (+0.63%)</td><td>54.92 <b>(-59.75%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>549.00 (n/a)</td><td>345.18 (n/a)</td><td>269.40 (n/a)</td><td>239.60 (n/a)</td><td>136.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (+1.90%)</td><td>0.01 (-11.26%)</td><td>0.01 <b>(-33.96%)</b></td><td>0.01 (+12.08%)</td><td>0.00 (+18.86%)</td><td>492.70 (-10.78%)</td><td>384.90 (+14.36%)</td><td>441.60 <b>(+51.44%)</b></td><td>239.90 (-1.88%)</td><td>122.31 (-1.02%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>552.20 (n/a)</td><td>336.56 (n/a)</td><td>291.60 (n/a)</td><td>244.50 (n/a)</td><td>123.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 <b>(+20.59%)</b></td><td>0.01 (+14.69%)</td><td>0.01 <b>(+40.71%)</b></td><td>0.00 <b>(+20.28%)</b></td><td>0.00 (+16.58%)</td><td>680.10 (-16.86%)</td><td>395.70 (-11.38%)</td><td>275.10 <b>(-28.95%)</b></td><td>199.70 (-17.07%)</td><td>218.10 (-9.73%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>818.00 (n/a)</td><td>446.50 (n/a)</td><td>387.20 (n/a)</td><td>240.80 (n/a)</td><td>241.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (+17.66%)</td><td>0.01 (+10.19%)</td><td>0.01 (+16.75%)</td><td>0.00 (-10.11%)</td><td>0.00 <b>(+65.79%)</b></td><td>530.90 (+11.23%)</td><td>360.20 (-4.53%)</td><td>292.70 (-14.37%)</td><td>260.40 (-15.01%)</td><td>123.26 <b>(+53.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.30 (n/a)</td><td>377.28 (n/a)</td><td>341.80 (n/a)</td><td>306.40 (n/a)</td><td>80.16 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+2.05%)</td><td>0.02 (-15.49%)</td><td>0.02 (-2.37%)</td><td>0.01 <b>(-45.30%)</b></td><td>0.01 <b>(+275.04%)</b></td><td>515.10 <b>(+82.85%)</b></td><td>343.88 <b>(+32.03%)</b></td><td>268.10 (+2.41%)</td><td>230.50 (-2.00%)</td><td>134.89 <b>(+571.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>281.70 (n/a)</td><td>260.46 (n/a)</td><td>261.80 (n/a)</td><td>235.20 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-1.00%)</td><td>0.02 (-14.71%)</td><td>0.02 (+1.97%)</td><td>0.01 <b>(-44.80%)</b></td><td>0.01 <b>(+66.38%)</b></td><td>750.80 <b>(+81.18%)</b></td><td>388.96 <b>(+44.20%)</b></td><td>235.30 (-1.96%)</td><td>198.40 (+0.97%)</td><td>242.86 <b>(+186.27%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>414.40 (n/a)</td><td>269.74 (n/a)</td><td>240.00 (n/a)</td><td>196.50 (n/a)</td><td>84.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-14.36%)</td><td>0.02 (-7.19%)</td><td>0.02 (-17.38%)</td><td>0.01 <b>(+30.02%)</b></td><td>0.01 <b>(-32.86%)</b></td><td>488.00 <b>(-23.09%)</b></td><td>338.34 (-3.25%)</td><td>284.40 <b>(+21.02%)</b></td><td>239.70 (+16.76%)</td><td>113.86 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.50 (n/a)</td><td>349.72 (n/a)</td><td>235.00 (n/a)</td><td>205.30 (n/a)</td><td>186.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-11.07%)</td><td>0.02 (+0.46%)</td><td>0.02 <b>(+38.18%)</b></td><td>0.01 (+6.22%)</td><td>0.00 <b>(-28.22%)</b></td><td>569.90 (-5.86%)</td><td>365.16 (-5.36%)</td><td>304.30 <b>(-27.62%)</b></td><td>258.20 (+12.46%)</td><td>126.55 (-17.69%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.40 (n/a)</td><td>385.86 (n/a)</td><td>420.40 (n/a)</td><td>229.60 (n/a)</td><td>153.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(+48.32%)</b></td><td>0.01 (-16.91%)</td><td>0.01 <b>(-33.56%)</b></td><td>0.00 <b>(-57.98%)</b></td><td>0.01 <b>(+154.34%)</b></td><td>1125.10 <b>(+137.97%)</b></td><td>608.04 <b>(+61.75%)</b></td><td>596.50 <b>(+50.52%)</b></td><td>180.90 <b>(-32.58%)</b></td><td>337.61 <b>(+271.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.80 (n/a)</td><td>375.92 (n/a)</td><td>396.30 (n/a)</td><td>268.30 (n/a)</td><td>90.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-3.02%)</td><td>0.01 (-8.90%)</td><td>0.01 (-18.43%)</td><td>0.01 (+12.21%)</td><td>0.00 (+1.95%)</td><td>545.90 (-10.89%)</td><td>405.48 (+9.42%)</td><td>373.90 <b>(+22.59%)</b></td><td>274.00 (+3.12%)</td><td>132.34 (-6.52%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.60 (n/a)</td><td>370.56 (n/a)</td><td>305.00 (n/a)</td><td>265.70 (n/a)</td><td>141.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-4.65%)</td><td>0.04 (+13.27%)</td><td>0.04 (+5.04%)</td><td>0.03 <b>(+62.66%)</b></td><td>0.00 <b>(-68.73%)</b></td><td>320.10 <b>(-38.53%)</b></td><td>291.78 (-17.15%)</td><td>294.40 (-4.79%)</td><td>260.30 (+4.88%)</td><td>21.36 <b>(-80.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.70 (n/a)</td><td>352.16 (n/a)</td><td>309.20 (n/a)</td><td>248.20 (n/a)</td><td>108.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (+8.04%)</td><td>0.03 (-16.61%)</td><td>0.03 <b>(-31.21%)</b></td><td>0.00 <b>(-68.74%)</b></td><td>0.02 <b>(+29.43%)</b></td><td>2435.20 <b>(+219.87%)</b></td><td>790.52 <b>(+96.10%)</b></td><td>407.50 <b>(+45.33%)</b></td><td>226.70 (-7.47%)</td><td>930.41 <b>(+323.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>761.30 (n/a)</td><td>403.12 (n/a)</td><td>280.40 (n/a)</td><td>245.00 (n/a)</td><td>219.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (+0.31%)</td><td>0.03 (-19.35%)</td><td>0.03 <b>(-35.00%)</b></td><td>0.02 (-6.98%)</td><td>0.01 <b>(+20.28%)</b></td><td>545.70 (+7.48%)</td><td>382.88 <b>(+28.53%)</b></td><td>385.20 <b>(+53.83%)</b></td><td>231.10 (-0.30%)</td><td>143.14 <b>(+21.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.70 (n/a)</td><td>297.88 (n/a)</td><td>250.40 (n/a)</td><td>231.80 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(+24.31%)</b></td><td>0.03 (-6.12%)</td><td>0.02 <b>(-23.59%)</b></td><td>0.02 (-14.44%)</td><td>0.01 <b>(+57.65%)</b></td><td>602.10 (+16.87%)</td><td>467.36 (+14.85%)</td><td>571.20 <b>(+30.89%)</b></td><td>239.70 (-19.56%)</td><td>162.69 <b>(+59.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>406.92 (n/a)</td><td>436.40 (n/a)</td><td>298.00 (n/a)</td><td>102.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (+13.33%)</td><td>0.03 (-5.42%)</td><td>0.04 (-8.17%)</td><td>0.02 (+6.75%)</td><td>0.01 <b>(+27.70%)</b></td><td>568.10 (-6.33%)</td><td>371.70 (+9.01%)</td><td>297.30 (+8.90%)</td><td>231.70 (-11.77%)</td><td>155.31 (+4.33%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.50 (n/a)</td><td>340.98 (n/a)</td><td>273.00 (n/a)</td><td>262.60 (n/a)</td><td>148.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (+4.44%)</td><td>0.03 (+10.70%)</td><td>0.04 (+16.03%)</td><td>0.02 (-6.32%)</td><td>0.01 (+8.29%)</td><td>502.40 (+6.73%)</td><td>340.40 (-9.04%)</td><td>291.90 (-13.82%)</td><td>280.50 (-4.23%)</td><td>93.73 (+8.81%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.70 (n/a)</td><td>374.22 (n/a)</td><td>338.70 (n/a)</td><td>292.90 (n/a)</td><td>86.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (+7.67%)</td><td>0.07 <b>(+26.64%)</b></td><td>0.07 <b>(+33.18%)</b></td><td>0.06 <b>(+81.18%)</b></td><td>0.01 <b>(-45.20%)</b></td><td>368.80 <b>(-44.80%)</b></td><td>298.98 <b>(-31.37%)</b></td><td>301.70 <b>(-24.91%)</b></td><td>232.30 (-7.15%)</td><td>56.64 <b>(-70.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>668.10 (n/a)</td><td>435.62 (n/a)</td><td>401.80 (n/a)</td><td>250.20 (n/a)</td><td>195.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (+1.85%)</td><td>0.06 (-9.45%)</td><td>0.08 (+9.61%)</td><td>0.03 <b>(-39.83%)</b></td><td>0.02 <b>(+100.70%)</b></td><td>642.60 <b>(+66.18%)</b></td><td>376.92 <b>(+25.31%)</b></td><td>273.30 (-8.78%)</td><td>243.30 (-1.82%)</td><td>177.18 <b>(+217.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>386.70 (n/a)</td><td>300.80 (n/a)</td><td>299.60 (n/a)</td><td>247.80 (n/a)</td><td>55.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (+4.29%)</td><td>0.07 (+1.84%)</td><td>0.07 (-13.61%)</td><td>0.04 <b>(+267.08%)</b></td><td>0.02 <b>(-35.11%)</b></td><td>548.10 <b>(-72.76%)</b></td><td>356.20 <b>(-43.66%)</b></td><td>290.30 (+15.75%)</td><td>222.60 (-4.13%)</td><td>132.26 <b>(-82.94%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2011.90 (n/a)</td><td>632.22 (n/a)</td><td>250.80 (n/a)</td><td>232.20 (n/a)</td><td>775.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (+4.06%)</td><td>0.06 (-14.29%)</td><td>0.04 <b>(-44.51%)</b></td><td>0.03 (-4.27%)</td><td>0.03 (+3.00%)</td><td>639.20 (+4.46%)</td><td>445.06 (+17.73%)</td><td>484.00 <b>(+80.19%)</b></td><td>232.00 (-3.89%)</td><td>179.50 (+4.86%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.90 (n/a)</td><td>378.02 (n/a)</td><td>268.60 (n/a)</td><td>241.40 (n/a)</td><td>171.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-15.38%)</td><td>0.04 <b>(-38.54%)</b></td><td>0.04 <b>(-50.51%)</b></td><td>0.02 <b>(-54.12%)</b></td><td>0.02 (-3.28%)</td><td>1009.30 <b>(+117.94%)</b></td><td>555.90 <b>(+78.64%)</b></td><td>491.50 <b>(+102.10%)</b></td><td>283.90 (+18.14%)</td><td>272.82 <b>(+170.35%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>463.10 (n/a)</td><td>311.18 (n/a)</td><td>243.20 (n/a)</td><td>240.30 (n/a)</td><td>100.92 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-37.59%)</b></td><td>0.04 <b>(-35.54%)</b></td><td>0.04 <b>(-35.54%)</b></td><td>0.02 <b>(-54.96%)</b></td><td>0.01 <b>(-35.67%)</b></td><td>1319.20 <b>(+122.01%)</b></td><td>671.22 <b>(+62.67%)</b></td><td>497.50 <b>(+55.13%)</b></td><td>444.10 <b>(+60.21%)</b></td><td>367.79 <b>(+132.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.20 (n/a)</td><td>412.62 (n/a)</td><td>320.70 (n/a)</td><td>277.20 (n/a)</td><td>158.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>536.10 (n/a)</td><td>306.68 (n/a)</td><td>268.60 (n/a)</td><td>223.30 (n/a)</td><td>130.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.70 (n/a)</td><td>446.20 (n/a)</td><td>425.40 (n/a)</td><td>317.40 (n/a)</td><td>127.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.00 (n/a)</td><td>407.28 (n/a)</td><td>332.90 (n/a)</td><td>299.80 (n/a)</td><td>126.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>393.82 (n/a)</td><td>452.20 (n/a)</td><td>228.20 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.80 (n/a)</td><td>365.02 (n/a)</td><td>410.50 (n/a)</td><td>223.80 (n/a)</td><td>130.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>461.50 (n/a)</td><td>301.60 (n/a)</td><td>272.10 (n/a)</td><td>238.00 (n/a)</td><td>90.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>431.20 (n/a)</td><td>304.50 (n/a)</td><td>252.40 (n/a)</td><td>240.20 (n/a)</td><td>85.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.70 (n/a)</td><td>329.06 (n/a)</td><td>284.00 (n/a)</td><td>244.60 (n/a)</td><td>112.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>589.70 (n/a)</td><td>337.88 (n/a)</td><td>280.30 (n/a)</td><td>213.30 (n/a)</td><td>151.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (+2.30%)</td><td>0.17 (+14.33%)</td><td>0.19 (+8.07%)</td><td>0.11 (+17.51%)</td><td>0.04 (-17.74%)</td><td>452.10 (-14.91%)</td><td>299.40 (-15.86%)</td><td>261.80 (-7.49%)</td><td>241.90 (-2.26%)</td><td>88.09 <b>(-30.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>531.30 (n/a)</td><td>355.84 (n/a)</td><td>283.00 (n/a)</td><td>247.50 (n/a)</td><td>126.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>553.40 (n/a)</td><td>385.22 (n/a)</td><td>347.90 (n/a)</td><td>260.00 (n/a)</td><td>109.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>566.80 (n/a)</td><td>375.74 (n/a)</td><td>275.10 (n/a)</td><td>246.80 (n/a)</td><td>155.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.50 (n/a)</td><td>366.40 (n/a)</td><td>365.80 (n/a)</td><td>284.60 (n/a)</td><td>83.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.60 (n/a)</td><td>442.96 (n/a)</td><td>500.90 (n/a)</td><td>233.00 (n/a)</td><td>142.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1908.50 (n/a)</td><td>731.32 (n/a)</td><td>512.00 (n/a)</td><td>214.00 (n/a)</td><td>670.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>303.16 (n/a)</td><td>242.10 (n/a)</td><td>219.00 (n/a)</td><td>142.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.40 (n/a)</td><td>354.16 (n/a)</td><td>274.60 (n/a)</td><td>257.90 (n/a)</td><td>130.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.70 (n/a)</td><td>372.90 (n/a)</td><td>423.30 (n/a)</td><td>247.90 (n/a)</td><td>117.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>796.60 (n/a)</td><td>438.24 (n/a)</td><td>446.50 (n/a)</td><td>153.60 (n/a)</td><td>245.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1888.90 (n/a)</td><td>645.86 (n/a)</td><td>289.10 (n/a)</td><td>200.40 (n/a)</td><td>711.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>480.20 (n/a)</td><td>307.26 (n/a)</td><td>283.20 (n/a)</td><td>235.90 (n/a)</td><td>99.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>461.00 (n/a)</td><td>407.36 (n/a)</td><td>415.50 (n/a)</td><td>327.70 (n/a)</td><td>57.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>473.10 (n/a)</td><td>297.20 (n/a)</td><td>295.30 (n/a)</td><td>164.40 (n/a)</td><td>113.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.38 (-2.91%)</td><td>3.16 (-7.46%)</td><td>2.83 <b>(-20.88%)</b></td><td>2.55 (+11.54%)</td><td>0.78 (-14.77%)</td><td>4111.90 (-10.35%)</td><td>3461.52 (+5.96%)</td><td>3701.60 <b>(+26.39%)</b></td><td>2394.40 (+3.00%)</td><td>749.60 <b>(-20.41%)</b></td><td>1793.79 (-2.91%)</td><td>1295.74 (-7.46%)</td><td>1160.31 <b>(-20.88%)</b></td><td>1044.52 (+11.54%)</td><td>320.33 (-14.77%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.51 (n/a)</td><td>3.42 (n/a)</td><td>3.58 (n/a)</td><td>2.29 (n/a)</td><td>0.92 (n/a)</td><td>4586.40 (n/a)</td><td>3266.84 (n/a)</td><td>2928.60 (n/a)</td><td>2324.60 (n/a)</td><td>941.79 (n/a)</td><td>1847.59 (n/a)</td><td>1400.14 (n/a)</td><td>1466.58 (n/a)</td><td>936.46 (n/a)</td><td>375.83 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.55 (+2.62%)</td><td>3.32 (+3.97%)</td><td>3.28 (+2.32%)</td><td>3.15 (+9.86%)</td><td>0.16 <b>(-38.59%)</b></td><td>7499.70 (-8.97%)</td><td>7121.84 (-4.17%)</td><td>7199.50 (-2.26%)</td><td>6654.70 (-2.56%)</td><td>341.02 <b>(-45.04%)</b></td><td>2016.89 (+2.62%)</td><td>1888.11 (+3.97%)</td><td>1864.26 (+2.32%)</td><td>1789.63 (+9.86%)</td><td>91.83 <b>(-38.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.45 (n/a)</td><td>3.19 (n/a)</td><td>3.20 (n/a)</td><td>2.86 (n/a)</td><td>0.26 (n/a)</td><td>8239.10 (n/a)</td><td>7431.54 (n/a)</td><td>7366.20 (n/a)</td><td>6829.40 (n/a)</td><td>620.50 (n/a)</td><td>1965.31 (n/a)</td><td>1816.03 (n/a)</td><td>1822.07 (n/a)</td><td>1629.04 (n/a)</td><td>149.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.85 (+5.00%)</td><td>3.53 (+6.71%)</td><td>3.54 (+5.57%)</td><td>3.21 (+13.33%)</td><td>0.28 (-8.93%)</td><td>5232.60 (-11.77%)</td><td>4771.98 (-6.50%)</td><td>4734.90 (-5.28%)</td><td>4355.30 (-4.76%)</td><td>377.78 <b>(-24.87%)</b></td><td>1972.28 (+5.00%)</td><td>1809.09 (+6.71%)</td><td>1814.18 (+5.57%)</td><td>1641.62 (+13.33%)</td><td>142.42 (-8.93%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.67 (n/a)</td><td>3.31 (n/a)</td><td>3.36 (n/a)</td><td>2.83 (n/a)</td><td>0.31 (n/a)</td><td>5930.30 (n/a)</td><td>5103.90 (n/a)</td><td>4998.70 (n/a)</td><td>4572.90 (n/a)</td><td>502.81 (n/a)</td><td>1878.43 (n/a)</td><td>1695.29 (n/a)</td><td>1718.43 (n/a)</td><td>1448.47 (n/a)</td><td>156.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.27 (-14.33%)</td><td>0.80 (-6.33%)</td><td>0.72 (-11.41%)</td><td>0.43 <b>(+206.73%)</b></td><td>0.32 <b>(-35.39%)</b></td><td>1075.60 <b>(-67.40%)</b></td><td>652.46 <b>(-37.22%)</b></td><td>636.40 (+12.88%)</td><td>361.20 (+16.74%)</td><td>269.02 <b>(-78.79%)</b></td><td>92.90 (-14.33%)</td><td>58.55 (-6.33%)</td><td>52.72 (-11.41%)</td><td>31.20 <b>(+206.73%)</b></td><td>23.13 <b>(-35.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.48 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.14 (n/a)</td><td>0.49 (n/a)</td><td>3299.20 (n/a)</td><td>1039.30 (n/a)</td><td>563.80 (n/a)</td><td>309.40 (n/a)</td><td>1268.37 (n/a)</td><td>108.44 (n/a)</td><td>62.51 (n/a)</td><td>59.51 (n/a)</td><td>10.17 (n/a)</td><td>35.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.15 <b>(-32.60%)</b></td><td>0.81 (-10.85%)</td><td>0.97 (+11.96%)</td><td>0.19 (+1.61%)</td><td>0.37 <b>(-31.31%)</b></td><td>3429.90 (-1.59%)</td><td>1246.54 (+1.48%)</td><td>675.70 (-10.68%)</td><td>569.70 <b>(+48.36%)</b></td><td>1226.17 (-3.75%)</td><td>117.80 <b>(-32.60%)</b></td><td>82.54 (-10.85%)</td><td>99.32 (+11.96%)</td><td>19.57 (+1.61%)</td><td>38.32 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.71 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.19 (n/a)</td><td>0.54 (n/a)</td><td>3485.20 (n/a)</td><td>1228.40 (n/a)</td><td>756.50 (n/a)</td><td>384.00 (n/a)</td><td>1273.90 (n/a)</td><td>174.78 (n/a)</td><td>92.59 (n/a)</td><td>88.72 (n/a)</td><td>19.26 (n/a)</td><td>55.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.21 (-19.59%)</td><td>0.99 (-11.77%)</td><td>1.02 (-7.19%)</td><td>0.74 (+7.67%)</td><td>0.19 <b>(-36.20%)</b></td><td>1017.90 (-7.13%)</td><td>784.20 (+9.33%)</td><td>742.20 (+7.75%)</td><td>623.60 <b>(+24.37%)</b></td><td>162.04 <b>(-28.93%)</b></td><td>134.53 (-19.59%)</td><td>110.49 (-11.77%)</td><td>113.03 (-7.19%)</td><td>82.41 (+7.67%)</td><td>21.46 <b>(-36.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.50 (n/a)</td><td>1.13 (n/a)</td><td>1.09 (n/a)</td><td>0.69 (n/a)</td><td>0.30 (n/a)</td><td>1096.00 (n/a)</td><td>717.28 (n/a)</td><td>688.80 (n/a)</td><td>501.40 (n/a)</td><td>227.99 (n/a)</td><td>167.30 (n/a)</td><td>125.23 (n/a)</td><td>121.79 (n/a)</td><td>76.54 (n/a)</td><td>33.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.93 (+4.26%)</td><td>1.36 (-9.12%)</td><td>1.21 (-18.05%)</td><td>0.88 <b>(-24.64%)</b></td><td>0.40 <b>(+24.90%)</b></td><td>1186.70 <b>(+32.71%)</b></td><td>827.82 (+13.69%)</td><td>867.40 <b>(+22.01%)</b></td><td>542.60 (-4.08%)</td><td>245.02 <b>(+55.65%)</b></td><td>247.35 (+4.26%)</td><td>173.97 (-9.12%)</td><td>154.73 (-18.05%)</td><td>113.10 <b>(-24.64%)</b></td><td>51.59 <b>(+24.90%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.85 (n/a)</td><td>1.50 (n/a)</td><td>1.48 (n/a)</td><td>1.17 (n/a)</td><td>0.32 (n/a)</td><td>894.20 (n/a)</td><td>728.16 (n/a)</td><td>710.90 (n/a)</td><td>565.70 (n/a)</td><td>157.41 (n/a)</td><td>237.24 (n/a)</td><td>191.43 (n/a)</td><td>188.80 (n/a)</td><td>150.09 (n/a)</td><td>41.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.49 <b>(+54.55%)</b></td><td>1.73 <b>(+47.06%)</b></td><td>1.49 <b>(+28.06%)</b></td><td>1.35 <b>(+69.10%)</b></td><td>0.49 <b>(+54.59%)</b></td><td>778.90 <b>(-40.86%)</b></td><td>642.78 <b>(-32.24%)</b></td><td>703.20 <b>(-21.92%)</b></td><td>421.70 <b>(-35.30%)</b></td><td>156.06 <b>(-39.99%)</b></td><td>318.25 <b>(+54.55%)</b></td><td>220.81 <b>(+47.06%)</b></td><td>190.86 <b>(+28.06%)</b></td><td>172.31 <b>(+69.10%)</b></td><td>62.53 <b>(+54.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.61 (n/a)</td><td>1.17 (n/a)</td><td>1.16 (n/a)</td><td>0.80 (n/a)</td><td>0.32 (n/a)</td><td>1317.10 (n/a)</td><td>948.66 (n/a)</td><td>900.60 (n/a)</td><td>651.80 (n/a)</td><td>260.05 (n/a)</td><td>205.92 (n/a)</td><td>150.15 (n/a)</td><td>149.04 (n/a)</td><td>101.90 (n/a)</td><td>40.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.00 (-16.17%)</td><td>1.58 (-12.50%)</td><td>1.67 (-17.66%)</td><td>1.06 (+3.55%)</td><td>0.44 <b>(-26.77%)</b></td><td>989.50 (-3.43%)</td><td>711.10 (+9.90%)</td><td>629.20 <b>(+21.44%)</b></td><td>525.30 (+19.31%)</td><td>212.30 (-15.90%)</td><td>255.53 (-16.17%)</td><td>201.97 (-12.50%)</td><td>213.30 (-17.66%)</td><td>135.65 (+3.55%)</td><td>55.83 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.38 (n/a)</td><td>1.80 (n/a)</td><td>2.02 (n/a)</td><td>1.02 (n/a)</td><td>0.60 (n/a)</td><td>1024.60 (n/a)</td><td>647.06 (n/a)</td><td>518.10 (n/a)</td><td>440.30 (n/a)</td><td>252.45 (n/a)</td><td>304.83 (n/a)</td><td>230.82 (n/a)</td><td>259.04 (n/a)</td><td>130.99 (n/a)</td><td>76.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.66 (-9.48%)</td><td>1.24 (+11.55%)</td><td>1.20 (-6.95%)</td><td>0.93 <b>(+216.25%)</b></td><td>0.29 <b>(-57.82%)</b></td><td>1130.10 <b>(-68.38%)</b></td><td>885.36 <b>(-42.99%)</b></td><td>874.90 (+7.46%)</td><td>631.70 (+10.48%)</td><td>198.00 <b>(-84.82%)</b></td><td>212.46 (-9.48%)</td><td>158.14 (+11.55%)</td><td>153.40 (-6.95%)</td><td>118.77 <b>(+216.25%)</b></td><td>37.15 <b>(-57.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.83 (n/a)</td><td>1.11 (n/a)</td><td>1.29 (n/a)</td><td>0.29 (n/a)</td><td>0.69 (n/a)</td><td>3573.90 (n/a)</td><td>1553.08 (n/a)</td><td>814.20 (n/a)</td><td>571.80 (n/a)</td><td>1303.97 (n/a)</td><td>234.72 (n/a)</td><td>141.77 (n/a)</td><td>164.86 (n/a)</td><td>37.55 (n/a)</td><td>88.06 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.63 (+5.05%)</td><td>1.28 (+12.53%)</td><td>1.23 (-1.59%)</td><td>1.08 <b>(+261.03%)</b></td><td>0.21 <b>(-57.18%)</b></td><td>968.00 <b>(-72.30%)</b></td><td>833.14 <b>(-37.18%)</b></td><td>852.80 (+1.62%)</td><td>644.50 (-4.81%)</td><td>121.67 <b>(-89.98%)</b></td><td>208.24 (+5.05%)</td><td>164.20 (+12.53%)</td><td>157.39 (-1.59%)</td><td>138.65 <b>(+261.03%)</b></td><td>26.75 <b>(-57.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.55 (n/a)</td><td>1.14 (n/a)</td><td>1.25 (n/a)</td><td>0.30 (n/a)</td><td>0.49 (n/a)</td><td>3494.90 (n/a)</td><td>1326.30 (n/a)</td><td>839.20 (n/a)</td><td>677.10 (n/a)</td><td>1214.58 (n/a)</td><td>198.24 (n/a)</td><td>145.91 (n/a)</td><td>159.93 (n/a)</td><td>38.40 (n/a)</td><td>62.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.40 <b>(+38.93%)</b></td><td>1.60 <b>(+39.35%)</b></td><td>1.32 (+7.54%)</td><td>1.18 <b>(+155.42%)</b></td><td>0.51 (+10.41%)</td><td>885.00 <b>(-60.85%)</b></td><td>703.96 <b>(-36.76%)</b></td><td>795.70 (-7.01%)</td><td>436.60 <b>(-28.03%)</b></td><td>188.28 <b>(-71.45%)</b></td><td>307.41 <b>(+38.93%)</b></td><td>204.44 <b>(+39.35%)</b></td><td>168.68 (+7.54%)</td><td>151.66 <b>(+155.42%)</b></td><td>65.33 (+10.41%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.73 (n/a)</td><td>1.15 (n/a)</td><td>1.23 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>2260.40 (n/a)</td><td>1113.18 (n/a)</td><td>855.70 (n/a)</td><td>606.60 (n/a)</td><td>659.56 (n/a)</td><td>221.27 (n/a)</td><td>146.72 (n/a)</td><td>156.86 (n/a)</td><td>59.38 (n/a)</td><td>59.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.99 (-16.90%)</td><td>0.70 (-16.70%)</td><td>0.73 (-11.81%)</td><td>0.40 <b>(-34.30%)</b></td><td>0.24 (+8.29%)</td><td>911.50 <b>(+52.20%)</b></td><td>572.48 <b>(+27.16%)</b></td><td>491.30 (+13.39%)</td><td>365.30 <b>(+20.32%)</b></td><td>223.62 <b>(+100.87%)</b></td><td>45.92 (-16.90%)</td><td>32.71 (-16.70%)</td><td>34.15 (-11.81%)</td><td>18.41 <b>(-34.30%)</b></td><td>11.21 (+8.29%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.19 (n/a)</td><td>0.84 (n/a)</td><td>0.83 (n/a)</td><td>0.60 (n/a)</td><td>0.22 (n/a)</td><td>598.90 (n/a)</td><td>450.20 (n/a)</td><td>433.30 (n/a)</td><td>303.60 (n/a)</td><td>111.33 (n/a)</td><td>55.26 (n/a)</td><td>39.26 (n/a)</td><td>38.72 (n/a)</td><td>28.01 (n/a)</td><td>10.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.85 (-9.26%)</td><td>1.97 <b>(-20.78%)</b></td><td>1.83 <b>(-28.58%)</b></td><td>1.12 <b>(-31.11%)</b></td><td>0.73 <b>(+34.52%)</b></td><td>3742.60 <b>(+45.16%)</b></td><td>2391.86 <b>(+35.62%)</b></td><td>2288.60 <b>(+40.02%)</b></td><td>1471.30 (+10.20%)</td><td>933.23 <b>(+97.06%)</b></td><td>729.77 (-9.26%)</td><td>505.59 <b>(-20.78%)</b></td><td>469.16 <b>(-28.58%)</b></td><td>286.90 <b>(-31.11%)</b></td><td>187.60 <b>(+34.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.14 (n/a)</td><td>2.49 (n/a)</td><td>2.57 (n/a)</td><td>1.63 (n/a)</td><td>0.54 (n/a)</td><td>2578.30 (n/a)</td><td>1763.62 (n/a)</td><td>1634.50 (n/a)</td><td>1335.10 (n/a)</td><td>473.57 (n/a)</td><td>804.26 (n/a)</td><td>638.20 (n/a)</td><td>656.93 (n/a)</td><td>416.45 (n/a)</td><td>139.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.57 (+0.32%)</td><td>2.26 (-10.85%)</td><td>2.17 (-18.62%)</td><td>1.13 (-2.45%)</td><td>0.91 (+3.26%)</td><td>2319.90 (+2.51%)</td><td>1340.44 (+12.13%)</td><td>1207.00 <b>(+22.89%)</b></td><td>734.10 (-0.31%)</td><td>606.79 (-0.70%)</td><td>731.36 (+0.32%)</td><td>463.52 (-10.85%)</td><td>444.82 (-18.62%)</td><td>231.42 (-2.45%)</td><td>187.02 (+3.26%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.56 (n/a)</td><td>2.54 (n/a)</td><td>2.67 (n/a)</td><td>1.16 (n/a)</td><td>0.88 (n/a)</td><td>2263.10 (n/a)</td><td>1195.44 (n/a)</td><td>982.20 (n/a)</td><td>736.40 (n/a)</td><td>611.07 (n/a)</td><td>729.02 (n/a)</td><td>519.92 (n/a)</td><td>546.60 (n/a)</td><td>237.22 (n/a)</td><td>181.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.79 (+12.33%)</td><td>3.34 <b>(+26.62%)</b></td><td>3.29 <b>(+21.98%)</b></td><td>2.87 <b>(+67.28%)</b></td><td>0.34 <b>(-45.85%)</b></td><td>2736.70 <b>(-40.22%)</b></td><td>2371.46 <b>(-24.48%)</b></td><td>2392.00 (-18.02%)</td><td>2077.70 (-10.98%)</td><td>246.28 <b>(-71.84%)</b></td><td>1162.81 (+12.33%)</td><td>1027.39 <b>(+26.62%)</b></td><td>1009.99 <b>(+21.98%)</b></td><td>882.79 <b>(+67.28%)</b></td><td>104.35 <b>(-45.85%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.37 (n/a)</td><td>2.64 (n/a)</td><td>2.70 (n/a)</td><td>1.72 (n/a)</td><td>0.63 (n/a)</td><td>4577.80 (n/a)</td><td>3140.18 (n/a)</td><td>2917.70 (n/a)</td><td>2333.90 (n/a)</td><td>874.50 (n/a)</td><td>1035.16 (n/a)</td><td>811.40 (n/a)</td><td>828.01 (n/a)</td><td>527.75 (n/a)</td><td>192.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.00 (n/a)</td><td>307.08 (n/a)</td><td>273.30 (n/a)</td><td>236.00 (n/a)</td><td>94.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.80 (n/a)</td><td>306.66 (n/a)</td><td>226.00 (n/a)</td><td>175.10 (n/a)</td><td>147.69 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1901.30 (n/a)</td><td>647.90 (n/a)</td><td>366.60 (n/a)</td><td>230.20 (n/a)</td><td>706.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1001.20 (n/a)</td><td>540.40 (n/a)</td><td>548.70 (n/a)</td><td>246.60 (n/a)</td><td>289.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>642.00 (n/a)</td><td>342.90 (n/a)</td><td>272.30 (n/a)</td><td>252.20 (n/a)</td><td>167.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.60 (n/a)</td><td>378.32 (n/a)</td><td>326.30 (n/a)</td><td>240.00 (n/a)</td><td>155.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>280.20 (n/a)</td><td>259.50 (n/a)</td><td>272.80 (n/a)</td><td>226.90 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.70 (n/a)</td><td>368.30 (n/a)</td><td>349.30 (n/a)</td><td>218.90 (n/a)</td><td>124.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.40 (n/a)</td><td>359.62 (n/a)</td><td>315.50 (n/a)</td><td>241.80 (n/a)</td><td>110.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.20 (n/a)</td><td>416.50 (n/a)</td><td>422.20 (n/a)</td><td>267.50 (n/a)</td><td>154.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.20 (n/a)</td><td>351.58 (n/a)</td><td>304.80 (n/a)</td><td>230.80 (n/a)</td><td>114.93 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.70 (n/a)</td><td>442.14 (n/a)</td><td>514.10 (n/a)</td><td>233.80 (n/a)</td><td>124.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>444.00 (n/a)</td><td>342.92 (n/a)</td><td>296.40 (n/a)</td><td>256.90 (n/a)</td><td>83.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1948.40 (n/a)</td><td>634.72 (n/a)</td><td>314.10 (n/a)</td><td>258.20 (n/a)</td><td>735.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>334.12 (n/a)</td><td>292.70 (n/a)</td><td>251.20 (n/a)</td><td>110.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>669.10 (n/a)</td><td>453.12 (n/a)</td><td>392.20 (n/a)</td><td>268.40 (n/a)</td><td>168.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.60 (n/a)</td><td>392.52 (n/a)</td><td>439.50 (n/a)</td><td>188.00 (n/a)</td><td>139.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1878.40 (n/a)</td><td>743.42 (n/a)</td><td>529.40 (n/a)</td><td>315.70 (n/a)</td><td>646.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>556.50 (n/a)</td><td>435.20 (n/a)</td><td>462.30 (n/a)</td><td>274.60 (n/a)</td><td>106.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>543.20 (n/a)</td><td>376.46 (n/a)</td><td>294.30 (n/a)</td><td>230.40 (n/a)</td><td>145.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.10 (n/a)</td><td>393.36 (n/a)</td><td>329.10 (n/a)</td><td>253.20 (n/a)</td><td>145.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>601.90 (n/a)</td><td>431.52 (n/a)</td><td>468.00 (n/a)</td><td>239.90 (n/a)</td><td>158.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>707.10 (n/a)</td><td>500.74 (n/a)</td><td>532.40 (n/a)</td><td>271.90 (n/a)</td><td>160.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>523.50 (n/a)</td><td>417.84 (n/a)</td><td>364.50 (n/a)</td><td>345.60 (n/a)</td><td>84.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.63 <b>(+28.83%)</b></td><td>0.58 <b>(+82.58%)</b></td><td>0.63 <b>(+85.70%)</b></td><td>0.46 <b>(+270.24%)</b></td><td>0.08 <b>(-42.60%)</b></td><td>482.90 <b>(-72.99%)</b></td><td>390.00 <b>(-54.99%)</b></td><td>352.60 <b>(-46.14%)</b></td><td>351.60 <b>(-22.38%)</b></td><td>57.72 <b>(-89.13%)</b></td><td>26.84 <b>(+28.83%)</b></td><td>24.58 <b>(+82.58%)</b></td><td>26.77 <b>(+85.70%)</b></td><td>19.54 <b>(+270.24%)</b></td><td>3.26 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>1787.80 (n/a)</td><td>866.40 (n/a)</td><td>654.70 (n/a)</td><td>453.00 (n/a)</td><td>531.16 (n/a)</td><td>20.83 (n/a)</td><td>13.46 (n/a)</td><td>14.41 (n/a)</td><td>5.28 (n/a)</td><td>5.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.53 (-9.11%)</td><td>0.47 (+9.01%)</td><td>0.50 <b>(+22.53%)</b></td><td>0.40 <b>(+20.58%)</b></td><td>0.06 <b>(-35.22%)</b></td><td>559.70 (-17.06%)</td><td>481.82 (-10.24%)</td><td>445.70 (-18.38%)</td><td>417.10 (+10.02%)</td><td>67.51 <b>(-38.36%)</b></td><td>22.62 (-9.11%)</td><td>19.89 (+9.01%)</td><td>21.17 <b>(+22.53%)</b></td><td>16.86 <b>(+20.58%)</b></td><td>2.68 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>674.80 (n/a)</td><td>536.80 (n/a)</td><td>546.10 (n/a)</td><td>379.10 (n/a)</td><td>109.52 (n/a)</td><td>24.89 (n/a)</td><td>18.24 (n/a)</td><td>17.28 (n/a)</td><td>13.98 (n/a)</td><td>4.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.31 (-0.05%)</td><td>0.31 (+0.22%)</td><td>0.31 (+1.32%)</td><td>0.29 (-2.15%)</td><td>0.01 <b>(+87.06%)</b></td><td>85862.70 (+2.20%)</td><td>82463.70 (-0.19%)</td><td>81566.50 (-1.30%)</td><td>81278.70 (+0.05%)</td><td>1944.66 <b>(+91.55%)</b></td><td>211.37 (-0.05%)</td><td>208.42 (+0.22%)</td><td>210.62 (+1.32%)</td><td>200.09 (-2.15%)</td><td>4.78 <b>(+87.05%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84014.00 (n/a)</td><td>82622.50 (n/a)</td><td>82643.50 (n/a)</td><td>81238.70 (n/a)</td><td>1015.22 (n/a)</td><td>211.47 (n/a)</td><td>207.96 (n/a)</td><td>207.88 (n/a)</td><td>204.49 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.15 (+0.00%)</td><td>1.13 (-0.15%)</td><td>1.14 (-0.62%)</td><td>1.09 (-0.66%)</td><td>0.02 (+6.53%)</td><td>23060.40 (+0.66%)</td><td>22296.34 (+0.16%)</td><td>22165.00 (+0.62%)</td><td>21905.00 (+0.00%)</td><td>464.20 (+7.50%)</td><td>784.29 (+0.00%)</td><td>770.79 (-0.15%)</td><td>775.09 (-0.62%)</td><td>744.99 (-0.66%)</td><td>15.76 (+6.53%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.10 (n/a)</td><td>0.02 (n/a)</td><td>22909.20 (n/a)</td><td>22260.94 (n/a)</td><td>22028.70 (n/a)</td><td>21905.00 (n/a)</td><td>431.79 (n/a)</td><td>784.29 (n/a)</td><td>771.98 (n/a)</td><td>779.89 (n/a)</td><td>749.91 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.80 (-0.33%)</td><td>0.79 (+0.32%)</td><td>0.79 (+0.07%)</td><td>0.78 (+3.06%)</td><td>0.01 <b>(-62.56%)</b></td><td>96247.70 (-2.97%)</td><td>95171.90 (-0.35%)</td><td>95109.90 (-0.07%)</td><td>94112.60 (+0.33%)</td><td>782.82 <b>(-63.66%)</b></td><td>730.18 (-0.33%)</td><td>722.10 (+0.32%)</td><td>722.53 (+0.07%)</td><td>713.99 (+3.06%)</td><td>5.94 <b>(-62.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.02 (n/a)</td><td>99196.30 (n/a)</td><td>95509.78 (n/a)</td><td>95178.10 (n/a)</td><td>93801.90 (n/a)</td><td>2154.25 (n/a)</td><td>732.60 (n/a)</td><td>719.79 (n/a)</td><td>722.01 (n/a)</td><td>692.76 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (+0.20%)</td><td>0.77 (-1.13%)</td><td>0.76 (-1.70%)</td><td>0.76 (-1.73%)</td><td>0.01 <b>(+152.73%)</b></td><td>99868.70 (+1.76%)</td><td>98421.68 (+1.16%)</td><td>98835.40 (+1.73%)</td><td>96468.70 (-0.20%)</td><td>1528.01 <b>(+156.89%)</b></td><td>712.35 (+0.20%)</td><td>698.35 (-1.13%)</td><td>695.29 (-1.70%)</td><td>688.10 (-1.73%)</td><td>10.89 <b>(+152.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98136.80 (n/a)</td><td>97292.54 (n/a)</td><td>97150.90 (n/a)</td><td>96662.50 (n/a)</td><td>594.82 (n/a)</td><td>710.92 (n/a)</td><td>706.34 (n/a)</td><td>707.35 (n/a)</td><td>700.24 (n/a)</td><td>4.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.90 (+0.25%)</td><td>0.89 (+0.34%)</td><td>0.89 (+0.85%)</td><td>0.88 (-0.05%)</td><td>0.01 <b>(+21.69%)</b></td><td>85874.30 (+0.05%)</td><td>84749.44 (-0.34%)</td><td>84406.40 (-0.85%)</td><td>84160.30 (-0.25%)</td><td>712.58 <b>(+21.52%)</b></td><td>816.53 (+0.25%)</td><td>810.90 (+0.34%)</td><td>814.15 (+0.85%)</td><td>800.23 (-0.05%)</td><td>6.78 <b>(+21.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85828.20 (n/a)</td><td>85034.56 (n/a)</td><td>85127.20 (n/a)</td><td>84368.50 (n/a)</td><td>586.37 (n/a)</td><td>814.52 (n/a)</td><td>808.17 (n/a)</td><td>807.26 (n/a)</td><td>800.66 (n/a)</td><td>5.57 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.09 <b>(-24.08%)</b></td><td>3.06 (-14.21%)</td><td>2.83 (-15.07%)</td><td>2.14 (-16.13%)</td><td>0.96 (-14.40%)</td><td>4159.20 (+19.23%)</td><td>3143.68 (+17.84%)</td><td>3146.60 (+17.74%)</td><td>2177.10 <b>(+31.73%)</b></td><td>953.47 <b>(+34.32%)</b></td><td>246.60 <b>(-24.08%)</b></td><td>184.61 (-14.21%)</td><td>170.62 (-15.07%)</td><td>129.08 (-16.13%)</td><td>57.54 (-14.40%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>5.39 (n/a)</td><td>3.57 (n/a)</td><td>3.34 (n/a)</td><td>2.55 (n/a)</td><td>1.12 (n/a)</td><td>3488.50 (n/a)</td><td>2667.80 (n/a)</td><td>2672.40 (n/a)</td><td>1652.70 (n/a)</td><td>709.88 (n/a)</td><td>324.84 (n/a)</td><td>215.18 (n/a)</td><td>200.90 (n/a)</td><td>153.90 (n/a)</td><td>67.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.58 (+8.10%)</td><td>2.99 (+4.53%)</td><td>2.71 (+0.52%)</td><td>2.17 (+0.18%)</td><td>0.98 (+16.00%)</td><td>4102.80 (-0.18%)</td><td>3208.36 (-3.08%)</td><td>3289.30 (-0.52%)</td><td>1947.90 (-7.50%)</td><td>879.13 (+6.02%)</td><td>275.61 (+8.10%)</td><td>179.95 (+4.53%)</td><td>163.22 (+0.52%)</td><td>130.86 (+0.18%)</td><td>58.90 (+16.00%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.23 (n/a)</td><td>2.86 (n/a)</td><td>2.70 (n/a)</td><td>2.17 (n/a)</td><td>0.84 (n/a)</td><td>4110.30 (n/a)</td><td>3310.34 (n/a)</td><td>3306.40 (n/a)</td><td>2105.80 (n/a)</td><td>829.22 (n/a)</td><td>254.95 (n/a)</td><td>172.15 (n/a)</td><td>162.37 (n/a)</td><td>130.62 (n/a)</td><td>50.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.86 <b>(+36.56%)</b></td><td>3.96 <b>(+28.97%)</b></td><td>3.46 <b>(+29.77%)</b></td><td>2.21 (+1.93%)</td><td>1.61 <b>(+81.14%)</b></td><td>4041.70 (-1.90%)</td><td>2584.74 (-16.50%)</td><td>2574.80 <b>(-22.94%)</b></td><td>1520.30 <b>(-26.77%)</b></td><td>1054.29 <b>(+26.32%)</b></td><td>353.14 <b>(+36.56%)</b></td><td>238.31 <b>(+28.97%)</b></td><td>208.51 <b>(+29.77%)</b></td><td>132.83 (+1.93%)</td><td>96.77 <b>(+81.14%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.29 (n/a)</td><td>3.07 (n/a)</td><td>2.67 (n/a)</td><td>2.16 (n/a)</td><td>0.89 (n/a)</td><td>4119.80 (n/a)</td><td>3095.60 (n/a)</td><td>3341.40 (n/a)</td><td>2076.10 (n/a)</td><td>834.62 (n/a)</td><td>258.60 (n/a)</td><td>184.79 (n/a)</td><td>160.67 (n/a)</td><td>130.31 (n/a)</td><td>53.42 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.81 (+1.45%)</td><td>5.86 (+5.50%)</td><td>5.75 (+8.08%)</td><td>5.18 (+14.22%)</td><td>0.62 <b>(-35.18%)</b></td><td>6736.30 (-12.45%)</td><td>6002.66 (-6.60%)</td><td>6066.40 (-7.47%)</td><td>5116.90 (-1.42%)</td><td>605.68 <b>(-44.02%)</b></td><td>419.69 (+1.45%)</td><td>360.82 (+5.50%)</td><td>354.00 (+8.08%)</td><td>318.79 (+14.22%)</td><td>38.08 <b>(-35.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.72 (n/a)</td><td>5.55 (n/a)</td><td>5.32 (n/a)</td><td>4.53 (n/a)</td><td>0.95 (n/a)</td><td>7694.10 (n/a)</td><td>6427.04 (n/a)</td><td>6556.30 (n/a)</td><td>5190.80 (n/a)</td><td>1081.93 (n/a)</td><td>413.71 (n/a)</td><td>342.01 (n/a)</td><td>327.54 (n/a)</td><td>279.11 (n/a)</td><td>58.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.76 (-8.76%)</td><td>4.54 (-2.35%)</td><td>4.82 (+12.32%)</td><td>3.56 (-6.99%)</td><td>0.95 (-4.67%)</td><td>9806.00 (+7.51%)</td><td>7958.94 (+2.86%)</td><td>7231.00 (-10.97%)</td><td>6052.70 (+9.61%)</td><td>1701.58 (+19.65%)</td><td>354.80 (-8.76%)</td><td>279.80 (-2.35%)</td><td>296.98 (+12.32%)</td><td>219.00 (-6.99%)</td><td>58.75 (-4.67%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.31 (n/a)</td><td>4.65 (n/a)</td><td>4.29 (n/a)</td><td>3.82 (n/a)</td><td>1.00 (n/a)</td><td>9120.90 (n/a)</td><td>7737.54 (n/a)</td><td>8122.20 (n/a)</td><td>5522.20 (n/a)</td><td>1422.19 (n/a)</td><td>388.88 (n/a)</td><td>286.52 (n/a)</td><td>264.40 (n/a)</td><td>235.45 (n/a)</td><td>61.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.15 (+3.33%)</td><td>5.53 (-4.40%)</td><td>5.03 (-17.61%)</td><td>4.34 (+8.95%)</td><td>1.35 (+19.66%)</td><td>8027.80 (-8.21%)</td><td>6595.18 (+5.54%)</td><td>6927.30 <b>(+21.37%)</b></td><td>4877.40 (-3.23%)</td><td>1519.72 (+3.48%)</td><td>440.29 (+3.33%)</td><td>340.82 (-4.40%)</td><td>310.00 (-17.61%)</td><td>267.51 (+8.95%)</td><td>82.88 (+19.66%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.92 (n/a)</td><td>5.79 (n/a)</td><td>6.11 (n/a)</td><td>3.99 (n/a)</td><td>1.12 (n/a)</td><td>8746.00 (n/a)</td><td>6249.26 (n/a)</td><td>5707.50 (n/a)</td><td>5040.00 (n/a)</td><td>1468.64 (n/a)</td><td>426.09 (n/a)</td><td>356.52 (n/a)</td><td>376.26 (n/a)</td><td>245.54 (n/a)</td><td>69.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (-1.34%)</td><td>0.75 (-1.10%)</td><td>0.75 (-1.28%)</td><td>0.73 (-1.06%)</td><td>0.02 (+13.10%)</td><td>102965.40 (+1.07%)</td><td>100075.02 (+1.13%)</td><td>100131.10 (+1.30%)</td><td>96762.50 (+1.36%)</td><td>2776.78 (+16.29%)</td><td>710.19 (-1.34%)</td><td>687.10 (-1.10%)</td><td>686.29 (-1.28%)</td><td>667.40 (-1.06%)</td><td>19.11 (+13.10%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101878.00 (n/a)</td><td>98955.12 (n/a)</td><td>98850.60 (n/a)</td><td>95467.70 (n/a)</td><td>2387.87 (n/a)</td><td>719.82 (n/a)</td><td>694.78 (n/a)</td><td>695.19 (n/a)</td><td>674.53 (n/a)</td><td>16.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.78 (-0.62%)</td><td>0.77 (+0.21%)</td><td>0.77 (+0.29%)</td><td>0.76 (+0.31%)</td><td>0.01 <b>(-31.95%)</b></td><td>99724.40 (-0.31%)</td><td>98631.28 (-0.21%)</td><td>98626.60 (-0.29%)</td><td>97175.50 (+0.63%)</td><td>950.07 <b>(-31.76%)</b></td><td>707.17 (-0.62%)</td><td>696.78 (+0.21%)</td><td>696.76 (+0.29%)</td><td>689.09 (+0.31%)</td><td>6.74 <b>(-31.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100033.00 (n/a)</td><td>98843.64 (n/a)</td><td>98908.80 (n/a)</td><td>96570.00 (n/a)</td><td>1392.32 (n/a)</td><td>711.60 (n/a)</td><td>695.35 (n/a)</td><td>694.78 (n/a)</td><td>686.97 (n/a)</td><td>9.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.90 (-0.71%)</td><td>0.89 (-0.39%)</td><td>0.89 (-0.15%)</td><td>0.88 (-0.67%)</td><td>0.01 (-10.17%)</td><td>85865.40 (+0.67%)</td><td>84783.38 (+0.39%)</td><td>84401.50 (+0.15%)</td><td>84095.50 (+0.71%)</td><td>727.22 (-9.06%)</td><td>817.16 (-0.71%)</td><td>810.58 (-0.39%)</td><td>814.20 (-0.15%)</td><td>800.32 (-0.67%)</td><td>6.92 (-10.17%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>85293.70 (n/a)</td><td>84452.20 (n/a)</td><td>84278.20 (n/a)</td><td>83502.30 (n/a)</td><td>799.71 (n/a)</td><td>822.96 (n/a)</td><td>813.77 (n/a)</td><td>815.39 (n/a)</td><td>805.68 (n/a)</td><td>7.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.38 (+5.32%)</td><td>2.66 (+4.70%)</td><td>2.50 (+10.40%)</td><td>1.70 (+9.23%)</td><td>1.03 (+5.63%)</td><td>4752.20 (-8.45%)</td><td>3342.72 (-4.64%)</td><td>3219.10 (-9.42%)</td><td>1841.90 (-5.05%)</td><td>1078.66 (-7.95%)</td><td>1147.70 (+5.32%)</td><td>698.86 (+4.70%)</td><td>656.67 (+10.40%)</td><td>444.84 (+9.23%)</td><td>270.04 (+5.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.16 (n/a)</td><td>2.55 (n/a)</td><td>2.27 (n/a)</td><td>1.55 (n/a)</td><td>0.97 (n/a)</td><td>5190.80 (n/a)</td><td>3505.38 (n/a)</td><td>3554.00 (n/a)</td><td>1939.90 (n/a)</td><td>1171.86 (n/a)</td><td>1089.72 (n/a)</td><td>667.49 (n/a)</td><td>594.80 (n/a)</td><td>407.24 (n/a)</td><td>255.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.22 (-7.99%)</td><td>0.21 (+3.07%)</td><td>0.20 (+3.02%)</td><td>0.18 (+15.35%)</td><td>0.02 <b>(-46.09%)</b></td><td>6767.50 (-13.31%)</td><td>6102.66 (-4.29%)</td><td>6207.10 (-2.94%)</td><td>5557.70 (+8.68%)</td><td>492.13 <b>(-49.64%)</b></td><td>12.07 (-7.99%)</td><td>11.05 (+3.07%)</td><td>10.81 (+3.02%)</td><td>9.92 (+15.35%)</td><td>0.89 <b>(-46.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>7806.40 (n/a)</td><td>6376.14 (n/a)</td><td>6394.80 (n/a)</td><td>5113.80 (n/a)</td><td>977.12 (n/a)</td><td>13.12 (n/a)</td><td>10.72 (n/a)</td><td>10.49 (n/a)</td><td>8.60 (n/a)</td><td>1.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.91 (n/a)</td><td>3.77 (n/a)</td><td>3.75 (n/a)</td><td>3.66 (n/a)</td><td>0.09 (n/a)</td><td>3.90 (n/a)</td><td>3.77 (n/a)</td><td>3.75 (n/a)</td><td>3.65 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.66 (+19.05%)</td><td>6.55 (+10.86%)</td><td>6.70 (+16.14%)</td><td>5.70 (+0.81%)</td><td>0.80 <b>(+147.27%)</b></td><td>7.66 (+19.05%)</td><td>6.54 (+10.86%)</td><td>6.70 (+16.14%)</td><td>5.69 (+0.81%)</td><td>0.80 <b>(+147.27%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.44 (n/a)</td><td>5.90 (n/a)</td><td>5.77 (n/a)</td><td>5.65 (n/a)</td><td>0.32 (n/a)</td><td>6.43 (n/a)</td><td>5.90 (n/a)</td><td>5.77 (n/a)</td><td>5.65 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>12.17 (-9.68%)</td><td>9.22 (-2.47%)</td><td>9.10 (-2.18%)</td><td>7.05 (+10.84%)</td><td>2.11 (-19.15%)</td><td>12.16 (-9.68%)</td><td>9.21 (-2.47%)</td><td>9.09 (-2.18%)</td><td>7.05 (+10.84%)</td><td>2.10 (-19.15%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>13.47 (n/a)</td><td>9.45 (n/a)</td><td>9.30 (n/a)</td><td>6.36 (n/a)</td><td>2.60 (n/a)</td><td>13.46 (n/a)</td><td>9.45 (n/a)</td><td>9.29 (n/a)</td><td>6.36 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.74 (n/a)</td><td>3.60 (n/a)</td><td>3.60 (n/a)</td><td>3.44 (n/a)</td><td>0.11 (n/a)</td><td>3.74 (n/a)</td><td>3.60 (n/a)</td><td>3.60 (n/a)</td><td>3.44 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>7.42 (-2.00%)</td><td>6.81 (+7.57%)</td><td>6.70 (+9.16%)</td><td>6.44 (+19.68%)</td><td>0.39 <b>(-55.64%)</b></td><td>7.42 (-2.00%)</td><td>6.80 (+7.57%)</td><td>6.69 (+9.16%)</td><td>6.44 (+19.68%)</td><td>0.39 <b>(-55.64%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.58 (n/a)</td><td>6.33 (n/a)</td><td>6.14 (n/a)</td><td>5.38 (n/a)</td><td>0.87 (n/a)</td><td>7.57 (n/a)</td><td>6.32 (n/a)</td><td>6.13 (n/a)</td><td>5.38 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>14.45 (+7.34%)</td><td>12.08 (+9.24%)</td><td>13.19 (+8.30%)</td><td>9.02 (+9.16%)</td><td>2.48 (-1.85%)</td><td>14.44 (+7.34%)</td><td>12.07 (+9.24%)</td><td>13.18 (+8.30%)</td><td>9.02 (+9.16%)</td><td>2.48 (-1.85%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>13.46 (n/a)</td><td>11.06 (n/a)</td><td>12.18 (n/a)</td><td>8.27 (n/a)</td><td>2.53 (n/a)</td><td>13.45 (n/a)</td><td>11.05 (n/a)</td><td>12.17 (n/a)</td><td>8.26 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.23 (+18.10%)</td><td>2.01 (-10.30%)</td><td>1.68 <b>(-34.29%)</b></td><td>1.02 (-13.53%)</td><td>1.08 <b>(+63.39%)</b></td><td>3.22 (+18.10%)</td><td>2.01 (-10.30%)</td><td>1.68 <b>(-34.29%)</b></td><td>1.02 (-13.53%)</td><td>1.08 <b>(+63.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.73 (n/a)</td><td>2.24 (n/a)</td><td>2.56 (n/a)</td><td>1.18 (n/a)</td><td>0.66 (n/a)</td><td>2.73 (n/a)</td><td>2.24 (n/a)</td><td>2.56 (n/a)</td><td>1.18 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 <b>(+20.09%)</b></td><td>0.44 <b>(+50.07%)</b></td><td>0.51 <b>(+53.30%)</b></td><td>0.14 <b>(+93.11%)</b></td><td>0.17 (+13.83%)</td><td>0.54 <b>(+20.09%)</b></td><td>0.43 <b>(+50.07%)</b></td><td>0.50 <b>(+53.30%)</b></td><td>0.14 <b>(+93.11%)</b></td><td>0.16 (+13.83%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.75 <b>(+52.93%)</b></td><td>0.66 <b>(+92.30%)</b></td><td>0.64 <b>(+65.81%)</b></td><td>0.56 <b>(+651.93%)</b></td><td>0.07 <b>(-58.58%)</b></td><td>0.74 <b>(+52.93%)</b></td><td>0.65 <b>(+92.30%)</b></td><td>0.64 <b>(+65.81%)</b></td><td>0.55 <b>(+651.93%)</b></td><td>0.07 <b>(-58.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.77 <b>(+23.25%)</b></td><td>2.01 <b>(+30.86%)</b></td><td>1.92 (+19.97%)</td><td>1.08 <b>(+39.59%)</b></td><td>0.64 (+8.03%)</td><td>2.72 <b>(+23.25%)</b></td><td>1.97 <b>(+30.86%)</b></td><td>1.89 (+19.97%)</td><td>1.06 <b>(+39.59%)</b></td><td>0.63 (+8.03%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.25 (n/a)</td><td>1.53 (n/a)</td><td>1.60 (n/a)</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>2.21 (n/a)</td><td>1.51 (n/a)</td><td>1.58 (n/a)</td><td>0.76 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.40 (n/a)</td><td>311.00 (n/a)</td><td>262.10 (n/a)</td><td>233.10 (n/a)</td><td>137.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>331.10 (n/a)</td><td>295.40 (n/a)</td><td>195.30 (n/a)</td><td>133.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.30 (n/a)</td><td>380.72 (n/a)</td><td>385.10 (n/a)</td><td>265.60 (n/a)</td><td>114.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.20 (n/a)</td><td>424.56 (n/a)</td><td>463.70 (n/a)</td><td>226.20 (n/a)</td><td>116.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>666.50 (n/a)</td><td>422.22 (n/a)</td><td>411.70 (n/a)</td><td>233.20 (n/a)</td><td>181.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>683.50 (n/a)</td><td>449.08 (n/a)</td><td>421.80 (n/a)</td><td>294.40 (n/a)</td><td>142.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.60 (n/a)</td><td>319.68 (n/a)</td><td>277.30 (n/a)</td><td>157.00 (n/a)</td><td>128.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.50 (n/a)</td><td>413.16 (n/a)</td><td>461.40 (n/a)</td><td>186.30 (n/a)</td><td>176.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>693.30 (n/a)</td><td>487.92 (n/a)</td><td>483.80 (n/a)</td><td>351.20 (n/a)</td><td>137.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.80 (n/a)</td><td>467.06 (n/a)</td><td>501.30 (n/a)</td><td>246.40 (n/a)</td><td>131.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.50 (n/a)</td><td>414.88 (n/a)</td><td>442.90 (n/a)</td><td>274.90 (n/a)</td><td>133.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.40 (n/a)</td><td>408.32 (n/a)</td><td>466.20 (n/a)</td><td>244.80 (n/a)</td><td>100.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>607.20 (n/a)</td><td>464.98 (n/a)</td><td>531.00 (n/a)</td><td>320.20 (n/a)</td><td>131.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>603.40 (n/a)</td><td>422.72 (n/a)</td><td>398.90 (n/a)</td><td>337.10 (n/a)</td><td>109.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.20 (n/a)</td><td>423.16 (n/a)</td><td>424.70 (n/a)</td><td>263.20 (n/a)</td><td>130.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>633.20 (n/a)</td><td>436.14 (n/a)</td><td>484.80 (n/a)</td><td>246.80 (n/a)</td><td>151.13 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>621.70 (n/a)</td><td>490.10 (n/a)</td><td>605.90 (n/a)</td><td>205.30 (n/a)</td><td>185.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1066.60 (n/a)</td><td>555.04 (n/a)</td><td>515.30 (n/a)</td><td>263.80 (n/a)</td><td>324.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>658.00 (n/a)</td><td>422.34 (n/a)</td><td>313.10 (n/a)</td><td>264.80 (n/a)</td><td>177.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1966.90 (n/a)</td><td>760.24 (n/a)</td><td>541.90 (n/a)</td><td>214.30 (n/a)</td><td>695.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>609.70 (n/a)</td><td>469.82 (n/a)</td><td>494.70 (n/a)</td><td>250.70 (n/a)</td><td>132.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>625.40 (n/a)</td><td>407.44 (n/a)</td><td>273.10 (n/a)</td><td>253.40 (n/a)</td><td>195.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>463.60 (n/a)</td><td>339.78 (n/a)</td><td>291.10 (n/a)</td><td>230.10 (n/a)</td><td>101.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.60 (n/a)</td><td>453.82 (n/a)</td><td>452.10 (n/a)</td><td>305.00 (n/a)</td><td>154.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(+64.58%)</b></td><td>0.02 <b>(+27.26%)</b></td><td>0.02 <b>(+22.30%)</b></td><td>0.01 (+11.87%)</td><td>0.01 <b>(+253.04%)</b></td><td>296.80 (-10.60%)</td><td>246.12 (-17.79%)</td><td>241.20 (-18.24%)</td><td>157.20 <b>(-39.23%)</b></td><td>57.06 <b>(+89.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>332.00 (n/a)</td><td>299.38 (n/a)</td><td>295.00 (n/a)</td><td>258.70 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(+25.83%)</b></td><td>0.02 (+8.21%)</td><td>0.02 (+18.23%)</td><td>0.01 (-13.14%)</td><td>0.01 <b>(+51.99%)</b></td><td>534.40 (+15.12%)</td><td>297.12 (-1.31%)</td><td>237.80 (-15.43%)</td><td>189.20 <b>(-20.54%)</b></td><td>137.43 <b>(+46.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.20 (n/a)</td><td>301.06 (n/a)</td><td>281.20 (n/a)</td><td>238.10 (n/a)</td><td>93.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-3.49%)</td><td>0.01 (+6.95%)</td><td>0.02 <b>(+34.44%)</b></td><td>0.01 <b>(-32.73%)</b></td><td>0.01 <b>(+48.76%)</b></td><td>651.60 <b>(+48.63%)</b></td><td>379.46 (+4.91%)</td><td>269.50 <b>(-25.61%)</b></td><td>237.40 (+3.62%)</td><td>186.14 <b>(+126.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.40 (n/a)</td><td>361.70 (n/a)</td><td>362.30 (n/a)</td><td>229.10 (n/a)</td><td>82.25 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+16.90%)</td><td>0.01 (+0.13%)</td><td>0.01 (+2.17%)</td><td>0.00 <b>(-38.88%)</b></td><td>0.01 <b>(+62.89%)</b></td><td>1080.90 <b>(+63.60%)</b></td><td>496.58 (+19.89%)</td><td>373.60 (-2.12%)</td><td>236.90 (-14.45%)</td><td>338.45 <b>(+132.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>660.70 (n/a)</td><td>414.18 (n/a)</td><td>381.70 (n/a)</td><td>276.90 (n/a)</td><td>145.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+12.92%)</td><td>0.01 <b>(+31.51%)</b></td><td>0.01 <b>(+41.74%)</b></td><td>0.01 <b>(+23.23%)</b></td><td>0.00 (+19.62%)</td><td>553.70 (-18.86%)</td><td>345.20 <b>(-23.65%)</b></td><td>318.70 <b>(-29.44%)</b></td><td>237.40 (-11.45%)</td><td>128.56 (-14.53%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>682.40 (n/a)</td><td>452.12 (n/a)</td><td>451.70 (n/a)</td><td>268.10 (n/a)</td><td>150.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-2.87%)</td><td>0.01 (-7.62%)</td><td>0.01 (-16.76%)</td><td>0.00 <b>(-33.31%)</b></td><td>0.01 (+15.15%)</td><td>863.70 <b>(+49.95%)</b></td><td>504.94 <b>(+21.97%)</b></td><td>548.60 <b>(+20.15%)</b></td><td>206.60 (+2.94%)</td><td>257.38 <b>(+83.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.00 (n/a)</td><td>413.98 (n/a)</td><td>456.60 (n/a)</td><td>200.70 (n/a)</td><td>140.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-0.15%)</td><td>0.03 <b>(+22.35%)</b></td><td>0.03 (+9.44%)</td><td>0.02 <b>(+89.53%)</b></td><td>0.00 <b>(-57.89%)</b></td><td>332.40 <b>(-47.24%)</b></td><td>277.84 <b>(-29.59%)</b></td><td>269.40 (-8.62%)</td><td>225.30 (+0.18%)</td><td>39.07 <b>(-78.77%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.00 (n/a)</td><td>394.58 (n/a)</td><td>294.80 (n/a)</td><td>224.90 (n/a)</td><td>184.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(+71.39%)</b></td><td>0.03 <b>(+30.64%)</b></td><td>0.02 <b>(+47.75%)</b></td><td>0.01 (-2.42%)</td><td>0.01 <b>(+115.84%)</b></td><td>572.70 (+2.49%)</td><td>377.82 (-13.56%)</td><td>330.30 <b>(-32.33%)</b></td><td>173.00 <b>(-41.67%)</b></td><td>172.89 <b>(+39.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.80 (n/a)</td><td>437.10 (n/a)</td><td>488.10 (n/a)</td><td>296.60 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-0.22%)</td><td>0.02 (-7.17%)</td><td>0.03 (-10.32%)</td><td>0.02 (+10.07%)</td><td>0.01 (-5.43%)</td><td>477.60 (-9.15%)</td><td>359.04 (+6.64%)</td><td>321.10 (+11.49%)</td><td>241.20 (+0.21%)</td><td>108.72 (-8.14%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.70 (n/a)</td><td>336.68 (n/a)</td><td>288.00 (n/a)</td><td>240.70 (n/a)</td><td>118.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (+3.81%)</td><td>0.03 <b>(+33.67%)</b></td><td>0.03 <b>(+59.99%)</b></td><td>0.02 (+11.70%)</td><td>0.01 (+5.80%)</td><td>508.00 (-10.47%)</td><td>335.50 <b>(-25.16%)</b></td><td>303.50 <b>(-37.50%)</b></td><td>227.20 (-3.69%)</td><td>119.59 (-4.41%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>448.28 (n/a)</td><td>485.60 (n/a)</td><td>235.90 (n/a)</td><td>125.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (+3.52%)</td><td>0.03 (-4.27%)</td><td>0.02 <b>(-28.88%)</b></td><td>0.01 (-12.65%)</td><td>0.02 (+16.02%)</td><td>567.20 (+14.49%)</td><td>407.46 (+15.32%)</td><td>526.80 <b>(+40.63%)</b></td><td>145.30 (-3.39%)</td><td>200.13 <b>(+34.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>495.40 (n/a)</td><td>353.34 (n/a)</td><td>374.60 (n/a)</td><td>150.40 (n/a)</td><td>149.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(+25.36%)</b></td><td>0.03 <b>(+42.43%)</b></td><td>0.03 <b>(+91.54%)</b></td><td>0.02 (+12.12%)</td><td>0.01 <b>(+75.01%)</b></td><td>493.30 (-10.81%)</td><td>345.66 <b>(-25.49%)</b></td><td>261.10 <b>(-47.80%)</b></td><td>241.20 <b>(-20.24%)</b></td><td>133.04 <b>(+26.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.10 (n/a)</td><td>463.90 (n/a)</td><td>500.20 (n/a)</td><td>302.40 (n/a)</td><td>105.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+3.12%)</td><td>0.02 (-0.71%)</td><td>0.02 <b>(-42.76%)</b></td><td>0.01 <b>(+210.95%)</b></td><td>0.01 (-17.79%)</td><td>592.90 <b>(-67.84%)</b></td><td>432.34 <b>(-32.08%)</b></td><td>510.90 <b>(+74.67%)</b></td><td>246.90 (-3.02%)</td><td>165.62 <b>(-75.75%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1843.50 (n/a)</td><td>636.52 (n/a)</td><td>292.50 (n/a)</td><td>254.60 (n/a)</td><td>682.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+16.72%)</td><td>0.02 (+4.48%)</td><td>0.01 (-17.30%)</td><td>0.00 <b>(-67.23%)</b></td><td>0.01 <b>(+77.64%)</b></td><td>2302.40 <b>(+205.16%)</b></td><td>807.88 <b>(+53.69%)</b></td><td>568.50 <b>(+20.91%)</b></td><td>259.50 (-14.33%)</td><td>849.63 <b>(+373.49%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>754.50 (n/a)</td><td>525.64 (n/a)</td><td>470.20 (n/a)</td><td>302.90 (n/a)</td><td>179.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 <b>(+30.88%)</b></td><td>0.05 (+17.80%)</td><td>0.06 (+14.86%)</td><td>0.03 (+5.72%)</td><td>0.02 <b>(+62.43%)</b></td><td>519.20 (-5.41%)</td><td>351.04 (-8.85%)</td><td>295.00 (-12.95%)</td><td>206.90 <b>(-23.60%)</b></td><td>151.56 <b>(+23.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>548.90 (n/a)</td><td>385.12 (n/a)</td><td>338.90 (n/a)</td><td>270.80 (n/a)</td><td>122.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 <b>(+23.34%)</b></td><td>0.05 <b>(+46.03%)</b></td><td>0.06 <b>(+85.06%)</b></td><td>0.03 (+2.99%)</td><td>0.02 <b>(+34.94%)</b></td><td>614.10 (-2.91%)</td><td>343.02 <b>(-28.77%)</b></td><td>283.90 <b>(-45.96%)</b></td><td>241.20 (-18.95%)</td><td>153.01 (+17.84%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>632.50 (n/a)</td><td>481.56 (n/a)</td><td>525.40 (n/a)</td><td>297.60 (n/a)</td><td>129.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 <b>(+21.35%)</b></td><td>0.05 <b>(+20.15%)</b></td><td>0.05 <b>(+49.40%)</b></td><td>0.03 (-9.33%)</td><td>0.02 <b>(+78.18%)</b></td><td>642.30 (+10.29%)</td><td>390.78 (-9.10%)</td><td>299.70 <b>(-33.06%)</b></td><td>255.60 (-17.60%)</td><td>173.31 <b>(+58.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.40 (n/a)</td><td>429.90 (n/a)</td><td>447.70 (n/a)</td><td>310.20 (n/a)</td><td>109.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+12.12%)</td><td>0.05 <b>(+42.37%)</b></td><td>0.05 <b>(+84.05%)</b></td><td>0.03 <b>(+23.40%)</b></td><td>0.02 <b>(+22.34%)</b></td><td>606.50 (-18.96%)</td><td>387.26 <b>(-28.68%)</b></td><td>302.20 <b>(-45.67%)</b></td><td>244.20 (-10.78%)</td><td>168.66 (-10.46%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>748.40 (n/a)</td><td>543.00 (n/a)</td><td>556.20 (n/a)</td><td>273.70 (n/a)</td><td>188.36 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (+2.91%)</td><td>0.06 <b>(+34.43%)</b></td><td>0.07 <b>(+84.58%)</b></td><td>0.03 <b>(+359.64%)</b></td><td>0.02 <b>(-23.24%)</b></td><td>521.70 <b>(-78.24%)</b></td><td>345.92 <b>(-57.59%)</b></td><td>245.30 <b>(-45.83%)</b></td><td>203.10 (-2.82%)</td><td>159.90 <b>(-82.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2397.80 (n/a)</td><td>815.68 (n/a)</td><td>452.80 (n/a)</td><td>209.00 (n/a)</td><td>911.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-11.59%)</td><td>0.04 <b>(-23.07%)</b></td><td>0.03 <b>(-50.82%)</b></td><td>0.02 (+3.20%)</td><td>0.02 (-8.29%)</td><td>1022.90 (-3.10%)</td><td>564.94 <b>(+24.27%)</b></td><td>617.90 <b>(+103.32%)</b></td><td>241.30 (+13.13%)</td><td>312.14 (-9.96%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1055.60 (n/a)</td><td>454.60 (n/a)</td><td>303.90 (n/a)</td><td>213.30 (n/a)</td><td>346.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (-6.30%)</td><td>0.09 <b>(-20.36%)</b></td><td>0.08 <b>(-32.90%)</b></td><td>0.06 <b>(-22.63%)</b></td><td>0.04 <b>(+36.06%)</b></td><td>542.80 <b>(+29.24%)</b></td><td>393.30 <b>(+33.95%)</b></td><td>416.20 <b>(+49.02%)</b></td><td>243.90 (+6.74%)</td><td>138.26 <b>(+80.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>420.00 (n/a)</td><td>293.62 (n/a)</td><td>279.30 (n/a)</td><td>228.50 (n/a)</td><td>76.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 <b>(+41.21%)</b></td><td>0.12 (+11.87%)</td><td>0.12 (+13.50%)</td><td>0.06 <b>(-31.90%)</b></td><td>0.04 <b>(+202.80%)</b></td><td>515.60 <b>(+46.85%)</b></td><td>296.20 (-0.91%)</td><td>269.80 (-11.89%)</td><td>186.00 <b>(-29.20%)</b></td><td>128.00 <b>(+244.29%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>351.10 (n/a)</td><td>298.92 (n/a)</td><td>306.20 (n/a)</td><td>262.70 (n/a)</td><td>37.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 <b>(+48.92%)</b></td><td>0.10 <b>(+29.31%)</b></td><td>0.10 <b>(+35.24%)</b></td><td>0.07 <b>(+25.54%)</b></td><td>0.02 <b>(+99.12%)</b></td><td>445.70 <b>(-20.35%)</b></td><td>349.44 <b>(-20.51%)</b></td><td>317.20 <b>(-26.06%)</b></td><td>246.80 <b>(-32.84%)</b></td><td>87.05 (+12.25%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>559.60 (n/a)</td><td>439.58 (n/a)</td><td>429.00 (n/a)</td><td>367.50 (n/a)</td><td>77.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (+8.16%)</td><td>0.12 <b>(+35.81%)</b></td><td>0.12 <b>(+64.09%)</b></td><td>0.07 (+18.27%)</td><td>0.04 (-7.03%)</td><td>501.80 (-15.44%)</td><td>302.84 <b>(-28.69%)</b></td><td>273.20 <b>(-39.06%)</b></td><td>195.40 (-7.57%)</td><td>117.42 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>593.40 (n/a)</td><td>424.66 (n/a)</td><td>448.30 (n/a)</td><td>211.40 (n/a)</td><td>147.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 <b>(+31.42%)</b></td><td>0.09 <b>(+24.62%)</b></td><td>0.07 (+4.83%)</td><td>0.05 (+14.97%)</td><td>0.04 <b>(+43.15%)</b></td><td>674.30 (-13.03%)</td><td>439.54 (-17.22%)</td><td>473.00 (-4.62%)</td><td>227.20 <b>(-23.91%)</b></td><td>171.72 (-8.03%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>775.30 (n/a)</td><td>531.00 (n/a)</td><td>495.90 (n/a)</td><td>298.60 (n/a)</td><td>186.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-5.86%)</td><td>0.01 <b>(+36.18%)</b></td><td>0.02 <b>(+67.70%)</b></td><td>0.01 <b>(+46.64%)</b></td><td>0.00 <b>(-32.34%)</b></td><td>451.70 <b>(-31.81%)</b></td><td>303.04 <b>(-31.81%)</b></td><td>270.20 <b>(-40.38%)</b></td><td>243.60 (+6.19%)</td><td>84.83 <b>(-46.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.40 (n/a)</td><td>444.42 (n/a)</td><td>453.20 (n/a)</td><td>229.40 (n/a)</td><td>158.61 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-9.72%)</td><td>0.01 <b>(+22.04%)</b></td><td>0.02 (+9.16%)</td><td>0.01 <b>(+88.79%)</b></td><td>0.00 <b>(-68.28%)</b></td><td>317.10 <b>(-47.03%)</b></td><td>277.22 <b>(-27.59%)</b></td><td>269.50 (-8.40%)</td><td>250.30 (+10.80%)</td><td>28.41 <b>(-82.17%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.60 (n/a)</td><td>382.84 (n/a)</td><td>294.20 (n/a)</td><td>225.90 (n/a)</td><td>159.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-19.37%)</td><td>0.01 (-5.28%)</td><td>0.01 <b>(+38.65%)</b></td><td>0.01 (-14.52%)</td><td>0.00 <b>(-26.68%)</b></td><td>610.30 (+16.98%)</td><td>425.60 (+2.52%)</td><td>370.80 <b>(-27.87%)</b></td><td>294.60 <b>(+23.99%)</b></td><td>142.90 (+0.88%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.70 (n/a)</td><td>415.12 (n/a)</td><td>514.10 (n/a)</td><td>237.60 (n/a)</td><td>141.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+2.94%)</td><td>0.01 (-14.22%)</td><td>0.01 (-13.91%)</td><td>0.01 <b>(-33.55%)</b></td><td>0.00 <b>(+31.41%)</b></td><td>665.60 <b>(+50.49%)</b></td><td>403.80 <b>(+26.30%)</b></td><td>356.70 (+16.15%)</td><td>229.60 (-2.88%)</td><td>172.39 <b>(+99.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>442.30 (n/a)</td><td>319.72 (n/a)</td><td>307.10 (n/a)</td><td>236.40 (n/a)</td><td>86.49 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-0.76%)</td><td>0.01 <b>(-32.55%)</b></td><td>0.01 <b>(-43.43%)</b></td><td>0.00 <b>(-55.73%)</b></td><td>0.01 <b>(+46.83%)</b></td><td>1049.90 <b>(+125.88%)</b></td><td>574.08 <b>(+81.26%)</b></td><td>519.70 <b>(+76.77%)</b></td><td>240.10 (+0.76%)</td><td>321.52 <b>(+241.22%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.80 (n/a)</td><td>316.72 (n/a)</td><td>294.00 (n/a)</td><td>238.30 (n/a)</td><td>94.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-6.89%)</td><td>0.01 (+9.40%)</td><td>0.01 <b>(+37.75%)</b></td><td>0.01 (+2.58%)</td><td>0.00 (-18.40%)</td><td>503.20 (-2.52%)</td><td>352.94 (-11.15%)</td><td>333.60 <b>(-27.42%)</b></td><td>255.70 (+7.39%)</td><td>101.70 (-16.41%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.20 (n/a)</td><td>397.22 (n/a)</td><td>459.60 (n/a)</td><td>238.10 (n/a)</td><td>121.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(+46.40%)</b></td><td>0.01 (+17.56%)</td><td>0.02 (+18.99%)</td><td>0.01 (-11.71%)</td><td>0.01 <b>(+80.42%)</b></td><td>778.90 (+13.26%)</td><td>400.10 (-1.63%)</td><td>260.50 (-15.97%)</td><td>198.00 <b>(-31.70%)</b></td><td>243.97 <b>(+44.28%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>687.70 (n/a)</td><td>406.74 (n/a)</td><td>310.00 (n/a)</td><td>289.90 (n/a)</td><td>169.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-10.68%)</td><td>0.01 (-11.28%)</td><td>0.01 (-3.00%)</td><td>0.01 <b>(-36.81%)</b></td><td>0.00 (+8.20%)</td><td>748.90 <b>(+58.23%)</b></td><td>463.36 <b>(+20.24%)</b></td><td>476.80 (+3.07%)</td><td>263.90 (+11.96%)</td><td>198.68 <b>(+72.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.30 (n/a)</td><td>385.36 (n/a)</td><td>462.60 (n/a)</td><td>235.70 (n/a)</td><td>114.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+9.76%)</td><td>0.01 (-6.47%)</td><td>0.01 <b>(-30.29%)</b></td><td>0.01 (+12.06%)</td><td>0.00 (+3.94%)</td><td>547.90 (-10.77%)</td><td>417.72 (+4.45%)</td><td>449.60 <b>(+43.46%)</b></td><td>222.90 (-8.87%)</td><td>123.65 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.00 (n/a)</td><td>399.94 (n/a)</td><td>313.40 (n/a)</td><td>244.60 (n/a)</td><td>160.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-1.90%)</td><td>0.01 (-15.68%)</td><td>0.01 (-4.54%)</td><td>0.01 <b>(-22.39%)</b></td><td>0.00 (-6.50%)</td><td>618.20 <b>(+28.85%)</b></td><td>450.90 (+19.04%)</td><td>476.20 (+4.75%)</td><td>234.00 (+1.96%)</td><td>146.04 (+14.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.80 (n/a)</td><td>378.78 (n/a)</td><td>454.60 (n/a)</td><td>229.50 (n/a)</td><td>127.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+16.80%)</td><td>0.01 (+13.15%)</td><td>0.01 (+18.43%)</td><td>0.01 (+3.17%)</td><td>0.00 <b>(+29.67%)</b></td><td>556.40 (-3.07%)</td><td>375.32 (-8.57%)</td><td>361.40 (-15.56%)</td><td>213.90 (-14.37%)</td><td>141.07 (+9.61%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.00 (n/a)</td><td>410.52 (n/a)</td><td>428.00 (n/a)</td><td>249.80 (n/a)</td><td>128.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-5.86%)</td><td>0.01 (-7.51%)</td><td>0.01 (-7.27%)</td><td>0.00 <b>(-74.21%)</b></td><td>0.00 <b>(+55.57%)</b></td><td>2392.50 <b>(+287.70%)</b></td><td>793.94 <b>(+76.41%)</b></td><td>473.10 (+7.84%)</td><td>301.40 (+6.24%)</td><td>897.34 <b>(+604.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.10 (n/a)</td><td>450.06 (n/a)</td><td>438.70 (n/a)</td><td>283.70 (n/a)</td><td>127.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (+17.22%)</td><td>0.03 (+14.28%)</td><td>0.03 (+4.77%)</td><td>0.03 <b>(+51.78%)</b></td><td>0.00 <b>(-25.16%)</b></td><td>298.00 <b>(-34.11%)</b></td><td>276.50 (-14.57%)</td><td>287.70 (-4.58%)</td><td>225.40 (-14.69%)</td><td>29.34 <b>(-60.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>452.30 (n/a)</td><td>323.66 (n/a)</td><td>301.50 (n/a)</td><td>264.20 (n/a)</td><td>74.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-14.38%)</td><td>0.02 (+0.71%)</td><td>0.02 (+9.72%)</td><td>0.02 <b>(+270.87%)</b></td><td>0.00 <b>(-55.22%)</b></td><td>545.60 <b>(-73.04%)</b></td><td>432.74 <b>(-38.17%)</b></td><td>411.70 (-8.86%)</td><td>312.90 (+16.80%)</td><td>99.88 <b>(-86.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2023.40 (n/a)</td><td>699.84 (n/a)</td><td>451.70 (n/a)</td><td>267.90 (n/a)</td><td>745.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 <b>(-31.00%)</b></td><td>0.02 (-17.52%)</td><td>0.01 (-17.00%)</td><td>0.01 (-15.16%)</td><td>0.01 <b>(-34.93%)</b></td><td>670.40 (+17.86%)</td><td>496.60 (+16.53%)</td><td>571.70 <b>(+20.48%)</b></td><td>294.40 <b>(+44.95%)</b></td><td>168.88 (+7.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>426.16 (n/a)</td><td>474.50 (n/a)</td><td>203.10 (n/a)</td><td>156.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+8.32%)</td><td>0.02 (-3.85%)</td><td>0.03 (-6.21%)</td><td>0.01 (+5.27%)</td><td>0.01 (+19.07%)</td><td>582.60 (-5.01%)</td><td>383.22 (+5.97%)</td><td>321.80 (+6.63%)</td><td>235.40 (-7.69%)</td><td>147.30 (+1.57%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.30 (n/a)</td><td>361.64 (n/a)</td><td>301.80 (n/a)</td><td>255.00 (n/a)</td><td>145.02 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(+33.37%)</b></td><td>0.03 <b>(+24.91%)</b></td><td>0.03 <b>(+44.18%)</b></td><td>0.02 <b>(+25.27%)</b></td><td>0.01 <b>(+31.91%)</b></td><td>497.90 <b>(-20.17%)</b></td><td>339.14 (-19.34%)</td><td>292.10 <b>(-30.65%)</b></td><td>183.10 <b>(-25.02%)</b></td><td>128.55 (-17.67%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.70 (n/a)</td><td>420.44 (n/a)</td><td>421.20 (n/a)</td><td>244.20 (n/a)</td><td>156.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+1.57%)</td><td>0.03 (-6.65%)</td><td>0.03 (-16.49%)</td><td>0.02 (-1.81%)</td><td>0.01 (+4.98%)</td><td>533.30 (+1.85%)</td><td>341.64 (+8.06%)</td><td>290.40 (+19.75%)</td><td>234.30 (-1.55%)</td><td>129.24 (+4.75%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.60 (n/a)</td><td>316.16 (n/a)</td><td>242.50 (n/a)</td><td>238.00 (n/a)</td><td>123.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (+19.94%)</td><td>0.02 (+6.46%)</td><td>0.02 (-9.96%)</td><td>0.01 (-16.80%)</td><td>0.01 <b>(+60.85%)</b></td><td>595.10 <b>(+20.20%)</b></td><td>402.82 (+1.36%)</td><td>447.40 (+11.07%)</td><td>219.60 (-16.63%)</td><td>153.14 <b>(+52.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>397.40 (n/a)</td><td>402.80 (n/a)</td><td>263.40 (n/a)</td><td>100.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-4.55%)</td><td>0.02 (-5.74%)</td><td>0.02 (+2.24%)</td><td>0.01 (-0.81%)</td><td>0.01 (-8.68%)</td><td>556.90 (+0.81%)</td><td>415.66 (+4.85%)</td><td>394.40 (-2.18%)</td><td>230.20 (+4.78%)</td><td>139.67 (-1.15%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>396.42 (n/a)</td><td>403.20 (n/a)</td><td>219.70 (n/a)</td><td>141.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (+5.82%)</td><td>0.03 <b>(+22.67%)</b></td><td>0.03 (-2.83%)</td><td>0.02 <b>(+313.68%)</b></td><td>0.01 <b>(-37.92%)</b></td><td>455.40 <b>(-75.83%)</b></td><td>306.02 <b>(-50.47%)</b></td><td>301.40 (+2.90%)</td><td>233.00 (-5.52%)</td><td>90.13 <b>(-87.30%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1884.00 (n/a)</td><td>617.90 (n/a)</td><td>292.90 (n/a)</td><td>246.60 (n/a)</td><td>709.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-13.01%)</td><td>0.02 <b>(-27.19%)</b></td><td>0.02 <b>(-39.51%)</b></td><td>0.01 (-13.24%)</td><td>0.01 <b>(-25.75%)</b></td><td>764.70 (+15.25%)</td><td>499.62 <b>(+32.44%)</b></td><td>447.70 <b>(+65.32%)</b></td><td>289.80 (+14.95%)</td><td>176.44 (+0.43%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.50 (n/a)</td><td>377.24 (n/a)</td><td>270.80 (n/a)</td><td>252.10 (n/a)</td><td>175.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+0.49%)</td><td>0.02 (+11.59%)</td><td>0.02 (+15.92%)</td><td>0.01 <b>(+27.20%)</b></td><td>0.01 (-10.60%)</td><td>554.10 <b>(-21.37%)</b></td><td>418.04 (-14.25%)</td><td>477.10 (-13.74%)</td><td>245.90 (-0.49%)</td><td>127.04 <b>(-28.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>704.70 (n/a)</td><td>487.52 (n/a)</td><td>553.10 (n/a)</td><td>247.10 (n/a)</td><td>177.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+10.95%)</td><td>0.02 <b>(+35.55%)</b></td><td>0.02 <b>(+54.25%)</b></td><td>0.01 (+5.69%)</td><td>0.01 <b>(+29.28%)</b></td><td>670.40 (-5.38%)</td><td>441.20 <b>(-22.81%)</b></td><td>418.30 <b>(-35.17%)</b></td><td>253.80 (-9.87%)</td><td>191.17 (+10.96%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>708.50 (n/a)</td><td>571.60 (n/a)</td><td>645.20 (n/a)</td><td>281.60 (n/a)</td><td>172.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+0.76%)</td><td>0.05 (+5.04%)</td><td>0.04 (+17.81%)</td><td>0.03 <b>(+113.57%)</b></td><td>0.02 <b>(-28.50%)</b></td><td>635.10 <b>(-53.18%)</b></td><td>399.08 <b>(-27.08%)</b></td><td>376.30 (-15.11%)</td><td>244.10 (-0.73%)</td><td>154.89 <b>(-66.54%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1356.50 (n/a)</td><td>547.32 (n/a)</td><td>443.30 (n/a)</td><td>245.90 (n/a)</td><td>462.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-16.39%)</td><td>0.05 (-19.03%)</td><td>0.05 <b>(-23.79%)</b></td><td>0.03 <b>(-26.61%)</b></td><td>0.01 (-5.35%)</td><td>567.20 <b>(+36.25%)</b></td><td>384.60 <b>(+26.59%)</b></td><td>322.70 <b>(+31.23%)</b></td><td>274.00 (+19.60%)</td><td>132.71 <b>(+49.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>416.30 (n/a)</td><td>303.82 (n/a)</td><td>245.90 (n/a)</td><td>229.10 (n/a)</td><td>88.64 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-4.56%)</td><td>0.05 (-10.40%)</td><td>0.06 (-11.70%)</td><td>0.04 (+8.70%)</td><td>0.01 (-18.81%)</td><td>467.00 (-8.02%)</td><td>339.22 (+8.65%)</td><td>292.90 (+13.26%)</td><td>257.80 (+4.80%)</td><td>86.75 <b>(-22.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>507.70 (n/a)</td><td>312.20 (n/a)</td><td>258.60 (n/a)</td><td>246.00 (n/a)</td><td>111.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-26.37%)</b></td><td>0.04 <b>(-33.52%)</b></td><td>0.04 <b>(-49.47%)</b></td><td>0.03 (+1.08%)</td><td>0.01 <b>(-52.56%)</b></td><td>530.20 (-1.06%)</td><td>448.52 <b>(+37.41%)</b></td><td>462.40 <b>(+97.86%)</b></td><td>298.20 <b>(+35.79%)</b></td><td>94.48 <b>(-34.06%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>535.90 (n/a)</td><td>326.42 (n/a)</td><td>233.70 (n/a)</td><td>219.60 (n/a)</td><td>143.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-8.56%)</td><td>0.05 (-2.78%)</td><td>0.05 (-8.51%)</td><td>0.03 (+18.79%)</td><td>0.01 <b>(-24.32%)</b></td><td>476.10 (-15.82%)</td><td>347.96 (-3.25%)</td><td>298.90 (+9.33%)</td><td>248.90 (+9.36%)</td><td>109.93 <b>(-29.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>565.60 (n/a)</td><td>359.66 (n/a)</td><td>273.40 (n/a)</td><td>227.60 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+9.75%)</td><td>0.05 (-9.61%)</td><td>0.06 (-7.12%)</td><td>0.01 <b>(-80.56%)</b></td><td>0.03 <b>(+118.59%)</b></td><td>2108.40 <b>(+414.37%)</b></td><td>626.20 <b>(+115.95%)</b></td><td>266.20 (+7.69%)</td><td>221.20 (-8.90%)</td><td>828.82 <b>(+1059.05%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>409.90 (n/a)</td><td>289.98 (n/a)</td><td>247.20 (n/a)</td><td>242.80 (n/a)</td><td>71.51 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-33.49%)</b></td><td>0.04 <b>(-35.13%)</b></td><td>0.04 <b>(-40.36%)</b></td><td>0.03 <b>(-21.33%)</b></td><td>0.01 <b>(-42.73%)</b></td><td>556.10 <b>(+27.11%)</b></td><td>446.64 <b>(+50.06%)</b></td><td>421.00 <b>(+67.73%)</b></td><td>304.10 <b>(+50.40%)</b></td><td>104.44 (+9.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>437.50 (n/a)</td><td>297.64 (n/a)</td><td>251.00 (n/a)</td><td>202.20 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(-46.23%)</b></td><td>0.03 <b>(-44.79%)</b></td><td>0.03 <b>(-27.18%)</b></td><td>0.01 <b>(-78.17%)</b></td><td>0.01 (-6.35%)</td><td>2000.00 <b>(+358.09%)</b></td><td>826.56 <b>(+136.81%)</b></td><td>508.10 <b>(+37.32%)</b></td><td>439.90 <b>(+86.00%)</b></td><td>666.17 <b>(+721.52%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>436.60 (n/a)</td><td>349.04 (n/a)</td><td>370.00 (n/a)</td><td>236.50 (n/a)</td><td>81.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+17.71%)</td><td>0.04 (+7.59%)</td><td>0.03 (+1.85%)</td><td>0.01 <b>(-37.89%)</b></td><td>0.02 <b>(+41.50%)</b></td><td>1117.10 <b>(+60.99%)</b></td><td>536.70 (+9.17%)</td><td>493.70 (-1.81%)</td><td>232.00 (-15.02%)</td><td>349.30 <b>(+91.31%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>693.90 (n/a)</td><td>491.60 (n/a)</td><td>502.80 (n/a)</td><td>273.00 (n/a)</td><td>182.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+2.72%)</td><td>0.05 (-9.95%)</td><td>0.06 (+2.66%)</td><td>0.03 <b>(-23.42%)</b></td><td>0.02 <b>(+42.02%)</b></td><td>599.30 <b>(+30.59%)</b></td><td>369.82 (+19.20%)</td><td>278.30 (-2.62%)</td><td>237.30 (-2.67%)</td><td>153.61 <b>(+77.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.90 (n/a)</td><td>310.26 (n/a)</td><td>285.80 (n/a)</td><td>243.80 (n/a)</td><td>86.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 <b>(+106.68%)</b></td><td>0.06 <b>(+72.51%)</b></td><td>0.05 <b>(+77.72%)</b></td><td>0.04 <b>(+30.60%)</b></td><td>0.02 <b>(+185.43%)</b></td><td>467.60 <b>(-23.44%)</b></td><td>316.42 <b>(-38.74%)</b></td><td>310.20 <b>(-43.73%)</b></td><td>184.30 <b>(-51.60%)</b></td><td>101.20 (+1.94%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>610.80 (n/a)</td><td>516.48 (n/a)</td><td>551.30 (n/a)</td><td>380.80 (n/a)</td><td>99.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-11.33%)</td><td>0.05 (+6.93%)</td><td>0.06 (-0.90%)</td><td>0.04 <b>(+302.38%)</b></td><td>0.01 <b>(-56.30%)</b></td><td>437.80 <b>(-75.15%)</b></td><td>315.96 <b>(-44.81%)</b></td><td>288.50 (+0.91%)</td><td>260.70 (+12.81%)</td><td>73.59 <b>(-88.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1761.60 (n/a)</td><td>572.46 (n/a)</td><td>285.90 (n/a)</td><td>231.10 (n/a)</td><td>665.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (+0.80%)</td><td>0.12 <b>(+24.22%)</b></td><td>0.12 <b>(+54.50%)</b></td><td>0.10 <b>(+42.70%)</b></td><td>0.02 <b>(-46.65%)</b></td><td>341.30 <b>(-29.92%)</b></td><td>286.54 <b>(-24.88%)</b></td><td>284.50 <b>(-35.27%)</b></td><td>243.90 (-0.81%)</td><td>42.58 <b>(-63.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>487.00 (n/a)</td><td>381.42 (n/a)</td><td>439.50 (n/a)</td><td>245.90 (n/a)</td><td>116.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 <b>(+35.50%)</b></td><td>0.12 <b>(+50.62%)</b></td><td>0.12 <b>(+62.56%)</b></td><td>0.06 (+13.89%)</td><td>0.03 <b>(+79.02%)</b></td><td>517.70 (-12.19%)</td><td>306.14 <b>(-30.54%)</b></td><td>265.30 <b>(-38.49%)</b></td><td>236.40 <b>(-26.19%)</b></td><td>119.03 <b>(+20.66%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>589.60 (n/a)</td><td>440.74 (n/a)</td><td>431.30 (n/a)</td><td>320.30 (n/a)</td><td>98.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (+10.75%)</td><td>0.08 (-3.76%)</td><td>0.07 <b>(-31.06%)</b></td><td>0.02 <b>(+33.86%)</b></td><td>0.05 (+6.54%)</td><td>1868.40 <b>(-25.30%)</b></td><td>676.52 (-12.11%)</td><td>442.00 <b>(+45.06%)</b></td><td>247.30 (-9.71%)</td><td>677.71 <b>(-30.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2501.10 (n/a)</td><td>769.72 (n/a)</td><td>304.70 (n/a)</td><td>273.90 (n/a)</td><td>970.81 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (-3.79%)</td><td>0.10 (+5.96%)</td><td>0.11 <b>(+51.93%)</b></td><td>0.02 <b>(-72.14%)</b></td><td>0.05 <b>(+35.34%)</b></td><td>1968.60 <b>(+258.97%)</b></td><td>617.08 <b>(+56.78%)</b></td><td>296.70 <b>(-34.17%)</b></td><td>246.40 (+3.97%)</td><td>755.80 <b>(+473.26%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>548.40 (n/a)</td><td>393.60 (n/a)</td><td>450.70 (n/a)</td><td>237.00 (n/a)</td><td>131.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (+13.79%)</td><td>0.12 (-0.07%)</td><td>0.11 <b>(-21.51%)</b></td><td>0.07 (+17.82%)</td><td>0.04 (-14.37%)</td><td>468.10 (-15.12%)</td><td>305.86 (-5.44%)</td><td>293.00 <b>(+27.45%)</b></td><td>193.20 (-12.10%)</td><td>99.94 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>551.50 (n/a)</td><td>323.46 (n/a)</td><td>229.90 (n/a)</td><td>219.80 (n/a)</td><td>146.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (+17.32%)</td><td>0.10 (+9.91%)</td><td>0.10 (-17.98%)</td><td>0.07 <b>(+343.84%)</b></td><td>0.03 <b>(-39.29%)</b></td><td>452.00 <b>(-77.47%)</b></td><td>335.24 <b>(-48.03%)</b></td><td>318.70 <b>(+21.92%)</b></td><td>214.50 (-14.78%)</td><td>87.03 <b>(-88.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2006.10 (n/a)</td><td>645.04 (n/a)</td><td>261.40 (n/a)</td><td>251.70 (n/a)</td><td>765.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (+11.79%)</td><td>0.10 (-7.05%)</td><td>0.08 <b>(-35.11%)</b></td><td>0.05 (+5.56%)</td><td>0.04 (+2.55%)</td><td>598.50 (-5.27%)</td><td>380.86 (+5.06%)</td><td>392.90 <b>(+54.14%)</b></td><td>195.90 (-10.55%)</td><td>154.10 (-14.13%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>631.80 (n/a)</td><td>362.52 (n/a)</td><td>254.90 (n/a)</td><td>219.00 (n/a)</td><td>179.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (-13.81%)</td><td>0.08 (-16.26%)</td><td>0.08 (-13.83%)</td><td>0.05 (+2.03%)</td><td>0.02 <b>(-38.97%)</b></td><td>605.60 (-1.99%)</td><td>441.78 (+11.55%)</td><td>431.40 (+16.06%)</td><td>289.90 (+16.05%)</td><td>113.00 <b>(-28.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>617.90 (n/a)</td><td>396.04 (n/a)</td><td>371.70 (n/a)</td><td>249.80 (n/a)</td><td>157.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 <b>(+29.50%)</b></td><td>0.12 <b>(+59.03%)</b></td><td>0.13 <b>(+128.61%)</b></td><td>0.02 <b>(+29.23%)</b></td><td>0.06 <b>(+24.26%)</b></td><td>1909.10 <b>(-22.62%)</b></td><td>570.52 <b>(-31.79%)</b></td><td>244.50 <b>(-56.25%)</b></td><td>195.70 <b>(-22.80%)</b></td><td>748.69 (-19.00%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2467.10 (n/a)</td><td>836.44 (n/a)</td><td>558.90 (n/a)</td><td>253.50 (n/a)</td><td>924.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (-17.09%)</td><td>0.11 (+9.49%)</td><td>0.11 <b>(+32.60%)</b></td><td>0.06 <b>(-21.42%)</b></td><td>0.03 <b>(-23.33%)</b></td><td>592.50 <b>(+27.26%)</b></td><td>338.30 (-8.58%)</td><td>292.40 <b>(-24.58%)</b></td><td>231.80 <b>(+20.60%)</b></td><td>144.57 <b>(+32.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>465.60 (n/a)</td><td>370.06 (n/a)</td><td>387.70 (n/a)</td><td>192.20 (n/a)</td><td>109.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (-14.95%)</td><td>0.07 <b>(-30.52%)</b></td><td>0.06 <b>(-39.27%)</b></td><td>0.04 <b>(-35.98%)</b></td><td>0.02 (+9.64%)</td><td>763.30 <b>(+56.19%)</b></td><td>540.18 <b>(+49.72%)</b></td><td>556.20 <b>(+64.65%)</b></td><td>327.80 (+17.58%)</td><td>160.31 <b>(+94.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>488.70 (n/a)</td><td>360.80 (n/a)</td><td>337.80 (n/a)</td><td>278.80 (n/a)</td><td>82.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (-3.30%)</td><td>0.08 (+4.49%)</td><td>0.09 (-13.53%)</td><td>0.02 (-1.19%)</td><td>0.04 (-17.33%)</td><td>2047.00 (+1.20%)</td><td>688.94 (-12.49%)</td><td>355.50 (+15.65%)</td><td>271.70 (+3.39%)</td><td>763.32 (-0.39%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2022.70 (n/a)</td><td>787.28 (n/a)</td><td>307.40 (n/a)</td><td>262.80 (n/a)</td><td>766.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (-10.61%)</td><td>0.09 (+13.89%)</td><td>0.09 <b>(+22.32%)</b></td><td>0.08 <b>(+39.12%)</b></td><td>0.01 <b>(-54.02%)</b></td><td>302.10 <b>(-28.12%)</b></td><td>271.52 (-16.98%)</td><td>281.20 (-18.26%)</td><td>228.30 (+11.86%)</td><td>32.85 <b>(-62.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>420.30 (n/a)</td><td>327.04 (n/a)</td><td>344.00 (n/a)</td><td>204.10 (n/a)</td><td>87.71 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.21 (-11.66%)</td><td>0.17 <b>(+27.43%)</b></td><td>0.20 <b>(+63.13%)</b></td><td>0.10 <b>(+328.18%)</b></td><td>0.06 <b>(-29.26%)</b></td><td>504.70 <b>(-76.65%)</b></td><td>333.30 <b>(-53.11%)</b></td><td>249.00 <b>(-38.70%)</b></td><td>233.00 (+13.22%)</td><td>130.80 <b>(-83.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2161.00 (n/a)</td><td>710.78 (n/a)</td><td>406.20 (n/a)</td><td>205.80 (n/a)</td><td>817.20 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.29 (+2.43%)</td><td>3.40 (-1.84%)</td><td>3.26 (-10.40%)</td><td>2.59 <b>(+28.90%)</b></td><td>0.69 (-18.84%)</td><td>4054.40 <b>(-22.42%)</b></td><td>3189.52 (-1.76%)</td><td>3218.80 (+11.61%)</td><td>2444.90 (-2.37%)</td><td>642.23 <b>(-42.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.19 (n/a)</td><td>3.46 (n/a)</td><td>3.64 (n/a)</td><td>2.01 (n/a)</td><td>0.84 (n/a)</td><td>5226.30 (n/a)</td><td>3246.62 (n/a)</td><td>2883.90 (n/a)</td><td>2504.30 (n/a)</td><td>1118.01 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (-0.75%)</td><td>0.15 (+18.55%)</td><td>0.15 (+6.93%)</td><td>0.11 <b>(+102.70%)</b></td><td>0.02 <b>(-50.05%)</b></td><td>381.20 <b>(-50.67%)</b></td><td>288.42 <b>(-28.24%)</b></td><td>269.90 (-6.48%)</td><td>242.70 (+0.79%)</td><td>56.25 <b>(-74.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>772.70 (n/a)</td><td>401.92 (n/a)</td><td>288.60 (n/a)</td><td>240.80 (n/a)</td><td>223.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+12.01%)</td><td>0.02 (+15.23%)</td><td>0.02 <b>(+23.95%)</b></td><td>0.01 (-6.09%)</td><td>0.01 <b>(+35.27%)</b></td><td>584.70 (+6.48%)</td><td>322.94 (-8.78%)</td><td>248.70 (-19.31%)</td><td>225.90 (-10.75%)</td><td>150.05 <b>(+28.35%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.10 (n/a)</td><td>354.04 (n/a)</td><td>308.20 (n/a)</td><td>253.10 (n/a)</td><td>116.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 <b>(-33.40%)</b></td><td>0.01 <b>(-34.84%)</b></td><td>0.01 <b>(-37.48%)</b></td><td>0.01 (-9.28%)</td><td>0.00 <b>(-39.10%)</b></td><td>515.20 (+10.23%)</td><td>394.70 <b>(+47.36%)</b></td><td>379.20 <b>(+59.93%)</b></td><td>280.80 <b>(+50.16%)</b></td><td>110.28 (-3.35%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>467.40 (n/a)</td><td>267.84 (n/a)</td><td>237.10 (n/a)</td><td>187.00 (n/a)</td><td>114.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+0.30%)</td><td>0.02 <b>(+38.04%)</b></td><td>0.03 <b>(+68.72%)</b></td><td>0.01 <b>(+258.99%)</b></td><td>0.01 <b>(-32.18%)</b></td><td>534.60 <b>(-72.14%)</b></td><td>301.80 <b>(-54.56%)</b></td><td>245.00 <b>(-40.74%)</b></td><td>216.50 (-0.32%)</td><td>132.47 <b>(-81.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1919.00 (n/a)</td><td>664.10 (n/a)</td><td>413.40 (n/a)</td><td>217.20 (n/a)</td><td>711.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+19.94%)</td><td>0.01 <b>(-21.12%)</b></td><td>0.01 <b>(-43.17%)</b></td><td>0.01 <b>(-34.79%)</b></td><td>0.01 <b>(+122.85%)</b></td><td>594.50 <b>(+53.34%)</b></td><td>422.10 <b>(+47.53%)</b></td><td>470.80 <b>(+75.93%)</b></td><td>190.30 (-16.61%)</td><td>173.90 <b>(+182.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>387.70 (n/a)</td><td>286.12 (n/a)</td><td>267.60 (n/a)</td><td>228.20 (n/a)</td><td>61.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+4.35%)</td><td>0.02 (+4.53%)</td><td>0.01 (-10.47%)</td><td>0.01 <b>(+28.52%)</b></td><td>0.01 (-0.90%)</td><td>472.80 <b>(-22.20%)</b></td><td>347.36 (-7.48%)</td><td>351.10 (+11.71%)</td><td>209.20 (-4.17%)</td><td>122.88 <b>(-25.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.70 (n/a)</td><td>375.46 (n/a)</td><td>314.30 (n/a)</td><td>218.30 (n/a)</td><td>163.85 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(-22.12%)</b></td><td>0.01 (-8.73%)</td><td>0.01 (+0.30%)</td><td>0.01 (+15.58%)</td><td>0.00 <b>(-37.09%)</b></td><td>524.70 (-13.47%)</td><td>340.20 (+1.08%)</td><td>290.00 (-0.31%)</td><td>242.50 <b>(+28.44%)</b></td><td>112.41 <b>(-30.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.40 (n/a)</td><td>336.56 (n/a)</td><td>290.90 (n/a)</td><td>188.80 (n/a)</td><td>162.47 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-6.11%)</td><td>0.02 (+16.73%)</td><td>0.02 <b>(+34.35%)</b></td><td>0.01 (-10.63%)</td><td>0.00 (-7.48%)</td><td>587.90 (+11.90%)</td><td>363.94 (-13.69%)</td><td>340.40 <b>(-25.56%)</b></td><td>256.30 (+6.53%)</td><td>131.66 <b>(+20.79%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.40 (n/a)</td><td>421.68 (n/a)</td><td>457.30 (n/a)</td><td>240.60 (n/a)</td><td>108.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+4.15%)</td><td>0.01 (+7.09%)</td><td>0.01 <b>(+35.43%)</b></td><td>0.01 (+17.40%)</td><td>0.00 (-12.04%)</td><td>497.30 (-14.82%)</td><td>373.96 (-9.34%)</td><td>335.40 <b>(-26.16%)</b></td><td>247.30 (-4.00%)</td><td>104.39 <b>(-22.87%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.80 (n/a)</td><td>412.50 (n/a)</td><td>454.20 (n/a)</td><td>257.60 (n/a)</td><td>135.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 <b>(-29.98%)</b></td><td>0.01 (-15.45%)</td><td>0.01 (+5.69%)</td><td>0.01 (-18.13%)</td><td>0.00 <b>(-42.79%)</b></td><td>797.20 <b>(+22.14%)</b></td><td>496.66 (+11.13%)</td><td>443.40 (-5.38%)</td><td>344.40 <b>(+42.79%)</b></td><td>183.27 (+1.08%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>652.70 (n/a)</td><td>446.92 (n/a)</td><td>468.60 (n/a)</td><td>241.20 (n/a)</td><td>181.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-15.82%)</td><td>0.01 (-16.10%)</td><td>0.01 <b>(-24.23%)</b></td><td>0.01 (-5.00%)</td><td>0.00 (-16.15%)</td><td>646.50 (+5.28%)</td><td>466.24 (+17.83%)</td><td>524.80 <b>(+31.96%)</b></td><td>299.20 (+18.82%)</td><td>154.14 (+3.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.10 (n/a)</td><td>395.68 (n/a)</td><td>397.70 (n/a)</td><td>251.80 (n/a)</td><td>148.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(-24.17%)</b></td><td>0.01 (-6.02%)</td><td>0.01 <b>(+37.39%)</b></td><td>0.01 (+9.08%)</td><td>0.00 <b>(-37.64%)</b></td><td>546.90 (-8.32%)</td><td>380.08 (-0.81%)</td><td>312.90 <b>(-27.22%)</b></td><td>279.00 <b>(+31.91%)</b></td><td>122.06 <b>(-22.00%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.50 (n/a)</td><td>383.20 (n/a)</td><td>429.90 (n/a)</td><td>211.50 (n/a)</td><td>156.50 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 <b>(+29.38%)</b></td><td>0.01 (+12.39%)</td><td>0.01 (-3.52%)</td><td>0.01 (+1.61%)</td><td>0.00 <b>(+130.87%)</b></td><td>617.90 (-1.59%)</td><td>479.42 (-6.98%)</td><td>536.20 (+3.65%)</td><td>335.00 <b>(-22.72%)</b></td><td>125.21 <b>(+69.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.90 (n/a)</td><td>515.40 (n/a)</td><td>517.30 (n/a)</td><td>433.50 (n/a)</td><td>73.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(+22.68%)</b></td><td>0.02 (-8.47%)</td><td>0.02 <b>(-35.09%)</b></td><td>0.01 (-7.08%)</td><td>0.01 <b>(+46.23%)</b></td><td>599.50 (+7.61%)</td><td>430.54 (+18.26%)</td><td>483.10 <b>(+54.05%)</b></td><td>207.60 (-18.49%)</td><td>174.23 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>364.06 (n/a)</td><td>313.60 (n/a)</td><td>254.70 (n/a)</td><td>129.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(-29.76%)</b></td><td>0.03 <b>(-25.64%)</b></td><td>0.03 (-12.04%)</td><td>0.02 (-14.79%)</td><td>0.01 <b>(-42.17%)</b></td><td>660.40 (+17.36%)</td><td>511.70 <b>(+28.48%)</b></td><td>472.80 (+13.68%)</td><td>324.70 <b>(+42.35%)</b></td><td>135.81 (-1.45%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>562.70 (n/a)</td><td>398.28 (n/a)</td><td>415.90 (n/a)</td><td>228.10 (n/a)</td><td>137.80 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(+51.96%)</b></td><td>0.03 <b>(+44.79%)</b></td><td>0.03 <b>(+59.92%)</b></td><td>0.02 (+15.19%)</td><td>0.01 <b>(+67.06%)</b></td><td>484.20 (-13.19%)</td><td>315.12 <b>(-28.35%)</b></td><td>313.90 <b>(-37.46%)</b></td><td>180.50 <b>(-34.20%)</b></td><td>117.13 (-6.73%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>439.78 (n/a)</td><td>501.90 (n/a)</td><td>274.30 (n/a)</td><td>125.58 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-12.24%)</td><td>0.03 <b>(-31.83%)</b></td><td>0.02 <b>(-53.80%)</b></td><td>0.02 (-3.00%)</td><td>0.01 (-4.95%)</td><td>653.40 (+3.09%)</td><td>463.64 <b>(+45.99%)</b></td><td>527.90 <b>(+116.44%)</b></td><td>228.30 (+13.92%)</td><td>181.95 (+1.97%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>633.80 (n/a)</td><td>317.58 (n/a)</td><td>243.90 (n/a)</td><td>200.40 (n/a)</td><td>178.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-2.21%)</td><td>0.03 (+14.61%)</td><td>0.03 <b>(+37.19%)</b></td><td>0.01 (+3.37%)</td><td>0.01 (-5.95%)</td><td>601.10 (-3.27%)</td><td>356.38 (-13.76%)</td><td>297.90 <b>(-27.11%)</b></td><td>235.30 (+2.26%)</td><td>148.63 (-4.81%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.40 (n/a)</td><td>413.22 (n/a)</td><td>408.70 (n/a)</td><td>230.10 (n/a)</td><td>156.15 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-17.88%)</td><td>0.02 <b>(-30.06%)</b></td><td>0.02 <b>(-46.00%)</b></td><td>0.02 (-9.76%)</td><td>0.01 <b>(-32.26%)</b></td><td>580.80 (+10.82%)</td><td>460.78 <b>(+34.39%)</b></td><td>457.70 <b>(+85.23%)</b></td><td>255.70 <b>(+21.76%)</b></td><td>128.13 (-15.70%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.10 (n/a)</td><td>342.86 (n/a)</td><td>247.10 (n/a)</td><td>210.00 (n/a)</td><td>152.00 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (+7.75%)</td><td>0.02 (+11.20%)</td><td>0.02 <b>(+28.17%)</b></td><td>0.02 (+18.66%)</td><td>0.01 (+2.83%)</td><td>481.50 (-15.73%)</td><td>365.16 (-10.94%)</td><td>358.20 <b>(-21.98%)</b></td><td>247.80 (-7.19%)</td><td>113.93 (-13.73%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>410.02 (n/a)</td><td>459.10 (n/a)</td><td>267.00 (n/a)</td><td>132.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 (-7.58%)</td><td>0.02 (-14.14%)</td><td>0.02 (-12.26%)</td><td>0.01 <b>(-23.30%)</b></td><td>0.01 (-0.30%)</td><td>666.00 <b>(+30.38%)</b></td><td>451.28 <b>(+21.39%)</b></td><td>496.80 (+13.97%)</td><td>238.10 (+8.18%)</td><td>183.35 <b>(+41.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>371.76 (n/a)</td><td>435.90 (n/a)</td><td>220.10 (n/a)</td><td>129.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.03 (-13.24%)</td><td>0.02 (-8.53%)</td><td>0.02 (+7.27%)</td><td>0.02 (+11.44%)</td><td>0.01 <b>(-35.71%)</b></td><td>524.80 (-10.28%)</td><td>425.00 (+2.09%)</td><td>431.80 (-6.78%)</td><td>270.80 (+15.23%)</td><td>95.75 <b>(-35.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>416.30 (n/a)</td><td>463.20 (n/a)</td><td>235.00 (n/a)</td><td>148.56 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.04 <b>(+36.09%)</b></td><td>0.03 <b>(+51.00%)</b></td><td>0.02 (+17.53%)</td><td>0.02 <b>(+202.59%)</b></td><td>0.01 (+18.49%)</td><td>598.20 <b>(-66.95%)</b></td><td>391.50 <b>(-46.82%)</b></td><td>420.60 (-14.91%)</td><td>248.10 <b>(-26.51%)</b></td><td>144.34 <b>(-76.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1810.20 (n/a)</td><td>736.24 (n/a)</td><td>494.30 (n/a)</td><td>337.60 (n/a)</td><td>606.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(-26.12%)</b></td><td>0.02 <b>(-25.29%)</b></td><td>0.01 <b>(-20.26%)</b></td><td>0.01 <b>(-63.24%)</b></td><td>0.01 (+6.24%)</td><td>1345.00 <b>(+172.05%)</b></td><td>651.52 <b>(+57.59%)</b></td><td>577.30 <b>(+25.39%)</b></td><td>345.00 <b>(+35.35%)</b></td><td>402.57 <b>(+318.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.40 (n/a)</td><td>413.42 (n/a)</td><td>460.40 (n/a)</td><td>254.90 (n/a)</td><td>96.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.06 (-0.83%)</td><td>0.06 (+18.13%)</td><td>0.06 <b>(+45.82%)</b></td><td>0.04 (+8.43%)</td><td>0.01 (-12.83%)</td><td>461.90 (-7.77%)</td><td>308.94 (-16.93%)</td><td>260.80 <b>(-31.40%)</b></td><td>256.60 (+0.83%)</td><td>88.29 (-17.44%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>371.92 (n/a)</td><td>380.20 (n/a)</td><td>254.50 (n/a)</td><td>106.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 <b>(-28.91%)</b></td><td>0.07 (-15.64%)</td><td>0.07 (-7.18%)</td><td>0.05 (-3.79%)</td><td>0.02 <b>(-40.05%)</b></td><td>520.20 (+3.94%)</td><td>388.10 (+12.66%)</td><td>328.10 (+7.75%)</td><td>290.90 <b>(+40.67%)</b></td><td>109.48 (-13.87%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>500.50 (n/a)</td><td>344.50 (n/a)</td><td>304.50 (n/a)</td><td>206.80 (n/a)</td><td>127.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-4.68%)</td><td>0.05 (+0.23%)</td><td>0.05 (-8.03%)</td><td>0.04 <b>(+25.65%)</b></td><td>0.01 <b>(-38.78%)</b></td><td>438.40 <b>(-20.42%)</b></td><td>319.02 (-7.20%)</td><td>299.20 (+8.72%)</td><td>248.80 (+4.89%)</td><td>73.78 <b>(-46.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.90 (n/a)</td><td>343.76 (n/a)</td><td>275.20 (n/a)</td><td>237.20 (n/a)</td><td>136.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 <b>(+32.63%)</b></td><td>0.06 (-1.43%)</td><td>0.05 <b>(-36.28%)</b></td><td>0.04 <b>(+126.02%)</b></td><td>0.03 (+10.95%)</td><td>467.70 <b>(-55.75%)</b></td><td>366.98 (-14.40%)</td><td>437.40 <b>(+56.94%)</b></td><td>186.20 <b>(-24.58%)</b></td><td>127.68 <b>(-63.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1057.00 (n/a)</td><td>428.70 (n/a)</td><td>278.70 (n/a)</td><td>246.90 (n/a)</td><td>351.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-0.95%)</td><td>0.05 <b>(+24.39%)</b></td><td>0.04 (+12.99%)</td><td>0.03 <b>(+97.21%)</b></td><td>0.02 (-17.28%)</td><td>573.50 <b>(-49.29%)</b></td><td>377.36 <b>(-31.43%)</b></td><td>398.30 (-11.51%)</td><td>241.50 (+0.92%)</td><td>133.96 <b>(-61.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1131.00 (n/a)</td><td>550.34 (n/a)</td><td>450.10 (n/a)</td><td>239.30 (n/a)</td><td>345.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-14.32%)</td><td>0.05 (-9.73%)</td><td>0.04 (-9.60%)</td><td>0.04 (-9.23%)</td><td>0.02 (-19.93%)</td><td>583.20 (+10.16%)</td><td>478.06 (+9.21%)</td><td>529.80 (+10.61%)</td><td>278.70 (+16.71%)</td><td>120.62 (+3.38%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>529.40 (n/a)</td><td>437.76 (n/a)</td><td>479.00 (n/a)</td><td>238.80 (n/a)</td><td>116.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-19.47%)</td><td>0.05 (-1.72%)</td><td>0.05 <b>(+35.17%)</b></td><td>0.03 (+6.74%)</td><td>0.02 <b>(-27.11%)</b></td><td>549.60 (-6.32%)</td><td>380.56 (-2.13%)</td><td>312.10 <b>(-26.01%)</b></td><td>235.30 <b>(+24.17%)</b></td><td>137.85 (-6.25%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.70 (n/a)</td><td>388.86 (n/a)</td><td>421.80 (n/a)</td><td>189.50 (n/a)</td><td>147.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-31.75%)</b></td><td>0.04 <b>(-20.00%)</b></td><td>0.04 <b>(-30.38%)</b></td><td>0.04 <b>(+21.55%)</b></td><td>0.01 <b>(-67.20%)</b></td><td>471.90 (-17.72%)</td><td>417.00 (+14.41%)</td><td>437.30 <b>(+43.66%)</b></td><td>357.10 <b>(+46.53%)</b></td><td>54.15 <b>(-60.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.50 (n/a)</td><td>364.48 (n/a)</td><td>304.40 (n/a)</td><td>243.70 (n/a)</td><td>138.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-35.01%)</b></td><td>0.03 (-18.01%)</td><td>0.03 (-2.06%)</td><td>0.03 (-5.48%)</td><td>0.01 <b>(-51.22%)</b></td><td>627.50 (+5.80%)</td><td>510.26 (+9.79%)</td><td>551.80 (+2.11%)</td><td>298.00 <b>(+53.85%)</b></td><td>131.08 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>464.74 (n/a)</td><td>540.40 (n/a)</td><td>193.70 (n/a)</td><td>168.41 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+13.71%)</td><td>0.05 (-15.85%)</td><td>0.04 <b>(-32.68%)</b></td><td>0.03 (-13.37%)</td><td>0.02 <b>(+25.14%)</b></td><td>604.60 (+15.43%)</td><td>438.66 <b>(+21.76%)</b></td><td>447.00 <b>(+48.55%)</b></td><td>258.20 (-12.06%)</td><td>122.76 <b>(+22.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>523.80 (n/a)</td><td>360.28 (n/a)</td><td>300.90 (n/a)</td><td>293.60 (n/a)</td><td>99.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 <b>(+28.81%)</b></td><td>0.04 (-6.12%)</td><td>0.04 (+2.10%)</td><td>0.01 <b>(-67.55%)</b></td><td>0.02 <b>(+77.76%)</b></td><td>1885.10 <b>(+208.17%)</b></td><td>712.54 <b>(+53.63%)</b></td><td>467.20 (-2.05%)</td><td>248.10 <b>(-22.37%)</b></td><td>663.27 <b>(+393.87%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>611.70 (n/a)</td><td>463.80 (n/a)</td><td>477.00 (n/a)</td><td>319.60 (n/a)</td><td>134.30 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (+19.57%)</td><td>0.12 <b>(+29.76%)</b></td><td>0.10 <b>(+34.17%)</b></td><td>0.06 (+5.03%)</td><td>0.04 <b>(+38.35%)</b></td><td>563.20 (-4.78%)</td><td>322.42 (-19.51%)</td><td>319.80 <b>(-25.45%)</b></td><td>199.60 (-16.38%)</td><td>147.14 (+8.46%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>591.50 (n/a)</td><td>400.56 (n/a)</td><td>429.00 (n/a)</td><td>238.70 (n/a)</td><td>135.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (-0.60%)</td><td>0.10 (+17.66%)</td><td>0.12 <b>(+81.40%)</b></td><td>0.06 (+8.63%)</td><td>0.04 (+8.82%)</td><td>593.00 (-7.93%)</td><td>372.34 (-13.50%)</td><td>264.70 <b>(-44.89%)</b></td><td>239.90 (+0.63%)</td><td>166.90 (+2.61%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>644.10 (n/a)</td><td>430.46 (n/a)</td><td>480.30 (n/a)</td><td>238.40 (n/a)</td><td>162.65 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 <b>(-23.91%)</b></td><td>0.10 (-19.92%)</td><td>0.09 <b>(-44.82%)</b></td><td>0.08 <b>(+21.76%)</b></td><td>0.03 <b>(-53.44%)</b></td><td>515.50 (-17.87%)</td><td>411.72 (+5.39%)</td><td>453.20 <b>(+81.21%)</b></td><td>283.70 <b>(+31.46%)</b></td><td>99.86 <b>(-53.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>627.70 (n/a)</td><td>390.66 (n/a)</td><td>250.10 (n/a)</td><td>215.80 (n/a)</td><td>212.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (-8.40%)</td><td>0.07 (-14.39%)</td><td>0.07 (-18.47%)</td><td>0.06 (+10.85%)</td><td>0.02 <b>(-34.93%)</b></td><td>560.40 (-9.79%)</td><td>460.58 (+9.01%)</td><td>473.90 <b>(+22.64%)</b></td><td>293.30 (+9.16%)</td><td>100.16 <b>(-38.12%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>621.20 (n/a)</td><td>422.50 (n/a)</td><td>386.40 (n/a)</td><td>268.70 (n/a)</td><td>161.87 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (-7.75%)</td><td>0.10 (-12.98%)</td><td>0.08 (-16.62%)</td><td>0.07 <b>(-21.61%)</b></td><td>0.02 (+17.05%)</td><td>565.10 <b>(+27.56%)</b></td><td>449.54 (+17.47%)</td><td>500.50 (+19.91%)</td><td>313.70 (+8.40%)</td><td>104.70 <b>(+59.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>443.00 (n/a)</td><td>382.70 (n/a)</td><td>417.40 (n/a)</td><td>289.40 (n/a)</td><td>65.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 <b>(-42.61%)</b></td><td>0.06 <b>(-27.07%)</b></td><td>0.06 (-11.12%)</td><td>0.04 (-19.65%)</td><td>0.01 <b>(-64.87%)</b></td><td>731.30 <b>(+24.46%)</b></td><td>571.10 <b>(+29.03%)</b></td><td>563.70 (+12.51%)</td><td>460.50 <b>(+74.23%)</b></td><td>102.74 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.60 (n/a)</td><td>442.62 (n/a)</td><td>501.00 (n/a)</td><td>264.30 (n/a)</td><td>131.75 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 <b>(-28.10%)</b></td><td>0.08 (-10.97%)</td><td>0.08 (-2.11%)</td><td>0.06 (+0.56%)</td><td>0.03 <b>(-44.59%)</b></td><td>605.10 (-0.56%)</td><td>477.42 (+4.22%)</td><td>491.40 (+2.16%)</td><td>291.10 <b>(+39.08%)</b></td><td>122.16 (-19.26%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>608.50 (n/a)</td><td>458.08 (n/a)</td><td>481.00 (n/a)</td><td>209.30 (n/a)</td><td>151.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (+4.75%)</td><td>0.08 (+13.38%)</td><td>0.08 (+14.35%)</td><td>0.06 (+11.77%)</td><td>0.03 (+5.12%)</td><td>577.50 (-10.53%)</td><td>418.38 (-12.51%)</td><td>435.50 (-12.55%)</td><td>284.10 (-4.54%)</td><td>127.36 (-14.36%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>645.50 (n/a)</td><td>478.20 (n/a)</td><td>498.00 (n/a)</td><td>297.60 (n/a)</td><td>148.72 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 <b>(+43.22%)</b></td><td>0.11 (+9.81%)</td><td>0.10 <b>(+32.76%)</b></td><td>0.05 (-19.39%)</td><td>0.08 <b>(+74.38%)</b></td><td>695.50 <b>(+24.04%)</b></td><td>431.26 (+6.11%)</td><td>358.70 <b>(-24.67%)</b></td><td>152.40 <b>(-30.19%)</b></td><td>215.81 <b>(+50.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>560.70 (n/a)</td><td>406.44 (n/a)</td><td>476.20 (n/a)</td><td>218.30 (n/a)</td><td>143.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (-12.99%)</td><td>0.08 (+12.04%)</td><td>0.08 (+9.72%)</td><td>0.06 <b>(+30.50%)</b></td><td>0.02 <b>(-41.50%)</b></td><td>516.80 <b>(-23.38%)</b></td><td>419.70 (-16.67%)</td><td>421.80 (-8.86%)</td><td>332.80 (+14.92%)</td><td>80.08 <b>(-51.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.50 (n/a)</td><td>503.68 (n/a)</td><td>462.80 (n/a)</td><td>289.60 (n/a)</td><td>165.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (-1.05%)</td><td>0.06 (-16.31%)</td><td>0.07 (+1.97%)</td><td>0.01 <b>(-73.85%)</b></td><td>0.03 <b>(+75.01%)</b></td><td>2000.40 <b>(+282.34%)</b></td><td>658.42 <b>(+101.59%)</b></td><td>287.90 (-1.94%)</td><td>244.20 (+1.08%)</td><td>756.11 <b>(+571.37%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.20 (n/a)</td><td>326.62 (n/a)</td><td>293.60 (n/a)</td><td>241.60 (n/a)</td><td>112.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-14.81%)</td><td>0.06 (-7.96%)</td><td>0.05 <b>(-26.84%)</b></td><td>0.04 <b>(+25.43%)</b></td><td>0.01 <b>(-44.44%)</b></td><td>478.90 <b>(-20.26%)</b></td><td>384.18 (-2.67%)</td><td>427.70 <b>(+36.69%)</b></td><td>279.90 (+17.36%)</td><td>87.78 <b>(-50.44%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.60 (n/a)</td><td>394.70 (n/a)</td><td>312.90 (n/a)</td><td>238.50 (n/a)</td><td>177.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+4.28%)</td><td>0.04 (+3.30%)</td><td>0.04 (+18.28%)</td><td>0.01 <b>(+28.05%)</b></td><td>0.02 (-4.78%)</td><td>1896.30 <b>(-21.91%)</b></td><td>740.14 (-14.43%)</td><td>507.30 (-15.45%)</td><td>285.40 (-4.10%)</td><td>653.37 <b>(-26.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2428.20 (n/a)</td><td>865.00 (n/a)</td><td>600.00 (n/a)</td><td>297.60 (n/a)</td><td>884.04 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 <b>(-23.72%)</b></td><td>0.06 (+2.39%)</td><td>0.07 <b>(+53.50%)</b></td><td>0.02 <b>(-28.07%)</b></td><td>0.02 <b>(-27.99%)</b></td><td>1032.80 <b>(+39.02%)</b></td><td>448.30 (-0.74%)</td><td>299.80 <b>(-34.85%)</b></td><td>298.80 <b>(+31.11%)</b></td><td>326.78 <b>(+45.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>742.90 (n/a)</td><td>451.66 (n/a)</td><td>460.20 (n/a)</td><td>227.90 (n/a)</td><td>225.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-1.84%)</td><td>0.05 (+3.80%)</td><td>0.05 (+7.10%)</td><td>0.04 (+1.21%)</td><td>0.01 (-8.37%)</td><td>561.40 (-1.20%)</td><td>420.78 (-4.64%)</td><td>429.80 (-6.63%)</td><td>280.80 (+1.85%)</td><td>106.59 (-7.96%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>568.20 (n/a)</td><td>441.24 (n/a)</td><td>460.30 (n/a)</td><td>275.70 (n/a)</td><td>115.82 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 <b>(+71.53%)</b></td><td>0.06 <b>(+56.41%)</b></td><td>0.04 (+19.77%)</td><td>0.03 <b>(+75.89%)</b></td><td>0.03 <b>(+104.40%)</b></td><td>606.20 <b>(-43.14%)</b></td><td>432.12 <b>(-32.85%)</b></td><td>526.90 (-16.50%)</td><td>212.50 <b>(-41.70%)</b></td><td>174.25 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1066.20 (n/a)</td><td>643.52 (n/a)</td><td>631.00 (n/a)</td><td>364.50 (n/a)</td><td>260.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 <b>(+24.96%)</b></td><td>0.09 <b>(+35.49%)</b></td><td>0.09 (+18.37%)</td><td>0.08 <b>(+77.51%)</b></td><td>0.01 <b>(-47.15%)</b></td><td>323.50 <b>(-43.66%)</b></td><td>277.46 <b>(-31.96%)</b></td><td>276.00 (-15.54%)</td><td>232.40 (-19.97%)</td><td>33.81 <b>(-76.48%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>574.20 (n/a)</td><td>407.78 (n/a)</td><td>326.80 (n/a)</td><td>290.40 (n/a)</td><td>143.77 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 <b>(-29.83%)</b></td><td>0.05 <b>(-31.13%)</b></td><td>0.05 <b>(-31.84%)</b></td><td>0.04 (-8.43%)</td><td>0.01 <b>(-48.09%)</b></td><td>635.90 (+9.20%)</td><td>515.94 <b>(+37.64%)</b></td><td>488.60 <b>(+46.73%)</b></td><td>357.00 <b>(+42.51%)</b></td><td>112.74 (-17.53%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.30 (n/a)</td><td>374.84 (n/a)</td><td>333.00 (n/a)</td><td>250.50 (n/a)</td><td>136.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 <b>(+29.13%)</b></td><td>0.07 <b>(+21.29%)</b></td><td>0.05 <b>(+22.51%)</b></td><td>0.02 <b>(+64.85%)</b></td><td>0.04 <b>(+20.41%)</b></td><td>1104.40 <b>(-39.34%)</b></td><td>526.58 <b>(-27.36%)</b></td><td>493.80 (-18.37%)</td><td>188.00 <b>(-22.54%)</b></td><td>353.64 <b>(-44.46%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1820.60 (n/a)</td><td>724.94 (n/a)</td><td>604.90 (n/a)</td><td>242.70 (n/a)</td><td>636.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 <b>(+20.81%)</b></td><td>0.06 (-6.71%)</td><td>0.05 <b>(-23.72%)</b></td><td>0.01 <b>(-67.71%)</b></td><td>0.04 <b>(+94.97%)</b></td><td>1831.10 <b>(+209.67%)</b></td><td>694.68 <b>(+67.49%)</b></td><td>501.50 <b>(+31.11%)</b></td><td>220.20 (-17.22%)</td><td>656.89 <b>(+405.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.30 (n/a)</td><td>414.76 (n/a)</td><td>382.50 (n/a)</td><td>266.00 (n/a)</td><td>129.94 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 <b>(+38.81%)</b></td><td>0.08 (+3.08%)</td><td>0.06 <b>(-22.48%)</b></td><td>0.05 (+15.75%)</td><td>0.04 <b>(+51.28%)</b></td><td>461.40 (-13.60%)</td><td>364.20 (+0.09%)</td><td>416.00 <b>(+28.99%)</b></td><td>172.90 <b>(-27.96%)</b></td><td>114.39 (-10.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>534.00 (n/a)</td><td>363.86 (n/a)</td><td>322.50 (n/a)</td><td>240.00 (n/a)</td><td>128.23 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 (+0.42%)</td><td>0.07 (-3.92%)</td><td>0.05 <b>(-22.95%)</b></td><td>0.04 (-3.97%)</td><td>0.03 (+19.31%)</td><td>574.30 (+4.13%)</td><td>423.28 (+7.97%)</td><td>497.40 <b>(+29.77%)</b></td><td>253.60 (-0.43%)</td><td>152.29 (+19.93%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.50 (n/a)</td><td>392.02 (n/a)</td><td>383.30 (n/a)</td><td>254.70 (n/a)</td><td>126.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-8.70%)</td><td>0.05 (-8.29%)</td><td>0.04 (-2.90%)</td><td>0.03 <b>(-20.21%)</b></td><td>0.01 (-2.89%)</td><td>601.30 <b>(+25.32%)</b></td><td>437.46 (+10.74%)</td><td>413.70 (+2.99%)</td><td>269.80 (+9.54%)</td><td>122.94 <b>(+35.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>479.80 (n/a)</td><td>395.04 (n/a)</td><td>401.70 (n/a)</td><td>246.30 (n/a)</td><td>90.68 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 (+11.13%)</td><td>0.06 (-7.49%)</td><td>0.05 <b>(-23.93%)</b></td><td>0.04 <b>(+21.48%)</b></td><td>0.02 (+7.29%)</td><td>486.30 (-17.69%)</td><td>354.50 (+6.09%)</td><td>349.50 <b>(+31.44%)</b></td><td>218.20 (-10.02%)</td><td>111.52 <b>(-23.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.80 (n/a)</td><td>334.16 (n/a)</td><td>265.90 (n/a)</td><td>242.50 (n/a)</td><td>145.55 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (-4.92%)</td><td>0.04 <b>(-32.79%)</b></td><td>0.04 <b>(-48.12%)</b></td><td>0.03 <b>(-25.72%)</b></td><td>0.02 <b>(+23.96%)</b></td><td>575.00 <b>(+34.63%)</b></td><td>455.32 <b>(+54.82%)</b></td><td>494.70 <b>(+92.79%)</b></td><td>254.30 (+5.21%)</td><td>122.78 <b>(+60.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>427.10 (n/a)</td><td>294.10 (n/a)</td><td>256.60 (n/a)</td><td>241.70 (n/a)</td><td>76.29 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 (+12.35%)</td><td>0.06 (+3.11%)</td><td>0.05 (-17.17%)</td><td>0.04 (+18.85%)</td><td>0.02 (-5.63%)</td><td>501.00 (-15.85%)</td><td>356.68 (-7.43%)</td><td>348.10 <b>(+20.74%)</b></td><td>214.90 (-10.98%)</td><td>109.91 <b>(-31.89%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.40 (n/a)</td><td>385.30 (n/a)</td><td>288.30 (n/a)</td><td>241.40 (n/a)</td><td>161.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+1.94%)</td><td>0.06 (+6.67%)</td><td>0.07 (+18.64%)</td><td>0.03 (+13.14%)</td><td>0.02 (-5.44%)</td><td>547.60 (-11.61%)</td><td>368.68 (-8.65%)</td><td>280.70 (-15.71%)</td><td>246.00 (-1.91%)</td><td>139.92 (-16.75%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>619.50 (n/a)</td><td>403.58 (n/a)</td><td>333.00 (n/a)</td><td>250.80 (n/a)</td><td>168.08 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.05 <b>(-30.88%)</b></td><td>0.04 (-9.52%)</td><td>0.03 (-6.23%)</td><td>0.03 (+4.63%)</td><td>0.01 <b>(-52.10%)</b></td><td>574.30 (-4.41%)</td><td>498.66 (+4.71%)</td><td>549.40 (+6.64%)</td><td>390.30 <b>(+44.66%)</b></td><td>90.11 <b>(-31.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>600.80 (n/a)</td><td>476.22 (n/a)</td><td>515.20 (n/a)</td><td>269.80 (n/a)</td><td>131.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.36 (+1.31%)</td><td>0.24 <b>(-22.13%)</b></td><td>0.23 <b>(-32.52%)</b></td><td>0.15 <b>(-20.86%)</b></td><td>0.09 <b>(+31.38%)</b></td><td>673.60 <b>(+26.36%)</b></td><td>459.66 <b>(+36.56%)</b></td><td>432.70 <b>(+48.18%)</b></td><td>276.80 (-1.32%)</td><td>176.48 <b>(+60.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>533.10 (n/a)</td><td>336.60 (n/a)</td><td>292.00 (n/a)</td><td>280.50 (n/a)</td><td>109.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.36 (-2.58%)</td><td>0.30 (+5.92%)</td><td>0.35 <b>(+21.62%)</b></td><td>0.19 (-12.72%)</td><td>0.08 <b>(+30.81%)</b></td><td>521.70 (+14.58%)</td><td>346.34 (-2.67%)</td><td>280.50 (-17.79%)</td><td>274.10 (+2.66%)</td><td>107.17 <b>(+49.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>455.30 (n/a)</td><td>355.84 (n/a)</td><td>341.20 (n/a)</td><td>267.00 (n/a)</td><td>71.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.34 (+14.03%)</td><td>0.23 (-6.00%)</td><td>0.21 (-15.19%)</td><td>0.05 <b>(-72.08%)</b></td><td>0.12 <b>(+144.58%)</b></td><td>1829.30 <b>(+258.12%)</b></td><td>678.44 <b>(+60.66%)</b></td><td>475.10 (+17.92%)</td><td>285.20 (-12.30%)</td><td>651.10 <b>(+665.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>510.80 (n/a)</td><td>422.28 (n/a)</td><td>402.90 (n/a)</td><td>325.20 (n/a)</td><td>85.09 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.32 (-4.78%)</td><td>0.24 (+5.25%)</td><td>0.26 (+8.80%)</td><td>0.12 (-5.19%)</td><td>0.08 <b>(-22.22%)</b></td><td>624.80 (+5.49%)</td><td>340.38 (-8.73%)</td><td>283.50 (-8.10%)</td><td>229.30 (+4.99%)</td><td>160.68 (-5.28%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>592.30 (n/a)</td><td>372.94 (n/a)</td><td>308.50 (n/a)</td><td>218.40 (n/a)</td><td>169.63 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.31 (+3.99%)</td><td>0.19 <b>(-23.07%)</b></td><td>0.15 <b>(-42.36%)</b></td><td>0.07 <b>(-59.32%)</b></td><td>0.11 <b>(+100.77%)</b></td><td>1108.70 <b>(+145.78%)</b></td><td>521.10 <b>(+69.51%)</b></td><td>485.10 <b>(+73.50%)</b></td><td>234.50 (-3.85%)</td><td>353.96 <b>(+328.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>451.10 (n/a)</td><td>307.42 (n/a)</td><td>279.60 (n/a)</td><td>243.90 (n/a)</td><td>82.66 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.30 (-2.95%)</td><td>0.22 <b>(+27.75%)</b></td><td>0.20 <b>(+36.18%)</b></td><td>0.10 <b>(+152.84%)</b></td><td>0.08 (-18.59%)</td><td>722.10 <b>(-60.45%)</b></td><td>396.62 <b>(-42.46%)</b></td><td>368.00 <b>(-26.56%)</b></td><td>247.90 (+3.03%)</td><td>192.44 <b>(-70.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1825.60 (n/a)</td><td>689.28 (n/a)</td><td>501.10 (n/a)</td><td>240.60 (n/a)</td><td>645.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 <b>(+28.41%)</b></td><td>0.11 (+7.17%)</td><td>0.08 (-19.39%)</td><td>0.07 (+1.36%)</td><td>0.04 <b>(+58.53%)</b></td><td>540.40 (-1.33%)</td><td>393.24 (-1.32%)</td><td>447.10 <b>(+24.06%)</b></td><td>224.40 <b>(-22.14%)</b></td><td>140.18 <b>(+20.86%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>547.70 (n/a)</td><td>398.50 (n/a)</td><td>360.40 (n/a)</td><td>288.20 (n/a)</td><td>115.99 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 <b>(+21.43%)</b></td><td>0.08 (-0.43%)</td><td>0.07 (-3.75%)</td><td>0.05 (-16.19%)</td><td>0.04 <b>(+36.66%)</b></td><td>750.50 (+19.32%)</td><td>503.52 (+5.82%)</td><td>498.50 (+3.90%)</td><td>244.20 (-17.64%)</td><td>189.26 <b>(+24.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>629.00 (n/a)</td><td>475.84 (n/a)</td><td>479.80 (n/a)</td><td>296.50 (n/a)</td><td>152.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (-19.86%)</td><td>0.11 (-9.51%)</td><td>0.12 (-2.70%)</td><td>0.06 (-10.14%)</td><td>0.03 <b>(-37.27%)</b></td><td>573.00 (+11.28%)</td><td>367.68 (+4.60%)</td><td>303.70 (+2.77%)</td><td>278.60 <b>(+24.76%)</b></td><td>121.52 (-13.33%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>514.90 (n/a)</td><td>351.50 (n/a)</td><td>295.50 (n/a)</td><td>223.30 (n/a)</td><td>140.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.12 (-18.32%)</td><td>0.09 (+2.99%)</td><td>0.09 (+17.79%)</td><td>0.06 (-0.48%)</td><td>0.03 <b>(-28.47%)</b></td><td>596.30 (+0.49%)</td><td>426.28 (-6.86%)</td><td>431.40 (-15.10%)</td><td>303.80 <b>(+22.40%)</b></td><td>122.36 (-16.84%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>593.40 (n/a)</td><td>457.68 (n/a)</td><td>508.10 (n/a)</td><td>248.20 (n/a)</td><td>147.14 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.08 <b>(-27.01%)</b></td><td>0.06 (-19.12%)</td><td>0.07 (-1.80%)</td><td>0.04 <b>(-34.78%)</b></td><td>0.02 <b>(-26.09%)</b></td><td>1024.30 <b>(+53.32%)</b></td><td>618.14 <b>(+25.69%)</b></td><td>537.30 (+1.84%)</td><td>434.90 <b>(+37.02%)</b></td><td>232.85 <b>(+70.14%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>668.10 (n/a)</td><td>491.78 (n/a)</td><td>527.60 (n/a)</td><td>317.40 (n/a)</td><td>136.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.10 <b>(-32.51%)</b></td><td>0.08 (-7.01%)</td><td>0.07 (+3.12%)</td><td>0.06 <b>(+286.59%)</b></td><td>0.02 <b>(-64.29%)</b></td><td>629.40 <b>(-74.13%)</b></td><td>488.18 <b>(-39.61%)</b></td><td>497.50 (-3.02%)</td><td>352.60 <b>(+48.21%)</b></td><td>111.65 <b>(-87.82%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2433.20 (n/a)</td><td>808.40 (n/a)</td><td>513.00 (n/a)</td><td>237.90 (n/a)</td><td>916.74 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (-5.93%)</td><td>0.10 (-10.76%)</td><td>0.08 <b>(-24.91%)</b></td><td>0.07 (+7.45%)</td><td>0.03 (-11.24%)</td><td>602.70 (-6.93%)</td><td>453.02 (+9.84%)</td><td>508.50 <b>(+33.18%)</b></td><td>286.40 (+6.31%)</td><td>133.03 (-12.64%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>647.60 (n/a)</td><td>412.42 (n/a)</td><td>381.80 (n/a)</td><td>269.40 (n/a)</td><td>152.28 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (-4.83%)</td><td>0.12 (-14.67%)</td><td>0.14 (-14.76%)</td><td>0.09 (+0.99%)</td><td>0.03 (-2.91%)</td><td>481.40 (-0.97%)</td><td>354.48 (+17.14%)</td><td>295.80 (+17.29%)</td><td>254.50 (+5.04%)</td><td>106.23 (+2.28%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>486.10 (n/a)</td><td>302.60 (n/a)</td><td>252.20 (n/a)</td><td>242.30 (n/a)</td><td>103.86 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 (+10.34%)</td><td>0.12 (-2.96%)</td><td>0.14 (-1.69%)</td><td>0.06 <b>(-24.63%)</b></td><td>0.05 <b>(+45.98%)</b></td><td>661.20 <b>(+32.69%)</b></td><td>379.52 (+11.94%)</td><td>302.50 (+1.71%)</td><td>226.40 (-9.37%)</td><td>174.76 <b>(+76.60%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>498.30 (n/a)</td><td>339.04 (n/a)</td><td>297.40 (n/a)</td><td>249.80 (n/a)</td><td>98.96 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 (+3.48%)</td><td>0.11 (+7.60%)</td><td>0.10 (+12.91%)</td><td>0.08 <b>(+30.60%)</b></td><td>0.04 (-9.96%)</td><td>487.30 <b>(-23.44%)</b></td><td>386.38 (-10.58%)</td><td>428.10 (-11.42%)</td><td>251.40 (-3.38%)</td><td>111.13 <b>(-28.91%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>636.50 (n/a)</td><td>432.08 (n/a)</td><td>483.30 (n/a)</td><td>260.20 (n/a)</td><td>156.32 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.17 (+17.60%)</td><td>0.11 <b>(+31.63%)</b></td><td>0.11 <b>(+41.57%)</b></td><td>0.05 <b>(+33.43%)</b></td><td>0.05 <b>(+20.82%)</b></td><td>800.20 <b>(-25.05%)</b></td><td>444.94 <b>(-24.23%)</b></td><td>360.90 <b>(-29.37%)</b></td><td>245.50 (-14.96%)</td><td>221.62 <b>(-23.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1067.70 (n/a)</td><td>587.24 (n/a)</td><td>511.00 (n/a)</td><td>288.70 (n/a)</td><td>288.53 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.20 <b>(+39.46%)</b></td><td>0.11 (+6.04%)</td><td>0.07 (-12.60%)</td><td>0.06 (-10.58%)</td><td>0.06 <b>(+59.53%)</b></td><td>643.50 (+11.84%)</td><td>457.80 (+3.46%)</td><td>548.10 (+14.40%)</td><td>208.80 <b>(-28.30%)</b></td><td>190.20 <b>(+32.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>575.40 (n/a)</td><td>442.48 (n/a)</td><td>479.10 (n/a)</td><td>291.20 (n/a)</td><td>143.10 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.18 <b>(+45.93%)</b></td><td>0.09 (-5.91%)</td><td>0.06 <b>(-36.42%)</b></td><td>0.06 (+6.23%)</td><td>0.05 <b>(+65.87%)</b></td><td>628.20 (-5.86%)</td><td>479.72 (+14.14%)</td><td>537.00 <b>(+57.29%)</b></td><td>190.30 <b>(-31.47%)</b></td><td>171.33 (+1.12%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>667.30 (n/a)</td><td>420.30 (n/a)</td><td>341.40 (n/a)</td><td>277.70 (n/a)</td><td>169.43 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.14 (-4.40%)</td><td>0.11 (+7.83%)</td><td>0.12 (+13.43%)</td><td>0.06 (-13.17%)</td><td>0.03 (-9.08%)</td><td>614.60 (+15.18%)</td><td>351.82 (-7.10%)</td><td>293.10 (-11.85%)</td><td>257.50 (+4.59%)</td><td>148.49 (+11.97%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>533.60 (n/a)</td><td>378.72 (n/a)</td><td>332.50 (n/a)</td><td>246.20 (n/a)</td><td>132.62 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 <b>(-30.37%)</b></td><td>0.06 <b>(-35.69%)</b></td><td>0.08 <b>(-36.63%)</b></td><td>0.01 <b>(-75.58%)</b></td><td>0.03 (-12.51%)</td><td>2468.70 <b>(+309.47%)</b></td><td>869.96 <b>(+120.29%)</b></td><td>452.00 <b>(+57.82%)</b></td><td>389.90 <b>(+43.61%)</b></td><td>898.51 <b>(+456.57%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>602.90 (n/a)</td><td>394.92 (n/a)</td><td>286.40 (n/a)</td><td>271.50 (n/a)</td><td>161.44 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.15 (+14.56%)</td><td>0.10 (-13.51%)</td><td>0.08 <b>(-27.33%)</b></td><td>0.06 (-19.38%)</td><td>0.04 <b>(+74.06%)</b></td><td>566.10 <b>(+24.04%)</b></td><td>403.14 <b>(+23.50%)</b></td><td>416.90 <b>(+37.59%)</b></td><td>228.40 (-12.72%)</td><td>132.17 <b>(+76.10%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>456.40 (n/a)</td><td>326.42 (n/a)</td><td>303.00 (n/a)</td><td>261.70 (n/a)</td><td>75.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.22 <b>(+94.73%)</b></td><td>0.12 <b>(+90.53%)</b></td><td>0.13 <b>(+91.36%)</b></td><td>0.07 <b>(+313.77%)</b></td><td>0.06 <b>(+74.17%)</b></td><td>490.10 <b>(-75.83%)</b></td><td>335.80 <b>(-57.92%)</b></td><td>278.50 <b>(-47.74%)</b></td><td>160.00 <b>(-48.64%)</b></td><td>141.76 <b>(-79.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2028.10 (n/a)</td><td>797.94 (n/a)</td><td>532.90 (n/a)</td><td>311.50 (n/a)</td><td>697.90 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.09 <b>(-45.92%)</b></td><td>0.08 <b>(-24.06%)</b></td><td>0.08 <b>(-30.68%)</b></td><td>0.08 <b>(+42.19%)</b></td><td>0.01 <b>(-88.95%)</b></td><td>457.40 <b>(-29.66%)</b></td><td>431.98 (+8.87%)</td><td>436.70 <b>(+44.27%)</b></td><td>387.80 <b>(+84.93%)</b></td><td>26.96 <b>(-86.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>650.30 (n/a)</td><td>396.80 (n/a)</td><td>302.70 (n/a)</td><td>209.70 (n/a)</td><td>197.97 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.42 <b>(-27.54%)</b></td><td>0.30 (-10.20%)</td><td>0.28 (+1.23%)</td><td>0.23 <b>(+75.61%)</b></td><td>0.08 <b>(-53.14%)</b></td><td>566.10 <b>(-43.06%)</b></td><td>455.42 (-8.13%)</td><td>468.30 (-1.20%)</td><td>312.40 <b>(+37.99%)</b></td><td>109.43 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.17 (n/a)</td><td>994.20 (n/a)</td><td>495.74 (n/a)</td><td>474.00 (n/a)</td><td>226.40 (n/a)</td><td>298.52 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.44 (-4.75%)</td><td>0.30 <b>(+42.95%)</b></td><td>0.25 <b>(+23.35%)</b></td><td>0.22 <b>(+302.67%)</b></td><td>0.10 <b>(-41.15%)</b></td><td>600.00 <b>(-75.16%)</b></td><td>475.42 <b>(-58.57%)</b></td><td>530.80 (-18.94%)</td><td>300.20 (+4.97%)</td><td>135.33 <b>(-85.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>0.16 (n/a)</td><td>2415.90 (n/a)</td><td>1147.60 (n/a)</td><td>654.80 (n/a)</td><td>286.00 (n/a)</td><td>939.21 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.65 <b>(+44.69%)</b></td><td>0.33 (-2.67%)</td><td>0.26 (-4.85%)</td><td>0.23 (-14.42%)</td><td>0.18 <b>(+91.73%)</b></td><td>580.00 (+16.84%)</td><td>468.76 (+13.30%)</td><td>511.00 (+5.10%)</td><td>200.50 <b>(-30.89%)</b></td><td>154.74 <b>(+45.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>496.40 (n/a)</td><td>413.72 (n/a)</td><td>486.20 (n/a)</td><td>290.10 (n/a)</td><td>106.24 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-16.32%)</td><td>0.01 (-0.92%)</td><td>0.01 <b>(+30.75%)</b></td><td>0.01 (-11.35%)</td><td>0.00 <b>(-20.65%)</b></td><td>575.10 (+12.81%)</td><td>385.46 (-0.80%)</td><td>314.40 <b>(-23.52%)</b></td><td>274.20 (+19.48%)</td><td>130.95 (+2.81%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.80 (n/a)</td><td>388.58 (n/a)</td><td>411.10 (n/a)</td><td>229.50 (n/a)</td><td>127.37 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 <b>(+35.36%)</b></td><td>0.02 <b>(+25.52%)</b></td><td>0.01 (-4.43%)</td><td>0.01 (-1.73%)</td><td>0.01 <b>(+50.94%)</b></td><td>568.40 (+1.75%)</td><td>314.50 (-15.86%)</td><td>304.20 (+4.64%)</td><td>188.20 <b>(-26.11%)</b></td><td>153.19 (+10.34%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.60 (n/a)</td><td>373.76 (n/a)</td><td>290.70 (n/a)</td><td>254.70 (n/a)</td><td>138.84 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (+10.90%)</td><td>0.01 (-11.69%)</td><td>0.01 <b>(-31.65%)</b></td><td>0.01 (-6.44%)</td><td>0.00 <b>(+43.36%)</b></td><td>557.20 (+6.87%)</td><td>414.88 (+17.97%)</td><td>457.10 <b>(+46.27%)</b></td><td>248.90 (-9.82%)</td><td>128.69 <b>(+31.18%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.40 (n/a)</td><td>351.68 (n/a)</td><td>312.50 (n/a)</td><td>276.00 (n/a)</td><td>98.11 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>12.14 <b>(+53.65%)</b></td><td>7.22 (+13.20%)</td><td>5.40 (-13.85%)</td><td>4.40 (-12.64%)</td><td>3.37 <b>(+209.78%)</b></td><td>477.20 (+14.46%)</td><td>339.28 (+0.77%)</td><td>388.20 (+16.09%)</td><td>172.80 <b>(-34.94%)</b></td><td>133.12 <b>(+132.01%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.90 (n/a)</td><td>6.38 (n/a)</td><td>6.27 (n/a)</td><td>5.03 (n/a)</td><td>1.09 (n/a)</td><td>416.90 (n/a)</td><td>336.68 (n/a)</td><td>334.40 (n/a)</td><td>265.60 (n/a)</td><td>57.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.52 (-4.80%)</td><td>0.40 (-14.63%)</td><td>0.49 (-3.19%)</td><td>0.24 <b>(-28.26%)</b></td><td>0.14 <b>(+67.86%)</b></td><td>547.10 <b>(+39.39%)</b></td><td>365.00 <b>(+27.03%)</b></td><td>271.90 (+3.27%)</td><td>252.80 (+5.03%)</td><td>141.62 <b>(+134.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>392.50 (n/a)</td><td>287.34 (n/a)</td><td>263.30 (n/a)</td><td>240.70 (n/a)</td><td>60.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 (-5.74%)</td><td>0.44 (+12.96%)</td><td>0.45 <b>(+45.04%)</b></td><td>0.28 (+2.63%)</td><td>0.11 <b>(-28.56%)</b></td><td>479.50 (-2.54%)</td><td>316.60 (-15.95%)</td><td>295.40 <b>(-31.05%)</b></td><td>242.30 (+6.09%)</td><td>96.42 <b>(-25.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>492.00 (n/a)</td><td>376.66 (n/a)</td><td>428.40 (n/a)</td><td>228.40 (n/a)</td><td>129.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.47 (-15.08%)</td><td>0.35 (-6.74%)</td><td>0.29 (-4.49%)</td><td>0.24 (+0.90%)</td><td>0.10 <b>(-21.51%)</b></td><td>551.10 (-0.90%)</td><td>410.38 (+4.43%)</td><td>455.30 (+4.71%)</td><td>280.60 (+17.75%)</td><td>116.35 (-9.93%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>556.10 (n/a)</td><td>392.98 (n/a)</td><td>434.80 (n/a)</td><td>238.30 (n/a)</td><td>129.18 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.55 (+14.09%)</td><td>0.43 (+18.48%)</td><td>0.45 <b>(+24.29%)</b></td><td>0.27 <b>(+26.81%)</b></td><td>0.10 (-13.68%)</td><td>491.50 <b>(-21.15%)</b></td><td>322.50 (-18.88%)</td><td>295.60 (-19.54%)</td><td>239.30 (-12.34%)</td><td>97.48 <b>(-33.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>623.30 (n/a)</td><td>397.56 (n/a)</td><td>367.40 (n/a)</td><td>273.00 (n/a)</td><td>146.22 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.56 (-3.81%)</td><td>0.44 (-5.35%)</td><td>0.46 (-9.87%)</td><td>0.29 <b>(+24.54%)</b></td><td>0.11 <b>(-21.78%)</b></td><td>462.20 (-19.72%)</td><td>314.64 (-0.29%)</td><td>284.40 (+10.96%)</td><td>235.00 (+3.98%)</td><td>90.55 <b>(-38.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.52 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>575.70 (n/a)</td><td>315.54 (n/a)</td><td>256.30 (n/a)</td><td>226.00 (n/a)</td><td>146.26 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.01 (-12.28%)</td><td>0.01 (-8.11%)</td><td>0.01 (-13.47%)</td><td>0.01 (+11.89%)</td><td>0.00 <b>(-31.86%)</b></td><td>402.40 (-10.62%)</td><td>333.30 (+5.85%)</td><td>316.10 (+15.53%)</td><td>273.10 (+13.98%)</td><td>61.03 <b>(-29.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.20 (n/a)</td><td>314.88 (n/a)</td><td>273.60 (n/a)</td><td>239.60 (n/a)</td><td>87.16 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.02 (-9.85%)</td><td>0.01 (-9.91%)</td><td>0.01 <b>(-26.88%)</b></td><td>0.01 <b>(+20.49%)</b></td><td>0.00 <b>(-26.64%)</b></td><td>510.20 (-17.00%)</td><td>388.66 (+4.27%)</td><td>420.90 <b>(+36.79%)</b></td><td>249.20 (+10.90%)</td><td>101.11 <b>(-35.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.70 (n/a)</td><td>372.76 (n/a)</td><td>307.70 (n/a)</td><td>224.70 (n/a)</td><td>156.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.00 (+20.00%)</td><td>0.00 <b>(+69.23%)</b></td><td>0.00 <b>(+200.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+63.30%)</b></td><td>23982.72 (+2.16%)</td><td>13180.15 <b>(-27.81%)</b></td><td>6867.10 <b>(-67.02%)</b></td><td>6309.89 <b>(-27.32%)</b></td><td>8992.49 <b>(+51.33%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23475.17 (n/a)</td><td>18258.74 (n/a)</td><td>20819.46 (n/a)</td><td>8681.71 (n/a)</td><td>5942.38 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.00 <b>(-42.86%)</b></td><td>0.00 <b>(-47.06%)</b></td><td>0.00 <b>(-58.33%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(-58.26%)</b></td><td>19723.19 <b>(+23.69%)</b></td><td>16126.55 <b>(+78.39%)</b></td><td>17139.32 <b>(+149.53%)</b></td><td>9851.57 <b>(+70.99%)</b></td><td>3714.41 (-10.54%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>15945.70 (n/a)</td><td>9039.86 (n/a)</td><td>6868.75 (n/a)</td><td>5761.33 (n/a)</td><td>4151.98 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.16 <b>(+25.94%)</b></td><td>0.11 (+16.40%)</td><td>0.11 (+15.00%)</td><td>0.08 (+10.99%)</td><td>0.03 <b>(+63.90%)</b></td><td>25953.47 (-9.96%)</td><td>20167.87 (-11.32%)</td><td>19830.76 (-13.02%)</td><td>13053.73 <b>(-20.59%)</b></td><td>5410.44 <b>(+22.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28824.41 (n/a)</td><td>22743.56 (n/a)</td><td>22799.64 (n/a)</td><td>16438.36 (n/a)</td><td>4401.45 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.77 (-5.74%)</td><td>2.01 (+4.52%)</td><td>1.99 (-16.46%)</td><td>1.29 <b>(+327.14%)</b></td><td>0.70 <b>(-31.26%)</b></td><td>812.20 <b>(-76.59%)</b></td><td>580.70 <b>(-45.88%)</b></td><td>526.90 (+19.70%)</td><td>378.70 (+6.08%)</td><td>209.88 <b>(-84.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.94 (n/a)</td><td>1.92 (n/a)</td><td>2.38 (n/a)</td><td>0.30 (n/a)</td><td>1.02 (n/a)</td><td>3469.40 (n/a)</td><td>1073.02 (n/a)</td><td>440.20 (n/a)</td><td>357.00 (n/a)</td><td>1344.31 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.26 (+9.55%)</td><td>2.23 (-7.60%)</td><td>2.48 (-3.48%)</td><td>1.19 (+1.40%)</td><td>0.91 <b>(+24.72%)</b></td><td>877.60 (-1.38%)</td><td>551.04 (+12.88%)</td><td>422.90 (+3.60%)</td><td>321.80 (-8.71%)</td><td>252.97 (+11.34%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.97 (n/a)</td><td>2.42 (n/a)</td><td>2.57 (n/a)</td><td>1.18 (n/a)</td><td>0.73 (n/a)</td><td>889.90 (n/a)</td><td>488.18 (n/a)</td><td>408.20 (n/a)</td><td>352.50 (n/a)</td><td>227.19 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.14 (+12.39%)</td><td>2.25 <b>(+31.74%)</b></td><td>2.05 <b>(+44.49%)</b></td><td>1.73 <b>(+236.67%)</b></td><td>0.58 <b>(-39.27%)</b></td><td>604.70 <b>(-70.30%)</b></td><td>489.56 <b>(-44.50%)</b></td><td>511.00 <b>(-30.80%)</b></td><td>333.70 (-11.01%)</td><td>112.38 <b>(-83.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.80 (n/a)</td><td>1.71 (n/a)</td><td>1.42 (n/a)</td><td>0.52 (n/a)</td><td>0.96 (n/a)</td><td>2035.70 (n/a)</td><td>882.16 (n/a)</td><td>738.40 (n/a)</td><td>375.00 (n/a)</td><td>677.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.61 <b>(-54.61%)</b></td><td>1.42 <b>(-41.61%)</b></td><td>1.51 <b>(-42.18%)</b></td><td>0.98 <b>(-32.92%)</b></td><td>0.25 <b>(-70.05%)</b></td><td>1068.90 <b>(+49.08%)</b></td><td>764.88 <b>(+59.72%)</b></td><td>695.10 <b>(+72.95%)</b></td><td>652.10 <b>(+120.30%)</b></td><td>171.86 (-0.92%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.54 (n/a)</td><td>2.42 (n/a)</td><td>2.61 (n/a)</td><td>1.46 (n/a)</td><td>0.83 (n/a)</td><td>717.00 (n/a)</td><td>478.88 (n/a)</td><td>401.90 (n/a)</td><td>296.00 (n/a)</td><td>173.46 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.24 (-16.34%)</td><td>1.61 <b>(-23.62%)</b></td><td>1.11 <b>(-40.15%)</b></td><td>0.59 (+1.17%)</td><td>1.06 <b>(-33.11%)</b></td><td>3564.90 (-1.15%)</td><td>1829.34 (-2.07%)</td><td>1882.90 <b>(+67.07%)</b></td><td>647.50 (+19.53%)</td><td>1135.21 <b>(-26.83%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.87 (n/a)</td><td>2.11 (n/a)</td><td>1.86 (n/a)</td><td>0.58 (n/a)</td><td>1.59 (n/a)</td><td>3606.40 (n/a)</td><td>1867.92 (n/a)</td><td>1127.00 (n/a)</td><td>541.70 (n/a)</td><td>1551.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.44 <b>(+30.72%)</b></td><td>2.63 <b>(+75.98%)</b></td><td>2.04 <b>(+87.49%)</b></td><td>0.97 <b>(+66.21%)</b></td><td>1.42 <b>(+21.66%)</b></td><td>2165.90 <b>(-39.83%)</b></td><td>1058.52 <b>(-50.25%)</b></td><td>1029.60 <b>(-46.66%)</b></td><td>472.40 <b>(-23.51%)</b></td><td>674.15 <b>(-48.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.40 (n/a)</td><td>1.49 (n/a)</td><td>1.09 (n/a)</td><td>0.58 (n/a)</td><td>1.17 (n/a)</td><td>3599.90 (n/a)</td><td>2127.72 (n/a)</td><td>1930.40 (n/a)</td><td>617.60 (n/a)</td><td>1301.76 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.23 (-4.17%)</td><td>2.93 <b>(-22.25%)</b></td><td>3.37 <b>(-22.94%)</b></td><td>0.61 (+2.97%)</td><td>1.72 (-13.31%)</td><td>3424.10 (-2.88%)</td><td>1216.32 (+11.71%)</td><td>623.00 <b>(+29.76%)</b></td><td>401.10 (+4.34%)</td><td>1253.78 (-8.24%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>5.46 (n/a)</td><td>3.77 (n/a)</td><td>4.37 (n/a)</td><td>0.59 (n/a)</td><td>1.98 (n/a)</td><td>3525.70 (n/a)</td><td>1088.78 (n/a)</td><td>480.10 (n/a)</td><td>384.40 (n/a)</td><td>1366.39 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.61 (+2.71%)</td><td>3.34 (-2.60%)</td><td>2.51 (-7.20%)</td><td>0.59 <b>(-77.35%)</b></td><td>3.00 <b>(+78.66%)</b></td><td>3567.00 <b>(+341.52%)</b></td><td>1720.62 <b>(+148.95%)</b></td><td>835.60 (+7.75%)</td><td>317.40 (-2.64%)</td><td>1693.80 <b>(+724.06%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.43 (n/a)</td><td>3.43 (n/a)</td><td>2.70 (n/a)</td><td>2.60 (n/a)</td><td>1.68 (n/a)</td><td>807.90 (n/a)</td><td>691.14 (n/a)</td><td>775.50 (n/a)</td><td>326.00 (n/a)</td><td>205.54 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>4.54 (+19.47%)</td><td>3.66 <b>(+83.22%)</b></td><td>4.14 <b>(+161.45%)</b></td><td>2.36 <b>(+277.20%)</b></td><td>0.94 <b>(-32.90%)</b></td><td>890.50 <b>(-73.49%)</b></td><td>610.58 <b>(-63.35%)</b></td><td>506.00 <b>(-61.75%)</b></td><td>461.70 (-16.28%)</td><td>182.66 <b>(-84.80%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.80 (n/a)</td><td>2.00 (n/a)</td><td>1.59 (n/a)</td><td>0.62 (n/a)</td><td>1.40 (n/a)</td><td>3359.00 (n/a)</td><td>1665.82 (n/a)</td><td>1322.90 (n/a)</td><td>551.50 (n/a)</td><td>1201.34 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>6.45 (+1.62%)</td><td>3.64 (-16.88%)</td><td>3.13 (-13.68%)</td><td>1.77 <b>(-34.22%)</b></td><td>1.82 (+17.09%)</td><td>1184.70 <b>(+52.04%)</b></td><td>697.08 <b>(+31.77%)</b></td><td>669.20 (+15.84%)</td><td>325.30 (-1.60%)</td><td>330.11 <b>(+80.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>6.34 (n/a)</td><td>4.38 (n/a)</td><td>3.63 (n/a)</td><td>2.69 (n/a)</td><td>1.55 (n/a)</td><td>779.20 (n/a)</td><td>529.00 (n/a)</td><td>577.70 (n/a)</td><td>330.60 (n/a)</td><td>182.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.03 (+2.67%)</td><td>3.24 (-1.68%)</td><td>3.33 <b>(+22.12%)</b></td><td>1.72 (-11.73%)</td><td>1.50 (+3.08%)</td><td>2436.70 (+13.29%)</td><td>1576.10 (+6.14%)</td><td>1258.90 (-18.11%)</td><td>833.40 (-2.61%)</td><td>779.17 <b>(+27.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>4.90 (n/a)</td><td>3.29 (n/a)</td><td>2.73 (n/a)</td><td>1.95 (n/a)</td><td>1.45 (n/a)</td><td>2150.80 (n/a)</td><td>1484.86 (n/a)</td><td>1537.40 (n/a)</td><td>855.70 (n/a)</td><td>610.27 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>5.81 <b>(-28.77%)</b></td><td>3.54 <b>(-42.39%)</b></td><td>3.90 <b>(-38.39%)</b></td><td>1.16 <b>(-70.74%)</b></td><td>2.06 <b>(+35.96%)</b></td><td>3605.20 <b>(+241.76%)</b></td><td>1737.48 <b>(+141.17%)</b></td><td>1076.10 <b>(+62.31%)</b></td><td>722.40 <b>(+40.38%)</b></td><td>1259.84 <b>(+520.38%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>8.15 (n/a)</td><td>6.15 (n/a)</td><td>6.33 (n/a)</td><td>3.98 (n/a)</td><td>1.51 (n/a)</td><td>1054.90 (n/a)</td><td>720.44 (n/a)</td><td>663.00 (n/a)</td><td>514.60 (n/a)</td><td>203.07 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>10.15 <b>(+33.01%)</b></td><td>6.65 <b>(+25.67%)</b></td><td>6.26 (+6.10%)</td><td>3.62 <b>(+86.58%)</b></td><td>2.35 (+11.30%)</td><td>1159.90 <b>(-46.41%)</b></td><td>703.96 <b>(-29.17%)</b></td><td>669.70 (-5.74%)</td><td>413.30 <b>(-24.83%)</b></td><td>276.74 <b>(-58.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>7.63 (n/a)</td><td>5.29 (n/a)</td><td>5.90 (n/a)</td><td>1.94 (n/a)</td><td>2.11 (n/a)</td><td>2164.20 (n/a)</td><td>993.88 (n/a)</td><td>710.50 (n/a)</td><td>549.80 (n/a)</td><td>662.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>10.04 (-5.95%)</td><td>6.27 (-10.73%)</td><td>6.58 (+2.29%)</td><td>3.99 (-19.41%)</td><td>2.50 (+15.41%)</td><td>1052.10 <b>(+24.08%)</b></td><td>755.32 (+18.81%)</td><td>637.20 (-2.24%)</td><td>417.70 (+6.31%)</td><td>283.22 <b>(+73.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>10.68 (n/a)</td><td>7.03 (n/a)</td><td>6.43 (n/a)</td><td>4.95 (n/a)</td><td>2.16 (n/a)</td><td>847.90 (n/a)</td><td>635.76 (n/a)</td><td>651.80 (n/a)</td><td>392.90 (n/a)</td><td>163.48 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>9.72 (+4.22%)</td><td>5.64 (+18.74%)</td><td>6.52 <b>(+57.30%)</b></td><td>1.15 (-1.85%)</td><td>3.80 (+11.73%)</td><td>3643.10 (+1.89%)</td><td>1415.72 (-7.28%)</td><td>643.10 <b>(-36.43%)</b></td><td>431.50 (-4.07%)</td><td>1377.79 (+6.39%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>9.33 (n/a)</td><td>4.75 (n/a)</td><td>4.15 (n/a)</td><td>1.17 (n/a)</td><td>3.40 (n/a)</td><td>3575.60 (n/a)</td><td>1526.82 (n/a)</td><td>1011.60 (n/a)</td><td>449.80 (n/a)</td><td>1295.03 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>8.71 (-3.33%)</td><td>7.35 <b>(+24.35%)</b></td><td>7.36 (+7.67%)</td><td>5.81 <b>(+183.93%)</b></td><td>1.17 <b>(-59.62%)</b></td><td>722.20 <b>(-64.78%)</b></td><td>582.52 <b>(-38.84%)</b></td><td>569.60 (-7.13%)</td><td>481.60 (+3.46%)</td><td>96.72 <b>(-85.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>9.01 (n/a)</td><td>5.91 (n/a)</td><td>6.84 (n/a)</td><td>2.05 (n/a)</td><td>2.90 (n/a)</td><td>2050.50 (n/a)</td><td>952.44 (n/a)</td><td>613.30 (n/a)</td><td>465.50 (n/a)</td><td>662.40 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.70 (+4.33%)</td><td>1.40 (+17.10%)</td><td>1.46 (+11.38%)</td><td>0.96 <b>(+32.27%)</b></td><td>0.32 (-15.71%)</td><td>548.90 <b>(-24.39%)</b></td><td>392.06 (-18.27%)</td><td>358.00 (-10.21%)</td><td>308.30 (-4.17%)</td><td>100.49 <b>(-40.60%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.63 (n/a)</td><td>1.20 (n/a)</td><td>1.31 (n/a)</td><td>0.72 (n/a)</td><td>0.37 (n/a)</td><td>726.00 (n/a)</td><td>479.72 (n/a)</td><td>398.70 (n/a)</td><td>321.70 (n/a)</td><td>169.17 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>2.46 (-4.45%)</td><td>1.53 (-17.84%)</td><td>1.59 <b>(-31.69%)</b></td><td>0.30 (+0.31%)</td><td>0.78 (-19.99%)</td><td>3452.30 (-0.31%)</td><td>1164.04 (+7.41%)</td><td>657.60 <b>(+46.39%)</b></td><td>426.30 (+4.66%)</td><td>1282.97 (-3.91%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>2.57 (n/a)</td><td>1.86 (n/a)</td><td>2.33 (n/a)</td><td>0.30 (n/a)</td><td>0.97 (n/a)</td><td>3462.90 (n/a)</td><td>1083.76 (n/a)</td><td>449.20 (n/a)</td><td>407.30 (n/a)</td><td>1335.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>3.82 (-4.11%)</td><td>2.99 (+18.81%)</td><td>3.43 (+5.21%)</td><td>1.02 <b>(+66.90%)</b></td><td>1.13 <b>(-26.56%)</b></td><td>2046.70 <b>(-40.08%)</b></td><td>894.58 <b>(-36.55%)</b></td><td>612.00 (-4.95%)</td><td>549.30 (+4.29%)</td><td>645.86 <b>(-48.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>3.98 (n/a)</td><td>2.51 (n/a)</td><td>3.26 (n/a)</td><td>0.61 (n/a)</td><td>1.54 (n/a)</td><td>3415.80 (n/a)</td><td>1409.84 (n/a)</td><td>643.90 (n/a)</td><td>526.70 (n/a)</td><td>1254.91 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>1.92 <b>(+54.13%)</b></td><td>1.55 <b>(+74.17%)</b></td><td>1.59 <b>(+71.25%)</b></td><td>1.04 <b>(+274.04%)</b></td><td>0.33 (-13.61%)</td><td>503.10 <b>(-73.26%)</b></td><td>352.94 <b>(-55.29%)</b></td><td>329.00 <b>(-41.61%)</b></td><td>273.00 <b>(-35.12%)</b></td><td>89.42 <b>(-85.50%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>1.25 (n/a)</td><td>0.89 (n/a)</td><td>0.93 (n/a)</td><td>0.28 (n/a)</td><td>0.38 (n/a)</td><td>1881.80 (n/a)</td><td>789.32 (n/a)</td><td>563.50 (n/a)</td><td>420.80 (n/a)</td><td>616.67 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.13 (-16.24%)</td><td>0.09 <b>(-29.56%)</b></td><td>0.06 <b>(-46.95%)</b></td><td>0.05 <b>(-51.30%)</b></td><td>0.04 <b>(+79.48%)</b></td><td>624.00 <b>(+105.33%)</b></td><td>438.86 <b>(+60.71%)</b></td><td>522.30 <b>(+88.49%)</b></td><td>246.20 (+19.40%)</td><td>169.86 <b>(+326.88%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>303.90 (n/a)</td><td>273.08 (n/a)</td><td>277.10 (n/a)</td><td>206.20 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.11 (-8.99%)</td><td>0.07 (-14.04%)</td><td>0.06 (-1.34%)</td><td>0.06 (+8.53%)</td><td>0.02 <b>(-29.16%)</b></td><td>562.00 (-7.87%)</td><td>487.28 (+9.94%)</td><td>524.40 (+1.35%)</td><td>288.80 (+9.89%)</td><td>112.39 <b>(-28.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.00 (n/a)</td><td>443.24 (n/a)</td><td>517.40 (n/a)</td><td>262.80 (n/a)</td><td>157.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 (+7.80%)</td><td>0.16 (+4.13%)</td><td>0.13 (-4.42%)</td><td>0.12 (+2.81%)</td><td>0.05 <b>(+27.33%)</b></td><td>526.20 (-2.74%)</td><td>430.94 (-1.34%)</td><td>505.50 (+4.62%)</td><td>268.50 (-7.22%)</td><td>122.36 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>541.00 (n/a)</td><td>436.78 (n/a)</td><td>483.20 (n/a)</td><td>289.40 (n/a)</td><td>100.73 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.24 (+13.18%)</td><td>0.19 (+16.95%)</td><td>0.18 <b>(+21.64%)</b></td><td>0.12 (-8.26%)</td><td>0.05 <b>(+58.09%)</b></td><td>532.60 (+9.01%)</td><td>373.28 (-11.36%)</td><td>362.00 (-17.78%)</td><td>270.20 (-11.67%)</td><td>107.48 <b>(+53.29%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>488.60 (n/a)</td><td>421.10 (n/a)</td><td>440.30 (n/a)</td><td>305.90 (n/a)</td><td>70.12 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.23 (-4.98%)</td><td>0.15 (-10.36%)</td><td>0.14 (-14.15%)</td><td>0.12 (-10.78%)</td><td>0.04 (+3.98%)</td><td>561.60 (+12.10%)</td><td>461.60 (+12.70%)</td><td>477.00 (+16.48%)</td><td>291.20 (+5.24%)</td><td>102.66 (+19.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>501.00 (n/a)</td><td>409.58 (n/a)</td><td>409.50 (n/a)</td><td>276.70 (n/a)</td><td>85.70 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.44 (-1.56%)</td><td>0.37 (+19.97%)</td><td>0.42 <b>(+62.57%)</b></td><td>0.26 <b>(+31.66%)</b></td><td>0.09 <b>(-30.32%)</b></td><td>503.50 <b>(-24.06%)</b></td><td>370.38 <b>(-22.87%)</b></td><td>311.10 <b>(-38.48%)</b></td><td>294.70 (+1.59%)</td><td>96.94 <b>(-46.16%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>663.00 (n/a)</td><td>480.20 (n/a)</td><td>505.70 (n/a)</td><td>290.10 (n/a)</td><td>180.05 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.51 (+13.80%)</td><td>0.34 (+2.96%)</td><td>0.29 (-7.34%)</td><td>0.22 (+3.17%)</td><td>0.12 <b>(+24.18%)</b></td><td>591.20 (-3.08%)</td><td>424.18 (-0.48%)</td><td>454.80 (+7.90%)</td><td>259.10 (-12.11%)</td><td>141.68 (+7.51%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>610.00 (n/a)</td><td>426.22 (n/a)</td><td>421.50 (n/a)</td><td>294.80 (n/a)</td><td>131.78 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.56 <b>(+24.95%)</b></td><td>0.37 (+14.53%)</td><td>0.46 <b>(+54.71%)</b></td><td>0.07 <b>(-74.72%)</b></td><td>0.19 <b>(+169.74%)</b></td><td>1878.10 <b>(+295.56%)</b></td><td>618.98 <b>(+49.50%)</b></td><td>287.70 <b>(-35.36%)</b></td><td>233.30 (-19.97%)</td><td>707.08 <b>(+870.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>474.80 (n/a)</td><td>414.02 (n/a)</td><td>445.10 (n/a)</td><td>291.50 (n/a)</td><td>72.89 (n/a)</td>
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
<td><code>abd8bb1</code> — 2026-09-12 02:15:58</td><td>0.07 (+17.85%)</td><td>0.05 (+17.75%)</td><td>0.06 <b>(+79.55%)</b></td><td>0.03 (-10.08%)</td><td>0.02 <b>(+44.11%)</b></td><td>514.50 (+11.22%)</td><td>348.02 (-9.44%)</td><td>254.70 <b>(-44.32%)</b></td><td>224.10 (-15.15%)</td><td>146.18 <b>(+40.26%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:09:42</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>462.60 (n/a)</td><td>384.30 (n/a)</td><td>457.40 (n/a)</td><td>264.10 (n/a)</td><td>104.22 (n/a)</td>
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
