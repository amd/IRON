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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.10 (+19.70%)</td><td>0.08 (-0.65%)</td><td>0.08 (-2.61%)</td><td>0.05 <b>(-26.90%)</b></td><td>0.02 <b>(+273.22%)</b></td><td>234.00 <b>(+36.84%)</b></td><td>170.80 (+7.87%)</td><td>161.70 (+2.67%)</td><td>120.00 (-16.43%)</td><td>51.86 <b>(+315.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>171.00 (n/a)</td><td>158.34 (n/a)</td><td>157.50 (n/a)</td><td>143.60 (n/a)</td><td>12.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.09 (-4.97%)</td><td>0.08 (+1.28%)</td><td>0.08 (+2.88%)</td><td>0.06 (+18.35%)</td><td>0.01 <b>(-32.41%)</b></td><td>197.20 (-15.51%)</td><td>162.08 (-3.56%)</td><td>154.50 (-2.83%)</td><td>135.80 (+5.27%)</td><td>23.69 <b>(-40.85%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.40 (n/a)</td><td>168.06 (n/a)</td><td>159.00 (n/a)</td><td>129.00 (n/a)</td><td>40.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.11 <b>(+42.75%)</b></td><td>0.08 (+12.07%)</td><td>0.07 (+2.33%)</td><td>0.06 (+4.28%)</td><td>0.02 <b>(+161.57%)</b></td><td>207.60 (-4.11%)</td><td>167.58 (-8.05%)</td><td>169.80 (-2.25%)</td><td>114.00 <b>(-29.98%)</b></td><td>33.96 <b>(+64.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>182.26 (n/a)</td><td>173.70 (n/a)</td><td>162.80 (n/a)</td><td>20.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.09 (+16.45%)</td><td>0.08 (+16.73%)</td><td>0.07 <b>(+21.31%)</b></td><td>0.06 (+6.59%)</td><td>0.01 <b>(+35.12%)</b></td><td>197.20 (-6.18%)</td><td>162.24 (-13.85%)</td><td>164.90 (-17.55%)</td><td>136.80 (-14.07%)</td><td>24.42 (+7.32%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>188.32 (n/a)</td><td>200.00 (n/a)</td><td>159.20 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (-1.50%)</td><td>0.03 (+17.86%)</td><td>0.03 (+8.26%)</td><td>0.03 <b>(+81.07%)</b></td><td>0.00 <b>(-64.74%)</b></td><td>184.70 <b>(-44.75%)</b></td><td>164.28 <b>(-21.36%)</b></td><td>161.20 (-7.67%)</td><td>150.90 (+1.55%)</td><td>14.26 <b>(-80.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.30 (n/a)</td><td>208.90 (n/a)</td><td>174.60 (n/a)</td><td>148.60 (n/a)</td><td>74.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (+16.92%)</td><td>0.04 (+5.72%)</td><td>0.04 (+1.32%)</td><td>0.03 <b>(+26.09%)</b></td><td>0.01 (+11.65%)</td><td>177.90 <b>(-20.69%)</b></td><td>149.34 (-5.96%)</td><td>146.10 (-1.35%)</td><td>113.00 (-14.46%)</td><td>27.85 <b>(-25.30%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>158.80 (n/a)</td><td>148.10 (n/a)</td><td>132.10 (n/a)</td><td>37.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 <b>(+30.90%)</b></td><td>0.04 (+18.50%)</td><td>0.03 (+4.20%)</td><td>0.03 <b>(+25.10%)</b></td><td>0.01 <b>(+37.56%)</b></td><td>177.10 <b>(-20.08%)</b></td><td>149.04 (-15.34%)</td><td>158.50 (-4.06%)</td><td>104.90 <b>(-23.60%)</b></td><td>27.88 (-19.37%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>176.04 (n/a)</td><td>165.20 (n/a)</td><td>137.30 (n/a)</td><td>34.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (+16.94%)</td><td>0.03 (+8.23%)</td><td>0.03 (-5.40%)</td><td>0.03 (+2.71%)</td><td>0.01 <b>(+50.69%)</b></td><td>207.20 (-2.63%)</td><td>163.98 (-5.18%)</td><td>183.00 (+5.72%)</td><td>114.20 (-14.46%)</td><td>41.31 <b>(+23.43%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>172.94 (n/a)</td><td>173.10 (n/a)</td><td>133.50 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 <b>(+24.80%)</b></td><td>0.03 (+0.66%)</td><td>0.03 (+6.29%)</td><td>0.02 <b>(-35.96%)</b></td><td>0.01 <b>(+195.88%)</b></td><td>336.00 <b>(+56.13%)</b></td><td>201.58 (+9.69%)</td><td>171.00 (-5.89%)</td><td>124.80 (-19.85%)</td><td>81.52 <b>(+285.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>215.20 (n/a)</td><td>183.78 (n/a)</td><td>181.70 (n/a)</td><td>155.70 (n/a)</td><td>21.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 <b>(-23.38%)</b></td><td>0.03 (-11.54%)</td><td>0.03 (-7.52%)</td><td>0.03 (+9.98%)</td><td>0.00 <b>(-64.70%)</b></td><td>203.90 (-9.09%)</td><td>188.40 (+9.48%)</td><td>191.60 (+8.13%)</td><td>162.90 <b>(+30.53%)</b></td><td>15.21 <b>(-58.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>172.08 (n/a)</td><td>177.20 (n/a)</td><td>124.80 (n/a)</td><td>36.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 <b>(-22.23%)</b></td><td>0.03 (+0.09%)</td><td>0.03 (+1.33%)</td><td>0.03 (+15.03%)</td><td>0.00 <b>(-59.13%)</b></td><td>189.90 (-13.09%)</td><td>167.98 (-4.76%)</td><td>174.10 (-1.30%)</td><td>140.80 <b>(+28.58%)</b></td><td>19.92 <b>(-53.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>176.38 (n/a)</td><td>176.40 (n/a)</td><td>109.50 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 <b>(+21.63%)</b></td><td>0.03 (+18.05%)</td><td>0.03 (+13.07%)</td><td>0.02 (+8.41%)</td><td>0.00 <b>(+96.52%)</b></td><td>230.20 (-7.77%)</td><td>195.34 (-14.48%)</td><td>204.00 (-11.54%)</td><td>167.40 (-17.78%)</td><td>26.43 <b>(+45.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>249.60 (n/a)</td><td>228.42 (n/a)</td><td>230.60 (n/a)</td><td>203.60 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>159.70 (n/a)</td><td>165.50 (n/a)</td><td>119.90 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>178.80 (n/a)</td><td>177.00 (n/a)</td><td>154.40 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>178.28 (n/a)</td><td>171.40 (n/a)</td><td>151.80 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>203.04 (n/a)</td><td>198.90 (n/a)</td><td>192.00 (n/a)</td><td>13.00 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.60 (n/a)</td><td>176.18 (n/a)</td><td>170.30 (n/a)</td><td>157.50 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>176.48 (n/a)</td><td>175.50 (n/a)</td><td>136.30 (n/a)</td><td>35.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>205.80 (n/a)</td><td>162.42 (n/a)</td><td>168.10 (n/a)</td><td>114.00 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>354.70 (n/a)</td><td>249.84 (n/a)</td><td>227.80 (n/a)</td><td>166.50 (n/a)</td><td>79.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.63 (+11.58%)</td><td>3.13 (+3.52%)</td><td>3.10 (-0.25%)</td><td>2.88 (+5.22%)</td><td>0.30 <b>(+21.78%)</b></td><td>477.60 (-4.96%)</td><td>442.20 (-3.25%)</td><td>443.70 (+0.25%)</td><td>378.90 (-10.36%)</td><td>39.96 (+3.77%)</td><td>708.50 (+11.58%)</td><td>611.35 (+3.52%)</td><td>605.02 (-0.25%)</td><td>562.07 (+5.22%)</td><td>59.32 <b>(+21.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.26 (n/a)</td><td>3.03 (n/a)</td><td>3.11 (n/a)</td><td>2.74 (n/a)</td><td>0.25 (n/a)</td><td>502.50 (n/a)</td><td>457.06 (n/a)</td><td>442.60 (n/a)</td><td>422.70 (n/a)</td><td>38.51 (n/a)</td><td>634.98 (n/a)</td><td>590.57 (n/a)</td><td>606.52 (n/a)</td><td>534.17 (n/a)</td><td>48.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>5.36 (+9.59%)</td><td>4.46 (+14.11%)</td><td>4.30 (+17.18%)</td><td>3.85 (+9.93%)</td><td>0.67 (+17.52%)</td><td>357.90 (-9.05%)</td><td>313.94 (-12.13%)</td><td>319.90 (-14.65%)</td><td>256.90 (-8.74%)</td><td>45.65 (+0.24%)</td><td>1045.06 (+9.59%)</td><td>870.34 (+14.11%)</td><td>839.17 (+17.18%)</td><td>749.97 (+9.93%)</td><td>131.21 (+17.52%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.89 (n/a)</td><td>3.91 (n/a)</td><td>3.67 (n/a)</td><td>3.50 (n/a)</td><td>0.57 (n/a)</td><td>393.50 (n/a)</td><td>357.28 (n/a)</td><td>374.80 (n/a)</td><td>281.50 (n/a)</td><td>45.54 (n/a)</td><td>953.64 (n/a)</td><td>762.72 (n/a)</td><td>716.16 (n/a)</td><td>682.21 (n/a)</td><td>111.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.86 <b>(+31.36%)</b></td><td>4.74 (+12.90%)</td><td>4.11 (+7.33%)</td><td>3.40 (-5.79%)</td><td>1.42 <b>(+96.69%)</b></td><td>405.10 (+6.13%)</td><td>310.08 (-7.57%)</td><td>334.70 (-6.85%)</td><td>200.50 <b>(-23.88%)</b></td><td>82.55 <b>(+54.83%)</b></td><td>1339.00 <b>(+31.36%)</b></td><td>923.55 (+12.90%)</td><td>801.92 (+7.33%)</td><td>662.61 (-5.79%)</td><td>276.26 <b>(+96.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>5.23 (n/a)</td><td>4.19 (n/a)</td><td>3.83 (n/a)</td><td>3.61 (n/a)</td><td>0.72 (n/a)</td><td>381.70 (n/a)</td><td>335.46 (n/a)</td><td>359.30 (n/a)</td><td>263.40 (n/a)</td><td>53.32 (n/a)</td><td>1019.31 (n/a)</td><td>818.04 (n/a)</td><td>747.16 (n/a)</td><td>703.34 (n/a)</td><td>140.45 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.30 (-11.87%)</td><td>4.10 (-3.32%)</td><td>3.86 (+7.11%)</td><td>3.13 (-4.08%)</td><td>1.27 <b>(-22.05%)</b></td><td>439.00 (+4.25%)</td><td>356.96 (+1.14%)</td><td>356.50 (-6.65%)</td><td>218.40 (+13.45%)</td><td>85.53 (-6.32%)</td><td>1228.82 (-11.87%)</td><td>798.83 (-3.32%)</td><td>752.97 (+7.11%)</td><td>611.47 (-4.08%)</td><td>248.55 <b>(-22.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>7.15 (n/a)</td><td>4.24 (n/a)</td><td>3.60 (n/a)</td><td>3.27 (n/a)</td><td>1.63 (n/a)</td><td>421.10 (n/a)</td><td>352.94 (n/a)</td><td>381.90 (n/a)</td><td>192.50 (n/a)</td><td>91.30 (n/a)</td><td>1394.35 (n/a)</td><td>826.26 (n/a)</td><td>702.97 (n/a)</td><td>637.47 (n/a)</td><td>318.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.68 (-3.61%)</td><td>3.23 (-2.11%)</td><td>3.15 (+0.11%)</td><td>3.02 (-1.17%)</td><td>0.27 (-12.23%)</td><td>455.00 (+1.20%)</td><td>428.32 (+2.04%)</td><td>437.40 (-0.11%)</td><td>373.80 (+3.75%)</td><td>33.49 (-7.24%)</td><td>718.09 (-3.61%)</td><td>630.03 (-2.11%)</td><td>613.71 (+0.11%)</td><td>590.02 (-1.17%)</td><td>52.92 (-12.23%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.82 (n/a)</td><td>3.30 (n/a)</td><td>3.14 (n/a)</td><td>3.06 (n/a)</td><td>0.31 (n/a)</td><td>449.60 (n/a)</td><td>419.74 (n/a)</td><td>437.90 (n/a)</td><td>360.30 (n/a)</td><td>36.11 (n/a)</td><td>744.98 (n/a)</td><td>643.64 (n/a)</td><td>613.03 (n/a)</td><td>597.02 (n/a)</td><td>60.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.52 <b>(+31.24%)</b></td><td>1.52 <b>(+22.87%)</b></td><td>1.14 (+3.88%)</td><td>1.08 (+13.70%)</td><td>0.63 <b>(+57.67%)</b></td><td>372.60 (-12.06%)</td><td>295.58 (-14.71%)</td><td>353.00 (-3.74%)</td><td>159.20 <b>(-23.79%)</b></td><td>95.60 (+13.15%)</td><td>210.82 <b>(+31.24%)</b></td><td>126.81 <b>(+22.87%)</b></td><td>95.06 (+3.88%)</td><td>90.04 (+13.70%)</td><td>52.31 <b>(+57.67%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.92 (n/a)</td><td>1.23 (n/a)</td><td>1.09 (n/a)</td><td>0.95 (n/a)</td><td>0.40 (n/a)</td><td>423.70 (n/a)</td><td>346.54 (n/a)</td><td>366.70 (n/a)</td><td>208.90 (n/a)</td><td>84.49 (n/a)</td><td>160.63 (n/a)</td><td>103.20 (n/a)</td><td>91.50 (n/a)</td><td>79.20 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>8.83 <b>(+37.76%)</b></td><td>6.42 <b>(+20.79%)</b></td><td>6.09 (+18.84%)</td><td>4.83 (+4.94%)</td><td>1.60 <b>(+102.62%)</b></td><td>400.70 (-4.69%)</td><td>315.38 (-14.76%)</td><td>317.40 (-15.85%)</td><td>218.90 <b>(-27.40%)</b></td><td>72.40 <b>(+37.81%)</b></td><td>1839.62 <b>(+37.76%)</b></td><td>1336.93 <b>(+20.79%)</b></td><td>1268.56 (+18.84%)</td><td>1004.98 (+4.94%)</td><td>332.71 <b>(+102.62%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.41 (n/a)</td><td>5.31 (n/a)</td><td>5.13 (n/a)</td><td>4.60 (n/a)</td><td>0.79 (n/a)</td><td>420.40 (n/a)</td><td>369.98 (n/a)</td><td>377.20 (n/a)</td><td>301.50 (n/a)</td><td>52.54 (n/a)</td><td>1335.39 (n/a)</td><td>1106.84 (n/a)</td><td>1067.43 (n/a)</td><td>957.69 (n/a)</td><td>164.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>16.29 (-12.70%)</td><td>12.41 (-9.33%)</td><td>11.54 (-14.15%)</td><td>11.07 (-0.89%)</td><td>2.18 <b>(-26.33%)</b></td><td>497.30 (+0.91%)</td><td>452.58 (+9.01%)</td><td>477.10 (+16.48%)</td><td>338.00 (+14.54%)</td><td>64.77 (-15.32%)</td><td>6353.71 (-12.70%)</td><td>4842.33 (-9.33%)</td><td>4501.35 (-14.15%)</td><td>4318.60 (-0.89%)</td><td>849.42 <b>(-26.33%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>18.66 (n/a)</td><td>13.69 (n/a)</td><td>13.44 (n/a)</td><td>11.17 (n/a)</td><td>2.96 (n/a)</td><td>492.80 (n/a)</td><td>415.18 (n/a)</td><td>409.60 (n/a)</td><td>295.10 (n/a)</td><td>76.49 (n/a)</td><td>7277.83 (n/a)</td><td>5340.51 (n/a)</td><td>5243.39 (n/a)</td><td>4357.56 (n/a)</td><td>1153.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>169.82 (n/a)</td><td>170.90 (n/a)</td><td>142.00 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.40 (n/a)</td><td>161.72 (n/a)</td><td>160.80 (n/a)</td><td>151.30 (n/a)</td><td>10.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.60 (n/a)</td><td>188.58 (n/a)</td><td>162.80 (n/a)</td><td>153.10 (n/a)</td><td>61.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>150.34 (n/a)</td><td>147.40 (n/a)</td><td>115.80 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>157.16 (n/a)</td><td>143.20 (n/a)</td><td>129.40 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>177.88 (n/a)</td><td>183.40 (n/a)</td><td>137.30 (n/a)</td><td>26.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>176.10 (n/a)</td><td>178.80 (n/a)</td><td>130.50 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>217.66 (n/a)</td><td>224.20 (n/a)</td><td>168.80 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>4.19 (-15.21%)</td><td>4.02 (-10.41%)</td><td>4.18 (-2.17%)</td><td>3.39 (-16.38%)</td><td>0.35 (-15.28%)</td><td>2777.20 (+19.59%)</td><td>2357.96 (+11.65%)</td><td>2250.70 (+2.22%)</td><td>2245.90 (+17.94%)</td><td>234.55 <b>(+22.13%)</b></td><td>1647.14 (-15.21%)</td><td>1579.92 (-10.41%)</td><td>1643.68 (-2.17%)</td><td>1332.05 (-16.38%)</td><td>138.73 (-15.28%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.94 (n/a)</td><td>4.48 (n/a)</td><td>4.27 (n/a)</td><td>4.05 (n/a)</td><td>0.42 (n/a)</td><td>2322.30 (n/a)</td><td>2111.92 (n/a)</td><td>2201.80 (n/a)</td><td>1904.30 (n/a)</td><td>192.05 (n/a)</td><td>1942.62 (n/a)</td><td>1763.57 (n/a)</td><td>1680.19 (n/a)</td><td>1592.99 (n/a)</td><td>163.76 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.21 (-0.02%)</td><td>0.98 (-9.37%)</td><td>1.15 (+12.93%)</td><td>0.63 <b>(-37.07%)</b></td><td>0.28 <b>(+199.19%)</b></td><td>348.90 <b>(+58.88%)</b></td><td>243.68 (+18.25%)</td><td>191.50 (-11.47%)</td><td>182.60 (+0.05%)</td><td>78.03 <b>(+362.02%)</b></td><td>51.69 (-0.02%)</td><td>41.74 (-9.37%)</td><td>49.27 (+12.93%)</td><td>27.05 <b>(-37.07%)</b></td><td>11.79 <b>(+199.19%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.21 (n/a)</td><td>1.08 (n/a)</td><td>1.02 (n/a)</td><td>1.01 (n/a)</td><td>0.09 (n/a)</td><td>219.60 (n/a)</td><td>206.08 (n/a)</td><td>216.30 (n/a)</td><td>182.50 (n/a)</td><td>16.89 (n/a)</td><td>51.71 (n/a)</td><td>46.05 (n/a)</td><td>43.63 (n/a)</td><td>42.98 (n/a)</td><td>3.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.20 (-5.41%)</td><td>0.98 (+0.22%)</td><td>1.01 (+5.94%)</td><td>0.63 (-7.99%)</td><td>0.22 (+0.88%)</td><td>352.00 (+8.68%)</td><td>237.62 (+0.64%)</td><td>219.50 (-5.59%)</td><td>184.30 (+5.68%)</td><td>66.30 (+19.38%)</td><td>51.19 (-5.41%)</td><td>41.74 (+0.22%)</td><td>42.99 (+5.94%)</td><td>26.81 (-7.99%)</td><td>9.21 (+0.88%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.27 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.68 (n/a)</td><td>0.21 (n/a)</td><td>323.90 (n/a)</td><td>236.12 (n/a)</td><td>232.50 (n/a)</td><td>174.40 (n/a)</td><td>55.54 (n/a)</td><td>54.12 (n/a)</td><td>41.65 (n/a)</td><td>40.58 (n/a)</td><td>29.14 (n/a)</td><td>9.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (+0.08%)</td><td>0.53 (+0.00%)</td><td>0.53 (-0.01%)</td><td>0.53 (-0.04%)</td><td>0.00 (+12.95%)</td><td>47850.00 (+0.04%)</td><td>47731.80 (-0.00%)</td><td>47795.00 (+0.01%)</td><td>47421.80 (-0.08%)</td><td>175.37 (+12.89%)</td><td>362.28 (+0.08%)</td><td>359.93 (+0.00%)</td><td>359.45 (-0.01%)</td><td>359.04 (-0.04%)</td><td>1.33 (+12.95%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47828.70 (n/a)</td><td>47733.52 (n/a)</td><td>47789.70 (n/a)</td><td>47458.10 (n/a)</td><td>155.34 (n/a)</td><td>362.00 (n/a)</td><td>359.92 (n/a)</td><td>359.49 (n/a)</td><td>359.20 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.90 (-0.23%)</td><td>0.90 (-0.07%)</td><td>0.90 (-0.00%)</td><td>0.89 (-0.29%)</td><td>0.00 (+8.59%)</td><td>28120.20 (+0.30%)</td><td>27918.34 (+0.07%)</td><td>27889.00 (+0.00%)</td><td>27807.70 (+0.23%)</td><td>118.24 (+9.33%)</td><td>617.81 (-0.23%)</td><td>615.37 (-0.07%)</td><td>616.01 (-0.00%)</td><td>610.94 (-0.29%)</td><td>2.59 (+8.59%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28037.30 (n/a)</td><td>27899.72 (n/a)</td><td>27888.40 (n/a)</td><td>27743.10 (n/a)</td><td>108.15 (n/a)</td><td>619.25 (n/a)</td><td>615.78 (n/a)</td><td>616.02 (n/a)</td><td>612.75 (n/a)</td><td>2.39 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.31 (-3.84%)</td><td>3.27 (-0.11%)</td><td>3.30 (+1.56%)</td><td>3.14 (-0.88%)</td><td>0.07 <b>(-33.03%)</b></td><td>8011.00 (+0.89%)</td><td>7695.84 (+0.06%)</td><td>7615.70 (-1.53%)</td><td>7599.50 (+3.99%)</td><td>177.51 <b>(-29.57%)</b></td><td>2260.65 (-3.84%)</td><td>2233.28 (-0.11%)</td><td>2255.85 (+1.56%)</td><td>2144.55 (-0.88%)</td><td>50.02 <b>(-33.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.44 (n/a)</td><td>3.27 (n/a)</td><td>3.25 (n/a)</td><td>3.17 (n/a)</td><td>0.11 (n/a)</td><td>7940.60 (n/a)</td><td>7691.06 (n/a)</td><td>7734.40 (n/a)</td><td>7307.60 (n/a)</td><td>252.03 (n/a)</td><td>2350.97 (n/a)</td><td>2235.70 (n/a)</td><td>2221.22 (n/a)</td><td>2163.54 (n/a)</td><td>74.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>3.97 (-7.92%)</td><td>3.70 (+3.30%)</td><td>3.84 (+17.21%)</td><td>3.27 (+0.77%)</td><td>0.30 <b>(-38.24%)</b></td><td>2468.30 (-0.76%)</td><td>2188.50 (-3.96%)</td><td>2098.50 (-14.68%)</td><td>2028.20 (+8.60%)</td><td>184.39 <b>(-34.64%)</b></td><td>1042.28 (-7.92%)</td><td>971.17 (+3.30%)</td><td>1007.33 (+17.21%)</td><td>856.42 (+0.77%)</td><td>77.92 <b>(-38.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.32 (n/a)</td><td>3.59 (n/a)</td><td>3.28 (n/a)</td><td>3.24 (n/a)</td><td>0.48 (n/a)</td><td>2487.30 (n/a)</td><td>2278.68 (n/a)</td><td>2459.60 (n/a)</td><td>1867.60 (n/a)</td><td>282.13 (n/a)</td><td>1131.91 (n/a)</td><td>940.18 (n/a)</td><td>859.45 (n/a)</td><td>849.90 (n/a)</td><td>126.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.51 (+1.33%)</td><td>0.38 (-10.80%)</td><td>0.35 (-19.29%)</td><td>0.32 (+5.55%)</td><td>0.08 (-11.52%)</td><td>3864.30 (-5.26%)</td><td>3391.70 (+10.95%)</td><td>3532.90 <b>(+23.90%)</b></td><td>2422.30 (-1.32%)</td><td>564.10 (-18.46%)</td><td>27.70 (+1.33%)</td><td>20.34 (-10.80%)</td><td>19.00 (-19.29%)</td><td>17.37 (+5.55%)</td><td>4.19 (-11.52%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>4078.90 (n/a)</td><td>3056.84 (n/a)</td><td>2851.40 (n/a)</td><td>2454.60 (n/a)</td><td>691.84 (n/a)</td><td>27.34 (n/a)</td><td>22.80 (n/a)</td><td>23.54 (n/a)</td><td>16.45 (n/a)</td><td>4.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.48 (-0.34%)</td><td>5.17 (+12.56%)</td><td>4.85 (+2.57%)</td><td>4.63 <b>(+39.76%)</b></td><td>0.75 <b>(-39.99%)</b></td><td>1436.00 <b>(-28.45%)</b></td><td>1305.10 (-14.71%)</td><td>1372.60 (-2.51%)</td><td>1026.40 (+0.34%)</td><td>161.39 <b>(-58.35%)</b></td><td>2002.41 (-0.34%)</td><td>1597.55 (+12.56%)</td><td>1497.31 (+2.57%)</td><td>1431.19 <b>(+39.76%)</b></td><td>230.90 <b>(-39.99%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.50 (n/a)</td><td>4.59 (n/a)</td><td>4.72 (n/a)</td><td>3.31 (n/a)</td><td>1.25 (n/a)</td><td>2006.90 (n/a)</td><td>1530.24 (n/a)</td><td>1407.90 (n/a)</td><td>1022.90 (n/a)</td><td>387.50 (n/a)</td><td>2009.20 (n/a)</td><td>1419.25 (n/a)</td><td>1459.77 (n/a)</td><td>1024.07 (n/a)</td><td>384.75 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.61 (n/a)</td><td>12.91 (n/a)</td><td>13.14 (n/a)</td><td>12.14 (n/a)</td><td>0.59 (n/a)</td><td>13.60 (n/a)</td><td>12.90 (n/a)</td><td>13.13 (n/a)</td><td>12.13 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>25.16 (+0.30%)</td><td>24.10 (-1.08%)</td><td>24.26 (-0.31%)</td><td>22.47 (-5.78%)</td><td>0.99 <b>(+102.16%)</b></td><td>25.15 (+0.30%)</td><td>24.08 (-1.08%)</td><td>24.25 (-0.31%)</td><td>22.46 (-5.78%)</td><td>0.99 <b>(+102.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>25.09 (n/a)</td><td>24.36 (n/a)</td><td>24.34 (n/a)</td><td>23.85 (n/a)</td><td>0.49 (n/a)</td><td>25.07 (n/a)</td><td>24.35 (n/a)</td><td>24.32 (n/a)</td><td>23.84 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>42.86 (+0.74%)</td><td>40.83 (+0.88%)</td><td>40.21 (+0.32%)</td><td>39.82 (+0.43%)</td><td>1.28 (+8.57%)</td><td>42.83 (+0.74%)</td><td>40.80 (+0.88%)</td><td>40.18 (+0.32%)</td><td>39.79 (+0.43%)</td><td>1.28 (+8.57%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>42.54 (n/a)</td><td>40.47 (n/a)</td><td>40.08 (n/a)</td><td>39.65 (n/a)</td><td>1.18 (n/a)</td><td>42.52 (n/a)</td><td>40.45 (n/a)</td><td>40.05 (n/a)</td><td>39.62 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>46.11 (-2.88%)</td><td>44.89 (-0.13%)</td><td>45.32 (+0.87%)</td><td>43.34 (+1.06%)</td><td>1.15 <b>(-38.49%)</b></td><td>46.08 (-2.88%)</td><td>44.86 (-0.13%)</td><td>45.29 (+0.87%)</td><td>43.31 (+1.06%)</td><td>1.15 <b>(-38.49%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>47.48 (n/a)</td><td>44.95 (n/a)</td><td>44.93 (n/a)</td><td>42.88 (n/a)</td><td>1.86 (n/a)</td><td>47.45 (n/a)</td><td>44.92 (n/a)</td><td>44.90 (n/a)</td><td>42.86 (n/a)</td><td>1.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.53 (n/a)</td><td>13.12 (n/a)</td><td>13.42 (n/a)</td><td>11.80 (n/a)</td><td>0.74 (n/a)</td><td>13.52 (n/a)</td><td>13.12 (n/a)</td><td>13.41 (n/a)</td><td>11.80 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>25.26 (+0.98%)</td><td>24.56 (+0.61%)</td><td>24.38 (+0.53%)</td><td>23.92 (-1.08%)</td><td>0.54 <b>(+56.05%)</b></td><td>25.25 (+0.98%)</td><td>24.55 (+0.61%)</td><td>24.37 (+0.53%)</td><td>23.91 (-1.08%)</td><td>0.54 <b>(+56.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>25.02 (n/a)</td><td>24.41 (n/a)</td><td>24.25 (n/a)</td><td>24.18 (n/a)</td><td>0.35 (n/a)</td><td>25.00 (n/a)</td><td>24.40 (n/a)</td><td>24.24 (n/a)</td><td>24.17 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>41.78 (-0.81%)</td><td>40.61 (+3.76%)</td><td>41.33 (+1.00%)</td><td>39.17 <b>(+25.49%)</b></td><td>1.23 <b>(-72.46%)</b></td><td>41.76 (-0.81%)</td><td>40.58 (+3.76%)</td><td>41.31 (+1.00%)</td><td>39.15 <b>(+25.49%)</b></td><td>1.23 <b>(-72.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>42.13 (n/a)</td><td>39.14 (n/a)</td><td>40.93 (n/a)</td><td>31.22 (n/a)</td><td>4.48 (n/a)</td><td>42.10 (n/a)</td><td>39.11 (n/a)</td><td>40.90 (n/a)</td><td>31.20 (n/a)</td><td>4.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>46.61 (+2.67%)</td><td>40.86 (-5.43%)</td><td>45.24 (+6.51%)</td><td>23.39 <b>(-43.87%)</b></td><td>9.86 <b>(+509.26%)</b></td><td>46.58 (+2.67%)</td><td>40.83 (-5.43%)</td><td>45.21 (+6.51%)</td><td>23.37 <b>(-43.87%)</b></td><td>9.86 <b>(+509.26%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>45.40 (n/a)</td><td>43.20 (n/a)</td><td>42.47 (n/a)</td><td>41.67 (n/a)</td><td>1.62 (n/a)</td><td>45.37 (n/a)</td><td>43.18 (n/a)</td><td>42.45 (n/a)</td><td>41.65 (n/a)</td><td>1.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>9.01 (+2.18%)</td><td>8.28 (-4.75%)</td><td>8.24 (-5.30%)</td><td>7.32 (-14.57%)</td><td>0.64 <b>(+565.03%)</b></td><td>8.99 (+2.18%)</td><td>8.27 (-4.75%)</td><td>8.22 (-5.30%)</td><td>7.31 (-14.57%)</td><td>0.64 <b>(+565.03%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>8.82 (n/a)</td><td>8.70 (n/a)</td><td>8.70 (n/a)</td><td>8.57 (n/a)</td><td>0.10 (n/a)</td><td>8.80 (n/a)</td><td>8.68 (n/a)</td><td>8.68 (n/a)</td><td>8.56 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.93 (-0.44%)</td><td>0.88 (-0.65%)</td><td>0.86 (-6.08%)</td><td>0.80 (+1.65%)</td><td>0.06 (-11.08%)</td><td>0.92 (-0.44%)</td><td>0.86 (-0.65%)</td><td>0.85 (-6.08%)</td><td>0.78 (+1.65%)</td><td>0.06 (-11.08%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.94 (n/a)</td><td>0.88 (n/a)</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.07 (n/a)</td><td>0.92 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>0.77 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.34 (-7.18%)</td><td>1.08 (-14.47%)</td><td>1.05 (-16.20%)</td><td>0.91 (-18.35%)</td><td>0.16 <b>(+25.76%)</b></td><td>1.33 (-7.18%)</td><td>1.07 (-14.47%)</td><td>1.03 (-16.20%)</td><td>0.90 (-18.35%)</td><td>0.16 <b>(+25.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.45 (n/a)</td><td>1.27 (n/a)</td><td>1.25 (n/a)</td><td>1.11 (n/a)</td><td>0.13 (n/a)</td><td>1.43 (n/a)</td><td>1.25 (n/a)</td><td>1.23 (n/a)</td><td>1.10 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>17.94 (-1.15%)</td><td>16.84 (-1.42%)</td><td>17.23 (-1.03%)</td><td>15.70 (+3.11%)</td><td>1.01 (-8.69%)</td><td>17.74 (-1.15%)</td><td>16.65 (-1.42%)</td><td>17.03 (-1.03%)</td><td>15.52 (+3.11%)</td><td>1.00 (-8.69%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>18.15 (n/a)</td><td>17.08 (n/a)</td><td>17.41 (n/a)</td><td>15.23 (n/a)</td><td>1.11 (n/a)</td><td>17.94 (n/a)</td><td>16.88 (n/a)</td><td>17.21 (n/a)</td><td>15.05 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.64 (-2.86%)</td><td>13.22 (-2.64%)</td><td>13.19 (-3.15%)</td><td>12.62 (-3.20%)</td><td>0.39 (+7.91%)</td><td>13.40 (-2.86%)</td><td>12.99 (-2.64%)</td><td>12.96 (-3.15%)</td><td>12.40 (-3.20%)</td><td>0.39 (+7.91%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>14.05 (n/a)</td><td>13.58 (n/a)</td><td>13.62 (n/a)</td><td>13.04 (n/a)</td><td>0.36 (n/a)</td><td>13.80 (n/a)</td><td>13.34 (n/a)</td><td>13.38 (n/a)</td><td>12.81 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>8.63 (-5.17%)</td><td>7.72 (-3.97%)</td><td>7.62 (-5.37%)</td><td>6.95 (-0.64%)</td><td>0.76 (+1.85%)</td><td>8.48 (-5.17%)</td><td>7.58 (-3.97%)</td><td>7.49 (-5.37%)</td><td>6.83 (-0.64%)</td><td>0.75 (+1.85%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>9.10 (n/a)</td><td>8.04 (n/a)</td><td>8.05 (n/a)</td><td>6.99 (n/a)</td><td>0.75 (n/a)</td><td>8.94 (n/a)</td><td>7.90 (n/a)</td><td>7.91 (n/a)</td><td>6.87 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>6.41 (+5.67%)</td><td>5.87 (+4.08%)</td><td>5.99 (+10.22%)</td><td>4.96 (-8.36%)</td><td>0.59 <b>(+94.38%)</b></td><td>6.31 (+5.67%)</td><td>5.78 (+4.08%)</td><td>5.89 (+10.22%)</td><td>4.88 (-8.36%)</td><td>0.58 <b>(+94.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.07 (n/a)</td><td>5.64 (n/a)</td><td>5.43 (n/a)</td><td>5.41 (n/a)</td><td>0.30 (n/a)</td><td>5.97 (n/a)</td><td>5.55 (n/a)</td><td>5.34 (n/a)</td><td>5.33 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.47 (n/a)</td><td>12.98 (n/a)</td><td>13.20 (n/a)</td><td>11.90 (n/a)</td><td>0.62 (n/a)</td><td>13.46 (n/a)</td><td>12.97 (n/a)</td><td>13.20 (n/a)</td><td>11.89 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>13.42 (n/a)</td><td>13.18 (n/a)</td><td>13.16 (n/a)</td><td>12.92 (n/a)</td><td>0.18 (n/a)</td><td>13.42 (n/a)</td><td>13.17 (n/a)</td><td>13.15 (n/a)</td><td>12.91 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>273.70 (n/a)</td><td>194.88 (n/a)</td><td>181.30 (n/a)</td><td>138.10 (n/a)</td><td>52.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.80 (n/a)</td><td>204.74 (n/a)</td><td>194.90 (n/a)</td><td>151.40 (n/a)</td><td>43.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>159.82 (n/a)</td><td>152.10 (n/a)</td><td>140.20 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.70 (n/a)</td><td>184.90 (n/a)</td><td>182.70 (n/a)</td><td>156.90 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>190.84 (n/a)</td><td>191.20 (n/a)</td><td>154.60 (n/a)</td><td>32.85 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.40 (n/a)</td><td>204.00 (n/a)</td><td>192.90 (n/a)</td><td>167.60 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>176.40 (n/a)</td><td>173.60 (n/a)</td><td>137.60 (n/a)</td><td>25.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.00 (n/a)</td><td>257.80 (n/a)</td><td>242.20 (n/a)</td><td>184.40 (n/a)</td><td>66.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-9.56%)</td><td>0.04 (-11.19%)</td><td>0.04 (-9.19%)</td><td>0.03 (-11.02%)</td><td>0.01 (-12.42%)</td><td>236.10 (+12.38%)</td><td>191.72 (+12.24%)</td><td>198.30 (+10.11%)</td><td>132.40 (+10.52%)</td><td>38.44 (+5.71%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.10 (n/a)</td><td>170.82 (n/a)</td><td>180.10 (n/a)</td><td>119.80 (n/a)</td><td>36.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (-6.43%)</td><td>0.05 (-6.41%)</td><td>0.05 (-5.69%)</td><td>0.04 (-9.09%)</td><td>0.01 (-4.69%)</td><td>209.80 (+10.02%)</td><td>179.06 (+6.94%)</td><td>181.00 (+6.03%)</td><td>151.00 (+6.86%)</td><td>21.19 (+12.86%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>167.44 (n/a)</td><td>170.70 (n/a)</td><td>141.30 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 <b>(-27.45%)</b></td><td>0.04 (-17.94%)</td><td>0.04 (-19.40%)</td><td>0.03 (+0.97%)</td><td>0.01 <b>(-62.86%)</b></td><td>239.10 (-0.99%)</td><td>197.80 (+15.04%)</td><td>195.10 <b>(+24.11%)</b></td><td>164.60 <b>(+37.86%)</b></td><td>26.60 <b>(-49.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.50 (n/a)</td><td>171.94 (n/a)</td><td>157.20 (n/a)</td><td>119.40 (n/a)</td><td>52.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 <b>(-33.59%)</b></td><td>0.04 <b>(-20.20%)</b></td><td>0.04 <b>(-28.78%)</b></td><td>0.04 (+13.42%)</td><td>0.00 <b>(-70.54%)</b></td><td>210.80 (-11.84%)</td><td>190.90 (+17.15%)</td><td>197.60 <b>(+40.44%)</b></td><td>160.50 <b>(+50.56%)</b></td><td>19.63 <b>(-61.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>239.10 (n/a)</td><td>162.96 (n/a)</td><td>140.70 (n/a)</td><td>106.60 (n/a)</td><td>51.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.08 (+8.76%)</td><td>0.05 (-8.08%)</td><td>0.05 (-12.04%)</td><td>0.04 (-11.37%)</td><td>0.02 <b>(+45.63%)</b></td><td>214.10 (+12.86%)</td><td>169.98 (+12.57%)</td><td>177.70 (+13.69%)</td><td>100.70 (-8.04%)</td><td>41.73 <b>(+44.18%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>151.00 (n/a)</td><td>156.30 (n/a)</td><td>109.50 (n/a)</td><td>28.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-14.79%)</td><td>0.05 (-13.32%)</td><td>0.04 (-13.13%)</td><td>0.04 (-11.54%)</td><td>0.01 (-13.06%)</td><td>207.60 (+13.01%)</td><td>180.78 (+15.47%)</td><td>183.50 (+15.12%)</td><td>141.80 (+17.38%)</td><td>27.14 (+19.97%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>156.56 (n/a)</td><td>159.40 (n/a)</td><td>120.80 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-19.62%)</td><td>0.05 <b>(-24.71%)</b></td><td>0.04 <b>(-32.16%)</b></td><td>0.04 <b>(-28.66%)</b></td><td>0.01 (+9.37%)</td><td>217.40 <b>(+40.17%)</b></td><td>186.98 <b>(+35.20%)</b></td><td>202.70 <b>(+47.42%)</b></td><td>135.40 <b>(+24.33%)</b></td><td>36.02 <b>(+95.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>155.10 (n/a)</td><td>138.30 (n/a)</td><td>137.50 (n/a)</td><td>108.90 (n/a)</td><td>18.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-5.94%)</td><td>0.04 (-18.57%)</td><td>0.04 <b>(-25.44%)</b></td><td>0.03 <b>(-30.25%)</b></td><td>0.01 <b>(+94.73%)</b></td><td>248.00 <b>(+43.35%)</b></td><td>200.58 <b>(+27.60%)</b></td><td>208.60 <b>(+34.15%)</b></td><td>143.50 (+6.38%)</td><td>46.28 <b>(+196.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.00 (n/a)</td><td>157.20 (n/a)</td><td>155.50 (n/a)</td><td>134.90 (n/a)</td><td>15.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (-13.94%)</td><td>0.04 (-13.01%)</td><td>0.04 (-15.63%)</td><td>0.04 (-7.42%)</td><td>0.00 <b>(-31.22%)</b></td><td>205.60 (+8.04%)</td><td>190.06 (+14.56%)</td><td>190.90 (+18.50%)</td><td>168.40 (+16.22%)</td><td>14.52 (-14.34%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>165.90 (n/a)</td><td>161.10 (n/a)</td><td>144.90 (n/a)</td><td>16.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 <b>(+41.72%)</b></td><td>0.04 <b>(+22.33%)</b></td><td>0.04 (+17.21%)</td><td>0.04 <b>(+24.27%)</b></td><td>0.01 <b>(+88.32%)</b></td><td>231.60 (-19.53%)</td><td>193.44 (-16.59%)</td><td>200.10 (-14.67%)</td><td>127.60 <b>(-29.46%)</b></td><td>39.11 (+1.93%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.80 (n/a)</td><td>231.92 (n/a)</td><td>234.50 (n/a)</td><td>180.90 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 <b>(-21.75%)</b></td><td>0.05 (-15.93%)</td><td>0.05 <b>(-26.08%)</b></td><td>0.04 (-0.53%)</td><td>0.00 <b>(-70.20%)</b></td><td>199.50 (+0.50%)</td><td>178.52 (+14.91%)</td><td>176.30 <b>(+35.30%)</b></td><td>164.00 <b>(+27.83%)</b></td><td>13.76 <b>(-61.25%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.50 (n/a)</td><td>155.36 (n/a)</td><td>130.30 (n/a)</td><td>128.30 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (-4.92%)</td><td>0.03 (-10.91%)</td><td>0.03 (-14.47%)</td><td>0.03 (-6.67%)</td><td>0.01 (-12.11%)</td><td>313.40 (+7.15%)</td><td>248.30 (+11.79%)</td><td>244.60 (+16.92%)</td><td>190.40 (+5.19%)</td><td>43.66 (-2.04%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.50 (n/a)</td><td>222.12 (n/a)</td><td>209.20 (n/a)</td><td>181.00 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (+1.62%)</td><td>0.05 (+1.12%)</td><td>0.05 (+2.01%)</td><td>0.03 <b>(-30.77%)</b></td><td>0.01 <b>(+43.54%)</b></td><td>316.60 <b>(+44.43%)</b></td><td>190.04 (+5.05%)</td><td>168.00 (-1.93%)</td><td>132.00 (-1.57%)</td><td>74.03 <b>(+105.55%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>180.90 (n/a)</td><td>171.30 (n/a)</td><td>134.10 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 <b>(-20.37%)</b></td><td>0.05 (-11.58%)</td><td>0.04 (-16.51%)</td><td>0.04 (+7.15%)</td><td>0.01 <b>(-55.92%)</b></td><td>203.30 (-6.70%)</td><td>182.60 (+8.85%)</td><td>187.60 (+19.80%)</td><td>151.60 <b>(+25.60%)</b></td><td>20.97 <b>(-49.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>167.76 (n/a)</td><td>156.60 (n/a)</td><td>120.70 (n/a)</td><td>41.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 <b>(+44.33%)</b></td><td>0.05 <b>(+24.26%)</b></td><td>0.04 (+5.63%)</td><td>0.04 <b>(+62.20%)</b></td><td>0.01 (+15.37%)</td><td>217.40 <b>(-38.34%)</b></td><td>178.42 <b>(-21.66%)</b></td><td>185.10 (-5.37%)</td><td>127.70 <b>(-30.71%)</b></td><td>32.73 <b>(-53.81%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>352.60 (n/a)</td><td>227.76 (n/a)</td><td>195.60 (n/a)</td><td>184.30 (n/a)</td><td>70.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (+16.95%)</td><td>0.05 (+3.55%)</td><td>0.05 (-3.65%)</td><td>0.04 (-6.08%)</td><td>0.01 <b>(+87.80%)</b></td><td>209.30 (+6.51%)</td><td>165.82 (-0.59%)</td><td>170.70 (+3.77%)</td><td>117.30 (-14.44%)</td><td>36.46 <b>(+70.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.50 (n/a)</td><td>166.80 (n/a)</td><td>164.50 (n/a)</td><td>137.10 (n/a)</td><td>21.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (-6.96%)</td><td>0.04 (-14.85%)</td><td>0.04 (-16.72%)</td><td>0.03 (-11.05%)</td><td>0.01 (+11.83%)</td><td>238.60 (+12.39%)</td><td>202.78 (+18.27%)</td><td>199.70 <b>(+20.08%)</b></td><td>155.40 (+7.47%)</td><td>32.54 <b>(+31.20%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>171.46 (n/a)</td><td>166.30 (n/a)</td><td>144.60 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (-10.94%)</td><td>0.04 (-9.89%)</td><td>0.04 (-12.71%)</td><td>0.04 (+4.08%)</td><td>0.00 <b>(-58.14%)</b></td><td>212.90 (-3.93%)</td><td>196.68 (+9.88%)</td><td>193.20 (+14.59%)</td><td>187.70 (+12.26%)</td><td>10.67 <b>(-55.22%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>179.00 (n/a)</td><td>168.60 (n/a)</td><td>167.20 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47879.30 (n/a)</td><td>47744.34 (n/a)</td><td>47783.60 (n/a)</td><td>47422.90 (n/a)</td><td>185.72 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.20 (-1.53%)</td><td>0.17 (+2.24%)</td><td>0.17 (-5.88%)</td><td>0.13 <b>(+23.63%)</b></td><td>0.03 <b>(-37.31%)</b></td><td>187.40 (-19.08%)</td><td>150.28 (-6.18%)</td><td>140.60 (+6.27%)</td><td>125.40 (+1.54%)</td><td>25.49 <b>(-46.84%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>231.60 (n/a)</td><td>160.18 (n/a)</td><td>132.30 (n/a)</td><td>123.50 (n/a)</td><td>47.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.27 (-14.00%)</td><td>0.25 (+0.25%)</td><td>0.25 (+1.81%)</td><td>0.22 <b>(+22.36%)</b></td><td>0.02 <b>(-58.49%)</b></td><td>184.40 (-18.26%)</td><td>162.50 (-2.94%)</td><td>160.70 (-1.77%)</td><td>150.50 (+16.31%)</td><td>13.70 <b>(-61.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>225.60 (n/a)</td><td>167.42 (n/a)</td><td>163.60 (n/a)</td><td>129.40 (n/a)</td><td>35.70 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (-6.35%)</td><td>0.03 (+3.00%)</td><td>0.03 (+9.48%)</td><td>0.02 (-4.14%)</td><td>0.01 (-16.43%)</td><td>205.60 (+4.31%)</td><td>162.84 (-3.45%)</td><td>160.20 (-8.67%)</td><td>128.00 (+6.76%)</td><td>28.41 (-2.11%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>168.66 (n/a)</td><td>175.40 (n/a)</td><td>119.90 (n/a)</td><td>29.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (+11.82%)</td><td>0.05 (+8.85%)</td><td>0.05 (+4.86%)</td><td>0.04 (+10.66%)</td><td>0.01 (+4.07%)</td><td>232.20 (-9.65%)</td><td>175.80 (-8.72%)</td><td>173.20 (-4.63%)</td><td>125.80 (-10.53%)</td><td>37.76 (-17.44%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>257.00 (n/a)</td><td>192.60 (n/a)</td><td>181.60 (n/a)</td><td>140.60 (n/a)</td><td>45.74 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.10 (+9.58%)</td><td>0.07 (-10.41%)</td><td>0.07 <b>(-20.30%)</b></td><td>0.07 (-9.84%)</td><td>0.01 <b>(+53.77%)</b></td><td>188.40 (+10.95%)</td><td>168.84 (+13.25%)</td><td>174.10 <b>(+25.43%)</b></td><td>121.80 (-8.76%)</td><td>27.10 <b>(+51.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>169.80 (n/a)</td><td>149.08 (n/a)</td><td>138.80 (n/a)</td><td>133.50 (n/a)</td><td>17.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (+18.37%)</td><td>0.05 (-0.25%)</td><td>0.05 (-1.49%)</td><td>0.04 (-15.06%)</td><td>0.01 <b>(+110.63%)</b></td><td>214.40 (+17.74%)</td><td>169.82 (+3.88%)</td><td>168.40 (+1.51%)</td><td>112.60 (-15.53%)</td><td>37.71 <b>(+107.87%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>163.48 (n/a)</td><td>165.90 (n/a)</td><td>133.30 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-19.64%)</td><td>0.05 <b>(-20.90%)</b></td><td>0.04 <b>(-22.30%)</b></td><td>0.04 <b>(-27.60%)</b></td><td>0.01 (+8.25%)</td><td>266.10 <b>(+38.09%)</b></td><td>214.96 <b>(+28.23%)</b></td><td>228.30 <b>(+28.69%)</b></td><td>170.20 <b>(+24.42%)</b></td><td>40.36 <b>(+82.17%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.70 (n/a)</td><td>167.64 (n/a)</td><td>177.40 (n/a)</td><td>136.80 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (+11.82%)</td><td>0.04 (-0.16%)</td><td>0.04 (-5.03%)</td><td>0.04 (-8.81%)</td><td>0.01 <b>(+48.91%)</b></td><td>227.90 (+9.67%)</td><td>187.32 (+1.21%)</td><td>190.40 (+5.31%)</td><td>147.60 (-10.55%)</td><td>28.89 <b>(+44.05%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.80 (n/a)</td><td>185.08 (n/a)</td><td>180.80 (n/a)</td><td>165.00 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-13.35%)</td><td>0.05 (+1.04%)</td><td>0.05 (-8.94%)</td><td>0.05 <b>(+32.87%)</b></td><td>0.00 <b>(-70.76%)</b></td><td>215.20 <b>(-24.76%)</b></td><td>192.02 (-6.37%)</td><td>186.90 (+9.81%)</td><td>175.70 (+15.36%)</td><td>14.85 <b>(-74.58%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>286.00 (n/a)</td><td>205.08 (n/a)</td><td>170.20 (n/a)</td><td>152.30 (n/a)</td><td>58.43 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (+12.97%)</td><td>0.05 (+0.23%)</td><td>0.05 (-1.65%)</td><td>0.04 (-9.61%)</td><td>0.01 <b>(+124.59%)</b></td><td>228.70 (+10.64%)</td><td>184.18 (+1.60%)</td><td>179.40 (+1.70%)</td><td>150.10 (-11.50%)</td><td>31.66 <b>(+116.24%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>181.28 (n/a)</td><td>176.40 (n/a)</td><td>169.60 (n/a)</td><td>14.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 (+7.17%)</td><td>0.05 (-4.74%)</td><td>0.05 (-13.23%)</td><td>0.04 (+2.56%)</td><td>0.01 (+13.21%)</td><td>213.80 (-2.46%)</td><td>186.48 (+5.20%)</td><td>192.20 (+15.23%)</td><td>139.50 (-6.69%)</td><td>27.92 (-1.35%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>177.26 (n/a)</td><td>166.80 (n/a)</td><td>149.50 (n/a)</td><td>28.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.07 <b>(+33.19%)</b></td><td>0.05 <b>(+24.80%)</b></td><td>0.05 <b>(+21.86%)</b></td><td>0.04 <b>(+48.92%)</b></td><td>0.01 (+16.81%)</td><td>187.50 <b>(-32.87%)</b></td><td>163.82 <b>(-20.88%)</b></td><td>172.60 (-17.97%)</td><td>118.60 <b>(-24.94%)</b></td><td>26.46 <b>(-43.44%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.30 (n/a)</td><td>207.04 (n/a)</td><td>210.40 (n/a)</td><td>158.00 (n/a)</td><td>46.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 <b>(-28.05%)</b></td><td>0.05 (-19.74%)</td><td>0.04 <b>(-20.05%)</b></td><td>0.04 (-14.82%)</td><td>0.01 <b>(-41.51%)</b></td><td>236.60 (+17.36%)</td><td>203.06 <b>(+21.94%)</b></td><td>220.70 <b>(+25.11%)</b></td><td>145.30 <b>(+38.91%)</b></td><td>36.32 (-0.42%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>201.60 (n/a)</td><td>166.52 (n/a)</td><td>176.40 (n/a)</td><td>104.60 (n/a)</td><td>36.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.06 (-2.55%)</td><td>0.04 (-12.72%)</td><td>0.05 (-6.83%)</td><td>0.03 <b>(-38.89%)</b></td><td>0.01 <b>(+149.25%)</b></td><td>296.30 <b>(+63.61%)</b></td><td>197.80 <b>(+22.11%)</b></td><td>170.60 (+7.30%)</td><td>148.30 (+2.63%)</td><td>63.28 <b>(+305.08%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>161.98 (n/a)</td><td>159.00 (n/a)</td><td>144.50 (n/a)</td><td>15.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (-2.16%)</td><td>0.04 (-12.53%)</td><td>0.04 (-13.68%)</td><td>0.04 <b>(-21.31%)</b></td><td>0.01 <b>(+95.51%)</b></td><td>246.00 <b>(+27.07%)</b></td><td>213.94 (+15.82%)</td><td>218.60 (+15.85%)</td><td>168.00 (+2.19%)</td><td>29.12 <b>(+151.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>193.60 (n/a)</td><td>184.72 (n/a)</td><td>188.70 (n/a)</td><td>164.40 (n/a)</td><td>11.59 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (-9.67%)</td><td>0.05 (-5.87%)</td><td>0.04 (-7.37%)</td><td>0.04 (-4.24%)</td><td>0.01 (-9.01%)</td><td>211.30 (+4.45%)</td><td>179.10 (+6.13%)</td><td>183.60 (+7.94%)</td><td>152.00 (+10.71%)</td><td>25.56 (+3.13%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>168.76 (n/a)</td><td>170.10 (n/a)</td><td>137.30 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.05 (+9.30%)</td><td>0.04 (+3.09%)</td><td>0.04 (-5.90%)</td><td>0.04 (+3.60%)</td><td>0.01 <b>(+73.93%)</b></td><td>219.80 (-3.47%)</td><td>199.94 (-2.17%)</td><td>215.80 (+6.31%)</td><td>167.40 (-8.47%)</td><td>24.75 <b>(+55.28%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>227.70 (n/a)</td><td>204.38 (n/a)</td><td>203.00 (n/a)</td><td>182.90 (n/a)</td><td>15.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 (+8.90%)</td><td>0.04 (+4.81%)</td><td>0.04 (+1.08%)</td><td>0.03 (+7.35%)</td><td>0.00 (+10.74%)</td><td>243.40 (-6.85%)</td><td>218.52 (-4.55%)</td><td>221.20 (-1.03%)</td><td>194.60 (-8.16%)</td><td>19.11 (-5.65%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>261.30 (n/a)</td><td>228.94 (n/a)</td><td>223.50 (n/a)</td><td>211.90 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.75 (-7.04%)</td><td>0.61 (+15.89%)</td><td>0.62 (+17.13%)</td><td>0.39 <b>(+36.06%)</b></td><td>0.14 <b>(-28.59%)</b></td><td>252.20 <b>(-26.52%)</b></td><td>170.12 (-18.87%)</td><td>157.60 (-14.63%)</td><td>130.70 (+7.57%)</td><td>47.63 <b>(-42.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.81 (n/a)</td><td>0.52 (n/a)</td><td>0.53 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>343.20 (n/a)</td><td>209.70 (n/a)</td><td>184.60 (n/a)</td><td>121.50 (n/a)</td><td>82.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.86 (+14.57%)</td><td>0.65 (-1.68%)</td><td>0.61 (-15.33%)</td><td>0.58 (+8.02%)</td><td>0.12 <b>(+21.92%)</b></td><td>169.60 (-7.42%)</td><td>153.34 (+2.05%)</td><td>162.40 (+18.11%)</td><td>114.00 (-12.71%)</td><td>22.53 (-3.18%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.71 (n/a)</td><td>0.54 (n/a)</td><td>0.10 (n/a)</td><td>183.20 (n/a)</td><td>150.26 (n/a)</td><td>137.50 (n/a)</td><td>130.60 (n/a)</td><td>23.27 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.85 (+7.01%)</td><td>0.62 (-2.37%)</td><td>0.62 (+4.70%)</td><td>0.49 (-2.99%)</td><td>0.15 (+10.20%)</td><td>201.40 (+3.07%)</td><td>164.60 (+3.16%)</td><td>158.90 (-4.51%)</td><td>115.90 (-6.53%)</td><td>35.69 (+11.01%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.79 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.50 (n/a)</td><td>0.13 (n/a)</td><td>195.40 (n/a)</td><td>159.56 (n/a)</td><td>166.40 (n/a)</td><td>124.00 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.66 (+2.92%)</td><td>0.58 (+11.93%)</td><td>0.63 (+16.99%)</td><td>0.48 <b>(+29.79%)</b></td><td>0.08 (-16.02%)</td><td>204.50 <b>(-22.95%)</b></td><td>171.64 (-12.07%)</td><td>156.70 (-14.51%)</td><td>148.70 (-2.87%)</td><td>26.12 <b>(-38.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.64 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.10 (n/a)</td><td>265.40 (n/a)</td><td>195.20 (n/a)</td><td>183.30 (n/a)</td><td>153.10 (n/a)</td><td>42.66 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.60 (+7.54%)</td><td>0.42 (-12.07%)</td><td>0.41 (-19.99%)</td><td>0.27 <b>(-25.28%)</b></td><td>0.12 <b>(+51.93%)</b></td><td>271.00 <b>(+33.83%)</b></td><td>187.82 (+18.89%)</td><td>178.30 <b>(+24.95%)</b></td><td>123.20 (-7.02%)</td><td>56.10 <b>(+90.27%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.52 (n/a)</td><td>0.36 (n/a)</td><td>0.08 (n/a)</td><td>202.50 (n/a)</td><td>157.98 (n/a)</td><td>142.70 (n/a)</td><td>132.50 (n/a)</td><td>29.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.65 (-3.20%)</td><td>0.49 (+1.76%)</td><td>0.46 (+1.29%)</td><td>0.39 (+12.57%)</td><td>0.10 <b>(-29.32%)</b></td><td>190.00 (-11.17%)</td><td>155.76 (-5.09%)</td><td>160.80 (-1.29%)</td><td>114.20 (+3.25%)</td><td>27.42 <b>(-38.21%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.67 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.14 (n/a)</td><td>213.90 (n/a)</td><td>164.12 (n/a)</td><td>162.90 (n/a)</td><td>110.60 (n/a)</td><td>44.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (-0.27%)</td><td>0.46 (+4.85%)</td><td>0.48 (+11.19%)</td><td>0.35 (+13.03%)</td><td>0.08 (-17.61%)</td><td>213.30 (-11.53%)</td><td>165.96 (-6.10%)</td><td>152.60 (-10.08%)</td><td>140.00 (+0.29%)</td><td>30.97 <b>(-25.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>241.10 (n/a)</td><td>176.74 (n/a)</td><td>169.70 (n/a)</td><td>139.60 (n/a)</td><td>41.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.53 (+15.10%)</td><td>0.43 (+9.85%)</td><td>0.43 (+8.67%)</td><td>0.32 (-1.79%)</td><td>0.09 <b>(+51.54%)</b></td><td>232.60 (+1.79%)</td><td>179.06 (-7.44%)</td><td>171.60 (-7.99%)</td><td>140.10 (-13.14%)</td><td>37.64 <b>(+32.35%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>228.50 (n/a)</td><td>193.46 (n/a)</td><td>186.50 (n/a)</td><td>161.30 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.24 <b>(+20.23%)</b></td><td>0.78 (-10.77%)</td><td>0.65 (-19.19%)</td><td>0.56 <b>(-22.71%)</b></td><td>0.28 <b>(+88.93%)</b></td><td>232.30 <b>(+29.42%)</b></td><td>183.56 (+19.13%)</td><td>201.80 <b>(+23.73%)</b></td><td>105.80 (-16.82%)</td><td>52.15 <b>(+107.86%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.03 (n/a)</td><td>0.87 (n/a)</td><td>0.80 (n/a)</td><td>0.73 (n/a)</td><td>0.15 (n/a)</td><td>179.50 (n/a)</td><td>154.08 (n/a)</td><td>163.10 (n/a)</td><td>127.20 (n/a)</td><td>25.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.02 (-4.97%)</td><td>0.81 (+7.17%)</td><td>0.80 (+16.03%)</td><td>0.63 <b>(+46.41%)</b></td><td>0.15 <b>(-42.13%)</b></td><td>207.70 <b>(-31.70%)</b></td><td>165.50 (-13.36%)</td><td>164.10 (-13.81%)</td><td>127.90 (+5.18%)</td><td>29.52 <b>(-58.46%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.08 (n/a)</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>304.10 (n/a)</td><td>191.02 (n/a)</td><td>190.40 (n/a)</td><td>121.60 (n/a)</td><td>71.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.13 <b>(+35.23%)</b></td><td>0.79 (+4.75%)</td><td>0.72 (-9.71%)</td><td>0.58 (-11.99%)</td><td>0.21 <b>(+162.98%)</b></td><td>227.60 (+13.63%)</td><td>173.72 (-0.55%)</td><td>181.40 (+10.74%)</td><td>116.00 <b>(-26.07%)</b></td><td>41.25 <b>(+114.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.84 (n/a)</td><td>0.76 (n/a)</td><td>0.80 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>200.30 (n/a)</td><td>174.68 (n/a)</td><td>163.80 (n/a)</td><td>156.90 (n/a)</td><td>19.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (-11.60%)</td><td>0.02 (-15.15%)</td><td>0.02 (-19.61%)</td><td>0.02 (-14.92%)</td><td>0.00 (+14.73%)</td><td>242.80 (+17.58%)</td><td>200.62 (+19.87%)</td><td>207.40 <b>(+24.34%)</b></td><td>147.60 (+13.10%)</td><td>42.39 <b>(+56.38%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.50 (n/a)</td><td>167.36 (n/a)</td><td>166.80 (n/a)</td><td>130.50 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (+18.57%)</td><td>0.03 (+15.74%)</td><td>0.02 (+9.90%)</td><td>0.02 <b>(+25.78%)</b></td><td>0.00 (+4.18%)</td><td>183.20 <b>(-20.49%)</b></td><td>160.36 (-14.06%)</td><td>166.80 (-9.00%)</td><td>130.00 (-15.69%)</td><td>20.10 <b>(-31.52%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.40 (n/a)</td><td>186.60 (n/a)</td><td>183.30 (n/a)</td><td>154.20 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (-12.51%)</td><td>0.02 (-14.78%)</td><td>0.02 (-13.76%)</td><td>0.02 (-10.60%)</td><td>0.00 (-13.71%)</td><td>218.50 (+11.82%)</td><td>181.40 (+17.27%)</td><td>171.70 (+15.94%)</td><td>150.80 (+14.33%)</td><td>29.49 (+12.29%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.40 (n/a)</td><td>154.68 (n/a)</td><td>148.10 (n/a)</td><td>131.90 (n/a)</td><td>26.26 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.17 <b>(+27.39%)</b></td><td>0.88 (+19.38%)</td><td>0.84 (+15.94%)</td><td>0.54 (-11.21%)</td><td>0.24 <b>(+108.77%)</b></td><td>243.70 (+12.62%)</td><td>160.22 (-11.77%)</td><td>157.40 (-13.75%)</td><td>112.60 <b>(-21.53%)</b></td><td>51.21 <b>(+88.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.72 (n/a)</td><td>0.61 (n/a)</td><td>0.12 (n/a)</td><td>216.40 (n/a)</td><td>181.60 (n/a)</td><td>182.50 (n/a)</td><td>143.50 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.03 (+15.60%)</td><td>0.87 <b>(+26.95%)</b></td><td>0.83 <b>(+26.69%)</b></td><td>0.72 <b>(+35.80%)</b></td><td>0.13 (-11.84%)</td><td>182.50 <b>(-26.35%)</b></td><td>155.28 <b>(-22.55%)</b></td><td>158.80 <b>(-21.07%)</b></td><td>127.80 (-13.53%)</td><td>22.28 <b>(-44.19%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.89 (n/a)</td><td>0.68 (n/a)</td><td>0.66 (n/a)</td><td>0.53 (n/a)</td><td>0.14 (n/a)</td><td>247.80 (n/a)</td><td>200.50 (n/a)</td><td>201.20 (n/a)</td><td>147.80 (n/a)</td><td>39.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.87 <b>(+22.91%)</b></td><td>0.75 (+16.85%)</td><td>0.81 (+18.68%)</td><td>0.53 (-0.37%)</td><td>0.14 <b>(+95.84%)</b></td><td>250.10 (+0.36%)</td><td>183.06 (-12.37%)</td><td>164.00 (-15.72%)</td><td>151.50 (-18.68%)</td><td>41.33 <b>(+58.80%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.68 (n/a)</td><td>0.53 (n/a)</td><td>0.07 (n/a)</td><td>249.20 (n/a)</td><td>208.90 (n/a)</td><td>194.60 (n/a)</td><td>186.30 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.02 (-4.90%)</td><td>0.88 (+14.37%)</td><td>0.95 (+18.07%)</td><td>0.62 (+16.93%)</td><td>0.16 <b>(-21.06%)</b></td><td>214.60 (-14.50%)</td><td>154.54 (-14.54%)</td><td>139.50 (-15.35%)</td><td>129.60 (+5.11%)</td><td>34.71 <b>(-27.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.07 (n/a)</td><td>0.77 (n/a)</td><td>0.80 (n/a)</td><td>0.53 (n/a)</td><td>0.20 (n/a)</td><td>251.00 (n/a)</td><td>180.84 (n/a)</td><td>164.80 (n/a)</td><td>123.30 (n/a)</td><td>47.94 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>1.04 <b>(+26.67%)</b></td><td>0.92 <b>(+24.31%)</b></td><td>0.97 <b>(+32.37%)</b></td><td>0.62 (-8.91%)</td><td>0.17 <b>(+216.47%)</b></td><td>212.30 (+9.77%)</td><td>149.64 (-16.94%)</td><td>135.90 <b>(-24.50%)</b></td><td>127.20 <b>(-21.09%)</b></td><td>35.79 <b>(+178.92%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.82 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.68 (n/a)</td><td>0.05 (n/a)</td><td>193.40 (n/a)</td><td>180.16 (n/a)</td><td>180.00 (n/a)</td><td>161.20 (n/a)</td><td>12.83 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.03 (+3.49%)</td><td>0.02 (-10.62%)</td><td>0.02 (-13.28%)</td><td>0.02 <b>(-23.24%)</b></td><td>0.01 <b>(+30.60%)</b></td><td>265.40 <b>(+30.23%)</b></td><td>189.46 (+15.20%)</td><td>189.00 (+15.31%)</td><td>125.00 (-3.40%)</td><td>50.34 <b>(+63.59%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.80 (n/a)</td><td>164.46 (n/a)</td><td>163.90 (n/a)</td><td>129.40 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.04 <b>(+28.53%)</b></td><td>0.02 (-2.23%)</td><td>0.02 (-12.04%)</td><td>0.02 (-7.08%)</td><td>0.01 <b>(+181.12%)</b></td><td>200.70 (+7.61%)</td><td>173.60 (+6.45%)</td><td>185.30 (+13.68%)</td><td>111.90 <b>(-22.18%)</b></td><td>36.78 <b>(+131.28%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.50 (n/a)</td><td>163.08 (n/a)</td><td>163.00 (n/a)</td><td>143.80 (n/a)</td><td>15.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.00 (+0.00%)</td><td>0.00 (-0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.63%)</td><td>0.00 <b>(-26.97%)</b></td><td>1055.28 (-3.00%)</td><td>980.48 (-0.05%)</td><td>970.45 (-0.40%)</td><td>939.58 (+1.17%)</td><td>43.78 <b>(-31.72%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1087.95 (n/a)</td><td>980.93 (n/a)</td><td>974.36 (n/a)</td><td>928.68 (n/a)</td><td>64.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.01 (+0.00%)</td><td>0.01 (-0.75%)</td><td>0.01 (-1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 (-6.17%)</td><td>1088.29 (-0.53%)</td><td>1030.13 (+0.83%)</td><td>1028.58 (+2.22%)</td><td>977.31 (+0.70%)</td><td>39.66 (-16.13%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1094.10 (n/a)</td><td>1021.61 (n/a)</td><td>1006.22 (n/a)</td><td>970.54 (n/a)</td><td>47.29 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>0.99 (+0.40%)</td><td>0.97 (+1.17%)</td><td>0.96 (+0.40%)</td><td>0.95 (+0.91%)</td><td>0.02 (+16.86%)</td><td>2200.97 (-0.90%)</td><td>2164.06 (-1.15%)</td><td>2191.59 (-0.40%)</td><td>2113.01 (-0.40%)</td><td>45.20 (+15.59%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2221.04 (n/a)</td><td>2189.27 (n/a)</td><td>2200.44 (n/a)</td><td>2121.50 (n/a)</td><td>39.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.87 (+1.02%)</td><td>2.56 (-2.69%)</td><td>2.54 (-3.72%)</td><td>2.29 (-3.22%)</td><td>0.22 <b>(+27.93%)</b></td><td>228.60 (+3.30%)</td><td>206.22 (+2.98%)</td><td>206.10 (+3.88%)</td><td>182.40 (-1.03%)</td><td>17.19 <b>(+29.19%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>2.84 (n/a)</td><td>2.63 (n/a)</td><td>2.64 (n/a)</td><td>2.37 (n/a)</td><td>0.17 (n/a)</td><td>221.30 (n/a)</td><td>200.26 (n/a)</td><td>198.40 (n/a)</td><td>184.30 (n/a)</td><td>13.31 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>5.78 (+7.26%)</td><td>5.03 (+3.58%)</td><td>4.77 (-2.66%)</td><td>4.61 (+4.83%)</td><td>0.48 (+6.41%)</td><td>227.50 (-4.61%)</td><td>209.80 (-3.48%)</td><td>219.80 (+2.71%)</td><td>181.50 (-6.73%)</td><td>18.80 (-7.14%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>5.39 (n/a)</td><td>4.86 (n/a)</td><td>4.90 (n/a)</td><td>4.40 (n/a)</td><td>0.45 (n/a)</td><td>238.50 (n/a)</td><td>217.36 (n/a)</td><td>214.00 (n/a)</td><td>194.60 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:35:43</td><td>2.90 (-9.99%)</td><td>2.68 (-2.74%)</td><td>2.64 (-4.81%)</td><td>2.44 (+4.41%)</td><td>0.22 <b>(-35.09%)</b></td><td>214.70 (-4.19%)</td><td>196.84 (+2.17%)</td><td>198.90 (+5.07%)</td><td>180.60 (+11.07%)</td><td>15.79 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.22 (n/a)</td><td>2.75 (n/a)</td><td>2.77 (n/a)</td><td>2.34 (n/a)</td><td>0.33 (n/a)</td><td>224.10 (n/a)</td><td>192.66 (n/a)</td><td>189.30 (n/a)</td><td>162.60 (n/a)</td><td>23.13 (n/a)</td>
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
