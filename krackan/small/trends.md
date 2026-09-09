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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (+13.58%)</td><td>0.08 (+11.56%)</td><td>0.07 (+1.84%)</td><td>0.07 (+14.35%)</td><td>0.02 <b>(+34.39%)</b></td><td>186.40 (-12.53%)</td><td>159.02 (-9.59%)</td><td>167.00 (-1.82%)</td><td>123.10 (-12.01%)</td><td>29.62 (+4.49%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.10 (n/a)</td><td>175.88 (n/a)</td><td>170.10 (n/a)</td><td>139.90 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.08 (+7.62%)</td><td>0.07 (+1.44%)</td><td>0.07 (+3.51%)</td><td>0.06 (-10.15%)</td><td>0.01 <b>(+95.73%)</b></td><td>216.80 (+11.29%)</td><td>184.22 (-0.52%)</td><td>185.80 (-3.38%)</td><td>158.00 (-7.11%)</td><td>22.90 <b>(+101.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>185.18 (n/a)</td><td>192.30 (n/a)</td><td>170.10 (n/a)</td><td>11.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 <b>(-25.27%)</b></td><td>0.06 (-6.67%)</td><td>0.06 (+5.25%)</td><td>0.04 (-0.01%)</td><td>0.01 <b>(-40.51%)</b></td><td>310.80 (+0.00%)</td><td>217.68 (+3.16%)</td><td>196.20 (-4.99%)</td><td>169.10 <b>(+33.89%)</b></td><td>55.35 (-15.71%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>310.80 (n/a)</td><td>211.02 (n/a)</td><td>206.50 (n/a)</td><td>126.30 (n/a)</td><td>65.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+12.06%)</td><td>0.05 (-3.46%)</td><td>0.04 <b>(-25.34%)</b></td><td>0.04 (+1.65%)</td><td>0.01 <b>(+51.20%)</b></td><td>303.40 (-1.62%)</td><td>246.68 (+6.39%)</td><td>277.10 <b>(+33.93%)</b></td><td>177.90 (-10.74%)</td><td>60.93 <b>(+31.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>308.40 (n/a)</td><td>231.86 (n/a)</td><td>206.90 (n/a)</td><td>199.30 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (+12.98%)</td><td>0.03 (+11.23%)</td><td>0.03 (+8.28%)</td><td>0.02 (+13.99%)</td><td>0.01 (+18.96%)</td><td>215.30 (-12.27%)</td><td>172.80 (-9.86%)</td><td>169.80 (-7.67%)</td><td>134.90 (-11.48%)</td><td>33.74 (-8.04%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>191.70 (n/a)</td><td>183.90 (n/a)</td><td>152.40 (n/a)</td><td>36.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 <b>(+27.72%)</b></td><td>0.04 <b>(+32.15%)</b></td><td>0.04 <b>(+51.26%)</b></td><td>0.03 <b>(+21.87%)</b></td><td>0.01 <b>(+48.89%)</b></td><td>193.70 (-17.92%)</td><td>150.60 <b>(-23.38%)</b></td><td>127.20 <b>(-33.85%)</b></td><td>120.40 <b>(-21.72%)</b></td><td>35.98 (-5.88%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>196.56 (n/a)</td><td>192.30 (n/a)</td><td>153.80 (n/a)</td><td>38.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 <b>(+50.43%)</b></td><td>0.04 <b>(+40.54%)</b></td><td>0.03 <b>(+26.33%)</b></td><td>0.03 <b>(+65.50%)</b></td><td>0.01 <b>(+43.49%)</b></td><td>176.90 <b>(-39.56%)</b></td><td>146.84 <b>(-29.38%)</b></td><td>161.60 <b>(-20.82%)</b></td><td>106.70 <b>(-33.52%)</b></td><td>29.47 <b>(-43.19%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>292.70 (n/a)</td><td>207.92 (n/a)</td><td>204.10 (n/a)</td><td>160.50 (n/a)</td><td>51.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (+13.41%)</td><td>0.03 <b>(+37.10%)</b></td><td>0.03 <b>(+56.61%)</b></td><td>0.03 <b>(+43.78%)</b></td><td>0.00 <b>(-27.96%)</b></td><td>187.90 <b>(-30.46%)</b></td><td>163.80 <b>(-28.53%)</b></td><td>154.80 <b>(-36.16%)</b></td><td>144.70 (-11.82%)</td><td>18.77 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.20 (n/a)</td><td>229.20 (n/a)</td><td>242.50 (n/a)</td><td>164.10 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (-13.81%)</td><td>0.03 (+16.74%)</td><td>0.03 <b>(+29.06%)</b></td><td>0.03 <b>(+54.13%)</b></td><td>0.00 <b>(-60.85%)</b></td><td>167.70 <b>(-35.13%)</b></td><td>152.62 <b>(-20.15%)</b></td><td>153.50 <b>(-22.51%)</b></td><td>126.30 (+16.08%)</td><td>16.94 <b>(-68.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.50 (n/a)</td><td>191.14 (n/a)</td><td>198.10 (n/a)</td><td>108.80 (n/a)</td><td>53.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (+17.56%)</td><td>0.03 (+16.68%)</td><td>0.03 (+11.82%)</td><td>0.03 <b>(+55.89%)</b></td><td>0.01 (-15.77%)</td><td>199.80 <b>(-35.86%)</b></td><td>166.54 (-17.40%)</td><td>156.80 (-10.60%)</td><td>131.20 (-14.92%)</td><td>27.66 <b>(-56.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>311.50 (n/a)</td><td>201.62 (n/a)</td><td>175.40 (n/a)</td><td>154.20 (n/a)</td><td>62.87 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 <b>(-25.11%)</b></td><td>0.03 (-2.24%)</td><td>0.03 (+9.83%)</td><td>0.02 (+0.71%)</td><td>0.01 <b>(-52.86%)</b></td><td>210.90 (-0.71%)</td><td>172.28 (-3.58%)</td><td>179.60 (-8.92%)</td><td>130.30 <b>(+33.50%)</b></td><td>30.03 <b>(-37.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>178.68 (n/a)</td><td>197.20 (n/a)</td><td>97.60 (n/a)</td><td>47.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (-4.12%)</td><td>0.03 (+8.95%)</td><td>0.03 (+13.94%)</td><td>0.02 (+4.17%)</td><td>0.00 <b>(-23.54%)</b></td><td>222.80 (-4.01%)</td><td>191.20 (-8.63%)</td><td>184.20 (-12.24%)</td><td>179.10 (+4.31%)</td><td>18.29 <b>(-22.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.10 (n/a)</td><td>209.26 (n/a)</td><td>209.90 (n/a)</td><td>171.70 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>164.50 (n/a)</td><td>138.18 (n/a)</td><td>124.90 (n/a)</td><td>114.70 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>160.34 (n/a)</td><td>159.00 (n/a)</td><td>131.10 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>198.00 (n/a)</td><td>158.02 (n/a)</td><td>137.00 (n/a)</td><td>121.90 (n/a)</td><td>36.41 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>175.50 (n/a)</td><td>153.68 (n/a)</td><td>160.60 (n/a)</td><td>109.30 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>159.80 (n/a)</td><td>138.30 (n/a)</td><td>133.80 (n/a)</td><td>124.30 (n/a)</td><td>13.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>153.80 (n/a)</td><td>134.48 (n/a)</td><td>131.30 (n/a)</td><td>120.00 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.70 (n/a)</td><td>162.18 (n/a)</td><td>150.40 (n/a)</td><td>122.70 (n/a)</td><td>37.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>293.90 (n/a)</td><td>188.10 (n/a)</td><td>159.80 (n/a)</td><td>142.70 (n/a)</td><td>61.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>177.64 (n/a)</td><td>175.60 (n/a)</td><td>153.20 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>181.62 (n/a)</td><td>174.90 (n/a)</td><td>156.50 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.70 (n/a)</td><td>188.50 (n/a)</td><td>194.80 (n/a)</td><td>129.90 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.60 (n/a)</td><td>181.52 (n/a)</td><td>174.10 (n/a)</td><td>160.80 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>371.90 (n/a)</td><td>201.78 (n/a)</td><td>172.30 (n/a)</td><td>135.70 (n/a)</td><td>96.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>235.10 (n/a)</td><td>197.60 (n/a)</td><td>195.90 (n/a)</td><td>174.60 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.90 (n/a)</td><td>166.50 (n/a)</td><td>157.30 (n/a)</td><td>132.10 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>201.36 (n/a)</td><td>207.40 (n/a)</td><td>122.90 (n/a)</td><td>47.19 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>4.28 (+3.14%)</td><td>4.20 (+7.32%)</td><td>4.24 (+9.66%)</td><td>4.06 (+11.97%)</td><td>0.09 <b>(-59.51%)</b></td><td>2316.80 (-10.69%)</td><td>2237.30 (-7.01%)</td><td>2217.10 (-8.81%)</td><td>2198.10 (-3.04%)</td><td>46.87 <b>(-64.62%)</b></td><td>1682.99 (+3.14%)</td><td>1654.06 (+7.32%)</td><td>1668.55 (+9.66%)</td><td>1596.74 (+11.97%)</td><td>33.94 <b>(-59.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>4.15 (n/a)</td><td>3.92 (n/a)</td><td>3.87 (n/a)</td><td>3.63 (n/a)</td><td>0.21 (n/a)</td><td>2594.20 (n/a)</td><td>2406.08 (n/a)</td><td>2431.20 (n/a)</td><td>2267.10 (n/a)</td><td>132.49 (n/a)</td><td>1631.75 (n/a)</td><td>1541.20 (n/a)</td><td>1521.63 (n/a)</td><td>1426.00 (n/a)</td><td>83.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>2.00 <b>(+100.17%)</b></td><td>1.10 <b>(+32.88%)</b></td><td>0.95 (+10.90%)</td><td>0.64 (-1.64%)</td><td>0.52 <b>(+216.82%)</b></td><td>345.10 (+1.68%)</td><td>230.68 (-16.40%)</td><td>233.80 (-9.83%)</td><td>110.70 <b>(-50.05%)</b></td><td>84.00 <b>(+48.08%)</b></td><td>85.23 <b>(+100.17%)</b></td><td>46.98 <b>(+32.88%)</b></td><td>40.36 (+10.90%)</td><td>27.35 (-1.64%)</td><td>22.29 <b>(+216.82%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.00 (n/a)</td><td>0.83 (n/a)</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>0.16 (n/a)</td><td>339.40 (n/a)</td><td>275.92 (n/a)</td><td>259.30 (n/a)</td><td>221.60 (n/a)</td><td>56.72 (n/a)</td><td>42.58 (n/a)</td><td>35.35 (n/a)</td><td>36.39 (n/a)</td><td>27.80 (n/a)</td><td>7.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.07 (-2.01%)</td><td>0.90 (-10.08%)</td><td>0.95 (-5.01%)</td><td>0.59 <b>(-31.28%)</b></td><td>0.19 <b>(+102.17%)</b></td><td>375.80 <b>(+45.55%)</b></td><td>257.82 (+15.59%)</td><td>233.20 (+5.28%)</td><td>206.80 (+2.07%)</td><td>68.95 <b>(+207.92%)</b></td><td>45.64 (-2.01%)</td><td>38.34 (-10.08%)</td><td>40.47 (-5.01%)</td><td>25.12 <b>(-31.28%)</b></td><td>8.19 <b>(+102.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.09 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.86 (n/a)</td><td>0.09 (n/a)</td><td>258.20 (n/a)</td><td>223.04 (n/a)</td><td>221.50 (n/a)</td><td>202.60 (n/a)</td><td>22.39 (n/a)</td><td>46.57 (n/a)</td><td>42.63 (n/a)</td><td>42.60 (n/a)</td><td>36.55 (n/a)</td><td>4.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.52 (+0.91%)</td><td>0.52 (+0.14%)</td><td>0.52 (+0.02%)</td><td>0.52 (-0.21%)</td><td>0.00 <b>(+565.14%)</b></td><td>48639.00 (+0.21%)</td><td>48405.48 (-0.14%)</td><td>48453.60 (-0.02%)</td><td>48005.60 (-0.90%)</td><td>236.94 <b>(+559.48%)</b></td><td>357.87 (+0.91%)</td><td>354.92 (+0.14%)</td><td>354.56 (+0.02%)</td><td>353.21 (-0.21%)</td><td>1.75 <b>(+565.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48535.20 (n/a)</td><td>48473.32 (n/a)</td><td>48463.30 (n/a)</td><td>48442.50 (n/a)</td><td>35.93 (n/a)</td><td>354.64 (n/a)</td><td>354.42 (n/a)</td><td>354.49 (n/a)</td><td>353.97 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.90 (-0.96%)</td><td>0.89 (-0.71%)</td><td>0.88 (-0.90%)</td><td>0.87 (-0.76%)</td><td>0.01 (-3.93%)</td><td>28772.60 (+0.77%)</td><td>28407.86 (+0.71%)</td><td>28483.30 (+0.91%)</td><td>28066.00 (+0.97%)</td><td>270.15 (-2.19%)</td><td>612.12 (-0.96%)</td><td>604.80 (-0.71%)</td><td>603.16 (-0.90%)</td><td>597.09 (-0.76%)</td><td>5.75 (-3.93%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>28553.10 (n/a)</td><td>28207.40 (n/a)</td><td>28226.60 (n/a)</td><td>27795.20 (n/a)</td><td>276.21 (n/a)</td><td>618.09 (n/a)</td><td>609.10 (n/a)</td><td>608.64 (n/a)</td><td>601.68 (n/a)</td><td>5.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.31 (+0.97%)</td><td>3.22 (+0.89%)</td><td>3.19 (+0.38%)</td><td>3.16 (+0.27%)</td><td>0.07 <b>(+40.12%)</b></td><td>7970.60 (-0.27%)</td><td>7819.24 (-0.87%)</td><td>7895.50 (-0.38%)</td><td>7598.40 (-0.96%)</td><td>174.95 <b>(+38.99%)</b></td><td>2260.97 (+0.97%)</td><td>2198.01 (+0.89%)</td><td>2175.91 (+0.38%)</td><td>2155.39 (+0.27%)</td><td>49.56 <b>(+40.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.28 (n/a)</td><td>3.19 (n/a)</td><td>3.18 (n/a)</td><td>3.15 (n/a)</td><td>0.05 (n/a)</td><td>7992.20 (n/a)</td><td>7887.64 (n/a)</td><td>7925.60 (n/a)</td><td>7672.10 (n/a)</td><td>125.87 (n/a)</td><td>2239.28 (n/a)</td><td>2178.54 (n/a)</td><td>2167.65 (n/a)</td><td>2149.59 (n/a)</td><td>35.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.76 (-0.00%)</td><td>3.50 (+0.92%)</td><td>3.51 (-1.32%)</td><td>3.19 (+4.63%)</td><td>0.22 (-17.94%)</td><td>2523.10 (-4.43%)</td><td>2308.28 (-1.09%)</td><td>2299.70 (+1.34%)</td><td>2143.20 (+0.00%)</td><td>144.80 <b>(-22.48%)</b></td><td>986.32 (-0.00%)</td><td>918.62 (+0.92%)</td><td>919.20 (-1.32%)</td><td>837.83 (+4.63%)</td><td>56.46 (-17.94%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.76 (n/a)</td><td>3.47 (n/a)</td><td>3.55 (n/a)</td><td>3.05 (n/a)</td><td>0.26 (n/a)</td><td>2640.00 (n/a)</td><td>2333.66 (n/a)</td><td>2269.40 (n/a)</td><td>2143.20 (n/a)</td><td>186.78 (n/a)</td><td>986.33 (n/a)</td><td>910.24 (n/a)</td><td>931.50 (n/a)</td><td>800.74 (n/a)</td><td>68.80 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.53 <b>(+50.91%)</b></td><td>0.35 (+8.59%)</td><td>0.31 (-5.95%)</td><td>0.29 (+4.41%)</td><td>0.10 <b>(+222.98%)</b></td><td>4325.10 (-4.23%)</td><td>3735.86 (-3.97%)</td><td>3968.60 (+6.33%)</td><td>2362.80 <b>(-33.73%)</b></td><td>798.42 <b>(+99.93%)</b></td><td>28.40 <b>(+50.91%)</b></td><td>18.88 (+8.59%)</td><td>16.91 (-5.95%)</td><td>15.52 (+4.41%)</td><td>5.40 <b>(+222.98%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.03 (n/a)</td><td>4516.00 (n/a)</td><td>3890.14 (n/a)</td><td>3732.50 (n/a)</td><td>3565.60 (n/a)</td><td>399.35 (n/a)</td><td>18.82 (n/a)</td><td>17.39 (n/a)</td><td>17.98 (n/a)</td><td>14.86 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>6.43 <b>(+33.22%)</b></td><td>5.15 <b>(+29.33%)</b></td><td>4.91 <b>(+37.55%)</b></td><td>4.55 <b>(+38.86%)</b></td><td>0.75 (-0.28%)</td><td>1462.30 <b>(-27.98%)</b></td><td>1311.20 <b>(-23.63%)</b></td><td>1354.40 <b>(-27.30%)</b></td><td>1033.90 <b>(-24.94%)</b></td><td>165.48 <b>(-45.96%)</b></td><td>1987.75 <b>(+33.22%)</b></td><td>1590.61 <b>(+29.33%)</b></td><td>1517.47 <b>(+37.55%)</b></td><td>1405.51 <b>(+38.86%)</b></td><td>230.58 (-0.27%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>4.83 (n/a)</td><td>3.98 (n/a)</td><td>3.57 (n/a)</td><td>3.28 (n/a)</td><td>0.75 (n/a)</td><td>2030.50 (n/a)</td><td>1717.00 (n/a)</td><td>1863.00 (n/a)</td><td>1377.40 (n/a)</td><td>306.22 (n/a)</td><td>1492.11 (n/a)</td><td>1229.91 (n/a)</td><td>1103.18 (n/a)</td><td>1012.15 (n/a)</td><td>231.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>13.38 (n/a)</td><td>12.52 (n/a)</td><td>12.96 (n/a)</td><td>10.48 (n/a)</td><td>1.18 (n/a)</td><td>13.37 (n/a)</td><td>12.51 (n/a)</td><td>12.95 (n/a)</td><td>10.47 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>24.90 (+2.00%)</td><td>22.30 (-7.16%)</td><td>23.98 (-0.42%)</td><td>17.05 <b>(-27.86%)</b></td><td>3.29 <b>(+1032.24%)</b></td><td>24.89 (+2.00%)</td><td>22.29 (-7.16%)</td><td>23.97 (-0.42%)</td><td>17.04 <b>(-27.86%)</b></td><td>3.29 <b>(+1032.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>24.42 (n/a)</td><td>24.02 (n/a)</td><td>24.08 (n/a)</td><td>23.63 (n/a)</td><td>0.29 (n/a)</td><td>24.40 (n/a)</td><td>24.01 (n/a)</td><td>24.07 (n/a)</td><td>23.62 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>41.22 (+0.38%)</td><td>38.91 (-1.83%)</td><td>40.09 (+1.47%)</td><td>33.30 (-12.64%)</td><td>3.18 <b>(+182.76%)</b></td><td>41.19 (+0.38%)</td><td>38.89 (-1.83%)</td><td>40.06 (+1.47%)</td><td>33.27 (-12.64%)</td><td>3.18 <b>(+182.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>41.06 (n/a)</td><td>39.63 (n/a)</td><td>39.51 (n/a)</td><td>38.11 (n/a)</td><td>1.13 (n/a)</td><td>41.04 (n/a)</td><td>39.61 (n/a)</td><td>39.48 (n/a)</td><td>38.09 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>46.51 (+6.30%)</td><td>42.61 (+2.97%)</td><td>42.69 (+1.72%)</td><td>36.56 (-1.46%)</td><td>3.82 <b>(+51.76%)</b></td><td>46.48 (+6.30%)</td><td>42.58 (+2.97%)</td><td>42.66 (+1.72%)</td><td>36.54 (-1.46%)</td><td>3.82 <b>(+51.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>43.75 (n/a)</td><td>41.38 (n/a)</td><td>41.97 (n/a)</td><td>37.10 (n/a)</td><td>2.52 (n/a)</td><td>43.72 (n/a)</td><td>41.36 (n/a)</td><td>41.94 (n/a)</td><td>37.08 (n/a)</td><td>2.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>13.32 (n/a)</td><td>12.80 (n/a)</td><td>13.03 (n/a)</td><td>12.24 (n/a)</td><td>0.52 (n/a)</td><td>13.31 (n/a)</td><td>12.79 (n/a)</td><td>13.02 (n/a)</td><td>12.23 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>24.26 (-2.14%)</td><td>23.22 (-3.75%)</td><td>22.88 (-6.01%)</td><td>22.10 (-3.84%)</td><td>0.95 <b>(+32.92%)</b></td><td>24.24 (-2.14%)</td><td>23.20 (-3.75%)</td><td>22.87 (-6.01%)</td><td>22.09 (-3.84%)</td><td>0.95 <b>(+32.92%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>24.79 (n/a)</td><td>24.12 (n/a)</td><td>24.34 (n/a)</td><td>22.98 (n/a)</td><td>0.71 (n/a)</td><td>24.77 (n/a)</td><td>24.11 (n/a)</td><td>24.33 (n/a)</td><td>22.97 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>40.61 (-4.47%)</td><td>36.59 (-9.04%)</td><td>38.07 (-4.59%)</td><td>31.24 (-19.59%)</td><td>4.02 <b>(+193.05%)</b></td><td>40.59 (-4.47%)</td><td>36.57 (-9.04%)</td><td>38.04 (-4.59%)</td><td>31.22 (-19.59%)</td><td>4.02 <b>(+193.05%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>42.51 (n/a)</td><td>40.23 (n/a)</td><td>39.90 (n/a)</td><td>38.85 (n/a)</td><td>1.37 (n/a)</td><td>42.49 (n/a)</td><td>40.20 (n/a)</td><td>39.87 (n/a)</td><td>38.82 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>45.24 (-0.93%)</td><td>42.34 (+1.01%)</td><td>42.96 (+2.49%)</td><td>37.84 (-0.91%)</td><td>3.06 (+15.17%)</td><td>45.21 (-0.93%)</td><td>42.31 (+1.01%)</td><td>42.94 (+2.49%)</td><td>37.82 (-0.91%)</td><td>3.06 (+15.17%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>45.66 (n/a)</td><td>41.91 (n/a)</td><td>41.92 (n/a)</td><td>38.19 (n/a)</td><td>2.65 (n/a)</td><td>45.64 (n/a)</td><td>41.89 (n/a)</td><td>41.89 (n/a)</td><td>38.16 (n/a)</td><td>2.65 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>9.70 (+4.81%)</td><td>9.05 (+2.09%)</td><td>8.94 (-0.66%)</td><td>8.50 (+2.53%)</td><td>0.45 (+18.33%)</td><td>9.68 (+4.81%)</td><td>9.03 (+2.09%)</td><td>8.93 (-0.66%)</td><td>8.48 (+2.53%)</td><td>0.45 (+18.33%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>9.25 (n/a)</td><td>8.87 (n/a)</td><td>9.00 (n/a)</td><td>8.29 (n/a)</td><td>0.38 (n/a)</td><td>9.23 (n/a)</td><td>8.85 (n/a)</td><td>8.99 (n/a)</td><td>8.27 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.98 (+6.12%)</td><td>0.87 (-0.06%)</td><td>0.84 (-3.50%)</td><td>0.78 (-1.44%)</td><td>0.08 <b>(+47.81%)</b></td><td>0.96 (+6.12%)</td><td>0.86 (-0.06%)</td><td>0.83 (-3.50%)</td><td>0.77 (-1.44%)</td><td>0.08 <b>(+47.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.92 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.78 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.33 (+0.01%)</td><td>1.10 (-3.15%)</td><td>1.08 (-5.82%)</td><td>0.98 (-2.34%)</td><td>0.14 (+7.65%)</td><td>1.31 (+0.01%)</td><td>1.09 (-3.15%)</td><td>1.06 (-5.82%)</td><td>0.97 (-2.34%)</td><td>0.14 (+7.65%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.33 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.01 (n/a)</td><td>0.13 (n/a)</td><td>1.31 (n/a)</td><td>1.12 (n/a)</td><td>1.13 (n/a)</td><td>0.99 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>18.25 (+1.84%)</td><td>16.88 (+0.46%)</td><td>16.67 (+2.07%)</td><td>15.39 (-3.96%)</td><td>1.19 <b>(+33.98%)</b></td><td>18.04 (+1.84%)</td><td>16.68 (+0.46%)</td><td>16.48 (+2.07%)</td><td>15.21 (-3.96%)</td><td>1.18 <b>(+33.98%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>17.92 (n/a)</td><td>16.80 (n/a)</td><td>16.33 (n/a)</td><td>16.02 (n/a)</td><td>0.89 (n/a)</td><td>17.72 (n/a)</td><td>16.60 (n/a)</td><td>16.15 (n/a)</td><td>15.84 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>14.16 (+0.10%)</td><td>12.85 (-2.66%)</td><td>13.79 (+3.21%)</td><td>8.71 <b>(-25.71%)</b></td><td>2.34 <b>(+156.72%)</b></td><td>13.91 (+0.10%)</td><td>12.63 (-2.66%)</td><td>13.54 (+3.21%)</td><td>8.55 <b>(-25.71%)</b></td><td>2.29 <b>(+156.72%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>14.15 (n/a)</td><td>13.20 (n/a)</td><td>13.36 (n/a)</td><td>11.72 (n/a)</td><td>0.91 (n/a)</td><td>13.90 (n/a)</td><td>12.97 (n/a)</td><td>13.12 (n/a)</td><td>11.52 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>10.45 <b>(+23.95%)</b></td><td>8.07 (+0.17%)</td><td>7.12 (-12.45%)</td><td>6.77 (-9.30%)</td><td>1.62 <b>(+351.36%)</b></td><td>10.27 <b>(+23.95%)</b></td><td>7.93 (+0.17%)</td><td>7.00 (-12.45%)</td><td>6.66 (-9.30%)</td><td>1.59 <b>(+351.36%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>8.43 (n/a)</td><td>8.06 (n/a)</td><td>8.13 (n/a)</td><td>7.47 (n/a)</td><td>0.36 (n/a)</td><td>8.29 (n/a)</td><td>7.92 (n/a)</td><td>7.99 (n/a)</td><td>7.34 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>6.40 (+6.92%)</td><td>5.56 (-0.93%)</td><td>5.60 (-0.53%)</td><td>4.79 (-9.31%)</td><td>0.63 <b>(+138.04%)</b></td><td>6.30 (+6.92%)</td><td>5.47 (-0.93%)</td><td>5.51 (-0.53%)</td><td>4.72 (-9.31%)</td><td>0.62 <b>(+138.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>5.98 (n/a)</td><td>5.61 (n/a)</td><td>5.63 (n/a)</td><td>5.29 (n/a)</td><td>0.26 (n/a)</td><td>5.89 (n/a)</td><td>5.52 (n/a)</td><td>5.54 (n/a)</td><td>5.20 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>12.94 (n/a)</td><td>12.40 (n/a)</td><td>12.58 (n/a)</td><td>11.57 (n/a)</td><td>0.56 (n/a)</td><td>12.93 (n/a)</td><td>12.39 (n/a)</td><td>12.58 (n/a)</td><td>11.57 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>13.26 (n/a)</td><td>12.17 (n/a)</td><td>11.61 (n/a)</td><td>11.45 (n/a)</td><td>0.90 (n/a)</td><td>13.25 (n/a)</td><td>12.16 (n/a)</td><td>11.61 (n/a)</td><td>11.45 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>162.06 (n/a)</td><td>162.60 (n/a)</td><td>135.50 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>181.30 (n/a)</td><td>187.70 (n/a)</td><td>146.90 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>248.30 (n/a)</td><td>156.20 (n/a)</td><td>133.90 (n/a)</td><td>100.90 (n/a)</td><td>62.34 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>171.72 (n/a)</td><td>159.90 (n/a)</td><td>144.40 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>173.68 (n/a)</td><td>169.80 (n/a)</td><td>134.40 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.40 (n/a)</td><td>199.20 (n/a)</td><td>185.70 (n/a)</td><td>135.10 (n/a)</td><td>57.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>191.18 (n/a)</td><td>203.70 (n/a)</td><td>150.70 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>417.50 (n/a)</td><td>281.28 (n/a)</td><td>236.10 (n/a)</td><td>190.80 (n/a)</td><td>94.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (+0.34%)</td><td>0.04 (-5.58%)</td><td>0.04 (-5.24%)</td><td>0.04 (-12.48%)</td><td>0.01 <b>(+26.49%)</b></td><td>230.50 (+14.22%)</td><td>195.48 (+7.36%)</td><td>202.50 (+5.52%)</td><td>139.80 (-0.36%)</td><td>35.36 <b>(+44.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>182.08 (n/a)</td><td>191.90 (n/a)</td><td>140.30 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 <b>(+28.99%)</b></td><td>0.05 (+11.01%)</td><td>0.05 (+11.98%)</td><td>0.04 (+4.24%)</td><td>0.01 <b>(+90.80%)</b></td><td>203.90 (-4.05%)</td><td>168.24 (-7.48%)</td><td>168.20 (-10.67%)</td><td>112.10 <b>(-22.48%)</b></td><td>35.13 <b>(+39.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>181.84 (n/a)</td><td>188.30 (n/a)</td><td>144.60 (n/a)</td><td>25.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 <b>(+38.04%)</b></td><td>0.05 (+14.20%)</td><td>0.05 (+6.26%)</td><td>0.04 (-0.71%)</td><td>0.01 <b>(+475.25%)</b></td><td>186.40 (+0.70%)</td><td>156.54 (-10.46%)</td><td>161.80 (-5.88%)</td><td>122.90 <b>(-27.54%)</b></td><td>25.95 <b>(+315.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.10 (n/a)</td><td>174.82 (n/a)</td><td>171.90 (n/a)</td><td>169.60 (n/a)</td><td>6.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (-13.61%)</td><td>0.04 (-17.42%)</td><td>0.05 (-12.05%)</td><td>0.03 <b>(-22.70%)</b></td><td>0.01 (-18.17%)</td><td>234.50 <b>(+29.34%)</b></td><td>188.50 <b>(+21.11%)</b></td><td>181.80 (+13.70%)</td><td>150.10 (+15.73%)</td><td>30.61 <b>(+25.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>155.64 (n/a)</td><td>159.90 (n/a)</td><td>129.70 (n/a)</td><td>24.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (-11.93%)</td><td>0.05 (+1.69%)</td><td>0.06 (+17.95%)</td><td>0.04 (-12.90%)</td><td>0.01 (-19.93%)</td><td>209.60 (+14.79%)</td><td>155.86 (-2.05%)</td><td>144.90 (-15.21%)</td><td>122.50 (+13.64%)</td><td>32.95 (+11.56%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>159.12 (n/a)</td><td>170.90 (n/a)</td><td>107.80 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+1.14%)</td><td>0.05 (+4.58%)</td><td>0.05 <b>(+26.06%)</b></td><td>0.03 (-16.31%)</td><td>0.02 (+15.92%)</td><td>237.40 (+19.48%)</td><td>169.34 (-1.82%)</td><td>149.80 <b>(-20.66%)</b></td><td>111.70 (-1.06%)</td><td>50.12 <b>(+42.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>172.48 (n/a)</td><td>188.80 (n/a)</td><td>112.90 (n/a)</td><td>35.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (-13.08%)</td><td>0.04 (-14.42%)</td><td>0.05 (+0.41%)</td><td>0.03 (-18.56%)</td><td>0.01 (-7.65%)</td><td>250.80 <b>(+22.82%)</b></td><td>196.32 (+17.91%)</td><td>181.40 (-0.44%)</td><td>143.60 (+15.06%)</td><td>46.31 <b>(+36.78%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.20 (n/a)</td><td>166.50 (n/a)</td><td>182.20 (n/a)</td><td>124.80 (n/a)</td><td>33.85 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+10.15%)</td><td>0.05 (+6.08%)</td><td>0.05 (+0.06%)</td><td>0.04 (+6.12%)</td><td>0.01 <b>(+21.81%)</b></td><td>192.20 (-5.78%)</td><td>167.66 (-5.20%)</td><td>174.10 (-0.11%)</td><td>122.40 (-9.27%)</td><td>28.45 (+4.33%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>176.86 (n/a)</td><td>174.30 (n/a)</td><td>134.90 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (+11.42%)</td><td>0.04 (-6.70%)</td><td>0.04 (-5.11%)</td><td>0.03 <b>(-20.48%)</b></td><td>0.01 <b>(+66.23%)</b></td><td>270.00 <b>(+25.76%)</b></td><td>199.48 (+11.04%)</td><td>197.00 (+5.40%)</td><td>133.20 (-10.24%)</td><td>49.90 <b>(+87.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>179.64 (n/a)</td><td>186.90 (n/a)</td><td>148.40 (n/a)</td><td>26.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (+11.30%)</td><td>0.04 (-6.07%)</td><td>0.04 (-6.48%)</td><td>0.03 <b>(-29.29%)</b></td><td>0.01 <b>(+179.75%)</b></td><td>313.40 <b>(+41.43%)</b></td><td>232.72 (+10.49%)</td><td>231.20 (+6.94%)</td><td>166.80 (-10.13%)</td><td>53.29 <b>(+256.94%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>210.62 (n/a)</td><td>216.20 (n/a)</td><td>185.60 (n/a)</td><td>14.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (-15.49%)</td><td>0.05 (-14.94%)</td><td>0.05 (-10.74%)</td><td>0.03 <b>(-34.61%)</b></td><td>0.01 <b>(+28.61%)</b></td><td>242.40 <b>(+52.93%)</b></td><td>174.80 <b>(+20.67%)</b></td><td>166.30 (+12.06%)</td><td>136.90 (+18.32%)</td><td>41.20 <b>(+142.45%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>158.50 (n/a)</td><td>144.86 (n/a)</td><td>148.40 (n/a)</td><td>115.70 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (+6.92%)</td><td>0.04 (-2.90%)</td><td>0.04 (-12.49%)</td><td>0.03 (-14.01%)</td><td>0.01 <b>(+111.19%)</b></td><td>235.30 (+16.31%)</td><td>192.82 (+4.69%)</td><td>201.80 (+14.27%)</td><td>161.30 (-6.49%)</td><td>31.18 <b>(+123.23%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>184.18 (n/a)</td><td>176.60 (n/a)</td><td>172.50 (n/a)</td><td>13.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 <b>(-24.69%)</b></td><td>0.05 (-17.46%)</td><td>0.04 (-18.92%)</td><td>0.04 <b>(-22.43%)</b></td><td>0.01 <b>(-25.17%)</b></td><td>222.60 <b>(+28.89%)</b></td><td>177.72 <b>(+21.10%)</b></td><td>187.10 <b>(+23.34%)</b></td><td>134.60 <b>(+32.74%)</b></td><td>35.56 <b>(+32.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.70 (n/a)</td><td>146.76 (n/a)</td><td>151.70 (n/a)</td><td>101.40 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 <b>(-29.42%)</b></td><td>0.04 (-13.92%)</td><td>0.05 (-1.13%)</td><td>0.03 (-11.91%)</td><td>0.01 <b>(-45.27%)</b></td><td>258.20 (+13.54%)</td><td>198.72 (+12.86%)</td><td>180.10 (+1.18%)</td><td>159.10 <b>(+41.67%)</b></td><td>40.15 (-9.20%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>176.08 (n/a)</td><td>178.00 (n/a)</td><td>112.30 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (+5.44%)</td><td>0.05 (-2.65%)</td><td>0.05 (-5.70%)</td><td>0.04 (-8.39%)</td><td>0.01 <b>(+92.21%)</b></td><td>191.90 (+9.16%)</td><td>161.88 (+5.04%)</td><td>166.20 (+6.06%)</td><td>128.80 (-5.15%)</td><td>30.71 <b>(+98.96%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>154.12 (n/a)</td><td>156.70 (n/a)</td><td>135.80 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (-13.01%)</td><td>0.05 (-1.82%)</td><td>0.05 (-6.49%)</td><td>0.04 (+7.67%)</td><td>0.01 <b>(-39.94%)</b></td><td>215.20 (-7.12%)</td><td>170.44 (-1.01%)</td><td>167.40 (+6.96%)</td><td>143.00 (+14.95%)</td><td>27.40 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>172.18 (n/a)</td><td>156.50 (n/a)</td><td>124.40 (n/a)</td><td>42.48 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 <b>(-22.44%)</b></td><td>0.04 <b>(-21.75%)</b></td><td>0.04 (-14.08%)</td><td>0.03 <b>(-34.34%)</b></td><td>0.01 (-9.39%)</td><td>298.90 <b>(+52.34%)</b></td><td>210.50 <b>(+30.36%)</b></td><td>194.00 (+16.38%)</td><td>150.90 <b>(+28.97%)</b></td><td>55.01 <b>(+88.25%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>161.48 (n/a)</td><td>166.70 (n/a)</td><td>117.00 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (-15.48%)</td><td>0.04 <b>(-22.04%)</b></td><td>0.04 <b>(-22.12%)</b></td><td>0.02 <b>(-43.14%)</b></td><td>0.01 <b>(+65.10%)</b></td><td>332.00 <b>(+75.85%)</b></td><td>220.26 <b>(+34.39%)</b></td><td>203.10 <b>(+28.38%)</b></td><td>172.70 (+18.37%)</td><td>65.54 <b>(+247.71%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>163.90 (n/a)</td><td>158.20 (n/a)</td><td>145.90 (n/a)</td><td>18.85 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.18 (-0.42%)</td><td>0.18 (+0.02%)</td><td>0.18 (+0.11%)</td><td>0.18 (+0.21%)</td><td>0.00 <b>(-51.18%)</b></td><td>47440.20 (-0.21%)</td><td>47321.42 (-0.02%)</td><td>47342.10 (-0.11%)</td><td>47142.90 (+0.42%)</td><td>113.95 <b>(-51.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47542.10 (n/a)</td><td>47332.68 (n/a)</td><td>47396.40 (n/a)</td><td>46945.00 (n/a)</td><td>232.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.16 (-13.95%)</td><td>0.14 (-8.95%)</td><td>0.14 (-13.23%)</td><td>0.10 (+3.81%)</td><td>0.03 <b>(-26.15%)</b></td><td>234.30 (-3.66%)</td><td>186.62 (+7.84%)</td><td>180.30 (+15.28%)</td><td>149.30 (+16.28%)</td><td>35.77 (-19.49%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>243.20 (n/a)</td><td>173.06 (n/a)</td><td>156.40 (n/a)</td><td>128.40 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.32 (-2.14%)</td><td>0.24 (-2.64%)</td><td>0.23 (-5.28%)</td><td>0.20 (+2.13%)</td><td>0.05 (-0.78%)</td><td>207.30 (-2.08%)</td><td>176.40 (+2.77%)</td><td>179.10 (+5.60%)</td><td>127.60 (+2.16%)</td><td>31.82 (+1.70%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>211.70 (n/a)</td><td>171.64 (n/a)</td><td>169.60 (n/a)</td><td>124.90 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 <b>(+26.55%)</b></td><td>0.03 (-5.48%)</td><td>0.03 (-13.05%)</td><td>0.02 <b>(-25.07%)</b></td><td>0.01 <b>(+144.86%)</b></td><td>259.70 <b>(+33.45%)</b></td><td>189.64 (+14.82%)</td><td>195.20 (+14.96%)</td><td>109.60 <b>(-20.98%)</b></td><td>61.47 <b>(+162.99%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>165.16 (n/a)</td><td>169.80 (n/a)</td><td>138.70 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+2.35%)</td><td>0.05 (-0.22%)</td><td>0.05 (-11.95%)</td><td>0.04 <b>(+36.80%)</b></td><td>0.01 <b>(-22.98%)</b></td><td>216.50 <b>(-26.91%)</b></td><td>166.32 (-5.12%)</td><td>168.10 (+13.58%)</td><td>122.60 (-2.31%)</td><td>36.62 <b>(-47.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.20 (n/a)</td><td>175.30 (n/a)</td><td>148.00 (n/a)</td><td>125.50 (n/a)</td><td>69.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.09 (-17.07%)</td><td>0.08 (-3.82%)</td><td>0.08 (+10.92%)</td><td>0.05 (-10.33%)</td><td>0.02 (-15.45%)</td><td>239.40 (+11.50%)</td><td>167.58 (+3.88%)</td><td>148.80 (-9.82%)</td><td>134.40 <b>(+20.54%)</b></td><td>43.96 (+14.37%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.70 (n/a)</td><td>161.32 (n/a)</td><td>165.00 (n/a)</td><td>111.50 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 <b>(+30.71%)</b></td><td>0.05 (+14.77%)</td><td>0.05 (+1.00%)</td><td>0.03 <b>(+24.67%)</b></td><td>0.01 <b>(+28.59%)</b></td><td>263.10 (-19.79%)</td><td>172.14 (-13.17%)</td><td>169.80 (-0.99%)</td><td>116.30 <b>(-23.54%)</b></td><td>55.86 <b>(-23.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.00 (n/a)</td><td>198.26 (n/a)</td><td>171.50 (n/a)</td><td>152.10 (n/a)</td><td>73.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.08 (+10.25%)</td><td>0.07 (+18.34%)</td><td>0.06 (+15.80%)</td><td>0.06 <b>(+21.40%)</b></td><td>0.01 (+4.64%)</td><td>184.90 (-17.60%)</td><td>157.90 (-15.80%)</td><td>167.10 (-13.64%)</td><td>126.20 (-9.27%)</td><td>24.94 (-19.66%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>187.52 (n/a)</td><td>193.50 (n/a)</td><td>139.10 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 <b>(-22.95%)</b></td><td>0.05 (-18.81%)</td><td>0.05 <b>(-23.87%)</b></td><td>0.05 (-10.07%)</td><td>0.00 <b>(-60.80%)</b></td><td>178.00 (+11.18%)</td><td>163.56 <b>(+21.61%)</b></td><td>160.10 <b>(+31.34%)</b></td><td>152.60 <b>(+29.87%)</b></td><td>11.19 <b>(-43.47%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>160.10 (n/a)</td><td>134.50 (n/a)</td><td>121.90 (n/a)</td><td>117.50 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 <b>(-23.38%)</b></td><td>0.06 (-11.86%)</td><td>0.06 (+14.01%)</td><td>0.04 (-10.95%)</td><td>0.01 <b>(-43.24%)</b></td><td>248.80 (+12.33%)</td><td>184.78 (+9.92%)</td><td>161.10 (-12.25%)</td><td>157.10 <b>(+30.59%)</b></td><td>39.67 (-13.00%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>221.50 (n/a)</td><td>168.10 (n/a)</td><td>183.60 (n/a)</td><td>120.30 (n/a)</td><td>45.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (-3.69%)</td><td>0.05 (-19.52%)</td><td>0.05 <b>(-24.53%)</b></td><td>0.03 <b>(-31.54%)</b></td><td>0.01 <b>(+54.08%)</b></td><td>234.60 <b>(+46.08%)</b></td><td>177.10 <b>(+28.00%)</b></td><td>172.70 <b>(+32.44%)</b></td><td>128.80 (+3.87%)</td><td>40.39 <b>(+135.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>160.60 (n/a)</td><td>138.36 (n/a)</td><td>130.40 (n/a)</td><td>124.00 (n/a)</td><td>17.13 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+5.62%)</td><td>0.05 (+1.54%)</td><td>0.05 (+4.18%)</td><td>0.03 <b>(-21.21%)</b></td><td>0.02 <b>(+46.79%)</b></td><td>289.40 <b>(+26.93%)</b></td><td>195.84 (+4.31%)</td><td>192.00 (-4.00%)</td><td>129.30 (-5.34%)</td><td>69.32 <b>(+64.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>187.74 (n/a)</td><td>200.00 (n/a)</td><td>136.60 (n/a)</td><td>42.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (+15.98%)</td><td>0.04 <b>(-23.60%)</b></td><td>0.04 <b>(-32.00%)</b></td><td>0.02 <b>(-54.99%)</b></td><td>0.02 <b>(+290.69%)</b></td><td>422.40 <b>(+122.20%)</b></td><td>247.62 <b>(+49.33%)</b></td><td>233.30 <b>(+47.10%)</b></td><td>134.80 (-13.76%)</td><td>107.51 <b>(+660.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.10 (n/a)</td><td>165.82 (n/a)</td><td>158.60 (n/a)</td><td>156.30 (n/a)</td><td>14.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (+1.62%)</td><td>0.05 (-2.57%)</td><td>0.05 (+10.04%)</td><td>0.03 <b>(-28.52%)</b></td><td>0.01 <b>(+26.30%)</b></td><td>310.30 <b>(+39.90%)</b></td><td>193.48 (+7.32%)</td><td>171.00 (-9.14%)</td><td>130.60 (-1.58%)</td><td>68.74 <b>(+84.75%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>180.28 (n/a)</td><td>188.20 (n/a)</td><td>132.70 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (-5.82%)</td><td>0.04 (-12.73%)</td><td>0.03 (-18.67%)</td><td>0.03 (-17.77%)</td><td>0.01 <b>(+22.36%)</b></td><td>321.00 <b>(+21.64%)</b></td><td>243.12 (+17.22%)</td><td>239.40 <b>(+22.96%)</b></td><td>180.40 (+6.18%)</td><td>59.93 <b>(+55.18%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.90 (n/a)</td><td>207.40 (n/a)</td><td>194.70 (n/a)</td><td>169.90 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 <b>(+34.24%)</b></td><td>0.04 (+16.08%)</td><td>0.04 (+6.00%)</td><td>0.04 <b>(+36.59%)</b></td><td>0.01 <b>(+49.43%)</b></td><td>231.50 <b>(-26.79%)</b></td><td>205.82 (-13.35%)</td><td>217.80 (-5.67%)</td><td>138.40 <b>(-25.51%)</b></td><td>38.80 <b>(-21.41%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.20 (n/a)</td><td>237.54 (n/a)</td><td>230.90 (n/a)</td><td>185.80 (n/a)</td><td>49.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (-5.86%)</td><td>0.05 (-10.91%)</td><td>0.04 <b>(-21.43%)</b></td><td>0.03 (-2.57%)</td><td>0.01 (-5.74%)</td><td>258.00 (+2.63%)</td><td>186.52 (+11.84%)</td><td>185.30 <b>(+27.27%)</b></td><td>134.90 (+6.22%)</td><td>51.69 (-0.18%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.40 (n/a)</td><td>166.78 (n/a)</td><td>145.60 (n/a)</td><td>127.00 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (+8.79%)</td><td>0.04 (+6.66%)</td><td>0.05 (+10.13%)</td><td>0.02 (-8.92%)</td><td>0.01 <b>(+44.29%)</b></td><td>353.60 (+9.78%)</td><td>216.06 (-1.89%)</td><td>189.60 (-9.20%)</td><td>152.10 (-8.10%)</td><td>82.54 <b>(+38.29%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>322.10 (n/a)</td><td>220.22 (n/a)</td><td>208.80 (n/a)</td><td>165.50 (n/a)</td><td>59.69 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (-1.49%)</td><td>0.04 (-2.90%)</td><td>0.04 (-5.16%)</td><td>0.04 (+1.29%)</td><td>0.00 <b>(-20.56%)</b></td><td>230.80 (-1.24%)</td><td>214.24 (+2.77%)</td><td>215.20 (+5.49%)</td><td>194.50 (+1.51%)</td><td>14.51 (-19.76%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>208.46 (n/a)</td><td>204.00 (n/a)</td><td>191.60 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.68 (-15.93%)</td><td>0.60 (-7.01%)</td><td>0.61 (+5.75%)</td><td>0.54 (+10.10%)</td><td>0.06 <b>(-61.08%)</b></td><td>180.60 (-9.15%)</td><td>164.74 (+4.24%)</td><td>161.10 (-5.40%)</td><td>144.20 (+18.98%)</td><td>14.80 <b>(-55.90%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.81 (n/a)</td><td>0.65 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.14 (n/a)</td><td>198.80 (n/a)</td><td>158.04 (n/a)</td><td>170.30 (n/a)</td><td>121.20 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.78 (-3.14%)</td><td>0.62 (-5.50%)</td><td>0.58 <b>(-22.17%)</b></td><td>0.54 (+15.17%)</td><td>0.10 <b>(-38.15%)</b></td><td>182.50 (-13.18%)</td><td>161.98 (+2.14%)</td><td>169.90 <b>(+28.42%)</b></td><td>126.20 (+3.27%)</td><td>23.11 <b>(-45.43%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.80 (n/a)</td><td>0.65 (n/a)</td><td>0.74 (n/a)</td><td>0.47 (n/a)</td><td>0.16 (n/a)</td><td>210.20 (n/a)</td><td>158.58 (n/a)</td><td>132.30 (n/a)</td><td>122.20 (n/a)</td><td>42.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.70 (-4.69%)</td><td>0.59 (-7.11%)</td><td>0.61 (-5.08%)</td><td>0.39 (-18.21%)</td><td>0.13 <b>(+21.01%)</b></td><td>252.20 <b>(+22.31%)</b></td><td>175.00 (+9.95%)</td><td>161.10 (+5.36%)</td><td>139.70 (+4.96%)</td><td>45.78 <b>(+56.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.74 (n/a)</td><td>0.63 (n/a)</td><td>0.64 (n/a)</td><td>0.48 (n/a)</td><td>0.10 (n/a)</td><td>206.20 (n/a)</td><td>159.16 (n/a)</td><td>152.90 (n/a)</td><td>133.10 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.54 (-12.21%)</td><td>0.44 <b>(-23.02%)</b></td><td>0.46 <b>(-21.37%)</b></td><td>0.33 <b>(-27.73%)</b></td><td>0.10 <b>(+58.68%)</b></td><td>295.00 <b>(+38.37%)</b></td><td>233.82 <b>(+34.15%)</b></td><td>213.10 <b>(+27.22%)</b></td><td>182.50 (+13.85%)</td><td>55.18 <b>(+151.00%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.61 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.46 (n/a)</td><td>0.06 (n/a)</td><td>213.20 (n/a)</td><td>174.30 (n/a)</td><td>167.50 (n/a)</td><td>160.30 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.61 (+2.51%)</td><td>0.50 (+14.12%)</td><td>0.46 (+14.86%)</td><td>0.41 (+12.51%)</td><td>0.10 (+0.01%)</td><td>180.10 (-11.11%)</td><td>151.70 (-12.75%)</td><td>159.50 (-12.94%)</td><td>120.50 (-2.43%)</td><td>27.76 (-13.96%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.60 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>202.60 (n/a)</td><td>173.86 (n/a)</td><td>183.20 (n/a)</td><td>123.50 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.54 <b>(-20.26%)</b></td><td>0.48 (-7.45%)</td><td>0.52 (+2.90%)</td><td>0.38 (-7.97%)</td><td>0.07 <b>(-35.14%)</b></td><td>192.20 (+8.65%)</td><td>154.94 (+6.47%)</td><td>141.60 (-2.88%)</td><td>136.30 <b>(+25.39%)</b></td><td>24.63 (-14.19%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.68 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.11 (n/a)</td><td>176.90 (n/a)</td><td>145.52 (n/a)</td><td>145.80 (n/a)</td><td>108.70 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.57 (-6.90%)</td><td>0.45 (-9.93%)</td><td>0.48 (-11.04%)</td><td>0.22 <b>(-44.90%)</b></td><td>0.14 <b>(+39.86%)</b></td><td>339.80 <b>(+81.52%)</b></td><td>183.90 <b>(+21.40%)</b></td><td>152.40 (+12.39%)</td><td>129.40 (+7.48%)</td><td>87.88 <b>(+181.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>187.20 (n/a)</td><td>151.48 (n/a)</td><td>135.60 (n/a)</td><td>120.40 (n/a)</td><td>31.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.55 (+14.68%)</td><td>0.46 (+11.46%)</td><td>0.46 (+10.42%)</td><td>0.38 (+12.40%)</td><td>0.08 (+15.63%)</td><td>193.00 (-11.02%)</td><td>163.42 (-10.17%)</td><td>159.90 (-9.46%)</td><td>132.90 (-12.74%)</td><td>27.15 (-8.54%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.48 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>216.90 (n/a)</td><td>181.92 (n/a)</td><td>176.60 (n/a)</td><td>152.30 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.86 <b>(-36.74%)</b></td><td>0.69 <b>(-27.11%)</b></td><td>0.73 (-19.34%)</td><td>0.52 <b>(-32.50%)</b></td><td>0.14 <b>(-39.60%)</b></td><td>250.70 <b>(+48.17%)</b></td><td>196.54 <b>(+36.54%)</b></td><td>178.90 <b>(+23.98%)</b></td><td>152.90 <b>(+58.12%)</b></td><td>42.76 <b>(+45.49%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.35 (n/a)</td><td>0.95 (n/a)</td><td>0.91 (n/a)</td><td>0.77 (n/a)</td><td>0.24 (n/a)</td><td>169.20 (n/a)</td><td>143.94 (n/a)</td><td>144.30 (n/a)</td><td>96.70 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.02 (+1.54%)</td><td>0.75 (-12.29%)</td><td>0.78 (-14.02%)</td><td>0.57 (-9.11%)</td><td>0.18 (+15.72%)</td><td>231.20 (+10.04%)</td><td>183.10 (+15.80%)</td><td>168.80 (+16.33%)</td><td>128.40 (-1.53%)</td><td>43.30 <b>(+30.51%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.01 (n/a)</td><td>0.86 (n/a)</td><td>0.90 (n/a)</td><td>0.62 (n/a)</td><td>0.16 (n/a)</td><td>210.10 (n/a)</td><td>158.12 (n/a)</td><td>145.10 (n/a)</td><td>130.40 (n/a)</td><td>33.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.85 (-17.58%)</td><td>0.70 (-18.04%)</td><td>0.74 (-12.51%)</td><td>0.48 <b>(-35.97%)</b></td><td>0.14 <b>(+22.99%)</b></td><td>275.10 <b>(+56.22%)</b></td><td>193.20 <b>(+25.18%)</b></td><td>177.50 (+14.29%)</td><td>154.10 <b>(+21.34%)</b></td><td>47.07 <b>(+147.48%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.84 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td><td>176.10 (n/a)</td><td>154.34 (n/a)</td><td>155.30 (n/a)</td><td>127.00 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (-2.12%)</td><td>0.02 (+11.80%)</td><td>0.02 (+6.42%)</td><td>0.02 (+12.65%)</td><td>0.00 <b>(-22.99%)</b></td><td>232.50 (-11.23%)</td><td>173.32 (-12.47%)</td><td>166.40 (-6.04%)</td><td>146.70 (+2.16%)</td><td>34.36 <b>(-29.91%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.90 (n/a)</td><td>198.02 (n/a)</td><td>177.10 (n/a)</td><td>143.60 (n/a)</td><td>49.02 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (-18.79%)</td><td>0.02 (-18.61%)</td><td>0.02 <b>(-23.02%)</b></td><td>0.02 <b>(-20.14%)</b></td><td>0.00 (+7.72%)</td><td>227.00 <b>(+25.21%)</b></td><td>189.54 <b>(+24.76%)</b></td><td>206.70 <b>(+29.92%)</b></td><td>148.00 <b>(+23.13%)</b></td><td>38.42 <b>(+62.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.30 (n/a)</td><td>151.92 (n/a)</td><td>159.10 (n/a)</td><td>120.20 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (+0.83%)</td><td>0.02 (-0.37%)</td><td>0.02 (-4.89%)</td><td>0.02 (+2.03%)</td><td>0.00 (-10.78%)</td><td>190.50 (-2.01%)</td><td>172.32 (+0.13%)</td><td>173.80 (+5.14%)</td><td>150.50 (-0.86%)</td><td>16.19 (-14.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.40 (n/a)</td><td>172.10 (n/a)</td><td>165.30 (n/a)</td><td>151.80 (n/a)</td><td>18.90 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.92 (-9.44%)</td><td>0.72 (-15.43%)</td><td>0.70 (-10.28%)</td><td>0.54 <b>(-25.86%)</b></td><td>0.15 (+12.21%)</td><td>243.80 <b>(+34.85%)</b></td><td>190.62 <b>(+20.08%)</b></td><td>187.70 (+11.46%)</td><td>143.40 (+10.39%)</td><td>39.20 <b>(+66.86%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.02 (n/a)</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.13 (n/a)</td><td>180.80 (n/a)</td><td>158.74 (n/a)</td><td>168.40 (n/a)</td><td>129.90 (n/a)</td><td>23.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.96 (-10.90%)</td><td>0.77 (-16.13%)</td><td>0.74 (-16.75%)</td><td>0.56 <b>(-26.61%)</b></td><td>0.18 (+19.01%)</td><td>237.90 <b>(+36.25%)</b></td><td>179.84 <b>(+22.01%)</b></td><td>179.40 <b>(+20.08%)</b></td><td>137.20 (+12.27%)</td><td>42.59 <b>(+79.15%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.08 (n/a)</td><td>0.92 (n/a)</td><td>0.88 (n/a)</td><td>0.76 (n/a)</td><td>0.15 (n/a)</td><td>174.60 (n/a)</td><td>147.40 (n/a)</td><td>149.40 (n/a)</td><td>122.20 (n/a)</td><td>23.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.84 <b>(-21.05%)</b></td><td>0.71 <b>(-23.29%)</b></td><td>0.70 <b>(-33.41%)</b></td><td>0.58 (-13.65%)</td><td>0.09 <b>(-51.03%)</b></td><td>227.70 (+15.82%)</td><td>189.96 <b>(+27.22%)</b></td><td>189.80 <b>(+50.16%)</b></td><td>157.40 <b>(+26.63%)</b></td><td>25.33 <b>(-25.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.06 (n/a)</td><td>0.92 (n/a)</td><td>1.05 (n/a)</td><td>0.67 (n/a)</td><td>0.19 (n/a)</td><td>196.60 (n/a)</td><td>149.32 (n/a)</td><td>126.40 (n/a)</td><td>124.30 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.95 (-7.55%)</td><td>0.80 (-12.40%)</td><td>0.75 (-15.82%)</td><td>0.67 (-16.25%)</td><td>0.12 <b>(+22.39%)</b></td><td>197.80 (+19.44%)</td><td>168.30 (+15.20%)</td><td>175.80 (+18.78%)</td><td>139.10 (+8.16%)</td><td>25.54 <b>(+57.34%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.03 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.10 (n/a)</td><td>165.60 (n/a)</td><td>146.10 (n/a)</td><td>148.00 (n/a)</td><td>128.60 (n/a)</td><td>16.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.84 <b>(-23.01%)</b></td><td>0.70 <b>(-22.02%)</b></td><td>0.74 <b>(-21.94%)</b></td><td>0.50 <b>(-29.58%)</b></td><td>0.13 (-17.84%)</td><td>262.10 <b>(+41.98%)</b></td><td>195.62 <b>(+28.97%)</b></td><td>178.80 <b>(+28.08%)</b></td><td>157.80 <b>(+29.88%)</b></td><td>40.84 <b>(+51.41%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.09 (n/a)</td><td>0.89 (n/a)</td><td>0.95 (n/a)</td><td>0.72 (n/a)</td><td>0.16 (n/a)</td><td>184.60 (n/a)</td><td>151.68 (n/a)</td><td>139.60 (n/a)</td><td>121.50 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (-10.61%)</td><td>0.02 (-9.99%)</td><td>0.02 (+5.69%)</td><td>0.02 (-11.34%)</td><td>0.00 <b>(-33.19%)</b></td><td>233.50 (+12.75%)</td><td>185.24 (+8.70%)</td><td>181.20 (-5.38%)</td><td>139.60 (+11.95%)</td><td>34.57 (-14.91%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>170.42 (n/a)</td><td>191.50 (n/a)</td><td>124.70 (n/a)</td><td>40.63 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (+14.22%)</td><td>0.02 (+13.80%)</td><td>0.03 (+17.12%)</td><td>0.02 (+14.22%)</td><td>0.00 (+12.09%)</td><td>189.80 (-12.45%)</td><td>166.90 (-12.14%)</td><td>161.30 (-14.61%)</td><td>146.00 (-12.47%)</td><td>19.69 (-12.35%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.80 (n/a)</td><td>189.96 (n/a)</td><td>188.90 (n/a)</td><td>166.80 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.00 (-2.27%)</td><td>0.00 (-0.00%)</td><td>0.00 (+2.44%)</td><td>0.00 (+0.00%)</td><td>0.00 (-16.52%)</td><td>1048.01 (-0.01%)</td><td>992.13 (+0.63%)</td><td>983.25 (-0.91%)</td><td>949.29 (+2.54%)</td><td>35.89 (-18.65%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1048.13 (n/a)</td><td>985.95 (n/a)</td><td>992.24 (n/a)</td><td>925.81 (n/a)</td><td>44.12 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.01 (+1.19%)</td><td>0.01 (+3.05%)</td><td>0.01 (+2.53%)</td><td>0.01 (+8.33%)</td><td>0.00 <b>(-36.84%)</b></td><td>1049.45 (-7.82%)</td><td>1010.20 (-3.48%)</td><td>1010.24 (-2.92%)</td><td>958.74 (-2.16%)</td><td>34.52 <b>(-40.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1138.53 (n/a)</td><td>1046.62 (n/a)</td><td>1040.58 (n/a)</td><td>979.86 (n/a)</td><td>57.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.96 (-3.04%)</td><td>0.95 (-1.10%)</td><td>0.95 (-0.73%)</td><td>0.94 (+1.18%)</td><td>0.01 <b>(-68.39%)</b></td><td>2222.33 (-1.17%)</td><td>2207.71 (+1.08%)</td><td>2208.59 (+0.73%)</td><td>2185.08 (+3.14%)</td><td>15.64 <b>(-67.83%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2248.54 (n/a)</td><td>2184.17 (n/a)</td><td>2192.64 (n/a)</td><td>2118.62 (n/a)</td><td>48.63 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.40 (-1.03%)</td><td>0.39 (-1.43%)</td><td>0.39 (-3.44%)</td><td>0.38 (-0.31%)</td><td>0.01 (-3.42%)</td><td>1371.14 (+0.32%)</td><td>1339.42 (+1.45%)</td><td>1355.46 (+3.56%)</td><td>1299.29 (+1.03%)</td><td>33.86 (-2.31%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1366.82 (n/a)</td><td>1320.33 (n/a)</td><td>1308.81 (n/a)</td><td>1286.03 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.25 (-0.43%)</td><td>0.24 (-3.16%)</td><td>0.24 (-5.64%)</td><td>0.23 (-4.20%)</td><td>0.01 <b>(+42.02%)</b></td><td>2275.37 (+4.38%)</td><td>2177.27 (+3.34%)</td><td>2206.97 (+5.99%)</td><td>2062.09 (+0.45%)</td><td>82.70 <b>(+47.84%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2179.88 (n/a)</td><td>2107.00 (n/a)</td><td>2082.26 (n/a)</td><td>2052.78 (n/a)</td><td>55.94 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.36 (-4.07%)</td><td>0.36 (-2.25%)</td><td>0.36 (-1.18%)</td><td>0.35 (-1.03%)</td><td>0.00 <b>(-57.64%)</b></td><td>1477.55 (+1.03%)</td><td>1456.43 (+2.27%)</td><td>1452.02 (+1.20%)</td><td>1444.42 (+4.26%)</td><td>13.44 <b>(-55.62%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1462.55 (n/a)</td><td>1424.09 (n/a)</td><td>1434.83 (n/a)</td><td>1385.39 (n/a)</td><td>30.29 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.95 (+13.89%)</td><td>2.86 (-12.20%)</td><td>2.64 (-17.72%)</td><td>2.44 <b>(-20.74%)</b></td><td>0.61 <b>(+272.56%)</b></td><td>215.20 <b>(+26.22%)</b></td><td>188.88 (+17.08%)</td><td>198.70 <b>(+21.53%)</b></td><td>132.80 (-12.23%)</td><td>32.16 <b>(+298.04%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.47 (n/a)</td><td>3.26 (n/a)</td><td>3.21 (n/a)</td><td>3.07 (n/a)</td><td>0.16 (n/a)</td><td>170.50 (n/a)</td><td>161.32 (n/a)</td><td>163.50 (n/a)</td><td>151.30 (n/a)</td><td>8.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>5.29 (-10.01%)</td><td>4.84 (-11.00%)</td><td>4.78 (-14.06%)</td><td>4.34 (-10.74%)</td><td>0.35 (-19.60%)</td><td>241.60 (+12.01%)</td><td>217.56 (+12.24%)</td><td>219.40 (+16.33%)</td><td>198.40 (+11.15%)</td><td>16.06 (+0.57%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>5.87 (n/a)</td><td>5.44 (n/a)</td><td>5.56 (n/a)</td><td>4.86 (n/a)</td><td>0.44 (n/a)</td><td>215.70 (n/a)</td><td>193.84 (n/a)</td><td>188.60 (n/a)</td><td>178.50 (n/a)</td><td>15.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.23 (-15.22%)</td><td>2.79 (-15.27%)</td><td>2.84 (-12.25%)</td><td>2.44 (-14.61%)</td><td>0.35 (-10.62%)</td><td>215.30 (+17.14%)</td><td>190.20 (+18.21%)</td><td>184.90 (+13.92%)</td><td>162.40 (+18.02%)</td><td>23.58 <b>(+26.60%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.81 (n/a)</td><td>3.29 (n/a)</td><td>3.23 (n/a)</td><td>2.85 (n/a)</td><td>0.39 (n/a)</td><td>183.80 (n/a)</td><td>160.90 (n/a)</td><td>162.30 (n/a)</td><td>137.60 (n/a)</td><td>18.62 (n/a)</td>
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
