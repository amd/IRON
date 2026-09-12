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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (+15.70%)</td><td>0.04 <b>(+49.15%)</b></td><td>0.05 <b>(+91.58%)</b></td><td>0.02 (+1.21%)</td><td>0.01 <b>(+42.56%)</b></td><td>614.20 (-1.19%)</td><td>328.94 <b>(-28.77%)</b></td><td>245.90 <b>(-47.80%)</b></td><td>235.50 (-13.58%)</td><td>162.61 <b>(+30.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>621.60 (n/a)</td><td>461.80 (n/a)</td><td>471.10 (n/a)</td><td>272.50 (n/a)</td><td>124.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 <b>(-29.18%)</b></td><td>0.05 (+11.69%)</td><td>0.05 <b>(+84.63%)</b></td><td>0.03 <b>(+39.67%)</b></td><td>0.01 <b>(-52.83%)</b></td><td>427.00 <b>(-28.40%)</b></td><td>284.28 <b>(-24.65%)</b></td><td>238.90 <b>(-45.84%)</b></td><td>209.60 <b>(+41.24%)</b></td><td>88.24 <b>(-49.60%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>596.40 (n/a)</td><td>377.26 (n/a)</td><td>441.10 (n/a)</td><td>148.40 (n/a)</td><td>175.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 (-9.05%)</td><td>0.04 (+6.51%)</td><td>0.04 <b>(+47.96%)</b></td><td>0.02 <b>(-25.92%)</b></td><td>0.01 (-16.98%)</td><td>727.30 <b>(+34.99%)</b></td><td>356.94 (-4.31%)</td><td>291.10 <b>(-32.41%)</b></td><td>219.40 (+9.97%)</td><td>209.37 <b>(+38.91%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>538.80 (n/a)</td><td>373.00 (n/a)</td><td>430.70 (n/a)</td><td>199.50 (n/a)</td><td>150.73 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (-3.36%)</td><td>0.02 <b>(+35.54%)</b></td><td>0.02 <b>(+63.34%)</b></td><td>0.01 <b>(+22.33%)</b></td><td>0.00 <b>(-31.02%)</b></td><td>424.50 (-18.26%)</td><td>289.58 <b>(-31.10%)</b></td><td>268.30 <b>(-38.77%)</b></td><td>207.30 (+3.44%)</td><td>81.69 <b>(-36.57%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>519.30 (n/a)</td><td>420.32 (n/a)</td><td>438.20 (n/a)</td><td>200.40 (n/a)</td><td>128.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (+13.15%)</td><td>0.02 <b>(+33.79%)</b></td><td>0.02 <b>(+45.83%)</b></td><td>0.01 <b>(+30.85%)</b></td><td>0.00 (-5.08%)</td><td>456.90 <b>(-23.58%)</b></td><td>319.10 <b>(-26.73%)</b></td><td>289.20 <b>(-31.42%)</b></td><td>256.90 (-11.63%)</td><td>78.90 <b>(-32.25%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>597.90 (n/a)</td><td>435.54 (n/a)</td><td>421.70 (n/a)</td><td>290.70 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (+2.37%)</td><td>0.02 (+16.56%)</td><td>0.02 <b>(+62.43%)</b></td><td>0.01 (-1.72%)</td><td>0.01 (+15.71%)</td><td>593.50 (+1.75%)</td><td>351.96 (-11.08%)</td><td>262.00 <b>(-38.44%)</b></td><td>224.50 (-2.31%)</td><td>159.92 (+15.90%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.30 (n/a)</td><td>395.80 (n/a)</td><td>425.60 (n/a)</td><td>229.80 (n/a)</td><td>137.98 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 <b>(+48.36%)</b></td><td>0.01 <b>(+28.63%)</b></td><td>0.01 (-0.28%)</td><td>0.01 <b>(+317.69%)</b></td><td>0.00 (-7.21%)</td><td>496.50 <b>(-76.06%)</b></td><td>415.80 <b>(-45.02%)</b></td><td>438.70 (+0.30%)</td><td>252.60 <b>(-32.59%)</b></td><td>94.84 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2073.80 (n/a)</td><td>756.24 (n/a)</td><td>437.40 (n/a)</td><td>374.70 (n/a)</td><td>737.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (-12.57%)</td><td>0.02 (+11.39%)</td><td>0.02 <b>(+59.33%)</b></td><td>0.01 <b>(-21.33%)</b></td><td>0.01 (-12.64%)</td><td>784.50 <b>(+27.11%)</b></td><td>387.12 (-7.56%)</td><td>279.90 <b>(-37.23%)</b></td><td>239.10 (+14.40%)</td><td>226.17 <b>(+37.71%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.20 (n/a)</td><td>418.80 (n/a)</td><td>445.90 (n/a)</td><td>209.00 (n/a)</td><td>164.23 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 <b>(+44.98%)</b></td><td>0.01 (-4.64%)</td><td>0.01 (-16.37%)</td><td>0.00 <b>(-46.91%)</b></td><td>0.01 <b>(+83.62%)</b></td><td>1867.30 <b>(+88.37%)</b></td><td>758.30 <b>(+40.24%)</b></td><td>577.10 (+19.58%)</td><td>245.60 <b>(-31.03%)</b></td><td>637.63 <b>(+145.97%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>991.30 (n/a)</td><td>540.72 (n/a)</td><td>482.60 (n/a)</td><td>356.10 (n/a)</td><td>259.24 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>677.50 (n/a)</td><td>384.32 (n/a)</td><td>245.70 (n/a)</td><td>219.70 (n/a)</td><td>215.57 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.80 (n/a)</td><td>415.50 (n/a)</td><td>468.40 (n/a)</td><td>244.60 (n/a)</td><td>159.47 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.90 (n/a)</td><td>419.38 (n/a)</td><td>483.10 (n/a)</td><td>284.60 (n/a)</td><td>122.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>304.10 (n/a)</td><td>272.70 (n/a)</td><td>204.10 (n/a)</td><td>108.06 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1878.90 (n/a)</td><td>633.40 (n/a)</td><td>269.90 (n/a)</td><td>262.80 (n/a)</td><td>703.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.00 (n/a)</td><td>410.90 (n/a)</td><td>340.20 (n/a)</td><td>296.30 (n/a)</td><td>143.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.77 <b>(-39.30%)</b></td><td>0.49 <b>(-43.14%)</b></td><td>0.44 <b>(-47.58%)</b></td><td>0.18 <b>(-64.25%)</b></td><td>0.22 (-18.99%)</td><td>2504.90 <b>(+179.75%)</b></td><td>1186.42 <b>(+104.94%)</b></td><td>1037.00 <b>(+90.80%)</b></td><td>593.00 <b>(+64.72%)</b></td><td>762.75 <b>(+289.30%)</b></td><td>56.58 <b>(-39.30%)</b></td><td>35.87 <b>(-43.14%)</b></td><td>32.36 <b>(-47.58%)</b></td><td>13.40 <b>(-64.25%)</b></td><td>16.20 (-18.99%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.27 (n/a)</td><td>0.86 (n/a)</td><td>0.84 (n/a)</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>895.40 (n/a)</td><td>578.92 (n/a)</td><td>543.50 (n/a)</td><td>360.00 (n/a)</td><td>195.93 (n/a)</td><td>93.21 (n/a)</td><td>63.08 (n/a)</td><td>61.73 (n/a)</td><td>37.47 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.19 <b>(-21.52%)</b></td><td>1.07 (-11.05%)</td><td>1.15 (-9.61%)</td><td>0.91 <b>(+28.84%)</b></td><td>0.14 <b>(-55.66%)</b></td><td>723.60 <b>(-22.39%)</b></td><td>620.52 (+6.21%)</td><td>571.60 (+10.63%)</td><td>549.50 <b>(+27.41%)</b></td><td>82.05 <b>(-58.82%)</b></td><td>122.12 <b>(-21.52%)</b></td><td>109.61 (-11.05%)</td><td>117.41 (-9.61%)</td><td>92.74 <b>(+28.84%)</b></td><td>13.83 <b>(-55.66%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.52 (n/a)</td><td>1.20 (n/a)</td><td>1.27 (n/a)</td><td>0.70 (n/a)</td><td>0.30 (n/a)</td><td>932.30 (n/a)</td><td>584.22 (n/a)</td><td>516.70 (n/a)</td><td>431.30 (n/a)</td><td>199.25 (n/a)</td><td>155.61 (n/a)</td><td>123.22 (n/a)</td><td>129.89 (n/a)</td><td>71.98 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.40 (-2.30%)</td><td>1.14 (+2.10%)</td><td>1.25 (+10.10%)</td><td>0.76 (+13.91%)</td><td>0.25 (-12.85%)</td><td>996.40 (-12.21%)</td><td>693.54 (-4.19%)</td><td>604.80 (-9.18%)</td><td>538.70 (+2.36%)</td><td>182.65 <b>(-23.64%)</b></td><td>155.71 (-2.30%)</td><td>126.73 (+2.10%)</td><td>138.69 (+10.10%)</td><td>84.19 (+13.91%)</td><td>27.81 (-12.85%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.43 (n/a)</td><td>1.12 (n/a)</td><td>1.13 (n/a)</td><td>0.66 (n/a)</td><td>0.29 (n/a)</td><td>1135.00 (n/a)</td><td>723.86 (n/a)</td><td>665.90 (n/a)</td><td>526.30 (n/a)</td><td>239.21 (n/a)</td><td>159.38 (n/a)</td><td>124.12 (n/a)</td><td>125.97 (n/a)</td><td>73.91 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.63 (+8.87%)</td><td>1.27 (+3.52%)</td><td>1.36 (+4.76%)</td><td>0.68 <b>(-29.53%)</b></td><td>0.37 <b>(+76.09%)</b></td><td>1531.40 <b>(+41.91%)</b></td><td>907.56 (+3.63%)</td><td>773.40 (-4.54%)</td><td>643.40 (-8.14%)</td><td>360.48 <b>(+136.96%)</b></td><td>208.62 (+8.87%)</td><td>162.45 (+3.52%)</td><td>173.54 (+4.76%)</td><td>87.64 <b>(-29.53%)</b></td><td>46.94 <b>(+76.09%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.50 (n/a)</td><td>1.23 (n/a)</td><td>1.29 (n/a)</td><td>0.97 (n/a)</td><td>0.21 (n/a)</td><td>1079.10 (n/a)</td><td>875.76 (n/a)</td><td>810.20 (n/a)</td><td>700.40 (n/a)</td><td>152.13 (n/a)</td><td>191.62 (n/a)</td><td>156.93 (n/a)</td><td>165.65 (n/a)</td><td>124.37 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.95 <b>(+40.62%)</b></td><td>1.56 (-3.81%)</td><td>1.57 (-16.44%)</td><td>0.32 <b>(-62.62%)</b></td><td>1.01 <b>(+97.90%)</b></td><td>3228.40 <b>(+167.54%)</b></td><td>1178.42 <b>(+63.92%)</b></td><td>668.80 (+19.66%)</td><td>355.00 <b>(-28.89%)</b></td><td>1180.82 <b>(+300.84%)</b></td><td>378.05 <b>(+40.62%)</b></td><td>199.67 (-3.81%)</td><td>200.68 (-16.44%)</td><td>41.57 <b>(-62.62%)</b></td><td>129.05 <b>(+97.90%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.10 (n/a)</td><td>1.62 (n/a)</td><td>1.88 (n/a)</td><td>0.87 (n/a)</td><td>0.51 (n/a)</td><td>1206.70 (n/a)</td><td>718.92 (n/a)</td><td>558.90 (n/a)</td><td>499.20 (n/a)</td><td>294.59 (n/a)</td><td>268.84 (n/a)</td><td>207.57 (n/a)</td><td>240.16 (n/a)</td><td>111.22 (n/a)</td><td>65.21 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.52 (+16.34%)</td><td>1.67 (-0.89%)</td><td>1.60 (+2.84%)</td><td>0.65 <b>(-52.95%)</b></td><td>0.74 <b>(+127.75%)</b></td><td>1611.80 <b>(+112.53%)</b></td><td>784.52 <b>(+22.80%)</b></td><td>656.90 (-2.77%)</td><td>415.90 (-14.05%)</td><td>483.32 <b>(+329.70%)</b></td><td>322.69 (+16.34%)</td><td>213.94 (-0.89%)</td><td>204.31 (+2.84%)</td><td>83.27 <b>(-52.95%)</b></td><td>94.10 <b>(+127.75%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.17 (n/a)</td><td>1.69 (n/a)</td><td>1.55 (n/a)</td><td>1.38 (n/a)</td><td>0.32 (n/a)</td><td>758.40 (n/a)</td><td>638.86 (n/a)</td><td>675.60 (n/a)</td><td>483.90 (n/a)</td><td>112.48 (n/a)</td><td>277.37 (n/a)</td><td>215.87 (n/a)</td><td>198.66 (n/a)</td><td>176.97 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.00 (+18.75%)</td><td>1.09 (-3.88%)</td><td>0.83 <b>(-29.29%)</b></td><td>0.48 (-2.02%)</td><td>0.62 <b>(+36.41%)</b></td><td>2184.40 (+2.06%)</td><td>1227.64 (+11.49%)</td><td>1270.40 <b>(+41.42%)</b></td><td>523.80 (-15.79%)</td><td>651.21 (+7.41%)</td><td>256.25 (+18.75%)</td><td>140.10 (-3.88%)</td><td>105.65 <b>(-29.29%)</b></td><td>61.44 (-2.02%)</td><td>78.77 <b>(+36.41%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.69 (n/a)</td><td>1.14 (n/a)</td><td>1.17 (n/a)</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>2140.40 (n/a)</td><td>1101.16 (n/a)</td><td>898.30 (n/a)</td><td>622.00 (n/a)</td><td>606.27 (n/a)</td><td>215.78 (n/a)</td><td>145.75 (n/a)</td><td>149.42 (n/a)</td><td>62.71 (n/a)</td><td>57.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.12 (-12.32%)</td><td>0.59 (-13.46%)</td><td>0.42 <b>(-20.77%)</b></td><td>0.33 <b>(-26.90%)</b></td><td>0.34 (-2.28%)</td><td>1076.80 <b>(+36.81%)</b></td><td>756.78 <b>(+23.87%)</b></td><td>866.40 <b>(+26.22%)</b></td><td>322.90 (+14.06%)</td><td>334.81 <b>(+57.22%)</b></td><td>51.96 (-12.32%)</td><td>27.51 (-13.46%)</td><td>19.37 <b>(-20.77%)</b></td><td>15.58 <b>(-26.90%)</b></td><td>15.64 (-2.28%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.27 (n/a)</td><td>0.68 (n/a)</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>787.10 (n/a)</td><td>610.94 (n/a)</td><td>686.40 (n/a)</td><td>283.10 (n/a)</td><td>212.96 (n/a)</td><td>59.26 (n/a)</td><td>31.78 (n/a)</td><td>24.44 (n/a)</td><td>21.31 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>4.14 (+13.20%)</td><td>2.50 <b>(+27.02%)</b></td><td>2.20 <b>(+106.36%)</b></td><td>1.18 <b>(+71.52%)</b></td><td>1.10 <b>(-28.80%)</b></td><td>2219.90 <b>(-41.70%)</b></td><td>1241.60 <b>(-44.05%)</b></td><td>1191.20 <b>(-51.54%)</b></td><td>632.70 (-11.66%)</td><td>600.96 <b>(-58.73%)</b></td><td>848.57 (+13.20%)</td><td>512.19 <b>(+27.02%)</b></td><td>450.69 <b>(+106.36%)</b></td><td>241.85 <b>(+71.52%)</b></td><td>225.88 <b>(-28.80%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.66 (n/a)</td><td>1.97 (n/a)</td><td>1.07 (n/a)</td><td>0.69 (n/a)</td><td>1.55 (n/a)</td><td>3807.50 (n/a)</td><td>2219.12 (n/a)</td><td>2458.20 (n/a)</td><td>716.20 (n/a)</td><td>1456.33 (n/a)</td><td>749.60 (n/a)</td><td>403.23 (n/a)</td><td>218.40 (n/a)</td><td>141.00 (n/a)</td><td>317.27 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>378.30 (n/a)</td><td>300.66 (n/a)</td><td>294.90 (n/a)</td><td>248.80 (n/a)</td><td>49.55 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.50 (n/a)</td><td>318.48 (n/a)</td><td>273.30 (n/a)</td><td>239.70 (n/a)</td><td>94.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>357.14 (n/a)</td><td>318.00 (n/a)</td><td>231.80 (n/a)</td><td>133.86 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1985.10 (n/a)</td><td>802.14 (n/a)</td><td>512.30 (n/a)</td><td>454.70 (n/a)</td><td>662.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1974.80 (n/a)</td><td>816.82 (n/a)</td><td>543.50 (n/a)</td><td>473.00 (n/a)</td><td>648.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.40 (n/a)</td><td>418.56 (n/a)</td><td>383.20 (n/a)</td><td>293.00 (n/a)</td><td>136.07 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.48 (-2.58%)</td><td>0.27 <b>(-34.53%)</b></td><td>0.25 <b>(-44.28%)</b></td><td>0.12 <b>(-54.13%)</b></td><td>0.14 <b>(+56.08%)</b></td><td>1821.10 <b>(+117.99%)</b></td><td>1013.90 <b>(+82.04%)</b></td><td>867.80 <b>(+79.45%)</b></td><td>459.40 (+2.64%)</td><td>539.31 <b>(+239.00%)</b></td><td>20.54 (-2.58%)</td><td>11.67 <b>(-34.53%)</b></td><td>10.87 <b>(-44.28%)</b></td><td>5.18 <b>(-54.13%)</b></td><td>6.03 <b>(+56.08%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>0.09 (n/a)</td><td>835.40 (n/a)</td><td>556.96 (n/a)</td><td>483.60 (n/a)</td><td>447.60 (n/a)</td><td>159.09 (n/a)</td><td>21.08 (n/a)</td><td>17.82 (n/a)</td><td>19.52 (n/a)</td><td>11.30 (n/a)</td><td>3.86 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.45 (-4.92%)</td><td>0.30 (-19.31%)</td><td>0.36 (-0.63%)</td><td>0.13 <b>(-59.00%)</b></td><td>0.15 <b>(+133.20%)</b></td><td>1722.90 <b>(+143.93%)</b></td><td>938.84 <b>(+56.70%)</b></td><td>619.20 (+0.63%)</td><td>488.40 (+5.19%)</td><td>557.03 <b>(+499.50%)</b></td><td>19.32 (-4.92%)</td><td>12.98 (-19.31%)</td><td>15.24 (-0.63%)</td><td>5.48 <b>(-59.00%)</b></td><td>6.31 <b>(+133.20%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>706.30 (n/a)</td><td>599.12 (n/a)</td><td>615.30 (n/a)</td><td>464.30 (n/a)</td><td>92.91 (n/a)</td><td>20.32 (n/a)</td><td>16.08 (n/a)</td><td>15.34 (n/a)</td><td>13.36 (n/a)</td><td>2.71 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.31 (+0.10%)</td><td>0.31 (+0.37%)</td><td>0.31 (-0.20%)</td><td>0.30 (+1.29%)</td><td>0.00 <b>(-39.95%)</b></td><td>82669.60 (-1.27%)</td><td>81831.66 (-0.37%)</td><td>81895.60 (+0.20%)</td><td>81198.40 (-0.10%)</td><td>578.73 <b>(-40.86%)</b></td><td>211.58 (+0.10%)</td><td>209.95 (+0.37%)</td><td>209.78 (-0.20%)</td><td>207.81 (+1.29%)</td><td>1.48 <b>(-39.95%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83735.30 (n/a)</td><td>82138.82 (n/a)</td><td>81730.00 (n/a)</td><td>81282.90 (n/a)</td><td>978.60 (n/a)</td><td>211.36 (n/a)</td><td>209.18 (n/a)</td><td>210.20 (n/a)</td><td>205.17 (n/a)</td><td>2.47 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.17 (+1.79%)</td><td>1.14 (+1.51%)</td><td>1.15 (+1.10%)</td><td>1.11 (+2.66%)</td><td>0.02 <b>(-20.73%)</b></td><td>22610.00 (-2.59%)</td><td>22017.58 (-1.51%)</td><td>21934.50 (-1.09%)</td><td>21515.60 (-1.76%)</td><td>399.93 <b>(-24.15%)</b></td><td>798.48 (+1.79%)</td><td>780.48 (+1.51%)</td><td>783.23 (+1.10%)</td><td>759.83 (+2.66%)</td><td>14.10 <b>(-20.73%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.13 (n/a)</td><td>1.08 (n/a)</td><td>0.03 (n/a)</td><td>23212.20 (n/a)</td><td>22354.56 (n/a)</td><td>22176.00 (n/a)</td><td>21901.30 (n/a)</td><td>527.30 (n/a)</td><td>784.42 (n/a)</td><td>768.85 (n/a)</td><td>774.70 (n/a)</td><td>740.12 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.41 (-19.61%)</td><td>1.98 (+1.14%)</td><td>1.96 (+7.64%)</td><td>1.59 <b>(+53.74%)</b></td><td>0.34 <b>(-57.34%)</b></td><td>5077.00 <b>(-34.96%)</b></td><td>4164.40 (-12.30%)</td><td>4110.90 (-7.10%)</td><td>3349.30 <b>(+24.39%)</b></td><td>714.87 <b>(-65.12%)</b></td><td>631.16 (-19.61%)</td><td>519.76 (+1.14%)</td><td>514.22 (+7.64%)</td><td>416.37 <b>(+53.74%)</b></td><td>88.94 <b>(-57.34%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.99 (n/a)</td><td>1.96 (n/a)</td><td>1.82 (n/a)</td><td>1.03 (n/a)</td><td>0.80 (n/a)</td><td>7805.40 (n/a)</td><td>4748.36 (n/a)</td><td>4425.00 (n/a)</td><td>2692.50 (n/a)</td><td>2049.39 (n/a)</td><td>785.13 (n/a)</td><td>513.92 (n/a)</td><td>477.73 (n/a)</td><td>270.83 (n/a)</td><td>208.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.21 (-5.75%)</td><td>0.18 (-13.87%)</td><td>0.19 (-13.35%)</td><td>0.16 <b>(-21.45%)</b></td><td>0.02 <b>(+130.57%)</b></td><td>7961.70 <b>(+27.31%)</b></td><td>6916.48 (+17.60%)</td><td>6576.30 (+15.41%)</td><td>5990.50 (+6.10%)</td><td>950.31 <b>(+217.61%)</b></td><td>11.20 (-5.75%)</td><td>9.85 (-13.87%)</td><td>10.20 (-13.35%)</td><td>8.43 <b>(-21.45%)</b></td><td>1.32 <b>(+130.57%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td><td>6253.80 (n/a)</td><td>5881.56 (n/a)</td><td>5698.20 (n/a)</td><td>5646.00 (n/a)</td><td>299.21 (n/a)</td><td>11.89 (n/a)</td><td>11.43 (n/a)</td><td>11.78 (n/a)</td><td>10.73 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.73 (n/a)</td><td>3.59 (n/a)</td><td>0.08 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.73 (n/a)</td><td>3.59 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>7.51 (-1.90%)</td><td>6.08 (-10.64%)</td><td>5.72 (-16.56%)</td><td>5.05 (-11.30%)</td><td>0.97 <b>(+27.13%)</b></td><td>7.51 (-1.90%)</td><td>6.07 (-10.64%)</td><td>5.71 (-16.56%)</td><td>5.04 (-11.30%)</td><td>0.97 <b>(+27.13%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>7.66 (n/a)</td><td>6.80 (n/a)</td><td>6.85 (n/a)</td><td>5.69 (n/a)</td><td>0.77 (n/a)</td><td>7.65 (n/a)</td><td>6.80 (n/a)</td><td>6.85 (n/a)</td><td>5.69 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>13.71 (-0.80%)</td><td>9.59 <b>(-20.24%)</b></td><td>8.46 <b>(-37.56%)</b></td><td>7.36 (-14.25%)</td><td>2.53 (+6.22%)</td><td>13.70 (-0.80%)</td><td>9.58 <b>(-20.24%)</b></td><td>8.46 <b>(-37.56%)</b></td><td>7.36 (-14.25%)</td><td>2.53 (+6.22%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>13.82 (n/a)</td><td>12.02 (n/a)</td><td>13.56 (n/a)</td><td>8.59 (n/a)</td><td>2.39 (n/a)</td><td>13.81 (n/a)</td><td>12.01 (n/a)</td><td>13.55 (n/a)</td><td>8.58 (n/a)</td><td>2.38 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.90 (n/a)</td><td>3.59 (n/a)</td><td>3.61 (n/a)</td><td>3.27 (n/a)</td><td>0.27 (n/a)</td><td>3.89 (n/a)</td><td>3.59 (n/a)</td><td>3.60 (n/a)</td><td>3.27 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>7.31 (+5.87%)</td><td>6.38 (-0.85%)</td><td>6.47 (-0.13%)</td><td>5.07 (-10.04%)</td><td>0.93 <b>(+87.70%)</b></td><td>7.31 (+5.87%)</td><td>6.38 (-0.85%)</td><td>6.46 (-0.13%)</td><td>5.06 (-10.04%)</td><td>0.93 <b>(+87.70%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>6.91 (n/a)</td><td>6.44 (n/a)</td><td>6.48 (n/a)</td><td>5.63 (n/a)</td><td>0.50 (n/a)</td><td>6.90 (n/a)</td><td>6.43 (n/a)</td><td>6.47 (n/a)</td><td>5.63 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>13.40 (-2.53%)</td><td>9.81 (-2.57%)</td><td>8.07 (-16.38%)</td><td>6.89 (-14.65%)</td><td>3.11 <b>(+37.30%)</b></td><td>13.39 (-2.53%)</td><td>9.81 (-2.57%)</td><td>8.07 (-16.38%)</td><td>6.89 (-14.65%)</td><td>3.10 <b>(+37.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>13.75 (n/a)</td><td>10.07 (n/a)</td><td>9.65 (n/a)</td><td>8.07 (n/a)</td><td>2.26 (n/a)</td><td>13.74 (n/a)</td><td>10.07 (n/a)</td><td>9.65 (n/a)</td><td>8.07 (n/a)</td><td>2.26 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.19 (+2.25%)</td><td>2.62 <b>(+33.81%)</b></td><td>2.90 <b>(+136.49%)</b></td><td>1.20 (+1.17%)</td><td>0.81 <b>(-21.83%)</b></td><td>3.18 (+2.25%)</td><td>2.61 <b>(+33.81%)</b></td><td>2.89 <b>(+136.49%)</b></td><td>1.20 (+1.17%)</td><td>0.80 <b>(-21.83%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.12 (n/a)</td><td>1.96 (n/a)</td><td>1.22 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td><td>3.11 (n/a)</td><td>1.95 (n/a)</td><td>1.22 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.57 (+3.06%)</td><td>0.49 <b>(+42.70%)</b></td><td>0.53 <b>(+53.44%)</b></td><td>0.34 <b>(+350.73%)</b></td><td>0.10 <b>(-49.39%)</b></td><td>0.56 (+3.06%)</td><td>0.48 <b>(+42.70%)</b></td><td>0.52 <b>(+53.44%)</b></td><td>0.34 <b>(+350.73%)</b></td><td>0.10 <b>(-49.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.56 (n/a)</td><td>0.34 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.55 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.70 (-9.18%)</td><td>0.38 <b>(-25.97%)</b></td><td>0.38 (-15.45%)</td><td>0.08 <b>(-72.43%)</b></td><td>0.31 <b>(+48.03%)</b></td><td>0.69 (-9.18%)</td><td>0.38 <b>(-25.97%)</b></td><td>0.37 (-15.45%)</td><td>0.08 <b>(-72.43%)</b></td><td>0.30 <b>(+48.03%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.77 (n/a)</td><td>0.52 (n/a)</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.76 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.80 (+3.01%)</td><td>1.96 <b>(+22.34%)</b></td><td>2.02 <b>(+22.71%)</b></td><td>0.78 (+3.27%)</td><td>0.77 (+5.00%)</td><td>2.76 (+3.01%)</td><td>1.93 <b>(+22.34%)</b></td><td>1.99 <b>(+22.71%)</b></td><td>0.77 (+3.27%)</td><td>0.75 (+5.00%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.72 (n/a)</td><td>1.60 (n/a)</td><td>1.65 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>2.67 (n/a)</td><td>1.57 (n/a)</td><td>1.62 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>364.02 (n/a)</td><td>333.60 (n/a)</td><td>255.60 (n/a)</td><td>105.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.20 (n/a)</td><td>397.44 (n/a)</td><td>382.80 (n/a)</td><td>268.10 (n/a)</td><td>121.89 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>508.00 (n/a)</td><td>412.84 (n/a)</td><td>402.10 (n/a)</td><td>330.40 (n/a)</td><td>64.96 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.40 (n/a)</td><td>390.32 (n/a)</td><td>303.50 (n/a)</td><td>190.00 (n/a)</td><td>216.09 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.70 (n/a)</td><td>440.26 (n/a)</td><td>420.70 (n/a)</td><td>274.10 (n/a)</td><td>170.75 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1850.40 (n/a)</td><td>727.06 (n/a)</td><td>477.40 (n/a)</td><td>260.20 (n/a)</td><td>638.79 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (+2.26%)</td><td>0.02 (-7.39%)</td><td>0.02 (+1.24%)</td><td>0.01 (-10.27%)</td><td>0.01 (+2.85%)</td><td>561.80 (+11.45%)</td><td>407.20 (+8.37%)</td><td>399.90 (-1.21%)</td><td>201.80 (-2.18%)</td><td>133.59 (+2.23%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.10 (n/a)</td><td>375.74 (n/a)</td><td>404.80 (n/a)</td><td>206.30 (n/a)</td><td>130.67 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 <b>(+25.99%)</b></td><td>0.02 (-8.51%)</td><td>0.02 <b>(-40.96%)</b></td><td>0.02 (-2.70%)</td><td>0.01 <b>(+43.78%)</b></td><td>486.40 (+2.77%)</td><td>381.80 (+15.08%)</td><td>450.50 <b>(+69.36%)</b></td><td>193.60 <b>(-20.62%)</b></td><td>130.30 <b>(+22.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.30 (n/a)</td><td>331.76 (n/a)</td><td>266.00 (n/a)</td><td>243.90 (n/a)</td><td>106.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 <b>(+49.72%)</b></td><td>0.03 (+3.41%)</td><td>0.02 (-14.29%)</td><td>0.02 (-6.64%)</td><td>0.01 <b>(+116.23%)</b></td><td>507.70 (+7.11%)</td><td>372.28 (+7.60%)</td><td>382.90 (+16.67%)</td><td>176.90 <b>(-33.22%)</b></td><td>142.43 <b>(+63.23%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.00 (n/a)</td><td>345.98 (n/a)</td><td>328.20 (n/a)</td><td>264.90 (n/a)</td><td>87.26 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (-1.32%)</td><td>0.02 (+13.85%)</td><td>0.03 <b>(+63.06%)</b></td><td>0.00 <b>(-67.03%)</b></td><td>0.01 <b>(+39.82%)</b></td><td>1925.80 <b>(+203.28%)</b></td><td>629.04 <b>(+41.59%)</b></td><td>290.80 <b>(-38.68%)</b></td><td>231.60 (+1.36%)</td><td>730.98 <b>(+340.44%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.00 (n/a)</td><td>444.28 (n/a)</td><td>474.20 (n/a)</td><td>228.50 (n/a)</td><td>165.96 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (-11.40%)</td><td>0.02 (-19.24%)</td><td>0.02 <b>(-28.13%)</b></td><td>0.01 (-14.45%)</td><td>0.01 <b>(-25.13%)</b></td><td>649.90 (+16.89%)</td><td>421.96 <b>(+20.35%)</b></td><td>375.50 <b>(+39.13%)</b></td><td>266.20 (+12.84%)</td><td>144.77 (+2.43%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>350.62 (n/a)</td><td>269.90 (n/a)</td><td>235.90 (n/a)</td><td>141.33 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (+19.83%)</td><td>0.02 (-3.47%)</td><td>0.02 <b>(-29.51%)</b></td><td>0.02 (+7.56%)</td><td>0.01 (+18.14%)</td><td>474.70 (-7.03%)</td><td>382.78 (+3.39%)</td><td>425.80 <b>(+41.89%)</b></td><td>216.10 (-16.56%)</td><td>100.49 (-16.63%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.60 (n/a)</td><td>370.22 (n/a)</td><td>300.10 (n/a)</td><td>259.00 (n/a)</td><td>120.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (+1.31%)</td><td>0.02 <b>(+45.39%)</b></td><td>0.02 <b>(+35.23%)</b></td><td>0.01 <b>(+298.27%)</b></td><td>0.01 <b>(-23.66%)</b></td><td>607.90 <b>(-74.89%)</b></td><td>397.44 <b>(-55.35%)</b></td><td>417.70 <b>(-26.06%)</b></td><td>241.80 (-1.31%)</td><td>146.17 <b>(-83.26%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2421.10 (n/a)</td><td>890.04 (n/a)</td><td>564.90 (n/a)</td><td>245.00 (n/a)</td><td>872.91 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (-16.45%)</td><td>0.02 (-19.00%)</td><td>0.02 <b>(-26.87%)</b></td><td>0.01 (-16.88%)</td><td>0.00 <b>(-25.59%)</b></td><td>598.70 <b>(+20.29%)</b></td><td>471.62 <b>(+22.30%)</b></td><td>469.60 <b>(+36.75%)</b></td><td>347.50 (+19.70%)</td><td>89.74 (+2.99%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>497.70 (n/a)</td><td>385.64 (n/a)</td><td>343.40 (n/a)</td><td>290.30 (n/a)</td><td>87.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (+16.39%)</td><td>0.03 <b>(+29.34%)</b></td><td>0.03 <b>(+52.77%)</b></td><td>0.02 (-7.03%)</td><td>0.01 (+19.42%)</td><td>539.80 (+7.55%)</td><td>315.26 <b>(-20.79%)</b></td><td>298.50 <b>(-34.54%)</b></td><td>199.80 (-14.06%)</td><td>133.41 (+11.03%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.90 (n/a)</td><td>398.00 (n/a)</td><td>456.00 (n/a)</td><td>232.50 (n/a)</td><td>120.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (-0.06%)</td><td>0.02 (-11.28%)</td><td>0.02 <b>(-36.00%)</b></td><td>0.01 <b>(-21.59%)</b></td><td>0.01 (+12.34%)</td><td>577.90 <b>(+27.54%)</b></td><td>387.26 (+16.60%)</td><td>417.90 <b>(+56.22%)</b></td><td>224.20 (+0.04%)</td><td>142.55 <b>(+29.67%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>453.10 (n/a)</td><td>332.14 (n/a)</td><td>267.50 (n/a)</td><td>224.10 (n/a)</td><td>109.94 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (+17.06%)</td><td>0.03 (+19.50%)</td><td>0.03 (+1.23%)</td><td>0.03 <b>(+52.39%)</b></td><td>0.00 <b>(-47.80%)</b></td><td>304.20 <b>(-34.38%)</b></td><td>271.34 <b>(-21.19%)</b></td><td>270.80 (-1.20%)</td><td>224.20 (-14.56%)</td><td>30.44 <b>(-71.33%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.60 (n/a)</td><td>344.30 (n/a)</td><td>274.10 (n/a)</td><td>262.40 (n/a)</td><td>106.19 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 <b>(+61.70%)</b></td><td>0.02 <b>(+42.75%)</b></td><td>0.02 (+13.60%)</td><td>0.02 <b>(+33.65%)</b></td><td>0.01 <b>(+114.05%)</b></td><td>536.80 <b>(-25.18%)</b></td><td>412.74 <b>(-24.78%)</b></td><td>494.00 (-11.97%)</td><td>229.30 <b>(-38.14%)</b></td><td>151.93 (+2.24%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>717.50 (n/a)</td><td>548.68 (n/a)</td><td>561.20 (n/a)</td><td>370.70 (n/a)</td><td>148.60 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (+3.31%)</td><td>0.02 (+8.04%)</td><td>0.02 (+3.57%)</td><td>0.02 (+15.70%)</td><td>0.01 (-14.29%)</td><td>509.30 (-13.58%)</td><td>373.48 (-11.64%)</td><td>375.50 (-3.45%)</td><td>243.10 (-3.22%)</td><td>104.02 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.30 (n/a)</td><td>422.68 (n/a)</td><td>388.90 (n/a)</td><td>251.20 (n/a)</td><td>154.65 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (-9.17%)</td><td>0.02 (+0.49%)</td><td>0.02 (+3.73%)</td><td>0.01 (-13.00%)</td><td>0.01 (-8.84%)</td><td>693.00 (+14.94%)</td><td>453.40 (+0.55%)</td><td>469.50 (-3.61%)</td><td>226.90 (+10.09%)</td><td>184.69 (+19.94%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.90 (n/a)</td><td>450.94 (n/a)</td><td>487.10 (n/a)</td><td>206.10 (n/a)</td><td>153.99 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.10 (+9.41%)</td><td>0.08 (+1.45%)</td><td>0.10 <b>(+21.47%)</b></td><td>0.05 <b>(-29.67%)</b></td><td>0.02 <b>(+201.15%)</b></td><td>504.20 <b>(+42.19%)</b></td><td>332.08 (+6.83%)</td><td>252.50 (-17.65%)</td><td>246.80 (-8.59%)</td><td>117.80 <b>(+273.44%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>354.60 (n/a)</td><td>310.86 (n/a)</td><td>306.60 (n/a)</td><td>270.00 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.16 (-7.32%)</td><td>0.12 (-19.75%)</td><td>0.10 <b>(-29.38%)</b></td><td>0.09 <b>(-25.80%)</b></td><td>0.03 <b>(+73.00%)</b></td><td>439.30 <b>(+34.75%)</b></td><td>360.62 <b>(+28.81%)</b></td><td>394.70 <b>(+41.62%)</b></td><td>257.10 (+7.89%)</td><td>79.28 <b>(+151.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>326.00 (n/a)</td><td>279.96 (n/a)</td><td>278.70 (n/a)</td><td>238.30 (n/a)</td><td>31.50 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 <b>(+54.93%)</b></td><td>0.02 <b>(+30.81%)</b></td><td>0.02 (+14.92%)</td><td>0.02 <b>(+72.30%)</b></td><td>0.00 <b>(+37.53%)</b></td><td>295.60 <b>(-41.96%)</b></td><td>265.28 <b>(-24.57%)</b></td><td>282.30 (-12.98%)</td><td>184.40 <b>(-35.46%)</b></td><td>46.17 <b>(-49.96%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.30 (n/a)</td><td>351.70 (n/a)</td><td>324.40 (n/a)</td><td>285.70 (n/a)</td><td>92.28 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (+2.75%)</td><td>0.03 (-5.14%)</td><td>0.03 (+5.26%)</td><td>0.02 (-14.46%)</td><td>0.01 <b>(+66.70%)</b></td><td>513.80 (+16.91%)</td><td>351.34 (+14.29%)</td><td>264.00 (-5.00%)</td><td>239.10 (-2.69%)</td><td>141.90 <b>(+84.53%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>439.50 (n/a)</td><td>307.42 (n/a)</td><td>277.90 (n/a)</td><td>245.70 (n/a)</td><td>76.90 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (-6.17%)</td><td>0.04 (-11.56%)</td><td>0.03 <b>(-28.09%)</b></td><td>0.03 (+5.77%)</td><td>0.01 <b>(-28.51%)</b></td><td>481.40 (-5.46%)</td><td>363.26 (+7.92%)</td><td>389.60 <b>(+39.09%)</b></td><td>249.60 (+6.58%)</td><td>90.36 <b>(-27.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.20 (n/a)</td><td>336.60 (n/a)</td><td>280.10 (n/a)</td><td>234.20 (n/a)</td><td>123.86 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (+5.51%)</td><td>0.03 (-6.88%)</td><td>0.03 (-11.24%)</td><td>0.01 (-10.54%)</td><td>0.01 (+10.63%)</td><td>631.00 (+11.78%)</td><td>335.58 (+10.47%)</td><td>276.80 (+12.66%)</td><td>211.20 (-5.21%)</td><td>171.21 (+16.92%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>303.78 (n/a)</td><td>245.70 (n/a)</td><td>222.80 (n/a)</td><td>146.44 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (-5.44%)</td><td>0.03 <b>(-24.85%)</b></td><td>0.02 <b>(-39.49%)</b></td><td>0.01 <b>(-46.09%)</b></td><td>0.01 (+19.02%)</td><td>1004.90 <b>(+85.51%)</b></td><td>499.62 <b>(+51.85%)</b></td><td>450.90 <b>(+65.23%)</b></td><td>253.70 (+5.75%)</td><td>298.41 <b>(+137.67%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>329.02 (n/a)</td><td>272.90 (n/a)</td><td>239.90 (n/a)</td><td>125.55 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (-1.86%)</td><td>0.03 <b>(+38.13%)</b></td><td>0.03 <b>(+57.79%)</b></td><td>0.02 <b>(+76.73%)</b></td><td>0.00 <b>(-49.95%)</b></td><td>350.30 <b>(-43.41%)</b></td><td>282.34 <b>(-33.31%)</b></td><td>269.00 <b>(-36.62%)</b></td><td>239.00 (+1.88%)</td><td>42.43 <b>(-69.28%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.00 (n/a)</td><td>423.38 (n/a)</td><td>424.40 (n/a)</td><td>234.60 (n/a)</td><td>138.13 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (-3.60%)</td><td>0.02 <b>(-44.51%)</b></td><td>0.02 <b>(-57.63%)</b></td><td>0.01 <b>(-49.19%)</b></td><td>0.01 <b>(+22.64%)</b></td><td>1039.40 <b>(+96.78%)</b></td><td>638.72 <b>(+105.36%)</b></td><td>576.90 <b>(+136.05%)</b></td><td>252.00 (+3.75%)</td><td>289.89 <b>(+134.77%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>311.02 (n/a)</td><td>244.40 (n/a)</td><td>242.90 (n/a)</td><td>123.48 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (+1.86%)</td><td>0.03 (+12.82%)</td><td>0.03 <b>(+24.48%)</b></td><td>0.01 <b>(+95.47%)</b></td><td>0.01 (-7.41%)</td><td>548.40 <b>(-48.83%)</b></td><td>372.46 <b>(-22.80%)</b></td><td>295.60 (-19.67%)</td><td>238.30 (-1.85%)</td><td>155.54 <b>(-54.19%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1071.80 (n/a)</td><td>482.44 (n/a)</td><td>368.00 (n/a)</td><td>242.80 (n/a)</td><td>339.52 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 <b>(-21.37%)</b></td><td>0.02 <b>(-29.14%)</b></td><td>0.02 <b>(-35.81%)</b></td><td>0.01 <b>(-37.15%)</b></td><td>0.01 (+0.22%)</td><td>747.00 <b>(+59.11%)</b></td><td>446.30 <b>(+48.25%)</b></td><td>423.60 <b>(+55.79%)</b></td><td>295.80 <b>(+27.17%)</b></td><td>182.23 <b>(+89.81%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.50 (n/a)</td><td>301.04 (n/a)</td><td>271.90 (n/a)</td><td>232.60 (n/a)</td><td>96.01 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 <b>(+22.42%)</b></td><td>0.03 (+17.53%)</td><td>0.02 <b>(+45.13%)</b></td><td>0.01 (+2.63%)</td><td>0.01 <b>(+31.52%)</b></td><td>644.70 (-2.55%)</td><td>397.06 (-10.07%)</td><td>343.30 <b>(-31.09%)</b></td><td>199.50 (-18.30%)</td><td>191.24 (+11.33%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.60 (n/a)</td><td>441.52 (n/a)</td><td>498.20 (n/a)</td><td>244.20 (n/a)</td><td>171.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (-4.81%)</td><td>0.02 <b>(-21.93%)</b></td><td>0.02 <b>(-38.84%)</b></td><td>0.02 <b>(-31.88%)</b></td><td>0.01 <b>(+94.77%)</b></td><td>554.40 <b>(+46.78%)</b></td><td>418.98 <b>(+36.21%)</b></td><td>476.20 <b>(+63.53%)</b></td><td>286.00 (+5.07%)</td><td>121.91 <b>(+183.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>377.70 (n/a)</td><td>307.60 (n/a)</td><td>291.20 (n/a)</td><td>272.20 (n/a)</td><td>43.03 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 <b>(+29.44%)</b></td><td>0.02 (+1.94%)</td><td>0.02 (-7.53%)</td><td>0.01 (-3.87%)</td><td>0.00 <b>(+92.54%)</b></td><td>636.40 (+4.04%)</td><td>504.86 (+1.00%)</td><td>496.10 (+8.15%)</td><td>339.50 <b>(-22.75%)</b></td><td>111.52 <b>(+51.67%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.70 (n/a)</td><td>499.84 (n/a)</td><td>458.70 (n/a)</td><td>439.50 (n/a)</td><td>73.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.35 <b>(-41.56%)</b></td><td>0.29 (-16.29%)</td><td>0.30 (-3.60%)</td><td>0.17 (+1.41%)</td><td>0.07 <b>(-61.40%)</b></td><td>585.00 (-1.40%)</td><td>367.44 (+1.39%)</td><td>325.20 (+3.73%)</td><td>277.90 <b>(+71.12%)</b></td><td>123.78 <b>(-33.38%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.61 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>593.30 (n/a)</td><td>362.40 (n/a)</td><td>313.50 (n/a)</td><td>162.40 (n/a)</td><td>185.80 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.40 (-0.15%)</td><td>0.28 <b>(+24.01%)</b></td><td>0.23 <b>(+29.30%)</b></td><td>0.17 <b>(+222.27%)</b></td><td>0.11 <b>(-27.85%)</b></td><td>574.90 <b>(-68.97%)</b></td><td>400.06 <b>(-46.43%)</b></td><td>434.70 <b>(-22.67%)</b></td><td>246.30 (+0.16%)</td><td>148.55 <b>(-77.52%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.15 (n/a)</td><td>1852.80 (n/a)</td><td>746.82 (n/a)</td><td>562.10 (n/a)</td><td>245.90 (n/a)</td><td>660.68 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.34 <b>(-48.34%)</b></td><td>0.20 <b>(-47.58%)</b></td><td>0.16 <b>(-50.82%)</b></td><td>0.13 <b>(-47.13%)</b></td><td>0.08 <b>(-47.95%)</b></td><td>768.00 <b>(+89.16%)</b></td><td>561.64 <b>(+91.42%)</b></td><td>611.80 <b>(+103.32%)</b></td><td>291.60 <b>(+93.50%)</b></td><td>181.02 <b>(+97.84%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.65 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>406.00 (n/a)</td><td>293.40 (n/a)</td><td>300.90 (n/a)</td><td>150.70 (n/a)</td><td>91.50 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.30 (-7.92%)</td><td>0.23 (-6.84%)</td><td>0.24 (+0.32%)</td><td>0.12 <b>(-32.22%)</b></td><td>0.07 (-2.10%)</td><td>637.30 <b>(+47.52%)</b></td><td>362.00 (+11.69%)</td><td>309.30 (-0.32%)</td><td>249.00 (+8.59%)</td><td>156.01 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>432.00 (n/a)</td><td>324.10 (n/a)</td><td>310.30 (n/a)</td><td>229.30 (n/a)</td><td>91.35 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.31 (+16.67%)</td><td>0.30 <b>(+65.68%)</b></td><td>0.31 <b>(+79.84%)</b></td><td>0.26 <b>(+90.95%)</b></td><td>0.02 <b>(-58.80%)</b></td><td>286.20 <b>(-47.62%)</b></td><td>249.80 <b>(-43.00%)</b></td><td>241.30 <b>(-44.39%)</b></td><td>237.40 (-14.30%)</td><td>20.58 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>546.40 (n/a)</td><td>438.26 (n/a)</td><td>433.90 (n/a)</td><td>277.00 (n/a)</td><td>112.53 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.29 (-16.87%)</td><td>0.16 <b>(-25.58%)</b></td><td>0.14 (-6.27%)</td><td>0.10 <b>(-28.06%)</b></td><td>0.07 <b>(-22.17%)</b></td><td>722.40 <b>(+39.00%)</b></td><td>521.32 <b>(+32.36%)</b></td><td>518.20 (+6.69%)</td><td>257.20 <b>(+20.30%)</b></td><td>170.12 (+17.32%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>519.70 (n/a)</td><td>393.86 (n/a)</td><td>485.70 (n/a)</td><td>213.80 (n/a)</td><td>145.00 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.27 <b>(-43.73%)</b></td><td>0.25 <b>(-23.33%)</b></td><td>0.25 (-11.24%)</td><td>0.21 (-6.96%)</td><td>0.02 <b>(-79.36%)</b></td><td>619.30 (+7.48%)</td><td>535.76 <b>(+20.93%)</b></td><td>533.80 (+12.66%)</td><td>478.70 <b>(+77.69%)</b></td><td>51.90 <b>(-60.49%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>576.20 (n/a)</td><td>443.04 (n/a)</td><td>473.80 (n/a)</td><td>269.40 (n/a)</td><td>131.34 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.42 (-1.98%)</td><td>0.31 (+6.26%)</td><td>0.27 (+4.18%)</td><td>0.21 (-8.20%)</td><td>0.09 (+16.28%)</td><td>611.60 (+8.92%)</td><td>457.14 (-3.63%)</td><td>477.10 (-4.00%)</td><td>310.60 (+2.00%)</td><td>133.00 <b>(+28.96%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.43 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>561.50 (n/a)</td><td>474.36 (n/a)</td><td>497.00 (n/a)</td><td>304.50 (n/a)</td><td>103.14 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.40 (-17.74%)</td><td>0.27 (-5.98%)</td><td>0.24 (-6.80%)</td><td>0.20 (+11.85%)</td><td>0.08 <b>(-34.29%)</b></td><td>652.60 (-10.60%)</td><td>512.28 (+0.94%)</td><td>547.90 (+7.31%)</td><td>329.10 <b>(+21.57%)</b></td><td>120.10 <b>(-27.55%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.48 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>730.00 (n/a)</td><td>507.52 (n/a)</td><td>510.60 (n/a)</td><td>270.70 (n/a)</td><td>165.77 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (-3.22%)</td><td>0.01 (-14.37%)</td><td>0.01 (-16.24%)</td><td>0.01 (-8.83%)</td><td>0.00 (+2.86%)</td><td>585.50 (+9.69%)</td><td>363.24 (+18.10%)</td><td>313.80 (+19.36%)</td><td>201.00 (+3.34%)</td><td>144.46 (+9.71%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.80 (n/a)</td><td>307.58 (n/a)</td><td>262.90 (n/a)</td><td>194.50 (n/a)</td><td>131.67 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.01 (-3.21%)</td><td>0.01 <b>(-28.12%)</b></td><td>0.01 (-7.36%)</td><td>0.00 <b>(-78.38%)</b></td><td>0.01 <b>(+171.52%)</b></td><td>1992.10 <b>(+362.63%)</b></td><td>965.14 <b>(+178.17%)</b></td><td>335.10 (+7.96%)</td><td>290.60 (+3.31%)</td><td>894.58 <b>(+1224.20%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>430.60 (n/a)</td><td>346.96 (n/a)</td><td>310.40 (n/a)</td><td>281.30 (n/a)</td><td>67.56 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (+1.23%)</td><td>0.01 (+1.22%)</td><td>0.01 (-2.53%)</td><td>0.01 (-0.58%)</td><td>0.00 (+9.64%)</td><td>511.20 (+0.57%)</td><td>364.90 (-0.23%)</td><td>318.50 (+2.61%)</td><td>266.20 (-1.22%)</td><td>108.79 (+7.26%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.30 (n/a)</td><td>365.74 (n/a)</td><td>310.40 (n/a)</td><td>269.50 (n/a)</td><td>101.43 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.76 <b>(+62.47%)</b></td><td>0.43 (+17.55%)</td><td>0.35 (-19.11%)</td><td>0.32 <b>(+30.99%)</b></td><td>0.19 <b>(+68.90%)</b></td><td>410.30 <b>(-23.65%)</b></td><td>336.68 (-13.22%)</td><td>381.30 <b>(+23.64%)</b></td><td>173.40 <b>(-38.45%)</b></td><td>96.52 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.47 (n/a)</td><td>0.37 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>537.40 (n/a)</td><td>387.96 (n/a)</td><td>308.40 (n/a)</td><td>281.70 (n/a)</td><td>128.49 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.30 <b>(-33.41%)</b></td><td>0.26 <b>(-27.60%)</b></td><td>0.28 (-19.42%)</td><td>0.21 (-17.98%)</td><td>0.04 <b>(-54.53%)</b></td><td>635.80 <b>(+21.92%)</b></td><td>514.72 <b>(+34.35%)</b></td><td>475.70 <b>(+24.11%)</b></td><td>436.10 <b>(+50.17%)</b></td><td>81.00 (-13.91%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>521.50 (n/a)</td><td>383.12 (n/a)</td><td>383.30 (n/a)</td><td>290.40 (n/a)</td><td>94.09 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.54 <b>(+29.16%)</b></td><td>0.41 <b>(+27.71%)</b></td><td>0.44 <b>(+49.09%)</b></td><td>0.27 (+7.58%)</td><td>0.13 <b>(+80.25%)</b></td><td>495.00 (-7.06%)</td><td>353.88 (-17.57%)</td><td>299.80 <b>(-32.93%)</b></td><td>244.50 <b>(-22.58%)</b></td><td>120.88 <b>(+33.50%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>532.60 (n/a)</td><td>429.32 (n/a)</td><td>447.00 (n/a)</td><td>315.80 (n/a)</td><td>90.54 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.45 (-9.74%)</td><td>0.35 (-0.11%)</td><td>0.32 (-12.32%)</td><td>0.25 <b>(+30.69%)</b></td><td>0.09 <b>(-31.24%)</b></td><td>523.00 <b>(-23.49%)</b></td><td>400.76 (-6.90%)</td><td>419.10 (+14.04%)</td><td>294.20 (+10.81%)</td><td>98.12 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>683.60 (n/a)</td><td>430.44 (n/a)</td><td>367.50 (n/a)</td><td>265.50 (n/a)</td><td>174.76 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.54 (+19.18%)</td><td>0.36 <b>(+22.41%)</b></td><td>0.36 <b>(+20.73%)</b></td><td>0.06 (-11.27%)</td><td>0.19 (+15.17%)</td><td>2058.70 (+12.70%)</td><td>669.04 (-5.50%)</td><td>369.40 (-17.17%)</td><td>244.80 (-16.08%)</td><td>779.78 <b>(+21.03%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1826.70 (n/a)</td><td>707.96 (n/a)</td><td>446.00 (n/a)</td><td>291.70 (n/a)</td><td>644.26 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.01 (-17.35%)</td><td>0.01 <b>(-23.30%)</b></td><td>0.01 <b>(-23.21%)</b></td><td>0.01 <b>(-24.37%)</b></td><td>0.00 <b>(-20.18%)</b></td><td>786.30 <b>(+32.22%)</b></td><td>532.84 <b>(+29.78%)</b></td><td>525.10 <b>(+30.23%)</b></td><td>285.20 <b>(+21.00%)</b></td><td>188.37 <b>(+23.46%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.70 (n/a)</td><td>410.58 (n/a)</td><td>403.20 (n/a)</td><td>235.70 (n/a)</td><td>152.58 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (-10.24%)</td><td>0.01 <b>(-22.04%)</b></td><td>0.01 <b>(-42.41%)</b></td><td>0.01 (+3.17%)</td><td>0.00 (-16.61%)</td><td>456.10 (-3.08%)</td><td>373.56 <b>(+26.13%)</b></td><td>426.00 <b>(+73.66%)</b></td><td>264.60 (+11.41%)</td><td>87.59 (-11.69%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>470.60 (n/a)</td><td>296.18 (n/a)</td><td>245.30 (n/a)</td><td>237.50 (n/a)</td><td>99.18 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.00 (+14.29%)</td><td>0.00 (-7.14%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+46.27%)</b></td><td>22605.29 <b>(+29.91%)</b></td><td>12124.46 <b>(+39.07%)</b></td><td>6613.74 (-8.20%)</td><td>5251.52 (-7.95%)</td><td>8799.81 <b>(+79.11%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17400.17 (n/a)</td><td>8718.18 (n/a)</td><td>7204.74 (n/a)</td><td>5704.79 (n/a)</td><td>4913.16 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.00 <b>(-21.43%)</b></td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.77%)</b></td><td>20695.92 (-8.97%)</td><td>14077.66 (+6.73%)</td><td>14201.12 (-0.59%)</td><td>7511.46 <b>(+28.86%)</b></td><td>6273.39 (-12.77%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22735.50 (n/a)</td><td>13190.16 (n/a)</td><td>14285.05 (n/a)</td><td>5829.19 (n/a)</td><td>7191.58 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.14 (-3.91%)</td><td>0.09 (-6.57%)</td><td>0.08 (-9.16%)</td><td>0.07 (+0.69%)</td><td>0.03 (-0.84%)</td><td>28709.91 (-0.77%)</td><td>24899.92 (+7.31%)</td><td>26451.07 (+10.14%)</td><td>15504.10 (+4.13%)</td><td>5368.16 (+4.81%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28931.51 (n/a)</td><td>23203.46 (n/a)</td><td>24016.78 (n/a)</td><td>14889.54 (n/a)</td><td>5121.87 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.65 (-9.10%)</td><td>1.41 (+12.41%)</td><td>1.56 (-0.79%)</td><td>1.04 <b>(+262.92%)</b></td><td>0.27 <b>(-56.76%)</b></td><td>503.80 <b>(-72.45%)</b></td><td>383.98 <b>(-42.14%)</b></td><td>335.50 (+0.81%)</td><td>318.60 (+10.01%)</td><td>82.44 <b>(-87.50%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.81 (n/a)</td><td>1.26 (n/a)</td><td>1.58 (n/a)</td><td>0.29 (n/a)</td><td>0.63 (n/a)</td><td>1828.50 (n/a)</td><td>663.60 (n/a)</td><td>332.80 (n/a)</td><td>289.60 (n/a)</td><td>659.48 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.14 <b>(+36.27%)</b></td><td>2.12 <b>(+52.55%)</b></td><td>2.20 <b>(+72.06%)</b></td><td>1.15 <b>(+281.41%)</b></td><td>0.75 (+0.87%)</td><td>915.30 <b>(-73.78%)</b></td><td>554.44 <b>(-55.07%)</b></td><td>476.80 <b>(-41.87%)</b></td><td>334.00 <b>(-26.63%)</b></td><td>225.50 <b>(-82.26%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.30 (n/a)</td><td>1.39 (n/a)</td><td>1.28 (n/a)</td><td>0.30 (n/a)</td><td>0.75 (n/a)</td><td>3490.90 (n/a)</td><td>1234.12 (n/a)</td><td>820.30 (n/a)</td><td>455.20 (n/a)</td><td>1271.46 (n/a)</td>
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
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.74 <b>(+54.60%)</b></td><td>1.07 (+13.02%)</td><td>0.93 (-2.11%)</td><td>0.47 <b>(-38.92%)</b></td><td>0.51 <b>(+260.42%)</b></td><td>1105.20 <b>(+63.71%)</b></td><td>601.98 (+6.91%)</td><td>565.70 (+2.17%)</td><td>301.00 <b>(-35.31%)</b></td><td>318.68 <b>(+274.75%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.13 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.78 (n/a)</td><td>0.14 (n/a)</td><td>675.10 (n/a)</td><td>563.08 (n/a)</td><td>553.70 (n/a)</td><td>465.30 (n/a)</td><td>85.04 (n/a)</td>
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
