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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (+12.07%)</td><td>0.07 (-0.75%)</td><td>0.07 (-6.81%)</td><td>0.06 (+5.20%)</td><td>0.01 <b>(+28.70%)</b></td><td>199.70 (-4.95%)</td><td>171.76 (+1.27%)</td><td>170.70 (+7.29%)</td><td>133.30 (-10.78%)</td><td>25.61 (+6.15%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>169.60 (n/a)</td><td>159.10 (n/a)</td><td>149.40 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (-12.11%)</td><td>0.08 (-5.78%)</td><td>0.08 (+1.66%)</td><td>0.06 (+2.48%)</td><td>0.01 <b>(-44.17%)</b></td><td>192.20 (-2.39%)</td><td>163.96 (+4.61%)</td><td>158.80 (-1.67%)</td><td>147.30 (+13.75%)</td><td>17.24 <b>(-36.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>156.74 (n/a)</td><td>161.50 (n/a)</td><td>129.50 (n/a)</td><td>26.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 <b>(-27.84%)</b></td><td>0.07 (-13.20%)</td><td>0.07 (-15.01%)</td><td>0.05 (-16.14%)</td><td>0.01 <b>(-41.44%)</b></td><td>236.50 (+19.26%)</td><td>180.12 (+12.42%)</td><td>182.40 (+17.60%)</td><td>140.80 <b>(+38.58%)</b></td><td>37.48 (-3.65%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>198.30 (n/a)</td><td>160.22 (n/a)</td><td>155.10 (n/a)</td><td>101.60 (n/a)</td><td>38.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (+1.17%)</td><td>0.07 (-8.90%)</td><td>0.06 (-8.75%)</td><td>0.04 <b>(-38.67%)</b></td><td>0.02 <b>(+39.46%)</b></td><td>340.80 <b>(+63.06%)</b></td><td>202.56 (+18.23%)</td><td>189.30 (+9.61%)</td><td>121.40 (-1.22%)</td><td>82.68 <b>(+132.69%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>171.32 (n/a)</td><td>172.70 (n/a)</td><td>122.90 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(+42.72%)</b></td><td>0.04 <b>(+20.39%)</b></td><td>0.04 <b>(+23.14%)</b></td><td>0.02 (-0.94%)</td><td>0.01 <b>(+120.30%)</b></td><td>236.00 (+0.94%)</td><td>162.14 (-11.31%)</td><td>147.10 (-18.77%)</td><td>96.30 <b>(-29.91%)</b></td><td>54.12 <b>(+57.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.80 (n/a)</td><td>182.82 (n/a)</td><td>181.10 (n/a)</td><td>137.40 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (+12.84%)</td><td>0.04 (+19.35%)</td><td>0.04 (+11.25%)</td><td>0.03 <b>(+26.08%)</b></td><td>0.01 (-10.45%)</td><td>192.30 <b>(-20.67%)</b></td><td>141.38 (-17.96%)</td><td>133.30 (-10.11%)</td><td>114.50 (-11.38%)</td><td>29.76 <b>(-35.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.40 (n/a)</td><td>172.34 (n/a)</td><td>148.30 (n/a)</td><td>129.20 (n/a)</td><td>45.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 <b>(+26.66%)</b></td><td>0.03 (+13.77%)</td><td>0.03 (+13.87%)</td><td>0.03 (+3.95%)</td><td>0.01 <b>(+103.35%)</b></td><td>188.10 (-3.79%)</td><td>161.18 (-10.85%)</td><td>166.70 (-12.17%)</td><td>123.50 <b>(-21.04%)</b></td><td>24.61 <b>(+51.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>180.80 (n/a)</td><td>189.80 (n/a)</td><td>156.40 (n/a)</td><td>16.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(+48.29%)</b></td><td>0.03 <b>(+32.78%)</b></td><td>0.04 <b>(+37.33%)</b></td><td>0.02 (+11.27%)</td><td>0.01 <b>(+102.84%)</b></td><td>213.40 (-10.15%)</td><td>157.12 <b>(-22.92%)</b></td><td>147.70 <b>(-27.21%)</b></td><td>114.70 <b>(-32.57%)</b></td><td>35.95 <b>(+24.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.50 (n/a)</td><td>203.84 (n/a)</td><td>202.90 (n/a)</td><td>170.10 (n/a)</td><td>28.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (-8.36%)</td><td>0.03 (+8.38%)</td><td>0.03 (+10.20%)</td><td>0.03 (+10.50%)</td><td>0.00 <b>(-34.31%)</b></td><td>186.70 (-9.50%)</td><td>167.18 (-9.19%)</td><td>179.10 (-9.27%)</td><td>142.40 (+9.12%)</td><td>20.38 <b>(-33.78%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>184.10 (n/a)</td><td>197.40 (n/a)</td><td>130.50 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (-5.88%)</td><td>0.03 (-6.51%)</td><td>0.03 (-7.74%)</td><td>0.02 (-2.51%)</td><td>0.00 (-17.94%)</td><td>219.50 (+2.57%)</td><td>188.82 (+6.40%)</td><td>190.80 (+8.41%)</td><td>155.40 (+6.22%)</td><td>25.06 (-10.44%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.00 (n/a)</td><td>177.46 (n/a)</td><td>176.00 (n/a)</td><td>146.30 (n/a)</td><td>27.98 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (-6.12%)</td><td>0.03 (+5.42%)</td><td>0.03 (+6.36%)</td><td>0.03 (+13.34%)</td><td>0.00 <b>(-63.41%)</b></td><td>187.60 (-11.76%)</td><td>180.26 (-5.87%)</td><td>183.20 (-5.95%)</td><td>171.60 (+6.52%)</td><td>6.82 <b>(-65.29%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>191.50 (n/a)</td><td>194.80 (n/a)</td><td>161.10 (n/a)</td><td>19.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 <b>(+28.26%)</b></td><td>0.03 <b>(+21.81%)</b></td><td>0.03 (+16.22%)</td><td>0.02 <b>(+36.95%)</b></td><td>0.00 (-0.69%)</td><td>233.90 <b>(-26.97%)</b></td><td>200.10 (-18.59%)</td><td>197.00 (-13.94%)</td><td>172.80 <b>(-22.02%)</b></td><td>23.23 <b>(-44.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>320.30 (n/a)</td><td>245.80 (n/a)</td><td>228.90 (n/a)</td><td>221.60 (n/a)</td><td>41.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.70 (n/a)</td><td>154.84 (n/a)</td><td>155.30 (n/a)</td><td>131.80 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>201.10 (n/a)</td><td>172.94 (n/a)</td><td>181.10 (n/a)</td><td>101.10 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>189.40 (n/a)</td><td>151.08 (n/a)</td><td>160.00 (n/a)</td><td>118.70 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>246.10 (n/a)</td><td>164.18 (n/a)</td><td>141.10 (n/a)</td><td>117.70 (n/a)</td><td>51.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.00 (n/a)</td><td>133.80 (n/a)</td><td>127.98 (n/a)</td><td>127.20 (n/a)</td><td>120.60 (n/a)</td><td>5.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>150.18 (n/a)</td><td>151.50 (n/a)</td><td>126.00 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.90 (n/a)</td><td>148.66 (n/a)</td><td>144.60 (n/a)</td><td>99.90 (n/a)</td><td>41.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>189.34 (n/a)</td><td>194.40 (n/a)</td><td>158.90 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.46 (+11.22%)</td><td>3.03 (+2.22%)</td><td>2.92 (-0.34%)</td><td>2.86 (+0.07%)</td><td>0.25 <b>(+154.96%)</b></td><td>481.60 (-0.06%)</td><td>456.50 (-1.79%)</td><td>471.10 (+0.34%)</td><td>397.90 (-10.10%)</td><td>33.86 <b>(+127.71%)</b></td><td>674.55 (+11.22%)</td><td>590.87 (+2.22%)</td><td>569.82 (-0.34%)</td><td>557.43 (+0.07%)</td><td>47.92 <b>(+154.96%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.11 (n/a)</td><td>2.96 (n/a)</td><td>2.93 (n/a)</td><td>2.86 (n/a)</td><td>0.10 (n/a)</td><td>481.90 (n/a)</td><td>464.80 (n/a)</td><td>469.50 (n/a)</td><td>442.60 (n/a)</td><td>14.87 (n/a)</td><td>606.52 (n/a)</td><td>578.01 (n/a)</td><td>571.79 (n/a)</td><td>557.02 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.81 <b>(+24.15%)</b></td><td>3.89 (+5.61%)</td><td>3.76 (+1.24%)</td><td>3.46 (-0.24%)</td><td>0.54 <b>(+187.74%)</b></td><td>398.30 (+0.25%)</td><td>358.44 (-4.21%)</td><td>365.70 (-1.24%)</td><td>286.20 (-19.47%)</td><td>44.17 <b>(+129.58%)</b></td><td>937.85 <b>(+24.15%)</b></td><td>759.22 (+5.61%)</td><td>733.96 (+1.24%)</td><td>673.99 (-0.24%)</td><td>105.50 <b>(+187.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.87 (n/a)</td><td>3.69 (n/a)</td><td>3.72 (n/a)</td><td>3.46 (n/a)</td><td>0.19 (n/a)</td><td>397.30 (n/a)</td><td>374.20 (n/a)</td><td>370.30 (n/a)</td><td>355.40 (n/a)</td><td>19.24 (n/a)</td><td>755.40 (n/a)</td><td>718.89 (n/a)</td><td>725.00 (n/a)</td><td>675.62 (n/a)</td><td>36.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>6.68 (+11.64%)</td><td>4.67 (+15.73%)</td><td>4.17 (+16.03%)</td><td>3.37 (-1.20%)</td><td>1.41 <b>(+28.41%)</b></td><td>407.80 (+1.22%)</td><td>315.22 (-11.60%)</td><td>330.00 (-13.82%)</td><td>205.90 (-10.44%)</td><td>86.67 <b>(+20.19%)</b></td><td>1303.58 (+11.64%)</td><td>911.13 (+15.73%)</td><td>813.42 (+16.03%)</td><td>658.19 (-1.20%)</td><td>274.83 <b>(+28.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.99 (n/a)</td><td>4.04 (n/a)</td><td>3.59 (n/a)</td><td>3.42 (n/a)</td><td>1.10 (n/a)</td><td>402.90 (n/a)</td><td>356.60 (n/a)</td><td>382.90 (n/a)</td><td>229.90 (n/a)</td><td>72.11 (n/a)</td><td>1167.63 (n/a)</td><td>787.28 (n/a)</td><td>701.06 (n/a)</td><td>666.18 (n/a)</td><td>214.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.00 (+10.43%)</td><td>4.94 (+8.13%)</td><td>4.71 (+19.17%)</td><td>3.40 (-4.82%)</td><td>1.81 (+18.04%)</td><td>405.30 (+5.05%)</td><td>303.82 (-5.78%)</td><td>292.10 (-16.09%)</td><td>172.10 (-9.47%)</td><td>89.41 (+11.14%)</td><td>1559.52 (+10.43%)</td><td>964.03 (+8.13%)</td><td>919.09 (+19.17%)</td><td>662.28 (-4.82%)</td><td>353.81 (+18.04%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>7.24 (n/a)</td><td>4.57 (n/a)</td><td>3.95 (n/a)</td><td>3.57 (n/a)</td><td>1.54 (n/a)</td><td>385.80 (n/a)</td><td>322.46 (n/a)</td><td>348.10 (n/a)</td><td>190.10 (n/a)</td><td>80.45 (n/a)</td><td>1412.28 (n/a)</td><td>891.57 (n/a)</td><td>771.23 (n/a)</td><td>695.82 (n/a)</td><td>299.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.56 <b>(+40.32%)</b></td><td>3.59 (+17.45%)</td><td>3.38 (+9.03%)</td><td>2.86 (+7.63%)</td><td>0.64 <b>(+171.32%)</b></td><td>480.40 (-7.10%)</td><td>392.88 (-13.20%)</td><td>407.00 (-8.27%)</td><td>302.00 <b>(-28.72%)</b></td><td>67.02 <b>(+76.26%)</b></td><td>888.99 <b>(+40.33%)</b></td><td>700.23 (+17.45%)</td><td>659.57 (+9.03%)</td><td>558.75 (+7.63%)</td><td>125.60 <b>(+171.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.25 (n/a)</td><td>3.06 (n/a)</td><td>3.10 (n/a)</td><td>2.66 (n/a)</td><td>0.24 (n/a)</td><td>517.10 (n/a)</td><td>452.62 (n/a)</td><td>443.70 (n/a)</td><td>423.70 (n/a)</td><td>38.02 (n/a)</td><td>633.53 (n/a)</td><td>596.17 (n/a)</td><td>604.97 (n/a)</td><td>519.14 (n/a)</td><td>46.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.21 <b>(-27.66%)</b></td><td>1.10 (-3.77%)</td><td>1.09 (+5.85%)</td><td>1.01 (+7.95%)</td><td>0.07 <b>(-75.31%)</b></td><td>397.50 (-7.36%)</td><td>367.26 (-0.08%)</td><td>367.70 (-5.55%)</td><td>332.90 <b>(+38.25%)</b></td><td>24.25 <b>(-67.13%)</b></td><td>100.80 <b>(-27.66%)</b></td><td>91.69 (-3.77%)</td><td>91.24 (+5.85%)</td><td>84.41 (+7.95%)</td><td>6.17 <b>(-75.31%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.67 (n/a)</td><td>1.14 (n/a)</td><td>1.03 (n/a)</td><td>0.94 (n/a)</td><td>0.30 (n/a)</td><td>429.10 (n/a)</td><td>367.56 (n/a)</td><td>389.30 (n/a)</td><td>240.80 (n/a)</td><td>73.78 (n/a)</td><td>139.33 (n/a)</td><td>95.28 (n/a)</td><td>86.20 (n/a)</td><td>78.20 (n/a)</td><td>24.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.03 (+13.76%)</td><td>5.67 (+4.58%)</td><td>5.04 (-0.17%)</td><td>4.64 (+0.52%)</td><td>1.38 <b>(+42.60%)</b></td><td>416.90 (-0.50%)</td><td>354.36 (-2.78%)</td><td>383.40 (+0.18%)</td><td>240.80 (-12.12%)</td><td>69.47 <b>(+24.63%)</b></td><td>1671.95 (+13.76%)</td><td>1180.79 (+4.58%)</td><td>1050.30 (-0.17%)</td><td>965.89 (+0.52%)</td><td>286.38 <b>(+42.60%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>7.06 (n/a)</td><td>5.42 (n/a)</td><td>5.05 (n/a)</td><td>4.61 (n/a)</td><td>0.96 (n/a)</td><td>419.00 (n/a)</td><td>364.50 (n/a)</td><td>382.70 (n/a)</td><td>274.00 (n/a)</td><td>55.74 (n/a)</td><td>1469.75 (n/a)</td><td>1129.10 (n/a)</td><td>1052.06 (n/a)</td><td>960.92 (n/a)</td><td>200.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>16.23 (-5.26%)</td><td>12.59 (+6.34%)</td><td>11.62 (+9.72%)</td><td>10.61 (+6.57%)</td><td>2.30 <b>(-22.79%)</b></td><td>518.70 (-6.17%)</td><td>447.90 (-7.37%)</td><td>473.90 (-8.87%)</td><td>339.30 (+5.57%)</td><td>73.22 <b>(-20.80%)</b></td><td>6329.81 (-5.26%)</td><td>4911.06 (+6.34%)</td><td>4531.59 (+9.72%)</td><td>4140.07 (+6.57%)</td><td>896.96 <b>(-22.79%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>17.13 (n/a)</td><td>11.84 (n/a)</td><td>10.59 (n/a)</td><td>9.96 (n/a)</td><td>2.98 (n/a)</td><td>552.80 (n/a)</td><td>483.56 (n/a)</td><td>520.00 (n/a)</td><td>321.40 (n/a)</td><td>92.45 (n/a)</td><td>6681.43 (n/a)</td><td>4618.16 (n/a)</td><td>4130.17 (n/a)</td><td>3884.72 (n/a)</td><td>1161.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>163.56 (n/a)</td><td>160.90 (n/a)</td><td>136.50 (n/a)</td><td>22.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.30 (n/a)</td><td>155.94 (n/a)</td><td>158.20 (n/a)</td><td>126.20 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>165.40 (n/a)</td><td>170.80 (n/a)</td><td>130.10 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.20 (n/a)</td><td>200.86 (n/a)</td><td>222.30 (n/a)</td><td>153.00 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>167.90 (n/a)</td><td>148.52 (n/a)</td><td>152.10 (n/a)</td><td>122.60 (n/a)</td><td>17.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>160.52 (n/a)</td><td>166.10 (n/a)</td><td>133.40 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>174.40 (n/a)</td><td>180.60 (n/a)</td><td>148.50 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>310.10 (n/a)</td><td>218.76 (n/a)</td><td>201.60 (n/a)</td><td>172.60 (n/a)</td><td>57.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.19 (-10.66%)</td><td>3.98 (+3.59%)</td><td>4.07 (+2.08%)</td><td>3.56 (+12.36%)</td><td>0.24 <b>(-60.55%)</b></td><td>2643.20 (-11.00%)</td><td>2370.60 (-5.13%)</td><td>2312.60 (-2.04%)</td><td>2246.70 (+11.93%)</td><td>156.11 <b>(-60.88%)</b></td><td>1646.60 (-10.66%)</td><td>1565.58 (+3.59%)</td><td>1599.67 (+2.08%)</td><td>1399.60 (+12.36%)</td><td>95.82 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>4.69 (n/a)</td><td>3.84 (n/a)</td><td>3.98 (n/a)</td><td>3.17 (n/a)</td><td>0.62 (n/a)</td><td>2969.90 (n/a)</td><td>2498.68 (n/a)</td><td>2360.70 (n/a)</td><td>2007.20 (n/a)</td><td>399.03 (n/a)</td><td>1843.08 (n/a)</td><td>1511.38 (n/a)</td><td>1567.05 (n/a)</td><td>1245.61 (n/a)</td><td>242.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.98 <b>(-39.95%)</b></td><td>0.82 <b>(-30.49%)</b></td><td>0.79 <b>(-39.77%)</b></td><td>0.65 (-9.45%)</td><td>0.14 <b>(-66.71%)</b></td><td>342.70 (+10.41%)</td><td>274.82 <b>(+31.62%)</b></td><td>279.40 <b>(+66.01%)</b></td><td>226.40 <b>(+66.59%)</b></td><td>47.16 <b>(-41.33%)</b></td><td>41.68 <b>(-39.95%)</b></td><td>35.14 <b>(-30.49%)</b></td><td>33.78 <b>(-39.77%)</b></td><td>27.53 (-9.45%)</td><td>5.85 <b>(-66.71%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.63 (n/a)</td><td>1.18 (n/a)</td><td>1.31 (n/a)</td><td>0.71 (n/a)</td><td>0.41 (n/a)</td><td>310.40 (n/a)</td><td>208.80 (n/a)</td><td>168.30 (n/a)</td><td>135.90 (n/a)</td><td>80.39 (n/a)</td><td>69.42 (n/a)</td><td>50.55 (n/a)</td><td>56.08 (n/a)</td><td>30.41 (n/a)</td><td>17.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.26 (+12.19%)</td><td>0.95 (+5.79%)</td><td>0.94 (+3.17%)</td><td>0.61 (+2.22%)</td><td>0.24 (+17.67%)</td><td>365.20 (-2.17%)</td><td>248.02 (-4.54%)</td><td>235.60 (-3.09%)</td><td>175.10 (-10.89%)</td><td>71.93 (+3.60%)</td><td>53.89 (+12.19%)</td><td>40.37 (+5.79%)</td><td>40.06 (+3.17%)</td><td>25.84 (+2.22%)</td><td>10.32 (+17.67%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.13 (n/a)</td><td>0.89 (n/a)</td><td>0.91 (n/a)</td><td>0.59 (n/a)</td><td>0.21 (n/a)</td><td>373.30 (n/a)</td><td>259.82 (n/a)</td><td>243.10 (n/a)</td><td>196.50 (n/a)</td><td>69.43 (n/a)</td><td>48.04 (n/a)</td><td>38.16 (n/a)</td><td>38.82 (n/a)</td><td>25.28 (n/a)</td><td>8.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.53 (+0.01%)</td><td>0.53 (+0.04%)</td><td>0.53 (+0.03%)</td><td>0.53 (+0.07%)</td><td>0.00 <b>(-43.55%)</b></td><td>47815.90 (-0.07%)</td><td>47802.36 (-0.04%)</td><td>47809.40 (-0.03%)</td><td>47781.20 (-0.01%)</td><td>16.06 <b>(-43.61%)</b></td><td>359.55 (+0.01%)</td><td>359.39 (+0.04%)</td><td>359.34 (+0.03%)</td><td>359.29 (+0.07%)</td><td>0.12 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47850.70 (n/a)</td><td>47820.26 (n/a)</td><td>47823.80 (n/a)</td><td>47785.20 (n/a)</td><td>28.48 (n/a)</td><td>359.52 (n/a)</td><td>359.26 (n/a)</td><td>359.23 (n/a)</td><td>359.03 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.91 (-0.16%)</td><td>0.90 (-0.06%)</td><td>0.90 (+0.24%)</td><td>0.89 (-0.66%)</td><td>0.01 <b>(+47.13%)</b></td><td>28403.80 (+0.67%)</td><td>27951.48 (+0.06%)</td><td>27848.80 (-0.24%)</td><td>27794.60 (+0.16%)</td><td>256.34 <b>(+48.31%)</b></td><td>618.10 (-0.16%)</td><td>614.67 (-0.06%)</td><td>616.90 (+0.24%)</td><td>604.84 (-0.66%)</td><td>5.57 <b>(+47.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28215.50 (n/a)</td><td>27934.44 (n/a)</td><td>27916.00 (n/a)</td><td>27749.60 (n/a)</td><td>172.84 (n/a)</td><td>619.10 (n/a)</td><td>615.03 (n/a)</td><td>615.41 (n/a)</td><td>608.88 (n/a)</td><td>3.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.31 (-0.73%)</td><td>3.19 (-0.33%)</td><td>3.16 (-0.36%)</td><td>3.15 (+1.47%)</td><td>0.07 <b>(-22.03%)</b></td><td>7989.20 (-1.45%)</td><td>7888.22 (+0.31%)</td><td>7959.10 (+0.36%)</td><td>7602.90 (+0.73%)</td><td>161.10 <b>(-22.56%)</b></td><td>2259.65 (-0.73%)</td><td>2178.67 (-0.33%)</td><td>2158.53 (-0.36%)</td><td>2150.39 (+1.47%)</td><td>45.69 <b>(-22.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.33 (n/a)</td><td>3.20 (n/a)</td><td>3.17 (n/a)</td><td>3.10 (n/a)</td><td>0.09 (n/a)</td><td>8106.40 (n/a)</td><td>7863.56 (n/a)</td><td>7930.30 (n/a)</td><td>7547.70 (n/a)</td><td>208.02 (n/a)</td><td>2276.17 (n/a)</td><td>2185.99 (n/a)</td><td>2166.37 (n/a)</td><td>2119.29 (n/a)</td><td>58.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.68 (-11.59%)</td><td>3.40 (-6.32%)</td><td>3.36 (-8.51%)</td><td>3.04 (+0.16%)</td><td>0.28 <b>(-30.48%)</b></td><td>2647.50 (-0.15%)</td><td>2384.20 (+6.23%)</td><td>2397.50 (+9.31%)</td><td>2188.10 (+13.12%)</td><td>199.86 <b>(-23.66%)</b></td><td>966.12 (-11.59%)</td><td>891.61 (-6.32%)</td><td>881.74 (-8.51%)</td><td>798.47 (+0.16%)</td><td>74.14 <b>(-30.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>4.17 (n/a)</td><td>3.63 (n/a)</td><td>3.68 (n/a)</td><td>3.04 (n/a)</td><td>0.41 (n/a)</td><td>2651.60 (n/a)</td><td>2244.40 (n/a)</td><td>2193.30 (n/a)</td><td>1934.40 (n/a)</td><td>261.81 (n/a)</td><td>1092.79 (n/a)</td><td>951.75 (n/a)</td><td>963.80 (n/a)</td><td>797.23 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.50 (-7.95%)</td><td>0.37 (-9.47%)</td><td>0.34 (-3.26%)</td><td>0.32 (-3.23%)</td><td>0.07 <b>(-20.56%)</b></td><td>3883.40 (+3.33%)</td><td>3467.94 (+9.20%)</td><td>3669.80 (+3.37%)</td><td>2510.30 (+8.63%)</td><td>555.72 (-13.72%)</td><td>26.73 (-7.95%)</td><td>19.85 (-9.47%)</td><td>18.29 (-3.26%)</td><td>17.28 (-3.23%)</td><td>3.92 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>3758.20 (n/a)</td><td>3175.66 (n/a)</td><td>3550.30 (n/a)</td><td>2310.80 (n/a)</td><td>644.05 (n/a)</td><td>29.04 (n/a)</td><td>21.93 (n/a)</td><td>18.90 (n/a)</td><td>17.86 (n/a)</td><td>4.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.88 (-4.54%)</td><td>4.29 (+1.18%)</td><td>4.68 (+6.16%)</td><td>3.49 (+2.51%)</td><td>0.69 (-9.50%)</td><td>1908.40 (-2.45%)</td><td>1584.06 (-1.63%)</td><td>1421.60 (-5.80%)</td><td>1361.90 (+4.75%)</td><td>269.84 (-9.36%)</td><td>1509.03 (-4.54%)</td><td>1326.44 (+1.18%)</td><td>1445.73 (+6.16%)</td><td>1076.93 (+2.51%)</td><td>213.06 (-9.50%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.12 (n/a)</td><td>4.24 (n/a)</td><td>4.41 (n/a)</td><td>3.40 (n/a)</td><td>0.76 (n/a)</td><td>1956.40 (n/a)</td><td>1610.32 (n/a)</td><td>1509.10 (n/a)</td><td>1300.10 (n/a)</td><td>297.70 (n/a)</td><td>1580.85 (n/a)</td><td>1310.97 (n/a)</td><td>1361.88 (n/a)</td><td>1050.53 (n/a)</td><td>235.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>13.29 (n/a)</td><td>12.19 (n/a)</td><td>12.18 (n/a)</td><td>10.97 (n/a)</td><td>0.90 (n/a)</td><td>13.28 (n/a)</td><td>12.19 (n/a)</td><td>12.17 (n/a)</td><td>10.97 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>25.17 (+0.87%)</td><td>24.26 (-1.11%)</td><td>24.19 (-2.32%)</td><td>23.20 (-2.92%)</td><td>0.72 <b>(+47.04%)</b></td><td>25.15 (+0.87%)</td><td>24.25 (-1.11%)</td><td>24.18 (-2.32%)</td><td>23.18 (-2.92%)</td><td>0.72 <b>(+47.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>24.95 (n/a)</td><td>24.54 (n/a)</td><td>24.77 (n/a)</td><td>23.90 (n/a)</td><td>0.49 (n/a)</td><td>24.94 (n/a)</td><td>24.52 (n/a)</td><td>24.75 (n/a)</td><td>23.88 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.25 (+2.18%)</td><td>40.48 (+0.30%)</td><td>40.08 (-3.30%)</td><td>38.88 (+9.56%)</td><td>1.66 <b>(-40.86%)</b></td><td>43.22 (+2.18%)</td><td>40.46 (+0.30%)</td><td>40.06 (-3.30%)</td><td>38.85 (+9.56%)</td><td>1.66 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>42.33 (n/a)</td><td>40.36 (n/a)</td><td>41.45 (n/a)</td><td>35.48 (n/a)</td><td>2.80 (n/a)</td><td>42.30 (n/a)</td><td>40.34 (n/a)</td><td>41.42 (n/a)</td><td>35.46 (n/a)</td><td>2.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.51 (-4.54%)</td><td>42.79 (-1.12%)</td><td>42.83 (-0.11%)</td><td>42.04 (+0.10%)</td><td>0.68 <b>(-53.34%)</b></td><td>43.48 (-4.54%)</td><td>42.77 (-1.12%)</td><td>42.80 (-0.11%)</td><td>42.01 (+0.10%)</td><td>0.68 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>45.57 (n/a)</td><td>43.28 (n/a)</td><td>42.88 (n/a)</td><td>42.00 (n/a)</td><td>1.47 (n/a)</td><td>45.55 (n/a)</td><td>43.25 (n/a)</td><td>42.85 (n/a)</td><td>41.97 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>13.38 (n/a)</td><td>12.15 (n/a)</td><td>12.15 (n/a)</td><td>10.90 (n/a)</td><td>0.88 (n/a)</td><td>13.37 (n/a)</td><td>12.14 (n/a)</td><td>12.14 (n/a)</td><td>10.89 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>24.40 (-3.17%)</td><td>23.49 (-3.18%)</td><td>23.82 (-3.63%)</td><td>21.35 (-3.78%)</td><td>1.22 (+1.00%)</td><td>24.39 (-3.17%)</td><td>23.47 (-3.18%)</td><td>23.81 (-3.63%)</td><td>21.34 (-3.78%)</td><td>1.22 (+1.00%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>25.20 (n/a)</td><td>24.26 (n/a)</td><td>24.72 (n/a)</td><td>22.19 (n/a)</td><td>1.21 (n/a)</td><td>25.18 (n/a)</td><td>24.25 (n/a)</td><td>24.70 (n/a)</td><td>22.18 (n/a)</td><td>1.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>39.82 (-6.34%)</td><td>39.50 (-1.52%)</td><td>39.47 (-3.95%)</td><td>39.21 (+13.30%)</td><td>0.25 <b>(-91.99%)</b></td><td>39.80 (-6.34%)</td><td>39.47 (-1.52%)</td><td>39.44 (-3.95%)</td><td>39.19 (+13.30%)</td><td>0.25 <b>(-91.99%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>42.52 (n/a)</td><td>40.10 (n/a)</td><td>41.09 (n/a)</td><td>34.61 (n/a)</td><td>3.17 (n/a)</td><td>42.49 (n/a)</td><td>40.08 (n/a)</td><td>41.06 (n/a)</td><td>34.59 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.22 (-6.71%)</td><td>40.79 (-8.89%)</td><td>40.97 (-10.34%)</td><td>38.04 (-10.55%)</td><td>1.93 (+16.48%)</td><td>43.19 (-6.71%)</td><td>40.76 (-8.89%)</td><td>40.94 (-10.34%)</td><td>38.02 (-10.55%)</td><td>1.93 (+16.48%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>46.32 (n/a)</td><td>44.77 (n/a)</td><td>45.69 (n/a)</td><td>42.53 (n/a)</td><td>1.65 (n/a)</td><td>46.30 (n/a)</td><td>44.74 (n/a)</td><td>45.66 (n/a)</td><td>42.50 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.75 (-6.21%)</td><td>8.65 (+2.91%)</td><td>8.72 (+3.11%)</td><td>8.43 (+7.91%)</td><td>0.13 <b>(-77.81%)</b></td><td>8.73 (-6.21%)</td><td>8.63 (+2.91%)</td><td>8.70 (+3.11%)</td><td>8.41 (+7.91%)</td><td>0.13 <b>(-77.81%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>9.33 (n/a)</td><td>8.41 (n/a)</td><td>8.45 (n/a)</td><td>7.81 (n/a)</td><td>0.61 (n/a)</td><td>9.31 (n/a)</td><td>8.39 (n/a)</td><td>8.44 (n/a)</td><td>7.79 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.03 (+9.16%)</td><td>0.92 (+11.17%)</td><td>0.89 (+10.94%)</td><td>0.79 (+7.79%)</td><td>0.10 <b>(+33.03%)</b></td><td>1.01 (+9.16%)</td><td>0.90 (+11.17%)</td><td>0.87 (+10.94%)</td><td>0.78 (+7.79%)</td><td>0.10 <b>(+33.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.94 (n/a)</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.73 (n/a)</td><td>0.08 (n/a)</td><td>0.93 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.42 (+3.85%)</td><td>1.23 (+14.91%)</td><td>1.32 <b>(+20.26%)</b></td><td>0.92 (+4.60%)</td><td>0.20 (+3.18%)</td><td>1.41 (+3.85%)</td><td>1.22 (+14.91%)</td><td>1.30 <b>(+20.26%)</b></td><td>0.91 (+4.60%)</td><td>0.20 (+3.18%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.37 (n/a)</td><td>1.07 (n/a)</td><td>1.10 (n/a)</td><td>0.88 (n/a)</td><td>0.20 (n/a)</td><td>1.35 (n/a)</td><td>1.06 (n/a)</td><td>1.08 (n/a)</td><td>0.87 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>17.15 (-6.53%)</td><td>15.39 (+0.61%)</td><td>15.43 (+0.31%)</td><td>12.54 (-4.17%)</td><td>1.81 (-16.83%)</td><td>16.95 (-6.53%)</td><td>15.22 (+0.61%)</td><td>15.25 (+0.31%)</td><td>12.39 (-4.17%)</td><td>1.79 (-16.83%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>18.35 (n/a)</td><td>15.30 (n/a)</td><td>15.38 (n/a)</td><td>13.08 (n/a)</td><td>2.18 (n/a)</td><td>18.13 (n/a)</td><td>15.12 (n/a)</td><td>15.20 (n/a)</td><td>12.93 (n/a)</td><td>2.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>14.08 (+0.50%)</td><td>12.24 (-9.24%)</td><td>13.50 (-0.28%)</td><td>7.98 <b>(-36.64%)</b></td><td>2.50 <b>(+363.11%)</b></td><td>13.84 (+0.50%)</td><td>12.03 (-9.24%)</td><td>13.27 (-0.28%)</td><td>7.84 <b>(-36.64%)</b></td><td>2.46 <b>(+363.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>14.01 (n/a)</td><td>13.49 (n/a)</td><td>13.54 (n/a)</td><td>12.60 (n/a)</td><td>0.54 (n/a)</td><td>13.77 (n/a)</td><td>13.25 (n/a)</td><td>13.30 (n/a)</td><td>12.38 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.25 (-2.07%)</td><td>7.74 (+1.90%)</td><td>8.03 (+7.33%)</td><td>7.08 (-0.30%)</td><td>0.57 (+12.35%)</td><td>8.11 (-2.07%)</td><td>7.61 (+1.90%)</td><td>7.89 (+7.33%)</td><td>6.96 (-0.30%)</td><td>0.56 (+12.35%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>8.43 (n/a)</td><td>7.60 (n/a)</td><td>7.48 (n/a)</td><td>7.10 (n/a)</td><td>0.51 (n/a)</td><td>8.28 (n/a)</td><td>7.47 (n/a)</td><td>7.35 (n/a)</td><td>6.98 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>6.49 (+10.77%)</td><td>5.68 (+1.40%)</td><td>5.64 (-2.31%)</td><td>4.71 (-5.67%)</td><td>0.79 <b>(+119.62%)</b></td><td>6.39 (+10.77%)</td><td>5.59 (+1.40%)</td><td>5.55 (-2.31%)</td><td>4.64 (-5.67%)</td><td>0.78 <b>(+119.62%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.86 (n/a)</td><td>5.60 (n/a)</td><td>5.78 (n/a)</td><td>5.00 (n/a)</td><td>0.36 (n/a)</td><td>5.77 (n/a)</td><td>5.51 (n/a)</td><td>5.68 (n/a)</td><td>4.92 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>13.40 (n/a)</td><td>13.12 (n/a)</td><td>13.19 (n/a)</td><td>12.59 (n/a)</td><td>0.31 (n/a)</td><td>13.39 (n/a)</td><td>13.11 (n/a)</td><td>13.18 (n/a)</td><td>12.59 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>13.36 (n/a)</td><td>12.11 (n/a)</td><td>12.36 (n/a)</td><td>10.86 (n/a)</td><td>0.96 (n/a)</td><td>13.35 (n/a)</td><td>12.11 (n/a)</td><td>12.35 (n/a)</td><td>10.85 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>163.96 (n/a)</td><td>164.70 (n/a)</td><td>131.70 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>174.34 (n/a)</td><td>186.60 (n/a)</td><td>122.70 (n/a)</td><td>42.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>154.04 (n/a)</td><td>162.00 (n/a)</td><td>119.20 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>198.14 (n/a)</td><td>202.30 (n/a)</td><td>149.40 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>176.90 (n/a)</td><td>180.00 (n/a)</td><td>157.20 (n/a)</td><td>11.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.40 (n/a)</td><td>202.92 (n/a)</td><td>214.00 (n/a)</td><td>147.00 (n/a)</td><td>53.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>193.02 (n/a)</td><td>192.70 (n/a)</td><td>178.00 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>304.10 (n/a)</td><td>248.44 (n/a)</td><td>227.40 (n/a)</td><td>225.30 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-25.74%)</b></td><td>0.05 (-15.86%)</td><td>0.04 <b>(-24.64%)</b></td><td>0.04 (+9.29%)</td><td>0.00 <b>(-57.54%)</b></td><td>198.40 (-8.49%)</td><td>182.14 (+15.19%)</td><td>191.60 <b>(+32.69%)</b></td><td>159.10 <b>(+34.72%)</b></td><td>19.10 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.80 (n/a)</td><td>158.12 (n/a)</td><td>144.40 (n/a)</td><td>118.10 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 <b>(-21.01%)</b></td><td>0.05 (-11.23%)</td><td>0.04 (-17.35%)</td><td>0.04 (-9.02%)</td><td>0.01 <b>(-30.90%)</b></td><td>217.50 (+9.90%)</td><td>184.90 (+11.26%)</td><td>203.10 <b>(+20.96%)</b></td><td>142.50 <b>(+26.55%)</b></td><td>32.73 (-1.52%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.90 (n/a)</td><td>166.18 (n/a)</td><td>167.90 (n/a)</td><td>112.60 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-20.15%)</b></td><td>0.04 (-14.66%)</td><td>0.04 (-18.85%)</td><td>0.04 (-0.59%)</td><td>0.00 <b>(-60.75%)</b></td><td>204.30 (+0.59%)</td><td>187.00 (+15.28%)</td><td>185.00 <b>(+23.25%)</b></td><td>172.80 <b>(+25.22%)</b></td><td>13.22 <b>(-50.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>162.22 (n/a)</td><td>150.10 (n/a)</td><td>138.00 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-30.60%)</b></td><td>0.04 (-14.51%)</td><td>0.04 (-3.83%)</td><td>0.04 (-13.55%)</td><td>0.01 <b>(-55.93%)</b></td><td>219.30 (+15.66%)</td><td>189.88 (+14.52%)</td><td>182.90 (+3.98%)</td><td>165.60 <b>(+44.13%)</b></td><td>22.53 <b>(-23.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>165.80 (n/a)</td><td>175.90 (n/a)</td><td>114.90 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-14.40%)</td><td>0.05 (-8.24%)</td><td>0.04 (-5.74%)</td><td>0.04 (-9.58%)</td><td>0.01 <b>(-27.85%)</b></td><td>211.10 (+10.58%)</td><td>184.22 (+8.16%)</td><td>186.00 (+6.10%)</td><td>146.90 (+16.87%)</td><td>24.83 (-6.40%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.90 (n/a)</td><td>170.32 (n/a)</td><td>175.30 (n/a)</td><td>125.70 (n/a)</td><td>26.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-20.60%)</b></td><td>0.04 (-9.31%)</td><td>0.04 (-0.02%)</td><td>0.04 (+1.17%)</td><td>0.00 <b>(-61.98%)</b></td><td>203.70 (-1.16%)</td><td>188.58 (+8.11%)</td><td>182.40 (+0.00%)</td><td>172.40 <b>(+25.93%)</b></td><td>14.23 <b>(-51.69%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>174.44 (n/a)</td><td>182.40 (n/a)</td><td>136.90 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-31.72%)</b></td><td>0.04 <b>(-20.01%)</b></td><td>0.04 <b>(-24.27%)</b></td><td>0.04 (+3.32%)</td><td>0.00 <b>(-67.98%)</b></td><td>217.20 (-3.25%)</td><td>192.54 (+18.17%)</td><td>183.50 <b>(+32.01%)</b></td><td>169.20 <b>(+46.37%)</b></td><td>21.54 <b>(-55.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.50 (n/a)</td><td>162.94 (n/a)</td><td>139.00 (n/a)</td><td>115.60 (n/a)</td><td>47.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (-8.79%)</td><td>0.05 (-3.79%)</td><td>0.04 (-1.59%)</td><td>0.04 (-3.04%)</td><td>0.01 <b>(-22.21%)</b></td><td>208.70 (+3.11%)</td><td>180.30 (+3.29%)</td><td>187.70 (+1.62%)</td><td>151.60 (+9.62%)</td><td>23.03 (-12.51%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>174.56 (n/a)</td><td>184.70 (n/a)</td><td>138.30 (n/a)</td><td>26.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (-3.56%)</td><td>0.04 (-13.61%)</td><td>0.04 (-18.77%)</td><td>0.04 (-13.42%)</td><td>0.01 <b>(+21.61%)</b></td><td>223.70 (+15.49%)</td><td>186.02 (+16.60%)</td><td>187.00 <b>(+23.11%)</b></td><td>150.50 (+3.65%)</td><td>27.51 <b>(+41.55%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>159.54 (n/a)</td><td>151.90 (n/a)</td><td>145.20 (n/a)</td><td>19.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (+9.85%)</td><td>0.04 (-1.18%)</td><td>0.04 (+5.07%)</td><td>0.03 <b>(-25.64%)</b></td><td>0.01 <b>(+121.50%)</b></td><td>311.60 <b>(+34.48%)</b></td><td>226.32 (+4.37%)</td><td>217.40 (-4.82%)</td><td>173.50 (-8.97%)</td><td>51.83 <b>(+177.61%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.70 (n/a)</td><td>216.84 (n/a)</td><td>228.40 (n/a)</td><td>190.60 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 <b>(-21.26%)</b></td><td>0.05 (-10.51%)</td><td>0.05 (+4.22%)</td><td>0.04 (+1.83%)</td><td>0.01 <b>(-50.43%)</b></td><td>192.80 (-1.78%)</td><td>166.88 (+7.47%)</td><td>166.90 (-4.03%)</td><td>135.10 <b>(+26.97%)</b></td><td>24.91 <b>(-36.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>196.30 (n/a)</td><td>155.28 (n/a)</td><td>173.90 (n/a)</td><td>106.40 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 <b>(-21.39%)</b></td><td>0.03 (-4.20%)</td><td>0.04 (+8.80%)</td><td>0.02 (+4.59%)</td><td>0.01 <b>(-37.35%)</b></td><td>342.70 (-4.38%)</td><td>253.44 (-0.59%)</td><td>232.40 (-8.07%)</td><td>174.00 <b>(+27.19%)</b></td><td>66.34 (-19.20%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>358.40 (n/a)</td><td>254.94 (n/a)</td><td>252.80 (n/a)</td><td>136.80 (n/a)</td><td>82.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (+13.65%)</td><td>0.04 (-11.91%)</td><td>0.04 (-4.73%)</td><td>0.03 <b>(-41.50%)</b></td><td>0.02 <b>(+80.64%)</b></td><td>324.60 <b>(+70.93%)</b></td><td>207.78 <b>(+23.44%)</b></td><td>197.50 (+5.00%)</td><td>114.40 (-12.07%)</td><td>75.68 <b>(+160.13%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>168.32 (n/a)</td><td>188.10 (n/a)</td><td>130.10 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (+18.15%)</td><td>0.05 (-7.74%)</td><td>0.04 <b>(-20.42%)</b></td><td>0.04 (-13.85%)</td><td>0.01 <b>(+91.35%)</b></td><td>213.40 (+16.04%)</td><td>180.22 (+11.45%)</td><td>189.60 <b>(+25.65%)</b></td><td>122.00 (-15.34%)</td><td>36.00 <b>(+80.78%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>161.70 (n/a)</td><td>150.90 (n/a)</td><td>144.10 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (+13.86%)</td><td>0.05 (-11.68%)</td><td>0.04 <b>(-21.83%)</b></td><td>0.04 (-5.55%)</td><td>0.02 <b>(+33.63%)</b></td><td>217.50 (+5.84%)</td><td>182.96 (+16.17%)</td><td>196.90 <b>(+27.86%)</b></td><td>108.00 (-12.20%)</td><td>44.52 <b>(+24.52%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>157.50 (n/a)</td><td>154.00 (n/a)</td><td>123.00 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-7.11%)</td><td>0.05 (-16.42%)</td><td>0.04 (-17.91%)</td><td>0.04 <b>(-20.68%)</b></td><td>0.01 <b>(+48.77%)</b></td><td>203.30 <b>(+26.12%)</b></td><td>184.32 <b>(+21.15%)</b></td><td>191.70 <b>(+21.79%)</b></td><td>139.40 (+7.64%)</td><td>25.71 <b>(+100.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>161.20 (n/a)</td><td>152.14 (n/a)</td><td>157.40 (n/a)</td><td>129.50 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 <b>(+23.99%)</b></td><td>0.04 (-3.03%)</td><td>0.04 (-16.91%)</td><td>0.04 (+16.43%)</td><td>0.01 <b>(+37.85%)</b></td><td>226.60 (-14.10%)</td><td>195.18 (+4.12%)</td><td>209.00 <b>(+20.39%)</b></td><td>124.30 (-19.39%)</td><td>40.89 (-9.02%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.80 (n/a)</td><td>187.46 (n/a)</td><td>173.60 (n/a)</td><td>154.20 (n/a)</td><td>44.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-0.66%)</td><td>0.04 (+2.78%)</td><td>0.04 (+2.05%)</td><td>0.04 (+17.10%)</td><td>0.01 (-17.18%)</td><td>219.00 (-14.62%)</td><td>191.94 (-4.82%)</td><td>198.80 (-2.02%)</td><td>134.30 (+0.67%)</td><td>34.24 <b>(-30.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.50 (n/a)</td><td>201.66 (n/a)</td><td>202.90 (n/a)</td><td>133.40 (n/a)</td><td>49.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52388.40 (n/a)</td><td>52233.84 (n/a)</td><td>52207.30 (n/a)</td><td>52164.90 (n/a)</td><td>92.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.15 <b>(-31.22%)</b></td><td>0.14 (-14.67%)</td><td>0.14 (-4.35%)</td><td>0.13 (+8.80%)</td><td>0.01 <b>(-81.66%)</b></td><td>187.50 (-8.09%)</td><td>172.04 (+11.63%)</td><td>172.50 (+4.55%)</td><td>162.80 <b>(+45.36%)</b></td><td>9.71 <b>(-74.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>204.00 (n/a)</td><td>154.12 (n/a)</td><td>165.00 (n/a)</td><td>112.00 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.29 (-10.52%)</td><td>0.26 (-4.75%)</td><td>0.25 (-4.64%)</td><td>0.24 (+12.29%)</td><td>0.02 <b>(-59.34%)</b></td><td>170.30 (-10.98%)</td><td>161.06 (+2.10%)</td><td>164.80 (+4.83%)</td><td>138.90 (+11.84%)</td><td>12.59 <b>(-60.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>191.30 (n/a)</td><td>157.74 (n/a)</td><td>157.20 (n/a)</td><td>124.20 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (+6.56%)</td><td>0.03 (+10.40%)</td><td>0.04 (+13.47%)</td><td>0.03 <b>(+28.86%)</b></td><td>0.00 <b>(-24.70%)</b></td><td>174.60 <b>(-22.37%)</b></td><td>149.26 (-11.09%)</td><td>144.30 (-11.85%)</td><td>126.10 (-6.18%)</td><td>19.51 <b>(-45.08%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>167.88 (n/a)</td><td>163.70 (n/a)</td><td>134.40 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 <b>(-23.91%)</b></td><td>0.05 (+8.12%)</td><td>0.05 <b>(+22.73%)</b></td><td>0.04 <b>(+20.36%)</b></td><td>0.01 <b>(-51.90%)</b></td><td>201.90 (-16.91%)</td><td>161.38 (-13.25%)</td><td>160.50 (-18.53%)</td><td>134.20 <b>(+31.44%)</b></td><td>28.60 <b>(-45.57%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>186.02 (n/a)</td><td>197.00 (n/a)</td><td>102.10 (n/a)</td><td>52.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (-3.69%)</td><td>0.07 (-9.51%)</td><td>0.06 <b>(-24.40%)</b></td><td>0.06 (+6.39%)</td><td>0.01 (-12.70%)</td><td>202.10 (-6.00%)</td><td>174.36 (+9.50%)</td><td>191.70 <b>(+32.30%)</b></td><td>131.30 (+3.79%)</td><td>30.19 (-15.36%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>159.24 (n/a)</td><td>144.90 (n/a)</td><td>126.50 (n/a)</td><td>35.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-16.07%)</td><td>0.05 (-1.20%)</td><td>0.05 (+1.75%)</td><td>0.04 <b>(+68.48%)</b></td><td>0.00 <b>(-69.17%)</b></td><td>185.00 <b>(-40.65%)</b></td><td>162.74 (-8.46%)</td><td>153.60 (-1.73%)</td><td>148.70 (+19.15%)</td><td>16.13 <b>(-79.01%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>311.70 (n/a)</td><td>177.78 (n/a)</td><td>156.30 (n/a)</td><td>124.80 (n/a)</td><td>76.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (-4.78%)</td><td>0.06 (-1.58%)</td><td>0.07 (+1.84%)</td><td>0.04 (-18.42%)</td><td>0.01 <b>(+20.58%)</b></td><td>246.70 <b>(+22.55%)</b></td><td>175.16 (+3.24%)</td><td>156.80 (-1.82%)</td><td>150.60 (+5.02%)</td><td>40.66 <b>(+55.92%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>169.66 (n/a)</td><td>159.70 (n/a)</td><td>143.40 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 <b>(-20.96%)</b></td><td>0.05 (-18.84%)</td><td>0.04 <b>(-25.68%)</b></td><td>0.04 (-8.62%)</td><td>0.01 <b>(-26.30%)</b></td><td>218.90 (+9.45%)</td><td>182.94 <b>(+22.03%)</b></td><td>197.80 <b>(+34.56%)</b></td><td>140.20 <b>(+26.53%)</b></td><td>34.33 (+0.84%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>149.92 (n/a)</td><td>147.00 (n/a)</td><td>110.80 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (+17.69%)</td><td>0.07 (+5.11%)</td><td>0.07 (+15.14%)</td><td>0.04 <b>(-21.42%)</b></td><td>0.02 <b>(+38.10%)</b></td><td>270.30 <b>(+27.26%)</b></td><td>167.84 (+0.00%)</td><td>142.70 (-13.15%)</td><td>106.40 (-15.08%)</td><td>63.80 <b>(+53.63%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>167.84 (n/a)</td><td>164.30 (n/a)</td><td>125.30 (n/a)</td><td>41.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-5.16%)</td><td>0.04 (-14.68%)</td><td>0.04 <b>(-23.71%)</b></td><td>0.03 (-0.91%)</td><td>0.01 <b>(-21.81%)</b></td><td>240.00 (+0.88%)</td><td>198.10 (+15.08%)</td><td>201.40 <b>(+31.03%)</b></td><td>140.30 (+5.49%)</td><td>37.15 (-18.25%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.90 (n/a)</td><td>172.14 (n/a)</td><td>153.70 (n/a)</td><td>133.00 (n/a)</td><td>45.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 <b>(+32.08%)</b></td><td>0.06 (+11.83%)</td><td>0.06 (+12.92%)</td><td>0.04 (-1.37%)</td><td>0.02 <b>(+86.63%)</b></td><td>216.50 (+1.36%)</td><td>169.42 (-7.37%)</td><td>166.20 (-11.41%)</td><td>109.90 <b>(-24.26%)</b></td><td>42.51 <b>(+42.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>182.90 (n/a)</td><td>187.60 (n/a)</td><td>145.10 (n/a)</td><td>29.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (+15.63%)</td><td>0.05 (-3.55%)</td><td>0.05 (-19.37%)</td><td>0.04 (+2.27%)</td><td>0.01 <b>(+21.38%)</b></td><td>219.70 (-2.18%)</td><td>168.96 (+4.91%)</td><td>174.00 <b>(+24.02%)</b></td><td>112.00 (-13.51%)</td><td>43.07 (+4.43%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.60 (n/a)</td><td>161.06 (n/a)</td><td>140.30 (n/a)</td><td>129.50 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (-2.22%)</td><td>0.05 (-10.87%)</td><td>0.05 (-10.71%)</td><td>0.03 <b>(-25.88%)</b></td><td>0.01 <b>(+40.73%)</b></td><td>274.00 <b>(+34.91%)</b></td><td>188.14 (+16.81%)</td><td>177.00 (+11.95%)</td><td>128.50 (+2.23%)</td><td>55.54 <b>(+96.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.10 (n/a)</td><td>161.06 (n/a)</td><td>158.10 (n/a)</td><td>125.70 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 <b>(+34.87%)</b></td><td>0.05 (+5.46%)</td><td>0.05 (+2.86%)</td><td>0.03 (-19.13%)</td><td>0.01 <b>(+211.02%)</b></td><td>282.90 <b>(+23.65%)</b></td><td>194.54 (+1.45%)</td><td>182.00 (-2.78%)</td><td>129.60 <b>(-25.86%)</b></td><td>61.32 <b>(+182.43%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>191.76 (n/a)</td><td>187.20 (n/a)</td><td>174.80 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (-0.64%)</td><td>0.05 (+4.87%)</td><td>0.05 (+8.56%)</td><td>0.04 (+0.12%)</td><td>0.00 (-4.95%)</td><td>209.90 (-0.14%)</td><td>185.62 (-4.68%)</td><td>181.60 (-7.86%)</td><td>168.50 (+0.66%)</td><td>15.95 (-2.23%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.20 (n/a)</td><td>194.74 (n/a)</td><td>197.10 (n/a)</td><td>167.40 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (-19.12%)</td><td>0.04 (-8.08%)</td><td>0.04 (+1.08%)</td><td>0.03 (-8.60%)</td><td>0.01 <b>(-35.02%)</b></td><td>242.70 (+9.42%)</td><td>194.32 (+7.79%)</td><td>184.30 (-1.07%)</td><td>171.90 <b>(+23.67%)</b></td><td>27.81 (-8.29%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>180.28 (n/a)</td><td>186.30 (n/a)</td><td>139.00 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (-4.84%)</td><td>0.04 (-2.70%)</td><td>0.04 (-7.24%)</td><td>0.03 (-2.28%)</td><td>0.01 (-1.63%)</td><td>293.60 (+2.34%)</td><td>212.90 (+2.93%)</td><td>208.50 (+7.81%)</td><td>155.60 (+5.06%)</td><td>53.29 (+4.35%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>286.90 (n/a)</td><td>206.84 (n/a)</td><td>193.40 (n/a)</td><td>148.10 (n/a)</td><td>51.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 <b>(+44.47%)</b></td><td>0.05 <b>(+26.12%)</b></td><td>0.04 (+6.23%)</td><td>0.04 <b>(+50.91%)</b></td><td>0.01 <b>(+62.35%)</b></td><td>217.10 <b>(-33.75%)</b></td><td>187.36 <b>(-20.01%)</b></td><td>213.80 (-5.90%)</td><td>122.20 <b>(-30.76%)</b></td><td>42.23 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>327.70 (n/a)</td><td>234.24 (n/a)</td><td>227.20 (n/a)</td><td>176.50 (n/a)</td><td>57.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.90 <b>(+24.62%)</b></td><td>0.68 (+17.65%)</td><td>0.70 <b>(+32.07%)</b></td><td>0.50 (+3.72%)</td><td>0.16 <b>(+62.98%)</b></td><td>197.30 (-3.57%)</td><td>152.18 (-13.00%)</td><td>141.00 <b>(-24.27%)</b></td><td>109.40 (-19.79%)</td><td>35.89 <b>(+29.64%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.72 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.10 (n/a)</td><td>204.60 (n/a)</td><td>174.92 (n/a)</td><td>186.20 (n/a)</td><td>136.40 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.66 (-18.76%)</td><td>0.58 (-5.61%)</td><td>0.57 (-6.80%)</td><td>0.48 (+3.25%)</td><td>0.07 <b>(-42.95%)</b></td><td>203.90 (-3.14%)</td><td>171.18 (+3.82%)</td><td>172.40 (+7.28%)</td><td>149.30 <b>(+23.08%)</b></td><td>22.28 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.81 (n/a)</td><td>0.62 (n/a)</td><td>0.61 (n/a)</td><td>0.47 (n/a)</td><td>0.13 (n/a)</td><td>210.50 (n/a)</td><td>164.88 (n/a)</td><td>160.70 (n/a)</td><td>121.30 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.80 <b>(+21.90%)</b></td><td>0.62 (+5.17%)</td><td>0.60 (-0.42%)</td><td>0.50 (+0.54%)</td><td>0.12 <b>(+101.07%)</b></td><td>196.70 (-0.56%)</td><td>162.32 (-3.05%)</td><td>164.80 (+0.43%)</td><td>123.20 (-17.98%)</td><td>29.55 <b>(+61.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.65 (n/a)</td><td>0.59 (n/a)</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.06 (n/a)</td><td>197.80 (n/a)</td><td>167.42 (n/a)</td><td>164.10 (n/a)</td><td>150.20 (n/a)</td><td>18.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.64 <b>(+20.10%)</b></td><td>0.47 (+0.40%)</td><td>0.49 (+4.30%)</td><td>0.33 (-16.07%)</td><td>0.12 <b>(+148.04%)</b></td><td>293.50 (+19.16%)</td><td>221.28 (+4.18%)</td><td>202.20 (-4.13%)</td><td>154.40 (-16.72%)</td><td>57.07 <b>(+150.53%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.05 (n/a)</td><td>246.30 (n/a)</td><td>212.40 (n/a)</td><td>210.90 (n/a)</td><td>185.40 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.57 (+18.06%)</td><td>0.45 (+6.42%)</td><td>0.43 (-3.22%)</td><td>0.37 (+12.96%)</td><td>0.07 <b>(+29.42%)</b></td><td>197.40 (-11.48%)</td><td>167.14 (-5.74%)</td><td>173.40 (+3.34%)</td><td>129.30 (-15.27%)</td><td>24.91 (-8.04%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>223.00 (n/a)</td><td>177.32 (n/a)</td><td>167.80 (n/a)</td><td>152.60 (n/a)</td><td>27.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.53 (+14.00%)</td><td>0.43 (+13.34%)</td><td>0.43 (+19.99%)</td><td>0.38 (+18.11%)</td><td>0.06 (-0.76%)</td><td>194.30 (-15.34%)</td><td>173.04 (-12.20%)</td><td>172.00 (-16.63%)</td><td>139.90 (-12.29%)</td><td>21.46 <b>(-26.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.46 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>229.50 (n/a)</td><td>197.08 (n/a)</td><td>206.30 (n/a)</td><td>159.50 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.45 (-11.77%)</td><td>0.39 (-0.15%)</td><td>0.39 (+8.11%)</td><td>0.33 (+4.43%)</td><td>0.04 <b>(-46.23%)</b></td><td>221.40 (-4.24%)</td><td>191.30 (-2.04%)</td><td>190.10 (-7.49%)</td><td>164.70 (+13.27%)</td><td>21.63 <b>(-42.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>231.20 (n/a)</td><td>195.28 (n/a)</td><td>205.50 (n/a)</td><td>145.40 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.43 (+10.26%)</td><td>0.38 (+7.67%)</td><td>0.38 (+7.43%)</td><td>0.34 (+7.31%)</td><td>0.03 <b>(+25.66%)</b></td><td>215.30 (-6.84%)</td><td>193.44 (-6.99%)</td><td>192.30 (-6.92%)</td><td>171.20 (-9.27%)</td><td>16.18 (+5.13%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>231.10 (n/a)</td><td>207.98 (n/a)</td><td>206.60 (n/a)</td><td>188.70 (n/a)</td><td>15.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.16 (+19.06%)</td><td>0.91 (+16.32%)</td><td>0.82 (-5.09%)</td><td>0.74 <b>(+30.70%)</b></td><td>0.18 (+0.30%)</td><td>177.40 <b>(-23.50%)</b></td><td>148.32 (-15.54%)</td><td>160.50 (+5.38%)</td><td>113.20 (-16.02%)</td><td>28.14 <b>(-36.86%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.97 (n/a)</td><td>0.78 (n/a)</td><td>0.86 (n/a)</td><td>0.57 (n/a)</td><td>0.18 (n/a)</td><td>231.90 (n/a)</td><td>175.60 (n/a)</td><td>152.30 (n/a)</td><td>134.80 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.20 <b>(+31.27%)</b></td><td>0.88 (+9.51%)</td><td>0.80 (+0.51%)</td><td>0.72 (+0.19%)</td><td>0.19 <b>(+140.98%)</b></td><td>180.80 (-0.22%)</td><td>152.92 (-6.55%)</td><td>164.00 (-0.49%)</td><td>109.10 <b>(-23.87%)</b></td><td>27.38 <b>(+77.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.08 (n/a)</td><td>181.20 (n/a)</td><td>163.64 (n/a)</td><td>164.80 (n/a)</td><td>143.30 (n/a)</td><td>15.42 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 (+16.06%)</td><td>0.88 (+7.66%)</td><td>0.85 (-4.72%)</td><td>0.71 (+7.80%)</td><td>0.13 (+7.65%)</td><td>183.80 (-7.22%)</td><td>151.16 (-7.22%)</td><td>154.40 (+4.96%)</td><td>123.00 (-13.81%)</td><td>22.46 (-12.81%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.92 (n/a)</td><td>0.82 (n/a)</td><td>0.89 (n/a)</td><td>0.66 (n/a)</td><td>0.12 (n/a)</td><td>198.10 (n/a)</td><td>162.92 (n/a)</td><td>147.10 (n/a)</td><td>142.70 (n/a)</td><td>25.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 <b>(+36.52%)</b></td><td>0.03 (+18.32%)</td><td>0.03 (+8.08%)</td><td>0.02 (+0.71%)</td><td>0.01 <b>(+223.36%)</b></td><td>184.60 (-0.70%)</td><td>149.76 (-12.92%)</td><td>157.10 (-7.48%)</td><td>116.10 <b>(-26.70%)</b></td><td>30.36 <b>(+127.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.90 (n/a)</td><td>171.98 (n/a)</td><td>169.80 (n/a)</td><td>158.40 (n/a)</td><td>13.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 <b>(+22.62%)</b></td><td>0.03 (+8.94%)</td><td>0.02 (-4.52%)</td><td>0.02 (+5.11%)</td><td>0.01 <b>(+77.00%)</b></td><td>191.00 (-4.83%)</td><td>163.52 (-6.42%)</td><td>182.00 (+4.72%)</td><td>120.40 (-18.43%)</td><td>31.23 <b>(+38.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.70 (n/a)</td><td>174.74 (n/a)</td><td>173.80 (n/a)</td><td>147.60 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (+2.46%)</td><td>0.02 <b>(+20.79%)</b></td><td>0.02 (+12.70%)</td><td>0.02 <b>(+73.24%)</b></td><td>0.00 <b>(-55.04%)</b></td><td>214.00 <b>(-42.29%)</b></td><td>188.26 <b>(-26.21%)</b></td><td>188.20 (-11.27%)</td><td>151.40 (-2.39%)</td><td>24.65 <b>(-76.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.80 (n/a)</td><td>255.12 (n/a)</td><td>212.10 (n/a)</td><td>155.10 (n/a)</td><td>103.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.05 (+5.32%)</td><td>0.84 (-6.06%)</td><td>0.72 <b>(-21.68%)</b></td><td>0.67 (-9.53%)</td><td>0.19 <b>(+79.18%)</b></td><td>196.70 (+10.51%)</td><td>163.46 (+9.31%)</td><td>183.30 <b>(+27.65%)</b></td><td>125.90 (-5.05%)</td><td>34.32 <b>(+82.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.11 (n/a)</td><td>178.00 (n/a)</td><td>149.54 (n/a)</td><td>143.60 (n/a)</td><td>132.60 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.10 (+16.71%)</td><td>0.87 (+8.87%)</td><td>0.82 (-8.01%)</td><td>0.53 (-13.01%)</td><td>0.24 <b>(+42.29%)</b></td><td>247.50 (+14.96%)</td><td>163.20 (-5.16%)</td><td>160.30 (+8.68%)</td><td>119.60 (-14.33%)</td><td>52.23 <b>(+33.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.95 (n/a)</td><td>0.80 (n/a)</td><td>0.90 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>215.30 (n/a)</td><td>172.08 (n/a)</td><td>147.50 (n/a)</td><td>139.60 (n/a)</td><td>39.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.03 <b>(+20.38%)</b></td><td>0.84 <b>(+28.47%)</b></td><td>0.84 <b>(+37.33%)</b></td><td>0.67 <b>(+30.17%)</b></td><td>0.13 (-4.57%)</td><td>195.70 <b>(-23.19%)</b></td><td>160.98 <b>(-23.25%)</b></td><td>157.00 <b>(-27.18%)</b></td><td>128.70 (-16.91%)</td><td>25.27 <b>(-39.38%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.85 (n/a)</td><td>0.65 (n/a)</td><td>0.61 (n/a)</td><td>0.52 (n/a)</td><td>0.14 (n/a)</td><td>254.80 (n/a)</td><td>209.74 (n/a)</td><td>215.60 (n/a)</td><td>154.90 (n/a)</td><td>41.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 <b>(+20.40%)</b></td><td>0.85 (+10.97%)</td><td>0.77 (-0.19%)</td><td>0.69 (+7.57%)</td><td>0.18 <b>(+101.14%)</b></td><td>192.80 (-7.04%)</td><td>161.28 (-7.70%)</td><td>170.60 (+0.18%)</td><td>123.50 (-16.95%)</td><td>32.99 <b>(+53.73%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.89 (n/a)</td><td>0.76 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.09 (n/a)</td><td>207.40 (n/a)</td><td>174.74 (n/a)</td><td>170.30 (n/a)</td><td>148.70 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 (+10.35%)</td><td>0.85 (-0.76%)</td><td>0.81 (-9.00%)</td><td>0.61 (-1.97%)</td><td>0.20 <b>(+42.66%)</b></td><td>216.20 (+2.03%)</td><td>161.62 (+2.69%)</td><td>163.50 (+9.88%)</td><td>123.30 (-9.34%)</td><td>38.54 <b>(+23.95%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.97 (n/a)</td><td>0.86 (n/a)</td><td>0.89 (n/a)</td><td>0.62 (n/a)</td><td>0.14 (n/a)</td><td>211.90 (n/a)</td><td>157.38 (n/a)</td><td>148.80 (n/a)</td><td>136.00 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (+18.43%)</td><td>0.02 (-0.57%)</td><td>0.02 (-9.87%)</td><td>0.02 (+0.45%)</td><td>0.01 <b>(+83.55%)</b></td><td>209.50 (-0.48%)</td><td>186.38 (+3.17%)</td><td>205.30 (+10.91%)</td><td>123.90 (-15.60%)</td><td>36.17 <b>(+54.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.50 (n/a)</td><td>180.66 (n/a)</td><td>185.10 (n/a)</td><td>146.80 (n/a)</td><td>23.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 <b>(+42.79%)</b></td><td>0.03 <b>(+25.77%)</b></td><td>0.03 (+17.81%)</td><td>0.02 <b>(+26.74%)</b></td><td>0.00 <b>(+63.28%)</b></td><td>173.60 <b>(-21.09%)</b></td><td>155.04 <b>(-20.12%)</b></td><td>158.10 (-15.09%)</td><td>121.20 <b>(-29.94%)</b></td><td>20.08 (-12.69%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>220.00 (n/a)</td><td>194.08 (n/a)</td><td>186.20 (n/a)</td><td>173.00 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>1049.74 (-0.24%)</td><td>979.63 (-0.33%)</td><td>970.56 (+0.12%)</td><td>950.28 (-0.86%)</td><td>40.95 (+4.71%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1052.30 (n/a)</td><td>982.88 (n/a)</td><td>969.44 (n/a)</td><td>958.54 (n/a)</td><td>39.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.01 (-1.16%)</td><td>0.01 (+0.50%)</td><td>0.01 (+1.25%)</td><td>0.01 (-1.33%)</td><td>0.00 (-11.84%)</td><td>1112.29 (+1.74%)</td><td>1022.18 (-0.67%)</td><td>1007.63 (-1.53%)</td><td>961.58 (+1.33%)</td><td>55.30 (-8.20%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1093.24 (n/a)</td><td>1029.03 (n/a)</td><td>1023.25 (n/a)</td><td>948.98 (n/a)</td><td>60.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.96 (-1.67%)</td><td>0.95 (-1.20%)</td><td>0.96 (-0.87%)</td><td>0.95 (-1.00%)</td><td>0.01 <b>(-24.24%)</b></td><td>2217.39 (+1.01%)</td><td>2198.61 (+1.21%)</td><td>2195.36 (+0.88%)</td><td>2176.79 (+1.71%)</td><td>15.66 <b>(-22.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2195.14 (n/a)</td><td>2172.30 (n/a)</td><td>2176.20 (n/a)</td><td>2140.29 (n/a)</td><td>20.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.59 (+0.74%)</td><td>2.87 (-2.00%)</td><td>2.80 (-6.31%)</td><td>2.48 (+9.98%)</td><td>0.43 (-8.89%)</td><td>211.50 (-9.07%)</td><td>185.56 (+1.44%)</td><td>187.10 (+6.73%)</td><td>145.90 (-0.68%)</td><td>24.73 <b>(-21.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.57 (n/a)</td><td>2.93 (n/a)</td><td>2.99 (n/a)</td><td>2.25 (n/a)</td><td>0.47 (n/a)</td><td>232.60 (n/a)</td><td>182.92 (n/a)</td><td>175.30 (n/a)</td><td>146.90 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>5.25 (-2.35%)</td><td>4.62 (+1.82%)</td><td>4.62 (+0.99%)</td><td>4.13 (+1.89%)</td><td>0.42 <b>(-21.69%)</b></td><td>253.90 (-1.86%)</td><td>228.32 (-2.18%)</td><td>226.90 (-1.00%)</td><td>199.70 (+2.41%)</td><td>20.00 <b>(-21.98%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.38 (n/a)</td><td>4.54 (n/a)</td><td>4.58 (n/a)</td><td>4.05 (n/a)</td><td>0.53 (n/a)</td><td>258.70 (n/a)</td><td>233.40 (n/a)</td><td>229.20 (n/a)</td><td>195.00 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.30 (+7.52%)</td><td>2.53 (-8.81%)</td><td>2.57 (-9.44%)</td><td>1.82 (-17.44%)</td><td>0.60 <b>(+79.59%)</b></td><td>287.50 <b>(+21.10%)</b></td><td>217.02 (+13.30%)</td><td>204.10 (+10.44%)</td><td>158.90 (-6.97%)</td><td>52.38 <b>(+98.63%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.07 (n/a)</td><td>2.77 (n/a)</td><td>2.84 (n/a)</td><td>2.21 (n/a)</td><td>0.33 (n/a)</td><td>237.40 (n/a)</td><td>191.54 (n/a)</td><td>184.80 (n/a)</td><td>170.80 (n/a)</td><td>26.37 (n/a)</td>
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
