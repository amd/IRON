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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.12 <b>(+27.85%)</b></td><td>0.08 (+7.65%)</td><td>0.07 (-1.70%)</td><td>0.06 (-0.87%)</td><td>0.02 <b>(+88.41%)</b></td><td>201.50 (+0.90%)</td><td>164.68 (-4.12%)</td><td>173.70 (+1.76%)</td><td>104.20 <b>(-21.83%)</b></td><td>36.30 <b>(+41.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>171.76 (n/a)</td><td>170.70 (n/a)</td><td>133.30 (n/a)</td><td>25.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.09 (+3.45%)</td><td>0.07 (-3.73%)</td><td>0.07 (-9.63%)</td><td>0.07 (+4.31%)</td><td>0.01 (+5.69%)</td><td>184.20 (-4.16%)</td><td>170.32 (+3.88%)</td><td>175.80 (+10.71%)</td><td>142.40 (-3.33%)</td><td>16.25 (-5.75%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.20 (n/a)</td><td>163.96 (n/a)</td><td>158.80 (n/a)</td><td>147.30 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.11 <b>(+21.96%)</b></td><td>0.08 (+10.12%)</td><td>0.07 (+10.38%)</td><td>0.06 <b>(+24.52%)</b></td><td>0.02 <b>(+20.94%)</b></td><td>189.90 (-19.70%)</td><td>163.36 (-9.30%)</td><td>165.30 (-9.37%)</td><td>115.50 (-17.97%)</td><td>29.46 <b>(-21.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.50 (n/a)</td><td>180.12 (n/a)</td><td>182.40 (n/a)</td><td>140.80 (n/a)</td><td>37.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(-34.46%)</b></td><td>0.06 (-15.08%)</td><td>0.06 (-13.02%)</td><td>0.05 <b>(+42.38%)</b></td><td>0.01 <b>(-71.84%)</b></td><td>239.30 <b>(-29.78%)</b></td><td>215.44 (+6.36%)</td><td>217.60 (+14.95%)</td><td>185.30 <b>(+52.64%)</b></td><td>24.14 <b>(-70.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>340.80 (n/a)</td><td>202.56 (n/a)</td><td>189.30 (n/a)</td><td>121.40 (n/a)</td><td>82.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 <b>(-21.17%)</b></td><td>0.03 (-5.12%)</td><td>0.03 (-11.19%)</td><td>0.03 (+17.90%)</td><td>0.01 <b>(-42.28%)</b></td><td>200.20 (-15.17%)</td><td>161.14 (-0.62%)</td><td>165.60 (+12.58%)</td><td>122.10 <b>(+26.79%)</b></td><td>33.17 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.00 (n/a)</td><td>162.14 (n/a)</td><td>147.10 (n/a)</td><td>96.30 (n/a)</td><td>54.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (+9.66%)</td><td>0.04 (+0.99%)</td><td>0.04 (-4.64%)</td><td>0.03 (+16.63%)</td><td>0.01 (+2.50%)</td><td>164.90 (-14.25%)</td><td>139.02 (-1.67%)</td><td>139.80 (+4.88%)</td><td>104.40 (-8.82%)</td><td>22.13 <b>(-25.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>141.38 (n/a)</td><td>133.30 (n/a)</td><td>114.50 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (+0.02%)</td><td>0.03 (-0.08%)</td><td>0.03 (+1.92%)</td><td>0.03 (-0.83%)</td><td>0.01 (-2.59%)</td><td>189.70 (+0.85%)</td><td>161.10 (-0.05%)</td><td>163.50 (-1.92%)</td><td>123.50 (+0.00%)</td><td>23.80 (-3.28%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>161.18 (n/a)</td><td>166.70 (n/a)</td><td>123.50 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 <b>(-21.51%)</b></td><td>0.03 (-13.64%)</td><td>0.03 <b>(-20.70%)</b></td><td>0.03 (+10.10%)</td><td>0.00 <b>(-52.21%)</b></td><td>193.80 (-9.18%)</td><td>176.72 (+12.47%)</td><td>186.30 <b>(+26.13%)</b></td><td>146.10 <b>(+27.38%)</b></td><td>19.53 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>157.12 (n/a)</td><td>147.70 (n/a)</td><td>114.70 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-5.62%)</td><td>0.03 (-12.62%)</td><td>0.03 (-10.10%)</td><td>0.02 <b>(-21.91%)</b></td><td>0.00 (+19.35%)</td><td>239.10 <b>(+28.07%)</b></td><td>193.50 (+15.74%)</td><td>199.20 (+11.22%)</td><td>150.90 (+5.97%)</td><td>32.97 <b>(+61.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>167.18 (n/a)</td><td>179.10 (n/a)</td><td>142.40 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (+7.99%)</td><td>0.03 (-1.62%)</td><td>0.03 (-1.45%)</td><td>0.02 (-10.13%)</td><td>0.01 <b>(+50.42%)</b></td><td>244.20 (+11.25%)</td><td>195.58 (+3.58%)</td><td>193.60 (+1.47%)</td><td>143.90 (-7.40%)</td><td>38.88 <b>(+55.13%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>188.82 (n/a)</td><td>190.80 (n/a)</td><td>155.40 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 <b>(+22.70%)</b></td><td>0.03 (+19.05%)</td><td>0.04 <b>(+26.42%)</b></td><td>0.03 (+3.62%)</td><td>0.00 <b>(+206.51%)</b></td><td>181.10 (-3.46%)</td><td>152.56 (-15.37%)</td><td>144.90 <b>(-20.91%)</b></td><td>139.90 (-18.47%)</td><td>16.71 <b>(+145.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.60 (n/a)</td><td>180.26 (n/a)</td><td>183.20 (n/a)</td><td>171.60 (n/a)</td><td>6.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-6.36%)</td><td>0.03 (+2.52%)</td><td>0.03 (+5.33%)</td><td>0.02 (+4.60%)</td><td>0.00 <b>(-30.70%)</b></td><td>223.60 (-4.40%)</td><td>194.12 (-2.99%)</td><td>187.00 (-5.08%)</td><td>184.50 (+6.77%)</td><td>16.54 <b>(-28.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.90 (n/a)</td><td>200.10 (n/a)</td><td>197.00 (n/a)</td><td>172.80 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>149.54 (n/a)</td><td>155.60 (n/a)</td><td>122.90 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>195.70 (n/a)</td><td>141.44 (n/a)</td><td>130.00 (n/a)</td><td>123.50 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>183.10 (n/a)</td><td>167.10 (n/a)</td><td>157.30 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>170.68 (n/a)</td><td>171.80 (n/a)</td><td>131.70 (n/a)</td><td>23.62 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>179.40 (n/a)</td><td>165.30 (n/a)</td><td>151.30 (n/a)</td><td>29.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>269.70 (n/a)</td><td>172.08 (n/a)</td><td>150.30 (n/a)</td><td>120.50 (n/a)</td><td>57.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>164.06 (n/a)</td><td>161.20 (n/a)</td><td>134.30 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>304.00 (n/a)</td><td>189.62 (n/a)</td><td>162.40 (n/a)</td><td>145.70 (n/a)</td><td>64.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.86 (+11.75%)</td><td>3.25 (+7.16%)</td><td>3.21 (+9.79%)</td><td>2.87 (+0.36%)</td><td>0.38 <b>(+54.40%)</b></td><td>479.90 (-0.35%)</td><td>428.28 (-6.18%)</td><td>429.10 (-8.92%)</td><td>356.10 (-10.51%)</td><td>46.43 <b>(+37.15%)</b></td><td>753.78 (+11.75%)</td><td>633.18 (+7.16%)</td><td>625.58 (+9.79%)</td><td>559.41 (+0.36%)</td><td>73.99 <b>(+54.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.46 (n/a)</td><td>3.03 (n/a)</td><td>2.92 (n/a)</td><td>2.86 (n/a)</td><td>0.25 (n/a)</td><td>481.60 (n/a)</td><td>456.50 (n/a)</td><td>471.10 (n/a)</td><td>397.90 (n/a)</td><td>33.86 (n/a)</td><td>674.55 (n/a)</td><td>590.87 (n/a)</td><td>569.82 (n/a)</td><td>557.43 (n/a)</td><td>47.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.68 <b>(-23.46%)</b></td><td>3.48 (-10.59%)</td><td>3.55 (-5.78%)</td><td>3.16 (-8.60%)</td><td>0.20 <b>(-63.77%)</b></td><td>435.80 (+9.42%)</td><td>396.54 (+10.63%)</td><td>388.20 (+6.15%)</td><td>374.00 <b>(+30.68%)</b></td><td>23.48 <b>(-46.84%)</b></td><td>717.82 <b>(-23.46%)</b></td><td>678.80 (-10.59%)</td><td>691.54 (-5.78%)</td><td>616.00 (-8.60%)</td><td>38.22 <b>(-63.77%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.81 (n/a)</td><td>3.89 (n/a)</td><td>3.76 (n/a)</td><td>3.46 (n/a)</td><td>0.54 (n/a)</td><td>398.30 (n/a)</td><td>358.44 (n/a)</td><td>365.70 (n/a)</td><td>286.20 (n/a)</td><td>44.17 (n/a)</td><td>937.85 (n/a)</td><td>759.22 (n/a)</td><td>733.96 (n/a)</td><td>673.99 (n/a)</td><td>105.50 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.83 (-12.82%)</td><td>3.98 (-14.88%)</td><td>3.49 (-16.31%)</td><td>3.31 (-1.90%)</td><td>1.05 <b>(-25.41%)</b></td><td>415.70 (+1.94%)</td><td>361.42 (+14.66%)</td><td>394.30 (+19.48%)</td><td>236.20 (+14.72%)</td><td>72.86 (-15.93%)</td><td>1136.43 (-12.82%)</td><td>775.59 (-14.88%)</td><td>680.72 (-16.31%)</td><td>645.68 (-1.90%)</td><td>205.00 <b>(-25.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>6.68 (n/a)</td><td>4.67 (n/a)</td><td>4.17 (n/a)</td><td>3.37 (n/a)</td><td>1.41 (n/a)</td><td>407.80 (n/a)</td><td>315.22 (n/a)</td><td>330.00 (n/a)</td><td>205.90 (n/a)</td><td>86.67 (n/a)</td><td>1303.58 (n/a)</td><td>911.13 (n/a)</td><td>813.42 (n/a)</td><td>658.19 (n/a)</td><td>274.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.62 <b>(-29.70%)</b></td><td>4.93 (-0.26%)</td><td>5.02 (+6.45%)</td><td>3.81 (+12.33%)</td><td>0.71 <b>(-60.74%)</b></td><td>360.80 (-10.98%)</td><td>284.50 (-6.36%)</td><td>274.40 (-6.06%)</td><td>244.90 <b>(+42.30%)</b></td><td>46.18 <b>(-48.35%)</b></td><td>1096.30 <b>(-29.70%)</b></td><td>961.52 (-0.26%)</td><td>978.40 (+6.45%)</td><td>743.95 (+12.33%)</td><td>138.91 <b>(-60.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.00 (n/a)</td><td>4.94 (n/a)</td><td>4.71 (n/a)</td><td>3.40 (n/a)</td><td>1.81 (n/a)</td><td>405.30 (n/a)</td><td>303.82 (n/a)</td><td>292.10 (n/a)</td><td>172.10 (n/a)</td><td>89.41 (n/a)</td><td>1559.52 (n/a)</td><td>964.03 (n/a)</td><td>919.09 (n/a)</td><td>662.28 (n/a)</td><td>353.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.56 <b>(-21.94%)</b></td><td>3.25 (-9.58%)</td><td>3.15 (-6.86%)</td><td>2.99 (+4.27%)</td><td>0.27 <b>(-57.99%)</b></td><td>460.80 (-4.08%)</td><td>426.28 (+8.50%)</td><td>437.00 (+7.37%)</td><td>386.80 <b>(+28.08%)</b></td><td>34.88 <b>(-47.95%)</b></td><td>693.93 <b>(-21.94%)</b></td><td>633.16 (-9.58%)</td><td>614.31 (-6.86%)</td><td>582.60 (+4.27%)</td><td>52.77 <b>(-57.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.56 (n/a)</td><td>3.59 (n/a)</td><td>3.38 (n/a)</td><td>2.86 (n/a)</td><td>0.64 (n/a)</td><td>480.40 (n/a)</td><td>392.88 (n/a)</td><td>407.00 (n/a)</td><td>302.00 (n/a)</td><td>67.02 (n/a)</td><td>888.99 (n/a)</td><td>700.23 (n/a)</td><td>659.57 (n/a)</td><td>558.75 (n/a)</td><td>125.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.24 (+2.71%)</td><td>1.11 (+1.21%)</td><td>1.04 (-4.55%)</td><td>1.02 (+0.95%)</td><td>0.11 <b>(+46.64%)</b></td><td>393.80 (-0.93%)</td><td>364.30 (-0.81%)</td><td>385.30 (+4.79%)</td><td>324.10 (-2.64%)</td><td>34.33 <b>(+41.56%)</b></td><td>103.53 (+2.71%)</td><td>92.79 (+1.21%)</td><td>87.09 (-4.55%)</td><td>85.21 (+0.95%)</td><td>9.05 <b>(+46.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.21 (n/a)</td><td>1.10 (n/a)</td><td>1.09 (n/a)</td><td>1.01 (n/a)</td><td>0.07 (n/a)</td><td>397.50 (n/a)</td><td>367.26 (n/a)</td><td>367.70 (n/a)</td><td>332.90 (n/a)</td><td>24.25 (n/a)</td><td>100.80 (n/a)</td><td>91.69 (n/a)</td><td>91.24 (n/a)</td><td>84.41 (n/a)</td><td>6.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>6.68 (-16.85%)</td><td>5.29 (-6.61%)</td><td>4.88 (-3.19%)</td><td>4.77 (+2.91%)</td><td>0.80 <b>(-41.93%)</b></td><td>405.10 (-2.83%)</td><td>370.92 (+4.67%)</td><td>396.00 (+3.29%)</td><td>289.60 <b>(+20.27%)</b></td><td>48.05 <b>(-30.83%)</b></td><td>1390.28 (-16.85%)</td><td>1102.75 (-6.61%)</td><td>1016.82 (-3.19%)</td><td>994.03 (+2.91%)</td><td>166.30 <b>(-41.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.03 (n/a)</td><td>5.67 (n/a)</td><td>5.04 (n/a)</td><td>4.64 (n/a)</td><td>1.38 (n/a)</td><td>416.90 (n/a)</td><td>354.36 (n/a)</td><td>383.40 (n/a)</td><td>240.80 (n/a)</td><td>69.47 (n/a)</td><td>1671.95 (n/a)</td><td>1180.79 (n/a)</td><td>1050.30 (n/a)</td><td>965.89 (n/a)</td><td>286.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>15.05 (-7.27%)</td><td>12.59 (+0.00%)</td><td>12.17 (+4.80%)</td><td>11.06 (+4.26%)</td><td>1.65 <b>(-28.35%)</b></td><td>497.50 (-4.09%)</td><td>442.98 (-1.10%)</td><td>452.20 (-4.58%)</td><td>365.80 (+7.81%)</td><td>54.79 <b>(-25.17%)</b></td><td>5869.91 (-7.27%)</td><td>4911.19 (+0.00%)</td><td>4749.17 (+4.80%)</td><td>4316.32 (+4.26%)</td><td>642.63 <b>(-28.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>16.23 (n/a)</td><td>12.59 (n/a)</td><td>11.62 (n/a)</td><td>10.61 (n/a)</td><td>2.30 (n/a)</td><td>518.70 (n/a)</td><td>447.90 (n/a)</td><td>473.90 (n/a)</td><td>339.30 (n/a)</td><td>73.22 (n/a)</td><td>6329.81 (n/a)</td><td>4911.06 (n/a)</td><td>4531.59 (n/a)</td><td>4140.07 (n/a)</td><td>896.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.80 (n/a)</td><td>145.82 (n/a)</td><td>142.90 (n/a)</td><td>121.80 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>148.58 (n/a)</td><td>154.20 (n/a)</td><td>126.50 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.90 (n/a)</td><td>178.50 (n/a)</td><td>156.00 (n/a)</td><td>129.60 (n/a)</td><td>65.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>173.06 (n/a)</td><td>179.20 (n/a)</td><td>127.80 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>155.46 (n/a)</td><td>158.80 (n/a)</td><td>117.10 (n/a)</td><td>28.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>176.08 (n/a)</td><td>189.80 (n/a)</td><td>135.80 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>167.46 (n/a)</td><td>161.60 (n/a)</td><td>114.40 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.80 (n/a)</td><td>210.32 (n/a)</td><td>211.80 (n/a)</td><td>171.30 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>4.09 (-2.24%)</td><td>3.89 (-2.17%)</td><td>4.04 (-0.63%)</td><td>3.51 (-1.31%)</td><td>0.25 (+4.03%)</td><td>2678.20 (+1.32%)</td><td>2423.84 (+2.25%)</td><td>2327.30 (+0.64%)</td><td>2298.20 (+2.29%)</td><td>164.99 (+5.69%)</td><td>1609.68 (-2.24%)</td><td>1531.67 (-2.17%)</td><td>1589.54 (-0.63%)</td><td>1381.29 (-1.31%)</td><td>99.68 (+4.03%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.19 (n/a)</td><td>3.98 (n/a)</td><td>4.07 (n/a)</td><td>3.56 (n/a)</td><td>0.24 (n/a)</td><td>2643.20 (n/a)</td><td>2370.60 (n/a)</td><td>2312.60 (n/a)</td><td>2246.70 (n/a)</td><td>156.11 (n/a)</td><td>1646.60 (n/a)</td><td>1565.58 (n/a)</td><td>1599.67 (n/a)</td><td>1399.60 (n/a)</td><td>95.82 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.61 <b>(+64.40%)</b></td><td>1.08 <b>(+31.47%)</b></td><td>1.03 <b>(+29.48%)</b></td><td>0.78 <b>(+21.38%)</b></td><td>0.31 <b>(+125.91%)</b></td><td>282.40 (-17.60%)</td><td>215.82 <b>(-21.47%)</b></td><td>215.80 <b>(-22.76%)</b></td><td>137.70 <b>(-39.18%)</b></td><td>51.79 (+9.80%)</td><td>68.53 <b>(+64.40%)</b></td><td>46.19 <b>(+31.47%)</b></td><td>43.74 <b>(+29.48%)</b></td><td>33.42 <b>(+21.38%)</b></td><td>13.21 <b>(+125.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.98 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.65 (n/a)</td><td>0.14 (n/a)</td><td>342.70 (n/a)</td><td>274.82 (n/a)</td><td>279.40 (n/a)</td><td>226.40 (n/a)</td><td>47.16 (n/a)</td><td>41.68 (n/a)</td><td>35.14 (n/a)</td><td>33.78 (n/a)</td><td>27.53 (n/a)</td><td>5.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.07 (-15.34%)</td><td>0.86 (-9.40%)</td><td>0.92 (-1.57%)</td><td>0.63 (+4.55%)</td><td>0.17 <b>(-28.65%)</b></td><td>349.30 (-4.35%)</td><td>267.12 (+7.70%)</td><td>239.40 (+1.61%)</td><td>206.80 (+18.10%)</td><td>57.16 <b>(-20.53%)</b></td><td>45.63 (-15.34%)</td><td>36.57 (-9.40%)</td><td>39.43 (-1.57%)</td><td>27.02 (+4.55%)</td><td>7.36 <b>(-28.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.26 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.61 (n/a)</td><td>0.24 (n/a)</td><td>365.20 (n/a)</td><td>248.02 (n/a)</td><td>235.60 (n/a)</td><td>175.10 (n/a)</td><td>71.93 (n/a)</td><td>53.89 (n/a)</td><td>40.37 (n/a)</td><td>40.06 (n/a)</td><td>25.84 (n/a)</td><td>10.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.53 (+0.05%)</td><td>0.53 (-0.05%)</td><td>0.53 (-0.01%)</td><td>0.53 (-0.16%)</td><td>0.00 <b>(+234.29%)</b></td><td>47892.30 (+0.16%)</td><td>47824.48 (+0.05%)</td><td>47814.10 (+0.01%)</td><td>47758.10 (-0.05%)</td><td>53.78 <b>(+234.82%)</b></td><td>359.73 (+0.05%)</td><td>359.23 (-0.05%)</td><td>359.31 (-0.01%)</td><td>358.72 (-0.16%)</td><td>0.40 <b>(+234.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47815.90 (n/a)</td><td>47802.36 (n/a)</td><td>47809.40 (n/a)</td><td>47781.20 (n/a)</td><td>16.06 (n/a)</td><td>359.55 (n/a)</td><td>359.39 (n/a)</td><td>359.34 (n/a)</td><td>359.29 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.91 (+0.05%)</td><td>0.90 (+0.08%)</td><td>0.90 (-0.52%)</td><td>0.90 (+1.29%)</td><td>0.00 <b>(-48.75%)</b></td><td>28040.80 (-1.28%)</td><td>27927.42 (-0.09%)</td><td>27995.20 (+0.53%)</td><td>27780.70 (-0.05%)</td><td>129.46 <b>(-49.50%)</b></td><td>618.41 (+0.05%)</td><td>615.17 (+0.08%)</td><td>613.67 (-0.52%)</td><td>612.68 (+1.29%)</td><td>2.86 <b>(-48.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28403.80 (n/a)</td><td>27951.48 (n/a)</td><td>27848.80 (n/a)</td><td>27794.60 (n/a)</td><td>256.34 (n/a)</td><td>618.10 (n/a)</td><td>614.67 (n/a)</td><td>616.90 (n/a)</td><td>604.84 (n/a)</td><td>5.57 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.32 (+0.36%)</td><td>3.20 (+0.15%)</td><td>3.18 (+0.65%)</td><td>3.13 (-0.64%)</td><td>0.07 (+10.33%)</td><td>8040.30 (+0.64%)</td><td>7877.10 (-0.14%)</td><td>7908.00 (-0.64%)</td><td>7575.30 (-0.36%)</td><td>177.82 (+10.38%)</td><td>2267.88 (+0.36%)</td><td>2181.91 (+0.15%)</td><td>2172.47 (+0.65%)</td><td>2136.73 (-0.64%)</td><td>50.41 (+10.33%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.31 (n/a)</td><td>3.19 (n/a)</td><td>3.16 (n/a)</td><td>3.15 (n/a)</td><td>0.07 (n/a)</td><td>7989.20 (n/a)</td><td>7888.22 (n/a)</td><td>7959.10 (n/a)</td><td>7602.90 (n/a)</td><td>161.10 (n/a)</td><td>2259.65 (n/a)</td><td>2178.67 (n/a)</td><td>2158.53 (n/a)</td><td>2150.39 (n/a)</td><td>45.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.88 (+5.40%)</td><td>3.58 (+5.16%)</td><td>3.83 (+14.04%)</td><td>2.92 (-4.03%)</td><td>0.42 <b>(+47.93%)</b></td><td>2758.60 (+4.20%)</td><td>2282.02 (-4.29%)</td><td>2102.20 (-12.32%)</td><td>2076.00 (-5.12%)</td><td>294.56 <b>(+47.38%)</b></td><td>1018.25 (+5.40%)</td><td>937.63 (+5.16%)</td><td>1005.57 (+14.04%)</td><td>766.31 (-4.03%)</td><td>109.68 <b>(+47.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.68 (n/a)</td><td>3.40 (n/a)</td><td>3.36 (n/a)</td><td>3.04 (n/a)</td><td>0.28 (n/a)</td><td>2647.50 (n/a)</td><td>2384.20 (n/a)</td><td>2397.50 (n/a)</td><td>2188.10 (n/a)</td><td>199.86 (n/a)</td><td>966.12 (n/a)</td><td>891.61 (n/a)</td><td>881.74 (n/a)</td><td>798.47 (n/a)</td><td>74.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.48 (-3.96%)</td><td>0.35 (-3.70%)</td><td>0.32 (-4.58%)</td><td>0.32 (-0.93%)</td><td>0.07 (-6.01%)</td><td>3919.90 (+0.94%)</td><td>3595.82 (+3.69%)</td><td>3846.10 (+4.80%)</td><td>2613.70 (+4.12%)</td><td>553.90 (-0.33%)</td><td>25.68 (-3.96%)</td><td>19.12 (-3.70%)</td><td>17.45 (-4.58%)</td><td>17.12 (-0.93%)</td><td>3.68 (-6.01%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>3883.40 (n/a)</td><td>3467.94 (n/a)</td><td>3669.80 (n/a)</td><td>2510.30 (n/a)</td><td>555.72 (n/a)</td><td>26.73 (n/a)</td><td>19.85 (n/a)</td><td>18.29 (n/a)</td><td>17.28 (n/a)</td><td>3.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>4.96 (+1.61%)</td><td>3.92 (-8.65%)</td><td>3.60 <b>(-22.98%)</b></td><td>3.14 (-9.81%)</td><td>0.86 <b>(+24.83%)</b></td><td>2116.00 (+10.88%)</td><td>1760.48 (+11.14%)</td><td>1845.60 <b>(+29.83%)</b></td><td>1340.30 (-1.59%)</td><td>367.62 <b>(+36.24%)</b></td><td>1533.38 (+1.61%)</td><td>1211.67 (-8.65%)</td><td>1113.56 <b>(-22.98%)</b></td><td>971.27 (-9.81%)</td><td>265.96 <b>(+24.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>4.88 (n/a)</td><td>4.29 (n/a)</td><td>4.68 (n/a)</td><td>3.49 (n/a)</td><td>0.69 (n/a)</td><td>1908.40 (n/a)</td><td>1584.06 (n/a)</td><td>1421.60 (n/a)</td><td>1361.90 (n/a)</td><td>269.84 (n/a)</td><td>1509.03 (n/a)</td><td>1326.44 (n/a)</td><td>1445.73 (n/a)</td><td>1076.93 (n/a)</td><td>213.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>13.40 (n/a)</td><td>12.78 (n/a)</td><td>13.16 (n/a)</td><td>12.01 (n/a)</td><td>0.67 (n/a)</td><td>13.39 (n/a)</td><td>12.77 (n/a)</td><td>13.15 (n/a)</td><td>12.00 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>25.41 (+0.95%)</td><td>24.78 (+2.14%)</td><td>24.63 (+1.79%)</td><td>24.20 (+4.32%)</td><td>0.49 <b>(-31.50%)</b></td><td>25.39 (+0.95%)</td><td>24.77 (+2.14%)</td><td>24.61 (+1.79%)</td><td>24.19 (+4.32%)</td><td>0.49 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>25.17 (n/a)</td><td>24.26 (n/a)</td><td>24.19 (n/a)</td><td>23.20 (n/a)</td><td>0.72 (n/a)</td><td>25.15 (n/a)</td><td>24.25 (n/a)</td><td>24.18 (n/a)</td><td>23.18 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>41.16 (-4.84%)</td><td>39.87 (-1.50%)</td><td>39.77 (-0.79%)</td><td>38.60 (-0.71%)</td><td>0.98 <b>(-41.03%)</b></td><td>41.13 (-4.84%)</td><td>39.85 (-1.50%)</td><td>39.74 (-0.79%)</td><td>38.58 (-0.71%)</td><td>0.98 <b>(-41.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.25 (n/a)</td><td>40.48 (n/a)</td><td>40.08 (n/a)</td><td>38.88 (n/a)</td><td>1.66 (n/a)</td><td>43.22 (n/a)</td><td>40.46 (n/a)</td><td>40.06 (n/a)</td><td>38.85 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>47.01 (+8.06%)</td><td>44.58 (+4.18%)</td><td>45.38 (+5.95%)</td><td>42.50 (+1.09%)</td><td>2.01 <b>(+193.32%)</b></td><td>46.98 (+8.06%)</td><td>44.56 (+4.18%)</td><td>45.35 (+5.95%)</td><td>42.47 (+1.09%)</td><td>2.00 <b>(+193.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.51 (n/a)</td><td>42.79 (n/a)</td><td>42.83 (n/a)</td><td>42.04 (n/a)</td><td>0.68 (n/a)</td><td>43.48 (n/a)</td><td>42.77 (n/a)</td><td>42.80 (n/a)</td><td>42.01 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>13.49 (n/a)</td><td>12.02 (n/a)</td><td>12.48 (n/a)</td><td>10.64 (n/a)</td><td>1.25 (n/a)</td><td>13.48 (n/a)</td><td>12.01 (n/a)</td><td>12.47 (n/a)</td><td>10.63 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>24.39 (-0.05%)</td><td>22.50 (-4.19%)</td><td>23.96 (+0.57%)</td><td>17.47 (-18.20%)</td><td>2.90 <b>(+137.64%)</b></td><td>24.37 (-0.05%)</td><td>22.49 (-4.19%)</td><td>23.94 (+0.57%)</td><td>17.46 (-18.20%)</td><td>2.90 <b>(+137.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>24.40 (n/a)</td><td>23.49 (n/a)</td><td>23.82 (n/a)</td><td>21.35 (n/a)</td><td>1.22 (n/a)</td><td>24.39 (n/a)</td><td>23.47 (n/a)</td><td>23.81 (n/a)</td><td>21.34 (n/a)</td><td>1.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>40.89 (+2.68%)</td><td>38.51 (-2.49%)</td><td>38.88 (-1.49%)</td><td>34.09 (-13.07%)</td><td>2.63 <b>(+935.92%)</b></td><td>40.87 (+2.68%)</td><td>38.49 (-2.49%)</td><td>38.85 (-1.49%)</td><td>34.07 (-13.07%)</td><td>2.62 <b>(+935.94%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>39.82 (n/a)</td><td>39.50 (n/a)</td><td>39.47 (n/a)</td><td>39.21 (n/a)</td><td>0.25 (n/a)</td><td>39.80 (n/a)</td><td>39.47 (n/a)</td><td>39.44 (n/a)</td><td>39.19 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>45.34 (+4.92%)</td><td>43.68 (+7.09%)</td><td>44.06 (+7.56%)</td><td>40.40 (+6.19%)</td><td>2.04 (+5.73%)</td><td>45.31 (+4.92%)</td><td>43.65 (+7.09%)</td><td>44.04 (+7.56%)</td><td>40.37 (+6.19%)</td><td>2.04 (+5.73%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>43.22 (n/a)</td><td>40.79 (n/a)</td><td>40.97 (n/a)</td><td>38.04 (n/a)</td><td>1.93 (n/a)</td><td>43.19 (n/a)</td><td>40.76 (n/a)</td><td>40.94 (n/a)</td><td>38.02 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>9.84 (+12.40%)</td><td>9.03 (+4.44%)</td><td>8.81 (+1.05%)</td><td>8.47 (+0.47%)</td><td>0.56 <b>(+318.45%)</b></td><td>9.82 (+12.40%)</td><td>9.02 (+4.44%)</td><td>8.79 (+1.05%)</td><td>8.45 (+0.47%)</td><td>0.56 <b>(+318.45%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.75 (n/a)</td><td>8.65 (n/a)</td><td>8.72 (n/a)</td><td>8.43 (n/a)</td><td>0.13 (n/a)</td><td>8.73 (n/a)</td><td>8.63 (n/a)</td><td>8.70 (n/a)</td><td>8.41 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.96 (-6.27%)</td><td>0.87 (-4.74%)</td><td>0.86 (-2.43%)</td><td>0.82 (+3.61%)</td><td>0.06 <b>(-46.79%)</b></td><td>0.95 (-6.27%)</td><td>0.86 (-4.74%)</td><td>0.85 (-2.43%)</td><td>0.81 (+3.61%)</td><td>0.05 <b>(-46.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.03 (n/a)</td><td>0.92 (n/a)</td><td>0.89 (n/a)</td><td>0.79 (n/a)</td><td>0.10 (n/a)</td><td>1.01 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.21 (-14.65%)</td><td>1.08 (-11.92%)</td><td>1.11 (-15.85%)</td><td>0.90 (-2.62%)</td><td>0.12 <b>(-42.68%)</b></td><td>1.20 (-14.65%)</td><td>1.07 (-11.92%)</td><td>1.10 (-15.85%)</td><td>0.89 (-2.62%)</td><td>0.11 <b>(-42.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.42 (n/a)</td><td>1.23 (n/a)</td><td>1.32 (n/a)</td><td>0.92 (n/a)</td><td>0.20 (n/a)</td><td>1.41 (n/a)</td><td>1.22 (n/a)</td><td>1.30 (n/a)</td><td>0.91 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>17.69 (+3.14%)</td><td>15.42 (+0.16%)</td><td>15.45 (+0.12%)</td><td>13.38 (+6.73%)</td><td>1.65 (-8.86%)</td><td>17.48 (+3.14%)</td><td>15.24 (+0.16%)</td><td>15.27 (+0.12%)</td><td>13.23 (+6.73%)</td><td>1.63 (-8.86%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>17.15 (n/a)</td><td>15.39 (n/a)</td><td>15.43 (n/a)</td><td>12.54 (n/a)</td><td>1.81 (n/a)</td><td>16.95 (n/a)</td><td>15.22 (n/a)</td><td>15.25 (n/a)</td><td>12.39 (n/a)</td><td>1.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>13.21 (-6.19%)</td><td>12.65 (+3.31%)</td><td>12.50 (-7.45%)</td><td>11.95 <b>(+49.71%)</b></td><td>0.53 <b>(-78.89%)</b></td><td>12.98 (-6.19%)</td><td>12.43 (+3.31%)</td><td>12.28 (-7.45%)</td><td>11.74 <b>(+49.71%)</b></td><td>0.52 <b>(-78.89%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>14.08 (n/a)</td><td>12.24 (n/a)</td><td>13.50 (n/a)</td><td>7.98 (n/a)</td><td>2.50 (n/a)</td><td>13.84 (n/a)</td><td>12.03 (n/a)</td><td>13.27 (n/a)</td><td>7.84 (n/a)</td><td>2.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>8.86 (+7.35%)</td><td>7.82 (+1.00%)</td><td>7.47 (-7.04%)</td><td>7.16 (+1.05%)</td><td>0.79 <b>(+37.31%)</b></td><td>8.71 (+7.35%)</td><td>7.69 (+1.00%)</td><td>7.34 (-7.04%)</td><td>7.03 (+1.05%)</td><td>0.77 <b>(+37.31%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>8.25 (n/a)</td><td>7.74 (n/a)</td><td>8.03 (n/a)</td><td>7.08 (n/a)</td><td>0.57 (n/a)</td><td>8.11 (n/a)</td><td>7.61 (n/a)</td><td>7.89 (n/a)</td><td>6.96 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>7.03 (+8.32%)</td><td>5.71 (+0.63%)</td><td>5.61 (-0.51%)</td><td>4.49 (-4.66%)</td><td>0.91 (+14.65%)</td><td>6.92 (+8.32%)</td><td>5.62 (+0.63%)</td><td>5.52 (-0.51%)</td><td>4.42 (-4.66%)</td><td>0.90 (+14.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>6.49 (n/a)</td><td>5.68 (n/a)</td><td>5.64 (n/a)</td><td>4.71 (n/a)</td><td>0.79 (n/a)</td><td>6.39 (n/a)</td><td>5.59 (n/a)</td><td>5.55 (n/a)</td><td>4.64 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>12.96 (n/a)</td><td>12.59 (n/a)</td><td>12.64 (n/a)</td><td>12.11 (n/a)</td><td>0.37 (n/a)</td><td>12.96 (n/a)</td><td>12.59 (n/a)</td><td>12.64 (n/a)</td><td>12.10 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>13.39 (n/a)</td><td>12.77 (n/a)</td><td>13.01 (n/a)</td><td>11.26 (n/a)</td><td>0.86 (n/a)</td><td>13.38 (n/a)</td><td>12.77 (n/a)</td><td>13.00 (n/a)</td><td>11.25 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.30 (n/a)</td><td>151.22 (n/a)</td><td>146.00 (n/a)</td><td>124.00 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>164.96 (n/a)</td><td>171.20 (n/a)</td><td>108.40 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>164.04 (n/a)</td><td>163.70 (n/a)</td><td>143.00 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.50 (n/a)</td><td>170.42 (n/a)</td><td>176.50 (n/a)</td><td>123.80 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>170.54 (n/a)</td><td>182.40 (n/a)</td><td>120.10 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.10 (n/a)</td><td>162.42 (n/a)</td><td>172.80 (n/a)</td><td>110.20 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.90 (n/a)</td><td>216.72 (n/a)</td><td>207.40 (n/a)</td><td>182.90 (n/a)</td><td>35.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>204.36 (n/a)</td><td>215.40 (n/a)</td><td>167.20 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (+8.71%)</td><td>0.04 (-6.76%)</td><td>0.04 (-7.48%)</td><td>0.04 (-10.53%)</td><td>0.01 <b>(+58.36%)</b></td><td>221.70 (+11.74%)</td><td>198.00 (+8.71%)</td><td>207.10 (+8.09%)</td><td>146.30 (-8.05%)</td><td>30.36 <b>(+58.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>182.14 (n/a)</td><td>191.60 (n/a)</td><td>159.10 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (-7.84%)</td><td>0.05 (+3.91%)</td><td>0.05 (+14.86%)</td><td>0.04 (+17.90%)</td><td>0.00 <b>(-59.86%)</b></td><td>184.50 (-15.17%)</td><td>173.90 (-5.95%)</td><td>176.80 (-12.95%)</td><td>154.70 (+8.56%)</td><td>12.11 <b>(-63.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>184.90 (n/a)</td><td>203.10 (n/a)</td><td>142.50 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 <b>(+36.90%)</b></td><td>0.05 <b>(+24.31%)</b></td><td>0.05 (+19.35%)</td><td>0.05 <b>(+23.70%)</b></td><td>0.01 <b>(+103.23%)</b></td><td>165.20 (-19.14%)</td><td>151.28 (-19.10%)</td><td>155.00 (-16.22%)</td><td>126.20 <b>(-26.97%)</b></td><td>15.91 <b>(+20.29%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>187.00 (n/a)</td><td>185.00 (n/a)</td><td>172.80 (n/a)</td><td>13.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (+17.62%)</td><td>0.05 (+4.38%)</td><td>0.04 (-3.15%)</td><td>0.04 (-2.27%)</td><td>0.01 <b>(+58.48%)</b></td><td>224.40 (+2.33%)</td><td>184.12 (-3.03%)</td><td>188.90 (+3.28%)</td><td>140.80 (-14.98%)</td><td>30.32 <b>(+34.57%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>189.88 (n/a)</td><td>182.90 (n/a)</td><td>165.60 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(+22.14%)</b></td><td>0.05 (+13.87%)</td><td>0.05 (+13.69%)</td><td>0.04 (-8.88%)</td><td>0.01 <b>(+89.82%)</b></td><td>231.70 (+9.76%)</td><td>167.44 (-9.11%)</td><td>163.60 (-12.04%)</td><td>120.30 (-18.11%)</td><td>42.88 <b>(+72.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>184.22 (n/a)</td><td>186.00 (n/a)</td><td>146.90 (n/a)</td><td>24.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 <b>(+32.40%)</b></td><td>0.05 (+15.16%)</td><td>0.05 (+5.43%)</td><td>0.05 (+12.08%)</td><td>0.01 <b>(+125.66%)</b></td><td>181.80 (-10.75%)</td><td>165.46 (-12.26%)</td><td>173.00 (-5.15%)</td><td>130.20 <b>(-24.48%)</b></td><td>21.00 <b>(+47.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>203.70 (n/a)</td><td>188.58 (n/a)</td><td>182.40 (n/a)</td><td>172.40 (n/a)</td><td>14.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 <b>(+34.03%)</b></td><td>0.05 <b>(+23.40%)</b></td><td>0.05 (+9.60%)</td><td>0.05 <b>(+26.39%)</b></td><td>0.01 <b>(+54.56%)</b></td><td>171.90 <b>(-20.86%)</b></td><td>156.62 (-18.66%)</td><td>167.40 (-8.77%)</td><td>126.30 <b>(-25.35%)</b></td><td>19.34 (-10.21%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>217.20 (n/a)</td><td>192.54 (n/a)</td><td>183.50 (n/a)</td><td>169.20 (n/a)</td><td>21.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (+17.51%)</td><td>0.05 (+8.05%)</td><td>0.04 (+0.93%)</td><td>0.04 (+2.04%)</td><td>0.01 <b>(+66.97%)</b></td><td>204.50 (-2.01%)</td><td>169.80 (-5.82%)</td><td>186.00 (-0.91%)</td><td>129.00 (-14.91%)</td><td>32.06 <b>(+39.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.70 (n/a)</td><td>180.30 (n/a)</td><td>187.70 (n/a)</td><td>151.60 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (-1.51%)</td><td>0.04 (-9.09%)</td><td>0.04 (-4.52%)</td><td>0.02 <b>(-31.96%)</b></td><td>0.01 <b>(+52.92%)</b></td><td>328.80 <b>(+46.98%)</b></td><td>214.16 (+15.13%)</td><td>195.90 (+4.76%)</td><td>152.90 (+1.59%)</td><td>66.93 <b>(+143.25%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>186.02 (n/a)</td><td>187.00 (n/a)</td><td>150.50 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(+46.23%)</b></td><td>0.04 (+11.93%)</td><td>0.04 (+2.30%)</td><td>0.03 (-0.37%)</td><td>0.02 <b>(+110.16%)</b></td><td>312.70 (+0.35%)</td><td>214.54 (-5.21%)</td><td>212.50 (-2.25%)</td><td>118.60 <b>(-31.64%)</b></td><td>68.76 <b>(+32.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.60 (n/a)</td><td>226.32 (n/a)</td><td>217.40 (n/a)</td><td>173.50 (n/a)</td><td>51.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (+1.37%)</td><td>0.05 (-6.45%)</td><td>0.04 (-11.43%)</td><td>0.04 (-8.77%)</td><td>0.01 <b>(+20.01%)</b></td><td>211.30 (+9.60%)</td><td>180.08 (+7.91%)</td><td>188.40 (+12.88%)</td><td>133.30 (-1.33%)</td><td>31.70 <b>(+27.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>166.88 (n/a)</td><td>166.90 (n/a)</td><td>135.10 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (-9.85%)</td><td>0.04 (+6.00%)</td><td>0.04 (+4.45%)</td><td>0.03 (+7.91%)</td><td>0.01 <b>(-29.35%)</b></td><td>317.50 (-7.35%)</td><td>233.02 (-8.06%)</td><td>222.50 (-4.26%)</td><td>193.00 (+10.92%)</td><td>49.17 <b>(-25.89%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>342.70 (n/a)</td><td>253.44 (n/a)</td><td>232.40 (n/a)</td><td>174.00 (n/a)</td><td>66.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 <b>(-22.74%)</b></td><td>0.05 (+15.60%)</td><td>0.05 <b>(+25.36%)</b></td><td>0.05 <b>(+86.34%)</b></td><td>0.00 <b>(-79.60%)</b></td><td>174.20 <b>(-46.33%)</b></td><td>161.58 <b>(-22.24%)</b></td><td>157.50 <b>(-20.25%)</b></td><td>148.10 <b>(+29.46%)</b></td><td>11.03 <b>(-85.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>324.60 (n/a)</td><td>207.78 (n/a)</td><td>197.50 (n/a)</td><td>114.40 (n/a)</td><td>75.68 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (-3.94%)</td><td>0.04 (-9.70%)</td><td>0.04 (-18.31%)</td><td>0.03 (-13.31%)</td><td>0.01 (+12.80%)</td><td>246.20 (+15.37%)</td><td>203.94 (+13.16%)</td><td>232.10 <b>(+22.42%)</b></td><td>127.00 (+4.10%)</td><td>50.03 <b>(+38.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>180.22 (n/a)</td><td>189.60 (n/a)</td><td>122.00 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 <b>(-20.65%)</b></td><td>0.05 (-2.31%)</td><td>0.04 (+6.30%)</td><td>0.04 (+1.90%)</td><td>0.01 <b>(-46.26%)</b></td><td>213.50 (-1.84%)</td><td>179.70 (-1.78%)</td><td>185.30 (-5.89%)</td><td>136.20 <b>(+26.11%)</b></td><td>30.09 <b>(-32.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>182.96 (n/a)</td><td>196.90 (n/a)</td><td>108.00 (n/a)</td><td>44.52 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (-5.64%)</td><td>0.05 (+2.88%)</td><td>0.05 <b>(+21.49%)</b></td><td>0.03 <b>(-36.46%)</b></td><td>0.01 <b>(+60.62%)</b></td><td>319.90 <b>(+57.35%)</b></td><td>191.00 (+3.62%)</td><td>157.80 (-17.68%)</td><td>147.70 (+5.95%)</td><td>72.94 <b>(+183.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>184.32 (n/a)</td><td>191.70 (n/a)</td><td>139.40 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 <b>(-33.50%)</b></td><td>0.04 (-11.86%)</td><td>0.04 (+8.72%)</td><td>0.03 <b>(-22.79%)</b></td><td>0.01 <b>(-45.19%)</b></td><td>293.40 <b>(+29.48%)</b></td><td>217.34 (+11.35%)</td><td>192.20 (-8.04%)</td><td>187.00 <b>(+50.44%)</b></td><td>45.20 (+10.53%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.60 (n/a)</td><td>195.18 (n/a)</td><td>209.00 (n/a)</td><td>124.30 (n/a)</td><td>40.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 <b>(-26.41%)</b></td><td>0.04 (-6.18%)</td><td>0.04 (-2.25%)</td><td>0.04 (+1.17%)</td><td>0.00 <b>(-66.47%)</b></td><td>216.50 (-1.14%)</td><td>199.18 (+3.77%)</td><td>203.40 (+2.31%)</td><td>182.50 <b>(+35.89%)</b></td><td>15.53 <b>(-54.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>191.94 (n/a)</td><td>198.80 (n/a)</td><td>134.30 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52297.50 (n/a)</td><td>52249.26 (n/a)</td><td>52279.30 (n/a)</td><td>52167.80 (n/a)</td><td>57.29 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.18 (+18.90%)</td><td>0.16 (+12.88%)</td><td>0.15 (+7.39%)</td><td>0.15 (+13.50%)</td><td>0.02 <b>(+92.81%)</b></td><td>165.20 (-11.89%)</td><td>153.06 (-11.03%)</td><td>160.60 (-6.90%)</td><td>136.90 (-15.91%)</td><td>13.82 <b>(+42.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>172.04 (n/a)</td><td>172.50 (n/a)</td><td>162.80 (n/a)</td><td>9.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.35 (+18.41%)</td><td>0.30 (+17.65%)</td><td>0.31 <b>(+25.68%)</b></td><td>0.24 (-2.01%)</td><td>0.04 <b>(+95.96%)</b></td><td>173.80 (+2.06%)</td><td>138.68 (-13.90%)</td><td>131.10 <b>(-20.45%)</b></td><td>117.30 (-15.55%)</td><td>21.98 <b>(+74.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>170.30 (n/a)</td><td>161.06 (n/a)</td><td>164.80 (n/a)</td><td>138.90 (n/a)</td><td>12.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (+1.57%)</td><td>0.04 (+2.76%)</td><td>0.04 (+1.08%)</td><td>0.03 (-5.62%)</td><td>0.01 <b>(+28.79%)</b></td><td>185.00 (+5.96%)</td><td>146.58 (-1.80%)</td><td>142.70 (-1.11%)</td><td>124.20 (-1.51%)</td><td>25.45 <b>(+30.47%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>174.60 (n/a)</td><td>149.26 (n/a)</td><td>144.30 (n/a)</td><td>126.10 (n/a)</td><td>19.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (+11.44%)</td><td>0.05 (+4.12%)</td><td>0.05 (-4.06%)</td><td>0.04 (+2.79%)</td><td>0.01 <b>(+34.90%)</b></td><td>196.40 (-2.72%)</td><td>157.16 (-2.61%)</td><td>167.30 (+4.24%)</td><td>120.40 (-10.28%)</td><td>33.48 (+17.07%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>161.38 (n/a)</td><td>160.50 (n/a)</td><td>134.20 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.10 (+8.85%)</td><td>0.08 (+6.09%)</td><td>0.08 <b>(+25.13%)</b></td><td>0.05 (-18.63%)</td><td>0.02 <b>(+35.57%)</b></td><td>248.40 <b>(+22.91%)</b></td><td>169.14 (-2.99%)</td><td>153.20 <b>(-20.08%)</b></td><td>120.60 (-8.15%)</td><td>47.91 <b>(+58.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>174.36 (n/a)</td><td>191.70 (n/a)</td><td>131.30 (n/a)</td><td>30.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(+28.93%)</b></td><td>0.06 (+16.69%)</td><td>0.06 <b>(+21.70%)</b></td><td>0.04 (+0.09%)</td><td>0.01 <b>(+134.40%)</b></td><td>184.80 (-0.11%)</td><td>142.90 (-12.19%)</td><td>126.20 (-17.84%)</td><td>115.30 <b>(-22.46%)</b></td><td>29.54 <b>(+83.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.00 (n/a)</td><td>162.74 (n/a)</td><td>153.60 (n/a)</td><td>148.70 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (+10.00%)</td><td>0.06 (+3.95%)</td><td>0.07 (-0.30%)</td><td>0.05 <b>(+26.69%)</b></td><td>0.01 (-11.62%)</td><td>194.80 <b>(-21.04%)</b></td><td>166.06 (-5.20%)</td><td>157.30 (+0.32%)</td><td>136.90 (-9.10%)</td><td>26.10 <b>(-35.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>175.16 (n/a)</td><td>156.80 (n/a)</td><td>150.60 (n/a)</td><td>40.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (+12.06%)</td><td>0.06 <b>(+21.09%)</b></td><td>0.05 <b>(+28.35%)</b></td><td>0.05 <b>(+25.94%)</b></td><td>0.01 (-6.82%)</td><td>173.80 <b>(-20.60%)</b></td><td>149.30 (-18.39%)</td><td>154.10 <b>(-22.09%)</b></td><td>125.10 (-10.77%)</td><td>22.46 <b>(-34.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>182.94 (n/a)</td><td>197.80 (n/a)</td><td>140.20 (n/a)</td><td>34.33 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(-26.48%)</b></td><td>0.06 (-4.02%)</td><td>0.07 (-8.06%)</td><td>0.06 <b>(+55.46%)</b></td><td>0.00 <b>(-79.54%)</b></td><td>173.90 <b>(-35.66%)</b></td><td>158.86 (-5.35%)</td><td>155.20 (+8.76%)</td><td>144.80 <b>(+36.09%)</b></td><td>11.10 <b>(-82.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>270.30 (n/a)</td><td>167.84 (n/a)</td><td>142.70 (n/a)</td><td>106.40 (n/a)</td><td>63.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (+15.45%)</td><td>0.05 <b>(+27.71%)</b></td><td>0.05 <b>(+20.42%)</b></td><td>0.05 <b>(+34.77%)</b></td><td>0.01 (+2.27%)</td><td>178.10 <b>(-25.79%)</b></td><td>153.62 <b>(-22.45%)</b></td><td>167.30 (-16.93%)</td><td>121.50 (-13.40%)</td><td>25.18 <b>(-32.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.00 (n/a)</td><td>198.10 (n/a)</td><td>201.40 (n/a)</td><td>140.30 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (-11.98%)</td><td>0.06 (-0.83%)</td><td>0.05 (-9.43%)</td><td>0.05 (+6.99%)</td><td>0.01 <b>(-21.96%)</b></td><td>202.40 (-6.51%)</td><td>167.50 (-1.13%)</td><td>183.50 (+10.41%)</td><td>124.80 (+13.56%)</td><td>34.92 (-17.86%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>169.42 (n/a)</td><td>166.20 (n/a)</td><td>109.90 (n/a)</td><td>42.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (-17.37%)</td><td>0.05 (-1.30%)</td><td>0.05 (+12.84%)</td><td>0.04 (-4.92%)</td><td>0.01 <b>(-36.08%)</b></td><td>231.00 (+5.14%)</td><td>166.88 (-1.23%)</td><td>154.20 (-11.38%)</td><td>135.60 <b>(+21.07%)</b></td><td>36.98 (-14.13%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>168.96 (n/a)</td><td>174.00 (n/a)</td><td>112.00 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (-16.37%)</td><td>0.05 (-4.39%)</td><td>0.05 (-10.65%)</td><td>0.04 <b>(+21.84%)</b></td><td>0.01 <b>(-43.32%)</b></td><td>224.90 (-17.92%)</td><td>188.32 (+0.10%)</td><td>198.10 (+11.92%)</td><td>153.70 (+19.61%)</td><td>29.88 <b>(-46.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.00 (n/a)</td><td>188.14 (n/a)</td><td>177.00 (n/a)</td><td>128.50 (n/a)</td><td>55.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (+9.56%)</td><td>0.05 (+12.91%)</td><td>0.05 (+12.98%)</td><td>0.03 <b>(+20.60%)</b></td><td>0.01 (-9.76%)</td><td>234.60 (-17.07%)</td><td>167.46 (-13.92%)</td><td>161.10 (-11.48%)</td><td>118.30 (-8.72%)</td><td>42.44 <b>(-30.79%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.90 (n/a)</td><td>194.54 (n/a)</td><td>182.00 (n/a)</td><td>129.60 (n/a)</td><td>61.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (-11.88%)</td><td>0.04 (-16.22%)</td><td>0.04 (-14.62%)</td><td>0.03 <b>(-26.00%)</b></td><td>0.01 <b>(+39.70%)</b></td><td>283.70 <b>(+35.16%)</b></td><td>224.16 <b>(+20.76%)</b></td><td>212.70 (+17.13%)</td><td>191.20 (+13.47%)</td><td>35.11 <b>(+120.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.90 (n/a)</td><td>185.62 (n/a)</td><td>181.60 (n/a)</td><td>168.50 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 <b>(+45.22%)</b></td><td>0.05 (+16.68%)</td><td>0.05 (+10.76%)</td><td>0.04 (+9.33%)</td><td>0.01 <b>(+130.88%)</b></td><td>222.00 (-8.53%)</td><td>171.62 (-11.68%)</td><td>166.40 (-9.71%)</td><td>118.40 <b>(-31.12%)</b></td><td>38.68 <b>(+39.10%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>194.32 (n/a)</td><td>184.30 (n/a)</td><td>171.90 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (-5.44%)</td><td>0.04 (-3.03%)</td><td>0.04 (-3.28%)</td><td>0.04 <b>(+21.91%)</b></td><td>0.01 <b>(-33.90%)</b></td><td>240.80 (-17.98%)</td><td>213.20 (+0.14%)</td><td>215.60 (+3.41%)</td><td>164.50 (+5.72%)</td><td>30.02 <b>(-43.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.60 (n/a)</td><td>212.90 (n/a)</td><td>208.50 (n/a)</td><td>155.60 (n/a)</td><td>53.29 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 <b>(-31.84%)</b></td><td>0.04 (-17.72%)</td><td>0.04 (-3.15%)</td><td>0.03 (-16.53%)</td><td>0.01 <b>(-59.97%)</b></td><td>260.10 (+19.81%)</td><td>219.54 (+17.18%)</td><td>220.80 (+3.27%)</td><td>179.30 <b>(+46.73%)</b></td><td>28.73 <b>(-31.97%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>187.36 (n/a)</td><td>213.80 (n/a)</td><td>122.20 (n/a)</td><td>42.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.70 <b>(-22.48%)</b></td><td>0.54 <b>(-20.05%)</b></td><td>0.52 <b>(-25.29%)</b></td><td>0.39 <b>(-20.85%)</b></td><td>0.12 <b>(-25.29%)</b></td><td>249.30 <b>(+26.36%)</b></td><td>189.40 <b>(+24.46%)</b></td><td>188.70 <b>(+33.83%)</b></td><td>141.20 <b>(+29.07%)</b></td><td>42.58 (+18.63%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.90 (n/a)</td><td>0.68 (n/a)</td><td>0.70 (n/a)</td><td>0.50 (n/a)</td><td>0.16 (n/a)</td><td>197.30 (n/a)</td><td>152.18 (n/a)</td><td>141.00 (n/a)</td><td>109.40 (n/a)</td><td>35.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.71 (+7.22%)</td><td>0.57 (-1.72%)</td><td>0.59 (+3.86%)</td><td>0.40 (-17.70%)</td><td>0.12 <b>(+64.00%)</b></td><td>247.70 <b>(+21.48%)</b></td><td>178.98 (+4.56%)</td><td>166.00 (-3.71%)</td><td>139.30 (-6.70%)</td><td>42.69 <b>(+91.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.07 (n/a)</td><td>203.90 (n/a)</td><td>171.18 (n/a)</td><td>172.40 (n/a)</td><td>149.30 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.58 <b>(-27.64%)</b></td><td>0.54 (-13.58%)</td><td>0.55 (-7.61%)</td><td>0.47 (-5.98%)</td><td>0.04 <b>(-65.59%)</b></td><td>209.20 (+6.35%)</td><td>183.52 (+13.06%)</td><td>178.40 (+8.25%)</td><td>170.30 <b>(+38.23%)</b></td><td>15.17 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.80 (n/a)</td><td>0.62 (n/a)</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>196.70 (n/a)</td><td>162.32 (n/a)</td><td>164.80 (n/a)</td><td>123.20 (n/a)</td><td>29.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.55 (-12.88%)</td><td>0.51 (+8.08%)</td><td>0.52 (+7.03%)</td><td>0.44 <b>(+30.24%)</b></td><td>0.05 <b>(-60.59%)</b></td><td>225.30 <b>(-23.24%)</b></td><td>195.44 (-11.68%)</td><td>188.90 (-6.58%)</td><td>177.20 (+14.77%)</td><td>19.42 <b>(-65.97%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.64 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.12 (n/a)</td><td>293.50 (n/a)</td><td>221.28 (n/a)</td><td>202.20 (n/a)</td><td>154.40 (n/a)</td><td>57.07 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.54 (-6.06%)</td><td>0.47 (+4.01%)</td><td>0.48 (+12.90%)</td><td>0.38 (+2.52%)</td><td>0.07 (-10.20%)</td><td>192.60 (-2.43%)</td><td>160.26 (-4.12%)</td><td>153.60 (-11.42%)</td><td>137.60 (+6.42%)</td><td>23.69 (-4.90%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>197.40 (n/a)</td><td>167.14 (n/a)</td><td>173.40 (n/a)</td><td>129.30 (n/a)</td><td>24.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.59 (+12.35%)</td><td>0.48 (+10.76%)</td><td>0.53 <b>(+23.03%)</b></td><td>0.33 (-13.26%)</td><td>0.11 <b>(+86.74%)</b></td><td>224.00 (+15.29%)</td><td>161.64 (-6.59%)</td><td>139.80 (-18.72%)</td><td>124.60 (-10.94%)</td><td>41.49 <b>(+93.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.06 (n/a)</td><td>194.30 (n/a)</td><td>173.04 (n/a)</td><td>172.00 (n/a)</td><td>139.90 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.57 <b>(+28.40%)</b></td><td>0.49 <b>(+25.41%)</b></td><td>0.49 <b>(+26.27%)</b></td><td>0.41 <b>(+24.09%)</b></td><td>0.06 <b>(+43.29%)</b></td><td>178.40 (-19.42%)</td><td>153.00 <b>(-20.02%)</b></td><td>150.60 <b>(-20.78%)</b></td><td>128.30 <b>(-22.10%)</b></td><td>19.47 (-9.99%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.45 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.04 (n/a)</td><td>221.40 (n/a)</td><td>191.30 (n/a)</td><td>190.10 (n/a)</td><td>164.70 (n/a)</td><td>21.63 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.53 <b>(+22.65%)</b></td><td>0.43 (+11.67%)</td><td>0.40 (+4.64%)</td><td>0.33 (-2.55%)</td><td>0.08 <b>(+158.12%)</b></td><td>221.00 (+2.65%)</td><td>177.60 (-8.19%)</td><td>183.80 (-4.42%)</td><td>139.60 (-18.46%)</td><td>34.25 <b>(+111.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>193.44 (n/a)</td><td>192.30 (n/a)</td><td>171.20 (n/a)</td><td>16.18 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.06 (-8.30%)</td><td>0.93 (+2.38%)</td><td>1.00 <b>(+23.07%)</b></td><td>0.67 (-9.80%)</td><td>0.16 (-14.45%)</td><td>196.70 (+10.88%)</td><td>144.50 (-2.58%)</td><td>130.40 (-18.75%)</td><td>123.50 (+9.10%)</td><td>30.04 (+6.78%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.16 (n/a)</td><td>0.91 (n/a)</td><td>0.82 (n/a)</td><td>0.74 (n/a)</td><td>0.18 (n/a)</td><td>177.40 (n/a)</td><td>148.32 (n/a)</td><td>160.50 (n/a)</td><td>113.20 (n/a)</td><td>28.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.02 (-14.83%)</td><td>0.91 (+2.72%)</td><td>0.97 <b>(+20.73%)</b></td><td>0.77 (+5.64%)</td><td>0.12 <b>(-36.51%)</b></td><td>171.20 (-5.31%)</td><td>146.52 (-4.19%)</td><td>135.80 (-17.20%)</td><td>128.20 (+17.51%)</td><td>20.09 <b>(-26.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.20 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.72 (n/a)</td><td>0.19 (n/a)</td><td>180.80 (n/a)</td><td>152.92 (n/a)</td><td>164.00 (n/a)</td><td>109.10 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.95 (-10.64%)</td><td>0.85 (-4.08%)</td><td>0.91 (+6.93%)</td><td>0.64 (-10.33%)</td><td>0.13 (+0.70%)</td><td>204.90 (+11.48%)</td><td>158.30 (+4.72%)</td><td>144.40 (-6.48%)</td><td>137.60 (+11.87%)</td><td>28.21 <b>(+25.61%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.71 (n/a)</td><td>0.13 (n/a)</td><td>183.80 (n/a)</td><td>151.16 (n/a)</td><td>154.40 (n/a)</td><td>123.00 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-3.87%)</td><td>0.02 (-14.97%)</td><td>0.03 (-2.50%)</td><td>0.02 <b>(-28.32%)</b></td><td>0.01 <b>(+21.43%)</b></td><td>257.50 <b>(+39.49%)</b></td><td>183.42 <b>(+22.48%)</b></td><td>161.20 (+2.61%)</td><td>120.70 (+3.96%)</td><td>56.39 <b>(+85.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>149.76 (n/a)</td><td>157.10 (n/a)</td><td>116.10 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-14.49%)</td><td>0.03 (+0.38%)</td><td>0.03 <b>(+22.26%)</b></td><td>0.02 (+0.76%)</td><td>0.00 <b>(-43.66%)</b></td><td>189.50 (-0.79%)</td><td>159.54 (-2.43%)</td><td>148.90 (-18.19%)</td><td>140.80 (+16.94%)</td><td>20.24 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>163.52 (n/a)</td><td>182.00 (n/a)</td><td>120.40 (n/a)</td><td>31.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (+0.95%)</td><td>0.02 (+9.38%)</td><td>0.02 (+14.04%)</td><td>0.02 (-0.19%)</td><td>0.00 (+2.82%)</td><td>214.40 (+0.19%)</td><td>172.28 (-8.49%)</td><td>165.00 (-12.33%)</td><td>150.00 (-0.92%)</td><td>25.55 (+3.66%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.00 (n/a)</td><td>188.26 (n/a)</td><td>188.20 (n/a)</td><td>151.40 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.96 (-8.74%)</td><td>0.84 (+0.21%)</td><td>0.86 (+19.01%)</td><td>0.75 (+11.60%)</td><td>0.08 <b>(-55.83%)</b></td><td>176.30 (-10.37%)</td><td>158.18 (-3.23%)</td><td>154.00 (-15.98%)</td><td>138.00 (+9.61%)</td><td>15.53 <b>(-54.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.72 (n/a)</td><td>0.67 (n/a)</td><td>0.19 (n/a)</td><td>196.70 (n/a)</td><td>163.46 (n/a)</td><td>183.30 (n/a)</td><td>125.90 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.00 (-9.15%)</td><td>0.91 (+4.57%)</td><td>0.87 (+6.12%)</td><td>0.84 <b>(+56.92%)</b></td><td>0.08 <b>(-67.60%)</b></td><td>157.70 <b>(-36.28%)</b></td><td>146.14 (-10.45%)</td><td>151.00 (-5.80%)</td><td>131.60 (+10.03%)</td><td>12.20 <b>(-76.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.10 (n/a)</td><td>0.87 (n/a)</td><td>0.82 (n/a)</td><td>0.53 (n/a)</td><td>0.24 (n/a)</td><td>247.50 (n/a)</td><td>163.20 (n/a)</td><td>160.30 (n/a)</td><td>119.60 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.00 (-2.40%)</td><td>0.83 (-0.41%)</td><td>0.88 (+4.19%)</td><td>0.66 (-2.22%)</td><td>0.15 (+9.73%)</td><td>200.20 (+2.30%)</td><td>162.56 (+0.98%)</td><td>150.70 (-4.01%)</td><td>131.90 (+2.49%)</td><td>29.45 (+16.52%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.67 (n/a)</td><td>0.13 (n/a)</td><td>195.70 (n/a)</td><td>160.98 (n/a)</td><td>157.00 (n/a)</td><td>128.70 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.11 (+3.39%)</td><td>0.86 (+1.23%)</td><td>0.81 (+4.23%)</td><td>0.78 (+13.96%)</td><td>0.14 <b>(-24.54%)</b></td><td>169.20 (-12.24%)</td><td>156.40 (-3.03%)</td><td>163.70 (-4.04%)</td><td>119.40 (-3.32%)</td><td>20.81 <b>(-36.94%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>0.18 (n/a)</td><td>192.80 (n/a)</td><td>161.28 (n/a)</td><td>170.60 (n/a)</td><td>123.50 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.06 (-1.07%)</td><td>0.95 (+11.08%)</td><td>0.99 <b>(+22.69%)</b></td><td>0.83 <b>(+35.90%)</b></td><td>0.10 <b>(-48.60%)</b></td><td>159.10 <b>(-26.41%)</b></td><td>140.44 (-13.10%)</td><td>133.20 (-18.53%)</td><td>124.60 (+1.05%)</td><td>15.46 <b>(-59.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>1.07 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.61 (n/a)</td><td>0.20 (n/a)</td><td>216.20 (n/a)</td><td>161.62 (n/a)</td><td>163.50 (n/a)</td><td>123.30 (n/a)</td><td>38.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-9.62%)</td><td>0.03 (+13.19%)</td><td>0.03 <b>(+37.84%)</b></td><td>0.02 (-10.75%)</td><td>0.01 (-11.50%)</td><td>234.80 (+12.08%)</td><td>164.62 (-11.68%)</td><td>149.00 <b>(-27.42%)</b></td><td>137.10 (+10.65%)</td><td>40.70 (+12.50%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.50 (n/a)</td><td>186.38 (n/a)</td><td>205.30 (n/a)</td><td>123.90 (n/a)</td><td>36.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (-4.65%)</td><td>0.03 (-0.43%)</td><td>0.03 (+3.96%)</td><td>0.02 (-9.47%)</td><td>0.00 (+0.82%)</td><td>191.80 (+10.48%)</td><td>156.22 (+0.76%)</td><td>152.00 (-3.86%)</td><td>127.10 (+4.87%)</td><td>24.31 <b>(+21.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.60 (n/a)</td><td>155.04 (n/a)</td><td>158.10 (n/a)</td><td>121.20 (n/a)</td><td>20.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.00 (+6.98%)</td><td>0.00 (+4.78%)</td><td>0.00 (+4.76%)</td><td>0.00 (+5.13%)</td><td>0.00 (+17.06%)</td><td>1004.42 (-4.32%)</td><td>938.05 (-4.24%)</td><td>922.96 (-4.90%)</td><td>893.99 (-5.92%)</td><td>42.56 (+3.95%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1049.74 (n/a)</td><td>979.63 (n/a)</td><td>970.56 (n/a)</td><td>950.28 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.01 (-5.88%)</td><td>0.01 (-1.25%)</td><td>0.01 (-1.23%)</td><td>0.01 (+5.41%)</td><td>0.00 <b>(-72.35%)</b></td><td>1056.25 (-5.04%)</td><td>1039.29 (+1.67%)</td><td>1029.93 (+2.21%)</td><td>1026.67 (+6.77%)</td><td>15.24 <b>(-72.44%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1112.29 (n/a)</td><td>1022.18 (n/a)</td><td>1007.63 (n/a)</td><td>961.58 (n/a)</td><td>55.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.00 (n/a)</td><td>2192.27 (n/a)</td><td>2182.00 (n/a)</td><td>2183.27 (n/a)</td><td>2173.51 (n/a)</td><td>8.23 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.86 (n/a)</td><td>0.02 (n/a)</td><td>2447.65 (n/a)</td><td>2369.59 (n/a)</td><td>2362.67 (n/a)</td><td>2320.31 (n/a)</td><td>47.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.53 (-1.77%)</td><td>2.96 (+3.04%)</td><td>2.83 (+1.14%)</td><td>2.47 (-0.32%)</td><td>0.48 (+11.25%)</td><td>212.20 (+0.33%)</td><td>180.90 (-2.51%)</td><td>185.00 (-1.12%)</td><td>148.50 (+1.78%)</td><td>28.60 (+15.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.59 (n/a)</td><td>2.87 (n/a)</td><td>2.80 (n/a)</td><td>2.48 (n/a)</td><td>0.43 (n/a)</td><td>211.50 (n/a)</td><td>185.56 (n/a)</td><td>187.10 (n/a)</td><td>145.90 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.17 (-1.48%)</td><td>4.43 (-4.12%)</td><td>4.49 (-2.91%)</td><td>3.46 (-16.32%)</td><td>0.62 <b>(+48.83%)</b></td><td>303.40 (+19.50%)</td><td>240.78 (+5.46%)</td><td>233.80 (+3.04%)</td><td>202.70 (+1.50%)</td><td>37.42 <b>(+87.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>5.25 (n/a)</td><td>4.62 (n/a)</td><td>4.62 (n/a)</td><td>4.13 (n/a)</td><td>0.42 (n/a)</td><td>253.90 (n/a)</td><td>228.32 (n/a)</td><td>226.90 (n/a)</td><td>199.70 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.70 (+12.12%)</td><td>3.25 <b>(+28.44%)</b></td><td>3.29 <b>(+28.11%)</b></td><td>2.66 <b>(+45.80%)</b></td><td>0.38 <b>(-36.47%)</b></td><td>197.20 <b>(-31.41%)</b></td><td>163.30 <b>(-24.75%)</b></td><td>159.30 <b>(-21.95%)</b></td><td>141.70 (-10.82%)</td><td>20.62 <b>(-60.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>3.30 (n/a)</td><td>2.53 (n/a)</td><td>2.57 (n/a)</td><td>1.82 (n/a)</td><td>0.60 (n/a)</td><td>287.50 (n/a)</td><td>217.02 (n/a)</td><td>204.10 (n/a)</td><td>158.90 (n/a)</td><td>52.38 (n/a)</td>
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
