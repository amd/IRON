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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (-7.33%)</td><td>0.09 (+9.09%)</td><td>0.08 (-7.83%)</td><td>0.08 <b>(+53.99%)</b></td><td>0.01 <b>(-68.47%)</b></td><td>155.90 <b>(-35.07%)</b></td><td>143.70 (-14.86%)</td><td>147.20 (+8.47%)</td><td>128.90 (+7.87%)</td><td>11.94 <b>(-78.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>240.10 (n/a)</td><td>168.78 (n/a)</td><td>135.70 (n/a)</td><td>119.50 (n/a)</td><td>55.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.12 <b>(+20.83%)</b></td><td>0.08 (+8.57%)</td><td>0.07 (-9.43%)</td><td>0.07 <b>(+22.19%)</b></td><td>0.02 <b>(+28.03%)</b></td><td>173.30 (-18.14%)</td><td>153.08 (-7.59%)</td><td>167.10 (+10.44%)</td><td>103.70 (-17.30%)</td><td>29.43 (-15.02%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>211.70 (n/a)</td><td>165.66 (n/a)</td><td>151.30 (n/a)</td><td>125.40 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (-18.50%)</td><td>0.07 (-14.23%)</td><td>0.07 (-10.62%)</td><td>0.06 (-10.72%)</td><td>0.01 <b>(-38.57%)</b></td><td>192.80 (+12.03%)</td><td>175.42 (+15.99%)</td><td>173.70 (+11.85%)</td><td>155.30 <b>(+22.67%)</b></td><td>14.89 (-14.38%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>151.24 (n/a)</td><td>155.30 (n/a)</td><td>126.60 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 <b>(-24.66%)</b></td><td>0.06 (-16.08%)</td><td>0.06 (-9.10%)</td><td>0.05 (-2.23%)</td><td>0.01 <b>(-59.57%)</b></td><td>227.70 (+2.25%)</td><td>201.72 (+15.98%)</td><td>196.30 (+10.03%)</td><td>179.60 <b>(+32.74%)</b></td><td>20.66 <b>(-43.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>222.70 (n/a)</td><td>173.92 (n/a)</td><td>178.40 (n/a)</td><td>135.30 (n/a)</td><td>36.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (-18.86%)</td><td>0.03 (-10.95%)</td><td>0.03 (-8.22%)</td><td>0.03 (-4.39%)</td><td>0.00 <b>(-54.77%)</b></td><td>188.40 (+4.61%)</td><td>177.78 (+10.84%)</td><td>182.20 (+8.97%)</td><td>155.40 <b>(+23.24%)</b></td><td>12.96 <b>(-42.90%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.10 (n/a)</td><td>160.40 (n/a)</td><td>167.20 (n/a)</td><td>126.10 (n/a)</td><td>22.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (+15.84%)</td><td>0.03 (+16.82%)</td><td>0.03 (+10.16%)</td><td>0.03 <b>(+25.91%)</b></td><td>0.01 (+0.25%)</td><td>192.40 <b>(-20.59%)</b></td><td>154.44 (-15.25%)</td><td>154.70 (-9.27%)</td><td>123.50 (-13.70%)</td><td>25.14 <b>(-32.60%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>182.22 (n/a)</td><td>170.50 (n/a)</td><td>143.10 (n/a)</td><td>37.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(+20.59%)</b></td><td>0.03 (+0.15%)</td><td>0.03 (-6.08%)</td><td>0.03 (+3.16%)</td><td>0.01 <b>(+48.34%)</b></td><td>198.20 (-3.08%)</td><td>162.68 (+1.92%)</td><td>164.80 (+6.46%)</td><td>103.00 (-17.07%)</td><td>36.21 (+13.49%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>159.62 (n/a)</td><td>154.80 (n/a)</td><td>124.20 (n/a)</td><td>31.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 <b>(-27.21%)</b></td><td>0.03 (-9.40%)</td><td>0.03 (+3.61%)</td><td>0.03 (-12.39%)</td><td>0.00 <b>(-55.56%)</b></td><td>206.90 (+14.12%)</td><td>172.54 (+8.30%)</td><td>165.70 (-3.49%)</td><td>156.00 <b>(+37.32%)</b></td><td>19.80 <b>(-26.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>181.30 (n/a)</td><td>159.32 (n/a)</td><td>171.70 (n/a)</td><td>113.60 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 <b>(+20.82%)</b></td><td>0.03 <b>(+29.37%)</b></td><td>0.03 (+19.83%)</td><td>0.03 <b>(+80.13%)</b></td><td>0.00 <b>(-38.66%)</b></td><td>196.50 <b>(-44.49%)</b></td><td>177.42 <b>(-25.82%)</b></td><td>181.10 (-16.54%)</td><td>158.30 (-17.25%)</td><td>18.17 <b>(-72.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>354.00 (n/a)</td><td>239.18 (n/a)</td><td>217.00 (n/a)</td><td>191.30 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (+11.84%)</td><td>0.03 (-4.24%)</td><td>0.03 (-12.20%)</td><td>0.02 (-0.07%)</td><td>0.01 <b>(+38.25%)</b></td><td>241.20 (+0.08%)</td><td>196.70 (+5.90%)</td><td>204.90 (+13.90%)</td><td>134.00 (-10.55%)</td><td>38.91 (+14.56%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.00 (n/a)</td><td>185.74 (n/a)</td><td>179.90 (n/a)</td><td>149.80 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (+6.49%)</td><td>0.03 (+16.91%)</td><td>0.03 (+15.47%)</td><td>0.02 <b>(+27.10%)</b></td><td>0.00 (-9.62%)</td><td>221.70 <b>(-21.33%)</b></td><td>183.56 (-15.65%)</td><td>178.30 (-13.40%)</td><td>152.40 (-6.10%)</td><td>30.43 <b>(-34.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>281.80 (n/a)</td><td>217.62 (n/a)</td><td>205.90 (n/a)</td><td>162.30 (n/a)</td><td>46.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (-5.67%)</td><td>0.02 (-14.00%)</td><td>0.02 (-18.03%)</td><td>0.02 (-13.34%)</td><td>0.00 (+15.61%)</td><td>326.70 (+15.40%)</td><td>252.56 (+18.17%)</td><td>235.90 <b>(+21.98%)</b></td><td>190.20 (+6.02%)</td><td>58.85 <b>(+40.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>283.10 (n/a)</td><td>213.72 (n/a)</td><td>193.40 (n/a)</td><td>179.40 (n/a)</td><td>41.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>201.10 (n/a)</td><td>142.08 (n/a)</td><td>129.10 (n/a)</td><td>122.40 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>144.10 (n/a)</td><td>141.00 (n/a)</td><td>124.80 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>364.30 (n/a)</td><td>193.24 (n/a)</td><td>157.10 (n/a)</td><td>135.80 (n/a)</td><td>96.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.50 (n/a)</td><td>164.34 (n/a)</td><td>163.60 (n/a)</td><td>135.80 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>184.30 (n/a)</td><td>149.76 (n/a)</td><td>137.70 (n/a)</td><td>119.20 (n/a)</td><td>28.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>208.50 (n/a)</td><td>162.00 (n/a)</td><td>160.70 (n/a)</td><td>122.70 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>187.20 (n/a)</td><td>146.76 (n/a)</td><td>130.20 (n/a)</td><td>121.40 (n/a)</td><td>29.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>284.70 (n/a)</td><td>207.58 (n/a)</td><td>182.70 (n/a)</td><td>156.00 (n/a)</td><td>55.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>169.40 (n/a)</td><td>174.80 (n/a)</td><td>133.80 (n/a)</td><td>23.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.00 (n/a)</td><td>159.52 (n/a)</td><td>159.30 (n/a)</td><td>110.80 (n/a)</td><td>34.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>193.60 (n/a)</td><td>165.30 (n/a)</td><td>178.90 (n/a)</td><td>102.80 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>159.92 (n/a)</td><td>148.10 (n/a)</td><td>103.80 (n/a)</td><td>52.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>305.90 (n/a)</td><td>192.56 (n/a)</td><td>168.40 (n/a)</td><td>109.60 (n/a)</td><td>80.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.80 (n/a)</td><td>168.48 (n/a)</td><td>154.20 (n/a)</td><td>129.70 (n/a)</td><td>46.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>178.84 (n/a)</td><td>170.00 (n/a)</td><td>152.20 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.10 (n/a)</td><td>223.78 (n/a)</td><td>204.90 (n/a)</td><td>172.10 (n/a)</td><td>51.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>4.21 (-1.25%)</td><td>3.90 (-6.44%)</td><td>4.12 (-0.94%)</td><td>3.24 (-19.38%)</td><td>0.41 <b>(+321.74%)</b></td><td>2900.70 <b>(+24.03%)</b></td><td>2436.38 (+7.89%)</td><td>2282.70 (+0.95%)</td><td>2231.60 (+1.26%)</td><td>282.60 <b>(+429.01%)</b></td><td>1657.75 (-1.25%)</td><td>1533.37 (-6.44%)</td><td>1620.60 (-0.94%)</td><td>1275.34 (-19.38%)</td><td>161.76 <b>(+321.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.27 (n/a)</td><td>4.17 (n/a)</td><td>4.16 (n/a)</td><td>4.02 (n/a)</td><td>0.10 (n/a)</td><td>2338.70 (n/a)</td><td>2258.22 (n/a)</td><td>2261.20 (n/a)</td><td>2203.80 (n/a)</td><td>53.42 (n/a)</td><td>1678.66 (n/a)</td><td>1638.92 (n/a)</td><td>1636.05 (n/a)</td><td>1581.84 (n/a)</td><td>38.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 <b>(-22.59%)</b></td><td>0.76 <b>(-24.06%)</b></td><td>0.68 <b>(-30.39%)</b></td><td>0.64 (-7.38%)</td><td>0.16 <b>(-35.70%)</b></td><td>348.30 (+7.97%)</td><td>299.66 <b>(+28.94%)</b></td><td>323.70 <b>(+43.68%)</b></td><td>216.70 <b>(+29.22%)</b></td><td>52.12 (-12.57%)</td><td>43.56 <b>(-22.59%)</b></td><td>32.41 <b>(-24.06%)</b></td><td>29.15 <b>(-30.39%)</b></td><td>27.09 (-7.38%)</td><td>6.65 <b>(-35.70%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.32 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.69 (n/a)</td><td>0.24 (n/a)</td><td>322.60 (n/a)</td><td>232.40 (n/a)</td><td>225.30 (n/a)</td><td>167.70 (n/a)</td><td>59.61 (n/a)</td><td>56.27 (n/a)</td><td>42.68 (n/a)</td><td>41.88 (n/a)</td><td>29.25 (n/a)</td><td>10.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.99 <b>(-25.08%)</b></td><td>0.84 (-14.71%)</td><td>0.80 <b>(-25.76%)</b></td><td>0.69 (+3.76%)</td><td>0.13 <b>(-53.43%)</b></td><td>320.50 (-3.64%)</td><td>267.24 (+11.41%)</td><td>278.00 <b>(+34.69%)</b></td><td>223.60 <b>(+33.49%)</b></td><td>41.09 <b>(-43.36%)</b></td><td>42.20 <b>(-25.08%)</b></td><td>35.99 (-14.71%)</td><td>33.94 <b>(-25.76%)</b></td><td>29.44 (+3.76%)</td><td>5.56 <b>(-53.43%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.32 (n/a)</td><td>0.99 (n/a)</td><td>1.07 (n/a)</td><td>0.67 (n/a)</td><td>0.28 (n/a)</td><td>332.60 (n/a)</td><td>239.86 (n/a)</td><td>206.40 (n/a)</td><td>167.50 (n/a)</td><td>72.54 (n/a)</td><td>56.32 (n/a)</td><td>42.20 (n/a)</td><td>45.72 (n/a)</td><td>28.38 (n/a)</td><td>11.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.52 (-0.01%)</td><td>0.52 (-0.08%)</td><td>0.52 (-0.05%)</td><td>0.52 (-0.21%)</td><td>0.00 <b>(+83.49%)</b></td><td>48658.90 (+0.21%)</td><td>48511.92 (+0.08%)</td><td>48478.30 (+0.05%)</td><td>48453.30 (+0.01%)</td><td>84.38 <b>(+83.87%)</b></td><td>354.57 (-0.01%)</td><td>354.14 (-0.08%)</td><td>354.38 (-0.05%)</td><td>353.07 (-0.21%)</td><td>0.61 <b>(+83.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48556.50 (n/a)</td><td>48474.60 (n/a)</td><td>48455.20 (n/a)</td><td>48450.50 (n/a)</td><td>45.89 (n/a)</td><td>354.59 (n/a)</td><td>354.41 (n/a)</td><td>354.55 (n/a)</td><td>353.81 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.90 (+0.87%)</td><td>0.89 (+0.10%)</td><td>0.89 (-0.22%)</td><td>0.89 (+0.11%)</td><td>0.01 <b>(+75.33%)</b></td><td>28432.00 (-0.11%)</td><td>28243.24 (-0.10%)</td><td>28313.00 (+0.22%)</td><td>27941.90 (-0.86%)</td><td>190.69 <b>(+73.40%)</b></td><td>614.84 (+0.87%)</td><td>608.31 (+0.10%)</td><td>606.78 (-0.22%)</td><td>604.24 (+0.11%)</td><td>4.13 <b>(+75.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.00 (n/a)</td><td>28461.90 (n/a)</td><td>28271.80 (n/a)</td><td>28250.00 (n/a)</td><td>28184.40 (n/a)</td><td>109.97 (n/a)</td><td>609.55 (n/a)</td><td>607.68 (n/a)</td><td>608.14 (n/a)</td><td>603.61 (n/a)</td><td>2.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.35 (+0.51%)</td><td>3.24 (+1.22%)</td><td>3.19 (+0.23%)</td><td>3.15 (+0.33%)</td><td>0.10 <b>(+24.19%)</b></td><td>7977.40 (-0.32%)</td><td>7766.06 (-1.18%)</td><td>7878.80 (-0.23%)</td><td>7502.80 (-0.50%)</td><td>227.60 <b>(+23.38%)</b></td><td>2289.79 (+0.51%)</td><td>2213.71 (+1.22%)</td><td>2180.52 (+0.23%)</td><td>2153.56 (+0.33%)</td><td>65.48 <b>(+24.19%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.34 (n/a)</td><td>3.20 (n/a)</td><td>3.19 (n/a)</td><td>3.14 (n/a)</td><td>0.08 (n/a)</td><td>8003.40 (n/a)</td><td>7859.10 (n/a)</td><td>7896.60 (n/a)</td><td>7540.80 (n/a)</td><td>184.48 (n/a)</td><td>2278.26 (n/a)</td><td>2186.98 (n/a)</td><td>2175.61 (n/a)</td><td>2146.58 (n/a)</td><td>52.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.88 (-9.56%)</td><td>3.69 (+1.09%)</td><td>3.77 (+3.98%)</td><td>3.30 (+13.43%)</td><td>0.24 <b>(-52.36%)</b></td><td>2442.10 (-11.84%)</td><td>2189.38 (-2.31%)</td><td>2136.00 (-3.82%)</td><td>2078.20 (+10.58%)</td><td>150.44 <b>(-54.30%)</b></td><td>1017.21 (-9.56%)</td><td>968.98 (+1.09%)</td><td>989.69 (+3.98%)</td><td>865.62 (+13.43%)</td><td>62.51 <b>(-52.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.29 (n/a)</td><td>3.66 (n/a)</td><td>3.63 (n/a)</td><td>2.91 (n/a)</td><td>0.50 (n/a)</td><td>2770.00 (n/a)</td><td>2241.06 (n/a)</td><td>2220.90 (n/a)</td><td>1879.40 (n/a)</td><td>329.16 (n/a)</td><td>1124.79 (n/a)</td><td>958.55 (n/a)</td><td>951.83 (n/a)</td><td>763.14 (n/a)</td><td>131.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.39 <b>(-23.29%)</b></td><td>0.34 (-12.11%)</td><td>0.34 (-4.00%)</td><td>0.32 (+14.19%)</td><td>0.03 <b>(-75.33%)</b></td><td>3833.10 (-12.43%)</td><td>3642.80 (+7.99%)</td><td>3693.30 (+4.17%)</td><td>3207.80 <b>(+30.36%)</b></td><td>253.29 <b>(-70.84%)</b></td><td>20.92 <b>(-23.29%)</b></td><td>18.50 (-12.11%)</td><td>18.17 (-4.00%)</td><td>17.51 (+14.19%)</td><td>1.39 <b>(-75.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>4377.10 (n/a)</td><td>3373.38 (n/a)</td><td>3545.60 (n/a)</td><td>2460.70 (n/a)</td><td>868.57 (n/a)</td><td>27.27 (n/a)</td><td>21.05 (n/a)</td><td>18.93 (n/a)</td><td>15.33 (n/a)</td><td>5.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>6.16 <b>(+24.85%)</b></td><td>4.45 (+9.82%)</td><td>4.44 <b>(+23.44%)</b></td><td>3.27 (-4.19%)</td><td>1.14 <b>(+55.45%)</b></td><td>2036.70 (+4.38%)</td><td>1570.56 (-6.61%)</td><td>1497.90 (-18.99%)</td><td>1080.30 (-19.90%)</td><td>382.96 <b>(+33.16%)</b></td><td>1902.40 <b>(+24.85%)</b></td><td>1376.29 (+9.82%)</td><td>1372.05 <b>(+23.44%)</b></td><td>1009.11 (-4.19%)</td><td>353.63 <b>(+55.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>4.93 (n/a)</td><td>4.06 (n/a)</td><td>3.60 (n/a)</td><td>3.41 (n/a)</td><td>0.74 (n/a)</td><td>1951.30 (n/a)</td><td>1681.74 (n/a)</td><td>1849.10 (n/a)</td><td>1348.70 (n/a)</td><td>287.59 (n/a)</td><td>1523.81 (n/a)</td><td>1253.17 (n/a)</td><td>1111.49 (n/a)</td><td>1053.25 (n/a)</td><td>227.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.51 (n/a)</td><td>12.32 (n/a)</td><td>11.99 (n/a)</td><td>10.90 (n/a)</td><td>1.15 (n/a)</td><td>13.50 (n/a)</td><td>12.31 (n/a)</td><td>11.99 (n/a)</td><td>10.89 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>24.24 (+1.95%)</td><td>23.74 (+9.43%)</td><td>23.89 (+6.92%)</td><td>23.11 <b>(+33.34%)</b></td><td>0.54 <b>(-78.42%)</b></td><td>24.23 (+1.95%)</td><td>23.72 (+9.43%)</td><td>23.87 (+6.92%)</td><td>23.09 <b>(+33.34%)</b></td><td>0.54 <b>(-78.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>23.78 (n/a)</td><td>21.69 (n/a)</td><td>22.34 (n/a)</td><td>17.33 (n/a)</td><td>2.52 (n/a)</td><td>23.76 (n/a)</td><td>21.68 (n/a)</td><td>22.33 (n/a)</td><td>17.32 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>41.78 (+2.06%)</td><td>39.53 (-1.92%)</td><td>41.16 (+1.60%)</td><td>35.55 (-9.61%)</td><td>2.87 <b>(+345.51%)</b></td><td>41.75 (+2.06%)</td><td>39.50 (-1.92%)</td><td>41.13 (+1.60%)</td><td>35.53 (-9.61%)</td><td>2.87 <b>(+345.51%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>40.93 (n/a)</td><td>40.30 (n/a)</td><td>40.51 (n/a)</td><td>39.33 (n/a)</td><td>0.64 (n/a)</td><td>40.91 (n/a)</td><td>40.27 (n/a)</td><td>40.49 (n/a)</td><td>39.31 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>45.37 (+6.88%)</td><td>43.21 (+5.40%)</td><td>44.52 (+5.07%)</td><td>37.00 (-4.02%)</td><td>3.50 <b>(+78.95%)</b></td><td>45.34 (+6.88%)</td><td>43.19 (+5.40%)</td><td>44.49 (+5.07%)</td><td>36.98 (-4.02%)</td><td>3.49 <b>(+78.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>42.45 (n/a)</td><td>41.00 (n/a)</td><td>42.37 (n/a)</td><td>38.55 (n/a)</td><td>1.95 (n/a)</td><td>42.42 (n/a)</td><td>40.97 (n/a)</td><td>42.35 (n/a)</td><td>38.53 (n/a)</td><td>1.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.57 (n/a)</td><td>12.72 (n/a)</td><td>12.99 (n/a)</td><td>11.04 (n/a)</td><td>1.00 (n/a)</td><td>13.56 (n/a)</td><td>12.71 (n/a)</td><td>12.98 (n/a)</td><td>11.04 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>24.90 (+2.29%)</td><td>24.35 (+3.65%)</td><td>24.40 (+2.98%)</td><td>23.46 (+4.22%)</td><td>0.55 <b>(-29.15%)</b></td><td>24.89 (+2.29%)</td><td>24.33 (+3.65%)</td><td>24.39 (+2.98%)</td><td>23.45 (+4.22%)</td><td>0.55 <b>(-29.15%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>24.35 (n/a)</td><td>23.49 (n/a)</td><td>23.70 (n/a)</td><td>22.51 (n/a)</td><td>0.78 (n/a)</td><td>24.33 (n/a)</td><td>23.47 (n/a)</td><td>23.68 (n/a)</td><td>22.50 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>41.90 (-3.45%)</td><td>36.55 (-11.62%)</td><td>41.30 (-1.78%)</td><td>23.29 <b>(-36.77%)</b></td><td>7.98 <b>(+202.12%)</b></td><td>41.87 (-3.45%)</td><td>36.53 (-11.62%)</td><td>41.27 (-1.78%)</td><td>23.28 <b>(-36.77%)</b></td><td>7.98 <b>(+202.12%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>43.39 (n/a)</td><td>41.36 (n/a)</td><td>42.04 (n/a)</td><td>36.84 (n/a)</td><td>2.64 (n/a)</td><td>43.37 (n/a)</td><td>41.33 (n/a)</td><td>42.02 (n/a)</td><td>36.81 (n/a)</td><td>2.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>45.49 (+2.52%)</td><td>43.47 (+1.19%)</td><td>44.80 (+4.11%)</td><td>39.98 (-4.26%)</td><td>2.47 <b>(+115.92%)</b></td><td>45.46 (+2.52%)</td><td>43.44 (+1.19%)</td><td>44.78 (+4.11%)</td><td>39.95 (-4.26%)</td><td>2.47 <b>(+115.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>44.37 (n/a)</td><td>42.96 (n/a)</td><td>43.03 (n/a)</td><td>41.76 (n/a)</td><td>1.14 (n/a)</td><td>44.34 (n/a)</td><td>42.93 (n/a)</td><td>43.01 (n/a)</td><td>41.73 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>9.59 (+3.96%)</td><td>8.64 (+0.04%)</td><td>8.99 (+3.30%)</td><td>7.06 (-4.98%)</td><td>0.97 <b>(+35.65%)</b></td><td>9.57 (+3.96%)</td><td>8.62 (+0.04%)</td><td>8.97 (+3.30%)</td><td>7.04 (-4.98%)</td><td>0.97 <b>(+35.65%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>9.23 (n/a)</td><td>8.63 (n/a)</td><td>8.70 (n/a)</td><td>7.43 (n/a)</td><td>0.72 (n/a)</td><td>9.21 (n/a)</td><td>8.62 (n/a)</td><td>8.68 (n/a)</td><td>7.41 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.97 (-10.91%)</td><td>0.90 (-2.55%)</td><td>0.90 (-1.14%)</td><td>0.81 (+1.61%)</td><td>0.06 <b>(-45.26%)</b></td><td>0.95 (-10.91%)</td><td>0.88 (-2.55%)</td><td>0.89 (-1.14%)</td><td>0.80 (+1.61%)</td><td>0.06 <b>(-45.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.08 (n/a)</td><td>0.92 (n/a)</td><td>0.92 (n/a)</td><td>0.80 (n/a)</td><td>0.11 (n/a)</td><td>1.07 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.79 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.50 (+8.84%)</td><td>1.25 (+7.17%)</td><td>1.24 (+12.68%)</td><td>1.02 (+2.30%)</td><td>0.22 <b>(+44.19%)</b></td><td>1.48 (+8.84%)</td><td>1.23 (+7.17%)</td><td>1.23 (+12.68%)</td><td>1.01 (+2.30%)</td><td>0.22 <b>(+44.19%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.38 (n/a)</td><td>1.17 (n/a)</td><td>1.10 (n/a)</td><td>1.00 (n/a)</td><td>0.15 (n/a)</td><td>1.36 (n/a)</td><td>1.15 (n/a)</td><td>1.09 (n/a)</td><td>0.99 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>18.27 (-2.85%)</td><td>15.71 (-10.20%)</td><td>16.53 (-3.42%)</td><td>12.96 <b>(-21.50%)</b></td><td>2.24 <b>(+126.26%)</b></td><td>18.06 (-2.85%)</td><td>15.52 (-10.20%)</td><td>16.34 (-3.42%)</td><td>12.81 <b>(-21.50%)</b></td><td>2.21 <b>(+126.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>18.81 (n/a)</td><td>17.49 (n/a)</td><td>17.11 (n/a)</td><td>16.51 (n/a)</td><td>0.99 (n/a)</td><td>18.59 (n/a)</td><td>17.29 (n/a)</td><td>16.92 (n/a)</td><td>16.32 (n/a)</td><td>0.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.89 (-1.00%)</td><td>13.60 (+1.15%)</td><td>13.78 (+1.14%)</td><td>13.19 (+8.67%)</td><td>0.32 <b>(-57.46%)</b></td><td>13.64 (-1.00%)</td><td>13.36 (+1.15%)</td><td>13.54 (+1.14%)</td><td>12.96 (+8.67%)</td><td>0.32 <b>(-57.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>14.03 (n/a)</td><td>13.45 (n/a)</td><td>13.63 (n/a)</td><td>12.14 (n/a)</td><td>0.76 (n/a)</td><td>13.78 (n/a)</td><td>13.21 (n/a)</td><td>13.39 (n/a)</td><td>11.93 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>9.10 (-2.00%)</td><td>7.95 (+2.12%)</td><td>7.78 (+0.63%)</td><td>6.74 (+2.93%)</td><td>0.89 (-8.60%)</td><td>8.95 (-2.00%)</td><td>7.81 (+2.12%)</td><td>7.64 (+0.63%)</td><td>6.63 (+2.93%)</td><td>0.88 (-8.60%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>9.29 (n/a)</td><td>7.78 (n/a)</td><td>7.73 (n/a)</td><td>6.55 (n/a)</td><td>0.98 (n/a)</td><td>9.13 (n/a)</td><td>7.65 (n/a)</td><td>7.59 (n/a)</td><td>6.44 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>6.03 (-6.40%)</td><td>5.65 (-5.83%)</td><td>5.51 (-12.53%)</td><td>5.35 (+11.56%)</td><td>0.31 <b>(-55.45%)</b></td><td>5.94 (-6.40%)</td><td>5.56 (-5.83%)</td><td>5.42 (-12.53%)</td><td>5.26 (+11.56%)</td><td>0.30 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>6.44 (n/a)</td><td>6.00 (n/a)</td><td>6.30 (n/a)</td><td>4.80 (n/a)</td><td>0.69 (n/a)</td><td>6.34 (n/a)</td><td>5.91 (n/a)</td><td>6.20 (n/a)</td><td>4.72 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.25 (n/a)</td><td>12.41 (n/a)</td><td>12.55 (n/a)</td><td>11.08 (n/a)</td><td>0.87 (n/a)</td><td>13.24 (n/a)</td><td>12.41 (n/a)</td><td>12.54 (n/a)</td><td>11.07 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.30 (n/a)</td><td>12.36 (n/a)</td><td>12.05 (n/a)</td><td>11.23 (n/a)</td><td>0.89 (n/a)</td><td>13.29 (n/a)</td><td>12.36 (n/a)</td><td>12.04 (n/a)</td><td>11.23 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>172.84 (n/a)</td><td>187.50 (n/a)</td><td>138.50 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.70 (n/a)</td><td>192.88 (n/a)</td><td>195.00 (n/a)</td><td>126.90 (n/a)</td><td>47.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>183.00 (n/a)</td><td>182.30 (n/a)</td><td>152.10 (n/a)</td><td>29.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>167.62 (n/a)</td><td>167.30 (n/a)</td><td>124.50 (n/a)</td><td>30.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>407.70 (n/a)</td><td>248.80 (n/a)</td><td>200.50 (n/a)</td><td>169.80 (n/a)</td><td>97.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>185.08 (n/a)</td><td>200.10 (n/a)</td><td>155.10 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>176.12 (n/a)</td><td>169.90 (n/a)</td><td>141.50 (n/a)</td><td>30.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.10 (n/a)</td><td>229.30 (n/a)</td><td>212.00 (n/a)</td><td>185.80 (n/a)</td><td>46.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(-30.05%)</b></td><td>0.04 <b>(-25.55%)</b></td><td>0.05 <b>(-26.40%)</b></td><td>0.04 (-9.12%)</td><td>0.00 <b>(-64.77%)</b></td><td>202.00 (+10.02%)</td><td>184.52 <b>(+31.86%)</b></td><td>176.00 <b>(+35.91%)</b></td><td>172.80 <b>(+42.93%)</b></td><td>13.96 <b>(-45.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>139.94 (n/a)</td><td>129.50 (n/a)</td><td>120.90 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 <b>(-24.08%)</b></td><td>0.05 (-2.10%)</td><td>0.05 (+6.58%)</td><td>0.04 (+14.20%)</td><td>0.01 <b>(-63.16%)</b></td><td>189.70 (-12.42%)</td><td>169.68 (-2.05%)</td><td>163.30 (-6.20%)</td><td>147.00 <b>(+31.72%)</b></td><td>17.60 <b>(-54.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>173.24 (n/a)</td><td>174.10 (n/a)</td><td>111.60 (n/a)</td><td>39.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (-1.90%)</td><td>0.06 (+0.26%)</td><td>0.05 (-4.59%)</td><td>0.05 (+4.75%)</td><td>0.01 (-10.61%)</td><td>178.70 (-4.54%)</td><td>150.78 (-0.85%)</td><td>155.60 (+4.78%)</td><td>124.60 (+1.88%)</td><td>23.11 (-14.45%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.20 (n/a)</td><td>152.08 (n/a)</td><td>148.50 (n/a)</td><td>122.30 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-16.33%)</td><td>0.04 <b>(-23.91%)</b></td><td>0.05 (-18.63%)</td><td>0.03 <b>(-36.27%)</b></td><td>0.01 <b>(+36.68%)</b></td><td>285.10 <b>(+56.91%)</b></td><td>200.04 <b>(+37.07%)</b></td><td>180.10 <b>(+22.85%)</b></td><td>147.90 (+19.56%)</td><td>57.28 <b>(+153.51%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.70 (n/a)</td><td>145.94 (n/a)</td><td>146.60 (n/a)</td><td>123.70 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(-34.34%)</b></td><td>0.04 <b>(-23.00%)</b></td><td>0.04 <b>(-31.65%)</b></td><td>0.04 <b>(+22.02%)</b></td><td>0.00 <b>(-75.44%)</b></td><td>210.40 (-18.04%)</td><td>186.16 (+19.24%)</td><td>188.50 <b>(+46.24%)</b></td><td>162.50 <b>(+52.30%)</b></td><td>17.48 <b>(-70.72%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>256.70 (n/a)</td><td>156.12 (n/a)</td><td>128.90 (n/a)</td><td>106.70 (n/a)</td><td>59.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(-30.30%)</b></td><td>0.04 <b>(-26.16%)</b></td><td>0.05 <b>(-24.81%)</b></td><td>0.03 <b>(-26.55%)</b></td><td>0.01 <b>(-48.36%)</b></td><td>239.00 <b>(+36.18%)</b></td><td>189.78 <b>(+33.78%)</b></td><td>181.80 <b>(+32.99%)</b></td><td>167.20 <b>(+43.52%)</b></td><td>28.18 (+5.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.50 (n/a)</td><td>141.86 (n/a)</td><td>136.70 (n/a)</td><td>116.50 (n/a)</td><td>26.59 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(-23.16%)</b></td><td>0.04 <b>(-27.18%)</b></td><td>0.05 (-13.64%)</td><td>0.02 <b>(-56.09%)</b></td><td>0.01 <b>(+84.67%)</b></td><td>374.40 <b>(+127.74%)</b></td><td>222.00 <b>(+50.12%)</b></td><td>175.20 (+15.80%)</td><td>160.90 <b>(+30.07%)</b></td><td>89.84 <b>(+449.20%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.40 (n/a)</td><td>147.88 (n/a)</td><td>151.30 (n/a)</td><td>123.70 (n/a)</td><td>16.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (-13.30%)</td><td>0.04 (-17.41%)</td><td>0.04 (-18.15%)</td><td>0.03 (-12.94%)</td><td>0.01 (-11.70%)</td><td>238.40 (+14.89%)</td><td>205.40 <b>(+21.17%)</b></td><td>203.00 <b>(+22.14%)</b></td><td>154.80 (+15.26%)</td><td>33.80 (+17.31%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.50 (n/a)</td><td>169.52 (n/a)</td><td>166.20 (n/a)</td><td>134.30 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (-8.50%)</td><td>0.04 (-14.24%)</td><td>0.04 <b>(-21.55%)</b></td><td>0.04 (-8.49%)</td><td>0.00 (-12.28%)</td><td>208.50 (+9.28%)</td><td>188.12 (+16.50%)</td><td>195.10 <b>(+27.43%)</b></td><td>165.40 (+9.32%)</td><td>17.28 (+3.35%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>190.80 (n/a)</td><td>161.48 (n/a)</td><td>153.10 (n/a)</td><td>151.30 (n/a)</td><td>16.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (-2.32%)</td><td>0.04 (+3.74%)</td><td>0.04 (+7.11%)</td><td>0.03 (+10.38%)</td><td>0.00 <b>(-32.09%)</b></td><td>237.00 (-9.40%)</td><td>207.96 (-4.54%)</td><td>207.20 (-6.62%)</td><td>180.70 (+2.38%)</td><td>19.94 <b>(-36.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.60 (n/a)</td><td>217.84 (n/a)</td><td>221.90 (n/a)</td><td>176.50 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-13.13%)</td><td>0.05 (-14.38%)</td><td>0.05 (-15.21%)</td><td>0.04 (-16.04%)</td><td>0.01 (+13.90%)</td><td>230.10 (+19.10%)</td><td>186.32 (+18.78%)</td><td>175.00 (+17.92%)</td><td>146.60 (+15.07%)</td><td>41.07 <b>(+57.82%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>156.86 (n/a)</td><td>148.40 (n/a)</td><td>127.40 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 <b>(-30.76%)</b></td><td>0.04 (-12.19%)</td><td>0.04 (-0.06%)</td><td>0.03 (-3.23%)</td><td>0.00 <b>(-74.47%)</b></td><td>242.30 (+3.37%)</td><td>220.00 (+10.15%)</td><td>221.40 (+0.09%)</td><td>201.60 <b>(+44.41%)</b></td><td>15.09 <b>(-61.67%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.40 (n/a)</td><td>199.72 (n/a)</td><td>221.20 (n/a)</td><td>139.60 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (+5.15%)</td><td>0.04 (-3.98%)</td><td>0.04 (+0.87%)</td><td>0.03 (-2.15%)</td><td>0.01 (-3.04%)</td><td>254.60 (+2.21%)</td><td>193.64 (+3.88%)</td><td>185.70 (-0.85%)</td><td>136.60 (-4.94%)</td><td>43.92 (-1.82%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.10 (n/a)</td><td>186.40 (n/a)</td><td>187.30 (n/a)</td><td>143.70 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (+0.79%)</td><td>0.05 (-4.56%)</td><td>0.05 (-16.69%)</td><td>0.04 (+8.84%)</td><td>0.01 <b>(-20.51%)</b></td><td>182.60 (-8.10%)</td><td>165.92 (+3.42%)</td><td>176.00 <b>(+20.05%)</b></td><td>128.40 (-0.85%)</td><td>22.12 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>160.44 (n/a)</td><td>146.60 (n/a)</td><td>129.50 (n/a)</td><td>31.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (+0.99%)</td><td>0.05 (-8.72%)</td><td>0.04 (-6.65%)</td><td>0.04 (-6.27%)</td><td>0.01 (-3.76%)</td><td>204.30 (+6.68%)</td><td>178.40 (+9.50%)</td><td>190.80 (+7.13%)</td><td>126.80 (-0.94%)</td><td>32.16 (+2.89%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.50 (n/a)</td><td>162.92 (n/a)</td><td>178.10 (n/a)</td><td>128.00 (n/a)</td><td>31.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-13.64%)</td><td>0.04 (-19.14%)</td><td>0.04 (-16.16%)</td><td>0.03 <b>(-25.22%)</b></td><td>0.01 (-15.39%)</td><td>284.60 <b>(+33.74%)</b></td><td>208.82 <b>(+24.56%)</b></td><td>232.70 (+19.27%)</td><td>130.80 (+15.85%)</td><td>63.63 <b>(+31.30%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>212.80 (n/a)</td><td>167.64 (n/a)</td><td>195.10 (n/a)</td><td>112.90 (n/a)</td><td>48.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-0.55%)</td><td>0.05 (-0.41%)</td><td>0.05 (+7.22%)</td><td>0.04 (+0.26%)</td><td>0.01 (-4.11%)</td><td>220.10 (-0.27%)</td><td>176.38 (+0.15%)</td><td>176.60 (-6.71%)</td><td>126.70 (+0.56%)</td><td>37.72 (-2.30%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>176.12 (n/a)</td><td>189.30 (n/a)</td><td>126.00 (n/a)</td><td>38.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (-17.59%)</td><td>0.04 <b>(-20.99%)</b></td><td>0.04 (-19.80%)</td><td>0.03 <b>(-26.98%)</b></td><td>0.01 (-8.15%)</td><td>275.00 <b>(+36.95%)</b></td><td>214.96 <b>(+28.32%)</b></td><td>219.80 <b>(+24.74%)</b></td><td>157.80 <b>(+21.29%)</b></td><td>52.64 <b>(+51.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>167.52 (n/a)</td><td>176.20 (n/a)</td><td>130.10 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.18 (-0.92%)</td><td>0.18 (-0.41%)</td><td>0.18 (-0.20%)</td><td>0.18 (-0.29%)</td><td>0.00 <b>(-55.70%)</b></td><td>47550.70 (+0.30%)</td><td>47448.00 (+0.41%)</td><td>47409.70 (+0.20%)</td><td>47367.40 (+0.93%)</td><td>85.59 <b>(-55.11%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47410.80 (n/a)</td><td>47253.18 (n/a)</td><td>47316.80 (n/a)</td><td>46932.30 (n/a)</td><td>190.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.21 (-12.83%)</td><td>0.18 (+12.01%)</td><td>0.18 <b>(+22.04%)</b></td><td>0.16 <b>(+23.41%)</b></td><td>0.02 <b>(-57.55%)</b></td><td>150.60 (-18.95%)</td><td>136.96 (-13.85%)</td><td>137.70 (-18.04%)</td><td>118.90 (+14.77%)</td><td>13.41 <b>(-58.39%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>185.80 (n/a)</td><td>158.98 (n/a)</td><td>168.00 (n/a)</td><td>103.60 (n/a)</td><td>32.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.33 <b>(+29.79%)</b></td><td>0.29 <b>(+23.23%)</b></td><td>0.29 (+19.98%)</td><td>0.24 (+10.40%)</td><td>0.03 <b>(+140.93%)</b></td><td>169.00 (-9.43%)</td><td>143.56 (-18.18%)</td><td>143.60 (-16.66%)</td><td>125.90 <b>(-22.95%)</b></td><td>17.38 <b>(+64.53%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>186.60 (n/a)</td><td>175.46 (n/a)</td><td>172.30 (n/a)</td><td>163.40 (n/a)</td><td>10.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (-3.79%)</td><td>0.04 <b>(+20.95%)</b></td><td>0.04 <b>(+27.50%)</b></td><td>0.03 <b>(+83.35%)</b></td><td>0.01 <b>(-49.81%)</b></td><td>169.40 <b>(-45.48%)</b></td><td>138.80 <b>(-24.66%)</b></td><td>127.30 <b>(-21.57%)</b></td><td>120.70 (+3.87%)</td><td>20.55 <b>(-72.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>310.70 (n/a)</td><td>184.22 (n/a)</td><td>162.30 (n/a)</td><td>116.20 (n/a)</td><td>75.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 <b>(+53.70%)</b></td><td>0.06 <b>(+23.64%)</b></td><td>0.05 (-7.90%)</td><td>0.05 <b>(+95.71%)</b></td><td>0.02 <b>(+23.36%)</b></td><td>179.60 <b>(-48.90%)</b></td><td>154.78 <b>(-23.32%)</b></td><td>171.40 (+8.55%)</td><td>94.40 <b>(-34.94%)</b></td><td>35.65 <b>(-59.30%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.50 (n/a)</td><td>201.86 (n/a)</td><td>157.90 (n/a)</td><td>145.10 (n/a)</td><td>87.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 (-9.09%)</td><td>0.07 (-8.68%)</td><td>0.08 (+8.25%)</td><td>0.04 (-11.40%)</td><td>0.02 (-2.29%)</td><td>273.60 (+12.87%)</td><td>189.36 (+10.71%)</td><td>162.00 (-7.64%)</td><td>139.20 (+10.04%)</td><td>56.43 <b>(+23.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>242.40 (n/a)</td><td>171.04 (n/a)</td><td>175.40 (n/a)</td><td>126.50 (n/a)</td><td>45.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 <b>(+21.69%)</b></td><td>0.05 (+10.97%)</td><td>0.05 (+12.76%)</td><td>0.04 (-0.98%)</td><td>0.01 <b>(+102.72%)</b></td><td>191.00 (+0.95%)</td><td>162.46 (-8.57%)</td><td>164.00 (-11.30%)</td><td>125.70 (-17.79%)</td><td>24.97 <b>(+66.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>177.68 (n/a)</td><td>184.90 (n/a)</td><td>152.90 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (+2.97%)</td><td>0.06 (+1.13%)</td><td>0.06 (+3.75%)</td><td>0.05 (-0.67%)</td><td>0.01 (+8.23%)</td><td>193.00 (+0.68%)</td><td>168.64 (-1.02%)</td><td>167.90 (-3.62%)</td><td>151.00 (-2.89%)</td><td>16.25 (+7.68%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>170.38 (n/a)</td><td>174.20 (n/a)</td><td>155.50 (n/a)</td><td>15.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (-19.98%)</td><td>0.05 (-9.49%)</td><td>0.05 (-2.01%)</td><td>0.04 (-10.10%)</td><td>0.01 <b>(-36.45%)</b></td><td>208.10 (+11.22%)</td><td>157.84 (+7.58%)</td><td>151.60 (+2.02%)</td><td>118.60 <b>(+24.97%)</b></td><td>33.50 (-11.88%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>146.72 (n/a)</td><td>148.60 (n/a)</td><td>94.90 (n/a)</td><td>38.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (-10.59%)</td><td>0.06 (-14.33%)</td><td>0.06 <b>(-27.18%)</b></td><td>0.04 (-0.20%)</td><td>0.01 <b>(-23.85%)</b></td><td>259.20 (+0.23%)</td><td>183.68 (+13.65%)</td><td>185.50 <b>(+37.31%)</b></td><td>137.20 (+11.91%)</td><td>48.01 (-15.64%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>258.60 (n/a)</td><td>161.62 (n/a)</td><td>135.10 (n/a)</td><td>122.60 (n/a)</td><td>56.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-18.37%)</td><td>0.05 (-2.80%)</td><td>0.05 (-2.70%)</td><td>0.05 (+8.60%)</td><td>0.00 <b>(-61.40%)</b></td><td>173.70 (-7.95%)</td><td>159.98 (+0.39%)</td><td>164.10 (+2.82%)</td><td>145.20 <b>(+22.43%)</b></td><td>12.47 <b>(-57.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>159.36 (n/a)</td><td>159.60 (n/a)</td><td>118.60 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 <b>(+29.39%)</b></td><td>0.06 (+10.02%)</td><td>0.05 (-7.45%)</td><td>0.05 (+9.57%)</td><td>0.01 <b>(+62.37%)</b></td><td>187.50 (-8.71%)</td><td>163.44 (-8.06%)</td><td>175.70 (+8.06%)</td><td>120.30 <b>(-22.74%)</b></td><td>27.20 (+11.33%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.40 (n/a)</td><td>177.76 (n/a)</td><td>162.60 (n/a)</td><td>155.70 (n/a)</td><td>24.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 <b>(-35.83%)</b></td><td>0.05 (-19.00%)</td><td>0.05 (-11.42%)</td><td>0.04 (-10.25%)</td><td>0.01 <b>(-63.56%)</b></td><td>214.30 (+11.44%)</td><td>178.34 (+18.37%)</td><td>173.90 (+12.92%)</td><td>151.90 <b>(+55.79%)</b></td><td>23.85 <b>(-35.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>192.30 (n/a)</td><td>150.66 (n/a)</td><td>154.00 (n/a)</td><td>97.50 (n/a)</td><td>36.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (+6.71%)</td><td>0.06 (+0.66%)</td><td>0.06 (+5.35%)</td><td>0.05 (+1.22%)</td><td>0.01 (+14.47%)</td><td>187.50 (-1.21%)</td><td>160.02 (-0.11%)</td><td>162.40 (-5.08%)</td><td>114.20 (-6.32%)</td><td>29.74 (+6.38%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>160.20 (n/a)</td><td>171.10 (n/a)</td><td>121.90 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (-18.60%)</td><td>0.04 <b>(-25.04%)</b></td><td>0.04 (-17.12%)</td><td>0.03 <b>(-40.75%)</b></td><td>0.01 <b>(+25.17%)</b></td><td>307.20 <b>(+68.79%)</b></td><td>228.30 <b>(+38.15%)</b></td><td>207.60 <b>(+20.63%)</b></td><td>158.10 <b>(+22.84%)</b></td><td>57.21 <b>(+165.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>165.26 (n/a)</td><td>172.10 (n/a)</td><td>128.70 (n/a)</td><td>21.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (+6.50%)</td><td>0.05 (-2.41%)</td><td>0.05 (-8.97%)</td><td>0.04 (-0.10%)</td><td>0.01 (+10.26%)</td><td>225.20 (+0.09%)</td><td>184.68 (+2.90%)</td><td>175.20 (+9.84%)</td><td>146.70 (-6.08%)</td><td>34.06 (+8.10%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>179.48 (n/a)</td><td>159.50 (n/a)</td><td>156.20 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (-1.18%)</td><td>0.05 (+12.04%)</td><td>0.05 <b>(+22.80%)</b></td><td>0.04 (+2.78%)</td><td>0.01 (-14.48%)</td><td>216.00 (-2.70%)</td><td>172.46 (-11.54%)</td><td>164.40 (-18.57%)</td><td>136.20 (+1.19%)</td><td>30.89 (-13.72%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.00 (n/a)</td><td>194.96 (n/a)</td><td>201.90 (n/a)</td><td>134.60 (n/a)</td><td>35.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (+3.45%)</td><td>0.05 (-6.93%)</td><td>0.05 (-10.74%)</td><td>0.04 (-10.62%)</td><td>0.01 <b>(+51.76%)</b></td><td>211.20 (+11.92%)</td><td>189.44 (+8.07%)</td><td>191.40 (+12.00%)</td><td>158.70 (-3.35%)</td><td>20.18 <b>(+62.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>188.70 (n/a)</td><td>175.30 (n/a)</td><td>170.90 (n/a)</td><td>164.20 (n/a)</td><td>12.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 <b>(+27.74%)</b></td><td>0.05 <b>(+28.49%)</b></td><td>0.05 <b>(+30.61%)</b></td><td>0.04 <b>(+34.91%)</b></td><td>0.01 <b>(+30.38%)</b></td><td>207.70 <b>(-25.87%)</b></td><td>172.74 <b>(-22.18%)</b></td><td>166.00 <b>(-23.47%)</b></td><td>137.60 <b>(-21.68%)</b></td><td>28.33 <b>(-24.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.20 (n/a)</td><td>221.98 (n/a)</td><td>216.90 (n/a)</td><td>175.70 (n/a)</td><td>37.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.75 (+2.43%)</td><td>0.62 (+0.30%)</td><td>0.61 (-7.97%)</td><td>0.45 (-12.06%)</td><td>0.12 <b>(+24.58%)</b></td><td>217.00 (+13.73%)</td><td>162.82 (+1.00%)</td><td>161.50 (+8.61%)</td><td>131.00 (-2.31%)</td><td>35.03 <b>(+31.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.73 (n/a)</td><td>0.62 (n/a)</td><td>0.66 (n/a)</td><td>0.52 (n/a)</td><td>0.10 (n/a)</td><td>190.80 (n/a)</td><td>161.20 (n/a)</td><td>148.70 (n/a)</td><td>134.10 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.72 (+12.48%)</td><td>0.59 (+9.34%)</td><td>0.58 (+4.22%)</td><td>0.44 (-1.42%)</td><td>0.10 <b>(+29.08%)</b></td><td>223.80 (+1.40%)</td><td>171.40 (-7.78%)</td><td>168.80 (-4.04%)</td><td>137.40 (-11.13%)</td><td>32.01 (+18.05%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.08 (n/a)</td><td>220.70 (n/a)</td><td>185.86 (n/a)</td><td>175.90 (n/a)</td><td>154.60 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.73 (-1.95%)</td><td>0.57 (-4.23%)</td><td>0.58 (-1.53%)</td><td>0.39 (-6.60%)</td><td>0.14 (+16.56%)</td><td>251.20 (+7.08%)</td><td>182.00 (+6.22%)</td><td>168.60 (+1.57%)</td><td>134.70 (+2.05%)</td><td>49.24 <b>(+24.35%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.74 (n/a)</td><td>0.60 (n/a)</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.12 (n/a)</td><td>234.60 (n/a)</td><td>171.34 (n/a)</td><td>166.00 (n/a)</td><td>132.00 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.80 <b>(+52.91%)</b></td><td>0.58 (+15.90%)</td><td>0.49 (-4.51%)</td><td>0.42 (-5.32%)</td><td>0.17 <b>(+463.52%)</b></td><td>232.20 (+5.59%)</td><td>181.34 (-8.09%)</td><td>202.50 (+4.76%)</td><td>123.50 <b>(-34.59%)</b></td><td>49.22 <b>(+279.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.52 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.45 (n/a)</td><td>0.03 (n/a)</td><td>219.90 (n/a)</td><td>197.30 (n/a)</td><td>193.30 (n/a)</td><td>188.80 (n/a)</td><td>12.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.49 (-2.31%)</td><td>0.44 (+0.09%)</td><td>0.44 (-8.69%)</td><td>0.41 (+15.34%)</td><td>0.03 <b>(-56.05%)</b></td><td>179.60 (-13.32%)</td><td>167.28 (-2.06%)</td><td>167.40 (+9.48%)</td><td>149.60 (+2.40%)</td><td>11.83 <b>(-61.04%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.48 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>207.20 (n/a)</td><td>170.80 (n/a)</td><td>152.90 (n/a)</td><td>146.10 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.52 (-13.11%)</td><td>0.44 (+8.95%)</td><td>0.44 (+4.47%)</td><td>0.32 <b>(+55.34%)</b></td><td>0.08 <b>(-46.40%)</b></td><td>229.10 <b>(-35.63%)</b></td><td>173.54 (-16.45%)</td><td>167.60 (-4.28%)</td><td>142.40 (+15.12%)</td><td>34.11 <b>(-61.69%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.60 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>355.90 (n/a)</td><td>207.72 (n/a)</td><td>175.10 (n/a)</td><td>123.70 (n/a)</td><td>89.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.59 <b>(+31.92%)</b></td><td>0.44 (+3.56%)</td><td>0.40 (-7.78%)</td><td>0.38 (+2.98%)</td><td>0.09 <b>(+183.23%)</b></td><td>193.80 (-2.91%)</td><td>172.74 (-1.26%)</td><td>185.60 (+8.41%)</td><td>124.10 <b>(-24.19%)</b></td><td>28.61 <b>(+101.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.03 (n/a)</td><td>199.60 (n/a)</td><td>174.94 (n/a)</td><td>171.20 (n/a)</td><td>163.70 (n/a)</td><td>14.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.46 (-5.38%)</td><td>0.40 (+2.12%)</td><td>0.39 (-3.53%)</td><td>0.35 (+19.99%)</td><td>0.04 <b>(-40.77%)</b></td><td>213.50 (-16.63%)</td><td>187.98 (-4.11%)</td><td>189.60 (+3.66%)</td><td>161.10 (+5.64%)</td><td>20.24 <b>(-48.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>256.10 (n/a)</td><td>196.04 (n/a)</td><td>182.90 (n/a)</td><td>152.50 (n/a)</td><td>39.44 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.71 (-5.42%)</td><td>0.67 (+0.35%)</td><td>0.68 (+4.08%)</td><td>0.62 (+10.43%)</td><td>0.04 <b>(-55.09%)</b></td><td>213.00 (-9.44%)</td><td>195.54 (-1.28%)</td><td>193.00 (-3.93%)</td><td>185.20 (+5.71%)</td><td>10.76 <b>(-56.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.65 (n/a)</td><td>0.56 (n/a)</td><td>0.08 (n/a)</td><td>235.20 (n/a)</td><td>198.08 (n/a)</td><td>200.90 (n/a)</td><td>175.20 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.70 (-4.17%)</td><td>0.63 (-5.12%)</td><td>0.62 (-9.35%)</td><td>0.56 (-7.28%)</td><td>0.06 (+18.87%)</td><td>236.00 (+7.81%)</td><td>208.00 (+5.67%)</td><td>212.60 (+10.27%)</td><td>186.00 (+4.38%)</td><td>20.09 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.74 (n/a)</td><td>0.67 (n/a)</td><td>0.68 (n/a)</td><td>0.60 (n/a)</td><td>0.05 (n/a)</td><td>218.90 (n/a)</td><td>196.84 (n/a)</td><td>192.80 (n/a)</td><td>178.20 (n/a)</td><td>15.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.79 (-0.29%)</td><td>0.64 (-7.53%)</td><td>0.62 (-9.58%)</td><td>0.54 (-11.26%)</td><td>0.09 <b>(+22.18%)</b></td><td>241.70 (+12.68%)</td><td>207.48 (+8.74%)</td><td>212.10 (+10.58%)</td><td>166.50 (+0.30%)</td><td>26.95 <b>(+34.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.61 (n/a)</td><td>0.07 (n/a)</td><td>214.50 (n/a)</td><td>190.80 (n/a)</td><td>191.80 (n/a)</td><td>166.00 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (-11.65%)</td><td>0.03 (-2.94%)</td><td>0.03 (-5.29%)</td><td>0.02 (+2.61%)</td><td>0.00 <b>(-35.58%)</b></td><td>201.40 (-2.52%)</td><td>165.02 (+1.70%)</td><td>157.70 (+5.63%)</td><td>149.90 (+13.13%)</td><td>20.90 <b>(-28.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.60 (n/a)</td><td>162.26 (n/a)</td><td>149.30 (n/a)</td><td>132.50 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (+5.02%)</td><td>0.03 (+8.68%)</td><td>0.03 <b>(+24.13%)</b></td><td>0.02 (+3.85%)</td><td>0.00 (+2.06%)</td><td>192.20 (-3.71%)</td><td>154.52 (-8.02%)</td><td>142.10 (-19.40%)</td><td>127.10 (-4.72%)</td><td>26.50 (-4.67%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.60 (n/a)</td><td>168.00 (n/a)</td><td>176.30 (n/a)</td><td>133.40 (n/a)</td><td>27.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 <b>(+27.63%)</b></td><td>0.03 (+19.89%)</td><td>0.02 (+0.52%)</td><td>0.02 <b>(+20.83%)</b></td><td>0.01 <b>(+38.38%)</b></td><td>189.70 (-17.27%)</td><td>155.94 (-16.19%)</td><td>166.90 (-0.54%)</td><td>123.20 <b>(-21.68%)</b></td><td>29.17 (-12.63%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.30 (n/a)</td><td>186.06 (n/a)</td><td>167.80 (n/a)</td><td>157.30 (n/a)</td><td>33.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 (-13.29%)</td><td>0.85 (-3.39%)</td><td>0.83 (-0.11%)</td><td>0.76 (+9.99%)</td><td>0.10 <b>(-47.62%)</b></td><td>174.10 (-9.09%)</td><td>157.54 (+0.70%)</td><td>158.40 (+0.13%)</td><td>129.10 (+15.27%)</td><td>17.68 <b>(-46.14%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.18 (n/a)</td><td>0.88 (n/a)</td><td>0.83 (n/a)</td><td>0.69 (n/a)</td><td>0.20 (n/a)</td><td>191.50 (n/a)</td><td>156.44 (n/a)</td><td>158.20 (n/a)</td><td>112.00 (n/a)</td><td>32.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.25 (+8.74%)</td><td>0.94 (+12.78%)</td><td>1.10 <b>(+42.55%)</b></td><td>0.52 (-13.74%)</td><td>0.30 <b>(+29.80%)</b></td><td>254.10 (+15.92%)</td><td>155.50 (-7.25%)</td><td>120.50 <b>(-29.86%)</b></td><td>105.80 (-8.00%)</td><td>61.81 <b>(+39.51%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.15 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.60 (n/a)</td><td>0.23 (n/a)</td><td>219.20 (n/a)</td><td>167.66 (n/a)</td><td>171.80 (n/a)</td><td>115.00 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.96 (-16.92%)</td><td>0.80 (-6.25%)</td><td>0.75 (+0.48%)</td><td>0.67 (+9.31%)</td><td>0.12 <b>(-49.66%)</b></td><td>196.60 (-8.52%)</td><td>168.14 (+2.44%)</td><td>175.50 (-0.51%)</td><td>137.70 <b>(+20.37%)</b></td><td>23.70 <b>(-43.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.15 (n/a)</td><td>0.85 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.23 (n/a)</td><td>214.90 (n/a)</td><td>164.14 (n/a)</td><td>176.40 (n/a)</td><td>114.40 (n/a)</td><td>42.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.08 <b>(+34.27%)</b></td><td>0.89 <b>(+27.91%)</b></td><td>0.84 (+17.35%)</td><td>0.79 <b>(+51.90%)</b></td><td>0.12 (+6.60%)</td><td>166.60 <b>(-34.18%)</b></td><td>150.94 <b>(-22.63%)</b></td><td>156.80 (-14.78%)</td><td>122.50 <b>(-25.53%)</b></td><td>18.58 <b>(-47.84%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.72 (n/a)</td><td>0.52 (n/a)</td><td>0.11 (n/a)</td><td>253.10 (n/a)</td><td>195.10 (n/a)</td><td>184.00 (n/a)</td><td>164.50 (n/a)</td><td>35.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.05 (-3.18%)</td><td>0.85 (+6.29%)</td><td>0.88 (+10.43%)</td><td>0.68 (+18.66%)</td><td>0.15 <b>(-21.47%)</b></td><td>193.20 (-15.71%)</td><td>159.04 (-7.63%)</td><td>150.50 (-9.45%)</td><td>125.90 (+3.28%)</td><td>27.32 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.08 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.58 (n/a)</td><td>0.19 (n/a)</td><td>229.20 (n/a)</td><td>172.18 (n/a)</td><td>166.20 (n/a)</td><td>121.90 (n/a)</td><td>39.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (+18.93%)</td><td>0.03 (+13.80%)</td><td>0.03 (+6.12%)</td><td>0.02 (+4.82%)</td><td>0.01 <b>(+77.09%)</b></td><td>193.80 (-4.58%)</td><td>155.32 (-10.49%)</td><td>159.50 (-5.79%)</td><td>121.40 (-15.93%)</td><td>30.36 <b>(+39.69%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>203.10 (n/a)</td><td>173.52 (n/a)</td><td>169.30 (n/a)</td><td>144.40 (n/a)</td><td>21.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (-12.53%)</td><td>0.03 (+7.60%)</td><td>0.03 (+14.60%)</td><td>0.02 (+19.68%)</td><td>0.01 <b>(-23.58%)</b></td><td>194.40 (-16.46%)</td><td>159.50 (-9.09%)</td><td>153.40 (-12.69%)</td><td>126.90 (+14.32%)</td><td>33.55 <b>(-22.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>175.44 (n/a)</td><td>175.70 (n/a)</td><td>111.00 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.00 (+2.27%)</td><td>0.00 (+0.48%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.77%)</td><td>1040.78 (+0.24%)</td><td>970.58 (-0.79%)</td><td>962.08 (+0.16%)</td><td>903.90 (-2.25%)</td><td>51.91 (-1.63%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1038.25 (n/a)</td><td>978.32 (n/a)</td><td>960.53 (n/a)</td><td>924.69 (n/a)</td><td>52.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.01 (-6.98%)</td><td>0.01 (-2.73%)</td><td>0.01 (-2.47%)</td><td>0.01 (+0.00%)</td><td>0.00 <b>(-51.06%)</b></td><td>1100.92 (-0.93%)</td><td>1042.36 (+2.02%)</td><td>1032.42 (+2.46%)</td><td>1021.62 (+6.95%)</td><td>33.09 <b>(-50.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1111.30 (n/a)</td><td>1021.72 (n/a)</td><td>1007.67 (n/a)</td><td>955.19 (n/a)</td><td>66.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 (+0.56%)</td><td>0.97 (-0.96%)</td><td>0.96 (-1.74%)</td><td>0.95 (-0.98%)</td><td>0.03 <b>(+32.63%)</b></td><td>2217.66 (+1.00%)</td><td>2162.70 (+1.00%)</td><td>2173.65 (+1.77%)</td><td>2064.88 (-0.56%)</td><td>63.03 <b>(+33.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.02 (n/a)</td><td>2195.72 (n/a)</td><td>2141.29 (n/a)</td><td>2135.92 (n/a)</td><td>2076.58 (n/a)</td><td>47.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.41 (+0.12%)</td><td>0.40 (+2.62%)</td><td>0.40 (+4.84%)</td><td>0.38 (+1.30%)</td><td>0.01 (-2.73%)</td><td>1374.30 (-1.29%)</td><td>1323.95 (-2.56%)</td><td>1307.23 (-4.61%)</td><td>1293.50 (-0.14%)</td><td>35.69 (-3.58%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1392.23 (n/a)</td><td>1358.80 (n/a)</td><td>1370.43 (n/a)</td><td>1295.28 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.24 (-2.20%)</td><td>0.24 (-1.87%)</td><td>0.24 (-2.65%)</td><td>0.24 (-0.63%)</td><td>0.00 <b>(-46.86%)</b></td><td>2202.82 (+0.62%)</td><td>2173.78 (+1.88%)</td><td>2165.71 (+2.74%)</td><td>2143.64 (+2.26%)</td><td>24.81 <b>(-45.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.01 (n/a)</td><td>2189.35 (n/a)</td><td>2133.58 (n/a)</td><td>2107.93 (n/a)</td><td>2096.23 (n/a)</td><td>45.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.37 (-2.25%)</td><td>0.37 (-1.00%)</td><td>0.37 (+0.63%)</td><td>0.36 (-0.22%)</td><td>0.01 <b>(-48.14%)</b></td><td>1463.57 (+0.22%)</td><td>1432.69 (+0.96%)</td><td>1432.06 (-0.64%)</td><td>1404.91 (+2.31%)</td><td>21.75 <b>(-46.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1460.31 (n/a)</td><td>1419.06 (n/a)</td><td>1441.22 (n/a)</td><td>1373.17 (n/a)</td><td>40.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.11 (-9.88%)</td><td>2.79 (+6.42%)</td><td>2.95 (+12.90%)</td><td>2.00 (-0.92%)</td><td>0.45 (-15.23%)</td><td>262.00 (+0.92%)</td><td>192.92 (-6.43%)</td><td>177.90 (-11.40%)</td><td>168.60 (+10.99%)</td><td>38.84 (-0.47%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.45 (n/a)</td><td>2.62 (n/a)</td><td>2.61 (n/a)</td><td>2.02 (n/a)</td><td>0.53 (n/a)</td><td>259.60 (n/a)</td><td>206.18 (n/a)</td><td>200.80 (n/a)</td><td>151.90 (n/a)</td><td>39.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>5.05 (-13.84%)</td><td>4.59 (-4.15%)</td><td>4.67 (-0.10%)</td><td>4.17 (+12.63%)</td><td>0.36 <b>(-55.93%)</b></td><td>251.40 (-11.20%)</td><td>229.70 (+2.40%)</td><td>224.40 (+0.09%)</td><td>207.60 (+16.04%)</td><td>17.82 <b>(-54.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>5.86 (n/a)</td><td>4.79 (n/a)</td><td>4.68 (n/a)</td><td>3.70 (n/a)</td><td>0.81 (n/a)</td><td>283.10 (n/a)</td><td>224.32 (n/a)</td><td>224.20 (n/a)</td><td>178.90 (n/a)</td><td>39.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.61 (+11.44%)</td><td>2.87 (+4.01%)</td><td>2.74 (-0.34%)</td><td>2.56 (+11.61%)</td><td>0.42 (+19.36%)</td><td>205.10 (-10.40%)</td><td>185.38 (-3.72%)</td><td>191.20 (+0.31%)</td><td>145.20 (-10.26%)</td><td>23.26 (-7.09%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:57:20</td><td>3.24 (n/a)</td><td>2.76 (n/a)</td><td>2.75 (n/a)</td><td>2.29 (n/a)</td><td>0.35 (n/a)</td><td>228.90 (n/a)</td><td>192.54 (n/a)</td><td>190.60 (n/a)</td><td>161.80 (n/a)</td><td>25.03 (n/a)</td>
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
