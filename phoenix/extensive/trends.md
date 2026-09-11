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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+0.31%)</td><td>0.02 (-2.46%)</td><td>0.02 (-1.78%)</td><td>0.01 (-10.14%)</td><td>0.01 (+16.67%)</td><td>428.40 (+11.27%)</td><td>296.80 (+4.94%)</td><td>279.40 (+1.79%)</td><td>196.40 (-0.30%)</td><td>88.69 <b>(+30.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>385.00 (n/a)</td><td>282.84 (n/a)</td><td>274.50 (n/a)</td><td>197.00 (n/a)</td><td>67.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-12.65%)</td><td>0.02 <b>(+22.74%)</b></td><td>0.02 <b>(+46.39%)</b></td><td>0.02 <b>(+77.06%)</b></td><td>0.00 <b>(-77.07%)</b></td><td>280.90 <b>(-43.51%)</b></td><td>253.18 <b>(-26.36%)</b></td><td>246.20 <b>(-31.69%)</b></td><td>237.30 (+14.47%)</td><td>18.14 <b>(-84.81%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>497.30 (n/a)</td><td>343.82 (n/a)</td><td>360.40 (n/a)</td><td>207.30 (n/a)</td><td>119.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-19.04%)</td><td>0.02 (-9.90%)</td><td>0.02 (+12.52%)</td><td>0.01 <b>(-45.59%)</b></td><td>0.01 (-7.63%)</td><td>664.10 <b>(+83.81%)</b></td><td>339.34 <b>(+21.62%)</b></td><td>270.40 (-11.14%)</td><td>187.60 <b>(+23.50%)</b></td><td>188.90 <b>(+139.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>361.30 (n/a)</td><td>279.02 (n/a)</td><td>304.30 (n/a)</td><td>151.90 (n/a)</td><td>78.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-19.65%)</td><td>0.02 (-19.56%)</td><td>0.02 (-6.03%)</td><td>0.01 <b>(-27.87%)</b></td><td>0.01 (+7.23%)</td><td>440.30 <b>(+38.63%)</b></td><td>307.70 <b>(+29.38%)</b></td><td>248.20 (+6.43%)</td><td>225.80 <b>(+24.48%)</b></td><td>102.24 <b>(+84.80%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>317.60 (n/a)</td><td>237.82 (n/a)</td><td>233.20 (n/a)</td><td>181.40 (n/a)</td><td>55.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-10.88%)</td><td>0.02 (-18.46%)</td><td>0.02 (-8.32%)</td><td>0.00 <b>(-66.76%)</b></td><td>0.01 <b>(+34.32%)</b></td><td>1872.70 <b>(+200.88%)</b></td><td>643.18 <b>(+80.58%)</b></td><td>320.00 (+9.07%)</td><td>303.50 (+12.20%)</td><td>688.77 <b>(+358.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.40 (n/a)</td><td>356.18 (n/a)</td><td>293.40 (n/a)</td><td>270.50 (n/a)</td><td>150.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+9.71%)</td><td>0.02 (-3.27%)</td><td>0.01 (-19.22%)</td><td>0.01 (+6.17%)</td><td>0.01 <b>(+25.26%)</b></td><td>528.40 (-5.81%)</td><td>408.90 (+6.19%)</td><td>457.40 <b>(+23.79%)</b></td><td>247.10 (-8.85%)</td><td>129.75 (+11.24%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.00 (n/a)</td><td>385.08 (n/a)</td><td>369.50 (n/a)</td><td>271.10 (n/a)</td><td>116.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 <b>(-23.29%)</b></td><td>0.04 <b>(-20.97%)</b></td><td>0.04 <b>(-22.17%)</b></td><td>0.03 (+13.50%)</td><td>0.01 <b>(-40.72%)</b></td><td>457.20 (-11.91%)</td><td>352.84 (+19.02%)</td><td>317.80 <b>(+28.51%)</b></td><td>270.70 <b>(+30.39%)</b></td><td>80.65 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.00 (n/a)</td><td>296.46 (n/a)</td><td>247.30 (n/a)</td><td>207.60 (n/a)</td><td>126.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (-4.32%)</td><td>0.04 (-13.76%)</td><td>0.04 (-2.96%)</td><td>0.03 <b>(-24.16%)</b></td><td>0.01 <b>(+58.65%)</b></td><td>434.70 <b>(+31.85%)</b></td><td>325.02 <b>(+21.43%)</b></td><td>278.50 (+3.07%)</td><td>236.20 (+4.51%)</td><td>94.19 <b>(+128.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>329.70 (n/a)</td><td>267.66 (n/a)</td><td>270.20 (n/a)</td><td>226.00 (n/a)</td><td>41.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (-11.53%)</td><td>0.04 (-13.09%)</td><td>0.05 (+2.78%)</td><td>0.02 (+12.34%)</td><td>0.01 (-3.73%)</td><td>605.10 (-10.99%)</td><td>383.52 (+12.89%)</td><td>266.60 (-2.70%)</td><td>251.30 (+12.99%)</td><td>171.20 (-10.81%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>679.80 (n/a)</td><td>339.72 (n/a)</td><td>274.00 (n/a)</td><td>222.40 (n/a)</td><td>191.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-14.93%)</td><td>0.03 <b>(-20.16%)</b></td><td>0.03 <b>(-40.92%)</b></td><td>0.02 <b>(+70.96%)</b></td><td>0.01 <b>(-38.97%)</b></td><td>656.10 <b>(-41.50%)</b></td><td>470.28 (-0.29%)</td><td>472.40 <b>(+69.26%)</b></td><td>278.10 (+17.54%)</td><td>147.63 <b>(-60.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1121.60 (n/a)</td><td>471.66 (n/a)</td><td>279.10 (n/a)</td><td>236.60 (n/a)</td><td>371.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 <b>(+20.38%)</b></td><td>0.04 <b>(+28.25%)</b></td><td>0.04 <b>(+50.25%)</b></td><td>0.02 <b>(+106.75%)</b></td><td>0.01 (+1.57%)</td><td>510.90 <b>(-51.63%)</b></td><td>349.32 <b>(-30.71%)</b></td><td>274.60 <b>(-33.45%)</b></td><td>234.00 (-16.93%)</td><td>132.26 <b>(-58.58%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1056.20 (n/a)</td><td>504.16 (n/a)</td><td>412.60 (n/a)</td><td>281.70 (n/a)</td><td>319.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 <b>(-23.56%)</b></td><td>0.02 <b>(-42.73%)</b></td><td>0.02 <b>(-54.37%)</b></td><td>0.01 (-1.07%)</td><td>0.01 <b>(-27.19%)</b></td><td>1006.20 (+1.07%)</td><td>619.10 <b>(+53.23%)</b></td><td>608.20 <b>(+119.17%)</b></td><td>260.60 <b>(+30.82%)</b></td><td>264.51 <b>(-20.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>995.50 (n/a)</td><td>404.02 (n/a)</td><td>277.50 (n/a)</td><td>199.20 (n/a)</td><td>333.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (-5.95%)</td><td>0.08 (-2.62%)</td><td>0.08 (-7.89%)</td><td>0.05 (-16.84%)</td><td>0.02 (-7.28%)</td><td>513.50 <b>(+20.26%)</b></td><td>330.14 (+3.20%)</td><td>291.60 (+8.56%)</td><td>243.60 (+6.33%)</td><td>107.38 (+18.35%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>427.00 (n/a)</td><td>319.90 (n/a)</td><td>268.60 (n/a)</td><td>229.10 (n/a)</td><td>90.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (-2.91%)</td><td>0.10 (+2.06%)</td><td>0.10 (+12.46%)</td><td>0.04 (+6.05%)</td><td>0.04 (-7.46%)</td><td>570.70 (-5.70%)</td><td>300.30 (-4.41%)</td><td>250.20 (-11.09%)</td><td>156.70 (+3.02%)</td><td>157.75 (-8.28%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>605.20 (n/a)</td><td>314.16 (n/a)</td><td>281.40 (n/a)</td><td>152.10 (n/a)</td><td>171.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 <b>(+77.62%)</b></td><td>0.10 <b>(+26.76%)</b></td><td>0.08 <b>(+23.29%)</b></td><td>0.06 (+9.70%)</td><td>0.06 <b>(+101.79%)</b></td><td>440.70 (-8.83%)</td><td>304.74 (-13.10%)</td><td>311.20 (-18.87%)</td><td>124.90 <b>(-43.69%)</b></td><td>125.91 (+6.10%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>483.40 (n/a)</td><td>350.66 (n/a)</td><td>383.60 (n/a)</td><td>221.80 (n/a)</td><td>118.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 <b>(-22.91%)</b></td><td>0.07 <b>(-26.84%)</b></td><td>0.07 <b>(-30.72%)</b></td><td>0.06 <b>(-32.69%)</b></td><td>0.02 (+11.92%)</td><td>438.30 <b>(+48.58%)</b></td><td>356.34 <b>(+40.56%)</b></td><td>377.70 <b>(+44.38%)</b></td><td>254.70 <b>(+29.68%)</b></td><td>82.50 <b>(+122.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>295.00 (n/a)</td><td>253.52 (n/a)</td><td>261.60 (n/a)</td><td>196.40 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (+14.96%)</td><td>0.07 (+5.43%)</td><td>0.05 (-16.27%)</td><td>0.04 (-3.73%)</td><td>0.03 <b>(+46.31%)</b></td><td>560.90 (+3.87%)</td><td>421.24 (+1.85%)</td><td>498.10 (+19.42%)</td><td>215.40 (-13.04%)</td><td>154.97 <b>(+42.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>540.00 (n/a)</td><td>413.60 (n/a)</td><td>417.10 (n/a)</td><td>247.70 (n/a)</td><td>109.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (-5.94%)</td><td>0.06 (-17.89%)</td><td>0.05 (-16.52%)</td><td>0.04 (-18.36%)</td><td>0.04 (-1.26%)</td><td>663.00 <b>(+22.48%)</b></td><td>474.86 <b>(+24.75%)</b></td><td>496.40 (+19.79%)</td><td>173.70 (+6.30%)</td><td>182.89 (+13.93%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>541.30 (n/a)</td><td>380.64 (n/a)</td><td>414.40 (n/a)</td><td>163.40 (n/a)</td><td>160.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (+10.67%)</td><td>0.15 (+7.02%)</td><td>0.14 (+6.00%)</td><td>0.10 (+14.30%)</td><td>0.04 (-6.72%)</td><td>479.00 (-12.51%)</td><td>344.86 (-8.53%)</td><td>345.20 (-5.66%)</td><td>240.30 (-9.63%)</td><td>91.91 <b>(-22.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>547.50 (n/a)</td><td>377.00 (n/a)</td><td>365.90 (n/a)</td><td>265.90 (n/a)</td><td>119.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.21 (+2.11%)</td><td>0.17 (+18.31%)</td><td>0.20 <b>(+76.59%)</b></td><td>0.07 <b>(-32.59%)</b></td><td>0.06 <b>(+22.02%)</b></td><td>672.80 <b>(+48.32%)</b></td><td>336.18 (-8.09%)</td><td>245.80 <b>(-43.36%)</b></td><td>233.90 (-2.09%)</td><td>189.13 <b>(+81.87%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>453.60 (n/a)</td><td>365.76 (n/a)</td><td>434.00 (n/a)</td><td>238.90 (n/a)</td><td>103.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.22 <b>(+29.96%)</b></td><td>0.15 (+13.05%)</td><td>0.13 (-8.79%)</td><td>0.10 <b>(+29.04%)</b></td><td>0.05 <b>(+39.59%)</b></td><td>488.80 <b>(-22.50%)</b></td><td>363.92 (-10.15%)</td><td>368.20 (+9.62%)</td><td>219.90 <b>(-23.06%)</b></td><td>122.02 (-14.48%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>630.70 (n/a)</td><td>405.02 (n/a)</td><td>335.90 (n/a)</td><td>285.80 (n/a)</td><td>142.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 (+0.54%)</td><td>0.13 (-16.98%)</td><td>0.11 <b>(-36.62%)</b></td><td>0.08 (-1.74%)</td><td>0.06 (-5.85%)</td><td>592.90 (+1.77%)</td><td>414.62 (+18.20%)</td><td>449.20 <b>(+57.78%)</b></td><td>215.90 (-0.55%)</td><td>142.79 (-7.63%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>582.60 (n/a)</td><td>350.78 (n/a)</td><td>284.70 (n/a)</td><td>217.10 (n/a)</td><td>154.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 <b>(+39.25%)</b></td><td>0.16 <b>(+36.31%)</b></td><td>0.17 <b>(+22.50%)</b></td><td>0.10 <b>(+330.10%)</b></td><td>0.06 (-3.55%)</td><td>481.90 <b>(-76.75%)</b></td><td>332.00 <b>(-52.17%)</b></td><td>291.00 (-18.37%)</td><td>209.40 <b>(-28.19%)</b></td><td>118.83 <b>(-84.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2072.60 (n/a)</td><td>694.18 (n/a)</td><td>356.50 (n/a)</td><td>291.60 (n/a)</td><td>772.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.21 (-7.08%)</td><td>0.17 (+12.87%)</td><td>0.18 <b>(+30.84%)</b></td><td>0.11 (-7.39%)</td><td>0.04 (-2.38%)</td><td>458.90 (+7.98%)</td><td>314.86 (-10.74%)</td><td>274.90 <b>(-23.55%)</b></td><td>236.00 (+7.62%)</td><td>93.79 (+16.96%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>425.00 (n/a)</td><td>352.74 (n/a)</td><td>359.60 (n/a)</td><td>219.30 (n/a)</td><td>80.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (+8.23%)</td><td>0.01 (-18.11%)</td><td>0.01 <b>(-32.16%)</b></td><td>0.00 <b>(-25.17%)</b></td><td>0.00 <b>(+59.31%)</b></td><td>587.30 <b>(+33.66%)</b></td><td>392.44 <b>(+32.98%)</b></td><td>401.90 <b>(+47.43%)</b></td><td>216.20 (-7.57%)</td><td>152.07 <b>(+84.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.40 (n/a)</td><td>295.12 (n/a)</td><td>272.60 (n/a)</td><td>233.90 (n/a)</td><td>82.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-15.49%)</td><td>0.01 (-4.11%)</td><td>0.01 (+10.92%)</td><td>0.00 (-5.26%)</td><td>0.00 (-13.82%)</td><td>564.00 (+5.56%)</td><td>342.78 (+2.13%)</td><td>235.50 (-9.87%)</td><td>230.20 (+18.35%)</td><td>155.07 (-0.59%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>534.30 (n/a)</td><td>335.64 (n/a)</td><td>261.30 (n/a)</td><td>194.50 (n/a)</td><td>155.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 <b>(-23.60%)</b></td><td>0.01 (-6.43%)</td><td>0.01 (-15.70%)</td><td>0.01 <b>(+62.02%)</b></td><td>0.00 <b>(-61.37%)</b></td><td>386.90 <b>(-38.28%)</b></td><td>305.74 (-16.43%)</td><td>298.70 (+18.63%)</td><td>228.80 <b>(+30.89%)</b></td><td>65.64 <b>(-70.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>626.90 (n/a)</td><td>365.86 (n/a)</td><td>251.80 (n/a)</td><td>174.80 (n/a)</td><td>219.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-0.12%)</td><td>0.01 <b>(-28.92%)</b></td><td>0.00 <b>(-37.83%)</b></td><td>0.00 <b>(-35.21%)</b></td><td>0.00 <b>(+41.19%)</b></td><td>805.70 <b>(+54.32%)</b></td><td>538.50 <b>(+54.47%)</b></td><td>538.60 <b>(+60.82%)</b></td><td>242.60 (+0.12%)</td><td>200.78 <b>(+91.94%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.10 (n/a)</td><td>348.62 (n/a)</td><td>334.90 (n/a)</td><td>242.30 (n/a)</td><td>104.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-8.11%)</td><td>0.01 (+16.40%)</td><td>0.01 (+19.03%)</td><td>0.00 <b>(+24.18%)</b></td><td>0.00 (-13.84%)</td><td>532.40 (-19.48%)</td><td>395.08 (-17.99%)</td><td>449.50 (-16.00%)</td><td>249.90 (+8.79%)</td><td>128.60 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>661.20 (n/a)</td><td>481.74 (n/a)</td><td>535.10 (n/a)</td><td>229.70 (n/a)</td><td>172.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (+17.26%)</td><td>0.01 (+18.55%)</td><td>0.01 (-6.67%)</td><td>0.00 <b>(+22.16%)</b></td><td>0.00 <b>(+50.91%)</b></td><td>553.90 (-18.13%)</td><td>426.36 (-12.16%)</td><td>488.00 (+7.16%)</td><td>264.60 (-14.73%)</td><td>143.33 (+5.73%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>676.60 (n/a)</td><td>485.36 (n/a)</td><td>455.40 (n/a)</td><td>310.30 (n/a)</td><td>135.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-5.83%)</td><td>0.01 (-5.90%)</td><td>0.02 (+14.25%)</td><td>0.01 <b>(-26.22%)</b></td><td>0.00 <b>(+25.09%)</b></td><td>629.30 <b>(+35.54%)</b></td><td>389.14 (+12.40%)</td><td>293.70 (-12.46%)</td><td>272.90 (+6.19%)</td><td>153.42 <b>(+78.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.30 (n/a)</td><td>346.20 (n/a)</td><td>335.50 (n/a)</td><td>257.00 (n/a)</td><td>85.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+3.20%)</td><td>0.02 (+12.06%)</td><td>0.01 <b>(+22.77%)</b></td><td>0.01 (+17.30%)</td><td>0.00 (+1.14%)</td><td>474.20 (-14.76%)</td><td>363.40 (-11.72%)</td><td>367.20 (-18.54%)</td><td>265.50 (-3.10%)</td><td>97.35 (-17.07%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>556.30 (n/a)</td><td>411.64 (n/a)</td><td>450.80 (n/a)</td><td>274.00 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(-26.82%)</b></td><td>0.01 <b>(-22.80%)</b></td><td>0.01 <b>(-39.39%)</b></td><td>0.01 <b>(+200.60%)</b></td><td>0.00 <b>(-51.34%)</b></td><td>635.20 <b>(-66.73%)</b></td><td>484.54 <b>(-23.62%)</b></td><td>551.50 <b>(+65.02%)</b></td><td>282.40 <b>(+36.69%)</b></td><td>155.23 <b>(-78.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1909.40 (n/a)</td><td>634.34 (n/a)</td><td>334.20 (n/a)</td><td>206.60 (n/a)</td><td>721.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(-27.28%)</b></td><td>0.01 (-10.38%)</td><td>0.01 (-11.62%)</td><td>0.01 <b>(+40.83%)</b></td><td>0.00 <b>(-47.95%)</b></td><td>557.00 <b>(-29.00%)</b></td><td>457.34 (-2.15%)</td><td>503.10 (+13.13%)</td><td>292.40 <b>(+37.47%)</b></td><td>114.19 <b>(-47.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>784.50 (n/a)</td><td>467.40 (n/a)</td><td>444.70 (n/a)</td><td>212.70 (n/a)</td><td>217.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(-22.66%)</b></td><td>0.01 <b>(-31.53%)</b></td><td>0.01 <b>(-42.65%)</b></td><td>0.00 <b>(-40.18%)</b></td><td>0.01 <b>(-24.35%)</b></td><td>1088.70 <b>(+67.16%)</b></td><td>558.18 <b>(+51.65%)</b></td><td>489.60 <b>(+74.36%)</b></td><td>294.70 <b>(+29.31%)</b></td><td>316.06 <b>(+73.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.30 (n/a)</td><td>368.08 (n/a)</td><td>280.80 (n/a)</td><td>227.90 (n/a)</td><td>182.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-12.10%)</td><td>0.01 (-17.39%)</td><td>0.01 (-1.09%)</td><td>0.01 <b>(-27.71%)</b></td><td>0.00 (-7.52%)</td><td>652.40 <b>(+38.34%)</b></td><td>471.94 <b>(+22.89%)</b></td><td>423.40 (+1.10%)</td><td>312.60 (+13.76%)</td><td>130.87 <b>(+46.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.60 (n/a)</td><td>384.02 (n/a)</td><td>418.80 (n/a)</td><td>274.80 (n/a)</td><td>89.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (+6.04%)</td><td>0.04 (+8.27%)</td><td>0.04 (+18.18%)</td><td>0.02 <b>(-22.08%)</b></td><td>0.01 <b>(+58.58%)</b></td><td>545.00 <b>(+28.33%)</b></td><td>308.60 (-0.94%)</td><td>241.10 (-15.37%)</td><td>228.60 (-5.69%)</td><td>134.60 <b>(+91.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>424.70 (n/a)</td><td>311.52 (n/a)</td><td>284.90 (n/a)</td><td>242.40 (n/a)</td><td>70.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-3.16%)</td><td>0.02 <b>(-30.33%)</b></td><td>0.02 <b>(-37.73%)</b></td><td>0.01 <b>(-75.88%)</b></td><td>0.02 <b>(+107.04%)</b></td><td>1839.10 <b>(+314.59%)</b></td><td>711.60 <b>(+128.69%)</b></td><td>458.40 <b>(+60.62%)</b></td><td>252.20 (+3.28%)</td><td>658.95 <b>(+737.60%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>443.60 (n/a)</td><td>311.16 (n/a)</td><td>285.40 (n/a)</td><td>244.20 (n/a)</td><td>78.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-17.51%)</td><td>0.02 <b>(-39.48%)</b></td><td>0.02 <b>(-48.99%)</b></td><td>0.02 <b>(-33.73%)</b></td><td>0.01 (+10.06%)</td><td>601.10 <b>(+50.92%)</b></td><td>474.64 <b>(+74.37%)</b></td><td>476.40 <b>(+96.05%)</b></td><td>243.70 <b>(+21.18%)</b></td><td>143.76 <b>(+88.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>398.30 (n/a)</td><td>272.20 (n/a)</td><td>243.00 (n/a)</td><td>201.10 (n/a)</td><td>76.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-4.55%)</td><td>0.02 <b>(-29.77%)</b></td><td>0.02 <b>(-41.01%)</b></td><td>0.01 <b>(-40.17%)</b></td><td>0.01 <b>(+27.86%)</b></td><td>799.10 <b>(+67.14%)</b></td><td>485.00 <b>(+54.20%)</b></td><td>487.60 <b>(+69.54%)</b></td><td>270.80 (+4.76%)</td><td>201.37 <b>(+117.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.10 (n/a)</td><td>314.52 (n/a)</td><td>287.60 (n/a)</td><td>258.50 (n/a)</td><td>92.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(-34.47%)</b></td><td>0.03 <b>(-25.59%)</b></td><td>0.02 <b>(-41.80%)</b></td><td>0.02 (-14.99%)</td><td>0.01 <b>(-33.17%)</b></td><td>637.30 (+17.65%)</td><td>430.20 <b>(+29.20%)</b></td><td>454.80 <b>(+71.82%)</b></td><td>248.60 <b>(+52.61%)</b></td><td>170.59 (+10.05%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>541.70 (n/a)</td><td>332.96 (n/a)</td><td>264.70 (n/a)</td><td>162.90 (n/a)</td><td>155.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (+4.90%)</td><td>0.03 (-18.52%)</td><td>0.02 <b>(-33.14%)</b></td><td>0.02 <b>(-34.29%)</b></td><td>0.01 <b>(+81.97%)</b></td><td>641.60 <b>(+52.18%)</b></td><td>474.30 <b>(+36.07%)</b></td><td>529.80 <b>(+49.58%)</b></td><td>241.70 (-4.65%)</td><td>167.50 <b>(+174.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>421.60 (n/a)</td><td>348.58 (n/a)</td><td>354.20 (n/a)</td><td>253.50 (n/a)</td><td>60.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-13.41%)</td><td>0.06 (-7.51%)</td><td>0.06 (-10.20%)</td><td>0.03 <b>(-22.81%)</b></td><td>0.02 (-1.28%)</td><td>644.90 <b>(+29.55%)</b></td><td>390.74 (+11.01%)</td><td>340.70 (+11.38%)</td><td>279.90 (+15.47%)</td><td>151.24 <b>(+43.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>497.80 (n/a)</td><td>352.00 (n/a)</td><td>305.90 (n/a)</td><td>242.40 (n/a)</td><td>105.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 <b>(-25.02%)</b></td><td>0.06 (-16.54%)</td><td>0.05 (-2.46%)</td><td>0.04 (-18.66%)</td><td>0.02 <b>(-30.70%)</b></td><td>583.10 <b>(+22.94%)</b></td><td>410.66 (+14.74%)</td><td>462.80 (+2.53%)</td><td>226.10 <b>(+33.39%)</b></td><td>151.68 (+6.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>474.30 (n/a)</td><td>357.92 (n/a)</td><td>451.40 (n/a)</td><td>169.50 (n/a)</td><td>143.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (+8.11%)</td><td>0.07 <b>(+27.76%)</b></td><td>0.07 (-4.27%)</td><td>0.06 <b>(+208.61%)</b></td><td>0.01 <b>(-61.61%)</b></td><td>335.80 <b>(-67.60%)</b></td><td>288.18 <b>(-39.85%)</b></td><td>294.90 (+4.43%)</td><td>244.20 (-7.50%)</td><td>39.40 <b>(-88.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1036.30 (n/a)</td><td>479.08 (n/a)</td><td>282.40 (n/a)</td><td>264.00 (n/a)</td><td>331.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (-11.97%)</td><td>0.06 (-8.34%)</td><td>0.05 <b>(-22.47%)</b></td><td>0.03 (-1.12%)</td><td>0.02 (-17.35%)</td><td>659.80 (+1.13%)</td><td>425.84 (+5.05%)</td><td>438.70 <b>(+28.99%)</b></td><td>245.90 (+13.58%)</td><td>163.24 (-9.77%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>652.40 (n/a)</td><td>405.38 (n/a)</td><td>340.10 (n/a)</td><td>216.50 (n/a)</td><td>180.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 <b>(-38.53%)</b></td><td>0.05 <b>(-39.96%)</b></td><td>0.04 <b>(-50.62%)</b></td><td>0.04 (-9.41%)</td><td>0.01 <b>(-56.78%)</b></td><td>534.20 (+10.39%)</td><td>470.44 <b>(+55.93%)</b></td><td>506.30 <b>(+102.52%)</b></td><td>323.80 <b>(+62.71%)</b></td><td>86.25 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>483.90 (n/a)</td><td>301.70 (n/a)</td><td>250.00 (n/a)</td><td>199.00 (n/a)</td><td>115.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-2.16%)</td><td>0.06 (+3.51%)</td><td>0.05 (+11.00%)</td><td>0.04 (+2.47%)</td><td>0.01 (+4.07%)</td><td>483.80 (-2.42%)</td><td>394.24 (-3.03%)</td><td>387.60 (-9.90%)</td><td>303.90 (+2.19%)</td><td>80.90 (+7.29%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>495.80 (n/a)</td><td>406.56 (n/a)</td><td>430.20 (n/a)</td><td>297.40 (n/a)</td><td>75.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.40 (n/a)</td><td>318.10 (n/a)</td><td>284.00 (n/a)</td><td>230.20 (n/a)</td><td>114.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.00 (n/a)</td><td>434.48 (n/a)</td><td>434.10 (n/a)</td><td>257.00 (n/a)</td><td>172.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.60 (n/a)</td><td>397.36 (n/a)</td><td>445.80 (n/a)</td><td>258.50 (n/a)</td><td>127.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>467.60 (n/a)</td><td>337.92 (n/a)</td><td>296.60 (n/a)</td><td>222.70 (n/a)</td><td>121.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.60 (n/a)</td><td>397.36 (n/a)</td><td>423.00 (n/a)</td><td>202.60 (n/a)</td><td>114.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>536.80 (n/a)</td><td>484.36 (n/a)</td><td>494.80 (n/a)</td><td>382.90 (n/a)</td><td>63.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>462.40 (n/a)</td><td>332.10 (n/a)</td><td>302.40 (n/a)</td><td>257.70 (n/a)</td><td>85.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>606.20 (n/a)</td><td>403.42 (n/a)</td><td>421.60 (n/a)</td><td>195.70 (n/a)</td><td>169.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>627.90 (n/a)</td><td>527.88 (n/a)</td><td>530.30 (n/a)</td><td>421.30 (n/a)</td><td>74.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (-8.05%)</td><td>0.14 (-4.11%)</td><td>0.13 (-14.65%)</td><td>0.08 (+18.32%)</td><td>0.05 (-2.84%)</td><td>616.60 (-15.48%)</td><td>400.36 (+1.29%)</td><td>386.90 (+17.17%)</td><td>251.20 (+8.79%)</td><td>158.48 <b>(-20.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>729.50 (n/a)</td><td>395.26 (n/a)</td><td>330.20 (n/a)</td><td>230.90 (n/a)</td><td>198.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>542.80 (n/a)</td><td>407.76 (n/a)</td><td>450.50 (n/a)</td><td>239.80 (n/a)</td><td>135.70 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>557.30 (n/a)</td><td>429.50 (n/a)</td><td>452.40 (n/a)</td><td>250.40 (n/a)</td><td>112.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.40 (n/a)</td><td>410.92 (n/a)</td><td>450.40 (n/a)</td><td>244.80 (n/a)</td><td>140.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.60 (n/a)</td><td>327.28 (n/a)</td><td>275.20 (n/a)</td><td>249.90 (n/a)</td><td>98.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.20 (n/a)</td><td>408.40 (n/a)</td><td>458.30 (n/a)</td><td>288.40 (n/a)</td><td>112.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>453.20 (n/a)</td><td>300.18 (n/a)</td><td>274.70 (n/a)</td><td>209.50 (n/a)</td><td>91.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>518.40 (n/a)</td><td>410.08 (n/a)</td><td>445.30 (n/a)</td><td>189.40 (n/a)</td><td>128.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>642.60 (n/a)</td><td>491.36 (n/a)</td><td>607.20 (n/a)</td><td>278.20 (n/a)</td><td>186.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>565.10 (n/a)</td><td>433.72 (n/a)</td><td>458.20 (n/a)</td><td>266.10 (n/a)</td><td>111.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>622.10 (n/a)</td><td>397.80 (n/a)</td><td>278.60 (n/a)</td><td>216.80 (n/a)</td><td>193.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>557.60 (n/a)</td><td>465.52 (n/a)</td><td>484.80 (n/a)</td><td>302.00 (n/a)</td><td>97.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>547.00 (n/a)</td><td>403.04 (n/a)</td><td>443.40 (n/a)</td><td>241.20 (n/a)</td><td>124.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>626.60 (n/a)</td><td>419.44 (n/a)</td><td>450.50 (n/a)</td><td>239.70 (n/a)</td><td>161.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.32 (n/a)</td><td>3.30 (n/a)</td><td>3.51 (n/a)</td><td>1.83 (n/a)</td><td>0.92 (n/a)</td><td>5744.60 (n/a)</td><td>3461.72 (n/a)</td><td>2987.40 (n/a)</td><td>2424.50 (n/a)</td><td>1309.51 (n/a)</td><td>1771.49 (n/a)</td><td>1351.33 (n/a)</td><td>1437.68 (n/a)</td><td>747.65 (n/a)</td><td>375.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.37 (n/a)</td><td>3.07 (n/a)</td><td>3.01 (n/a)</td><td>2.71 (n/a)</td><td>0.27 (n/a)</td><td>8698.30 (n/a)</td><td>7720.40 (n/a)</td><td>7832.20 (n/a)</td><td>6996.10 (n/a)</td><td>680.27 (n/a)</td><td>1918.47 (n/a)</td><td>1749.11 (n/a)</td><td>1713.66 (n/a)</td><td>1543.04 (n/a)</td><td>151.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.57 (n/a)</td><td>3.44 (n/a)</td><td>3.46 (n/a)</td><td>3.26 (n/a)</td><td>0.11 (n/a)</td><td>5142.70 (n/a)</td><td>4880.16 (n/a)</td><td>4847.60 (n/a)</td><td>4703.10 (n/a)</td><td>160.41 (n/a)</td><td>1826.45 (n/a)</td><td>1761.67 (n/a)</td><td>1772.00 (n/a)</td><td>1670.32 (n/a)</td><td>56.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.12 (n/a)</td><td>0.99 (n/a)</td><td>1.01 (n/a)</td><td>0.82 (n/a)</td><td>0.11 (n/a)</td><td>556.70 (n/a)</td><td>466.18 (n/a)</td><td>453.40 (n/a)</td><td>409.10 (n/a)</td><td>55.05 (n/a)</td><td>82.03 (n/a)</td><td>72.72 (n/a)</td><td>74.01 (n/a)</td><td>60.27 (n/a)</td><td>7.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.84 (n/a)</td><td>1.37 (n/a)</td><td>1.41 (n/a)</td><td>0.91 (n/a)</td><td>0.36 (n/a)</td><td>721.10 (n/a)</td><td>508.60 (n/a)</td><td>464.50 (n/a)</td><td>356.70 (n/a)</td><td>141.96 (n/a)</td><td>188.12 (n/a)</td><td>139.91 (n/a)</td><td>144.49 (n/a)</td><td>93.07 (n/a)</td><td>36.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (n/a)</td><td>1.13 (n/a)</td><td>1.10 (n/a)</td><td>0.64 (n/a)</td><td>0.41 (n/a)</td><td>1168.50 (n/a)</td><td>747.90 (n/a)</td><td>682.60 (n/a)</td><td>447.80 (n/a)</td><td>288.93 (n/a)</td><td>187.31 (n/a)</td><td>125.90 (n/a)</td><td>122.90 (n/a)</td><td>71.79 (n/a)</td><td>46.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.59 (n/a)</td><td>1.25 (n/a)</td><td>1.19 (n/a)</td><td>0.96 (n/a)</td><td>0.24 (n/a)</td><td>1092.00 (n/a)</td><td>863.08 (n/a)</td><td>882.10 (n/a)</td><td>658.70 (n/a)</td><td>162.35 (n/a)</td><td>203.75 (n/a)</td><td>160.03 (n/a)</td><td>152.15 (n/a)</td><td>122.91 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.92 (n/a)</td><td>1.66 (n/a)</td><td>1.78 (n/a)</td><td>1.08 (n/a)</td><td>0.33 (n/a)</td><td>970.80 (n/a)</td><td>660.50 (n/a)</td><td>588.10 (n/a)</td><td>546.50 (n/a)</td><td>175.03 (n/a)</td><td>245.61 (n/a)</td><td>212.16 (n/a)</td><td>228.24 (n/a)</td><td>138.25 (n/a)</td><td>42.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.28 (n/a)</td><td>1.28 (n/a)</td><td>1.19 (n/a)</td><td>0.30 (n/a)</td><td>0.71 (n/a)</td><td>3454.60 (n/a)</td><td>1283.94 (n/a)</td><td>877.80 (n/a)</td><td>459.80 (n/a)</td><td>1227.32 (n/a)</td><td>291.93 (n/a)</td><td>164.09 (n/a)</td><td>152.91 (n/a)</td><td>38.85 (n/a)</td><td>91.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.98 (n/a)</td><td>1.66 (n/a)</td><td>1.90 (n/a)</td><td>0.92 (n/a)</td><td>0.44 (n/a)</td><td>1142.10 (n/a)</td><td>684.98 (n/a)</td><td>551.70 (n/a)</td><td>528.60 (n/a)</td><td>260.46 (n/a)</td><td>253.93 (n/a)</td><td>213.00 (n/a)</td><td>243.26 (n/a)</td><td>117.51 (n/a)</td><td>56.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (n/a)</td><td>1.37 (n/a)</td><td>1.43 (n/a)</td><td>0.95 (n/a)</td><td>0.29 (n/a)</td><td>1107.90 (n/a)</td><td>796.76 (n/a)</td><td>734.70 (n/a)</td><td>622.50 (n/a)</td><td>194.89 (n/a)</td><td>215.60 (n/a)</td><td>175.71 (n/a)</td><td>182.67 (n/a)</td><td>121.14 (n/a)</td><td>37.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.76 (n/a)</td><td>1.10 (n/a)</td><td>1.14 (n/a)</td><td>0.52 (n/a)</td><td>0.57 (n/a)</td><td>2004.30 (n/a)</td><td>1234.56 (n/a)</td><td>922.00 (n/a)</td><td>595.30 (n/a)</td><td>701.10 (n/a)</td><td>225.44 (n/a)</td><td>141.03 (n/a)</td><td>145.58 (n/a)</td><td>66.96 (n/a)</td><td>73.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>1.01 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>970.30 (n/a)</td><td>507.02 (n/a)</td><td>357.80 (n/a)</td><td>341.30 (n/a)</td><td>268.62 (n/a)</td><td>49.16 (n/a)</td><td>38.74 (n/a)</td><td>46.89 (n/a)</td><td>17.29 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.80 (n/a)</td><td>1.90 (n/a)</td><td>1.70 (n/a)</td><td>1.59 (n/a)</td><td>0.51 (n/a)</td><td>2645.50 (n/a)</td><td>2305.08 (n/a)</td><td>2463.70 (n/a)</td><td>1498.90 (n/a)</td><td>458.65 (n/a)</td><td>716.37 (n/a)</td><td>486.35 (n/a)</td><td>435.83 (n/a)</td><td>405.87 (n/a)</td><td>129.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.30 (n/a)</td><td>2.97 (n/a)</td><td>3.09 (n/a)</td><td>0.70 (n/a)</td><td>1.44 (n/a)</td><td>3767.30 (n/a)</td><td>1370.16 (n/a)</td><td>849.70 (n/a)</td><td>609.50 (n/a)</td><td>1348.83 (n/a)</td><td>880.89 (n/a)</td><td>607.82 (n/a)</td><td>631.85 (n/a)</td><td>142.51 (n/a)</td><td>295.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.58 (n/a)</td><td>3.13 (n/a)</td><td>3.48 (n/a)</td><td>2.41 (n/a)</td><td>0.55 (n/a)</td><td>3259.80 (n/a)</td><td>2577.30 (n/a)</td><td>2260.70 (n/a)</td><td>2196.70 (n/a)</td><td>488.79 (n/a)</td><td>1099.78 (n/a)</td><td>962.78 (n/a)</td><td>1068.67 (n/a)</td><td>741.13 (n/a)</td><td>167.74 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.40 (n/a)</td><td>330.48 (n/a)</td><td>310.80 (n/a)</td><td>216.10 (n/a)</td><td>132.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.30 (n/a)</td><td>400.80 (n/a)</td><td>430.20 (n/a)</td><td>221.60 (n/a)</td><td>138.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.30 (n/a)</td><td>462.36 (n/a)</td><td>521.80 (n/a)</td><td>273.10 (n/a)</td><td>144.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.30 (n/a)</td><td>500.84 (n/a)</td><td>499.60 (n/a)</td><td>335.10 (n/a)</td><td>106.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.90 (n/a)</td><td>398.74 (n/a)</td><td>447.40 (n/a)</td><td>251.20 (n/a)</td><td>122.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.90 (n/a)</td><td>488.40 (n/a)</td><td>470.40 (n/a)</td><td>363.80 (n/a)</td><td>91.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.30 (n/a)</td><td>405.08 (n/a)</td><td>465.10 (n/a)</td><td>284.10 (n/a)</td><td>103.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>696.80 (n/a)</td><td>402.36 (n/a)</td><td>343.00 (n/a)</td><td>179.00 (n/a)</td><td>215.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.90 (n/a)</td><td>382.04 (n/a)</td><td>393.30 (n/a)</td><td>229.60 (n/a)</td><td>145.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>428.92 (n/a)</td><td>468.70 (n/a)</td><td>251.90 (n/a)</td><td>138.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.70 (n/a)</td><td>375.28 (n/a)</td><td>279.50 (n/a)</td><td>236.60 (n/a)</td><td>178.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>536.50 (n/a)</td><td>423.34 (n/a)</td><td>392.40 (n/a)</td><td>341.20 (n/a)</td><td>82.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.20 (n/a)</td><td>360.60 (n/a)</td><td>382.90 (n/a)</td><td>227.80 (n/a)</td><td>129.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>506.10 (n/a)</td><td>348.80 (n/a)</td><td>298.70 (n/a)</td><td>236.30 (n/a)</td><td>117.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.40 (n/a)</td><td>418.44 (n/a)</td><td>506.70 (n/a)</td><td>246.40 (n/a)</td><td>146.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2480.90 (n/a)</td><td>1154.36 (n/a)</td><td>583.80 (n/a)</td><td>294.20 (n/a)</td><td>957.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>588.00 (n/a)</td><td>424.78 (n/a)</td><td>428.50 (n/a)</td><td>287.20 (n/a)</td><td>123.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1912.50 (n/a)</td><td>691.52 (n/a)</td><td>363.70 (n/a)</td><td>284.80 (n/a)</td><td>691.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>536.00 (n/a)</td><td>388.00 (n/a)</td><td>395.30 (n/a)</td><td>237.10 (n/a)</td><td>145.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>642.20 (n/a)</td><td>473.22 (n/a)</td><td>500.10 (n/a)</td><td>253.80 (n/a)</td><td>152.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>614.90 (n/a)</td><td>429.06 (n/a)</td><td>449.20 (n/a)</td><td>260.10 (n/a)</td><td>156.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>522.10 (n/a)</td><td>384.44 (n/a)</td><td>419.10 (n/a)</td><td>242.60 (n/a)</td><td>133.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>620.30 (n/a)</td><td>422.56 (n/a)</td><td>445.70 (n/a)</td><td>271.20 (n/a)</td><td>143.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1878.40 (n/a)</td><td>700.94 (n/a)</td><td>372.10 (n/a)</td><td>239.60 (n/a)</td><td>678.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.63 (+10.05%)</td><td>0.39 (-0.26%)</td><td>0.39 (+2.15%)</td><td>0.19 <b>(+57.17%)</b></td><td>0.16 (-14.16%)</td><td>1144.50 <b>(-36.37%)</b></td><td>650.10 (-14.76%)</td><td>562.70 (-2.11%)</td><td>353.60 (-9.15%)</td><td>299.19 <b>(-49.34%)</b></td><td>26.69 (+10.05%)</td><td>16.80 (-0.26%)</td><td>16.77 (+2.15%)</td><td>8.25 <b>(+57.17%)</b></td><td>6.72 (-14.16%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.12 (n/a)</td><td>0.18 (n/a)</td><td>1798.80 (n/a)</td><td>762.68 (n/a)</td><td>574.80 (n/a)</td><td>389.20 (n/a)</td><td>590.54 (n/a)</td><td>24.25 (n/a)</td><td>16.84 (n/a)</td><td>16.42 (n/a)</td><td>5.25 (n/a)</td><td>7.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.53 (+6.30%)</td><td>0.29 (-15.61%)</td><td>0.24 <b>(-35.83%)</b></td><td>0.12 (+4.06%)</td><td>0.17 (+18.59%)</td><td>1807.90 (-3.90%)</td><td>985.14 <b>(+20.36%)</b></td><td>904.60 <b>(+55.83%)</b></td><td>419.50 (-5.92%)</td><td>560.44 (-6.29%)</td><td>22.50 (+6.30%)</td><td>12.57 (-15.61%)</td><td>10.43 <b>(-35.83%)</b></td><td>5.22 (+4.06%)</td><td>7.11 (+18.59%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1881.20 (n/a)</td><td>818.48 (n/a)</td><td>580.50 (n/a)</td><td>445.90 (n/a)</td><td>598.03 (n/a)</td><td>21.17 (n/a)</td><td>14.89 (n/a)</td><td>16.26 (n/a)</td><td>5.02 (n/a)</td><td>6.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.31 (-1.12%)</td><td>0.30 (-1.14%)</td><td>0.30 (+0.20%)</td><td>0.29 (-4.53%)</td><td>0.01 <b>(+106.35%)</b></td><td>87917.50 (+4.75%)</td><td>83833.74 (+1.20%)</td><td>82711.00 (-0.20%)</td><td>82213.00 (+1.13%)</td><td>2366.44 <b>(+118.95%)</b></td><td>208.97 (-1.12%)</td><td>205.05 (-1.14%)</td><td>207.71 (+0.20%)</td><td>195.41 (-4.53%)</td><td>5.61 <b>(+106.35%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83931.40 (n/a)</td><td>82841.70 (n/a)</td><td>82880.10 (n/a)</td><td>81290.40 (n/a)</td><td>1080.84 (n/a)</td><td>211.34 (n/a)</td><td>207.41 (n/a)</td><td>207.29 (n/a)</td><td>204.69 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.15 (+11.94%)</td><td>1.13 (+13.10%)</td><td>1.14 (+13.99%)</td><td>1.10 (+11.65%)</td><td>0.02 <b>(+32.11%)</b></td><td>22974.80 (-10.43%)</td><td>22268.92 (-11.57%)</td><td>22105.10 (-12.27%)</td><td>21938.80 (-10.67%)</td><td>434.55 (+5.81%)</td><td>783.08 (+11.94%)</td><td>771.70 (+13.10%)</td><td>777.19 (+13.99%)</td><td>747.77 (+11.65%)</td><td>14.82 <b>(+32.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25651.00 (n/a)</td><td>25183.80 (n/a)</td><td>25196.50 (n/a)</td><td>24558.20 (n/a)</td><td>410.68 (n/a)</td><td>699.56 (n/a)</td><td>682.33 (n/a)</td><td>681.83 (n/a)</td><td>669.75 (n/a)</td><td>11.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.81 (-1.86%)</td><td>0.79 (-1.44%)</td><td>0.78 (-3.19%)</td><td>0.77 (+1.81%)</td><td>0.01 <b>(-45.29%)</b></td><td>97836.60 (-1.78%)</td><td>95970.00 (+1.40%)</td><td>96384.50 (+3.29%)</td><td>93629.80 (+1.90%)</td><td>1685.40 <b>(-45.43%)</b></td><td>733.95 (-1.86%)</td><td>716.23 (-1.44%)</td><td>712.97 (-3.19%)</td><td>702.39 (+1.81%)</td><td>12.65 <b>(-45.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.03 (n/a)</td><td>99608.90 (n/a)</td><td>94641.78 (n/a)</td><td>93314.20 (n/a)</td><td>91887.00 (n/a)</td><td>3088.25 (n/a)</td><td>747.87 (n/a)</td><td>726.70 (n/a)</td><td>736.43 (n/a)</td><td>689.89 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.78 (+1.40%)</td><td>0.77 (+0.95%)</td><td>0.77 (+0.80%)</td><td>0.76 (+0.84%)</td><td>0.01 <b>(+22.82%)</b></td><td>99129.70 (-0.84%)</td><td>97995.30 (-0.94%)</td><td>97954.80 (-0.80%)</td><td>97109.90 (-1.38%)</td><td>726.64 <b>(+20.14%)</b></td><td>707.65 (+1.40%)</td><td>701.28 (+0.95%)</td><td>701.54 (+0.80%)</td><td>693.23 (+0.84%)</td><td>5.18 <b>(+22.82%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99967.30 (n/a)</td><td>98927.18 (n/a)</td><td>98742.00 (n/a)</td><td>98469.60 (n/a)</td><td>604.80 (n/a)</td><td>697.88 (n/a)</td><td>694.67 (n/a)</td><td>695.95 (n/a)</td><td>687.42 (n/a)</td><td>4.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.90 (+12.15%)</td><td>0.89 (+12.62%)</td><td>0.90 (+12.95%)</td><td>0.89 (+12.96%)</td><td>0.00 <b>(-38.38%)</b></td><td>84764.10 (-11.47%)</td><td>84382.10 (-11.21%)</td><td>84287.00 (-11.47%)</td><td>84064.00 (-10.83%)</td><td>292.83 <b>(-51.33%)</b></td><td>817.47 (+12.15%)</td><td>814.39 (+12.62%)</td><td>815.30 (+12.95%)</td><td>810.71 (+12.96%)</td><td>2.82 <b>(-38.38%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95749.80 (n/a)</td><td>95033.66 (n/a)</td><td>95203.60 (n/a)</td><td>94274.20 (n/a)</td><td>601.64 (n/a)</td><td>728.93 (n/a)</td><td>723.13 (n/a)</td><td>721.82 (n/a)</td><td>717.70 (n/a)</td><td>4.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.72 <b>(+44.85%)</b></td><td>4.27 <b>(+47.18%)</b></td><td>4.03 <b>(+46.16%)</b></td><td>3.64 <b>(+68.17%)</b></td><td>0.83 (+4.61%)</td><td>2448.90 <b>(-40.53%)</b></td><td>2141.86 <b>(-34.30%)</b></td><td>2210.50 <b>(-31.58%)</b></td><td>1559.30 <b>(-30.96%)</b></td><td>341.53 <b>(-60.15%)</b></td><td>344.30 <b>(+44.85%)</b></td><td>256.99 <b>(+47.18%)</b></td><td>242.87 <b>(+46.16%)</b></td><td>219.23 <b>(+68.17%)</b></td><td>49.88 (+4.61%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.95 (n/a)</td><td>2.90 (n/a)</td><td>2.76 (n/a)</td><td>2.16 (n/a)</td><td>0.79 (n/a)</td><td>4118.20 (n/a)</td><td>3259.92 (n/a)</td><td>3231.00 (n/a)</td><td>2258.60 (n/a)</td><td>856.98 (n/a)</td><td>237.70 (n/a)</td><td>174.61 (n/a)</td><td>166.16 (n/a)</td><td>130.36 (n/a)</td><td>47.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.58 (+19.33%)</td><td>2.77 (-0.38%)</td><td>2.31 (-7.20%)</td><td>1.94 (-5.91%)</td><td>1.05 <b>(+34.36%)</b></td><td>4583.00 (+6.28%)</td><td>3512.66 (+3.17%)</td><td>3860.60 (+7.75%)</td><td>1944.30 (-16.20%)</td><td>992.08 (+11.86%)</td><td>276.13 (+19.33%)</td><td>166.79 (-0.38%)</td><td>139.07 (-7.20%)</td><td>117.14 (-5.91%)</td><td>63.35 <b>(+34.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.84 (n/a)</td><td>2.78 (n/a)</td><td>2.49 (n/a)</td><td>2.07 (n/a)</td><td>0.78 (n/a)</td><td>4312.30 (n/a)</td><td>3404.66 (n/a)</td><td>3582.80 (n/a)</td><td>2320.10 (n/a)</td><td>886.92 (n/a)</td><td>231.40 (n/a)</td><td>167.42 (n/a)</td><td>149.85 (n/a)</td><td>124.50 (n/a)</td><td>47.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.97 (+10.25%)</td><td>3.54 (-11.44%)</td><td>3.19 (-13.77%)</td><td>2.11 (-3.27%)</td><td>1.48 (+10.31%)</td><td>4234.10 (+3.38%)</td><td>2837.28 (+14.21%)</td><td>2793.00 (+15.96%)</td><td>1492.40 (-9.29%)</td><td>1016.37 (+2.65%)</td><td>359.74 (+10.25%)</td><td>213.33 (-11.44%)</td><td>192.22 (-13.77%)</td><td>126.80 (-3.27%)</td><td>89.24 (+10.31%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.42 (n/a)</td><td>4.00 (n/a)</td><td>3.70 (n/a)</td><td>2.18 (n/a)</td><td>1.34 (n/a)</td><td>4095.60 (n/a)</td><td>2484.20 (n/a)</td><td>2408.50 (n/a)</td><td>1645.30 (n/a)</td><td>990.11 (n/a)</td><td>326.31 (n/a)</td><td>240.88 (n/a)</td><td>222.90 (n/a)</td><td>131.09 (n/a)</td><td>80.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.38 (-4.22%)</td><td>5.56 (-1.08%)</td><td>6.03 (+6.13%)</td><td>4.29 (+3.24%)</td><td>0.86 (-9.61%)</td><td>8122.30 (-3.14%)</td><td>6402.10 (+0.61%)</td><td>5782.30 (-5.78%)</td><td>5466.20 (+4.40%)</td><td>1099.05 (-10.18%)</td><td>392.87 (-4.22%)</td><td>342.68 (-1.08%)</td><td>371.39 (+6.13%)</td><td>264.39 (+3.24%)</td><td>52.99 (-9.61%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.66 (n/a)</td><td>5.62 (n/a)</td><td>5.68 (n/a)</td><td>4.16 (n/a)</td><td>0.95 (n/a)</td><td>8385.60 (n/a)</td><td>6363.00 (n/a)</td><td>6137.00 (n/a)</td><td>5235.60 (n/a)</td><td>1223.64 (n/a)</td><td>410.17 (n/a)</td><td>346.42 (n/a)</td><td>349.92 (n/a)</td><td>256.09 (n/a)</td><td>58.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.69 (+2.47%)</td><td>5.11 (+8.57%)</td><td>5.34 <b>(+21.85%)</b></td><td>4.51 (+8.82%)</td><td>0.52 <b>(-22.04%)</b></td><td>7727.60 (-8.11%)</td><td>6877.16 (-8.53%)</td><td>6532.20 (-17.93%)</td><td>6131.50 (-2.41%)</td><td>716.66 <b>(-29.48%)</b></td><td>350.24 (+2.47%)</td><td>314.93 (+8.57%)</td><td>328.75 <b>(+21.85%)</b></td><td>277.90 (+8.82%)</td><td>32.03 <b>(-22.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.55 (n/a)</td><td>4.71 (n/a)</td><td>4.38 (n/a)</td><td>4.15 (n/a)</td><td>0.67 (n/a)</td><td>8409.30 (n/a)</td><td>7518.30 (n/a)</td><td>7959.40 (n/a)</td><td>6282.80 (n/a)</td><td>1016.24 (n/a)</td><td>341.80 (n/a)</td><td>290.07 (n/a)</td><td>269.81 (n/a)</td><td>255.37 (n/a)</td><td>41.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.49 (+11.83%)</td><td>5.64 (+8.89%)</td><td>5.49 (+6.00%)</td><td>5.21 (+15.45%)</td><td>0.49 (-14.22%)</td><td>6688.80 (-13.38%)</td><td>6211.50 (-8.56%)</td><td>6349.30 (-5.66%)</td><td>5374.60 (-10.58%)</td><td>498.00 <b>(-34.32%)</b></td><td>399.56 (+11.83%)</td><td>347.67 (+8.89%)</td><td>338.22 (+6.00%)</td><td>321.06 (+15.45%)</td><td>30.31 (-14.22%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.80 (n/a)</td><td>5.18 (n/a)</td><td>5.18 (n/a)</td><td>4.52 (n/a)</td><td>0.57 (n/a)</td><td>7721.90 (n/a)</td><td>6792.78 (n/a)</td><td>6730.10 (n/a)</td><td>6010.40 (n/a)</td><td>758.22 (n/a)</td><td>357.30 (n/a)</td><td>319.29 (n/a)</td><td>319.09 (n/a)</td><td>278.10 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.78 (+0.20%)</td><td>0.76 (-1.03%)</td><td>0.76 (-0.37%)</td><td>0.74 (-2.30%)</td><td>0.02 <b>(+129.55%)</b></td><td>101893.50 (+2.36%)</td><td>99513.02 (+1.08%)</td><td>98941.40 (+0.37%)</td><td>96722.30 (-0.20%)</td><td>2252.14 <b>(+136.00%)</b></td><td>710.48 (+0.20%)</td><td>690.84 (-1.03%)</td><td>694.55 (-0.37%)</td><td>674.42 (-2.30%)</td><td>15.63 <b>(+129.55%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99545.00 (n/a)</td><td>98450.58 (n/a)</td><td>98574.20 (n/a)</td><td>96914.10 (n/a)</td><td>954.29 (n/a)</td><td>709.08 (n/a)</td><td>698.06 (n/a)</td><td>697.13 (n/a)</td><td>690.34 (n/a)</td><td>6.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.77 (-0.91%)</td><td>0.76 (+1.25%)</td><td>0.76 (+1.86%)</td><td>0.75 (+3.76%)</td><td>0.01 <b>(-57.47%)</b></td><td>101052.30 (-3.63%)</td><td>99268.06 (-1.30%)</td><td>98823.70 (-1.83%)</td><td>97820.50 (+0.92%)</td><td>1287.63 <b>(-58.58%)</b></td><td>702.51 (-0.91%)</td><td>692.35 (+1.25%)</td><td>695.37 (+1.86%)</td><td>680.04 (+3.76%)</td><td>8.94 <b>(-57.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.72 (n/a)</td><td>0.02 (n/a)</td><td>104853.40 (n/a)</td><td>100571.72 (n/a)</td><td>100666.70 (n/a)</td><td>96932.50 (n/a)</td><td>3108.38 (n/a)</td><td>708.94 (n/a)</td><td>683.81 (n/a)</td><td>682.64 (n/a)</td><td>655.39 (n/a)</td><td>21.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.89 (+10.08%)</td><td>0.88 (+9.45%)</td><td>0.88 (+9.45%)</td><td>0.87 (+8.30%)</td><td>0.01 <b>(+256.56%)</b></td><td>87117.30 (-7.66%)</td><td>85860.48 (-8.63%)</td><td>85845.40 (-8.63%)</td><td>85108.80 (-9.15%)</td><td>823.80 <b>(+198.96%)</b></td><td>807.43 (+10.08%)</td><td>800.42 (+9.45%)</td><td>800.50 (+9.45%)</td><td>788.82 (+8.30%)</td><td>7.64 <b>(+256.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94344.80 (n/a)</td><td>93970.78 (n/a)</td><td>93955.80 (n/a)</td><td>93685.00 (n/a)</td><td>275.55 (n/a)</td><td>733.52 (n/a)</td><td>731.29 (n/a)</td><td>731.40 (n/a)</td><td>728.39 (n/a)</td><td>2.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.55 <b>(+34.91%)</b></td><td>2.27 (-12.95%)</td><td>1.68 <b>(-46.57%)</b></td><td>1.42 (-9.70%)</td><td>1.31 <b>(+40.89%)</b></td><td>5663.00 (+10.75%)</td><td>4253.02 <b>(+21.40%)</b></td><td>4801.80 <b>(+87.18%)</b></td><td>1771.50 <b>(-25.88%)</b></td><td>1563.16 (+9.42%)</td><td>1193.30 <b>(+34.91%)</b></td><td>594.30 (-12.95%)</td><td>440.24 <b>(-46.57%)</b></td><td>373.29 (-9.70%)</td><td>342.80 <b>(+40.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.37 (n/a)</td><td>2.60 (n/a)</td><td>3.14 (n/a)</td><td>1.58 (n/a)</td><td>0.93 (n/a)</td><td>5113.40 (n/a)</td><td>3503.32 (n/a)</td><td>2565.40 (n/a)</td><td>2389.90 (n/a)</td><td>1428.54 (n/a)</td><td>884.51 (n/a)</td><td>682.68 (n/a)</td><td>824.00 (n/a)</td><td>413.41 (n/a)</td><td>243.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.24 (+0.80%)</td><td>0.19 (+4.95%)</td><td>0.18 (+0.91%)</td><td>0.13 (-4.50%)</td><td>0.05 <b>(+31.79%)</b></td><td>9416.00 (+4.72%)</td><td>6990.04 (-2.65%)</td><td>7079.30 (-0.91%)</td><td>5270.80 (-0.80%)</td><td>1752.08 <b>(+33.67%)</b></td><td>12.73 (+0.80%)</td><td>10.09 (+4.95%)</td><td>9.48 (+0.91%)</td><td>7.13 (-4.50%)</td><td>2.48 <b>(+31.79%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>8991.90 (n/a)</td><td>7180.48 (n/a)</td><td>7144.00 (n/a)</td><td>5313.20 (n/a)</td><td>1310.71 (n/a)</td><td>12.63 (n/a)</td><td>9.62 (n/a)</td><td>9.39 (n/a)</td><td>7.46 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.81 (n/a)</td><td>3.58 (n/a)</td><td>3.46 (n/a)</td><td>3.36 (n/a)</td><td>0.21 (n/a)</td><td>3.81 (n/a)</td><td>3.57 (n/a)</td><td>3.46 (n/a)</td><td>3.35 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>7.27 (-5.52%)</td><td>6.25 (-9.64%)</td><td>5.81 <b>(-20.01%)</b></td><td>5.45 (+5.04%)</td><td>0.84 (-18.92%)</td><td>7.27 (-5.52%)</td><td>6.24 (-9.64%)</td><td>5.80 <b>(-20.01%)</b></td><td>5.44 (+5.04%)</td><td>0.84 (-18.92%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.70 (n/a)</td><td>6.91 (n/a)</td><td>7.26 (n/a)</td><td>5.19 (n/a)</td><td>1.03 (n/a)</td><td>7.69 (n/a)</td><td>6.91 (n/a)</td><td>7.25 (n/a)</td><td>5.18 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.48 <b>(-32.39%)</b></td><td>7.70 (-17.56%)</td><td>7.58 (-7.62%)</td><td>6.78 (-15.18%)</td><td>0.67 <b>(-65.21%)</b></td><td>8.47 <b>(-32.39%)</b></td><td>7.69 (-17.56%)</td><td>7.58 (-7.62%)</td><td>6.78 (-15.18%)</td><td>0.67 <b>(-65.21%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>12.54 (n/a)</td><td>9.33 (n/a)</td><td>8.21 (n/a)</td><td>8.00 (n/a)</td><td>1.94 (n/a)</td><td>12.53 (n/a)</td><td>9.33 (n/a)</td><td>8.20 (n/a)</td><td>7.99 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.92 (n/a)</td><td>3.60 (n/a)</td><td>3.77 (n/a)</td><td>2.92 (n/a)</td><td>0.40 (n/a)</td><td>3.92 (n/a)</td><td>3.60 (n/a)</td><td>3.77 (n/a)</td><td>2.92 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>7.04 (+4.03%)</td><td>6.29 (+1.69%)</td><td>6.14 (-6.54%)</td><td>5.59 (+2.39%)</td><td>0.63 (-0.30%)</td><td>7.04 (+4.03%)</td><td>6.29 (+1.69%)</td><td>6.14 (-6.54%)</td><td>5.58 (+2.39%)</td><td>0.63 (-0.30%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.77 (n/a)</td><td>6.19 (n/a)</td><td>6.57 (n/a)</td><td>5.46 (n/a)</td><td>0.63 (n/a)</td><td>6.77 (n/a)</td><td>6.18 (n/a)</td><td>6.56 (n/a)</td><td>5.45 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>9.77 <b>(-30.22%)</b></td><td>8.43 <b>(-27.03%)</b></td><td>8.22 <b>(-38.73%)</b></td><td>7.39 (-11.08%)</td><td>0.87 <b>(-70.67%)</b></td><td>9.76 <b>(-30.22%)</b></td><td>8.42 <b>(-27.03%)</b></td><td>8.21 <b>(-38.73%)</b></td><td>7.39 (-11.08%)</td><td>0.86 <b>(-70.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>14.00 (n/a)</td><td>11.55 (n/a)</td><td>13.41 (n/a)</td><td>8.31 (n/a)</td><td>2.95 (n/a)</td><td>13.99 (n/a)</td><td>11.54 (n/a)</td><td>13.41 (n/a)</td><td>8.31 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.07 (+0.20%)</td><td>2.84 <b>(+56.47%)</b></td><td>2.78 <b>(+135.92%)</b></td><td>2.72 <b>(+157.73%)</b></td><td>0.14 <b>(-85.49%)</b></td><td>3.06 (+0.20%)</td><td>2.84 <b>(+56.47%)</b></td><td>2.78 <b>(+135.92%)</b></td><td>2.71 <b>(+157.73%)</b></td><td>0.14 <b>(-85.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.06 (n/a)</td><td>1.82 (n/a)</td><td>1.18 (n/a)</td><td>1.06 (n/a)</td><td>0.97 (n/a)</td><td>3.06 (n/a)</td><td>1.81 (n/a)</td><td>1.18 (n/a)</td><td>1.05 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.44 <b>(-28.69%)</b></td><td>0.23 <b>(-26.08%)</b></td><td>0.25 (-2.17%)</td><td>0.07 (-13.95%)</td><td>0.16 (-18.82%)</td><td>0.44 <b>(-28.69%)</b></td><td>0.23 <b>(-26.08%)</b></td><td>0.24 (-2.17%)</td><td>0.07 (-13.95%)</td><td>0.16 (-18.82%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.62 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>0.20 (n/a)</td><td>0.61 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.72 (-5.09%)</td><td>0.62 <b>(+68.41%)</b></td><td>0.67 <b>(+118.00%)</b></td><td>0.37 <b>(+378.29%)</b></td><td>0.14 <b>(-43.14%)</b></td><td>0.72 (-5.09%)</td><td>0.61 <b>(+68.41%)</b></td><td>0.66 <b>(+118.00%)</b></td><td>0.37 <b>(+378.29%)</b></td><td>0.14 <b>(-43.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.76 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.75 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.36 (-16.68%)</td><td>1.82 (-13.84%)</td><td>2.15 (-10.42%)</td><td>0.77 <b>(-43.59%)</b></td><td>0.69 (+5.52%)</td><td>2.32 (-16.68%)</td><td>1.79 (-13.84%)</td><td>2.11 (-10.42%)</td><td>0.76 <b>(-43.59%)</b></td><td>0.68 (+5.52%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.83 (n/a)</td><td>2.11 (n/a)</td><td>2.40 (n/a)</td><td>1.36 (n/a)</td><td>0.65 (n/a)</td><td>2.79 (n/a)</td><td>2.07 (n/a)</td><td>2.36 (n/a)</td><td>1.34 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.60 (n/a)</td><td>369.46 (n/a)</td><td>306.60 (n/a)</td><td>269.70 (n/a)</td><td>126.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1968.30 (n/a)</td><td>795.32 (n/a)</td><td>684.00 (n/a)</td><td>239.20 (n/a)</td><td>699.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2537.40 (n/a)</td><td>797.68 (n/a)</td><td>391.70 (n/a)</td><td>240.80 (n/a)</td><td>981.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.00 (n/a)</td><td>387.66 (n/a)</td><td>409.40 (n/a)</td><td>246.30 (n/a)</td><td>137.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1897.40 (n/a)</td><td>729.16 (n/a)</td><td>480.50 (n/a)</td><td>253.70 (n/a)</td><td>668.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.50 (n/a)</td><td>483.26 (n/a)</td><td>528.50 (n/a)</td><td>339.30 (n/a)</td><td>124.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>647.40 (n/a)</td><td>390.06 (n/a)</td><td>300.30 (n/a)</td><td>230.10 (n/a)</td><td>185.45 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>444.40 (n/a)</td><td>305.18 (n/a)</td><td>272.70 (n/a)</td><td>219.40 (n/a)</td><td>90.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.10 (n/a)</td><td>340.22 (n/a)</td><td>312.80 (n/a)</td><td>241.30 (n/a)</td><td>122.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>382.06 (n/a)</td><td>408.40 (n/a)</td><td>234.90 (n/a)</td><td>145.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1902.60 (n/a)</td><td>796.88 (n/a)</td><td>529.20 (n/a)</td><td>423.40 (n/a)</td><td>622.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1043.40 (n/a)</td><td>567.06 (n/a)</td><td>512.90 (n/a)</td><td>233.50 (n/a)</td><td>300.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.50 (n/a)</td><td>425.42 (n/a)</td><td>467.50 (n/a)</td><td>237.00 (n/a)</td><td>128.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.00 (n/a)</td><td>423.14 (n/a)</td><td>447.30 (n/a)</td><td>196.60 (n/a)</td><td>172.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.20 (n/a)</td><td>440.84 (n/a)</td><td>532.10 (n/a)</td><td>226.70 (n/a)</td><td>175.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>593.40 (n/a)</td><td>497.12 (n/a)</td><td>501.90 (n/a)</td><td>437.90 (n/a)</td><td>62.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>564.90 (n/a)</td><td>461.68 (n/a)</td><td>477.80 (n/a)</td><td>317.20 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>679.50 (n/a)</td><td>477.78 (n/a)</td><td>355.70 (n/a)</td><td>332.90 (n/a)</td><td>179.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>501.00 (n/a)</td><td>330.98 (n/a)</td><td>297.70 (n/a)</td><td>270.50 (n/a)</td><td>95.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>559.00 (n/a)</td><td>419.46 (n/a)</td><td>462.40 (n/a)</td><td>246.30 (n/a)</td><td>129.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>659.70 (n/a)</td><td>501.02 (n/a)</td><td>516.90 (n/a)</td><td>273.80 (n/a)</td><td>142.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>636.60 (n/a)</td><td>403.42 (n/a)</td><td>303.10 (n/a)</td><td>221.20 (n/a)</td><td>185.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.00 (n/a)</td><td>385.16 (n/a)</td><td>375.30 (n/a)</td><td>253.70 (n/a)</td><td>131.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>470.80 (n/a)</td><td>338.16 (n/a)</td><td>304.30 (n/a)</td><td>221.50 (n/a)</td><td>108.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+2.67%)</td><td>0.01 <b>(+24.15%)</b></td><td>0.02 <b>(+92.87%)</b></td><td>0.01 (+0.92%)</td><td>0.01 (+2.70%)</td><td>573.30 (-0.92%)</td><td>336.72 (-19.82%)</td><td>263.00 <b>(-48.15%)</b></td><td>207.70 (-2.58%)</td><td>157.79 (-4.54%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.60 (n/a)</td><td>419.94 (n/a)</td><td>507.20 (n/a)</td><td>213.20 (n/a)</td><td>165.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+22.89%)</b></td><td>0.01 (+9.26%)</td><td>0.01 (+10.14%)</td><td>0.00 <b>(-72.87%)</b></td><td>0.01 <b>(+119.84%)</b></td><td>2042.00 <b>(+268.59%)</b></td><td>699.54 <b>(+52.27%)</b></td><td>435.80 (-9.21%)</td><td>237.00 (-18.61%)</td><td>757.84 <b>(+659.74%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.00 (n/a)</td><td>459.42 (n/a)</td><td>480.00 (n/a)</td><td>291.20 (n/a)</td><td>99.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+9.13%)</td><td>0.01 <b>(+47.17%)</b></td><td>0.02 <b>(+131.61%)</b></td><td>0.01 (+6.10%)</td><td>0.01 <b>(+38.06%)</b></td><td>549.20 (-5.75%)</td><td>355.60 <b>(-27.53%)</b></td><td>237.10 <b>(-56.84%)</b></td><td>230.50 (-8.35%)</td><td>168.35 <b>(+21.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.70 (n/a)</td><td>490.70 (n/a)</td><td>549.30 (n/a)</td><td>251.50 (n/a)</td><td>138.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (+4.24%)</td><td>0.01 <b>(+24.37%)</b></td><td>0.01 <b>(+39.81%)</b></td><td>0.01 (+12.88%)</td><td>0.00 (-9.24%)</td><td>484.00 (-11.40%)</td><td>368.56 <b>(-20.84%)</b></td><td>361.00 <b>(-28.47%)</b></td><td>279.90 (-4.08%)</td><td>81.80 <b>(-22.01%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.30 (n/a)</td><td>465.56 (n/a)</td><td>504.70 (n/a)</td><td>291.80 (n/a)</td><td>104.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-16.15%)</td><td>0.01 (-12.88%)</td><td>0.01 (-4.74%)</td><td>0.01 (-8.60%)</td><td>0.00 <b>(-27.93%)</b></td><td>580.50 (+9.40%)</td><td>458.44 (+10.77%)</td><td>481.70 (+4.97%)</td><td>280.10 (+19.24%)</td><td>116.71 (-11.56%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.60 (n/a)</td><td>413.86 (n/a)</td><td>458.90 (n/a)</td><td>234.90 (n/a)</td><td>131.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-16.24%)</td><td>0.01 (+10.50%)</td><td>0.01 <b>(+20.14%)</b></td><td>0.01 (+14.58%)</td><td>0.00 (-18.11%)</td><td>546.00 (-12.72%)</td><td>412.32 (-14.05%)</td><td>484.40 (-16.77%)</td><td>249.90 (+19.40%)</td><td>147.18 (-18.79%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.60 (n/a)</td><td>479.70 (n/a)</td><td>582.00 (n/a)</td><td>209.30 (n/a)</td><td>181.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+4.54%)</td><td>0.03 <b>(+62.42%)</b></td><td>0.03 <b>(+93.95%)</b></td><td>0.03 <b>(+101.40%)</b></td><td>0.00 <b>(-68.17%)</b></td><td>298.80 <b>(-50.35%)</b></td><td>274.46 <b>(-43.74%)</b></td><td>267.70 <b>(-48.44%)</b></td><td>245.50 (-4.33%)</td><td>21.91 <b>(-83.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.80 (n/a)</td><td>487.86 (n/a)</td><td>519.20 (n/a)</td><td>256.60 (n/a)</td><td>136.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (+1.61%)</td><td>0.02 (-14.34%)</td><td>0.02 <b>(-34.94%)</b></td><td>0.02 (+2.35%)</td><td>0.01 (+15.03%)</td><td>505.20 (-2.30%)</td><td>383.98 (+18.58%)</td><td>442.50 <b>(+53.70%)</b></td><td>222.20 (-1.59%)</td><td>117.82 (+4.10%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.10 (n/a)</td><td>323.82 (n/a)</td><td>287.90 (n/a)</td><td>225.80 (n/a)</td><td>113.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+1.21%)</td><td>0.03 (+2.16%)</td><td>0.03 (+4.42%)</td><td>0.02 <b>(+24.02%)</b></td><td>0.00 (-12.51%)</td><td>387.10 (-19.35%)</td><td>322.66 (-3.64%)</td><td>294.90 (-4.22%)</td><td>264.30 (-1.20%)</td><td>57.72 <b>(-31.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.00 (n/a)</td><td>334.86 (n/a)</td><td>307.90 (n/a)</td><td>267.50 (n/a)</td><td>83.87 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(+32.79%)</b></td><td>0.03 (+9.61%)</td><td>0.03 (+4.68%)</td><td>0.02 <b>(+22.32%)</b></td><td>0.01 <b>(+38.60%)</b></td><td>542.10 (-18.26%)</td><td>349.78 (-7.12%)</td><td>280.30 (-4.46%)</td><td>209.80 <b>(-24.69%)</b></td><td>140.72 (-13.83%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.20 (n/a)</td><td>376.60 (n/a)</td><td>293.40 (n/a)</td><td>278.60 (n/a)</td><td>163.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+13.60%)</td><td>0.02 (+0.59%)</td><td>0.02 (-7.69%)</td><td>0.02 (+0.83%)</td><td>0.01 (+18.80%)</td><td>518.20 (-0.82%)</td><td>406.22 (+0.67%)</td><td>439.90 (+8.32%)</td><td>262.60 (-11.97%)</td><td>106.79 (+6.07%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.50 (n/a)</td><td>403.50 (n/a)</td><td>406.10 (n/a)</td><td>298.30 (n/a)</td><td>100.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+31.78%)</b></td><td>0.03 <b>(+39.25%)</b></td><td>0.02 <b>(+35.54%)</b></td><td>0.02 <b>(+26.79%)</b></td><td>0.01 <b>(+67.44%)</b></td><td>513.50 <b>(-21.13%)</b></td><td>354.00 <b>(-25.47%)</b></td><td>338.60 <b>(-26.21%)</b></td><td>235.60 <b>(-24.10%)</b></td><td>120.59 (-0.82%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.10 (n/a)</td><td>474.96 (n/a)</td><td>458.90 (n/a)</td><td>310.40 (n/a)</td><td>121.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+48.56%)</b></td><td>0.03 <b>(+46.92%)</b></td><td>0.03 <b>(+57.99%)</b></td><td>0.02 <b>(+26.46%)</b></td><td>0.01 <b>(+73.31%)</b></td><td>523.60 <b>(-20.93%)</b></td><td>321.00 <b>(-29.90%)</b></td><td>277.70 <b>(-36.71%)</b></td><td>234.60 <b>(-32.68%)</b></td><td>115.33 (-4.65%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.20 (n/a)</td><td>457.92 (n/a)</td><td>438.80 (n/a)</td><td>348.50 (n/a)</td><td>120.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+40.99%)</b></td><td>0.02 <b>(+21.76%)</b></td><td>0.02 (+15.57%)</td><td>0.01 (+9.50%)</td><td>0.01 <b>(+77.71%)</b></td><td>580.30 (-8.67%)</td><td>453.38 (-13.84%)</td><td>491.90 (-13.46%)</td><td>236.60 <b>(-29.08%)</b></td><td>130.61 (+12.55%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.40 (n/a)</td><td>526.20 (n/a)</td><td>568.40 (n/a)</td><td>333.60 (n/a)</td><td>116.05 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+4.43%)</td><td>0.05 (+19.97%)</td><td>0.04 <b>(+29.15%)</b></td><td>0.03 (+1.12%)</td><td>0.01 (-1.32%)</td><td>512.30 (-1.12%)</td><td>368.94 (-17.17%)</td><td>388.70 <b>(-22.57%)</b></td><td>240.30 (-4.22%)</td><td>105.20 (-5.63%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>518.10 (n/a)</td><td>445.42 (n/a)</td><td>502.00 (n/a)</td><td>250.90 (n/a)</td><td>111.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 <b>(+49.49%)</b></td><td>0.05 <b>(+33.02%)</b></td><td>0.04 (+18.79%)</td><td>0.03 (+5.31%)</td><td>0.01 <b>(+196.60%)</b></td><td>477.00 (-5.06%)</td><td>342.92 <b>(-20.84%)</b></td><td>370.30 (-15.80%)</td><td>247.70 <b>(-33.11%)</b></td><td>96.67 <b>(+78.23%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>502.40 (n/a)</td><td>433.20 (n/a)</td><td>439.80 (n/a)</td><td>370.30 (n/a)</td><td>54.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+7.87%)</td><td>0.04 (-8.21%)</td><td>0.04 (-1.01%)</td><td>0.02 <b>(-38.97%)</b></td><td>0.03 <b>(+20.66%)</b></td><td>987.90 <b>(+63.86%)</b></td><td>499.58 <b>(+26.55%)</b></td><td>448.60 (+1.04%)</td><td>196.50 (-7.31%)</td><td>311.91 <b>(+90.41%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.90 (n/a)</td><td>394.78 (n/a)</td><td>444.00 (n/a)</td><td>212.00 (n/a)</td><td>163.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 <b>(+20.09%)</b></td><td>0.05 (+15.11%)</td><td>0.04 (+11.76%)</td><td>0.03 <b>(+74.03%)</b></td><td>0.02 (+3.20%)</td><td>593.70 <b>(-42.54%)</b></td><td>380.32 <b>(-22.41%)</b></td><td>374.10 (-10.52%)</td><td>204.90 (-16.71%)</td><td>155.14 <b>(-51.37%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1033.30 (n/a)</td><td>490.18 (n/a)</td><td>418.10 (n/a)</td><td>246.00 (n/a)</td><td>319.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+3.89%)</td><td>0.05 (-3.20%)</td><td>0.04 (-18.65%)</td><td>0.03 (-9.06%)</td><td>0.02 (+8.96%)</td><td>599.60 (+9.96%)</td><td>399.96 (+4.89%)</td><td>408.50 <b>(+22.93%)</b></td><td>236.70 (-3.74%)</td><td>143.10 (+9.64%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.30 (n/a)</td><td>381.32 (n/a)</td><td>332.30 (n/a)</td><td>245.90 (n/a)</td><td>130.52 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 <b>(+37.30%)</b></td><td>0.04 (+7.66%)</td><td>0.03 (-17.55%)</td><td>0.03 (+7.51%)</td><td>0.02 <b>(+69.35%)</b></td><td>589.20 (-6.98%)</td><td>438.02 (+0.38%)</td><td>520.40 <b>(+21.31%)</b></td><td>222.10 <b>(-27.16%)</b></td><td>168.83 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>633.40 (n/a)</td><td>436.36 (n/a)</td><td>429.00 (n/a)</td><td>304.90 (n/a)</td><td>136.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (-10.91%)</td><td>0.09 (-8.41%)</td><td>0.08 <b>(-28.69%)</b></td><td>0.08 <b>(+40.50%)</b></td><td>0.02 <b>(-40.61%)</b></td><td>429.30 <b>(-28.83%)</b></td><td>375.06 (+1.68%)</td><td>422.30 <b>(+40.21%)</b></td><td>283.60 (+12.23%)</td><td>70.56 <b>(-51.46%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>603.20 (n/a)</td><td>368.88 (n/a)</td><td>301.20 (n/a)</td><td>252.70 (n/a)</td><td>145.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (+14.80%)</td><td>0.12 (+14.29%)</td><td>0.12 (-0.17%)</td><td>0.11 <b>(+50.72%)</b></td><td>0.02 <b>(-20.67%)</b></td><td>310.10 <b>(-33.65%)</b></td><td>270.36 (-15.33%)</td><td>277.50 (+0.14%)</td><td>217.10 (-12.88%)</td><td>41.25 <b>(-53.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>467.40 (n/a)</td><td>319.30 (n/a)</td><td>277.10 (n/a)</td><td>249.20 (n/a)</td><td>89.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (+2.75%)</td><td>0.09 <b>(+23.05%)</b></td><td>0.08 (+17.18%)</td><td>0.06 <b>(+320.44%)</b></td><td>0.04 (-19.97%)</td><td>570.10 <b>(-76.21%)</b></td><td>403.52 <b>(-50.05%)</b></td><td>432.30 (-14.67%)</td><td>238.10 (-2.66%)</td><td>149.45 <b>(-83.37%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2396.80 (n/a)</td><td>807.84 (n/a)</td><td>506.60 (n/a)</td><td>244.60 (n/a)</td><td>898.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (+13.20%)</td><td>0.11 <b>(+20.61%)</b></td><td>0.11 <b>(+46.32%)</b></td><td>0.06 (-16.10%)</td><td>0.03 <b>(+27.89%)</b></td><td>594.90 (+19.19%)</td><td>341.88 (-13.39%)</td><td>285.30 <b>(-31.65%)</b></td><td>243.70 (-11.67%)</td><td>143.96 <b>(+43.21%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>499.10 (n/a)</td><td>394.72 (n/a)</td><td>417.40 (n/a)</td><td>275.90 (n/a)</td><td>100.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (+0.09%)</td><td>0.08 <b>(+40.82%)</b></td><td>0.08 <b>(+37.39%)</b></td><td>0.05 <b>(+200.69%)</b></td><td>0.03 <b>(-37.89%)</b></td><td>636.00 <b>(-66.75%)</b></td><td>451.40 <b>(-55.03%)</b></td><td>398.30 <b>(-27.21%)</b></td><td>287.70 (-0.10%)</td><td>144.35 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1912.50 (n/a)</td><td>1003.72 (n/a)</td><td>547.20 (n/a)</td><td>288.00 (n/a)</td><td>789.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+21.70%)</b></td><td>0.01 (-4.49%)</td><td>0.01 (-13.33%)</td><td>0.01 (-14.56%)</td><td>0.00 <b>(+48.31%)</b></td><td>578.30 (+17.04%)</td><td>433.62 (+10.62%)</td><td>445.70 (+15.38%)</td><td>243.00 (-17.85%)</td><td>143.86 <b>(+47.77%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.10 (n/a)</td><td>392.00 (n/a)</td><td>386.30 (n/a)</td><td>295.80 (n/a)</td><td>97.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-10.61%)</td><td>0.01 (-3.11%)</td><td>0.01 (+1.95%)</td><td>0.01 (+2.75%)</td><td>0.00 (-11.07%)</td><td>529.20 (-2.67%)</td><td>368.00 (+2.09%)</td><td>326.50 (-1.92%)</td><td>283.40 (+11.84%)</td><td>104.32 (-7.40%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.70 (n/a)</td><td>360.46 (n/a)</td><td>332.90 (n/a)</td><td>253.40 (n/a)</td><td>112.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 <b>(-39.75%)</b></td><td>0.01 (-19.56%)</td><td>0.01 (-6.57%)</td><td>0.01 (-10.93%)</td><td>0.00 <b>(-65.98%)</b></td><td>607.10 (+12.28%)</td><td>498.44 (+18.64%)</td><td>457.10 (+7.02%)</td><td>447.60 <b>(+65.96%)</b></td><td>68.10 <b>(-36.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.70 (n/a)</td><td>420.14 (n/a)</td><td>427.10 (n/a)</td><td>269.70 (n/a)</td><td>107.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 <b>(-21.45%)</b></td><td>0.01 (-9.31%)</td><td>0.01 (-6.56%)</td><td>0.01 (+13.66%)</td><td>0.00 <b>(-44.38%)</b></td><td>448.90 (-12.01%)</td><td>343.60 (+4.98%)</td><td>312.60 (+7.02%)</td><td>281.90 <b>(+27.33%)</b></td><td>66.65 <b>(-39.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.20 (n/a)</td><td>327.30 (n/a)</td><td>292.10 (n/a)</td><td>221.40 (n/a)</td><td>110.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+4.53%)</td><td>0.01 (-15.22%)</td><td>0.01 (+4.85%)</td><td>0.00 <b>(-74.75%)</b></td><td>0.01 <b>(+36.79%)</b></td><td>2403.20 <b>(+296.04%)</b></td><td>809.54 <b>(+93.96%)</b></td><td>443.70 (-4.62%)</td><td>226.70 (-4.35%)</td><td>900.92 <b>(+502.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.80 (n/a)</td><td>417.38 (n/a)</td><td>465.20 (n/a)</td><td>237.00 (n/a)</td><td>149.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+1.16%)</td><td>0.01 (-3.57%)</td><td>0.01 (-0.99%)</td><td>0.01 (-17.29%)</td><td>0.00 (+7.01%)</td><td>616.70 <b>(+20.90%)</b></td><td>385.04 (+6.52%)</td><td>297.50 (+0.98%)</td><td>248.50 (-1.15%)</td><td>154.44 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.10 (n/a)</td><td>361.48 (n/a)</td><td>294.60 (n/a)</td><td>251.40 (n/a)</td><td>122.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+45.09%)</b></td><td>0.01 <b>(+39.62%)</b></td><td>0.01 <b>(+76.57%)</b></td><td>0.01 (+5.12%)</td><td>0.00 <b>(+149.44%)</b></td><td>618.10 (-4.86%)</td><td>394.14 <b>(-21.20%)</b></td><td>286.70 <b>(-43.36%)</b></td><td>262.80 <b>(-31.08%)</b></td><td>166.20 <b>(+61.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>649.70 (n/a)</td><td>500.18 (n/a)</td><td>506.20 (n/a)</td><td>381.30 (n/a)</td><td>102.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-14.85%)</td><td>0.01 (-15.33%)</td><td>0.01 (-5.87%)</td><td>0.01 <b>(-25.67%)</b></td><td>0.00 <b>(-21.41%)</b></td><td>613.30 <b>(+34.55%)</b></td><td>435.54 (+17.98%)</td><td>445.10 (+6.23%)</td><td>313.70 (+17.40%)</td><td>114.64 <b>(+27.65%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.80 (n/a)</td><td>369.16 (n/a)</td><td>419.00 (n/a)</td><td>267.20 (n/a)</td><td>89.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 <b>(-22.64%)</b></td><td>0.01 (-5.05%)</td><td>0.01 (+16.41%)</td><td>0.01 <b>(+74.03%)</b></td><td>0.00 <b>(-59.27%)</b></td><td>548.20 <b>(-42.54%)</b></td><td>427.98 (-13.69%)</td><td>398.10 (-14.09%)</td><td>329.50 <b>(+29.27%)</b></td><td>94.31 <b>(-66.97%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>954.00 (n/a)</td><td>495.88 (n/a)</td><td>463.40 (n/a)</td><td>254.90 (n/a)</td><td>285.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (+6.04%)</td><td>0.01 (+13.74%)</td><td>0.01 (-1.08%)</td><td>0.01 <b>(+108.89%)</b></td><td>0.00 <b>(-28.42%)</b></td><td>494.30 <b>(-52.13%)</b></td><td>364.96 <b>(-25.22%)</b></td><td>328.30 (+1.11%)</td><td>275.20 (-5.69%)</td><td>97.46 <b>(-68.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.50 (n/a)</td><td>488.02 (n/a)</td><td>324.70 (n/a)</td><td>291.80 (n/a)</td><td>312.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-9.15%)</td><td>0.01 (+5.82%)</td><td>0.01 (+5.84%)</td><td>0.01 <b>(+31.18%)</b></td><td>0.00 <b>(-63.11%)</b></td><td>468.30 <b>(-23.77%)</b></td><td>435.60 (-7.92%)</td><td>448.20 (-5.52%)</td><td>401.20 (+10.07%)</td><td>28.20 <b>(-69.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.30 (n/a)</td><td>473.08 (n/a)</td><td>474.40 (n/a)</td><td>364.50 (n/a)</td><td>92.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-13.76%)</td><td>0.01 (-3.57%)</td><td>0.01 (+0.09%)</td><td>0.01 <b>(+131.28%)</b></td><td>0.00 <b>(-44.23%)</b></td><td>814.80 <b>(-56.76%)</b></td><td>514.46 <b>(-26.85%)</b></td><td>481.10 (-0.08%)</td><td>334.80 (+15.97%)</td><td>179.48 <b>(-73.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1884.50 (n/a)</td><td>703.30 (n/a)</td><td>481.50 (n/a)</td><td>288.70 (n/a)</td><td>667.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(-48.21%)</b></td><td>0.02 <b>(-24.32%)</b></td><td>0.02 (-8.95%)</td><td>0.01 (-18.81%)</td><td>0.01 <b>(-59.79%)</b></td><td>657.40 <b>(+23.18%)</b></td><td>425.84 (+19.25%)</td><td>352.60 (+9.84%)</td><td>316.60 <b>(+93.05%)</b></td><td>142.02 (-6.24%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>357.10 (n/a)</td><td>321.00 (n/a)</td><td>164.00 (n/a)</td><td>151.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-5.69%)</td><td>0.02 (-8.61%)</td><td>0.03 (-3.10%)</td><td>0.00 <b>(-73.49%)</b></td><td>0.01 <b>(+38.02%)</b></td><td>1937.70 <b>(+277.20%)</b></td><td>635.36 <b>(+77.67%)</b></td><td>276.90 (+3.21%)</td><td>245.20 (+6.01%)</td><td>734.10 <b>(+415.91%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.70 (n/a)</td><td>357.60 (n/a)</td><td>268.30 (n/a)</td><td>231.30 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+3.92%)</td><td>0.02 (-13.72%)</td><td>0.02 (-11.52%)</td><td>0.01 <b>(-51.83%)</b></td><td>0.01 (+13.18%)</td><td>1154.20 <b>(+107.59%)</b></td><td>560.40 <b>(+34.34%)</b></td><td>532.60 (+13.01%)</td><td>245.10 (-3.77%)</td><td>355.19 <b>(+137.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>417.16 (n/a)</td><td>471.30 (n/a)</td><td>254.70 (n/a)</td><td>149.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (+13.13%)</td><td>0.02 (-8.15%)</td><td>0.02 <b>(-31.93%)</b></td><td>0.01 (-15.03%)</td><td>0.01 <b>(+49.04%)</b></td><td>620.40 (+17.68%)</td><td>397.38 (+19.48%)</td><td>390.00 <b>(+46.89%)</b></td><td>210.90 (-11.57%)</td><td>178.34 <b>(+49.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.20 (n/a)</td><td>332.60 (n/a)</td><td>265.50 (n/a)</td><td>238.50 (n/a)</td><td>119.34 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(-38.21%)</b></td><td>0.02 <b>(-34.02%)</b></td><td>0.02 <b>(-33.65%)</b></td><td>0.00 <b>(-71.92%)</b></td><td>0.01 (-14.12%)</td><td>2056.80 <b>(+256.09%)</b></td><td>754.52 <b>(+104.84%)</b></td><td>446.60 <b>(+50.73%)</b></td><td>368.30 <b>(+61.89%)</b></td><td>730.59 <b>(+414.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.60 (n/a)</td><td>368.34 (n/a)</td><td>296.30 (n/a)</td><td>227.50 (n/a)</td><td>142.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 <b>(+46.18%)</b></td><td>0.03 <b>(+61.28%)</b></td><td>0.03 <b>(+74.55%)</b></td><td>0.02 <b>(+47.23%)</b></td><td>0.01 <b>(+31.88%)</b></td><td>405.10 <b>(-32.08%)</b></td><td>268.36 <b>(-38.89%)</b></td><td>242.80 <b>(-42.71%)</b></td><td>177.80 <b>(-31.59%)</b></td><td>84.07 <b>(-36.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.40 (n/a)</td><td>439.16 (n/a)</td><td>423.80 (n/a)</td><td>259.90 (n/a)</td><td>133.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (+16.99%)</td><td>0.02 (+5.78%)</td><td>0.02 (+13.67%)</td><td>0.01 <b>(-46.34%)</b></td><td>0.01 <b>(+54.97%)</b></td><td>1051.90 <b>(+86.34%)</b></td><td>511.60 (+17.81%)</td><td>452.60 (-12.01%)</td><td>209.30 (-14.50%)</td><td>341.15 <b>(+128.74%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>434.26 (n/a)</td><td>514.40 (n/a)</td><td>244.80 (n/a)</td><td>149.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (+18.83%)</td><td>0.02 (-1.66%)</td><td>0.02 (-16.88%)</td><td>0.01 (+3.81%)</td><td>0.01 <b>(+32.70%)</b></td><td>561.40 (-3.67%)</td><td>385.96 (+4.20%)</td><td>367.70 <b>(+20.32%)</b></td><td>252.10 (-15.85%)</td><td>129.22 (+6.12%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.80 (n/a)</td><td>370.40 (n/a)</td><td>305.60 (n/a)</td><td>299.60 (n/a)</td><td>121.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-4.71%)</td><td>0.02 (+15.12%)</td><td>0.02 (+16.32%)</td><td>0.01 <b>(+231.31%)</b></td><td>0.01 <b>(-31.64%)</b></td><td>584.20 <b>(-69.82%)</b></td><td>402.10 <b>(-42.74%)</b></td><td>422.40 (-14.02%)</td><td>245.60 (+4.96%)</td><td>137.47 <b>(-80.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1935.60 (n/a)</td><td>702.18 (n/a)</td><td>491.30 (n/a)</td><td>234.00 (n/a)</td><td>701.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(+38.74%)</b></td><td>0.03 (+13.64%)</td><td>0.03 (+18.25%)</td><td>0.02 (-0.83%)</td><td>0.01 <b>(+98.10%)</b></td><td>492.20 (+0.84%)</td><td>351.50 (-7.13%)</td><td>317.10 (-15.44%)</td><td>218.00 <b>(-27.91%)</b></td><td>110.84 <b>(+48.63%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>488.10 (n/a)</td><td>378.50 (n/a)</td><td>375.00 (n/a)</td><td>302.40 (n/a)</td><td>74.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-7.78%)</td><td>0.02 (-16.71%)</td><td>0.01 (-8.30%)</td><td>0.01 <b>(-48.40%)</b></td><td>0.01 <b>(+21.66%)</b></td><td>1026.80 <b>(+93.77%)</b></td><td>606.28 <b>(+31.69%)</b></td><td>566.30 (+9.05%)</td><td>314.90 (+8.44%)</td><td>263.35 <b>(+157.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.90 (n/a)</td><td>460.38 (n/a)</td><td>519.30 (n/a)</td><td>290.40 (n/a)</td><td>102.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-19.88%)</td><td>0.01 <b>(-39.25%)</b></td><td>0.02 (-17.55%)</td><td>0.00 <b>(-77.45%)</b></td><td>0.01 <b>(+35.94%)</b></td><td>2467.40 <b>(+343.46%)</b></td><td>1145.06 <b>(+172.24%)</b></td><td>544.40 <b>(+21.27%)</b></td><td>336.80 <b>(+24.79%)</b></td><td>964.60 <b>(+716.30%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.40 (n/a)</td><td>420.60 (n/a)</td><td>448.90 (n/a)</td><td>269.90 (n/a)</td><td>118.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 <b>(-23.09%)</b></td><td>0.05 (-15.29%)</td><td>0.04 <b>(-26.47%)</b></td><td>0.03 (-4.66%)</td><td>0.02 <b>(-30.62%)</b></td><td>532.20 (+4.89%)</td><td>392.18 (+12.30%)</td><td>441.40 <b>(+36.02%)</b></td><td>246.50 <b>(+30.01%)</b></td><td>123.10 (-11.69%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>507.40 (n/a)</td><td>349.22 (n/a)</td><td>324.50 (n/a)</td><td>189.60 (n/a)</td><td>139.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-6.40%)</td><td>0.06 (-2.74%)</td><td>0.06 (-3.75%)</td><td>0.03 <b>(-23.29%)</b></td><td>0.01 (+15.62%)</td><td>510.50 <b>(+30.36%)</b></td><td>314.36 (+6.50%)</td><td>282.40 (+3.90%)</td><td>238.50 (+6.85%)</td><td>112.21 <b>(+64.77%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>391.60 (n/a)</td><td>295.16 (n/a)</td><td>271.80 (n/a)</td><td>223.20 (n/a)</td><td>68.11 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+9.43%)</td><td>0.05 (+17.34%)</td><td>0.04 (+10.37%)</td><td>0.03 <b>(+113.90%)</b></td><td>0.02 (-11.14%)</td><td>488.70 <b>(-53.25%)</b></td><td>387.82 <b>(-25.91%)</b></td><td>438.20 (-9.39%)</td><td>223.50 (-8.63%)</td><td>117.03 <b>(-62.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1045.40 (n/a)</td><td>523.44 (n/a)</td><td>483.60 (n/a)</td><td>244.60 (n/a)</td><td>310.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+1.67%)</td><td>0.05 (+17.54%)</td><td>0.04 (+13.77%)</td><td>0.03 (-5.91%)</td><td>0.02 (+16.77%)</td><td>580.50 (+6.28%)</td><td>393.44 (-11.18%)</td><td>432.30 (-12.10%)</td><td>219.50 (-1.66%)</td><td>157.55 <b>(+24.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>546.20 (n/a)</td><td>442.94 (n/a)</td><td>491.80 (n/a)</td><td>223.20 (n/a)</td><td>126.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-2.38%)</td><td>0.05 (+5.23%)</td><td>0.05 <b>(+34.53%)</b></td><td>0.03 (-8.38%)</td><td>0.02 (+6.25%)</td><td>573.10 (+9.16%)</td><td>389.06 (-2.16%)</td><td>351.80 <b>(-25.67%)</b></td><td>224.30 (+2.47%)</td><td>167.25 (+18.76%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.00 (n/a)</td><td>397.66 (n/a)</td><td>473.30 (n/a)</td><td>218.90 (n/a)</td><td>140.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 <b>(-20.10%)</b></td><td>0.05 (-8.66%)</td><td>0.04 (-17.08%)</td><td>0.03 <b>(+48.83%)</b></td><td>0.02 <b>(-33.70%)</b></td><td>545.90 <b>(-32.81%)</b></td><td>395.60 (-4.23%)</td><td>419.40 <b>(+20.59%)</b></td><td>233.40 <b>(+25.15%)</b></td><td>127.86 <b>(-46.66%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>812.50 (n/a)</td><td>413.08 (n/a)</td><td>347.80 (n/a)</td><td>186.50 (n/a)</td><td>239.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+3.79%)</td><td>0.05 (+7.76%)</td><td>0.05 <b>(+38.13%)</b></td><td>0.03 (+1.88%)</td><td>0.02 (-17.56%)</td><td>599.70 (-1.85%)</td><td>360.22 (-10.44%)</td><td>321.40 <b>(-27.61%)</b></td><td>233.60 (-3.63%)</td><td>142.44 (-10.26%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.00 (n/a)</td><td>402.22 (n/a)</td><td>444.00 (n/a)</td><td>242.40 (n/a)</td><td>158.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(-36.58%)</b></td><td>0.03 (-18.65%)</td><td>0.03 (-11.70%)</td><td>0.02 <b>(+211.11%)</b></td><td>0.00 <b>(-75.82%)</b></td><td>666.90 <b>(-67.86%)</b></td><td>525.18 <b>(-25.58%)</b></td><td>487.60 (+13.24%)</td><td>441.80 <b>(+57.67%)</b></td><td>87.83 <b>(-88.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2074.80 (n/a)</td><td>705.72 (n/a)</td><td>430.60 (n/a)</td><td>280.20 (n/a)</td><td>768.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+11.29%)</td><td>0.04 (+4.60%)</td><td>0.03 (+5.99%)</td><td>0.02 (-17.01%)</td><td>0.02 <b>(+29.84%)</b></td><td>751.10 <b>(+20.48%)</b></td><td>497.92 (+1.60%)</td><td>488.20 (-5.64%)</td><td>246.80 (-10.16%)</td><td>189.50 <b>(+46.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>623.40 (n/a)</td><td>490.08 (n/a)</td><td>517.40 (n/a)</td><td>274.70 (n/a)</td><td>128.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+18.64%)</td><td>0.05 (+15.88%)</td><td>0.05 <b>(+32.00%)</b></td><td>0.04 <b>(+21.83%)</b></td><td>0.01 (+14.61%)</td><td>443.10 (-17.91%)</td><td>335.74 (-13.74%)</td><td>298.90 <b>(-24.25%)</b></td><td>244.40 (-15.72%)</td><td>89.40 (-14.11%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>389.22 (n/a)</td><td>394.60 (n/a)</td><td>290.00 (n/a)</td><td>104.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (-12.24%)</td><td>0.04 (-4.48%)</td><td>0.04 <b>(+39.27%)</b></td><td>0.01 <b>(-42.25%)</b></td><td>0.02 (+5.01%)</td><td>1316.20 <b>(+73.16%)</b></td><td>594.60 <b>(+20.90%)</b></td><td>377.30 <b>(-28.20%)</b></td><td>306.10 (+13.96%)</td><td>418.78 <b>(+121.53%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>760.10 (n/a)</td><td>491.82 (n/a)</td><td>525.50 (n/a)</td><td>268.60 (n/a)</td><td>189.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (-18.46%)</td><td>0.04 (-11.55%)</td><td>0.03 (+12.96%)</td><td>0.03 (+4.85%)</td><td>0.01 <b>(-43.92%)</b></td><td>624.00 (-4.63%)</td><td>454.42 (+1.10%)</td><td>476.60 (-11.48%)</td><td>291.80 <b>(+22.66%)</b></td><td>134.65 <b>(-30.87%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>654.30 (n/a)</td><td>449.48 (n/a)</td><td>538.40 (n/a)</td><td>237.90 (n/a)</td><td>194.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 <b>(-46.64%)</b></td><td>0.06 <b>(-36.51%)</b></td><td>0.07 (-13.31%)</td><td>0.02 <b>(-63.29%)</b></td><td>0.02 <b>(-40.97%)</b></td><td>2073.30 <b>(+172.41%)</b></td><td>814.08 <b>(+83.35%)</b></td><td>466.50 (+15.36%)</td><td>431.10 <b>(+87.35%)</b></td><td>708.70 <b>(+223.28%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>761.10 (n/a)</td><td>444.00 (n/a)</td><td>404.40 (n/a)</td><td>230.10 (n/a)</td><td>219.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-2.16%)</td><td>0.09 (-13.49%)</td><td>0.10 <b>(-21.11%)</b></td><td>0.07 <b>(+37.98%)</b></td><td>0.03 <b>(-21.54%)</b></td><td>504.10 <b>(-27.53%)</b></td><td>380.08 (+7.06%)</td><td>339.10 <b>(+26.77%)</b></td><td>257.20 (+2.23%)</td><td>112.88 <b>(-40.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>695.60 (n/a)</td><td>355.02 (n/a)</td><td>267.50 (n/a)</td><td>251.60 (n/a)</td><td>191.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-1.65%)</td><td>0.10 (+17.57%)</td><td>0.11 <b>(+56.27%)</b></td><td>0.07 <b>(+36.08%)</b></td><td>0.02 <b>(-37.48%)</b></td><td>443.10 <b>(-26.51%)</b></td><td>326.62 <b>(-21.25%)</b></td><td>299.30 <b>(-36.01%)</b></td><td>249.80 (+1.67%)</td><td>73.67 <b>(-50.30%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>602.90 (n/a)</td><td>414.78 (n/a)</td><td>467.70 (n/a)</td><td>245.70 (n/a)</td><td>148.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (+16.55%)</td><td>0.09 (+0.53%)</td><td>0.07 (-19.81%)</td><td>0.06 (-0.26%)</td><td>0.04 <b>(+42.43%)</b></td><td>539.80 (+0.26%)</td><td>409.62 (+6.22%)</td><td>493.60 <b>(+24.68%)</b></td><td>204.20 (-14.20%)</td><td>153.12 <b>(+29.00%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>538.40 (n/a)</td><td>385.64 (n/a)</td><td>395.90 (n/a)</td><td>238.00 (n/a)</td><td>118.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (-3.64%)</td><td>0.10 (+9.41%)</td><td>0.10 <b>(+29.77%)</b></td><td>0.07 <b>(+28.65%)</b></td><td>0.02 <b>(-36.70%)</b></td><td>494.50 <b>(-22.27%)</b></td><td>357.22 (-14.28%)</td><td>342.60 <b>(-22.94%)</b></td><td>282.20 (+3.75%)</td><td>83.03 <b>(-44.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>636.20 (n/a)</td><td>416.72 (n/a)</td><td>444.60 (n/a)</td><td>272.00 (n/a)</td><td>149.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-9.26%)</td><td>0.10 (+5.86%)</td><td>0.11 <b>(+42.17%)</b></td><td>0.05 <b>(-25.37%)</b></td><td>0.03 (-1.99%)</td><td>649.10 <b>(+34.00%)</b></td><td>385.48 (-2.09%)</td><td>302.50 <b>(-29.67%)</b></td><td>244.90 (+10.22%)</td><td>162.25 <b>(+52.68%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>484.40 (n/a)</td><td>393.70 (n/a)</td><td>430.10 (n/a)</td><td>222.20 (n/a)</td><td>106.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 <b>(-22.17%)</b></td><td>0.09 (-0.79%)</td><td>0.07 (+1.36%)</td><td>0.07 (+4.82%)</td><td>0.02 <b>(-28.79%)</b></td><td>487.80 (-4.61%)</td><td>403.24 (-2.42%)</td><td>464.20 (-1.34%)</td><td>290.90 <b>(+28.43%)</b></td><td>102.32 (-12.75%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>511.40 (n/a)</td><td>413.22 (n/a)</td><td>470.50 (n/a)</td><td>226.50 (n/a)</td><td>117.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-19.75%)</td><td>0.10 (-14.45%)</td><td>0.11 (+1.63%)</td><td>0.06 <b>(-21.39%)</b></td><td>0.03 (-18.47%)</td><td>562.30 <b>(+27.22%)</b></td><td>378.16 (+17.33%)</td><td>295.60 (-1.63%)</td><td>247.50 <b>(+24.62%)</b></td><td>140.89 <b>(+26.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>442.00 (n/a)</td><td>322.30 (n/a)</td><td>300.50 (n/a)</td><td>198.60 (n/a)</td><td>111.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (-3.49%)</td><td>0.07 (-17.89%)</td><td>0.06 (-16.23%)</td><td>0.05 (-4.20%)</td><td>0.02 (-14.11%)</td><td>597.70 (+4.38%)</td><td>505.70 (+19.94%)</td><td>533.80 (+19.36%)</td><td>293.80 (+3.63%)</td><td>123.50 (-5.67%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.60 (n/a)</td><td>421.64 (n/a)</td><td>447.20 (n/a)</td><td>283.50 (n/a)</td><td>130.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (+3.76%)</td><td>0.09 (+13.67%)</td><td>0.07 (+16.62%)</td><td>0.07 <b>(+30.91%)</b></td><td>0.03 (-17.25%)</td><td>497.70 <b>(-23.62%)</b></td><td>394.32 (-17.12%)</td><td>446.40 (-14.25%)</td><td>273.60 (-3.63%)</td><td>105.99 <b>(-39.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>651.60 (n/a)</td><td>475.78 (n/a)</td><td>520.60 (n/a)</td><td>283.90 (n/a)</td><td>174.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 <b>(+22.49%)</b></td><td>0.08 (-0.13%)</td><td>0.07 (+4.95%)</td><td>0.05 (-4.13%)</td><td>0.03 <b>(+26.99%)</b></td><td>643.00 (+4.32%)</td><td>465.84 (+2.19%)</td><td>471.40 (-4.71%)</td><td>271.10 (-18.37%)</td><td>134.26 (+9.79%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>616.40 (n/a)</td><td>455.84 (n/a)</td><td>494.70 (n/a)</td><td>332.10 (n/a)</td><td>122.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (-5.10%)</td><td>0.07 (-13.14%)</td><td>0.05 <b>(-21.32%)</b></td><td>0.04 <b>(-25.47%)</b></td><td>0.03 (+13.27%)</td><td>773.00 <b>(+34.15%)</b></td><td>549.78 <b>(+20.84%)</b></td><td>602.60 <b>(+27.10%)</b></td><td>287.50 (+5.39%)</td><td>180.83 <b>(+63.09%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>576.20 (n/a)</td><td>454.98 (n/a)</td><td>474.10 (n/a)</td><td>272.80 (n/a)</td><td>110.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 <b>(+21.50%)</b></td><td>0.08 <b>(+70.17%)</b></td><td>0.09 <b>(+72.72%)</b></td><td>0.05 <b>(+317.86%)</b></td><td>0.02 (-19.53%)</td><td>501.20 <b>(-76.07%)</b></td><td>318.02 <b>(-59.23%)</b></td><td>275.70 <b>(-42.10%)</b></td><td>249.80 (-17.69%)</td><td>105.26 <b>(-85.82%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2094.50 (n/a)</td><td>780.10 (n/a)</td><td>476.20 (n/a)</td><td>303.50 (n/a)</td><td>742.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.22 (+9.35%)</td><td>0.18 <b>(+23.87%)</b></td><td>0.18 (+10.00%)</td><td>0.16 <b>(+67.24%)</b></td><td>0.02 <b>(-58.13%)</b></td><td>299.40 <b>(-40.20%)</b></td><td>268.30 <b>(-25.05%)</b></td><td>269.40 (-9.11%)</td><td>228.50 (-8.56%)</td><td>25.73 <b>(-78.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>500.70 (n/a)</td><td>357.96 (n/a)</td><td>296.40 (n/a)</td><td>249.90 (n/a)</td><td>117.74 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.07 (-1.91%)</td><td>3.16 (-7.88%)</td><td>2.91 (-19.21%)</td><td>2.65 (+0.67%)</td><td>0.61 (-18.49%)</td><td>3951.50 (-0.67%)</td><td>3407.64 (+7.13%)</td><td>3597.60 <b>(+23.77%)</b></td><td>2577.40 (+1.94%)</td><td>607.54 (-17.09%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.15 (n/a)</td><td>3.44 (n/a)</td><td>3.61 (n/a)</td><td>2.64 (n/a)</td><td>0.75 (n/a)</td><td>3978.00 (n/a)</td><td>3180.70 (n/a)</td><td>2906.60 (n/a)</td><td>2528.30 (n/a)</td><td>732.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (+4.80%)</td><td>0.12 (-11.74%)</td><td>0.16 (+2.79%)</td><td>0.02 <b>(-66.34%)</b></td><td>0.07 <b>(+58.84%)</b></td><td>1882.70 <b>(+197.14%)</b></td><td>617.64 <b>(+83.66%)</b></td><td>255.00 (-2.71%)</td><td>239.10 (-4.59%)</td><td>713.75 <b>(+328.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>633.60 (n/a)</td><td>336.30 (n/a)</td><td>262.10 (n/a)</td><td>250.60 (n/a)</td><td>166.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-7.70%)</td><td>0.02 (-4.83%)</td><td>0.02 (-7.17%)</td><td>0.01 <b>(+30.42%)</b></td><td>0.00 <b>(-37.52%)</b></td><td>411.60 <b>(-23.31%)</b></td><td>316.16 (-0.79%)</td><td>299.30 (+7.74%)</td><td>259.20 (+8.36%)</td><td>60.65 <b>(-50.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.70 (n/a)</td><td>318.68 (n/a)</td><td>277.80 (n/a)</td><td>239.20 (n/a)</td><td>123.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+21.30%)</b></td><td>0.02 <b>(+24.09%)</b></td><td>0.02 <b>(+36.06%)</b></td><td>0.01 (-11.39%)</td><td>0.00 <b>(+31.31%)</b></td><td>533.50 (+12.84%)</td><td>294.14 (-15.65%)</td><td>231.20 <b>(-26.51%)</b></td><td>209.80 (-17.56%)</td><td>135.51 <b>(+29.78%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.80 (n/a)</td><td>348.70 (n/a)</td><td>314.60 (n/a)</td><td>254.50 (n/a)</td><td>104.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+30.62%)</b></td><td>0.02 <b>(+28.99%)</b></td><td>0.02 <b>(+38.26%)</b></td><td>0.01 (-4.67%)</td><td>0.01 <b>(+36.88%)</b></td><td>597.50 (+4.90%)</td><td>327.16 (-18.81%)</td><td>271.00 <b>(-27.68%)</b></td><td>205.60 <b>(-23.43%)</b></td><td>156.32 (+17.64%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.60 (n/a)</td><td>402.96 (n/a)</td><td>374.70 (n/a)</td><td>268.50 (n/a)</td><td>132.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-15.13%)</td><td>0.01 (-18.19%)</td><td>0.01 <b>(-32.85%)</b></td><td>0.01 <b>(-22.40%)</b></td><td>0.00 (+14.67%)</td><td>550.70 <b>(+28.88%)</b></td><td>426.78 <b>(+28.79%)</b></td><td>491.90 <b>(+48.93%)</b></td><td>261.50 (+17.85%)</td><td>141.25 <b>(+76.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>427.30 (n/a)</td><td>331.38 (n/a)</td><td>330.30 (n/a)</td><td>221.90 (n/a)</td><td>79.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+55.42%)</b></td><td>0.01 <b>(+32.53%)</b></td><td>0.01 (+19.97%)</td><td>0.01 (-1.55%)</td><td>0.01 <b>(+170.80%)</b></td><td>585.50 (+1.56%)</td><td>391.72 (-17.55%)</td><td>417.60 (-16.65%)</td><td>244.60 <b>(-35.67%)</b></td><td>144.54 <b>(+69.19%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.50 (n/a)</td><td>475.10 (n/a)</td><td>501.00 (n/a)</td><td>380.20 (n/a)</td><td>85.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-7.61%)</td><td>0.01 (-19.42%)</td><td>0.01 <b>(-41.94%)</b></td><td>0.01 <b>(+224.75%)</b></td><td>0.00 <b>(-28.53%)</b></td><td>613.40 <b>(-69.21%)</b></td><td>432.20 <b>(-27.98%)</b></td><td>472.80 <b>(+72.24%)</b></td><td>235.40 (+8.23%)</td><td>167.83 <b>(-78.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1992.10 (n/a)</td><td>600.10 (n/a)</td><td>274.50 (n/a)</td><td>217.50 (n/a)</td><td>778.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+49.56%)</b></td><td>0.02 <b>(+45.28%)</b></td><td>0.02 <b>(+84.57%)</b></td><td>0.01 (-9.20%)</td><td>0.01 <b>(+99.47%)</b></td><td>650.60 (+10.14%)</td><td>352.64 <b>(-21.48%)</b></td><td>253.10 <b>(-45.81%)</b></td><td>179.50 <b>(-33.12%)</b></td><td>189.82 <b>(+59.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.70 (n/a)</td><td>449.08 (n/a)</td><td>467.10 (n/a)</td><td>268.40 (n/a)</td><td>118.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+8.16%)</td><td>0.01 (+13.45%)</td><td>0.01 (+16.06%)</td><td>0.01 <b>(+69.68%)</b></td><td>0.00 (-9.21%)</td><td>609.90 <b>(-41.07%)</b></td><td>459.72 <b>(-20.12%)</b></td><td>464.80 (-13.83%)</td><td>253.00 (-7.53%)</td><td>132.58 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1034.90 (n/a)</td><td>575.54 (n/a)</td><td>539.40 (n/a)</td><td>273.60 (n/a)</td><td>286.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-1.70%)</td><td>0.01 <b>(+24.19%)</b></td><td>0.01 <b>(+38.14%)</b></td><td>0.01 <b>(+39.29%)</b></td><td>0.00 <b>(-40.84%)</b></td><td>425.00 <b>(-28.21%)</b></td><td>335.96 <b>(-25.06%)</b></td><td>332.60 <b>(-27.60%)</b></td><td>259.60 (+1.72%)</td><td>60.27 <b>(-57.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.00 (n/a)</td><td>448.28 (n/a)</td><td>459.40 (n/a)</td><td>255.20 (n/a)</td><td>142.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (+3.09%)</td><td>0.01 (-3.11%)</td><td>0.01 <b>(-21.20%)</b></td><td>0.01 <b>(-24.26%)</b></td><td>0.00 <b>(+53.07%)</b></td><td>624.80 <b>(+32.04%)</b></td><td>423.38 (+11.47%)</td><td>482.10 <b>(+26.90%)</b></td><td>255.20 (-3.00%)</td><td>158.38 <b>(+79.13%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.20 (n/a)</td><td>379.80 (n/a)</td><td>379.90 (n/a)</td><td>263.10 (n/a)</td><td>88.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+32.38%)</b></td><td>0.01 (+11.75%)</td><td>0.01 (-4.71%)</td><td>0.01 (-8.67%)</td><td>0.00 <b>(+125.06%)</b></td><td>596.80 (+9.48%)</td><td>437.18 (-1.39%)</td><td>492.10 (+4.93%)</td><td>258.90 <b>(-24.45%)</b></td><td>161.89 <b>(+84.65%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.10 (n/a)</td><td>443.36 (n/a)</td><td>469.00 (n/a)</td><td>342.70 (n/a)</td><td>87.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (+1.46%)</td><td>0.01 (-0.00%)</td><td>0.01 (+11.73%)</td><td>0.01 (+16.30%)</td><td>0.00 (-5.45%)</td><td>532.20 (-14.02%)</td><td>401.58 (-1.37%)</td><td>349.00 (-10.49%)</td><td>304.70 (-1.42%)</td><td>99.27 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.00 (n/a)</td><td>407.14 (n/a)</td><td>389.90 (n/a)</td><td>309.10 (n/a)</td><td>124.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-12.40%)</td><td>0.03 (-14.07%)</td><td>0.02 (-19.59%)</td><td>0.02 (-14.38%)</td><td>0.01 (-6.06%)</td><td>502.90 (+16.79%)</td><td>343.82 (+17.18%)</td><td>344.00 <b>(+24.37%)</b></td><td>248.20 (+14.17%)</td><td>99.18 <b>(+21.23%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>430.60 (n/a)</td><td>293.40 (n/a)</td><td>276.60 (n/a)</td><td>217.40 (n/a)</td><td>81.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (+10.77%)</td><td>0.03 (-11.80%)</td><td>0.04 (-12.91%)</td><td>0.01 <b>(-74.79%)</b></td><td>0.02 <b>(+88.78%)</b></td><td>2009.20 <b>(+296.68%)</b></td><td>669.62 <b>(+95.43%)</b></td><td>314.90 (+14.80%)</td><td>236.00 (-9.72%)</td><td>758.69 <b>(+605.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.50 (n/a)</td><td>342.64 (n/a)</td><td>274.30 (n/a)</td><td>261.40 (n/a)</td><td>107.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(+109.83%)</b></td><td>0.02 <b>(+68.21%)</b></td><td>0.02 <b>(+20.56%)</b></td><td>0.02 <b>(+301.79%)</b></td><td>0.01 <b>(+45.80%)</b></td><td>528.60 <b>(-75.11%)</b></td><td>397.12 <b>(-52.81%)</b></td><td>437.70 (-17.04%)</td><td>240.70 <b>(-52.35%)</b></td><td>119.58 <b>(-83.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2124.00 (n/a)</td><td>841.60 (n/a)</td><td>527.60 (n/a)</td><td>505.10 (n/a)</td><td>716.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-4.34%)</td><td>0.03 (+3.22%)</td><td>0.02 (+0.29%)</td><td>0.01 <b>(-28.54%)</b></td><td>0.01 <b>(+21.63%)</b></td><td>711.00 <b>(+39.93%)</b></td><td>429.40 (+4.67%)</td><td>423.50 (-0.28%)</td><td>245.30 (+4.52%)</td><td>189.02 <b>(+79.76%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.10 (n/a)</td><td>410.26 (n/a)</td><td>424.70 (n/a)</td><td>234.70 (n/a)</td><td>105.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (-0.93%)</td><td>0.02 (+13.65%)</td><td>0.02 (+15.51%)</td><td>0.01 (+1.06%)</td><td>0.01 (+15.30%)</td><td>607.70 (-1.04%)</td><td>421.04 (-7.87%)</td><td>409.20 (-13.43%)</td><td>239.00 (+0.93%)</td><td>173.87 <b>(+26.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.10 (n/a)</td><td>457.00 (n/a)</td><td>472.70 (n/a)</td><td>236.80 (n/a)</td><td>137.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (-11.46%)</td><td>0.03 (-6.22%)</td><td>0.03 (+6.57%)</td><td>0.02 (-18.77%)</td><td>0.01 (+6.36%)</td><td>592.50 <b>(+23.10%)</b></td><td>418.58 (+9.64%)</td><td>391.40 (-6.16%)</td><td>288.50 (+12.92%)</td><td>131.14 <b>(+49.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.30 (n/a)</td><td>381.78 (n/a)</td><td>417.10 (n/a)</td><td>255.50 (n/a)</td><td>87.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(+31.47%)</b></td><td>0.03 <b>(+37.89%)</b></td><td>0.03 <b>(+68.27%)</b></td><td>0.01 (+7.82%)</td><td>0.01 <b>(+70.19%)</b></td><td>625.60 (-7.24%)</td><td>395.02 (-19.89%)</td><td>311.30 <b>(-40.58%)</b></td><td>215.90 <b>(-23.95%)</b></td><td>194.53 <b>(+27.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.40 (n/a)</td><td>493.10 (n/a)</td><td>523.90 (n/a)</td><td>283.90 (n/a)</td><td>152.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(-27.12%)</b></td><td>0.02 <b>(-20.23%)</b></td><td>0.02 (-14.22%)</td><td>0.02 (-6.20%)</td><td>0.00 <b>(-39.13%)</b></td><td>614.20 (+6.59%)</td><td>494.24 <b>(+21.78%)</b></td><td>494.70 (+16.59%)</td><td>360.00 <b>(+37.20%)</b></td><td>106.33 (-9.02%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.20 (n/a)</td><td>405.84 (n/a)</td><td>424.30 (n/a)</td><td>262.40 (n/a)</td><td>116.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 <b>(+54.72%)</b></td><td>0.03 (+16.05%)</td><td>0.03 (+18.81%)</td><td>0.00 <b>(-73.23%)</b></td><td>0.02 <b>(+172.10%)</b></td><td>2006.10 <b>(+273.58%)</b></td><td>627.62 <b>(+63.20%)</b></td><td>301.90 (-15.83%)</td><td>178.80 <b>(-35.36%)</b></td><td>775.08 <b>(+645.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.00 (n/a)</td><td>384.58 (n/a)</td><td>358.70 (n/a)</td><td>276.60 (n/a)</td><td>103.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 <b>(+46.79%)</b></td><td>0.03 <b>(+32.42%)</b></td><td>0.02 (+2.97%)</td><td>0.01 <b>(+28.15%)</b></td><td>0.02 <b>(+79.54%)</b></td><td>623.60 <b>(-21.96%)</b></td><td>374.62 (-16.39%)</td><td>401.40 (-2.88%)</td><td>156.80 <b>(-31.89%)</b></td><td>195.79 (-9.45%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>799.10 (n/a)</td><td>448.06 (n/a)</td><td>413.30 (n/a)</td><td>230.20 (n/a)</td><td>216.22 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 <b>(-24.01%)</b></td><td>0.02 (-16.19%)</td><td>0.02 (-13.18%)</td><td>0.01 <b>(-22.30%)</b></td><td>0.01 <b>(-22.55%)</b></td><td>601.30 <b>(+28.70%)</b></td><td>433.36 (+19.30%)</td><td>414.70 (+15.19%)</td><td>306.10 <b>(+31.60%)</b></td><td>123.30 <b>(+28.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.20 (n/a)</td><td>363.24 (n/a)</td><td>360.00 (n/a)</td><td>232.60 (n/a)</td><td>96.27 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+16.96%)</td><td>0.05 (+6.32%)</td><td>0.05 (-1.55%)</td><td>0.03 (+7.74%)</td><td>0.02 (+16.09%)</td><td>530.70 (-7.19%)</td><td>372.26 (-4.94%)</td><td>342.30 (+1.57%)</td><td>211.80 (-14.49%)</td><td>146.00 (-4.64%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.80 (n/a)</td><td>391.62 (n/a)</td><td>337.00 (n/a)</td><td>247.70 (n/a)</td><td>153.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (-1.61%)</td><td>0.08 (-4.94%)</td><td>0.09 (+0.00%)</td><td>0.04 <b>(-25.14%)</b></td><td>0.04 <b>(+33.93%)</b></td><td>660.60 <b>(+33.59%)</b></td><td>366.38 (+17.73%)</td><td>282.70 (+0.00%)</td><td>198.20 (+1.64%)</td><td>195.64 <b>(+74.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>494.50 (n/a)</td><td>311.20 (n/a)</td><td>282.70 (n/a)</td><td>195.00 (n/a)</td><td>112.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+19.20%)</td><td>0.06 <b>(+25.97%)</b></td><td>0.06 <b>(+74.13%)</b></td><td>0.03 (+19.75%)</td><td>0.02 (+14.18%)</td><td>479.80 (-16.50%)</td><td>327.00 <b>(-20.78%)</b></td><td>268.80 <b>(-42.56%)</b></td><td>218.90 (-16.13%)</td><td>115.72 (-14.47%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.60 (n/a)</td><td>412.80 (n/a)</td><td>468.00 (n/a)</td><td>261.00 (n/a)</td><td>135.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (-14.34%)</td><td>0.06 (+12.24%)</td><td>0.07 <b>(+63.13%)</b></td><td>0.04 (-2.83%)</td><td>0.02 <b>(-24.51%)</b></td><td>533.50 (+2.91%)</td><td>360.46 (-14.34%)</td><td>294.60 <b>(-38.70%)</b></td><td>211.30 (+16.74%)</td><td>137.96 (-1.08%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>518.40 (n/a)</td><td>420.80 (n/a)</td><td>480.60 (n/a)</td><td>181.00 (n/a)</td><td>139.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+13.31%)</td><td>0.05 <b>(+37.87%)</b></td><td>0.06 <b>(+96.54%)</b></td><td>0.03 (+8.77%)</td><td>0.02 <b>(+20.45%)</b></td><td>583.20 (-8.07%)</td><td>368.06 <b>(-25.58%)</b></td><td>297.20 <b>(-49.13%)</b></td><td>212.10 (-11.74%)</td><td>166.32 (+0.01%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.40 (n/a)</td><td>494.58 (n/a)</td><td>584.20 (n/a)</td><td>240.30 (n/a)</td><td>166.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (-5.05%)</td><td>0.06 (-11.14%)</td><td>0.05 (-15.08%)</td><td>0.04 (+1.40%)</td><td>0.02 (-11.87%)</td><td>569.30 (-1.39%)</td><td>416.16 (+8.45%)</td><td>437.00 (+17.76%)</td><td>210.50 (+5.30%)</td><td>130.41 (-16.56%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>577.30 (n/a)</td><td>383.72 (n/a)</td><td>371.10 (n/a)</td><td>199.90 (n/a)</td><td>156.30 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-6.81%)</td><td>0.05 <b>(-23.20%)</b></td><td>0.04 <b>(-41.45%)</b></td><td>0.03 <b>(-29.33%)</b></td><td>0.02 <b>(+81.54%)</b></td><td>511.70 <b>(+41.51%)</b></td><td>389.10 <b>(+42.48%)</b></td><td>448.40 <b>(+70.82%)</b></td><td>241.40 (+7.29%)</td><td>135.80 <b>(+158.96%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>361.60 (n/a)</td><td>273.10 (n/a)</td><td>262.50 (n/a)</td><td>225.00 (n/a)</td><td>52.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 <b>(-22.45%)</b></td><td>0.04 (-11.22%)</td><td>0.04 (-11.52%)</td><td>0.03 (+4.75%)</td><td>0.01 <b>(-35.94%)</b></td><td>600.10 (-4.53%)</td><td>455.78 (+7.95%)</td><td>474.20 (+13.01%)</td><td>328.20 <b>(+28.96%)</b></td><td>109.26 <b>(-21.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.60 (n/a)</td><td>422.20 (n/a)</td><td>419.60 (n/a)</td><td>254.50 (n/a)</td><td>139.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (-12.88%)</td><td>0.05 (-9.48%)</td><td>0.04 <b>(-22.13%)</b></td><td>0.03 (+0.44%)</td><td>0.01 (-13.88%)</td><td>521.40 (-0.44%)</td><td>383.24 (+8.54%)</td><td>376.40 <b>(+28.42%)</b></td><td>257.30 (+14.76%)</td><td>121.64 (-5.51%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>523.70 (n/a)</td><td>353.10 (n/a)</td><td>293.10 (n/a)</td><td>224.20 (n/a)</td><td>128.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+19.23%)</td><td>0.05 (-0.01%)</td><td>0.03 (-19.22%)</td><td>0.03 (-8.51%)</td><td>0.02 <b>(+57.10%)</b></td><td>628.40 (+9.31%)</td><td>462.62 (+8.05%)</td><td>539.90 <b>(+23.80%)</b></td><td>231.20 (-16.14%)</td><td>168.50 <b>(+47.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>428.14 (n/a)</td><td>436.10 (n/a)</td><td>275.70 (n/a)</td><td>114.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 <b>(+25.19%)</b></td><td>0.04 (+9.71%)</td><td>0.05 (+13.73%)</td><td>0.03 (-1.85%)</td><td>0.02 <b>(+54.93%)</b></td><td>646.80 (+1.87%)</td><td>421.40 (-3.72%)</td><td>347.90 (-12.06%)</td><td>268.40 <b>(-20.14%)</b></td><td>163.07 <b>(+30.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>634.90 (n/a)</td><td>437.68 (n/a)</td><td>395.60 (n/a)</td><td>336.10 (n/a)</td><td>125.06 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (-4.75%)</td><td>0.11 (-7.87%)</td><td>0.12 (-0.13%)</td><td>0.06 <b>(-36.04%)</b></td><td>0.03 <b>(+78.63%)</b></td><td>535.30 <b>(+56.34%)</b></td><td>334.02 (+14.73%)</td><td>284.80 (+0.14%)</td><td>262.30 (+5.00%)</td><td>114.10 <b>(+204.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>342.40 (n/a)</td><td>291.14 (n/a)</td><td>284.40 (n/a)</td><td>249.80 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 <b>(-26.15%)</b></td><td>0.07 <b>(-35.52%)</b></td><td>0.08 <b>(-29.53%)</b></td><td>0.01 <b>(-83.34%)</b></td><td>0.04 (+1.04%)</td><td>2528.20 <b>(+500.24%)</b></td><td>833.90 <b>(+158.64%)</b></td><td>436.20 <b>(+41.90%)</b></td><td>240.60 <b>(+35.40%)</b></td><td>953.21 <b>(+832.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>421.20 (n/a)</td><td>322.42 (n/a)</td><td>307.40 (n/a)</td><td>177.70 (n/a)</td><td>102.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.19 (+4.64%)</td><td>0.12 (+7.17%)</td><td>0.10 (+6.52%)</td><td>0.06 <b>(-28.12%)</b></td><td>0.06 <b>(+36.40%)</b></td><td>685.20 <b>(+39.13%)</b></td><td>425.08 (+3.97%)</td><td>421.20 (-6.11%)</td><td>214.80 (-4.41%)</td><td>198.19 <b>(+82.21%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>492.50 (n/a)</td><td>408.86 (n/a)</td><td>448.60 (n/a)</td><td>224.70 (n/a)</td><td>108.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-1.66%)</td><td>0.09 (-4.97%)</td><td>0.08 <b>(-22.70%)</b></td><td>0.08 (-2.37%)</td><td>0.02 (+11.97%)</td><td>428.50 (+2.41%)</td><td>362.24 (+6.27%)</td><td>405.10 <b>(+29.38%)</b></td><td>260.50 (+1.68%)</td><td>80.25 (+14.82%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>418.40 (n/a)</td><td>340.86 (n/a)</td><td>313.10 (n/a)</td><td>256.20 (n/a)</td><td>69.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (-9.91%)</td><td>0.09 (-18.51%)</td><td>0.08 (-18.78%)</td><td>0.07 (-8.41%)</td><td>0.04 (-6.28%)</td><td>587.80 (+9.18%)</td><td>487.60 <b>(+23.42%)</b></td><td>541.90 <b>(+23.13%)</b></td><td>242.00 (+10.96%)</td><td>139.98 (+10.41%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>538.40 (n/a)</td><td>395.08 (n/a)</td><td>440.10 (n/a)</td><td>218.10 (n/a)</td><td>126.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 <b>(+22.52%)</b></td><td>0.11 <b>(+56.51%)</b></td><td>0.11 <b>(+84.97%)</b></td><td>0.07 <b>(+40.84%)</b></td><td>0.03 (+1.09%)</td><td>478.00 <b>(-29.00%)</b></td><td>313.54 <b>(-38.15%)</b></td><td>285.50 <b>(-45.93%)</b></td><td>215.80 (-18.38%)</td><td>99.14 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>673.20 (n/a)</td><td>506.94 (n/a)</td><td>528.00 (n/a)</td><td>264.40 (n/a)</td><td>149.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (+1.02%)</td><td>0.11 <b>(+21.09%)</b></td><td>0.10 <b>(+46.12%)</b></td><td>0.07 <b>(+395.77%)</b></td><td>0.03 <b>(-41.65%)</b></td><td>497.70 <b>(-79.83%)</b></td><td>374.90 <b>(-54.36%)</b></td><td>360.00 <b>(-31.56%)</b></td><td>229.80 (-0.99%)</td><td>99.94 <b>(-89.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.06 (n/a)</td><td>2467.30 (n/a)</td><td>821.34 (n/a)</td><td>526.00 (n/a)</td><td>232.10 (n/a)</td><td>932.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (-15.88%)</td><td>0.08 (+0.07%)</td><td>0.07 (+11.54%)</td><td>0.03 <b>(-37.54%)</b></td><td>0.03 (-13.35%)</td><td>1018.50 <b>(+60.12%)</b></td><td>522.86 (+6.19%)</td><td>463.80 (-10.34%)</td><td>276.30 (+18.89%)</td><td>290.52 <b>(+86.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>636.10 (n/a)</td><td>492.38 (n/a)</td><td>517.30 (n/a)</td><td>232.40 (n/a)</td><td>155.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 <b>(-34.52%)</b></td><td>0.08 <b>(-26.79%)</b></td><td>0.09 (-17.09%)</td><td>0.07 (-11.52%)</td><td>0.01 <b>(-59.25%)</b></td><td>552.70 (+13.00%)</td><td>449.60 <b>(+30.48%)</b></td><td>425.10 <b>(+20.60%)</b></td><td>363.90 <b>(+52.71%)</b></td><td>72.15 <b>(-27.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>489.10 (n/a)</td><td>344.58 (n/a)</td><td>352.50 (n/a)</td><td>238.30 (n/a)</td><td>99.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (-4.49%)</td><td>0.09 (-0.49%)</td><td>0.09 <b>(+25.25%)</b></td><td>0.06 (+13.30%)</td><td>0.04 (-17.07%)</td><td>574.40 (-11.74%)</td><td>403.04 (-4.71%)</td><td>351.70 <b>(-20.16%)</b></td><td>221.50 (+4.73%)</td><td>157.61 (-16.14%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>650.80 (n/a)</td><td>422.94 (n/a)</td><td>440.50 (n/a)</td><td>211.50 (n/a)</td><td>187.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+15.25%)</td><td>0.06 (+7.78%)</td><td>0.05 (-3.52%)</td><td>0.04 (+7.05%)</td><td>0.02 (+17.14%)</td><td>522.50 (-6.58%)</td><td>391.88 (-6.33%)</td><td>427.10 (+3.64%)</td><td>241.60 (-13.22%)</td><td>130.66 (-5.55%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.30 (n/a)</td><td>418.36 (n/a)</td><td>412.10 (n/a)</td><td>278.40 (n/a)</td><td>138.34 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (-6.15%)</td><td>0.06 (-8.29%)</td><td>0.05 <b>(-24.79%)</b></td><td>0.04 (+0.73%)</td><td>0.02 (-15.03%)</td><td>522.40 (-0.72%)</td><td>392.98 (+5.38%)</td><td>411.50 <b>(+32.96%)</b></td><td>231.10 (+6.55%)</td><td>113.30 (-18.62%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>526.20 (n/a)</td><td>372.90 (n/a)</td><td>309.50 (n/a)</td><td>216.90 (n/a)</td><td>139.21 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-13.66%)</td><td>0.05 (-5.43%)</td><td>0.05 <b>(+28.40%)</b></td><td>0.01 <b>(-73.25%)</b></td><td>0.03 <b>(+23.06%)</b></td><td>1997.40 <b>(+273.83%)</b></td><td>673.00 <b>(+61.45%)</b></td><td>383.50 <b>(-22.12%)</b></td><td>282.20 (+15.80%)</td><td>742.66 <b>(+456.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>534.30 (n/a)</td><td>416.84 (n/a)</td><td>492.40 (n/a)</td><td>243.70 (n/a)</td><td>133.56 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (-10.54%)</td><td>0.05 (-10.96%)</td><td>0.07 (+5.03%)</td><td>0.01 <b>(-72.79%)</b></td><td>0.03 <b>(+43.91%)</b></td><td>1919.30 <b>(+267.47%)</b></td><td>663.02 <b>(+79.91%)</b></td><td>282.50 (-4.79%)</td><td>256.50 (+11.81%)</td><td>716.04 <b>(+434.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>522.30 (n/a)</td><td>368.52 (n/a)</td><td>296.70 (n/a)</td><td>229.40 (n/a)</td><td>133.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 <b>(+29.46%)</b></td><td>0.06 (+17.57%)</td><td>0.05 (-1.18%)</td><td>0.04 <b>(+20.35%)</b></td><td>0.02 <b>(+44.75%)</b></td><td>531.60 (-16.90%)</td><td>391.90 (-12.82%)</td><td>444.20 (+1.18%)</td><td>247.80 <b>(-22.76%)</b></td><td>126.36 (-6.38%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>639.70 (n/a)</td><td>449.52 (n/a)</td><td>439.00 (n/a)</td><td>320.80 (n/a)</td><td>134.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 <b>(-30.57%)</b></td><td>0.06 (+12.98%)</td><td>0.07 <b>(+43.78%)</b></td><td>0.04 (+8.40%)</td><td>0.02 <b>(-51.54%)</b></td><td>563.20 (-7.75%)</td><td>356.18 <b>(-21.58%)</b></td><td>305.10 <b>(-30.44%)</b></td><td>263.60 <b>(+44.04%)</b></td><td>120.23 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>610.50 (n/a)</td><td>454.20 (n/a)</td><td>438.60 (n/a)</td><td>183.00 (n/a)</td><td>173.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (-0.75%)</td><td>0.08 (-1.11%)</td><td>0.08 (-0.76%)</td><td>0.06 (+2.58%)</td><td>0.01 (-13.23%)</td><td>398.40 (-2.52%)</td><td>304.70 (+0.32%)</td><td>291.30 (+0.76%)</td><td>246.10 (+0.78%)</td><td>56.87 (-12.92%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>408.70 (n/a)</td><td>303.72 (n/a)</td><td>289.10 (n/a)</td><td>244.20 (n/a)</td><td>65.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (+3.58%)</td><td>0.07 (-9.00%)</td><td>0.07 (-4.76%)</td><td>0.03 <b>(-25.81%)</b></td><td>0.03 <b>(+21.55%)</b></td><td>763.50 <b>(+34.77%)</b></td><td>462.68 <b>(+21.46%)</b></td><td>346.40 (+5.00%)</td><td>243.20 (-3.45%)</td><td>240.19 <b>(+67.56%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>566.50 (n/a)</td><td>380.92 (n/a)</td><td>329.90 (n/a)</td><td>251.90 (n/a)</td><td>143.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (+7.84%)</td><td>0.07 (+1.66%)</td><td>0.06 (-3.56%)</td><td>0.05 (+4.07%)</td><td>0.02 (+5.61%)</td><td>485.30 (-3.92%)</td><td>393.56 (-1.56%)</td><td>433.50 (+3.71%)</td><td>272.20 (-7.29%)</td><td>93.53 (-3.54%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>505.10 (n/a)</td><td>399.78 (n/a)</td><td>418.00 (n/a)</td><td>293.60 (n/a)</td><td>96.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (-13.35%)</td><td>0.06 (-7.42%)</td><td>0.06 (+4.19%)</td><td>0.04 (+0.36%)</td><td>0.02 <b>(-26.98%)</b></td><td>609.70 (-0.38%)</td><td>437.70 (+3.95%)</td><td>425.40 (-4.04%)</td><td>286.40 (+15.39%)</td><td>125.05 (-14.44%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>612.00 (n/a)</td><td>421.06 (n/a)</td><td>443.30 (n/a)</td><td>248.20 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 <b>(+55.28%)</b></td><td>0.08 (+5.23%)</td><td>0.08 (+7.60%)</td><td>0.02 <b>(-57.58%)</b></td><td>0.05 <b>(+167.81%)</b></td><td>1057.50 <b>(+135.73%)</b></td><td>440.00 <b>(+36.20%)</b></td><td>293.10 (-7.07%)</td><td>156.40 <b>(-35.58%)</b></td><td>361.43 <b>(+337.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>448.60 (n/a)</td><td>323.06 (n/a)</td><td>315.40 (n/a)</td><td>242.80 (n/a)</td><td>82.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 <b>(+22.81%)</b></td><td>0.07 (+4.50%)</td><td>0.06 (-15.71%)</td><td>0.04 (+10.11%)</td><td>0.02 <b>(+40.53%)</b></td><td>565.50 (-9.17%)</td><td>390.46 (-1.81%)</td><td>416.00 (+18.65%)</td><td>248.30 (-18.59%)</td><td>130.93 (-0.80%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>622.60 (n/a)</td><td>397.64 (n/a)</td><td>350.60 (n/a)</td><td>305.00 (n/a)</td><td>131.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 <b>(-56.98%)</b></td><td>0.03 <b>(-54.84%)</b></td><td>0.04 <b>(-48.07%)</b></td><td>0.01 <b>(-82.61%)</b></td><td>0.01 (-12.58%)</td><td>2068.30 <b>(+475.17%)</b></td><td>820.36 <b>(+194.14%)</b></td><td>519.90 <b>(+92.56%)</b></td><td>474.70 <b>(+132.47%)</b></td><td>698.02 <b>(+1148.35%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>359.60 (n/a)</td><td>278.90 (n/a)</td><td>270.00 (n/a)</td><td>204.20 (n/a)</td><td>55.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-1.44%)</td><td>0.06 <b>(+27.53%)</b></td><td>0.07 <b>(+67.92%)</b></td><td>0.05 <b>(+48.92%)</b></td><td>0.01 <b>(-56.25%)</b></td><td>351.60 <b>(-32.85%)</b></td><td>289.32 <b>(-27.32%)</b></td><td>277.90 <b>(-40.44%)</b></td><td>260.20 (+1.44%)</td><td>37.71 <b>(-69.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>523.60 (n/a)</td><td>398.08 (n/a)</td><td>466.60 (n/a)</td><td>256.50 (n/a)</td><td>122.96 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (-9.64%)</td><td>0.06 (+13.34%)</td><td>0.07 <b>(+48.09%)</b></td><td>0.04 <b>(+28.01%)</b></td><td>0.02 (-16.04%)</td><td>489.30 <b>(-21.87%)</b></td><td>340.68 (-15.29%)</td><td>267.60 <b>(-32.48%)</b></td><td>247.90 (+10.67%)</td><td>111.80 <b>(-26.84%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>626.30 (n/a)</td><td>402.18 (n/a)</td><td>396.30 (n/a)</td><td>224.00 (n/a)</td><td>152.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+3.62%)</td><td>0.05 (-3.32%)</td><td>0.04 (-9.29%)</td><td>0.02 <b>(-30.38%)</b></td><td>0.02 <b>(+46.62%)</b></td><td>756.10 <b>(+43.66%)</b></td><td>483.00 (+16.79%)</td><td>511.80 (+10.23%)</td><td>248.40 (-3.50%)</td><td>223.29 <b>(+88.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>526.30 (n/a)</td><td>413.58 (n/a)</td><td>464.30 (n/a)</td><td>257.40 (n/a)</td><td>118.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (+17.93%)</td><td>0.04 (+15.03%)</td><td>0.04 (+12.80%)</td><td>0.03 (+4.88%)</td><td>0.02 <b>(+20.93%)</b></td><td>649.70 (-4.65%)</td><td>471.90 (-12.18%)</td><td>506.20 (-11.35%)</td><td>233.60 (-15.21%)</td><td>155.15 (-8.42%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>681.40 (n/a)</td><td>537.34 (n/a)</td><td>571.00 (n/a)</td><td>275.50 (n/a)</td><td>169.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 <b>(-33.26%)</b></td><td>0.05 <b>(-33.74%)</b></td><td>0.06 (-14.64%)</td><td>0.02 <b>(-70.15%)</b></td><td>0.02 <b>(+27.38%)</b></td><td>1024.90 <b>(+235.04%)</b></td><td>468.06 <b>(+93.25%)</b></td><td>291.40 (+17.17%)</td><td>247.10 <b>(+49.85%)</b></td><td>330.30 <b>(+550.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>305.90 (n/a)</td><td>242.20 (n/a)</td><td>248.70 (n/a)</td><td>164.90 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.34 (-16.13%)</td><td>0.21 <b>(-38.50%)</b></td><td>0.21 <b>(-41.70%)</b></td><td>0.05 <b>(-75.21%)</b></td><td>0.10 <b>(+37.26%)</b></td><td>1880.70 <b>(+303.41%)</b></td><td>715.36 <b>(+130.79%)</b></td><td>473.80 <b>(+71.54%)</b></td><td>287.80 (+19.22%)</td><td>657.54 <b>(+626.14%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>466.20 (n/a)</td><td>309.96 (n/a)</td><td>276.20 (n/a)</td><td>241.40 (n/a)</td><td>90.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.36 (-4.57%)</td><td>0.31 (+18.90%)</td><td>0.34 <b>(+59.91%)</b></td><td>0.18 (+6.49%)</td><td>0.07 (-19.02%)</td><td>538.80 (-6.08%)</td><td>337.22 (-18.15%)</td><td>285.90 <b>(-37.45%)</b></td><td>274.70 (+4.77%)</td><td>113.39 (-14.76%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>573.70 (n/a)</td><td>411.98 (n/a)</td><td>457.10 (n/a)</td><td>262.20 (n/a)</td><td>133.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.33 (+5.19%)</td><td>0.21 (+7.72%)</td><td>0.18 (+6.42%)</td><td>0.16 <b>(+68.13%)</b></td><td>0.07 (-13.02%)</td><td>613.20 <b>(-40.52%)</b></td><td>502.96 (-14.51%)</td><td>540.80 (-6.03%)</td><td>297.10 (-4.93%)</td><td>126.10 <b>(-53.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>1031.00 (n/a)</td><td>588.30 (n/a)</td><td>575.50 (n/a)</td><td>312.50 (n/a)</td><td>270.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.29 (-7.44%)</td><td>0.20 (-5.27%)</td><td>0.16 (-7.72%)</td><td>0.14 (-13.16%)</td><td>0.08 (+12.13%)</td><td>541.40 (+15.14%)</td><td>404.14 (+9.20%)</td><td>450.30 (+8.38%)</td><td>256.30 (+8.05%)</td><td>136.78 <b>(+33.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>470.20 (n/a)</td><td>370.08 (n/a)</td><td>415.50 (n/a)</td><td>237.20 (n/a)</td><td>102.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.30 <b>(+23.36%)</b></td><td>0.20 (+7.12%)</td><td>0.16 (-1.93%)</td><td>0.13 (+5.91%)</td><td>0.07 <b>(+34.67%)</b></td><td>546.80 (-5.59%)</td><td>410.66 (-3.78%)</td><td>463.90 (+1.98%)</td><td>245.80 (-18.96%)</td><td>131.81 (+9.49%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>579.20 (n/a)</td><td>426.80 (n/a)</td><td>454.90 (n/a)</td><td>303.30 (n/a)</td><td>120.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.25 (-1.89%)</td><td>0.15 <b>(-20.10%)</b></td><td>0.20 (+17.04%)</td><td>0.04 <b>(-73.09%)</b></td><td>0.10 <b>(+137.09%)</b></td><td>1956.80 <b>(+271.66%)</b></td><td>963.82 <b>(+133.46%)</b></td><td>361.70 (-14.57%)</td><td>294.10 (+1.94%)</td><td>860.79 <b>(+905.08%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>526.50 (n/a)</td><td>412.84 (n/a)</td><td>423.40 (n/a)</td><td>288.50 (n/a)</td><td>85.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (-4.08%)</td><td>0.09 <b>(-23.81%)</b></td><td>0.08 <b>(-35.78%)</b></td><td>0.06 (-14.78%)</td><td>0.04 (+13.19%)</td><td>589.70 (+17.33%)</td><td>435.38 <b>(+36.84%)</b></td><td>435.20 <b>(+55.71%)</b></td><td>254.10 (+4.27%)</td><td>154.78 <b>(+43.80%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>502.60 (n/a)</td><td>318.16 (n/a)</td><td>279.50 (n/a)</td><td>243.70 (n/a)</td><td>107.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 <b>(+36.46%)</b></td><td>0.11 (+15.31%)</td><td>0.10 (+11.30%)</td><td>0.07 (-17.18%)</td><td>0.05 <b>(+99.44%)</b></td><td>547.70 <b>(+20.75%)</b></td><td>361.66 (-5.86%)</td><td>387.00 (-10.15%)</td><td>208.00 <b>(-26.71%)</b></td><td>135.25 <b>(+69.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>453.60 (n/a)</td><td>384.18 (n/a)</td><td>430.70 (n/a)</td><td>283.80 (n/a)</td><td>79.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (+17.51%)</td><td>0.09 (+3.84%)</td><td>0.08 (+3.34%)</td><td>0.07 <b>(+99.86%)</b></td><td>0.04 (-8.83%)</td><td>504.50 <b>(-49.97%)</b></td><td>432.94 (-15.76%)</td><td>473.70 (-3.23%)</td><td>225.50 (-14.87%)</td><td>117.20 <b>(-60.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1008.30 (n/a)</td><td>513.94 (n/a)</td><td>489.50 (n/a)</td><td>264.90 (n/a)</td><td>299.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (-2.03%)</td><td>0.11 (+10.28%)</td><td>0.12 <b>(+36.27%)</b></td><td>0.08 (+16.56%)</td><td>0.03 (-10.97%)</td><td>465.20 (-14.20%)</td><td>350.94 (-11.24%)</td><td>304.20 <b>(-26.63%)</b></td><td>245.30 (+2.04%)</td><td>102.37 (-16.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>542.20 (n/a)</td><td>395.36 (n/a)</td><td>414.60 (n/a)</td><td>240.40 (n/a)</td><td>123.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 <b>(-24.97%)</b></td><td>0.12 <b>(+30.36%)</b></td><td>0.15 <b>(+87.68%)</b></td><td>0.07 (+14.64%)</td><td>0.04 <b>(-38.08%)</b></td><td>552.80 (-12.78%)</td><td>329.90 <b>(-30.78%)</b></td><td>252.20 <b>(-46.71%)</b></td><td>248.00 <b>(+33.26%)</b></td><td>131.70 <b>(-27.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>633.80 (n/a)</td><td>476.58 (n/a)</td><td>473.30 (n/a)</td><td>186.10 (n/a)</td><td>180.72 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (-19.98%)</td><td>0.13 (+11.74%)</td><td>0.14 <b>(+26.83%)</b></td><td>0.07 (-4.25%)</td><td>0.03 <b>(-25.67%)</b></td><td>523.40 (+4.43%)</td><td>311.92 (-12.41%)</td><td>260.70 <b>(-21.14%)</b></td><td>242.30 <b>(+24.96%)</b></td><td>119.57 (+1.93%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>501.20 (n/a)</td><td>356.12 (n/a)</td><td>330.60 (n/a)</td><td>193.90 (n/a)</td><td>117.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 (+14.47%)</td><td>0.14 (+17.08%)</td><td>0.15 (+8.40%)</td><td>0.08 (-3.75%)</td><td>0.04 (+17.57%)</td><td>521.90 (+3.90%)</td><td>317.60 (-13.28%)</td><td>273.40 (-7.73%)</td><td>233.70 (-12.64%)</td><td>118.99 (+6.13%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>502.30 (n/a)</td><td>366.22 (n/a)</td><td>296.30 (n/a)</td><td>267.50 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (+11.57%)</td><td>0.11 (+4.85%)</td><td>0.09 (+0.02%)</td><td>0.08 <b>(+22.10%)</b></td><td>0.03 (-7.05%)</td><td>500.50 (-18.10%)</td><td>404.00 (-6.94%)</td><td>454.70 (-0.02%)</td><td>268.70 (-10.37%)</td><td>95.85 <b>(-27.80%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>611.10 (n/a)</td><td>434.14 (n/a)</td><td>454.80 (n/a)</td><td>299.80 (n/a)</td><td>132.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (-1.30%)</td><td>0.13 <b>(+26.10%)</b></td><td>0.16 <b>(+78.72%)</b></td><td>0.08 (+10.45%)</td><td>0.05 (+9.45%)</td><td>541.40 (-9.46%)</td><td>365.46 (-19.47%)</td><td>260.70 <b>(-44.04%)</b></td><td>242.90 (+1.34%)</td><td>152.12 (+1.16%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>598.00 (n/a)</td><td>453.80 (n/a)</td><td>465.90 (n/a)</td><td>239.70 (n/a)</td><td>150.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 <b>(+29.10%)</b></td><td>0.12 <b>(+33.79%)</b></td><td>0.14 <b>(+58.80%)</b></td><td>0.07 <b>(+226.83%)</b></td><td>0.05 (-2.40%)</td><td>596.00 <b>(-69.40%)</b></td><td>376.20 <b>(-46.47%)</b></td><td>293.10 <b>(-37.04%)</b></td><td>225.80 <b>(-22.54%)</b></td><td>158.75 <b>(-77.40%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1947.90 (n/a)</td><td>702.80 (n/a)</td><td>465.50 (n/a)</td><td>291.50 (n/a)</td><td>702.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-3.06%)</td><td>0.08 (-13.60%)</td><td>0.07 (-16.45%)</td><td>0.02 <b>(-71.79%)</b></td><td>0.04 <b>(+73.39%)</b></td><td>1922.70 <b>(+254.55%)</b></td><td>739.86 <b>(+66.31%)</b></td><td>548.10 (+19.70%)</td><td>304.00 (+3.16%)</td><td>670.22 <b>(+628.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>542.30 (n/a)</td><td>444.88 (n/a)</td><td>457.90 (n/a)</td><td>294.70 (n/a)</td><td>92.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (-15.98%)</td><td>0.10 (-3.81%)</td><td>0.08 (-4.16%)</td><td>0.06 <b>(-20.42%)</b></td><td>0.04 (-16.98%)</td><td>683.30 <b>(+25.65%)</b></td><td>471.20 (+4.34%)</td><td>512.30 (+4.34%)</td><td>254.70 (+19.02%)</td><td>172.43 <b>(+27.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>543.80 (n/a)</td><td>451.60 (n/a)</td><td>491.00 (n/a)</td><td>214.00 (n/a)</td><td>134.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 <b>(+45.18%)</b></td><td>0.11 <b>(+110.18%)</b></td><td>0.12 <b>(+82.76%)</b></td><td>0.07 <b>(+299.90%)</b></td><td>0.02 <b>(-28.03%)</b></td><td>498.10 <b>(-74.99%)</b></td><td>333.70 <b>(-68.45%)</b></td><td>292.90 <b>(-45.27%)</b></td><td>267.00 <b>(-31.10%)</b></td><td>93.68 <b>(-88.32%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1991.80 (n/a)</td><td>1057.68 (n/a)</td><td>535.20 (n/a)</td><td>387.50 (n/a)</td><td>801.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (+0.66%)</td><td>0.10 (-12.88%)</td><td>0.11 (-13.83%)</td><td>0.06 (-16.12%)</td><td>0.04 <b>(+25.00%)</b></td><td>612.10 (+19.20%)</td><td>390.42 <b>(+21.03%)</b></td><td>317.60 (+16.04%)</td><td>247.80 (-0.64%)</td><td>159.28 <b>(+44.83%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>513.50 (n/a)</td><td>322.58 (n/a)</td><td>273.70 (n/a)</td><td>249.40 (n/a)</td><td>109.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 <b>(+117.61%)</b></td><td>0.09 <b>(+71.22%)</b></td><td>0.09 <b>(+41.30%)</b></td><td>0.05 <b>(+48.95%)</b></td><td>0.04 <b>(+177.33%)</b></td><td>668.30 <b>(-32.86%)</b></td><td>414.34 <b>(-37.66%)</b></td><td>404.90 <b>(-29.23%)</b></td><td>246.20 <b>(-54.05%)</b></td><td>164.93 (-15.06%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>995.40 (n/a)</td><td>664.66 (n/a)</td><td>572.10 (n/a)</td><td>535.80 (n/a)</td><td>194.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (+16.51%)</td><td>0.13 <b>(+63.93%)</b></td><td>0.14 <b>(+59.49%)</b></td><td>0.11 <b>(+247.88%)</b></td><td>0.01 <b>(-69.64%)</b></td><td>319.40 <b>(-71.25%)</b></td><td>272.24 <b>(-53.20%)</b></td><td>256.30 <b>(-37.30%)</b></td><td>253.50 (-14.18%)</td><td>28.04 <b>(-92.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1111.00 (n/a)</td><td>581.66 (n/a)</td><td>408.80 (n/a)</td><td>295.40 (n/a)</td><td>357.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 <b>(-31.28%)</b></td><td>0.07 <b>(-24.97%)</b></td><td>0.08 <b>(+21.13%)</b></td><td>0.01 <b>(-72.90%)</b></td><td>0.05 (-7.99%)</td><td>2445.20 <b>(+268.92%)</b></td><td>1125.28 <b>(+142.74%)</b></td><td>430.60 (-17.45%)</td><td>264.70 <b>(+45.52%)</b></td><td>1073.84 <b>(+499.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>662.80 (n/a)</td><td>463.58 (n/a)</td><td>521.60 (n/a)</td><td>181.90 (n/a)</td><td>179.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 <b>(+24.70%)</b></td><td>0.11 <b>(+31.23%)</b></td><td>0.12 <b>(+59.13%)</b></td><td>0.07 <b>(+22.52%)</b></td><td>0.04 <b>(+38.59%)</b></td><td>509.30 (-18.38%)</td><td>353.12 <b>(-22.11%)</b></td><td>299.70 <b>(-37.17%)</b></td><td>242.20 (-19.80%)</td><td>127.20 (-6.80%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>624.00 (n/a)</td><td>453.34 (n/a)</td><td>477.00 (n/a)</td><td>302.00 (n/a)</td><td>136.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.44 <b>(+51.98%)</b></td><td>0.26 (+10.34%)</td><td>0.21 (-3.74%)</td><td>0.17 (-7.50%)</td><td>0.10 <b>(+186.95%)</b></td><td>751.30 (+8.12%)</td><td>563.50 (-1.87%)</td><td>611.60 (+3.89%)</td><td>300.10 <b>(-34.20%)</b></td><td>167.71 <b>(+92.90%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>694.90 (n/a)</td><td>574.24 (n/a)</td><td>588.70 (n/a)</td><td>456.10 (n/a)</td><td>86.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.51 <b>(+39.80%)</b></td><td>0.29 (+6.71%)</td><td>0.24 (-2.27%)</td><td>0.20 (-7.73%)</td><td>0.13 <b>(+115.62%)</b></td><td>644.10 (+8.38%)</td><td>500.66 (+0.69%)</td><td>537.20 (+2.32%)</td><td>255.30 <b>(-28.49%)</b></td><td>145.51 <b>(+56.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>594.30 (n/a)</td><td>497.22 (n/a)</td><td>525.00 (n/a)</td><td>357.00 (n/a)</td><td>92.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.26 <b>(-38.40%)</b></td><td>0.23 (-12.98%)</td><td>0.23 (-1.72%)</td><td>0.19 (-3.11%)</td><td>0.03 <b>(-64.69%)</b></td><td>684.90 (+3.21%)</td><td>580.10 (+8.58%)</td><td>574.00 (+1.74%)</td><td>494.70 <b>(+62.36%)</b></td><td>84.62 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>663.60 (n/a)</td><td>534.28 (n/a)</td><td>564.20 (n/a)</td><td>304.70 (n/a)</td><td>135.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+26.88%)</b></td><td>0.01 <b>(+21.89%)</b></td><td>0.01 (+8.75%)</td><td>0.01 <b>(+26.02%)</b></td><td>0.00 (+5.59%)</td><td>406.30 <b>(-20.64%)</b></td><td>294.66 (-18.95%)</td><td>280.10 (-8.04%)</td><td>232.60 <b>(-21.18%)</b></td><td>66.32 <b>(-29.85%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.00 (n/a)</td><td>363.56 (n/a)</td><td>304.60 (n/a)</td><td>295.10 (n/a)</td><td>94.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 <b>(-24.31%)</b></td><td>0.01 (-15.52%)</td><td>0.01 (-18.64%)</td><td>0.01 <b>(+24.38%)</b></td><td>0.00 <b>(-52.00%)</b></td><td>418.20 (-19.59%)</td><td>349.18 (+11.06%)</td><td>337.60 <b>(+22.90%)</b></td><td>294.30 <b>(+32.09%)</b></td><td>55.73 <b>(-52.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.10 (n/a)</td><td>314.40 (n/a)</td><td>274.70 (n/a)</td><td>222.80 (n/a)</td><td>117.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (-4.43%)</td><td>0.01 (-19.94%)</td><td>0.01 <b>(-42.27%)</b></td><td>0.01 (-17.73%)</td><td>0.00 (+9.16%)</td><td>641.20 <b>(+21.55%)</b></td><td>462.96 <b>(+28.78%)</b></td><td>526.00 <b>(+73.25%)</b></td><td>269.50 (+4.62%)</td><td>151.05 <b>(+34.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.50 (n/a)</td><td>359.50 (n/a)</td><td>303.60 (n/a)</td><td>257.60 (n/a)</td><td>111.95 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.31 (-7.73%)</td><td>6.46 (-17.25%)</td><td>7.72 (-0.13%)</td><td>4.17 <b>(-36.98%)</b></td><td>2.02 <b>(+115.13%)</b></td><td>503.80 <b>(+58.73%)</b></td><td>355.66 <b>(+30.88%)</b></td><td>271.80 (+0.11%)</td><td>252.40 (+8.37%)</td><td>124.72 <b>(+277.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>9.01 (n/a)</td><td>7.81 (n/a)</td><td>7.73 (n/a)</td><td>6.61 (n/a)</td><td>0.94 (n/a)</td><td>317.40 (n/a)</td><td>271.74 (n/a)</td><td>271.50 (n/a)</td><td>232.90 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.51 (-5.37%)</td><td>0.45 <b>(+35.51%)</b></td><td>0.46 <b>(+43.52%)</b></td><td>0.35 <b>(+129.48%)</b></td><td>0.06 <b>(-58.33%)</b></td><td>372.20 <b>(-56.43%)</b></td><td>299.92 <b>(-36.00%)</b></td><td>288.20 <b>(-30.34%)</b></td><td>261.30 (+5.70%)</td><td>42.68 <b>(-81.28%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>854.20 (n/a)</td><td>468.60 (n/a)</td><td>413.70 (n/a)</td><td>247.20 (n/a)</td><td>228.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.45 <b>(-32.77%)</b></td><td>0.34 (-13.63%)</td><td>0.33 (-2.41%)</td><td>0.21 (+0.39%)</td><td>0.09 <b>(-51.60%)</b></td><td>627.10 (-0.38%)</td><td>413.52 (+3.78%)</td><td>403.30 (+2.46%)</td><td>294.90 <b>(+48.71%)</b></td><td>130.08 <b>(-26.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.67 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>629.50 (n/a)</td><td>398.44 (n/a)</td><td>393.60 (n/a)</td><td>198.30 (n/a)</td><td>177.14 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.49 (+7.85%)</td><td>0.42 (+10.14%)</td><td>0.42 (+3.55%)</td><td>0.30 <b>(+28.11%)</b></td><td>0.08 (-13.42%)</td><td>446.60 <b>(-21.94%)</b></td><td>328.26 (-11.70%)</td><td>313.00 (-3.42%)</td><td>269.30 (-7.30%)</td><td>71.55 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>572.10 (n/a)</td><td>371.76 (n/a)</td><td>324.10 (n/a)</td><td>290.50 (n/a)</td><td>116.19 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.50 (-18.73%)</td><td>0.38 (+7.10%)</td><td>0.40 (-1.64%)</td><td>0.26 <b>(+267.37%)</b></td><td>0.10 <b>(-49.73%)</b></td><td>514.60 <b>(-72.78%)</b></td><td>367.64 <b>(-43.32%)</b></td><td>331.90 (+1.69%)</td><td>266.60 <b>(+23.03%)</b></td><td>106.08 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.61 (n/a)</td><td>0.36 (n/a)</td><td>0.40 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td><td>1890.30 (n/a)</td><td>648.64 (n/a)</td><td>326.40 (n/a)</td><td>216.70 (n/a)</td><td>702.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.53 <b>(-23.38%)</b></td><td>0.35 <b>(-34.59%)</b></td><td>0.28 <b>(-46.52%)</b></td><td>0.24 <b>(-40.69%)</b></td><td>0.13 <b>(+26.31%)</b></td><td>541.30 <b>(+68.63%)</b></td><td>419.20 <b>(+64.60%)</b></td><td>472.10 <b>(+86.97%)</b></td><td>248.00 <b>(+30.53%)</b></td><td>137.46 <b>(+189.54%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.70 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.10 (n/a)</td><td>321.00 (n/a)</td><td>254.68 (n/a)</td><td>252.50 (n/a)</td><td>190.00 (n/a)</td><td>47.48 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (-19.38%)</td><td>0.01 (-6.20%)</td><td>0.01 (-6.24%)</td><td>0.01 <b>(+36.36%)</b></td><td>0.00 <b>(-36.72%)</b></td><td>600.50 <b>(-26.67%)</b></td><td>390.24 (-7.00%)</td><td>316.80 (+6.63%)</td><td>282.30 <b>(+24.03%)</b></td><td>139.40 <b>(-43.79%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>818.90 (n/a)</td><td>419.62 (n/a)</td><td>297.10 (n/a)</td><td>227.60 (n/a)</td><td>247.98 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 <b>(+24.46%)</b></td><td>0.01 <b>(+24.40%)</b></td><td>0.01 <b>(+30.02%)</b></td><td>0.01 (-9.31%)</td><td>0.00 <b>(+74.85%)</b></td><td>531.20 (+10.25%)</td><td>348.56 (-15.44%)</td><td>326.50 <b>(-23.09%)</b></td><td>235.00 (-19.66%)</td><td>116.57 <b>(+61.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.80 (n/a)</td><td>412.20 (n/a)</td><td>424.50 (n/a)</td><td>292.50 (n/a)</td><td>72.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.00 (-14.29%)</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+150.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-10.98%)</td><td>19196.29 (-5.89%)</td><td>11766.76 <b>(-20.32%)</b></td><td>8775.94 <b>(-54.84%)</b></td><td>6475.98 (+10.19%)</td><td>6134.76 (-14.18%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20396.68 (n/a)</td><td>14766.60 (n/a)</td><td>19433.64 (n/a)</td><td>5876.91 (n/a)</td><td>7148.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.00 <b>(+33.33%)</b></td><td>0.00 (+11.11%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+63.54%)</b></td><td>22612.54 (+0.29%)</td><td>17356.01 (+0.44%)</td><td>17762.91 (+0.87%)</td><td>6600.71 <b>(-31.02%)</b></td><td>6531.73 <b>(+35.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22547.57 (n/a)</td><td>17280.07 (n/a)</td><td>17610.24 (n/a)</td><td>9569.62 (n/a)</td><td>4822.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (+9.26%)</td><td>0.10 (+13.04%)</td><td>0.08 (+10.04%)</td><td>0.07 (+1.69%)</td><td>0.03 <b>(+25.67%)</b></td><td>29138.95 (-1.68%)</td><td>22972.38 (-9.66%)</td><td>25189.19 (-9.05%)</td><td>15064.03 (-8.51%)</td><td>6218.14 (+17.23%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>29637.33 (n/a)</td><td>25428.51 (n/a)</td><td>27696.78 (n/a)</td><td>16465.11 (n/a)</td><td>5304.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.41 (-5.42%)</td><td>1.15 (-18.32%)</td><td>1.16 (-13.64%)</td><td>0.30 (-7.63%)</td><td>0.89 (+12.62%)</td><td>3489.30 (+8.26%)</td><td>1756.72 <b>(+48.62%)</b></td><td>905.50 (+15.79%)</td><td>435.50 (+5.73%)</td><td>1498.18 <b>(+30.09%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.55 (n/a)</td><td>1.41 (n/a)</td><td>1.34 (n/a)</td><td>0.33 (n/a)</td><td>0.79 (n/a)</td><td>3223.10 (n/a)</td><td>1182.00 (n/a)</td><td>782.00 (n/a)</td><td>411.90 (n/a)</td><td>1151.63 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.27 <b>(-32.10%)</b></td><td>2.00 (+3.84%)</td><td>2.53 <b>(+79.07%)</b></td><td>0.30 (-0.59%)</td><td>1.22 <b>(-28.63%)</b></td><td>3459.90 (+0.59%)</td><td>1094.16 (-5.66%)</td><td>414.70 <b>(-44.16%)</b></td><td>320.70 <b>(+47.25%)</b></td><td>1341.54 (+3.57%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.82 (n/a)</td><td>1.92 (n/a)</td><td>1.41 (n/a)</td><td>0.30 (n/a)</td><td>1.71 (n/a)</td><td>3439.50 (n/a)</td><td>1159.78 (n/a)</td><td>742.60 (n/a)</td><td>217.80 (n/a)</td><td>1295.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.87 (+6.97%)</td><td>1.96 (+8.85%)</td><td>1.90 (+9.91%)</td><td>1.31 <b>(+30.84%)</b></td><td>0.61 (+1.70%)</td><td>801.80 <b>(-23.57%)</b></td><td>577.42 (-10.39%)</td><td>550.80 (-9.02%)</td><td>365.70 (-6.52%)</td><td>171.35 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.68 (n/a)</td><td>1.80 (n/a)</td><td>1.73 (n/a)</td><td>1.00 (n/a)</td><td>0.60 (n/a)</td><td>1049.00 (n/a)</td><td>644.40 (n/a)</td><td>605.40 (n/a)</td><td>391.20 (n/a)</td><td>243.84 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.38 (-6.69%)</td><td>2.21 <b>(-23.85%)</b></td><td>1.70 <b>(-38.32%)</b></td><td>1.57 (-14.30%)</td><td>0.80 (+8.24%)</td><td>667.70 (+16.69%)</td><td>520.52 <b>(+35.49%)</b></td><td>617.50 <b>(+62.12%)</b></td><td>310.60 (+7.14%)</td><td>160.65 <b>(+39.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.62 (n/a)</td><td>2.90 (n/a)</td><td>2.75 (n/a)</td><td>1.83 (n/a)</td><td>0.74 (n/a)</td><td>572.20 (n/a)</td><td>384.18 (n/a)</td><td>380.90 (n/a)</td><td>289.90 (n/a)</td><td>114.80 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.18 (-8.54%)</td><td>3.28 (+4.26%)</td><td>3.31 (-6.79%)</td><td>2.08 <b>(+260.15%)</b></td><td>0.78 <b>(-49.10%)</b></td><td>1006.90 <b>(-72.23%)</b></td><td>675.12 <b>(-42.58%)</b></td><td>633.20 (+7.30%)</td><td>501.50 (+9.33%)</td><td>195.54 <b>(-85.75%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.57 (n/a)</td><td>3.15 (n/a)</td><td>3.55 (n/a)</td><td>0.58 (n/a)</td><td>1.53 (n/a)</td><td>3626.30 (n/a)</td><td>1175.82 (n/a)</td><td>590.10 (n/a)</td><td>458.70 (n/a)</td><td>1371.86 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.83 (+1.55%)</td><td>3.51 (-5.97%)</td><td>4.42 <b>(+28.90%)</b></td><td>0.65 <b>(-73.99%)</b></td><td>2.13 <b>(+70.97%)</b></td><td>3233.00 <b>(+284.42%)</b></td><td>1115.94 <b>(+83.84%)</b></td><td>474.00 <b>(-22.42%)</b></td><td>359.60 (-1.53%)</td><td>1216.30 <b>(+581.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.74 (n/a)</td><td>3.74 (n/a)</td><td>3.43 (n/a)</td><td>2.49 (n/a)</td><td>1.25 (n/a)</td><td>841.00 (n/a)</td><td>607.02 (n/a)</td><td>611.00 (n/a)</td><td>365.20 (n/a)</td><td>178.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.27 <b>(-26.53%)</b></td><td>1.86 <b>(-41.98%)</b></td><td>0.62 <b>(-72.24%)</b></td><td>0.58 <b>(-31.53%)</b></td><td>1.78 (-15.49%)</td><td>3623.90 <b>(+46.04%)</b></td><td>2348.14 <b>(+127.17%)</b></td><td>3408.00 <b>(+260.25%)</b></td><td>490.60 <b>(+36.13%)</b></td><td>1629.58 <b>(+90.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.82 (n/a)</td><td>3.21 (n/a)</td><td>2.22 (n/a)</td><td>0.85 (n/a)</td><td>2.10 (n/a)</td><td>2481.40 (n/a)</td><td>1033.66 (n/a)</td><td>946.00 (n/a)</td><td>360.40 (n/a)</td><td>857.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.49 (-8.74%)</td><td>4.13 (-6.43%)</td><td>3.89 (+3.77%)</td><td>2.73 (-6.73%)</td><td>1.52 (-9.12%)</td><td>769.10 (+7.22%)</td><td>560.44 (+6.99%)</td><td>538.60 (-3.63%)</td><td>323.10 (+9.56%)</td><td>184.10 (+11.46%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.11 (n/a)</td><td>4.41 (n/a)</td><td>3.75 (n/a)</td><td>2.92 (n/a)</td><td>1.67 (n/a)</td><td>717.30 (n/a)</td><td>523.84 (n/a)</td><td>558.90 (n/a)</td><td>294.90 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.89 (+9.14%)</td><td>2.98 (-14.01%)</td><td>3.27 (-5.67%)</td><td>0.59 <b>(-70.53%)</b></td><td>2.26 <b>(+52.12%)</b></td><td>3543.80 <b>(+239.35%)</b></td><td>1491.90 <b>(+110.45%)</b></td><td>641.00 (+6.00%)</td><td>355.80 (-8.37%)</td><td>1423.52 <b>(+358.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>5.40 (n/a)</td><td>3.47 (n/a)</td><td>3.47 (n/a)</td><td>2.01 (n/a)</td><td>1.49 (n/a)</td><td>1044.30 (n/a)</td><td>708.90 (n/a)</td><td>604.70 (n/a)</td><td>388.30 (n/a)</td><td>310.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.90 <b>(+20.03%)</b></td><td>3.54 (+13.76%)</td><td>3.00 <b>(-29.58%)</b></td><td>0.59 (-0.28%)</td><td>2.14 (+2.79%)</td><td>3571.90 (+0.28%)</td><td>1150.52 (-15.46%)</td><td>699.90 <b>(+42.00%)</b></td><td>355.30 (-16.69%)</td><td>1364.51 (-0.78%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.92 (n/a)</td><td>3.11 (n/a)</td><td>4.25 (n/a)</td><td>0.59 (n/a)</td><td>2.08 (n/a)</td><td>3561.80 (n/a)</td><td>1360.86 (n/a)</td><td>492.90 (n/a)</td><td>426.50 (n/a)</td><td>1375.29 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.38 (+8.40%)</td><td>3.48 (-1.08%)</td><td>3.32 (-14.32%)</td><td>1.71 <b>(+44.04%)</b></td><td>1.34 (-4.37%)</td><td>2455.20 <b>(-30.58%)</b></td><td>1387.62 (-9.73%)</td><td>1261.50 (+16.71%)</td><td>780.00 (-7.75%)</td><td>638.12 <b>(-43.21%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>4.96 (n/a)</td><td>3.52 (n/a)</td><td>3.88 (n/a)</td><td>1.19 (n/a)</td><td>1.40 (n/a)</td><td>3536.50 (n/a)</td><td>1537.18 (n/a)</td><td>1080.90 (n/a)</td><td>845.50 (n/a)</td><td>1123.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>9.28 (+9.09%)</td><td>4.38 (-17.31%)</td><td>3.42 <b>(-34.49%)</b></td><td>1.19 (-6.89%)</td><td>3.40 (+7.90%)</td><td>3539.20 (+7.40%)</td><td>1678.96 <b>(+30.97%)</b></td><td>1226.50 <b>(+52.66%)</b></td><td>452.20 (-8.33%)</td><td>1314.08 (+12.00%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>8.50 (n/a)</td><td>5.30 (n/a)</td><td>5.22 (n/a)</td><td>1.27 (n/a)</td><td>3.15 (n/a)</td><td>3295.20 (n/a)</td><td>1281.98 (n/a)</td><td>803.40 (n/a)</td><td>493.30 (n/a)</td><td>1173.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.97 (+13.05%)</td><td>5.59 (+8.25%)</td><td>7.57 <b>(+31.46%)</b></td><td>1.16 (-12.99%)</td><td>3.99 <b>(+39.14%)</b></td><td>3618.10 (+14.92%)</td><td>1634.54 <b>(+30.11%)</b></td><td>553.90 <b>(-23.94%)</b></td><td>467.50 (-11.56%)</td><td>1569.45 <b>(+41.88%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.94 (n/a)</td><td>5.17 (n/a)</td><td>5.76 (n/a)</td><td>1.33 (n/a)</td><td>2.87 (n/a)</td><td>3148.30 (n/a)</td><td>1256.26 (n/a)</td><td>728.20 (n/a)</td><td>528.60 (n/a)</td><td>1106.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.02 (-16.58%)</td><td>5.87 (+3.79%)</td><td>5.01 <b>(-27.65%)</b></td><td>4.33 <b>(+286.36%)</b></td><td>1.81 <b>(-56.98%)</b></td><td>969.10 <b>(-74.12%)</b></td><td>767.52 <b>(-54.78%)</b></td><td>837.30 <b>(+38.21%)</b></td><td>522.80 (+19.88%)</td><td>217.26 <b>(-86.87%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>9.62 (n/a)</td><td>5.66 (n/a)</td><td>6.92 (n/a)</td><td>1.12 (n/a)</td><td>4.20 (n/a)</td><td>3744.40 (n/a)</td><td>1697.44 (n/a)</td><td>605.80 (n/a)</td><td>436.10 (n/a)</td><td>1654.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>10.25 <b>(+42.94%)</b></td><td>4.50 <b>(-22.37%)</b></td><td>4.67 <b>(-30.28%)</b></td><td>1.10 <b>(-44.26%)</b></td><td>3.76 <b>(+74.47%)</b></td><td>3819.00 <b>(+79.40%)</b></td><td>1915.98 <b>(+107.54%)</b></td><td>897.90 <b>(+43.43%)</b></td><td>409.30 <b>(-30.03%)</b></td><td>1679.44 <b>(+149.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>7.17 (n/a)</td><td>5.80 (n/a)</td><td>6.70 (n/a)</td><td>1.97 (n/a)</td><td>2.16 (n/a)</td><td>2128.80 (n/a)</td><td>923.20 (n/a)</td><td>626.00 (n/a)</td><td>585.00 (n/a)</td><td>674.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>13.35 <b>(+91.43%)</b></td><td>7.98 <b>(+54.27%)</b></td><td>6.86 <b>(+56.43%)</b></td><td>4.66 (+9.37%)</td><td>3.27 <b>(+169.06%)</b></td><td>899.70 (-8.56%)</td><td>590.82 <b>(-29.99%)</b></td><td>611.40 <b>(-36.08%)</b></td><td>314.10 <b>(-47.77%)</b></td><td>212.35 <b>(+20.90%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>6.97 (n/a)</td><td>5.17 (n/a)</td><td>4.39 (n/a)</td><td>4.26 (n/a)</td><td>1.21 (n/a)</td><td>983.90 (n/a)</td><td>843.92 (n/a)</td><td>956.50 (n/a)</td><td>601.40 (n/a)</td><td>175.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (-0.81%)</td><td>0.75 (-17.96%)</td><td>0.80 (-1.35%)</td><td>0.16 (+1.69%)</td><td>0.64 (-12.83%)</td><td>3328.70 (-1.66%)</td><td>1630.80 <b>(+23.91%)</b></td><td>651.60 (+1.37%)</td><td>311.30 (+0.81%)</td><td>1545.64 (+15.97%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>1.70 (n/a)</td><td>0.91 (n/a)</td><td>0.82 (n/a)</td><td>0.15 (n/a)</td><td>0.73 (n/a)</td><td>3385.00 (n/a)</td><td>1316.12 (n/a)</td><td>642.80 (n/a)</td><td>308.80 (n/a)</td><td>1332.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.06 (+17.29%)</td><td>2.39 <b>(+22.54%)</b></td><td>2.42 <b>(+40.91%)</b></td><td>1.56 (+5.38%)</td><td>0.54 (+0.93%)</td><td>672.70 (-5.11%)</td><td>461.32 (-19.08%)</td><td>433.00 <b>(-29.03%)</b></td><td>342.70 (-14.73%)</td><td>124.62 (-14.44%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.61 (n/a)</td><td>1.95 (n/a)</td><td>1.72 (n/a)</td><td>1.48 (n/a)</td><td>0.53 (n/a)</td><td>708.90 (n/a)</td><td>570.10 (n/a)</td><td>610.10 (n/a)</td><td>401.90 (n/a)</td><td>145.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.69 <b>(-28.31%)</b></td><td>1.46 (-14.98%)</td><td>1.13 (+5.83%)</td><td>0.60 (+0.33%)</td><td>0.93 <b>(-31.72%)</b></td><td>3468.00 (-0.33%)</td><td>2019.18 (+2.29%)</td><td>1848.60 (-5.51%)</td><td>779.10 <b>(+39.50%)</b></td><td>1204.29 (-6.36%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>3.75 (n/a)</td><td>1.72 (n/a)</td><td>1.07 (n/a)</td><td>0.60 (n/a)</td><td>1.36 (n/a)</td><td>3479.40 (n/a)</td><td>1974.00 (n/a)</td><td>1956.40 (n/a)</td><td>558.50 (n/a)</td><td>1286.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.64 <b>(-21.03%)</b></td><td>1.22 (-16.83%)</td><td>1.11 <b>(-24.04%)</b></td><td>0.78 (-17.39%)</td><td>0.39 (-3.89%)</td><td>669.80 <b>(+21.03%)</b></td><td>468.06 <b>(+22.81%)</b></td><td>471.60 <b>(+31.66%)</b></td><td>320.40 <b>(+26.64%)</b></td><td>149.59 <b>(+37.67%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>2.07 (n/a)</td><td>1.46 (n/a)</td><td>1.46 (n/a)</td><td>0.95 (n/a)</td><td>0.40 (n/a)</td><td>553.40 (n/a)</td><td>381.12 (n/a)</td><td>358.20 (n/a)</td><td>253.00 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (-18.12%)</td><td>0.09 <b>(-20.02%)</b></td><td>0.10 (-6.27%)</td><td>0.05 <b>(-31.64%)</b></td><td>0.03 <b>(+23.16%)</b></td><td>608.80 <b>(+46.28%)</b></td><td>417.80 <b>(+32.67%)</b></td><td>339.90 (+6.69%)</td><td>285.60 <b>(+22.16%)</b></td><td>148.35 <b>(+122.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>416.20 (n/a)</td><td>314.92 (n/a)</td><td>318.60 (n/a)</td><td>233.80 (n/a)</td><td>66.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (-0.28%)</td><td>0.10 <b>(+25.80%)</b></td><td>0.10 <b>(+44.77%)</b></td><td>0.05 (+10.60%)</td><td>0.03 (+8.65%)</td><td>603.50 (-9.57%)</td><td>374.30 (-19.67%)</td><td>317.90 <b>(-30.92%)</b></td><td>249.50 (+0.28%)</td><td>152.05 (-1.01%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>667.40 (n/a)</td><td>465.98 (n/a)</td><td>460.20 (n/a)</td><td>248.80 (n/a)</td><td>153.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.26 (-1.44%)</td><td>0.17 (-15.39%)</td><td>0.15 <b>(-29.01%)</b></td><td>0.13 (-4.66%)</td><td>0.05 (+14.81%)</td><td>506.20 (+4.89%)</td><td>411.96 (+19.97%)</td><td>450.60 <b>(+40.86%)</b></td><td>256.60 (+1.46%)</td><td>99.43 (+15.99%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>482.60 (n/a)</td><td>343.40 (n/a)</td><td>319.90 (n/a)</td><td>252.90 (n/a)</td><td>85.73 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.27 (+14.90%)</td><td>0.19 <b>(+25.22%)</b></td><td>0.21 <b>(+60.17%)</b></td><td>0.12 (-4.43%)</td><td>0.06 <b>(+31.64%)</b></td><td>565.40 (+4.63%)</td><td>370.04 (-17.52%)</td><td>309.70 <b>(-37.57%)</b></td><td>247.30 (-12.98%)</td><td>128.33 <b>(+25.37%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>540.40 (n/a)</td><td>448.64 (n/a)</td><td>496.10 (n/a)</td><td>284.20 (n/a)</td><td>102.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 <b>(-21.20%)</b></td><td>0.16 (-16.19%)</td><td>0.21 <b>(+39.40%)</b></td><td>0.04 <b>(-71.26%)</b></td><td>0.09 (+11.49%)</td><td>1863.50 <b>(+247.99%)</b></td><td>668.16 <b>(+75.11%)</b></td><td>305.40 <b>(-28.28%)</b></td><td>289.50 <b>(+26.92%)</b></td><td>680.44 <b>(+393.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>535.50 (n/a)</td><td>381.56 (n/a)</td><td>425.80 (n/a)</td><td>228.10 (n/a)</td><td>137.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.58 <b>(+34.13%)</b></td><td>0.45 <b>(+69.95%)</b></td><td>0.48 <b>(+133.58%)</b></td><td>0.26 <b>(+31.42%)</b></td><td>0.12 (+17.54%)</td><td>508.00 <b>(-23.91%)</b></td><td>314.30 <b>(-42.17%)</b></td><td>270.80 <b>(-57.19%)</b></td><td>227.00 <b>(-25.45%)</b></td><td>111.39 <b>(-31.07%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.43 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>667.60 (n/a)</td><td>543.46 (n/a)</td><td>632.50 (n/a)</td><td>304.50 (n/a)</td><td>161.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.46 <b>(+53.20%)</b></td><td>0.34 <b>(+28.19%)</b></td><td>0.28 (+2.80%)</td><td>0.26 (+8.44%)</td><td>0.10 <b>(+321.97%)</b></td><td>506.30 (-7.78%)</td><td>411.04 (-16.96%)</td><td>473.80 (-2.73%)</td><td>283.30 <b>(-34.72%)</b></td><td>113.06 <b>(+151.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>549.00 (n/a)</td><td>494.98 (n/a)</td><td>487.10 (n/a)</td><td>434.00 (n/a)</td><td>44.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.57 (+9.54%)</td><td>0.39 (+16.24%)</td><td>0.47 <b>(+86.14%)</b></td><td>0.20 (-6.42%)</td><td>0.17 (+18.79%)</td><td>649.30 (+6.86%)</td><td>398.16 (-9.40%)</td><td>278.80 <b>(-46.28%)</b></td><td>231.30 (-8.69%)</td><td>195.00 <b>(+22.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>607.60 (n/a)</td><td>439.46 (n/a)</td><td>519.00 (n/a)</td><td>253.30 (n/a)</td><td>159.61 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (+14.78%)</td><td>0.05 (-5.46%)</td><td>0.05 (-16.09%)</td><td>0.03 <b>(-25.49%)</b></td><td>0.02 <b>(+53.99%)</b></td><td>640.30 <b>(+34.21%)</b></td><td>404.84 (+14.37%)</td><td>354.30 (+19.17%)</td><td>246.70 (-12.89%)</td><td>164.91 <b>(+82.87%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:03:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.10 (n/a)</td><td>353.96 (n/a)</td><td>297.30 (n/a)</td><td>283.20 (n/a)</td><td>90.18 (n/a)</td>
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
