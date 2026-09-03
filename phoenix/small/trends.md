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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (+8.42%)</td><td>0.04 (+7.89%)</td><td>0.05 (+15.72%)</td><td>0.02 <b>(-30.51%)</b></td><td>0.01 <b>(+128.78%)</b></td><td>497.60 <b>(+43.90%)</b></td><td>298.18 (-0.73%)</td><td>260.20 (-13.58%)</td><td>229.90 (-7.78%)</td><td>112.23 <b>(+224.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>345.80 (n/a)</td><td>300.38 (n/a)</td><td>301.10 (n/a)</td><td>249.30 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (-7.29%)</td><td>0.03 (+2.17%)</td><td>0.03 (+15.70%)</td><td>0.02 <b>(+26.80%)</b></td><td>0.01 <b>(-35.61%)</b></td><td>521.80 <b>(-21.13%)</b></td><td>431.64 (-10.38%)</td><td>487.30 (-13.57%)</td><td>283.90 (+7.86%)</td><td>99.82 <b>(-45.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>661.60 (n/a)</td><td>481.64 (n/a)</td><td>563.80 (n/a)</td><td>263.20 (n/a)</td><td>181.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 <b>(+39.91%)</b></td><td>0.04 <b>(+65.01%)</b></td><td>0.05 <b>(+86.31%)</b></td><td>0.03 <b>(+51.80%)</b></td><td>0.01 <b>(+32.63%)</b></td><td>372.80 <b>(-34.13%)</b></td><td>284.72 <b>(-39.58%)</b></td><td>259.80 <b>(-46.33%)</b></td><td>250.60 <b>(-28.52%)</b></td><td>50.91 <b>(-34.54%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>566.00 (n/a)</td><td>471.26 (n/a)</td><td>484.10 (n/a)</td><td>350.60 (n/a)</td><td>77.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (+15.47%)</td><td>0.01 (+19.42%)</td><td>0.02 <b>(+56.24%)</b></td><td>0.01 (-9.35%)</td><td>0.00 <b>(+93.81%)</b></td><td>569.20 (+10.31%)</td><td>402.22 (-10.97%)</td><td>313.60 <b>(-36.00%)</b></td><td>291.70 (-13.42%)</td><td>136.60 <b>(+87.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.00 (n/a)</td><td>451.76 (n/a)</td><td>490.00 (n/a)</td><td>336.90 (n/a)</td><td>72.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (-12.34%)</td><td>0.01 (-9.73%)</td><td>0.01 (-16.23%)</td><td>0.01 (+16.76%)</td><td>0.00 <b>(-33.31%)</b></td><td>532.30 (-14.37%)</td><td>398.36 (+2.57%)</td><td>388.20 (+19.37%)</td><td>264.80 (+14.04%)</td><td>111.20 <b>(-33.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.60 (n/a)</td><td>388.36 (n/a)</td><td>325.20 (n/a)</td><td>232.20 (n/a)</td><td>168.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (+13.04%)</td><td>0.01 (-9.37%)</td><td>0.01 <b>(-26.09%)</b></td><td>0.01 (-4.05%)</td><td>0.01 <b>(+24.28%)</b></td><td>583.40 (+4.22%)</td><td>434.76 (+13.32%)</td><td>470.30 <b>(+35.30%)</b></td><td>229.60 (-11.52%)</td><td>137.07 (+10.13%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.80 (n/a)</td><td>383.64 (n/a)</td><td>347.60 (n/a)</td><td>259.50 (n/a)</td><td>124.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 <b>(-29.23%)</b></td><td>0.01 <b>(-36.43%)</b></td><td>0.01 <b>(-45.39%)</b></td><td>0.01 <b>(-34.61%)</b></td><td>0.00 <b>(-32.07%)</b></td><td>738.00 <b>(+52.92%)</b></td><td>568.08 <b>(+57.26%)</b></td><td>599.00 <b>(+83.12%)</b></td><td>407.70 <b>(+41.32%)</b></td><td>125.96 <b>(+47.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.60 (n/a)</td><td>361.24 (n/a)</td><td>327.10 (n/a)</td><td>288.50 (n/a)</td><td>85.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 <b>(-39.20%)</b></td><td>0.01 <b>(-38.73%)</b></td><td>0.01 <b>(-23.02%)</b></td><td>0.00 <b>(-69.59%)</b></td><td>0.00 <b>(-24.44%)</b></td><td>1889.50 <b>(+228.78%)</b></td><td>836.68 <b>(+92.00%)</b></td><td>597.60 <b>(+29.91%)</b></td><td>479.40 <b>(+64.46%)</b></td><td>591.12 <b>(+364.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.70 (n/a)</td><td>435.76 (n/a)</td><td>460.00 (n/a)</td><td>291.50 (n/a)</td><td>127.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (+15.32%)</td><td>0.01 (-4.65%)</td><td>0.01 (+0.76%)</td><td>0.00 <b>(-47.95%)</b></td><td>0.00 <b>(+105.21%)</b></td><td>1073.60 <b>(+92.13%)</b></td><td>585.62 <b>(+20.57%)</b></td><td>496.90 (-0.76%)</td><td>308.50 (-13.29%)</td><td>291.77 <b>(+265.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.80 (n/a)</td><td>485.70 (n/a)</td><td>500.70 (n/a)</td><td>355.80 (n/a)</td><td>79.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.60 (n/a)</td><td>316.86 (n/a)</td><td>267.20 (n/a)</td><td>209.00 (n/a)</td><td>153.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>485.10 (n/a)</td><td>326.60 (n/a)</td><td>241.70 (n/a)</td><td>233.60 (n/a)</td><td>121.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>424.76 (n/a)</td><td>435.00 (n/a)</td><td>305.70 (n/a)</td><td>100.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.90 (n/a)</td><td>387.38 (n/a)</td><td>356.20 (n/a)</td><td>255.80 (n/a)</td><td>139.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.00 (n/a)</td><td>373.00 (n/a)</td><td>407.10 (n/a)</td><td>231.20 (n/a)</td><td>114.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>698.10 (n/a)</td><td>487.56 (n/a)</td><td>453.10 (n/a)</td><td>359.30 (n/a)</td><td>138.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.80 (n/a)</td><td>373.52 (n/a)</td><td>428.90 (n/a)</td><td>241.30 (n/a)</td><td>117.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>412.56 (n/a)</td><td>431.60 (n/a)</td><td>234.40 (n/a)</td><td>118.25 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>408.94 (n/a)</td><td>417.10 (n/a)</td><td>234.60 (n/a)</td><td>122.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>738.90 (n/a)</td><td>527.50 (n/a)</td><td>569.60 (n/a)</td><td>260.00 (n/a)</td><td>174.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>437.82 (n/a)</td><td>527.90 (n/a)</td><td>244.30 (n/a)</td><td>169.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.00 (n/a)</td><td>482.48 (n/a)</td><td>478.40 (n/a)</td><td>290.90 (n/a)</td><td>123.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.60 (+8.62%)</td><td>0.36 (-11.29%)</td><td>0.34 (-2.04%)</td><td>0.24 <b>(-30.47%)</b></td><td>0.15 <b>(+50.61%)</b></td><td>932.00 <b>(+43.80%)</b></td><td>675.30 <b>(+20.38%)</b></td><td>647.00 (+2.08%)</td><td>366.00 (-7.95%)</td><td>220.14 <b>(+90.37%)</b></td><td>25.78 (+8.62%)</td><td>15.52 (-11.29%)</td><td>14.59 (-2.04%)</td><td>10.13 <b>(-30.47%)</b></td><td>6.19 <b>(+50.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>648.10 (n/a)</td><td>560.96 (n/a)</td><td>633.80 (n/a)</td><td>397.60 (n/a)</td><td>115.63 (n/a)</td><td>23.74 (n/a)</td><td>17.50 (n/a)</td><td>14.89 (n/a)</td><td>14.56 (n/a)</td><td>4.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.53 (+9.89%)</td><td>0.43 (+7.19%)</td><td>0.43 (+8.20%)</td><td>0.33 (+12.25%)</td><td>0.07 (+5.37%)</td><td>672.50 (-10.92%)</td><td>529.58 (-6.99%)</td><td>519.50 (-7.58%)</td><td>420.40 (-9.00%)</td><td>96.07 (-15.44%)</td><td>22.45 (+9.89%)</td><td>18.28 (+7.19%)</td><td>18.17 (+8.20%)</td><td>14.03 (+12.25%)</td><td>3.19 (+5.37%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>754.90 (n/a)</td><td>569.38 (n/a)</td><td>562.10 (n/a)</td><td>462.00 (n/a)</td><td>113.60 (n/a)</td><td>20.43 (n/a)</td><td>17.05 (n/a)</td><td>16.79 (n/a)</td><td>12.50 (n/a)</td><td>3.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.31 (+1.18%)</td><td>0.30 (+0.89%)</td><td>0.30 (-0.18%)</td><td>0.29 (+1.76%)</td><td>0.01 (-3.17%)</td><td>85515.10 (-1.73%)</td><td>83065.28 (-0.89%)</td><td>83007.50 (+0.18%)</td><td>80599.30 (-1.17%)</td><td>2144.28 (-5.97%)</td><td>213.15 (+1.18%)</td><td>206.93 (+0.89%)</td><td>206.97 (-0.18%)</td><td>200.90 (+1.76%)</td><td>5.34 (-3.17%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87021.00 (n/a)</td><td>83810.68 (n/a)</td><td>82856.30 (n/a)</td><td>81552.30 (n/a)</td><td>2280.41 (n/a)</td><td>210.66 (n/a)</td><td>205.10 (n/a)</td><td>207.35 (n/a)</td><td>197.42 (n/a)</td><td>5.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.06 (+3.59%)</td><td>1.00 (-0.47%)</td><td>1.02 (+0.93%)</td><td>0.91 (-9.11%)</td><td>0.06 <b>(+553.66%)</b></td><td>27642.40 (+10.02%)</td><td>25113.04 (+0.73%)</td><td>24761.30 (-0.92%)</td><td>23828.30 (-3.47%)</td><td>1480.09 <b>(+602.37%)</b></td><td>720.99 (+3.59%)</td><td>685.90 (-0.47%)</td><td>693.82 (+0.93%)</td><td>621.50 (-9.11%)</td><td>38.15 <b>(+553.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25124.90 (n/a)</td><td>24931.00 (n/a)</td><td>24992.40 (n/a)</td><td>24684.20 (n/a)</td><td>210.73 (n/a)</td><td>695.99 (n/a)</td><td>689.14 (n/a)</td><td>687.40 (n/a)</td><td>683.78 (n/a)</td><td>5.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.53 (-8.11%)</td><td>2.79 (-4.76%)</td><td>3.20 (-10.19%)</td><td>1.70 (-1.42%)</td><td>0.80 <b>(-21.34%)</b></td><td>4741.70 (+1.44%)</td><td>3128.04 (+1.18%)</td><td>2520.30 (+11.35%)</td><td>2280.70 (+8.82%)</td><td>1059.56 (-14.08%)</td><td>926.87 (-8.11%)</td><td>731.90 (-4.76%)</td><td>838.78 (-10.19%)</td><td>445.81 (-1.42%)</td><td>209.63 <b>(-21.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>3.85 (n/a)</td><td>2.93 (n/a)</td><td>3.56 (n/a)</td><td>1.72 (n/a)</td><td>1.02 (n/a)</td><td>4674.40 (n/a)</td><td>3091.62 (n/a)</td><td>2263.50 (n/a)</td><td>2095.80 (n/a)</td><td>1233.19 (n/a)</td><td>1008.67 (n/a)</td><td>768.45 (n/a)</td><td>933.90 (n/a)</td><td>452.24 (n/a)</td><td>266.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.28 (-19.69%)</td><td>0.19 (-9.52%)</td><td>0.18 (+0.53%)</td><td>0.14 (-15.46%)</td><td>0.05 <b>(-31.32%)</b></td><td>8950.10 (+18.28%)</td><td>6782.70 (+8.18%)</td><td>6821.50 (-0.53%)</td><td>4500.30 <b>(+24.51%)</b></td><td>1601.93 (+2.69%)</td><td>14.91 (-19.69%)</td><td>10.40 (-9.52%)</td><td>9.84 (+0.53%)</td><td>7.50 (-15.46%)</td><td>2.76 <b>(-31.32%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>7566.70 (n/a)</td><td>6269.56 (n/a)</td><td>6858.00 (n/a)</td><td>3614.30 (n/a)</td><td>1559.94 (n/a)</td><td>18.57 (n/a)</td><td>11.49 (n/a)</td><td>9.79 (n/a)</td><td>8.87 (n/a)</td><td>4.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.72 (n/a)</td><td>3.58 (n/a)</td><td>3.56 (n/a)</td><td>3.37 (n/a)</td><td>0.14 (n/a)</td><td>3.71 (n/a)</td><td>3.57 (n/a)</td><td>3.56 (n/a)</td><td>3.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>6.92 (-3.21%)</td><td>6.03 (-6.49%)</td><td>5.90 (-7.16%)</td><td>5.64 (-1.26%)</td><td>0.51 (-14.53%)</td><td>6.91 (-3.21%)</td><td>6.03 (-6.49%)</td><td>5.89 (-7.16%)</td><td>5.64 (-1.26%)</td><td>0.51 (-14.53%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>7.15 (n/a)</td><td>6.45 (n/a)</td><td>6.35 (n/a)</td><td>5.71 (n/a)</td><td>0.60 (n/a)</td><td>7.14 (n/a)</td><td>6.44 (n/a)</td><td>6.35 (n/a)</td><td>5.71 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>13.05 (-2.39%)</td><td>9.73 (-15.51%)</td><td>10.08 (-13.46%)</td><td>6.77 <b>(-32.73%)</b></td><td>2.34 <b>(+79.62%)</b></td><td>13.04 (-2.39%)</td><td>9.72 (-15.51%)</td><td>10.08 (-13.46%)</td><td>6.77 <b>(-32.73%)</b></td><td>2.34 <b>(+79.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>13.37 (n/a)</td><td>11.51 (n/a)</td><td>11.65 (n/a)</td><td>10.07 (n/a)</td><td>1.30 (n/a)</td><td>13.36 (n/a)</td><td>11.51 (n/a)</td><td>11.65 (n/a)</td><td>10.06 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.81 (n/a)</td><td>3.73 (n/a)</td><td>3.73 (n/a)</td><td>3.66 (n/a)</td><td>0.06 (n/a)</td><td>3.80 (n/a)</td><td>3.73 (n/a)</td><td>3.73 (n/a)</td><td>3.66 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>6.86 (-0.78%)</td><td>6.11 (+2.33%)</td><td>6.11 (+7.45%)</td><td>5.25 (+5.95%)</td><td>0.64 <b>(-28.11%)</b></td><td>6.86 (-0.78%)</td><td>6.11 (+2.33%)</td><td>6.10 (+7.45%)</td><td>5.25 (+5.95%)</td><td>0.64 <b>(-28.11%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>6.92 (n/a)</td><td>5.97 (n/a)</td><td>5.68 (n/a)</td><td>4.96 (n/a)</td><td>0.90 (n/a)</td><td>6.91 (n/a)</td><td>5.97 (n/a)</td><td>5.68 (n/a)</td><td>4.95 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>13.24 (-4.21%)</td><td>10.13 (-1.78%)</td><td>8.71 (+0.22%)</td><td>7.45 (+0.53%)</td><td>2.68 (-14.30%)</td><td>13.23 (-4.21%)</td><td>10.12 (-1.78%)</td><td>8.70 (+0.22%)</td><td>7.45 (+0.53%)</td><td>2.67 (-14.30%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>13.82 (n/a)</td><td>10.31 (n/a)</td><td>8.69 (n/a)</td><td>7.41 (n/a)</td><td>3.12 (n/a)</td><td>13.81 (n/a)</td><td>10.30 (n/a)</td><td>8.68 (n/a)</td><td>7.41 (n/a)</td><td>3.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.17 (+9.82%)</td><td>2.26 (+11.56%)</td><td>2.91 <b>(+66.97%)</b></td><td>1.09 (+3.97%)</td><td>1.05 <b>(+37.46%)</b></td><td>3.17 (+9.82%)</td><td>2.26 (+11.56%)</td><td>2.91 <b>(+66.97%)</b></td><td>1.09 (+3.97%)</td><td>1.05 <b>(+37.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.89 (n/a)</td><td>2.03 (n/a)</td><td>1.74 (n/a)</td><td>1.05 (n/a)</td><td>0.76 (n/a)</td><td>2.88 (n/a)</td><td>2.02 (n/a)</td><td>1.74 (n/a)</td><td>1.04 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.56 (-0.37%)</td><td>0.30 <b>(-21.82%)</b></td><td>0.25 <b>(-36.08%)</b></td><td>0.08 (-8.16%)</td><td>0.22 (+19.93%)</td><td>0.55 (-0.37%)</td><td>0.29 <b>(-21.82%)</b></td><td>0.24 <b>(-36.08%)</b></td><td>0.07 (-8.16%)</td><td>0.22 (+19.93%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (n/a)</td><td>0.38 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.73 (-0.88%)</td><td>0.65 (+14.27%)</td><td>0.72 (+18.98%)</td><td>0.41 (+10.81%)</td><td>0.13 (-2.90%)</td><td>0.72 (-0.88%)</td><td>0.64 (+14.27%)</td><td>0.71 (+18.98%)</td><td>0.41 (+10.81%)</td><td>0.13 (-2.90%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td><td>0.72 (n/a)</td><td>0.56 (n/a)</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>2.49 (-6.96%)</td><td>1.06 <b>(-35.79%)</b></td><td>0.83 <b>(-52.65%)</b></td><td>0.44 (-2.53%)</td><td>0.85 (+6.43%)</td><td>2.45 (-6.96%)</td><td>1.04 <b>(-35.79%)</b></td><td>0.82 <b>(-52.65%)</b></td><td>0.43 (-2.53%)</td><td>0.83 (+6.43%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.68 (n/a)</td><td>1.65 (n/a)</td><td>1.75 (n/a)</td><td>0.45 (n/a)</td><td>0.80 (n/a)</td><td>2.63 (n/a)</td><td>1.62 (n/a)</td><td>1.72 (n/a)</td><td>0.44 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.70 (n/a)</td><td>376.36 (n/a)</td><td>420.80 (n/a)</td><td>232.30 (n/a)</td><td>98.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>443.56 (n/a)</td><td>456.50 (n/a)</td><td>264.50 (n/a)</td><td>112.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.70 (n/a)</td><td>453.56 (n/a)</td><td>466.50 (n/a)</td><td>267.20 (n/a)</td><td>120.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1057.10 (n/a)</td><td>569.96 (n/a)</td><td>481.60 (n/a)</td><td>251.80 (n/a)</td><td>299.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.40 (n/a)</td><td>427.46 (n/a)</td><td>466.40 (n/a)</td><td>224.10 (n/a)</td><td>124.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>492.80 (n/a)</td><td>474.74 (n/a)</td><td>478.70 (n/a)</td><td>451.00 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-12.73%)</td><td>0.02 (-19.69%)</td><td>0.02 (-14.86%)</td><td>0.02 <b>(-25.35%)</b></td><td>0.01 <b>(+23.16%)</b></td><td>519.30 <b>(+33.94%)</b></td><td>377.24 <b>(+28.65%)</b></td><td>329.40 (+17.48%)</td><td>272.60 (+14.59%)</td><td>104.85 <b>(+85.86%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>387.70 (n/a)</td><td>293.24 (n/a)</td><td>280.40 (n/a)</td><td>237.90 (n/a)</td><td>56.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-10.39%)</td><td>0.03 (-6.31%)</td><td>0.03 (+2.62%)</td><td>0.01 (-14.63%)</td><td>0.01 (+12.72%)</td><td>553.00 (+17.14%)</td><td>359.50 (+10.92%)</td><td>268.60 (-2.54%)</td><td>255.10 (+11.59%)</td><td>139.01 <b>(+39.59%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.10 (n/a)</td><td>324.12 (n/a)</td><td>275.60 (n/a)</td><td>228.60 (n/a)</td><td>99.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-13.58%)</td><td>0.02 (-7.90%)</td><td>0.02 <b>(-22.35%)</b></td><td>0.02 (-2.41%)</td><td>0.01 (-9.87%)</td><td>466.20 (+2.46%)</td><td>356.32 (+8.09%)</td><td>391.80 <b>(+28.80%)</b></td><td>260.70 (+15.71%)</td><td>89.47 (+0.50%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.00 (n/a)</td><td>329.64 (n/a)</td><td>304.20 (n/a)</td><td>225.30 (n/a)</td><td>89.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-11.48%)</td><td>0.03 (-3.18%)</td><td>0.03 (+4.39%)</td><td>0.02 (+2.11%)</td><td>0.01 <b>(-23.31%)</b></td><td>455.40 (-2.06%)</td><td>340.06 (+1.20%)</td><td>305.80 (-4.20%)</td><td>260.10 (+12.99%)</td><td>79.84 (-14.58%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.00 (n/a)</td><td>336.02 (n/a)</td><td>319.20 (n/a)</td><td>230.20 (n/a)</td><td>93.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 <b>(-23.49%)</b></td><td>0.02 (-2.69%)</td><td>0.02 (+16.70%)</td><td>0.01 (+0.80%)</td><td>0.00 <b>(-45.93%)</b></td><td>585.50 (-0.80%)</td><td>463.24 (-3.92%)</td><td>459.40 (-14.31%)</td><td>316.20 <b>(+30.72%)</b></td><td>101.35 <b>(-29.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.20 (n/a)</td><td>482.14 (n/a)</td><td>536.10 (n/a)</td><td>241.90 (n/a)</td><td>144.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-5.85%)</td><td>0.02 (+10.46%)</td><td>0.02 <b>(+23.04%)</b></td><td>0.02 <b>(+339.96%)</b></td><td>0.00 <b>(-55.17%)</b></td><td>477.90 <b>(-77.27%)</b></td><td>412.24 <b>(-44.78%)</b></td><td>420.40 (-18.73%)</td><td>281.50 (+6.23%)</td><td>78.25 <b>(-89.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2102.60 (n/a)</td><td>746.60 (n/a)</td><td>517.30 (n/a)</td><td>265.00 (n/a)</td><td>768.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-15.32%)</td><td>0.02 <b>(-32.98%)</b></td><td>0.02 <b>(-40.90%)</b></td><td>0.01 <b>(-26.79%)</b></td><td>0.01 (-1.14%)</td><td>559.20 <b>(+36.59%)</b></td><td>459.90 <b>(+52.87%)</b></td><td>485.70 <b>(+69.17%)</b></td><td>264.70 (+18.06%)</td><td>116.39 <b>(+53.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>409.40 (n/a)</td><td>300.84 (n/a)</td><td>287.10 (n/a)</td><td>224.20 (n/a)</td><td>75.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (+19.91%)</td><td>0.02 (+10.61%)</td><td>0.02 (-18.00%)</td><td>0.02 (+12.58%)</td><td>0.01 <b>(+51.35%)</b></td><td>538.40 (-11.18%)</td><td>446.82 (-6.89%)</td><td>534.90 <b>(+21.96%)</b></td><td>292.40 (-16.60%)</td><td>123.94 (+12.47%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.20 (n/a)</td><td>479.88 (n/a)</td><td>438.60 (n/a)</td><td>350.60 (n/a)</td><td>110.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (+1.80%)</td><td>0.02 (-11.65%)</td><td>0.02 <b>(-20.13%)</b></td><td>0.02 (+16.94%)</td><td>0.01 (+3.78%)</td><td>524.90 (-14.47%)</td><td>442.18 (+12.11%)</td><td>469.50 <b>(+25.20%)</b></td><td>241.50 (-1.79%)</td><td>115.28 (-17.34%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>394.40 (n/a)</td><td>375.00 (n/a)</td><td>245.90 (n/a)</td><td>139.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (-5.70%)</td><td>0.02 <b>(-23.32%)</b></td><td>0.02 <b>(-37.53%)</b></td><td>0.01 <b>(-22.44%)</b></td><td>0.01 <b>(+21.23%)</b></td><td>656.90 <b>(+28.93%)</b></td><td>424.04 <b>(+43.90%)</b></td><td>435.50 <b>(+60.05%)</b></td><td>210.30 (+6.05%)</td><td>201.68 <b>(+59.49%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.50 (n/a)</td><td>294.68 (n/a)</td><td>272.10 (n/a)</td><td>198.30 (n/a)</td><td>126.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-14.56%)</td><td>0.02 <b>(-24.64%)</b></td><td>0.02 <b>(-46.07%)</b></td><td>0.01 <b>(-30.87%)</b></td><td>0.01 (-2.60%)</td><td>657.60 <b>(+44.65%)</b></td><td>442.60 <b>(+38.58%)</b></td><td>457.90 <b>(+85.38%)</b></td><td>246.70 (+17.03%)</td><td>178.07 <b>(+52.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.60 (n/a)</td><td>319.38 (n/a)</td><td>247.00 (n/a)</td><td>210.80 (n/a)</td><td>117.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 <b>(+35.73%)</b></td><td>0.02 (-2.20%)</td><td>0.02 (-6.89%)</td><td>0.01 <b>(-20.90%)</b></td><td>0.01 <b>(+91.00%)</b></td><td>634.00 <b>(+26.42%)</b></td><td>466.02 (+10.90%)</td><td>487.00 (+7.39%)</td><td>235.00 <b>(-26.31%)</b></td><td>154.80 <b>(+72.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>501.50 (n/a)</td><td>420.20 (n/a)</td><td>453.50 (n/a)</td><td>318.90 (n/a)</td><td>89.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-18.69%)</td><td>0.02 <b>(-29.96%)</b></td><td>0.01 <b>(-48.14%)</b></td><td>0.01 <b>(+75.19%)</b></td><td>0.01 <b>(-27.46%)</b></td><td>1084.10 <b>(-42.92%)</b></td><td>650.78 (+0.83%)</td><td>639.30 <b>(+92.85%)</b></td><td>269.10 <b>(+22.99%)</b></td><td>289.39 <b>(-58.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1899.10 (n/a)</td><td>645.40 (n/a)</td><td>331.50 (n/a)</td><td>218.80 (n/a)</td><td>705.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (-7.03%)</td><td>0.02 (-3.10%)</td><td>0.02 (+6.43%)</td><td>0.01 <b>(+32.67%)</b></td><td>0.00 <b>(-43.83%)</b></td><td>573.30 <b>(-24.64%)</b></td><td>490.44 (-2.68%)</td><td>477.80 (-6.04%)</td><td>375.30 (+7.54%)</td><td>79.68 <b>(-52.29%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>760.70 (n/a)</td><td>503.92 (n/a)</td><td>508.50 (n/a)</td><td>349.00 (n/a)</td><td>167.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.08 (-18.06%)</td><td>0.05 <b>(-42.13%)</b></td><td>0.05 <b>(-46.48%)</b></td><td>0.01 <b>(-72.31%)</b></td><td>0.02 <b>(+25.75%)</b></td><td>1857.40 <b>(+261.15%)</b></td><td>755.04 <b>(+130.87%)</b></td><td>542.70 <b>(+86.82%)</b></td><td>300.90 <b>(+22.02%)</b></td><td>624.86 <b>(+486.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>514.30 (n/a)</td><td>327.04 (n/a)</td><td>290.50 (n/a)</td><td>246.60 (n/a)</td><td>106.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.15 (+3.29%)</td><td>0.11 (-9.97%)</td><td>0.12 (-14.40%)</td><td>0.07 (-8.00%)</td><td>0.03 (+16.75%)</td><td>550.50 (+8.69%)</td><td>394.00 (+14.20%)</td><td>334.40 (+16.84%)</td><td>269.70 (-3.16%)</td><td>129.20 <b>(+30.49%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>506.50 (n/a)</td><td>345.02 (n/a)</td><td>286.20 (n/a)</td><td>278.50 (n/a)</td><td>99.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (-11.35%)</td><td>0.02 (+4.23%)</td><td>0.02 (+3.59%)</td><td>0.01 (+14.34%)</td><td>0.00 <b>(-43.29%)</b></td><td>466.30 (-12.55%)</td><td>328.06 (-10.76%)</td><td>290.60 (-3.46%)</td><td>280.30 (+12.80%)</td><td>78.60 <b>(-43.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.20 (n/a)</td><td>367.62 (n/a)</td><td>301.00 (n/a)</td><td>248.50 (n/a)</td><td>138.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (+15.91%)</td><td>0.03 <b>(+43.61%)</b></td><td>0.03 <b>(+66.24%)</b></td><td>0.02 <b>(+33.38%)</b></td><td>0.01 (-10.65%)</td><td>327.90 <b>(-25.03%)</b></td><td>263.16 <b>(-32.07%)</b></td><td>254.60 <b>(-39.84%)</b></td><td>206.10 (-13.73%)</td><td>49.79 <b>(-40.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>437.40 (n/a)</td><td>387.42 (n/a)</td><td>423.20 (n/a)</td><td>238.90 (n/a)</td><td>83.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 <b>(-23.63%)</b></td><td>0.03 (-4.98%)</td><td>0.03 (+5.82%)</td><td>0.02 <b>(+20.51%)</b></td><td>0.01 <b>(-56.74%)</b></td><td>531.40 (-17.02%)</td><td>414.46 (-7.30%)</td><td>416.80 (-5.49%)</td><td>312.20 <b>(+30.96%)</b></td><td>84.64 <b>(-55.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>640.40 (n/a)</td><td>447.12 (n/a)</td><td>441.00 (n/a)</td><td>238.40 (n/a)</td><td>188.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (+11.15%)</td><td>0.02 (+12.02%)</td><td>0.02 (-1.12%)</td><td>0.01 (+16.44%)</td><td>0.01 <b>(+20.10%)</b></td><td>552.80 (-14.12%)</td><td>387.02 (-8.92%)</td><td>405.90 (+1.12%)</td><td>205.10 (-10.04%)</td><td>147.44 (-4.64%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.70 (n/a)</td><td>424.94 (n/a)</td><td>401.40 (n/a)</td><td>228.00 (n/a)</td><td>154.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (-13.62%)</td><td>0.03 (+4.72%)</td><td>0.02 (-10.92%)</td><td>0.02 <b>(+291.11%)</b></td><td>0.01 <b>(-55.72%)</b></td><td>520.40 <b>(-74.43%)</b></td><td>422.94 <b>(-41.26%)</b></td><td>450.70 (+12.25%)</td><td>294.00 (+15.79%)</td><td>88.38 <b>(-88.15%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2035.20 (n/a)</td><td>720.06 (n/a)</td><td>401.50 (n/a)</td><td>253.90 (n/a)</td><td>746.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (+3.41%)</td><td>0.03 (+4.91%)</td><td>0.03 (+11.93%)</td><td>0.02 (+0.13%)</td><td>0.01 <b>(+27.50%)</b></td><td>448.10 (-0.13%)</td><td>321.40 (-1.89%)</td><td>246.30 (-10.63%)</td><td>238.70 (-3.28%)</td><td>106.89 <b>(+21.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.70 (n/a)</td><td>327.60 (n/a)</td><td>275.60 (n/a)</td><td>246.80 (n/a)</td><td>87.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (+0.05%)</td><td>0.03 (-19.40%)</td><td>0.02 <b>(-40.18%)</b></td><td>0.02 (-12.71%)</td><td>0.01 (-0.09%)</td><td>584.50 (+14.56%)</td><td>449.74 <b>(+25.23%)</b></td><td>512.30 <b>(+67.15%)</b></td><td>226.90 (-0.04%)</td><td>152.74 (+10.12%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.20 (n/a)</td><td>359.14 (n/a)</td><td>306.50 (n/a)</td><td>227.00 (n/a)</td><td>138.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 <b>(+42.24%)</b></td><td>0.03 <b>(+46.58%)</b></td><td>0.03 (-0.45%)</td><td>0.02 <b>(+331.03%)</b></td><td>0.01 <b>(-27.72%)</b></td><td>462.00 <b>(-76.80%)</b></td><td>302.32 <b>(-68.03%)</b></td><td>293.80 (+0.44%)</td><td>173.80 <b>(-29.69%)</b></td><td>104.66 <b>(-88.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1991.30 (n/a)</td><td>945.52 (n/a)</td><td>292.50 (n/a)</td><td>247.20 (n/a)</td><td>933.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 <b>(+32.40%)</b></td><td>0.02 (+14.98%)</td><td>0.02 (+6.77%)</td><td>0.02 <b>(+35.97%)</b></td><td>0.01 <b>(+39.00%)</b></td><td>492.40 <b>(-26.45%)</b></td><td>428.88 (-12.92%)</td><td>457.90 (-6.36%)</td><td>287.10 <b>(-24.47%)</b></td><td>81.57 <b>(-26.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.50 (n/a)</td><td>492.54 (n/a)</td><td>489.00 (n/a)</td><td>380.10 (n/a)</td><td>111.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (+9.68%)</td><td>0.03 (+15.36%)</td><td>0.02 <b>(+40.02%)</b></td><td>0.02 (+12.70%)</td><td>0.01 (+10.11%)</td><td>489.20 (-11.26%)</td><td>350.52 (-13.17%)</td><td>332.60 <b>(-28.58%)</b></td><td>218.70 (-8.84%)</td><td>127.53 (-7.32%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.30 (n/a)</td><td>403.70 (n/a)</td><td>465.70 (n/a)</td><td>239.90 (n/a)</td><td>137.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 <b>(-29.94%)</b></td><td>0.03 (-0.12%)</td><td>0.02 (+9.26%)</td><td>0.02 (+19.56%)</td><td>0.01 <b>(-46.58%)</b></td><td>496.50 (-16.36%)</td><td>386.38 (-9.99%)</td><td>428.00 (-8.49%)</td><td>248.60 <b>(+42.71%)</b></td><td>109.95 <b>(-28.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>593.60 (n/a)</td><td>429.24 (n/a)</td><td>467.70 (n/a)</td><td>174.20 (n/a)</td><td>154.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (-14.47%)</td><td>0.02 <b>(-25.58%)</b></td><td>0.02 <b>(-23.42%)</b></td><td>0.00 <b>(-74.50%)</b></td><td>0.01 <b>(+43.13%)</b></td><td>1879.70 <b>(+292.18%)</b></td><td>704.86 <b>(+89.92%)</b></td><td>405.60 <b>(+30.59%)</b></td><td>335.60 (+16.93%)</td><td>660.87 <b>(+587.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.30 (n/a)</td><td>371.14 (n/a)</td><td>310.60 (n/a)</td><td>287.00 (n/a)</td><td>96.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.36 (-7.79%)</td><td>0.31 <b>(+42.84%)</b></td><td>0.32 <b>(+64.22%)</b></td><td>0.20 <b>(+328.50%)</b></td><td>0.06 <b>(-51.19%)</b></td><td>485.50 <b>(-76.66%)</b></td><td>331.98 <b>(-55.83%)</b></td><td>306.30 <b>(-39.11%)</b></td><td>273.20 (+8.46%)</td><td>87.09 <b>(-88.43%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>2080.30 (n/a)</td><td>751.64 (n/a)</td><td>503.00 (n/a)</td><td>251.90 (n/a)</td><td>752.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.33 (-1.62%)</td><td>0.20 (-14.73%)</td><td>0.19 (-13.53%)</td><td>0.10 <b>(-27.09%)</b></td><td>0.08 (-7.69%)</td><td>1030.30 <b>(+37.15%)</b></td><td>574.20 <b>(+20.27%)</b></td><td>516.80 (+15.64%)</td><td>300.70 (+1.66%)</td><td>272.38 <b>(+40.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>751.20 (n/a)</td><td>477.42 (n/a)</td><td>446.90 (n/a)</td><td>295.80 (n/a)</td><td>193.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.40 (-3.69%)</td><td>0.30 (+5.95%)</td><td>0.30 <b>(+38.91%)</b></td><td>0.16 (-17.19%)</td><td>0.09 (-10.89%)</td><td>619.70 <b>(+20.75%)</b></td><td>365.08 (-5.35%)</td><td>325.50 <b>(-28.00%)</b></td><td>246.80 (+3.83%)</td><td>148.71 (+18.82%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>513.20 (n/a)</td><td>385.70 (n/a)</td><td>452.10 (n/a)</td><td>237.70 (n/a)</td><td>125.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.24 (-15.70%)</td><td>0.18 (+4.13%)</td><td>0.18 (+5.33%)</td><td>0.11 <b>(+195.03%)</b></td><td>0.05 <b>(-51.45%)</b></td><td>654.50 <b>(-66.10%)</b></td><td>449.12 <b>(-37.82%)</b></td><td>420.50 (-5.06%)</td><td>312.30 (+18.61%)</td><td>134.63 <b>(-80.63%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1930.80 (n/a)</td><td>722.30 (n/a)</td><td>442.90 (n/a)</td><td>263.30 (n/a)</td><td>695.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.31 (+0.58%)</td><td>0.17 (-12.76%)</td><td>0.15 (-2.28%)</td><td>0.12 (-11.58%)</td><td>0.07 (+0.47%)</td><td>601.90 (+13.10%)</td><td>468.86 (+14.97%)</td><td>496.90 (+2.33%)</td><td>240.90 (-0.58%)</td><td>135.94 (+3.82%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>532.20 (n/a)</td><td>407.80 (n/a)</td><td>485.60 (n/a)</td><td>242.30 (n/a)</td><td>130.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.22 (-14.84%)</td><td>0.14 (-11.75%)</td><td>0.15 (-9.39%)</td><td>0.03 <b>(-67.21%)</b></td><td>0.07 (+8.64%)</td><td>2504.50 <b>(+204.98%)</b></td><td>864.62 <b>(+63.12%)</b></td><td>488.60 (+10.37%)</td><td>342.90 (+17.43%)</td><td>920.58 <b>(+328.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>821.20 (n/a)</td><td>530.04 (n/a)</td><td>442.70 (n/a)</td><td>292.00 (n/a)</td><td>214.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.43 (-9.41%)</td><td>0.31 (-0.47%)</td><td>0.29 (+10.80%)</td><td>0.17 <b>(-34.32%)</b></td><td>0.11 (+18.87%)</td><td>792.60 <b>(+52.25%)</b></td><td>479.76 (+7.31%)</td><td>445.90 (-9.76%)</td><td>306.60 (+10.41%)</td><td>197.62 <b>(+100.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>520.60 (n/a)</td><td>447.06 (n/a)</td><td>494.10 (n/a)</td><td>277.70 (n/a)</td><td>98.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.54 <b>(+35.79%)</b></td><td>0.32 (+6.15%)</td><td>0.26 (-4.44%)</td><td>0.20 (-14.13%)</td><td>0.14 <b>(+96.58%)</b></td><td>665.60 (+16.47%)</td><td>472.56 (+3.22%)</td><td>501.60 (+4.65%)</td><td>241.70 <b>(-26.36%)</b></td><td>173.68 <b>(+68.53%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>571.50 (n/a)</td><td>457.82 (n/a)</td><td>479.30 (n/a)</td><td>328.20 (n/a)</td><td>103.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.37 (-19.93%)</td><td>0.26 <b>(-24.79%)</b></td><td>0.26 <b>(-23.17%)</b></td><td>0.16 <b>(-27.02%)</b></td><td>0.07 <b>(-30.07%)</b></td><td>809.50 <b>(+37.02%)</b></td><td>541.82 <b>(+31.51%)</b></td><td>513.60 <b>(+30.16%)</b></td><td>355.20 <b>(+24.89%)</b></td><td>164.97 <b>(+26.25%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>590.80 (n/a)</td><td>412.00 (n/a)</td><td>394.60 (n/a)</td><td>284.40 (n/a)</td><td>130.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (+10.50%)</td><td>0.01 <b>(+30.78%)</b></td><td>0.01 <b>(+62.65%)</b></td><td>0.01 <b>(-22.40%)</b></td><td>0.00 <b>(+21.87%)</b></td><td>767.90 <b>(+28.89%)</b></td><td>405.72 (-18.49%)</td><td>347.10 <b>(-38.52%)</b></td><td>254.50 (-9.50%)</td><td>206.31 <b>(+57.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.80 (n/a)</td><td>497.74 (n/a)</td><td>564.60 (n/a)</td><td>281.20 (n/a)</td><td>130.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 (+19.62%)</td><td>0.01 <b>(+29.64%)</b></td><td>0.01 <b>(+29.17%)</b></td><td>0.01 (+14.28%)</td><td>0.00 <b>(+20.48%)</b></td><td>502.90 (-12.49%)</td><td>348.98 <b>(-22.66%)</b></td><td>313.30 <b>(-22.58%)</b></td><td>305.80 (-16.40%)</td><td>86.14 (-10.73%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.70 (n/a)</td><td>451.22 (n/a)</td><td>404.70 (n/a)</td><td>365.80 (n/a)</td><td>96.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 <b>(+32.78%)</b></td><td>0.01 (+8.24%)</td><td>0.01 (-9.26%)</td><td>0.01 (-13.56%)</td><td>0.00 <b>(+218.51%)</b></td><td>563.80 (+15.68%)</td><td>434.70 (+0.07%)</td><td>492.60 (+10.20%)</td><td>272.50 <b>(-24.70%)</b></td><td>135.30 <b>(+180.86%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.40 (n/a)</td><td>434.40 (n/a)</td><td>447.00 (n/a)</td><td>361.90 (n/a)</td><td>48.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.60 (+7.16%)</td><td>0.44 (+9.69%)</td><td>0.50 (+5.79%)</td><td>0.26 <b>(+26.01%)</b></td><td>0.16 (+0.80%)</td><td>499.80 <b>(-20.64%)</b></td><td>343.70 (-11.59%)</td><td>266.20 (-5.47%)</td><td>219.60 (-6.67%)</td><td>139.63 <b>(-22.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.47 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>629.80 (n/a)</td><td>388.76 (n/a)</td><td>281.60 (n/a)</td><td>235.30 (n/a)</td><td>179.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.55 <b>(-23.14%)</b></td><td>0.41 (+3.24%)</td><td>0.46 <b>(+41.29%)</b></td><td>0.21 (-8.31%)</td><td>0.15 <b>(-26.71%)</b></td><td>638.20 (+9.06%)</td><td>367.36 (-6.69%)</td><td>286.60 <b>(-29.23%)</b></td><td>241.80 <b>(+30.14%)</b></td><td>167.01 (+2.56%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.71 (n/a)</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>585.20 (n/a)</td><td>393.68 (n/a)</td><td>405.00 (n/a)</td><td>185.80 (n/a)</td><td>162.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.49 (-15.27%)</td><td>0.39 (+6.68%)</td><td>0.46 (+16.17%)</td><td>0.25 (+17.25%)</td><td>0.11 <b>(-29.50%)</b></td><td>525.10 (-14.71%)</td><td>361.26 (-13.28%)</td><td>289.20 (-13.90%)</td><td>270.10 (+18.00%)</td><td>114.26 <b>(-36.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.58 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>615.70 (n/a)</td><td>416.56 (n/a)</td><td>335.90 (n/a)</td><td>228.90 (n/a)</td><td>178.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.51 (-13.81%)</td><td>0.38 <b>(-20.27%)</b></td><td>0.40 (-18.64%)</td><td>0.22 <b>(-24.75%)</b></td><td>0.12 (-6.80%)</td><td>608.00 <b>(+32.90%)</b></td><td>384.98 <b>(+28.69%)</b></td><td>328.10 <b>(+22.88%)</b></td><td>257.00 (+16.03%)</td><td>144.94 <b>(+47.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.60 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td><td>457.50 (n/a)</td><td>299.16 (n/a)</td><td>267.00 (n/a)</td><td>221.50 (n/a)</td><td>98.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.52 (-10.52%)</td><td>0.44 (-1.28%)</td><td>0.45 (-1.09%)</td><td>0.28 (-9.37%)</td><td>0.09 (-15.03%)</td><td>469.60 (+10.34%)</td><td>316.04 (+0.86%)</td><td>291.50 (+1.11%)</td><td>251.70 (+11.77%)</td><td>88.24 (+7.48%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>425.60 (n/a)</td><td>313.34 (n/a)</td><td>288.30 (n/a)</td><td>225.20 (n/a)</td><td>82.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (+1.78%)</td><td>0.01 (+6.32%)</td><td>0.01 <b>(+60.52%)</b></td><td>0.01 <b>(-21.42%)</b></td><td>0.00 (+10.87%)</td><td>672.20 <b>(+27.26%)</b></td><td>401.80 (-1.68%)</td><td>300.80 <b>(-37.70%)</b></td><td>246.40 (-1.75%)</td><td>177.29 <b>(+40.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>408.66 (n/a)</td><td>482.80 (n/a)</td><td>250.80 (n/a)</td><td>126.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (-7.42%)</td><td>0.01 <b>(+29.33%)</b></td><td>0.01 <b>(+59.50%)</b></td><td>0.01 <b>(+75.98%)</b></td><td>0.00 <b>(-84.32%)</b></td><td>301.90 <b>(-43.17%)</b></td><td>284.30 <b>(-29.33%)</b></td><td>280.10 <b>(-37.31%)</b></td><td>271.40 (+8.04%)</td><td>12.30 <b>(-90.29%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.20 (n/a)</td><td>402.32 (n/a)</td><td>446.80 (n/a)</td><td>251.20 (n/a)</td><td>126.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-41.67%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(-36.38%)</b></td><td>19170.96 <b>(+23.69%)</b></td><td>15456.11 <b>(+55.16%)</b></td><td>17163.05 <b>(+82.08%)</b></td><td>7836.15 <b>(+37.93%)</b></td><td>4596.49 (+6.18%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>15499.75 (n/a)</td><td>9961.22 (n/a)</td><td>9426.18 (n/a)</td><td>5681.10 (n/a)</td><td>4328.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.00 (+0.00%)</td><td>0.00 (+6.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+7.82%)</td><td>22982.51 <b>(+20.45%)</b></td><td>16106.05 (+6.10%)</td><td>16633.39 (+0.27%)</td><td>7497.29 (-2.88%)</td><td>7010.54 <b>(+61.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19081.07 (n/a)</td><td>15180.38 (n/a)</td><td>16587.92 (n/a)</td><td>7720.00 (n/a)</td><td>4352.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.15 (+1.88%)</td><td>0.09 (-17.39%)</td><td>0.08 <b>(-33.01%)</b></td><td>0.08 (-1.79%)</td><td>0.03 (-6.37%)</td><td>27319.71 (+1.85%)</td><td>23722.69 (+19.67%)</td><td>25321.65 <b>(+49.27%)</b></td><td>14318.24 (-1.79%)</td><td>5322.31 (-11.19%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>26822.77 (n/a)</td><td>19822.91 (n/a)</td><td>16963.81 (n/a)</td><td>14579.20 (n/a)</td><td>5993.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.47 (-5.14%)</td><td>1.07 (-0.19%)</td><td>1.07 (-11.85%)</td><td>0.58 <b>(+260.69%)</b></td><td>0.38 <b>(-33.64%)</b></td><td>906.50 <b>(-72.27%)</b></td><td>550.14 <b>(-44.39%)</b></td><td>488.90 (+13.43%)</td><td>357.40 (+5.40%)</td><td>226.98 <b>(-82.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>1.55 (n/a)</td><td>1.08 (n/a)</td><td>1.22 (n/a)</td><td>0.16 (n/a)</td><td>0.57 (n/a)</td><td>3269.50 (n/a)</td><td>989.28 (n/a)</td><td>431.00 (n/a)</td><td>339.10 (n/a)</td><td>1277.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.11 <b>(+36.98%)</b></td><td>2.19 <b>(+47.91%)</b></td><td>2.31 <b>(+45.77%)</b></td><td>1.32 <b>(+333.46%)</b></td><td>0.68 (-6.57%)</td><td>796.60 <b>(-76.93%)</b></td><td>522.64 <b>(-55.66%)</b></td><td>453.80 <b>(-31.40%)</b></td><td>337.50 <b>(-26.98%)</b></td><td>178.77 <b>(-85.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.27 (n/a)</td><td>1.48 (n/a)</td><td>1.59 (n/a)</td><td>0.30 (n/a)</td><td>0.73 (n/a)</td><td>3452.80 (n/a)</td><td>1178.66 (n/a)</td><td>661.50 (n/a)</td><td>462.20 (n/a)</td><td>1275.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.74 <b>(-24.73%)</b></td><td>1.22 (-4.49%)</td><td>1.01 (+3.64%)</td><td>0.89 <b>(+87.34%)</b></td><td>0.37 <b>(-49.95%)</b></td><td>588.40 <b>(-46.63%)</b></td><td>460.76 (-16.87%)</td><td>517.00 (-3.51%)</td><td>301.50 <b>(+32.82%)</b></td><td>124.72 <b>(-63.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:41:02</td><td>2.31 (n/a)</td><td>1.27 (n/a)</td><td>0.98 (n/a)</td><td>0.48 (n/a)</td><td>0.74 (n/a)</td><td>1102.40 (n/a)</td><td>554.24 (n/a)</td><td>535.80 (n/a)</td><td>227.00 (n/a)</td><td>344.42 (n/a)</td>
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
