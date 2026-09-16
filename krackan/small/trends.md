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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (+8.88%)</td><td>0.08 (+10.14%)</td><td>0.08 (+6.50%)</td><td>0.07 <b>(+20.95%)</b></td><td>0.01 <b>(-21.66%)</b></td><td>167.00 (-17.33%)</td><td>152.48 (-9.69%)</td><td>152.90 (-6.14%)</td><td>138.20 (-8.11%)</td><td>11.53 <b>(-41.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.00 (n/a)</td><td>168.84 (n/a)</td><td>162.90 (n/a)</td><td>150.40 (n/a)</td><td>19.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.11 <b>(+30.08%)</b></td><td>0.09 <b>(+23.44%)</b></td><td>0.08 <b>(+20.52%)</b></td><td>0.06 (+6.65%)</td><td>0.02 <b>(+80.17%)</b></td><td>190.70 (-6.20%)</td><td>148.66 (-17.13%)</td><td>149.00 (-17.04%)</td><td>107.30 <b>(-23.14%)</b></td><td>32.36 <b>(+32.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>179.38 (n/a)</td><td>179.60 (n/a)</td><td>139.60 (n/a)</td><td>24.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (+15.28%)</td><td>0.08 <b>(+21.45%)</b></td><td>0.08 (+17.19%)</td><td>0.07 <b>(+66.26%)</b></td><td>0.01 <b>(-36.61%)</b></td><td>188.70 <b>(-39.87%)</b></td><td>164.26 <b>(-21.10%)</b></td><td>159.60 (-14.70%)</td><td>142.70 (-13.25%)</td><td>19.77 <b>(-67.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>313.80 (n/a)</td><td>208.20 (n/a)</td><td>187.10 (n/a)</td><td>164.50 (n/a)</td><td>61.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (+10.33%)</td><td>0.07 (+5.37%)</td><td>0.07 <b>(+23.51%)</b></td><td>0.05 (-15.90%)</td><td>0.02 <b>(+80.00%)</b></td><td>268.60 (+18.90%)</td><td>196.28 (-0.87%)</td><td>166.10 (-19.05%)</td><td>144.50 (-9.35%)</td><td>56.05 <b>(+95.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>198.00 (n/a)</td><td>205.20 (n/a)</td><td>159.40 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+10.43%)</td><td>0.03 (-8.24%)</td><td>0.03 <b>(-24.16%)</b></td><td>0.03 (+8.15%)</td><td>0.01 (-2.57%)</td><td>191.20 (-7.54%)</td><td>162.72 (+7.53%)</td><td>164.50 <b>(+31.92%)</b></td><td>105.10 (-9.47%)</td><td>34.74 (-19.69%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>151.32 (n/a)</td><td>124.70 (n/a)</td><td>116.10 (n/a)</td><td>43.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (-13.86%)</td><td>0.03 (-8.83%)</td><td>0.03 (+1.83%)</td><td>0.03 (-7.79%)</td><td>0.01 (-16.84%)</td><td>199.80 (+8.47%)</td><td>167.42 (+9.38%)</td><td>161.30 (-1.77%)</td><td>140.00 (+16.09%)</td><td>27.74 (+6.44%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>153.06 (n/a)</td><td>164.20 (n/a)</td><td>120.60 (n/a)</td><td>26.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (-14.54%)</td><td>0.03 (-5.30%)</td><td>0.03 (+0.49%)</td><td>0.03 (+5.00%)</td><td>0.01 <b>(-36.46%)</b></td><td>205.10 (-4.78%)</td><td>169.12 (+2.95%)</td><td>170.60 (-0.52%)</td><td>136.80 (+17.02%)</td><td>27.85 <b>(-28.75%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>164.28 (n/a)</td><td>171.50 (n/a)</td><td>116.90 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 <b>(+33.72%)</b></td><td>0.03 (+6.98%)</td><td>0.03 (-5.60%)</td><td>0.02 (+8.56%)</td><td>0.01 <b>(+72.36%)</b></td><td>231.50 (-7.88%)</td><td>181.32 (-2.56%)</td><td>196.70 (+5.92%)</td><td>101.60 <b>(-25.24%)</b></td><td>51.09 (+15.18%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>251.30 (n/a)</td><td>186.08 (n/a)</td><td>185.70 (n/a)</td><td>135.90 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 <b>(+45.30%)</b></td><td>0.03 <b>(+24.21%)</b></td><td>0.03 (+1.95%)</td><td>0.03 <b>(+69.06%)</b></td><td>0.01 <b>(+23.44%)</b></td><td>182.80 <b>(-40.84%)</b></td><td>156.28 <b>(-21.52%)</b></td><td>167.10 (-1.94%)</td><td>107.10 <b>(-31.17%)</b></td><td>29.13 <b>(-53.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>309.00 (n/a)</td><td>199.14 (n/a)</td><td>170.40 (n/a)</td><td>155.60 (n/a)</td><td>62.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (+9.22%)</td><td>0.03 (+1.70%)</td><td>0.03 (+11.14%)</td><td>0.02 (-5.67%)</td><td>0.00 <b>(+36.58%)</b></td><td>224.60 (+6.04%)</td><td>193.26 (-0.81%)</td><td>188.40 (-10.03%)</td><td>154.40 (-8.48%)</td><td>29.38 <b>(+34.54%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.80 (n/a)</td><td>194.84 (n/a)</td><td>209.40 (n/a)</td><td>168.70 (n/a)</td><td>21.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (-12.79%)</td><td>0.03 (-10.45%)</td><td>0.03 (+3.11%)</td><td>0.02 <b>(-29.82%)</b></td><td>0.01 <b>(+28.35%)</b></td><td>309.50 <b>(+42.50%)</b></td><td>216.00 (+15.04%)</td><td>192.10 (-2.98%)</td><td>172.30 (+14.71%)</td><td>57.32 <b>(+109.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>187.76 (n/a)</td><td>198.00 (n/a)</td><td>150.20 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (-4.52%)</td><td>0.02 (-3.29%)</td><td>0.02 (-7.32%)</td><td>0.02 (+19.27%)</td><td>0.00 <b>(-32.04%)</b></td><td>261.00 (-16.16%)</td><td>223.80 (+0.77%)</td><td>232.90 (+7.92%)</td><td>176.80 (+4.74%)</td><td>31.51 <b>(-42.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>222.08 (n/a)</td><td>215.80 (n/a)</td><td>168.80 (n/a)</td><td>54.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>153.28 (n/a)</td><td>145.10 (n/a)</td><td>140.80 (n/a)</td><td>15.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.10 (n/a)</td><td>164.96 (n/a)</td><td>176.40 (n/a)</td><td>118.80 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>171.54 (n/a)</td><td>178.30 (n/a)</td><td>108.60 (n/a)</td><td>43.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>300.70 (n/a)</td><td>194.04 (n/a)</td><td>180.00 (n/a)</td><td>145.80 (n/a)</td><td>61.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>231.10 (n/a)</td><td>174.22 (n/a)</td><td>172.10 (n/a)</td><td>124.30 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>203.28 (n/a)</td><td>214.50 (n/a)</td><td>175.60 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>261.60 (n/a)</td><td>207.90 (n/a)</td><td>212.70 (n/a)</td><td>132.90 (n/a)</td><td>49.14 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>259.50 (n/a)</td><td>218.06 (n/a)</td><td>206.50 (n/a)</td><td>197.20 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.20 <b>(-38.16%)</b></td><td>3.04 (-15.90%)</td><td>3.06 (-5.56%)</td><td>2.90 (-4.39%)</td><td>0.13 <b>(-85.59%)</b></td><td>474.50 (+4.61%)</td><td>452.80 (+14.64%)</td><td>449.40 (+5.89%)</td><td>429.80 <b>(+61.70%)</b></td><td>19.05 <b>(-74.76%)</b></td><td>624.52 <b>(-38.16%)</b></td><td>593.67 (-15.90%)</td><td>597.30 (-5.56%)</td><td>565.74 (-4.39%)</td><td>24.95 <b>(-85.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.18 (n/a)</td><td>3.62 (n/a)</td><td>3.24 (n/a)</td><td>3.03 (n/a)</td><td>0.89 (n/a)</td><td>453.60 (n/a)</td><td>394.96 (n/a)</td><td>424.40 (n/a)</td><td>265.80 (n/a)</td><td>75.47 (n/a)</td><td>1009.86 (n/a)</td><td>705.95 (n/a)</td><td>632.44 (n/a)</td><td>591.75 (n/a)</td><td>173.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.03 <b>(-34.97%)</b></td><td>3.65 <b>(-24.41%)</b></td><td>3.64 (-19.15%)</td><td>3.32 (-8.32%)</td><td>0.25 <b>(-76.27%)</b></td><td>414.00 (+9.06%)</td><td>378.86 <b>(+27.72%)</b></td><td>378.40 <b>(+23.66%)</b></td><td>341.50 <b>(+53.76%)</b></td><td>25.97 <b>(-59.71%)</b></td><td>786.00 <b>(-34.97%)</b></td><td>711.21 <b>(-24.41%)</b></td><td>709.40 (-19.15%)</td><td>648.40 (-8.32%)</td><td>49.52 <b>(-76.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.20 (n/a)</td><td>4.82 (n/a)</td><td>4.50 (n/a)</td><td>3.63 (n/a)</td><td>1.07 (n/a)</td><td>379.60 (n/a)</td><td>296.64 (n/a)</td><td>306.00 (n/a)</td><td>222.10 (n/a)</td><td>64.46 (n/a)</td><td>1208.61 (n/a)</td><td>940.89 (n/a)</td><td>877.38 (n/a)</td><td>707.21 (n/a)</td><td>208.65 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.25 (+12.28%)</td><td>4.71 (+10.22%)</td><td>4.03 (+0.58%)</td><td>3.48 (+0.63%)</td><td>1.33 <b>(+65.73%)</b></td><td>395.60 (-0.63%)</td><td>310.68 (-6.01%)</td><td>341.40 (-0.58%)</td><td>220.20 (-10.96%)</td><td>81.63 <b>(+45.09%)</b></td><td>1218.84 (+12.28%)</td><td>918.43 (+10.22%)</td><td>786.30 (+0.58%)</td><td>678.50 (+0.63%)</td><td>259.98 <b>(+65.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.57 (n/a)</td><td>4.27 (n/a)</td><td>4.01 (n/a)</td><td>3.46 (n/a)</td><td>0.80 (n/a)</td><td>398.10 (n/a)</td><td>330.54 (n/a)</td><td>343.40 (n/a)</td><td>247.30 (n/a)</td><td>56.26 (n/a)</td><td>1085.51 (n/a)</td><td>833.25 (n/a)</td><td>781.76 (n/a)</td><td>674.28 (n/a)</td><td>156.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.93 <b>(-45.89%)</b></td><td>3.91 <b>(-26.59%)</b></td><td>3.70 <b>(-21.20%)</b></td><td>3.37 (-11.11%)</td><td>0.62 <b>(-70.99%)</b></td><td>408.80 (+12.49%)</td><td>358.74 <b>(+26.35%)</b></td><td>372.00 <b>(+26.88%)</b></td><td>279.00 <b>(+84.77%)</b></td><td>51.19 <b>(-35.92%)</b></td><td>962.03 <b>(-45.89%)</b></td><td>762.12 <b>(-26.59%)</b></td><td>721.59 <b>(-21.20%)</b></td><td>656.66 (-11.11%)</td><td>121.89 <b>(-70.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>9.11 (n/a)</td><td>5.32 (n/a)</td><td>4.69 (n/a)</td><td>3.79 (n/a)</td><td>2.15 (n/a)</td><td>363.40 (n/a)</td><td>283.92 (n/a)</td><td>293.20 (n/a)</td><td>151.00 (n/a)</td><td>79.88 (n/a)</td><td>1777.75 (n/a)</td><td>1038.17 (n/a)</td><td>915.67 (n/a)</td><td>738.70 (n/a)</td><td>420.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.17 <b>(-30.21%)</b></td><td>3.20 (-16.79%)</td><td>2.95 (-14.48%)</td><td>2.88 (+0.79%)</td><td>0.55 <b>(-54.96%)</b></td><td>478.10 (-0.79%)</td><td>438.04 (+15.15%)</td><td>467.30 (+16.91%)</td><td>329.90 <b>(+43.25%)</b></td><td>62.46 <b>(-32.37%)</b></td><td>813.67 <b>(-30.21%)</b></td><td>625.01 (-16.79%)</td><td>574.43 (-14.48%)</td><td>561.45 (+0.79%)</td><td>107.37 <b>(-54.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.98 (n/a)</td><td>3.85 (n/a)</td><td>3.44 (n/a)</td><td>2.86 (n/a)</td><td>1.22 (n/a)</td><td>481.90 (n/a)</td><td>380.42 (n/a)</td><td>399.70 (n/a)</td><td>230.30 (n/a)</td><td>92.35 (n/a)</td><td>1165.80 (n/a)</td><td>751.10 (n/a)</td><td>671.66 (n/a)</td><td>557.07 (n/a)</td><td>238.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.08 <b>(-51.66%)</b></td><td>1.03 <b>(-47.41%)</b></td><td>1.01 <b>(-49.47%)</b></td><td>0.99 <b>(-36.58%)</b></td><td>0.04 <b>(-85.96%)</b></td><td>407.10 <b>(+57.67%)</b></td><td>390.86 <b>(+87.35%)</b></td><td>396.10 <b>(+97.95%)</b></td><td>373.10 <b>(+106.82%)</b></td><td>13.86 <b>(-54.85%)</b></td><td>89.93 <b>(-51.66%)</b></td><td>85.94 <b>(-47.41%)</b></td><td>84.72 <b>(-49.47%)</b></td><td>82.41 <b>(-36.58%)</b></td><td>3.07 <b>(-85.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>2.23 (n/a)</td><td>1.95 (n/a)</td><td>2.01 (n/a)</td><td>1.55 (n/a)</td><td>0.26 (n/a)</td><td>258.20 (n/a)</td><td>208.62 (n/a)</td><td>200.10 (n/a)</td><td>180.40 (n/a)</td><td>30.69 (n/a)</td><td>186.02 (n/a)</td><td>163.41 (n/a)</td><td>167.68 (n/a)</td><td>129.95 (n/a)</td><td>21.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.20 (-18.20%)</td><td>5.13 (-18.85%)</td><td>4.73 (-19.88%)</td><td>4.60 (-8.85%)</td><td>0.69 <b>(-38.77%)</b></td><td>419.90 (+9.69%)</td><td>382.22 <b>(+21.77%)</b></td><td>408.60 <b>(+24.84%)</b></td><td>311.80 <b>(+22.23%)</b></td><td>47.12 (-14.40%)</td><td>1291.20 (-18.20%)</td><td>1067.55 (-18.85%)</td><td>985.55 (-19.88%)</td><td>958.81 (-8.85%)</td><td>143.53 <b>(-38.77%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>7.58 (n/a)</td><td>6.32 (n/a)</td><td>5.91 (n/a)</td><td>5.05 (n/a)</td><td>1.13 (n/a)</td><td>382.80 (n/a)</td><td>313.88 (n/a)</td><td>327.30 (n/a)</td><td>255.10 (n/a)</td><td>55.05 (n/a)</td><td>1578.57 (n/a)</td><td>1315.55 (n/a)</td><td>1230.07 (n/a)</td><td>1051.93 (n/a)</td><td>234.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>17.47 <b>(+23.68%)</b></td><td>12.54 (-3.61%)</td><td>11.37 (-9.63%)</td><td>10.85 (-13.08%)</td><td>2.79 <b>(+289.41%)</b></td><td>507.50 (+15.05%)</td><td>452.94 (+6.81%)</td><td>484.30 (+10.65%)</td><td>315.20 (-19.14%)</td><td>79.16 <b>(+252.12%)</b></td><td>6813.10 <b>(+23.68%)</b></td><td>4892.63 (-3.61%)</td><td>4434.28 (-9.63%)</td><td>4231.45 (-13.08%)</td><td>1086.94 <b>(+289.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>14.12 (n/a)</td><td>13.01 (n/a)</td><td>12.58 (n/a)</td><td>12.48 (n/a)</td><td>0.72 (n/a)</td><td>441.10 (n/a)</td><td>424.08 (n/a)</td><td>437.70 (n/a)</td><td>389.80 (n/a)</td><td>22.48 (n/a)</td><td>5508.76 (n/a)</td><td>5075.69 (n/a)</td><td>4906.83 (n/a)</td><td>4868.16 (n/a)</td><td>279.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>157.06 (n/a)</td><td>148.60 (n/a)</td><td>131.70 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>174.50 (n/a)</td><td>161.20 (n/a)</td><td>150.10 (n/a)</td><td>24.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>189.46 (n/a)</td><td>207.20 (n/a)</td><td>127.00 (n/a)</td><td>42.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>173.18 (n/a)</td><td>167.30 (n/a)</td><td>143.20 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.30 (n/a)</td><td>206.02 (n/a)</td><td>202.10 (n/a)</td><td>143.20 (n/a)</td><td>60.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.70 (n/a)</td><td>224.22 (n/a)</td><td>213.60 (n/a)</td><td>153.10 (n/a)</td><td>57.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>200.22 (n/a)</td><td>210.40 (n/a)</td><td>152.10 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.60 (n/a)</td><td>260.30 (n/a)</td><td>234.80 (n/a)</td><td>214.10 (n/a)</td><td>53.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.87 (+16.65%)</td><td>4.34 (+7.89%)</td><td>4.17 (+2.88%)</td><td>4.07 (+11.81%)</td><td>0.33 <b>(+49.73%)</b></td><td>2310.90 (-10.56%)</td><td>2177.64 (-7.14%)</td><td>2253.10 (-2.80%)</td><td>1929.90 (-14.28%)</td><td>157.03 (+14.03%)</td><td>1916.84 (+16.65%)</td><td>1706.30 (+7.89%)</td><td>1641.88 (+2.88%)</td><td>1600.81 (+11.81%)</td><td>130.48 <b>(+49.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>4.18 (n/a)</td><td>4.02 (n/a)</td><td>4.06 (n/a)</td><td>3.64 (n/a)</td><td>0.22 (n/a)</td><td>2583.80 (n/a)</td><td>2345.10 (n/a)</td><td>2318.00 (n/a)</td><td>2251.30 (n/a)</td><td>137.71 (n/a)</td><td>1643.23 (n/a)</td><td>1581.59 (n/a)</td><td>1595.94 (n/a)</td><td>1431.78 (n/a)</td><td>87.15 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.30 (+10.73%)</td><td>0.87 (+7.39%)</td><td>0.81 (+19.46%)</td><td>0.60 (-2.81%)</td><td>0.29 <b>(+24.28%)</b></td><td>369.70 (+2.89%)</td><td>276.72 (-4.48%)</td><td>274.00 (-16.28%)</td><td>170.70 (-9.68%)</td><td>85.06 (+18.25%)</td><td>55.29 (+10.73%)</td><td>37.09 (+7.39%)</td><td>34.45 (+19.46%)</td><td>25.53 (-2.81%)</td><td>12.40 <b>(+24.28%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.17 (n/a)</td><td>0.81 (n/a)</td><td>0.68 (n/a)</td><td>0.62 (n/a)</td><td>0.23 (n/a)</td><td>359.30 (n/a)</td><td>289.70 (n/a)</td><td>327.30 (n/a)</td><td>189.00 (n/a)</td><td>71.93 (n/a)</td><td>49.93 (n/a)</td><td>34.54 (n/a)</td><td>28.84 (n/a)</td><td>26.27 (n/a)</td><td>9.98 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.96 <b>(-29.13%)</b></td><td>0.82 (-12.08%)</td><td>0.84 (-11.79%)</td><td>0.67 (-0.71%)</td><td>0.13 <b>(-51.02%)</b></td><td>329.20 (+0.73%)</td><td>277.40 (+9.02%)</td><td>263.90 (+13.36%)</td><td>231.00 <b>(+41.11%)</b></td><td>47.02 <b>(-32.09%)</b></td><td>40.85 <b>(-29.13%)</b></td><td>34.80 (-12.08%)</td><td>35.76 (-11.79%)</td><td>28.67 (-0.71%)</td><td>5.74 <b>(-51.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.35 (n/a)</td><td>0.93 (n/a)</td><td>0.95 (n/a)</td><td>0.68 (n/a)</td><td>0.27 (n/a)</td><td>326.80 (n/a)</td><td>254.46 (n/a)</td><td>232.80 (n/a)</td><td>163.70 (n/a)</td><td>69.25 (n/a)</td><td>57.63 (n/a)</td><td>39.58 (n/a)</td><td>40.54 (n/a)</td><td>28.87 (n/a)</td><td>11.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.53 (-0.80%)</td><td>0.53 (-0.33%)</td><td>0.53 (-0.24%)</td><td>0.53 (-0.20%)</td><td>0.00 <b>(-70.96%)</b></td><td>47909.30 (+0.20%)</td><td>47871.32 (+0.33%)</td><td>47895.00 (+0.24%)</td><td>47789.10 (+0.81%)</td><td>50.34 <b>(-70.66%)</b></td><td>359.49 (-0.80%)</td><td>358.88 (-0.33%)</td><td>358.70 (-0.24%)</td><td>358.59 (-0.20%)</td><td>0.38 <b>(-70.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47814.60 (n/a)</td><td>47712.18 (n/a)</td><td>47781.20 (n/a)</td><td>47406.90 (n/a)</td><td>171.56 (n/a)</td><td>362.39 (n/a)</td><td>360.08 (n/a)</td><td>359.55 (n/a)</td><td>359.30 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.92 (+1.01%)</td><td>0.91 (+0.50%)</td><td>0.90 (+0.23%)</td><td>0.90 (+0.32%)</td><td>0.01 <b>(+44.70%)</b></td><td>27997.70 (-0.32%)</td><td>27769.46 (-0.49%)</td><td>27855.30 (-0.23%)</td><td>27377.40 (-1.00%)</td><td>235.68 <b>(+42.58%)</b></td><td>627.52 (+1.01%)</td><td>618.70 (+0.50%)</td><td>616.75 (+0.23%)</td><td>613.62 (+0.32%)</td><td>5.29 <b>(+44.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>28086.20 (n/a)</td><td>27907.46 (n/a)</td><td>27919.10 (n/a)</td><td>27653.80 (n/a)</td><td>165.30 (n/a)</td><td>621.25 (n/a)</td><td>615.62 (n/a)</td><td>615.34 (n/a)</td><td>611.68 (n/a)</td><td>3.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.27 (-2.88%)</td><td>3.17 (-0.86%)</td><td>3.15 (-0.36%)</td><td>3.13 (-0.10%)</td><td>0.06 <b>(-40.38%)</b></td><td>8047.70 (+0.10%)</td><td>7951.02 (+0.82%)</td><td>7987.70 (+0.36%)</td><td>7701.80 (+2.96%)</td><td>142.57 <b>(-38.46%)</b></td><td>2230.62 (-2.88%)</td><td>2161.29 (-0.86%)</td><td>2150.80 (-0.36%)</td><td>2134.76 (-0.10%)</td><td>39.60 <b>(-40.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.36 (n/a)</td><td>3.19 (n/a)</td><td>3.16 (n/a)</td><td>3.13 (n/a)</td><td>0.10 (n/a)</td><td>8039.70 (n/a)</td><td>7886.54 (n/a)</td><td>7958.80 (n/a)</td><td>7480.40 (n/a)</td><td>231.69 (n/a)</td><td>2296.66 (n/a)</td><td>2179.95 (n/a)</td><td>2158.61 (n/a)</td><td>2136.88 (n/a)</td><td>66.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.36 <b>(+20.86%)</b></td><td>3.96 (+17.76%)</td><td>3.93 (+11.53%)</td><td>3.56 (+16.56%)</td><td>0.37 <b>(+31.19%)</b></td><td>2265.30 (-14.21%)</td><td>2051.86 (-14.98%)</td><td>2052.50 (-10.34%)</td><td>1848.80 (-17.26%)</td><td>190.14 (-8.12%)</td><td>1143.43 <b>(+20.86%)</b></td><td>1037.38 (+17.76%)</td><td>1029.92 (+11.53%)</td><td>933.16 (+16.56%)</td><td>96.32 <b>(+31.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.61 (n/a)</td><td>3.36 (n/a)</td><td>3.52 (n/a)</td><td>3.05 (n/a)</td><td>0.28 (n/a)</td><td>2640.40 (n/a)</td><td>2413.40 (n/a)</td><td>2289.10 (n/a)</td><td>2234.50 (n/a)</td><td>206.94 (n/a)</td><td>946.05 (n/a)</td><td>880.94 (n/a)</td><td>923.46 (n/a)</td><td>800.60 (n/a)</td><td>73.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.59 <b>(+26.40%)</b></td><td>0.41 (+9.89%)</td><td>0.36 (+4.73%)</td><td>0.30 (-5.52%)</td><td>0.12 <b>(+99.87%)</b></td><td>4111.00 (+5.84%)</td><td>3254.26 (-4.96%)</td><td>3453.90 (-4.51%)</td><td>2127.70 <b>(-20.89%)</b></td><td>850.55 <b>(+68.56%)</b></td><td>31.54 <b>(+26.40%)</b></td><td>21.95 (+9.89%)</td><td>19.43 (+4.73%)</td><td>16.32 (-5.52%)</td><td>6.45 <b>(+99.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>3884.00 (n/a)</td><td>3424.20 (n/a)</td><td>3617.20 (n/a)</td><td>2689.50 (n/a)</td><td>504.60 (n/a)</td><td>24.95 (n/a)</td><td>19.98 (n/a)</td><td>18.55 (n/a)</td><td>17.28 (n/a)</td><td>3.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.47 <b>(+34.47%)</b></td><td>4.79 (+4.69%)</td><td>4.72 (-1.37%)</td><td>3.30 (-10.43%)</td><td>1.13 <b>(+127.06%)</b></td><td>2014.80 (+11.64%)</td><td>1454.10 (-1.15%)</td><td>1410.70 (+1.39%)</td><td>1027.50 <b>(-25.64%)</b></td><td>354.51 <b>(+89.98%)</b></td><td>2000.14 <b>(+34.47%)</b></td><td>1479.01 (+4.69%)</td><td>1456.83 (-1.37%)</td><td>1020.08 (-10.43%)</td><td>347.80 <b>(+127.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>4.81 (n/a)</td><td>4.57 (n/a)</td><td>4.78 (n/a)</td><td>3.69 (n/a)</td><td>0.50 (n/a)</td><td>1804.70 (n/a)</td><td>1470.98 (n/a)</td><td>1391.40 (n/a)</td><td>1381.70 (n/a)</td><td>186.60 (n/a)</td><td>1487.46 (n/a)</td><td>1412.72 (n/a)</td><td>1477.08 (n/a)</td><td>1138.84 (n/a)</td><td>153.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>13.61 (n/a)</td><td>12.40 (n/a)</td><td>12.30 (n/a)</td><td>10.80 (n/a)</td><td>1.10 (n/a)</td><td>13.61 (n/a)</td><td>12.39 (n/a)</td><td>12.30 (n/a)</td><td>10.79 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>25.07 (+1.09%)</td><td>24.55 (+3.88%)</td><td>24.82 (+2.46%)</td><td>23.43 (+12.93%)</td><td>0.66 <b>(-60.38%)</b></td><td>25.06 (+1.09%)</td><td>24.54 (+3.88%)</td><td>24.80 (+2.46%)</td><td>23.42 (+12.93%)</td><td>0.66 <b>(-60.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>24.80 (n/a)</td><td>23.63 (n/a)</td><td>24.22 (n/a)</td><td>20.75 (n/a)</td><td>1.66 (n/a)</td><td>24.79 (n/a)</td><td>23.62 (n/a)</td><td>24.21 (n/a)</td><td>20.74 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>40.19 (-2.90%)</td><td>39.03 (-2.86%)</td><td>39.26 (-4.44%)</td><td>37.90 (-0.17%)</td><td>0.88 <b>(-43.83%)</b></td><td>40.16 (-2.90%)</td><td>39.01 (-2.86%)</td><td>39.24 (-4.44%)</td><td>37.87 (-0.17%)</td><td>0.88 <b>(-43.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>41.39 (n/a)</td><td>40.18 (n/a)</td><td>41.08 (n/a)</td><td>37.96 (n/a)</td><td>1.57 (n/a)</td><td>41.37 (n/a)</td><td>40.15 (n/a)</td><td>41.06 (n/a)</td><td>37.94 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>46.43 (+4.40%)</td><td>43.74 (+17.37%)</td><td>43.67 (+4.61%)</td><td>40.89 <b>(+79.16%)</b></td><td>2.10 <b>(-76.92%)</b></td><td>46.40 (+4.40%)</td><td>43.72 (+17.37%)</td><td>43.64 (+4.61%)</td><td>40.86 <b>(+79.16%)</b></td><td>2.10 <b>(-76.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>44.47 (n/a)</td><td>37.27 (n/a)</td><td>41.74 (n/a)</td><td>22.82 (n/a)</td><td>9.11 (n/a)</td><td>44.44 (n/a)</td><td>37.25 (n/a)</td><td>41.72 (n/a)</td><td>22.81 (n/a)</td><td>9.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>13.52 (n/a)</td><td>12.79 (n/a)</td><td>13.23 (n/a)</td><td>11.56 (n/a)</td><td>0.83 (n/a)</td><td>13.51 (n/a)</td><td>12.78 (n/a)</td><td>13.23 (n/a)</td><td>11.55 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>25.53 (+1.11%)</td><td>22.88 (-6.01%)</td><td>23.64 (-2.25%)</td><td>19.44 (-18.29%)</td><td>2.30 <b>(+322.35%)</b></td><td>25.51 (+1.11%)</td><td>22.87 (-6.01%)</td><td>23.63 (-2.25%)</td><td>19.43 (-18.29%)</td><td>2.30 <b>(+322.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>25.25 (n/a)</td><td>24.35 (n/a)</td><td>24.19 (n/a)</td><td>23.79 (n/a)</td><td>0.54 (n/a)</td><td>25.23 (n/a)</td><td>24.33 (n/a)</td><td>24.17 (n/a)</td><td>23.78 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>40.58 (+0.30%)</td><td>39.16 (+0.98%)</td><td>39.44 (+1.22%)</td><td>36.42 (-1.69%)</td><td>1.65 <b>(+29.62%)</b></td><td>40.56 (+0.30%)</td><td>39.13 (+0.98%)</td><td>39.42 (+1.22%)</td><td>36.40 (-1.69%)</td><td>1.65 <b>(+29.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>40.46 (n/a)</td><td>38.78 (n/a)</td><td>38.97 (n/a)</td><td>37.05 (n/a)</td><td>1.27 (n/a)</td><td>40.44 (n/a)</td><td>38.75 (n/a)</td><td>38.94 (n/a)</td><td>37.03 (n/a)</td><td>1.27 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>46.64 (+7.22%)</td><td>42.67 (+1.43%)</td><td>42.07 (-0.80%)</td><td>38.99 (-0.23%)</td><td>2.95 <b>(+66.38%)</b></td><td>46.61 (+7.22%)</td><td>42.65 (+1.43%)</td><td>42.05 (-0.80%)</td><td>38.97 (-0.23%)</td><td>2.95 <b>(+66.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>43.49 (n/a)</td><td>42.07 (n/a)</td><td>42.41 (n/a)</td><td>39.08 (n/a)</td><td>1.77 (n/a)</td><td>43.47 (n/a)</td><td>42.05 (n/a)</td><td>42.39 (n/a)</td><td>39.06 (n/a)</td><td>1.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>9.26 (-0.79%)</td><td>8.62 (-1.80%)</td><td>8.62 (-1.86%)</td><td>8.21 (-0.56%)</td><td>0.40 (+3.61%)</td><td>9.25 (-0.79%)</td><td>8.61 (-1.80%)</td><td>8.60 (-1.86%)</td><td>8.20 (-0.56%)</td><td>0.40 (+3.61%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>9.34 (n/a)</td><td>8.78 (n/a)</td><td>8.78 (n/a)</td><td>8.26 (n/a)</td><td>0.38 (n/a)</td><td>9.32 (n/a)</td><td>8.77 (n/a)</td><td>8.76 (n/a)</td><td>8.24 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.05 (+4.29%)</td><td>0.86 (-1.36%)</td><td>0.79 (-7.73%)</td><td>0.70 (-8.13%)</td><td>0.15 <b>(+66.67%)</b></td><td>1.03 (+4.29%)</td><td>0.84 (-1.36%)</td><td>0.77 (-7.73%)</td><td>0.69 (-8.13%)</td><td>0.15 <b>(+66.67%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.01 (n/a)</td><td>0.87 (n/a)</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.09 (n/a)</td><td>0.99 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.75 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.19 (-15.51%)</td><td>1.08 (-4.84%)</td><td>1.12 (-3.70%)</td><td>0.93 (+1.68%)</td><td>0.10 <b>(-54.46%)</b></td><td>1.18 (-15.51%)</td><td>1.07 (-4.84%)</td><td>1.11 (-3.70%)</td><td>0.92 (+1.68%)</td><td>0.10 <b>(-54.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.41 (n/a)</td><td>1.14 (n/a)</td><td>1.16 (n/a)</td><td>0.91 (n/a)</td><td>0.22 (n/a)</td><td>1.39 (n/a)</td><td>1.12 (n/a)</td><td>1.15 (n/a)</td><td>0.90 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>17.01 (-5.88%)</td><td>15.99 (+5.57%)</td><td>16.14 (+3.11%)</td><td>14.37 (+18.92%)</td><td>0.98 <b>(-60.96%)</b></td><td>16.81 (-5.88%)</td><td>15.81 (+5.57%)</td><td>15.95 (+3.11%)</td><td>14.20 (+18.92%)</td><td>0.97 <b>(-60.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>18.07 (n/a)</td><td>15.15 (n/a)</td><td>15.65 (n/a)</td><td>12.08 (n/a)</td><td>2.52 (n/a)</td><td>17.86 (n/a)</td><td>14.97 (n/a)</td><td>15.47 (n/a)</td><td>11.94 (n/a)</td><td>2.49 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>14.05 (+4.92%)</td><td>13.37 (+4.63%)</td><td>13.20 (-0.10%)</td><td>13.16 (+11.19%)</td><td>0.38 <b>(-49.69%)</b></td><td>13.80 (+4.92%)</td><td>13.14 (+4.63%)</td><td>12.97 (-0.10%)</td><td>12.93 (+11.19%)</td><td>0.37 <b>(-49.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.39 (n/a)</td><td>12.78 (n/a)</td><td>13.21 (n/a)</td><td>11.83 (n/a)</td><td>0.76 (n/a)</td><td>13.16 (n/a)</td><td>12.56 (n/a)</td><td>12.98 (n/a)</td><td>11.62 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>7.87 (+0.90%)</td><td>7.50 (+1.43%)</td><td>7.64 (+3.26%)</td><td>6.86 (-2.35%)</td><td>0.39 (+16.17%)</td><td>7.73 (+0.90%)</td><td>7.37 (+1.43%)</td><td>7.51 (+3.26%)</td><td>6.74 (-2.35%)</td><td>0.38 (+16.17%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>7.80 (n/a)</td><td>7.39 (n/a)</td><td>7.40 (n/a)</td><td>7.03 (n/a)</td><td>0.34 (n/a)</td><td>7.66 (n/a)</td><td>7.26 (n/a)</td><td>7.27 (n/a)</td><td>6.90 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.07 (-1.49%)</td><td>5.43 (+1.74%)</td><td>5.47 (+0.84%)</td><td>4.63 (+1.51%)</td><td>0.61 (+2.00%)</td><td>5.97 (-1.49%)</td><td>5.34 (+1.74%)</td><td>5.38 (+0.84%)</td><td>4.56 (+1.51%)</td><td>0.60 (+2.00%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.16 (n/a)</td><td>5.34 (n/a)</td><td>5.43 (n/a)</td><td>4.57 (n/a)</td><td>0.59 (n/a)</td><td>6.06 (n/a)</td><td>5.25 (n/a)</td><td>5.34 (n/a)</td><td>4.49 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>13.22 (n/a)</td><td>12.92 (n/a)</td><td>13.12 (n/a)</td><td>11.98 (n/a)</td><td>0.52 (n/a)</td><td>13.21 (n/a)</td><td>12.91 (n/a)</td><td>13.11 (n/a)</td><td>11.98 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>13.38 (n/a)</td><td>12.68 (n/a)</td><td>13.16 (n/a)</td><td>10.54 (n/a)</td><td>1.20 (n/a)</td><td>13.38 (n/a)</td><td>12.67 (n/a)</td><td>13.15 (n/a)</td><td>10.53 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>179.26 (n/a)</td><td>185.10 (n/a)</td><td>132.90 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>232.60 (n/a)</td><td>176.92 (n/a)</td><td>180.80 (n/a)</td><td>115.30 (n/a)</td><td>54.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.60 (n/a)</td><td>220.18 (n/a)</td><td>194.90 (n/a)</td><td>160.10 (n/a)</td><td>67.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>191.02 (n/a)</td><td>187.30 (n/a)</td><td>164.90 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>186.90 (n/a)</td><td>180.38 (n/a)</td><td>180.70 (n/a)</td><td>175.20 (n/a)</td><td>4.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>187.56 (n/a)</td><td>189.60 (n/a)</td><td>142.50 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>185.02 (n/a)</td><td>183.30 (n/a)</td><td>165.70 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>210.94 (n/a)</td><td>221.30 (n/a)</td><td>166.40 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.08 <b>(+39.98%)</b></td><td>0.05 (+19.01%)</td><td>0.05 (+8.59%)</td><td>0.04 (+6.25%)</td><td>0.01 <b>(+113.02%)</b></td><td>198.90 (-5.91%)</td><td>156.38 (-13.35%)</td><td>164.50 (-7.95%)</td><td>108.30 <b>(-28.56%)</b></td><td>36.00 <b>(+41.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>180.48 (n/a)</td><td>178.70 (n/a)</td><td>151.60 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (-16.31%)</td><td>0.06 (+3.41%)</td><td>0.07 <b>(+35.78%)</b></td><td>0.04 (+2.99%)</td><td>0.01 (-19.18%)</td><td>194.00 (-2.90%)</td><td>147.36 (-4.51%)</td><td>124.40 <b>(-26.35%)</b></td><td>117.80 (+19.47%)</td><td>37.13 (-4.61%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>154.32 (n/a)</td><td>168.90 (n/a)</td><td>98.60 (n/a)</td><td>38.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (-7.94%)</td><td>0.04 <b>(-23.35%)</b></td><td>0.04 <b>(-33.53%)</b></td><td>0.03 <b>(-21.78%)</b></td><td>0.01 (+17.97%)</td><td>238.70 <b>(+27.85%)</b></td><td>198.74 <b>(+34.54%)</b></td><td>213.80 <b>(+50.46%)</b></td><td>118.10 (+8.65%)</td><td>49.22 <b>(+59.36%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.70 (n/a)</td><td>147.72 (n/a)</td><td>142.10 (n/a)</td><td>108.70 (n/a)</td><td>30.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 <b>(+31.74%)</b></td><td>0.05 (+13.47%)</td><td>0.05 (+1.05%)</td><td>0.04 (+8.70%)</td><td>0.01 <b>(+58.62%)</b></td><td>217.10 (-7.97%)</td><td>165.80 (-10.53%)</td><td>166.30 (-1.01%)</td><td>118.20 <b>(-24.13%)</b></td><td>35.21 (+8.39%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.90 (n/a)</td><td>185.32 (n/a)</td><td>168.00 (n/a)</td><td>155.80 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 <b>(+27.06%)</b></td><td>0.05 (+9.83%)</td><td>0.05 (+2.38%)</td><td>0.04 (+10.87%)</td><td>0.01 <b>(+58.39%)</b></td><td>201.60 (-9.80%)</td><td>172.10 (-7.98%)</td><td>170.60 (-2.35%)</td><td>127.90 <b>(-21.29%)</b></td><td>28.61 (+10.63%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>187.02 (n/a)</td><td>174.70 (n/a)</td><td>162.50 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (+8.72%)</td><td>0.05 (+5.75%)</td><td>0.05 (+0.06%)</td><td>0.04 (+17.12%)</td><td>0.01 (-4.37%)</td><td>201.70 (-14.61%)</td><td>165.14 (-6.32%)</td><td>157.00 (-0.06%)</td><td>131.00 (-8.01%)</td><td>30.76 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>176.28 (n/a)</td><td>157.10 (n/a)</td><td>142.40 (n/a)</td><td>39.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (+11.02%)</td><td>0.05 (+7.07%)</td><td>0.05 (+9.78%)</td><td>0.04 (-4.59%)</td><td>0.01 <b>(+45.03%)</b></td><td>197.60 (+4.83%)</td><td>158.50 (-5.47%)</td><td>152.60 (-8.90%)</td><td>124.10 (-9.88%)</td><td>27.57 <b>(+37.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>167.68 (n/a)</td><td>167.50 (n/a)</td><td>137.70 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+14.35%)</td><td>0.04 (+0.19%)</td><td>0.04 (-3.62%)</td><td>0.04 (+0.91%)</td><td>0.01 <b>(+82.68%)</b></td><td>219.90 (-0.90%)</td><td>197.58 (+0.85%)</td><td>198.00 (+3.72%)</td><td>155.30 (-12.56%)</td><td>26.40 <b>(+56.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>221.90 (n/a)</td><td>195.92 (n/a)</td><td>190.90 (n/a)</td><td>177.60 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (-4.71%)</td><td>0.05 (-6.50%)</td><td>0.04 (-10.65%)</td><td>0.04 (-1.96%)</td><td>0.01 (+2.50%)</td><td>193.70 (+2.00%)</td><td>166.74 (+7.46%)</td><td>184.80 (+11.93%)</td><td>125.60 (+4.93%)</td><td>32.57 (+13.25%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>155.16 (n/a)</td><td>165.10 (n/a)</td><td>119.70 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+8.20%)</td><td>0.04 (+4.29%)</td><td>0.04 (+4.14%)</td><td>0.03 (-2.78%)</td><td>0.00 <b>(+42.93%)</b></td><td>240.80 (+2.86%)</td><td>207.92 (-3.63%)</td><td>212.00 (-3.99%)</td><td>176.90 (-7.62%)</td><td>24.00 <b>(+35.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.10 (n/a)</td><td>215.76 (n/a)</td><td>220.80 (n/a)</td><td>191.50 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-10.99%)</td><td>0.05 (-10.15%)</td><td>0.06 (+0.69%)</td><td>0.02 <b>(-44.22%)</b></td><td>0.02 <b>(+39.39%)</b></td><td>345.10 <b>(+79.27%)</b></td><td>187.34 <b>(+22.22%)</b></td><td>142.30 (-0.70%)</td><td>130.50 (+12.31%)</td><td>90.13 <b>(+184.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.50 (n/a)</td><td>153.28 (n/a)</td><td>143.30 (n/a)</td><td>116.20 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+4.27%)</td><td>0.04 (+0.56%)</td><td>0.04 (-0.33%)</td><td>0.03 (-12.02%)</td><td>0.01 <b>(+53.99%)</b></td><td>321.00 (+13.67%)</td><td>228.84 (+2.62%)</td><td>216.80 (+0.37%)</td><td>171.70 (-4.08%)</td><td>61.18 <b>(+62.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.40 (n/a)</td><td>223.00 (n/a)</td><td>216.00 (n/a)</td><td>179.00 (n/a)</td><td>37.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 <b>(+43.47%)</b></td><td>0.06 <b>(+37.99%)</b></td><td>0.05 <b>(+32.03%)</b></td><td>0.05 <b>(+35.34%)</b></td><td>0.01 <b>(+72.89%)</b></td><td>170.80 <b>(-26.09%)</b></td><td>149.04 <b>(-26.86%)</b></td><td>163.30 <b>(-24.29%)</b></td><td>112.90 <b>(-30.31%)</b></td><td>25.10 (-9.42%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>203.78 (n/a)</td><td>215.70 (n/a)</td><td>162.00 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+9.86%)</td><td>0.05 (+19.76%)</td><td>0.05 (+15.98%)</td><td>0.04 <b>(+86.06%)</b></td><td>0.00 <b>(-54.61%)</b></td><td>188.70 <b>(-46.24%)</b></td><td>168.90 <b>(-21.99%)</b></td><td>167.90 (-13.76%)</td><td>150.00 (-8.98%)</td><td>16.71 <b>(-78.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.00 (n/a)</td><td>216.50 (n/a)</td><td>194.70 (n/a)</td><td>164.80 (n/a)</td><td>77.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-6.73%)</td><td>0.04 (-11.65%)</td><td>0.05 (-7.58%)</td><td>0.03 (-10.58%)</td><td>0.01 (+11.85%)</td><td>258.10 (+11.83%)</td><td>194.38 (+15.07%)</td><td>175.50 (+8.20%)</td><td>141.40 (+7.20%)</td><td>49.67 <b>(+32.91%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.80 (n/a)</td><td>168.92 (n/a)</td><td>162.20 (n/a)</td><td>131.90 (n/a)</td><td>37.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (+6.43%)</td><td>0.05 (-5.65%)</td><td>0.04 (-13.20%)</td><td>0.04 (+6.55%)</td><td>0.01 <b>(+23.16%)</b></td><td>206.40 (-6.14%)</td><td>178.74 (+7.43%)</td><td>196.20 (+15.21%)</td><td>111.80 (-6.05%)</td><td>39.43 (+7.69%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>166.38 (n/a)</td><td>170.30 (n/a)</td><td>119.00 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (+14.44%)</td><td>0.04 (+4.21%)</td><td>0.04 (-2.69%)</td><td>0.03 (-0.18%)</td><td>0.01 <b>(+49.24%)</b></td><td>237.10 (+0.17%)</td><td>192.20 (-2.19%)</td><td>203.00 (+2.78%)</td><td>132.50 (-12.66%)</td><td>39.81 <b>(+29.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.70 (n/a)</td><td>196.50 (n/a)</td><td>197.50 (n/a)</td><td>151.70 (n/a)</td><td>30.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (-19.38%)</td><td>0.04 (-15.89%)</td><td>0.04 (-12.79%)</td><td>0.04 (-11.23%)</td><td>0.01 <b>(-30.56%)</b></td><td>225.90 (+12.67%)</td><td>202.72 (+18.22%)</td><td>204.60 (+14.69%)</td><td>164.20 <b>(+24.02%)</b></td><td>25.16 (-0.01%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>171.48 (n/a)</td><td>178.40 (n/a)</td><td>132.40 (n/a)</td><td>25.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.18 (-0.13%)</td><td>0.18 (-0.14%)</td><td>0.18 (-0.27%)</td><td>0.18 (+0.16%)</td><td>0.00 <b>(-56.86%)</b></td><td>47624.80 (-0.16%)</td><td>47572.10 (+0.14%)</td><td>47584.00 (+0.27%)</td><td>47500.60 (+0.13%)</td><td>48.01 <b>(-56.90%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47702.20 (n/a)</td><td>47507.62 (n/a)</td><td>47455.20 (n/a)</td><td>47438.10 (n/a)</td><td>111.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.21 (+11.55%)</td><td>0.17 (-3.89%)</td><td>0.18 (-4.13%)</td><td>0.13 (-14.73%)</td><td>0.03 <b>(+111.45%)</b></td><td>183.70 (+17.31%)</td><td>148.78 (+6.38%)</td><td>138.70 (+4.29%)</td><td>116.00 (-10.36%)</td><td>27.97 <b>(+127.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>156.60 (n/a)</td><td>139.86 (n/a)</td><td>133.00 (n/a)</td><td>129.40 (n/a)</td><td>12.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.36 (+16.57%)</td><td>0.28 (+0.17%)</td><td>0.27 (-7.64%)</td><td>0.20 (-10.08%)</td><td>0.06 <b>(+84.81%)</b></td><td>204.60 (+11.20%)</td><td>151.94 (+2.70%)</td><td>153.00 (+8.28%)</td><td>114.70 (-14.21%)</td><td>35.58 <b>(+71.73%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>184.00 (n/a)</td><td>147.94 (n/a)</td><td>141.30 (n/a)</td><td>133.70 (n/a)</td><td>20.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (+2.93%)</td><td>0.04 (+13.96%)</td><td>0.03 (+16.51%)</td><td>0.03 <b>(+22.64%)</b></td><td>0.00 <b>(-46.38%)</b></td><td>152.20 (-18.44%)</td><td>144.44 (-13.30%)</td><td>147.60 (-14.19%)</td><td>128.40 (-2.87%)</td><td>9.29 <b>(-57.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.60 (n/a)</td><td>166.60 (n/a)</td><td>172.00 (n/a)</td><td>132.20 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-11.29%)</td><td>0.05 (-11.99%)</td><td>0.04 (-16.39%)</td><td>0.04 (-11.13%)</td><td>0.01 (-9.13%)</td><td>204.60 (+12.54%)</td><td>169.48 (+13.87%)</td><td>188.60 (+19.59%)</td><td>128.60 (+12.81%)</td><td>37.52 (+14.84%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>148.84 (n/a)</td><td>157.70 (n/a)</td><td>114.00 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 <b>(-21.72%)</b></td><td>0.07 (+1.89%)</td><td>0.07 (+3.60%)</td><td>0.05 <b>(+60.61%)</b></td><td>0.01 <b>(-63.34%)</b></td><td>232.10 <b>(-37.74%)</b></td><td>189.82 (-11.45%)</td><td>187.80 (-3.44%)</td><td>169.70 <b>(+27.79%)</b></td><td>25.35 <b>(-72.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>372.80 (n/a)</td><td>214.36 (n/a)</td><td>194.50 (n/a)</td><td>132.80 (n/a)</td><td>92.53 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-4.61%)</td><td>0.05 (-12.67%)</td><td>0.05 (-14.16%)</td><td>0.04 (-19.09%)</td><td>0.01 <b>(+20.36%)</b></td><td>212.60 <b>(+23.60%)</b></td><td>172.60 (+15.81%)</td><td>161.40 (+16.53%)</td><td>136.00 (+4.86%)</td><td>30.30 <b>(+54.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>149.04 (n/a)</td><td>138.50 (n/a)</td><td>129.70 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 <b>(-30.23%)</b></td><td>0.05 (-15.20%)</td><td>0.05 (-9.70%)</td><td>0.05 (+11.40%)</td><td>0.00 <b>(-76.88%)</b></td><td>223.60 (-10.24%)</td><td>196.94 (+11.83%)</td><td>192.70 (+10.75%)</td><td>187.50 <b>(+43.35%)</b></td><td>15.12 <b>(-68.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>249.10 (n/a)</td><td>176.10 (n/a)</td><td>174.00 (n/a)</td><td>130.80 (n/a)</td><td>48.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 <b>(+20.49%)</b></td><td>0.05 (-3.72%)</td><td>0.04 (-10.40%)</td><td>0.03 <b>(-39.66%)</b></td><td>0.02 <b>(+247.91%)</b></td><td>291.70 <b>(+65.74%)</b></td><td>188.42 (+17.50%)</td><td>186.00 (+11.64%)</td><td>111.20 (-17.01%)</td><td>75.37 <b>(+369.12%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.00 (n/a)</td><td>160.36 (n/a)</td><td>166.60 (n/a)</td><td>134.00 (n/a)</td><td>16.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (-11.89%)</td><td>0.06 (-6.94%)</td><td>0.06 (-5.33%)</td><td>0.04 (-11.74%)</td><td>0.01 (-14.34%)</td><td>230.50 (+13.32%)</td><td>175.28 (+7.18%)</td><td>168.50 (+5.64%)</td><td>143.90 (+13.49%)</td><td>35.90 (+7.54%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>163.54 (n/a)</td><td>159.50 (n/a)</td><td>126.80 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (+6.48%)</td><td>0.05 (-2.83%)</td><td>0.04 (-6.38%)</td><td>0.04 (-17.86%)</td><td>0.01 <b>(+38.13%)</b></td><td>225.20 <b>(+21.73%)</b></td><td>176.10 (+5.91%)</td><td>188.00 (+6.82%)</td><td>111.40 (-6.07%)</td><td>41.78 <b>(+54.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>166.28 (n/a)</td><td>176.00 (n/a)</td><td>118.60 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-19.14%)</td><td>0.05 (-16.08%)</td><td>0.05 <b>(-22.88%)</b></td><td>0.04 (+7.91%)</td><td>0.01 <b>(-48.36%)</b></td><td>221.50 (-7.32%)</td><td>192.94 (+15.23%)</td><td>189.30 <b>(+29.66%)</b></td><td>157.80 <b>(+23.67%)</b></td><td>26.07 <b>(-41.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>167.44 (n/a)</td><td>146.00 (n/a)</td><td>127.60 (n/a)</td><td>44.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (-9.92%)</td><td>0.05 (-9.98%)</td><td>0.04 <b>(-29.09%)</b></td><td>0.04 <b>(+30.67%)</b></td><td>0.01 <b>(-35.00%)</b></td><td>204.10 <b>(-23.47%)</b></td><td>169.86 (+4.70%)</td><td>186.60 <b>(+40.94%)</b></td><td>130.30 (+10.99%)</td><td>34.16 <b>(-45.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>266.70 (n/a)</td><td>162.24 (n/a)</td><td>132.40 (n/a)</td><td>117.40 (n/a)</td><td>62.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (-13.29%)</td><td>0.05 (-4.18%)</td><td>0.05 (-11.00%)</td><td>0.04 <b>(+33.41%)</b></td><td>0.00 <b>(-65.63%)</b></td><td>218.20 <b>(-25.04%)</b></td><td>196.78 (-0.52%)</td><td>189.90 (+12.37%)</td><td>180.60 (+15.33%)</td><td>16.76 <b>(-70.24%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.10 (n/a)</td><td>197.80 (n/a)</td><td>169.00 (n/a)</td><td>156.60 (n/a)</td><td>56.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (+10.18%)</td><td>0.04 (-5.61%)</td><td>0.04 (-14.11%)</td><td>0.03 (-4.47%)</td><td>0.01 <b>(+47.66%)</b></td><td>234.80 (+4.68%)</td><td>192.56 (+8.47%)</td><td>208.30 (+16.43%)</td><td>129.20 (-9.27%)</td><td>42.77 <b>(+38.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>177.52 (n/a)</td><td>178.90 (n/a)</td><td>142.40 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (+9.87%)</td><td>0.05 (+13.07%)</td><td>0.04 (+3.88%)</td><td>0.04 <b>(+30.95%)</b></td><td>0.01 (-3.18%)</td><td>237.00 <b>(-23.65%)</b></td><td>193.94 (-12.84%)</td><td>205.30 (-3.75%)</td><td>159.30 (-8.97%)</td><td>33.25 <b>(-36.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.40 (n/a)</td><td>222.52 (n/a)</td><td>213.30 (n/a)</td><td>175.00 (n/a)</td><td>52.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (+11.01%)</td><td>0.05 (+6.34%)</td><td>0.05 (-5.29%)</td><td>0.04 <b>(+46.19%)</b></td><td>0.01 (-19.14%)</td><td>203.70 <b>(-31.60%)</b></td><td>176.86 (-9.67%)</td><td>177.20 (+5.60%)</td><td>128.90 (-9.92%)</td><td>30.50 <b>(-51.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.80 (n/a)</td><td>195.80 (n/a)</td><td>167.80 (n/a)</td><td>143.10 (n/a)</td><td>62.45 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (+13.41%)</td><td>0.05 (+6.42%)</td><td>0.05 (+1.45%)</td><td>0.03 (-1.13%)</td><td>0.02 <b>(+30.09%)</b></td><td>312.40 (+1.17%)</td><td>203.54 (-2.85%)</td><td>179.50 (-1.43%)</td><td>124.00 (-11.81%)</td><td>74.75 (+15.47%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>308.80 (n/a)</td><td>209.52 (n/a)</td><td>182.10 (n/a)</td><td>140.60 (n/a)</td><td>64.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 <b>(+30.27%)</b></td><td>0.04 (+4.78%)</td><td>0.04 (-0.74%)</td><td>0.03 (-4.12%)</td><td>0.01 <b>(+276.68%)</b></td><td>248.60 (+4.28%)</td><td>213.76 (-2.81%)</td><td>215.40 (+0.75%)</td><td>163.60 <b>(-23.23%)</b></td><td>31.89 <b>(+194.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>219.94 (n/a)</td><td>213.80 (n/a)</td><td>213.10 (n/a)</td><td>10.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.55 <b>(-29.33%)</b></td><td>0.50 <b>(-22.55%)</b></td><td>0.50 <b>(-25.38%)</b></td><td>0.46 (-6.75%)</td><td>0.04 <b>(-67.78%)</b></td><td>211.40 (+7.20%)</td><td>196.26 <b>(+26.29%)</b></td><td>198.10 <b>(+34.03%)</b></td><td>178.10 <b>(+41.57%)</b></td><td>14.13 <b>(-51.21%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.67 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>197.20 (n/a)</td><td>155.40 (n/a)</td><td>147.80 (n/a)</td><td>125.80 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.60 (-18.28%)</td><td>0.52 (-17.24%)</td><td>0.52 <b>(-20.78%)</b></td><td>0.44 (-14.89%)</td><td>0.06 <b>(-28.29%)</b></td><td>223.10 (+17.48%)</td><td>189.48 <b>(+20.40%)</b></td><td>187.70 <b>(+26.23%)</b></td><td>164.10 <b>(+22.37%)</b></td><td>22.17 (+2.61%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.73 (n/a)</td><td>0.63 (n/a)</td><td>0.66 (n/a)</td><td>0.52 (n/a)</td><td>0.08 (n/a)</td><td>189.90 (n/a)</td><td>157.38 (n/a)</td><td>148.70 (n/a)</td><td>134.10 (n/a)</td><td>21.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.58 (-3.69%)</td><td>0.53 (-2.32%)</td><td>0.55 (+0.94%)</td><td>0.44 (-12.77%)</td><td>0.05 <b>(+54.77%)</b></td><td>222.40 (+14.64%)</td><td>186.06 (+2.99%)</td><td>178.70 (-0.94%)</td><td>170.60 (+3.83%)</td><td>20.78 <b>(+89.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.60 (n/a)</td><td>0.55 (n/a)</td><td>0.55 (n/a)</td><td>0.51 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>180.66 (n/a)</td><td>180.40 (n/a)</td><td>164.30 (n/a)</td><td>10.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.55 (-19.41%)</td><td>0.49 (-1.26%)</td><td>0.49 (-8.63%)</td><td>0.40 <b>(+27.24%)</b></td><td>0.06 <b>(-56.52%)</b></td><td>245.70 <b>(-21.40%)</b></td><td>201.94 (-4.51%)</td><td>201.30 (+9.46%)</td><td>177.50 <b>(+24.04%)</b></td><td>27.48 <b>(-58.66%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.69 (n/a)</td><td>0.50 (n/a)</td><td>0.53 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>312.60 (n/a)</td><td>211.48 (n/a)</td><td>183.90 (n/a)</td><td>143.10 (n/a)</td><td>66.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.47 <b>(-20.02%)</b></td><td>0.38 (-5.19%)</td><td>0.37 (-7.56%)</td><td>0.31 <b>(+55.51%)</b></td><td>0.06 <b>(-58.33%)</b></td><td>234.20 <b>(-35.69%)</b></td><td>198.28 (-4.65%)</td><td>199.50 (+8.19%)</td><td>158.50 <b>(+25.00%)</b></td><td>27.87 <b>(-69.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.58 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>364.20 (n/a)</td><td>207.96 (n/a)</td><td>184.40 (n/a)</td><td>126.80 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.52 (-10.93%)</td><td>0.42 (-5.62%)</td><td>0.40 (-7.05%)</td><td>0.34 (+2.59%)</td><td>0.07 <b>(-37.27%)</b></td><td>216.80 (-2.56%)</td><td>181.18 (+3.05%)</td><td>182.90 (+7.59%)</td><td>142.20 (+12.23%)</td><td>27.93 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>222.50 (n/a)</td><td>175.82 (n/a)</td><td>170.00 (n/a)</td><td>126.70 (n/a)</td><td>42.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.53 (-7.14%)</td><td>0.41 (-10.71%)</td><td>0.35 (-19.33%)</td><td>0.33 (-2.02%)</td><td>0.09 (-2.39%)</td><td>221.30 (+2.03%)</td><td>186.80 (+12.35%)</td><td>211.80 <b>(+23.93%)</b></td><td>140.20 (+7.68%)</td><td>39.50 (+10.46%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>216.90 (n/a)</td><td>166.26 (n/a)</td><td>170.90 (n/a)</td><td>130.20 (n/a)</td><td>35.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.43 (+1.36%)</td><td>0.35 (-5.35%)</td><td>0.38 (+1.60%)</td><td>0.22 <b>(-28.71%)</b></td><td>0.08 <b>(+65.21%)</b></td><td>329.20 <b>(+40.26%)</b></td><td>220.56 (+9.86%)</td><td>193.80 (-1.57%)</td><td>170.10 (-1.33%)</td><td>63.48 <b>(+138.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>234.70 (n/a)</td><td>200.76 (n/a)</td><td>196.90 (n/a)</td><td>172.40 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.35 <b>(+43.48%)</b></td><td>0.84 <b>(+20.84%)</b></td><td>0.71 (+12.72%)</td><td>0.65 (+10.28%)</td><td>0.30 <b>(+99.95%)</b></td><td>202.20 (-9.29%)</td><td>169.22 (-13.50%)</td><td>185.80 (-11.27%)</td><td>97.30 <b>(-30.25%)</b></td><td>43.83 <b>(+24.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.94 (n/a)</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.59 (n/a)</td><td>0.15 (n/a)</td><td>222.90 (n/a)</td><td>195.62 (n/a)</td><td>209.40 (n/a)</td><td>139.50 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.89 (-2.63%)</td><td>0.75 (+18.37%)</td><td>0.75 <b>(+31.94%)</b></td><td>0.61 <b>(+73.81%)</b></td><td>0.11 <b>(-50.85%)</b></td><td>216.00 <b>(-42.46%)</b></td><td>177.58 <b>(-23.15%)</b></td><td>174.80 <b>(-24.20%)</b></td><td>148.00 (+2.64%)</td><td>26.80 <b>(-70.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.91 (n/a)</td><td>0.63 (n/a)</td><td>0.57 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>375.40 (n/a)</td><td>231.08 (n/a)</td><td>230.60 (n/a)</td><td>144.20 (n/a)</td><td>91.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.01 (+13.25%)</td><td>0.75 (+16.44%)</td><td>0.66 (+12.38%)</td><td>0.64 <b>(+37.36%)</b></td><td>0.16 (-1.23%)</td><td>203.60 <b>(-27.21%)</b></td><td>179.38 (-15.44%)</td><td>198.20 (-11.00%)</td><td>129.80 (-11.70%)</td><td>32.68 <b>(-34.24%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.89 (n/a)</td><td>0.65 (n/a)</td><td>0.59 (n/a)</td><td>0.47 (n/a)</td><td>0.16 (n/a)</td><td>279.70 (n/a)</td><td>212.14 (n/a)</td><td>222.70 (n/a)</td><td>147.00 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (-12.42%)</td><td>0.02 (+0.23%)</td><td>0.02 (-0.64%)</td><td>0.02 <b>(+20.02%)</b></td><td>0.01 <b>(-35.02%)</b></td><td>208.20 (-16.69%)</td><td>172.98 (-4.97%)</td><td>180.30 (+0.67%)</td><td>120.90 (+14.16%)</td><td>33.63 <b>(-37.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>182.02 (n/a)</td><td>179.10 (n/a)</td><td>105.90 (n/a)</td><td>54.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (+6.70%)</td><td>0.03 (+3.60%)</td><td>0.03 (+6.66%)</td><td>0.02 (+10.70%)</td><td>0.01 (-2.98%)</td><td>227.90 (-9.67%)</td><td>169.68 (-4.30%)</td><td>153.10 (-6.25%)</td><td>131.50 (-6.27%)</td><td>37.44 (-17.28%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.30 (n/a)</td><td>177.30 (n/a)</td><td>163.30 (n/a)</td><td>140.30 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (-6.58%)</td><td>0.02 (-9.25%)</td><td>0.02 (-14.41%)</td><td>0.01 (-16.72%)</td><td>0.01 (-11.99%)</td><td>285.50 <b>(+20.06%)</b></td><td>199.82 (+9.77%)</td><td>195.60 (+16.85%)</td><td>136.80 (+7.04%)</td><td>55.97 (+8.91%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>182.04 (n/a)</td><td>167.40 (n/a)</td><td>127.80 (n/a)</td><td>51.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.86 (-13.26%)</td><td>0.76 (-4.00%)</td><td>0.79 (+8.42%)</td><td>0.63 (-13.28%)</td><td>0.09 <b>(-22.01%)</b></td><td>211.30 (+15.34%)</td><td>175.42 (+3.92%)</td><td>166.80 (-7.74%)</td><td>153.60 (+15.32%)</td><td>22.33 (+5.66%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.99 (n/a)</td><td>0.79 (n/a)</td><td>0.73 (n/a)</td><td>0.72 (n/a)</td><td>0.11 (n/a)</td><td>183.20 (n/a)</td><td>168.80 (n/a)</td><td>180.80 (n/a)</td><td>133.20 (n/a)</td><td>21.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.13 (+13.43%)</td><td>0.72 (-10.93%)</td><td>0.64 <b>(-22.64%)</b></td><td>0.54 (-11.61%)</td><td>0.24 <b>(+40.96%)</b></td><td>243.50 (+13.15%)</td><td>196.22 (+15.67%)</td><td>206.40 <b>(+29.24%)</b></td><td>117.00 (-11.83%)</td><td>48.42 <b>(+33.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.00 (n/a)</td><td>0.81 (n/a)</td><td>0.83 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>215.20 (n/a)</td><td>169.64 (n/a)</td><td>159.70 (n/a)</td><td>132.70 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.94 (-2.20%)</td><td>0.83 (+3.00%)</td><td>0.87 (+1.10%)</td><td>0.71 <b>(+29.11%)</b></td><td>0.10 <b>(-38.28%)</b></td><td>185.80 <b>(-22.58%)</b></td><td>161.60 (-5.40%)</td><td>152.10 (-1.11%)</td><td>140.60 (+2.25%)</td><td>19.22 <b>(-52.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.96 (n/a)</td><td>0.80 (n/a)</td><td>0.86 (n/a)</td><td>0.55 (n/a)</td><td>0.16 (n/a)</td><td>240.00 (n/a)</td><td>170.82 (n/a)</td><td>153.80 (n/a)</td><td>137.50 (n/a)</td><td>40.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.95 (-7.70%)</td><td>0.79 (-7.13%)</td><td>0.78 (-12.40%)</td><td>0.67 (+17.34%)</td><td>0.10 <b>(-39.14%)</b></td><td>196.40 (-14.79%)</td><td>170.06 (+4.85%)</td><td>170.40 (+14.13%)</td><td>138.40 (+8.38%)</td><td>20.89 <b>(-47.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.03 (n/a)</td><td>0.85 (n/a)</td><td>0.88 (n/a)</td><td>0.57 (n/a)</td><td>0.17 (n/a)</td><td>230.50 (n/a)</td><td>162.20 (n/a)</td><td>149.30 (n/a)</td><td>127.70 (n/a)</td><td>39.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.80 (-15.44%)</td><td>0.69 (-14.61%)</td><td>0.68 (-17.14%)</td><td>0.57 <b>(-21.43%)</b></td><td>0.10 (+15.66%)</td><td>232.50 <b>(+27.33%)</b></td><td>193.56 (+18.07%)</td><td>194.40 <b>(+20.67%)</b></td><td>165.80 (+18.26%)</td><td>27.91 <b>(+71.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.94 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>0.08 (n/a)</td><td>182.60 (n/a)</td><td>163.94 (n/a)</td><td>161.10 (n/a)</td><td>140.20 (n/a)</td><td>16.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (+9.05%)</td><td>0.02 (-10.57%)</td><td>0.02 (-18.96%)</td><td>0.02 (-2.40%)</td><td>0.00 <b>(+38.88%)</b></td><td>216.20 (+2.46%)</td><td>193.60 (+13.43%)</td><td>203.90 <b>(+23.43%)</b></td><td>133.30 (-8.32%)</td><td>34.36 <b>(+28.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>170.68 (n/a)</td><td>165.20 (n/a)</td><td>145.40 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (-11.77%)</td><td>0.02 (-7.56%)</td><td>0.02 (-10.16%)</td><td>0.02 (-6.27%)</td><td>0.00 <b>(-22.12%)</b></td><td>231.10 (+6.69%)</td><td>186.62 (+7.62%)</td><td>183.70 (+11.27%)</td><td>160.10 (+13.31%)</td><td>26.73 (-4.70%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.60 (n/a)</td><td>173.40 (n/a)</td><td>165.10 (n/a)</td><td>141.30 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.00 (-6.52%)</td><td>0.00 (-4.50%)</td><td>0.00 (-4.55%)</td><td>0.00 (-2.33%)</td><td>0.00 <b>(-63.88%)</b></td><td>977.72 (+2.55%)</td><td>966.63 (+4.59%)</td><td>971.51 (+4.05%)</td><td>953.22 (+6.71%)</td><td>11.63 <b>(-59.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>953.37 (n/a)</td><td>924.17 (n/a)</td><td>933.67 (n/a)</td><td>893.29 (n/a)</td><td>28.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.01 (-2.33%)</td><td>0.01 (-4.63%)</td><td>0.01 (-3.66%)</td><td>0.01 (-11.54%)</td><td>0.00 <b>(+56.72%)</b></td><td>1180.69 (+12.02%)</td><td>1050.25 (+4.77%)</td><td>1031.46 (+2.77%)</td><td>971.68 (+2.40%)</td><td>77.66 <b>(+71.80%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1054.03 (n/a)</td><td>1002.43 (n/a)</td><td>1003.61 (n/a)</td><td>948.91 (n/a)</td><td>45.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.97 (-2.44%)</td><td>0.96 (-0.66%)</td><td>0.96 (+0.11%)</td><td>0.95 (+1.20%)</td><td>0.01 <b>(-70.00%)</b></td><td>2197.77 (-1.19%)</td><td>2180.96 (+0.62%)</td><td>2181.66 (-0.11%)</td><td>2156.11 (+2.50%)</td><td>15.93 <b>(-69.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2224.18 (n/a)</td><td>2167.46 (n/a)</td><td>2184.06 (n/a)</td><td>2103.51 (n/a)</td><td>52.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.37 (-5.52%)</td><td>3.04 (+3.98%)</td><td>3.06 (+17.25%)</td><td>2.57 (+5.39%)</td><td>0.31 <b>(-39.35%)</b></td><td>203.90 (-5.12%)</td><td>174.26 (-5.23%)</td><td>171.20 (-14.70%)</td><td>155.60 (+5.85%)</td><td>19.00 <b>(-38.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.57 (n/a)</td><td>2.92 (n/a)</td><td>2.61 (n/a)</td><td>2.44 (n/a)</td><td>0.52 (n/a)</td><td>214.90 (n/a)</td><td>183.88 (n/a)</td><td>200.70 (n/a)</td><td>147.00 (n/a)</td><td>30.70 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.57 <b>(-32.92%)</b></td><td>4.13 (-18.08%)</td><td>4.12 (-15.25%)</td><td>3.75 (-5.17%)</td><td>0.30 <b>(-72.31%)</b></td><td>279.30 (+5.48%)</td><td>254.78 (+18.61%)</td><td>254.40 (+18.00%)</td><td>229.50 <b>(+49.03%)</b></td><td>18.31 <b>(-55.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.81 (n/a)</td><td>5.04 (n/a)</td><td>4.86 (n/a)</td><td>3.96 (n/a)</td><td>1.08 (n/a)</td><td>264.80 (n/a)</td><td>214.80 (n/a)</td><td>215.60 (n/a)</td><td>154.00 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.87 (+15.36%)</td><td>2.91 (-1.11%)</td><td>2.78 (-5.99%)</td><td>2.47 (+0.28%)</td><td>0.57 <b>(+66.73%)</b></td><td>212.20 (-0.28%)</td><td>185.18 (+2.63%)</td><td>188.60 (+6.37%)</td><td>135.60 (-13.35%)</td><td>30.78 <b>(+42.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.35 (n/a)</td><td>2.94 (n/a)</td><td>2.96 (n/a)</td><td>2.46 (n/a)</td><td>0.34 (n/a)</td><td>212.80 (n/a)</td><td>180.44 (n/a)</td><td>177.30 (n/a)</td><td>156.50 (n/a)</td><td>21.66 (n/a)</td>
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
