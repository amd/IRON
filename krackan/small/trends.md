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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.10 (-2.22%)</td><td>0.07 (-7.49%)</td><td>0.07 (-6.86%)</td><td>0.06 (-15.11%)</td><td>0.02 (+0.39%)</td><td>219.50 (+17.76%)</td><td>172.70 (+8.60%)</td><td>179.30 (+7.37%)</td><td>125.90 (+2.27%)</td><td>34.82 (+17.57%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>159.02 (n/a)</td><td>167.00 (n/a)</td><td>123.10 (n/a)</td><td>29.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (+16.69%)</td><td>0.07 (+5.94%)</td><td>0.07 (+8.32%)</td><td>0.05 (-8.17%)</td><td>0.01 <b>(+78.86%)</b></td><td>236.00 (+8.86%)</td><td>178.02 (-3.37%)</td><td>171.50 (-7.70%)</td><td>135.40 (-14.30%)</td><td>38.62 <b>(+68.64%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>184.22 (n/a)</td><td>185.80 (n/a)</td><td>158.00 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (+9.83%)</td><td>0.06 (+7.94%)</td><td>0.06 (-8.02%)</td><td>0.05 <b>(+36.68%)</b></td><td>0.01 (-13.25%)</td><td>227.40 <b>(-26.83%)</b></td><td>197.30 (-9.36%)</td><td>213.30 (+8.72%)</td><td>154.00 (-8.93%)</td><td>30.80 <b>(-44.36%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>310.80 (n/a)</td><td>217.68 (n/a)</td><td>196.20 (n/a)</td><td>169.10 (n/a)</td><td>55.35 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (+18.71%)</td><td>0.06 (+14.93%)</td><td>0.05 <b>(+22.65%)</b></td><td>0.04 (-9.20%)</td><td>0.02 <b>(+30.25%)</b></td><td>334.10 (+10.12%)</td><td>220.56 (-10.59%)</td><td>225.90 (-18.48%)</td><td>149.80 (-15.80%)</td><td>73.35 <b>(+20.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>303.40 (n/a)</td><td>246.68 (n/a)</td><td>277.10 (n/a)</td><td>177.90 (n/a)</td><td>60.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (+16.85%)</td><td>0.04 <b>(+21.77%)</b></td><td>0.04 <b>(+23.43%)</b></td><td>0.03 <b>(+31.03%)</b></td><td>0.01 (-12.99%)</td><td>164.30 <b>(-23.69%)</b></td><td>139.74 (-19.13%)</td><td>137.60 (-18.96%)</td><td>115.40 (-14.46%)</td><td>19.24 <b>(-42.98%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>172.80 (n/a)</td><td>169.80 (n/a)</td><td>134.90 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (-12.82%)</td><td>0.03 (-11.03%)</td><td>0.03 <b>(-20.74%)</b></td><td>0.03 (-7.09%)</td><td>0.01 <b>(-34.46%)</b></td><td>208.50 (+7.64%)</td><td>165.82 (+10.11%)</td><td>160.40 <b>(+26.10%)</b></td><td>138.10 (+14.70%)</td><td>28.67 <b>(-20.32%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>150.60 (n/a)</td><td>127.20 (n/a)</td><td>120.40 (n/a)</td><td>35.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (-16.12%)</td><td>0.03 (-10.62%)</td><td>0.03 (-2.53%)</td><td>0.03 (-1.76%)</td><td>0.00 <b>(-40.66%)</b></td><td>180.10 (+1.81%)</td><td>160.96 (+9.62%)</td><td>165.80 (+2.60%)</td><td>127.20 (+19.21%)</td><td>21.09 <b>(-28.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>176.90 (n/a)</td><td>146.84 (n/a)</td><td>161.60 (n/a)</td><td>106.70 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 <b>(+49.24%)</b></td><td>0.04 (+10.80%)</td><td>0.03 (-14.60%)</td><td>0.03 (-2.15%)</td><td>0.01 <b>(+221.77%)</b></td><td>192.10 (+2.24%)</td><td>157.02 (-4.14%)</td><td>181.30 (+17.12%)</td><td>96.90 <b>(-33.03%)</b></td><td>41.91 <b>(+123.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.90 (n/a)</td><td>163.80 (n/a)</td><td>154.80 (n/a)</td><td>144.70 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (-6.43%)</td><td>0.03 (-4.90%)</td><td>0.03 (-4.76%)</td><td>0.03 (-4.48%)</td><td>0.00 (-16.93%)</td><td>175.60 (+4.71%)</td><td>160.10 (+4.90%)</td><td>161.20 (+5.02%)</td><td>134.90 (+6.81%)</td><td>15.49 (-8.56%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>167.70 (n/a)</td><td>152.62 (n/a)</td><td>153.50 (n/a)</td><td>126.30 (n/a)</td><td>16.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (-19.47%)</td><td>0.03 (-17.64%)</td><td>0.03 (-16.64%)</td><td>0.02 <b>(-24.84%)</b></td><td>0.00 (-15.35%)</td><td>265.80 <b>(+33.03%)</b></td><td>203.04 <b>(+21.92%)</b></td><td>188.10 (+19.96%)</td><td>162.90 <b>(+24.16%)</b></td><td>39.04 <b>(+41.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>166.54 (n/a)</td><td>156.80 (n/a)</td><td>131.20 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (-5.82%)</td><td>0.03 (-13.25%)</td><td>0.03 (-5.65%)</td><td>0.02 <b>(-26.16%)</b></td><td>0.01 <b>(+47.48%)</b></td><td>285.60 <b>(+35.42%)</b></td><td>210.48 <b>(+22.17%)</b></td><td>190.30 (+5.96%)</td><td>138.30 (+6.14%)</td><td>68.03 <b>(+126.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>172.28 (n/a)</td><td>179.60 (n/a)</td><td>130.30 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (-4.33%)</td><td>0.02 (-14.59%)</td><td>0.02 (-15.32%)</td><td>0.02 <b>(-29.11%)</b></td><td>0.00 <b>(+94.51%)</b></td><td>314.30 <b>(+41.07%)</b></td><td>230.46 <b>(+20.53%)</b></td><td>217.50 (+18.08%)</td><td>187.20 (+4.52%)</td><td>51.93 <b>(+183.91%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.80 (n/a)</td><td>191.20 (n/a)</td><td>184.20 (n/a)</td><td>179.10 (n/a)</td><td>18.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>163.48 (n/a)</td><td>158.50 (n/a)</td><td>132.60 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>167.88 (n/a)</td><td>174.20 (n/a)</td><td>135.70 (n/a)</td><td>32.37 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.20 (n/a)</td><td>199.16 (n/a)</td><td>189.40 (n/a)</td><td>140.40 (n/a)</td><td>52.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>247.90 (n/a)</td><td>198.82 (n/a)</td><td>216.20 (n/a)</td><td>119.90 (n/a)</td><td>48.70 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.40 (n/a)</td><td>179.60 (n/a)</td><td>175.70 (n/a)</td><td>150.70 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.30 (n/a)</td><td>200.82 (n/a)</td><td>204.50 (n/a)</td><td>149.80 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>257.10 (n/a)</td><td>199.44 (n/a)</td><td>189.60 (n/a)</td><td>149.80 (n/a)</td><td>42.68 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>337.50 (n/a)</td><td>234.98 (n/a)</td><td>210.10 (n/a)</td><td>194.90 (n/a)</td><td>58.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>175.44 (n/a)</td><td>182.70 (n/a)</td><td>149.60 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.50 (n/a)</td><td>202.60 (n/a)</td><td>192.30 (n/a)</td><td>140.10 (n/a)</td><td>66.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>184.90 (n/a)</td><td>201.80 (n/a)</td><td>132.70 (n/a)</td><td>45.09 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>172.14 (n/a)</td><td>172.40 (n/a)</td><td>152.20 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>162.22 (n/a)</td><td>140.20 (n/a)</td><td>132.50 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>156.62 (n/a)</td><td>161.70 (n/a)</td><td>124.10 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.30 (n/a)</td><td>187.06 (n/a)</td><td>173.40 (n/a)</td><td>158.70 (n/a)</td><td>41.44 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.50 (n/a)</td><td>212.44 (n/a)</td><td>220.60 (n/a)</td><td>192.00 (n/a)</td><td>13.28 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>4.68 (+9.47%)</td><td>4.26 (+1.22%)</td><td>4.18 (-1.55%)</td><td>4.12 (+1.39%)</td><td>0.24 <b>(+179.42%)</b></td><td>2285.10 (-1.37%)</td><td>2214.82 (-1.00%)</td><td>2252.10 (+1.58%)</td><td>2008.00 (-8.65%)</td><td>117.02 <b>(+149.68%)</b></td><td>1842.33 (+9.47%)</td><td>1674.30 (+1.22%)</td><td>1642.67 (-1.55%)</td><td>1618.89 (+1.39%)</td><td>94.84 <b>(+179.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>4.28 (n/a)</td><td>4.20 (n/a)</td><td>4.24 (n/a)</td><td>4.06 (n/a)</td><td>0.09 (n/a)</td><td>2316.80 (n/a)</td><td>2237.30 (n/a)</td><td>2217.10 (n/a)</td><td>2198.10 (n/a)</td><td>46.87 (n/a)</td><td>1682.99 (n/a)</td><td>1654.06 (n/a)</td><td>1668.55 (n/a)</td><td>1596.74 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.12 <b>(-44.13%)</b></td><td>0.98 (-10.58%)</td><td>1.04 (+9.58%)</td><td>0.78 <b>(+21.20%)</b></td><td>0.14 <b>(-73.43%)</b></td><td>284.70 (-17.50%)</td><td>228.68 (-0.87%)</td><td>213.40 (-8.73%)</td><td>198.20 <b>(+79.04%)</b></td><td>35.50 <b>(-57.73%)</b></td><td>47.62 <b>(-44.13%)</b></td><td>42.00 (-10.58%)</td><td>44.23 (+9.58%)</td><td>33.15 <b>(+21.20%)</b></td><td>5.92 <b>(-73.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>2.00 (n/a)</td><td>1.10 (n/a)</td><td>0.95 (n/a)</td><td>0.64 (n/a)</td><td>0.52 (n/a)</td><td>345.10 (n/a)</td><td>230.68 (n/a)</td><td>233.80 (n/a)</td><td>110.70 (n/a)</td><td>84.00 (n/a)</td><td>85.23 (n/a)</td><td>46.98 (n/a)</td><td>40.36 (n/a)</td><td>27.35 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.34 <b>(+25.16%)</b></td><td>1.03 (+14.91%)</td><td>1.09 (+15.20%)</td><td>0.67 (+13.19%)</td><td>0.25 <b>(+28.61%)</b></td><td>332.00 (-11.66%)</td><td>226.12 (-12.30%)</td><td>202.40 (-13.21%)</td><td>165.20 <b>(-20.12%)</b></td><td>63.73 (-7.56%)</td><td>57.12 <b>(+25.16%)</b></td><td>44.05 (+14.91%)</td><td>46.62 (+15.20%)</td><td>28.43 (+13.19%)</td><td>10.54 <b>(+28.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.07 (n/a)</td><td>0.90 (n/a)</td><td>0.95 (n/a)</td><td>0.59 (n/a)</td><td>0.19 (n/a)</td><td>375.80 (n/a)</td><td>257.82 (n/a)</td><td>233.20 (n/a)</td><td>206.80 (n/a)</td><td>68.95 (n/a)</td><td>45.64 (n/a)</td><td>38.34 (n/a)</td><td>40.47 (n/a)</td><td>25.12 (n/a)</td><td>8.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.52 (-0.08%)</td><td>0.52 (-0.02%)</td><td>0.52 (+0.02%)</td><td>0.52 (-0.08%)</td><td>0.00 (-3.47%)</td><td>48676.40 (+0.08%)</td><td>48413.60 (+0.02%)</td><td>48445.50 (-0.02%)</td><td>48043.70 (+0.08%)</td><td>229.08 (-3.32%)</td><td>357.59 (-0.08%)</td><td>354.86 (-0.02%)</td><td>354.62 (+0.02%)</td><td>352.94 (-0.08%)</td><td>1.68 (-3.47%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48639.00 (n/a)</td><td>48405.48 (n/a)</td><td>48453.60 (n/a)</td><td>48005.60 (n/a)</td><td>236.94 (n/a)</td><td>357.87 (n/a)</td><td>354.92 (n/a)</td><td>354.56 (n/a)</td><td>353.21 (n/a)</td><td>1.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.91 (+2.03%)</td><td>0.89 (+0.49%)</td><td>0.88 (-0.17%)</td><td>0.87 (-0.17%)</td><td>0.02 <b>(+98.67%)</b></td><td>28821.90 (+0.17%)</td><td>28275.32 (-0.47%)</td><td>28532.60 (+0.17%)</td><td>27507.90 (-1.99%)</td><td>526.49 <b>(+94.89%)</b></td><td>624.54 (+2.03%)</td><td>607.76 (+0.49%)</td><td>602.11 (-0.17%)</td><td>596.07 (-0.17%)</td><td>11.42 <b>(+98.67%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>28772.60 (n/a)</td><td>28407.86 (n/a)</td><td>28483.30 (n/a)</td><td>28066.00 (n/a)</td><td>270.15 (n/a)</td><td>612.12 (n/a)</td><td>604.80 (n/a)</td><td>603.16 (n/a)</td><td>597.09 (n/a)</td><td>5.75 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.27 (-1.40%)</td><td>3.18 (-1.36%)</td><td>3.17 (-0.59%)</td><td>3.08 (-2.32%)</td><td>0.07 (-7.39%)</td><td>8159.70 (+2.37%)</td><td>7926.62 (+1.37%)</td><td>7942.00 (+0.59%)</td><td>7706.40 (+1.42%)</td><td>168.00 (-3.97%)</td><td>2229.31 (-1.40%)</td><td>2168.14 (-1.36%)</td><td>2163.16 (-0.59%)</td><td>2105.46 (-2.32%)</td><td>45.90 (-7.39%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.31 (n/a)</td><td>3.22 (n/a)</td><td>3.19 (n/a)</td><td>3.16 (n/a)</td><td>0.07 (n/a)</td><td>7970.60 (n/a)</td><td>7819.24 (n/a)</td><td>7895.50 (n/a)</td><td>7598.40 (n/a)</td><td>174.95 (n/a)</td><td>2260.97 (n/a)</td><td>2198.01 (n/a)</td><td>2175.91 (n/a)</td><td>2155.39 (n/a)</td><td>49.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.74 (-0.59%)</td><td>3.39 (-3.28%)</td><td>3.62 (+3.35%)</td><td>2.93 (-8.23%)</td><td>0.39 <b>(+81.40%)</b></td><td>2749.40 (+8.97%)</td><td>2405.78 (+4.22%)</td><td>2225.20 (-3.24%)</td><td>2156.00 (+0.60%)</td><td>288.93 <b>(+99.53%)</b></td><td>980.49 (-0.59%)</td><td>888.52 (-3.28%)</td><td>949.98 (+3.35%)</td><td>768.86 (-8.23%)</td><td>102.42 <b>(+81.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.76 (n/a)</td><td>3.50 (n/a)</td><td>3.51 (n/a)</td><td>3.19 (n/a)</td><td>0.22 (n/a)</td><td>2523.10 (n/a)</td><td>2308.28 (n/a)</td><td>2299.70 (n/a)</td><td>2143.20 (n/a)</td><td>144.80 (n/a)</td><td>986.32 (n/a)</td><td>918.62 (n/a)</td><td>919.20 (n/a)</td><td>837.83 (n/a)</td><td>56.46 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.37 <b>(-28.97%)</b></td><td>0.35 (+0.66%)</td><td>0.36 (+15.42%)</td><td>0.33 (+13.54%)</td><td>0.02 <b>(-76.66%)</b></td><td>3809.50 (-11.92%)</td><td>3543.70 (-5.14%)</td><td>3438.50 (-13.36%)</td><td>3326.40 <b>(+40.78%)</b></td><td>239.35 <b>(-70.02%)</b></td><td>20.17 <b>(-28.97%)</b></td><td>19.01 (+0.66%)</td><td>19.52 (+15.42%)</td><td>17.62 (+13.54%)</td><td>1.26 <b>(-76.66%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>4325.10 (n/a)</td><td>3735.86 (n/a)</td><td>3968.60 (n/a)</td><td>2362.80 (n/a)</td><td>798.42 (n/a)</td><td>28.40 (n/a)</td><td>18.88 (n/a)</td><td>16.91 (n/a)</td><td>15.52 (n/a)</td><td>5.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>6.84 (+6.32%)</td><td>4.43 (-13.86%)</td><td>3.68 <b>(-24.98%)</b></td><td>3.27 <b>(-28.13%)</b></td><td>1.48 <b>(+98.81%)</b></td><td>2034.70 <b>(+39.14%)</b></td><td>1615.80 <b>(+23.23%)</b></td><td>1805.50 <b>(+33.31%)</b></td><td>972.50 (-5.94%)</td><td>440.11 <b>(+165.97%)</b></td><td>2113.28 (+6.32%)</td><td>1370.16 (-13.86%)</td><td>1138.33 <b>(-24.98%)</b></td><td>1010.09 <b>(-28.13%)</b></td><td>458.42 <b>(+98.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>6.43 (n/a)</td><td>5.15 (n/a)</td><td>4.91 (n/a)</td><td>4.55 (n/a)</td><td>0.75 (n/a)</td><td>1462.30 (n/a)</td><td>1311.20 (n/a)</td><td>1354.40 (n/a)</td><td>1033.90 (n/a)</td><td>165.48 (n/a)</td><td>1987.75 (n/a)</td><td>1590.61 (n/a)</td><td>1517.47 (n/a)</td><td>1405.51 (n/a)</td><td>230.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.26 (n/a)</td><td>11.96 (n/a)</td><td>11.63 (n/a)</td><td>11.19 (n/a)</td><td>0.84 (n/a)</td><td>13.25 (n/a)</td><td>11.95 (n/a)</td><td>11.63 (n/a)</td><td>11.18 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>24.84 (-0.27%)</td><td>23.36 (+4.72%)</td><td>24.37 (+1.62%)</td><td>20.60 <b>(+20.86%)</b></td><td>1.78 <b>(-45.99%)</b></td><td>24.82 (-0.27%)</td><td>23.34 (+4.72%)</td><td>24.35 (+1.62%)</td><td>20.59 <b>(+20.86%)</b></td><td>1.78 <b>(-45.99%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>24.90 (n/a)</td><td>22.30 (n/a)</td><td>23.98 (n/a)</td><td>17.05 (n/a)</td><td>3.29 (n/a)</td><td>24.89 (n/a)</td><td>22.29 (n/a)</td><td>23.97 (n/a)</td><td>17.04 (n/a)</td><td>3.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>41.34 (+0.30%)</td><td>39.62 (+1.82%)</td><td>40.80 (+1.79%)</td><td>35.65 (+7.07%)</td><td>2.39 <b>(-24.82%)</b></td><td>41.32 (+0.30%)</td><td>39.59 (+1.82%)</td><td>40.78 (+1.79%)</td><td>35.63 (+7.07%)</td><td>2.39 <b>(-24.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>41.22 (n/a)</td><td>38.91 (n/a)</td><td>40.09 (n/a)</td><td>33.30 (n/a)</td><td>3.18 (n/a)</td><td>41.19 (n/a)</td><td>38.89 (n/a)</td><td>40.06 (n/a)</td><td>33.27 (n/a)</td><td>3.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>44.48 (-4.35%)</td><td>43.11 (+1.18%)</td><td>43.06 (+0.88%)</td><td>41.63 (+13.86%)</td><td>1.02 <b>(-73.34%)</b></td><td>44.46 (-4.35%)</td><td>43.09 (+1.18%)</td><td>43.04 (+0.88%)</td><td>41.60 (+13.86%)</td><td>1.02 <b>(-73.35%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>46.51 (n/a)</td><td>42.61 (n/a)</td><td>42.69 (n/a)</td><td>36.56 (n/a)</td><td>3.82 (n/a)</td><td>46.48 (n/a)</td><td>42.58 (n/a)</td><td>42.66 (n/a)</td><td>36.54 (n/a)</td><td>3.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.43 (n/a)</td><td>12.38 (n/a)</td><td>13.30 (n/a)</td><td>10.87 (n/a)</td><td>1.33 (n/a)</td><td>13.42 (n/a)</td><td>12.38 (n/a)</td><td>13.29 (n/a)</td><td>10.87 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>24.26 (+0.02%)</td><td>23.85 (+2.71%)</td><td>24.17 (+5.62%)</td><td>22.50 (+1.78%)</td><td>0.76 <b>(-20.13%)</b></td><td>24.25 (+0.02%)</td><td>23.83 (+2.71%)</td><td>24.15 (+5.62%)</td><td>22.48 (+1.78%)</td><td>0.76 <b>(-20.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>24.26 (n/a)</td><td>23.22 (n/a)</td><td>22.88 (n/a)</td><td>22.10 (n/a)</td><td>0.95 (n/a)</td><td>24.24 (n/a)</td><td>23.20 (n/a)</td><td>22.87 (n/a)</td><td>22.09 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>41.63 (+2.51%)</td><td>38.12 (+4.16%)</td><td>38.23 (+0.45%)</td><td>35.03 (+12.13%)</td><td>2.56 <b>(-36.30%)</b></td><td>41.61 (+2.51%)</td><td>38.09 (+4.16%)</td><td>38.21 (+0.45%)</td><td>35.01 (+12.13%)</td><td>2.56 <b>(-36.30%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>40.61 (n/a)</td><td>36.59 (n/a)</td><td>38.07 (n/a)</td><td>31.24 (n/a)</td><td>4.02 (n/a)</td><td>40.59 (n/a)</td><td>36.57 (n/a)</td><td>38.04 (n/a)</td><td>31.22 (n/a)</td><td>4.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>45.60 (+0.79%)</td><td>43.46 (+2.66%)</td><td>43.42 (+1.06%)</td><td>42.18 (+11.47%)</td><td>1.36 <b>(-55.61%)</b></td><td>45.57 (+0.79%)</td><td>43.44 (+2.66%)</td><td>43.39 (+1.06%)</td><td>42.15 (+11.47%)</td><td>1.36 <b>(-55.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>45.24 (n/a)</td><td>42.34 (n/a)</td><td>42.96 (n/a)</td><td>37.84 (n/a)</td><td>3.06 (n/a)</td><td>45.21 (n/a)</td><td>42.31 (n/a)</td><td>42.94 (n/a)</td><td>37.82 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>9.26 (-4.54%)</td><td>8.67 (-4.23%)</td><td>8.70 (-2.76%)</td><td>8.02 (-5.64%)</td><td>0.49 (+7.80%)</td><td>9.24 (-4.54%)</td><td>8.65 (-4.23%)</td><td>8.68 (-2.76%)</td><td>8.00 (-5.64%)</td><td>0.49 (+7.80%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>9.70 (n/a)</td><td>9.05 (n/a)</td><td>8.94 (n/a)</td><td>8.50 (n/a)</td><td>0.45 (n/a)</td><td>9.68 (n/a)</td><td>9.03 (n/a)</td><td>8.93 (n/a)</td><td>8.48 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.90 (-8.30%)</td><td>0.85 (-2.53%)</td><td>0.87 (+3.67%)</td><td>0.76 (-2.27%)</td><td>0.06 <b>(-27.01%)</b></td><td>0.88 (-8.30%)</td><td>0.84 (-2.53%)</td><td>0.86 (+3.67%)</td><td>0.75 (-2.27%)</td><td>0.06 <b>(-27.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.98 (n/a)</td><td>0.87 (n/a)</td><td>0.84 (n/a)</td><td>0.78 (n/a)</td><td>0.08 (n/a)</td><td>0.96 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.77 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.15 (-13.58%)</td><td>1.08 (-1.36%)</td><td>1.09 (+0.77%)</td><td>1.01 (+3.24%)</td><td>0.05 <b>(-62.62%)</b></td><td>1.13 (-13.58%)</td><td>1.07 (-1.36%)</td><td>1.07 (+0.77%)</td><td>1.00 (+3.24%)</td><td>0.05 <b>(-62.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.33 (n/a)</td><td>1.10 (n/a)</td><td>1.08 (n/a)</td><td>0.98 (n/a)</td><td>0.14 (n/a)</td><td>1.31 (n/a)</td><td>1.09 (n/a)</td><td>1.06 (n/a)</td><td>0.97 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>17.39 (-4.71%)</td><td>15.79 (-6.41%)</td><td>15.73 (-5.63%)</td><td>14.57 (-5.29%)</td><td>1.05 (-12.32%)</td><td>17.19 (-4.71%)</td><td>15.61 (-6.41%)</td><td>15.55 (-5.63%)</td><td>14.41 (-5.29%)</td><td>1.03 (-12.32%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>18.25 (n/a)</td><td>16.88 (n/a)</td><td>16.67 (n/a)</td><td>15.39 (n/a)</td><td>1.19 (n/a)</td><td>18.04 (n/a)</td><td>16.68 (n/a)</td><td>16.48 (n/a)</td><td>15.21 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.70 (-3.23%)</td><td>13.38 (+4.13%)</td><td>13.45 (-2.42%)</td><td>12.99 <b>(+49.19%)</b></td><td>0.27 <b>(-88.61%)</b></td><td>13.46 (-3.23%)</td><td>13.15 (+4.13%)</td><td>13.22 (-2.42%)</td><td>12.76 <b>(+49.19%)</b></td><td>0.26 <b>(-88.61%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>14.16 (n/a)</td><td>12.85 (n/a)</td><td>13.79 (n/a)</td><td>8.71 (n/a)</td><td>2.34 (n/a)</td><td>13.91 (n/a)</td><td>12.63 (n/a)</td><td>13.54 (n/a)</td><td>8.55 (n/a)</td><td>2.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>9.34 (-10.69%)</td><td>7.97 (-1.22%)</td><td>7.80 (+9.60%)</td><td>6.81 (+0.47%)</td><td>0.94 <b>(-41.94%)</b></td><td>9.18 (-10.69%)</td><td>7.83 (-1.22%)</td><td>7.67 (+9.60%)</td><td>6.69 (+0.47%)</td><td>0.92 <b>(-41.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>10.45 (n/a)</td><td>8.07 (n/a)</td><td>7.12 (n/a)</td><td>6.77 (n/a)</td><td>1.62 (n/a)</td><td>10.27 (n/a)</td><td>7.93 (n/a)</td><td>7.00 (n/a)</td><td>6.66 (n/a)</td><td>1.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>5.74 (-10.34%)</td><td>5.52 (-0.68%)</td><td>5.54 (-1.06%)</td><td>5.21 (+8.69%)</td><td>0.22 <b>(-65.39%)</b></td><td>5.64 (-10.34%)</td><td>5.44 (-0.68%)</td><td>5.45 (-1.06%)</td><td>5.13 (+8.69%)</td><td>0.21 <b>(-65.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>6.40 (n/a)</td><td>5.56 (n/a)</td><td>5.60 (n/a)</td><td>4.79 (n/a)</td><td>0.63 (n/a)</td><td>6.30 (n/a)</td><td>5.47 (n/a)</td><td>5.51 (n/a)</td><td>4.72 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.24 (n/a)</td><td>12.28 (n/a)</td><td>12.45 (n/a)</td><td>10.85 (n/a)</td><td>0.89 (n/a)</td><td>13.23 (n/a)</td><td>12.27 (n/a)</td><td>12.44 (n/a)</td><td>10.84 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.41 (n/a)</td><td>12.75 (n/a)</td><td>12.67 (n/a)</td><td>11.95 (n/a)</td><td>0.63 (n/a)</td><td>13.41 (n/a)</td><td>12.74 (n/a)</td><td>12.66 (n/a)</td><td>11.94 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>157.30 (n/a)</td><td>141.14 (n/a)</td><td>154.10 (n/a)</td><td>116.70 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.90 (n/a)</td><td>152.62 (n/a)</td><td>154.90 (n/a)</td><td>120.80 (n/a)</td><td>20.27 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>156.34 (n/a)</td><td>146.40 (n/a)</td><td>129.60 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>170.00 (n/a)</td><td>147.44 (n/a)</td><td>143.10 (n/a)</td><td>136.30 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>161.98 (n/a)</td><td>165.10 (n/a)</td><td>124.30 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>175.74 (n/a)</td><td>179.60 (n/a)</td><td>139.30 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>158.88 (n/a)</td><td>146.30 (n/a)</td><td>135.80 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.00 (n/a)</td><td>215.98 (n/a)</td><td>214.00 (n/a)</td><td>143.90 (n/a)</td><td>61.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+3.71%)</td><td>0.05 (+18.94%)</td><td>0.05 <b>(+29.54%)</b></td><td>0.03 (-4.93%)</td><td>0.01 (+14.28%)</td><td>242.50 (+5.21%)</td><td>166.40 (-14.88%)</td><td>156.30 <b>(-22.81%)</b></td><td>134.80 (-3.58%)</td><td>43.55 <b>(+23.18%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>195.48 (n/a)</td><td>202.50 (n/a)</td><td>139.80 (n/a)</td><td>35.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-14.39%)</td><td>0.05 (-7.63%)</td><td>0.05 (-3.51%)</td><td>0.04 (-9.62%)</td><td>0.01 (-14.53%)</td><td>225.60 (+10.64%)</td><td>182.28 (+8.35%)</td><td>174.30 (+3.63%)</td><td>130.90 (+16.77%)</td><td>41.85 (+19.14%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>168.24 (n/a)</td><td>168.20 (n/a)</td><td>112.10 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (+5.87%)</td><td>0.05 (+2.59%)</td><td>0.06 (+16.76%)</td><td>0.03 <b>(-22.07%)</b></td><td>0.01 <b>(+43.85%)</b></td><td>239.20 <b>(+28.33%)</b></td><td>158.18 (+1.05%)</td><td>138.60 (-14.34%)</td><td>116.00 (-5.61%)</td><td>47.77 <b>(+84.10%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>156.54 (n/a)</td><td>161.80 (n/a)</td><td>122.90 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+11.37%)</td><td>0.05 <b>(+20.14%)</b></td><td>0.06 <b>(+26.90%)</b></td><td>0.04 (+9.19%)</td><td>0.01 <b>(+25.68%)</b></td><td>214.80 (-8.40%)</td><td>158.00 (-16.18%)</td><td>143.20 <b>(-21.23%)</b></td><td>134.80 (-10.19%)</td><td>32.50 (+6.19%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>188.50 (n/a)</td><td>181.80 (n/a)</td><td>150.10 (n/a)</td><td>30.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-13.63%)</td><td>0.05 (-15.30%)</td><td>0.05 <b>(-20.33%)</b></td><td>0.04 (-4.68%)</td><td>0.01 (-13.73%)</td><td>219.90 (+4.91%)</td><td>183.46 (+17.71%)</td><td>181.90 <b>(+25.53%)</b></td><td>141.80 (+15.76%)</td><td>34.26 (+3.98%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>155.86 (n/a)</td><td>144.90 (n/a)</td><td>122.50 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-19.90%)</td><td>0.05 (-12.51%)</td><td>0.05 (-15.34%)</td><td>0.04 (+3.87%)</td><td>0.01 <b>(-40.07%)</b></td><td>228.60 (-3.71%)</td><td>186.14 (+9.92%)</td><td>176.90 (+18.09%)</td><td>139.40 <b>(+24.80%)</b></td><td>35.94 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>237.40 (n/a)</td><td>169.34 (n/a)</td><td>149.80 (n/a)</td><td>111.70 (n/a)</td><td>50.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+8.93%)</td><td>0.05 (+10.03%)</td><td>0.05 (+7.09%)</td><td>0.03 (+3.87%)</td><td>0.01 (+3.63%)</td><td>241.40 (-3.75%)</td><td>177.80 (-9.43%)</td><td>169.40 (-6.62%)</td><td>131.80 (-8.22%)</td><td>41.60 (-10.17%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>196.32 (n/a)</td><td>181.40 (n/a)</td><td>143.60 (n/a)</td><td>46.31 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 <b>(-25.67%)</b></td><td>0.04 (-14.70%)</td><td>0.04 (-7.96%)</td><td>0.04 (-17.54%)</td><td>0.01 <b>(-38.55%)</b></td><td>233.10 <b>(+21.28%)</b></td><td>194.56 (+16.04%)</td><td>189.20 (+8.67%)</td><td>164.70 <b>(+34.56%)</b></td><td>28.62 (+0.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>167.66 (n/a)</td><td>174.10 (n/a)</td><td>122.40 (n/a)</td><td>28.45 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-10.12%)</td><td>0.04 (-3.16%)</td><td>0.04 (-10.92%)</td><td>0.03 (+8.76%)</td><td>0.01 (-16.85%)</td><td>248.20 (-8.07%)</td><td>203.12 (+1.82%)</td><td>221.10 (+12.23%)</td><td>148.20 (+11.26%)</td><td>42.85 (-14.12%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.00 (n/a)</td><td>199.48 (n/a)</td><td>197.00 (n/a)</td><td>133.20 (n/a)</td><td>49.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-3.62%)</td><td>0.04 (+5.44%)</td><td>0.03 (-3.04%)</td><td>0.03 <b>(+27.61%)</b></td><td>0.01 (-17.29%)</td><td>245.60 <b>(-21.63%)</b></td><td>216.90 (-6.80%)</td><td>238.40 (+3.11%)</td><td>173.00 (+3.72%)</td><td>36.23 <b>(-32.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>313.40 (n/a)</td><td>232.72 (n/a)</td><td>231.20 (n/a)</td><td>166.80 (n/a)</td><td>53.29 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 <b>(-20.90%)</b></td><td>0.04 (-15.17%)</td><td>0.04 <b>(-20.08%)</b></td><td>0.04 (+15.91%)</td><td>0.00 <b>(-64.88%)</b></td><td>209.10 (-13.74%)</td><td>199.24 (+13.98%)</td><td>208.00 <b>(+25.08%)</b></td><td>173.00 <b>(+26.37%)</b></td><td>15.47 <b>(-62.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.40 (n/a)</td><td>174.80 (n/a)</td><td>166.30 (n/a)</td><td>136.90 (n/a)</td><td>41.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-9.52%)</td><td>0.04 (-12.39%)</td><td>0.04 (-8.37%)</td><td>0.02 <b>(-28.86%)</b></td><td>0.01 <b>(+21.96%)</b></td><td>330.80 <b>(+40.59%)</b></td><td>226.42 (+17.43%)</td><td>220.30 (+9.17%)</td><td>178.30 (+10.54%)</td><td>61.72 <b>(+97.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.30 (n/a)</td><td>192.82 (n/a)</td><td>201.80 (n/a)</td><td>161.30 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-19.16%)</td><td>0.04 (-13.75%)</td><td>0.05 (+3.01%)</td><td>0.03 <b>(-30.07%)</b></td><td>0.01 (-3.65%)</td><td>318.40 <b>(+43.04%)</b></td><td>210.76 (+18.59%)</td><td>181.60 (-2.94%)</td><td>166.50 <b>(+23.70%)</b></td><td>62.80 <b>(+76.60%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>177.72 (n/a)</td><td>187.10 (n/a)</td><td>134.60 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+10.14%)</td><td>0.05 (+12.95%)</td><td>0.05 (+7.62%)</td><td>0.04 <b>(+26.90%)</b></td><td>0.01 (-7.22%)</td><td>203.40 <b>(-21.22%)</b></td><td>173.94 (-12.47%)</td><td>167.30 (-7.11%)</td><td>144.40 (-9.24%)</td><td>26.98 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.20 (n/a)</td><td>198.72 (n/a)</td><td>180.10 (n/a)</td><td>159.10 (n/a)</td><td>40.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-16.34%)</td><td>0.04 (-16.30%)</td><td>0.04 (-15.53%)</td><td>0.04 (-10.25%)</td><td>0.01 <b>(-42.76%)</b></td><td>213.80 (+11.41%)</td><td>190.18 (+17.48%)</td><td>196.80 (+18.41%)</td><td>154.00 (+19.57%)</td><td>23.12 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>161.88 (n/a)</td><td>166.20 (n/a)</td><td>128.80 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-8.40%)</td><td>0.04 (-17.92%)</td><td>0.04 (-13.58%)</td><td>0.02 <b>(-39.11%)</b></td><td>0.01 <b>(+55.41%)</b></td><td>353.40 <b>(+64.22%)</b></td><td>220.60 <b>(+29.43%)</b></td><td>193.70 (+15.71%)</td><td>156.10 (+9.16%)</td><td>78.13 <b>(+185.19%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>170.44 (n/a)</td><td>167.40 (n/a)</td><td>143.00 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+1.58%)</td><td>0.04 (+8.15%)</td><td>0.04 (+5.69%)</td><td>0.04 <b>(+36.03%)</b></td><td>0.01 <b>(-25.53%)</b></td><td>219.70 <b>(-26.50%)</b></td><td>189.06 (-10.19%)</td><td>183.60 (-5.36%)</td><td>148.60 (-1.52%)</td><td>29.34 <b>(-46.65%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>298.90 (n/a)</td><td>210.50 (n/a)</td><td>194.00 (n/a)</td><td>150.90 (n/a)</td><td>55.01 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 <b>(+21.41%)</b></td><td>0.04 (+14.09%)</td><td>0.04 (+3.97%)</td><td>0.04 <b>(+47.64%)</b></td><td>0.01 (-5.98%)</td><td>224.90 <b>(-32.26%)</b></td><td>187.64 (-14.81%)</td><td>195.30 (-3.84%)</td><td>142.20 (-17.66%)</td><td>34.08 <b>(-48.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.00 (n/a)</td><td>220.26 (n/a)</td><td>203.10 (n/a)</td><td>172.70 (n/a)</td><td>65.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.18 (-0.47%)</td><td>0.18 (-0.24%)</td><td>0.18 (-0.13%)</td><td>0.18 (-0.36%)</td><td>0.00 (-10.10%)</td><td>47613.30 (+0.36%)</td><td>47435.68 (+0.24%)</td><td>47405.20 (+0.13%)</td><td>47364.10 (+0.47%)</td><td>103.37 (-9.29%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47440.20 (n/a)</td><td>47321.42 (n/a)</td><td>47342.10 (n/a)</td><td>47142.90 (n/a)</td><td>113.95 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.19 (+17.50%)</td><td>0.17 <b>(+24.83%)</b></td><td>0.17 <b>(+22.17%)</b></td><td>0.15 <b>(+40.87%)</b></td><td>0.02 <b>(-31.95%)</b></td><td>166.30 <b>(-29.02%)</b></td><td>146.42 <b>(-21.54%)</b></td><td>147.60 (-18.14%)</td><td>127.00 (-14.94%)</td><td>14.73 <b>(-58.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>234.30 (n/a)</td><td>186.62 (n/a)</td><td>180.30 (n/a)</td><td>149.30 (n/a)</td><td>35.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.32 (+0.78%)</td><td>0.31 <b>(+27.78%)</b></td><td>0.31 <b>(+37.06%)</b></td><td>0.28 <b>(+43.08%)</b></td><td>0.02 <b>(-64.66%)</b></td><td>144.90 <b>(-30.10%)</b></td><td>134.32 <b>(-23.85%)</b></td><td>130.70 <b>(-27.02%)</b></td><td>126.60 (-0.78%)</td><td>7.87 <b>(-75.27%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>207.30 (n/a)</td><td>176.40 (n/a)</td><td>179.10 (n/a)</td><td>127.60 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (-17.41%)</td><td>0.03 (+8.64%)</td><td>0.03 (+16.59%)</td><td>0.03 <b>(+30.02%)</b></td><td>0.01 <b>(-52.95%)</b></td><td>199.80 <b>(-23.07%)</b></td><td>161.64 (-14.76%)</td><td>167.40 (-14.24%)</td><td>132.70 <b>(+21.08%)</b></td><td>26.56 <b>(-56.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.70 (n/a)</td><td>189.64 (n/a)</td><td>195.20 (n/a)</td><td>109.60 (n/a)</td><td>61.47 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (+1.22%)</td><td>0.05 (+5.27%)</td><td>0.06 <b>(+24.08%)</b></td><td>0.02 <b>(-42.51%)</b></td><td>0.02 <b>(+61.34%)</b></td><td>376.60 <b>(+73.95%)</b></td><td>181.46 (+9.10%)</td><td>135.50 (-19.39%)</td><td>121.10 (-1.22%)</td><td>109.37 <b>(+198.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>166.32 (n/a)</td><td>168.10 (n/a)</td><td>122.60 (n/a)</td><td>36.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.11 (+17.03%)</td><td>0.07 (-4.74%)</td><td>0.07 (-12.58%)</td><td>0.06 (+8.98%)</td><td>0.02 <b>(+21.51%)</b></td><td>219.60 (-8.27%)</td><td>177.20 (+5.74%)</td><td>170.20 (+14.38%)</td><td>114.90 (-14.51%)</td><td>42.34 (-3.68%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>239.40 (n/a)</td><td>167.58 (n/a)</td><td>148.80 (n/a)</td><td>134.40 (n/a)</td><td>43.96 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (+10.73%)</td><td>0.06 <b>(+23.58%)</b></td><td>0.06 <b>(+27.87%)</b></td><td>0.05 <b>(+56.74%)</b></td><td>0.01 (-17.11%)</td><td>167.80 <b>(-36.22%)</b></td><td>133.30 <b>(-22.56%)</b></td><td>132.80 <b>(-21.79%)</b></td><td>105.10 (-9.63%)</td><td>25.74 <b>(-53.92%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.10 (n/a)</td><td>172.14 (n/a)</td><td>169.80 (n/a)</td><td>116.30 (n/a)</td><td>55.86 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (-14.24%)</td><td>0.05 (-18.68%)</td><td>0.06 (-6.66%)</td><td>0.03 <b>(-49.13%)</b></td><td>0.02 <b>(+50.51%)</b></td><td>363.40 <b>(+96.54%)</b></td><td>211.32 <b>(+33.83%)</b></td><td>179.00 (+7.12%)</td><td>147.10 (+16.56%)</td><td>88.73 <b>(+255.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.90 (n/a)</td><td>157.90 (n/a)</td><td>167.10 (n/a)</td><td>126.20 (n/a)</td><td>24.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+18.43%)</td><td>0.05 (+9.30%)</td><td>0.06 (+11.44%)</td><td>0.05 (-0.91%)</td><td>0.01 <b>(+142.56%)</b></td><td>179.60 (+0.90%)</td><td>151.88 (-7.14%)</td><td>143.70 (-10.24%)</td><td>128.80 (-15.60%)</td><td>23.38 <b>(+108.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>163.56 (n/a)</td><td>160.10 (n/a)</td><td>152.60 (n/a)</td><td>11.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 <b>(+30.70%)</b></td><td>0.06 (+8.83%)</td><td>0.05 (-16.73%)</td><td>0.05 (+9.82%)</td><td>0.02 <b>(+78.13%)</b></td><td>226.60 (-8.92%)</td><td>176.26 (-4.61%)</td><td>193.40 <b>(+20.05%)</b></td><td>120.20 <b>(-23.49%)</b></td><td>49.09 <b>(+23.76%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>248.80 (n/a)</td><td>184.78 (n/a)</td><td>161.10 (n/a)</td><td>157.10 (n/a)</td><td>39.67 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-0.92%)</td><td>0.05 (+11.75%)</td><td>0.06 (+16.20%)</td><td>0.05 <b>(+32.69%)</b></td><td>0.01 <b>(-41.90%)</b></td><td>176.80 <b>(-24.64%)</b></td><td>153.72 (-13.20%)</td><td>148.70 (-13.90%)</td><td>130.00 (+0.93%)</td><td>17.86 <b>(-55.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>177.10 (n/a)</td><td>172.70 (n/a)</td><td>128.80 (n/a)</td><td>40.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (-0.43%)</td><td>0.06 (+18.63%)</td><td>0.07 <b>(+43.61%)</b></td><td>0.04 <b>(+37.93%)</b></td><td>0.01 <b>(-36.00%)</b></td><td>209.80 <b>(-27.51%)</b></td><td>154.22 <b>(-21.25%)</b></td><td>133.70 <b>(-30.36%)</b></td><td>129.80 (+0.39%)</td><td>34.03 <b>(-50.91%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>289.40 (n/a)</td><td>195.84 (n/a)</td><td>192.00 (n/a)</td><td>129.30 (n/a)</td><td>69.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (+19.10%)</td><td>0.06 <b>(+52.77%)</b></td><td>0.07 <b>(+92.41%)</b></td><td>0.04 <b>(+107.08%)</b></td><td>0.02 (+3.45%)</td><td>204.00 <b>(-51.70%)</b></td><td>151.06 <b>(-39.00%)</b></td><td>121.20 <b>(-48.05%)</b></td><td>113.10 (-16.10%)</td><td>45.14 <b>(-58.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>422.40 (n/a)</td><td>247.62 (n/a)</td><td>233.30 (n/a)</td><td>134.80 (n/a)</td><td>107.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (-0.25%)</td><td>0.06 (+9.72%)</td><td>0.05 (-4.75%)</td><td>0.05 <b>(+51.73%)</b></td><td>0.01 (-18.72%)</td><td>204.50 <b>(-34.10%)</b></td><td>168.26 (-13.03%)</td><td>179.50 (+4.97%)</td><td>130.90 (+0.23%)</td><td>33.88 <b>(-50.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.30 (n/a)</td><td>193.48 (n/a)</td><td>171.00 (n/a)</td><td>130.60 (n/a)</td><td>68.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 <b>(+54.88%)</b></td><td>0.05 <b>(+55.46%)</b></td><td>0.05 <b>(+54.85%)</b></td><td>0.04 <b>(+52.52%)</b></td><td>0.01 <b>(+44.73%)</b></td><td>210.50 <b>(-34.42%)</b></td><td>155.60 <b>(-36.00%)</b></td><td>154.60 <b>(-35.42%)</b></td><td>116.50 <b>(-35.42%)</b></td><td>37.06 <b>(-38.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.00 (n/a)</td><td>243.12 (n/a)</td><td>239.40 (n/a)</td><td>180.40 (n/a)</td><td>59.93 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (-16.64%)</td><td>0.05 (+2.64%)</td><td>0.04 (+11.08%)</td><td>0.04 (+2.32%)</td><td>0.01 <b>(-46.61%)</b></td><td>226.20 (-2.29%)</td><td>195.64 (-4.95%)</td><td>196.10 (-9.96%)</td><td>166.00 (+19.94%)</td><td>24.68 <b>(-36.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>205.82 (n/a)</td><td>217.80 (n/a)</td><td>138.40 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (+6.90%)</td><td>0.05 (+5.68%)</td><td>0.05 (+5.30%)</td><td>0.04 <b>(+24.85%)</b></td><td>0.01 <b>(-20.82%)</b></td><td>206.70 (-19.88%)</td><td>171.14 (-8.25%)</td><td>176.00 (-5.02%)</td><td>126.20 (-6.45%)</td><td>31.46 <b>(-39.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.00 (n/a)</td><td>186.52 (n/a)</td><td>185.30 (n/a)</td><td>134.90 (n/a)</td><td>51.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (-1.15%)</td><td>0.04 (+0.46%)</td><td>0.04 (-8.34%)</td><td>0.03 <b>(+36.46%)</b></td><td>0.01 <b>(-29.18%)</b></td><td>259.10 <b>(-26.73%)</b></td><td>203.02 (-6.04%)</td><td>206.90 (+9.12%)</td><td>153.90 (+1.18%)</td><td>42.73 <b>(-48.24%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>353.60 (n/a)</td><td>216.06 (n/a)</td><td>189.60 (n/a)</td><td>152.10 (n/a)</td><td>82.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (+17.07%)</td><td>0.04 (+3.95%)</td><td>0.04 (-3.28%)</td><td>0.03 (-13.95%)</td><td>0.01 <b>(+225.49%)</b></td><td>268.20 (+16.20%)</td><td>213.06 (-0.55%)</td><td>222.50 (+3.39%)</td><td>166.10 (-14.60%)</td><td>45.01 <b>(+210.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.80 (n/a)</td><td>214.24 (n/a)</td><td>215.20 (n/a)</td><td>194.50 (n/a)</td><td>14.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.91 <b>(+33.31%)</b></td><td>0.66 (+9.61%)</td><td>0.55 (-10.40%)</td><td>0.45 (-17.08%)</td><td>0.21 <b>(+275.54%)</b></td><td>217.70 <b>(+20.54%)</b></td><td>161.18 (-2.16%)</td><td>179.80 (+11.61%)</td><td>108.20 <b>(-24.97%)</b></td><td>47.55 <b>(+221.27%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.68 (n/a)</td><td>0.60 (n/a)</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.06 (n/a)</td><td>180.60 (n/a)</td><td>164.74 (n/a)</td><td>161.10 (n/a)</td><td>144.20 (n/a)</td><td>14.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.85 (+8.61%)</td><td>0.65 (+5.44%)</td><td>0.60 (+3.80%)</td><td>0.46 (-15.27%)</td><td>0.18 <b>(+85.03%)</b></td><td>215.40 (+18.03%)</td><td>160.70 (-0.79%)</td><td>163.70 (-3.65%)</td><td>116.20 (-7.92%)</td><td>44.35 <b>(+91.86%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.10 (n/a)</td><td>182.50 (n/a)</td><td>161.98 (n/a)</td><td>169.90 (n/a)</td><td>126.20 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.70 (-1.24%)</td><td>0.53 (-10.23%)</td><td>0.50 (-17.50%)</td><td>0.44 (+13.82%)</td><td>0.10 <b>(-20.96%)</b></td><td>221.50 (-12.17%)</td><td>190.94 (+9.11%)</td><td>195.20 <b>(+21.17%)</b></td><td>141.40 (+1.22%)</td><td>31.16 <b>(-31.93%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.70 (n/a)</td><td>0.59 (n/a)</td><td>0.61 (n/a)</td><td>0.39 (n/a)</td><td>0.13 (n/a)</td><td>252.20 (n/a)</td><td>175.00 (n/a)</td><td>161.10 (n/a)</td><td>139.70 (n/a)</td><td>45.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.63 (+17.03%)</td><td>0.49 (+12.10%)</td><td>0.46 (-0.12%)</td><td>0.32 (-5.27%)</td><td>0.13 <b>(+36.02%)</b></td><td>311.50 (+5.59%)</td><td>213.36 (-8.75%)</td><td>213.30 (+0.09%)</td><td>156.00 (-14.52%)</td><td>63.70 (+15.43%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>295.00 (n/a)</td><td>233.82 (n/a)</td><td>213.10 (n/a)</td><td>182.50 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.50 (-18.59%)</td><td>0.45 (-10.66%)</td><td>0.47 (+1.78%)</td><td>0.35 (-13.87%)</td><td>0.06 <b>(-36.83%)</b></td><td>209.10 (+16.10%)</td><td>167.78 (+10.60%)</td><td>156.70 (-1.76%)</td><td>148.00 <b>(+22.82%)</b></td><td>25.38 (-8.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.41 (n/a)</td><td>0.10 (n/a)</td><td>180.10 (n/a)</td><td>151.70 (n/a)</td><td>159.50 (n/a)</td><td>120.50 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.64 (+18.95%)</td><td>0.42 (-14.25%)</td><td>0.36 <b>(-30.46%)</b></td><td>0.34 (-12.17%)</td><td>0.13 <b>(+81.75%)</b></td><td>218.90 (+13.89%)</td><td>187.62 <b>(+21.09%)</b></td><td>203.70 <b>(+43.86%)</b></td><td>114.60 (-15.92%)</td><td>41.68 <b>(+69.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.52 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>192.20 (n/a)</td><td>154.94 (n/a)</td><td>141.60 (n/a)</td><td>136.30 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.57 (-0.65%)</td><td>0.43 (-5.45%)</td><td>0.42 (-12.64%)</td><td>0.26 <b>(+20.01%)</b></td><td>0.12 (-10.62%)</td><td>283.10 (-16.69%)</td><td>185.90 (+1.09%)</td><td>174.50 (+14.50%)</td><td>130.20 (+0.62%)</td><td>61.34 <b>(-30.20%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>339.80 (n/a)</td><td>183.90 (n/a)</td><td>152.40 (n/a)</td><td>129.40 (n/a)</td><td>87.88 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.43 <b>(-22.46%)</b></td><td>0.38 (-17.54%)</td><td>0.38 (-17.06%)</td><td>0.35 (-8.98%)</td><td>0.03 <b>(-55.71%)</b></td><td>212.00 (+9.84%)</td><td>195.02 (+19.34%)</td><td>192.80 <b>(+20.58%)</b></td><td>171.30 <b>(+28.89%)</b></td><td>16.97 <b>(-37.50%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.55 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>193.00 (n/a)</td><td>163.42 (n/a)</td><td>159.90 (n/a)</td><td>132.90 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.92 (+7.16%)</td><td>0.82 (+18.29%)</td><td>0.91 <b>(+24.71%)</b></td><td>0.53 (+1.95%)</td><td>0.17 (+15.45%)</td><td>245.90 (-1.91%)</td><td>167.38 (-14.84%)</td><td>143.40 (-19.84%)</td><td>142.70 (-6.67%)</td><td>44.61 (+4.33%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.86 (n/a)</td><td>0.69 (n/a)</td><td>0.73 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>250.70 (n/a)</td><td>196.54 (n/a)</td><td>178.90 (n/a)</td><td>152.90 (n/a)</td><td>42.76 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.94 (-7.82%)</td><td>0.80 (+6.89%)</td><td>0.78 (+0.24%)</td><td>0.67 (+18.48%)</td><td>0.10 <b>(-46.18%)</b></td><td>195.10 (-15.61%)</td><td>165.46 (-9.63%)</td><td>168.40 (-0.24%)</td><td>139.30 (+8.49%)</td><td>20.60 <b>(-52.42%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>1.02 (n/a)</td><td>0.75 (n/a)</td><td>0.78 (n/a)</td><td>0.57 (n/a)</td><td>0.18 (n/a)</td><td>231.20 (n/a)</td><td>183.10 (n/a)</td><td>168.80 (n/a)</td><td>128.40 (n/a)</td><td>43.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.99 (+16.38%)</td><td>0.73 (+3.17%)</td><td>0.73 (-1.61%)</td><td>0.51 (+7.69%)</td><td>0.17 <b>(+26.35%)</b></td><td>255.50 (-7.12%)</td><td>188.58 (-2.39%)</td><td>180.40 (+1.63%)</td><td>132.40 (-14.08%)</td><td>44.94 (-4.51%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.85 (n/a)</td><td>0.70 (n/a)</td><td>0.74 (n/a)</td><td>0.48 (n/a)</td><td>0.14 (n/a)</td><td>275.10 (n/a)</td><td>193.20 (n/a)</td><td>177.50 (n/a)</td><td>154.10 (n/a)</td><td>47.07 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (+17.94%)</td><td>0.03 (+3.62%)</td><td>0.03 (+3.94%)</td><td>0.01 <b>(-20.76%)</b></td><td>0.01 <b>(+103.19%)</b></td><td>293.40 <b>(+26.19%)</b></td><td>180.62 (+4.21%)</td><td>160.10 (-3.79%)</td><td>124.40 (-15.20%)</td><td>70.34 <b>(+104.74%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.50 (n/a)</td><td>173.32 (n/a)</td><td>166.40 (n/a)</td><td>146.70 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 <b>(+23.87%)</b></td><td>0.03 (+17.58%)</td><td>0.02 <b>(+21.49%)</b></td><td>0.02 (+5.48%)</td><td>0.01 <b>(+38.86%)</b></td><td>215.20 (-5.20%)</td><td>163.78 (-13.59%)</td><td>170.10 (-17.71%)</td><td>119.50 (-19.26%)</td><td>40.78 (+6.15%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.00 (n/a)</td><td>189.54 (n/a)</td><td>206.70 (n/a)</td><td>148.00 (n/a)</td><td>38.42 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (+19.15%)</td><td>0.03 (+10.35%)</td><td>0.03 (+8.46%)</td><td>0.02 (+6.71%)</td><td>0.00 <b>(+68.34%)</b></td><td>178.50 (-6.30%)</td><td>157.56 (-8.57%)</td><td>160.30 (-7.77%)</td><td>126.30 (-16.08%)</td><td>21.59 <b>(+33.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.50 (n/a)</td><td>172.32 (n/a)</td><td>173.80 (n/a)</td><td>150.50 (n/a)</td><td>16.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.06 (+15.37%)</td><td>0.80 (+11.23%)</td><td>0.74 (+5.27%)</td><td>0.66 <b>(+21.21%)</b></td><td>0.17 (+12.22%)</td><td>201.20 (-17.47%)</td><td>170.84 (-10.38%)</td><td>178.30 (-5.01%)</td><td>124.30 (-13.32%)</td><td>31.49 (-19.68%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.92 (n/a)</td><td>0.72 (n/a)</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.15 (n/a)</td><td>243.80 (n/a)</td><td>190.62 (n/a)</td><td>187.70 (n/a)</td><td>143.40 (n/a)</td><td>39.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.07 (+10.62%)</td><td>0.85 (+10.70%)</td><td>0.82 (+10.84%)</td><td>0.60 (+7.70%)</td><td>0.20 (+14.22%)</td><td>220.90 (-7.15%)</td><td>163.06 (-9.33%)</td><td>161.90 (-9.75%)</td><td>124.00 (-9.62%)</td><td>40.62 (-4.61%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.96 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.56 (n/a)</td><td>0.18 (n/a)</td><td>237.90 (n/a)</td><td>179.84 (n/a)</td><td>179.40 (n/a)</td><td>137.20 (n/a)</td><td>42.59 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.97 (+16.07%)</td><td>0.76 (+8.31%)</td><td>0.78 (+11.90%)</td><td>0.54 (-6.92%)</td><td>0.16 <b>(+73.58%)</b></td><td>244.60 (+7.42%)</td><td>179.80 (-5.35%)</td><td>169.60 (-10.64%)</td><td>135.60 (-13.85%)</td><td>41.32 <b>(+63.15%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.70 (n/a)</td><td>0.58 (n/a)</td><td>0.09 (n/a)</td><td>227.70 (n/a)</td><td>189.96 (n/a)</td><td>189.80 (n/a)</td><td>157.40 (n/a)</td><td>25.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.13 (+19.34%)</td><td>0.89 (+10.97%)</td><td>0.87 (+16.07%)</td><td>0.70 (+4.47%)</td><td>0.16 <b>(+25.47%)</b></td><td>189.30 (-4.30%)</td><td>152.40 (-9.45%)</td><td>151.50 (-13.82%)</td><td>116.60 (-16.18%)</td><td>25.83 (+1.12%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.95 (n/a)</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.12 (n/a)</td><td>197.80 (n/a)</td><td>168.30 (n/a)</td><td>175.80 (n/a)</td><td>139.10 (n/a)</td><td>25.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.08 <b>(+28.71%)</b></td><td>0.91 <b>(+29.97%)</b></td><td>0.86 (+15.94%)</td><td>0.73 <b>(+45.70%)</b></td><td>0.16 <b>(+22.97%)</b></td><td>179.90 <b>(-31.36%)</b></td><td>149.46 <b>(-23.60%)</b></td><td>154.20 (-13.76%)</td><td>122.60 <b>(-22.31%)</b></td><td>25.43 <b>(-37.73%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.84 (n/a)</td><td>0.70 (n/a)</td><td>0.74 (n/a)</td><td>0.50 (n/a)</td><td>0.13 (n/a)</td><td>262.10 (n/a)</td><td>195.62 (n/a)</td><td>178.80 (n/a)</td><td>157.80 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (+13.70%)</td><td>0.03 (+11.29%)</td><td>0.02 (+2.08%)</td><td>0.02 <b>(+23.02%)</b></td><td>0.00 (+11.23%)</td><td>189.80 (-18.72%)</td><td>165.94 (-10.42%)</td><td>177.50 (-2.04%)</td><td>122.70 (-12.11%)</td><td>27.51 <b>(-20.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>185.24 (n/a)</td><td>181.20 (n/a)</td><td>139.60 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (+16.11%)</td><td>0.02 (-1.14%)</td><td>0.02 (-10.97%)</td><td>0.02 (-7.14%)</td><td>0.00 <b>(+71.31%)</b></td><td>204.40 (+7.69%)</td><td>171.80 (+2.94%)</td><td>181.10 (+12.28%)</td><td>125.80 (-13.84%)</td><td>30.28 <b>(+53.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>166.90 (n/a)</td><td>161.30 (n/a)</td><td>146.00 (n/a)</td><td>19.69 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.00 (+2.33%)</td><td>0.00 (+2.42%)</td><td>0.00 (+2.38%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+36.73%)</b></td><td>1047.98 (-0.00%)</td><td>967.10 (-2.52%)</td><td>951.42 (-3.24%)</td><td>926.31 (-2.42%)</td><td>48.00 <b>(+33.74%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1048.01 (n/a)</td><td>992.13 (n/a)</td><td>983.25 (n/a)</td><td>949.29 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.01 (-2.35%)</td><td>0.01 (-0.49%)</td><td>0.01 (-1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 (-15.94%)</td><td>1055.47 (+0.57%)</td><td>1016.80 (+0.65%)</td><td>1023.60 (+1.32%)</td><td>981.36 (+2.36%)</td><td>33.48 (-3.02%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1049.45 (n/a)</td><td>1010.20 (n/a)</td><td>1010.24 (n/a)</td><td>958.74 (n/a)</td><td>34.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.97 (+1.09%)</td><td>0.96 (+0.70%)</td><td>0.95 (+0.34%)</td><td>0.95 (+0.51%)</td><td>0.01 <b>(+36.24%)</b></td><td>2210.94 (-0.51%)</td><td>2192.37 (-0.70%)</td><td>2201.23 (-0.33%)</td><td>2161.43 (-1.08%)</td><td>20.94 <b>(+33.88%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2222.33 (n/a)</td><td>2207.71 (n/a)</td><td>2208.59 (n/a)</td><td>2185.08 (n/a)</td><td>15.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.35 (-15.18%)</td><td>2.75 (-3.80%)</td><td>2.58 (-2.24%)</td><td>2.50 (+2.48%)</td><td>0.35 <b>(-43.09%)</b></td><td>209.90 (-2.46%)</td><td>192.80 (+2.08%)</td><td>203.20 (+2.26%)</td><td>156.60 (+17.92%)</td><td>21.67 <b>(-32.62%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.95 (n/a)</td><td>2.86 (n/a)</td><td>2.64 (n/a)</td><td>2.44 (n/a)</td><td>0.61 (n/a)</td><td>215.20 (n/a)</td><td>188.88 (n/a)</td><td>198.70 (n/a)</td><td>132.80 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>5.57 (+5.47%)</td><td>4.09 (-15.55%)</td><td>4.53 (-5.23%)</td><td>2.23 <b>(-48.67%)</b></td><td>1.27 <b>(+263.16%)</b></td><td>470.70 <b>(+94.83%)</b></td><td>283.48 <b>(+30.30%)</b></td><td>231.50 (+5.52%)</td><td>188.10 (-5.19%)</td><td>112.01 <b>(+597.53%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>5.29 (n/a)</td><td>4.84 (n/a)</td><td>4.78 (n/a)</td><td>4.34 (n/a)</td><td>0.35 (n/a)</td><td>241.60 (n/a)</td><td>217.56 (n/a)</td><td>219.40 (n/a)</td><td>198.40 (n/a)</td><td>16.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.29 (+1.99%)</td><td>2.95 (+5.76%)</td><td>2.97 (+4.80%)</td><td>2.60 (+6.95%)</td><td>0.28 <b>(-20.20%)</b></td><td>201.30 (-6.50%)</td><td>178.88 (-5.95%)</td><td>176.50 (-4.54%)</td><td>159.20 (-1.97%)</td><td>16.90 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>3.23 (n/a)</td><td>2.79 (n/a)</td><td>2.84 (n/a)</td><td>2.44 (n/a)</td><td>0.35 (n/a)</td><td>215.30 (n/a)</td><td>190.20 (n/a)</td><td>184.90 (n/a)</td><td>162.40 (n/a)</td><td>23.58 (n/a)</td>
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
