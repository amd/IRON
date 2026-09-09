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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.09 (-12.79%)</td><td>0.08 (+3.60%)</td><td>0.08 (+14.96%)</td><td>0.07 <b>(+20.17%)</b></td><td>0.01 <b>(-51.85%)</b></td><td>182.70 (-16.77%)</td><td>162.36 (-5.99%)</td><td>156.00 (-12.99%)</td><td>144.40 (+14.69%)</td><td>16.39 <b>(-52.91%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.50 (n/a)</td><td>172.70 (n/a)</td><td>179.30 (n/a)</td><td>125.90 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.12 <b>(+29.72%)</b></td><td>0.08 (+17.14%)</td><td>0.08 (+6.75%)</td><td>0.07 <b>(+28.36%)</b></td><td>0.02 <b>(+41.60%)</b></td><td>183.90 <b>(-22.08%)</b></td><td>153.04 (-14.03%)</td><td>160.70 (-6.30%)</td><td>104.40 <b>(-22.90%)</b></td><td>32.57 (-15.66%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>178.02 (n/a)</td><td>171.50 (n/a)</td><td>135.40 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.09 (+18.73%)</td><td>0.07 (+14.13%)</td><td>0.07 <b>(+26.04%)</b></td><td>0.06 (+3.47%)</td><td>0.01 <b>(+31.66%)</b></td><td>219.80 (-3.34%)</td><td>174.26 (-11.68%)</td><td>169.20 <b>(-20.68%)</b></td><td>129.70 (-15.78%)</td><td>32.69 (+6.14%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>197.30 (n/a)</td><td>213.30 (n/a)</td><td>154.00 (n/a)</td><td>30.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (-12.38%)</td><td>0.06 (-8.78%)</td><td>0.05 (-4.13%)</td><td>0.04 (+14.99%)</td><td>0.01 <b>(-26.94%)</b></td><td>290.60 (-13.02%)</td><td>233.50 (+5.87%)</td><td>235.70 (+4.34%)</td><td>171.00 (+14.15%)</td><td>55.17 <b>(-24.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>334.10 (n/a)</td><td>220.56 (n/a)</td><td>225.90 (n/a)</td><td>149.80 (n/a)</td><td>73.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (-2.32%)</td><td>0.04 (+1.77%)</td><td>0.04 (-3.65%)</td><td>0.03 (+5.08%)</td><td>0.01 (-2.71%)</td><td>156.40 (-4.81%)</td><td>137.12 (-1.87%)</td><td>142.80 (+3.78%)</td><td>118.20 (+2.43%)</td><td>17.75 (-7.72%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>164.30 (n/a)</td><td>139.74 (n/a)</td><td>137.60 (n/a)</td><td>115.40 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (-16.35%)</td><td>0.03 (-9.51%)</td><td>0.03 (-10.39%)</td><td>0.03 (+0.62%)</td><td>0.00 <b>(-52.88%)</b></td><td>207.20 (-0.62%)</td><td>180.26 (+8.71%)</td><td>179.00 (+11.60%)</td><td>165.10 (+19.55%)</td><td>16.33 <b>(-43.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.50 (n/a)</td><td>165.82 (n/a)</td><td>160.40 (n/a)</td><td>138.10 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (-6.46%)</td><td>0.03 (+3.73%)</td><td>0.04 (+14.90%)</td><td>0.03 (-6.65%)</td><td>0.00 (+0.92%)</td><td>192.90 (+7.11%)</td><td>155.58 (-3.34%)</td><td>144.30 (-12.97%)</td><td>136.00 (+6.92%)</td><td>24.38 (+15.59%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.10 (n/a)</td><td>160.96 (n/a)</td><td>165.80 (n/a)</td><td>127.20 (n/a)</td><td>21.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (-17.73%)</td><td>0.03 (-14.25%)</td><td>0.03 (-6.59%)</td><td>0.03 (-2.65%)</td><td>0.01 <b>(-33.04%)</b></td><td>197.30 (+2.71%)</td><td>177.44 (+13.00%)</td><td>194.10 (+7.06%)</td><td>117.80 <b>(+21.57%)</b></td><td>33.75 (-19.46%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>157.02 (n/a)</td><td>181.30 (n/a)</td><td>96.90 (n/a)</td><td>41.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (+10.49%)</td><td>0.03 (+3.52%)</td><td>0.03 (+3.06%)</td><td>0.03 (-6.42%)</td><td>0.01 <b>(+64.65%)</b></td><td>187.60 (+6.83%)</td><td>156.68 (-2.14%)</td><td>156.40 (-2.98%)</td><td>122.10 (-9.49%)</td><td>24.85 <b>(+60.43%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>175.60 (n/a)</td><td>160.10 (n/a)</td><td>161.20 (n/a)</td><td>134.90 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (+18.38%)</td><td>0.03 (+18.73%)</td><td>0.03 (+13.68%)</td><td>0.02 (+19.00%)</td><td>0.01 (+19.92%)</td><td>223.40 (-15.95%)</td><td>171.10 (-15.73%)</td><td>165.50 (-12.01%)</td><td>137.60 (-15.53%)</td><td>32.94 (-15.62%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>265.80 (n/a)</td><td>203.04 (n/a)</td><td>188.10 (n/a)</td><td>162.90 (n/a)</td><td>39.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 <b>(+60.73%)</b></td><td>0.04 <b>(+44.37%)</b></td><td>0.03 <b>(+26.92%)</b></td><td>0.03 <b>(+68.39%)</b></td><td>0.01 <b>(+43.25%)</b></td><td>169.60 <b>(-40.62%)</b></td><td>142.14 <b>(-32.47%)</b></td><td>150.00 <b>(-21.18%)</b></td><td>86.10 <b>(-37.74%)</b></td><td>32.40 <b>(-52.38%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>285.60 (n/a)</td><td>210.48 (n/a)</td><td>190.30 (n/a)</td><td>138.30 (n/a)</td><td>68.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (+4.78%)</td><td>0.03 (+13.68%)</td><td>0.03 (+16.16%)</td><td>0.02 <b>(+39.62%)</b></td><td>0.00 <b>(-46.81%)</b></td><td>225.10 <b>(-28.38%)</b></td><td>197.02 (-14.51%)</td><td>187.30 (-13.89%)</td><td>178.70 (-4.54%)</td><td>19.02 <b>(-63.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>314.30 (n/a)</td><td>230.46 (n/a)</td><td>217.50 (n/a)</td><td>187.20 (n/a)</td><td>51.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>152.62 (n/a)</td><td>149.60 (n/a)</td><td>101.90 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.00 (n/a)</td><td>167.28 (n/a)</td><td>164.70 (n/a)</td><td>116.40 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>183.82 (n/a)</td><td>187.20 (n/a)</td><td>160.60 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.80 (n/a)</td><td>173.32 (n/a)</td><td>181.70 (n/a)</td><td>104.60 (n/a)</td><td>42.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>177.00 (n/a)</td><td>158.40 (n/a)</td><td>158.40 (n/a)</td><td>131.30 (n/a)</td><td>18.27 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.70 (n/a)</td><td>173.76 (n/a)</td><td>189.80 (n/a)</td><td>116.60 (n/a)</td><td>47.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>174.54 (n/a)</td><td>169.40 (n/a)</td><td>155.80 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>323.90 (n/a)</td><td>215.26 (n/a)</td><td>192.50 (n/a)</td><td>158.60 (n/a)</td><td>68.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>163.38 (n/a)</td><td>151.60 (n/a)</td><td>129.20 (n/a)</td><td>37.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.70 (n/a)</td><td>204.54 (n/a)</td><td>203.50 (n/a)</td><td>148.30 (n/a)</td><td>52.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>187.28 (n/a)</td><td>172.30 (n/a)</td><td>163.10 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>198.54 (n/a)</td><td>204.70 (n/a)</td><td>141.00 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.40 (n/a)</td><td>181.76 (n/a)</td><td>168.90 (n/a)</td><td>153.80 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>249.90 (n/a)</td><td>187.96 (n/a)</td><td>197.10 (n/a)</td><td>110.30 (n/a)</td><td>53.81 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.20 (n/a)</td><td>202.36 (n/a)</td><td>192.90 (n/a)</td><td>125.50 (n/a)</td><td>66.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.00 (n/a)</td><td>221.62 (n/a)</td><td>231.70 (n/a)</td><td>183.80 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>4.21 (-10.21%)</td><td>3.84 (-9.90%)</td><td>3.85 (-7.80%)</td><td>3.40 (-17.28%)</td><td>0.37 <b>(+53.46%)</b></td><td>2762.60 <b>(+20.90%)</b></td><td>2470.76 (+11.56%)</td><td>2442.70 (+8.46%)</td><td>2236.20 (+11.36%)</td><td>240.79 <b>(+105.76%)</b></td><td>1654.30 (-10.21%)</td><td>1508.60 (-9.90%)</td><td>1514.49 (-7.80%)</td><td>1339.10 (-17.28%)</td><td>145.53 <b>(+53.46%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>4.68 (n/a)</td><td>4.26 (n/a)</td><td>4.18 (n/a)</td><td>4.12 (n/a)</td><td>0.24 (n/a)</td><td>2285.10 (n/a)</td><td>2214.82 (n/a)</td><td>2252.10 (n/a)</td><td>2008.00 (n/a)</td><td>117.02 (n/a)</td><td>1842.33 (n/a)</td><td>1674.30 (n/a)</td><td>1642.67 (n/a)</td><td>1618.89 (n/a)</td><td>94.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.10 (-1.34%)</td><td>0.93 (-6.02%)</td><td>0.96 (-7.84%)</td><td>0.73 (-5.96%)</td><td>0.14 (-2.65%)</td><td>302.80 (+6.36%)</td><td>243.48 (+6.47%)</td><td>231.60 (+8.53%)</td><td>200.90 (+1.36%)</td><td>37.77 (+6.40%)</td><td>46.98 (-1.34%)</td><td>39.47 (-6.02%)</td><td>40.76 (-7.84%)</td><td>31.17 (-5.96%)</td><td>5.77 (-2.65%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.12 (n/a)</td><td>0.98 (n/a)</td><td>1.04 (n/a)</td><td>0.78 (n/a)</td><td>0.14 (n/a)</td><td>284.70 (n/a)</td><td>228.68 (n/a)</td><td>213.40 (n/a)</td><td>198.20 (n/a)</td><td>35.50 (n/a)</td><td>47.62 (n/a)</td><td>42.00 (n/a)</td><td>44.23 (n/a)</td><td>33.15 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.04 <b>(-22.02%)</b></td><td>0.90 (-12.68%)</td><td>0.91 (-17.04%)</td><td>0.67 (+0.64%)</td><td>0.16 <b>(-36.97%)</b></td><td>329.80 (-0.66%)</td><td>251.96 (+11.43%)</td><td>244.00 <b>(+20.55%)</b></td><td>211.90 <b>(+28.27%)</b></td><td>48.52 <b>(-23.87%)</b></td><td>44.55 <b>(-22.02%)</b></td><td>38.47 (-12.68%)</td><td>38.67 (-17.04%)</td><td>28.61 (+0.64%)</td><td>6.64 <b>(-36.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.34 (n/a)</td><td>1.03 (n/a)</td><td>1.09 (n/a)</td><td>0.67 (n/a)</td><td>0.25 (n/a)</td><td>332.00 (n/a)</td><td>226.12 (n/a)</td><td>202.40 (n/a)</td><td>165.20 (n/a)</td><td>63.73 (n/a)</td><td>57.12 (n/a)</td><td>44.05 (n/a)</td><td>46.62 (n/a)</td><td>28.43 (n/a)</td><td>10.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.52 (-0.85%)</td><td>0.52 (-0.19%)</td><td>0.52 (-0.04%)</td><td>0.52 (+0.05%)</td><td>0.00 <b>(-63.35%)</b></td><td>48653.70 (-0.05%)</td><td>48502.76 (+0.18%)</td><td>48467.00 (+0.04%)</td><td>48456.60 (+0.86%)</td><td>84.77 <b>(-63.00%)</b></td><td>354.54 (-0.85%)</td><td>354.20 (-0.19%)</td><td>354.46 (-0.04%)</td><td>353.11 (+0.05%)</td><td>0.62 <b>(-63.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48676.40 (n/a)</td><td>48413.60 (n/a)</td><td>48445.50 (n/a)</td><td>48043.70 (n/a)</td><td>229.08 (n/a)</td><td>357.59 (n/a)</td><td>354.86 (n/a)</td><td>354.62 (n/a)</td><td>352.94 (n/a)</td><td>1.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.90 (-1.53%)</td><td>0.89 (+0.04%)</td><td>0.89 (+0.67%)</td><td>0.89 (+1.41%)</td><td>0.01 <b>(-62.50%)</b></td><td>28420.40 (-1.39%)</td><td>28256.42 (-0.07%)</td><td>28342.30 (-0.67%)</td><td>27934.80 (+1.55%)</td><td>197.83 <b>(-62.42%)</b></td><td>615.00 (-1.53%)</td><td>608.02 (+0.04%)</td><td>606.16 (+0.67%)</td><td>604.49 (+1.41%)</td><td>4.28 <b>(-62.50%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.02 (n/a)</td><td>28821.90 (n/a)</td><td>28275.32 (n/a)</td><td>28532.60 (n/a)</td><td>27507.90 (n/a)</td><td>526.49 (n/a)</td><td>624.54 (n/a)</td><td>607.76 (n/a)</td><td>602.11 (n/a)</td><td>596.07 (n/a)</td><td>11.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.33 (+1.84%)</td><td>3.23 (+1.82%)</td><td>3.21 (+1.19%)</td><td>3.13 (+1.45%)</td><td>0.08 <b>(+21.64%)</b></td><td>8042.70 (-1.43%)</td><td>7786.20 (-1.77%)</td><td>7848.70 (-1.17%)</td><td>7566.90 (-1.81%)</td><td>197.07 (+17.30%)</td><td>2270.41 (+1.84%)</td><td>2207.59 (+1.82%)</td><td>2188.89 (+1.19%)</td><td>2136.09 (+1.45%)</td><td>55.83 <b>(+21.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.27 (n/a)</td><td>3.18 (n/a)</td><td>3.17 (n/a)</td><td>3.08 (n/a)</td><td>0.07 (n/a)</td><td>8159.70 (n/a)</td><td>7926.62 (n/a)</td><td>7942.00 (n/a)</td><td>7706.40 (n/a)</td><td>168.00 (n/a)</td><td>2229.31 (n/a)</td><td>2168.14 (n/a)</td><td>2163.16 (n/a)</td><td>2105.46 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.61 (-3.37%)</td><td>3.52 (+3.79%)</td><td>3.58 (-1.21%)</td><td>3.25 (+10.81%)</td><td>0.15 <b>(-61.34%)</b></td><td>2481.30 (-9.75%)</td><td>2295.78 (-4.57%)</td><td>2252.50 (+1.23%)</td><td>2231.20 (+3.49%)</td><td>104.38 <b>(-63.87%)</b></td><td>947.43 (-3.37%)</td><td>922.23 (+3.79%)</td><td>938.48 (-1.21%)</td><td>851.96 (+10.81%)</td><td>39.59 <b>(-61.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.74 (n/a)</td><td>3.39 (n/a)</td><td>3.62 (n/a)</td><td>2.93 (n/a)</td><td>0.39 (n/a)</td><td>2749.40 (n/a)</td><td>2405.78 (n/a)</td><td>2225.20 (n/a)</td><td>2156.00 (n/a)</td><td>288.93 (n/a)</td><td>980.49 (n/a)</td><td>888.52 (n/a)</td><td>949.98 (n/a)</td><td>768.86 (n/a)</td><td>102.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.33 (-12.81%)</td><td>0.31 (-12.36%)</td><td>0.31 (-14.23%)</td><td>0.28 (-13.75%)</td><td>0.02 (-19.46%)</td><td>4416.90 (+15.94%)</td><td>4041.16 (+14.04%)</td><td>4009.00 (+16.59%)</td><td>3815.10 (+14.69%)</td><td>252.88 (+5.65%)</td><td>17.59 (-12.81%)</td><td>16.66 (-12.36%)</td><td>16.74 (-14.23%)</td><td>15.19 (-13.75%)</td><td>1.01 (-19.46%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.02 (n/a)</td><td>3809.50 (n/a)</td><td>3543.70 (n/a)</td><td>3438.50 (n/a)</td><td>3326.40 (n/a)</td><td>239.35 (n/a)</td><td>20.17 (n/a)</td><td>19.01 (n/a)</td><td>19.52 (n/a)</td><td>17.62 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>6.38 (-6.66%)</td><td>4.79 (+8.09%)</td><td>4.77 <b>(+29.34%)</b></td><td>3.24 (-0.92%)</td><td>1.12 <b>(-24.80%)</b></td><td>2053.50 (+0.92%)</td><td>1454.30 (-10.00%)</td><td>1395.90 <b>(-22.69%)</b></td><td>1041.90 (+7.14%)</td><td>368.60 (-16.25%)</td><td>1972.59 (-6.66%)</td><td>1480.94 (+8.09%)</td><td>1472.32 <b>(+29.34%)</b></td><td>1000.84 (-0.92%)</td><td>344.74 <b>(-24.80%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>6.84 (n/a)</td><td>4.43 (n/a)</td><td>3.68 (n/a)</td><td>3.27 (n/a)</td><td>1.48 (n/a)</td><td>2034.70 (n/a)</td><td>1615.80 (n/a)</td><td>1805.50 (n/a)</td><td>972.50 (n/a)</td><td>440.11 (n/a)</td><td>2113.28 (n/a)</td><td>1370.16 (n/a)</td><td>1138.33 (n/a)</td><td>1010.09 (n/a)</td><td>458.42 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.49 (n/a)</td><td>11.39 (n/a)</td><td>10.98 (n/a)</td><td>10.50 (n/a)</td><td>1.20 (n/a)</td><td>13.49 (n/a)</td><td>11.39 (n/a)</td><td>10.97 (n/a)</td><td>10.50 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>25.37 (+2.16%)</td><td>24.26 (+3.85%)</td><td>24.02 (-1.41%)</td><td>23.71 (+15.07%)</td><td>0.65 <b>(-63.19%)</b></td><td>25.36 (+2.16%)</td><td>24.24 (+3.85%)</td><td>24.01 (-1.41%)</td><td>23.70 (+15.07%)</td><td>0.65 <b>(-63.19%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>24.84 (n/a)</td><td>23.36 (n/a)</td><td>24.37 (n/a)</td><td>20.60 (n/a)</td><td>1.78 (n/a)</td><td>24.82 (n/a)</td><td>23.34 (n/a)</td><td>24.35 (n/a)</td><td>20.59 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>40.44 (-2.18%)</td><td>39.70 (+0.20%)</td><td>39.83 (-2.39%)</td><td>38.78 (+8.80%)</td><td>0.60 <b>(-74.82%)</b></td><td>40.41 (-2.18%)</td><td>39.67 (+0.20%)</td><td>39.80 (-2.39%)</td><td>38.76 (+8.80%)</td><td>0.60 <b>(-74.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>41.34 (n/a)</td><td>39.62 (n/a)</td><td>40.80 (n/a)</td><td>35.65 (n/a)</td><td>2.39 (n/a)</td><td>41.32 (n/a)</td><td>39.59 (n/a)</td><td>40.78 (n/a)</td><td>35.63 (n/a)</td><td>2.39 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>45.26 (+1.73%)</td><td>43.06 (-0.13%)</td><td>42.86 (-0.48%)</td><td>41.54 (-0.22%)</td><td>1.36 <b>(+33.14%)</b></td><td>45.23 (+1.73%)</td><td>43.03 (-0.13%)</td><td>42.83 (-0.48%)</td><td>41.51 (-0.22%)</td><td>1.35 <b>(+33.14%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>44.48 (n/a)</td><td>43.11 (n/a)</td><td>43.06 (n/a)</td><td>41.63 (n/a)</td><td>1.02 (n/a)</td><td>44.46 (n/a)</td><td>43.09 (n/a)</td><td>43.04 (n/a)</td><td>41.60 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.36 (n/a)</td><td>11.81 (n/a)</td><td>11.20 (n/a)</td><td>10.97 (n/a)</td><td>1.02 (n/a)</td><td>13.35 (n/a)</td><td>11.81 (n/a)</td><td>11.20 (n/a)</td><td>10.96 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>24.91 (+2.68%)</td><td>22.33 (-6.35%)</td><td>23.88 (-1.18%)</td><td>15.61 <b>(-30.63%)</b></td><td>3.81 <b>(+403.51%)</b></td><td>24.90 (+2.68%)</td><td>22.32 (-6.35%)</td><td>23.87 (-1.18%)</td><td>15.60 <b>(-30.63%)</b></td><td>3.81 <b>(+403.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>24.26 (n/a)</td><td>23.85 (n/a)</td><td>24.17 (n/a)</td><td>22.50 (n/a)</td><td>0.76 (n/a)</td><td>24.25 (n/a)</td><td>23.83 (n/a)</td><td>24.15 (n/a)</td><td>22.48 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>41.11 (-1.26%)</td><td>39.76 (+4.31%)</td><td>40.08 (+4.82%)</td><td>37.80 (+7.92%)</td><td>1.47 <b>(-42.76%)</b></td><td>41.08 (-1.26%)</td><td>39.74 (+4.31%)</td><td>40.05 (+4.82%)</td><td>37.78 (+7.92%)</td><td>1.46 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>41.63 (n/a)</td><td>38.12 (n/a)</td><td>38.23 (n/a)</td><td>35.03 (n/a)</td><td>2.56 (n/a)</td><td>41.61 (n/a)</td><td>38.09 (n/a)</td><td>38.21 (n/a)</td><td>35.01 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>45.12 (-1.05%)</td><td>43.59 (+0.30%)</td><td>43.73 (+0.71%)</td><td>42.10 (-0.17%)</td><td>1.19 (-12.64%)</td><td>45.09 (-1.05%)</td><td>43.57 (+0.30%)</td><td>43.70 (+0.71%)</td><td>42.08 (-0.17%)</td><td>1.18 (-12.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>45.60 (n/a)</td><td>43.46 (n/a)</td><td>43.42 (n/a)</td><td>42.18 (n/a)</td><td>1.36 (n/a)</td><td>45.57 (n/a)</td><td>43.44 (n/a)</td><td>43.39 (n/a)</td><td>42.15 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>9.64 (+4.09%)</td><td>9.02 (+4.07%)</td><td>9.16 (+5.32%)</td><td>8.39 (+4.58%)</td><td>0.47 (-3.12%)</td><td>9.62 (+4.09%)</td><td>9.00 (+4.07%)</td><td>9.14 (+5.32%)</td><td>8.37 (+4.58%)</td><td>0.47 (-3.12%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>9.26 (n/a)</td><td>8.67 (n/a)</td><td>8.70 (n/a)</td><td>8.02 (n/a)</td><td>0.49 (n/a)</td><td>9.24 (n/a)</td><td>8.65 (n/a)</td><td>8.68 (n/a)</td><td>8.00 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.09 <b>(+21.58%)</b></td><td>0.88 (+3.82%)</td><td>0.90 (+3.17%)</td><td>0.49 <b>(-35.59%)</b></td><td>0.24 <b>(+320.78%)</b></td><td>1.07 <b>(+21.58%)</b></td><td>0.87 (+3.82%)</td><td>0.88 (+3.17%)</td><td>0.48 <b>(-35.59%)</b></td><td>0.23 <b>(+320.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.90 (n/a)</td><td>0.85 (n/a)</td><td>0.87 (n/a)</td><td>0.76 (n/a)</td><td>0.06 (n/a)</td><td>0.88 (n/a)</td><td>0.84 (n/a)</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.30 (+13.55%)</td><td>1.20 (+11.13%)</td><td>1.22 (+12.06%)</td><td>1.10 (+8.29%)</td><td>0.07 <b>(+44.05%)</b></td><td>1.29 (+13.55%)</td><td>1.19 (+11.13%)</td><td>1.20 (+12.06%)</td><td>1.09 (+8.29%)</td><td>0.07 <b>(+44.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.15 (n/a)</td><td>1.08 (n/a)</td><td>1.09 (n/a)</td><td>1.01 (n/a)</td><td>0.05 (n/a)</td><td>1.13 (n/a)</td><td>1.07 (n/a)</td><td>1.07 (n/a)</td><td>1.00 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>19.31 (+11.04%)</td><td>17.88 (+13.24%)</td><td>18.47 (+17.38%)</td><td>15.56 (+6.75%)</td><td>1.52 <b>(+45.28%)</b></td><td>19.09 (+11.04%)</td><td>17.68 (+13.24%)</td><td>18.25 (+17.38%)</td><td>15.38 (+6.75%)</td><td>1.50 <b>(+45.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>17.39 (n/a)</td><td>15.79 (n/a)</td><td>15.73 (n/a)</td><td>14.57 (n/a)</td><td>1.05 (n/a)</td><td>17.19 (n/a)</td><td>15.61 (n/a)</td><td>15.55 (n/a)</td><td>14.41 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.79 (+0.66%)</td><td>13.31 (-0.55%)</td><td>13.32 (-0.97%)</td><td>12.59 (-3.05%)</td><td>0.50 <b>(+87.37%)</b></td><td>13.55 (+0.66%)</td><td>13.08 (-0.55%)</td><td>13.09 (-0.97%)</td><td>12.37 (-3.05%)</td><td>0.49 <b>(+87.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>13.70 (n/a)</td><td>13.38 (n/a)</td><td>13.45 (n/a)</td><td>12.99 (n/a)</td><td>0.27 (n/a)</td><td>13.46 (n/a)</td><td>13.15 (n/a)</td><td>13.22 (n/a)</td><td>12.76 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>8.43 (-9.70%)</td><td>7.74 (-2.92%)</td><td>8.00 (+2.49%)</td><td>7.05 (+3.54%)</td><td>0.58 <b>(-37.73%)</b></td><td>8.29 (-9.70%)</td><td>7.60 (-2.92%)</td><td>7.86 (+2.49%)</td><td>6.92 (+3.54%)</td><td>0.57 <b>(-37.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>9.34 (n/a)</td><td>7.97 (n/a)</td><td>7.80 (n/a)</td><td>6.81 (n/a)</td><td>0.94 (n/a)</td><td>9.18 (n/a)</td><td>7.83 (n/a)</td><td>7.67 (n/a)</td><td>6.69 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>7.08 <b>(+23.45%)</b></td><td>6.21 (+12.43%)</td><td>5.97 (+7.87%)</td><td>5.43 (+4.22%)</td><td>0.72 <b>(+230.57%)</b></td><td>6.97 <b>(+23.45%)</b></td><td>6.11 (+12.43%)</td><td>5.88 (+7.87%)</td><td>5.34 (+4.22%)</td><td>0.71 <b>(+230.57%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>5.74 (n/a)</td><td>5.52 (n/a)</td><td>5.54 (n/a)</td><td>5.21 (n/a)</td><td>0.22 (n/a)</td><td>5.64 (n/a)</td><td>5.44 (n/a)</td><td>5.45 (n/a)</td><td>5.13 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.45 (n/a)</td><td>12.67 (n/a)</td><td>12.93 (n/a)</td><td>11.77 (n/a)</td><td>0.71 (n/a)</td><td>13.44 (n/a)</td><td>12.66 (n/a)</td><td>12.92 (n/a)</td><td>11.77 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.42 (n/a)</td><td>12.56 (n/a)</td><td>12.78 (n/a)</td><td>10.98 (n/a)</td><td>0.94 (n/a)</td><td>13.41 (n/a)</td><td>12.56 (n/a)</td><td>12.78 (n/a)</td><td>10.97 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>186.04 (n/a)</td><td>176.90 (n/a)</td><td>134.10 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.70 (n/a)</td><td>179.04 (n/a)</td><td>171.90 (n/a)</td><td>122.50 (n/a)</td><td>42.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.60 (n/a)</td><td>175.68 (n/a)</td><td>167.80 (n/a)</td><td>153.20 (n/a)</td><td>23.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.20 (n/a)</td><td>190.56 (n/a)</td><td>188.00 (n/a)</td><td>115.90 (n/a)</td><td>53.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>185.82 (n/a)</td><td>189.20 (n/a)</td><td>153.60 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>193.02 (n/a)</td><td>185.80 (n/a)</td><td>158.30 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>196.84 (n/a)</td><td>207.50 (n/a)</td><td>150.80 (n/a)</td><td>40.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>326.30 (n/a)</td><td>242.54 (n/a)</td><td>267.30 (n/a)</td><td>142.60 (n/a)</td><td>75.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-2.84%)</td><td>0.06 (+7.20%)</td><td>0.06 (+5.22%)</td><td>0.05 <b>(+53.38%)</b></td><td>0.00 <b>(-74.41%)</b></td><td>158.10 <b>(-34.80%)</b></td><td>148.94 (-10.49%)</td><td>148.50 (-4.99%)</td><td>138.80 (+2.97%)</td><td>7.16 <b>(-83.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.50 (n/a)</td><td>166.40 (n/a)</td><td>156.30 (n/a)</td><td>134.80 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-8.29%)</td><td>0.04 (-12.20%)</td><td>0.04 (-10.79%)</td><td>0.02 <b>(-43.63%)</b></td><td>0.01 <b>(+22.40%)</b></td><td>400.20 <b>(+77.39%)</b></td><td>224.40 <b>(+23.11%)</b></td><td>195.40 (+12.11%)</td><td>142.80 (+9.09%)</td><td>101.68 <b>(+142.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>182.28 (n/a)</td><td>174.30 (n/a)</td><td>130.90 (n/a)</td><td>41.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-17.33%)</td><td>0.05 (-11.59%)</td><td>0.05 (-15.97%)</td><td>0.04 (+18.03%)</td><td>0.01 <b>(-46.74%)</b></td><td>202.70 (-15.26%)</td><td>171.56 (+8.46%)</td><td>164.90 (+18.98%)</td><td>140.40 <b>(+21.03%)</b></td><td>25.10 <b>(-47.46%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.20 (n/a)</td><td>158.18 (n/a)</td><td>138.60 (n/a)</td><td>116.00 (n/a)</td><td>47.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (+1.46%)</td><td>0.05 (-14.70%)</td><td>0.04 <b>(-23.35%)</b></td><td>0.03 (-10.71%)</td><td>0.01 <b>(+21.33%)</b></td><td>240.60 (+12.01%)</td><td>188.02 (+19.00%)</td><td>186.80 <b>(+30.45%)</b></td><td>132.80 (-1.48%)</td><td>42.04 <b>(+29.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>158.00 (n/a)</td><td>143.20 (n/a)</td><td>134.80 (n/a)</td><td>32.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (+19.17%)</td><td>0.05 (+10.82%)</td><td>0.04 (-3.45%)</td><td>0.04 (+9.75%)</td><td>0.01 <b>(+42.83%)</b></td><td>200.40 (-8.87%)</td><td>168.18 (-8.33%)</td><td>188.40 (+3.57%)</td><td>119.00 (-16.08%)</td><td>37.32 (+8.91%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>183.46 (n/a)</td><td>181.90 (n/a)</td><td>141.80 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (-7.71%)</td><td>0.05 (+1.57%)</td><td>0.05 (+5.67%)</td><td>0.04 (-2.30%)</td><td>0.01 (-9.34%)</td><td>233.90 (+2.32%)</td><td>182.70 (-1.85%)</td><td>167.40 (-5.37%)</td><td>151.10 (+8.39%)</td><td>35.43 (-1.44%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.60 (n/a)</td><td>186.14 (n/a)</td><td>176.90 (n/a)</td><td>139.40 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (+4.31%)</td><td>0.05 (+7.10%)</td><td>0.05 (+0.50%)</td><td>0.05 <b>(+36.98%)</b></td><td>0.01 <b>(-28.31%)</b></td><td>176.20 <b>(-27.01%)</b></td><td>161.68 (-9.07%)</td><td>168.60 (-0.47%)</td><td>126.30 (-4.17%)</td><td>20.18 <b>(-51.49%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.40 (n/a)</td><td>177.80 (n/a)</td><td>169.40 (n/a)</td><td>131.80 (n/a)</td><td>41.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (+5.17%)</td><td>0.05 (+10.56%)</td><td>0.05 (+6.66%)</td><td>0.04 (+19.79%)</td><td>0.00 <b>(-24.04%)</b></td><td>194.60 (-16.52%)</td><td>174.38 (-10.37%)</td><td>177.40 (-6.24%)</td><td>156.60 (-4.92%)</td><td>16.99 <b>(-40.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>194.56 (n/a)</td><td>189.20 (n/a)</td><td>164.70 (n/a)</td><td>28.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 <b>(+45.44%)</b></td><td>0.05 <b>(+30.77%)</b></td><td>0.05 <b>(+37.83%)</b></td><td>0.04 <b>(+20.66%)</b></td><td>0.02 <b>(+57.73%)</b></td><td>205.70 (-17.12%)</td><td>157.28 <b>(-22.57%)</b></td><td>160.40 <b>(-27.45%)</b></td><td>101.90 <b>(-31.24%)</b></td><td>36.91 (-13.86%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>203.12 (n/a)</td><td>221.10 (n/a)</td><td>148.20 (n/a)</td><td>42.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (-3.90%)</td><td>0.04 (+5.01%)</td><td>0.04 <b>(+20.62%)</b></td><td>0.03 (+4.71%)</td><td>0.00 <b>(-43.72%)</b></td><td>234.60 (-4.48%)</td><td>203.20 (-6.32%)</td><td>197.70 (-17.07%)</td><td>180.10 (+4.10%)</td><td>20.24 <b>(-44.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.60 (n/a)</td><td>216.90 (n/a)</td><td>238.40 (n/a)</td><td>173.00 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (+19.03%)</td><td>0.04 (+3.91%)</td><td>0.04 (-3.49%)</td><td>0.03 <b>(-23.24%)</b></td><td>0.01 <b>(+219.76%)</b></td><td>272.50 <b>(+30.32%)</b></td><td>201.52 (+1.14%)</td><td>215.60 (+3.65%)</td><td>145.40 (-15.95%)</td><td>52.20 <b>(+237.34%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.10 (n/a)</td><td>199.24 (n/a)</td><td>208.00 (n/a)</td><td>173.00 (n/a)</td><td>15.47 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 <b>(-23.48%)</b></td><td>0.03 (-14.42%)</td><td>0.03 (-8.33%)</td><td>0.03 (+4.48%)</td><td>0.00 <b>(-55.55%)</b></td><td>316.60 (-4.29%)</td><td>255.10 (+12.67%)</td><td>240.30 (+9.08%)</td><td>233.00 <b>(+30.68%)</b></td><td>34.68 <b>(-43.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.80 (n/a)</td><td>226.42 (n/a)</td><td>220.30 (n/a)</td><td>178.30 (n/a)</td><td>61.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 <b>(+42.95%)</b></td><td>0.05 (+15.52%)</td><td>0.05 (+1.25%)</td><td>0.04 <b>(+45.60%)</b></td><td>0.01 <b>(+40.62%)</b></td><td>218.70 <b>(-31.31%)</b></td><td>181.62 (-13.83%)</td><td>179.40 (-1.21%)</td><td>116.50 <b>(-30.03%)</b></td><td>41.08 <b>(-34.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>318.40 (n/a)</td><td>210.76 (n/a)</td><td>181.60 (n/a)</td><td>166.50 (n/a)</td><td>62.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 <b>(+40.67%)</b></td><td>0.05 (+10.43%)</td><td>0.05 (+3.69%)</td><td>0.04 (+0.37%)</td><td>0.02 <b>(+117.51%)</b></td><td>202.70 (-0.34%)</td><td>164.14 (-5.63%)</td><td>161.40 (-3.53%)</td><td>102.70 <b>(-28.88%)</b></td><td>40.58 <b>(+50.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>173.94 (n/a)</td><td>167.30 (n/a)</td><td>144.40 (n/a)</td><td>26.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (-15.40%)</td><td>0.04 (-0.51%)</td><td>0.04 (+6.86%)</td><td>0.04 (+7.15%)</td><td>0.00 <b>(-67.84%)</b></td><td>199.50 (-6.69%)</td><td>188.92 (-0.66%)</td><td>184.10 (-6.45%)</td><td>182.00 (+18.18%)</td><td>8.31 <b>(-64.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>190.18 (n/a)</td><td>196.80 (n/a)</td><td>154.00 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 <b>(+24.75%)</b></td><td>0.05 <b>(+23.58%)</b></td><td>0.05 (+11.09%)</td><td>0.04 <b>(+85.43%)</b></td><td>0.01 (-17.68%)</td><td>190.60 <b>(-46.07%)</b></td><td>168.70 <b>(-23.53%)</b></td><td>174.40 (-9.96%)</td><td>125.10 (-19.86%)</td><td>26.07 <b>(-66.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>353.40 (n/a)</td><td>220.60 (n/a)</td><td>193.70 (n/a)</td><td>156.10 (n/a)</td><td>78.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (-12.28%)</td><td>0.04 (-1.34%)</td><td>0.04 (-2.58%)</td><td>0.04 (+5.55%)</td><td>0.00 <b>(-48.47%)</b></td><td>208.20 (-5.23%)</td><td>188.82 (-0.13%)</td><td>188.40 (+2.61%)</td><td>169.30 (+13.93%)</td><td>16.13 <b>(-45.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>189.06 (n/a)</td><td>183.60 (n/a)</td><td>148.60 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (-9.74%)</td><td>0.04 (-12.09%)</td><td>0.04 (-6.78%)</td><td>0.03 <b>(-26.74%)</b></td><td>0.01 (+2.63%)</td><td>306.90 <b>(+36.46%)</b></td><td>217.10 (+15.70%)</td><td>209.50 (+7.27%)</td><td>157.60 (+10.83%)</td><td>54.66 <b>(+60.40%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>187.64 (n/a)</td><td>195.30 (n/a)</td><td>142.20 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.18 (-0.16%)</td><td>0.18 (-0.38%)</td><td>0.18 (-0.51%)</td><td>0.18 (-0.25%)</td><td>0.00 (+12.36%)</td><td>47731.80 (+0.25%)</td><td>47615.42 (+0.38%)</td><td>47646.20 (+0.51%)</td><td>47437.90 (+0.16%)</td><td>116.57 (+12.77%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47613.30 (n/a)</td><td>47435.68 (n/a)</td><td>47405.20 (n/a)</td><td>47364.10 (n/a)</td><td>103.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.22 (+14.63%)</td><td>0.17 (+2.53%)</td><td>0.17 (-0.01%)</td><td>0.14 (-3.75%)</td><td>0.03 <b>(+99.66%)</b></td><td>172.80 (+3.91%)</td><td>145.98 (-0.30%)</td><td>147.60 (+0.00%)</td><td>110.80 (-12.76%)</td><td>27.38 <b>(+85.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>166.30 (n/a)</td><td>146.42 (n/a)</td><td>147.60 (n/a)</td><td>127.00 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.30 (-8.67%)</td><td>0.24 <b>(-21.33%)</b></td><td>0.24 <b>(-24.96%)</b></td><td>0.19 <b>(-33.13%)</b></td><td>0.04 <b>(+123.45%)</b></td><td>216.60 <b>(+49.48%)</b></td><td>173.96 <b>(+29.51%)</b></td><td>174.10 <b>(+33.21%)</b></td><td>138.60 (+9.48%)</td><td>28.79 <b>(+265.84%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>144.90 (n/a)</td><td>134.32 (n/a)</td><td>130.70 (n/a)</td><td>126.60 (n/a)</td><td>7.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (-0.86%)</td><td>0.03 (-6.24%)</td><td>0.03 (-0.49%)</td><td>0.02 (-5.03%)</td><td>0.01 (+14.82%)</td><td>210.30 (+5.26%)</td><td>174.04 (+7.67%)</td><td>168.30 (+0.54%)</td><td>133.80 (+0.83%)</td><td>33.76 <b>(+27.10%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>161.64 (n/a)</td><td>167.40 (n/a)</td><td>132.70 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-11.24%)</td><td>0.05 (-13.57%)</td><td>0.05 <b>(-21.64%)</b></td><td>0.04 <b>(+71.76%)</b></td><td>0.01 <b>(-49.10%)</b></td><td>219.20 <b>(-41.80%)</b></td><td>181.36 (-0.06%)</td><td>172.90 <b>(+27.60%)</b></td><td>136.50 (+12.72%)</td><td>35.17 <b>(-67.85%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>376.60 (n/a)</td><td>181.46 (n/a)</td><td>135.50 (n/a)</td><td>121.10 (n/a)</td><td>109.37 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.11 (+0.68%)</td><td>0.07 (-2.57%)</td><td>0.06 (-11.63%)</td><td>0.06 (-0.73%)</td><td>0.02 (+2.26%)</td><td>221.30 (+0.77%)</td><td>181.96 (+2.69%)</td><td>192.60 (+13.16%)</td><td>114.10 (-0.70%)</td><td>41.41 (-2.21%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.60 (n/a)</td><td>177.20 (n/a)</td><td>170.20 (n/a)</td><td>114.90 (n/a)</td><td>42.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 <b>(-26.65%)</b></td><td>0.05 (-19.96%)</td><td>0.05 <b>(-22.30%)</b></td><td>0.04 (-8.40%)</td><td>0.01 <b>(-52.55%)</b></td><td>183.20 (+9.18%)</td><td>163.26 <b>(+22.48%)</b></td><td>170.90 <b>(+28.69%)</b></td><td>143.20 <b>(+36.25%)</b></td><td>18.04 <b>(-29.93%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>133.30 (n/a)</td><td>132.80 (n/a)</td><td>105.10 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (-1.32%)</td><td>0.06 (+8.12%)</td><td>0.06 (+1.25%)</td><td>0.05 <b>(+79.20%)</b></td><td>0.01 <b>(-58.16%)</b></td><td>202.80 <b>(-44.19%)</b></td><td>177.74 (-15.89%)</td><td>176.80 (-1.23%)</td><td>149.10 (+1.36%)</td><td>20.42 <b>(-76.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>363.40 (n/a)</td><td>211.32 (n/a)</td><td>179.00 (n/a)</td><td>147.10 (n/a)</td><td>88.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-6.91%)</td><td>0.05 (-6.29%)</td><td>0.05 (-11.06%)</td><td>0.04 (-2.44%)</td><td>0.01 <b>(-25.57%)</b></td><td>184.10 (+2.51%)</td><td>160.88 (+5.93%)</td><td>161.50 (+12.39%)</td><td>138.40 (+7.45%)</td><td>18.92 (-19.06%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.60 (n/a)</td><td>151.88 (n/a)</td><td>143.70 (n/a)</td><td>128.80 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 <b>(-25.12%)</b></td><td>0.05 (-12.92%)</td><td>0.05 (+0.25%)</td><td>0.05 (+5.75%)</td><td>0.01 <b>(-68.78%)</b></td><td>214.20 (-5.47%)</td><td>190.50 (+8.08%)</td><td>192.90 (-0.26%)</td><td>160.50 <b>(+33.53%)</b></td><td>19.37 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>226.60 (n/a)</td><td>176.26 (n/a)</td><td>193.40 (n/a)</td><td>120.20 (n/a)</td><td>49.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 <b>(-26.33%)</b></td><td>0.04 <b>(-30.06%)</b></td><td>0.04 <b>(-25.01%)</b></td><td>0.02 <b>(-49.23%)</b></td><td>0.01 <b>(+51.71%)</b></td><td>348.20 <b>(+96.95%)</b></td><td>231.84 <b>(+50.82%)</b></td><td>198.20 <b>(+33.29%)</b></td><td>176.40 <b>(+35.69%)</b></td><td>71.90 <b>(+302.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>153.72 (n/a)</td><td>148.70 (n/a)</td><td>130.00 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (-4.85%)</td><td>0.05 (-15.98%)</td><td>0.05 <b>(-29.46%)</b></td><td>0.04 (-0.46%)</td><td>0.01 <b>(-20.93%)</b></td><td>210.80 (+0.48%)</td><td>181.42 (+17.64%)</td><td>189.50 <b>(+41.74%)</b></td><td>136.50 (+5.16%)</td><td>27.66 (-18.72%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>154.22 (n/a)</td><td>133.70 (n/a)</td><td>129.80 (n/a)</td><td>34.03 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-17.88%)</td><td>0.05 (-17.34%)</td><td>0.05 <b>(-30.86%)</b></td><td>0.04 (-2.80%)</td><td>0.01 <b>(-48.42%)</b></td><td>209.90 (+2.89%)</td><td>174.80 (+15.72%)</td><td>175.30 <b>(+44.64%)</b></td><td>137.80 <b>(+21.84%)</b></td><td>28.54 <b>(-36.78%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>204.00 (n/a)</td><td>151.06 (n/a)</td><td>121.20 (n/a)</td><td>113.10 (n/a)</td><td>45.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (+14.75%)</td><td>0.05 (-9.86%)</td><td>0.05 (-7.85%)</td><td>0.04 (-19.99%)</td><td>0.02 <b>(+44.12%)</b></td><td>255.60 <b>(+24.99%)</b></td><td>193.86 (+15.21%)</td><td>194.80 (+8.52%)</td><td>114.10 (-12.83%)</td><td>51.51 <b>(+52.03%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>168.26 (n/a)</td><td>179.50 (n/a)</td><td>130.90 (n/a)</td><td>33.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 <b>(-36.95%)</b></td><td>0.04 <b>(-28.26%)</b></td><td>0.04 <b>(-21.43%)</b></td><td>0.03 <b>(-21.88%)</b></td><td>0.01 <b>(-52.19%)</b></td><td>269.40 <b>(+27.98%)</b></td><td>211.96 <b>(+36.22%)</b></td><td>196.80 <b>(+27.30%)</b></td><td>184.70 <b>(+58.54%)</b></td><td>35.88 (-3.18%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>155.60 (n/a)</td><td>154.60 (n/a)</td><td>116.50 (n/a)</td><td>37.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (+10.22%)</td><td>0.04 (-4.70%)</td><td>0.04 (-0.83%)</td><td>0.03 <b>(-23.04%)</b></td><td>0.01 <b>(+77.45%)</b></td><td>293.90 <b>(+29.93%)</b></td><td>212.30 (+8.52%)</td><td>197.70 (+0.82%)</td><td>150.60 (-9.28%)</td><td>52.40 <b>(+112.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>195.64 (n/a)</td><td>196.10 (n/a)</td><td>166.00 (n/a)</td><td>24.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-12.95%)</td><td>0.04 (-17.34%)</td><td>0.04 (-15.52%)</td><td>0.03 <b>(-36.26%)</b></td><td>0.01 (+14.19%)</td><td>324.20 <b>(+56.85%)</b></td><td>215.34 <b>(+25.83%)</b></td><td>208.30 (+18.35%)</td><td>144.90 (+14.82%)</td><td>67.12 <b>(+113.35%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>171.14 (n/a)</td><td>176.00 (n/a)</td><td>126.20 (n/a)</td><td>31.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (-0.37%)</td><td>0.05 (+3.83%)</td><td>0.04 (+4.57%)</td><td>0.04 (+12.51%)</td><td>0.01 (-11.52%)</td><td>230.30 (-11.12%)</td><td>193.52 (-4.68%)</td><td>197.80 (-4.40%)</td><td>154.50 (+0.39%)</td><td>34.09 <b>(-20.22%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.10 (n/a)</td><td>203.02 (n/a)</td><td>206.90 (n/a)</td><td>153.90 (n/a)</td><td>42.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (-11.05%)</td><td>0.04 (-12.04%)</td><td>0.04 (+6.97%)</td><td>0.02 (-18.91%)</td><td>0.01 (+7.21%)</td><td>330.70 <b>(+23.30%)</b></td><td>248.44 (+16.61%)</td><td>208.00 (-6.52%)</td><td>186.70 (+12.40%)</td><td>71.42 <b>(+58.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.20 (n/a)</td><td>213.06 (n/a)</td><td>222.50 (n/a)</td><td>166.10 (n/a)</td><td>45.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.84 (-7.13%)</td><td>0.64 (-2.89%)</td><td>0.59 (+8.23%)</td><td>0.52 (+14.78%)</td><td>0.13 <b>(-35.45%)</b></td><td>189.70 (-12.86%)</td><td>158.74 (-1.51%)</td><td>166.10 (-7.62%)</td><td>116.50 (+7.67%)</td><td>30.15 <b>(-36.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.91 (n/a)</td><td>0.66 (n/a)</td><td>0.55 (n/a)</td><td>0.45 (n/a)</td><td>0.21 (n/a)</td><td>217.70 (n/a)</td><td>161.18 (n/a)</td><td>179.80 (n/a)</td><td>108.20 (n/a)</td><td>47.55 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.81 (-4.56%)</td><td>0.61 (-6.75%)</td><td>0.60 (-0.84%)</td><td>0.47 (+2.94%)</td><td>0.12 <b>(-32.02%)</b></td><td>209.20 (-2.88%)</td><td>166.82 (+3.81%)</td><td>165.10 (+0.86%)</td><td>121.70 (+4.73%)</td><td>31.55 <b>(-28.86%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.18 (n/a)</td><td>215.40 (n/a)</td><td>160.70 (n/a)</td><td>163.70 (n/a)</td><td>116.20 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.74 (+5.93%)</td><td>0.62 (+18.11%)</td><td>0.67 <b>(+32.97%)</b></td><td>0.44 (-1.86%)</td><td>0.11 (+15.40%)</td><td>225.70 (+1.90%)</td><td>163.06 (-14.60%)</td><td>146.80 <b>(-24.80%)</b></td><td>133.50 (-5.59%)</td><td>36.54 (+17.24%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.70 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.10 (n/a)</td><td>221.50 (n/a)</td><td>190.94 (n/a)</td><td>195.20 (n/a)</td><td>141.40 (n/a)</td><td>31.16 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.77 <b>(+22.47%)</b></td><td>0.57 (+15.32%)</td><td>0.56 <b>(+21.26%)</b></td><td>0.46 <b>(+44.98%)</b></td><td>0.13 (-5.89%)</td><td>214.80 <b>(-31.04%)</b></td><td>179.42 (-15.91%)</td><td>175.90 (-17.53%)</td><td>127.40 (-18.33%)</td><td>35.32 <b>(-44.55%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.13 (n/a)</td><td>311.50 (n/a)</td><td>213.36 (n/a)</td><td>213.30 (n/a)</td><td>156.00 (n/a)</td><td>63.70 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.71 <b>(+42.51%)</b></td><td>0.53 (+18.66%)</td><td>0.51 (+7.54%)</td><td>0.33 (-6.00%)</td><td>0.15 <b>(+142.60%)</b></td><td>222.40 (+6.36%)</td><td>148.98 (-11.21%)</td><td>145.70 (-7.02%)</td><td>103.80 <b>(-29.86%)</b></td><td>46.18 <b>(+81.97%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.50 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>209.10 (n/a)</td><td>167.78 (n/a)</td><td>156.70 (n/a)</td><td>148.00 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.56 (-12.18%)</td><td>0.46 (+10.87%)</td><td>0.45 <b>(+25.55%)</b></td><td>0.36 (+6.03%)</td><td>0.09 <b>(-26.81%)</b></td><td>206.40 (-5.71%)</td><td>165.46 (-11.81%)</td><td>162.20 <b>(-20.37%)</b></td><td>130.50 (+13.87%)</td><td>33.93 (-18.58%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.64 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>218.90 (n/a)</td><td>187.62 (n/a)</td><td>203.70 (n/a)</td><td>114.60 (n/a)</td><td>41.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.61 (+7.35%)</td><td>0.48 (+11.29%)</td><td>0.48 (+12.79%)</td><td>0.30 (+15.80%)</td><td>0.13 (+4.70%)</td><td>244.50 (-13.63%)</td><td>165.48 (-10.98%)</td><td>154.70 (-11.35%)</td><td>121.30 (-6.84%)</td><td>50.75 (-17.27%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>283.10 (n/a)</td><td>185.90 (n/a)</td><td>174.50 (n/a)</td><td>130.20 (n/a)</td><td>61.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.45 (+4.48%)</td><td>0.40 (+4.15%)</td><td>0.42 (+10.63%)</td><td>0.32 (-7.08%)</td><td>0.05 <b>(+58.25%)</b></td><td>228.10 (+7.59%)</td><td>189.02 (-3.08%)</td><td>174.30 (-9.60%)</td><td>164.00 (-4.26%)</td><td>27.32 <b>(+61.04%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.03 (n/a)</td><td>212.00 (n/a)</td><td>195.02 (n/a)</td><td>192.80 (n/a)</td><td>171.30 (n/a)</td><td>16.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.14 <b>(+24.54%)</b></td><td>0.85 (+3.47%)</td><td>0.75 (-18.26%)</td><td>0.71 <b>(+33.60%)</b></td><td>0.18 (+10.26%)</td><td>184.10 <b>(-25.13%)</b></td><td>159.90 (-4.47%)</td><td>175.50 <b>(+22.38%)</b></td><td>114.60 (-19.69%)</td><td>29.57 <b>(-33.70%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.92 (n/a)</td><td>0.82 (n/a)</td><td>0.91 (n/a)</td><td>0.53 (n/a)</td><td>0.17 (n/a)</td><td>245.90 (n/a)</td><td>167.38 (n/a)</td><td>143.40 (n/a)</td><td>142.70 (n/a)</td><td>44.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.16 <b>(+23.10%)</b></td><td>0.93 (+15.60%)</td><td>0.85 (+9.04%)</td><td>0.72 (+7.20%)</td><td>0.20 <b>(+97.77%)</b></td><td>182.00 (-6.71%)</td><td>146.44 (-11.50%)</td><td>154.40 (-8.31%)</td><td>113.20 (-18.74%)</td><td>30.00 <b>(+45.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.10 (n/a)</td><td>195.10 (n/a)</td><td>165.46 (n/a)</td><td>168.40 (n/a)</td><td>139.30 (n/a)</td><td>20.60 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.04 (+5.31%)</td><td>0.85 (+16.38%)</td><td>0.80 (+10.48%)</td><td>0.61 (+18.58%)</td><td>0.17 (-2.18%)</td><td>215.40 (-15.69%)</td><td>160.42 (-14.93%)</td><td>163.30 (-9.48%)</td><td>125.70 (-5.06%)</td><td>35.12 <b>(-21.86%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.99 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.51 (n/a)</td><td>0.17 (n/a)</td><td>255.50 (n/a)</td><td>188.58 (n/a)</td><td>180.40 (n/a)</td><td>132.40 (n/a)</td><td>44.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (+2.48%)</td><td>0.03 (+10.41%)</td><td>0.03 (+12.57%)</td><td>0.02 <b>(+61.29%)</b></td><td>0.00 <b>(-46.18%)</b></td><td>181.90 <b>(-38.00%)</b></td><td>150.56 (-16.64%)</td><td>142.20 (-11.18%)</td><td>121.40 (-2.41%)</td><td>23.92 <b>(-66.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>293.40 (n/a)</td><td>180.62 (n/a)</td><td>160.10 (n/a)</td><td>124.40 (n/a)</td><td>70.34 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 <b>(-27.03%)</b></td><td>0.02 (-13.66%)</td><td>0.02 (-2.69%)</td><td>0.02 (+8.01%)</td><td>0.00 <b>(-72.79%)</b></td><td>199.20 (-7.43%)</td><td>181.10 (+10.58%)</td><td>174.80 (+2.76%)</td><td>163.70 <b>(+36.99%)</b></td><td>14.65 <b>(-64.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>163.78 (n/a)</td><td>170.10 (n/a)</td><td>119.50 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.02 <b>(-25.53%)</b></td><td>0.02 (-18.28%)</td><td>0.02 (-14.86%)</td><td>0.02 <b>(-20.55%)</b></td><td>0.00 <b>(-42.51%)</b></td><td>224.70 <b>(+25.88%)</b></td><td>191.46 <b>(+21.52%)</b></td><td>188.20 (+17.40%)</td><td>169.70 <b>(+34.36%)</b></td><td>21.01 (-2.67%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.50 (n/a)</td><td>157.56 (n/a)</td><td>160.30 (n/a)</td><td>126.30 (n/a)</td><td>21.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.95 (-11.02%)</td><td>0.83 (+3.53%)</td><td>0.82 (+10.60%)</td><td>0.71 (+7.94%)</td><td>0.09 <b>(-45.40%)</b></td><td>186.40 (-7.36%)</td><td>161.56 (-5.43%)</td><td>161.20 (-9.59%)</td><td>139.70 (+12.39%)</td><td>17.89 <b>(-43.17%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.06 (n/a)</td><td>0.80 (n/a)</td><td>0.74 (n/a)</td><td>0.66 (n/a)</td><td>0.17 (n/a)</td><td>201.20 (n/a)</td><td>170.84 (n/a)</td><td>178.30 (n/a)</td><td>124.30 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.79 <b>(-25.87%)</b></td><td>0.69 (-18.69%)</td><td>0.73 (-10.49%)</td><td>0.50 (-16.59%)</td><td>0.12 <b>(-43.17%)</b></td><td>264.90 (+19.92%)</td><td>196.42 <b>(+20.46%)</b></td><td>180.90 (+11.74%)</td><td>167.30 <b>(+34.92%)</b></td><td>39.69 (-2.31%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.82 (n/a)</td><td>0.60 (n/a)</td><td>0.20 (n/a)</td><td>220.90 (n/a)</td><td>163.06 (n/a)</td><td>161.90 (n/a)</td><td>124.00 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.90 (-7.38%)</td><td>0.80 (+5.07%)</td><td>0.82 (+5.73%)</td><td>0.60 (+11.13%)</td><td>0.12 <b>(-24.44%)</b></td><td>220.10 (-10.02%)</td><td>168.26 (-6.42%)</td><td>160.50 (-5.37%)</td><td>146.40 (+7.96%)</td><td>30.18 <b>(-26.96%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.78 (n/a)</td><td>0.54 (n/a)</td><td>0.16 (n/a)</td><td>244.60 (n/a)</td><td>179.80 (n/a)</td><td>169.60 (n/a)</td><td>135.60 (n/a)</td><td>41.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.75 <b>(-33.68%)</b></td><td>0.67 <b>(-24.26%)</b></td><td>0.65 <b>(-25.63%)</b></td><td>0.61 (-12.18%)</td><td>0.06 <b>(-62.24%)</b></td><td>215.60 (+13.89%)</td><td>197.66 <b>(+29.70%)</b></td><td>203.70 <b>(+34.46%)</b></td><td>175.70 <b>(+50.69%)</b></td><td>16.94 <b>(-34.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.13 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>189.30 (n/a)</td><td>152.40 (n/a)</td><td>151.50 (n/a)</td><td>116.60 (n/a)</td><td>25.83 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.98 (-9.06%)</td><td>0.81 (-10.58%)</td><td>0.79 (-7.68%)</td><td>0.72 (-1.29%)</td><td>0.10 <b>(-36.51%)</b></td><td>182.20 (+1.28%)</td><td>165.02 (+10.41%)</td><td>167.10 (+8.37%)</td><td>134.90 (+10.03%)</td><td>18.09 <b>(-28.87%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>1.08 (n/a)</td><td>0.91 (n/a)</td><td>0.86 (n/a)</td><td>0.73 (n/a)</td><td>0.16 (n/a)</td><td>179.90 (n/a)</td><td>149.46 (n/a)</td><td>154.20 (n/a)</td><td>122.60 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.02 <b>(-27.71%)</b></td><td>0.02 <b>(-21.80%)</b></td><td>0.02 (-17.09%)</td><td>0.02 (-17.78%)</td><td>0.00 <b>(-47.48%)</b></td><td>230.90 <b>(+21.65%)</b></td><td>209.32 <b>(+26.14%)</b></td><td>214.00 <b>(+20.56%)</b></td><td>169.80 <b>(+38.39%)</b></td><td>24.10 (-12.38%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>165.94 (n/a)</td><td>177.50 (n/a)</td><td>122.70 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (-3.32%)</td><td>0.02 (-7.55%)</td><td>0.02 (-1.23%)</td><td>0.02 (-13.88%)</td><td>0.01 (+15.34%)</td><td>237.40 (+16.14%)</td><td>189.18 (+10.12%)</td><td>183.40 (+1.27%)</td><td>130.10 (+3.42%)</td><td>43.33 <b>(+43.09%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>171.80 (n/a)</td><td>181.10 (n/a)</td><td>125.80 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.00 (-2.27%)</td><td>0.00 (-1.42%)</td><td>0.00 (-2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.76%)</b></td><td>1054.89 (+0.66%)</td><td>980.07 (+1.34%)</td><td>968.55 (+1.80%)</td><td>943.90 (+1.90%)</td><td>44.92 (-6.43%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1047.98 (n/a)</td><td>967.10 (n/a)</td><td>951.42 (n/a)</td><td>926.31 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.01 (+1.20%)</td><td>0.01 (-0.25%)</td><td>0.01 (+1.25%)</td><td>0.01 (-6.41%)</td><td>0.00 <b>(+95.71%)</b></td><td>1124.10 (+6.50%)</td><td>1019.17 (+0.23%)</td><td>1006.35 (-1.69%)</td><td>973.55 (-0.80%)</td><td>61.82 <b>(+84.68%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1055.47 (n/a)</td><td>1016.80 (n/a)</td><td>1023.60 (n/a)</td><td>981.36 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.01 (+3.80%)</td><td>0.97 (+1.30%)</td><td>0.96 (+1.07%)</td><td>0.95 (+0.58%)</td><td>0.02 <b>(+137.57%)</b></td><td>2198.28 (-0.57%)</td><td>2164.87 (-1.25%)</td><td>2178.03 (-1.05%)</td><td>2082.22 (-3.66%)</td><td>47.69 <b>(+127.71%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2210.94 (n/a)</td><td>2192.37 (n/a)</td><td>2201.23 (n/a)</td><td>2161.43 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.13 (-6.63%)</td><td>2.60 (-5.56%)</td><td>2.37 (-8.21%)</td><td>2.33 (-6.78%)</td><td>0.35 (+1.02%)</td><td>225.20 (+7.29%)</td><td>204.62 (+6.13%)</td><td>221.40 (+8.96%)</td><td>167.70 (+7.09%)</td><td>25.79 (+19.00%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.35 (n/a)</td><td>2.75 (n/a)</td><td>2.58 (n/a)</td><td>2.50 (n/a)</td><td>0.35 (n/a)</td><td>209.90 (n/a)</td><td>192.80 (n/a)</td><td>203.20 (n/a)</td><td>156.60 (n/a)</td><td>21.67 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>5.80 (+4.01%)</td><td>4.95 <b>(+21.21%)</b></td><td>4.57 (+0.95%)</td><td>4.40 <b>(+97.69%)</b></td><td>0.67 <b>(-47.65%)</b></td><td>238.10 <b>(-49.42%)</b></td><td>214.60 <b>(-24.30%)</b></td><td>229.40 (-0.91%)</td><td>180.80 (-3.88%)</td><td>27.49 <b>(-75.45%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>5.57 (n/a)</td><td>4.09 (n/a)</td><td>4.53 (n/a)</td><td>2.23 (n/a)</td><td>1.27 (n/a)</td><td>470.70 (n/a)</td><td>283.48 (n/a)</td><td>231.50 (n/a)</td><td>188.10 (n/a)</td><td>112.01 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.41 (+3.46%)</td><td>2.68 (-9.22%)</td><td>2.47 (-16.89%)</td><td>2.04 <b>(-21.77%)</b></td><td>0.55 <b>(+99.91%)</b></td><td>257.30 <b>(+27.82%)</b></td><td>202.34 (+13.11%)</td><td>212.30 <b>(+20.28%)</b></td><td>153.90 (-3.33%)</td><td>41.00 <b>(+142.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>3.29 (n/a)</td><td>2.95 (n/a)</td><td>2.97 (n/a)</td><td>2.60 (n/a)</td><td>0.28 (n/a)</td><td>201.30 (n/a)</td><td>178.88 (n/a)</td><td>176.50 (n/a)</td><td>159.20 (n/a)</td><td>16.90 (n/a)</td>
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
