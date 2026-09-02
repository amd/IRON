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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (+8.13%)</td><td>0.08 (+6.26%)</td><td>0.09 <b>(+29.25%)</b></td><td>0.05 (-17.99%)</td><td>0.02 <b>(+87.68%)</b></td><td>240.10 <b>(+21.94%)</b></td><td>168.78 (-0.08%)</td><td>135.70 <b>(-22.63%)</b></td><td>119.50 (-7.51%)</td><td>55.15 <b>(+123.01%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>168.92 (n/a)</td><td>175.40 (n/a)</td><td>129.20 (n/a)</td><td>24.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (+4.72%)</td><td>0.08 (-1.04%)</td><td>0.08 (+1.56%)</td><td>0.06 (-7.63%)</td><td>0.02 (+11.10%)</td><td>211.70 (+8.23%)</td><td>165.66 (+1.72%)</td><td>151.30 (-1.56%)</td><td>125.40 (-4.49%)</td><td>34.63 (+13.14%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>162.86 (n/a)</td><td>153.70 (n/a)</td><td>131.30 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 <b>(+36.58%)</b></td><td>0.08 <b>(+29.43%)</b></td><td>0.08 <b>(+22.84%)</b></td><td>0.07 <b>(+30.52%)</b></td><td>0.01 <b>(+50.52%)</b></td><td>172.10 <b>(-23.41%)</b></td><td>151.24 <b>(-22.56%)</b></td><td>155.30 (-18.61%)</td><td>126.60 <b>(-26.74%)</b></td><td>17.39 (-16.66%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>195.30 (n/a)</td><td>190.80 (n/a)</td><td>172.80 (n/a)</td><td>20.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.09 (+12.98%)</td><td>0.07 (+15.36%)</td><td>0.07 (+13.99%)</td><td>0.06 (-2.95%)</td><td>0.02 <b>(+59.63%)</b></td><td>222.70 (+3.05%)</td><td>173.92 (-11.58%)</td><td>178.40 (-12.29%)</td><td>135.30 (-11.51%)</td><td>36.47 <b>(+45.50%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>196.70 (n/a)</td><td>203.40 (n/a)</td><td>152.90 (n/a)</td><td>25.06 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (+8.80%)</td><td>0.03 (+19.37%)</td><td>0.03 (+2.70%)</td><td>0.03 <b>(+106.01%)</b></td><td>0.01 <b>(-46.40%)</b></td><td>180.10 <b>(-51.47%)</b></td><td>160.40 <b>(-25.03%)</b></td><td>167.20 (-2.68%)</td><td>126.10 (-8.09%)</td><td>22.70 <b>(-76.29%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>371.10 (n/a)</td><td>213.94 (n/a)</td><td>171.80 (n/a)</td><td>137.20 (n/a)</td><td>95.75 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (+8.81%)</td><td>0.03 (-0.87%)</td><td>0.03 (+9.29%)</td><td>0.02 <b>(-21.01%)</b></td><td>0.01 <b>(+83.70%)</b></td><td>242.30 <b>(+26.59%)</b></td><td>182.22 (+3.19%)</td><td>170.50 (-8.48%)</td><td>143.10 (-8.09%)</td><td>37.30 <b>(+118.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.40 (n/a)</td><td>176.58 (n/a)</td><td>186.30 (n/a)</td><td>155.70 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (+9.09%)</td><td>0.03 (+5.73%)</td><td>0.03 (+11.13%)</td><td>0.03 (-7.29%)</td><td>0.01 <b>(+57.45%)</b></td><td>204.50 (+7.86%)</td><td>159.62 (-3.65%)</td><td>154.80 (-10.00%)</td><td>124.20 (-8.34%)</td><td>31.90 <b>(+58.48%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.60 (n/a)</td><td>165.66 (n/a)</td><td>172.00 (n/a)</td><td>135.50 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 <b>(+38.29%)</b></td><td>0.03 (+17.71%)</td><td>0.03 (+13.05%)</td><td>0.03 <b>(+22.63%)</b></td><td>0.01 <b>(+65.34%)</b></td><td>181.30 (-18.44%)</td><td>159.32 (-14.13%)</td><td>171.70 (-11.54%)</td><td>113.60 <b>(-27.69%)</b></td><td>26.86 (-2.42%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.30 (n/a)</td><td>185.54 (n/a)</td><td>194.10 (n/a)</td><td>157.10 (n/a)</td><td>27.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 <b>(-35.74%)</b></td><td>0.02 <b>(-28.25%)</b></td><td>0.02 <b>(-21.00%)</b></td><td>0.01 <b>(-42.48%)</b></td><td>0.01 <b>(-21.84%)</b></td><td>354.00 <b>(+73.87%)</b></td><td>239.18 <b>(+42.28%)</b></td><td>217.00 <b>(+26.60%)</b></td><td>191.30 <b>(+55.66%)</b></td><td>66.70 <b>(+121.03%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>168.10 (n/a)</td><td>171.40 (n/a)</td><td>122.90 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (-13.15%)</td><td>0.03 (-3.41%)</td><td>0.03 (-1.53%)</td><td>0.02 (-7.15%)</td><td>0.00 <b>(-26.33%)</b></td><td>241.00 (+7.69%)</td><td>185.74 (+2.46%)</td><td>179.90 (+1.58%)</td><td>149.80 (+15.14%)</td><td>33.97 (-5.70%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>181.28 (n/a)</td><td>177.10 (n/a)</td><td>130.10 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 <b>(-20.66%)</b></td><td>0.02 (-11.43%)</td><td>0.03 (+0.77%)</td><td>0.02 <b>(-23.62%)</b></td><td>0.01 <b>(-25.21%)</b></td><td>281.80 <b>(+30.95%)</b></td><td>217.62 (+12.66%)</td><td>205.90 (-0.77%)</td><td>162.30 <b>(+26.11%)</b></td><td>46.12 <b>(+27.40%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>193.16 (n/a)</td><td>207.50 (n/a)</td><td>128.70 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 <b>(-33.77%)</b></td><td>0.03 (-5.96%)</td><td>0.03 <b>(+20.53%)</b></td><td>0.02 (-15.48%)</td><td>0.00 <b>(-56.37%)</b></td><td>283.10 (+18.30%)</td><td>213.72 (+1.42%)</td><td>193.40 (-17.03%)</td><td>179.40 <b>(+51.01%)</b></td><td>41.77 (-19.26%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.30 (n/a)</td><td>210.72 (n/a)</td><td>233.10 (n/a)</td><td>118.80 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.80 (n/a)</td><td>154.84 (n/a)</td><td>150.30 (n/a)</td><td>119.20 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>173.64 (n/a)</td><td>176.80 (n/a)</td><td>142.60 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>197.70 (n/a)</td><td>170.86 (n/a)</td><td>185.70 (n/a)</td><td>112.60 (n/a)</td><td>35.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>362.80 (n/a)</td><td>195.76 (n/a)</td><td>152.60 (n/a)</td><td>150.30 (n/a)</td><td>93.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>194.80 (n/a)</td><td>153.70 (n/a)</td><td>156.80 (n/a)</td><td>105.50 (n/a)</td><td>32.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>269.20 (n/a)</td><td>182.04 (n/a)</td><td>182.10 (n/a)</td><td>117.10 (n/a)</td><td>55.49 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>205.84 (n/a)</td><td>228.10 (n/a)</td><td>150.30 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>353.90 (n/a)</td><td>223.90 (n/a)</td><td>196.50 (n/a)</td><td>168.30 (n/a)</td><td>76.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>157.74 (n/a)</td><td>139.20 (n/a)</td><td>122.40 (n/a)</td><td>36.39 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>150.12 (n/a)</td><td>142.50 (n/a)</td><td>120.60 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>179.52 (n/a)</td><td>190.40 (n/a)</td><td>140.60 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>185.56 (n/a)</td><td>197.20 (n/a)</td><td>137.80 (n/a)</td><td>27.56 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>180.78 (n/a)</td><td>168.90 (n/a)</td><td>161.30 (n/a)</td><td>20.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>176.32 (n/a)</td><td>186.30 (n/a)</td><td>147.00 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>171.72 (n/a)</td><td>175.10 (n/a)</td><td>141.60 (n/a)</td><td>22.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>374.20 (n/a)</td><td>223.52 (n/a)</td><td>204.80 (n/a)</td><td>153.50 (n/a)</td><td>87.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.27 (-10.87%)</td><td>4.17 (-3.62%)</td><td>4.16 (-1.37%)</td><td>4.02 (-1.26%)</td><td>0.10 <b>(-66.14%)</b></td><td>2338.70 (+1.28%)</td><td>2258.22 (+3.45%)</td><td>2261.20 (+1.39%)</td><td>2203.80 (+12.20%)</td><td>53.42 <b>(-61.39%)</b></td><td>1678.66 (-10.87%)</td><td>1638.92 (-3.62%)</td><td>1636.05 (-1.37%)</td><td>1581.84 (-1.26%)</td><td>38.36 <b>(-66.14%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>4.79 (n/a)</td><td>4.32 (n/a)</td><td>4.22 (n/a)</td><td>4.07 (n/a)</td><td>0.29 (n/a)</td><td>2309.20 (n/a)</td><td>2182.96 (n/a)</td><td>2230.30 (n/a)</td><td>1964.20 (n/a)</td><td>138.35 (n/a)</td><td>1883.36 (n/a)</td><td>1700.40 (n/a)</td><td>1658.70 (n/a)</td><td>1602.04 (n/a)</td><td>113.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.32 (-2.06%)</td><td>1.00 (-9.62%)</td><td>0.98 (-4.93%)</td><td>0.69 <b>(-32.87%)</b></td><td>0.24 <b>(+74.95%)</b></td><td>322.60 <b>(+48.94%)</b></td><td>232.40 (+15.02%)</td><td>225.30 (+5.18%)</td><td>167.70 (+2.07%)</td><td>59.61 <b>(+168.54%)</b></td><td>56.27 (-2.06%)</td><td>42.68 (-9.62%)</td><td>41.88 (-4.93%)</td><td>29.25 <b>(-32.87%)</b></td><td>10.34 <b>(+74.95%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.35 (n/a)</td><td>1.11 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.14 (n/a)</td><td>216.60 (n/a)</td><td>202.06 (n/a)</td><td>214.20 (n/a)</td><td>164.30 (n/a)</td><td>22.20 (n/a)</td><td>57.45 (n/a)</td><td>47.22 (n/a)</td><td>44.05 (n/a)</td><td>43.58 (n/a)</td><td>5.91 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.32 (+2.66%)</td><td>0.99 (-9.23%)</td><td>1.07 (-2.15%)</td><td>0.67 (-13.28%)</td><td>0.28 <b>(+32.59%)</b></td><td>332.60 (+15.33%)</td><td>239.86 (+14.09%)</td><td>206.40 (+2.18%)</td><td>167.50 (-2.62%)</td><td>72.54 <b>(+53.36%)</b></td><td>56.32 (+2.66%)</td><td>42.20 (-9.23%)</td><td>45.72 (-2.15%)</td><td>28.38 (-13.28%)</td><td>11.95 <b>(+32.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.29 (n/a)</td><td>1.09 (n/a)</td><td>1.10 (n/a)</td><td>0.77 (n/a)</td><td>0.21 (n/a)</td><td>288.40 (n/a)</td><td>210.24 (n/a)</td><td>202.00 (n/a)</td><td>172.00 (n/a)</td><td>47.30 (n/a)</td><td>54.87 (n/a)</td><td>46.49 (n/a)</td><td>46.73 (n/a)</td><td>32.72 (n/a)</td><td>9.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.52 (+0.01%)</td><td>0.52 (+0.11%)</td><td>0.52 (+0.04%)</td><td>0.52 (+0.24%)</td><td>0.00 <b>(-50.60%)</b></td><td>48556.50 (-0.24%)</td><td>48474.60 (-0.11%)</td><td>48455.20 (-0.04%)</td><td>48450.50 (-0.01%)</td><td>45.89 <b>(-50.69%)</b></td><td>354.59 (+0.01%)</td><td>354.41 (+0.11%)</td><td>354.55 (+0.04%)</td><td>353.81 (+0.24%)</td><td>0.33 <b>(-50.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48672.10 (n/a)</td><td>48529.98 (n/a)</td><td>48474.50 (n/a)</td><td>48454.00 (n/a)</td><td>93.07 (n/a)</td><td>354.56 (n/a)</td><td>354.01 (n/a)</td><td>354.41 (n/a)</td><td>352.97 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.89 (-1.55%)</td><td>0.89 (-0.90%)</td><td>0.89 (-1.13%)</td><td>0.88 (-0.64%)</td><td>0.00 <b>(-54.86%)</b></td><td>28461.90 (+0.64%)</td><td>28271.80 (+0.91%)</td><td>28250.00 (+1.14%)</td><td>28184.40 (+1.57%)</td><td>109.97 <b>(-53.89%)</b></td><td>609.55 (-1.55%)</td><td>607.68 (-0.90%)</td><td>608.14 (-1.13%)</td><td>603.61 (-0.64%)</td><td>2.35 <b>(-54.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28280.30 (n/a)</td><td>28017.84 (n/a)</td><td>27931.50 (n/a)</td><td>27747.40 (n/a)</td><td>238.53 (n/a)</td><td>619.15 (n/a)</td><td>613.21 (n/a)</td><td>615.07 (n/a)</td><td>607.48 (n/a)</td><td>5.21 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.34 (-3.55%)</td><td>3.20 (-2.36%)</td><td>3.19 (-4.38%)</td><td>3.14 (+2.62%)</td><td>0.08 <b>(-52.27%)</b></td><td>8003.40 (-2.56%)</td><td>7859.10 (+2.26%)</td><td>7896.60 (+4.58%)</td><td>7540.80 (+3.68%)</td><td>184.48 <b>(-52.09%)</b></td><td>2278.26 (-3.55%)</td><td>2186.98 (-2.36%)</td><td>2175.61 (-4.38%)</td><td>2146.58 (+2.62%)</td><td>52.73 <b>(-52.27%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.46 (n/a)</td><td>3.28 (n/a)</td><td>3.33 (n/a)</td><td>3.06 (n/a)</td><td>0.16 (n/a)</td><td>8213.40 (n/a)</td><td>7685.64 (n/a)</td><td>7550.90 (n/a)</td><td>7273.00 (n/a)</td><td>385.03 (n/a)</td><td>2362.13 (n/a)</td><td>2239.74 (n/a)</td><td>2275.20 (n/a)</td><td>2091.69 (n/a)</td><td>110.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.29 (+2.69%)</td><td>3.66 (-0.97%)</td><td>3.63 (-6.25%)</td><td>2.91 (-1.55%)</td><td>0.50 (+7.59%)</td><td>2770.00 (+1.58%)</td><td>2241.06 (+1.18%)</td><td>2220.90 (+6.67%)</td><td>1879.40 (-2.62%)</td><td>329.16 (+6.28%)</td><td>1124.79 (+2.69%)</td><td>958.55 (-0.97%)</td><td>951.83 (-6.25%)</td><td>763.14 (-1.55%)</td><td>131.21 (+7.59%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>4.18 (n/a)</td><td>3.69 (n/a)</td><td>3.87 (n/a)</td><td>2.96 (n/a)</td><td>0.47 (n/a)</td><td>2727.00 (n/a)</td><td>2214.94 (n/a)</td><td>2082.00 (n/a)</td><td>1929.90 (n/a)</td><td>309.71 (n/a)</td><td>1095.38 (n/a)</td><td>967.97 (n/a)</td><td>1015.32 (n/a)</td><td>775.17 (n/a)</td><td>121.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.51 (+0.19%)</td><td>0.39 (-13.95%)</td><td>0.35 <b>(-28.89%)</b></td><td>0.28 (+2.38%)</td><td>0.10 (+6.36%)</td><td>4377.10 (-2.33%)</td><td>3373.38 (+16.44%)</td><td>3545.60 <b>(+40.62%)</b></td><td>2460.70 (-0.19%)</td><td>868.57 (-1.98%)</td><td>27.27 (+0.19%)</td><td>21.05 (-13.95%)</td><td>18.93 <b>(-28.89%)</b></td><td>15.33 (+2.38%)</td><td>5.65 (+6.36%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.51 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>4481.30 (n/a)</td><td>2897.20 (n/a)</td><td>2521.40 (n/a)</td><td>2465.40 (n/a)</td><td>886.11 (n/a)</td><td>27.22 (n/a)</td><td>24.46 (n/a)</td><td>26.62 (n/a)</td><td>14.98 (n/a)</td><td>5.32 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.93 (-5.75%)</td><td>4.06 (-13.72%)</td><td>3.60 <b>(-24.85%)</b></td><td>3.41 (-8.23%)</td><td>0.74 <b>(+26.73%)</b></td><td>1951.30 (+8.97%)</td><td>1681.74 (+17.18%)</td><td>1849.10 <b>(+33.08%)</b></td><td>1348.70 (+6.10%)</td><td>287.59 <b>(+40.55%)</b></td><td>1523.81 (-5.75%)</td><td>1253.17 (-13.72%)</td><td>1111.49 <b>(-24.85%)</b></td><td>1053.25 (-8.23%)</td><td>227.49 <b>(+26.73%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>5.23 (n/a)</td><td>4.70 (n/a)</td><td>4.79 (n/a)</td><td>3.71 (n/a)</td><td>0.58 (n/a)</td><td>1790.60 (n/a)</td><td>1435.16 (n/a)</td><td>1389.50 (n/a)</td><td>1271.10 (n/a)</td><td>204.62 (n/a)</td><td>1616.82 (n/a)</td><td>1452.44 (n/a)</td><td>1479.11 (n/a)</td><td>1147.76 (n/a)</td><td>179.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>13.09 (n/a)</td><td>12.33 (n/a)</td><td>12.67 (n/a)</td><td>10.86 (n/a)</td><td>0.89 (n/a)</td><td>13.08 (n/a)</td><td>12.32 (n/a)</td><td>12.66 (n/a)</td><td>10.85 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>23.78 (-3.40%)</td><td>21.69 (-8.45%)</td><td>22.34 (-6.20%)</td><td>17.33 <b>(-20.69%)</b></td><td>2.52 <b>(+130.37%)</b></td><td>23.76 (-3.40%)</td><td>21.68 (-8.45%)</td><td>22.33 (-6.20%)</td><td>17.32 <b>(-20.69%)</b></td><td>2.52 <b>(+130.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>24.62 (n/a)</td><td>23.69 (n/a)</td><td>23.82 (n/a)</td><td>21.85 (n/a)</td><td>1.09 (n/a)</td><td>24.60 (n/a)</td><td>23.68 (n/a)</td><td>23.80 (n/a)</td><td>21.84 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>40.93 (+3.10%)</td><td>40.30 (+5.60%)</td><td>40.51 (+4.65%)</td><td>39.33 (+12.50%)</td><td>0.64 <b>(-65.65%)</b></td><td>40.91 (+3.10%)</td><td>40.27 (+5.60%)</td><td>40.49 (+4.65%)</td><td>39.31 (+12.50%)</td><td>0.64 <b>(-65.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>39.70 (n/a)</td><td>38.16 (n/a)</td><td>38.71 (n/a)</td><td>34.96 (n/a)</td><td>1.87 (n/a)</td><td>39.68 (n/a)</td><td>38.14 (n/a)</td><td>38.69 (n/a)</td><td>34.94 (n/a)</td><td>1.87 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>42.45 (-7.03%)</td><td>41.00 (-4.46%)</td><td>42.37 (-3.58%)</td><td>38.55 (-2.08%)</td><td>1.95 <b>(-31.47%)</b></td><td>42.42 (-7.03%)</td><td>40.97 (-4.46%)</td><td>42.35 (-3.58%)</td><td>38.53 (-2.08%)</td><td>1.95 <b>(-31.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>45.66 (n/a)</td><td>42.91 (n/a)</td><td>43.95 (n/a)</td><td>39.37 (n/a)</td><td>2.85 (n/a)</td><td>45.63 (n/a)</td><td>42.89 (n/a)</td><td>43.92 (n/a)</td><td>39.35 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>13.19 (n/a)</td><td>12.55 (n/a)</td><td>12.50 (n/a)</td><td>12.09 (n/a)</td><td>0.41 (n/a)</td><td>13.19 (n/a)</td><td>12.54 (n/a)</td><td>12.49 (n/a)</td><td>12.08 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>24.35 (-1.93%)</td><td>23.49 (+2.26%)</td><td>23.70 (-2.00%)</td><td>22.51 <b>(+24.80%)</b></td><td>0.78 <b>(-72.28%)</b></td><td>24.33 (-1.93%)</td><td>23.47 (+2.26%)</td><td>23.68 (-2.00%)</td><td>22.50 <b>(+24.80%)</b></td><td>0.78 <b>(-72.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>24.83 (n/a)</td><td>22.97 (n/a)</td><td>24.18 (n/a)</td><td>18.04 (n/a)</td><td>2.81 (n/a)</td><td>24.81 (n/a)</td><td>22.96 (n/a)</td><td>24.17 (n/a)</td><td>18.03 (n/a)</td><td>2.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>43.39 (+2.72%)</td><td>41.36 (+4.96%)</td><td>42.04 (+6.53%)</td><td>36.84 (-1.61%)</td><td>2.64 <b>(+31.12%)</b></td><td>43.37 (+2.72%)</td><td>41.33 (+4.96%)</td><td>42.02 (+6.53%)</td><td>36.81 (-1.61%)</td><td>2.64 <b>(+31.12%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>42.24 (n/a)</td><td>39.41 (n/a)</td><td>39.47 (n/a)</td><td>37.44 (n/a)</td><td>2.02 (n/a)</td><td>42.22 (n/a)</td><td>39.38 (n/a)</td><td>39.44 (n/a)</td><td>37.42 (n/a)</td><td>2.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>44.37 (-0.66%)</td><td>42.96 (+0.67%)</td><td>43.03 (-0.49%)</td><td>41.76 (+8.16%)</td><td>1.14 <b>(-51.30%)</b></td><td>44.34 (-0.66%)</td><td>42.93 (+0.67%)</td><td>43.01 (-0.49%)</td><td>41.73 (+8.16%)</td><td>1.14 <b>(-51.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>44.67 (n/a)</td><td>42.67 (n/a)</td><td>43.25 (n/a)</td><td>38.61 (n/a)</td><td>2.35 (n/a)</td><td>44.64 (n/a)</td><td>42.64 (n/a)</td><td>43.22 (n/a)</td><td>38.59 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>9.23 (+1.64%)</td><td>8.63 (-0.20%)</td><td>8.70 (-0.94%)</td><td>7.43 (-8.95%)</td><td>0.72 <b>(+60.00%)</b></td><td>9.21 (+1.64%)</td><td>8.62 (-0.20%)</td><td>8.68 (-0.94%)</td><td>7.41 (-8.95%)</td><td>0.72 <b>(+60.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>9.08 (n/a)</td><td>8.65 (n/a)</td><td>8.78 (n/a)</td><td>8.16 (n/a)</td><td>0.45 (n/a)</td><td>9.06 (n/a)</td><td>8.63 (n/a)</td><td>8.76 (n/a)</td><td>8.14 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.08 (+8.67%)</td><td>0.92 (+3.10%)</td><td>0.92 (-0.61%)</td><td>0.80 (+4.29%)</td><td>0.11 <b>(+28.59%)</b></td><td>1.07 (+8.67%)</td><td>0.91 (+3.10%)</td><td>0.90 (-0.61%)</td><td>0.79 (+4.29%)</td><td>0.11 <b>(+28.59%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.00 (n/a)</td><td>0.89 (n/a)</td><td>0.92 (n/a)</td><td>0.77 (n/a)</td><td>0.09 (n/a)</td><td>0.98 (n/a)</td><td>0.88 (n/a)</td><td>0.91 (n/a)</td><td>0.75 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.38 (+1.30%)</td><td>1.17 (-0.76%)</td><td>1.10 (-3.56%)</td><td>1.00 (-3.47%)</td><td>0.15 <b>(+22.62%)</b></td><td>1.36 (+1.30%)</td><td>1.15 (-0.76%)</td><td>1.09 (-3.56%)</td><td>0.99 (-3.47%)</td><td>0.15 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.36 (n/a)</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.04 (n/a)</td><td>0.13 (n/a)</td><td>1.35 (n/a)</td><td>1.16 (n/a)</td><td>1.13 (n/a)</td><td>1.02 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>18.81 (+5.46%)</td><td>17.49 (+12.22%)</td><td>17.11 (+16.24%)</td><td>16.51 (+14.43%)</td><td>0.99 <b>(-31.20%)</b></td><td>18.59 (+5.46%)</td><td>17.29 (+12.22%)</td><td>16.92 (+16.24%)</td><td>16.32 (+14.43%)</td><td>0.98 <b>(-31.20%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>17.83 (n/a)</td><td>15.59 (n/a)</td><td>14.72 (n/a)</td><td>14.43 (n/a)</td><td>1.44 (n/a)</td><td>17.63 (n/a)</td><td>15.40 (n/a)</td><td>14.55 (n/a)</td><td>14.26 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>14.03 (+4.13%)</td><td>13.45 (+1.99%)</td><td>13.63 (+2.56%)</td><td>12.14 (-3.11%)</td><td>0.76 <b>(+100.78%)</b></td><td>13.78 (+4.13%)</td><td>13.21 (+1.99%)</td><td>13.39 (+2.56%)</td><td>11.93 (-3.11%)</td><td>0.74 <b>(+100.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>13.47 (n/a)</td><td>13.18 (n/a)</td><td>13.29 (n/a)</td><td>12.53 (n/a)</td><td>0.38 (n/a)</td><td>13.24 (n/a)</td><td>12.95 (n/a)</td><td>13.06 (n/a)</td><td>12.31 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>9.29 (+14.03%)</td><td>7.78 (+5.71%)</td><td>7.73 (+3.65%)</td><td>6.55 (+1.49%)</td><td>0.98 <b>(+54.30%)</b></td><td>9.13 (+14.03%)</td><td>7.65 (+5.71%)</td><td>7.59 (+3.65%)</td><td>6.44 (+1.49%)</td><td>0.96 <b>(+54.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>8.15 (n/a)</td><td>7.36 (n/a)</td><td>7.46 (n/a)</td><td>6.45 (n/a)</td><td>0.63 (n/a)</td><td>8.01 (n/a)</td><td>7.24 (n/a)</td><td>7.33 (n/a)</td><td>6.34 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>6.44 (+6.62%)</td><td>6.00 (+15.13%)</td><td>6.30 (+13.47%)</td><td>4.80 (+8.34%)</td><td>0.69 (-4.65%)</td><td>6.34 (+6.62%)</td><td>5.91 (+15.13%)</td><td>6.20 (+13.47%)</td><td>4.72 (+8.34%)</td><td>0.68 (-4.65%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>6.04 (n/a)</td><td>5.22 (n/a)</td><td>5.56 (n/a)</td><td>4.43 (n/a)</td><td>0.73 (n/a)</td><td>5.95 (n/a)</td><td>5.13 (n/a)</td><td>5.47 (n/a)</td><td>4.36 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>13.39 (n/a)</td><td>12.59 (n/a)</td><td>12.19 (n/a)</td><td>11.98 (n/a)</td><td>0.66 (n/a)</td><td>13.38 (n/a)</td><td>12.58 (n/a)</td><td>12.19 (n/a)</td><td>11.97 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>13.14 (n/a)</td><td>12.61 (n/a)</td><td>12.65 (n/a)</td><td>12.10 (n/a)</td><td>0.41 (n/a)</td><td>13.13 (n/a)</td><td>12.60 (n/a)</td><td>12.64 (n/a)</td><td>12.10 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>169.96 (n/a)</td><td>176.50 (n/a)</td><td>128.90 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.50 (n/a)</td><td>152.68 (n/a)</td><td>151.40 (n/a)</td><td>118.30 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.50 (n/a)</td><td>152.80 (n/a)</td><td>156.80 (n/a)</td><td>122.00 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>161.84 (n/a)</td><td>147.00 (n/a)</td><td>135.30 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.90 (n/a)</td><td>184.28 (n/a)</td><td>180.20 (n/a)</td><td>167.60 (n/a)</td><td>13.46 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>216.00 (n/a)</td><td>173.38 (n/a)</td><td>190.10 (n/a)</td><td>99.50 (n/a)</td><td>45.26 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.30 (n/a)</td><td>210.32 (n/a)</td><td>187.10 (n/a)</td><td>175.20 (n/a)</td><td>53.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>207.76 (n/a)</td><td>203.60 (n/a)</td><td>161.10 (n/a)</td><td>34.97 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (+6.95%)</td><td>0.06 (+6.63%)</td><td>0.06 (+3.97%)</td><td>0.04 (+3.90%)</td><td>0.01 (+4.15%)</td><td>183.60 (-3.72%)</td><td>139.94 (-6.21%)</td><td>129.50 (-3.86%)</td><td>120.90 (-6.50%)</td><td>25.63 (-3.45%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>149.20 (n/a)</td><td>134.70 (n/a)</td><td>129.30 (n/a)</td><td>26.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (+4.16%)</td><td>0.05 (-16.07%)</td><td>0.05 <b>(-23.72%)</b></td><td>0.04 (-7.93%)</td><td>0.01 (+10.65%)</td><td>216.60 (+8.63%)</td><td>173.24 <b>(+20.27%)</b></td><td>174.10 <b>(+31.10%)</b></td><td>111.60 (-3.96%)</td><td>39.05 (+12.12%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>144.04 (n/a)</td><td>132.80 (n/a)</td><td>116.20 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (+9.33%)</td><td>0.06 (+11.24%)</td><td>0.06 (+9.51%)</td><td>0.04 (+14.52%)</td><td>0.01 (+17.41%)</td><td>187.20 (-12.69%)</td><td>152.08 (-9.91%)</td><td>148.50 (-8.67%)</td><td>122.30 (-8.53%)</td><td>27.01 (-7.48%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.40 (n/a)</td><td>168.80 (n/a)</td><td>162.60 (n/a)</td><td>133.70 (n/a)</td><td>29.20 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (-7.07%)</td><td>0.06 (+4.61%)</td><td>0.06 (+15.34%)</td><td>0.05 (+4.69%)</td><td>0.01 <b>(-36.78%)</b></td><td>181.70 (-4.47%)</td><td>145.94 (-6.76%)</td><td>146.60 (-13.31%)</td><td>123.70 (+7.57%)</td><td>22.59 <b>(-34.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>156.52 (n/a)</td><td>169.10 (n/a)</td><td>115.00 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 <b>(+23.82%)</b></td><td>0.06 (+14.10%)</td><td>0.06 <b>(+26.90%)</b></td><td>0.03 <b>(-26.20%)</b></td><td>0.02 <b>(+133.65%)</b></td><td>256.70 <b>(+35.53%)</b></td><td>156.12 (-5.36%)</td><td>128.90 <b>(-21.16%)</b></td><td>106.70 (-19.23%)</td><td>59.69 <b>(+168.37%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>164.96 (n/a)</td><td>163.50 (n/a)</td><td>132.10 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (+12.99%)</td><td>0.06 <b>(+31.78%)</b></td><td>0.06 <b>(+34.06%)</b></td><td>0.05 <b>(+35.35%)</b></td><td>0.01 (-0.24%)</td><td>175.50 <b>(-26.14%)</b></td><td>141.86 <b>(-25.21%)</b></td><td>136.70 <b>(-25.38%)</b></td><td>116.50 (-11.54%)</td><td>26.59 <b>(-35.60%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.60 (n/a)</td><td>189.68 (n/a)</td><td>183.20 (n/a)</td><td>131.70 (n/a)</td><td>41.29 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (-6.17%)</td><td>0.06 (+2.64%)</td><td>0.05 (-2.34%)</td><td>0.05 (+17.90%)</td><td>0.01 <b>(-39.13%)</b></td><td>164.40 (-15.17%)</td><td>147.88 (-4.51%)</td><td>151.30 (+2.37%)</td><td>123.70 (+6.64%)</td><td>16.36 <b>(-45.21%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>154.86 (n/a)</td><td>147.80 (n/a)</td><td>116.00 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+3.42%)</td><td>0.05 (+5.87%)</td><td>0.05 (+11.01%)</td><td>0.04 (+11.12%)</td><td>0.01 (-10.48%)</td><td>207.50 (-10.02%)</td><td>169.52 (-6.43%)</td><td>166.20 (-9.92%)</td><td>134.30 (-3.24%)</td><td>28.81 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>181.16 (n/a)</td><td>184.50 (n/a)</td><td>138.80 (n/a)</td><td>36.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (-8.02%)</td><td>0.05 (+8.58%)</td><td>0.05 <b>(+21.05%)</b></td><td>0.04 <b>(+31.38%)</b></td><td>0.00 <b>(-56.54%)</b></td><td>190.80 <b>(-23.89%)</b></td><td>161.48 (-11.35%)</td><td>153.10 (-17.38%)</td><td>151.30 (+8.69%)</td><td>16.72 <b>(-62.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.70 (n/a)</td><td>182.16 (n/a)</td><td>185.30 (n/a)</td><td>139.20 (n/a)</td><td>45.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (+2.51%)</td><td>0.04 (-1.66%)</td><td>0.04 (-11.95%)</td><td>0.03 (+2.58%)</td><td>0.01 (-18.58%)</td><td>261.60 (-2.53%)</td><td>217.84 (+0.67%)</td><td>221.90 (+13.56%)</td><td>176.50 (-2.43%)</td><td>31.54 <b>(-22.98%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.40 (n/a)</td><td>216.40 (n/a)</td><td>195.40 (n/a)</td><td>180.90 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+7.20%)</td><td>0.05 (+0.85%)</td><td>0.06 (+10.04%)</td><td>0.04 (-11.18%)</td><td>0.01 <b>(+64.32%)</b></td><td>193.20 (+12.59%)</td><td>156.86 (+0.54%)</td><td>148.40 (-9.12%)</td><td>127.40 (-6.73%)</td><td>26.02 <b>(+75.15%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>171.60 (n/a)</td><td>156.02 (n/a)</td><td>163.30 (n/a)</td><td>136.60 (n/a)</td><td>14.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+13.36%)</td><td>0.04 (+1.23%)</td><td>0.04 (-3.01%)</td><td>0.03 (-5.52%)</td><td>0.01 <b>(+53.94%)</b></td><td>234.40 (+5.82%)</td><td>199.72 (+0.76%)</td><td>221.20 (+3.08%)</td><td>139.60 (-11.76%)</td><td>39.38 <b>(+41.87%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>198.22 (n/a)</td><td>214.60 (n/a)</td><td>158.20 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+8.16%)</td><td>0.05 (-8.29%)</td><td>0.04 (-13.24%)</td><td>0.03 <b>(-31.04%)</b></td><td>0.01 <b>(+448.59%)</b></td><td>249.10 <b>(+44.99%)</b></td><td>186.40 (+13.94%)</td><td>187.30 (+15.26%)</td><td>143.70 (-7.53%)</td><td>44.73 <b>(+600.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.80 (n/a)</td><td>163.60 (n/a)</td><td>162.50 (n/a)</td><td>155.40 (n/a)</td><td>6.38 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (-6.94%)</td><td>0.05 (+0.92%)</td><td>0.06 (+10.84%)</td><td>0.04 (+0.85%)</td><td>0.01 (-12.65%)</td><td>198.70 (-0.85%)</td><td>160.44 (-1.53%)</td><td>146.60 (-9.78%)</td><td>129.50 (+7.47%)</td><td>31.48 (-6.49%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>162.94 (n/a)</td><td>162.50 (n/a)</td><td>120.50 (n/a)</td><td>33.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+1.83%)</td><td>0.05 (+0.99%)</td><td>0.05 (-3.85%)</td><td>0.04 (-3.15%)</td><td>0.01 <b>(+30.43%)</b></td><td>191.50 (+3.29%)</td><td>162.92 (+0.31%)</td><td>178.10 (+3.97%)</td><td>128.00 (-1.84%)</td><td>31.26 <b>(+29.46%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>162.42 (n/a)</td><td>171.30 (n/a)</td><td>130.40 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 <b>(+31.34%)</b></td><td>0.05 (+5.12%)</td><td>0.04 <b>(-20.45%)</b></td><td>0.04 (-9.23%)</td><td>0.02 <b>(+199.09%)</b></td><td>212.80 (+10.20%)</td><td>167.64 (+1.62%)</td><td>195.10 <b>(+25.71%)</b></td><td>112.90 <b>(-23.87%)</b></td><td>48.46 <b>(+146.86%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>164.96 (n/a)</td><td>155.20 (n/a)</td><td>148.30 (n/a)</td><td>19.63 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 <b>(+28.86%)</b></td><td>0.05 (+7.77%)</td><td>0.04 (-5.40%)</td><td>0.04 (-6.32%)</td><td>0.01 <b>(+152.29%)</b></td><td>220.70 (+6.77%)</td><td>176.12 (-4.03%)</td><td>189.30 (+5.70%)</td><td>126.00 <b>(-22.41%)</b></td><td>38.61 <b>(+105.30%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>183.52 (n/a)</td><td>179.10 (n/a)</td><td>162.40 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 <b>(+24.88%)</b></td><td>0.05 (+14.90%)</td><td>0.05 (-6.12%)</td><td>0.04 <b>(+24.23%)</b></td><td>0.01 <b>(+35.56%)</b></td><td>200.80 (-19.49%)</td><td>167.52 (-12.44%)</td><td>176.20 (+6.47%)</td><td>130.10 (-19.89%)</td><td>34.66 (-11.52%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.40 (n/a)</td><td>191.32 (n/a)</td><td>165.50 (n/a)</td><td>162.40 (n/a)</td><td>39.17 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.18 (+0.93%)</td><td>0.18 (+0.36%)</td><td>0.18 (+0.22%)</td><td>0.18 (+0.12%)</td><td>0.00 <b>(+371.09%)</b></td><td>47410.80 (-0.12%)</td><td>47253.18 (-0.36%)</td><td>47316.80 (-0.22%)</td><td>46932.30 (-0.92%)</td><td>190.67 <b>(+365.91%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47469.90 (n/a)</td><td>47422.38 (n/a)</td><td>47420.30 (n/a)</td><td>47369.50 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.24 <b>(+23.84%)</b></td><td>0.16 (-1.59%)</td><td>0.15 (-6.11%)</td><td>0.13 (-2.43%)</td><td>0.04 <b>(+82.30%)</b></td><td>185.80 (+2.48%)</td><td>158.98 (+4.41%)</td><td>168.00 (+6.46%)</td><td>103.60 (-19.25%)</td><td>32.23 <b>(+47.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.30 (n/a)</td><td>152.26 (n/a)</td><td>157.80 (n/a)</td><td>128.30 (n/a)</td><td>21.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.25 <b>(-20.17%)</b></td><td>0.23 (-13.82%)</td><td>0.24 (-5.57%)</td><td>0.22 (-8.54%)</td><td>0.01 <b>(-58.38%)</b></td><td>186.60 (+9.31%)</td><td>175.46 (+15.00%)</td><td>172.30 (+5.90%)</td><td>163.40 <b>(+25.21%)</b></td><td>10.56 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>170.70 (n/a)</td><td>152.58 (n/a)</td><td>162.70 (n/a)</td><td>130.50 (n/a)</td><td>18.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 <b>(+20.17%)</b></td><td>0.03 (-10.70%)</td><td>0.03 (-9.23%)</td><td>0.02 <b>(-48.34%)</b></td><td>0.01 <b>(+473.03%)</b></td><td>310.70 <b>(+93.58%)</b></td><td>184.22 <b>(+24.62%)</b></td><td>162.30 (+10.18%)</td><td>116.20 (-16.76%)</td><td>75.53 <b>(+858.42%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.50 (n/a)</td><td>147.82 (n/a)</td><td>147.30 (n/a)</td><td>139.60 (n/a)</td><td>7.88 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (-7.08%)</td><td>0.05 (-14.82%)</td><td>0.05 (-4.52%)</td><td>0.02 <b>(-50.01%)</b></td><td>0.01 <b>(+122.78%)</b></td><td>351.50 <b>(+100.06%)</b></td><td>201.86 <b>(+29.81%)</b></td><td>157.90 (+4.78%)</td><td>145.10 (+7.64%)</td><td>87.61 <b>(+366.92%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>155.50 (n/a)</td><td>150.70 (n/a)</td><td>134.80 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (-5.70%)</td><td>0.08 (-8.98%)</td><td>0.07 (-18.71%)</td><td>0.05 <b>(-23.12%)</b></td><td>0.02 (+15.66%)</td><td>242.40 <b>(+30.04%)</b></td><td>171.04 (+12.33%)</td><td>175.40 <b>(+23.00%)</b></td><td>126.50 (+6.04%)</td><td>45.83 <b>(+53.15%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>152.26 (n/a)</td><td>142.60 (n/a)</td><td>119.30 (n/a)</td><td>29.92 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 <b>(-34.32%)</b></td><td>0.05 (-16.49%)</td><td>0.04 (-18.73%)</td><td>0.04 <b>(+61.81%)</b></td><td>0.00 <b>(-79.23%)</b></td><td>189.20 <b>(-38.19%)</b></td><td>177.68 (+4.59%)</td><td>184.90 <b>(+23.02%)</b></td><td>152.90 <b>(+52.14%)</b></td><td>14.97 <b>(-81.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>306.10 (n/a)</td><td>169.88 (n/a)</td><td>150.30 (n/a)</td><td>100.50 (n/a)</td><td>80.53 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (-12.47%)</td><td>0.06 (+0.73%)</td><td>0.06 (+1.74%)</td><td>0.05 (+9.62%)</td><td>0.01 <b>(-51.03%)</b></td><td>191.70 (-8.80%)</td><td>170.38 (-2.56%)</td><td>174.20 (-1.69%)</td><td>155.50 (+14.25%)</td><td>15.09 <b>(-49.75%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>174.86 (n/a)</td><td>177.20 (n/a)</td><td>136.10 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.09 <b>(+36.11%)</b></td><td>0.06 (+10.63%)</td><td>0.06 (-0.65%)</td><td>0.04 (+5.86%)</td><td>0.02 <b>(+89.31%)</b></td><td>187.10 (-5.55%)</td><td>146.72 (-6.26%)</td><td>148.60 (+0.68%)</td><td>94.90 <b>(-26.49%)</b></td><td>38.01 <b>(+32.88%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>156.52 (n/a)</td><td>147.60 (n/a)</td><td>129.10 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (-1.08%)</td><td>0.07 (+16.84%)</td><td>0.08 <b>(+41.69%)</b></td><td>0.04 (-17.09%)</td><td>0.02 <b>(+20.99%)</b></td><td>258.60 <b>(+20.62%)</b></td><td>161.62 (-11.48%)</td><td>135.10 <b>(-29.41%)</b></td><td>122.60 (+1.07%)</td><td>56.92 <b>(+50.78%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>214.40 (n/a)</td><td>182.58 (n/a)</td><td>191.40 (n/a)</td><td>121.30 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (+4.37%)</td><td>0.05 (+6.40%)</td><td>0.05 (+17.58%)</td><td>0.04 (+13.73%)</td><td>0.01 (-19.42%)</td><td>188.70 (-12.03%)</td><td>159.36 (-8.16%)</td><td>159.60 (-14.97%)</td><td>118.60 (-4.12%)</td><td>29.32 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>173.52 (n/a)</td><td>187.70 (n/a)</td><td>123.70 (n/a)</td><td>42.42 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 <b>(-22.84%)</b></td><td>0.05 (-4.23%)</td><td>0.06 (+14.12%)</td><td>0.04 (+1.06%)</td><td>0.01 <b>(-45.39%)</b></td><td>205.40 (-1.06%)</td><td>177.76 (+2.29%)</td><td>162.60 (-12.39%)</td><td>155.70 <b>(+29.64%)</b></td><td>24.43 <b>(-25.65%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>173.78 (n/a)</td><td>185.60 (n/a)</td><td>120.10 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 <b>(+27.12%)</b></td><td>0.06 (+8.76%)</td><td>0.05 (-1.71%)</td><td>0.04 (-0.43%)</td><td>0.02 <b>(+81.70%)</b></td><td>192.30 (+0.42%)</td><td>150.66 (-4.93%)</td><td>154.00 (+1.72%)</td><td>97.50 <b>(-21.31%)</b></td><td>36.74 <b>(+40.44%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>158.48 (n/a)</td><td>151.40 (n/a)</td><td>123.90 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (-7.24%)</td><td>0.06 (-5.28%)</td><td>0.05 (-9.73%)</td><td>0.05 (+7.85%)</td><td>0.01 (-19.38%)</td><td>189.80 (-7.28%)</td><td>160.20 (+4.13%)</td><td>171.10 (+10.82%)</td><td>121.90 (+7.78%)</td><td>27.96 (-19.64%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>153.84 (n/a)</td><td>154.40 (n/a)</td><td>113.10 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 <b>(+27.05%)</b></td><td>0.05 (+7.16%)</td><td>0.05 (-3.77%)</td><td>0.05 <b>(+22.85%)</b></td><td>0.01 <b>(+31.70%)</b></td><td>182.00 (-18.60%)</td><td>165.26 (-6.57%)</td><td>172.10 (+3.93%)</td><td>128.70 <b>(-21.28%)</b></td><td>21.52 (-17.72%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>176.88 (n/a)</td><td>165.60 (n/a)</td><td>163.50 (n/a)</td><td>26.16 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (+1.45%)</td><td>0.05 (+13.94%)</td><td>0.05 (+19.72%)</td><td>0.04 <b>(+63.17%)</b></td><td>0.01 <b>(-36.37%)</b></td><td>225.00 <b>(-38.71%)</b></td><td>179.48 (-18.11%)</td><td>159.50 (-16.49%)</td><td>156.20 (-1.45%)</td><td>31.51 <b>(-63.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>367.10 (n/a)</td><td>219.18 (n/a)</td><td>191.00 (n/a)</td><td>158.50 (n/a)</td><td>85.80 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (-3.20%)</td><td>0.04 (-19.15%)</td><td>0.04 <b>(-22.06%)</b></td><td>0.04 <b>(-25.72%)</b></td><td>0.01 <b>(+91.84%)</b></td><td>222.00 <b>(+34.63%)</b></td><td>194.96 <b>(+27.11%)</b></td><td>201.90 <b>(+28.27%)</b></td><td>134.60 (+3.30%)</td><td>35.80 <b>(+168.57%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.90 (n/a)</td><td>153.38 (n/a)</td><td>157.40 (n/a)</td><td>130.30 (n/a)</td><td>13.33 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (-2.91%)</td><td>0.05 (+6.85%)</td><td>0.05 (-0.17%)</td><td>0.05 <b>(+64.11%)</b></td><td>0.00 <b>(-68.35%)</b></td><td>188.70 <b>(-39.07%)</b></td><td>175.30 (-11.67%)</td><td>170.90 (+0.18%)</td><td>164.20 (+3.01%)</td><td>12.45 <b>(-80.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.70 (n/a)</td><td>198.46 (n/a)</td><td>170.60 (n/a)</td><td>159.40 (n/a)</td><td>63.54 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (-2.82%)</td><td>0.04 (-15.53%)</td><td>0.04 (-19.49%)</td><td>0.03 (-17.36%)</td><td>0.01 (+17.75%)</td><td>280.20 <b>(+20.98%)</b></td><td>221.98 (+19.43%)</td><td>216.90 <b>(+24.23%)</b></td><td>175.70 (+2.87%)</td><td>37.41 <b>(+45.64%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>185.86 (n/a)</td><td>174.60 (n/a)</td><td>170.80 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.73 <b>(+25.75%)</b></td><td>0.62 <b>(+36.79%)</b></td><td>0.66 <b>(+32.62%)</b></td><td>0.52 <b>(+97.47%)</b></td><td>0.10 <b>(-23.16%)</b></td><td>190.80 <b>(-49.36%)</b></td><td>161.20 <b>(-31.34%)</b></td><td>148.70 <b>(-24.59%)</b></td><td>134.10 <b>(-20.51%)</b></td><td>26.64 <b>(-68.68%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (n/a)</td><td>0.46 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>376.80 (n/a)</td><td>234.78 (n/a)</td><td>197.20 (n/a)</td><td>168.70 (n/a)</td><td>85.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.64 (-17.44%)</td><td>0.54 (-16.64%)</td><td>0.56 <b>(-20.86%)</b></td><td>0.45 (-13.58%)</td><td>0.08 <b>(-34.73%)</b></td><td>220.70 (+15.73%)</td><td>185.86 (+18.56%)</td><td>175.90 <b>(+26.36%)</b></td><td>154.60 <b>(+21.16%)</b></td><td>27.11 (-10.33%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.77 (n/a)</td><td>0.65 (n/a)</td><td>0.71 (n/a)</td><td>0.52 (n/a)</td><td>0.12 (n/a)</td><td>190.70 (n/a)</td><td>156.76 (n/a)</td><td>139.20 (n/a)</td><td>127.60 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.74 <b>(-20.30%)</b></td><td>0.60 (+1.93%)</td><td>0.59 <b>(+23.72%)</b></td><td>0.42 (-9.55%)</td><td>0.12 <b>(-38.44%)</b></td><td>234.60 (+10.56%)</td><td>171.34 (-5.06%)</td><td>166.00 (-19.18%)</td><td>132.00 <b>(+25.48%)</b></td><td>39.60 (-13.29%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.93 (n/a)</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.46 (n/a)</td><td>0.20 (n/a)</td><td>212.20 (n/a)</td><td>180.48 (n/a)</td><td>205.40 (n/a)</td><td>105.20 (n/a)</td><td>45.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.52 (-17.51%)</td><td>0.50 (-11.57%)</td><td>0.51 (-13.25%)</td><td>0.45 (-10.49%)</td><td>0.03 <b>(-50.80%)</b></td><td>219.90 (+11.74%)</td><td>197.30 (+12.33%)</td><td>193.30 (+15.27%)</td><td>188.80 <b>(+21.18%)</b></td><td>12.97 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.63 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.50 (n/a)</td><td>0.06 (n/a)</td><td>196.80 (n/a)</td><td>175.64 (n/a)</td><td>167.70 (n/a)</td><td>155.80 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.50 (-13.47%)</td><td>0.44 (-18.46%)</td><td>0.48 (-12.12%)</td><td>0.36 <b>(-29.36%)</b></td><td>0.07 <b>(+145.87%)</b></td><td>207.20 <b>(+41.53%)</b></td><td>170.80 <b>(+25.33%)</b></td><td>152.90 (+13.85%)</td><td>146.10 (+15.59%)</td><td>30.37 <b>(+299.95%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (n/a)</td><td>0.54 (n/a)</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.03 (n/a)</td><td>146.40 (n/a)</td><td>136.28 (n/a)</td><td>134.30 (n/a)</td><td>126.40 (n/a)</td><td>7.59 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.60 (+1.97%)</td><td>0.40 <b>(-24.00%)</b></td><td>0.42 <b>(-26.57%)</b></td><td>0.21 <b>(-38.19%)</b></td><td>0.14 <b>(+31.86%)</b></td><td>355.90 <b>(+61.77%)</b></td><td>207.72 <b>(+41.81%)</b></td><td>175.10 <b>(+36.16%)</b></td><td>123.70 (-1.90%)</td><td>89.04 <b>(+116.41%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (n/a)</td><td>0.53 (n/a)</td><td>0.57 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>220.00 (n/a)</td><td>146.48 (n/a)</td><td>128.60 (n/a)</td><td>126.10 (n/a)</td><td>41.15 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.45 <b>(-28.49%)</b></td><td>0.42 (-12.97%)</td><td>0.43 (-15.54%)</td><td>0.37 <b>(+42.69%)</b></td><td>0.03 <b>(-77.43%)</b></td><td>199.60 <b>(-29.92%)</b></td><td>174.94 (+4.97%)</td><td>171.20 (+18.40%)</td><td>163.70 <b>(+39.80%)</b></td><td>14.20 <b>(-78.96%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.63 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>284.80 (n/a)</td><td>166.66 (n/a)</td><td>144.60 (n/a)</td><td>117.10 (n/a)</td><td>67.50 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.48 (-16.64%)</td><td>0.39 (-19.37%)</td><td>0.40 (-13.91%)</td><td>0.29 <b>(-25.66%)</b></td><td>0.07 (+0.84%)</td><td>256.10 <b>(+34.51%)</b></td><td>196.04 <b>(+25.51%)</b></td><td>182.90 (+16.13%)</td><td>152.50 (+19.98%)</td><td>39.44 <b>(+65.34%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>190.40 (n/a)</td><td>156.20 (n/a)</td><td>157.50 (n/a)</td><td>127.10 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.75 <b>(-36.36%)</b></td><td>0.67 <b>(-31.43%)</b></td><td>0.65 <b>(-32.75%)</b></td><td>0.56 <b>(-35.13%)</b></td><td>0.08 <b>(-36.19%)</b></td><td>235.20 <b>(+54.13%)</b></td><td>198.08 <b>(+45.80%)</b></td><td>200.90 <b>(+48.70%)</b></td><td>175.20 <b>(+57.13%)</b></td><td>24.50 <b>(+53.17%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.18 (n/a)</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.86 (n/a)</td><td>0.12 (n/a)</td><td>152.60 (n/a)</td><td>135.86 (n/a)</td><td>135.10 (n/a)</td><td>111.50 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.74 <b>(-30.83%)</b></td><td>0.67 (-16.40%)</td><td>0.68 (-14.40%)</td><td>0.60 <b>(+24.19%)</b></td><td>0.05 <b>(-76.64%)</b></td><td>218.90 (-19.46%)</td><td>196.84 (+11.85%)</td><td>192.80 (+16.85%)</td><td>178.20 <b>(+44.53%)</b></td><td>15.26 <b>(-73.51%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.06 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.48 (n/a)</td><td>0.22 (n/a)</td><td>271.80 (n/a)</td><td>175.98 (n/a)</td><td>165.00 (n/a)</td><td>123.30 (n/a)</td><td>57.60 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.79 <b>(-21.66%)</b></td><td>0.69 (-9.89%)</td><td>0.68 (-12.84%)</td><td>0.61 <b>(+68.38%)</b></td><td>0.07 <b>(-70.80%)</b></td><td>214.50 <b>(-40.60%)</b></td><td>190.80 (-1.90%)</td><td>191.80 (+14.78%)</td><td>166.00 <b>(+27.69%)</b></td><td>19.97 <b>(-78.99%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.01 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>361.10 (n/a)</td><td>194.50 (n/a)</td><td>167.10 (n/a)</td><td>130.00 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (-2.96%)</td><td>0.03 (-3.17%)</td><td>0.03 (+10.49%)</td><td>0.02 (-8.90%)</td><td>0.00 (-5.66%)</td><td>206.60 (+9.78%)</td><td>162.26 (+3.39%)</td><td>149.30 (-9.52%)</td><td>132.50 (+3.11%)</td><td>29.22 (+11.44%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>156.94 (n/a)</td><td>165.00 (n/a)</td><td>128.50 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (-3.07%)</td><td>0.02 (-10.04%)</td><td>0.02 (-16.00%)</td><td>0.02 (-15.54%)</td><td>0.00 <b>(+37.45%)</b></td><td>199.60 (+18.39%)</td><td>168.00 (+12.59%)</td><td>176.30 (+19.04%)</td><td>133.40 (+3.17%)</td><td>27.80 <b>(+65.28%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>168.60 (n/a)</td><td>149.22 (n/a)</td><td>148.10 (n/a)</td><td>129.30 (n/a)</td><td>16.82 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (-7.12%)</td><td>0.02 (-6.89%)</td><td>0.02 (+6.00%)</td><td>0.02 (-18.13%)</td><td>0.00 <b>(+34.93%)</b></td><td>229.30 <b>(+22.16%)</b></td><td>186.06 (+8.92%)</td><td>167.80 (-5.62%)</td><td>157.30 (+7.67%)</td><td>33.38 <b>(+75.49%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.70 (n/a)</td><td>170.82 (n/a)</td><td>177.80 (n/a)</td><td>146.10 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.18 <b>(+21.57%)</b></td><td>0.88 (+19.07%)</td><td>0.83 (+13.15%)</td><td>0.69 <b>(+22.92%)</b></td><td>0.20 <b>(+32.70%)</b></td><td>191.50 (-18.65%)</td><td>156.44 (-15.47%)</td><td>158.20 (-11.67%)</td><td>112.00 (-17.71%)</td><td>32.82 (-9.52%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.97 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.56 (n/a)</td><td>0.15 (n/a)</td><td>235.40 (n/a)</td><td>185.06 (n/a)</td><td>179.10 (n/a)</td><td>136.10 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.15 <b>(+39.33%)</b></td><td>0.84 (+17.29%)</td><td>0.77 (+3.05%)</td><td>0.60 (-0.68%)</td><td>0.23 <b>(+140.99%)</b></td><td>219.20 (+0.69%)</td><td>167.66 (-10.83%)</td><td>171.80 (-2.94%)</td><td>115.00 <b>(-28.21%)</b></td><td>44.31 <b>(+69.47%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.10 (n/a)</td><td>217.70 (n/a)</td><td>188.02 (n/a)</td><td>177.00 (n/a)</td><td>160.20 (n/a)</td><td>26.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.15 (+18.91%)</td><td>0.85 (+3.45%)</td><td>0.75 (-8.71%)</td><td>0.61 (-15.49%)</td><td>0.23 <b>(+150.36%)</b></td><td>214.90 (+18.34%)</td><td>164.14 (+1.37%)</td><td>176.40 (+9.57%)</td><td>114.40 (-15.88%)</td><td>42.17 <b>(+146.00%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.73 (n/a)</td><td>0.09 (n/a)</td><td>181.60 (n/a)</td><td>161.92 (n/a)</td><td>161.00 (n/a)</td><td>136.00 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.80 <b>(-26.37%)</b></td><td>0.69 <b>(-27.21%)</b></td><td>0.72 <b>(-27.12%)</b></td><td>0.52 <b>(-27.89%)</b></td><td>0.11 (-18.75%)</td><td>253.10 <b>(+38.68%)</b></td><td>195.10 <b>(+37.96%)</b></td><td>184.00 <b>(+37.21%)</b></td><td>164.50 <b>(+35.84%)</b></td><td>35.63 <b>(+49.14%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>1.09 (n/a)</td><td>0.95 (n/a)</td><td>0.99 (n/a)</td><td>0.72 (n/a)</td><td>0.14 (n/a)</td><td>182.50 (n/a)</td><td>141.42 (n/a)</td><td>134.10 (n/a)</td><td>121.10 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.08 (+9.41%)</td><td>0.80 (+6.89%)</td><td>0.80 (+6.37%)</td><td>0.58 (-5.18%)</td><td>0.19 (+18.33%)</td><td>229.20 (+5.48%)</td><td>172.18 (-5.54%)</td><td>166.20 (-5.94%)</td><td>121.90 (-8.55%)</td><td>39.22 (+10.46%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.99 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.16 (n/a)</td><td>217.30 (n/a)</td><td>182.28 (n/a)</td><td>176.70 (n/a)</td><td>133.30 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (-3.50%)</td><td>0.02 (-7.77%)</td><td>0.02 (-3.17%)</td><td>0.02 (-15.19%)</td><td>0.00 <b>(+29.00%)</b></td><td>203.10 (+17.94%)</td><td>173.52 (+9.12%)</td><td>169.30 (+3.23%)</td><td>144.40 (+3.66%)</td><td>21.73 <b>(+57.10%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.20 (n/a)</td><td>159.02 (n/a)</td><td>164.00 (n/a)</td><td>139.30 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 <b>(+39.06%)</b></td><td>0.02 (+2.21%)</td><td>0.02 (-3.77%)</td><td>0.02 <b>(-21.36%)</b></td><td>0.01 <b>(+373.74%)</b></td><td>232.70 <b>(+27.16%)</b></td><td>175.44 (+3.29%)</td><td>175.70 (+3.90%)</td><td>111.00 <b>(-28.11%)</b></td><td>43.29 <b>(+314.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.00 (n/a)</td><td>169.86 (n/a)</td><td>169.10 (n/a)</td><td>154.40 (n/a)</td><td>10.44 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.00 (-4.35%)</td><td>0.00 (-1.87%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 (+8.18%)</td><td>1038.25 (+0.36%)</td><td>978.32 (+1.77%)</td><td>960.53 (+0.62%)</td><td>924.69 (+2.74%)</td><td>52.77 (+8.30%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1034.55 (n/a)</td><td>961.28 (n/a)</td><td>954.57 (n/a)</td><td>900.03 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.01 (+6.17%)</td><td>0.01 (+3.87%)</td><td>0.01 (+3.85%)</td><td>0.01 (+2.78%)</td><td>0.00 <b>(+52.56%)</b></td><td>1111.30 (-1.80%)</td><td>1021.72 (-3.41%)</td><td>1007.67 (-4.23%)</td><td>955.19 (-5.32%)</td><td>66.60 <b>(+46.89%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1131.70 (n/a)</td><td>1057.76 (n/a)</td><td>1052.13 (n/a)</td><td>1008.85 (n/a)</td><td>45.34 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.01 (+1.84%)</td><td>0.98 (+2.73%)</td><td>0.98 (+4.11%)</td><td>0.96 (+1.82%)</td><td>0.02 (-2.14%)</td><td>2195.72 (-1.79%)</td><td>2141.29 (-2.66%)</td><td>2135.92 (-3.95%)</td><td>2076.58 (-1.80%)</td><td>47.28 (-5.33%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.99 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2235.74 (n/a)</td><td>2199.88 (n/a)</td><td>2223.65 (n/a)</td><td>2114.71 (n/a)</td><td>49.94 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.40 (+3.37%)</td><td>0.39 (+1.45%)</td><td>0.38 (+1.27%)</td><td>0.38 (+1.05%)</td><td>0.01 <b>(+34.24%)</b></td><td>1392.23 (-1.02%)</td><td>1358.80 (-1.40%)</td><td>1370.43 (-1.25%)</td><td>1295.28 (-3.25%)</td><td>37.02 <b>(+27.58%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.01 (n/a)</td><td>1406.59 (n/a)</td><td>1378.10 (n/a)</td><td>1387.76 (n/a)</td><td>1338.84 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.25 (-5.16%)</td><td>0.25 (-0.70%)</td><td>0.25 (-1.19%)</td><td>0.24 (+10.78%)</td><td>0.01 <b>(-72.01%)</b></td><td>2189.35 (-9.71%)</td><td>2133.58 (+0.26%)</td><td>2107.93 (+1.20%)</td><td>2096.23 (+5.43%)</td><td>45.38 <b>(-73.69%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>2424.73 (n/a)</td><td>2128.13 (n/a)</td><td>2083.03 (n/a)</td><td>1988.28 (n/a)</td><td>172.47 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.38 (+2.88%)</td><td>0.37 (+1.07%)</td><td>0.36 (-0.52%)</td><td>0.36 (-0.53%)</td><td>0.01 <b>(+184.54%)</b></td><td>1460.31 (+0.54%)</td><td>1419.06 (-1.00%)</td><td>1441.22 (+0.53%)</td><td>1373.17 (-2.80%)</td><td>40.76 <b>(+177.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.00 (n/a)</td><td>1452.53 (n/a)</td><td>1433.38 (n/a)</td><td>1433.58 (n/a)</td><td>1412.70 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.45 (+4.43%)</td><td>2.62 (-5.51%)</td><td>2.61 (-1.91%)</td><td>2.02 (-17.33%)</td><td>0.53 <b>(+56.56%)</b></td><td>259.60 <b>(+20.97%)</b></td><td>206.18 (+7.90%)</td><td>200.80 (+1.93%)</td><td>151.90 (-4.22%)</td><td>39.02 <b>(+80.35%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.31 (n/a)</td><td>2.77 (n/a)</td><td>2.66 (n/a)</td><td>2.44 (n/a)</td><td>0.34 (n/a)</td><td>214.60 (n/a)</td><td>191.08 (n/a)</td><td>197.00 (n/a)</td><td>158.60 (n/a)</td><td>21.64 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>5.86 (-5.16%)</td><td>4.79 (-6.86%)</td><td>4.68 (-5.72%)</td><td>3.70 (-11.27%)</td><td>0.81 (-7.61%)</td><td>283.10 (+12.70%)</td><td>224.32 (+7.41%)</td><td>224.20 (+6.05%)</td><td>178.90 (+5.42%)</td><td>39.09 (+11.54%)</td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>6.18 (n/a)</td><td>5.14 (n/a)</td><td>4.96 (n/a)</td><td>4.17 (n/a)</td><td>0.87 (n/a)</td><td>251.20 (n/a)</td><td>208.84 (n/a)</td><td>211.40 (n/a)</td><td>169.70 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.24 (-2.53%)</td><td>2.76 (-9.31%)</td><td>2.75 (-7.48%)</td><td>2.29 (-13.89%)</td><td>0.35 <b>(+30.02%)</b></td><td>228.90 (+16.13%)</td><td>192.54 (+11.03%)</td><td>190.60 (+8.11%)</td><td>161.80 (+2.60%)</td><td>25.03 <b>(+56.81%)</b></td>
</tr>
<tr>
<td><code>a279467</code> — 2026-08-31 15:38:06</td><td>3.32 (n/a)</td><td>3.04 (n/a)</td><td>2.97 (n/a)</td><td>2.66 (n/a)</td><td>0.27 (n/a)</td><td>197.10 (n/a)</td><td>173.42 (n/a)</td><td>176.30 (n/a)</td><td>157.70 (n/a)</td><td>15.96 (n/a)</td>
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
