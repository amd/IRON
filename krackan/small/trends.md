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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 <b>(+21.13%)</b></td><td>0.07 (+12.66%)</td><td>0.07 (+6.55%)</td><td>0.05 (+0.19%)</td><td>0.01 <b>(+65.87%)</b></td><td>231.80 (-0.22%)</td><td>182.02 (-10.10%)</td><td>181.30 (-6.11%)</td><td>144.80 (-17.45%)</td><td>31.74 <b>(+37.09%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.30 (n/a)</td><td>202.46 (n/a)</td><td>193.10 (n/a)</td><td>175.40 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.12 <b>(+45.82%)</b></td><td>0.08 (+2.62%)</td><td>0.07 (-2.46%)</td><td>0.05 (-12.71%)</td><td>0.03 <b>(+177.01%)</b></td><td>247.60 (+14.58%)</td><td>180.74 (+5.66%)</td><td>172.00 (+2.50%)</td><td>100.90 <b>(-31.45%)</b></td><td>58.09 <b>(+114.32%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.10 (n/a)</td><td>171.06 (n/a)</td><td>167.80 (n/a)</td><td>147.20 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 <b>(+35.07%)</b></td><td>0.07 (-1.30%)</td><td>0.06 (-14.31%)</td><td>0.05 <b>(-23.45%)</b></td><td>0.02 <b>(+239.16%)</b></td><td>265.90 <b>(+30.66%)</b></td><td>197.46 (+8.52%)</td><td>207.80 (+16.68%)</td><td>122.00 <b>(-25.97%)</b></td><td>56.85 <b>(+225.05%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>181.96 (n/a)</td><td>178.10 (n/a)</td><td>164.80 (n/a)</td><td>17.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (+17.96%)</td><td>0.07 (+10.95%)</td><td>0.07 <b>(+20.05%)</b></td><td>0.06 (-0.18%)</td><td>0.01 <b>(+102.85%)</b></td><td>218.30 (+0.18%)</td><td>185.44 (-8.33%)</td><td>173.70 (-16.69%)</td><td>147.60 (-15.22%)</td><td>31.54 <b>(+80.84%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>202.28 (n/a)</td><td>208.50 (n/a)</td><td>174.10 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (-11.31%)</td><td>0.03 (+0.59%)</td><td>0.03 (+13.82%)</td><td>0.03 <b>(+20.34%)</b></td><td>0.01 <b>(-49.92%)</b></td><td>186.30 (-16.90%)</td><td>159.72 (-5.85%)</td><td>165.40 (-12.11%)</td><td>130.40 (+12.71%)</td><td>23.59 <b>(-51.35%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>169.64 (n/a)</td><td>188.20 (n/a)</td><td>115.70 (n/a)</td><td>48.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (+11.26%)</td><td>0.04 <b>(+22.55%)</b></td><td>0.04 <b>(+28.91%)</b></td><td>0.04 <b>(+22.19%)</b></td><td>0.00 (-18.03%)</td><td>146.20 (-18.14%)</td><td>129.62 (-18.98%)</td><td>126.80 <b>(-22.40%)</b></td><td>116.40 (-10.12%)</td><td>12.32 <b>(-40.10%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>159.98 (n/a)</td><td>163.40 (n/a)</td><td>129.50 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-16.20%)</td><td>0.03 (-10.18%)</td><td>0.03 (-2.52%)</td><td>0.03 (-7.05%)</td><td>0.00 <b>(-45.85%)</b></td><td>194.50 (+7.58%)</td><td>172.46 (+10.45%)</td><td>167.10 (+2.58%)</td><td>157.60 (+19.30%)</td><td>13.98 <b>(-28.95%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.80 (n/a)</td><td>156.14 (n/a)</td><td>162.90 (n/a)</td><td>132.10 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (+16.48%)</td><td>0.04 (+14.96%)</td><td>0.04 (+12.42%)</td><td>0.03 <b>(+39.25%)</b></td><td>0.01 (-1.39%)</td><td>186.30 <b>(-28.18%)</b></td><td>150.92 (-14.75%)</td><td>148.20 (-11.10%)</td><td>116.60 (-14.14%)</td><td>28.68 <b>(-40.93%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>259.40 (n/a)</td><td>177.04 (n/a)</td><td>166.70 (n/a)</td><td>135.80 (n/a)</td><td>48.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (-2.49%)</td><td>0.04 (+8.47%)</td><td>0.04 (+10.73%)</td><td>0.03 (+14.67%)</td><td>0.00 <b>(-39.51%)</b></td><td>168.70 (-12.77%)</td><td>148.70 (-8.86%)</td><td>146.50 (-9.68%)</td><td>137.10 (+2.54%)</td><td>12.84 <b>(-46.06%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.40 (n/a)</td><td>163.16 (n/a)</td><td>162.20 (n/a)</td><td>133.70 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-11.86%)</td><td>0.03 (+6.43%)</td><td>0.03 (+3.22%)</td><td>0.03 (+16.54%)</td><td>0.00 <b>(-47.54%)</b></td><td>204.10 (-14.17%)</td><td>178.02 (-8.74%)</td><td>183.80 (-3.16%)</td><td>157.50 (+13.47%)</td><td>20.14 <b>(-51.49%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>195.06 (n/a)</td><td>189.80 (n/a)</td><td>138.80 (n/a)</td><td>41.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (-9.49%)</td><td>0.04 (-3.91%)</td><td>0.03 (-8.90%)</td><td>0.03 (-3.39%)</td><td>0.01 <b>(-25.15%)</b></td><td>172.10 (+3.49%)</td><td>147.40 (+3.08%)</td><td>153.90 (+9.77%)</td><td>117.70 (+10.52%)</td><td>20.29 (-16.28%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>166.30 (n/a)</td><td>143.00 (n/a)</td><td>140.20 (n/a)</td><td>106.50 (n/a)</td><td>24.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-13.78%)</td><td>0.03 (-5.37%)</td><td>0.03 (+0.90%)</td><td>0.02 (-16.12%)</td><td>0.00 (-5.76%)</td><td>258.00 (+19.22%)</td><td>200.08 (+6.13%)</td><td>194.20 (-0.92%)</td><td>173.10 (+16.02%)</td><td>34.00 <b>(+35.78%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>188.52 (n/a)</td><td>196.00 (n/a)</td><td>149.20 (n/a)</td><td>25.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>173.26 (n/a)</td><td>167.80 (n/a)</td><td>150.00 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>170.80 (n/a)</td><td>144.94 (n/a)</td><td>150.50 (n/a)</td><td>112.80 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>174.32 (n/a)</td><td>182.60 (n/a)</td><td>129.80 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>174.28 (n/a)</td><td>178.40 (n/a)</td><td>129.90 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>152.30 (n/a)</td><td>132.64 (n/a)</td><td>131.40 (n/a)</td><td>119.40 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>152.40 (n/a)</td><td>141.82 (n/a)</td><td>149.10 (n/a)</td><td>109.40 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.60 (n/a)</td><td>154.48 (n/a)</td><td>154.00 (n/a)</td><td>114.10 (n/a)</td><td>37.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>169.36 (n/a)</td><td>168.90 (n/a)</td><td>150.70 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.21 (+18.45%)</td><td>3.58 (+8.29%)</td><td>3.24 (+2.23%)</td><td>2.94 (+3.97%)</td><td>0.92 <b>(+45.61%)</b></td><td>468.10 (-3.80%)</td><td>401.12 (-6.11%)</td><td>424.10 (-2.19%)</td><td>264.20 (-15.56%)</td><td>78.96 (+15.25%)</td><td>1016.13 (+18.45%)</td><td>697.46 (+8.29%)</td><td>632.91 (+2.23%)</td><td>573.49 (+3.97%)</td><td>180.08 <b>(+45.61%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.40 (n/a)</td><td>3.30 (n/a)</td><td>3.17 (n/a)</td><td>2.83 (n/a)</td><td>0.63 (n/a)</td><td>486.60 (n/a)</td><td>427.24 (n/a)</td><td>433.60 (n/a)</td><td>312.90 (n/a)</td><td>68.51 (n/a)</td><td>857.85 (n/a)</td><td>644.07 (n/a)</td><td>619.09 (n/a)</td><td>551.60 (n/a)</td><td>123.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.93 (-19.10%)</td><td>4.43 (-1.19%)</td><td>3.79 (-2.67%)</td><td>3.41 (+0.52%)</td><td>1.10 <b>(-32.17%)</b></td><td>403.80 (-0.52%)</td><td>325.52 (-1.94%)</td><td>362.80 (+2.75%)</td><td>232.10 <b>(+23.65%)</b></td><td>74.50 (-14.39%)</td><td>1156.64 (-19.10%)</td><td>863.90 (-1.19%)</td><td>739.94 (-2.67%)</td><td>664.79 (+0.52%)</td><td>215.50 <b>(-32.17%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.33 (n/a)</td><td>4.48 (n/a)</td><td>3.90 (n/a)</td><td>3.39 (n/a)</td><td>1.63 (n/a)</td><td>405.90 (n/a)</td><td>331.96 (n/a)</td><td>353.10 (n/a)</td><td>187.70 (n/a)</td><td>87.03 (n/a)</td><td>1429.77 (n/a)</td><td>874.26 (n/a)</td><td>760.22 (n/a)</td><td>661.35 (n/a)</td><td>317.72 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.75 (-18.78%)</td><td>4.22 (-10.04%)</td><td>4.04 (+3.37%)</td><td>3.48 (+1.76%)</td><td>0.90 <b>(-40.10%)</b></td><td>394.90 (-1.74%)</td><td>336.56 (+6.84%)</td><td>340.80 (-3.26%)</td><td>239.40 <b>(+23.15%)</b></td><td>60.86 <b>(-28.43%)</b></td><td>1121.26 (-18.78%)</td><td>822.83 (-10.04%)</td><td>787.66 (+3.37%)</td><td>679.70 (+1.76%)</td><td>176.28 <b>(-40.10%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.08 (n/a)</td><td>4.69 (n/a)</td><td>3.91 (n/a)</td><td>3.42 (n/a)</td><td>1.51 (n/a)</td><td>401.90 (n/a)</td><td>315.00 (n/a)</td><td>352.30 (n/a)</td><td>194.40 (n/a)</td><td>85.03 (n/a)</td><td>1380.49 (n/a)</td><td>914.66 (n/a)</td><td>761.95 (n/a)</td><td>667.93 (n/a)</td><td>294.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>6.24 (+14.40%)</td><td>4.95 <b>(+22.08%)</b></td><td>5.04 <b>(+33.82%)</b></td><td>3.69 (+4.58%)</td><td>1.21 <b>(+53.46%)</b></td><td>373.00 (-4.38%)</td><td>292.00 (-15.98%)</td><td>273.10 <b>(-25.28%)</b></td><td>220.60 (-12.60%)</td><td>73.34 <b>(+34.85%)</b></td><td>1216.85 (+14.40%)</td><td>966.41 <b>(+22.08%)</b></td><td>982.92 <b>(+33.82%)</b></td><td>719.72 (+4.58%)</td><td>235.74 <b>(+53.46%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.45 (n/a)</td><td>4.06 (n/a)</td><td>3.77 (n/a)</td><td>3.53 (n/a)</td><td>0.79 (n/a)</td><td>390.10 (n/a)</td><td>347.54 (n/a)</td><td>365.50 (n/a)</td><td>252.40 (n/a)</td><td>54.38 (n/a)</td><td>1063.70 (n/a)</td><td>791.63 (n/a)</td><td>734.52 (n/a)</td><td>688.19 (n/a)</td><td>153.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.14 (-5.76%)</td><td>3.67 (-12.10%)</td><td>3.42 (-6.41%)</td><td>3.13 (-7.03%)</td><td>0.83 (-13.21%)</td><td>439.30 (+7.57%)</td><td>387.68 (+13.01%)</td><td>402.60 (+6.85%)</td><td>268.00 (+6.14%)</td><td>68.91 (-4.73%)</td><td>1001.77 (-5.76%)</td><td>715.39 (-12.10%)</td><td>666.74 (-6.41%)</td><td>611.02 (-7.03%)</td><td>162.08 (-13.21%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.45 (n/a)</td><td>4.17 (n/a)</td><td>3.65 (n/a)</td><td>3.37 (n/a)</td><td>0.96 (n/a)</td><td>408.40 (n/a)</td><td>343.04 (n/a)</td><td>376.80 (n/a)</td><td>252.50 (n/a)</td><td>72.34 (n/a)</td><td>1063.03 (n/a)</td><td>813.90 (n/a)</td><td>712.43 (n/a)</td><td>657.24 (n/a)</td><td>186.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>2.22 (+12.63%)</td><td>1.88 (+6.90%)</td><td>1.77 (-3.59%)</td><td>1.59 (+6.70%)</td><td>0.26 <b>(+35.48%)</b></td><td>251.70 (-6.29%)</td><td>216.70 (-5.99%)</td><td>227.20 (+3.74%)</td><td>180.80 (-11.20%)</td><td>28.90 (+10.59%)</td><td>185.63 (+12.63%)</td><td>157.15 (+6.90%)</td><td>147.68 (-3.59%)</td><td>133.32 (+6.70%)</td><td>21.57 <b>(+35.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.97 (n/a)</td><td>1.76 (n/a)</td><td>1.83 (n/a)</td><td>1.49 (n/a)</td><td>0.19 (n/a)</td><td>268.60 (n/a)</td><td>230.50 (n/a)</td><td>219.00 (n/a)</td><td>203.60 (n/a)</td><td>26.13 (n/a)</td><td>164.81 (n/a)</td><td>147.01 (n/a)</td><td>153.19 (n/a)</td><td>124.95 (n/a)</td><td>15.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>8.00 (+13.10%)</td><td>6.35 (+15.42%)</td><td>6.92 <b>(+33.46%)</b></td><td>4.50 (-4.12%)</td><td>1.46 <b>(+60.30%)</b></td><td>429.20 (+4.28%)</td><td>318.96 (-10.93%)</td><td>279.30 <b>(-25.06%)</b></td><td>241.70 (-11.56%)</td><td>79.59 <b>(+55.14%)</b></td><td>1666.06 (+13.10%)</td><td>1322.81 (+15.42%)</td><td>1441.69 <b>(+33.46%)</b></td><td>938.07 (-4.12%)</td><td>305.04 <b>(+60.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.07 (n/a)</td><td>5.50 (n/a)</td><td>5.19 (n/a)</td><td>4.70 (n/a)</td><td>0.91 (n/a)</td><td>411.60 (n/a)</td><td>358.10 (n/a)</td><td>372.70 (n/a)</td><td>273.30 (n/a)</td><td>51.30 (n/a)</td><td>1473.09 (n/a)</td><td>1146.08 (n/a)</td><td>1080.23 (n/a)</td><td>978.35 (n/a)</td><td>190.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>19.61 (+18.93%)</td><td>14.00 (+4.63%)</td><td>12.66 (-0.47%)</td><td>12.09 (+1.50%)</td><td>3.17 <b>(+71.11%)</b></td><td>455.50 (-1.47%)</td><td>406.28 (-2.62%)</td><td>434.90 (+0.46%)</td><td>280.70 (-15.93%)</td><td>71.58 <b>(+39.74%)</b></td><td>7650.08 (+18.93%)</td><td>5459.41 (+4.63%)</td><td>4937.45 (-0.47%)</td><td>4714.90 (+1.50%)</td><td>1234.85 <b>(+71.11%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>16.49 (n/a)</td><td>13.38 (n/a)</td><td>12.72 (n/a)</td><td>11.91 (n/a)</td><td>1.85 (n/a)</td><td>462.30 (n/a)</td><td>417.22 (n/a)</td><td>432.90 (n/a)</td><td>333.90 (n/a)</td><td>51.23 (n/a)</td><td>6432.38 (n/a)</td><td>5217.96 (n/a)</td><td>4960.76 (n/a)</td><td>4645.13 (n/a)</td><td>721.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>176.18 (n/a)</td><td>163.70 (n/a)</td><td>131.40 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.80 (n/a)</td><td>189.48 (n/a)</td><td>183.50 (n/a)</td><td>138.60 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>338.40 (n/a)</td><td>211.54 (n/a)</td><td>190.60 (n/a)</td><td>153.20 (n/a)</td><td>75.27 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>340.10 (n/a)</td><td>210.22 (n/a)</td><td>189.70 (n/a)</td><td>118.60 (n/a)</td><td>82.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.70 (n/a)</td><td>181.58 (n/a)</td><td>185.00 (n/a)</td><td>161.40 (n/a)</td><td>11.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>174.68 (n/a)</td><td>164.50 (n/a)</td><td>138.90 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>215.70 (n/a)</td><td>185.44 (n/a)</td><td>182.90 (n/a)</td><td>166.40 (n/a)</td><td>19.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.90 (n/a)</td><td>238.46 (n/a)</td><td>220.70 (n/a)</td><td>193.80 (n/a)</td><td>51.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.78 (+15.21%)</td><td>4.30 (+7.87%)</td><td>4.20 (+1.98%)</td><td>4.12 (+15.83%)</td><td>0.27 (+8.93%)</td><td>2281.20 (-13.66%)</td><td>2191.96 (-7.34%)</td><td>2241.40 (-1.94%)</td><td>1967.40 (-13.20%)</td><td>128.14 (-19.38%)</td><td>1880.31 (+15.21%)</td><td>1692.68 (+7.87%)</td><td>1650.44 (+1.98%)</td><td>1621.71 (+15.83%)</td><td>106.57 (+8.93%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.15 (n/a)</td><td>3.99 (n/a)</td><td>4.11 (n/a)</td><td>3.56 (n/a)</td><td>0.25 (n/a)</td><td>2642.10 (n/a)</td><td>2365.48 (n/a)</td><td>2285.80 (n/a)</td><td>2266.60 (n/a)</td><td>158.95 (n/a)</td><td>1632.14 (n/a)</td><td>1569.15 (n/a)</td><td>1618.40 (n/a)</td><td>1400.14 (n/a)</td><td>97.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.21 (+5.15%)</td><td>1.02 (+3.93%)</td><td>1.09 (+13.07%)</td><td>0.70 (-11.82%)</td><td>0.20 <b>(+40.77%)</b></td><td>315.40 (+13.37%)</td><td>225.68 (-1.87%)</td><td>203.40 (-11.57%)</td><td>182.20 (-4.91%)</td><td>52.82 <b>(+57.14%)</b></td><td>51.79 (+5.15%)</td><td>43.37 (+3.93%)</td><td>46.39 (+13.07%)</td><td>29.92 (-11.82%)</td><td>8.40 <b>(+40.77%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.15 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.80 (n/a)</td><td>0.14 (n/a)</td><td>278.20 (n/a)</td><td>229.98 (n/a)</td><td>230.00 (n/a)</td><td>191.60 (n/a)</td><td>33.62 (n/a)</td><td>49.26 (n/a)</td><td>41.73 (n/a)</td><td>41.02 (n/a)</td><td>33.93 (n/a)</td><td>5.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.23 (+6.32%)</td><td>1.06 (+7.31%)</td><td>1.12 (+9.77%)</td><td>0.71 (-6.02%)</td><td>0.21 <b>(+30.63%)</b></td><td>312.40 (+6.40%)</td><td>216.26 (-5.22%)</td><td>198.20 (-8.92%)</td><td>180.00 (-5.96%)</td><td>54.65 <b>(+34.13%)</b></td><td>52.42 (+6.32%)</td><td>45.42 (+7.31%)</td><td>47.61 (+9.77%)</td><td>30.21 (-6.02%)</td><td>8.87 <b>(+30.63%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.16 (n/a)</td><td>0.99 (n/a)</td><td>1.02 (n/a)</td><td>0.75 (n/a)</td><td>0.16 (n/a)</td><td>293.60 (n/a)</td><td>228.18 (n/a)</td><td>217.60 (n/a)</td><td>191.40 (n/a)</td><td>40.75 (n/a)</td><td>49.30 (n/a)</td><td>42.32 (n/a)</td><td>43.37 (n/a)</td><td>32.14 (n/a)</td><td>6.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.53 (-0.02%)</td><td>0.53 (-0.05%)</td><td>0.53 (-0.08%)</td><td>0.53 (-0.05%)</td><td>0.00 (+9.79%)</td><td>47897.20 (+0.05%)</td><td>47826.26 (+0.05%)</td><td>47828.70 (+0.08%)</td><td>47777.90 (+0.02%)</td><td>46.10 (+9.81%)</td><td>359.58 (-0.02%)</td><td>359.21 (-0.05%)</td><td>359.20 (-0.08%)</td><td>358.68 (-0.05%)</td><td>0.35 (+9.79%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47873.50 (n/a)</td><td>47800.64 (n/a)</td><td>47791.90 (n/a)</td><td>47768.10 (n/a)</td><td>41.98 (n/a)</td><td>359.65 (n/a)</td><td>359.41 (n/a)</td><td>359.47 (n/a)</td><td>358.86 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.90 (-0.07%)</td><td>0.90 (-0.06%)</td><td>0.90 (-0.17%)</td><td>0.90 (+0.21%)</td><td>0.00 <b>(-36.03%)</b></td><td>28028.50 (-0.21%)</td><td>27932.50 (+0.06%)</td><td>27928.30 (+0.17%)</td><td>27860.50 (+0.07%)</td><td>62.27 <b>(-36.14%)</b></td><td>616.64 (-0.07%)</td><td>615.05 (-0.06%)</td><td>615.14 (-0.17%)</td><td>612.94 (+0.21%)</td><td>1.37 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28086.80 (n/a)</td><td>27917.04 (n/a)</td><td>27881.50 (n/a)</td><td>27841.70 (n/a)</td><td>97.51 (n/a)</td><td>617.05 (n/a)</td><td>615.40 (n/a)</td><td>616.18 (n/a)</td><td>611.67 (n/a)</td><td>2.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.32 (-0.20%)</td><td>3.23 (-0.32%)</td><td>3.18 (-2.40%)</td><td>3.16 (+0.93%)</td><td>0.08 (-6.57%)</td><td>7961.40 (-0.92%)</td><td>7796.64 (+0.31%)</td><td>7916.50 (+2.46%)</td><td>7582.60 (+0.20%)</td><td>193.82 (-7.33%)</td><td>2265.70 (-0.20%)</td><td>2204.60 (-0.32%)</td><td>2170.15 (-2.40%)</td><td>2157.90 (+0.93%)</td><td>55.28 (-6.57%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.33 (n/a)</td><td>3.24 (n/a)</td><td>3.26 (n/a)</td><td>3.13 (n/a)</td><td>0.09 (n/a)</td><td>8035.70 (n/a)</td><td>7772.30 (n/a)</td><td>7726.60 (n/a)</td><td>7567.70 (n/a)</td><td>209.15 (n/a)</td><td>2270.15 (n/a)</td><td>2211.67 (n/a)</td><td>2223.47 (n/a)</td><td>2137.95 (n/a)</td><td>59.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.23 (-1.84%)</td><td>3.84 (+3.41%)</td><td>3.75 (+3.67%)</td><td>3.66 (+18.28%)</td><td>0.23 <b>(-58.72%)</b></td><td>2200.70 (-15.45%)</td><td>2106.52 (-4.75%)</td><td>2146.80 (-3.54%)</td><td>1904.90 (+1.87%)</td><td>117.38 <b>(-64.19%)</b></td><td>1109.71 (-1.84%)</td><td>1006.17 (+3.41%)</td><td>984.67 (+3.67%)</td><td>960.59 (+18.28%)</td><td>59.77 <b>(-58.72%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>4.31 (n/a)</td><td>3.71 (n/a)</td><td>3.62 (n/a)</td><td>3.10 (n/a)</td><td>0.55 (n/a)</td><td>2602.90 (n/a)</td><td>2211.46 (n/a)</td><td>2225.70 (n/a)</td><td>1869.90 (n/a)</td><td>327.81 (n/a)</td><td>1130.48 (n/a)</td><td>973.01 (n/a)</td><td>949.77 (n/a)</td><td>812.16 (n/a)</td><td>144.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.51 <b>(+45.23%)</b></td><td>0.40 <b>(+24.42%)</b></td><td>0.36 (+7.12%)</td><td>0.33 (+11.43%)</td><td>0.09 <b>(+256.05%)</b></td><td>3803.20 (-10.26%)</td><td>3210.22 (-16.95%)</td><td>3488.50 (-6.65%)</td><td>2422.90 <b>(-31.14%)</b></td><td>667.23 <b>(+118.85%)</b></td><td>27.70 <b>(+45.23%)</b></td><td>21.71 <b>(+24.42%)</b></td><td>19.24 (+7.12%)</td><td>17.65 (+11.43%)</td><td>4.84 <b>(+256.04%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>4237.90 (n/a)</td><td>3865.36 (n/a)</td><td>3736.90 (n/a)</td><td>3518.60 (n/a)</td><td>304.88 (n/a)</td><td>19.07 (n/a)</td><td>17.45 (n/a)</td><td>17.96 (n/a)</td><td>15.84 (n/a)</td><td>1.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>6.40 <b>(+25.94%)</b></td><td>4.92 (+16.36%)</td><td>4.88 (+3.49%)</td><td>3.40 (+9.36%)</td><td>1.07 (+19.34%)</td><td>1959.10 (-8.56%)</td><td>1409.72 (-13.93%)</td><td>1363.50 (-3.37%)</td><td>1039.20 <b>(-20.61%)</b></td><td>336.22 (-10.89%)</td><td>1977.61 <b>(+25.94%)</b></td><td>1519.08 (+16.36%)</td><td>1507.28 (+3.48%)</td><td>1049.05 (+9.36%)</td><td>329.53 (+19.34%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.08 (n/a)</td><td>4.23 (n/a)</td><td>4.71 (n/a)</td><td>3.10 (n/a)</td><td>0.89 (n/a)</td><td>2142.40 (n/a)</td><td>1637.90 (n/a)</td><td>1411.00 (n/a)</td><td>1308.90 (n/a)</td><td>377.32 (n/a)</td><td>1570.23 (n/a)</td><td>1305.50 (n/a)</td><td>1456.52 (n/a)</td><td>959.29 (n/a)</td><td>276.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.53 (n/a)</td><td>12.65 (n/a)</td><td>12.79 (n/a)</td><td>11.51 (n/a)</td><td>0.81 (n/a)</td><td>13.52 (n/a)</td><td>12.64 (n/a)</td><td>12.78 (n/a)</td><td>11.50 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>24.98 (-1.72%)</td><td>24.58 (+6.96%)</td><td>24.69 (+2.34%)</td><td>23.87 <b>(+41.20%)</b></td><td>0.42 <b>(-87.82%)</b></td><td>24.96 (-1.72%)</td><td>24.57 (+6.96%)</td><td>24.67 (+2.34%)</td><td>23.85 <b>(+41.20%)</b></td><td>0.42 <b>(-87.82%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>25.42 (n/a)</td><td>22.98 (n/a)</td><td>24.13 (n/a)</td><td>16.90 (n/a)</td><td>3.44 (n/a)</td><td>25.40 (n/a)</td><td>22.97 (n/a)</td><td>24.11 (n/a)</td><td>16.89 (n/a)</td><td>3.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>41.44 (+1.66%)</td><td>40.64 (+1.90%)</td><td>40.25 (+1.39%)</td><td>39.97 (+2.21%)</td><td>0.71 (-8.22%)</td><td>41.41 (+1.66%)</td><td>40.61 (+1.90%)</td><td>40.23 (+1.39%)</td><td>39.95 (+2.21%)</td><td>0.71 (-8.22%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>40.76 (n/a)</td><td>39.88 (n/a)</td><td>39.70 (n/a)</td><td>39.10 (n/a)</td><td>0.77 (n/a)</td><td>40.74 (n/a)</td><td>39.85 (n/a)</td><td>39.68 (n/a)</td><td>39.08 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>44.98 (+3.94%)</td><td>40.74 (-3.99%)</td><td>44.41 (+4.95%)</td><td>27.98 <b>(-32.02%)</b></td><td>7.25 <b>(+735.86%)</b></td><td>44.95 (+3.94%)</td><td>40.71 (-3.99%)</td><td>44.38 (+4.95%)</td><td>27.96 <b>(-32.02%)</b></td><td>7.25 <b>(+735.86%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>43.27 (n/a)</td><td>42.43 (n/a)</td><td>42.31 (n/a)</td><td>41.16 (n/a)</td><td>0.87 (n/a)</td><td>43.24 (n/a)</td><td>42.41 (n/a)</td><td>42.29 (n/a)</td><td>41.13 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.45 (n/a)</td><td>12.60 (n/a)</td><td>12.55 (n/a)</td><td>11.87 (n/a)</td><td>0.56 (n/a)</td><td>13.44 (n/a)</td><td>12.59 (n/a)</td><td>12.54 (n/a)</td><td>11.86 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>25.30 (+3.44%)</td><td>24.43 (+2.39%)</td><td>24.42 (+1.20%)</td><td>23.95 (+7.33%)</td><td>0.54 <b>(-38.37%)</b></td><td>25.28 (+3.44%)</td><td>24.41 (+2.39%)</td><td>24.41 (+1.20%)</td><td>23.93 (+7.33%)</td><td>0.54 <b>(-38.37%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>24.46 (n/a)</td><td>23.86 (n/a)</td><td>24.13 (n/a)</td><td>22.31 (n/a)</td><td>0.88 (n/a)</td><td>24.44 (n/a)</td><td>23.84 (n/a)</td><td>24.12 (n/a)</td><td>22.30 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>41.71 (-0.10%)</td><td>38.95 (-1.87%)</td><td>39.64 (-1.91%)</td><td>34.16 (-8.91%)</td><td>3.07 <b>(+60.47%)</b></td><td>41.68 (-0.10%)</td><td>38.93 (-1.87%)</td><td>39.62 (-1.91%)</td><td>34.14 (-8.91%)</td><td>3.07 <b>(+60.47%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>41.75 (n/a)</td><td>39.69 (n/a)</td><td>40.42 (n/a)</td><td>37.50 (n/a)</td><td>1.91 (n/a)</td><td>41.73 (n/a)</td><td>39.67 (n/a)</td><td>40.39 (n/a)</td><td>37.47 (n/a)</td><td>1.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>47.46 (+8.52%)</td><td>44.74 (+6.01%)</td><td>44.17 (+5.51%)</td><td>43.29 (+3.91%)</td><td>1.65 <b>(+89.74%)</b></td><td>47.44 (+8.52%)</td><td>44.71 (+6.01%)</td><td>44.14 (+5.51%)</td><td>43.27 (+3.91%)</td><td>1.65 <b>(+89.74%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>43.74 (n/a)</td><td>42.20 (n/a)</td><td>41.86 (n/a)</td><td>41.66 (n/a)</td><td>0.87 (n/a)</td><td>43.71 (n/a)</td><td>42.17 (n/a)</td><td>41.83 (n/a)</td><td>41.64 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>9.99 (+14.66%)</td><td>8.94 (+5.26%)</td><td>8.80 (+1.38%)</td><td>8.41 (+7.12%)</td><td>0.61 <b>(+66.19%)</b></td><td>9.97 (+14.66%)</td><td>8.93 (+5.26%)</td><td>8.79 (+1.38%)</td><td>8.39 (+7.12%)</td><td>0.61 <b>(+66.19%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>8.71 (n/a)</td><td>8.50 (n/a)</td><td>8.68 (n/a)</td><td>7.85 (n/a)</td><td>0.37 (n/a)</td><td>8.70 (n/a)</td><td>8.48 (n/a)</td><td>8.67 (n/a)</td><td>7.83 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.02 (-7.46%)</td><td>0.89 (-4.60%)</td><td>0.86 (-8.54%)</td><td>0.82 (+9.42%)</td><td>0.08 <b>(-37.07%)</b></td><td>1.00 (-7.46%)</td><td>0.88 (-4.60%)</td><td>0.85 (-8.54%)</td><td>0.80 (+9.42%)</td><td>0.08 <b>(-37.07%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.10 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.75 (n/a)</td><td>0.13 (n/a)</td><td>1.08 (n/a)</td><td>0.92 (n/a)</td><td>0.93 (n/a)</td><td>0.73 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.26 (+4.56%)</td><td>1.15 (+11.12%)</td><td>1.14 (+12.43%)</td><td>1.03 (+8.75%)</td><td>0.11 (+3.49%)</td><td>1.25 (+4.56%)</td><td>1.13 (+11.12%)</td><td>1.12 (+12.43%)</td><td>1.01 (+8.75%)</td><td>0.11 (+3.49%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.21 (n/a)</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>0.94 (n/a)</td><td>0.10 (n/a)</td><td>1.20 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>0.93 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>19.95 (+12.84%)</td><td>17.56 (+7.82%)</td><td>17.11 (+7.55%)</td><td>15.74 (+4.20%)</td><td>1.65 <b>(+58.74%)</b></td><td>19.72 (+12.84%)</td><td>17.35 (+7.82%)</td><td>16.91 (+7.55%)</td><td>15.56 (+4.20%)</td><td>1.63 <b>(+58.74%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>17.68 (n/a)</td><td>16.28 (n/a)</td><td>15.91 (n/a)</td><td>15.11 (n/a)</td><td>1.04 (n/a)</td><td>17.48 (n/a)</td><td>16.09 (n/a)</td><td>15.73 (n/a)</td><td>14.93 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.88 (+3.45%)</td><td>13.21 (+8.20%)</td><td>13.33 (+1.55%)</td><td>12.00 <b>(+48.19%)</b></td><td>0.75 <b>(-67.49%)</b></td><td>13.64 (+3.45%)</td><td>12.97 (+8.20%)</td><td>13.10 (+1.55%)</td><td>11.79 <b>(+48.19%)</b></td><td>0.73 <b>(-67.49%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>13.42 (n/a)</td><td>12.20 (n/a)</td><td>13.13 (n/a)</td><td>8.09 (n/a)</td><td>2.30 (n/a)</td><td>13.18 (n/a)</td><td>11.99 (n/a)</td><td>12.90 (n/a)</td><td>7.95 (n/a)</td><td>2.26 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>8.81 (+12.70%)</td><td>7.74 (+5.31%)</td><td>7.57 (-0.63%)</td><td>6.97 (+4.56%)</td><td>0.67 <b>(+31.29%)</b></td><td>8.66 (+12.70%)</td><td>7.60 (+5.31%)</td><td>7.44 (-0.63%)</td><td>6.85 (+4.56%)</td><td>0.66 <b>(+31.29%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.82 (n/a)</td><td>7.35 (n/a)</td><td>7.62 (n/a)</td><td>6.67 (n/a)</td><td>0.51 (n/a)</td><td>7.68 (n/a)</td><td>7.22 (n/a)</td><td>7.48 (n/a)</td><td>6.55 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.86 (-16.26%)</td><td>5.28 (-11.45%)</td><td>5.23 (-9.15%)</td><td>4.50 (-17.37%)</td><td>0.52 (-18.17%)</td><td>5.77 (-16.26%)</td><td>5.20 (-11.45%)</td><td>5.14 (-9.15%)</td><td>4.43 (-17.37%)</td><td>0.51 (-18.17%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>7.00 (n/a)</td><td>5.97 (n/a)</td><td>5.76 (n/a)</td><td>5.45 (n/a)</td><td>0.63 (n/a)</td><td>6.89 (n/a)</td><td>5.87 (n/a)</td><td>5.66 (n/a)</td><td>5.36 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.22 (n/a)</td><td>12.41 (n/a)</td><td>12.62 (n/a)</td><td>11.19 (n/a)</td><td>0.87 (n/a)</td><td>13.21 (n/a)</td><td>12.40 (n/a)</td><td>12.61 (n/a)</td><td>11.19 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.25 (n/a)</td><td>12.30 (n/a)</td><td>12.49 (n/a)</td><td>10.43 (n/a)</td><td>1.15 (n/a)</td><td>13.24 (n/a)</td><td>12.29 (n/a)</td><td>12.48 (n/a)</td><td>10.42 (n/a)</td><td>1.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>159.22 (n/a)</td><td>154.70 (n/a)</td><td>127.50 (n/a)</td><td>28.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.50 (n/a)</td><td>160.38 (n/a)</td><td>162.90 (n/a)</td><td>134.10 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>192.60 (n/a)</td><td>196.10 (n/a)</td><td>150.00 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>168.48 (n/a)</td><td>170.20 (n/a)</td><td>126.60 (n/a)</td><td>30.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>168.96 (n/a)</td><td>157.70 (n/a)</td><td>133.40 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>225.80 (n/a)</td><td>171.32 (n/a)</td><td>188.10 (n/a)</td><td>78.70 (n/a)</td><td>56.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>166.52 (n/a)</td><td>158.70 (n/a)</td><td>145.00 (n/a)</td><td>23.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.00 (n/a)</td><td>213.88 (n/a)</td><td>199.20 (n/a)</td><td>165.10 (n/a)</td><td>41.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 <b>(+24.43%)</b></td><td>0.06 (+13.39%)</td><td>0.05 (-0.02%)</td><td>0.04 (+4.52%)</td><td>0.01 <b>(+99.90%)</b></td><td>189.20 (-4.35%)</td><td>146.90 (-8.96%)</td><td>155.50 (+0.00%)</td><td>109.20 (-19.59%)</td><td>35.26 <b>(+46.00%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.80 (n/a)</td><td>161.36 (n/a)</td><td>155.50 (n/a)</td><td>135.80 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+37.72%)</b></td><td>0.06 (+17.86%)</td><td>0.05 (+8.12%)</td><td>0.05 (+19.05%)</td><td>0.01 <b>(+89.79%)</b></td><td>181.40 (-15.98%)</td><td>152.50 (-14.09%)</td><td>156.80 (-7.49%)</td><td>115.90 <b>(-27.43%)</b></td><td>25.03 (+11.96%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>177.52 (n/a)</td><td>169.50 (n/a)</td><td>159.70 (n/a)</td><td>22.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (+6.44%)</td><td>0.06 (-2.85%)</td><td>0.05 (-7.04%)</td><td>0.05 (-2.94%)</td><td>0.01 <b>(+51.70%)</b></td><td>169.30 (+3.04%)</td><td>147.46 (+3.77%)</td><td>152.30 (+7.56%)</td><td>120.80 (-6.07%)</td><td>19.73 <b>(+44.80%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>164.30 (n/a)</td><td>142.10 (n/a)</td><td>141.60 (n/a)</td><td>128.60 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+47.13%)</b></td><td>0.06 <b>(+26.33%)</b></td><td>0.05 (+12.41%)</td><td>0.05 <b>(+31.72%)</b></td><td>0.01 <b>(+64.25%)</b></td><td>175.30 <b>(-24.08%)</b></td><td>150.44 <b>(-20.41%)</b></td><td>153.70 (-11.05%)</td><td>115.10 <b>(-32.05%)</b></td><td>22.66 (-15.96%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>189.02 (n/a)</td><td>172.80 (n/a)</td><td>169.40 (n/a)</td><td>26.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+21.35%)</b></td><td>0.06 (+9.84%)</td><td>0.06 (+16.75%)</td><td>0.04 (-13.44%)</td><td>0.01 <b>(+124.84%)</b></td><td>217.00 (+15.55%)</td><td>153.36 (-4.84%)</td><td>137.00 (-14.32%)</td><td>113.90 (-17.58%)</td><td>42.58 <b>(+114.81%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>161.16 (n/a)</td><td>159.90 (n/a)</td><td>138.20 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (-4.54%)</td><td>0.05 (-12.02%)</td><td>0.05 (-17.47%)</td><td>0.04 (-7.88%)</td><td>0.01 (-11.71%)</td><td>190.10 (+8.57%)</td><td>155.86 (+13.39%)</td><td>154.30 <b>(+21.21%)</b></td><td>125.70 (+4.75%)</td><td>22.99 (+0.41%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.10 (n/a)</td><td>137.46 (n/a)</td><td>127.30 (n/a)</td><td>120.00 (n/a)</td><td>22.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+23.33%)</b></td><td>0.06 <b>(+21.96%)</b></td><td>0.05 (+9.67%)</td><td>0.04 (+13.34%)</td><td>0.01 <b>(+52.95%)</b></td><td>186.90 (-11.76%)</td><td>145.94 (-16.85%)</td><td>156.10 (-8.82%)</td><td>112.00 (-18.96%)</td><td>31.36 (+4.66%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.80 (n/a)</td><td>175.52 (n/a)</td><td>171.20 (n/a)</td><td>138.20 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+47.85%)</b></td><td>0.05 <b>(+23.88%)</b></td><td>0.05 (+19.22%)</td><td>0.05 (+12.31%)</td><td>0.01 <b>(+281.26%)</b></td><td>180.50 (-10.95%)</td><td>157.52 (-17.78%)</td><td>161.10 (-16.09%)</td><td>119.40 <b>(-32.39%)</b></td><td>23.57 <b>(+124.44%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.70 (n/a)</td><td>191.58 (n/a)</td><td>192.00 (n/a)</td><td>176.60 (n/a)</td><td>10.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (+15.18%)</td><td>0.05 <b>(+24.22%)</b></td><td>0.05 (+9.69%)</td><td>0.04 <b>(+36.79%)</b></td><td>0.01 <b>(-20.19%)</b></td><td>220.60 <b>(-26.91%)</b></td><td>169.74 <b>(-23.17%)</b></td><td>163.20 (-8.83%)</td><td>134.00 (-13.21%)</td><td>33.97 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.80 (n/a)</td><td>220.92 (n/a)</td><td>179.00 (n/a)</td><td>154.40 (n/a)</td><td>70.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 <b>(+22.41%)</b></td><td>0.04 (+15.95%)</td><td>0.04 (+19.70%)</td><td>0.03 (+0.20%)</td><td>0.01 <b>(+107.32%)</b></td><td>240.80 (-0.17%)</td><td>195.16 (-12.81%)</td><td>188.30 (-16.46%)</td><td>165.20 (-18.30%)</td><td>27.86 <b>(+72.75%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>241.20 (n/a)</td><td>223.84 (n/a)</td><td>225.40 (n/a)</td><td>202.20 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+22.36%)</b></td><td>0.05 (+18.44%)</td><td>0.05 (+19.59%)</td><td>0.05 <b>(+23.39%)</b></td><td>0.01 (+11.45%)</td><td>178.90 (-18.98%)</td><td>154.50 (-16.18%)</td><td>158.90 (-16.41%)</td><td>112.10 (-18.29%)</td><td>25.13 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.80 (n/a)</td><td>184.32 (n/a)</td><td>190.10 (n/a)</td><td>137.20 (n/a)</td><td>35.95 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 <b>(+31.97%)</b></td><td>0.04 (+9.80%)</td><td>0.04 (+4.04%)</td><td>0.03 (-6.20%)</td><td>0.01 <b>(+239.61%)</b></td><td>254.10 (+6.59%)</td><td>209.40 (-6.68%)</td><td>215.40 (-3.88%)</td><td>155.60 <b>(-24.21%)</b></td><td>37.02 <b>(+166.98%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>238.40 (n/a)</td><td>224.38 (n/a)</td><td>224.10 (n/a)</td><td>205.30 (n/a)</td><td>13.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 <b>(+33.01%)</b></td><td>0.05 <b>(+24.44%)</b></td><td>0.05 (+5.18%)</td><td>0.04 <b>(+41.03%)</b></td><td>0.01 (+10.62%)</td><td>190.60 <b>(-29.09%)</b></td><td>155.32 <b>(-20.96%)</b></td><td>160.80 (-4.91%)</td><td>113.80 <b>(-24.83%)</b></td><td>27.68 <b>(-43.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.80 (n/a)</td><td>196.52 (n/a)</td><td>169.10 (n/a)</td><td>151.40 (n/a)</td><td>48.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 <b>(+54.15%)</b></td><td>0.06 <b>(+27.57%)</b></td><td>0.06 <b>(+32.30%)</b></td><td>0.03 <b>(-32.48%)</b></td><td>0.02 <b>(+322.00%)</b></td><td>313.60 <b>(+48.13%)</b></td><td>169.16 (-10.07%)</td><td>138.10 <b>(-24.41%)</b></td><td>104.50 <b>(-35.13%)</b></td><td>84.26 <b>(+324.13%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>188.10 (n/a)</td><td>182.70 (n/a)</td><td>161.10 (n/a)</td><td>19.87 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (+6.74%)</td><td>0.06 <b>(+24.96%)</b></td><td>0.05 <b>(+20.85%)</b></td><td>0.05 <b>(+55.16%)</b></td><td>0.01 <b>(-32.22%)</b></td><td>168.50 <b>(-35.56%)</b></td><td>147.24 <b>(-23.67%)</b></td><td>155.00 (-17.29%)</td><td>116.40 (-6.36%)</td><td>22.04 <b>(-58.90%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.50 (n/a)</td><td>192.90 (n/a)</td><td>187.40 (n/a)</td><td>124.30 (n/a)</td><td>53.62 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (+18.44%)</td><td>0.06 (+11.52%)</td><td>0.05 (-1.12%)</td><td>0.04 (+2.74%)</td><td>0.02 <b>(+48.19%)</b></td><td>210.60 (-2.64%)</td><td>159.82 (-7.23%)</td><td>175.80 (+1.15%)</td><td>99.10 (-15.52%)</td><td>45.18 <b>(+24.96%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.30 (n/a)</td><td>172.28 (n/a)</td><td>173.80 (n/a)</td><td>117.30 (n/a)</td><td>36.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (+0.72%)</td><td>0.05 (+4.82%)</td><td>0.05 (+18.21%)</td><td>0.04 (+3.60%)</td><td>0.01 (-7.28%)</td><td>212.80 (-3.49%)</td><td>182.26 (-4.93%)</td><td>174.70 (-15.40%)</td><td>148.10 (-0.74%)</td><td>27.13 (-9.27%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>191.72 (n/a)</td><td>206.50 (n/a)</td><td>149.20 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (+11.32%)</td><td>0.04 (+6.51%)</td><td>0.04 (+0.50%)</td><td>0.03 <b>(+24.37%)</b></td><td>0.01 (-10.94%)</td><td>252.80 (-19.59%)</td><td>192.04 (-8.16%)</td><td>189.20 (-0.53%)</td><td>152.50 (-10.19%)</td><td>38.19 <b>(-36.46%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.40 (n/a)</td><td>209.10 (n/a)</td><td>190.20 (n/a)</td><td>169.80 (n/a)</td><td>60.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.18 (-0.99%)</td><td>0.18 (-0.31%)</td><td>0.18 (-0.27%)</td><td>0.18 (-0.06%)</td><td>0.00 <b>(-67.11%)</b></td><td>47619.30 (+0.06%)</td><td>47537.18 (+0.31%)</td><td>47576.90 (+0.27%)</td><td>47434.30 (+1.00%)</td><td>83.32 <b>(-66.75%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47590.50 (n/a)</td><td>47391.48 (n/a)</td><td>47446.60 (n/a)</td><td>46966.80 (n/a)</td><td>250.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.19 (+7.92%)</td><td>0.15 (-0.92%)</td><td>0.14 (-13.22%)</td><td>0.12 (-0.03%)</td><td>0.03 <b>(+41.44%)</b></td><td>208.90 (+0.05%)</td><td>165.36 (+2.47%)</td><td>172.70 (+15.21%)</td><td>127.70 (-7.33%)</td><td>34.28 <b>(+23.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>161.38 (n/a)</td><td>149.90 (n/a)</td><td>137.80 (n/a)</td><td>27.76 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.27 (-0.73%)</td><td>0.22 (+1.72%)</td><td>0.23 (+15.16%)</td><td>0.18 (-3.02%)</td><td>0.03 (-11.80%)</td><td>223.40 (+3.14%)</td><td>185.38 (-2.08%)</td><td>179.90 (-13.13%)</td><td>151.70 (+0.73%)</td><td>27.26 (-8.30%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>216.60 (n/a)</td><td>189.32 (n/a)</td><td>207.10 (n/a)</td><td>150.60 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-0.37%)</td><td>0.03 (-1.01%)</td><td>0.03 (-5.79%)</td><td>0.03 (+2.88%)</td><td>0.00 <b>(-20.07%)</b></td><td>178.60 (-2.83%)</td><td>166.72 (+0.86%)</td><td>169.30 (+6.14%)</td><td>154.30 (+0.39%)</td><td>9.28 <b>(-22.88%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.80 (n/a)</td><td>165.30 (n/a)</td><td>159.50 (n/a)</td><td>153.70 (n/a)</td><td>12.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (-7.97%)</td><td>0.05 (-9.71%)</td><td>0.05 (-14.77%)</td><td>0.04 (-10.56%)</td><td>0.01 (+10.01%)</td><td>195.90 (+11.82%)</td><td>169.34 (+11.44%)</td><td>173.20 (+17.34%)</td><td>136.90 (+8.65%)</td><td>25.63 <b>(+34.42%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.20 (n/a)</td><td>151.96 (n/a)</td><td>147.60 (n/a)</td><td>126.00 (n/a)</td><td>19.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 (+3.26%)</td><td>0.07 (-9.48%)</td><td>0.08 (-6.73%)</td><td>0.04 <b>(-35.59%)</b></td><td>0.02 <b>(+81.41%)</b></td><td>280.50 <b>(+55.23%)</b></td><td>182.44 (+16.98%)</td><td>160.80 (+7.27%)</td><td>124.40 (-3.19%)</td><td>59.36 <b>(+180.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.70 (n/a)</td><td>155.96 (n/a)</td><td>149.90 (n/a)</td><td>128.50 (n/a)</td><td>21.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (-10.51%)</td><td>0.05 (+6.35%)</td><td>0.05 (+7.41%)</td><td>0.04 <b>(+22.81%)</b></td><td>0.01 <b>(-36.87%)</b></td><td>191.30 (-18.60%)</td><td>164.24 (-8.85%)</td><td>163.70 (-6.88%)</td><td>139.60 (+11.68%)</td><td>24.59 <b>(-43.35%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>180.18 (n/a)</td><td>175.80 (n/a)</td><td>125.00 (n/a)</td><td>43.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (+15.08%)</td><td>0.07 (+7.40%)</td><td>0.07 (+7.52%)</td><td>0.05 (+5.88%)</td><td>0.01 <b>(+20.98%)</b></td><td>192.10 (-5.56%)</td><td>149.94 (-6.38%)</td><td>138.90 (-6.97%)</td><td>113.30 (-13.11%)</td><td>30.52 (+0.05%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>203.40 (n/a)</td><td>160.16 (n/a)</td><td>149.30 (n/a)</td><td>130.40 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (-10.51%)</td><td>0.04 <b>(-24.53%)</b></td><td>0.04 <b>(-32.73%)</b></td><td>0.03 (-18.72%)</td><td>0.01 (+1.70%)</td><td>279.50 <b>(+23.02%)</b></td><td>224.24 <b>(+33.81%)</b></td><td>225.20 <b>(+48.65%)</b></td><td>163.00 (+11.80%)</td><td>46.40 <b>(+36.69%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.20 (n/a)</td><td>167.58 (n/a)</td><td>151.50 (n/a)</td><td>145.80 (n/a)</td><td>33.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (-17.16%)</td><td>0.07 (+6.46%)</td><td>0.07 <b>(+21.40%)</b></td><td>0.05 <b>(+32.66%)</b></td><td>0.02 <b>(-46.92%)</b></td><td>202.10 <b>(-24.62%)</b></td><td>154.22 (-16.62%)</td><td>144.40 (-17.63%)</td><td>108.00 <b>(+20.81%)</b></td><td>35.18 <b>(-53.83%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>268.10 (n/a)</td><td>184.96 (n/a)</td><td>175.30 (n/a)</td><td>89.40 (n/a)</td><td>76.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (-13.03%)</td><td>0.05 (-7.78%)</td><td>0.05 (+7.45%)</td><td>0.03 (-19.40%)</td><td>0.01 (-4.60%)</td><td>256.00 <b>(+24.03%)</b></td><td>177.02 (+9.85%)</td><td>158.70 (-6.92%)</td><td>133.50 (+14.99%)</td><td>50.38 <b>(+37.79%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>161.14 (n/a)</td><td>170.50 (n/a)</td><td>116.10 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (-1.63%)</td><td>0.06 (+12.60%)</td><td>0.06 <b>(+29.20%)</b></td><td>0.04 (-3.33%)</td><td>0.01 (-3.61%)</td><td>223.60 (+3.42%)</td><td>161.04 (-11.09%)</td><td>146.60 <b>(-22.60%)</b></td><td>121.70 (+1.67%)</td><td>39.99 (+6.86%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>181.12 (n/a)</td><td>189.40 (n/a)</td><td>119.70 (n/a)</td><td>37.42 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (+5.58%)</td><td>0.05 (-13.71%)</td><td>0.04 <b>(-24.30%)</b></td><td>0.03 <b>(-23.58%)</b></td><td>0.01 <b>(+113.78%)</b></td><td>245.40 <b>(+30.81%)</b></td><td>187.84 <b>(+22.18%)</b></td><td>199.00 <b>(+32.05%)</b></td><td>127.40 (-5.28%)</td><td>51.32 <b>(+154.94%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>153.74 (n/a)</td><td>150.70 (n/a)</td><td>134.50 (n/a)</td><td>20.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (+7.15%)</td><td>0.05 (-11.96%)</td><td>0.05 (-10.58%)</td><td>0.04 <b>(-28.78%)</b></td><td>0.01 <b>(+122.23%)</b></td><td>245.10 <b>(+40.38%)</b></td><td>188.58 (+19.22%)</td><td>181.30 (+11.84%)</td><td>122.60 (-6.70%)</td><td>47.64 <b>(+197.71%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.60 (n/a)</td><td>158.18 (n/a)</td><td>162.10 (n/a)</td><td>131.40 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 <b>(+24.12%)</b></td><td>0.05 (+19.72%)</td><td>0.06 <b>(+24.33%)</b></td><td>0.03 (+13.34%)</td><td>0.01 <b>(+43.29%)</b></td><td>242.30 (-11.76%)</td><td>164.84 (-15.23%)</td><td>143.70 (-19.59%)</td><td>128.10 (-19.43%)</td><td>45.75 (-0.00%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.60 (n/a)</td><td>194.46 (n/a)</td><td>178.70 (n/a)</td><td>159.00 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (-13.70%)</td><td>0.04 (-9.46%)</td><td>0.04 (-6.36%)</td><td>0.03 (-17.52%)</td><td>0.01 (-8.35%)</td><td>268.30 <b>(+21.24%)</b></td><td>217.18 (+10.82%)</td><td>219.60 (+6.81%)</td><td>177.50 (+15.86%)</td><td>34.46 <b>(+32.30%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.30 (n/a)</td><td>195.98 (n/a)</td><td>205.60 (n/a)</td><td>153.20 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (+1.55%)</td><td>0.05 (+10.67%)</td><td>0.05 (+13.77%)</td><td>0.04 (+6.05%)</td><td>0.01 (-10.75%)</td><td>192.00 (-5.74%)</td><td>163.16 (-10.08%)</td><td>168.70 (-12.09%)</td><td>136.30 (-1.52%)</td><td>21.74 (-16.35%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>181.46 (n/a)</td><td>191.90 (n/a)</td><td>138.40 (n/a)</td><td>25.99 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 <b>(-24.24%)</b></td><td>0.04 (-14.48%)</td><td>0.04 (-8.88%)</td><td>0.03 (-17.95%)</td><td>0.01 <b>(-38.66%)</b></td><td>250.80 <b>(+21.87%)</b></td><td>207.12 (+15.79%)</td><td>210.80 (+9.73%)</td><td>180.50 <b>(+32.04%)</b></td><td>28.66 (-3.62%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>178.88 (n/a)</td><td>192.10 (n/a)</td><td>136.70 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (+1.10%)</td><td>0.04 (+13.43%)</td><td>0.04 (+19.83%)</td><td>0.03 <b>(+29.68%)</b></td><td>0.01 (-18.54%)</td><td>243.90 <b>(-22.87%)</b></td><td>197.96 (-13.51%)</td><td>184.30 (-16.53%)</td><td>170.10 (-1.10%)</td><td>31.74 <b>(-40.22%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>316.20 (n/a)</td><td>228.88 (n/a)</td><td>220.80 (n/a)</td><td>172.00 (n/a)</td><td>53.09 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.75 <b>(+30.26%)</b></td><td>0.68 <b>(+31.31%)</b></td><td>0.71 <b>(+29.59%)</b></td><td>0.58 <b>(+40.16%)</b></td><td>0.06 (-4.79%)</td><td>168.80 <b>(-28.66%)</b></td><td>145.06 <b>(-24.38%)</b></td><td>139.40 <b>(-22.81%)</b></td><td>131.60 <b>(-23.27%)</b></td><td>14.31 <b>(-47.05%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.57 (n/a)</td><td>0.52 (n/a)</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>236.60 (n/a)</td><td>191.82 (n/a)</td><td>180.60 (n/a)</td><td>171.50 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.90 <b>(+32.65%)</b></td><td>0.67 (+18.30%)</td><td>0.72 <b>(+36.73%)</b></td><td>0.45 (+1.59%)</td><td>0.18 <b>(+72.58%)</b></td><td>220.20 (-1.56%)</td><td>155.88 (-12.49%)</td><td>136.80 <b>(-26.88%)</b></td><td>108.60 <b>(-24.64%)</b></td><td>44.75 <b>(+34.98%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.68 (n/a)</td><td>0.57 (n/a)</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.10 (n/a)</td><td>223.70 (n/a)</td><td>178.12 (n/a)</td><td>187.10 (n/a)</td><td>144.10 (n/a)</td><td>33.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.82 <b>(+28.63%)</b></td><td>0.64 (+18.43%)</td><td>0.65 <b>(+31.00%)</b></td><td>0.46 (-2.92%)</td><td>0.13 <b>(+69.96%)</b></td><td>212.40 (+3.01%)</td><td>158.24 (-13.80%)</td><td>152.20 <b>(-23.63%)</b></td><td>119.30 <b>(-22.23%)</b></td><td>34.83 <b>(+38.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.08 (n/a)</td><td>206.20 (n/a)</td><td>183.58 (n/a)</td><td>199.30 (n/a)</td><td>153.40 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.67 (-19.70%)</td><td>0.54 (-3.03%)</td><td>0.59 (+3.68%)</td><td>0.37 (+6.62%)</td><td>0.12 <b>(-45.50%)</b></td><td>267.70 (-6.20%)</td><td>189.90 (-4.96%)</td><td>166.70 (-3.59%)</td><td>147.30 <b>(+24.51%)</b></td><td>47.75 <b>(-39.19%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.83 (n/a)</td><td>0.56 (n/a)</td><td>0.57 (n/a)</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>285.40 (n/a)</td><td>199.82 (n/a)</td><td>172.90 (n/a)</td><td>118.30 (n/a)</td><td>78.51 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.64 <b>(+50.44%)</b></td><td>0.52 <b>(+36.25%)</b></td><td>0.51 <b>(+25.61%)</b></td><td>0.40 <b>(+47.10%)</b></td><td>0.09 <b>(+40.70%)</b></td><td>183.30 <b>(-32.01%)</b></td><td>145.50 <b>(-26.84%)</b></td><td>143.40 <b>(-20.38%)</b></td><td>114.80 <b>(-33.49%)</b></td><td>25.52 <b>(-37.14%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>269.60 (n/a)</td><td>198.88 (n/a)</td><td>180.10 (n/a)</td><td>172.60 (n/a)</td><td>40.60 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.61 <b>(+24.40%)</b></td><td>0.50 <b>(+41.21%)</b></td><td>0.51 <b>(+56.96%)</b></td><td>0.37 <b>(+28.83%)</b></td><td>0.09 (+10.17%)</td><td>198.80 <b>(-22.37%)</b></td><td>152.76 <b>(-29.84%)</b></td><td>144.90 <b>(-36.28%)</b></td><td>119.90 (-19.64%)</td><td>30.67 <b>(-30.58%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.49 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>256.10 (n/a)</td><td>217.72 (n/a)</td><td>227.40 (n/a)</td><td>149.20 (n/a)</td><td>44.18 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.63 <b>(+29.51%)</b></td><td>0.51 <b>(+27.34%)</b></td><td>0.51 <b>(+26.79%)</b></td><td>0.41 <b>(+35.61%)</b></td><td>0.09 <b>(+33.14%)</b></td><td>179.30 <b>(-26.27%)</b></td><td>149.02 <b>(-21.44%)</b></td><td>144.30 <b>(-21.15%)</b></td><td>116.90 <b>(-22.79%)</b></td><td>25.87 <b>(-24.24%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>243.20 (n/a)</td><td>189.70 (n/a)</td><td>183.00 (n/a)</td><td>151.40 (n/a)</td><td>34.14 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.54 (-0.07%)</td><td>0.48 (+17.81%)</td><td>0.47 <b>(+20.05%)</b></td><td>0.44 <b>(+53.62%)</b></td><td>0.04 <b>(-55.69%)</b></td><td>167.50 <b>(-34.93%)</b></td><td>154.56 (-18.18%)</td><td>156.60 (-16.70%)</td><td>135.90 (+0.07%)</td><td>12.67 <b>(-71.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>257.40 (n/a)</td><td>188.90 (n/a)</td><td>188.00 (n/a)</td><td>135.80 (n/a)</td><td>44.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.72 <b>(-26.38%)</b></td><td>0.61 <b>(-31.04%)</b></td><td>0.56 <b>(-37.91%)</b></td><td>0.55 <b>(-32.05%)</b></td><td>0.08 (+8.02%)</td><td>236.70 <b>(+47.11%)</b></td><td>216.66 <b>(+45.98%)</b></td><td>232.80 <b>(+61.11%)</b></td><td>181.20 <b>(+35.83%)</b></td><td>25.30 <b>(+115.05%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.98 (n/a)</td><td>0.89 (n/a)</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.07 (n/a)</td><td>160.90 (n/a)</td><td>148.42 (n/a)</td><td>144.50 (n/a)</td><td>133.40 (n/a)</td><td>11.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.73 <b>(-21.32%)</b></td><td>0.67 (-14.10%)</td><td>0.69 (-6.18%)</td><td>0.59 (-15.78%)</td><td>0.05 <b>(-45.86%)</b></td><td>223.00 (+18.74%)</td><td>197.00 (+15.65%)</td><td>190.50 (+6.60%)</td><td>180.70 <b>(+27.07%)</b></td><td>16.38 (-18.27%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.70 (n/a)</td><td>0.10 (n/a)</td><td>187.80 (n/a)</td><td>170.34 (n/a)</td><td>178.70 (n/a)</td><td>142.20 (n/a)</td><td>20.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.97 (+17.02%)</td><td>0.71 (-8.73%)</td><td>0.67 (-11.58%)</td><td>0.51 <b>(-30.99%)</b></td><td>0.18 <b>(+347.31%)</b></td><td>258.90 <b>(+44.88%)</b></td><td>195.78 (+15.11%)</td><td>196.30 (+13.08%)</td><td>135.60 (-14.56%)</td><td>48.62 <b>(+450.73%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.83 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.04 (n/a)</td><td>178.70 (n/a)</td><td>170.08 (n/a)</td><td>173.60 (n/a)</td><td>158.70 (n/a)</td><td>8.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-0.71%)</td><td>0.03 (-4.14%)</td><td>0.03 (+13.39%)</td><td>0.02 (-19.55%)</td><td>0.01 <b>(+50.75%)</b></td><td>220.30 <b>(+24.32%)</b></td><td>161.26 (+8.65%)</td><td>131.90 (-11.83%)</td><td>124.60 (+0.73%)</td><td>46.94 <b>(+90.73%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.20 (n/a)</td><td>148.42 (n/a)</td><td>149.60 (n/a)</td><td>123.70 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (-13.11%)</td><td>0.03 (-9.07%)</td><td>0.03 (-3.02%)</td><td>0.02 (-9.41%)</td><td>0.00 <b>(-36.22%)</b></td><td>177.60 (+10.38%)</td><td>157.44 (+9.29%)</td><td>156.50 (+3.10%)</td><td>143.40 (+15.09%)</td><td>14.61 (-18.77%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>160.90 (n/a)</td><td>144.06 (n/a)</td><td>151.80 (n/a)</td><td>124.60 (n/a)</td><td>17.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (+19.78%)</td><td>0.02 (-14.50%)</td><td>0.02 (-11.10%)</td><td>0.01 <b>(-48.83%)</b></td><td>0.01 <b>(+485.78%)</b></td><td>347.20 <b>(+95.39%)</b></td><td>217.26 <b>(+29.77%)</b></td><td>187.80 (+12.46%)</td><td>129.30 (-16.53%)</td><td>82.38 <b>(+880.48%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>167.42 (n/a)</td><td>167.00 (n/a)</td><td>154.90 (n/a)</td><td>8.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.05 (+18.01%)</td><td>0.87 (+19.45%)</td><td>0.91 <b>(+21.43%)</b></td><td>0.65 (+14.00%)</td><td>0.16 <b>(+21.78%)</b></td><td>204.60 (-12.30%)</td><td>157.18 (-16.07%)</td><td>145.40 (-17.67%)</td><td>125.50 (-15.26%)</td><td>31.67 (-9.68%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.89 (n/a)</td><td>0.73 (n/a)</td><td>0.75 (n/a)</td><td>0.57 (n/a)</td><td>0.13 (n/a)</td><td>233.30 (n/a)</td><td>187.28 (n/a)</td><td>176.60 (n/a)</td><td>148.10 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.91 (-14.12%)</td><td>0.80 (-1.86%)</td><td>0.81 (+5.42%)</td><td>0.68 (+10.35%)</td><td>0.09 <b>(-47.37%)</b></td><td>193.60 (-9.41%)</td><td>166.52 (-0.34%)</td><td>163.20 (-5.17%)</td><td>146.00 (+16.52%)</td><td>18.51 <b>(-43.97%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.05 (n/a)</td><td>0.82 (n/a)</td><td>0.77 (n/a)</td><td>0.62 (n/a)</td><td>0.16 (n/a)</td><td>213.70 (n/a)</td><td>167.08 (n/a)</td><td>172.10 (n/a)</td><td>125.30 (n/a)</td><td>33.04 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.79 (-13.97%)</td><td>0.70 (-10.02%)</td><td>0.73 (-2.70%)</td><td>0.58 (-15.28%)</td><td>0.08 (-16.11%)</td><td>227.30 (+18.08%)</td><td>190.04 (+11.11%)</td><td>180.60 (+2.79%)</td><td>166.60 (+16.26%)</td><td>23.59 (+16.64%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.92 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.10 (n/a)</td><td>192.50 (n/a)</td><td>171.04 (n/a)</td><td>175.70 (n/a)</td><td>143.30 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.91 (-14.76%)</td><td>0.74 (-11.18%)</td><td>0.70 (-12.13%)</td><td>0.66 (-2.81%)</td><td>0.10 <b>(-41.48%)</b></td><td>201.30 (+2.91%)</td><td>180.18 (+10.51%)</td><td>187.50 (+13.84%)</td><td>145.20 (+17.29%)</td><td>21.30 <b>(-32.13%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.07 (n/a)</td><td>0.84 (n/a)</td><td>0.80 (n/a)</td><td>0.68 (n/a)</td><td>0.17 (n/a)</td><td>195.60 (n/a)</td><td>163.04 (n/a)</td><td>164.70 (n/a)</td><td>123.80 (n/a)</td><td>31.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.06 (+2.52%)</td><td>0.86 (-0.77%)</td><td>0.74 (-9.08%)</td><td>0.68 (-1.51%)</td><td>0.19 (+18.98%)</td><td>194.20 (+1.52%)</td><td>159.94 (+1.81%)</td><td>178.00 (+10.01%)</td><td>124.50 (-2.51%)</td><td>32.84 (+16.76%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.82 (n/a)</td><td>0.69 (n/a)</td><td>0.16 (n/a)</td><td>191.30 (n/a)</td><td>157.10 (n/a)</td><td>161.80 (n/a)</td><td>127.70 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (+2.23%)</td><td>0.02 (-0.90%)</td><td>0.02 (-1.39%)</td><td>0.02 (-8.97%)</td><td>0.00 <b>(+25.81%)</b></td><td>206.90 (+9.88%)</td><td>167.18 (+1.65%)</td><td>165.20 (+1.41%)</td><td>142.80 (-2.19%)</td><td>25.67 <b>(+36.47%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.30 (n/a)</td><td>164.46 (n/a)</td><td>162.90 (n/a)</td><td>146.00 (n/a)</td><td>18.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 <b>(+27.52%)</b></td><td>0.03 <b>(+25.74%)</b></td><td>0.02 (+17.74%)</td><td>0.02 <b>(+33.38%)</b></td><td>0.00 (+13.26%)</td><td>178.10 <b>(-25.01%)</b></td><td>159.50 <b>(-20.91%)</b></td><td>164.40 (-15.08%)</td><td>125.40 <b>(-21.58%)</b></td><td>19.98 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>237.50 (n/a)</td><td>201.68 (n/a)</td><td>193.60 (n/a)</td><td>159.90 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.00 (-2.22%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.38%)</td><td>0.00 (-4.76%)</td><td>0.00 <b>(+24.72%)</b></td><td>1027.22 (+5.10%)</td><td>967.25 (+1.10%)</td><td>951.11 (-1.67%)</td><td>936.75 (+3.68%)</td><td>38.11 <b>(+26.52%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>977.38 (n/a)</td><td>956.76 (n/a)</td><td>967.28 (n/a)</td><td>903.46 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.01 (+0.00%)</td><td>0.01 (-0.75%)</td><td>0.01 (-1.23%)</td><td>0.01 (+0.00%)</td><td>0.00 (-3.92%)</td><td>1102.35 (-0.78%)</td><td>1024.64 (+0.26%)</td><td>1020.13 (+0.46%)</td><td>972.63 (+0.15%)</td><td>47.82 (-9.87%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1110.98 (n/a)</td><td>1021.97 (n/a)</td><td>1015.43 (n/a)</td><td>971.17 (n/a)</td><td>53.06 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.98 (-0.70%)</td><td>0.96 (-0.85%)</td><td>0.95 (-0.32%)</td><td>0.94 (-1.54%)</td><td>0.02 (+9.14%)</td><td>2233.84 (+1.57%)</td><td>2194.56 (+0.86%)</td><td>2198.47 (+0.32%)</td><td>2139.92 (+0.70%)</td><td>34.23 (+11.50%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2199.40 (n/a)</td><td>2175.84 (n/a)</td><td>2191.39 (n/a)</td><td>2125.03 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.32 (+9.90%)</td><td>2.84 (+4.51%)</td><td>2.67 (-2.22%)</td><td>2.46 (+7.09%)</td><td>0.38 <b>(+38.79%)</b></td><td>213.30 (-6.65%)</td><td>187.18 (-3.82%)</td><td>196.60 (+2.24%)</td><td>157.90 (-8.99%)</td><td>24.28 (+15.26%)</td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.02 (n/a)</td><td>2.72 (n/a)</td><td>2.73 (n/a)</td><td>2.29 (n/a)</td><td>0.28 (n/a)</td><td>228.50 (n/a)</td><td>194.62 (n/a)</td><td>192.30 (n/a)</td><td>173.50 (n/a)</td><td>21.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.60 (-15.14%)</td><td>4.18 (-8.27%)</td><td>4.06 (-7.38%)</td><td>3.81 (-6.19%)</td><td>0.31 <b>(-39.74%)</b></td><td>275.10 (+6.59%)</td><td>252.12 (+8.49%)</td><td>258.20 (+7.94%)</td><td>228.20 (+17.87%)</td><td>18.39 <b>(-23.07%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>5.41 (n/a)</td><td>4.55 (n/a)</td><td>4.38 (n/a)</td><td>4.06 (n/a)</td><td>0.51 (n/a)</td><td>258.10 (n/a)</td><td>232.40 (n/a)</td><td>239.20 (n/a)</td><td>193.60 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.28 (+7.21%)</td><td>2.55 (-8.96%)</td><td>2.50 (-11.73%)</td><td>2.06 (-17.19%)</td><td>0.45 <b>(+99.99%)</b></td><td>254.30 <b>(+20.75%)</b></td><td>210.62 (+11.79%)</td><td>209.80 (+13.28%)</td><td>160.00 (-6.76%)</td><td>34.30 <b>(+120.01%)</b></td>
</tr>
<tr>
<td><code>b2eb090</code> — 2026-09-11 23:34:59</td><td>3.06 (n/a)</td><td>2.80 (n/a)</td><td>2.83 (n/a)</td><td>2.49 (n/a)</td><td>0.23 (n/a)</td><td>210.60 (n/a)</td><td>188.40 (n/a)</td><td>185.20 (n/a)</td><td>171.60 (n/a)</td><td>15.59 (n/a)</td>
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
