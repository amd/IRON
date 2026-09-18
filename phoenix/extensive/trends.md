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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (+17.96%)</td><td>0.02 (+0.91%)</td><td>0.01 (-19.50%)</td><td>0.01 (-15.73%)</td><td>0.01 <b>(+79.50%)</b></td><td>543.40 (+18.67%)</td><td>388.32 (+8.32%)</td><td>428.50 <b>(+24.20%)</b></td><td>223.90 (-15.25%)</td><td>146.80 <b>(+73.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.90 (n/a)</td><td>358.50 (n/a)</td><td>345.00 (n/a)</td><td>264.20 (n/a)</td><td>84.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-15.61%)</td><td>0.02 (+0.62%)</td><td>0.02 (+3.97%)</td><td>0.01 <b>(+35.62%)</b></td><td>0.01 <b>(-24.54%)</b></td><td>558.40 <b>(-26.26%)</b></td><td>384.54 (-8.55%)</td><td>296.50 (-3.83%)</td><td>283.20 (+18.49%)</td><td>133.40 <b>(-37.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>757.30 (n/a)</td><td>420.50 (n/a)</td><td>308.30 (n/a)</td><td>239.00 (n/a)</td><td>212.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+27.38%)</b></td><td>0.01 (-13.19%)</td><td>0.01 <b>(-25.43%)</b></td><td>0.00 <b>(-72.58%)</b></td><td>0.01 <b>(+92.46%)</b></td><td>1814.30 <b>(+264.68%)</b></td><td>732.06 <b>(+88.23%)</b></td><td>594.00 <b>(+34.12%)</b></td><td>204.70 <b>(-21.51%)</b></td><td>649.55 <b>(+449.19%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>497.50 (n/a)</td><td>388.92 (n/a)</td><td>442.90 (n/a)</td><td>260.80 (n/a)</td><td>118.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+9.27%)</td><td>0.02 (+10.53%)</td><td>0.01 (-10.99%)</td><td>0.01 (+2.71%)</td><td>0.01 <b>(+43.10%)</b></td><td>520.60 (-2.64%)</td><td>404.82 (-4.95%)</td><td>474.50 (+12.36%)</td><td>247.00 (-8.45%)</td><td>134.00 <b>(+33.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.70 (n/a)</td><td>425.92 (n/a)</td><td>422.30 (n/a)</td><td>269.80 (n/a)</td><td>100.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (+13.93%)</td><td>0.01 <b>(-26.31%)</b></td><td>0.01 <b>(-47.27%)</b></td><td>0.01 <b>(-20.77%)</b></td><td>0.01 <b>(+32.43%)</b></td><td>646.10 <b>(+26.22%)</b></td><td>503.52 <b>(+44.91%)</b></td><td>515.40 <b>(+89.62%)</b></td><td>229.10 (-12.22%)</td><td>169.03 <b>(+46.96%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.90 (n/a)</td><td>347.46 (n/a)</td><td>271.80 (n/a)</td><td>261.00 (n/a)</td><td>115.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (+15.31%)</td><td>0.02 <b>(-23.32%)</b></td><td>0.01 <b>(-42.09%)</b></td><td>0.01 (-1.93%)</td><td>0.01 <b>(+37.88%)</b></td><td>632.30 (+1.97%)</td><td>469.06 <b>(+36.41%)</b></td><td>490.20 <b>(+72.67%)</b></td><td>206.30 (-13.28%)</td><td>165.07 (+5.77%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.10 (n/a)</td><td>343.86 (n/a)</td><td>283.90 (n/a)</td><td>237.90 (n/a)</td><td>156.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (-16.12%)</td><td>0.03 (+7.64%)</td><td>0.03 (+8.02%)</td><td>0.02 <b>(+204.17%)</b></td><td>0.01 <b>(-32.90%)</b></td><td>634.00 <b>(-67.12%)</b></td><td>457.70 <b>(-36.15%)</b></td><td>466.50 (-7.42%)</td><td>292.80 (+19.22%)</td><td>161.09 <b>(-76.64%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1928.50 (n/a)</td><td>716.80 (n/a)</td><td>503.90 (n/a)</td><td>245.60 (n/a)</td><td>689.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (+6.57%)</td><td>0.03 (+10.97%)</td><td>0.03 <b>(+27.22%)</b></td><td>0.02 <b>(-29.49%)</b></td><td>0.01 (+18.74%)</td><td>804.60 <b>(+41.83%)</b></td><td>441.94 (-2.66%)</td><td>384.20 <b>(-21.40%)</b></td><td>227.30 (-6.15%)</td><td>218.39 <b>(+76.44%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>454.00 (n/a)</td><td>488.80 (n/a)</td><td>242.20 (n/a)</td><td>123.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (+7.77%)</td><td>0.03 (-18.35%)</td><td>0.03 (-18.43%)</td><td>0.00 <b>(-80.30%)</b></td><td>0.02 <b>(+84.58%)</b></td><td>2476.70 <b>(+407.62%)</b></td><td>828.58 <b>(+108.46%)</b></td><td>477.50 <b>(+22.59%)</b></td><td>247.00 (-7.21%)</td><td>926.54 <b>(+896.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>397.48 (n/a)</td><td>389.50 (n/a)</td><td>266.20 (n/a)</td><td>92.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (-1.46%)</td><td>0.03 (-14.43%)</td><td>0.03 <b>(-22.54%)</b></td><td>0.01 <b>(-79.75%)</b></td><td>0.02 <b>(+71.84%)</b></td><td>2450.10 <b>(+393.87%)</b></td><td>774.76 <b>(+117.03%)</b></td><td>420.50 <b>(+29.11%)</b></td><td>237.60 (+1.50%)</td><td>943.63 <b>(+778.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.10 (n/a)</td><td>356.98 (n/a)</td><td>325.70 (n/a)</td><td>234.10 (n/a)</td><td>107.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (+8.47%)</td><td>0.04 (-0.59%)</td><td>0.03 (-16.37%)</td><td>0.02 (-8.39%)</td><td>0.02 <b>(+20.30%)</b></td><td>608.90 (+9.16%)</td><td>410.74 (+5.01%)</td><td>414.40 (+19.60%)</td><td>221.30 (-7.83%)</td><td>176.21 (+15.01%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>391.16 (n/a)</td><td>346.50 (n/a)</td><td>240.10 (n/a)</td><td>153.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (-15.23%)</td><td>0.03 (+3.53%)</td><td>0.03 <b>(+34.40%)</b></td><td>0.02 (-14.17%)</td><td>0.01 <b>(-22.77%)</b></td><td>645.20 (+16.50%)</td><td>426.20 (-4.97%)</td><td>375.50 <b>(-25.60%)</b></td><td>285.00 (+17.96%)</td><td>142.44 (+7.88%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.80 (n/a)</td><td>448.48 (n/a)</td><td>504.70 (n/a)</td><td>241.60 (n/a)</td><td>132.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (-2.26%)</td><td>0.07 (+11.14%)</td><td>0.07 <b>(+25.86%)</b></td><td>0.05 (+18.64%)</td><td>0.02 (-4.84%)</td><td>490.70 (-15.70%)</td><td>368.58 (-11.19%)</td><td>352.50 <b>(-20.54%)</b></td><td>236.70 (+2.29%)</td><td>118.79 (-11.19%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>582.10 (n/a)</td><td>415.04 (n/a)</td><td>443.60 (n/a)</td><td>231.40 (n/a)</td><td>133.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 <b>(+45.64%)</b></td><td>0.08 <b>(+50.45%)</b></td><td>0.07 <b>(+70.54%)</b></td><td>0.05 <b>(+275.19%)</b></td><td>0.03 (+6.91%)</td><td>517.60 <b>(-73.35%)</b></td><td>357.24 <b>(-51.77%)</b></td><td>328.30 <b>(-41.36%)</b></td><td>203.40 <b>(-31.33%)</b></td><td>142.61 <b>(-79.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1942.00 (n/a)</td><td>740.74 (n/a)</td><td>559.90 (n/a)</td><td>296.20 (n/a)</td><td>686.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (+18.26%)</td><td>0.06 (+16.72%)</td><td>0.05 (+11.24%)</td><td>0.01 (-4.63%)</td><td>0.04 <b>(+20.37%)</b></td><td>1895.10 (+4.86%)</td><td>697.88 (-5.56%)</td><td>462.20 (-10.11%)</td><td>190.40 (-15.45%)</td><td>680.59 (+10.43%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1807.30 (n/a)</td><td>738.96 (n/a)</td><td>514.20 (n/a)</td><td>225.20 (n/a)</td><td>616.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (-11.85%)</td><td>0.06 (-14.40%)</td><td>0.05 (-6.88%)</td><td>0.01 <b>(-71.08%)</b></td><td>0.04 (+17.29%)</td><td>2021.50 <b>(+245.85%)</b></td><td>720.62 <b>(+78.71%)</b></td><td>465.00 (+7.39%)</td><td>228.40 (+13.46%)</td><td>742.88 <b>(+387.32%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>584.50 (n/a)</td><td>403.24 (n/a)</td><td>433.00 (n/a)</td><td>201.30 (n/a)</td><td>152.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-4.93%)</td><td>0.06 (-4.02%)</td><td>0.06 (+1.85%)</td><td>0.04 (-12.24%)</td><td>0.02 (-8.92%)</td><td>691.70 (+13.94%)</td><td>459.42 (+3.72%)</td><td>445.60 (-1.81%)</td><td>270.50 (+5.17%)</td><td>156.66 (+7.36%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>607.10 (n/a)</td><td>442.94 (n/a)</td><td>453.80 (n/a)</td><td>257.20 (n/a)</td><td>145.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 <b>(+32.16%)</b></td><td>0.09 <b>(+47.25%)</b></td><td>0.09 <b>(+64.32%)</b></td><td>0.05 (+17.60%)</td><td>0.02 <b>(+36.62%)</b></td><td>451.00 (-14.97%)</td><td>302.04 <b>(-31.20%)</b></td><td>282.70 <b>(-39.14%)</b></td><td>217.90 <b>(-24.34%)</b></td><td>88.42 (-3.36%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>530.40 (n/a)</td><td>439.02 (n/a)</td><td>464.50 (n/a)</td><td>288.00 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 (-13.83%)</td><td>0.15 (-0.99%)</td><td>0.17 <b>(+36.31%)</b></td><td>0.10 (+12.35%)</td><td>0.04 <b>(-26.83%)</b></td><td>491.30 (-11.00%)</td><td>359.52 (-3.05%)</td><td>292.20 <b>(-26.62%)</b></td><td>269.30 (+16.08%)</td><td>106.78 (-19.33%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>552.00 (n/a)</td><td>370.84 (n/a)</td><td>398.20 (n/a)</td><td>232.00 (n/a)</td><td>132.38 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (-17.82%)</td><td>0.13 (-9.31%)</td><td>0.13 <b>(-22.58%)</b></td><td>0.11 <b>(+33.90%)</b></td><td>0.01 <b>(-66.88%)</b></td><td>439.20 <b>(-25.31%)</b></td><td>385.14 (+2.20%)</td><td>380.40 <b>(+29.17%)</b></td><td>341.80 <b>(+21.68%)</b></td><td>41.52 <b>(-69.04%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>588.00 (n/a)</td><td>376.84 (n/a)</td><td>294.50 (n/a)</td><td>280.90 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 <b>(-50.66%)</b></td><td>0.13 (-17.89%)</td><td>0.13 <b>(+39.45%)</b></td><td>0.09 (+4.63%)</td><td>0.03 <b>(-71.42%)</b></td><td>556.00 (-4.42%)</td><td>394.68 (-3.71%)</td><td>368.70 <b>(-28.28%)</b></td><td>305.10 <b>(+102.59%)</b></td><td>102.88 <b>(-48.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.33 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>581.70 (n/a)</td><td>409.90 (n/a)</td><td>514.10 (n/a)</td><td>150.60 (n/a)</td><td>198.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 (-8.95%)</td><td>0.13 (-16.69%)</td><td>0.11 <b>(-36.34%)</b></td><td>0.08 <b>(+232.19%)</b></td><td>0.05 <b>(-36.55%)</b></td><td>621.20 <b>(-69.90%)</b></td><td>436.88 <b>(-30.68%)</b></td><td>434.90 <b>(+57.06%)</b></td><td>268.10 (+9.83%)</td><td>153.10 <b>(-80.90%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2063.60 (n/a)</td><td>630.26 (n/a)</td><td>276.90 (n/a)</td><td>244.10 (n/a)</td><td>801.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.23 (+1.50%)</td><td>0.15 (+19.68%)</td><td>0.19 <b>(+67.18%)</b></td><td>0.02 <b>(-72.32%)</b></td><td>0.08 <b>(+47.88%)</b></td><td>2008.00 <b>(+261.28%)</b></td><td>620.90 <b>(+46.51%)</b></td><td>260.30 <b>(-40.17%)</b></td><td>218.00 (-1.49%)</td><td>777.41 <b>(+518.78%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>555.80 (n/a)</td><td>423.80 (n/a)</td><td>435.10 (n/a)</td><td>221.30 (n/a)</td><td>125.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 <b>(-44.85%)</b></td><td>0.07 <b>(-53.63%)</b></td><td>0.09 <b>(-46.96%)</b></td><td>0.02 <b>(-74.91%)</b></td><td>0.04 <b>(-23.16%)</b></td><td>2184.80 <b>(+298.61%)</b></td><td>1112.22 <b>(+203.85%)</b></td><td>525.30 <b>(+88.55%)</b></td><td>437.50 <b>(+81.31%)</b></td><td>867.07 <b>(+465.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>548.10 (n/a)</td><td>366.04 (n/a)</td><td>278.60 (n/a)</td><td>241.30 (n/a)</td><td>153.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (-2.44%)</td><td>0.01 (-17.42%)</td><td>0.01 (-13.47%)</td><td>0.00 <b>(-47.90%)</b></td><td>0.00 <b>(+67.56%)</b></td><td>772.20 <b>(+91.90%)</b></td><td>403.28 <b>(+37.81%)</b></td><td>312.50 (+15.57%)</td><td>242.30 (+2.50%)</td><td>213.76 <b>(+234.98%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>402.40 (n/a)</td><td>292.64 (n/a)</td><td>270.40 (n/a)</td><td>236.40 (n/a)</td><td>63.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 <b>(-30.94%)</b></td><td>0.01 <b>(-33.09%)</b></td><td>0.00 <b>(-44.97%)</b></td><td>0.00 (-5.24%)</td><td>0.00 <b>(-48.15%)</b></td><td>587.10 (+5.52%)</td><td>485.20 <b>(+41.54%)</b></td><td>529.20 <b>(+81.67%)</b></td><td>338.50 <b>(+44.78%)</b></td><td>97.24 <b>(-24.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>556.40 (n/a)</td><td>342.80 (n/a)</td><td>291.30 (n/a)</td><td>233.80 (n/a)</td><td>128.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 <b>(-23.25%)</b></td><td>0.01 (-6.94%)</td><td>0.01 (-2.68%)</td><td>0.01 (+7.60%)</td><td>0.00 <b>(-38.87%)</b></td><td>450.80 (-7.07%)</td><td>309.88 (+2.56%)</td><td>275.10 (+2.76%)</td><td>259.20 <b>(+30.25%)</b></td><td>80.11 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.10 (n/a)</td><td>302.14 (n/a)</td><td>267.70 (n/a)</td><td>199.00 (n/a)</td><td>110.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (+1.73%)</td><td>0.01 <b>(+52.13%)</b></td><td>0.01 <b>(+61.19%)</b></td><td>0.00 <b>(+238.98%)</b></td><td>0.00 <b>(-29.94%)</b></td><td>561.20 <b>(-70.50%)</b></td><td>331.10 <b>(-54.58%)</b></td><td>273.40 <b>(-37.98%)</b></td><td>250.30 (-1.69%)</td><td>130.31 <b>(-80.62%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1902.40 (n/a)</td><td>729.02 (n/a)</td><td>440.80 (n/a)</td><td>254.60 (n/a)</td><td>672.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 <b>(+98.92%)</b></td><td>0.01 <b>(+41.22%)</b></td><td>0.01 (+8.33%)</td><td>0.01 <b>(+26.20%)</b></td><td>0.00 <b>(+170.18%)</b></td><td>467.60 <b>(-20.76%)</b></td><td>357.82 <b>(-23.41%)</b></td><td>415.90 (-7.68%)</td><td>175.70 <b>(-49.73%)</b></td><td>117.90 (+3.37%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>590.10 (n/a)</td><td>467.18 (n/a)</td><td>450.50 (n/a)</td><td>349.50 (n/a)</td><td>114.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (+14.30%)</td><td>0.01 (-11.29%)</td><td>0.00 <b>(-31.42%)</b></td><td>0.00 (-2.69%)</td><td>0.00 <b>(+40.68%)</b></td><td>580.30 (+2.76%)</td><td>472.74 (+18.12%)</td><td>535.70 <b>(+45.81%)</b></td><td>235.60 (-12.51%)</td><td>143.68 <b>(+22.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>564.70 (n/a)</td><td>400.22 (n/a)</td><td>367.40 (n/a)</td><td>269.30 (n/a)</td><td>117.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-10.28%)</td><td>0.02 (+1.94%)</td><td>0.02 (+1.66%)</td><td>0.01 (+14.19%)</td><td>0.00 <b>(-29.17%)</b></td><td>528.90 (-12.43%)</td><td>327.34 (-7.67%)</td><td>285.70 (-1.65%)</td><td>246.90 (+11.47%)</td><td>114.68 <b>(-27.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.00 (n/a)</td><td>354.52 (n/a)</td><td>290.50 (n/a)</td><td>221.50 (n/a)</td><td>157.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+13.56%)</td><td>0.01 (+13.94%)</td><td>0.01 (+7.47%)</td><td>0.01 <b>(+269.20%)</b></td><td>0.01 <b>(-26.55%)</b></td><td>523.20 <b>(-72.91%)</b></td><td>411.00 <b>(-41.68%)</b></td><td>462.80 (-6.96%)</td><td>233.30 (-11.93%)</td><td>116.00 <b>(-83.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1931.60 (n/a)</td><td>704.78 (n/a)</td><td>497.40 (n/a)</td><td>264.90 (n/a)</td><td>696.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+27.79%)</b></td><td>0.01 (+16.53%)</td><td>0.01 (+8.84%)</td><td>0.01 <b>(+32.44%)</b></td><td>0.00 <b>(+30.67%)</b></td><td>478.20 <b>(-24.50%)</b></td><td>381.72 (-14.39%)</td><td>383.70 (-8.14%)</td><td>252.80 <b>(-21.73%)</b></td><td>83.52 <b>(-27.87%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.40 (n/a)</td><td>445.88 (n/a)</td><td>417.70 (n/a)</td><td>323.00 (n/a)</td><td>115.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(-36.53%)</b></td><td>0.01 <b>(-33.79%)</b></td><td>0.01 (-12.56%)</td><td>0.00 <b>(-71.67%)</b></td><td>0.01 <b>(-24.62%)</b></td><td>1826.80 <b>(+253.00%)</b></td><td>710.56 <b>(+92.93%)</b></td><td>493.40 (+14.35%)</td><td>324.30 <b>(+57.50%)</b></td><td>630.85 <b>(+361.42%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.50 (n/a)</td><td>368.30 (n/a)</td><td>431.50 (n/a)</td><td>205.90 (n/a)</td><td>136.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(-36.05%)</b></td><td>0.01 (-19.46%)</td><td>0.01 (-4.91%)</td><td>0.01 (-4.60%)</td><td>0.00 <b>(-51.48%)</b></td><td>558.90 (+4.82%)</td><td>422.60 (+13.85%)</td><td>350.10 (+5.17%)</td><td>320.60 <b>(+56.39%)</b></td><td>116.00 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.20 (n/a)</td><td>371.18 (n/a)</td><td>332.90 (n/a)</td><td>205.00 (n/a)</td><td>152.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+15.75%)</td><td>0.01 (-5.78%)</td><td>0.01 (-0.44%)</td><td>0.01 <b>(-25.56%)</b></td><td>0.01 <b>(+28.86%)</b></td><td>716.20 <b>(+34.35%)</b></td><td>456.32 (+11.88%)</td><td>447.30 (+0.45%)</td><td>252.00 (-13.61%)</td><td>170.72 <b>(+56.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.10 (n/a)</td><td>407.86 (n/a)</td><td>445.30 (n/a)</td><td>291.70 (n/a)</td><td>109.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (-19.70%)</td><td>0.03 (-10.51%)</td><td>0.03 (-13.71%)</td><td>0.02 <b>(+33.48%)</b></td><td>0.01 <b>(-39.84%)</b></td><td>471.40 <b>(-25.08%)</b></td><td>330.70 (+0.33%)</td><td>326.80 (+15.89%)</td><td>223.40 <b>(+24.53%)</b></td><td>90.06 <b>(-47.98%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>629.20 (n/a)</td><td>329.62 (n/a)</td><td>282.00 (n/a)</td><td>179.40 (n/a)</td><td>173.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+7.17%)</td><td>0.03 (+1.93%)</td><td>0.03 (-14.48%)</td><td>0.02 (-14.80%)</td><td>0.01 (+17.55%)</td><td>521.60 (+17.37%)</td><td>338.02 (+0.33%)</td><td>334.30 (+16.97%)</td><td>239.60 (-6.70%)</td><td>112.88 <b>(+24.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>444.40 (n/a)</td><td>336.90 (n/a)</td><td>285.80 (n/a)</td><td>256.80 (n/a)</td><td>90.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 <b>(+27.02%)</b></td><td>0.03 (-0.55%)</td><td>0.02 <b>(-34.81%)</b></td><td>0.02 (-4.16%)</td><td>0.02 <b>(+36.04%)</b></td><td>570.30 (+4.35%)</td><td>395.34 (+4.76%)</td><td>456.60 <b>(+53.43%)</b></td><td>191.00 <b>(-21.27%)</b></td><td>154.35 (+4.16%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.50 (n/a)</td><td>377.36 (n/a)</td><td>297.60 (n/a)</td><td>242.60 (n/a)</td><td>148.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (-7.09%)</td><td>0.04 (-0.42%)</td><td>0.03 (-5.18%)</td><td>0.02 (+9.71%)</td><td>0.01 (-7.15%)</td><td>499.90 (-8.86%)</td><td>339.78 (-1.44%)</td><td>319.70 (+5.48%)</td><td>197.60 (+7.63%)</td><td>132.99 (-9.24%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>548.50 (n/a)</td><td>344.76 (n/a)</td><td>303.10 (n/a)</td><td>183.60 (n/a)</td><td>146.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 <b>(-39.23%)</b></td><td>0.02 <b>(-35.06%)</b></td><td>0.02 <b>(-44.32%)</b></td><td>0.02 (-1.73%)</td><td>0.01 <b>(-51.34%)</b></td><td>621.90 (+1.77%)</td><td>465.68 <b>(+38.99%)</b></td><td>458.00 <b>(+79.61%)</b></td><td>291.90 <b>(+64.54%)</b></td><td>137.32 <b>(-20.05%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>611.10 (n/a)</td><td>335.04 (n/a)</td><td>255.00 (n/a)</td><td>177.40 (n/a)</td><td>171.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 <b>(+24.35%)</b></td><td>0.03 (+2.57%)</td><td>0.02 (-3.34%)</td><td>0.02 <b>(+22.05%)</b></td><td>0.01 <b>(+22.92%)</b></td><td>508.00 (-18.06%)</td><td>425.74 (-2.62%)</td><td>467.70 (+3.45%)</td><td>223.50 (-19.58%)</td><td>114.76 <b>(-20.74%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.00 (n/a)</td><td>437.20 (n/a)</td><td>452.10 (n/a)</td><td>277.90 (n/a)</td><td>144.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 <b>(-35.78%)</b></td><td>0.05 <b>(-31.45%)</b></td><td>0.05 <b>(-32.94%)</b></td><td>0.04 (-1.08%)</td><td>0.02 <b>(-44.58%)</b></td><td>552.70 (+1.08%)</td><td>416.28 <b>(+35.43%)</b></td><td>422.30 <b>(+49.12%)</b></td><td>248.20 <b>(+55.71%)</b></td><td>121.41 (-15.81%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>546.80 (n/a)</td><td>307.38 (n/a)</td><td>283.20 (n/a)</td><td>159.40 (n/a)</td><td>144.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 <b>(+21.51%)</b></td><td>0.06 (+19.71%)</td><td>0.07 <b>(+55.25%)</b></td><td>0.01 <b>(-57.41%)</b></td><td>0.03 <b>(+83.40%)</b></td><td>2080.80 <b>(+134.80%)</b></td><td>674.40 <b>(+34.25%)</b></td><td>300.40 <b>(-35.59%)</b></td><td>264.80 (-17.69%)</td><td>789.89 <b>(+252.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>886.20 (n/a)</td><td>502.36 (n/a)</td><td>466.40 (n/a)</td><td>321.70 (n/a)</td><td>224.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 <b>(+22.22%)</b></td><td>0.05 (+6.95%)</td><td>0.04 (-14.63%)</td><td>0.04 (-17.31%)</td><td>0.02 <b>(+105.15%)</b></td><td>577.90 <b>(+20.95%)</b></td><td>443.22 (+3.01%)</td><td>543.40 (+17.14%)</td><td>245.30 (-18.21%)</td><td>158.32 <b>(+113.53%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>477.80 (n/a)</td><td>430.26 (n/a)</td><td>463.90 (n/a)</td><td>299.90 (n/a)</td><td>74.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (+3.55%)</td><td>0.06 (+5.24%)</td><td>0.06 (-6.45%)</td><td>0.04 (+14.04%)</td><td>0.02 (+10.24%)</td><td>544.20 (-12.31%)</td><td>379.98 (-4.78%)</td><td>369.00 (+6.89%)</td><td>234.80 (-3.45%)</td><td>138.63 (-8.97%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.60 (n/a)</td><td>399.06 (n/a)</td><td>345.20 (n/a)</td><td>243.20 (n/a)</td><td>152.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-7.73%)</td><td>0.05 <b>(-26.71%)</b></td><td>0.04 <b>(-44.96%)</b></td><td>0.03 (+5.12%)</td><td>0.02 (-12.47%)</td><td>650.10 (-4.87%)</td><td>495.22 <b>(+30.99%)</b></td><td>543.70 <b>(+81.66%)</b></td><td>239.80 (+8.36%)</td><td>154.12 (-18.08%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>683.40 (n/a)</td><td>378.06 (n/a)</td><td>299.30 (n/a)</td><td>221.30 (n/a)</td><td>188.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-7.10%)</td><td>0.05 (-16.37%)</td><td>0.05 (-11.97%)</td><td>0.04 (+7.77%)</td><td>0.02 (-12.33%)</td><td>566.90 (-7.20%)</td><td>448.86 (+15.83%)</td><td>455.50 (+13.59%)</td><td>222.50 (+7.64%)</td><td>136.50 (-14.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>610.90 (n/a)</td><td>387.52 (n/a)</td><td>401.00 (n/a)</td><td>206.70 (n/a)</td><td>159.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.30 (n/a)</td><td>365.60 (n/a)</td><td>327.90 (n/a)</td><td>274.60 (n/a)</td><td>93.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.10 (n/a)</td><td>396.86 (n/a)</td><td>378.00 (n/a)</td><td>242.00 (n/a)</td><td>131.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.90 (n/a)</td><td>392.38 (n/a)</td><td>310.30 (n/a)</td><td>268.20 (n/a)</td><td>143.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>808.20 (n/a)</td><td>506.18 (n/a)</td><td>597.30 (n/a)</td><td>237.20 (n/a)</td><td>239.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1025.60 (n/a)</td><td>475.06 (n/a)</td><td>317.80 (n/a)</td><td>223.00 (n/a)</td><td>322.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2462.10 (n/a)</td><td>845.38 (n/a)</td><td>494.40 (n/a)</td><td>360.80 (n/a)</td><td>906.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>627.30 (n/a)</td><td>461.94 (n/a)</td><td>485.10 (n/a)</td><td>228.30 (n/a)</td><td>149.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.80 (n/a)</td><td>318.14 (n/a)</td><td>278.30 (n/a)</td><td>231.50 (n/a)</td><td>116.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>610.20 (n/a)</td><td>473.78 (n/a)</td><td>473.40 (n/a)</td><td>295.30 (n/a)</td><td>122.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (-1.25%)</td><td>0.16 <b>(+26.04%)</b></td><td>0.16 <b>(+52.45%)</b></td><td>0.13 <b>(+60.44%)</b></td><td>0.01 <b>(-65.29%)</b></td><td>369.80 <b>(-37.67%)</b></td><td>317.04 <b>(-26.36%)</b></td><td>308.50 <b>(-34.40%)</b></td><td>289.50 (+1.26%)</td><td>30.92 <b>(-76.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>593.30 (n/a)</td><td>430.50 (n/a)</td><td>470.30 (n/a)</td><td>285.90 (n/a)</td><td>131.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>471.30 (n/a)</td><td>373.94 (n/a)</td><td>334.20 (n/a)</td><td>306.40 (n/a)</td><td>79.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>565.80 (n/a)</td><td>398.04 (n/a)</td><td>360.60 (n/a)</td><td>234.30 (n/a)</td><td>146.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>492.40 (n/a)</td><td>304.84 (n/a)</td><td>248.80 (n/a)</td><td>230.20 (n/a)</td><td>108.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>319.48 (n/a)</td><td>271.10 (n/a)</td><td>232.20 (n/a)</td><td>147.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>730.50 (n/a)</td><td>420.58 (n/a)</td><td>298.70 (n/a)</td><td>252.30 (n/a)</td><td>205.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>298.10 (n/a)</td><td>261.64 (n/a)</td><td>245.90 (n/a)</td><td>236.40 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>761.00 (n/a)</td><td>408.06 (n/a)</td><td>244.30 (n/a)</td><td>208.10 (n/a)</td><td>250.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>315.56 (n/a)</td><td>249.40 (n/a)</td><td>232.80 (n/a)</td><td>128.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>292.80 (n/a)</td><td>259.46 (n/a)</td><td>259.10 (n/a)</td><td>238.20 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>387.10 (n/a)</td><td>300.04 (n/a)</td><td>259.50 (n/a)</td><td>235.20 (n/a)</td><td>71.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>298.70 (n/a)</td><td>273.32 (n/a)</td><td>265.50 (n/a)</td><td>248.10 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>446.90 (n/a)</td><td>283.50 (n/a)</td><td>245.60 (n/a)</td><td>234.20 (n/a)</td><td>91.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>513.40 (n/a)</td><td>332.96 (n/a)</td><td>268.30 (n/a)</td><td>234.90 (n/a)</td><td>120.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.61 (+10.90%)</td><td>2.78 (-16.50%)</td><td>2.71 <b>(-22.13%)</b></td><td>1.49 <b>(-21.09%)</b></td><td>1.14 <b>(+26.98%)</b></td><td>7044.80 <b>(+26.73%)</b></td><td>4290.74 <b>(+25.91%)</b></td><td>3871.10 <b>(+28.42%)</b></td><td>2272.50 (-9.83%)</td><td>1740.82 <b>(+40.10%)</b></td><td>1889.94 (+10.90%)</td><td>1140.44 (-16.50%)</td><td>1109.49 <b>(-22.13%)</b></td><td>609.66 <b>(-21.09%)</b></td><td>468.32 <b>(+26.98%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.16 (n/a)</td><td>3.33 (n/a)</td><td>3.48 (n/a)</td><td>1.89 (n/a)</td><td>0.90 (n/a)</td><td>5558.80 (n/a)</td><td>3407.72 (n/a)</td><td>3014.30 (n/a)</td><td>2520.30 (n/a)</td><td>1242.54 (n/a)</td><td>1704.13 (n/a)</td><td>1365.81 (n/a)</td><td>1424.85 (n/a)</td><td>772.64 (n/a)</td><td>368.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.69 (-3.76%)</td><td>3.10 (-15.02%)</td><td>3.30 (-11.13%)</td><td>2.46 <b>(-27.69%)</b></td><td>0.52 <b>(+211.80%)</b></td><td>9585.30 <b>(+38.30%)</b></td><td>7788.88 <b>(+20.29%)</b></td><td>7160.00 (+12.52%)</td><td>6386.40 (+3.90%)</td><td>1368.70 <b>(+352.09%)</b></td><td>2101.61 (-3.76%)</td><td>1764.66 (-15.02%)</td><td>1874.55 (-11.13%)</td><td>1400.25 <b>(-27.69%)</b></td><td>296.21 <b>(+211.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.84 (n/a)</td><td>3.65 (n/a)</td><td>3.71 (n/a)</td><td>3.40 (n/a)</td><td>0.17 (n/a)</td><td>6930.80 (n/a)</td><td>6474.84 (n/a)</td><td>6363.30 (n/a)</td><td>6146.40 (n/a)</td><td>302.75 (n/a)</td><td>2183.69 (n/a)</td><td>2076.47 (n/a)</td><td>2109.26 (n/a)</td><td>1936.54 (n/a)</td><td>95.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.99 (+3.19%)</td><td>3.09 (-2.81%)</td><td>2.91 (-9.58%)</td><td>2.07 (-18.61%)</td><td>0.76 <b>(+59.08%)</b></td><td>8120.40 <b>(+22.87%)</b></td><td>5724.58 (+6.52%)</td><td>5758.70 (+10.60%)</td><td>4205.60 (-3.09%)</td><td>1534.64 <b>(+87.51%)</b></td><td>2042.48 (+3.19%)</td><td>1581.93 (-2.81%)</td><td>1491.63 (-9.58%)</td><td>1057.82 (-18.61%)</td><td>387.83 <b>(+59.08%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.87 (n/a)</td><td>3.18 (n/a)</td><td>3.22 (n/a)</td><td>2.54 (n/a)</td><td>0.48 (n/a)</td><td>6609.10 (n/a)</td><td>5374.14 (n/a)</td><td>5207.00 (n/a)</td><td>4339.80 (n/a)</td><td>818.42 (n/a)</td><td>1979.34 (n/a)</td><td>1627.72 (n/a)</td><td>1649.69 (n/a)</td><td>1299.70 (n/a)</td><td>243.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.06 (+8.34%)</td><td>0.82 (+17.81%)</td><td>0.84 <b>(+23.37%)</b></td><td>0.62 <b>(+40.85%)</b></td><td>0.17 (-16.01%)</td><td>739.40 <b>(-29.01%)</b></td><td>580.44 (-18.10%)</td><td>546.80 (-18.94%)</td><td>434.10 (-7.70%)</td><td>116.70 <b>(-45.39%)</b></td><td>77.29 (+8.34%)</td><td>59.73 (+17.81%)</td><td>61.36 <b>(+23.37%)</b></td><td>45.38 <b>(+40.85%)</b></td><td>12.14 (-16.01%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.98 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.44 (n/a)</td><td>0.20 (n/a)</td><td>1041.50 (n/a)</td><td>708.76 (n/a)</td><td>674.60 (n/a)</td><td>470.30 (n/a)</td><td>213.69 (n/a)</td><td>71.34 (n/a)</td><td>50.70 (n/a)</td><td>49.74 (n/a)</td><td>32.22 (n/a)</td><td>14.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.33 (+9.19%)</td><td>1.03 (+1.47%)</td><td>0.90 (-5.64%)</td><td>0.83 (+12.78%)</td><td>0.25 <b>(+20.59%)</b></td><td>791.70 (-11.32%)</td><td>662.64 (-0.64%)</td><td>724.60 (+5.98%)</td><td>491.10 (-8.41%)</td><td>147.98 (+1.27%)</td><td>136.65 (+9.19%)</td><td>105.81 (+1.47%)</td><td>92.62 (-5.64%)</td><td>84.77 (+12.78%)</td><td>25.45 <b>(+20.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.22 (n/a)</td><td>1.02 (n/a)</td><td>0.96 (n/a)</td><td>0.73 (n/a)</td><td>0.21 (n/a)</td><td>892.80 (n/a)</td><td>666.88 (n/a)</td><td>683.70 (n/a)</td><td>536.20 (n/a)</td><td>146.12 (n/a)</td><td>125.15 (n/a)</td><td>104.28 (n/a)</td><td>98.16 (n/a)</td><td>75.17 (n/a)</td><td>21.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.52 (+2.65%)</td><td>1.12 (-11.51%)</td><td>1.29 (-5.07%)</td><td>0.31 <b>(-68.39%)</b></td><td>0.50 <b>(+134.33%)</b></td><td>2450.90 <b>(+216.37%)</b></td><td>957.10 <b>(+57.28%)</b></td><td>586.10 (+5.34%)</td><td>497.30 (-2.59%)</td><td>841.35 <b>(+651.61%)</b></td><td>168.67 (+2.65%)</td><td>125.07 (-11.51%)</td><td>143.12 (-5.07%)</td><td>34.23 <b>(-68.39%)</b></td><td>55.82 <b>(+134.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.48 (n/a)</td><td>1.27 (n/a)</td><td>1.35 (n/a)</td><td>0.97 (n/a)</td><td>0.21 (n/a)</td><td>774.70 (n/a)</td><td>608.52 (n/a)</td><td>556.40 (n/a)</td><td>510.50 (n/a)</td><td>111.94 (n/a)</td><td>164.31 (n/a)</td><td>141.34 (n/a)</td><td>150.76 (n/a)</td><td>108.29 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.48 (-6.92%)</td><td>0.94 <b>(-31.31%)</b></td><td>1.11 <b>(-22.46%)</b></td><td>0.47 <b>(-58.83%)</b></td><td>0.43 <b>(+110.16%)</b></td><td>2223.20 <b>(+142.92%)</b></td><td>1359.82 <b>(+74.78%)</b></td><td>941.90 <b>(+28.96%)</b></td><td>706.60 (+7.44%)</td><td>693.97 <b>(+475.79%)</b></td><td>189.95 (-6.92%)</td><td>120.74 <b>(-31.31%)</b></td><td>142.49 <b>(-22.46%)</b></td><td>60.37 <b>(-58.83%)</b></td><td>55.39 <b>(+110.16%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.59 (n/a)</td><td>1.37 (n/a)</td><td>1.44 (n/a)</td><td>1.15 (n/a)</td><td>0.21 (n/a)</td><td>915.20 (n/a)</td><td>778.00 (n/a)</td><td>730.40 (n/a)</td><td>657.70 (n/a)</td><td>120.52 (n/a)</td><td>204.08 (n/a)</td><td>175.78 (n/a)</td><td>183.76 (n/a)</td><td>146.65 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.99 (+7.18%)</td><td>1.64 (+4.33%)</td><td>1.92 <b>(+30.58%)</b></td><td>1.06 (-19.78%)</td><td>0.44 <b>(+93.51%)</b></td><td>989.60 <b>(+24.65%)</b></td><td>682.06 (+0.82%)</td><td>545.00 <b>(-23.42%)</b></td><td>527.30 (-6.71%)</td><td>209.18 <b>(+120.99%)</b></td><td>254.55 (+7.18%)</td><td>210.35 (+4.33%)</td><td>246.25 <b>(+30.58%)</b></td><td>135.62 (-19.78%)</td><td>55.70 <b>(+93.51%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.86 (n/a)</td><td>1.58 (n/a)</td><td>1.47 (n/a)</td><td>1.32 (n/a)</td><td>0.22 (n/a)</td><td>793.90 (n/a)</td><td>676.50 (n/a)</td><td>711.70 (n/a)</td><td>565.20 (n/a)</td><td>94.66 (n/a)</td><td>237.49 (n/a)</td><td>201.62 (n/a)</td><td>188.59 (n/a)</td><td>169.07 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.17 (+7.89%)</td><td>1.56 (-3.41%)</td><td>1.36 (-16.44%)</td><td>1.09 (+6.40%)</td><td>0.43 (+1.38%)</td><td>959.60 (-6.02%)</td><td>713.52 (+2.93%)</td><td>768.70 (+19.68%)</td><td>484.30 (-7.31%)</td><td>185.26 (-10.75%)</td><td>277.17 (+7.89%)</td><td>199.21 (-3.41%)</td><td>174.61 (-16.44%)</td><td>139.87 (+6.40%)</td><td>54.48 (+1.38%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.01 (n/a)</td><td>1.61 (n/a)</td><td>1.63 (n/a)</td><td>1.03 (n/a)</td><td>0.42 (n/a)</td><td>1021.10 (n/a)</td><td>693.20 (n/a)</td><td>642.30 (n/a)</td><td>522.50 (n/a)</td><td>207.57 (n/a)</td><td>256.89 (n/a)</td><td>206.25 (n/a)</td><td>208.96 (n/a)</td><td>131.45 (n/a)</td><td>53.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.84 (-1.56%)</td><td>1.10 (-17.84%)</td><td>0.97 <b>(-42.15%)</b></td><td>0.43 (-13.86%)</td><td>0.67 (+5.24%)</td><td>2449.70 (+16.09%)</td><td>1370.46 <b>(+32.08%)</b></td><td>1078.50 <b>(+72.86%)</b></td><td>568.40 (+1.57%)</td><td>880.88 <b>(+29.77%)</b></td><td>236.13 (-1.56%)</td><td>140.27 (-17.84%)</td><td>124.45 <b>(-42.15%)</b></td><td>54.79 (-13.86%)</td><td>86.31 (+5.24%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.87 (n/a)</td><td>1.33 (n/a)</td><td>1.68 (n/a)</td><td>0.50 (n/a)</td><td>0.64 (n/a)</td><td>2110.20 (n/a)</td><td>1037.62 (n/a)</td><td>623.90 (n/a)</td><td>559.60 (n/a)</td><td>678.83 (n/a)</td><td>239.86 (n/a)</td><td>170.73 (n/a)</td><td>215.12 (n/a)</td><td>63.61 (n/a)</td><td>82.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.75 (+8.08%)</td><td>1.32 <b>(+20.62%)</b></td><td>1.52 <b>(+22.38%)</b></td><td>0.48 <b>(+63.60%)</b></td><td>0.50 (-9.03%)</td><td>2167.00 <b>(-38.87%)</b></td><td>988.18 <b>(-29.79%)</b></td><td>688.10 (-18.29%)</td><td>597.50 (-7.48%)</td><td>664.46 <b>(-45.73%)</b></td><td>224.63 (+8.08%)</td><td>169.44 <b>(+20.62%)</b></td><td>195.05 <b>(+22.38%)</b></td><td>61.94 <b>(+63.60%)</b></td><td>64.22 (-9.03%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.62 (n/a)</td><td>1.10 (n/a)</td><td>1.25 (n/a)</td><td>0.30 (n/a)</td><td>0.55 (n/a)</td><td>3545.10 (n/a)</td><td>1407.46 (n/a)</td><td>842.10 (n/a)</td><td>645.80 (n/a)</td><td>1224.41 (n/a)</td><td>207.84 (n/a)</td><td>140.47 (n/a)</td><td>159.38 (n/a)</td><td>37.86 (n/a)</td><td>70.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.52 <b>(-22.71%)</b></td><td>0.94 <b>(-27.41%)</b></td><td>1.09 (-14.55%)</td><td>0.42 <b>(-33.64%)</b></td><td>0.49 (-7.74%)</td><td>2494.50 <b>(+50.69%)</b></td><td>1486.70 <b>(+55.80%)</b></td><td>965.80 (+17.01%)</td><td>692.00 <b>(+29.39%)</b></td><td>894.20 <b>(+98.62%)</b></td><td>193.95 <b>(-22.71%)</b></td><td>119.79 <b>(-27.41%)</b></td><td>138.97 (-14.55%)</td><td>53.81 <b>(-33.64%)</b></td><td>62.75 (-7.74%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.96 (n/a)</td><td>1.29 (n/a)</td><td>1.27 (n/a)</td><td>0.63 (n/a)</td><td>0.53 (n/a)</td><td>1655.40 (n/a)</td><td>954.22 (n/a)</td><td>825.40 (n/a)</td><td>534.80 (n/a)</td><td>450.20 (n/a)</td><td>250.95 (n/a)</td><td>165.02 (n/a)</td><td>162.62 (n/a)</td><td>81.08 (n/a)</td><td>68.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.78 (-7.13%)</td><td>0.59 (+14.04%)</td><td>0.52 <b>(+25.08%)</b></td><td>0.50 <b>(+37.56%)</b></td><td>0.12 <b>(-39.64%)</b></td><td>717.10 <b>(-27.30%)</b></td><td>625.70 (-18.63%)</td><td>697.80 <b>(-20.05%)</b></td><td>461.50 (+7.68%)</td><td>117.10 <b>(-53.13%)</b></td><td>36.35 (-7.13%)</td><td>27.68 (+14.04%)</td><td>24.04 <b>(+25.08%)</b></td><td>23.40 <b>(+37.56%)</b></td><td>5.80 <b>(-39.64%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.84 (n/a)</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.37 (n/a)</td><td>0.21 (n/a)</td><td>986.40 (n/a)</td><td>768.94 (n/a)</td><td>872.80 (n/a)</td><td>428.60 (n/a)</td><td>249.85 (n/a)</td><td>39.15 (n/a)</td><td>24.27 (n/a)</td><td>19.22 (n/a)</td><td>17.01 (n/a)</td><td>9.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.03 (-0.41%)</td><td>1.53 (-16.04%)</td><td>1.11 <b>(-31.03%)</b></td><td>0.97 (-11.82%)</td><td>0.86 (+10.40%)</td><td>4326.50 (+13.40%)</td><td>3251.76 <b>(+23.98%)</b></td><td>3782.50 <b>(+44.98%)</b></td><td>1383.60 (+0.41%)</td><td>1162.02 (+19.81%)</td><td>776.02 (-0.41%)</td><td>391.06 (-16.04%)</td><td>283.87 <b>(-31.03%)</b></td><td>248.18 (-11.82%)</td><td>219.79 (+10.40%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.04 (n/a)</td><td>1.82 (n/a)</td><td>1.61 (n/a)</td><td>1.10 (n/a)</td><td>0.78 (n/a)</td><td>3815.10 (n/a)</td><td>2622.76 (n/a)</td><td>2608.90 (n/a)</td><td>1377.90 (n/a)</td><td>969.91 (n/a)</td><td>779.26 (n/a)</td><td>465.75 (n/a)</td><td>411.57 (n/a)</td><td>281.45 (n/a)</td><td>199.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.91 (+8.46%)</td><td>2.64 (+5.64%)</td><td>2.56 <b>(-22.45%)</b></td><td>0.68 (-14.94%)</td><td>1.33 (-2.89%)</td><td>3842.50 (+17.57%)</td><td>1481.60 (-3.41%)</td><td>1024.70 <b>(+28.96%)</b></td><td>670.90 (-7.81%)</td><td>1338.39 (+17.22%)</td><td>800.20 (+8.46%)</td><td>540.55 (+5.64%)</td><td>523.93 <b>(-22.45%)</b></td><td>139.72 (-14.94%)</td><td>272.42 (-2.89%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.60 (n/a)</td><td>2.50 (n/a)</td><td>3.30 (n/a)</td><td>0.80 (n/a)</td><td>1.37 (n/a)</td><td>3268.40 (n/a)</td><td>1533.86 (n/a)</td><td>794.60 (n/a)</td><td>727.70 (n/a)</td><td>1141.82 (n/a)</td><td>737.81 (n/a)</td><td>511.71 (n/a)</td><td>675.63 (n/a)</td><td>164.26 (n/a)</td><td>280.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.43 (+6.65%)</td><td>2.31 (-15.99%)</td><td>2.13 <b>(-28.71%)</b></td><td>1.56 (-6.44%)</td><td>0.70 (+11.32%)</td><td>5026.10 (+6.88%)</td><td>3632.38 (+19.93%)</td><td>3688.30 <b>(+40.27%)</b></td><td>2294.60 (-6.24%)</td><td>993.90 (+5.02%)</td><td>1052.88 (+6.65%)</td><td>710.15 (-15.99%)</td><td>655.03 <b>(-28.71%)</b></td><td>480.67 (-6.44%)</td><td>213.58 (+11.32%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.21 (n/a)</td><td>2.75 (n/a)</td><td>2.99 (n/a)</td><td>1.67 (n/a)</td><td>0.62 (n/a)</td><td>4702.40 (n/a)</td><td>3028.70 (n/a)</td><td>2629.40 (n/a)</td><td>2447.30 (n/a)</td><td>946.44 (n/a)</td><td>987.19 (n/a)</td><td>845.35 (n/a)</td><td>918.82 (n/a)</td><td>513.77 (n/a)</td><td>191.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.00 (n/a)</td><td>393.78 (n/a)</td><td>427.60 (n/a)</td><td>260.00 (n/a)</td><td>111.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.60 (n/a)</td><td>370.96 (n/a)</td><td>327.30 (n/a)</td><td>301.90 (n/a)</td><td>93.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.70 (n/a)</td><td>422.04 (n/a)</td><td>472.30 (n/a)</td><td>259.40 (n/a)</td><td>143.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>694.80 (n/a)</td><td>513.72 (n/a)</td><td>545.50 (n/a)</td><td>290.80 (n/a)</td><td>148.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.90 (n/a)</td><td>359.48 (n/a)</td><td>290.10 (n/a)</td><td>245.20 (n/a)</td><td>121.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.90 (n/a)</td><td>430.70 (n/a)</td><td>392.60 (n/a)</td><td>255.70 (n/a)</td><td>161.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>878.30 (n/a)</td><td>419.64 (n/a)</td><td>257.30 (n/a)</td><td>174.90 (n/a)</td><td>289.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1051.20 (n/a)</td><td>503.00 (n/a)</td><td>325.30 (n/a)</td><td>262.70 (n/a)</td><td>325.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.10 (n/a)</td><td>453.46 (n/a)</td><td>536.90 (n/a)</td><td>280.30 (n/a)</td><td>158.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.20 (n/a)</td><td>369.18 (n/a)</td><td>267.50 (n/a)</td><td>244.50 (n/a)</td><td>153.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.70 (n/a)</td><td>260.64 (n/a)</td><td>264.70 (n/a)</td><td>206.60 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1292.10 (n/a)</td><td>630.60 (n/a)</td><td>474.60 (n/a)</td><td>437.00 (n/a)</td><td>370.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>780.30 (n/a)</td><td>493.76 (n/a)</td><td>517.20 (n/a)</td><td>266.70 (n/a)</td><td>210.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.60 (n/a)</td><td>428.14 (n/a)</td><td>498.50 (n/a)</td><td>243.90 (n/a)</td><td>136.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>707.40 (n/a)</td><td>359.24 (n/a)</td><td>292.70 (n/a)</td><td>235.90 (n/a)</td><td>196.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>452.56 (n/a)</td><td>481.00 (n/a)</td><td>261.90 (n/a)</td><td>110.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>550.50 (n/a)</td><td>443.78 (n/a)</td><td>462.80 (n/a)</td><td>290.60 (n/a)</td><td>110.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1734.70 (n/a)</td><td>630.74 (n/a)</td><td>354.40 (n/a)</td><td>285.20 (n/a)</td><td>622.28 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>554.10 (n/a)</td><td>428.12 (n/a)</td><td>436.60 (n/a)</td><td>303.90 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1020.30 (n/a)</td><td>494.38 (n/a)</td><td>318.30 (n/a)</td><td>304.70 (n/a)</td><td>308.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1889.20 (n/a)</td><td>675.02 (n/a)</td><td>358.00 (n/a)</td><td>225.70 (n/a)</td><td>696.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>499.10 (n/a)</td><td>423.44 (n/a)</td><td>460.00 (n/a)</td><td>299.00 (n/a)</td><td>84.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1283.90 (n/a)</td><td>634.38 (n/a)</td><td>507.60 (n/a)</td><td>374.40 (n/a)</td><td>368.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>651.50 (n/a)</td><td>439.60 (n/a)</td><td>437.10 (n/a)</td><td>250.50 (n/a)</td><td>147.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.80 <b>(+32.90%)</b></td><td>0.49 (-2.73%)</td><td>0.40 <b>(-24.15%)</b></td><td>0.35 (+2.78%)</td><td>0.19 <b>(+90.61%)</b></td><td>627.70 (-2.71%)</td><td>496.28 (+8.83%)</td><td>557.10 <b>(+31.83%)</b></td><td>277.50 <b>(-24.76%)</b></td><td>149.78 <b>(+36.28%)</b></td><td>34.01 <b>(+32.90%)</b></td><td>20.91 (-2.73%)</td><td>16.94 <b>(-24.15%)</b></td><td>15.03 (+2.78%)</td><td>8.01 <b>(+90.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>645.20 (n/a)</td><td>456.02 (n/a)</td><td>422.60 (n/a)</td><td>368.80 (n/a)</td><td>109.90 (n/a)</td><td>25.59 (n/a)</td><td>21.50 (n/a)</td><td>22.33 (n/a)</td><td>14.63 (n/a)</td><td>4.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.71 <b>(+25.87%)</b></td><td>0.43 (+10.64%)</td><td>0.34 (-13.22%)</td><td>0.19 <b>(+106.39%)</b></td><td>0.22 (+11.45%)</td><td>1185.00 <b>(-51.55%)</b></td><td>642.12 <b>(-27.74%)</b></td><td>641.70 (+15.23%)</td><td>311.80 <b>(-20.54%)</b></td><td>347.45 <b>(-60.40%)</b></td><td>30.27 <b>(+25.87%)</b></td><td>18.40 (+10.64%)</td><td>14.71 (-13.22%)</td><td>7.96 <b>(+106.39%)</b></td><td>9.23 (+11.45%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.09 (n/a)</td><td>0.19 (n/a)</td><td>2445.60 (n/a)</td><td>888.62 (n/a)</td><td>556.90 (n/a)</td><td>392.40 (n/a)</td><td>877.34 (n/a)</td><td>24.05 (n/a)</td><td>16.63 (n/a)</td><td>16.95 (n/a)</td><td>3.86 (n/a)</td><td>8.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.31 (+0.23%)</td><td>0.30 (-0.34%)</td><td>0.31 (+0.06%)</td><td>0.29 (-2.11%)</td><td>0.01 <b>(+69.94%)</b></td><td>86099.60 (+2.16%)</td><td>82751.54 (+0.38%)</td><td>82341.70 (-0.06%)</td><td>81016.80 (-0.22%)</td><td>2082.45 <b>(+73.09%)</b></td><td>212.05 (+0.23%)</td><td>207.71 (-0.34%)</td><td>208.64 (+0.06%)</td><td>199.53 (-2.11%)</td><td>5.13 <b>(+69.94%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84282.20 (n/a)</td><td>82439.40 (n/a)</td><td>82390.40 (n/a)</td><td>81199.40 (n/a)</td><td>1203.07 (n/a)</td><td>211.58 (n/a)</td><td>208.43 (n/a)</td><td>208.52 (n/a)</td><td>203.84 (n/a)</td><td>3.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.17 (+1.22%)</td><td>1.14 (+0.47%)</td><td>1.14 (+0.17%)</td><td>1.12 (+0.40%)</td><td>0.02 (+13.84%)</td><td>22516.30 (-0.40%)</td><td>21989.64 (-0.46%)</td><td>21990.90 (-0.17%)</td><td>21537.20 (-1.21%)</td><td>351.38 (+11.98%)</td><td>797.68 (+1.22%)</td><td>781.43 (+0.47%)</td><td>781.23 (+0.17%)</td><td>763.00 (+0.40%)</td><td>12.43 (+13.84%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22606.10 (n/a)</td><td>22092.02 (n/a)</td><td>22028.90 (n/a)</td><td>21800.00 (n/a)</td><td>313.79 (n/a)</td><td>788.07 (n/a)</td><td>777.77 (n/a)</td><td>779.88 (n/a)</td><td>759.96 (n/a)</td><td>10.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.80 (-0.27%)</td><td>0.79 (-0.05%)</td><td>0.80 (+0.22%)</td><td>0.77 (-0.36%)</td><td>0.01 (+9.66%)</td><td>97586.70 (+0.36%)</td><td>95737.92 (+0.05%)</td><td>94942.00 (-0.22%)</td><td>94855.50 (+0.27%)</td><td>1222.69 (+10.14%)</td><td>724.46 (-0.27%)</td><td>717.88 (-0.05%)</td><td>723.81 (+0.22%)</td><td>704.19 (-0.36%)</td><td>9.09 (+9.66%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97237.40 (n/a)</td><td>95687.10 (n/a)</td><td>95152.20 (n/a)</td><td>94597.40 (n/a)</td><td>1110.11 (n/a)</td><td>726.44 (n/a)</td><td>718.25 (n/a)</td><td>722.21 (n/a)</td><td>706.72 (n/a)</td><td>8.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.77 (-1.46%)</td><td>0.76 (-1.87%)</td><td>0.76 (-1.47%)</td><td>0.74 (-1.69%)</td><td>0.01 (+9.43%)</td><td>101825.60 (+1.72%)</td><td>99690.20 (+1.91%)</td><td>98974.60 (+1.49%)</td><td>98195.90 (+1.48%)</td><td>1514.80 (+12.83%)</td><td>699.82 (-1.46%)</td><td>689.46 (-1.87%)</td><td>694.31 (-1.47%)</td><td>674.87 (-1.69%)</td><td>10.41 (+9.43%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100105.00 (n/a)</td><td>97820.92 (n/a)</td><td>97524.20 (n/a)</td><td>96761.20 (n/a)</td><td>1342.60 (n/a)</td><td>710.20 (n/a)</td><td>702.61 (n/a)</td><td>704.64 (n/a)</td><td>686.47 (n/a)</td><td>9.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.89 (-0.56%)</td><td>0.84 (-5.18%)</td><td>0.88 (-0.97%)</td><td>0.68 <b>(-22.56%)</b></td><td>0.09 <b>(+1277.34%)</b></td><td>111382.60 <b>(+29.13%)</b></td><td>90857.32 (+6.62%)</td><td>85868.80 (+0.98%)</td><td>85005.00 (+0.56%)</td><td>11486.84 <b>(+1699.11%)</b></td><td>808.42 (-0.56%)</td><td>764.71 (-5.18%)</td><td>800.28 (-0.97%)</td><td>616.97 <b>(-22.56%)</b></td><td>82.75 <b>(+1277.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>86259.10 (n/a)</td><td>85214.20 (n/a)</td><td>85031.80 (n/a)</td><td>84530.00 (n/a)</td><td>638.47 (n/a)</td><td>812.96 (n/a)</td><td>806.47 (n/a)</td><td>808.16 (n/a)</td><td>796.66 (n/a)</td><td>6.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.22 (-6.23%)</td><td>2.86 <b>(-28.27%)</b></td><td>2.39 <b>(-32.92%)</b></td><td>2.06 (-3.54%)</td><td>1.33 (-12.02%)</td><td>4320.80 (+3.67%)</td><td>3493.74 <b>(+37.63%)</b></td><td>3730.70 <b>(+49.08%)</b></td><td>1707.40 (+6.64%)</td><td>1043.02 (-1.26%)</td><td>314.44 (-6.23%)</td><td>172.53 <b>(-28.27%)</b></td><td>143.91 <b>(-32.92%)</b></td><td>124.25 (-3.54%)</td><td>80.02 (-12.02%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.57 (n/a)</td><td>3.99 (n/a)</td><td>3.56 (n/a)</td><td>2.14 (n/a)</td><td>1.51 (n/a)</td><td>4167.90 (n/a)</td><td>2538.42 (n/a)</td><td>2502.40 (n/a)</td><td>1601.10 (n/a)</td><td>1056.35 (n/a)</td><td>335.32 (n/a)</td><td>240.54 (n/a)</td><td>214.55 (n/a)</td><td>128.81 (n/a)</td><td>90.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.83 (+4.98%)</td><td>2.64 <b>(-24.17%)</b></td><td>2.22 <b>(-35.78%)</b></td><td>1.89 (-10.98%)</td><td>1.23 <b>(+32.85%)</b></td><td>4725.10 (+12.33%)</td><td>3786.76 <b>(+38.29%)</b></td><td>4006.80 <b>(+55.71%)</b></td><td>1846.50 (-4.74%)</td><td>1127.23 <b>(+28.41%)</b></td><td>290.76 (+4.98%)</td><td>159.20 <b>(-24.17%)</b></td><td>133.99 <b>(-35.78%)</b></td><td>113.62 (-10.98%)</td><td>74.07 <b>(+32.85%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.60 (n/a)</td><td>3.49 (n/a)</td><td>3.46 (n/a)</td><td>2.12 (n/a)</td><td>0.93 (n/a)</td><td>4206.40 (n/a)</td><td>2738.30 (n/a)</td><td>2573.30 (n/a)</td><td>1938.30 (n/a)</td><td>877.84 (n/a)</td><td>276.98 (n/a)</td><td>209.95 (n/a)</td><td>208.63 (n/a)</td><td>127.63 (n/a)</td><td>55.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.78 (-1.93%)</td><td>4.61 (+15.82%)</td><td>4.40 (+8.55%)</td><td>2.99 <b>(+37.26%)</b></td><td>1.19 (-10.37%)</td><td>2982.90 <b>(-27.14%)</b></td><td>2052.52 (-17.24%)</td><td>2024.40 (-7.87%)</td><td>1542.50 (+1.96%)</td><td>591.08 <b>(-38.67%)</b></td><td>348.04 (-1.93%)</td><td>277.68 (+15.82%)</td><td>265.21 (+8.55%)</td><td>179.98 <b>(+37.26%)</b></td><td>71.47 (-10.37%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.89 (n/a)</td><td>3.98 (n/a)</td><td>4.06 (n/a)</td><td>2.18 (n/a)</td><td>1.32 (n/a)</td><td>4094.20 (n/a)</td><td>2480.22 (n/a)</td><td>2197.40 (n/a)</td><td>1512.80 (n/a)</td><td>963.74 (n/a)</td><td>354.89 (n/a)</td><td>239.76 (n/a)</td><td>244.32 (n/a)</td><td>131.13 (n/a)</td><td>79.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.51 (-18.11%)</td><td>4.75 (-12.78%)</td><td>5.01 (-7.23%)</td><td>3.57 (-10.09%)</td><td>0.78 <b>(-27.45%)</b></td><td>9755.40 (+11.23%)</td><td>7524.58 (+13.61%)</td><td>6959.20 (+7.79%)</td><td>6332.00 <b>(+22.12%)</b></td><td>1388.35 (-0.97%)</td><td>339.15 (-18.11%)</td><td>292.42 (-12.78%)</td><td>308.58 (-7.23%)</td><td>220.13 (-10.09%)</td><td>47.90 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>6.72 (n/a)</td><td>5.44 (n/a)</td><td>5.40 (n/a)</td><td>3.98 (n/a)</td><td>1.07 (n/a)</td><td>8770.80 (n/a)</td><td>6622.92 (n/a)</td><td>6456.00 (n/a)</td><td>5185.20 (n/a)</td><td>1401.99 (n/a)</td><td>414.16 (n/a)</td><td>335.28 (n/a)</td><td>332.63 (n/a)</td><td>244.84 (n/a)</td><td>66.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.00 (+12.18%)</td><td>4.99 (+4.81%)</td><td>5.23 (+12.05%)</td><td>3.95 (-2.23%)</td><td>0.90 <b>(+70.46%)</b></td><td>8824.00 (+2.28%)</td><td>7181.58 (-2.94%)</td><td>6664.60 (-10.75%)</td><td>5807.30 (-10.86%)</td><td>1344.93 <b>(+59.33%)</b></td><td>369.79 (+12.18%)</td><td>307.30 (+4.81%)</td><td>322.22 (+12.05%)</td><td>243.37 (-2.23%)</td><td>55.42 <b>(+70.46%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.35 (n/a)</td><td>4.76 (n/a)</td><td>4.67 (n/a)</td><td>4.04 (n/a)</td><td>0.53 (n/a)</td><td>8627.10 (n/a)</td><td>7399.32 (n/a)</td><td>7467.40 (n/a)</td><td>6514.70 (n/a)</td><td>844.10 (n/a)</td><td>329.64 (n/a)</td><td>293.18 (n/a)</td><td>287.58 (n/a)</td><td>248.92 (n/a)</td><td>32.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.17 (-12.34%)</td><td>5.40 (-4.82%)</td><td>5.59 (+10.60%)</td><td>4.34 (+2.31%)</td><td>0.71 <b>(-43.68%)</b></td><td>8040.90 (-2.26%)</td><td>6555.56 (+2.51%)</td><td>6239.30 (-9.59%)</td><td>5655.10 (+14.08%)</td><td>941.25 <b>(-33.16%)</b></td><td>379.74 (-12.34%)</td><td>332.61 (-4.82%)</td><td>344.18 (+10.60%)</td><td>267.07 (+2.31%)</td><td>44.00 <b>(-43.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.03 (n/a)</td><td>5.67 (n/a)</td><td>5.05 (n/a)</td><td>4.24 (n/a)</td><td>1.27 (n/a)</td><td>8226.70 (n/a)</td><td>6394.74 (n/a)</td><td>6901.00 (n/a)</td><td>4957.30 (n/a)</td><td>1408.22 (n/a)</td><td>433.20 (n/a)</td><td>349.47 (n/a)</td><td>311.18 (n/a)</td><td>261.04 (n/a)</td><td>78.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.78 (+1.66%)</td><td>0.77 (+3.70%)</td><td>0.77 (+2.73%)</td><td>0.74 (+8.61%)</td><td>0.02 <b>(-53.61%)</b></td><td>102081.10 (-7.93%)</td><td>98693.10 (-3.70%)</td><td>98420.40 (-2.66%)</td><td>97159.60 (-1.63%)</td><td>1994.22 <b>(-58.34%)</b></td><td>707.28 (+1.66%)</td><td>696.52 (+3.70%)</td><td>698.22 (+2.73%)</td><td>673.19 (+8.61%)</td><td>13.79 <b>(-53.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.75 (n/a)</td><td>0.68 (n/a)</td><td>0.03 (n/a)</td><td>110868.60 (n/a)</td><td>102485.80 (n/a)</td><td>101104.80 (n/a)</td><td>98769.60 (n/a)</td><td>4786.52 (n/a)</td><td>695.76 (n/a)</td><td>671.64 (n/a)</td><td>679.69 (n/a)</td><td>619.83 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.79 (+1.63%)</td><td>0.77 (+2.33%)</td><td>0.77 (+2.85%)</td><td>0.76 (+3.87%)</td><td>0.01 <b>(-25.48%)</b></td><td>99901.80 (-3.72%)</td><td>97948.38 (-2.30%)</td><td>97553.40 (-2.77%)</td><td>95783.90 (-1.61%)</td><td>1817.16 <b>(-29.11%)</b></td><td>717.44 (+1.63%)</td><td>701.78 (+2.33%)</td><td>704.43 (+2.85%)</td><td>687.87 (+3.87%)</td><td>13.01 <b>(-25.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103765.10 (n/a)</td><td>100253.26 (n/a)</td><td>100330.80 (n/a)</td><td>97347.20 (n/a)</td><td>2563.46 (n/a)</td><td>705.92 (n/a)</td><td>685.82 (n/a)</td><td>684.93 (n/a)</td><td>662.26 (n/a)</td><td>17.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.90 (+0.56%)</td><td>0.89 (+0.43%)</td><td>0.89 (+0.65%)</td><td>0.87 (-1.05%)</td><td>0.01 <b>(+156.09%)</b></td><td>86307.30 (+1.06%)</td><td>84597.48 (-0.42%)</td><td>84369.20 (-0.65%)</td><td>83913.20 (-0.56%)</td><td>980.76 <b>(+157.83%)</b></td><td>818.94 (+0.56%)</td><td>812.40 (+0.43%)</td><td>814.51 (+0.65%)</td><td>796.22 (-1.05%)</td><td>9.29 <b>(+156.09%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>85402.80 (n/a)</td><td>84957.84 (n/a)</td><td>84921.00 (n/a)</td><td>84384.50 (n/a)</td><td>380.39 (n/a)</td><td>814.36 (n/a)</td><td>808.88 (n/a)</td><td>809.22 (n/a)</td><td>804.65 (n/a)</td><td>3.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.25 <b>(+41.39%)</b></td><td>2.94 <b>(+20.96%)</b></td><td>3.62 <b>(+32.52%)</b></td><td>1.41 (-12.59%)</td><td>1.31 <b>(+107.81%)</b></td><td>5698.10 (+14.41%)</td><td>3367.82 (-4.53%)</td><td>2225.70 <b>(-24.54%)</b></td><td>1897.50 <b>(-29.27%)</b></td><td>1780.24 <b>(+73.05%)</b></td><td>1114.07 <b>(+41.39%)</b></td><td>771.11 <b>(+20.96%)</b></td><td>949.77 <b>(+32.52%)</b></td><td>370.99 (-12.59%)</td><td>342.90 <b>(+107.81%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.00 (n/a)</td><td>2.43 (n/a)</td><td>2.73 (n/a)</td><td>1.62 (n/a)</td><td>0.63 (n/a)</td><td>4980.40 (n/a)</td><td>3527.64 (n/a)</td><td>2949.50 (n/a)</td><td>2682.90 (n/a)</td><td>1028.76 (n/a)</td><td>787.91 (n/a)</td><td>637.49 (n/a)</td><td>716.71 (n/a)</td><td>424.45 (n/a)</td><td>165.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.28 (+9.10%)</td><td>0.21 (+1.65%)</td><td>0.22 (+7.90%)</td><td>0.17 (-1.95%)</td><td>0.05 <b>(+48.69%)</b></td><td>7433.30 (+1.99%)</td><td>6085.52 (+0.38%)</td><td>5634.10 (-7.32%)</td><td>4456.60 (-8.34%)</td><td>1295.36 <b>(+46.16%)</b></td><td>15.06 (+9.10%)</td><td>11.45 (+1.65%)</td><td>11.91 (+7.90%)</td><td>9.03 (-1.95%)</td><td>2.51 <b>(+48.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7288.60 (n/a)</td><td>6062.78 (n/a)</td><td>6079.10 (n/a)</td><td>4862.20 (n/a)</td><td>886.26 (n/a)</td><td>13.80 (n/a)</td><td>11.26 (n/a)</td><td>11.04 (n/a)</td><td>9.21 (n/a)</td><td>1.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.73 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>3.42 (n/a)</td><td>0.12 (n/a)</td><td>3.73 (n/a)</td><td>3.52 (n/a)</td><td>3.49 (n/a)</td><td>3.42 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.84 (-9.23%)</td><td>6.52 (-5.61%)</td><td>6.68 (-1.02%)</td><td>5.93 (-10.58%)</td><td>0.39 (+7.99%)</td><td>6.83 (-9.23%)</td><td>6.51 (-5.61%)</td><td>6.68 (-1.02%)</td><td>5.93 (-10.58%)</td><td>0.39 (+7.99%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.53 (n/a)</td><td>6.90 (n/a)</td><td>6.75 (n/a)</td><td>6.63 (n/a)</td><td>0.36 (n/a)</td><td>7.53 (n/a)</td><td>6.90 (n/a)</td><td>6.74 (n/a)</td><td>6.63 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>14.06 (+3.90%)</td><td>10.26 (+1.44%)</td><td>8.27 (-11.71%)</td><td>7.45 (+4.24%)</td><td>3.16 (+17.77%)</td><td>14.05 (+3.90%)</td><td>10.26 (+1.44%)</td><td>8.26 (-11.71%)</td><td>7.45 (+4.24%)</td><td>3.16 (+17.77%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>13.53 (n/a)</td><td>10.12 (n/a)</td><td>9.36 (n/a)</td><td>7.15 (n/a)</td><td>2.68 (n/a)</td><td>13.52 (n/a)</td><td>10.11 (n/a)</td><td>9.36 (n/a)</td><td>7.15 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.82 (n/a)</td><td>3.49 (n/a)</td><td>3.37 (n/a)</td><td>3.24 (n/a)</td><td>0.27 (n/a)</td><td>3.82 (n/a)</td><td>3.48 (n/a)</td><td>3.37 (n/a)</td><td>3.24 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.83 (-7.58%)</td><td>6.37 (-3.17%)</td><td>6.78 (+3.41%)</td><td>5.64 (-6.62%)</td><td>0.60 (+6.73%)</td><td>6.83 (-7.58%)</td><td>6.37 (-3.17%)</td><td>6.78 (+3.41%)</td><td>5.64 (-6.62%)</td><td>0.59 (+6.73%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.40 (n/a)</td><td>6.58 (n/a)</td><td>6.56 (n/a)</td><td>6.04 (n/a)</td><td>0.56 (n/a)</td><td>7.39 (n/a)</td><td>6.57 (n/a)</td><td>6.56 (n/a)</td><td>6.03 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>13.69 (-4.17%)</td><td>10.88 (+5.04%)</td><td>13.07 <b>(+37.11%)</b></td><td>6.27 (-12.10%)</td><td>3.38 (+1.96%)</td><td>13.69 (-4.17%)</td><td>10.87 (+5.04%)</td><td>13.06 <b>(+37.11%)</b></td><td>6.26 (-12.10%)</td><td>3.38 (+1.96%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>14.29 (n/a)</td><td>10.36 (n/a)</td><td>9.53 (n/a)</td><td>7.13 (n/a)</td><td>3.32 (n/a)</td><td>14.28 (n/a)</td><td>10.35 (n/a)</td><td>9.52 (n/a)</td><td>7.13 (n/a)</td><td>3.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.84 (+0.47%)</td><td>1.79 (-10.28%)</td><td>1.45 (-16.59%)</td><td>1.17 <b>(+23.63%)</b></td><td>0.73 (-9.44%)</td><td>2.83 (+0.47%)</td><td>1.79 (-10.28%)</td><td>1.45 (-16.59%)</td><td>1.16 <b>(+23.63%)</b></td><td>0.73 (-9.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.82 (n/a)</td><td>1.99 (n/a)</td><td>1.74 (n/a)</td><td>0.94 (n/a)</td><td>0.81 (n/a)</td><td>2.82 (n/a)</td><td>1.99 (n/a)</td><td>1.74 (n/a)</td><td>0.94 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.54 (+0.76%)</td><td>0.49 <b>(+191.96%)</b></td><td>0.52 <b>(+573.83%)</b></td><td>0.38 <b>(+395.52%)</b></td><td>0.07 <b>(-67.00%)</b></td><td>0.53 (+0.76%)</td><td>0.48 <b>(+191.96%)</b></td><td>0.51 <b>(+573.83%)</b></td><td>0.37 <b>(+395.52%)</b></td><td>0.07 <b>(-67.00%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.53 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.52 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.73 (-1.96%)</td><td>0.50 (-11.80%)</td><td>0.44 <b>(-32.32%)</b></td><td>0.34 <b>(+20.64%)</b></td><td>0.18 (-4.67%)</td><td>0.72 (-1.96%)</td><td>0.50 (-11.80%)</td><td>0.44 <b>(-32.32%)</b></td><td>0.34 <b>(+20.64%)</b></td><td>0.17 (-4.67%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.75 (n/a)</td><td>0.57 (n/a)</td><td>0.65 (n/a)</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.74 (n/a)</td><td>0.56 (n/a)</td><td>0.65 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.68 (+8.13%)</td><td>1.01 <b>(-38.68%)</b></td><td>0.73 <b>(-60.15%)</b></td><td>0.44 <b>(-39.77%)</b></td><td>0.94 (+9.43%)</td><td>2.64 (+8.13%)</td><td>1.00 <b>(-38.68%)</b></td><td>0.72 <b>(-60.15%)</b></td><td>0.43 <b>(-39.77%)</b></td><td>0.93 (+9.43%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.48 (n/a)</td><td>1.65 (n/a)</td><td>1.83 (n/a)</td><td>0.72 (n/a)</td><td>0.86 (n/a)</td><td>2.44 (n/a)</td><td>1.63 (n/a)</td><td>1.80 (n/a)</td><td>0.71 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.10 (n/a)</td><td>351.80 (n/a)</td><td>267.50 (n/a)</td><td>227.50 (n/a)</td><td>145.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.40 (n/a)</td><td>329.86 (n/a)</td><td>282.80 (n/a)</td><td>228.20 (n/a)</td><td>138.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>702.90 (n/a)</td><td>462.64 (n/a)</td><td>426.20 (n/a)</td><td>288.70 (n/a)</td><td>155.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1146.70 (n/a)</td><td>639.20 (n/a)</td><td>562.60 (n/a)</td><td>391.00 (n/a)</td><td>293.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2399.60 (n/a)</td><td>887.42 (n/a)</td><td>547.10 (n/a)</td><td>379.70 (n/a)</td><td>848.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>668.80 (n/a)</td><td>530.08 (n/a)</td><td>536.80 (n/a)</td><td>367.90 (n/a)</td><td>108.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.30 (n/a)</td><td>291.10 (n/a)</td><td>251.20 (n/a)</td><td>162.40 (n/a)</td><td>128.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.40 (n/a)</td><td>259.26 (n/a)</td><td>264.20 (n/a)</td><td>199.20 (n/a)</td><td>38.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>444.70 (n/a)</td><td>295.72 (n/a)</td><td>268.00 (n/a)</td><td>236.70 (n/a)</td><td>85.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1017.50 (n/a)</td><td>536.44 (n/a)</td><td>503.00 (n/a)</td><td>242.50 (n/a)</td><td>324.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1907.40 (n/a)</td><td>695.90 (n/a)</td><td>414.20 (n/a)</td><td>316.40 (n/a)</td><td>682.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>972.80 (n/a)</td><td>531.98 (n/a)</td><td>493.60 (n/a)</td><td>317.70 (n/a)</td><td>262.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>500.72 (n/a)</td><td>489.50 (n/a)</td><td>370.60 (n/a)</td><td>92.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.10 (n/a)</td><td>404.86 (n/a)</td><td>358.10 (n/a)</td><td>280.70 (n/a)</td><td>107.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1967.90 (n/a)</td><td>679.80 (n/a)</td><td>381.80 (n/a)</td><td>202.10 (n/a)</td><td>736.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.40 (n/a)</td><td>382.62 (n/a)</td><td>317.70 (n/a)</td><td>241.50 (n/a)</td><td>155.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>548.60 (n/a)</td><td>373.74 (n/a)</td><td>301.90 (n/a)</td><td>226.80 (n/a)</td><td>138.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.50 (n/a)</td><td>433.82 (n/a)</td><td>401.30 (n/a)</td><td>311.50 (n/a)</td><td>106.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>641.50 (n/a)</td><td>415.12 (n/a)</td><td>394.50 (n/a)</td><td>243.10 (n/a)</td><td>166.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>688.40 (n/a)</td><td>398.12 (n/a)</td><td>367.80 (n/a)</td><td>255.70 (n/a)</td><td>170.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>587.40 (n/a)</td><td>430.20 (n/a)</td><td>493.40 (n/a)</td><td>240.10 (n/a)</td><td>144.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>666.30 (n/a)</td><td>454.54 (n/a)</td><td>471.50 (n/a)</td><td>268.80 (n/a)</td><td>166.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>573.70 (n/a)</td><td>506.92 (n/a)</td><td>540.30 (n/a)</td><td>356.80 (n/a)</td><td>86.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>571.60 (n/a)</td><td>458.70 (n/a)</td><td>480.70 (n/a)</td><td>308.80 (n/a)</td><td>101.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+22.34%)</b></td><td>0.01 <b>(+27.94%)</b></td><td>0.01 <b>(+38.76%)</b></td><td>0.01 (-1.20%)</td><td>0.00 <b>(+44.44%)</b></td><td>608.60 (+1.21%)</td><td>399.92 (-17.73%)</td><td>374.40 <b>(-27.93%)</b></td><td>233.00 (-18.27%)</td><td>152.58 <b>(+27.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.30 (n/a)</td><td>486.12 (n/a)</td><td>519.50 (n/a)</td><td>285.10 (n/a)</td><td>119.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+3.94%)</td><td>0.01 (-7.89%)</td><td>0.01 (-18.86%)</td><td>0.01 <b>(-20.39%)</b></td><td>0.00 <b>(+39.62%)</b></td><td>632.50 <b>(+25.62%)</b></td><td>460.92 (+16.99%)</td><td>496.90 <b>(+23.24%)</b></td><td>273.00 (-3.81%)</td><td>175.62 <b>(+67.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>503.50 (n/a)</td><td>393.98 (n/a)</td><td>403.20 (n/a)</td><td>283.80 (n/a)</td><td>104.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+11.75%)</td><td>0.01 (+0.66%)</td><td>0.01 (-7.19%)</td><td>0.01 (-18.35%)</td><td>0.01 (+18.97%)</td><td>705.40 <b>(+22.49%)</b></td><td>398.02 (+5.30%)</td><td>292.40 (+7.74%)</td><td>231.70 (-10.54%)</td><td>202.66 <b>(+31.82%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.90 (n/a)</td><td>377.98 (n/a)</td><td>271.40 (n/a)</td><td>259.00 (n/a)</td><td>153.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+7.61%)</td><td>0.01 (+13.95%)</td><td>0.01 (-15.34%)</td><td>0.01 (+7.20%)</td><td>0.01 <b>(+21.67%)</b></td><td>593.00 (-6.72%)</td><td>450.88 (-7.39%)</td><td>579.40 (+18.12%)</td><td>216.80 (-7.07%)</td><td>186.41 (+17.40%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.70 (n/a)</td><td>486.88 (n/a)</td><td>490.50 (n/a)</td><td>233.30 (n/a)</td><td>158.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+23.90%)</b></td><td>0.01 <b>(+25.30%)</b></td><td>0.02 <b>(+60.28%)</b></td><td>0.01 <b>(-40.87%)</b></td><td>0.00 <b>(+106.96%)</b></td><td>791.30 <b>(+69.12%)</b></td><td>367.74 (-5.60%)</td><td>259.70 <b>(-37.60%)</b></td><td>234.80 (-19.31%)</td><td>238.22 <b>(+197.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.90 (n/a)</td><td>389.56 (n/a)</td><td>416.20 (n/a)</td><td>291.00 (n/a)</td><td>80.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+66.11%)</b></td><td>0.01 <b>(+60.28%)</b></td><td>0.01 <b>(+80.61%)</b></td><td>0.01 <b>(+30.95%)</b></td><td>0.00 <b>(+117.49%)</b></td><td>468.40 <b>(-23.63%)</b></td><td>341.14 <b>(-35.44%)</b></td><td>306.60 <b>(-44.63%)</b></td><td>227.50 <b>(-39.80%)</b></td><td>94.21 (+5.57%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.30 (n/a)</td><td>528.44 (n/a)</td><td>553.70 (n/a)</td><td>377.90 (n/a)</td><td>89.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+22.89%)</b></td><td>0.03 <b>(+46.00%)</b></td><td>0.03 <b>(+45.84%)</b></td><td>0.03 <b>(+64.59%)</b></td><td>0.00 <b>(-34.43%)</b></td><td>298.70 <b>(-39.24%)</b></td><td>256.90 <b>(-33.81%)</b></td><td>243.50 <b>(-31.43%)</b></td><td>234.10 (-18.60%)</td><td>28.02 <b>(-69.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.60 (n/a)</td><td>388.10 (n/a)</td><td>355.10 (n/a)</td><td>287.60 (n/a)</td><td>90.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(-25.36%)</b></td><td>0.03 (-4.69%)</td><td>0.03 (-7.16%)</td><td>0.02 (+18.69%)</td><td>0.01 <b>(-45.52%)</b></td><td>434.20 (-15.75%)</td><td>333.78 (-3.57%)</td><td>326.90 (+7.71%)</td><td>240.20 <b>(+33.97%)</b></td><td>81.21 <b>(-38.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.40 (n/a)</td><td>346.14 (n/a)</td><td>303.50 (n/a)</td><td>179.30 (n/a)</td><td>132.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(-33.60%)</b></td><td>0.02 <b>(-30.05%)</b></td><td>0.03 (-17.79%)</td><td>0.02 <b>(-38.58%)</b></td><td>0.01 <b>(-24.39%)</b></td><td>480.90 <b>(+62.85%)</b></td><td>354.16 <b>(+45.88%)</b></td><td>322.80 <b>(+21.67%)</b></td><td>244.90 <b>(+50.62%)</b></td><td>100.52 <b>(+95.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>295.30 (n/a)</td><td>242.78 (n/a)</td><td>265.30 (n/a)</td><td>162.60 (n/a)</td><td>51.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(-22.47%)</b></td><td>0.03 (+3.90%)</td><td>0.03 (+11.20%)</td><td>0.01 (-19.73%)</td><td>0.01 <b>(-20.83%)</b></td><td>637.00 <b>(+24.56%)</b></td><td>334.46 (-3.17%)</td><td>261.60 (-10.07%)</td><td>242.50 <b>(+28.99%)</b></td><td>169.87 <b>(+27.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>345.42 (n/a)</td><td>290.90 (n/a)</td><td>188.00 (n/a)</td><td>132.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(-25.72%)</b></td><td>0.02 <b>(-27.60%)</b></td><td>0.02 <b>(-37.59%)</b></td><td>0.01 <b>(-42.52%)</b></td><td>0.01 (+7.12%)</td><td>760.70 <b>(+73.99%)</b></td><td>474.76 <b>(+51.56%)</b></td><td>465.00 <b>(+60.23%)</b></td><td>273.90 <b>(+34.59%)</b></td><td>209.03 <b>(+131.21%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>437.20 (n/a)</td><td>313.24 (n/a)</td><td>290.20 (n/a)</td><td>203.50 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-2.87%)</td><td>0.02 (-4.19%)</td><td>0.02 <b>(-24.59%)</b></td><td>0.01 <b>(+74.00%)</b></td><td>0.01 (-13.01%)</td><td>675.90 <b>(-42.53%)</b></td><td>487.12 (-8.60%)</td><td>537.90 <b>(+32.62%)</b></td><td>289.70 (+2.99%)</td><td>163.44 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1176.10 (n/a)</td><td>532.96 (n/a)</td><td>405.60 (n/a)</td><td>281.30 (n/a)</td><td>363.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-3.58%)</td><td>0.02 (-2.44%)</td><td>0.02 (+5.34%)</td><td>0.02 <b>(+57.89%)</b></td><td>0.01 <b>(-29.80%)</b></td><td>505.80 <b>(-36.66%)</b></td><td>440.34 (-7.23%)</td><td>470.90 (-5.06%)</td><td>269.40 (+3.74%)</td><td>97.24 <b>(-54.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>798.50 (n/a)</td><td>474.68 (n/a)</td><td>496.00 (n/a)</td><td>259.70 (n/a)</td><td>211.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+45.46%)</b></td><td>0.02 (+13.74%)</td><td>0.02 (-0.99%)</td><td>0.01 (+10.75%)</td><td>0.01 <b>(+107.44%)</b></td><td>590.10 (-9.72%)</td><td>463.56 (-7.65%)</td><td>494.90 (+1.00%)</td><td>256.20 <b>(-31.24%)</b></td><td>125.03 (+19.88%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.60 (n/a)</td><td>501.98 (n/a)</td><td>490.00 (n/a)</td><td>372.60 (n/a)</td><td>104.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(+20.16%)</b></td><td>0.05 <b>(+45.85%)</b></td><td>0.05 <b>(+67.49%)</b></td><td>0.04 <b>(+20.66%)</b></td><td>0.01 (+7.35%)</td><td>428.70 (-17.13%)</td><td>312.78 <b>(-31.98%)</b></td><td>298.00 <b>(-40.30%)</b></td><td>246.30 (-16.79%)</td><td>71.33 <b>(-22.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>517.30 (n/a)</td><td>459.86 (n/a)</td><td>499.20 (n/a)</td><td>296.00 (n/a)</td><td>92.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+19.16%)</td><td>0.05 <b>(+26.01%)</b></td><td>0.04 (+7.71%)</td><td>0.03 <b>(+240.14%)</b></td><td>0.02 (-2.98%)</td><td>545.40 <b>(-70.60%)</b></td><td>395.78 <b>(-42.45%)</b></td><td>414.60 (-7.17%)</td><td>233.90 (-16.10%)</td><td>148.51 <b>(-77.54%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1855.20 (n/a)</td><td>687.68 (n/a)</td><td>446.60 (n/a)</td><td>278.80 (n/a)</td><td>661.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(+31.31%)</b></td><td>0.04 (+17.17%)</td><td>0.04 (-6.22%)</td><td>0.02 <b>(+53.64%)</b></td><td>0.02 <b>(+36.78%)</b></td><td>719.80 <b>(-34.92%)</b></td><td>443.88 (-17.33%)</td><td>443.10 (+6.64%)</td><td>227.70 <b>(-23.85%)</b></td><td>193.36 <b>(-40.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1106.00 (n/a)</td><td>536.92 (n/a)</td><td>415.50 (n/a)</td><td>299.00 (n/a)</td><td>323.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+18.77%)</td><td>0.05 (+2.89%)</td><td>0.04 <b>(-27.56%)</b></td><td>0.03 (-4.69%)</td><td>0.02 <b>(+52.03%)</b></td><td>620.80 (+4.92%)</td><td>406.94 (+3.90%)</td><td>441.00 <b>(+38.03%)</b></td><td>229.10 (-15.80%)</td><td>165.52 <b>(+25.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>391.68 (n/a)</td><td>319.50 (n/a)</td><td>272.10 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(+80.34%)</b></td><td>0.05 <b>(+68.96%)</b></td><td>0.05 <b>(+85.87%)</b></td><td>0.03 <b>(+41.04%)</b></td><td>0.01 <b>(+108.33%)</b></td><td>545.30 <b>(-29.10%)</b></td><td>353.26 <b>(-38.80%)</b></td><td>316.70 <b>(-46.19%)</b></td><td>241.50 <b>(-44.55%)</b></td><td>119.10 (-13.49%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>769.10 (n/a)</td><td>577.24 (n/a)</td><td>588.60 (n/a)</td><td>435.50 (n/a)</td><td>137.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 <b>(+33.82%)</b></td><td>0.05 <b>(+37.90%)</b></td><td>0.04 <b>(+29.54%)</b></td><td>0.03 <b>(+46.96%)</b></td><td>0.02 <b>(+28.82%)</b></td><td>487.80 <b>(-31.95%)</b></td><td>384.10 <b>(-28.95%)</b></td><td>416.70 <b>(-22.79%)</b></td><td>181.40 <b>(-25.26%)</b></td><td>124.64 <b>(-34.49%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>716.80 (n/a)</td><td>540.62 (n/a)</td><td>539.70 (n/a)</td><td>242.70 (n/a)</td><td>190.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 <b>(+25.73%)</b></td><td>0.10 (+8.70%)</td><td>0.11 (+11.55%)</td><td>0.05 (+2.89%)</td><td>0.04 <b>(+73.47%)</b></td><td>643.50 (-2.81%)</td><td>403.36 (+1.13%)</td><td>304.60 (-10.36%)</td><td>237.10 <b>(-20.46%)</b></td><td>194.65 <b>(+29.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>662.10 (n/a)</td><td>398.86 (n/a)</td><td>339.80 (n/a)</td><td>298.10 (n/a)</td><td>150.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (-1.87%)</td><td>0.08 (-7.51%)</td><td>0.07 <b>(-27.63%)</b></td><td>0.06 <b>(+20.34%)</b></td><td>0.02 (-13.04%)</td><td>542.80 (-16.90%)</td><td>414.10 (+4.44%)</td><td>440.80 <b>(+38.18%)</b></td><td>291.60 (+1.89%)</td><td>112.63 <b>(-27.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>653.20 (n/a)</td><td>396.50 (n/a)</td><td>319.00 (n/a)</td><td>286.20 (n/a)</td><td>155.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (-3.37%)</td><td>0.10 (-2.11%)</td><td>0.12 (+5.15%)</td><td>0.05 (-3.21%)</td><td>0.03 (+4.81%)</td><td>628.60 (+3.30%)</td><td>387.38 (+3.73%)</td><td>281.20 (-4.90%)</td><td>269.40 (+3.50%)</td><td>162.61 (+9.09%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.50 (n/a)</td><td>373.46 (n/a)</td><td>295.70 (n/a)</td><td>260.30 (n/a)</td><td>149.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (-11.24%)</td><td>0.10 (+4.42%)</td><td>0.12 <b>(+51.85%)</b></td><td>0.05 (-18.14%)</td><td>0.04 (+7.20%)</td><td>619.10 <b>(+22.16%)</b></td><td>396.42 (+1.99%)</td><td>279.40 <b>(-34.15%)</b></td><td>240.70 (+12.69%)</td><td>181.19 <b>(+58.64%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>506.80 (n/a)</td><td>388.68 (n/a)</td><td>424.30 (n/a)</td><td>213.60 (n/a)</td><td>114.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 <b>(+30.56%)</b></td><td>0.08 (+18.53%)</td><td>0.10 <b>(+42.35%)</b></td><td>0.02 <b>(-53.52%)</b></td><td>0.05 <b>(+190.22%)</b></td><td>1344.50 <b>(+115.15%)</b></td><td>573.16 <b>(+20.03%)</b></td><td>332.90 <b>(-29.75%)</b></td><td>261.40 <b>(-23.41%)</b></td><td>462.11 <b>(+358.38%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>624.90 (n/a)</td><td>477.52 (n/a)</td><td>473.90 (n/a)</td><td>341.30 (n/a)</td><td>100.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-7.73%)</td><td>0.02 (+14.82%)</td><td>0.01 (+7.64%)</td><td>0.01 <b>(+53.12%)</b></td><td>0.00 <b>(-76.56%)</b></td><td>276.60 <b>(-34.70%)</b></td><td>269.26 (-17.04%)</td><td>274.60 (-7.10%)</td><td>246.10 (+8.37%)</td><td>12.99 <b>(-83.87%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>423.60 (n/a)</td><td>324.56 (n/a)</td><td>295.60 (n/a)</td><td>227.10 (n/a)</td><td>80.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+10.46%)</td><td>0.02 <b>(+21.43%)</b></td><td>0.02 (+13.21%)</td><td>0.01 <b>(+33.29%)</b></td><td>0.00 <b>(-31.73%)</b></td><td>358.80 <b>(-24.98%)</b></td><td>278.38 <b>(-21.17%)</b></td><td>252.40 (-11.66%)</td><td>241.60 (-9.45%)</td><td>48.11 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.30 (n/a)</td><td>353.16 (n/a)</td><td>285.70 (n/a)</td><td>266.80 (n/a)</td><td>103.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+21.62%)</b></td><td>0.01 (+17.50%)</td><td>0.01 <b>(+64.72%)</b></td><td>0.00 <b>(-78.37%)</b></td><td>0.01 <b>(+135.88%)</b></td><td>2443.40 <b>(+362.24%)</b></td><td>756.64 <b>(+64.71%)</b></td><td>307.80 <b>(-39.29%)</b></td><td>240.80 (-17.79%)</td><td>949.37 <b>(+860.09%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.60 (n/a)</td><td>459.38 (n/a)</td><td>507.00 (n/a)</td><td>292.90 (n/a)</td><td>98.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-9.60%)</td><td>0.01 (-1.03%)</td><td>0.01 (-4.19%)</td><td>0.00 <b>(-39.88%)</b></td><td>0.01 (+12.77%)</td><td>1055.30 <b>(+66.35%)</b></td><td>465.92 (+16.94%)</td><td>340.00 (+4.39%)</td><td>242.80 (+10.62%)</td><td>339.79 <b>(+100.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.40 (n/a)</td><td>398.44 (n/a)</td><td>325.70 (n/a)</td><td>219.50 (n/a)</td><td>169.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(-20.29%)</b></td><td>0.01 (+3.98%)</td><td>0.01 (-15.74%)</td><td>0.01 <b>(+261.09%)</b></td><td>0.01 <b>(-32.77%)</b></td><td>512.50 <b>(-72.31%)</b></td><td>394.50 <b>(-38.85%)</b></td><td>476.60 (+18.68%)</td><td>228.70 <b>(+25.45%)</b></td><td>145.36 <b>(-78.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1850.60 (n/a)</td><td>645.14 (n/a)</td><td>401.60 (n/a)</td><td>182.30 (n/a)</td><td>684.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+3.75%)</td><td>0.01 (-8.59%)</td><td>0.01 <b>(-33.88%)</b></td><td>0.01 (-4.93%)</td><td>0.01 (+12.13%)</td><td>576.10 (+5.17%)</td><td>418.04 (+12.37%)</td><td>475.40 <b>(+51.21%)</b></td><td>219.60 (-3.64%)</td><td>160.58 (+10.60%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.80 (n/a)</td><td>372.02 (n/a)</td><td>314.40 (n/a)</td><td>227.90 (n/a)</td><td>145.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(-30.12%)</b></td><td>0.01 <b>(-27.27%)</b></td><td>0.01 (-19.89%)</td><td>0.00 <b>(-39.76%)</b></td><td>0.01 <b>(-31.09%)</b></td><td>2133.60 <b>(+66.00%)</b></td><td>796.60 <b>(+46.61%)</b></td><td>583.80 <b>(+24.82%)</b></td><td>229.20 <b>(+43.07%)</b></td><td>762.68 <b>(+74.54%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1285.30 (n/a)</td><td>543.36 (n/a)</td><td>467.70 (n/a)</td><td>160.20 (n/a)</td><td>436.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (-14.07%)</td><td>0.01 (-18.42%)</td><td>0.01 (-7.87%)</td><td>0.00 <b>(-47.30%)</b></td><td>0.00 (-8.27%)</td><td>1139.40 <b>(+89.77%)</b></td><td>563.88 <b>(+34.69%)</b></td><td>504.90 (+8.53%)</td><td>280.40 (+16.35%)</td><td>335.15 <b>(+122.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>600.40 (n/a)</td><td>418.66 (n/a)</td><td>465.20 (n/a)</td><td>241.00 (n/a)</td><td>150.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-11.29%)</td><td>0.01 (-11.77%)</td><td>0.01 (-13.89%)</td><td>0.01 (-1.31%)</td><td>0.00 <b>(-22.02%)</b></td><td>537.40 (+1.32%)</td><td>442.56 (+9.72%)</td><td>494.90 (+16.15%)</td><td>264.30 (+12.71%)</td><td>109.11 (-16.01%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.40 (n/a)</td><td>403.34 (n/a)</td><td>426.10 (n/a)</td><td>234.50 (n/a)</td><td>129.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-19.42%)</td><td>0.01 (+2.36%)</td><td>0.01 (+8.49%)</td><td>0.01 (-10.29%)</td><td>0.00 <b>(-24.41%)</b></td><td>562.50 (+11.47%)</td><td>388.76 (-4.75%)</td><td>413.80 (-7.84%)</td><td>232.30 <b>(+24.09%)</b></td><td>137.01 (+7.26%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>504.60 (n/a)</td><td>408.14 (n/a)</td><td>449.00 (n/a)</td><td>187.20 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (+19.00%)</td><td>0.01 <b>(+25.02%)</b></td><td>0.01 <b>(+28.76%)</b></td><td>0.01 <b>(+32.06%)</b></td><td>0.00 (+1.44%)</td><td>613.00 <b>(-24.27%)</b></td><td>378.32 <b>(-22.17%)</b></td><td>331.60 <b>(-22.32%)</b></td><td>289.80 (-15.98%)</td><td>132.81 <b>(-30.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>809.50 (n/a)</td><td>486.06 (n/a)</td><td>426.90 (n/a)</td><td>344.90 (n/a)</td><td>192.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-14.31%)</td><td>0.02 (-19.35%)</td><td>0.02 (-12.02%)</td><td>0.01 <b>(-25.22%)</b></td><td>0.01 (-8.30%)</td><td>613.30 <b>(+33.70%)</b></td><td>431.74 <b>(+26.59%)</b></td><td>374.40 (+13.66%)</td><td>286.10 (+16.68%)</td><td>139.06 <b>(+49.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.70 (n/a)</td><td>341.06 (n/a)</td><td>329.40 (n/a)</td><td>245.20 (n/a)</td><td>93.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-18.27%)</td><td>0.02 <b>(-20.59%)</b></td><td>0.02 <b>(-23.26%)</b></td><td>0.02 <b>(-23.19%)</b></td><td>0.00 <b>(-22.05%)</b></td><td>416.90 <b>(+30.20%)</b></td><td>342.48 <b>(+25.83%)</b></td><td>346.70 <b>(+30.34%)</b></td><td>280.20 <b>(+22.36%)</b></td><td>53.68 <b>(+23.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>320.20 (n/a)</td><td>272.18 (n/a)</td><td>266.00 (n/a)</td><td>229.00 (n/a)</td><td>43.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (+1.06%)</td><td>0.02 (+2.48%)</td><td>0.02 (-11.53%)</td><td>0.01 <b>(+65.19%)</b></td><td>0.01 <b>(-20.72%)</b></td><td>651.70 <b>(-39.46%)</b></td><td>416.30 (-16.60%)</td><td>344.70 (+13.02%)</td><td>268.60 (-1.07%)</td><td>167.58 <b>(-51.28%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1076.50 (n/a)</td><td>499.18 (n/a)</td><td>305.00 (n/a)</td><td>271.50 (n/a)</td><td>343.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 <b>(+26.50%)</b></td><td>0.02 (+3.10%)</td><td>0.02 (-0.74%)</td><td>0.02 (+2.03%)</td><td>0.01 <b>(+38.89%)</b></td><td>472.80 (-1.99%)</td><td>362.26 (-0.83%)</td><td>358.40 (+0.76%)</td><td>218.20 <b>(-20.94%)</b></td><td>97.57 (+7.70%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.40 (n/a)</td><td>365.28 (n/a)</td><td>355.70 (n/a)</td><td>276.00 (n/a)</td><td>90.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+39.49%)</b></td><td>0.02 <b>(+41.34%)</b></td><td>0.03 <b>(+44.10%)</b></td><td>0.01 (-0.62%)</td><td>0.01 <b>(+107.74%)</b></td><td>595.80 (+0.62%)</td><td>357.64 <b>(-25.00%)</b></td><td>322.10 <b>(-30.61%)</b></td><td>265.90 <b>(-28.31%)</b></td><td>136.98 <b>(+51.70%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.10 (n/a)</td><td>476.88 (n/a)</td><td>464.20 (n/a)</td><td>370.90 (n/a)</td><td>90.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-1.95%)</td><td>0.03 (-13.28%)</td><td>0.03 (-3.36%)</td><td>0.01 <b>(-49.31%)</b></td><td>0.01 <b>(+49.23%)</b></td><td>941.00 <b>(+97.32%)</b></td><td>419.26 <b>(+38.84%)</b></td><td>277.70 (+3.50%)</td><td>238.60 (+1.97%)</td><td>296.02 <b>(+199.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.90 (n/a)</td><td>301.98 (n/a)</td><td>268.30 (n/a)</td><td>234.00 (n/a)</td><td>98.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-17.41%)</td><td>0.02 <b>(-22.13%)</b></td><td>0.02 (-13.95%)</td><td>0.01 <b>(-22.43%)</b></td><td>0.01 <b>(-22.51%)</b></td><td>574.30 <b>(+28.91%)</b></td><td>453.64 <b>(+27.50%)</b></td><td>467.60 (+16.20%)</td><td>286.20 <b>(+21.12%)</b></td><td>107.99 (+15.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>445.50 (n/a)</td><td>355.80 (n/a)</td><td>402.40 (n/a)</td><td>236.30 (n/a)</td><td>93.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+31.56%)</b></td><td>0.02 <b>(+54.67%)</b></td><td>0.03 <b>(+67.13%)</b></td><td>0.02 <b>(+305.19%)</b></td><td>0.01 (+3.65%)</td><td>507.60 <b>(-75.32%)</b></td><td>360.62 <b>(-52.67%)</b></td><td>276.90 <b>(-40.17%)</b></td><td>265.40 <b>(-23.98%)</b></td><td>122.38 <b>(-83.13%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2056.60 (n/a)</td><td>761.94 (n/a)</td><td>462.80 (n/a)</td><td>349.10 (n/a)</td><td>725.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+12.02%)</td><td>0.03 (+16.86%)</td><td>0.03 <b>(+21.97%)</b></td><td>0.01 (-0.50%)</td><td>0.01 (+10.79%)</td><td>569.80 (+0.51%)</td><td>336.18 (-13.29%)</td><td>304.70 (-18.00%)</td><td>215.90 (-10.75%)</td><td>136.59 (+5.89%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>387.70 (n/a)</td><td>371.60 (n/a)</td><td>241.90 (n/a)</td><td>129.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+9.03%)</td><td>0.02 (-15.53%)</td><td>0.02 <b>(-37.49%)</b></td><td>0.01 <b>(-37.39%)</b></td><td>0.01 <b>(+56.23%)</b></td><td>680.00 <b>(+59.74%)</b></td><td>428.08 <b>(+31.29%)</b></td><td>446.40 <b>(+60.00%)</b></td><td>222.10 (-8.30%)</td><td>179.72 <b>(+115.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.70 (n/a)</td><td>326.06 (n/a)</td><td>279.00 (n/a)</td><td>242.20 (n/a)</td><td>83.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-14.42%)</td><td>0.02 (-3.64%)</td><td>0.02 <b>(+27.82%)</b></td><td>0.01 <b>(-22.13%)</b></td><td>0.01 (-10.48%)</td><td>614.90 <b>(+28.40%)</b></td><td>419.52 (+5.10%)</td><td>357.60 <b>(-21.77%)</b></td><td>282.80 (+16.86%)</td><td>139.70 <b>(+33.09%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.90 (n/a)</td><td>399.16 (n/a)</td><td>457.10 (n/a)</td><td>242.00 (n/a)</td><td>104.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-7.87%)</td><td>0.02 <b>(-32.15%)</b></td><td>0.02 <b>(-34.83%)</b></td><td>0.00 <b>(-81.01%)</b></td><td>0.01 <b>(+154.48%)</b></td><td>1984.40 <b>(+426.51%)</b></td><td>709.96 <b>(+133.97%)</b></td><td>456.50 <b>(+53.45%)</b></td><td>281.90 (+8.55%)</td><td>718.84 <b>(+1458.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>376.90 (n/a)</td><td>303.44 (n/a)</td><td>297.50 (n/a)</td><td>259.70 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+7.72%)</td><td>0.05 (-9.14%)</td><td>0.06 (-7.56%)</td><td>0.03 <b>(-38.59%)</b></td><td>0.02 <b>(+79.59%)</b></td><td>638.70 <b>(+62.85%)</b></td><td>354.80 <b>(+21.70%)</b></td><td>293.60 (+8.18%)</td><td>222.20 (-7.18%)</td><td>164.92 <b>(+179.36%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>392.20 (n/a)</td><td>291.54 (n/a)</td><td>271.40 (n/a)</td><td>239.40 (n/a)</td><td>59.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-6.02%)</td><td>0.05 <b>(-22.99%)</b></td><td>0.05 <b>(-20.72%)</b></td><td>0.03 <b>(-57.63%)</b></td><td>0.02 <b>(+240.80%)</b></td><td>635.40 <b>(+136.03%)</b></td><td>355.46 <b>(+44.32%)</b></td><td>300.40 <b>(+26.11%)</b></td><td>245.00 (+6.38%)</td><td>158.30 <b>(+833.86%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>269.20 (n/a)</td><td>246.30 (n/a)</td><td>238.20 (n/a)</td><td>230.30 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+17.89%)</td><td>0.05 <b>(+22.71%)</b></td><td>0.04 (+0.32%)</td><td>0.03 <b>(+342.02%)</b></td><td>0.02 (-16.23%)</td><td>549.20 <b>(-77.37%)</b></td><td>386.62 <b>(-50.47%)</b></td><td>366.00 (-0.33%)</td><td>242.10 (-15.17%)</td><td>133.18 <b>(-85.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2427.40 (n/a)</td><td>780.56 (n/a)</td><td>367.20 (n/a)</td><td>285.40 (n/a)</td><td>923.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (-15.57%)</td><td>0.05 (+4.56%)</td><td>0.06 (-7.48%)</td><td>0.03 <b>(+290.21%)</b></td><td>0.01 <b>(-57.64%)</b></td><td>484.30 <b>(-74.38%)</b></td><td>327.20 <b>(-45.43%)</b></td><td>291.60 (+8.08%)</td><td>281.30 (+18.44%)</td><td>87.96 <b>(-87.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1890.00 (n/a)</td><td>599.60 (n/a)</td><td>269.80 (n/a)</td><td>237.50 (n/a)</td><td>722.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(+27.04%)</b></td><td>0.05 <b>(+27.88%)</b></td><td>0.06 <b>(+46.53%)</b></td><td>0.04 <b>(+50.02%)</b></td><td>0.02 (+18.33%)</td><td>455.80 <b>(-33.34%)</b></td><td>330.72 <b>(-23.11%)</b></td><td>277.10 <b>(-31.75%)</b></td><td>225.20 <b>(-21.29%)</b></td><td>113.26 <b>(-31.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>683.80 (n/a)</td><td>430.12 (n/a)</td><td>406.00 (n/a)</td><td>286.10 (n/a)</td><td>164.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 <b>(-28.47%)</b></td><td>0.05 (-17.48%)</td><td>0.05 (-17.75%)</td><td>0.04 (-5.94%)</td><td>0.01 <b>(-43.97%)</b></td><td>461.50 (+6.31%)</td><td>359.04 (+14.78%)</td><td>311.40 <b>(+21.55%)</b></td><td>284.60 <b>(+39.78%)</b></td><td>87.59 <b>(-21.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>434.10 (n/a)</td><td>312.82 (n/a)</td><td>256.20 (n/a)</td><td>203.60 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+17.31%)</td><td>0.04 (-19.72%)</td><td>0.04 <b>(-34.13%)</b></td><td>0.01 <b>(-70.28%)</b></td><td>0.03 <b>(+109.95%)</b></td><td>1875.30 <b>(+236.44%)</b></td><td>698.44 <b>(+99.53%)</b></td><td>464.90 <b>(+51.83%)</b></td><td>235.50 (-14.77%)</td><td>679.19 <b>(+477.04%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>557.40 (n/a)</td><td>350.04 (n/a)</td><td>306.20 (n/a)</td><td>276.30 (n/a)</td><td>117.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-16.19%)</td><td>0.04 (-1.96%)</td><td>0.03 (-8.45%)</td><td>0.03 (-17.25%)</td><td>0.02 (-5.60%)</td><td>614.00 <b>(+20.84%)</b></td><td>452.10 (+5.77%)</td><td>508.10 (+9.22%)</td><td>248.50 (+19.30%)</td><td>178.41 <b>(+42.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>508.10 (n/a)</td><td>427.42 (n/a)</td><td>465.20 (n/a)</td><td>208.30 (n/a)</td><td>125.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (+6.70%)</td><td>0.04 (-2.85%)</td><td>0.04 <b>(-22.90%)</b></td><td>0.03 <b>(+363.12%)</b></td><td>0.01 <b>(-36.91%)</b></td><td>535.10 <b>(-78.41%)</b></td><td>435.94 <b>(-42.90%)</b></td><td>445.70 <b>(+29.71%)</b></td><td>261.70 (-6.27%)</td><td>107.54 <b>(-88.79%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2477.90 (n/a)</td><td>763.50 (n/a)</td><td>343.60 (n/a)</td><td>279.20 (n/a)</td><td>959.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+10.49%)</td><td>0.06 <b>(+24.22%)</b></td><td>0.07 <b>(+43.07%)</b></td><td>0.04 (+12.90%)</td><td>0.01 <b>(+20.71%)</b></td><td>414.50 (-11.43%)</td><td>286.00 (-18.98%)</td><td>243.50 <b>(-30.13%)</b></td><td>238.10 (-9.50%)</td><td>75.06 (-3.47%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>468.00 (n/a)</td><td>352.98 (n/a)</td><td>348.50 (n/a)</td><td>263.10 (n/a)</td><td>77.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 <b>(+23.85%)</b></td><td>0.04 <b>(+34.17%)</b></td><td>0.04 <b>(+33.76%)</b></td><td>0.03 <b>(+119.21%)</b></td><td>0.01 (-3.85%)</td><td>592.40 <b>(-54.39%)</b></td><td>433.02 <b>(-33.74%)</b></td><td>408.40 <b>(-25.23%)</b></td><td>288.50 (-19.23%)</td><td>119.64 <b>(-67.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1298.70 (n/a)</td><td>653.54 (n/a)</td><td>546.20 (n/a)</td><td>357.20 (n/a)</td><td>369.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (-2.19%)</td><td>0.05 (+2.55%)</td><td>0.05 (+4.37%)</td><td>0.03 (+1.84%)</td><td>0.01 (-13.55%)</td><td>551.70 (-1.80%)</td><td>376.00 (-4.76%)</td><td>308.30 (-4.17%)</td><td>284.60 (+2.23%)</td><td>115.73 (-15.29%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.80 (n/a)</td><td>394.80 (n/a)</td><td>321.70 (n/a)</td><td>278.40 (n/a)</td><td>136.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (-13.60%)</td><td>0.10 (-6.68%)</td><td>0.12 (+3.75%)</td><td>0.07 (+0.13%)</td><td>0.03 (-10.22%)</td><td>491.30 (-0.12%)</td><td>353.98 (+6.63%)</td><td>276.60 (-3.59%)</td><td>267.10 (+15.73%)</td><td>111.47 (+2.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.90 (n/a)</td><td>331.98 (n/a)</td><td>286.90 (n/a)</td><td>230.80 (n/a)</td><td>108.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-2.04%)</td><td>0.09 <b>(-25.04%)</b></td><td>0.07 <b>(-45.44%)</b></td><td>0.06 <b>(-21.51%)</b></td><td>0.03 <b>(+36.37%)</b></td><td>532.20 <b>(+27.41%)</b></td><td>397.50 <b>(+41.55%)</b></td><td>443.10 <b>(+83.33%)</b></td><td>243.60 (+2.10%)</td><td>133.78 <b>(+72.95%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>417.70 (n/a)</td><td>280.82 (n/a)</td><td>241.70 (n/a)</td><td>238.60 (n/a)</td><td>77.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (-5.64%)</td><td>0.09 (-0.15%)</td><td>0.08 (+13.96%)</td><td>0.06 (+3.37%)</td><td>0.02 <b>(-23.21%)</b></td><td>507.00 (-3.26%)</td><td>383.46 (-3.41%)</td><td>410.10 (-12.24%)</td><td>275.40 (+5.96%)</td><td>100.61 <b>(-20.58%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>524.10 (n/a)</td><td>396.98 (n/a)</td><td>467.30 (n/a)</td><td>259.90 (n/a)</td><td>126.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-9.23%)</td><td>0.12 (+5.25%)</td><td>0.12 (+8.47%)</td><td>0.08 <b>(+36.79%)</b></td><td>0.02 <b>(-30.46%)</b></td><td>436.90 <b>(-26.89%)</b></td><td>297.08 (-11.38%)</td><td>275.00 (-7.81%)</td><td>245.50 (+10.19%)</td><td>79.78 <b>(-46.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>597.60 (n/a)</td><td>335.22 (n/a)</td><td>298.30 (n/a)</td><td>222.80 (n/a)</td><td>150.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (-14.20%)</td><td>0.12 (+12.58%)</td><td>0.12 (+10.32%)</td><td>0.09 <b>(+100.32%)</b></td><td>0.02 <b>(-46.29%)</b></td><td>379.30 <b>(-50.07%)</b></td><td>283.26 <b>(-24.71%)</b></td><td>268.70 (-9.35%)</td><td>230.00 (+16.57%)</td><td>62.50 <b>(-71.82%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>759.70 (n/a)</td><td>376.22 (n/a)</td><td>296.40 (n/a)</td><td>197.30 (n/a)</td><td>221.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (+0.52%)</td><td>0.12 (+12.84%)</td><td>0.12 (-3.08%)</td><td>0.09 <b>(+43.19%)</b></td><td>0.02 <b>(-45.06%)</b></td><td>365.80 <b>(-30.16%)</b></td><td>282.52 (-18.24%)</td><td>274.50 (+3.20%)</td><td>241.00 (-0.54%)</td><td>50.81 <b>(-61.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.80 (n/a)</td><td>345.56 (n/a)</td><td>266.00 (n/a)</td><td>242.30 (n/a)</td><td>130.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 <b>(+26.30%)</b></td><td>0.10 <b>(+50.71%)</b></td><td>0.11 <b>(+70.08%)</b></td><td>0.06 <b>(+80.66%)</b></td><td>0.03 (+16.87%)</td><td>589.10 <b>(-44.65%)</b></td><td>361.62 <b>(-37.36%)</b></td><td>291.20 <b>(-41.20%)</b></td><td>247.70 <b>(-20.84%)</b></td><td>139.38 <b>(-51.10%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1064.30 (n/a)</td><td>577.28 (n/a)</td><td>495.20 (n/a)</td><td>312.90 (n/a)</td><td>285.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-7.77%)</td><td>0.10 (-2.50%)</td><td>0.11 (-9.28%)</td><td>0.06 (+13.79%)</td><td>0.03 <b>(-32.97%)</b></td><td>515.50 (-12.12%)</td><td>342.16 (-4.58%)</td><td>308.80 (+10.21%)</td><td>245.40 (+8.44%)</td><td>104.01 <b>(-33.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>586.60 (n/a)</td><td>358.60 (n/a)</td><td>280.20 (n/a)</td><td>226.30 (n/a)</td><td>155.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (-10.74%)</td><td>0.09 (-10.94%)</td><td>0.08 (-19.57%)</td><td>0.06 (+18.27%)</td><td>0.03 <b>(-38.69%)</b></td><td>575.80 (-15.45%)</td><td>396.52 (-3.38%)</td><td>388.80 <b>(+24.34%)</b></td><td>236.60 (+12.03%)</td><td>124.37 <b>(-44.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>681.00 (n/a)</td><td>410.38 (n/a)</td><td>312.70 (n/a)</td><td>211.20 (n/a)</td><td>223.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-2.26%)</td><td>0.11 (+8.00%)</td><td>0.12 <b>(+26.46%)</b></td><td>0.08 (+18.99%)</td><td>0.03 <b>(-21.27%)</b></td><td>434.50 (-15.97%)</td><td>323.50 (-11.02%)</td><td>273.70 <b>(-20.94%)</b></td><td>244.20 (+2.30%)</td><td>84.82 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.10 (n/a)</td><td>363.58 (n/a)</td><td>346.20 (n/a)</td><td>238.70 (n/a)</td><td>121.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (+9.29%)</td><td>0.09 (+5.36%)</td><td>0.09 (-9.71%)</td><td>0.05 (-3.74%)</td><td>0.03 (+1.78%)</td><td>596.30 (+3.89%)</td><td>388.36 (-5.83%)</td><td>378.30 (+10.74%)</td><td>261.00 (-8.52%)</td><td>133.76 (-7.89%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.00 (n/a)</td><td>412.40 (n/a)</td><td>341.60 (n/a)</td><td>285.30 (n/a)</td><td>145.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-0.63%)</td><td>0.09 (+16.42%)</td><td>0.09 <b>(+47.36%)</b></td><td>0.05 (-3.00%)</td><td>0.03 (+8.34%)</td><td>631.60 (+3.08%)</td><td>408.14 (-11.95%)</td><td>350.20 <b>(-32.14%)</b></td><td>254.10 (+0.63%)</td><td>163.14 (+16.63%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>612.70 (n/a)</td><td>463.52 (n/a)</td><td>516.10 (n/a)</td><td>252.50 (n/a)</td><td>139.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (+11.87%)</td><td>0.10 <b>(+24.53%)</b></td><td>0.10 (+11.57%)</td><td>0.09 <b>(+84.03%)</b></td><td>0.01 <b>(-62.78%)</b></td><td>270.20 <b>(-45.67%)</b></td><td>251.54 <b>(-25.51%)</b></td><td>249.30 (-10.39%)</td><td>219.30 (-10.64%)</td><td>20.91 <b>(-81.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>497.30 (n/a)</td><td>337.70 (n/a)</td><td>278.20 (n/a)</td><td>245.40 (n/a)</td><td>112.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.22 (+4.05%)</td><td>0.18 (+9.85%)</td><td>0.20 (+18.06%)</td><td>0.10 (-1.40%)</td><td>0.05 <b>(+20.42%)</b></td><td>497.50 (+1.43%)</td><td>297.52 (-6.77%)</td><td>243.70 (-15.32%)</td><td>221.20 (-3.87%)</td><td>114.43 (+14.85%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>490.50 (n/a)</td><td>319.14 (n/a)</td><td>287.80 (n/a)</td><td>230.10 (n/a)</td><td>99.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.33 (+4.64%)</td><td>3.85 <b>(+20.52%)</b></td><td>4.14 <b>(+33.47%)</b></td><td>2.81 (+10.88%)</td><td>0.61 (-10.58%)</td><td>3726.50 (-9.81%)</td><td>2793.38 (-17.94%)</td><td>2533.20 <b>(-25.08%)</b></td><td>2422.80 (-4.44%)</td><td>538.52 <b>(-23.49%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.14 (n/a)</td><td>3.19 (n/a)</td><td>3.10 (n/a)</td><td>2.54 (n/a)</td><td>0.69 (n/a)</td><td>4132.00 (n/a)</td><td>3404.14 (n/a)</td><td>3381.10 (n/a)</td><td>2535.30 (n/a)</td><td>703.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (+8.31%)</td><td>0.14 (+12.74%)</td><td>0.16 (+19.17%)</td><td>0.07 <b>(+37.52%)</b></td><td>0.04 (+0.51%)</td><td>617.90 <b>(-27.28%)</b></td><td>331.24 (-16.92%)</td><td>251.70 (-16.10%)</td><td>235.40 (-7.69%)</td><td>162.88 <b>(-35.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>849.70 (n/a)</td><td>398.68 (n/a)</td><td>300.00 (n/a)</td><td>255.00 (n/a)</td><td>253.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-0.80%)</td><td>0.02 (-1.89%)</td><td>0.02 (+18.87%)</td><td>0.01 <b>(-32.58%)</b></td><td>0.00 <b>(+156.26%)</b></td><td>458.30 <b>(+48.32%)</b></td><td>308.60 (+8.01%)</td><td>245.60 (-15.86%)</td><td>244.40 (+0.78%)</td><td>95.23 <b>(+274.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>309.00 (n/a)</td><td>285.72 (n/a)</td><td>291.90 (n/a)</td><td>242.50 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (-10.96%)</td><td>0.01 (+7.51%)</td><td>0.01 (+19.85%)</td><td>0.01 (+10.91%)</td><td>0.00 <b>(-24.96%)</b></td><td>559.30 (-9.83%)</td><td>373.58 (-10.92%)</td><td>325.70 (-16.55%)</td><td>289.50 (+12.34%)</td><td>112.80 <b>(-24.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.30 (n/a)</td><td>419.36 (n/a)</td><td>390.30 (n/a)</td><td>257.70 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (+1.53%)</td><td>0.02 (+0.47%)</td><td>0.02 (+18.08%)</td><td>0.01 (-10.17%)</td><td>0.01 (+1.85%)</td><td>602.00 (+11.32%)</td><td>386.40 (+1.16%)</td><td>363.80 (-15.32%)</td><td>237.60 (-1.53%)</td><td>153.48 (+15.76%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>540.80 (n/a)</td><td>381.96 (n/a)</td><td>429.60 (n/a)</td><td>241.30 (n/a)</td><td>132.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (-17.33%)</td><td>0.01 <b>(-23.06%)</b></td><td>0.01 <b>(-35.02%)</b></td><td>0.01 (-5.89%)</td><td>0.00 (-16.09%)</td><td>554.10 (+6.25%)</td><td>428.66 <b>(+28.93%)</b></td><td>438.90 <b>(+53.89%)</b></td><td>288.70 <b>(+20.95%)</b></td><td>115.93 (+4.05%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.50 (n/a)</td><td>332.48 (n/a)</td><td>285.20 (n/a)</td><td>238.70 (n/a)</td><td>111.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+3.80%)</td><td>0.02 (+16.80%)</td><td>0.02 <b>(+65.77%)</b></td><td>0.01 (+10.59%)</td><td>0.01 (+2.87%)</td><td>531.40 (-9.58%)</td><td>372.28 (-14.74%)</td><td>285.70 <b>(-39.69%)</b></td><td>257.40 (-3.67%)</td><td>143.59 (-7.06%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.70 (n/a)</td><td>436.64 (n/a)</td><td>473.70 (n/a)</td><td>267.20 (n/a)</td><td>154.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+20.30%)</b></td><td>0.01 (-15.79%)</td><td>0.01 <b>(-44.76%)</b></td><td>0.00 <b>(-67.47%)</b></td><td>0.01 <b>(+63.11%)</b></td><td>1903.20 <b>(+207.46%)</b></td><td>699.98 <b>(+85.32%)</b></td><td>542.90 <b>(+81.03%)</b></td><td>204.10 (-16.90%)</td><td>691.48 <b>(+335.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.00 (n/a)</td><td>377.72 (n/a)</td><td>299.90 (n/a)</td><td>245.60 (n/a)</td><td>158.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-8.43%)</td><td>0.01 <b>(-21.10%)</b></td><td>0.01 <b>(-26.98%)</b></td><td>0.00 (-15.03%)</td><td>0.01 (-2.22%)</td><td>1184.40 (+17.69%)</td><td>708.50 <b>(+36.90%)</b></td><td>646.30 <b>(+36.93%)</b></td><td>273.20 (+9.19%)</td><td>413.71 <b>(+35.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1006.40 (n/a)</td><td>517.54 (n/a)</td><td>472.00 (n/a)</td><td>250.20 (n/a)</td><td>305.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+2.47%)</td><td>0.01 (+0.33%)</td><td>0.01 <b>(+22.82%)</b></td><td>0.01 <b>(-21.07%)</b></td><td>0.01 (+15.90%)</td><td>795.20 <b>(+26.68%)</b></td><td>406.00 (+7.68%)</td><td>278.40 (-18.60%)</td><td>231.60 (-2.40%)</td><td>232.81 <b>(+48.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.70 (n/a)</td><td>377.04 (n/a)</td><td>342.00 (n/a)</td><td>237.30 (n/a)</td><td>157.28 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-18.12%)</td><td>0.01 (-19.55%)</td><td>0.01 <b>(-24.31%)</b></td><td>0.01 <b>(-27.61%)</b></td><td>0.00 (-15.40%)</td><td>813.90 <b>(+38.14%)</b></td><td>565.68 <b>(+26.62%)</b></td><td>601.20 <b>(+32.13%)</b></td><td>265.90 <b>(+22.08%)</b></td><td>197.27 <b>(+41.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.20 (n/a)</td><td>446.76 (n/a)</td><td>455.00 (n/a)</td><td>217.80 (n/a)</td><td>139.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+0.09%)</td><td>0.01 (+0.57%)</td><td>0.01 (-17.68%)</td><td>0.01 <b>(+25.35%)</b></td><td>0.00 <b>(-29.80%)</b></td><td>507.20 <b>(-20.23%)</b></td><td>389.20 (-8.45%)</td><td>386.30 <b>(+21.48%)</b></td><td>270.70 (-0.07%)</td><td>98.10 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.80 (n/a)</td><td>425.14 (n/a)</td><td>318.00 (n/a)</td><td>270.90 (n/a)</td><td>181.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 <b>(-34.65%)</b></td><td>0.01 (-13.33%)</td><td>0.01 (-5.55%)</td><td>0.01 (+5.38%)</td><td>0.00 <b>(-57.04%)</b></td><td>569.10 (-5.10%)</td><td>489.28 (+4.08%)</td><td>520.40 (+5.88%)</td><td>321.60 <b>(+53.00%)</b></td><td>98.85 <b>(-36.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>470.10 (n/a)</td><td>491.50 (n/a)</td><td>210.20 (n/a)</td><td>154.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 <b>(+29.85%)</b></td><td>0.01 (+6.02%)</td><td>0.01 (-13.95%)</td><td>0.01 (+8.29%)</td><td>0.00 <b>(+77.12%)</b></td><td>569.50 (-7.65%)</td><td>435.54 (-2.67%)</td><td>484.50 (+16.21%)</td><td>289.00 <b>(-22.99%)</b></td><td>114.15 (+18.52%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>447.48 (n/a)</td><td>416.90 (n/a)</td><td>375.30 (n/a)</td><td>96.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+14.51%)</td><td>0.03 <b>(+46.45%)</b></td><td>0.03 <b>(+70.36%)</b></td><td>0.02 <b>(+74.47%)</b></td><td>0.01 (-11.52%)</td><td>462.70 <b>(-42.68%)</b></td><td>333.48 <b>(-36.57%)</b></td><td>304.10 <b>(-41.30%)</b></td><td>222.80 (-12.66%)</td><td>93.86 <b>(-52.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>807.20 (n/a)</td><td>525.78 (n/a)</td><td>518.10 (n/a)</td><td>255.10 (n/a)</td><td>196.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (+10.93%)</td><td>0.04 <b>(+47.38%)</b></td><td>0.04 <b>(+74.28%)</b></td><td>0.03 <b>(+47.03%)</b></td><td>0.01 (-14.65%)</td><td>473.70 <b>(-31.98%)</b></td><td>325.32 <b>(-35.84%)</b></td><td>300.10 <b>(-42.63%)</b></td><td>230.30 (-9.86%)</td><td>93.26 <b>(-42.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>696.40 (n/a)</td><td>507.02 (n/a)</td><td>523.10 (n/a)</td><td>255.50 (n/a)</td><td>161.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (-2.23%)</td><td>0.03 (-5.55%)</td><td>0.03 (-0.50%)</td><td>0.02 (+15.37%)</td><td>0.01 <b>(-21.00%)</b></td><td>538.80 (-13.32%)</td><td>320.36 (-0.37%)</td><td>277.00 (+0.51%)</td><td>219.30 (+2.29%)</td><td>125.26 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.60 (n/a)</td><td>321.54 (n/a)</td><td>275.60 (n/a)</td><td>214.40 (n/a)</td><td>170.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (-8.82%)</td><td>0.03 (-13.81%)</td><td>0.03 (-7.40%)</td><td>0.01 <b>(-63.57%)</b></td><td>0.02 <b>(+22.25%)</b></td><td>1665.30 <b>(+174.48%)</b></td><td>611.90 <b>(+67.90%)</b></td><td>317.00 (+7.97%)</td><td>221.00 (+9.68%)</td><td>605.95 <b>(+272.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.70 (n/a)</td><td>364.44 (n/a)</td><td>293.60 (n/a)</td><td>201.50 (n/a)</td><td>162.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+1.84%)</td><td>0.03 <b>(+36.10%)</b></td><td>0.03 <b>(+71.12%)</b></td><td>0.02 <b>(+57.39%)</b></td><td>0.01 (-17.34%)</td><td>505.30 <b>(-36.46%)</b></td><td>360.06 <b>(-32.92%)</b></td><td>302.70 <b>(-41.57%)</b></td><td>224.80 (-1.79%)</td><td>124.18 <b>(-43.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.30 (n/a)</td><td>536.78 (n/a)</td><td>518.10 (n/a)</td><td>228.90 (n/a)</td><td>220.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+6.03%)</td><td>0.03 <b>(+21.15%)</b></td><td>0.03 <b>(+63.29%)</b></td><td>0.02 (-13.14%)</td><td>0.01 <b>(+26.20%)</b></td><td>629.00 (+15.14%)</td><td>396.12 (-12.92%)</td><td>309.30 <b>(-38.75%)</b></td><td>247.80 (-5.71%)</td><td>165.77 <b>(+40.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.30 (n/a)</td><td>454.90 (n/a)</td><td>505.00 (n/a)</td><td>262.80 (n/a)</td><td>118.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (+2.40%)</td><td>0.02 (+18.87%)</td><td>0.02 <b>(+46.76%)</b></td><td>0.01 <b>(-50.25%)</b></td><td>0.01 <b>(+41.68%)</b></td><td>1360.60 <b>(+101.00%)</b></td><td>595.62 (+13.31%)</td><td>405.40 <b>(-31.87%)</b></td><td>231.40 (-2.32%)</td><td>474.99 <b>(+175.87%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.90 (n/a)</td><td>525.66 (n/a)</td><td>595.00 (n/a)</td><td>236.90 (n/a)</td><td>172.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 <b>(+63.06%)</b></td><td>0.03 <b>(+57.17%)</b></td><td>0.03 <b>(+64.16%)</b></td><td>0.02 <b>(+26.18%)</b></td><td>0.01 <b>(+96.26%)</b></td><td>431.60 <b>(-20.76%)</b></td><td>303.54 <b>(-34.83%)</b></td><td>293.20 <b>(-39.09%)</b></td><td>208.50 <b>(-38.68%)</b></td><td>80.39 (-2.95%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>544.70 (n/a)</td><td>465.78 (n/a)</td><td>481.40 (n/a)</td><td>340.00 (n/a)</td><td>82.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(+21.76%)</b></td><td>0.03 <b>(+81.79%)</b></td><td>0.03 <b>(+82.32%)</b></td><td>0.02 <b>(+514.28%)</b></td><td>0.00 <b>(-58.82%)</b></td><td>341.00 <b>(-83.72%)</b></td><td>285.94 <b>(-63.67%)</b></td><td>279.20 <b>(-45.16%)</b></td><td>242.20 (-17.87%)</td><td>35.77 <b>(-95.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2094.50 (n/a)</td><td>787.12 (n/a)</td><td>509.10 (n/a)</td><td>294.90 (n/a)</td><td>738.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 <b>(-21.79%)</b></td><td>0.02 (-15.43%)</td><td>0.02 (-11.92%)</td><td>0.02 (+1.58%)</td><td>0.01 <b>(-38.06%)</b></td><td>567.50 (-1.56%)</td><td>448.92 (+10.60%)</td><td>515.70 (+13.54%)</td><td>287.40 <b>(+27.85%)</b></td><td>123.73 <b>(-20.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.50 (n/a)</td><td>405.90 (n/a)</td><td>454.20 (n/a)</td><td>224.80 (n/a)</td><td>154.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (-18.56%)</td><td>0.02 (+2.96%)</td><td>0.02 (+7.64%)</td><td>0.02 <b>(+20.59%)</b></td><td>0.01 <b>(-40.00%)</b></td><td>525.30 (-17.08%)</td><td>403.44 (-10.62%)</td><td>423.00 (-7.09%)</td><td>259.20 <b>(+22.79%)</b></td><td>99.73 <b>(-36.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.50 (n/a)</td><td>451.38 (n/a)</td><td>455.30 (n/a)</td><td>211.10 (n/a)</td><td>156.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-12.63%)</td><td>0.05 (+7.16%)</td><td>0.05 <b>(+48.71%)</b></td><td>0.03 <b>(+26.00%)</b></td><td>0.02 <b>(-34.97%)</b></td><td>513.00 <b>(-20.64%)</b></td><td>359.90 (-17.97%)</td><td>332.70 <b>(-32.76%)</b></td><td>225.60 (+14.46%)</td><td>119.85 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>646.40 (n/a)</td><td>438.72 (n/a)</td><td>494.80 (n/a)</td><td>197.10 (n/a)</td><td>201.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-16.40%)</td><td>0.06 <b>(-30.90%)</b></td><td>0.05 <b>(-38.41%)</b></td><td>0.04 <b>(-47.38%)</b></td><td>0.02 <b>(+51.40%)</b></td><td>621.60 <b>(+90.03%)</b></td><td>432.32 <b>(+55.62%)</b></td><td>458.70 <b>(+62.37%)</b></td><td>270.50 (+19.58%)</td><td>141.93 <b>(+235.62%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>327.10 (n/a)</td><td>277.80 (n/a)</td><td>282.50 (n/a)</td><td>226.20 (n/a)</td><td>42.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-1.26%)</td><td>0.05 (+12.11%)</td><td>0.03 (+2.23%)</td><td>0.03 <b>(+232.45%)</b></td><td>0.02 (-14.17%)</td><td>605.20 <b>(-69.92%)</b></td><td>446.12 <b>(-39.39%)</b></td><td>581.50 (-2.19%)</td><td>221.90 (+1.28%)</td><td>196.72 <b>(-73.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2012.10 (n/a)</td><td>736.04 (n/a)</td><td>594.50 (n/a)</td><td>219.10 (n/a)</td><td>735.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (-13.68%)</td><td>0.05 <b>(-20.74%)</b></td><td>0.04 <b>(-36.90%)</b></td><td>0.04 (-7.10%)</td><td>0.02 <b>(-23.29%)</b></td><td>579.60 (+7.63%)</td><td>433.14 <b>(+21.13%)</b></td><td>458.20 <b>(+58.49%)</b></td><td>246.50 (+15.84%)</td><td>122.48 (-13.74%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>538.50 (n/a)</td><td>357.58 (n/a)</td><td>289.10 (n/a)</td><td>212.80 (n/a)</td><td>141.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-9.46%)</td><td>0.05 (+19.41%)</td><td>0.06 <b>(+78.32%)</b></td><td>0.03 <b>(+59.34%)</b></td><td>0.02 (-14.65%)</td><td>645.00 <b>(-37.24%)</b></td><td>401.86 <b>(-25.20%)</b></td><td>287.20 <b>(-43.92%)</b></td><td>223.20 (+10.44%)</td><td>205.11 <b>(-36.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1027.70 (n/a)</td><td>537.26 (n/a)</td><td>512.10 (n/a)</td><td>202.10 (n/a)</td><td>322.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (+9.59%)</td><td>0.07 (+19.33%)</td><td>0.07 (+3.50%)</td><td>0.04 <b>(+303.29%)</b></td><td>0.02 <b>(-29.79%)</b></td><td>486.70 <b>(-75.20%)</b></td><td>343.76 <b>(-48.28%)</b></td><td>275.30 (-3.37%)</td><td>235.70 (-8.75%)</td><td>122.06 <b>(-83.40%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1962.60 (n/a)</td><td>664.72 (n/a)</td><td>284.90 (n/a)</td><td>258.30 (n/a)</td><td>735.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (-3.95%)</td><td>0.06 (+8.35%)</td><td>0.06 (+6.46%)</td><td>0.04 (+17.91%)</td><td>0.02 (-15.15%)</td><td>450.20 (-15.18%)</td><td>313.04 (-11.85%)</td><td>267.20 (-6.08%)</td><td>211.80 (+4.13%)</td><td>102.67 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.80 (n/a)</td><td>355.14 (n/a)</td><td>284.50 (n/a)</td><td>203.40 (n/a)</td><td>141.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (+7.47%)</td><td>0.05 <b>(+24.30%)</b></td><td>0.04 (-7.34%)</td><td>0.03 <b>(+28.68%)</b></td><td>0.03 <b>(+22.78%)</b></td><td>635.50 <b>(-22.29%)</b></td><td>424.98 (-18.06%)</td><td>500.20 (+7.92%)</td><td>224.50 (-6.96%)</td><td>183.88 (-14.49%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>817.80 (n/a)</td><td>518.66 (n/a)</td><td>463.50 (n/a)</td><td>241.30 (n/a)</td><td>215.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (-17.76%)</td><td>0.04 (-0.37%)</td><td>0.04 <b>(+24.55%)</b></td><td>0.02 <b>(-38.75%)</b></td><td>0.02 (-6.13%)</td><td>1054.60 <b>(+63.25%)</b></td><td>514.84 (+9.80%)</td><td>438.00 (-19.71%)</td><td>263.00 <b>(+21.59%)</b></td><td>322.88 <b>(+82.86%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.00 (n/a)</td><td>468.88 (n/a)</td><td>545.50 (n/a)</td><td>216.30 (n/a)</td><td>176.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 <b>(-24.13%)</b></td><td>0.04 <b>(-27.14%)</b></td><td>0.05 <b>(-22.13%)</b></td><td>0.02 <b>(-38.43%)</b></td><td>0.01 (-6.72%)</td><td>820.50 <b>(+62.41%)</b></td><td>466.36 <b>(+44.17%)</b></td><td>362.70 <b>(+28.43%)</b></td><td>322.70 <b>(+31.82%)</b></td><td>205.20 <b>(+96.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>505.20 (n/a)</td><td>323.48 (n/a)</td><td>282.40 (n/a)</td><td>244.80 (n/a)</td><td>104.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(+20.00%)</b></td><td>0.05 <b>(+36.07%)</b></td><td>0.04 <b>(+39.88%)</b></td><td>0.04 <b>(+49.35%)</b></td><td>0.02 (+0.25%)</td><td>438.60 <b>(-33.04%)</b></td><td>345.92 <b>(-30.19%)</b></td><td>388.10 <b>(-28.51%)</b></td><td>219.20 (-16.65%)</td><td>92.82 <b>(-45.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>655.00 (n/a)</td><td>495.52 (n/a)</td><td>542.90 (n/a)</td><td>263.00 (n/a)</td><td>169.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 <b>(-21.19%)</b></td><td>0.09 (+2.08%)</td><td>0.09 <b>(+56.26%)</b></td><td>0.06 <b>(+30.78%)</b></td><td>0.03 <b>(-48.60%)</b></td><td>520.90 <b>(-23.53%)</b></td><td>394.34 (-17.34%)</td><td>363.20 <b>(-36.00%)</b></td><td>265.10 <b>(+26.90%)</b></td><td>112.98 <b>(-49.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>681.20 (n/a)</td><td>477.04 (n/a)</td><td>567.50 (n/a)</td><td>208.90 (n/a)</td><td>223.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (+2.72%)</td><td>0.11 (+6.01%)</td><td>0.11 (+8.40%)</td><td>0.07 (+7.03%)</td><td>0.03 <b>(+26.74%)</b></td><td>482.00 (-6.57%)</td><td>335.66 (-3.08%)</td><td>289.90 (-7.76%)</td><td>231.50 (-2.65%)</td><td>115.24 (+11.19%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>515.90 (n/a)</td><td>346.34 (n/a)</td><td>314.30 (n/a)</td><td>237.80 (n/a)</td><td>103.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (+4.49%)</td><td>0.09 (-8.39%)</td><td>0.08 <b>(-37.41%)</b></td><td>0.07 <b>(+205.74%)</b></td><td>0.04 <b>(-34.95%)</b></td><td>622.80 <b>(-67.29%)</b></td><td>476.96 <b>(-29.98%)</b></td><td>505.30 <b>(+59.75%)</b></td><td>257.20 (-4.28%)</td><td>133.85 <b>(-80.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1904.20 (n/a)</td><td>681.20 (n/a)</td><td>316.30 (n/a)</td><td>268.70 (n/a)</td><td>700.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 <b>(+36.04%)</b></td><td>0.08 <b>(+49.64%)</b></td><td>0.08 <b>(+24.93%)</b></td><td>0.06 <b>(+252.82%)</b></td><td>0.02 (-8.39%)</td><td>531.00 <b>(-71.66%)</b></td><td>416.54 <b>(-47.97%)</b></td><td>412.50 (-19.95%)</td><td>275.70 <b>(-26.48%)</b></td><td>114.59 <b>(-81.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1873.60 (n/a)</td><td>800.52 (n/a)</td><td>515.30 (n/a)</td><td>375.00 (n/a)</td><td>617.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (-2.32%)</td><td>0.11 (+0.44%)</td><td>0.09 (-2.12%)</td><td>0.09 (+4.79%)</td><td>0.03 (-6.46%)</td><td>472.00 (-4.57%)</td><td>399.92 (-1.33%)</td><td>464.00 (+2.16%)</td><td>245.20 (+2.38%)</td><td>101.43 (-6.74%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>494.60 (n/a)</td><td>405.32 (n/a)</td><td>454.20 (n/a)</td><td>239.50 (n/a)</td><td>108.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (+17.88%)</td><td>0.08 (+2.48%)</td><td>0.07 (-8.76%)</td><td>0.05 (+2.22%)</td><td>0.02 <b>(+28.63%)</b></td><td>629.00 (-2.18%)</td><td>467.56 (-0.31%)</td><td>460.20 (+9.60%)</td><td>302.30 (-15.18%)</td><td>139.82 (+10.02%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>643.00 (n/a)</td><td>469.02 (n/a)</td><td>419.90 (n/a)</td><td>356.40 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 <b>(+25.85%)</b></td><td>0.10 <b>(+42.19%)</b></td><td>0.10 <b>(+48.26%)</b></td><td>0.07 <b>(+36.01%)</b></td><td>0.02 (+3.26%)</td><td>496.70 <b>(-26.47%)</b></td><td>371.36 <b>(-30.80%)</b></td><td>365.60 <b>(-32.56%)</b></td><td>303.50 <b>(-20.55%)</b></td><td>75.18 <b>(-38.78%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>675.50 (n/a)</td><td>536.68 (n/a)</td><td>542.10 (n/a)</td><td>382.00 (n/a)</td><td>122.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 (+15.55%)</td><td>0.10 <b>(+33.66%)</b></td><td>0.10 <b>(+50.03%)</b></td><td>0.06 (+7.20%)</td><td>0.04 <b>(+29.81%)</b></td><td>544.90 (-6.71%)</td><td>363.16 <b>(-22.10%)</b></td><td>317.40 <b>(-33.36%)</b></td><td>212.10 (-13.46%)</td><td>151.45 (+10.03%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.10 (n/a)</td><td>466.18 (n/a)</td><td>476.30 (n/a)</td><td>245.10 (n/a)</td><td>137.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (-2.49%)</td><td>0.12 <b>(+24.36%)</b></td><td>0.13 <b>(+55.43%)</b></td><td>0.07 (+7.55%)</td><td>0.04 (-2.31%)</td><td>536.10 (-7.01%)</td><td>344.42 <b>(-20.46%)</b></td><td>273.90 <b>(-35.66%)</b></td><td>234.20 (+2.54%)</td><td>131.95 (-10.09%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>576.50 (n/a)</td><td>433.00 (n/a)</td><td>425.70 (n/a)</td><td>228.40 (n/a)</td><td>146.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-1.54%)</td><td>0.08 <b>(-20.77%)</b></td><td>0.06 <b>(-38.54%)</b></td><td>0.05 <b>(-23.23%)</b></td><td>0.04 <b>(+36.81%)</b></td><td>674.10 <b>(+30.26%)</b></td><td>481.00 <b>(+38.35%)</b></td><td>571.30 <b>(+62.67%)</b></td><td>256.90 (+1.58%)</td><td>191.58 <b>(+80.79%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.50 (n/a)</td><td>347.66 (n/a)</td><td>351.20 (n/a)</td><td>252.90 (n/a)</td><td>105.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-9.11%)</td><td>0.06 (-14.50%)</td><td>0.07 (+0.45%)</td><td>0.04 <b>(-40.84%)</b></td><td>0.02 <b>(+84.05%)</b></td><td>505.60 <b>(+69.04%)</b></td><td>346.76 <b>(+26.48%)</b></td><td>286.00 (-0.45%)</td><td>235.80 (+10.03%)</td><td>122.22 <b>(+253.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>299.10 (n/a)</td><td>274.16 (n/a)</td><td>287.30 (n/a)</td><td>214.30 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (-10.33%)</td><td>0.06 (+19.25%)</td><td>0.07 <b>(+33.66%)</b></td><td>0.05 <b>(+28.56%)</b></td><td>0.01 <b>(-35.52%)</b></td><td>417.40 <b>(-22.21%)</b></td><td>331.00 (-19.99%)</td><td>303.60 <b>(-25.17%)</b></td><td>272.10 (+11.52%)</td><td>64.92 <b>(-43.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>536.60 (n/a)</td><td>413.72 (n/a)</td><td>405.70 (n/a)</td><td>244.00 (n/a)</td><td>114.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 <b>(+60.44%)</b></td><td>0.06 <b>(+43.34%)</b></td><td>0.06 <b>(+38.69%)</b></td><td>0.05 <b>(+48.12%)</b></td><td>0.01 <b>(+67.06%)</b></td><td>439.50 <b>(-32.49%)</b></td><td>350.02 <b>(-29.93%)</b></td><td>363.40 <b>(-27.90%)</b></td><td>258.40 <b>(-37.67%)</b></td><td>67.45 <b>(-29.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>651.00 (n/a)</td><td>499.50 (n/a)</td><td>504.00 (n/a)</td><td>414.60 (n/a)</td><td>95.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (+4.10%)</td><td>0.05 (+19.87%)</td><td>0.05 <b>(+30.10%)</b></td><td>0.03 (+4.36%)</td><td>0.02 (+3.28%)</td><td>586.90 (-4.18%)</td><td>413.28 (-16.87%)</td><td>424.90 <b>(-23.14%)</b></td><td>260.50 (-3.95%)</td><td>134.08 (-6.85%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.50 (n/a)</td><td>497.14 (n/a)</td><td>552.80 (n/a)</td><td>271.20 (n/a)</td><td>143.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (+7.72%)</td><td>0.07 <b>(+26.83%)</b></td><td>0.06 <b>(+43.23%)</b></td><td>0.04 (+17.11%)</td><td>0.02 (-2.19%)</td><td>581.70 (-14.62%)</td><td>353.26 <b>(-24.71%)</b></td><td>355.10 <b>(-30.18%)</b></td><td>222.10 (-7.15%)</td><td>145.25 <b>(-25.86%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>681.30 (n/a)</td><td>469.18 (n/a)</td><td>508.60 (n/a)</td><td>239.20 (n/a)</td><td>195.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (+13.62%)</td><td>0.07 (+6.92%)</td><td>0.08 <b>(+25.72%)</b></td><td>0.04 <b>(+22.61%)</b></td><td>0.02 <b>(+21.34%)</b></td><td>499.30 (-18.44%)</td><td>344.60 (-5.47%)</td><td>270.10 <b>(-20.44%)</b></td><td>219.00 (-11.98%)</td><td>130.47 (-10.30%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>612.20 (n/a)</td><td>364.54 (n/a)</td><td>339.50 (n/a)</td><td>248.80 (n/a)</td><td>145.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (+16.41%)</td><td>0.07 (+17.46%)</td><td>0.06 (+9.63%)</td><td>0.04 <b>(+332.83%)</b></td><td>0.03 (-15.53%)</td><td>581.30 <b>(-76.90%)</b></td><td>412.74 <b>(-48.87%)</b></td><td>423.90 (-8.78%)</td><td>237.60 (-14.10%)</td><td>153.72 <b>(-84.00%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2516.20 (n/a)</td><td>807.16 (n/a)</td><td>464.70 (n/a)</td><td>276.60 (n/a)</td><td>960.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 <b>(+45.31%)</b></td><td>0.08 (+19.22%)</td><td>0.06 (+8.58%)</td><td>0.05 (+18.74%)</td><td>0.03 <b>(+73.15%)</b></td><td>452.30 (-15.77%)</td><td>355.70 (-12.34%)</td><td>402.60 (-7.89%)</td><td>204.50 <b>(-31.17%)</b></td><td>111.25 (+8.70%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>537.00 (n/a)</td><td>405.78 (n/a)</td><td>437.10 (n/a)</td><td>297.10 (n/a)</td><td>102.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (-1.37%)</td><td>0.05 <b>(-25.60%)</b></td><td>0.05 <b>(-22.02%)</b></td><td>0.01 <b>(-79.48%)</b></td><td>0.03 <b>(+61.62%)</b></td><td>2485.10 <b>(+387.27%)</b></td><td>873.28 <b>(+115.80%)</b></td><td>528.60 <b>(+28.24%)</b></td><td>270.00 (+1.39%)</td><td>908.91 <b>(+815.78%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>510.00 (n/a)</td><td>404.68 (n/a)</td><td>412.20 (n/a)</td><td>266.30 (n/a)</td><td>99.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 <b>(+57.74%)</b></td><td>0.09 <b>(+38.19%)</b></td><td>0.10 (+19.75%)</td><td>0.05 (+13.06%)</td><td>0.03 <b>(+44.45%)</b></td><td>535.70 (-11.54%)</td><td>305.06 <b>(-26.30%)</b></td><td>254.80 (-16.51%)</td><td>184.80 <b>(-36.60%)</b></td><td>135.83 (-13.51%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>605.60 (n/a)</td><td>413.94 (n/a)</td><td>305.20 (n/a)</td><td>291.50 (n/a)</td><td>157.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 <b>(+20.00%)</b></td><td>0.07 <b>(+22.31%)</b></td><td>0.09 <b>(+64.06%)</b></td><td>0.01 <b>(-74.46%)</b></td><td>0.04 <b>(+126.74%)</b></td><td>2046.90 <b>(+291.53%)</b></td><td>651.40 <b>(+50.21%)</b></td><td>285.30 <b>(-39.05%)</b></td><td>223.00 (-16.67%)</td><td>786.38 <b>(+704.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>522.80 (n/a)</td><td>433.66 (n/a)</td><td>468.10 (n/a)</td><td>267.60 (n/a)</td><td>97.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (-0.92%)</td><td>0.05 (-18.33%)</td><td>0.04 <b>(-27.75%)</b></td><td>0.02 <b>(-27.11%)</b></td><td>0.03 (+7.84%)</td><td>1047.70 <b>(+37.19%)</b></td><td>602.96 <b>(+29.71%)</b></td><td>585.30 <b>(+38.40%)</b></td><td>244.00 (+0.91%)</td><td>287.53 <b>(+40.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>763.70 (n/a)</td><td>464.86 (n/a)</td><td>422.90 (n/a)</td><td>241.80 (n/a)</td><td>204.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (+19.99%)</td><td>0.05 (+8.32%)</td><td>0.04 (-11.82%)</td><td>0.04 <b>(+23.74%)</b></td><td>0.02 <b>(+23.43%)</b></td><td>521.20 (-19.19%)</td><td>387.52 (-6.88%)</td><td>459.70 (+13.42%)</td><td>206.60 (-16.63%)</td><td>137.68 (-14.31%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.00 (n/a)</td><td>416.16 (n/a)</td><td>405.30 (n/a)</td><td>247.80 (n/a)</td><td>160.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 <b>(+39.64%)</b></td><td>0.06 <b>(+34.05%)</b></td><td>0.04 (+14.78%)</td><td>0.03 (+9.82%)</td><td>0.03 <b>(+115.24%)</b></td><td>538.20 (-8.93%)</td><td>381.06 (-15.95%)</td><td>417.10 (-12.87%)</td><td>203.30 <b>(-28.39%)</b></td><td>164.31 <b>(+44.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>591.00 (n/a)</td><td>453.38 (n/a)</td><td>478.70 (n/a)</td><td>283.90 (n/a)</td><td>113.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (-15.86%)</td><td>0.06 (+7.02%)</td><td>0.06 (+18.36%)</td><td>0.04 (+14.27%)</td><td>0.02 (-18.46%)</td><td>517.70 (-12.49%)</td><td>344.86 (-10.23%)</td><td>285.20 (-15.50%)</td><td>243.80 (+18.87%)</td><td>124.11 (-18.89%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.60 (n/a)</td><td>384.14 (n/a)</td><td>337.50 (n/a)</td><td>205.10 (n/a)</td><td>153.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (+9.31%)</td><td>0.05 (+9.10%)</td><td>0.07 <b>(+64.51%)</b></td><td>0.01 <b>(-77.80%)</b></td><td>0.03 <b>(+89.71%)</b></td><td>2465.60 <b>(+350.42%)</b></td><td>742.06 <b>(+73.61%)</b></td><td>279.40 <b>(-39.21%)</b></td><td>275.30 (-8.51%)</td><td>965.23 <b>(+722.76%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>547.40 (n/a)</td><td>427.42 (n/a)</td><td>459.60 (n/a)</td><td>300.90 (n/a)</td><td>117.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (-17.71%)</td><td>0.04 <b>(-22.51%)</b></td><td>0.04 (-2.74%)</td><td>0.01 <b>(-74.76%)</b></td><td>0.02 (+12.48%)</td><td>1914.40 <b>(+296.11%)</b></td><td>709.36 <b>(+82.52%)</b></td><td>462.20 (+2.83%)</td><td>278.50 <b>(+21.51%)</b></td><td>678.94 <b>(+509.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>483.30 (n/a)</td><td>388.64 (n/a)</td><td>449.50 (n/a)</td><td>229.20 (n/a)</td><td>111.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (+17.83%)</td><td>0.05 (+8.11%)</td><td>0.05 (+14.83%)</td><td>0.03 <b>(-22.91%)</b></td><td>0.02 <b>(+48.06%)</b></td><td>611.60 <b>(+29.71%)</b></td><td>391.60 (-1.30%)</td><td>409.10 (-12.92%)</td><td>238.40 (-15.13%)</td><td>153.07 <b>(+51.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>396.74 (n/a)</td><td>469.80 (n/a)</td><td>280.90 (n/a)</td><td>101.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.42 (+10.54%)</td><td>0.26 (-4.93%)</td><td>0.31 (+12.32%)</td><td>0.05 <b>(-72.78%)</b></td><td>0.15 <b>(+76.17%)</b></td><td>1973.40 <b>(+267.42%)</b></td><td>680.46 <b>(+72.43%)</b></td><td>322.10 (-10.97%)</td><td>234.90 (-9.51%)</td><td>734.82 <b>(+502.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>537.10 (n/a)</td><td>394.64 (n/a)</td><td>361.80 (n/a)</td><td>259.60 (n/a)</td><td>122.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.38 (+5.05%)</td><td>0.28 <b>(+26.08%)</b></td><td>0.27 <b>(+33.37%)</b></td><td>0.19 <b>(+27.12%)</b></td><td>0.08 (-4.70%)</td><td>508.60 <b>(-21.33%)</b></td><td>383.96 <b>(-22.83%)</b></td><td>367.80 <b>(-25.02%)</b></td><td>256.80 (-4.78%)</td><td>113.17 <b>(-26.49%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>646.50 (n/a)</td><td>497.56 (n/a)</td><td>490.50 (n/a)</td><td>269.70 (n/a)</td><td>153.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.41 (-4.65%)</td><td>0.26 (-8.46%)</td><td>0.20 (-14.52%)</td><td>0.14 (-10.38%)</td><td>0.13 (+16.02%)</td><td>689.50 (+11.57%)</td><td>467.74 (+17.60%)</td><td>501.50 (+16.98%)</td><td>242.10 (+4.85%)</td><td>216.15 <b>(+36.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>618.00 (n/a)</td><td>397.74 (n/a)</td><td>428.70 (n/a)</td><td>230.90 (n/a)</td><td>158.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.33 <b>(+25.62%)</b></td><td>0.26 <b>(+42.27%)</b></td><td>0.26 <b>(+82.29%)</b></td><td>0.20 <b>(+50.28%)</b></td><td>0.05 <b>(-23.50%)</b></td><td>363.00 <b>(-33.46%)</b></td><td>289.38 <b>(-33.77%)</b></td><td>287.70 <b>(-45.14%)</b></td><td>223.80 <b>(-20.41%)</b></td><td>52.97 <b>(-59.96%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>545.50 (n/a)</td><td>436.90 (n/a)</td><td>524.40 (n/a)</td><td>281.20 (n/a)</td><td>132.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.31 (+9.48%)</td><td>0.22 (-8.89%)</td><td>0.18 <b>(-29.87%)</b></td><td>0.14 (-7.02%)</td><td>0.08 <b>(+64.53%)</b></td><td>525.80 (+7.57%)</td><td>382.46 (+17.36%)</td><td>415.70 <b>(+42.61%)</b></td><td>234.60 (-8.68%)</td><td>136.46 <b>(+47.23%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>488.80 (n/a)</td><td>325.90 (n/a)</td><td>291.50 (n/a)</td><td>256.90 (n/a)</td><td>92.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.33 <b>(-36.13%)</b></td><td>0.19 <b>(-30.65%)</b></td><td>0.16 <b>(-35.04%)</b></td><td>0.12 (-1.03%)</td><td>0.08 <b>(-43.80%)</b></td><td>639.10 (+1.03%)</td><td>436.02 <b>(+30.54%)</b></td><td>459.30 <b>(+53.92%)</b></td><td>225.00 <b>(+56.58%)</b></td><td>150.24 (-16.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>632.60 (n/a)</td><td>334.02 (n/a)</td><td>298.40 (n/a)</td><td>143.70 (n/a)</td><td>179.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (-18.85%)</td><td>0.08 (-14.35%)</td><td>0.08 <b>(-28.42%)</b></td><td>0.06 (+6.04%)</td><td>0.01 <b>(-54.43%)</b></td><td>582.20 (-5.70%)</td><td>467.68 (+8.40%)</td><td>477.00 <b>(+39.68%)</b></td><td>375.20 <b>(+23.22%)</b></td><td>81.62 <b>(-47.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>617.40 (n/a)</td><td>431.44 (n/a)</td><td>341.50 (n/a)</td><td>304.50 (n/a)</td><td>156.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 <b>(+27.20%)</b></td><td>0.11 (+9.06%)</td><td>0.12 (+6.37%)</td><td>0.06 (-1.46%)</td><td>0.03 <b>(+43.91%)</b></td><td>619.60 (+1.47%)</td><td>375.18 (-4.76%)</td><td>314.30 (-5.98%)</td><td>250.90 <b>(-21.40%)</b></td><td>146.65 (+18.10%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>610.60 (n/a)</td><td>393.94 (n/a)</td><td>334.30 (n/a)</td><td>319.20 (n/a)</td><td>124.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (-5.17%)</td><td>0.09 (-9.72%)</td><td>0.09 (+17.07%)</td><td>0.06 (+8.72%)</td><td>0.04 <b>(-23.38%)</b></td><td>569.20 (-8.02%)</td><td>428.92 (+3.34%)</td><td>416.50 (-14.58%)</td><td>231.00 (+5.43%)</td><td>129.28 <b>(-25.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>618.80 (n/a)</td><td>415.04 (n/a)</td><td>487.60 (n/a)</td><td>219.10 (n/a)</td><td>173.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.20 (-0.77%)</td><td>0.11 (-7.72%)</td><td>0.11 (-7.49%)</td><td>0.03 <b>(-45.60%)</b></td><td>0.06 (+13.87%)</td><td>1166.80 <b>(+83.83%)</b></td><td>509.76 <b>(+31.52%)</b></td><td>331.90 (+8.11%)</td><td>186.50 (+0.76%)</td><td>390.83 <b>(+117.79%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>634.70 (n/a)</td><td>387.60 (n/a)</td><td>307.00 (n/a)</td><td>185.10 (n/a)</td><td>179.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 <b>(+34.30%)</b></td><td>0.11 (+3.19%)</td><td>0.09 (-18.73%)</td><td>0.08 (+15.75%)</td><td>0.04 <b>(+61.55%)</b></td><td>468.50 (-13.59%)</td><td>379.28 (-0.23%)</td><td>416.00 <b>(+23.04%)</b></td><td>209.90 <b>(-25.54%)</b></td><td>100.58 (-3.17%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>542.20 (n/a)</td><td>380.16 (n/a)</td><td>338.10 (n/a)</td><td>281.90 (n/a)</td><td>103.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-7.46%)</td><td>0.08 (-15.76%)</td><td>0.08 (-2.30%)</td><td>0.03 <b>(-61.52%)</b></td><td>0.04 <b>(+29.25%)</b></td><td>1351.10 <b>(+159.93%)</b></td><td>626.06 <b>(+45.11%)</b></td><td>471.20 (+2.37%)</td><td>283.40 (+8.09%)</td><td>420.48 <b>(+295.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>519.80 (n/a)</td><td>431.44 (n/a)</td><td>460.30 (n/a)</td><td>262.20 (n/a)</td><td>106.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (+3.21%)</td><td>0.12 (+19.12%)</td><td>0.13 <b>(+28.75%)</b></td><td>0.09 <b>(+68.51%)</b></td><td>0.03 <b>(-29.66%)</b></td><td>450.40 <b>(-40.65%)</b></td><td>345.36 <b>(-24.50%)</b></td><td>324.40 <b>(-22.32%)</b></td><td>241.80 (-3.09%)</td><td>84.22 <b>(-58.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>758.90 (n/a)</td><td>457.46 (n/a)</td><td>417.60 (n/a)</td><td>249.50 (n/a)</td><td>204.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 <b>(+89.47%)</b></td><td>0.13 <b>(+84.55%)</b></td><td>0.14 <b>(+92.89%)</b></td><td>0.06 <b>(+78.99%)</b></td><td>0.04 <b>(+101.95%)</b></td><td>632.40 <b>(-44.13%)</b></td><td>362.84 <b>(-44.94%)</b></td><td>290.20 <b>(-48.16%)</b></td><td>247.30 <b>(-47.21%)</b></td><td>158.29 <b>(-41.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>1131.90 (n/a)</td><td>658.98 (n/a)</td><td>559.80 (n/a)</td><td>468.50 (n/a)</td><td>271.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.25 (-6.52%)</td><td>0.13 (-10.27%)</td><td>0.08 <b>(-43.57%)</b></td><td>0.07 (-8.24%)</td><td>0.08 (+5.21%)</td><td>594.20 (+8.97%)</td><td>398.90 (+17.82%)</td><td>487.20 <b>(+77.23%)</b></td><td>164.80 (+6.94%)</td><td>191.27 (+19.75%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>545.30 (n/a)</td><td>338.58 (n/a)</td><td>274.90 (n/a)</td><td>154.10 (n/a)</td><td>159.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (-15.12%)</td><td>0.08 (-17.97%)</td><td>0.08 (-2.24%)</td><td>0.02 <b>(-75.02%)</b></td><td>0.06 (+1.10%)</td><td>2558.90 <b>(+300.27%)</b></td><td>907.50 <b>(+85.58%)</b></td><td>535.00 (+2.27%)</td><td>248.20 (+17.80%)</td><td>941.48 <b>(+436.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>639.30 (n/a)</td><td>489.02 (n/a)</td><td>523.10 (n/a)</td><td>210.70 (n/a)</td><td>175.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.20 <b>(+28.86%)</b></td><td>0.12 (+11.06%)</td><td>0.09 (-8.87%)</td><td>0.08 (+7.07%)</td><td>0.05 <b>(+50.80%)</b></td><td>513.10 (-6.61%)</td><td>376.88 (-5.15%)</td><td>447.20 (+9.74%)</td><td>202.60 <b>(-22.38%)</b></td><td>136.95 (+12.18%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>549.40 (n/a)</td><td>397.36 (n/a)</td><td>407.50 (n/a)</td><td>261.00 (n/a)</td><td>122.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.22 <b>(+48.18%)</b></td><td>0.15 <b>(+35.91%)</b></td><td>0.16 <b>(+24.16%)</b></td><td>0.08 (+15.43%)</td><td>0.06 <b>(+56.29%)</b></td><td>537.70 (-13.37%)</td><td>312.48 <b>(-23.31%)</b></td><td>252.60 (-19.48%)</td><td>185.00 <b>(-32.53%)</b></td><td>148.02 (-8.94%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>620.70 (n/a)</td><td>407.46 (n/a)</td><td>313.70 (n/a)</td><td>274.20 (n/a)</td><td>162.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (-1.68%)</td><td>0.09 (-14.77%)</td><td>0.09 <b>(-26.29%)</b></td><td>0.06 <b>(+31.07%)</b></td><td>0.03 (-14.92%)</td><td>544.50 <b>(-23.71%)</b></td><td>412.34 (+10.70%)</td><td>401.40 <b>(+35.65%)</b></td><td>277.20 (+1.72%)</td><td>124.85 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>713.70 (n/a)</td><td>372.48 (n/a)</td><td>295.90 (n/a)</td><td>272.50 (n/a)</td><td>191.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 <b>(+21.24%)</b></td><td>0.10 (+0.07%)</td><td>0.11 (-0.18%)</td><td>0.07 (-2.78%)</td><td>0.03 <b>(+66.43%)</b></td><td>484.50 (+2.87%)</td><td>358.58 (+3.41%)</td><td>321.80 (+0.16%)</td><td>238.10 (-17.53%)</td><td>98.51 <b>(+37.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>471.00 (n/a)</td><td>346.74 (n/a)</td><td>321.30 (n/a)</td><td>288.70 (n/a)</td><td>71.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 <b>(+31.48%)</b></td><td>0.08 (+12.18%)</td><td>0.09 <b>(+23.24%)</b></td><td>0.02 <b>(-63.34%)</b></td><td>0.04 <b>(+167.83%)</b></td><td>1840.20 <b>(+172.82%)</b></td><td>665.52 <b>(+38.01%)</b></td><td>386.20 (-18.87%)</td><td>274.30 <b>(-23.95%)</b></td><td>665.64 <b>(+457.90%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>674.50 (n/a)</td><td>482.22 (n/a)</td><td>476.00 (n/a)</td><td>360.70 (n/a)</td><td>119.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 <b>(+42.03%)</b></td><td>0.09 <b>(+33.63%)</b></td><td>0.11 <b>(+62.37%)</b></td><td>0.03 <b>(+41.56%)</b></td><td>0.05 <b>(+84.59%)</b></td><td>1304.90 <b>(-29.35%)</b></td><td>638.18 (-14.80%)</td><td>306.40 <b>(-38.41%)</b></td><td>271.70 <b>(-29.57%)</b></td><td>491.19 <b>(-20.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1847.10 (n/a)</td><td>749.02 (n/a)</td><td>497.50 (n/a)</td><td>385.80 (n/a)</td><td>617.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 <b>(-20.15%)</b></td><td>0.09 <b>(-20.57%)</b></td><td>0.08 <b>(-31.73%)</b></td><td>0.07 (-7.99%)</td><td>0.03 <b>(-22.80%)</b></td><td>483.40 (+8.70%)</td><td>405.64 <b>(+24.50%)</b></td><td>446.30 <b>(+46.47%)</b></td><td>245.10 <b>(+25.24%)</b></td><td>100.84 (+7.47%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>444.70 (n/a)</td><td>325.82 (n/a)</td><td>304.70 (n/a)</td><td>195.70 (n/a)</td><td>93.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (-16.11%)</td><td>0.07 (-10.73%)</td><td>0.07 (-11.39%)</td><td>0.06 (-7.73%)</td><td>0.01 <b>(-31.04%)</b></td><td>631.20 (+8.38%)</td><td>523.14 (+11.05%)</td><td>522.10 (+12.86%)</td><td>438.10 (+19.18%)</td><td>71.51 (-10.12%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>582.40 (n/a)</td><td>471.08 (n/a)</td><td>462.60 (n/a)</td><td>367.60 (n/a)</td><td>79.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.47 (+1.05%)</td><td>0.33 (+15.56%)</td><td>0.26 (-10.09%)</td><td>0.24 <b>(+131.88%)</b></td><td>0.11 (-10.99%)</td><td>555.60 <b>(-56.87%)</b></td><td>429.32 <b>(-26.41%)</b></td><td>497.10 (+11.21%)</td><td>281.70 (-1.05%)</td><td>131.16 <b>(-67.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>1288.20 (n/a)</td><td>583.36 (n/a)</td><td>447.00 (n/a)</td><td>284.70 (n/a)</td><td>400.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.69 <b>(+30.43%)</b></td><td>0.33 (-4.75%)</td><td>0.24 <b>(-33.29%)</b></td><td>0.22 (+11.92%)</td><td>0.20 <b>(+47.33%)</b></td><td>588.20 (-10.65%)</td><td>478.34 (+9.91%)</td><td>544.00 <b>(+49.90%)</b></td><td>191.20 <b>(-23.31%)</b></td><td>162.26 (-8.93%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>658.30 (n/a)</td><td>435.20 (n/a)</td><td>362.90 (n/a)</td><td>249.30 (n/a)</td><td>178.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.34 <b>(-32.88%)</b></td><td>0.25 <b>(-34.00%)</b></td><td>0.25 <b>(-37.40%)</b></td><td>0.17 <b>(-37.57%)</b></td><td>0.06 <b>(-38.95%)</b></td><td>759.20 <b>(+60.20%)</b></td><td>540.30 <b>(+50.43%)</b></td><td>521.50 <b>(+59.72%)</b></td><td>384.90 <b>(+48.96%)</b></td><td>136.13 <b>(+44.84%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>473.90 (n/a)</td><td>359.16 (n/a)</td><td>326.50 (n/a)</td><td>258.40 (n/a)</td><td>93.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+11.86%)</td><td>0.01 (+5.03%)</td><td>0.01 (+17.85%)</td><td>0.01 (-4.91%)</td><td>0.00 <b>(+36.71%)</b></td><td>537.80 (+5.16%)</td><td>347.46 (-1.78%)</td><td>288.50 (-15.17%)</td><td>246.00 (-10.58%)</td><td>116.96 <b>(+26.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.40 (n/a)</td><td>353.76 (n/a)</td><td>340.10 (n/a)</td><td>275.10 (n/a)</td><td>92.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (+0.26%)</td><td>0.01 (+3.61%)</td><td>0.01 (-6.00%)</td><td>0.01 (-3.34%)</td><td>0.00 (+3.26%)</td><td>566.00 (+3.45%)</td><td>326.40 (-2.51%)</td><td>293.80 (+6.41%)</td><td>228.20 (-0.26%)</td><td>137.93 (+7.51%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.10 (n/a)</td><td>334.82 (n/a)</td><td>276.10 (n/a)</td><td>228.80 (n/a)</td><td>128.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+20.52%)</b></td><td>0.01 (-10.77%)</td><td>0.01 <b>(-28.14%)</b></td><td>0.00 <b>(-60.86%)</b></td><td>0.01 <b>(+122.03%)</b></td><td>1214.50 <b>(+155.47%)</b></td><td>508.96 <b>(+54.15%)</b></td><td>426.30 <b>(+39.18%)</b></td><td>210.20 (-17.05%)</td><td>407.52 <b>(+370.10%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.40 (n/a)</td><td>330.18 (n/a)</td><td>306.30 (n/a)</td><td>253.40 (n/a)</td><td>86.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>7.87 <b>(-28.28%)</b></td><td>5.64 <b>(-26.38%)</b></td><td>6.97 (-13.54%)</td><td>2.27 <b>(-38.55%)</b></td><td>2.48 (-15.53%)</td><td>925.90 <b>(+62.72%)</b></td><td>467.58 <b>(+46.67%)</b></td><td>300.90 (+15.64%)</td><td>266.70 <b>(+39.41%)</b></td><td>282.90 <b>(+83.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>10.97 (n/a)</td><td>7.67 (n/a)</td><td>8.06 (n/a)</td><td>3.69 (n/a)</td><td>2.94 (n/a)</td><td>569.00 (n/a)</td><td>318.80 (n/a)</td><td>260.20 (n/a)</td><td>191.30 (n/a)</td><td>153.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.64 <b>(+29.76%)</b></td><td>0.38 (+10.67%)</td><td>0.35 (+18.63%)</td><td>0.23 (+0.41%)</td><td>0.17 <b>(+44.60%)</b></td><td>577.20 (-0.41%)</td><td>404.12 (-3.97%)</td><td>372.30 (-15.69%)</td><td>206.20 <b>(-22.92%)</b></td><td>166.10 <b>(+21.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>579.60 (n/a)</td><td>420.84 (n/a)</td><td>441.60 (n/a)</td><td>267.50 (n/a)</td><td>136.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.55 (-4.66%)</td><td>0.43 (-9.92%)</td><td>0.46 (+9.58%)</td><td>0.28 <b>(-30.02%)</b></td><td>0.12 <b>(+41.21%)</b></td><td>466.40 <b>(+42.89%)</b></td><td>331.46 (+16.04%)</td><td>287.90 (-8.75%)</td><td>238.20 (+4.84%)</td><td>99.47 <b>(+112.23%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.08 (n/a)</td><td>326.40 (n/a)</td><td>285.64 (n/a)</td><td>315.50 (n/a)</td><td>227.20 (n/a)</td><td>46.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.45 <b>(-25.71%)</b></td><td>0.32 <b>(-23.85%)</b></td><td>0.27 <b>(-26.24%)</b></td><td>0.26 (+2.40%)</td><td>0.08 <b>(-47.73%)</b></td><td>505.90 (-2.34%)</td><td>431.86 <b>(+22.44%)</b></td><td>487.90 <b>(+35.57%)</b></td><td>291.30 <b>(+34.61%)</b></td><td>96.37 <b>(-26.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.61 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>518.00 (n/a)</td><td>352.70 (n/a)</td><td>359.90 (n/a)</td><td>216.40 (n/a)</td><td>130.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.45 (-7.17%)</td><td>0.34 (+1.32%)</td><td>0.32 (+11.78%)</td><td>0.29 <b>(+35.98%)</b></td><td>0.07 <b>(-49.12%)</b></td><td>457.00 <b>(-26.47%)</b></td><td>394.38 (-9.79%)</td><td>408.80 (-10.53%)</td><td>292.00 (+7.71%)</td><td>66.53 <b>(-57.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>621.50 (n/a)</td><td>437.20 (n/a)</td><td>456.90 (n/a)</td><td>271.10 (n/a)</td><td>158.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.39 <b>(-22.90%)</b></td><td>0.27 <b>(-28.54%)</b></td><td>0.28 <b>(-34.30%)</b></td><td>0.07 <b>(-70.97%)</b></td><td>0.12 (+19.38%)</td><td>1824.90 <b>(+244.52%)</b></td><td>700.88 <b>(+89.85%)</b></td><td>478.20 <b>(+52.20%)</b></td><td>337.60 <b>(+29.70%)</b></td><td>632.22 <b>(+469.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>529.70 (n/a)</td><td>369.18 (n/a)</td><td>314.20 (n/a)</td><td>260.30 (n/a)</td><td>111.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (-12.40%)</td><td>0.01 (+19.48%)</td><td>0.01 <b>(+62.08%)</b></td><td>0.01 <b>(+247.18%)</b></td><td>0.00 <b>(-45.29%)</b></td><td>559.00 <b>(-71.20%)</b></td><td>353.62 <b>(-48.17%)</b></td><td>302.70 <b>(-38.30%)</b></td><td>257.40 (+14.20%)</td><td>123.88 <b>(-82.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.70 (n/a)</td><td>682.26 (n/a)</td><td>490.60 (n/a)</td><td>225.40 (n/a)</td><td>714.28 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 <b>(+22.29%)</b></td><td>0.01 (+11.98%)</td><td>0.01 (-6.47%)</td><td>0.01 (+2.51%)</td><td>0.00 <b>(+69.52%)</b></td><td>524.30 (-2.44%)</td><td>396.42 (-5.00%)</td><td>449.70 (+6.92%)</td><td>236.10 (-18.25%)</td><td>135.71 <b>(+35.84%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>417.30 (n/a)</td><td>420.60 (n/a)</td><td>288.80 (n/a)</td><td>99.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.00 (+0.00%)</td><td>0.00 (+5.56%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+27.73%)</b></td><td>21491.91 <b>(+29.97%)</b></td><td>13876.47 (+5.25%)</td><td>17449.95 (+17.63%)</td><td>6067.86 (+2.94%)</td><td>7093.87 <b>(+68.98%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16536.32 (n/a)</td><td>13184.46 (n/a)</td><td>14834.15 (n/a)</td><td>5894.38 (n/a)</td><td>4198.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.00 (+0.00%)</td><td>0.00 (-19.15%)</td><td>0.00 <b>(-58.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-14.10%)</td><td>19327.13 (-14.81%)</td><td>13189.76 (+10.33%)</td><td>15111.83 <b>(+123.32%)</b></td><td>5699.18 (-3.34%)</td><td>5858.30 <b>(-26.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22688.14 (n/a)</td><td>11954.37 (n/a)</td><td>6766.77 (n/a)</td><td>5896.34 (n/a)</td><td>7929.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (+5.34%)</td><td>0.10 (+1.49%)</td><td>0.09 (+6.85%)</td><td>0.07 (-0.54%)</td><td>0.03 (-5.08%)</td><td>28335.16 (+0.53%)</td><td>22050.70 (-2.41%)</td><td>24034.92 (-6.34%)</td><td>14767.00 (-5.07%)</td><td>5450.80 (-9.81%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28185.36 (n/a)</td><td>22595.87 (n/a)</td><td>25661.19 (n/a)</td><td>15556.05 (n/a)</td><td>6043.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.55 (-17.19%)</td><td>2.22 <b>(+64.32%)</b></td><td>2.36 <b>(+75.81%)</b></td><td>1.62 <b>(+427.99%)</b></td><td>0.39 <b>(-66.13%)</b></td><td>647.60 <b>(-81.06%)</b></td><td>485.00 <b>(-71.34%)</b></td><td>444.20 <b>(-43.12%)</b></td><td>412.00 <b>(+20.75%)</b></td><td>98.56 <b>(-93.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.07 (n/a)</td><td>1.35 (n/a)</td><td>1.34 (n/a)</td><td>0.31 (n/a)</td><td>1.15 (n/a)</td><td>3419.10 (n/a)</td><td>1692.54 (n/a)</td><td>780.90 (n/a)</td><td>341.20 (n/a)</td><td>1537.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.43 (+8.72%)</td><td>1.64 <b>(-23.58%)</b></td><td>1.40 <b>(-24.60%)</b></td><td>0.32 <b>(-79.06%)</b></td><td>1.17 <b>(+84.10%)</b></td><td>3254.30 <b>(+377.59%)</b></td><td>1168.52 <b>(+124.68%)</b></td><td>748.00 <b>(+32.62%)</b></td><td>306.00 (-8.03%)</td><td>1195.14 <b>(+789.81%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.15 (n/a)</td><td>2.14 (n/a)</td><td>1.86 (n/a)</td><td>1.54 (n/a)</td><td>0.64 (n/a)</td><td>681.40 (n/a)</td><td>520.08 (n/a)</td><td>564.00 (n/a)</td><td>332.70 (n/a)</td><td>134.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.53 <b>(+53.67%)</b></td><td>2.03 <b>(+32.42%)</b></td><td>2.36 <b>(+48.54%)</b></td><td>0.56 (+2.39%)</td><td>1.18 <b>(+88.67%)</b></td><td>1865.10 (-2.34%)</td><td>788.64 (-8.93%)</td><td>445.00 <b>(-32.69%)</b></td><td>297.40 <b>(-34.92%)</b></td><td>648.22 (+9.88%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.29 (n/a)</td><td>1.53 (n/a)</td><td>1.59 (n/a)</td><td>0.55 (n/a)</td><td>0.63 (n/a)</td><td>1909.70 (n/a)</td><td>865.96 (n/a)</td><td>661.10 (n/a)</td><td>457.00 (n/a)</td><td>589.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.51 <b>(+28.91%)</b></td><td>2.67 <b>(+77.53%)</b></td><td>2.44 <b>(+78.19%)</b></td><td>1.76 <b>(+189.93%)</b></td><td>0.76 (-4.04%)</td><td>594.60 <b>(-65.51%)</b></td><td>420.10 <b>(-52.60%)</b></td><td>430.20 <b>(-43.88%)</b></td><td>299.10 <b>(-22.43%)</b></td><td>122.52 <b>(-76.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.72 (n/a)</td><td>1.50 (n/a)</td><td>1.37 (n/a)</td><td>0.61 (n/a)</td><td>0.79 (n/a)</td><td>1724.00 (n/a)</td><td>886.36 (n/a)</td><td>766.60 (n/a)</td><td>385.60 (n/a)</td><td>511.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.32 (+5.82%)</td><td>2.91 (+18.54%)</td><td>2.59 <b>(-22.30%)</b></td><td>2.09 <b>(+255.19%)</b></td><td>0.86 <b>(-46.19%)</b></td><td>1003.90 <b>(-71.85%)</b></td><td>765.98 <b>(-50.38%)</b></td><td>809.70 <b>(+28.69%)</b></td><td>485.60 (-5.51%)</td><td>193.64 <b>(-85.91%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.08 (n/a)</td><td>2.45 (n/a)</td><td>3.33 (n/a)</td><td>0.59 (n/a)</td><td>1.60 (n/a)</td><td>3565.90 (n/a)</td><td>1543.58 (n/a)</td><td>629.20 (n/a)</td><td>513.90 (n/a)</td><td>1374.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.99 (+18.93%)</td><td>2.72 (+5.23%)</td><td>2.50 (-17.72%)</td><td>1.62 <b>(+173.92%)</b></td><td>0.89 <b>(-22.62%)</b></td><td>1296.00 <b>(-63.49%)</b></td><td>842.42 <b>(-33.03%)</b></td><td>838.20 <b>(+21.53%)</b></td><td>525.80 (-15.91%)</td><td>290.57 <b>(-77.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>3.35 (n/a)</td><td>2.59 (n/a)</td><td>3.04 (n/a)</td><td>0.59 (n/a)</td><td>1.15 (n/a)</td><td>3550.00 (n/a)</td><td>1257.90 (n/a)</td><td>689.70 (n/a)</td><td>625.30 (n/a)</td><td>1282.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.31 (-11.94%)</td><td>2.67 <b>(-37.50%)</b></td><td>2.56 <b>(-37.57%)</b></td><td>0.84 <b>(-69.02%)</b></td><td>1.86 <b>(+51.24%)</b></td><td>2497.20 <b>(+222.84%)</b></td><td>1259.74 <b>(+139.29%)</b></td><td>818.60 <b>(+60.16%)</b></td><td>394.60 (+13.55%)</td><td>932.58 <b>(+486.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>6.04 (n/a)</td><td>4.27 (n/a)</td><td>4.10 (n/a)</td><td>2.71 (n/a)</td><td>1.23 (n/a)</td><td>773.50 (n/a)</td><td>526.46 (n/a)</td><td>511.10 (n/a)</td><td>347.50 (n/a)</td><td>158.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.55 <b>(-27.63%)</b></td><td>2.96 <b>(-37.17%)</b></td><td>2.98 <b>(-22.45%)</b></td><td>0.56 <b>(-78.13%)</b></td><td>1.92 (-14.28%)</td><td>3729.20 <b>(+357.29%)</b></td><td>1301.64 <b>(+145.37%)</b></td><td>704.30 <b>(+28.95%)</b></td><td>377.80 <b>(+38.19%)</b></td><td>1388.30 <b>(+496.84%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.67 (n/a)</td><td>4.71 (n/a)</td><td>3.84 (n/a)</td><td>2.57 (n/a)</td><td>2.24 (n/a)</td><td>815.50 (n/a)</td><td>530.48 (n/a)</td><td>546.20 (n/a)</td><td>273.40 (n/a)</td><td>232.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.29 (-2.52%)</td><td>2.99 (+5.65%)</td><td>3.56 (+15.99%)</td><td>0.60 (+4.49%)</td><td>1.52 (+8.72%)</td><td>3480.30 (-4.30%)</td><td>1186.98 (-3.87%)</td><td>588.70 (-13.78%)</td><td>488.40 (+2.58%)</td><td>1290.70 (-4.12%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.41 (n/a)</td><td>2.83 (n/a)</td><td>3.07 (n/a)</td><td>0.58 (n/a)</td><td>1.40 (n/a)</td><td>3636.50 (n/a)</td><td>1234.80 (n/a)</td><td>682.80 (n/a)</td><td>476.10 (n/a)</td><td>1346.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.13 (-6.48%)</td><td>2.87 (-8.21%)</td><td>2.49 (-6.52%)</td><td>0.60 <b>(-70.54%)</b></td><td>1.69 <b>(+25.00%)</b></td><td>3497.90 <b>(+239.40%)</b></td><td>1238.00 <b>(+65.35%)</b></td><td>842.50 (+6.97%)</td><td>409.20 (+6.92%)</td><td>1278.91 <b>(+440.32%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.48 (n/a)</td><td>3.13 (n/a)</td><td>2.66 (n/a)</td><td>2.03 (n/a)</td><td>1.36 (n/a)</td><td>1030.60 (n/a)</td><td>748.70 (n/a)</td><td>787.60 (n/a)</td><td>382.70 (n/a)</td><td>236.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.93 (-5.73%)</td><td>4.14 (-5.33%)</td><td>4.09 (-1.74%)</td><td>2.87 (-14.12%)</td><td>0.83 (+6.32%)</td><td>1459.20 (+16.45%)</td><td>1053.04 (+6.80%)</td><td>1025.20 (+1.77%)</td><td>850.80 (+6.08%)</td><td>245.48 <b>(+34.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>5.23 (n/a)</td><td>4.37 (n/a)</td><td>4.16 (n/a)</td><td>3.35 (n/a)</td><td>0.78 (n/a)</td><td>1253.10 (n/a)</td><td>985.96 (n/a)</td><td>1007.40 (n/a)</td><td>802.00 (n/a)</td><td>182.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>7.60 (-2.09%)</td><td>5.18 (+4.36%)</td><td>5.36 (+3.34%)</td><td>1.67 (-4.71%)</td><td>2.49 (+16.30%)</td><td>2509.30 (+4.93%)</td><td>1098.12 (+1.65%)</td><td>782.80 (-3.24%)</td><td>552.00 (+2.15%)</td><td>817.13 (+9.90%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.76 (n/a)</td><td>4.96 (n/a)</td><td>5.18 (n/a)</td><td>1.75 (n/a)</td><td>2.14 (n/a)</td><td>2391.30 (n/a)</td><td>1080.26 (n/a)</td><td>809.00 (n/a)</td><td>540.40 (n/a)</td><td>743.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>8.51 (+10.31%)</td><td>5.73 (-8.79%)</td><td>7.46 (+14.08%)</td><td>1.24 <b>(-65.64%)</b></td><td>3.18 <b>(+91.06%)</b></td><td>3370.10 <b>(+191.03%)</b></td><td>1228.58 <b>(+70.59%)</b></td><td>562.40 (-12.34%)</td><td>493.00 (-9.34%)</td><td>1230.91 <b>(+384.91%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>7.71 (n/a)</td><td>6.28 (n/a)</td><td>6.54 (n/a)</td><td>3.62 (n/a)</td><td>1.66 (n/a)</td><td>1158.00 (n/a)</td><td>720.20 (n/a)</td><td>641.60 (n/a)</td><td>543.80 (n/a)</td><td>253.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>9.77 (+2.20%)</td><td>6.94 <b>(+25.50%)</b></td><td>6.70 <b>(+64.37%)</b></td><td>2.27 <b>(+30.45%)</b></td><td>3.06 (-8.81%)</td><td>1846.40 <b>(-23.34%)</b></td><td>799.96 <b>(-27.14%)</b></td><td>626.00 <b>(-39.16%)</b></td><td>429.20 (-2.14%)</td><td>594.54 <b>(-25.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>9.56 (n/a)</td><td>5.53 (n/a)</td><td>4.08 (n/a)</td><td>1.74 (n/a)</td><td>3.35 (n/a)</td><td>2408.70 (n/a)</td><td>1098.00 (n/a)</td><td>1028.90 (n/a)</td><td>438.60 (n/a)</td><td>794.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>8.82 (+0.61%)</td><td>6.19 (-8.53%)</td><td>6.63 (-13.40%)</td><td>1.29 <b>(-59.83%)</b></td><td>2.89 <b>(+34.79%)</b></td><td>3248.10 <b>(+148.93%)</b></td><td>1108.86 <b>(+57.45%)</b></td><td>632.30 (+15.47%)</td><td>475.60 (-0.61%)</td><td>1197.80 <b>(+251.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>8.77 (n/a)</td><td>6.77 (n/a)</td><td>7.66 (n/a)</td><td>3.21 (n/a)</td><td>2.14 (n/a)</td><td>1304.80 (n/a)</td><td>704.24 (n/a)</td><td>547.60 (n/a)</td><td>478.50 (n/a)</td><td>341.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>10.27 (+5.85%)</td><td>5.77 (+0.04%)</td><td>6.63 <b>(+36.71%)</b></td><td>1.26 <b>(-26.56%)</b></td><td>3.38 (+8.56%)</td><td>3329.00 <b>(+36.16%)</b></td><td>1211.04 (+17.02%)</td><td>632.70 <b>(-26.86%)</b></td><td>408.50 (-5.51%)</td><td>1207.79 <b>(+48.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>9.70 (n/a)</td><td>5.77 (n/a)</td><td>4.85 (n/a)</td><td>1.72 (n/a)</td><td>3.11 (n/a)</td><td>2444.90 (n/a)</td><td>1034.86 (n/a)</td><td>865.00 (n/a)</td><td>432.30 (n/a)</td><td>814.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.60 (-15.79%)</td><td>0.92 <b>(-26.84%)</b></td><td>0.92 (-5.45%)</td><td>0.15 <b>(-82.66%)</b></td><td>0.58 <b>(+24.99%)</b></td><td>3453.80 <b>(+476.79%)</b></td><td>1132.26 <b>(+145.15%)</b></td><td>567.40 (+5.76%)</td><td>326.80 (+18.75%)</td><td>1318.12 <b>(+787.77%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>1.91 (n/a)</td><td>1.25 (n/a)</td><td>0.98 (n/a)</td><td>0.88 (n/a)</td><td>0.47 (n/a)</td><td>598.80 (n/a)</td><td>461.86 (n/a)</td><td>536.50 (n/a)</td><td>275.20 (n/a)</td><td>148.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.86 <b>(-34.82%)</b></td><td>1.13 <b>(-44.76%)</b></td><td>1.38 <b>(-42.64%)</b></td><td>0.29 (+0.22%)</td><td>0.69 <b>(-32.19%)</b></td><td>3610.80 (-0.22%)</td><td>1517.54 <b>(+42.65%)</b></td><td>760.10 <b>(+74.33%)</b></td><td>562.60 <b>(+53.42%)</b></td><td>1308.97 (-8.39%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.86 (n/a)</td><td>2.05 (n/a)</td><td>2.41 (n/a)</td><td>0.29 (n/a)</td><td>1.02 (n/a)</td><td>3618.70 (n/a)</td><td>1063.82 (n/a)</td><td>436.00 (n/a)</td><td>366.70 (n/a)</td><td>1428.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.50 (-14.19%)</td><td>2.93 <b>(+66.76%)</b></td><td>3.01 <b>(+411.04%)</b></td><td>2.37 <b>(+314.61%)</b></td><td>0.53 <b>(-67.94%)</b></td><td>885.40 <b>(-75.88%)</b></td><td>736.48 <b>(-69.43%)</b></td><td>697.40 <b>(-80.43%)</b></td><td>599.10 (+16.53%)</td><td>137.15 <b>(-91.65%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>4.08 (n/a)</td><td>1.75 (n/a)</td><td>0.59 (n/a)</td><td>0.57 (n/a)</td><td>1.66 (n/a)</td><td>3670.90 (n/a)</td><td>2409.28 (n/a)</td><td>3564.00 (n/a)</td><td>514.10 (n/a)</td><td>1642.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.84 (-16.68%)</td><td>1.45 <b>(+38.00%)</b></td><td>1.69 <b>(+78.24%)</b></td><td>0.96 <b>(+263.93%)</b></td><td>0.45 <b>(-37.41%)</b></td><td>548.80 <b>(-72.52%)</b></td><td>395.72 <b>(-49.99%)</b></td><td>309.80 <b>(-43.89%)</b></td><td>285.20 <b>(+20.03%)</b></td><td>136.54 <b>(-80.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>2.21 (n/a)</td><td>1.05 (n/a)</td><td>0.95 (n/a)</td><td>0.26 (n/a)</td><td>0.71 (n/a)</td><td>1997.10 (n/a)</td><td>791.32 (n/a)</td><td>552.10 (n/a)</td><td>237.60 (n/a)</td><td>692.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (-3.21%)</td><td>0.08 (-6.51%)</td><td>0.07 (-14.25%)</td><td>0.02 <b>(-70.13%)</b></td><td>0.05 <b>(+47.89%)</b></td><td>2014.10 <b>(+234.79%)</b></td><td>702.30 <b>(+70.62%)</b></td><td>484.20 (+16.62%)</td><td>240.00 (+3.31%)</td><td>745.68 <b>(+399.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>601.60 (n/a)</td><td>411.62 (n/a)</td><td>415.20 (n/a)</td><td>232.30 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 <b>(-27.09%)</b></td><td>0.05 <b>(-33.36%)</b></td><td>0.05 (-16.47%)</td><td>0.02 <b>(-72.08%)</b></td><td>0.02 <b>(+37.97%)</b></td><td>2054.00 <b>(+258.21%)</b></td><td>891.28 <b>(+91.16%)</b></td><td>606.80 (+19.73%)</td><td>486.70 <b>(+37.18%)</b></td><td>660.66 <b>(+622.42%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>573.40 (n/a)</td><td>466.24 (n/a)</td><td>506.80 (n/a)</td><td>354.80 (n/a)</td><td>91.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.29 (+15.22%)</td><td>0.18 (-3.53%)</td><td>0.13 <b>(-39.57%)</b></td><td>0.10 (-8.92%)</td><td>0.09 <b>(+37.10%)</b></td><td>679.20 (+9.80%)</td><td>440.56 (+11.16%)</td><td>493.70 <b>(+65.50%)</b></td><td>226.80 (-13.20%)</td><td>194.55 <b>(+23.01%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>618.60 (n/a)</td><td>396.34 (n/a)</td><td>298.30 (n/a)</td><td>261.30 (n/a)</td><td>158.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.27 (-0.99%)</td><td>0.19 (+4.00%)</td><td>0.17 (+15.14%)</td><td>0.13 (+18.52%)</td><td>0.07 (-11.73%)</td><td>521.40 (-15.62%)</td><td>375.62 (-7.62%)</td><td>376.70 (-13.16%)</td><td>241.20 (+1.01%)</td><td>131.36 <b>(-20.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>617.90 (n/a)</td><td>406.62 (n/a)</td><td>433.80 (n/a)</td><td>238.80 (n/a)</td><td>164.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (-4.27%)</td><td>0.14 (-2.58%)</td><td>0.14 (-4.34%)</td><td>0.12 (+3.07%)</td><td>0.02 <b>(-28.30%)</b></td><td>558.80 (-2.99%)</td><td>467.40 (+1.61%)</td><td>456.80 (+4.53%)</td><td>405.00 (+4.46%)</td><td>57.89 <b>(-25.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>576.00 (n/a)</td><td>459.98 (n/a)</td><td>437.00 (n/a)</td><td>387.70 (n/a)</td><td>78.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.48 (-15.70%)</td><td>0.35 (-6.95%)</td><td>0.29 (-10.36%)</td><td>0.27 (+2.37%)</td><td>0.10 (-17.01%)</td><td>493.00 (-2.32%)</td><td>401.56 (+6.16%)</td><td>457.50 (+11.56%)</td><td>271.70 (+18.59%)</td><td>108.37 (-0.80%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.57 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>504.70 (n/a)</td><td>378.26 (n/a)</td><td>410.10 (n/a)</td><td>229.10 (n/a)</td><td>109.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.49 (-1.16%)</td><td>0.38 (+14.09%)</td><td>0.46 <b>(+44.19%)</b></td><td>0.25 (+19.75%)</td><td>0.12 (-3.80%)</td><td>529.40 (-16.50%)</td><td>372.50 (-14.05%)</td><td>287.30 <b>(-30.64%)</b></td><td>265.50 (+1.18%)</td><td>128.31 (-17.71%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>634.00 (n/a)</td><td>433.40 (n/a)</td><td>414.20 (n/a)</td><td>262.40 (n/a)</td><td>155.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.46 <b>(+22.22%)</b></td><td>0.36 <b>(+40.25%)</b></td><td>0.40 <b>(+71.70%)</b></td><td>0.24 <b>(+25.07%)</b></td><td>0.10 <b>(+35.01%)</b></td><td>542.00 <b>(-20.04%)</b></td><td>386.04 <b>(-27.84%)</b></td><td>329.50 <b>(-41.76%)</b></td><td>286.70 (-18.18%)</td><td>112.99 (-9.28%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>677.80 (n/a)</td><td>535.00 (n/a)</td><td>565.80 (n/a)</td><td>350.40 (n/a)</td><td>124.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 <b>(-26.61%)</b></td><td>0.05 <b>(-23.60%)</b></td><td>0.06 (-13.73%)</td><td>0.03 <b>(-28.65%)</b></td><td>0.01 (+5.44%)</td><td>469.40 <b>(+40.16%)</b></td><td>361.92 <b>(+34.65%)</b></td><td>295.50 (+15.88%)</td><td>287.10 <b>(+36.26%)</b></td><td>96.93 <b>(+101.94%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:36:50</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>334.90 (n/a)</td><td>268.78 (n/a)</td><td>255.00 (n/a)</td><td>210.70 (n/a)</td><td>48.00 (n/a)</td>
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
