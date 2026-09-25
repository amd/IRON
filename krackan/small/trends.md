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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (-3.84%)</td><td>0.06 (-18.46%)</td><td>0.06 <b>(-26.36%)</b></td><td>0.03 <b>(-40.14%)</b></td><td>0.03 <b>(+33.89%)</b></td><td>369.80 <b>(+67.03%)</b></td><td>220.76 <b>(+34.58%)</b></td><td>219.00 <b>(+35.86%)</b></td><td>126.50 (+3.94%)</td><td>96.24 <b>(+132.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>164.04 (n/a)</td><td>161.20 (n/a)</td><td>121.70 (n/a)</td><td>41.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (+1.78%)</td><td>0.08 (+4.25%)</td><td>0.07 (+7.85%)</td><td>0.06 (-4.46%)</td><td>0.02 (+15.13%)</td><td>213.00 (+4.67%)</td><td>166.38 (-3.27%)</td><td>169.00 (-7.30%)</td><td>129.00 (-1.75%)</td><td>33.76 (+17.84%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>172.00 (n/a)</td><td>182.30 (n/a)</td><td>131.30 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (-0.69%)</td><td>0.08 (+19.01%)</td><td>0.08 (+19.73%)</td><td>0.07 <b>(+41.94%)</b></td><td>0.01 <b>(-38.10%)</b></td><td>181.00 <b>(-29.57%)</b></td><td>157.64 (-19.56%)</td><td>161.00 (-16.49%)</td><td>122.30 (+0.74%)</td><td>22.15 <b>(-55.06%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>257.00 (n/a)</td><td>195.98 (n/a)</td><td>192.80 (n/a)</td><td>121.40 (n/a)</td><td>49.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.09 (+12.07%)</td><td>0.07 (+5.30%)</td><td>0.06 (-13.93%)</td><td>0.05 <b>(+24.96%)</b></td><td>0.02 (+0.32%)</td><td>229.60 (-19.97%)</td><td>192.00 (-6.41%)</td><td>208.50 (+16.22%)</td><td>135.70 (-10.72%)</td><td>37.53 <b>(-30.49%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>286.90 (n/a)</td><td>205.16 (n/a)</td><td>179.40 (n/a)</td><td>152.00 (n/a)</td><td>53.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (+10.02%)</td><td>0.03 (+13.18%)</td><td>0.03 (+18.72%)</td><td>0.03 (+17.70%)</td><td>0.00 (-12.53%)</td><td>173.60 (-15.03%)</td><td>155.94 (-12.47%)</td><td>163.10 (-15.75%)</td><td>124.80 (-9.10%)</td><td>18.69 <b>(-34.26%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>178.16 (n/a)</td><td>193.60 (n/a)</td><td>137.30 (n/a)</td><td>28.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (-10.80%)</td><td>0.03 (-7.37%)</td><td>0.03 <b>(+20.13%)</b></td><td>0.02 <b>(-36.08%)</b></td><td>0.01 <b>(+36.18%)</b></td><td>324.80 <b>(+56.45%)</b></td><td>210.18 (+13.84%)</td><td>167.50 (-16.79%)</td><td>154.20 (+12.15%)</td><td>71.98 <b>(+134.16%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>184.62 (n/a)</td><td>201.30 (n/a)</td><td>137.50 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (+1.65%)</td><td>0.03 (+8.81%)</td><td>0.03 <b>(+21.58%)</b></td><td>0.02 (+6.49%)</td><td>0.01 (-5.12%)</td><td>222.80 (-6.11%)</td><td>164.82 (-8.94%)</td><td>162.40 (-17.73%)</td><td>126.50 (-1.63%)</td><td>40.20 (-12.38%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>181.00 (n/a)</td><td>197.40 (n/a)</td><td>128.60 (n/a)</td><td>45.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (+12.59%)</td><td>0.03 (+7.70%)</td><td>0.03 (+14.92%)</td><td>0.02 (+13.11%)</td><td>0.01 (-4.42%)</td><td>215.50 (-11.57%)</td><td>180.72 (-7.91%)</td><td>178.40 (-12.98%)</td><td>138.10 (-11.19%)</td><td>28.70 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>196.24 (n/a)</td><td>205.00 (n/a)</td><td>155.50 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 <b>(-23.05%)</b></td><td>0.03 (-4.41%)</td><td>0.03 (+0.39%)</td><td>0.02 (+17.30%)</td><td>0.00 <b>(-59.54%)</b></td><td>214.60 (-14.77%)</td><td>187.80 (-1.76%)</td><td>183.60 (-0.38%)</td><td>156.50 <b>(+29.98%)</b></td><td>25.01 <b>(-56.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.80 (n/a)</td><td>191.16 (n/a)</td><td>184.30 (n/a)</td><td>120.40 (n/a)</td><td>56.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (+10.00%)</td><td>0.03 <b>(+33.46%)</b></td><td>0.03 <b>(+43.36%)</b></td><td>0.02 <b>(+44.48%)</b></td><td>0.00 <b>(-29.44%)</b></td><td>221.60 <b>(-30.79%)</b></td><td>183.84 <b>(-28.21%)</b></td><td>189.10 <b>(-30.22%)</b></td><td>145.80 (-9.10%)</td><td>28.73 <b>(-55.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>320.20 (n/a)</td><td>256.08 (n/a)</td><td>271.00 (n/a)</td><td>160.40 (n/a)</td><td>65.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (-7.39%)</td><td>0.03 (-2.85%)</td><td>0.03 (+4.46%)</td><td>0.02 (-7.64%)</td><td>0.00 (-11.15%)</td><td>270.00 (+8.26%)</td><td>209.90 (+2.81%)</td><td>200.20 (-4.26%)</td><td>166.50 (+7.98%)</td><td>38.00 (+7.52%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.40 (n/a)</td><td>204.16 (n/a)</td><td>209.10 (n/a)</td><td>154.20 (n/a)</td><td>35.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (-4.35%)</td><td>0.03 (+14.11%)</td><td>0.03 <b>(+26.99%)</b></td><td>0.02 (+17.25%)</td><td>0.00 <b>(-42.34%)</b></td><td>232.70 (-14.70%)</td><td>205.84 (-14.73%)</td><td>207.50 <b>(-21.28%)</b></td><td>169.00 (+4.51%)</td><td>23.96 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>272.80 (n/a)</td><td>241.40 (n/a)</td><td>263.60 (n/a)</td><td>161.70 (n/a)</td><td>46.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>165.58 (n/a)</td><td>176.00 (n/a)</td><td>118.50 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>168.22 (n/a)</td><td>169.00 (n/a)</td><td>135.10 (n/a)</td><td>29.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>172.66 (n/a)</td><td>181.70 (n/a)</td><td>143.10 (n/a)</td><td>23.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>262.50 (n/a)</td><td>215.66 (n/a)</td><td>222.60 (n/a)</td><td>164.20 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>201.90 (n/a)</td><td>152.54 (n/a)</td><td>145.20 (n/a)</td><td>110.60 (n/a)</td><td>33.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.40 (n/a)</td><td>163.24 (n/a)</td><td>170.40 (n/a)</td><td>129.00 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>179.98 (n/a)</td><td>176.30 (n/a)</td><td>154.90 (n/a)</td><td>26.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>242.00 (n/a)</td><td>220.66 (n/a)</td><td>218.20 (n/a)</td><td>196.70 (n/a)</td><td>16.79 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_gate_up_interleaved_blob[iter0]

_No metrics available._


### test_gate_up_interleaved_blob[iter1]

_No metrics available._


### test_gate_up_interleaved_blob[iter2]

_No metrics available._


### test_gate_up_interleaved_blob[iter3]

_No metrics available._


### test_gate_up_interleaved_blob[iter4]

_No metrics available._


### test_large_k_shapes[K_4096-N_1536]

_No metrics available._


### test_large_k_shapes[K_6144-N_1536]

_No metrics available._


### test_matches_reference[K_1024-N_128]

_No metrics available._


### test_matches_reference[K_1024-N_512]

_No metrics available._


### test_matches_reference[K_1536-N_640]

_No metrics available._


### test_matches_reference[K_2048-N_256]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter0]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter1]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter2]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter3]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter4]

_No metrics available._


### test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n]

_No metrics available._


</details>


<details>
<summary>iron/operators/flm/gemm</summary>


### test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]

_No metrics available._


### test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]

_No metrics available._


### test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.79 (-11.08%)</td><td>3.15 (-7.27%)</td><td>3.02 (-2.36%)</td><td>2.60 (-5.92%)</td><td>0.44 <b>(-30.74%)</b></td><td>530.20 (+6.30%)</td><td>444.20 (+6.61%)</td><td>455.80 (+2.40%)</td><td>363.00 (+12.45%)</td><td>61.42 (-16.82%)</td><td>739.59 (-11.08%)</td><td>613.74 (-7.27%)</td><td>588.87 (-2.36%)</td><td>506.27 (-5.92%)</td><td>86.16 <b>(-30.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.26 (n/a)</td><td>3.39 (n/a)</td><td>3.09 (n/a)</td><td>2.76 (n/a)</td><td>0.64 (n/a)</td><td>498.80 (n/a)</td><td>416.66 (n/a)</td><td>445.10 (n/a)</td><td>322.80 (n/a)</td><td>73.84 (n/a)</td><td>831.70 (n/a)</td><td>661.83 (n/a)</td><td>603.10 (n/a)</td><td>538.14 (n/a)</td><td>124.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.06 (+2.18%)</td><td>4.47 (-0.21%)</td><td>3.77 (-3.08%)</td><td>3.63 (+1.71%)</td><td>1.12 (+2.05%)</td><td>378.70 (-1.69%)</td><td>322.08 (+0.31%)</td><td>364.80 (+3.20%)</td><td>227.20 (-2.11%)</td><td>72.32 (+0.10%)</td><td>1181.74 (+2.18%)</td><td>872.62 (-0.21%)</td><td>735.90 (-3.08%)</td><td>708.81 (+1.71%)</td><td>218.98 (+2.05%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>5.93 (n/a)</td><td>4.48 (n/a)</td><td>3.89 (n/a)</td><td>3.57 (n/a)</td><td>1.10 (n/a)</td><td>385.20 (n/a)</td><td>321.10 (n/a)</td><td>353.50 (n/a)</td><td>232.10 (n/a)</td><td>72.25 (n/a)</td><td>1156.54 (n/a)</td><td>874.49 (n/a)</td><td>759.32 (n/a)</td><td>696.87 (n/a)</td><td>214.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.82 (-15.24%)</td><td>4.75 (+6.04%)</td><td>4.27 (+19.50%)</td><td>3.60 (+6.98%)</td><td>1.32 <b>(-34.50%)</b></td><td>382.50 (-6.52%)</td><td>306.06 (-10.74%)</td><td>322.00 (-16.32%)</td><td>201.90 (+18.00%)</td><td>73.87 <b>(-25.93%)</b></td><td>1329.45 (-15.24%)</td><td>925.86 (+6.04%)</td><td>833.64 (+19.50%)</td><td>701.72 (+6.98%)</td><td>256.87 <b>(-34.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>8.04 (n/a)</td><td>4.48 (n/a)</td><td>3.58 (n/a)</td><td>3.36 (n/a)</td><td>2.01 (n/a)</td><td>409.20 (n/a)</td><td>342.90 (n/a)</td><td>384.80 (n/a)</td><td>171.10 (n/a)</td><td>99.74 (n/a)</td><td>1568.56 (n/a)</td><td>873.13 (n/a)</td><td>697.61 (n/a)</td><td>655.94 (n/a)</td><td>392.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.31 (-0.23%)</td><td>5.10 (+18.03%)</td><td>5.47 <b>(+43.97%)</b></td><td>3.71 (-1.36%)</td><td>1.17 (+4.29%)</td><td>371.20 (+1.39%)</td><td>282.28 (-14.85%)</td><td>251.60 <b>(-30.54%)</b></td><td>218.10 (+0.23%)</td><td>69.20 (+8.14%)</td><td>1230.88 (-0.23%)</td><td>995.50 (+18.03%)</td><td>1067.05 <b>(+43.97%)</b></td><td>723.14 (-1.36%)</td><td>227.98 (+4.29%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.33 (n/a)</td><td>4.32 (n/a)</td><td>3.80 (n/a)</td><td>3.76 (n/a)</td><td>1.12 (n/a)</td><td>366.10 (n/a)</td><td>331.52 (n/a)</td><td>362.20 (n/a)</td><td>217.60 (n/a)</td><td>64.00 (n/a)</td><td>1233.77 (n/a)</td><td>843.47 (n/a)</td><td>741.15 (n/a)</td><td>733.14 (n/a)</td><td>218.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>4.61 <b>(-27.40%)</b></td><td>3.47 (-8.59%)</td><td>3.22 (+2.43%)</td><td>3.07 (+0.85%)</td><td>0.64 <b>(-54.97%)</b></td><td>448.90 (-0.86%)</td><td>405.96 (+3.38%)</td><td>427.20 (-2.38%)</td><td>298.70 <b>(+37.71%)</b></td><td>61.38 <b>(-38.15%)</b></td><td>898.56 <b>(-27.40%)</b></td><td>676.39 (-8.59%)</td><td>628.38 (+2.43%)</td><td>597.95 (+0.85%)</td><td>125.65 <b>(-54.97%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.35 (n/a)</td><td>3.79 (n/a)</td><td>3.15 (n/a)</td><td>3.04 (n/a)</td><td>1.43 (n/a)</td><td>452.80 (n/a)</td><td>392.68 (n/a)</td><td>437.60 (n/a)</td><td>216.90 (n/a)</td><td>99.25 (n/a)</td><td>1237.75 (n/a)</td><td>739.94 (n/a)</td><td>613.46 (n/a)</td><td>592.89 (n/a)</td><td>279.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.95 (-16.05%)</td><td>1.64 <b>(+24.01%)</b></td><td>1.68 <b>(+51.70%)</b></td><td>1.05 (+2.92%)</td><td>0.35 <b>(-37.82%)</b></td><td>381.60 (-2.83%)</td><td>257.06 <b>(-23.21%)</b></td><td>239.60 <b>(-34.09%)</b></td><td>206.20 (+19.12%)</td><td>71.13 <b>(-22.10%)</b></td><td>162.77 (-16.05%)</td><td>136.91 <b>(+24.01%)</b></td><td>140.02 <b>(+51.70%)</b></td><td>87.93 (+2.92%)</td><td>29.08 <b>(-37.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>2.32 (n/a)</td><td>1.32 (n/a)</td><td>1.10 (n/a)</td><td>1.02 (n/a)</td><td>0.56 (n/a)</td><td>392.70 (n/a)</td><td>334.76 (n/a)</td><td>363.50 (n/a)</td><td>173.10 (n/a)</td><td>91.30 (n/a)</td><td>193.88 (n/a)</td><td>110.41 (n/a)</td><td>92.30 (n/a)</td><td>85.44 (n/a)</td><td>46.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.67 <b>(-27.66%)</b></td><td>5.20 (-15.17%)</td><td>4.91 (+0.51%)</td><td>4.61 (-2.58%)</td><td>0.84 <b>(-57.38%)</b></td><td>419.00 (+2.65%)</td><td>378.00 (+11.92%)</td><td>393.90 (-0.51%)</td><td>289.90 <b>(+38.25%)</b></td><td>51.23 <b>(-42.83%)</b></td><td>1389.03 <b>(-27.66%)</b></td><td>1084.04 (-15.17%)</td><td>1022.22 (+0.51%)</td><td>960.90 (-2.58%)</td><td>174.18 <b>(-57.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>9.22 (n/a)</td><td>6.14 (n/a)</td><td>4.88 (n/a)</td><td>4.74 (n/a)</td><td>1.96 (n/a)</td><td>408.20 (n/a)</td><td>337.74 (n/a)</td><td>395.90 (n/a)</td><td>209.70 (n/a)</td><td>89.61 (n/a)</td><td>1920.15 (n/a)</td><td>1277.92 (n/a)</td><td>1017.02 (n/a)</td><td>986.32 (n/a)</td><td>408.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>15.49 (+6.79%)</td><td>11.30 (-4.19%)</td><td>10.74 (-4.61%)</td><td>5.81 <b>(-40.63%)</b></td><td>3.94 <b>(+125.07%)</b></td><td>947.20 <b>(+68.42%)</b></td><td>550.86 (+16.08%)</td><td>512.40 (+4.85%)</td><td>355.40 (-6.35%)</td><td>238.90 <b>(+256.77%)</b></td><td>6043.17 (+6.79%)</td><td>4408.53 (-4.19%)</td><td>4191.31 (-4.61%)</td><td>2267.11 <b>(-40.63%)</b></td><td>1537.77 <b>(+125.07%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>14.51 (n/a)</td><td>11.80 (n/a)</td><td>11.26 (n/a)</td><td>9.79 (n/a)</td><td>1.75 (n/a)</td><td>562.40 (n/a)</td><td>474.56 (n/a)</td><td>488.70 (n/a)</td><td>379.50 (n/a)</td><td>66.96 (n/a)</td><td>5659.00 (n/a)</td><td>4601.52 (n/a)</td><td>4394.01 (n/a)</td><td>3818.37 (n/a)</td><td>683.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>370.70 (n/a)</td><td>222.32 (n/a)</td><td>171.60 (n/a)</td><td>131.60 (n/a)</td><td>97.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>168.30 (n/a)</td><td>167.00 (n/a)</td><td>145.70 (n/a)</td><td>25.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>252.40 (n/a)</td><td>174.42 (n/a)</td><td>171.00 (n/a)</td><td>111.50 (n/a)</td><td>53.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.80 (n/a)</td><td>201.74 (n/a)</td><td>204.90 (n/a)</td><td>176.60 (n/a)</td><td>20.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>193.72 (n/a)</td><td>205.20 (n/a)</td><td>126.60 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>293.00 (n/a)</td><td>232.82 (n/a)</td><td>215.30 (n/a)</td><td>207.50 (n/a)</td><td>35.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.20 (n/a)</td><td>191.16 (n/a)</td><td>163.20 (n/a)</td><td>142.50 (n/a)</td><td>52.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.80 (n/a)</td><td>216.82 (n/a)</td><td>211.80 (n/a)</td><td>149.30 (n/a)</td><td>47.77 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>5.00 (+2.79%)</td><td>4.35 (+2.56%)</td><td>4.10 (-2.58%)</td><td>3.71 (-1.82%)</td><td>0.55 <b>(+39.42%)</b></td><td>2532.80 (+1.85%)</td><td>2189.34 (-1.92%)</td><td>2292.60 (+2.66%)</td><td>1881.40 (-2.71%)</td><td>271.54 <b>(+37.49%)</b></td><td>1966.33 (+2.79%)</td><td>1710.96 (+2.56%)</td><td>1613.64 (-2.58%)</td><td>1460.58 (-1.82%)</td><td>214.56 <b>(+39.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.86 (n/a)</td><td>4.24 (n/a)</td><td>4.21 (n/a)</td><td>3.78 (n/a)</td><td>0.39 (n/a)</td><td>2486.80 (n/a)</td><td>2232.14 (n/a)</td><td>2233.30 (n/a)</td><td>1933.90 (n/a)</td><td>197.50 (n/a)</td><td>1912.94 (n/a)</td><td>1668.18 (n/a)</td><td>1656.45 (n/a)</td><td>1487.61 (n/a)</td><td>153.89 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.28 <b>(+23.85%)</b></td><td>0.96 (+3.46%)</td><td>0.98 (-1.08%)</td><td>0.72 (+6.29%)</td><td>0.22 <b>(+50.64%)</b></td><td>308.10 (-5.89%)</td><td>240.06 (-1.79%)</td><td>225.70 (+1.07%)</td><td>173.20 (-19.25%)</td><td>52.83 (+12.53%)</td><td>54.48 <b>(+23.85%)</b></td><td>40.92 (+3.46%)</td><td>41.81 (-1.08%)</td><td>30.63 (+6.29%)</td><td>9.26 <b>(+50.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.03 (n/a)</td><td>0.93 (n/a)</td><td>0.99 (n/a)</td><td>0.68 (n/a)</td><td>0.14 (n/a)</td><td>327.40 (n/a)</td><td>244.44 (n/a)</td><td>223.30 (n/a)</td><td>214.50 (n/a)</td><td>46.95 (n/a)</td><td>43.99 (n/a)</td><td>39.55 (n/a)</td><td>42.27 (n/a)</td><td>28.82 (n/a)</td><td>6.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.10 (-4.86%)</td><td>0.90 (-12.53%)</td><td>0.93 (-9.54%)</td><td>0.70 <b>(-21.69%)</b></td><td>0.18 <b>(+88.93%)</b></td><td>315.70 <b>(+27.71%)</b></td><td>253.56 (+17.42%)</td><td>236.90 (+10.55%)</td><td>200.40 (+5.09%)</td><td>52.76 <b>(+156.13%)</b></td><td>47.08 (-4.86%)</td><td>38.50 (-12.53%)</td><td>39.83 (-9.54%)</td><td>29.89 <b>(-21.69%)</b></td><td>7.75 <b>(+88.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.16 (n/a)</td><td>1.03 (n/a)</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.10 (n/a)</td><td>247.20 (n/a)</td><td>215.94 (n/a)</td><td>214.30 (n/a)</td><td>190.70 (n/a)</td><td>20.60 (n/a)</td><td>49.49 (n/a)</td><td>44.01 (n/a)</td><td>44.03 (n/a)</td><td>38.17 (n/a)</td><td>4.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.53 (+0.02%)</td><td>0.53 (-0.06%)</td><td>0.53 (-0.21%)</td><td>0.53 (+0.04%)</td><td>0.00 (-12.69%)</td><td>47888.70 (-0.04%)</td><td>47849.60 (+0.06%)</td><td>47883.30 (+0.21%)</td><td>47769.10 (-0.02%)</td><td>52.45 (-12.63%)</td><td>359.64 (+0.02%)</td><td>359.04 (-0.06%)</td><td>358.79 (-0.21%)</td><td>358.75 (+0.04%)</td><td>0.39 (-12.69%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47908.80 (n/a)</td><td>47822.90 (n/a)</td><td>47783.90 (n/a)</td><td>47777.10 (n/a)</td><td>60.04 (n/a)</td><td>359.58 (n/a)</td><td>359.24 (n/a)</td><td>359.53 (n/a)</td><td>358.59 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.91 (-0.20%)</td><td>0.90 (+0.03%)</td><td>0.91 (-0.07%)</td><td>0.90 (+0.80%)</td><td>0.00 <b>(-66.71%)</b></td><td>27896.10 (-0.79%)</td><td>27827.30 (-0.04%)</td><td>27797.90 (+0.07%)</td><td>27784.10 (+0.20%)</td><td>52.68 <b>(-66.96%)</b></td><td>618.34 (-0.20%)</td><td>617.38 (+0.03%)</td><td>618.03 (-0.07%)</td><td>615.85 (+0.80%)</td><td>1.17 <b>(-66.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28118.80 (n/a)</td><td>27837.24 (n/a)</td><td>27779.70 (n/a)</td><td>27728.30 (n/a)</td><td>159.43 (n/a)</td><td>619.58 (n/a)</td><td>617.17 (n/a)</td><td>618.43 (n/a)</td><td>610.98 (n/a)</td><td>3.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.18 (-4.70%)</td><td>3.16 (-1.42%)</td><td>3.15 (-0.99%)</td><td>3.14 (+0.10%)</td><td>0.02 <b>(-79.26%)</b></td><td>8025.30 (-0.10%)</td><td>7972.12 (+1.39%)</td><td>7976.80 (+1.00%)</td><td>7910.80 (+4.93%)</td><td>42.26 <b>(-78.20%)</b></td><td>2171.70 (-4.70%)</td><td>2155.04 (-1.42%)</td><td>2153.72 (-0.99%)</td><td>2140.70 (+0.10%)</td><td>11.44 <b>(-79.26%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>3.34 (n/a)</td><td>3.20 (n/a)</td><td>3.19 (n/a)</td><td>3.13 (n/a)</td><td>0.08 (n/a)</td><td>8033.60 (n/a)</td><td>7862.90 (n/a)</td><td>7898.10 (n/a)</td><td>7538.80 (n/a)</td><td>193.87 (n/a)</td><td>2278.87 (n/a)</td><td>2186.02 (n/a)</td><td>2175.20 (n/a)</td><td>2138.51 (n/a)</td><td>55.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.90 (-6.77%)</td><td>3.74 (+3.70%)</td><td>3.70 (+0.02%)</td><td>3.60 (+18.82%)</td><td>0.13 <b>(-70.80%)</b></td><td>2238.20 (-15.84%)</td><td>2156.98 (-4.61%)</td><td>2181.40 (-0.01%)</td><td>2066.00 (+7.26%)</td><td>72.31 <b>(-73.88%)</b></td><td>1023.22 (-6.77%)</td><td>980.93 (+3.70%)</td><td>969.08 (+0.02%)</td><td>944.46 (+18.82%)</td><td>33.14 <b>(-70.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.18 (n/a)</td><td>3.61 (n/a)</td><td>3.69 (n/a)</td><td>3.03 (n/a)</td><td>0.43 (n/a)</td><td>2659.40 (n/a)</td><td>2261.18 (n/a)</td><td>2181.70 (n/a)</td><td>1926.20 (n/a)</td><td>276.80 (n/a)</td><td>1097.49 (n/a)</td><td>945.93 (n/a)</td><td>968.93 (n/a)</td><td>794.89 (n/a)</td><td>113.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.46 <b>(+27.27%)</b></td><td>0.34 (+1.60%)</td><td>0.31 (-6.53%)</td><td>0.29 (-7.73%)</td><td>0.07 <b>(+266.42%)</b></td><td>4249.20 (+8.38%)</td><td>3743.58 (+0.99%)</td><td>4033.10 (+6.98%)</td><td>2688.40 <b>(-21.43%)</b></td><td>638.21 <b>(+207.91%)</b></td><td>24.96 <b>(+27.27%)</b></td><td>18.44 (+1.60%)</td><td>16.64 (-6.53%)</td><td>15.79 (-7.73%)</td><td>3.80 <b>(+266.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.02 (n/a)</td><td>3920.80 (n/a)</td><td>3706.72 (n/a)</td><td>3769.90 (n/a)</td><td>3421.60 (n/a)</td><td>207.27 (n/a)</td><td>19.61 (n/a)</td><td>18.15 (n/a)</td><td>17.80 (n/a)</td><td>17.12 (n/a)</td><td>1.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.80 (+10.48%)</td><td>4.92 (+9.04%)</td><td>4.83 (+2.12%)</td><td>3.53 (+10.35%)</td><td>1.18 (+1.74%)</td><td>1885.90 (-9.38%)</td><td>1412.60 (-9.19%)</td><td>1375.90 (-2.08%)</td><td>977.50 (-9.48%)</td><td>323.11 (-19.33%)</td><td>2102.47 (+10.48%)</td><td>1519.88 (+9.04%)</td><td>1493.69 (+2.12%)</td><td>1089.79 (+10.35%)</td><td>366.12 (+1.74%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.16 (n/a)</td><td>4.51 (n/a)</td><td>4.73 (n/a)</td><td>3.20 (n/a)</td><td>1.16 (n/a)</td><td>2081.00 (n/a)</td><td>1555.56 (n/a)</td><td>1405.10 (n/a)</td><td>1079.90 (n/a)</td><td>400.54 (n/a)</td><td>1903.11 (n/a)</td><td>1393.91 (n/a)</td><td>1462.68 (n/a)</td><td>987.60 (n/a)</td><td>359.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>13.21 (n/a)</td><td>12.37 (n/a)</td><td>12.32 (n/a)</td><td>11.38 (n/a)</td><td>0.75 (n/a)</td><td>13.20 (n/a)</td><td>12.36 (n/a)</td><td>12.31 (n/a)</td><td>11.37 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>25.08 (+0.71%)</td><td>24.41 (+0.83%)</td><td>24.37 (+1.14%)</td><td>23.73 (-0.81%)</td><td>0.49 <b>(+20.58%)</b></td><td>25.06 (+0.71%)</td><td>24.39 (+0.83%)</td><td>24.36 (+1.14%)</td><td>23.71 (-0.81%)</td><td>0.49 <b>(+20.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>24.90 (n/a)</td><td>24.21 (n/a)</td><td>24.10 (n/a)</td><td>23.92 (n/a)</td><td>0.41 (n/a)</td><td>24.89 (n/a)</td><td>24.19 (n/a)</td><td>24.08 (n/a)</td><td>23.90 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>40.67 (-2.96%)</td><td>39.16 (-3.92%)</td><td>39.66 (-1.86%)</td><td>36.76 (-8.29%)</td><td>1.59 <b>(+107.06%)</b></td><td>40.64 (-2.96%)</td><td>39.14 (-3.92%)</td><td>39.64 (-1.86%)</td><td>36.74 (-8.29%)</td><td>1.59 <b>(+107.06%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>41.91 (n/a)</td><td>40.76 (n/a)</td><td>40.42 (n/a)</td><td>40.09 (n/a)</td><td>0.77 (n/a)</td><td>41.88 (n/a)</td><td>40.74 (n/a)</td><td>40.39 (n/a)</td><td>40.06 (n/a)</td><td>0.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>44.98 (+5.89%)</td><td>43.17 (+2.89%)</td><td>43.10 (+1.94%)</td><td>41.88 (+2.37%)</td><td>1.28 <b>(+97.13%)</b></td><td>44.95 (+5.89%)</td><td>43.15 (+2.89%)</td><td>43.07 (+1.94%)</td><td>41.85 (+2.37%)</td><td>1.28 <b>(+97.13%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>42.48 (n/a)</td><td>41.96 (n/a)</td><td>42.28 (n/a)</td><td>40.91 (n/a)</td><td>0.65 (n/a)</td><td>42.45 (n/a)</td><td>41.94 (n/a)</td><td>42.25 (n/a)</td><td>40.88 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>13.29 (n/a)</td><td>13.00 (n/a)</td><td>13.16 (n/a)</td><td>12.60 (n/a)</td><td>0.33 (n/a)</td><td>13.28 (n/a)</td><td>12.99 (n/a)</td><td>13.16 (n/a)</td><td>12.59 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>24.74 (+0.19%)</td><td>24.47 (+0.89%)</td><td>24.45 (+0.95%)</td><td>24.24 (+2.95%)</td><td>0.21 <b>(-56.31%)</b></td><td>24.72 (+0.19%)</td><td>24.45 (+0.89%)</td><td>24.44 (+0.95%)</td><td>24.23 (+2.95%)</td><td>0.20 <b>(-56.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>24.69 (n/a)</td><td>24.25 (n/a)</td><td>24.22 (n/a)</td><td>23.55 (n/a)</td><td>0.47 (n/a)</td><td>24.68 (n/a)</td><td>24.24 (n/a)</td><td>24.21 (n/a)</td><td>23.53 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>40.57 (+0.53%)</td><td>39.80 (+1.10%)</td><td>39.68 (+1.81%)</td><td>38.96 (+0.84%)</td><td>0.66 (-17.52%)</td><td>40.55 (+0.53%)</td><td>39.78 (+1.10%)</td><td>39.65 (+1.81%)</td><td>38.93 (+0.84%)</td><td>0.65 (-17.52%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>40.36 (n/a)</td><td>39.37 (n/a)</td><td>38.97 (n/a)</td><td>38.63 (n/a)</td><td>0.79 (n/a)</td><td>40.33 (n/a)</td><td>39.34 (n/a)</td><td>38.95 (n/a)</td><td>38.61 (n/a)</td><td>0.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>45.41 (+5.38%)</td><td>43.04 (+1.30%)</td><td>42.52 (+0.01%)</td><td>41.76 (-0.31%)</td><td>1.47 <b>(+242.19%)</b></td><td>45.38 (+5.38%)</td><td>43.01 (+1.30%)</td><td>42.49 (+0.01%)</td><td>41.74 (-0.31%)</td><td>1.47 <b>(+242.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>43.09 (n/a)</td><td>42.49 (n/a)</td><td>42.51 (n/a)</td><td>41.89 (n/a)</td><td>0.43 (n/a)</td><td>43.07 (n/a)</td><td>42.46 (n/a)</td><td>42.49 (n/a)</td><td>41.86 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>9.00 (-9.96%)</td><td>8.65 (-2.31%)</td><td>8.78 (-0.49%)</td><td>8.27 (+5.62%)</td><td>0.34 <b>(-59.71%)</b></td><td>8.99 (-9.96%)</td><td>8.63 (-2.31%)</td><td>8.76 (-0.49%)</td><td>8.25 (+5.62%)</td><td>0.34 <b>(-59.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>10.00 (n/a)</td><td>8.85 (n/a)</td><td>8.82 (n/a)</td><td>7.83 (n/a)</td><td>0.84 (n/a)</td><td>9.98 (n/a)</td><td>8.83 (n/a)</td><td>8.81 (n/a)</td><td>7.81 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.13 (+9.09%)</td><td>1.02 (+7.07%)</td><td>1.04 (+6.32%)</td><td>0.91 (+9.27%)</td><td>0.11 <b>(+38.82%)</b></td><td>1.11 (+9.09%)</td><td>1.00 (+7.07%)</td><td>1.02 (+6.32%)</td><td>0.89 (+9.27%)</td><td>0.11 <b>(+38.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.04 (n/a)</td><td>0.95 (n/a)</td><td>0.97 (n/a)</td><td>0.83 (n/a)</td><td>0.08 (n/a)</td><td>1.02 (n/a)</td><td>0.94 (n/a)</td><td>0.96 (n/a)</td><td>0.82 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.21 (-15.41%)</td><td>1.11 (-9.17%)</td><td>1.11 (-10.89%)</td><td>1.00 (-4.14%)</td><td>0.08 <b>(-47.81%)</b></td><td>1.20 (-15.41%)</td><td>1.09 (-9.17%)</td><td>1.10 (-10.89%)</td><td>0.99 (-4.14%)</td><td>0.08 <b>(-47.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.43 (n/a)</td><td>1.22 (n/a)</td><td>1.25 (n/a)</td><td>1.04 (n/a)</td><td>0.15 (n/a)</td><td>1.41 (n/a)</td><td>1.20 (n/a)</td><td>1.23 (n/a)</td><td>1.03 (n/a)</td><td>0.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>18.71 (-1.34%)</td><td>17.05 (-2.36%)</td><td>16.85 (-1.27%)</td><td>15.93 (-2.40%)</td><td>1.03 (-17.33%)</td><td>18.49 (-1.34%)</td><td>16.85 (-2.36%)</td><td>16.66 (-1.27%)</td><td>15.74 (-2.40%)</td><td>1.02 (-17.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>18.96 (n/a)</td><td>17.46 (n/a)</td><td>17.07 (n/a)</td><td>16.32 (n/a)</td><td>1.25 (n/a)</td><td>18.74 (n/a)</td><td>17.26 (n/a)</td><td>16.87 (n/a)</td><td>16.13 (n/a)</td><td>1.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>14.12 (+0.42%)</td><td>13.75 (+10.47%)</td><td>13.68 (+3.28%)</td><td>13.40 <b>(+67.81%)</b></td><td>0.27 <b>(-89.18%)</b></td><td>13.87 (+0.42%)</td><td>13.51 (+10.47%)</td><td>13.44 (+3.28%)</td><td>13.17 <b>(+67.81%)</b></td><td>0.27 <b>(-89.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>14.06 (n/a)</td><td>12.45 (n/a)</td><td>13.24 (n/a)</td><td>7.99 (n/a)</td><td>2.53 (n/a)</td><td>13.82 (n/a)</td><td>12.23 (n/a)</td><td>13.01 (n/a)</td><td>7.85 (n/a)</td><td>2.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>7.95 (-3.16%)</td><td>7.44 (-3.63%)</td><td>7.65 (-2.03%)</td><td>6.80 (-2.19%)</td><td>0.53 (+9.04%)</td><td>7.81 (-3.16%)</td><td>7.32 (-3.63%)</td><td>7.52 (-2.03%)</td><td>6.68 (-2.19%)</td><td>0.52 (+9.04%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>8.21 (n/a)</td><td>7.72 (n/a)</td><td>7.81 (n/a)</td><td>6.95 (n/a)</td><td>0.48 (n/a)</td><td>8.06 (n/a)</td><td>7.59 (n/a)</td><td>7.68 (n/a)</td><td>6.83 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>5.95 (-11.66%)</td><td>5.41 (-4.68%)</td><td>5.62 (+5.09%)</td><td>4.73 (-3.63%)</td><td>0.48 <b>(-43.33%)</b></td><td>5.85 (-11.66%)</td><td>5.32 (-4.68%)</td><td>5.53 (+5.09%)</td><td>4.65 (-3.63%)</td><td>0.47 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.73 (n/a)</td><td>5.68 (n/a)</td><td>5.35 (n/a)</td><td>4.91 (n/a)</td><td>0.84 (n/a)</td><td>6.62 (n/a)</td><td>5.59 (n/a)</td><td>5.26 (n/a)</td><td>4.83 (n/a)</td><td>0.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>13.42 (n/a)</td><td>13.15 (n/a)</td><td>13.19 (n/a)</td><td>12.68 (n/a)</td><td>0.29 (n/a)</td><td>13.41 (n/a)</td><td>13.14 (n/a)</td><td>13.18 (n/a)</td><td>12.67 (n/a)</td><td>0.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>13.54 (n/a)</td><td>13.07 (n/a)</td><td>13.22 (n/a)</td><td>12.05 (n/a)</td><td>0.59 (n/a)</td><td>13.53 (n/a)</td><td>13.07 (n/a)</td><td>13.21 (n/a)</td><td>12.04 (n/a)</td><td>0.59 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>156.20 (n/a)</td><td>153.40 (n/a)</td><td>125.80 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>165.98 (n/a)</td><td>164.90 (n/a)</td><td>106.50 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>161.42 (n/a)</td><td>166.60 (n/a)</td><td>116.80 (n/a)</td><td>33.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>167.30 (n/a)</td><td>176.20 (n/a)</td><td>136.50 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>168.76 (n/a)</td><td>178.90 (n/a)</td><td>120.60 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>206.80 (n/a)</td><td>228.60 (n/a)</td><td>131.30 (n/a)</td><td>43.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.20 (n/a)</td><td>198.80 (n/a)</td><td>197.50 (n/a)</td><td>178.80 (n/a)</td><td>21.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.20 (n/a)</td><td>224.76 (n/a)</td><td>224.70 (n/a)</td><td>203.80 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+6.11%)</td><td>0.05 (+4.04%)</td><td>0.05 (-1.37%)</td><td>0.04 (+4.17%)</td><td>0.01 (-3.00%)</td><td>191.90 (-4.00%)</td><td>164.70 (-4.11%)</td><td>164.60 (+1.42%)</td><td>138.20 (-5.79%)</td><td>19.05 (-13.80%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>171.76 (n/a)</td><td>162.30 (n/a)</td><td>146.70 (n/a)</td><td>22.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+5.04%)</td><td>0.05 (-4.85%)</td><td>0.05 (+0.01%)</td><td>0.02 <b>(-44.18%)</b></td><td>0.02 <b>(+79.11%)</b></td><td>375.20 <b>(+79.09%)</b></td><td>202.06 (+17.23%)</td><td>170.60 (+0.00%)</td><td>126.70 (-4.81%)</td><td>98.66 <b>(+236.90%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>172.36 (n/a)</td><td>170.60 (n/a)</td><td>133.10 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+18.97%)</td><td>0.05 (+4.42%)</td><td>0.05 (+3.78%)</td><td>0.04 (-4.21%)</td><td>0.01 <b>(+94.56%)</b></td><td>205.80 (+4.36%)</td><td>166.40 (-2.53%)</td><td>155.00 (-3.67%)</td><td>131.90 (-15.93%)</td><td>29.86 <b>(+73.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>170.72 (n/a)</td><td>160.90 (n/a)</td><td>156.90 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 <b>(+25.26%)</b></td><td>0.05 (+15.47%)</td><td>0.05 (+14.98%)</td><td>0.04 <b>(+25.94%)</b></td><td>0.01 (+8.28%)</td><td>182.50 <b>(-20.62%)</b></td><td>157.96 (-14.10%)</td><td>169.60 (-13.03%)</td><td>115.30 <b>(-20.15%)</b></td><td>26.88 <b>(-29.17%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>183.88 (n/a)</td><td>195.00 (n/a)</td><td>144.40 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 <b>(+48.85%)</b></td><td>0.05 <b>(+22.26%)</b></td><td>0.05 (+15.96%)</td><td>0.03 <b>(-28.26%)</b></td><td>0.02 <b>(+191.05%)</b></td><td>300.00 <b>(+39.41%)</b></td><td>174.20 (-6.61%)</td><td>166.60 (-13.72%)</td><td>97.30 <b>(-32.85%)</b></td><td>80.08 <b>(+165.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>186.52 (n/a)</td><td>193.10 (n/a)</td><td>144.90 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 <b>(+55.09%)</b></td><td>0.05 <b>(+32.67%)</b></td><td>0.05 <b>(+31.66%)</b></td><td>0.04 (+14.45%)</td><td>0.01 <b>(+219.02%)</b></td><td>190.40 (-12.62%)</td><td>153.06 <b>(-23.24%)</b></td><td>152.00 <b>(-24.08%)</b></td><td>119.20 <b>(-35.53%)</b></td><td>25.38 <b>(+80.65%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.90 (n/a)</td><td>199.40 (n/a)</td><td>200.20 (n/a)</td><td>184.90 (n/a)</td><td>14.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (+0.24%)</td><td>0.05 (+0.58%)</td><td>0.05 (-0.48%)</td><td>0.04 <b>(+28.59%)</b></td><td>0.01 <b>(-38.43%)</b></td><td>202.90 <b>(-22.23%)</b></td><td>180.22 (-3.09%)</td><td>177.90 (+0.51%)</td><td>151.60 (-0.26%)</td><td>20.19 <b>(-53.60%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.90 (n/a)</td><td>185.96 (n/a)</td><td>177.00 (n/a)</td><td>152.00 (n/a)</td><td>43.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (+19.28%)</td><td>0.05 (+17.96%)</td><td>0.05 <b>(+20.63%)</b></td><td>0.04 (+17.13%)</td><td>0.01 <b>(+30.08%)</b></td><td>197.30 (-14.66%)</td><td>179.32 (-15.08%)</td><td>178.90 (-17.10%)</td><td>151.30 (-16.18%)</td><td>19.10 (-5.66%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.20 (n/a)</td><td>211.16 (n/a)</td><td>215.80 (n/a)</td><td>180.50 (n/a)</td><td>20.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+4.89%)</td><td>0.05 <b>(+25.67%)</b></td><td>0.05 <b>(+52.10%)</b></td><td>0.04 (+18.23%)</td><td>0.01 (-2.20%)</td><td>221.60 (-15.42%)</td><td>164.16 <b>(-21.44%)</b></td><td>150.70 <b>(-34.25%)</b></td><td>128.30 (-4.68%)</td><td>40.22 <b>(-21.43%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>262.00 (n/a)</td><td>208.96 (n/a)</td><td>229.20 (n/a)</td><td>134.60 (n/a)</td><td>51.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 <b>(+20.26%)</b></td><td>0.04 (+8.90%)</td><td>0.04 (+10.12%)</td><td>0.03 (-16.11%)</td><td>0.01 <b>(+211.23%)</b></td><td>278.40 (+19.23%)</td><td>207.46 (-5.48%)</td><td>204.60 (-9.19%)</td><td>167.60 (-16.87%)</td><td>44.11 <b>(+209.63%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>219.48 (n/a)</td><td>225.30 (n/a)</td><td>201.60 (n/a)</td><td>14.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+7.58%)</td><td>0.05 (+10.03%)</td><td>0.06 (+18.29%)</td><td>0.04 (+6.74%)</td><td>0.01 <b>(+29.83%)</b></td><td>198.20 (-6.29%)</td><td>160.64 (-8.65%)</td><td>146.30 (-15.43%)</td><td>141.80 (-7.02%)</td><td>23.91 (+10.23%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>175.86 (n/a)</td><td>173.00 (n/a)</td><td>152.50 (n/a)</td><td>21.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (-4.03%)</td><td>0.04 (-1.77%)</td><td>0.04 (+2.99%)</td><td>0.02 (-4.74%)</td><td>0.01 (-6.61%)</td><td>352.40 (+4.97%)</td><td>236.20 (+1.81%)</td><td>217.80 (-2.90%)</td><td>187.80 (+4.16%)</td><td>66.28 (+6.44%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>335.70 (n/a)</td><td>232.00 (n/a)</td><td>224.30 (n/a)</td><td>180.30 (n/a)</td><td>62.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+17.44%)</td><td>0.05 (+9.56%)</td><td>0.05 (-0.23%)</td><td>0.04 (+6.74%)</td><td>0.01 <b>(+58.55%)</b></td><td>185.80 (-6.30%)</td><td>162.62 (-7.65%)</td><td>173.80 (+0.23%)</td><td>126.90 (-14.83%)</td><td>26.48 <b>(+26.13%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>176.10 (n/a)</td><td>173.40 (n/a)</td><td>149.00 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (-7.11%)</td><td>0.05 (-10.29%)</td><td>0.05 (-16.49%)</td><td>0.03 (-12.32%)</td><td>0.01 (+10.20%)</td><td>234.70 (+14.04%)</td><td>179.60 (+12.98%)</td><td>178.30 (+19.74%)</td><td>132.80 (+7.70%)</td><td>41.50 <b>(+32.54%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>158.96 (n/a)</td><td>148.90 (n/a)</td><td>123.30 (n/a)</td><td>31.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (-10.04%)</td><td>0.04 (-9.69%)</td><td>0.04 (-5.88%)</td><td>0.04 (-15.20%)</td><td>0.00 (+9.49%)</td><td>218.30 (+17.87%)</td><td>190.96 (+11.07%)</td><td>184.00 (+6.24%)</td><td>165.70 (+11.13%)</td><td>20.31 <b>(+46.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.20 (n/a)</td><td>171.92 (n/a)</td><td>173.20 (n/a)</td><td>149.10 (n/a)</td><td>13.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 <b>(-22.53%)</b></td><td>0.04 (-18.59%)</td><td>0.04 (-12.02%)</td><td>0.03 <b>(-25.48%)</b></td><td>0.01 <b>(-28.96%)</b></td><td>256.50 <b>(+34.22%)</b></td><td>190.80 <b>(+22.45%)</b></td><td>184.90 (+13.64%)</td><td>149.80 <b>(+29.03%)</b></td><td>39.53 <b>(+28.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>155.82 (n/a)</td><td>162.70 (n/a)</td><td>116.10 (n/a)</td><td>30.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (-11.34%)</td><td>0.04 (-11.18%)</td><td>0.05 (-3.03%)</td><td>0.03 <b>(-26.94%)</b></td><td>0.01 (+15.26%)</td><td>276.40 <b>(+36.90%)</b></td><td>197.46 (+15.20%)</td><td>181.80 (+3.12%)</td><td>149.40 (+12.75%)</td><td>49.36 <b>(+83.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>171.40 (n/a)</td><td>176.30 (n/a)</td><td>132.50 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (-9.95%)</td><td>0.04 (-2.86%)</td><td>0.05 (-4.56%)</td><td>0.04 (+12.18%)</td><td>0.00 <b>(-60.54%)</b></td><td>202.30 (-10.84%)</td><td>186.38 (+1.25%)</td><td>181.20 (+4.74%)</td><td>175.40 (+11.01%)</td><td>11.79 <b>(-60.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>184.08 (n/a)</td><td>173.00 (n/a)</td><td>158.00 (n/a)</td><td>29.78 (n/a)</td>
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


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52647.20 (n/a)</td><td>52577.50 (n/a)</td><td>52580.00 (n/a)</td><td>52538.50 (n/a)</td><td>44.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.18 (-12.05%)</td><td>0.15 (-4.73%)</td><td>0.14 (-6.35%)</td><td>0.13 (-8.51%)</td><td>0.02 (-6.30%)</td><td>184.20 (+9.32%)</td><td>164.34 (+5.09%)</td><td>174.00 (+6.75%)</td><td>140.20 (+13.71%)</td><td>21.92 (+16.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>168.50 (n/a)</td><td>156.38 (n/a)</td><td>163.00 (n/a)</td><td>123.30 (n/a)</td><td>18.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.28 (-12.45%)</td><td>0.26 (-5.78%)</td><td>0.26 (-16.81%)</td><td>0.24 <b>(+33.11%)</b></td><td>0.02 <b>(-70.92%)</b></td><td>173.00 <b>(-24.85%)</b></td><td>157.42 (+1.03%)</td><td>156.00 <b>(+20.18%)</b></td><td>145.10 (+14.25%)</td><td>11.33 <b>(-74.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>230.20 (n/a)</td><td>155.82 (n/a)</td><td>129.80 (n/a)</td><td>127.00 (n/a)</td><td>44.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (-11.21%)</td><td>0.03 (-19.80%)</td><td>0.03 <b>(-21.71%)</b></td><td>0.02 <b>(-23.93%)</b></td><td>0.01 (+0.47%)</td><td>229.50 <b>(+31.44%)</b></td><td>177.54 <b>(+25.83%)</b></td><td>173.40 <b>(+27.78%)</b></td><td>137.00 (+12.66%)</td><td>33.24 <b>(+51.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>174.60 (n/a)</td><td>141.10 (n/a)</td><td>135.70 (n/a)</td><td>121.60 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+4.49%)</td><td>0.05 (-1.46%)</td><td>0.05 (-5.02%)</td><td>0.04 (+9.25%)</td><td>0.01 (-13.82%)</td><td>216.90 (-8.48%)</td><td>179.26 (+0.30%)</td><td>175.50 (+5.28%)</td><td>138.60 (-4.28%)</td><td>28.34 <b>(-25.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>178.72 (n/a)</td><td>166.70 (n/a)</td><td>144.80 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.12 (+11.75%)</td><td>0.09 <b>(+23.99%)</b></td><td>0.09 <b>(+40.42%)</b></td><td>0.07 (+4.31%)</td><td>0.02 <b>(+33.72%)</b></td><td>186.40 (-4.12%)</td><td>141.00 (-17.98%)</td><td>134.00 <b>(-28.76%)</b></td><td>106.60 (-10.57%)</td><td>35.97 (+12.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>171.90 (n/a)</td><td>188.10 (n/a)</td><td>119.20 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (-8.17%)</td><td>0.05 (-1.71%)</td><td>0.06 (-2.22%)</td><td>0.05 (+5.30%)</td><td>0.01 <b>(-21.14%)</b></td><td>176.60 (-5.05%)</td><td>153.90 (+1.14%)</td><td>148.10 (+2.28%)</td><td>138.00 (+8.92%)</td><td>17.69 <b>(-20.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>152.16 (n/a)</td><td>144.80 (n/a)</td><td>126.70 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 (-9.29%)</td><td>0.06 (-1.48%)</td><td>0.06 (+0.46%)</td><td>0.05 <b>(+22.44%)</b></td><td>0.01 <b>(-38.01%)</b></td><td>204.40 (-18.31%)</td><td>169.68 (-2.18%)</td><td>173.50 (-0.46%)</td><td>133.50 (+10.24%)</td><td>26.25 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>250.20 (n/a)</td><td>173.46 (n/a)</td><td>174.30 (n/a)</td><td>121.10 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+6.67%)</td><td>0.06 (+16.11%)</td><td>0.06 (+15.64%)</td><td>0.05 <b>(+31.21%)</b></td><td>0.01 <b>(-22.24%)</b></td><td>168.70 <b>(-23.80%)</b></td><td>149.68 (-14.95%)</td><td>140.70 (-13.52%)</td><td>135.70 (-6.28%)</td><td>16.62 <b>(-44.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>176.00 (n/a)</td><td>162.70 (n/a)</td><td>144.80 (n/a)</td><td>30.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (+2.45%)</td><td>0.06 (-4.52%)</td><td>0.06 (-9.42%)</td><td>0.05 (+7.75%)</td><td>0.01 (-10.65%)</td><td>212.10 (-7.18%)</td><td>181.02 (+4.13%)</td><td>174.90 (+10.42%)</td><td>150.80 (-2.39%)</td><td>25.70 (-18.44%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>173.84 (n/a)</td><td>158.40 (n/a)</td><td>154.50 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+7.78%)</td><td>0.05 (+13.47%)</td><td>0.05 (+14.00%)</td><td>0.04 (+2.78%)</td><td>0.01 <b>(+24.35%)</b></td><td>214.30 (-2.72%)</td><td>163.70 (-11.24%)</td><td>162.10 (-12.28%)</td><td>138.10 (-7.19%)</td><td>30.96 (+11.74%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>184.44 (n/a)</td><td>184.80 (n/a)</td><td>148.80 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (+13.87%)</td><td>0.06 (+5.64%)</td><td>0.06 (+5.80%)</td><td>0.04 (-0.18%)</td><td>0.01 <b>(+36.37%)</b></td><td>219.00 (+0.18%)</td><td>167.30 (-4.15%)</td><td>156.10 (-5.45%)</td><td>126.50 (-12.15%)</td><td>34.53 (+19.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>174.54 (n/a)</td><td>165.10 (n/a)</td><td>144.00 (n/a)</td><td>28.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (-5.42%)</td><td>0.05 (-7.92%)</td><td>0.05 (-13.57%)</td><td>0.04 (+5.57%)</td><td>0.01 <b>(-31.24%)</b></td><td>199.60 (-5.27%)</td><td>175.46 (+6.56%)</td><td>178.40 (+15.69%)</td><td>138.40 (+5.73%)</td><td>24.93 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>164.66 (n/a)</td><td>154.20 (n/a)</td><td>130.90 (n/a)</td><td>35.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (+3.51%)</td><td>0.06 (+19.85%)</td><td>0.06 (+14.83%)</td><td>0.06 <b>(+96.20%)</b></td><td>0.00 <b>(-67.00%)</b></td><td>165.40 <b>(-49.03%)</b></td><td>158.44 <b>(-22.40%)</b></td><td>161.90 (-12.91%)</td><td>139.20 (-3.40%)</td><td>10.97 <b>(-84.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.50 (n/a)</td><td>204.18 (n/a)</td><td>185.90 (n/a)</td><td>144.10 (n/a)</td><td>70.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (-15.81%)</td><td>0.04 (-11.48%)</td><td>0.04 (-4.81%)</td><td>0.03 <b>(-34.94%)</b></td><td>0.01 (+15.56%)</td><td>324.90 <b>(+53.69%)</b></td><td>210.98 (+17.12%)</td><td>190.30 (+5.08%)</td><td>163.70 (+18.80%)</td><td>66.66 <b>(+107.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>180.14 (n/a)</td><td>181.10 (n/a)</td><td>137.80 (n/a)</td><td>32.14 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (+8.21%)</td><td>0.04 (+1.65%)</td><td>0.05 (+11.56%)</td><td>0.03 <b>(-24.57%)</b></td><td>0.01 <b>(+116.20%)</b></td><td>303.00 <b>(+32.60%)</b></td><td>207.14 (+2.44%)</td><td>177.60 (-10.35%)</td><td>163.60 (-7.57%)</td><td>56.85 <b>(+169.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.50 (n/a)</td><td>202.20 (n/a)</td><td>198.10 (n/a)</td><td>177.00 (n/a)</td><td>21.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+8.04%)</td><td>0.05 (+8.74%)</td><td>0.05 (+19.24%)</td><td>0.04 (+8.00%)</td><td>0.01 (-13.91%)</td><td>183.90 (-7.40%)</td><td>159.74 (-8.79%)</td><td>159.70 (-16.17%)</td><td>129.30 (-7.44%)</td><td>19.76 <b>(-28.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>175.14 (n/a)</td><td>190.50 (n/a)</td><td>139.70 (n/a)</td><td>27.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+12.21%)</td><td>0.05 (+12.39%)</td><td>0.05 (+18.22%)</td><td>0.04 (+10.30%)</td><td>0.00 <b>(+25.71%)</b></td><td>204.30 (-9.32%)</td><td>177.72 (-10.85%)</td><td>170.10 (-15.42%)</td><td>157.50 (-10.92%)</td><td>18.47 (+2.49%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>199.36 (n/a)</td><td>201.10 (n/a)</td><td>176.80 (n/a)</td><td>18.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (+15.74%)</td><td>0.04 (+5.70%)</td><td>0.04 (+9.37%)</td><td>0.04 (+6.78%)</td><td>0.01 (+13.81%)</td><td>231.10 (-6.36%)</td><td>196.24 (-5.41%)</td><td>203.50 (-8.54%)</td><td>135.20 (-13.61%)</td><td>36.52 (-12.10%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.80 (n/a)</td><td>207.46 (n/a)</td><td>222.50 (n/a)</td><td>156.50 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.69 (-11.24%)</td><td>0.56 (-2.64%)</td><td>0.53 (+2.37%)</td><td>0.49 (+5.20%)</td><td>0.08 <b>(-35.36%)</b></td><td>199.10 (-4.92%)</td><td>179.54 (+0.80%)</td><td>186.60 (-2.35%)</td><td>141.60 (+12.65%)</td><td>23.76 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.78 (n/a)</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.13 (n/a)</td><td>209.40 (n/a)</td><td>178.12 (n/a)</td><td>191.10 (n/a)</td><td>125.70 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.70 (+16.47%)</td><td>0.59 (+5.25%)</td><td>0.62 (+6.19%)</td><td>0.44 (-13.40%)</td><td>0.12 <b>(+166.55%)</b></td><td>224.50 (+15.48%)</td><td>173.22 (-2.07%)</td><td>159.00 (-5.86%)</td><td>140.50 (-14.17%)</td><td>37.61 <b>(+158.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.60 (n/a)</td><td>0.56 (n/a)</td><td>0.58 (n/a)</td><td>0.51 (n/a)</td><td>0.04 (n/a)</td><td>194.40 (n/a)</td><td>176.88 (n/a)</td><td>168.90 (n/a)</td><td>163.70 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.75 (-1.57%)</td><td>0.51 (-10.36%)</td><td>0.47 <b>(-20.14%)</b></td><td>0.40 (-4.75%)</td><td>0.14 (+10.25%)</td><td>244.60 (+4.98%)</td><td>201.38 (+12.88%)</td><td>209.00 <b>(+25.22%)</b></td><td>131.40 (+1.55%)</td><td>47.13 (+17.74%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.76 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.13 (n/a)</td><td>233.00 (n/a)</td><td>178.40 (n/a)</td><td>166.90 (n/a)</td><td>129.40 (n/a)</td><td>40.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.59 (-9.38%)</td><td>0.39 <b>(-30.21%)</b></td><td>0.36 <b>(-33.49%)</b></td><td>0.29 <b>(-40.20%)</b></td><td>0.12 <b>(+87.65%)</b></td><td>340.00 <b>(+67.24%)</b></td><td>269.06 <b>(+51.94%)</b></td><td>273.40 <b>(+50.39%)</b></td><td>165.60 (+10.40%)</td><td>72.50 <b>(+253.57%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.66 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.07 (n/a)</td><td>203.30 (n/a)</td><td>177.08 (n/a)</td><td>181.80 (n/a)</td><td>150.00 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.54 (+0.07%)</td><td>0.45 (-4.74%)</td><td>0.43 (-11.97%)</td><td>0.38 (-2.48%)</td><td>0.07 (+7.89%)</td><td>191.90 (+2.51%)</td><td>166.36 (+5.36%)</td><td>171.40 (+13.66%)</td><td>135.50 (-0.07%)</td><td>26.51 (+11.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>187.20 (n/a)</td><td>157.90 (n/a)</td><td>150.80 (n/a)</td><td>135.60 (n/a)</td><td>23.72 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.50 <b>(-20.21%)</b></td><td>0.42 (-12.50%)</td><td>0.45 (+4.29%)</td><td>0.32 <b>(-27.21%)</b></td><td>0.07 (-12.13%)</td><td>233.70 <b>(+37.39%)</b></td><td>178.74 (+15.03%)</td><td>162.70 (-4.12%)</td><td>148.40 <b>(+25.34%)</b></td><td>34.30 <b>(+51.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>170.10 (n/a)</td><td>155.38 (n/a)</td><td>169.70 (n/a)</td><td>118.40 (n/a)</td><td>22.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.55 <b>(+25.04%)</b></td><td>0.43 (+8.36%)</td><td>0.42 (+0.37%)</td><td>0.32 (-1.16%)</td><td>0.09 <b>(+80.48%)</b></td><td>231.40 (+1.18%)</td><td>180.08 (-5.54%)</td><td>177.40 (-0.34%)</td><td>135.00 <b>(-20.02%)</b></td><td>38.90 <b>(+47.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>228.70 (n/a)</td><td>190.64 (n/a)</td><td>178.00 (n/a)</td><td>168.80 (n/a)</td><td>26.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.46 <b>(+21.64%)</b></td><td>0.39 (+15.46%)</td><td>0.38 (+8.06%)</td><td>0.33 <b>(+31.81%)</b></td><td>0.05 (-3.19%)</td><td>222.20 <b>(-24.14%)</b></td><td>192.00 (-14.20%)</td><td>192.60 (-7.49%)</td><td>159.30 (-17.80%)</td><td>23.09 <b>(-41.91%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.35 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>292.90 (n/a)</td><td>223.78 (n/a)</td><td>208.20 (n/a)</td><td>193.80 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.07 (-2.37%)</td><td>0.83 (-1.42%)</td><td>0.99 <b>(+20.81%)</b></td><td>0.53 <b>(-22.13%)</b></td><td>0.25 <b>(+64.41%)</b></td><td>248.50 <b>(+28.42%)</b></td><td>171.10 (+7.84%)</td><td>133.00 (-17.24%)</td><td>122.60 (+2.42%)</td><td>58.28 <b>(+121.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.10 (n/a)</td><td>0.85 (n/a)</td><td>0.82 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>193.50 (n/a)</td><td>158.66 (n/a)</td><td>160.70 (n/a)</td><td>119.70 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.00 (-17.80%)</td><td>0.73 (-12.29%)</td><td>0.71 (-10.94%)</td><td>0.53 (-10.74%)</td><td>0.17 <b>(-32.51%)</b></td><td>245.30 (+12.01%)</td><td>185.98 (+11.03%)</td><td>185.80 (+12.27%)</td><td>131.10 <b>(+21.61%)</b></td><td>41.09 (-10.67%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.22 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.25 (n/a)</td><td>219.00 (n/a)</td><td>167.50 (n/a)</td><td>165.50 (n/a)</td><td>107.80 (n/a)</td><td>46.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.98 (+5.95%)</td><td>0.72 (-7.71%)</td><td>0.69 (-12.05%)</td><td>0.45 <b>(-26.30%)</b></td><td>0.20 <b>(+59.97%)</b></td><td>292.60 <b>(+35.71%)</b></td><td>195.54 (+13.53%)</td><td>190.00 (+13.70%)</td><td>133.80 (-5.64%)</td><td>60.37 <b>(+108.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.61 (n/a)</td><td>0.12 (n/a)</td><td>215.60 (n/a)</td><td>172.24 (n/a)</td><td>167.10 (n/a)</td><td>141.80 (n/a)</td><td>28.98 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (+11.73%)</td><td>0.03 (-3.64%)</td><td>0.02 (-14.77%)</td><td>0.02 (-12.43%)</td><td>0.01 <b>(+69.00%)</b></td><td>216.20 (+14.21%)</td><td>168.86 (+7.04%)</td><td>176.50 (+17.28%)</td><td>114.70 (-10.53%)</td><td>39.25 <b>(+69.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>157.76 (n/a)</td><td>150.50 (n/a)</td><td>128.20 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (-10.31%)</td><td>0.03 (-2.79%)</td><td>0.03 (-2.37%)</td><td>0.02 (-5.79%)</td><td>0.00 (-12.94%)</td><td>223.70 (+6.17%)</td><td>159.00 (+2.58%)</td><td>146.60 (+2.37%)</td><td>133.60 (+11.52%)</td><td>36.81 (+4.72%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.70 (n/a)</td><td>155.00 (n/a)</td><td>143.20 (n/a)</td><td>119.80 (n/a)</td><td>35.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (+9.59%)</td><td>0.02 (-1.88%)</td><td>0.03 (-2.02%)</td><td>0.02 (-7.34%)</td><td>0.01 <b>(+52.76%)</b></td><td>215.60 (+7.96%)</td><td>171.72 (+4.22%)</td><td>155.00 (+2.04%)</td><td>129.10 (-8.76%)</td><td>38.10 <b>(+55.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.70 (n/a)</td><td>164.76 (n/a)</td><td>151.90 (n/a)</td><td>141.50 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.19 (+5.12%)</td><td>0.81 (-16.38%)</td><td>0.74 <b>(-21.92%)</b></td><td>0.67 (-15.11%)</td><td>0.21 <b>(+55.47%)</b></td><td>196.80 (+17.77%)</td><td>168.94 <b>(+22.62%)</b></td><td>179.60 <b>(+28.10%)</b></td><td>111.50 (-4.86%)</td><td>33.07 <b>(+67.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.13 (n/a)</td><td>0.97 (n/a)</td><td>0.94 (n/a)</td><td>0.79 (n/a)</td><td>0.13 (n/a)</td><td>167.10 (n/a)</td><td>137.78 (n/a)</td><td>140.20 (n/a)</td><td>117.20 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.00 (-2.10%)</td><td>0.83 (-10.82%)</td><td>0.83 (-10.10%)</td><td>0.61 <b>(-25.95%)</b></td><td>0.17 <b>(+118.77%)</b></td><td>217.50 <b>(+35.01%)</b></td><td>164.42 (+15.46%)</td><td>158.60 (+11.22%)</td><td>131.90 (+2.17%)</td><td>35.51 <b>(+193.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.02 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.08 (n/a)</td><td>161.10 (n/a)</td><td>142.40 (n/a)</td><td>142.60 (n/a)</td><td>129.10 (n/a)</td><td>12.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.90 (-13.85%)</td><td>0.80 (-12.75%)</td><td>0.88 (-1.45%)</td><td>0.61 <b>(-21.07%)</b></td><td>0.13 <b>(+31.81%)</b></td><td>215.00 <b>(+26.69%)</b></td><td>169.96 (+16.24%)</td><td>150.40 (+1.42%)</td><td>146.70 (+16.06%)</td><td>30.46 <b>(+90.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.04 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.78 (n/a)</td><td>0.10 (n/a)</td><td>169.70 (n/a)</td><td>146.22 (n/a)</td><td>148.30 (n/a)</td><td>126.40 (n/a)</td><td>16.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.14 (+10.99%)</td><td>0.86 (-0.24%)</td><td>0.91 (+9.73%)</td><td>0.60 (-16.42%)</td><td>0.24 <b>(+104.93%)</b></td><td>221.20 (+19.63%)</td><td>164.54 (+5.64%)</td><td>144.80 (-8.87%)</td><td>115.50 (-9.91%)</td><td>48.25 <b>(+130.77%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.71 (n/a)</td><td>0.12 (n/a)</td><td>184.90 (n/a)</td><td>155.76 (n/a)</td><td>158.90 (n/a)</td><td>128.20 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.06 (+8.48%)</td><td>0.92 (+4.70%)</td><td>0.91 (-2.20%)</td><td>0.81 (+14.79%)</td><td>0.10 (-18.52%)</td><td>163.70 (-12.88%)</td><td>144.62 (-5.20%)</td><td>144.70 (+2.26%)</td><td>124.40 (-7.85%)</td><td>14.95 <b>(-33.99%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.98 (n/a)</td><td>0.88 (n/a)</td><td>0.93 (n/a)</td><td>0.70 (n/a)</td><td>0.12 (n/a)</td><td>187.90 (n/a)</td><td>152.56 (n/a)</td><td>141.50 (n/a)</td><td>135.00 (n/a)</td><td>22.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (-11.34%)</td><td>0.03 (-1.73%)</td><td>0.03 (+16.36%)</td><td>0.02 (-15.47%)</td><td>0.00 (+1.82%)</td><td>231.60 (+18.28%)</td><td>169.70 (+2.79%)</td><td>150.20 (-14.07%)</td><td>139.70 (+12.75%)</td><td>38.44 <b>(+37.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.80 (n/a)</td><td>165.10 (n/a)</td><td>174.80 (n/a)</td><td>123.90 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (+1.63%)</td><td>0.03 (+8.55%)</td><td>0.03 (-2.95%)</td><td>0.02 <b>(+21.73%)</b></td><td>0.01 <b>(-20.94%)</b></td><td>209.20 (-17.83%)</td><td>148.82 (-10.84%)</td><td>140.90 (+3.00%)</td><td>124.30 (-1.58%)</td><td>34.98 <b>(-35.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.60 (n/a)</td><td>166.92 (n/a)</td><td>136.80 (n/a)</td><td>126.30 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.00 (-2.27%)</td><td>0.00 (+1.42%)</td><td>0.00 (+2.38%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(-69.85%)</b></td><td>974.86 (-5.60%)</td><td>953.86 (-1.77%)</td><td>949.82 (-1.75%)</td><td>947.15 (+2.28%)</td><td>11.83 <b>(-69.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.70 (n/a)</td><td>971.04 (n/a)</td><td>966.73 (n/a)</td><td>926.07 (n/a)</td><td>38.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.01 (+1.20%)</td><td>0.01 (+0.75%)</td><td>0.01 (-1.23%)</td><td>0.01 (+8.11%)</td><td>0.00 <b>(-49.80%)</b></td><td>1028.78 (-6.51%)</td><td>1016.59 (-0.56%)</td><td>1026.36 (+1.33%)</td><td>974.08 (-1.23%)</td><td>23.79 <b>(-47.41%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1100.36 (n/a)</td><td>1022.35 (n/a)</td><td>1012.87 (n/a)</td><td>986.20 (n/a)</td><td>45.23 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.97 (+0.61%)</td><td>0.95 (-0.14%)</td><td>0.96 (-0.33%)</td><td>0.94 (-0.63%)</td><td>0.01 <b>(+65.44%)</b></td><td>2233.19 (+0.64%)</td><td>2196.77 (+0.15%)</td><td>2194.22 (+0.34%)</td><td>2165.43 (-0.61%)</td><td>25.75 <b>(+65.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2219.02 (n/a)</td><td>2193.58 (n/a)</td><td>2186.78 (n/a)</td><td>2178.67 (n/a)</td><td>15.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.92 (+0.93%)</td><td>0.88 (-1.28%)</td><td>0.88 (-2.04%)</td><td>0.87 (-1.29%)</td><td>0.02 <b>(+102.07%)</b></td><td>2406.40 (+1.31%)</td><td>2373.91 (+1.33%)</td><td>2389.21 (+2.09%)</td><td>2291.31 (-0.91%)</td><td>47.46 <b>(+102.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>2375.30 (n/a)</td><td>2342.81 (n/a)</td><td>2340.37 (n/a)</td><td>2312.39 (n/a)</td><td>23.49 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.96 (-1.67%)</td><td>0.95 (-1.20%)</td><td>0.96 (-0.87%)</td><td>0.95 (-1.00%)</td><td>0.01 <b>(-24.24%)</b></td><td>2217.39 (+1.01%)</td><td>2198.61 (+1.21%)</td><td>2195.36 (+0.88%)</td><td>2176.79 (+1.71%)</td><td>15.66 <b>(-22.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2195.14 (n/a)</td><td>2172.30 (n/a)</td><td>2176.20 (n/a)</td><td>2140.29 (n/a)</td><td>20.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_weight_layout_reaches_both_gemms[b_col_maj_False]

_No metrics available._


### test_weight_layout_reaches_both_gemms[b_col_maj_True]

_No metrics available._


</details>


<details>
<summary>iron/operators/swiglu_prefill_stream</summary>


### test_swiglu_prefill_stream[k_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.39 (-3.74%)</td><td>0.38 (-2.75%)</td><td>0.38 (-1.16%)</td><td>0.37 (-2.33%)</td><td>0.01 <b>(-36.70%)</b></td><td>1403.68 (+2.37%)</td><td>1376.90 (+2.80%)</td><td>1371.38 (+1.17%)</td><td>1349.75 (+3.88%)</td><td>22.90 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1371.14 (n/a)</td><td>1339.42 (n/a)</td><td>1355.46 (n/a)</td><td>1299.29 (n/a)</td><td>33.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.25 (-1.73%)</td><td>0.24 (+1.41%)</td><td>0.24 (+2.57%)</td><td>0.24 (+3.17%)</td><td>0.01 <b>(-44.27%)</b></td><td>2205.51 (-3.07%)</td><td>2145.16 (-1.47%)</td><td>2151.48 (-2.51%)</td><td>2097.68 (+1.73%)</td><td>45.57 <b>(-44.90%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.01 (n/a)</td><td>2275.37 (n/a)</td><td>2177.27 (n/a)</td><td>2206.97 (n/a)</td><td>2062.09 (n/a)</td><td>82.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.38 (+3.47%)</td><td>0.37 (+2.33%)</td><td>0.37 (+1.61%)</td><td>0.36 (+2.68%)</td><td>0.00 <b>(+42.85%)</b></td><td>1439.29 (-2.59%)</td><td>1423.42 (-2.27%)</td><td>1428.90 (-1.59%)</td><td>1396.02 (-3.35%)</td><td>18.11 <b>(+34.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.00 (n/a)</td><td>1477.55 (n/a)</td><td>1456.43 (n/a)</td><td>1452.02 (n/a)</td><td>1444.42 (n/a)</td><td>13.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.61 (-5.55%)</td><td>0.57 (-6.53%)</td><td>0.59 (-5.42%)</td><td>0.51 (-13.04%)</td><td>0.04 <b>(+90.57%)</b></td><td>1018.60 (+14.99%)</td><td>916.34 (+7.30%)</td><td>895.60 (+5.73%)</td><td>862.30 (+5.88%)</td><td>64.96 <b>(+131.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.64 (n/a)</td><td>0.61 (n/a)</td><td>0.62 (n/a)</td><td>0.59 (n/a)</td><td>0.02 (n/a)</td><td>885.80 (n/a)</td><td>853.98 (n/a)</td><td>847.10 (n/a)</td><td>814.40 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.67 (-1.88%)</td><td>0.61 (-4.60%)</td><td>0.64 (-2.84%)</td><td>0.49 (-9.47%)</td><td>0.07 <b>(+27.99%)</b></td><td>2137.60 (+10.46%)</td><td>1744.52 (+5.41%)</td><td>1648.70 (+2.93%)</td><td>1565.60 (+1.91%)</td><td>228.99 <b>(+43.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.05 (n/a)</td><td>1935.20 (n/a)</td><td>1655.02 (n/a)</td><td>1601.80 (n/a)</td><td>1536.20 (n/a)</td><td>159.15 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.72 <b>(+20.32%)</b></td><td>3.12 (+16.02%)</td><td>3.04 (+6.32%)</td><td>2.73 <b>(+32.06%)</b></td><td>0.43 (+8.15%)</td><td>192.20 <b>(-24.30%)</b></td><td>170.32 (-14.26%)</td><td>172.50 (-5.94%)</td><td>141.00 (-16.86%)</td><td>22.57 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (n/a)</td><td>2.69 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.40 (n/a)</td><td>253.90 (n/a)</td><td>198.64 (n/a)</td><td>183.40 (n/a)</td><td>169.60 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.07 (+5.23%)</td><td>0.96 (-0.93%)</td><td>0.97 (-1.43%)</td><td>0.88 (-0.86%)</td><td>0.08 <b>(+65.48%)</b></td><td>593.00 (+0.85%)</td><td>548.24 (+1.27%)</td><td>542.70 (+1.46%)</td><td>491.40 (-4.99%)</td><td>44.34 <b>(+59.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.05 (n/a)</td><td>588.00 (n/a)</td><td>541.38 (n/a)</td><td>534.90 (n/a)</td><td>517.20 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.36 (+7.95%)</td><td>3.26 (+13.04%)</td><td>3.33 <b>(+22.37%)</b></td><td>2.38 (+18.97%)</td><td>0.79 (-14.92%)</td><td>220.70 (-15.96%)</td><td>168.40 (-14.68%)</td><td>157.40 (-18.28%)</td><td>120.30 (-7.39%)</td><td>40.78 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (n/a)</td><td>2.89 (n/a)</td><td>2.72 (n/a)</td><td>2.00 (n/a)</td><td>0.93 (n/a)</td><td>262.60 (n/a)</td><td>197.38 (n/a)</td><td>192.60 (n/a)</td><td>129.90 (n/a)</td><td>62.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>
