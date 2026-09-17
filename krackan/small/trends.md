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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (-6.87%)</td><td>0.07 (-19.35%)</td><td>0.06 <b>(-20.99%)</b></td><td>0.05 <b>(-31.36%)</b></td><td>0.01 <b>(+92.30%)</b></td><td>243.30 <b>(+45.69%)</b></td><td>193.12 <b>(+26.65%)</b></td><td>193.60 <b>(+26.62%)</b></td><td>148.30 (+7.31%)</td><td>34.71 <b>(+200.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>167.00 (n/a)</td><td>152.48 (n/a)</td><td>152.90 (n/a)</td><td>138.20 (n/a)</td><td>11.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 <b>(-29.75%)</b></td><td>0.07 (-18.60%)</td><td>0.08 (-8.84%)</td><td>0.05 (-18.00%)</td><td>0.01 <b>(-41.08%)</b></td><td>232.50 <b>(+21.92%)</b></td><td>179.86 <b>(+20.99%)</b></td><td>163.50 (+9.73%)</td><td>152.70 <b>(+42.31%)</b></td><td>33.25 (+2.76%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>148.66 (n/a)</td><td>149.00 (n/a)</td><td>107.30 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (-5.36%)</td><td>0.07 (-10.88%)</td><td>0.07 (-14.13%)</td><td>0.05 (-19.15%)</td><td>0.01 (+17.48%)</td><td>233.40 <b>(+23.69%)</b></td><td>185.98 (+13.22%)</td><td>185.90 (+16.48%)</td><td>150.80 (+5.68%)</td><td>30.49 <b>(+54.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>164.26 (n/a)</td><td>159.60 (n/a)</td><td>142.70 (n/a)</td><td>19.77 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (-18.09%)</td><td>0.06 (-4.11%)</td><td>0.06 (-14.07%)</td><td>0.06 <b>(+23.03%)</b></td><td>0.00 <b>(-71.59%)</b></td><td>218.40 (-18.69%)</td><td>193.50 (-1.42%)</td><td>193.30 (+16.38%)</td><td>176.40 <b>(+22.08%)</b></td><td>15.70 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>268.60 (n/a)</td><td>196.28 (n/a)</td><td>166.10 (n/a)</td><td>144.50 (n/a)</td><td>56.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-19.68%)</td><td>0.03 (-3.33%)</td><td>0.03 (+2.76%)</td><td>0.02 (-15.66%)</td><td>0.01 <b>(-28.66%)</b></td><td>226.70 (+18.57%)</td><td>166.52 (+2.34%)</td><td>160.00 (-2.74%)</td><td>130.80 <b>(+24.45%)</b></td><td>37.71 (+8.57%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>162.72 (n/a)</td><td>164.50 (n/a)</td><td>105.10 (n/a)</td><td>34.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-0.95%)</td><td>0.03 (+4.53%)</td><td>0.04 (+8.19%)</td><td>0.03 (+6.18%)</td><td>0.00 <b>(-25.90%)</b></td><td>188.20 (-5.81%)</td><td>158.54 (-5.30%)</td><td>149.10 (-7.56%)</td><td>141.30 (+0.93%)</td><td>19.55 <b>(-29.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>167.42 (n/a)</td><td>161.30 (n/a)</td><td>140.00 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (+8.40%)</td><td>0.03 (+10.00%)</td><td>0.04 <b>(+26.96%)</b></td><td>0.02 (-3.49%)</td><td>0.01 <b>(+37.15%)</b></td><td>212.50 (+3.61%)</td><td>156.42 (-7.51%)</td><td>134.40 <b>(-21.22%)</b></td><td>126.20 (-7.75%)</td><td>36.66 <b>(+31.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>169.12 (n/a)</td><td>170.60 (n/a)</td><td>136.80 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 <b>(-25.44%)</b></td><td>0.03 (+0.64%)</td><td>0.03 (+14.31%)</td><td>0.02 (+9.96%)</td><td>0.01 <b>(-56.99%)</b></td><td>210.50 (-9.07%)</td><td>168.86 (-6.87%)</td><td>172.10 (-12.51%)</td><td>136.30 <b>(+34.15%)</b></td><td>27.77 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>181.32 (n/a)</td><td>196.70 (n/a)</td><td>101.60 (n/a)</td><td>51.09 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 <b>(-32.68%)</b></td><td>0.03 <b>(-21.17%)</b></td><td>0.03 (-13.47%)</td><td>0.02 (-19.12%)</td><td>0.00 <b>(-56.23%)</b></td><td>226.00 <b>(+23.63%)</b></td><td>193.84 <b>(+24.03%)</b></td><td>193.10 (+15.56%)</td><td>159.00 <b>(+48.46%)</b></td><td>24.14 (-17.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>156.28 (n/a)</td><td>167.10 (n/a)</td><td>107.10 (n/a)</td><td>29.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 <b>(+25.11%)</b></td><td>0.03 (+10.79%)</td><td>0.03 (+5.43%)</td><td>0.03 (+7.94%)</td><td>0.01 <b>(+60.00%)</b></td><td>208.10 (-7.35%)</td><td>177.16 (-8.33%)</td><td>178.70 (-5.15%)</td><td>123.40 <b>(-20.08%)</b></td><td>33.59 (+14.33%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>193.26 (n/a)</td><td>188.40 (n/a)</td><td>154.40 (n/a)</td><td>29.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (+2.53%)</td><td>0.03 (+4.77%)</td><td>0.03 (-4.13%)</td><td>0.02 (+19.77%)</td><td>0.00 (-18.98%)</td><td>258.40 (-16.51%)</td><td>201.60 (-6.67%)</td><td>200.30 (+4.27%)</td><td>168.00 (-2.50%)</td><td>37.23 <b>(-35.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>309.50 (n/a)</td><td>216.00 (n/a)</td><td>192.10 (n/a)</td><td>172.30 (n/a)</td><td>57.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (-4.08%)</td><td>0.02 (-0.99%)</td><td>0.02 (-2.56%)</td><td>0.02 (+5.04%)</td><td>0.00 (-11.62%)</td><td>248.50 (-4.79%)</td><td>225.28 (+0.66%)</td><td>239.00 (+2.62%)</td><td>184.30 (+4.24%)</td><td>28.53 (-9.46%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>261.00 (n/a)</td><td>223.80 (n/a)</td><td>232.90 (n/a)</td><td>176.80 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>159.92 (n/a)</td><td>151.20 (n/a)</td><td>142.00 (n/a)</td><td>20.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>211.90 (n/a)</td><td>176.12 (n/a)</td><td>178.80 (n/a)</td><td>144.80 (n/a)</td><td>27.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>169.60 (n/a)</td><td>158.32 (n/a)</td><td>158.40 (n/a)</td><td>149.20 (n/a)</td><td>7.64 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>165.90 (n/a)</td><td>159.50 (n/a)</td><td>148.30 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>170.90 (n/a)</td><td>149.76 (n/a)</td><td>161.80 (n/a)</td><td>110.80 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>163.14 (n/a)</td><td>156.40 (n/a)</td><td>147.60 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>206.90 (n/a)</td><td>162.70 (n/a)</td><td>175.90 (n/a)</td><td>123.60 (n/a)</td><td>34.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>280.10 (n/a)</td><td>190.64 (n/a)</td><td>183.70 (n/a)</td><td>123.70 (n/a)</td><td>56.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.15 (-1.72%)</td><td>2.98 (-2.21%)</td><td>2.99 (-2.42%)</td><td>2.79 (-3.86%)</td><td>0.14 (+7.08%)</td><td>493.50 (+4.00%)</td><td>463.18 (+2.29%)</td><td>460.60 (+2.49%)</td><td>437.40 (+1.77%)</td><td>21.49 (+12.82%)</td><td>613.77 (-1.72%)</td><td>580.53 (-2.21%)</td><td>582.83 (-2.42%)</td><td>543.92 (-3.86%)</td><td>26.72 (+7.08%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.20 (n/a)</td><td>3.04 (n/a)</td><td>3.06 (n/a)</td><td>2.90 (n/a)</td><td>0.13 (n/a)</td><td>474.50 (n/a)</td><td>452.80 (n/a)</td><td>449.40 (n/a)</td><td>429.80 (n/a)</td><td>19.05 (n/a)</td><td>624.52 (n/a)</td><td>593.67 (n/a)</td><td>597.30 (n/a)</td><td>565.74 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.89 <b>(+21.31%)</b></td><td>4.09 (+12.03%)</td><td>3.87 (+6.30%)</td><td>3.33 (+0.17%)</td><td>0.68 <b>(+168.69%)</b></td><td>413.30 (-0.17%)</td><td>344.42 (-9.09%)</td><td>356.00 (-5.92%)</td><td>281.50 (-17.57%)</td><td>56.50 <b>(+117.57%)</b></td><td>953.48 <b>(+21.31%)</b></td><td>796.78 (+12.03%)</td><td>754.11 (+6.30%)</td><td>649.47 (+0.17%)</td><td>133.06 <b>(+168.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.03 (n/a)</td><td>3.65 (n/a)</td><td>3.64 (n/a)</td><td>3.32 (n/a)</td><td>0.25 (n/a)</td><td>414.00 (n/a)</td><td>378.86 (n/a)</td><td>378.40 (n/a)</td><td>341.50 (n/a)</td><td>25.97 (n/a)</td><td>786.00 (n/a)</td><td>711.21 (n/a)</td><td>709.40 (n/a)</td><td>648.40 (n/a)</td><td>49.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>6.00 (-4.04%)</td><td>4.60 (-2.41%)</td><td>3.70 (-8.16%)</td><td>3.64 (+4.70%)</td><td>1.27 (-4.67%)</td><td>377.90 (-4.47%)</td><td>317.10 (+2.07%)</td><td>371.70 (+8.88%)</td><td>229.50 (+4.22%)</td><td>79.68 (-2.39%)</td><td>1169.58 (-4.04%)</td><td>896.34 (-2.41%)</td><td>722.14 (-8.16%)</td><td>710.42 (+4.70%)</td><td>247.83 (-4.67%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.25 (n/a)</td><td>4.71 (n/a)</td><td>4.03 (n/a)</td><td>3.48 (n/a)</td><td>1.33 (n/a)</td><td>395.60 (n/a)</td><td>310.68 (n/a)</td><td>341.40 (n/a)</td><td>220.20 (n/a)</td><td>81.63 (n/a)</td><td>1218.84 (n/a)</td><td>918.43 (n/a)</td><td>786.30 (n/a)</td><td>678.50 (n/a)</td><td>259.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>7.33 <b>(+48.61%)</b></td><td>4.49 (+14.91%)</td><td>3.86 (+4.25%)</td><td>3.14 (-6.61%)</td><td>1.66 <b>(+165.23%)</b></td><td>437.70 (+7.07%)</td><td>333.50 (-7.04%)</td><td>356.80 (-4.09%)</td><td>187.80 <b>(-32.69%)</b></td><td>93.85 <b>(+83.34%)</b></td><td>1429.63 <b>(+48.61%)</b></td><td>875.76 (+14.91%)</td><td>752.25 (+4.25%)</td><td>613.28 (-6.61%)</td><td>323.28 <b>(+165.23%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.93 (n/a)</td><td>3.91 (n/a)</td><td>3.70 (n/a)</td><td>3.37 (n/a)</td><td>0.62 (n/a)</td><td>408.80 (n/a)</td><td>358.74 (n/a)</td><td>372.00 (n/a)</td><td>279.00 (n/a)</td><td>51.19 (n/a)</td><td>962.03 (n/a)</td><td>762.12 (n/a)</td><td>721.59 (n/a)</td><td>656.66 (n/a)</td><td>121.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.43 (+6.18%)</td><td>3.52 (+9.85%)</td><td>3.44 (+16.94%)</td><td>2.94 (+2.14%)</td><td>0.55 (+0.12%)</td><td>468.10 (-2.09%)</td><td>398.02 (-9.14%)</td><td>399.60 (-14.49%)</td><td>310.70 (-5.82%)</td><td>56.69 (-9.24%)</td><td>863.98 (+6.18%)</td><td>686.55 (+9.85%)</td><td>671.73 (+16.94%)</td><td>573.47 (+2.14%)</td><td>107.50 (+0.12%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.17 (n/a)</td><td>3.20 (n/a)</td><td>2.95 (n/a)</td><td>2.88 (n/a)</td><td>0.55 (n/a)</td><td>478.10 (n/a)</td><td>438.04 (n/a)</td><td>467.30 (n/a)</td><td>329.90 (n/a)</td><td>62.46 (n/a)</td><td>813.67 (n/a)</td><td>625.01 (n/a)</td><td>574.43 (n/a)</td><td>561.45 (n/a)</td><td>107.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.13 (+4.97%)</td><td>1.06 (+3.49%)</td><td>1.06 (+4.69%)</td><td>1.01 (+2.02%)</td><td>0.05 <b>(+26.37%)</b></td><td>399.10 (-1.97%)</td><td>377.86 (-3.33%)</td><td>378.30 (-4.49%)</td><td>355.50 (-4.72%)</td><td>16.38 (+18.18%)</td><td>94.40 (+4.97%)</td><td>88.94 (+3.49%)</td><td>88.70 (+4.69%)</td><td>84.08 (+2.02%)</td><td>3.88 <b>(+26.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.08 (n/a)</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>0.99 (n/a)</td><td>0.04 (n/a)</td><td>407.10 (n/a)</td><td>390.86 (n/a)</td><td>396.10 (n/a)</td><td>373.10 (n/a)</td><td>13.86 (n/a)</td><td>89.93 (n/a)</td><td>85.94 (n/a)</td><td>84.72 (n/a)</td><td>82.41 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>7.41 (+19.45%)</td><td>6.08 (+18.66%)</td><td>6.73 <b>(+42.13%)</b></td><td>4.38 (-4.83%)</td><td>1.33 <b>(+93.17%)</b></td><td>441.30 (+5.10%)</td><td>331.70 (-13.22%)</td><td>287.40 <b>(-29.66%)</b></td><td>261.10 (-16.26%)</td><td>79.50 <b>(+68.69%)</b></td><td>1542.35 (+19.45%)</td><td>1266.81 (+18.66%)</td><td>1400.81 <b>(+42.13%)</b></td><td>912.48 (-4.83%)</td><td>277.26 <b>(+93.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.20 (n/a)</td><td>5.13 (n/a)</td><td>4.73 (n/a)</td><td>4.60 (n/a)</td><td>0.69 (n/a)</td><td>419.90 (n/a)</td><td>382.22 (n/a)</td><td>408.60 (n/a)</td><td>311.80 (n/a)</td><td>47.12 (n/a)</td><td>1291.20 (n/a)</td><td>1067.55 (n/a)</td><td>985.55 (n/a)</td><td>958.81 (n/a)</td><td>143.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>16.67 (-4.56%)</td><td>12.25 (-2.35%)</td><td>11.31 (-0.52%)</td><td>10.62 (-2.08%)</td><td>2.49 (-10.61%)</td><td>518.30 (+2.13%)</td><td>461.64 (+1.92%)</td><td>486.80 (+0.52%)</td><td>330.20 (+4.76%)</td><td>74.76 (-5.55%)</td><td>6502.70 (-4.56%)</td><td>4777.47 (-2.35%)</td><td>4411.15 (-0.52%)</td><td>4143.64 (-2.08%)</td><td>971.57 (-10.61%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>17.47 (n/a)</td><td>12.54 (n/a)</td><td>11.37 (n/a)</td><td>10.85 (n/a)</td><td>2.79 (n/a)</td><td>507.50 (n/a)</td><td>452.94 (n/a)</td><td>484.30 (n/a)</td><td>315.20 (n/a)</td><td>79.16 (n/a)</td><td>6813.10 (n/a)</td><td>4892.63 (n/a)</td><td>4434.28 (n/a)</td><td>4231.45 (n/a)</td><td>1086.94 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.50 (n/a)</td><td>176.02 (n/a)</td><td>153.70 (n/a)</td><td>149.10 (n/a)</td><td>39.39 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.60 (n/a)</td><td>165.88 (n/a)</td><td>177.30 (n/a)</td><td>121.80 (n/a)</td><td>29.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.80 (n/a)</td><td>194.58 (n/a)</td><td>187.70 (n/a)</td><td>155.50 (n/a)</td><td>30.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>169.04 (n/a)</td><td>176.50 (n/a)</td><td>122.00 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>164.60 (n/a)</td><td>164.90 (n/a)</td><td>124.10 (n/a)</td><td>28.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>169.30 (n/a)</td><td>160.90 (n/a)</td><td>132.60 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>179.28 (n/a)</td><td>184.50 (n/a)</td><td>142.80 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>213.60 (n/a)</td><td>185.48 (n/a)</td><td>175.90 (n/a)</td><td>171.80 (n/a)</td><td>18.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.88 (+0.16%)</td><td>4.27 (-1.68%)</td><td>4.18 (+0.25%)</td><td>3.59 (-11.75%)</td><td>0.49 <b>(+46.52%)</b></td><td>2618.60 (+13.32%)</td><td>2228.72 (+2.35%)</td><td>2247.60 (-0.24%)</td><td>1926.80 (-0.16%)</td><td>261.43 <b>(+66.49%)</b></td><td>1919.91 (+0.16%)</td><td>1677.71 (-1.68%)</td><td>1645.91 (+0.25%)</td><td>1412.75 (-11.75%)</td><td>191.19 <b>(+46.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.87 (n/a)</td><td>4.34 (n/a)</td><td>4.17 (n/a)</td><td>4.07 (n/a)</td><td>0.33 (n/a)</td><td>2310.90 (n/a)</td><td>2177.64 (n/a)</td><td>2253.10 (n/a)</td><td>1929.90 (n/a)</td><td>157.03 (n/a)</td><td>1916.84 (n/a)</td><td>1706.30 (n/a)</td><td>1641.88 (n/a)</td><td>1600.81 (n/a)</td><td>130.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.10 (-15.16%)</td><td>1.00 (+15.09%)</td><td>1.00 <b>(+23.98%)</b></td><td>0.91 <b>(+51.50%)</b></td><td>0.08 <b>(-74.18%)</b></td><td>244.00 <b>(-34.00%)</b></td><td>222.08 (-19.75%)</td><td>221.00 (-19.34%)</td><td>201.20 (+17.87%)</td><td>16.66 <b>(-80.42%)</b></td><td>46.91 (-15.16%)</td><td>42.69 (+15.09%)</td><td>42.71 <b>(+23.98%)</b></td><td>38.68 <b>(+51.50%)</b></td><td>3.20 <b>(-74.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.30 (n/a)</td><td>0.87 (n/a)</td><td>0.81 (n/a)</td><td>0.60 (n/a)</td><td>0.29 (n/a)</td><td>369.70 (n/a)</td><td>276.72 (n/a)</td><td>274.00 (n/a)</td><td>170.70 (n/a)</td><td>85.06 (n/a)</td><td>55.29 (n/a)</td><td>37.09 (n/a)</td><td>34.45 (n/a)</td><td>25.53 (n/a)</td><td>12.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.22 <b>(+27.54%)</b></td><td>0.92 (+12.53%)</td><td>0.94 (+12.06%)</td><td>0.66 (-2.19%)</td><td>0.21 <b>(+56.84%)</b></td><td>336.50 (+2.22%)</td><td>251.54 (-9.32%)</td><td>235.50 (-10.76%)</td><td>181.10 <b>(-21.60%)</b></td><td>58.58 <b>(+24.59%)</b></td><td>52.10 <b>(+27.54%)</b></td><td>39.16 (+12.53%)</td><td>40.07 (+12.06%)</td><td>28.04 (-2.19%)</td><td>9.01 <b>(+56.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.96 (n/a)</td><td>0.82 (n/a)</td><td>0.84 (n/a)</td><td>0.67 (n/a)</td><td>0.13 (n/a)</td><td>329.20 (n/a)</td><td>277.40 (n/a)</td><td>263.90 (n/a)</td><td>231.00 (n/a)</td><td>47.02 (n/a)</td><td>40.85 (n/a)</td><td>34.80 (n/a)</td><td>35.76 (n/a)</td><td>28.67 (n/a)</td><td>5.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.53 (+0.37%)</td><td>0.53 (+0.26%)</td><td>0.53 (+0.29%)</td><td>0.53 (+0.13%)</td><td>0.00 <b>(+71.36%)</b></td><td>47848.40 (-0.13%)</td><td>47748.80 (-0.26%)</td><td>47755.60 (-0.29%)</td><td>47613.00 (-0.37%)</td><td>85.83 <b>(+70.50%)</b></td><td>360.82 (+0.37%)</td><td>359.80 (+0.26%)</td><td>359.75 (+0.29%)</td><td>359.05 (+0.13%)</td><td>0.65 <b>(+71.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47909.30 (n/a)</td><td>47871.32 (n/a)</td><td>47895.00 (n/a)</td><td>47789.10 (n/a)</td><td>50.34 (n/a)</td><td>359.49 (n/a)</td><td>358.88 (n/a)</td><td>358.70 (n/a)</td><td>358.59 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.90 (-1.64%)</td><td>0.90 (-0.74%)</td><td>0.90 (-0.14%)</td><td>0.89 (-0.82%)</td><td>0.01 <b>(-34.62%)</b></td><td>28228.20 (+0.82%)</td><td>27974.92 (+0.74%)</td><td>27893.70 (+0.14%)</td><td>27832.60 (+1.66%)</td><td>158.31 <b>(-32.83%)</b></td><td>617.26 (-1.64%)</td><td>614.13 (-0.74%)</td><td>615.90 (-0.14%)</td><td>608.61 (-0.82%)</td><td>3.46 <b>(-34.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>27997.70 (n/a)</td><td>27769.46 (n/a)</td><td>27855.30 (n/a)</td><td>27377.40 (n/a)</td><td>235.68 (n/a)</td><td>627.52 (n/a)</td><td>618.70 (n/a)</td><td>616.75 (n/a)</td><td>613.62 (n/a)</td><td>5.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.32 (+1.71%)</td><td>3.17 (+0.00%)</td><td>3.15 (+0.08%)</td><td>3.07 (-1.93%)</td><td>0.10 <b>(+67.81%)</b></td><td>8206.40 (+1.97%)</td><td>7954.76 (+0.05%)</td><td>7981.40 (-0.08%)</td><td>7572.60 (-1.68%)</td><td>239.31 <b>(+67.85%)</b></td><td>2268.69 (+1.71%)</td><td>2161.29 (+0.00%)</td><td>2152.48 (+0.08%)</td><td>2093.46 (-1.93%)</td><td>66.45 <b>(+67.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.27 (n/a)</td><td>3.17 (n/a)</td><td>3.15 (n/a)</td><td>3.13 (n/a)</td><td>0.06 (n/a)</td><td>8047.70 (n/a)</td><td>7951.02 (n/a)</td><td>7987.70 (n/a)</td><td>7701.80 (n/a)</td><td>142.57 (n/a)</td><td>2230.62 (n/a)</td><td>2161.29 (n/a)</td><td>2150.80 (n/a)</td><td>2134.76 (n/a)</td><td>39.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.32 (-1.00%)</td><td>3.84 (-2.93%)</td><td>4.07 (+3.67%)</td><td>3.03 (-14.78%)</td><td>0.57 <b>(+54.02%)</b></td><td>2658.20 (+17.34%)</td><td>2139.66 (+4.28%)</td><td>1979.90 (-3.54%)</td><td>1867.50 (+1.01%)</td><td>343.45 <b>(+80.63%)</b></td><td>1131.96 (-1.00%)</td><td>1006.96 (-2.93%)</td><td>1067.71 (+3.67%)</td><td>795.26 (-14.78%)</td><td>148.36 <b>(+54.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.36 (n/a)</td><td>3.96 (n/a)</td><td>3.93 (n/a)</td><td>3.56 (n/a)</td><td>0.37 (n/a)</td><td>2265.30 (n/a)</td><td>2051.86 (n/a)</td><td>2052.50 (n/a)</td><td>1848.80 (n/a)</td><td>190.14 (n/a)</td><td>1143.43 (n/a)</td><td>1037.38 (n/a)</td><td>1029.92 (n/a)</td><td>933.16 (n/a)</td><td>96.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.37 <b>(-37.58%)</b></td><td>0.32 <b>(-20.48%)</b></td><td>0.33 (-7.95%)</td><td>0.27 (-9.29%)</td><td>0.03 <b>(-72.45%)</b></td><td>4532.00 (+10.24%)</td><td>3878.12 (+19.17%)</td><td>3752.20 (+8.64%)</td><td>3408.40 <b>(+60.19%)</b></td><td>414.54 <b>(-51.26%)</b></td><td>19.69 <b>(-37.58%)</b></td><td>17.46 <b>(-20.48%)</b></td><td>17.89 (-7.95%)</td><td>14.81 (-9.29%)</td><td>1.78 <b>(-72.45%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.12 (n/a)</td><td>4111.00 (n/a)</td><td>3254.26 (n/a)</td><td>3453.90 (n/a)</td><td>2127.70 (n/a)</td><td>850.55 (n/a)</td><td>31.54 (n/a)</td><td>21.95 (n/a)</td><td>19.43 (n/a)</td><td>16.32 (n/a)</td><td>6.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.27 <b>(-34.01%)</b></td><td>3.71 <b>(-22.55%)</b></td><td>3.67 <b>(-22.10%)</b></td><td>3.36 (+1.67%)</td><td>0.37 <b>(-67.35%)</b></td><td>1981.70 (-1.64%)</td><td>1807.66 <b>(+24.31%)</b></td><td>1811.00 <b>(+28.38%)</b></td><td>1557.20 <b>(+51.55%)</b></td><td>170.94 <b>(-51.78%)</b></td><td>1319.84 <b>(-34.01%)</b></td><td>1145.50 <b>(-22.55%)</b></td><td>1134.82 <b>(-22.10%)</b></td><td>1037.07 (+1.67%)</td><td>113.55 <b>(-67.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.47 (n/a)</td><td>4.79 (n/a)</td><td>4.72 (n/a)</td><td>3.30 (n/a)</td><td>1.13 (n/a)</td><td>2014.80 (n/a)</td><td>1454.10 (n/a)</td><td>1410.70 (n/a)</td><td>1027.50 (n/a)</td><td>354.51 (n/a)</td><td>2000.14 (n/a)</td><td>1479.01 (n/a)</td><td>1456.83 (n/a)</td><td>1020.08 (n/a)</td><td>347.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>13.47 (n/a)</td><td>12.99 (n/a)</td><td>13.40 (n/a)</td><td>12.18 (n/a)</td><td>0.62 (n/a)</td><td>13.46 (n/a)</td><td>12.98 (n/a)</td><td>13.39 (n/a)</td><td>12.18 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>24.89 (-0.74%)</td><td>24.22 (-1.34%)</td><td>24.64 (-0.71%)</td><td>22.47 (-4.12%)</td><td>1.01 <b>(+53.28%)</b></td><td>24.87 (-0.74%)</td><td>24.21 (-1.34%)</td><td>24.63 (-0.71%)</td><td>22.45 (-4.12%)</td><td>1.01 <b>(+53.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>25.07 (n/a)</td><td>24.55 (n/a)</td><td>24.82 (n/a)</td><td>23.43 (n/a)</td><td>0.66 (n/a)</td><td>25.06 (n/a)</td><td>24.54 (n/a)</td><td>24.80 (n/a)</td><td>23.42 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>41.62 (+3.57%)</td><td>40.48 (+3.73%)</td><td>39.99 (+1.85%)</td><td>39.52 (+4.28%)</td><td>0.97 (+10.07%)</td><td>41.60 (+3.57%)</td><td>40.46 (+3.73%)</td><td>39.96 (+1.85%)</td><td>39.50 (+4.28%)</td><td>0.97 (+10.07%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>40.19 (n/a)</td><td>39.03 (n/a)</td><td>39.26 (n/a)</td><td>37.90 (n/a)</td><td>0.88 (n/a)</td><td>40.16 (n/a)</td><td>39.01 (n/a)</td><td>39.24 (n/a)</td><td>37.87 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>44.08 (-5.06%)</td><td>41.80 (-4.45%)</td><td>41.75 (-4.38%)</td><td>39.74 (-2.79%)</td><td>1.66 <b>(-21.13%)</b></td><td>44.05 (-5.06%)</td><td>41.77 (-4.45%)</td><td>41.73 (-4.38%)</td><td>39.72 (-2.79%)</td><td>1.66 <b>(-21.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>46.43 (n/a)</td><td>43.74 (n/a)</td><td>43.67 (n/a)</td><td>40.89 (n/a)</td><td>2.10 (n/a)</td><td>46.40 (n/a)</td><td>43.72 (n/a)</td><td>43.64 (n/a)</td><td>40.86 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>13.34 (n/a)</td><td>12.53 (n/a)</td><td>12.15 (n/a)</td><td>11.92 (n/a)</td><td>0.69 (n/a)</td><td>13.33 (n/a)</td><td>12.53 (n/a)</td><td>12.14 (n/a)</td><td>11.91 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>24.42 (-4.34%)</td><td>23.50 (+2.70%)</td><td>23.04 (-2.56%)</td><td>22.78 (+17.18%)</td><td>0.80 <b>(-65.31%)</b></td><td>24.41 (-4.34%)</td><td>23.49 (+2.70%)</td><td>23.02 (-2.56%)</td><td>22.77 (+17.18%)</td><td>0.80 <b>(-65.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>25.53 (n/a)</td><td>22.88 (n/a)</td><td>23.64 (n/a)</td><td>19.44 (n/a)</td><td>2.30 (n/a)</td><td>25.51 (n/a)</td><td>22.87 (n/a)</td><td>23.63 (n/a)</td><td>19.43 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>41.66 (+2.67%)</td><td>39.19 (+0.07%)</td><td>38.92 (-1.32%)</td><td>36.15 (-0.74%)</td><td>2.16 <b>(+31.30%)</b></td><td>41.64 (+2.67%)</td><td>39.16 (+0.07%)</td><td>38.90 (-1.32%)</td><td>36.13 (-0.74%)</td><td>2.16 <b>(+31.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>40.58 (n/a)</td><td>39.16 (n/a)</td><td>39.44 (n/a)</td><td>36.42 (n/a)</td><td>1.65 (n/a)</td><td>40.56 (n/a)</td><td>39.13 (n/a)</td><td>39.42 (n/a)</td><td>36.40 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>46.26 (-0.81%)</td><td>41.78 (-2.09%)</td><td>42.15 (+0.18%)</td><td>38.92 (-0.18%)</td><td>2.99 (+1.31%)</td><td>46.23 (-0.81%)</td><td>41.76 (-2.09%)</td><td>42.12 (+0.18%)</td><td>38.90 (-0.18%)</td><td>2.99 (+1.31%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>46.64 (n/a)</td><td>42.67 (n/a)</td><td>42.07 (n/a)</td><td>38.99 (n/a)</td><td>2.95 (n/a)</td><td>46.61 (n/a)</td><td>42.65 (n/a)</td><td>42.05 (n/a)</td><td>38.97 (n/a)</td><td>2.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>9.90 (+6.83%)</td><td>9.15 (+6.12%)</td><td>9.02 (+4.68%)</td><td>8.72 (+6.16%)</td><td>0.45 (+13.42%)</td><td>9.88 (+6.83%)</td><td>9.13 (+6.12%)</td><td>9.00 (+4.68%)</td><td>8.70 (+6.16%)</td><td>0.45 (+13.42%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>9.26 (n/a)</td><td>8.62 (n/a)</td><td>8.62 (n/a)</td><td>8.21 (n/a)</td><td>0.40 (n/a)</td><td>9.25 (n/a)</td><td>8.61 (n/a)</td><td>8.60 (n/a)</td><td>8.20 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.96 (-8.92%)</td><td>0.92 (+6.97%)</td><td>0.91 (+15.38%)</td><td>0.89 <b>(+27.81%)</b></td><td>0.03 <b>(-81.88%)</b></td><td>0.94 (-8.92%)</td><td>0.90 (+6.97%)</td><td>0.89 (+15.38%)</td><td>0.88 <b>(+27.81%)</b></td><td>0.03 <b>(-81.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.05 (n/a)</td><td>0.86 (n/a)</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.15 (n/a)</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.36 (+14.76%)</td><td>1.25 (+15.44%)</td><td>1.28 (+14.12%)</td><td>1.08 (+16.54%)</td><td>0.12 (+16.82%)</td><td>1.35 (+14.76%)</td><td>1.24 (+15.44%)</td><td>1.26 (+14.12%)</td><td>1.07 (+16.54%)</td><td>0.12 (+16.82%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.19 (n/a)</td><td>1.08 (n/a)</td><td>1.12 (n/a)</td><td>0.93 (n/a)</td><td>0.10 (n/a)</td><td>1.18 (n/a)</td><td>1.07 (n/a)</td><td>1.11 (n/a)</td><td>0.92 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>18.53 (+8.92%)</td><td>17.18 (+7.40%)</td><td>17.23 (+6.78%)</td><td>15.81 (+10.03%)</td><td>1.05 (+7.14%)</td><td>18.31 (+8.92%)</td><td>16.98 (+7.40%)</td><td>17.03 (+6.78%)</td><td>15.62 (+10.03%)</td><td>1.04 (+7.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>17.01 (n/a)</td><td>15.99 (n/a)</td><td>16.14 (n/a)</td><td>14.37 (n/a)</td><td>0.98 (n/a)</td><td>16.81 (n/a)</td><td>15.81 (n/a)</td><td>15.95 (n/a)</td><td>14.20 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>14.14 (+0.63%)</td><td>12.64 (-5.44%)</td><td>13.77 (+4.30%)</td><td>8.27 <b>(-37.11%)</b></td><td>2.47 <b>(+548.08%)</b></td><td>13.89 (+0.63%)</td><td>12.42 (-5.44%)</td><td>13.52 (+4.30%)</td><td>8.13 <b>(-37.11%)</b></td><td>2.42 <b>(+548.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>14.05 (n/a)</td><td>13.37 (n/a)</td><td>13.20 (n/a)</td><td>13.16 (n/a)</td><td>0.38 (n/a)</td><td>13.80 (n/a)</td><td>13.14 (n/a)</td><td>12.97 (n/a)</td><td>12.93 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>10.25 <b>(+30.28%)</b></td><td>8.74 (+16.55%)</td><td>8.79 (+15.08%)</td><td>7.62 (+11.06%)</td><td>1.06 <b>(+170.96%)</b></td><td>10.07 <b>(+30.28%)</b></td><td>8.58 (+16.55%)</td><td>8.64 (+15.08%)</td><td>7.49 (+11.06%)</td><td>1.04 <b>(+170.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>7.87 (n/a)</td><td>7.50 (n/a)</td><td>7.64 (n/a)</td><td>6.86 (n/a)</td><td>0.39 (n/a)</td><td>7.73 (n/a)</td><td>7.37 (n/a)</td><td>7.51 (n/a)</td><td>6.74 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>6.35 (+4.57%)</td><td>5.43 (+0.09%)</td><td>5.49 (+0.25%)</td><td>4.51 (-2.66%)</td><td>0.68 (+12.99%)</td><td>6.24 (+4.57%)</td><td>5.35 (+0.09%)</td><td>5.40 (+0.25%)</td><td>4.44 (-2.66%)</td><td>0.67 (+12.99%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>6.07 (n/a)</td><td>5.43 (n/a)</td><td>5.47 (n/a)</td><td>4.63 (n/a)</td><td>0.61 (n/a)</td><td>5.97 (n/a)</td><td>5.34 (n/a)</td><td>5.38 (n/a)</td><td>4.56 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.01 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>13.39 (n/a)</td><td>12.67 (n/a)</td><td>13.23 (n/a)</td><td>11.20 (n/a)</td><td>0.98 (n/a)</td><td>13.38 (n/a)</td><td>12.66 (n/a)</td><td>13.23 (n/a)</td><td>11.19 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>13.40 (n/a)</td><td>12.90 (n/a)</td><td>12.98 (n/a)</td><td>12.25 (n/a)</td><td>0.53 (n/a)</td><td>13.39 (n/a)</td><td>12.89 (n/a)</td><td>12.97 (n/a)</td><td>12.24 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>157.20 (n/a)</td><td>146.90 (n/a)</td><td>126.90 (n/a)</td><td>38.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.40 (n/a)</td><td>171.52 (n/a)</td><td>160.40 (n/a)</td><td>139.80 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>175.46 (n/a)</td><td>173.60 (n/a)</td><td>139.70 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.20 (n/a)</td><td>181.22 (n/a)</td><td>174.70 (n/a)</td><td>140.40 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>168.58 (n/a)</td><td>165.40 (n/a)</td><td>147.70 (n/a)</td><td>18.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>182.98 (n/a)</td><td>176.20 (n/a)</td><td>145.40 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.20 (n/a)</td><td>194.56 (n/a)</td><td>177.30 (n/a)</td><td>151.90 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>287.00 (n/a)</td><td>240.16 (n/a)</td><td>241.70 (n/a)</td><td>195.20 (n/a)</td><td>42.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (-3.59%)</td><td>0.05 (-6.03%)</td><td>0.05 (-8.15%)</td><td>0.03 (-16.22%)</td><td>0.02 (+8.90%)</td><td>237.40 (+19.36%)</td><td>169.80 (+8.58%)</td><td>179.10 (+8.88%)</td><td>112.30 (+3.69%)</td><td>48.30 <b>(+34.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>156.38 (n/a)</td><td>164.50 (n/a)</td><td>108.30 (n/a)</td><td>36.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 <b>(-25.22%)</b></td><td>0.05 (-19.97%)</td><td>0.05 <b>(-30.81%)</b></td><td>0.04 (+2.23%)</td><td>0.00 <b>(-73.20%)</b></td><td>189.80 (-2.16%)</td><td>176.40 (+19.71%)</td><td>179.80 <b>(+44.53%)</b></td><td>157.50 <b>(+33.70%)</b></td><td>13.17 <b>(-64.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.00 (n/a)</td><td>147.36 (n/a)</td><td>124.40 (n/a)</td><td>117.80 (n/a)</td><td>37.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 <b>(-33.44%)</b></td><td>0.04 (-5.11%)</td><td>0.04 (+10.56%)</td><td>0.04 (+10.33%)</td><td>0.00 <b>(-78.16%)</b></td><td>216.30 (-9.38%)</td><td>196.80 (-0.98%)</td><td>193.40 (-9.54%)</td><td>177.40 <b>(+50.21%)</b></td><td>14.97 <b>(-69.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>198.74 (n/a)</td><td>213.80 (n/a)</td><td>118.10 (n/a)</td><td>49.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (-2.74%)</td><td>0.04 (-13.30%)</td><td>0.05 (-7.79%)</td><td>0.02 <b>(-43.68%)</b></td><td>0.02 <b>(+52.16%)</b></td><td>385.40 <b>(+77.52%)</b></td><td>214.38 <b>(+29.30%)</b></td><td>180.30 (+8.42%)</td><td>121.60 (+2.88%)</td><td>103.20 <b>(+193.10%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>165.80 (n/a)</td><td>166.30 (n/a)</td><td>118.20 (n/a)</td><td>35.21 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (-15.06%)</td><td>0.04 (-9.42%)</td><td>0.04 (-10.97%)</td><td>0.03 (-17.56%)</td><td>0.01 (-13.96%)</td><td>244.50 <b>(+21.28%)</b></td><td>190.32 (+10.59%)</td><td>191.60 (+12.31%)</td><td>150.50 (+17.67%)</td><td>35.75 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.60 (n/a)</td><td>172.10 (n/a)</td><td>170.60 (n/a)</td><td>127.90 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 <b>(-22.44%)</b></td><td>0.04 <b>(-22.08%)</b></td><td>0.04 <b>(-22.29%)</b></td><td>0.03 <b>(-31.59%)</b></td><td>0.01 (-19.61%)</td><td>294.80 <b>(+46.16%)</b></td><td>213.28 <b>(+29.15%)</b></td><td>202.00 <b>(+28.66%)</b></td><td>168.80 <b>(+28.85%)</b></td><td>47.88 <b>(+55.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>201.70 (n/a)</td><td>165.14 (n/a)</td><td>157.00 (n/a)</td><td>131.00 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-5.99%)</td><td>0.05 (-11.48%)</td><td>0.05 (-10.99%)</td><td>0.03 <b>(-20.03%)</b></td><td>0.01 (+18.35%)</td><td>247.00 <b>(+25.00%)</b></td><td>182.70 (+15.27%)</td><td>171.40 (+12.32%)</td><td>132.00 (+6.37%)</td><td>43.66 <b>(+58.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>158.50 (n/a)</td><td>152.60 (n/a)</td><td>124.10 (n/a)</td><td>27.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (-2.62%)</td><td>0.04 (-1.02%)</td><td>0.04 (+2.89%)</td><td>0.03 <b>(-21.52%)</b></td><td>0.01 <b>(+27.82%)</b></td><td>280.10 <b>(+27.38%)</b></td><td>203.44 (+2.97%)</td><td>192.50 (-2.78%)</td><td>159.50 (+2.70%)</td><td>45.80 <b>(+73.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.90 (n/a)</td><td>197.58 (n/a)</td><td>198.00 (n/a)</td><td>155.30 (n/a)</td><td>26.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 <b>(-21.37%)</b></td><td>0.05 (-10.13%)</td><td>0.05 (+3.77%)</td><td>0.04 (-5.67%)</td><td>0.01 <b>(-51.04%)</b></td><td>205.30 (+5.99%)</td><td>181.32 (+8.74%)</td><td>178.10 (-3.63%)</td><td>159.70 <b>(+27.15%)</b></td><td>21.18 <b>(-34.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>166.74 (n/a)</td><td>184.80 (n/a)</td><td>125.60 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (+8.60%)</td><td>0.04 (-2.36%)</td><td>0.04 (-8.50%)</td><td>0.03 (-0.43%)</td><td>0.01 <b>(+45.34%)</b></td><td>241.80 (+0.42%)</td><td>215.06 (+3.43%)</td><td>231.70 (+9.29%)</td><td>162.90 (-7.91%)</td><td>31.94 <b>(+33.08%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.80 (n/a)</td><td>207.92 (n/a)</td><td>212.00 (n/a)</td><td>176.90 (n/a)</td><td>24.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-1.81%)</td><td>0.05 (+1.77%)</td><td>0.05 (-12.34%)</td><td>0.04 <b>(+80.96%)</b></td><td>0.01 <b>(-50.50%)</b></td><td>190.70 <b>(-44.74%)</b></td><td>165.04 (-11.90%)</td><td>162.30 (+14.05%)</td><td>132.90 (+1.84%)</td><td>24.80 <b>(-72.49%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>345.10 (n/a)</td><td>187.34 (n/a)</td><td>142.30 (n/a)</td><td>130.50 (n/a)</td><td>90.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-15.03%)</td><td>0.04 (+1.29%)</td><td>0.04 (+0.50%)</td><td>0.04 <b>(+39.34%)</b></td><td>0.00 <b>(-77.70%)</b></td><td>230.40 <b>(-28.22%)</b></td><td>214.80 (-6.14%)</td><td>215.70 (-0.51%)</td><td>202.10 (+17.71%)</td><td>11.63 <b>(-81.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.00 (n/a)</td><td>228.84 (n/a)</td><td>216.80 (n/a)</td><td>171.70 (n/a)</td><td>61.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-14.49%)</td><td>0.05 (-3.73%)</td><td>0.06 (+12.08%)</td><td>0.05 (-3.04%)</td><td>0.01 <b>(-35.82%)</b></td><td>176.10 (+3.10%)</td><td>152.86 (+2.56%)</td><td>145.70 (-10.78%)</td><td>132.10 (+17.01%)</td><td>19.53 <b>(-22.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>149.04 (n/a)</td><td>163.30 (n/a)</td><td>112.90 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (+7.82%)</td><td>0.05 (+8.61%)</td><td>0.05 (+2.65%)</td><td>0.05 (+12.79%)</td><td>0.00 (+3.05%)</td><td>167.30 (-11.34%)</td><td>155.38 (-8.00%)</td><td>163.60 (-2.56%)</td><td>139.10 (-7.27%)</td><td>14.12 (-15.54%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.70 (n/a)</td><td>168.90 (n/a)</td><td>167.90 (n/a)</td><td>150.00 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (+8.62%)</td><td>0.05 (+11.56%)</td><td>0.05 (+4.63%)</td><td>0.04 <b>(+32.27%)</b></td><td>0.01 <b>(-25.57%)</b></td><td>195.20 <b>(-24.37%)</b></td><td>168.82 (-13.15%)</td><td>167.70 (-4.44%)</td><td>130.20 (-7.92%)</td><td>24.70 <b>(-50.28%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.10 (n/a)</td><td>194.38 (n/a)</td><td>175.50 (n/a)</td><td>141.40 (n/a)</td><td>49.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-17.98%)</td><td>0.05 (+6.99%)</td><td>0.05 <b>(+24.28%)</b></td><td>0.04 (-3.37%)</td><td>0.01 <b>(-39.41%)</b></td><td>213.60 (+3.49%)</td><td>162.50 (-9.09%)</td><td>157.80 (-19.57%)</td><td>136.30 <b>(+21.91%)</b></td><td>30.91 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>178.74 (n/a)</td><td>196.20 (n/a)</td><td>111.80 (n/a)</td><td>39.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-2.84%)</td><td>0.05 (+2.78%)</td><td>0.04 (+5.84%)</td><td>0.04 (+8.76%)</td><td>0.01 (-15.43%)</td><td>218.00 (-8.06%)</td><td>184.76 (-3.87%)</td><td>191.80 (-5.52%)</td><td>136.40 (+2.94%)</td><td>32.41 (-18.57%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.10 (n/a)</td><td>192.20 (n/a)</td><td>203.00 (n/a)</td><td>132.50 (n/a)</td><td>39.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (+11.46%)</td><td>0.05 (+18.07%)</td><td>0.05 <b>(+23.61%)</b></td><td>0.04 (+10.23%)</td><td>0.01 (+15.06%)</td><td>204.90 (-9.30%)</td><td>171.86 (-15.22%)</td><td>165.50 (-19.11%)</td><td>147.30 (-10.29%)</td><td>23.55 (-6.42%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>202.72 (n/a)</td><td>204.60 (n/a)</td><td>164.20 (n/a)</td><td>25.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.18 (+0.18%)</td><td>0.18 (+0.17%)</td><td>0.18 (+0.11%)</td><td>0.18 (+0.17%)</td><td>0.00 <b>(+26.33%)</b></td><td>47542.10 (-0.17%)</td><td>47493.50 (-0.17%)</td><td>47530.70 (-0.11%)</td><td>47415.30 (-0.18%)</td><td>60.48 <b>(+25.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47624.80 (n/a)</td><td>47572.10 (n/a)</td><td>47584.00 (n/a)</td><td>47500.60 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.17 (-18.22%)</td><td>0.15 (-12.70%)</td><td>0.14 (-18.69%)</td><td>0.14 (+1.37%)</td><td>0.02 <b>(-50.48%)</b></td><td>181.20 (-1.36%)</td><td>167.10 (+12.31%)</td><td>170.60 <b>(+23.00%)</b></td><td>141.90 <b>(+22.33%)</b></td><td>16.49 <b>(-41.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.70 (n/a)</td><td>148.78 (n/a)</td><td>138.70 (n/a)</td><td>116.00 (n/a)</td><td>27.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.30 (-14.95%)</td><td>0.27 (-3.99%)</td><td>0.28 (+4.16%)</td><td>0.23 (+14.56%)</td><td>0.03 <b>(-46.76%)</b></td><td>178.60 (-12.71%)</td><td>153.66 (+1.13%)</td><td>146.90 (-3.99%)</td><td>134.80 (+17.52%)</td><td>19.68 <b>(-44.71%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>204.60 (n/a)</td><td>151.94 (n/a)</td><td>153.00 (n/a)</td><td>114.70 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-4.39%)</td><td>0.03 (-11.63%)</td><td>0.03 (-9.61%)</td><td>0.02 <b>(-29.54%)</b></td><td>0.01 <b>(+125.41%)</b></td><td>216.00 <b>(+41.92%)</b></td><td>167.28 (+15.81%)</td><td>163.30 (+10.64%)</td><td>134.30 (+4.60%)</td><td>31.68 <b>(+241.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>152.20 (n/a)</td><td>144.44 (n/a)</td><td>147.60 (n/a)</td><td>128.40 (n/a)</td><td>9.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (-17.87%)</td><td>0.05 (-5.29%)</td><td>0.05 (+7.65%)</td><td>0.05 (+15.41%)</td><td>0.00 <b>(-78.82%)</b></td><td>177.30 (-13.34%)</td><td>171.76 (+1.35%)</td><td>175.20 (-7.10%)</td><td>156.50 <b>(+21.70%)</b></td><td>8.60 <b>(-77.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>169.48 (n/a)</td><td>188.60 (n/a)</td><td>128.60 (n/a)</td><td>37.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.09 (+18.35%)</td><td>0.07 (+4.09%)</td><td>0.06 (-3.89%)</td><td>0.05 (+2.59%)</td><td>0.01 <b>(+70.31%)</b></td><td>226.20 (-2.54%)</td><td>185.50 (-2.28%)</td><td>195.40 (+4.05%)</td><td>143.40 (-15.50%)</td><td>34.92 <b>(+37.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>189.82 (n/a)</td><td>187.80 (n/a)</td><td>169.70 (n/a)</td><td>25.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-7.74%)</td><td>0.05 (-1.81%)</td><td>0.05 (-6.27%)</td><td>0.04 (+3.60%)</td><td>0.01 <b>(-34.56%)</b></td><td>205.20 (-3.48%)</td><td>173.42 (+0.48%)</td><td>172.20 (+6.69%)</td><td>147.40 (+8.38%)</td><td>20.67 <b>(-31.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.60 (n/a)</td><td>172.60 (n/a)</td><td>161.40 (n/a)</td><td>136.00 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 <b>(+31.73%)</b></td><td>0.06 (+9.87%)</td><td>0.06 (+3.74%)</td><td>0.05 (-0.63%)</td><td>0.01 <b>(+205.43%)</b></td><td>225.00 (+0.63%)</td><td>183.88 (-6.63%)</td><td>185.70 (-3.63%)</td><td>142.40 <b>(-24.05%)</b></td><td>34.93 <b>(+131.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>223.60 (n/a)</td><td>196.94 (n/a)</td><td>192.70 (n/a)</td><td>187.50 (n/a)</td><td>15.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-11.94%)</td><td>0.05 (-9.29%)</td><td>0.04 (+0.76%)</td><td>0.03 (+17.02%)</td><td>0.01 <b>(-36.33%)</b></td><td>249.30 (-14.54%)</td><td>192.64 (+2.24%)</td><td>184.60 (-0.75%)</td><td>126.30 (+13.58%)</td><td>48.54 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>291.70 (n/a)</td><td>188.42 (n/a)</td><td>186.00 (n/a)</td><td>111.20 (n/a)</td><td>75.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (+1.95%)</td><td>0.06 (-6.04%)</td><td>0.05 (-11.33%)</td><td>0.04 (-3.42%)</td><td>0.01 (+5.07%)</td><td>238.60 (+3.51%)</td><td>187.26 (+6.83%)</td><td>190.00 (+12.76%)</td><td>141.20 (-1.88%)</td><td>38.64 (+7.65%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>175.28 (n/a)</td><td>168.50 (n/a)</td><td>143.90 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (-7.53%)</td><td>0.05 (+0.72%)</td><td>0.04 (-6.46%)</td><td>0.04 (+5.52%)</td><td>0.01 (-5.43%)</td><td>213.40 (-5.24%)</td><td>174.72 (-0.78%)</td><td>201.00 (+6.91%)</td><td>120.40 (+8.08%)</td><td>42.93 (+2.76%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>176.10 (n/a)</td><td>188.00 (n/a)</td><td>111.40 (n/a)</td><td>41.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-3.45%)</td><td>0.05 (-5.98%)</td><td>0.04 (-8.01%)</td><td>0.04 (-13.43%)</td><td>0.01 (+11.37%)</td><td>255.90 (+15.53%)</td><td>206.60 (+7.08%)</td><td>205.80 (+8.72%)</td><td>163.40 (+3.55%)</td><td>34.32 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>192.94 (n/a)</td><td>189.30 (n/a)</td><td>157.80 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-6.49%)</td><td>0.04 (-12.71%)</td><td>0.04 (-9.25%)</td><td>0.03 (-14.55%)</td><td>0.01 (-9.30%)</td><td>238.90 (+17.05%)</td><td>194.78 (+14.67%)</td><td>205.70 (+10.24%)</td><td>139.30 (+6.91%)</td><td>38.98 (+14.10%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.10 (n/a)</td><td>169.86 (n/a)</td><td>186.60 (n/a)</td><td>130.30 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 <b>(+29.56%)</b></td><td>0.05 (+3.17%)</td><td>0.05 (+2.40%)</td><td>0.03 <b>(-27.78%)</b></td><td>0.01 <b>(+229.87%)</b></td><td>302.10 <b>(+38.45%)</b></td><td>202.16 (+2.73%)</td><td>185.40 (-2.37%)</td><td>139.40 <b>(-22.81%)</b></td><td>61.02 <b>(+264.16%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>218.20 (n/a)</td><td>196.78 (n/a)</td><td>189.90 (n/a)</td><td>180.60 (n/a)</td><td>16.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (+2.12%)</td><td>0.04 (+0.88%)</td><td>0.04 (+4.09%)</td><td>0.04 (+9.29%)</td><td>0.01 (-3.80%)</td><td>214.80 (-8.52%)</td><td>189.36 (-1.66%)</td><td>200.10 (-3.94%)</td><td>126.60 (-2.01%)</td><td>36.38 (-14.93%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>192.56 (n/a)</td><td>208.30 (n/a)</td><td>129.20 (n/a)</td><td>42.77 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-19.19%)</td><td>0.04 (-14.34%)</td><td>0.04 (-5.70%)</td><td>0.03 (-12.53%)</td><td>0.00 <b>(-43.29%)</b></td><td>271.00 (+14.35%)</td><td>223.66 (+15.32%)</td><td>217.80 (+6.09%)</td><td>197.10 <b>(+23.73%)</b></td><td>28.29 (-14.92%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>193.94 (n/a)</td><td>205.30 (n/a)</td><td>159.30 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (-11.90%)</td><td>0.05 (-3.33%)</td><td>0.04 (-6.67%)</td><td>0.04 (-7.08%)</td><td>0.01 (-16.26%)</td><td>219.20 (+7.61%)</td><td>182.16 (+3.00%)</td><td>189.80 (+7.11%)</td><td>146.30 (+13.50%)</td><td>30.71 (+0.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>176.86 (n/a)</td><td>177.20 (n/a)</td><td>128.90 (n/a)</td><td>30.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 <b>(-34.42%)</b></td><td>0.04 (-17.30%)</td><td>0.04 (-12.21%)</td><td>0.03 (-4.93%)</td><td>0.01 <b>(-52.17%)</b></td><td>328.60 (+5.19%)</td><td>230.98 (+13.48%)</td><td>204.40 (+13.87%)</td><td>189.00 <b>(+52.42%)</b></td><td>57.41 <b>(-23.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>312.40 (n/a)</td><td>203.54 (n/a)</td><td>179.50 (n/a)</td><td>124.00 (n/a)</td><td>74.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (-17.18%)</td><td>0.04 (-4.17%)</td><td>0.04 (-2.07%)</td><td>0.03 (+5.97%)</td><td>0.00 <b>(-63.01%)</b></td><td>234.60 (-5.63%)</td><td>219.32 (+2.60%)</td><td>219.90 (+2.09%)</td><td>197.50 <b>(+20.72%)</b></td><td>13.61 <b>(-57.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.60 (n/a)</td><td>213.76 (n/a)</td><td>215.40 (n/a)</td><td>163.60 (n/a)</td><td>31.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.67 <b>(+21.96%)</b></td><td>0.57 (+13.81%)</td><td>0.56 (+13.75%)</td><td>0.48 (+3.49%)</td><td>0.07 <b>(+98.99%)</b></td><td>204.30 (-3.36%)</td><td>173.96 (-11.36%)</td><td>174.10 (-12.12%)</td><td>146.00 (-18.02%)</td><td>22.22 <b>(+57.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.46 (n/a)</td><td>0.04 (n/a)</td><td>211.40 (n/a)</td><td>196.26 (n/a)</td><td>198.10 (n/a)</td><td>178.10 (n/a)</td><td>14.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.84 <b>(+39.73%)</b></td><td>0.58 (+10.56%)</td><td>0.48 (-7.50%)</td><td>0.48 (+9.33%)</td><td>0.15 <b>(+161.12%)</b></td><td>204.10 (-8.52%)</td><td>177.70 (-6.22%)</td><td>202.90 (+8.10%)</td><td>117.40 <b>(-28.46%)</b></td><td>38.57 <b>(+74.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.06 (n/a)</td><td>223.10 (n/a)</td><td>189.48 (n/a)</td><td>187.70 (n/a)</td><td>164.10 (n/a)</td><td>22.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.73 <b>(+25.84%)</b></td><td>0.59 (+10.89%)</td><td>0.61 (+10.48%)</td><td>0.46 (+4.96%)</td><td>0.10 <b>(+87.76%)</b></td><td>211.80 (-4.77%)</td><td>170.12 (-8.57%)</td><td>161.70 (-9.51%)</td><td>135.50 <b>(-20.57%)</b></td><td>29.15 <b>(+40.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.58 (n/a)</td><td>0.53 (n/a)</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.05 (n/a)</td><td>222.40 (n/a)</td><td>186.06 (n/a)</td><td>178.70 (n/a)</td><td>170.60 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.70 <b>(+26.82%)</b></td><td>0.47 (-4.14%)</td><td>0.39 (-19.27%)</td><td>0.32 (-18.80%)</td><td>0.16 <b>(+153.10%)</b></td><td>302.50 <b>(+23.12%)</b></td><td>225.24 (+11.54%)</td><td>249.30 <b>(+23.85%)</b></td><td>140.00 <b>(-21.13%)</b></td><td>66.80 <b>(+143.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.55 (n/a)</td><td>0.49 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>245.70 (n/a)</td><td>201.94 (n/a)</td><td>201.30 (n/a)</td><td>177.50 (n/a)</td><td>27.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.48 (+2.74%)</td><td>0.42 (+10.50%)</td><td>0.42 (+12.49%)</td><td>0.33 (+5.07%)</td><td>0.06 (+5.09%)</td><td>222.90 (-4.82%)</td><td>179.56 (-9.44%)</td><td>177.30 (-11.13%)</td><td>154.30 (-2.65%)</td><td>27.42 (-1.59%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>234.20 (n/a)</td><td>198.28 (n/a)</td><td>199.50 (n/a)</td><td>158.50 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.54 (+4.47%)</td><td>0.44 (+5.73%)</td><td>0.41 (+1.99%)</td><td>0.39 (+13.76%)</td><td>0.06 (-4.11%)</td><td>190.60 (-12.08%)</td><td>170.64 (-5.82%)</td><td>179.30 (-1.97%)</td><td>136.10 (-4.29%)</td><td>22.87 (-18.10%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>216.80 (n/a)</td><td>181.18 (n/a)</td><td>182.90 (n/a)</td><td>142.20 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.49 (-7.46%)</td><td>0.38 (-7.61%)</td><td>0.37 (+5.22%)</td><td>0.30 (-10.32%)</td><td>0.07 <b>(-23.83%)</b></td><td>246.80 (+11.52%)</td><td>199.72 (+6.92%)</td><td>201.30 (-4.96%)</td><td>151.50 (+8.06%)</td><td>36.08 (-8.66%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>221.30 (n/a)</td><td>186.80 (n/a)</td><td>211.80 (n/a)</td><td>140.20 (n/a)</td><td>39.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.59 <b>(+35.03%)</b></td><td>0.39 (+10.22%)</td><td>0.34 (-11.23%)</td><td>0.25 (+10.28%)</td><td>0.13 <b>(+63.06%)</b></td><td>298.50 (-9.33%)</td><td>206.78 (-6.25%)</td><td>218.30 (+12.64%)</td><td>126.00 <b>(-25.93%)</b></td><td>65.55 (+3.27%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>329.20 (n/a)</td><td>220.56 (n/a)</td><td>193.80 (n/a)</td><td>170.10 (n/a)</td><td>63.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.94 <b>(-30.34%)</b></td><td>0.72 (-14.01%)</td><td>0.69 (-2.14%)</td><td>0.61 (-6.16%)</td><td>0.13 <b>(-56.67%)</b></td><td>215.40 (+6.53%)</td><td>186.52 (+10.22%)</td><td>189.80 (+2.15%)</td><td>139.60 <b>(+43.47%)</b></td><td>28.27 <b>(-35.51%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.35 (n/a)</td><td>0.84 (n/a)</td><td>0.71 (n/a)</td><td>0.65 (n/a)</td><td>0.30 (n/a)</td><td>202.20 (n/a)</td><td>169.22 (n/a)</td><td>185.80 (n/a)</td><td>97.30 (n/a)</td><td>43.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.17 <b>(+31.91%)</b></td><td>0.78 (+4.43%)</td><td>0.71 (-4.73%)</td><td>0.56 (-8.49%)</td><td>0.24 <b>(+118.40%)</b></td><td>236.00 (+9.26%)</td><td>178.38 (+0.45%)</td><td>183.40 (+4.92%)</td><td>112.20 <b>(-24.19%)</b></td><td>47.53 <b>(+77.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.89 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.11 (n/a)</td><td>216.00 (n/a)</td><td>177.58 (n/a)</td><td>174.80 (n/a)</td><td>148.00 (n/a)</td><td>26.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.91 (-10.08%)</td><td>0.79 (+4.58%)</td><td>0.82 <b>(+23.90%)</b></td><td>0.61 (-4.54%)</td><td>0.11 <b>(-29.87%)</b></td><td>213.30 (+4.76%)</td><td>169.28 (-5.63%)</td><td>160.00 (-19.27%)</td><td>144.30 (+11.17%)</td><td>26.76 (-18.12%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.01 (n/a)</td><td>0.75 (n/a)</td><td>0.66 (n/a)</td><td>0.64 (n/a)</td><td>0.16 (n/a)</td><td>203.60 (n/a)</td><td>179.38 (n/a)</td><td>198.20 (n/a)</td><td>129.80 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (-12.48%)</td><td>0.03 (+9.67%)</td><td>0.03 <b>(+21.38%)</b></td><td>0.02 <b>(+20.57%)</b></td><td>0.00 <b>(-47.72%)</b></td><td>172.70 (-17.05%)</td><td>153.66 (-11.17%)</td><td>148.50 (-17.64%)</td><td>138.10 (+14.23%)</td><td>17.11 <b>(-49.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.20 (n/a)</td><td>172.98 (n/a)</td><td>180.30 (n/a)</td><td>120.90 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (-5.24%)</td><td>0.03 (+3.54%)</td><td>0.03 (+0.23%)</td><td>0.02 (-3.41%)</td><td>0.00 (-1.51%)</td><td>236.00 (+3.55%)</td><td>164.32 (-3.16%)</td><td>152.70 (-0.26%)</td><td>138.70 (+5.48%)</td><td>40.64 (+8.57%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>169.68 (n/a)</td><td>153.10 (n/a)</td><td>131.50 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (-5.20%)</td><td>0.03 (+15.05%)</td><td>0.03 <b>(+28.50%)</b></td><td>0.02 <b>(+34.01%)</b></td><td>0.00 <b>(-30.51%)</b></td><td>213.10 <b>(-25.36%)</b></td><td>167.42 (-16.21%)</td><td>152.20 <b>(-22.19%)</b></td><td>144.30 (+5.48%)</td><td>29.96 <b>(-46.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>285.50 (n/a)</td><td>199.82 (n/a)</td><td>195.60 (n/a)</td><td>136.80 (n/a)</td><td>55.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.06 <b>(+23.27%)</b></td><td>0.78 (+2.68%)</td><td>0.73 (-8.09%)</td><td>0.64 (+2.87%)</td><td>0.17 <b>(+91.53%)</b></td><td>205.40 (-2.79%)</td><td>174.58 (-0.48%)</td><td>181.40 (+8.75%)</td><td>124.60 (-18.88%)</td><td>33.32 <b>(+49.23%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.86 (n/a)</td><td>0.76 (n/a)</td><td>0.79 (n/a)</td><td>0.63 (n/a)</td><td>0.09 (n/a)</td><td>211.30 (n/a)</td><td>175.42 (n/a)</td><td>166.80 (n/a)</td><td>153.60 (n/a)</td><td>22.33 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.93 (-17.99%)</td><td>0.84 (+16.79%)</td><td>0.80 <b>(+25.71%)</b></td><td>0.75 <b>(+37.68%)</b></td><td>0.08 <b>(-66.34%)</b></td><td>176.80 <b>(-27.39%)</b></td><td>158.42 (-19.26%)</td><td>164.20 <b>(-20.45%)</b></td><td>142.70 <b>(+21.97%)</b></td><td>14.82 <b>(-69.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>1.13 (n/a)</td><td>0.72 (n/a)</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.24 (n/a)</td><td>243.50 (n/a)</td><td>196.22 (n/a)</td><td>206.40 (n/a)</td><td>117.00 (n/a)</td><td>48.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.19 <b>(+26.43%)</b></td><td>0.75 (-9.68%)</td><td>0.69 <b>(-20.41%)</b></td><td>0.54 <b>(-23.37%)</b></td><td>0.25 <b>(+165.53%)</b></td><td>242.50 <b>(+30.52%)</b></td><td>190.10 (+17.64%)</td><td>191.10 <b>(+25.64%)</b></td><td>111.20 <b>(-20.91%)</b></td><td>49.27 <b>(+156.36%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.94 (n/a)</td><td>0.83 (n/a)</td><td>0.87 (n/a)</td><td>0.71 (n/a)</td><td>0.10 (n/a)</td><td>185.80 (n/a)</td><td>161.60 (n/a)</td><td>152.10 (n/a)</td><td>140.60 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.05 (+10.45%)</td><td>0.78 (-0.77%)</td><td>0.74 (-4.79%)</td><td>0.60 (-10.89%)</td><td>0.17 <b>(+61.40%)</b></td><td>220.40 (+12.22%)</td><td>174.88 (+2.83%)</td><td>179.00 (+5.05%)</td><td>125.30 (-9.47%)</td><td>33.91 <b>(+62.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.95 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.10 (n/a)</td><td>196.40 (n/a)</td><td>170.06 (n/a)</td><td>170.40 (n/a)</td><td>138.40 (n/a)</td><td>20.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.93 (+16.50%)</td><td>0.81 (+17.08%)</td><td>0.81 (+19.35%)</td><td>0.74 <b>(+29.84%)</b></td><td>0.08 <b>(-21.42%)</b></td><td>179.00 <b>(-23.01%)</b></td><td>163.74 (-15.41%)</td><td>162.90 (-16.20%)</td><td>142.30 (-14.17%)</td><td>14.88 <b>(-46.70%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.57 (n/a)</td><td>0.10 (n/a)</td><td>232.50 (n/a)</td><td>193.56 (n/a)</td><td>194.40 (n/a)</td><td>165.80 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (-9.33%)</td><td>0.03 (+16.22%)</td><td>0.03 <b>(+24.98%)</b></td><td>0.02 <b>(+20.49%)</b></td><td>0.00 <b>(-59.95%)</b></td><td>179.40 (-17.02%)</td><td>162.00 (-16.32%)</td><td>163.10 <b>(-20.01%)</b></td><td>147.00 (+10.28%)</td><td>12.83 <b>(-62.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.20 (n/a)</td><td>193.60 (n/a)</td><td>203.90 (n/a)</td><td>133.30 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (+3.34%)</td><td>0.02 (+6.23%)</td><td>0.03 (+14.71%)</td><td>0.02 (+4.16%)</td><td>0.00 (+18.22%)</td><td>221.80 (-4.02%)</td><td>176.36 (-5.50%)</td><td>160.20 (-12.79%)</td><td>155.00 (-3.19%)</td><td>28.41 (+6.29%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>186.62 (n/a)</td><td>183.70 (n/a)</td><td>160.10 (n/a)</td><td>26.73 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.00 (+4.65%)</td><td>0.00 (+1.89%)</td><td>0.00 (+2.38%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+138.05%)</b></td><td>984.43 (+0.69%)</td><td>955.67 (-1.13%)</td><td>961.96 (-0.98%)</td><td>920.43 (-3.44%)</td><td>29.07 <b>(+149.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>977.72 (n/a)</td><td>966.63 (n/a)</td><td>971.51 (n/a)</td><td>953.22 (n/a)</td><td>11.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.01 (+1.19%)</td><td>0.01 (+2.30%)</td><td>0.01 (+1.27%)</td><td>0.01 (+7.25%)</td><td>0.00 <b>(-28.94%)</b></td><td>1113.97 (-5.65%)</td><td>1027.66 (-2.15%)</td><td>1019.79 (-1.13%)</td><td>965.47 (-0.64%)</td><td>53.68 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1180.69 (n/a)</td><td>1050.25 (n/a)</td><td>1031.46 (n/a)</td><td>971.68 (n/a)</td><td>77.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.01 (+3.45%)</td><td>0.97 (+0.67%)</td><td>0.96 (-0.05%)</td><td>0.95 (-0.66%)</td><td>0.02 <b>(+220.06%)</b></td><td>2212.39 (+0.67%)</td><td>2167.31 (-0.63%)</td><td>2182.81 (+0.05%)</td><td>2083.95 (-3.35%)</td><td>49.70 <b>(+211.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2197.77 (n/a)</td><td>2180.96 (n/a)</td><td>2181.66 (n/a)</td><td>2156.11 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.87 (+14.93%)</td><td>3.26 (+7.46%)</td><td>3.18 (+3.72%)</td><td>2.81 (+9.13%)</td><td>0.39 <b>(+23.83%)</b></td><td>186.80 (-8.39%)</td><td>162.44 (-6.78%)</td><td>165.00 (-3.62%)</td><td>135.40 (-12.98%)</td><td>18.43 (-3.01%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.37 (n/a)</td><td>3.04 (n/a)</td><td>3.06 (n/a)</td><td>2.57 (n/a)</td><td>0.31 (n/a)</td><td>203.90 (n/a)</td><td>174.26 (n/a)</td><td>171.20 (n/a)</td><td>155.60 (n/a)</td><td>19.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>5.95 <b>(+30.26%)</b></td><td>5.69 <b>(+37.80%)</b></td><td>5.60 <b>(+35.97%)</b></td><td>5.58 <b>(+48.66%)</b></td><td>0.16 <b>(-46.77%)</b></td><td>187.90 <b>(-32.72%)</b></td><td>184.24 <b>(-27.69%)</b></td><td>187.10 <b>(-26.45%)</b></td><td>176.20 <b>(-23.22%)</b></td><td>5.05 <b>(-72.42%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>4.57 (n/a)</td><td>4.13 (n/a)</td><td>4.12 (n/a)</td><td>3.75 (n/a)</td><td>0.30 (n/a)</td><td>279.30 (n/a)</td><td>254.78 (n/a)</td><td>254.40 (n/a)</td><td>229.50 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.13 (+6.96%)</td><td>3.43 (+18.04%)</td><td>3.46 <b>(+24.33%)</b></td><td>2.90 (+17.31%)</td><td>0.51 (-9.91%)</td><td>180.90 (-14.75%)</td><td>155.54 (-16.01%)</td><td>151.70 (-19.57%)</td><td>126.80 (-6.49%)</td><td>22.72 <b>(-26.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:21:41</td><td>3.87 (n/a)</td><td>2.91 (n/a)</td><td>2.78 (n/a)</td><td>2.47 (n/a)</td><td>0.57 (n/a)</td><td>212.20 (n/a)</td><td>185.18 (n/a)</td><td>188.60 (n/a)</td><td>135.60 (n/a)</td><td>30.78 (n/a)</td>
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
