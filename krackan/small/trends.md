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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (+3.30%)</td><td>0.08 (+19.43%)</td><td>0.08 <b>(+22.91%)</b></td><td>0.07 <b>(+42.27%)</b></td><td>0.01 <b>(-47.88%)</b></td><td>171.00 <b>(-29.72%)</b></td><td>158.34 (-18.01%)</td><td>157.50 (-18.65%)</td><td>143.60 (-3.17%)</td><td>12.50 <b>(-64.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>243.30 (n/a)</td><td>193.12 (n/a)</td><td>193.60 (n/a)</td><td>148.30 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (+18.37%)</td><td>0.08 (+8.70%)</td><td>0.08 (+2.83%)</td><td>0.05 (-0.37%)</td><td>0.02 <b>(+38.37%)</b></td><td>233.40 (+0.39%)</td><td>168.06 (-6.56%)</td><td>159.00 (-2.75%)</td><td>129.00 (-15.52%)</td><td>40.05 <b>(+20.42%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>179.86 (n/a)</td><td>163.50 (n/a)</td><td>152.70 (n/a)</td><td>33.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (-7.39%)</td><td>0.07 (+0.92%)</td><td>0.07 (+6.99%)</td><td>0.06 (+7.84%)</td><td>0.01 <b>(-32.96%)</b></td><td>216.50 (-7.24%)</td><td>182.26 (-2.00%)</td><td>173.70 (-6.56%)</td><td>162.80 (+7.96%)</td><td>20.65 <b>(-32.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.40 (n/a)</td><td>185.98 (n/a)</td><td>185.90 (n/a)</td><td>150.80 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (+10.78%)</td><td>0.07 (+3.48%)</td><td>0.06 (-3.36%)</td><td>0.06 (+3.87%)</td><td>0.01 <b>(+68.77%)</b></td><td>210.20 (-3.75%)</td><td>188.32 (-2.68%)</td><td>200.00 (+3.47%)</td><td>159.20 (-9.75%)</td><td>22.76 <b>(+44.98%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>218.40 (n/a)</td><td>193.50 (n/a)</td><td>193.30 (n/a)</td><td>176.40 (n/a)</td><td>15.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (-11.95%)</td><td>0.03 (-16.61%)</td><td>0.03 (-8.33%)</td><td>0.02 <b>(-32.19%)</b></td><td>0.01 (+15.76%)</td><td>334.30 <b>(+47.46%)</b></td><td>208.90 <b>(+25.45%)</b></td><td>174.60 (+9.12%)</td><td>148.60 (+13.61%)</td><td>74.79 <b>(+98.31%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>166.52 (n/a)</td><td>160.00 (n/a)</td><td>130.80 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (+7.00%)</td><td>0.03 (+2.24%)</td><td>0.04 (+0.70%)</td><td>0.02 (-16.11%)</td><td>0.01 <b>(+64.42%)</b></td><td>224.30 (+19.18%)</td><td>158.80 (+0.16%)</td><td>148.10 (-0.67%)</td><td>132.10 (-6.51%)</td><td>37.28 <b>(+90.74%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.20 (n/a)</td><td>158.54 (n/a)</td><td>149.10 (n/a)</td><td>141.30 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (-8.03%)</td><td>0.03 (-11.92%)</td><td>0.03 (-18.65%)</td><td>0.02 (-4.09%)</td><td>0.01 (-18.21%)</td><td>221.60 (+4.28%)</td><td>176.04 (+12.54%)</td><td>165.20 <b>(+22.92%)</b></td><td>137.30 (+8.80%)</td><td>34.58 (-5.66%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>156.42 (n/a)</td><td>134.40 (n/a)</td><td>126.20 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (+2.08%)</td><td>0.03 (-1.40%)</td><td>0.03 (-0.59%)</td><td>0.02 (-1.07%)</td><td>0.01 <b>(+21.92%)</b></td><td>212.80 (+1.09%)</td><td>172.94 (+2.42%)</td><td>173.10 (+0.58%)</td><td>133.50 (-2.05%)</td><td>33.47 <b>(+20.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>168.86 (n/a)</td><td>172.10 (n/a)</td><td>136.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (+2.14%)</td><td>0.03 (+5.22%)</td><td>0.03 (+6.26%)</td><td>0.02 (+5.05%)</td><td>0.00 (-7.24%)</td><td>215.20 (-4.78%)</td><td>183.78 (-5.19%)</td><td>181.70 (-5.90%)</td><td>155.70 (-2.08%)</td><td>21.16 (-12.33%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.00 (n/a)</td><td>193.84 (n/a)</td><td>193.10 (n/a)</td><td>159.00 (n/a)</td><td>24.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (-1.09%)</td><td>0.03 (+3.26%)</td><td>0.03 (+0.86%)</td><td>0.02 (-7.23%)</td><td>0.01 (-0.16%)</td><td>224.30 (+7.78%)</td><td>172.08 (-2.87%)</td><td>177.20 (-0.84%)</td><td>124.80 (+1.13%)</td><td>36.80 (+9.55%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>177.16 (n/a)</td><td>178.70 (n/a)</td><td>123.40 (n/a)</td><td>33.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 <b>(+53.40%)</b></td><td>0.03 (+18.26%)</td><td>0.03 (+13.58%)</td><td>0.02 (+18.27%)</td><td>0.01 <b>(+108.54%)</b></td><td>218.50 (-15.44%)</td><td>176.38 (-12.51%)</td><td>176.40 (-11.93%)</td><td>109.50 <b>(-34.82%)</b></td><td>42.79 (+14.96%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.40 (n/a)</td><td>201.60 (n/a)</td><td>200.30 (n/a)</td><td>168.00 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (-9.46%)</td><td>0.02 (-2.23%)</td><td>0.02 (+3.62%)</td><td>0.02 (-0.44%)</td><td>0.00 <b>(-41.78%)</b></td><td>249.60 (+0.44%)</td><td>228.42 (+1.39%)</td><td>230.60 (-3.51%)</td><td>203.60 (+10.47%)</td><td>18.16 <b>(-36.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>248.50 (n/a)</td><td>225.28 (n/a)</td><td>239.00 (n/a)</td><td>184.30 (n/a)</td><td>28.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>344.30 (n/a)</td><td>197.26 (n/a)</td><td>160.00 (n/a)</td><td>129.30 (n/a)</td><td>89.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>288.10 (n/a)</td><td>207.98 (n/a)</td><td>199.30 (n/a)</td><td>145.00 (n/a)</td><td>59.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.50 (n/a)</td><td>166.32 (n/a)</td><td>154.60 (n/a)</td><td>126.00 (n/a)</td><td>36.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>350.20 (n/a)</td><td>224.78 (n/a)</td><td>191.80 (n/a)</td><td>174.30 (n/a)</td><td>72.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>145.52 (n/a)</td><td>138.30 (n/a)</td><td>128.40 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>155.10 (n/a)</td><td>136.18 (n/a)</td><td>133.60 (n/a)</td><td>120.20 (n/a)</td><td>13.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>214.90 (n/a)</td><td>155.32 (n/a)</td><td>153.10 (n/a)</td><td>118.00 (n/a)</td><td>39.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>241.60 (n/a)</td><td>171.06 (n/a)</td><td>148.40 (n/a)</td><td>130.20 (n/a)</td><td>48.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.26 (+3.46%)</td><td>3.03 (+1.73%)</td><td>3.11 (+4.06%)</td><td>2.74 (-1.79%)</td><td>0.25 <b>(+82.31%)</b></td><td>502.50 (+1.82%)</td><td>457.06 (-1.32%)</td><td>442.60 (-3.91%)</td><td>422.70 (-3.36%)</td><td>38.51 <b>(+79.16%)</b></td><td>634.98 (+3.46%)</td><td>590.57 (+1.73%)</td><td>606.52 (+4.06%)</td><td>534.17 (-1.79%)</td><td>48.71 <b>(+82.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.15 (n/a)</td><td>2.98 (n/a)</td><td>2.99 (n/a)</td><td>2.79 (n/a)</td><td>0.14 (n/a)</td><td>493.50 (n/a)</td><td>463.18 (n/a)</td><td>460.60 (n/a)</td><td>437.40 (n/a)</td><td>21.49 (n/a)</td><td>613.77 (n/a)</td><td>580.53 (n/a)</td><td>582.83 (n/a)</td><td>543.92 (n/a)</td><td>26.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.89 (+0.02%)</td><td>3.91 (-4.28%)</td><td>3.67 (-5.03%)</td><td>3.50 (+5.04%)</td><td>0.57 (-16.09%)</td><td>393.50 (-4.79%)</td><td>357.28 (+3.73%)</td><td>374.80 (+5.28%)</td><td>281.50 (+0.00%)</td><td>45.54 (-19.39%)</td><td>953.64 (+0.02%)</td><td>762.72 (-4.28%)</td><td>716.16 (-5.03%)</td><td>682.21 (+5.04%)</td><td>111.65 (-16.09%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.89 (n/a)</td><td>4.09 (n/a)</td><td>3.87 (n/a)</td><td>3.33 (n/a)</td><td>0.68 (n/a)</td><td>413.30 (n/a)</td><td>344.42 (n/a)</td><td>356.00 (n/a)</td><td>281.50 (n/a)</td><td>56.50 (n/a)</td><td>953.48 (n/a)</td><td>796.78 (n/a)</td><td>754.11 (n/a)</td><td>649.47 (n/a)</td><td>133.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>5.23 (-12.85%)</td><td>4.19 (-8.73%)</td><td>3.83 (+3.47%)</td><td>3.61 (-1.00%)</td><td>0.72 <b>(-43.33%)</b></td><td>381.70 (+1.01%)</td><td>335.46 (+5.79%)</td><td>359.30 (-3.34%)</td><td>263.40 (+14.77%)</td><td>53.32 <b>(-33.09%)</b></td><td>1019.31 (-12.85%)</td><td>818.04 (-8.73%)</td><td>747.16 (+3.47%)</td><td>703.34 (-1.00%)</td><td>140.45 <b>(-43.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>6.00 (n/a)</td><td>4.60 (n/a)</td><td>3.70 (n/a)</td><td>3.64 (n/a)</td><td>1.27 (n/a)</td><td>377.90 (n/a)</td><td>317.10 (n/a)</td><td>371.70 (n/a)</td><td>229.50 (n/a)</td><td>79.68 (n/a)</td><td>1169.58 (n/a)</td><td>896.34 (n/a)</td><td>722.14 (n/a)</td><td>710.42 (n/a)</td><td>247.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>7.15 (-2.47%)</td><td>4.24 (-5.65%)</td><td>3.60 (-6.55%)</td><td>3.27 (+3.95%)</td><td>1.63 (-1.37%)</td><td>421.10 (-3.79%)</td><td>352.94 (+5.83%)</td><td>381.90 (+7.03%)</td><td>192.50 (+2.50%)</td><td>91.30 (-2.72%)</td><td>1394.35 (-2.47%)</td><td>826.26 (-5.65%)</td><td>702.97 (-6.55%)</td><td>637.47 (+3.95%)</td><td>318.87 (-1.37%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>7.33 (n/a)</td><td>4.49 (n/a)</td><td>3.86 (n/a)</td><td>3.14 (n/a)</td><td>1.66 (n/a)</td><td>437.70 (n/a)</td><td>333.50 (n/a)</td><td>356.80 (n/a)</td><td>187.80 (n/a)</td><td>93.85 (n/a)</td><td>1429.63 (n/a)</td><td>875.76 (n/a)</td><td>752.25 (n/a)</td><td>613.28 (n/a)</td><td>323.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.82 (-13.77%)</td><td>3.30 (-6.25%)</td><td>3.14 (-8.74%)</td><td>3.06 (+4.11%)</td><td>0.31 <b>(-43.91%)</b></td><td>449.60 (-3.95%)</td><td>419.74 (+5.46%)</td><td>437.90 (+9.58%)</td><td>360.30 (+15.96%)</td><td>36.11 <b>(-36.31%)</b></td><td>744.98 (-13.77%)</td><td>643.64 (-6.25%)</td><td>613.03 (-8.74%)</td><td>597.02 (+4.11%)</td><td>60.29 <b>(-43.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.43 (n/a)</td><td>3.52 (n/a)</td><td>3.44 (n/a)</td><td>2.94 (n/a)</td><td>0.55 (n/a)</td><td>468.10 (n/a)</td><td>398.02 (n/a)</td><td>399.60 (n/a)</td><td>310.70 (n/a)</td><td>56.69 (n/a)</td><td>863.98 (n/a)</td><td>686.55 (n/a)</td><td>671.73 (n/a)</td><td>573.47 (n/a)</td><td>107.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.92 <b>(+70.16%)</b></td><td>1.23 (+16.04%)</td><td>1.09 (+3.16%)</td><td>0.95 (-5.81%)</td><td>0.40 <b>(+754.75%)</b></td><td>423.70 (+6.16%)</td><td>346.54 (-8.29%)</td><td>366.70 (-3.07%)</td><td>208.90 <b>(-41.24%)</b></td><td>84.49 <b>(+415.81%)</b></td><td>160.63 <b>(+70.16%)</b></td><td>103.20 (+16.04%)</td><td>91.50 (+3.16%)</td><td>79.20 (-5.81%)</td><td>33.17 <b>(+754.75%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.13 (n/a)</td><td>1.06 (n/a)</td><td>1.06 (n/a)</td><td>1.01 (n/a)</td><td>0.05 (n/a)</td><td>399.10 (n/a)</td><td>377.86 (n/a)</td><td>378.30 (n/a)</td><td>355.50 (n/a)</td><td>16.38 (n/a)</td><td>94.40 (n/a)</td><td>88.94 (n/a)</td><td>88.70 (n/a)</td><td>84.08 (n/a)</td><td>3.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.41 (-13.42%)</td><td>5.31 (-12.63%)</td><td>5.13 <b>(-23.80%)</b></td><td>4.60 (+4.96%)</td><td>0.79 <b>(-40.78%)</b></td><td>420.40 (-4.74%)</td><td>369.98 (+11.54%)</td><td>377.20 <b>(+31.25%)</b></td><td>301.50 (+15.47%)</td><td>52.54 <b>(-33.91%)</b></td><td>1335.39 (-13.42%)</td><td>1106.84 (-12.63%)</td><td>1067.43 <b>(-23.80%)</b></td><td>957.69 (+4.96%)</td><td>164.21 <b>(-40.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>7.41 (n/a)</td><td>6.08 (n/a)</td><td>6.73 (n/a)</td><td>4.38 (n/a)</td><td>1.33 (n/a)</td><td>441.30 (n/a)</td><td>331.70 (n/a)</td><td>287.40 (n/a)</td><td>261.10 (n/a)</td><td>79.50 (n/a)</td><td>1542.35 (n/a)</td><td>1266.81 (n/a)</td><td>1400.81 (n/a)</td><td>912.48 (n/a)</td><td>277.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>18.66 (+11.92%)</td><td>13.69 (+11.79%)</td><td>13.44 (+18.87%)</td><td>11.17 (+5.16%)</td><td>2.96 (+18.68%)</td><td>492.80 (-4.92%)</td><td>415.18 (-10.06%)</td><td>409.60 (-15.86%)</td><td>295.10 (-10.63%)</td><td>76.49 (+2.32%)</td><td>7277.83 (+11.92%)</td><td>5340.51 (+11.79%)</td><td>5243.39 (+18.87%)</td><td>4357.56 (+5.16%)</td><td>1153.05 (+18.68%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>16.67 (n/a)</td><td>12.25 (n/a)</td><td>11.31 (n/a)</td><td>10.62 (n/a)</td><td>2.49 (n/a)</td><td>518.30 (n/a)</td><td>461.64 (n/a)</td><td>486.80 (n/a)</td><td>330.20 (n/a)</td><td>74.76 (n/a)</td><td>6502.70 (n/a)</td><td>4777.47 (n/a)</td><td>4411.15 (n/a)</td><td>4143.64 (n/a)</td><td>971.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.70 (n/a)</td><td>190.72 (n/a)</td><td>177.50 (n/a)</td><td>153.40 (n/a)</td><td>46.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.40 (n/a)</td><td>201.18 (n/a)</td><td>176.50 (n/a)</td><td>156.90 (n/a)</td><td>44.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.30 (n/a)</td><td>193.84 (n/a)</td><td>180.40 (n/a)</td><td>176.80 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>245.50 (n/a)</td><td>192.56 (n/a)</td><td>215.30 (n/a)</td><td>114.70 (n/a)</td><td>54.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.70 (n/a)</td><td>197.08 (n/a)</td><td>197.00 (n/a)</td><td>140.70 (n/a)</td><td>44.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>202.36 (n/a)</td><td>187.90 (n/a)</td><td>171.10 (n/a)</td><td>30.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.60 (n/a)</td><td>223.68 (n/a)</td><td>209.60 (n/a)</td><td>147.40 (n/a)</td><td>62.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>253.60 (n/a)</td><td>222.84 (n/a)</td><td>217.30 (n/a)</td><td>192.00 (n/a)</td><td>24.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.94 (+1.18%)</td><td>4.48 (+5.12%)</td><td>4.27 (+2.08%)</td><td>4.05 (+12.76%)</td><td>0.42 (-14.35%)</td><td>2322.30 (-11.32%)</td><td>2111.92 (-5.24%)</td><td>2201.80 (-2.04%)</td><td>1904.30 (-1.17%)</td><td>192.05 <b>(-26.54%)</b></td><td>1942.62 (+1.18%)</td><td>1763.57 (+5.12%)</td><td>1680.19 (+2.08%)</td><td>1592.99 (+12.76%)</td><td>163.76 (-14.35%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.88 (n/a)</td><td>4.27 (n/a)</td><td>4.18 (n/a)</td><td>3.59 (n/a)</td><td>0.49 (n/a)</td><td>2618.60 (n/a)</td><td>2228.72 (n/a)</td><td>2247.60 (n/a)</td><td>1926.80 (n/a)</td><td>261.43 (n/a)</td><td>1919.91 (n/a)</td><td>1677.71 (n/a)</td><td>1645.91 (n/a)</td><td>1412.75 (n/a)</td><td>191.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.21 (+10.23%)</td><td>1.08 (+7.88%)</td><td>1.02 (+2.16%)</td><td>1.01 (+11.12%)</td><td>0.09 <b>(+23.03%)</b></td><td>219.60 (-10.00%)</td><td>206.08 (-7.20%)</td><td>216.30 (-2.13%)</td><td>182.50 (-9.29%)</td><td>16.89 (+1.40%)</td><td>51.71 (+10.23%)</td><td>46.05 (+7.88%)</td><td>43.63 (+2.16%)</td><td>42.98 (+11.12%)</td><td>3.94 <b>(+23.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.10 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.91 (n/a)</td><td>0.08 (n/a)</td><td>244.00 (n/a)</td><td>222.08 (n/a)</td><td>221.00 (n/a)</td><td>201.20 (n/a)</td><td>16.66 (n/a)</td><td>46.91 (n/a)</td><td>42.69 (n/a)</td><td>42.71 (n/a)</td><td>38.68 (n/a)</td><td>3.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.27 (+3.88%)</td><td>0.98 (+6.36%)</td><td>0.95 (+1.27%)</td><td>0.68 (+3.90%)</td><td>0.21 (+1.37%)</td><td>323.90 (-3.74%)</td><td>236.12 (-6.13%)</td><td>232.50 (-1.27%)</td><td>174.40 (-3.70%)</td><td>55.54 (-5.20%)</td><td>54.12 (+3.88%)</td><td>41.65 (+6.36%)</td><td>40.58 (+1.27%)</td><td>29.14 (+3.90%)</td><td>9.13 (+1.37%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.22 (n/a)</td><td>0.92 (n/a)</td><td>0.94 (n/a)</td><td>0.66 (n/a)</td><td>0.21 (n/a)</td><td>336.50 (n/a)</td><td>251.54 (n/a)</td><td>235.50 (n/a)</td><td>181.10 (n/a)</td><td>58.58 (n/a)</td><td>52.10 (n/a)</td><td>39.16 (n/a)</td><td>40.07 (n/a)</td><td>28.04 (n/a)</td><td>9.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.53 (+0.33%)</td><td>0.53 (+0.03%)</td><td>0.53 (-0.07%)</td><td>0.53 (+0.04%)</td><td>0.00 <b>(+81.68%)</b></td><td>47828.70 (-0.04%)</td><td>47733.52 (-0.03%)</td><td>47789.70 (+0.07%)</td><td>47458.10 (-0.33%)</td><td>155.34 <b>(+80.98%)</b></td><td>362.00 (+0.33%)</td><td>359.92 (+0.03%)</td><td>359.49 (-0.07%)</td><td>359.20 (+0.04%)</td><td>1.18 <b>(+81.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47848.40 (n/a)</td><td>47748.80 (n/a)</td><td>47755.60 (n/a)</td><td>47613.00 (n/a)</td><td>85.83 (n/a)</td><td>360.82 (n/a)</td><td>359.80 (n/a)</td><td>359.75 (n/a)</td><td>359.05 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.91 (+0.32%)</td><td>0.90 (+0.27%)</td><td>0.90 (+0.02%)</td><td>0.90 (+0.68%)</td><td>0.00 <b>(-30.94%)</b></td><td>28037.30 (-0.68%)</td><td>27899.72 (-0.27%)</td><td>27888.40 (-0.02%)</td><td>27743.10 (-0.32%)</td><td>108.15 <b>(-31.69%)</b></td><td>619.25 (+0.32%)</td><td>615.78 (+0.27%)</td><td>616.02 (+0.02%)</td><td>612.75 (+0.68%)</td><td>2.39 <b>(-30.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28228.20 (n/a)</td><td>27974.92 (n/a)</td><td>27893.70 (n/a)</td><td>27832.60 (n/a)</td><td>158.31 (n/a)</td><td>617.26 (n/a)</td><td>614.13 (n/a)</td><td>615.90 (n/a)</td><td>608.61 (n/a)</td><td>3.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.44 (+3.63%)</td><td>3.27 (+3.44%)</td><td>3.25 (+3.19%)</td><td>3.17 (+3.35%)</td><td>0.11 (+12.39%)</td><td>7940.60 (-3.24%)</td><td>7691.06 (-3.31%)</td><td>7734.40 (-3.09%)</td><td>7307.60 (-3.50%)</td><td>252.03 (+5.31%)</td><td>2350.97 (+3.63%)</td><td>2235.70 (+3.44%)</td><td>2221.22 (+3.19%)</td><td>2163.54 (+3.35%)</td><td>74.69 (+12.39%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.32 (n/a)</td><td>3.17 (n/a)</td><td>3.15 (n/a)</td><td>3.07 (n/a)</td><td>0.10 (n/a)</td><td>8206.40 (n/a)</td><td>7954.76 (n/a)</td><td>7981.40 (n/a)</td><td>7572.60 (n/a)</td><td>239.31 (n/a)</td><td>2268.69 (n/a)</td><td>2161.29 (n/a)</td><td>2152.48 (n/a)</td><td>2093.46 (n/a)</td><td>66.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>4.32 (-0.00%)</td><td>3.59 (-6.63%)</td><td>3.28 (-19.51%)</td><td>3.24 (+6.87%)</td><td>0.48 (-14.96%)</td><td>2487.30 (-6.43%)</td><td>2278.68 (+6.50%)</td><td>2459.60 <b>(+24.23%)</b></td><td>1867.60 (+0.01%)</td><td>282.13 (-17.85%)</td><td>1131.91 (-0.00%)</td><td>940.18 (-6.63%)</td><td>859.45 (-19.51%)</td><td>849.90 (+6.87%)</td><td>126.17 (-14.96%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.32 (n/a)</td><td>3.84 (n/a)</td><td>4.07 (n/a)</td><td>3.03 (n/a)</td><td>0.57 (n/a)</td><td>2658.20 (n/a)</td><td>2139.66 (n/a)</td><td>1979.90 (n/a)</td><td>1867.50 (n/a)</td><td>343.45 (n/a)</td><td>1131.96 (n/a)</td><td>1006.96 (n/a)</td><td>1067.71 (n/a)</td><td>795.26 (n/a)</td><td>148.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.51 <b>(+38.86%)</b></td><td>0.42 <b>(+30.64%)</b></td><td>0.44 <b>(+31.59%)</b></td><td>0.31 (+11.11%)</td><td>0.09 <b>(+166.53%)</b></td><td>4078.90 (-10.00%)</td><td>3056.84 <b>(-21.18%)</b></td><td>2851.40 <b>(-24.01%)</b></td><td>2454.60 <b>(-27.98%)</b></td><td>691.84 <b>(+66.89%)</b></td><td>27.34 <b>(+38.86%)</b></td><td>22.80 <b>(+30.64%)</b></td><td>23.54 <b>(+31.59%)</b></td><td>16.45 (+11.11%)</td><td>4.74 <b>(+166.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.03 (n/a)</td><td>4532.00 (n/a)</td><td>3878.12 (n/a)</td><td>3752.20 (n/a)</td><td>3408.40 (n/a)</td><td>414.54 (n/a)</td><td>19.69 (n/a)</td><td>17.46 (n/a)</td><td>17.89 (n/a)</td><td>14.81 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.50 <b>(+52.23%)</b></td><td>4.59 <b>(+23.90%)</b></td><td>4.72 <b>(+28.63%)</b></td><td>3.31 (-1.25%)</td><td>1.25 <b>(+238.85%)</b></td><td>2006.90 (+1.27%)</td><td>1530.24 (-15.35%)</td><td>1407.90 <b>(-22.26%)</b></td><td>1022.90 <b>(-34.31%)</b></td><td>387.50 <b>(+126.69%)</b></td><td>2009.20 <b>(+52.23%)</b></td><td>1419.25 <b>(+23.90%)</b></td><td>1459.77 <b>(+28.63%)</b></td><td>1024.07 (-1.25%)</td><td>384.75 <b>(+238.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.27 (n/a)</td><td>3.71 (n/a)</td><td>3.67 (n/a)</td><td>3.36 (n/a)</td><td>0.37 (n/a)</td><td>1981.70 (n/a)</td><td>1807.66 (n/a)</td><td>1811.00 (n/a)</td><td>1557.20 (n/a)</td><td>170.94 (n/a)</td><td>1319.84 (n/a)</td><td>1145.50 (n/a)</td><td>1134.82 (n/a)</td><td>1037.07 (n/a)</td><td>113.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>13.27 (n/a)</td><td>12.59 (n/a)</td><td>12.61 (n/a)</td><td>11.39 (n/a)</td><td>0.77 (n/a)</td><td>13.26 (n/a)</td><td>12.58 (n/a)</td><td>12.60 (n/a)</td><td>11.38 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>25.09 (+0.81%)</td><td>24.36 (+0.58%)</td><td>24.34 (-1.23%)</td><td>23.85 (+6.16%)</td><td>0.49 <b>(-51.58%)</b></td><td>25.07 (+0.81%)</td><td>24.35 (+0.58%)</td><td>24.32 (-1.23%)</td><td>23.84 (+6.16%)</td><td>0.49 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>24.89 (n/a)</td><td>24.22 (n/a)</td><td>24.64 (n/a)</td><td>22.47 (n/a)</td><td>1.01 (n/a)</td><td>24.87 (n/a)</td><td>24.21 (n/a)</td><td>24.63 (n/a)</td><td>22.45 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>42.54 (+2.21%)</td><td>40.47 (-0.03%)</td><td>40.08 (+0.23%)</td><td>39.65 (+0.32%)</td><td>1.18 <b>(+21.44%)</b></td><td>42.52 (+2.21%)</td><td>40.45 (-0.03%)</td><td>40.05 (+0.23%)</td><td>39.62 (+0.32%)</td><td>1.18 <b>(+21.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>41.62 (n/a)</td><td>40.48 (n/a)</td><td>39.99 (n/a)</td><td>39.52 (n/a)</td><td>0.97 (n/a)</td><td>41.60 (n/a)</td><td>40.46 (n/a)</td><td>39.96 (n/a)</td><td>39.50 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>47.48 (+7.70%)</td><td>44.95 (+7.54%)</td><td>44.93 (+7.61%)</td><td>42.88 (+7.90%)</td><td>1.86 (+12.42%)</td><td>47.45 (+7.70%)</td><td>44.92 (+7.54%)</td><td>44.90 (+7.61%)</td><td>42.86 (+7.90%)</td><td>1.86 (+12.42%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>44.08 (n/a)</td><td>41.80 (n/a)</td><td>41.75 (n/a)</td><td>39.74 (n/a)</td><td>1.66 (n/a)</td><td>44.05 (n/a)</td><td>41.77 (n/a)</td><td>41.73 (n/a)</td><td>39.72 (n/a)</td><td>1.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>13.25 (n/a)</td><td>12.70 (n/a)</td><td>12.99 (n/a)</td><td>11.79 (n/a)</td><td>0.63 (n/a)</td><td>13.24 (n/a)</td><td>12.69 (n/a)</td><td>12.98 (n/a)</td><td>11.78 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>25.02 (+2.43%)</td><td>24.41 (+3.89%)</td><td>24.25 (+5.27%)</td><td>24.18 (+6.15%)</td><td>0.35 <b>(-56.48%)</b></td><td>25.00 (+2.43%)</td><td>24.40 (+3.89%)</td><td>24.24 (+5.27%)</td><td>24.17 (+6.15%)</td><td>0.35 <b>(-56.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>24.42 (n/a)</td><td>23.50 (n/a)</td><td>23.04 (n/a)</td><td>22.78 (n/a)</td><td>0.80 (n/a)</td><td>24.41 (n/a)</td><td>23.49 (n/a)</td><td>23.02 (n/a)</td><td>22.77 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>42.13 (+1.11%)</td><td>39.14 (-0.13%)</td><td>40.93 (+5.15%)</td><td>31.22 (-13.65%)</td><td>4.48 <b>(+107.35%)</b></td><td>42.10 (+1.11%)</td><td>39.11 (-0.13%)</td><td>40.90 (+5.15%)</td><td>31.20 (-13.65%)</td><td>4.48 <b>(+107.35%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>41.66 (n/a)</td><td>39.19 (n/a)</td><td>38.92 (n/a)</td><td>36.15 (n/a)</td><td>2.16 (n/a)</td><td>41.64 (n/a)</td><td>39.16 (n/a)</td><td>38.90 (n/a)</td><td>36.13 (n/a)</td><td>2.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>45.40 (-1.87%)</td><td>43.20 (+3.40%)</td><td>42.47 (+0.77%)</td><td>41.67 (+7.06%)</td><td>1.62 <b>(-45.86%)</b></td><td>45.37 (-1.87%)</td><td>43.18 (+3.40%)</td><td>42.45 (+0.77%)</td><td>41.65 (+7.06%)</td><td>1.62 <b>(-45.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>46.26 (n/a)</td><td>41.78 (n/a)</td><td>42.15 (n/a)</td><td>38.92 (n/a)</td><td>2.99 (n/a)</td><td>46.23 (n/a)</td><td>41.76 (n/a)</td><td>42.12 (n/a)</td><td>38.90 (n/a)</td><td>2.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>8.82 (-10.89%)</td><td>8.70 (-4.99%)</td><td>8.70 (-3.52%)</td><td>8.57 (-1.65%)</td><td>0.10 <b>(-78.63%)</b></td><td>8.80 (-10.89%)</td><td>8.68 (-4.99%)</td><td>8.68 (-3.52%)</td><td>8.56 (-1.65%)</td><td>0.10 <b>(-78.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>9.90 (n/a)</td><td>9.15 (n/a)</td><td>9.02 (n/a)</td><td>8.72 (n/a)</td><td>0.45 (n/a)</td><td>9.88 (n/a)</td><td>9.13 (n/a)</td><td>9.00 (n/a)</td><td>8.70 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.94 (-1.98%)</td><td>0.88 (-3.58%)</td><td>0.92 (+1.41%)</td><td>0.78 (-12.25%)</td><td>0.07 <b>(+136.98%)</b></td><td>0.92 (-1.98%)</td><td>0.87 (-3.58%)</td><td>0.90 (+1.41%)</td><td>0.77 (-12.25%)</td><td>0.06 <b>(+136.98%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.96 (n/a)</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.03 (n/a)</td><td>0.94 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.45 (+5.96%)</td><td>1.27 (+1.31%)</td><td>1.25 (-2.33%)</td><td>1.11 (+3.14%)</td><td>0.13 (+10.14%)</td><td>1.43 (+5.96%)</td><td>1.25 (+1.31%)</td><td>1.23 (-2.33%)</td><td>1.10 (+3.14%)</td><td>0.13 (+10.14%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.36 (n/a)</td><td>1.25 (n/a)</td><td>1.28 (n/a)</td><td>1.08 (n/a)</td><td>0.12 (n/a)</td><td>1.35 (n/a)</td><td>1.24 (n/a)</td><td>1.26 (n/a)</td><td>1.07 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>18.15 (-2.02%)</td><td>17.08 (-0.55%)</td><td>17.41 (+1.03%)</td><td>15.23 (-3.66%)</td><td>1.11 (+4.98%)</td><td>17.94 (-2.02%)</td><td>16.88 (-0.55%)</td><td>17.21 (+1.03%)</td><td>15.05 (-3.66%)</td><td>1.09 (+4.98%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>18.53 (n/a)</td><td>17.18 (n/a)</td><td>17.23 (n/a)</td><td>15.81 (n/a)</td><td>1.05 (n/a)</td><td>18.31 (n/a)</td><td>16.98 (n/a)</td><td>17.03 (n/a)</td><td>15.62 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>14.05 (-0.66%)</td><td>13.58 (+7.39%)</td><td>13.62 (-1.09%)</td><td>13.04 <b>(+57.64%)</b></td><td>0.36 <b>(-85.22%)</b></td><td>13.80 (-0.66%)</td><td>13.34 (+7.39%)</td><td>13.38 (-1.09%)</td><td>12.81 <b>(+57.64%)</b></td><td>0.36 <b>(-85.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>14.14 (n/a)</td><td>12.64 (n/a)</td><td>13.77 (n/a)</td><td>8.27 (n/a)</td><td>2.47 (n/a)</td><td>13.89 (n/a)</td><td>12.42 (n/a)</td><td>13.52 (n/a)</td><td>8.13 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>9.10 (-11.22%)</td><td>8.04 (-8.01%)</td><td>8.05 (-8.45%)</td><td>6.99 (-8.23%)</td><td>0.75 <b>(-29.35%)</b></td><td>8.94 (-11.22%)</td><td>7.90 (-8.01%)</td><td>7.91 (-8.45%)</td><td>6.87 (-8.23%)</td><td>0.74 <b>(-29.35%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>10.25 (n/a)</td><td>8.74 (n/a)</td><td>8.79 (n/a)</td><td>7.62 (n/a)</td><td>1.06 (n/a)</td><td>10.07 (n/a)</td><td>8.58 (n/a)</td><td>8.64 (n/a)</td><td>7.49 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>6.07 (-4.38%)</td><td>5.64 (+3.79%)</td><td>5.43 (-0.98%)</td><td>5.41 (+19.98%)</td><td>0.30 <b>(-55.49%)</b></td><td>5.97 (-4.38%)</td><td>5.55 (+3.79%)</td><td>5.34 (-0.98%)</td><td>5.33 (+19.98%)</td><td>0.30 <b>(-55.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>6.35 (n/a)</td><td>5.43 (n/a)</td><td>5.49 (n/a)</td><td>4.51 (n/a)</td><td>0.68 (n/a)</td><td>6.24 (n/a)</td><td>5.35 (n/a)</td><td>5.40 (n/a)</td><td>4.44 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>13.52 (n/a)</td><td>11.76 (n/a)</td><td>11.61 (n/a)</td><td>10.79 (n/a)</td><td>1.05 (n/a)</td><td>13.51 (n/a)</td><td>11.75 (n/a)</td><td>11.60 (n/a)</td><td>10.78 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>13.31 (n/a)</td><td>12.99 (n/a)</td><td>13.23 (n/a)</td><td>12.43 (n/a)</td><td>0.39 (n/a)</td><td>13.30 (n/a)</td><td>12.98 (n/a)</td><td>13.22 (n/a)</td><td>12.43 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.50 (n/a)</td><td>175.76 (n/a)</td><td>179.80 (n/a)</td><td>132.90 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>199.50 (n/a)</td><td>138.52 (n/a)</td><td>136.40 (n/a)</td><td>82.20 (n/a)</td><td>41.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>160.48 (n/a)</td><td>152.60 (n/a)</td><td>137.80 (n/a)</td><td>20.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>209.00 (n/a)</td><td>178.48 (n/a)</td><td>172.40 (n/a)</td><td>162.30 (n/a)</td><td>17.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.00 (n/a)</td><td>169.94 (n/a)</td><td>171.50 (n/a)</td><td>133.40 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>266.50 (n/a)</td><td>197.18 (n/a)</td><td>183.70 (n/a)</td><td>152.30 (n/a)</td><td>43.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.10 (n/a)</td><td>174.74 (n/a)</td><td>171.10 (n/a)</td><td>153.50 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.10 (n/a)</td><td>228.12 (n/a)</td><td>206.50 (n/a)</td><td>197.70 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (-6.25%)</td><td>0.05 (-3.15%)</td><td>0.05 (-0.54%)</td><td>0.04 (+13.00%)</td><td>0.01 <b>(-21.00%)</b></td><td>210.10 (-11.50%)</td><td>170.82 (+0.60%)</td><td>180.10 (+0.56%)</td><td>119.80 (+6.68%)</td><td>36.36 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>237.40 (n/a)</td><td>169.80 (n/a)</td><td>179.10 (n/a)</td><td>112.30 (n/a)</td><td>48.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+11.48%)</td><td>0.05 (+5.95%)</td><td>0.05 (+5.35%)</td><td>0.04 (-0.51%)</td><td>0.01 <b>(+59.70%)</b></td><td>190.70 (+0.47%)</td><td>167.44 (-5.08%)</td><td>170.70 (-5.06%)</td><td>141.30 (-10.29%)</td><td>18.77 <b>(+42.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.80 (n/a)</td><td>176.40 (n/a)</td><td>179.80 (n/a)</td><td>157.50 (n/a)</td><td>13.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 <b>(+48.61%)</b></td><td>0.05 <b>(+22.39%)</b></td><td>0.05 <b>(+22.98%)</b></td><td>0.03 (-10.41%)</td><td>0.01 <b>(+363.85%)</b></td><td>241.50 (+11.65%)</td><td>171.94 (-12.63%)</td><td>157.20 (-18.72%)</td><td>119.40 <b>(-32.69%)</b></td><td>52.18 <b>(+248.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>196.80 (n/a)</td><td>193.40 (n/a)</td><td>177.40 (n/a)</td><td>14.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 (+14.03%)</td><td>0.05 <b>(+22.02%)</b></td><td>0.06 <b>(+28.16%)</b></td><td>0.03 <b>(+61.16%)</b></td><td>0.02 (-6.03%)</td><td>239.10 <b>(-37.96%)</b></td><td>162.96 <b>(-23.99%)</b></td><td>140.70 <b>(-21.96%)</b></td><td>106.60 (-12.34%)</td><td>51.63 <b>(-49.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>385.40 (n/a)</td><td>214.38 (n/a)</td><td>180.30 (n/a)</td><td>121.60 (n/a)</td><td>103.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 <b>(+37.47%)</b></td><td>0.06 <b>(+26.66%)</b></td><td>0.05 <b>(+22.58%)</b></td><td>0.04 <b>(+28.86%)</b></td><td>0.01 <b>(+47.41%)</b></td><td>189.70 <b>(-22.41%)</b></td><td>151.00 <b>(-20.66%)</b></td><td>156.30 (-18.42%)</td><td>109.50 <b>(-27.24%)</b></td><td>28.94 (-19.05%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.50 (n/a)</td><td>190.32 (n/a)</td><td>191.60 (n/a)</td><td>150.50 (n/a)</td><td>35.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 <b>(+39.76%)</b></td><td>0.05 <b>(+34.15%)</b></td><td>0.05 <b>(+26.71%)</b></td><td>0.04 <b>(+60.51%)</b></td><td>0.01 (+14.57%)</td><td>183.70 <b>(-37.69%)</b></td><td>156.56 <b>(-26.59%)</b></td><td>159.40 <b>(-21.09%)</b></td><td>120.80 <b>(-28.44%)</b></td><td>22.62 <b>(-52.75%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>294.80 (n/a)</td><td>213.28 (n/a)</td><td>202.00 (n/a)</td><td>168.80 (n/a)</td><td>47.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.08 <b>(+21.20%)</b></td><td>0.06 <b>(+28.40%)</b></td><td>0.06 <b>(+24.64%)</b></td><td>0.05 <b>(+59.28%)</b></td><td>0.01 (-17.16%)</td><td>155.10 <b>(-37.21%)</b></td><td>138.30 <b>(-24.30%)</b></td><td>137.50 (-19.78%)</td><td>108.90 (-17.50%)</td><td>18.41 <b>(-57.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>182.70 (n/a)</td><td>171.40 (n/a)</td><td>132.00 (n/a)</td><td>43.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+18.20%)</td><td>0.05 <b>(+25.97%)</b></td><td>0.05 <b>(+23.76%)</b></td><td>0.05 <b>(+61.92%)</b></td><td>0.01 <b>(-33.11%)</b></td><td>173.00 <b>(-38.24%)</b></td><td>157.20 <b>(-22.73%)</b></td><td>155.50 (-19.22%)</td><td>134.90 (-15.42%)</td><td>15.59 <b>(-65.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.10 (n/a)</td><td>203.44 (n/a)</td><td>192.50 (n/a)</td><td>159.50 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+10.20%)</td><td>0.05 (+9.01%)</td><td>0.05 (+10.58%)</td><td>0.04 (+7.89%)</td><td>0.01 (-5.26%)</td><td>190.30 (-7.31%)</td><td>165.90 (-8.50%)</td><td>161.10 (-9.55%)</td><td>144.90 (-9.27%)</td><td>16.96 (-19.94%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>181.32 (n/a)</td><td>178.10 (n/a)</td><td>159.70 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (-9.92%)</td><td>0.04 (-7.13%)</td><td>0.03 (-1.20%)</td><td>0.03 (-15.98%)</td><td>0.01 (-9.79%)</td><td>287.80 (+19.02%)</td><td>231.92 (+7.84%)</td><td>234.50 (+1.21%)</td><td>180.90 (+11.05%)</td><td>38.37 <b>(+20.11%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.80 (n/a)</td><td>215.06 (n/a)</td><td>231.70 (n/a)</td><td>162.90 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+3.58%)</td><td>0.05 (+8.41%)</td><td>0.06 <b>(+24.51%)</b></td><td>0.04 (-3.91%)</td><td>0.01 <b>(+47.00%)</b></td><td>198.50 (+4.09%)</td><td>155.36 (-5.87%)</td><td>130.30 (-19.72%)</td><td>128.30 (-3.46%)</td><td>35.51 <b>(+43.20%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.70 (n/a)</td><td>165.04 (n/a)</td><td>162.30 (n/a)</td><td>132.90 (n/a)</td><td>24.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (+11.62%)</td><td>0.04 (-0.68%)</td><td>0.04 (+3.10%)</td><td>0.03 <b>(-21.23%)</b></td><td>0.01 <b>(+232.73%)</b></td><td>292.50 <b>(+26.95%)</b></td><td>222.12 (+3.41%)</td><td>209.20 (-3.01%)</td><td>181.00 (-10.44%)</td><td>44.56 <b>(+283.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>230.40 (n/a)</td><td>214.80 (n/a)</td><td>215.70 (n/a)</td><td>202.10 (n/a)</td><td>11.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (-1.53%)</td><td>0.05 (-13.75%)</td><td>0.05 (-14.95%)</td><td>0.04 (-19.64%)</td><td>0.01 <b>(+43.50%)</b></td><td>219.20 <b>(+24.47%)</b></td><td>180.90 (+18.34%)</td><td>171.30 (+17.57%)</td><td>134.10 (+1.51%)</td><td>36.01 <b>(+84.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.10 (n/a)</td><td>152.86 (n/a)</td><td>145.70 (n/a)</td><td>132.10 (n/a)</td><td>19.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (+15.23%)</td><td>0.05 (-3.34%)</td><td>0.05 (+4.43%)</td><td>0.04 <b>(-23.23%)</b></td><td>0.01 <b>(+154.18%)</b></td><td>217.90 <b>(+30.25%)</b></td><td>167.76 (+7.97%)</td><td>156.60 (-4.28%)</td><td>120.70 (-13.23%)</td><td>41.67 <b>(+195.20%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>167.30 (n/a)</td><td>155.38 (n/a)</td><td>163.60 (n/a)</td><td>139.10 (n/a)</td><td>14.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 <b>(-29.37%)</b></td><td>0.04 <b>(-22.96%)</b></td><td>0.04 (-14.25%)</td><td>0.02 <b>(-44.65%)</b></td><td>0.01 (+7.04%)</td><td>352.60 <b>(+80.64%)</b></td><td>227.76 <b>(+34.91%)</b></td><td>195.60 (+16.64%)</td><td>184.30 <b>(+41.55%)</b></td><td>70.86 <b>(+186.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.20 (n/a)</td><td>168.82 (n/a)</td><td>167.70 (n/a)</td><td>130.20 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (-0.63%)</td><td>0.05 (-3.75%)</td><td>0.05 (-4.03%)</td><td>0.04 (+8.68%)</td><td>0.01 <b>(-24.32%)</b></td><td>196.50 (-8.01%)</td><td>166.80 (+2.65%)</td><td>164.50 (+4.25%)</td><td>137.10 (+0.59%)</td><td>21.33 <b>(-31.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>162.50 (n/a)</td><td>157.80 (n/a)</td><td>136.30 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (-5.67%)</td><td>0.05 (+6.41%)</td><td>0.05 (+15.31%)</td><td>0.04 (+2.70%)</td><td>0.01 <b>(-28.44%)</b></td><td>212.30 (-2.61%)</td><td>171.46 (-7.20%)</td><td>166.30 (-13.30%)</td><td>144.60 (+6.01%)</td><td>24.80 <b>(-23.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.00 (n/a)</td><td>184.76 (n/a)</td><td>191.80 (n/a)</td><td>136.40 (n/a)</td><td>32.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (-11.87%)</td><td>0.05 (-4.21%)</td><td>0.05 (-1.85%)</td><td>0.04 (-7.52%)</td><td>0.01 (-17.84%)</td><td>221.60 (+8.15%)</td><td>179.00 (+4.15%)</td><td>168.60 (+1.87%)</td><td>167.20 (+13.51%)</td><td>23.83 (+1.19%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.90 (n/a)</td><td>171.86 (n/a)</td><td>165.50 (n/a)</td><td>147.30 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.18 (-0.21%)</td><td>0.18 (-0.20%)</td><td>0.18 (-0.06%)</td><td>0.18 (-0.31%)</td><td>0.00 <b>(+36.85%)</b></td><td>47691.70 (+0.31%)</td><td>47589.30 (+0.20%)</td><td>47559.70 (+0.06%)</td><td>47514.70 (+0.21%)</td><td>83.18 <b>(+37.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47542.10 (n/a)</td><td>47493.50 (n/a)</td><td>47530.70 (n/a)</td><td>47415.30 (n/a)</td><td>60.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.20 (+14.87%)</td><td>0.16 (+10.21%)</td><td>0.19 <b>(+28.90%)</b></td><td>0.11 <b>(-21.77%)</b></td><td>0.04 <b>(+170.02%)</b></td><td>231.60 <b>(+27.81%)</b></td><td>160.18 (-4.14%)</td><td>132.30 <b>(-22.45%)</b></td><td>123.50 (-12.97%)</td><td>47.96 <b>(+190.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>181.20 (n/a)</td><td>167.10 (n/a)</td><td>170.60 (n/a)</td><td>141.90 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.32 (+4.18%)</td><td>0.25 (-6.36%)</td><td>0.25 (-10.20%)</td><td>0.18 <b>(-20.82%)</b></td><td>0.05 <b>(+45.56%)</b></td><td>225.60 <b>(+26.32%)</b></td><td>167.42 (+8.95%)</td><td>163.60 (+11.37%)</td><td>129.40 (-4.01%)</td><td>35.70 <b>(+81.46%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>153.66 (n/a)</td><td>146.90 (n/a)</td><td>134.80 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (+12.06%)</td><td>0.03 (-0.57%)</td><td>0.03 (-6.88%)</td><td>0.03 (+9.58%)</td><td>0.01 (+18.36%)</td><td>197.10 (-8.75%)</td><td>168.66 (+0.82%)</td><td>175.40 (+7.41%)</td><td>119.90 (-10.72%)</td><td>29.02 (-8.39%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>167.28 (n/a)</td><td>163.30 (n/a)</td><td>134.30 (n/a)</td><td>31.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+11.33%)</td><td>0.04 (-7.00%)</td><td>0.05 (-3.55%)</td><td>0.03 <b>(-31.01%)</b></td><td>0.01 <b>(+303.33%)</b></td><td>257.00 <b>(+44.95%)</b></td><td>192.60 (+12.13%)</td><td>181.60 (+3.65%)</td><td>140.60 (-10.16%)</td><td>45.74 <b>(+432.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>171.76 (n/a)</td><td>175.20 (n/a)</td><td>156.50 (n/a)</td><td>8.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 (+7.40%)</td><td>0.08 <b>(+22.11%)</b></td><td>0.09 <b>(+40.78%)</b></td><td>0.07 <b>(+33.19%)</b></td><td>0.01 <b>(-28.09%)</b></td><td>169.80 <b>(-24.93%)</b></td><td>149.08 (-19.63%)</td><td>138.80 <b>(-28.97%)</b></td><td>133.50 (-6.90%)</td><td>17.94 <b>(-48.64%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>185.50 (n/a)</td><td>195.40 (n/a)</td><td>143.40 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+10.55%)</td><td>0.05 (+6.08%)</td><td>0.05 (+3.76%)</td><td>0.04 (+12.70%)</td><td>0.01 (+13.18%)</td><td>182.10 (-11.26%)</td><td>163.48 (-5.73%)</td><td>165.90 (-3.66%)</td><td>133.30 (-9.57%)</td><td>18.14 (-12.24%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>173.42 (n/a)</td><td>172.20 (n/a)</td><td>147.40 (n/a)</td><td>20.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (+4.06%)</td><td>0.06 (+8.05%)</td><td>0.06 (+4.71%)</td><td>0.05 (+16.80%)</td><td>0.01 <b>(-22.46%)</b></td><td>192.70 (-14.36%)</td><td>167.64 (-8.83%)</td><td>177.40 (-4.47%)</td><td>136.80 (-3.93%)</td><td>22.15 <b>(-36.57%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>183.88 (n/a)</td><td>185.70 (n/a)</td><td>142.40 (n/a)</td><td>34.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 <b>(-23.45%)</b></td><td>0.04 (-0.75%)</td><td>0.05 (+2.07%)</td><td>0.04 (+19.94%)</td><td>0.00 <b>(-62.06%)</b></td><td>207.80 (-16.65%)</td><td>185.08 (-3.92%)</td><td>180.80 (-2.06%)</td><td>165.00 <b>(+30.64%)</b></td><td>20.06 <b>(-58.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.30 (n/a)</td><td>192.64 (n/a)</td><td>184.60 (n/a)</td><td>126.30 (n/a)</td><td>48.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.07 (-7.30%)</td><td>0.05 (-6.36%)</td><td>0.06 (+11.68%)</td><td>0.04 (-16.55%)</td><td>0.01 (+14.91%)</td><td>286.00 (+19.87%)</td><td>205.08 (+9.52%)</td><td>170.20 (-10.42%)</td><td>152.30 (+7.86%)</td><td>58.43 <b>(+51.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>238.60 (n/a)</td><td>187.26 (n/a)</td><td>190.00 (n/a)</td><td>141.20 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 <b>(-28.97%)</b></td><td>0.05 (-8.35%)</td><td>0.05 (+13.89%)</td><td>0.04 (+3.23%)</td><td>0.00 <b>(-75.16%)</b></td><td>206.70 (-3.14%)</td><td>181.28 (+3.75%)</td><td>176.40 (-12.24%)</td><td>169.60 <b>(+40.86%)</b></td><td>14.64 <b>(-65.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.40 (n/a)</td><td>174.72 (n/a)</td><td>201.00 (n/a)</td><td>120.40 (n/a)</td><td>42.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+9.31%)</td><td>0.05 (+16.23%)</td><td>0.06 <b>(+23.39%)</b></td><td>0.04 (+16.71%)</td><td>0.01 (+4.69%)</td><td>219.20 (-14.34%)</td><td>177.26 (-14.20%)</td><td>166.80 (-18.95%)</td><td>149.50 (-8.51%)</td><td>28.30 (-17.54%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>255.90 (n/a)</td><td>206.60 (n/a)</td><td>205.80 (n/a)</td><td>163.40 (n/a)</td><td>34.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (-11.83%)</td><td>0.04 (-5.71%)</td><td>0.04 (-2.24%)</td><td>0.03 (-14.46%)</td><td>0.01 (-10.85%)</td><td>279.30 (+16.91%)</td><td>207.04 (+6.29%)</td><td>210.40 (+2.28%)</td><td>158.00 (+13.42%)</td><td>46.79 <b>(+20.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>194.78 (n/a)</td><td>205.70 (n/a)</td><td>139.30 (n/a)</td><td>38.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.09 <b>(+33.30%)</b></td><td>0.06 (+19.95%)</td><td>0.05 (+5.11%)</td><td>0.05 <b>(+49.88%)</b></td><td>0.02 <b>(+31.39%)</b></td><td>201.60 <b>(-33.27%)</b></td><td>166.52 (-17.63%)</td><td>176.40 (-4.85%)</td><td>104.60 <b>(-24.96%)</b></td><td>36.48 <b>(-40.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>302.10 (n/a)</td><td>202.16 (n/a)</td><td>185.40 (n/a)</td><td>139.40 (n/a)</td><td>61.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (-12.42%)</td><td>0.05 (+13.28%)</td><td>0.05 <b>(+25.87%)</b></td><td>0.05 (+18.63%)</td><td>0.00 <b>(-56.59%)</b></td><td>181.10 (-15.69%)</td><td>161.98 (-14.46%)</td><td>159.00 <b>(-20.54%)</b></td><td>144.50 (+14.14%)</td><td>15.62 <b>(-57.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.80 (n/a)</td><td>189.36 (n/a)</td><td>200.10 (n/a)</td><td>126.60 (n/a)</td><td>36.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (+19.90%)</td><td>0.05 <b>(+20.10%)</b></td><td>0.05 (+15.42%)</td><td>0.04 <b>(+39.98%)</b></td><td>0.00 <b>(-28.81%)</b></td><td>193.60 <b>(-28.56%)</b></td><td>184.72 (-17.41%)</td><td>188.70 (-13.36%)</td><td>164.40 (-16.59%)</td><td>11.59 <b>(-59.05%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>271.00 (n/a)</td><td>223.66 (n/a)</td><td>217.80 (n/a)</td><td>197.10 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.06 (+6.58%)</td><td>0.05 (+7.31%)</td><td>0.05 (+11.60%)</td><td>0.04 (+8.35%)</td><td>0.01 (-7.95%)</td><td>202.30 (-7.71%)</td><td>168.76 (-7.36%)</td><td>170.10 (-10.38%)</td><td>137.30 (-6.15%)</td><td>24.79 (-19.28%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>182.16 (n/a)</td><td>189.80 (n/a)</td><td>146.30 (n/a)</td><td>30.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.05 (+3.33%)</td><td>0.04 (+9.04%)</td><td>0.04 (+0.69%)</td><td>0.04 <b>(+44.27%)</b></td><td>0.00 <b>(-57.93%)</b></td><td>227.70 <b>(-30.71%)</b></td><td>204.38 (-11.52%)</td><td>203.00 (-0.68%)</td><td>182.90 (-3.23%)</td><td>15.94 <b>(-72.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>328.60 (n/a)</td><td>230.98 (n/a)</td><td>204.40 (n/a)</td><td>189.00 (n/a)</td><td>57.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.04 (-6.79%)</td><td>0.04 (-3.95%)</td><td>0.04 (-1.62%)</td><td>0.03 (-10.20%)</td><td>0.00 <b>(+22.93%)</b></td><td>261.30 (+11.38%)</td><td>228.94 (+4.39%)</td><td>223.50 (+1.64%)</td><td>211.90 (+7.29%)</td><td>20.25 <b>(+48.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.60 (n/a)</td><td>219.32 (n/a)</td><td>219.90 (n/a)</td><td>197.50 (n/a)</td><td>13.61 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.81 <b>(+20.22%)</b></td><td>0.52 (-8.41%)</td><td>0.53 (-5.65%)</td><td>0.29 <b>(-40.47%)</b></td><td>0.19 <b>(+158.32%)</b></td><td>343.20 <b>(+67.99%)</b></td><td>209.70 <b>(+20.54%)</b></td><td>184.60 (+6.03%)</td><td>121.50 (-16.78%)</td><td>82.31 <b>(+270.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.67 (n/a)</td><td>0.57 (n/a)</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.07 (n/a)</td><td>204.30 (n/a)</td><td>173.96 (n/a)</td><td>174.10 (n/a)</td><td>146.00 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.75 (-10.11%)</td><td>0.67 (+14.89%)</td><td>0.71 <b>(+47.53%)</b></td><td>0.54 (+11.42%)</td><td>0.10 <b>(-37.76%)</b></td><td>183.20 (-10.24%)</td><td>150.26 (-15.44%)</td><td>137.50 <b>(-32.23%)</b></td><td>130.60 (+11.24%)</td><td>23.27 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.84 (n/a)</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.48 (n/a)</td><td>0.15 (n/a)</td><td>204.10 (n/a)</td><td>177.70 (n/a)</td><td>202.90 (n/a)</td><td>117.40 (n/a)</td><td>38.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.79 (+9.33%)</td><td>0.64 (+7.82%)</td><td>0.59 (-2.79%)</td><td>0.50 (+8.41%)</td><td>0.13 <b>(+34.57%)</b></td><td>195.40 (-7.74%)</td><td>159.56 (-6.21%)</td><td>166.40 (+2.91%)</td><td>124.00 (-8.49%)</td><td>32.15 (+10.27%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.73 (n/a)</td><td>0.59 (n/a)</td><td>0.61 (n/a)</td><td>0.46 (n/a)</td><td>0.10 (n/a)</td><td>211.80 (n/a)</td><td>170.12 (n/a)</td><td>161.70 (n/a)</td><td>135.50 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.64 (-8.56%)</td><td>0.52 (+10.07%)</td><td>0.54 <b>(+36.02%)</b></td><td>0.37 (+13.98%)</td><td>0.10 <b>(-36.38%)</b></td><td>265.40 (-12.26%)</td><td>195.20 (-13.34%)</td><td>183.30 <b>(-26.47%)</b></td><td>153.10 (+9.36%)</td><td>42.66 <b>(-36.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.70 (n/a)</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>302.50 (n/a)</td><td>225.24 (n/a)</td><td>249.30 (n/a)</td><td>140.00 (n/a)</td><td>66.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.56 (+16.40%)</td><td>0.48 (+14.61%)</td><td>0.52 <b>(+24.32%)</b></td><td>0.36 (+10.05%)</td><td>0.08 <b>(+37.68%)</b></td><td>202.50 (-9.15%)</td><td>157.98 (-12.02%)</td><td>142.70 (-19.51%)</td><td>132.50 (-14.13%)</td><td>29.48 (+7.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>222.90 (n/a)</td><td>179.56 (n/a)</td><td>177.30 (n/a)</td><td>154.30 (n/a)</td><td>27.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.67 <b>(+23.14%)</b></td><td>0.48 (+8.96%)</td><td>0.45 (+10.06%)</td><td>0.34 (-10.87%)</td><td>0.14 <b>(+110.14%)</b></td><td>213.90 (+12.22%)</td><td>164.12 (-3.82%)</td><td>162.90 (-9.15%)</td><td>110.60 (-18.74%)</td><td>44.38 <b>(+94.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.06 (n/a)</td><td>190.60 (n/a)</td><td>170.64 (n/a)</td><td>179.30 (n/a)</td><td>136.10 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.53 (+8.54%)</td><td>0.43 (+14.55%)</td><td>0.43 (+18.61%)</td><td>0.31 (+2.37%)</td><td>0.09 <b>(+30.41%)</b></td><td>241.10 (-2.31%)</td><td>176.74 (-11.51%)</td><td>169.70 (-15.70%)</td><td>139.60 (-7.85%)</td><td>41.83 (+15.95%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.07 (n/a)</td><td>246.80 (n/a)</td><td>199.72 (n/a)</td><td>201.30 (n/a)</td><td>151.50 (n/a)</td><td>36.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.46 <b>(-21.88%)</b></td><td>0.39 (-0.21%)</td><td>0.40 (+17.03%)</td><td>0.32 <b>(+30.65%)</b></td><td>0.06 <b>(-57.00%)</b></td><td>228.50 <b>(-23.45%)</b></td><td>193.46 (-6.44%)</td><td>186.50 (-14.57%)</td><td>161.30 <b>(+28.02%)</b></td><td>28.44 <b>(-56.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.59 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.13 (n/a)</td><td>298.50 (n/a)</td><td>206.78 (n/a)</td><td>218.30 (n/a)</td><td>126.00 (n/a)</td><td>65.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.03 (+9.77%)</td><td>0.87 <b>(+21.14%)</b></td><td>0.80 (+16.39%)</td><td>0.73 (+20.00%)</td><td>0.15 (+15.61%)</td><td>179.50 (-16.67%)</td><td>154.08 (-17.39%)</td><td>163.10 (-14.07%)</td><td>127.20 (-8.88%)</td><td>25.09 (-11.23%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.94 (n/a)</td><td>0.72 (n/a)</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.13 (n/a)</td><td>215.40 (n/a)</td><td>186.52 (n/a)</td><td>189.80 (n/a)</td><td>139.60 (n/a)</td><td>28.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.08 (-7.67%)</td><td>0.76 (-3.38%)</td><td>0.69 (-3.65%)</td><td>0.43 <b>(-22.40%)</b></td><td>0.25 (+5.06%)</td><td>304.10 <b>(+28.86%)</b></td><td>191.02 (+7.09%)</td><td>190.40 (+3.82%)</td><td>121.60 (+8.38%)</td><td>71.05 <b>(+49.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.17 (n/a)</td><td>0.78 (n/a)</td><td>0.71 (n/a)</td><td>0.56 (n/a)</td><td>0.24 (n/a)</td><td>236.00 (n/a)</td><td>178.38 (n/a)</td><td>183.40 (n/a)</td><td>112.20 (n/a)</td><td>47.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.84 (-8.01%)</td><td>0.76 (-3.91%)</td><td>0.80 (-2.33%)</td><td>0.65 (+6.51%)</td><td>0.08 <b>(-28.40%)</b></td><td>200.30 (-6.09%)</td><td>174.68 (+3.19%)</td><td>163.80 (+2.38%)</td><td>156.90 (+8.73%)</td><td>19.21 <b>(-28.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.91 (n/a)</td><td>0.79 (n/a)</td><td>0.82 (n/a)</td><td>0.61 (n/a)</td><td>0.11 (n/a)</td><td>213.30 (n/a)</td><td>169.28 (n/a)</td><td>160.00 (n/a)</td><td>144.30 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (+5.85%)</td><td>0.03 (-7.09%)</td><td>0.02 (-10.93%)</td><td>0.02 (-16.38%)</td><td>0.00 <b>(+41.66%)</b></td><td>206.50 (+19.57%)</td><td>167.36 (+8.92%)</td><td>166.80 (+12.32%)</td><td>130.50 (-5.50%)</td><td>27.10 <b>(+58.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.70 (n/a)</td><td>153.66 (n/a)</td><td>148.50 (n/a)</td><td>138.10 (n/a)</td><td>17.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (-10.01%)</td><td>0.02 (-13.64%)</td><td>0.02 (-16.71%)</td><td>0.02 (+2.41%)</td><td>0.00 <b>(-31.89%)</b></td><td>230.40 (-2.37%)</td><td>186.60 (+13.56%)</td><td>183.30 <b>(+20.04%)</b></td><td>154.20 (+11.18%)</td><td>29.36 <b>(-27.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>236.00 (n/a)</td><td>164.32 (n/a)</td><td>152.70 (n/a)</td><td>138.70 (n/a)</td><td>40.64 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (+9.36%)</td><td>0.03 (+8.01%)</td><td>0.03 (+2.79%)</td><td>0.02 (+9.07%)</td><td>0.00 (+3.85%)</td><td>195.40 (-8.31%)</td><td>154.68 (-7.61%)</td><td>148.10 (-2.69%)</td><td>131.90 (-8.59%)</td><td>26.26 (-12.34%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.10 (n/a)</td><td>167.42 (n/a)</td><td>152.20 (n/a)</td><td>144.30 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.92 (-13.18%)</td><td>0.74 (-5.30%)</td><td>0.72 (-0.59%)</td><td>0.61 (-5.09%)</td><td>0.12 <b>(-32.01%)</b></td><td>216.40 (+5.36%)</td><td>181.60 (+4.02%)</td><td>182.50 (+0.61%)</td><td>143.50 (+15.17%)</td><td>27.11 (-18.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.06 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.17 (n/a)</td><td>205.40 (n/a)</td><td>174.58 (n/a)</td><td>181.40 (n/a)</td><td>124.60 (n/a)</td><td>33.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.89 (-3.45%)</td><td>0.68 (-18.85%)</td><td>0.66 (-18.40%)</td><td>0.53 <b>(-28.65%)</b></td><td>0.14 <b>(+81.39%)</b></td><td>247.80 <b>(+40.16%)</b></td><td>200.50 <b>(+26.56%)</b></td><td>201.20 <b>(+22.53%)</b></td><td>147.80 (+3.57%)</td><td>39.92 <b>(+169.31%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.93 (n/a)</td><td>0.84 (n/a)</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.08 (n/a)</td><td>176.80 (n/a)</td><td>158.42 (n/a)</td><td>164.20 (n/a)</td><td>142.70 (n/a)</td><td>14.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.71 <b>(-40.30%)</b></td><td>0.64 (-14.31%)</td><td>0.68 (-1.78%)</td><td>0.53 (-2.66%)</td><td>0.07 <b>(-71.02%)</b></td><td>249.20 (+2.76%)</td><td>208.90 (+9.89%)</td><td>194.60 (+1.83%)</td><td>186.30 <b>(+67.54%)</b></td><td>26.03 <b>(-47.17%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.19 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.54 (n/a)</td><td>0.25 (n/a)</td><td>242.50 (n/a)</td><td>190.10 (n/a)</td><td>191.10 (n/a)</td><td>111.20 (n/a)</td><td>49.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>1.07 (+1.63%)</td><td>0.77 (-1.08%)</td><td>0.80 (+8.65%)</td><td>0.53 (-12.17%)</td><td>0.20 <b>(+21.65%)</b></td><td>251.00 (+13.88%)</td><td>180.84 (+3.41%)</td><td>164.80 (-7.93%)</td><td>123.30 (-1.60%)</td><td>47.94 <b>(+41.39%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.05 (n/a)</td><td>0.78 (n/a)</td><td>0.74 (n/a)</td><td>0.60 (n/a)</td><td>0.17 (n/a)</td><td>220.40 (n/a)</td><td>174.88 (n/a)</td><td>179.00 (n/a)</td><td>125.30 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.82 (-11.71%)</td><td>0.74 (-9.34%)</td><td>0.73 (-9.48%)</td><td>0.68 (-7.44%)</td><td>0.05 <b>(-29.11%)</b></td><td>193.40 (+8.04%)</td><td>180.16 (+10.03%)</td><td>180.00 (+10.50%)</td><td>161.20 (+13.28%)</td><td>12.83 (-13.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.93 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>0.08 (n/a)</td><td>179.00 (n/a)</td><td>163.74 (n/a)</td><td>162.90 (n/a)</td><td>142.30 (n/a)</td><td>14.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (+13.64%)</td><td>0.03 (+0.83%)</td><td>0.02 (-0.46%)</td><td>0.02 (-11.95%)</td><td>0.00 <b>(+140.29%)</b></td><td>203.80 (+13.60%)</td><td>164.46 (+1.52%)</td><td>163.90 (+0.49%)</td><td>129.40 (-11.97%)</td><td>30.77 <b>(+139.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.40 (n/a)</td><td>162.00 (n/a)</td><td>163.10 (n/a)</td><td>147.00 (n/a)</td><td>12.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.03 (+7.74%)</td><td>0.03 (+6.93%)</td><td>0.03 (-1.73%)</td><td>0.02 (+18.93%)</td><td>0.00 <b>(-28.95%)</b></td><td>186.50 (-15.92%)</td><td>163.08 (-7.53%)</td><td>163.00 (+1.75%)</td><td>143.80 (-7.23%)</td><td>15.90 <b>(-44.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>176.36 (n/a)</td><td>160.20 (n/a)</td><td>155.00 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.00 (-2.22%)</td><td>0.00 (-2.78%)</td><td>0.00 (-2.33%)</td><td>0.00 (-9.52%)</td><td>0.00 <b>(+87.87%)</b></td><td>1087.95 (+10.52%)</td><td>980.93 (+2.64%)</td><td>974.36 (+1.29%)</td><td>928.68 (+0.90%)</td><td>64.12 <b>(+120.58%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>984.43 (n/a)</td><td>955.67 (n/a)</td><td>961.96 (n/a)</td><td>920.43 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.01 (-1.18%)</td><td>0.01 (+0.25%)</td><td>0.01 (+1.25%)</td><td>0.01 (+1.35%)</td><td>0.00 (-13.12%)</td><td>1094.10 (-1.78%)</td><td>1021.61 (-0.59%)</td><td>1006.22 (-1.33%)</td><td>970.54 (+0.53%)</td><td>47.29 (-11.90%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1113.97 (n/a)</td><td>1027.66 (n/a)</td><td>1019.79 (n/a)</td><td>965.47 (n/a)</td><td>53.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>0.99 (-1.77%)</td><td>0.96 (-1.02%)</td><td>0.95 (-0.80%)</td><td>0.94 (-0.39%)</td><td>0.02 <b>(-23.04%)</b></td><td>2221.04 (+0.39%)</td><td>2189.27 (+1.01%)</td><td>2200.44 (+0.81%)</td><td>2121.50 (+1.80%)</td><td>39.10 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2212.39 (n/a)</td><td>2167.31 (n/a)</td><td>2182.81 (n/a)</td><td>2083.95 (n/a)</td><td>49.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>2.84 <b>(-26.52%)</b></td><td>2.63 (-19.47%)</td><td>2.64 (-16.83%)</td><td>2.37 (-15.57%)</td><td>0.17 <b>(-56.24%)</b></td><td>221.30 (+18.47%)</td><td>200.26 <b>(+23.28%)</b></td><td>198.40 <b>(+20.24%)</b></td><td>184.30 <b>(+36.12%)</b></td><td>13.31 <b>(-27.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>3.87 (n/a)</td><td>3.26 (n/a)</td><td>3.18 (n/a)</td><td>2.81 (n/a)</td><td>0.39 (n/a)</td><td>186.80 (n/a)</td><td>162.44 (n/a)</td><td>165.00 (n/a)</td><td>135.40 (n/a)</td><td>18.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>5.39 (-9.47%)</td><td>4.86 (-14.69%)</td><td>4.90 (-12.54%)</td><td>4.40 <b>(-21.23%)</b></td><td>0.45 <b>(+182.32%)</b></td><td>238.50 <b>(+26.93%)</b></td><td>217.36 (+17.98%)</td><td>214.00 (+14.38%)</td><td>194.60 (+10.44%)</td><td>20.25 <b>(+301.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>5.95 (n/a)</td><td>5.69 (n/a)</td><td>5.60 (n/a)</td><td>5.58 (n/a)</td><td>0.16 (n/a)</td><td>187.90 (n/a)</td><td>184.24 (n/a)</td><td>187.10 (n/a)</td><td>176.20 (n/a)</td><td>5.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:47:10</td><td>3.22 <b>(-22.01%)</b></td><td>2.75 (-19.74%)</td><td>2.77 (-19.87%)</td><td>2.34 (-19.27%)</td><td>0.33 <b>(-34.84%)</b></td><td>224.10 <b>(+23.88%)</b></td><td>192.66 <b>(+23.87%)</b></td><td>189.30 <b>(+24.79%)</b></td><td>162.60 <b>(+28.23%)</b></td><td>23.13 (+1.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:38:35</td><td>4.13 (n/a)</td><td>3.43 (n/a)</td><td>3.46 (n/a)</td><td>2.90 (n/a)</td><td>0.51 (n/a)</td><td>180.90 (n/a)</td><td>155.54 (n/a)</td><td>151.70 (n/a)</td><td>126.80 (n/a)</td><td>22.72 (n/a)</td>
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
