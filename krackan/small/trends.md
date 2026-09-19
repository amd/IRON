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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 <b>(-39.63%)</b></td><td>0.07 (-10.70%)</td><td>0.07 (+0.14%)</td><td>0.07 (+12.22%)</td><td>0.00 <b>(-94.43%)</b></td><td>179.50 (-10.92%)</td><td>175.26 (+6.42%)</td><td>173.50 (-0.12%)</td><td>172.70 <b>(+65.74%)</b></td><td>3.13 <b>(-91.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>201.50 (n/a)</td><td>164.68 (n/a)</td><td>173.70 (n/a)</td><td>104.20 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (-14.17%)</td><td>0.07 (-8.69%)</td><td>0.07 (-6.04%)</td><td>0.06 (-12.59%)</td><td>0.01 <b>(-21.67%)</b></td><td>210.80 (+14.44%)</td><td>186.30 (+9.38%)</td><td>187.10 (+6.43%)</td><td>165.90 (+16.50%)</td><td>17.32 (+6.63%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>170.32 (n/a)</td><td>175.80 (n/a)</td><td>142.40 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 <b>(-28.80%)</b></td><td>0.07 (-16.23%)</td><td>0.07 (-9.27%)</td><td>0.05 (-16.98%)</td><td>0.01 <b>(-49.52%)</b></td><td>228.70 <b>(+20.43%)</b></td><td>191.64 (+17.31%)</td><td>182.20 (+10.22%)</td><td>162.20 <b>(+40.43%)</b></td><td>25.87 (-12.20%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>189.90 (n/a)</td><td>163.36 (n/a)</td><td>165.30 (n/a)</td><td>115.50 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+8.42%)</td><td>0.06 (+4.20%)</td><td>0.06 (+11.66%)</td><td>0.04 <b>(-20.09%)</b></td><td>0.01 <b>(+73.64%)</b></td><td>299.50 <b>(+25.16%)</b></td><td>212.26 (-1.48%)</td><td>194.90 (-10.43%)</td><td>170.90 (-7.77%)</td><td>50.25 <b>(+108.16%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>215.44 (n/a)</td><td>217.60 (n/a)</td><td>185.30 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (+10.23%)</td><td>0.04 (+6.99%)</td><td>0.03 (+8.27%)</td><td>0.03 (+11.89%)</td><td>0.01 (-1.15%)</td><td>178.90 (-10.64%)</td><td>149.52 (-7.21%)</td><td>153.00 (-7.61%)</td><td>110.80 (-9.25%)</td><td>26.50 <b>(-20.10%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>161.14 (n/a)</td><td>165.60 (n/a)</td><td>122.10 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (+12.25%)</td><td>0.04 (+1.34%)</td><td>0.03 (-7.24%)</td><td>0.03 (-4.16%)</td><td>0.01 <b>(+46.66%)</b></td><td>172.00 (+4.31%)</td><td>140.24 (+0.88%)</td><td>150.70 (+7.80%)</td><td>93.00 (-10.92%)</td><td>29.97 <b>(+35.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>164.90 (n/a)</td><td>139.02 (n/a)</td><td>139.80 (n/a)</td><td>104.40 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (-7.39%)</td><td>0.04 (+8.83%)</td><td>0.04 <b>(+21.27%)</b></td><td>0.03 (+14.01%)</td><td>0.00 <b>(-26.31%)</b></td><td>166.40 (-12.28%)</td><td>146.70 (-8.94%)</td><td>134.80 (-17.55%)</td><td>133.30 (+7.94%)</td><td>17.23 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>161.10 (n/a)</td><td>163.50 (n/a)</td><td>123.50 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (+9.64%)</td><td>0.03 (+14.83%)</td><td>0.04 <b>(+37.56%)</b></td><td>0.03 (-6.52%)</td><td>0.01 <b>(+81.87%)</b></td><td>207.40 (+7.02%)</td><td>157.42 (-10.92%)</td><td>135.40 <b>(-27.32%)</b></td><td>133.30 (-8.76%)</td><td>33.76 <b>(+72.88%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.80 (n/a)</td><td>176.72 (n/a)</td><td>186.30 (n/a)</td><td>146.10 (n/a)</td><td>19.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (-2.95%)</td><td>0.03 (+4.25%)</td><td>0.03 (+8.18%)</td><td>0.03 <b>(+20.23%)</b></td><td>0.00 <b>(-41.07%)</b></td><td>198.80 (-16.85%)</td><td>182.56 (-5.65%)</td><td>184.20 (-7.53%)</td><td>155.50 (+3.05%)</td><td>16.48 <b>(-50.03%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.10 (n/a)</td><td>193.50 (n/a)</td><td>199.20 (n/a)</td><td>150.90 (n/a)</td><td>32.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 <b>(+20.76%)</b></td><td>0.03 (+18.13%)</td><td>0.03 (+10.22%)</td><td>0.03 <b>(+34.14%)</b></td><td>0.01 (+9.67%)</td><td>182.10 <b>(-25.43%)</b></td><td>164.14 (-16.08%)</td><td>175.60 (-9.30%)</td><td>119.20 (-17.16%)</td><td>25.84 <b>(-33.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.20 (n/a)</td><td>195.58 (n/a)</td><td>193.60 (n/a)</td><td>143.90 (n/a)</td><td>38.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (+2.87%)</td><td>0.03 (-13.79%)</td><td>0.03 (-18.48%)</td><td>0.02 (-15.89%)</td><td>0.01 <b>(+60.10%)</b></td><td>215.30 (+18.88%)</td><td>179.78 (+17.84%)</td><td>177.70 <b>(+22.64%)</b></td><td>136.00 (-2.79%)</td><td>30.18 <b>(+80.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>152.56 (n/a)</td><td>144.90 (n/a)</td><td>139.90 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (-3.71%)</td><td>0.03 (-7.26%)</td><td>0.03 (-7.59%)</td><td>0.02 (-7.12%)</td><td>0.00 (+5.68%)</td><td>240.80 (+7.69%)</td><td>209.60 (+7.97%)</td><td>202.40 (+8.24%)</td><td>191.60 (+3.85%)</td><td>19.51 (+17.92%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>194.12 (n/a)</td><td>187.00 (n/a)</td><td>184.50 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>175.44 (n/a)</td><td>178.80 (n/a)</td><td>146.90 (n/a)</td><td>20.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>172.84 (n/a)</td><td>168.30 (n/a)</td><td>145.90 (n/a)</td><td>26.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>183.06 (n/a)</td><td>183.20 (n/a)</td><td>143.10 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>262.50 (n/a)</td><td>204.18 (n/a)</td><td>198.60 (n/a)</td><td>153.30 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>407.30 (n/a)</td><td>229.00 (n/a)</td><td>176.50 (n/a)</td><td>156.90 (n/a)</td><td>103.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>192.58 (n/a)</td><td>192.20 (n/a)</td><td>150.80 (n/a)</td><td>38.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>269.60 (n/a)</td><td>202.50 (n/a)</td><td>201.40 (n/a)</td><td>133.40 (n/a)</td><td>53.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>219.70 (n/a)</td><td>180.60 (n/a)</td><td>184.40 (n/a)</td><td>129.00 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.54 (+17.52%)</td><td>3.38 (+4.27%)</td><td>3.18 (-0.70%)</td><td>2.88 (+0.47%)</td><td>0.66 <b>(+74.04%)</b></td><td>477.60 (-0.48%)</td><td>416.94 (-2.65%)</td><td>432.10 (+0.70%)</td><td>303.00 (-14.91%)</td><td>66.66 <b>(+43.57%)</b></td><td>885.88 (+17.52%)</td><td>660.19 (+4.27%)</td><td>621.22 (-0.70%)</td><td>562.02 (+0.47%)</td><td>128.77 <b>(+74.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.86 (n/a)</td><td>3.25 (n/a)</td><td>3.21 (n/a)</td><td>2.87 (n/a)</td><td>0.38 (n/a)</td><td>479.90 (n/a)</td><td>428.28 (n/a)</td><td>429.10 (n/a)</td><td>356.10 (n/a)</td><td>46.43 (n/a)</td><td>753.78 (n/a)</td><td>633.18 (n/a)</td><td>625.58 (n/a)</td><td>559.41 (n/a)</td><td>73.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.94 <b>(+34.36%)</b></td><td>4.03 (+15.94%)</td><td>3.86 (+8.89%)</td><td>3.48 (+10.20%)</td><td>0.55 <b>(+180.20%)</b></td><td>395.40 (-9.27%)</td><td>345.72 (-12.82%)</td><td>356.50 (-8.17%)</td><td>278.30 <b>(-25.59%)</b></td><td>42.84 <b>(+82.47%)</b></td><td>964.45 <b>(+34.36%)</b></td><td>786.98 (+15.94%)</td><td>753.04 (+8.89%)</td><td>678.84 (+10.20%)</td><td>107.11 <b>(+180.20%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.68 (n/a)</td><td>3.48 (n/a)</td><td>3.55 (n/a)</td><td>3.16 (n/a)</td><td>0.20 (n/a)</td><td>435.80 (n/a)</td><td>396.54 (n/a)</td><td>388.20 (n/a)</td><td>374.00 (n/a)</td><td>23.48 (n/a)</td><td>717.82 (n/a)</td><td>678.80 (n/a)</td><td>691.54 (n/a)</td><td>616.00 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.36 (+9.16%)</td><td>4.32 (+8.53%)</td><td>3.98 (+13.96%)</td><td>3.31 (-0.11%)</td><td>1.18 (+12.19%)</td><td>416.20 (+0.12%)</td><td>334.52 (-7.44%)</td><td>346.00 (-12.25%)</td><td>216.40 (-8.38%)</td><td>72.66 (-0.28%)</td><td>1240.51 (+9.16%)</td><td>841.75 (+8.53%)</td><td>775.74 (+13.96%)</td><td>644.95 (-0.11%)</td><td>229.99 (+12.19%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.83 (n/a)</td><td>3.98 (n/a)</td><td>3.49 (n/a)</td><td>3.31 (n/a)</td><td>1.05 (n/a)</td><td>415.70 (n/a)</td><td>361.42 (n/a)</td><td>394.30 (n/a)</td><td>236.20 (n/a)</td><td>72.86 (n/a)</td><td>1136.43 (n/a)</td><td>775.59 (n/a)</td><td>680.72 (n/a)</td><td>645.68 (n/a)</td><td>205.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.83 <b>(+21.52%)</b></td><td>4.40 (-10.79%)</td><td>4.00 <b>(-20.28%)</b></td><td>3.46 (-9.24%)</td><td>1.38 <b>(+93.62%)</b></td><td>397.60 (+10.20%)</td><td>331.92 (+16.67%)</td><td>344.10 <b>(+25.40%)</b></td><td>201.50 (-17.72%)</td><td>76.32 <b>(+65.26%)</b></td><td>1332.23 <b>(+21.52%)</b></td><td>857.78 (-10.79%)</td><td>780.01 <b>(-20.28%)</b></td><td>675.20 (-9.24%)</td><td>268.96 <b>(+93.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.62 (n/a)</td><td>4.93 (n/a)</td><td>5.02 (n/a)</td><td>3.81 (n/a)</td><td>0.71 (n/a)</td><td>360.80 (n/a)</td><td>284.50 (n/a)</td><td>274.40 (n/a)</td><td>244.90 (n/a)</td><td>46.18 (n/a)</td><td>1096.30 (n/a)</td><td>961.52 (n/a)</td><td>978.40 (n/a)</td><td>743.95 (n/a)</td><td>138.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.34 (-6.11%)</td><td>3.16 (-2.58%)</td><td>3.32 (+5.44%)</td><td>2.85 (-4.48%)</td><td>0.23 (-14.00%)</td><td>482.40 (+4.69%)</td><td>437.18 (+2.56%)</td><td>414.40 (-5.17%)</td><td>412.00 (+6.51%)</td><td>33.30 (-4.52%)</td><td>651.55 (-6.11%)</td><td>616.80 (-2.58%)</td><td>647.72 (+5.44%)</td><td>556.50 (-4.48%)</td><td>45.38 (-14.00%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.56 (n/a)</td><td>3.25 (n/a)</td><td>3.15 (n/a)</td><td>2.99 (n/a)</td><td>0.27 (n/a)</td><td>460.80 (n/a)</td><td>426.28 (n/a)</td><td>437.00 (n/a)</td><td>386.80 (n/a)</td><td>34.88 (n/a)</td><td>693.93 (n/a)</td><td>633.16 (n/a)</td><td>614.31 (n/a)</td><td>582.60 (n/a)</td><td>52.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.74 <b>(+40.09%)</b></td><td>1.21 (+9.23%)</td><td>1.07 (+2.26%)</td><td>1.01 (-0.59%)</td><td>0.30 <b>(+176.02%)</b></td><td>396.10 (+0.58%)</td><td>344.06 (-5.56%)</td><td>376.80 (-2.21%)</td><td>231.30 <b>(-28.63%)</b></td><td>66.36 <b>(+93.27%)</b></td><td>145.04 <b>(+40.09%)</b></td><td>101.35 (+9.23%)</td><td>89.06 (+2.26%)</td><td>84.71 (-0.59%)</td><td>24.98 <b>(+176.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.24 (n/a)</td><td>1.11 (n/a)</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>0.11 (n/a)</td><td>393.80 (n/a)</td><td>364.30 (n/a)</td><td>385.30 (n/a)</td><td>324.10 (n/a)</td><td>34.33 (n/a)</td><td>103.53 (n/a)</td><td>92.79 (n/a)</td><td>87.09 (n/a)</td><td>85.21 (n/a)</td><td>9.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>5.22 <b>(-21.78%)</b></td><td>4.79 (-9.59%)</td><td>4.88 (-0.14%)</td><td>4.16 (-12.88%)</td><td>0.47 <b>(-41.69%)</b></td><td>464.90 (+14.76%)</td><td>407.02 (+9.73%)</td><td>396.50 (+0.13%)</td><td>370.30 <b>(+27.87%)</b></td><td>41.01 (-14.66%)</td><td>1087.48 <b>(-21.78%)</b></td><td>997.04 (-9.59%)</td><td>1015.40 (-0.14%)</td><td>866.02 (-12.88%)</td><td>96.97 <b>(-41.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>6.68 (n/a)</td><td>5.29 (n/a)</td><td>4.88 (n/a)</td><td>4.77 (n/a)</td><td>0.80 (n/a)</td><td>405.10 (n/a)</td><td>370.92 (n/a)</td><td>396.00 (n/a)</td><td>289.60 (n/a)</td><td>48.05 (n/a)</td><td>1390.28 (n/a)</td><td>1102.75 (n/a)</td><td>1016.82 (n/a)</td><td>994.03 (n/a)</td><td>166.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>15.23 (+1.20%)</td><td>11.76 (-6.60%)</td><td>11.26 (-7.53%)</td><td>10.23 (-7.52%)</td><td>2.05 <b>(+24.18%)</b></td><td>538.00 (+8.14%)</td><td>478.06 (+7.92%)</td><td>489.00 (+8.14%)</td><td>361.50 (-1.18%)</td><td>71.74 <b>(+30.94%)</b></td><td>5940.35 (+1.20%)</td><td>4587.19 (-6.60%)</td><td>4391.48 (-7.53%)</td><td>3991.65 (-7.52%)</td><td>798.05 <b>(+24.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>15.05 (n/a)</td><td>12.59 (n/a)</td><td>12.17 (n/a)</td><td>11.06 (n/a)</td><td>1.65 (n/a)</td><td>497.50 (n/a)</td><td>442.98 (n/a)</td><td>452.20 (n/a)</td><td>365.80 (n/a)</td><td>54.79 (n/a)</td><td>5869.91 (n/a)</td><td>4911.19 (n/a)</td><td>4749.17 (n/a)</td><td>4316.32 (n/a)</td><td>642.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>143.82 (n/a)</td><td>147.20 (n/a)</td><td>113.20 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>179.70 (n/a)</td><td>148.44 (n/a)</td><td>149.00 (n/a)</td><td>119.00 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>186.82 (n/a)</td><td>178.30 (n/a)</td><td>137.80 (n/a)</td><td>35.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>165.66 (n/a)</td><td>166.20 (n/a)</td><td>135.70 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>291.70 (n/a)</td><td>184.26 (n/a)</td><td>171.00 (n/a)</td><td>120.00 (n/a)</td><td>65.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>174.30 (n/a)</td><td>181.30 (n/a)</td><td>150.50 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>174.54 (n/a)</td><td>181.00 (n/a)</td><td>145.10 (n/a)</td><td>17.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>203.34 (n/a)</td><td>209.70 (n/a)</td><td>165.70 (n/a)</td><td>25.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.27 (+4.31%)</td><td>3.82 (-1.87%)</td><td>3.66 (-9.43%)</td><td>3.49 (-0.57%)</td><td>0.38 <b>(+49.79%)</b></td><td>2693.60 (+0.58%)</td><td>2480.38 (+2.33%)</td><td>2569.70 (+10.42%)</td><td>2203.30 (-4.13%)</td><td>239.67 <b>(+45.26%)</b></td><td>1679.05 (+4.31%)</td><td>1502.99 (-1.87%)</td><td>1439.61 (-9.43%)</td><td>1373.41 (-0.57%)</td><td>149.31 <b>(+49.79%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>4.09 (n/a)</td><td>3.89 (n/a)</td><td>4.04 (n/a)</td><td>3.51 (n/a)</td><td>0.25 (n/a)</td><td>2678.20 (n/a)</td><td>2423.84 (n/a)</td><td>2327.30 (n/a)</td><td>2298.20 (n/a)</td><td>164.99 (n/a)</td><td>1609.68 (n/a)</td><td>1531.67 (n/a)</td><td>1589.54 (n/a)</td><td>1381.29 (n/a)</td><td>99.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.00 <b>(-38.05%)</b></td><td>0.85 <b>(-21.09%)</b></td><td>0.90 (-12.69%)</td><td>0.63 (-19.78%)</td><td>0.15 <b>(-50.18%)</b></td><td>352.00 <b>(+24.65%)</b></td><td>266.66 <b>(+23.56%)</b></td><td>247.10 (+14.50%)</td><td>222.30 <b>(+61.44%)</b></td><td>54.09 (+4.46%)</td><td>42.45 <b>(-38.05%)</b></td><td>36.45 <b>(-21.09%)</b></td><td>38.19 (-12.69%)</td><td>26.81 (-19.78%)</td><td>6.58 <b>(-50.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.61 (n/a)</td><td>1.08 (n/a)</td><td>1.03 (n/a)</td><td>0.78 (n/a)</td><td>0.31 (n/a)</td><td>282.40 (n/a)</td><td>215.82 (n/a)</td><td>215.80 (n/a)</td><td>137.70 (n/a)</td><td>51.79 (n/a)</td><td>68.53 (n/a)</td><td>46.19 (n/a)</td><td>43.74 (n/a)</td><td>33.42 (n/a)</td><td>13.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.07 (-0.23%)</td><td>0.92 (+7.83%)</td><td>1.02 (+10.79%)</td><td>0.66 (+4.44%)</td><td>0.17 (+1.24%)</td><td>334.50 (-4.24%)</td><td>247.44 (-7.37%)</td><td>216.10 (-9.73%)</td><td>207.30 (+0.24%)</td><td>54.24 (-5.11%)</td><td>45.52 (-0.23%)</td><td>39.44 (+7.83%)</td><td>43.68 (+10.79%)</td><td>28.22 (+4.44%)</td><td>7.45 (+1.24%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.07 (n/a)</td><td>0.86 (n/a)</td><td>0.92 (n/a)</td><td>0.63 (n/a)</td><td>0.17 (n/a)</td><td>349.30 (n/a)</td><td>267.12 (n/a)</td><td>239.40 (n/a)</td><td>206.80 (n/a)</td><td>57.16 (n/a)</td><td>45.63 (n/a)</td><td>36.57 (n/a)</td><td>39.43 (n/a)</td><td>27.02 (n/a)</td><td>7.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.53 (-0.04%)</td><td>0.53 (-0.04%)</td><td>0.53 (-0.01%)</td><td>0.52 (-0.23%)</td><td>0.00 <b>(+72.92%)</b></td><td>48004.50 (+0.23%)</td><td>47843.80 (+0.04%)</td><td>47820.40 (+0.01%)</td><td>47776.90 (+0.04%)</td><td>93.21 <b>(+73.32%)</b></td><td>359.59 (-0.04%)</td><td>359.08 (-0.04%)</td><td>359.26 (-0.01%)</td><td>357.88 (-0.23%)</td><td>0.70 <b>(+72.91%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47892.30 (n/a)</td><td>47824.48 (n/a)</td><td>47814.10 (n/a)</td><td>47758.10 (n/a)</td><td>53.78 (n/a)</td><td>359.73 (n/a)</td><td>359.23 (n/a)</td><td>359.31 (n/a)</td><td>358.72 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.92 (+1.60%)</td><td>0.91 (+1.08%)</td><td>0.91 (+1.26%)</td><td>0.91 (+0.85%)</td><td>0.01 <b>(+49.18%)</b></td><td>27804.50 (-0.84%)</td><td>27629.30 (-1.07%)</td><td>27646.50 (-1.25%)</td><td>27344.30 (-1.57%)</td><td>188.62 <b>(+45.70%)</b></td><td>628.28 (+1.60%)</td><td>621.82 (+1.08%)</td><td>621.41 (+1.26%)</td><td>617.88 (+0.85%)</td><td>4.26 <b>(+49.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28040.80 (n/a)</td><td>27927.42 (n/a)</td><td>27995.20 (n/a)</td><td>27780.70 (n/a)</td><td>129.46 (n/a)</td><td>618.41 (n/a)</td><td>615.17 (n/a)</td><td>613.67 (n/a)</td><td>612.68 (n/a)</td><td>2.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.31 (-0.29%)</td><td>3.19 (-0.28%)</td><td>3.17 (-0.28%)</td><td>3.10 (-0.91%)</td><td>0.08 (+4.66%)</td><td>8114.10 (+0.92%)</td><td>7899.74 (+0.29%)</td><td>7929.90 (+0.28%)</td><td>7597.30 (+0.29%)</td><td>188.42 (+5.96%)</td><td>2261.30 (-0.29%)</td><td>2175.74 (-0.28%)</td><td>2166.46 (-0.28%)</td><td>2117.28 (-0.91%)</td><td>52.76 (+4.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.32 (n/a)</td><td>3.20 (n/a)</td><td>3.18 (n/a)</td><td>3.13 (n/a)</td><td>0.07 (n/a)</td><td>8040.30 (n/a)</td><td>7877.10 (n/a)</td><td>7908.00 (n/a)</td><td>7575.30 (n/a)</td><td>177.82 (n/a)</td><td>2267.88 (n/a)</td><td>2181.91 (n/a)</td><td>2172.47 (n/a)</td><td>2136.73 (n/a)</td><td>50.41 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.17 (+7.40%)</td><td>3.58 (+0.24%)</td><td>3.69 (-3.64%)</td><td>2.98 (+2.05%)</td><td>0.56 <b>(+33.06%)</b></td><td>2703.20 (-2.01%)</td><td>2294.56 (+0.55%)</td><td>2181.70 (+3.78%)</td><td>1933.00 (-6.89%)</td><td>366.08 <b>(+24.28%)</b></td><td>1093.61 (+7.40%)</td><td>939.87 (+0.24%)</td><td>968.93 (-3.64%)</td><td>782.01 (+2.05%)</td><td>145.93 <b>(+33.06%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.88 (n/a)</td><td>3.58 (n/a)</td><td>3.83 (n/a)</td><td>2.92 (n/a)</td><td>0.42 (n/a)</td><td>2758.60 (n/a)</td><td>2282.02 (n/a)</td><td>2102.20 (n/a)</td><td>2076.00 (n/a)</td><td>294.56 (n/a)</td><td>1018.25 (n/a)</td><td>937.63 (n/a)</td><td>1005.57 (n/a)</td><td>766.31 (n/a)</td><td>109.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.48 (+1.74%)</td><td>0.36 (+2.39%)</td><td>0.35 (+8.32%)</td><td>0.28 (-13.38%)</td><td>0.08 (+10.76%)</td><td>4525.20 (+15.44%)</td><td>3541.52 (-1.51%)</td><td>3550.80 (-7.68%)</td><td>2569.00 (-1.71%)</td><td>691.99 <b>(+24.93%)</b></td><td>26.12 (+1.74%)</td><td>19.57 (+2.39%)</td><td>18.90 (+8.32%)</td><td>14.83 (-13.38%)</td><td>4.08 (+10.76%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>3919.90 (n/a)</td><td>3595.82 (n/a)</td><td>3846.10 (n/a)</td><td>2613.70 (n/a)</td><td>553.90 (n/a)</td><td>25.68 (n/a)</td><td>19.12 (n/a)</td><td>17.45 (n/a)</td><td>17.12 (n/a)</td><td>3.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.06 <b>(+22.11%)</b></td><td>5.06 <b>(+29.11%)</b></td><td>4.86 <b>(+34.93%)</b></td><td>4.66 <b>(+48.23%)</b></td><td>0.57 <b>(-34.29%)</b></td><td>1427.50 <b>(-32.54%)</b></td><td>1325.32 <b>(-24.72%)</b></td><td>1367.90 <b>(-25.88%)</b></td><td>1097.60 (-18.11%)</td><td>130.41 <b>(-64.53%)</b></td><td>1872.37 <b>(+22.11%)</b></td><td>1564.44 <b>(+29.11%)</b></td><td>1502.47 <b>(+34.93%)</b></td><td>1439.68 <b>(+48.23%)</b></td><td>174.75 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>4.96 (n/a)</td><td>3.92 (n/a)</td><td>3.60 (n/a)</td><td>3.14 (n/a)</td><td>0.86 (n/a)</td><td>2116.00 (n/a)</td><td>1760.48 (n/a)</td><td>1845.60 (n/a)</td><td>1340.30 (n/a)</td><td>367.62 (n/a)</td><td>1533.38 (n/a)</td><td>1211.67 (n/a)</td><td>1113.56 (n/a)</td><td>971.27 (n/a)</td><td>265.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>13.51 (n/a)</td><td>13.05 (n/a)</td><td>13.16 (n/a)</td><td>12.25 (n/a)</td><td>0.50 (n/a)</td><td>13.50 (n/a)</td><td>13.04 (n/a)</td><td>13.16 (n/a)</td><td>12.24 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>25.08 (-1.28%)</td><td>24.70 (-0.34%)</td><td>24.77 (+0.60%)</td><td>24.25 (+0.20%)</td><td>0.33 <b>(-33.86%)</b></td><td>25.07 (-1.28%)</td><td>24.68 (-0.34%)</td><td>24.76 (+0.60%)</td><td>24.24 (+0.20%)</td><td>0.33 <b>(-33.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>25.41 (n/a)</td><td>24.78 (n/a)</td><td>24.63 (n/a)</td><td>24.20 (n/a)</td><td>0.49 (n/a)</td><td>25.39 (n/a)</td><td>24.77 (n/a)</td><td>24.61 (n/a)</td><td>24.19 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>44.00 (+6.91%)</td><td>41.95 (+5.21%)</td><td>42.56 (+7.04%)</td><td>39.41 (+2.10%)</td><td>1.80 <b>(+84.59%)</b></td><td>43.97 (+6.91%)</td><td>41.93 (+5.21%)</td><td>42.54 (+7.04%)</td><td>39.39 (+2.10%)</td><td>1.80 <b>(+84.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>41.16 (n/a)</td><td>39.87 (n/a)</td><td>39.77 (n/a)</td><td>38.60 (n/a)</td><td>0.98 (n/a)</td><td>41.13 (n/a)</td><td>39.85 (n/a)</td><td>39.74 (n/a)</td><td>38.58 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>45.27 (-3.70%)</td><td>43.66 (-2.08%)</td><td>43.38 (-4.40%)</td><td>42.78 (+0.66%)</td><td>0.95 <b>(-52.62%)</b></td><td>45.24 (-3.70%)</td><td>43.63 (-2.08%)</td><td>43.35 (-4.40%)</td><td>42.75 (+0.66%)</td><td>0.95 <b>(-52.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>47.01 (n/a)</td><td>44.58 (n/a)</td><td>45.38 (n/a)</td><td>42.50 (n/a)</td><td>2.01 (n/a)</td><td>46.98 (n/a)</td><td>44.56 (n/a)</td><td>45.35 (n/a)</td><td>42.47 (n/a)</td><td>2.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>13.47 (n/a)</td><td>12.44 (n/a)</td><td>12.22 (n/a)</td><td>11.12 (n/a)</td><td>0.94 (n/a)</td><td>13.47 (n/a)</td><td>12.43 (n/a)</td><td>12.21 (n/a)</td><td>11.11 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>25.68 (+5.29%)</td><td>24.47 (+8.74%)</td><td>24.72 (+3.16%)</td><td>22.84 <b>(+30.79%)</b></td><td>1.06 <b>(-63.58%)</b></td><td>25.66 (+5.29%)</td><td>24.46 (+8.74%)</td><td>24.70 (+3.16%)</td><td>22.83 <b>(+30.79%)</b></td><td>1.05 <b>(-63.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>24.39 (n/a)</td><td>22.50 (n/a)</td><td>23.96 (n/a)</td><td>17.47 (n/a)</td><td>2.90 (n/a)</td><td>24.37 (n/a)</td><td>22.49 (n/a)</td><td>23.94 (n/a)</td><td>17.46 (n/a)</td><td>2.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>42.69 (+4.39%)</td><td>40.96 (+6.36%)</td><td>40.75 (+4.82%)</td><td>38.88 (+14.05%)</td><td>1.55 <b>(-40.86%)</b></td><td>42.66 (+4.39%)</td><td>40.94 (+6.36%)</td><td>40.73 (+4.82%)</td><td>38.85 (+14.05%)</td><td>1.55 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>40.89 (n/a)</td><td>38.51 (n/a)</td><td>38.88 (n/a)</td><td>34.09 (n/a)</td><td>2.63 (n/a)</td><td>40.87 (n/a)</td><td>38.49 (n/a)</td><td>38.85 (n/a)</td><td>34.07 (n/a)</td><td>2.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>47.19 (+4.09%)</td><td>43.65 (-0.07%)</td><td>43.27 (-1.81%)</td><td>38.68 (-4.25%)</td><td>3.28 <b>(+61.12%)</b></td><td>47.16 (+4.09%)</td><td>43.62 (-0.07%)</td><td>43.24 (-1.81%)</td><td>38.66 (-4.25%)</td><td>3.28 <b>(+61.12%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>45.34 (n/a)</td><td>43.68 (n/a)</td><td>44.06 (n/a)</td><td>40.40 (n/a)</td><td>2.04 (n/a)</td><td>45.31 (n/a)</td><td>43.65 (n/a)</td><td>44.04 (n/a)</td><td>40.37 (n/a)</td><td>2.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>10.02 (+1.91%)</td><td>9.02 (-0.11%)</td><td>8.78 (-0.34%)</td><td>8.47 (+0.03%)</td><td>0.64 (+13.40%)</td><td>10.00 (+1.91%)</td><td>9.01 (-0.11%)</td><td>8.76 (-0.34%)</td><td>8.45 (+0.03%)</td><td>0.64 (+13.40%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>9.84 (n/a)</td><td>9.03 (n/a)</td><td>8.81 (n/a)</td><td>8.47 (n/a)</td><td>0.56 (n/a)</td><td>9.82 (n/a)</td><td>9.02 (n/a)</td><td>8.79 (n/a)</td><td>8.45 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.91 (-5.39%)</td><td>0.85 (-2.74%)</td><td>0.86 (-0.44%)</td><td>0.79 (-3.64%)</td><td>0.05 (-1.41%)</td><td>0.90 (-5.39%)</td><td>0.84 (-2.74%)</td><td>0.85 (-0.44%)</td><td>0.78 (-3.64%)</td><td>0.05 (-1.41%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.96 (n/a)</td><td>0.87 (n/a)</td><td>0.86 (n/a)</td><td>0.82 (n/a)</td><td>0.06 (n/a)</td><td>0.95 (n/a)</td><td>0.86 (n/a)</td><td>0.85 (n/a)</td><td>0.81 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.17 (-3.34%)</td><td>1.13 (+4.58%)</td><td>1.15 (+3.21%)</td><td>1.08 (+19.52%)</td><td>0.04 <b>(-64.82%)</b></td><td>1.16 (-3.34%)</td><td>1.12 (+4.58%)</td><td>1.13 (+3.21%)</td><td>1.06 (+19.52%)</td><td>0.04 <b>(-64.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.21 (n/a)</td><td>1.08 (n/a)</td><td>1.11 (n/a)</td><td>0.90 (n/a)</td><td>0.12 (n/a)</td><td>1.20 (n/a)</td><td>1.07 (n/a)</td><td>1.10 (n/a)</td><td>0.89 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>18.41 (+4.11%)</td><td>17.26 (+11.97%)</td><td>16.96 (+9.78%)</td><td>16.27 <b>(+21.57%)</b></td><td>0.93 <b>(-43.76%)</b></td><td>18.20 (+4.11%)</td><td>17.06 (+11.97%)</td><td>16.76 (+9.78%)</td><td>16.08 <b>(+21.57%)</b></td><td>0.92 <b>(-43.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>17.69 (n/a)</td><td>15.42 (n/a)</td><td>15.45 (n/a)</td><td>13.38 (n/a)</td><td>1.65 (n/a)</td><td>17.48 (n/a)</td><td>15.24 (n/a)</td><td>15.27 (n/a)</td><td>13.23 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>14.01 (+6.05%)</td><td>13.23 (+4.58%)</td><td>12.99 (+3.90%)</td><td>12.65 (+5.85%)</td><td>0.54 (+2.15%)</td><td>13.77 (+6.05%)</td><td>12.99 (+4.58%)</td><td>12.76 (+3.90%)</td><td>12.43 (+5.85%)</td><td>0.53 (+2.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>13.21 (n/a)</td><td>12.65 (n/a)</td><td>12.50 (n/a)</td><td>11.95 (n/a)</td><td>0.53 (n/a)</td><td>12.98 (n/a)</td><td>12.43 (n/a)</td><td>12.28 (n/a)</td><td>11.74 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>8.63 (-2.66%)</td><td>7.87 (+0.62%)</td><td>8.04 (+7.63%)</td><td>6.84 (-4.34%)</td><td>0.66 (-16.39%)</td><td>8.48 (-2.66%)</td><td>7.73 (+0.62%)</td><td>7.90 (+7.63%)</td><td>6.73 (-4.34%)</td><td>0.65 (-16.39%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>8.86 (n/a)</td><td>7.82 (n/a)</td><td>7.47 (n/a)</td><td>7.16 (n/a)</td><td>0.79 (n/a)</td><td>8.71 (n/a)</td><td>7.69 (n/a)</td><td>7.34 (n/a)</td><td>7.03 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>5.98 (-14.89%)</td><td>5.57 (-2.57%)</td><td>5.64 (+0.53%)</td><td>4.83 (+7.60%)</td><td>0.46 <b>(-49.18%)</b></td><td>5.89 (-14.89%)</td><td>5.48 (-2.57%)</td><td>5.55 (+0.53%)</td><td>4.76 (+7.60%)</td><td>0.45 <b>(-49.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>7.03 (n/a)</td><td>5.71 (n/a)</td><td>5.61 (n/a)</td><td>4.49 (n/a)</td><td>0.91 (n/a)</td><td>6.92 (n/a)</td><td>5.62 (n/a)</td><td>5.52 (n/a)</td><td>4.42 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>13.36 (n/a)</td><td>12.25 (n/a)</td><td>12.12 (n/a)</td><td>11.45 (n/a)</td><td>0.69 (n/a)</td><td>13.35 (n/a)</td><td>12.25 (n/a)</td><td>12.12 (n/a)</td><td>11.45 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>13.31 (n/a)</td><td>13.02 (n/a)</td><td>13.24 (n/a)</td><td>12.16 (n/a)</td><td>0.49 (n/a)</td><td>13.30 (n/a)</td><td>13.01 (n/a)</td><td>13.23 (n/a)</td><td>12.15 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>154.66 (n/a)</td><td>156.60 (n/a)</td><td>112.70 (n/a)</td><td>31.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>144.98 (n/a)</td><td>162.10 (n/a)</td><td>106.40 (n/a)</td><td>36.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.10 (n/a)</td><td>196.32 (n/a)</td><td>183.80 (n/a)</td><td>163.40 (n/a)</td><td>47.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>189.96 (n/a)</td><td>203.00 (n/a)</td><td>125.10 (n/a)</td><td>37.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>179.06 (n/a)</td><td>198.60 (n/a)</td><td>140.30 (n/a)</td><td>35.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.20 (n/a)</td><td>183.76 (n/a)</td><td>180.20 (n/a)</td><td>150.80 (n/a)</td><td>41.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>189.16 (n/a)</td><td>181.10 (n/a)</td><td>176.00 (n/a)</td><td>15.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>368.70 (n/a)</td><td>280.50 (n/a)</td><td>337.70 (n/a)</td><td>160.30 (n/a)</td><td>100.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+19.65%)</td><td>0.06 <b>(+34.67%)</b></td><td>0.06 <b>(+48.81%)</b></td><td>0.05 <b>(+26.61%)</b></td><td>0.01 (+12.06%)</td><td>175.10 <b>(-21.02%)</b></td><td>146.56 <b>(-25.98%)</b></td><td>139.20 <b>(-32.79%)</b></td><td>122.30 (-16.40%)</td><td>23.17 <b>(-23.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.70 (n/a)</td><td>198.00 (n/a)</td><td>207.10 (n/a)</td><td>146.30 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (+11.16%)</td><td>0.05 (+9.57%)</td><td>0.05 (+16.98%)</td><td>0.04 (-1.47%)</td><td>0.01 <b>(+80.98%)</b></td><td>187.20 (+1.46%)</td><td>160.00 (-7.99%)</td><td>151.20 (-14.48%)</td><td>139.10 (-10.08%)</td><td>20.19 <b>(+66.73%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>184.50 (n/a)</td><td>173.90 (n/a)</td><td>176.80 (n/a)</td><td>154.70 (n/a)</td><td>12.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-14.61%)</td><td>0.05 (-14.34%)</td><td>0.05 (-13.54%)</td><td>0.04 (-18.77%)</td><td>0.01 (-1.34%)</td><td>203.40 <b>(+23.12%)</b></td><td>177.30 (+17.20%)</td><td>179.30 (+15.68%)</td><td>147.80 (+17.12%)</td><td>22.67 <b>(+42.51%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.20 (n/a)</td><td>151.28 (n/a)</td><td>155.00 (n/a)</td><td>126.20 (n/a)</td><td>15.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+17.15%)</td><td>0.05 (+18.67%)</td><td>0.05 (+11.39%)</td><td>0.04 (+10.62%)</td><td>0.01 <b>(+64.34%)</b></td><td>202.90 (-9.58%)</td><td>158.84 (-13.73%)</td><td>169.60 (-10.22%)</td><td>120.20 (-14.63%)</td><td>37.16 <b>(+22.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>184.12 (n/a)</td><td>188.90 (n/a)</td><td>140.80 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-4.99%)</td><td>0.05 (-0.77%)</td><td>0.05 (-5.75%)</td><td>0.04 (+14.95%)</td><td>0.01 (-14.62%)</td><td>201.60 (-12.99%)</td><td>166.06 (-0.82%)</td><td>173.60 (+6.11%)</td><td>126.60 (+5.24%)</td><td>33.26 <b>(-22.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>167.44 (n/a)</td><td>163.60 (n/a)</td><td>120.30 (n/a)</td><td>42.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+6.84%)</td><td>0.05 (-6.90%)</td><td>0.04 (-11.14%)</td><td>0.04 (-15.84%)</td><td>0.01 <b>(+63.31%)</b></td><td>216.00 (+18.81%)</td><td>182.80 (+10.48%)</td><td>194.70 (+12.54%)</td><td>121.90 (-6.37%)</td><td>37.98 <b>(+80.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>165.46 (n/a)</td><td>173.00 (n/a)</td><td>130.20 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+6.79%)</td><td>0.05 (-10.05%)</td><td>0.04 (-16.14%)</td><td>0.04 <b>(-21.36%)</b></td><td>0.01 <b>(+81.16%)</b></td><td>218.60 <b>(+27.17%)</b></td><td>180.84 (+15.46%)</td><td>199.70 (+19.30%)</td><td>118.20 (-6.41%)</td><td>41.50 <b>(+114.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.90 (n/a)</td><td>156.62 (n/a)</td><td>167.40 (n/a)</td><td>126.30 (n/a)</td><td>19.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 <b>(-24.60%)</b></td><td>0.04 (-15.58%)</td><td>0.04 (-6.39%)</td><td>0.04 (-4.32%)</td><td>0.00 <b>(-64.85%)</b></td><td>213.80 (+4.55%)</td><td>196.12 (+15.50%)</td><td>198.70 (+6.83%)</td><td>171.20 <b>(+32.71%)</b></td><td>15.50 <b>(-51.65%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>169.80 (n/a)</td><td>186.00 (n/a)</td><td>129.00 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (-7.00%)</td><td>0.04 (+2.80%)</td><td>0.04 (+0.47%)</td><td>0.04 <b>(+41.04%)</b></td><td>0.01 <b>(-45.96%)</b></td><td>233.10 <b>(-29.11%)</b></td><td>198.32 (-7.40%)</td><td>195.00 (-0.46%)</td><td>164.40 (+7.52%)</td><td>25.93 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.80 (n/a)</td><td>214.16 (n/a)</td><td>195.90 (n/a)</td><td>152.90 (n/a)</td><td>66.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (-4.92%)</td><td>0.04 (+3.53%)</td><td>0.04 (+2.37%)</td><td>0.04 <b>(+36.27%)</b></td><td>0.01 <b>(-22.05%)</b></td><td>229.50 <b>(-26.61%)</b></td><td>197.72 (-7.84%)</td><td>207.60 (-2.31%)</td><td>124.80 (+5.23%)</td><td>41.84 <b>(-39.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>312.70 (n/a)</td><td>214.54 (n/a)</td><td>212.50 (n/a)</td><td>118.60 (n/a)</td><td>68.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.10 <b>(+66.55%)</b></td><td>0.06 <b>(+21.30%)</b></td><td>0.05 (+3.75%)</td><td>0.04 (-0.95%)</td><td>0.03 <b>(+181.91%)</b></td><td>213.30 (+0.95%)</td><td>162.58 (-9.72%)</td><td>181.60 (-3.61%)</td><td>80.10 <b>(-39.91%)</b></td><td>50.81 <b>(+60.30%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>180.08 (n/a)</td><td>188.40 (n/a)</td><td>133.30 (n/a)</td><td>31.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (+12.41%)</td><td>0.04 (+5.55%)</td><td>0.04 (-4.04%)</td><td>0.03 (+9.60%)</td><td>0.01 <b>(+35.08%)</b></td><td>289.70 (-8.76%)</td><td>223.18 (-4.22%)</td><td>231.80 (+4.18%)</td><td>171.70 (-11.04%)</td><td>50.04 (+1.77%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>317.50 (n/a)</td><td>233.02 (n/a)</td><td>222.50 (n/a)</td><td>193.00 (n/a)</td><td>49.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (+6.79%)</td><td>0.05 (-3.70%)</td><td>0.05 (-11.52%)</td><td>0.04 (-9.05%)</td><td>0.01 <b>(+102.90%)</b></td><td>191.50 (+9.93%)</td><td>169.80 (+5.09%)</td><td>178.10 (+13.08%)</td><td>138.70 (-6.35%)</td><td>22.93 <b>(+107.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>174.20 (n/a)</td><td>161.58 (n/a)</td><td>157.50 (n/a)</td><td>148.10 (n/a)</td><td>11.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-12.86%)</td><td>0.04 (+4.01%)</td><td>0.05 <b>(+40.36%)</b></td><td>0.02 <b>(-32.87%)</b></td><td>0.01 (+3.62%)</td><td>366.80 <b>(+48.98%)</b></td><td>206.42 (+1.22%)</td><td>165.30 <b>(-28.78%)</b></td><td>145.70 (+14.72%)</td><td>91.98 <b>(+83.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.20 (n/a)</td><td>203.94 (n/a)</td><td>232.10 (n/a)</td><td>127.00 (n/a)</td><td>50.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (+3.64%)</td><td>0.05 (+4.45%)</td><td>0.05 (+7.25%)</td><td>0.04 (+0.42%)</td><td>0.01 (+3.46%)</td><td>212.60 (-0.42%)</td><td>172.12 (-4.22%)</td><td>172.70 (-6.80%)</td><td>131.40 (-3.52%)</td><td>29.93 (-0.55%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.50 (n/a)</td><td>179.70 (n/a)</td><td>185.30 (n/a)</td><td>136.20 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (+2.33%)</td><td>0.05 (+10.11%)</td><td>0.05 (-5.76%)</td><td>0.05 <b>(+84.13%)</b></td><td>0.00 <b>(-64.22%)</b></td><td>173.70 <b>(-45.70%)</b></td><td>160.58 (-15.93%)</td><td>167.40 (+6.08%)</td><td>144.40 (-2.23%)</td><td>13.30 <b>(-81.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.90 (n/a)</td><td>191.00 (n/a)</td><td>157.80 (n/a)</td><td>147.70 (n/a)</td><td>72.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 <b>(+31.69%)</b></td><td>0.05 <b>(+20.96%)</b></td><td>0.05 (+19.93%)</td><td>0.03 (+0.53%)</td><td>0.01 <b>(+67.86%)</b></td><td>291.90 (-0.51%)</td><td>186.08 (-14.38%)</td><td>160.30 (-16.60%)</td><td>142.00 <b>(-24.06%)</b></td><td>60.58 <b>(+34.03%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.40 (n/a)</td><td>217.34 (n/a)</td><td>192.20 (n/a)</td><td>187.00 (n/a)</td><td>45.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 <b>(+52.65%)</b></td><td>0.05 (+14.06%)</td><td>0.04 (+5.30%)</td><td>0.04 (+5.59%)</td><td>0.01 <b>(+267.68%)</b></td><td>205.00 (-5.31%)</td><td>180.80 (-9.23%)</td><td>193.20 (-5.01%)</td><td>119.50 <b>(-34.52%)</b></td><td>34.67 <b>(+123.32%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.50 (n/a)</td><td>199.18 (n/a)</td><td>203.40 (n/a)</td><td>182.50 (n/a)</td><td>15.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52448.80 (n/a)</td><td>52394.42 (n/a)</td><td>52380.70 (n/a)</td><td>52341.40 (n/a)</td><td>43.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.17 (-3.26%)</td><td>0.16 (-3.85%)</td><td>0.15 (-4.06%)</td><td>0.14 (-5.32%)</td><td>0.02 (+3.57%)</td><td>174.50 (+5.63%)</td><td>159.38 (+4.13%)</td><td>167.40 (+4.23%)</td><td>141.60 (+3.43%)</td><td>15.50 (+12.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>165.20 (n/a)</td><td>153.06 (n/a)</td><td>160.60 (n/a)</td><td>136.90 (n/a)</td><td>13.82 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.31 (-10.66%)</td><td>0.23 <b>(-23.08%)</b></td><td>0.22 <b>(-28.36%)</b></td><td>0.18 <b>(-23.92%)</b></td><td>0.05 <b>(+20.30%)</b></td><td>228.50 <b>(+31.47%)</b></td><td>183.82 <b>(+32.55%)</b></td><td>183.10 <b>(+39.66%)</b></td><td>131.20 (+11.85%)</td><td>38.29 <b>(+74.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>173.80 (n/a)</td><td>138.68 (n/a)</td><td>131.10 (n/a)</td><td>117.30 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.04 (-1.96%)</td><td>0.03 (-2.62%)</td><td>0.03 (-10.61%)</td><td>0.03 (+7.83%)</td><td>0.00 (-15.05%)</td><td>171.50 (-7.30%)</td><td>149.46 (+1.96%)</td><td>159.60 (+11.84%)</td><td>126.70 (+2.01%)</td><td>20.37 (-19.96%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>146.58 (n/a)</td><td>142.70 (n/a)</td><td>124.20 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-11.73%)</td><td>0.05 (-7.77%)</td><td>0.05 (+5.45%)</td><td>0.04 (-1.01%)</td><td>0.01 <b>(-34.63%)</b></td><td>198.40 (+1.02%)</td><td>167.30 (+6.45%)</td><td>158.60 (-5.20%)</td><td>136.40 (+13.29%)</td><td>26.49 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>157.16 (n/a)</td><td>167.30 (n/a)</td><td>120.40 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.13 <b>(+25.50%)</b></td><td>0.09 (+12.64%)</td><td>0.08 (+0.23%)</td><td>0.06 (+19.57%)</td><td>0.03 <b>(+33.77%)</b></td><td>207.70 (-16.38%)</td><td>150.96 (-10.75%)</td><td>152.80 (-0.26%)</td><td>96.10 <b>(-20.32%)</b></td><td>39.80 (-16.91%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.40 (n/a)</td><td>169.14 (n/a)</td><td>153.20 (n/a)</td><td>120.60 (n/a)</td><td>47.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+0.09%)</td><td>0.05 (-9.87%)</td><td>0.05 <b>(-22.95%)</b></td><td>0.04 (+1.23%)</td><td>0.01 (-9.16%)</td><td>182.60 (-1.19%)</td><td>157.46 (+10.19%)</td><td>163.90 <b>(+29.87%)</b></td><td>115.20 (-0.09%)</td><td>25.30 (-14.36%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>142.90 (n/a)</td><td>126.20 (n/a)</td><td>115.30 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.09 <b>(+25.68%)</b></td><td>0.07 (+6.85%)</td><td>0.06 (-0.20%)</td><td>0.05 (+2.32%)</td><td>0.02 <b>(+61.47%)</b></td><td>190.30 (-2.31%)</td><td>158.04 (-4.83%)</td><td>157.60 (+0.19%)</td><td>108.90 <b>(-20.45%)</b></td><td>30.72 (+17.72%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>166.06 (n/a)</td><td>157.30 (n/a)</td><td>136.90 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+2.66%)</td><td>0.06 (-0.76%)</td><td>0.05 (+1.05%)</td><td>0.05 (-2.23%)</td><td>0.01 (+12.44%)</td><td>177.80 (+2.30%)</td><td>151.28 (+1.33%)</td><td>152.50 (-1.04%)</td><td>121.80 (-2.64%)</td><td>25.91 (+15.34%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>149.30 (n/a)</td><td>154.10 (n/a)</td><td>125.10 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.08 (+18.44%)</td><td>0.07 (+2.42%)</td><td>0.06 (-5.95%)</td><td>0.04 <b>(-27.04%)</b></td><td>0.02 <b>(+268.89%)</b></td><td>238.30 <b>(+37.03%)</b></td><td>163.60 (+2.98%)</td><td>165.00 (+6.31%)</td><td>122.20 (-15.61%)</td><td>46.58 <b>(+319.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>158.86 (n/a)</td><td>155.20 (n/a)</td><td>144.80 (n/a)</td><td>11.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-7.73%)</td><td>0.05 (-9.89%)</td><td>0.05 (-0.85%)</td><td>0.04 (-11.19%)</td><td>0.01 (-13.41%)</td><td>200.60 (+12.63%)</td><td>170.12 (+10.74%)</td><td>168.70 (+0.84%)</td><td>131.70 (+8.40%)</td><td>26.48 (+5.17%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.10 (n/a)</td><td>153.62 (n/a)</td><td>167.30 (n/a)</td><td>121.50 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (-3.84%)</td><td>0.06 (-0.23%)</td><td>0.06 (+10.98%)</td><td>0.05 (+10.03%)</td><td>0.01 <b>(-36.23%)</b></td><td>183.90 (-9.14%)</td><td>163.98 (-2.10%)</td><td>165.30 (-9.92%)</td><td>129.80 (+4.01%)</td><td>20.70 <b>(-40.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.40 (n/a)</td><td>167.50 (n/a)</td><td>183.50 (n/a)</td><td>124.80 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-3.84%)</td><td>0.05 (+3.14%)</td><td>0.05 (+2.46%)</td><td>0.04 <b>(+24.51%)</b></td><td>0.01 <b>(-39.06%)</b></td><td>185.50 (-19.70%)</td><td>158.16 (-5.23%)</td><td>150.50 (-2.40%)</td><td>141.00 (+3.98%)</td><td>18.00 <b>(-51.33%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>166.88 (n/a)</td><td>154.20 (n/a)</td><td>135.60 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+16.09%)</td><td>0.06 (+13.12%)</td><td>0.06 <b>(+22.73%)</b></td><td>0.04 (+8.19%)</td><td>0.01 (+14.87%)</td><td>207.80 (-7.60%)</td><td>166.70 (-11.48%)</td><td>161.40 (-18.53%)</td><td>132.40 (-13.86%)</td><td>27.99 (-6.30%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.90 (n/a)</td><td>188.32 (n/a)</td><td>198.10 (n/a)</td><td>153.70 (n/a)</td><td>29.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 (-18.94%)</td><td>0.04 (-15.49%)</td><td>0.04 (-16.86%)</td><td>0.03 (-0.66%)</td><td>0.01 <b>(-33.31%)</b></td><td>236.20 (+0.68%)</td><td>193.94 (+15.81%)</td><td>193.70 <b>(+20.24%)</b></td><td>145.90 <b>(+23.33%)</b></td><td>34.28 (-19.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>167.46 (n/a)</td><td>161.10 (n/a)</td><td>118.30 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.06 <b>(+35.47%)</b></td><td>0.05 <b>(+28.20%)</b></td><td>0.05 <b>(+20.08%)</b></td><td>0.04 <b>(+21.02%)</b></td><td>0.01 <b>(+87.16%)</b></td><td>234.40 (-17.38%)</td><td>177.90 <b>(-20.64%)</b></td><td>177.10 (-16.74%)</td><td>141.20 <b>(-26.15%)</b></td><td>37.95 (+8.08%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.70 (n/a)</td><td>224.16 (n/a)</td><td>212.70 (n/a)</td><td>191.20 (n/a)</td><td>35.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.07 (+6.08%)</td><td>0.05 (+5.62%)</td><td>0.05 (-0.88%)</td><td>0.04 (+19.05%)</td><td>0.01 (-2.65%)</td><td>186.50 (-15.99%)</td><td>160.70 (-6.36%)</td><td>167.80 (+0.84%)</td><td>111.60 (-5.74%)</td><td>29.23 <b>(-24.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>171.62 (n/a)</td><td>166.40 (n/a)</td><td>118.40 (n/a)</td><td>38.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (+1.29%)</td><td>0.05 (+15.38%)</td><td>0.05 <b>(+25.34%)</b></td><td>0.04 (+3.11%)</td><td>0.01 (+1.34%)</td><td>233.50 (-3.03%)</td><td>184.78 (-13.33%)</td><td>172.00 <b>(-20.22%)</b></td><td>162.40 (-1.28%)</td><td>29.58 (-1.46%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>213.20 (n/a)</td><td>215.60 (n/a)</td><td>164.50 (n/a)</td><td>30.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.05 (+4.78%)</td><td>0.04 (+14.25%)</td><td>0.04 (+15.23%)</td><td>0.04 <b>(+22.92%)</b></td><td>0.00 <b>(-32.47%)</b></td><td>211.60 (-18.65%)</td><td>190.42 (-13.26%)</td><td>191.60 (-13.22%)</td><td>171.10 (-4.57%)</td><td>15.19 <b>(-47.12%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.10 (n/a)</td><td>219.54 (n/a)</td><td>220.80 (n/a)</td><td>179.30 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.76 (+9.64%)</td><td>0.65 (+19.63%)</td><td>0.65 <b>(+24.23%)</b></td><td>0.54 <b>(+35.94%)</b></td><td>0.09 <b>(-25.73%)</b></td><td>183.40 <b>(-26.43%)</b></td><td>154.44 (-18.46%)</td><td>151.90 (-19.50%)</td><td>128.70 (-8.85%)</td><td>21.42 <b>(-49.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.39 (n/a)</td><td>0.12 (n/a)</td><td>249.30 (n/a)</td><td>189.40 (n/a)</td><td>188.70 (n/a)</td><td>141.20 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.82 (+15.58%)</td><td>0.68 (+18.73%)</td><td>0.69 (+15.71%)</td><td>0.49 <b>(+22.42%)</b></td><td>0.12 (+1.09%)</td><td>202.30 (-18.33%)</td><td>149.22 (-16.63%)</td><td>143.50 (-13.55%)</td><td>120.50 (-13.50%)</td><td>31.21 <b>(-26.89%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.71 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.40 (n/a)</td><td>0.12 (n/a)</td><td>247.70 (n/a)</td><td>178.98 (n/a)</td><td>166.00 (n/a)</td><td>139.30 (n/a)</td><td>42.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.64 (+9.99%)</td><td>0.55 (+2.44%)</td><td>0.59 (+7.92%)</td><td>0.39 (-16.83%)</td><td>0.10 <b>(+135.91%)</b></td><td>251.50 <b>(+20.22%)</b></td><td>183.78 (+0.14%)</td><td>165.30 (-7.34%)</td><td>154.80 (-9.10%)</td><td>39.45 <b>(+160.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.04 (n/a)</td><td>209.20 (n/a)</td><td>183.52 (n/a)</td><td>178.40 (n/a)</td><td>170.30 (n/a)</td><td>15.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.61 (+10.45%)</td><td>0.49 (-3.52%)</td><td>0.49 (-6.08%)</td><td>0.36 (-17.47%)</td><td>0.10 <b>(+110.64%)</b></td><td>273.00 <b>(+21.17%)</b></td><td>208.32 (+6.59%)</td><td>201.10 (+6.46%)</td><td>160.40 (-9.48%)</td><td>44.78 <b>(+130.53%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.55 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.05 (n/a)</td><td>225.30 (n/a)</td><td>195.44 (n/a)</td><td>188.90 (n/a)</td><td>177.20 (n/a)</td><td>19.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.57 (+5.60%)</td><td>0.51 (+9.90%)</td><td>0.55 (+13.59%)</td><td>0.44 (+14.71%)</td><td>0.06 (-11.80%)</td><td>167.90 (-12.82%)</td><td>144.96 (-9.55%)</td><td>135.20 (-11.98%)</td><td>130.30 (-5.31%)</td><td>17.30 <b>(-27.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>192.60 (n/a)</td><td>160.26 (n/a)</td><td>153.60 (n/a)</td><td>137.60 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.78 <b>(+31.40%)</b></td><td>0.58 <b>(+20.97%)</b></td><td>0.50 (-5.34%)</td><td>0.42 <b>(+27.42%)</b></td><td>0.16 <b>(+44.01%)</b></td><td>175.80 <b>(-21.52%)</b></td><td>134.86 (-16.57%)</td><td>147.70 (+5.65%)</td><td>94.80 <b>(-23.92%)</b></td><td>34.50 (-16.86%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.11 (n/a)</td><td>224.00 (n/a)</td><td>161.64 (n/a)</td><td>139.80 (n/a)</td><td>124.60 (n/a)</td><td>41.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.50 (-13.19%)</td><td>0.43 (-11.38%)</td><td>0.44 (-10.16%)</td><td>0.35 (-14.10%)</td><td>0.06 (-6.24%)</td><td>207.70 (+16.42%)</td><td>173.04 (+13.10%)</td><td>167.60 (+11.29%)</td><td>147.80 (+15.20%)</td><td>24.42 <b>(+25.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>178.40 (n/a)</td><td>153.00 (n/a)</td><td>150.60 (n/a)</td><td>128.30 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.50 (-5.70%)</td><td>0.40 (-5.53%)</td><td>0.42 (+3.59%)</td><td>0.32 (-2.91%)</td><td>0.07 <b>(-21.15%)</b></td><td>227.60 (+2.99%)</td><td>186.26 (+4.88%)</td><td>177.40 (-3.48%)</td><td>148.00 (+6.02%)</td><td>30.35 (-11.38%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>221.00 (n/a)</td><td>177.60 (n/a)</td><td>183.80 (n/a)</td><td>139.60 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.11 (+4.38%)</td><td>0.84 (-10.27%)</td><td>0.84 (-16.16%)</td><td>0.63 (-6.12%)</td><td>0.18 (+12.49%)</td><td>209.50 (+6.51%)</td><td>162.08 (+12.17%)</td><td>155.60 (+19.33%)</td><td>118.30 (-4.21%)</td><td>33.45 (+11.34%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.06 (n/a)</td><td>0.93 (n/a)</td><td>1.00 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>196.70 (n/a)</td><td>144.50 (n/a)</td><td>130.40 (n/a)</td><td>123.50 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.21 (+18.79%)</td><td>0.90 (-0.69%)</td><td>0.85 (-12.36%)</td><td>0.73 (-4.54%)</td><td>0.19 <b>(+57.29%)</b></td><td>179.30 (+4.73%)</td><td>149.80 (+2.24%)</td><td>154.90 (+14.06%)</td><td>107.90 (-15.83%)</td><td>26.80 <b>(+33.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.02 (n/a)</td><td>0.91 (n/a)</td><td>0.97 (n/a)</td><td>0.77 (n/a)</td><td>0.12 (n/a)</td><td>171.20 (n/a)</td><td>146.52 (n/a)</td><td>135.80 (n/a)</td><td>128.20 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.17 <b>(+22.65%)</b></td><td>0.88 (+4.26%)</td><td>0.87 (-4.12%)</td><td>0.62 (-2.89%)</td><td>0.20 <b>(+50.33%)</b></td><td>211.00 (+2.98%)</td><td>154.78 (-2.22%)</td><td>150.60 (+4.29%)</td><td>112.20 (-18.46%)</td><td>36.05 <b>(+27.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.95 (n/a)</td><td>0.85 (n/a)</td><td>0.91 (n/a)</td><td>0.64 (n/a)</td><td>0.13 (n/a)</td><td>204.90 (n/a)</td><td>158.30 (n/a)</td><td>144.40 (n/a)</td><td>137.60 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (-1.88%)</td><td>0.02 (+2.33%)</td><td>0.02 (-2.18%)</td><td>0.02 <b>(+21.19%)</b></td><td>0.01 <b>(-24.27%)</b></td><td>212.50 (-17.48%)</td><td>172.38 (-6.02%)</td><td>164.70 (+2.17%)</td><td>123.00 (+1.91%)</td><td>34.96 <b>(-38.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.50 (n/a)</td><td>183.42 (n/a)</td><td>161.20 (n/a)</td><td>120.70 (n/a)</td><td>56.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (+10.89%)</td><td>0.03 (+4.64%)</td><td>0.03 (-7.53%)</td><td>0.02 (+6.39%)</td><td>0.00 <b>(+26.25%)</b></td><td>178.10 (-6.02%)</td><td>153.06 (-4.06%)</td><td>161.00 (+8.13%)</td><td>126.90 (-9.87%)</td><td>21.34 (+5.43%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.50 (n/a)</td><td>159.54 (n/a)</td><td>148.90 (n/a)</td><td>140.80 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (-7.46%)</td><td>0.02 (-0.81%)</td><td>0.02 (-2.39%)</td><td>0.02 (+17.03%)</td><td>0.00 <b>(-65.44%)</b></td><td>183.20 (-14.55%)</td><td>171.26 (-0.59%)</td><td>169.10 (+2.48%)</td><td>162.10 (+8.07%)</td><td>8.05 <b>(-68.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.40 (n/a)</td><td>172.28 (n/a)</td><td>165.00 (n/a)</td><td>150.00 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.88 (-8.36%)</td><td>0.77 (-8.45%)</td><td>0.79 (-8.24%)</td><td>0.55 <b>(-26.14%)</b></td><td>0.13 <b>(+56.61%)</b></td><td>238.70 <b>(+35.39%)</b></td><td>176.32 (+11.47%)</td><td>167.90 (+9.03%)</td><td>150.60 (+9.13%)</td><td>36.16 <b>(+132.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.96 (n/a)</td><td>0.84 (n/a)</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.08 (n/a)</td><td>176.30 (n/a)</td><td>158.18 (n/a)</td><td>154.00 (n/a)</td><td>138.00 (n/a)</td><td>15.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.93 (-7.58%)</td><td>0.80 (-11.47%)</td><td>0.78 (-10.72%)</td><td>0.74 (-11.59%)</td><td>0.07 (-5.24%)</td><td>178.40 (+13.13%)</td><td>165.16 (+13.01%)</td><td>169.20 (+12.05%)</td><td>142.40 (+8.21%)</td><td>14.05 (+15.19%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td><td>0.87 (n/a)</td><td>0.84 (n/a)</td><td>0.08 (n/a)</td><td>157.70 (n/a)</td><td>146.14 (n/a)</td><td>151.00 (n/a)</td><td>131.60 (n/a)</td><td>12.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.06 (+5.48%)</td><td>0.83 (-0.04%)</td><td>0.78 (-10.66%)</td><td>0.74 (+12.24%)</td><td>0.13 (-12.61%)</td><td>178.30 (-10.94%)</td><td>161.04 (-0.94%)</td><td>168.70 (+11.94%)</td><td>125.00 (-5.23%)</td><td>20.79 <b>(-29.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.00 (n/a)</td><td>0.83 (n/a)</td><td>0.88 (n/a)</td><td>0.66 (n/a)</td><td>0.15 (n/a)</td><td>200.20 (n/a)</td><td>162.56 (n/a)</td><td>150.70 (n/a)</td><td>131.90 (n/a)</td><td>29.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.01 (-8.85%)</td><td>0.75 (-13.08%)</td><td>0.70 (-13.39%)</td><td>0.56 <b>(-28.53%)</b></td><td>0.17 <b>(+25.52%)</b></td><td>236.70 <b>(+39.89%)</b></td><td>184.20 (+17.77%)</td><td>189.00 (+15.46%)</td><td>131.00 (+9.72%)</td><td>40.25 <b>(+93.43%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.11 (n/a)</td><td>0.86 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.14 (n/a)</td><td>169.20 (n/a)</td><td>156.40 (n/a)</td><td>163.70 (n/a)</td><td>119.40 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.04 (-1.90%)</td><td>0.90 (-4.80%)</td><td>0.86 (-13.10%)</td><td>0.82 (-1.76%)</td><td>0.10 (-5.35%)</td><td>161.90 (+1.76%)</td><td>147.42 (+4.97%)</td><td>153.30 (+15.09%)</td><td>127.00 (+1.93%)</td><td>15.01 (-2.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>1.06 (n/a)</td><td>0.95 (n/a)</td><td>0.99 (n/a)</td><td>0.83 (n/a)</td><td>0.10 (n/a)</td><td>159.10 (n/a)</td><td>140.44 (n/a)</td><td>133.20 (n/a)</td><td>124.60 (n/a)</td><td>15.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (+15.93%)</td><td>0.02 (-7.80%)</td><td>0.03 (-7.52%)</td><td>0.01 <b>(-31.11%)</b></td><td>0.01 <b>(+63.83%)</b></td><td>340.80 <b>(+45.14%)</b></td><td>194.78 (+18.32%)</td><td>161.10 (+8.12%)</td><td>118.30 (-13.71%)</td><td>86.87 <b>(+113.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>164.62 (n/a)</td><td>149.00 (n/a)</td><td>137.10 (n/a)</td><td>40.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.03 (+5.37%)</td><td>0.03 (+0.91%)</td><td>0.03 (+2.01%)</td><td>0.02 (-10.54%)</td><td>0.01 <b>(+32.05%)</b></td><td>214.40 (+11.78%)</td><td>157.36 (+0.73%)</td><td>149.00 (-1.97%)</td><td>120.60 (-5.11%)</td><td>34.88 <b>(+43.52%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.80 (n/a)</td><td>156.22 (n/a)</td><td>152.00 (n/a)</td><td>127.10 (n/a)</td><td>24.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.00 (-2.17%)</td><td>0.00 (-1.83%)</td><td>0.00 (-2.27%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-26.48%)</b></td><td>1008.33 (+0.39%)</td><td>957.48 (+2.07%)</td><td>957.85 (+3.78%)</td><td>904.17 (+1.14%)</td><td>36.87 (-13.39%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1004.42 (n/a)</td><td>938.05 (n/a)</td><td>922.96 (n/a)</td><td>893.99 (n/a)</td><td>42.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.01 (+3.75%)</td><td>0.01 (+0.25%)</td><td>0.01 (+0.00%)</td><td>0.01 (-3.85%)</td><td>0.00 <b>(+163.00%)</b></td><td>1086.60 (+2.87%)</td><td>1029.55 (-0.94%)</td><td>1020.13 (-0.95%)</td><td>984.36 (-4.12%)</td><td>37.23 <b>(+144.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1056.25 (n/a)</td><td>1039.29 (n/a)</td><td>1029.93 (n/a)</td><td>1026.67 (n/a)</td><td>15.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>1.00 (+3.42%)</td><td>0.96 (+0.04%)</td><td>0.96 (-0.37%)</td><td>0.95 (-1.13%)</td><td>0.02 <b>(+481.64%)</b></td><td>2217.37 (+1.14%)</td><td>2181.98 (-0.00%)</td><td>2191.35 (+0.37%)</td><td>2101.56 (-3.31%)</td><td>46.80 <b>(+468.86%)</b></td>
</tr>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>0.91 (+0.96%)</td><td>0.88 (-0.21%)</td><td>0.88 (-0.69%)</td><td>0.86 (+0.84%)</td><td>0.02 (+5.17%)</td><td>2427.32 (-0.83%)</td><td>2374.80 (+0.22%)</td><td>2379.12 (+0.70%)</td><td>2298.17 (-0.95%)</td><td>49.16 (+2.75%)</td>
</tr>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>4.19 (+18.79%)</td><td>3.43 (+16.02%)</td><td>3.41 <b>(+20.28%)</b></td><td>2.84 (+15.13%)</td><td>0.50 (+5.46%)</td><td>184.30 (-13.15%)</td><td>155.32 (-14.14%)</td><td>153.80 (-16.86%)</td><td>125.00 (-15.82%)</td><td>22.05 <b>(-22.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.53 (n/a)</td><td>2.96 (n/a)</td><td>2.83 (n/a)</td><td>2.47 (n/a)</td><td>0.48 (n/a)</td><td>212.20 (n/a)</td><td>180.90 (n/a)</td><td>185.00 (n/a)</td><td>148.50 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>6.13 (+18.50%)</td><td>5.42 <b>(+22.26%)</b></td><td>5.83 <b>(+30.05%)</b></td><td>3.82 (+10.62%)</td><td>0.93 <b>(+50.14%)</b></td><td>274.30 (-9.59%)</td><td>199.38 (-17.19%)</td><td>179.70 <b>(-23.14%)</b></td><td>171.10 (-15.59%)</td><td>42.70 (+14.11%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>5.17 (n/a)</td><td>4.43 (n/a)</td><td>4.49 (n/a)</td><td>3.46 (n/a)</td><td>0.62 (n/a)</td><td>303.40 (n/a)</td><td>240.78 (n/a)</td><td>233.80 (n/a)</td><td>202.70 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:06:49</td><td>3.89 (+5.18%)</td><td>3.33 (+2.57%)</td><td>3.45 (+4.96%)</td><td>2.60 (-2.37%)</td><td>0.48 <b>(+26.41%)</b></td><td>202.00 (+2.43%)</td><td>160.24 (-1.87%)</td><td>151.80 (-4.71%)</td><td>134.70 (-4.94%)</td><td>25.45 <b>(+23.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:36:58</td><td>3.70 (n/a)</td><td>3.25 (n/a)</td><td>3.29 (n/a)</td><td>2.66 (n/a)</td><td>0.38 (n/a)</td><td>197.20 (n/a)</td><td>163.30 (n/a)</td><td>159.30 (n/a)</td><td>141.70 (n/a)</td><td>20.62 (n/a)</td>
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
