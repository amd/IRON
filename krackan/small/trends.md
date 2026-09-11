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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (-19.15%)</td><td>0.06 <b>(-23.93%)</b></td><td>0.06 <b>(-20.05%)</b></td><td>0.05 <b>(-27.57%)</b></td><td>0.01 <b>(+31.24%)</b></td><td>232.30 <b>(+38.11%)</b></td><td>202.46 <b>(+32.36%)</b></td><td>193.10 <b>(+25.06%)</b></td><td>175.40 <b>(+23.70%)</b></td><td>23.15 <b>(+126.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>168.20 (n/a)</td><td>152.96 (n/a)</td><td>154.40 (n/a)</td><td>141.80 (n/a)</td><td>10.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (-7.67%)</td><td>0.07 (-3.99%)</td><td>0.07 (+1.07%)</td><td>0.06 (-11.54%)</td><td>0.01 (+2.84%)</td><td>216.10 (+13.02%)</td><td>171.06 (+4.61%)</td><td>167.80 (-1.06%)</td><td>147.20 (+8.31%)</td><td>27.10 <b>(+28.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>163.52 (n/a)</td><td>169.60 (n/a)</td><td>135.90 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (-5.01%)</td><td>0.07 (+4.99%)</td><td>0.07 (+6.19%)</td><td>0.06 (+16.83%)</td><td>0.01 <b>(-35.24%)</b></td><td>203.50 (-14.42%)</td><td>181.96 (-5.89%)</td><td>178.10 (-5.82%)</td><td>164.80 (+5.30%)</td><td>17.49 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>193.34 (n/a)</td><td>189.10 (n/a)</td><td>156.50 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 <b>(-28.30%)</b></td><td>0.06 (-16.58%)</td><td>0.06 (-13.26%)</td><td>0.06 (-12.04%)</td><td>0.01 <b>(-59.74%)</b></td><td>217.90 (+13.67%)</td><td>202.28 (+17.77%)</td><td>208.50 (+15.32%)</td><td>174.10 <b>(+39.50%)</b></td><td>17.44 <b>(-34.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>171.76 (n/a)</td><td>180.80 (n/a)</td><td>124.80 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (+5.04%)</td><td>0.03 (+0.71%)</td><td>0.03 (-9.32%)</td><td>0.02 (-13.20%)</td><td>0.01 <b>(+50.02%)</b></td><td>224.20 (+15.21%)</td><td>169.64 (+3.44%)</td><td>188.20 (+10.25%)</td><td>115.70 (-4.77%)</td><td>48.48 <b>(+56.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>164.00 (n/a)</td><td>170.70 (n/a)</td><td>121.50 (n/a)</td><td>31.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (+15.03%)</td><td>0.03 (+9.43%)</td><td>0.03 (+4.83%)</td><td>0.03 (+11.50%)</td><td>0.00 <b>(+27.96%)</b></td><td>178.60 (-10.34%)</td><td>159.98 (-8.34%)</td><td>163.40 (-4.61%)</td><td>129.50 (-13.09%)</td><td>20.57 (-0.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>199.20 (n/a)</td><td>174.54 (n/a)</td><td>171.30 (n/a)</td><td>149.00 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (-9.87%)</td><td>0.03 (-4.35%)</td><td>0.03 (-11.81%)</td><td>0.03 (+5.88%)</td><td>0.00 <b>(-29.84%)</b></td><td>180.80 (-5.54%)</td><td>156.14 (+3.28%)</td><td>162.90 (+13.36%)</td><td>132.10 (+11.01%)</td><td>19.68 <b>(-27.99%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>151.18 (n/a)</td><td>143.70 (n/a)</td><td>119.00 (n/a)</td><td>27.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (-0.05%)</td><td>0.03 (-0.17%)</td><td>0.03 (+3.56%)</td><td>0.02 <b>(-20.03%)</b></td><td>0.01 <b>(+38.30%)</b></td><td>259.40 <b>(+25.07%)</b></td><td>177.04 (+3.16%)</td><td>166.70 (-3.42%)</td><td>135.80 (+0.07%)</td><td>48.56 <b>(+80.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>207.40 (n/a)</td><td>171.62 (n/a)</td><td>172.60 (n/a)</td><td>135.70 (n/a)</td><td>26.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (-15.58%)</td><td>0.03 (+5.79%)</td><td>0.03 (+11.55%)</td><td>0.03 (+16.17%)</td><td>0.00 <b>(-46.54%)</b></td><td>193.40 (-13.93%)</td><td>163.16 (-8.94%)</td><td>162.20 (-10.39%)</td><td>133.70 (+18.42%)</td><td>23.81 <b>(-42.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>179.18 (n/a)</td><td>181.00 (n/a)</td><td>112.90 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (+1.17%)</td><td>0.03 (+2.21%)</td><td>0.03 (+2.48%)</td><td>0.02 (+5.06%)</td><td>0.01 (+4.60%)</td><td>237.80 (-4.84%)</td><td>195.06 (-1.87%)</td><td>189.80 (-2.42%)</td><td>138.80 (-1.21%)</td><td>41.52 (+3.29%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>249.90 (n/a)</td><td>198.78 (n/a)</td><td>194.50 (n/a)</td><td>140.50 (n/a)</td><td>40.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 <b>(+49.62%)</b></td><td>0.04 <b>(+29.52%)</b></td><td>0.04 (+18.13%)</td><td>0.03 <b>(+62.67%)</b></td><td>0.01 <b>(+28.26%)</b></td><td>166.30 <b>(-38.52%)</b></td><td>143.00 <b>(-23.81%)</b></td><td>140.20 (-15.39%)</td><td>106.50 <b>(-33.19%)</b></td><td>24.23 <b>(-48.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.50 (n/a)</td><td>187.68 (n/a)</td><td>165.70 (n/a)</td><td>159.40 (n/a)</td><td>46.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (+12.90%)</td><td>0.03 (+8.10%)</td><td>0.03 (-2.20%)</td><td>0.02 <b>(+41.29%)</b></td><td>0.00 <b>(-26.19%)</b></td><td>216.40 <b>(-29.23%)</b></td><td>188.52 (-10.31%)</td><td>196.00 (+2.30%)</td><td>149.20 (-11.45%)</td><td>25.04 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>305.80 (n/a)</td><td>210.18 (n/a)</td><td>191.60 (n/a)</td><td>168.50 (n/a)</td><td>56.22 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.10 (n/a)</td><td>204.34 (n/a)</td><td>206.40 (n/a)</td><td>143.00 (n/a)</td><td>53.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>179.62 (n/a)</td><td>184.40 (n/a)</td><td>156.50 (n/a)</td><td>13.56 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>323.50 (n/a)</td><td>208.26 (n/a)</td><td>181.50 (n/a)</td><td>166.30 (n/a)</td><td>65.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>214.62 (n/a)</td><td>202.80 (n/a)</td><td>199.40 (n/a)</td><td>19.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>245.70 (n/a)</td><td>179.18 (n/a)</td><td>148.20 (n/a)</td><td>127.70 (n/a)</td><td>53.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.40 (n/a)</td><td>151.52 (n/a)</td><td>135.00 (n/a)</td><td>128.90 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.50 (n/a)</td><td>182.72 (n/a)</td><td>185.60 (n/a)</td><td>153.70 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>288.10 (n/a)</td><td>207.42 (n/a)</td><td>193.80 (n/a)</td><td>161.40 (n/a)</td><td>48.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.40 (+0.10%)</td><td>3.30 (-2.45%)</td><td>3.17 (+0.28%)</td><td>2.83 (-7.63%)</td><td>0.63 (+12.10%)</td><td>486.60 (+8.25%)</td><td>427.24 (+3.16%)</td><td>433.60 (-0.28%)</td><td>312.90 (-0.10%)</td><td>68.51 <b>(+20.65%)</b></td><td>857.85 (+0.10%)</td><td>644.07 (-2.45%)</td><td>619.09 (+0.28%)</td><td>551.60 (-7.63%)</td><td>123.68 (+12.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.39 (n/a)</td><td>3.38 (n/a)</td><td>3.17 (n/a)</td><td>3.06 (n/a)</td><td>0.57 (n/a)</td><td>449.50 (n/a)</td><td>414.16 (n/a)</td><td>434.80 (n/a)</td><td>313.20 (n/a)</td><td>56.78 (n/a)</td><td>856.99 (n/a)</td><td>660.23 (n/a)</td><td>617.39 (n/a)</td><td>597.17 (n/a)</td><td>110.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.33 (-1.42%)</td><td>4.48 (+1.56%)</td><td>3.90 (+6.90%)</td><td>3.39 (-3.35%)</td><td>1.63 (-3.98%)</td><td>405.90 (+3.47%)</td><td>331.96 (-1.94%)</td><td>353.10 (-6.46%)</td><td>187.70 (+1.40%)</td><td>87.03 (-0.13%)</td><td>1429.77 (-1.42%)</td><td>874.26 (+1.56%)</td><td>760.22 (+6.90%)</td><td>661.35 (-3.35%)</td><td>317.72 (-3.98%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>7.44 (n/a)</td><td>4.41 (n/a)</td><td>3.65 (n/a)</td><td>3.51 (n/a)</td><td>1.70 (n/a)</td><td>392.30 (n/a)</td><td>338.54 (n/a)</td><td>377.50 (n/a)</td><td>185.10 (n/a)</td><td>87.14 (n/a)</td><td>1450.30 (n/a)</td><td>860.82 (n/a)</td><td>711.14 (n/a)</td><td>684.29 (n/a)</td><td>330.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.08 <b>(+31.64%)</b></td><td>4.69 (+11.27%)</td><td>3.91 (-0.68%)</td><td>3.42 (-9.44%)</td><td>1.51 <b>(+128.63%)</b></td><td>401.90 (+10.41%)</td><td>315.00 (-5.13%)</td><td>352.30 (+0.69%)</td><td>194.40 <b>(-24.06%)</b></td><td>85.03 <b>(+94.51%)</b></td><td>1380.49 <b>(+31.64%)</b></td><td>914.66 (+11.27%)</td><td>761.95 (-0.68%)</td><td>667.93 (-9.44%)</td><td>294.27 <b>(+128.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>5.38 (n/a)</td><td>4.21 (n/a)</td><td>3.93 (n/a)</td><td>3.78 (n/a)</td><td>0.66 (n/a)</td><td>364.00 (n/a)</td><td>332.04 (n/a)</td><td>349.90 (n/a)</td><td>256.00 (n/a)</td><td>43.72 (n/a)</td><td>1048.68 (n/a)</td><td>821.99 (n/a)</td><td>767.13 (n/a)</td><td>737.52 (n/a)</td><td>128.71 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.45 (-4.49%)</td><td>4.06 (-12.66%)</td><td>3.77 (-8.39%)</td><td>3.53 (-7.76%)</td><td>0.79 (-17.19%)</td><td>390.10 (+8.42%)</td><td>347.54 (+13.66%)</td><td>365.50 (+9.17%)</td><td>252.40 (+4.73%)</td><td>54.38 (-7.39%)</td><td>1063.70 (-4.49%)</td><td>791.63 (-12.66%)</td><td>734.52 (-8.39%)</td><td>688.19 (-7.76%)</td><td>153.61 (-17.19%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>5.71 (n/a)</td><td>4.65 (n/a)</td><td>4.11 (n/a)</td><td>3.83 (n/a)</td><td>0.95 (n/a)</td><td>359.80 (n/a)</td><td>305.78 (n/a)</td><td>334.80 (n/a)</td><td>241.00 (n/a)</td><td>58.73 (n/a)</td><td>1113.72 (n/a)</td><td>906.36 (n/a)</td><td>801.80 (n/a)</td><td>746.09 (n/a)</td><td>185.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.45 (+19.65%)</td><td>4.17 (+18.50%)</td><td>3.65 (+11.61%)</td><td>3.37 (+5.74%)</td><td>0.96 <b>(+65.09%)</b></td><td>408.40 (-5.44%)</td><td>343.04 (-13.79%)</td><td>376.80 (-10.39%)</td><td>252.50 (-16.42%)</td><td>72.34 <b>(+34.06%)</b></td><td>1063.03 (+19.65%)</td><td>813.90 (+18.50%)</td><td>712.43 (+11.61%)</td><td>657.24 (+5.74%)</td><td>186.75 <b>(+65.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.56 (n/a)</td><td>3.52 (n/a)</td><td>3.27 (n/a)</td><td>3.19 (n/a)</td><td>0.58 (n/a)</td><td>431.90 (n/a)</td><td>397.90 (n/a)</td><td>420.50 (n/a)</td><td>302.10 (n/a)</td><td>53.96 (n/a)</td><td>888.44 (n/a)</td><td>686.86 (n/a)</td><td>638.30 (n/a)</td><td>621.56 (n/a)</td><td>113.12 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.97 (-10.82%)</td><td>1.76 (-5.20%)</td><td>1.83 (-0.93%)</td><td>1.49 (-5.16%)</td><td>0.19 <b>(-22.78%)</b></td><td>268.60 (+5.46%)</td><td>230.50 (+5.06%)</td><td>219.00 (+0.92%)</td><td>203.60 (+12.11%)</td><td>26.13 (-8.11%)</td><td>164.81 (-10.82%)</td><td>147.01 (-5.20%)</td><td>153.19 (-0.93%)</td><td>124.95 (-5.16%)</td><td>15.92 <b>(-22.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>2.21 (n/a)</td><td>1.86 (n/a)</td><td>1.85 (n/a)</td><td>1.58 (n/a)</td><td>0.25 (n/a)</td><td>254.70 (n/a)</td><td>219.40 (n/a)</td><td>217.00 (n/a)</td><td>181.60 (n/a)</td><td>28.43 (n/a)</td><td>184.80 (n/a)</td><td>155.07 (n/a)</td><td>154.63 (n/a)</td><td>131.75 (n/a)</td><td>20.62 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.07 <b>(+34.95%)</b></td><td>5.50 (+7.10%)</td><td>5.19 (+0.92%)</td><td>4.70 (-6.10%)</td><td>0.91 <b>(+815.67%)</b></td><td>411.60 (+6.49%)</td><td>358.10 (-4.87%)</td><td>372.70 (-0.93%)</td><td>273.30 <b>(-25.91%)</b></td><td>51.30 <b>(+597.97%)</b></td><td>1473.09 <b>(+34.95%)</b></td><td>1146.08 (+7.10%)</td><td>1080.23 (+0.92%)</td><td>978.35 (-6.10%)</td><td>190.30 <b>(+815.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>5.24 (n/a)</td><td>5.14 (n/a)</td><td>5.14 (n/a)</td><td>5.00 (n/a)</td><td>0.10 (n/a)</td><td>386.50 (n/a)</td><td>376.42 (n/a)</td><td>376.20 (n/a)</td><td>368.90 (n/a)</td><td>7.35 (n/a)</td><td>1091.57 (n/a)</td><td>1070.09 (n/a)</td><td>1070.40 (n/a)</td><td>1041.90 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>16.49 (+5.90%)</td><td>13.38 (+1.49%)</td><td>12.72 (+1.74%)</td><td>11.91 (-4.21%)</td><td>1.85 <b>(+36.82%)</b></td><td>462.30 (+4.40%)</td><td>417.22 (-0.85%)</td><td>432.90 (-1.70%)</td><td>333.90 (-5.54%)</td><td>51.23 <b>(+33.87%)</b></td><td>6432.38 (+5.90%)</td><td>5217.96 (+1.49%)</td><td>4960.76 (+1.74%)</td><td>4645.13 (-4.21%)</td><td>721.66 <b>(+36.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>15.57 (n/a)</td><td>13.18 (n/a)</td><td>12.50 (n/a)</td><td>12.43 (n/a)</td><td>1.35 (n/a)</td><td>442.80 (n/a)</td><td>420.80 (n/a)</td><td>440.40 (n/a)</td><td>353.50 (n/a)</td><td>38.27 (n/a)</td><td>6074.09 (n/a)</td><td>5141.42 (n/a)</td><td>4875.86 (n/a)</td><td>4849.27 (n/a)</td><td>527.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_windowing[iter0]

_No metrics available._


### test_gemm_split_leg_windowing[iter1]

_No metrics available._


### test_gemm_split_leg_windowing[iter2]

_No metrics available._


### test_gemm_split_leg_windowing[iter3]

_No metrics available._


### test_gemm_split_leg_windowing[iter4]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter0]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter1]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter2]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter3]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter4]

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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>164.24 (n/a)</td><td>161.80 (n/a)</td><td>147.70 (n/a)</td><td>16.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>184.60 (n/a)</td><td>181.50 (n/a)</td><td>143.60 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>169.28 (n/a)</td><td>171.80 (n/a)</td><td>130.90 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>207.60 (n/a)</td><td>219.90 (n/a)</td><td>141.70 (n/a)</td><td>38.96 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>195.88 (n/a)</td><td>211.60 (n/a)</td><td>150.10 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>188.02 (n/a)</td><td>208.30 (n/a)</td><td>124.70 (n/a)</td><td>46.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>172.18 (n/a)</td><td>175.70 (n/a)</td><td>144.40 (n/a)</td><td>27.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.20 (n/a)</td><td>191.72 (n/a)</td><td>189.60 (n/a)</td><td>134.10 (n/a)</td><td>44.95 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.15 (-4.06%)</td><td>3.99 (-0.93%)</td><td>4.11 (+1.05%)</td><td>3.56 (+1.15%)</td><td>0.25 (-17.80%)</td><td>2642.10 (-1.14%)</td><td>2365.48 (+0.78%)</td><td>2285.80 (-1.04%)</td><td>2266.60 (+4.23%)</td><td>158.95 (-16.52%)</td><td>1632.14 (-4.06%)</td><td>1569.15 (-0.93%)</td><td>1618.40 (+1.05%)</td><td>1400.14 (+1.15%)</td><td>97.83 (-17.80%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.32 (n/a)</td><td>4.03 (n/a)</td><td>4.07 (n/a)</td><td>3.52 (n/a)</td><td>0.30 (n/a)</td><td>2672.50 (n/a)</td><td>2347.12 (n/a)</td><td>2309.90 (n/a)</td><td>2174.60 (n/a)</td><td>190.41 (n/a)</td><td>1701.20 (n/a)</td><td>1583.85 (n/a)</td><td>1601.54 (n/a)</td><td>1384.25 (n/a)</td><td>119.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.15 (+5.07%)</td><td>0.98 (+8.86%)</td><td>0.96 (+0.37%)</td><td>0.80 (+13.59%)</td><td>0.14 (-17.20%)</td><td>278.20 (-11.96%)</td><td>229.98 (-9.31%)</td><td>230.00 (-0.39%)</td><td>191.60 (-4.82%)</td><td>33.62 <b>(-32.19%)</b></td><td>49.26 (+5.07%)</td><td>41.73 (+8.86%)</td><td>41.02 (+0.37%)</td><td>33.93 (+13.59%)</td><td>5.96 (-17.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>0.96 (n/a)</td><td>0.70 (n/a)</td><td>0.17 (n/a)</td><td>316.00 (n/a)</td><td>253.60 (n/a)</td><td>230.90 (n/a)</td><td>201.30 (n/a)</td><td>49.57 (n/a)</td><td>46.88 (n/a)</td><td>38.33 (n/a)</td><td>40.88 (n/a)</td><td>29.87 (n/a)</td><td>7.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.16 (+0.64%)</td><td>0.99 (-0.22%)</td><td>1.02 (-0.94%)</td><td>0.75 (+9.27%)</td><td>0.16 (-13.58%)</td><td>293.60 (-8.48%)</td><td>228.18 (-0.87%)</td><td>217.60 (+0.97%)</td><td>191.40 (-0.62%)</td><td>40.75 <b>(-22.37%)</b></td><td>49.30 (+0.64%)</td><td>42.32 (-0.22%)</td><td>43.37 (-0.94%)</td><td>32.14 (+9.27%)</td><td>6.79 (-13.58%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.15 (n/a)</td><td>0.99 (n/a)</td><td>1.03 (n/a)</td><td>0.69 (n/a)</td><td>0.18 (n/a)</td><td>320.80 (n/a)</td><td>230.18 (n/a)</td><td>215.50 (n/a)</td><td>192.60 (n/a)</td><td>52.49 (n/a)</td><td>48.99 (n/a)</td><td>42.41 (n/a)</td><td>43.78 (n/a)</td><td>29.41 (n/a)</td><td>7.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.53 (+0.02%)</td><td>0.53 (+0.05%)</td><td>0.53 (+0.01%)</td><td>0.53 (+0.07%)</td><td>0.00 <b>(-20.81%)</b></td><td>47873.50 (-0.07%)</td><td>47800.64 (-0.05%)</td><td>47791.90 (-0.01%)</td><td>47768.10 (-0.02%)</td><td>41.98 <b>(-20.83%)</b></td><td>359.65 (+0.02%)</td><td>359.41 (+0.05%)</td><td>359.47 (+0.01%)</td><td>358.86 (+0.07%)</td><td>0.32 <b>(-20.81%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47905.70 (n/a)</td><td>47823.48 (n/a)</td><td>47797.00 (n/a)</td><td>47775.90 (n/a)</td><td>53.03 (n/a)</td><td>359.59 (n/a)</td><td>359.24 (n/a)</td><td>359.43 (n/a)</td><td>358.62 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.90 (-0.87%)</td><td>0.90 (-0.30%)</td><td>0.90 (+0.02%)</td><td>0.90 (-0.61%)</td><td>0.00 <b>(-26.87%)</b></td><td>28086.80 (+0.62%)</td><td>27917.04 (+0.30%)</td><td>27881.50 (-0.02%)</td><td>27841.70 (+0.88%)</td><td>97.51 <b>(-25.68%)</b></td><td>617.05 (-0.87%)</td><td>615.40 (-0.30%)</td><td>616.18 (+0.02%)</td><td>611.67 (-0.61%)</td><td>2.14 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27915.10 (n/a)</td><td>27832.26 (n/a)</td><td>27887.30 (n/a)</td><td>27599.20 (n/a)</td><td>131.21 (n/a)</td><td>622.48 (n/a)</td><td>617.28 (n/a)</td><td>616.05 (n/a)</td><td>615.43 (n/a)</td><td>2.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.33 (-0.10%)</td><td>3.24 (-0.36%)</td><td>3.26 (-0.25%)</td><td>3.13 (-0.53%)</td><td>0.09 <b>(+30.02%)</b></td><td>8035.70 (+0.53%)</td><td>7772.30 (+0.39%)</td><td>7726.60 (+0.25%)</td><td>7567.70 (+0.10%)</td><td>209.15 <b>(+30.31%)</b></td><td>2270.15 (-0.10%)</td><td>2211.67 (-0.36%)</td><td>2223.47 (-0.25%)</td><td>2137.95 (-0.53%)</td><td>59.16 <b>(+30.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.33 (n/a)</td><td>3.25 (n/a)</td><td>3.27 (n/a)</td><td>3.15 (n/a)</td><td>0.07 (n/a)</td><td>7993.00 (n/a)</td><td>7742.12 (n/a)</td><td>7707.10 (n/a)</td><td>7560.40 (n/a)</td><td>160.50 (n/a)</td><td>2272.36 (n/a)</td><td>2219.77 (n/a)</td><td>2229.11 (n/a)</td><td>2149.37 (n/a)</td><td>45.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.31 (+3.49%)</td><td>3.71 (+1.36%)</td><td>3.62 (-1.60%)</td><td>3.10 (-0.49%)</td><td>0.55 <b>(+47.97%)</b></td><td>2602.90 (+0.50%)</td><td>2211.46 (-0.44%)</td><td>2225.70 (+1.62%)</td><td>1869.90 (-3.37%)</td><td>327.81 <b>(+39.66%)</b></td><td>1130.48 (+3.49%)</td><td>973.01 (+1.36%)</td><td>949.77 (-1.60%)</td><td>812.16 (-0.49%)</td><td>144.79 <b>(+47.97%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.17 (n/a)</td><td>3.66 (n/a)</td><td>3.68 (n/a)</td><td>3.11 (n/a)</td><td>0.37 (n/a)</td><td>2590.00 (n/a)</td><td>2221.24 (n/a)</td><td>2190.20 (n/a)</td><td>1935.20 (n/a)</td><td>234.73 (n/a)</td><td>1092.37 (n/a)</td><td>959.92 (n/a)</td><td>965.17 (n/a)</td><td>816.19 (n/a)</td><td>97.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.35 <b>(-28.05%)</b></td><td>0.32 (-10.67%)</td><td>0.33 (+0.64%)</td><td>0.29 (-9.49%)</td><td>0.03 <b>(-65.25%)</b></td><td>4237.90 (+10.48%)</td><td>3865.36 (+9.64%)</td><td>3736.90 (-0.63%)</td><td>3518.60 <b>(+38.98%)</b></td><td>304.88 <b>(-45.50%)</b></td><td>19.07 <b>(-28.05%)</b></td><td>17.45 (-10.67%)</td><td>17.96 (+0.64%)</td><td>15.84 (-9.49%)</td><td>1.36 <b>(-65.25%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.49 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>3836.00 (n/a)</td><td>3525.38 (n/a)</td><td>3760.60 (n/a)</td><td>2531.80 (n/a)</td><td>559.38 (n/a)</td><td>26.51 (n/a)</td><td>19.53 (n/a)</td><td>17.85 (n/a)</td><td>17.49 (n/a)</td><td>3.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.08 <b>(+23.31%)</b></td><td>4.23 (+14.80%)</td><td>4.71 <b>(+26.22%)</b></td><td>3.10 (-7.65%)</td><td>0.89 <b>(+192.44%)</b></td><td>2142.40 (+8.28%)</td><td>1637.90 (-9.86%)</td><td>1411.00 <b>(-20.77%)</b></td><td>1308.90 (-18.90%)</td><td>377.32 <b>(+155.18%)</b></td><td>1570.23 <b>(+23.31%)</b></td><td>1305.50 (+14.80%)</td><td>1456.52 <b>(+26.22%)</b></td><td>959.29 (-7.65%)</td><td>276.12 <b>(+192.44%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.12 (n/a)</td><td>3.68 (n/a)</td><td>3.73 (n/a)</td><td>3.36 (n/a)</td><td>0.31 (n/a)</td><td>1978.60 (n/a)</td><td>1817.00 (n/a)</td><td>1781.00 (n/a)</td><td>1613.90 (n/a)</td><td>147.86 (n/a)</td><td>1273.42 (n/a)</td><td>1137.24 (n/a)</td><td>1153.96 (n/a)</td><td>1038.74 (n/a)</td><td>94.42 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.41 (n/a)</td><td>13.08 (n/a)</td><td>13.16 (n/a)</td><td>12.50 (n/a)</td><td>0.34 (n/a)</td><td>13.41 (n/a)</td><td>13.07 (n/a)</td><td>13.15 (n/a)</td><td>12.49 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>25.42 (+2.41%)</td><td>22.98 (-6.49%)</td><td>24.13 (-2.05%)</td><td>16.90 <b>(-30.10%)</b></td><td>3.44 <b>(+1304.77%)</b></td><td>25.40 (+2.41%)</td><td>22.97 (-6.49%)</td><td>24.11 (-2.05%)</td><td>16.89 <b>(-30.10%)</b></td><td>3.44 <b>(+1304.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>24.82 (n/a)</td><td>24.58 (n/a)</td><td>24.63 (n/a)</td><td>24.18 (n/a)</td><td>0.25 (n/a)</td><td>24.80 (n/a)</td><td>24.56 (n/a)</td><td>24.61 (n/a)</td><td>24.17 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>40.76 (-6.30%)</td><td>39.88 (-3.92%)</td><td>39.70 (-3.62%)</td><td>39.10 (-1.31%)</td><td>0.77 <b>(-46.71%)</b></td><td>40.74 (-6.30%)</td><td>39.85 (-3.92%)</td><td>39.68 (-3.62%)</td><td>39.08 (-1.31%)</td><td>0.77 <b>(-46.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>43.50 (n/a)</td><td>41.50 (n/a)</td><td>41.19 (n/a)</td><td>39.62 (n/a)</td><td>1.44 (n/a)</td><td>43.48 (n/a)</td><td>41.48 (n/a)</td><td>41.17 (n/a)</td><td>39.60 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>43.27 (-4.71%)</td><td>42.43 (+0.12%)</td><td>42.31 (+0.31%)</td><td>41.16 (+9.20%)</td><td>0.87 <b>(-71.01%)</b></td><td>43.24 (-4.71%)</td><td>42.41 (+0.12%)</td><td>42.29 (+0.31%)</td><td>41.13 (+9.20%)</td><td>0.87 <b>(-71.01%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>45.41 (n/a)</td><td>42.38 (n/a)</td><td>42.18 (n/a)</td><td>37.69 (n/a)</td><td>2.99 (n/a)</td><td>45.38 (n/a)</td><td>42.36 (n/a)</td><td>42.16 (n/a)</td><td>37.67 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.46 (n/a)</td><td>12.62 (n/a)</td><td>12.84 (n/a)</td><td>10.94 (n/a)</td><td>1.02 (n/a)</td><td>13.45 (n/a)</td><td>12.61 (n/a)</td><td>12.83 (n/a)</td><td>10.94 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>24.46 (-2.29%)</td><td>23.86 (-0.54%)</td><td>24.13 (-0.40%)</td><td>22.31 (-3.45%)</td><td>0.88 (+11.20%)</td><td>24.44 (-2.29%)</td><td>23.84 (-0.54%)</td><td>24.12 (-0.40%)</td><td>22.30 (-3.45%)</td><td>0.88 (+11.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>25.03 (n/a)</td><td>23.99 (n/a)</td><td>24.23 (n/a)</td><td>23.11 (n/a)</td><td>0.79 (n/a)</td><td>25.02 (n/a)</td><td>23.97 (n/a)</td><td>24.21 (n/a)</td><td>23.10 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>41.75 (-0.30%)</td><td>39.69 (-0.43%)</td><td>40.42 (+1.19%)</td><td>37.50 (-1.27%)</td><td>1.91 <b>(+22.82%)</b></td><td>41.73 (-0.30%)</td><td>39.67 (-0.43%)</td><td>40.39 (+1.19%)</td><td>37.47 (-1.27%)</td><td>1.91 <b>(+22.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>41.88 (n/a)</td><td>39.87 (n/a)</td><td>39.94 (n/a)</td><td>37.98 (n/a)</td><td>1.56 (n/a)</td><td>41.85 (n/a)</td><td>39.84 (n/a)</td><td>39.92 (n/a)</td><td>37.96 (n/a)</td><td>1.56 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>43.74 (-5.01%)</td><td>42.20 (+2.27%)</td><td>41.86 (-0.36%)</td><td>41.66 (+14.05%)</td><td>0.87 <b>(-75.30%)</b></td><td>43.71 (-5.01%)</td><td>42.17 (+2.27%)</td><td>41.83 (-0.36%)</td><td>41.64 (+14.05%)</td><td>0.87 <b>(-75.30%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>46.05 (n/a)</td><td>41.26 (n/a)</td><td>42.01 (n/a)</td><td>36.53 (n/a)</td><td>3.52 (n/a)</td><td>46.02 (n/a)</td><td>41.23 (n/a)</td><td>41.98 (n/a)</td><td>36.51 (n/a)</td><td>3.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>8.71 (-7.49%)</td><td>8.50 (-5.70%)</td><td>8.68 (-5.68%)</td><td>7.85 (-6.53%)</td><td>0.37 (-16.87%)</td><td>8.70 (-7.49%)</td><td>8.48 (-5.70%)</td><td>8.67 (-5.68%)</td><td>7.83 (-6.53%)</td><td>0.37 (-16.87%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>9.42 (n/a)</td><td>9.01 (n/a)</td><td>9.21 (n/a)</td><td>8.40 (n/a)</td><td>0.44 (n/a)</td><td>9.40 (n/a)</td><td>8.99 (n/a)</td><td>9.19 (n/a)</td><td>8.38 (n/a)</td><td>0.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.10 (+13.99%)</td><td>0.94 (+8.64%)</td><td>0.94 (+9.79%)</td><td>0.75 (+3.68%)</td><td>0.13 <b>(+39.45%)</b></td><td>1.08 (+13.99%)</td><td>0.92 (+8.64%)</td><td>0.93 (+9.79%)</td><td>0.73 (+3.68%)</td><td>0.13 <b>(+39.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.96 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.72 (n/a)</td><td>0.09 (n/a)</td><td>0.95 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.21 (-17.81%)</td><td>1.03 (-13.20%)</td><td>1.01 (-13.73%)</td><td>0.94 (-4.76%)</td><td>0.10 <b>(-41.97%)</b></td><td>1.20 (-17.81%)</td><td>1.02 (-13.20%)</td><td>1.00 (-13.73%)</td><td>0.93 (-4.76%)</td><td>0.10 <b>(-41.97%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.47 (n/a)</td><td>1.19 (n/a)</td><td>1.17 (n/a)</td><td>0.99 (n/a)</td><td>0.18 (n/a)</td><td>1.45 (n/a)</td><td>1.17 (n/a)</td><td>1.16 (n/a)</td><td>0.98 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>17.68 (-3.89%)</td><td>16.28 (-9.13%)</td><td>15.91 (-11.64%)</td><td>15.11 (-12.64%)</td><td>1.04 <b>(+104.61%)</b></td><td>17.48 (-3.89%)</td><td>16.09 (-9.13%)</td><td>15.73 (-11.64%)</td><td>14.93 (-12.64%)</td><td>1.03 <b>(+104.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>18.40 (n/a)</td><td>17.92 (n/a)</td><td>18.01 (n/a)</td><td>17.29 (n/a)</td><td>0.51 (n/a)</td><td>18.19 (n/a)</td><td>17.71 (n/a)</td><td>17.80 (n/a)</td><td>17.09 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.42 (-6.14%)</td><td>12.20 (-10.53%)</td><td>13.13 (-1.79%)</td><td>8.09 <b>(-38.72%)</b></td><td>2.30 <b>(+394.48%)</b></td><td>13.18 (-6.14%)</td><td>11.99 (-10.53%)</td><td>12.90 (-1.79%)</td><td>7.95 <b>(-38.72%)</b></td><td>2.26 <b>(+394.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>14.30 (n/a)</td><td>13.64 (n/a)</td><td>13.37 (n/a)</td><td>13.21 (n/a)</td><td>0.47 (n/a)</td><td>14.05 (n/a)</td><td>13.40 (n/a)</td><td>13.14 (n/a)</td><td>12.98 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.82 (-12.48%)</td><td>7.35 (-4.87%)</td><td>7.62 (-2.11%)</td><td>6.67 <b>(+27.98%)</b></td><td>0.51 <b>(-66.20%)</b></td><td>7.68 (-12.48%)</td><td>7.22 (-4.87%)</td><td>7.48 (-2.11%)</td><td>6.55 <b>(+27.98%)</b></td><td>0.50 <b>(-66.20%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>8.93 (n/a)</td><td>7.72 (n/a)</td><td>7.78 (n/a)</td><td>5.21 (n/a)</td><td>1.52 (n/a)</td><td>8.78 (n/a)</td><td>7.59 (n/a)</td><td>7.64 (n/a)</td><td>5.12 (n/a)</td><td>1.49 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.00 (+6.54%)</td><td>5.97 (+9.08%)</td><td>5.76 (+4.14%)</td><td>5.45 <b>(+26.99%)</b></td><td>0.63 <b>(-27.62%)</b></td><td>6.89 (+6.54%)</td><td>5.87 (+9.08%)</td><td>5.66 (+4.14%)</td><td>5.36 <b>(+26.99%)</b></td><td>0.62 <b>(-27.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>6.57 (n/a)</td><td>5.47 (n/a)</td><td>5.53 (n/a)</td><td>4.29 (n/a)</td><td>0.87 (n/a)</td><td>6.47 (n/a)</td><td>5.38 (n/a)</td><td>5.44 (n/a)</td><td>4.22 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.55 (n/a)</td><td>13.01 (n/a)</td><td>13.12 (n/a)</td><td>11.83 (n/a)</td><td>0.70 (n/a)</td><td>13.54 (n/a)</td><td>13.01 (n/a)</td><td>13.11 (n/a)</td><td>11.82 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.39 (n/a)</td><td>12.15 (n/a)</td><td>12.33 (n/a)</td><td>10.68 (n/a)</td><td>1.00 (n/a)</td><td>13.39 (n/a)</td><td>12.14 (n/a)</td><td>12.32 (n/a)</td><td>10.67 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.20 (n/a)</td><td>180.84 (n/a)</td><td>174.90 (n/a)</td><td>168.80 (n/a)</td><td>12.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>172.68 (n/a)</td><td>160.90 (n/a)</td><td>134.20 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.80 (n/a)</td><td>188.82 (n/a)</td><td>187.10 (n/a)</td><td>169.80 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>193.12 (n/a)</td><td>178.40 (n/a)</td><td>171.20 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.60 (n/a)</td><td>195.22 (n/a)</td><td>199.50 (n/a)</td><td>180.00 (n/a)</td><td>14.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>217.80 (n/a)</td><td>168.86 (n/a)</td><td>177.30 (n/a)</td><td>100.00 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>198.02 (n/a)</td><td>205.50 (n/a)</td><td>159.40 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>252.00 (n/a)</td><td>204.94 (n/a)</td><td>195.50 (n/a)</td><td>181.00 (n/a)</td><td>27.55 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (+17.55%)</td><td>0.05 (+9.83%)</td><td>0.05 (+6.33%)</td><td>0.04 (+8.77%)</td><td>0.01 <b>(+35.01%)</b></td><td>197.80 (-8.04%)</td><td>161.36 (-8.51%)</td><td>155.50 (-5.99%)</td><td>135.80 (-14.97%)</td><td>24.15 (+5.70%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>176.36 (n/a)</td><td>165.40 (n/a)</td><td>159.70 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-3.31%)</td><td>0.05 (-0.20%)</td><td>0.05 (+0.96%)</td><td>0.04 (-1.57%)</td><td>0.01 (-4.02%)</td><td>215.90 (+1.60%)</td><td>177.52 (+0.17%)</td><td>169.50 (-0.94%)</td><td>159.70 (+3.43%)</td><td>22.36 (+1.36%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>177.22 (n/a)</td><td>171.10 (n/a)</td><td>154.40 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 <b>(+23.16%)</b></td><td>0.06 <b>(+57.76%)</b></td><td>0.06 <b>(+48.98%)</b></td><td>0.05 <b>(+133.83%)</b></td><td>0.01 <b>(-56.31%)</b></td><td>164.30 <b>(-57.25%)</b></td><td>142.10 <b>(-42.10%)</b></td><td>141.60 <b>(-32.89%)</b></td><td>128.60 (-18.81%)</td><td>13.63 <b>(-84.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>384.30 (n/a)</td><td>245.44 (n/a)</td><td>211.00 (n/a)</td><td>158.40 (n/a)</td><td>90.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-11.65%)</td><td>0.04 (-4.76%)</td><td>0.05 (+6.20%)</td><td>0.04 (-10.41%)</td><td>0.01 (-12.41%)</td><td>230.90 (+11.60%)</td><td>189.02 (+4.92%)</td><td>172.80 (-5.83%)</td><td>169.40 (+13.24%)</td><td>26.96 (+8.70%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>180.16 (n/a)</td><td>183.50 (n/a)</td><td>149.60 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (+17.12%)</td><td>0.05 <b>(+23.19%)</b></td><td>0.05 <b>(+28.75%)</b></td><td>0.04 <b>(+28.71%)</b></td><td>0.01 <b>(-22.19%)</b></td><td>187.80 <b>(-22.33%)</b></td><td>161.16 <b>(-20.24%)</b></td><td>159.90 <b>(-22.34%)</b></td><td>138.20 (-14.64%)</td><td>19.82 <b>(-47.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>202.06 (n/a)</td><td>205.90 (n/a)</td><td>161.90 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (+16.43%)</td><td>0.06 <b>(+23.64%)</b></td><td>0.06 <b>(+33.25%)</b></td><td>0.05 (+11.41%)</td><td>0.01 <b>(+38.41%)</b></td><td>175.10 (-10.25%)</td><td>137.46 (-18.60%)</td><td>127.30 <b>(-24.99%)</b></td><td>120.00 (-14.16%)</td><td>22.90 (+7.24%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>168.88 (n/a)</td><td>169.70 (n/a)</td><td>139.80 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (-6.50%)</td><td>0.05 (+4.63%)</td><td>0.05 (+12.89%)</td><td>0.04 (+0.35%)</td><td>0.01 (-18.91%)</td><td>211.80 (-0.38%)</td><td>175.52 (-5.30%)</td><td>171.20 (-11.43%)</td><td>138.20 (+6.97%)</td><td>29.96 (-11.19%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>185.34 (n/a)</td><td>193.30 (n/a)</td><td>129.20 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-3.12%)</td><td>0.04 (+2.34%)</td><td>0.04 (-0.67%)</td><td>0.04 (+11.24%)</td><td>0.00 <b>(-49.45%)</b></td><td>202.70 (-10.11%)</td><td>191.58 (-3.07%)</td><td>192.00 (+0.68%)</td><td>176.60 (+3.21%)</td><td>10.50 <b>(-53.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.50 (n/a)</td><td>197.64 (n/a)</td><td>190.70 (n/a)</td><td>171.10 (n/a)</td><td>22.62 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (+5.47%)</td><td>0.04 (-9.66%)</td><td>0.05 (-2.37%)</td><td>0.03 <b>(-22.25%)</b></td><td>0.01 <b>(+83.28%)</b></td><td>301.80 <b>(+28.64%)</b></td><td>220.92 (+17.36%)</td><td>179.00 (+2.40%)</td><td>154.40 (-5.16%)</td><td>70.17 <b>(+135.32%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>188.24 (n/a)</td><td>174.80 (n/a)</td><td>162.80 (n/a)</td><td>29.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (+14.74%)</td><td>0.04 (+11.70%)</td><td>0.04 (+3.56%)</td><td>0.03 <b>(+38.10%)</b></td><td>0.00 <b>(-42.13%)</b></td><td>241.20 <b>(-27.61%)</b></td><td>223.84 (-11.88%)</td><td>225.40 (-3.43%)</td><td>202.20 (-12.84%)</td><td>16.13 <b>(-63.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>333.20 (n/a)</td><td>254.02 (n/a)</td><td>233.40 (n/a)</td><td>232.00 (n/a)</td><td>44.36 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (-15.86%)</td><td>0.05 (-16.82%)</td><td>0.04 (-15.73%)</td><td>0.04 (-5.72%)</td><td>0.01 <b>(-27.47%)</b></td><td>220.80 (+6.10%)</td><td>184.32 (+18.53%)</td><td>190.10 (+18.66%)</td><td>137.20 (+18.79%)</td><td>35.95 (-4.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>155.50 (n/a)</td><td>160.20 (n/a)</td><td>115.50 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 <b>(-25.40%)</b></td><td>0.04 (-3.51%)</td><td>0.04 (-7.68%)</td><td>0.03 <b>(+48.23%)</b></td><td>0.00 <b>(-82.68%)</b></td><td>238.40 <b>(-32.52%)</b></td><td>224.38 (-6.73%)</td><td>224.10 (+8.31%)</td><td>205.30 <b>(+34.01%)</b></td><td>13.87 <b>(-84.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>353.30 (n/a)</td><td>240.58 (n/a)</td><td>206.90 (n/a)</td><td>153.20 (n/a)</td><td>89.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (+0.04%)</td><td>0.04 (-6.33%)</td><td>0.05 (+3.53%)</td><td>0.03 <b>(-20.98%)</b></td><td>0.01 <b>(+75.68%)</b></td><td>268.80 <b>(+26.55%)</b></td><td>196.52 (+10.35%)</td><td>169.10 (-3.43%)</td><td>151.40 (-0.07%)</td><td>48.81 <b>(+121.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>178.08 (n/a)</td><td>175.10 (n/a)</td><td>151.50 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (+3.81%)</td><td>0.04 (+2.77%)</td><td>0.04 (+12.37%)</td><td>0.04 (+1.23%)</td><td>0.00 (-1.62%)</td><td>211.70 (-1.26%)</td><td>188.10 (-2.79%)</td><td>182.70 (-11.01%)</td><td>161.10 (-3.71%)</td><td>19.87 (-5.49%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>214.40 (n/a)</td><td>193.50 (n/a)</td><td>205.30 (n/a)</td><td>167.30 (n/a)</td><td>21.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (+14.44%)</td><td>0.05 (-6.52%)</td><td>0.04 (-4.32%)</td><td>0.03 <b>(-25.81%)</b></td><td>0.01 <b>(+104.15%)</b></td><td>261.50 <b>(+34.79%)</b></td><td>192.90 (+12.74%)</td><td>187.40 (+4.52%)</td><td>124.30 (-12.59%)</td><td>53.62 <b>(+140.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>171.10 (n/a)</td><td>179.30 (n/a)</td><td>142.20 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (+7.44%)</td><td>0.05 (-0.86%)</td><td>0.05 (-2.62%)</td><td>0.04 (-3.21%)</td><td>0.01 (+6.33%)</td><td>216.30 (+3.30%)</td><td>172.28 (+0.89%)</td><td>173.80 (+2.72%)</td><td>117.30 (-6.90%)</td><td>36.15 (-4.51%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>170.76 (n/a)</td><td>169.20 (n/a)</td><td>126.00 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-11.54%)</td><td>0.04 (-13.09%)</td><td>0.04 (-16.99%)</td><td>0.04 (-12.40%)</td><td>0.01 (-0.17%)</td><td>220.50 (+14.19%)</td><td>191.72 (+15.68%)</td><td>206.50 <b>(+20.48%)</b></td><td>149.20 (+13.03%)</td><td>29.90 <b>(+31.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>165.74 (n/a)</td><td>171.40 (n/a)</td><td>132.00 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-18.27%)</td><td>0.04 (-17.73%)</td><td>0.04 (-14.53%)</td><td>0.03 <b>(-36.42%)</b></td><td>0.01 <b>(+34.06%)</b></td><td>314.40 <b>(+57.28%)</b></td><td>209.10 <b>(+26.05%)</b></td><td>190.20 (+17.05%)</td><td>169.80 <b>(+22.42%)</b></td><td>60.09 <b>(+163.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.90 (n/a)</td><td>165.88 (n/a)</td><td>162.50 (n/a)</td><td>138.70 (n/a)</td><td>22.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.18 (+1.07%)</td><td>0.18 (+0.39%)</td><td>0.18 (+0.20%)</td><td>0.18 (+0.29%)</td><td>0.00 <b>(+133.96%)</b></td><td>47590.50 (-0.29%)</td><td>47391.48 (-0.39%)</td><td>47446.60 (-0.20%)</td><td>46966.80 (-1.06%)</td><td>250.60 <b>(+130.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47727.10 (n/a)</td><td>47575.24 (n/a)</td><td>47543.60 (n/a)</td><td>47469.90 (n/a)</td><td>108.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.18 <b>(+24.19%)</b></td><td>0.16 <b>(+21.61%)</b></td><td>0.16 <b>(+20.93%)</b></td><td>0.12 (+8.62%)</td><td>0.02 <b>(+51.23%)</b></td><td>208.80 (-7.94%)</td><td>161.38 (-17.08%)</td><td>149.90 (-17.32%)</td><td>137.80 (-19.51%)</td><td>27.76 (+15.03%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>194.62 (n/a)</td><td>181.30 (n/a)</td><td>171.20 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.27 (+7.76%)</td><td>0.22 (-6.10%)</td><td>0.20 (-16.17%)</td><td>0.19 (-12.06%)</td><td>0.04 <b>(+147.43%)</b></td><td>216.60 (+13.70%)</td><td>189.32 (+8.43%)</td><td>207.10 (+19.30%)</td><td>150.60 (-7.21%)</td><td>29.73 <b>(+162.70%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>190.50 (n/a)</td><td>174.60 (n/a)</td><td>173.60 (n/a)</td><td>162.30 (n/a)</td><td>11.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (-9.58%)</td><td>0.03 (+5.51%)</td><td>0.03 (+9.72%)</td><td>0.03 (+7.66%)</td><td>0.00 <b>(-51.03%)</b></td><td>183.80 (-7.12%)</td><td>165.30 (-6.38%)</td><td>159.50 (-8.86%)</td><td>153.70 (+10.58%)</td><td>12.04 <b>(-49.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>176.56 (n/a)</td><td>175.00 (n/a)</td><td>139.00 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (-7.89%)</td><td>0.05 (-4.65%)</td><td>0.06 (-7.80%)</td><td>0.05 (+13.83%)</td><td>0.01 <b>(-39.43%)</b></td><td>175.20 (-12.14%)</td><td>151.96 (+2.41%)</td><td>147.60 (+8.45%)</td><td>126.00 (+8.53%)</td><td>19.07 <b>(-42.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>148.38 (n/a)</td><td>136.10 (n/a)</td><td>116.10 (n/a)</td><td>33.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.10 (-6.43%)</td><td>0.08 (-6.56%)</td><td>0.08 (+1.16%)</td><td>0.07 (-6.50%)</td><td>0.01 (-7.62%)</td><td>180.70 (+6.99%)</td><td>155.96 (+7.01%)</td><td>149.90 (-1.19%)</td><td>128.50 (+6.91%)</td><td>21.17 (+7.87%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>168.90 (n/a)</td><td>145.74 (n/a)</td><td>151.70 (n/a)</td><td>120.20 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (+2.99%)</td><td>0.05 (-11.58%)</td><td>0.05 (-12.25%)</td><td>0.03 (-17.09%)</td><td>0.01 <b>(+27.24%)</b></td><td>235.00 <b>(+20.64%)</b></td><td>180.18 (+15.78%)</td><td>175.80 (+13.93%)</td><td>125.00 (-2.87%)</td><td>43.40 <b>(+53.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>155.62 (n/a)</td><td>154.30 (n/a)</td><td>128.70 (n/a)</td><td>28.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (-1.92%)</td><td>0.07 (-1.50%)</td><td>0.07 (+3.90%)</td><td>0.05 (+8.89%)</td><td>0.01 (-11.24%)</td><td>203.40 (-8.13%)</td><td>160.16 (+0.53%)</td><td>149.30 (-3.80%)</td><td>130.40 (+1.95%)</td><td>30.50 (-17.90%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>159.32 (n/a)</td><td>155.20 (n/a)</td><td>127.90 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (-19.30%)</td><td>0.05 (-3.54%)</td><td>0.05 (+16.82%)</td><td>0.04 (-9.28%)</td><td>0.01 <b>(-32.84%)</b></td><td>227.20 (+10.24%)</td><td>167.58 (+2.17%)</td><td>151.50 (-14.41%)</td><td>145.80 <b>(+23.87%)</b></td><td>33.94 (-4.89%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.10 (n/a)</td><td>164.02 (n/a)</td><td>177.00 (n/a)</td><td>117.70 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.11 <b>(+29.19%)</b></td><td>0.07 (-1.98%)</td><td>0.06 (-9.61%)</td><td>0.04 (-17.54%)</td><td>0.03 <b>(+85.68%)</b></td><td>268.10 <b>(+21.26%)</b></td><td>184.96 (+13.89%)</td><td>175.30 (+10.60%)</td><td>89.40 <b>(-22.60%)</b></td><td>76.20 <b>(+81.79%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>221.10 (n/a)</td><td>162.40 (n/a)</td><td>158.50 (n/a)</td><td>115.50 (n/a)</td><td>41.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (-6.40%)</td><td>0.05 (-13.45%)</td><td>0.05 <b>(-26.32%)</b></td><td>0.04 (-7.93%)</td><td>0.01 (-4.36%)</td><td>206.40 (+8.63%)</td><td>161.14 (+15.76%)</td><td>170.50 <b>(+35.75%)</b></td><td>116.10 (+6.81%)</td><td>36.57 (+9.04%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>139.20 (n/a)</td><td>125.60 (n/a)</td><td>108.70 (n/a)</td><td>33.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (+12.54%)</td><td>0.05 (-1.22%)</td><td>0.05 (-16.79%)</td><td>0.04 (+7.80%)</td><td>0.01 (+16.77%)</td><td>216.20 (-7.21%)</td><td>181.12 (+1.48%)</td><td>189.40 <b>(+20.18%)</b></td><td>119.70 (-11.14%)</td><td>37.42 (-9.00%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.00 (n/a)</td><td>178.48 (n/a)</td><td>157.60 (n/a)</td><td>134.70 (n/a)</td><td>41.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (-9.58%)</td><td>0.05 (+0.08%)</td><td>0.05 (+4.43%)</td><td>0.04 (+1.02%)</td><td>0.01 <b>(-37.68%)</b></td><td>187.60 (-1.00%)</td><td>153.74 (-1.64%)</td><td>150.70 (-4.20%)</td><td>134.50 (+10.52%)</td><td>20.13 <b>(-30.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>156.30 (n/a)</td><td>157.30 (n/a)</td><td>121.70 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (-8.91%)</td><td>0.06 (-2.44%)</td><td>0.06 <b>(-21.59%)</b></td><td>0.05 <b>(+47.15%)</b></td><td>0.01 <b>(-67.65%)</b></td><td>174.60 <b>(-32.04%)</b></td><td>158.18 (-7.44%)</td><td>162.10 <b>(+27.54%)</b></td><td>131.40 (+9.77%)</td><td>16.00 <b>(-75.98%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>256.90 (n/a)</td><td>170.90 (n/a)</td><td>127.10 (n/a)</td><td>119.70 (n/a)</td><td>66.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-8.99%)</td><td>0.04 (-2.40%)</td><td>0.05 (+3.83%)</td><td>0.03 (+9.12%)</td><td>0.01 <b>(-26.87%)</b></td><td>274.60 (-8.34%)</td><td>194.46 (-0.34%)</td><td>178.70 (-3.67%)</td><td>159.00 (+9.88%)</td><td>45.75 <b>(-25.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>299.60 (n/a)</td><td>195.12 (n/a)</td><td>185.50 (n/a)</td><td>144.70 (n/a)</td><td>61.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (+4.49%)</td><td>0.05 (-5.78%)</td><td>0.04 (-11.60%)</td><td>0.04 (+3.55%)</td><td>0.01 (+2.75%)</td><td>221.30 (-3.45%)</td><td>195.98 (+6.05%)</td><td>205.60 (+13.09%)</td><td>153.20 (-4.25%)</td><td>26.04 (-7.08%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>184.80 (n/a)</td><td>181.80 (n/a)</td><td>160.00 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (+10.92%)</td><td>0.05 (+3.96%)</td><td>0.04 (-8.90%)</td><td>0.04 <b>(+31.66%)</b></td><td>0.01 (-14.82%)</td><td>203.70 <b>(-24.02%)</b></td><td>181.46 (-5.72%)</td><td>191.90 (+9.78%)</td><td>138.40 (-9.84%)</td><td>25.99 <b>(-43.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.10 (n/a)</td><td>192.46 (n/a)</td><td>174.80 (n/a)</td><td>153.50 (n/a)</td><td>46.09 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (-1.83%)</td><td>0.05 (+10.61%)</td><td>0.05 (+12.39%)</td><td>0.04 <b>(+44.58%)</b></td><td>0.01 <b>(-36.41%)</b></td><td>205.80 <b>(-30.82%)</b></td><td>178.88 (-14.46%)</td><td>192.10 (-11.02%)</td><td>136.70 (+1.86%)</td><td>29.74 <b>(-54.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>297.50 (n/a)</td><td>209.12 (n/a)</td><td>215.90 (n/a)</td><td>134.20 (n/a)</td><td>64.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (-1.14%)</td><td>0.04 (+6.27%)</td><td>0.04 (+4.03%)</td><td>0.03 (+1.80%)</td><td>0.01 (-15.33%)</td><td>316.20 (-1.77%)</td><td>228.88 (-7.31%)</td><td>220.80 (-3.87%)</td><td>172.00 (+1.18%)</td><td>53.09 (-15.16%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.90 (n/a)</td><td>246.92 (n/a)</td><td>229.70 (n/a)</td><td>170.00 (n/a)</td><td>62.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.57 <b>(-22.11%)</b></td><td>0.52 <b>(-20.14%)</b></td><td>0.54 (-16.28%)</td><td>0.42 <b>(-23.21%)</b></td><td>0.07 (-8.02%)</td><td>236.60 <b>(+30.21%)</b></td><td>191.82 <b>(+25.72%)</b></td><td>180.60 (+19.44%)</td><td>171.50 <b>(+28.37%)</b></td><td>27.02 <b>(+51.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.07 (n/a)</td><td>181.70 (n/a)</td><td>152.58 (n/a)</td><td>151.20 (n/a)</td><td>133.60 (n/a)</td><td>17.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.68 (-1.58%)</td><td>0.57 (-10.00%)</td><td>0.53 <b>(-21.78%)</b></td><td>0.44 (-4.01%)</td><td>0.10 (+5.48%)</td><td>223.70 (+4.14%)</td><td>178.12 (+11.44%)</td><td>187.10 <b>(+27.89%)</b></td><td>144.10 (+1.62%)</td><td>33.15 (+6.46%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.69 (n/a)</td><td>0.63 (n/a)</td><td>0.67 (n/a)</td><td>0.46 (n/a)</td><td>0.10 (n/a)</td><td>214.80 (n/a)</td><td>159.84 (n/a)</td><td>146.30 (n/a)</td><td>141.80 (n/a)</td><td>31.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.64 (-9.18%)</td><td>0.54 (-7.04%)</td><td>0.49 (-19.59%)</td><td>0.48 (+17.06%)</td><td>0.08 <b>(-29.91%)</b></td><td>206.20 (-14.58%)</td><td>183.58 (+5.52%)</td><td>199.30 <b>(+24.33%)</b></td><td>153.40 (+10.12%)</td><td>25.14 <b>(-36.76%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.71 (n/a)</td><td>0.59 (n/a)</td><td>0.61 (n/a)</td><td>0.41 (n/a)</td><td>0.11 (n/a)</td><td>241.40 (n/a)</td><td>173.98 (n/a)</td><td>160.30 (n/a)</td><td>139.30 (n/a)</td><td>39.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.83 (+16.49%)</td><td>0.56 (-6.97%)</td><td>0.57 (-1.74%)</td><td>0.34 <b>(-29.50%)</b></td><td>0.21 <b>(+130.46%)</b></td><td>285.40 <b>(+41.85%)</b></td><td>199.82 (+19.52%)</td><td>172.90 (+1.77%)</td><td>118.30 (-14.15%)</td><td>78.51 <b>(+204.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.71 (n/a)</td><td>0.60 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.09 (n/a)</td><td>201.20 (n/a)</td><td>167.18 (n/a)</td><td>169.90 (n/a)</td><td>137.80 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.43 (-17.31%)</td><td>0.38 (-16.27%)</td><td>0.41 (-12.49%)</td><td>0.27 (-15.68%)</td><td>0.06 (-18.76%)</td><td>269.60 (+18.61%)</td><td>198.88 (+19.25%)</td><td>180.10 (+14.28%)</td><td>172.60 <b>(+20.87%)</b></td><td>40.60 (+16.40%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.52 (n/a)</td><td>0.46 (n/a)</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>227.30 (n/a)</td><td>166.78 (n/a)</td><td>157.60 (n/a)</td><td>142.80 (n/a)</td><td>34.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.49 (-12.45%)</td><td>0.35 <b>(-20.57%)</b></td><td>0.32 (-18.17%)</td><td>0.29 (-15.09%)</td><td>0.09 <b>(-20.91%)</b></td><td>256.10 (+17.80%)</td><td>217.72 <b>(+25.16%)</b></td><td>227.40 <b>(+22.19%)</b></td><td>149.20 (+14.24%)</td><td>44.18 (+10.29%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>217.40 (n/a)</td><td>173.96 (n/a)</td><td>186.10 (n/a)</td><td>130.60 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.49 <b>(-23.23%)</b></td><td>0.40 (-14.94%)</td><td>0.40 (+1.45%)</td><td>0.30 (-14.16%)</td><td>0.07 <b>(-45.19%)</b></td><td>243.20 (+16.48%)</td><td>189.70 (+14.41%)</td><td>183.00 (-1.40%)</td><td>151.40 <b>(+30.18%)</b></td><td>34.14 (-14.33%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.63 (n/a)</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>208.80 (n/a)</td><td>165.80 (n/a)</td><td>185.60 (n/a)</td><td>116.30 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.54 (+9.51%)</td><td>0.41 (+3.43%)</td><td>0.39 (+1.92%)</td><td>0.29 (-11.53%)</td><td>0.09 <b>(+42.09%)</b></td><td>257.40 (+13.04%)</td><td>188.90 (-1.19%)</td><td>188.00 (-1.88%)</td><td>135.80 (-8.74%)</td><td>44.28 <b>(+49.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>227.70 (n/a)</td><td>191.18 (n/a)</td><td>191.60 (n/a)</td><td>148.80 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.98 (-3.95%)</td><td>0.89 (-3.51%)</td><td>0.91 (-4.98%)</td><td>0.81 (+15.61%)</td><td>0.07 <b>(-45.73%)</b></td><td>160.90 (-13.49%)</td><td>148.42 (+2.20%)</td><td>144.50 (+5.24%)</td><td>133.40 (+4.06%)</td><td>11.77 <b>(-50.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.02 (n/a)</td><td>0.92 (n/a)</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.13 (n/a)</td><td>186.00 (n/a)</td><td>145.22 (n/a)</td><td>137.30 (n/a)</td><td>128.20 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.92 (-11.71%)</td><td>0.78 (-10.61%)</td><td>0.73 (-18.45%)</td><td>0.70 (+0.09%)</td><td>0.10 <b>(-32.22%)</b></td><td>187.80 (-0.11%)</td><td>170.34 (+10.68%)</td><td>178.70 <b>(+22.65%)</b></td><td>142.20 (+13.31%)</td><td>20.05 <b>(-23.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.04 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>0.70 (n/a)</td><td>0.14 (n/a)</td><td>188.00 (n/a)</td><td>153.90 (n/a)</td><td>145.70 (n/a)</td><td>125.50 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.83 <b>(-21.13%)</b></td><td>0.77 (-6.24%)</td><td>0.76 (+6.74%)</td><td>0.73 (+12.07%)</td><td>0.04 <b>(-78.87%)</b></td><td>178.70 (-10.74%)</td><td>170.08 (+2.56%)</td><td>173.60 (-6.26%)</td><td>158.70 <b>(+26.76%)</b></td><td>8.83 <b>(-75.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.05 (n/a)</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.19 (n/a)</td><td>200.20 (n/a)</td><td>165.84 (n/a)</td><td>185.20 (n/a)</td><td>125.20 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (+14.61%)</td><td>0.03 <b>(+29.17%)</b></td><td>0.03 <b>(+39.88%)</b></td><td>0.02 <b>(+25.12%)</b></td><td>0.00 (+6.43%)</td><td>177.20 <b>(-20.11%)</b></td><td>148.42 <b>(-23.11%)</b></td><td>149.60 <b>(-28.49%)</b></td><td>123.70 (-12.76%)</td><td>24.61 <b>(-28.22%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>193.04 (n/a)</td><td>209.20 (n/a)</td><td>141.80 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 <b>(+33.36%)</b></td><td>0.03 <b>(+30.85%)</b></td><td>0.03 <b>(+22.57%)</b></td><td>0.03 <b>(+32.27%)</b></td><td>0.00 <b>(+41.62%)</b></td><td>160.90 <b>(-24.39%)</b></td><td>144.06 <b>(-23.46%)</b></td><td>151.80 (-18.43%)</td><td>124.60 <b>(-24.98%)</b></td><td>17.98 <b>(-20.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.80 (n/a)</td><td>188.22 (n/a)</td><td>186.10 (n/a)</td><td>166.10 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (-2.48%)</td><td>0.02 (+2.18%)</td><td>0.02 (+1.33%)</td><td>0.02 (+12.29%)</td><td>0.00 <b>(-51.01%)</b></td><td>177.70 (-10.93%)</td><td>167.42 (-2.83%)</td><td>167.00 (-1.30%)</td><td>154.90 (+2.58%)</td><td>8.40 <b>(-55.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.50 (n/a)</td><td>172.30 (n/a)</td><td>169.20 (n/a)</td><td>151.00 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.89 <b>(-20.03%)</b></td><td>0.73 (-15.64%)</td><td>0.75 (-12.64%)</td><td>0.57 (-17.22%)</td><td>0.13 <b>(-22.03%)</b></td><td>233.30 <b>(+20.82%)</b></td><td>187.28 (+18.31%)</td><td>176.60 (+14.45%)</td><td>148.10 <b>(+25.08%)</b></td><td>35.06 (+18.56%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.12 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.68 (n/a)</td><td>0.17 (n/a)</td><td>193.10 (n/a)</td><td>158.30 (n/a)</td><td>154.30 (n/a)</td><td>118.40 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.05 (+3.52%)</td><td>0.82 (-2.43%)</td><td>0.77 (-0.61%)</td><td>0.62 (-17.78%)</td><td>0.16 <b>(+44.88%)</b></td><td>213.70 <b>(+21.63%)</b></td><td>167.08 (+4.40%)</td><td>172.10 (+0.64%)</td><td>125.30 (-3.47%)</td><td>33.04 <b>(+68.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.11 (n/a)</td><td>175.70 (n/a)</td><td>160.04 (n/a)</td><td>171.00 (n/a)</td><td>129.80 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.92 (-7.76%)</td><td>0.78 (+6.00%)</td><td>0.75 (+11.00%)</td><td>0.69 <b>(+22.68%)</b></td><td>0.10 <b>(-41.97%)</b></td><td>192.50 (-18.50%)</td><td>171.04 (-8.08%)</td><td>175.70 (-9.94%)</td><td>143.30 (+8.40%)</td><td>20.23 <b>(-47.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.00 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.56 (n/a)</td><td>0.17 (n/a)</td><td>236.20 (n/a)</td><td>186.08 (n/a)</td><td>195.10 (n/a)</td><td>132.20 (n/a)</td><td>38.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.07 <b>(+21.84%)</b></td><td>0.84 (+8.53%)</td><td>0.80 (+4.70%)</td><td>0.68 (-3.63%)</td><td>0.17 <b>(+154.75%)</b></td><td>195.60 (+3.77%)</td><td>163.04 (-5.46%)</td><td>164.70 (-4.52%)</td><td>123.80 (-17.90%)</td><td>31.39 <b>(+122.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.88 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.07 (n/a)</td><td>188.50 (n/a)</td><td>172.46 (n/a)</td><td>172.50 (n/a)</td><td>150.80 (n/a)</td><td>14.08 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.03 (-6.84%)</td><td>0.86 (-2.92%)</td><td>0.82 (-6.71%)</td><td>0.69 (-1.77%)</td><td>0.16 (-3.96%)</td><td>191.30 (+1.81%)</td><td>157.10 (+2.95%)</td><td>161.80 (+7.15%)</td><td>127.70 (+7.40%)</td><td>28.12 (+1.54%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.11 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>187.90 (n/a)</td><td>152.60 (n/a)</td><td>151.00 (n/a)</td><td>118.90 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (-16.16%)</td><td>0.03 (-13.98%)</td><td>0.03 (-17.36%)</td><td>0.02 (-12.74%)</td><td>0.00 <b>(-29.20%)</b></td><td>188.30 (+14.61%)</td><td>164.46 (+15.64%)</td><td>162.90 <b>(+21.03%)</b></td><td>146.00 (+19.28%)</td><td>18.81 (-6.41%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>164.30 (n/a)</td><td>142.22 (n/a)</td><td>134.60 (n/a)</td><td>122.40 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (-18.42%)</td><td>0.02 <b>(-20.75%)</b></td><td>0.02 <b>(-21.07%)</b></td><td>0.02 <b>(-22.42%)</b></td><td>0.00 (-14.88%)</td><td>237.50 <b>(+28.87%)</b></td><td>201.68 <b>(+26.46%)</b></td><td>193.60 <b>(+26.70%)</b></td><td>159.90 <b>(+22.62%)</b></td><td>31.41 <b>(+31.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.30 (n/a)</td><td>159.48 (n/a)</td><td>152.80 (n/a)</td><td>130.40 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.00 (+4.65%)</td><td>0.00 (+1.91%)</td><td>0.00 (+0.00%)</td><td>0.00 (+5.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>977.38 (-5.71%)</td><td>956.76 (-2.14%)</td><td>967.28 (+0.02%)</td><td>903.46 (-4.85%)</td><td>30.12 (-11.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1036.62 (n/a)</td><td>977.71 (n/a)</td><td>967.06 (n/a)</td><td>949.52 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.01 (+0.00%)</td><td>0.01 (-0.50%)</td><td>0.01 (+1.25%)</td><td>0.01 (-7.50%)</td><td>0.00 <b>(+111.39%)</b></td><td>1110.98 (+8.27%)</td><td>1021.97 (+0.85%)</td><td>1015.43 (-0.56%)</td><td>971.17 (-0.72%)</td><td>53.06 <b>(+168.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1026.15 (n/a)</td><td>1013.33 (n/a)</td><td>1021.13 (n/a)</td><td>978.24 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.99 (-0.96%)</td><td>0.96 (-0.16%)</td><td>0.96 (-0.60%)</td><td>0.95 (+1.72%)</td><td>0.01 <b>(-49.07%)</b></td><td>2199.40 (-1.68%)</td><td>2175.84 (+0.12%)</td><td>2191.39 (+0.61%)</td><td>2125.03 (+0.98%)</td><td>30.69 <b>(-49.53%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.00 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.03 (n/a)</td><td>2237.09 (n/a)</td><td>2173.28 (n/a)</td><td>2178.12 (n/a)</td><td>2104.50 (n/a)</td><td>60.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.02 (-7.47%)</td><td>2.72 (-2.74%)</td><td>2.73 (+3.74%)</td><td>2.29 (-7.28%)</td><td>0.28 <b>(-21.95%)</b></td><td>228.50 (+7.88%)</td><td>194.62 (+2.45%)</td><td>192.30 (-3.61%)</td><td>173.50 (+8.03%)</td><td>21.07 (-8.01%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.27 (n/a)</td><td>2.79 (n/a)</td><td>2.63 (n/a)</td><td>2.48 (n/a)</td><td>0.35 (n/a)</td><td>211.80 (n/a)</td><td>189.96 (n/a)</td><td>199.50 (n/a)</td><td>160.60 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.41 (-6.20%)</td><td>4.55 (-5.66%)</td><td>4.38 (-9.25%)</td><td>4.06 (+8.04%)</td><td>0.51 <b>(-30.06%)</b></td><td>258.10 (-7.42%)</td><td>232.40 (+4.91%)</td><td>239.20 (+10.23%)</td><td>193.60 (+6.61%)</td><td>23.90 <b>(-33.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>5.77 (n/a)</td><td>4.83 (n/a)</td><td>4.83 (n/a)</td><td>3.76 (n/a)</td><td>0.73 (n/a)</td><td>278.80 (n/a)</td><td>221.52 (n/a)</td><td>217.00 (n/a)</td><td>181.60 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.06 (-11.48%)</td><td>2.80 (-10.80%)</td><td>2.83 (-13.76%)</td><td>2.49 (-10.35%)</td><td>0.23 <b>(-25.75%)</b></td><td>210.60 (+11.55%)</td><td>188.40 (+11.84%)</td><td>185.20 (+15.97%)</td><td>171.60 (+12.97%)</td><td>15.59 (-7.18%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.45 (n/a)</td><td>3.14 (n/a)</td><td>3.28 (n/a)</td><td>2.78 (n/a)</td><td>0.30 (n/a)</td><td>188.80 (n/a)</td><td>168.46 (n/a)</td><td>159.70 (n/a)</td><td>151.90 (n/a)</td><td>16.79 (n/a)</td>
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
