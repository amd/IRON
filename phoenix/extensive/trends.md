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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 <b>(+28.31%)</b></td><td>0.02 <b>(+33.31%)</b></td><td>0.02 <b>(+64.74%)</b></td><td>0.01 (+14.98%)</td><td>0.01 (+4.49%)</td><td>472.60 (-13.03%)</td><td>282.66 <b>(-27.21%)</b></td><td>260.10 <b>(-39.30%)</b></td><td>174.50 <b>(-22.06%)</b></td><td>112.50 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>388.32 (n/a)</td><td>428.50 (n/a)</td><td>223.90 (n/a)</td><td>146.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 <b>(+24.16%)</b></td><td>0.02 (+9.49%)</td><td>0.02 (-11.14%)</td><td>0.02 <b>(+36.54%)</b></td><td>0.00 (-11.49%)</td><td>409.00 <b>(-26.76%)</b></td><td>335.24 (-12.82%)</td><td>333.70 (+12.55%)</td><td>228.10 (-19.46%)</td><td>70.29 <b>(-47.31%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.40 (n/a)</td><td>384.54 (n/a)</td><td>296.50 (n/a)</td><td>283.20 (n/a)</td><td>133.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-13.99%)</td><td>0.01 (-10.41%)</td><td>0.01 <b>(+23.84%)</b></td><td>0.00 <b>(-23.85%)</b></td><td>0.01 <b>(-24.09%)</b></td><td>2382.60 <b>(+31.32%)</b></td><td>820.22 (+12.04%)</td><td>479.60 (-19.26%)</td><td>238.00 (+16.27%)</td><td>883.57 <b>(+36.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1814.30 (n/a)</td><td>732.06 (n/a)</td><td>594.00 (n/a)</td><td>204.70 (n/a)</td><td>649.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+0.62%)</td><td>0.02 <b>(+23.88%)</b></td><td>0.02 <b>(+70.40%)</b></td><td>0.01 <b>(+22.12%)</b></td><td>0.00 <b>(-37.34%)</b></td><td>426.30 (-18.11%)</td><td>304.96 <b>(-24.67%)</b></td><td>278.40 <b>(-41.33%)</b></td><td>245.50 (-0.61%)</td><td>70.66 <b>(-47.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>404.82 (n/a)</td><td>474.50 (n/a)</td><td>247.00 (n/a)</td><td>134.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-7.84%)</td><td>0.02 <b>(+27.08%)</b></td><td>0.02 <b>(+75.73%)</b></td><td>0.01 (+4.06%)</td><td>0.01 (-9.66%)</td><td>620.90 (-3.90%)</td><td>390.92 <b>(-22.36%)</b></td><td>293.30 <b>(-43.09%)</b></td><td>248.50 (+8.47%)</td><td>165.74 (-1.95%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.10 (n/a)</td><td>503.52 (n/a)</td><td>515.40 (n/a)</td><td>229.10 (n/a)</td><td>169.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-4.64%)</td><td>0.02 (+14.16%)</td><td>0.01 (+6.51%)</td><td>0.01 (-0.25%)</td><td>0.01 (+3.28%)</td><td>633.80 (+0.24%)</td><td>420.82 (-10.28%)</td><td>460.20 (-6.12%)</td><td>216.40 (+4.90%)</td><td>183.42 (+11.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.30 (n/a)</td><td>469.06 (n/a)</td><td>490.20 (n/a)</td><td>206.30 (n/a)</td><td>165.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 <b>(+22.96%)</b></td><td>0.03 (+9.93%)</td><td>0.02 (-7.07%)</td><td>0.02 (+17.93%)</td><td>0.01 (+19.18%)</td><td>537.60 (-15.21%)</td><td>418.62 (-8.54%)</td><td>502.00 (+7.61%)</td><td>238.10 (-18.68%)</td><td>141.76 (-12.00%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>634.00 (n/a)</td><td>457.70 (n/a)</td><td>466.50 (n/a)</td><td>292.80 (n/a)</td><td>161.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (+16.05%)</td><td>0.04 <b>(+29.23%)</b></td><td>0.05 <b>(+56.07%)</b></td><td>0.02 <b>(+52.96%)</b></td><td>0.02 <b>(+20.69%)</b></td><td>526.00 <b>(-34.63%)</b></td><td>336.74 <b>(-23.80%)</b></td><td>246.20 <b>(-35.92%)</b></td><td>195.90 (-13.81%)</td><td>150.65 <b>(-31.02%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>804.60 (n/a)</td><td>441.94 (n/a)</td><td>384.20 (n/a)</td><td>227.30 (n/a)</td><td>218.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(+23.55%)</b></td><td>0.04 <b>(+46.98%)</b></td><td>0.04 <b>(+64.00%)</b></td><td>0.02 <b>(+301.36%)</b></td><td>0.02 (+17.64%)</td><td>617.10 <b>(-75.08%)</b></td><td>392.14 <b>(-52.67%)</b></td><td>291.20 <b>(-39.02%)</b></td><td>199.90 (-19.07%)</td><td>206.19 <b>(-77.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2476.70 (n/a)</td><td>828.58 (n/a)</td><td>477.50 (n/a)</td><td>247.00 (n/a)</td><td>926.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (+19.14%)</td><td>0.04 (+19.88%)</td><td>0.05 <b>(+67.36%)</b></td><td>0.01 <b>(+25.66%)</b></td><td>0.02 <b>(+22.96%)</b></td><td>1949.90 <b>(-20.42%)</b></td><td>647.30 (-16.45%)</td><td>251.30 <b>(-40.24%)</b></td><td>199.40 (-16.08%)</td><td>746.33 <b>(-20.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2450.10 (n/a)</td><td>774.76 (n/a)</td><td>420.50 (n/a)</td><td>237.60 (n/a)</td><td>943.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (-18.49%)</td><td>0.03 (-6.56%)</td><td>0.03 (-8.14%)</td><td>0.02 (+15.96%)</td><td>0.01 <b>(-37.72%)</b></td><td>525.10 (-13.76%)</td><td>399.34 (-2.78%)</td><td>451.10 (+8.86%)</td><td>271.50 <b>(+22.68%)</b></td><td>112.80 <b>(-35.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>608.90 (n/a)</td><td>410.74 (n/a)</td><td>414.40 (n/a)</td><td>221.30 (n/a)</td><td>176.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (+9.91%)</td><td>0.04 (+14.81%)</td><td>0.04 <b>(+26.94%)</b></td><td>0.02 (+12.20%)</td><td>0.01 (+17.98%)</td><td>575.10 (-10.86%)</td><td>374.92 (-12.03%)</td><td>295.80 <b>(-21.23%)</b></td><td>259.30 (-9.02%)</td><td>134.41 (-5.64%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.20 (n/a)</td><td>426.20 (n/a)</td><td>375.50 (n/a)</td><td>285.00 (n/a)</td><td>142.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 <b>(+20.28%)</b></td><td>0.08 (+15.01%)</td><td>0.10 <b>(+39.24%)</b></td><td>0.05 (-9.73%)</td><td>0.03 <b>(+40.81%)</b></td><td>543.50 (+10.76%)</td><td>342.10 (-7.18%)</td><td>253.20 <b>(-28.17%)</b></td><td>196.80 (-16.86%)</td><td>153.38 <b>(+29.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>490.70 (n/a)</td><td>368.58 (n/a)</td><td>352.50 (n/a)</td><td>236.70 (n/a)</td><td>118.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (-8.86%)</td><td>0.09 (+14.66%)</td><td>0.09 (+18.66%)</td><td>0.07 <b>(+42.99%)</b></td><td>0.02 <b>(-51.62%)</b></td><td>362.00 <b>(-30.06%)</b></td><td>279.20 <b>(-21.85%)</b></td><td>276.70 (-15.72%)</td><td>223.20 (+9.73%)</td><td>51.73 <b>(-63.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>517.60 (n/a)</td><td>357.24 (n/a)</td><td>328.30 (n/a)</td><td>203.40 (n/a)</td><td>142.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 <b>(-23.99%)</b></td><td>0.08 <b>(+32.28%)</b></td><td>0.09 <b>(+67.48%)</b></td><td>0.05 <b>(+304.51%)</b></td><td>0.02 <b>(-51.44%)</b></td><td>468.50 <b>(-75.28%)</b></td><td>329.10 <b>(-52.84%)</b></td><td>276.00 <b>(-40.29%)</b></td><td>250.50 <b>(+31.57%)</b></td><td>96.66 <b>(-85.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1895.10 (n/a)</td><td>697.88 (n/a)</td><td>462.20 (n/a)</td><td>190.40 (n/a)</td><td>680.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (-7.35%)</td><td>0.07 (+15.48%)</td><td>0.06 (+17.69%)</td><td>0.05 <b>(+274.38%)</b></td><td>0.03 <b>(-31.62%)</b></td><td>540.00 <b>(-73.29%)</b></td><td>395.26 <b>(-45.15%)</b></td><td>395.10 (-15.03%)</td><td>246.50 (+7.92%)</td><td>141.80 <b>(-80.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2021.50 (n/a)</td><td>720.62 (n/a)</td><td>465.00 (n/a)</td><td>228.40 (n/a)</td><td>742.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (+8.81%)</td><td>0.08 <b>(+29.90%)</b></td><td>0.08 <b>(+38.50%)</b></td><td>0.04 <b>(+23.67%)</b></td><td>0.02 (+2.48%)</td><td>559.30 (-19.14%)</td><td>348.24 <b>(-24.20%)</b></td><td>321.70 <b>(-27.81%)</b></td><td>248.60 (-8.10%)</td><td>124.03 <b>(-20.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>691.70 (n/a)</td><td>459.42 (n/a)</td><td>445.60 (n/a)</td><td>270.50 (n/a)</td><td>156.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (-6.89%)</td><td>0.08 (-9.11%)</td><td>0.08 (-4.72%)</td><td>0.05 (-15.12%)</td><td>0.03 <b>(+20.99%)</b></td><td>531.40 (+17.83%)</td><td>346.36 (+14.67%)</td><td>296.70 (+4.95%)</td><td>234.10 (+7.43%)</td><td>127.33 <b>(+44.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>451.00 (n/a)</td><td>302.04 (n/a)</td><td>282.70 (n/a)</td><td>217.90 (n/a)</td><td>88.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.21 (+17.68%)</td><td>0.15 (+5.33%)</td><td>0.16 (-4.72%)</td><td>0.09 (-6.22%)</td><td>0.05 (+18.17%)</td><td>523.90 (+6.64%)</td><td>346.52 (-3.62%)</td><td>306.60 (+4.93%)</td><td>228.80 (-15.04%)</td><td>115.37 (+8.04%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>491.30 (n/a)</td><td>359.52 (n/a)</td><td>292.20 (n/a)</td><td>269.30 (n/a)</td><td>106.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 <b>(+24.74%)</b></td><td>0.14 (+12.24%)</td><td>0.16 <b>(+22.89%)</b></td><td>0.10 (-11.13%)</td><td>0.04 <b>(+160.18%)</b></td><td>494.20 (+12.52%)</td><td>359.08 (-6.77%)</td><td>309.60 (-18.61%)</td><td>274.00 (-19.84%)</td><td>97.57 <b>(+135.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>439.20 (n/a)</td><td>385.14 (n/a)</td><td>380.40 (n/a)</td><td>341.80 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.23 <b>(+42.38%)</b></td><td>0.16 <b>(+20.65%)</b></td><td>0.16 (+16.73%)</td><td>0.09 (-1.52%)</td><td>0.05 <b>(+69.03%)</b></td><td>564.60 (+1.55%)</td><td>343.78 (-12.90%)</td><td>315.80 (-14.35%)</td><td>214.30 <b>(-29.76%)</b></td><td>131.64 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>556.00 (n/a)</td><td>394.68 (n/a)</td><td>368.70 (n/a)</td><td>305.10 (n/a)</td><td>102.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.19 (+2.82%)</td><td>0.15 <b>(+20.75%)</b></td><td>0.17 <b>(+54.45%)</b></td><td>0.08 (+3.72%)</td><td>0.05 (-1.05%)</td><td>598.90 (-3.59%)</td><td>358.94 (-17.84%)</td><td>281.60 <b>(-35.25%)</b></td><td>260.70 (-2.76%)</td><td>142.63 (-6.84%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>621.20 (n/a)</td><td>436.88 (n/a)</td><td>434.90 (n/a)</td><td>268.10 (n/a)</td><td>153.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 <b>(-42.07%)</b></td><td>0.10 <b>(-37.82%)</b></td><td>0.10 <b>(-47.33%)</b></td><td>0.04 <b>(+49.72%)</b></td><td>0.04 <b>(-51.68%)</b></td><td>1341.20 <b>(-33.21%)</b></td><td>637.26 (+2.63%)</td><td>494.20 <b>(+89.86%)</b></td><td>376.30 <b>(+72.61%)</b></td><td>403.05 <b>(-48.15%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2008.00 (n/a)</td><td>620.90 (n/a)</td><td>260.30 (n/a)</td><td>218.00 (n/a)</td><td>777.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 <b>(+61.88%)</b></td><td>0.10 <b>(+38.00%)</b></td><td>0.09 (-3.81%)</td><td>0.05 <b>(+109.25%)</b></td><td>0.05 (+15.63%)</td><td>1044.10 <b>(-52.21%)</b></td><td>603.44 <b>(-45.74%)</b></td><td>546.10 (+3.96%)</td><td>270.20 <b>(-38.24%)</b></td><td>280.20 <b>(-67.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2184.80 (n/a)</td><td>1112.22 (n/a)</td><td>525.30 (n/a)</td><td>437.50 (n/a)</td><td>867.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (+4.94%)</td><td>0.01 (+8.16%)</td><td>0.01 (-11.30%)</td><td>0.01 <b>(+68.00%)</b></td><td>0.00 (-6.43%)</td><td>459.70 <b>(-40.47%)</b></td><td>343.82 (-14.74%)</td><td>352.30 (+12.74%)</td><td>230.90 (-4.70%)</td><td>104.78 <b>(-50.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>772.20 (n/a)</td><td>403.28 (n/a)</td><td>312.50 (n/a)</td><td>242.30 (n/a)</td><td>213.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(+40.93%)</b></td><td>0.01 <b>(+49.94%)</b></td><td>0.01 <b>(+102.62%)</b></td><td>0.01 (+18.10%)</td><td>0.00 <b>(+115.24%)</b></td><td>497.10 (-15.33%)</td><td>346.78 <b>(-28.53%)</b></td><td>261.20 <b>(-50.64%)</b></td><td>240.20 <b>(-29.04%)</b></td><td>131.45 <b>(+35.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>587.10 (n/a)</td><td>485.20 (n/a)</td><td>529.20 (n/a)</td><td>338.50 (n/a)</td><td>97.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(+24.24%)</b></td><td>0.01 (+15.38%)</td><td>0.01 (+2.28%)</td><td>0.01 <b>(+26.92%)</b></td><td>0.00 (+13.67%)</td><td>355.20 <b>(-21.21%)</b></td><td>266.34 (-14.05%)</td><td>269.00 (-2.22%)</td><td>208.70 (-19.48%)</td><td>56.54 <b>(-29.43%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.80 (n/a)</td><td>309.88 (n/a)</td><td>275.10 (n/a)</td><td>259.20 (n/a)</td><td>80.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (+9.37%)</td><td>0.01 (-16.64%)</td><td>0.01 <b>(-34.62%)</b></td><td>0.00 <b>(-43.30%)</b></td><td>0.00 <b>(+45.77%)</b></td><td>989.80 <b>(+76.37%)</b></td><td>467.84 <b>(+41.30%)</b></td><td>418.30 <b>(+53.00%)</b></td><td>228.80 (-8.59%)</td><td>304.39 <b>(+133.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>561.20 (n/a)</td><td>331.10 (n/a)</td><td>273.40 (n/a)</td><td>250.30 (n/a)</td><td>130.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-28.31%)</b></td><td>0.01 (-14.13%)</td><td>0.01 (-1.86%)</td><td>0.00 <b>(-38.96%)</b></td><td>0.00 <b>(-21.62%)</b></td><td>766.10 <b>(+63.84%)</b></td><td>433.82 <b>(+21.24%)</b></td><td>423.70 (+1.88%)</td><td>245.10 <b>(+39.50%)</b></td><td>208.92 <b>(+77.21%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.60 (n/a)</td><td>357.82 (n/a)</td><td>415.90 (n/a)</td><td>175.70 (n/a)</td><td>117.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-16.28%)</td><td>0.01 (+9.61%)</td><td>0.01 <b>(+63.27%)</b></td><td>0.00 <b>(-26.04%)</b></td><td>0.00 (-8.91%)</td><td>784.60 <b>(+35.21%)</b></td><td>447.12 (-5.42%)</td><td>328.10 <b>(-38.75%)</b></td><td>281.40 (+19.44%)</td><td>213.35 <b>(+48.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>580.30 (n/a)</td><td>472.74 (n/a)</td><td>535.70 (n/a)</td><td>235.60 (n/a)</td><td>143.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+12.79%)</td><td>0.02 (-12.96%)</td><td>0.01 <b>(-36.72%)</b></td><td>0.01 (-6.59%)</td><td>0.01 <b>(+55.56%)</b></td><td>566.20 (+7.05%)</td><td>407.22 <b>(+24.40%)</b></td><td>451.50 <b>(+58.03%)</b></td><td>218.90 (-11.34%)</td><td>161.22 <b>(+40.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.90 (n/a)</td><td>327.34 (n/a)</td><td>285.70 (n/a)</td><td>246.90 (n/a)</td><td>114.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-4.67%)</td><td>0.02 (+10.15%)</td><td>0.01 (+9.28%)</td><td>0.01 (+4.66%)</td><td>0.01 (+1.40%)</td><td>499.90 (-4.45%)</td><td>373.88 (-9.03%)</td><td>423.50 (-8.49%)</td><td>244.70 (+4.89%)</td><td>115.61 (-0.33%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>411.00 (n/a)</td><td>462.80 (n/a)</td><td>233.30 (n/a)</td><td>116.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+13.49%)</td><td>0.02 (+6.56%)</td><td>0.01 (-14.78%)</td><td>0.01 <b>(-22.94%)</b></td><td>0.01 <b>(+82.43%)</b></td><td>620.60 <b>(+29.78%)</b></td><td>400.96 (+5.04%)</td><td>450.30 (+17.36%)</td><td>222.70 (-11.91%)</td><td>168.43 <b>(+101.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.20 (n/a)</td><td>381.72 (n/a)</td><td>383.70 (n/a)</td><td>252.80 (n/a)</td><td>83.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(+22.89%)</b></td><td>0.01 (+17.11%)</td><td>0.01 (+1.74%)</td><td>0.01 <b>(+133.37%)</b></td><td>0.01 (+0.87%)</td><td>782.80 <b>(-57.15%)</b></td><td>479.78 <b>(-32.48%)</b></td><td>485.00 (-1.70%)</td><td>263.90 (-18.62%)</td><td>202.52 <b>(-67.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1826.80 (n/a)</td><td>710.56 (n/a)</td><td>493.40 (n/a)</td><td>324.30 (n/a)</td><td>630.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-9.00%)</td><td>0.01 (-15.42%)</td><td>0.01 <b>(-25.98%)</b></td><td>0.01 (-9.84%)</td><td>0.00 (-16.63%)</td><td>619.90 (+10.91%)</td><td>495.72 (+17.30%)</td><td>473.00 <b>(+35.10%)</b></td><td>352.30 (+9.89%)</td><td>120.24 (+3.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.90 (n/a)</td><td>422.60 (n/a)</td><td>350.10 (n/a)</td><td>320.60 (n/a)</td><td>116.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(-27.19%)</b></td><td>0.01 (-7.77%)</td><td>0.01 (-4.91%)</td><td>0.01 (+13.78%)</td><td>0.00 <b>(-39.72%)</b></td><td>629.40 (-12.12%)</td><td>465.06 (+1.92%)</td><td>470.40 (+5.16%)</td><td>346.10 <b>(+37.34%)</b></td><td>120.16 <b>(-29.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>716.20 (n/a)</td><td>456.32 (n/a)</td><td>447.30 (n/a)</td><td>252.00 (n/a)</td><td>170.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (-4.37%)</td><td>0.03 (-4.31%)</td><td>0.03 (+1.26%)</td><td>0.02 (-11.48%)</td><td>0.01 <b>(+34.76%)</b></td><td>532.50 (+12.96%)</td><td>369.00 (+11.58%)</td><td>322.70 (-1.25%)</td><td>233.60 (+4.57%)</td><td>144.76 <b>(+60.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.40 (n/a)</td><td>330.70 (n/a)</td><td>326.80 (n/a)</td><td>223.40 (n/a)</td><td>90.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(+27.73%)</b></td><td>0.04 (+16.67%)</td><td>0.04 <b>(+22.90%)</b></td><td>0.02 (+11.03%)</td><td>0.01 <b>(+24.31%)</b></td><td>469.80 (-9.93%)</td><td>292.58 (-13.44%)</td><td>272.00 (-18.64%)</td><td>187.60 <b>(-21.70%)</b></td><td>105.19 (-6.81%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.60 (n/a)</td><td>338.02 (n/a)</td><td>334.30 (n/a)</td><td>239.60 (n/a)</td><td>112.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (-14.90%)</td><td>0.04 (+13.16%)</td><td>0.04 <b>(+88.77%)</b></td><td>0.02 (-2.20%)</td><td>0.01 (-11.36%)</td><td>583.10 (+2.24%)</td><td>346.68 (-12.31%)</td><td>241.90 <b>(-47.02%)</b></td><td>224.40 (+17.49%)</td><td>161.28 (+4.49%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>570.30 (n/a)</td><td>395.34 (n/a)</td><td>456.60 (n/a)</td><td>191.00 (n/a)</td><td>154.35 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (-5.59%)</td><td>0.03 (-14.25%)</td><td>0.02 <b>(-36.88%)</b></td><td>0.02 (-15.57%)</td><td>0.02 (+10.05%)</td><td>592.10 (+18.44%)</td><td>421.44 <b>(+24.03%)</b></td><td>506.40 <b>(+58.40%)</b></td><td>209.30 (+5.92%)</td><td>181.51 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>339.78 (n/a)</td><td>319.70 (n/a)</td><td>197.60 (n/a)</td><td>132.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (+12.00%)</td><td>0.03 <b>(+21.36%)</b></td><td>0.03 <b>(+51.61%)</b></td><td>0.02 (+3.42%)</td><td>0.01 <b>(+37.51%)</b></td><td>601.30 (-3.31%)</td><td>403.34 (-13.39%)</td><td>302.10 <b>(-34.04%)</b></td><td>260.60 (-10.72%)</td><td>165.99 <b>(+20.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>621.90 (n/a)</td><td>465.68 (n/a)</td><td>458.00 (n/a)</td><td>291.90 (n/a)</td><td>137.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (-19.33%)</td><td>0.02 (-10.67%)</td><td>0.02 (-2.78%)</td><td>0.02 <b>(-22.42%)</b></td><td>0.01 <b>(-25.71%)</b></td><td>654.80 <b>(+28.90%)</b></td><td>470.66 (+10.55%)</td><td>481.10 (+2.87%)</td><td>277.00 <b>(+23.94%)</b></td><td>137.77 <b>(+20.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.00 (n/a)</td><td>425.74 (n/a)</td><td>467.70 (n/a)</td><td>223.50 (n/a)</td><td>114.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 <b>(-21.05%)</b></td><td>0.05 (-17.55%)</td><td>0.04 (-17.49%)</td><td>0.03 (-19.66%)</td><td>0.01 <b>(-27.53%)</b></td><td>688.00 <b>(+24.48%)</b></td><td>497.22 (+19.44%)</td><td>511.80 <b>(+21.19%)</b></td><td>314.40 <b>(+26.67%)</b></td><td>135.84 (+11.88%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>552.70 (n/a)</td><td>416.28 (n/a)</td><td>422.30 (n/a)</td><td>248.20 (n/a)</td><td>121.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 <b>(+20.12%)</b></td><td>0.06 (+7.72%)</td><td>0.05 <b>(-31.04%)</b></td><td>0.04 <b>(+306.56%)</b></td><td>0.02 (-16.91%)</td><td>511.80 <b>(-75.40%)</b></td><td>386.20 <b>(-42.73%)</b></td><td>435.60 <b>(+45.01%)</b></td><td>220.40 (-16.77%)</td><td>131.91 <b>(-83.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2080.80 (n/a)</td><td>674.40 (n/a)</td><td>300.40 (n/a)</td><td>264.80 (n/a)</td><td>789.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-3.42%)</td><td>0.06 (+6.59%)</td><td>0.06 <b>(+46.17%)</b></td><td>0.03 <b>(-29.54%)</b></td><td>0.03 (+11.42%)</td><td>820.20 <b>(+41.93%)</b></td><td>445.52 (+0.52%)</td><td>371.70 <b>(-31.60%)</b></td><td>254.00 (+3.55%)</td><td>237.27 <b>(+49.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.90 (n/a)</td><td>443.22 (n/a)</td><td>543.40 (n/a)</td><td>245.30 (n/a)</td><td>158.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-7.67%)</td><td>0.05 <b>(-24.17%)</b></td><td>0.04 <b>(-29.03%)</b></td><td>0.03 (-9.38%)</td><td>0.02 (-12.37%)</td><td>600.50 (+10.35%)</td><td>495.50 <b>(+30.40%)</b></td><td>519.90 <b>(+40.89%)</b></td><td>254.30 (+8.30%)</td><td>140.85 (+1.60%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>544.20 (n/a)</td><td>379.98 (n/a)</td><td>369.00 (n/a)</td><td>234.80 (n/a)</td><td>138.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+5.28%)</td><td>0.06 (+19.31%)</td><td>0.07 <b>(+81.09%)</b></td><td>0.01 <b>(-65.77%)</b></td><td>0.03 <b>(+42.60%)</b></td><td>1899.40 <b>(+192.17%)</b></td><td>650.70 <b>(+31.40%)</b></td><td>300.20 <b>(-44.79%)</b></td><td>227.80 (-5.00%)</td><td>708.25 <b>(+359.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>650.10 (n/a)</td><td>495.22 (n/a)</td><td>543.70 (n/a)</td><td>239.80 (n/a)</td><td>154.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (-8.05%)</td><td>0.04 (-15.58%)</td><td>0.03 <b>(-26.64%)</b></td><td>0.03 (-14.75%)</td><td>0.02 (+0.08%)</td><td>665.00 (+17.30%)</td><td>549.10 <b>(+22.33%)</b></td><td>620.90 <b>(+36.31%)</b></td><td>242.00 (+8.76%)</td><td>175.21 <b>(+28.36%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>566.90 (n/a)</td><td>448.86 (n/a)</td><td>455.50 (n/a)</td><td>222.50 (n/a)</td><td>136.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>382.20 (n/a)</td><td>277.28 (n/a)</td><td>270.10 (n/a)</td><td>182.40 (n/a)</td><td>74.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.30 (n/a)</td><td>315.72 (n/a)</td><td>285.50 (n/a)</td><td>209.90 (n/a)</td><td>114.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2190.20 (n/a)</td><td>714.00 (n/a)</td><td>337.80 (n/a)</td><td>240.20 (n/a)</td><td>830.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>382.70 (n/a)</td><td>296.18 (n/a)</td><td>294.80 (n/a)</td><td>244.80 (n/a)</td><td>54.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.90 (n/a)</td><td>344.08 (n/a)</td><td>285.40 (n/a)</td><td>263.90 (n/a)</td><td>94.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2384.40 (n/a)</td><td>849.58 (n/a)</td><td>491.80 (n/a)</td><td>269.00 (n/a)</td><td>867.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.20 (n/a)</td><td>426.48 (n/a)</td><td>413.20 (n/a)</td><td>243.20 (n/a)</td><td>141.77 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>490.00 (n/a)</td><td>388.74 (n/a)</td><td>407.20 (n/a)</td><td>288.20 (n/a)</td><td>90.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>654.60 (n/a)</td><td>523.44 (n/a)</td><td>549.30 (n/a)</td><td>418.50 (n/a)</td><td>94.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.19 (+9.23%)</td><td>0.14 (-11.72%)</td><td>0.15 (-7.46%)</td><td>0.06 <b>(-54.34%)</b></td><td>0.05 <b>(+244.99%)</b></td><td>809.80 <b>(+118.98%)</b></td><td>416.88 <b>(+31.49%)</b></td><td>333.40 (+8.07%)</td><td>265.00 (-8.46%)</td><td>223.89 <b>(+624.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>369.80 (n/a)</td><td>317.04 (n/a)</td><td>308.50 (n/a)</td><td>289.50 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2433.10 (n/a)</td><td>756.24 (n/a)</td><td>276.40 (n/a)</td><td>241.40 (n/a)</td><td>947.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1904.20 (n/a)</td><td>701.90 (n/a)</td><td>478.60 (n/a)</td><td>269.40 (n/a)</td><td>680.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.40 (n/a)</td><td>440.76 (n/a)</td><td>467.70 (n/a)</td><td>359.70 (n/a)</td><td>74.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.50 (n/a)</td><td>447.06 (n/a)</td><td>475.50 (n/a)</td><td>278.10 (n/a)</td><td>99.05 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.60 (n/a)</td><td>507.98 (n/a)</td><td>553.60 (n/a)</td><td>319.90 (n/a)</td><td>110.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>368.14 (n/a)</td><td>299.20 (n/a)</td><td>274.50 (n/a)</td><td>116.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>606.80 (n/a)</td><td>478.26 (n/a)</td><td>470.90 (n/a)</td><td>389.10 (n/a)</td><td>83.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>469.62 (n/a)</td><td>536.30 (n/a)</td><td>220.20 (n/a)</td><td>148.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>753.40 (n/a)</td><td>533.12 (n/a)</td><td>446.20 (n/a)</td><td>290.60 (n/a)</td><td>203.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>642.30 (n/a)</td><td>416.24 (n/a)</td><td>429.00 (n/a)</td><td>189.40 (n/a)</td><td>179.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>495.10 (n/a)</td><td>356.00 (n/a)</td><td>306.80 (n/a)</td><td>247.10 (n/a)</td><td>105.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>677.10 (n/a)</td><td>477.66 (n/a)</td><td>515.20 (n/a)</td><td>207.20 (n/a)</td><td>173.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>551.10 (n/a)</td><td>367.38 (n/a)</td><td>299.70 (n/a)</td><td>166.30 (n/a)</td><td>164.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.02 <b>(-34.49%)</b></td><td>2.66 (-4.42%)</td><td>2.77 (+2.10%)</td><td>2.35 <b>(+57.67%)</b></td><td>0.29 <b>(-74.77%)</b></td><td>4468.10 <b>(-36.58%)</b></td><td>3977.92 (-7.29%)</td><td>3791.40 (-2.06%)</td><td>3468.80 <b>(+52.64%)</b></td><td>434.97 <b>(-75.01%)</b></td><td>1238.17 <b>(-34.49%)</b></td><td>1090.02 (-4.42%)</td><td>1132.82 (+2.10%)</td><td>961.26 <b>(+57.67%)</b></td><td>118.17 <b>(-74.77%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.61 (n/a)</td><td>2.78 (n/a)</td><td>2.71 (n/a)</td><td>1.49 (n/a)</td><td>1.14 (n/a)</td><td>7044.80 (n/a)</td><td>4290.74 (n/a)</td><td>3871.10 (n/a)</td><td>2272.50 (n/a)</td><td>1740.82 (n/a)</td><td>1889.94 (n/a)</td><td>1140.44 (n/a)</td><td>1109.49 (n/a)</td><td>609.66 (n/a)</td><td>468.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.73 (+0.99%)</td><td>3.13 (+0.81%)</td><td>3.18 (-3.39%)</td><td>2.52 (+2.38%)</td><td>0.44 (-15.52%)</td><td>9362.60 (-2.32%)</td><td>7668.92 (-1.54%)</td><td>7411.50 (+3.51%)</td><td>6324.10 (-0.98%)</td><td>1114.40 (-18.58%)</td><td>2122.32 (+0.99%)</td><td>1778.96 (+0.81%)</td><td>1810.94 (-3.39%)</td><td>1433.55 (+2.38%)</td><td>250.23 (-15.52%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.69 (n/a)</td><td>3.10 (n/a)</td><td>3.30 (n/a)</td><td>2.46 (n/a)</td><td>0.52 (n/a)</td><td>9585.30 (n/a)</td><td>7788.88 (n/a)</td><td>7160.00 (n/a)</td><td>6386.40 (n/a)</td><td>1368.70 (n/a)</td><td>2101.61 (n/a)</td><td>1764.66 (n/a)</td><td>1874.55 (n/a)</td><td>1400.25 (n/a)</td><td>296.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.20 (-19.90%)</td><td>2.63 (-14.92%)</td><td>2.77 (-4.75%)</td><td>2.14 (+3.54%)</td><td>0.46 <b>(-38.71%)</b></td><td>7842.90 (-3.42%)</td><td>6548.80 (+14.40%)</td><td>6046.10 (+4.99%)</td><td>5250.30 <b>(+24.84%)</b></td><td>1183.71 <b>(-22.87%)</b></td><td>1636.09 (-19.90%)</td><td>1345.90 (-14.92%)</td><td>1420.74 (-4.75%)</td><td>1095.25 (+3.54%)</td><td>237.71 <b>(-38.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.99 (n/a)</td><td>3.09 (n/a)</td><td>2.91 (n/a)</td><td>2.07 (n/a)</td><td>0.76 (n/a)</td><td>8120.40 (n/a)</td><td>5724.58 (n/a)</td><td>5758.70 (n/a)</td><td>4205.60 (n/a)</td><td>1534.64 (n/a)</td><td>2042.48 (n/a)</td><td>1581.93 (n/a)</td><td>1491.63 (n/a)</td><td>1057.82 (n/a)</td><td>387.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.88 (-16.55%)</td><td>0.58 <b>(-29.38%)</b></td><td>0.62 <b>(-26.23%)</b></td><td>0.26 <b>(-58.71%)</b></td><td>0.23 <b>(+41.25%)</b></td><td>1790.60 <b>(+142.17%)</b></td><td>947.78 <b>(+63.29%)</b></td><td>741.20 <b>(+35.55%)</b></td><td>520.20 (+19.83%)</td><td>501.62 <b>(+329.83%)</b></td><td>64.50 (-16.55%)</td><td>42.18 <b>(-29.38%)</b></td><td>45.27 <b>(-26.23%)</b></td><td>18.74 <b>(-58.71%)</b></td><td>17.14 <b>(+41.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.06 (n/a)</td><td>0.82 (n/a)</td><td>0.84 (n/a)</td><td>0.62 (n/a)</td><td>0.17 (n/a)</td><td>739.40 (n/a)</td><td>580.44 (n/a)</td><td>546.80 (n/a)</td><td>434.10 (n/a)</td><td>116.70 (n/a)</td><td>77.29 (n/a)</td><td>59.73 (n/a)</td><td>61.36 (n/a)</td><td>45.38 (n/a)</td><td>12.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.30 (-2.57%)</td><td>1.08 (+4.50%)</td><td>1.17 <b>(+29.25%)</b></td><td>0.84 (+1.70%)</td><td>0.19 <b>(-21.80%)</b></td><td>778.50 (-1.67%)</td><td>623.84 (-5.86%)</td><td>560.60 <b>(-22.63%)</b></td><td>504.00 (+2.63%)</td><td>118.20 <b>(-20.12%)</b></td><td>133.14 (-2.57%)</td><td>110.58 (+4.50%)</td><td>119.71 <b>(+29.25%)</b></td><td>86.21 (+1.70%)</td><td>19.90 <b>(-21.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.33 (n/a)</td><td>1.03 (n/a)</td><td>0.90 (n/a)</td><td>0.83 (n/a)</td><td>0.25 (n/a)</td><td>791.70 (n/a)</td><td>662.64 (n/a)</td><td>724.60 (n/a)</td><td>491.10 (n/a)</td><td>147.98 (n/a)</td><td>136.65 (n/a)</td><td>105.81 (n/a)</td><td>92.62 (n/a)</td><td>84.77 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.59 (+5.00%)</td><td>1.30 (+15.54%)</td><td>1.30 (+1.34%)</td><td>1.04 <b>(+238.19%)</b></td><td>0.21 <b>(-58.55%)</b></td><td>724.70 <b>(-70.43%)</b></td><td>592.56 <b>(-38.09%)</b></td><td>578.40 (-1.31%)</td><td>473.60 (-4.77%)</td><td>94.87 <b>(-88.72%)</b></td><td>177.11 (+5.00%)</td><td>144.50 (+15.54%)</td><td>145.04 (+1.34%)</td><td>115.75 <b>(+238.19%)</b></td><td>23.13 <b>(-58.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.52 (n/a)</td><td>1.12 (n/a)</td><td>1.29 (n/a)</td><td>0.31 (n/a)</td><td>0.50 (n/a)</td><td>2450.90 (n/a)</td><td>957.10 (n/a)</td><td>586.10 (n/a)</td><td>497.30 (n/a)</td><td>841.35 (n/a)</td><td>168.67 (n/a)</td><td>125.07 (n/a)</td><td>143.12 (n/a)</td><td>34.23 (n/a)</td><td>55.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.48 (-0.03%)</td><td>1.15 <b>(+22.26%)</b></td><td>1.21 (+8.77%)</td><td>0.48 (+2.47%)</td><td>0.39 (-9.23%)</td><td>2169.60 (-2.41%)</td><td>1074.10 <b>(-21.01%)</b></td><td>866.00 (-8.06%)</td><td>706.80 (+0.03%)</td><td>616.43 (-11.17%)</td><td>189.89 (-0.03%)</td><td>147.62 <b>(+22.26%)</b></td><td>154.99 (+8.77%)</td><td>61.86 (+2.47%)</td><td>50.28 (-9.23%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.48 (n/a)</td><td>0.94 (n/a)</td><td>1.11 (n/a)</td><td>0.47 (n/a)</td><td>0.43 (n/a)</td><td>2223.20 (n/a)</td><td>1359.82 (n/a)</td><td>941.90 (n/a)</td><td>706.60 (n/a)</td><td>693.97 (n/a)</td><td>189.95 (n/a)</td><td>120.74 (n/a)</td><td>142.49 (n/a)</td><td>60.37 (n/a)</td><td>55.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.74 (-12.73%)</td><td>1.30 <b>(-20.64%)</b></td><td>1.34 <b>(-30.56%)</b></td><td>0.42 <b>(-60.17%)</b></td><td>0.53 <b>(+22.84%)</b></td><td>2484.60 <b>(+151.07%)</b></td><td>1057.36 <b>(+55.02%)</b></td><td>784.90 <b>(+44.02%)</b></td><td>604.20 (+14.58%)</td><td>803.48 <b>(+284.10%)</b></td><td>222.13 (-12.73%)</td><td>166.94 <b>(-20.64%)</b></td><td>170.99 <b>(-30.56%)</b></td><td>54.02 <b>(-60.17%)</b></td><td>68.42 <b>(+22.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.99 (n/a)</td><td>1.64 (n/a)</td><td>1.92 (n/a)</td><td>1.06 (n/a)</td><td>0.44 (n/a)</td><td>989.60 (n/a)</td><td>682.06 (n/a)</td><td>545.00 (n/a)</td><td>527.30 (n/a)</td><td>209.18 (n/a)</td><td>254.55 (n/a)</td><td>210.35 (n/a)</td><td>246.25 (n/a)</td><td>135.62 (n/a)</td><td>55.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.00 (-7.43%)</td><td>1.29 (-17.34%)</td><td>1.42 (+4.12%)</td><td>0.57 <b>(-48.22%)</b></td><td>0.69 <b>(+61.65%)</b></td><td>1853.10 <b>(+93.11%)</b></td><td>1099.56 <b>(+54.10%)</b></td><td>738.30 (-3.95%)</td><td>523.10 (+8.01%)</td><td>678.37 <b>(+266.18%)</b></td><td>256.58 (-7.43%)</td><td>164.67 (-17.34%)</td><td>181.80 (+4.12%)</td><td>72.43 <b>(-48.22%)</b></td><td>88.08 <b>(+61.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.17 (n/a)</td><td>1.56 (n/a)</td><td>1.36 (n/a)</td><td>1.09 (n/a)</td><td>0.43 (n/a)</td><td>959.60 (n/a)</td><td>713.52 (n/a)</td><td>768.70 (n/a)</td><td>484.30 (n/a)</td><td>185.26 (n/a)</td><td>277.17 (n/a)</td><td>199.21 (n/a)</td><td>174.61 (n/a)</td><td>139.87 (n/a)</td><td>54.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.90 (+2.80%)</td><td>1.28 (+17.14%)</td><td>1.42 <b>(+45.73%)</b></td><td>0.43 (+0.80%)</td><td>0.54 <b>(-20.59%)</b></td><td>2430.40 (-0.79%)</td><td>1060.36 <b>(-22.63%)</b></td><td>740.00 <b>(-31.39%)</b></td><td>553.00 (-2.71%)</td><td>773.26 (-12.22%)</td><td>242.73 (+2.80%)</td><td>164.31 (+17.14%)</td><td>181.37 <b>(+45.73%)</b></td><td>55.23 (+0.80%)</td><td>68.54 <b>(-20.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.84 (n/a)</td><td>1.10 (n/a)</td><td>0.97 (n/a)</td><td>0.43 (n/a)</td><td>0.67 (n/a)</td><td>2449.70 (n/a)</td><td>1370.46 (n/a)</td><td>1078.50 (n/a)</td><td>568.40 (n/a)</td><td>880.88 (n/a)</td><td>236.13 (n/a)</td><td>140.27 (n/a)</td><td>124.45 (n/a)</td><td>54.79 (n/a)</td><td>86.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.47 (-16.25%)</td><td>1.18 (-11.20%)</td><td>1.21 <b>(-20.39%)</b></td><td>0.81 <b>(+67.06%)</b></td><td>0.25 <b>(-50.53%)</b></td><td>1297.20 <b>(-40.14%)</b></td><td>929.44 (-5.94%)</td><td>864.40 <b>(+25.62%)</b></td><td>713.40 (+19.40%)</td><td>225.04 <b>(-66.13%)</b></td><td>188.14 (-16.25%)</td><td>150.46 (-11.20%)</td><td>155.28 <b>(-20.39%)</b></td><td>103.47 <b>(+67.06%)</b></td><td>31.77 <b>(-50.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.75 (n/a)</td><td>1.32 (n/a)</td><td>1.52 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>2167.00 (n/a)</td><td>988.18 (n/a)</td><td>688.10 (n/a)</td><td>597.50 (n/a)</td><td>664.46 (n/a)</td><td>224.63 (n/a)</td><td>169.44 (n/a)</td><td>195.05 (n/a)</td><td>61.94 (n/a)</td><td>64.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.68 (+11.08%)</td><td>1.41 <b>(+50.35%)</b></td><td>1.47 <b>(+35.38%)</b></td><td>1.02 <b>(+143.76%)</b></td><td>0.25 <b>(-48.80%)</b></td><td>1023.30 <b>(-58.98%)</b></td><td>767.30 <b>(-48.39%)</b></td><td>713.40 <b>(-26.13%)</b></td><td>623.00 (-9.97%)</td><td>156.16 <b>(-82.54%)</b></td><td>215.44 (+11.08%)</td><td>180.10 <b>(+50.35%)</b></td><td>188.14 <b>(+35.38%)</b></td><td>131.16 <b>(+143.76%)</b></td><td>32.13 <b>(-48.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.52 (n/a)</td><td>0.94 (n/a)</td><td>1.09 (n/a)</td><td>0.42 (n/a)</td><td>0.49 (n/a)</td><td>2494.50 (n/a)</td><td>1486.70 (n/a)</td><td>965.80 (n/a)</td><td>692.00 (n/a)</td><td>894.20 (n/a)</td><td>193.95 (n/a)</td><td>119.79 (n/a)</td><td>138.97 (n/a)</td><td>53.81 (n/a)</td><td>62.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.67 (-13.60%)</td><td>0.52 (-13.29%)</td><td>0.58 (+12.07%)</td><td>0.15 <b>(-70.63%)</b></td><td>0.22 <b>(+75.09%)</b></td><td>2441.60 <b>(+240.48%)</b></td><td>970.06 <b>(+55.04%)</b></td><td>622.60 (-10.78%)</td><td>534.10 (+15.73%)</td><td>826.09 <b>(+605.49%)</b></td><td>31.41 (-13.60%)</td><td>24.00 (-13.29%)</td><td>26.95 (+12.07%)</td><td>6.87 <b>(-70.63%)</b></td><td>10.15 <b>(+75.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.78 (n/a)</td><td>0.59 (n/a)</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>717.10 (n/a)</td><td>625.70 (n/a)</td><td>697.80 (n/a)</td><td>461.50 (n/a)</td><td>117.10 (n/a)</td><td>36.35 (n/a)</td><td>27.68 (n/a)</td><td>24.04 (n/a)</td><td>23.40 (n/a)</td><td>5.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.04 (+0.26%)</td><td>1.92 <b>(+25.47%)</b></td><td>2.06 <b>(+85.52%)</b></td><td>0.98 (+1.25%)</td><td>0.89 (+4.04%)</td><td>4273.10 (-1.23%)</td><td>2678.24 (-17.64%)</td><td>2038.90 <b>(-46.10%)</b></td><td>1380.10 (-0.25%)</td><td>1350.56 (+16.23%)</td><td>778.02 (+0.26%)</td><td>490.64 <b>(+25.47%)</b></td><td>526.63 <b>(+85.51%)</b></td><td>251.28 (+1.25%)</td><td>228.67 (+4.04%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.03 (n/a)</td><td>1.53 (n/a)</td><td>1.11 (n/a)</td><td>0.97 (n/a)</td><td>0.86 (n/a)</td><td>4326.50 (n/a)</td><td>3251.76 (n/a)</td><td>3782.50 (n/a)</td><td>1383.60 (n/a)</td><td>1162.02 (n/a)</td><td>776.02 (n/a)</td><td>391.06 (n/a)</td><td>283.87 (n/a)</td><td>248.18 (n/a)</td><td>219.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.61 (-7.54%)</td><td>3.18 <b>(+20.59%)</b></td><td>3.58 <b>(+40.00%)</b></td><td>2.06 <b>(+202.47%)</b></td><td>0.67 <b>(-49.84%)</b></td><td>1270.40 <b>(-66.94%)</b></td><td>862.68 <b>(-41.77%)</b></td><td>731.90 <b>(-28.57%)</b></td><td>725.60 (+8.15%)</td><td>234.50 <b>(-82.48%)</b></td><td>739.85 (-7.54%)</td><td>651.83 <b>(+20.59%)</b></td><td>733.49 <b>(+40.00%)</b></td><td>422.61 <b>(+202.47%)</b></td><td>136.64 <b>(-49.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.91 (n/a)</td><td>2.64 (n/a)</td><td>2.56 (n/a)</td><td>0.68 (n/a)</td><td>1.33 (n/a)</td><td>3842.50 (n/a)</td><td>1481.60 (n/a)</td><td>1024.70 (n/a)</td><td>670.90 (n/a)</td><td>1338.39 (n/a)</td><td>800.20 (n/a)</td><td>540.55 (n/a)</td><td>523.93 (n/a)</td><td>139.72 (n/a)</td><td>272.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.86 (-16.69%)</td><td>2.39 (+3.19%)</td><td>2.72 <b>(+27.68%)</b></td><td>1.65 (+5.16%)</td><td>0.57 (-17.35%)</td><td>4779.50 (-4.91%)</td><td>3476.90 (-4.28%)</td><td>2888.70 <b>(-21.68%)</b></td><td>2754.40 <b>(+20.04%)</b></td><td>938.25 (-5.60%)</td><td>877.12 (-16.69%)</td><td>732.81 (+3.19%)</td><td>836.32 <b>(+27.68%)</b></td><td>505.47 (+5.16%)</td><td>176.53 (-17.35%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.43 (n/a)</td><td>2.31 (n/a)</td><td>2.13 (n/a)</td><td>1.56 (n/a)</td><td>0.70 (n/a)</td><td>5026.10 (n/a)</td><td>3632.38 (n/a)</td><td>3688.30 (n/a)</td><td>2294.60 (n/a)</td><td>993.90 (n/a)</td><td>1052.88 (n/a)</td><td>710.15 (n/a)</td><td>655.03 (n/a)</td><td>480.67 (n/a)</td><td>213.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.90 (n/a)</td><td>433.82 (n/a)</td><td>430.00 (n/a)</td><td>338.10 (n/a)</td><td>69.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.70 (n/a)</td><td>316.26 (n/a)</td><td>296.50 (n/a)</td><td>214.60 (n/a)</td><td>125.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.90 (n/a)</td><td>382.52 (n/a)</td><td>404.40 (n/a)</td><td>272.50 (n/a)</td><td>97.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1828.70 (n/a)</td><td>750.76 (n/a)</td><td>564.10 (n/a)</td><td>251.60 (n/a)</td><td>620.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.50 (n/a)</td><td>360.32 (n/a)</td><td>419.90 (n/a)</td><td>230.10 (n/a)</td><td>117.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.30 (n/a)</td><td>482.06 (n/a)</td><td>497.80 (n/a)</td><td>217.50 (n/a)</td><td>161.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>764.30 (n/a)</td><td>433.80 (n/a)</td><td>373.20 (n/a)</td><td>245.40 (n/a)</td><td>208.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1034.70 (n/a)</td><td>574.44 (n/a)</td><td>524.80 (n/a)</td><td>234.00 (n/a)</td><td>297.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.50 (n/a)</td><td>358.06 (n/a)</td><td>302.20 (n/a)</td><td>236.90 (n/a)</td><td>124.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1940.00 (n/a)</td><td>645.58 (n/a)</td><td>403.80 (n/a)</td><td>218.10 (n/a)</td><td>729.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.10 (n/a)</td><td>432.92 (n/a)</td><td>484.50 (n/a)</td><td>182.40 (n/a)</td><td>172.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2028.00 (n/a)</td><td>819.14 (n/a)</td><td>488.90 (n/a)</td><td>273.50 (n/a)</td><td>703.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>617.60 (n/a)</td><td>471.96 (n/a)</td><td>500.10 (n/a)</td><td>303.20 (n/a)</td><td>134.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.80 (n/a)</td><td>472.58 (n/a)</td><td>480.10 (n/a)</td><td>311.60 (n/a)</td><td>126.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1957.20 (n/a)</td><td>704.84 (n/a)</td><td>446.70 (n/a)</td><td>285.30 (n/a)</td><td>708.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>665.70 (n/a)</td><td>477.38 (n/a)</td><td>519.70 (n/a)</td><td>269.80 (n/a)</td><td>153.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.40 (n/a)</td><td>394.24 (n/a)</td><td>442.20 (n/a)</td><td>226.20 (n/a)</td><td>143.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>639.10 (n/a)</td><td>519.56 (n/a)</td><td>553.30 (n/a)</td><td>282.90 (n/a)</td><td>136.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>3284.80 (n/a)</td><td>1059.80 (n/a)</td><td>521.10 (n/a)</td><td>327.20 (n/a)</td><td>1249.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>606.60 (n/a)</td><td>450.60 (n/a)</td><td>495.60 (n/a)</td><td>325.90 (n/a)</td><td>122.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>677.60 (n/a)</td><td>485.98 (n/a)</td><td>506.20 (n/a)</td><td>227.40 (n/a)</td><td>162.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>621.30 (n/a)</td><td>517.14 (n/a)</td><td>567.90 (n/a)</td><td>245.30 (n/a)</td><td>153.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>626.60 (n/a)</td><td>538.92 (n/a)</td><td>594.30 (n/a)</td><td>406.50 (n/a)</td><td>94.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>474.94 (n/a)</td><td>455.60 (n/a)</td><td>365.90 (n/a)</td><td>88.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 <b>(-35.88%)</b></td><td>0.39 <b>(-20.91%)</b></td><td>0.34 (-14.31%)</td><td>0.30 (-14.33%)</td><td>0.10 <b>(-49.03%)</b></td><td>732.70 (+16.73%)</td><td>597.52 <b>(+20.40%)</b></td><td>650.20 (+16.71%)</td><td>432.80 <b>(+55.96%)</b></td><td>136.57 (-8.82%)</td><td>21.81 <b>(-35.88%)</b></td><td>16.54 <b>(-20.91%)</b></td><td>14.51 (-14.31%)</td><td>12.88 (-14.33%)</td><td>4.08 <b>(-49.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.80 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>627.70 (n/a)</td><td>496.28 (n/a)</td><td>557.10 (n/a)</td><td>277.50 (n/a)</td><td>149.78 (n/a)</td><td>34.01 (n/a)</td><td>20.91 (n/a)</td><td>16.94 (n/a)</td><td>15.03 (n/a)</td><td>8.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.58 (-17.95%)</td><td>0.42 (-3.01%)</td><td>0.43 <b>(+26.02%)</b></td><td>0.22 (+18.16%)</td><td>0.15 <b>(-30.64%)</b></td><td>1002.80 (-15.38%)</td><td>600.02 (-6.56%)</td><td>509.20 <b>(-20.65%)</b></td><td>380.00 <b>(+21.87%)</b></td><td>256.51 <b>(-26.17%)</b></td><td>24.84 (-17.95%)</td><td>17.84 (-3.01%)</td><td>18.53 <b>(+26.02%)</b></td><td>9.41 (+18.16%)</td><td>6.41 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.71 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>1185.00 (n/a)</td><td>642.12 (n/a)</td><td>641.70 (n/a)</td><td>311.80 (n/a)</td><td>347.45 (n/a)</td><td>30.27 (n/a)</td><td>18.40 (n/a)</td><td>14.71 (n/a)</td><td>7.96 (n/a)</td><td>9.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.31 (+1.02%)</td><td>0.31 (+1.31%)</td><td>0.31 (+1.35%)</td><td>0.30 (+2.92%)</td><td>0.01 <b>(-33.42%)</b></td><td>83656.10 (-2.84%)</td><td>81655.92 (-1.32%)</td><td>81244.30 (-1.33%)</td><td>80202.40 (-1.01%)</td><td>1335.73 <b>(-35.86%)</b></td><td>214.21 (+1.02%)</td><td>210.44 (+1.31%)</td><td>211.46 (+1.35%)</td><td>205.36 (+2.92%)</td><td>3.42 <b>(-33.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86099.60 (n/a)</td><td>82751.54 (n/a)</td><td>82341.70 (n/a)</td><td>81016.80 (n/a)</td><td>2082.45 (n/a)</td><td>212.05 (n/a)</td><td>207.71 (n/a)</td><td>208.64 (n/a)</td><td>199.53 (n/a)</td><td>5.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.15 (-1.91%)</td><td>1.12 (-1.86%)</td><td>1.14 (-0.30%)</td><td>1.06 (-5.10%)</td><td>0.04 <b>(+96.74%)</b></td><td>23727.10 (+5.38%)</td><td>22421.32 (+1.96%)</td><td>22057.80 (+0.30%)</td><td>21957.10 (+1.95%)</td><td>743.99 <b>(+111.73%)</b></td><td>782.43 (-1.91%)</td><td>766.88 (-1.86%)</td><td>778.86 (-0.30%)</td><td>724.06 (-5.10%)</td><td>24.46 <b>(+96.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.12 (n/a)</td><td>0.02 (n/a)</td><td>22516.30 (n/a)</td><td>21989.64 (n/a)</td><td>21990.90 (n/a)</td><td>21537.20 (n/a)</td><td>351.38 (n/a)</td><td>797.68 (n/a)</td><td>781.43 (n/a)</td><td>781.23 (n/a)</td><td>763.00 (n/a)</td><td>12.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (-1.04%)</td><td>0.78 (-0.80%)</td><td>0.79 (-1.23%)</td><td>0.77 (-0.33%)</td><td>0.01 <b>(-30.41%)</b></td><td>97906.40 (+0.33%)</td><td>96502.08 (+0.80%)</td><td>96122.80 (+1.24%)</td><td>95856.90 (+1.06%)</td><td>863.93 <b>(-29.34%)</b></td><td>716.90 (-1.04%)</td><td>712.15 (-0.80%)</td><td>714.91 (-1.23%)</td><td>701.89 (-0.33%)</td><td>6.33 <b>(-30.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97586.70 (n/a)</td><td>95737.92 (n/a)</td><td>94942.00 (n/a)</td><td>94855.50 (n/a)</td><td>1222.69 (n/a)</td><td>724.46 (n/a)</td><td>717.88 (n/a)</td><td>723.81 (n/a)</td><td>704.19 (n/a)</td><td>9.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.78 (+1.20%)</td><td>0.77 (+1.93%)</td><td>0.77 (+1.06%)</td><td>0.77 (+3.45%)</td><td>0.00 <b>(-57.39%)</b></td><td>98427.30 (-3.34%)</td><td>97787.04 (-1.91%)</td><td>97939.80 (-1.05%)</td><td>97030.30 (-1.19%)</td><td>616.13 <b>(-59.33%)</b></td><td>708.23 (+1.20%)</td><td>702.77 (+1.93%)</td><td>701.65 (+1.06%)</td><td>698.17 (+3.45%)</td><td>4.43 <b>(-57.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101825.60 (n/a)</td><td>99690.20 (n/a)</td><td>98974.60 (n/a)</td><td>98195.90 (n/a)</td><td>1514.80 (n/a)</td><td>699.82 (n/a)</td><td>689.46 (n/a)</td><td>694.31 (n/a)</td><td>674.87 (n/a)</td><td>10.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.90 (+0.81%)</td><td>0.88 (+4.66%)</td><td>0.88 (-0.26%)</td><td>0.86 <b>(+27.08%)</b></td><td>0.01 <b>(-85.13%)</b></td><td>87647.80 <b>(-21.31%)</b></td><td>85881.12 (-5.48%)</td><td>86089.60 (+0.26%)</td><td>84324.00 (-0.80%)</td><td>1322.10 <b>(-88.49%)</b></td><td>814.95 (+0.81%)</td><td>800.32 (+4.66%)</td><td>798.23 (-0.26%)</td><td>784.04 <b>(+27.08%)</b></td><td>12.30 <b>(-85.13%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.88 (n/a)</td><td>0.68 (n/a)</td><td>0.09 (n/a)</td><td>111382.60 (n/a)</td><td>90857.32 (n/a)</td><td>85868.80 (n/a)</td><td>85005.00 (n/a)</td><td>11486.84 (n/a)</td><td>808.42 (n/a)</td><td>764.71 (n/a)</td><td>800.28 (n/a)</td><td>616.97 (n/a)</td><td>82.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.31 (-17.38%)</td><td>3.25 (+13.40%)</td><td>3.56 <b>(+48.99%)</b></td><td>2.17 (+5.39%)</td><td>1.00 <b>(-24.99%)</b></td><td>4099.90 (-5.11%)</td><td>2985.80 (-14.54%)</td><td>2503.90 <b>(-32.88%)</b></td><td>2066.60 <b>(+21.04%)</b></td><td>991.65 (-4.93%)</td><td>259.78 (-17.38%)</td><td>195.65 (+13.40%)</td><td>214.41 <b>(+48.99%)</b></td><td>130.95 (+5.39%)</td><td>60.02 <b>(-24.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.22 (n/a)</td><td>2.86 (n/a)</td><td>2.39 (n/a)</td><td>2.06 (n/a)</td><td>1.33 (n/a)</td><td>4320.80 (n/a)</td><td>3493.74 (n/a)</td><td>3730.70 (n/a)</td><td>1707.40 (n/a)</td><td>1043.02 (n/a)</td><td>314.44 (n/a)</td><td>172.53 (n/a)</td><td>143.91 (n/a)</td><td>124.25 (n/a)</td><td>80.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.91 <b>(-39.73%)</b></td><td>2.33 (-11.98%)</td><td>2.22 (-0.31%)</td><td>2.06 (+8.96%)</td><td>0.34 <b>(-72.71%)</b></td><td>4336.60 (-8.22%)</td><td>3886.96 (+2.65%)</td><td>4019.40 (+0.31%)</td><td>3063.50 <b>(+65.91%)</b></td><td>485.28 <b>(-56.95%)</b></td><td>175.25 <b>(-39.73%)</b></td><td>140.13 (-11.98%)</td><td>133.57 (-0.31%)</td><td>123.80 (+8.96%)</td><td>20.21 <b>(-72.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.83 (n/a)</td><td>2.64 (n/a)</td><td>2.22 (n/a)</td><td>1.89 (n/a)</td><td>1.23 (n/a)</td><td>4725.10 (n/a)</td><td>3786.76 (n/a)</td><td>4006.80 (n/a)</td><td>1846.50 (n/a)</td><td>1127.23 (n/a)</td><td>290.76 (n/a)</td><td>159.20 (n/a)</td><td>133.99 (n/a)</td><td>113.62 (n/a)</td><td>74.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.95 (+2.90%)</td><td>4.06 (-12.00%)</td><td>4.17 (-5.22%)</td><td>1.95 <b>(-34.85%)</b></td><td>1.90 <b>(+60.33%)</b></td><td>4578.80 <b>(+53.50%)</b></td><td>2714.48 <b>(+32.25%)</b></td><td>2135.90 (+5.51%)</td><td>1499.10 (-2.81%)</td><td>1416.43 <b>(+139.63%)</b></td><td>358.13 (+2.90%)</td><td>244.36 (-12.00%)</td><td>251.35 (-5.22%)</td><td>117.25 <b>(-34.85%)</b></td><td>114.58 <b>(+60.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.78 (n/a)</td><td>4.61 (n/a)</td><td>4.40 (n/a)</td><td>2.99 (n/a)</td><td>1.19 (n/a)</td><td>2982.90 (n/a)</td><td>2052.52 (n/a)</td><td>2024.40 (n/a)</td><td>1542.50 (n/a)</td><td>591.08 (n/a)</td><td>348.04 (n/a)</td><td>277.68 (n/a)</td><td>265.21 (n/a)</td><td>179.98 (n/a)</td><td>71.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.78 <b>(+23.08%)</b></td><td>5.24 (+10.47%)</td><td>4.75 (-5.20%)</td><td>4.25 (+18.91%)</td><td>1.09 <b>(+40.62%)</b></td><td>8204.00 (-15.90%)</td><td>6867.78 (-8.73%)</td><td>7340.90 (+5.48%)</td><td>5144.50 (-18.75%)</td><td>1325.59 (-4.52%)</td><td>417.43 <b>(+23.08%)</b></td><td>323.04 (+10.47%)</td><td>292.54 (-5.20%)</td><td>261.76 (+18.91%)</td><td>67.35 <b>(+40.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.51 (n/a)</td><td>4.75 (n/a)</td><td>5.01 (n/a)</td><td>3.57 (n/a)</td><td>0.78 (n/a)</td><td>9755.40 (n/a)</td><td>7524.58 (n/a)</td><td>6959.20 (n/a)</td><td>6332.00 (n/a)</td><td>1388.35 (n/a)</td><td>339.15 (n/a)</td><td>292.42 (n/a)</td><td>308.58 (n/a)</td><td>220.13 (n/a)</td><td>47.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.26 (-12.35%)</td><td>4.58 (-8.27%)</td><td>4.52 (-13.63%)</td><td>3.78 (-4.27%)</td><td>0.63 <b>(-29.49%)</b></td><td>9217.20 (+4.46%)</td><td>7738.88 (+7.76%)</td><td>7716.70 (+15.79%)</td><td>6625.50 (+14.09%)</td><td>1093.35 (-18.71%)</td><td>324.12 (-12.35%)</td><td>281.89 (-8.27%)</td><td>278.29 (-13.63%)</td><td>232.99 (-4.27%)</td><td>39.07 <b>(-29.49%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.00 (n/a)</td><td>4.99 (n/a)</td><td>5.23 (n/a)</td><td>3.95 (n/a)</td><td>0.90 (n/a)</td><td>8824.00 (n/a)</td><td>7181.58 (n/a)</td><td>6664.60 (n/a)</td><td>5807.30 (n/a)</td><td>1344.93 (n/a)</td><td>369.79 (n/a)</td><td>307.30 (n/a)</td><td>322.22 (n/a)</td><td>243.37 (n/a)</td><td>55.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.20 (+16.82%)</td><td>6.06 (+12.19%)</td><td>6.81 <b>(+21.92%)</b></td><td>4.20 (-3.05%)</td><td>1.41 <b>(+96.98%)</b></td><td>8294.20 (+3.15%)</td><td>6046.26 (-7.77%)</td><td>5117.70 (-17.98%)</td><td>4840.90 (-14.40%)</td><td>1576.08 <b>(+67.45%)</b></td><td>443.61 (+16.82%)</td><td>373.16 (+12.19%)</td><td>419.62 <b>(+21.92%)</b></td><td>258.91 (-3.05%)</td><td>86.67 <b>(+96.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.17 (n/a)</td><td>5.40 (n/a)</td><td>5.59 (n/a)</td><td>4.34 (n/a)</td><td>0.71 (n/a)</td><td>8040.90 (n/a)</td><td>6555.56 (n/a)</td><td>6239.30 (n/a)</td><td>5655.10 (n/a)</td><td>941.25 (n/a)</td><td>379.74 (n/a)</td><td>332.61 (n/a)</td><td>344.18 (n/a)</td><td>267.07 (n/a)</td><td>44.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (+1.88%)</td><td>0.77 (+0.45%)</td><td>0.77 (+0.47%)</td><td>0.75 (+1.24%)</td><td>0.02 <b>(+21.10%)</b></td><td>100827.30 (-1.23%)</td><td>98263.48 (-0.44%)</td><td>97962.50 (-0.47%)</td><td>95369.30 (-1.84%)</td><td>2343.95 (+17.54%)</td><td>720.56 (+1.88%)</td><td>699.66 (+0.45%)</td><td>701.49 (+0.47%)</td><td>681.56 (+1.24%)</td><td>16.70 <b>(+21.10%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102081.10 (n/a)</td><td>98693.10 (n/a)</td><td>98420.40 (n/a)</td><td>97159.60 (n/a)</td><td>1994.22 (n/a)</td><td>707.28 (n/a)</td><td>696.52 (n/a)</td><td>698.22 (n/a)</td><td>673.19 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.79 (-0.19%)</td><td>0.76 (-1.62%)</td><td>0.75 (-3.14%)</td><td>0.73 (-2.91%)</td><td>0.02 <b>(+70.92%)</b></td><td>102901.00 (+3.00%)</td><td>99619.92 (+1.71%)</td><td>100715.90 (+3.24%)</td><td>95968.20 (+0.19%)</td><td>3185.01 <b>(+75.27%)</b></td><td>716.07 (-0.19%)</td><td>690.39 (-1.62%)</td><td>682.31 (-3.14%)</td><td>667.82 (-2.91%)</td><td>22.24 <b>(+70.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99901.80 (n/a)</td><td>97948.38 (n/a)</td><td>97553.40 (n/a)</td><td>95783.90 (n/a)</td><td>1817.16 (n/a)</td><td>717.44 (n/a)</td><td>701.78 (n/a)</td><td>704.43 (n/a)</td><td>687.87 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.90 (+0.09%)</td><td>0.89 (-0.69%)</td><td>0.89 (-1.01%)</td><td>0.87 (-0.59%)</td><td>0.01 (+9.51%)</td><td>86823.30 (+0.60%)</td><td>85186.02 (+0.70%)</td><td>85228.30 (+1.02%)</td><td>83836.00 (-0.09%)</td><td>1079.22 (+10.04%)</td><td>819.69 (+0.09%)</td><td>806.80 (-0.69%)</td><td>806.30 (-1.01%)</td><td>791.49 (-0.59%)</td><td>10.18 (+9.51%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86307.30 (n/a)</td><td>84597.48 (n/a)</td><td>84369.20 (n/a)</td><td>83913.20 (n/a)</td><td>980.76 (n/a)</td><td>818.94 (n/a)</td><td>812.40 (n/a)</td><td>814.51 (n/a)</td><td>796.22 (n/a)</td><td>9.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.22 (-0.62%)</td><td>2.97 (+1.09%)</td><td>3.41 (-5.91%)</td><td>1.52 (+7.42%)</td><td>1.11 (-14.91%)</td><td>5304.50 (-6.91%)</td><td>3123.46 (-7.26%)</td><td>2365.50 (+6.28%)</td><td>1909.40 (+0.63%)</td><td>1415.60 <b>(-20.48%)</b></td><td>1107.12 (-0.62%)</td><td>779.48 (+1.09%)</td><td>893.66 (-5.91%)</td><td>398.52 (+7.42%)</td><td>291.77 (-14.91%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.25 (n/a)</td><td>2.94 (n/a)</td><td>3.62 (n/a)</td><td>1.41 (n/a)</td><td>1.31 (n/a)</td><td>5698.10 (n/a)</td><td>3367.82 (n/a)</td><td>2225.70 (n/a)</td><td>1897.50 (n/a)</td><td>1780.24 (n/a)</td><td>1114.07 (n/a)</td><td>771.11 (n/a)</td><td>949.77 (n/a)</td><td>370.99 (n/a)</td><td>342.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.30 (+8.72%)</td><td>0.21 (+0.86%)</td><td>0.20 (-8.91%)</td><td>0.17 (-1.11%)</td><td>0.05 (+12.36%)</td><td>7517.10 (+1.13%)</td><td>6047.52 (-0.62%)</td><td>6185.30 (+9.78%)</td><td>4099.20 (-8.02%)</td><td>1232.89 (-4.82%)</td><td>16.37 (+8.72%)</td><td>11.55 (+0.86%)</td><td>10.85 (-8.91%)</td><td>8.93 (-1.11%)</td><td>2.82 (+12.36%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>7433.30 (n/a)</td><td>6085.52 (n/a)</td><td>5634.10 (n/a)</td><td>4456.60 (n/a)</td><td>1295.36 (n/a)</td><td>15.06 (n/a)</td><td>11.45 (n/a)</td><td>11.91 (n/a)</td><td>9.03 (n/a)</td><td>2.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.77 (n/a)</td><td>3.58 (n/a)</td><td>3.54 (n/a)</td><td>3.40 (n/a)</td><td>0.14 (n/a)</td><td>3.77 (n/a)</td><td>3.57 (n/a)</td><td>3.54 (n/a)</td><td>3.40 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.32 (+7.08%)</td><td>6.26 (-3.90%)</td><td>6.92 (+3.57%)</td><td>5.02 (-15.43%)</td><td>1.12 <b>(+186.69%)</b></td><td>7.32 (+7.08%)</td><td>6.26 (-3.90%)</td><td>6.91 (+3.57%)</td><td>5.01 (-15.43%)</td><td>1.12 <b>(+186.69%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.84 (n/a)</td><td>6.52 (n/a)</td><td>6.68 (n/a)</td><td>5.93 (n/a)</td><td>0.39 (n/a)</td><td>6.83 (n/a)</td><td>6.51 (n/a)</td><td>6.68 (n/a)</td><td>5.93 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>13.24 (-5.79%)</td><td>9.68 (-5.66%)</td><td>8.59 (+3.86%)</td><td>8.26 (+10.79%)</td><td>2.08 <b>(-34.25%)</b></td><td>13.24 (-5.79%)</td><td>9.68 (-5.66%)</td><td>8.58 (+3.86%)</td><td>8.25 (+10.79%)</td><td>2.08 <b>(-34.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>14.06 (n/a)</td><td>10.26 (n/a)</td><td>8.27 (n/a)</td><td>7.45 (n/a)</td><td>3.16 (n/a)</td><td>14.05 (n/a)</td><td>10.26 (n/a)</td><td>8.26 (n/a)</td><td>7.45 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.92 (n/a)</td><td>3.59 (n/a)</td><td>3.62 (n/a)</td><td>3.21 (n/a)</td><td>0.27 (n/a)</td><td>3.92 (n/a)</td><td>3.58 (n/a)</td><td>3.62 (n/a)</td><td>3.21 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.30 (+6.84%)</td><td>6.31 (-0.85%)</td><td>6.40 (-5.59%)</td><td>5.20 (-7.77%)</td><td>0.86 <b>(+43.96%)</b></td><td>7.30 (+6.84%)</td><td>6.31 (-0.85%)</td><td>6.40 (-5.59%)</td><td>5.20 (-7.77%)</td><td>0.86 <b>(+43.96%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>6.83 (n/a)</td><td>6.37 (n/a)</td><td>6.78 (n/a)</td><td>5.64 (n/a)</td><td>0.60 (n/a)</td><td>6.83 (n/a)</td><td>6.37 (n/a)</td><td>6.78 (n/a)</td><td>5.64 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>13.87 (+1.24%)</td><td>9.74 (-10.49%)</td><td>9.66 <b>(-26.04%)</b></td><td>7.42 (+18.46%)</td><td>2.53 <b>(-25.18%)</b></td><td>13.86 (+1.24%)</td><td>9.73 (-10.49%)</td><td>9.66 <b>(-26.04%)</b></td><td>7.42 (+18.46%)</td><td>2.53 <b>(-25.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>13.69 (n/a)</td><td>10.88 (n/a)</td><td>13.07 (n/a)</td><td>6.27 (n/a)</td><td>3.38 (n/a)</td><td>13.69 (n/a)</td><td>10.87 (n/a)</td><td>13.06 (n/a)</td><td>6.26 (n/a)</td><td>3.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.11 (+9.53%)</td><td>2.53 <b>(+41.22%)</b></td><td>2.79 <b>(+91.90%)</b></td><td>1.21 (+3.44%)</td><td>0.75 (+2.93%)</td><td>3.10 (+9.53%)</td><td>2.52 <b>(+41.22%)</b></td><td>2.78 <b>(+91.90%)</b></td><td>1.20 (+3.44%)</td><td>0.75 (+2.93%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.84 (n/a)</td><td>1.79 (n/a)</td><td>1.45 (n/a)</td><td>1.17 (n/a)</td><td>0.73 (n/a)</td><td>2.83 (n/a)</td><td>1.79 (n/a)</td><td>1.45 (n/a)</td><td>1.16 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.56 (+3.39%)</td><td>0.30 <b>(-39.19%)</b></td><td>0.35 <b>(-33.50%)</b></td><td>0.08 <b>(-80.01%)</b></td><td>0.20 <b>(+203.99%)</b></td><td>0.55 (+3.39%)</td><td>0.29 <b>(-39.19%)</b></td><td>0.34 <b>(-33.50%)</b></td><td>0.07 <b>(-80.01%)</b></td><td>0.20 <b>(+204.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.69 (-5.46%)</td><td>0.59 (+16.94%)</td><td>0.64 <b>(+44.38%)</b></td><td>0.30 (-12.58%)</td><td>0.16 (-6.80%)</td><td>0.68 (-5.46%)</td><td>0.58 (+16.94%)</td><td>0.63 <b>(+44.38%)</b></td><td>0.29 (-12.58%)</td><td>0.16 (-6.80%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.73 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.72 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.38 (-11.28%)</td><td>1.20 (+18.84%)</td><td>0.78 (+7.44%)</td><td>0.46 (+6.17%)</td><td>0.88 (-6.29%)</td><td>2.34 (-11.28%)</td><td>1.19 (+18.84%)</td><td>0.77 (+7.44%)</td><td>0.46 (+6.17%)</td><td>0.87 (-6.29%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.68 (n/a)</td><td>1.01 (n/a)</td><td>0.73 (n/a)</td><td>0.44 (n/a)</td><td>0.94 (n/a)</td><td>2.64 (n/a)</td><td>1.00 (n/a)</td><td>0.72 (n/a)</td><td>0.43 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.60 (n/a)</td><td>348.30 (n/a)</td><td>294.70 (n/a)</td><td>243.90 (n/a)</td><td>108.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.20 (n/a)</td><td>404.72 (n/a)</td><td>410.80 (n/a)</td><td>270.00 (n/a)</td><td>105.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.00 (n/a)</td><td>336.94 (n/a)</td><td>299.80 (n/a)</td><td>216.50 (n/a)</td><td>141.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.10 (n/a)</td><td>446.44 (n/a)</td><td>567.80 (n/a)</td><td>207.20 (n/a)</td><td>188.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1930.40 (n/a)</td><td>646.24 (n/a)</td><td>323.10 (n/a)</td><td>239.30 (n/a)</td><td>722.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.50 (n/a)</td><td>480.86 (n/a)</td><td>498.80 (n/a)</td><td>324.90 (n/a)</td><td>95.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2064.50 (n/a)</td><td>739.70 (n/a)</td><td>400.90 (n/a)</td><td>370.50 (n/a)</td><td>741.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.80 (n/a)</td><td>386.46 (n/a)</td><td>293.50 (n/a)</td><td>247.60 (n/a)</td><td>157.20 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.60 (n/a)</td><td>370.28 (n/a)</td><td>284.80 (n/a)</td><td>249.20 (n/a)</td><td>149.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.20 (n/a)</td><td>400.10 (n/a)</td><td>432.80 (n/a)</td><td>239.00 (n/a)</td><td>127.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.30 (n/a)</td><td>372.64 (n/a)</td><td>344.20 (n/a)</td><td>219.80 (n/a)</td><td>134.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.30 (n/a)</td><td>486.12 (n/a)</td><td>487.80 (n/a)</td><td>327.50 (n/a)</td><td>151.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>606.90 (n/a)</td><td>389.54 (n/a)</td><td>292.70 (n/a)</td><td>255.40 (n/a)</td><td>158.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>406.76 (n/a)</td><td>307.60 (n/a)</td><td>289.40 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.20 (n/a)</td><td>428.00 (n/a)</td><td>454.30 (n/a)</td><td>254.80 (n/a)</td><td>148.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.70 (n/a)</td><td>397.62 (n/a)</td><td>361.70 (n/a)</td><td>239.20 (n/a)</td><td>128.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1062.50 (n/a)</td><td>505.58 (n/a)</td><td>459.10 (n/a)</td><td>239.50 (n/a)</td><td>334.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>630.10 (n/a)</td><td>452.24 (n/a)</td><td>476.60 (n/a)</td><td>306.20 (n/a)</td><td>125.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>550.40 (n/a)</td><td>366.52 (n/a)</td><td>282.00 (n/a)</td><td>262.10 (n/a)</td><td>133.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>539.50 (n/a)</td><td>390.84 (n/a)</td><td>326.60 (n/a)</td><td>262.70 (n/a)</td><td>121.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.80 (n/a)</td><td>386.94 (n/a)</td><td>331.50 (n/a)</td><td>252.70 (n/a)</td><td>128.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1983.40 (n/a)</td><td>832.24 (n/a)</td><td>656.20 (n/a)</td><td>233.50 (n/a)</td><td>688.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>639.20 (n/a)</td><td>397.58 (n/a)</td><td>304.40 (n/a)</td><td>258.90 (n/a)</td><td>161.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>571.00 (n/a)</td><td>434.48 (n/a)</td><td>470.70 (n/a)</td><td>295.80 (n/a)</td><td>108.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(+24.48%)</b></td><td>0.02 <b>(+33.49%)</b></td><td>0.02 <b>(+42.77%)</b></td><td>0.01 (+19.88%)</td><td>0.01 (+15.03%)</td><td>507.70 (-16.58%)</td><td>296.98 <b>(-25.74%)</b></td><td>262.20 <b>(-29.97%)</b></td><td>187.20 (-19.66%)</td><td>124.13 (-18.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.60 (n/a)</td><td>399.92 (n/a)</td><td>374.40 (n/a)</td><td>233.00 (n/a)</td><td>152.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-7.02%)</td><td>0.01 (-12.68%)</td><td>0.01 <b>(+24.00%)</b></td><td>0.00 <b>(-73.86%)</b></td><td>0.00 (+7.21%)</td><td>2419.50 <b>(+282.53%)</b></td><td>803.44 <b>(+74.31%)</b></td><td>400.70 (-19.36%)</td><td>293.60 (+7.55%)</td><td>906.91 <b>(+416.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>632.50 (n/a)</td><td>460.92 (n/a)</td><td>496.90 (n/a)</td><td>273.00 (n/a)</td><td>175.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+11.49%)</td><td>0.01 (+4.34%)</td><td>0.01 <b>(-23.71%)</b></td><td>0.01 <b>(+44.58%)</b></td><td>0.00 (-9.40%)</td><td>487.90 <b>(-30.83%)</b></td><td>350.54 (-11.93%)</td><td>383.30 <b>(+31.09%)</b></td><td>207.90 (-10.27%)</td><td>112.51 <b>(-44.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>705.40 (n/a)</td><td>398.02 (n/a)</td><td>292.40 (n/a)</td><td>231.70 (n/a)</td><td>202.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-19.33%)</td><td>0.01 (-4.94%)</td><td>0.01 (+16.22%)</td><td>0.01 (+1.34%)</td><td>0.00 <b>(-29.37%)</b></td><td>585.10 (-1.33%)</td><td>440.08 (-2.40%)</td><td>498.50 (-13.96%)</td><td>268.80 <b>(+23.99%)</b></td><td>148.93 <b>(-20.10%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.00 (n/a)</td><td>450.88 (n/a)</td><td>579.40 (n/a)</td><td>216.80 (n/a)</td><td>186.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-3.76%)</td><td>0.01 (-9.90%)</td><td>0.01 <b>(-26.69%)</b></td><td>0.01 <b>(+46.43%)</b></td><td>0.00 <b>(-22.23%)</b></td><td>540.40 <b>(-31.71%)</b></td><td>362.16 (-1.52%)</td><td>354.20 <b>(+36.39%)</b></td><td>244.00 (+3.92%)</td><td>120.77 <b>(-49.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>791.30 (n/a)</td><td>367.74 (n/a)</td><td>259.70 (n/a)</td><td>234.80 (n/a)</td><td>238.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-26.87%)</b></td><td>0.01 <b>(-24.50%)</b></td><td>0.01 <b>(-23.93%)</b></td><td>0.01 <b>(-24.08%)</b></td><td>0.00 <b>(-23.31%)</b></td><td>616.90 <b>(+31.70%)</b></td><td>454.50 <b>(+33.23%)</b></td><td>403.00 <b>(+31.44%)</b></td><td>311.00 <b>(+36.70%)</b></td><td>133.30 <b>(+41.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.40 (n/a)</td><td>341.14 (n/a)</td><td>306.60 (n/a)</td><td>227.50 (n/a)</td><td>94.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-2.30%)</td><td>0.03 (-13.76%)</td><td>0.03 <b>(-21.91%)</b></td><td>0.02 <b>(-20.81%)</b></td><td>0.00 <b>(+45.87%)</b></td><td>377.10 <b>(+26.25%)</b></td><td>302.46 (+17.73%)</td><td>311.80 <b>(+28.05%)</b></td><td>239.60 (+2.35%)</td><td>52.83 <b>(+88.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>298.70 (n/a)</td><td>256.90 (n/a)</td><td>243.50 (n/a)</td><td>234.10 (n/a)</td><td>28.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-7.33%)</td><td>0.03 (-2.78%)</td><td>0.03 (+10.82%)</td><td>0.02 (-10.87%)</td><td>0.01 (+5.54%)</td><td>487.20 (+12.21%)</td><td>349.04 (+4.57%)</td><td>295.00 (-9.76%)</td><td>259.20 (+7.91%)</td><td>103.25 <b>(+27.14%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>434.20 (n/a)</td><td>333.78 (n/a)</td><td>326.90 (n/a)</td><td>240.20 (n/a)</td><td>81.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (+8.12%)</td><td>0.02 (-16.24%)</td><td>0.02 <b>(-37.43%)</b></td><td>0.01 <b>(-48.95%)</b></td><td>0.01 <b>(+67.76%)</b></td><td>942.10 <b>(+95.90%)</b></td><td>514.12 <b>(+45.17%)</b></td><td>515.90 <b>(+59.82%)</b></td><td>226.50 (-7.51%)</td><td>286.05 <b>(+184.56%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.90 (n/a)</td><td>354.16 (n/a)</td><td>322.80 (n/a)</td><td>244.90 (n/a)</td><td>100.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-10.10%)</td><td>0.02 <b>(-23.38%)</b></td><td>0.02 <b>(-43.80%)</b></td><td>0.01 (+8.71%)</td><td>0.01 (-6.74%)</td><td>586.00 (-8.01%)</td><td>426.10 <b>(+27.40%)</b></td><td>465.60 <b>(+77.98%)</b></td><td>269.80 (+11.26%)</td><td>147.52 (-13.16%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.00 (n/a)</td><td>334.46 (n/a)</td><td>261.60 (n/a)</td><td>242.50 (n/a)</td><td>169.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (+18.82%)</td><td>0.02 (+0.45%)</td><td>0.02 (-3.40%)</td><td>0.01 (+18.00%)</td><td>0.01 (+3.17%)</td><td>644.70 (-15.25%)</td><td>457.64 (-3.61%)</td><td>481.30 (+3.51%)</td><td>230.50 (-15.85%)</td><td>161.31 <b>(-22.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>760.70 (n/a)</td><td>474.76 (n/a)</td><td>465.00 (n/a)</td><td>273.90 (n/a)</td><td>209.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+5.50%)</td><td>0.02 (+1.43%)</td><td>0.02 (+10.56%)</td><td>0.01 (+9.27%)</td><td>0.01 (-7.14%)</td><td>618.60 (-8.48%)</td><td>466.96 (-4.14%)</td><td>486.50 (-9.56%)</td><td>274.60 (-5.21%)</td><td>128.11 <b>(-21.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.90 (n/a)</td><td>487.12 (n/a)</td><td>537.90 (n/a)</td><td>289.70 (n/a)</td><td>163.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 <b>(+66.06%)</b></td><td>0.03 <b>(+29.72%)</b></td><td>0.02 (-5.72%)</td><td>0.01 (-7.93%)</td><td>0.02 <b>(+151.53%)</b></td><td>549.30 (+8.60%)</td><td>398.72 (-9.45%)</td><td>499.50 (+6.07%)</td><td>162.20 <b>(-39.79%)</b></td><td>169.50 <b>(+74.31%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.80 (n/a)</td><td>440.34 (n/a)</td><td>470.90 (n/a)</td><td>269.40 (n/a)</td><td>97.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(-25.02%)</b></td><td>0.01 <b>(-22.58%)</b></td><td>0.02 (-7.52%)</td><td>0.00 <b>(-72.91%)</b></td><td>0.01 (-0.69%)</td><td>2178.80 <b>(+269.23%)</b></td><td>820.60 <b>(+77.02%)</b></td><td>535.10 (+8.12%)</td><td>341.60 <b>(+33.33%)</b></td><td>763.65 <b>(+510.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.10 (n/a)</td><td>463.56 (n/a)</td><td>494.90 (n/a)</td><td>256.20 (n/a)</td><td>125.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (+12.61%)</td><td>0.04 <b>(-29.51%)</b></td><td>0.03 <b>(-40.91%)</b></td><td>0.02 <b>(-34.72%)</b></td><td>0.02 <b>(+90.90%)</b></td><td>656.70 <b>(+53.18%)</b></td><td>500.70 <b>(+60.08%)</b></td><td>504.40 <b>(+69.26%)</b></td><td>218.80 (-11.17%)</td><td>173.53 <b>(+143.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>428.70 (n/a)</td><td>312.78 (n/a)</td><td>298.00 (n/a)</td><td>246.30 (n/a)</td><td>71.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (-1.26%)</td><td>0.05 (-3.69%)</td><td>0.05 <b>(+35.39%)</b></td><td>0.01 <b>(-78.11%)</b></td><td>0.02 <b>(+28.78%)</b></td><td>2492.00 <b>(+356.91%)</b></td><td>749.48 <b>(+89.37%)</b></td><td>306.20 <b>(-26.15%)</b></td><td>236.90 (+1.28%)</td><td>977.11 <b>(+557.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.40 (n/a)</td><td>395.78 (n/a)</td><td>414.60 (n/a)</td><td>233.90 (n/a)</td><td>148.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (-18.18%)</td><td>0.04 (-9.29%)</td><td>0.03 <b>(-20.11%)</b></td><td>0.03 (+14.47%)</td><td>0.02 (-18.87%)</td><td>628.90 (-12.63%)</td><td>470.32 (+5.96%)</td><td>554.60 <b>(+25.16%)</b></td><td>278.30 <b>(+22.22%)</b></td><td>167.51 (-13.37%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>719.80 (n/a)</td><td>443.88 (n/a)</td><td>443.10 (n/a)</td><td>227.70 (n/a)</td><td>193.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (-11.22%)</td><td>0.04 (-6.70%)</td><td>0.03 (-7.31%)</td><td>0.03 (+6.99%)</td><td>0.02 (-15.17%)</td><td>580.20 (-6.54%)</td><td>423.16 (+3.99%)</td><td>475.80 (+7.89%)</td><td>258.10 (+12.66%)</td><td>150.06 (-9.34%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.80 (n/a)</td><td>406.94 (n/a)</td><td>441.00 (n/a)</td><td>229.10 (n/a)</td><td>165.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (-8.52%)</td><td>0.03 <b>(-33.76%)</b></td><td>0.03 <b>(-36.04%)</b></td><td>0.01 <b>(-77.92%)</b></td><td>0.02 <b>(+35.78%)</b></td><td>2470.30 <b>(+353.02%)</b></td><td>850.06 <b>(+140.63%)</b></td><td>495.10 <b>(+56.33%)</b></td><td>264.00 (+9.32%)</td><td>911.97 <b>(+665.70%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>545.30 (n/a)</td><td>353.26 (n/a)</td><td>316.70 (n/a)</td><td>241.50 (n/a)</td><td>119.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-16.38%)</td><td>0.05 (+0.57%)</td><td>0.05 (+18.04%)</td><td>0.03 (+0.23%)</td><td>0.02 <b>(-27.91%)</b></td><td>486.70 (-0.23%)</td><td>365.74 (-4.78%)</td><td>353.00 (-15.29%)</td><td>216.90 (+19.57%)</td><td>114.13 (-8.43%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.80 (n/a)</td><td>384.10 (n/a)</td><td>416.70 (n/a)</td><td>181.40 (n/a)</td><td>124.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+5.07%)</td><td>0.10 (+4.56%)</td><td>0.10 (-2.64%)</td><td>0.06 (+17.03%)</td><td>0.04 (-9.72%)</td><td>549.90 (-14.55%)</td><td>364.54 (-9.62%)</td><td>312.90 (+2.72%)</td><td>225.70 (-4.81%)</td><td>143.33 <b>(-26.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>643.50 (n/a)</td><td>403.36 (n/a)</td><td>304.60 (n/a)</td><td>237.10 (n/a)</td><td>194.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (+18.27%)</td><td>0.12 <b>(+36.47%)</b></td><td>0.12 <b>(+66.89%)</b></td><td>0.08 <b>(+25.30%)</b></td><td>0.02 (-2.91%)</td><td>433.20 <b>(-20.19%)</b></td><td>297.30 <b>(-28.21%)</b></td><td>264.10 <b>(-40.09%)</b></td><td>246.60 (-15.43%)</td><td>78.04 <b>(-30.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>542.80 (n/a)</td><td>414.10 (n/a)</td><td>440.80 (n/a)</td><td>291.60 (n/a)</td><td>112.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 <b>(+21.73%)</b></td><td>0.11 (+14.92%)</td><td>0.11 (-6.69%)</td><td>0.08 <b>(+48.58%)</b></td><td>0.03 (-4.60%)</td><td>423.10 <b>(-32.69%)</b></td><td>319.40 (-17.55%)</td><td>301.40 (+7.18%)</td><td>221.30 (-17.85%)</td><td>92.41 <b>(-43.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>628.60 (n/a)</td><td>387.38 (n/a)</td><td>281.20 (n/a)</td><td>269.40 (n/a)</td><td>162.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+7.84%)</td><td>0.11 (+16.38%)</td><td>0.12 (+6.48%)</td><td>0.06 (+10.74%)</td><td>0.03 (-9.91%)</td><td>559.10 (-9.69%)</td><td>324.32 (-18.19%)</td><td>262.40 (-6.08%)</td><td>223.20 (-7.27%)</td><td>136.98 <b>(-24.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>619.10 (n/a)</td><td>396.42 (n/a)</td><td>279.40 (n/a)</td><td>240.70 (n/a)</td><td>181.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (-16.03%)</td><td>0.07 (-12.37%)</td><td>0.07 <b>(-32.05%)</b></td><td>0.05 <b>(+116.57%)</b></td><td>0.02 <b>(-50.56%)</b></td><td>620.80 <b>(-53.83%)</b></td><td>475.34 (-17.07%)</td><td>490.00 <b>(+47.19%)</b></td><td>311.30 (+19.09%)</td><td>134.29 <b>(-70.94%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1344.50 (n/a)</td><td>573.16 (n/a)</td><td>332.90 (n/a)</td><td>261.40 (n/a)</td><td>462.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+16.30%)</td><td>0.02 (+10.93%)</td><td>0.02 (+12.52%)</td><td>0.01 (-7.61%)</td><td>0.00 <b>(+176.89%)</b></td><td>299.40 (+8.24%)</td><td>245.74 (-8.74%)</td><td>244.10 (-11.11%)</td><td>211.60 (-14.02%)</td><td>33.87 <b>(+160.78%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>276.60 (n/a)</td><td>269.26 (n/a)</td><td>274.60 (n/a)</td><td>246.10 (n/a)</td><td>12.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+6.53%)</td><td>0.02 (+1.99%)</td><td>0.01 (-7.71%)</td><td>0.01 (+16.89%)</td><td>0.00 (-18.82%)</td><td>307.00 (-14.44%)</td><td>270.26 (-2.92%)</td><td>273.50 (+8.36%)</td><td>226.80 (-6.13%)</td><td>30.87 <b>(-35.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>358.80 (n/a)</td><td>278.38 (n/a)</td><td>252.40 (n/a)</td><td>241.60 (n/a)</td><td>48.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+5.15%)</td><td>0.01 <b>(+25.36%)</b></td><td>0.02 <b>(+25.92%)</b></td><td>0.01 <b>(+289.78%)</b></td><td>0.01 (-17.63%)</td><td>626.90 <b>(-74.34%)</b></td><td>346.84 <b>(-54.16%)</b></td><td>244.50 <b>(-20.57%)</b></td><td>229.00 (-4.90%)</td><td>172.39 <b>(-81.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2443.40 (n/a)</td><td>756.64 (n/a)</td><td>307.80 (n/a)</td><td>240.80 (n/a)</td><td>949.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+2.81%)</td><td>0.01 <b>(+25.50%)</b></td><td>0.02 <b>(+26.53%)</b></td><td>0.01 <b>(+136.97%)</b></td><td>0.00 <b>(-40.48%)</b></td><td>445.30 <b>(-57.80%)</b></td><td>293.36 <b>(-37.04%)</b></td><td>268.70 <b>(-20.97%)</b></td><td>236.20 (-2.72%)</td><td>86.39 <b>(-74.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1055.30 (n/a)</td><td>465.92 (n/a)</td><td>340.00 (n/a)</td><td>242.80 (n/a)</td><td>339.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-4.80%)</td><td>0.01 (+6.75%)</td><td>0.01 <b>(+53.37%)</b></td><td>0.01 (+9.72%)</td><td>0.00 <b>(-33.64%)</b></td><td>467.10 (-8.86%)</td><td>342.84 (-13.10%)</td><td>310.80 <b>(-34.79%)</b></td><td>240.30 (+5.07%)</td><td>93.37 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.50 (n/a)</td><td>394.50 (n/a)</td><td>476.60 (n/a)</td><td>228.70 (n/a)</td><td>145.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-24.14%)</b></td><td>0.01 (-6.40%)</td><td>0.01 (+15.29%)</td><td>0.01 (+4.02%)</td><td>0.00 <b>(-39.13%)</b></td><td>553.90 (-3.85%)</td><td>413.46 (-1.10%)</td><td>412.40 (-13.25%)</td><td>289.50 <b>(+31.83%)</b></td><td>119.49 <b>(-25.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.10 (n/a)</td><td>418.04 (n/a)</td><td>475.40 (n/a)</td><td>219.60 (n/a)</td><td>160.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-33.16%)</b></td><td>0.01 (+8.19%)</td><td>0.01 <b>(+29.48%)</b></td><td>0.01 <b>(+276.56%)</b></td><td>0.00 <b>(-69.84%)</b></td><td>566.60 <b>(-73.44%)</b></td><td>451.40 <b>(-43.33%)</b></td><td>450.90 <b>(-22.76%)</b></td><td>342.90 <b>(+49.61%)</b></td><td>83.48 <b>(-89.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2133.60 (n/a)</td><td>796.60 (n/a)</td><td>583.80 (n/a)</td><td>229.20 (n/a)</td><td>762.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-2.58%)</td><td>0.01 <b>(+23.89%)</b></td><td>0.01 <b>(+41.04%)</b></td><td>0.01 <b>(+102.30%)</b></td><td>0.00 <b>(-23.80%)</b></td><td>563.20 <b>(-50.57%)</b></td><td>393.40 <b>(-30.23%)</b></td><td>358.00 <b>(-29.09%)</b></td><td>287.90 (+2.67%)</td><td>118.25 <b>(-64.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1139.40 (n/a)</td><td>563.88 (n/a)</td><td>504.90 (n/a)</td><td>280.40 (n/a)</td><td>335.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+8.46%)</td><td>0.01 (-0.38%)</td><td>0.01 <b>(+27.16%)</b></td><td>0.00 <b>(-77.94%)</b></td><td>0.01 <b>(+69.59%)</b></td><td>2436.40 <b>(+353.37%)</b></td><td>780.14 <b>(+76.28%)</b></td><td>389.10 <b>(-21.38%)</b></td><td>243.70 (-7.79%)</td><td>929.85 <b>(+752.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>442.56 (n/a)</td><td>494.90 (n/a)</td><td>264.30 (n/a)</td><td>109.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-12.07%)</td><td>0.01 (-0.03%)</td><td>0.01 <b>(+39.73%)</b></td><td>0.01 (-2.89%)</td><td>0.00 (-16.04%)</td><td>579.20 (+2.97%)</td><td>383.32 (-1.40%)</td><td>296.20 <b>(-28.42%)</b></td><td>264.20 (+13.73%)</td><td>139.03 (+1.47%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.50 (n/a)</td><td>388.76 (n/a)</td><td>413.80 (n/a)</td><td>232.30 (n/a)</td><td>137.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (+0.16%)</td><td>0.01 (-9.27%)</td><td>0.01 (-19.04%)</td><td>0.01 (+6.94%)</td><td>0.00 (-7.76%)</td><td>573.20 (-6.49%)</td><td>409.48 (+8.24%)</td><td>409.50 <b>(+23.49%)</b></td><td>289.40 (-0.14%)</td><td>108.20 (-18.53%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.00 (n/a)</td><td>378.32 (n/a)</td><td>331.60 (n/a)</td><td>289.80 (n/a)</td><td>132.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+7.60%)</td><td>0.03 <b>(+24.78%)</b></td><td>0.03 <b>(+25.00%)</b></td><td>0.02 <b>(+22.51%)</b></td><td>0.01 (-9.21%)</td><td>500.60 (-18.38%)</td><td>336.00 <b>(-22.18%)</b></td><td>299.50 <b>(-20.01%)</b></td><td>265.90 (-7.06%)</td><td>95.69 <b>(-31.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.30 (n/a)</td><td>431.74 (n/a)</td><td>374.40 (n/a)</td><td>286.10 (n/a)</td><td>139.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+7.54%)</td><td>0.02 (-1.40%)</td><td>0.02 (+3.38%)</td><td>0.01 <b>(-35.58%)</b></td><td>0.01 <b>(+85.80%)</b></td><td>647.20 <b>(+55.24%)</b></td><td>376.02 (+9.79%)</td><td>335.30 (-3.29%)</td><td>260.60 (-7.00%)</td><td>155.12 <b>(+188.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>416.90 (n/a)</td><td>342.48 (n/a)</td><td>346.70 (n/a)</td><td>280.20 (n/a)</td><td>53.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+3.70%)</td><td>0.02 (+9.10%)</td><td>0.03 <b>(+26.82%)</b></td><td>0.01 (+8.47%)</td><td>0.01 (+13.92%)</td><td>600.80 (-7.81%)</td><td>388.76 (-6.62%)</td><td>271.80 <b>(-21.15%)</b></td><td>259.00 (-3.57%)</td><td>168.90 (+0.79%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.70 (n/a)</td><td>416.30 (n/a)</td><td>344.70 (n/a)</td><td>268.60 (n/a)</td><td>167.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-19.00%)</td><td>0.02 (-6.72%)</td><td>0.02 (-13.18%)</td><td>0.01 (-18.07%)</td><td>0.01 (-11.25%)</td><td>577.10 <b>(+22.06%)</b></td><td>392.46 (+8.34%)</td><td>412.80 (+15.18%)</td><td>269.40 <b>(+23.46%)</b></td><td>126.57 <b>(+29.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>362.26 (n/a)</td><td>358.40 (n/a)</td><td>218.20 (n/a)</td><td>97.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+1.42%)</td><td>0.02 (-6.87%)</td><td>0.02 (-9.65%)</td><td>0.02 <b>(+29.08%)</b></td><td>0.01 <b>(-21.35%)</b></td><td>461.60 <b>(-22.52%)</b></td><td>367.22 (+2.68%)</td><td>356.60 (+10.71%)</td><td>262.20 (-1.39%)</td><td>82.18 <b>(-40.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.80 (n/a)</td><td>357.64 (n/a)</td><td>322.10 (n/a)</td><td>265.90 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-11.55%)</td><td>0.02 (-15.03%)</td><td>0.02 <b>(-40.82%)</b></td><td>0.01 <b>(+50.71%)</b></td><td>0.01 <b>(-24.57%)</b></td><td>624.40 <b>(-33.65%)</b></td><td>426.78 (+1.79%)</td><td>469.20 <b>(+68.96%)</b></td><td>269.80 (+13.08%)</td><td>148.77 <b>(-49.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>941.00 (n/a)</td><td>419.26 (n/a)</td><td>277.70 (n/a)</td><td>238.60 (n/a)</td><td>296.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+7.35%)</td><td>0.02 (+1.83%)</td><td>0.02 (+6.91%)</td><td>0.01 <b>(-23.74%)</b></td><td>0.01 <b>(+34.57%)</b></td><td>753.00 <b>(+31.12%)</b></td><td>475.60 (+4.84%)</td><td>437.40 (-6.46%)</td><td>266.60 (-6.85%)</td><td>185.81 <b>(+72.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>453.64 (n/a)</td><td>467.60 (n/a)</td><td>286.20 (n/a)</td><td>107.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-0.79%)</td><td>0.02 <b>(-20.77%)</b></td><td>0.02 <b>(-38.37%)</b></td><td>0.00 <b>(-72.59%)</b></td><td>0.01 <b>(+39.76%)</b></td><td>1851.80 <b>(+264.81%)</b></td><td>670.60 <b>(+85.96%)</b></td><td>449.30 <b>(+62.26%)</b></td><td>267.50 (+0.79%)</td><td>667.46 <b>(+445.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.60 (n/a)</td><td>360.62 (n/a)</td><td>276.90 (n/a)</td><td>265.40 (n/a)</td><td>122.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-11.82%)</td><td>0.02 (-14.61%)</td><td>0.03 (-3.84%)</td><td>0.01 <b>(-32.60%)</b></td><td>0.01 (+7.43%)</td><td>845.30 <b>(+48.35%)</b></td><td>428.58 <b>(+27.49%)</b></td><td>316.80 (+3.97%)</td><td>244.90 (+13.43%)</td><td>243.88 <b>(+78.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.80 (n/a)</td><td>336.18 (n/a)</td><td>304.70 (n/a)</td><td>215.90 (n/a)</td><td>136.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-11.61%)</td><td>0.03 (+18.03%)</td><td>0.03 <b>(+52.91%)</b></td><td>0.02 <b>(+27.07%)</b></td><td>0.01 <b>(-34.25%)</b></td><td>535.10 <b>(-21.31%)</b></td><td>333.48 <b>(-22.10%)</b></td><td>291.90 <b>(-34.61%)</b></td><td>251.30 (+13.15%)</td><td>114.67 <b>(-36.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>680.00 (n/a)</td><td>428.08 (n/a)</td><td>446.40 (n/a)</td><td>222.10 (n/a)</td><td>179.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+19.71%)</td><td>0.02 (-7.05%)</td><td>0.02 <b>(-28.07%)</b></td><td>0.00 <b>(-73.06%)</b></td><td>0.01 <b>(+85.38%)</b></td><td>2283.00 <b>(+271.28%)</b></td><td>764.50 <b>(+82.23%)</b></td><td>497.10 <b>(+39.01%)</b></td><td>236.20 (-16.48%)</td><td>857.56 <b>(+513.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.90 (n/a)</td><td>419.52 (n/a)</td><td>357.60 (n/a)</td><td>282.80 (n/a)</td><td>139.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (+11.64%)</td><td>0.02 <b>(+27.33%)</b></td><td>0.02 <b>(+24.63%)</b></td><td>0.02 <b>(+281.44%)</b></td><td>0.01 <b>(-20.30%)</b></td><td>520.20 <b>(-73.79%)</b></td><td>377.18 <b>(-46.87%)</b></td><td>366.30 (-19.76%)</td><td>252.50 (-10.43%)</td><td>122.89 <b>(-82.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1984.40 (n/a)</td><td>709.96 (n/a)</td><td>456.50 (n/a)</td><td>281.90 (n/a)</td><td>718.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (-10.12%)</td><td>0.05 (-11.99%)</td><td>0.05 (-5.96%)</td><td>0.01 <b>(-68.77%)</b></td><td>0.02 <b>(+28.52%)</b></td><td>2045.40 <b>(+220.24%)</b></td><td>649.58 <b>(+83.08%)</b></td><td>312.20 (+6.34%)</td><td>247.20 (+11.25%)</td><td>781.67 <b>(+373.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>638.70 (n/a)</td><td>354.80 (n/a)</td><td>293.60 (n/a)</td><td>222.20 (n/a)</td><td>164.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (+1.89%)</td><td>0.05 (+1.55%)</td><td>0.06 (+6.55%)</td><td>0.03 <b>(+33.29%)</b></td><td>0.02 (+2.36%)</td><td>476.70 <b>(-24.98%)</b></td><td>340.42 (-4.23%)</td><td>282.00 (-6.13%)</td><td>240.50 (-1.84%)</td><td>111.82 <b>(-29.36%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>635.40 (n/a)</td><td>355.46 (n/a)</td><td>300.40 (n/a)</td><td>245.00 (n/a)</td><td>158.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 <b>(+27.67%)</b></td><td>0.06 <b>(+21.32%)</b></td><td>0.07 <b>(+50.33%)</b></td><td>0.03 (-15.96%)</td><td>0.03 <b>(+56.66%)</b></td><td>653.40 (+18.97%)</td><td>356.22 (-7.86%)</td><td>243.50 <b>(-33.47%)</b></td><td>189.60 <b>(-21.69%)</b></td><td>195.70 <b>(+46.94%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>549.20 (n/a)</td><td>386.62 (n/a)</td><td>366.00 (n/a)</td><td>242.10 (n/a)</td><td>133.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 <b>(+49.85%)</b></td><td>0.06 (+12.64%)</td><td>0.06 (+11.69%)</td><td>0.03 (-11.27%)</td><td>0.02 <b>(+137.84%)</b></td><td>545.80 (+12.70%)</td><td>328.74 (+0.47%)</td><td>261.10 (-10.46%)</td><td>187.70 <b>(-33.27%)</b></td><td>155.36 <b>(+76.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.30 (n/a)</td><td>327.20 (n/a)</td><td>291.60 (n/a)</td><td>281.30 (n/a)</td><td>87.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(-22.68%)</b></td><td>0.04 <b>(-26.84%)</b></td><td>0.04 <b>(-40.79%)</b></td><td>0.03 (-11.16%)</td><td>0.01 <b>(-42.98%)</b></td><td>513.00 (+12.55%)</td><td>430.12 <b>(+30.06%)</b></td><td>468.00 <b>(+68.89%)</b></td><td>291.30 <b>(+29.35%)</b></td><td>86.92 <b>(-23.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>455.80 (n/a)</td><td>330.72 (n/a)</td><td>277.10 (n/a)</td><td>225.20 (n/a)</td><td>113.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 <b>(+21.25%)</b></td><td>0.06 (+15.66%)</td><td>0.06 (+15.21%)</td><td>0.03 (-12.15%)</td><td>0.01 <b>(+35.52%)</b></td><td>525.40 (+13.85%)</td><td>321.12 (-10.56%)</td><td>270.30 (-13.20%)</td><td>234.70 (-17.53%)</td><td>117.04 <b>(+33.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>461.50 (n/a)</td><td>359.04 (n/a)</td><td>311.40 (n/a)</td><td>284.60 (n/a)</td><td>87.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 <b>(-22.33%)</b></td><td>0.04 (+3.88%)</td><td>0.04 (+9.95%)</td><td>0.04 <b>(+334.37%)</b></td><td>0.01 <b>(-72.89%)</b></td><td>431.70 <b>(-76.98%)</b></td><td>399.80 <b>(-42.76%)</b></td><td>422.80 (-9.06%)</td><td>303.20 <b>(+28.75%)</b></td><td>54.27 <b>(-92.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1875.30 (n/a)</td><td>698.44 (n/a)</td><td>464.90 (n/a)</td><td>235.50 (n/a)</td><td>679.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (-13.34%)</td><td>0.04 (+4.19%)</td><td>0.04 <b>(+38.58%)</b></td><td>0.03 (+8.09%)</td><td>0.01 <b>(-35.27%)</b></td><td>568.10 (-7.48%)</td><td>399.42 (-11.65%)</td><td>366.70 <b>(-27.83%)</b></td><td>286.70 (+15.37%)</td><td>119.79 <b>(-32.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.00 (n/a)</td><td>452.10 (n/a)</td><td>508.10 (n/a)</td><td>248.50 (n/a)</td><td>178.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (+7.63%)</td><td>0.04 (+7.46%)</td><td>0.04 (+3.65%)</td><td>0.02 <b>(-27.58%)</b></td><td>0.02 <b>(+52.22%)</b></td><td>738.80 <b>(+38.07%)</b></td><td>454.48 (+4.25%)</td><td>430.00 (-3.52%)</td><td>243.10 (-7.11%)</td><td>210.06 <b>(+95.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>535.10 (n/a)</td><td>435.94 (n/a)</td><td>445.70 (n/a)</td><td>261.70 (n/a)</td><td>107.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (+0.99%)</td><td>0.04 <b>(-37.63%)</b></td><td>0.04 <b>(-47.91%)</b></td><td>0.02 <b>(-57.63%)</b></td><td>0.02 <b>(+57.06%)</b></td><td>978.30 <b>(+136.02%)</b></td><td>539.12 <b>(+88.50%)</b></td><td>467.60 <b>(+92.03%)</b></td><td>235.80 (-0.97%)</td><td>273.14 <b>(+263.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>414.50 (n/a)</td><td>286.00 (n/a)</td><td>243.50 (n/a)</td><td>238.10 (n/a)</td><td>75.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (-8.44%)</td><td>0.04 (-0.66%)</td><td>0.04 (-10.20%)</td><td>0.03 (-7.24%)</td><td>0.01 (+1.69%)</td><td>638.60 (+7.80%)</td><td>439.62 (+1.52%)</td><td>454.70 (+11.34%)</td><td>315.00 (+9.19%)</td><td>134.01 (+12.01%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>592.40 (n/a)</td><td>433.02 (n/a)</td><td>408.40 (n/a)</td><td>288.50 (n/a)</td><td>119.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 <b>(+23.45%)</b></td><td>0.05 (+1.15%)</td><td>0.05 (-5.84%)</td><td>0.02 <b>(-21.91%)</b></td><td>0.02 <b>(+64.46%)</b></td><td>706.50 <b>(+28.06%)</b></td><td>414.76 (+10.31%)</td><td>327.40 (+6.20%)</td><td>230.50 (-19.01%)</td><td>202.28 <b>(+74.78%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>551.70 (n/a)</td><td>376.00 (n/a)</td><td>308.30 (n/a)</td><td>284.60 (n/a)</td><td>115.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 <b>(+20.23%)</b></td><td>0.12 (+19.09%)</td><td>0.13 (+10.41%)</td><td>0.07 (+7.19%)</td><td>0.03 (+4.73%)</td><td>458.30 (-6.72%)</td><td>294.72 (-16.74%)</td><td>250.50 (-9.44%)</td><td>222.10 (-16.85%)</td><td>95.15 (-14.64%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.30 (n/a)</td><td>353.98 (n/a)</td><td>276.60 (n/a)</td><td>267.10 (n/a)</td><td>111.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (-1.24%)</td><td>0.11 <b>(+25.30%)</b></td><td>0.11 <b>(+53.09%)</b></td><td>0.08 <b>(+35.14%)</b></td><td>0.02 <b>(-41.16%)</b></td><td>393.80 <b>(-26.01%)</b></td><td>293.82 <b>(-26.08%)</b></td><td>289.40 <b>(-34.69%)</b></td><td>246.60 (+1.23%)</td><td>59.86 <b>(-55.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>532.20 (n/a)</td><td>397.50 (n/a)</td><td>443.10 (n/a)</td><td>243.60 (n/a)</td><td>133.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (+19.49%)</td><td>0.10 (+10.10%)</td><td>0.13 <b>(+67.99%)</b></td><td>0.01 <b>(-79.21%)</b></td><td>0.06 <b>(+132.32%)</b></td><td>2439.20 <b>(+381.10%)</b></td><td>726.12 <b>(+89.36%)</b></td><td>244.10 <b>(-40.48%)</b></td><td>230.50 (-16.30%)</td><td>963.73 <b>(+857.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>507.00 (n/a)</td><td>383.46 (n/a)</td><td>410.10 (n/a)</td><td>275.40 (n/a)</td><td>100.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (+4.79%)</td><td>0.11 (-3.74%)</td><td>0.13 (+10.71%)</td><td>0.06 <b>(-20.43%)</b></td><td>0.03 <b>(+46.85%)</b></td><td>549.00 <b>(+25.66%)</b></td><td>328.22 (+10.48%)</td><td>248.40 (-9.67%)</td><td>234.20 (-4.60%)</td><td>134.53 <b>(+68.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>436.90 (n/a)</td><td>297.08 (n/a)</td><td>275.00 (n/a)</td><td>245.50 (n/a)</td><td>79.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-4.43%)</td><td>0.11 (-4.99%)</td><td>0.12 (-3.66%)</td><td>0.08 (-10.03%)</td><td>0.02 (-1.77%)</td><td>421.50 (+11.13%)</td><td>299.70 (+5.80%)</td><td>278.90 (+3.80%)</td><td>240.70 (+4.65%)</td><td>73.45 (+17.51%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>379.30 (n/a)</td><td>283.26 (n/a)</td><td>268.70 (n/a)</td><td>230.00 (n/a)</td><td>62.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (-1.76%)</td><td>0.11 (-9.54%)</td><td>0.12 (+0.11%)</td><td>0.05 <b>(-40.56%)</b></td><td>0.03 <b>(+75.48%)</b></td><td>615.40 <b>(+68.23%)</b></td><td>343.04 <b>(+21.42%)</b></td><td>274.20 (-0.11%)</td><td>245.30 (+1.78%)</td><td>156.06 <b>(+207.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>365.80 (n/a)</td><td>282.52 (n/a)</td><td>274.50 (n/a)</td><td>241.00 (n/a)</td><td>50.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (+0.31%)</td><td>0.10 (-0.07%)</td><td>0.11 (+1.10%)</td><td>0.06 (+2.27%)</td><td>0.03 (+9.47%)</td><td>576.00 (-2.22%)</td><td>366.80 (+1.43%)</td><td>288.00 (-1.10%)</td><td>247.00 (-0.28%)</td><td>144.46 (+3.64%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>589.10 (n/a)</td><td>361.62 (n/a)</td><td>291.20 (n/a)</td><td>247.70 (n/a)</td><td>139.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+14.57%)</td><td>0.11 (+12.36%)</td><td>0.13 <b>(+26.53%)</b></td><td>0.07 (+16.95%)</td><td>0.04 <b>(+43.51%)</b></td><td>440.70 (-14.51%)</td><td>315.50 (-7.79%)</td><td>244.10 <b>(-20.95%)</b></td><td>214.20 (-12.71%)</td><td>113.48 (+9.10%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>515.50 (n/a)</td><td>342.16 (n/a)</td><td>308.80 (n/a)</td><td>245.40 (n/a)</td><td>104.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+10.20%)</td><td>0.13 <b>(+43.38%)</b></td><td>0.13 <b>(+56.11%)</b></td><td>0.10 <b>(+77.10%)</b></td><td>0.02 <b>(-34.42%)</b></td><td>325.10 <b>(-43.54%)</b></td><td>259.38 <b>(-34.59%)</b></td><td>249.00 <b>(-35.96%)</b></td><td>214.70 (-9.26%)</td><td>42.99 <b>(-65.44%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.80 (n/a)</td><td>396.52 (n/a)</td><td>388.80 (n/a)</td><td>236.60 (n/a)</td><td>124.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (-2.35%)</td><td>0.10 (-4.41%)</td><td>0.12 (-0.27%)</td><td>0.06 <b>(-20.20%)</b></td><td>0.03 <b>(+34.40%)</b></td><td>544.60 <b>(+25.34%)</b></td><td>359.28 (+11.06%)</td><td>274.50 (+0.29%)</td><td>250.10 (+2.42%)</td><td>140.24 <b>(+65.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>434.50 (n/a)</td><td>323.50 (n/a)</td><td>273.70 (n/a)</td><td>244.20 (n/a)</td><td>84.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 <b>(+36.12%)</b></td><td>0.08 (-8.83%)</td><td>0.06 <b>(-29.57%)</b></td><td>0.06 (+1.80%)</td><td>0.05 <b>(+71.37%)</b></td><td>585.70 (-1.78%)</td><td>464.42 (+19.58%)</td><td>537.10 <b>(+41.98%)</b></td><td>191.80 <b>(-26.51%)</b></td><td>160.73 <b>(+20.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>596.30 (n/a)</td><td>388.36 (n/a)</td><td>378.30 (n/a)</td><td>261.00 (n/a)</td><td>133.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (-3.53%)</td><td>0.11 (+15.87%)</td><td>0.11 (+19.42%)</td><td>0.06 <b>(+24.72%)</b></td><td>0.02 <b>(-30.31%)</b></td><td>506.40 (-19.82%)</td><td>329.32 (-19.31%)</td><td>293.30 (-16.25%)</td><td>263.40 (+3.66%)</td><td>99.79 <b>(-38.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>631.60 (n/a)</td><td>408.14 (n/a)</td><td>350.20 (n/a)</td><td>254.10 (n/a)</td><td>163.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 (-1.61%)</td><td>0.07 <b>(-28.11%)</b></td><td>0.06 <b>(-43.07%)</b></td><td>0.05 <b>(-49.38%)</b></td><td>0.03 <b>(+227.69%)</b></td><td>533.80 <b>(+97.56%)</b></td><td>390.92 <b>(+55.41%)</b></td><td>438.00 <b>(+75.69%)</b></td><td>222.90 (+1.64%)</td><td>136.55 <b>(+553.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>270.20 (n/a)</td><td>251.54 (n/a)</td><td>249.30 (n/a)</td><td>219.30 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (-19.90%)</td><td>0.17 (-4.10%)</td><td>0.18 (-12.34%)</td><td>0.15 <b>(+56.80%)</b></td><td>0.01 <b>(-79.72%)</b></td><td>317.30 <b>(-36.22%)</b></td><td>285.44 (-4.06%)</td><td>278.10 (+14.12%)</td><td>276.10 <b>(+24.82%)</b></td><td>17.83 <b>(-84.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>497.50 (n/a)</td><td>297.52 (n/a)</td><td>243.70 (n/a)</td><td>221.20 (n/a)</td><td>114.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.37 (+1.05%)</td><td>4.01 (+4.11%)</td><td>4.04 (-2.38%)</td><td>3.71 <b>(+31.79%)</b></td><td>0.27 <b>(-56.62%)</b></td><td>2827.50 <b>(-24.12%)</b></td><td>2626.54 (-5.97%)</td><td>2595.10 (+2.44%)</td><td>2397.70 (-1.04%)</td><td>172.96 <b>(-67.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.33 (n/a)</td><td>3.85 (n/a)</td><td>4.14 (n/a)</td><td>2.81 (n/a)</td><td>0.61 (n/a)</td><td>3726.50 (n/a)</td><td>2793.38 (n/a)</td><td>2533.20 (n/a)</td><td>2422.80 (n/a)</td><td>538.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (-14.06%)</td><td>0.14 (+0.36%)</td><td>0.15 (-10.67%)</td><td>0.13 <b>(+95.68%)</b></td><td>0.01 <b>(-81.75%)</b></td><td>315.80 <b>(-48.89%)</b></td><td>290.38 (-12.34%)</td><td>281.80 (+11.96%)</td><td>274.00 (+16.40%)</td><td>17.28 <b>(-89.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>617.90 (n/a)</td><td>331.24 (n/a)</td><td>251.70 (n/a)</td><td>235.40 (n/a)</td><td>162.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+5.44%)</td><td>0.02 (+0.92%)</td><td>0.02 (-9.48%)</td><td>0.01 (-2.06%)</td><td>0.00 (-8.94%)</td><td>468.00 (+2.12%)</td><td>303.72 (-1.58%)</td><td>271.30 (+10.46%)</td><td>231.80 (-5.16%)</td><td>93.69 (-1.62%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.30 (n/a)</td><td>308.60 (n/a)</td><td>245.60 (n/a)</td><td>244.40 (n/a)</td><td>95.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-3.21%)</td><td>0.01 (-4.42%)</td><td>0.01 (-15.16%)</td><td>0.01 (+18.07%)</td><td>0.00 (-14.67%)</td><td>473.70 (-15.30%)</td><td>382.44 (+2.37%)</td><td>383.80 (+17.84%)</td><td>299.10 (+3.32%)</td><td>83.04 <b>(-26.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.30 (n/a)</td><td>373.58 (n/a)</td><td>325.70 (n/a)</td><td>289.50 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-1.11%)</td><td>0.02 (-0.48%)</td><td>0.01 (-12.36%)</td><td>0.01 (+16.69%)</td><td>0.01 (+0.62%)</td><td>515.90 (-14.30%)</td><td>383.86 (-0.66%)</td><td>415.10 (+14.10%)</td><td>240.30 (+1.14%)</td><td>134.91 (-12.10%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.00 (n/a)</td><td>386.40 (n/a)</td><td>363.80 (n/a)</td><td>237.60 (n/a)</td><td>153.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(+47.01%)</b></td><td>0.01 (+19.32%)</td><td>0.01 (-10.22%)</td><td>0.01 (-12.44%)</td><td>0.01 <b>(+114.28%)</b></td><td>632.80 (+14.20%)</td><td>411.32 (-4.05%)</td><td>488.90 (+11.39%)</td><td>196.40 <b>(-31.97%)</b></td><td>184.34 <b>(+59.02%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>428.66 (n/a)</td><td>438.90 (n/a)</td><td>288.70 (n/a)</td><td>115.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+6.22%)</td><td>0.01 (-6.50%)</td><td>0.02 (-16.27%)</td><td>0.01 (-14.80%)</td><td>0.01 (+10.17%)</td><td>623.80 (+17.39%)</td><td>412.60 (+10.83%)</td><td>341.30 (+19.46%)</td><td>242.40 (-5.83%)</td><td>177.98 <b>(+23.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>372.28 (n/a)</td><td>285.70 (n/a)</td><td>257.40 (n/a)</td><td>143.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-15.65%)</td><td>0.01 <b>(+20.54%)</b></td><td>0.01 <b>(+46.11%)</b></td><td>0.01 <b>(+263.13%)</b></td><td>0.00 <b>(-44.35%)</b></td><td>524.10 <b>(-72.46%)</b></td><td>357.42 <b>(-48.94%)</b></td><td>371.50 <b>(-31.57%)</b></td><td>242.00 (+18.57%)</td><td>115.62 <b>(-83.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1903.20 (n/a)</td><td>699.98 (n/a)</td><td>542.90 (n/a)</td><td>204.10 (n/a)</td><td>691.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+17.22%)</td><td>0.01 <b>(+39.55%)</b></td><td>0.01 <b>(+36.99%)</b></td><td>0.01 <b>(+115.16%)</b></td><td>0.01 (-11.48%)</td><td>550.50 <b>(-53.52%)</b></td><td>410.74 <b>(-42.03%)</b></td><td>471.80 <b>(-27.00%)</b></td><td>233.10 (-14.68%)</td><td>141.20 <b>(-65.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1184.40 (n/a)</td><td>708.50 (n/a)</td><td>646.30 (n/a)</td><td>273.20 (n/a)</td><td>413.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (-12.44%)</td><td>0.01 (-17.08%)</td><td>0.01 <b>(-31.11%)</b></td><td>0.01 (+14.66%)</td><td>0.00 <b>(-30.80%)</b></td><td>693.50 (-12.79%)</td><td>442.68 (+9.03%)</td><td>404.20 <b>(+45.19%)</b></td><td>264.50 (+14.21%)</td><td>158.87 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.20 (n/a)</td><td>406.00 (n/a)</td><td>278.40 (n/a)</td><td>231.60 (n/a)</td><td>232.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+7.89%)</td><td>0.01 <b>(+54.07%)</b></td><td>0.02 <b>(+100.26%)</b></td><td>0.01 <b>(+51.49%)</b></td><td>0.00 (-15.24%)</td><td>537.20 <b>(-34.00%)</b></td><td>343.90 <b>(-39.21%)</b></td><td>300.20 <b>(-50.07%)</b></td><td>246.50 (-7.30%)</td><td>115.43 <b>(-41.49%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>813.90 (n/a)</td><td>565.68 (n/a)</td><td>601.20 (n/a)</td><td>265.90 (n/a)</td><td>197.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+7.47%)</td><td>0.01 (+7.31%)</td><td>0.01 (+4.98%)</td><td>0.01 (-4.91%)</td><td>0.00 <b>(+26.72%)</b></td><td>533.40 (+5.17%)</td><td>372.28 (-4.35%)</td><td>368.00 (-4.74%)</td><td>251.90 (-6.94%)</td><td>117.36 (+19.64%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.20 (n/a)</td><td>389.20 (n/a)</td><td>386.30 (n/a)</td><td>270.70 (n/a)</td><td>98.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(+38.48%)</b></td><td>0.01 <b>(+43.85%)</b></td><td>0.01 <b>(+45.44%)</b></td><td>0.01 (-8.91%)</td><td>0.01 <b>(+116.37%)</b></td><td>624.70 (+9.77%)</td><td>374.92 <b>(-23.37%)</b></td><td>357.80 <b>(-31.25%)</b></td><td>232.20 <b>(-27.80%)</b></td><td>162.89 <b>(+64.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.10 (n/a)</td><td>489.28 (n/a)</td><td>520.40 (n/a)</td><td>321.60 (n/a)</td><td>98.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-28.26%)</b></td><td>0.01 <b>(-21.56%)</b></td><td>0.01 (-13.56%)</td><td>0.01 (-3.43%)</td><td>0.00 <b>(-53.91%)</b></td><td>589.70 (+3.55%)</td><td>532.36 <b>(+22.23%)</b></td><td>560.50 (+15.69%)</td><td>402.90 <b>(+39.41%)</b></td><td>75.72 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.50 (n/a)</td><td>435.54 (n/a)</td><td>484.50 (n/a)</td><td>289.00 (n/a)</td><td>114.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (-1.97%)</td><td>0.02 <b>(-20.11%)</b></td><td>0.02 <b>(-32.30%)</b></td><td>0.00 <b>(-76.58%)</b></td><td>0.01 <b>(+68.98%)</b></td><td>1975.90 <b>(+327.04%)</b></td><td>686.14 <b>(+105.75%)</b></td><td>449.20 <b>(+47.71%)</b></td><td>227.30 (+2.02%)</td><td>730.27 <b>(+678.07%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.70 (n/a)</td><td>333.48 (n/a)</td><td>304.10 (n/a)</td><td>222.80 (n/a)</td><td>93.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (+10.28%)</td><td>0.04 (+11.21%)</td><td>0.05 <b>(+23.14%)</b></td><td>0.01 <b>(-75.13%)</b></td><td>0.02 <b>(+110.99%)</b></td><td>1904.20 <b>(+301.98%)</b></td><td>563.60 <b>(+73.24%)</b></td><td>243.70 (-18.79%)</td><td>208.90 (-9.29%)</td><td>749.60 <b>(+703.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.70 (n/a)</td><td>325.32 (n/a)</td><td>300.10 (n/a)</td><td>230.30 (n/a)</td><td>93.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 <b>(-40.67%)</b></td><td>0.02 <b>(-40.11%)</b></td><td>0.02 <b>(-45.71%)</b></td><td>0.01 (-11.46%)</td><td>0.00 <b>(-58.24%)</b></td><td>608.50 (+12.94%)</td><td>502.70 <b>(+56.92%)</b></td><td>510.20 <b>(+84.19%)</b></td><td>369.60 <b>(+68.54%)</b></td><td>90.45 <b>(-27.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.80 (n/a)</td><td>320.36 (n/a)</td><td>277.00 (n/a)</td><td>219.30 (n/a)</td><td>125.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (+14.48%)</td><td>0.04 <b>(+29.47%)</b></td><td>0.04 <b>(+27.25%)</b></td><td>0.02 <b>(+236.97%)</b></td><td>0.01 (-14.13%)</td><td>494.20 <b>(-70.32%)</b></td><td>322.30 <b>(-47.33%)</b></td><td>249.10 <b>(-21.42%)</b></td><td>193.00 (-12.67%)</td><td>135.76 <b>(-77.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1665.30 (n/a)</td><td>611.90 (n/a)</td><td>317.00 (n/a)</td><td>221.00 (n/a)</td><td>605.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-8.45%)</td><td>0.03 (+18.62%)</td><td>0.03 (+8.91%)</td><td>0.03 <b>(+68.51%)</b></td><td>0.00 <b>(-70.66%)</b></td><td>299.90 <b>(-40.65%)</b></td><td>277.40 <b>(-22.96%)</b></td><td>278.00 (-8.16%)</td><td>245.60 (+9.25%)</td><td>22.41 <b>(-81.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.30 (n/a)</td><td>360.06 (n/a)</td><td>302.70 (n/a)</td><td>224.80 (n/a)</td><td>124.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (+2.43%)</td><td>0.03 (-10.79%)</td><td>0.02 <b>(-32.54%)</b></td><td>0.02 <b>(+25.48%)</b></td><td>0.01 (-14.48%)</td><td>501.30 <b>(-20.30%)</b></td><td>420.06 (+6.04%)</td><td>458.40 <b>(+48.21%)</b></td><td>241.90 (-2.38%)</td><td>106.14 <b>(-35.97%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>629.00 (n/a)</td><td>396.12 (n/a)</td><td>309.30 (n/a)</td><td>247.80 (n/a)</td><td>165.77 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 <b>(+27.79%)</b></td><td>0.02 (+0.25%)</td><td>0.02 <b>(-22.94%)</b></td><td>0.00 <b>(-27.97%)</b></td><td>0.02 (+17.27%)</td><td>1888.80 <b>(+38.82%)</b></td><td>690.08 (+15.86%)</td><td>526.10 <b>(+29.77%)</b></td><td>181.10 <b>(-21.74%)</b></td><td>687.97 <b>(+44.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1360.60 (n/a)</td><td>595.62 (n/a)</td><td>405.40 (n/a)</td><td>231.40 (n/a)</td><td>474.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 <b>(-31.03%)</b></td><td>0.03 (-18.41%)</td><td>0.03 (-14.21%)</td><td>0.02 (+0.31%)</td><td>0.00 <b>(-50.27%)</b></td><td>430.30 (-0.30%)</td><td>359.84 (+18.55%)</td><td>341.80 (+16.58%)</td><td>302.30 <b>(+44.99%)</b></td><td>57.37 <b>(-28.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>431.60 (n/a)</td><td>303.54 (n/a)</td><td>293.20 (n/a)</td><td>208.50 (n/a)</td><td>80.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 (+13.26%)</td><td>0.02 <b>(-22.22%)</b></td><td>0.02 <b>(-44.46%)</b></td><td>0.01 <b>(-47.59%)</b></td><td>0.01 <b>(+224.96%)</b></td><td>650.60 <b>(+90.79%)</b></td><td>438.52 <b>(+53.36%)</b></td><td>502.80 <b>(+80.09%)</b></td><td>213.80 (-11.73%)</td><td>190.39 <b>(+432.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>341.00 (n/a)</td><td>285.94 (n/a)</td><td>279.20 (n/a)</td><td>242.20 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.04 <b>(+25.04%)</b></td><td>0.03 (+14.31%)</td><td>0.02 (+10.57%)</td><td>0.02 (+2.57%)</td><td>0.01 <b>(+46.14%)</b></td><td>553.20 (-2.52%)</td><td>410.28 (-8.61%)</td><td>466.40 (-9.56%)</td><td>229.90 <b>(-20.01%)</b></td><td>140.76 (+13.76%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.50 (n/a)</td><td>448.92 (n/a)</td><td>515.70 (n/a)</td><td>287.40 (n/a)</td><td>123.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.03 (-16.71%)</td><td>0.02 (-13.83%)</td><td>0.02 (-9.83%)</td><td>0.01 (-12.77%)</td><td>0.01 (-17.87%)</td><td>602.20 (+14.64%)</td><td>467.18 (+15.80%)</td><td>469.00 (+10.87%)</td><td>311.20 <b>(+20.06%)</b></td><td>116.33 (+16.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>403.44 (n/a)</td><td>423.00 (n/a)</td><td>259.20 (n/a)</td><td>99.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (-5.23%)</td><td>0.05 (-3.01%)</td><td>0.05 (+4.47%)</td><td>0.03 (+3.66%)</td><td>0.01 (-10.98%)</td><td>494.90 (-3.53%)</td><td>365.90 (+1.67%)</td><td>318.50 (-4.27%)</td><td>238.00 (+5.50%)</td><td>112.49 (-6.14%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>513.00 (n/a)</td><td>359.90 (n/a)</td><td>332.70 (n/a)</td><td>225.60 (n/a)</td><td>119.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (+8.72%)</td><td>0.06 (-8.28%)</td><td>0.05 (-11.40%)</td><td>0.01 <b>(-67.26%)</b></td><td>0.04 <b>(+69.97%)</b></td><td>1898.50 <b>(+205.42%)</b></td><td>721.28 <b>(+66.84%)</b></td><td>517.70 (+12.86%)</td><td>248.80 (-8.02%)</td><td>680.76 <b>(+379.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>621.60 (n/a)</td><td>432.32 (n/a)</td><td>458.70 (n/a)</td><td>270.50 (n/a)</td><td>141.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(-22.48%)</b></td><td>0.04 (-16.69%)</td><td>0.03 <b>(+21.58%)</b></td><td>0.03 (+7.14%)</td><td>0.01 <b>(-51.44%)</b></td><td>564.90 (-6.66%)</td><td>463.18 (+3.82%)</td><td>478.30 (-17.75%)</td><td>286.20 <b>(+28.98%)</b></td><td>112.33 <b>(-42.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.20 (n/a)</td><td>446.12 (n/a)</td><td>581.50 (n/a)</td><td>221.90 (n/a)</td><td>196.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+3.67%)</td><td>0.05 (-2.41%)</td><td>0.04 (-5.41%)</td><td>0.01 <b>(-76.42%)</b></td><td>0.03 <b>(+74.46%)</b></td><td>2457.80 <b>(+324.05%)</b></td><td>806.46 <b>(+86.19%)</b></td><td>484.40 (+5.72%)</td><td>237.80 (-3.53%)</td><td>935.40 <b>(+663.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>579.60 (n/a)</td><td>433.14 (n/a)</td><td>458.20 (n/a)</td><td>246.50 (n/a)</td><td>122.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(-24.15%)</b></td><td>0.04 (-9.72%)</td><td>0.04 <b>(-26.76%)</b></td><td>0.03 <b>(+20.90%)</b></td><td>0.01 <b>(-52.18%)</b></td><td>533.50 (-17.29%)</td><td>383.18 (-4.65%)</td><td>392.10 <b>(+36.53%)</b></td><td>294.20 <b>(+31.81%)</b></td><td>98.00 <b>(-52.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>645.00 (n/a)</td><td>401.86 (n/a)</td><td>287.20 (n/a)</td><td>223.20 (n/a)</td><td>205.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-9.87%)</td><td>0.06 (-1.55%)</td><td>0.07 (-4.24%)</td><td>0.03 (-19.96%)</td><td>0.02 (-14.84%)</td><td>608.00 <b>(+24.92%)</b></td><td>349.58 (+1.69%)</td><td>287.50 (+4.43%)</td><td>261.60 (+10.99%)</td><td>145.80 (+19.45%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>486.70 (n/a)</td><td>343.76 (n/a)</td><td>275.30 (n/a)</td><td>235.70 (n/a)</td><td>122.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 (-14.33%)</td><td>0.04 <b>(-23.88%)</b></td><td>0.04 <b>(-37.93%)</b></td><td>0.03 (-12.39%)</td><td>0.01 <b>(-22.35%)</b></td><td>513.80 (+14.13%)</td><td>402.80 <b>(+28.67%)</b></td><td>430.50 <b>(+61.12%)</b></td><td>247.20 (+16.71%)</td><td>98.26 (-4.30%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>450.20 (n/a)</td><td>313.04 (n/a)</td><td>267.20 (n/a)</td><td>211.80 (n/a)</td><td>102.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 <b>(-34.32%)</b></td><td>0.04 <b>(-29.79%)</b></td><td>0.03 (-7.44%)</td><td>0.03 (+1.09%)</td><td>0.01 <b>(-60.40%)</b></td><td>628.70 (-1.07%)</td><td>529.52 <b>(+24.60%)</b></td><td>540.40 (+8.04%)</td><td>341.90 <b>(+52.29%)</b></td><td>115.44 <b>(-37.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>635.50 (n/a)</td><td>424.98 (n/a)</td><td>500.20 (n/a)</td><td>224.50 (n/a)</td><td>183.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 <b>(+20.84%)</b></td><td>0.05 <b>(+25.63%)</b></td><td>0.06 <b>(+57.67%)</b></td><td>0.01 <b>(-40.45%)</b></td><td>0.03 <b>(+27.32%)</b></td><td>1771.10 <b>(+67.94%)</b></td><td>569.88 (+10.69%)</td><td>277.80 <b>(-36.58%)</b></td><td>217.60 (-17.26%)</td><td>672.41 <b>(+108.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1054.60 (n/a)</td><td>514.84 (n/a)</td><td>438.00 (n/a)</td><td>263.00 (n/a)</td><td>322.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.05 (-13.44%)</td><td>0.04 (-11.02%)</td><td>0.04 <b>(-30.08%)</b></td><td>0.03 <b>(+40.11%)</b></td><td>0.01 <b>(-35.78%)</b></td><td>585.60 <b>(-28.63%)</b></td><td>486.62 (+4.34%)</td><td>518.70 <b>(+43.01%)</b></td><td>372.80 (+15.53%)</td><td>103.28 <b>(-49.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>820.50 (n/a)</td><td>466.36 (n/a)</td><td>362.70 (n/a)</td><td>322.70 (n/a)</td><td>205.20 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 <b>(-25.38%)</b></td><td>0.04 <b>(-30.08%)</b></td><td>0.03 (-19.97%)</td><td>0.01 <b>(-77.03%)</b></td><td>0.02 (+15.51%)</td><td>1909.30 <b>(+335.32%)</b></td><td>712.16 <b>(+105.87%)</b></td><td>485.00 <b>(+24.97%)</b></td><td>293.70 <b>(+33.99%)</b></td><td>676.67 <b>(+629.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>438.60 (n/a)</td><td>345.92 (n/a)</td><td>388.10 (n/a)</td><td>219.20 (n/a)</td><td>92.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (+3.74%)</td><td>0.08 (-12.04%)</td><td>0.06 <b>(-30.10%)</b></td><td>0.05 (-14.95%)</td><td>0.03 (+19.45%)</td><td>612.40 (+17.57%)</td><td>463.18 (+17.46%)</td><td>519.60 <b>(+43.06%)</b></td><td>255.60 (-3.58%)</td><td>144.09 <b>(+27.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>520.90 (n/a)</td><td>394.34 (n/a)</td><td>363.20 (n/a)</td><td>265.10 (n/a)</td><td>112.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (+18.31%)</td><td>0.11 (+7.53%)</td><td>0.11 (-0.62%)</td><td>0.06 (-18.26%)</td><td>0.04 (+19.47%)</td><td>589.70 <b>(+22.34%)</b></td><td>325.98 (-2.88%)</td><td>291.70 (+0.62%)</td><td>195.70 (-15.46%)</td><td>153.19 <b>(+32.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.00 (n/a)</td><td>335.66 (n/a)</td><td>289.90 (n/a)</td><td>231.50 (n/a)</td><td>115.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (+5.42%)</td><td>0.12 <b>(+28.05%)</b></td><td>0.13 <b>(+55.16%)</b></td><td>0.07 (+0.95%)</td><td>0.04 (+19.37%)</td><td>617.00 (-0.93%)</td><td>386.34 (-19.00%)</td><td>325.70 <b>(-35.54%)</b></td><td>243.90 (-5.17%)</td><td>160.31 (+19.77%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>622.80 (n/a)</td><td>476.96 (n/a)</td><td>505.30 (n/a)</td><td>257.20 (n/a)</td><td>133.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (+15.84%)</td><td>0.11 <b>(+26.65%)</b></td><td>0.10 <b>(+31.97%)</b></td><td>0.07 (+11.37%)</td><td>0.03 (+17.80%)</td><td>476.80 (-10.21%)</td><td>328.94 <b>(-21.03%)</b></td><td>312.50 <b>(-24.24%)</b></td><td>238.00 (-13.67%)</td><td>98.07 (-14.42%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>531.00 (n/a)</td><td>416.54 (n/a)</td><td>412.50 (n/a)</td><td>275.70 (n/a)</td><td>114.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (-13.13%)</td><td>0.10 (-6.49%)</td><td>0.09 (-1.91%)</td><td>0.07 (-18.16%)</td><td>0.03 (-3.67%)</td><td>576.70 <b>(+22.18%)</b></td><td>434.46 (+8.64%)</td><td>473.00 (+1.94%)</td><td>282.20 (+15.09%)</td><td>131.07 <b>(+29.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>472.00 (n/a)</td><td>399.92 (n/a)</td><td>464.00 (n/a)</td><td>245.20 (n/a)</td><td>101.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 <b>(+25.98%)</b></td><td>0.09 <b>(+21.94%)</b></td><td>0.09 <b>(+24.67%)</b></td><td>0.06 (+13.59%)</td><td>0.03 <b>(+31.59%)</b></td><td>553.80 (-11.96%)</td><td>388.82 (-16.84%)</td><td>369.10 (-19.80%)</td><td>239.90 <b>(-20.64%)</b></td><td>127.84 (-8.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>629.00 (n/a)</td><td>467.56 (n/a)</td><td>460.20 (n/a)</td><td>302.30 (n/a)</td><td>139.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.24 <b>(+93.71%)</b></td><td>0.10 (+1.79%)</td><td>0.07 <b>(-27.28%)</b></td><td>0.06 (-15.80%)</td><td>0.07 <b>(+310.25%)</b></td><td>589.90 (+18.76%)</td><td>450.10 <b>(+21.20%)</b></td><td>502.80 <b>(+37.53%)</b></td><td>156.70 <b>(-48.37%)</b></td><td>172.17 <b>(+129.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>496.70 (n/a)</td><td>371.36 (n/a)</td><td>365.60 (n/a)</td><td>303.50 (n/a)</td><td>75.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (-1.75%)</td><td>0.08 <b>(-23.61%)</b></td><td>0.07 <b>(-32.50%)</b></td><td>0.04 <b>(-30.00%)</b></td><td>0.04 (+1.07%)</td><td>778.40 <b>(+42.85%)</b></td><td>491.54 <b>(+35.35%)</b></td><td>470.30 <b>(+48.17%)</b></td><td>215.90 (+1.79%)</td><td>201.99 <b>(+33.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>544.90 (n/a)</td><td>363.16 (n/a)</td><td>317.40 (n/a)</td><td>212.10 (n/a)</td><td>151.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-8.16%)</td><td>0.08 <b>(-28.77%)</b></td><td>0.07 <b>(-45.18%)</b></td><td>0.06 (-13.43%)</td><td>0.03 (-12.86%)</td><td>619.20 (+15.50%)</td><td>478.00 <b>(+38.78%)</b></td><td>499.60 <b>(+82.40%)</b></td><td>255.00 (+8.88%)</td><td>134.96 (+2.28%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>536.10 (n/a)</td><td>344.42 (n/a)</td><td>273.90 (n/a)</td><td>234.20 (n/a)</td><td>131.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (+7.54%)</td><td>0.09 (+10.63%)</td><td>0.08 <b>(+38.23%)</b></td><td>0.06 <b>(+21.38%)</b></td><td>0.03 (-17.56%)</td><td>555.40 (-17.61%)</td><td>403.30 (-16.15%)</td><td>413.30 <b>(-27.66%)</b></td><td>238.90 (-7.01%)</td><td>119.85 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.10 (n/a)</td><td>481.00 (n/a)</td><td>571.30 (n/a)</td><td>256.90 (n/a)</td><td>191.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+3.13%)</td><td>0.06 (-6.80%)</td><td>0.06 (-11.09%)</td><td>0.04 (-3.49%)</td><td>0.02 (-3.84%)</td><td>523.80 (+3.60%)</td><td>369.32 (+6.51%)</td><td>321.70 (+12.48%)</td><td>228.60 (-3.05%)</td><td>119.08 (-2.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>505.60 (n/a)</td><td>346.76 (n/a)</td><td>286.00 (n/a)</td><td>235.80 (n/a)</td><td>122.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (+10.36%)</td><td>0.06 (-1.02%)</td><td>0.08 (+16.76%)</td><td>0.03 <b>(-32.07%)</b></td><td>0.02 <b>(+109.58%)</b></td><td>614.50 <b>(+47.22%)</b></td><td>379.46 (+14.64%)</td><td>260.00 (-14.36%)</td><td>246.60 (-9.37%)</td><td>175.98 <b>(+171.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>417.40 (n/a)</td><td>331.00 (n/a)</td><td>303.60 (n/a)</td><td>272.10 (n/a)</td><td>64.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+8.59%)</td><td>0.05 (-9.11%)</td><td>0.04 <b>(-26.15%)</b></td><td>0.04 <b>(-24.69%)</b></td><td>0.02 <b>(+79.35%)</b></td><td>583.70 <b>(+32.81%)</b></td><td>420.14 <b>(+20.03%)</b></td><td>492.10 <b>(+35.42%)</b></td><td>237.90 (-7.93%)</td><td>147.89 <b>(+119.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>439.50 (n/a)</td><td>350.02 (n/a)</td><td>363.40 (n/a)</td><td>258.40 (n/a)</td><td>67.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+11.59%)</td><td>0.05 (-13.29%)</td><td>0.04 (-11.07%)</td><td>0.02 <b>(-46.22%)</b></td><td>0.03 <b>(+36.95%)</b></td><td>1091.30 <b>(+85.94%)</b></td><td>552.30 <b>(+33.64%)</b></td><td>477.80 (+12.45%)</td><td>233.50 (-10.36%)</td><td>319.93 <b>(+138.61%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.90 (n/a)</td><td>413.28 (n/a)</td><td>424.90 (n/a)</td><td>260.50 (n/a)</td><td>134.08 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 <b>(+20.42%)</b></td><td>0.06 (-11.43%)</td><td>0.04 <b>(-31.58%)</b></td><td>0.04 (+1.16%)</td><td>0.03 <b>(+34.28%)</b></td><td>575.00 (-1.15%)</td><td>427.14 <b>(+20.91%)</b></td><td>518.90 <b>(+46.13%)</b></td><td>184.40 (-16.97%)</td><td>172.89 (+19.03%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.70 (n/a)</td><td>353.26 (n/a)</td><td>355.10 (n/a)</td><td>222.10 (n/a)</td><td>145.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (-8.11%)</td><td>0.04 <b>(-34.40%)</b></td><td>0.04 <b>(-43.94%)</b></td><td>0.01 <b>(-75.02%)</b></td><td>0.03 (+18.53%)</td><td>1998.70 <b>(+300.30%)</b></td><td>754.90 <b>(+119.07%)</b></td><td>481.80 <b>(+78.38%)</b></td><td>238.30 (+8.81%)</td><td>707.24 <b>(+442.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>499.30 (n/a)</td><td>344.60 (n/a)</td><td>270.10 (n/a)</td><td>219.00 (n/a)</td><td>130.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (-3.13%)</td><td>0.07 (+3.88%)</td><td>0.08 <b>(+36.13%)</b></td><td>0.04 (+3.72%)</td><td>0.02 (-10.49%)</td><td>560.50 (-3.58%)</td><td>390.14 (-5.48%)</td><td>311.40 <b>(-26.54%)</b></td><td>245.20 (+3.20%)</td><td>144.88 (-5.75%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>581.30 (n/a)</td><td>412.74 (n/a)</td><td>423.90 (n/a)</td><td>237.60 (n/a)</td><td>153.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 <b>(-37.56%)</b></td><td>0.06 <b>(-20.86%)</b></td><td>0.06 (-2.04%)</td><td>0.05 (-9.52%)</td><td>0.01 <b>(-65.58%)</b></td><td>499.90 (+10.52%)</td><td>416.30 (+17.04%)</td><td>411.00 (+2.09%)</td><td>327.50 <b>(+60.15%)</b></td><td>65.44 <b>(-41.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>452.30 (n/a)</td><td>355.70 (n/a)</td><td>402.60 (n/a)</td><td>204.50 (n/a)</td><td>111.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+2.75%)</td><td>0.07 <b>(+38.17%)</b></td><td>0.06 <b>(+25.75%)</b></td><td>0.04 <b>(+274.49%)</b></td><td>0.02 (-17.98%)</td><td>663.60 <b>(-73.30%)</b></td><td>417.24 <b>(-52.22%)</b></td><td>420.30 <b>(-20.49%)</b></td><td>262.80 (-2.67%)</td><td>161.52 <b>(-82.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2485.10 (n/a)</td><td>873.28 (n/a)</td><td>528.60 (n/a)</td><td>270.00 (n/a)</td><td>908.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 <b>(-34.37%)</b></td><td>0.07 <b>(-25.80%)</b></td><td>0.08 (-14.29%)</td><td>0.04 (-14.51%)</td><td>0.02 <b>(-24.59%)</b></td><td>626.60 (+16.97%)</td><td>410.38 <b>(+34.52%)</b></td><td>297.30 (+16.68%)</td><td>281.60 <b>(+52.38%)</b></td><td>168.04 <b>(+23.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>535.70 (n/a)</td><td>305.06 (n/a)</td><td>254.80 (n/a)</td><td>184.80 (n/a)</td><td>135.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.10 (-5.19%)</td><td>0.07 (-6.60%)</td><td>0.05 <b>(-45.87%)</b></td><td>0.04 <b>(+257.56%)</b></td><td>0.03 <b>(-22.02%)</b></td><td>572.50 <b>(-72.03%)</b></td><td>422.78 <b>(-35.10%)</b></td><td>527.20 <b>(+84.79%)</b></td><td>235.20 (+5.47%)</td><td>170.04 <b>(-78.38%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2046.90 (n/a)</td><td>651.40 (n/a)</td><td>285.30 (n/a)</td><td>223.00 (n/a)</td><td>786.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-19.36%)</td><td>0.05 (+1.14%)</td><td>0.04 (+1.77%)</td><td>0.04 <b>(+76.92%)</b></td><td>0.02 <b>(-41.78%)</b></td><td>592.20 <b>(-43.48%)</b></td><td>513.28 (-14.87%)</td><td>575.00 (-1.76%)</td><td>302.60 <b>(+24.02%)</b></td><td>122.90 <b>(-57.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1047.70 (n/a)</td><td>602.96 (n/a)</td><td>585.30 (n/a)</td><td>244.00 (n/a)</td><td>287.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (-5.35%)</td><td>0.06 (+11.20%)</td><td>0.07 <b>(+80.56%)</b></td><td>0.03 (-7.46%)</td><td>0.02 (+3.47%)</td><td>563.30 (+8.08%)</td><td>359.56 (-7.22%)</td><td>254.60 <b>(-44.62%)</b></td><td>218.20 (+5.61%)</td><td>166.40 <b>(+20.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>521.20 (n/a)</td><td>387.52 (n/a)</td><td>459.70 (n/a)</td><td>206.60 (n/a)</td><td>137.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.07 <b>(-27.30%)</b></td><td>0.05 (-11.95%)</td><td>0.06 <b>(+34.60%)</b></td><td>0.03 (-12.47%)</td><td>0.02 <b>(-44.00%)</b></td><td>614.80 (+14.23%)</td><td>396.64 (+4.09%)</td><td>309.90 <b>(-25.70%)</b></td><td>279.70 <b>(+37.58%)</b></td><td>144.82 (-11.86%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>538.20 (n/a)</td><td>381.06 (n/a)</td><td>417.10 (n/a)</td><td>203.30 (n/a)</td><td>164.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.09 (+16.19%)</td><td>0.05 (-11.51%)</td><td>0.04 <b>(-37.71%)</b></td><td>0.03 (-7.38%)</td><td>0.02 <b>(+23.88%)</b></td><td>558.90 (+7.96%)</td><td>405.68 (+17.64%)</td><td>457.80 <b>(+60.52%)</b></td><td>209.80 (-13.95%)</td><td>147.82 (+19.10%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>517.70 (n/a)</td><td>344.86 (n/a)</td><td>285.20 (n/a)</td><td>243.80 (n/a)</td><td>124.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 <b>(+23.65%)</b></td><td>0.05 (-7.20%)</td><td>0.04 <b>(-45.69%)</b></td><td>0.02 <b>(+225.35%)</b></td><td>0.02 (-9.40%)</td><td>757.80 <b>(-69.27%)</b></td><td>472.40 <b>(-36.34%)</b></td><td>514.40 <b>(+84.11%)</b></td><td>222.60 (-19.14%)</td><td>206.59 <b>(-78.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2465.60 (n/a)</td><td>742.06 (n/a)</td><td>279.40 (n/a)</td><td>275.30 (n/a)</td><td>965.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.08 (+16.17%)</td><td>0.06 <b>(+50.17%)</b></td><td>0.06 <b>(+61.33%)</b></td><td>0.03 <b>(+181.95%)</b></td><td>0.02 (-2.50%)</td><td>679.00 <b>(-64.53%)</b></td><td>355.04 <b>(-49.95%)</b></td><td>286.50 <b>(-38.01%)</b></td><td>239.70 (-13.93%)</td><td>183.96 <b>(-72.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1914.40 (n/a)</td><td>709.36 (n/a)</td><td>462.20 (n/a)</td><td>278.50 (n/a)</td><td>678.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.11 <b>(+42.78%)</b></td><td>0.06 (+16.95%)</td><td>0.06 <b>(+38.29%)</b></td><td>0.03 (+6.53%)</td><td>0.03 <b>(+58.80%)</b></td><td>574.10 (-6.13%)</td><td>370.32 (-5.43%)</td><td>295.80 <b>(-27.69%)</b></td><td>167.00 <b>(-29.95%)</b></td><td>188.21 <b>(+22.96%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.60 (n/a)</td><td>391.60 (n/a)</td><td>409.10 (n/a)</td><td>238.40 (n/a)</td><td>153.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.46 (+9.52%)</td><td>0.31 <b>(+22.34%)</b></td><td>0.31 (+0.59%)</td><td>0.16 <b>(+223.03%)</b></td><td>0.11 <b>(-24.54%)</b></td><td>610.90 <b>(-69.04%)</b></td><td>354.68 <b>(-47.88%)</b></td><td>320.20 (-0.59%)</td><td>214.50 (-8.68%)</td><td>153.22 <b>(-79.15%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>1973.40 (n/a)</td><td>680.46 (n/a)</td><td>322.10 (n/a)</td><td>234.90 (n/a)</td><td>734.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.42 (+9.35%)</td><td>0.28 (+2.05%)</td><td>0.28 (+3.65%)</td><td>0.19 (-1.29%)</td><td>0.09 (+15.00%)</td><td>515.20 (+1.30%)</td><td>382.44 (-0.40%)</td><td>354.80 (-3.53%)</td><td>234.80 (-8.57%)</td><td>122.98 (+8.67%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>508.60 (n/a)</td><td>383.96 (n/a)</td><td>367.80 (n/a)</td><td>256.80 (n/a)</td><td>113.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.40 (-0.62%)</td><td>0.30 (+15.33%)</td><td>0.30 <b>(+55.22%)</b></td><td>0.20 <b>(+38.38%)</b></td><td>0.07 <b>(-44.32%)</b></td><td>498.30 <b>(-27.73%)</b></td><td>347.72 <b>(-25.66%)</b></td><td>323.10 <b>(-35.57%)</b></td><td>243.70 (+0.66%)</td><td>93.69 <b>(-56.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>689.50 (n/a)</td><td>467.74 (n/a)</td><td>501.50 (n/a)</td><td>242.10 (n/a)</td><td>216.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.33 (+1.26%)</td><td>0.25 (-4.29%)</td><td>0.23 (-9.18%)</td><td>0.16 (-19.98%)</td><td>0.07 <b>(+35.30%)</b></td><td>453.60 <b>(+24.96%)</b></td><td>312.36 (+7.94%)</td><td>316.80 (+10.11%)</td><td>221.10 (-1.21%)</td><td>89.26 <b>(+68.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>363.00 (n/a)</td><td>289.38 (n/a)</td><td>287.70 (n/a)</td><td>223.80 (n/a)</td><td>52.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.24 <b>(-22.25%)</b></td><td>0.18 (-17.40%)</td><td>0.16 (-12.45%)</td><td>0.12 (-15.47%)</td><td>0.06 <b>(-32.84%)</b></td><td>622.00 (+18.30%)</td><td>446.24 (+16.68%)</td><td>474.80 (+14.22%)</td><td>301.80 <b>(+28.64%)</b></td><td>136.94 (+0.35%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>525.80 (n/a)</td><td>382.46 (n/a)</td><td>415.70 (n/a)</td><td>234.60 (n/a)</td><td>136.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.30 (-8.33%)</td><td>0.15 <b>(-23.30%)</b></td><td>0.12 <b>(-22.32%)</b></td><td>0.03 <b>(-73.87%)</b></td><td>0.10 <b>(+20.05%)</b></td><td>2446.10 <b>(+282.74%)</b></td><td>873.64 <b>(+100.37%)</b></td><td>591.30 <b>(+28.74%)</b></td><td>245.40 (+9.07%)</td><td>890.55 <b>(+492.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>639.10 (n/a)</td><td>436.02 (n/a)</td><td>459.30 (n/a)</td><td>225.00 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 <b>(+87.03%)</b></td><td>0.13 <b>(+61.05%)</b></td><td>0.12 <b>(+58.03%)</b></td><td>0.09 <b>(+36.17%)</b></td><td>0.04 <b>(+158.58%)</b></td><td>427.60 <b>(-26.55%)</b></td><td>301.34 <b>(-35.57%)</b></td><td>301.90 <b>(-36.71%)</b></td><td>200.60 <b>(-46.54%)</b></td><td>83.63 (+2.47%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>582.20 (n/a)</td><td>467.68 (n/a)</td><td>477.00 (n/a)</td><td>375.20 (n/a)</td><td>81.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (-0.67%)</td><td>0.10 (-11.61%)</td><td>0.08 <b>(-31.88%)</b></td><td>0.06 (+5.98%)</td><td>0.03 (+4.40%)</td><td>584.60 (-5.65%)</td><td>424.44 (+13.13%)</td><td>461.40 <b>(+46.80%)</b></td><td>252.60 (+0.68%)</td><td>138.48 (-5.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>619.60 (n/a)</td><td>375.18 (n/a)</td><td>314.30 (n/a)</td><td>250.90 (n/a)</td><td>146.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 (+3.23%)</td><td>0.11 <b>(+20.06%)</b></td><td>0.13 <b>(+41.46%)</b></td><td>0.06 (-5.89%)</td><td>0.05 <b>(+32.39%)</b></td><td>604.80 (+6.25%)</td><td>391.08 (-8.82%)</td><td>294.50 <b>(-29.29%)</b></td><td>223.80 (-3.12%)</td><td>193.05 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>569.20 (n/a)</td><td>428.92 (n/a)</td><td>416.50 (n/a)</td><td>231.00 (n/a)</td><td>129.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 <b>(-33.41%)</b></td><td>0.10 (-7.32%)</td><td>0.10 (-9.60%)</td><td>0.05 <b>(+72.65%)</b></td><td>0.03 <b>(-50.02%)</b></td><td>675.80 <b>(-42.08%)</b></td><td>417.80 (-18.04%)</td><td>367.20 (+10.64%)</td><td>280.10 <b>(+50.19%)</b></td><td>160.80 <b>(-58.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1166.80 (n/a)</td><td>509.76 (n/a)</td><td>331.90 (n/a)</td><td>186.50 (n/a)</td><td>390.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 <b>(-28.34%)</b></td><td>0.08 <b>(-23.51%)</b></td><td>0.08 (-12.82%)</td><td>0.06 <b>(-23.24%)</b></td><td>0.03 <b>(-33.14%)</b></td><td>610.30 <b>(+30.27%)</b></td><td>489.82 <b>(+29.14%)</b></td><td>477.20 (+14.71%)</td><td>292.90 <b>(+39.54%)</b></td><td>128.49 <b>(+27.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>468.50 (n/a)</td><td>379.28 (n/a)</td><td>416.00 (n/a)</td><td>209.90 (n/a)</td><td>100.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+16.13%)</td><td>0.10 <b>(+32.93%)</b></td><td>0.09 <b>(+20.73%)</b></td><td>0.07 <b>(+161.91%)</b></td><td>0.03 (-14.96%)</td><td>515.90 <b>(-61.82%)</b></td><td>388.02 <b>(-38.02%)</b></td><td>390.30 (-17.17%)</td><td>244.00 (-13.90%)</td><td>108.60 <b>(-74.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1351.10 (n/a)</td><td>626.06 (n/a)</td><td>471.20 (n/a)</td><td>283.40 (n/a)</td><td>420.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 (+1.31%)</td><td>0.13 (+3.80%)</td><td>0.15 (+16.83%)</td><td>0.08 (-14.85%)</td><td>0.05 <b>(+49.40%)</b></td><td>528.90 (+17.43%)</td><td>358.42 (+3.78%)</td><td>277.60 (-14.43%)</td><td>238.60 (-1.32%)</td><td>145.45 <b>(+72.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>450.40 (n/a)</td><td>345.36 (n/a)</td><td>324.40 (n/a)</td><td>241.80 (n/a)</td><td>84.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 (-4.62%)</td><td>0.12 (-4.46%)</td><td>0.12 (-14.20%)</td><td>0.08 <b>(+30.27%)</b></td><td>0.03 <b>(-33.89%)</b></td><td>485.40 <b>(-23.24%)</b></td><td>353.04 (-2.70%)</td><td>338.20 (+16.54%)</td><td>259.30 (+4.85%)</td><td>83.54 <b>(-47.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>632.40 (n/a)</td><td>362.84 (n/a)</td><td>290.20 (n/a)</td><td>247.30 (n/a)</td><td>158.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 <b>(-30.42%)</b></td><td>0.11 (-18.73%)</td><td>0.08 (-5.99%)</td><td>0.07 (+3.37%)</td><td>0.05 <b>(-40.80%)</b></td><td>574.90 (-3.25%)</td><td>436.82 (+9.51%)</td><td>518.30 (+6.38%)</td><td>236.90 <b>(+43.75%)</b></td><td>161.60 (-15.52%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>594.20 (n/a)</td><td>398.90 (n/a)</td><td>487.20 (n/a)</td><td>164.80 (n/a)</td><td>191.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.18 (+9.50%)</td><td>0.12 <b>(+45.54%)</b></td><td>0.15 <b>(+89.46%)</b></td><td>0.02 <b>(+24.36%)</b></td><td>0.07 <b>(+20.61%)</b></td><td>2057.70 (-19.59%)</td><td>664.66 <b>(-26.76%)</b></td><td>282.40 <b>(-47.21%)</b></td><td>226.70 (-8.66%)</td><td>786.69 (-16.44%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2558.90 (n/a)</td><td>907.50 (n/a)</td><td>535.00 (n/a)</td><td>248.20 (n/a)</td><td>941.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.22 (+7.56%)</td><td>0.12 (-5.53%)</td><td>0.09 (+1.80%)</td><td>0.07 (-14.55%)</td><td>0.06 (+9.23%)</td><td>600.40 (+17.01%)</td><td>406.48 (+7.85%)</td><td>439.30 (-1.77%)</td><td>188.30 (-7.06%)</td><td>151.30 (+10.48%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>513.10 (n/a)</td><td>376.88 (n/a)</td><td>447.20 (n/a)</td><td>202.60 (n/a)</td><td>136.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 <b>(-41.36%)</b></td><td>0.09 <b>(-40.61%)</b></td><td>0.09 <b>(-44.91%)</b></td><td>0.06 (-15.31%)</td><td>0.03 <b>(-59.40%)</b></td><td>634.90 (+18.08%)</td><td>474.98 <b>(+52.00%)</b></td><td>458.60 <b>(+81.55%)</b></td><td>315.50 <b>(+70.54%)</b></td><td>121.58 (-17.86%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>537.70 (n/a)</td><td>312.48 (n/a)</td><td>252.60 (n/a)</td><td>185.00 (n/a)</td><td>148.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (-1.11%)</td><td>0.08 (-12.46%)</td><td>0.07 (-18.26%)</td><td>0.06 (-6.56%)</td><td>0.03 (-9.18%)</td><td>582.80 (+7.03%)</td><td>464.68 (+12.69%)</td><td>491.10 <b>(+22.35%)</b></td><td>280.30 (+1.12%)</td><td>112.92 (-9.55%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.50 (n/a)</td><td>412.34 (n/a)</td><td>401.40 (n/a)</td><td>277.20 (n/a)</td><td>124.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-5.48%)</td><td>0.09 (-10.72%)</td><td>0.08 <b>(-29.36%)</b></td><td>0.06 (-17.79%)</td><td>0.03 (+16.98%)</td><td>589.40 <b>(+21.65%)</b></td><td>418.64 (+16.75%)</td><td>455.60 <b>(+41.58%)</b></td><td>251.90 (+5.80%)</td><td>142.11 <b>(+44.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>484.50 (n/a)</td><td>358.58 (n/a)</td><td>321.80 (n/a)</td><td>238.10 (n/a)</td><td>98.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 (+15.60%)</td><td>0.11 <b>(+25.17%)</b></td><td>0.12 <b>(+33.18%)</b></td><td>0.06 <b>(+204.41%)</b></td><td>0.04 (-15.05%)</td><td>604.50 <b>(-67.15%)</b></td><td>373.10 <b>(-43.94%)</b></td><td>290.00 <b>(-24.91%)</b></td><td>237.30 (-13.49%)</td><td>157.57 <b>(-76.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1840.20 (n/a)</td><td>665.52 (n/a)</td><td>386.20 (n/a)</td><td>274.30 (n/a)</td><td>665.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.17 <b>(+29.08%)</b></td><td>0.10 (+14.15%)</td><td>0.07 <b>(-37.65%)</b></td><td>0.05 <b>(+97.01%)</b></td><td>0.05 (+2.66%)</td><td>662.30 <b>(-49.25%)</b></td><td>443.74 <b>(-30.47%)</b></td><td>491.40 <b>(+60.38%)</b></td><td>210.50 <b>(-22.52%)</b></td><td>204.92 <b>(-58.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1304.90 (n/a)</td><td>638.18 (n/a)</td><td>306.40 (n/a)</td><td>271.70 (n/a)</td><td>491.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.12 (-18.09%)</td><td>0.09 (-1.67%)</td><td>0.11 <b>(+34.89%)</b></td><td>0.04 <b>(-51.18%)</b></td><td>0.03 (+13.55%)</td><td>990.10 <b>(+104.82%)</b></td><td>471.58 (+16.26%)</td><td>330.90 <b>(-25.86%)</b></td><td>299.20 <b>(+22.07%)</b></td><td>294.31 <b>(+191.85%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>483.40 (n/a)</td><td>405.64 (n/a)</td><td>446.30 (n/a)</td><td>245.10 (n/a)</td><td>100.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.16 <b>(+104.66%)</b></td><td>0.09 <b>(+30.23%)</b></td><td>0.07 (+10.36%)</td><td>0.06 (-0.17%)</td><td>0.04 <b>(+376.35%)</b></td><td>632.30 (+0.17%)</td><td>451.96 (-13.61%)</td><td>473.10 (-9.39%)</td><td>214.10 <b>(-51.13%)</b></td><td>150.82 <b>(+110.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>631.20 (n/a)</td><td>523.14 (n/a)</td><td>522.10 (n/a)</td><td>438.10 (n/a)</td><td>71.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.47 (+1.17%)</td><td>0.34 (+2.97%)</td><td>0.39 <b>(+47.48%)</b></td><td>0.21 (-8.99%)</td><td>0.12 (+5.27%)</td><td>610.40 (+9.86%)</td><td>427.66 (-0.39%)</td><td>337.10 <b>(-32.19%)</b></td><td>278.50 (-1.14%)</td><td>164.02 <b>(+25.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>555.60 (n/a)</td><td>429.32 (n/a)</td><td>497.10 (n/a)</td><td>281.70 (n/a)</td><td>131.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.47 <b>(-31.50%)</b></td><td>0.35 (+6.77%)</td><td>0.42 <b>(+75.88%)</b></td><td>0.16 <b>(-27.33%)</b></td><td>0.13 <b>(-34.18%)</b></td><td>809.40 <b>(+37.61%)</b></td><td>439.60 (-8.10%)</td><td>309.30 <b>(-43.14%)</b></td><td>279.10 <b>(+45.97%)</b></td><td>224.43 <b>(+38.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.69 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>588.20 (n/a)</td><td>478.34 (n/a)</td><td>544.00 (n/a)</td><td>191.20 (n/a)</td><td>162.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 <b>(+50.71%)</b></td><td>0.34 <b>(+31.87%)</b></td><td>0.24 (-4.30%)</td><td>0.22 <b>(+27.64%)</b></td><td>0.15 <b>(+143.93%)</b></td><td>594.80 <b>(-21.65%)</b></td><td>449.50 (-16.81%)</td><td>545.00 (+4.51%)</td><td>255.40 <b>(-33.65%)</b></td><td>168.88 <b>(+24.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>759.20 (n/a)</td><td>540.30 (n/a)</td><td>521.50 (n/a)</td><td>384.90 (n/a)</td><td>136.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-11.05%)</td><td>0.01 (-10.87%)</td><td>0.01 <b>(-23.69%)</b></td><td>0.01 (+1.75%)</td><td>0.00 (-13.87%)</td><td>528.60 (-1.71%)</td><td>383.68 (+10.42%)</td><td>378.10 <b>(+31.06%)</b></td><td>276.50 (+12.40%)</td><td>105.58 (-9.73%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.80 (n/a)</td><td>347.46 (n/a)</td><td>288.50 (n/a)</td><td>246.00 (n/a)</td><td>116.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-16.66%)</td><td>0.01 (-0.72%)</td><td>0.01 (-0.07%)</td><td>0.01 <b>(+62.29%)</b></td><td>0.00 <b>(-69.10%)</b></td><td>348.80 <b>(-38.37%)</b></td><td>298.38 (-8.58%)</td><td>294.00 (+0.07%)</td><td>273.80 (+19.98%)</td><td>30.44 <b>(-77.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.00 (n/a)</td><td>326.40 (n/a)</td><td>293.80 (n/a)</td><td>228.20 (n/a)</td><td>137.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 <b>(-37.45%)</b></td><td>0.01 (-15.69%)</td><td>0.01 (-0.25%)</td><td>0.01 <b>(+112.13%)</b></td><td>0.00 <b>(-65.79%)</b></td><td>572.50 <b>(-52.86%)</b></td><td>436.50 (-14.24%)</td><td>427.30 (+0.23%)</td><td>336.10 <b>(+59.90%)</b></td><td>99.77 <b>(-75.52%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1214.50 (n/a)</td><td>508.96 (n/a)</td><td>426.30 (n/a)</td><td>210.20 (n/a)</td><td>407.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.78 (-1.16%)</td><td>6.31 (+11.75%)</td><td>7.25 (+4.04%)</td><td>2.76 <b>(+21.82%)</b></td><td>2.08 (-16.17%)</td><td>760.10 (-17.91%)</td><td>387.32 (-17.16%)</td><td>289.20 (-3.89%)</td><td>269.80 (+1.16%)</td><td>210.30 <b>(-25.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>7.87 (n/a)</td><td>5.64 (n/a)</td><td>6.97 (n/a)</td><td>2.27 (n/a)</td><td>2.48 (n/a)</td><td>925.90 (n/a)</td><td>467.58 (n/a)</td><td>300.90 (n/a)</td><td>266.70 (n/a)</td><td>282.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.57 (-10.55%)</td><td>0.38 (+0.54%)</td><td>0.34 (-3.61%)</td><td>0.23 (+0.18%)</td><td>0.13 <b>(-22.87%)</b></td><td>576.20 (-0.17%)</td><td>379.84 (-6.01%)</td><td>386.20 (+3.73%)</td><td>230.50 (+11.78%)</td><td>132.17 <b>(-20.43%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>577.20 (n/a)</td><td>404.12 (n/a)</td><td>372.30 (n/a)</td><td>206.20 (n/a)</td><td>166.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.52 (-6.36%)</td><td>0.33 <b>(-22.69%)</b></td><td>0.41 (-10.51%)</td><td>0.07 <b>(-76.66%)</b></td><td>0.18 <b>(+53.67%)</b></td><td>1998.50 <b>(+328.49%)</b></td><td>692.10 <b>(+108.80%)</b></td><td>321.70 (+11.74%)</td><td>254.40 (+6.80%)</td><td>740.48 <b>(+644.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>466.40 (n/a)</td><td>331.46 (n/a)</td><td>287.90 (n/a)</td><td>238.20 (n/a)</td><td>99.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.51 (+12.96%)</td><td>0.35 (+9.10%)</td><td>0.32 (+17.30%)</td><td>0.26 (-1.25%)</td><td>0.10 <b>(+21.52%)</b></td><td>512.30 (+1.27%)</td><td>400.72 (-7.21%)</td><td>416.00 (-14.74%)</td><td>257.90 (-11.47%)</td><td>101.42 (+5.25%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>505.90 (n/a)</td><td>431.86 (n/a)</td><td>487.90 (n/a)</td><td>291.30 (n/a)</td><td>96.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.54 (+18.64%)</td><td>0.37 (+7.62%)</td><td>0.32 (-0.42%)</td><td>0.24 (-15.69%)</td><td>0.13 <b>(+97.45%)</b></td><td>542.10 (+18.62%)</td><td>393.30 (-0.27%)</td><td>410.50 (+0.42%)</td><td>246.10 (-15.72%)</td><td>130.22 <b>(+95.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>457.00 (n/a)</td><td>394.38 (n/a)</td><td>408.80 (n/a)</td><td>292.00 (n/a)</td><td>66.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.63 <b>(+60.47%)</b></td><td>0.38 <b>(+39.90%)</b></td><td>0.33 <b>(+21.23%)</b></td><td>0.27 <b>(+269.85%)</b></td><td>0.15 (+16.35%)</td><td>493.40 <b>(-72.96%)</b></td><td>378.22 <b>(-46.04%)</b></td><td>394.50 (-17.50%)</td><td>210.40 <b>(-37.68%)</b></td><td>111.14 <b>(-82.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>0.12 (n/a)</td><td>1824.90 (n/a)</td><td>700.88 (n/a)</td><td>478.20 (n/a)</td><td>337.60 (n/a)</td><td>632.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.02 (+9.95%)</td><td>0.01 (-3.88%)</td><td>0.01 (-7.76%)</td><td>0.01 (-10.79%)</td><td>0.00 <b>(+27.67%)</b></td><td>626.60 (+12.09%)</td><td>385.92 (+9.13%)</td><td>328.20 (+8.42%)</td><td>234.10 (-9.05%)</td><td>161.02 <b>(+29.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.00 (n/a)</td><td>353.62 (n/a)</td><td>302.70 (n/a)</td><td>257.40 (n/a)</td><td>123.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.01 (-16.02%)</td><td>0.01 (-0.26%)</td><td>0.01 <b>(+46.47%)</b></td><td>0.01 (-3.02%)</td><td>0.00 <b>(-24.36%)</b></td><td>540.60 (+3.11%)</td><td>385.22 (-2.83%)</td><td>307.00 <b>(-31.73%)</b></td><td>281.20 (+19.10%)</td><td>126.30 (-6.93%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.30 (n/a)</td><td>396.42 (n/a)</td><td>449.70 (n/a)</td><td>236.10 (n/a)</td><td>135.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.00 (+14.29%)</td><td>0.00 (+10.53%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+7.76%)</td><td>23035.14 (+7.18%)</td><td>13605.68 (-1.95%)</td><td>16070.90 (-7.90%)</td><td>5182.08 (-14.60%)</td><td>7519.35 (+6.00%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21491.91 (n/a)</td><td>13876.47 (n/a)</td><td>17449.95 (n/a)</td><td>6067.86 (n/a)</td><td>7093.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.00 (-7.14%)</td><td>0.00 (+13.16%)</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+1.36%)</td><td>19948.71 (+3.22%)</td><td>12083.52 (-8.39%)</td><td>8374.43 <b>(-44.58%)</b></td><td>6475.99 (+13.63%)</td><td>6679.13 (+14.01%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19327.13 (n/a)</td><td>13189.76 (n/a)</td><td>15111.83 (n/a)</td><td>5699.18 (n/a)</td><td>5858.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-3.03%)</td><td>0.10 (+3.28%)</td><td>0.09 (+8.02%)</td><td>0.08 (+3.38%)</td><td>0.03 (-8.84%)</td><td>27406.71 (-3.28%)</td><td>21153.91 (-4.07%)</td><td>22243.66 (-7.45%)</td><td>15227.60 (+3.12%)</td><td>4937.71 (-9.41%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28335.16 (n/a)</td><td>22050.70 (n/a)</td><td>24034.92 (n/a)</td><td>14767.00 (n/a)</td><td>5450.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.99 (+17.58%)</td><td>1.73 <b>(-22.16%)</b></td><td>1.86 <b>(-21.21%)</b></td><td>0.30 <b>(-81.75%)</b></td><td>1.05 <b>(+169.89%)</b></td><td>3548.80 <b>(+447.99%)</b></td><td>1163.82 <b>(+139.96%)</b></td><td>563.80 <b>(+26.92%)</b></td><td>350.40 (-14.95%)</td><td>1350.12 <b>(+1269.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>2.55 (n/a)</td><td>2.22 (n/a)</td><td>2.36 (n/a)</td><td>1.62 (n/a)</td><td>0.39 (n/a)</td><td>647.60 (n/a)</td><td>485.00 (n/a)</td><td>444.20 (n/a)</td><td>412.00 (n/a)</td><td>98.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.30 (-3.62%)</td><td>1.49 (-8.88%)</td><td>1.15 (-18.29%)</td><td>0.31 (-4.75%)</td><td>1.16 (-0.52%)</td><td>3416.60 (+4.99%)</td><td>1298.14 (+11.09%)</td><td>915.40 <b>(+22.38%)</b></td><td>317.50 (+3.76%)</td><td>1240.20 (+3.77%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.43 (n/a)</td><td>1.64 (n/a)</td><td>1.40 (n/a)</td><td>0.32 (n/a)</td><td>1.17 (n/a)</td><td>3254.30 (n/a)</td><td>1168.52 (n/a)</td><td>748.00 (n/a)</td><td>306.00 (n/a)</td><td>1195.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.88 (+10.19%)</td><td>1.81 (-10.85%)</td><td>1.58 <b>(-32.94%)</b></td><td>0.30 <b>(-46.51%)</b></td><td>1.34 (+13.33%)</td><td>3486.70 <b>(+86.94%)</b></td><td>1165.64 <b>(+47.80%)</b></td><td>663.70 <b>(+49.15%)</b></td><td>269.90 (-9.25%)</td><td>1318.74 <b>(+103.44%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.53 (n/a)</td><td>2.03 (n/a)</td><td>2.36 (n/a)</td><td>0.56 (n/a)</td><td>1.18 (n/a)</td><td>1865.10 (n/a)</td><td>788.64 (n/a)</td><td>445.00 (n/a)</td><td>297.40 (n/a)</td><td>648.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.54 <b>(-27.64%)</b></td><td>1.91 <b>(-28.57%)</b></td><td>1.76 <b>(-27.86%)</b></td><td>1.48 (-16.35%)</td><td>0.42 <b>(-44.67%)</b></td><td>710.80 (+19.54%)</td><td>570.12 <b>(+35.71%)</b></td><td>596.40 <b>(+38.63%)</b></td><td>413.40 <b>(+38.21%)</b></td><td>116.01 (-5.32%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.51 (n/a)</td><td>2.67 (n/a)</td><td>2.44 (n/a)</td><td>1.76 (n/a)</td><td>0.76 (n/a)</td><td>594.60 (n/a)</td><td>420.10 (n/a)</td><td>430.20 (n/a)</td><td>299.10 (n/a)</td><td>122.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.21 <b>(-25.77%)</b></td><td>2.27 <b>(-21.96%)</b></td><td>2.50 (-3.48%)</td><td>0.60 <b>(-71.20%)</b></td><td>1.02 (+18.23%)</td><td>3485.40 <b>(+247.19%)</b></td><td>1337.08 <b>(+74.56%)</b></td><td>838.90 (+3.61%)</td><td>654.20 <b>(+34.72%)</b></td><td>1207.63 <b>(+523.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.32 (n/a)</td><td>2.91 (n/a)</td><td>2.59 (n/a)</td><td>2.09 (n/a)</td><td>0.86 (n/a)</td><td>1003.90 (n/a)</td><td>765.98 (n/a)</td><td>809.70 (n/a)</td><td>485.60 (n/a)</td><td>193.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.21 (-19.40%)</td><td>2.22 (-18.64%)</td><td>2.40 (-4.01%)</td><td>0.60 <b>(-63.00%)</b></td><td>0.97 (+8.89%)</td><td>3502.80 <b>(+170.28%)</b></td><td>1350.78 <b>(+60.35%)</b></td><td>873.20 (+4.18%)</td><td>652.30 <b>(+24.06%)</b></td><td>1206.69 <b>(+315.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.99 (n/a)</td><td>2.72 (n/a)</td><td>2.50 (n/a)</td><td>1.62 (n/a)</td><td>0.89 (n/a)</td><td>1296.00 (n/a)</td><td>842.42 (n/a)</td><td>838.20 (n/a)</td><td>525.80 (n/a)</td><td>290.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.19 <b>(-21.15%)</b></td><td>2.44 (-8.41%)</td><td>2.98 (+16.35%)</td><td>0.60 <b>(-28.74%)</b></td><td>1.58 (-15.22%)</td><td>3504.10 <b>(+40.32%)</b></td><td>1489.32 (+18.22%)</td><td>703.60 (-14.05%)</td><td>500.40 <b>(+26.81%)</b></td><td>1308.81 <b>(+40.34%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.31 (n/a)</td><td>2.67 (n/a)</td><td>2.56 (n/a)</td><td>0.84 (n/a)</td><td>1.86 (n/a)</td><td>2497.20 (n/a)</td><td>1259.74 (n/a)</td><td>818.60 (n/a)</td><td>394.60 (n/a)</td><td>932.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.56 (+18.22%)</td><td>3.55 (+19.68%)</td><td>3.81 <b>(+27.92%)</b></td><td>0.58 (+3.13%)</td><td>2.90 <b>(+51.42%)</b></td><td>3616.10 (-3.03%)</td><td>1680.54 <b>(+29.11%)</b></td><td>550.60 <b>(-21.82%)</b></td><td>319.60 (-15.40%)</td><td>1751.70 <b>(+26.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.55 (n/a)</td><td>2.96 (n/a)</td><td>2.98 (n/a)</td><td>0.56 (n/a)</td><td>1.92 (n/a)</td><td>3729.20 (n/a)</td><td>1301.64 (n/a)</td><td>704.30 (n/a)</td><td>377.80 (n/a)</td><td>1388.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>4.37 (+1.67%)</td><td>2.27 <b>(-24.27%)</b></td><td>2.16 <b>(-39.32%)</b></td><td>0.59 (-2.40%)</td><td>1.53 (+0.83%)</td><td>3566.00 (+2.46%)</td><td>1524.62 <b>(+28.45%)</b></td><td>970.20 <b>(+64.80%)</b></td><td>480.40 (-1.64%)</td><td>1272.04 (-1.45%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.29 (n/a)</td><td>2.99 (n/a)</td><td>3.56 (n/a)</td><td>0.60 (n/a)</td><td>1.52 (n/a)</td><td>3480.30 (n/a)</td><td>1186.98 (n/a)</td><td>588.70 (n/a)</td><td>488.40 (n/a)</td><td>1290.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>7.40 <b>(+44.42%)</b></td><td>4.61 <b>(+60.39%)</b></td><td>4.48 <b>(+79.88%)</b></td><td>3.25 <b>(+442.20%)</b></td><td>1.69 (-0.11%)</td><td>645.10 <b>(-81.56%)</b></td><td>497.96 <b>(-59.78%)</b></td><td>468.40 <b>(-44.40%)</b></td><td>283.30 <b>(-30.77%)</b></td><td>151.23 <b>(-88.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>5.13 (n/a)</td><td>2.87 (n/a)</td><td>2.49 (n/a)</td><td>0.60 (n/a)</td><td>1.69 (n/a)</td><td>3497.90 (n/a)</td><td>1238.00 (n/a)</td><td>842.50 (n/a)</td><td>409.20 (n/a)</td><td>1278.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>5.71 (+15.81%)</td><td>3.99 (-3.48%)</td><td>4.38 (+7.14%)</td><td>1.17 <b>(-59.24%)</b></td><td>1.76 <b>(+111.96%)</b></td><td>3579.80 <b>(+145.33%)</b></td><td>1451.00 <b>(+37.79%)</b></td><td>956.90 (-6.66%)</td><td>734.70 (-13.65%)</td><td>1200.42 <b>(+389.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>4.93 (n/a)</td><td>4.14 (n/a)</td><td>4.09 (n/a)</td><td>2.87 (n/a)</td><td>0.83 (n/a)</td><td>1459.20 (n/a)</td><td>1053.04 (n/a)</td><td>1025.20 (n/a)</td><td>850.80 (n/a)</td><td>245.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>10.01 <b>(+31.69%)</b></td><td>5.55 (+7.15%)</td><td>3.84 <b>(-28.35%)</b></td><td>1.61 (-3.41%)</td><td>3.53 <b>(+41.74%)</b></td><td>2597.80 (+3.53%)</td><td>1139.82 (+3.80%)</td><td>1092.50 <b>(+39.56%)</b></td><td>419.20 <b>(-24.06%)</b></td><td>875.27 (+7.11%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>7.60 (n/a)</td><td>5.18 (n/a)</td><td>5.36 (n/a)</td><td>1.67 (n/a)</td><td>2.49 (n/a)</td><td>2509.30 (n/a)</td><td>1098.12 (n/a)</td><td>782.80 (n/a)</td><td>552.00 (n/a)</td><td>817.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>8.62 (+1.29%)</td><td>5.47 (-4.52%)</td><td>6.03 (-19.15%)</td><td>1.16 (-6.46%)</td><td>2.92 (-8.17%)</td><td>3602.80 (+6.90%)</td><td>1271.80 (+3.52%)</td><td>695.60 <b>(+23.68%)</b></td><td>486.70 (-1.28%)</td><td>1317.90 (+7.07%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>8.51 (n/a)</td><td>5.73 (n/a)</td><td>7.46 (n/a)</td><td>1.24 (n/a)</td><td>3.18 (n/a)</td><td>3370.10 (n/a)</td><td>1228.58 (n/a)</td><td>562.40 (n/a)</td><td>493.00 (n/a)</td><td>1230.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.80 <b>(-30.44%)</b></td><td>4.59 <b>(-33.89%)</b></td><td>3.91 <b>(-41.71%)</b></td><td>2.02 (-11.23%)</td><td>2.01 <b>(-34.07%)</b></td><td>2079.90 (+12.65%)</td><td>1107.98 <b>(+38.50%)</b></td><td>1073.80 <b>(+71.53%)</b></td><td>617.00 <b>(+43.76%)</b></td><td>591.34 (-0.54%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>9.77 (n/a)</td><td>6.94 (n/a)</td><td>6.70 (n/a)</td><td>2.27 (n/a)</td><td>3.06 (n/a)</td><td>1846.40 (n/a)</td><td>799.96 (n/a)</td><td>626.00 (n/a)</td><td>429.20 (n/a)</td><td>594.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>8.20 (-7.07%)</td><td>3.26 <b>(-47.32%)</b></td><td>1.68 <b>(-74.62%)</b></td><td>1.10 (-14.87%)</td><td>3.02 (+4.47%)</td><td>3815.60 (+17.47%)</td><td>2264.02 <b>(+104.18%)</b></td><td>2491.00 <b>(+293.96%)</b></td><td>511.70 (+7.59%)</td><td>1464.06 <b>(+22.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>8.82 (n/a)</td><td>6.19 (n/a)</td><td>6.63 (n/a)</td><td>1.29 (n/a)</td><td>2.89 (n/a)</td><td>3248.10 (n/a)</td><td>1108.86 (n/a)</td><td>632.30 (n/a)</td><td>475.60 (n/a)</td><td>1197.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>6.79 <b>(-33.85%)</b></td><td>5.46 (-5.38%)</td><td>6.57 (-0.93%)</td><td>1.11 (-11.92%)</td><td>2.45 <b>(-27.63%)</b></td><td>3779.40 (+13.53%)</td><td>1268.98 (+4.78%)</td><td>638.60 (+0.93%)</td><td>617.50 <b>(+51.16%)</b></td><td>1403.59 (+16.21%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>10.27 (n/a)</td><td>5.77 (n/a)</td><td>6.63 (n/a)</td><td>1.26 (n/a)</td><td>3.38 (n/a)</td><td>3329.00 (n/a)</td><td>1211.04 (n/a)</td><td>632.70 (n/a)</td><td>408.50 (n/a)</td><td>1207.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.28 <b>(-20.12%)</b></td><td>1.00 (+9.52%)</td><td>0.95 (+2.90%)</td><td>0.65 <b>(+330.35%)</b></td><td>0.27 <b>(-54.15%)</b></td><td>802.50 <b>(-76.76%)</b></td><td>555.38 <b>(-50.95%)</b></td><td>551.40 (-2.82%)</td><td>409.10 <b>(+25.18%)</b></td><td>161.05 <b>(-87.78%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.60 (n/a)</td><td>0.92 (n/a)</td><td>0.92 (n/a)</td><td>0.15 (n/a)</td><td>0.58 (n/a)</td><td>3453.80 (n/a)</td><td>1132.26 (n/a)</td><td>567.40 (n/a)</td><td>326.80 (n/a)</td><td>1318.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>2.44 <b>(+30.96%)</b></td><td>1.60 <b>(+41.41%)</b></td><td>1.73 <b>(+25.60%)</b></td><td>0.31 (+5.64%)</td><td>0.82 (+18.64%)</td><td>3418.20 (-5.33%)</td><td>1136.92 <b>(-25.08%)</b></td><td>605.10 <b>(-20.39%)</b></td><td>429.60 <b>(-23.64%)</b></td><td>1280.43 (-2.18%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.86 (n/a)</td><td>1.13 (n/a)</td><td>1.38 (n/a)</td><td>0.29 (n/a)</td><td>0.69 (n/a)</td><td>3610.80 (n/a)</td><td>1517.54 (n/a)</td><td>760.10 (n/a)</td><td>562.60 (n/a)</td><td>1308.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>3.72 (+6.25%)</td><td>2.87 (-1.78%)</td><td>2.95 (-1.84%)</td><td>1.65 <b>(-30.41%)</b></td><td>0.79 <b>(+49.33%)</b></td><td>1272.30 <b>(+43.70%)</b></td><td>790.28 (+7.31%)</td><td>710.40 (+1.86%)</td><td>563.90 (-5.88%)</td><td>282.21 <b>(+105.77%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>3.50 (n/a)</td><td>2.93 (n/a)</td><td>3.01 (n/a)</td><td>2.37 (n/a)</td><td>0.53 (n/a)</td><td>885.40 (n/a)</td><td>736.48 (n/a)</td><td>697.40 (n/a)</td><td>599.10 (n/a)</td><td>137.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>1.39 <b>(-24.56%)</b></td><td>0.95 <b>(-34.68%)</b></td><td>0.89 <b>(-47.63%)</b></td><td>0.68 <b>(-28.32%)</b></td><td>0.27 <b>(-40.44%)</b></td><td>765.60 <b>(+39.50%)</b></td><td>585.34 <b>(+47.92%)</b></td><td>591.50 <b>(+90.93%)</b></td><td>378.10 <b>(+32.57%)</b></td><td>141.48 (+3.62%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>1.84 (n/a)</td><td>1.45 (n/a)</td><td>1.69 (n/a)</td><td>0.96 (n/a)</td><td>0.45 (n/a)</td><td>548.80 (n/a)</td><td>395.72 (n/a)</td><td>309.80 (n/a)</td><td>285.20 (n/a)</td><td>136.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.13 (-6.55%)</td><td>0.11 <b>(+31.68%)</b></td><td>0.12 <b>(+73.03%)</b></td><td>0.09 <b>(+460.74%)</b></td><td>0.02 <b>(-67.44%)</b></td><td>359.20 <b>(-82.17%)</b></td><td>303.46 <b>(-56.79%)</b></td><td>279.80 <b>(-42.21%)</b></td><td>256.80 (+7.00%)</td><td>48.74 <b>(-93.46%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2014.10 (n/a)</td><td>702.30 (n/a)</td><td>484.20 (n/a)</td><td>240.00 (n/a)</td><td>745.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.15 <b>(+120.09%)</b></td><td>0.11 <b>(+130.21%)</b></td><td>0.12 <b>(+116.63%)</b></td><td>0.05 <b>(+194.35%)</b></td><td>0.04 <b>(+89.01%)</b></td><td>697.80 <b>(-66.03%)</b></td><td>348.04 <b>(-60.95%)</b></td><td>280.10 <b>(-53.84%)</b></td><td>221.10 <b>(-54.57%)</b></td><td>197.91 <b>(-70.04%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>2054.00 (n/a)</td><td>891.28 (n/a)</td><td>606.80 (n/a)</td><td>486.70 (n/a)</td><td>660.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.28 (-2.29%)</td><td>0.13 <b>(-25.41%)</b></td><td>0.10 <b>(-27.66%)</b></td><td>0.03 <b>(-67.02%)</b></td><td>0.10 (+9.23%)</td><td>2059.10 <b>(+203.17%)</b></td><td>816.06 <b>(+85.23%)</b></td><td>682.50 <b>(+38.24%)</b></td><td>232.10 (+2.34%)</td><td>722.91 <b>(+271.57%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>679.20 (n/a)</td><td>440.56 (n/a)</td><td>493.70 (n/a)</td><td>226.80 (n/a)</td><td>194.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.25 (-7.24%)</td><td>0.18 (-9.43%)</td><td>0.15 (-14.39%)</td><td>0.13 (+3.54%)</td><td>0.05 <b>(-29.20%)</b></td><td>503.60 (-3.41%)</td><td>395.14 (+5.20%)</td><td>440.00 (+16.80%)</td><td>260.00 (+7.79%)</td><td>98.12 <b>(-25.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>521.40 (n/a)</td><td>375.62 (n/a)</td><td>376.70 (n/a)</td><td>241.20 (n/a)</td><td>131.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.28 <b>(+72.29%)</b></td><td>0.17 <b>(+20.05%)</b></td><td>0.13 (-10.96%)</td><td>0.11 (-6.18%)</td><td>0.08 <b>(+357.35%)</b></td><td>595.60 (+6.59%)</td><td>442.98 (-5.22%)</td><td>513.10 (+12.32%)</td><td>235.10 <b>(-41.95%)</b></td><td>165.82 <b>(+186.46%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>558.80 (n/a)</td><td>467.40 (n/a)</td><td>456.80 (n/a)</td><td>405.00 (n/a)</td><td>57.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.57 (+17.43%)</td><td>0.32 (-7.00%)</td><td>0.24 (-14.70%)</td><td>0.22 (-16.06%)</td><td>0.15 <b>(+39.26%)</b></td><td>587.40 (+19.15%)</td><td>457.60 (+13.96%)</td><td>536.30 (+17.22%)</td><td>231.40 (-14.83%)</td><td>153.25 <b>(+41.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>493.00 (n/a)</td><td>401.56 (n/a)</td><td>457.50 (n/a)</td><td>271.70 (n/a)</td><td>108.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.56 (+13.69%)</td><td>0.32 (-15.99%)</td><td>0.25 <b>(-44.89%)</b></td><td>0.24 (-3.57%)</td><td>0.14 (+16.02%)</td><td>549.00 (+3.70%)</td><td>450.02 <b>(+20.81%)</b></td><td>521.20 <b>(+81.41%)</b></td><td>233.50 (-12.05%)</td><td>132.17 (+3.01%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>529.40 (n/a)</td><td>372.50 (n/a)</td><td>287.30 (n/a)</td><td>265.50 (n/a)</td><td>128.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.69 <b>(+50.46%)</b></td><td>0.38 (+5.73%)</td><td>0.28 <b>(-30.15%)</b></td><td>0.19 (-19.52%)</td><td>0.20 <b>(+112.66%)</b></td><td>673.40 <b>(+24.24%)</b></td><td>420.38 (+8.90%)</td><td>471.80 <b>(+43.19%)</b></td><td>190.60 <b>(-33.52%)</b></td><td>192.76 <b>(+70.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>542.00 (n/a)</td><td>386.04 (n/a)</td><td>329.50 (n/a)</td><td>286.70 (n/a)</td><td>112.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.06 (+13.62%)</td><td>0.05 (+8.31%)</td><td>0.06 (+7.72%)</td><td>0.03 (-3.54%)</td><td>0.02 <b>(+32.41%)</b></td><td>486.70 (+3.69%)</td><td>344.08 (-4.93%)</td><td>274.30 (-7.17%)</td><td>252.70 (-11.98%)</td><td>115.02 (+18.66%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>469.40 (n/a)</td><td>361.92 (n/a)</td><td>295.50 (n/a)</td><td>287.10 (n/a)</td><td>96.93 (n/a)</td>
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
