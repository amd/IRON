# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (+10.51%)</td><td>0.04 (+15.81%)</td><td>0.04 (+5.92%)</td><td>0.04 <b>(+55.38%)</b></td><td>0.01 <b>(-44.20%)</b></td><td>345.80 <b>(-35.64%)</b></td><td>300.38 (-17.79%)</td><td>301.10 (-5.58%)</td><td>249.30 (-9.51%)</td><td>34.62 <b>(-67.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>365.40 (n/a)</td><td>318.90 (n/a)</td><td>275.50 (n/a)</td><td>108.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (+10.54%)</td><td>0.03 (-1.15%)</td><td>0.02 (-19.87%)</td><td>0.02 (-9.36%)</td><td>0.01 <b>(+41.24%)</b></td><td>661.60 (+10.32%)</td><td>481.64 (+8.23%)</td><td>563.80 <b>(+24.79%)</b></td><td>263.20 (-9.55%)</td><td>181.60 <b>(+40.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.70 (n/a)</td><td>445.02 (n/a)</td><td>451.80 (n/a)</td><td>291.00 (n/a)</td><td>128.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 <b>(-44.43%)</b></td><td>0.03 <b>(-34.78%)</b></td><td>0.03 <b>(-36.57%)</b></td><td>0.02 (+9.13%)</td><td>0.00 <b>(-74.40%)</b></td><td>566.00 (-8.37%)</td><td>471.26 <b>(+27.66%)</b></td><td>484.10 <b>(+57.69%)</b></td><td>350.60 <b>(+79.89%)</b></td><td>77.77 <b>(-58.70%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>617.70 (n/a)</td><td>369.14 (n/a)</td><td>307.00 (n/a)</td><td>194.90 (n/a)</td><td>188.30 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(-21.94%)</b></td><td>0.01 <b>(-24.13%)</b></td><td>0.01 <b>(-45.47%)</b></td><td>0.01 <b>(+30.73%)</b></td><td>0.00 <b>(-61.80%)</b></td><td>516.00 <b>(-23.51%)</b></td><td>451.76 (+16.48%)</td><td>490.00 <b>(+83.38%)</b></td><td>336.90 <b>(+28.10%)</b></td><td>72.69 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.60 (n/a)</td><td>387.84 (n/a)</td><td>267.20 (n/a)</td><td>263.00 (n/a)</td><td>183.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(+25.15%)</b></td><td>0.02 <b>(+25.30%)</b></td><td>0.02 <b>(+29.94%)</b></td><td>0.01 (-10.82%)</td><td>0.01 <b>(+76.99%)</b></td><td>621.60 (+12.14%)</td><td>388.36 (-12.79%)</td><td>325.20 <b>(-23.05%)</b></td><td>232.20 <b>(-20.07%)</b></td><td>168.43 <b>(+56.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.30 (n/a)</td><td>445.34 (n/a)</td><td>422.60 (n/a)</td><td>290.50 (n/a)</td><td>107.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (-11.04%)</td><td>0.01 (-3.09%)</td><td>0.02 (-18.02%)</td><td>0.01 <b>(+341.72%)</b></td><td>0.00 <b>(-45.28%)</b></td><td>559.80 <b>(-77.36%)</b></td><td>383.64 <b>(-47.50%)</b></td><td>347.60 <b>(+21.96%)</b></td><td>259.50 (+12.39%)</td><td>124.46 <b>(-87.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2472.60 (n/a)</td><td>730.70 (n/a)</td><td>285.00 (n/a)</td><td>230.90 (n/a)</td><td>976.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (-14.32%)</td><td>0.02 (-0.70%)</td><td>0.02 (+15.08%)</td><td>0.01 (+8.30%)</td><td>0.00 <b>(-41.16%)</b></td><td>482.60 (-7.65%)</td><td>361.24 (-5.83%)</td><td>327.10 (-13.12%)</td><td>288.50 (+16.71%)</td><td>85.33 <b>(-37.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>383.62 (n/a)</td><td>376.50 (n/a)</td><td>247.20 (n/a)</td><td>136.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(-27.74%)</b></td><td>0.01 (-6.13%)</td><td>0.01 (-2.83%)</td><td>0.01 (+9.62%)</td><td>0.00 <b>(-36.77%)</b></td><td>574.70 (-8.78%)</td><td>435.76 (+0.99%)</td><td>460.00 (+2.91%)</td><td>291.50 <b>(+38.41%)</b></td><td>127.34 (-14.53%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.00 (n/a)</td><td>431.48 (n/a)</td><td>447.00 (n/a)</td><td>210.60 (n/a)</td><td>148.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 <b>(-31.18%)</b></td><td>0.01 (-17.04%)</td><td>0.01 (-6.42%)</td><td>0.01 (-12.51%)</td><td>0.00 <b>(-52.73%)</b></td><td>558.80 (+14.30%)</td><td>485.70 (+15.64%)</td><td>500.70 (+6.85%)</td><td>355.80 <b>(+45.28%)</b></td><td>79.79 <b>(-20.72%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>488.90 (n/a)</td><td>420.02 (n/a)</td><td>468.60 (n/a)</td><td>244.90 (n/a)</td><td>100.64 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>501.00 (n/a)</td><td>338.54 (n/a)</td><td>249.30 (n/a)</td><td>212.20 (n/a)</td><td>141.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.30 (n/a)</td><td>367.32 (n/a)</td><td>299.50 (n/a)</td><td>297.40 (n/a)</td><td>135.58 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>676.20 (n/a)</td><td>439.36 (n/a)</td><td>399.20 (n/a)</td><td>250.30 (n/a)</td><td>181.11 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.00 (n/a)</td><td>307.34 (n/a)</td><td>261.10 (n/a)</td><td>242.80 (n/a)</td><td>111.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>456.00 (n/a)</td><td>314.10 (n/a)</td><td>296.30 (n/a)</td><td>223.00 (n/a)</td><td>98.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1857.60 (n/a)</td><td>674.08 (n/a)</td><td>428.60 (n/a)</td><td>252.00 (n/a)</td><td>672.93 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gelu</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.90 (n/a)</td><td>329.88 (n/a)</td><td>303.80 (n/a)</td><td>263.90 (n/a)</td><td>86.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.60 (n/a)</td><td>351.94 (n/a)</td><td>287.70 (n/a)</td><td>227.90 (n/a)</td><td>119.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.00 (n/a)</td><td>379.08 (n/a)</td><td>300.30 (n/a)</td><td>259.00 (n/a)</td><td>128.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.50 (n/a)</td><td>541.08 (n/a)</td><td>547.30 (n/a)</td><td>439.40 (n/a)</td><td>64.61 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1109.80 (n/a)</td><td>612.24 (n/a)</td><td>515.00 (n/a)</td><td>375.50 (n/a)</td><td>288.08 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.90 (n/a)</td><td>517.16 (n/a)</td><td>555.40 (n/a)</td><td>286.70 (n/a)</td><td>163.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (-19.01%)</td><td>0.41 (+4.13%)</td><td>0.35 (+6.55%)</td><td>0.34 (+12.13%)</td><td>0.10 <b>(-41.39%)</b></td><td>648.10 (-10.82%)</td><td>560.96 (-9.11%)</td><td>633.80 (-6.15%)</td><td>397.60 <b>(+23.48%)</b></td><td>115.63 <b>(-30.79%)</b></td><td>23.74 (-19.01%)</td><td>17.50 (+4.13%)</td><td>14.89 (+6.55%)</td><td>14.56 (+12.13%)</td><td>4.11 <b>(-41.39%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.69 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>726.70 (n/a)</td><td>617.20 (n/a)</td><td>675.30 (n/a)</td><td>322.00 (n/a)</td><td>167.08 (n/a)</td><td>29.31 (n/a)</td><td>16.80 (n/a)</td><td>13.97 (n/a)</td><td>12.99 (n/a)</td><td>7.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.48 (-9.89%)</td><td>0.40 (-13.17%)</td><td>0.39 (-15.64%)</td><td>0.29 (-14.71%)</td><td>0.07 (-6.75%)</td><td>754.90 (+17.24%)</td><td>569.38 (+15.58%)</td><td>562.10 (+18.54%)</td><td>462.00 (+10.98%)</td><td>113.60 <b>(+23.12%)</b></td><td>20.43 (-9.89%)</td><td>17.05 (-13.17%)</td><td>16.79 (-15.64%)</td><td>12.50 (-14.71%)</td><td>3.03 (-6.75%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>643.90 (n/a)</td><td>492.64 (n/a)</td><td>474.20 (n/a)</td><td>416.30 (n/a)</td><td>92.27 (n/a)</td><td>22.67 (n/a)</td><td>19.64 (n/a)</td><td>19.90 (n/a)</td><td>14.66 (n/a)</td><td>3.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.31 (-0.79%)</td><td>0.30 (-0.85%)</td><td>0.30 (+0.01%)</td><td>0.29 (-1.67%)</td><td>0.01 <b>(+22.22%)</b></td><td>87021.00 (+1.70%)</td><td>83810.68 (+0.87%)</td><td>82856.30 (-0.01%)</td><td>81552.30 (+0.80%)</td><td>2280.41 <b>(+25.29%)</b></td><td>210.66 (-0.79%)</td><td>205.10 (-0.85%)</td><td>207.35 (+0.01%)</td><td>197.42 (-1.67%)</td><td>5.52 <b>(+22.22%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85569.90 (n/a)</td><td>83085.36 (n/a)</td><td>82863.00 (n/a)</td><td>80906.70 (n/a)</td><td>1820.16 (n/a)</td><td>212.34 (n/a)</td><td>206.85 (n/a)</td><td>207.33 (n/a)</td><td>200.77 (n/a)</td><td>4.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>1.02 (-2.06%)</td><td>1.01 (-0.69%)</td><td>1.01 (-1.20%)</td><td>1.00 (+1.02%)</td><td>0.01 <b>(-53.57%)</b></td><td>25124.90 (-1.01%)</td><td>24931.00 (+0.67%)</td><td>24992.40 (+1.22%)</td><td>24684.20 (+2.10%)</td><td>210.73 <b>(-53.09%)</b></td><td>695.99 (-2.06%)</td><td>689.14 (-0.69%)</td><td>687.40 (-1.20%)</td><td>683.78 (+1.02%)</td><td>5.84 <b>(-53.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>1.02 (n/a)</td><td>0.99 (n/a)</td><td>0.02 (n/a)</td><td>25380.20 (n/a)</td><td>24764.18 (n/a)</td><td>24691.80 (n/a)</td><td>24176.40 (n/a)</td><td>449.22 (n/a)</td><td>710.61 (n/a)</td><td>693.92 (n/a)</td><td>695.77 (n/a)</td><td>676.90 (n/a)</td><td>12.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>3.85 (+2.76%)</td><td>2.93 (+17.67%)</td><td>3.56 <b>(+67.70%)</b></td><td>1.72 <b>(+30.53%)</b></td><td>1.02 (-0.16%)</td><td>4674.40 <b>(-23.39%)</b></td><td>3091.62 (-17.20%)</td><td>2263.50 <b>(-40.37%)</b></td><td>2095.80 (-2.68%)</td><td>1233.19 <b>(-22.40%)</b></td><td>1008.67 (+2.76%)</td><td>768.45 (+17.67%)</td><td>933.90 <b>(+67.70%)</b></td><td>452.24 <b>(+30.53%)</b></td><td>266.49 (-0.16%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.74 (n/a)</td><td>2.49 (n/a)</td><td>2.12 (n/a)</td><td>1.32 (n/a)</td><td>1.02 (n/a)</td><td>6101.60 (n/a)</td><td>3734.00 (n/a)</td><td>3796.00 (n/a)</td><td>2153.60 (n/a)</td><td>1589.10 (n/a)</td><td>981.56 (n/a)</td><td>653.07 (n/a)</td><td>556.88 (n/a)</td><td>346.46 (n/a)</td><td>266.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.34 <b>(+76.62%)</b></td><td>0.21 (+16.35%)</td><td>0.18 (-1.94%)</td><td>0.16 (-3.05%)</td><td>0.07 <b>(+605.22%)</b></td><td>7566.70 (+3.14%)</td><td>6269.56 (-7.95%)</td><td>6858.00 (+1.98%)</td><td>3614.30 <b>(-43.38%)</b></td><td>1559.94 <b>(+292.61%)</b></td><td>18.57 <b>(+76.62%)</b></td><td>11.49 (+16.35%)</td><td>9.79 (-1.94%)</td><td>8.87 (-3.05%)</td><td>4.01 <b>(+605.22%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>7336.20 (n/a)</td><td>6811.00 (n/a)</td><td>6724.90 (n/a)</td><td>6383.60 (n/a)</td><td>397.33 (n/a)</td><td>10.51 (n/a)</td><td>9.88 (n/a)</td><td>9.98 (n/a)</td><td>9.15 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>3.76 (n/a)</td><td>3.54 (n/a)</td><td>3.64 (n/a)</td><td>3.28 (n/a)</td><td>0.22 (n/a)</td><td>3.76 (n/a)</td><td>3.54 (n/a)</td><td>3.64 (n/a)</td><td>3.27 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>7.15 (-5.60%)</td><td>6.45 (+1.52%)</td><td>6.35 (+6.48%)</td><td>5.71 (+0.41%)</td><td>0.60 <b>(-25.73%)</b></td><td>7.14 (-5.60%)</td><td>6.44 (+1.52%)</td><td>6.35 (+6.48%)</td><td>5.71 (+0.41%)</td><td>0.60 <b>(-25.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>7.57 (n/a)</td><td>6.35 (n/a)</td><td>5.97 (n/a)</td><td>5.69 (n/a)</td><td>0.81 (n/a)</td><td>7.57 (n/a)</td><td>6.35 (n/a)</td><td>5.96 (n/a)</td><td>5.69 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>13.37 <b>(+23.40%)</b></td><td>11.51 <b>(+29.26%)</b></td><td>11.65 <b>(+35.38%)</b></td><td>10.07 <b>(+35.68%)</b></td><td>1.30 (+2.56%)</td><td>13.36 <b>(+23.40%)</b></td><td>11.51 <b>(+29.26%)</b></td><td>11.65 <b>(+35.38%)</b></td><td>10.06 <b>(+35.67%)</b></td><td>1.30 (+2.56%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>10.84 (n/a)</td><td>8.91 (n/a)</td><td>8.61 (n/a)</td><td>7.42 (n/a)</td><td>1.27 (n/a)</td><td>10.83 (n/a)</td><td>8.90 (n/a)</td><td>8.60 (n/a)</td><td>7.42 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>3.88 (n/a)</td><td>3.71 (n/a)</td><td>3.73 (n/a)</td><td>3.56 (n/a)</td><td>0.12 (n/a)</td><td>3.87 (n/a)</td><td>3.71 (n/a)</td><td>3.72 (n/a)</td><td>3.56 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>6.92 (-10.16%)</td><td>5.97 (-4.25%)</td><td>5.68 (-5.38%)</td><td>4.96 (+2.97%)</td><td>0.90 (-17.40%)</td><td>6.91 (-10.16%)</td><td>5.97 (-4.25%)</td><td>5.68 (-5.38%)</td><td>4.95 (+2.97%)</td><td>0.90 (-17.40%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>7.70 (n/a)</td><td>6.24 (n/a)</td><td>6.00 (n/a)</td><td>4.81 (n/a)</td><td>1.09 (n/a)</td><td>7.69 (n/a)</td><td>6.23 (n/a)</td><td>6.00 (n/a)</td><td>4.81 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>13.82 (-1.22%)</td><td>10.31 (+2.83%)</td><td>8.69 (-8.27%)</td><td>7.41 (-6.40%)</td><td>3.12 <b>(+35.09%)</b></td><td>13.81 (-1.22%)</td><td>10.30 (+2.83%)</td><td>8.68 (-8.27%)</td><td>7.41 (-6.40%)</td><td>3.12 <b>(+35.09%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>13.99 (n/a)</td><td>10.03 (n/a)</td><td>9.47 (n/a)</td><td>7.92 (n/a)</td><td>2.31 (n/a)</td><td>13.98 (n/a)</td><td>10.02 (n/a)</td><td>9.47 (n/a)</td><td>7.92 (n/a)</td><td>2.31 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.89 (-2.35%)</td><td>2.03 (+2.11%)</td><td>1.74 <b>(-21.87%)</b></td><td>1.05 (-0.18%)</td><td>0.76 (-12.60%)</td><td>2.88 (-2.36%)</td><td>2.02 (+2.11%)</td><td>1.74 <b>(-21.87%)</b></td><td>1.04 (-0.18%)</td><td>0.76 (-12.60%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>2.96 (n/a)</td><td>1.99 (n/a)</td><td>2.23 (n/a)</td><td>1.05 (n/a)</td><td>0.87 (n/a)</td><td>2.95 (n/a)</td><td>1.98 (n/a)</td><td>2.23 (n/a)</td><td>1.05 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (+8.01%)</td><td>0.38 <b>(+22.51%)</b></td><td>0.39 (+1.91%)</td><td>0.08 <b>(-24.67%)</b></td><td>0.19 (+7.20%)</td><td>0.55 (+8.01%)</td><td>0.38 <b>(+22.51%)</b></td><td>0.38 (+1.91%)</td><td>0.08 <b>(-24.67%)</b></td><td>0.18 (+7.20%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.52 (n/a)</td><td>0.31 (n/a)</td><td>0.38 (n/a)</td><td>0.11 (n/a)</td><td>0.17 (n/a)</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.37 (n/a)</td><td>0.11 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.73 (+18.22%)</td><td>0.57 <b>(+48.70%)</b></td><td>0.60 <b>(+34.46%)</b></td><td>0.37 <b>(+194.64%)</b></td><td>0.14 <b>(-41.17%)</b></td><td>0.72 (+18.22%)</td><td>0.56 <b>(+48.70%)</b></td><td>0.60 <b>(+34.46%)</b></td><td>0.37 <b>(+194.64%)</b></td><td>0.14 <b>(-41.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.62 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.13 (n/a)</td><td>0.23 (n/a)</td><td>0.61 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.13 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.68 (+12.02%)</td><td>1.65 (-11.26%)</td><td>1.75 <b>(-25.04%)</b></td><td>0.45 (+0.88%)</td><td>0.80 (-4.39%)</td><td>2.63 (+12.02%)</td><td>1.62 (-11.26%)</td><td>1.72 <b>(-25.04%)</b></td><td>0.44 (+0.88%)</td><td>0.78 (-4.39%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>2.39 (n/a)</td><td>1.86 (n/a)</td><td>2.34 (n/a)</td><td>0.45 (n/a)</td><td>0.83 (n/a)</td><td>2.35 (n/a)</td><td>1.83 (n/a)</td><td>2.30 (n/a)</td><td>0.44 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>362.46 (n/a)</td><td>262.20 (n/a)</td><td>234.90 (n/a)</td><td>155.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>337.84 (n/a)</td><td>288.30 (n/a)</td><td>179.80 (n/a)</td><td>145.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.90 (n/a)</td><td>358.46 (n/a)</td><td>251.90 (n/a)</td><td>224.60 (n/a)</td><td>179.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1042.70 (n/a)</td><td>478.72 (n/a)</td><td>246.40 (n/a)</td><td>233.20 (n/a)</td><td>357.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.60 (n/a)</td><td>402.58 (n/a)</td><td>290.00 (n/a)</td><td>241.40 (n/a)</td><td>188.36 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.00 (n/a)</td><td>416.06 (n/a)</td><td>427.40 (n/a)</td><td>240.70 (n/a)</td><td>142.47 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (+4.08%)</td><td>0.03 <b>(+23.72%)</b></td><td>0.03 <b>(+47.20%)</b></td><td>0.02 <b>(+34.70%)</b></td><td>0.00 <b>(-36.47%)</b></td><td>387.70 <b>(-25.76%)</b></td><td>293.24 <b>(-23.62%)</b></td><td>280.40 <b>(-32.07%)</b></td><td>237.90 (-3.92%)</td><td>56.41 <b>(-51.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.20 (n/a)</td><td>383.94 (n/a)</td><td>412.80 (n/a)</td><td>247.60 (n/a)</td><td>117.43 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (+8.89%)</td><td>0.03 (+3.44%)</td><td>0.03 (+11.33%)</td><td>0.02 (+0.33%)</td><td>0.01 <b>(+31.84%)</b></td><td>472.10 (-0.34%)</td><td>324.12 (-1.03%)</td><td>275.60 (-10.17%)</td><td>228.60 (-8.16%)</td><td>99.58 (+16.38%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.70 (n/a)</td><td>327.48 (n/a)</td><td>306.80 (n/a)</td><td>248.90 (n/a)</td><td>85.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (-2.41%)</td><td>0.03 (+7.76%)</td><td>0.03 <b>(+25.09%)</b></td><td>0.02 (+10.58%)</td><td>0.01 (-18.91%)</td><td>455.00 (-9.56%)</td><td>329.64 (-10.39%)</td><td>304.20 <b>(-20.07%)</b></td><td>225.30 (+2.46%)</td><td>89.03 <b>(-24.20%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.10 (n/a)</td><td>367.86 (n/a)</td><td>380.60 (n/a)</td><td>219.90 (n/a)</td><td>117.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 <b>(-22.67%)</b></td><td>0.03 (+18.49%)</td><td>0.03 <b>(+66.23%)</b></td><td>0.02 <b>(+67.94%)</b></td><td>0.01 <b>(-50.23%)</b></td><td>465.00 <b>(-40.45%)</b></td><td>336.02 <b>(-30.65%)</b></td><td>319.20 <b>(-39.85%)</b></td><td>230.20 <b>(+29.33%)</b></td><td>93.47 <b>(-59.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>780.90 (n/a)</td><td>484.52 (n/a)</td><td>530.70 (n/a)</td><td>178.00 (n/a)</td><td>230.19 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 <b>(-23.89%)</b></td><td>0.02 <b>(-29.06%)</b></td><td>0.02 <b>(-43.14%)</b></td><td>0.01 (-6.98%)</td><td>0.01 <b>(-30.94%)</b></td><td>590.20 (+7.50%)</td><td>482.14 <b>(+32.69%)</b></td><td>536.10 <b>(+75.83%)</b></td><td>241.90 <b>(+31.40%)</b></td><td>144.08 (-11.47%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.00 (n/a)</td><td>363.36 (n/a)</td><td>304.90 (n/a)</td><td>184.10 (n/a)</td><td>162.75 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 <b>(+40.01%)</b></td><td>0.02 (+4.84%)</td><td>0.02 (-7.98%)</td><td>0.00 <b>(-74.25%)</b></td><td>0.01 <b>(+298.84%)</b></td><td>2102.60 <b>(+288.44%)</b></td><td>746.60 <b>(+59.37%)</b></td><td>517.30 (+8.68%)</td><td>265.00 <b>(-28.59%)</b></td><td>768.94 <b>(+1055.11%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>541.30 (n/a)</td><td>468.48 (n/a)</td><td>476.00 (n/a)</td><td>371.10 (n/a)</td><td>66.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (+8.89%)</td><td>0.03 <b>(+26.45%)</b></td><td>0.03 <b>(+53.06%)</b></td><td>0.02 <b>(+36.26%)</b></td><td>0.01 <b>(-25.04%)</b></td><td>409.40 <b>(-26.60%)</b></td><td>300.84 <b>(-26.65%)</b></td><td>287.10 <b>(-34.66%)</b></td><td>224.20 (-8.15%)</td><td>75.60 <b>(-49.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>410.14 (n/a)</td><td>439.40 (n/a)</td><td>244.10 (n/a)</td><td>150.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(-21.00%)</b></td><td>0.02 (-11.68%)</td><td>0.02 (-7.98%)</td><td>0.01 (-3.08%)</td><td>0.00 <b>(-37.87%)</b></td><td>606.20 (+3.18%)</td><td>479.88 (+8.63%)</td><td>438.60 (+8.67%)</td><td>350.60 <b>(+26.57%)</b></td><td>110.20 <b>(-21.02%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.50 (n/a)</td><td>441.76 (n/a)</td><td>403.60 (n/a)</td><td>277.00 (n/a)</td><td>139.52 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (+7.69%)</td><td>0.02 (-2.82%)</td><td>0.02 <b>(-20.64%)</b></td><td>0.01 (+1.55%)</td><td>0.01 (-7.19%)</td><td>613.70 (-1.54%)</td><td>394.40 (+0.44%)</td><td>375.00 <b>(+26.01%)</b></td><td>245.90 (-7.14%)</td><td>139.47 (-12.56%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.30 (n/a)</td><td>392.66 (n/a)</td><td>297.60 (n/a)</td><td>264.80 (n/a)</td><td>159.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 <b>(+33.58%)</b></td><td>0.03 <b>(+71.73%)</b></td><td>0.03 <b>(+87.45%)</b></td><td>0.02 <b>(+50.09%)</b></td><td>0.01 <b>(+34.69%)</b></td><td>509.50 <b>(-33.37%)</b></td><td>294.68 <b>(-41.82%)</b></td><td>272.10 <b>(-46.64%)</b></td><td>198.30 <b>(-25.14%)</b></td><td>126.45 <b>(-28.67%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>764.70 (n/a)</td><td>506.50 (n/a)</td><td>509.90 (n/a)</td><td>264.90 (n/a)</td><td>177.28 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (+19.71%)</td><td>0.03 <b>(+21.07%)</b></td><td>0.03 <b>(+24.78%)</b></td><td>0.02 <b>(+33.90%)</b></td><td>0.01 (+16.65%)</td><td>454.60 <b>(-25.32%)</b></td><td>319.38 (-18.34%)</td><td>247.00 (-19.83%)</td><td>210.80 (-16.48%)</td><td>117.14 <b>(-24.04%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.70 (n/a)</td><td>391.10 (n/a)</td><td>308.10 (n/a)</td><td>252.40 (n/a)</td><td>154.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 <b>(-27.33%)</b></td><td>0.02 (-9.19%)</td><td>0.02 (+11.74%)</td><td>0.02 <b>(+25.82%)</b></td><td>0.00 <b>(-55.72%)</b></td><td>501.50 <b>(-20.52%)</b></td><td>420.20 (-2.84%)</td><td>453.50 (-10.50%)</td><td>318.90 <b>(+37.58%)</b></td><td>89.86 <b>(-49.53%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.00 (n/a)</td><td>432.48 (n/a)</td><td>506.70 (n/a)</td><td>231.80 (n/a)</td><td>178.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (+3.04%)</td><td>0.02 (-15.88%)</td><td>0.02 (-14.00%)</td><td>0.00 <b>(-72.12%)</b></td><td>0.01 <b>(+21.70%)</b></td><td>1899.10 <b>(+258.66%)</b></td><td>645.40 <b>(+79.42%)</b></td><td>331.50 (+16.27%)</td><td>218.80 (-2.97%)</td><td>705.60 <b>(+366.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.50 (n/a)</td><td>359.72 (n/a)</td><td>285.10 (n/a)</td><td>225.50 (n/a)</td><td>151.25 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(-28.33%)</b></td><td>0.02 (-12.11%)</td><td>0.02 (+11.38%)</td><td>0.01 (-10.69%)</td><td>0.01 <b>(-41.88%)</b></td><td>760.70 (+11.98%)</td><td>503.92 (+5.80%)</td><td>508.50 (-10.22%)</td><td>349.00 <b>(+39.54%)</b></td><td>167.01 (-11.22%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.30 (n/a)</td><td>476.28 (n/a)</td><td>566.40 (n/a)</td><td>250.10 (n/a)</td><td>188.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.10 (+6.89%)</td><td>0.08 (-12.19%)</td><td>0.08 (-7.52%)</td><td>0.05 <b>(-46.76%)</b></td><td>0.02 <b>(+1272.34%)</b></td><td>514.30 <b>(+87.84%)</b></td><td>327.04 <b>(+21.36%)</b></td><td>290.50 (+8.15%)</td><td>246.60 (-6.45%)</td><td>106.52 <b>(+2491.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>273.80 (n/a)</td><td>269.48 (n/a)</td><td>268.60 (n/a)</td><td>263.60 (n/a)</td><td>4.11 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.15 (-13.15%)</td><td>0.13 (+3.31%)</td><td>0.14 <b>(+41.53%)</b></td><td>0.08 (-1.11%)</td><td>0.03 <b>(-27.45%)</b></td><td>506.50 (+1.12%)</td><td>345.02 (-6.20%)</td><td>286.20 <b>(-29.35%)</b></td><td>278.50 (+15.13%)</td><td>99.01 (-13.71%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>500.90 (n/a)</td><td>367.84 (n/a)</td><td>405.10 (n/a)</td><td>241.90 (n/a)</td><td>114.74 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (+12.04%)</td><td>0.02 (+8.51%)</td><td>0.02 (+10.92%)</td><td>0.01 (-2.71%)</td><td>0.01 <b>(+44.78%)</b></td><td>533.20 (+2.80%)</td><td>367.62 (-3.06%)</td><td>301.00 (-9.85%)</td><td>248.50 (-10.74%)</td><td>138.97 <b>(+32.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.70 (n/a)</td><td>379.24 (n/a)</td><td>333.90 (n/a)</td><td>278.40 (n/a)</td><td>104.98 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (-4.55%)</td><td>0.02 <b>(-24.31%)</b></td><td>0.02 <b>(-40.29%)</b></td><td>0.02 <b>(+26.20%)</b></td><td>0.01 <b>(-20.28%)</b></td><td>437.40 <b>(-20.76%)</b></td><td>387.42 <b>(+25.39%)</b></td><td>423.20 <b>(+67.47%)</b></td><td>238.90 (+4.78%)</td><td>83.65 <b>(-38.82%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.00 (n/a)</td><td>308.98 (n/a)</td><td>252.70 (n/a)</td><td>228.00 (n/a)</td><td>136.71 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (-14.00%)</td><td>0.03 (-18.75%)</td><td>0.03 (-11.71%)</td><td>0.02 <b>(-22.90%)</b></td><td>0.01 (-8.45%)</td><td>640.40 <b>(+29.71%)</b></td><td>447.12 <b>(+27.95%)</b></td><td>441.00 (+13.25%)</td><td>238.40 (+16.29%)</td><td>188.38 <b>(+48.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>493.70 (n/a)</td><td>349.44 (n/a)</td><td>389.40 (n/a)</td><td>205.00 (n/a)</td><td>126.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (-3.59%)</td><td>0.02 (-19.34%)</td><td>0.02 <b>(-26.83%)</b></td><td>0.01 (-17.97%)</td><td>0.01 (-8.02%)</td><td>643.70 <b>(+21.91%)</b></td><td>424.94 <b>(+24.22%)</b></td><td>401.40 <b>(+36.67%)</b></td><td>228.00 (+3.73%)</td><td>154.61 (+15.28%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.00 (n/a)</td><td>342.08 (n/a)</td><td>293.70 (n/a)</td><td>219.80 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (-7.42%)</td><td>0.02 <b>(-21.31%)</b></td><td>0.03 <b>(-32.72%)</b></td><td>0.01 <b>(-50.47%)</b></td><td>0.01 (-12.65%)</td><td>2035.20 <b>(+101.90%)</b></td><td>720.06 <b>(+54.92%)</b></td><td>401.50 <b>(+48.65%)</b></td><td>253.90 (+8.00%)</td><td>746.05 <b>(+122.27%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1008.00 (n/a)</td><td>464.78 (n/a)</td><td>270.10 (n/a)</td><td>235.10 (n/a)</td><td>335.65 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (-11.92%)</td><td>0.03 (+5.50%)</td><td>0.03 (-1.95%)</td><td>0.02 <b>(+450.79%)</b></td><td>0.01 <b>(-54.46%)</b></td><td>448.70 <b>(-81.84%)</b></td><td>327.60 <b>(-54.89%)</b></td><td>275.60 (+1.96%)</td><td>246.80 (+13.52%)</td><td>87.85 <b>(-91.03%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2471.30 (n/a)</td><td>726.16 (n/a)</td><td>270.30 (n/a)</td><td>217.40 (n/a)</td><td>979.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (+8.85%)</td><td>0.03 (+11.32%)</td><td>0.03 <b>(+43.60%)</b></td><td>0.02 (+3.91%)</td><td>0.01 (+16.85%)</td><td>510.20 (-3.77%)</td><td>359.14 (-7.74%)</td><td>306.50 <b>(-30.36%)</b></td><td>227.00 (-8.13%)</td><td>138.70 (+12.49%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.20 (n/a)</td><td>389.28 (n/a)</td><td>440.10 (n/a)</td><td>247.10 (n/a)</td><td>123.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (+0.73%)</td><td>0.02 (+10.66%)</td><td>0.03 <b>(+67.99%)</b></td><td>0.00 (-9.58%)</td><td>0.01 <b>(+42.74%)</b></td><td>1991.30 (+10.60%)</td><td>945.52 <b>(+37.29%)</b></td><td>292.50 <b>(-40.48%)</b></td><td>247.20 (-0.72%)</td><td>933.79 <b>(+47.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1800.50 (n/a)</td><td>688.68 (n/a)</td><td>491.40 (n/a)</td><td>249.00 (n/a)</td><td>632.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 <b>(-38.59%)</b></td><td>0.02 (-19.25%)</td><td>0.02 (-14.52%)</td><td>0.01 (-16.45%)</td><td>0.00 <b>(-55.95%)</b></td><td>669.50 (+19.70%)</td><td>492.54 (+17.67%)</td><td>489.00 (+16.99%)</td><td>380.10 <b>(+62.85%)</b></td><td>111.09 (-8.60%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.30 (n/a)</td><td>418.58 (n/a)</td><td>418.00 (n/a)</td><td>233.40 (n/a)</td><td>121.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 <b>(+31.80%)</b></td><td>0.02 <b>(+32.17%)</b></td><td>0.02 (+2.99%)</td><td>0.01 <b>(+60.97%)</b></td><td>0.01 <b>(+39.21%)</b></td><td>551.30 <b>(-37.87%)</b></td><td>403.70 <b>(-25.05%)</b></td><td>465.70 (-2.90%)</td><td>239.90 <b>(-24.11%)</b></td><td>137.59 <b>(-37.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>887.40 (n/a)</td><td>538.62 (n/a)</td><td>479.60 (n/a)</td><td>316.10 (n/a)</td><td>218.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 <b>(+36.37%)</b></td><td>0.03 (+5.84%)</td><td>0.02 (-9.29%)</td><td>0.02 (-10.98%)</td><td>0.02 <b>(+83.81%)</b></td><td>593.60 (+12.34%)</td><td>429.24 (+5.33%)</td><td>467.70 (+10.23%)</td><td>174.20 <b>(-26.68%)</b></td><td>154.34 <b>(+45.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.40 (n/a)</td><td>407.52 (n/a)</td><td>424.30 (n/a)</td><td>237.60 (n/a)</td><td>106.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (-19.96%)</td><td>0.02 (+4.62%)</td><td>0.03 (-6.94%)</td><td>0.02 <b>(+244.83%)</b></td><td>0.01 <b>(-55.71%)</b></td><td>479.30 <b>(-71.00%)</b></td><td>371.14 <b>(-39.38%)</b></td><td>310.60 (+7.44%)</td><td>287.00 <b>(+24.95%)</b></td><td>96.16 <b>(-83.97%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1652.90 (n/a)</td><td>612.22 (n/a)</td><td>289.10 (n/a)</td><td>229.70 (n/a)</td><td>599.70 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.39 (+11.13%)</td><td>0.22 (-12.27%)</td><td>0.20 (+3.89%)</td><td>0.05 <b>(-73.76%)</b></td><td>0.13 <b>(+46.59%)</b></td><td>2080.30 <b>(+281.15%)</b></td><td>751.64 <b>(+72.11%)</b></td><td>503.00 (-3.75%)</td><td>251.90 (-10.00%)</td><td>752.82 <b>(+454.23%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>545.80 (n/a)</td><td>436.72 (n/a)</td><td>522.60 (n/a)</td><td>279.90 (n/a)</td><td>135.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.33 (+0.48%)</td><td>0.23 <b>(+43.67%)</b></td><td>0.22 <b>(+27.46%)</b></td><td>0.13 <b>(+222.41%)</b></td><td>0.09 <b>(-25.09%)</b></td><td>751.20 <b>(-68.98%)</b></td><td>477.42 <b>(-56.89%)</b></td><td>446.90 <b>(-21.54%)</b></td><td>295.80 (-0.47%)</td><td>193.67 <b>(-79.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.33 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>2421.90 (n/a)</td><td>1107.32 (n/a)</td><td>569.60 (n/a)</td><td>297.20 (n/a)</td><td>945.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.41 (+10.46%)</td><td>0.28 (+13.75%)</td><td>0.22 (-9.73%)</td><td>0.19 (+19.28%)</td><td>0.10 <b>(+23.04%)</b></td><td>513.20 (-16.17%)</td><td>385.70 (-10.96%)</td><td>452.10 (+10.78%)</td><td>237.70 (-9.48%)</td><td>125.15 (-8.67%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.37 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>612.20 (n/a)</td><td>433.20 (n/a)</td><td>408.10 (n/a)</td><td>262.60 (n/a)</td><td>137.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.28 (-12.99%)</td><td>0.17 <b>(-25.29%)</b></td><td>0.17 <b>(-29.71%)</b></td><td>0.04 <b>(-75.66%)</b></td><td>0.10 <b>(+45.85%)</b></td><td>1930.80 <b>(+310.90%)</b></td><td>722.30 <b>(+105.36%)</b></td><td>442.90 <b>(+42.27%)</b></td><td>263.30 (+14.93%)</td><td>695.14 <b>(+564.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>469.90 (n/a)</td><td>351.72 (n/a)</td><td>311.30 (n/a)</td><td>229.10 (n/a)</td><td>104.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.30 (+6.91%)</td><td>0.20 (+1.09%)</td><td>0.15 (-5.30%)</td><td>0.14 (+6.88%)</td><td>0.07 (-4.86%)</td><td>532.20 (-6.43%)</td><td>407.80 (-3.04%)</td><td>485.60 (+5.61%)</td><td>242.30 (-6.45%)</td><td>130.94 (-13.38%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>568.80 (n/a)</td><td>420.60 (n/a)</td><td>459.80 (n/a)</td><td>259.00 (n/a)</td><td>151.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.25 <b>(-30.38%)</b></td><td>0.16 (-16.49%)</td><td>0.17 (+8.13%)</td><td>0.09 <b>(-28.04%)</b></td><td>0.06 <b>(-34.15%)</b></td><td>821.20 <b>(+38.95%)</b></td><td>530.04 (+19.01%)</td><td>442.70 (-7.52%)</td><td>292.00 <b>(+43.63%)</b></td><td>214.63 <b>(+47.63%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>591.00 (n/a)</td><td>445.38 (n/a)</td><td>478.70 (n/a)</td><td>203.30 (n/a)</td><td>145.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.47 (+18.06%)</td><td>0.31 <b>(+22.50%)</b></td><td>0.27 (+15.27%)</td><td>0.25 <b>(+48.87%)</b></td><td>0.09 (+4.88%)</td><td>520.60 <b>(-32.83%)</b></td><td>447.06 <b>(-20.55%)</b></td><td>494.10 (-13.24%)</td><td>277.70 (-15.31%)</td><td>98.69 <b>(-39.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.40 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>775.00 (n/a)</td><td>562.68 (n/a)</td><td>569.50 (n/a)</td><td>327.90 (n/a)</td><td>163.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.40 <b>(+28.05%)</b></td><td>0.30 <b>(+42.03%)</b></td><td>0.27 <b>(+41.07%)</b></td><td>0.23 <b>(+127.50%)</b></td><td>0.07 (-13.95%)</td><td>571.50 <b>(-56.05%)</b></td><td>457.82 <b>(-37.02%)</b></td><td>479.30 <b>(-29.12%)</b></td><td>328.20 <b>(-21.91%)</b></td><td>103.05 <b>(-70.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>1300.20 (n/a)</td><td>726.98 (n/a)</td><td>676.20 (n/a)</td><td>420.30 (n/a)</td><td>349.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.46 <b>(+21.25%)</b></td><td>0.34 <b>(+28.37%)</b></td><td>0.33 <b>(+21.11%)</b></td><td>0.22 <b>(+173.85%)</b></td><td>0.11 (-10.76%)</td><td>590.80 <b>(-63.48%)</b></td><td>412.00 <b>(-38.19%)</b></td><td>394.60 (-17.43%)</td><td>284.40 (-17.54%)</td><td>130.67 <b>(-75.66%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>0.12 (n/a)</td><td>1617.80 (n/a)</td><td>666.54 (n/a)</td><td>477.90 (n/a)</td><td>344.90 (n/a)</td><td>536.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 (-16.39%)</td><td>0.01 <b>(-27.89%)</b></td><td>0.01 <b>(-47.24%)</b></td><td>0.01 (-7.00%)</td><td>0.00 (-18.73%)</td><td>595.80 (+7.53%)</td><td>497.74 <b>(+36.51%)</b></td><td>564.60 <b>(+89.53%)</b></td><td>281.20 (+19.61%)</td><td>130.89 (+0.50%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>364.62 (n/a)</td><td>297.90 (n/a)</td><td>235.10 (n/a)</td><td>130.23 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 <b>(-39.39%)</b></td><td>0.01 (-18.48%)</td><td>0.01 <b>(-28.42%)</b></td><td>0.01 <b>(+229.45%)</b></td><td>0.00 <b>(-70.96%)</b></td><td>574.70 <b>(-69.65%)</b></td><td>451.22 <b>(-29.42%)</b></td><td>404.70 <b>(+39.70%)</b></td><td>365.80 <b>(+65.00%)</b></td><td>96.49 <b>(-86.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1893.30 (n/a)</td><td>639.28 (n/a)</td><td>289.70 (n/a)</td><td>221.70 (n/a)</td><td>710.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 <b>(-40.46%)</b></td><td>0.01 <b>(-29.12%)</b></td><td>0.01 <b>(-37.67%)</b></td><td>0.01 (+11.54%)</td><td>0.00 <b>(-79.17%)</b></td><td>487.40 (-10.34%)</td><td>434.40 <b>(+22.13%)</b></td><td>447.00 <b>(+60.45%)</b></td><td>361.90 <b>(+68.01%)</b></td><td>48.17 <b>(-69.85%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.60 (n/a)</td><td>355.68 (n/a)</td><td>278.60 (n/a)</td><td>215.40 (n/a)</td><td>159.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (+1.92%)</td><td>0.40 (-13.71%)</td><td>0.47 (-6.28%)</td><td>0.21 (-6.99%)</td><td>0.16 (+16.44%)</td><td>629.80 (+7.51%)</td><td>388.76 <b>(+20.87%)</b></td><td>281.60 (+6.71%)</td><td>235.30 (-1.88%)</td><td>179.17 <b>(+20.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>585.80 (n/a)</td><td>321.64 (n/a)</td><td>263.90 (n/a)</td><td>239.80 (n/a)</td><td>148.57 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.71 (+18.01%)</td><td>0.40 <b>(-24.33%)</b></td><td>0.33 <b>(-37.00%)</b></td><td>0.23 <b>(-50.65%)</b></td><td>0.20 <b>(+279.08%)</b></td><td>585.20 <b>(+102.63%)</b></td><td>393.68 <b>(+55.52%)</b></td><td>405.00 <b>(+58.76%)</b></td><td>185.80 (-15.28%)</td><td>162.84 <b>(+551.25%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.60 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.05 (n/a)</td><td>288.80 (n/a)</td><td>253.14 (n/a)</td><td>255.10 (n/a)</td><td>219.30 (n/a)</td><td>25.00 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.58 <b>(+35.44%)</b></td><td>0.37 (+18.02%)</td><td>0.39 <b>(+32.75%)</b></td><td>0.21 (-17.85%)</td><td>0.15 <b>(+130.40%)</b></td><td>615.70 <b>(+21.73%)</b></td><td>416.56 (-4.56%)</td><td>335.90 <b>(-24.67%)</b></td><td>228.90 <b>(-26.16%)</b></td><td>178.61 <b>(+130.54%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.07 (n/a)</td><td>505.80 (n/a)</td><td>436.48 (n/a)</td><td>445.90 (n/a)</td><td>310.00 (n/a)</td><td>77.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.60 <b>(+26.04%)</b></td><td>0.48 <b>(+42.27%)</b></td><td>0.49 <b>(+97.43%)</b></td><td>0.29 (+18.72%)</td><td>0.13 (+8.40%)</td><td>457.50 (-15.78%)</td><td>299.16 <b>(-31.36%)</b></td><td>267.00 <b>(-49.35%)</b></td><td>221.50 <b>(-20.67%)</b></td><td>98.55 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>543.20 (n/a)</td><td>435.82 (n/a)</td><td>527.10 (n/a)</td><td>279.20 (n/a)</td><td>139.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.59 (-4.99%)</td><td>0.44 (-1.65%)</td><td>0.46 (+8.92%)</td><td>0.31 (-9.63%)</td><td>0.11 (+2.94%)</td><td>425.60 (+10.66%)</td><td>313.34 (+2.79%)</td><td>288.30 (-8.18%)</td><td>225.20 (+5.23%)</td><td>82.10 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.62 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>384.60 (n/a)</td><td>304.84 (n/a)</td><td>314.00 (n/a)</td><td>214.00 (n/a)</td><td>67.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (-19.60%)</td><td>0.01 (-10.50%)</td><td>0.01 <b>(-38.62%)</b></td><td>0.01 <b>(+38.00%)</b></td><td>0.00 <b>(-33.31%)</b></td><td>528.20 <b>(-27.53%)</b></td><td>408.66 (-0.76%)</td><td>482.80 <b>(+62.94%)</b></td><td>250.80 <b>(+24.40%)</b></td><td>126.44 <b>(-41.75%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>728.90 (n/a)</td><td>411.80 (n/a)</td><td>296.30 (n/a)</td><td>201.60 (n/a)</td><td>217.07 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (+2.84%)</td><td>0.01 (-8.63%)</td><td>0.01 <b>(-34.47%)</b></td><td>0.01 (-1.12%)</td><td>0.00 (+12.37%)</td><td>531.20 (+1.12%)</td><td>402.32 (+11.24%)</td><td>446.80 <b>(+52.60%)</b></td><td>251.20 (-2.79%)</td><td>126.63 (+9.05%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.30 (n/a)</td><td>361.68 (n/a)</td><td>292.80 (n/a)</td><td>258.40 (n/a)</td><td>116.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.00 <b>(+133.33%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+274.17%)</b></td><td>15499.75 <b>(-25.43%)</b></td><td>9961.22 <b>(-42.58%)</b></td><td>9426.18 <b>(-46.32%)</b></td><td>5681.10 <b>(-61.41%)</b></td><td>4328.80 <b>(+70.43%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20786.53 (n/a)</td><td>17346.57 (n/a)</td><td>17558.44 (n/a)</td><td>14720.43 (n/a)</td><td>2539.98 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.00 (-15.38%)</td><td>0.00 <b>(-23.08%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-40.63%)</b></td><td>19081.07 (+3.29%)</td><td>15180.38 (+15.36%)</td><td>16587.92 (+0.46%)</td><td>7720.00 <b>(+26.32%)</b></td><td>4352.24 <b>(-31.24%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18473.88 (n/a)</td><td>13158.86 (n/a)</td><td>16512.32 (n/a)</td><td>6111.54 (n/a)</td><td>6329.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.14 (-6.99%)</td><td>0.11 (+10.03%)</td><td>0.12 <b>(+35.68%)</b></td><td>0.08 (+19.03%)</td><td>0.03 (-9.09%)</td><td>26822.77 (-16.01%)</td><td>19822.91 (-10.66%)</td><td>16963.81 <b>(-26.28%)</b></td><td>14579.20 (+7.50%)</td><td>5993.22 (-15.26%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>31935.69 (n/a)</td><td>22189.18 (n/a)</td><td>23011.36 (n/a)</td><td>13562.18 (n/a)</td><td>7072.47 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>1.55 <b>(-20.65%)</b></td><td>1.08 (-4.46%)</td><td>1.22 <b>(+24.57%)</b></td><td>0.16 <b>(-35.63%)</b></td><td>0.57 (-17.91%)</td><td>3269.50 <b>(+55.36%)</b></td><td>989.28 <b>(+26.48%)</b></td><td>431.00 (-19.72%)</td><td>339.10 <b>(+26.06%)</b></td><td>1277.89 <b>(+68.38%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.95 (n/a)</td><td>1.13 (n/a)</td><td>0.98 (n/a)</td><td>0.25 (n/a)</td><td>0.69 (n/a)</td><td>2104.40 (n/a)</td><td>782.18 (n/a)</td><td>536.90 (n/a)</td><td>269.00 (n/a)</td><td>758.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.27 <b>(-24.80%)</b></td><td>1.48 <b>(-22.83%)</b></td><td>1.59 <b>(-38.01%)</b></td><td>0.30 (-7.66%)</td><td>0.73 <b>(-35.93%)</b></td><td>3452.80 (+8.30%)</td><td>1178.66 (+11.28%)</td><td>661.50 <b>(+61.30%)</b></td><td>462.20 <b>(+32.97%)</b></td><td>1275.45 (+5.04%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>3.02 (n/a)</td><td>1.92 (n/a)</td><td>2.56 (n/a)</td><td>0.33 (n/a)</td><td>1.14 (n/a)</td><td>3188.30 (n/a)</td><td>1059.16 (n/a)</td><td>410.10 (n/a)</td><td>347.60 (n/a)</td><td>1214.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.58 (-2.67%)</td><td>1.21 (+5.65%)</td><td>1.29 <b>(+41.89%)</b></td><td>0.66 <b>(-20.05%)</b></td><td>0.38 (-2.53%)</td><td>792.90 <b>(+25.08%)</b></td><td>479.12 (-3.80%)</td><td>406.80 <b>(-29.52%)</b></td><td>331.10 (+2.76%)</td><td>189.18 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>633.90 (n/a)</td><td>498.02 (n/a)</td><td>577.20 (n/a)</td><td>322.20 (n/a)</td><td>149.40 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.31 <b>(+40.69%)</b></td><td>1.27 <b>(+45.90%)</b></td><td>0.98 <b>(+57.82%)</b></td><td>0.48 (+3.12%)</td><td>0.74 <b>(+53.25%)</b></td><td>1102.40 (-3.03%)</td><td>554.24 <b>(-24.66%)</b></td><td>535.80 <b>(-36.64%)</b></td><td>227.00 <b>(-28.91%)</b></td><td>344.42 (+6.26%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 16:07:16</td><td>1.64 (n/a)</td><td>0.87 (n/a)</td><td>0.62 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>1136.80 (n/a)</td><td>735.64 (n/a)</td><td>845.70 (n/a)</td><td>319.30 (n/a)</td><td>324.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.75 (-15.44%)</td><td>1.32 (-0.50%)</td><td>1.36 <b>(+22.47%)</b></td><td>0.77 (-19.20%)</td><td>0.36 <b>(-21.75%)</b></td><td>678.10 <b>(+23.76%)</b></td><td>430.02 (-0.09%)</td><td>385.10 (-18.34%)</td><td>300.10 (+18.29%)</td><td>146.96 (+19.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (n/a)</td><td>1.32 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>0.46 (n/a)</td><td>547.90 (n/a)</td><td>430.40 (n/a)</td><td>471.60 (n/a)</td><td>253.70 (n/a)</td><td>123.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>
