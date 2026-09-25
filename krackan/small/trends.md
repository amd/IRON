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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 <b>(+26.82%)</b></td><td>0.07 (+3.60%)</td><td>0.07 (-4.72%)</td><td>0.07 (-4.46%)</td><td>0.01 <b>(+713.32%)</b></td><td>187.90 (+4.68%)</td><td>171.44 (-2.18%)</td><td>182.00 (+4.90%)</td><td>136.10 <b>(-21.19%)</b></td><td>20.92 <b>(+568.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>179.50 (n/a)</td><td>175.26 (n/a)</td><td>173.50 (n/a)</td><td>172.70 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (-5.31%)</td><td>0.06 (-5.06%)</td><td>0.07 (+1.59%)</td><td>0.05 (-5.78%)</td><td>0.01 <b>(+22.17%)</b></td><td>223.70 (+6.12%)</td><td>197.16 (+5.83%)</td><td>184.10 (-1.60%)</td><td>175.20 (+5.61%)</td><td>24.16 <b>(+39.48%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>186.30 (n/a)</td><td>187.10 (n/a)</td><td>165.90 (n/a)</td><td>17.32 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (-12.00%)</td><td>0.06 (-12.03%)</td><td>0.06 (-17.55%)</td><td>0.05 (-13.62%)</td><td>0.01 (-7.96%)</td><td>264.80 (+15.78%)</td><td>218.16 (+13.84%)</td><td>221.00 <b>(+21.30%)</b></td><td>184.30 (+13.63%)</td><td>31.06 <b>(+20.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>191.64 (n/a)</td><td>182.20 (n/a)</td><td>162.20 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (+4.51%)</td><td>0.06 (+1.93%)</td><td>0.06 (-10.36%)</td><td>0.05 <b>(+27.67%)</b></td><td>0.01 (-18.43%)</td><td>234.60 <b>(-21.67%)</b></td><td>204.30 (-3.75%)</td><td>217.40 (+11.54%)</td><td>163.50 (-4.33%)</td><td>29.09 <b>(-42.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>299.50 (n/a)</td><td>212.26 (n/a)</td><td>194.90 (n/a)</td><td>170.90 (n/a)</td><td>50.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 <b>(-31.68%)</b></td><td>0.03 <b>(-22.88%)</b></td><td>0.03 <b>(-22.16%)</b></td><td>0.02 <b>(-24.96%)</b></td><td>0.00 <b>(-38.21%)</b></td><td>238.50 <b>(+33.31%)</b></td><td>192.46 <b>(+28.72%)</b></td><td>196.50 <b>(+28.43%)</b></td><td>162.20 <b>(+46.39%)</b></td><td>31.49 (+18.82%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>149.52 (n/a)</td><td>153.00 (n/a)</td><td>110.80 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 <b>(-28.29%)</b></td><td>0.03 (-16.50%)</td><td>0.03 (-10.65%)</td><td>0.03 (-8.17%)</td><td>0.00 <b>(-52.73%)</b></td><td>187.30 (+8.90%)</td><td>163.14 (+16.33%)</td><td>168.70 (+11.94%)</td><td>129.70 <b>(+39.46%)</b></td><td>21.98 <b>(-26.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>140.24 (n/a)</td><td>150.70 (n/a)</td><td>93.00 (n/a)</td><td>29.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 <b>(-20.12%)</b></td><td>0.03 (-18.98%)</td><td>0.03 <b>(-24.45%)</b></td><td>0.03 (-13.13%)</td><td>0.00 <b>(-63.31%)</b></td><td>191.50 (+15.08%)</td><td>179.52 <b>(+22.37%)</b></td><td>178.50 <b>(+32.42%)</b></td><td>166.90 <b>(+25.21%)</b></td><td>9.09 <b>(-47.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>166.40 (n/a)</td><td>146.70 (n/a)</td><td>134.80 (n/a)</td><td>133.30 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 <b>(-22.63%)</b></td><td>0.03 (-18.32%)</td><td>0.03 <b>(-25.88%)</b></td><td>0.02 (-8.56%)</td><td>0.00 <b>(-55.58%)</b></td><td>226.80 (+9.35%)</td><td>188.28 (+19.60%)</td><td>182.70 <b>(+34.93%)</b></td><td>172.30 <b>(+29.26%)</b></td><td>22.18 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>157.42 (n/a)</td><td>135.40 (n/a)</td><td>133.30 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-1.08%)</td><td>0.03 (+0.13%)</td><td>0.03 (+0.75%)</td><td>0.02 (-6.99%)</td><td>0.00 (+14.32%)</td><td>213.80 (+7.55%)</td><td>182.88 (+0.18%)</td><td>182.80 (-0.76%)</td><td>157.20 (+1.09%)</td><td>20.92 <b>(+26.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>182.56 (n/a)</td><td>184.20 (n/a)</td><td>155.50 (n/a)</td><td>16.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 <b>(-25.88%)</b></td><td>0.03 <b>(-21.91%)</b></td><td>0.03 (-13.94%)</td><td>0.02 <b>(-34.71%)</b></td><td>0.00 <b>(-22.57%)</b></td><td>278.90 <b>(+53.16%)</b></td><td>211.54 <b>(+28.88%)</b></td><td>204.10 (+16.23%)</td><td>160.80 <b>(+34.90%)</b></td><td>42.86 <b>(+65.88%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.10 (n/a)</td><td>164.14 (n/a)</td><td>175.60 (n/a)</td><td>119.20 (n/a)</td><td>25.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (+19.96%)</td><td>0.03 (+8.11%)</td><td>0.03 (+14.19%)</td><td>0.02 (-5.12%)</td><td>0.01 <b>(+69.61%)</b></td><td>226.90 (+5.39%)</td><td>172.76 (-3.90%)</td><td>155.70 (-12.38%)</td><td>113.40 (-16.62%)</td><td>46.70 <b>(+54.75%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>179.78 (n/a)</td><td>177.70 (n/a)</td><td>136.00 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-7.63%)</td><td>0.02 (-11.63%)</td><td>0.02 (-9.82%)</td><td>0.02 <b>(-20.02%)</b></td><td>0.00 <b>(+40.58%)</b></td><td>301.10 <b>(+25.04%)</b></td><td>239.78 (+14.40%)</td><td>224.40 (+10.87%)</td><td>207.40 (+8.25%)</td><td>37.37 <b>(+91.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.80 (n/a)</td><td>209.60 (n/a)</td><td>202.40 (n/a)</td><td>191.60 (n/a)</td><td>19.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>200.50 (n/a)</td><td>154.08 (n/a)</td><td>148.80 (n/a)</td><td>105.70 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>177.40 (n/a)</td><td>160.34 (n/a)</td><td>167.70 (n/a)</td><td>138.80 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>243.90 (n/a)</td><td>181.20 (n/a)</td><td>166.40 (n/a)</td><td>132.30 (n/a)</td><td>45.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>185.62 (n/a)</td><td>182.10 (n/a)</td><td>162.80 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>185.90 (n/a)</td><td>168.26 (n/a)</td><td>174.90 (n/a)</td><td>142.30 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>166.68 (n/a)</td><td>162.10 (n/a)</td><td>134.40 (n/a)</td><td>27.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>289.70 (n/a)</td><td>208.78 (n/a)</td><td>210.70 (n/a)</td><td>147.50 (n/a)</td><td>54.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>178.98 (n/a)</td><td>184.50 (n/a)</td><td>138.80 (n/a)</td><td>23.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.71 (+3.78%)</td><td>3.56 (+5.22%)</td><td>3.25 (+2.05%)</td><td>2.90 (+0.78%)</td><td>0.76 (+15.17%)</td><td>473.90 (-0.77%)</td><td>399.46 (-4.19%)</td><td>423.40 (-2.01%)</td><td>292.00 (-3.63%)</td><td>76.88 (+15.33%)</td><td>919.38 (+3.78%)</td><td>694.66 (+5.22%)</td><td>633.97 (+2.05%)</td><td>566.39 (+0.78%)</td><td>148.30 (+15.17%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.54 (n/a)</td><td>3.38 (n/a)</td><td>3.18 (n/a)</td><td>2.88 (n/a)</td><td>0.66 (n/a)</td><td>477.60 (n/a)</td><td>416.94 (n/a)</td><td>432.10 (n/a)</td><td>303.00 (n/a)</td><td>66.66 (n/a)</td><td>885.88 (n/a)</td><td>660.19 (n/a)</td><td>621.22 (n/a)</td><td>562.02 (n/a)</td><td>128.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.08 <b>(+22.96%)</b></td><td>4.51 (+11.88%)</td><td>3.60 (-6.77%)</td><td>3.48 (-0.14%)</td><td>1.31 <b>(+139.39%)</b></td><td>396.00 (+0.15%)</td><td>324.78 (-6.06%)</td><td>382.40 (+7.27%)</td><td>226.40 (-18.65%)</td><td>85.45 <b>(+99.45%)</b></td><td>1185.93 <b>(+22.96%)</b></td><td>880.50 (+11.88%)</td><td>702.05 (-6.77%)</td><td>677.88 (-0.14%)</td><td>256.40 <b>(+139.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.94 (n/a)</td><td>4.03 (n/a)</td><td>3.86 (n/a)</td><td>3.48 (n/a)</td><td>0.55 (n/a)</td><td>395.40 (n/a)</td><td>345.72 (n/a)</td><td>356.50 (n/a)</td><td>278.30 (n/a)</td><td>42.84 (n/a)</td><td>964.45 (n/a)</td><td>786.98 (n/a)</td><td>753.04 (n/a)</td><td>678.84 (n/a)</td><td>107.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.63 (+4.27%)</td><td>4.90 (+13.48%)</td><td>5.04 <b>(+26.79%)</b></td><td>3.44 (+4.01%)</td><td>1.40 (+18.79%)</td><td>400.20 (-3.84%)</td><td>301.00 (-10.02%)</td><td>272.90 <b>(-21.13%)</b></td><td>207.50 (-4.11%)</td><td>88.28 <b>(+21.51%)</b></td><td>1293.44 (+4.27%)</td><td>955.17 (+13.48%)</td><td>983.53 <b>(+26.79%)</b></td><td>670.83 (+4.01%)</td><td>273.20 (+18.79%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.36 (n/a)</td><td>4.32 (n/a)</td><td>3.98 (n/a)</td><td>3.31 (n/a)</td><td>1.18 (n/a)</td><td>416.20 (n/a)</td><td>334.52 (n/a)</td><td>346.00 (n/a)</td><td>216.40 (n/a)</td><td>72.66 (n/a)</td><td>1240.51 (n/a)</td><td>841.75 (n/a)</td><td>775.74 (n/a)</td><td>644.95 (n/a)</td><td>229.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>5.42 <b>(-20.69%)</b></td><td>4.27 (-3.01%)</td><td>3.70 (-7.49%)</td><td>3.40 (-1.82%)</td><td>1.01 <b>(-26.46%)</b></td><td>404.90 (+1.84%)</td><td>336.78 (+1.46%)</td><td>372.00 (+8.11%)</td><td>254.10 <b>(+26.10%)</b></td><td>74.39 (-2.52%)</td><td>1056.61 <b>(-20.69%)</b></td><td>831.96 (-3.01%)</td><td>721.56 (-7.49%)</td><td>662.93 (-1.82%)</td><td>197.79 <b>(-26.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.83 (n/a)</td><td>4.40 (n/a)</td><td>4.00 (n/a)</td><td>3.46 (n/a)</td><td>1.38 (n/a)</td><td>397.60 (n/a)</td><td>331.92 (n/a)</td><td>344.10 (n/a)</td><td>201.50 (n/a)</td><td>76.32 (n/a)</td><td>1332.23 (n/a)</td><td>857.78 (n/a)</td><td>780.01 (n/a)</td><td>675.20 (n/a)</td><td>268.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.39 <b>(+31.31%)</b></td><td>3.67 (+15.93%)</td><td>3.70 (+11.54%)</td><td>3.01 (+5.51%)</td><td>0.52 <b>(+122.16%)</b></td><td>457.20 (-5.22%)</td><td>381.46 (-12.75%)</td><td>371.50 (-10.35%)</td><td>313.80 <b>(-23.83%)</b></td><td>54.05 <b>(+62.29%)</b></td><td>855.55 <b>(+31.31%)</b></td><td>715.08 (+15.93%)</td><td>722.48 (+11.54%)</td><td>587.18 (+5.51%)</td><td>100.82 <b>(+122.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.34 (n/a)</td><td>3.16 (n/a)</td><td>3.32 (n/a)</td><td>2.85 (n/a)</td><td>0.23 (n/a)</td><td>482.40 (n/a)</td><td>437.18 (n/a)</td><td>414.40 (n/a)</td><td>412.00 (n/a)</td><td>33.30 (n/a)</td><td>651.55 (n/a)</td><td>616.80 (n/a)</td><td>647.72 (n/a)</td><td>556.50 (n/a)</td><td>45.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.70 (-1.79%)</td><td>1.31 (+8.32%)</td><td>1.24 (+15.94%)</td><td>1.05 (+3.18%)</td><td>0.29 (-4.38%)</td><td>383.90 (-3.08%)</td><td>316.92 (-7.89%)</td><td>325.00 (-13.75%)</td><td>235.60 (+1.86%)</td><td>65.24 (-1.68%)</td><td>142.43 (-1.79%)</td><td>109.79 (+8.32%)</td><td>103.25 (+15.94%)</td><td>87.40 (+3.18%)</td><td>23.88 (-4.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.74 (n/a)</td><td>1.21 (n/a)</td><td>1.07 (n/a)</td><td>1.01 (n/a)</td><td>0.30 (n/a)</td><td>396.10 (n/a)</td><td>344.06 (n/a)</td><td>376.80 (n/a)</td><td>231.30 (n/a)</td><td>66.36 (n/a)</td><td>145.04 (n/a)</td><td>101.35 (n/a)</td><td>89.06 (n/a)</td><td>84.71 (n/a)</td><td>24.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.66 <b>(+27.59%)</b></td><td>5.54 (+15.75%)</td><td>5.26 (+7.84%)</td><td>4.67 (+12.27%)</td><td>0.91 <b>(+95.94%)</b></td><td>414.10 (-10.93%)</td><td>356.34 (-12.45%)</td><td>367.70 (-7.26%)</td><td>290.20 <b>(-21.63%)</b></td><td>56.69 <b>(+38.24%)</b></td><td>1387.54 <b>(+27.59%)</b></td><td>1154.09 (+15.75%)</td><td>1094.97 (+7.84%)</td><td>972.24 (+12.27%)</td><td>190.01 <b>(+95.94%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>5.22 (n/a)</td><td>4.79 (n/a)</td><td>4.88 (n/a)</td><td>4.16 (n/a)</td><td>0.47 (n/a)</td><td>464.90 (n/a)</td><td>407.02 (n/a)</td><td>396.50 (n/a)</td><td>370.30 (n/a)</td><td>41.01 (n/a)</td><td>1087.48 (n/a)</td><td>997.04 (n/a)</td><td>1015.40 (n/a)</td><td>866.02 (n/a)</td><td>96.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>14.78 (-2.91%)</td><td>12.68 (+7.87%)</td><td>12.25 (+8.86%)</td><td>11.21 (+9.57%)</td><td>1.56 <b>(-23.90%)</b></td><td>491.00 (-8.74%)</td><td>439.12 (-8.15%)</td><td>449.20 (-8.14%)</td><td>372.40 (+3.02%)</td><td>52.04 <b>(-27.45%)</b></td><td>5767.24 (-2.91%)</td><td>4948.00 (+7.87%)</td><td>4780.42 (+8.86%)</td><td>4373.56 (+9.57%)</td><td>607.28 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>15.23 (n/a)</td><td>11.76 (n/a)</td><td>11.26 (n/a)</td><td>10.23 (n/a)</td><td>2.05 (n/a)</td><td>538.00 (n/a)</td><td>478.06 (n/a)</td><td>489.00 (n/a)</td><td>361.50 (n/a)</td><td>71.74 (n/a)</td><td>5940.35 (n/a)</td><td>4587.19 (n/a)</td><td>4391.48 (n/a)</td><td>3991.65 (n/a)</td><td>798.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>164.24 (n/a)</td><td>169.70 (n/a)</td><td>134.30 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>158.80 (n/a)</td><td>170.80 (n/a)</td><td>121.90 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.80 (n/a)</td><td>173.68 (n/a)</td><td>173.00 (n/a)</td><td>160.90 (n/a)</td><td>10.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>203.60 (n/a)</td><td>174.06 (n/a)</td><td>172.40 (n/a)</td><td>156.30 (n/a)</td><td>18.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>161.22 (n/a)</td><td>152.00 (n/a)</td><td>129.30 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>180.62 (n/a)</td><td>179.30 (n/a)</td><td>154.90 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>187.70 (n/a)</td><td>181.40 (n/a)</td><td>129.40 (n/a)</td><td>41.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.40 (n/a)</td><td>234.84 (n/a)</td><td>225.00 (n/a)</td><td>172.00 (n/a)</td><td>58.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.82 (+13.02%)</td><td>4.14 (+8.36%)</td><td>4.21 (+15.11%)</td><td>3.52 (+0.94%)</td><td>0.54 <b>(+41.27%)</b></td><td>2668.40 (-0.94%)</td><td>2302.48 (-7.17%)</td><td>2232.40 (-13.13%)</td><td>1949.40 (-11.52%)</td><td>299.81 <b>(+25.09%)</b></td><td>1897.70 (+13.02%)</td><td>1628.60 (+8.36%)</td><td>1657.12 (+15.11%)</td><td>1386.35 (+0.94%)</td><td>210.94 <b>(+41.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.27 (n/a)</td><td>3.82 (n/a)</td><td>3.66 (n/a)</td><td>3.49 (n/a)</td><td>0.38 (n/a)</td><td>2693.60 (n/a)</td><td>2480.38 (n/a)</td><td>2569.70 (n/a)</td><td>2203.30 (n/a)</td><td>239.67 (n/a)</td><td>1679.05 (n/a)</td><td>1502.99 (n/a)</td><td>1439.61 (n/a)</td><td>1373.41 (n/a)</td><td>149.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.24 <b>(+24.12%)</b></td><td>0.94 (+10.60%)</td><td>1.06 (+18.16%)</td><td>0.64 (+1.26%)</td><td>0.27 <b>(+76.30%)</b></td><td>347.60 (-1.25%)</td><td>252.16 (-5.44%)</td><td>209.10 (-15.38%)</td><td>179.10 (-19.43%)</td><td>79.04 <b>(+46.12%)</b></td><td>52.69 <b>(+24.12%)</b></td><td>40.31 (+10.60%)</td><td>45.12 (+18.16%)</td><td>27.15 (+1.26%)</td><td>11.60 <b>(+76.30%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.00 (n/a)</td><td>0.85 (n/a)</td><td>0.90 (n/a)</td><td>0.63 (n/a)</td><td>0.15 (n/a)</td><td>352.00 (n/a)</td><td>266.66 (n/a)</td><td>247.10 (n/a)</td><td>222.30 (n/a)</td><td>54.09 (n/a)</td><td>42.45 (n/a)</td><td>36.45 (n/a)</td><td>38.19 (n/a)</td><td>26.81 (n/a)</td><td>6.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.29 <b>(+20.90%)</b></td><td>1.06 (+15.18%)</td><td>1.12 (+9.76%)</td><td>0.81 <b>(+23.09%)</b></td><td>0.21 (+18.89%)</td><td>271.70 (-18.77%)</td><td>214.60 (-13.27%)</td><td>196.80 (-8.93%)</td><td>171.50 (-17.27%)</td><td>44.11 (-18.69%)</td><td>55.04 <b>(+20.90%)</b></td><td>45.43 (+15.18%)</td><td>47.94 (+9.76%)</td><td>34.73 <b>(+23.09%)</b></td><td>8.86 (+18.89%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.07 (n/a)</td><td>0.92 (n/a)</td><td>1.02 (n/a)</td><td>0.66 (n/a)</td><td>0.17 (n/a)</td><td>334.50 (n/a)</td><td>247.44 (n/a)</td><td>216.10 (n/a)</td><td>207.30 (n/a)</td><td>54.24 (n/a)</td><td>45.52 (n/a)</td><td>39.44 (n/a)</td><td>43.68 (n/a)</td><td>28.22 (n/a)</td><td>7.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.53 (+0.03%)</td><td>0.53 (+0.07%)</td><td>0.53 (+0.04%)</td><td>0.53 (+0.24%)</td><td>0.00 <b>(-46.26%)</b></td><td>47889.20 (-0.24%)</td><td>47811.14 (-0.07%)</td><td>47803.60 (-0.04%)</td><td>47762.70 (-0.03%)</td><td>49.95 <b>(-46.41%)</b></td><td>359.69 (+0.03%)</td><td>359.33 (+0.07%)</td><td>359.38 (+0.04%)</td><td>358.74 (+0.24%)</td><td>0.38 <b>(-46.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48004.50 (n/a)</td><td>47843.80 (n/a)</td><td>47820.40 (n/a)</td><td>47776.90 (n/a)</td><td>93.21 (n/a)</td><td>359.59 (n/a)</td><td>359.08 (n/a)</td><td>359.26 (n/a)</td><td>357.88 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (-1.28%)</td><td>0.90 (-0.65%)</td><td>0.90 (-0.78%)</td><td>0.90 (-0.31%)</td><td>0.00 <b>(-48.76%)</b></td><td>27891.80 (+0.31%)</td><td>27810.44 (+0.66%)</td><td>27864.70 (+0.79%)</td><td>27699.90 (+1.30%)</td><td>98.17 <b>(-47.95%)</b></td><td>620.21 (-1.28%)</td><td>617.75 (-0.65%)</td><td>616.55 (-0.78%)</td><td>615.95 (-0.31%)</td><td>2.18 <b>(-48.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.91 (n/a)</td><td>0.91 (n/a)</td><td>0.01 (n/a)</td><td>27804.50 (n/a)</td><td>27629.30 (n/a)</td><td>27646.50 (n/a)</td><td>27344.30 (n/a)</td><td>188.62 (n/a)</td><td>628.28 (n/a)</td><td>621.82 (n/a)</td><td>621.41 (n/a)</td><td>617.88 (n/a)</td><td>4.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>3.32 (+0.09%)</td><td>3.26 (+2.41%)</td><td>3.28 (+3.40%)</td><td>3.16 (+2.03%)</td><td>0.06 <b>(-24.63%)</b></td><td>7952.30 (-1.99%)</td><td>7712.62 (-2.37%)</td><td>7669.00 (-3.29%)</td><td>7590.50 (-0.09%)</td><td>140.22 <b>(-25.58%)</b></td><td>2263.35 (+0.09%)</td><td>2228.09 (+2.41%)</td><td>2240.17 (+3.40%)</td><td>2160.37 (+2.03%)</td><td>39.76 <b>(-24.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.31 (n/a)</td><td>3.19 (n/a)</td><td>3.17 (n/a)</td><td>3.10 (n/a)</td><td>0.08 (n/a)</td><td>8114.10 (n/a)</td><td>7899.74 (n/a)</td><td>7929.90 (n/a)</td><td>7597.30 (n/a)</td><td>188.42 (n/a)</td><td>2261.30 (n/a)</td><td>2175.74 (n/a)</td><td>2166.46 (n/a)</td><td>2117.28 (n/a)</td><td>52.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.08 (-2.16%)</td><td>3.79 (+5.78%)</td><td>3.70 (+0.24%)</td><td>3.69 <b>(+23.80%)</b></td><td>0.17 <b>(-70.22%)</b></td><td>2183.60 (-19.22%)</td><td>2129.42 (-7.20%)</td><td>2176.40 (-0.24%)</td><td>1975.70 (+2.21%)</td><td>88.52 <b>(-75.82%)</b></td><td>1069.96 (-2.16%)</td><td>994.17 (+5.78%)</td><td>971.29 (+0.24%)</td><td>968.10 <b>(+23.80%)</b></td><td>43.46 <b>(-70.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.17 (n/a)</td><td>3.58 (n/a)</td><td>3.69 (n/a)</td><td>2.98 (n/a)</td><td>0.56 (n/a)</td><td>2703.20 (n/a)</td><td>2294.56 (n/a)</td><td>2181.70 (n/a)</td><td>1933.00 (n/a)</td><td>366.08 (n/a)</td><td>1093.61 (n/a)</td><td>939.87 (n/a)</td><td>968.93 (n/a)</td><td>782.01 (n/a)</td><td>145.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.40 (-17.50%)</td><td>0.36 (-2.11%)</td><td>0.35 (+1.13%)</td><td>0.33 <b>(+20.55%)</b></td><td>0.03 <b>(-63.23%)</b></td><td>3753.80 (-17.05%)</td><td>3518.92 (-0.64%)</td><td>3511.20 (-1.12%)</td><td>3114.10 <b>(+21.22%)</b></td><td>262.27 <b>(-62.10%)</b></td><td>21.55 (-17.50%)</td><td>19.16 (-2.11%)</td><td>19.11 (+1.13%)</td><td>17.88 <b>(+20.55%)</b></td><td>1.50 <b>(-63.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>4525.20 (n/a)</td><td>3541.52 (n/a)</td><td>3550.80 (n/a)</td><td>2569.00 (n/a)</td><td>691.99 (n/a)</td><td>26.12 (n/a)</td><td>19.57 (n/a)</td><td>18.90 (n/a)</td><td>14.83 (n/a)</td><td>4.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.10 (+0.61%)</td><td>4.91 (-3.02%)</td><td>4.79 (-1.48%)</td><td>3.71 <b>(-20.32%)</b></td><td>0.86 <b>(+51.89%)</b></td><td>1791.60 <b>(+25.51%)</b></td><td>1389.88 (+4.87%)</td><td>1388.40 (+1.50%)</td><td>1091.00 (-0.60%)</td><td>256.00 <b>(+96.31%)</b></td><td>1883.77 (+0.61%)</td><td>1517.17 (-3.02%)</td><td>1480.22 (-1.48%)</td><td>1147.11 <b>(-20.32%)</b></td><td>265.43 <b>(+51.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.06 (n/a)</td><td>5.06 (n/a)</td><td>4.86 (n/a)</td><td>4.66 (n/a)</td><td>0.57 (n/a)</td><td>1427.50 (n/a)</td><td>1325.32 (n/a)</td><td>1367.90 (n/a)</td><td>1097.60 (n/a)</td><td>130.41 (n/a)</td><td>1872.37 (n/a)</td><td>1564.44 (n/a)</td><td>1502.47 (n/a)</td><td>1439.68 (n/a)</td><td>174.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>12.80 (n/a)</td><td>12.34 (n/a)</td><td>12.55 (n/a)</td><td>11.23 (n/a)</td><td>0.63 (n/a)</td><td>12.79 (n/a)</td><td>12.34 (n/a)</td><td>12.54 (n/a)</td><td>11.22 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>24.46 (-2.48%)</td><td>22.12 (-10.45%)</td><td>23.55 (-4.93%)</td><td>16.84 <b>(-30.55%)</b></td><td>3.08 <b>(+844.33%)</b></td><td>24.44 (-2.48%)</td><td>22.11 (-10.45%)</td><td>23.54 (-4.93%)</td><td>16.83 <b>(-30.55%)</b></td><td>3.07 <b>(+844.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>25.08 (n/a)</td><td>24.70 (n/a)</td><td>24.77 (n/a)</td><td>24.25 (n/a)</td><td>0.33 (n/a)</td><td>25.07 (n/a)</td><td>24.68 (n/a)</td><td>24.76 (n/a)</td><td>24.24 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>41.74 (-5.13%)</td><td>40.43 (-3.62%)</td><td>39.90 (-6.26%)</td><td>39.50 (+0.21%)</td><td>0.98 <b>(-45.43%)</b></td><td>41.72 (-5.13%)</td><td>40.41 (-3.62%)</td><td>39.87 (-6.26%)</td><td>39.47 (+0.21%)</td><td>0.98 <b>(-45.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>44.00 (n/a)</td><td>41.95 (n/a)</td><td>42.56 (n/a)</td><td>39.41 (n/a)</td><td>1.80 (n/a)</td><td>43.97 (n/a)</td><td>41.93 (n/a)</td><td>42.54 (n/a)</td><td>39.39 (n/a)</td><td>1.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>45.60 (+0.73%)</td><td>44.20 (+1.24%)</td><td>44.59 (+2.79%)</td><td>42.51 (-0.64%)</td><td>1.17 <b>(+23.24%)</b></td><td>45.58 (+0.73%)</td><td>44.17 (+1.24%)</td><td>44.56 (+2.79%)</td><td>42.48 (-0.64%)</td><td>1.17 <b>(+23.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>45.27 (n/a)</td><td>43.66 (n/a)</td><td>43.38 (n/a)</td><td>42.78 (n/a)</td><td>0.95 (n/a)</td><td>45.24 (n/a)</td><td>43.63 (n/a)</td><td>43.35 (n/a)</td><td>42.75 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>13.20 (n/a)</td><td>12.33 (n/a)</td><td>12.30 (n/a)</td><td>11.52 (n/a)</td><td>0.61 (n/a)</td><td>13.19 (n/a)</td><td>12.32 (n/a)</td><td>12.29 (n/a)</td><td>11.51 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>25.36 (-1.25%)</td><td>23.93 (-2.19%)</td><td>23.74 (-3.94%)</td><td>22.82 (-0.09%)</td><td>0.94 (-10.96%)</td><td>25.34 (-1.25%)</td><td>23.92 (-2.19%)</td><td>23.73 (-3.94%)</td><td>22.81 (-0.09%)</td><td>0.94 (-10.96%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>25.68 (n/a)</td><td>24.47 (n/a)</td><td>24.72 (n/a)</td><td>22.84 (n/a)</td><td>1.06 (n/a)</td><td>25.66 (n/a)</td><td>24.46 (n/a)</td><td>24.70 (n/a)</td><td>22.83 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>42.91 (+0.52%)</td><td>38.43 (-6.17%)</td><td>40.16 (-1.45%)</td><td>27.87 <b>(-28.30%)</b></td><td>6.01 <b>(+287.25%)</b></td><td>42.89 (+0.52%)</td><td>38.41 (-6.17%)</td><td>40.14 (-1.45%)</td><td>27.86 <b>(-28.30%)</b></td><td>6.01 <b>(+287.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>42.69 (n/a)</td><td>40.96 (n/a)</td><td>40.75 (n/a)</td><td>38.88 (n/a)</td><td>1.55 (n/a)</td><td>42.66 (n/a)</td><td>40.94 (n/a)</td><td>40.73 (n/a)</td><td>38.85 (n/a)</td><td>1.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>45.30 (-4.01%)</td><td>43.93 (+0.65%)</td><td>43.41 (+0.34%)</td><td>42.55 (+10.00%)</td><td>1.26 <b>(-61.47%)</b></td><td>45.27 (-4.01%)</td><td>43.90 (+0.65%)</td><td>43.39 (+0.34%)</td><td>42.52 (+10.00%)</td><td>1.26 <b>(-61.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>47.19 (n/a)</td><td>43.65 (n/a)</td><td>43.27 (n/a)</td><td>38.68 (n/a)</td><td>3.28 (n/a)</td><td>47.16 (n/a)</td><td>43.62 (n/a)</td><td>43.24 (n/a)</td><td>38.66 (n/a)</td><td>3.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>9.32 (-7.05%)</td><td>8.72 (-3.33%)</td><td>8.69 (-0.96%)</td><td>8.21 (-3.05%)</td><td>0.45 <b>(-28.87%)</b></td><td>9.30 (-7.05%)</td><td>8.71 (-3.33%)</td><td>8.68 (-0.96%)</td><td>8.19 (-3.05%)</td><td>0.45 <b>(-28.87%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>10.02 (n/a)</td><td>9.02 (n/a)</td><td>8.78 (n/a)</td><td>8.47 (n/a)</td><td>0.64 (n/a)</td><td>10.00 (n/a)</td><td>9.01 (n/a)</td><td>8.76 (n/a)</td><td>8.45 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.05 (+14.68%)</td><td>0.91 (+6.90%)</td><td>0.88 (+2.15%)</td><td>0.80 (+0.94%)</td><td>0.10 <b>(+86.22%)</b></td><td>1.03 (+14.68%)</td><td>0.89 (+6.90%)</td><td>0.86 (+2.15%)</td><td>0.78 (+0.94%)</td><td>0.10 <b>(+86.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.86 (n/a)</td><td>0.79 (n/a)</td><td>0.05 (n/a)</td><td>0.90 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.78 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.38 (+17.94%)</td><td>1.23 (+8.95%)</td><td>1.19 (+4.12%)</td><td>1.13 (+5.40%)</td><td>0.10 <b>(+153.21%)</b></td><td>1.37 (+17.94%)</td><td>1.22 (+8.95%)</td><td>1.18 (+4.12%)</td><td>1.12 (+5.40%)</td><td>0.10 <b>(+153.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.17 (n/a)</td><td>1.13 (n/a)</td><td>1.15 (n/a)</td><td>1.08 (n/a)</td><td>0.04 (n/a)</td><td>1.16 (n/a)</td><td>1.12 (n/a)</td><td>1.13 (n/a)</td><td>1.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>21.14 (+14.78%)</td><td>17.65 (+2.23%)</td><td>17.61 (+3.87%)</td><td>15.80 (-2.90%)</td><td>2.18 <b>(+133.91%)</b></td><td>20.89 (+14.78%)</td><td>17.44 (+2.23%)</td><td>17.41 (+3.87%)</td><td>15.61 (-2.90%)</td><td>2.15 <b>(+133.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>18.41 (n/a)</td><td>17.26 (n/a)</td><td>16.96 (n/a)</td><td>16.27 (n/a)</td><td>0.93 (n/a)</td><td>18.20 (n/a)</td><td>17.06 (n/a)</td><td>16.76 (n/a)</td><td>16.08 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>13.61 (-2.89%)</td><td>13.32 (+0.68%)</td><td>13.50 (+3.93%)</td><td>12.96 (+2.45%)</td><td>0.32 <b>(-40.61%)</b></td><td>13.37 (-2.89%)</td><td>13.08 (+0.68%)</td><td>13.26 (+3.93%)</td><td>12.73 (+2.45%)</td><td>0.31 <b>(-40.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>14.01 (n/a)</td><td>13.23 (n/a)</td><td>12.99 (n/a)</td><td>12.65 (n/a)</td><td>0.54 (n/a)</td><td>13.77 (n/a)</td><td>12.99 (n/a)</td><td>12.76 (n/a)</td><td>12.43 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>8.23 (-4.60%)</td><td>7.39 (-6.05%)</td><td>7.86 (-2.18%)</td><td>5.81 (-15.08%)</td><td>0.97 <b>(+47.76%)</b></td><td>8.09 (-4.60%)</td><td>7.27 (-6.05%)</td><td>7.72 (-2.18%)</td><td>5.71 (-15.08%)</td><td>0.96 <b>(+47.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>8.63 (n/a)</td><td>7.87 (n/a)</td><td>8.04 (n/a)</td><td>6.84 (n/a)</td><td>0.66 (n/a)</td><td>8.48 (n/a)</td><td>7.73 (n/a)</td><td>7.90 (n/a)</td><td>6.73 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.17 (+3.05%)</td><td>5.40 (-2.91%)</td><td>5.24 (-7.23%)</td><td>4.69 (-2.90%)</td><td>0.57 <b>(+23.16%)</b></td><td>6.07 (+3.05%)</td><td>5.32 (-2.91%)</td><td>5.15 (-7.23%)</td><td>4.62 (-2.90%)</td><td>0.56 <b>(+23.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>5.98 (n/a)</td><td>5.57 (n/a)</td><td>5.64 (n/a)</td><td>4.83 (n/a)</td><td>0.46 (n/a)</td><td>5.89 (n/a)</td><td>5.48 (n/a)</td><td>5.55 (n/a)</td><td>4.76 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>13.33 (n/a)</td><td>13.02 (n/a)</td><td>13.22 (n/a)</td><td>12.12 (n/a)</td><td>0.51 (n/a)</td><td>13.32 (n/a)</td><td>13.01 (n/a)</td><td>13.21 (n/a)</td><td>12.11 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>13.23 (n/a)</td><td>11.87 (n/a)</td><td>11.20 (n/a)</td><td>10.82 (n/a)</td><td>1.13 (n/a)</td><td>13.23 (n/a)</td><td>11.86 (n/a)</td><td>11.19 (n/a)</td><td>10.81 (n/a)</td><td>1.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>159.40 (n/a)</td><td>164.70 (n/a)</td><td>118.70 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>162.12 (n/a)</td><td>166.00 (n/a)</td><td>120.40 (n/a)</td><td>32.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.50 (n/a)</td><td>160.12 (n/a)</td><td>168.20 (n/a)</td><td>130.10 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>173.24 (n/a)</td><td>187.00 (n/a)</td><td>114.60 (n/a)</td><td>46.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.60 (n/a)</td><td>174.94 (n/a)</td><td>170.10 (n/a)</td><td>148.40 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>269.30 (n/a)</td><td>197.42 (n/a)</td><td>201.40 (n/a)</td><td>105.90 (n/a)</td><td>69.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>181.98 (n/a)</td><td>184.00 (n/a)</td><td>140.10 (n/a)</td><td>41.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.60 (n/a)</td><td>213.32 (n/a)</td><td>193.60 (n/a)</td><td>149.40 (n/a)</td><td>60.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 <b>(-22.97%)</b></td><td>0.04 <b>(-25.99%)</b></td><td>0.04 <b>(-32.51%)</b></td><td>0.04 <b>(-24.89%)</b></td><td>0.01 (-14.89%)</td><td>233.20 <b>(+33.18%)</b></td><td>198.96 <b>(+35.75%)</b></td><td>206.20 <b>(+48.13%)</b></td><td>158.80 <b>(+29.84%)</b></td><td>33.79 <b>(+45.87%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>146.56 (n/a)</td><td>139.20 (n/a)</td><td>122.30 (n/a)</td><td>23.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (+2.74%)</td><td>0.05 (-5.18%)</td><td>0.05 (-8.16%)</td><td>0.04 (-11.01%)</td><td>0.01 <b>(+33.68%)</b></td><td>210.40 (+12.39%)</td><td>170.68 (+6.68%)</td><td>164.60 (+8.86%)</td><td>135.40 (-2.66%)</td><td>29.50 <b>(+46.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>160.00 (n/a)</td><td>151.20 (n/a)</td><td>139.10 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (+18.40%)</td><td>0.04 (-8.64%)</td><td>0.04 (-11.67%)</td><td>0.02 <b>(-44.27%)</b></td><td>0.02 <b>(+152.44%)</b></td><td>365.00 <b>(+79.45%)</b></td><td>215.84 <b>(+21.74%)</b></td><td>203.00 (+13.22%)</td><td>124.80 (-15.56%)</td><td>89.94 <b>(+296.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>177.30 (n/a)</td><td>179.30 (n/a)</td><td>147.80 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 <b>(-22.03%)</b></td><td>0.04 (-19.43%)</td><td>0.04 (-11.11%)</td><td>0.04 (-11.99%)</td><td>0.01 <b>(-41.09%)</b></td><td>230.50 (+13.60%)</td><td>193.00 <b>(+21.51%)</b></td><td>190.80 (+12.50%)</td><td>154.10 <b>(+28.20%)</b></td><td>34.04 (-8.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>158.84 (n/a)</td><td>169.60 (n/a)</td><td>120.20 (n/a)</td><td>37.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-16.08%)</td><td>0.04 (-14.99%)</td><td>0.04 (-8.93%)</td><td>0.04 (-11.61%)</td><td>0.01 <b>(-34.64%)</b></td><td>228.00 (+13.10%)</td><td>192.46 (+15.90%)</td><td>190.60 (+9.79%)</td><td>150.80 (+19.12%)</td><td>29.21 (-12.18%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>166.06 (n/a)</td><td>173.60 (n/a)</td><td>126.60 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (-8.38%)</td><td>0.05 (+3.06%)</td><td>0.05 (+8.83%)</td><td>0.04 (+3.83%)</td><td>0.01 <b>(-25.20%)</b></td><td>208.00 (-3.70%)</td><td>174.36 (-4.62%)</td><td>178.90 (-8.12%)</td><td>133.00 (+9.11%)</td><td>30.33 <b>(-20.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>182.80 (n/a)</td><td>194.70 (n/a)</td><td>121.90 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (+16.88%)</td><td>0.05 (+12.40%)</td><td>0.05 <b>(+26.28%)</b></td><td>0.04 (-3.87%)</td><td>0.02 <b>(+31.50%)</b></td><td>227.40 (+4.03%)</td><td>164.94 (-8.79%)</td><td>158.10 <b>(-20.83%)</b></td><td>101.20 (-14.38%)</td><td>48.33 (+16.46%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.60 (n/a)</td><td>180.84 (n/a)</td><td>199.70 (n/a)</td><td>118.20 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 <b>(+32.86%)</b></td><td>0.04 (+3.16%)</td><td>0.04 (+1.69%)</td><td>0.03 <b>(-20.57%)</b></td><td>0.01 <b>(+247.99%)</b></td><td>269.10 <b>(+25.87%)</b></td><td>200.10 (+2.03%)</td><td>195.40 (-1.66%)</td><td>128.80 <b>(-24.77%)</b></td><td>50.25 <b>(+224.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.80 (n/a)</td><td>196.12 (n/a)</td><td>198.70 (n/a)</td><td>171.20 (n/a)</td><td>15.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 <b>(+27.44%)</b></td><td>0.04 (+6.51%)</td><td>0.04 (-4.03%)</td><td>0.04 (+4.12%)</td><td>0.01 <b>(+102.47%)</b></td><td>223.90 (-3.95%)</td><td>191.54 (-3.42%)</td><td>203.10 (+4.15%)</td><td>129.00 <b>(-21.53%)</b></td><td>39.63 <b>(+52.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.10 (n/a)</td><td>198.32 (n/a)</td><td>195.00 (n/a)</td><td>164.40 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 <b>(-35.82%)</b></td><td>0.04 (-15.96%)</td><td>0.04 (-7.00%)</td><td>0.03 (-12.66%)</td><td>0.00 <b>(-68.17%)</b></td><td>262.80 (+14.51%)</td><td>226.04 (+14.32%)</td><td>223.20 (+7.51%)</td><td>194.40 <b>(+55.77%)</b></td><td>24.88 <b>(-40.54%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>197.72 (n/a)</td><td>207.60 (n/a)</td><td>124.80 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 <b>(-40.66%)</b></td><td>0.05 (-12.14%)</td><td>0.05 (+10.55%)</td><td>0.04 (-4.03%)</td><td>0.01 <b>(-62.02%)</b></td><td>222.30 (+4.22%)</td><td>169.96 (+4.54%)</td><td>164.30 (-9.53%)</td><td>134.90 <b>(+68.41%)</b></td><td>35.81 <b>(-29.51%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>213.30 (n/a)</td><td>162.58 (n/a)</td><td>181.60 (n/a)</td><td>80.10 (n/a)</td><td>50.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-4.67%)</td><td>0.04 (+9.11%)</td><td>0.04 (+19.89%)</td><td>0.04 <b>(+36.07%)</b></td><td>0.00 <b>(-65.32%)</b></td><td>212.90 <b>(-26.51%)</b></td><td>197.20 (-11.64%)</td><td>193.40 (-16.57%)</td><td>180.10 (+4.89%)</td><td>14.11 <b>(-71.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.70 (n/a)</td><td>223.18 (n/a)</td><td>231.80 (n/a)</td><td>171.70 (n/a)</td><td>50.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (+6.43%)</td><td>0.05 (-5.04%)</td><td>0.05 (-1.08%)</td><td>0.04 (-15.28%)</td><td>0.01 <b>(+46.17%)</b></td><td>226.10 (+18.07%)</td><td>182.40 (+7.42%)</td><td>180.00 (+1.07%)</td><td>130.30 (-6.06%)</td><td>36.55 <b>(+59.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>169.80 (n/a)</td><td>178.10 (n/a)</td><td>138.70 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (+9.15%)</td><td>0.05 (+19.01%)</td><td>0.05 (+1.94%)</td><td>0.04 <b>(+99.50%)</b></td><td>0.01 <b>(-42.81%)</b></td><td>183.90 <b>(-49.86%)</b></td><td>157.62 <b>(-23.64%)</b></td><td>162.20 (-1.88%)</td><td>133.50 (-8.37%)</td><td>22.76 <b>(-75.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>366.80 (n/a)</td><td>206.42 (n/a)</td><td>165.30 (n/a)</td><td>145.70 (n/a)</td><td>91.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-14.61%)</td><td>0.04 (-10.94%)</td><td>0.04 (-7.02%)</td><td>0.03 <b>(-23.14%)</b></td><td>0.01 (-1.42%)</td><td>276.60 <b>(+30.10%)</b></td><td>195.96 (+13.85%)</td><td>185.80 (+7.59%)</td><td>153.90 (+17.12%)</td><td>47.37 <b>(+58.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>172.12 (n/a)</td><td>172.70 (n/a)</td><td>131.40 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-15.21%)</td><td>0.04 (-13.66%)</td><td>0.04 (-8.97%)</td><td>0.04 (-15.18%)</td><td>0.00 <b>(-28.74%)</b></td><td>204.80 (+17.90%)</td><td>185.64 (+15.61%)</td><td>183.90 (+9.86%)</td><td>170.20 (+17.87%)</td><td>13.32 (+0.13%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.70 (n/a)</td><td>160.58 (n/a)</td><td>167.40 (n/a)</td><td>144.40 (n/a)</td><td>13.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-19.04%)</td><td>0.05 (-4.06%)</td><td>0.05 (-11.15%)</td><td>0.04 <b>(+55.22%)</b></td><td>0.00 <b>(-88.48%)</b></td><td>188.10 <b>(-35.56%)</b></td><td>182.04 (-2.17%)</td><td>180.40 (+12.54%)</td><td>175.40 <b>(+23.52%)</b></td><td>5.31 <b>(-91.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.90 (n/a)</td><td>186.08 (n/a)</td><td>160.30 (n/a)</td><td>142.00 (n/a)</td><td>60.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (+0.40%)</td><td>0.05 (+7.55%)</td><td>0.05 (+11.08%)</td><td>0.04 (-0.81%)</td><td>0.01 (+4.62%)</td><td>206.70 (+0.83%)</td><td>169.16 (-6.44%)</td><td>173.90 (-9.99%)</td><td>119.10 (-0.33%)</td><td>38.68 (+11.55%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>180.80 (n/a)</td><td>193.20 (n/a)</td><td>119.50 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>53187.80 (n/a)</td><td>52670.90 (n/a)</td><td>52549.60 (n/a)</td><td>52471.00 (n/a)</td><td>293.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.13 <b>(-22.39%)</b></td><td>0.13 (-17.33%)</td><td>0.13 (-11.90%)</td><td>0.12 (-17.09%)</td><td>0.01 <b>(-55.59%)</b></td><td>210.50 <b>(+20.63%)</b></td><td>191.76 <b>(+20.32%)</b></td><td>190.00 (+13.50%)</td><td>182.40 <b>(+28.81%)</b></td><td>10.95 <b>(-29.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>174.50 (n/a)</td><td>159.38 (n/a)</td><td>167.40 (n/a)</td><td>141.60 (n/a)</td><td>15.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.31 (+0.44%)</td><td>0.25 (+6.47%)</td><td>0.23 (+2.27%)</td><td>0.18 (+0.06%)</td><td>0.05 (+0.95%)</td><td>228.40 (-0.04%)</td><td>172.68 (-6.06%)</td><td>179.00 (-2.24%)</td><td>130.70 (-0.38%)</td><td>38.12 (-0.47%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>228.50 (n/a)</td><td>183.82 (n/a)</td><td>183.10 (n/a)</td><td>131.20 (n/a)</td><td>38.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (+2.96%)</td><td>0.03 (-11.59%)</td><td>0.03 (-11.84%)</td><td>0.02 <b>(-28.46%)</b></td><td>0.01 <b>(+64.55%)</b></td><td>239.80 <b>(+39.83%)</b></td><td>175.96 (+17.73%)</td><td>181.10 (+13.47%)</td><td>123.00 (-2.92%)</td><td>45.98 <b>(+125.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>171.50 (n/a)</td><td>149.46 (n/a)</td><td>159.60 (n/a)</td><td>126.70 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (+9.54%)</td><td>0.05 (-0.93%)</td><td>0.05 (-7.72%)</td><td>0.04 (-3.92%)</td><td>0.01 <b>(+23.85%)</b></td><td>206.50 (+4.08%)</td><td>170.08 (+1.66%)</td><td>171.90 (+8.39%)</td><td>124.50 (-8.72%)</td><td>29.40 (+10.99%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>167.30 (n/a)</td><td>158.60 (n/a)</td><td>136.40 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 <b>(-26.60%)</b></td><td>0.08 (-4.54%)</td><td>0.09 (+13.13%)</td><td>0.06 (+4.40%)</td><td>0.01 <b>(-42.55%)</b></td><td>199.00 (-4.19%)</td><td>153.00 (+1.35%)</td><td>135.10 (-11.58%)</td><td>131.00 <b>(+36.32%)</b></td><td>30.11 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>207.70 (n/a)</td><td>150.96 (n/a)</td><td>152.80 (n/a)</td><td>96.10 (n/a)</td><td>39.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (-19.26%)</td><td>0.05 (-9.48%)</td><td>0.05 (-6.78%)</td><td>0.04 (-8.55%)</td><td>0.01 <b>(-25.79%)</b></td><td>199.70 (+9.36%)</td><td>173.04 (+9.89%)</td><td>175.80 (+7.26%)</td><td>142.70 <b>(+23.87%)</b></td><td>26.64 (+5.31%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>157.46 (n/a)</td><td>163.90 (n/a)</td><td>115.20 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (-16.83%)</td><td>0.06 (-10.05%)</td><td>0.06 (-5.15%)</td><td>0.04 (-17.68%)</td><td>0.02 (-0.44%)</td><td>231.20 <b>(+21.49%)</b></td><td>179.24 (+13.41%)</td><td>166.20 (+5.46%)</td><td>131.00 <b>(+20.29%)</b></td><td>47.73 <b>(+55.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>158.04 (n/a)</td><td>157.60 (n/a)</td><td>108.90 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (-0.94%)</td><td>0.05 (-17.97%)</td><td>0.04 <b>(-22.90%)</b></td><td>0.04 <b>(-21.60%)</b></td><td>0.01 <b>(+26.15%)</b></td><td>226.80 <b>(+27.56%)</b></td><td>188.56 <b>(+24.64%)</b></td><td>197.90 <b>(+29.77%)</b></td><td>123.00 (+0.99%)</td><td>40.14 <b>(+54.94%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.80 (n/a)</td><td>151.28 (n/a)</td><td>152.50 (n/a)</td><td>121.80 (n/a)</td><td>25.91 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (-6.59%)</td><td>0.06 (-10.33%)</td><td>0.05 (-11.44%)</td><td>0.05 (+18.32%)</td><td>0.01 <b>(-33.90%)</b></td><td>201.40 (-15.48%)</td><td>176.30 (+7.76%)</td><td>186.30 (+12.91%)</td><td>130.80 (+7.04%)</td><td>27.54 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>238.30 (n/a)</td><td>163.60 (n/a)</td><td>165.00 (n/a)</td><td>122.20 (n/a)</td><td>46.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 <b>(-21.36%)</b></td><td>0.05 (-7.56%)</td><td>0.04 (-7.42%)</td><td>0.04 (+5.70%)</td><td>0.00 <b>(-73.13%)</b></td><td>189.70 (-5.43%)</td><td>180.50 (+6.10%)</td><td>182.20 (+8.00%)</td><td>167.40 <b>(+27.11%)</b></td><td>8.59 <b>(-67.56%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.60 (n/a)</td><td>170.12 (n/a)</td><td>168.70 (n/a)</td><td>131.70 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (+6.93%)</td><td>0.06 (+0.23%)</td><td>0.05 (-4.19%)</td><td>0.05 (-6.02%)</td><td>0.01 <b>(+47.90%)</b></td><td>195.70 (+6.42%)</td><td>166.54 (+1.56%)</td><td>172.50 (+4.36%)</td><td>121.40 (-6.47%)</td><td>31.69 <b>(+53.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>163.98 (n/a)</td><td>165.30 (n/a)</td><td>129.80 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-15.93%)</td><td>0.04 (-15.22%)</td><td>0.04 <b>(-20.08%)</b></td><td>0.04 (-5.01%)</td><td>0.00 <b>(-49.69%)</b></td><td>195.30 (+5.28%)</td><td>185.32 (+17.17%)</td><td>188.30 <b>(+25.12%)</b></td><td>167.70 (+18.94%)</td><td>11.30 <b>(-37.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>158.16 (n/a)</td><td>150.50 (n/a)</td><td>141.00 (n/a)</td><td>18.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (+0.61%)</td><td>0.06 (-0.95%)</td><td>0.05 (-6.62%)</td><td>0.05 (+12.97%)</td><td>0.01 (-12.75%)</td><td>184.00 (-11.45%)</td><td>167.06 (+0.22%)</td><td>172.90 (+7.13%)</td><td>131.60 (-0.60%)</td><td>21.04 <b>(-24.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>166.70 (n/a)</td><td>161.40 (n/a)</td><td>132.40 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 <b>(-23.19%)</b></td><td>0.04 (-12.49%)</td><td>0.04 (-7.65%)</td><td>0.03 (-16.51%)</td><td>0.01 <b>(-34.46%)</b></td><td>282.90 (+19.77%)</td><td>219.90 (+13.39%)</td><td>209.80 (+8.31%)</td><td>190.00 <b>(+30.23%)</b></td><td>36.49 (+6.46%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.20 (n/a)</td><td>193.94 (n/a)</td><td>193.70 (n/a)</td><td>145.90 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (-11.33%)</td><td>0.05 (-8.23%)</td><td>0.04 (-9.99%)</td><td>0.04 (+5.28%)</td><td>0.01 <b>(-40.87%)</b></td><td>222.70 (-4.99%)</td><td>189.80 (+6.69%)</td><td>196.80 (+11.12%)</td><td>159.20 (+12.75%)</td><td>24.43 <b>(-35.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>177.90 (n/a)</td><td>177.10 (n/a)</td><td>141.20 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 <b>(-33.15%)</b></td><td>0.04 <b>(-23.33%)</b></td><td>0.04 <b>(-20.48%)</b></td><td>0.03 <b>(-26.03%)</b></td><td>0.01 <b>(-43.59%)</b></td><td>252.10 <b>(+35.17%)</b></td><td>207.28 <b>(+28.99%)</b></td><td>211.10 <b>(+25.80%)</b></td><td>166.90 <b>(+49.55%)</b></td><td>34.17 (+16.91%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>160.70 (n/a)</td><td>167.80 (n/a)</td><td>111.60 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (+0.83%)</td><td>0.04 (-6.67%)</td><td>0.04 (-12.58%)</td><td>0.04 (-0.08%)</td><td>0.01 (-11.36%)</td><td>233.70 (+0.09%)</td><td>197.14 (+6.69%)</td><td>196.70 (+14.36%)</td><td>161.10 (-0.80%)</td><td>25.79 (-12.81%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>184.78 (n/a)</td><td>172.00 (n/a)</td><td>162.40 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (-16.84%)</td><td>0.03 <b>(-21.10%)</b></td><td>0.04 (-14.30%)</td><td>0.02 <b>(-43.00%)</b></td><td>0.01 <b>(+109.23%)</b></td><td>371.20 <b>(+75.43%)</b></td><td>251.60 <b>(+32.13%)</b></td><td>223.60 (+16.70%)</td><td>205.70 <b>(+20.22%)</b></td><td>68.71 <b>(+352.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.60 (n/a)</td><td>190.42 (n/a)</td><td>191.60 (n/a)</td><td>171.10 (n/a)</td><td>15.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.61 <b>(-20.22%)</b></td><td>0.56 (-13.88%)</td><td>0.56 (-13.85%)</td><td>0.50 (-6.07%)</td><td>0.05 <b>(-41.48%)</b></td><td>195.20 (+6.43%)</td><td>177.88 (+15.18%)</td><td>176.40 (+16.13%)</td><td>161.40 <b>(+25.41%)</b></td><td>16.67 <b>(-22.17%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.09 (n/a)</td><td>183.40 (n/a)</td><td>154.44 (n/a)</td><td>151.90 (n/a)</td><td>128.70 (n/a)</td><td>21.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.65 <b>(-20.38%)</b></td><td>0.53 <b>(-22.46%)</b></td><td>0.50 <b>(-27.07%)</b></td><td>0.43 (-11.54%)</td><td>0.08 <b>(-31.40%)</b></td><td>228.70 (+13.05%)</td><td>190.38 <b>(+27.58%)</b></td><td>196.80 <b>(+37.14%)</b></td><td>151.30 <b>(+25.56%)</b></td><td>28.91 (-7.37%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.82 (n/a)</td><td>0.68 (n/a)</td><td>0.69 (n/a)</td><td>0.49 (n/a)</td><td>0.12 (n/a)</td><td>202.30 (n/a)</td><td>149.22 (n/a)</td><td>143.50 (n/a)</td><td>120.50 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.63 (-0.09%)</td><td>0.50 (-8.44%)</td><td>0.51 (-13.72%)</td><td>0.39 (-0.81%)</td><td>0.09 (-7.77%)</td><td>253.60 (+0.83%)</td><td>199.74 (+8.68%)</td><td>191.60 (+15.91%)</td><td>154.90 (+0.06%)</td><td>36.11 (-8.47%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.64 (n/a)</td><td>0.55 (n/a)</td><td>0.59 (n/a)</td><td>0.39 (n/a)</td><td>0.10 (n/a)</td><td>251.50 (n/a)</td><td>183.78 (n/a)</td><td>165.30 (n/a)</td><td>154.80 (n/a)</td><td>39.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.64 (+4.15%)</td><td>0.56 (+14.54%)</td><td>0.58 (+19.41%)</td><td>0.49 <b>(+35.36%)</b></td><td>0.07 <b>(-34.11%)</b></td><td>201.70 <b>(-26.12%)</b></td><td>177.54 (-14.78%)</td><td>168.40 (-16.26%)</td><td>154.00 (-3.99%)</td><td>21.38 <b>(-52.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>273.00 (n/a)</td><td>208.32 (n/a)</td><td>201.10 (n/a)</td><td>160.40 (n/a)</td><td>44.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.56 (-1.43%)</td><td>0.45 (-13.12%)</td><td>0.44 (-18.53%)</td><td>0.34 <b>(-21.81%)</b></td><td>0.08 <b>(+30.94%)</b></td><td>214.70 <b>(+27.87%)</b></td><td>169.04 (+16.61%)</td><td>166.00 <b>(+22.78%)</b></td><td>132.20 (+1.46%)</td><td>29.71 <b>(+71.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.57 (n/a)</td><td>0.51 (n/a)</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.06 (n/a)</td><td>167.90 (n/a)</td><td>144.96 (n/a)</td><td>135.20 (n/a)</td><td>130.30 (n/a)</td><td>17.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.53 <b>(-32.39%)</b></td><td>0.40 <b>(-30.62%)</b></td><td>0.40 <b>(-20.04%)</b></td><td>0.29 <b>(-30.36%)</b></td><td>0.09 <b>(-41.80%)</b></td><td>252.40 <b>(+43.57%)</b></td><td>191.54 <b>(+42.03%)</b></td><td>184.70 <b>(+25.05%)</b></td><td>140.20 <b>(+47.89%)</b></td><td>44.05 <b>(+27.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.78 (n/a)</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.16 (n/a)</td><td>175.80 (n/a)</td><td>134.86 (n/a)</td><td>147.70 (n/a)</td><td>94.80 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.59 (+17.93%)</td><td>0.44 (+1.99%)</td><td>0.42 (-3.88%)</td><td>0.29 (-19.31%)</td><td>0.12 <b>(+97.40%)</b></td><td>257.40 <b>(+23.93%)</b></td><td>177.50 (+2.58%)</td><td>174.40 (+4.06%)</td><td>125.30 (-15.22%)</td><td>50.96 <b>(+108.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>207.70 (n/a)</td><td>173.04 (n/a)</td><td>167.60 (n/a)</td><td>147.80 (n/a)</td><td>24.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.46 (-7.97%)</td><td>0.35 (-14.17%)</td><td>0.38 (-8.69%)</td><td>0.25 <b>(-23.44%)</b></td><td>0.09 <b>(+34.88%)</b></td><td>297.30 <b>(+30.62%)</b></td><td>224.66 <b>(+20.62%)</b></td><td>194.30 (+9.53%)</td><td>160.80 (+8.65%)</td><td>60.16 <b>(+98.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>227.60 (n/a)</td><td>186.26 (n/a)</td><td>177.40 (n/a)</td><td>148.00 (n/a)</td><td>30.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (-18.24%)</td><td>0.68 (-18.58%)</td><td>0.63 <b>(-25.60%)</b></td><td>0.54 (-13.77%)</td><td>0.15 (-16.85%)</td><td>243.00 (+15.99%)</td><td>199.02 <b>(+22.79%)</b></td><td>209.10 <b>(+34.38%)</b></td><td>144.70 <b>(+22.32%)</b></td><td>39.34 (+17.62%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.11 (n/a)</td><td>0.84 (n/a)</td><td>0.84 (n/a)</td><td>0.63 (n/a)</td><td>0.18 (n/a)</td><td>209.50 (n/a)</td><td>162.08 (n/a)</td><td>155.60 (n/a)</td><td>118.30 (n/a)</td><td>33.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.04 (-14.63%)</td><td>0.76 (-15.89%)</td><td>0.66 <b>(-21.87%)</b></td><td>0.59 (-18.76%)</td><td>0.19 (-0.59%)</td><td>220.80 <b>(+23.15%)</b></td><td>180.58 <b>(+20.55%)</b></td><td>198.30 <b>(+28.02%)</b></td><td>126.40 (+17.15%)</td><td>39.52 <b>(+47.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.21 (n/a)</td><td>0.90 (n/a)</td><td>0.85 (n/a)</td><td>0.73 (n/a)</td><td>0.19 (n/a)</td><td>179.30 (n/a)</td><td>149.80 (n/a)</td><td>154.90 (n/a)</td><td>107.90 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.97 (-16.62%)</td><td>0.76 (-13.80%)</td><td>0.69 <b>(-20.33%)</b></td><td>0.66 (+6.09%)</td><td>0.13 <b>(-32.05%)</b></td><td>198.90 (-5.73%)</td><td>176.12 (+13.79%)</td><td>189.00 <b>(+25.50%)</b></td><td>134.60 (+19.96%)</td><td>27.61 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.17 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.62 (n/a)</td><td>0.20 (n/a)</td><td>211.00 (n/a)</td><td>154.78 (n/a)</td><td>150.60 (n/a)</td><td>112.20 (n/a)</td><td>36.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-0.15%)</td><td>0.03 (+18.41%)</td><td>0.03 <b>(+21.48%)</b></td><td>0.02 (+18.84%)</td><td>0.00 <b>(-26.23%)</b></td><td>178.80 (-15.86%)</td><td>142.84 (-17.14%)</td><td>135.60 (-17.67%)</td><td>123.20 (+0.16%)</td><td>22.03 <b>(-36.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>172.38 (n/a)</td><td>164.70 (n/a)</td><td>123.00 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-8.15%)</td><td>0.02 (-9.97%)</td><td>0.03 (+0.79%)</td><td>0.02 <b>(-30.91%)</b></td><td>0.01 <b>(+38.10%)</b></td><td>257.90 <b>(+44.81%)</b></td><td>175.74 (+14.82%)</td><td>159.70 (-0.81%)</td><td>138.20 (+8.90%)</td><td>48.27 <b>(+126.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>153.06 (n/a)</td><td>161.00 (n/a)</td><td>126.90 (n/a)</td><td>21.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 <b>(+20.17%)</b></td><td>0.02 (-1.38%)</td><td>0.02 (-8.23%)</td><td>0.02 (-19.53%)</td><td>0.01 <b>(+379.29%)</b></td><td>227.70 <b>(+24.29%)</b></td><td>180.42 (+5.35%)</td><td>184.20 (+8.93%)</td><td>134.90 (-16.78%)</td><td>39.50 <b>(+390.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.20 (n/a)</td><td>171.26 (n/a)</td><td>169.10 (n/a)</td><td>162.10 (n/a)</td><td>8.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.07 <b>(+22.12%)</b></td><td>0.88 (+14.61%)</td><td>0.93 (+18.05%)</td><td>0.64 (+16.51%)</td><td>0.19 <b>(+43.32%)</b></td><td>204.90 (-14.16%)</td><td>155.58 (-11.76%)</td><td>142.20 (-15.31%)</td><td>123.30 (-18.13%)</td><td>35.56 (-1.65%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.88 (n/a)</td><td>0.77 (n/a)</td><td>0.79 (n/a)</td><td>0.55 (n/a)</td><td>0.13 (n/a)</td><td>238.70 (n/a)</td><td>176.32 (n/a)</td><td>167.90 (n/a)</td><td>150.60 (n/a)</td><td>36.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.07 (+15.29%)</td><td>0.93 (+15.62%)</td><td>1.02 <b>(+31.20%)</b></td><td>0.75 (+1.00%)</td><td>0.16 <b>(+116.87%)</b></td><td>176.60 (-1.01%)</td><td>145.60 (-11.84%)</td><td>128.90 <b>(-23.82%)</b></td><td>123.50 (-13.27%)</td><td>26.62 <b>(+89.49%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.93 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.07 (n/a)</td><td>178.40 (n/a)</td><td>165.16 (n/a)</td><td>169.20 (n/a)</td><td>142.40 (n/a)</td><td>14.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.00 (-5.59%)</td><td>0.78 (-5.93%)</td><td>0.75 (-4.19%)</td><td>0.64 (-13.15%)</td><td>0.13 (+2.89%)</td><td>205.30 (+15.14%)</td><td>171.96 (+6.78%)</td><td>176.10 (+4.39%)</td><td>132.40 (+5.92%)</td><td>26.19 <b>(+25.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.13 (n/a)</td><td>178.30 (n/a)</td><td>161.04 (n/a)</td><td>168.70 (n/a)</td><td>125.00 (n/a)</td><td>20.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.09 (+8.44%)</td><td>0.81 (+9.10%)</td><td>0.78 (+11.90%)</td><td>0.70 <b>(+26.06%)</b></td><td>0.16 (-7.44%)</td><td>187.80 <b>(-20.66%)</b></td><td>166.36 (-9.69%)</td><td>168.90 (-10.63%)</td><td>120.80 (-7.79%)</td><td>27.21 <b>(-32.40%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.01 (n/a)</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.17 (n/a)</td><td>236.70 (n/a)</td><td>184.20 (n/a)</td><td>189.00 (n/a)</td><td>131.00 (n/a)</td><td>40.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.93 (-10.19%)</td><td>0.82 (-8.92%)</td><td>0.79 (-8.40%)</td><td>0.74 (-9.74%)</td><td>0.08 (-14.63%)</td><td>179.40 (+10.81%)</td><td>161.70 (+9.69%)</td><td>167.40 (+9.20%)</td><td>141.40 (+11.34%)</td><td>15.69 (+4.57%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td><td>0.86 (n/a)</td><td>0.82 (n/a)</td><td>0.10 (n/a)</td><td>161.90 (n/a)</td><td>147.42 (n/a)</td><td>153.30 (n/a)</td><td>127.00 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-15.24%)</td><td>0.03 (+7.27%)</td><td>0.03 (+1.43%)</td><td>0.02 <b>(+56.15%)</b></td><td>0.00 <b>(-48.67%)</b></td><td>218.30 <b>(-35.94%)</b></td><td>164.30 (-15.65%)</td><td>158.80 (-1.43%)</td><td>139.60 (+18.01%)</td><td>32.12 <b>(-63.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>340.80 (n/a)</td><td>194.78 (n/a)</td><td>161.10 (n/a)</td><td>118.30 (n/a)</td><td>86.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (-1.37%)</td><td>0.03 (-0.02%)</td><td>0.03 (-1.78%)</td><td>0.02 (+17.22%)</td><td>0.00 (-13.13%)</td><td>182.90 (-14.69%)</td><td>155.54 (-1.16%)</td><td>151.70 (+1.81%)</td><td>122.30 (+1.41%)</td><td>26.09 <b>(-25.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>157.36 (n/a)</td><td>149.00 (n/a)</td><td>120.60 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.00 (+0.00%)</td><td>0.00 (-0.93%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.44%)</td><td>0.00 <b>(+28.45%)</b></td><td>1024.81 (+1.63%)</td><td>965.12 (+0.80%)</td><td>950.85 (-0.73%)</td><td>918.88 (+1.63%)</td><td>40.84 (+10.77%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1008.33 (n/a)</td><td>957.48 (n/a)</td><td>957.85 (n/a)</td><td>904.17 (n/a)</td><td>36.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.01 (+3.61%)</td><td>0.01 (+1.76%)</td><td>0.01 (+5.00%)</td><td>0.01 (-9.33%)</td><td>0.00 <b>(+156.72%)</b></td><td>1196.41 (+10.11%)</td><td>1018.59 (-1.06%)</td><td>973.42 (-4.58%)</td><td>949.95 (-3.50%)</td><td>101.44 <b>(+172.48%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1086.60 (n/a)</td><td>1029.55 (n/a)</td><td>1020.13 (n/a)</td><td>984.36 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.98 (-1.64%)</td><td>0.96 (-0.09%)</td><td>0.96 (+0.65%)</td><td>0.95 (-0.03%)</td><td>0.01 <b>(-32.47%)</b></td><td>2218.07 (+0.03%)</td><td>2183.60 (+0.07%)</td><td>2177.30 (-0.64%)</td><td>2136.70 (+1.67%)</td><td>32.27 <b>(-31.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.00 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2217.37 (n/a)</td><td>2181.98 (n/a)</td><td>2191.35 (n/a)</td><td>2101.56 (n/a)</td><td>46.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (-0.41%)</td><td>0.89 (+0.36%)</td><td>0.88 (-0.36%)</td><td>0.87 (+1.17%)</td><td>0.02 (-16.98%)</td><td>2399.15 (-1.16%)</td><td>2366.04 (-0.37%)</td><td>2387.71 (+0.36%)</td><td>2307.61 (+0.41%)</td><td>40.56 (-17.49%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.91 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.86 (n/a)</td><td>0.02 (n/a)</td><td>2427.32 (n/a)</td><td>2374.80 (n/a)</td><td>2379.12 (n/a)</td><td>2298.17 (n/a)</td><td>49.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.58 <b>(-86.15%)</b></td><td>0.56 <b>(-83.73%)</b></td><td>0.56 <b>(-83.67%)</b></td><td>0.54 <b>(-80.96%)</b></td><td>0.01 <b>(-97.16%)</b></td><td>967.90 <b>(+425.18%)</b></td><td>939.50 <b>(+504.88%)</b></td><td>941.90 <b>(+512.42%)</b></td><td>902.80 <b>(+622.24%)</b></td><td>23.78 (+7.88%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.19 (n/a)</td><td>3.43 (n/a)</td><td>3.41 (n/a)</td><td>2.84 (n/a)</td><td>0.50 (n/a)</td><td>184.30 (n/a)</td><td>155.32 (n/a)</td><td>153.80 (n/a)</td><td>125.00 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.65 <b>(-89.33%)</b></td><td>0.63 <b>(-88.29%)</b></td><td>0.63 <b>(-89.19%)</b></td><td>0.61 <b>(-83.97%)</b></td><td>0.02 <b>(-98.26%)</b></td><td>1710.70 <b>(+523.66%)</b></td><td>1654.22 <b>(+729.68%)</b></td><td>1662.00 <b>(+824.87%)</b></td><td>1603.90 <b>(+837.41%)</b></td><td>42.20 (-1.15%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.13 (n/a)</td><td>5.42 (n/a)</td><td>5.83 (n/a)</td><td>3.82 (n/a)</td><td>0.93 (n/a)</td><td>274.30 (n/a)</td><td>199.38 (n/a)</td><td>179.70 (n/a)</td><td>171.10 (n/a)</td><td>42.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.96 <b>(-75.44%)</b></td><td>0.90 <b>(-72.94%)</b></td><td>0.87 <b>(-74.67%)</b></td><td>0.87 <b>(-66.48%)</b></td><td>0.04 <b>(-91.33%)</b></td><td>602.40 <b>(+198.22%)</b></td><td>582.36 <b>(+263.43%)</b></td><td>599.40 <b>(+294.86%)</b></td><td>548.60 <b>(+307.28%)</b></td><td>26.28 (+3.23%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.89 (n/a)</td><td>3.33 (n/a)</td><td>3.45 (n/a)</td><td>2.60 (n/a)</td><td>0.48 (n/a)</td><td>202.00 (n/a)</td><td>160.24 (n/a)</td><td>151.80 (n/a)</td><td>134.70 (n/a)</td><td>25.45 (n/a)</td>
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
