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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-7.26%)</td><td>0.02 <b>(-34.62%)</b></td><td>0.02 <b>(-40.01%)</b></td><td>0.00 <b>(-83.32%)</b></td><td>0.01 <b>(+182.52%)</b></td><td>1846.30 <b>(+499.45%)</b></td><td>659.54 <b>(+147.98%)</b></td><td>409.20 <b>(+66.68%)</b></td><td>251.50 (+7.85%)</td><td>671.17 <b>(+1827.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>308.00 (n/a)</td><td>265.96 (n/a)</td><td>245.50 (n/a)</td><td>233.20 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-5.05%)</td><td>0.02 <b>(-31.82%)</b></td><td>0.01 <b>(-38.22%)</b></td><td>0.01 <b>(-55.72%)</b></td><td>0.01 <b>(+124.88%)</b></td><td>666.50 <b>(+125.86%)</b></td><td>444.98 <b>(+71.29%)</b></td><td>417.30 <b>(+61.87%)</b></td><td>224.10 (+5.31%)</td><td>193.94 <b>(+443.87%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>295.10 (n/a)</td><td>259.78 (n/a)</td><td>257.80 (n/a)</td><td>212.80 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (+0.73%)</td><td>0.02 (+4.49%)</td><td>0.02 (+7.08%)</td><td>0.01 <b>(+124.34%)</b></td><td>0.01 <b>(-36.73%)</b></td><td>500.70 <b>(-55.43%)</b></td><td>377.62 <b>(-24.95%)</b></td><td>398.10 (-6.62%)</td><td>237.00 (-0.71%)</td><td>105.31 <b>(-71.03%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1123.40 (n/a)</td><td>503.14 (n/a)</td><td>426.30 (n/a)</td><td>238.70 (n/a)</td><td>363.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(-20.39%)</b></td><td>0.02 (+0.84%)</td><td>0.02 (+18.74%)</td><td>0.01 <b>(+270.64%)</b></td><td>0.01 <b>(-47.44%)</b></td><td>569.00 <b>(-73.02%)</b></td><td>404.02 <b>(-43.18%)</b></td><td>352.50 (-15.77%)</td><td>266.20 <b>(+25.63%)</b></td><td>145.61 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2109.10 (n/a)</td><td>711.06 (n/a)</td><td>418.50 (n/a)</td><td>211.90 (n/a)</td><td>795.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(-26.53%)</b></td><td>0.02 (-0.99%)</td><td>0.02 <b>(+56.42%)</b></td><td>0.01 (+14.07%)</td><td>0.00 <b>(-48.53%)</b></td><td>524.80 (-12.33%)</td><td>365.74 (-9.50%)</td><td>303.20 <b>(-36.06%)</b></td><td>285.50 <b>(+36.15%)</b></td><td>104.55 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.60 (n/a)</td><td>404.12 (n/a)</td><td>474.20 (n/a)</td><td>209.70 (n/a)</td><td>167.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(-21.32%)</b></td><td>0.02 (-6.19%)</td><td>0.01 (-8.35%)</td><td>0.01 (+13.23%)</td><td>0.01 <b>(-33.11%)</b></td><td>539.90 (-11.69%)</td><td>427.46 (-1.57%)</td><td>487.90 (+9.10%)</td><td>269.50 <b>(+27.12%)</b></td><td>130.82 <b>(-27.04%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.40 (n/a)</td><td>434.28 (n/a)</td><td>447.20 (n/a)</td><td>212.00 (n/a)</td><td>179.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (+18.14%)</td><td>0.04 (+5.91%)</td><td>0.04 (+7.72%)</td><td>0.02 <b>(+31.83%)</b></td><td>0.02 (+17.09%)</td><td>496.80 <b>(-24.14%)</b></td><td>344.10 (-5.96%)</td><td>293.20 (-7.16%)</td><td>199.80 (-15.37%)</td><td>139.08 (-18.93%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>654.90 (n/a)</td><td>365.92 (n/a)</td><td>315.80 (n/a)</td><td>236.10 (n/a)</td><td>171.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (-16.10%)</td><td>0.04 (+10.87%)</td><td>0.05 <b>(+56.28%)</b></td><td>0.03 <b>(+32.43%)</b></td><td>0.01 <b>(-37.02%)</b></td><td>484.90 <b>(-24.49%)</b></td><td>319.80 (-18.67%)</td><td>271.30 <b>(-36.01%)</b></td><td>243.90 (+19.21%)</td><td>102.29 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>642.20 (n/a)</td><td>393.20 (n/a)</td><td>424.00 (n/a)</td><td>204.60 (n/a)</td><td>175.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 <b>(+57.41%)</b></td><td>0.04 (-4.59%)</td><td>0.03 <b>(-33.35%)</b></td><td>0.02 <b>(-27.43%)</b></td><td>0.03 <b>(+140.19%)</b></td><td>641.10 <b>(+37.78%)</b></td><td>383.06 <b>(+29.38%)</b></td><td>378.10 <b>(+50.04%)</b></td><td>145.60 <b>(-36.47%)</b></td><td>200.80 <b>(+104.69%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>465.30 (n/a)</td><td>296.08 (n/a)</td><td>252.00 (n/a)</td><td>229.20 (n/a)</td><td>98.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (+13.91%)</td><td>0.03 (-1.92%)</td><td>0.03 (+1.72%)</td><td>0.02 (+0.16%)</td><td>0.01 (+2.66%)</td><td>560.50 (-0.18%)</td><td>398.50 (+0.99%)</td><td>411.50 (-1.67%)</td><td>210.40 (-12.22%)</td><td>135.23 (-7.88%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>394.58 (n/a)</td><td>418.50 (n/a)</td><td>239.70 (n/a)</td><td>146.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-9.28%)</td><td>0.04 (+15.23%)</td><td>0.04 <b>(+48.80%)</b></td><td>0.03 (+9.15%)</td><td>0.01 <b>(-33.73%)</b></td><td>471.10 (-8.38%)</td><td>324.94 (-16.86%)</td><td>289.60 <b>(-32.79%)</b></td><td>280.70 (+10.21%)</td><td>81.86 <b>(-30.24%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.20 (n/a)</td><td>390.82 (n/a)</td><td>430.90 (n/a)</td><td>254.70 (n/a)</td><td>117.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (-3.90%)</td><td>0.03 (-13.41%)</td><td>0.03 <b>(-30.54%)</b></td><td>0.01 <b>(-49.70%)</b></td><td>0.01 <b>(+31.67%)</b></td><td>1056.20 <b>(+98.80%)</b></td><td>507.16 <b>(+36.10%)</b></td><td>444.40 <b>(+43.96%)</b></td><td>258.80 (+4.06%)</td><td>324.04 <b>(+158.50%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.30 (n/a)</td><td>372.64 (n/a)</td><td>308.70 (n/a)</td><td>248.70 (n/a)</td><td>125.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (+8.78%)</td><td>0.07 (-6.74%)</td><td>0.06 <b>(-23.84%)</b></td><td>0.05 <b>(-26.52%)</b></td><td>0.03 <b>(+110.52%)</b></td><td>542.10 <b>(+36.10%)</b></td><td>384.88 (+19.15%)</td><td>418.50 <b>(+31.31%)</b></td><td>225.90 (-8.10%)</td><td>144.75 <b>(+157.13%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>398.30 (n/a)</td><td>323.02 (n/a)</td><td>318.70 (n/a)</td><td>245.80 (n/a)</td><td>56.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (-12.60%)</td><td>0.06 (-18.96%)</td><td>0.05 (-17.41%)</td><td>0.01 <b>(-65.49%)</b></td><td>0.03 (+16.80%)</td><td>1887.60 <b>(+189.82%)</b></td><td>704.56 <b>(+72.43%)</b></td><td>449.30 <b>(+21.07%)</b></td><td>274.40 (+14.43%)</td><td>673.12 <b>(+308.23%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>651.30 (n/a)</td><td>408.60 (n/a)</td><td>371.10 (n/a)</td><td>239.80 (n/a)</td><td>164.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (+11.70%)</td><td>0.09 <b>(+30.04%)</b></td><td>0.09 <b>(+54.15%)</b></td><td>0.05 <b>(+33.48%)</b></td><td>0.02 (-13.25%)</td><td>498.90 <b>(-25.09%)</b></td><td>306.28 <b>(-27.22%)</b></td><td>268.70 <b>(-35.13%)</b></td><td>219.50 (-10.48%)</td><td>110.17 <b>(-35.47%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>666.00 (n/a)</td><td>420.82 (n/a)</td><td>414.20 (n/a)</td><td>245.20 (n/a)</td><td>170.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (+7.62%)</td><td>0.06 (-2.14%)</td><td>0.05 (-10.93%)</td><td>0.04 <b>(+41.21%)</b></td><td>0.03 (-15.09%)</td><td>692.20 <b>(-29.18%)</b></td><td>454.78 (-10.19%)</td><td>475.00 (+12.27%)</td><td>227.50 (-7.07%)</td><td>170.19 <b>(-43.96%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>977.40 (n/a)</td><td>506.40 (n/a)</td><td>423.10 (n/a)</td><td>244.80 (n/a)</td><td>303.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 <b>(+22.43%)</b></td><td>0.06 (+6.82%)</td><td>0.05 (-4.82%)</td><td>0.04 (-8.46%)</td><td>0.03 <b>(+53.08%)</b></td><td>598.10 (+9.24%)</td><td>456.66 (-0.46%)</td><td>511.90 (+5.07%)</td><td>224.60 (-18.30%)</td><td>146.81 <b>(+37.44%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.50 (n/a)</td><td>458.78 (n/a)</td><td>487.20 (n/a)</td><td>274.90 (n/a)</td><td>106.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 <b>(-22.28%)</b></td><td>0.05 <b>(-34.37%)</b></td><td>0.04 <b>(-47.22%)</b></td><td>0.01 <b>(-72.68%)</b></td><td>0.03 (+3.10%)</td><td>1836.30 <b>(+265.94%)</b></td><td>728.70 <b>(+102.75%)</b></td><td>559.80 <b>(+89.44%)</b></td><td>294.90 <b>(+28.66%)</b></td><td>629.57 <b>(+398.64%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>501.80 (n/a)</td><td>359.40 (n/a)</td><td>295.50 (n/a)</td><td>229.20 (n/a)</td><td>126.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.25 <b>(+30.20%)</b></td><td>0.14 (+11.97%)</td><td>0.11 (+14.43%)</td><td>0.05 <b>(-42.51%)</b></td><td>0.09 <b>(+63.96%)</b></td><td>1043.80 <b>(+73.97%)</b></td><td>492.98 (+11.90%)</td><td>456.40 (-12.60%)</td><td>194.20 <b>(-23.18%)</b></td><td>340.03 <b>(+113.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>600.00 (n/a)</td><td>440.54 (n/a)</td><td>522.20 (n/a)</td><td>252.80 (n/a)</td><td>159.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 <b>(+68.31%)</b></td><td>0.11 (+11.80%)</td><td>0.09 (-2.93%)</td><td>0.03 <b>(-66.28%)</b></td><td>0.07 <b>(+254.36%)</b></td><td>1907.00 <b>(+196.53%)</b></td><td>726.72 <b>(+37.94%)</b></td><td>529.30 (+3.02%)</td><td>236.40 <b>(-40.57%)</b></td><td>672.02 <b>(+583.82%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>643.10 (n/a)</td><td>526.82 (n/a)</td><td>513.80 (n/a)</td><td>397.80 (n/a)</td><td>98.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.23 (-18.67%)</td><td>0.14 (+9.24%)</td><td>0.16 <b>(+62.20%)</b></td><td>0.07 (-5.61%)</td><td>0.06 <b>(-23.99%)</b></td><td>657.50 (+5.95%)</td><td>420.60 (-10.53%)</td><td>315.70 <b>(-38.34%)</b></td><td>218.40 <b>(+22.97%)</b></td><td>201.24 (+16.58%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>620.60 (n/a)</td><td>470.08 (n/a)</td><td>512.00 (n/a)</td><td>177.60 (n/a)</td><td>172.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 <b>(+38.32%)</b></td><td>0.11 (-4.45%)</td><td>0.10 (-15.45%)</td><td>0.04 <b>(-49.43%)</b></td><td>0.06 <b>(+167.64%)</b></td><td>1106.10 <b>(+97.77%)</b></td><td>573.80 <b>(+32.30%)</b></td><td>499.50 (+18.28%)</td><td>234.70 <b>(-27.70%)</b></td><td>335.99 <b>(+284.31%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>559.30 (n/a)</td><td>433.72 (n/a)</td><td>422.30 (n/a)</td><td>324.60 (n/a)</td><td>87.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.18 (-10.61%)</td><td>0.14 (+5.23%)</td><td>0.16 <b>(+84.68%)</b></td><td>0.07 (-5.42%)</td><td>0.05 <b>(-22.53%)</b></td><td>657.80 (+5.74%)</td><td>405.42 (-9.37%)</td><td>303.30 <b>(-45.85%)</b></td><td>270.80 (+11.85%)</td><td>173.60 (-6.94%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>622.10 (n/a)</td><td>447.34 (n/a)</td><td>560.10 (n/a)</td><td>242.10 (n/a)</td><td>186.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (-5.53%)</td><td>0.10 <b>(-23.30%)</b></td><td>0.09 <b>(-28.72%)</b></td><td>0.07 (-12.75%)</td><td>0.03 (+5.22%)</td><td>659.70 (+14.61%)</td><td>526.42 <b>(+31.59%)</b></td><td>533.10 <b>(+40.29%)</b></td><td>340.20 (+5.85%)</td><td>119.38 (+17.80%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>575.60 (n/a)</td><td>400.06 (n/a)</td><td>380.00 (n/a)</td><td>321.40 (n/a)</td><td>101.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (-8.94%)</td><td>0.01 <b>(-21.55%)</b></td><td>0.01 <b>(-35.31%)</b></td><td>0.01 (+4.46%)</td><td>0.00 <b>(-29.72%)</b></td><td>512.40 (-4.28%)</td><td>396.22 <b>(+22.17%)</b></td><td>400.10 <b>(+54.60%)</b></td><td>269.50 (+9.82%)</td><td>86.70 <b>(-29.24%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>535.30 (n/a)</td><td>324.32 (n/a)</td><td>258.80 (n/a)</td><td>245.40 (n/a)</td><td>122.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (+8.78%)</td><td>0.01 <b>(+50.77%)</b></td><td>0.01 <b>(+68.73%)</b></td><td>0.01 <b>(+161.60%)</b></td><td>0.00 <b>(-38.39%)</b></td><td>406.60 <b>(-61.78%)</b></td><td>293.74 <b>(-45.51%)</b></td><td>268.50 <b>(-40.73%)</b></td><td>235.10 (-8.06%)</td><td>68.45 <b>(-78.49%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1063.80 (n/a)</td><td>539.08 (n/a)</td><td>453.00 (n/a)</td><td>255.70 (n/a)</td><td>318.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (-3.45%)</td><td>0.01 (-2.78%)</td><td>0.01 (+17.05%)</td><td>0.00 <b>(-35.75%)</b></td><td>0.00 (+12.59%)</td><td>985.80 <b>(+55.64%)</b></td><td>467.14 (+15.42%)</td><td>366.10 (-14.58%)</td><td>261.70 (+3.56%)</td><td>300.66 <b>(+93.07%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>633.40 (n/a)</td><td>404.74 (n/a)</td><td>428.60 (n/a)</td><td>252.70 (n/a)</td><td>155.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 <b>(+28.58%)</b></td><td>0.01 (+13.73%)</td><td>0.01 (-2.31%)</td><td>0.01 (-0.41%)</td><td>0.00 <b>(+61.80%)</b></td><td>517.50 (+0.43%)</td><td>365.90 (-6.19%)</td><td>405.00 (+2.35%)</td><td>208.00 <b>(-22.21%)</b></td><td>138.11 <b>(+24.25%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.30 (n/a)</td><td>390.04 (n/a)</td><td>395.70 (n/a)</td><td>267.40 (n/a)</td><td>111.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(+51.89%)</b></td><td>0.01 <b>(+27.44%)</b></td><td>0.01 <b>(+62.18%)</b></td><td>0.00 (-14.07%)</td><td>0.00 <b>(+100.62%)</b></td><td>591.10 (+16.38%)</td><td>349.26 (-10.72%)</td><td>271.10 <b>(-38.33%)</b></td><td>172.20 <b>(-34.17%)</b></td><td>174.03 <b>(+62.56%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.90 (n/a)</td><td>391.18 (n/a)</td><td>439.60 (n/a)</td><td>261.60 (n/a)</td><td>107.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 <b>(-35.68%)</b></td><td>0.01 (-7.18%)</td><td>0.01 <b>(+44.92%)</b></td><td>0.00 (+9.80%)</td><td>0.00 <b>(-49.36%)</b></td><td>603.20 (-8.92%)</td><td>421.50 (-6.37%)</td><td>375.90 <b>(-30.99%)</b></td><td>255.10 <b>(+55.45%)</b></td><td>154.37 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>662.30 (n/a)</td><td>450.20 (n/a)</td><td>544.70 (n/a)</td><td>164.10 (n/a)</td><td>198.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+10.18%)</td><td>0.01 (-14.70%)</td><td>0.01 <b>(-33.47%)</b></td><td>0.01 (-10.48%)</td><td>0.00 <b>(+37.08%)</b></td><td>554.10 (+11.71%)</td><td>446.12 <b>(+21.80%)</b></td><td>493.30 <b>(+50.30%)</b></td><td>247.30 (-9.25%)</td><td>124.42 <b>(+34.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.00 (n/a)</td><td>366.26 (n/a)</td><td>328.20 (n/a)</td><td>272.50 (n/a)</td><td>92.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+119.55%)</b></td><td>0.02 <b>(+45.41%)</b></td><td>0.01 (-14.50%)</td><td>0.01 (+10.87%)</td><td>0.01 <b>(+273.73%)</b></td><td>567.00 (-9.81%)</td><td>402.70 (-11.46%)</td><td>514.60 (+16.95%)</td><td>137.40 <b>(-54.46%)</b></td><td>199.36 <b>(+65.20%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>628.70 (n/a)</td><td>454.82 (n/a)</td><td>440.00 (n/a)</td><td>301.70 (n/a)</td><td>120.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(+122.59%)</b></td><td>0.02 <b>(+69.68%)</b></td><td>0.01 (+11.24%)</td><td>0.01 <b>(+224.82%)</b></td><td>0.01 <b>(+104.60%)</b></td><td>643.80 <b>(-69.22%)</b></td><td>420.46 <b>(-49.03%)</b></td><td>490.50 (-10.10%)</td><td>199.40 <b>(-55.07%)</b></td><td>182.63 <b>(-74.29%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2091.30 (n/a)</td><td>824.90 (n/a)</td><td>545.60 (n/a)</td><td>443.80 (n/a)</td><td>710.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+15.98%)</td><td>0.01 (+13.49%)</td><td>0.01 (+4.57%)</td><td>0.01 (+13.36%)</td><td>0.00 (+17.99%)</td><td>578.20 (-11.79%)</td><td>472.10 (-11.72%)</td><td>522.80 (-4.37%)</td><td>281.40 (-13.76%)</td><td>117.73 (-13.28%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>655.50 (n/a)</td><td>534.80 (n/a)</td><td>546.70 (n/a)</td><td>326.30 (n/a)</td><td>135.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-13.69%)</td><td>0.02 (+16.41%)</td><td>0.02 <b>(+46.00%)</b></td><td>0.01 <b>(+47.87%)</b></td><td>0.00 <b>(-45.07%)</b></td><td>425.80 <b>(-32.37%)</b></td><td>303.88 <b>(-23.13%)</b></td><td>290.40 <b>(-31.51%)</b></td><td>224.90 (+15.87%)</td><td>74.59 <b>(-54.20%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>629.60 (n/a)</td><td>395.32 (n/a)</td><td>424.00 (n/a)</td><td>194.10 (n/a)</td><td>162.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-17.87%)</td><td>0.02 (+17.06%)</td><td>0.02 <b>(+32.20%)</b></td><td>0.01 <b>(+20.37%)</b></td><td>0.00 <b>(-43.59%)</b></td><td>526.70 (-16.92%)</td><td>362.44 <b>(-21.68%)</b></td><td>335.90 <b>(-24.36%)</b></td><td>268.40 <b>(+21.72%)</b></td><td>98.86 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.00 (n/a)</td><td>462.74 (n/a)</td><td>444.10 (n/a)</td><td>220.50 (n/a)</td><td>161.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (+5.52%)</td><td>0.02 <b>(-25.28%)</b></td><td>0.02 <b>(-41.37%)</b></td><td>0.02 (-13.84%)</td><td>0.01 <b>(+21.45%)</b></td><td>603.40 (+16.06%)</td><td>483.22 <b>(+38.30%)</b></td><td>498.30 <b>(+70.59%)</b></td><td>260.20 (-5.24%)</td><td>136.98 <b>(+31.05%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.90 (n/a)</td><td>349.40 (n/a)</td><td>292.10 (n/a)</td><td>274.60 (n/a)</td><td>104.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 <b>(+23.49%)</b></td><td>0.03 (-6.63%)</td><td>0.03 (+1.09%)</td><td>0.00 <b>(-77.10%)</b></td><td>0.02 <b>(+103.96%)</b></td><td>2511.60 <b>(+336.80%)</b></td><td>775.32 <b>(+112.82%)</b></td><td>304.90 (-1.07%)</td><td>199.50 (-19.03%)</td><td>980.59 <b>(+668.54%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.00 (n/a)</td><td>364.30 (n/a)</td><td>308.20 (n/a)</td><td>246.40 (n/a)</td><td>127.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-1.10%)</td><td>0.04 <b>(+39.23%)</b></td><td>0.04 <b>(+68.66%)</b></td><td>0.03 <b>(+126.08%)</b></td><td>0.01 <b>(-59.54%)</b></td><td>365.20 <b>(-55.77%)</b></td><td>292.08 <b>(-40.38%)</b></td><td>274.90 <b>(-40.72%)</b></td><td>250.10 (+1.13%)</td><td>45.80 <b>(-81.05%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>825.60 (n/a)</td><td>489.88 (n/a)</td><td>463.70 (n/a)</td><td>247.30 (n/a)</td><td>241.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-5.01%)</td><td>0.03 (+6.05%)</td><td>0.03 (-11.76%)</td><td>0.01 <b>(+162.92%)</b></td><td>0.01 <b>(-24.42%)</b></td><td>722.40 <b>(-61.96%)</b></td><td>408.74 <b>(-36.87%)</b></td><td>374.50 (+13.35%)</td><td>256.60 (+5.25%)</td><td>191.08 <b>(-72.94%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1899.30 (n/a)</td><td>647.42 (n/a)</td><td>330.40 (n/a)</td><td>243.80 (n/a)</td><td>706.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (+4.47%)</td><td>0.03 (-2.81%)</td><td>0.02 (+9.55%)</td><td>0.02 (-17.53%)</td><td>0.01 (+14.16%)</td><td>625.50 <b>(+21.27%)</b></td><td>429.26 (+8.70%)</td><td>442.90 (-8.72%)</td><td>227.30 (-4.29%)</td><td>185.60 <b>(+34.10%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.80 (n/a)</td><td>394.92 (n/a)</td><td>485.20 (n/a)</td><td>237.50 (n/a)</td><td>138.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(-27.27%)</b></td><td>0.02 <b>(-29.37%)</b></td><td>0.02 <b>(-30.00%)</b></td><td>0.01 <b>(-29.79%)</b></td><td>0.00 <b>(-35.52%)</b></td><td>713.30 <b>(+42.43%)</b></td><td>556.62 <b>(+40.11%)</b></td><td>592.70 <b>(+42.85%)</b></td><td>392.30 <b>(+37.46%)</b></td><td>122.01 <b>(+24.79%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>397.26 (n/a)</td><td>414.90 (n/a)</td><td>285.40 (n/a)</td><td>97.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (+10.95%)</td><td>0.06 <b>(+38.46%)</b></td><td>0.06 <b>(+38.75%)</b></td><td>0.04 <b>(+27.24%)</b></td><td>0.01 (-5.63%)</td><td>491.80 <b>(-21.40%)</b></td><td>343.62 <b>(-29.63%)</b></td><td>331.50 <b>(-27.93%)</b></td><td>279.10 (-9.85%)</td><td>87.23 <b>(-35.71%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.70 (n/a)</td><td>488.30 (n/a)</td><td>460.00 (n/a)</td><td>309.60 (n/a)</td><td>135.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (-0.21%)</td><td>0.05 (-17.29%)</td><td>0.05 <b>(-23.03%)</b></td><td>0.04 (-16.05%)</td><td>0.02 (+9.73%)</td><td>595.70 (+19.12%)</td><td>437.78 <b>(+23.79%)</b></td><td>459.20 <b>(+29.90%)</b></td><td>234.40 (+0.21%)</td><td>131.46 <b>(+23.50%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>500.10 (n/a)</td><td>353.64 (n/a)</td><td>353.50 (n/a)</td><td>233.90 (n/a)</td><td>106.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-15.69%)</td><td>0.05 (-7.63%)</td><td>0.05 (-14.54%)</td><td>0.04 <b>(+36.95%)</b></td><td>0.01 <b>(-46.13%)</b></td><td>529.80 <b>(-26.97%)</b></td><td>429.54 (-4.26%)</td><td>444.70 (+17.03%)</td><td>294.50 (+18.61%)</td><td>96.17 <b>(-53.62%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>725.50 (n/a)</td><td>448.66 (n/a)</td><td>380.00 (n/a)</td><td>248.30 (n/a)</td><td>207.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 <b>(+173.80%)</b></td><td>0.06 <b>(+51.26%)</b></td><td>0.04 (-1.31%)</td><td>0.04 <b>(+81.57%)</b></td><td>0.04 <b>(+277.43%)</b></td><td>591.40 <b>(-44.92%)</b></td><td>481.18 <b>(-23.34%)</b></td><td>561.90 (+1.33%)</td><td>162.60 <b>(-63.48%)</b></td><td>179.76 <b>(-30.02%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1073.80 (n/a)</td><td>627.72 (n/a)</td><td>554.50 (n/a)</td><td>445.20 (n/a)</td><td>256.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 <b>(+43.74%)</b></td><td>0.07 <b>(+44.11%)</b></td><td>0.05 (-3.24%)</td><td>0.04 <b>(+124.51%)</b></td><td>0.03 <b>(+49.87%)</b></td><td>485.20 <b>(-55.46%)</b></td><td>351.28 <b>(-34.74%)</b></td><td>420.30 (+3.37%)</td><td>189.60 <b>(-30.45%)</b></td><td>140.53 <b>(-56.78%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1089.40 (n/a)</td><td>538.28 (n/a)</td><td>406.60 (n/a)</td><td>272.60 (n/a)</td><td>325.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 <b>(-22.08%)</b></td><td>0.04 <b>(-34.05%)</b></td><td>0.04 <b>(-40.62%)</b></td><td>0.01 <b>(-67.72%)</b></td><td>0.02 <b>(-21.54%)</b></td><td>2014.00 <b>(+209.75%)</b></td><td>768.38 <b>(+89.54%)</b></td><td>521.00 <b>(+68.39%)</b></td><td>313.10 <b>(+28.37%)</b></td><td>701.63 <b>(+264.09%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>650.20 (n/a)</td><td>405.40 (n/a)</td><td>309.40 (n/a)</td><td>243.90 (n/a)</td><td>192.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>379.54 (n/a)</td><td>315.20 (n/a)</td><td>265.80 (n/a)</td><td>144.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.40 (n/a)</td><td>333.98 (n/a)</td><td>272.70 (n/a)</td><td>236.50 (n/a)</td><td>171.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>923.60 (n/a)</td><td>533.62 (n/a)</td><td>494.00 (n/a)</td><td>278.70 (n/a)</td><td>236.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>467.70 (n/a)</td><td>320.52 (n/a)</td><td>275.90 (n/a)</td><td>148.70 (n/a)</td><td>132.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.10 (n/a)</td><td>452.82 (n/a)</td><td>425.90 (n/a)</td><td>322.70 (n/a)</td><td>122.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>948.00 (n/a)</td><td>520.60 (n/a)</td><td>494.50 (n/a)</td><td>271.10 (n/a)</td><td>278.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>498.60 (n/a)</td><td>340.20 (n/a)</td><td>270.60 (n/a)</td><td>242.20 (n/a)</td><td>120.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1921.30 (n/a)</td><td>631.34 (n/a)</td><td>263.30 (n/a)</td><td>231.90 (n/a)</td><td>727.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1327.00 (n/a)</td><td>641.24 (n/a)</td><td>533.50 (n/a)</td><td>298.60 (n/a)</td><td>396.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (+10.78%)</td><td>0.16 (+4.68%)</td><td>0.18 (+11.19%)</td><td>0.08 (-11.06%)</td><td>0.05 <b>(+27.02%)</b></td><td>606.70 (+12.44%)</td><td>342.22 (-0.36%)</td><td>279.90 (-10.06%)</td><td>239.70 (-9.72%)</td><td>149.87 <b>(+33.56%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>539.60 (n/a)</td><td>343.46 (n/a)</td><td>311.20 (n/a)</td><td>265.50 (n/a)</td><td>112.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>646.60 (n/a)</td><td>429.12 (n/a)</td><td>429.80 (n/a)</td><td>278.70 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>606.50 (n/a)</td><td>447.46 (n/a)</td><td>507.70 (n/a)</td><td>211.10 (n/a)</td><td>151.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>359.32 (n/a)</td><td>273.10 (n/a)</td><td>209.80 (n/a)</td><td>161.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.80 (n/a)</td><td>434.30 (n/a)</td><td>439.40 (n/a)</td><td>223.30 (n/a)</td><td>138.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.90 (n/a)</td><td>395.90 (n/a)</td><td>351.40 (n/a)</td><td>266.90 (n/a)</td><td>124.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>385.00 (n/a)</td><td>327.30 (n/a)</td><td>318.30 (n/a)</td><td>272.70 (n/a)</td><td>44.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.40 (n/a)</td><td>386.64 (n/a)</td><td>319.90 (n/a)</td><td>250.90 (n/a)</td><td>134.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>704.70 (n/a)</td><td>508.08 (n/a)</td><td>478.80 (n/a)</td><td>381.40 (n/a)</td><td>132.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>688.70 (n/a)</td><td>408.46 (n/a)</td><td>392.90 (n/a)</td><td>238.50 (n/a)</td><td>175.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>520.40 (n/a)</td><td>348.04 (n/a)</td><td>298.60 (n/a)</td><td>275.80 (n/a)</td><td>101.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>783.50 (n/a)</td><td>473.06 (n/a)</td><td>356.30 (n/a)</td><td>250.00 (n/a)</td><td>237.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>569.30 (n/a)</td><td>400.14 (n/a)</td><td>357.30 (n/a)</td><td>250.60 (n/a)</td><td>151.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>537.90 (n/a)</td><td>356.76 (n/a)</td><td>264.50 (n/a)</td><td>228.60 (n/a)</td><td>150.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.05 (-9.22%)</td><td>2.50 (+1.57%)</td><td>2.33 <b>(+21.06%)</b></td><td>1.80 (+3.30%)</td><td>0.93 (-19.50%)</td><td>5836.50 (-3.19%)</td><td>4588.16 (-4.87%)</td><td>4502.80 (-17.40%)</td><td>2587.50 (+10.15%)</td><td>1347.52 (-11.36%)</td><td>1659.92 (-9.22%)</td><td>1022.49 (+1.57%)</td><td>953.84 <b>(+21.06%)</b></td><td>735.89 (+3.30%)</td><td>379.02 (-19.50%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.46 (n/a)</td><td>2.46 (n/a)</td><td>1.92 (n/a)</td><td>1.74 (n/a)</td><td>1.15 (n/a)</td><td>6028.80 (n/a)</td><td>4823.06 (n/a)</td><td>5451.20 (n/a)</td><td>2349.00 (n/a)</td><td>1520.17 (n/a)</td><td>1828.44 (n/a)</td><td>1006.67 (n/a)</td><td>787.89 (n/a)</td><td>712.41 (n/a)</td><td>470.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.49 (-9.50%)</td><td>2.87 (-12.81%)</td><td>2.91 <b>(-21.05%)</b></td><td>2.29 (+4.00%)</td><td>0.43 <b>(-37.82%)</b></td><td>10291.00 (-3.84%)</td><td>8371.04 (+11.79%)</td><td>8118.50 <b>(+26.67%)</b></td><td>6757.40 (+10.49%)</td><td>1277.47 <b>(-33.67%)</b></td><td>1986.24 (-9.50%)</td><td>1632.95 (-12.81%)</td><td>1653.24 <b>(-21.05%)</b></td><td>1304.22 (+4.00%)</td><td>245.31 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.86 (n/a)</td><td>3.29 (n/a)</td><td>3.68 (n/a)</td><td>2.20 (n/a)</td><td>0.69 (n/a)</td><td>10702.30 (n/a)</td><td>7488.36 (n/a)</td><td>6409.20 (n/a)</td><td>6115.70 (n/a)</td><td>1925.86 (n/a)</td><td>2194.66 (n/a)</td><td>1872.79 (n/a)</td><td>2094.13 (n/a)</td><td>1254.11 (n/a)</td><td>394.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.02 (-1.26%)</td><td>3.05 (+1.64%)</td><td>2.87 (+0.71%)</td><td>2.23 (-3.45%)</td><td>0.67 (-5.26%)</td><td>7523.80 (+3.58%)</td><td>5704.66 (-1.87%)</td><td>5840.80 (-0.71%)</td><td>4171.60 (+1.28%)</td><td>1243.52 (-0.85%)</td><td>2059.16 (-1.26%)</td><td>1564.13 (+1.64%)</td><td>1470.68 (+0.71%)</td><td>1141.71 (-3.45%)</td><td>341.61 (-5.26%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.07 (n/a)</td><td>3.01 (n/a)</td><td>2.85 (n/a)</td><td>2.31 (n/a)</td><td>0.70 (n/a)</td><td>7264.10 (n/a)</td><td>5813.50 (n/a)</td><td>5882.40 (n/a)</td><td>4118.90 (n/a)</td><td>1254.21 (n/a)</td><td>2085.48 (n/a)</td><td>1538.97 (n/a)</td><td>1460.29 (n/a)</td><td>1182.52 (n/a)</td><td>360.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.20 <b>(+35.38%)</b></td><td>0.81 (+14.93%)</td><td>0.76 (+11.88%)</td><td>0.50 (+0.45%)</td><td>0.26 <b>(+76.47%)</b></td><td>924.50 (-0.45%)</td><td>618.86 (-8.87%)</td><td>604.00 (-10.61%)</td><td>381.90 <b>(-26.15%)</b></td><td>203.64 <b>(+28.57%)</b></td><td>87.85 <b>(+35.38%)</b></td><td>59.10 (+14.93%)</td><td>55.56 (+11.88%)</td><td>36.29 (+0.45%)</td><td>19.38 <b>(+76.47%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.89 (n/a)</td><td>0.70 (n/a)</td><td>0.68 (n/a)</td><td>0.49 (n/a)</td><td>0.15 (n/a)</td><td>928.70 (n/a)</td><td>679.12 (n/a)</td><td>675.70 (n/a)</td><td>517.10 (n/a)</td><td>158.39 (n/a)</td><td>64.89 (n/a)</td><td>51.42 (n/a)</td><td>49.66 (n/a)</td><td>36.13 (n/a)</td><td>10.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.62 (+6.92%)</td><td>0.99 (-11.31%)</td><td>1.03 (+11.88%)</td><td>0.36 <b>(-57.43%)</b></td><td>0.45 <b>(+35.75%)</b></td><td>1823.50 <b>(+134.93%)</b></td><td>845.02 <b>(+34.95%)</b></td><td>636.30 (-10.61%)</td><td>403.40 (-6.47%)</td><td>561.48 <b>(+230.60%)</b></td><td>166.35 (+6.92%)</td><td>101.63 (-11.31%)</td><td>105.47 (+11.88%)</td><td>36.80 <b>(-57.43%)</b></td><td>46.51 <b>(+35.75%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.52 (n/a)</td><td>1.12 (n/a)</td><td>0.92 (n/a)</td><td>0.84 (n/a)</td><td>0.33 (n/a)</td><td>776.20 (n/a)</td><td>626.16 (n/a)</td><td>711.80 (n/a)</td><td>431.30 (n/a)</td><td>169.84 (n/a)</td><td>155.58 (n/a)</td><td>114.59 (n/a)</td><td>94.28 (n/a)</td><td>86.46 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.27 (-11.41%)</td><td>0.99 (-18.04%)</td><td>1.05 (-10.43%)</td><td>0.67 <b>(-31.43%)</b></td><td>0.25 <b>(+46.51%)</b></td><td>1117.00 <b>(+45.84%)</b></td><td>805.74 <b>(+27.02%)</b></td><td>717.40 (+11.64%)</td><td>593.60 (+12.87%)</td><td>221.39 <b>(+142.89%)</b></td><td>141.32 (-11.41%)</td><td>110.17 (-18.04%)</td><td>116.93 (-10.43%)</td><td>75.10 <b>(-31.43%)</b></td><td>27.86 <b>(+46.51%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.43 (n/a)</td><td>1.21 (n/a)</td><td>1.17 (n/a)</td><td>0.98 (n/a)</td><td>0.17 (n/a)</td><td>765.90 (n/a)</td><td>634.34 (n/a)</td><td>642.60 (n/a)</td><td>525.90 (n/a)</td><td>91.15 (n/a)</td><td>159.52 (n/a)</td><td>134.41 (n/a)</td><td>130.55 (n/a)</td><td>109.52 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.63 (-2.33%)</td><td>1.21 <b>(+36.21%)</b></td><td>1.45 <b>(+96.28%)</b></td><td>0.30 <b>(-36.11%)</b></td><td>0.54 (+11.24%)</td><td>3462.50 <b>(+56.51%)</b></td><td>1290.16 (-11.40%)</td><td>723.80 <b>(-49.05%)</b></td><td>644.00 (+2.38%)</td><td>1220.07 <b>(+84.34%)</b></td><td>208.42 (-2.33%)</td><td>154.67 <b>(+36.21%)</b></td><td>185.44 <b>(+96.28%)</b></td><td>38.76 <b>(-36.11%)</b></td><td>69.58 (+11.24%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.67 (n/a)</td><td>0.89 (n/a)</td><td>0.74 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>2212.30 (n/a)</td><td>1456.16 (n/a)</td><td>1420.70 (n/a)</td><td>629.00 (n/a)</td><td>661.84 (n/a)</td><td>213.39 (n/a)</td><td>113.55 (n/a)</td><td>94.48 (n/a)</td><td>60.67 (n/a)</td><td>62.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.02 (-8.95%)</td><td>1.60 (+10.96%)</td><td>1.58 (+18.84%)</td><td>1.30 <b>(+45.18%)</b></td><td>0.30 <b>(-49.40%)</b></td><td>807.10 <b>(-31.12%)</b></td><td>674.98 (-19.07%)</td><td>665.60 (-15.86%)</td><td>518.20 (+9.83%)</td><td>120.69 <b>(-63.21%)</b></td><td>259.02 (-8.95%)</td><td>204.25 (+10.96%)</td><td>201.64 (+18.84%)</td><td>166.29 <b>(+45.18%)</b></td><td>38.11 <b>(-49.40%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.22 (n/a)</td><td>1.44 (n/a)</td><td>1.33 (n/a)</td><td>0.89 (n/a)</td><td>0.59 (n/a)</td><td>1171.80 (n/a)</td><td>833.98 (n/a)</td><td>791.10 (n/a)</td><td>471.80 (n/a)</td><td>328.01 (n/a)</td><td>284.48 (n/a)</td><td>184.07 (n/a)</td><td>169.67 (n/a)</td><td>114.54 (n/a)</td><td>75.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.57 <b>(+21.59%)</b></td><td>1.74 (-9.98%)</td><td>1.57 <b>(-20.45%)</b></td><td>1.30 <b>(-20.23%)</b></td><td>0.52 <b>(+166.36%)</b></td><td>804.20 <b>(+25.34%)</b></td><td>640.58 (+17.19%)</td><td>669.60 <b>(+25.70%)</b></td><td>408.30 (-17.75%)</td><td>164.58 <b>(+177.23%)</b></td><td>328.73 <b>(+21.59%)</b></td><td>223.00 (-9.98%)</td><td>200.44 <b>(-20.45%)</b></td><td>166.89 <b>(-20.23%)</b></td><td>66.74 <b>(+166.36%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.11 (n/a)</td><td>1.94 (n/a)</td><td>1.97 (n/a)</td><td>1.63 (n/a)</td><td>0.20 (n/a)</td><td>641.60 (n/a)</td><td>546.62 (n/a)</td><td>532.70 (n/a)</td><td>496.40 (n/a)</td><td>59.37 (n/a)</td><td>270.37 (n/a)</td><td>247.71 (n/a)</td><td>251.97 (n/a)</td><td>209.20 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.33 (-9.74%)</td><td>0.80 (-10.16%)</td><td>0.61 <b>(-27.49%)</b></td><td>0.49 (+9.66%)</td><td>0.38 (-15.23%)</td><td>2156.20 (-8.81%)</td><td>1556.86 (+5.20%)</td><td>1715.80 <b>(+37.90%)</b></td><td>787.20 (+10.80%)</td><td>638.50 (-15.93%)</td><td>170.50 (-9.74%)</td><td>101.87 (-10.16%)</td><td>78.22 <b>(-27.49%)</b></td><td>62.25 (+9.66%)</td><td>48.70 (-15.23%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.48 (n/a)</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>2364.40 (n/a)</td><td>1479.92 (n/a)</td><td>1244.20 (n/a)</td><td>710.50 (n/a)</td><td>759.47 (n/a)</td><td>188.90 (n/a)</td><td>113.39 (n/a)</td><td>107.88 (n/a)</td><td>56.77 (n/a)</td><td>57.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.61 (-3.23%)</td><td>1.02 (+0.98%)</td><td>1.20 (+9.08%)</td><td>0.30 (-15.53%)</td><td>0.60 <b>(+25.26%)</b></td><td>3551.70 (+18.38%)</td><td>1569.78 (+16.13%)</td><td>877.00 (-8.32%)</td><td>652.30 (+3.34%)</td><td>1253.19 <b>(+32.55%)</b></td><td>205.76 (-3.23%)</td><td>131.14 (+0.98%)</td><td>153.05 (+9.08%)</td><td>37.79 (-15.53%)</td><td>76.17 <b>(+25.26%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.66 (n/a)</td><td>1.01 (n/a)</td><td>1.10 (n/a)</td><td>0.35 (n/a)</td><td>0.48 (n/a)</td><td>3000.20 (n/a)</td><td>1351.78 (n/a)</td><td>956.60 (n/a)</td><td>631.20 (n/a)</td><td>945.47 (n/a)</td><td>212.64 (n/a)</td><td>129.88 (n/a)</td><td>140.31 (n/a)</td><td>44.74 (n/a)</td><td>60.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.31 <b>(-24.87%)</b></td><td>1.10 <b>(-22.16%)</b></td><td>1.16 <b>(-29.96%)</b></td><td>0.72 <b>(+42.81%)</b></td><td>0.22 <b>(-57.53%)</b></td><td>1446.90 <b>(-29.98%)</b></td><td>998.22 (+7.27%)</td><td>905.70 <b>(+42.79%)</b></td><td>798.00 <b>(+33.11%)</b></td><td>256.20 <b>(-59.79%)</b></td><td>168.20 <b>(-24.87%)</b></td><td>140.19 <b>(-22.16%)</b></td><td>148.20 <b>(-29.96%)</b></td><td>92.76 <b>(+42.81%)</b></td><td>28.17 <b>(-57.53%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.75 (n/a)</td><td>1.41 (n/a)</td><td>1.65 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>2066.40 (n/a)</td><td>930.58 (n/a)</td><td>634.30 (n/a)</td><td>599.50 (n/a)</td><td>637.19 (n/a)</td><td>223.88 (n/a)</td><td>180.10 (n/a)</td><td>211.60 (n/a)</td><td>64.95 (n/a)</td><td>66.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.80 <b>(-27.02%)</b></td><td>0.66 (-15.24%)</td><td>0.66 (-14.52%)</td><td>0.50 (-6.52%)</td><td>0.11 <b>(-51.43%)</b></td><td>716.50 (+6.97%)</td><td>563.70 (+12.54%)</td><td>542.10 (+16.98%)</td><td>452.90 <b>(+36.99%)</b></td><td>102.06 <b>(-31.01%)</b></td><td>37.04 <b>(-27.02%)</b></td><td>30.51 (-15.24%)</td><td>30.95 (-14.52%)</td><td>23.41 (-6.52%)</td><td>5.23 <b>(-51.43%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.09 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.54 (n/a)</td><td>0.23 (n/a)</td><td>669.80 (n/a)</td><td>500.88 (n/a)</td><td>463.40 (n/a)</td><td>330.60 (n/a)</td><td>147.93 (n/a)</td><td>50.75 (n/a)</td><td>36.00 (n/a)</td><td>36.21 (n/a)</td><td>25.05 (n/a)</td><td>10.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.03 <b>(+52.95%)</b></td><td>2.43 <b>(+52.58%)</b></td><td>2.82 <b>(+68.39%)</b></td><td>1.69 <b>(+81.19%)</b></td><td>0.66 <b>(+55.48%)</b></td><td>2484.20 <b>(-44.81%)</b></td><td>1848.48 <b>(-34.94%)</b></td><td>1486.30 <b>(-40.61%)</b></td><td>1383.70 <b>(-34.62%)</b></td><td>553.58 <b>(-43.36%)</b></td><td>775.97 <b>(+52.95%)</b></td><td>621.24 <b>(+52.58%)</b></td><td>722.43 <b>(+68.39%)</b></td><td>432.22 <b>(+81.19%)</b></td><td>168.71 <b>(+55.48%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.98 (n/a)</td><td>1.59 (n/a)</td><td>1.68 (n/a)</td><td>0.93 (n/a)</td><td>0.42 (n/a)</td><td>4501.30 (n/a)</td><td>2841.28 (n/a)</td><td>2502.70 (n/a)</td><td>2116.40 (n/a)</td><td>977.29 (n/a)</td><td>507.34 (n/a)</td><td>407.16 (n/a)</td><td>429.03 (n/a)</td><td>238.54 (n/a)</td><td>108.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.99 (+9.58%)</td><td>2.82 (-10.18%)</td><td>3.34 (+2.18%)</td><td>1.20 <b>(-45.39%)</b></td><td>1.15 <b>(+96.24%)</b></td><td>2179.90 <b>(+83.09%)</b></td><td>1129.72 <b>(+30.70%)</b></td><td>785.20 (-2.13%)</td><td>656.50 (-8.74%)</td><td>635.20 <b>(+228.24%)</b></td><td>817.73 (+9.58%)</td><td>577.09 (-10.18%)</td><td>683.76 (+2.18%)</td><td>246.28 <b>(-45.38%)</b></td><td>236.33 <b>(+96.24%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.64 (n/a)</td><td>3.14 (n/a)</td><td>3.27 (n/a)</td><td>2.20 (n/a)</td><td>0.59 (n/a)</td><td>1190.60 (n/a)</td><td>864.38 (n/a)</td><td>802.30 (n/a)</td><td>719.40 (n/a)</td><td>193.52 (n/a)</td><td>746.27 (n/a)</td><td>642.49 (n/a)</td><td>669.17 (n/a)</td><td>450.94 (n/a)</td><td>120.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.61 (+19.95%)</td><td>2.59 (+2.78%)</td><td>2.58 (-10.21%)</td><td>1.84 (+16.61%)</td><td>0.70 (+13.31%)</td><td>4264.50 (-14.24%)</td><td>3211.58 (-3.05%)</td><td>3045.00 (+11.38%)</td><td>2181.10 (-16.63%)</td><td>843.12 (-16.45%)</td><td>1107.65 (+19.95%)</td><td>796.73 (+2.78%)</td><td>793.40 (-10.21%)</td><td>566.51 (+16.61%)</td><td>215.93 (+13.31%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.01 (n/a)</td><td>2.52 (n/a)</td><td>2.88 (n/a)</td><td>1.58 (n/a)</td><td>0.62 (n/a)</td><td>4972.80 (n/a)</td><td>3312.70 (n/a)</td><td>2734.00 (n/a)</td><td>2616.20 (n/a)</td><td>1009.14 (n/a)</td><td>923.46 (n/a)</td><td>775.18 (n/a)</td><td>883.64 (n/a)</td><td>485.83 (n/a)</td><td>190.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.70 (n/a)</td><td>365.36 (n/a)</td><td>323.00 (n/a)</td><td>269.60 (n/a)</td><td>99.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>578.70 (n/a)</td><td>406.08 (n/a)</td><td>469.80 (n/a)</td><td>222.70 (n/a)</td><td>169.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.50 (n/a)</td><td>347.32 (n/a)</td><td>316.90 (n/a)</td><td>292.80 (n/a)</td><td>69.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2408.10 (n/a)</td><td>894.48 (n/a)</td><td>552.80 (n/a)</td><td>307.40 (n/a)</td><td>864.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.90 (n/a)</td><td>485.82 (n/a)</td><td>499.90 (n/a)</td><td>258.80 (n/a)</td><td>141.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.30 (n/a)</td><td>414.10 (n/a)</td><td>481.50 (n/a)</td><td>224.40 (n/a)</td><td>112.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>429.68 (n/a)</td><td>474.80 (n/a)</td><td>270.70 (n/a)</td><td>153.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.00 (n/a)</td><td>381.80 (n/a)</td><td>414.50 (n/a)</td><td>272.70 (n/a)</td><td>84.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>352.68 (n/a)</td><td>293.40 (n/a)</td><td>244.20 (n/a)</td><td>117.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.30 (n/a)</td><td>324.24 (n/a)</td><td>267.80 (n/a)</td><td>218.50 (n/a)</td><td>103.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>438.30 (n/a)</td><td>469.00 (n/a)</td><td>221.50 (n/a)</td><td>132.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>648.20 (n/a)</td><td>487.54 (n/a)</td><td>503.40 (n/a)</td><td>276.10 (n/a)</td><td>133.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.80 (n/a)</td><td>398.58 (n/a)</td><td>323.10 (n/a)</td><td>266.20 (n/a)</td><td>152.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>338.80 (n/a)</td><td>293.90 (n/a)</td><td>274.80 (n/a)</td><td>249.70 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>539.10 (n/a)</td><td>420.04 (n/a)</td><td>446.80 (n/a)</td><td>216.40 (n/a)</td><td>121.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>528.50 (n/a)</td><td>383.58 (n/a)</td><td>349.90 (n/a)</td><td>245.50 (n/a)</td><td>121.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>551.30 (n/a)</td><td>348.92 (n/a)</td><td>303.10 (n/a)</td><td>263.20 (n/a)</td><td>116.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>964.50 (n/a)</td><td>594.54 (n/a)</td><td>553.00 (n/a)</td><td>310.00 (n/a)</td><td>235.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>678.70 (n/a)</td><td>492.30 (n/a)</td><td>541.30 (n/a)</td><td>256.10 (n/a)</td><td>199.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>638.10 (n/a)</td><td>427.52 (n/a)</td><td>459.80 (n/a)</td><td>243.10 (n/a)</td><td>170.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>751.10 (n/a)</td><td>453.60 (n/a)</td><td>463.20 (n/a)</td><td>240.60 (n/a)</td><td>196.88 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>542.60 (n/a)</td><td>473.38 (n/a)</td><td>527.80 (n/a)</td><td>303.00 (n/a)</td><td>101.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>551.10 (n/a)</td><td>431.06 (n/a)</td><td>504.90 (n/a)</td><td>203.20 (n/a)</td><td>144.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>612.80 (n/a)</td><td>502.00 (n/a)</td><td>512.60 (n/a)</td><td>306.20 (n/a)</td><td>117.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.72 <b>(+59.36%)</b></td><td>0.47 <b>(+42.21%)</b></td><td>0.50 <b>(+37.69%)</b></td><td>0.23 <b>(+99.94%)</b></td><td>0.19 <b>(+45.06%)</b></td><td>970.60 <b>(-49.99%)</b></td><td>549.34 <b>(-35.77%)</b></td><td>439.80 <b>(-27.37%)</b></td><td>307.60 <b>(-37.25%)</b></td><td>259.40 <b>(-57.46%)</b></td><td>30.68 <b>(+59.36%)</b></td><td>19.98 <b>(+42.21%)</b></td><td>21.46 <b>(+37.69%)</b></td><td>9.72 <b>(+99.94%)</b></td><td>7.90 <b>(+45.06%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.37 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>1940.70 (n/a)</td><td>855.24 (n/a)</td><td>605.50 (n/a)</td><td>490.20 (n/a)</td><td>609.80 (n/a)</td><td>19.25 (n/a)</td><td>14.05 (n/a)</td><td>15.59 (n/a)</td><td>4.86 (n/a)</td><td>5.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 <b>(-23.98%)</b></td><td>0.38 (-17.50%)</td><td>0.41 (-9.82%)</td><td>0.11 <b>(-68.02%)</b></td><td>0.15 <b>(+34.97%)</b></td><td>1971.60 <b>(+212.75%)</b></td><td>794.92 <b>(+57.48%)</b></td><td>536.20 (+10.88%)</td><td>457.60 <b>(+31.53%)</b></td><td>658.87 <b>(+485.73%)</b></td><td>20.62 <b>(-23.98%)</b></td><td>16.12 (-17.50%)</td><td>17.60 (-9.82%)</td><td>4.79 <b>(-68.02%)</b></td><td>6.50 <b>(+34.96%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.64 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.11 (n/a)</td><td>630.40 (n/a)</td><td>504.78 (n/a)</td><td>483.60 (n/a)</td><td>347.90 (n/a)</td><td>112.49 (n/a)</td><td>27.13 (n/a)</td><td>19.54 (n/a)</td><td>19.52 (n/a)</td><td>14.97 (n/a)</td><td>4.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.31 (+1.52%)</td><td>0.31 (+1.09%)</td><td>0.31 (+1.17%)</td><td>0.30 (+0.17%)</td><td>0.00 <b>(+66.46%)</b></td><td>83327.60 (-0.17%)</td><td>81833.04 (-1.07%)</td><td>81689.60 (-1.16%)</td><td>80651.90 (-1.49%)</td><td>968.08 <b>(+63.98%)</b></td><td>213.01 (+1.52%)</td><td>209.96 (+1.09%)</td><td>210.31 (+1.17%)</td><td>206.17 (+0.17%)</td><td>2.47 <b>(+66.46%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83469.90 (n/a)</td><td>82719.86 (n/a)</td><td>82648.00 (n/a)</td><td>81875.90 (n/a)</td><td>590.37 (n/a)</td><td>209.83 (n/a)</td><td>207.70 (n/a)</td><td>207.87 (n/a)</td><td>205.82 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.15 (-1.44%)</td><td>1.14 (+0.70%)</td><td>1.13 (+0.38%)</td><td>1.13 (+1.90%)</td><td>0.01 <b>(-55.84%)</b></td><td>22345.90 (-1.86%)</td><td>22167.50 (-0.72%)</td><td>22256.20 (-0.38%)</td><td>21930.50 (+1.46%)</td><td>198.01 <b>(-55.97%)</b></td><td>783.38 (-1.44%)</td><td>775.05 (+0.70%)</td><td>771.91 (+0.38%)</td><td>768.81 (+1.90%)</td><td>6.94 <b>(-55.84%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.16 (n/a)</td><td>1.13 (n/a)</td><td>1.13 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22769.50 (n/a)</td><td>22327.54 (n/a)</td><td>22340.90 (n/a)</td><td>21614.40 (n/a)</td><td>449.77 (n/a)</td><td>794.83 (n/a)</td><td>769.70 (n/a)</td><td>768.99 (n/a)</td><td>754.51 (n/a)</td><td>15.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.80 (-0.59%)</td><td>0.77 (-0.68%)</td><td>0.79 (+1.22%)</td><td>0.75 (-1.58%)</td><td>0.02 <b>(+35.85%)</b></td><td>101217.20 (+1.61%)</td><td>97515.12 (+0.72%)</td><td>96105.60 (-1.21%)</td><td>94578.70 (+0.59%)</td><td>2979.72 <b>(+39.26%)</b></td><td>726.59 (-0.59%)</td><td>705.23 (-0.68%)</td><td>715.04 (+1.22%)</td><td>678.93 (-1.58%)</td><td>21.35 <b>(+35.85%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.02 (n/a)</td><td>99615.30 (n/a)</td><td>96818.60 (n/a)</td><td>97278.40 (n/a)</td><td>94019.50 (n/a)</td><td>2139.69 (n/a)</td><td>730.91 (n/a)</td><td>710.05 (n/a)</td><td>706.42 (n/a)</td><td>689.85 (n/a)</td><td>15.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.78 (+0.89%)</td><td>0.77 (+1.57%)</td><td>0.77 (+1.63%)</td><td>0.77 (+2.95%)</td><td>0.00 <b>(-53.52%)</b></td><td>98599.10 (-2.86%)</td><td>97664.26 (-1.56%)</td><td>97507.70 (-1.61%)</td><td>97010.50 (-0.89%)</td><td>624.43 <b>(-55.32%)</b></td><td>708.37 (+0.89%)</td><td>703.65 (+1.57%)</td><td>704.76 (+1.63%)</td><td>696.96 (+2.95%)</td><td>4.48 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101505.00 (n/a)</td><td>99209.78 (n/a)</td><td>99100.60 (n/a)</td><td>97878.70 (n/a)</td><td>1397.59 (n/a)</td><td>702.09 (n/a)</td><td>692.78 (n/a)</td><td>693.43 (n/a)</td><td>677.01 (n/a)</td><td>9.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.90 (+0.12%)</td><td>0.89 (-0.07%)</td><td>0.89 (-0.76%)</td><td>0.87 (+0.46%)</td><td>0.01 <b>(-27.66%)</b></td><td>86566.30 (-0.46%)</td><td>85310.26 (+0.06%)</td><td>85185.00 (+0.77%)</td><td>84093.50 (-0.12%)</td><td>889.95 <b>(-28.01%)</b></td><td>817.18 (+0.12%)</td><td>805.59 (-0.07%)</td><td>806.71 (-0.76%)</td><td>793.84 (+0.46%)</td><td>8.40 <b>(-27.66%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86965.60 (n/a)</td><td>85256.52 (n/a)</td><td>84538.20 (n/a)</td><td>84191.50 (n/a)</td><td>1236.23 (n/a)</td><td>816.23 (n/a)</td><td>806.17 (n/a)</td><td>812.88 (n/a)</td><td>790.19 (n/a)</td><td>11.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.61 (+1.73%)</td><td>5.11 <b>(+22.63%)</b></td><td>5.38 <b>(+39.25%)</b></td><td>4.06 (+15.97%)</td><td>0.63 <b>(-24.43%)</b></td><td>2197.50 (-13.77%)</td><td>1769.00 (-19.60%)</td><td>1655.20 <b>(-28.18%)</b></td><td>1588.80 (-1.70%)</td><td>249.39 <b>(-35.03%)</b></td><td>337.91 (+1.73%)</td><td>307.74 <b>(+22.63%)</b></td><td>324.35 <b>(+39.25%)</b></td><td>244.31 (+15.97%)</td><td>37.80 <b>(-24.43%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.51 (n/a)</td><td>4.17 (n/a)</td><td>3.87 (n/a)</td><td>3.50 (n/a)</td><td>0.83 (n/a)</td><td>2548.30 (n/a)</td><td>2200.18 (n/a)</td><td>2304.80 (n/a)</td><td>1616.30 (n/a)</td><td>383.84 (n/a)</td><td>332.17 (n/a)</td><td>250.94 (n/a)</td><td>232.93 (n/a)</td><td>210.68 (n/a)</td><td>50.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.72 (+11.04%)</td><td>2.75 (-4.70%)</td><td>2.26 (-15.17%)</td><td>2.13 (+15.35%)</td><td>1.11 (+16.54%)</td><td>4185.40 (-13.31%)</td><td>3544.62 (+5.45%)</td><td>3937.30 (+17.88%)</td><td>1889.60 (-9.94%)</td><td>953.58 (-11.01%)</td><td>284.12 (+11.04%)</td><td>165.71 (-4.70%)</td><td>136.35 (-15.17%)</td><td>128.27 (+15.35%)</td><td>66.71 (+16.54%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.25 (n/a)</td><td>2.89 (n/a)</td><td>2.67 (n/a)</td><td>1.85 (n/a)</td><td>0.95 (n/a)</td><td>4828.00 (n/a)</td><td>3361.30 (n/a)</td><td>3340.00 (n/a)</td><td>2098.20 (n/a)</td><td>1071.57 (n/a)</td><td>255.88 (n/a)</td><td>173.88 (n/a)</td><td>160.74 (n/a)</td><td>111.20 (n/a)</td><td>57.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.59 (-3.05%)</td><td>3.66 (-12.47%)</td><td>3.61 (-12.91%)</td><td>2.07 (+4.50%)</td><td>1.47 (-5.47%)</td><td>4307.10 (-4.31%)</td><td>2798.34 (+13.02%)</td><td>2467.80 (+14.82%)</td><td>1595.00 (+3.15%)</td><td>1156.41 (-4.20%)</td><td>336.59 (-3.05%)</td><td>220.26 (-12.47%)</td><td>217.55 (-12.91%)</td><td>124.65 (+4.50%)</td><td>88.60 (-5.47%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.76 (n/a)</td><td>4.18 (n/a)</td><td>4.15 (n/a)</td><td>1.98 (n/a)</td><td>1.56 (n/a)</td><td>4500.90 (n/a)</td><td>2476.00 (n/a)</td><td>2149.30 (n/a)</td><td>1546.30 (n/a)</td><td>1207.09 (n/a)</td><td>347.19 (n/a)</td><td>251.63 (n/a)</td><td>249.78 (n/a)</td><td>119.28 (n/a)</td><td>93.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.59 (+2.46%)</td><td>5.77 (+4.73%)</td><td>5.49 (+1.25%)</td><td>5.22 (+11.84%)</td><td>0.59 (-6.19%)</td><td>6674.40 (-10.59%)</td><td>6095.52 (-4.74%)</td><td>6354.20 (-1.23%)</td><td>5292.30 (-2.40%)</td><td>601.48 (-17.99%)</td><td>405.77 (+2.46%)</td><td>355.18 (+4.73%)</td><td>337.96 (+1.25%)</td><td>321.75 (+11.84%)</td><td>36.53 (-6.19%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.43 (n/a)</td><td>5.51 (n/a)</td><td>5.42 (n/a)</td><td>4.67 (n/a)</td><td>0.63 (n/a)</td><td>7464.90 (n/a)</td><td>6398.70 (n/a)</td><td>6433.40 (n/a)</td><td>5422.50 (n/a)</td><td>733.40 (n/a)</td><td>396.04 (n/a)</td><td>339.16 (n/a)</td><td>333.80 (n/a)</td><td>287.68 (n/a)</td><td>38.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.25 (+1.16%)</td><td>4.77 (-1.54%)</td><td>4.89 (+2.60%)</td><td>3.84 (-14.45%)</td><td>0.56 <b>(+72.85%)</b></td><td>9080.60 (+16.89%)</td><td>7397.86 (+2.47%)</td><td>7126.00 (-2.54%)</td><td>6639.90 (-1.15%)</td><td>982.49 <b>(+105.21%)</b></td><td>323.42 (+1.16%)</td><td>293.93 (-1.54%)</td><td>301.36 (+2.60%)</td><td>236.49 (-14.45%)</td><td>34.45 <b>(+72.85%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.19 (n/a)</td><td>4.85 (n/a)</td><td>4.77 (n/a)</td><td>4.49 (n/a)</td><td>0.32 (n/a)</td><td>7768.80 (n/a)</td><td>7219.40 (n/a)</td><td>7311.50 (n/a)</td><td>6717.10 (n/a)</td><td>478.78 (n/a)</td><td>319.70 (n/a)</td><td>298.52 (n/a)</td><td>293.71 (n/a)</td><td>276.43 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.35 (+5.46%)</td><td>5.38 (-1.34%)</td><td>5.25 (-4.05%)</td><td>4.68 (-4.94%)</td><td>0.73 <b>(+87.06%)</b></td><td>7456.90 (+5.20%)</td><td>6578.50 (+2.41%)</td><td>6638.80 (+4.22%)</td><td>5493.30 (-5.18%)</td><td>872.26 <b>(+89.20%)</b></td><td>390.93 (+5.46%)</td><td>331.21 (-1.34%)</td><td>323.47 (-4.05%)</td><td>287.98 (-4.94%)</td><td>45.11 <b>(+87.06%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.02 (n/a)</td><td>5.45 (n/a)</td><td>5.47 (n/a)</td><td>4.92 (n/a)</td><td>0.39 (n/a)</td><td>7088.20 (n/a)</td><td>6423.48 (n/a)</td><td>6370.10 (n/a)</td><td>5793.30 (n/a)</td><td>461.02 (n/a)</td><td>370.68 (n/a)</td><td>335.70 (n/a)</td><td>337.12 (n/a)</td><td>302.97 (n/a)</td><td>24.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.78 (+0.44%)</td><td>0.76 (-0.11%)</td><td>0.75 (-1.25%)</td><td>0.74 (+1.28%)</td><td>0.02 (-7.85%)</td><td>102190.80 (-1.27%)</td><td>99946.48 (+0.11%)</td><td>100575.60 (+1.27%)</td><td>97099.50 (-0.44%)</td><td>2068.15 (-9.74%)</td><td>707.72 (+0.44%)</td><td>687.80 (-0.11%)</td><td>683.26 (-1.25%)</td><td>672.46 (+1.28%)</td><td>14.33 (-7.86%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103500.60 (n/a)</td><td>99839.40 (n/a)</td><td>99318.30 (n/a)</td><td>97527.60 (n/a)</td><td>2291.42 (n/a)</td><td>704.62 (n/a)</td><td>688.59 (n/a)</td><td>691.91 (n/a)</td><td>663.95 (n/a)</td><td>15.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.77 (-0.26%)</td><td>0.76 (-0.69%)</td><td>0.75 (-1.47%)</td><td>0.74 (-1.17%)</td><td>0.01 (+17.77%)</td><td>101416.50 (+1.18%)</td><td>99639.76 (+0.70%)</td><td>100033.00 (+1.50%)</td><td>97977.80 (+0.26%)</td><td>1370.88 (+19.14%)</td><td>701.38 (-0.26%)</td><td>689.78 (-0.69%)</td><td>686.97 (-1.47%)</td><td>677.60 (-1.17%)</td><td>9.49 (+17.77%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100231.20 (n/a)</td><td>98948.08 (n/a)</td><td>98557.70 (n/a)</td><td>97725.50 (n/a)</td><td>1150.68 (n/a)</td><td>703.19 (n/a)</td><td>694.58 (n/a)</td><td>697.25 (n/a)</td><td>685.61 (n/a)</td><td>8.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.90 (+0.08%)</td><td>0.90 (+0.81%)</td><td>0.90 (+0.40%)</td><td>0.89 (+1.84%)</td><td>0.01 <b>(-50.99%)</b></td><td>84949.90 (-1.81%)</td><td>84337.92 (-0.81%)</td><td>84116.00 (-0.40%)</td><td>83612.40 (-0.08%)</td><td>581.04 <b>(-51.91%)</b></td><td>821.88 (+0.08%)</td><td>814.84 (+0.81%)</td><td>816.96 (+0.40%)</td><td>808.94 (+1.84%)</td><td>5.61 <b>(-50.99%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86512.20 (n/a)</td><td>85027.44 (n/a)</td><td>84453.30 (n/a)</td><td>83676.50 (n/a)</td><td>1208.26 (n/a)</td><td>821.25 (n/a)</td><td>808.33 (n/a)</td><td>813.70 (n/a)</td><td>794.33 (n/a)</td><td>11.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.37 (+2.57%)</td><td>2.73 (+12.64%)</td><td>2.09 (+7.70%)</td><td>1.93 (+14.24%)</td><td>1.08 (-0.83%)</td><td>4174.50 (-12.47%)</td><td>3282.38 (-12.50%)</td><td>3853.70 (-7.15%)</td><td>1843.20 (-2.50%)</td><td>1062.88 (-13.19%)</td><td>1146.91 (+2.57%)</td><td>716.01 (+12.64%)</td><td>548.54 (+7.70%)</td><td>506.39 (+14.24%)</td><td>281.93 (-0.83%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.26 (n/a)</td><td>2.42 (n/a)</td><td>1.94 (n/a)</td><td>1.69 (n/a)</td><td>1.08 (n/a)</td><td>4769.00 (n/a)</td><td>3751.46 (n/a)</td><td>4150.50 (n/a)</td><td>1890.50 (n/a)</td><td>1224.31 (n/a)</td><td>1118.18 (n/a)</td><td>635.64 (n/a)</td><td>509.32 (n/a)</td><td>443.26 (n/a)</td><td>284.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 <b>(+26.00%)</b></td><td>0.20 (+10.57%)</td><td>0.18 (+4.11%)</td><td>0.15 (-1.98%)</td><td>0.05 <b>(+80.80%)</b></td><td>8270.90 (+2.03%)</td><td>6512.32 (-7.30%)</td><td>6798.00 (-3.95%)</td><td>4454.70 <b>(-20.63%)</b></td><td>1379.15 <b>(+41.70%)</b></td><td>15.06 <b>(+26.00%)</b></td><td>10.74 (+10.57%)</td><td>9.87 (+4.11%)</td><td>8.11 (-1.98%)</td><td>2.61 <b>(+80.80%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>8106.70 (n/a)</td><td>7025.36 (n/a)</td><td>7077.20 (n/a)</td><td>5612.80 (n/a)</td><td>973.29 (n/a)</td><td>11.96 (n/a)</td><td>9.71 (n/a)</td><td>9.48 (n/a)</td><td>8.28 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.81 (n/a)</td><td>3.61 (n/a)</td><td>3.63 (n/a)</td><td>3.28 (n/a)</td><td>0.20 (n/a)</td><td>3.81 (n/a)</td><td>3.61 (n/a)</td><td>3.63 (n/a)</td><td>3.28 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.68 (+1.51%)</td><td>6.95 (+6.65%)</td><td>6.98 (+1.32%)</td><td>5.89 <b>(+22.94%)</b></td><td>0.71 <b>(-39.28%)</b></td><td>7.67 (+1.51%)</td><td>6.94 (+6.65%)</td><td>6.97 (+1.32%)</td><td>5.89 <b>(+22.94%)</b></td><td>0.71 <b>(-39.28%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.56 (n/a)</td><td>6.51 (n/a)</td><td>6.89 (n/a)</td><td>4.79 (n/a)</td><td>1.17 (n/a)</td><td>7.56 (n/a)</td><td>6.51 (n/a)</td><td>6.88 (n/a)</td><td>4.79 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>14.51 (+11.53%)</td><td>10.38 (-3.89%)</td><td>8.28 <b>(-26.68%)</b></td><td>7.31 (-14.24%)</td><td>3.40 <b>(+94.84%)</b></td><td>14.50 (+11.53%)</td><td>10.38 (-3.89%)</td><td>8.27 <b>(-26.68%)</b></td><td>7.30 (-14.24%)</td><td>3.40 <b>(+94.84%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>13.01 (n/a)</td><td>10.80 (n/a)</td><td>11.29 (n/a)</td><td>8.52 (n/a)</td><td>1.75 (n/a)</td><td>13.00 (n/a)</td><td>10.80 (n/a)</td><td>11.28 (n/a)</td><td>8.51 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.89 (n/a)</td><td>3.66 (n/a)</td><td>3.74 (n/a)</td><td>3.38 (n/a)</td><td>0.20 (n/a)</td><td>3.88 (n/a)</td><td>3.66 (n/a)</td><td>3.73 (n/a)</td><td>3.38 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.42 (+2.08%)</td><td>6.52 (+1.38%)</td><td>6.16 (-7.85%)</td><td>5.79 (+13.56%)</td><td>0.79 (-5.97%)</td><td>7.42 (+2.08%)</td><td>6.52 (+1.38%)</td><td>6.16 (-7.85%)</td><td>5.78 (+13.56%)</td><td>0.79 (-5.97%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.27 (n/a)</td><td>6.43 (n/a)</td><td>6.69 (n/a)</td><td>5.10 (n/a)</td><td>0.84 (n/a)</td><td>7.27 (n/a)</td><td>6.43 (n/a)</td><td>6.68 (n/a)</td><td>5.09 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>13.87 <b>(+33.31%)</b></td><td>9.47 (-1.78%)</td><td>8.42 (-14.45%)</td><td>8.19 (-3.78%)</td><td>2.46 <b>(+242.76%)</b></td><td>13.86 <b>(+33.31%)</b></td><td>9.47 (-1.78%)</td><td>8.41 (-14.45%)</td><td>8.19 (-3.78%)</td><td>2.46 <b>(+242.76%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>10.41 (n/a)</td><td>9.65 (n/a)</td><td>9.84 (n/a)</td><td>8.51 (n/a)</td><td>0.72 (n/a)</td><td>10.40 (n/a)</td><td>9.64 (n/a)</td><td>9.84 (n/a)</td><td>8.51 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.05 (+3.07%)</td><td>2.49 (-9.91%)</td><td>2.82 (+2.58%)</td><td>1.03 <b>(-60.63%)</b></td><td>0.83 <b>(+567.00%)</b></td><td>3.04 (+3.07%)</td><td>2.48 (-9.91%)</td><td>2.82 (+2.58%)</td><td>1.03 <b>(-60.63%)</b></td><td>0.83 <b>(+567.00%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.96 (n/a)</td><td>2.76 (n/a)</td><td>2.75 (n/a)</td><td>2.61 (n/a)</td><td>0.12 (n/a)</td><td>2.95 (n/a)</td><td>2.76 (n/a)</td><td>2.75 (n/a)</td><td>2.61 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.53 (+4.20%)</td><td>0.48 <b>(+43.62%)</b></td><td>0.50 <b>(+46.59%)</b></td><td>0.33 <b>(+158.45%)</b></td><td>0.08 <b>(-39.79%)</b></td><td>0.52 (+4.20%)</td><td>0.47 <b>(+43.62%)</b></td><td>0.50 <b>(+46.59%)</b></td><td>0.33 <b>(+158.45%)</b></td><td>0.08 <b>(-39.79%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.77 <b>(+22.97%)</b></td><td>0.66 <b>(+73.62%)</b></td><td>0.72 <b>(+49.58%)</b></td><td>0.39 <b>(+178.57%)</b></td><td>0.15 <b>(-31.51%)</b></td><td>0.76 <b>(+22.97%)</b></td><td>0.65 <b>(+73.62%)</b></td><td>0.71 <b>(+49.58%)</b></td><td>0.38 <b>(+178.57%)</b></td><td>0.15 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.62 (n/a)</td><td>0.38 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>0.22 (n/a)</td><td>0.62 (n/a)</td><td>0.38 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.53 (+5.88%)</td><td>1.49 (+9.26%)</td><td>1.57 (+16.07%)</td><td>0.43 (-11.09%)</td><td>1.03 <b>(+38.79%)</b></td><td>2.49 (+5.88%)</td><td>1.47 (+9.26%)</td><td>1.55 (+16.07%)</td><td>0.42 (-11.09%)</td><td>1.02 <b>(+38.79%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.39 (n/a)</td><td>1.37 (n/a)</td><td>1.35 (n/a)</td><td>0.49 (n/a)</td><td>0.74 (n/a)</td><td>2.35 (n/a)</td><td>1.34 (n/a)</td><td>1.33 (n/a)</td><td>0.48 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.90 (n/a)</td><td>415.64 (n/a)</td><td>400.70 (n/a)</td><td>273.10 (n/a)</td><td>115.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>424.90 (n/a)</td><td>314.50 (n/a)</td><td>329.00 (n/a)</td><td>171.20 (n/a)</td><td>96.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>356.02 (n/a)</td><td>295.70 (n/a)</td><td>172.20 (n/a)</td><td>174.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.20 (n/a)</td><td>377.90 (n/a)</td><td>343.20 (n/a)</td><td>290.80 (n/a)</td><td>94.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>648.00 (n/a)</td><td>487.06 (n/a)</td><td>464.50 (n/a)</td><td>318.80 (n/a)</td><td>155.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>662.60 (n/a)</td><td>461.42 (n/a)</td><td>483.00 (n/a)</td><td>262.60 (n/a)</td><td>186.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.00 (n/a)</td><td>398.98 (n/a)</td><td>427.30 (n/a)</td><td>205.80 (n/a)</td><td>136.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>401.16 (n/a)</td><td>405.40 (n/a)</td><td>292.90 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>416.42 (n/a)</td><td>486.00 (n/a)</td><td>230.00 (n/a)</td><td>153.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.10 (n/a)</td><td>419.84 (n/a)</td><td>503.20 (n/a)</td><td>238.20 (n/a)</td><td>160.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.20 (n/a)</td><td>331.32 (n/a)</td><td>318.00 (n/a)</td><td>227.50 (n/a)</td><td>105.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>405.64 (n/a)</td><td>346.70 (n/a)</td><td>287.40 (n/a)</td><td>111.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.20 (n/a)</td><td>387.80 (n/a)</td><td>351.50 (n/a)</td><td>294.40 (n/a)</td><td>95.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>652.80 (n/a)</td><td>505.14 (n/a)</td><td>505.20 (n/a)</td><td>292.30 (n/a)</td><td>152.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>618.40 (n/a)</td><td>450.86 (n/a)</td><td>469.50 (n/a)</td><td>271.50 (n/a)</td><td>129.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.50 (n/a)</td><td>456.14 (n/a)</td><td>535.40 (n/a)</td><td>234.90 (n/a)</td><td>149.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1041.80 (n/a)</td><td>474.90 (n/a)</td><td>312.70 (n/a)</td><td>234.70 (n/a)</td><td>332.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>544.30 (n/a)</td><td>452.14 (n/a)</td><td>486.20 (n/a)</td><td>266.70 (n/a)</td><td>108.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>834.30 (n/a)</td><td>544.34 (n/a)</td><td>573.10 (n/a)</td><td>310.90 (n/a)</td><td>228.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>502.60 (n/a)</td><td>330.96 (n/a)</td><td>310.30 (n/a)</td><td>255.90 (n/a)</td><td>99.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1891.60 (n/a)</td><td>733.38 (n/a)</td><td>626.50 (n/a)</td><td>209.90 (n/a)</td><td>675.52 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>751.60 (n/a)</td><td>506.76 (n/a)</td><td>518.70 (n/a)</td><td>235.40 (n/a)</td><td>183.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1840.70 (n/a)</td><td>713.60 (n/a)</td><td>481.20 (n/a)</td><td>245.80 (n/a)</td><td>639.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>502.40 (n/a)</td><td>412.06 (n/a)</td><td>392.80 (n/a)</td><td>278.10 (n/a)</td><td>92.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+6.40%)</td><td>0.01 (-10.81%)</td><td>0.01 <b>(-35.49%)</b></td><td>0.01 <b>(-20.87%)</b></td><td>0.00 <b>(+26.78%)</b></td><td>591.20 <b>(+26.38%)</b></td><td>404.06 (+17.71%)</td><td>438.50 <b>(+55.00%)</b></td><td>244.30 (-6.04%)</td><td>145.92 <b>(+43.36%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.80 (n/a)</td><td>343.26 (n/a)</td><td>282.90 (n/a)</td><td>260.00 (n/a)</td><td>101.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-1.61%)</td><td>0.01 (-2.63%)</td><td>0.01 (+0.14%)</td><td>0.01 (-18.43%)</td><td>0.00 (+3.41%)</td><td>649.10 <b>(+22.59%)</b></td><td>401.46 (+5.56%)</td><td>412.20 (-0.15%)</td><td>243.20 (+1.63%)</td><td>166.48 <b>(+26.78%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.50 (n/a)</td><td>380.32 (n/a)</td><td>412.80 (n/a)</td><td>239.30 (n/a)</td><td>131.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+16.58%)</td><td>0.01 (+16.48%)</td><td>0.01 <b>(+60.64%)</b></td><td>0.00 <b>(-42.42%)</b></td><td>0.01 <b>(+29.24%)</b></td><td>1802.50 <b>(+73.67%)</b></td><td>608.40 (+19.57%)</td><td>281.10 <b>(-37.74%)</b></td><td>205.40 (-14.20%)</td><td>678.05 <b>(+110.14%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1037.90 (n/a)</td><td>508.84 (n/a)</td><td>451.50 (n/a)</td><td>239.40 (n/a)</td><td>322.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+15.21%)</td><td>0.01 <b>(+26.57%)</b></td><td>0.02 <b>(+66.45%)</b></td><td>0.01 (-10.42%)</td><td>0.00 <b>(+21.02%)</b></td><td>547.30 (+11.63%)</td><td>323.62 (-18.77%)</td><td>268.90 <b>(-39.92%)</b></td><td>246.60 (-13.23%)</td><td>126.05 <b>(+25.21%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.30 (n/a)</td><td>398.42 (n/a)</td><td>447.60 (n/a)</td><td>284.20 (n/a)</td><td>100.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+9.36%)</td><td>0.01 (+8.80%)</td><td>0.01 (+15.50%)</td><td>0.01 (+3.29%)</td><td>0.01 (+11.65%)</td><td>595.20 (-3.19%)</td><td>398.72 (-6.91%)</td><td>412.80 (-13.42%)</td><td>225.60 (-8.55%)</td><td>163.48 (-0.76%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>614.80 (n/a)</td><td>428.32 (n/a)</td><td>476.80 (n/a)</td><td>246.70 (n/a)</td><td>164.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 <b>(-47.53%)</b></td><td>0.01 <b>(-29.68%)</b></td><td>0.01 <b>(-21.05%)</b></td><td>0.01 (-19.69%)</td><td>0.00 <b>(-66.36%)</b></td><td>672.80 <b>(+24.50%)</b></td><td>562.50 <b>(+32.15%)</b></td><td>591.50 <b>(+26.66%)</b></td><td>436.60 <b>(+90.57%)</b></td><td>103.35 <b>(-21.06%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>540.40 (n/a)</td><td>425.64 (n/a)</td><td>467.00 (n/a)</td><td>229.10 (n/a)</td><td>130.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-14.02%)</td><td>0.03 (-1.82%)</td><td>0.03 (-5.73%)</td><td>0.02 <b>(+27.03%)</b></td><td>0.01 <b>(-46.71%)</b></td><td>422.00 <b>(-21.28%)</b></td><td>316.96 (-7.68%)</td><td>308.50 (+6.09%)</td><td>233.80 (+16.32%)</td><td>68.77 <b>(-51.88%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.10 (n/a)</td><td>343.34 (n/a)</td><td>290.80 (n/a)</td><td>201.00 (n/a)</td><td>142.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(-41.52%)</b></td><td>0.02 <b>(-28.92%)</b></td><td>0.02 <b>(-22.04%)</b></td><td>0.01 (-19.12%)</td><td>0.00 <b>(-57.98%)</b></td><td>578.80 <b>(+23.62%)</b></td><td>485.82 <b>(+36.50%)</b></td><td>476.00 <b>(+28.27%)</b></td><td>413.10 <b>(+71.06%)</b></td><td>75.62 (-10.92%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.20 (n/a)</td><td>355.92 (n/a)</td><td>371.10 (n/a)</td><td>241.50 (n/a)</td><td>84.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-17.07%)</td><td>0.02 <b>(-36.52%)</b></td><td>0.02 <b>(-47.28%)</b></td><td>0.02 <b>(-32.54%)</b></td><td>0.01 (+7.72%)</td><td>518.80 <b>(+48.23%)</b></td><td>426.42 <b>(+63.52%)</b></td><td>463.30 <b>(+89.64%)</b></td><td>238.40 <b>(+20.59%)</b></td><td>109.51 <b>(+80.55%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>350.00 (n/a)</td><td>260.78 (n/a)</td><td>244.30 (n/a)</td><td>197.70 (n/a)</td><td>60.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (+2.72%)</td><td>0.02 (-8.11%)</td><td>0.02 <b>(-33.60%)</b></td><td>0.01 <b>(+212.73%)</b></td><td>0.01 <b>(-25.56%)</b></td><td>585.70 <b>(-68.02%)</b></td><td>456.02 <b>(-28.06%)</b></td><td>504.20 <b>(+50.60%)</b></td><td>237.30 (-2.63%)</td><td>133.22 <b>(-80.25%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1831.50 (n/a)</td><td>633.86 (n/a)</td><td>334.80 (n/a)</td><td>243.70 (n/a)</td><td>674.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-17.10%)</td><td>0.03 (+19.03%)</td><td>0.03 <b>(+47.23%)</b></td><td>0.02 <b>(+25.36%)</b></td><td>0.01 <b>(-42.26%)</b></td><td>468.00 <b>(-20.23%)</b></td><td>332.84 <b>(-23.71%)</b></td><td>291.50 <b>(-32.08%)</b></td><td>237.40 <b>(+20.63%)</b></td><td>90.57 <b>(-41.23%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.70 (n/a)</td><td>436.30 (n/a)</td><td>429.20 (n/a)</td><td>196.80 (n/a)</td><td>154.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(-20.68%)</b></td><td>0.02 (-11.55%)</td><td>0.02 (-4.51%)</td><td>0.01 <b>(+31.26%)</b></td><td>0.01 <b>(-43.01%)</b></td><td>609.40 <b>(-23.81%)</b></td><td>470.14 (-0.91%)</td><td>532.80 (+4.74%)</td><td>301.50 <b>(+26.05%)</b></td><td>136.93 <b>(-41.06%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>799.80 (n/a)</td><td>474.44 (n/a)</td><td>508.70 (n/a)</td><td>239.20 (n/a)</td><td>232.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-10.69%)</td><td>0.02 (-8.90%)</td><td>0.02 (-5.05%)</td><td>0.01 (-10.35%)</td><td>0.01 (-14.11%)</td><td>621.00 (+11.53%)</td><td>443.70 (+9.01%)</td><td>451.40 (+5.32%)</td><td>265.40 (+11.98%)</td><td>127.49 (+7.06%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.80 (n/a)</td><td>407.04 (n/a)</td><td>428.60 (n/a)</td><td>237.00 (n/a)</td><td>119.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-4.17%)</td><td>0.02 (+0.49%)</td><td>0.01 (-12.39%)</td><td>0.01 (+5.17%)</td><td>0.01 (-4.75%)</td><td>632.00 (-4.91%)</td><td>489.54 (-0.66%)</td><td>615.00 (+14.14%)</td><td>211.20 (+4.35%)</td><td>190.98 (+3.15%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.60 (n/a)</td><td>492.78 (n/a)</td><td>538.80 (n/a)</td><td>202.40 (n/a)</td><td>185.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 <b>(-28.63%)</b></td><td>0.04 <b>(-38.98%)</b></td><td>0.03 <b>(-44.56%)</b></td><td>0.02 <b>(-24.46%)</b></td><td>0.01 <b>(-32.27%)</b></td><td>678.40 <b>(+32.37%)</b></td><td>485.16 <b>(+60.34%)</b></td><td>470.40 <b>(+80.37%)</b></td><td>302.40 <b>(+40.13%)</b></td><td>134.77 (+13.04%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>512.50 (n/a)</td><td>302.58 (n/a)</td><td>260.80 (n/a)</td><td>215.80 (n/a)</td><td>119.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-8.23%)</td><td>0.04 <b>(-20.12%)</b></td><td>0.03 <b>(-40.73%)</b></td><td>0.03 (-15.57%)</td><td>0.02 (+0.05%)</td><td>626.90 (+18.44%)</td><td>443.94 <b>(+27.79%)</b></td><td>475.40 <b>(+68.70%)</b></td><td>260.60 (+8.99%)</td><td>152.21 <b>(+25.71%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.30 (n/a)</td><td>347.40 (n/a)</td><td>281.80 (n/a)</td><td>239.10 (n/a)</td><td>121.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (+1.69%)</td><td>0.05 (-3.44%)</td><td>0.05 (-13.09%)</td><td>0.04 <b>(+35.23%)</b></td><td>0.02 (-6.80%)</td><td>467.80 <b>(-26.05%)</b></td><td>346.60 (-0.81%)</td><td>311.80 (+15.06%)</td><td>224.10 (-1.67%)</td><td>114.26 <b>(-30.83%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>632.60 (n/a)</td><td>349.44 (n/a)</td><td>271.00 (n/a)</td><td>227.90 (n/a)</td><td>165.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-12.68%)</td><td>0.04 <b>(-22.02%)</b></td><td>0.03 <b>(-40.22%)</b></td><td>0.03 (-0.56%)</td><td>0.01 (-16.01%)</td><td>543.30 (+0.56%)</td><td>422.88 <b>(+25.89%)</b></td><td>483.60 <b>(+67.28%)</b></td><td>249.10 (+14.53%)</td><td>123.48 (-4.66%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>540.30 (n/a)</td><td>335.90 (n/a)</td><td>289.10 (n/a)</td><td>217.50 (n/a)</td><td>129.52 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(-30.09%)</b></td><td>0.03 <b>(-27.24%)</b></td><td>0.03 (-15.16%)</td><td>0.03 (-10.75%)</td><td>0.01 <b>(-58.51%)</b></td><td>578.10 (+12.06%)</td><td>501.50 <b>(+30.24%)</b></td><td>497.40 (+17.87%)</td><td>377.00 <b>(+43.02%)</b></td><td>78.38 <b>(-30.85%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>515.90 (n/a)</td><td>385.06 (n/a)</td><td>422.00 (n/a)</td><td>263.60 (n/a)</td><td>113.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(-44.04%)</b></td><td>0.03 <b>(-29.14%)</b></td><td>0.03 (-14.86%)</td><td>0.03 (-11.92%)</td><td>0.00 <b>(-86.31%)</b></td><td>560.90 (+13.54%)</td><td>535.54 <b>(+32.67%)</b></td><td>552.00 (+17.45%)</td><td>492.90 <b>(+78.72%)</b></td><td>29.50 <b>(-72.37%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>494.00 (n/a)</td><td>403.66 (n/a)</td><td>470.00 (n/a)</td><td>275.80 (n/a)</td><td>106.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (-7.54%)</td><td>0.07 (-13.87%)</td><td>0.06 <b>(-26.90%)</b></td><td>0.05 (+9.60%)</td><td>0.03 (-15.69%)</td><td>605.60 (-8.75%)</td><td>497.78 (+11.46%)</td><td>553.20 <b>(+36.80%)</b></td><td>268.50 (+8.18%)</td><td>136.85 <b>(-21.87%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>663.70 (n/a)</td><td>446.60 (n/a)</td><td>404.40 (n/a)</td><td>248.20 (n/a)</td><td>175.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (+14.68%)</td><td>0.08 <b>(-27.85%)</b></td><td>0.07 <b>(-44.49%)</b></td><td>0.05 <b>(-41.60%)</b></td><td>0.04 <b>(+65.90%)</b></td><td>726.20 <b>(+71.23%)</b></td><td>506.62 <b>(+56.24%)</b></td><td>502.00 <b>(+80.12%)</b></td><td>220.40 (-12.82%)</td><td>192.08 <b>(+131.50%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>424.10 (n/a)</td><td>324.26 (n/a)</td><td>278.70 (n/a)</td><td>252.80 (n/a)</td><td>82.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 <b>(-31.14%)</b></td><td>0.07 <b>(-37.80%)</b></td><td>0.06 <b>(-55.33%)</b></td><td>0.06 (-9.19%)</td><td>0.02 <b>(-59.52%)</b></td><td>586.70 (+10.12%)</td><td>500.28 <b>(+44.61%)</b></td><td>530.30 <b>(+123.85%)</b></td><td>335.40 <b>(+45.19%)</b></td><td>96.34 <b>(-37.15%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>532.80 (n/a)</td><td>345.94 (n/a)</td><td>236.90 (n/a)</td><td>231.00 (n/a)</td><td>153.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-3.91%)</td><td>0.09 (+3.01%)</td><td>0.09 (+13.13%)</td><td>0.06 <b>(+24.94%)</b></td><td>0.03 <b>(-31.06%)</b></td><td>507.40 (-19.97%)</td><td>372.06 (-10.22%)</td><td>350.60 (-11.60%)</td><td>255.90 (+4.07%)</td><td>101.58 <b>(-39.87%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>634.00 (n/a)</td><td>414.42 (n/a)</td><td>396.60 (n/a)</td><td>245.90 (n/a)</td><td>168.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 <b>(+58.59%)</b></td><td>0.08 (+13.45%)</td><td>0.06 (-1.56%)</td><td>0.06 (+12.03%)</td><td>0.03 <b>(+173.70%)</b></td><td>572.90 (-10.74%)</td><td>472.02 (-6.30%)</td><td>511.40 (+1.59%)</td><td>258.00 <b>(-36.95%)</b></td><td>123.14 <b>(+42.40%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>641.80 (n/a)</td><td>503.74 (n/a)</td><td>503.40 (n/a)</td><td>409.20 (n/a)</td><td>86.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-0.47%)</td><td>0.01 (+8.23%)</td><td>0.02 <b>(+47.72%)</b></td><td>0.01 (-5.86%)</td><td>0.00 (+17.33%)</td><td>512.00 (+6.22%)</td><td>344.90 (-4.67%)</td><td>263.10 <b>(-32.31%)</b></td><td>244.90 (+0.49%)</td><td>126.48 <b>(+26.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.00 (n/a)</td><td>361.80 (n/a)</td><td>388.70 (n/a)</td><td>243.70 (n/a)</td><td>100.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+13.91%)</td><td>0.01 (+13.64%)</td><td>0.01 <b>(+48.85%)</b></td><td>0.01 (-7.49%)</td><td>0.00 <b>(+49.15%)</b></td><td>551.30 (+8.08%)</td><td>383.60 (-6.68%)</td><td>299.90 <b>(-32.82%)</b></td><td>245.00 (-12.19%)</td><td>144.11 <b>(+51.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.10 (n/a)</td><td>411.04 (n/a)</td><td>446.40 (n/a)</td><td>279.00 (n/a)</td><td>95.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+18.40%)</td><td>0.01 (+9.77%)</td><td>0.01 (+10.65%)</td><td>0.01 <b>(+33.17%)</b></td><td>0.00 (+3.93%)</td><td>510.90 <b>(-24.90%)</b></td><td>385.12 (-11.32%)</td><td>367.40 (-9.62%)</td><td>238.80 (-15.53%)</td><td>115.09 <b>(-29.67%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>680.30 (n/a)</td><td>434.28 (n/a)</td><td>406.50 (n/a)</td><td>282.70 (n/a)</td><td>163.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-9.71%)</td><td>0.01 (+2.09%)</td><td>0.01 (-8.95%)</td><td>0.01 <b>(+84.58%)</b></td><td>0.00 <b>(-35.06%)</b></td><td>557.70 <b>(-45.82%)</b></td><td>332.22 <b>(-21.54%)</b></td><td>296.20 (+9.83%)</td><td>239.80 (+10.76%)</td><td>128.72 <b>(-62.35%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1029.40 (n/a)</td><td>423.44 (n/a)</td><td>269.70 (n/a)</td><td>216.50 (n/a)</td><td>341.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(+31.49%)</b></td><td>0.01 (+17.91%)</td><td>0.02 (+17.70%)</td><td>0.01 (+11.48%)</td><td>0.00 <b>(+66.28%)</b></td><td>438.00 (-10.28%)</td><td>302.04 (-11.27%)</td><td>257.00 (-15.04%)</td><td>199.90 <b>(-23.96%)</b></td><td>107.11 (+15.64%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.20 (n/a)</td><td>340.42 (n/a)</td><td>302.50 (n/a)</td><td>262.90 (n/a)</td><td>92.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-2.06%)</td><td>0.01 (+7.29%)</td><td>0.01 (+0.45%)</td><td>0.01 <b>(+27.11%)</b></td><td>0.00 <b>(-20.66%)</b></td><td>449.10 <b>(-21.33%)</b></td><td>336.60 (-12.20%)</td><td>294.90 (-0.47%)</td><td>238.50 (+2.10%)</td><td>96.53 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.90 (n/a)</td><td>383.36 (n/a)</td><td>296.30 (n/a)</td><td>233.60 (n/a)</td><td>153.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(+63.08%)</b></td><td>0.01 <b>(+35.60%)</b></td><td>0.01 (+18.21%)</td><td>0.01 <b>(+22.77%)</b></td><td>0.00 <b>(+153.98%)</b></td><td>561.00 (-18.54%)</td><td>418.48 <b>(-21.23%)</b></td><td>445.40 (-15.40%)</td><td>260.20 <b>(-38.68%)</b></td><td>136.71 <b>(+28.42%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>688.70 (n/a)</td><td>531.26 (n/a)</td><td>526.50 (n/a)</td><td>424.30 (n/a)</td><td>106.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (-2.72%)</td><td>0.01 (-18.05%)</td><td>0.01 (-10.32%)</td><td>0.00 <b>(-68.24%)</b></td><td>0.00 <b>(+27.20%)</b></td><td>2076.90 <b>(+214.82%)</b></td><td>756.44 <b>(+73.25%)</b></td><td>446.80 (+11.50%)</td><td>292.40 (+2.78%)</td><td>743.20 <b>(+380.69%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.70 (n/a)</td><td>436.62 (n/a)</td><td>400.70 (n/a)</td><td>284.50 (n/a)</td><td>154.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+3.77%)</td><td>0.01 (+7.57%)</td><td>0.01 (+6.10%)</td><td>0.01 (+0.67%)</td><td>0.00 (-11.46%)</td><td>447.40 (-0.67%)</td><td>322.50 (-7.93%)</td><td>299.10 (-5.77%)</td><td>264.00 (-3.65%)</td><td>72.41 (-12.45%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.40 (n/a)</td><td>350.28 (n/a)</td><td>317.40 (n/a)</td><td>274.00 (n/a)</td><td>82.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(-21.41%)</b></td><td>0.01 (-5.65%)</td><td>0.01 (+14.86%)</td><td>0.01 <b>(+31.31%)</b></td><td>0.00 <b>(-46.76%)</b></td><td>474.10 <b>(-23.84%)</b></td><td>369.68 (-6.18%)</td><td>373.80 (-12.93%)</td><td>252.00 <b>(+27.27%)</b></td><td>93.95 <b>(-45.83%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.50 (n/a)</td><td>394.04 (n/a)</td><td>429.30 (n/a)</td><td>198.00 (n/a)</td><td>173.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 <b>(-25.40%)</b></td><td>0.01 (-12.07%)</td><td>0.01 (-6.60%)</td><td>0.01 (-10.57%)</td><td>0.00 <b>(-46.58%)</b></td><td>668.50 (+11.83%)</td><td>573.70 (+11.31%)</td><td>599.20 (+7.06%)</td><td>488.30 <b>(+34.04%)</b></td><td>78.32 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.80 (n/a)</td><td>515.40 (n/a)</td><td>559.70 (n/a)</td><td>364.30 (n/a)</td><td>102.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-6.61%)</td><td>0.02 (+13.86%)</td><td>0.02 <b>(+20.78%)</b></td><td>0.01 (+4.13%)</td><td>0.01 (-2.69%)</td><td>899.30 (-3.97%)</td><td>500.38 (-11.42%)</td><td>459.10 (-17.22%)</td><td>267.30 (+7.09%)</td><td>253.86 (+3.32%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>936.50 (n/a)</td><td>564.88 (n/a)</td><td>554.60 (n/a)</td><td>249.60 (n/a)</td><td>245.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-5.69%)</td><td>0.02 (-19.26%)</td><td>0.02 (-16.61%)</td><td>0.01 <b>(-21.39%)</b></td><td>0.01 (-2.15%)</td><td>676.40 <b>(+27.21%)</b></td><td>490.10 <b>(+25.85%)</b></td><td>476.60 (+19.93%)</td><td>296.00 (+6.06%)</td><td>141.36 <b>(+33.45%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.70 (n/a)</td><td>389.44 (n/a)</td><td>397.40 (n/a)</td><td>279.10 (n/a)</td><td>105.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+39.87%)</b></td><td>0.02 (+7.96%)</td><td>0.02 (-5.76%)</td><td>0.01 (+10.14%)</td><td>0.01 <b>(+53.56%)</b></td><td>551.40 (-9.20%)</td><td>417.16 (-4.08%)</td><td>386.50 (+6.12%)</td><td>222.30 <b>(-28.52%)</b></td><td>137.96 (+0.63%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.30 (n/a)</td><td>434.90 (n/a)</td><td>364.20 (n/a)</td><td>311.00 (n/a)</td><td>137.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (+5.18%)</td><td>0.02 <b>(+24.37%)</b></td><td>0.03 <b>(+69.05%)</b></td><td>0.01 <b>(+45.52%)</b></td><td>0.01 (-4.24%)</td><td>591.70 <b>(-31.28%)</b></td><td>411.98 <b>(-23.30%)</b></td><td>318.50 <b>(-40.84%)</b></td><td>287.20 (-4.93%)</td><td>148.31 <b>(-34.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>861.00 (n/a)</td><td>537.16 (n/a)</td><td>538.40 (n/a)</td><td>302.10 (n/a)</td><td>225.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-4.45%)</td><td>0.02 (-18.25%)</td><td>0.02 <b>(-30.51%)</b></td><td>0.01 <b>(-42.69%)</b></td><td>0.01 <b>(+47.64%)</b></td><td>952.40 <b>(+74.46%)</b></td><td>548.02 <b>(+34.09%)</b></td><td>516.30 <b>(+43.90%)</b></td><td>352.60 (+4.66%)</td><td>242.42 <b>(+169.66%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>545.90 (n/a)</td><td>408.70 (n/a)</td><td>358.80 (n/a)</td><td>336.90 (n/a)</td><td>89.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-17.36%)</td><td>0.02 <b>(-22.84%)</b></td><td>0.02 <b>(-39.62%)</b></td><td>0.01 (-17.29%)</td><td>0.01 (-15.80%)</td><td>563.20 <b>(+20.91%)</b></td><td>445.22 <b>(+29.73%)</b></td><td>509.60 <b>(+65.62%)</b></td><td>281.50 <b>(+20.97%)</b></td><td>127.32 (+19.88%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.80 (n/a)</td><td>343.20 (n/a)</td><td>307.70 (n/a)</td><td>232.70 (n/a)</td><td>106.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-0.93%)</td><td>0.02 (+15.43%)</td><td>0.03 <b>(+77.08%)</b></td><td>0.01 (-11.91%)</td><td>0.01 (-4.38%)</td><td>666.60 (+13.52%)</td><td>381.06 (-13.07%)</td><td>294.00 <b>(-43.52%)</b></td><td>243.60 (+0.95%)</td><td>174.09 (+9.94%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.20 (n/a)</td><td>438.34 (n/a)</td><td>520.50 (n/a)</td><td>241.30 (n/a)</td><td>158.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-17.72%)</td><td>0.02 <b>(-23.77%)</b></td><td>0.02 <b>(-31.72%)</b></td><td>0.01 <b>(-21.29%)</b></td><td>0.01 (-9.86%)</td><td>625.10 <b>(+27.05%)</b></td><td>508.48 <b>(+33.08%)</b></td><td>530.80 <b>(+46.47%)</b></td><td>299.30 <b>(+21.57%)</b></td><td>133.88 <b>(+38.56%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.00 (n/a)</td><td>382.08 (n/a)</td><td>362.40 (n/a)</td><td>246.20 (n/a)</td><td>96.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (+5.19%)</td><td>0.02 (-10.19%)</td><td>0.02 <b>(-48.52%)</b></td><td>0.01 (+10.05%)</td><td>0.01 (+0.81%)</td><td>563.80 (-9.14%)</td><td>412.32 (+9.69%)</td><td>502.60 <b>(+94.28%)</b></td><td>230.40 (-4.91%)</td><td>156.47 (-11.21%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.50 (n/a)</td><td>375.88 (n/a)</td><td>258.70 (n/a)</td><td>242.30 (n/a)</td><td>176.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(-24.58%)</b></td><td>0.02 (-5.73%)</td><td>0.03 (+13.84%)</td><td>0.02 (-4.36%)</td><td>0.01 <b>(-34.24%)</b></td><td>531.70 (+4.56%)</td><td>373.02 (+2.07%)</td><td>316.20 (-12.14%)</td><td>278.20 <b>(+32.60%)</b></td><td>109.50 (-9.87%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.50 (n/a)</td><td>365.46 (n/a)</td><td>359.90 (n/a)</td><td>209.80 (n/a)</td><td>121.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 <b>(-42.62%)</b></td><td>0.02 (-17.09%)</td><td>0.02 (-15.17%)</td><td>0.01 (-18.69%)</td><td>0.01 <b>(-47.28%)</b></td><td>628.20 <b>(+22.98%)</b></td><td>460.34 (+12.65%)</td><td>533.10 (+17.86%)</td><td>283.30 <b>(+74.34%)</b></td><td>160.75 (+14.47%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>408.64 (n/a)</td><td>452.30 (n/a)</td><td>162.50 (n/a)</td><td>140.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+29.49%)</b></td><td>0.02 <b>(+34.73%)</b></td><td>0.02 <b>(+47.89%)</b></td><td>0.01 (-12.99%)</td><td>0.01 <b>(+53.17%)</b></td><td>621.00 (+14.94%)</td><td>369.06 <b>(-21.37%)</b></td><td>341.70 <b>(-32.38%)</b></td><td>223.30 <b>(-22.79%)</b></td><td>150.98 <b>(+46.37%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.30 (n/a)</td><td>469.38 (n/a)</td><td>505.30 (n/a)</td><td>289.20 (n/a)</td><td>103.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-1.43%)</td><td>0.04 (-1.75%)</td><td>0.04 <b>(-27.48%)</b></td><td>0.03 <b>(+250.46%)</b></td><td>0.01 <b>(-46.11%)</b></td><td>520.30 <b>(-71.47%)</b></td><td>391.40 <b>(-37.83%)</b></td><td>365.80 <b>(+37.88%)</b></td><td>254.20 (+1.48%)</td><td>113.14 <b>(-83.33%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1823.40 (n/a)</td><td>629.60 (n/a)</td><td>265.30 (n/a)</td><td>250.50 (n/a)</td><td>678.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 <b>(-27.52%)</b></td><td>0.05 (-15.25%)</td><td>0.06 (-0.34%)</td><td>0.03 (+5.46%)</td><td>0.01 <b>(-36.63%)</b></td><td>496.50 (-5.18%)</td><td>359.22 (+12.27%)</td><td>297.10 (+0.34%)</td><td>259.00 <b>(+37.91%)</b></td><td>106.28 (-16.68%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>523.60 (n/a)</td><td>319.96 (n/a)</td><td>296.10 (n/a)</td><td>187.80 (n/a)</td><td>127.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-9.35%)</td><td>0.04 (-4.87%)</td><td>0.03 <b>(-20.07%)</b></td><td>0.03 <b>(-25.94%)</b></td><td>0.02 <b>(+26.27%)</b></td><td>647.10 <b>(+35.04%)</b></td><td>451.08 (+16.26%)</td><td>519.70 <b>(+25.11%)</b></td><td>240.40 (+10.33%)</td><td>193.30 <b>(+85.01%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>479.20 (n/a)</td><td>387.98 (n/a)</td><td>415.40 (n/a)</td><td>217.90 (n/a)</td><td>104.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (+5.16%)</td><td>0.06 (+11.24%)</td><td>0.06 (+1.89%)</td><td>0.03 (-2.03%)</td><td>0.02 (-6.39%)</td><td>529.80 (+2.06%)</td><td>313.52 (-10.91%)</td><td>272.50 (-1.87%)</td><td>232.00 (-4.88%)</td><td>122.14 (-3.29%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>519.10 (n/a)</td><td>351.92 (n/a)</td><td>277.70 (n/a)</td><td>243.90 (n/a)</td><td>126.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-0.19%)</td><td>0.04 (-16.73%)</td><td>0.04 <b>(-35.94%)</b></td><td>0.03 (-8.49%)</td><td>0.02 (-11.75%)</td><td>539.90 (+9.27%)</td><td>398.46 (+16.86%)</td><td>420.80 <b>(+56.08%)</b></td><td>224.90 (+0.18%)</td><td>113.60 (-13.13%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>494.10 (n/a)</td><td>340.98 (n/a)</td><td>269.60 (n/a)</td><td>224.50 (n/a)</td><td>130.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-16.11%)</td><td>0.05 (+8.82%)</td><td>0.06 (-1.68%)</td><td>0.03 <b>(+111.14%)</b></td><td>0.01 <b>(-51.85%)</b></td><td>482.60 <b>(-52.64%)</b></td><td>322.80 <b>(-28.60%)</b></td><td>291.70 (+1.71%)</td><td>269.20 (+19.17%)</td><td>90.41 <b>(-72.72%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1019.00 (n/a)</td><td>452.08 (n/a)</td><td>286.80 (n/a)</td><td>225.90 (n/a)</td><td>331.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 <b>(-20.25%)</b></td><td>0.04 <b>(-22.70%)</b></td><td>0.04 <b>(-34.49%)</b></td><td>0.03 (-5.71%)</td><td>0.02 <b>(-31.73%)</b></td><td>594.50 (+6.07%)</td><td>430.36 <b>(+21.93%)</b></td><td>456.40 <b>(+52.64%)</b></td><td>246.20 <b>(+25.36%)</b></td><td>129.93 (-14.81%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>560.50 (n/a)</td><td>352.96 (n/a)</td><td>299.00 (n/a)</td><td>196.40 (n/a)</td><td>152.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-3.28%)</td><td>0.04 (-9.81%)</td><td>0.04 (-11.97%)</td><td>0.02 <b>(-49.69%)</b></td><td>0.02 <b>(+31.52%)</b></td><td>1060.40 <b>(+98.80%)</b></td><td>512.56 <b>(+30.92%)</b></td><td>418.40 (+13.57%)</td><td>257.10 (+3.38%)</td><td>325.86 <b>(+161.61%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.40 (n/a)</td><td>391.52 (n/a)</td><td>368.40 (n/a)</td><td>248.70 (n/a)</td><td>124.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-0.26%)</td><td>0.04 (-2.24%)</td><td>0.03 (+2.48%)</td><td>0.03 (+0.77%)</td><td>0.01 (+1.93%)</td><td>632.00 (-0.75%)</td><td>484.30 (+2.80%)</td><td>508.20 (-2.42%)</td><td>294.90 (+0.24%)</td><td>142.28 (+4.67%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>636.80 (n/a)</td><td>471.12 (n/a)</td><td>520.80 (n/a)</td><td>294.20 (n/a)</td><td>135.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (+18.64%)</td><td>0.05 (-14.55%)</td><td>0.03 <b>(-36.52%)</b></td><td>0.03 (-12.86%)</td><td>0.02 <b>(+79.94%)</b></td><td>526.70 (+14.77%)</td><td>405.32 <b>(+25.97%)</b></td><td>474.30 <b>(+57.52%)</b></td><td>221.70 (-15.70%)</td><td>133.94 <b>(+70.39%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.90 (n/a)</td><td>321.76 (n/a)</td><td>301.10 (n/a)</td><td>263.00 (n/a)</td><td>78.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-2.67%)</td><td>0.04 (-8.19%)</td><td>0.03 (-2.00%)</td><td>0.03 (+15.01%)</td><td>0.01 <b>(-28.58%)</b></td><td>542.20 (-13.07%)</td><td>475.92 (+2.29%)</td><td>518.40 (+2.05%)</td><td>291.80 (+2.75%)</td><td>103.81 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>623.70 (n/a)</td><td>465.26 (n/a)</td><td>508.00 (n/a)</td><td>284.00 (n/a)</td><td>165.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-3.41%)</td><td>0.05 <b>(+47.28%)</b></td><td>0.05 <b>(+94.57%)</b></td><td>0.03 <b>(+92.69%)</b></td><td>0.01 <b>(-36.33%)</b></td><td>514.70 <b>(-48.11%)</b></td><td>331.16 <b>(-42.63%)</b></td><td>298.20 <b>(-48.60%)</b></td><td>232.00 (+3.53%)</td><td>107.81 <b>(-61.72%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>991.90 (n/a)</td><td>577.24 (n/a)</td><td>580.20 (n/a)</td><td>224.10 (n/a)</td><td>281.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-0.34%)</td><td>0.10 (-13.55%)</td><td>0.11 (-13.99%)</td><td>0.05 (-14.49%)</td><td>0.03 (+4.42%)</td><td>598.90 (+16.95%)</td><td>368.98 (+17.91%)</td><td>298.00 (+16.27%)</td><td>251.90 (+0.36%)</td><td>139.71 <b>(+24.12%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>512.10 (n/a)</td><td>312.94 (n/a)</td><td>256.30 (n/a)</td><td>251.00 (n/a)</td><td>112.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (-2.15%)</td><td>0.09 (-17.64%)</td><td>0.09 <b>(-27.49%)</b></td><td>0.06 (-10.71%)</td><td>0.02 (-1.51%)</td><td>509.20 (+12.01%)</td><td>386.30 <b>(+21.72%)</b></td><td>382.60 <b>(+37.92%)</b></td><td>272.60 (+2.21%)</td><td>86.75 (+9.90%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>454.60 (n/a)</td><td>317.36 (n/a)</td><td>277.40 (n/a)</td><td>266.70 (n/a)</td><td>78.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 <b>(+32.46%)</b></td><td>0.11 (+4.91%)</td><td>0.09 <b>(-21.27%)</b></td><td>0.05 (-2.57%)</td><td>0.05 <b>(+54.74%)</b></td><td>612.40 (+2.63%)</td><td>376.34 (+3.43%)</td><td>358.00 <b>(+27.04%)</b></td><td>190.50 <b>(-24.52%)</b></td><td>177.52 <b>(+20.30%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>596.70 (n/a)</td><td>363.86 (n/a)</td><td>281.80 (n/a)</td><td>252.40 (n/a)</td><td>147.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 <b>(+37.81%)</b></td><td>0.12 <b>(+25.67%)</b></td><td>0.10 <b>(+26.12%)</b></td><td>0.08 <b>(+22.97%)</b></td><td>0.03 <b>(+29.83%)</b></td><td>401.10 (-18.69%)</td><td>302.24 <b>(-20.35%)</b></td><td>318.00 <b>(-20.70%)</b></td><td>197.50 <b>(-27.44%)</b></td><td>80.94 <b>(-20.96%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>493.30 (n/a)</td><td>379.48 (n/a)</td><td>401.00 (n/a)</td><td>272.20 (n/a)</td><td>102.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (-3.10%)</td><td>0.12 (+6.27%)</td><td>0.12 (+9.84%)</td><td>0.08 <b>(+41.47%)</b></td><td>0.03 <b>(-30.60%)</b></td><td>394.30 <b>(-29.31%)</b></td><td>296.90 (-12.78%)</td><td>278.40 (-8.96%)</td><td>209.20 (+3.21%)</td><td>69.34 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>557.80 (n/a)</td><td>340.42 (n/a)</td><td>305.80 (n/a)</td><td>202.70 (n/a)</td><td>138.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (-5.43%)</td><td>0.07 (-9.46%)</td><td>0.06 (-1.32%)</td><td>0.06 (-10.62%)</td><td>0.03 (-1.73%)</td><td>575.60 (+11.88%)</td><td>480.00 (+11.32%)</td><td>505.10 (+1.34%)</td><td>263.80 (+5.77%)</td><td>127.87 (+12.46%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.50 (n/a)</td><td>431.20 (n/a)</td><td>498.40 (n/a)</td><td>249.40 (n/a)</td><td>113.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 <b>(-28.62%)</b></td><td>0.09 <b>(-21.58%)</b></td><td>0.12 (-2.88%)</td><td>0.03 <b>(-48.19%)</b></td><td>0.04 <b>(-25.15%)</b></td><td>1029.90 <b>(+92.97%)</b></td><td>465.84 <b>(+36.92%)</b></td><td>284.70 (+2.97%)</td><td>257.60 <b>(+40.08%)</b></td><td>328.56 <b>(+93.36%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>533.70 (n/a)</td><td>340.24 (n/a)</td><td>276.50 (n/a)</td><td>183.90 (n/a)</td><td>169.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (+12.46%)</td><td>0.10 (+14.74%)</td><td>0.12 <b>(+62.06%)</b></td><td>0.06 (-8.82%)</td><td>0.04 <b>(+26.39%)</b></td><td>567.10 (+9.67%)</td><td>367.90 (-7.49%)</td><td>275.90 <b>(-38.29%)</b></td><td>212.00 (-11.07%)</td><td>170.38 <b>(+28.72%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>517.10 (n/a)</td><td>397.70 (n/a)</td><td>447.10 (n/a)</td><td>238.40 (n/a)</td><td>132.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 <b>(-23.34%)</b></td><td>0.10 (+1.50%)</td><td>0.09 <b>(+34.26%)</b></td><td>0.07 <b>(+25.09%)</b></td><td>0.03 <b>(-45.49%)</b></td><td>461.20 <b>(-20.06%)</b></td><td>356.62 (-12.76%)</td><td>365.40 <b>(-25.52%)</b></td><td>243.80 <b>(+30.44%)</b></td><td>95.02 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>576.90 (n/a)</td><td>408.78 (n/a)</td><td>490.60 (n/a)</td><td>186.90 (n/a)</td><td>167.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (-16.26%)</td><td>0.09 (+8.26%)</td><td>0.11 <b>(+63.48%)</b></td><td>0.05 <b>(-23.49%)</b></td><td>0.03 (-2.70%)</td><td>667.70 <b>(+30.69%)</b></td><td>417.56 (-3.20%)</td><td>297.30 <b>(-38.84%)</b></td><td>266.00 (+19.39%)</td><td>187.12 <b>(+54.95%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>510.90 (n/a)</td><td>431.38 (n/a)</td><td>486.10 (n/a)</td><td>222.80 (n/a)</td><td>120.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(-20.11%)</b></td><td>0.07 (-3.07%)</td><td>0.06 (+1.09%)</td><td>0.05 (+8.25%)</td><td>0.02 <b>(-39.71%)</b></td><td>598.80 (-7.62%)</td><td>475.12 (-2.27%)</td><td>514.80 (-1.10%)</td><td>361.60 <b>(+25.16%)</b></td><td>102.30 <b>(-33.21%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>648.20 (n/a)</td><td>486.18 (n/a)</td><td>520.50 (n/a)</td><td>288.90 (n/a)</td><td>153.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (-5.13%)</td><td>0.09 (-8.98%)</td><td>0.11 (-6.11%)</td><td>0.04 <b>(-35.82%)</b></td><td>0.03 <b>(+21.75%)</b></td><td>807.10 <b>(+55.81%)</b></td><td>438.54 (+19.51%)</td><td>311.30 (+6.50%)</td><td>292.60 (+5.40%)</td><td>220.16 <b>(+97.39%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>518.00 (n/a)</td><td>366.96 (n/a)</td><td>292.30 (n/a)</td><td>277.60 (n/a)</td><td>111.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (-5.70%)</td><td>0.07 (-11.17%)</td><td>0.07 (-11.78%)</td><td>0.05 (-2.50%)</td><td>0.02 (+5.10%)</td><td>508.60 (+2.56%)</td><td>365.84 (+14.32%)</td><td>333.50 (+13.36%)</td><td>249.20 (+6.04%)</td><td>121.73 (+14.73%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>495.90 (n/a)</td><td>320.02 (n/a)</td><td>294.20 (n/a)</td><td>235.00 (n/a)</td><td>106.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.22 (-0.40%)</td><td>0.17 (+6.39%)</td><td>0.19 (+2.03%)</td><td>0.12 <b>(+41.23%)</b></td><td>0.04 <b>(-22.66%)</b></td><td>400.40 <b>(-29.20%)</b></td><td>303.44 (-11.78%)</td><td>258.70 (-2.01%)</td><td>227.80 (+0.40%)</td><td>80.73 <b>(-43.43%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>565.50 (n/a)</td><td>343.94 (n/a)</td><td>264.00 (n/a)</td><td>226.90 (n/a)</td><td>142.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.21 (+8.05%)</td><td>3.01 (-2.72%)</td><td>2.79 (+3.61%)</td><td>2.28 (-4.27%)</td><td>0.76 (+4.52%)</td><td>4594.40 (+4.46%)</td><td>3641.92 (+3.10%)</td><td>3756.60 (-3.49%)</td><td>2488.80 (-7.45%)</td><td>810.51 (+3.88%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.90 (n/a)</td><td>3.10 (n/a)</td><td>2.69 (n/a)</td><td>2.38 (n/a)</td><td>0.72 (n/a)</td><td>4398.10 (n/a)</td><td>3532.32 (n/a)</td><td>3892.30 (n/a)</td><td>2689.20 (n/a)</td><td>780.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (+1.70%)</td><td>0.16 <b>(+37.36%)</b></td><td>0.16 <b>(+74.77%)</b></td><td>0.14 <b>(+104.85%)</b></td><td>0.01 <b>(-80.53%)</b></td><td>286.90 <b>(-51.19%)</b></td><td>264.68 <b>(-35.33%)</b></td><td>263.00 <b>(-42.79%)</b></td><td>247.90 (-1.67%)</td><td>15.11 <b>(-89.88%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>587.80 (n/a)</td><td>409.26 (n/a)</td><td>459.70 (n/a)</td><td>252.10 (n/a)</td><td>149.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-17.68%)</td><td>0.01 (-19.59%)</td><td>0.02 (-17.45%)</td><td>0.01 <b>(-27.51%)</b></td><td>0.01 (-3.93%)</td><td>721.40 <b>(+37.93%)</b></td><td>410.94 <b>(+29.91%)</b></td><td>311.90 <b>(+21.13%)</b></td><td>268.00 <b>(+21.49%)</b></td><td>191.79 <b>(+55.08%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.00 (n/a)</td><td>316.32 (n/a)</td><td>257.50 (n/a)</td><td>220.60 (n/a)</td><td>123.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+3.87%)</td><td>0.01 (+12.06%)</td><td>0.02 (+15.16%)</td><td>0.01 (-8.74%)</td><td>0.00 (+14.10%)</td><td>525.70 (+9.57%)</td><td>304.80 (-8.33%)</td><td>246.40 (-13.15%)</td><td>228.70 (-3.71%)</td><td>125.05 <b>(+23.89%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>479.80 (n/a)</td><td>332.48 (n/a)</td><td>283.70 (n/a)</td><td>237.50 (n/a)</td><td>100.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (+7.36%)</td><td>0.02 (+16.05%)</td><td>0.02 (+10.50%)</td><td>0.01 (+4.57%)</td><td>0.01 (-3.15%)</td><td>482.10 (-4.38%)</td><td>316.88 (-15.30%)</td><td>299.60 (-9.51%)</td><td>214.40 (-6.86%)</td><td>101.02 (-16.44%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>504.20 (n/a)</td><td>374.10 (n/a)</td><td>331.10 (n/a)</td><td>230.20 (n/a)</td><td>120.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-14.18%)</td><td>0.01 (+2.22%)</td><td>0.01 (+10.48%)</td><td>0.01 (-13.34%)</td><td>0.00 (-9.45%)</td><td>593.90 (+15.39%)</td><td>350.24 (-1.46%)</td><td>278.30 (-9.47%)</td><td>244.00 (+16.52%)</td><td>146.82 (+17.44%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.70 (n/a)</td><td>355.44 (n/a)</td><td>307.40 (n/a)</td><td>209.40 (n/a)</td><td>125.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-8.68%)</td><td>0.01 <b>(-22.90%)</b></td><td>0.01 <b>(-44.03%)</b></td><td>0.01 (+0.29%)</td><td>0.00 (-19.15%)</td><td>578.00 (-0.29%)</td><td>474.26 <b>(+24.27%)</b></td><td>526.90 <b>(+78.67%)</b></td><td>258.20 (+9.50%)</td><td>125.74 (-19.82%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.70 (n/a)</td><td>381.64 (n/a)</td><td>294.90 (n/a)</td><td>235.80 (n/a)</td><td>156.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+7.25%)</td><td>0.01 (+15.49%)</td><td>0.01 (-4.97%)</td><td>0.01 <b>(+268.62%)</b></td><td>0.00 (-14.96%)</td><td>669.50 <b>(-72.87%)</b></td><td>491.46 <b>(-43.46%)</b></td><td>529.30 (+5.23%)</td><td>239.20 (-6.74%)</td><td>159.47 <b>(-82.38%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2467.80 (n/a)</td><td>869.26 (n/a)</td><td>503.00 (n/a)</td><td>256.50 (n/a)</td><td>904.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-1.63%)</td><td>0.02 (+6.75%)</td><td>0.01 (-4.51%)</td><td>0.01 (+3.32%)</td><td>0.01 (+12.95%)</td><td>512.90 (-3.21%)</td><td>371.34 (-4.01%)</td><td>426.10 (+4.74%)</td><td>218.60 (+1.67%)</td><td>136.37 (+8.15%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.90 (n/a)</td><td>386.84 (n/a)</td><td>406.80 (n/a)</td><td>215.00 (n/a)</td><td>126.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(+21.09%)</b></td><td>0.01 (-10.21%)</td><td>0.01 (-18.97%)</td><td>0.01 (-4.15%)</td><td>0.00 <b>(+24.63%)</b></td><td>685.20 (+4.32%)</td><td>511.72 (+14.97%)</td><td>565.20 <b>(+23.41%)</b></td><td>231.50 (-17.44%)</td><td>171.43 (+5.57%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>656.80 (n/a)</td><td>445.10 (n/a)</td><td>458.00 (n/a)</td><td>280.40 (n/a)</td><td>162.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-13.07%)</td><td>0.01 (-3.16%)</td><td>0.01 (+15.49%)</td><td>0.01 (+14.92%)</td><td>0.00 <b>(-21.95%)</b></td><td>580.20 (-12.99%)</td><td>412.12 (-2.64%)</td><td>409.80 (-13.42%)</td><td>260.70 (+15.00%)</td><td>151.08 (-18.67%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.80 (n/a)</td><td>423.28 (n/a)</td><td>473.30 (n/a)</td><td>226.70 (n/a)</td><td>185.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+12.39%)</td><td>0.01 (+15.80%)</td><td>0.02 (+11.01%)</td><td>0.01 <b>(+23.74%)</b></td><td>0.00 (+5.30%)</td><td>518.50 (-19.19%)</td><td>303.00 (-15.50%)</td><td>262.10 (-9.90%)</td><td>215.80 (-11.01%)</td><td>122.86 <b>(-24.26%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.60 (n/a)</td><td>358.60 (n/a)</td><td>290.90 (n/a)</td><td>242.50 (n/a)</td><td>162.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 <b>(+81.26%)</b></td><td>0.02 <b>(+95.53%)</b></td><td>0.01 <b>(+57.17%)</b></td><td>0.01 <b>(+361.03%)</b></td><td>0.01 <b>(+49.58%)</b></td><td>450.50 <b>(-78.31%)</b></td><td>332.78 <b>(-59.84%)</b></td><td>334.50 <b>(-36.37%)</b></td><td>223.20 <b>(-44.85%)</b></td><td>108.48 <b>(-84.55%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2077.10 (n/a)</td><td>828.56 (n/a)</td><td>525.70 (n/a)</td><td>404.70 (n/a)</td><td>702.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (-14.03%)</td><td>0.01 <b>(-30.36%)</b></td><td>0.01 <b>(-30.20%)</b></td><td>0.00 <b>(-78.51%)</b></td><td>0.00 <b>(+30.00%)</b></td><td>2390.10 <b>(+365.36%)</b></td><td>845.70 <b>(+119.69%)</b></td><td>530.50 <b>(+43.26%)</b></td><td>293.10 (+16.31%)</td><td>868.90 <b>(+709.66%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.60 (n/a)</td><td>384.96 (n/a)</td><td>370.30 (n/a)</td><td>252.00 (n/a)</td><td>107.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+36.09%)</b></td><td>0.03 <b>(+58.15%)</b></td><td>0.03 <b>(+105.84%)</b></td><td>0.02 <b>(+27.56%)</b></td><td>0.01 <b>(+74.10%)</b></td><td>518.70 <b>(-21.60%)</b></td><td>331.88 <b>(-31.77%)</b></td><td>244.70 <b>(-51.41%)</b></td><td>201.40 <b>(-26.52%)</b></td><td>153.05 (+10.76%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.60 (n/a)</td><td>486.44 (n/a)</td><td>503.60 (n/a)</td><td>274.10 (n/a)</td><td>138.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (+11.01%)</td><td>0.03 <b>(+24.23%)</b></td><td>0.04 <b>(+56.36%)</b></td><td>0.02 (+11.14%)</td><td>0.01 <b>(+52.03%)</b></td><td>595.90 (-10.03%)</td><td>403.48 (-14.38%)</td><td>287.50 <b>(-36.05%)</b></td><td>271.90 (-9.91%)</td><td>167.35 <b>(+26.59%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>662.30 (n/a)</td><td>471.26 (n/a)</td><td>449.60 (n/a)</td><td>301.80 (n/a)</td><td>132.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+28.89%)</b></td><td>0.03 <b>(+30.33%)</b></td><td>0.02 <b>(+22.21%)</b></td><td>0.02 <b>(+144.58%)</b></td><td>0.01 (-11.83%)</td><td>434.30 <b>(-59.11%)</b></td><td>331.76 <b>(-35.61%)</b></td><td>351.00 (-18.16%)</td><td>208.40 <b>(-22.44%)</b></td><td>95.32 <b>(-70.77%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1062.10 (n/a)</td><td>515.22 (n/a)</td><td>428.90 (n/a)</td><td>268.70 (n/a)</td><td>326.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(-20.42%)</b></td><td>0.02 (-2.04%)</td><td>0.02 (+8.82%)</td><td>0.02 (+13.64%)</td><td>0.01 <b>(-41.42%)</b></td><td>522.60 (-12.01%)</td><td>434.82 (-5.65%)</td><td>464.70 (-8.11%)</td><td>271.80 <b>(+25.66%)</b></td><td>96.53 <b>(-34.71%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.90 (n/a)</td><td>460.84 (n/a)</td><td>505.70 (n/a)</td><td>216.30 (n/a)</td><td>147.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (-2.77%)</td><td>0.02 (-5.77%)</td><td>0.02 <b>(-20.70%)</b></td><td>0.01 (+18.98%)</td><td>0.01 (-5.94%)</td><td>555.80 (-15.94%)</td><td>401.46 (+2.83%)</td><td>476.30 <b>(+26.11%)</b></td><td>204.60 (+2.87%)</td><td>146.50 (-18.34%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.20 (n/a)</td><td>390.42 (n/a)</td><td>377.70 (n/a)</td><td>198.90 (n/a)</td><td>179.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(-41.97%)</b></td><td>0.03 (-7.94%)</td><td>0.03 <b>(+34.29%)</b></td><td>0.02 (-7.75%)</td><td>0.01 <b>(-49.77%)</b></td><td>564.80 (+8.41%)</td><td>382.98 (-1.90%)</td><td>310.50 <b>(-25.54%)</b></td><td>243.80 <b>(+72.30%)</b></td><td>155.27 (+1.57%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>521.00 (n/a)</td><td>390.40 (n/a)</td><td>417.00 (n/a)</td><td>141.50 (n/a)</td><td>152.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+40.64%)</b></td><td>0.02 (-3.37%)</td><td>0.02 <b>(-25.70%)</b></td><td>0.01 <b>(+23.02%)</b></td><td>0.01 <b>(+38.95%)</b></td><td>612.90 (-18.71%)</td><td>404.34 (+3.58%)</td><td>410.40 <b>(+34.60%)</b></td><td>206.90 <b>(-28.90%)</b></td><td>155.48 <b>(-23.54%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>754.00 (n/a)</td><td>390.38 (n/a)</td><td>304.90 (n/a)</td><td>291.00 (n/a)</td><td>203.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (+16.50%)</td><td>0.03 (+16.46%)</td><td>0.03 <b>(+26.69%)</b></td><td>0.02 <b>(+24.20%)</b></td><td>0.01 <b>(+29.60%)</b></td><td>457.50 (-19.50%)</td><td>348.56 (-13.31%)</td><td>309.40 <b>(-21.07%)</b></td><td>252.80 (-14.16%)</td><td>95.14 (-8.48%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.30 (n/a)</td><td>402.06 (n/a)</td><td>392.00 (n/a)</td><td>294.50 (n/a)</td><td>103.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(+34.20%)</b></td><td>0.03 <b>(+59.42%)</b></td><td>0.02 <b>(+43.55%)</b></td><td>0.01 <b>(+214.33%)</b></td><td>0.01 (+14.99%)</td><td>650.50 <b>(-68.18%)</b></td><td>370.18 <b>(-52.98%)</b></td><td>346.50 <b>(-30.34%)</b></td><td>183.70 <b>(-25.51%)</b></td><td>179.16 <b>(-75.08%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2044.60 (n/a)</td><td>787.22 (n/a)</td><td>497.40 (n/a)</td><td>246.60 (n/a)</td><td>718.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-17.84%)</td><td>0.02 <b>(-29.57%)</b></td><td>0.02 <b>(-33.72%)</b></td><td>0.02 <b>(-26.19%)</b></td><td>0.01 (-4.95%)</td><td>596.00 <b>(+35.49%)</b></td><td>520.64 <b>(+45.89%)</b></td><td>576.50 <b>(+50.88%)</b></td><td>276.60 <b>(+21.69%)</b></td><td>136.81 <b>(+51.25%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>439.90 (n/a)</td><td>356.88 (n/a)</td><td>382.10 (n/a)</td><td>227.30 (n/a)</td><td>90.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (-15.67%)</td><td>0.02 (-17.30%)</td><td>0.02 (+10.72%)</td><td>0.00 <b>(-73.60%)</b></td><td>0.01 (+11.86%)</td><td>1912.20 <b>(+278.80%)</b></td><td>697.56 <b>(+75.33%)</b></td><td>419.30 (-9.67%)</td><td>255.20 (+18.59%)</td><td>688.75 <b>(+440.16%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.80 (n/a)</td><td>397.86 (n/a)</td><td>464.20 (n/a)</td><td>215.20 (n/a)</td><td>127.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-3.00%)</td><td>0.05 (-5.50%)</td><td>0.05 (-7.41%)</td><td>0.03 (-15.23%)</td><td>0.01 (-0.42%)</td><td>563.30 (+17.97%)</td><td>362.74 (+7.22%)</td><td>304.10 (+7.99%)</td><td>257.60 (+3.08%)</td><td>127.54 <b>(+21.53%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.50 (n/a)</td><td>338.30 (n/a)</td><td>281.60 (n/a)</td><td>249.90 (n/a)</td><td>104.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (-7.18%)</td><td>0.05 <b>(-29.33%)</b></td><td>0.05 <b>(-39.41%)</b></td><td>0.04 <b>(-29.43%)</b></td><td>0.02 <b>(+28.18%)</b></td><td>652.90 <b>(+41.69%)</b></td><td>512.08 <b>(+50.03%)</b></td><td>508.50 <b>(+65.04%)</b></td><td>272.70 (+7.74%)</td><td>156.59 <b>(+92.53%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>460.80 (n/a)</td><td>341.32 (n/a)</td><td>308.10 (n/a)</td><td>253.10 (n/a)</td><td>81.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(+27.27%)</b></td><td>0.06 (+11.12%)</td><td>0.05 (-18.19%)</td><td>0.05 <b>(+70.44%)</b></td><td>0.02 (-6.72%)</td><td>351.30 <b>(-41.32%)</b></td><td>298.46 (-16.51%)</td><td>333.20 <b>(+22.23%)</b></td><td>186.00 <b>(-21.42%)</b></td><td>69.38 <b>(-55.89%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>598.70 (n/a)</td><td>357.48 (n/a)</td><td>272.60 (n/a)</td><td>236.70 (n/a)</td><td>157.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (+1.65%)</td><td>0.06 (+4.57%)</td><td>0.06 (+7.05%)</td><td>0.04 (+15.23%)</td><td>0.02 (-8.18%)</td><td>502.00 (-13.22%)</td><td>369.28 (-6.76%)</td><td>326.40 (-6.58%)</td><td>260.60 (-1.62%)</td><td>119.49 (-18.39%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>578.50 (n/a)</td><td>396.04 (n/a)</td><td>349.40 (n/a)</td><td>264.90 (n/a)</td><td>146.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 <b>(+58.79%)</b></td><td>0.04 (+7.95%)</td><td>0.04 (-4.40%)</td><td>0.03 (-15.11%)</td><td>0.02 <b>(+226.97%)</b></td><td>595.30 (+17.79%)</td><td>434.94 (+0.76%)</td><td>464.70 (+4.59%)</td><td>233.10 <b>(-37.03%)</b></td><td>131.65 <b>(+131.00%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>505.40 (n/a)</td><td>431.64 (n/a)</td><td>444.30 (n/a)</td><td>370.20 (n/a)</td><td>56.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (+4.98%)</td><td>0.05 (-12.90%)</td><td>0.04 <b>(-43.43%)</b></td><td>0.04 (+1.39%)</td><td>0.02 (+1.88%)</td><td>577.70 (-1.37%)</td><td>439.44 (+14.96%)</td><td>529.40 <b>(+76.76%)</b></td><td>228.40 (-4.75%)</td><td>166.01 (-0.72%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.70 (n/a)</td><td>382.26 (n/a)</td><td>299.50 (n/a)</td><td>239.80 (n/a)</td><td>167.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-0.02%)</td><td>0.04 (-16.69%)</td><td>0.04 <b>(-33.02%)</b></td><td>0.03 <b>(-22.61%)</b></td><td>0.02 <b>(+51.49%)</b></td><td>592.00 <b>(+29.23%)</b></td><td>424.94 <b>(+30.29%)</b></td><td>421.00 <b>(+49.29%)</b></td><td>255.40 (+0.04%)</td><td>161.84 <b>(+95.47%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>458.10 (n/a)</td><td>326.14 (n/a)</td><td>282.00 (n/a)</td><td>255.30 (n/a)</td><td>82.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (+1.97%)</td><td>0.05 (-12.28%)</td><td>0.04 (-17.13%)</td><td>0.03 (-1.92%)</td><td>0.02 (-10.74%)</td><td>572.80 (+1.96%)</td><td>432.42 (+11.12%)</td><td>470.80 <b>(+20.69%)</b></td><td>234.20 (-1.93%)</td><td>129.78 (-11.40%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.80 (n/a)</td><td>389.16 (n/a)</td><td>390.10 (n/a)</td><td>238.80 (n/a)</td><td>146.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 <b>(-21.33%)</b></td><td>0.04 <b>(-28.49%)</b></td><td>0.04 <b>(-34.99%)</b></td><td>0.03 (+3.46%)</td><td>0.02 <b>(-25.69%)</b></td><td>581.10 (-3.34%)</td><td>442.52 <b>(+32.75%)</b></td><td>465.30 <b>(+53.82%)</b></td><td>236.10 <b>(+27.14%)</b></td><td>127.04 (-19.85%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>601.20 (n/a)</td><td>333.34 (n/a)</td><td>302.50 (n/a)</td><td>185.70 (n/a)</td><td>158.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (-6.97%)</td><td>0.04 (-15.92%)</td><td>0.04 <b>(-21.22%)</b></td><td>0.03 (+9.39%)</td><td>0.01 <b>(-24.97%)</b></td><td>625.70 (-8.58%)</td><td>483.30 (+12.79%)</td><td>467.30 <b>(+26.95%)</b></td><td>293.60 (+7.51%)</td><td>125.68 <b>(-27.59%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>684.40 (n/a)</td><td>428.50 (n/a)</td><td>368.10 (n/a)</td><td>273.10 (n/a)</td><td>173.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (+1.96%)</td><td>0.05 (-7.80%)</td><td>0.04 (-14.42%)</td><td>0.03 (-1.80%)</td><td>0.01 (-11.93%)</td><td>532.90 (+1.82%)</td><td>384.44 (+6.75%)</td><td>389.30 (+16.84%)</td><td>254.70 (-1.89%)</td><td>99.76 (-10.59%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>523.40 (n/a)</td><td>360.14 (n/a)</td><td>333.20 (n/a)</td><td>259.60 (n/a)</td><td>111.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (+1.80%)</td><td>0.10 (+1.24%)</td><td>0.11 (-0.09%)</td><td>0.05 <b>(-23.36%)</b></td><td>0.03 <b>(+21.84%)</b></td><td>630.50 <b>(+30.48%)</b></td><td>354.76 (+4.54%)</td><td>311.50 (+0.10%)</td><td>228.70 (-1.76%)</td><td>158.35 <b>(+66.79%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>483.20 (n/a)</td><td>339.34 (n/a)</td><td>311.20 (n/a)</td><td>232.80 (n/a)</td><td>94.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-7.61%)</td><td>0.09 (-18.53%)</td><td>0.07 <b>(-35.29%)</b></td><td>0.06 <b>(-20.98%)</b></td><td>0.03 (+9.10%)</td><td>538.60 <b>(+26.55%)</b></td><td>406.64 <b>(+26.97%)</b></td><td>471.70 <b>(+54.55%)</b></td><td>252.80 (+8.27%)</td><td>127.03 <b>(+48.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>425.60 (n/a)</td><td>320.26 (n/a)</td><td>305.20 (n/a)</td><td>233.50 (n/a)</td><td>85.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.22 <b>(+59.72%)</b></td><td>0.12 (+15.45%)</td><td>0.08 <b>(-24.53%)</b></td><td>0.07 <b>(+35.59%)</b></td><td>0.06 <b>(+71.36%)</b></td><td>574.90 <b>(-26.24%)</b></td><td>420.06 (-8.42%)</td><td>521.80 <b>(+32.50%)</b></td><td>183.50 <b>(-37.41%)</b></td><td>171.54 (-15.65%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>779.40 (n/a)</td><td>458.68 (n/a)</td><td>393.80 (n/a)</td><td>293.20 (n/a)</td><td>203.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-2.22%)</td><td>0.10 (-1.09%)</td><td>0.11 (-0.82%)</td><td>0.05 (-10.10%)</td><td>0.04 (+10.46%)</td><td>617.30 (+11.23%)</td><td>386.98 (+4.31%)</td><td>299.20 (+0.84%)</td><td>253.60 (+2.26%)</td><td>165.59 <b>(+20.48%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>555.00 (n/a)</td><td>370.98 (n/a)</td><td>296.70 (n/a)</td><td>248.00 (n/a)</td><td>137.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(-37.18%)</b></td><td>0.07 <b>(-35.44%)</b></td><td>0.07 <b>(-48.72%)</b></td><td>0.06 <b>(+32.55%)</b></td><td>0.02 <b>(-67.64%)</b></td><td>723.80 <b>(-24.56%)</b></td><td>590.78 <b>(+27.03%)</b></td><td>585.30 <b>(+94.97%)</b></td><td>435.90 <b>(+59.20%)</b></td><td>121.71 <b>(-58.65%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>959.40 (n/a)</td><td>465.06 (n/a)</td><td>300.20 (n/a)</td><td>273.80 (n/a)</td><td>294.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-14.89%)</td><td>0.10 (-10.11%)</td><td>0.10 (-7.93%)</td><td>0.06 (+17.60%)</td><td>0.03 <b>(-31.80%)</b></td><td>542.60 (-14.95%)</td><td>356.96 (+3.09%)</td><td>329.40 (+8.61%)</td><td>245.60 (+17.46%)</td><td>114.81 <b>(-32.90%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>638.00 (n/a)</td><td>346.26 (n/a)</td><td>303.30 (n/a)</td><td>209.10 (n/a)</td><td>171.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-12.34%)</td><td>0.10 (+8.23%)</td><td>0.12 <b>(+77.89%)</b></td><td>0.06 (+12.22%)</td><td>0.03 <b>(-33.87%)</b></td><td>602.30 (-10.89%)</td><td>387.00 (-15.79%)</td><td>299.40 <b>(-43.80%)</b></td><td>280.30 (+14.08%)</td><td>139.32 <b>(-29.45%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>675.90 (n/a)</td><td>459.54 (n/a)</td><td>532.70 (n/a)</td><td>245.70 (n/a)</td><td>197.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 <b>(-29.06%)</b></td><td>0.10 (-9.94%)</td><td>0.12 (-0.76%)</td><td>0.06 (+3.14%)</td><td>0.03 <b>(-34.72%)</b></td><td>567.70 (-3.04%)</td><td>374.60 (+2.23%)</td><td>279.90 (+0.79%)</td><td>263.00 <b>(+40.94%)</b></td><td>145.01 (-19.04%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>585.50 (n/a)</td><td>366.42 (n/a)</td><td>277.70 (n/a)</td><td>186.60 (n/a)</td><td>179.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 <b>(-32.60%)</b></td><td>0.08 (-18.29%)</td><td>0.08 (-7.52%)</td><td>0.07 (+13.90%)</td><td>0.01 <b>(-72.17%)</b></td><td>510.50 (-12.19%)</td><td>455.94 (+11.94%)</td><td>468.70 (+8.14%)</td><td>373.60 <b>(+48.37%)</b></td><td>50.26 <b>(-63.56%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>581.40 (n/a)</td><td>407.32 (n/a)</td><td>433.40 (n/a)</td><td>251.80 (n/a)</td><td>137.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 <b>(+38.46%)</b></td><td>0.10 <b>(+33.98%)</b></td><td>0.12 <b>(+80.66%)</b></td><td>0.06 (-4.90%)</td><td>0.04 <b>(+89.84%)</b></td><td>593.80 (+5.17%)</td><td>366.92 (-19.18%)</td><td>282.60 <b>(-44.64%)</b></td><td>241.00 <b>(-27.78%)</b></td><td>156.17 <b>(+45.78%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>564.60 (n/a)</td><td>453.98 (n/a)</td><td>510.50 (n/a)</td><td>333.70 (n/a)</td><td>107.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (+6.67%)</td><td>0.07 (-5.28%)</td><td>0.08 (+4.12%)</td><td>0.05 <b>(-32.29%)</b></td><td>0.02 <b>(+189.87%)</b></td><td>448.10 <b>(+47.69%)</b></td><td>308.10 (+11.30%)</td><td>267.50 (-3.95%)</td><td>234.10 (-6.25%)</td><td>88.93 <b>(+301.69%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>303.40 (n/a)</td><td>276.82 (n/a)</td><td>278.50 (n/a)</td><td>249.70 (n/a)</td><td>22.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (+3.03%)</td><td>0.06 (-19.16%)</td><td>0.06 <b>(-27.64%)</b></td><td>0.04 <b>(-33.26%)</b></td><td>0.02 <b>(+93.42%)</b></td><td>541.00 <b>(+49.82%)</b></td><td>381.70 <b>(+33.57%)</b></td><td>368.90 <b>(+38.22%)</b></td><td>243.30 (-2.91%)</td><td>129.15 <b>(+180.62%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>361.10 (n/a)</td><td>285.76 (n/a)</td><td>266.90 (n/a)</td><td>250.60 (n/a)</td><td>46.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (-9.54%)</td><td>0.06 (+18.30%)</td><td>0.06 <b>(+57.83%)</b></td><td>0.03 (-4.07%)</td><td>0.02 <b>(-23.69%)</b></td><td>656.10 (+4.24%)</td><td>390.82 (-18.25%)</td><td>343.30 <b>(-36.65%)</b></td><td>250.00 (+10.52%)</td><td>155.52 (-1.42%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.40 (n/a)</td><td>478.06 (n/a)</td><td>541.90 (n/a)</td><td>226.20 (n/a)</td><td>157.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(+28.68%)</b></td><td>0.06 <b>(+28.56%)</b></td><td>0.06 <b>(+29.45%)</b></td><td>0.04 (+4.74%)</td><td>0.02 <b>(+52.44%)</b></td><td>572.30 (-4.52%)</td><td>392.68 (-18.76%)</td><td>362.20 <b>(-22.76%)</b></td><td>233.60 <b>(-22.29%)</b></td><td>140.65 (+13.70%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>599.40 (n/a)</td><td>483.38 (n/a)</td><td>468.90 (n/a)</td><td>300.60 (n/a)</td><td>123.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (-18.88%)</td><td>0.05 (-4.53%)</td><td>0.05 (+4.44%)</td><td>0.04 <b>(+72.31%)</b></td><td>0.02 <b>(-43.75%)</b></td><td>575.70 <b>(-41.97%)</b></td><td>428.54 (-14.15%)</td><td>434.60 (-4.25%)</td><td>259.90 <b>(+23.29%)</b></td><td>116.74 <b>(-61.50%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>992.10 (n/a)</td><td>499.16 (n/a)</td><td>453.90 (n/a)</td><td>210.80 (n/a)</td><td>303.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-14.37%)</td><td>0.05 (-15.76%)</td><td>0.04 (-16.88%)</td><td>0.02 <b>(-46.51%)</b></td><td>0.02 (+8.17%)</td><td>1089.20 <b>(+86.96%)</b></td><td>557.00 <b>(+34.29%)</b></td><td>519.30 <b>(+20.29%)</b></td><td>287.70 (+16.76%)</td><td>323.13 <b>(+129.73%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.60 (n/a)</td><td>414.76 (n/a)</td><td>431.70 (n/a)</td><td>246.40 (n/a)</td><td>140.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 <b>(+22.68%)</b></td><td>0.09 <b>(+37.08%)</b></td><td>0.10 <b>(+35.27%)</b></td><td>0.04 (+18.38%)</td><td>0.03 (+15.62%)</td><td>570.00 (-15.53%)</td><td>301.22 <b>(-27.48%)</b></td><td>247.40 <b>(-26.06%)</b></td><td>199.20 (-18.49%)</td><td>153.17 (-17.00%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>674.80 (n/a)</td><td>415.36 (n/a)</td><td>334.60 (n/a)</td><td>244.40 (n/a)</td><td>184.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (+10.39%)</td><td>0.07 (+3.30%)</td><td>0.05 (+6.15%)</td><td>0.04 <b>(-20.44%)</b></td><td>0.03 <b>(+24.00%)</b></td><td>660.70 <b>(+25.68%)</b></td><td>421.06 (+1.35%)</td><td>448.90 (-5.79%)</td><td>248.30 (-9.41%)</td><td>163.80 <b>(+37.00%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>525.70 (n/a)</td><td>415.44 (n/a)</td><td>476.50 (n/a)</td><td>274.10 (n/a)</td><td>119.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 <b>(+74.70%)</b></td><td>0.07 (-10.33%)</td><td>0.06 <b>(-22.75%)</b></td><td>0.01 <b>(-82.60%)</b></td><td>0.05 <b>(+429.82%)</b></td><td>2097.40 <b>(+474.79%)</b></td><td>691.80 <b>(+122.26%)</b></td><td>381.50 <b>(+29.45%)</b></td><td>156.20 <b>(-42.74%)</b></td><td>795.55 <b>(+1838.41%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>364.90 (n/a)</td><td>311.26 (n/a)</td><td>294.70 (n/a)</td><td>272.80 (n/a)</td><td>41.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (-15.00%)</td><td>0.06 (-7.92%)</td><td>0.05 (+2.04%)</td><td>0.03 <b>(-26.85%)</b></td><td>0.02 (-8.10%)</td><td>712.10 <b>(+36.71%)</b></td><td>438.18 (+11.08%)</td><td>457.50 (-1.99%)</td><td>270.60 (+17.65%)</td><td>180.24 <b>(+37.52%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>520.90 (n/a)</td><td>394.48 (n/a)</td><td>466.80 (n/a)</td><td>230.00 (n/a)</td><td>131.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (+6.28%)</td><td>0.08 (+16.65%)</td><td>0.08 <b>(+27.95%)</b></td><td>0.04 (+10.83%)</td><td>0.03 (+7.86%)</td><td>599.00 (-9.78%)</td><td>365.74 (-14.33%)</td><td>323.60 <b>(-21.85%)</b></td><td>220.80 (-5.92%)</td><td>154.64 (-8.54%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>663.90 (n/a)</td><td>426.90 (n/a)</td><td>414.10 (n/a)</td><td>234.70 (n/a)</td><td>169.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 <b>(-35.59%)</b></td><td>0.06 (-13.62%)</td><td>0.05 (-6.53%)</td><td>0.05 <b>(+37.54%)</b></td><td>0.01 <b>(-75.76%)</b></td><td>484.80 <b>(-27.29%)</b></td><td>441.14 (+2.57%)</td><td>450.10 (+6.99%)</td><td>364.90 <b>(+55.28%)</b></td><td>45.49 <b>(-73.02%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>666.80 (n/a)</td><td>430.08 (n/a)</td><td>420.70 (n/a)</td><td>235.00 (n/a)</td><td>168.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (-7.52%)</td><td>0.06 (-3.47%)</td><td>0.07 (+13.70%)</td><td>0.04 (-6.87%)</td><td>0.02 <b>(+27.41%)</b></td><td>503.30 (+7.38%)</td><td>353.54 (+8.43%)</td><td>264.10 (-12.05%)</td><td>252.40 (+8.14%)</td><td>129.08 <b>(+45.33%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>468.70 (n/a)</td><td>326.06 (n/a)</td><td>300.30 (n/a)</td><td>233.40 (n/a)</td><td>88.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (+14.85%)</td><td>0.06 (+10.15%)</td><td>0.05 <b>(-27.99%)</b></td><td>0.03 <b>(+205.31%)</b></td><td>0.02 (-8.94%)</td><td>628.90 <b>(-67.25%)</b></td><td>385.44 <b>(-39.81%)</b></td><td>394.20 <b>(+38.85%)</b></td><td>215.10 (-12.91%)</td><td>168.18 <b>(-76.66%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1920.10 (n/a)</td><td>640.38 (n/a)</td><td>283.90 (n/a)</td><td>247.00 (n/a)</td><td>720.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(+64.60%)</b></td><td>0.05 <b>(+50.63%)</b></td><td>0.04 (+9.53%)</td><td>0.03 <b>(+246.66%)</b></td><td>0.02 <b>(+35.52%)</b></td><td>559.80 <b>(-71.15%)</b></td><td>406.60 <b>(-47.97%)</b></td><td>432.60 (-8.71%)</td><td>202.10 <b>(-39.25%)</b></td><td>136.75 <b>(-79.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1940.70 (n/a)</td><td>781.40 (n/a)</td><td>473.90 (n/a)</td><td>332.70 (n/a)</td><td>661.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 <b>(-41.89%)</b></td><td>0.03 <b>(-35.50%)</b></td><td>0.03 <b>(-30.47%)</b></td><td>0.02 <b>(-43.13%)</b></td><td>0.01 <b>(-40.38%)</b></td><td>1063.50 <b>(+75.84%)</b></td><td>655.96 <b>(+54.83%)</b></td><td>630.30 <b>(+43.81%)</b></td><td>386.40 <b>(+72.12%)</b></td><td>282.06 <b>(+67.86%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.80 (n/a)</td><td>423.66 (n/a)</td><td>438.30 (n/a)</td><td>224.50 (n/a)</td><td>168.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 <b>(+32.76%)</b></td><td>0.07 <b>(+67.31%)</b></td><td>0.07 <b>(+77.85%)</b></td><td>0.04 <b>(+65.66%)</b></td><td>0.02 (+17.70%)</td><td>467.00 <b>(-39.63%)</b></td><td>285.38 <b>(-42.03%)</b></td><td>252.00 <b>(-43.76%)</b></td><td>212.30 <b>(-24.66%)</b></td><td>103.20 <b>(-43.15%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>773.60 (n/a)</td><td>492.26 (n/a)</td><td>448.10 (n/a)</td><td>281.80 (n/a)</td><td>181.52 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(-46.71%)</b></td><td>0.03 (-14.37%)</td><td>0.03 (-9.89%)</td><td>0.03 <b>(+74.11%)</b></td><td>0.01 <b>(-76.27%)</b></td><td>639.10 <b>(-42.56%)</b></td><td>546.00 (-6.37%)</td><td>568.70 (+10.97%)</td><td>443.50 <b>(+87.69%)</b></td><td>82.40 <b>(-74.44%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1112.70 (n/a)</td><td>583.12 (n/a)</td><td>512.50 (n/a)</td><td>236.30 (n/a)</td><td>322.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.38 (-6.52%)</td><td>0.29 (-0.08%)</td><td>0.35 <b>(+30.72%)</b></td><td>0.18 (-7.16%)</td><td>0.10 (-4.81%)</td><td>554.50 (+7.71%)</td><td>375.14 (+0.89%)</td><td>282.40 <b>(-23.51%)</b></td><td>260.20 (+6.99%)</td><td>145.04 (+12.73%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>514.80 (n/a)</td><td>371.82 (n/a)</td><td>369.20 (n/a)</td><td>243.20 (n/a)</td><td>128.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.36 (-11.00%)</td><td>0.21 <b>(-34.08%)</b></td><td>0.21 <b>(-40.59%)</b></td><td>0.05 <b>(-75.77%)</b></td><td>0.13 <b>(+59.38%)</b></td><td>1877.40 <b>(+312.71%)</b></td><td>799.54 <b>(+138.33%)</b></td><td>467.50 <b>(+68.35%)</b></td><td>275.60 (+12.35%)</td><td>682.21 <b>(+592.15%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>454.90 (n/a)</td><td>335.48 (n/a)</td><td>277.70 (n/a)</td><td>245.30 (n/a)</td><td>98.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 <b>(-43.44%)</b></td><td>0.22 <b>(-40.57%)</b></td><td>0.22 <b>(-46.34%)</b></td><td>0.18 (+2.29%)</td><td>0.04 <b>(-65.07%)</b></td><td>544.30 (-2.24%)</td><td>462.26 <b>(+52.27%)</b></td><td>452.20 <b>(+86.32%)</b></td><td>349.40 <b>(+76.73%)</b></td><td>82.64 <b>(-42.84%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>556.80 (n/a)</td><td>303.58 (n/a)</td><td>242.70 (n/a)</td><td>197.70 (n/a)</td><td>144.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.24 (-15.76%)</td><td>0.17 <b>(-30.25%)</b></td><td>0.20 <b>(-23.76%)</b></td><td>0.04 <b>(-79.95%)</b></td><td>0.08 <b>(+138.29%)</b></td><td>1877.60 <b>(+398.83%)</b></td><td>667.62 <b>(+122.58%)</b></td><td>367.00 <b>(+31.17%)</b></td><td>305.90 (+18.70%)</td><td>679.79 <b>(+1357.09%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>376.40 (n/a)</td><td>299.94 (n/a)</td><td>279.80 (n/a)</td><td>257.70 (n/a)</td><td>46.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (+3.29%)</td><td>0.18 (-1.75%)</td><td>0.16 (+10.46%)</td><td>0.14 (+16.18%)</td><td>0.05 <b>(-24.14%)</b></td><td>521.10 (-13.94%)</td><td>433.02 (-4.19%)</td><td>455.50 (-9.48%)</td><td>267.80 (-3.18%)</td><td>96.43 <b>(-39.19%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>605.50 (n/a)</td><td>451.96 (n/a)</td><td>503.20 (n/a)</td><td>276.60 (n/a)</td><td>158.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 <b>(-27.09%)</b></td><td>0.18 <b>(-23.09%)</b></td><td>0.17 <b>(-35.85%)</b></td><td>0.12 (+11.27%)</td><td>0.06 <b>(-46.56%)</b></td><td>602.10 (-10.12%)</td><td>430.18 (+14.40%)</td><td>430.40 <b>(+55.89%)</b></td><td>267.50 <b>(+37.18%)</b></td><td>124.47 <b>(-37.09%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>669.90 (n/a)</td><td>376.04 (n/a)</td><td>276.10 (n/a)</td><td>195.00 (n/a)</td><td>197.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (-0.10%)</td><td>0.12 (+3.61%)</td><td>0.13 (+0.23%)</td><td>0.07 (-3.94%)</td><td>0.03 (+8.89%)</td><td>562.30 (+4.11%)</td><td>331.56 (-1.95%)</td><td>288.70 (-0.21%)</td><td>249.50 (+0.08%)</td><td>131.21 (+11.88%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>540.10 (n/a)</td><td>338.14 (n/a)</td><td>289.30 (n/a)</td><td>249.30 (n/a)</td><td>117.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (+2.42%)</td><td>0.12 (-9.59%)</td><td>0.12 (-9.76%)</td><td>0.09 <b>(-27.01%)</b></td><td>0.03 <b>(+112.70%)</b></td><td>425.70 <b>(+36.97%)</b></td><td>318.16 (+14.50%)</td><td>303.50 (+10.81%)</td><td>244.20 (-2.36%)</td><td>74.65 <b>(+182.54%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>310.80 (n/a)</td><td>277.86 (n/a)</td><td>273.90 (n/a)</td><td>250.10 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.18 (+6.75%)</td><td>0.11 (+16.87%)</td><td>0.10 <b>(+20.72%)</b></td><td>0.08 <b>(+31.40%)</b></td><td>0.04 (-3.12%)</td><td>457.60 <b>(-23.90%)</b></td><td>354.34 (-16.98%)</td><td>370.30 (-17.16%)</td><td>203.20 (-6.32%)</td><td>102.75 <b>(-26.41%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>601.30 (n/a)</td><td>426.80 (n/a)</td><td>447.00 (n/a)</td><td>216.90 (n/a)</td><td>139.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 <b>(-22.01%)</b></td><td>0.12 (+2.94%)</td><td>0.12 <b>(+24.30%)</b></td><td>0.06 (-6.79%)</td><td>0.04 <b>(-31.25%)</b></td><td>568.70 (+7.30%)</td><td>348.70 (-8.23%)</td><td>305.80 (-19.57%)</td><td>240.40 <b>(+28.21%)</b></td><td>134.92 (-11.18%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>530.00 (n/a)</td><td>379.98 (n/a)</td><td>380.20 (n/a)</td><td>187.50 (n/a)</td><td>151.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 <b>(+40.74%)</b></td><td>0.11 <b>(+28.42%)</b></td><td>0.12 <b>(+53.14%)</b></td><td>0.06 (+2.88%)</td><td>0.04 <b>(+141.39%)</b></td><td>570.60 (-2.81%)</td><td>388.16 (-15.32%)</td><td>303.80 <b>(-34.69%)</b></td><td>252.50 <b>(-28.93%)</b></td><td>149.17 <b>(+72.87%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.10 (n/a)</td><td>458.40 (n/a)</td><td>465.20 (n/a)</td><td>355.30 (n/a)</td><td>86.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (+2.64%)</td><td>0.12 (+12.53%)</td><td>0.13 <b>(+40.06%)</b></td><td>0.07 (-8.51%)</td><td>0.04 <b>(+27.28%)</b></td><td>545.50 (+9.32%)</td><td>364.10 (-5.95%)</td><td>292.60 <b>(-28.60%)</b></td><td>228.00 (-2.61%)</td><td>152.53 <b>(+38.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.00 (n/a)</td><td>387.14 (n/a)</td><td>409.80 (n/a)</td><td>234.10 (n/a)</td><td>110.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (+6.71%)</td><td>0.14 <b>(+33.47%)</b></td><td>0.14 <b>(+56.28%)</b></td><td>0.08 (+19.61%)</td><td>0.03 (-15.62%)</td><td>507.30 (-16.40%)</td><td>321.92 <b>(-28.32%)</b></td><td>290.10 <b>(-36.02%)</b></td><td>250.00 (-6.30%)</td><td>104.99 <b>(-32.52%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>606.80 (n/a)</td><td>449.10 (n/a)</td><td>453.40 (n/a)</td><td>266.80 (n/a)</td><td>155.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (+7.63%)</td><td>0.10 (+7.19%)</td><td>0.08 (-5.03%)</td><td>0.08 (+19.98%)</td><td>0.04 <b>(+20.28%)</b></td><td>537.60 (-16.65%)</td><td>428.42 (-5.41%)</td><td>497.10 (+5.30%)</td><td>269.60 (-7.07%)</td><td>130.81 (-3.36%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>645.00 (n/a)</td><td>452.92 (n/a)</td><td>472.10 (n/a)</td><td>290.10 (n/a)</td><td>135.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 <b>(-27.80%)</b></td><td>0.09 <b>(-28.61%)</b></td><td>0.08 <b>(-29.02%)</b></td><td>0.07 (+4.74%)</td><td>0.03 <b>(-44.16%)</b></td><td>553.30 (-4.52%)</td><td>490.92 <b>(+29.65%)</b></td><td>533.40 <b>(+40.89%)</b></td><td>291.40 <b>(+38.50%)</b></td><td>112.25 <b>(-26.13%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>579.50 (n/a)</td><td>378.64 (n/a)</td><td>378.60 (n/a)</td><td>210.40 (n/a)</td><td>151.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.20 (+6.99%)</td><td>0.12 (+16.75%)</td><td>0.11 <b>(+41.99%)</b></td><td>0.08 <b>(+105.45%)</b></td><td>0.05 <b>(-25.93%)</b></td><td>503.10 <b>(-51.32%)</b></td><td>366.52 <b>(-31.82%)</b></td><td>376.30 <b>(-29.57%)</b></td><td>202.50 (-6.51%)</td><td>121.39 <b>(-63.64%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.07 (n/a)</td><td>1033.50 (n/a)</td><td>537.58 (n/a)</td><td>534.30 (n/a)</td><td>216.60 (n/a)</td><td>333.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (+3.97%)</td><td>0.12 (+15.24%)</td><td>0.13 <b>(+31.59%)</b></td><td>0.07 (-6.44%)</td><td>0.05 <b>(+36.32%)</b></td><td>612.60 (+6.89%)</td><td>396.78 (-7.09%)</td><td>314.50 <b>(-24.02%)</b></td><td>248.50 (-3.83%)</td><td>171.07 <b>(+44.59%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>573.10 (n/a)</td><td>427.04 (n/a)</td><td>413.90 (n/a)</td><td>258.40 (n/a)</td><td>118.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-6.57%)</td><td>0.10 (+7.07%)</td><td>0.12 <b>(+24.92%)</b></td><td>0.04 <b>(+88.11%)</b></td><td>0.04 (-15.80%)</td><td>1048.00 <b>(-46.84%)</b></td><td>511.88 <b>(-27.67%)</b></td><td>346.20 (-19.95%)</td><td>308.40 (+7.05%)</td><td>309.93 <b>(-56.39%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1971.40 (n/a)</td><td>707.68 (n/a)</td><td>432.50 (n/a)</td><td>288.10 (n/a)</td><td>710.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (-7.44%)</td><td>0.10 (-4.17%)</td><td>0.09 (+6.08%)</td><td>0.06 (+11.74%)</td><td>0.03 <b>(-21.03%)</b></td><td>548.90 (-10.52%)</td><td>397.86 (-0.31%)</td><td>384.00 (-5.74%)</td><td>257.90 (+8.04%)</td><td>135.30 (-16.89%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>613.40 (n/a)</td><td>399.10 (n/a)</td><td>407.40 (n/a)</td><td>238.70 (n/a)</td><td>162.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.19 (+15.74%)</td><td>0.13 (+14.36%)</td><td>0.13 (+14.62%)</td><td>0.08 (+2.06%)</td><td>0.04 <b>(+40.04%)</b></td><td>416.30 (-2.02%)</td><td>288.56 (-9.39%)</td><td>278.20 (-12.74%)</td><td>181.20 (-13.59%)</td><td>93.57 <b>(+22.84%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>424.90 (n/a)</td><td>318.48 (n/a)</td><td>318.80 (n/a)</td><td>209.70 (n/a)</td><td>76.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 <b>(-23.69%)</b></td><td>0.08 (-9.58%)</td><td>0.08 (+14.56%)</td><td>0.06 <b>(+43.43%)</b></td><td>0.02 <b>(-55.44%)</b></td><td>535.70 <b>(-30.27%)</b></td><td>435.92 (-3.80%)</td><td>426.00 (-12.72%)</td><td>319.50 <b>(+31.05%)</b></td><td>95.82 <b>(-54.99%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>768.30 (n/a)</td><td>453.14 (n/a)</td><td>488.10 (n/a)</td><td>243.80 (n/a)</td><td>212.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (+13.25%)</td><td>0.10 (+11.28%)</td><td>0.08 (+7.38%)</td><td>0.05 (-10.23%)</td><td>0.05 <b>(+25.01%)</b></td><td>666.00 (+11.41%)</td><td>407.68 (-5.63%)</td><td>428.20 (-6.87%)</td><td>208.10 (-11.71%)</td><td>179.58 (+19.46%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>597.80 (n/a)</td><td>431.98 (n/a)</td><td>459.80 (n/a)</td><td>235.70 (n/a)</td><td>150.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 <b>(-29.27%)</b></td><td>0.08 <b>(-21.35%)</b></td><td>0.07 <b>(-30.18%)</b></td><td>0.02 <b>(-62.38%)</b></td><td>0.04 (-18.41%)</td><td>1905.20 <b>(+165.83%)</b></td><td>716.00 <b>(+58.92%)</b></td><td>512.80 <b>(+43.24%)</b></td><td>279.10 <b>(+41.39%)</b></td><td>676.83 <b>(+190.41%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>716.70 (n/a)</td><td>450.54 (n/a)</td><td>358.00 (n/a)</td><td>197.40 (n/a)</td><td>233.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (-7.07%)</td><td>0.09 <b>(-23.97%)</b></td><td>0.07 <b>(-37.36%)</b></td><td>0.05 (-18.87%)</td><td>0.04 (+5.60%)</td><td>644.20 <b>(+23.24%)</b></td><td>433.12 <b>(+36.16%)</b></td><td>472.50 <b>(+59.63%)</b></td><td>243.90 (+7.59%)</td><td>161.08 <b>(+34.13%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>522.70 (n/a)</td><td>318.10 (n/a)</td><td>296.00 (n/a)</td><td>226.70 (n/a)</td><td>120.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.47 (-6.57%)</td><td>0.32 <b>(-27.42%)</b></td><td>0.26 <b>(-40.10%)</b></td><td>0.21 <b>(-44.12%)</b></td><td>0.12 <b>(+138.49%)</b></td><td>620.40 <b>(+78.94%)</b></td><td>451.32 <b>(+50.75%)</b></td><td>508.60 <b>(+66.97%)</b></td><td>280.90 (+7.05%)</td><td>149.28 <b>(+344.29%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.05 (n/a)</td><td>346.70 (n/a)</td><td>299.38 (n/a)</td><td>304.60 (n/a)</td><td>262.40 (n/a)</td><td>33.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.47 (-14.29%)</td><td>0.37 (-7.73%)</td><td>0.44 (+2.45%)</td><td>0.24 (+11.30%)</td><td>0.11 (-13.36%)</td><td>552.30 (-10.15%)</td><td>385.58 (+5.99%)</td><td>300.80 (-2.37%)</td><td>279.20 (+16.67%)</td><td>131.25 (-12.44%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.55 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>614.70 (n/a)</td><td>363.78 (n/a)</td><td>308.10 (n/a)</td><td>239.30 (n/a)</td><td>149.89 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.42 (-16.18%)</td><td>0.31 <b>(-23.38%)</b></td><td>0.29 <b>(-28.60%)</b></td><td>0.26 (-11.13%)</td><td>0.06 <b>(-21.09%)</b></td><td>512.20 (+12.52%)</td><td>432.40 <b>(+29.59%)</b></td><td>450.50 <b>(+40.04%)</b></td><td>314.00 (+19.30%)</td><td>74.12 (+0.10%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>455.20 (n/a)</td><td>333.66 (n/a)</td><td>321.70 (n/a)</td><td>263.20 (n/a)</td><td>74.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+3.73%)</td><td>0.01 (+0.05%)</td><td>0.01 (-10.68%)</td><td>0.01 (+4.68%)</td><td>0.00 (+19.76%)</td><td>516.80 (-4.47%)</td><td>359.60 (+2.35%)</td><td>329.40 (+11.93%)</td><td>229.50 (-3.57%)</td><td>129.04 (+8.13%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.00 (n/a)</td><td>351.34 (n/a)</td><td>294.30 (n/a)</td><td>238.00 (n/a)</td><td>119.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-6.35%)</td><td>0.01 (-5.19%)</td><td>0.01 (-0.01%)</td><td>0.01 (+11.44%)</td><td>0.00 (-5.11%)</td><td>462.40 (-10.28%)</td><td>341.74 (+4.24%)</td><td>284.40 (+0.00%)</td><td>272.30 (+6.78%)</td><td>90.24 (-15.41%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.40 (n/a)</td><td>327.84 (n/a)</td><td>284.40 (n/a)</td><td>255.00 (n/a)</td><td>106.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-2.88%)</td><td>0.01 (+19.24%)</td><td>0.01 (+16.46%)</td><td>0.01 <b>(+415.54%)</b></td><td>0.00 <b>(-45.73%)</b></td><td>475.40 <b>(-80.60%)</b></td><td>399.94 <b>(-51.81%)</b></td><td>437.90 (-14.14%)</td><td>258.50 (+2.99%)</td><td>91.98 <b>(-89.97%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2451.10 (n/a)</td><td>829.98 (n/a)</td><td>510.00 (n/a)</td><td>251.00 (n/a)</td><td>917.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.48 (-2.91%)</td><td>6.15 (+15.59%)</td><td>6.43 <b>(+36.49%)</b></td><td>5.03 <b>(+25.74%)</b></td><td>1.05 <b>(-26.89%)</b></td><td>417.10 <b>(-20.48%)</b></td><td>349.46 (-15.65%)</td><td>326.20 <b>(-26.73%)</b></td><td>280.50 (+3.01%)</td><td>60.30 <b>(-35.83%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.70 (n/a)</td><td>5.32 (n/a)</td><td>4.71 (n/a)</td><td>4.00 (n/a)</td><td>1.43 (n/a)</td><td>524.50 (n/a)</td><td>414.32 (n/a)</td><td>445.20 (n/a)</td><td>272.30 (n/a)</td><td>93.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.51 (-0.73%)</td><td>0.43 <b>(+35.98%)</b></td><td>0.43 <b>(+39.70%)</b></td><td>0.30 <b>(+47.99%)</b></td><td>0.09 <b>(-26.74%)</b></td><td>447.60 <b>(-32.43%)</b></td><td>317.90 <b>(-30.62%)</b></td><td>309.00 <b>(-28.42%)</b></td><td>257.80 (+0.74%)</td><td>77.15 <b>(-48.26%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.52 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>662.40 (n/a)</td><td>458.22 (n/a)</td><td>431.70 (n/a)</td><td>255.90 (n/a)</td><td>149.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.74 <b>(+60.84%)</b></td><td>0.52 <b>(+68.52%)</b></td><td>0.53 <b>(+65.79%)</b></td><td>0.24 <b>(+275.65%)</b></td><td>0.18 (+15.02%)</td><td>548.60 <b>(-73.38%)</b></td><td>291.84 <b>(-58.96%)</b></td><td>250.30 <b>(-39.67%)</b></td><td>177.50 <b>(-37.85%)</b></td><td>147.42 <b>(-80.59%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>0.16 (n/a)</td><td>2060.60 (n/a)</td><td>711.04 (n/a)</td><td>414.90 (n/a)</td><td>285.60 (n/a)</td><td>759.32 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 (+9.86%)</td><td>0.34 (+8.87%)</td><td>0.30 (+1.10%)</td><td>0.23 (+8.40%)</td><td>0.12 <b>(+35.66%)</b></td><td>569.00 (-7.73%)</td><td>418.50 (-5.37%)</td><td>436.30 (-1.09%)</td><td>273.20 (-8.96%)</td><td>132.35 (+11.66%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>616.70 (n/a)</td><td>442.24 (n/a)</td><td>441.10 (n/a)</td><td>300.10 (n/a)</td><td>118.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.60 (-0.20%)</td><td>0.43 (-5.28%)</td><td>0.42 (-10.65%)</td><td>0.26 <b>(+31.36%)</b></td><td>0.17 (+8.00%)</td><td>513.20 <b>(-23.87%)</b></td><td>355.36 (+3.24%)</td><td>317.90 (+11.90%)</td><td>218.80 (+0.18%)</td><td>144.62 <b>(-22.73%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.60 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>674.10 (n/a)</td><td>344.22 (n/a)</td><td>284.10 (n/a)</td><td>218.40 (n/a)</td><td>187.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.50 (-13.20%)</td><td>0.35 (-13.22%)</td><td>0.27 <b>(-31.89%)</b></td><td>0.22 <b>(-29.61%)</b></td><td>0.13 <b>(+25.10%)</b></td><td>605.40 <b>(+42.08%)</b></td><td>427.78 <b>(+22.97%)</b></td><td>484.50 <b>(+46.82%)</b></td><td>265.20 (+15.20%)</td><td>152.37 <b>(+86.55%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.57 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>426.10 (n/a)</td><td>347.88 (n/a)</td><td>330.00 (n/a)</td><td>230.20 (n/a)</td><td>81.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (-19.11%)</td><td>0.01 <b>(-32.83%)</b></td><td>0.01 <b>(-39.35%)</b></td><td>0.01 <b>(-29.07%)</b></td><td>0.00 (-8.17%)</td><td>673.40 <b>(+40.97%)</b></td><td>459.48 <b>(+53.16%)</b></td><td>449.70 <b>(+64.85%)</b></td><td>268.20 <b>(+23.59%)</b></td><td>160.05 <b>(+53.76%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>477.70 (n/a)</td><td>300.00 (n/a)</td><td>272.80 (n/a)</td><td>217.00 (n/a)</td><td>104.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (+9.84%)</td><td>0.01 (+9.82%)</td><td>0.01 (-1.33%)</td><td>0.01 (+8.35%)</td><td>0.00 (+4.43%)</td><td>495.30 (-7.70%)</td><td>327.04 (-10.08%)</td><td>304.20 (+1.37%)</td><td>207.90 (-8.94%)</td><td>113.57 (-15.20%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.60 (n/a)</td><td>363.72 (n/a)</td><td>300.10 (n/a)</td><td>228.30 (n/a)</td><td>133.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-11.06%)</td><td>22496.59 <b>(+21.48%)</b></td><td>14527.35 <b>(+35.63%)</b></td><td>16735.20 <b>(+158.59%)</b></td><td>5598.71 (-1.11%)</td><td>7561.35 (+16.37%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18518.64 (n/a)</td><td>10710.67 (n/a)</td><td>6471.73 (n/a)</td><td>5661.55 (n/a)</td><td>6497.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.00 (+16.67%)</td><td>0.00 (+16.13%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+32.20%)</b></td><td>23099.68 (+5.88%)</td><td>14669.65 (-7.57%)</td><td>15685.36 (-6.75%)</td><td>5879.06 (-13.83%)</td><td>7030.36 <b>(+28.08%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21817.34 (n/a)</td><td>15871.19 (n/a)</td><td>16820.49 (n/a)</td><td>6822.26 (n/a)</td><td>5488.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 <b>(-22.82%)</b></td><td>0.09 (+2.38%)</td><td>0.09 (+19.17%)</td><td>0.08 (+12.97%)</td><td>0.02 <b>(-55.24%)</b></td><td>25600.61 (-11.52%)</td><td>22629.24 (-8.94%)</td><td>23586.36 (-16.05%)</td><td>16942.91 <b>(+29.56%)</b></td><td>3464.67 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>28934.00 (n/a)</td><td>24850.20 (n/a)</td><td>28095.55 (n/a)</td><td>13077.47 (n/a)</td><td>6676.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.59 <b>(-27.95%)</b></td><td>1.36 (-8.49%)</td><td>1.62 (+11.93%)</td><td>0.31 (+3.76%)</td><td>1.01 <b>(-22.02%)</b></td><td>3342.20 (-3.63%)</td><td>1649.14 (+16.05%)</td><td>646.20 (-10.65%)</td><td>404.70 <b>(+38.79%)</b></td><td>1534.05 (+18.09%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.60 (n/a)</td><td>1.48 (n/a)</td><td>1.45 (n/a)</td><td>0.30 (n/a)</td><td>1.30 (n/a)</td><td>3468.00 (n/a)</td><td>1421.00 (n/a)</td><td>723.20 (n/a)</td><td>291.60 (n/a)</td><td>1299.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.85 <b>(-33.12%)</b></td><td>2.01 (-4.06%)</td><td>2.39 <b>(+44.98%)</b></td><td>1.00 <b>(-28.79%)</b></td><td>0.88 <b>(-27.89%)</b></td><td>1048.60 <b>(+40.43%)</b></td><td>634.78 (+6.97%)</td><td>438.10 <b>(-31.02%)</b></td><td>367.40 <b>(+49.53%)</b></td><td>326.76 <b>(+60.52%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.27 (n/a)</td><td>2.10 (n/a)</td><td>1.65 (n/a)</td><td>1.40 (n/a)</td><td>1.22 (n/a)</td><td>746.70 (n/a)</td><td>593.40 (n/a)</td><td>635.10 (n/a)</td><td>245.70 (n/a)</td><td>203.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.79 <b>(+20.62%)</b></td><td>2.19 (+11.72%)</td><td>1.51 (-2.65%)</td><td>1.41 (+8.15%)</td><td>1.06 <b>(+30.05%)</b></td><td>744.20 (-7.54%)</td><td>560.86 (-7.28%)</td><td>692.60 (+2.71%)</td><td>276.30 (-17.10%)</td><td>215.60 (+0.96%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.15 (n/a)</td><td>1.96 (n/a)</td><td>1.56 (n/a)</td><td>1.30 (n/a)</td><td>0.81 (n/a)</td><td>804.90 (n/a)</td><td>604.92 (n/a)</td><td>674.30 (n/a)</td><td>333.30 (n/a)</td><td>213.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.90 (+11.55%)</td><td>1.95 (+11.99%)</td><td>1.49 (-3.68%)</td><td>1.31 <b>(+337.78%)</b></td><td>1.10 (-4.33%)</td><td>800.70 <b>(-77.16%)</b></td><td>632.04 <b>(-45.00%)</b></td><td>701.70 (+3.82%)</td><td>268.70 (-10.37%)</td><td>212.46 <b>(-83.98%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.50 (n/a)</td><td>1.74 (n/a)</td><td>1.55 (n/a)</td><td>0.30 (n/a)</td><td>1.15 (n/a)</td><td>3505.20 (n/a)</td><td>1149.20 (n/a)</td><td>675.90 (n/a)</td><td>299.80 (n/a)</td><td>1326.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.36 (-13.80%)</td><td>1.66 <b>(-25.78%)</b></td><td>0.62 <b>(-70.04%)</b></td><td>0.58 (-16.87%)</td><td>1.44 (+1.83%)</td><td>3592.80 <b>(+20.29%)</b></td><td>2328.80 <b>(+63.07%)</b></td><td>3361.90 <b>(+233.79%)</b></td><td>624.00 (+16.01%)</td><td>1535.63 <b>(+46.49%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.90 (n/a)</td><td>2.23 (n/a)</td><td>2.08 (n/a)</td><td>0.70 (n/a)</td><td>1.41 (n/a)</td><td>2986.70 (n/a)</td><td>1428.10 (n/a)</td><td>1007.20 (n/a)</td><td>537.90 (n/a)</td><td>1048.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.00 <b>(+43.01%)</b></td><td>3.27 (+16.67%)</td><td>3.23 (+9.61%)</td><td>0.59 (+0.64%)</td><td>1.92 <b>(+34.33%)</b></td><td>3578.80 (-0.64%)</td><td>1173.34 (-5.73%)</td><td>650.00 (-8.77%)</td><td>349.40 <b>(-30.08%)</b></td><td>1350.96 (+1.91%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>4.20 (n/a)</td><td>2.80 (n/a)</td><td>2.94 (n/a)</td><td>0.58 (n/a)</td><td>1.43 (n/a)</td><td>3601.90 (n/a)</td><td>1244.72 (n/a)</td><td>712.50 (n/a)</td><td>499.70 (n/a)</td><td>1325.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.40 (+1.64%)</td><td>2.85 (-19.71%)</td><td>3.04 <b>(-31.18%)</b></td><td>0.60 (-0.67%)</td><td>1.76 (-8.86%)</td><td>3518.10 (+0.68%)</td><td>1257.88 (+12.37%)</td><td>689.60 <b>(+45.30%)</b></td><td>388.50 (-1.62%)</td><td>1284.75 (-3.93%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.31 (n/a)</td><td>3.55 (n/a)</td><td>4.42 (n/a)</td><td>0.60 (n/a)</td><td>1.94 (n/a)</td><td>3494.50 (n/a)</td><td>1119.36 (n/a)</td><td>474.60 (n/a)</td><td>394.90 (n/a)</td><td>1337.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.28 (-10.05%)</td><td>2.90 (-3.56%)</td><td>2.69 (-14.31%)</td><td>0.59 (-2.03%)</td><td>2.00 (+2.69%)</td><td>3566.60 (+2.07%)</td><td>1337.00 (+8.39%)</td><td>780.10 (+16.71%)</td><td>397.30 (+11.16%)</td><td>1318.23 (+2.46%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.87 (n/a)</td><td>3.01 (n/a)</td><td>3.14 (n/a)</td><td>0.60 (n/a)</td><td>1.94 (n/a)</td><td>3494.10 (n/a)</td><td>1233.46 (n/a)</td><td>668.40 (n/a)</td><td>357.40 (n/a)</td><td>1286.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.88 <b>(-23.45%)</b></td><td>3.96 (+9.75%)</td><td>3.90 (+13.07%)</td><td>3.05 <b>(+180.64%)</b></td><td>0.72 <b>(-62.12%)</b></td><td>687.20 <b>(-64.37%)</b></td><td>544.16 <b>(-32.95%)</b></td><td>538.40 (-11.55%)</td><td>429.90 <b>(+30.63%)</b></td><td>100.86 <b>(-84.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.37 (n/a)</td><td>3.61 (n/a)</td><td>3.45 (n/a)</td><td>1.09 (n/a)</td><td>1.89 (n/a)</td><td>1928.60 (n/a)</td><td>811.52 (n/a)</td><td>608.70 (n/a)</td><td>329.10 (n/a)</td><td>637.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.35 <b>(-35.35%)</b></td><td>3.79 (+10.82%)</td><td>3.61 <b>(+43.49%)</b></td><td>2.89 <b>(+395.97%)</b></td><td>1.00 <b>(-66.21%)</b></td><td>725.60 <b>(-79.84%)</b></td><td>581.20 <b>(-54.01%)</b></td><td>580.20 <b>(-30.31%)</b></td><td>392.10 <b>(+54.67%)</b></td><td>136.60 <b>(-89.82%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>8.27 (n/a)</td><td>3.42 (n/a)</td><td>2.52 (n/a)</td><td>0.58 (n/a)</td><td>2.95 (n/a)</td><td>3599.00 (n/a)</td><td>1263.72 (n/a)</td><td>832.60 (n/a)</td><td>253.50 (n/a)</td><td>1341.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.05 (-6.99%)</td><td>3.65 <b>(+24.87%)</b></td><td>4.16 <b>(+89.53%)</b></td><td>1.11 (+0.42%)</td><td>1.52 (-16.37%)</td><td>3762.60 (-0.42%)</td><td>1550.48 <b>(-22.17%)</b></td><td>1008.40 <b>(-47.23%)</b></td><td>830.70 (+7.52%)</td><td>1243.89 (+2.23%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>5.43 (n/a)</td><td>2.92 (n/a)</td><td>2.19 (n/a)</td><td>1.11 (n/a)</td><td>1.82 (n/a)</td><td>3778.40 (n/a)</td><td>1992.20 (n/a)</td><td>1911.10 (n/a)</td><td>772.60 (n/a)</td><td>1216.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>8.75 (+9.91%)</td><td>5.78 <b>(+25.47%)</b></td><td>5.91 (+1.91%)</td><td>3.60 <b>(+203.28%)</b></td><td>2.09 <b>(-30.18%)</b></td><td>1165.00 <b>(-67.03%)</b></td><td>807.12 <b>(-48.98%)</b></td><td>709.70 (-1.88%)</td><td>479.60 (-9.01%)</td><td>289.97 <b>(-78.54%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>7.96 (n/a)</td><td>4.61 (n/a)</td><td>5.80 (n/a)</td><td>1.19 (n/a)</td><td>3.00 (n/a)</td><td>3533.10 (n/a)</td><td>1582.02 (n/a)</td><td>723.30 (n/a)</td><td>527.10 (n/a)</td><td>1351.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.38 (+14.93%)</td><td>4.96 (+0.21%)</td><td>5.94 (-4.75%)</td><td>1.26 (+6.30%)</td><td>2.50 (+12.33%)</td><td>3322.90 (-5.93%)</td><td>1277.72 (-0.62%)</td><td>705.80 (+4.98%)</td><td>568.20 (-12.99%)</td><td>1166.38 (-7.44%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>6.42 (n/a)</td><td>4.95 (n/a)</td><td>6.24 (n/a)</td><td>1.19 (n/a)</td><td>2.23 (n/a)</td><td>3532.40 (n/a)</td><td>1285.66 (n/a)</td><td>672.30 (n/a)</td><td>653.00 (n/a)</td><td>1260.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.57 <b>(-32.34%)</b></td><td>3.51 <b>(-48.59%)</b></td><td>3.91 <b>(-38.38%)</b></td><td>1.10 <b>(-74.07%)</b></td><td>2.11 (+5.99%)</td><td>3796.30 <b>(+285.72%)</b></td><td>1730.10 <b>(+162.51%)</b></td><td>1071.50 <b>(+62.30%)</b></td><td>638.70 <b>(+47.81%)</b></td><td>1273.01 <b>(+521.89%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>9.71 (n/a)</td><td>6.84 (n/a)</td><td>6.35 (n/a)</td><td>4.26 (n/a)</td><td>1.99 (n/a)</td><td>984.20 (n/a)</td><td>659.06 (n/a)</td><td>660.20 (n/a)</td><td>432.10 (n/a)</td><td>204.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>8.40 (-16.60%)</td><td>6.93 (-2.27%)</td><td>7.17 (-3.80%)</td><td>3.98 (+11.90%)</td><td>1.81 <b>(-22.84%)</b></td><td>1055.10 (-10.64%)</td><td>652.36 (-2.05%)</td><td>584.90 (+3.95%)</td><td>499.50 (+19.93%)</td><td>231.43 <b>(-22.21%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>10.07 (n/a)</td><td>7.10 (n/a)</td><td>7.45 (n/a)</td><td>3.55 (n/a)</td><td>2.35 (n/a)</td><td>1180.70 (n/a)</td><td>666.00 (n/a)</td><td>562.70 (n/a)</td><td>416.50 (n/a)</td><td>297.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>9.27 (+3.61%)</td><td>5.30 (+3.49%)</td><td>4.27 <b>(-28.92%)</b></td><td>1.24 (+2.19%)</td><td>3.27 (+7.04%)</td><td>3375.50 (-2.14%)</td><td>1290.00 (-3.51%)</td><td>981.80 <b>(+40.68%)</b></td><td>452.50 (-3.50%)</td><td>1200.02 (-2.92%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>8.95 (n/a)</td><td>5.13 (n/a)</td><td>6.01 (n/a)</td><td>1.22 (n/a)</td><td>3.05 (n/a)</td><td>3449.40 (n/a)</td><td>1336.94 (n/a)</td><td>697.90 (n/a)</td><td>468.90 (n/a)</td><td>1236.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.49 (-5.20%)</td><td>1.15 (+2.27%)</td><td>1.10 (-0.70%)</td><td>0.63 (-2.05%)</td><td>0.35 (-17.10%)</td><td>835.60 (+2.09%)</td><td>502.90 (-4.91%)</td><td>477.90 (+0.72%)</td><td>351.50 (+5.49%)</td><td>196.12 (-7.07%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.57 (n/a)</td><td>1.12 (n/a)</td><td>1.10 (n/a)</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>818.50 (n/a)</td><td>528.88 (n/a)</td><td>474.50 (n/a)</td><td>333.20 (n/a)</td><td>211.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.80 <b>(+21.07%)</b></td><td>1.69 (+6.33%)</td><td>2.35 (+10.40%)</td><td>0.30 (+1.56%)</td><td>1.28 <b>(+46.40%)</b></td><td>3494.60 (-1.54%)</td><td>1623.98 <b>(+36.25%)</b></td><td>447.10 (-9.42%)</td><td>375.10 (-17.42%)</td><td>1671.67 <b>(+25.22%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>2.31 (n/a)</td><td>1.59 (n/a)</td><td>2.12 (n/a)</td><td>0.30 (n/a)</td><td>0.87 (n/a)</td><td>3549.10 (n/a)</td><td>1191.94 (n/a)</td><td>493.60 (n/a)</td><td>454.20 (n/a)</td><td>1334.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.55 (-3.73%)</td><td>2.08 (-6.43%)</td><td>2.26 (+13.20%)</td><td>0.60 (+3.62%)</td><td>1.44 <b>(+23.11%)</b></td><td>3516.90 (-3.50%)</td><td>1827.12 <b>(+29.34%)</b></td><td>929.80 (-11.66%)</td><td>590.90 (+3.89%)</td><td>1532.83 <b>(+21.01%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>3.69 (n/a)</td><td>2.23 (n/a)</td><td>1.99 (n/a)</td><td>0.58 (n/a)</td><td>1.17 (n/a)</td><td>3644.30 (n/a)</td><td>1412.64 (n/a)</td><td>1052.50 (n/a)</td><td>568.80 (n/a)</td><td>1266.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.77 (+10.77%)</td><td>1.21 (+14.62%)</td><td>1.54 <b>(+45.54%)</b></td><td>0.29 (+13.51%)</td><td>0.64 <b>(+20.29%)</b></td><td>1829.20 (-11.91%)</td><td>688.64 (-10.38%)</td><td>340.00 <b>(-31.30%)</b></td><td>296.50 (-9.71%)</td><td>655.03 (-11.34%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>1.60 (n/a)</td><td>1.06 (n/a)</td><td>1.06 (n/a)</td><td>0.25 (n/a)</td><td>0.53 (n/a)</td><td>2076.40 (n/a)</td><td>768.36 (n/a)</td><td>494.90 (n/a)</td><td>328.40 (n/a)</td><td>738.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 <b>(+26.00%)</b></td><td>0.08 (+19.32%)</td><td>0.07 (-3.27%)</td><td>0.06 <b>(+32.33%)</b></td><td>0.02 <b>(+40.81%)</b></td><td>555.60 <b>(-24.43%)</b></td><td>445.60 (-15.14%)</td><td>494.20 (+3.39%)</td><td>290.10 <b>(-20.65%)</b></td><td>124.76 (-14.66%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>735.20 (n/a)</td><td>525.08 (n/a)</td><td>478.00 (n/a)</td><td>365.60 (n/a)</td><td>146.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (-18.03%)</td><td>0.07 <b>(-20.96%)</b></td><td>0.06 (-18.22%)</td><td>0.04 <b>(-30.01%)</b></td><td>0.03 (-19.23%)</td><td>746.50 <b>(+42.87%)</b></td><td>507.50 <b>(+27.36%)</b></td><td>536.50 <b>(+22.27%)</b></td><td>300.40 <b>(+22.01%)</b></td><td>171.55 <b>(+37.14%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>522.50 (n/a)</td><td>398.48 (n/a)</td><td>438.80 (n/a)</td><td>246.20 (n/a)</td><td>125.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (-17.07%)</td><td>0.17 <b>(-22.27%)</b></td><td>0.18 <b>(-20.27%)</b></td><td>0.09 <b>(-39.78%)</b></td><td>0.05 <b>(+23.59%)</b></td><td>724.80 <b>(+66.09%)</b></td><td>430.58 <b>(+37.06%)</b></td><td>372.30 <b>(+25.44%)</b></td><td>305.90 <b>(+20.58%)</b></td><td>172.12 <b>(+141.59%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>436.40 (n/a)</td><td>314.16 (n/a)</td><td>296.80 (n/a)</td><td>253.70 (n/a)</td><td>71.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.32 (+17.89%)</td><td>0.19 (+2.22%)</td><td>0.14 (+0.15%)</td><td>0.11 (-18.84%)</td><td>0.09 <b>(+40.26%)</b></td><td>603.80 <b>(+23.20%)</b></td><td>412.64 (+5.75%)</td><td>469.10 (-0.15%)</td><td>206.90 (-15.17%)</td><td>169.63 <b>(+41.75%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>490.10 (n/a)</td><td>390.20 (n/a)</td><td>469.80 (n/a)</td><td>243.90 (n/a)</td><td>119.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (+4.80%)</td><td>0.17 (+13.76%)</td><td>0.14 (-3.97%)</td><td>0.11 <b>(+215.50%)</b></td><td>0.07 (-19.50%)</td><td>570.00 <b>(-68.30%)</b></td><td>425.26 <b>(-37.10%)</b></td><td>475.30 (+4.14%)</td><td>236.60 (-4.56%)</td><td>132.33 <b>(-79.14%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1798.30 (n/a)</td><td>676.10 (n/a)</td><td>456.40 (n/a)</td><td>247.90 (n/a)</td><td>634.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.55 (-10.80%)</td><td>0.41 (-10.75%)</td><td>0.42 (-15.15%)</td><td>0.29 (-13.53%)</td><td>0.10 (-18.86%)</td><td>450.00 (+15.62%)</td><td>333.78 (+10.84%)</td><td>311.50 (+17.86%)</td><td>236.30 (+12.15%)</td><td>79.60 (-0.00%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.62 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>389.20 (n/a)</td><td>301.14 (n/a)</td><td>264.30 (n/a)</td><td>210.70 (n/a)</td><td>79.60 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 (-9.91%)</td><td>0.34 (-14.26%)</td><td>0.30 <b>(-29.38%)</b></td><td>0.20 (-16.67%)</td><td>0.11 (-8.39%)</td><td>667.30 <b>(+20.02%)</b></td><td>424.72 (+17.42%)</td><td>431.40 <b>(+41.63%)</b></td><td>271.00 (+10.97%)</td><td>155.60 (+19.76%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.54 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>556.00 (n/a)</td><td>361.72 (n/a)</td><td>304.60 (n/a)</td><td>244.20 (n/a)</td><td>129.93 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.59 <b>(+21.32%)</b></td><td>0.28 <b>(-22.95%)</b></td><td>0.23 <b>(-34.88%)</b></td><td>0.12 <b>(-50.71%)</b></td><td>0.18 <b>(+80.13%)</b></td><td>1115.40 <b>(+102.87%)</b></td><td>603.60 <b>(+58.08%)</b></td><td>576.70 <b>(+53.58%)</b></td><td>223.60 (-17.58%)</td><td>322.35 <b>(+190.54%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>549.80 (n/a)</td><td>381.84 (n/a)</td><td>375.50 (n/a)</td><td>271.30 (n/a)</td><td>110.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 <b>(-46.33%)</b></td><td>0.03 <b>(-47.53%)</b></td><td>0.03 <b>(-28.51%)</b></td><td>0.01 <b>(-70.22%)</b></td><td>0.01 <b>(-22.24%)</b></td><td>1929.10 <b>(+235.85%)</b></td><td>884.38 <b>(+139.02%)</b></td><td>500.50 <b>(+39.88%)</b></td><td>424.60 <b>(+86.31%)</b></td><td>640.67 <b>(+378.23%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:41:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.40 (n/a)</td><td>370.00 (n/a)</td><td>357.80 (n/a)</td><td>227.90 (n/a)</td><td>133.97 (n/a)</td>
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
