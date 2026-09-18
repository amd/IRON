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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (-19.67%)</td><td>0.07 (-5.14%)</td><td>0.08 (+1.63%)</td><td>0.06 (+11.38%)</td><td>0.01 <b>(-59.73%)</b></td><td>210.10 (-10.21%)</td><td>169.60 (-0.70%)</td><td>159.10 (-1.61%)</td><td>149.40 <b>(+24.50%)</b></td><td>24.13 <b>(-53.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>170.80 (n/a)</td><td>161.70 (n/a)</td><td>120.00 (n/a)</td><td>51.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (+4.87%)</td><td>0.08 (+4.05%)</td><td>0.08 (-4.32%)</td><td>0.06 (+0.13%)</td><td>0.01 <b>(+22.42%)</b></td><td>196.90 (-0.15%)</td><td>156.74 (-3.29%)</td><td>161.50 (+4.53%)</td><td>129.50 (-4.64%)</td><td>26.94 (+13.74%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>162.08 (n/a)</td><td>154.50 (n/a)</td><td>135.80 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.12 (+12.22%)</td><td>0.08 (+6.49%)</td><td>0.08 (+9.49%)</td><td>0.06 (+4.67%)</td><td>0.02 <b>(+28.72%)</b></td><td>198.30 (-4.48%)</td><td>160.22 (-4.39%)</td><td>155.10 (-8.66%)</td><td>101.60 (-10.88%)</td><td>38.90 (+14.56%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>167.58 (n/a)</td><td>169.80 (n/a)</td><td>114.00 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.10 (+11.31%)</td><td>0.07 (-3.38%)</td><td>0.07 (-4.51%)</td><td>0.06 (-5.63%)</td><td>0.02 <b>(+48.96%)</b></td><td>209.00 (+5.98%)</td><td>171.32 (+5.60%)</td><td>172.70 (+4.73%)</td><td>122.90 (-10.16%)</td><td>35.53 <b>(+45.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>162.24 (n/a)</td><td>164.90 (n/a)</td><td>136.80 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (+9.82%)</td><td>0.03 (-8.08%)</td><td>0.03 (-10.96%)</td><td>0.02 <b>(-21.03%)</b></td><td>0.01 <b>(+109.18%)</b></td><td>233.80 <b>(+26.58%)</b></td><td>182.82 (+11.29%)</td><td>181.10 (+12.34%)</td><td>137.40 (-8.95%)</td><td>34.37 <b>(+141.01%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.70 (n/a)</td><td>164.28 (n/a)</td><td>161.20 (n/a)</td><td>150.90 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (-12.57%)</td><td>0.03 (-11.45%)</td><td>0.04 (-1.48%)</td><td>0.02 <b>(-26.62%)</b></td><td>0.01 (+7.18%)</td><td>242.40 <b>(+36.26%)</b></td><td>172.34 (+15.40%)</td><td>148.30 (+1.51%)</td><td>129.20 (+14.34%)</td><td>45.90 <b>(+64.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.90 (n/a)</td><td>149.34 (n/a)</td><td>146.10 (n/a)</td><td>113.00 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 <b>(-32.96%)</b></td><td>0.03 (-19.75%)</td><td>0.03 (-16.47%)</td><td>0.03 (-9.41%)</td><td>0.00 <b>(-65.60%)</b></td><td>195.50 (+10.39%)</td><td>180.80 <b>(+21.31%)</b></td><td>189.80 (+19.75%)</td><td>156.40 <b>(+49.09%)</b></td><td>16.22 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>177.10 (n/a)</td><td>149.04 (n/a)</td><td>158.50 (n/a)</td><td>104.90 (n/a)</td><td>27.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 <b>(-32.86%)</b></td><td>0.03 <b>(-22.72%)</b></td><td>0.03 (-9.81%)</td><td>0.02 (-12.75%)</td><td>0.00 <b>(-59.70%)</b></td><td>237.50 (+14.62%)</td><td>203.84 <b>(+24.31%)</b></td><td>202.90 (+10.87%)</td><td>170.10 <b>(+48.95%)</b></td><td>28.96 <b>(-29.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>163.98 (n/a)</td><td>183.00 (n/a)</td><td>114.20 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (-4.38%)</td><td>0.03 (+0.97%)</td><td>0.03 (-13.37%)</td><td>0.03 <b>(+62.88%)</b></td><td>0.01 <b>(-37.03%)</b></td><td>206.30 <b>(-38.60%)</b></td><td>184.10 (-8.67%)</td><td>197.40 (+15.44%)</td><td>130.50 (+4.57%)</td><td>30.78 <b>(-62.24%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>336.00 (n/a)</td><td>201.58 (n/a)</td><td>171.00 (n/a)</td><td>124.80 (n/a)</td><td>81.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (+11.36%)</td><td>0.03 (+7.68%)</td><td>0.03 (+8.86%)</td><td>0.02 (-4.71%)</td><td>0.00 <b>(+91.82%)</b></td><td>214.00 (+4.95%)</td><td>177.46 (-5.81%)</td><td>176.00 (-8.14%)</td><td>146.30 (-10.19%)</td><td>27.98 <b>(+83.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>203.90 (n/a)</td><td>188.40 (n/a)</td><td>191.60 (n/a)</td><td>162.90 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (-12.60%)</td><td>0.03 (-12.53%)</td><td>0.03 (-10.66%)</td><td>0.02 (-10.69%)</td><td>0.00 <b>(-22.40%)</b></td><td>212.60 (+11.95%)</td><td>191.50 (+14.00%)</td><td>194.80 (+11.89%)</td><td>161.10 (+14.42%)</td><td>19.64 (-1.41%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>167.98 (n/a)</td><td>174.10 (n/a)</td><td>140.80 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.02 <b>(-24.45%)</b></td><td>0.02 <b>(-20.18%)</b></td><td>0.02 (-10.90%)</td><td>0.02 <b>(-28.14%)</b></td><td>0.00 (-17.92%)</td><td>320.30 <b>(+39.14%)</b></td><td>245.80 <b>(+25.83%)</b></td><td>228.90 (+12.21%)</td><td>221.60 <b>(+32.38%)</b></td><td>41.79 <b>(+58.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.20 (n/a)</td><td>195.34 (n/a)</td><td>204.00 (n/a)</td><td>167.40 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>187.02 (n/a)</td><td>173.20 (n/a)</td><td>159.00 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>165.76 (n/a)</td><td>157.90 (n/a)</td><td>139.20 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>249.20 (n/a)</td><td>193.10 (n/a)</td><td>205.70 (n/a)</td><td>140.40 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>329.20 (n/a)</td><td>221.30 (n/a)</td><td>205.80 (n/a)</td><td>163.10 (n/a)</td><td>69.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>149.58 (n/a)</td><td>148.70 (n/a)</td><td>121.00 (n/a)</td><td>24.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.00 (n/a)</td><td>160.20 (n/a)</td><td>150.52 (n/a)</td><td>149.60 (n/a)</td><td>141.60 (n/a)</td><td>9.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>155.24 (n/a)</td><td>144.10 (n/a)</td><td>132.50 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>270.60 (n/a)</td><td>188.76 (n/a)</td><td>177.80 (n/a)</td><td>147.50 (n/a)</td><td>47.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.11 (-14.39%)</td><td>2.96 (-5.45%)</td><td>2.93 (-5.49%)</td><td>2.86 (-0.90%)</td><td>0.10 <b>(-68.31%)</b></td><td>481.90 (+0.90%)</td><td>464.80 (+5.11%)</td><td>469.50 (+5.81%)</td><td>442.60 (+16.81%)</td><td>14.87 <b>(-62.79%)</b></td><td>606.52 (-14.39%)</td><td>578.01 (-5.45%)</td><td>571.79 (-5.49%)</td><td>557.02 (-0.90%)</td><td>18.80 <b>(-68.31%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.63 (n/a)</td><td>3.13 (n/a)</td><td>3.10 (n/a)</td><td>2.88 (n/a)</td><td>0.30 (n/a)</td><td>477.60 (n/a)</td><td>442.20 (n/a)</td><td>443.70 (n/a)</td><td>378.90 (n/a)</td><td>39.96 (n/a)</td><td>708.50 (n/a)</td><td>611.35 (n/a)</td><td>605.02 (n/a)</td><td>562.07 (n/a)</td><td>59.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.87 <b>(-27.72%)</b></td><td>3.69 (-17.40%)</td><td>3.72 (-13.60%)</td><td>3.46 (-9.91%)</td><td>0.19 <b>(-72.05%)</b></td><td>397.30 (+11.01%)</td><td>374.20 (+19.19%)</td><td>370.30 (+15.75%)</td><td>355.40 <b>(+38.34%)</b></td><td>19.24 <b>(-57.86%)</b></td><td>755.40 <b>(-27.72%)</b></td><td>718.89 (-17.40%)</td><td>725.00 (-13.60%)</td><td>675.62 (-9.91%)</td><td>36.67 <b>(-72.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>5.36 (n/a)</td><td>4.46 (n/a)</td><td>4.30 (n/a)</td><td>3.85 (n/a)</td><td>0.67 (n/a)</td><td>357.90 (n/a)</td><td>313.94 (n/a)</td><td>319.90 (n/a)</td><td>256.90 (n/a)</td><td>45.65 (n/a)</td><td>1045.06 (n/a)</td><td>870.34 (n/a)</td><td>839.17 (n/a)</td><td>749.97 (n/a)</td><td>131.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.99 (-12.80%)</td><td>4.04 (-14.76%)</td><td>3.59 (-12.58%)</td><td>3.42 (+0.54%)</td><td>1.10 <b>(-22.53%)</b></td><td>402.90 (-0.54%)</td><td>356.60 (+15.00%)</td><td>382.90 (+14.40%)</td><td>229.90 (+14.66%)</td><td>72.11 (-12.65%)</td><td>1167.63 (-12.80%)</td><td>787.28 (-14.76%)</td><td>701.06 (-12.58%)</td><td>666.18 (+0.54%)</td><td>214.02 <b>(-22.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.86 (n/a)</td><td>4.74 (n/a)</td><td>4.11 (n/a)</td><td>3.40 (n/a)</td><td>1.42 (n/a)</td><td>405.10 (n/a)</td><td>310.08 (n/a)</td><td>334.70 (n/a)</td><td>200.50 (n/a)</td><td>82.55 (n/a)</td><td>1339.00 (n/a)</td><td>923.55 (n/a)</td><td>801.92 (n/a)</td><td>662.61 (n/a)</td><td>276.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>7.24 (+14.93%)</td><td>4.57 (+11.61%)</td><td>3.95 (+2.42%)</td><td>3.57 (+13.79%)</td><td>1.54 <b>(+20.60%)</b></td><td>385.80 (-12.12%)</td><td>322.46 (-9.66%)</td><td>348.10 (-2.36%)</td><td>190.10 (-12.96%)</td><td>80.45 (-5.94%)</td><td>1412.28 (+14.93%)</td><td>891.57 (+11.61%)</td><td>771.23 (+2.42%)</td><td>695.82 (+13.79%)</td><td>299.75 <b>(+20.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.30 (n/a)</td><td>4.10 (n/a)</td><td>3.86 (n/a)</td><td>3.13 (n/a)</td><td>1.27 (n/a)</td><td>439.00 (n/a)</td><td>356.96 (n/a)</td><td>356.50 (n/a)</td><td>218.40 (n/a)</td><td>85.53 (n/a)</td><td>1228.82 (n/a)</td><td>798.83 (n/a)</td><td>752.97 (n/a)</td><td>611.47 (n/a)</td><td>248.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.25 (-11.78%)</td><td>3.06 (-5.37%)</td><td>3.10 (-1.42%)</td><td>2.66 (-12.01%)</td><td>0.24 (-12.52%)</td><td>517.10 (+13.65%)</td><td>452.62 (+5.67%)</td><td>443.70 (+1.44%)</td><td>423.70 (+13.35%)</td><td>38.02 (+13.52%)</td><td>633.53 (-11.78%)</td><td>596.17 (-5.37%)</td><td>604.97 (-1.42%)</td><td>519.14 (-12.01%)</td><td>46.29 (-12.52%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.68 (n/a)</td><td>3.23 (n/a)</td><td>3.15 (n/a)</td><td>3.02 (n/a)</td><td>0.27 (n/a)</td><td>455.00 (n/a)</td><td>428.32 (n/a)</td><td>437.40 (n/a)</td><td>373.80 (n/a)</td><td>33.49 (n/a)</td><td>718.09 (n/a)</td><td>630.03 (n/a)</td><td>613.71 (n/a)</td><td>590.02 (n/a)</td><td>52.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.67 <b>(-33.91%)</b></td><td>1.14 <b>(-24.86%)</b></td><td>1.03 (-9.32%)</td><td>0.94 (-13.16%)</td><td>0.30 <b>(-52.21%)</b></td><td>429.10 (+15.16%)</td><td>367.56 <b>(+24.35%)</b></td><td>389.30 (+10.28%)</td><td>240.80 <b>(+51.26%)</b></td><td>73.78 <b>(-22.83%)</b></td><td>139.33 <b>(-33.91%)</b></td><td>95.28 <b>(-24.86%)</b></td><td>86.20 (-9.32%)</td><td>78.20 (-13.16%)</td><td>24.99 <b>(-52.21%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.52 (n/a)</td><td>1.52 (n/a)</td><td>1.14 (n/a)</td><td>1.08 (n/a)</td><td>0.63 (n/a)</td><td>372.60 (n/a)</td><td>295.58 (n/a)</td><td>353.00 (n/a)</td><td>159.20 (n/a)</td><td>95.60 (n/a)</td><td>210.82 (n/a)</td><td>126.81 (n/a)</td><td>95.06 (n/a)</td><td>90.04 (n/a)</td><td>52.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>7.06 <b>(-20.11%)</b></td><td>5.42 (-15.54%)</td><td>5.05 (-17.07%)</td><td>4.61 (-4.38%)</td><td>0.96 <b>(-39.64%)</b></td><td>419.00 (+4.57%)</td><td>364.50 (+15.57%)</td><td>382.70 <b>(+20.57%)</b></td><td>274.00 <b>(+25.17%)</b></td><td>55.74 <b>(-23.02%)</b></td><td>1469.75 <b>(-20.11%)</b></td><td>1129.10 (-15.54%)</td><td>1052.06 (-17.07%)</td><td>960.92 (-4.38%)</td><td>200.82 <b>(-39.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>8.83 (n/a)</td><td>6.42 (n/a)</td><td>6.09 (n/a)</td><td>4.83 (n/a)</td><td>1.60 (n/a)</td><td>400.70 (n/a)</td><td>315.38 (n/a)</td><td>317.40 (n/a)</td><td>218.90 (n/a)</td><td>72.40 (n/a)</td><td>1839.62 (n/a)</td><td>1336.93 (n/a)</td><td>1268.56 (n/a)</td><td>1004.98 (n/a)</td><td>332.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>17.13 (+5.16%)</td><td>11.84 (-4.63%)</td><td>10.59 (-8.25%)</td><td>9.96 (-10.05%)</td><td>2.98 <b>(+36.78%)</b></td><td>552.80 (+11.16%)</td><td>483.56 (+6.85%)</td><td>520.00 (+8.99%)</td><td>321.40 (-4.91%)</td><td>92.45 <b>(+42.73%)</b></td><td>6681.43 (+5.16%)</td><td>4618.16 (-4.63%)</td><td>4130.17 (-8.25%)</td><td>3884.72 (-10.05%)</td><td>1161.79 <b>(+36.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>16.29 (n/a)</td><td>12.41 (n/a)</td><td>11.54 (n/a)</td><td>11.07 (n/a)</td><td>2.18 (n/a)</td><td>497.30 (n/a)</td><td>452.58 (n/a)</td><td>477.10 (n/a)</td><td>338.00 (n/a)</td><td>64.77 (n/a)</td><td>6353.71 (n/a)</td><td>4842.33 (n/a)</td><td>4501.35 (n/a)</td><td>4318.60 (n/a)</td><td>849.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>163.92 (n/a)</td><td>156.10 (n/a)</td><td>132.50 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.50 (n/a)</td><td>161.20 (n/a)</td><td>149.80 (n/a)</td><td>139.50 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>165.20 (n/a)</td><td>159.70 (n/a)</td><td>141.20 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>173.38 (n/a)</td><td>168.50 (n/a)</td><td>121.50 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>179.14 (n/a)</td><td>194.30 (n/a)</td><td>132.50 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>190.52 (n/a)</td><td>183.60 (n/a)</td><td>160.80 (n/a)</td><td>25.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>204.44 (n/a)</td><td>196.30 (n/a)</td><td>154.60 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.20 (n/a)</td><td>225.94 (n/a)</td><td>220.20 (n/a)</td><td>192.20 (n/a)</td><td>39.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>4.69 (+11.90%)</td><td>3.84 (-4.34%)</td><td>3.98 (-4.66%)</td><td>3.17 (-6.49%)</td><td>0.62 <b>(+75.10%)</b></td><td>2969.90 (+6.94%)</td><td>2498.68 (+5.97%)</td><td>2360.70 (+4.89%)</td><td>2007.20 (-10.63%)</td><td>399.03 <b>(+70.12%)</b></td><td>1843.08 (+11.90%)</td><td>1511.38 (-4.34%)</td><td>1567.05 (-4.66%)</td><td>1245.61 (-6.49%)</td><td>242.92 <b>(+75.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>4.19 (n/a)</td><td>4.02 (n/a)</td><td>4.18 (n/a)</td><td>3.39 (n/a)</td><td>0.35 (n/a)</td><td>2777.20 (n/a)</td><td>2357.96 (n/a)</td><td>2250.70 (n/a)</td><td>2245.90 (n/a)</td><td>234.55 (n/a)</td><td>1647.14 (n/a)</td><td>1579.92 (n/a)</td><td>1643.68 (n/a)</td><td>1332.05 (n/a)</td><td>138.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.63 <b>(+34.29%)</b></td><td>1.18 <b>(+21.11%)</b></td><td>1.31 (+13.82%)</td><td>0.71 (+12.41%)</td><td>0.41 <b>(+49.00%)</b></td><td>310.40 (-11.03%)</td><td>208.80 (-14.31%)</td><td>168.30 (-12.11%)</td><td>135.90 <b>(-25.58%)</b></td><td>80.39 (+3.02%)</td><td>69.42 <b>(+34.29%)</b></td><td>50.55 <b>(+21.11%)</b></td><td>56.08 (+13.82%)</td><td>30.41 (+12.41%)</td><td>17.56 <b>(+49.00%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.21 (n/a)</td><td>0.98 (n/a)</td><td>1.15 (n/a)</td><td>0.63 (n/a)</td><td>0.28 (n/a)</td><td>348.90 (n/a)</td><td>243.68 (n/a)</td><td>191.50 (n/a)</td><td>182.60 (n/a)</td><td>78.03 (n/a)</td><td>51.69 (n/a)</td><td>41.74 (n/a)</td><td>49.27 (n/a)</td><td>27.05 (n/a)</td><td>11.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.13 (-6.17%)</td><td>0.89 (-8.56%)</td><td>0.91 (-9.69%)</td><td>0.59 (-5.70%)</td><td>0.21 (-4.83%)</td><td>373.30 (+6.05%)</td><td>259.82 (+9.34%)</td><td>243.10 (+10.75%)</td><td>196.50 (+6.62%)</td><td>69.43 (+4.72%)</td><td>48.04 (-6.17%)</td><td>38.16 (-8.56%)</td><td>38.82 (-9.69%)</td><td>25.28 (-5.70%)</td><td>8.77 (-4.83%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.20 (n/a)</td><td>0.98 (n/a)</td><td>1.01 (n/a)</td><td>0.63 (n/a)</td><td>0.22 (n/a)</td><td>352.00 (n/a)</td><td>237.62 (n/a)</td><td>219.50 (n/a)</td><td>184.30 (n/a)</td><td>66.30 (n/a)</td><td>51.19 (n/a)</td><td>41.74 (n/a)</td><td>42.99 (n/a)</td><td>26.81 (n/a)</td><td>9.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.53 (-0.76%)</td><td>0.53 (-0.19%)</td><td>0.53 (-0.06%)</td><td>0.53 (-0.00%)</td><td>0.00 <b>(-83.90%)</b></td><td>47850.70 (+0.00%)</td><td>47820.26 (+0.19%)</td><td>47823.80 (+0.06%)</td><td>47785.20 (+0.77%)</td><td>28.48 <b>(-83.76%)</b></td><td>359.52 (-0.76%)</td><td>359.26 (-0.19%)</td><td>359.23 (-0.06%)</td><td>359.03 (-0.00%)</td><td>0.21 <b>(-83.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47850.00 (n/a)</td><td>47731.80 (n/a)</td><td>47795.00 (n/a)</td><td>47421.80 (n/a)</td><td>175.37 (n/a)</td><td>362.28 (n/a)</td><td>359.93 (n/a)</td><td>359.45 (n/a)</td><td>359.04 (n/a)</td><td>1.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.91 (+0.21%)</td><td>0.90 (-0.06%)</td><td>0.90 (-0.10%)</td><td>0.89 (-0.34%)</td><td>0.01 <b>(+45.99%)</b></td><td>28215.50 (+0.34%)</td><td>27934.44 (+0.06%)</td><td>27916.00 (+0.10%)</td><td>27749.60 (-0.21%)</td><td>172.84 <b>(+46.18%)</b></td><td>619.10 (+0.21%)</td><td>615.03 (-0.06%)</td><td>615.41 (-0.10%)</td><td>608.88 (-0.34%)</td><td>3.79 <b>(+45.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28120.20 (n/a)</td><td>27918.34 (n/a)</td><td>27889.00 (n/a)</td><td>27807.70 (n/a)</td><td>118.24 (n/a)</td><td>617.81 (n/a)</td><td>615.37 (n/a)</td><td>616.01 (n/a)</td><td>610.94 (n/a)</td><td>2.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.33 (+0.69%)</td><td>3.20 (-2.12%)</td><td>3.17 (-3.97%)</td><td>3.10 (-1.18%)</td><td>0.09 (+17.16%)</td><td>8106.40 (+1.19%)</td><td>7863.56 (+2.18%)</td><td>7930.30 (+4.13%)</td><td>7547.70 (-0.68%)</td><td>208.02 (+17.19%)</td><td>2276.17 (+0.69%)</td><td>2185.99 (-2.12%)</td><td>2166.37 (-3.97%)</td><td>2119.29 (-1.18%)</td><td>58.60 (+17.16%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.31 (n/a)</td><td>3.27 (n/a)</td><td>3.30 (n/a)</td><td>3.14 (n/a)</td><td>0.07 (n/a)</td><td>8011.00 (n/a)</td><td>7695.84 (n/a)</td><td>7615.70 (n/a)</td><td>7599.50 (n/a)</td><td>177.51 (n/a)</td><td>2260.65 (n/a)</td><td>2233.28 (n/a)</td><td>2255.85 (n/a)</td><td>2144.55 (n/a)</td><td>50.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>4.17 (+4.85%)</td><td>3.63 (-2.00%)</td><td>3.68 (-4.32%)</td><td>3.04 (-6.91%)</td><td>0.41 <b>(+36.88%)</b></td><td>2651.60 (+7.43%)</td><td>2244.40 (+2.55%)</td><td>2193.30 (+4.52%)</td><td>1934.40 (-4.62%)</td><td>261.81 <b>(+41.99%)</b></td><td>1092.79 (+4.85%)</td><td>951.75 (-2.00%)</td><td>963.80 (-4.32%)</td><td>797.23 (-6.91%)</td><td>106.65 <b>(+36.88%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.97 (n/a)</td><td>3.70 (n/a)</td><td>3.84 (n/a)</td><td>3.27 (n/a)</td><td>0.30 (n/a)</td><td>2468.30 (n/a)</td><td>2188.50 (n/a)</td><td>2098.50 (n/a)</td><td>2028.20 (n/a)</td><td>184.39 (n/a)</td><td>1042.28 (n/a)</td><td>971.17 (n/a)</td><td>1007.33 (n/a)</td><td>856.42 (n/a)</td><td>77.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.54 (+4.82%)</td><td>0.41 (+7.80%)</td><td>0.35 (-0.49%)</td><td>0.33 (+2.82%)</td><td>0.09 (+17.69%)</td><td>3758.20 (-2.75%)</td><td>3175.66 (-6.37%)</td><td>3550.30 (+0.49%)</td><td>2310.80 (-4.60%)</td><td>644.05 (+14.17%)</td><td>29.04 (+4.82%)</td><td>21.93 (+7.80%)</td><td>18.90 (-0.49%)</td><td>17.86 (+2.82%)</td><td>4.93 (+17.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>3864.30 (n/a)</td><td>3391.70 (n/a)</td><td>3532.90 (n/a)</td><td>2422.30 (n/a)</td><td>564.10 (n/a)</td><td>27.70 (n/a)</td><td>20.34 (n/a)</td><td>19.00 (n/a)</td><td>17.37 (n/a)</td><td>4.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.12 <b>(-21.05%)</b></td><td>4.24 (-17.94%)</td><td>4.41 (-9.05%)</td><td>3.40 <b>(-26.60%)</b></td><td>0.76 (+1.96%)</td><td>1956.40 <b>(+36.24%)</b></td><td>1610.32 <b>(+23.39%)</b></td><td>1509.10 (+9.94%)</td><td>1300.10 <b>(+26.67%)</b></td><td>297.70 <b>(+84.46%)</b></td><td>1580.85 <b>(-21.05%)</b></td><td>1310.97 (-17.94%)</td><td>1361.88 (-9.05%)</td><td>1050.53 <b>(-26.60%)</b></td><td>235.43 (+1.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.48 (n/a)</td><td>5.17 (n/a)</td><td>4.85 (n/a)</td><td>4.63 (n/a)</td><td>0.75 (n/a)</td><td>1436.00 (n/a)</td><td>1305.10 (n/a)</td><td>1372.60 (n/a)</td><td>1026.40 (n/a)</td><td>161.39 (n/a)</td><td>2002.41 (n/a)</td><td>1597.55 (n/a)</td><td>1497.31 (n/a)</td><td>1431.19 (n/a)</td><td>230.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>13.47 (n/a)</td><td>11.80 (n/a)</td><td>11.16 (n/a)</td><td>10.16 (n/a)</td><td>1.55 (n/a)</td><td>13.47 (n/a)</td><td>11.80 (n/a)</td><td>11.15 (n/a)</td><td>10.16 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>24.95 (-0.84%)</td><td>24.54 (+1.82%)</td><td>24.77 (+2.08%)</td><td>23.90 (+6.34%)</td><td>0.49 <b>(-50.38%)</b></td><td>24.94 (-0.84%)</td><td>24.52 (+1.82%)</td><td>24.75 (+2.08%)</td><td>23.88 (+6.34%)</td><td>0.49 <b>(-50.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>25.16 (n/a)</td><td>24.10 (n/a)</td><td>24.26 (n/a)</td><td>22.47 (n/a)</td><td>0.99 (n/a)</td><td>25.15 (n/a)</td><td>24.08 (n/a)</td><td>24.25 (n/a)</td><td>22.46 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>42.33 (-1.24%)</td><td>40.36 (-1.14%)</td><td>41.45 (+3.09%)</td><td>35.48 (-10.89%)</td><td>2.80 <b>(+118.96%)</b></td><td>42.30 (-1.24%)</td><td>40.34 (-1.14%)</td><td>41.42 (+3.09%)</td><td>35.46 (-10.89%)</td><td>2.80 <b>(+118.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>42.86 (n/a)</td><td>40.83 (n/a)</td><td>40.21 (n/a)</td><td>39.82 (n/a)</td><td>1.28 (n/a)</td><td>42.83 (n/a)</td><td>40.80 (n/a)</td><td>40.18 (n/a)</td><td>39.79 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>45.57 (-1.16%)</td><td>43.28 (-3.59%)</td><td>42.88 (-5.39%)</td><td>42.00 (-3.10%)</td><td>1.47 <b>(+27.74%)</b></td><td>45.55 (-1.16%)</td><td>43.25 (-3.59%)</td><td>42.85 (-5.39%)</td><td>41.97 (-3.10%)</td><td>1.46 <b>(+27.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>46.11 (n/a)</td><td>44.89 (n/a)</td><td>45.32 (n/a)</td><td>43.34 (n/a)</td><td>1.15 (n/a)</td><td>46.08 (n/a)</td><td>44.86 (n/a)</td><td>45.29 (n/a)</td><td>43.31 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>13.41 (n/a)</td><td>13.13 (n/a)</td><td>13.28 (n/a)</td><td>12.77 (n/a)</td><td>0.31 (n/a)</td><td>13.40 (n/a)</td><td>13.12 (n/a)</td><td>13.28 (n/a)</td><td>12.77 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>25.20 (-0.24%)</td><td>24.26 (-1.24%)</td><td>24.72 (+1.39%)</td><td>22.19 (-7.23%)</td><td>1.21 <b>(+122.96%)</b></td><td>25.18 (-0.24%)</td><td>24.25 (-1.24%)</td><td>24.70 (+1.39%)</td><td>22.18 (-7.23%)</td><td>1.21 <b>(+122.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>25.26 (n/a)</td><td>24.56 (n/a)</td><td>24.38 (n/a)</td><td>23.92 (n/a)</td><td>0.54 (n/a)</td><td>25.25 (n/a)</td><td>24.55 (n/a)</td><td>24.37 (n/a)</td><td>23.91 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>42.52 (+1.76%)</td><td>40.10 (-1.24%)</td><td>41.09 (-0.59%)</td><td>34.61 (-11.65%)</td><td>3.17 <b>(+156.35%)</b></td><td>42.49 (+1.76%)</td><td>40.08 (-1.24%)</td><td>41.06 (-0.59%)</td><td>34.59 (-11.65%)</td><td>3.16 <b>(+156.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>41.78 (n/a)</td><td>40.61 (n/a)</td><td>41.33 (n/a)</td><td>39.17 (n/a)</td><td>1.23 (n/a)</td><td>41.76 (n/a)</td><td>40.58 (n/a)</td><td>41.31 (n/a)</td><td>39.15 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>46.32 (-0.61%)</td><td>44.77 (+9.57%)</td><td>45.69 (+1.01%)</td><td>42.53 <b>(+81.82%)</b></td><td>1.65 <b>(-83.23%)</b></td><td>46.30 (-0.61%)</td><td>44.74 (+9.57%)</td><td>45.66 (+1.01%)</td><td>42.50 <b>(+81.82%)</b></td><td>1.65 <b>(-83.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>46.61 (n/a)</td><td>40.86 (n/a)</td><td>45.24 (n/a)</td><td>23.39 (n/a)</td><td>9.86 (n/a)</td><td>46.58 (n/a)</td><td>40.83 (n/a)</td><td>45.21 (n/a)</td><td>23.37 (n/a)</td><td>9.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>9.33 (+3.54%)</td><td>8.41 (+1.49%)</td><td>8.45 (+2.58%)</td><td>7.81 (+6.60%)</td><td>0.61 (-5.17%)</td><td>9.31 (+3.54%)</td><td>8.39 (+1.49%)</td><td>8.44 (+2.58%)</td><td>7.79 (+6.60%)</td><td>0.60 (-5.17%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>9.01 (n/a)</td><td>8.28 (n/a)</td><td>8.24 (n/a)</td><td>7.32 (n/a)</td><td>0.64 (n/a)</td><td>8.99 (n/a)</td><td>8.27 (n/a)</td><td>8.22 (n/a)</td><td>7.31 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.94 (+1.00%)</td><td>0.83 (-5.91%)</td><td>0.80 (-7.41%)</td><td>0.73 (-7.78%)</td><td>0.08 <b>(+35.49%)</b></td><td>0.93 (+1.00%)</td><td>0.81 (-5.91%)</td><td>0.79 (-7.41%)</td><td>0.72 (-7.78%)</td><td>0.08 <b>(+35.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.93 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.80 (n/a)</td><td>0.06 (n/a)</td><td>0.92 (n/a)</td><td>0.86 (n/a)</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.37 (+2.07%)</td><td>1.07 (-1.15%)</td><td>1.10 (+4.83%)</td><td>0.88 (-2.85%)</td><td>0.20 <b>(+21.79%)</b></td><td>1.35 (+2.07%)</td><td>1.06 (-1.15%)</td><td>1.08 (+4.83%)</td><td>0.87 (-2.85%)</td><td>0.19 <b>(+21.79%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.34 (n/a)</td><td>1.08 (n/a)</td><td>1.05 (n/a)</td><td>0.91 (n/a)</td><td>0.16 (n/a)</td><td>1.33 (n/a)</td><td>1.07 (n/a)</td><td>1.03 (n/a)</td><td>0.90 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>18.35 (+2.24%)</td><td>15.30 (-9.14%)</td><td>15.38 (-10.73%)</td><td>13.08 (-16.67%)</td><td>2.18 <b>(+116.23%)</b></td><td>18.13 (+2.24%)</td><td>15.12 (-9.14%)</td><td>15.20 (-10.73%)</td><td>12.93 (-16.67%)</td><td>2.16 <b>(+116.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>17.94 (n/a)</td><td>16.84 (n/a)</td><td>17.23 (n/a)</td><td>15.70 (n/a)</td><td>1.01 (n/a)</td><td>17.74 (n/a)</td><td>16.65 (n/a)</td><td>17.03 (n/a)</td><td>15.52 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>14.01 (+2.72%)</td><td>13.49 (+2.02%)</td><td>13.54 (+2.69%)</td><td>12.60 (-0.22%)</td><td>0.54 <b>(+37.16%)</b></td><td>13.77 (+2.72%)</td><td>13.25 (+2.02%)</td><td>13.30 (+2.69%)</td><td>12.38 (-0.22%)</td><td>0.53 <b>(+37.16%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.64 (n/a)</td><td>13.22 (n/a)</td><td>13.19 (n/a)</td><td>12.62 (n/a)</td><td>0.39 (n/a)</td><td>13.40 (n/a)</td><td>12.99 (n/a)</td><td>12.96 (n/a)</td><td>12.40 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>8.43 (-2.31%)</td><td>7.60 (-1.52%)</td><td>7.48 (-1.76%)</td><td>7.10 (+2.21%)</td><td>0.51 <b>(-32.97%)</b></td><td>8.28 (-2.31%)</td><td>7.47 (-1.52%)</td><td>7.35 (-1.76%)</td><td>6.98 (+2.21%)</td><td>0.50 <b>(-32.97%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>8.63 (n/a)</td><td>7.72 (n/a)</td><td>7.62 (n/a)</td><td>6.95 (n/a)</td><td>0.76 (n/a)</td><td>8.48 (n/a)</td><td>7.58 (n/a)</td><td>7.49 (n/a)</td><td>6.83 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.86 (-8.61%)</td><td>5.60 (-4.60%)</td><td>5.78 (-3.51%)</td><td>5.00 (+0.72%)</td><td>0.36 <b>(-38.96%)</b></td><td>5.77 (-8.61%)</td><td>5.51 (-4.60%)</td><td>5.68 (-3.51%)</td><td>4.92 (+0.72%)</td><td>0.36 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.41 (n/a)</td><td>5.87 (n/a)</td><td>5.99 (n/a)</td><td>4.96 (n/a)</td><td>0.59 (n/a)</td><td>6.31 (n/a)</td><td>5.78 (n/a)</td><td>5.89 (n/a)</td><td>4.88 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>12.70 (n/a)</td><td>11.67 (n/a)</td><td>11.15 (n/a)</td><td>10.92 (n/a)</td><td>0.92 (n/a)</td><td>12.69 (n/a)</td><td>11.66 (n/a)</td><td>11.15 (n/a)</td><td>10.91 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>13.48 (n/a)</td><td>12.97 (n/a)</td><td>13.07 (n/a)</td><td>12.29 (n/a)</td><td>0.48 (n/a)</td><td>13.47 (n/a)</td><td>12.96 (n/a)</td><td>13.07 (n/a)</td><td>12.28 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>174.54 (n/a)</td><td>159.80 (n/a)</td><td>142.00 (n/a)</td><td>37.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.20 (n/a)</td><td>155.64 (n/a)</td><td>159.90 (n/a)</td><td>110.70 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.40 (n/a)</td><td>158.48 (n/a)</td><td>163.90 (n/a)</td><td>132.10 (n/a)</td><td>15.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>156.42 (n/a)</td><td>145.20 (n/a)</td><td>119.50 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>155.72 (n/a)</td><td>153.50 (n/a)</td><td>107.90 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>194.34 (n/a)</td><td>192.30 (n/a)</td><td>170.50 (n/a)</td><td>23.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.50 (n/a)</td><td>188.34 (n/a)</td><td>169.10 (n/a)</td><td>153.50 (n/a)</td><td>38.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>345.20 (n/a)</td><td>223.32 (n/a)</td><td>189.90 (n/a)</td><td>179.00 (n/a)</td><td>69.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (+12.10%)</td><td>0.05 <b>(+21.61%)</b></td><td>0.06 <b>(+37.36%)</b></td><td>0.04 (+8.92%)</td><td>0.01 (+11.52%)</td><td>216.80 (-8.17%)</td><td>158.12 (-17.53%)</td><td>144.40 <b>(-27.18%)</b></td><td>118.10 (-10.80%)</td><td>37.22 (-3.17%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>191.72 (n/a)</td><td>198.30 (n/a)</td><td>132.40 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 <b>(+34.16%)</b></td><td>0.05 (+10.84%)</td><td>0.05 (+7.80%)</td><td>0.04 (+6.03%)</td><td>0.01 <b>(+129.11%)</b></td><td>197.90 (-5.67%)</td><td>166.18 (-7.19%)</td><td>167.90 (-7.24%)</td><td>112.60 <b>(-25.43%)</b></td><td>33.23 <b>(+56.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.80 (n/a)</td><td>179.06 (n/a)</td><td>181.00 (n/a)</td><td>151.00 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+19.30%)</td><td>0.05 <b>(+22.71%)</b></td><td>0.05 <b>(+29.96%)</b></td><td>0.04 (+17.73%)</td><td>0.01 <b>(+43.00%)</b></td><td>203.10 (-15.06%)</td><td>162.22 (-17.99%)</td><td>150.10 <b>(-23.07%)</b></td><td>138.00 (-16.16%)</td><td>26.89 (+1.09%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.10 (n/a)</td><td>197.80 (n/a)</td><td>195.10 (n/a)</td><td>164.60 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 <b>(+39.70%)</b></td><td>0.05 (+17.82%)</td><td>0.05 (+12.31%)</td><td>0.04 (+11.19%)</td><td>0.01 <b>(+138.97%)</b></td><td>189.60 (-10.06%)</td><td>165.80 (-13.15%)</td><td>175.90 (-10.98%)</td><td>114.90 <b>(-28.41%)</b></td><td>29.31 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>190.90 (n/a)</td><td>197.60 (n/a)</td><td>160.50 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (-19.93%)</td><td>0.05 (-4.37%)</td><td>0.05 (+1.36%)</td><td>0.04 (+12.16%)</td><td>0.01 <b>(-46.11%)</b></td><td>190.90 (-10.84%)</td><td>170.32 (+0.20%)</td><td>175.30 (-1.35%)</td><td>125.70 <b>(+24.83%)</b></td><td>26.53 <b>(-36.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>214.10 (n/a)</td><td>169.98 (n/a)</td><td>177.70 (n/a)</td><td>100.70 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+3.57%)</td><td>0.05 (+4.13%)</td><td>0.04 (+0.63%)</td><td>0.04 (+0.74%)</td><td>0.01 (+14.26%)</td><td>206.10 (-0.72%)</td><td>174.44 (-3.51%)</td><td>182.40 (-0.60%)</td><td>136.90 (-3.46%)</td><td>29.46 (+8.56%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>180.78 (n/a)</td><td>183.50 (n/a)</td><td>141.80 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (+17.21%)</td><td>0.05 (+18.54%)</td><td>0.06 <b>(+45.86%)</b></td><td>0.04 (-3.14%)</td><td>0.01 <b>(+49.50%)</b></td><td>224.50 (+3.27%)</td><td>162.94 (-12.86%)</td><td>139.00 <b>(-31.43%)</b></td><td>115.60 (-14.62%)</td><td>47.92 <b>(+33.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>186.98 (n/a)</td><td>202.70 (n/a)</td><td>135.40 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+3.72%)</td><td>0.05 (+11.89%)</td><td>0.04 (+12.93%)</td><td>0.04 <b>(+22.57%)</b></td><td>0.01 <b>(-26.60%)</b></td><td>202.40 (-18.39%)</td><td>174.56 (-12.97%)</td><td>184.70 (-11.46%)</td><td>138.30 (-3.62%)</td><td>26.33 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.00 (n/a)</td><td>200.58 (n/a)</td><td>208.60 (n/a)</td><td>143.50 (n/a)</td><td>46.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+15.99%)</td><td>0.05 (+19.79%)</td><td>0.05 <b>(+25.65%)</b></td><td>0.04 (+6.13%)</td><td>0.01 <b>(+60.27%)</b></td><td>193.70 (-5.79%)</td><td>159.54 (-16.06%)</td><td>151.90 <b>(-20.43%)</b></td><td>145.20 (-13.78%)</td><td>19.44 <b>(+33.82%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>205.60 (n/a)</td><td>190.06 (n/a)</td><td>190.90 (n/a)</td><td>168.40 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 <b>(-33.03%)</b></td><td>0.04 (-13.95%)</td><td>0.04 (-12.41%)</td><td>0.04 (-0.06%)</td><td>0.00 <b>(-69.93%)</b></td><td>231.70 (+0.04%)</td><td>216.84 (+12.10%)</td><td>228.40 (+14.14%)</td><td>190.60 <b>(+49.37%)</b></td><td>18.67 <b>(-52.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>193.44 (n/a)</td><td>200.10 (n/a)</td><td>127.60 (n/a)</td><td>39.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 <b>(+54.06%)</b></td><td>0.06 <b>(+21.21%)</b></td><td>0.05 (+1.39%)</td><td>0.04 (+1.63%)</td><td>0.02 <b>(+352.37%)</b></td><td>196.30 (-1.60%)</td><td>155.28 (-13.02%)</td><td>173.90 (-1.36%)</td><td>106.40 <b>(-35.12%)</b></td><td>39.24 <b>(+185.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.50 (n/a)</td><td>178.52 (n/a)</td><td>176.30 (n/a)</td><td>164.00 (n/a)</td><td>13.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 <b>(+39.21%)</b></td><td>0.04 (+5.46%)</td><td>0.03 (-3.26%)</td><td>0.02 (-12.55%)</td><td>0.01 <b>(+138.83%)</b></td><td>358.40 (+14.36%)</td><td>254.94 (+2.67%)</td><td>252.80 (+3.35%)</td><td>136.80 <b>(-28.15%)</b></td><td>82.11 <b>(+88.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>313.40 (n/a)</td><td>248.30 (n/a)</td><td>244.60 (n/a)</td><td>190.40 (n/a)</td><td>43.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+1.45%)</td><td>0.05 (+5.56%)</td><td>0.04 (-10.73%)</td><td>0.04 <b>(+66.73%)</b></td><td>0.01 <b>(-32.75%)</b></td><td>189.90 <b>(-40.02%)</b></td><td>168.32 (-11.43%)</td><td>188.10 (+11.96%)</td><td>130.10 (-1.44%)</td><td>29.09 <b>(-60.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.60 (n/a)</td><td>190.04 (n/a)</td><td>168.00 (n/a)</td><td>132.00 (n/a)</td><td>74.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+5.22%)</td><td>0.05 (+12.99%)</td><td>0.05 <b>(+24.37%)</b></td><td>0.04 (+10.58%)</td><td>0.01 (+8.96%)</td><td>183.90 (-9.54%)</td><td>161.70 (-11.45%)</td><td>150.90 (-19.56%)</td><td>144.10 (-4.95%)</td><td>19.92 (-5.03%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.30 (n/a)</td><td>182.60 (n/a)</td><td>187.60 (n/a)</td><td>151.60 (n/a)</td><td>20.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (+3.80%)</td><td>0.05 (+14.37%)</td><td>0.05 <b>(+20.26%)</b></td><td>0.04 (+5.80%)</td><td>0.01 (+19.16%)</td><td>205.50 (-5.47%)</td><td>157.50 (-11.73%)</td><td>154.00 (-16.80%)</td><td>123.00 (-3.68%)</td><td>35.75 (+9.23%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.40 (n/a)</td><td>178.42 (n/a)</td><td>185.10 (n/a)</td><td>127.70 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (-9.44%)</td><td>0.05 (+5.15%)</td><td>0.05 (+8.48%)</td><td>0.05 <b>(+29.78%)</b></td><td>0.01 <b>(-58.21%)</b></td><td>161.20 <b>(-22.98%)</b></td><td>152.14 (-8.25%)</td><td>157.40 (-7.79%)</td><td>129.50 (+10.40%)</td><td>12.84 <b>(-64.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.30 (n/a)</td><td>165.82 (n/a)</td><td>170.70 (n/a)</td><td>117.30 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (+0.82%)</td><td>0.05 (+9.92%)</td><td>0.05 (+15.04%)</td><td>0.03 (-9.55%)</td><td>0.01 <b>(+24.33%)</b></td><td>263.80 (+10.56%)</td><td>187.46 (-7.55%)</td><td>173.60 (-13.07%)</td><td>154.20 (-0.77%)</td><td>44.95 <b>(+38.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>202.78 (n/a)</td><td>199.70 (n/a)</td><td>155.40 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 <b>(+40.72%)</b></td><td>0.04 (+2.69%)</td><td>0.04 (-4.78%)</td><td>0.03 (-17.00%)</td><td>0.01 <b>(+436.74%)</b></td><td>256.50 <b>(+20.48%)</b></td><td>201.66 (+2.53%)</td><td>202.90 (+5.02%)</td><td>133.40 <b>(-28.93%)</b></td><td>49.04 <b>(+359.65%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>196.68 (n/a)</td><td>193.20 (n/a)</td><td>187.70 (n/a)</td><td>10.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52332.50 (n/a)</td><td>52121.36 (n/a)</td><td>52200.10 (n/a)</td><td>51663.00 (n/a)</td><td>267.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.22 (+11.99%)</td><td>0.17 (+0.42%)</td><td>0.15 (-14.76%)</td><td>0.12 (-8.17%)</td><td>0.04 <b>(+60.46%)</b></td><td>204.00 (+8.86%)</td><td>154.12 (+2.56%)</td><td>165.00 (+17.35%)</td><td>112.00 (-10.69%)</td><td>38.22 <b>(+49.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>187.40 (n/a)</td><td>150.28 (n/a)</td><td>140.60 (n/a)</td><td>125.40 (n/a)</td><td>25.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.33 <b>(+21.11%)</b></td><td>0.27 (+5.92%)</td><td>0.26 (+2.23%)</td><td>0.21 (-3.61%)</td><td>0.05 <b>(+170.01%)</b></td><td>191.30 (+3.74%)</td><td>157.74 (-2.93%)</td><td>157.20 (-2.18%)</td><td>124.20 (-17.48%)</td><td>31.78 <b>(+131.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>184.40 (n/a)</td><td>162.50 (n/a)</td><td>160.70 (n/a)</td><td>150.50 (n/a)</td><td>13.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.04 (-4.77%)</td><td>0.03 (-2.18%)</td><td>0.03 (-2.15%)</td><td>0.02 (-8.58%)</td><td>0.01 (+8.65%)</td><td>224.90 (+9.39%)</td><td>167.88 (+3.10%)</td><td>163.70 (+2.18%)</td><td>134.40 (+5.00%)</td><td>35.51 <b>(+25.00%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>162.84 (n/a)</td><td>160.20 (n/a)</td><td>128.00 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 <b>(+23.19%)</b></td><td>0.05 (-0.57%)</td><td>0.04 (-12.07%)</td><td>0.03 (-4.42%)</td><td>0.02 <b>(+73.00%)</b></td><td>243.00 (+4.65%)</td><td>186.02 (+5.81%)</td><td>197.00 (+13.74%)</td><td>102.10 (-18.84%)</td><td>52.54 <b>(+39.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>175.80 (n/a)</td><td>173.20 (n/a)</td><td>125.80 (n/a)</td><td>37.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.10 (-3.66%)</td><td>0.08 (+7.13%)</td><td>0.08 <b>(+20.18%)</b></td><td>0.06 (-12.40%)</td><td>0.02 (+7.51%)</td><td>215.00 (+14.12%)</td><td>159.24 (-5.69%)</td><td>144.90 (-16.77%)</td><td>126.50 (+3.86%)</td><td>35.66 <b>(+31.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>168.84 (n/a)</td><td>174.10 (n/a)</td><td>121.80 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (-9.77%)</td><td>0.05 (+1.55%)</td><td>0.05 (+7.75%)</td><td>0.03 <b>(-31.23%)</b></td><td>0.02 (+17.81%)</td><td>311.70 <b>(+45.38%)</b></td><td>177.78 (+4.69%)</td><td>156.30 (-7.19%)</td><td>124.80 (+10.83%)</td><td>76.86 <b>(+103.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>169.82 (n/a)</td><td>168.40 (n/a)</td><td>112.60 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (+18.73%)</td><td>0.06 <b>(+25.35%)</b></td><td>0.06 <b>(+42.92%)</b></td><td>0.05 <b>(+32.20%)</b></td><td>0.01 (-2.70%)</td><td>201.30 <b>(-24.35%)</b></td><td>169.66 <b>(-21.07%)</b></td><td>159.70 <b>(-30.05%)</b></td><td>143.40 (-15.75%)</td><td>26.08 <b>(-35.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>266.10 (n/a)</td><td>214.96 (n/a)</td><td>228.30 (n/a)</td><td>170.20 (n/a)</td><td>40.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 <b>(+33.19%)</b></td><td>0.06 <b>(+27.54%)</b></td><td>0.06 <b>(+29.49%)</b></td><td>0.04 (+13.94%)</td><td>0.01 <b>(+76.57%)</b></td><td>200.00 (-12.24%)</td><td>149.92 (-19.97%)</td><td>147.00 <b>(-22.79%)</b></td><td>110.80 <b>(-24.93%)</b></td><td>34.05 (+17.86%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>187.32 (n/a)</td><td>190.40 (n/a)</td><td>147.60 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.08 <b>(+40.29%)</b></td><td>0.06 (+19.75%)</td><td>0.06 (+13.75%)</td><td>0.05 (+1.33%)</td><td>0.02 <b>(+299.89%)</b></td><td>212.40 (-1.30%)</td><td>167.84 (-12.59%)</td><td>164.30 (-12.09%)</td><td>125.30 <b>(-28.69%)</b></td><td>41.53 <b>(+179.59%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>192.02 (n/a)</td><td>186.90 (n/a)</td><td>175.70 (n/a)</td><td>14.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+12.84%)</td><td>0.05 (+10.06%)</td><td>0.05 (+16.76%)</td><td>0.03 (-3.85%)</td><td>0.01 <b>(+57.93%)</b></td><td>237.90 (+4.02%)</td><td>172.14 (-6.54%)</td><td>153.70 (-14.33%)</td><td>133.00 (-11.39%)</td><td>45.44 <b>(+43.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>184.18 (n/a)</td><td>179.40 (n/a)</td><td>150.10 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (-3.86%)</td><td>0.05 (+2.08%)</td><td>0.05 (+2.46%)</td><td>0.04 (+0.08%)</td><td>0.01 (-1.71%)</td><td>213.60 (-0.09%)</td><td>182.90 (-1.92%)</td><td>187.60 (-2.39%)</td><td>145.10 (+4.01%)</td><td>29.91 (+7.12%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>186.48 (n/a)</td><td>192.20 (n/a)</td><td>139.50 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (-8.41%)</td><td>0.05 (+3.83%)</td><td>0.06 <b>(+23.05%)</b></td><td>0.04 (-16.52%)</td><td>0.01 (+17.19%)</td><td>224.60 (+19.79%)</td><td>161.06 (-1.68%)</td><td>140.30 (-18.71%)</td><td>129.50 (+9.19%)</td><td>41.24 <b>(+55.84%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>163.82 (n/a)</td><td>172.60 (n/a)</td><td>118.60 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.07 (+15.64%)</td><td>0.06 <b>(+25.32%)</b></td><td>0.06 <b>(+39.63%)</b></td><td>0.05 (+16.53%)</td><td>0.01 (+2.74%)</td><td>203.10 (-14.16%)</td><td>161.06 <b>(-20.68%)</b></td><td>158.10 <b>(-28.36%)</b></td><td>125.70 (-13.49%)</td><td>28.30 <b>(-22.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>203.06 (n/a)</td><td>220.70 (n/a)</td><td>145.30 (n/a)</td><td>36.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (-15.14%)</td><td>0.04 (-3.04%)</td><td>0.04 (-8.85%)</td><td>0.04 <b>(+29.51%)</b></td><td>0.00 <b>(-63.75%)</b></td><td>228.80 <b>(-22.78%)</b></td><td>191.76 (-3.05%)</td><td>187.20 (+9.73%)</td><td>174.80 (+17.87%)</td><td>21.71 <b>(-65.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>296.30 (n/a)</td><td>197.80 (n/a)</td><td>170.60 (n/a)</td><td>148.30 (n/a)</td><td>63.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (+0.35%)</td><td>0.04 (+8.71%)</td><td>0.04 (+10.88%)</td><td>0.04 (+17.04%)</td><td>0.00 <b>(-34.64%)</b></td><td>210.20 (-14.55%)</td><td>194.74 (-8.97%)</td><td>197.10 (-9.84%)</td><td>167.40 (-0.36%)</td><td>16.32 <b>(-43.98%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>213.94 (n/a)</td><td>218.60 (n/a)</td><td>168.00 (n/a)</td><td>29.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+9.34%)</td><td>0.05 (+0.05%)</td><td>0.04 (-1.41%)</td><td>0.04 (-4.76%)</td><td>0.01 <b>(+22.09%)</b></td><td>221.80 (+4.97%)</td><td>180.28 (+0.66%)</td><td>186.30 (+1.47%)</td><td>139.00 (-8.55%)</td><td>30.32 (+18.62%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>179.10 (n/a)</td><td>183.60 (n/a)</td><td>152.00 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.06 (+13.05%)</td><td>0.04 (-0.10%)</td><td>0.05 (+11.56%)</td><td>0.03 <b>(-23.37%)</b></td><td>0.01 <b>(+77.89%)</b></td><td>286.90 <b>(+30.53%)</b></td><td>206.84 (+3.45%)</td><td>193.40 (-10.38%)</td><td>148.10 (-11.53%)</td><td>51.07 <b>(+106.29%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>199.94 (n/a)</td><td>215.80 (n/a)</td><td>167.40 (n/a)</td><td>24.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.05 (+10.24%)</td><td>0.04 (-3.32%)</td><td>0.04 (-2.65%)</td><td>0.03 <b>(-25.72%)</b></td><td>0.01 <b>(+136.48%)</b></td><td>327.70 <b>(+34.63%)</b></td><td>234.24 (+7.19%)</td><td>227.20 (+2.71%)</td><td>176.50 (-9.30%)</td><td>57.00 <b>(+198.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>243.40 (n/a)</td><td>218.52 (n/a)</td><td>221.20 (n/a)</td><td>194.60 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.72 (-4.19%)</td><td>0.57 (-5.49%)</td><td>0.53 (-15.39%)</td><td>0.48 <b>(+23.27%)</b></td><td>0.10 <b>(-27.35%)</b></td><td>204.60 (-18.87%)</td><td>174.92 (+2.82%)</td><td>186.20 (+18.15%)</td><td>136.40 (+4.36%)</td><td>27.69 <b>(-41.87%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.62 (n/a)</td><td>0.39 (n/a)</td><td>0.14 (n/a)</td><td>252.20 (n/a)</td><td>170.12 (n/a)</td><td>157.60 (n/a)</td><td>130.70 (n/a)</td><td>47.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.81 (-6.00%)</td><td>0.62 (-5.89%)</td><td>0.61 (+1.05%)</td><td>0.47 (-19.44%)</td><td>0.13 (+9.05%)</td><td>210.50 <b>(+24.12%)</b></td><td>164.88 (+7.53%)</td><td>160.70 (-1.05%)</td><td>121.30 (+6.40%)</td><td>33.00 <b>(+46.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.86 (n/a)</td><td>0.65 (n/a)</td><td>0.61 (n/a)</td><td>0.58 (n/a)</td><td>0.12 (n/a)</td><td>169.60 (n/a)</td><td>153.34 (n/a)</td><td>162.40 (n/a)</td><td>114.00 (n/a)</td><td>22.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.65 <b>(-22.86%)</b></td><td>0.59 (-4.82%)</td><td>0.60 (-3.17%)</td><td>0.50 (+1.84%)</td><td>0.06 <b>(-59.36%)</b></td><td>197.80 (-1.79%)</td><td>167.42 (+1.71%)</td><td>164.10 (+3.27%)</td><td>150.20 <b>(+29.59%)</b></td><td>18.33 <b>(-48.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.85 (n/a)</td><td>0.62 (n/a)</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.15 (n/a)</td><td>201.40 (n/a)</td><td>164.60 (n/a)</td><td>158.90 (n/a)</td><td>115.90 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.53 (-19.77%)</td><td>0.47 (-19.89%)</td><td>0.47 <b>(-25.70%)</b></td><td>0.40 (-16.98%)</td><td>0.05 <b>(-41.98%)</b></td><td>246.30 <b>(+20.44%)</b></td><td>212.40 <b>(+23.75%)</b></td><td>210.90 <b>(+34.59%)</b></td><td>185.40 <b>(+24.68%)</b></td><td>22.78 (-12.78%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.63 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>204.50 (n/a)</td><td>171.64 (n/a)</td><td>156.70 (n/a)</td><td>148.70 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.48 (-19.25%)</td><td>0.42 (+0.40%)</td><td>0.44 (+6.22%)</td><td>0.33 <b>(+21.54%)</b></td><td>0.06 <b>(-53.69%)</b></td><td>223.00 (-17.71%)</td><td>177.32 (-5.59%)</td><td>167.80 (-5.89%)</td><td>152.60 <b>(+23.86%)</b></td><td>27.09 <b>(-51.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.60 (n/a)</td><td>0.42 (n/a)</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>271.00 (n/a)</td><td>187.82 (n/a)</td><td>178.30 (n/a)</td><td>123.20 (n/a)</td><td>56.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.46 <b>(-28.41%)</b></td><td>0.38 <b>(-21.72%)</b></td><td>0.36 <b>(-22.05%)</b></td><td>0.32 (-17.21%)</td><td>0.06 <b>(-38.79%)</b></td><td>229.50 <b>(+20.79%)</b></td><td>197.08 <b>(+26.53%)</b></td><td>206.30 <b>(+28.30%)</b></td><td>159.50 <b>(+39.67%)</b></td><td>29.05 (+5.97%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.65 (n/a)</td><td>0.49 (n/a)</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>190.00 (n/a)</td><td>155.76 (n/a)</td><td>160.80 (n/a)</td><td>114.20 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.51 (-3.70%)</td><td>0.39 (-14.43%)</td><td>0.36 <b>(-25.73%)</b></td><td>0.32 (-7.75%)</td><td>0.08 (+5.40%)</td><td>231.20 (+8.39%)</td><td>195.28 (+17.67%)</td><td>205.50 <b>(+34.67%)</b></td><td>145.40 (+3.86%)</td><td>37.46 <b>(+20.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>213.30 (n/a)</td><td>165.96 (n/a)</td><td>152.60 (n/a)</td><td>140.00 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.39 <b>(-25.76%)</b></td><td>0.36 (-16.42%)</td><td>0.36 (-16.94%)</td><td>0.32 (+0.67%)</td><td>0.03 <b>(-69.70%)</b></td><td>231.10 (-0.64%)</td><td>207.98 (+16.15%)</td><td>206.60 <b>(+20.40%)</b></td><td>188.70 <b>(+34.69%)</b></td><td>15.39 <b>(-59.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>232.60 (n/a)</td><td>179.06 (n/a)</td><td>171.60 (n/a)</td><td>140.10 (n/a)</td><td>37.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.97 <b>(-21.52%)</b></td><td>0.78 (+0.96%)</td><td>0.86 <b>(+32.48%)</b></td><td>0.57 (+0.18%)</td><td>0.18 <b>(-34.07%)</b></td><td>231.90 (-0.17%)</td><td>175.60 (-4.34%)</td><td>152.30 <b>(-24.53%)</b></td><td>134.80 <b>(+27.41%)</b></td><td>44.56 (-14.56%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.24 (n/a)</td><td>0.78 (n/a)</td><td>0.65 (n/a)</td><td>0.56 (n/a)</td><td>0.28 (n/a)</td><td>232.30 (n/a)</td><td>183.56 (n/a)</td><td>201.80 (n/a)</td><td>105.80 (n/a)</td><td>52.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.91 (-10.71%)</td><td>0.81 (-0.68%)</td><td>0.80 (-0.42%)</td><td>0.72 (+14.64%)</td><td>0.08 <b>(-46.64%)</b></td><td>181.20 (-12.76%)</td><td>163.64 (-1.12%)</td><td>164.80 (+0.43%)</td><td>143.30 (+12.04%)</td><td>15.42 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.63 (n/a)</td><td>0.15 (n/a)</td><td>207.70 (n/a)</td><td>165.50 (n/a)</td><td>164.10 (n/a)</td><td>127.90 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.92 (-18.71%)</td><td>0.82 (+3.33%)</td><td>0.89 <b>(+23.32%)</b></td><td>0.66 (+14.86%)</td><td>0.12 <b>(-42.40%)</b></td><td>198.10 (-12.96%)</td><td>162.92 (-6.22%)</td><td>147.10 (-18.91%)</td><td>142.70 <b>(+23.02%)</b></td><td>25.76 <b>(-37.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.13 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.58 (n/a)</td><td>0.21 (n/a)</td><td>227.60 (n/a)</td><td>173.72 (n/a)</td><td>181.40 (n/a)</td><td>116.00 (n/a)</td><td>41.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (-6.85%)</td><td>0.02 (+12.78%)</td><td>0.02 <b>(+22.15%)</b></td><td>0.02 <b>(+30.59%)</b></td><td>0.00 <b>(-61.36%)</b></td><td>185.90 <b>(-23.43%)</b></td><td>171.98 (-14.28%)</td><td>169.80 (-18.13%)</td><td>158.40 (+7.32%)</td><td>13.34 <b>(-68.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.80 (n/a)</td><td>200.62 (n/a)</td><td>207.40 (n/a)</td><td>147.60 (n/a)</td><td>42.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (-11.90%)</td><td>0.02 (-8.21%)</td><td>0.02 (-3.99%)</td><td>0.02 (-8.73%)</td><td>0.00 (-11.45%)</td><td>200.70 (+9.55%)</td><td>174.74 (+8.97%)</td><td>173.80 (+4.20%)</td><td>147.60 (+13.54%)</td><td>22.62 (+12.53%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.20 (n/a)</td><td>160.36 (n/a)</td><td>166.80 (n/a)</td><td>130.00 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (-2.80%)</td><td>0.02 <b>(-20.70%)</b></td><td>0.02 (-19.06%)</td><td>0.01 <b>(-41.07%)</b></td><td>0.01 <b>(+91.37%)</b></td><td>370.80 <b>(+69.70%)</b></td><td>255.12 <b>(+40.64%)</b></td><td>212.10 <b>(+23.53%)</b></td><td>155.10 (+2.85%)</td><td>103.71 <b>(+251.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.50 (n/a)</td><td>181.40 (n/a)</td><td>171.70 (n/a)</td><td>150.80 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>1.00 (-15.06%)</td><td>0.89 (+1.03%)</td><td>0.92 (+9.63%)</td><td>0.74 <b>(+36.94%)</b></td><td>0.11 <b>(-56.64%)</b></td><td>178.00 <b>(-26.96%)</b></td><td>149.54 (-6.67%)</td><td>143.60 (-8.77%)</td><td>132.60 (+17.76%)</td><td>18.81 <b>(-63.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.17 (n/a)</td><td>0.88 (n/a)</td><td>0.84 (n/a)</td><td>0.54 (n/a)</td><td>0.24 (n/a)</td><td>243.70 (n/a)</td><td>160.22 (n/a)</td><td>157.40 (n/a)</td><td>112.60 (n/a)</td><td>51.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.95 (-8.40%)</td><td>0.80 (-7.70%)</td><td>0.90 (+7.71%)</td><td>0.61 (-15.23%)</td><td>0.17 <b>(+33.04%)</b></td><td>215.30 (+17.97%)</td><td>172.08 (+10.82%)</td><td>147.50 (-7.12%)</td><td>139.60 (+9.23%)</td><td>39.24 <b>(+76.13%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>0.83 (n/a)</td><td>0.72 (n/a)</td><td>0.13 (n/a)</td><td>182.50 (n/a)</td><td>155.28 (n/a)</td><td>158.80 (n/a)</td><td>127.80 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.85 (-2.17%)</td><td>0.65 (-12.83%)</td><td>0.61 <b>(-23.95%)</b></td><td>0.52 (-1.84%)</td><td>0.14 (-4.08%)</td><td>254.80 (+1.88%)</td><td>209.74 (+14.57%)</td><td>215.60 <b>(+31.46%)</b></td><td>154.90 (+2.24%)</td><td>41.69 (+0.87%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.87 (n/a)</td><td>0.75 (n/a)</td><td>0.81 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>250.10 (n/a)</td><td>183.06 (n/a)</td><td>164.00 (n/a)</td><td>151.50 (n/a)</td><td>41.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.89 (-12.80%)</td><td>0.76 (-13.40%)</td><td>0.78 (-18.08%)</td><td>0.64 (+3.51%)</td><td>0.09 <b>(-43.25%)</b></td><td>207.40 (-3.36%)</td><td>174.74 (+13.07%)</td><td>170.30 <b>(+22.08%)</b></td><td>148.70 (+14.74%)</td><td>21.46 <b>(-38.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>0.95 (n/a)</td><td>0.62 (n/a)</td><td>0.16 (n/a)</td><td>214.60 (n/a)</td><td>154.54 (n/a)</td><td>139.50 (n/a)</td><td>129.60 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.97 (-6.46%)</td><td>0.86 (-5.91%)</td><td>0.89 (-8.61%)</td><td>0.62 (+0.19%)</td><td>0.14 (-19.44%)</td><td>211.90 (-0.19%)</td><td>157.38 (+5.17%)</td><td>148.80 (+9.49%)</td><td>136.00 (+6.92%)</td><td>31.09 (-13.12%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.04 (n/a)</td><td>0.92 (n/a)</td><td>0.97 (n/a)</td><td>0.62 (n/a)</td><td>0.17 (n/a)</td><td>212.30 (n/a)</td><td>149.64 (n/a)</td><td>135.90 (n/a)</td><td>127.20 (n/a)</td><td>35.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.03 (-14.83%)</td><td>0.02 (+0.42%)</td><td>0.02 (+2.10%)</td><td>0.02 <b>(+26.12%)</b></td><td>0.00 <b>(-49.84%)</b></td><td>210.50 <b>(-20.69%)</b></td><td>180.66 (-4.64%)</td><td>185.10 (-2.06%)</td><td>146.80 (+17.44%)</td><td>23.41 <b>(-53.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>265.40 (n/a)</td><td>189.46 (n/a)</td><td>189.00 (n/a)</td><td>125.00 (n/a)</td><td>50.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.02 <b>(-35.31%)</b></td><td>0.02 (-13.75%)</td><td>0.02 (-0.50%)</td><td>0.02 (-8.78%)</td><td>0.00 <b>(-63.75%)</b></td><td>220.00 (+9.62%)</td><td>194.08 (+11.80%)</td><td>186.20 (+0.49%)</td><td>173.00 <b>(+54.60%)</b></td><td>23.00 <b>(-37.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>173.60 (n/a)</td><td>185.30 (n/a)</td><td>111.90 (n/a)</td><td>36.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.00 (-2.27%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-8.14%)</td><td>1052.30 (-0.28%)</td><td>982.88 (+0.24%)</td><td>969.44 (-0.10%)</td><td>958.54 (+2.02%)</td><td>39.10 (-10.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1055.28 (n/a)</td><td>980.48 (n/a)</td><td>970.45 (n/a)</td><td>939.58 (n/a)</td><td>43.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.01 (+2.38%)</td><td>0.01 (+0.25%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(+40.04%)</b></td><td>1093.24 (+0.45%)</td><td>1029.03 (-0.11%)</td><td>1023.25 (-0.52%)</td><td>948.98 (-2.90%)</td><td>60.24 <b>(+51.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1088.29 (n/a)</td><td>1030.13 (n/a)</td><td>1028.58 (n/a)</td><td>977.31 (n/a)</td><td>39.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.98 (-1.28%)</td><td>0.97 (-0.41%)</td><td>0.96 (+0.71%)</td><td>0.96 (+0.27%)</td><td>0.01 <b>(-56.01%)</b></td><td>2195.14 (-0.26%)</td><td>2172.30 (+0.38%)</td><td>2176.20 (-0.70%)</td><td>2140.29 (+1.29%)</td><td>20.15 <b>(-55.42%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.99 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2200.97 (n/a)</td><td>2164.06 (n/a)</td><td>2191.59 (n/a)</td><td>2113.01 (n/a)</td><td>45.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.57 <b>(+24.15%)</b></td><td>2.93 (+14.60%)</td><td>2.99 (+17.57%)</td><td>2.25 (-1.72%)</td><td>0.47 <b>(+117.98%)</b></td><td>232.60 (+1.75%)</td><td>182.92 (-11.30%)</td><td>175.30 (-14.94%)</td><td>146.90 (-19.46%)</td><td>31.36 <b>(+82.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.87 (n/a)</td><td>2.56 (n/a)</td><td>2.54 (n/a)</td><td>2.29 (n/a)</td><td>0.22 (n/a)</td><td>228.60 (n/a)</td><td>206.22 (n/a)</td><td>206.10 (n/a)</td><td>182.40 (n/a)</td><td>17.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>5.38 (-6.94%)</td><td>4.54 (-9.80%)</td><td>4.58 (-4.09%)</td><td>4.05 (-12.04%)</td><td>0.53 (+10.66%)</td><td>258.70 (+13.71%)</td><td>233.40 (+11.25%)</td><td>229.20 (+4.28%)</td><td>195.00 (+7.44%)</td><td>25.63 <b>(+36.31%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>5.78 (n/a)</td><td>5.03 (n/a)</td><td>4.77 (n/a)</td><td>4.61 (n/a)</td><td>0.48 (n/a)</td><td>227.50 (n/a)</td><td>209.80 (n/a)</td><td>219.80 (n/a)</td><td>181.50 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>3.07 (+5.76%)</td><td>2.77 (+3.59%)</td><td>2.84 (+7.58%)</td><td>2.21 (-9.56%)</td><td>0.33 <b>(+53.61%)</b></td><td>237.40 (+10.57%)</td><td>191.54 (-2.69%)</td><td>184.80 (-7.09%)</td><td>170.80 (-5.43%)</td><td>26.37 <b>(+67.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.90 (n/a)</td><td>2.68 (n/a)</td><td>2.64 (n/a)</td><td>2.44 (n/a)</td><td>0.22 (n/a)</td><td>214.70 (n/a)</td><td>196.84 (n/a)</td><td>198.90 (n/a)</td><td>180.60 (n/a)</td><td>15.79 (n/a)</td>
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
