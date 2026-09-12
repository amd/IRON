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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(-34.63%)</b></td><td>0.02 (+0.11%)</td><td>0.02 <b>(+40.05%)</b></td><td>0.01 <b>(+32.41%)</b></td><td>0.01 <b>(-46.71%)</b></td><td>538.70 <b>(-24.47%)</b></td><td>369.64 (-19.44%)</td><td>334.40 <b>(-28.61%)</b></td><td>237.70 <b>(+52.96%)</b></td><td>142.51 <b>(-43.22%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>713.20 (n/a)</td><td>458.82 (n/a)</td><td>468.40 (n/a)</td><td>155.40 (n/a)</td><td>250.97 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+24.99%)</b></td><td>0.02 <b>(+25.70%)</b></td><td>0.02 (+16.62%)</td><td>0.01 <b>(+50.05%)</b></td><td>0.01 (+8.04%)</td><td>429.00 <b>(-33.35%)</b></td><td>313.12 <b>(-22.86%)</b></td><td>282.80 (-14.25%)</td><td>238.90 (-19.99%)</td><td>83.55 <b>(-42.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>643.70 (n/a)</td><td>405.92 (n/a)</td><td>329.80 (n/a)</td><td>298.60 (n/a)</td><td>145.87 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+17.05%)</td><td>0.02 (+12.00%)</td><td>0.03 <b>(+22.32%)</b></td><td>0.01 (+2.16%)</td><td>0.01 <b>(+47.27%)</b></td><td>551.40 (-2.11%)</td><td>338.30 (-5.05%)</td><td>234.30 (-18.25%)</td><td>222.60 (-14.58%)</td><td>153.31 (+19.79%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.30 (n/a)</td><td>356.30 (n/a)</td><td>286.60 (n/a)</td><td>260.60 (n/a)</td><td>127.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-5.59%)</td><td>0.02 <b>(+23.93%)</b></td><td>0.02 <b>(+78.23%)</b></td><td>0.01 <b>(+48.51%)</b></td><td>0.01 <b>(-31.08%)</b></td><td>603.40 <b>(-32.66%)</b></td><td>329.70 <b>(-30.57%)</b></td><td>271.70 <b>(-43.89%)</b></td><td>237.10 (+5.90%)</td><td>154.99 <b>(-43.66%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>896.10 (n/a)</td><td>474.88 (n/a)</td><td>484.20 (n/a)</td><td>223.90 (n/a)</td><td>275.12 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-3.31%)</td><td>0.02 (-8.62%)</td><td>0.02 (-3.32%)</td><td>0.01 <b>(-25.84%)</b></td><td>0.00 <b>(+36.39%)</b></td><td>599.10 <b>(+34.84%)</b></td><td>415.74 (+14.72%)</td><td>360.00 (+3.45%)</td><td>294.30 (+3.44%)</td><td>135.19 <b>(+85.57%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>444.30 (n/a)</td><td>362.40 (n/a)</td><td>348.00 (n/a)</td><td>284.50 (n/a)</td><td>72.85 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-7.49%)</td><td>0.02 (-4.92%)</td><td>0.02 (-15.57%)</td><td>0.01 <b>(-34.25%)</b></td><td>0.01 (+0.61%)</td><td>769.80 <b>(+52.07%)</b></td><td>375.04 (+13.06%)</td><td>298.10 (+18.43%)</td><td>248.70 (+8.08%)</td><td>221.84 <b>(+77.55%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.20 (n/a)</td><td>331.72 (n/a)</td><td>251.70 (n/a)</td><td>230.10 (n/a)</td><td>124.94 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (+7.54%)</td><td>0.05 <b>(+29.88%)</b></td><td>0.05 <b>(+71.19%)</b></td><td>0.03 (+11.42%)</td><td>0.01 (-0.07%)</td><td>400.80 (-10.26%)</td><td>269.44 <b>(-23.60%)</b></td><td>230.90 <b>(-41.59%)</b></td><td>227.20 (-7.00%)</td><td>74.65 (-14.72%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>446.60 (n/a)</td><td>352.68 (n/a)</td><td>395.30 (n/a)</td><td>244.30 (n/a)</td><td>87.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-9.68%)</td><td>0.03 (-6.39%)</td><td>0.03 (+16.78%)</td><td>0.02 (+6.73%)</td><td>0.01 <b>(-20.84%)</b></td><td>586.40 (-6.31%)</td><td>414.66 (+3.69%)</td><td>352.50 (-14.38%)</td><td>280.10 (+10.71%)</td><td>137.76 (-9.93%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>625.90 (n/a)</td><td>399.90 (n/a)</td><td>411.70 (n/a)</td><td>253.00 (n/a)</td><td>152.95 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (-6.36%)</td><td>0.04 (-17.83%)</td><td>0.03 <b>(-26.15%)</b></td><td>0.02 <b>(-21.13%)</b></td><td>0.01 <b>(+41.32%)</b></td><td>557.50 <b>(+26.79%)</b></td><td>389.62 <b>(+30.40%)</b></td><td>371.70 <b>(+35.41%)</b></td><td>243.20 (+6.81%)</td><td>145.49 <b>(+78.54%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>439.70 (n/a)</td><td>298.78 (n/a)</td><td>274.50 (n/a)</td><td>227.70 (n/a)</td><td>81.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (+1.42%)</td><td>0.04 (-10.09%)</td><td>0.04 <b>(-30.11%)</b></td><td>0.02 (+7.38%)</td><td>0.02 (-10.95%)</td><td>556.20 (-6.87%)</td><td>354.54 (+6.20%)</td><td>335.20 <b>(+43.06%)</b></td><td>196.60 (-1.40%)</td><td>148.16 (-15.67%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>597.20 (n/a)</td><td>333.84 (n/a)</td><td>234.30 (n/a)</td><td>199.40 (n/a)</td><td>175.69 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-11.45%)</td><td>0.03 (-7.69%)</td><td>0.02 (-14.01%)</td><td>0.02 (+0.83%)</td><td>0.01 (-12.44%)</td><td>568.80 (-0.82%)</td><td>440.68 (+6.92%)</td><td>505.60 (+16.28%)</td><td>292.40 (+12.94%)</td><td>135.00 (-2.55%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>573.50 (n/a)</td><td>412.16 (n/a)</td><td>434.80 (n/a)</td><td>258.90 (n/a)</td><td>138.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (-10.96%)</td><td>0.03 (+13.87%)</td><td>0.03 (-0.38%)</td><td>0.02 <b>(+25.22%)</b></td><td>0.01 (-11.21%)</td><td>656.30 <b>(-20.14%)</b></td><td>448.12 (-16.85%)</td><td>476.30 (+0.38%)</td><td>262.10 (+12.30%)</td><td>176.72 <b>(-25.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>821.80 (n/a)</td><td>538.96 (n/a)</td><td>474.50 (n/a)</td><td>233.40 (n/a)</td><td>237.44 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 <b>(+41.62%)</b></td><td>0.08 <b>(+45.99%)</b></td><td>0.08 <b>(+46.04%)</b></td><td>0.06 <b>(+45.28%)</b></td><td>0.02 <b>(+55.78%)</b></td><td>444.10 <b>(-31.17%)</b></td><td>320.32 <b>(-31.14%)</b></td><td>302.20 <b>(-31.54%)</b></td><td>248.70 <b>(-29.39%)</b></td><td>78.64 <b>(-27.23%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>645.20 (n/a)</td><td>465.20 (n/a)</td><td>441.40 (n/a)</td><td>352.20 (n/a)</td><td>108.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (+2.93%)</td><td>0.08 (+3.58%)</td><td>0.09 (-4.58%)</td><td>0.05 <b>(+23.79%)</b></td><td>0.02 (-12.98%)</td><td>526.30 (-19.22%)</td><td>330.22 (-8.47%)</td><td>270.40 (+4.81%)</td><td>235.90 (-2.84%)</td><td>121.56 <b>(-30.40%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>651.50 (n/a)</td><td>360.76 (n/a)</td><td>258.00 (n/a)</td><td>242.80 (n/a)</td><td>174.65 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (-18.60%)</td><td>0.06 (-14.37%)</td><td>0.05 (-10.41%)</td><td>0.04 (+4.19%)</td><td>0.02 <b>(-30.74%)</b></td><td>581.20 (-4.03%)</td><td>455.16 (+11.18%)</td><td>492.10 (+11.61%)</td><td>275.90 <b>(+22.84%)</b></td><td>125.56 (-16.63%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>605.60 (n/a)</td><td>409.38 (n/a)</td><td>440.90 (n/a)</td><td>224.60 (n/a)</td><td>150.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (+2.06%)</td><td>0.05 (-13.27%)</td><td>0.04 <b>(-40.41%)</b></td><td>0.04 <b>(+307.39%)</b></td><td>0.02 <b>(-27.00%)</b></td><td>586.90 <b>(-75.45%)</b></td><td>499.42 <b>(-32.96%)</b></td><td>552.80 <b>(+67.82%)</b></td><td>257.20 (-2.02%)</td><td>138.25 <b>(-85.00%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2390.90 (n/a)</td><td>744.92 (n/a)</td><td>329.40 (n/a)</td><td>262.50 (n/a)</td><td>921.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (-18.44%)</td><td>0.06 (-3.70%)</td><td>0.06 <b>(+28.44%)</b></td><td>0.03 <b>(-31.75%)</b></td><td>0.03 <b>(-22.14%)</b></td><td>863.60 <b>(+46.52%)</b></td><td>456.32 (+3.67%)</td><td>422.30 <b>(-22.16%)</b></td><td>259.00 <b>(+22.63%)</b></td><td>242.00 <b>(+33.96%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>589.40 (n/a)</td><td>440.18 (n/a)</td><td>542.50 (n/a)</td><td>211.20 (n/a)</td><td>180.65 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (+14.68%)</td><td>0.07 <b>(+20.04%)</b></td><td>0.07 <b>(+30.36%)</b></td><td>0.05 (-4.65%)</td><td>0.02 <b>(+54.75%)</b></td><td>523.10 (+4.87%)</td><td>381.70 (-13.00%)</td><td>367.40 <b>(-23.28%)</b></td><td>258.50 (-12.82%)</td><td>120.02 <b>(+42.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>438.74 (n/a)</td><td>478.90 (n/a)</td><td>296.50 (n/a)</td><td>84.10 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.32 <b>(+52.48%)</b></td><td>0.16 (-2.38%)</td><td>0.11 <b>(-36.06%)</b></td><td>0.06 <b>(-38.75%)</b></td><td>0.10 <b>(+126.99%)</b></td><td>768.60 <b>(+63.29%)</b></td><td>421.90 <b>(+28.11%)</b></td><td>444.40 <b>(+56.37%)</b></td><td>154.80 <b>(-34.43%)</b></td><td>234.32 <b>(+133.22%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>470.70 (n/a)</td><td>329.32 (n/a)</td><td>284.20 (n/a)</td><td>236.10 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (-11.99%)</td><td>0.17 (+10.02%)</td><td>0.18 <b>(+21.84%)</b></td><td>0.12 <b>(+36.66%)</b></td><td>0.03 <b>(-30.79%)</b></td><td>422.30 <b>(-26.82%)</b></td><td>305.46 (-14.16%)</td><td>273.80 (-17.93%)</td><td>250.20 (+13.62%)</td><td>72.77 <b>(-45.40%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>577.10 (n/a)</td><td>355.84 (n/a)</td><td>333.60 (n/a)</td><td>220.20 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.25 (-2.23%)</td><td>0.16 (+14.02%)</td><td>0.17 <b>(+61.96%)</b></td><td>0.09 (+16.40%)</td><td>0.07 (-6.87%)</td><td>520.60 (-14.08%)</td><td>346.70 (-14.39%)</td><td>285.50 <b>(-38.26%)</b></td><td>199.00 (+2.31%)</td><td>146.16 (-11.13%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>605.90 (n/a)</td><td>404.96 (n/a)</td><td>462.40 (n/a)</td><td>194.50 (n/a)</td><td>164.48 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (-12.85%)</td><td>0.14 (+15.15%)</td><td>0.16 <b>(+49.80%)</b></td><td>0.10 (+5.15%)</td><td>0.04 <b>(-22.59%)</b></td><td>507.10 (-4.89%)</td><td>369.50 (-15.32%)</td><td>316.60 <b>(-33.25%)</b></td><td>264.80 (+14.73%)</td><td>109.07 (-7.50%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>533.20 (n/a)</td><td>436.34 (n/a)</td><td>474.30 (n/a)</td><td>230.80 (n/a)</td><td>117.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.24 (+10.21%)</td><td>0.15 (+12.92%)</td><td>0.12 (+12.74%)</td><td>0.09 (-2.12%)</td><td>0.06 (+13.66%)</td><td>574.00 (+2.15%)</td><td>377.08 (-9.98%)</td><td>397.40 (-11.31%)</td><td>207.70 (-9.26%)</td><td>138.25 (+5.40%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>561.90 (n/a)</td><td>418.88 (n/a)</td><td>448.10 (n/a)</td><td>228.90 (n/a)</td><td>131.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (-14.97%)</td><td>0.14 (-15.19%)</td><td>0.16 (-12.91%)</td><td>0.07 (-17.30%)</td><td>0.05 (-10.26%)</td><td>676.90 <b>(+20.92%)</b></td><td>396.20 (+19.57%)</td><td>315.80 (+14.79%)</td><td>247.80 (+17.61%)</td><td>173.13 <b>(+25.78%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>559.80 (n/a)</td><td>331.36 (n/a)</td><td>275.10 (n/a)</td><td>210.70 (n/a)</td><td>137.65 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-19.83%)</td><td>0.01 <b>(-29.16%)</b></td><td>0.01 <b>(-37.31%)</b></td><td>0.00 <b>(-20.97%)</b></td><td>0.00 <b>(-23.66%)</b></td><td>527.00 <b>(+26.53%)</b></td><td>445.34 <b>(+40.54%)</b></td><td>467.30 <b>(+59.54%)</b></td><td>304.90 <b>(+24.70%)</b></td><td>87.16 (+17.51%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.50 (n/a)</td><td>316.88 (n/a)</td><td>292.90 (n/a)</td><td>244.50 (n/a)</td><td>74.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (+4.37%)</td><td>0.01 (-13.17%)</td><td>0.01 <b>(-39.96%)</b></td><td>0.00 <b>(-25.98%)</b></td><td>0.00 <b>(+25.33%)</b></td><td>767.50 <b>(+35.10%)</b></td><td>437.34 <b>(+25.18%)</b></td><td>459.20 <b>(+66.56%)</b></td><td>231.80 (-4.18%)</td><td>215.22 <b>(+55.34%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>568.10 (n/a)</td><td>349.38 (n/a)</td><td>275.70 (n/a)</td><td>241.90 (n/a)</td><td>138.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-5.45%)</td><td>0.01 (-8.97%)</td><td>0.01 (+3.98%)</td><td>0.01 <b>(-24.35%)</b></td><td>0.00 <b>(+29.45%)</b></td><td>502.80 <b>(+32.18%)</b></td><td>352.14 (+15.89%)</td><td>281.00 (-3.83%)</td><td>238.40 (+5.77%)</td><td>124.41 <b>(+83.24%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>380.40 (n/a)</td><td>303.86 (n/a)</td><td>292.20 (n/a)</td><td>225.40 (n/a)</td><td>67.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 <b>(-44.45%)</b></td><td>0.01 <b>(-36.46%)</b></td><td>0.01 <b>(-41.13%)</b></td><td>0.00 (-14.01%)</td><td>0.00 <b>(-56.63%)</b></td><td>554.00 (+16.29%)</td><td>467.74 <b>(+42.46%)</b></td><td>492.80 <b>(+69.87%)</b></td><td>269.50 <b>(+80.03%)</b></td><td>115.04 (-14.13%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.40 (n/a)</td><td>328.34 (n/a)</td><td>290.10 (n/a)</td><td>149.70 (n/a)</td><td>133.97 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 <b>(-25.06%)</b></td><td>0.01 (-10.30%)</td><td>0.01 (-3.37%)</td><td>0.00 (-13.47%)</td><td>0.00 <b>(-23.02%)</b></td><td>594.00 (+15.56%)</td><td>362.64 (+9.56%)</td><td>271.70 (+3.47%)</td><td>264.20 <b>(+33.43%)</b></td><td>145.20 (+9.31%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.00 (n/a)</td><td>331.00 (n/a)</td><td>262.60 (n/a)</td><td>198.00 (n/a)</td><td>132.83 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-2.64%)</td><td>0.01 (-0.79%)</td><td>0.00 (-8.38%)</td><td>0.00 (+6.25%)</td><td>0.00 (+2.76%)</td><td>599.20 (-5.87%)</td><td>438.94 (+1.68%)</td><td>526.90 (+9.16%)</td><td>239.20 (+2.71%)</td><td>166.86 (+1.76%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>636.60 (n/a)</td><td>431.70 (n/a)</td><td>482.70 (n/a)</td><td>232.90 (n/a)</td><td>163.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+37.21%)</b></td><td>0.02 (+14.79%)</td><td>0.01 <b>(-29.69%)</b></td><td>0.01 <b>(+306.22%)</b></td><td>0.01 (+11.93%)</td><td>505.30 <b>(-75.38%)</b></td><td>367.92 <b>(-43.96%)</b></td><td>447.50 <b>(+42.20%)</b></td><td>169.50 <b>(-27.13%)</b></td><td>155.30 <b>(-80.21%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2052.70 (n/a)</td><td>656.50 (n/a)</td><td>314.70 (n/a)</td><td>232.60 (n/a)</td><td>784.83 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-12.45%)</td><td>0.02 (-5.11%)</td><td>0.01 <b>(-22.10%)</b></td><td>0.01 (-0.81%)</td><td>0.00 <b>(-22.34%)</b></td><td>500.10 (+0.83%)</td><td>356.12 (+2.37%)</td><td>371.60 <b>(+28.36%)</b></td><td>263.50 (+14.22%)</td><td>95.89 (-16.57%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.00 (n/a)</td><td>347.88 (n/a)</td><td>289.50 (n/a)</td><td>230.70 (n/a)</td><td>114.93 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-3.96%)</td><td>0.01 (-19.80%)</td><td>0.01 <b>(-40.59%)</b></td><td>0.01 <b>(+23.34%)</b></td><td>0.00 <b>(-31.67%)</b></td><td>466.30 (-18.92%)</td><td>404.82 (+15.88%)</td><td>431.80 <b>(+68.34%)</b></td><td>250.60 (+4.16%)</td><td>88.25 <b>(-41.23%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.10 (n/a)</td><td>349.34 (n/a)</td><td>256.50 (n/a)</td><td>240.60 (n/a)</td><td>150.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+14.75%)</td><td>0.01 <b>(+26.71%)</b></td><td>0.01 (+1.39%)</td><td>0.01 <b>(+37.24%)</b></td><td>0.01 <b>(+27.71%)</b></td><td>566.60 <b>(-27.13%)</b></td><td>415.52 <b>(-20.66%)</b></td><td>491.90 (-1.38%)</td><td>234.30 (-12.83%)</td><td>161.99 <b>(-21.95%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>777.60 (n/a)</td><td>523.70 (n/a)</td><td>498.80 (n/a)</td><td>268.80 (n/a)</td><td>207.55 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+39.89%)</b></td><td>0.02 <b>(+35.63%)</b></td><td>0.02 <b>(+58.30%)</b></td><td>0.01 (+11.87%)</td><td>0.01 <b>(+85.64%)</b></td><td>557.80 (-10.61%)</td><td>391.40 <b>(-21.52%)</b></td><td>325.00 <b>(-36.82%)</b></td><td>247.00 <b>(-28.51%)</b></td><td>148.98 <b>(+24.63%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.00 (n/a)</td><td>498.70 (n/a)</td><td>514.40 (n/a)</td><td>345.50 (n/a)</td><td>119.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+0.14%)</td><td>0.01 (+1.07%)</td><td>0.01 (+0.31%)</td><td>0.01 (+0.86%)</td><td>0.00 (+10.94%)</td><td>566.20 (-0.86%)</td><td>454.26 (+0.20%)</td><td>487.30 (-0.31%)</td><td>306.40 (-0.13%)</td><td>118.81 (+13.60%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.10 (n/a)</td><td>453.34 (n/a)</td><td>488.80 (n/a)</td><td>306.80 (n/a)</td><td>104.58 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-7.78%)</td><td>0.03 (+11.18%)</td><td>0.03 (+11.79%)</td><td>0.02 (-0.96%)</td><td>0.01 (-14.22%)</td><td>567.20 (+0.98%)</td><td>337.58 (-11.57%)</td><td>303.50 (-10.55%)</td><td>244.40 (+8.43%)</td><td>131.65 (-4.11%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.70 (n/a)</td><td>381.76 (n/a)</td><td>339.30 (n/a)</td><td>225.40 (n/a)</td><td>137.30 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (-11.98%)</td><td>0.04 (+18.05%)</td><td>0.04 <b>(+78.00%)</b></td><td>0.02 <b>(+30.37%)</b></td><td>0.01 <b>(-21.45%)</b></td><td>445.50 <b>(-23.30%)</b></td><td>313.52 <b>(-20.30%)</b></td><td>246.20 <b>(-43.83%)</b></td><td>199.80 (+13.59%)</td><td>120.62 <b>(-23.18%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>580.80 (n/a)</td><td>393.36 (n/a)</td><td>438.30 (n/a)</td><td>175.90 (n/a)</td><td>157.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(-39.78%)</b></td><td>0.04 (+15.71%)</td><td>0.04 <b>(+57.73%)</b></td><td>0.02 <b>(+297.71%)</b></td><td>0.01 <b>(-60.44%)</b></td><td>476.20 <b>(-74.85%)</b></td><td>317.16 <b>(-52.45%)</b></td><td>275.20 <b>(-36.60%)</b></td><td>224.80 <b>(+66.03%)</b></td><td>107.54 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1893.70 (n/a)</td><td>667.06 (n/a)</td><td>434.10 (n/a)</td><td>135.40 (n/a)</td><td>697.93 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-18.79%)</td><td>0.03 (+2.95%)</td><td>0.02 (+4.73%)</td><td>0.02 (+1.83%)</td><td>0.01 <b>(-20.95%)</b></td><td>588.90 (-1.80%)</td><td>418.40 (-4.80%)</td><td>435.90 (-4.51%)</td><td>279.60 <b>(+23.12%)</b></td><td>132.79 (-0.81%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>439.48 (n/a)</td><td>456.50 (n/a)</td><td>227.10 (n/a)</td><td>133.88 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(+33.20%)</b></td><td>0.04 <b>(+47.37%)</b></td><td>0.03 <b>(+34.61%)</b></td><td>0.02 <b>(+44.19%)</b></td><td>0.01 <b>(+41.73%)</b></td><td>426.30 <b>(-30.64%)</b></td><td>317.12 <b>(-32.26%)</b></td><td>313.00 <b>(-25.72%)</b></td><td>229.80 <b>(-24.93%)</b></td><td>89.26 <b>(-32.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>614.60 (n/a)</td><td>468.16 (n/a)</td><td>421.40 (n/a)</td><td>306.10 (n/a)</td><td>131.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-13.68%)</td><td>0.03 (-15.21%)</td><td>0.02 <b>(-27.16%)</b></td><td>0.02 (+2.15%)</td><td>0.01 <b>(-20.81%)</b></td><td>514.70 (-2.11%)</td><td>419.36 (+15.04%)</td><td>462.30 <b>(+37.30%)</b></td><td>257.00 (+15.87%)</td><td>101.53 (-13.28%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.80 (n/a)</td><td>364.52 (n/a)</td><td>336.70 (n/a)</td><td>221.80 (n/a)</td><td>117.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(-27.91%)</b></td><td>0.04 <b>(-37.54%)</b></td><td>0.04 <b>(-43.92%)</b></td><td>0.04 <b>(-25.01%)</b></td><td>0.01 <b>(-26.51%)</b></td><td>545.40 <b>(+33.35%)</b></td><td>487.80 <b>(+59.84%)</b></td><td>515.40 <b>(+78.34%)</b></td><td>355.40 <b>(+38.67%)</b></td><td>76.07 <b>(+26.98%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>409.00 (n/a)</td><td>305.18 (n/a)</td><td>289.00 (n/a)</td><td>256.30 (n/a)</td><td>59.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+0.21%)</td><td>0.05 (-14.57%)</td><td>0.04 <b>(-26.76%)</b></td><td>0.04 (+0.10%)</td><td>0.02 (-9.15%)</td><td>576.30 (-0.09%)</td><td>447.48 (+15.61%)</td><td>513.20 <b>(+36.56%)</b></td><td>247.40 (-0.20%)</td><td>141.21 (-2.60%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.80 (n/a)</td><td>387.06 (n/a)</td><td>375.80 (n/a)</td><td>247.90 (n/a)</td><td>144.97 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (+18.99%)</td><td>0.06 (-14.49%)</td><td>0.05 <b>(-34.62%)</b></td><td>0.04 <b>(-41.03%)</b></td><td>0.03 <b>(+286.44%)</b></td><td>565.50 <b>(+69.57%)</b></td><td>378.42 <b>(+33.82%)</b></td><td>420.00 <b>(+52.95%)</b></td><td>219.80 (-15.95%)</td><td>150.13 <b>(+407.19%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>333.50 (n/a)</td><td>282.78 (n/a)</td><td>274.60 (n/a)</td><td>261.50 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (-11.05%)</td><td>0.06 (-9.92%)</td><td>0.08 (+5.22%)</td><td>0.03 (-19.74%)</td><td>0.02 (+13.22%)</td><td>615.30 <b>(+24.61%)</b></td><td>401.06 (+18.36%)</td><td>274.10 (-4.96%)</td><td>265.70 (+12.39%)</td><td>181.13 <b>(+57.33%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>493.80 (n/a)</td><td>338.86 (n/a)</td><td>288.40 (n/a)</td><td>236.40 (n/a)</td><td>115.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(-39.01%)</b></td><td>0.05 <b>(-41.05%)</b></td><td>0.04 <b>(-56.44%)</b></td><td>0.03 (-6.47%)</td><td>0.02 <b>(-47.18%)</b></td><td>606.10 (+6.91%)</td><td>499.58 <b>(+53.17%)</b></td><td>561.90 <b>(+129.53%)</b></td><td>253.00 <b>(+63.97%)</b></td><td>142.04 (-14.70%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>566.90 (n/a)</td><td>326.16 (n/a)</td><td>244.80 (n/a)</td><td>154.30 (n/a)</td><td>166.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(-32.22%)</b></td><td>0.04 <b>(-25.90%)</b></td><td>0.04 <b>(-21.03%)</b></td><td>0.03 <b>(-23.47%)</b></td><td>0.01 <b>(-37.98%)</b></td><td>700.80 <b>(+30.67%)</b></td><td>525.28 <b>(+32.60%)</b></td><td>549.70 <b>(+26.63%)</b></td><td>375.00 <b>(+47.52%)</b></td><td>132.87 (+18.98%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>396.14 (n/a)</td><td>434.10 (n/a)</td><td>254.20 (n/a)</td><td>111.68 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.20 (n/a)</td><td>421.56 (n/a)</td><td>500.00 (n/a)</td><td>262.70 (n/a)</td><td>138.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1865.00 (n/a)</td><td>723.68 (n/a)</td><td>567.70 (n/a)</td><td>247.70 (n/a)</td><td>657.78 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.80 (n/a)</td><td>408.92 (n/a)</td><td>444.70 (n/a)</td><td>203.20 (n/a)</td><td>154.09 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.40 (n/a)</td><td>388.32 (n/a)</td><td>404.40 (n/a)</td><td>221.30 (n/a)</td><td>141.67 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>663.80 (n/a)</td><td>439.08 (n/a)</td><td>413.10 (n/a)</td><td>290.20 (n/a)</td><td>159.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>536.40 (n/a)</td><td>471.52 (n/a)</td><td>472.00 (n/a)</td><td>408.10 (n/a)</td><td>55.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>526.30 (n/a)</td><td>459.78 (n/a)</td><td>467.20 (n/a)</td><td>398.90 (n/a)</td><td>49.25 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>796.50 (n/a)</td><td>490.90 (n/a)</td><td>445.20 (n/a)</td><td>242.60 (n/a)</td><td>201.36 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>602.00 (n/a)</td><td>422.06 (n/a)</td><td>415.00 (n/a)</td><td>262.40 (n/a)</td><td>153.69 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 <b>(-21.78%)</b></td><td>0.11 <b>(-29.31%)</b></td><td>0.10 <b>(-44.68%)</b></td><td>0.08 (-11.38%)</td><td>0.04 <b>(-34.62%)</b></td><td>616.40 (+12.83%)</td><td>463.98 <b>(+33.00%)</b></td><td>479.30 <b>(+80.80%)</b></td><td>264.00 <b>(+27.85%)</b></td><td>130.27 (-14.30%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>546.30 (n/a)</td><td>348.86 (n/a)</td><td>265.10 (n/a)</td><td>206.50 (n/a)</td><td>152.02 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>509.90 (n/a)</td><td>435.16 (n/a)</td><td>488.20 (n/a)</td><td>279.80 (n/a)</td><td>99.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>695.80 (n/a)</td><td>421.08 (n/a)</td><td>442.70 (n/a)</td><td>235.90 (n/a)</td><td>189.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>382.56 (n/a)</td><td>347.80 (n/a)</td><td>218.00 (n/a)</td><td>159.93 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>771.60 (n/a)</td><td>403.62 (n/a)</td><td>311.00 (n/a)</td><td>193.00 (n/a)</td><td>234.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.90 (n/a)</td><td>406.62 (n/a)</td><td>463.00 (n/a)</td><td>250.80 (n/a)</td><td>139.57 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>454.30 (n/a)</td><td>318.08 (n/a)</td><td>296.30 (n/a)</td><td>231.00 (n/a)</td><td>93.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.60 (n/a)</td><td>375.74 (n/a)</td><td>385.40 (n/a)</td><td>225.30 (n/a)</td><td>148.55 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>547.00 (n/a)</td><td>351.48 (n/a)</td><td>382.50 (n/a)</td><td>203.30 (n/a)</td><td>144.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>444.90 (n/a)</td><td>289.74 (n/a)</td><td>277.30 (n/a)</td><td>200.40 (n/a)</td><td>92.31 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>491.10 (n/a)</td><td>381.08 (n/a)</td><td>452.10 (n/a)</td><td>240.30 (n/a)</td><td>126.20 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>508.90 (n/a)</td><td>402.28 (n/a)</td><td>486.20 (n/a)</td><td>255.20 (n/a)</td><td>132.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>471.50 (n/a)</td><td>348.42 (n/a)</td><td>390.50 (n/a)</td><td>203.40 (n/a)</td><td>116.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>607.60 (n/a)</td><td>472.48 (n/a)</td><td>503.70 (n/a)</td><td>245.30 (n/a)</td><td>140.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.22 (-4.37%)</td><td>3.76 (+12.16%)</td><td>3.98 <b>(+25.38%)</b></td><td>2.69 (+9.27%)</td><td>0.61 (-14.43%)</td><td>3903.90 (-8.48%)</td><td>2864.36 (-11.66%)</td><td>2637.40 <b>(-20.24%)</b></td><td>2487.70 (+4.57%)</td><td>585.27 (-15.09%)</td><td>1726.47 (-4.37%)</td><td>1540.26 (+12.16%)</td><td>1628.50 <b>(+25.38%)</b></td><td>1100.17 (+9.27%)</td><td>250.13 (-14.43%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.41 (n/a)</td><td>3.35 (n/a)</td><td>3.17 (n/a)</td><td>2.46 (n/a)</td><td>0.71 (n/a)</td><td>4265.80 (n/a)</td><td>3242.28 (n/a)</td><td>3306.70 (n/a)</td><td>2378.90 (n/a)</td><td>689.32 (n/a)</td><td>1805.42 (n/a)</td><td>1373.30 (n/a)</td><td>1298.85 (n/a)</td><td>1006.84 (n/a)</td><td>292.30 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.61 (+0.43%)</td><td>3.25 (+3.82%)</td><td>3.22 (+4.02%)</td><td>2.87 (+8.01%)</td><td>0.29 (-13.58%)</td><td>8227.40 (-7.42%)</td><td>7297.44 (-3.97%)</td><td>7327.80 (-3.87%)</td><td>6527.20 (-0.43%)</td><td>666.86 <b>(-21.10%)</b></td><td>2056.30 (+0.43%)</td><td>1851.44 (+3.82%)</td><td>1831.63 (+4.02%)</td><td>1631.36 (+8.01%)</td><td>167.13 (-13.58%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.60 (n/a)</td><td>3.13 (n/a)</td><td>3.10 (n/a)</td><td>2.65 (n/a)</td><td>0.34 (n/a)</td><td>8886.50 (n/a)</td><td>7599.52 (n/a)</td><td>7622.50 (n/a)</td><td>6555.40 (n/a)</td><td>845.18 (n/a)</td><td>2047.44 (n/a)</td><td>1783.24 (n/a)</td><td>1760.81 (n/a)</td><td>1510.36 (n/a)</td><td>193.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.83 (-7.12%)</td><td>3.43 (+2.50%)</td><td>3.57 (+10.88%)</td><td>3.07 (+9.38%)</td><td>0.34 <b>(-37.36%)</b></td><td>5472.30 (-8.57%)</td><td>4932.62 (-3.60%)</td><td>4693.40 (-9.82%)</td><td>4377.70 (+7.67%)</td><td>494.00 <b>(-37.14%)</b></td><td>1962.20 (-7.12%)</td><td>1755.32 (+2.50%)</td><td>1830.22 (+10.88%)</td><td>1569.71 (+9.38%)</td><td>173.35 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.13 (n/a)</td><td>3.34 (n/a)</td><td>3.22 (n/a)</td><td>2.80 (n/a)</td><td>0.54 (n/a)</td><td>5985.50 (n/a)</td><td>5116.92 (n/a)</td><td>5204.20 (n/a)</td><td>4065.90 (n/a)</td><td>785.89 (n/a)</td><td>2112.67 (n/a)</td><td>1712.54 (n/a)</td><td>1650.58 (n/a)</td><td>1435.11 (n/a)</td><td>276.74 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.36 (+7.01%)</td><td>0.99 (+3.28%)</td><td>1.04 (+18.97%)</td><td>0.71 (-2.32%)</td><td>0.27 (+17.37%)</td><td>646.40 (+2.38%)</td><td>493.52 (-1.55%)</td><td>439.90 (-15.94%)</td><td>338.00 (-6.55%)</td><td>135.48 (+18.73%)</td><td>99.28 (+7.01%)</td><td>72.28 (+3.28%)</td><td>76.28 (+18.97%)</td><td>51.91 (-2.32%)</td><td>19.81 (+17.37%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.27 (n/a)</td><td>0.96 (n/a)</td><td>0.88 (n/a)</td><td>0.73 (n/a)</td><td>0.23 (n/a)</td><td>631.40 (n/a)</td><td>501.28 (n/a)</td><td>523.30 (n/a)</td><td>361.70 (n/a)</td><td>114.11 (n/a)</td><td>92.78 (n/a)</td><td>69.98 (n/a)</td><td>64.12 (n/a)</td><td>53.14 (n/a)</td><td>16.88 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.47 <b>(-22.01%)</b></td><td>1.09 (+7.53%)</td><td>1.40 <b>(+37.51%)</b></td><td>0.33 <b>(+73.42%)</b></td><td>0.50 (-18.33%)</td><td>1987.30 <b>(-42.34%)</b></td><td>827.82 <b>(-28.38%)</b></td><td>469.40 <b>(-27.27%)</b></td><td>444.50 <b>(+28.25%)</b></td><td>662.42 <b>(-48.61%)</b></td><td>150.99 <b>(-22.01%)</b></td><td>111.83 (+7.53%)</td><td>142.98 <b>(+37.51%)</b></td><td>33.77 <b>(+73.42%)</b></td><td>50.77 (-18.33%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.89 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.19 (n/a)</td><td>0.61 (n/a)</td><td>3446.40 (n/a)</td><td>1155.78 (n/a)</td><td>645.40 (n/a)</td><td>346.60 (n/a)</td><td>1288.92 (n/a)</td><td>193.61 (n/a)</td><td>103.99 (n/a)</td><td>103.98 (n/a)</td><td>19.47 (n/a)</td><td>62.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.84 (+3.06%)</td><td>1.62 (+19.47%)</td><td>1.57 (+10.52%)</td><td>1.43 <b>(+39.72%)</b></td><td>0.17 <b>(-43.05%)</b></td><td>525.50 <b>(-28.44%)</b></td><td>468.08 (-18.85%)</td><td>479.40 (-9.51%)</td><td>408.60 (-2.97%)</td><td>49.08 <b>(-61.54%)</b></td><td>205.32 (+3.06%)</td><td>180.84 (+19.47%)</td><td>175.00 (+10.52%)</td><td>159.62 <b>(+39.72%)</b></td><td>19.32 <b>(-43.05%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.79 (n/a)</td><td>1.36 (n/a)</td><td>1.42 (n/a)</td><td>1.03 (n/a)</td><td>0.30 (n/a)</td><td>734.30 (n/a)</td><td>576.80 (n/a)</td><td>529.80 (n/a)</td><td>421.10 (n/a)</td><td>127.62 (n/a)</td><td>199.23 (n/a)</td><td>151.36 (n/a)</td><td>158.34 (n/a)</td><td>114.24 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.85 (+8.45%)</td><td>1.44 <b>(+25.86%)</b></td><td>1.33 (+11.58%)</td><td>1.09 <b>(+266.88%)</b></td><td>0.34 <b>(-43.49%)</b></td><td>957.80 <b>(-72.74%)</b></td><td>762.22 <b>(-44.89%)</b></td><td>785.60 (-10.38%)</td><td>565.40 (-7.80%)</td><td>173.95 <b>(-85.78%)</b></td><td>237.39 (+8.45%)</td><td>183.99 <b>(+25.86%)</b></td><td>170.85 (+11.58%)</td><td>140.13 <b>(+266.88%)</b></td><td>43.59 <b>(-43.49%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.71 (n/a)</td><td>1.14 (n/a)</td><td>1.20 (n/a)</td><td>0.30 (n/a)</td><td>0.60 (n/a)</td><td>3514.00 (n/a)</td><td>1383.10 (n/a)</td><td>876.60 (n/a)</td><td>613.20 (n/a)</td><td>1222.97 (n/a)</td><td>218.89 (n/a)</td><td>146.19 (n/a)</td><td>153.12 (n/a)</td><td>38.20 (n/a)</td><td>77.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.34 (+10.30%)</td><td>2.17 <b>(+64.45%)</b></td><td>2.21 <b>(+46.96%)</b></td><td>1.89 <b>(+538.21%)</b></td><td>0.17 <b>(-77.23%)</b></td><td>554.40 <b>(-84.33%)</b></td><td>484.90 <b>(-62.74%)</b></td><td>474.70 <b>(-31.94%)</b></td><td>448.80 (-9.33%)</td><td>40.49 <b>(-96.84%)</b></td><td>299.06 (+10.30%)</td><td>278.23 <b>(+64.45%)</b></td><td>282.76 <b>(+46.96%)</b></td><td>242.10 <b>(+538.21%)</b></td><td>21.43 <b>(-77.23%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.12 (n/a)</td><td>1.32 (n/a)</td><td>1.50 (n/a)</td><td>0.30 (n/a)</td><td>0.74 (n/a)</td><td>3538.20 (n/a)</td><td>1301.30 (n/a)</td><td>697.50 (n/a)</td><td>495.00 (n/a)</td><td>1279.96 (n/a)</td><td>271.15 (n/a)</td><td>169.19 (n/a)</td><td>192.42 (n/a)</td><td>37.93 (n/a)</td><td>94.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.46 <b>(+20.93%)</b></td><td>1.68 (+19.22%)</td><td>1.76 <b>(+29.92%)</b></td><td>0.30 <b>(-68.63%)</b></td><td>0.88 <b>(+124.67%)</b></td><td>3540.70 <b>(+218.72%)</b></td><td>1141.58 <b>(+44.72%)</b></td><td>596.90 <b>(-23.02%)</b></td><td>426.20 (-17.31%)</td><td>1346.39 <b>(+535.36%)</b></td><td>314.91 <b>(+20.93%)</b></td><td>215.18 (+19.22%)</td><td>224.88 <b>(+29.92%)</b></td><td>37.91 <b>(-68.63%)</b></td><td>112.90 <b>(+124.67%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.03 (n/a)</td><td>1.41 (n/a)</td><td>1.35 (n/a)</td><td>0.94 (n/a)</td><td>0.39 (n/a)</td><td>1110.90 (n/a)</td><td>788.82 (n/a)</td><td>775.40 (n/a)</td><td>515.40 (n/a)</td><td>211.91 (n/a)</td><td>260.41 (n/a)</td><td>180.50 (n/a)</td><td>173.09 (n/a)</td><td>120.82 (n/a)</td><td>50.25 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.92 (+1.22%)</td><td>1.16 (+8.43%)</td><td>1.19 (+14.86%)</td><td>0.30 <b>(-29.89%)</b></td><td>0.61 (+14.10%)</td><td>3507.30 <b>(+42.64%)</b></td><td>1354.14 (+10.33%)</td><td>878.50 (-12.94%)</td><td>545.60 (-1.21%)</td><td>1222.25 <b>(+69.01%)</b></td><td>246.01 (+1.22%)</td><td>148.76 (+8.43%)</td><td>152.78 (+14.86%)</td><td>38.27 <b>(-29.89%)</b></td><td>77.47 (+14.10%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.90 (n/a)</td><td>1.07 (n/a)</td><td>1.04 (n/a)</td><td>0.43 (n/a)</td><td>0.53 (n/a)</td><td>2458.90 (n/a)</td><td>1227.30 (n/a)</td><td>1009.10 (n/a)</td><td>552.30 (n/a)</td><td>723.19 (n/a)</td><td>243.03 (n/a)</td><td>137.20 (n/a)</td><td>133.01 (n/a)</td><td>54.58 (n/a)</td><td>67.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.82 (-2.64%)</td><td>1.58 (+16.28%)</td><td>1.68 <b>(+29.73%)</b></td><td>1.24 <b>(+39.45%)</b></td><td>0.24 <b>(-34.87%)</b></td><td>845.80 <b>(-28.29%)</b></td><td>675.26 (-17.44%)</td><td>624.50 <b>(-22.91%)</b></td><td>576.10 (+2.71%)</td><td>110.70 <b>(-52.29%)</b></td><td>232.97 (-2.64%)</td><td>202.73 (+16.28%)</td><td>214.93 <b>(+29.73%)</b></td><td>158.69 <b>(+39.45%)</b></td><td>30.37 <b>(-34.87%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.87 (n/a)</td><td>1.36 (n/a)</td><td>1.29 (n/a)</td><td>0.89 (n/a)</td><td>0.36 (n/a)</td><td>1179.50 (n/a)</td><td>817.86 (n/a)</td><td>810.10 (n/a)</td><td>560.90 (n/a)</td><td>232.03 (n/a)</td><td>239.29 (n/a)</td><td>174.35 (n/a)</td><td>165.68 (n/a)</td><td>113.79 (n/a)</td><td>46.62 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.10 <b>(+33.30%)</b></td><td>1.44 <b>(+34.92%)</b></td><td>1.23 (+13.67%)</td><td>1.19 <b>(+140.68%)</b></td><td>0.39 <b>(-24.20%)</b></td><td>884.40 <b>(-58.45%)</b></td><td>763.68 <b>(-37.82%)</b></td><td>849.70 (-12.03%)</td><td>499.80 <b>(-24.98%)</b></td><td>163.53 <b>(-75.22%)</b></td><td>268.54 <b>(+33.30%)</b></td><td>184.17 <b>(+34.92%)</b></td><td>157.95 (+13.67%)</td><td>151.77 <b>(+140.68%)</b></td><td>49.57 <b>(-24.20%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.57 (n/a)</td><td>1.07 (n/a)</td><td>1.09 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>2128.50 (n/a)</td><td>1228.24 (n/a)</td><td>965.90 (n/a)</td><td>666.20 (n/a)</td><td>659.84 (n/a)</td><td>201.45 (n/a)</td><td>136.50 (n/a)</td><td>138.96 (n/a)</td><td>63.06 (n/a)</td><td>65.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.15 (+4.41%)</td><td>0.89 (+14.60%)</td><td>1.00 <b>(+45.96%)</b></td><td>0.46 (-7.97%)</td><td>0.26 (-3.97%)</td><td>779.00 (+8.66%)</td><td>448.58 (-12.42%)</td><td>360.20 <b>(-31.48%)</b></td><td>312.30 (-4.23%)</td><td>189.54 (+9.22%)</td><td>53.71 (+4.41%)</td><td>41.46 (+14.60%)</td><td>46.58 <b>(+45.96%)</b></td><td>21.54 (-7.97%)</td><td>12.31 (-3.97%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.11 (n/a)</td><td>0.78 (n/a)</td><td>0.69 (n/a)</td><td>0.50 (n/a)</td><td>0.28 (n/a)</td><td>716.90 (n/a)</td><td>512.18 (n/a)</td><td>525.70 (n/a)</td><td>326.10 (n/a)</td><td>173.53 (n/a)</td><td>51.44 (n/a)</td><td>36.18 (n/a)</td><td>31.91 (n/a)</td><td>23.40 (n/a)</td><td>12.82 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.18 (+6.74%)</td><td>2.65 (+8.21%)</td><td>2.87 (+2.49%)</td><td>1.77 (+5.23%)</td><td>0.55 (-11.27%)</td><td>2366.60 (-4.97%)</td><td>1651.20 (-9.05%)</td><td>1461.60 (-2.42%)</td><td>1320.60 (-6.31%)</td><td>422.91 (-17.70%)</td><td>813.08 (+6.74%)</td><td>679.00 (+8.21%)</td><td>734.64 (+2.49%)</td><td>453.70 (+5.23%)</td><td>141.76 (-11.27%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.98 (n/a)</td><td>2.45 (n/a)</td><td>2.80 (n/a)</td><td>1.68 (n/a)</td><td>0.62 (n/a)</td><td>2490.40 (n/a)</td><td>1815.56 (n/a)</td><td>1497.90 (n/a)</td><td>1409.50 (n/a)</td><td>513.88 (n/a)</td><td>761.77 (n/a)</td><td>627.48 (n/a)</td><td>716.82 (n/a)</td><td>431.15 (n/a)</td><td>159.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.36 (+2.35%)</td><td>3.38 <b>(+21.29%)</b></td><td>4.07 <b>(+56.03%)</b></td><td>1.20 <b>(+61.11%)</b></td><td>1.31 (-4.77%)</td><td>2184.60 <b>(-37.93%)</b></td><td>980.90 <b>(-28.74%)</b></td><td>643.80 <b>(-35.91%)</b></td><td>600.90 (-2.29%)</td><td>679.94 <b>(-43.98%)</b></td><td>893.50 (+2.35%)</td><td>692.33 <b>(+21.29%)</b></td><td>833.86 <b>(+56.03%)</b></td><td>245.76 <b>(+61.11%)</b></td><td>269.13 (-4.77%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.26 (n/a)</td><td>2.79 (n/a)</td><td>2.61 (n/a)</td><td>0.74 (n/a)</td><td>1.38 (n/a)</td><td>3519.50 (n/a)</td><td>1376.52 (n/a)</td><td>1004.60 (n/a)</td><td>615.00 (n/a)</td><td>1213.81 (n/a)</td><td>872.97 (n/a)</td><td>570.79 (n/a)</td><td>534.43 (n/a)</td><td>152.54 (n/a)</td><td>282.61 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.77 (+3.49%)</td><td>3.24 (+13.04%)</td><td>2.98 (+4.40%)</td><td>2.80 <b>(+35.07%)</b></td><td>0.45 (-19.98%)</td><td>2809.50 <b>(-25.96%)</b></td><td>2467.64 (-13.12%)</td><td>2635.80 (-4.22%)</td><td>2085.30 (-3.37%)</td><td>330.13 <b>(-44.79%)</b></td><td>1158.53 (+3.49%)</td><td>993.82 (+13.04%)</td><td>916.59 (+4.40%)</td><td>859.91 <b>(+35.07%)</b></td><td>138.33 (-19.98%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.64 (n/a)</td><td>2.86 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.56 (n/a)</td><td>3794.70 (n/a)</td><td>2840.14 (n/a)</td><td>2751.90 (n/a)</td><td>2158.10 (n/a)</td><td>597.93 (n/a)</td><td>1119.47 (n/a)</td><td>879.15 (n/a)</td><td>877.92 (n/a)</td><td>636.65 (n/a)</td><td>172.87 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.00 (n/a)</td><td>285.28 (n/a)</td><td>249.30 (n/a)</td><td>223.20 (n/a)</td><td>101.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2461.80 (n/a)</td><td>1042.96 (n/a)</td><td>285.60 (n/a)</td><td>275.90 (n/a)</td><td>1063.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.30 (n/a)</td><td>423.86 (n/a)</td><td>489.60 (n/a)</td><td>232.80 (n/a)</td><td>150.45 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>742.90 (n/a)</td><td>359.66 (n/a)</td><td>259.60 (n/a)</td><td>242.00 (n/a)</td><td>215.26 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2473.00 (n/a)</td><td>816.78 (n/a)</td><td>485.90 (n/a)</td><td>220.30 (n/a)</td><td>932.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.20 (n/a)</td><td>480.02 (n/a)</td><td>526.80 (n/a)</td><td>288.50 (n/a)</td><td>114.40 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>459.30 (n/a)</td><td>320.44 (n/a)</td><td>295.80 (n/a)</td><td>265.30 (n/a)</td><td>80.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.70 (n/a)</td><td>553.06 (n/a)</td><td>566.50 (n/a)</td><td>477.80 (n/a)</td><td>56.44 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.80 (n/a)</td><td>376.56 (n/a)</td><td>362.80 (n/a)</td><td>218.20 (n/a)</td><td>138.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1915.60 (n/a)</td><td>712.88 (n/a)</td><td>472.00 (n/a)</td><td>274.10 (n/a)</td><td>684.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>457.20 (n/a)</td><td>325.90 (n/a)</td><td>290.60 (n/a)</td><td>272.70 (n/a)</td><td>75.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1004.60 (n/a)</td><td>529.54 (n/a)</td><td>493.20 (n/a)</td><td>238.80 (n/a)</td><td>286.44 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1830.00 (n/a)</td><td>693.42 (n/a)</td><td>497.00 (n/a)</td><td>294.80 (n/a)</td><td>644.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.10 (n/a)</td><td>413.80 (n/a)</td><td>301.00 (n/a)</td><td>250.30 (n/a)</td><td>180.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>606.50 (n/a)</td><td>338.90 (n/a)</td><td>300.30 (n/a)</td><td>151.50 (n/a)</td><td>167.99 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2101.90 (n/a)</td><td>680.76 (n/a)</td><td>292.10 (n/a)</td><td>180.30 (n/a)</td><td>808.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>585.90 (n/a)</td><td>419.06 (n/a)</td><td>437.70 (n/a)</td><td>218.80 (n/a)</td><td>164.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1894.80 (n/a)</td><td>741.42 (n/a)</td><td>578.90 (n/a)</td><td>301.90 (n/a)</td><td>659.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>304.10 (n/a)</td><td>284.48 (n/a)</td><td>273.40 (n/a)</td><td>271.20 (n/a)</td><td>16.72 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>526.50 (n/a)</td><td>389.88 (n/a)</td><td>496.10 (n/a)</td><td>169.20 (n/a)</td><td>165.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.80 (n/a)</td><td>384.02 (n/a)</td><td>285.50 (n/a)</td><td>257.10 (n/a)</td><td>158.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>565.60 (n/a)</td><td>358.24 (n/a)</td><td>304.40 (n/a)</td><td>231.70 (n/a)</td><td>142.30 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>585.90 (n/a)</td><td>364.86 (n/a)</td><td>293.40 (n/a)</td><td>273.00 (n/a)</td><td>130.85 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>613.00 (n/a)</td><td>440.70 (n/a)</td><td>499.50 (n/a)</td><td>273.80 (n/a)</td><td>144.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.52 (-17.27%)</td><td>0.43 (-1.43%)</td><td>0.43 <b>(+24.19%)</b></td><td>0.33 (+17.33%)</td><td>0.07 <b>(-55.49%)</b></td><td>673.80 (-14.76%)</td><td>529.92 (-6.03%)</td><td>513.90 (-19.48%)</td><td>427.40 <b>(+20.87%)</b></td><td>91.52 <b>(-51.19%)</b></td><td>22.08 (-17.27%)</td><td>18.21 (-1.43%)</td><td>18.36 <b>(+24.19%)</b></td><td>14.01 (+17.33%)</td><td>2.95 <b>(-55.49%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.63 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>790.50 (n/a)</td><td>563.90 (n/a)</td><td>638.20 (n/a)</td><td>353.60 (n/a)</td><td>187.50 (n/a)</td><td>26.69 (n/a)</td><td>18.47 (n/a)</td><td>14.79 (n/a)</td><td>11.94 (n/a)</td><td>6.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.58 (+14.92%)</td><td>0.43 (+10.12%)</td><td>0.48 (+6.82%)</td><td>0.23 <b>(+35.24%)</b></td><td>0.13 (+2.96%)</td><td>942.90 <b>(-26.06%)</b></td><td>575.74 (-13.41%)</td><td>461.20 (-6.39%)</td><td>381.80 (-12.99%)</td><td>225.69 <b>(-35.22%)</b></td><td>24.72 (+14.92%)</td><td>18.14 (+10.12%)</td><td>20.46 (+6.82%)</td><td>10.01 <b>(+35.24%)</b></td><td>5.75 (+2.96%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.45 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>1275.20 (n/a)</td><td>664.88 (n/a)</td><td>492.70 (n/a)</td><td>438.80 (n/a)</td><td>348.38 (n/a)</td><td>21.51 (n/a)</td><td>16.47 (n/a)</td><td>19.15 (n/a)</td><td>7.40 (n/a)</td><td>5.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.31 (-1.65%)</td><td>0.30 (-0.26%)</td><td>0.30 (+1.27%)</td><td>0.29 (-1.78%)</td><td>0.01 (-4.46%)</td><td>86041.70 (+1.81%)</td><td>83376.92 (+0.26%)</td><td>82981.50 (-1.25%)</td><td>82244.10 (+1.68%)</td><td>1541.34 (-0.91%)</td><td>208.89 (-1.65%)</td><td>206.11 (-0.26%)</td><td>207.03 (+1.27%)</td><td>199.67 (-1.78%)</td><td>3.73 (-4.46%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84510.00 (n/a)</td><td>83161.34 (n/a)</td><td>84031.80 (n/a)</td><td>80885.20 (n/a)</td><td>1555.57 (n/a)</td><td>212.40 (n/a)</td><td>206.64 (n/a)</td><td>204.44 (n/a)</td><td>203.29 (n/a)</td><td>3.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.17 (+0.13%)</td><td>1.14 (-0.37%)</td><td>1.15 (-0.39%)</td><td>1.12 (+0.90%)</td><td>0.02 (-4.51%)</td><td>22459.90 (-0.89%)</td><td>22038.34 (+0.37%)</td><td>21951.50 (+0.39%)</td><td>21479.80 (-0.13%)</td><td>401.72 (-5.67%)</td><td>799.82 (+0.13%)</td><td>779.75 (-0.37%)</td><td>782.63 (-0.39%)</td><td>764.91 (+0.90%)</td><td>14.27 (-4.51%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.17 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22661.10 (n/a)</td><td>21958.00 (n/a)</td><td>21866.20 (n/a)</td><td>21508.00 (n/a)</td><td>425.86 (n/a)</td><td>798.77 (n/a)</td><td>782.63 (n/a)</td><td>785.68 (n/a)</td><td>758.12 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.80 (+0.17%)</td><td>0.79 (-0.55%)</td><td>0.79 (-0.44%)</td><td>0.77 (-1.50%)</td><td>0.01 <b>(+91.63%)</b></td><td>97509.90 (+1.53%)</td><td>95498.30 (+0.56%)</td><td>95222.70 (+0.44%)</td><td>94390.60 (-0.17%)</td><td>1190.83 <b>(+94.56%)</b></td><td>728.03 (+0.17%)</td><td>719.68 (-0.55%)</td><td>721.67 (-0.44%)</td><td>704.74 (-1.50%)</td><td>8.87 <b>(+91.63%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>96042.70 (n/a)</td><td>94968.62 (n/a)</td><td>94806.50 (n/a)</td><td>94549.30 (n/a)</td><td>612.07 (n/a)</td><td>726.81 (n/a)</td><td>723.63 (n/a)</td><td>724.84 (n/a)</td><td>715.51 (n/a)</td><td>4.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.78 (+0.59%)</td><td>0.77 (+0.36%)</td><td>0.77 (+0.40%)</td><td>0.76 (+0.03%)</td><td>0.01 (+19.09%)</td><td>99090.50 (-0.03%)</td><td>97938.96 (-0.36%)</td><td>98257.00 (-0.40%)</td><td>96517.20 (-0.58%)</td><td>977.74 (+18.30%)</td><td>711.99 (+0.59%)</td><td>701.71 (+0.36%)</td><td>699.38 (+0.40%)</td><td>693.50 (+0.03%)</td><td>7.03 (+19.09%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99120.00 (n/a)</td><td>98287.94 (n/a)</td><td>98650.90 (n/a)</td><td>97084.20 (n/a)</td><td>826.49 (n/a)</td><td>707.83 (n/a)</td><td>699.20 (n/a)</td><td>696.59 (n/a)</td><td>693.30 (n/a)</td><td>5.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.90 (+0.15%)</td><td>0.89 (-0.11%)</td><td>0.89 (+0.77%)</td><td>0.87 (-1.30%)</td><td>0.01 <b>(+50.84%)</b></td><td>87097.50 (+1.31%)</td><td>85126.94 (+0.12%)</td><td>84546.30 (-0.77%)</td><td>84065.00 (-0.15%)</td><td>1209.68 <b>(+53.08%)</b></td><td>817.46 (+0.15%)</td><td>807.39 (-0.11%)</td><td>812.80 (+0.77%)</td><td>788.99 (-1.30%)</td><td>11.34 <b>(+50.84%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85967.90 (n/a)</td><td>85026.26 (n/a)</td><td>85198.30 (n/a)</td><td>84192.10 (n/a)</td><td>790.21 (n/a)</td><td>816.22 (n/a)</td><td>808.27 (n/a)</td><td>806.58 (n/a)</td><td>799.36 (n/a)</td><td>7.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.65 (-3.92%)</td><td>4.09 (-3.20%)</td><td>4.10 (+1.72%)</td><td>2.16 (-1.06%)</td><td>1.26 (-9.50%)</td><td>4123.40 (+1.07%)</td><td>2411.62 (+2.09%)</td><td>2173.80 (-1.69%)</td><td>1578.30 (+4.08%)</td><td>990.98 (-1.92%)</td><td>340.16 (-3.92%)</td><td>246.65 (-3.20%)</td><td>246.98 (+1.72%)</td><td>130.20 (-1.06%)</td><td>76.15 (-9.50%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.88 (n/a)</td><td>4.23 (n/a)</td><td>4.03 (n/a)</td><td>2.18 (n/a)</td><td>1.40 (n/a)</td><td>4079.90 (n/a)</td><td>2362.20 (n/a)</td><td>2211.20 (n/a)</td><td>1516.50 (n/a)</td><td>1010.33 (n/a)</td><td>354.02 (n/a)</td><td>254.80 (n/a)</td><td>242.80 (n/a)</td><td>131.59 (n/a)</td><td>84.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.73 (+0.47%)</td><td>2.76 <b>(-21.35%)</b></td><td>2.27 <b>(-34.60%)</b></td><td>2.17 (+3.75%)</td><td>1.11 (-2.54%)</td><td>4098.10 (-3.61%)</td><td>3529.30 <b>(+26.47%)</b></td><td>3927.20 <b>(+52.90%)</b></td><td>1883.80 (-0.46%)</td><td>938.72 (-5.30%)</td><td>284.99 (+0.47%)</td><td>166.24 <b>(-21.35%)</b></td><td>136.71 <b>(-34.60%)</b></td><td>131.00 (+3.75%)</td><td>66.72 (-2.54%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.71 (n/a)</td><td>3.51 (n/a)</td><td>3.47 (n/a)</td><td>2.10 (n/a)</td><td>1.14 (n/a)</td><td>4251.60 (n/a)</td><td>2790.54 (n/a)</td><td>2568.50 (n/a)</td><td>1892.60 (n/a)</td><td>991.21 (n/a)</td><td>283.66 (n/a)</td><td>211.38 (n/a)</td><td>209.03 (n/a)</td><td>126.27 (n/a)</td><td>68.46 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.91 (+2.54%)</td><td>4.33 (+14.37%)</td><td>4.41 (+9.38%)</td><td>2.20 (-1.79%)</td><td>1.35 (-1.74%)</td><td>4052.00 (+1.82%)</td><td>2299.04 (-12.33%)</td><td>2020.70 (-8.57%)</td><td>1507.00 (-2.48%)</td><td>1003.16 (+4.00%)</td><td>356.25 (+2.54%)</td><td>260.79 (+14.37%)</td><td>265.69 (+9.38%)</td><td>132.49 (-1.79%)</td><td>81.05 (-1.74%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.77 (n/a)</td><td>3.79 (n/a)</td><td>4.03 (n/a)</td><td>2.24 (n/a)</td><td>1.37 (n/a)</td><td>3979.50 (n/a)</td><td>2622.38 (n/a)</td><td>2210.10 (n/a)</td><td>1545.30 (n/a)</td><td>964.60 (n/a)</td><td>347.42 (n/a)</td><td>228.03 (n/a)</td><td>242.92 (n/a)</td><td>134.91 (n/a)</td><td>82.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.63 (+3.38%)</td><td>5.87 (+5.05%)</td><td>6.25 (+5.08%)</td><td>4.44 (+2.19%)</td><td>0.88 (+0.90%)</td><td>7859.30 (-2.14%)</td><td>6068.46 (-4.85%)</td><td>5581.20 (-4.83%)</td><td>5255.40 (-3.27%)</td><td>1061.33 (-2.88%)</td><td>408.62 (+3.38%)</td><td>361.45 (+5.05%)</td><td>384.77 (+5.08%)</td><td>273.24 (+2.19%)</td><td>54.40 (+0.90%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.42 (n/a)</td><td>5.59 (n/a)</td><td>5.94 (n/a)</td><td>4.34 (n/a)</td><td>0.88 (n/a)</td><td>8031.30 (n/a)</td><td>6377.62 (n/a)</td><td>5864.60 (n/a)</td><td>5433.10 (n/a)</td><td>1092.83 (n/a)</td><td>395.26 (n/a)</td><td>344.08 (n/a)</td><td>366.17 (n/a)</td><td>267.39 (n/a)</td><td>53.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.38 (-9.94%)</td><td>4.82 (+0.70%)</td><td>5.20 (+8.74%)</td><td>4.02 (+0.85%)</td><td>0.62 <b>(-20.72%)</b></td><td>8681.30 (-0.85%)</td><td>7342.38 (-1.31%)</td><td>6704.70 (-8.04%)</td><td>6478.30 (+11.04%)</td><td>1001.56 (-13.18%)</td><td>331.49 (-9.94%)</td><td>296.65 (+0.70%)</td><td>320.29 (+8.74%)</td><td>247.37 (+0.85%)</td><td>38.32 <b>(-20.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.98 (n/a)</td><td>4.78 (n/a)</td><td>4.78 (n/a)</td><td>3.98 (n/a)</td><td>0.78 (n/a)</td><td>8755.40 (n/a)</td><td>7439.72 (n/a)</td><td>7290.60 (n/a)</td><td>5834.10 (n/a)</td><td>1153.66 (n/a)</td><td>368.09 (n/a)</td><td>294.60 (n/a)</td><td>294.56 (n/a)</td><td>245.27 (n/a)</td><td>48.33 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.13 (+17.37%)</td><td>5.57 (-2.82%)</td><td>5.89 (+2.79%)</td><td>4.34 (-17.77%)</td><td>1.19 <b>(+289.62%)</b></td><td>8038.40 <b>(+21.61%)</b></td><td>6498.72 (+6.57%)</td><td>5922.30 (-2.71%)</td><td>4890.40 (-14.80%)</td><td>1404.83 <b>(+320.97%)</b></td><td>439.12 (+17.37%)</td><td>343.03 (-2.82%)</td><td>362.61 (+2.79%)</td><td>267.15 (-17.77%)</td><td>73.39 <b>(+289.62%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.07 (n/a)</td><td>5.73 (n/a)</td><td>5.73 (n/a)</td><td>5.27 (n/a)</td><td>0.31 (n/a)</td><td>6610.00 (n/a)</td><td>6097.80 (n/a)</td><td>6087.30 (n/a)</td><td>5740.00 (n/a)</td><td>333.71 (n/a)</td><td>374.13 (n/a)</td><td>353.00 (n/a)</td><td>352.78 (n/a)</td><td>324.88 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.78 (-0.50%)</td><td>0.76 (-0.76%)</td><td>0.77 (-0.72%)</td><td>0.75 (-1.11%)</td><td>0.01 (+7.49%)</td><td>101149.40 (+1.12%)</td><td>98762.56 (+0.77%)</td><td>98587.00 (+0.73%)</td><td>97342.30 (+0.51%)</td><td>1428.45 (+9.68%)</td><td>705.96 (-0.50%)</td><td>695.92 (-0.76%)</td><td>697.04 (-0.72%)</td><td>679.39 (-1.11%)</td><td>9.94 (+7.49%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100027.90 (n/a)</td><td>98005.72 (n/a)</td><td>97872.50 (n/a)</td><td>96851.40 (n/a)</td><td>1302.43 (n/a)</td><td>709.54 (n/a)</td><td>701.28 (n/a)</td><td>702.13 (n/a)</td><td>687.00 (n/a)</td><td>9.25 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.76 (-3.12%)</td><td>0.75 (-0.67%)</td><td>0.75 (-0.30%)</td><td>0.75 (+0.13%)</td><td>0.01 <b>(-65.65%)</b></td><td>101255.00 (-0.13%)</td><td>100412.68 (+0.65%)</td><td>100573.10 (+0.30%)</td><td>99314.10 (+3.22%)</td><td>725.31 <b>(-64.46%)</b></td><td>691.94 (-3.12%)</td><td>684.40 (-0.67%)</td><td>683.28 (-0.30%)</td><td>678.68 (+0.13%)</td><td>4.96 <b>(-65.65%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101384.10 (n/a)</td><td>99766.70 (n/a)</td><td>100271.50 (n/a)</td><td>96214.80 (n/a)</td><td>2041.10 (n/a)</td><td>714.23 (n/a)</td><td>689.04 (n/a)</td><td>685.33 (n/a)</td><td>677.81 (n/a)</td><td>14.44 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.89 (-0.81%)</td><td>0.88 (+0.20%)</td><td>0.88 (-0.09%)</td><td>0.87 (+2.28%)</td><td>0.01 <b>(-63.03%)</b></td><td>86347.80 (-2.23%)</td><td>85471.28 (-0.23%)</td><td>85396.50 (+0.09%)</td><td>84684.10 (+0.82%)</td><td>673.41 <b>(-63.47%)</b></td><td>811.48 (-0.81%)</td><td>804.05 (+0.20%)</td><td>804.71 (-0.09%)</td><td>795.84 (+2.28%)</td><td>6.33 <b>(-63.03%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.02 (n/a)</td><td>88317.50 (n/a)</td><td>85666.42 (n/a)</td><td>85322.00 (n/a)</td><td>83998.90 (n/a)</td><td>1843.40 (n/a)</td><td>818.10 (n/a)</td><td>802.47 (n/a)</td><td>805.41 (n/a)</td><td>778.10 (n/a)</td><td>17.12 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.01 (-4.50%)</td><td>2.26 <b>(-20.78%)</b></td><td>2.04 <b>(-29.76%)</b></td><td>1.40 (-14.61%)</td><td>1.03 (-13.17%)</td><td>5759.70 (+17.11%)</td><td>4066.62 <b>(+22.94%)</b></td><td>3955.10 <b>(+42.38%)</b></td><td>2012.00 (+4.71%)</td><td>1424.11 (-2.52%)</td><td>1050.68 (-4.50%)</td><td>591.83 <b>(-20.78%)</b></td><td>534.48 <b>(-29.76%)</b></td><td>367.02 (-14.61%)</td><td>270.33 (-13.17%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.20 (n/a)</td><td>2.85 (n/a)</td><td>2.90 (n/a)</td><td>1.64 (n/a)</td><td>1.19 (n/a)</td><td>4918.30 (n/a)</td><td>3307.78 (n/a)</td><td>2777.90 (n/a)</td><td>1921.50 (n/a)</td><td>1460.98 (n/a)</td><td>1100.17 (n/a)</td><td>747.10 (n/a)</td><td>760.99 (n/a)</td><td>429.81 (n/a)</td><td>311.33 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.23 <b>(-29.09%)</b></td><td>0.20 (-13.95%)</td><td>0.19 (-13.29%)</td><td>0.18 (-9.48%)</td><td>0.02 <b>(-52.88%)</b></td><td>6820.40 (+10.48%)</td><td>6203.28 (+13.93%)</td><td>6587.00 (+15.33%)</td><td>5407.20 <b>(+41.01%)</b></td><td>707.77 <b>(-25.86%)</b></td><td>12.41 <b>(-29.09%)</b></td><td>10.94 (-13.95%)</td><td>10.19 (-13.29%)</td><td>9.84 (-9.48%)</td><td>1.30 <b>(-52.88%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>6173.70 (n/a)</td><td>5444.60 (n/a)</td><td>5711.60 (n/a)</td><td>3834.50 (n/a)</td><td>954.65 (n/a)</td><td>17.50 (n/a)</td><td>12.71 (n/a)</td><td>11.75 (n/a)</td><td>10.87 (n/a)</td><td>2.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.79 (n/a)</td><td>3.60 (n/a)</td><td>3.62 (n/a)</td><td>3.34 (n/a)</td><td>0.17 (n/a)</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.62 (n/a)</td><td>3.34 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.42 (-0.64%)</td><td>6.34 (+2.78%)</td><td>5.77 (+1.71%)</td><td>5.58 (-0.12%)</td><td>0.90 (+9.01%)</td><td>7.42 (-0.64%)</td><td>6.34 (+2.78%)</td><td>5.77 (+1.71%)</td><td>5.57 (-0.12%)</td><td>0.90 (+9.01%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.47 (n/a)</td><td>6.17 (n/a)</td><td>5.67 (n/a)</td><td>5.58 (n/a)</td><td>0.82 (n/a)</td><td>7.46 (n/a)</td><td>6.17 (n/a)</td><td>5.67 (n/a)</td><td>5.58 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>13.44 (-2.83%)</td><td>10.60 (+5.58%)</td><td>9.98 (+9.29%)</td><td>7.78 (-9.34%)</td><td>2.64 <b>(+22.86%)</b></td><td>13.43 (-2.83%)</td><td>10.59 (+5.58%)</td><td>9.97 (+9.29%)</td><td>7.78 (-9.34%)</td><td>2.64 <b>(+22.86%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>13.83 (n/a)</td><td>10.04 (n/a)</td><td>9.13 (n/a)</td><td>8.58 (n/a)</td><td>2.15 (n/a)</td><td>13.82 (n/a)</td><td>10.03 (n/a)</td><td>9.13 (n/a)</td><td>8.58 (n/a)</td><td>2.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.84 (n/a)</td><td>3.65 (n/a)</td><td>3.68 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td><td>3.84 (n/a)</td><td>3.64 (n/a)</td><td>3.68 (n/a)</td><td>3.43 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.19 (+2.14%)</td><td>6.31 (+6.16%)</td><td>6.20 (+1.42%)</td><td>5.68 <b>(+27.20%)</b></td><td>0.66 <b>(-40.64%)</b></td><td>7.18 (+2.14%)</td><td>6.31 (+6.16%)</td><td>6.19 (+1.42%)</td><td>5.68 <b>(+27.20%)</b></td><td>0.66 <b>(-40.64%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.04 (n/a)</td><td>5.95 (n/a)</td><td>6.11 (n/a)</td><td>4.47 (n/a)</td><td>1.10 (n/a)</td><td>7.03 (n/a)</td><td>5.94 (n/a)</td><td>6.11 (n/a)</td><td>4.46 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>8.47 <b>(-39.42%)</b></td><td>8.13 (-12.54%)</td><td>8.18 (-0.48%)</td><td>7.71 (+0.26%)</td><td>0.34 <b>(-87.14%)</b></td><td>8.46 <b>(-39.42%)</b></td><td>8.12 (-12.54%)</td><td>8.18 (-0.48%)</td><td>7.71 (+0.26%)</td><td>0.34 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>13.98 (n/a)</td><td>9.29 (n/a)</td><td>8.22 (n/a)</td><td>7.69 (n/a)</td><td>2.63 (n/a)</td><td>13.97 (n/a)</td><td>9.28 (n/a)</td><td>8.22 (n/a)</td><td>7.69 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.12 (-2.60%)</td><td>1.99 (-17.43%)</td><td>1.70 <b>(-38.07%)</b></td><td>1.00 <b>(-34.36%)</b></td><td>0.91 (+18.31%)</td><td>3.11 (-2.60%)</td><td>1.98 (-17.43%)</td><td>1.70 <b>(-38.07%)</b></td><td>1.00 <b>(-34.36%)</b></td><td>0.91 (+18.31%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.20 (n/a)</td><td>2.41 (n/a)</td><td>2.74 (n/a)</td><td>1.52 (n/a)</td><td>0.77 (n/a)</td><td>3.20 (n/a)</td><td>2.40 (n/a)</td><td>2.74 (n/a)</td><td>1.52 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.52 (-7.81%)</td><td>0.25 <b>(-37.07%)</b></td><td>0.14 <b>(-63.72%)</b></td><td>0.08 (+2.36%)</td><td>0.19 (-2.44%)</td><td>0.51 (-7.81%)</td><td>0.24 <b>(-37.07%)</b></td><td>0.14 <b>(-63.72%)</b></td><td>0.08 (+2.36%)</td><td>0.19 (-2.44%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.64 (-1.54%)</td><td>0.39 (-7.80%)</td><td>0.45 (-6.59%)</td><td>0.08 (-6.70%)</td><td>0.21 (-4.92%)</td><td>0.63 (-1.54%)</td><td>0.39 (-7.80%)</td><td>0.44 (-6.59%)</td><td>0.07 (-6.70%)</td><td>0.20 (-4.92%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.65 (n/a)</td><td>0.43 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.44 <b>(-44.51%)</b></td><td>0.76 <b>(-66.37%)</b></td><td>0.63 <b>(-73.19%)</b></td><td>0.42 <b>(-72.80%)</b></td><td>0.42 (-0.40%)</td><td>1.42 <b>(-44.51%)</b></td><td>0.75 <b>(-66.37%)</b></td><td>0.62 <b>(-73.19%)</b></td><td>0.42 <b>(-72.80%)</b></td><td>0.41 (-0.40%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.60 (n/a)</td><td>2.27 (n/a)</td><td>2.35 (n/a)</td><td>1.56 (n/a)</td><td>0.42 (n/a)</td><td>2.56 (n/a)</td><td>2.23 (n/a)</td><td>2.31 (n/a)</td><td>1.54 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1832.70 (n/a)</td><td>707.82 (n/a)</td><td>561.60 (n/a)</td><td>269.10 (n/a)</td><td>648.12 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>646.00 (n/a)</td><td>414.22 (n/a)</td><td>351.50 (n/a)</td><td>245.60 (n/a)</td><td>186.04 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.40 (n/a)</td><td>397.48 (n/a)</td><td>429.70 (n/a)</td><td>246.70 (n/a)</td><td>93.22 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1890.20 (n/a)</td><td>1119.66 (n/a)</td><td>1038.50 (n/a)</td><td>277.70 (n/a)</td><td>752.30 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.80 (n/a)</td><td>420.48 (n/a)</td><td>476.90 (n/a)</td><td>289.80 (n/a)</td><td>103.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.40 (n/a)</td><td>539.52 (n/a)</td><td>545.10 (n/a)</td><td>475.80 (n/a)</td><td>66.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.80 (n/a)</td><td>402.78 (n/a)</td><td>342.20 (n/a)</td><td>278.20 (n/a)</td><td>146.62 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1959.20 (n/a)</td><td>963.10 (n/a)</td><td>416.90 (n/a)</td><td>249.20 (n/a)</td><td>893.73 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1963.60 (n/a)</td><td>800.82 (n/a)</td><td>535.20 (n/a)</td><td>475.20 (n/a)</td><td>650.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>393.84 (n/a)</td><td>466.20 (n/a)</td><td>241.90 (n/a)</td><td>124.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>990.50 (n/a)</td><td>477.92 (n/a)</td><td>416.60 (n/a)</td><td>242.10 (n/a)</td><td>301.56 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.40 (n/a)</td><td>442.66 (n/a)</td><td>467.00 (n/a)</td><td>229.00 (n/a)</td><td>128.81 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>545.60 (n/a)</td><td>457.78 (n/a)</td><td>497.60 (n/a)</td><td>281.00 (n/a)</td><td>108.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>638.60 (n/a)</td><td>445.02 (n/a)</td><td>395.40 (n/a)</td><td>348.30 (n/a)</td><td>117.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>489.80 (n/a)</td><td>297.88 (n/a)</td><td>258.30 (n/a)</td><td>207.20 (n/a)</td><td>112.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>532.80 (n/a)</td><td>395.28 (n/a)</td><td>396.10 (n/a)</td><td>269.60 (n/a)</td><td>110.02 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.60 (n/a)</td><td>394.46 (n/a)</td><td>468.20 (n/a)</td><td>202.10 (n/a)</td><td>164.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1928.20 (n/a)</td><td>736.76 (n/a)</td><td>612.10 (n/a)</td><td>220.60 (n/a)</td><td>691.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>720.40 (n/a)</td><td>416.66 (n/a)</td><td>311.00 (n/a)</td><td>274.90 (n/a)</td><td>193.46 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>498.30 (n/a)</td><td>413.16 (n/a)</td><td>459.20 (n/a)</td><td>289.50 (n/a)</td><td>100.62 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.60 (n/a)</td><td>418.08 (n/a)</td><td>473.90 (n/a)</td><td>279.00 (n/a)</td><td>125.82 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>590.00 (n/a)</td><td>463.32 (n/a)</td><td>485.50 (n/a)</td><td>294.30 (n/a)</td><td>114.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.40 (n/a)</td><td>374.14 (n/a)</td><td>355.40 (n/a)</td><td>246.00 (n/a)</td><td>111.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>589.10 (n/a)</td><td>464.64 (n/a)</td><td>485.50 (n/a)</td><td>376.30 (n/a)</td><td>89.87 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+3.55%)</td><td>0.02 <b>(+41.76%)</b></td><td>0.02 <b>(+66.86%)</b></td><td>0.01 <b>(+31.60%)</b></td><td>0.00 (-19.49%)</td><td>420.30 <b>(-24.00%)</b></td><td>276.80 <b>(-32.76%)</b></td><td>249.50 <b>(-40.07%)</b></td><td>225.60 (-3.42%)</td><td>80.83 <b>(-39.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.00 (n/a)</td><td>411.64 (n/a)</td><td>416.30 (n/a)</td><td>233.60 (n/a)</td><td>132.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+9.18%)</td><td>0.01 <b>(+21.82%)</b></td><td>0.02 <b>(+75.38%)</b></td><td>0.00 <b>(-79.07%)</b></td><td>0.01 <b>(+102.33%)</b></td><td>2464.10 <b>(+377.91%)</b></td><td>702.42 <b>(+71.33%)</b></td><td>256.50 <b>(-42.99%)</b></td><td>237.80 (-8.43%)</td><td>985.09 <b>(+862.50%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>515.60 (n/a)</td><td>409.98 (n/a)</td><td>449.90 (n/a)</td><td>259.70 (n/a)</td><td>102.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+70.77%)</b></td><td>0.01 <b>(+47.23%)</b></td><td>0.01 (+10.89%)</td><td>0.01 <b>(+45.73%)</b></td><td>0.01 <b>(+99.43%)</b></td><td>510.30 <b>(-31.38%)</b></td><td>380.38 <b>(-27.26%)</b></td><td>441.50 (-9.82%)</td><td>163.90 <b>(-41.44%)</b></td><td>150.30 (-18.05%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>743.70 (n/a)</td><td>522.96 (n/a)</td><td>489.60 (n/a)</td><td>279.90 (n/a)</td><td>183.40 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+15.01%)</td><td>0.01 <b>(+61.08%)</b></td><td>0.01 <b>(+117.65%)</b></td><td>0.01 <b>(+320.09%)</b></td><td>0.00 (-16.70%)</td><td>461.30 <b>(-76.20%)</b></td><td>335.22 <b>(-56.72%)</b></td><td>284.40 <b>(-54.06%)</b></td><td>198.80 (-13.07%)</td><td>117.58 <b>(-82.45%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1937.90 (n/a)</td><td>774.62 (n/a)</td><td>619.10 (n/a)</td><td>228.70 (n/a)</td><td>669.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+33.86%)</b></td><td>0.01 <b>(+46.67%)</b></td><td>0.01 (+5.98%)</td><td>0.01 <b>(+437.20%)</b></td><td>0.00 (-18.11%)</td><td>449.80 <b>(-81.38%)</b></td><td>359.98 <b>(-56.45%)</b></td><td>406.10 (-5.65%)</td><td>262.90 <b>(-25.29%)</b></td><td>89.70 <b>(-89.94%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2416.30 (n/a)</td><td>826.54 (n/a)</td><td>430.40 (n/a)</td><td>351.90 (n/a)</td><td>891.96 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-11.59%)</td><td>0.01 (+2.44%)</td><td>0.01 (-4.16%)</td><td>0.01 (+14.63%)</td><td>0.00 <b>(-40.96%)</b></td><td>430.10 (-12.76%)</td><td>330.54 (-7.22%)</td><td>327.20 (+4.34%)</td><td>268.50 (+13.10%)</td><td>62.91 <b>(-43.50%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.00 (n/a)</td><td>356.26 (n/a)</td><td>313.60 (n/a)</td><td>237.40 (n/a)</td><td>111.34 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(+55.82%)</b></td><td>0.04 <b>(+51.44%)</b></td><td>0.03 <b>(+21.20%)</b></td><td>0.03 <b>(+72.46%)</b></td><td>0.01 (+3.49%)</td><td>304.50 <b>(-42.01%)</b></td><td>237.86 <b>(-37.36%)</b></td><td>243.50 (-17.49%)</td><td>173.80 <b>(-35.82%)</b></td><td>46.98 <b>(-63.40%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>379.74 (n/a)</td><td>295.10 (n/a)</td><td>270.80 (n/a)</td><td>128.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (+19.73%)</td><td>0.02 (-2.89%)</td><td>0.02 <b>(-30.65%)</b></td><td>0.02 <b>(+22.57%)</b></td><td>0.01 (+1.39%)</td><td>491.80 (-18.41%)</td><td>387.30 (-0.69%)</td><td>424.90 <b>(+44.18%)</b></td><td>221.40 (-16.48%)</td><td>104.67 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.80 (n/a)</td><td>390.00 (n/a)</td><td>294.70 (n/a)</td><td>265.10 (n/a)</td><td>155.61 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+113.58%)</b></td><td>0.02 <b>(+83.57%)</b></td><td>0.03 <b>(+72.97%)</b></td><td>0.02 <b>(+269.75%)</b></td><td>0.01 <b>(+55.15%)</b></td><td>544.40 <b>(-72.95%)</b></td><td>370.80 <b>(-55.10%)</b></td><td>313.00 <b>(-42.19%)</b></td><td>236.20 <b>(-53.18%)</b></td><td>128.90 <b>(-80.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2012.80 (n/a)</td><td>825.80 (n/a)</td><td>541.40 (n/a)</td><td>504.50 (n/a)</td><td>663.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+17.98%)</td><td>0.02 (-4.10%)</td><td>0.02 (-6.14%)</td><td>0.01 <b>(-39.67%)</b></td><td>0.01 <b>(+58.76%)</b></td><td>1109.20 <b>(+65.75%)</b></td><td>560.42 <b>(+22.36%)</b></td><td>488.40 (+6.54%)</td><td>240.80 (-15.24%)</td><td>326.89 <b>(+132.01%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>669.20 (n/a)</td><td>458.02 (n/a)</td><td>458.40 (n/a)</td><td>284.10 (n/a)</td><td>140.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(+60.15%)</b></td><td>0.03 <b>(+28.17%)</b></td><td>0.02 (+18.90%)</td><td>0.01 (+14.73%)</td><td>0.01 <b>(+86.58%)</b></td><td>567.60 (-12.84%)</td><td>375.14 (-14.94%)</td><td>392.00 (-15.88%)</td><td>181.50 <b>(-37.54%)</b></td><td>163.01 (+8.22%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.20 (n/a)</td><td>441.02 (n/a)</td><td>466.00 (n/a)</td><td>290.60 (n/a)</td><td>150.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(+83.72%)</b></td><td>0.03 (+10.01%)</td><td>0.02 <b>(-26.31%)</b></td><td>0.01 <b>(-30.96%)</b></td><td>0.02 <b>(+164.50%)</b></td><td>789.60 <b>(+44.85%)</b></td><td>423.96 (+13.40%)</td><td>410.40 <b>(+35.71%)</b></td><td>157.80 <b>(-45.59%)</b></td><td>239.66 <b>(+110.17%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.10 (n/a)</td><td>373.86 (n/a)</td><td>302.40 (n/a)</td><td>290.00 (n/a)</td><td>114.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 <b>(+26.91%)</b></td><td>0.02 (+13.54%)</td><td>0.03 <b>(+52.26%)</b></td><td>0.01 <b>(-39.01%)</b></td><td>0.01 <b>(+97.22%)</b></td><td>783.90 <b>(+63.96%)</b></td><td>457.52 (+12.08%)</td><td>298.30 <b>(-34.34%)</b></td><td>193.50 <b>(-21.21%)</b></td><td>280.08 <b>(+189.98%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.10 (n/a)</td><td>408.22 (n/a)</td><td>454.30 (n/a)</td><td>245.60 (n/a)</td><td>96.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(-37.71%)</b></td><td>0.02 <b>(-20.34%)</b></td><td>0.02 (+0.45%)</td><td>0.01 <b>(-40.69%)</b></td><td>0.01 <b>(-42.29%)</b></td><td>1041.00 <b>(+68.61%)</b></td><td>585.60 <b>(+25.16%)</b></td><td>486.00 (-0.45%)</td><td>342.50 <b>(+60.57%)</b></td><td>272.72 <b>(+74.46%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.40 (n/a)</td><td>467.88 (n/a)</td><td>488.20 (n/a)</td><td>213.30 (n/a)</td><td>156.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(+21.60%)</b></td><td>0.06 <b>(+31.71%)</b></td><td>0.07 <b>(+30.96%)</b></td><td>0.03 (-4.08%)</td><td>0.02 <b>(+41.69%)</b></td><td>503.60 (+4.27%)</td><td>284.24 <b>(-20.84%)</b></td><td>233.00 <b>(-23.66%)</b></td><td>218.40 (-17.77%)</td><td>122.82 <b>(+23.55%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>483.00 (n/a)</td><td>359.08 (n/a)</td><td>305.20 (n/a)</td><td>265.60 (n/a)</td><td>99.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (+19.66%)</td><td>0.05 (+19.74%)</td><td>0.06 <b>(+58.65%)</b></td><td>0.02 <b>(-23.04%)</b></td><td>0.03 <b>(+33.98%)</b></td><td>747.40 <b>(+29.94%)</b></td><td>384.42 (-6.87%)</td><td>272.70 <b>(-36.98%)</b></td><td>178.20 (-16.42%)</td><td>230.01 <b>(+46.96%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>575.20 (n/a)</td><td>412.76 (n/a)</td><td>432.70 (n/a)</td><td>213.20 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (+3.60%)</td><td>0.04 (-11.51%)</td><td>0.03 <b>(-43.51%)</b></td><td>0.03 (-8.43%)</td><td>0.02 (+5.64%)</td><td>569.50 (+9.20%)</td><td>416.36 (+14.30%)</td><td>493.40 <b>(+77.04%)</b></td><td>237.80 (-3.45%)</td><td>148.92 (+5.57%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>521.50 (n/a)</td><td>364.26 (n/a)</td><td>278.70 (n/a)</td><td>246.30 (n/a)</td><td>141.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-14.15%)</td><td>0.04 (-9.01%)</td><td>0.04 (+2.29%)</td><td>0.03 <b>(+24.01%)</b></td><td>0.01 <b>(-44.77%)</b></td><td>528.90 (-19.36%)</td><td>418.08 (-2.63%)</td><td>453.40 (-2.24%)</td><td>273.50 (+16.48%)</td><td>107.76 <b>(-43.19%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>655.90 (n/a)</td><td>429.36 (n/a)</td><td>463.80 (n/a)</td><td>234.80 (n/a)</td><td>189.69 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 <b>(+28.03%)</b></td><td>0.04 (+18.94%)</td><td>0.04 (+13.16%)</td><td>0.02 (-11.43%)</td><td>0.02 <b>(+64.58%)</b></td><td>761.10 (+12.91%)</td><td>453.28 (-7.36%)</td><td>439.00 (-11.62%)</td><td>229.20 <b>(-21.91%)</b></td><td>209.07 <b>(+47.42%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>674.10 (n/a)</td><td>489.28 (n/a)</td><td>496.70 (n/a)</td><td>293.50 (n/a)</td><td>141.82 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(+43.05%)</b></td><td>0.04 (+19.46%)</td><td>0.04 (-9.80%)</td><td>0.03 <b>(+219.01%)</b></td><td>0.01 (-2.64%)</td><td>588.40 <b>(-68.65%)</b></td><td>436.54 <b>(-37.89%)</b></td><td>460.20 (+10.86%)</td><td>253.90 <b>(-30.09%)</b></td><td>124.69 <b>(-81.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1877.00 (n/a)</td><td>702.90 (n/a)</td><td>415.10 (n/a)</td><td>363.20 (n/a)</td><td>657.56 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (+9.03%)</td><td>0.09 (+4.18%)</td><td>0.08 (+9.09%)</td><td>0.07 <b>(+27.05%)</b></td><td>0.03 (-9.46%)</td><td>477.70 <b>(-21.29%)</b></td><td>387.66 (-7.83%)</td><td>407.20 (-8.33%)</td><td>236.50 (-8.30%)</td><td>93.10 <b>(-35.38%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>606.90 (n/a)</td><td>420.58 (n/a)</td><td>444.20 (n/a)</td><td>257.90 (n/a)</td><td>144.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 <b>(-20.38%)</b></td><td>0.10 (+9.98%)</td><td>0.10 <b>(+40.41%)</b></td><td>0.06 (-0.65%)</td><td>0.02 <b>(-37.72%)</b></td><td>530.90 (+0.66%)</td><td>352.44 (-13.49%)</td><td>313.70 <b>(-28.79%)</b></td><td>277.00 <b>(+25.57%)</b></td><td>103.51 (-19.43%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>527.40 (n/a)</td><td>407.42 (n/a)</td><td>440.50 (n/a)</td><td>220.60 (n/a)</td><td>128.48 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 <b>(+47.77%)</b></td><td>0.09 (+18.78%)</td><td>0.06 (-19.95%)</td><td>0.06 (+1.60%)</td><td>0.04 <b>(+164.04%)</b></td><td>565.10 (-1.57%)</td><td>432.36 (-6.03%)</td><td>530.80 <b>(+24.92%)</b></td><td>236.00 <b>(-32.32%)</b></td><td>162.17 <b>(+78.70%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>574.10 (n/a)</td><td>460.10 (n/a)</td><td>424.90 (n/a)</td><td>348.70 (n/a)</td><td>90.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 <b>(+35.56%)</b></td><td>0.10 <b>(+41.17%)</b></td><td>0.10 <b>(+41.55%)</b></td><td>0.07 <b>(+35.99%)</b></td><td>0.03 <b>(+63.62%)</b></td><td>466.90 <b>(-26.47%)</b></td><td>343.78 <b>(-26.87%)</b></td><td>333.20 <b>(-29.36%)</b></td><td>221.40 <b>(-26.22%)</b></td><td>112.13 (-5.61%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>635.00 (n/a)</td><td>470.10 (n/a)</td><td>471.70 (n/a)</td><td>300.10 (n/a)</td><td>118.80 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 <b>(-25.45%)</b></td><td>0.09 (+16.16%)</td><td>0.07 <b>(+27.88%)</b></td><td>0.06 (+18.59%)</td><td>0.03 <b>(-40.49%)</b></td><td>544.00 (-15.67%)</td><td>414.14 <b>(-22.60%)</b></td><td>465.80 <b>(-21.81%)</b></td><td>285.30 <b>(+34.13%)</b></td><td>120.13 <b>(-33.85%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>645.10 (n/a)</td><td>535.06 (n/a)</td><td>595.70 (n/a)</td><td>212.70 (n/a)</td><td>181.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-8.01%)</td><td>0.01 (-10.69%)</td><td>0.01 (-15.56%)</td><td>0.01 (-9.63%)</td><td>0.00 (-9.67%)</td><td>547.40 (+10.65%)</td><td>332.30 (+11.78%)</td><td>292.00 (+18.41%)</td><td>228.80 (+8.69%)</td><td>124.92 (+9.42%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.70 (n/a)</td><td>297.28 (n/a)</td><td>246.60 (n/a)</td><td>210.50 (n/a)</td><td>114.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-3.75%)</td><td>0.01 <b>(-21.60%)</b></td><td>0.01 <b>(-25.18%)</b></td><td>0.01 <b>(-33.98%)</b></td><td>0.00 <b>(+118.34%)</b></td><td>447.60 <b>(+51.47%)</b></td><td>362.46 <b>(+32.65%)</b></td><td>372.10 <b>(+33.66%)</b></td><td>244.40 (+3.91%)</td><td>79.72 <b>(+243.71%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>295.50 (n/a)</td><td>273.24 (n/a)</td><td>278.40 (n/a)</td><td>235.20 (n/a)</td><td>23.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-6.85%)</td><td>0.01 (+12.72%)</td><td>0.01 (+2.84%)</td><td>0.01 <b>(+142.85%)</b></td><td>0.01 <b>(-29.84%)</b></td><td>695.10 <b>(-58.83%)</b></td><td>386.88 <b>(-41.62%)</b></td><td>298.10 (-2.77%)</td><td>236.30 (+7.31%)</td><td>194.72 <b>(-69.01%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1688.20 (n/a)</td><td>662.74 (n/a)</td><td>306.60 (n/a)</td><td>220.20 (n/a)</td><td>628.28 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-9.98%)</td><td>0.01 (+4.52%)</td><td>0.02 (-1.58%)</td><td>0.01 <b>(+52.95%)</b></td><td>0.00 <b>(-67.03%)</b></td><td>319.20 <b>(-34.62%)</b></td><td>275.90 (-10.30%)</td><td>267.60 (+1.59%)</td><td>258.70 (+11.13%)</td><td>24.49 <b>(-76.53%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.20 (n/a)</td><td>307.58 (n/a)</td><td>263.40 (n/a)</td><td>232.80 (n/a)</td><td>104.36 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(-39.32%)</b></td><td>0.01 <b>(-28.59%)</b></td><td>0.01 <b>(-33.08%)</b></td><td>0.00 <b>(-65.61%)</b></td><td>0.01 <b>(-36.04%)</b></td><td>1900.10 <b>(+190.76%)</b></td><td>656.64 <b>(+71.89%)</b></td><td>392.90 <b>(+49.45%)</b></td><td>243.20 <b>(+64.77%)</b></td><td>700.66 <b>(+199.77%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.50 (n/a)</td><td>382.02 (n/a)</td><td>262.90 (n/a)</td><td>147.60 (n/a)</td><td>233.73 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+11.28%)</td><td>0.01 (+19.56%)</td><td>0.02 <b>(+56.21%)</b></td><td>0.01 (+7.88%)</td><td>0.00 (+13.56%)</td><td>522.70 (-7.31%)</td><td>333.90 (-15.62%)</td><td>263.90 <b>(-35.99%)</b></td><td>239.20 (-10.14%)</td><td>121.66 (-2.22%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.90 (n/a)</td><td>395.70 (n/a)</td><td>412.30 (n/a)</td><td>266.20 (n/a)</td><td>124.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-9.55%)</td><td>0.01 (+19.12%)</td><td>0.01 <b>(+41.72%)</b></td><td>0.01 <b>(+40.82%)</b></td><td>0.00 <b>(-43.16%)</b></td><td>432.00 <b>(-28.99%)</b></td><td>325.50 <b>(-20.95%)</b></td><td>302.10 <b>(-29.43%)</b></td><td>280.40 (+10.57%)</td><td>61.25 <b>(-53.64%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>608.40 (n/a)</td><td>411.76 (n/a)</td><td>428.10 (n/a)</td><td>253.60 (n/a)</td><td>132.12 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+48.04%)</b></td><td>0.01 (+5.79%)</td><td>0.01 <b>(-22.23%)</b></td><td>0.01 (+8.95%)</td><td>0.01 <b>(+78.73%)</b></td><td>542.70 (-8.20%)</td><td>391.10 (+2.43%)</td><td>447.20 <b>(+28.58%)</b></td><td>178.10 <b>(-32.46%)</b></td><td>151.60 (+12.70%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.20 (n/a)</td><td>381.82 (n/a)</td><td>347.80 (n/a)</td><td>263.70 (n/a)</td><td>134.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+34.80%)</b></td><td>0.01 (-5.65%)</td><td>0.01 <b>(-24.91%)</b></td><td>0.01 (-12.61%)</td><td>0.01 <b>(+80.03%)</b></td><td>639.80 (+14.43%)</td><td>475.04 (+16.67%)</td><td>500.30 <b>(+33.16%)</b></td><td>204.10 <b>(-25.81%)</b></td><td>169.82 <b>(+41.54%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.10 (n/a)</td><td>407.16 (n/a)</td><td>375.70 (n/a)</td><td>275.10 (n/a)</td><td>119.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 <b>(-28.87%)</b></td><td>0.01 <b>(-25.65%)</b></td><td>0.01 <b>(-27.96%)</b></td><td>0.01 (-19.20%)</td><td>0.00 <b>(-54.24%)</b></td><td>605.80 <b>(+23.76%)</b></td><td>500.06 <b>(+30.97%)</b></td><td>477.00 <b>(+38.82%)</b></td><td>424.70 <b>(+40.58%)</b></td><td>71.66 <b>(-20.05%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.50 (n/a)</td><td>381.80 (n/a)</td><td>343.60 (n/a)</td><td>302.10 (n/a)</td><td>89.63 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-17.61%)</td><td>0.01 (+6.26%)</td><td>0.01 <b>(+30.70%)</b></td><td>0.01 (+8.78%)</td><td>0.00 <b>(-32.44%)</b></td><td>556.80 (-8.07%)</td><td>431.40 (-9.57%)</td><td>387.10 <b>(-23.50%)</b></td><td>339.40 <b>(+21.34%)</b></td><td>102.90 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.70 (n/a)</td><td>477.04 (n/a)</td><td>506.00 (n/a)</td><td>279.70 (n/a)</td><td>138.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-9.09%)</td><td>0.01 (+13.43%)</td><td>0.01 <b>(+56.47%)</b></td><td>0.01 <b>(+30.84%)</b></td><td>0.00 <b>(-52.20%)</b></td><td>432.50 <b>(-23.57%)</b></td><td>367.54 (-18.02%)</td><td>343.80 <b>(-36.08%)</b></td><td>314.20 (+10.01%)</td><td>56.48 <b>(-59.44%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.90 (n/a)</td><td>448.34 (n/a)</td><td>537.90 (n/a)</td><td>285.60 (n/a)</td><td>139.25 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+5.04%)</td><td>0.02 (-1.51%)</td><td>0.03 (+5.83%)</td><td>0.02 (-15.64%)</td><td>0.01 <b>(+36.61%)</b></td><td>533.00 (+18.55%)</td><td>360.40 (+5.64%)</td><td>306.90 (-5.51%)</td><td>260.90 (-4.82%)</td><td>117.23 <b>(+56.28%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>449.60 (n/a)</td><td>341.16 (n/a)</td><td>324.80 (n/a)</td><td>274.10 (n/a)</td><td>75.01 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-2.17%)</td><td>0.02 (-2.44%)</td><td>0.02 (-4.69%)</td><td>0.02 (+1.29%)</td><td>0.01 (-2.66%)</td><td>445.80 (-1.26%)</td><td>357.88 (+2.35%)</td><td>372.80 (+4.93%)</td><td>247.60 (+2.19%)</td><td>87.71 (-0.31%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.50 (n/a)</td><td>349.66 (n/a)</td><td>355.30 (n/a)</td><td>242.30 (n/a)</td><td>87.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-8.08%)</td><td>0.02 <b>(-30.76%)</b></td><td>0.02 <b>(-26.09%)</b></td><td>0.01 <b>(-56.18%)</b></td><td>0.01 <b>(+158.35%)</b></td><td>741.50 <b>(+128.22%)</b></td><td>465.08 <b>(+61.11%)</b></td><td>372.40 <b>(+35.27%)</b></td><td>285.50 (+8.76%)</td><td>186.20 <b>(+556.57%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>324.90 (n/a)</td><td>288.68 (n/a)</td><td>275.30 (n/a)</td><td>262.50 (n/a)</td><td>28.36 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-5.04%)</td><td>0.02 (-2.63%)</td><td>0.02 (-10.97%)</td><td>0.01 (+4.48%)</td><td>0.01 (-8.81%)</td><td>679.10 (-4.28%)</td><td>437.44 (+0.37%)</td><td>457.60 (+12.32%)</td><td>280.50 (+5.29%)</td><td>165.09 (-10.41%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>709.50 (n/a)</td><td>435.84 (n/a)</td><td>407.40 (n/a)</td><td>266.40 (n/a)</td><td>184.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-8.24%)</td><td>0.02 (-10.66%)</td><td>0.02 (-4.91%)</td><td>0.01 (-14.28%)</td><td>0.01 (-13.07%)</td><td>630.40 (+16.65%)</td><td>425.48 (+11.55%)</td><td>342.00 (+5.17%)</td><td>282.50 (+8.99%)</td><td>151.04 (+11.40%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.40 (n/a)</td><td>381.44 (n/a)</td><td>325.20 (n/a)</td><td>259.20 (n/a)</td><td>135.58 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-19.40%)</td><td>0.02 <b>(-22.76%)</b></td><td>0.02 (-17.51%)</td><td>0.01 (-12.17%)</td><td>0.00 <b>(-24.60%)</b></td><td>592.10 (+13.87%)</td><td>471.34 <b>(+28.28%)</b></td><td>442.00 <b>(+21.23%)</b></td><td>329.80 <b>(+24.08%)</b></td><td>106.93 (+8.52%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.00 (n/a)</td><td>367.44 (n/a)</td><td>364.60 (n/a)</td><td>265.80 (n/a)</td><td>98.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+21.74%)</b></td><td>0.02 (-1.01%)</td><td>0.02 (-11.61%)</td><td>0.02 (+16.66%)</td><td>0.01 (+11.33%)</td><td>531.40 (-14.28%)</td><td>434.02 (-0.42%)</td><td>475.90 (+13.12%)</td><td>235.10 (-17.85%)</td><td>115.10 <b>(-24.10%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.90 (n/a)</td><td>435.86 (n/a)</td><td>420.70 (n/a)</td><td>286.20 (n/a)</td><td>151.64 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(-24.61%)</b></td><td>0.02 (-2.43%)</td><td>0.03 (-11.32%)</td><td>0.02 <b>(+294.99%)</b></td><td>0.01 <b>(-56.50%)</b></td><td>491.80 <b>(-74.68%)</b></td><td>371.30 <b>(-41.92%)</b></td><td>309.70 (+12.78%)</td><td>283.60 <b>(+32.65%)</b></td><td>102.57 <b>(-86.08%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1942.60 (n/a)</td><td>639.26 (n/a)</td><td>274.60 (n/a)</td><td>213.80 (n/a)</td><td>736.99 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-7.11%)</td><td>0.02 (-8.65%)</td><td>0.02 <b>(-21.00%)</b></td><td>0.01 <b>(+20.14%)</b></td><td>0.01 <b>(-31.67%)</b></td><td>568.20 (-16.76%)</td><td>400.90 (+1.83%)</td><td>355.40 <b>(+26.61%)</b></td><td>290.90 (+7.66%)</td><td>115.73 <b>(-35.63%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.60 (n/a)</td><td>393.70 (n/a)</td><td>280.70 (n/a)</td><td>270.20 (n/a)</td><td>179.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+5.19%)</td><td>0.03 (+12.02%)</td><td>0.03 <b>(+36.20%)</b></td><td>0.02 (+2.48%)</td><td>0.01 (+10.84%)</td><td>458.10 (-2.43%)</td><td>336.16 (-9.92%)</td><td>284.90 <b>(-26.59%)</b></td><td>239.40 (-4.92%)</td><td>97.17 (+5.01%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.50 (n/a)</td><td>373.20 (n/a)</td><td>388.10 (n/a)</td><td>251.80 (n/a)</td><td>92.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+17.26%)</td><td>0.02 (-6.38%)</td><td>0.02 (+9.28%)</td><td>0.00 <b>(-71.69%)</b></td><td>0.01 <b>(+101.46%)</b></td><td>1958.80 <b>(+253.19%)</b></td><td>725.12 <b>(+66.33%)</b></td><td>409.60 (-8.49%)</td><td>269.30 (-14.72%)</td><td>707.50 <b>(+536.33%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>435.94 (n/a)</td><td>447.60 (n/a)</td><td>315.80 (n/a)</td><td>111.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+10.23%)</td><td>0.02 (+11.35%)</td><td>0.02 (+2.32%)</td><td>0.01 <b>(-22.65%)</b></td><td>0.01 <b>(+37.40%)</b></td><td>1022.50 <b>(+29.28%)</b></td><td>547.96 (+1.26%)</td><td>494.90 (-2.25%)</td><td>257.80 (-9.29%)</td><td>318.08 <b>(+44.09%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>790.90 (n/a)</td><td>541.16 (n/a)</td><td>506.30 (n/a)</td><td>284.20 (n/a)</td><td>220.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (+13.50%)</td><td>0.05 (+13.13%)</td><td>0.06 (+11.70%)</td><td>0.03 <b>(+27.31%)</b></td><td>0.01 (+0.63%)</td><td>476.00 <b>(-21.45%)</b></td><td>323.44 (-13.66%)</td><td>291.10 (-10.49%)</td><td>248.80 (-11.90%)</td><td>93.48 <b>(-30.79%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>606.00 (n/a)</td><td>374.60 (n/a)</td><td>325.20 (n/a)</td><td>282.40 (n/a)</td><td>135.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-0.39%)</td><td>0.04 (-10.52%)</td><td>0.03 (-4.69%)</td><td>0.03 (-1.57%)</td><td>0.01 (-12.87%)</td><td>543.20 (+1.59%)</td><td>444.42 (+9.45%)</td><td>476.10 (+4.91%)</td><td>265.90 (+0.38%)</td><td>105.30 (-14.33%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>406.04 (n/a)</td><td>453.80 (n/a)</td><td>264.90 (n/a)</td><td>122.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (+11.90%)</td><td>0.04 (-13.57%)</td><td>0.03 <b>(-29.77%)</b></td><td>0.01 <b>(-74.47%)</b></td><td>0.02 <b>(+103.34%)</b></td><td>2097.80 <b>(+291.67%)</b></td><td>746.36 <b>(+92.09%)</b></td><td>537.10 <b>(+42.39%)</b></td><td>256.40 (-10.63%)</td><td>770.45 <b>(+617.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>535.60 (n/a)</td><td>388.54 (n/a)</td><td>377.20 (n/a)</td><td>286.90 (n/a)</td><td>107.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 <b>(-27.84%)</b></td><td>0.04 (-14.43%)</td><td>0.05 (-12.73%)</td><td>0.03 (-12.50%)</td><td>0.01 <b>(-41.00%)</b></td><td>603.30 (+14.28%)</td><td>394.26 (+9.71%)</td><td>336.80 (+14.60%)</td><td>298.10 <b>(+38.59%)</b></td><td>128.41 (-13.45%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>527.90 (n/a)</td><td>359.38 (n/a)</td><td>293.90 (n/a)</td><td>215.10 (n/a)</td><td>148.37 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-8.55%)</td><td>0.05 (-13.58%)</td><td>0.04 <b>(-37.47%)</b></td><td>0.03 <b>(+116.74%)</b></td><td>0.02 <b>(-33.24%)</b></td><td>514.10 <b>(-53.86%)</b></td><td>378.38 (-11.61%)</td><td>412.70 <b>(+59.90%)</b></td><td>252.60 (+9.35%)</td><td>114.11 <b>(-70.28%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1114.20 (n/a)</td><td>428.08 (n/a)</td><td>258.10 (n/a)</td><td>231.00 (n/a)</td><td>383.94 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(-32.47%)</b></td><td>0.04 <b>(-32.23%)</b></td><td>0.04 <b>(-39.24%)</b></td><td>0.03 (-18.49%)</td><td>0.01 <b>(-26.05%)</b></td><td>588.80 <b>(+22.69%)</b></td><td>437.76 <b>(+47.37%)</b></td><td>445.60 <b>(+64.55%)</b></td><td>282.20 <b>(+48.06%)</b></td><td>140.92 <b>(+28.69%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>479.90 (n/a)</td><td>297.04 (n/a)</td><td>270.80 (n/a)</td><td>190.60 (n/a)</td><td>109.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(+61.04%)</b></td><td>0.04 (+17.20%)</td><td>0.03 (-8.11%)</td><td>0.03 (-16.55%)</td><td>0.02 <b>(+694.35%)</b></td><td>606.50 (+19.81%)</td><td>461.50 (-4.13%)</td><td>533.80 (+8.83%)</td><td>271.80 <b>(-37.89%)</b></td><td>162.53 <b>(+498.24%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>506.20 (n/a)</td><td>481.38 (n/a)</td><td>490.50 (n/a)</td><td>437.60 (n/a)</td><td>27.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(+61.73%)</b></td><td>0.04 (+11.78%)</td><td>0.04 (+8.68%)</td><td>0.03 (-17.17%)</td><td>0.01 <b>(+582.08%)</b></td><td>619.20 <b>(+20.73%)</b></td><td>464.18 (-3.20%)</td><td>443.60 (-7.99%)</td><td>277.90 <b>(-38.16%)</b></td><td>137.73 <b>(+416.85%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>512.90 (n/a)</td><td>479.54 (n/a)</td><td>482.10 (n/a)</td><td>449.40 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(+27.56%)</b></td><td>0.05 (+18.92%)</td><td>0.06 <b>(+49.57%)</b></td><td>0.03 (-8.84%)</td><td>0.02 <b>(+45.42%)</b></td><td>621.50 (+9.69%)</td><td>364.56 (-10.44%)</td><td>293.50 <b>(-33.13%)</b></td><td>216.20 <b>(-21.61%)</b></td><td>163.06 <b>(+34.10%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.60 (n/a)</td><td>407.06 (n/a)</td><td>438.90 (n/a)</td><td>275.80 (n/a)</td><td>121.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-7.97%)</td><td>0.04 (-9.57%)</td><td>0.04 (-18.52%)</td><td>0.03 (-5.17%)</td><td>0.01 (-12.52%)</td><td>535.80 (+5.45%)</td><td>398.12 (+9.43%)</td><td>382.50 <b>(+22.71%)</b></td><td>276.40 (+8.69%)</td><td>113.08 (-1.59%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>508.10 (n/a)</td><td>363.80 (n/a)</td><td>311.70 (n/a)</td><td>254.30 (n/a)</td><td>114.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.05 (+2.77%)</td><td>0.04 <b>(+30.27%)</b></td><td>0.04 (+17.72%)</td><td>0.03 <b>(+94.39%)</b></td><td>0.01 <b>(-41.85%)</b></td><td>508.30 <b>(-48.55%)</b></td><td>411.10 <b>(-31.27%)</b></td><td>424.00 (-15.06%)</td><td>327.80 (-2.70%)</td><td>71.60 <b>(-71.91%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>988.00 (n/a)</td><td>598.18 (n/a)</td><td>499.20 (n/a)</td><td>336.90 (n/a)</td><td>254.87 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (+2.44%)</td><td>0.03 (-1.49%)</td><td>0.03 (-15.94%)</td><td>0.03 (+18.88%)</td><td>0.01 (-4.92%)</td><td>624.30 (-15.89%)</td><td>515.78 (-1.31%)</td><td>561.60 (+18.96%)</td><td>294.20 (-2.39%)</td><td>138.04 <b>(-24.94%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>742.20 (n/a)</td><td>522.62 (n/a)</td><td>472.10 (n/a)</td><td>301.40 (n/a)</td><td>183.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 <b>(-35.58%)</b></td><td>0.07 <b>(-22.83%)</b></td><td>0.07 <b>(-20.37%)</b></td><td>0.06 (-6.10%)</td><td>0.01 <b>(-73.73%)</b></td><td>582.00 (+6.50%)</td><td>504.50 <b>(+23.88%)</b></td><td>500.70 <b>(+25.58%)</b></td><td>468.40 <b>(+55.25%)</b></td><td>46.16 <b>(-55.44%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>546.50 (n/a)</td><td>407.26 (n/a)</td><td>398.70 (n/a)</td><td>301.70 (n/a)</td><td>103.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (+0.62%)</td><td>0.10 (+7.17%)</td><td>0.09 <b>(+32.49%)</b></td><td>0.06 (+2.66%)</td><td>0.04 (-6.50%)</td><td>544.90 (-2.59%)</td><td>383.42 (-8.99%)</td><td>373.30 <b>(-24.52%)</b></td><td>208.50 (-0.62%)</td><td>141.00 (-10.81%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>559.40 (n/a)</td><td>421.28 (n/a)</td><td>494.60 (n/a)</td><td>209.80 (n/a)</td><td>158.10 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (-14.80%)</td><td>0.08 (-19.03%)</td><td>0.07 <b>(-43.36%)</b></td><td>0.06 (-0.63%)</td><td>0.03 <b>(-23.84%)</b></td><td>586.40 (+0.62%)</td><td>434.06 (+17.96%)</td><td>478.20 <b>(+76.59%)</b></td><td>274.50 (+17.36%)</td><td>142.40 (-12.64%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.80 (n/a)</td><td>367.96 (n/a)</td><td>270.80 (n/a)</td><td>233.90 (n/a)</td><td>163.01 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (-1.67%)</td><td>0.09 (+9.76%)</td><td>0.10 <b>(+20.82%)</b></td><td>0.06 <b>(+20.84%)</b></td><td>0.02 (-18.45%)</td><td>511.80 (-17.25%)</td><td>372.80 (-12.72%)</td><td>331.40 (-17.23%)</td><td>266.60 (+1.72%)</td><td>104.22 <b>(-30.93%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>618.50 (n/a)</td><td>427.14 (n/a)</td><td>400.40 (n/a)</td><td>262.10 (n/a)</td><td>150.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (-2.00%)</td><td>0.09 (-13.02%)</td><td>0.08 <b>(-27.85%)</b></td><td>0.06 (-6.69%)</td><td>0.03 <b>(+29.64%)</b></td><td>521.20 (+7.15%)</td><td>383.66 (+18.68%)</td><td>413.50 <b>(+38.62%)</b></td><td>258.30 (+2.05%)</td><td>118.06 <b>(+26.84%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>486.40 (n/a)</td><td>323.26 (n/a)</td><td>298.30 (n/a)</td><td>253.10 (n/a)</td><td>93.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (-19.78%)</td><td>0.08 (-14.81%)</td><td>0.06 <b>(-41.81%)</b></td><td>0.06 (+17.06%)</td><td>0.04 <b>(-20.66%)</b></td><td>574.50 (-14.57%)</td><td>441.38 (+11.06%)</td><td>530.40 <b>(+71.87%)</b></td><td>255.90 <b>(+24.65%)</b></td><td>161.27 (-17.52%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>672.50 (n/a)</td><td>397.44 (n/a)</td><td>308.60 (n/a)</td><td>205.30 (n/a)</td><td>195.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (-9.76%)</td><td>0.09 (+0.23%)</td><td>0.10 <b>(+38.41%)</b></td><td>0.05 (+0.74%)</td><td>0.03 (-13.63%)</td><td>669.50 (-0.73%)</td><td>414.66 (-1.86%)</td><td>315.60 <b>(-27.75%)</b></td><td>272.30 (+10.83%)</td><td>176.02 (-0.49%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.40 (n/a)</td><td>422.54 (n/a)</td><td>436.80 (n/a)</td><td>245.70 (n/a)</td><td>176.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (-10.22%)</td><td>0.10 (-4.81%)</td><td>0.10 (-19.80%)</td><td>0.07 (+4.13%)</td><td>0.02 <b>(-32.24%)</b></td><td>495.20 (-3.96%)</td><td>345.44 (-0.20%)</td><td>331.60 <b>(+24.71%)</b></td><td>263.80 (+11.40%)</td><td>92.51 <b>(-28.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>515.60 (n/a)</td><td>346.12 (n/a)</td><td>265.90 (n/a)</td><td>236.80 (n/a)</td><td>128.56 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 <b>(-22.91%)</b></td><td>0.08 <b>(-28.02%)</b></td><td>0.08 <b>(-35.94%)</b></td><td>0.06 (+6.68%)</td><td>0.02 <b>(-28.82%)</b></td><td>551.80 (-6.27%)</td><td>427.66 <b>(+32.60%)</b></td><td>427.80 <b>(+56.07%)</b></td><td>292.00 <b>(+29.72%)</b></td><td>123.35 (-17.88%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.70 (n/a)</td><td>322.52 (n/a)</td><td>274.10 (n/a)</td><td>225.10 (n/a)</td><td>150.20 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (+0.17%)</td><td>0.08 (-8.45%)</td><td>0.07 <b>(-35.28%)</b></td><td>0.05 (+3.08%)</td><td>0.04 (-3.98%)</td><td>671.10 (-2.99%)</td><td>444.78 (+6.68%)</td><td>461.50 <b>(+54.50%)</b></td><td>242.30 (-0.16%)</td><td>176.37 (-10.82%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>691.80 (n/a)</td><td>416.92 (n/a)</td><td>298.70 (n/a)</td><td>242.70 (n/a)</td><td>197.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(-25.31%)</b></td><td>0.05 <b>(-40.40%)</b></td><td>0.07 <b>(-29.06%)</b></td><td>0.02 <b>(-74.95%)</b></td><td>0.03 <b>(+83.84%)</b></td><td>1866.90 <b>(+299.25%)</b></td><td>866.12 <b>(+126.27%)</b></td><td>496.10 <b>(+40.98%)</b></td><td>436.40 <b>(+33.87%)</b></td><td>619.44 <b>(+836.11%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>467.60 (n/a)</td><td>382.78 (n/a)</td><td>351.90 (n/a)</td><td>326.00 (n/a)</td><td>66.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 <b>(-20.08%)</b></td><td>0.10 (-5.18%)</td><td>0.10 (-5.82%)</td><td>0.05 (+5.34%)</td><td>0.04 <b>(-30.01%)</b></td><td>722.70 (-5.08%)</td><td>388.50 (-3.65%)</td><td>337.50 (+6.17%)</td><td>223.40 <b>(+25.15%)</b></td><td>197.30 (-15.11%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>761.40 (n/a)</td><td>403.20 (n/a)</td><td>317.90 (n/a)</td><td>178.50 (n/a)</td><td>232.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (+11.53%)</td><td>0.10 <b>(+25.16%)</b></td><td>0.10 <b>(+21.55%)</b></td><td>0.08 <b>(+81.77%)</b></td><td>0.01 <b>(-50.14%)</b></td><td>291.30 <b>(-44.98%)</b></td><td>255.78 <b>(-25.11%)</b></td><td>253.60 (-17.74%)</td><td>220.10 (-10.35%)</td><td>27.71 <b>(-75.69%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>529.40 (n/a)</td><td>341.52 (n/a)</td><td>308.30 (n/a)</td><td>245.50 (n/a)</td><td>113.96 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.20 (-4.28%)</td><td>0.15 (-7.35%)</td><td>0.16 (-12.76%)</td><td>0.11 (+10.64%)</td><td>0.04 (+1.02%)</td><td>453.20 (-9.61%)</td><td>339.06 (+7.43%)</td><td>310.10 (+14.64%)</td><td>247.30 (+4.48%)</td><td>97.68 (-8.76%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>501.40 (n/a)</td><td>315.62 (n/a)</td><td>270.50 (n/a)</td><td>236.70 (n/a)</td><td>107.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.29 <b>(+58.71%)</b></td><td>3.59 <b>(+39.38%)</b></td><td>3.61 <b>(+40.35%)</b></td><td>2.62 (+9.80%)</td><td>0.71 <b>(+455.86%)</b></td><td>4002.00 (-8.92%)</td><td>3020.24 <b>(-25.91%)</b></td><td>2905.80 <b>(-28.75%)</b></td><td>2444.60 <b>(-36.99%)</b></td><td>648.55 <b>(+212.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.70 (n/a)</td><td>2.58 (n/a)</td><td>2.57 (n/a)</td><td>2.39 (n/a)</td><td>0.13 (n/a)</td><td>4394.10 (n/a)</td><td>4076.18 (n/a)</td><td>4078.30 (n/a)</td><td>3879.80 (n/a)</td><td>207.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (+4.30%)</td><td>0.12 (-14.93%)</td><td>0.13 (-18.14%)</td><td>0.07 (-8.43%)</td><td>0.04 (+18.16%)</td><td>563.10 (+9.21%)</td><td>392.06 <b>(+22.25%)</b></td><td>321.50 <b>(+22.15%)</b></td><td>240.20 (-4.11%)</td><td>149.08 <b>(+32.16%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>515.60 (n/a)</td><td>320.70 (n/a)</td><td>263.20 (n/a)</td><td>250.50 (n/a)</td><td>112.81 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-13.71%)</td><td>0.02 (-5.33%)</td><td>0.02 (-6.49%)</td><td>0.01 <b>(+24.38%)</b></td><td>0.00 <b>(-60.67%)</b></td><td>346.10 (-19.59%)</td><td>309.76 (+1.98%)</td><td>314.20 (+6.94%)</td><td>274.80 (+15.90%)</td><td>26.47 <b>(-64.70%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>430.40 (n/a)</td><td>303.74 (n/a)</td><td>293.80 (n/a)</td><td>237.10 (n/a)</td><td>74.99 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-18.30%)</td><td>0.01 (-12.69%)</td><td>0.01 (+3.33%)</td><td>0.00 <b>(-69.50%)</b></td><td>0.01 (+11.78%)</td><td>1719.50 <b>(+227.90%)</b></td><td>633.74 <b>(+62.55%)</b></td><td>445.00 (-3.22%)</td><td>248.80 <b>(+22.38%)</b></td><td>616.96 <b>(+349.41%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.40 (n/a)</td><td>389.88 (n/a)</td><td>459.80 (n/a)</td><td>203.30 (n/a)</td><td>137.28 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(-22.55%)</b></td><td>0.02 <b>(-35.64%)</b></td><td>0.01 <b>(-45.75%)</b></td><td>0.01 (-7.89%)</td><td>0.01 (-18.79%)</td><td>553.30 (+8.55%)</td><td>444.60 <b>(+52.94%)</b></td><td>455.50 <b>(+84.34%)</b></td><td>228.60 <b>(+29.08%)</b></td><td>130.25 (+2.08%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>509.70 (n/a)</td><td>290.70 (n/a)</td><td>247.10 (n/a)</td><td>177.10 (n/a)</td><td>127.61 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-13.55%)</td><td>0.01 (+3.25%)</td><td>0.01 <b>(+31.58%)</b></td><td>0.01 <b>(+344.40%)</b></td><td>0.00 <b>(-53.36%)</b></td><td>466.10 <b>(-77.50%)</b></td><td>396.58 <b>(-48.00%)</b></td><td>442.40 <b>(-24.00%)</b></td><td>228.60 (+15.63%)</td><td>99.18 <b>(-87.08%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2071.50 (n/a)</td><td>762.72 (n/a)</td><td>582.10 (n/a)</td><td>197.70 (n/a)</td><td>767.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+13.65%)</td><td>0.01 (-6.08%)</td><td>0.01 (-1.21%)</td><td>0.00 <b>(-79.80%)</b></td><td>0.01 <b>(+140.64%)</b></td><td>2480.40 <b>(+394.99%)</b></td><td>850.34 <b>(+107.56%)</b></td><td>459.30 (+1.23%)</td><td>237.80 (-12.02%)</td><td>942.35 <b>(+889.73%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.10 (n/a)</td><td>409.68 (n/a)</td><td>453.70 (n/a)</td><td>270.30 (n/a)</td><td>95.21 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-1.64%)</td><td>0.02 (+18.09%)</td><td>0.02 (+2.24%)</td><td>0.01 <b>(+59.67%)</b></td><td>0.00 <b>(-59.72%)</b></td><td>295.10 <b>(-37.39%)</b></td><td>264.70 <b>(-21.89%)</b></td><td>266.80 (-2.16%)</td><td>229.20 (+1.69%)</td><td>28.07 <b>(-75.80%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.30 (n/a)</td><td>338.90 (n/a)</td><td>272.70 (n/a)</td><td>225.40 (n/a)</td><td>116.01 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+35.68%)</b></td><td>0.02 <b>(+37.27%)</b></td><td>0.02 <b>(+97.01%)</b></td><td>0.01 (+4.73%)</td><td>0.01 <b>(+46.98%)</b></td><td>556.70 (-4.51%)</td><td>340.24 <b>(-23.56%)</b></td><td>264.90 <b>(-49.24%)</b></td><td>200.60 <b>(-26.30%)</b></td><td>151.91 (+5.93%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.00 (n/a)</td><td>445.10 (n/a)</td><td>521.90 (n/a)</td><td>272.20 (n/a)</td><td>143.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+10.86%)</td><td>0.01 (+2.85%)</td><td>0.01 (-0.04%)</td><td>0.01 (+11.09%)</td><td>0.00 (+5.67%)</td><td>572.40 (-9.97%)</td><td>397.90 (-3.45%)</td><td>429.40 (+0.05%)</td><td>227.00 (-9.78%)</td><td>138.92 (-11.53%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.80 (n/a)</td><td>412.10 (n/a)</td><td>429.20 (n/a)</td><td>251.60 (n/a)</td><td>157.02 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-6.61%)</td><td>0.01 (+5.12%)</td><td>0.01 (+5.80%)</td><td>0.01 (+1.10%)</td><td>0.01 (-1.69%)</td><td>539.10 (-1.08%)</td><td>379.18 (-4.36%)</td><td>400.60 (-5.47%)</td><td>220.90 (+7.08%)</td><td>139.98 (+4.54%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>545.00 (n/a)</td><td>396.46 (n/a)</td><td>423.80 (n/a)</td><td>206.30 (n/a)</td><td>133.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+4.00%)</td><td>0.01 (-2.57%)</td><td>0.01 (-10.19%)</td><td>0.01 (-5.75%)</td><td>0.00 <b>(+24.69%)</b></td><td>572.10 (+6.10%)</td><td>421.20 (+7.54%)</td><td>487.10 (+11.36%)</td><td>245.10 (-3.84%)</td><td>152.64 <b>(+29.20%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.20 (n/a)</td><td>391.66 (n/a)</td><td>437.40 (n/a)</td><td>254.90 (n/a)</td><td>118.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+22.61%)</b></td><td>0.01 <b>(+24.72%)</b></td><td>0.01 <b>(+25.26%)</b></td><td>0.00 (-14.75%)</td><td>0.01 <b>(+35.97%)</b></td><td>1229.20 (+17.30%)</td><td>515.50 (-9.12%)</td><td>355.40 <b>(-20.15%)</b></td><td>284.90 (-18.46%)</td><td>402.28 <b>(+38.62%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1047.90 (n/a)</td><td>567.24 (n/a)</td><td>445.10 (n/a)</td><td>349.40 (n/a)</td><td>290.21 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.01 (-6.83%)</td><td>0.01 (-15.49%)</td><td>0.01 (-13.98%)</td><td>0.00 <b>(-73.68%)</b></td><td>0.00 <b>(+53.56%)</b></td><td>1885.00 <b>(+279.96%)</b></td><td>711.72 <b>(+73.27%)</b></td><td>508.30 (+16.26%)</td><td>277.00 (+7.32%)</td><td>665.98 <b>(+575.76%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>410.76 (n/a)</td><td>437.20 (n/a)</td><td>258.10 (n/a)</td><td>98.55 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 <b>(+23.09%)</b></td><td>0.03 <b>(+37.25%)</b></td><td>0.03 <b>(+35.33%)</b></td><td>0.02 <b>(+28.32%)</b></td><td>0.00 (+13.03%)</td><td>354.60 <b>(-22.07%)</b></td><td>281.90 <b>(-27.51%)</b></td><td>276.00 <b>(-26.10%)</b></td><td>241.20 (-18.76%)</td><td>45.90 <b>(-30.33%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>455.00 (n/a)</td><td>388.90 (n/a)</td><td>373.50 (n/a)</td><td>296.90 (n/a)</td><td>65.88 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-2.58%)</td><td>0.03 (-9.07%)</td><td>0.03 (+9.24%)</td><td>0.02 <b>(-24.05%)</b></td><td>0.02 (+1.25%)</td><td>614.00 <b>(+31.67%)</b></td><td>423.60 (+12.22%)</td><td>423.00 (-8.46%)</td><td>200.00 (+2.67%)</td><td>150.62 <b>(+20.83%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>466.30 (n/a)</td><td>377.46 (n/a)</td><td>462.10 (n/a)</td><td>194.80 (n/a)</td><td>124.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+5.65%)</td><td>0.03 <b>(+35.99%)</b></td><td>0.03 <b>(+57.51%)</b></td><td>0.02 <b>(+44.32%)</b></td><td>0.01 (-11.94%)</td><td>443.20 <b>(-30.71%)</b></td><td>332.30 <b>(-29.31%)</b></td><td>287.20 <b>(-36.52%)</b></td><td>246.30 (-5.34%)</td><td>87.72 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.60 (n/a)</td><td>470.10 (n/a)</td><td>452.40 (n/a)</td><td>260.20 (n/a)</td><td>141.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 <b>(+56.37%)</b></td><td>0.04 <b>(+54.01%)</b></td><td>0.04 <b>(+77.66%)</b></td><td>0.02 (+10.84%)</td><td>0.01 <b>(+96.09%)</b></td><td>415.80 (-9.79%)</td><td>267.40 <b>(-32.02%)</b></td><td>248.30 <b>(-43.71%)</b></td><td>173.80 <b>(-36.03%)</b></td><td>93.28 (+13.69%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.90 (n/a)</td><td>393.34 (n/a)</td><td>441.10 (n/a)</td><td>271.70 (n/a)</td><td>82.04 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (-8.27%)</td><td>0.02 (-10.38%)</td><td>0.03 (+7.09%)</td><td>0.01 (-10.47%)</td><td>0.01 <b>(+20.37%)</b></td><td>561.50 (+11.70%)</td><td>378.70 (+17.47%)</td><td>278.20 (-6.64%)</td><td>251.50 (+9.02%)</td><td>153.31 <b>(+44.09%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.70 (n/a)</td><td>322.38 (n/a)</td><td>298.00 (n/a)</td><td>230.70 (n/a)</td><td>106.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 <b>(+42.03%)</b></td><td>0.03 <b>(+93.64%)</b></td><td>0.04 <b>(+151.07%)</b></td><td>0.02 <b>(+130.64%)</b></td><td>0.01 <b>(+57.01%)</b></td><td>600.10 <b>(-56.64%)</b></td><td>380.30 <b>(-49.84%)</b></td><td>259.70 <b>(-60.17%)</b></td><td>240.90 <b>(-29.60%)</b></td><td>182.41 <b>(-52.70%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1384.00 (n/a)</td><td>758.20 (n/a)</td><td>652.00 (n/a)</td><td>342.20 (n/a)</td><td>385.61 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+1.21%)</td><td>0.03 (+18.55%)</td><td>0.03 <b>(+33.66%)</b></td><td>0.02 <b>(+26.60%)</b></td><td>0.01 <b>(-28.59%)</b></td><td>470.80 <b>(-21.01%)</b></td><td>313.38 <b>(-21.93%)</b></td><td>287.20 <b>(-25.19%)</b></td><td>242.00 (-1.18%)</td><td>93.98 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.00 (n/a)</td><td>401.42 (n/a)</td><td>383.90 (n/a)</td><td>244.90 (n/a)</td><td>161.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (+5.62%)</td><td>0.03 (+18.75%)</td><td>0.03 (+8.83%)</td><td>0.02 <b>(+38.16%)</b></td><td>0.01 <b>(-32.32%)</b></td><td>410.60 <b>(-27.62%)</b></td><td>316.38 <b>(-20.35%)</b></td><td>307.80 (-8.12%)</td><td>248.30 (-5.34%)</td><td>59.10 <b>(-54.17%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>397.20 (n/a)</td><td>335.00 (n/a)</td><td>262.30 (n/a)</td><td>128.94 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+15.55%)</td><td>0.02 (+4.89%)</td><td>0.03 (+13.66%)</td><td>0.01 (-3.93%)</td><td>0.01 <b>(+44.62%)</b></td><td>601.50 (+4.08%)</td><td>378.22 (-0.57%)</td><td>293.50 (-12.02%)</td><td>265.20 (-13.47%)</td><td>142.81 <b>(+26.23%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.90 (n/a)</td><td>380.40 (n/a)</td><td>333.60 (n/a)</td><td>306.50 (n/a)</td><td>113.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.04 (-10.50%)</td><td>0.03 (+6.00%)</td><td>0.03 <b>(+22.86%)</b></td><td>0.02 (+9.45%)</td><td>0.01 <b>(-26.13%)</b></td><td>504.80 (-8.62%)</td><td>351.46 (-10.18%)</td><td>340.40 (-18.60%)</td><td>240.30 (+11.72%)</td><td>104.01 <b>(-24.01%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>391.30 (n/a)</td><td>418.20 (n/a)</td><td>215.10 (n/a)</td><td>136.88 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.03 (+15.42%)</td><td>0.02 (-3.08%)</td><td>0.02 (+0.44%)</td><td>0.01 (-17.64%)</td><td>0.01 <b>(+98.35%)</b></td><td>602.70 <b>(+21.41%)</b></td><td>413.88 (+13.01%)</td><td>340.50 (-0.44%)</td><td>256.80 (-13.36%)</td><td>163.44 <b>(+112.27%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>496.40 (n/a)</td><td>366.24 (n/a)</td><td>342.00 (n/a)</td><td>296.40 (n/a)</td><td>77.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (+7.44%)</td><td>0.05 (-9.93%)</td><td>0.05 (-17.12%)</td><td>0.03 (-9.16%)</td><td>0.01 (+13.90%)</td><td>475.80 (+10.09%)</td><td>326.22 (+12.48%)</td><td>308.60 <b>(+20.64%)</b></td><td>230.20 (-6.91%)</td><td>93.15 (+16.85%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>432.20 (n/a)</td><td>290.02 (n/a)</td><td>255.80 (n/a)</td><td>247.30 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (-0.12%)</td><td>0.07 (+13.63%)</td><td>0.05 (-4.57%)</td><td>0.05 <b>(+294.79%)</b></td><td>0.03 <b>(-30.51%)</b></td><td>484.20 <b>(-74.67%)</b></td><td>383.82 <b>(-43.65%)</b></td><td>463.00 (+4.80%)</td><td>243.90 (+0.12%)</td><td>124.20 <b>(-82.27%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1911.40 (n/a)</td><td>681.08 (n/a)</td><td>441.80 (n/a)</td><td>243.60 (n/a)</td><td>700.42 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-17.32%)</td><td>0.05 <b>(-30.08%)</b></td><td>0.05 <b>(-20.42%)</b></td><td>0.03 <b>(-51.93%)</b></td><td>0.01 <b>(+220.52%)</b></td><td>569.90 <b>(+107.99%)</b></td><td>380.92 <b>(+55.19%)</b></td><td>302.20 <b>(+25.65%)</b></td><td>278.00 <b>(+20.92%)</b></td><td>131.65 <b>(+676.02%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>274.00 (n/a)</td><td>245.46 (n/a)</td><td>240.50 (n/a)</td><td>229.90 (n/a)</td><td>16.97 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 (+0.43%)</td><td>0.06 (-4.73%)</td><td>0.07 (-9.05%)</td><td>0.04 (+8.63%)</td><td>0.02 (-17.00%)</td><td>524.70 (-7.93%)</td><td>356.48 (+0.82%)</td><td>310.00 (+9.97%)</td><td>233.20 (-0.43%)</td><td>116.15 <b>(-20.61%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.90 (n/a)</td><td>353.58 (n/a)</td><td>281.90 (n/a)</td><td>234.20 (n/a)</td><td>146.30 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-5.42%)</td><td>0.04 (-14.03%)</td><td>0.04 <b>(-22.30%)</b></td><td>0.03 (+0.56%)</td><td>0.01 (-2.25%)</td><td>508.20 (-0.57%)</td><td>415.40 (+16.59%)</td><td>458.60 <b>(+28.71%)</b></td><td>260.60 (+5.76%)</td><td>106.80 (+4.63%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.10 (n/a)</td><td>356.28 (n/a)</td><td>356.30 (n/a)</td><td>246.40 (n/a)</td><td>102.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+1.11%)</td><td>0.06 (-0.12%)</td><td>0.05 (+8.84%)</td><td>0.04 (-0.77%)</td><td>0.02 (-3.08%)</td><td>552.20 (+0.77%)</td><td>406.82 (-0.46%)</td><td>448.50 (-8.11%)</td><td>245.30 (-1.09%)</td><td>136.83 (-1.93%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>548.00 (n/a)</td><td>408.72 (n/a)</td><td>488.10 (n/a)</td><td>248.00 (n/a)</td><td>139.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+17.48%)</td><td>0.03 <b>(-28.84%)</b></td><td>0.04 <b>(-26.67%)</b></td><td>0.01 <b>(-69.88%)</b></td><td>0.03 <b>(+79.35%)</b></td><td>1961.10 <b>(+232.05%)</b></td><td>983.24 <b>(+160.85%)</b></td><td>428.10 <b>(+36.38%)</b></td><td>217.00 (-14.87%)</td><td>869.55 <b>(+514.55%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.60 (n/a)</td><td>376.94 (n/a)</td><td>313.90 (n/a)</td><td>254.90 (n/a)</td><td>141.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+10.74%)</td><td>0.05 (-3.69%)</td><td>0.05 (-12.29%)</td><td>0.03 (-19.19%)</td><td>0.02 <b>(+37.30%)</b></td><td>541.10 <b>(+23.74%)</b></td><td>367.30 (+8.30%)</td><td>337.40 (+14.03%)</td><td>233.50 (-9.71%)</td><td>121.37 <b>(+50.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>437.30 (n/a)</td><td>339.16 (n/a)</td><td>295.90 (n/a)</td><td>258.60 (n/a)</td><td>80.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-11.22%)</td><td>0.04 <b>(-21.67%)</b></td><td>0.04 <b>(-30.73%)</b></td><td>0.03 <b>(-26.68%)</b></td><td>0.01 (-8.04%)</td><td>597.80 <b>(+36.39%)</b></td><td>411.40 <b>(+29.71%)</b></td><td>428.70 <b>(+44.34%)</b></td><td>262.80 (+12.64%)</td><td>125.33 <b>(+42.77%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.30 (n/a)</td><td>317.18 (n/a)</td><td>297.00 (n/a)</td><td>233.30 (n/a)</td><td>87.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+1.48%)</td><td>0.05 (-12.29%)</td><td>0.04 <b>(-33.69%)</b></td><td>0.03 <b>(-28.49%)</b></td><td>0.02 (+17.69%)</td><td>669.20 <b>(+39.82%)</b></td><td>414.80 <b>(+20.67%)</b></td><td>426.50 <b>(+50.81%)</b></td><td>226.20 (-1.44%)</td><td>173.96 <b>(+49.79%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>478.60 (n/a)</td><td>343.76 (n/a)</td><td>282.80 (n/a)</td><td>229.50 (n/a)</td><td>116.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (+15.59%)</td><td>0.04 (+7.92%)</td><td>0.03 (+7.31%)</td><td>0.01 <b>(-50.57%)</b></td><td>0.02 <b>(+69.85%)</b></td><td>1362.60 <b>(+102.29%)</b></td><td>602.82 (+14.58%)</td><td>474.70 (-6.81%)</td><td>292.60 (-13.48%)</td><td>432.12 <b>(+237.52%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>673.60 (n/a)</td><td>526.12 (n/a)</td><td>509.40 (n/a)</td><td>338.20 (n/a)</td><td>128.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (+18.78%)</td><td>0.09 <b>(+21.73%)</b></td><td>0.11 <b>(+67.58%)</b></td><td>0.05 (-18.70%)</td><td>0.03 <b>(+99.96%)</b></td><td>635.90 <b>(+23.00%)</b></td><td>409.76 (-10.91%)</td><td>305.10 <b>(-40.33%)</b></td><td>282.00 (-15.82%)</td><td>160.63 <b>(+100.13%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>517.00 (n/a)</td><td>459.92 (n/a)</td><td>511.30 (n/a)</td><td>335.00 (n/a)</td><td>80.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 <b>(-34.00%)</b></td><td>0.09 (-17.00%)</td><td>0.09 <b>(-34.96%)</b></td><td>0.06 <b>(+252.47%)</b></td><td>0.02 <b>(-70.35%)</b></td><td>537.00 <b>(-71.63%)</b></td><td>392.70 <b>(-35.90%)</b></td><td>384.10 <b>(+53.76%)</b></td><td>304.10 <b>(+51.52%)</b></td><td>90.59 <b>(-87.51%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1892.70 (n/a)</td><td>612.60 (n/a)</td><td>249.80 (n/a)</td><td>200.70 (n/a)</td><td>725.05 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (-12.00%)</td><td>0.09 (-18.80%)</td><td>0.09 (-6.53%)</td><td>0.02 <b>(-68.33%)</b></td><td>0.05 (-5.59%)</td><td>2464.10 <b>(+215.79%)</b></td><td>831.24 <b>(+76.28%)</b></td><td>468.00 (+7.00%)</td><td>266.90 (+13.67%)</td><td>917.67 <b>(+302.26%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>780.30 (n/a)</td><td>471.54 (n/a)</td><td>437.40 (n/a)</td><td>234.80 (n/a)</td><td>228.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 <b>(-33.64%)</b></td><td>0.09 (-10.78%)</td><td>0.08 (+17.15%)</td><td>0.04 <b>(-33.08%)</b></td><td>0.03 <b>(-35.87%)</b></td><td>778.50 <b>(+49.42%)</b></td><td>445.72 (+10.36%)</td><td>415.40 (-14.63%)</td><td>263.80 <b>(+50.66%)</b></td><td>206.89 <b>(+43.56%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>521.00 (n/a)</td><td>403.88 (n/a)</td><td>486.60 (n/a)</td><td>175.10 (n/a)</td><td>144.12 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (-4.70%)</td><td>0.10 (+4.14%)</td><td>0.11 <b>(+39.25%)</b></td><td>0.07 (+9.43%)</td><td>0.03 (-17.11%)</td><td>557.50 (-8.62%)</td><td>425.70 (-6.45%)</td><td>375.40 <b>(-28.19%)</b></td><td>289.80 (+4.92%)</td><td>123.81 (-13.98%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>610.10 (n/a)</td><td>455.04 (n/a)</td><td>522.80 (n/a)</td><td>276.20 (n/a)</td><td>143.93 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (+7.31%)</td><td>0.11 (+15.55%)</td><td>0.13 <b>(+30.55%)</b></td><td>0.07 <b>(+29.76%)</b></td><td>0.03 (+4.61%)</td><td>461.90 <b>(-22.93%)</b></td><td>326.64 (-14.96%)</td><td>259.20 <b>(-23.40%)</b></td><td>237.60 (-6.79%)</td><td>106.45 <b>(-24.37%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>599.30 (n/a)</td><td>384.10 (n/a)</td><td>338.40 (n/a)</td><td>254.90 (n/a)</td><td>140.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 <b>(+36.57%)</b></td><td>0.07 (-6.71%)</td><td>0.09 (+6.59%)</td><td>0.02 <b>(-76.28%)</b></td><td>0.04 <b>(+331.89%)</b></td><td>2394.00 <b>(+321.63%)</b></td><td>835.62 <b>(+76.79%)</b></td><td>429.10 (-6.19%)</td><td>306.90 <b>(-26.77%)</b></td><td>878.87 <b>(+1389.53%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>567.80 (n/a)</td><td>472.66 (n/a)</td><td>457.40 (n/a)</td><td>419.10 (n/a)</td><td>59.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 <b>(-23.45%)</b></td><td>0.09 (-19.18%)</td><td>0.09 <b>(-26.47%)</b></td><td>0.06 (-11.18%)</td><td>0.02 <b>(-40.77%)</b></td><td>577.10 (+12.58%)</td><td>387.60 (+18.16%)</td><td>347.60 <b>(+35.99%)</b></td><td>289.70 <b>(+30.61%)</b></td><td>112.39 (-9.60%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>512.60 (n/a)</td><td>328.02 (n/a)</td><td>255.60 (n/a)</td><td>221.80 (n/a)</td><td>124.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (-12.24%)</td><td>0.08 <b>(-22.33%)</b></td><td>0.06 <b>(-30.22%)</b></td><td>0.06 (-7.62%)</td><td>0.04 (-17.89%)</td><td>641.90 (+8.25%)</td><td>500.26 <b>(+24.18%)</b></td><td>573.80 <b>(+43.31%)</b></td><td>229.70 (+14.00%)</td><td>166.89 (-5.31%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>593.00 (n/a)</td><td>402.84 (n/a)</td><td>400.40 (n/a)</td><td>201.50 (n/a)</td><td>176.25 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (-14.72%)</td><td>0.08 (-4.59%)</td><td>0.07 (-13.26%)</td><td>0.06 <b>(+134.47%)</b></td><td>0.02 <b>(-43.36%)</b></td><td>555.70 <b>(-57.35%)</b></td><td>439.02 (-19.49%)</td><td>477.30 (+15.29%)</td><td>300.10 (+17.27%)</td><td>115.46 <b>(-73.28%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1302.80 (n/a)</td><td>545.32 (n/a)</td><td>414.00 (n/a)</td><td>255.90 (n/a)</td><td>432.09 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (-11.57%)</td><td>0.04 <b>(-37.42%)</b></td><td>0.03 <b>(-50.62%)</b></td><td>0.01 <b>(-81.48%)</b></td><td>0.03 <b>(+95.10%)</b></td><td>2444.50 <b>(+439.86%)</b></td><td>857.94 <b>(+170.66%)</b></td><td>609.40 <b>(+102.53%)</b></td><td>295.70 (+13.08%)</td><td>901.22 <b>(+1053.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>452.80 (n/a)</td><td>316.98 (n/a)</td><td>300.90 (n/a)</td><td>261.50 (n/a)</td><td>78.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (+17.99%)</td><td>0.07 (-7.39%)</td><td>0.07 (-9.50%)</td><td>0.04 (+3.77%)</td><td>0.03 <b>(+32.04%)</b></td><td>483.30 (-3.63%)</td><td>337.34 (+11.21%)</td><td>301.90 (+10.51%)</td><td>176.40 (-15.23%)</td><td>120.09 (+3.11%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.50 (n/a)</td><td>303.34 (n/a)</td><td>273.20 (n/a)</td><td>208.10 (n/a)</td><td>116.46 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (-5.43%)</td><td>0.04 <b>(-22.04%)</b></td><td>0.04 (-17.25%)</td><td>0.02 <b>(-47.87%)</b></td><td>0.02 (+0.88%)</td><td>1062.50 <b>(+91.82%)</b></td><td>564.86 <b>(+39.84%)</b></td><td>494.70 <b>(+20.84%)</b></td><td>276.70 (+5.73%)</td><td>294.55 <b>(+118.01%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.90 (n/a)</td><td>403.94 (n/a)</td><td>409.40 (n/a)</td><td>261.70 (n/a)</td><td>135.11 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+19.03%)</td><td>0.07 (+19.07%)</td><td>0.08 <b>(+48.11%)</b></td><td>0.04 (-9.04%)</td><td>0.02 <b>(+88.29%)</b></td><td>527.70 (+9.94%)</td><td>349.18 (-9.78%)</td><td>255.00 <b>(-32.49%)</b></td><td>249.70 (-15.98%)</td><td>134.15 <b>(+65.62%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>480.00 (n/a)</td><td>387.04 (n/a)</td><td>377.70 (n/a)</td><td>297.20 (n/a)</td><td>81.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (-3.78%)</td><td>0.04 (-9.83%)</td><td>0.04 (-13.98%)</td><td>0.03 (-0.51%)</td><td>0.02 (-0.31%)</td><td>591.10 (+0.51%)</td><td>499.70 (+11.33%)</td><td>537.30 (+16.25%)</td><td>268.40 (+3.91%)</td><td>133.73 (+3.01%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.10 (n/a)</td><td>448.86 (n/a)</td><td>462.20 (n/a)</td><td>258.30 (n/a)</td><td>129.83 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (-4.98%)</td><td>0.05 <b>(-28.02%)</b></td><td>0.04 <b>(-49.58%)</b></td><td>0.03 (-9.73%)</td><td>0.02 (-16.07%)</td><td>679.70 (+10.77%)</td><td>486.54 <b>(+34.55%)</b></td><td>493.60 <b>(+98.31%)</b></td><td>242.90 (+5.24%)</td><td>164.55 (-3.97%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>613.60 (n/a)</td><td>361.60 (n/a)</td><td>248.90 (n/a)</td><td>230.80 (n/a)</td><td>171.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(-20.57%)</b></td><td>0.06 (-14.06%)</td><td>0.05 (-11.99%)</td><td>0.04 (-18.69%)</td><td>0.02 <b>(-22.33%)</b></td><td>588.40 <b>(+22.99%)</b></td><td>466.08 (+16.13%)</td><td>501.70 (+13.61%)</td><td>304.90 <b>(+25.89%)</b></td><td>117.21 <b>(+25.15%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>478.40 (n/a)</td><td>401.34 (n/a)</td><td>441.60 (n/a)</td><td>242.20 (n/a)</td><td>93.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 (+6.00%)</td><td>0.06 (-19.95%)</td><td>0.05 <b>(-42.57%)</b></td><td>0.01 <b>(-69.27%)</b></td><td>0.04 <b>(+37.44%)</b></td><td>1859.60 <b>(+225.39%)</b></td><td>691.96 <b>(+86.28%)</b></td><td>518.80 <b>(+74.15%)</b></td><td>221.10 (-5.63%)</td><td>670.57 <b>(+330.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>571.50 (n/a)</td><td>371.46 (n/a)</td><td>297.90 (n/a)</td><td>234.30 (n/a)</td><td>155.74 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 <b>(-25.64%)</b></td><td>0.06 <b>(-21.30%)</b></td><td>0.06 <b>(-27.41%)</b></td><td>0.04 (-9.69%)</td><td>0.02 <b>(-35.95%)</b></td><td>558.50 (+10.73%)</td><td>421.98 <b>(+23.08%)</b></td><td>409.10 <b>(+37.74%)</b></td><td>297.10 <b>(+34.50%)</b></td><td>106.24 (-6.02%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>504.40 (n/a)</td><td>342.84 (n/a)</td><td>297.00 (n/a)</td><td>220.90 (n/a)</td><td>113.05 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 <b>(-22.35%)</b></td><td>0.05 <b>(-29.04%)</b></td><td>0.05 (-19.76%)</td><td>0.02 <b>(-48.63%)</b></td><td>0.02 (-18.47%)</td><td>1009.00 <b>(+94.67%)</b></td><td>570.78 <b>(+48.49%)</b></td><td>494.30 <b>(+24.60%)</b></td><td>341.20 <b>(+28.80%)</b></td><td>256.33 <b>(+126.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>518.30 (n/a)</td><td>384.40 (n/a)</td><td>396.70 (n/a)</td><td>264.90 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.10 (-5.30%)</td><td>0.07 (+13.68%)</td><td>0.05 (+5.73%)</td><td>0.04 (+0.69%)</td><td>0.03 (+3.68%)</td><td>549.50 (-0.69%)</td><td>415.66 (-10.86%)</td><td>486.00 (-5.43%)</td><td>254.80 (+5.59%)</td><td>142.15 (+9.73%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.30 (n/a)</td><td>466.32 (n/a)</td><td>513.90 (n/a)</td><td>241.30 (n/a)</td><td>129.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.11 <b>(+20.13%)</b></td><td>0.07 (-3.62%)</td><td>0.07 (-16.99%)</td><td>0.01 <b>(-75.35%)</b></td><td>0.04 <b>(+77.56%)</b></td><td>2356.10 <b>(+305.73%)</b></td><td>741.00 <b>(+89.88%)</b></td><td>360.40 <b>(+20.45%)</b></td><td>231.60 (-16.75%)</td><td>910.50 <b>(+526.61%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>580.70 (n/a)</td><td>390.24 (n/a)</td><td>299.20 (n/a)</td><td>278.20 (n/a)</td><td>145.31 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+8.37%)</td><td>0.05 (-4.10%)</td><td>0.04 <b>(-25.00%)</b></td><td>0.03 <b>(+29.16%)</b></td><td>0.02 (-4.09%)</td><td>532.50 <b>(-22.58%)</b></td><td>441.10 (-1.60%)</td><td>496.70 <b>(+33.34%)</b></td><td>228.10 (-7.73%)</td><td>125.52 <b>(-36.81%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>687.80 (n/a)</td><td>448.26 (n/a)</td><td>372.50 (n/a)</td><td>247.20 (n/a)</td><td>198.64 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (+7.66%)</td><td>0.05 (-3.74%)</td><td>0.04 <b>(-31.32%)</b></td><td>0.03 (+10.46%)</td><td>0.02 (+4.07%)</td><td>556.70 (-9.48%)</td><td>411.72 (+2.96%)</td><td>442.30 <b>(+45.64%)</b></td><td>256.70 (-7.09%)</td><td>136.60 (-12.07%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>615.00 (n/a)</td><td>399.88 (n/a)</td><td>303.70 (n/a)</td><td>276.30 (n/a)</td><td>155.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (-17.47%)</td><td>0.05 (-5.64%)</td><td>0.04 (+0.48%)</td><td>0.03 (+2.15%)</td><td>0.02 <b>(-28.43%)</b></td><td>574.60 (-2.10%)</td><td>428.88 (+0.07%)</td><td>464.30 (-0.47%)</td><td>285.00 <b>(+21.17%)</b></td><td>131.46 <b>(-20.09%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>586.90 (n/a)</td><td>428.56 (n/a)</td><td>466.50 (n/a)</td><td>235.20 (n/a)</td><td>164.50 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.07 (+6.10%)</td><td>0.04 (+3.93%)</td><td>0.03 (+10.38%)</td><td>0.03 (+19.41%)</td><td>0.02 (-9.78%)</td><td>567.20 (-16.27%)</td><td>459.66 (-7.89%)</td><td>529.80 (-9.40%)</td><td>263.00 (-5.73%)</td><td>135.37 <b>(-26.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>677.40 (n/a)</td><td>499.02 (n/a)</td><td>584.80 (n/a)</td><td>279.00 (n/a)</td><td>184.11 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 <b>(+34.58%)</b></td><td>0.05 (+10.80%)</td><td>0.03 (-2.96%)</td><td>0.03 (-5.04%)</td><td>0.03 <b>(+70.82%)</b></td><td>615.70 (+5.32%)</td><td>472.54 (-1.48%)</td><td>531.10 (+3.05%)</td><td>201.20 <b>(-25.67%)</b></td><td>164.63 <b>(+31.57%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.60 (n/a)</td><td>479.66 (n/a)</td><td>515.40 (n/a)</td><td>270.70 (n/a)</td><td>125.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.08 (+5.84%)</td><td>0.06 (+8.27%)</td><td>0.06 (+14.44%)</td><td>0.04 (+2.70%)</td><td>0.02 (-1.40%)</td><td>511.00 (-2.61%)</td><td>355.92 (-8.64%)</td><td>324.70 (-12.60%)</td><td>231.80 (-5.54%)</td><td>106.94 (-11.47%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>524.70 (n/a)</td><td>389.56 (n/a)</td><td>371.50 (n/a)</td><td>245.40 (n/a)</td><td>120.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.42 <b>(+25.43%)</b></td><td>0.23 (-3.49%)</td><td>0.20 (-5.90%)</td><td>0.04 <b>(-77.39%)</b></td><td>0.14 <b>(+90.99%)</b></td><td>2463.70 <b>(+342.32%)</b></td><td>805.38 <b>(+83.46%)</b></td><td>503.50 (+6.27%)</td><td>233.90 <b>(-20.28%)</b></td><td>935.06 <b>(+640.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>557.00 (n/a)</td><td>439.00 (n/a)</td><td>473.80 (n/a)</td><td>293.40 (n/a)</td><td>126.28 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.51 <b>(+22.23%)</b></td><td>0.34 (+16.49%)</td><td>0.36 (+1.97%)</td><td>0.14 (-7.43%)</td><td>0.13 (+17.30%)</td><td>689.50 (+8.02%)</td><td>342.92 (-10.93%)</td><td>274.60 (-1.96%)</td><td>194.30 (-18.19%)</td><td>197.86 (+13.62%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>638.30 (n/a)</td><td>385.02 (n/a)</td><td>280.10 (n/a)</td><td>237.50 (n/a)</td><td>174.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.40 <b>(+51.82%)</b></td><td>0.23 (+8.89%)</td><td>0.20 (-5.47%)</td><td>0.15 (-5.69%)</td><td>0.10 <b>(+150.82%)</b></td><td>639.80 (+6.03%)</td><td>478.20 (-0.92%)</td><td>503.60 (+5.80%)</td><td>248.20 <b>(-34.13%)</b></td><td>142.93 <b>(+61.33%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>603.40 (n/a)</td><td>482.64 (n/a)</td><td>476.00 (n/a)</td><td>376.80 (n/a)</td><td>88.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.27 <b>(-40.47%)</b></td><td>0.19 (-19.29%)</td><td>0.16 (-9.58%)</td><td>0.14 (+1.45%)</td><td>0.06 <b>(-54.13%)</b></td><td>544.10 (-1.43%)</td><td>417.22 (+9.86%)</td><td>456.60 (+10.58%)</td><td>269.00 <b>(+68.02%)</b></td><td>121.72 <b>(-23.22%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.46 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>552.00 (n/a)</td><td>379.78 (n/a)</td><td>412.90 (n/a)</td><td>160.10 (n/a)</td><td>158.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.28 (+7.74%)</td><td>0.21 (+9.59%)</td><td>0.24 <b>(+40.49%)</b></td><td>0.12 (-12.48%)</td><td>0.07 <b>(+49.60%)</b></td><td>596.10 (+14.26%)</td><td>388.06 (-2.78%)</td><td>302.40 <b>(-28.81%)</b></td><td>267.40 (-7.19%)</td><td>152.31 <b>(+58.29%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>521.70 (n/a)</td><td>399.14 (n/a)</td><td>424.80 (n/a)</td><td>288.10 (n/a)</td><td>96.22 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.22 (+7.22%)</td><td>0.18 <b>(+25.68%)</b></td><td>0.17 <b>(+20.17%)</b></td><td>0.12 <b>(+78.72%)</b></td><td>0.04 <b>(-21.49%)</b></td><td>609.30 <b>(-44.05%)</b></td><td>440.98 <b>(-27.55%)</b></td><td>446.50 (-16.78%)</td><td>335.90 (-6.72%)</td><td>109.82 <b>(-61.54%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>1089.00 (n/a)</td><td>608.70 (n/a)</td><td>536.50 (n/a)</td><td>360.10 (n/a)</td><td>285.51 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (-4.46%)</td><td>0.12 (-0.25%)</td><td>0.13 (+2.65%)</td><td>0.08 (+1.61%)</td><td>0.03 (-6.88%)</td><td>480.10 (-1.60%)</td><td>318.58 (-0.36%)</td><td>289.20 (-2.59%)</td><td>249.00 (+4.67%)</td><td>92.42 (-4.88%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>487.90 (n/a)</td><td>319.72 (n/a)</td><td>296.90 (n/a)</td><td>237.90 (n/a)</td><td>97.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (+2.73%)</td><td>0.09 (-10.61%)</td><td>0.07 <b>(-24.19%)</b></td><td>0.05 (-16.24%)</td><td>0.04 <b>(+20.26%)</b></td><td>734.00 (+19.39%)</td><td>489.56 <b>(+20.22%)</b></td><td>509.00 <b>(+31.93%)</b></td><td>255.10 (-2.63%)</td><td>216.01 <b>(+42.68%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>614.80 (n/a)</td><td>407.22 (n/a)</td><td>385.80 (n/a)</td><td>262.00 (n/a)</td><td>151.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (+12.58%)</td><td>0.10 (+9.60%)</td><td>0.08 (+3.07%)</td><td>0.06 <b>(+74.19%)</b></td><td>0.04 (-10.16%)</td><td>630.80 <b>(-42.59%)</b></td><td>429.58 <b>(-20.10%)</b></td><td>478.60 (-2.98%)</td><td>242.70 (-11.20%)</td><td>160.22 <b>(-52.53%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1098.80 (n/a)</td><td>537.64 (n/a)</td><td>493.30 (n/a)</td><td>273.30 (n/a)</td><td>337.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 <b>(+68.00%)</b></td><td>0.14 <b>(+74.00%)</b></td><td>0.14 <b>(+73.79%)</b></td><td>0.12 <b>(+97.56%)</b></td><td>0.01 (-8.14%)</td><td>302.10 <b>(-49.39%)</b></td><td>272.06 <b>(-43.26%)</b></td><td>267.40 <b>(-42.45%)</b></td><td>246.20 <b>(-40.47%)</b></td><td>20.40 <b>(-72.27%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>479.46 (n/a)</td><td>464.60 (n/a)</td><td>413.60 (n/a)</td><td>73.59 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (-1.35%)</td><td>0.08 <b>(-25.48%)</b></td><td>0.07 <b>(-41.62%)</b></td><td>0.03 <b>(-45.82%)</b></td><td>0.04 (+1.94%)</td><td>1101.20 <b>(+84.55%)</b></td><td>567.36 <b>(+46.24%)</b></td><td>510.90 <b>(+71.27%)</b></td><td>246.00 (+1.40%)</td><td>318.42 <b>(+90.90%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>596.70 (n/a)</td><td>387.96 (n/a)</td><td>298.30 (n/a)</td><td>242.60 (n/a)</td><td>166.80 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.14 (-16.09%)</td><td>0.11 <b>(+23.56%)</b></td><td>0.12 <b>(+64.30%)</b></td><td>0.06 (+1.88%)</td><td>0.04 <b>(-21.59%)</b></td><td>599.60 (-1.83%)</td><td>362.54 <b>(-21.48%)</b></td><td>294.90 <b>(-39.15%)</b></td><td>257.30 (+19.18%)</td><td>144.94 (-3.27%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>610.80 (n/a)</td><td>461.70 (n/a)</td><td>484.60 (n/a)</td><td>215.90 (n/a)</td><td>149.84 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.19 (+17.75%)</td><td>0.13 (-1.14%)</td><td>0.15 (+2.33%)</td><td>0.08 (-2.56%)</td><td>0.04 <b>(+40.77%)</b></td><td>535.80 (+2.62%)</td><td>349.70 (+5.31%)</td><td>282.00 (-2.29%)</td><td>218.10 (-15.07%)</td><td>130.18 <b>(+20.08%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>522.10 (n/a)</td><td>332.06 (n/a)</td><td>288.60 (n/a)</td><td>256.80 (n/a)</td><td>108.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (-7.28%)</td><td>0.10 (+4.47%)</td><td>0.09 <b>(+25.31%)</b></td><td>0.08 <b>(+246.92%)</b></td><td>0.03 <b>(-50.13%)</b></td><td>542.90 <b>(-71.18%)</b></td><td>437.80 <b>(-39.96%)</b></td><td>443.60 <b>(-20.20%)</b></td><td>266.40 (+7.85%)</td><td>108.74 <b>(-83.86%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1883.60 (n/a)</td><td>729.16 (n/a)</td><td>555.90 (n/a)</td><td>247.00 (n/a)</td><td>673.81 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (+3.99%)</td><td>0.11 (+1.89%)</td><td>0.14 <b>(+37.65%)</b></td><td>0.02 <b>(-74.53%)</b></td><td>0.06 <b>(+67.06%)</b></td><td>2030.60 <b>(+292.61%)</b></td><td>660.36 <b>(+66.85%)</b></td><td>292.90 <b>(-27.36%)</b></td><td>240.80 (-3.83%)</td><td>771.47 <b>(+544.29%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>517.20 (n/a)</td><td>395.78 (n/a)</td><td>403.20 (n/a)</td><td>250.40 (n/a)</td><td>119.74 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.17 (-10.39%)</td><td>0.11 (+6.43%)</td><td>0.11 <b>(+32.99%)</b></td><td>0.08 <b>(+88.82%)</b></td><td>0.04 <b>(-35.18%)</b></td><td>510.80 <b>(-47.05%)</b></td><td>386.86 <b>(-21.18%)</b></td><td>371.00 <b>(-24.79%)</b></td><td>247.80 (+11.62%)</td><td>119.37 <b>(-59.14%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>964.60 (n/a)</td><td>490.84 (n/a)</td><td>493.30 (n/a)</td><td>222.00 (n/a)</td><td>292.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.12 (-16.63%)</td><td>0.08 <b>(-23.70%)</b></td><td>0.08 <b>(-38.55%)</b></td><td>0.05 <b>(-32.10%)</b></td><td>0.03 (-13.59%)</td><td>893.70 <b>(+47.28%)</b></td><td>551.16 <b>(+34.00%)</b></td><td>531.10 <b>(+62.76%)</b></td><td>351.20 (+19.95%)</td><td>220.98 <b>(+49.10%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>606.80 (n/a)</td><td>411.32 (n/a)</td><td>326.30 (n/a)</td><td>292.80 (n/a)</td><td>148.21 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.16 (+16.19%)</td><td>0.10 (+1.66%)</td><td>0.09 (+13.47%)</td><td>0.07 (-4.47%)</td><td>0.04 (+11.81%)</td><td>624.00 (+4.68%)</td><td>455.46 (-0.68%)</td><td>473.30 (-11.86%)</td><td>261.80 (-13.94%)</td><td>142.43 (+3.01%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>596.10 (n/a)</td><td>458.60 (n/a)</td><td>537.00 (n/a)</td><td>304.20 (n/a)</td><td>138.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (+9.58%)</td><td>0.09 (+12.02%)</td><td>0.08 (+16.54%)</td><td>0.07 (+1.15%)</td><td>0.03 (+14.59%)</td><td>529.00 (-1.14%)</td><td>391.42 (-10.06%)</td><td>410.60 (-14.17%)</td><td>264.80 (-8.72%)</td><td>108.49 (-0.45%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>535.10 (n/a)</td><td>435.18 (n/a)</td><td>478.40 (n/a)</td><td>290.10 (n/a)</td><td>108.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.09 <b>(-34.33%)</b></td><td>0.07 <b>(-30.44%)</b></td><td>0.07 <b>(-39.94%)</b></td><td>0.06 (-8.25%)</td><td>0.01 <b>(-61.65%)</b></td><td>585.90 (+9.00%)</td><td>482.82 <b>(+34.93%)</b></td><td>487.60 <b>(+66.47%)</b></td><td>373.80 <b>(+52.26%)</b></td><td>75.15 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>537.50 (n/a)</td><td>357.82 (n/a)</td><td>292.90 (n/a)</td><td>245.50 (n/a)</td><td>122.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.21 <b>(+58.71%)</b></td><td>0.11 <b>(+24.86%)</b></td><td>0.08 (-8.48%)</td><td>0.07 <b>(+37.27%)</b></td><td>0.06 <b>(+88.87%)</b></td><td>506.30 <b>(-27.15%)</b></td><td>374.26 (-13.18%)</td><td>453.50 (+9.28%)</td><td>168.40 <b>(-37.00%)</b></td><td>157.36 (-7.29%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>695.00 (n/a)</td><td>431.06 (n/a)</td><td>415.00 (n/a)</td><td>267.30 (n/a)</td><td>169.74 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (-6.12%)</td><td>0.11 <b>(+25.34%)</b></td><td>0.12 <b>(+63.14%)</b></td><td>0.07 <b>(+32.98%)</b></td><td>0.03 <b>(-27.49%)</b></td><td>493.20 <b>(-24.81%)</b></td><td>329.84 <b>(-27.43%)</b></td><td>287.90 <b>(-38.71%)</b></td><td>232.90 (+6.49%)</td><td>106.98 <b>(-43.11%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>655.90 (n/a)</td><td>454.54 (n/a)</td><td>469.70 (n/a)</td><td>218.70 (n/a)</td><td>188.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (-5.96%)</td><td>0.08 <b>(-25.16%)</b></td><td>0.06 <b>(-46.66%)</b></td><td>0.05 (-6.54%)</td><td>0.03 (-14.95%)</td><td>634.80 (+6.99%)</td><td>505.96 <b>(+30.10%)</b></td><td>554.90 <b>(+87.47%)</b></td><td>271.10 (+6.36%)</td><td>142.25 (-9.04%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>593.30 (n/a)</td><td>388.90 (n/a)</td><td>296.00 (n/a)</td><td>254.90 (n/a)</td><td>156.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (+1.61%)</td><td>0.10 (-4.61%)</td><td>0.09 (+3.57%)</td><td>0.06 (-19.32%)</td><td>0.04 <b>(+24.22%)</b></td><td>603.30 <b>(+23.96%)</b></td><td>402.82 (+12.18%)</td><td>388.20 (-3.43%)</td><td>236.40 (-1.62%)</td><td>168.16 <b>(+54.12%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>486.70 (n/a)</td><td>359.08 (n/a)</td><td>402.00 (n/a)</td><td>240.30 (n/a)</td><td>109.11 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.49 <b>(+47.85%)</b></td><td>0.37 <b>(+64.21%)</b></td><td>0.42 <b>(+71.85%)</b></td><td>0.22 <b>(+243.75%)</b></td><td>0.12 (+12.55%)</td><td>607.20 <b>(-70.91%)</b></td><td>392.48 <b>(-52.72%)</b></td><td>315.80 <b>(-41.81%)</b></td><td>267.70 <b>(-32.36%)</b></td><td>144.79 <b>(-79.62%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>0.10 (n/a)</td><td>2087.10 (n/a)</td><td>830.12 (n/a)</td><td>542.70 (n/a)</td><td>395.80 (n/a)</td><td>710.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.31 <b>(-27.39%)</b></td><td>0.23 (-18.34%)</td><td>0.22 (-15.73%)</td><td>0.18 (+11.94%)</td><td>0.05 <b>(-51.08%)</b></td><td>716.20 (-10.68%)</td><td>601.72 (+13.22%)</td><td>594.30 (+18.65%)</td><td>420.00 <b>(+37.75%)</b></td><td>115.28 <b>(-41.16%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>801.80 (n/a)</td><td>531.46 (n/a)</td><td>500.90 (n/a)</td><td>304.90 (n/a)</td><td>195.92 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.48 <b>(+24.31%)</b></td><td>0.28 (-3.46%)</td><td>0.25 (-12.25%)</td><td>0.18 (-6.04%)</td><td>0.12 <b>(+71.82%)</b></td><td>721.00 (+6.44%)</td><td>528.06 (+9.90%)</td><td>515.20 (+13.96%)</td><td>274.90 (-19.55%)</td><td>165.31 <b>(+35.21%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>677.40 (n/a)</td><td>480.48 (n/a)</td><td>452.10 (n/a)</td><td>341.70 (n/a)</td><td>122.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-14.22%)</td><td>0.01 (+4.32%)</td><td>0.01 (+3.79%)</td><td>0.01 <b>(+36.81%)</b></td><td>0.00 <b>(-51.74%)</b></td><td>308.80 <b>(-26.89%)</b></td><td>285.16 (-10.83%)</td><td>301.70 (-3.64%)</td><td>215.70 (+16.59%)</td><td>39.28 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>422.40 (n/a)</td><td>319.80 (n/a)</td><td>313.10 (n/a)</td><td>185.00 (n/a)</td><td>99.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+14.63%)</td><td>0.02 (+5.99%)</td><td>0.02 (+1.40%)</td><td>0.01 (-14.31%)</td><td>0.00 <b>(+63.77%)</b></td><td>480.40 (+16.72%)</td><td>295.62 (-0.69%)</td><td>268.50 (-1.40%)</td><td>212.30 (-12.78%)</td><td>108.33 <b>(+63.95%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>411.60 (n/a)</td><td>297.68 (n/a)</td><td>272.30 (n/a)</td><td>243.40 (n/a)</td><td>66.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (+1.00%)</td><td>0.01 (-12.32%)</td><td>0.01 <b>(-29.02%)</b></td><td>0.01 <b>(-21.85%)</b></td><td>0.00 (+16.81%)</td><td>641.60 <b>(+27.96%)</b></td><td>404.02 (+18.84%)</td><td>409.10 <b>(+40.87%)</b></td><td>239.30 (-0.99%)</td><td>152.71 <b>(+45.59%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.40 (n/a)</td><td>339.98 (n/a)</td><td>290.40 (n/a)</td><td>241.70 (n/a)</td><td>104.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>11.16 <b>(+35.30%)</b></td><td>6.83 (+5.85%)</td><td>6.00 (-9.52%)</td><td>3.66 (-19.19%)</td><td>2.89 <b>(+65.89%)</b></td><td>572.90 <b>(+23.76%)</b></td><td>354.12 (+2.25%)</td><td>349.60 (+10.53%)</td><td>188.00 <b>(-26.10%)</b></td><td>147.04 <b>(+49.99%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.25 (n/a)</td><td>6.45 (n/a)</td><td>6.63 (n/a)</td><td>4.53 (n/a)</td><td>1.74 (n/a)</td><td>462.90 (n/a)</td><td>346.32 (n/a)</td><td>316.30 (n/a)</td><td>254.40 (n/a)</td><td>98.04 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.60 (+11.70%)</td><td>0.41 (+7.88%)</td><td>0.38 (-3.34%)</td><td>0.28 <b>(+24.01%)</b></td><td>0.13 (+8.59%)</td><td>480.00 (-19.35%)</td><td>350.18 (-8.58%)</td><td>349.80 (+3.46%)</td><td>220.60 (-10.47%)</td><td>102.73 <b>(-23.75%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>595.20 (n/a)</td><td>383.04 (n/a)</td><td>338.10 (n/a)</td><td>246.40 (n/a)</td><td>134.73 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.49 (-14.29%)</td><td>0.35 (-18.98%)</td><td>0.42 (-2.63%)</td><td>0.07 <b>(-73.74%)</b></td><td>0.17 <b>(+39.00%)</b></td><td>1976.00 <b>(+280.81%)</b></td><td>646.80 <b>(+97.77%)</b></td><td>314.40 (+2.71%)</td><td>271.60 (+16.67%)</td><td>743.85 <b>(+557.17%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>518.90 (n/a)</td><td>327.04 (n/a)</td><td>306.10 (n/a)</td><td>232.80 (n/a)</td><td>113.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.53 <b>(+37.35%)</b></td><td>0.35 (+10.00%)</td><td>0.27 (-10.86%)</td><td>0.24 (-5.01%)</td><td>0.14 <b>(+178.29%)</b></td><td>539.60 (+5.29%)</td><td>419.24 (-0.46%)</td><td>482.90 (+12.17%)</td><td>246.90 <b>(-27.19%)</b></td><td>141.21 <b>(+120.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>512.50 (n/a)</td><td>421.18 (n/a)</td><td>430.50 (n/a)</td><td>339.10 (n/a)</td><td>64.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.46 (-18.61%)</td><td>0.39 (-19.65%)</td><td>0.37 (-19.57%)</td><td>0.32 (-17.10%)</td><td>0.05 <b>(-24.72%)</b></td><td>412.50 <b>(+20.61%)</b></td><td>347.20 <b>(+24.09%)</b></td><td>355.30 <b>(+24.32%)</b></td><td>288.60 <b>(+22.86%)</b></td><td>48.36 (+12.37%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>342.00 (n/a)</td><td>279.80 (n/a)</td><td>285.80 (n/a)</td><td>234.90 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.50 <b>(-26.66%)</b></td><td>0.39 (+0.32%)</td><td>0.44 <b>(+31.35%)</b></td><td>0.22 <b>(+213.20%)</b></td><td>0.11 <b>(-52.17%)</b></td><td>592.10 <b>(-68.07%)</b></td><td>368.60 <b>(-40.73%)</b></td><td>300.90 <b>(-23.86%)</b></td><td>261.80 <b>(+36.35%)</b></td><td>135.09 <b>(-80.59%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.69 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.24 (n/a)</td><td>1854.40 (n/a)</td><td>621.88 (n/a)</td><td>395.20 (n/a)</td><td>192.00 (n/a)</td><td>695.99 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 (-1.66%)</td><td>0.01 (-8.96%)</td><td>0.01 (-4.44%)</td><td>0.01 (-4.34%)</td><td>0.00 (+2.85%)</td><td>484.90 (+4.53%)</td><td>333.80 (+10.30%)</td><td>292.30 (+4.65%)</td><td>235.10 (+1.69%)</td><td>97.50 (+5.51%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.90 (n/a)</td><td>302.64 (n/a)</td><td>279.30 (n/a)</td><td>231.20 (n/a)</td><td>92.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.02 <b>(+31.45%)</b></td><td>0.01 <b>(+26.07%)</b></td><td>0.01 <b>(+54.48%)</b></td><td>0.01 (+4.92%)</td><td>0.01 <b>(+35.51%)</b></td><td>546.80 (-4.69%)</td><td>345.22 (-18.47%)</td><td>295.80 <b>(-35.27%)</b></td><td>196.60 <b>(-23.95%)</b></td><td>135.97 (+0.60%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.70 (n/a)</td><td>423.42 (n/a)</td><td>457.00 (n/a)</td><td>258.50 (n/a)</td><td>135.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.00 <b>(+250.00%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (n/a)</td><td>23734.84 (+6.73%)</td><td>18436.34 (-3.85%)</td><td>21309.47 (+16.32%)</td><td>5875.93 <b>(-64.60%)</b></td><td>7419.25 <b>(+209.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22238.43 (n/a)</td><td>19174.41 (n/a)</td><td>18319.39 (n/a)</td><td>16597.11 (n/a)</td><td>2397.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.00 (+0.00%)</td><td>0.00 (-6.25%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-4.40%)</td><td>22543.35 (+8.72%)</td><td>16236.29 (+10.53%)</td><td>17448.61 (+10.09%)</td><td>7356.13 (-5.69%)</td><td>5983.84 (+8.85%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20735.50 (n/a)</td><td>14690.06 (n/a)</td><td>15850.02 (n/a)</td><td>7800.25 (n/a)</td><td>5497.28 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (+12.11%)</td><td>0.12 <b>(+21.33%)</b></td><td>0.13 <b>(+40.72%)</b></td><td>0.08 (+11.44%)</td><td>0.03 <b>(+35.77%)</b></td><td>25642.24 (-10.26%)</td><td>18948.67 (-15.71%)</td><td>16186.29 <b>(-28.95%)</b></td><td>13895.47 (-10.81%)</td><td>5365.46 (+15.39%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28572.76 (n/a)</td><td>22480.18 (n/a)</td><td>22782.06 (n/a)</td><td>15579.71 (n/a)</td><td>4649.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.60 <b>(-39.80%)</b></td><td>1.28 (-15.17%)</td><td>1.38 <b>(+23.43%)</b></td><td>0.51 (+13.63%)</td><td>0.44 <b>(-51.74%)</b></td><td>2063.70 (-12.00%)</td><td>985.00 (-4.02%)</td><td>758.30 (-18.99%)</td><td>655.70 <b>(+66.13%)</b></td><td>604.91 <b>(-22.92%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.66 (n/a)</td><td>1.51 (n/a)</td><td>1.12 (n/a)</td><td>0.45 (n/a)</td><td>0.92 (n/a)</td><td>2345.00 (n/a)</td><td>1026.26 (n/a)</td><td>936.00 (n/a)</td><td>394.70 (n/a)</td><td>784.80 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.87 (-7.87%)</td><td>1.71 (-17.37%)</td><td>1.57 (-1.03%)</td><td>1.14 (-1.27%)</td><td>0.68 <b>(-24.28%)</b></td><td>917.80 (+1.29%)</td><td>674.96 (+15.01%)</td><td>668.70 (+1.04%)</td><td>365.30 (+8.56%)</td><td>205.31 (-14.63%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.12 (n/a)</td><td>2.07 (n/a)</td><td>1.58 (n/a)</td><td>1.16 (n/a)</td><td>0.89 (n/a)</td><td>906.10 (n/a)</td><td>586.88 (n/a)</td><td>661.80 (n/a)</td><td>336.50 (n/a)</td><td>240.50 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.18 <b>(+20.10%)</b></td><td>2.67 <b>(+52.81%)</b></td><td>2.38 <b>(+47.17%)</b></td><td>1.69 <b>(+204.97%)</b></td><td>1.03 (-3.63%)</td><td>619.10 <b>(-67.21%)</b></td><td>439.08 <b>(-47.95%)</b></td><td>441.20 <b>(-32.05%)</b></td><td>251.00 (-16.72%)</td><td>154.54 <b>(-74.64%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.48 (n/a)</td><td>1.75 (n/a)</td><td>1.61 (n/a)</td><td>0.56 (n/a)</td><td>1.07 (n/a)</td><td>1888.20 (n/a)</td><td>843.54 (n/a)</td><td>649.30 (n/a)</td><td>301.40 (n/a)</td><td>609.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.82 (-16.18%)</td><td>1.36 <b>(-24.74%)</b></td><td>1.53 (-15.25%)</td><td>0.59 <b>(-60.51%)</b></td><td>0.50 <b>(+72.00%)</b></td><td>1790.70 <b>(+153.25%)</b></td><td>913.06 <b>(+54.48%)</b></td><td>685.60 (+18.00%)</td><td>574.90 (+19.30%)</td><td>506.93 <b>(+431.34%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.18 (n/a)</td><td>1.81 (n/a)</td><td>1.80 (n/a)</td><td>1.48 (n/a)</td><td>0.29 (n/a)</td><td>707.10 (n/a)</td><td>591.04 (n/a)</td><td>581.00 (n/a)</td><td>481.90 (n/a)</td><td>95.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>4.41 <b>(+354.40%)</b></td><td>2.85 <b>(+287.85%)</b></td><td>2.89 <b>(+355.16%)</b></td><td>1.78 <b>(+205.94%)</b></td><td>1.12 <b>(+546.34%)</b></td><td>1180.90 <b>(-67.31%)</b></td><td>835.72 <b>(-71.94%)</b></td><td>725.60 <b>(-78.03%)</b></td><td>475.80 <b>(-77.99%)</b></td><td>324.18 <b>(-49.46%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.97 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.58 (n/a)</td><td>0.17 (n/a)</td><td>3612.80 (n/a)</td><td>2978.46 (n/a)</td><td>3302.50 (n/a)</td><td>2162.10 (n/a)</td><td>641.40 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.45 (+6.59%)</td><td>4.06 (+16.88%)</td><td>4.96 <b>(+49.87%)</b></td><td>0.56 (-4.47%)</td><td>2.26 (+11.42%)</td><td>3726.10 (+4.68%)</td><td>1105.86 (-3.44%)</td><td>422.40 <b>(-33.28%)</b></td><td>325.20 (-6.17%)</td><td>1469.33 (+8.24%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.05 (n/a)</td><td>3.47 (n/a)</td><td>3.31 (n/a)</td><td>0.59 (n/a)</td><td>2.02 (n/a)</td><td>3559.40 (n/a)</td><td>1145.20 (n/a)</td><td>633.10 (n/a)</td><td>346.60 (n/a)</td><td>1357.43 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.10 (-5.63%)</td><td>3.31 <b>(+31.15%)</b></td><td>3.91 <b>(+88.54%)</b></td><td>0.97 <b>(+66.71%)</b></td><td>2.07 (-13.84%)</td><td>2171.10 <b>(-40.02%)</b></td><td>981.60 <b>(-44.88%)</b></td><td>535.70 <b>(-46.97%)</b></td><td>343.90 (+5.95%)</td><td>767.40 <b>(-49.54%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.46 (n/a)</td><td>2.53 (n/a)</td><td>2.08 (n/a)</td><td>0.58 (n/a)</td><td>2.40 (n/a)</td><td>3619.50 (n/a)</td><td>1780.70 (n/a)</td><td>1010.10 (n/a)</td><td>324.60 (n/a)</td><td>1520.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.76 <b>(-32.09%)</b></td><td>1.89 <b>(-25.72%)</b></td><td>1.99 <b>(-32.31%)</b></td><td>0.60 (+2.96%)</td><td>1.34 <b>(-35.12%)</b></td><td>3518.70 (-2.87%)</td><td>1880.84 (+5.09%)</td><td>1052.10 <b>(+47.75%)</b></td><td>558.10 <b>(+47.26%)</b></td><td>1468.72 (-10.88%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.53 (n/a)</td><td>2.55 (n/a)</td><td>2.94 (n/a)</td><td>0.58 (n/a)</td><td>2.07 (n/a)</td><td>3622.70 (n/a)</td><td>1789.76 (n/a)</td><td>712.10 (n/a)</td><td>379.00 (n/a)</td><td>1648.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.91 <b>(-31.16%)</b></td><td>2.83 (-2.15%)</td><td>3.01 (+5.28%)</td><td>0.87 <b>(+48.12%)</b></td><td>1.19 <b>(-34.62%)</b></td><td>2408.90 <b>(-32.49%)</b></td><td>997.48 <b>(-20.32%)</b></td><td>695.80 (-5.01%)</td><td>536.10 <b>(+45.28%)</b></td><td>794.52 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.68 (n/a)</td><td>2.89 (n/a)</td><td>2.86 (n/a)</td><td>0.59 (n/a)</td><td>1.83 (n/a)</td><td>3568.10 (n/a)</td><td>1251.86 (n/a)</td><td>732.50 (n/a)</td><td>369.00 (n/a)</td><td>1308.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>6.39 (+14.65%)</td><td>3.99 <b>(+33.27%)</b></td><td>3.98 <b>(+98.75%)</b></td><td>2.01 <b>(+237.20%)</b></td><td>1.65 <b>(-30.82%)</b></td><td>1041.90 <b>(-70.34%)</b></td><td>610.54 <b>(-56.17%)</b></td><td>526.70 <b>(-49.68%)</b></td><td>328.20 (-12.78%)</td><td>273.99 <b>(-78.89%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.57 (n/a)</td><td>2.99 (n/a)</td><td>2.00 (n/a)</td><td>0.60 (n/a)</td><td>2.38 (n/a)</td><td>3513.30 (n/a)</td><td>1393.04 (n/a)</td><td>1046.80 (n/a)</td><td>376.30 (n/a)</td><td>1297.93 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>5.32 (-2.88%)</td><td>3.74 (-15.52%)</td><td>3.72 (-6.31%)</td><td>2.12 <b>(-38.80%)</b></td><td>1.15 <b>(+24.50%)</b></td><td>1981.90 <b>(+63.39%)</b></td><td>1226.82 <b>(+25.12%)</b></td><td>1128.70 (+6.73%)</td><td>788.20 (+2.97%)</td><td>448.80 <b>(+128.61%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.48 (n/a)</td><td>4.42 (n/a)</td><td>3.97 (n/a)</td><td>3.46 (n/a)</td><td>0.92 (n/a)</td><td>1213.00 (n/a)</td><td>980.50 (n/a)</td><td>1057.50 (n/a)</td><td>765.50 (n/a)</td><td>196.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>7.50 (-4.59%)</td><td>6.27 (-4.55%)</td><td>5.89 (-19.14%)</td><td>5.79 <b>(+44.85%)</b></td><td>0.73 <b>(-54.47%)</b></td><td>724.30 <b>(-30.97%)</b></td><td>675.52 (-0.66%)</td><td>711.70 <b>(+23.67%)</b></td><td>559.10 (+4.82%)</td><td>70.32 <b>(-67.40%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.86 (n/a)</td><td>6.57 (n/a)</td><td>7.29 (n/a)</td><td>4.00 (n/a)</td><td>1.60 (n/a)</td><td>1049.20 (n/a)</td><td>680.00 (n/a)</td><td>575.50 (n/a)</td><td>533.40 (n/a)</td><td>215.70 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>8.71 (-13.50%)</td><td>6.56 (-4.26%)</td><td>7.31 (+12.13%)</td><td>3.69 <b>(-25.68%)</b></td><td>2.35 <b>(+21.06%)</b></td><td>1136.70 <b>(+34.57%)</b></td><td>723.84 (+11.87%)</td><td>573.60 (-10.82%)</td><td>481.70 (+15.63%)</td><td>297.88 <b>(+89.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>10.07 (n/a)</td><td>6.85 (n/a)</td><td>6.52 (n/a)</td><td>4.97 (n/a)</td><td>1.94 (n/a)</td><td>844.70 (n/a)</td><td>647.04 (n/a)</td><td>643.20 (n/a)</td><td>416.60 (n/a)</td><td>157.20 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>10.22 <b>(+22.99%)</b></td><td>7.26 <b>(+32.33%)</b></td><td>6.81 (+1.77%)</td><td>5.64 <b>(+394.20%)</b></td><td>1.74 <b>(-45.56%)</b></td><td>743.80 <b>(-79.77%)</b></td><td>600.28 <b>(-54.91%)</b></td><td>615.70 (-1.74%)</td><td>410.50 (-18.70%)</td><td>121.50 <b>(-91.03%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.31 (n/a)</td><td>5.49 (n/a)</td><td>6.69 (n/a)</td><td>1.14 (n/a)</td><td>3.20 (n/a)</td><td>3675.90 (n/a)</td><td>1331.44 (n/a)</td><td>626.60 (n/a)</td><td>504.90 (n/a)</td><td>1355.15 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>10.00 (+14.64%)</td><td>6.54 (-3.76%)</td><td>7.03 (+7.50%)</td><td>4.27 (+5.39%)</td><td>2.38 <b>(+29.90%)</b></td><td>982.50 (-5.11%)</td><td>712.60 (+7.43%)</td><td>596.30 (-6.97%)</td><td>419.50 (-12.77%)</td><td>253.44 (+14.50%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.72 (n/a)</td><td>6.80 (n/a)</td><td>6.54 (n/a)</td><td>4.05 (n/a)</td><td>1.84 (n/a)</td><td>1035.40 (n/a)</td><td>663.32 (n/a)</td><td>641.00 (n/a)</td><td>480.90 (n/a)</td><td>221.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>9.48 <b>(+26.20%)</b></td><td>6.10 (+18.63%)</td><td>6.55 (+3.20%)</td><td>1.17 (-1.55%)</td><td>3.03 (+18.03%)</td><td>3589.00 (+1.57%)</td><td>1187.24 (-7.71%)</td><td>640.80 (-3.10%)</td><td>442.30 <b>(-20.75%)</b></td><td>1345.29 (+5.88%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.51 (n/a)</td><td>5.14 (n/a)</td><td>6.34 (n/a)</td><td>1.19 (n/a)</td><td>2.56 (n/a)</td><td>3533.40 (n/a)</td><td>1286.38 (n/a)</td><td>661.30 (n/a)</td><td>558.10 (n/a)</td><td>1270.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>1.60 (-15.47%)</td><td>0.93 <b>(-25.96%)</b></td><td>0.71 <b>(-56.46%)</b></td><td>0.24 <b>(+51.51%)</b></td><td>0.56 <b>(-23.31%)</b></td><td>2180.20 <b>(-34.00%)</b></td><td>877.86 (-8.98%)</td><td>737.70 <b>(+129.67%)</b></td><td>326.80 (+18.28%)</td><td>755.44 <b>(-42.53%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.90 (n/a)</td><td>1.25 (n/a)</td><td>1.63 (n/a)</td><td>0.16 (n/a)</td><td>0.73 (n/a)</td><td>3303.20 (n/a)</td><td>964.46 (n/a)</td><td>321.20 (n/a)</td><td>276.30 (n/a)</td><td>1314.57 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.43 (+0.32%)</td><td>1.73 <b>(+28.13%)</b></td><td>2.01 <b>(+47.65%)</b></td><td>0.30 (+2.34%)</td><td>0.87 (+15.95%)</td><td>3456.00 (-2.29%)</td><td>1106.50 (-12.34%)</td><td>520.70 <b>(-32.28%)</b></td><td>431.30 (-0.32%)</td><td>1317.19 (+2.85%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.42 (n/a)</td><td>1.35 (n/a)</td><td>1.36 (n/a)</td><td>0.30 (n/a)</td><td>0.75 (n/a)</td><td>3537.00 (n/a)</td><td>1262.30 (n/a)</td><td>768.90 (n/a)</td><td>432.70 (n/a)</td><td>1280.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>3.06 (-17.42%)</td><td>1.81 <b>(-28.73%)</b></td><td>2.15 (-15.79%)</td><td>0.59 (-0.52%)</td><td>1.16 (-5.62%)</td><td>3543.10 (+0.53%)</td><td>1901.40 <b>(+48.77%)</b></td><td>973.50 (+18.75%)</td><td>684.50 <b>(+21.11%)</b></td><td>1490.88 (+18.06%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.71 (n/a)</td><td>2.54 (n/a)</td><td>2.56 (n/a)</td><td>0.60 (n/a)</td><td>1.23 (n/a)</td><td>3524.50 (n/a)</td><td>1278.12 (n/a)</td><td>819.80 (n/a)</td><td>565.20 (n/a)</td><td>1262.86 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>2.23 (+12.18%)</td><td>1.07 <b>(-28.12%)</b></td><td>0.84 <b>(-44.12%)</b></td><td>0.71 (-4.38%)</td><td>0.65 <b>(+39.96%)</b></td><td>741.00 (+4.59%)</td><td>588.02 <b>(+48.76%)</b></td><td>622.30 <b>(+78.98%)</b></td><td>235.40 (-10.87%)</td><td>205.71 (+15.10%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.99 (n/a)</td><td>1.49 (n/a)</td><td>1.51 (n/a)</td><td>0.74 (n/a)</td><td>0.46 (n/a)</td><td>708.50 (n/a)</td><td>395.28 (n/a)</td><td>347.70 (n/a)</td><td>264.10 (n/a)</td><td>178.73 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.13 (+3.85%)</td><td>0.10 (+19.76%)</td><td>0.13 <b>(+54.07%)</b></td><td>0.05 (-13.88%)</td><td>0.04 <b>(+44.13%)</b></td><td>635.30 (+16.12%)</td><td>362.38 (-9.82%)</td><td>258.10 <b>(-35.09%)</b></td><td>246.00 (-3.68%)</td><td>170.44 <b>(+55.34%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.10 (n/a)</td><td>401.82 (n/a)</td><td>397.60 (n/a)</td><td>255.40 (n/a)</td><td>109.72 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.15 (+1.88%)</td><td>0.10 <b>(+48.06%)</b></td><td>0.11 <b>(+106.03%)</b></td><td>0.05 <b>(+193.71%)</b></td><td>0.04 (-9.53%)</td><td>707.90 <b>(-65.95%)</b></td><td>390.16 <b>(-50.64%)</b></td><td>285.60 <b>(-51.47%)</b></td><td>218.20 (-1.84%)</td><td>206.64 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2079.30 (n/a)</td><td>790.46 (n/a)</td><td>588.50 (n/a)</td><td>222.30 (n/a)</td><td>735.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.25 (+0.08%)</td><td>0.16 (+14.20%)</td><td>0.19 <b>(+33.36%)</b></td><td>0.03 (-18.59%)</td><td>0.09 (+15.64%)</td><td>2514.80 <b>(+22.84%)</b></td><td>796.38 (+6.78%)</td><td>344.70 <b>(-25.02%)</b></td><td>262.60 (-0.08%)</td><td>968.53 <b>(+31.52%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>2047.20 (n/a)</td><td>745.78 (n/a)</td><td>459.70 (n/a)</td><td>262.80 (n/a)</td><td>736.39 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.29 (-10.61%)</td><td>0.22 (-3.22%)</td><td>0.22 (-0.23%)</td><td>0.12 (-11.36%)</td><td>0.06 <b>(-21.53%)</b></td><td>535.30 (+12.84%)</td><td>330.74 (+0.76%)</td><td>298.60 (+0.23%)</td><td>224.10 (+11.83%)</td><td>122.51 (-0.35%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>474.40 (n/a)</td><td>328.26 (n/a)</td><td>297.90 (n/a)</td><td>200.40 (n/a)</td><td>122.94 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.27 (-4.44%)</td><td>0.19 (-2.15%)</td><td>0.15 (-18.18%)</td><td>0.12 (-19.21%)</td><td>0.07 <b>(+29.65%)</b></td><td>554.30 <b>(+23.76%)</b></td><td>389.06 (+8.08%)</td><td>446.60 <b>(+22.22%)</b></td><td>241.80 (+4.63%)</td><td>138.81 <b>(+52.94%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>447.90 (n/a)</td><td>359.98 (n/a)</td><td>365.40 (n/a)</td><td>231.10 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.42 <b>(-46.56%)</b></td><td>0.27 <b>(-25.55%)</b></td><td>0.26 (-6.33%)</td><td>0.05 <b>(-75.46%)</b></td><td>0.15 <b>(-35.67%)</b></td><td>2467.80 <b>(+307.56%)</b></td><td>840.90 <b>(+91.04%)</b></td><td>511.30 (+6.77%)</td><td>312.90 <b>(+87.14%)</b></td><td>917.60 <b>(+462.36%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>605.50 (n/a)</td><td>440.18 (n/a)</td><td>478.90 (n/a)</td><td>167.20 (n/a)</td><td>163.17 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.55 (+2.61%)</td><td>0.37 (-9.27%)</td><td>0.31 <b>(-32.31%)</b></td><td>0.26 (+17.95%)</td><td>0.13 (-3.09%)</td><td>507.30 (-15.22%)</td><td>390.54 (+8.00%)</td><td>429.50 <b>(+47.75%)</b></td><td>240.20 (-2.56%)</td><td>122.01 (-17.64%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.45 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>598.40 (n/a)</td><td>361.62 (n/a)</td><td>290.70 (n/a)</td><td>246.50 (n/a)</td><td>148.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.54 <b>(-20.26%)</b></td><td>0.37 (+4.52%)</td><td>0.30 (+4.61%)</td><td>0.25 (+2.54%)</td><td>0.13 <b>(-27.37%)</b></td><td>517.90 (-2.49%)</td><td>389.42 (-8.26%)</td><td>434.90 (-4.40%)</td><td>240.50 <b>(+25.39%)</b></td><td>126.20 (-6.11%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.68 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>531.10 (n/a)</td><td>424.48 (n/a)</td><td>454.90 (n/a)</td><td>191.80 (n/a)</td><td>134.41 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:19:28</td><td>0.06 (+8.69%)</td><td>0.05 (+11.53%)</td><td>0.06 <b>(+48.87%)</b></td><td>0.03 (-17.93%)</td><td>0.02 (+18.39%)</td><td>642.10 <b>(+21.84%)</b></td><td>380.26 (-6.51%)</td><td>296.20 <b>(-32.82%)</b></td><td>257.20 (-8.01%)</td><td>161.85 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>406.76 (n/a)</td><td>440.90 (n/a)</td><td>279.60 (n/a)</td><td>118.59 (n/a)</td>
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
