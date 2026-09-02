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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-4.63%)</td><td>0.02 (-9.48%)</td><td>0.02 <b>(-28.03%)</b></td><td>0.01 (-3.09%)</td><td>0.01 (-10.00%)</td><td>540.90 (+3.19%)</td><td>387.20 (+8.62%)</td><td>375.50 <b>(+38.92%)</b></td><td>259.10 (+4.86%)</td><td>130.88 (-5.52%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>356.48 (n/a)</td><td>270.30 (n/a)</td><td>247.10 (n/a)</td><td>138.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (+7.61%)</td><td>0.02 (+11.39%)</td><td>0.02 (+12.22%)</td><td>0.01 (+17.29%)</td><td>0.01 (+6.27%)</td><td>544.70 (-14.74%)</td><td>375.28 (-10.91%)</td><td>322.40 (-10.89%)</td><td>239.50 (-7.06%)</td><td>126.39 (-14.97%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.90 (n/a)</td><td>421.22 (n/a)</td><td>361.80 (n/a)</td><td>257.70 (n/a)</td><td>148.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-8.36%)</td><td>0.02 (-10.23%)</td><td>0.01 (-13.00%)</td><td>0.01 <b>(-32.96%)</b></td><td>0.01 (+8.22%)</td><td>784.90 <b>(+49.16%)</b></td><td>453.28 <b>(+20.59%)</b></td><td>479.40 (+14.94%)</td><td>229.60 (+9.13%)</td><td>217.11 <b>(+76.07%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>526.20 (n/a)</td><td>375.88 (n/a)</td><td>417.10 (n/a)</td><td>210.40 (n/a)</td><td>123.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (+10.98%)</td><td>0.02 <b>(+32.99%)</b></td><td>0.02 <b>(+50.42%)</b></td><td>0.01 <b>(+113.70%)</b></td><td>0.01 <b>(-27.67%)</b></td><td>473.00 <b>(-53.21%)</b></td><td>330.30 <b>(-43.57%)</b></td><td>283.60 <b>(-33.52%)</b></td><td>213.90 (-9.90%)</td><td>119.49 <b>(-69.64%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1010.80 (n/a)</td><td>585.30 (n/a)</td><td>426.60 (n/a)</td><td>237.40 (n/a)</td><td>393.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(-49.51%)</b></td><td>0.01 <b>(-43.06%)</b></td><td>0.01 <b>(-32.10%)</b></td><td>0.00 <b>(-69.92%)</b></td><td>0.00 <b>(-45.49%)</b></td><td>1869.00 <b>(+232.44%)</b></td><td>762.42 <b>(+103.96%)</b></td><td>522.60 <b>(+47.29%)</b></td><td>418.20 <b>(+98.01%)</b></td><td>620.54 <b>(+295.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>373.80 (n/a)</td><td>354.80 (n/a)</td><td>211.20 (n/a)</td><td>156.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+3.40%)</td><td>0.02 (-7.75%)</td><td>0.02 (+19.05%)</td><td>0.01 <b>(-54.06%)</b></td><td>0.01 <b>(+31.06%)</b></td><td>1082.20 <b>(+117.66%)</b></td><td>495.72 <b>(+29.34%)</b></td><td>353.60 (-15.99%)</td><td>254.60 (-3.27%)</td><td>336.65 <b>(+209.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>497.20 (n/a)</td><td>383.28 (n/a)</td><td>420.90 (n/a)</td><td>263.20 (n/a)</td><td>108.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(-23.73%)</b></td><td>0.03 <b>(-24.48%)</b></td><td>0.03 <b>(-28.26%)</b></td><td>0.02 <b>(-23.67%)</b></td><td>0.01 <b>(-23.02%)</b></td><td>558.40 <b>(+30.99%)</b></td><td>430.40 <b>(+32.59%)</b></td><td>487.80 <b>(+39.41%)</b></td><td>301.00 <b>(+31.10%)</b></td><td>115.51 <b>(+32.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>426.30 (n/a)</td><td>324.60 (n/a)</td><td>349.90 (n/a)</td><td>229.60 (n/a)</td><td>87.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(-23.29%)</b></td><td>0.03 (-8.37%)</td><td>0.03 <b>(-24.40%)</b></td><td>0.03 <b>(+30.78%)</b></td><td>0.01 <b>(-48.46%)</b></td><td>478.00 <b>(-23.53%)</b></td><td>377.40 (-5.89%)</td><td>370.70 <b>(+32.30%)</b></td><td>274.70 <b>(+30.37%)</b></td><td>95.93 <b>(-53.04%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>625.10 (n/a)</td><td>401.04 (n/a)</td><td>280.20 (n/a)</td><td>210.70 (n/a)</td><td>204.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (-18.98%)</td><td>0.02 (-3.55%)</td><td>0.02 (+9.37%)</td><td>0.01 (-12.12%)</td><td>0.01 (-17.53%)</td><td>2112.00 (+13.80%)</td><td>814.16 (+6.21%)</td><td>534.80 (-8.57%)</td><td>315.00 <b>(+23.43%)</b></td><td>738.61 (+18.25%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1855.90 (n/a)</td><td>766.58 (n/a)</td><td>584.90 (n/a)</td><td>255.20 (n/a)</td><td>624.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-30.94%)</b></td><td>0.02 <b>(-39.33%)</b></td><td>0.02 <b>(-44.74%)</b></td><td>0.01 <b>(-65.61%)</b></td><td>0.01 <b>(-23.31%)</b></td><td>1877.70 <b>(+190.76%)</b></td><td>760.92 <b>(+100.18%)</b></td><td>494.00 <b>(+81.02%)</b></td><td>354.80 <b>(+44.82%)</b></td><td>631.51 <b>(+265.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.80 (n/a)</td><td>380.12 (n/a)</td><td>272.90 (n/a)</td><td>245.00 (n/a)</td><td>172.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(+54.91%)</b></td><td>0.03 <b>(+33.59%)</b></td><td>0.03 (-7.64%)</td><td>0.02 <b>(+37.13%)</b></td><td>0.01 <b>(+117.03%)</b></td><td>581.40 <b>(-27.08%)</b></td><td>421.42 (-19.97%)</td><td>480.00 (+8.28%)</td><td>249.30 <b>(-35.45%)</b></td><td>157.04 (-4.70%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>797.30 (n/a)</td><td>526.60 (n/a)</td><td>443.30 (n/a)</td><td>386.20 (n/a)</td><td>164.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (+2.38%)</td><td>0.04 <b>(+28.98%)</b></td><td>0.04 <b>(+63.47%)</b></td><td>0.02 <b>(+31.43%)</b></td><td>0.01 (-17.37%)</td><td>493.50 <b>(-23.91%)</b></td><td>336.32 <b>(-26.41%)</b></td><td>296.50 <b>(-38.82%)</b></td><td>232.10 (-2.31%)</td><td>101.92 <b>(-34.94%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>648.60 (n/a)</td><td>457.04 (n/a)</td><td>484.60 (n/a)</td><td>237.60 (n/a)</td><td>156.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 <b>(+65.97%)</b></td><td>0.09 (-0.47%)</td><td>0.07 <b>(-27.94%)</b></td><td>0.05 (-11.14%)</td><td>0.05 <b>(+163.35%)</b></td><td>506.10 (+12.54%)</td><td>354.22 (+17.47%)</td><td>374.30 <b>(+38.78%)</b></td><td>145.40 <b>(-39.77%)</b></td><td>150.24 <b>(+75.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>449.70 (n/a)</td><td>301.54 (n/a)</td><td>269.70 (n/a)</td><td>241.40 (n/a)</td><td>85.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (-10.89%)</td><td>0.08 (-13.04%)</td><td>0.06 <b>(-35.92%)</b></td><td>0.05 (-1.86%)</td><td>0.03 (+12.47%)</td><td>502.50 (+1.89%)</td><td>369.94 <b>(+20.42%)</b></td><td>429.10 <b>(+56.09%)</b></td><td>205.90 (+12.21%)</td><td>144.00 <b>(+24.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>493.20 (n/a)</td><td>307.22 (n/a)</td><td>274.90 (n/a)</td><td>183.50 (n/a)</td><td>115.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-12.00%)</td><td>0.06 <b>(-28.24%)</b></td><td>0.05 <b>(-40.65%)</b></td><td>0.04 <b>(-22.60%)</b></td><td>0.02 (-12.06%)</td><td>602.80 <b>(+29.19%)</b></td><td>448.20 <b>(+39.41%)</b></td><td>453.60 <b>(+68.50%)</b></td><td>241.60 (+13.64%)</td><td>131.13 (+16.44%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>466.60 (n/a)</td><td>321.50 (n/a)</td><td>269.20 (n/a)</td><td>212.60 (n/a)</td><td>112.61 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (-16.30%)</td><td>0.06 (-18.77%)</td><td>0.06 <b>(-30.43%)</b></td><td>0.04 (-7.72%)</td><td>0.02 <b>(-26.41%)</b></td><td>596.40 (+8.36%)</td><td>429.28 (+18.37%)</td><td>394.20 <b>(+43.71%)</b></td><td>279.40 (+19.45%)</td><td>150.40 (-3.68%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>550.40 (n/a)</td><td>362.66 (n/a)</td><td>274.30 (n/a)</td><td>233.90 (n/a)</td><td>156.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (+16.78%)</td><td>0.07 (-1.59%)</td><td>0.05 <b>(-34.92%)</b></td><td>0.04 (-16.28%)</td><td>0.04 <b>(+50.16%)</b></td><td>644.30 (+19.45%)</td><td>406.66 (+11.56%)</td><td>464.10 <b>(+53.62%)</b></td><td>201.50 (-14.36%)</td><td>181.24 <b>(+43.26%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>539.40 (n/a)</td><td>364.52 (n/a)</td><td>302.10 (n/a)</td><td>235.30 (n/a)</td><td>126.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 <b>(+50.66%)</b></td><td>0.06 (+16.66%)</td><td>0.05 (-6.37%)</td><td>0.04 (-6.68%)</td><td>0.03 <b>(+219.01%)</b></td><td>589.00 (+7.15%)</td><td>430.06 (-5.69%)</td><td>499.90 (+6.79%)</td><td>250.00 <b>(-33.63%)</b></td><td>147.65 <b>(+124.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>549.70 (n/a)</td><td>456.00 (n/a)</td><td>468.10 (n/a)</td><td>376.70 (n/a)</td><td>65.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (+3.07%)</td><td>0.15 (-1.87%)</td><td>0.13 <b>(-24.28%)</b></td><td>0.10 (-0.35%)</td><td>0.05 (+7.88%)</td><td>488.60 (+0.35%)</td><td>350.16 (+2.32%)</td><td>371.10 <b>(+32.06%)</b></td><td>235.60 (-2.97%)</td><td>107.36 (-1.47%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>486.90 (n/a)</td><td>342.22 (n/a)</td><td>281.00 (n/a)</td><td>242.80 (n/a)</td><td>108.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 <b>(+21.39%)</b></td><td>0.18 (+13.95%)</td><td>0.20 <b>(+24.37%)</b></td><td>0.09 <b>(-20.40%)</b></td><td>0.05 <b>(+66.05%)</b></td><td>524.60 <b>(+25.62%)</b></td><td>300.60 (-6.14%)</td><td>247.30 (-19.60%)</td><td>211.50 (-17.64%)</td><td>127.22 <b>(+88.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>417.60 (n/a)</td><td>320.28 (n/a)</td><td>307.60 (n/a)</td><td>256.80 (n/a)</td><td>67.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.22 (+7.29%)</td><td>0.18 (+0.70%)</td><td>0.20 (-1.16%)</td><td>0.10 <b>(-25.08%)</b></td><td>0.05 <b>(+44.85%)</b></td><td>502.80 <b>(+33.47%)</b></td><td>298.08 (+4.94%)</td><td>251.20 (+1.17%)</td><td>218.90 (-6.81%)</td><td>116.63 <b>(+91.55%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>376.70 (n/a)</td><td>284.06 (n/a)</td><td>248.30 (n/a)</td><td>234.90 (n/a)</td><td>60.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.24 (+17.40%)</td><td>0.16 (-1.97%)</td><td>0.17 (+1.79%)</td><td>0.08 (-15.97%)</td><td>0.07 <b>(+59.23%)</b></td><td>630.50 (+19.01%)</td><td>369.58 (+12.23%)</td><td>297.10 (-1.75%)</td><td>207.10 (-14.81%)</td><td>177.33 <b>(+54.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>529.80 (n/a)</td><td>329.32 (n/a)</td><td>302.40 (n/a)</td><td>243.10 (n/a)</td><td>115.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 <b>(+20.94%)</b></td><td>0.18 (+7.41%)</td><td>0.20 <b>(+21.78%)</b></td><td>0.10 <b>(-30.87%)</b></td><td>0.05 <b>(+172.80%)</b></td><td>493.00 <b>(+44.62%)</b></td><td>292.86 (+0.56%)</td><td>241.10 (-17.91%)</td><td>216.00 (-17.34%)</td><td>113.80 <b>(+249.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>340.90 (n/a)</td><td>291.24 (n/a)</td><td>293.70 (n/a)</td><td>261.30 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (+10.59%)</td><td>0.14 (-3.27%)</td><td>0.11 <b>(-33.79%)</b></td><td>0.10 <b>(+30.23%)</b></td><td>0.05 (-2.72%)</td><td>484.80 <b>(-23.22%)</b></td><td>385.52 (-0.06%)</td><td>440.70 <b>(+51.03%)</b></td><td>239.30 (-9.60%)</td><td>111.50 <b>(-29.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>631.40 (n/a)</td><td>385.74 (n/a)</td><td>291.80 (n/a)</td><td>264.70 (n/a)</td><td>158.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(+23.10%)</b></td><td>0.01 <b>(+21.95%)</b></td><td>0.01 <b>(+65.87%)</b></td><td>0.01 <b>(+41.20%)</b></td><td>0.00 (+8.44%)</td><td>522.20 <b>(-29.18%)</b></td><td>368.50 <b>(-20.14%)</b></td><td>296.30 <b>(-39.70%)</b></td><td>219.60 (-18.76%)</td><td>140.86 <b>(-26.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>737.40 (n/a)</td><td>461.44 (n/a)</td><td>491.40 (n/a)</td><td>270.30 (n/a)</td><td>192.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(-35.46%)</b></td><td>0.01 <b>(-25.77%)</b></td><td>0.01 (-15.62%)</td><td>0.00 <b>(-38.82%)</b></td><td>0.00 <b>(-22.98%)</b></td><td>773.00 <b>(+63.46%)</b></td><td>529.94 <b>(+36.72%)</b></td><td>478.60 (+18.52%)</td><td>454.50 <b>(+54.96%)</b></td><td>136.47 <b>(+102.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.90 (n/a)</td><td>387.62 (n/a)</td><td>403.80 (n/a)</td><td>293.30 (n/a)</td><td>67.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (+0.10%)</td><td>0.01 (-4.60%)</td><td>0.01 <b>(-32.19%)</b></td><td>0.00 (+2.12%)</td><td>0.00 (+2.17%)</td><td>553.50 (-2.07%)</td><td>395.72 (+4.03%)</td><td>443.50 <b>(+47.49%)</b></td><td>229.00 (-0.09%)</td><td>144.75 (-8.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>565.20 (n/a)</td><td>380.40 (n/a)</td><td>300.70 (n/a)</td><td>229.20 (n/a)</td><td>158.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-4.64%)</td><td>0.01 (-9.83%)</td><td>0.01 (-0.05%)</td><td>0.00 (+0.18%)</td><td>0.00 <b>(-22.54%)</b></td><td>538.60 (-0.19%)</td><td>451.92 (+6.69%)</td><td>491.10 (+0.04%)</td><td>275.40 (+4.83%)</td><td>103.33 <b>(-23.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>539.60 (n/a)</td><td>423.60 (n/a)</td><td>490.90 (n/a)</td><td>262.70 (n/a)</td><td>135.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-6.06%)</td><td>0.01 (-18.60%)</td><td>0.01 <b>(-46.91%)</b></td><td>0.00 (-5.72%)</td><td>0.00 (-13.26%)</td><td>603.60 (+6.06%)</td><td>447.02 <b>(+20.71%)</b></td><td>522.60 <b>(+88.39%)</b></td><td>266.90 (+6.46%)</td><td>147.85 (-1.91%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>569.10 (n/a)</td><td>370.32 (n/a)</td><td>277.40 (n/a)</td><td>250.70 (n/a)</td><td>150.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-19.59%)</td><td>0.01 (-8.46%)</td><td>0.01 (+0.49%)</td><td>0.00 <b>(+28.26%)</b></td><td>0.00 <b>(-43.43%)</b></td><td>625.60 <b>(-22.03%)</b></td><td>511.28 (+1.40%)</td><td>501.10 (-0.50%)</td><td>363.40 <b>(+24.37%)</b></td><td>107.05 <b>(-44.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>802.40 (n/a)</td><td>504.20 (n/a)</td><td>503.60 (n/a)</td><td>292.20 (n/a)</td><td>192.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-18.50%)</td><td>0.01 (-15.44%)</td><td>0.02 (-6.78%)</td><td>0.01 <b>(-23.54%)</b></td><td>0.01 (-7.50%)</td><td>668.30 <b>(+30.78%)</b></td><td>415.70 <b>(+22.18%)</b></td><td>310.60 (+7.29%)</td><td>267.40 <b>(+22.72%)</b></td><td>177.57 <b>(+45.12%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>511.00 (n/a)</td><td>340.24 (n/a)</td><td>289.50 (n/a)</td><td>217.90 (n/a)</td><td>122.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+18.01%)</td><td>0.01 (-13.02%)</td><td>0.01 <b>(-31.88%)</b></td><td>0.01 (-17.05%)</td><td>0.01 <b>(+50.50%)</b></td><td>574.60 <b>(+20.56%)</b></td><td>438.46 <b>(+20.94%)</b></td><td>473.00 <b>(+46.80%)</b></td><td>229.10 (-15.27%)</td><td>129.16 <b>(+39.74%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.60 (n/a)</td><td>362.54 (n/a)</td><td>322.20 (n/a)</td><td>270.40 (n/a)</td><td>92.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+7.41%)</td><td>0.01 <b>(-20.83%)</b></td><td>0.01 <b>(-20.76%)</b></td><td>0.01 <b>(-41.88%)</b></td><td>0.01 <b>(+23.60%)</b></td><td>1049.40 <b>(+72.06%)</b></td><td>606.70 <b>(+41.47%)</b></td><td>563.10 <b>(+26.20%)</b></td><td>241.80 (-6.89%)</td><td>293.63 <b>(+92.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.90 (n/a)</td><td>428.86 (n/a)</td><td>446.20 (n/a)</td><td>259.70 (n/a)</td><td>152.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(+32.01%)</b></td><td>0.01 (+18.74%)</td><td>0.01 (+9.76%)</td><td>0.01 (+17.76%)</td><td>0.00 <b>(+59.66%)</b></td><td>512.60 (-15.09%)</td><td>406.06 (-14.79%)</td><td>423.00 (-8.90%)</td><td>297.10 <b>(-24.25%)</b></td><td>79.22 (-0.73%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.70 (n/a)</td><td>476.56 (n/a)</td><td>464.30 (n/a)</td><td>392.20 (n/a)</td><td>79.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-3.48%)</td><td>0.02 <b>(+69.29%)</b></td><td>0.02 <b>(+95.94%)</b></td><td>0.01 <b>(+557.47%)</b></td><td>0.00 <b>(-59.88%)</b></td><td>364.80 <b>(-84.79%)</b></td><td>315.88 <b>(-65.15%)</b></td><td>316.00 <b>(-48.96%)</b></td><td>238.40 (+3.61%)</td><td>51.19 <b>(-94.02%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2398.60 (n/a)</td><td>906.30 (n/a)</td><td>619.10 (n/a)</td><td>230.10 (n/a)</td><td>855.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(-20.22%)</b></td><td>0.01 (-14.36%)</td><td>0.01 <b>(-32.71%)</b></td><td>0.01 <b>(+226.71%)</b></td><td>0.00 <b>(-57.37%)</b></td><td>568.20 <b>(-69.39%)</b></td><td>469.16 <b>(-26.67%)</b></td><td>501.20 <b>(+48.59%)</b></td><td>321.30 <b>(+25.31%)</b></td><td>102.23 <b>(-85.06%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1856.30 (n/a)</td><td>639.78 (n/a)</td><td>337.30 (n/a)</td><td>256.40 (n/a)</td><td>684.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (-8.31%)</td><td>0.03 <b>(-22.64%)</b></td><td>0.02 <b>(-43.41%)</b></td><td>0.02 (-9.82%)</td><td>0.01 (+11.80%)</td><td>520.30 (+10.89%)</td><td>402.36 <b>(+32.91%)</b></td><td>474.50 <b>(+76.72%)</b></td><td>252.50 (+9.07%)</td><td>124.74 <b>(+29.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.20 (n/a)</td><td>302.74 (n/a)</td><td>268.50 (n/a)</td><td>231.50 (n/a)</td><td>96.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-53.59%)</b></td><td>0.02 <b>(-54.48%)</b></td><td>0.02 <b>(-57.61%)</b></td><td>0.02 <b>(-54.59%)</b></td><td>0.00 <b>(-50.97%)</b></td><td>659.50 <b>(+120.20%)</b></td><td>572.44 <b>(+120.59%)</b></td><td>630.90 <b>(+135.94%)</b></td><td>402.70 <b>(+115.46%)</b></td><td>105.51 <b>(+133.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>259.50 (n/a)</td><td>267.40 (n/a)</td><td>186.90 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (+12.01%)</td><td>0.02 (-6.29%)</td><td>0.03 (+17.73%)</td><td>0.01 <b>(-66.22%)</b></td><td>0.01 <b>(+92.06%)</b></td><td>1903.50 <b>(+195.99%)</b></td><td>696.14 <b>(+58.01%)</b></td><td>368.10 (-15.07%)</td><td>299.30 (-10.74%)</td><td>682.32 <b>(+449.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>643.10 (n/a)</td><td>440.56 (n/a)</td><td>433.40 (n/a)</td><td>335.30 (n/a)</td><td>124.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (-5.49%)</td><td>0.03 (-15.43%)</td><td>0.03 (-11.72%)</td><td>0.02 (-9.91%)</td><td>0.01 (+13.96%)</td><td>531.20 (+10.99%)</td><td>388.70 <b>(+22.17%)</b></td><td>329.90 (+13.29%)</td><td>257.90 (+5.78%)</td><td>131.84 <b>(+39.62%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>318.16 (n/a)</td><td>291.20 (n/a)</td><td>243.80 (n/a)</td><td>94.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-26.43%)</b></td><td>0.02 <b>(-20.92%)</b></td><td>0.02 (-6.24%)</td><td>0.02 <b>(+23.55%)</b></td><td>0.01 <b>(-56.93%)</b></td><td>522.40 (-19.06%)</td><td>450.34 (+12.54%)</td><td>462.00 (+6.65%)</td><td>310.10 <b>(+35.95%)</b></td><td>86.33 <b>(-49.66%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.40 (n/a)</td><td>400.16 (n/a)</td><td>433.20 (n/a)</td><td>228.10 (n/a)</td><td>171.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-30.93%)</b></td><td>0.02 <b>(-29.53%)</b></td><td>0.02 (-14.61%)</td><td>0.01 <b>(-33.29%)</b></td><td>0.01 <b>(-39.37%)</b></td><td>749.20 <b>(+49.90%)</b></td><td>542.86 <b>(+40.00%)</b></td><td>517.10 (+17.10%)</td><td>376.70 <b>(+44.77%)</b></td><td>147.05 <b>(+35.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.80 (n/a)</td><td>387.76 (n/a)</td><td>441.60 (n/a)</td><td>260.20 (n/a)</td><td>108.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 <b>(+38.67%)</b></td><td>0.06 <b>(+33.74%)</b></td><td>0.05 <b>(+26.92%)</b></td><td>0.04 <b>(+22.85%)</b></td><td>0.01 <b>(+50.76%)</b></td><td>486.80 (-18.60%)</td><td>385.38 <b>(-24.73%)</b></td><td>399.70 <b>(-21.21%)</b></td><td>282.50 <b>(-27.88%)</b></td><td>74.82 (-15.12%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>598.00 (n/a)</td><td>511.98 (n/a)</td><td>507.30 (n/a)</td><td>391.70 (n/a)</td><td>88.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (-8.57%)</td><td>0.05 <b>(-31.31%)</b></td><td>0.06 (-13.11%)</td><td>0.01 <b>(-79.63%)</b></td><td>0.03 <b>(+112.53%)</b></td><td>2078.70 <b>(+390.84%)</b></td><td>761.46 <b>(+151.01%)</b></td><td>330.70 (+15.11%)</td><td>272.60 (+9.39%)</td><td>771.29 <b>(+986.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>423.50 (n/a)</td><td>303.36 (n/a)</td><td>287.30 (n/a)</td><td>249.20 (n/a)</td><td>71.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 <b>(+47.31%)</b></td><td>0.07 <b>(+38.51%)</b></td><td>0.08 <b>(+60.57%)</b></td><td>0.05 <b>(+37.10%)</b></td><td>0.02 <b>(+38.47%)</b></td><td>462.40 <b>(-27.07%)</b></td><td>326.38 <b>(-27.77%)</b></td><td>275.00 <b>(-37.73%)</b></td><td>205.90 <b>(-32.11%)</b></td><td>108.08 <b>(-26.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.00 (n/a)</td><td>451.84 (n/a)</td><td>441.60 (n/a)</td><td>303.30 (n/a)</td><td>147.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 <b>(-46.15%)</b></td><td>0.04 (-19.85%)</td><td>0.05 (+5.29%)</td><td>0.02 <b>(-29.95%)</b></td><td>0.02 <b>(-50.99%)</b></td><td>987.00 <b>(+42.73%)</b></td><td>539.90 (+19.76%)</td><td>437.80 (-5.01%)</td><td>355.70 <b>(+85.74%)</b></td><td>260.20 <b>(+46.90%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>691.50 (n/a)</td><td>450.82 (n/a)</td><td>460.90 (n/a)</td><td>191.50 (n/a)</td><td>177.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (-17.39%)</td><td>0.06 (-1.08%)</td><td>0.06 <b>(+30.00%)</b></td><td>0.04 (-4.24%)</td><td>0.02 <b>(-25.00%)</b></td><td>553.60 (+4.43%)</td><td>383.22 (-1.91%)</td><td>342.20 <b>(-23.07%)</b></td><td>252.50 <b>(+21.05%)</b></td><td>128.23 (-3.15%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>530.10 (n/a)</td><td>390.68 (n/a)</td><td>444.80 (n/a)</td><td>208.60 (n/a)</td><td>132.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-10.39%)</td><td>0.04 (-18.50%)</td><td>0.04 <b>(-35.84%)</b></td><td>0.03 (-1.20%)</td><td>0.01 (-13.21%)</td><td>608.20 (+1.21%)</td><td>522.92 <b>(+21.71%)</b></td><td>592.50 <b>(+55.84%)</b></td><td>341.30 (+11.61%)</td><td>117.21 (-1.80%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.90 (n/a)</td><td>429.64 (n/a)</td><td>380.20 (n/a)</td><td>305.80 (n/a)</td><td>119.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>514.80 (n/a)</td><td>365.46 (n/a)</td><td>335.80 (n/a)</td><td>242.00 (n/a)</td><td>111.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.80 (n/a)</td><td>458.64 (n/a)</td><td>438.40 (n/a)</td><td>299.80 (n/a)</td><td>115.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.40 (n/a)</td><td>446.32 (n/a)</td><td>471.60 (n/a)</td><td>337.90 (n/a)</td><td>87.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.40 (n/a)</td><td>427.46 (n/a)</td><td>470.80 (n/a)</td><td>306.50 (n/a)</td><td>107.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1870.30 (n/a)</td><td>733.84 (n/a)</td><td>447.30 (n/a)</td><td>271.70 (n/a)</td><td>650.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>764.80 (n/a)</td><td>529.20 (n/a)</td><td>625.70 (n/a)</td><td>242.40 (n/a)</td><td>241.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.90 (n/a)</td><td>462.38 (n/a)</td><td>489.10 (n/a)</td><td>274.60 (n/a)</td><td>115.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>501.80 (n/a)</td><td>348.94 (n/a)</td><td>303.00 (n/a)</td><td>229.10 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>625.80 (n/a)</td><td>387.28 (n/a)</td><td>347.10 (n/a)</td><td>240.80 (n/a)</td><td>160.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 <b>(+55.81%)</b></td><td>0.16 <b>(+69.11%)</b></td><td>0.18 <b>(+78.11%)</b></td><td>0.08 <b>(+198.68%)</b></td><td>0.06 <b>(+40.12%)</b></td><td>635.20 <b>(-66.52%)</b></td><td>363.66 <b>(-51.45%)</b></td><td>279.10 <b>(-43.85%)</b></td><td>231.40 <b>(-35.81%)</b></td><td>168.64 <b>(-73.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1897.20 (n/a)</td><td>749.06 (n/a)</td><td>497.10 (n/a)</td><td>360.50 (n/a)</td><td>644.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>490.40 (n/a)</td><td>362.42 (n/a)</td><td>368.30 (n/a)</td><td>231.30 (n/a)</td><td>120.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>551.60 (n/a)</td><td>423.00 (n/a)</td><td>447.90 (n/a)</td><td>277.00 (n/a)</td><td>131.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.30 (n/a)</td><td>394.14 (n/a)</td><td>448.40 (n/a)</td><td>158.10 (n/a)</td><td>164.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.30 (n/a)</td><td>486.68 (n/a)</td><td>535.80 (n/a)</td><td>355.50 (n/a)</td><td>114.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.00 (n/a)</td><td>359.86 (n/a)</td><td>295.00 (n/a)</td><td>186.60 (n/a)</td><td>161.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>607.80 (n/a)</td><td>362.58 (n/a)</td><td>324.20 (n/a)</td><td>229.20 (n/a)</td><td>146.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>572.30 (n/a)</td><td>402.70 (n/a)</td><td>407.70 (n/a)</td><td>213.60 (n/a)</td><td>159.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>433.64 (n/a)</td><td>399.30 (n/a)</td><td>310.40 (n/a)</td><td>128.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.40 (n/a)</td><td>373.74 (n/a)</td><td>317.10 (n/a)</td><td>298.70 (n/a)</td><td>96.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>564.80 (n/a)</td><td>490.38 (n/a)</td><td>497.10 (n/a)</td><td>401.20 (n/a)</td><td>66.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>611.20 (n/a)</td><td>494.12 (n/a)</td><td>555.60 (n/a)</td><td>280.60 (n/a)</td><td>134.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>565.30 (n/a)</td><td>432.96 (n/a)</td><td>482.90 (n/a)</td><td>199.60 (n/a)</td><td>155.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>624.30 (n/a)</td><td>455.06 (n/a)</td><td>444.90 (n/a)</td><td>319.90 (n/a)</td><td>118.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2092.10 (n/a)</td><td>702.30 (n/a)</td><td>463.90 (n/a)</td><td>220.00 (n/a)</td><td>786.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.20 (n/a)</td><td>302.80 (n/a)</td><td>248.90 (n/a)</td><td>235.50 (n/a)</td><td>109.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>765.90 (n/a)</td><td>508.86 (n/a)</td><td>531.90 (n/a)</td><td>240.70 (n/a)</td><td>188.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.00 (n/a)</td><td>459.32 (n/a)</td><td>488.20 (n/a)</td><td>304.10 (n/a)</td><td>131.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.00 (n/a)</td><td>355.82 (n/a)</td><td>315.50 (n/a)</td><td>228.60 (n/a)</td><td>135.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.50 (n/a)</td><td>441.42 (n/a)</td><td>447.60 (n/a)</td><td>219.30 (n/a)</td><td>158.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.70 (n/a)</td><td>379.54 (n/a)</td><td>299.40 (n/a)</td><td>243.10 (n/a)</td><td>161.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.60 (n/a)</td><td>393.24 (n/a)</td><td>378.50 (n/a)</td><td>217.70 (n/a)</td><td>171.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.80 (n/a)</td><td>466.46 (n/a)</td><td>474.70 (n/a)</td><td>318.60 (n/a)</td><td>97.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1616.60 (n/a)</td><td>703.10 (n/a)</td><td>316.40 (n/a)</td><td>249.10 (n/a)</td><td>616.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.10 (n/a)</td><td>378.52 (n/a)</td><td>426.40 (n/a)</td><td>223.70 (n/a)</td><td>143.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>983.20 (n/a)</td><td>529.96 (n/a)</td><td>452.20 (n/a)</td><td>291.90 (n/a)</td><td>283.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.30 (n/a)</td><td>343.64 (n/a)</td><td>288.30 (n/a)</td><td>280.80 (n/a)</td><td>119.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>639.80 (n/a)</td><td>425.46 (n/a)</td><td>500.60 (n/a)</td><td>195.50 (n/a)</td><td>203.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>590.70 (n/a)</td><td>431.72 (n/a)</td><td>409.40 (n/a)</td><td>286.70 (n/a)</td><td>130.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>656.10 (n/a)</td><td>488.34 (n/a)</td><td>482.40 (n/a)</td><td>270.90 (n/a)</td><td>145.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>582.00 (n/a)</td><td>367.54 (n/a)</td><td>294.80 (n/a)</td><td>232.30 (n/a)</td><td>145.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>584.40 (n/a)</td><td>469.36 (n/a)</td><td>475.70 (n/a)</td><td>332.80 (n/a)</td><td>89.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>590.90 (n/a)</td><td>416.22 (n/a)</td><td>352.30 (n/a)</td><td>322.10 (n/a)</td><td>119.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>581.20 (n/a)</td><td>437.90 (n/a)</td><td>454.50 (n/a)</td><td>307.50 (n/a)</td><td>124.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>558.80 (n/a)</td><td>390.00 (n/a)</td><td>326.70 (n/a)</td><td>301.20 (n/a)</td><td>112.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>704.00 (n/a)</td><td>486.14 (n/a)</td><td>572.20 (n/a)</td><td>273.10 (n/a)</td><td>196.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1968.30 (n/a)</td><td>752.76 (n/a)</td><td>426.00 (n/a)</td><td>233.60 (n/a)</td><td>718.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>563.40 (n/a)</td><td>405.00 (n/a)</td><td>323.00 (n/a)</td><td>299.00 (n/a)</td><td>131.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.50 (+1.52%)</td><td>0.33 <b>(-24.10%)</b></td><td>0.28 <b>(-36.68%)</b></td><td>0.18 <b>(-50.26%)</b></td><td>0.14 <b>(+143.13%)</b></td><td>1208.30 <b>(+101.05%)</b></td><td>768.08 <b>(+49.96%)</b></td><td>778.60 <b>(+57.93%)</b></td><td>439.70 (-1.50%)</td><td>318.12 <b>(+362.01%)</b></td><td>21.46 (+1.52%)</td><td>14.18 <b>(-24.10%)</b></td><td>12.12 <b>(-36.68%)</b></td><td>7.81 <b>(-50.26%)</b></td><td>5.92 <b>(+143.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.37 (n/a)</td><td>0.06 (n/a)</td><td>601.00 (n/a)</td><td>512.18 (n/a)</td><td>493.00 (n/a)</td><td>446.40 (n/a)</td><td>68.86 (n/a)</td><td>21.14 (n/a)</td><td>18.69 (n/a)</td><td>19.14 (n/a)</td><td>15.70 (n/a)</td><td>2.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.58 <b>(+21.71%)</b></td><td>0.39 (+12.95%)</td><td>0.50 <b>(+31.94%)</b></td><td>0.17 (-8.99%)</td><td>0.20 <b>(+73.91%)</b></td><td>1289.10 (+9.88%)</td><td>733.60 (+4.27%)</td><td>444.00 <b>(-24.21%)</b></td><td>382.70 (-17.82%)</td><td>441.38 <b>(+54.91%)</b></td><td>24.66 <b>(+21.71%)</b></td><td>16.85 (+12.95%)</td><td>21.25 <b>(+31.94%)</b></td><td>7.32 (-8.99%)</td><td>8.35 <b>(+73.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>1173.20 (n/a)</td><td>703.58 (n/a)</td><td>585.80 (n/a)</td><td>465.70 (n/a)</td><td>284.93 (n/a)</td><td>20.26 (n/a)</td><td>14.92 (n/a)</td><td>16.11 (n/a)</td><td>8.04 (n/a)</td><td>4.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.31 (+0.45%)</td><td>0.31 (+0.86%)</td><td>0.31 (+0.88%)</td><td>0.30 (+2.63%)</td><td>0.01 <b>(-34.22%)</b></td><td>84145.90 (-2.57%)</td><td>82343.98 (-0.88%)</td><td>82382.30 (-0.87%)</td><td>80393.20 (-0.44%)</td><td>1410.87 <b>(-36.19%)</b></td><td>213.70 (+0.45%)</td><td>208.68 (+0.86%)</td><td>208.54 (+0.88%)</td><td>204.17 (+2.63%)</td><td>3.58 <b>(-34.22%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86361.50 (n/a)</td><td>83076.40 (n/a)</td><td>83106.40 (n/a)</td><td>80752.00 (n/a)</td><td>2211.14 (n/a)</td><td>212.75 (n/a)</td><td>206.91 (n/a)</td><td>206.72 (n/a)</td><td>198.93 (n/a)</td><td>5.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.03 (-0.89%)</td><td>1.00 (-1.93%)</td><td>1.01 (-0.92%)</td><td>0.94 (-4.97%)</td><td>0.03 <b>(+84.64%)</b></td><td>26689.30 (+5.23%)</td><td>25194.92 (+2.03%)</td><td>24858.10 (+0.93%)</td><td>24451.10 (+0.90%)</td><td>869.94 <b>(+97.32%)</b></td><td>702.62 (-0.89%)</td><td>682.51 (-1.93%)</td><td>691.12 (-0.92%)</td><td>643.70 (-4.97%)</td><td>22.73 <b>(+84.64%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25363.30 (n/a)</td><td>24692.70 (n/a)</td><td>24629.60 (n/a)</td><td>24233.20 (n/a)</td><td>440.87 (n/a)</td><td>708.94 (n/a)</td><td>695.92 (n/a)</td><td>697.53 (n/a)</td><td>677.35 (n/a)</td><td>12.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.83 (+0.47%)</td><td>0.82 (+1.20%)</td><td>0.82 (+1.75%)</td><td>0.81 (+1.39%)</td><td>0.01 <b>(-26.21%)</b></td><td>93714.80 (-1.37%)</td><td>92378.56 (-1.20%)</td><td>92231.40 (-1.72%)</td><td>91187.40 (-0.47%)</td><td>970.18 <b>(-27.47%)</b></td><td>753.61 (+0.47%)</td><td>743.96 (+1.20%)</td><td>745.08 (+1.75%)</td><td>733.28 (+1.39%)</td><td>7.80 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95020.30 (n/a)</td><td>93495.86 (n/a)</td><td>93848.20 (n/a)</td><td>91613.80 (n/a)</td><td>1337.69 (n/a)</td><td>750.10 (n/a)</td><td>735.12 (n/a)</td><td>732.24 (n/a)</td><td>723.21 (n/a)</td><td>10.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (+0.21%)</td><td>0.77 (+0.46%)</td><td>0.77 (+0.33%)</td><td>0.75 (+2.26%)</td><td>0.01 <b>(-30.61%)</b></td><td>100335.50 (-2.21%)</td><td>98338.06 (-0.48%)</td><td>97770.90 (-0.33%)</td><td>97061.50 (-0.21%)</td><td>1452.14 <b>(-32.63%)</b></td><td>708.00 (+0.21%)</td><td>698.93 (+0.46%)</td><td>702.86 (+0.33%)</td><td>684.90 (+2.26%)</td><td>10.26 <b>(-30.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102601.50 (n/a)</td><td>98812.52 (n/a)</td><td>98091.30 (n/a)</td><td>97269.50 (n/a)</td><td>2155.58 (n/a)</td><td>706.49 (n/a)</td><td>695.71 (n/a)</td><td>700.57 (n/a)</td><td>669.77 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.80 (-0.17%)</td><td>0.80 (-0.03%)</td><td>0.80 (-0.24%)</td><td>0.79 (+0.03%)</td><td>0.00 (-17.12%)</td><td>95282.50 (-0.03%)</td><td>94602.60 (+0.03%)</td><td>94773.80 (+0.24%)</td><td>93907.00 (+0.17%)</td><td>528.35 (-17.07%)</td><td>731.78 (-0.17%)</td><td>726.42 (-0.03%)</td><td>725.09 (-0.24%)</td><td>721.22 (+0.03%)</td><td>4.06 (-17.13%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95311.70 (n/a)</td><td>94578.72 (n/a)</td><td>94545.30 (n/a)</td><td>93748.50 (n/a)</td><td>637.08 (n/a)</td><td>733.02 (n/a)</td><td>726.61 (n/a)</td><td>726.84 (n/a)</td><td>721.00 (n/a)</td><td>4.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.53 (+3.85%)</td><td>3.46 (-5.56%)</td><td>3.03 <b>(-25.35%)</b></td><td>2.43 (+11.45%)</td><td>1.23 (-9.89%)</td><td>3670.80 (-10.27%)</td><td>2795.38 (+1.28%)</td><td>2938.70 <b>(+33.97%)</b></td><td>1612.80 (-3.71%)</td><td>793.26 <b>(-28.88%)</b></td><td>332.88 (+3.85%)</td><td>208.46 (-5.56%)</td><td>182.69 <b>(-25.35%)</b></td><td>146.25 (+11.45%)</td><td>74.28 (-9.89%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.32 (n/a)</td><td>3.66 (n/a)</td><td>4.06 (n/a)</td><td>2.18 (n/a)</td><td>1.37 (n/a)</td><td>4091.00 (n/a)</td><td>2760.08 (n/a)</td><td>2193.60 (n/a)</td><td>1674.90 (n/a)</td><td>1115.41 (n/a)</td><td>320.54 (n/a)</td><td>220.74 (n/a)</td><td>244.74 (n/a)</td><td>131.23 (n/a)</td><td>82.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.09 (+4.08%)</td><td>3.38 (+2.70%)</td><td>2.82 <b>(+22.95%)</b></td><td>2.23 (+0.19%)</td><td>1.33 (-4.75%)</td><td>4000.00 (-0.19%)</td><td>2971.96 (-4.10%)</td><td>3155.40 (-18.66%)</td><td>1749.60 (-3.92%)</td><td>1068.69 (-6.44%)</td><td>306.85 (+4.08%)</td><td>203.45 (+2.70%)</td><td>170.15 <b>(+22.95%)</b></td><td>134.22 (+0.19%)</td><td>80.34 (-4.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>4.89 (n/a)</td><td>3.29 (n/a)</td><td>2.30 (n/a)</td><td>2.22 (n/a)</td><td>1.40 (n/a)</td><td>4007.70 (n/a)</td><td>3099.04 (n/a)</td><td>3879.50 (n/a)</td><td>1821.00 (n/a)</td><td>1142.23 (n/a)</td><td>294.81 (n/a)</td><td>198.10 (n/a)</td><td>138.39 (n/a)</td><td>133.96 (n/a)</td><td>84.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.02 (+9.62%)</td><td>3.20 (-15.72%)</td><td>2.46 <b>(-30.24%)</b></td><td>2.15 (+4.34%)</td><td>1.63 (+12.38%)</td><td>4146.90 (-4.16%)</td><td>3235.64 <b>(+20.82%)</b></td><td>3621.40 <b>(+43.36%)</b></td><td>1481.10 (-8.77%)</td><td>1127.64 (+1.77%)</td><td>362.49 (+9.62%)</td><td>192.51 (-15.72%)</td><td>148.25 <b>(-30.24%)</b></td><td>129.46 (+4.34%)</td><td>98.48 (+12.38%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.49 (n/a)</td><td>3.79 (n/a)</td><td>3.53 (n/a)</td><td>2.06 (n/a)</td><td>1.45 (n/a)</td><td>4326.70 (n/a)</td><td>2678.10 (n/a)</td><td>2526.10 (n/a)</td><td>1623.50 (n/a)</td><td>1108.02 (n/a)</td><td>330.69 (n/a)</td><td>228.41 (n/a)</td><td>212.53 (n/a)</td><td>124.08 (n/a)</td><td>87.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.40 (-1.58%)</td><td>5.62 (+8.20%)</td><td>5.74 (+18.43%)</td><td>4.98 (+10.04%)</td><td>0.63 (-19.06%)</td><td>7004.40 (-9.12%)</td><td>6265.72 (-8.11%)</td><td>6074.50 (-15.56%)</td><td>5447.90 (+1.61%)</td><td>705.20 <b>(-21.74%)</b></td><td>394.18 (-1.58%)</td><td>346.22 (+8.20%)</td><td>353.52 (+18.43%)</td><td>306.59 (+10.04%)</td><td>38.75 (-19.06%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.50 (n/a)</td><td>5.19 (n/a)</td><td>4.85 (n/a)</td><td>4.52 (n/a)</td><td>0.78 (n/a)</td><td>7707.70 (n/a)</td><td>6818.98 (n/a)</td><td>7194.00 (n/a)</td><td>5361.70 (n/a)</td><td>901.08 (n/a)</td><td>400.52 (n/a)</td><td>319.97 (n/a)</td><td>298.51 (n/a)</td><td>278.61 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.65 (-14.22%)</td><td>4.34 (-7.53%)</td><td>4.30 (-8.95%)</td><td>3.87 (+3.24%)</td><td>0.31 <b>(-51.31%)</b></td><td>9001.40 (-3.13%)</td><td>8075.18 (+6.91%)</td><td>8107.50 (+9.83%)</td><td>7502.50 (+16.57%)</td><td>596.70 <b>(-45.71%)</b></td><td>286.24 (-14.22%)</td><td>267.06 (-7.53%)</td><td>264.87 (-8.95%)</td><td>238.57 (+3.24%)</td><td>19.01 <b>(-51.31%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.42 (n/a)</td><td>4.69 (n/a)</td><td>4.72 (n/a)</td><td>3.75 (n/a)</td><td>0.63 (n/a)</td><td>9292.60 (n/a)</td><td>7553.58 (n/a)</td><td>7382.10 (n/a)</td><td>6435.80 (n/a)</td><td>1099.09 (n/a)</td><td>333.68 (n/a)</td><td>288.81 (n/a)</td><td>290.90 (n/a)</td><td>231.10 (n/a)</td><td>39.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.59 (-16.84%)</td><td>5.19 (-8.24%)</td><td>5.00 (-12.51%)</td><td>4.94 (+13.61%)</td><td>0.30 <b>(-65.40%)</b></td><td>7055.80 (-11.98%)</td><td>6737.64 (+7.05%)</td><td>6971.80 (+14.30%)</td><td>6241.20 <b>(+20.25%)</b></td><td>378.09 <b>(-64.15%)</b></td><td>344.08 (-16.84%)</td><td>319.55 (-8.24%)</td><td>308.02 (-12.51%)</td><td>304.36 (+13.61%)</td><td>18.38 <b>(-65.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.72 (n/a)</td><td>5.65 (n/a)</td><td>5.72 (n/a)</td><td>4.35 (n/a)</td><td>0.86 (n/a)</td><td>8016.40 (n/a)</td><td>6293.86 (n/a)</td><td>6099.50 (n/a)</td><td>5190.40 (n/a)</td><td>1054.64 (n/a)</td><td>413.74 (n/a)</td><td>348.25 (n/a)</td><td>352.07 (n/a)</td><td>267.89 (n/a)</td><td>53.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (+1.18%)</td><td>0.76 (-0.83%)</td><td>0.76 (-0.73%)</td><td>0.74 (-3.11%)</td><td>0.02 <b>(+317.84%)</b></td><td>101569.90 (+3.21%)</td><td>98776.52 (+0.87%)</td><td>98723.20 (+0.74%)</td><td>96221.40 (-1.16%)</td><td>1983.76 <b>(+326.39%)</b></td><td>714.18 (+1.18%)</td><td>695.93 (-0.83%)</td><td>696.08 (-0.73%)</td><td>676.57 (-3.11%)</td><td>13.94 <b>(+317.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98410.20 (n/a)</td><td>97928.78 (n/a)</td><td>98001.90 (n/a)</td><td>97354.80 (n/a)</td><td>465.25 (n/a)</td><td>705.87 (n/a)</td><td>701.74 (n/a)</td><td>701.21 (n/a)</td><td>698.30 (n/a)</td><td>3.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (+0.33%)</td><td>0.77 (+0.67%)</td><td>0.77 (+1.66%)</td><td>0.74 (-0.90%)</td><td>0.02 <b>(+35.54%)</b></td><td>101806.00 (+0.91%)</td><td>98683.04 (-0.65%)</td><td>98295.60 (-1.63%)</td><td>96807.00 (-0.33%)</td><td>2119.09 <b>(+36.03%)</b></td><td>709.86 (+0.33%)</td><td>696.62 (+0.67%)</td><td>699.11 (+1.66%)</td><td>675.00 (-0.90%)</td><td>14.81 <b>(+35.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100884.70 (n/a)</td><td>99326.82 (n/a)</td><td>99926.70 (n/a)</td><td>97131.20 (n/a)</td><td>1557.76 (n/a)</td><td>707.49 (n/a)</td><td>691.99 (n/a)</td><td>687.70 (n/a)</td><td>681.17 (n/a)</td><td>10.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.81 (-0.43%)</td><td>0.80 (+0.14%)</td><td>0.81 (-0.02%)</td><td>0.79 (+0.98%)</td><td>0.01 <b>(-27.71%)</b></td><td>95338.40 (-0.97%)</td><td>94169.96 (-0.15%)</td><td>93778.60 (+0.02%)</td><td>93271.20 (+0.43%)</td><td>1016.29 <b>(-28.13%)</b></td><td>736.77 (-0.43%)</td><td>729.81 (+0.14%)</td><td>732.78 (-0.02%)</td><td>720.80 (+0.98%)</td><td>7.85 <b>(-27.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96276.60 (n/a)</td><td>94308.80 (n/a)</td><td>93760.40 (n/a)</td><td>92872.70 (n/a)</td><td>1414.04 (n/a)</td><td>739.93 (n/a)</td><td>728.79 (n/a)</td><td>732.93 (n/a)</td><td>713.77 (n/a)</td><td>10.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.46 (-10.97%)</td><td>2.65 (-2.25%)</td><td>2.89 (+5.94%)</td><td>1.66 <b>(+22.16%)</b></td><td>0.75 <b>(-24.81%)</b></td><td>4868.10 (-18.14%)</td><td>3276.08 (-3.82%)</td><td>2793.90 (-5.61%)</td><td>2326.50 (+12.32%)</td><td>1059.50 <b>(-31.59%)</b></td><td>908.62 (-10.97%)</td><td>695.38 (-2.25%)</td><td>756.62 (+5.94%)</td><td>434.24 <b>(+22.16%)</b></td><td>196.89 <b>(-24.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.89 (n/a)</td><td>2.71 (n/a)</td><td>2.72 (n/a)</td><td>1.36 (n/a)</td><td>1.00 (n/a)</td><td>5946.90 (n/a)</td><td>3406.18 (n/a)</td><td>2959.90 (n/a)</td><td>2071.30 (n/a)</td><td>1548.68 (n/a)</td><td>1020.56 (n/a)</td><td>711.35 (n/a)</td><td>714.18 (n/a)</td><td>355.47 (n/a)</td><td>261.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.30 (+1.49%)</td><td>0.24 (+17.09%)</td><td>0.27 <b>(+27.33%)</b></td><td>0.18 <b>(+22.81%)</b></td><td>0.06 (-1.40%)</td><td>7050.90 (-18.58%)</td><td>5440.76 (-15.65%)</td><td>4578.80 <b>(-21.47%)</b></td><td>4119.00 (-1.47%)</td><td>1471.28 (-19.37%)</td><td>16.29 (+1.49%)</td><td>13.04 (+17.09%)</td><td>14.66 <b>(+27.33%)</b></td><td>9.52 <b>(+22.81%)</b></td><td>3.26 (-1.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>8659.40 (n/a)</td><td>6449.86 (n/a)</td><td>5830.30 (n/a)</td><td>4180.40 (n/a)</td><td>1824.69 (n/a)</td><td>16.05 (n/a)</td><td>11.13 (n/a)</td><td>11.51 (n/a)</td><td>7.75 (n/a)</td><td>3.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.87 (n/a)</td><td>3.69 (n/a)</td><td>3.83 (n/a)</td><td>3.34 (n/a)</td><td>0.23 (n/a)</td><td>3.86 (n/a)</td><td>3.69 (n/a)</td><td>3.83 (n/a)</td><td>3.34 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.36 (+7.99%)</td><td>6.88 (+12.81%)</td><td>6.99 (+19.38%)</td><td>6.08 (+6.52%)</td><td>0.48 (+3.93%)</td><td>7.36 (+7.99%)</td><td>6.88 (+12.81%)</td><td>6.98 (+19.38%)</td><td>6.07 (+6.52%)</td><td>0.48 (+3.93%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.82 (n/a)</td><td>6.10 (n/a)</td><td>5.85 (n/a)</td><td>5.71 (n/a)</td><td>0.46 (n/a)</td><td>6.81 (n/a)</td><td>6.10 (n/a)</td><td>5.85 (n/a)</td><td>5.70 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.38 <b>(-22.28%)</b></td><td>8.51 (-9.80%)</td><td>8.33 (-1.80%)</td><td>8.20 (-0.66%)</td><td>0.49 <b>(-69.60%)</b></td><td>9.38 <b>(-22.28%)</b></td><td>8.51 (-9.80%)</td><td>8.32 (-1.80%)</td><td>8.20 (-0.66%)</td><td>0.49 <b>(-69.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>12.08 (n/a)</td><td>9.44 (n/a)</td><td>8.48 (n/a)</td><td>8.26 (n/a)</td><td>1.62 (n/a)</td><td>12.07 (n/a)</td><td>9.43 (n/a)</td><td>8.47 (n/a)</td><td>8.25 (n/a)</td><td>1.61 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.84 (n/a)</td><td>3.60 (n/a)</td><td>3.66 (n/a)</td><td>3.37 (n/a)</td><td>0.21 (n/a)</td><td>3.84 (n/a)</td><td>3.59 (n/a)</td><td>3.66 (n/a)</td><td>3.36 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.08 (+3.62%)</td><td>6.25 (+11.95%)</td><td>6.57 (+16.25%)</td><td>4.59 (+6.29%)</td><td>0.97 (+6.05%)</td><td>7.08 (+3.62%)</td><td>6.25 (+11.95%)</td><td>6.57 (+16.25%)</td><td>4.59 (+6.29%)</td><td>0.97 (+6.05%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.84 (n/a)</td><td>5.58 (n/a)</td><td>5.65 (n/a)</td><td>4.32 (n/a)</td><td>0.91 (n/a)</td><td>6.83 (n/a)</td><td>5.58 (n/a)</td><td>5.65 (n/a)</td><td>4.32 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>13.01 (-3.42%)</td><td>9.47 (+2.21%)</td><td>8.43 (+0.14%)</td><td>7.66 (-1.15%)</td><td>2.18 (-7.75%)</td><td>13.00 (-3.42%)</td><td>9.47 (+2.21%)</td><td>8.43 (+0.14%)</td><td>7.65 (-1.15%)</td><td>2.18 (-7.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>13.47 (n/a)</td><td>9.27 (n/a)</td><td>8.42 (n/a)</td><td>7.75 (n/a)</td><td>2.36 (n/a)</td><td>13.46 (n/a)</td><td>9.26 (n/a)</td><td>8.42 (n/a)</td><td>7.74 (n/a)</td><td>2.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.23 (+1.27%)</td><td>2.02 (-18.46%)</td><td>1.75 <b>(-35.78%)</b></td><td>1.05 (+12.30%)</td><td>0.85 (-3.99%)</td><td>3.22 (+1.27%)</td><td>2.01 (-18.46%)</td><td>1.74 <b>(-35.78%)</b></td><td>1.05 (+12.30%)</td><td>0.85 (-3.99%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.19 (n/a)</td><td>2.47 (n/a)</td><td>2.72 (n/a)</td><td>0.94 (n/a)</td><td>0.89 (n/a)</td><td>3.18 (n/a)</td><td>2.47 (n/a)</td><td>2.71 (n/a)</td><td>0.93 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.58 (+1.21%)</td><td>0.39 (-14.76%)</td><td>0.38 (-9.95%)</td><td>0.08 <b>(-79.41%)</b></td><td>0.20 <b>(+144.67%)</b></td><td>0.57 (+1.21%)</td><td>0.38 (-14.76%)</td><td>0.38 (-9.95%)</td><td>0.08 <b>(-79.41%)</b></td><td>0.19 <b>(+144.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.67 (+7.27%)</td><td>0.56 <b>(+88.85%)</b></td><td>0.64 <b>(+83.95%)</b></td><td>0.37 <b>(+360.54%)</b></td><td>0.14 <b>(-39.92%)</b></td><td>0.66 (+7.27%)</td><td>0.55 <b>(+88.85%)</b></td><td>0.63 <b>(+83.95%)</b></td><td>0.37 <b>(+360.54%)</b></td><td>0.13 <b>(-39.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.62 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.23 (n/a)</td><td>0.62 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.76 <b>(+45.14%)</b></td><td>1.06 <b>(-20.29%)</b></td><td>0.46 <b>(-73.13%)</b></td><td>0.43 (-3.96%)</td><td>1.01 <b>(+53.93%)</b></td><td>2.72 <b>(+45.14%)</b></td><td>1.04 <b>(-20.29%)</b></td><td>0.45 <b>(-73.13%)</b></td><td>0.43 (-3.96%)</td><td>0.99 <b>(+53.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.90 (n/a)</td><td>1.33 (n/a)</td><td>1.71 (n/a)</td><td>0.45 (n/a)</td><td>0.65 (n/a)</td><td>1.87 (n/a)</td><td>1.31 (n/a)</td><td>1.69 (n/a)</td><td>0.44 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>427.60 (n/a)</td><td>311.74 (n/a)</td><td>300.60 (n/a)</td><td>215.70 (n/a)</td><td>78.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>606.10 (n/a)</td><td>360.14 (n/a)</td><td>281.40 (n/a)</td><td>193.80 (n/a)</td><td>177.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>493.60 (n/a)</td><td>334.70 (n/a)</td><td>284.50 (n/a)</td><td>153.20 (n/a)</td><td>144.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.80 (n/a)</td><td>509.40 (n/a)</td><td>557.30 (n/a)</td><td>420.70 (n/a)</td><td>80.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1050.10 (n/a)</td><td>581.18 (n/a)</td><td>489.00 (n/a)</td><td>423.90 (n/a)</td><td>264.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>660.20 (n/a)</td><td>509.44 (n/a)</td><td>567.40 (n/a)</td><td>338.00 (n/a)</td><td>143.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.30 (n/a)</td><td>409.08 (n/a)</td><td>415.10 (n/a)</td><td>267.90 (n/a)</td><td>137.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.20 (n/a)</td><td>322.18 (n/a)</td><td>281.90 (n/a)</td><td>152.60 (n/a)</td><td>139.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.00 (n/a)</td><td>425.38 (n/a)</td><td>467.40 (n/a)</td><td>241.20 (n/a)</td><td>118.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.10 (n/a)</td><td>486.48 (n/a)</td><td>462.70 (n/a)</td><td>442.10 (n/a)</td><td>51.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>406.50 (n/a)</td><td>350.00 (n/a)</td><td>238.80 (n/a)</td><td>180.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2026.50 (n/a)</td><td>766.06 (n/a)</td><td>518.00 (n/a)</td><td>202.30 (n/a)</td><td>719.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.40 (n/a)</td><td>399.80 (n/a)</td><td>423.30 (n/a)</td><td>305.50 (n/a)</td><td>87.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>575.40 (n/a)</td><td>443.30 (n/a)</td><td>426.50 (n/a)</td><td>290.20 (n/a)</td><td>115.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2445.30 (n/a)</td><td>868.92 (n/a)</td><td>538.50 (n/a)</td><td>321.90 (n/a)</td><td>885.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.50 (n/a)</td><td>441.26 (n/a)</td><td>460.50 (n/a)</td><td>208.10 (n/a)</td><td>146.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>709.60 (n/a)</td><td>513.52 (n/a)</td><td>518.30 (n/a)</td><td>237.00 (n/a)</td><td>178.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>639.90 (n/a)</td><td>501.72 (n/a)</td><td>542.10 (n/a)</td><td>298.40 (n/a)</td><td>128.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>567.20 (n/a)</td><td>487.20 (n/a)</td><td>535.60 (n/a)</td><td>295.20 (n/a)</td><td>109.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1859.90 (n/a)</td><td>588.30 (n/a)</td><td>306.70 (n/a)</td><td>173.00 (n/a)</td><td>713.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>570.90 (n/a)</td><td>341.60 (n/a)</td><td>307.70 (n/a)</td><td>222.40 (n/a)</td><td>133.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.60 (n/a)</td><td>415.88 (n/a)</td><td>460.70 (n/a)</td><td>243.70 (n/a)</td><td>137.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1061.00 (n/a)</td><td>562.68 (n/a)</td><td>448.80 (n/a)</td><td>291.80 (n/a)</td><td>295.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>681.10 (n/a)</td><td>516.08 (n/a)</td><td>463.20 (n/a)</td><td>389.30 (n/a)</td><td>130.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-13.94%)</td><td>0.01 (-14.78%)</td><td>0.01 (-12.43%)</td><td>0.01 <b>(-22.10%)</b></td><td>0.00 (+4.96%)</td><td>539.60 <b>(+28.35%)</b></td><td>367.20 <b>(+23.81%)</b></td><td>282.30 (+14.20%)</td><td>231.80 (+16.19%)</td><td>157.15 <b>(+58.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>420.40 (n/a)</td><td>296.58 (n/a)</td><td>247.20 (n/a)</td><td>199.50 (n/a)</td><td>98.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+2.38%)</td><td>0.01 (-1.82%)</td><td>0.02 <b>(+47.41%)</b></td><td>0.01 <b>(-29.39%)</b></td><td>0.01 <b>(+21.01%)</b></td><td>732.00 <b>(+41.61%)</b></td><td>404.62 (+12.71%)</td><td>272.10 <b>(-32.16%)</b></td><td>226.90 (-2.28%)</td><td>217.05 <b>(+79.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.90 (n/a)</td><td>358.98 (n/a)</td><td>401.10 (n/a)</td><td>232.20 (n/a)</td><td>120.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-9.22%)</td><td>0.01 <b>(-30.86%)</b></td><td>0.01 <b>(-35.62%)</b></td><td>0.00 <b>(-81.52%)</b></td><td>0.01 <b>(+54.35%)</b></td><td>2457.40 <b>(+441.04%)</b></td><td>756.96 <b>(+163.91%)</b></td><td>382.60 <b>(+55.34%)</b></td><td>259.40 (+10.15%)</td><td>952.23 <b>(+912.62%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>454.20 (n/a)</td><td>286.82 (n/a)</td><td>246.30 (n/a)</td><td>235.50 (n/a)</td><td>94.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+0.44%)</td><td>0.01 (-4.37%)</td><td>0.01 (-18.01%)</td><td>0.01 (-13.15%)</td><td>0.00 <b>(+37.06%)</b></td><td>544.30 (+15.15%)</td><td>401.18 (+11.00%)</td><td>457.50 <b>(+21.97%)</b></td><td>243.90 (-0.45%)</td><td>141.19 <b>(+52.83%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>472.70 (n/a)</td><td>361.42 (n/a)</td><td>375.10 (n/a)</td><td>245.00 (n/a)</td><td>92.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-19.14%)</td><td>0.01 <b>(-30.76%)</b></td><td>0.01 <b>(-43.46%)</b></td><td>0.01 (-17.50%)</td><td>0.00 (-11.53%)</td><td>576.10 <b>(+21.21%)</b></td><td>453.62 <b>(+45.96%)</b></td><td>507.40 <b>(+76.86%)</b></td><td>283.90 <b>(+23.65%)</b></td><td>128.02 <b>(+30.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.30 (n/a)</td><td>310.78 (n/a)</td><td>286.90 (n/a)</td><td>229.60 (n/a)</td><td>97.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-14.49%)</td><td>0.01 (+9.01%)</td><td>0.01 (-0.94%)</td><td>0.01 <b>(+291.80%)</b></td><td>0.00 <b>(-62.22%)</b></td><td>541.00 <b>(-74.48%)</b></td><td>443.12 <b>(-41.89%)</b></td><td>449.30 (+0.97%)</td><td>361.30 (+16.96%)</td><td>80.54 <b>(-89.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2119.70 (n/a)</td><td>762.54 (n/a)</td><td>445.00 (n/a)</td><td>308.90 (n/a)</td><td>768.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-2.97%)</td><td>0.02 (-15.69%)</td><td>0.02 <b>(-40.93%)</b></td><td>0.02 (+13.64%)</td><td>0.01 (-14.52%)</td><td>482.80 (-12.01%)</td><td>387.50 (+15.04%)</td><td>441.10 <b>(+69.26%)</b></td><td>242.80 (+3.06%)</td><td>111.45 (-17.84%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.70 (n/a)</td><td>336.84 (n/a)</td><td>260.60 (n/a)</td><td>235.60 (n/a)</td><td>135.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-9.84%)</td><td>0.02 (-5.53%)</td><td>0.03 (-6.61%)</td><td>0.02 (+8.81%)</td><td>0.01 <b>(-28.56%)</b></td><td>484.20 (-8.09%)</td><td>356.44 (+1.30%)</td><td>316.50 (+7.11%)</td><td>265.50 (+10.95%)</td><td>93.63 <b>(-26.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.80 (n/a)</td><td>351.86 (n/a)</td><td>295.50 (n/a)</td><td>239.30 (n/a)</td><td>126.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-25.69%)</b></td><td>0.02 (-16.39%)</td><td>0.03 (-10.11%)</td><td>0.02 (-0.79%)</td><td>0.01 <b>(-30.66%)</b></td><td>528.60 (+0.80%)</td><td>367.08 (+15.25%)</td><td>292.40 (+11.26%)</td><td>268.10 <b>(+34.59%)</b></td><td>116.84 (-8.96%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.40 (n/a)</td><td>318.52 (n/a)</td><td>262.80 (n/a)</td><td>199.20 (n/a)</td><td>128.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (+13.38%)</td><td>0.03 (+6.07%)</td><td>0.03 (+12.86%)</td><td>0.01 <b>(-27.02%)</b></td><td>0.01 <b>(+70.60%)</b></td><td>590.90 <b>(+37.00%)</b></td><td>366.92 (+8.96%)</td><td>267.00 (-11.38%)</td><td>195.30 (-11.83%)</td><td>190.00 <b>(+108.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>431.30 (n/a)</td><td>336.74 (n/a)</td><td>301.30 (n/a)</td><td>221.50 (n/a)</td><td>91.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(+132.29%)</b></td><td>0.03 <b>(+105.60%)</b></td><td>0.03 <b>(+98.40%)</b></td><td>0.02 <b>(+109.98%)</b></td><td>0.01 <b>(+171.34%)</b></td><td>504.00 <b>(-52.38%)</b></td><td>302.72 <b>(-49.00%)</b></td><td>241.10 <b>(-49.60%)</b></td><td>170.80 <b>(-56.94%)</b></td><td>142.00 <b>(-46.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1058.40 (n/a)</td><td>593.62 (n/a)</td><td>478.40 (n/a)</td><td>396.70 (n/a)</td><td>267.59 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (+15.17%)</td><td>0.02 (+0.94%)</td><td>0.02 <b>(-32.05%)</b></td><td>0.02 (+3.10%)</td><td>0.01 <b>(+25.85%)</b></td><td>518.00 (-3.01%)</td><td>396.02 (+1.03%)</td><td>461.70 <b>(+47.18%)</b></td><td>252.50 (-13.14%)</td><td>125.50 (+1.52%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.10 (n/a)</td><td>391.98 (n/a)</td><td>313.70 (n/a)</td><td>290.70 (n/a)</td><td>123.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-34.26%)</b></td><td>0.02 (-6.96%)</td><td>0.02 (+9.16%)</td><td>0.01 (-7.24%)</td><td>0.01 <b>(-43.12%)</b></td><td>707.50 (+7.80%)</td><td>410.68 (-0.62%)</td><td>337.30 (-8.39%)</td><td>295.70 <b>(+52.11%)</b></td><td>172.52 (-7.37%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>413.24 (n/a)</td><td>368.20 (n/a)</td><td>194.40 (n/a)</td><td>186.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-8.14%)</td><td>0.02 <b>(-21.35%)</b></td><td>0.02 <b>(-20.50%)</b></td><td>0.01 (-18.66%)</td><td>0.00 (+2.95%)</td><td>621.90 <b>(+22.93%)</b></td><td>493.12 <b>(+28.73%)</b></td><td>490.30 <b>(+25.78%)</b></td><td>328.20 (+8.86%)</td><td>108.81 <b>(+34.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>505.90 (n/a)</td><td>383.08 (n/a)</td><td>389.80 (n/a)</td><td>301.50 (n/a)</td><td>80.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (+1.19%)</td><td>0.05 (+4.77%)</td><td>0.03 (-11.94%)</td><td>0.03 <b>(+357.33%)</b></td><td>0.02 <b>(-30.11%)</b></td><td>533.80 <b>(-78.14%)</b></td><td>405.00 <b>(-46.76%)</b></td><td>487.10 (+13.57%)</td><td>239.10 (-1.16%)</td><td>135.98 <b>(-85.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2441.40 (n/a)</td><td>760.64 (n/a)</td><td>428.90 (n/a)</td><td>241.90 (n/a)</td><td>944.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-11.07%)</td><td>0.05 (-19.48%)</td><td>0.04 <b>(-33.53%)</b></td><td>0.04 (+9.33%)</td><td>0.01 <b>(-23.50%)</b></td><td>459.20 (-8.54%)</td><td>372.26 <b>(+20.46%)</b></td><td>405.50 <b>(+50.46%)</b></td><td>268.80 (+12.47%)</td><td>79.80 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>502.10 (n/a)</td><td>309.02 (n/a)</td><td>269.50 (n/a)</td><td>239.00 (n/a)</td><td>108.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 <b>(-21.14%)</b></td><td>0.05 (+14.71%)</td><td>0.05 <b>(+43.53%)</b></td><td>0.03 <b>(+343.05%)</b></td><td>0.02 <b>(-49.41%)</b></td><td>541.10 <b>(-77.43%)</b></td><td>363.36 <b>(-53.75%)</b></td><td>328.60 <b>(-30.32%)</b></td><td>246.30 <b>(+26.76%)</b></td><td>123.00 <b>(-86.55%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2397.10 (n/a)</td><td>785.60 (n/a)</td><td>471.60 (n/a)</td><td>194.30 (n/a)</td><td>914.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-5.20%)</td><td>0.05 <b>(+20.87%)</b></td><td>0.04 (+16.41%)</td><td>0.03 <b>(+241.57%)</b></td><td>0.01 <b>(-33.45%)</b></td><td>541.30 <b>(-70.72%)</b></td><td>391.12 <b>(-44.02%)</b></td><td>420.10 (-14.11%)</td><td>261.70 (+5.48%)</td><td>120.95 <b>(-81.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1848.90 (n/a)</td><td>698.64 (n/a)</td><td>489.10 (n/a)</td><td>248.10 (n/a)</td><td>657.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-11.96%)</td><td>0.05 (-4.34%)</td><td>0.06 (-13.14%)</td><td>0.02 (-13.17%)</td><td>0.02 <b>(-20.02%)</b></td><td>660.30 (+15.18%)</td><td>355.14 (+3.13%)</td><td>286.80 (+15.13%)</td><td>252.30 (+13.60%)</td><td>172.19 (+11.74%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.30 (n/a)</td><td>344.36 (n/a)</td><td>249.10 (n/a)</td><td>222.10 (n/a)</td><td>154.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(-36.88%)</b></td><td>0.04 (-15.68%)</td><td>0.04 (+17.77%)</td><td>0.03 (-9.02%)</td><td>0.01 <b>(-56.95%)</b></td><td>556.50 (+9.92%)</td><td>435.38 (+10.52%)</td><td>383.90 (-15.09%)</td><td>343.30 <b>(+58.42%)</b></td><td>94.67 <b>(-25.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>506.30 (n/a)</td><td>393.92 (n/a)</td><td>452.10 (n/a)</td><td>216.70 (n/a)</td><td>126.84 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (+6.88%)</td><td>0.10 (-9.95%)</td><td>0.10 (-5.76%)</td><td>0.05 <b>(-32.96%)</b></td><td>0.04 <b>(+25.75%)</b></td><td>657.00 <b>(+49.18%)</b></td><td>387.80 (+19.93%)</td><td>318.10 (+6.10%)</td><td>217.20 (-6.42%)</td><td>174.37 <b>(+81.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>440.40 (n/a)</td><td>323.36 (n/a)</td><td>299.80 (n/a)</td><td>232.10 (n/a)</td><td>95.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 <b>(-28.61%)</b></td><td>0.08 <b>(-41.86%)</b></td><td>0.07 <b>(-46.09%)</b></td><td>0.06 <b>(-41.07%)</b></td><td>0.02 (-10.97%)</td><td>521.70 <b>(+69.71%)</b></td><td>421.14 <b>(+76.48%)</b></td><td>458.70 <b>(+85.48%)</b></td><td>270.80 <b>(+40.09%)</b></td><td>99.81 <b>(+113.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>307.40 (n/a)</td><td>238.64 (n/a)</td><td>247.30 (n/a)</td><td>193.30 (n/a)</td><td>46.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (-8.95%)</td><td>0.07 (-19.63%)</td><td>0.06 <b>(-34.52%)</b></td><td>0.06 <b>(+231.75%)</b></td><td>0.04 <b>(-33.78%)</b></td><td>581.30 <b>(-69.86%)</b></td><td>499.04 <b>(-23.48%)</b></td><td>559.70 <b>(+52.71%)</b></td><td>231.70 (+9.86%)</td><td>149.72 <b>(-79.32%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1928.50 (n/a)</td><td>652.14 (n/a)</td><td>366.50 (n/a)</td><td>210.90 (n/a)</td><td>724.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (-13.50%)</td><td>0.11 <b>(+48.46%)</b></td><td>0.11 <b>(+75.41%)</b></td><td>0.06 <b>(+285.60%)</b></td><td>0.03 <b>(-49.35%)</b></td><td>514.30 <b>(-74.07%)</b></td><td>334.42 <b>(-59.66%)</b></td><td>293.60 <b>(-42.99%)</b></td><td>231.90 (+15.66%)</td><td>109.60 <b>(-84.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1983.30 (n/a)</td><td>829.02 (n/a)</td><td>515.00 (n/a)</td><td>200.50 (n/a)</td><td>714.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 <b>(-24.37%)</b></td><td>0.08 (+0.09%)</td><td>0.07 (+14.00%)</td><td>0.06 (+12.06%)</td><td>0.02 <b>(-48.37%)</b></td><td>549.70 (-10.76%)</td><td>436.32 (-7.55%)</td><td>468.40 (-12.28%)</td><td>324.00 <b>(+32.24%)</b></td><td>92.35 <b>(-39.90%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>616.00 (n/a)</td><td>471.94 (n/a)</td><td>534.00 (n/a)</td><td>245.00 (n/a)</td><td>153.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-16.03%)</td><td>0.01 (-1.75%)</td><td>0.01 (+17.75%)</td><td>0.01 (+5.91%)</td><td>0.00 <b>(-30.39%)</b></td><td>437.90 (-5.58%)</td><td>342.28 (-2.19%)</td><td>334.70 (-15.07%)</td><td>244.90 (+19.06%)</td><td>86.85 (-20.00%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.80 (n/a)</td><td>349.94 (n/a)</td><td>394.10 (n/a)</td><td>205.70 (n/a)</td><td>108.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-8.23%)</td><td>0.01 (-4.11%)</td><td>0.01 (+12.13%)</td><td>0.01 (-8.79%)</td><td>0.00 <b>(-27.27%)</b></td><td>538.00 (+9.64%)</td><td>382.66 (+0.84%)</td><td>369.80 (-10.83%)</td><td>270.30 (+8.95%)</td><td>106.34 (-12.33%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.70 (n/a)</td><td>379.48 (n/a)</td><td>414.70 (n/a)</td><td>248.10 (n/a)</td><td>121.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(-61.33%)</b></td><td>0.01 <b>(-55.27%)</b></td><td>0.01 <b>(-47.53%)</b></td><td>0.00 <b>(-83.30%)</b></td><td>0.00 <b>(-55.90%)</b></td><td>2574.90 <b>(+498.81%)</b></td><td>932.36 <b>(+197.44%)</b></td><td>555.30 <b>(+90.63%)</b></td><td>378.80 <b>(+158.57%)</b></td><td>922.38 <b>(+677.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>430.00 (n/a)</td><td>313.46 (n/a)</td><td>291.30 (n/a)</td><td>146.50 (n/a)</td><td>118.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+1.50%)</td><td>0.01 (+7.10%)</td><td>0.01 (+11.75%)</td><td>0.01 (-1.59%)</td><td>0.00 (-1.92%)</td><td>450.10 (+1.60%)</td><td>312.26 (-6.54%)</td><td>280.20 (-10.51%)</td><td>265.00 (-1.45%)</td><td>77.68 (+3.84%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>443.00 (n/a)</td><td>334.12 (n/a)</td><td>313.10 (n/a)</td><td>268.90 (n/a)</td><td>74.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(-32.89%)</b></td><td>0.01 <b>(-28.89%)</b></td><td>0.01 (-18.48%)</td><td>0.00 <b>(-71.66%)</b></td><td>0.00 (-14.59%)</td><td>1832.30 <b>(+252.84%)</b></td><td>715.32 <b>(+85.37%)</b></td><td>522.50 <b>(+22.65%)</b></td><td>293.90 <b>(+48.96%)</b></td><td>638.64 <b>(+337.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>519.30 (n/a)</td><td>385.88 (n/a)</td><td>426.00 (n/a)</td><td>197.30 (n/a)</td><td>145.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-1.19%)</td><td>0.01 (-6.64%)</td><td>0.02 (+5.66%)</td><td>0.01 (-15.34%)</td><td>0.00 <b>(+58.38%)</b></td><td>493.80 (+18.11%)</td><td>343.52 (+14.10%)</td><td>262.70 (-5.33%)</td><td>243.30 (+1.21%)</td><td>124.69 <b>(+82.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>418.10 (n/a)</td><td>301.08 (n/a)</td><td>277.50 (n/a)</td><td>240.40 (n/a)</td><td>68.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+11.48%)</td><td>0.01 (-18.00%)</td><td>0.01 (-18.18%)</td><td>0.01 <b>(-20.81%)</b></td><td>0.01 <b>(+52.65%)</b></td><td>552.40 <b>(+26.26%)</b></td><td>376.54 <b>(+32.53%)</b></td><td>307.30 <b>(+22.19%)</b></td><td>201.40 (-10.33%)</td><td>152.32 <b>(+75.15%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.50 (n/a)</td><td>284.12 (n/a)</td><td>251.50 (n/a)</td><td>224.60 (n/a)</td><td>86.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-0.33%)</td><td>0.01 (+8.55%)</td><td>0.01 <b>(-30.59%)</b></td><td>0.01 <b>(+308.59%)</b></td><td>0.00 <b>(-60.29%)</b></td><td>468.50 <b>(-75.53%)</b></td><td>420.24 <b>(-55.09%)</b></td><td>460.40 <b>(+44.06%)</b></td><td>276.10 (+0.33%)</td><td>81.84 <b>(-90.74%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1914.40 (n/a)</td><td>935.66 (n/a)</td><td>319.60 (n/a)</td><td>275.20 (n/a)</td><td>883.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-12.14%)</td><td>0.01 (-6.00%)</td><td>0.01 (-10.85%)</td><td>0.01 <b>(+37.53%)</b></td><td>0.00 <b>(-33.82%)</b></td><td>566.50 <b>(-27.28%)</b></td><td>447.14 (-2.22%)</td><td>474.90 (+12.19%)</td><td>315.20 (+13.83%)</td><td>114.41 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>779.00 (n/a)</td><td>457.30 (n/a)</td><td>423.30 (n/a)</td><td>276.90 (n/a)</td><td>203.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(+44.12%)</b></td><td>0.01 (-9.65%)</td><td>0.01 <b>(-23.70%)</b></td><td>0.01 <b>(-25.35%)</b></td><td>0.01 <b>(+98.85%)</b></td><td>762.30 <b>(+33.95%)</b></td><td>488.36 <b>(+26.31%)</b></td><td>503.30 <b>(+31.07%)</b></td><td>197.60 <b>(-30.59%)</b></td><td>201.34 <b>(+73.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.10 (n/a)</td><td>386.64 (n/a)</td><td>384.00 (n/a)</td><td>284.70 (n/a)</td><td>116.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+3.51%)</td><td>0.01 (-12.62%)</td><td>0.01 (-14.54%)</td><td>0.01 <b>(-28.22%)</b></td><td>0.00 <b>(+45.39%)</b></td><td>609.80 <b>(+39.32%)</b></td><td>447.90 <b>(+22.56%)</b></td><td>475.10 (+16.99%)</td><td>258.80 (-3.40%)</td><td>152.57 <b>(+97.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.70 (n/a)</td><td>365.44 (n/a)</td><td>406.10 (n/a)</td><td>267.90 (n/a)</td><td>77.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+10.11%)</td><td>0.01 (+16.71%)</td><td>0.01 (+17.60%)</td><td>0.01 (+17.09%)</td><td>0.00 (+5.36%)</td><td>588.00 (-14.60%)</td><td>414.96 (-15.46%)</td><td>428.90 (-14.99%)</td><td>256.60 (-9.20%)</td><td>131.14 (-18.74%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>688.50 (n/a)</td><td>490.86 (n/a)</td><td>504.50 (n/a)</td><td>282.60 (n/a)</td><td>161.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (-18.02%)</td><td>0.02 <b>(-22.39%)</b></td><td>0.02 (+3.80%)</td><td>0.01 <b>(-22.74%)</b></td><td>0.01 <b>(-27.20%)</b></td><td>667.30 <b>(+29.42%)</b></td><td>474.34 <b>(+23.56%)</b></td><td>450.20 (-3.66%)</td><td>233.50 <b>(+22.00%)</b></td><td>163.56 (+5.27%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.60 (n/a)</td><td>383.90 (n/a)</td><td>467.30 (n/a)</td><td>191.40 (n/a)</td><td>155.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (-2.44%)</td><td>0.02 (-12.17%)</td><td>0.02 <b>(-51.68%)</b></td><td>0.01 <b>(+149.43%)</b></td><td>0.01 (-12.34%)</td><td>828.70 <b>(-59.91%)</b></td><td>478.10 <b>(-26.37%)</b></td><td>544.00 <b>(+106.92%)</b></td><td>204.80 (+2.50%)</td><td>252.09 <b>(-68.45%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2067.00 (n/a)</td><td>649.34 (n/a)</td><td>262.90 (n/a)</td><td>199.80 (n/a)</td><td>799.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+39.18%)</b></td><td>0.02 (-19.07%)</td><td>0.02 <b>(-40.17%)</b></td><td>0.02 <b>(-27.91%)</b></td><td>0.01 <b>(+195.83%)</b></td><td>544.20 <b>(+38.72%)</b></td><td>428.00 <b>(+40.65%)</b></td><td>488.90 <b>(+67.15%)</b></td><td>189.70 <b>(-28.14%)</b></td><td>141.79 <b>(+174.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>392.30 (n/a)</td><td>304.30 (n/a)</td><td>292.50 (n/a)</td><td>264.00 (n/a)</td><td>51.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (+7.38%)</td><td>0.02 (+6.84%)</td><td>0.03 <b>(+34.96%)</b></td><td>0.02 (-3.41%)</td><td>0.01 <b>(+27.49%)</b></td><td>505.80 (+3.54%)</td><td>369.68 (-3.41%)</td><td>307.20 <b>(-25.90%)</b></td><td>259.50 (-6.86%)</td><td>119.13 <b>(+32.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.50 (n/a)</td><td>382.74 (n/a)</td><td>414.60 (n/a)</td><td>278.60 (n/a)</td><td>90.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(+50.03%)</b></td><td>0.03 <b>(+21.45%)</b></td><td>0.02 (+15.77%)</td><td>0.01 <b>(-52.43%)</b></td><td>0.02 <b>(+127.60%)</b></td><td>1066.80 <b>(+110.21%)</b></td><td>460.68 (+13.77%)</td><td>414.30 (-13.63%)</td><td>173.20 <b>(-33.33%)</b></td><td>359.50 <b>(+206.98%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.50 (n/a)</td><td>404.94 (n/a)</td><td>479.70 (n/a)</td><td>259.80 (n/a)</td><td>117.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+24.43%)</b></td><td>0.03 <b>(+26.25%)</b></td><td>0.03 <b>(+53.27%)</b></td><td>0.01 <b>(+42.80%)</b></td><td>0.01 <b>(+21.54%)</b></td><td>720.50 <b>(-29.97%)</b></td><td>398.56 <b>(-22.58%)</b></td><td>311.20 <b>(-34.76%)</b></td><td>196.40 (-19.64%)</td><td>223.65 <b>(-29.07%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1028.90 (n/a)</td><td>514.82 (n/a)</td><td>477.00 (n/a)</td><td>244.40 (n/a)</td><td>315.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (+2.08%)</td><td>0.03 <b>(+40.87%)</b></td><td>0.03 <b>(+61.14%)</b></td><td>0.01 <b>(+89.63%)</b></td><td>0.01 (-18.69%)</td><td>688.70 <b>(-47.27%)</b></td><td>366.76 <b>(-41.52%)</b></td><td>305.40 <b>(-37.94%)</b></td><td>196.90 (-2.04%)</td><td>188.70 <b>(-54.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1306.00 (n/a)</td><td>627.18 (n/a)</td><td>492.10 (n/a)</td><td>201.00 (n/a)</td><td>415.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+26.73%)</b></td><td>0.02 (+14.39%)</td><td>0.03 <b>(+39.83%)</b></td><td>0.01 (-19.09%)</td><td>0.01 <b>(+103.79%)</b></td><td>580.40 <b>(+23.59%)</b></td><td>388.10 (-0.90%)</td><td>311.60 <b>(-28.48%)</b></td><td>219.10 <b>(-21.10%)</b></td><td>178.18 <b>(+113.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.60 (n/a)</td><td>391.64 (n/a)</td><td>435.70 (n/a)</td><td>277.70 (n/a)</td><td>83.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (+18.27%)</td><td>0.02 (+19.63%)</td><td>0.01 (+7.05%)</td><td>0.00 (+2.16%)</td><td>0.01 (+12.50%)</td><td>1864.70 (-2.11%)</td><td>740.40 (-19.12%)</td><td>578.20 (-6.58%)</td><td>196.80 (-15.43%)</td><td>648.37 (-6.76%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1904.90 (n/a)</td><td>915.48 (n/a)</td><td>618.90 (n/a)</td><td>232.70 (n/a)</td><td>695.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+26.92%)</b></td><td>0.03 (-1.60%)</td><td>0.02 <b>(-37.63%)</b></td><td>0.01 (+2.45%)</td><td>0.01 (+19.90%)</td><td>551.20 (-2.39%)</td><td>372.42 (+2.76%)</td><td>408.90 <b>(+60.35%)</b></td><td>189.50 <b>(-21.24%)</b></td><td>149.81 (-7.02%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.70 (n/a)</td><td>362.42 (n/a)</td><td>255.00 (n/a)</td><td>240.60 (n/a)</td><td>161.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+65.19%)</b></td><td>0.02 (+10.67%)</td><td>0.02 (-0.04%)</td><td>0.02 (-0.24%)</td><td>0.01 <b>(+174.07%)</b></td><td>545.30 (+0.24%)</td><td>452.78 (-2.14%)</td><td>482.70 (+0.04%)</td><td>228.80 <b>(-39.45%)</b></td><td>128.39 <b>(+61.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>544.00 (n/a)</td><td>462.66 (n/a)</td><td>482.50 (n/a)</td><td>377.90 (n/a)</td><td>79.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-2.28%)</td><td>0.02 (-4.09%)</td><td>0.01 (-11.90%)</td><td>0.01 <b>(+178.27%)</b></td><td>0.00 <b>(-39.08%)</b></td><td>680.90 <b>(-64.06%)</b></td><td>570.50 <b>(-23.66%)</b></td><td>635.50 (+13.50%)</td><td>350.10 (+2.34%)</td><td>140.99 <b>(-78.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1894.80 (n/a)</td><td>747.32 (n/a)</td><td>559.90 (n/a)</td><td>342.10 (n/a)</td><td>650.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 <b>(-36.60%)</b></td><td>0.04 <b>(-39.98%)</b></td><td>0.03 <b>(-47.05%)</b></td><td>0.02 <b>(-47.48%)</b></td><td>0.02 (-19.22%)</td><td>1052.90 <b>(+90.40%)</b></td><td>572.82 <b>(+82.25%)</b></td><td>533.00 <b>(+88.87%)</b></td><td>290.40 <b>(+57.74%)</b></td><td>309.56 <b>(+119.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.00 (n/a)</td><td>314.30 (n/a)</td><td>282.20 (n/a)</td><td>184.10 (n/a)</td><td>141.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 <b>(-22.42%)</b></td><td>0.05 (+5.96%)</td><td>0.06 <b>(+47.48%)</b></td><td>0.04 (+15.02%)</td><td>0.01 <b>(-55.83%)</b></td><td>421.00 (-13.05%)</td><td>317.22 (-13.79%)</td><td>289.70 <b>(-32.20%)</b></td><td>262.00 <b>(+28.87%)</b></td><td>62.61 <b>(-50.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>484.20 (n/a)</td><td>367.96 (n/a)</td><td>427.30 (n/a)</td><td>203.30 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (+6.15%)</td><td>0.04 (-3.86%)</td><td>0.03 (-9.41%)</td><td>0.03 <b>(-23.50%)</b></td><td>0.02 <b>(+39.55%)</b></td><td>647.60 <b>(+30.72%)</b></td><td>432.36 (+11.50%)</td><td>481.40 (+10.36%)</td><td>260.00 (-5.80%)</td><td>164.95 <b>(+65.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>495.40 (n/a)</td><td>387.78 (n/a)</td><td>436.20 (n/a)</td><td>276.00 (n/a)</td><td>99.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-7.49%)</td><td>0.05 (-14.95%)</td><td>0.05 (-6.80%)</td><td>0.03 <b>(-33.43%)</b></td><td>0.02 <b>(+65.76%)</b></td><td>577.80 <b>(+50.19%)</b></td><td>390.28 <b>(+26.95%)</b></td><td>318.40 (+7.31%)</td><td>261.00 (+8.12%)</td><td>142.29 <b>(+172.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>384.70 (n/a)</td><td>307.42 (n/a)</td><td>296.70 (n/a)</td><td>241.40 (n/a)</td><td>52.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (-9.74%)</td><td>0.04 (-6.15%)</td><td>0.03 (-15.16%)</td><td>0.03 (-6.95%)</td><td>0.02 (-1.62%)</td><td>601.20 (+7.45%)</td><td>432.30 (+8.15%)</td><td>516.40 (+17.87%)</td><td>248.10 (+10.81%)</td><td>162.76 (+13.41%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>399.72 (n/a)</td><td>438.10 (n/a)</td><td>223.90 (n/a)</td><td>143.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-3.25%)</td><td>0.05 (+14.76%)</td><td>0.06 (+9.40%)</td><td>0.04 <b>(+41.60%)</b></td><td>0.01 <b>(-36.42%)</b></td><td>454.20 <b>(-29.37%)</b></td><td>323.60 (-18.64%)</td><td>292.50 (-8.59%)</td><td>279.60 (+3.36%)</td><td>73.35 <b>(-52.45%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>643.10 (n/a)</td><td>397.76 (n/a)</td><td>320.00 (n/a)</td><td>270.50 (n/a)</td><td>154.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-19.98%)</td><td>0.03 <b>(-30.06%)</b></td><td>0.03 (-12.31%)</td><td>0.01 <b>(-69.23%)</b></td><td>0.02 (+3.12%)</td><td>1993.60 <b>(+224.96%)</b></td><td>1050.94 <b>(+122.58%)</b></td><td>565.30 (+14.04%)</td><td>257.90 <b>(+24.95%)</b></td><td>839.16 <b>(+433.84%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>613.50 (n/a)</td><td>472.16 (n/a)</td><td>495.70 (n/a)</td><td>206.40 (n/a)</td><td>157.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-10.45%)</td><td>0.04 (+8.92%)</td><td>0.04 (+2.92%)</td><td>0.03 <b>(+344.44%)</b></td><td>0.01 <b>(-50.05%)</b></td><td>538.10 <b>(-77.50%)</b></td><td>416.88 <b>(-47.90%)</b></td><td>445.30 (-2.84%)</td><td>272.90 (+11.66%)</td><td>102.71 <b>(-88.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2391.70 (n/a)</td><td>800.22 (n/a)</td><td>458.30 (n/a)</td><td>244.40 (n/a)</td><td>900.59 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (-13.12%)</td><td>0.04 <b>(-36.26%)</b></td><td>0.03 <b>(-48.52%)</b></td><td>0.03 <b>(-32.07%)</b></td><td>0.02 <b>(+20.63%)</b></td><td>593.10 <b>(+47.21%)</b></td><td>465.26 <b>(+67.35%)</b></td><td>509.20 <b>(+94.28%)</b></td><td>227.30 (+15.09%)</td><td>142.38 <b>(+86.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>402.90 (n/a)</td><td>278.02 (n/a)</td><td>262.10 (n/a)</td><td>197.50 (n/a)</td><td>76.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 <b>(-22.02%)</b></td><td>0.05 <b>(-30.26%)</b></td><td>0.04 <b>(-46.90%)</b></td><td>0.03 <b>(-25.00%)</b></td><td>0.02 (+2.65%)</td><td>480.20 <b>(+33.35%)</b></td><td>387.00 <b>(+49.61%)</b></td><td>466.30 <b>(+88.33%)</b></td><td>232.10 <b>(+28.23%)</b></td><td>118.53 <b>(+81.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>360.10 (n/a)</td><td>258.68 (n/a)</td><td>247.60 (n/a)</td><td>181.00 (n/a)</td><td>65.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(-32.03%)</b></td><td>0.03 <b>(-21.40%)</b></td><td>0.03 <b>(-24.31%)</b></td><td>0.02 (-3.87%)</td><td>0.01 <b>(-45.37%)</b></td><td>682.80 (+4.04%)</td><td>509.42 <b>(+20.32%)</b></td><td>515.90 <b>(+32.11%)</b></td><td>343.60 <b>(+47.09%)</b></td><td>128.98 (-15.97%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.30 (n/a)</td><td>423.40 (n/a)</td><td>390.50 (n/a)</td><td>233.60 (n/a)</td><td>153.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-12.79%)</td><td>0.04 (-15.62%)</td><td>0.04 <b>(-34.94%)</b></td><td>0.02 <b>(+97.95%)</b></td><td>0.02 <b>(-29.13%)</b></td><td>1011.90 <b>(-49.48%)</b></td><td>521.00 (-19.95%)</td><td>462.50 <b>(+53.71%)</b></td><td>289.50 (+14.65%)</td><td>292.63 <b>(-61.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2003.00 (n/a)</td><td>650.82 (n/a)</td><td>300.90 (n/a)</td><td>252.50 (n/a)</td><td>759.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.19 (+7.94%)</td><td>0.12 (+1.50%)</td><td>0.12 (-9.03%)</td><td>0.07 (+7.85%)</td><td>0.05 (-7.22%)</td><td>491.00 (-7.29%)</td><td>307.90 (-5.87%)</td><td>276.20 (+9.91%)</td><td>176.00 (-7.32%)</td><td>122.16 <b>(-20.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>529.60 (n/a)</td><td>327.10 (n/a)</td><td>251.30 (n/a)</td><td>189.90 (n/a)</td><td>154.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 <b>(-41.90%)</b></td><td>0.09 <b>(-42.64%)</b></td><td>0.11 <b>(-28.50%)</b></td><td>0.06 <b>(-54.94%)</b></td><td>0.03 (-13.66%)</td><td>547.00 <b>(+121.91%)</b></td><td>382.10 <b>(+83.74%)</b></td><td>298.00 <b>(+39.84%)</b></td><td>280.40 <b>(+72.13%)</b></td><td>128.36 <b>(+222.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>246.50 (n/a)</td><td>207.96 (n/a)</td><td>213.10 (n/a)</td><td>162.90 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (+18.29%)</td><td>0.10 <b>(+33.74%)</b></td><td>0.11 <b>(+65.86%)</b></td><td>0.06 <b>(+20.67%)</b></td><td>0.03 <b>(+24.93%)</b></td><td>521.80 (-17.12%)</td><td>371.04 <b>(-23.65%)</b></td><td>297.50 <b>(-39.70%)</b></td><td>227.50 (-15.49%)</td><td>137.30 (-0.56%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>629.60 (n/a)</td><td>485.96 (n/a)</td><td>493.40 (n/a)</td><td>269.20 (n/a)</td><td>138.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (+16.10%)</td><td>0.10 (-4.68%)</td><td>0.08 <b>(-30.53%)</b></td><td>0.07 (-1.69%)</td><td>0.03 <b>(+32.25%)</b></td><td>504.00 (+1.72%)</td><td>370.04 (+7.88%)</td><td>411.50 <b>(+43.98%)</b></td><td>231.30 (-13.89%)</td><td>113.00 (+15.45%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>495.50 (n/a)</td><td>343.00 (n/a)</td><td>285.80 (n/a)</td><td>268.60 (n/a)</td><td>97.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 <b>(+32.07%)</b></td><td>0.08 <b>(+28.45%)</b></td><td>0.06 (+3.85%)</td><td>0.04 <b>(+127.26%)</b></td><td>0.04 <b>(+22.84%)</b></td><td>812.10 <b>(-56.00%)</b></td><td>473.36 <b>(-35.30%)</b></td><td>515.70 (-3.72%)</td><td>224.20 <b>(-24.28%)</b></td><td>230.90 <b>(-63.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1845.50 (n/a)</td><td>731.62 (n/a)</td><td>535.60 (n/a)</td><td>296.10 (n/a)</td><td>634.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 <b>(+82.97%)</b></td><td>0.13 <b>(+104.40%)</b></td><td>0.13 <b>(+107.95%)</b></td><td>0.10 <b>(+213.87%)</b></td><td>0.02 (+16.05%)</td><td>337.60 <b>(-68.14%)</b></td><td>267.78 <b>(-55.06%)</b></td><td>243.60 <b>(-51.91%)</b></td><td>218.10 <b>(-45.35%)</b></td><td>49.24 <b>(-81.32%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1059.60 (n/a)</td><td>595.80 (n/a)</td><td>506.50 (n/a)</td><td>399.10 (n/a)</td><td>263.61 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (+13.85%)</td><td>0.11 (-3.26%)</td><td>0.12 (+1.17%)</td><td>0.07 (-3.95%)</td><td>0.04 <b>(+47.64%)</b></td><td>493.00 (+4.10%)</td><td>344.30 (+8.75%)</td><td>278.10 (-1.17%)</td><td>213.50 (-12.18%)</td><td>124.73 <b>(+36.69%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>473.60 (n/a)</td><td>316.60 (n/a)</td><td>281.40 (n/a)</td><td>243.10 (n/a)</td><td>91.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 <b>(+81.63%)</b></td><td>0.11 <b>(+53.15%)</b></td><td>0.12 <b>(+71.29%)</b></td><td>0.06 (-11.65%)</td><td>0.03 <b>(+452.16%)</b></td><td>551.70 (+13.19%)</td><td>323.94 <b>(-27.90%)</b></td><td>270.20 <b>(-41.62%)</b></td><td>218.50 <b>(-44.93%)</b></td><td>133.89 <b>(+259.83%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>487.40 (n/a)</td><td>449.30 (n/a)</td><td>462.80 (n/a)</td><td>396.80 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 <b>(-38.07%)</b></td><td>0.07 <b>(-31.95%)</b></td><td>0.06 <b>(-29.58%)</b></td><td>0.06 (-0.63%)</td><td>0.01 <b>(-64.12%)</b></td><td>549.20 (+0.64%)</td><td>480.94 <b>(+33.82%)</b></td><td>536.30 <b>(+41.99%)</b></td><td>356.80 <b>(+61.45%)</b></td><td>88.93 <b>(-35.45%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>545.70 (n/a)</td><td>359.38 (n/a)</td><td>377.70 (n/a)</td><td>221.00 (n/a)</td><td>137.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (+7.77%)</td><td>0.07 <b>(-29.96%)</b></td><td>0.06 <b>(-34.23%)</b></td><td>0.02 <b>(-76.70%)</b></td><td>0.04 <b>(+165.08%)</b></td><td>1769.80 <b>(+329.25%)</b></td><td>725.48 <b>(+102.53%)</b></td><td>525.30 <b>(+52.04%)</b></td><td>273.00 (-7.24%)</td><td>595.43 <b>(+1036.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>412.30 (n/a)</td><td>358.20 (n/a)</td><td>345.50 (n/a)</td><td>294.30 (n/a)</td><td>52.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 <b>(+34.56%)</b></td><td>0.09 (+15.80%)</td><td>0.08 (+7.59%)</td><td>0.06 (+7.06%)</td><td>0.03 <b>(+62.10%)</b></td><td>511.10 (-6.58%)</td><td>386.10 (-9.83%)</td><td>431.50 (-7.04%)</td><td>235.60 <b>(-25.68%)</b></td><td>122.11 (+17.84%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>547.10 (n/a)</td><td>428.20 (n/a)</td><td>464.20 (n/a)</td><td>317.00 (n/a)</td><td>103.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 <b>(+21.77%)</b></td><td>0.08 (+7.23%)</td><td>0.06 <b>(-29.12%)</b></td><td>0.04 <b>(+152.75%)</b></td><td>0.04 (+9.93%)</td><td>765.10 <b>(-60.44%)</b></td><td>489.76 <b>(-28.78%)</b></td><td>550.20 <b>(+41.08%)</b></td><td>259.40 (-17.89%)</td><td>218.96 <b>(-68.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1933.80 (n/a)</td><td>687.68 (n/a)</td><td>390.00 (n/a)</td><td>315.90 (n/a)</td><td>699.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (+11.51%)</td><td>0.08 (+12.78%)</td><td>0.09 (+3.18%)</td><td>0.05 (-3.20%)</td><td>0.02 (+11.63%)</td><td>544.30 (+3.30%)</td><td>319.80 (-9.86%)</td><td>278.30 (-3.10%)</td><td>242.10 (-10.33%)</td><td>127.14 (+11.00%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.90 (n/a)</td><td>354.80 (n/a)</td><td>287.20 (n/a)</td><td>270.00 (n/a)</td><td>114.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 (+12.19%)</td><td>0.18 <b>(+37.39%)</b></td><td>0.20 (+19.92%)</td><td>0.09 <b>(+250.89%)</b></td><td>0.05 <b>(-29.18%)</b></td><td>543.40 <b>(-71.50%)</b></td><td>308.32 <b>(-53.12%)</b></td><td>251.30 (-16.59%)</td><td>244.40 (-10.87%)</td><td>131.45 <b>(-81.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1906.60 (n/a)</td><td>657.72 (n/a)</td><td>301.30 (n/a)</td><td>274.20 (n/a)</td><td>706.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.03 (+2.41%)</td><td>3.50 (+14.52%)</td><td>3.48 <b>(+30.51%)</b></td><td>2.76 (+5.94%)</td><td>0.49 (-18.13%)</td><td>3799.20 (-5.61%)</td><td>3048.92 (-13.62%)</td><td>3017.00 <b>(-23.38%)</b></td><td>2599.50 (-2.35%)</td><td>465.02 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.94 (n/a)</td><td>3.05 (n/a)</td><td>2.66 (n/a)</td><td>2.61 (n/a)</td><td>0.60 (n/a)</td><td>4024.80 (n/a)</td><td>3529.46 (n/a)</td><td>3937.50 (n/a)</td><td>2662.10 (n/a)</td><td>622.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (+10.98%)</td><td>0.14 <b>(+39.00%)</b></td><td>0.16 <b>(+68.92%)</b></td><td>0.06 <b>(-27.59%)</b></td><td>0.05 <b>(+53.89%)</b></td><td>698.20 <b>(+38.12%)</b></td><td>344.10 (-19.76%)</td><td>257.80 <b>(-40.79%)</b></td><td>241.00 (-9.87%)</td><td>198.28 <b>(+104.13%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>505.50 (n/a)</td><td>428.86 (n/a)</td><td>435.40 (n/a)</td><td>267.40 (n/a)</td><td>97.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+5.71%)</td><td>0.02 (-18.42%)</td><td>0.01 <b>(-31.07%)</b></td><td>0.01 (-13.15%)</td><td>0.00 <b>(+32.52%)</b></td><td>468.50 (+15.14%)</td><td>363.44 <b>(+25.88%)</b></td><td>386.70 <b>(+45.05%)</b></td><td>223.00 (-5.39%)</td><td>91.41 <b>(+33.27%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>406.90 (n/a)</td><td>288.72 (n/a)</td><td>266.60 (n/a)</td><td>235.70 (n/a)</td><td>68.59 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (-10.12%)</td><td>0.01 (-7.87%)</td><td>0.01 (-18.95%)</td><td>0.01 (+6.30%)</td><td>0.00 <b>(-28.92%)</b></td><td>486.70 (-5.92%)</td><td>388.60 (+4.57%)</td><td>359.60 <b>(+23.36%)</b></td><td>295.30 (+11.27%)</td><td>92.17 <b>(-24.90%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.30 (n/a)</td><td>371.62 (n/a)</td><td>291.50 (n/a)</td><td>265.40 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(-24.71%)</b></td><td>0.01 <b>(-25.19%)</b></td><td>0.01 (-18.43%)</td><td>0.01 <b>(-28.19%)</b></td><td>0.00 <b>(-28.49%)</b></td><td>713.10 <b>(+39.25%)</b></td><td>505.98 <b>(+33.43%)</b></td><td>494.90 <b>(+22.59%)</b></td><td>353.70 <b>(+32.82%)</b></td><td>136.00 <b>(+36.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.10 (n/a)</td><td>379.22 (n/a)</td><td>403.70 (n/a)</td><td>266.30 (n/a)</td><td>99.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+3.79%)</td><td>0.01 (+11.92%)</td><td>0.01 <b>(+59.77%)</b></td><td>0.01 (-2.88%)</td><td>0.00 (+10.10%)</td><td>636.30 (+2.96%)</td><td>415.88 (-8.44%)</td><td>292.40 <b>(-37.41%)</b></td><td>270.60 (-3.67%)</td><td>180.16 (+10.67%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.00 (n/a)</td><td>454.24 (n/a)</td><td>467.20 (n/a)</td><td>280.90 (n/a)</td><td>162.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+15.55%)</td><td>0.02 <b>(+89.36%)</b></td><td>0.02 <b>(+70.05%)</b></td><td>0.01 <b>(+567.65%)</b></td><td>0.00 <b>(-62.44%)</b></td><td>367.50 <b>(-85.02%)</b></td><td>294.50 <b>(-73.36%)</b></td><td>291.50 <b>(-41.19%)</b></td><td>241.70 (-13.46%)</td><td>46.19 <b>(-95.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2453.80 (n/a)</td><td>1105.44 (n/a)</td><td>495.70 (n/a)</td><td>279.30 (n/a)</td><td>1005.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-5.34%)</td><td>0.01 (-15.10%)</td><td>0.01 (-5.48%)</td><td>0.00 <b>(-59.26%)</b></td><td>0.00 (+14.37%)</td><td>1288.80 <b>(+145.49%)</b></td><td>566.78 <b>(+43.50%)</b></td><td>455.90 (+5.80%)</td><td>243.00 (+5.65%)</td><td>414.26 <b>(+220.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.00 (n/a)</td><td>394.98 (n/a)</td><td>430.90 (n/a)</td><td>230.00 (n/a)</td><td>129.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 <b>(-32.79%)</b></td><td>0.01 <b>(-36.04%)</b></td><td>0.01 <b>(-34.85%)</b></td><td>0.01 <b>(-50.60%)</b></td><td>0.00 (-18.04%)</td><td>924.30 <b>(+102.43%)</b></td><td>533.22 <b>(+64.90%)</b></td><td>462.00 <b>(+53.49%)</b></td><td>354.80 <b>(+48.76%)</b></td><td>223.54 <b>(+164.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.60 (n/a)</td><td>323.36 (n/a)</td><td>301.00 (n/a)</td><td>238.50 (n/a)</td><td>84.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+13.31%)</td><td>0.01 (-17.86%)</td><td>0.00 <b>(-47.16%)</b></td><td>0.00 <b>(-73.69%)</b></td><td>0.01 <b>(+187.73%)</b></td><td>1895.60 <b>(+280.03%)</b></td><td>1036.52 <b>(+135.33%)</b></td><td>912.20 <b>(+89.21%)</b></td><td>261.00 (-11.73%)</td><td>805.08 <b>(+843.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.80 (n/a)</td><td>440.46 (n/a)</td><td>482.10 (n/a)</td><td>295.70 (n/a)</td><td>85.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(+51.06%)</b></td><td>0.01 (+2.14%)</td><td>0.01 <b>(-20.83%)</b></td><td>0.01 <b>(+37.82%)</b></td><td>0.01 <b>(+69.56%)</b></td><td>566.90 <b>(-27.44%)</b></td><td>479.14 (+2.16%)</td><td>547.70 <b>(+26.31%)</b></td><td>206.40 <b>(-33.80%)</b></td><td>153.36 (-19.55%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>781.30 (n/a)</td><td>469.02 (n/a)</td><td>433.60 (n/a)</td><td>311.80 (n/a)</td><td>190.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-5.07%)</td><td>0.01 (+8.99%)</td><td>0.01 (+17.49%)</td><td>0.01 <b>(-22.15%)</b></td><td>0.00 <b>(+20.66%)</b></td><td>678.10 <b>(+28.43%)</b></td><td>418.26 (-2.25%)</td><td>373.20 (-14.89%)</td><td>259.60 (+5.36%)</td><td>178.95 <b>(+59.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.00 (n/a)</td><td>427.90 (n/a)</td><td>438.50 (n/a)</td><td>246.40 (n/a)</td><td>112.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-16.85%)</td><td>0.01 (+8.93%)</td><td>0.01 (+12.19%)</td><td>0.01 <b>(+49.28%)</b></td><td>0.00 <b>(-37.41%)</b></td><td>646.00 <b>(-33.01%)</b></td><td>454.02 <b>(-23.77%)</b></td><td>459.50 (-10.86%)</td><td>243.80 <b>(+20.28%)</b></td><td>146.63 <b>(-51.01%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>964.30 (n/a)</td><td>595.60 (n/a)</td><td>515.50 (n/a)</td><td>202.70 (n/a)</td><td>299.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+16.50%)</td><td>0.01 (+12.72%)</td><td>0.01 (+17.64%)</td><td>0.01 (-7.70%)</td><td>0.00 <b>(+51.13%)</b></td><td>567.30 (+8.35%)</td><td>400.74 (-7.14%)</td><td>400.10 (-14.98%)</td><td>258.10 (-14.17%)</td><td>132.12 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.60 (n/a)</td><td>431.56 (n/a)</td><td>470.60 (n/a)</td><td>300.70 (n/a)</td><td>96.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-16.93%)</td><td>0.02 (+0.47%)</td><td>0.02 (-5.89%)</td><td>0.02 (-6.67%)</td><td>0.01 (-15.29%)</td><td>527.40 (+7.15%)</td><td>396.48 (-1.11%)</td><td>426.80 (+6.27%)</td><td>278.20 <b>(+20.38%)</b></td><td>111.28 (+6.48%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.20 (n/a)</td><td>400.92 (n/a)</td><td>401.60 (n/a)</td><td>231.10 (n/a)</td><td>104.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (+17.75%)</td><td>0.03 (-2.52%)</td><td>0.03 (-5.03%)</td><td>0.03 (+7.06%)</td><td>0.01 <b>(+20.06%)</b></td><td>478.00 (-6.60%)</td><td>409.74 (+3.41%)</td><td>444.50 (+5.28%)</td><td>245.90 (-15.09%)</td><td>95.21 (-3.60%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.80 (n/a)</td><td>396.22 (n/a)</td><td>422.20 (n/a)</td><td>289.60 (n/a)</td><td>98.77 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (+15.51%)</td><td>0.03 <b>(+25.90%)</b></td><td>0.03 <b>(+33.13%)</b></td><td>0.02 (+11.56%)</td><td>0.01 <b>(+38.87%)</b></td><td>531.00 (-10.36%)</td><td>336.54 (-18.70%)</td><td>276.30 <b>(-24.90%)</b></td><td>256.10 (-13.45%)</td><td>117.34 (+3.21%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.40 (n/a)</td><td>413.96 (n/a)</td><td>367.90 (n/a)</td><td>295.90 (n/a)</td><td>113.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(+52.48%)</b></td><td>0.02 (+15.32%)</td><td>0.02 (+3.55%)</td><td>0.02 (+2.76%)</td><td>0.01 <b>(+215.01%)</b></td><td>519.00 (-2.68%)</td><td>431.02 (-9.74%)</td><td>458.30 (-3.41%)</td><td>279.40 <b>(-34.43%)</b></td><td>93.63 <b>(+95.04%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>533.30 (n/a)</td><td>477.52 (n/a)</td><td>474.50 (n/a)</td><td>426.10 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-14.88%)</td><td>0.02 <b>(-32.04%)</b></td><td>0.01 <b>(-44.93%)</b></td><td>0.00 <b>(-74.36%)</b></td><td>0.01 <b>(+54.26%)</b></td><td>1938.90 <b>(+290.04%)</b></td><td>983.02 <b>(+171.57%)</b></td><td>551.50 <b>(+81.59%)</b></td><td>259.90 (+17.50%)</td><td>858.20 <b>(+591.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.10 (n/a)</td><td>361.98 (n/a)</td><td>303.70 (n/a)</td><td>221.20 (n/a)</td><td>124.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (+19.73%)</td><td>0.03 (-1.30%)</td><td>0.02 (-9.81%)</td><td>0.02 <b>(+31.62%)</b></td><td>0.01 (+5.40%)</td><td>496.40 <b>(-24.03%)</b></td><td>416.66 (-1.58%)</td><td>459.30 (+10.86%)</td><td>226.80 (-16.46%)</td><td>109.20 <b>(-31.94%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>653.40 (n/a)</td><td>423.34 (n/a)</td><td>414.30 (n/a)</td><td>271.50 (n/a)</td><td>160.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (+17.00%)</td><td>0.02 (+14.79%)</td><td>0.02 (-6.66%)</td><td>0.01 <b>(+148.43%)</b></td><td>0.01 (+5.37%)</td><td>748.60 <b>(-59.75%)</b></td><td>449.88 <b>(-34.16%)</b></td><td>483.40 (+7.14%)</td><td>197.90 (-14.55%)</td><td>208.27 <b>(-68.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1859.70 (n/a)</td><td>683.34 (n/a)</td><td>451.20 (n/a)</td><td>231.60 (n/a)</td><td>666.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-14.55%)</td><td>0.02 <b>(-27.46%)</b></td><td>0.02 <b>(-28.67%)</b></td><td>0.00 <b>(-68.59%)</b></td><td>0.01 (+13.61%)</td><td>1954.50 <b>(+218.37%)</b></td><td>749.04 <b>(+86.61%)</b></td><td>512.80 <b>(+40.19%)</b></td><td>302.90 (+17.04%)</td><td>679.87 <b>(+382.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>613.90 (n/a)</td><td>401.40 (n/a)</td><td>365.80 (n/a)</td><td>258.80 (n/a)</td><td>140.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 <b>(-34.87%)</b></td><td>0.02 <b>(-20.42%)</b></td><td>0.02 <b>(-29.20%)</b></td><td>0.02 (+0.06%)</td><td>0.00 <b>(-55.09%)</b></td><td>488.80 (-0.06%)</td><td>403.56 (+15.59%)</td><td>424.30 <b>(+41.25%)</b></td><td>309.80 <b>(+53.52%)</b></td><td>82.87 <b>(-37.33%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.10 (n/a)</td><td>349.12 (n/a)</td><td>300.40 (n/a)</td><td>201.80 (n/a)</td><td>132.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(-33.51%)</b></td><td>0.02 (-0.84%)</td><td>0.02 <b>(+29.28%)</b></td><td>0.01 <b>(+144.19%)</b></td><td>0.00 <b>(-59.52%)</b></td><td>809.80 <b>(-59.05%)</b></td><td>521.12 <b>(-32.06%)</b></td><td>467.90 <b>(-22.65%)</b></td><td>378.10 <b>(+50.40%)</b></td><td>168.91 <b>(-75.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1977.60 (n/a)</td><td>767.08 (n/a)</td><td>604.90 (n/a)</td><td>251.40 (n/a)</td><td>693.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (-7.69%)</td><td>0.02 (-5.28%)</td><td>0.02 (+0.08%)</td><td>0.01 (-9.82%)</td><td>0.01 (-10.21%)</td><td>551.70 (+10.89%)</td><td>438.12 (+5.04%)</td><td>461.90 (-0.09%)</td><td>248.20 (+8.29%)</td><td>115.79 (+5.42%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.50 (n/a)</td><td>417.10 (n/a)</td><td>462.30 (n/a)</td><td>229.20 (n/a)</td><td>109.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 <b>(-22.69%)</b></td><td>0.05 (-17.44%)</td><td>0.06 (+7.79%)</td><td>0.02 <b>(-21.38%)</b></td><td>0.02 (-5.72%)</td><td>673.80 <b>(+27.20%)</b></td><td>407.94 <b>(+27.73%)</b></td><td>285.60 (-7.24%)</td><td>244.50 <b>(+29.37%)</b></td><td>195.40 <b>(+52.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.70 (n/a)</td><td>319.38 (n/a)</td><td>307.90 (n/a)</td><td>189.00 (n/a)</td><td>128.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-1.66%)</td><td>0.07 (+0.34%)</td><td>0.08 <b>(+28.62%)</b></td><td>0.04 (-6.67%)</td><td>0.03 (+19.63%)</td><td>594.40 (+7.14%)</td><td>407.86 (+5.04%)</td><td>306.70 <b>(-22.24%)</b></td><td>256.30 (+1.71%)</td><td>168.45 <b>(+41.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.80 (n/a)</td><td>388.30 (n/a)</td><td>394.40 (n/a)</td><td>252.00 (n/a)</td><td>118.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (-17.36%)</td><td>0.04 (-9.05%)</td><td>0.04 (-17.72%)</td><td>0.03 (+9.35%)</td><td>0.01 (-19.51%)</td><td>515.40 (-8.55%)</td><td>409.66 (+7.36%)</td><td>434.10 <b>(+21.56%)</b></td><td>293.60 <b>(+21.02%)</b></td><td>110.26 (-13.12%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.60 (n/a)</td><td>381.56 (n/a)</td><td>357.10 (n/a)</td><td>242.60 (n/a)</td><td>126.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(-42.49%)</b></td><td>0.03 <b>(-38.42%)</b></td><td>0.04 (-19.73%)</td><td>0.01 <b>(-71.61%)</b></td><td>0.02 <b>(-32.18%)</b></td><td>2019.10 <b>(+252.31%)</b></td><td>822.32 <b>(+98.68%)</b></td><td>570.50 <b>(+24.59%)</b></td><td>406.50 <b>(+73.87%)</b></td><td>674.61 <b>(+364.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.10 (n/a)</td><td>413.90 (n/a)</td><td>457.90 (n/a)</td><td>233.80 (n/a)</td><td>145.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (-9.49%)</td><td>0.04 (-9.52%)</td><td>0.03 (-11.57%)</td><td>0.03 (+2.08%)</td><td>0.02 <b>(-22.19%)</b></td><td>526.80 (-2.05%)</td><td>416.20 (+5.88%)</td><td>490.60 (+13.07%)</td><td>246.30 (+10.45%)</td><td>130.06 (-13.28%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>537.80 (n/a)</td><td>393.10 (n/a)</td><td>433.90 (n/a)</td><td>223.00 (n/a)</td><td>149.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(-49.60%)</b></td><td>0.04 <b>(-24.21%)</b></td><td>0.04 (+5.98%)</td><td>0.03 (+11.95%)</td><td>0.00 <b>(-82.01%)</b></td><td>619.10 (-10.68%)</td><td>547.80 (+12.72%)</td><td>517.40 (-5.65%)</td><td>486.90 <b>(+98.41%)</b></td><td>64.51 <b>(-67.69%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>693.10 (n/a)</td><td>485.98 (n/a)</td><td>548.40 (n/a)</td><td>245.40 (n/a)</td><td>199.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 <b>(-40.87%)</b></td><td>0.03 <b>(-48.33%)</b></td><td>0.03 <b>(-49.31%)</b></td><td>0.01 <b>(-73.60%)</b></td><td>0.01 (-17.75%)</td><td>2054.10 <b>(+278.71%)</b></td><td>785.74 <b>(+155.26%)</b></td><td>529.20 <b>(+97.24%)</b></td><td>366.70 <b>(+69.14%)</b></td><td>714.26 <b>(+436.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.40 (n/a)</td><td>307.82 (n/a)</td><td>268.30 (n/a)</td><td>216.80 (n/a)</td><td>133.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (+2.86%)</td><td>0.05 (-1.24%)</td><td>0.04 <b>(-22.18%)</b></td><td>0.03 <b>(+254.64%)</b></td><td>0.02 <b>(-27.51%)</b></td><td>701.10 <b>(-71.80%)</b></td><td>461.98 <b>(-41.69%)</b></td><td>453.30 <b>(+28.49%)</b></td><td>241.00 (-2.78%)</td><td>182.01 <b>(-80.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2486.40 (n/a)</td><td>792.24 (n/a)</td><td>352.80 (n/a)</td><td>247.90 (n/a)</td><td>957.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (+12.41%)</td><td>0.04 (-16.69%)</td><td>0.03 <b>(-35.81%)</b></td><td>0.03 (-14.78%)</td><td>0.01 <b>(+58.89%)</b></td><td>561.30 (+17.35%)</td><td>474.72 <b>(+24.81%)</b></td><td>536.60 <b>(+55.76%)</b></td><td>284.40 (-11.01%)</td><td>114.82 <b>(+64.07%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.30 (n/a)</td><td>380.36 (n/a)</td><td>344.50 (n/a)</td><td>319.60 (n/a)</td><td>69.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(-33.32%)</b></td><td>0.04 (-16.78%)</td><td>0.04 <b>(-32.77%)</b></td><td>0.04 <b>(+100.11%)</b></td><td>0.01 <b>(-78.37%)</b></td><td>499.90 <b>(-50.02%)</b></td><td>430.62 (-9.86%)</td><td>437.20 <b>(+48.76%)</b></td><td>352.50 <b>(+50.00%)</b></td><td>52.93 <b>(-83.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1000.30 (n/a)</td><td>477.72 (n/a)</td><td>293.90 (n/a)</td><td>235.00 (n/a)</td><td>326.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 <b>(+73.92%)</b></td><td>0.05 <b>(+63.44%)</b></td><td>0.06 <b>(+90.16%)</b></td><td>0.03 <b>(+68.52%)</b></td><td>0.02 <b>(+96.57%)</b></td><td>604.10 <b>(-40.66%)</b></td><td>386.74 <b>(-37.36%)</b></td><td>295.00 <b>(-47.41%)</b></td><td>255.70 <b>(-42.50%)</b></td><td>150.89 <b>(-34.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1018.00 (n/a)</td><td>617.36 (n/a)</td><td>560.90 (n/a)</td><td>444.70 (n/a)</td><td>231.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (+5.49%)</td><td>0.10 (+13.21%)</td><td>0.11 (+18.46%)</td><td>0.06 (+10.44%)</td><td>0.03 (+13.30%)</td><td>523.40 (-9.46%)</td><td>370.42 (-11.23%)</td><td>309.20 (-15.59%)</td><td>271.50 (-5.20%)</td><td>117.07 (-5.99%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>578.10 (n/a)</td><td>417.26 (n/a)</td><td>366.30 (n/a)</td><td>286.40 (n/a)</td><td>124.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 <b>(+31.35%)</b></td><td>0.11 <b>(+22.23%)</b></td><td>0.12 <b>(+70.14%)</b></td><td>0.06 (-4.08%)</td><td>0.04 <b>(+52.70%)</b></td><td>530.60 (+4.26%)</td><td>357.66 (-12.49%)</td><td>282.10 <b>(-41.23%)</b></td><td>205.90 <b>(-23.85%)</b></td><td>152.20 <b>(+30.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>508.90 (n/a)</td><td>408.72 (n/a)</td><td>480.00 (n/a)</td><td>270.40 (n/a)</td><td>116.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 <b>(+37.96%)</b></td><td>0.14 <b>(+37.68%)</b></td><td>0.14 <b>(+68.84%)</b></td><td>0.08 (+1.89%)</td><td>0.06 <b>(+71.24%)</b></td><td>513.30 (-1.85%)</td><td>337.08 <b>(-21.33%)</b></td><td>284.50 <b>(-40.77%)</b></td><td>182.00 <b>(-27.52%)</b></td><td>144.21 <b>(+31.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>523.00 (n/a)</td><td>428.46 (n/a)</td><td>480.30 (n/a)</td><td>251.10 (n/a)</td><td>109.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 <b>(+36.07%)</b></td><td>0.07 (+4.35%)</td><td>0.06 (-4.97%)</td><td>0.05 (-8.98%)</td><td>0.02 <b>(+145.78%)</b></td><td>622.80 (+9.88%)</td><td>506.74 (+1.00%)</td><td>553.20 (+5.23%)</td><td>297.70 <b>(-26.51%)</b></td><td>124.74 <b>(+88.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>566.80 (n/a)</td><td>501.70 (n/a)</td><td>525.70 (n/a)</td><td>405.10 (n/a)</td><td>66.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.18 (+10.30%)</td><td>0.10 (+0.01%)</td><td>0.09 (-11.48%)</td><td>0.04 <b>(+84.79%)</b></td><td>0.06 (+5.14%)</td><td>1031.30 <b>(-45.89%)</b></td><td>538.20 (-19.56%)</td><td>452.30 (+12.96%)</td><td>228.40 (-9.33%)</td><td>327.32 <b>(-53.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1905.80 (n/a)</td><td>669.04 (n/a)</td><td>400.40 (n/a)</td><td>251.90 (n/a)</td><td>697.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (-17.03%)</td><td>0.09 (-11.47%)</td><td>0.10 (-14.45%)</td><td>0.06 (+13.63%)</td><td>0.03 (-18.26%)</td><td>592.00 (-12.00%)</td><td>411.10 (+8.94%)</td><td>333.40 (+16.90%)</td><td>257.80 <b>(+20.52%)</b></td><td>165.28 (-10.50%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>672.70 (n/a)</td><td>377.38 (n/a)</td><td>285.20 (n/a)</td><td>213.90 (n/a)</td><td>184.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (-14.68%)</td><td>0.09 (+0.26%)</td><td>0.07 (-0.16%)</td><td>0.07 (+10.62%)</td><td>0.03 <b>(-26.77%)</b></td><td>541.40 (-9.60%)</td><td>435.80 (-4.38%)</td><td>492.70 (+0.16%)</td><td>260.00 (+17.17%)</td><td>119.74 (-14.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>598.90 (n/a)</td><td>455.76 (n/a)</td><td>491.90 (n/a)</td><td>221.90 (n/a)</td><td>139.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (+17.74%)</td><td>0.11 <b>(+28.75%)</b></td><td>0.12 <b>(+68.84%)</b></td><td>0.06 (-6.86%)</td><td>0.04 <b>(+38.45%)</b></td><td>580.10 (+7.37%)</td><td>355.60 (-17.04%)</td><td>279.80 <b>(-40.77%)</b></td><td>203.40 (-15.07%)</td><td>159.84 <b>(+33.53%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>540.30 (n/a)</td><td>428.64 (n/a)</td><td>472.40 (n/a)</td><td>239.50 (n/a)</td><td>119.70 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-12.19%)</td><td>0.07 (-13.15%)</td><td>0.07 (-12.34%)</td><td>0.04 <b>(-41.03%)</b></td><td>0.02 (+19.72%)</td><td>965.80 <b>(+69.56%)</b></td><td>573.00 <b>(+22.99%)</b></td><td>532.70 (+14.07%)</td><td>370.00 (+13.88%)</td><td>230.15 <b>(+153.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>569.60 (n/a)</td><td>465.90 (n/a)</td><td>467.00 (n/a)</td><td>324.90 (n/a)</td><td>90.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (-5.93%)</td><td>0.08 (-14.36%)</td><td>0.06 <b>(-24.13%)</b></td><td>0.06 (-15.33%)</td><td>0.03 (+13.44%)</td><td>561.10 (+18.10%)</td><td>465.64 <b>(+20.43%)</b></td><td>537.90 <b>(+31.81%)</b></td><td>269.90 (+6.30%)</td><td>124.40 <b>(+49.45%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>475.10 (n/a)</td><td>386.66 (n/a)</td><td>408.10 (n/a)</td><td>253.90 (n/a)</td><td>83.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (+5.40%)</td><td>0.06 (+6.81%)</td><td>0.07 <b>(+40.55%)</b></td><td>0.04 (+2.66%)</td><td>0.02 (+7.40%)</td><td>477.20 (-2.59%)</td><td>353.02 (-5.47%)</td><td>294.20 <b>(-28.85%)</b></td><td>258.00 (-5.15%)</td><td>105.38 (+8.82%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>489.90 (n/a)</td><td>373.44 (n/a)</td><td>413.50 (n/a)</td><td>272.00 (n/a)</td><td>96.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (+6.96%)</td><td>0.05 (-11.44%)</td><td>0.04 <b>(-28.39%)</b></td><td>0.03 <b>(-34.44%)</b></td><td>0.03 <b>(+83.12%)</b></td><td>648.00 <b>(+52.54%)</b></td><td>445.20 <b>(+27.84%)</b></td><td>527.80 <b>(+39.63%)</b></td><td>242.80 (-6.51%)</td><td>182.05 <b>(+149.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>424.80 (n/a)</td><td>348.26 (n/a)</td><td>378.00 (n/a)</td><td>259.70 (n/a)</td><td>72.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (-3.77%)</td><td>0.06 (-10.34%)</td><td>0.06 (-18.23%)</td><td>0.04 (+12.73%)</td><td>0.02 (-10.04%)</td><td>492.00 (-11.30%)</td><td>366.52 (+8.82%)</td><td>365.90 <b>(+22.29%)</b></td><td>248.20 (+3.89%)</td><td>95.26 <b>(-23.52%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>336.82 (n/a)</td><td>299.20 (n/a)</td><td>238.90 (n/a)</td><td>124.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (-0.16%)</td><td>0.07 (+5.82%)</td><td>0.07 (-1.91%)</td><td>0.04 <b>(+93.09%)</b></td><td>0.02 <b>(-22.08%)</b></td><td>529.00 <b>(-48.22%)</b></td><td>344.18 <b>(-21.53%)</b></td><td>296.50 (+1.93%)</td><td>240.80 (+0.17%)</td><td>122.49 <b>(-62.87%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1021.60 (n/a)</td><td>438.64 (n/a)</td><td>290.90 (n/a)</td><td>240.40 (n/a)</td><td>329.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 <b>(+68.72%)</b></td><td>0.06 (-2.89%)</td><td>0.05 <b>(-31.95%)</b></td><td>0.04 (-4.34%)</td><td>0.04 <b>(+164.68%)</b></td><td>566.90 (+4.56%)</td><td>415.28 <b>(+21.37%)</b></td><td>450.00 <b>(+46.96%)</b></td><td>148.00 <b>(-40.73%)</b></td><td>162.27 <b>(+41.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>542.20 (n/a)</td><td>342.16 (n/a)</td><td>306.20 (n/a)</td><td>249.70 (n/a)</td><td>114.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 <b>(+35.02%)</b></td><td>0.05 (-2.84%)</td><td>0.04 (-19.98%)</td><td>0.04 <b>(+22.51%)</b></td><td>0.02 <b>(+49.94%)</b></td><td>552.00 (-18.37%)</td><td>447.04 (+5.09%)</td><td>486.90 <b>(+24.97%)</b></td><td>241.00 <b>(-25.94%)</b></td><td>126.33 (-12.92%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>676.20 (n/a)</td><td>425.38 (n/a)</td><td>389.60 (n/a)</td><td>325.40 (n/a)</td><td>145.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-10.67%)</td><td>0.06 (-9.76%)</td><td>0.06 <b>(-34.21%)</b></td><td>0.04 <b>(+215.15%)</b></td><td>0.02 <b>(-41.73%)</b></td><td>605.70 <b>(-68.27%)</b></td><td>438.40 <b>(-32.43%)</b></td><td>442.80 <b>(+52.01%)</b></td><td>249.20 (+11.95%)</td><td>131.78 <b>(-81.55%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1909.00 (n/a)</td><td>648.82 (n/a)</td><td>291.30 (n/a)</td><td>222.60 (n/a)</td><td>714.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-0.00%)</td><td>0.08 (+2.81%)</td><td>0.08 (+4.16%)</td><td>0.05 <b>(+20.11%)</b></td><td>0.02 (+6.68%)</td><td>459.20 (-16.74%)</td><td>338.92 (-3.06%)</td><td>293.70 (-4.02%)</td><td>245.10 (+0.00%)</td><td>107.30 (-12.18%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.50 (n/a)</td><td>349.62 (n/a)</td><td>306.00 (n/a)</td><td>245.10 (n/a)</td><td>122.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (+11.48%)</td><td>0.08 <b>(+48.90%)</b></td><td>0.08 <b>(+89.79%)</b></td><td>0.05 <b>(+24.32%)</b></td><td>0.02 (-3.93%)</td><td>544.80 (-19.56%)</td><td>355.64 <b>(-35.19%)</b></td><td>310.50 <b>(-47.31%)</b></td><td>233.60 (-10.29%)</td><td>124.26 <b>(-25.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>677.30 (n/a)</td><td>548.72 (n/a)</td><td>589.30 (n/a)</td><td>260.40 (n/a)</td><td>167.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (+15.31%)</td><td>0.09 <b>(+29.11%)</b></td><td>0.09 <b>(+69.97%)</b></td><td>0.05 <b>(+30.12%)</b></td><td>0.03 (-15.44%)</td><td>472.30 <b>(-23.15%)</b></td><td>296.88 <b>(-29.34%)</b></td><td>269.80 <b>(-41.18%)</b></td><td>185.20 (-13.30%)</td><td>107.67 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>614.60 (n/a)</td><td>420.18 (n/a)</td><td>458.70 (n/a)</td><td>213.60 (n/a)</td><td>183.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (-3.60%)</td><td>0.08 (+6.55%)</td><td>0.09 (+1.51%)</td><td>0.06 <b>(+24.81%)</b></td><td>0.02 <b>(-29.53%)</b></td><td>445.50 (-19.89%)</td><td>313.48 (-11.12%)</td><td>274.50 (-1.51%)</td><td>253.00 (+3.73%)</td><td>78.71 <b>(-40.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>556.10 (n/a)</td><td>352.72 (n/a)</td><td>278.70 (n/a)</td><td>243.90 (n/a)</td><td>132.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (-8.27%)</td><td>0.07 (-8.21%)</td><td>0.06 <b>(-22.97%)</b></td><td>0.06 (+18.72%)</td><td>0.02 <b>(-28.07%)</b></td><td>443.50 (-15.78%)</td><td>369.34 (+4.51%)</td><td>399.00 <b>(+29.84%)</b></td><td>259.30 (+9.00%)</td><td>75.47 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>526.60 (n/a)</td><td>353.40 (n/a)</td><td>307.30 (n/a)</td><td>237.90 (n/a)</td><td>116.65 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (+8.96%)</td><td>0.05 (+19.23%)</td><td>0.05 <b>(+20.82%)</b></td><td>0.03 <b>(+251.47%)</b></td><td>0.02 (-19.70%)</td><td>588.20 <b>(-71.55%)</b></td><td>399.56 <b>(-44.40%)</b></td><td>384.20 (-17.22%)</td><td>255.20 (-8.20%)</td><td>147.43 <b>(-80.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2067.20 (n/a)</td><td>718.62 (n/a)</td><td>464.10 (n/a)</td><td>278.00 (n/a)</td><td>760.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (+5.51%)</td><td>0.04 (-10.19%)</td><td>0.04 (-10.90%)</td><td>0.03 (-11.23%)</td><td>0.01 <b>(+22.92%)</b></td><td>533.30 (+12.65%)</td><td>452.88 (+13.28%)</td><td>481.40 (+12.24%)</td><td>292.70 (-5.21%)</td><td>97.51 <b>(+29.14%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>473.40 (n/a)</td><td>399.78 (n/a)</td><td>428.90 (n/a)</td><td>308.80 (n/a)</td><td>75.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (+7.50%)</td><td>0.07 (+6.75%)</td><td>0.08 (+4.75%)</td><td>0.04 (+19.42%)</td><td>0.02 (-0.60%)</td><td>490.90 (-16.26%)</td><td>292.28 (-8.98%)</td><td>233.80 (-4.53%)</td><td>200.40 (-6.96%)</td><td>117.20 <b>(-23.21%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.20 (n/a)</td><td>321.12 (n/a)</td><td>244.90 (n/a)</td><td>215.40 (n/a)</td><td>152.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (+14.31%)</td><td>0.05 (+16.50%)</td><td>0.05 (+15.84%)</td><td>0.04 <b>(+20.88%)</b></td><td>0.02 (+8.55%)</td><td>461.80 (-17.28%)</td><td>364.28 (-15.20%)</td><td>396.50 (-13.67%)</td><td>239.70 (-12.52%)</td><td>104.05 <b>(-21.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>558.30 (n/a)</td><td>429.56 (n/a)</td><td>459.30 (n/a)</td><td>274.00 (n/a)</td><td>132.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 <b>(-41.69%)</b></td><td>0.04 <b>(-22.09%)</b></td><td>0.04 (+15.31%)</td><td>0.03 (+15.37%)</td><td>0.01 <b>(-67.91%)</b></td><td>673.30 (-13.32%)</td><td>502.96 (+3.73%)</td><td>463.10 (-13.28%)</td><td>361.60 <b>(+71.46%)</b></td><td>123.39 <b>(-49.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>776.80 (n/a)</td><td>484.88 (n/a)</td><td>534.00 (n/a)</td><td>210.90 (n/a)</td><td>246.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 <b>(-30.47%)</b></td><td>0.04 (-19.41%)</td><td>0.04 (-3.13%)</td><td>0.01 <b>(-70.39%)</b></td><td>0.02 (-7.29%)</td><td>1894.40 <b>(+237.74%)</b></td><td>705.36 <b>(+70.73%)</b></td><td>491.10 (+3.22%)</td><td>290.00 <b>(+43.85%)</b></td><td>674.77 <b>(+367.56%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>560.90 (n/a)</td><td>413.14 (n/a)</td><td>475.80 (n/a)</td><td>201.60 (n/a)</td><td>144.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.43 (+19.89%)</td><td>0.37 <b>(+22.98%)</b></td><td>0.39 (+15.65%)</td><td>0.31 <b>(+45.66%)</b></td><td>0.05 (-19.65%)</td><td>320.70 <b>(-31.34%)</b></td><td>272.36 <b>(-21.00%)</b></td><td>254.80 (-13.54%)</td><td>227.30 (-16.59%)</td><td>41.74 <b>(-52.31%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>467.10 (n/a)</td><td>344.76 (n/a)</td><td>294.70 (n/a)</td><td>272.50 (n/a)</td><td>87.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.35 (-6.97%)</td><td>0.23 (-16.30%)</td><td>0.21 <b>(-39.54%)</b></td><td>0.16 (+13.89%)</td><td>0.07 <b>(-38.78%)</b></td><td>598.60 (-12.20%)</td><td>448.86 (+6.81%)</td><td>458.70 <b>(+65.42%)</b></td><td>283.10 (+7.48%)</td><td>118.71 <b>(-42.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.35 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>681.80 (n/a)</td><td>420.24 (n/a)</td><td>277.30 (n/a)</td><td>263.40 (n/a)</td><td>206.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.40 (-7.61%)</td><td>0.28 (-12.79%)</td><td>0.37 (+3.36%)</td><td>0.08 <b>(-63.85%)</b></td><td>0.14 <b>(+39.04%)</b></td><td>1306.70 <b>(+176.67%)</b></td><td>518.30 <b>(+55.24%)</b></td><td>268.50 (-3.24%)</td><td>248.20 (+8.24%)</td><td>452.91 <b>(+298.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>472.30 (n/a)</td><td>333.86 (n/a)</td><td>277.50 (n/a)</td><td>229.30 (n/a)</td><td>113.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.29 <b>(+24.69%)</b></td><td>0.20 (+3.63%)</td><td>0.19 (-12.11%)</td><td>0.11 <b>(-25.62%)</b></td><td>0.07 <b>(+77.47%)</b></td><td>675.30 <b>(+34.44%)</b></td><td>410.42 (+4.20%)</td><td>385.40 (+13.79%)</td><td>255.70 (-19.79%)</td><td>164.85 <b>(+90.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>502.30 (n/a)</td><td>393.86 (n/a)</td><td>338.70 (n/a)</td><td>318.80 (n/a)</td><td>86.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.26 (-18.81%)</td><td>0.15 <b>(-35.42%)</b></td><td>0.14 <b>(-47.99%)</b></td><td>0.07 <b>(-53.24%)</b></td><td>0.07 (-7.54%)</td><td>1110.80 <b>(+113.86%)</b></td><td>594.04 <b>(+70.17%)</b></td><td>536.50 <b>(+92.29%)</b></td><td>279.50 <b>(+23.18%)</b></td><td>312.07 <b>(+142.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>519.40 (n/a)</td><td>349.08 (n/a)</td><td>279.00 (n/a)</td><td>226.90 (n/a)</td><td>128.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.31 <b>(+47.51%)</b></td><td>0.19 <b>(+29.86%)</b></td><td>0.16 <b>(+21.14%)</b></td><td>0.13 <b>(+32.72%)</b></td><td>0.07 <b>(+74.79%)</b></td><td>586.30 <b>(-24.65%)</b></td><td>435.76 <b>(-20.53%)</b></td><td>449.60 (-17.44%)</td><td>239.40 <b>(-32.22%)</b></td><td>131.00 (-13.48%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>778.10 (n/a)</td><td>548.30 (n/a)</td><td>544.60 (n/a)</td><td>353.20 (n/a)</td><td>151.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 <b>(+24.66%)</b></td><td>0.11 <b>(+35.63%)</b></td><td>0.12 <b>(+55.24%)</b></td><td>0.07 (-1.54%)</td><td>0.05 <b>(+82.06%)</b></td><td>559.50 (+1.58%)</td><td>373.16 (-19.22%)</td><td>316.70 <b>(-35.59%)</b></td><td>229.90 (-19.76%)</td><td>159.51 <b>(+56.71%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>550.80 (n/a)</td><td>461.96 (n/a)</td><td>491.70 (n/a)</td><td>286.50 (n/a)</td><td>101.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 <b>(+58.41%)</b></td><td>0.13 <b>(+20.03%)</b></td><td>0.13 (+10.76%)</td><td>0.08 <b>(+22.98%)</b></td><td>0.05 <b>(+93.75%)</b></td><td>452.10 (-18.69%)</td><td>326.68 (-11.93%)</td><td>291.10 (-9.71%)</td><td>182.90 <b>(-36.89%)</b></td><td>117.43 (+5.80%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>556.00 (n/a)</td><td>370.92 (n/a)</td><td>322.40 (n/a)</td><td>289.80 (n/a)</td><td>110.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 <b>(+51.66%)</b></td><td>0.09 <b>(+46.59%)</b></td><td>0.08 <b>(+25.92%)</b></td><td>0.06 <b>(+78.71%)</b></td><td>0.03 <b>(+60.97%)</b></td><td>599.90 <b>(-44.04%)</b></td><td>428.10 <b>(-32.44%)</b></td><td>455.30 <b>(-20.58%)</b></td><td>271.00 <b>(-34.06%)</b></td><td>140.37 <b>(-45.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>1072.10 (n/a)</td><td>633.66 (n/a)</td><td>573.30 (n/a)</td><td>411.00 (n/a)</td><td>257.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 <b>(+21.32%)</b></td><td>0.09 (+12.27%)</td><td>0.08 (+4.37%)</td><td>0.02 <b>(-69.75%)</b></td><td>0.06 <b>(+124.22%)</b></td><td>1874.70 <b>(+230.63%)</b></td><td>672.86 <b>(+45.07%)</b></td><td>474.40 (-4.20%)</td><td>236.80 (-17.58%)</td><td>685.38 <b>(+496.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>567.00 (n/a)</td><td>463.82 (n/a)</td><td>495.20 (n/a)</td><td>287.30 (n/a)</td><td>114.90 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 <b>(+26.36%)</b></td><td>0.08 <b>(+26.56%)</b></td><td>0.08 <b>(+27.26%)</b></td><td>0.02 <b>(-32.02%)</b></td><td>0.04 <b>(+42.97%)</b></td><td>1943.40 <b>(+47.10%)</b></td><td>698.08 (+1.95%)</td><td>443.80 <b>(-21.41%)</b></td><td>279.80 <b>(-20.87%)</b></td><td>702.10 <b>(+80.18%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1321.10 (n/a)</td><td>684.76 (n/a)</td><td>564.70 (n/a)</td><td>353.60 (n/a)</td><td>389.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (-3.82%)</td><td>0.08 <b>(-34.80%)</b></td><td>0.06 <b>(-50.35%)</b></td><td>0.06 <b>(-42.18%)</b></td><td>0.04 <b>(+71.80%)</b></td><td>656.80 <b>(+72.98%)</b></td><td>513.14 <b>(+71.57%)</b></td><td>599.50 <b>(+101.38%)</b></td><td>246.10 (+3.97%)</td><td>178.53 <b>(+216.93%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>379.70 (n/a)</td><td>299.08 (n/a)</td><td>297.70 (n/a)</td><td>236.70 (n/a)</td><td>56.33 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 <b>(+23.35%)</b></td><td>0.15 <b>(+34.95%)</b></td><td>0.16 <b>(+99.72%)</b></td><td>0.08 (+10.17%)</td><td>0.04 (+8.99%)</td><td>484.70 (-9.23%)</td><td>306.94 <b>(-26.98%)</b></td><td>251.40 <b>(-49.92%)</b></td><td>205.10 (-18.93%)</td><td>111.58 (-19.66%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>534.00 (n/a)</td><td>420.36 (n/a)</td><td>502.00 (n/a)</td><td>253.00 (n/a)</td><td>138.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (+6.00%)</td><td>0.15 <b>(+20.35%)</b></td><td>0.16 (+18.33%)</td><td>0.10 <b>(+34.58%)</b></td><td>0.03 <b>(-30.20%)</b></td><td>401.90 <b>(-25.68%)</b></td><td>286.88 <b>(-21.29%)</b></td><td>258.50 (-15.50%)</td><td>245.00 (-5.66%)</td><td>64.95 <b>(-48.20%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>540.80 (n/a)</td><td>364.48 (n/a)</td><td>305.90 (n/a)</td><td>259.70 (n/a)</td><td>125.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (+6.26%)</td><td>0.13 <b>(+52.05%)</b></td><td>0.14 <b>(+74.41%)</b></td><td>0.09 <b>(+446.49%)</b></td><td>0.03 <b>(-32.28%)</b></td><td>446.80 <b>(-81.70%)</b></td><td>340.94 <b>(-59.54%)</b></td><td>282.90 <b>(-42.67%)</b></td><td>256.20 (-5.91%)</td><td>95.94 <b>(-89.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2441.60 (n/a)</td><td>842.68 (n/a)</td><td>493.50 (n/a)</td><td>272.30 (n/a)</td><td>901.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 <b>(+35.77%)</b></td><td>0.11 (+17.34%)</td><td>0.10 (+6.62%)</td><td>0.07 (-8.76%)</td><td>0.04 <b>(+116.83%)</b></td><td>581.60 (+9.61%)</td><td>398.64 (-8.00%)</td><td>410.30 (-6.20%)</td><td>247.10 <b>(-26.35%)</b></td><td>141.51 <b>(+68.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>530.60 (n/a)</td><td>433.32 (n/a)</td><td>437.40 (n/a)</td><td>335.50 (n/a)</td><td>83.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 <b>(+41.28%)</b></td><td>0.09 (-6.30%)</td><td>0.08 <b>(-21.70%)</b></td><td>0.07 (-14.91%)</td><td>0.04 <b>(+239.14%)</b></td><td>567.30 (+17.53%)</td><td>483.26 (+16.49%)</td><td>530.20 <b>(+27.70%)</b></td><td>247.90 <b>(-29.21%)</b></td><td>132.63 <b>(+172.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>482.70 (n/a)</td><td>414.84 (n/a)</td><td>415.20 (n/a)</td><td>350.20 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 <b>(-25.52%)</b></td><td>0.12 (-19.56%)</td><td>0.12 (-18.87%)</td><td>0.07 (-0.25%)</td><td>0.04 <b>(-22.60%)</b></td><td>569.50 (+0.26%)</td><td>391.46 <b>(+21.58%)</b></td><td>353.00 <b>(+23.25%)</b></td><td>244.00 <b>(+34.21%)</b></td><td>145.79 (+0.26%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>568.00 (n/a)</td><td>321.98 (n/a)</td><td>286.40 (n/a)</td><td>181.80 (n/a)</td><td>145.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (+10.41%)</td><td>0.12 <b>(+52.33%)</b></td><td>0.13 <b>(+99.91%)</b></td><td>0.07 <b>(+21.23%)</b></td><td>0.03 (+3.89%)</td><td>501.60 (-17.51%)</td><td>305.46 <b>(-35.23%)</b></td><td>258.50 <b>(-49.98%)</b></td><td>247.80 (-9.43%)</td><td>110.03 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>608.10 (n/a)</td><td>471.58 (n/a)</td><td>516.80 (n/a)</td><td>273.60 (n/a)</td><td>138.52 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (+6.10%)</td><td>0.08 (-18.45%)</td><td>0.07 (-15.66%)</td><td>0.03 <b>(-44.15%)</b></td><td>0.04 <b>(+22.16%)</b></td><td>1022.60 <b>(+79.06%)</b></td><td>577.22 <b>(+38.16%)</b></td><td>516.40 (+18.58%)</td><td>241.10 (-5.75%)</td><td>294.33 <b>(+103.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.10 (n/a)</td><td>417.80 (n/a)</td><td>435.50 (n/a)</td><td>255.80 (n/a)</td><td>144.78 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (-18.25%)</td><td>0.11 (+2.65%)</td><td>0.12 (+1.13%)</td><td>0.07 (+18.24%)</td><td>0.03 <b>(-42.37%)</b></td><td>499.70 (-15.43%)</td><td>339.30 (-12.95%)</td><td>296.90 (-1.13%)</td><td>264.70 <b>(+22.32%)</b></td><td>98.21 <b>(-45.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>590.90 (n/a)</td><td>389.78 (n/a)</td><td>300.30 (n/a)</td><td>216.40 (n/a)</td><td>180.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (+18.06%)</td><td>0.09 (+16.54%)</td><td>0.07 (+7.84%)</td><td>0.06 (-1.53%)</td><td>0.04 <b>(+36.86%)</b></td><td>579.30 (+1.56%)</td><td>423.28 (-9.94%)</td><td>489.40 (-7.28%)</td><td>223.50 (-15.28%)</td><td>153.93 (+17.72%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>570.40 (n/a)</td><td>470.02 (n/a)</td><td>527.80 (n/a)</td><td>263.80 (n/a)</td><td>130.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 <b>(+45.13%)</b></td><td>0.11 (+10.46%)</td><td>0.14 <b>(+23.99%)</b></td><td>0.05 <b>(-29.00%)</b></td><td>0.05 <b>(+205.49%)</b></td><td>635.20 <b>(+40.84%)</b></td><td>373.32 (+8.37%)</td><td>249.30 (-19.35%)</td><td>203.40 <b>(-31.10%)</b></td><td>196.06 <b>(+203.95%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>451.00 (n/a)</td><td>344.48 (n/a)</td><td>309.10 (n/a)</td><td>295.20 (n/a)</td><td>64.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (-2.51%)</td><td>0.11 (+19.44%)</td><td>0.13 <b>(+59.80%)</b></td><td>0.07 <b>(+66.21%)</b></td><td>0.03 <b>(-21.17%)</b></td><td>484.40 <b>(-39.84%)</b></td><td>349.14 <b>(-24.66%)</b></td><td>278.10 <b>(-37.42%)</b></td><td>244.50 (+2.56%)</td><td>121.38 <b>(-47.23%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>805.20 (n/a)</td><td>463.40 (n/a)</td><td>444.40 (n/a)</td><td>238.40 (n/a)</td><td>230.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.50 <b>(+82.42%)</b></td><td>0.29 <b>(+55.05%)</b></td><td>0.24 (+9.14%)</td><td>0.17 <b>(+149.33%)</b></td><td>0.13 <b>(+57.91%)</b></td><td>787.70 <b>(-59.89%)</b></td><td>528.76 <b>(-42.44%)</b></td><td>550.70 (-8.38%)</td><td>264.30 <b>(-45.19%)</b></td><td>202.73 <b>(-67.04%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1964.00 (n/a)</td><td>918.58 (n/a)</td><td>601.10 (n/a)</td><td>482.20 (n/a)</td><td>615.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.45 (-14.41%)</td><td>0.32 (+6.03%)</td><td>0.36 <b>(+43.78%)</b></td><td>0.16 <b>(-28.52%)</b></td><td>0.11 (-9.62%)</td><td>811.00 <b>(+39.90%)</b></td><td>469.06 (-2.21%)</td><td>359.80 <b>(-30.45%)</b></td><td>292.70 (+16.85%)</td><td>210.27 <b>(+60.72%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.52 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>579.70 (n/a)</td><td>479.64 (n/a)</td><td>517.30 (n/a)</td><td>250.50 (n/a)</td><td>130.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.40 (-17.34%)</td><td>0.31 (+13.51%)</td><td>0.27 (+9.40%)</td><td>0.22 <b>(+33.85%)</b></td><td>0.08 <b>(-37.15%)</b></td><td>582.90 <b>(-25.30%)</b></td><td>446.44 (-18.62%)</td><td>480.90 (-8.59%)</td><td>331.60 <b>(+20.98%)</b></td><td>108.13 <b>(-44.03%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>780.30 (n/a)</td><td>548.62 (n/a)</td><td>526.10 (n/a)</td><td>274.10 (n/a)</td><td>193.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+6.21%)</td><td>0.01 (+15.01%)</td><td>0.01 (+11.08%)</td><td>0.01 <b>(+23.86%)</b></td><td>0.00 <b>(-28.84%)</b></td><td>437.20 (-19.26%)</td><td>306.00 (-18.97%)</td><td>287.70 (-9.98%)</td><td>231.00 (-5.87%)</td><td>79.40 <b>(-45.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.50 (n/a)</td><td>377.62 (n/a)</td><td>319.60 (n/a)</td><td>245.40 (n/a)</td><td>146.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(-20.87%)</b></td><td>0.01 (-16.17%)</td><td>0.01 (-1.14%)</td><td>0.01 (-13.98%)</td><td>0.00 (-4.99%)</td><td>457.70 (+16.26%)</td><td>347.34 <b>(+21.39%)</b></td><td>295.10 (+1.13%)</td><td>260.50 <b>(+26.39%)</b></td><td>100.71 <b>(+43.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>393.70 (n/a)</td><td>286.14 (n/a)</td><td>291.80 (n/a)</td><td>206.10 (n/a)</td><td>70.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (+2.15%)</td><td>0.01 (-1.09%)</td><td>0.01 <b>(-22.41%)</b></td><td>0.01 (-6.88%)</td><td>0.00 <b>(+23.53%)</b></td><td>483.00 (+7.38%)</td><td>358.42 (+3.43%)</td><td>385.90 <b>(+28.89%)</b></td><td>246.40 (-2.11%)</td><td>105.95 (+16.91%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.80 (n/a)</td><td>346.54 (n/a)</td><td>299.40 (n/a)</td><td>251.70 (n/a)</td><td>90.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.99 <b>(-20.62%)</b></td><td>6.23 (-3.04%)</td><td>6.65 <b>(+35.38%)</b></td><td>4.04 (-1.37%)</td><td>1.50 <b>(-43.32%)</b></td><td>519.80 (+1.38%)</td><td>355.88 (-3.84%)</td><td>315.50 <b>(-26.13%)</b></td><td>262.70 <b>(+26.00%)</b></td><td>100.70 <b>(-24.55%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>10.06 (n/a)</td><td>6.42 (n/a)</td><td>4.91 (n/a)</td><td>4.09 (n/a)</td><td>2.65 (n/a)</td><td>512.70 (n/a)</td><td>370.08 (n/a)</td><td>427.10 (n/a)</td><td>208.50 (n/a)</td><td>133.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.57 (+7.42%)</td><td>0.42 (+2.19%)</td><td>0.44 (+4.43%)</td><td>0.28 (+2.46%)</td><td>0.13 (+9.82%)</td><td>478.80 (-2.41%)</td><td>342.94 (-1.25%)</td><td>296.90 (-4.23%)</td><td>232.10 (-6.94%)</td><td>108.80 (+3.70%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>490.60 (n/a)</td><td>347.28 (n/a)</td><td>310.00 (n/a)</td><td>249.40 (n/a)</td><td>104.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.52 (-0.38%)</td><td>0.40 (+13.80%)</td><td>0.37 <b>(+30.48%)</b></td><td>0.26 (+4.99%)</td><td>0.11 (-8.65%)</td><td>516.20 (-4.74%)</td><td>352.52 (-13.80%)</td><td>355.60 <b>(-23.36%)</b></td><td>256.30 (+0.39%)</td><td>105.81 (-14.88%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.52 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>541.90 (n/a)</td><td>408.94 (n/a)</td><td>464.00 (n/a)</td><td>255.30 (n/a)</td><td>124.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.48 (-5.05%)</td><td>0.40 (+16.77%)</td><td>0.44 <b>(+59.15%)</b></td><td>0.25 (+12.05%)</td><td>0.09 <b>(-26.37%)</b></td><td>535.10 (-10.76%)</td><td>350.24 (-18.00%)</td><td>301.20 <b>(-37.17%)</b></td><td>274.80 (+5.33%)</td><td>105.97 <b>(-25.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.51 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>599.60 (n/a)</td><td>427.12 (n/a)</td><td>479.40 (n/a)</td><td>260.90 (n/a)</td><td>142.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.56 (-0.89%)</td><td>0.45 (+5.80%)</td><td>0.46 (+2.68%)</td><td>0.35 <b>(+41.85%)</b></td><td>0.07 <b>(-36.93%)</b></td><td>372.30 <b>(-29.52%)</b></td><td>297.36 (-10.60%)</td><td>285.20 (-2.60%)</td><td>237.40 (+0.89%)</td><td>50.46 <b>(-56.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.56 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>528.20 (n/a)</td><td>332.62 (n/a)</td><td>292.80 (n/a)</td><td>235.30 (n/a)</td><td>115.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.60 (+8.47%)</td><td>0.50 (+13.95%)</td><td>0.47 (+4.84%)</td><td>0.46 <b>(+70.00%)</b></td><td>0.06 <b>(-48.18%)</b></td><td>289.20 <b>(-41.17%)</b></td><td>265.46 (-17.13%)</td><td>278.70 (-4.62%)</td><td>221.00 (-7.80%)</td><td>28.97 <b>(-71.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>491.60 (n/a)</td><td>320.34 (n/a)</td><td>292.20 (n/a)</td><td>239.70 (n/a)</td><td>102.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (-5.52%)</td><td>0.01 (-5.03%)</td><td>0.01 (-5.73%)</td><td>0.01 (-8.55%)</td><td>0.00 (-16.18%)</td><td>524.90 (+9.33%)</td><td>356.94 (+3.35%)</td><td>306.10 (+6.10%)</td><td>251.60 (+5.85%)</td><td>111.82 (-5.39%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.10 (n/a)</td><td>345.36 (n/a)</td><td>288.50 (n/a)</td><td>237.70 (n/a)</td><td>118.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 <b>(+20.69%)</b></td><td>0.01 <b>(+31.65%)</b></td><td>0.01 <b>(+72.70%)</b></td><td>0.01 (+7.99%)</td><td>0.01 (+1.60%)</td><td>567.50 (-7.41%)</td><td>316.64 <b>(-25.65%)</b></td><td>285.40 <b>(-42.09%)</b></td><td>194.70 (-17.15%)</td><td>145.71 (-13.22%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>612.90 (n/a)</td><td>425.90 (n/a)</td><td>492.80 (n/a)</td><td>235.00 (n/a)</td><td>167.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 (+18.75%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+127.30%)</b></td><td>21437.51 (+19.19%)</td><td>14984.85 (+5.51%)</td><td>19977.22 <b>(+25.74%)</b></td><td>5759.07 <b>(-24.56%)</b></td><td>8114.46 <b>(+102.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17985.96 (n/a)</td><td>14201.71 (n/a)</td><td>15887.83 (n/a)</td><td>7633.89 (n/a)</td><td>4005.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+57.14%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+67.62%)</b></td><td>19864.31 (-3.24%)</td><td>11760.23 <b>(-29.23%)</b></td><td>8245.53 <b>(-52.17%)</b></td><td>6004.96 <b>(-26.46%)</b></td><td>6411.73 <b>(+27.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20530.42 (n/a)</td><td>16616.43 (n/a)</td><td>17241.04 (n/a)</td><td>8165.72 (n/a)</td><td>5031.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (-2.39%)</td><td>0.09 (-13.94%)</td><td>0.07 (-13.96%)</td><td>0.07 (-5.69%)</td><td>0.03 (-12.18%)</td><td>30120.34 (+5.94%)</td><td>25110.88 (+14.93%)</td><td>28116.72 (+16.20%)</td><td>15105.13 (+2.43%)</td><td>6314.17 (-1.65%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28430.84 (n/a)</td><td>21848.04 (n/a)</td><td>24195.90 (n/a)</td><td>14747.17 (n/a)</td><td>6419.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.59 (-4.29%)</td><td>1.87 (+1.06%)</td><td>2.28 (-4.14%)</td><td>0.53 <b>(+77.57%)</b></td><td>0.84 (-19.56%)</td><td>1979.20 <b>(-43.68%)</b></td><td>791.10 <b>(-29.22%)</b></td><td>459.60 (+4.31%)</td><td>404.10 (+4.47%)</td><td>672.28 <b>(-50.32%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.71 (n/a)</td><td>1.85 (n/a)</td><td>2.38 (n/a)</td><td>0.30 (n/a)</td><td>1.05 (n/a)</td><td>3514.50 (n/a)</td><td>1117.64 (n/a)</td><td>440.60 (n/a)</td><td>386.80 (n/a)</td><td>1353.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.49 (+16.99%)</td><td>1.43 (-5.58%)</td><td>1.14 <b>(-37.11%)</b></td><td>0.30 (-8.02%)</td><td>1.27 (+18.93%)</td><td>3474.90 (+8.72%)</td><td>1449.84 (+13.42%)</td><td>921.10 <b>(+59.00%)</b></td><td>300.60 (-14.53%)</td><td>1286.29 (+7.74%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.98 (n/a)</td><td>1.52 (n/a)</td><td>1.81 (n/a)</td><td>0.33 (n/a)</td><td>1.07 (n/a)</td><td>3196.20 (n/a)</td><td>1278.26 (n/a)</td><td>579.30 (n/a)</td><td>351.70 (n/a)</td><td>1193.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.33 (+6.85%)</td><td>2.62 <b>(+75.97%)</b></td><td>2.51 <b>(+75.85%)</b></td><td>2.13 <b>(+600.16%)</b></td><td>0.48 <b>(-52.94%)</b></td><td>492.30 <b>(-85.72%)</b></td><td>409.68 <b>(-66.62%)</b></td><td>418.30 <b>(-43.13%)</b></td><td>315.20 (-6.41%)</td><td>70.63 <b>(-94.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.11 (n/a)</td><td>1.49 (n/a)</td><td>1.43 (n/a)</td><td>0.30 (n/a)</td><td>1.02 (n/a)</td><td>3447.00 (n/a)</td><td>1227.48 (n/a)</td><td>735.60 (n/a)</td><td>336.80 (n/a)</td><td>1257.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.44 <b>(-34.58%)</b></td><td>2.27 (-7.12%)</td><td>2.37 (-2.51%)</td><td>2.00 (+19.40%)</td><td>0.19 <b>(-77.80%)</b></td><td>524.60 (-16.25%)</td><td>464.82 (-0.74%)</td><td>441.90 (+2.58%)</td><td>429.70 <b>(+52.86%)</b></td><td>39.90 <b>(-72.76%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>3.73 (n/a)</td><td>2.44 (n/a)</td><td>2.43 (n/a)</td><td>1.67 (n/a)</td><td>0.84 (n/a)</td><td>626.40 (n/a)</td><td>468.28 (n/a)</td><td>430.80 (n/a)</td><td>281.10 (n/a)</td><td>146.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.78 <b>(-35.72%)</b></td><td>1.58 (-11.13%)</td><td>1.67 <b>(+73.02%)</b></td><td>0.59 (-0.91%)</td><td>0.99 <b>(-38.40%)</b></td><td>3557.60 (+0.92%)</td><td>2006.92 (-4.18%)</td><td>1257.20 <b>(-42.20%)</b></td><td>753.20 <b>(+55.59%)</b></td><td>1424.41 (+1.35%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>4.33 (n/a)</td><td>1.78 (n/a)</td><td>0.96 (n/a)</td><td>0.59 (n/a)</td><td>1.61 (n/a)</td><td>3525.20 (n/a)</td><td>2094.38 (n/a)</td><td>2175.20 (n/a)</td><td>484.10 (n/a)</td><td>1405.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.34 (+6.47%)</td><td>3.21 (-0.27%)</td><td>3.50 (-7.73%)</td><td>0.59 (-1.51%)</td><td>1.71 (+0.57%)</td><td>3538.60 (+1.53%)</td><td>1161.32 (+0.56%)</td><td>599.30 (+8.37%)</td><td>392.80 (-6.07%)</td><td>1333.51 (+1.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.01 (n/a)</td><td>3.22 (n/a)</td><td>3.79 (n/a)</td><td>0.60 (n/a)</td><td>1.70 (n/a)</td><td>3485.20 (n/a)</td><td>1154.86 (n/a)</td><td>553.00 (n/a)</td><td>418.20 (n/a)</td><td>1310.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.03 <b>(-31.31%)</b></td><td>2.35 <b>(-30.56%)</b></td><td>2.39 (-15.55%)</td><td>0.63 <b>(-36.48%)</b></td><td>1.21 <b>(-41.25%)</b></td><td>3309.60 <b>(+57.44%)</b></td><td>1299.10 <b>(+41.16%)</b></td><td>876.50 (+18.41%)</td><td>520.90 <b>(+45.58%)</b></td><td>1136.06 <b>(+60.12%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.86 (n/a)</td><td>3.39 (n/a)</td><td>2.83 (n/a)</td><td>1.00 (n/a)</td><td>2.05 (n/a)</td><td>2102.10 (n/a)</td><td>920.28 (n/a)</td><td>740.20 (n/a)</td><td>357.80 (n/a)</td><td>709.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.95 (-10.88%)</td><td>3.16 (-17.78%)</td><td>4.00 (-17.15%)</td><td>0.85 <b>(+45.19%)</b></td><td>2.22 (-11.80%)</td><td>2463.50 <b>(-31.12%)</b></td><td>1235.36 (+5.75%)</td><td>524.60 <b>(+20.71%)</b></td><td>352.80 (+12.21%)</td><td>1061.46 <b>(-23.31%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.67 (n/a)</td><td>3.84 (n/a)</td><td>4.83 (n/a)</td><td>0.59 (n/a)</td><td>2.52 (n/a)</td><td>3576.70 (n/a)</td><td>1168.18 (n/a)</td><td>434.60 (n/a)</td><td>314.40 (n/a)</td><td>1384.10 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.32 (-12.74%)</td><td>3.59 (+2.67%)</td><td>3.66 (+9.71%)</td><td>2.14 <b>(+255.21%)</b></td><td>1.18 <b>(-43.16%)</b></td><td>978.80 <b>(-71.85%)</b></td><td>640.24 <b>(-43.52%)</b></td><td>573.70 (-8.84%)</td><td>394.50 (+14.61%)</td><td>220.48 <b>(-83.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>6.09 (n/a)</td><td>3.49 (n/a)</td><td>3.33 (n/a)</td><td>0.60 (n/a)</td><td>2.08 (n/a)</td><td>3476.80 (n/a)</td><td>1133.56 (n/a)</td><td>629.30 (n/a)</td><td>344.20 (n/a)</td><td>1320.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.18 (+3.27%)</td><td>3.20 (+14.85%)</td><td>3.20 (+13.35%)</td><td>0.58 (+0.19%)</td><td>1.83 (-10.35%)</td><td>3587.40 (-0.19%)</td><td>1193.28 <b>(-20.58%)</b></td><td>655.00 (-11.78%)</td><td>404.70 (-3.18%)</td><td>1350.71 (-3.68%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.02 (n/a)</td><td>2.79 (n/a)</td><td>2.82 (n/a)</td><td>0.58 (n/a)</td><td>2.04 (n/a)</td><td>3594.10 (n/a)</td><td>1502.50 (n/a)</td><td>742.50 (n/a)</td><td>418.00 (n/a)</td><td>1402.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.03 (-6.56%)</td><td>4.03 (-17.36%)</td><td>4.00 (-18.98%)</td><td>3.36 (-16.67%)</td><td>0.63 <b>(+22.09%)</b></td><td>1249.20 <b>(+20.00%)</b></td><td>1059.20 <b>(+22.03%)</b></td><td>1047.60 <b>(+23.44%)</b></td><td>834.00 (+7.03%)</td><td>155.40 <b>(+52.14%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>5.38 (n/a)</td><td>4.88 (n/a)</td><td>4.94 (n/a)</td><td>4.03 (n/a)</td><td>0.52 (n/a)</td><td>1041.00 (n/a)</td><td>867.98 (n/a)</td><td>848.70 (n/a)</td><td>779.20 (n/a)</td><td>102.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.94 (+4.89%)</td><td>2.86 <b>(-40.65%)</b></td><td>1.72 <b>(-60.28%)</b></td><td>1.17 <b>(-30.36%)</b></td><td>2.87 <b>(+23.51%)</b></td><td>3584.70 <b>(+43.60%)</b></td><td>2367.68 <b>(+107.03%)</b></td><td>2433.30 <b>(+151.74%)</b></td><td>528.20 (-4.66%)</td><td>1254.42 <b>(+59.52%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>7.57 (n/a)</td><td>4.83 (n/a)</td><td>4.34 (n/a)</td><td>1.68 (n/a)</td><td>2.33 (n/a)</td><td>2496.30 (n/a)</td><td>1143.62 (n/a)</td><td>966.60 (n/a)</td><td>554.00 (n/a)</td><td>786.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.79 (-8.56%)</td><td>4.47 (-15.80%)</td><td>5.77 <b>(+42.03%)</b></td><td>1.23 <b>(-67.62%)</b></td><td>2.86 <b>(+39.48%)</b></td><td>3396.80 <b>(+208.86%)</b></td><td>1566.88 <b>(+79.45%)</b></td><td>726.40 <b>(-29.59%)</b></td><td>538.30 (+9.37%)</td><td>1286.64 <b>(+371.20%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>8.52 (n/a)</td><td>5.31 (n/a)</td><td>4.07 (n/a)</td><td>3.81 (n/a)</td><td>2.05 (n/a)</td><td>1099.80 (n/a)</td><td>873.14 (n/a)</td><td>1031.70 (n/a)</td><td>492.20 (n/a)</td><td>273.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.19 (+15.11%)</td><td>8.15 <b>(+34.27%)</b></td><td>8.56 (+17.66%)</td><td>6.73 <b>(+90.53%)</b></td><td>1.01 <b>(-52.13%)</b></td><td>623.20 <b>(-47.52%)</b></td><td>521.46 <b>(-32.90%)</b></td><td>490.10 (-15.00%)</td><td>456.30 (-13.12%)</td><td>68.71 <b>(-77.95%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>7.99 (n/a)</td><td>6.07 (n/a)</td><td>7.27 (n/a)</td><td>3.53 (n/a)</td><td>2.11 (n/a)</td><td>1187.40 (n/a)</td><td>777.18 (n/a)</td><td>576.60 (n/a)</td><td>525.20 (n/a)</td><td>311.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.90 <b>(-33.06%)</b></td><td>4.54 (-13.71%)</td><td>4.48 (-10.47%)</td><td>1.69 <b>(+45.11%)</b></td><td>2.22 <b>(-43.90%)</b></td><td>2485.10 <b>(-31.09%)</b></td><td>1203.06 <b>(-22.20%)</b></td><td>937.00 (+11.71%)</td><td>607.60 <b>(+49.40%)</b></td><td>774.80 <b>(-44.36%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>10.31 (n/a)</td><td>5.26 (n/a)</td><td>5.00 (n/a)</td><td>1.16 (n/a)</td><td>3.95 (n/a)</td><td>3606.10 (n/a)</td><td>1546.32 (n/a)</td><td>838.80 (n/a)</td><td>406.70 (n/a)</td><td>1392.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.04 (-4.72%)</td><td>5.12 <b>(-26.24%)</b></td><td>5.36 <b>(-33.16%)</b></td><td>1.74 <b>(-50.43%)</b></td><td>2.79 (+10.61%)</td><td>2407.00 <b>(+101.74%)</b></td><td>1119.96 <b>(+61.47%)</b></td><td>782.00 <b>(+49.61%)</b></td><td>464.10 (+4.93%)</td><td>776.66 <b>(+145.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>9.48 (n/a)</td><td>6.94 (n/a)</td><td>8.02 (n/a)</td><td>3.52 (n/a)</td><td>2.52 (n/a)</td><td>1193.10 (n/a)</td><td>693.62 (n/a)</td><td>522.70 (n/a)</td><td>442.30 (n/a)</td><td>316.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.66 (+1.33%)</td><td>1.11 <b>(-22.10%)</b></td><td>1.42 (-8.70%)</td><td>0.16 <b>(-81.85%)</b></td><td>0.63 <b>(+99.83%)</b></td><td>3307.20 <b>(+451.11%)</b></td><td>1001.36 <b>(+157.74%)</b></td><td>368.10 (+9.52%)</td><td>315.50 (-1.31%)</td><td>1297.16 <b>(+988.23%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.64 (n/a)</td><td>1.43 (n/a)</td><td>1.56 (n/a)</td><td>0.87 (n/a)</td><td>0.32 (n/a)</td><td>600.10 (n/a)</td><td>388.52 (n/a)</td><td>336.10 (n/a)</td><td>319.70 (n/a)</td><td>119.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.57 (+1.48%)</td><td>1.67 (-11.59%)</td><td>1.59 (-9.72%)</td><td>0.50 <b>(-69.01%)</b></td><td>0.81 <b>(+117.26%)</b></td><td>2098.10 <b>(+222.69%)</b></td><td>876.02 <b>(+53.41%)</b></td><td>659.30 (+10.77%)</td><td>407.70 (-1.47%)</td><td>697.87 <b>(+644.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.53 (n/a)</td><td>1.89 (n/a)</td><td>1.76 (n/a)</td><td>1.61 (n/a)</td><td>0.37 (n/a)</td><td>650.20 (n/a)</td><td>571.04 (n/a)</td><td>595.20 (n/a)</td><td>413.80 (n/a)</td><td>93.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.47 <b>(+27.85%)</b></td><td>2.11 (+3.39%)</td><td>2.41 (+4.96%)</td><td>0.99 <b>(+68.34%)</b></td><td>1.05 <b>(+26.55%)</b></td><td>2107.70 <b>(-40.60%)</b></td><td>1261.86 (-10.67%)</td><td>870.50 (-4.72%)</td><td>604.40 <b>(-21.78%)</b></td><td>691.99 <b>(-42.12%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>2.71 (n/a)</td><td>2.04 (n/a)</td><td>2.30 (n/a)</td><td>0.59 (n/a)</td><td>0.83 (n/a)</td><td>3548.10 (n/a)</td><td>1412.52 (n/a)</td><td>913.60 (n/a)</td><td>772.70 (n/a)</td><td>1195.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.82 (+2.38%)</td><td>1.12 (-10.50%)</td><td>0.98 <b>(-39.80%)</b></td><td>0.83 <b>(+204.98%)</b></td><td>0.40 <b>(-39.52%)</b></td><td>630.00 <b>(-67.21%)</b></td><td>503.86 <b>(-26.85%)</b></td><td>534.20 <b>(+66.11%)</b></td><td>288.50 (-2.30%)</td><td>128.83 <b>(-81.61%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>1.78 (n/a)</td><td>1.25 (n/a)</td><td>1.63 (n/a)</td><td>0.27 (n/a)</td><td>0.66 (n/a)</td><td>1921.30 (n/a)</td><td>688.80 (n/a)</td><td>321.60 (n/a)</td><td>295.30 (n/a)</td><td>700.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (-8.91%)</td><td>0.08 (+3.12%)</td><td>0.09 (+5.02%)</td><td>0.05 <b>(+195.50%)</b></td><td>0.03 <b>(-29.57%)</b></td><td>645.40 <b>(-66.16%)</b></td><td>444.18 <b>(-33.43%)</b></td><td>349.40 (-4.77%)</td><td>308.50 (+9.79%)</td><td>166.58 <b>(-76.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1907.10 (n/a)</td><td>667.24 (n/a)</td><td>366.90 (n/a)</td><td>281.00 (n/a)</td><td>696.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (-11.27%)</td><td>0.08 (-4.26%)</td><td>0.06 (-8.10%)</td><td>0.04 <b>(+38.77%)</b></td><td>0.04 (-17.66%)</td><td>797.70 <b>(-27.94%)</b></td><td>491.04 (-7.01%)</td><td>512.60 (+8.83%)</td><td>251.00 (+12.71%)</td><td>220.65 <b>(-36.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1107.00 (n/a)</td><td>528.08 (n/a)</td><td>471.00 (n/a)</td><td>222.70 (n/a)</td><td>347.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.29 (+13.19%)</td><td>0.19 (-11.20%)</td><td>0.21 (-2.39%)</td><td>0.04 <b>(-74.53%)</b></td><td>0.09 <b>(+115.82%)</b></td><td>1790.70 <b>(+292.61%)</b></td><td>594.02 <b>(+85.36%)</b></td><td>312.40 (+2.46%)</td><td>227.50 (-11.65%)</td><td>670.16 <b>(+746.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>456.10 (n/a)</td><td>320.46 (n/a)</td><td>304.90 (n/a)</td><td>257.50 (n/a)</td><td>79.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 (-5.89%)</td><td>0.18 (-0.89%)</td><td>0.20 (-8.73%)</td><td>0.12 <b>(+24.42%)</b></td><td>0.05 <b>(-31.43%)</b></td><td>567.70 (-19.63%)</td><td>382.14 (-7.05%)</td><td>335.80 (+9.60%)</td><td>279.50 (+6.27%)</td><td>115.93 <b>(-39.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>706.40 (n/a)</td><td>411.12 (n/a)</td><td>306.40 (n/a)</td><td>263.00 (n/a)</td><td>190.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.26 <b>(-20.75%)</b></td><td>0.18 (+2.33%)</td><td>0.19 <b>(+31.85%)</b></td><td>0.11 (+7.57%)</td><td>0.06 <b>(-30.25%)</b></td><td>580.00 (-7.04%)</td><td>406.32 (-6.60%)</td><td>353.30 <b>(-24.15%)</b></td><td>250.20 <b>(+26.17%)</b></td><td>144.24 (-5.85%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>623.90 (n/a)</td><td>435.02 (n/a)</td><td>465.80 (n/a)</td><td>198.30 (n/a)</td><td>153.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.44 (-15.21%)</td><td>0.29 <b>(-25.21%)</b></td><td>0.26 <b>(-43.92%)</b></td><td>0.21 (+0.58%)</td><td>0.09 <b>(-43.79%)</b></td><td>628.00 (-0.57%)</td><td>487.26 <b>(+20.11%)</b></td><td>512.20 <b>(+78.28%)</b></td><td>300.40 (+17.94%)</td><td>119.52 <b>(-37.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>631.60 (n/a)</td><td>405.68 (n/a)</td><td>287.30 (n/a)</td><td>254.70 (n/a)</td><td>192.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.51 (-13.33%)</td><td>0.37 (-5.67%)</td><td>0.31 (-18.88%)</td><td>0.26 (+3.58%)</td><td>0.12 (-6.74%)</td><td>513.10 (-3.46%)</td><td>387.92 (+5.72%)</td><td>420.00 <b>(+23.28%)</b></td><td>257.50 (+15.37%)</td><td>118.98 (+0.55%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.59 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>531.50 (n/a)</td><td>366.92 (n/a)</td><td>340.70 (n/a)</td><td>223.20 (n/a)</td><td>118.33 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.37 <b>(-32.81%)</b></td><td>0.31 (-14.28%)</td><td>0.30 (-15.25%)</td><td>0.26 (+9.59%)</td><td>0.05 <b>(-62.47%)</b></td><td>507.70 (-8.75%)</td><td>431.24 (+8.85%)</td><td>437.80 (+18.01%)</td><td>359.10 <b>(+48.82%)</b></td><td>62.85 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>556.40 (n/a)</td><td>396.18 (n/a)</td><td>371.00 (n/a)</td><td>241.30 (n/a)</td><td>125.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (+12.10%)</td><td>0.05 (+15.60%)</td><td>0.05 (+15.03%)</td><td>0.04 <b>(+36.11%)</b></td><td>0.02 (-1.77%)</td><td>457.10 <b>(-26.52%)</b></td><td>349.92 (-17.41%)</td><td>343.20 (-13.07%)</td><td>204.50 (-10.78%)</td><td>105.71 <b>(-35.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:40:29</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>622.10 (n/a)</td><td>423.70 (n/a)</td><td>394.80 (n/a)</td><td>229.20 (n/a)</td><td>164.62 (n/a)</td>
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
