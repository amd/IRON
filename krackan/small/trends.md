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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (-2.93%)</td><td>0.08 <b>(+24.34%)</b></td><td>0.09 <b>(+55.82%)</b></td><td>0.05 <b>(+63.81%)</b></td><td>0.02 <b>(-34.29%)</b></td><td>225.80 <b>(-38.94%)</b></td><td>160.66 <b>(-27.22%)</b></td><td>140.50 <b>(-35.84%)</b></td><td>130.30 (+3.00%)</td><td>40.36 <b>(-58.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>369.80 (n/a)</td><td>220.76 (n/a)</td><td>219.00 (n/a)</td><td>126.50 (n/a)</td><td>96.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.11 (+10.30%)</td><td>0.09 (+12.81%)</td><td>0.08 (+13.70%)</td><td>0.07 <b>(+28.04%)</b></td><td>0.01 <b>(-23.06%)</b></td><td>166.40 <b>(-21.88%)</b></td><td>144.78 (-12.98%)</td><td>148.70 (-12.01%)</td><td>117.00 (-9.30%)</td><td>18.33 <b>(-45.70%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.00 (n/a)</td><td>166.38 (n/a)</td><td>169.00 (n/a)</td><td>129.00 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (-6.19%)</td><td>0.08 (+5.57%)</td><td>0.09 (+16.15%)</td><td>0.06 (-15.19%)</td><td>0.02 <b>(+20.58%)</b></td><td>213.50 (+17.96%)</td><td>151.74 (-3.74%)</td><td>138.60 (-13.91%)</td><td>130.30 (+6.54%)</td><td>35.09 <b>(+58.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.00 (n/a)</td><td>157.64 (n/a)</td><td>161.00 (n/a)</td><td>122.30 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (-3.38%)</td><td>0.08 (+14.86%)</td><td>0.08 <b>(+35.19%)</b></td><td>0.06 (+4.34%)</td><td>0.01 <b>(-20.05%)</b></td><td>220.00 (-4.18%)</td><td>165.22 (-13.95%)</td><td>154.20 <b>(-26.04%)</b></td><td>140.40 (+3.46%)</td><td>31.40 (-16.35%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>229.60 (n/a)</td><td>192.00 (n/a)</td><td>208.50 (n/a)</td><td>135.70 (n/a)</td><td>37.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (+8.97%)</td><td>0.03 (-12.57%)</td><td>0.03 <b>(-20.26%)</b></td><td>0.02 <b>(-27.52%)</b></td><td>0.01 <b>(+103.82%)</b></td><td>239.50 <b>(+37.96%)</b></td><td>187.78 <b>(+20.42%)</b></td><td>204.50 <b>(+25.38%)</b></td><td>114.50 (-8.25%)</td><td>47.39 <b>(+153.60%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>173.60 (n/a)</td><td>155.94 (n/a)</td><td>163.10 (n/a)</td><td>124.80 (n/a)</td><td>18.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 <b>(+40.38%)</b></td><td>0.03 (+16.77%)</td><td>0.03 (-5.81%)</td><td>0.02 <b>(+51.76%)</b></td><td>0.01 <b>(+24.95%)</b></td><td>214.00 <b>(-34.11%)</b></td><td>176.20 (-16.17%)</td><td>177.90 (+6.21%)</td><td>109.80 <b>(-28.79%)</b></td><td>41.60 <b>(-42.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>324.80 (n/a)</td><td>210.18 (n/a)</td><td>167.50 (n/a)</td><td>154.20 (n/a)</td><td>71.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 <b>(-25.17%)</b></td><td>0.03 (-16.18%)</td><td>0.03 (-12.84%)</td><td>0.02 (+2.74%)</td><td>0.00 <b>(-66.32%)</b></td><td>216.90 (-2.65%)</td><td>189.22 (+14.80%)</td><td>186.30 (+14.72%)</td><td>169.10 <b>(+33.68%)</b></td><td>18.31 <b>(-54.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>164.82 (n/a)</td><td>162.40 (n/a)</td><td>126.50 (n/a)</td><td>40.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 <b>(-22.35%)</b></td><td>0.03 (-15.79%)</td><td>0.03 (-10.42%)</td><td>0.02 (-19.16%)</td><td>0.00 <b>(-25.28%)</b></td><td>266.50 <b>(+23.67%)</b></td><td>214.20 (+18.53%)</td><td>199.20 (+11.66%)</td><td>177.90 <b>(+28.82%)</b></td><td>35.12 <b>(+22.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>180.72 (n/a)</td><td>178.40 (n/a)</td><td>138.10 (n/a)</td><td>28.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.04 (+8.46%)</td><td>0.03 (+8.22%)</td><td>0.03 (+8.17%)</td><td>0.03 (+2.40%)</td><td>0.00 (+6.81%)</td><td>209.60 (-2.33%)</td><td>173.56 (-7.58%)</td><td>169.70 (-7.57%)</td><td>144.30 (-7.80%)</td><td>23.76 (-4.99%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.60 (n/a)</td><td>187.80 (n/a)</td><td>183.60 (n/a)</td><td>156.50 (n/a)</td><td>25.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-11.66%)</td><td>0.03 (-4.58%)</td><td>0.03 (-5.02%)</td><td>0.02 (-0.74%)</td><td>0.00 (-19.52%)</td><td>223.30 (+0.77%)</td><td>191.60 (+4.22%)</td><td>199.00 (+5.24%)</td><td>165.00 (+13.17%)</td><td>25.81 (-10.16%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.60 (n/a)</td><td>183.84 (n/a)</td><td>189.10 (n/a)</td><td>145.80 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.04 (+13.68%)</td><td>0.03 (+12.46%)</td><td>0.03 (+6.93%)</td><td>0.03 <b>(+32.31%)</b></td><td>0.00 (-6.39%)</td><td>204.00 <b>(-24.44%)</b></td><td>184.68 (-12.02%)</td><td>187.20 (-6.49%)</td><td>146.50 (-12.01%)</td><td>22.81 <b>(-39.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>270.00 (n/a)</td><td>209.90 (n/a)</td><td>200.20 (n/a)</td><td>166.50 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-8.57%)</td><td>0.02 (-18.02%)</td><td>0.02 (-18.25%)</td><td>0.01 <b>(-36.47%)</b></td><td>0.01 <b>(+54.77%)</b></td><td>366.20 <b>(+57.37%)</b></td><td>260.30 <b>(+26.46%)</b></td><td>253.90 <b>(+22.36%)</b></td><td>184.90 (+9.41%)</td><td>66.04 <b>(+175.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>205.84 (n/a)</td><td>207.50 (n/a)</td><td>169.00 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>150.92 (n/a)</td><td>133.20 (n/a)</td><td>131.30 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>179.80 (n/a)</td><td>148.50 (n/a)</td><td>135.40 (n/a)</td><td>118.60 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>209.90 (n/a)</td><td>161.36 (n/a)</td><td>162.00 (n/a)</td><td>119.30 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>170.14 (n/a)</td><td>163.30 (n/a)</td><td>143.40 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>164.80 (n/a)</td><td>143.90 (n/a)</td><td>142.90 (n/a)</td><td>130.60 (n/a)</td><td>12.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>199.80 (n/a)</td><td>164.78 (n/a)</td><td>161.30 (n/a)</td><td>121.80 (n/a)</td><td>30.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>172.08 (n/a)</td><td>158.30 (n/a)</td><td>154.50 (n/a)</td><td>27.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>180.24 (n/a)</td><td>175.60 (n/a)</td><td>162.40 (n/a)</td><td>14.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>5.02 <b>(+32.41%)</b></td><td>3.35 (+6.61%)</td><td>2.97 (-1.55%)</td><td>2.84 (+9.34%)</td><td>0.94 <b>(+111.79%)</b></td><td>484.90 (-8.54%)</td><td>429.88 (-3.22%)</td><td>463.00 (+1.58%)</td><td>274.10 <b>(-24.49%)</b></td><td>88.20 <b>(+43.60%)</b></td><td>979.29 <b>(+32.41%)</b></td><td>654.33 (+6.61%)</td><td>579.76 (-1.55%)</td><td>553.55 (+9.34%)</td><td>182.48 <b>(+111.79%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.79 (n/a)</td><td>3.15 (n/a)</td><td>3.02 (n/a)</td><td>2.60 (n/a)</td><td>0.44 (n/a)</td><td>530.20 (n/a)</td><td>444.20 (n/a)</td><td>455.80 (n/a)</td><td>363.00 (n/a)</td><td>61.42 (n/a)</td><td>739.59 (n/a)</td><td>613.74 (n/a)</td><td>588.87 (n/a)</td><td>506.27 (n/a)</td><td>86.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>5.71 (-5.75%)</td><td>4.28 (-4.25%)</td><td>3.71 (-1.58%)</td><td>3.43 (-5.48%)</td><td>1.02 (-8.79%)</td><td>400.70 (+5.81%)</td><td>335.10 (+4.04%)</td><td>370.60 (+1.59%)</td><td>241.00 (+6.07%)</td><td>72.67 (+0.48%)</td><td>1113.85 (-5.75%)</td><td>835.56 (-4.25%)</td><td>724.26 (-1.58%)</td><td>669.96 (-5.48%)</td><td>199.72 (-8.79%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.06 (n/a)</td><td>4.47 (n/a)</td><td>3.77 (n/a)</td><td>3.63 (n/a)</td><td>1.12 (n/a)</td><td>378.70 (n/a)</td><td>322.08 (n/a)</td><td>364.80 (n/a)</td><td>227.20 (n/a)</td><td>72.32 (n/a)</td><td>1181.74 (n/a)</td><td>872.62 (n/a)</td><td>735.90 (n/a)</td><td>708.81 (n/a)</td><td>218.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>6.43 (-5.73%)</td><td>4.56 (-3.84%)</td><td>3.79 (-11.37%)</td><td>3.50 (-2.72%)</td><td>1.30 (-1.35%)</td><td>393.20 (+2.80%)</td><td>319.70 (+4.46%)</td><td>363.30 (+12.83%)</td><td>214.20 (+6.09%)</td><td>80.42 (+8.87%)</td><td>1253.33 (-5.73%)</td><td>890.29 (-3.84%)</td><td>738.84 (-11.37%)</td><td>682.66 (-2.72%)</td><td>253.41 (-1.35%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.82 (n/a)</td><td>4.75 (n/a)</td><td>4.27 (n/a)</td><td>3.60 (n/a)</td><td>1.32 (n/a)</td><td>382.50 (n/a)</td><td>306.06 (n/a)</td><td>322.00 (n/a)</td><td>201.90 (n/a)</td><td>73.87 (n/a)</td><td>1329.45 (n/a)</td><td>925.86 (n/a)</td><td>833.64 (n/a)</td><td>701.72 (n/a)</td><td>256.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>6.31 (-0.07%)</td><td>4.32 (-15.30%)</td><td>3.80 <b>(-30.62%)</b></td><td>3.60 (-2.79%)</td><td>1.14 (-2.07%)</td><td>381.90 (+2.88%)</td><td>332.82 (+17.90%)</td><td>362.60 <b>(+44.12%)</b></td><td>218.20 (+0.05%)</td><td>68.89 (-0.45%)</td><td>1229.97 (-0.07%)</td><td>843.22 (-15.30%)</td><td>740.37 <b>(-30.62%)</b></td><td>702.94 (-2.79%)</td><td>223.26 (-2.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.31 (n/a)</td><td>5.10 (n/a)</td><td>5.47 (n/a)</td><td>3.71 (n/a)</td><td>1.17 (n/a)</td><td>371.20 (n/a)</td><td>282.28 (n/a)</td><td>251.60 (n/a)</td><td>218.10 (n/a)</td><td>69.20 (n/a)</td><td>1230.88 (n/a)</td><td>995.50 (n/a)</td><td>1067.05 (n/a)</td><td>723.14 (n/a)</td><td>227.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>5.72 <b>(+24.24%)</b></td><td>3.62 (+4.47%)</td><td>3.11 (-3.36%)</td><td>3.05 (-0.59%)</td><td>1.17 <b>(+82.39%)</b></td><td>451.60 (+0.60%)</td><td>403.60 (-0.58%)</td><td>442.00 (+3.46%)</td><td>240.50 (-19.48%)</td><td>91.32 <b>(+48.77%)</b></td><td>1116.35 <b>(+24.24%)</b></td><td>706.59 (+4.47%)</td><td>607.26 (-3.36%)</td><td>594.45 (-0.59%)</td><td>229.17 <b>(+82.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>4.61 (n/a)</td><td>3.47 (n/a)</td><td>3.22 (n/a)</td><td>3.07 (n/a)</td><td>0.64 (n/a)</td><td>448.90 (n/a)</td><td>405.96 (n/a)</td><td>427.20 (n/a)</td><td>298.70 (n/a)</td><td>61.38 (n/a)</td><td>898.56 (n/a)</td><td>676.39 (n/a)</td><td>628.38 (n/a)</td><td>597.95 (n/a)</td><td>125.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.58 (-19.06%)</td><td>1.23 <b>(-24.83%)</b></td><td>1.06 <b>(-36.59%)</b></td><td>1.01 (-4.08%)</td><td>0.27 <b>(-23.62%)</b></td><td>397.80 (+4.25%)</td><td>337.60 <b>(+31.33%)</b></td><td>377.90 <b>(+57.72%)</b></td><td>254.70 <b>(+23.52%)</b></td><td>67.20 (-5.52%)</td><td>131.74 (-19.06%)</td><td>102.92 <b>(-24.83%)</b></td><td>88.79 <b>(-36.59%)</b></td><td>84.34 (-4.08%)</td><td>22.21 <b>(-23.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.95 (n/a)</td><td>1.64 (n/a)</td><td>1.68 (n/a)</td><td>1.05 (n/a)</td><td>0.35 (n/a)</td><td>381.60 (n/a)</td><td>257.06 (n/a)</td><td>239.60 (n/a)</td><td>206.20 (n/a)</td><td>71.13 (n/a)</td><td>162.77 (n/a)</td><td>136.91 (n/a)</td><td>140.02 (n/a)</td><td>87.93 (n/a)</td><td>29.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>6.24 (-6.40%)</td><td>5.16 (-0.92%)</td><td>5.19 (+5.82%)</td><td>4.05 (-12.25%)</td><td>0.79 (-5.34%)</td><td>477.50 (+13.96%)</td><td>382.32 (+1.14%)</td><td>372.20 (-5.51%)</td><td>309.70 (+6.83%)</td><td>61.33 (+19.70%)</td><td>1300.10 (-6.40%)</td><td>1074.06 (-0.92%)</td><td>1081.76 (+5.82%)</td><td>843.22 (-12.25%)</td><td>164.89 (-5.33%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.67 (n/a)</td><td>5.20 (n/a)</td><td>4.91 (n/a)</td><td>4.61 (n/a)</td><td>0.84 (n/a)</td><td>419.00 (n/a)</td><td>378.00 (n/a)</td><td>393.90 (n/a)</td><td>289.90 (n/a)</td><td>51.23 (n/a)</td><td>1389.03 (n/a)</td><td>1084.04 (n/a)</td><td>1022.22 (n/a)</td><td>960.90 (n/a)</td><td>174.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>14.72 (-4.96%)</td><td>11.71 (+3.62%)</td><td>10.92 (+1.64%)</td><td>10.11 <b>(+73.95%)</b></td><td>1.80 <b>(-54.40%)</b></td><td>544.50 <b>(-42.51%)</b></td><td>478.02 (-13.22%)</td><td>504.10 (-1.62%)</td><td>373.90 (+5.21%)</td><td>64.92 <b>(-72.83%)</b></td><td>5743.13 (-4.96%)</td><td>4568.06 (+3.62%)</td><td>4260.04 (+1.64%)</td><td>3943.69 <b>(+73.95%)</b></td><td>701.16 <b>(-54.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>15.49 (n/a)</td><td>11.30 (n/a)</td><td>10.74 (n/a)</td><td>5.81 (n/a)</td><td>3.94 (n/a)</td><td>947.20 (n/a)</td><td>550.86 (n/a)</td><td>512.40 (n/a)</td><td>355.40 (n/a)</td><td>238.90 (n/a)</td><td>6043.17 (n/a)</td><td>4408.53 (n/a)</td><td>4191.31 (n/a)</td><td>2267.11 (n/a)</td><td>1537.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>176.28 (n/a)</td><td>166.40 (n/a)</td><td>139.10 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>312.00 (n/a)</td><td>201.44 (n/a)</td><td>181.80 (n/a)</td><td>131.30 (n/a)</td><td>67.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>186.52 (n/a)</td><td>176.60 (n/a)</td><td>164.30 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>192.70 (n/a)</td><td>175.68 (n/a)</td><td>176.00 (n/a)</td><td>156.00 (n/a)</td><td>13.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.10 (n/a)</td><td>183.46 (n/a)</td><td>175.40 (n/a)</td><td>143.50 (n/a)</td><td>38.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>180.66 (n/a)</td><td>176.70 (n/a)</td><td>140.70 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>178.06 (n/a)</td><td>170.80 (n/a)</td><td>147.10 (n/a)</td><td>25.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>235.70 (n/a)</td><td>200.70 (n/a)</td><td>209.60 (n/a)</td><td>146.70 (n/a)</td><td>34.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>4.98 (-0.38%)</td><td>4.08 (-6.30%)</td><td>4.19 (+2.26%)</td><td>3.47 (-6.53%)</td><td>0.62 (+13.06%)</td><td>2709.70 (+6.98%)</td><td>2348.68 (+7.28%)</td><td>2241.90 (-2.21%)</td><td>1888.60 (+0.38%)</td><td>342.65 <b>(+26.19%)</b></td><td>1958.79 (-0.38%)</td><td>1603.22 (-6.30%)</td><td>1650.12 (+2.26%)</td><td>1365.22 (-6.53%)</td><td>242.58 (+13.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>5.00 (n/a)</td><td>4.35 (n/a)</td><td>4.10 (n/a)</td><td>3.71 (n/a)</td><td>0.55 (n/a)</td><td>2532.80 (n/a)</td><td>2189.34 (n/a)</td><td>2292.60 (n/a)</td><td>1881.40 (n/a)</td><td>271.54 (n/a)</td><td>1966.33 (n/a)</td><td>1710.96 (n/a)</td><td>1613.64 (n/a)</td><td>1460.58 (n/a)</td><td>214.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.20 (-6.33%)</td><td>0.99 (+3.00%)</td><td>0.96 (-1.60%)</td><td>0.82 (+13.58%)</td><td>0.14 <b>(-35.77%)</b></td><td>271.20 (-11.98%)</td><td>227.46 (-5.25%)</td><td>229.40 (+1.64%)</td><td>184.90 (+6.76%)</td><td>31.42 <b>(-40.52%)</b></td><td>51.03 (-6.33%)</td><td>42.14 (+3.00%)</td><td>41.14 (-1.60%)</td><td>34.79 (+13.58%)</td><td>5.95 <b>(-35.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.28 (n/a)</td><td>0.96 (n/a)</td><td>0.98 (n/a)</td><td>0.72 (n/a)</td><td>0.22 (n/a)</td><td>308.10 (n/a)</td><td>240.06 (n/a)</td><td>225.70 (n/a)</td><td>173.20 (n/a)</td><td>52.83 (n/a)</td><td>54.48 (n/a)</td><td>40.92 (n/a)</td><td>41.81 (n/a)</td><td>30.63 (n/a)</td><td>9.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.19 (+7.84%)</td><td>1.00 (+10.98%)</td><td>1.06 (+13.94%)</td><td>0.67 (-3.84%)</td><td>0.21 (+17.32%)</td><td>328.30 (+3.99%)</td><td>230.78 (-8.98%)</td><td>207.90 (-12.24%)</td><td>185.90 (-7.24%)</td><td>58.85 (+11.54%)</td><td>50.78 (+7.84%)</td><td>42.73 (+10.98%)</td><td>45.38 (+13.94%)</td><td>28.74 (-3.84%)</td><td>9.09 (+17.32%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>0.93 (n/a)</td><td>0.70 (n/a)</td><td>0.18 (n/a)</td><td>315.70 (n/a)</td><td>253.56 (n/a)</td><td>236.90 (n/a)</td><td>200.40 (n/a)</td><td>52.76 (n/a)</td><td>47.08 (n/a)</td><td>38.50 (n/a)</td><td>39.83 (n/a)</td><td>29.89 (n/a)</td><td>7.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.53 (+0.00%)</td><td>0.53 (+0.12%)</td><td>0.53 (+0.19%)</td><td>0.53 (+0.13%)</td><td>0.00 <b>(-53.27%)</b></td><td>47825.60 (-0.13%)</td><td>47792.72 (-0.12%)</td><td>47791.70 (-0.19%)</td><td>47767.20 (-0.00%)</td><td>24.48 <b>(-53.32%)</b></td><td>359.66 (+0.00%)</td><td>359.47 (+0.12%)</td><td>359.47 (+0.19%)</td><td>359.22 (+0.13%)</td><td>0.18 <b>(-53.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47888.70 (n/a)</td><td>47849.60 (n/a)</td><td>47883.30 (n/a)</td><td>47769.10 (n/a)</td><td>52.45 (n/a)</td><td>359.64 (n/a)</td><td>359.04 (n/a)</td><td>358.79 (n/a)</td><td>358.75 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.91 (+0.32%)</td><td>0.90 (+0.07%)</td><td>0.91 (-0.00%)</td><td>0.90 (-0.03%)</td><td>0.00 <b>(+70.10%)</b></td><td>27904.50 (+0.03%)</td><td>27808.54 (-0.07%)</td><td>27798.50 (+0.00%)</td><td>27695.40 (-0.32%)</td><td>89.39 <b>(+69.68%)</b></td><td>620.32 (+0.32%)</td><td>617.80 (+0.07%)</td><td>618.01 (-0.00%)</td><td>615.67 (-0.03%)</td><td>1.99 <b>(+70.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27896.10 (n/a)</td><td>27827.30 (n/a)</td><td>27797.90 (n/a)</td><td>27784.10 (n/a)</td><td>52.68 (n/a)</td><td>618.34 (n/a)</td><td>617.38 (n/a)</td><td>618.03 (n/a)</td><td>615.85 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>3.32 (+4.47%)</td><td>3.22 (+1.96%)</td><td>3.16 (+0.20%)</td><td>3.14 (+0.27%)</td><td>0.09 <b>(+427.31%)</b></td><td>8003.80 (-0.27%)</td><td>7823.38 (-1.87%)</td><td>7960.60 (-0.20%)</td><td>7572.40 (-4.28%)</td><td>212.76 <b>(+403.44%)</b></td><td>2268.75 (+4.47%)</td><td>2197.28 (+1.96%)</td><td>2158.12 (+0.20%)</td><td>2146.45 (+0.27%)</td><td>60.35 <b>(+427.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>3.15 (n/a)</td><td>3.14 (n/a)</td><td>0.02 (n/a)</td><td>8025.30 (n/a)</td><td>7972.12 (n/a)</td><td>7976.80 (n/a)</td><td>7910.80 (n/a)</td><td>42.26 (n/a)</td><td>2171.70 (n/a)</td><td>2155.04 (n/a)</td><td>2153.72 (n/a)</td><td>2140.70 (n/a)</td><td>11.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>4.29 (+10.05%)</td><td>3.78 (+0.96%)</td><td>3.71 (+0.38%)</td><td>3.55 (-1.33%)</td><td>0.30 <b>(+140.58%)</b></td><td>2268.40 (+1.35%)</td><td>2144.88 (-0.56%)</td><td>2173.10 (-0.38%)</td><td>1877.30 (-9.13%)</td><td>159.88 <b>(+121.12%)</b></td><td>1126.08 (+10.05%)</td><td>990.33 (+0.96%)</td><td>972.79 (+0.38%)</td><td>931.91 (-1.33%)</td><td>79.74 <b>(+140.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>3.90 (n/a)</td><td>3.74 (n/a)</td><td>3.70 (n/a)</td><td>3.60 (n/a)</td><td>0.13 (n/a)</td><td>2238.20 (n/a)</td><td>2156.98 (n/a)</td><td>2181.40 (n/a)</td><td>2066.00 (n/a)</td><td>72.31 (n/a)</td><td>1023.22 (n/a)</td><td>980.93 (n/a)</td><td>969.08 (n/a)</td><td>944.46 (n/a)</td><td>33.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.53 (+14.51%)</td><td>0.39 (+14.50%)</td><td>0.34 (+8.77%)</td><td>0.33 (+12.13%)</td><td>0.09 <b>(+26.87%)</b></td><td>3789.60 (-10.82%)</td><td>3297.48 (-11.92%)</td><td>3708.00 (-8.06%)</td><td>2347.70 (-12.67%)</td><td>657.59 (+3.04%)</td><td>28.58 (+14.51%)</td><td>21.12 (+14.50%)</td><td>18.10 (+8.77%)</td><td>17.71 (+12.13%)</td><td>4.82 <b>(+26.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>4249.20 (n/a)</td><td>3743.58 (n/a)</td><td>4033.10 (n/a)</td><td>2688.40 (n/a)</td><td>638.21 (n/a)</td><td>24.96 (n/a)</td><td>18.44 (n/a)</td><td>16.64 (n/a)</td><td>15.79 (n/a)</td><td>3.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>6.21 (-8.70%)</td><td>4.12 (-16.22%)</td><td>3.62 <b>(-25.06%)</b></td><td>3.34 (-5.29%)</td><td>1.21 (+1.72%)</td><td>1991.30 (+5.59%)</td><td>1702.36 <b>(+20.51%)</b></td><td>1836.00 <b>(+33.44%)</b></td><td>1070.70 (+9.53%)</td><td>381.12 (+17.96%)</td><td>1919.56 (-8.70%)</td><td>1273.33 (-16.22%)</td><td>1119.40 <b>(-25.06%)</b></td><td>1032.09 (-5.29%)</td><td>372.41 (+1.72%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>6.80 (n/a)</td><td>4.92 (n/a)</td><td>4.83 (n/a)</td><td>3.53 (n/a)</td><td>1.18 (n/a)</td><td>1885.90 (n/a)</td><td>1412.60 (n/a)</td><td>1375.90 (n/a)</td><td>977.50 (n/a)</td><td>323.11 (n/a)</td><td>2102.47 (n/a)</td><td>1519.88 (n/a)</td><td>1493.69 (n/a)</td><td>1089.79 (n/a)</td><td>366.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>13.48 (n/a)</td><td>12.85 (n/a)</td><td>12.85 (n/a)</td><td>11.92 (n/a)</td><td>0.61 (n/a)</td><td>13.47 (n/a)</td><td>12.84 (n/a)</td><td>12.84 (n/a)</td><td>11.91 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>25.26 (+0.71%)</td><td>22.32 (-8.56%)</td><td>24.31 (-0.24%)</td><td>15.50 <b>(-34.67%)</b></td><td>3.99 <b>(+716.25%)</b></td><td>25.24 (+0.71%)</td><td>22.31 (-8.56%)</td><td>24.30 (-0.24%)</td><td>15.49 <b>(-34.67%)</b></td><td>3.99 <b>(+716.25%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>25.08 (n/a)</td><td>24.41 (n/a)</td><td>24.37 (n/a)</td><td>23.73 (n/a)</td><td>0.49 (n/a)</td><td>25.06 (n/a)</td><td>24.39 (n/a)</td><td>24.36 (n/a)</td><td>23.71 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>40.55 (-0.29%)</td><td>39.10 (-0.16%)</td><td>39.50 (-0.42%)</td><td>37.21 (+1.20%)</td><td>1.26 <b>(-20.86%)</b></td><td>40.52 (-0.29%)</td><td>39.08 (-0.16%)</td><td>39.47 (-0.42%)</td><td>37.18 (+1.20%)</td><td>1.26 <b>(-20.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>40.67 (n/a)</td><td>39.16 (n/a)</td><td>39.66 (n/a)</td><td>36.76 (n/a)</td><td>1.59 (n/a)</td><td>40.64 (n/a)</td><td>39.14 (n/a)</td><td>39.64 (n/a)</td><td>36.74 (n/a)</td><td>1.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>42.05 (-6.51%)</td><td>37.74 (-12.59%)</td><td>40.73 (-5.49%)</td><td>25.29 <b>(-39.60%)</b></td><td>7.03 <b>(+450.37%)</b></td><td>42.03 (-6.51%)</td><td>37.71 (-12.59%)</td><td>40.71 (-5.49%)</td><td>25.28 <b>(-39.60%)</b></td><td>7.03 <b>(+450.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>44.98 (n/a)</td><td>43.17 (n/a)</td><td>43.10 (n/a)</td><td>41.88 (n/a)</td><td>1.28 (n/a)</td><td>44.95 (n/a)</td><td>43.15 (n/a)</td><td>43.07 (n/a)</td><td>41.85 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>13.50 (n/a)</td><td>13.01 (n/a)</td><td>13.06 (n/a)</td><td>12.49 (n/a)</td><td>0.43 (n/a)</td><td>13.49 (n/a)</td><td>13.00 (n/a)</td><td>13.05 (n/a)</td><td>12.49 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>25.10 (+1.45%)</td><td>23.84 (-2.57%)</td><td>24.03 (-1.71%)</td><td>22.09 (-8.85%)</td><td>1.23 <b>(+498.59%)</b></td><td>25.08 (+1.45%)</td><td>23.82 (-2.57%)</td><td>24.02 (-1.71%)</td><td>22.08 (-8.85%)</td><td>1.23 <b>(+498.59%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>24.74 (n/a)</td><td>24.47 (n/a)</td><td>24.45 (n/a)</td><td>24.24 (n/a)</td><td>0.21 (n/a)</td><td>24.72 (n/a)</td><td>24.45 (n/a)</td><td>24.44 (n/a)</td><td>24.23 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>40.01 (-1.39%)</td><td>38.63 (-2.94%)</td><td>38.79 (-2.24%)</td><td>36.36 (-6.66%)</td><td>1.40 <b>(+112.89%)</b></td><td>39.98 (-1.39%)</td><td>38.61 (-2.94%)</td><td>38.76 (-2.24%)</td><td>36.34 (-6.66%)</td><td>1.39 <b>(+112.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>40.57 (n/a)</td><td>39.80 (n/a)</td><td>39.68 (n/a)</td><td>38.96 (n/a)</td><td>0.66 (n/a)</td><td>40.55 (n/a)</td><td>39.78 (n/a)</td><td>39.65 (n/a)</td><td>38.93 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>42.93 (-5.47%)</td><td>41.07 (-4.57%)</td><td>41.99 (-1.24%)</td><td>37.91 (-9.22%)</td><td>2.21 <b>(+50.51%)</b></td><td>42.90 (-5.47%)</td><td>41.05 (-4.57%)</td><td>41.96 (-1.24%)</td><td>37.89 (-9.22%)</td><td>2.21 <b>(+50.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>45.41 (n/a)</td><td>43.04 (n/a)</td><td>42.52 (n/a)</td><td>41.76 (n/a)</td><td>1.47 (n/a)</td><td>45.38 (n/a)</td><td>43.01 (n/a)</td><td>42.49 (n/a)</td><td>41.74 (n/a)</td><td>1.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>9.05 (+0.46%)</td><td>8.71 (+0.70%)</td><td>8.92 (+1.62%)</td><td>8.24 (-0.35%)</td><td>0.40 (+17.07%)</td><td>9.03 (+0.46%)</td><td>8.69 (+0.70%)</td><td>8.91 (+1.62%)</td><td>8.22 (-0.35%)</td><td>0.40 (+17.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>9.00 (n/a)</td><td>8.65 (n/a)</td><td>8.78 (n/a)</td><td>8.27 (n/a)</td><td>0.34 (n/a)</td><td>8.99 (n/a)</td><td>8.63 (n/a)</td><td>8.76 (n/a)</td><td>8.25 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.04 (-7.73%)</td><td>0.87 (-14.80%)</td><td>0.88 (-15.49%)</td><td>0.73 (-19.54%)</td><td>0.12 (+8.50%)</td><td>1.03 (-7.73%)</td><td>0.86 (-14.80%)</td><td>0.86 (-15.49%)</td><td>0.72 (-19.54%)</td><td>0.11 (+8.50%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.13 (n/a)</td><td>1.02 (n/a)</td><td>1.04 (n/a)</td><td>0.91 (n/a)</td><td>0.11 (n/a)</td><td>1.11 (n/a)</td><td>1.00 (n/a)</td><td>1.02 (n/a)</td><td>0.89 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.24 (+2.04%)</td><td>1.08 (-2.05%)</td><td>1.06 (-4.57%)</td><td>1.01 (+1.72%)</td><td>0.09 (+14.04%)</td><td>1.22 (+2.04%)</td><td>1.07 (-2.05%)</td><td>1.05 (-4.57%)</td><td>1.00 (+1.72%)</td><td>0.09 (+14.04%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.21 (n/a)</td><td>1.11 (n/a)</td><td>1.11 (n/a)</td><td>1.00 (n/a)</td><td>0.08 (n/a)</td><td>1.20 (n/a)</td><td>1.09 (n/a)</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>17.70 (-5.42%)</td><td>17.06 (+0.06%)</td><td>17.25 (+2.39%)</td><td>16.29 (+2.30%)</td><td>0.63 <b>(-38.69%)</b></td><td>17.49 (-5.42%)</td><td>16.86 (+0.06%)</td><td>17.05 (+2.39%)</td><td>16.11 (+2.30%)</td><td>0.63 <b>(-38.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>18.71 (n/a)</td><td>17.05 (n/a)</td><td>16.85 (n/a)</td><td>15.93 (n/a)</td><td>1.03 (n/a)</td><td>18.49 (n/a)</td><td>16.85 (n/a)</td><td>16.66 (n/a)</td><td>15.74 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>14.11 (-0.11%)</td><td>13.22 (-3.90%)</td><td>13.11 (-4.19%)</td><td>12.32 (-8.10%)</td><td>0.66 <b>(+139.56%)</b></td><td>13.86 (-0.11%)</td><td>12.99 (-3.90%)</td><td>12.88 (-4.19%)</td><td>12.10 (-8.10%)</td><td>0.64 <b>(+139.57%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>14.12 (n/a)</td><td>13.75 (n/a)</td><td>13.68 (n/a)</td><td>13.40 (n/a)</td><td>0.27 (n/a)</td><td>13.87 (n/a)</td><td>13.51 (n/a)</td><td>13.44 (n/a)</td><td>13.17 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>7.86 (-1.14%)</td><td>7.34 (-1.44%)</td><td>7.21 (-5.79%)</td><td>6.85 (+0.83%)</td><td>0.39 <b>(-25.71%)</b></td><td>7.72 (-1.14%)</td><td>7.21 (-1.44%)</td><td>7.08 (-5.79%)</td><td>6.74 (+0.83%)</td><td>0.38 <b>(-25.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>7.95 (n/a)</td><td>7.44 (n/a)</td><td>7.65 (n/a)</td><td>6.80 (n/a)</td><td>0.53 (n/a)</td><td>7.81 (n/a)</td><td>7.32 (n/a)</td><td>7.52 (n/a)</td><td>6.68 (n/a)</td><td>0.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>6.03 (+1.43%)</td><td>5.71 (+5.45%)</td><td>5.97 (+6.25%)</td><td>4.77 (+0.85%)</td><td>0.54 (+12.61%)</td><td>5.93 (+1.43%)</td><td>5.62 (+5.45%)</td><td>5.87 (+6.25%)</td><td>4.69 (+0.85%)</td><td>0.53 (+12.61%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>5.95 (n/a)</td><td>5.41 (n/a)</td><td>5.62 (n/a)</td><td>4.73 (n/a)</td><td>0.48 (n/a)</td><td>5.85 (n/a)</td><td>5.32 (n/a)</td><td>5.53 (n/a)</td><td>4.65 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>13.33 (n/a)</td><td>11.67 (n/a)</td><td>11.89 (n/a)</td><td>10.53 (n/a)</td><td>1.16 (n/a)</td><td>13.32 (n/a)</td><td>11.66 (n/a)</td><td>11.88 (n/a)</td><td>10.52 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>13.15 (n/a)</td><td>11.83 (n/a)</td><td>11.77 (n/a)</td><td>10.79 (n/a)</td><td>0.95 (n/a)</td><td>13.14 (n/a)</td><td>11.83 (n/a)</td><td>11.77 (n/a)</td><td>10.78 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>165.24 (n/a)</td><td>153.10 (n/a)</td><td>133.30 (n/a)</td><td>33.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>169.82 (n/a)</td><td>176.60 (n/a)</td><td>139.00 (n/a)</td><td>19.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>204.30 (n/a)</td><td>156.34 (n/a)</td><td>152.70 (n/a)</td><td>96.60 (n/a)</td><td>43.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>173.96 (n/a)</td><td>184.00 (n/a)</td><td>137.80 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>172.40 (n/a)</td><td>179.40 (n/a)</td><td>146.80 (n/a)</td><td>23.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.80 (n/a)</td><td>187.12 (n/a)</td><td>175.00 (n/a)</td><td>153.80 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>185.42 (n/a)</td><td>183.10 (n/a)</td><td>141.20 (n/a)</td><td>34.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>335.90 (n/a)</td><td>232.02 (n/a)</td><td>190.30 (n/a)</td><td>176.40 (n/a)</td><td>71.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (+1.49%)</td><td>0.05 (-0.39%)</td><td>0.05 (+7.56%)</td><td>0.04 (-12.43%)</td><td>0.01 <b>(+76.11%)</b></td><td>219.20 (+14.23%)</td><td>169.84 (+3.12%)</td><td>153.00 (-7.05%)</td><td>136.20 (-1.45%)</td><td>37.83 <b>(+98.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.90 (n/a)</td><td>164.70 (n/a)</td><td>164.60 (n/a)</td><td>138.20 (n/a)</td><td>19.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+7.29%)</td><td>0.05 (+17.36%)</td><td>0.05 (+7.92%)</td><td>0.04 <b>(+100.07%)</b></td><td>0.01 <b>(-26.73%)</b></td><td>187.50 <b>(-50.03%)</b></td><td>155.82 <b>(-22.88%)</b></td><td>158.10 (-7.33%)</td><td>118.10 (-6.79%)</td><td>31.17 <b>(-68.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>375.20 (n/a)</td><td>202.06 (n/a)</td><td>170.60 (n/a)</td><td>126.70 (n/a)</td><td>98.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-3.49%)</td><td>0.05 (+1.92%)</td><td>0.05 (-3.14%)</td><td>0.04 (+10.09%)</td><td>0.01 <b>(-28.89%)</b></td><td>187.00 (-9.14%)</td><td>161.12 (-3.17%)</td><td>160.10 (+3.29%)</td><td>136.60 (+3.56%)</td><td>19.73 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>166.40 (n/a)</td><td>155.00 (n/a)</td><td>131.90 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-15.67%)</td><td>0.05 (-4.05%)</td><td>0.05 (+6.60%)</td><td>0.04 (-9.99%)</td><td>0.01 <b>(-23.87%)</b></td><td>202.80 (+11.12%)</td><td>163.60 (+3.57%)</td><td>159.10 (-6.19%)</td><td>136.70 (+18.56%)</td><td>27.16 (+1.04%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>157.96 (n/a)</td><td>169.60 (n/a)</td><td>115.30 (n/a)</td><td>26.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 <b>(-26.49%)</b></td><td>0.05 (-6.51%)</td><td>0.05 (+3.46%)</td><td>0.04 <b>(+63.26%)</b></td><td>0.01 <b>(-70.73%)</b></td><td>183.70 <b>(-38.77%)</b></td><td>161.56 (-7.26%)</td><td>161.00 (-3.36%)</td><td>132.40 <b>(+36.07%)</b></td><td>19.63 <b>(-75.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>300.00 (n/a)</td><td>174.20 (n/a)</td><td>166.60 (n/a)</td><td>97.30 (n/a)</td><td>80.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-13.96%)</td><td>0.05 (-14.56%)</td><td>0.05 (-14.75%)</td><td>0.04 (-7.65%)</td><td>0.01 (-17.08%)</td><td>206.20 (+8.30%)</td><td>178.62 (+16.70%)</td><td>178.30 (+17.30%)</td><td>138.60 (+16.28%)</td><td>26.37 (+3.92%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>153.06 (n/a)</td><td>152.00 (n/a)</td><td>119.20 (n/a)</td><td>25.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (-5.61%)</td><td>0.05 (+1.98%)</td><td>0.05 (+2.36%)</td><td>0.04 (+0.63%)</td><td>0.00 (-19.59%)</td><td>201.70 (-0.59%)</td><td>176.12 (-2.27%)</td><td>173.80 (-2.30%)</td><td>160.60 (+5.94%)</td><td>16.95 (-16.06%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.90 (n/a)</td><td>180.22 (n/a)</td><td>177.90 (n/a)</td><td>151.60 (n/a)</td><td>20.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (-0.22%)</td><td>0.04 (-2.64%)</td><td>0.05 (-0.48%)</td><td>0.04 (-11.37%)</td><td>0.01 <b>(+33.01%)</b></td><td>222.70 (+12.87%)</td><td>185.98 (+3.71%)</td><td>179.80 (+0.50%)</td><td>151.70 (+0.26%)</td><td>28.67 <b>(+50.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>179.32 (n/a)</td><td>178.90 (n/a)</td><td>151.30 (n/a)</td><td>19.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 <b>(-21.95%)</b></td><td>0.04 (-17.37%)</td><td>0.04 <b>(-23.25%)</b></td><td>0.04 (-0.82%)</td><td>0.01 <b>(-52.84%)</b></td><td>223.40 (+0.81%)</td><td>192.48 (+17.25%)</td><td>196.40 <b>(+30.33%)</b></td><td>164.40 <b>(+28.14%)</b></td><td>24.61 <b>(-38.80%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>164.16 (n/a)</td><td>150.70 (n/a)</td><td>128.30 (n/a)</td><td>40.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 <b>(+49.90%)</b></td><td>0.05 (+11.13%)</td><td>0.04 (-9.60%)</td><td>0.03 (+16.68%)</td><td>0.02 <b>(+111.79%)</b></td><td>238.60 (-14.30%)</td><td>195.92 (-5.56%)</td><td>226.30 (+10.61%)</td><td>111.80 <b>(-33.29%)</b></td><td>53.26 <b>(+20.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.40 (n/a)</td><td>207.46 (n/a)</td><td>204.60 (n/a)</td><td>167.60 (n/a)</td><td>44.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+12.67%)</td><td>0.05 (-0.61%)</td><td>0.05 (-10.08%)</td><td>0.04 (+2.08%)</td><td>0.01 <b>(+21.40%)</b></td><td>194.10 (-2.07%)</td><td>162.26 (+1.01%)</td><td>162.70 (+11.21%)</td><td>125.80 (-11.28%)</td><td>24.84 (+3.93%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>160.64 (n/a)</td><td>146.30 (n/a)</td><td>141.80 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.04 (+1.92%)</td><td>0.04 (+5.88%)</td><td>0.04 (+5.22%)</td><td>0.03 <b>(+43.82%)</b></td><td>0.00 <b>(-40.60%)</b></td><td>245.00 <b>(-30.48%)</b></td><td>214.94 (-9.00%)</td><td>207.00 (-4.96%)</td><td>184.30 (-1.86%)</td><td>25.99 <b>(-60.79%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>352.40 (n/a)</td><td>236.20 (n/a)</td><td>217.80 (n/a)</td><td>187.80 (n/a)</td><td>66.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (-18.32%)</td><td>0.05 (-9.76%)</td><td>0.05 (-2.70%)</td><td>0.04 (-3.78%)</td><td>0.00 <b>(-54.73%)</b></td><td>193.10 (+3.93%)</td><td>177.10 (+8.90%)</td><td>178.60 (+2.76%)</td><td>155.30 <b>(+22.38%)</b></td><td>15.05 <b>(-43.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>162.62 (n/a)</td><td>173.80 (n/a)</td><td>126.90 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-1.22%)</td><td>0.05 (+9.09%)</td><td>0.05 (+16.39%)</td><td>0.04 <b>(+22.07%)</b></td><td>0.01 <b>(-37.06%)</b></td><td>192.30 (-18.07%)</td><td>160.02 (-10.90%)</td><td>153.20 (-14.08%)</td><td>134.40 (+1.20%)</td><td>22.03 <b>(-46.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.70 (n/a)</td><td>179.60 (n/a)</td><td>178.30 (n/a)</td><td>132.80 (n/a)</td><td>41.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 <b>(+38.93%)</b></td><td>0.05 (+19.69%)</td><td>0.05 (+7.48%)</td><td>0.04 (+12.15%)</td><td>0.01 <b>(+137.82%)</b></td><td>194.70 (-10.81%)</td><td>163.28 (-14.50%)</td><td>171.20 (-6.96%)</td><td>119.30 <b>(-28.00%)</b></td><td>30.80 <b>(+51.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.30 (n/a)</td><td>190.96 (n/a)</td><td>184.00 (n/a)</td><td>165.70 (n/a)</td><td>20.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (+17.09%)</td><td>0.05 (+12.45%)</td><td>0.05 (+2.65%)</td><td>0.03 (+1.21%)</td><td>0.01 <b>(+66.06%)</b></td><td>253.40 (-1.21%)</td><td>175.48 (-8.03%)</td><td>180.20 (-2.54%)</td><td>128.00 (-14.55%)</td><td>51.21 <b>(+29.54%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.50 (n/a)</td><td>190.80 (n/a)</td><td>184.90 (n/a)</td><td>149.80 (n/a)</td><td>39.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (+5.50%)</td><td>0.05 (+5.64%)</td><td>0.05 (+4.81%)</td><td>0.04 <b>(+27.66%)</b></td><td>0.01 (-14.66%)</td><td>216.50 <b>(-21.67%)</b></td><td>183.24 (-7.20%)</td><td>173.40 (-4.62%)</td><td>141.60 (-5.22%)</td><td>31.41 <b>(-36.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.40 (n/a)</td><td>197.46 (n/a)</td><td>181.80 (n/a)</td><td>149.40 (n/a)</td><td>49.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 <b>(+48.42%)</b></td><td>0.05 (+19.53%)</td><td>0.06 <b>(+22.95%)</b></td><td>0.04 (-13.00%)</td><td>0.01 <b>(+398.99%)</b></td><td>232.50 (+14.93%)</td><td>164.76 (-11.60%)</td><td>147.40 (-18.65%)</td><td>118.20 <b>(-32.61%)</b></td><td>46.06 <b>(+290.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>186.38 (n/a)</td><td>181.20 (n/a)</td><td>175.40 (n/a)</td><td>11.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52738.60 (n/a)</td><td>52635.22 (n/a)</td><td>52623.40 (n/a)</td><td>52527.20 (n/a)</td><td>79.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.19 (+8.39%)</td><td>0.15 (+2.01%)</td><td>0.15 (+4.21%)</td><td>0.12 (-8.48%)</td><td>0.03 <b>(+51.14%)</b></td><td>201.30 (+9.28%)</td><td>164.18 (-0.10%)</td><td>167.00 (-4.02%)</td><td>129.40 (-7.70%)</td><td>33.11 <b>(+51.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>184.20 (n/a)</td><td>164.34 (n/a)</td><td>174.00 (n/a)</td><td>140.20 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.26 (-7.91%)</td><td>0.23 (-13.42%)</td><td>0.23 (-13.41%)</td><td>0.19 <b>(-20.66%)</b></td><td>0.03 <b>(+39.69%)</b></td><td>218.00 <b>(+26.01%)</b></td><td>183.08 (+16.30%)</td><td>180.20 (+15.51%)</td><td>157.50 (+8.55%)</td><td>22.04 <b>(+94.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>173.00 (n/a)</td><td>157.42 (n/a)</td><td>156.00 (n/a)</td><td>145.10 (n/a)</td><td>11.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-13.14%)</td><td>0.03 (-0.70%)</td><td>0.03 (+0.15%)</td><td>0.03 <b>(+20.19%)</b></td><td>0.00 <b>(-60.78%)</b></td><td>190.90 (-16.82%)</td><td>174.74 (-1.58%)</td><td>173.10 (-0.17%)</td><td>157.70 (+15.11%)</td><td>12.32 <b>(-62.93%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.50 (n/a)</td><td>177.54 (n/a)</td><td>173.40 (n/a)</td><td>137.00 (n/a)</td><td>33.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+14.21%)</td><td>0.05 (+14.43%)</td><td>0.05 (+12.33%)</td><td>0.04 (-6.79%)</td><td>0.01 <b>(+64.24%)</b></td><td>232.70 (+7.28%)</td><td>161.78 (-9.75%)</td><td>156.30 (-10.94%)</td><td>121.40 (-12.41%)</td><td>44.32 <b>(+56.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>179.26 (n/a)</td><td>175.50 (n/a)</td><td>138.60 (n/a)</td><td>28.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.09 <b>(-20.68%)</b></td><td>0.07 <b>(-21.16%)</b></td><td>0.07 <b>(-24.63%)</b></td><td>0.06 (-3.59%)</td><td>0.01 <b>(-50.63%)</b></td><td>193.30 (+3.70%)</td><td>172.76 <b>(+22.52%)</b></td><td>177.80 <b>(+32.69%)</b></td><td>134.40 <b>(+26.08%)</b></td><td>23.30 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>186.40 (n/a)</td><td>141.00 (n/a)</td><td>134.00 (n/a)</td><td>106.60 (n/a)</td><td>35.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+13.50%)</td><td>0.06 (+5.35%)</td><td>0.06 (-0.40%)</td><td>0.05 (+4.98%)</td><td>0.01 <b>(+33.32%)</b></td><td>168.20 (-4.76%)</td><td>146.86 (-4.57%)</td><td>148.70 (+0.41%)</td><td>121.60 (-11.88%)</td><td>20.11 (+13.65%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.60 (n/a)</td><td>153.90 (n/a)</td><td>148.10 (n/a)</td><td>138.00 (n/a)</td><td>17.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 <b>(-21.78%)</b></td><td>0.05 (-18.57%)</td><td>0.05 (-16.68%)</td><td>0.04 (-10.63%)</td><td>0.01 <b>(-41.26%)</b></td><td>228.70 (+11.89%)</td><td>206.24 <b>(+21.55%)</b></td><td>208.20 (+20.00%)</td><td>170.60 <b>(+27.79%)</b></td><td>21.86 (-16.71%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.40 (n/a)</td><td>169.68 (n/a)</td><td>173.50 (n/a)</td><td>133.50 (n/a)</td><td>26.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (+1.30%)</td><td>0.05 (-13.52%)</td><td>0.04 <b>(-23.30%)</b></td><td>0.04 (-16.78%)</td><td>0.01 <b>(+45.57%)</b></td><td>202.70 <b>(+20.15%)</b></td><td>175.56 (+17.29%)</td><td>183.40 <b>(+30.35%)</b></td><td>134.00 (-1.25%)</td><td>28.74 <b>(+72.93%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.70 (n/a)</td><td>149.68 (n/a)</td><td>140.70 (n/a)</td><td>135.70 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+3.48%)</td><td>0.06 (-3.45%)</td><td>0.06 (-3.02%)</td><td>0.05 (-3.59%)</td><td>0.01 (+19.36%)</td><td>220.00 (+3.72%)</td><td>188.80 (+4.30%)</td><td>180.40 (+3.14%)</td><td>145.70 (-3.38%)</td><td>31.05 <b>(+20.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>181.02 (n/a)</td><td>174.90 (n/a)</td><td>150.80 (n/a)</td><td>25.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-4.33%)</td><td>0.04 (-16.43%)</td><td>0.04 (-13.14%)</td><td>0.03 <b>(-29.35%)</b></td><td>0.01 <b>(+24.01%)</b></td><td>303.40 <b>(+41.58%)</b></td><td>202.54 <b>(+23.73%)</b></td><td>186.60 (+15.11%)</td><td>144.30 (+4.49%)</td><td>60.00 <b>(+93.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>163.70 (n/a)</td><td>162.10 (n/a)</td><td>138.10 (n/a)</td><td>30.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-11.15%)</td><td>0.05 (-9.67%)</td><td>0.05 (-14.16%)</td><td>0.04 (-10.43%)</td><td>0.01 (+11.25%)</td><td>244.50 (+11.64%)</td><td>188.38 (+12.60%)</td><td>181.80 (+16.46%)</td><td>142.40 (+12.57%)</td><td>46.97 <b>(+36.04%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>167.30 (n/a)</td><td>156.10 (n/a)</td><td>126.50 (n/a)</td><td>34.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+15.89%)</td><td>0.05 (+8.20%)</td><td>0.05 (+4.03%)</td><td>0.05 (+12.44%)</td><td>0.01 <b>(+30.83%)</b></td><td>177.50 (-11.07%)</td><td>163.02 (-7.09%)</td><td>171.50 (-3.87%)</td><td>119.40 (-13.73%)</td><td>24.60 (-1.30%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.60 (n/a)</td><td>175.46 (n/a)</td><td>178.40 (n/a)</td><td>138.40 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 (-10.76%)</td><td>0.05 (-10.70%)</td><td>0.05 (-6.17%)</td><td>0.04 <b>(-23.44%)</b></td><td>0.01 <b>(+48.34%)</b></td><td>216.00 <b>(+30.59%)</b></td><td>179.06 (+13.01%)</td><td>172.50 (+6.55%)</td><td>156.00 (+12.07%)</td><td>24.00 <b>(+118.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>165.40 (n/a)</td><td>158.44 (n/a)</td><td>161.90 (n/a)</td><td>139.20 (n/a)</td><td>10.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.06 <b>(+20.74%)</b></td><td>0.05 (+16.37%)</td><td>0.05 (+5.68%)</td><td>0.04 <b>(+62.94%)</b></td><td>0.01 <b>(-25.17%)</b></td><td>199.40 <b>(-38.63%)</b></td><td>173.28 (-17.87%)</td><td>180.00 (-5.41%)</td><td>135.50 (-17.23%)</td><td>24.83 <b>(-62.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.90 (n/a)</td><td>210.98 (n/a)</td><td>190.30 (n/a)</td><td>163.70 (n/a)</td><td>66.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (-1.54%)</td><td>0.04 (+0.51%)</td><td>0.04 (-12.81%)</td><td>0.04 <b>(+37.39%)</b></td><td>0.00 <b>(-49.29%)</b></td><td>220.50 <b>(-27.23%)</b></td><td>198.00 (-4.41%)</td><td>203.70 (+14.70%)</td><td>166.10 (+1.53%)</td><td>20.55 <b>(-63.85%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>303.00 (n/a)</td><td>207.14 (n/a)</td><td>177.60 (n/a)</td><td>163.60 (n/a)</td><td>56.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.07 (+5.58%)</td><td>0.05 (-12.10%)</td><td>0.04 (-16.78%)</td><td>0.03 <b>(-33.83%)</b></td><td>0.01 <b>(+99.19%)</b></td><td>277.90 <b>(+51.11%)</b></td><td>192.66 <b>(+20.61%)</b></td><td>192.00 <b>(+20.23%)</b></td><td>122.50 (-5.26%)</td><td>57.15 <b>(+189.18%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>159.74 (n/a)</td><td>159.70 (n/a)</td><td>129.30 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.05 (-8.28%)</td><td>0.04 (-18.60%)</td><td>0.04 <b>(-23.23%)</b></td><td>0.03 <b>(-37.71%)</b></td><td>0.01 <b>(+84.14%)</b></td><td>328.00 <b>(+60.55%)</b></td><td>227.30 <b>(+27.90%)</b></td><td>221.60 <b>(+30.28%)</b></td><td>171.70 (+9.02%)</td><td>60.63 <b>(+228.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>177.72 (n/a)</td><td>170.10 (n/a)</td><td>157.50 (n/a)</td><td>18.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.04 <b>(-30.25%)</b></td><td>0.04 (-16.36%)</td><td>0.04 (-9.30%)</td><td>0.02 <b>(-29.65%)</b></td><td>0.01 <b>(-32.23%)</b></td><td>328.50 <b>(+42.15%)</b></td><td>234.64 (+19.57%)</td><td>224.30 (+10.22%)</td><td>193.80 <b>(+43.34%)</b></td><td>54.23 <b>(+48.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.10 (n/a)</td><td>196.24 (n/a)</td><td>203.50 (n/a)</td><td>135.20 (n/a)</td><td>36.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.68 (-2.28%)</td><td>0.57 (+1.85%)</td><td>0.59 (+12.01%)</td><td>0.43 (-12.95%)</td><td>0.10 <b>(+21.43%)</b></td><td>228.70 (+14.87%)</td><td>178.32 (-0.68%)</td><td>166.60 (-10.72%)</td><td>144.90 (+2.33%)</td><td>34.11 <b>(+43.56%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.69 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.49 (n/a)</td><td>0.08 (n/a)</td><td>199.10 (n/a)</td><td>179.54 (n/a)</td><td>186.60 (n/a)</td><td>141.60 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.75 (+7.19%)</td><td>0.65 (+10.52%)</td><td>0.69 (+10.82%)</td><td>0.53 <b>(+21.88%)</b></td><td>0.11 (-10.36%)</td><td>184.20 (-17.95%)</td><td>154.74 (-10.67%)</td><td>143.50 (-9.75%)</td><td>131.10 (-6.69%)</td><td>26.56 <b>(-29.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.70 (n/a)</td><td>0.59 (n/a)</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>0.12 (n/a)</td><td>224.50 (n/a)</td><td>173.22 (n/a)</td><td>159.00 (n/a)</td><td>140.50 (n/a)</td><td>37.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.68 (-9.03%)</td><td>0.52 (+1.28%)</td><td>0.50 (+6.93%)</td><td>0.40 (-1.38%)</td><td>0.11 <b>(-20.42%)</b></td><td>248.00 (+1.39%)</td><td>195.80 (-2.77%)</td><td>195.40 (-6.51%)</td><td>144.50 (+9.97%)</td><td>41.39 (-12.18%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.75 (n/a)</td><td>0.51 (n/a)</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.14 (n/a)</td><td>244.60 (n/a)</td><td>201.38 (n/a)</td><td>209.00 (n/a)</td><td>131.40 (n/a)</td><td>47.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.83 <b>(+39.00%)</b></td><td>0.60 <b>(+53.25%)</b></td><td>0.61 <b>(+68.27%)</b></td><td>0.39 <b>(+35.57%)</b></td><td>0.15 <b>(+23.78%)</b></td><td>250.80 <b>(-26.24%)</b></td><td>173.32 <b>(-35.58%)</b></td><td>162.50 <b>(-40.56%)</b></td><td>119.10 <b>(-28.08%)</b></td><td>48.08 <b>(-33.68%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.59 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.12 (n/a)</td><td>340.00 (n/a)</td><td>269.06 (n/a)</td><td>273.40 (n/a)</td><td>165.60 (n/a)</td><td>72.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.48 (-11.78%)</td><td>0.44 (-2.28%)</td><td>0.46 (+7.13%)</td><td>0.36 (-5.44%)</td><td>0.05 <b>(-38.06%)</b></td><td>203.00 (+5.78%)</td><td>168.34 (+1.19%)</td><td>159.90 (-6.71%)</td><td>153.60 (+13.36%)</td><td>19.93 <b>(-24.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.07 (n/a)</td><td>191.90 (n/a)</td><td>166.36 (n/a)</td><td>171.40 (n/a)</td><td>135.50 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.65 <b>(+31.07%)</b></td><td>0.50 (+18.12%)</td><td>0.49 (+7.05%)</td><td>0.41 <b>(+30.45%)</b></td><td>0.10 <b>(+33.22%)</b></td><td>179.10 <b>(-23.36%)</b></td><td>151.40 (-15.30%)</td><td>152.00 (-6.58%)</td><td>113.20 <b>(-23.72%)</b></td><td>26.42 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>233.70 (n/a)</td><td>178.74 (n/a)</td><td>162.70 (n/a)</td><td>148.40 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.53 (-2.18%)</td><td>0.44 (+3.38%)</td><td>0.44 (+6.24%)</td><td>0.31 (-2.58%)</td><td>0.08 (-10.07%)</td><td>237.50 (+2.64%)</td><td>173.42 (-3.70%)</td><td>167.00 (-5.86%)</td><td>138.00 (+2.22%)</td><td>38.07 (-2.13%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.55 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.09 (n/a)</td><td>231.40 (n/a)</td><td>180.08 (n/a)</td><td>177.40 (n/a)</td><td>135.00 (n/a)</td><td>38.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.60 <b>(+30.14%)</b></td><td>0.46 (+18.01%)</td><td>0.44 (+14.58%)</td><td>0.36 (+8.81%)</td><td>0.10 <b>(+112.29%)</b></td><td>204.20 (-8.10%)</td><td>167.10 (-12.97%)</td><td>168.10 (-12.72%)</td><td>122.40 <b>(-23.16%)</b></td><td>35.63 <b>(+54.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.05 (n/a)</td><td>222.20 (n/a)</td><td>192.00 (n/a)</td><td>192.60 (n/a)</td><td>159.30 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.70 <b>(-34.51%)</b></td><td>0.69 (-17.60%)</td><td>0.68 <b>(-30.63%)</b></td><td>0.68 <b>(+28.42%)</b></td><td>0.01 <b>(-95.71%)</b></td><td>193.50 <b>(-22.13%)</b></td><td>190.74 (+11.48%)</td><td>191.70 <b>(+44.14%)</b></td><td>187.20 <b>(+52.69%)</b></td><td>2.96 <b>(-94.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.07 (n/a)</td><td>0.83 (n/a)</td><td>0.99 (n/a)</td><td>0.53 (n/a)</td><td>0.25 (n/a)</td><td>248.50 (n/a)</td><td>171.10 (n/a)</td><td>133.00 (n/a)</td><td>122.60 (n/a)</td><td>58.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.74 <b>(-25.67%)</b></td><td>0.61 (-16.83%)</td><td>0.58 (-18.14%)</td><td>0.50 (-5.87%)</td><td>0.11 <b>(-35.02%)</b></td><td>260.60 (+6.24%)</td><td>220.26 (+18.43%)</td><td>227.00 <b>(+22.17%)</b></td><td>176.40 <b>(+34.55%)</b></td><td>38.52 (-6.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.00 (n/a)</td><td>0.73 (n/a)</td><td>0.71 (n/a)</td><td>0.53 (n/a)</td><td>0.17 (n/a)</td><td>245.30 (n/a)</td><td>185.98 (n/a)</td><td>185.80 (n/a)</td><td>131.10 (n/a)</td><td>41.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.90 (-8.36%)</td><td>0.76 (+6.01%)</td><td>0.80 (+15.80%)</td><td>0.58 <b>(+30.15%)</b></td><td>0.13 <b>(-34.83%)</b></td><td>224.80 <b>(-23.17%)</b></td><td>176.68 (-9.65%)</td><td>164.10 (-13.63%)</td><td>146.00 (+9.12%)</td><td>32.43 <b>(-46.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.98 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.45 (n/a)</td><td>0.20 (n/a)</td><td>292.60 (n/a)</td><td>195.54 (n/a)</td><td>190.00 (n/a)</td><td>133.80 (n/a)</td><td>60.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-11.03%)</td><td>0.03 (+0.45%)</td><td>0.02 (+2.94%)</td><td>0.02 (+14.10%)</td><td>0.00 <b>(-37.25%)</b></td><td>189.40 (-12.40%)</td><td>163.32 (-3.28%)</td><td>171.50 (-2.83%)</td><td>128.90 (+12.38%)</td><td>24.53 <b>(-37.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.20 (n/a)</td><td>168.86 (n/a)</td><td>176.50 (n/a)</td><td>114.70 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.02 <b>(-23.14%)</b></td><td>0.02 (-19.02%)</td><td>0.02 <b>(-20.45%)</b></td><td>0.02 (-5.29%)</td><td>0.00 <b>(-48.94%)</b></td><td>236.20 (+5.59%)</td><td>192.06 <b>(+20.79%)</b></td><td>184.30 <b>(+25.72%)</b></td><td>173.80 <b>(+30.09%)</b></td><td>25.38 <b>(-31.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.70 (n/a)</td><td>159.00 (n/a)</td><td>146.60 (n/a)</td><td>133.60 (n/a)</td><td>36.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-3.92%)</td><td>0.03 (+0.94%)</td><td>0.02 (-10.17%)</td><td>0.02 (+11.44%)</td><td>0.00 <b>(-24.30%)</b></td><td>193.40 (-10.30%)</td><td>167.00 (-2.75%)</td><td>172.60 (+11.35%)</td><td>134.30 (+4.03%)</td><td>26.07 <b>(-31.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>215.60 (n/a)</td><td>171.72 (n/a)</td><td>155.00 (n/a)</td><td>129.10 (n/a)</td><td>38.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.02 (-13.99%)</td><td>0.84 (+2.67%)</td><td>0.78 (+6.70%)</td><td>0.70 (+3.74%)</td><td>0.13 <b>(-36.35%)</b></td><td>189.80 (-3.56%)</td><td>161.08 (-4.65%)</td><td>168.30 (-6.29%)</td><td>129.60 (+16.23%)</td><td>24.59 <b>(-25.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.19 (n/a)</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>0.67 (n/a)</td><td>0.21 (n/a)</td><td>196.80 (n/a)</td><td>168.94 (n/a)</td><td>179.60 (n/a)</td><td>111.50 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.04 (+4.05%)</td><td>0.88 (+6.38%)</td><td>1.03 <b>(+23.97%)</b></td><td>0.58 (-5.13%)</td><td>0.22 <b>(+29.53%)</b></td><td>229.30 (+5.43%)</td><td>158.12 (-3.83%)</td><td>128.00 (-19.29%)</td><td>126.70 (-3.94%)</td><td>45.72 <b>(+28.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.00 (n/a)</td><td>0.83 (n/a)</td><td>0.83 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>217.50 (n/a)</td><td>164.42 (n/a)</td><td>158.60 (n/a)</td><td>131.90 (n/a)</td><td>35.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.02 (+13.40%)</td><td>0.76 (-4.64%)</td><td>0.68 <b>(-22.30%)</b></td><td>0.64 (+4.71%)</td><td>0.16 <b>(+21.02%)</b></td><td>205.30 (-4.51%)</td><td>179.26 (+5.47%)</td><td>193.60 <b>(+28.72%)</b></td><td>129.40 (-11.79%)</td><td>31.41 (+3.11%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.90 (n/a)</td><td>0.80 (n/a)</td><td>0.88 (n/a)</td><td>0.61 (n/a)</td><td>0.13 (n/a)</td><td>215.00 (n/a)</td><td>169.96 (n/a)</td><td>150.40 (n/a)</td><td>146.70 (n/a)</td><td>30.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.81 <b>(-29.06%)</b></td><td>0.77 (-10.28%)</td><td>0.79 (-13.52%)</td><td>0.67 (+12.72%)</td><td>0.06 <b>(-76.98%)</b></td><td>196.30 (-11.26%)</td><td>172.28 (+4.70%)</td><td>167.50 (+15.68%)</td><td>162.80 <b>(+40.95%)</b></td><td>13.58 <b>(-71.85%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.14 (n/a)</td><td>0.86 (n/a)</td><td>0.91 (n/a)</td><td>0.60 (n/a)</td><td>0.24 (n/a)</td><td>221.20 (n/a)</td><td>164.54 (n/a)</td><td>144.80 (n/a)</td><td>115.50 (n/a)</td><td>48.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.05 (-1.25%)</td><td>0.81 (-12.38%)</td><td>0.76 (-16.93%)</td><td>0.69 (-14.83%)</td><td>0.14 <b>(+45.20%)</b></td><td>192.20 (+17.41%)</td><td>167.10 (+15.54%)</td><td>174.20 <b>(+20.39%)</b></td><td>126.00 (+1.29%)</td><td>25.03 <b>(+67.46%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.06 (n/a)</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.81 (n/a)</td><td>0.10 (n/a)</td><td>163.70 (n/a)</td><td>144.62 (n/a)</td><td>144.70 (n/a)</td><td>124.40 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (+11.82%)</td><td>0.02 (-3.74%)</td><td>0.02 (-16.46%)</td><td>0.02 (-0.12%)</td><td>0.01 (+12.56%)</td><td>231.90 (+0.13%)</td><td>176.88 (+4.23%)</td><td>179.80 (+19.71%)</td><td>125.00 (-10.52%)</td><td>38.15 (-0.76%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.60 (n/a)</td><td>169.70 (n/a)</td><td>150.20 (n/a)</td><td>139.70 (n/a)</td><td>38.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.03 (-6.81%)</td><td>0.02 (-15.98%)</td><td>0.02 <b>(-20.54%)</b></td><td>0.02 (-15.06%)</td><td>0.01 (+1.04%)</td><td>246.20 (+17.69%)</td><td>178.72 <b>(+20.09%)</b></td><td>177.30 <b>(+25.83%)</b></td><td>133.30 (+7.24%)</td><td>43.94 <b>(+25.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.20 (n/a)</td><td>148.82 (n/a)</td><td>140.90 (n/a)</td><td>124.30 (n/a)</td><td>34.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.00 (+4.65%)</td><td>0.00 (-1.40%)</td><td>0.00 (-2.33%)</td><td>0.00 (-7.14%)</td><td>0.00 <b>(+433.85%)</b></td><td>1043.90 (+7.08%)</td><td>974.80 (+2.20%)</td><td>983.71 (+3.57%)</td><td>909.59 (-3.97%)</td><td>51.62 <b>(+336.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>974.86 (n/a)</td><td>953.86 (n/a)</td><td>949.82 (n/a)</td><td>947.15 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.01 (+0.00%)</td><td>0.01 (-1.24%)</td><td>0.01 (+1.25%)</td><td>0.01 (-6.25%)</td><td>0.00 <b>(+106.91%)</b></td><td>1097.21 (+6.65%)</td><td>1030.21 (+1.34%)</td><td>1009.11 (-1.68%)</td><td>980.58 (+0.67%)</td><td>47.59 <b>(+100.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1028.78 (n/a)</td><td>1016.59 (n/a)</td><td>1026.36 (n/a)</td><td>974.08 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.96 (-0.50%)</td><td>0.95 (-0.42%)</td><td>0.95 (-0.09%)</td><td>0.94 (-0.12%)</td><td>0.01 (+4.44%)</td><td>2235.83 (+0.12%)</td><td>2206.11 (+0.42%)</td><td>2196.16 (+0.09%)</td><td>2176.17 (+0.50%)</td><td>27.14 (+5.39%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.96 (n/a)</td><td>0.94 (n/a)</td><td>0.01 (n/a)</td><td>2233.19 (n/a)</td><td>2196.77 (n/a)</td><td>2194.22 (n/a)</td><td>2165.43 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.89 (-2.28%)</td><td>0.89 (+0.34%)</td><td>0.89 (+1.14%)</td><td>0.88 (+1.06%)</td><td>0.01 <b>(-66.99%)</b></td><td>2381.33 (-1.04%)</td><td>2365.03 (-0.37%)</td><td>2362.13 (-1.13%)</td><td>2344.66 (+2.33%)</td><td>15.97 <b>(-66.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.92 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.02 (n/a)</td><td>2406.40 (n/a)</td><td>2373.91 (n/a)</td><td>2389.21 (n/a)</td><td>2291.31 (n/a)</td><td>47.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.61 (+0.29%)</td><td>0.58 (+1.27%)</td><td>0.59 (+0.76%)</td><td>0.53 (+3.88%)</td><td>0.03 <b>(-26.27%)</b></td><td>980.60 (-3.73%)</td><td>903.22 (-1.43%)</td><td>888.90 (-0.75%)</td><td>859.80 (-0.29%)</td><td>46.49 <b>(-28.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.61 (n/a)</td><td>0.57 (n/a)</td><td>0.59 (n/a)</td><td>0.51 (n/a)</td><td>0.04 (n/a)</td><td>1018.60 (n/a)</td><td>916.34 (n/a)</td><td>895.60 (n/a)</td><td>862.30 (n/a)</td><td>64.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>0.64 (-4.05%)</td><td>0.63 (+4.17%)</td><td>0.64 (+0.79%)</td><td>0.61 <b>(+24.77%)</b></td><td>0.01 <b>(-81.66%)</b></td><td>1713.20 (-19.85%)</td><td>1655.02 (-5.13%)</td><td>1635.70 (-0.79%)</td><td>1631.70 (+4.22%)</td><td>34.42 <b>(-84.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.64 (n/a)</td><td>0.49 (n/a)</td><td>0.07 (n/a)</td><td>2137.60 (n/a)</td><td>1744.52 (n/a)</td><td>1648.70 (n/a)</td><td>1565.60 (n/a)</td><td>228.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 01:17:49</td><td>1.12 (+4.96%)</td><td>1.00 (+4.14%)</td><td>0.97 (+0.69%)</td><td>0.94 (+6.83%)</td><td>0.07 (-7.59%)</td><td>555.10 (-6.39%)</td><td>525.74 (-4.10%)</td><td>539.00 (-0.68%)</td><td>468.20 (-4.72%)</td><td>35.97 (-18.88%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:40</td><td>1.07 (n/a)</td><td>0.96 (n/a)</td><td>0.97 (n/a)</td><td>0.88 (n/a)</td><td>0.08 (n/a)</td><td>593.00 (n/a)</td><td>548.24 (n/a)</td><td>542.70 (n/a)</td><td>491.40 (n/a)</td><td>44.34 (n/a)</td>
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
