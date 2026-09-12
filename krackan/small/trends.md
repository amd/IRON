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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (-6.00%)</td><td>0.07 (-1.39%)</td><td>0.07 (+0.85%)</td><td>0.06 (+12.05%)</td><td>0.01 <b>(-31.64%)</b></td><td>206.90 (-10.74%)</td><td>182.22 (+0.11%)</td><td>179.70 (-0.88%)</td><td>154.00 (+6.35%)</td><td>20.33 <b>(-35.95%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.80 (n/a)</td><td>182.02 (n/a)</td><td>181.30 (n/a)</td><td>144.80 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.12 (-1.06%)</td><td>0.08 (+0.39%)</td><td>0.07 (-5.98%)</td><td>0.05 (+3.13%)</td><td>0.03 (-5.24%)</td><td>240.10 (-3.03%)</td><td>177.62 (-1.73%)</td><td>183.00 (+6.40%)</td><td>102.00 (+1.09%)</td><td>52.16 (-10.21%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>247.60 (n/a)</td><td>180.74 (n/a)</td><td>172.00 (n/a)</td><td>100.90 (n/a)</td><td>58.09 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 <b>(-21.70%)</b></td><td>0.07 (-2.98%)</td><td>0.07 (+17.02%)</td><td>0.05 (+14.15%)</td><td>0.01 <b>(-47.42%)</b></td><td>232.90 (-12.41%)</td><td>193.58 (-1.96%)</td><td>177.60 (-14.53%)</td><td>155.80 <b>(+27.70%)</b></td><td>35.12 <b>(-38.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>265.90 (n/a)</td><td>197.46 (n/a)</td><td>207.80 (n/a)</td><td>122.00 (n/a)</td><td>56.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (-6.60%)</td><td>0.06 (-7.46%)</td><td>0.06 (-16.80%)</td><td>0.05 (-11.57%)</td><td>0.01 (-6.49%)</td><td>246.90 (+13.10%)</td><td>200.38 (+8.06%)</td><td>208.70 <b>(+20.15%)</b></td><td>158.00 (+7.05%)</td><td>34.04 (+7.92%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.30 (n/a)</td><td>185.44 (n/a)</td><td>173.70 (n/a)</td><td>147.60 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-14.49%)</td><td>0.03 (-5.19%)</td><td>0.03 (+0.70%)</td><td>0.03 (+2.86%)</td><td>0.00 <b>(-58.28%)</b></td><td>181.10 (-2.79%)</td><td>166.02 (+3.94%)</td><td>164.20 (-0.73%)</td><td>152.50 (+16.95%)</td><td>11.26 <b>(-52.25%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>159.72 (n/a)</td><td>165.40 (n/a)</td><td>130.40 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 <b>(-20.05%)</b></td><td>0.03 <b>(-27.92%)</b></td><td>0.03 <b>(-30.67%)</b></td><td>0.03 <b>(-27.63%)</b></td><td>0.00 (+3.31%)</td><td>202.00 <b>(+38.17%)</b></td><td>180.80 <b>(+39.48%)</b></td><td>182.80 <b>(+44.16%)</b></td><td>145.60 <b>(+25.09%)</b></td><td>21.47 <b>(+74.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>146.20 (n/a)</td><td>129.62 (n/a)</td><td>126.80 (n/a)</td><td>116.40 (n/a)</td><td>12.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-6.26%)</td><td>0.03 (-12.14%)</td><td>0.03 (-6.78%)</td><td>0.02 <b>(-34.00%)</b></td><td>0.01 <b>(+136.83%)</b></td><td>294.70 <b>(+51.52%)</b></td><td>204.12 (+18.36%)</td><td>179.30 (+7.30%)</td><td>168.10 (+6.66%)</td><td>53.19 <b>(+280.40%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.50 (n/a)</td><td>172.46 (n/a)</td><td>167.10 (n/a)</td><td>157.60 (n/a)</td><td>13.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (-15.12%)</td><td>0.03 (-9.32%)</td><td>0.03 (-13.88%)</td><td>0.03 (-3.82%)</td><td>0.01 <b>(-24.30%)</b></td><td>193.70 (+3.97%)</td><td>164.88 (+9.25%)</td><td>172.10 (+16.13%)</td><td>137.30 (+17.75%)</td><td>25.75 (-10.24%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>150.92 (n/a)</td><td>148.20 (n/a)</td><td>116.60 (n/a)</td><td>28.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (-0.66%)</td><td>0.03 (-15.71%)</td><td>0.03 <b>(-25.39%)</b></td><td>0.02 <b>(-25.78%)</b></td><td>0.01 <b>(+123.07%)</b></td><td>227.30 <b>(+34.74%)</b></td><td>182.00 <b>(+22.39%)</b></td><td>196.40 <b>(+34.06%)</b></td><td>138.00 (+0.66%)</td><td>37.98 <b>(+195.83%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>168.70 (n/a)</td><td>148.70 (n/a)</td><td>146.50 (n/a)</td><td>137.10 (n/a)</td><td>12.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 <b>(+21.35%)</b></td><td>0.03 (+13.73%)</td><td>0.04 <b>(+27.58%)</b></td><td>0.03 (-0.51%)</td><td>0.01 <b>(+86.11%)</b></td><td>205.10 (+0.49%)</td><td>159.64 (-10.32%)</td><td>144.10 <b>(-21.60%)</b></td><td>129.80 (-17.59%)</td><td>32.01 <b>(+58.92%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>178.02 (n/a)</td><td>183.80 (n/a)</td><td>157.50 (n/a)</td><td>20.14 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 <b>(-33.61%)</b></td><td>0.03 <b>(-26.89%)</b></td><td>0.03 (-17.72%)</td><td>0.02 <b>(-30.57%)</b></td><td>0.00 <b>(-33.90%)</b></td><td>247.80 <b>(+43.99%)</b></td><td>201.48 <b>(+36.69%)</b></td><td>187.10 <b>(+21.57%)</b></td><td>177.20 <b>(+50.55%)</b></td><td>29.52 <b>(+45.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>147.40 (n/a)</td><td>153.90 (n/a)</td><td>117.70 (n/a)</td><td>20.29 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-13.42%)</td><td>0.02 (-10.64%)</td><td>0.02 (-12.18%)</td><td>0.02 (+7.11%)</td><td>0.00 <b>(-53.00%)</b></td><td>240.90 (-6.63%)</td><td>220.54 (+10.23%)</td><td>221.20 (+13.90%)</td><td>199.90 (+15.48%)</td><td>16.93 <b>(-50.22%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.00 (n/a)</td><td>200.08 (n/a)</td><td>194.20 (n/a)</td><td>173.10 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>188.62 (n/a)</td><td>199.30 (n/a)</td><td>133.30 (n/a)</td><td>33.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>189.28 (n/a)</td><td>196.60 (n/a)</td><td>158.40 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>261.50 (n/a)</td><td>189.58 (n/a)</td><td>176.60 (n/a)</td><td>124.10 (n/a)</td><td>50.49 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>241.40 (n/a)</td><td>218.86 (n/a)</td><td>227.00 (n/a)</td><td>181.00 (n/a)</td><td>23.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>220.80 (n/a)</td><td>168.20 (n/a)</td><td>144.90 (n/a)</td><td>132.00 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>290.70 (n/a)</td><td>187.64 (n/a)</td><td>185.70 (n/a)</td><td>127.00 (n/a)</td><td>66.93 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>252.30 (n/a)</td><td>192.50 (n/a)</td><td>184.60 (n/a)</td><td>128.40 (n/a)</td><td>49.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>180.66 (n/a)</td><td>198.70 (n/a)</td><td>123.70 (n/a)</td><td>36.17 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.16 <b>(-20.12%)</b></td><td>3.45 (-3.45%)</td><td>3.14 (-3.23%)</td><td>2.90 (-1.39%)</td><td>0.62 <b>(-32.41%)</b></td><td>474.70 (+1.41%)</td><td>408.76 (+1.90%)</td><td>438.30 (+3.35%)</td><td>330.70 <b>(+25.17%)</b></td><td>70.13 (-11.18%)</td><td>811.67 <b>(-20.12%)</b></td><td>673.41 (-3.45%)</td><td>612.48 (-3.23%)</td><td>565.50 (-1.39%)</td><td>121.72 <b>(-32.41%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.21 (n/a)</td><td>3.58 (n/a)</td><td>3.24 (n/a)</td><td>2.94 (n/a)</td><td>0.92 (n/a)</td><td>468.10 (n/a)</td><td>401.12 (n/a)</td><td>424.10 (n/a)</td><td>264.20 (n/a)</td><td>78.96 (n/a)</td><td>1016.13 (n/a)</td><td>697.46 (n/a)</td><td>632.91 (n/a)</td><td>573.49 (n/a)</td><td>180.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.78 (-19.43%)</td><td>3.84 (-13.36%)</td><td>3.59 (-5.41%)</td><td>3.48 (+2.03%)</td><td>0.54 <b>(-51.17%)</b></td><td>395.80 (-1.98%)</td><td>363.58 (+11.69%)</td><td>383.50 (+5.71%)</td><td>288.10 <b>(+24.13%)</b></td><td>44.03 <b>(-40.90%)</b></td><td>931.88 (-19.43%)</td><td>748.48 (-13.36%)</td><td>699.93 (-5.41%)</td><td>678.29 (+2.03%)</td><td>105.22 <b>(-51.17%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.93 (n/a)</td><td>4.43 (n/a)</td><td>3.79 (n/a)</td><td>3.41 (n/a)</td><td>1.10 (n/a)</td><td>403.80 (n/a)</td><td>325.52 (n/a)</td><td>362.80 (n/a)</td><td>232.10 (n/a)</td><td>74.50 (n/a)</td><td>1156.64 (n/a)</td><td>863.90 (n/a)</td><td>739.94 (n/a)</td><td>664.79 (n/a)</td><td>215.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.45 (-5.11%)</td><td>4.29 (+1.79%)</td><td>3.89 (-3.75%)</td><td>3.69 (+5.84%)</td><td>0.73 (-18.68%)</td><td>373.10 (-5.52%)</td><td>327.34 (-2.74%)</td><td>354.10 (+3.90%)</td><td>252.30 (+5.39%)</td><td>50.20 (-17.52%)</td><td>1063.95 (-5.11%)</td><td>837.56 (+1.79%)</td><td>758.16 (-3.75%)</td><td>719.40 (+5.84%)</td><td>143.35 (-18.68%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.75 (n/a)</td><td>4.22 (n/a)</td><td>4.04 (n/a)</td><td>3.48 (n/a)</td><td>0.90 (n/a)</td><td>394.90 (n/a)</td><td>336.56 (n/a)</td><td>340.80 (n/a)</td><td>239.40 (n/a)</td><td>60.86 (n/a)</td><td>1121.26 (n/a)</td><td>822.83 (n/a)</td><td>787.66 (n/a)</td><td>679.70 (n/a)</td><td>176.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>7.01 (+12.44%)</td><td>4.38 (-11.61%)</td><td>3.67 <b>(-27.16%)</b></td><td>3.61 (-2.30%)</td><td>1.48 <b>(+22.41%)</b></td><td>381.70 (+2.33%)</td><td>335.54 (+14.91%)</td><td>374.90 <b>(+37.28%)</b></td><td>196.20 (-11.06%)</td><td>78.97 (+7.68%)</td><td>1368.22 (+12.44%)</td><td>854.17 (-11.61%)</td><td>715.97 <b>(-27.16%)</b></td><td>703.19 (-2.30%)</td><td>288.57 <b>(+22.41%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>6.24 (n/a)</td><td>4.95 (n/a)</td><td>5.04 (n/a)</td><td>3.69 (n/a)</td><td>1.21 (n/a)</td><td>373.00 (n/a)</td><td>292.00 (n/a)</td><td>273.10 (n/a)</td><td>220.60 (n/a)</td><td>73.34 (n/a)</td><td>1216.85 (n/a)</td><td>966.41 (n/a)</td><td>982.92 (n/a)</td><td>719.72 (n/a)</td><td>235.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>7.08 <b>(+37.77%)</b></td><td>3.96 (+7.92%)</td><td>3.23 (-5.39%)</td><td>3.07 (-2.04%)</td><td>1.74 <b>(+109.94%)</b></td><td>448.50 (+2.09%)</td><td>385.48 (-0.57%)</td><td>425.60 (+5.71%)</td><td>194.50 <b>(-27.43%)</b></td><td>107.30 <b>(+55.71%)</b></td><td>1380.13 <b>(+37.77%)</b></td><td>772.04 (+7.92%)</td><td>630.80 (-5.39%)</td><td>598.54 (-2.04%)</td><td>340.28 <b>(+109.94%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.14 (n/a)</td><td>3.67 (n/a)</td><td>3.42 (n/a)</td><td>3.13 (n/a)</td><td>0.83 (n/a)</td><td>439.30 (n/a)</td><td>387.68 (n/a)</td><td>402.60 (n/a)</td><td>268.00 (n/a)</td><td>68.91 (n/a)</td><td>1001.77 (n/a)</td><td>715.39 (n/a)</td><td>666.74 (n/a)</td><td>611.02 (n/a)</td><td>162.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>2.22 (-0.24%)</td><td>1.87 (-0.60%)</td><td>1.86 (+5.04%)</td><td>1.66 (+4.31%)</td><td>0.22 (-16.61%)</td><td>241.30 (-4.13%)</td><td>216.94 (+0.11%)</td><td>216.30 (-4.80%)</td><td>181.20 (+0.22%)</td><td>23.27 (-19.47%)</td><td>185.17 (-0.24%)</td><td>156.21 (-0.60%)</td><td>155.12 (+5.04%)</td><td>139.07 (+4.31%)</td><td>17.99 (-16.61%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>2.22 (n/a)</td><td>1.88 (n/a)</td><td>1.77 (n/a)</td><td>1.59 (n/a)</td><td>0.26 (n/a)</td><td>251.70 (n/a)</td><td>216.70 (n/a)</td><td>227.20 (n/a)</td><td>180.80 (n/a)</td><td>28.90 (n/a)</td><td>185.63 (n/a)</td><td>157.15 (n/a)</td><td>147.68 (n/a)</td><td>133.32 (n/a)</td><td>21.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.13 <b>(-35.89%)</b></td><td>4.96 <b>(-21.92%)</b></td><td>4.96 <b>(-28.33%)</b></td><td>4.82 (+7.05%)</td><td>0.11 <b>(-92.23%)</b></td><td>401.00 (-6.57%)</td><td>390.04 <b>(+22.28%)</b></td><td>389.70 <b>(+39.53%)</b></td><td>377.00 <b>(+55.98%)</b></td><td>8.88 <b>(-88.84%)</b></td><td>1068.11 <b>(-35.89%)</b></td><td>1032.80 <b>(-21.92%)</b></td><td>1033.29 <b>(-28.33%)</b></td><td>1004.16 (+7.05%)</td><td>23.71 <b>(-92.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>8.00 (n/a)</td><td>6.35 (n/a)</td><td>6.92 (n/a)</td><td>4.50 (n/a)</td><td>1.46 (n/a)</td><td>429.20 (n/a)</td><td>318.96 (n/a)</td><td>279.30 (n/a)</td><td>241.70 (n/a)</td><td>79.59 (n/a)</td><td>1666.06 (n/a)</td><td>1322.81 (n/a)</td><td>1441.69 (n/a)</td><td>938.07 (n/a)</td><td>305.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>16.69 (-14.92%)</td><td>12.98 (-7.24%)</td><td>12.33 (-2.62%)</td><td>11.56 (-4.39%)</td><td>2.12 <b>(-33.03%)</b></td><td>476.40 (+4.59%)</td><td>431.78 (+6.28%)</td><td>446.60 (+2.69%)</td><td>329.90 (+17.53%)</td><td>59.50 (-16.88%)</td><td>6508.95 (-14.92%)</td><td>5064.35 (-7.24%)</td><td>4807.98 (-2.62%)</td><td>4507.76 (-4.39%)</td><td>826.99 <b>(-33.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>19.61 (n/a)</td><td>14.00 (n/a)</td><td>12.66 (n/a)</td><td>12.09 (n/a)</td><td>3.17 (n/a)</td><td>455.50 (n/a)</td><td>406.28 (n/a)</td><td>434.90 (n/a)</td><td>280.70 (n/a)</td><td>71.58 (n/a)</td><td>7650.08 (n/a)</td><td>5459.41 (n/a)</td><td>4937.45 (n/a)</td><td>4714.90 (n/a)</td><td>1234.85 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>147.54 (n/a)</td><td>135.00 (n/a)</td><td>124.80 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>168.42 (n/a)</td><td>166.90 (n/a)</td><td>146.80 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>168.12 (n/a)</td><td>171.40 (n/a)</td><td>142.70 (n/a)</td><td>21.15 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>234.60 (n/a)</td><td>164.92 (n/a)</td><td>148.30 (n/a)</td><td>120.00 (n/a)</td><td>50.89 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.30 (n/a)</td><td>159.06 (n/a)</td><td>156.60 (n/a)</td><td>148.50 (n/a)</td><td>11.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.70 (n/a)</td><td>207.34 (n/a)</td><td>186.70 (n/a)</td><td>132.50 (n/a)</td><td>74.27 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>176.36 (n/a)</td><td>157.20 (n/a)</td><td>155.30 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.80 (n/a)</td><td>195.36 (n/a)</td><td>180.00 (n/a)</td><td>144.50 (n/a)</td><td>44.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.16 (-13.06%)</td><td>3.88 (-9.79%)</td><td>3.98 (-5.10%)</td><td>3.52 (-14.65%)</td><td>0.26 (-5.06%)</td><td>2672.80 (+17.17%)</td><td>2431.38 (+10.92%)</td><td>2361.90 (+5.38%)</td><td>2263.00 (+15.02%)</td><td>165.93 <b>(+29.50%)</b></td><td>1634.75 (-13.06%)</td><td>1527.04 (-9.79%)</td><td>1566.29 (-5.10%)</td><td>1384.08 (-14.65%)</td><td>101.17 (-5.06%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.78 (n/a)</td><td>4.30 (n/a)</td><td>4.20 (n/a)</td><td>4.12 (n/a)</td><td>0.27 (n/a)</td><td>2281.20 (n/a)</td><td>2191.96 (n/a)</td><td>2241.40 (n/a)</td><td>1967.40 (n/a)</td><td>128.14 (n/a)</td><td>1880.31 (n/a)</td><td>1692.68 (n/a)</td><td>1650.44 (n/a)</td><td>1621.71 (n/a)</td><td>106.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.12 (-7.38%)</td><td>1.00 (-1.44%)</td><td>1.02 (-5.96%)</td><td>0.88 <b>(+25.26%)</b></td><td>0.09 <b>(-52.98%)</b></td><td>251.80 <b>(-20.16%)</b></td><td>222.30 (-1.50%)</td><td>216.30 (+6.34%)</td><td>196.70 (+7.96%)</td><td>20.83 <b>(-60.57%)</b></td><td>47.97 (-7.38%)</td><td>42.75 (-1.44%)</td><td>43.62 (-5.96%)</td><td>37.48 <b>(+25.26%)</b></td><td>3.95 <b>(-52.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.21 (n/a)</td><td>1.02 (n/a)</td><td>1.09 (n/a)</td><td>0.70 (n/a)</td><td>0.20 (n/a)</td><td>315.40 (n/a)</td><td>225.68 (n/a)</td><td>203.40 (n/a)</td><td>182.20 (n/a)</td><td>52.82 (n/a)</td><td>51.79 (n/a)</td><td>43.37 (n/a)</td><td>46.39 (n/a)</td><td>29.92 (n/a)</td><td>8.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.17 (-4.53%)</td><td>1.10 (+2.98%)</td><td>1.11 (-0.36%)</td><td>1.04 <b>(+46.77%)</b></td><td>0.06 <b>(-72.53%)</b></td><td>212.90 <b>(-31.85%)</b></td><td>202.22 (-6.49%)</td><td>198.90 (+0.35%)</td><td>188.60 (+4.78%)</td><td>10.50 <b>(-80.78%)</b></td><td>50.04 (-4.53%)</td><td>46.77 (+2.98%)</td><td>47.44 (-0.36%)</td><td>44.33 <b>(+46.77%)</b></td><td>2.44 <b>(-72.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.23 (n/a)</td><td>1.06 (n/a)</td><td>1.12 (n/a)</td><td>0.71 (n/a)</td><td>0.21 (n/a)</td><td>312.40 (n/a)</td><td>216.26 (n/a)</td><td>198.20 (n/a)</td><td>180.00 (n/a)</td><td>54.65 (n/a)</td><td>52.42 (n/a)</td><td>45.42 (n/a)</td><td>47.61 (n/a)</td><td>30.21 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.53 (-0.02%)</td><td>0.53 (+0.01%)</td><td>0.53 (+0.04%)</td><td>0.53 (+0.02%)</td><td>0.00 (-10.68%)</td><td>47889.10 (-0.02%)</td><td>47823.56 (-0.01%)</td><td>47811.20 (-0.04%)</td><td>47785.60 (+0.02%)</td><td>41.21 (-10.61%)</td><td>359.52 (-0.02%)</td><td>359.23 (+0.01%)</td><td>359.33 (+0.04%)</td><td>358.74 (+0.02%)</td><td>0.31 (-10.68%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47897.20 (n/a)</td><td>47826.26 (n/a)</td><td>47828.70 (n/a)</td><td>47777.90 (n/a)</td><td>46.10 (n/a)</td><td>359.58 (n/a)</td><td>359.21 (n/a)</td><td>359.20 (n/a)</td><td>358.68 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.92 (+1.74%)</td><td>0.91 (+0.79%)</td><td>0.91 (+0.91%)</td><td>0.90 (+0.34%)</td><td>0.01 <b>(+263.42%)</b></td><td>27934.80 (-0.33%)</td><td>27714.24 (-0.78%)</td><td>27676.10 (-0.90%)</td><td>27383.60 (-1.71%)</td><td>221.70 <b>(+256.01%)</b></td><td>627.38 (+1.74%)</td><td>619.93 (+0.79%)</td><td>620.75 (+0.91%)</td><td>615.00 (+0.34%)</td><td>4.98 <b>(+263.43%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28028.50 (n/a)</td><td>27932.50 (n/a)</td><td>27928.30 (n/a)</td><td>27860.50 (n/a)</td><td>62.27 (n/a)</td><td>616.64 (n/a)</td><td>615.05 (n/a)</td><td>615.14 (n/a)</td><td>612.94 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>3.34 (+0.51%)</td><td>3.20 (-0.94%)</td><td>3.19 (+0.41%)</td><td>3.10 (-1.86%)</td><td>0.09 (+6.17%)</td><td>8111.90 (+1.89%)</td><td>7871.20 (+0.96%)</td><td>7884.40 (-0.41%)</td><td>7544.20 (-0.51%)</td><td>208.21 (+7.42%)</td><td>2277.23 (+0.51%)</td><td>2183.87 (-0.94%)</td><td>2178.96 (+0.41%)</td><td>2117.86 (-1.86%)</td><td>58.69 (+6.17%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.32 (n/a)</td><td>3.23 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>0.08 (n/a)</td><td>7961.40 (n/a)</td><td>7796.64 (n/a)</td><td>7916.50 (n/a)</td><td>7582.60 (n/a)</td><td>193.82 (n/a)</td><td>2265.70 (n/a)</td><td>2204.60 (n/a)</td><td>2170.15 (n/a)</td><td>2157.90 (n/a)</td><td>55.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.22 (-0.32%)</td><td>3.70 (-3.54%)</td><td>3.60 (-4.19%)</td><td>3.01 (-17.83%)</td><td>0.50 <b>(+121.56%)</b></td><td>2678.30 <b>(+21.70%)</b></td><td>2212.10 (+5.01%)</td><td>2240.80 (+4.38%)</td><td>1911.10 (+0.33%)</td><td>314.60 <b>(+168.02%)</b></td><td>1106.13 (-0.32%)</td><td>970.59 (-3.54%)</td><td>943.37 (-4.19%)</td><td>789.28 (-17.83%)</td><td>132.42 <b>(+121.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.23 (n/a)</td><td>3.84 (n/a)</td><td>3.75 (n/a)</td><td>3.66 (n/a)</td><td>0.23 (n/a)</td><td>2200.70 (n/a)</td><td>2106.52 (n/a)</td><td>2146.80 (n/a)</td><td>1904.90 (n/a)</td><td>117.38 (n/a)</td><td>1109.71 (n/a)</td><td>1006.17 (n/a)</td><td>984.67 (n/a)</td><td>960.59 (n/a)</td><td>59.77 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.34 <b>(-34.69%)</b></td><td>0.32 <b>(-20.79%)</b></td><td>0.33 (-8.41%)</td><td>0.28 (-12.98%)</td><td>0.02 <b>(-77.66%)</b></td><td>4370.50 (+14.92%)</td><td>3916.00 <b>(+21.99%)</b></td><td>3808.70 (+9.18%)</td><td>3710.00 <b>(+53.12%)</b></td><td>264.09 <b>(-60.42%)</b></td><td>18.09 <b>(-34.69%)</b></td><td>17.20 <b>(-20.79%)</b></td><td>17.62 (-8.41%)</td><td>15.35 (-12.98%)</td><td>1.08 <b>(-77.66%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>3803.20 (n/a)</td><td>3210.22 (n/a)</td><td>3488.50 (n/a)</td><td>2422.90 (n/a)</td><td>667.23 (n/a)</td><td>27.70 (n/a)</td><td>21.71 (n/a)</td><td>19.24 (n/a)</td><td>17.65 (n/a)</td><td>4.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.76 <b>(-25.63%)</b></td><td>3.74 <b>(-23.96%)</b></td><td>3.55 <b>(-27.33%)</b></td><td>3.31 (-2.60%)</td><td>0.58 <b>(-45.56%)</b></td><td>2011.40 (+2.67%)</td><td>1808.58 <b>(+28.29%)</b></td><td>1876.40 <b>(+37.62%)</b></td><td>1397.30 <b>(+34.46%)</b></td><td>237.37 <b>(-29.40%)</b></td><td>1470.83 <b>(-25.63%)</b></td><td>1155.14 <b>(-23.96%)</b></td><td>1095.30 <b>(-27.33%)</b></td><td>1021.76 (-2.60%)</td><td>179.40 <b>(-45.56%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>6.40 (n/a)</td><td>4.92 (n/a)</td><td>4.88 (n/a)</td><td>3.40 (n/a)</td><td>1.07 (n/a)</td><td>1959.10 (n/a)</td><td>1409.72 (n/a)</td><td>1363.50 (n/a)</td><td>1039.20 (n/a)</td><td>336.22 (n/a)</td><td>1977.61 (n/a)</td><td>1519.08 (n/a)</td><td>1507.28 (n/a)</td><td>1049.05 (n/a)</td><td>329.53 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.30 (n/a)</td><td>12.83 (n/a)</td><td>12.98 (n/a)</td><td>12.38 (n/a)</td><td>0.40 (n/a)</td><td>13.29 (n/a)</td><td>12.83 (n/a)</td><td>12.97 (n/a)</td><td>12.37 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>24.50 (-1.91%)</td><td>24.12 (-1.87%)</td><td>24.04 (-2.62%)</td><td>23.91 (+0.18%)</td><td>0.23 <b>(-46.13%)</b></td><td>24.49 (-1.91%)</td><td>24.11 (-1.87%)</td><td>24.03 (-2.62%)</td><td>23.90 (+0.18%)</td><td>0.23 <b>(-46.14%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>24.98 (n/a)</td><td>24.58 (n/a)</td><td>24.69 (n/a)</td><td>23.87 (n/a)</td><td>0.42 (n/a)</td><td>24.96 (n/a)</td><td>24.57 (n/a)</td><td>24.67 (n/a)</td><td>23.85 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>41.08 (-0.87%)</td><td>39.04 (-3.93%)</td><td>38.82 (-3.56%)</td><td>37.79 (-5.45%)</td><td>1.24 <b>(+75.51%)</b></td><td>41.05 (-0.87%)</td><td>39.02 (-3.93%)</td><td>38.79 (-3.56%)</td><td>37.77 (-5.45%)</td><td>1.24 <b>(+75.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>41.44 (n/a)</td><td>40.64 (n/a)</td><td>40.25 (n/a)</td><td>39.97 (n/a)</td><td>0.71 (n/a)</td><td>41.41 (n/a)</td><td>40.61 (n/a)</td><td>40.23 (n/a)</td><td>39.95 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>44.59 (-0.86%)</td><td>43.01 (+5.57%)</td><td>43.14 (-2.86%)</td><td>40.96 <b>(+46.41%)</b></td><td>1.37 <b>(-81.06%)</b></td><td>44.56 (-0.86%)</td><td>42.98 (+5.57%)</td><td>43.11 (-2.86%)</td><td>40.94 <b>(+46.41%)</b></td><td>1.37 <b>(-81.06%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>44.98 (n/a)</td><td>40.74 (n/a)</td><td>44.41 (n/a)</td><td>27.98 (n/a)</td><td>7.25 (n/a)</td><td>44.95 (n/a)</td><td>40.71 (n/a)</td><td>44.38 (n/a)</td><td>27.96 (n/a)</td><td>7.25 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.25 (n/a)</td><td>12.82 (n/a)</td><td>12.65 (n/a)</td><td>12.44 (n/a)</td><td>0.35 (n/a)</td><td>13.24 (n/a)</td><td>12.81 (n/a)</td><td>12.64 (n/a)</td><td>12.43 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>24.49 (-3.21%)</td><td>24.02 (-1.67%)</td><td>24.06 (-1.48%)</td><td>23.63 (-1.33%)</td><td>0.32 <b>(-40.19%)</b></td><td>24.47 (-3.21%)</td><td>24.00 (-1.67%)</td><td>24.05 (-1.48%)</td><td>23.62 (-1.33%)</td><td>0.32 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>25.30 (n/a)</td><td>24.43 (n/a)</td><td>24.42 (n/a)</td><td>23.95 (n/a)</td><td>0.54 (n/a)</td><td>25.28 (n/a)</td><td>24.41 (n/a)</td><td>24.41 (n/a)</td><td>23.93 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>41.52 (-0.46%)</td><td>40.74 (+4.60%)</td><td>40.95 (+3.29%)</td><td>39.54 (+15.75%)</td><td>0.84 <b>(-72.65%)</b></td><td>41.49 (-0.46%)</td><td>40.72 (+4.60%)</td><td>40.92 (+3.29%)</td><td>39.51 (+15.75%)</td><td>0.84 <b>(-72.65%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>41.71 (n/a)</td><td>38.95 (n/a)</td><td>39.64 (n/a)</td><td>34.16 (n/a)</td><td>3.07 (n/a)</td><td>41.68 (n/a)</td><td>38.93 (n/a)</td><td>39.62 (n/a)</td><td>34.14 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>43.81 (-7.69%)</td><td>39.82 (-10.99%)</td><td>42.61 (-3.52%)</td><td>31.34 <b>(-27.61%)</b></td><td>5.34 <b>(+223.45%)</b></td><td>43.79 (-7.69%)</td><td>39.79 (-10.99%)</td><td>42.59 (-3.52%)</td><td>31.32 <b>(-27.61%)</b></td><td>5.33 <b>(+223.45%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>47.46 (n/a)</td><td>44.74 (n/a)</td><td>44.17 (n/a)</td><td>43.29 (n/a)</td><td>1.65 (n/a)</td><td>47.44 (n/a)</td><td>44.71 (n/a)</td><td>44.14 (n/a)</td><td>43.27 (n/a)</td><td>1.65 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>9.54 (-4.49%)</td><td>9.06 (+1.26%)</td><td>8.90 (+1.16%)</td><td>8.69 (+3.41%)</td><td>0.41 <b>(-33.14%)</b></td><td>9.52 (-4.49%)</td><td>9.04 (+1.26%)</td><td>8.89 (+1.16%)</td><td>8.68 (+3.41%)</td><td>0.41 <b>(-33.14%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>9.99 (n/a)</td><td>8.94 (n/a)</td><td>8.80 (n/a)</td><td>8.41 (n/a)</td><td>0.61 (n/a)</td><td>9.97 (n/a)</td><td>8.93 (n/a)</td><td>8.79 (n/a)</td><td>8.39 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.97 (-4.70%)</td><td>0.92 (+3.14%)</td><td>0.94 (+9.36%)</td><td>0.85 (+4.51%)</td><td>0.05 <b>(-37.34%)</b></td><td>0.95 (-4.70%)</td><td>0.91 (+3.14%)</td><td>0.93 (+9.36%)</td><td>0.84 (+4.51%)</td><td>0.05 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.02 (n/a)</td><td>0.89 (n/a)</td><td>0.86 (n/a)</td><td>0.82 (n/a)</td><td>0.08 (n/a)</td><td>1.00 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.80 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.41 (+11.90%)</td><td>1.24 (+7.89%)</td><td>1.24 (+9.47%)</td><td>1.06 (+3.09%)</td><td>0.13 (+18.02%)</td><td>1.40 (+11.90%)</td><td>1.22 (+7.89%)</td><td>1.23 (+9.47%)</td><td>1.05 (+3.09%)</td><td>0.13 (+18.02%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.26 (n/a)</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.03 (n/a)</td><td>0.11 (n/a)</td><td>1.25 (n/a)</td><td>1.13 (n/a)</td><td>1.12 (n/a)</td><td>1.01 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>16.34 (-18.12%)</td><td>15.43 (-12.14%)</td><td>15.89 (-7.16%)</td><td>13.32 (-15.36%)</td><td>1.22 <b>(-26.24%)</b></td><td>16.15 (-18.12%)</td><td>15.25 (-12.14%)</td><td>15.70 (-7.16%)</td><td>13.17 (-15.36%)</td><td>1.20 <b>(-26.24%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>19.95 (n/a)</td><td>17.56 (n/a)</td><td>17.11 (n/a)</td><td>15.74 (n/a)</td><td>1.65 (n/a)</td><td>19.72 (n/a)</td><td>17.35 (n/a)</td><td>16.91 (n/a)</td><td>15.56 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.74 (-0.99%)</td><td>13.17 (-0.27%)</td><td>13.42 (+0.64%)</td><td>11.86 (-1.17%)</td><td>0.76 (+2.06%)</td><td>13.50 (-0.99%)</td><td>12.94 (-0.27%)</td><td>13.18 (+0.64%)</td><td>11.65 (-1.17%)</td><td>0.75 (+2.06%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>13.88 (n/a)</td><td>13.21 (n/a)</td><td>13.33 (n/a)</td><td>12.00 (n/a)</td><td>0.75 (n/a)</td><td>13.64 (n/a)</td><td>12.97 (n/a)</td><td>13.10 (n/a)</td><td>11.79 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>9.25 (+5.02%)</td><td>7.93 (+2.53%)</td><td>8.39 (+10.87%)</td><td>5.98 (-14.23%)</td><td>1.33 <b>(+96.93%)</b></td><td>9.09 (+5.02%)</td><td>7.79 (+2.53%)</td><td>8.25 (+10.87%)</td><td>5.88 (-14.23%)</td><td>1.30 <b>(+96.93%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>8.81 (n/a)</td><td>7.74 (n/a)</td><td>7.57 (n/a)</td><td>6.97 (n/a)</td><td>0.67 (n/a)</td><td>8.66 (n/a)</td><td>7.60 (n/a)</td><td>7.44 (n/a)</td><td>6.85 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>6.65 (+13.42%)</td><td>5.63 (+6.51%)</td><td>5.86 (+12.08%)</td><td>4.70 (+4.33%)</td><td>0.78 <b>(+51.19%)</b></td><td>6.55 (+13.42%)</td><td>5.54 (+6.51%)</td><td>5.77 (+12.08%)</td><td>4.62 (+4.33%)</td><td>0.77 <b>(+51.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>5.86 (n/a)</td><td>5.28 (n/a)</td><td>5.23 (n/a)</td><td>4.50 (n/a)</td><td>0.52 (n/a)</td><td>5.77 (n/a)</td><td>5.20 (n/a)</td><td>5.14 (n/a)</td><td>4.43 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.34 (n/a)</td><td>13.14 (n/a)</td><td>13.20 (n/a)</td><td>12.82 (n/a)</td><td>0.20 (n/a)</td><td>13.33 (n/a)</td><td>13.13 (n/a)</td><td>13.19 (n/a)</td><td>12.81 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.58 (n/a)</td><td>13.30 (n/a)</td><td>13.27 (n/a)</td><td>13.03 (n/a)</td><td>0.20 (n/a)</td><td>13.58 (n/a)</td><td>13.29 (n/a)</td><td>13.27 (n/a)</td><td>13.03 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.80 (n/a)</td><td>149.56 (n/a)</td><td>155.60 (n/a)</td><td>118.90 (n/a)</td><td>23.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>163.76 (n/a)</td><td>152.60 (n/a)</td><td>139.90 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.80 (n/a)</td><td>158.18 (n/a)</td><td>163.40 (n/a)</td><td>134.60 (n/a)</td><td>16.70 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.90 (n/a)</td><td>161.86 (n/a)</td><td>164.10 (n/a)</td><td>138.00 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>149.94 (n/a)</td><td>147.40 (n/a)</td><td>102.30 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.70 (n/a)</td><td>173.74 (n/a)</td><td>170.70 (n/a)</td><td>137.60 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.70 (n/a)</td><td>172.86 (n/a)</td><td>172.20 (n/a)</td><td>152.00 (n/a)</td><td>15.60 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>225.30 (n/a)</td><td>203.92 (n/a)</td><td>206.00 (n/a)</td><td>177.60 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-13.55%)</td><td>0.05 (-11.73%)</td><td>0.05 (-4.53%)</td><td>0.04 (-5.39%)</td><td>0.01 <b>(-41.24%)</b></td><td>200.00 (+5.71%)</td><td>161.94 (+10.24%)</td><td>162.90 (+4.76%)</td><td>126.30 (+15.66%)</td><td>26.22 <b>(-25.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>146.90 (n/a)</td><td>155.50 (n/a)</td><td>109.20 (n/a)</td><td>35.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-12.77%)</td><td>0.05 (-3.81%)</td><td>0.05 (-2.69%)</td><td>0.05 (+1.85%)</td><td>0.01 <b>(-31.00%)</b></td><td>178.10 (-1.82%)</td><td>156.86 (+2.86%)</td><td>161.10 (+2.74%)</td><td>132.90 (+14.67%)</td><td>19.68 <b>(-21.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>152.50 (n/a)</td><td>156.80 (n/a)</td><td>115.90 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (+7.27%)</td><td>0.06 (+2.13%)</td><td>0.05 (-0.67%)</td><td>0.04 (-12.90%)</td><td>0.01 <b>(+64.21%)</b></td><td>194.40 (+14.83%)</td><td>148.26 (+0.54%)</td><td>153.40 (+0.72%)</td><td>112.60 (-6.79%)</td><td>33.75 <b>(+71.08%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.30 (n/a)</td><td>147.46 (n/a)</td><td>152.30 (n/a)</td><td>120.80 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-10.67%)</td><td>0.05 (-5.36%)</td><td>0.05 (-9.17%)</td><td>0.04 (-5.95%)</td><td>0.01 (-12.74%)</td><td>186.40 (+6.33%)</td><td>158.74 (+5.52%)</td><td>169.30 (+10.15%)</td><td>128.90 (+11.99%)</td><td>23.78 (+4.94%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.30 (n/a)</td><td>150.44 (n/a)</td><td>153.70 (n/a)</td><td>115.10 (n/a)</td><td>22.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-15.55%)</td><td>0.05 (-15.24%)</td><td>0.05 (-18.82%)</td><td>0.03 <b>(-21.98%)</b></td><td>0.01 (-17.25%)</td><td>278.10 <b>(+28.16%)</b></td><td>181.76 (+18.52%)</td><td>168.70 <b>(+23.14%)</b></td><td>134.90 (+18.44%)</td><td>56.09 <b>(+31.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>153.36 (n/a)</td><td>137.00 (n/a)</td><td>113.90 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-2.31%)</td><td>0.05 (-8.10%)</td><td>0.04 (-17.25%)</td><td>0.04 (-9.89%)</td><td>0.01 <b>(+30.38%)</b></td><td>211.00 (+10.99%)</td><td>172.30 (+10.55%)</td><td>186.50 <b>(+20.87%)</b></td><td>128.70 (+2.39%)</td><td>33.62 <b>(+46.21%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.10 (n/a)</td><td>155.86 (n/a)</td><td>154.30 (n/a)</td><td>125.70 (n/a)</td><td>22.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (+2.86%)</td><td>0.05 (-7.11%)</td><td>0.05 (+1.00%)</td><td>0.04 (-6.23%)</td><td>0.01 (+2.26%)</td><td>199.30 (+6.63%)</td><td>157.64 (+8.02%)</td><td>154.60 (-0.96%)</td><td>108.90 (-2.77%)</td><td>33.74 (+7.58%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>145.94 (n/a)</td><td>156.10 (n/a)</td><td>112.00 (n/a)</td><td>31.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-17.27%)</td><td>0.05 (-10.24%)</td><td>0.05 (-3.13%)</td><td>0.04 (-19.05%)</td><td>0.01 (+4.19%)</td><td>223.00 <b>(+23.55%)</b></td><td>177.82 (+12.89%)</td><td>166.30 (+3.23%)</td><td>144.40 <b>(+20.94%)</b></td><td>37.07 <b>(+57.23%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>157.52 (n/a)</td><td>161.10 (n/a)</td><td>119.40 (n/a)</td><td>23.57 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (-16.67%)</td><td>0.04 (-11.33%)</td><td>0.05 (-0.94%)</td><td>0.03 (-15.77%)</td><td>0.01 (-7.17%)</td><td>261.90 (+18.72%)</td><td>192.60 (+13.47%)</td><td>164.80 (+0.98%)</td><td>160.80 <b>(+20.00%)</b></td><td>43.89 <b>(+29.19%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>169.74 (n/a)</td><td>163.20 (n/a)</td><td>134.00 (n/a)</td><td>33.97 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (-8.60%)</td><td>0.04 (-6.61%)</td><td>0.04 (-6.18%)</td><td>0.03 (-1.38%)</td><td>0.00 (-14.98%)</td><td>244.10 (+1.37%)</td><td>208.32 (+6.74%)</td><td>200.70 (+6.59%)</td><td>180.80 (+9.44%)</td><td>25.72 (-7.66%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.80 (n/a)</td><td>195.16 (n/a)</td><td>188.30 (n/a)</td><td>165.20 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 <b>(-27.23%)</b></td><td>0.05 (-13.70%)</td><td>0.05 (-7.68%)</td><td>0.04 <b>(-20.21%)</b></td><td>0.01 <b>(-39.89%)</b></td><td>224.20 <b>(+25.32%)</b></td><td>177.50 (+14.89%)</td><td>172.10 (+8.31%)</td><td>154.10 <b>(+37.47%)</b></td><td>27.65 (+10.03%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>154.50 (n/a)</td><td>158.90 (n/a)</td><td>112.10 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (-15.95%)</td><td>0.04 (-7.92%)</td><td>0.04 (-3.66%)</td><td>0.03 <b>(-20.94%)</b></td><td>0.01 (-3.37%)</td><td>321.40 <b>(+26.49%)</b></td><td>230.08 (+9.88%)</td><td>223.60 (+3.81%)</td><td>185.10 (+18.96%)</td><td>55.00 <b>(+48.59%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.10 (n/a)</td><td>209.40 (n/a)</td><td>215.40 (n/a)</td><td>155.60 (n/a)</td><td>37.02 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (+3.20%)</td><td>0.05 (-2.92%)</td><td>0.06 (+10.01%)</td><td>0.03 <b>(-27.61%)</b></td><td>0.02 <b>(+70.14%)</b></td><td>263.30 <b>(+38.14%)</b></td><td>173.54 (+11.73%)</td><td>146.20 (-9.08%)</td><td>110.30 (-3.08%)</td><td>65.96 <b>(+138.32%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>155.32 (n/a)</td><td>160.80 (n/a)</td><td>113.80 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (-15.88%)</td><td>0.05 (-15.04%)</td><td>0.04 <b>(-27.18%)</b></td><td>0.04 <b>(+49.99%)</b></td><td>0.01 <b>(-46.68%)</b></td><td>209.10 <b>(-33.32%)</b></td><td>177.84 (+5.13%)</td><td>189.70 <b>(+37.36%)</b></td><td>124.20 (+18.85%)</td><td>32.88 <b>(-60.98%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>313.60 (n/a)</td><td>169.16 (n/a)</td><td>138.10 (n/a)</td><td>104.50 (n/a)</td><td>84.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 <b>(-22.66%)</b></td><td>0.05 (-18.78%)</td><td>0.05 (-7.87%)</td><td>0.04 <b>(-27.79%)</b></td><td>0.01 (-6.61%)</td><td>233.40 <b>(+38.52%)</b></td><td>183.22 <b>(+24.44%)</b></td><td>168.30 (+8.58%)</td><td>150.60 <b>(+29.38%)</b></td><td>36.43 <b>(+65.34%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>147.24 (n/a)</td><td>155.00 (n/a)</td><td>116.40 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 <b>(-36.17%)</b></td><td>0.05 (-17.68%)</td><td>0.05 (-2.56%)</td><td>0.04 (-6.53%)</td><td>0.01 <b>(-66.49%)</b></td><td>225.30 (+6.98%)</td><td>182.86 (+14.42%)</td><td>180.40 (+2.62%)</td><td>155.20 <b>(+56.61%)</b></td><td>26.19 <b>(-42.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>210.60 (n/a)</td><td>159.82 (n/a)</td><td>175.80 (n/a)</td><td>99.10 (n/a)</td><td>45.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (+11.12%)</td><td>0.04 (-12.18%)</td><td>0.03 <b>(-26.53%)</b></td><td>0.03 <b>(-26.20%)</b></td><td>0.01 <b>(+93.11%)</b></td><td>288.30 <b>(+35.48%)</b></td><td>219.82 <b>(+20.61%)</b></td><td>237.80 <b>(+36.12%)</b></td><td>133.30 (-9.99%)</td><td>61.58 <b>(+126.96%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>182.26 (n/a)</td><td>174.70 (n/a)</td><td>148.10 (n/a)</td><td>27.13 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 <b>(+21.00%)</b></td><td>0.05 (+4.60%)</td><td>0.04 (-8.27%)</td><td>0.04 (+16.23%)</td><td>0.01 <b>(+41.46%)</b></td><td>217.50 (-13.96%)</td><td>185.66 (-3.32%)</td><td>206.30 (+9.04%)</td><td>126.00 (-17.38%)</td><td>37.44 (-1.96%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.80 (n/a)</td><td>192.04 (n/a)</td><td>189.20 (n/a)</td><td>152.50 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.18 (-0.00%)</td><td>0.18 (+0.02%)</td><td>0.18 (+0.16%)</td><td>0.18 (+0.03%)</td><td>0.00 (-9.70%)</td><td>47606.70 (-0.03%)</td><td>47527.80 (-0.02%)</td><td>47502.50 (-0.16%)</td><td>47436.00 (+0.00%)</td><td>75.30 (-9.63%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47619.30 (n/a)</td><td>47537.18 (n/a)</td><td>47576.90 (n/a)</td><td>47434.30 (n/a)</td><td>83.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.16 (-16.21%)</td><td>0.14 (-5.92%)</td><td>0.15 (+2.10%)</td><td>0.13 (+10.49%)</td><td>0.01 <b>(-64.75%)</b></td><td>189.10 (-9.48%)</td><td>170.50 (+3.11%)</td><td>169.20 (-2.03%)</td><td>152.40 (+19.34%)</td><td>13.45 <b>(-60.76%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>208.90 (n/a)</td><td>165.36 (n/a)</td><td>172.70 (n/a)</td><td>127.70 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.24 (-10.32%)</td><td>0.21 (-6.03%)</td><td>0.20 (-11.31%)</td><td>0.19 (+2.86%)</td><td>0.02 <b>(-28.26%)</b></td><td>217.20 (-2.78%)</td><td>195.76 (+5.60%)</td><td>202.80 (+12.73%)</td><td>169.10 (+11.47%)</td><td>21.11 <b>(-22.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>223.40 (n/a)</td><td>185.38 (n/a)</td><td>179.90 (n/a)</td><td>151.70 (n/a)</td><td>27.26 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-1.64%)</td><td>0.03 (-6.16%)</td><td>0.03 (-5.15%)</td><td>0.03 (-10.68%)</td><td>0.00 <b>(+46.30%)</b></td><td>200.00 (+11.98%)</td><td>178.30 (+6.95%)</td><td>178.50 (+5.43%)</td><td>156.80 (+1.62%)</td><td>15.51 <b>(+67.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>166.72 (n/a)</td><td>169.30 (n/a)</td><td>154.30 (n/a)</td><td>9.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 <b>(+22.08%)</b></td><td>0.06 (+15.30%)</td><td>0.06 <b>(+24.57%)</b></td><td>0.04 (-14.90%)</td><td>0.01 <b>(+74.41%)</b></td><td>230.20 (+17.51%)</td><td>152.52 (-9.93%)</td><td>139.10 (-19.69%)</td><td>112.20 (-18.04%)</td><td>45.24 <b>(+76.51%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>169.34 (n/a)</td><td>173.20 (n/a)</td><td>136.90 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (-19.05%)</td><td>0.07 (-5.58%)</td><td>0.07 (-10.93%)</td><td>0.06 <b>(+37.55%)</b></td><td>0.01 <b>(-61.75%)</b></td><td>203.90 <b>(-27.31%)</b></td><td>181.52 (-0.50%)</td><td>180.50 (+12.25%)</td><td>153.70 <b>(+23.55%)</b></td><td>19.57 <b>(-67.03%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>280.50 (n/a)</td><td>182.44 (n/a)</td><td>160.80 (n/a)</td><td>124.40 (n/a)</td><td>59.36 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-0.75%)</td><td>0.05 (+5.19%)</td><td>0.05 (+7.75%)</td><td>0.05 (+15.65%)</td><td>0.00 <b>(-55.61%)</b></td><td>165.40 (-13.54%)</td><td>153.80 (-6.36%)</td><td>151.90 (-7.21%)</td><td>140.70 (+0.79%)</td><td>9.61 <b>(-60.90%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>164.24 (n/a)</td><td>163.70 (n/a)</td><td>139.60 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 <b>(-25.46%)</b></td><td>0.06 (-16.30%)</td><td>0.05 <b>(-25.41%)</b></td><td>0.05 (+0.41%)</td><td>0.01 <b>(-53.39%)</b></td><td>191.30 (-0.42%)</td><td>175.02 (+16.73%)</td><td>186.20 <b>(+34.05%)</b></td><td>152.00 <b>(+34.16%)</b></td><td>18.86 <b>(-38.20%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>149.94 (n/a)</td><td>138.90 (n/a)</td><td>113.30 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 <b>(+34.85%)</b></td><td>0.05 <b>(+35.06%)</b></td><td>0.05 <b>(+38.27%)</b></td><td>0.04 <b>(+27.60%)</b></td><td>0.01 <b>(+29.89%)</b></td><td>219.00 <b>(-21.65%)</b></td><td>165.82 <b>(-26.05%)</b></td><td>162.90 <b>(-27.66%)</b></td><td>120.80 <b>(-25.89%)</b></td><td>35.00 <b>(-24.58%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.50 (n/a)</td><td>224.24 (n/a)</td><td>225.20 (n/a)</td><td>163.00 (n/a)</td><td>46.40 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 <b>(-21.56%)</b></td><td>0.06 (-8.17%)</td><td>0.06 (-9.25%)</td><td>0.05 (+3.40%)</td><td>0.01 <b>(-52.60%)</b></td><td>195.50 (-3.27%)</td><td>162.80 (+5.56%)</td><td>159.10 (+10.18%)</td><td>137.60 <b>(+27.41%)</b></td><td>20.96 <b>(-40.42%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>154.22 (n/a)</td><td>144.40 (n/a)</td><td>108.00 (n/a)</td><td>35.18 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (+12.62%)</td><td>0.05 (+4.47%)</td><td>0.04 (-14.33%)</td><td>0.04 <b>(+31.67%)</b></td><td>0.01 (-0.18%)</td><td>194.40 <b>(-24.06%)</b></td><td>166.62 (-5.88%)</td><td>185.20 (+16.70%)</td><td>118.60 (-11.16%)</td><td>34.92 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>256.00 (n/a)</td><td>177.02 (n/a)</td><td>158.70 (n/a)</td><td>133.50 (n/a)</td><td>50.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (-3.54%)</td><td>0.06 (-8.06%)</td><td>0.05 <b>(-22.25%)</b></td><td>0.05 (+13.53%)</td><td>0.01 (-16.55%)</td><td>197.00 (-11.90%)</td><td>172.36 (+7.03%)</td><td>188.50 <b>(+28.58%)</b></td><td>126.10 (+3.62%)</td><td>30.12 <b>(-24.69%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.60 (n/a)</td><td>161.04 (n/a)</td><td>146.60 (n/a)</td><td>121.70 (n/a)</td><td>39.99 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (+0.70%)</td><td>0.05 (+7.32%)</td><td>0.05 (+14.72%)</td><td>0.04 <b>(+32.09%)</b></td><td>0.01 <b>(-37.62%)</b></td><td>185.80 <b>(-24.29%)</b></td><td>167.20 (-10.99%)</td><td>173.50 (-12.81%)</td><td>126.50 (-0.71%)</td><td>23.92 <b>(-53.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.40 (n/a)</td><td>187.84 (n/a)</td><td>199.00 (n/a)</td><td>127.40 (n/a)</td><td>51.32 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (-18.12%)</td><td>0.05 (+0.11%)</td><td>0.05 (-4.77%)</td><td>0.05 <b>(+24.56%)</b></td><td>0.01 <b>(-56.00%)</b></td><td>196.80 (-19.71%)</td><td>179.94 (-4.58%)</td><td>190.40 (+5.02%)</td><td>149.80 <b>(+22.19%)</b></td><td>20.90 <b>(-56.13%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>245.10 (n/a)</td><td>188.58 (n/a)</td><td>181.30 (n/a)</td><td>122.60 (n/a)</td><td>47.64 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (-18.89%)</td><td>0.05 (-11.83%)</td><td>0.05 <b>(-20.61%)</b></td><td>0.04 <b>(+23.36%)</b></td><td>0.00 <b>(-66.48%)</b></td><td>196.40 (-18.94%)</td><td>178.78 (+8.46%)</td><td>181.00 <b>(+25.96%)</b></td><td>157.90 <b>(+23.26%)</b></td><td>14.78 <b>(-67.70%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>164.84 (n/a)</td><td>143.70 (n/a)</td><td>128.10 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (+5.07%)</td><td>0.04 (+5.07%)</td><td>0.04 (+12.01%)</td><td>0.03 (-7.34%)</td><td>0.01 <b>(+24.69%)</b></td><td>289.60 (+7.94%)</td><td>209.40 (-3.58%)</td><td>196.10 (-10.70%)</td><td>168.90 (-4.85%)</td><td>46.39 <b>(+34.64%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>268.30 (n/a)</td><td>217.18 (n/a)</td><td>219.60 (n/a)</td><td>177.50 (n/a)</td><td>34.46 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 <b>(-30.37%)</b></td><td>0.04 <b>(-25.39%)</b></td><td>0.04 (-14.93%)</td><td>0.03 <b>(-39.91%)</b></td><td>0.01 (+1.61%)</td><td>319.60 <b>(+66.46%)</b></td><td>223.48 <b>(+36.97%)</b></td><td>198.30 (+17.55%)</td><td>195.80 <b>(+43.65%)</b></td><td>53.93 <b>(+148.04%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>192.00 (n/a)</td><td>163.16 (n/a)</td><td>168.70 (n/a)</td><td>136.30 (n/a)</td><td>21.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 <b>(+27.22%)</b></td><td>0.05 (+16.23%)</td><td>0.05 <b>(+22.24%)</b></td><td>0.04 (+15.59%)</td><td>0.01 <b>(+41.15%)</b></td><td>217.00 (-13.48%)</td><td>179.14 (-13.51%)</td><td>172.40 (-18.22%)</td><td>141.90 <b>(-21.39%)</b></td><td>27.86 (-2.80%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>207.12 (n/a)</td><td>210.80 (n/a)</td><td>180.50 (n/a)</td><td>28.66 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (-16.67%)</td><td>0.03 (-18.81%)</td><td>0.04 (-18.44%)</td><td>0.02 <b>(-25.83%)</b></td><td>0.01 (-6.45%)</td><td>328.80 <b>(+34.81%)</b></td><td>245.92 <b>(+24.23%)</b></td><td>225.90 <b>(+22.57%)</b></td><td>204.20 <b>(+20.05%)</b></td><td>49.50 <b>(+55.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.90 (n/a)</td><td>197.96 (n/a)</td><td>184.30 (n/a)</td><td>170.10 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.81 (+8.92%)</td><td>0.67 (-2.13%)</td><td>0.66 (-6.23%)</td><td>0.58 (-0.92%)</td><td>0.10 <b>(+55.37%)</b></td><td>170.40 (+0.95%)</td><td>149.54 (+3.09%)</td><td>148.70 (+6.67%)</td><td>120.90 (-8.13%)</td><td>20.51 <b>(+43.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.75 (n/a)</td><td>0.68 (n/a)</td><td>0.71 (n/a)</td><td>0.58 (n/a)</td><td>0.06 (n/a)</td><td>168.80 (n/a)</td><td>145.06 (n/a)</td><td>139.40 (n/a)</td><td>131.60 (n/a)</td><td>14.31 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.70 <b>(-23.14%)</b></td><td>0.56 (-15.87%)</td><td>0.56 <b>(-22.04%)</b></td><td>0.50 (+11.79%)</td><td>0.08 <b>(-55.64%)</b></td><td>197.00 (-10.54%)</td><td>176.66 (+13.33%)</td><td>175.50 <b>(+28.29%)</b></td><td>141.30 <b>(+30.11%)</b></td><td>22.79 <b>(-49.07%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.72 (n/a)</td><td>0.45 (n/a)</td><td>0.18 (n/a)</td><td>220.20 (n/a)</td><td>155.88 (n/a)</td><td>136.80 (n/a)</td><td>108.60 (n/a)</td><td>44.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.75 (-8.68%)</td><td>0.61 (-5.65%)</td><td>0.55 (-15.28%)</td><td>0.48 (+3.24%)</td><td>0.13 (-1.20%)</td><td>205.70 (-3.15%)</td><td>167.66 (+5.95%)</td><td>179.60 (+18.00%)</td><td>130.60 (+9.47%)</td><td>34.59 (-0.69%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.82 (n/a)</td><td>0.64 (n/a)</td><td>0.65 (n/a)</td><td>0.46 (n/a)</td><td>0.13 (n/a)</td><td>212.40 (n/a)</td><td>158.24 (n/a)</td><td>152.20 (n/a)</td><td>119.30 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.62 (-7.55%)</td><td>0.54 (+0.12%)</td><td>0.53 (-10.14%)</td><td>0.49 <b>(+34.62%)</b></td><td>0.05 <b>(-60.60%)</b></td><td>198.90 <b>(-25.70%)</b></td><td>182.56 (-3.87%)</td><td>185.50 (+11.28%)</td><td>159.30 (+8.15%)</td><td>14.54 <b>(-69.55%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.67 (n/a)</td><td>0.54 (n/a)</td><td>0.59 (n/a)</td><td>0.37 (n/a)</td><td>0.12 (n/a)</td><td>267.70 (n/a)</td><td>189.90 (n/a)</td><td>166.70 (n/a)</td><td>147.30 (n/a)</td><td>47.75 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.58 (-9.65%)</td><td>0.48 (-6.84%)</td><td>0.52 (+0.73%)</td><td>0.35 (-12.23%)</td><td>0.10 (+8.92%)</td><td>208.80 (+13.91%)</td><td>158.00 (+8.59%)</td><td>142.40 (-0.70%)</td><td>127.00 (+10.63%)</td><td>34.79 <b>(+36.36%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.64 (n/a)</td><td>0.52 (n/a)</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.09 (n/a)</td><td>183.30 (n/a)</td><td>145.50 (n/a)</td><td>143.40 (n/a)</td><td>114.80 (n/a)</td><td>25.52 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.56 (-8.60%)</td><td>0.45 (-9.03%)</td><td>0.47 (-7.19%)</td><td>0.35 (-4.51%)</td><td>0.09 (-0.04%)</td><td>208.20 (+4.73%)</td><td>168.86 (+10.54%)</td><td>156.10 (+7.73%)</td><td>131.20 (+9.42%)</td><td>36.10 (+17.71%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.09 (n/a)</td><td>198.80 (n/a)</td><td>152.76 (n/a)</td><td>144.90 (n/a)</td><td>119.90 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.50 <b>(-21.27%)</b></td><td>0.43 (-14.50%)</td><td>0.43 (-16.72%)</td><td>0.37 (-9.33%)</td><td>0.05 <b>(-46.40%)</b></td><td>197.80 (+10.32%)</td><td>171.76 (+15.26%)</td><td>173.30 <b>(+20.10%)</b></td><td>148.50 <b>(+27.03%)</b></td><td>19.08 <b>(-26.26%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.09 (n/a)</td><td>179.30 (n/a)</td><td>149.02 (n/a)</td><td>144.30 (n/a)</td><td>116.90 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.43 (-19.84%)</td><td>0.33 <b>(-31.28%)</b></td><td>0.32 <b>(-31.31%)</b></td><td>0.23 <b>(-46.78%)</b></td><td>0.07 <b>(+74.49%)</b></td><td>314.80 <b>(+87.94%)</b></td><td>232.54 <b>(+50.45%)</b></td><td>227.90 <b>(+45.53%)</b></td><td>169.60 <b>(+24.80%)</b></td><td>52.45 <b>(+313.94%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.04 (n/a)</td><td>167.50 (n/a)</td><td>154.56 (n/a)</td><td>156.60 (n/a)</td><td>135.90 (n/a)</td><td>12.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.03 <b>(+42.41%)</b></td><td>0.81 <b>(+32.19%)</b></td><td>0.78 <b>(+39.35%)</b></td><td>0.67 <b>(+20.32%)</b></td><td>0.14 <b>(+77.78%)</b></td><td>196.70 (-16.90%)</td><td>165.36 <b>(-23.68%)</b></td><td>167.00 <b>(-28.26%)</b></td><td>127.30 <b>(-29.75%)</b></td><td>25.26 (-0.15%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.72 (n/a)</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.08 (n/a)</td><td>236.70 (n/a)</td><td>216.66 (n/a)</td><td>232.80 (n/a)</td><td>181.20 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.21 <b>(+67.06%)</b></td><td>0.94 <b>(+40.15%)</b></td><td>0.90 <b>(+31.46%)</b></td><td>0.77 <b>(+30.21%)</b></td><td>0.17 <b>(+213.77%)</b></td><td>171.30 <b>(-23.18%)</b></td><td>143.00 <b>(-27.41%)</b></td><td>144.90 <b>(-23.94%)</b></td><td>108.20 <b>(-40.12%)</b></td><td>22.71 <b>(+38.63%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.73 (n/a)</td><td>0.67 (n/a)</td><td>0.69 (n/a)</td><td>0.59 (n/a)</td><td>0.05 (n/a)</td><td>223.00 (n/a)</td><td>197.00 (n/a)</td><td>190.50 (n/a)</td><td>180.70 (n/a)</td><td>16.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.13 (+16.75%)</td><td>0.93 <b>(+31.23%)</b></td><td>0.87 <b>(+29.94%)</b></td><td>0.72 <b>(+41.39%)</b></td><td>0.17 (-5.21%)</td><td>183.10 <b>(-29.28%)</b></td><td>145.74 <b>(-25.56%)</b></td><td>151.10 <b>(-23.03%)</b></td><td>116.20 (-14.31%)</td><td>27.39 <b>(-43.67%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.97 (n/a)</td><td>0.71 (n/a)</td><td>0.67 (n/a)</td><td>0.51 (n/a)</td><td>0.18 (n/a)</td><td>258.90 (n/a)</td><td>195.78 (n/a)</td><td>196.30 (n/a)</td><td>135.60 (n/a)</td><td>48.62 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (+1.06%)</td><td>0.03 (+3.18%)</td><td>0.03 (-7.43%)</td><td>0.02 (+16.02%)</td><td>0.00 <b>(-40.99%)</b></td><td>189.90 (-13.80%)</td><td>149.68 (-7.18%)</td><td>142.50 (+8.04%)</td><td>123.30 (-1.04%)</td><td>24.59 <b>(-47.61%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.30 (n/a)</td><td>161.26 (n/a)</td><td>131.90 (n/a)</td><td>124.60 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (+3.57%)</td><td>0.03 (-4.46%)</td><td>0.02 (-5.83%)</td><td>0.02 (-6.82%)</td><td>0.00 <b>(+23.01%)</b></td><td>190.60 (+7.32%)</td><td>165.42 (+5.07%)</td><td>166.20 (+6.20%)</td><td>138.40 (-3.49%)</td><td>18.65 <b>(+27.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>157.44 (n/a)</td><td>156.50 (n/a)</td><td>143.40 (n/a)</td><td>14.61 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-4.04%)</td><td>0.02 (+18.06%)</td><td>0.02 (+7.80%)</td><td>0.02 <b>(+60.11%)</b></td><td>0.00 <b>(-38.11%)</b></td><td>216.90 <b>(-37.53%)</b></td><td>170.20 <b>(-21.66%)</b></td><td>174.20 (-7.24%)</td><td>134.80 (+4.25%)</td><td>32.15 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>347.20 (n/a)</td><td>217.26 (n/a)</td><td>187.80 (n/a)</td><td>129.30 (n/a)</td><td>82.38 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.01 (-4.06%)</td><td>0.80 (-8.05%)</td><td>0.77 (-15.14%)</td><td>0.68 (+6.01%)</td><td>0.13 <b>(-22.42%)</b></td><td>193.00 (-5.67%)</td><td>168.78 (+7.38%)</td><td>171.40 (+17.88%)</td><td>130.80 (+4.22%)</td><td>23.18 <b>(-26.81%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.05 (n/a)</td><td>0.87 (n/a)</td><td>0.91 (n/a)</td><td>0.65 (n/a)</td><td>0.16 (n/a)</td><td>204.60 (n/a)</td><td>157.18 (n/a)</td><td>145.40 (n/a)</td><td>125.50 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.99 (+9.86%)</td><td>0.76 (-5.67%)</td><td>0.71 (-12.70%)</td><td>0.64 (-6.52%)</td><td>0.14 <b>(+63.03%)</b></td><td>207.10 (+6.97%)</td><td>179.06 (+7.53%)</td><td>187.00 (+14.58%)</td><td>132.90 (-8.97%)</td><td>28.51 <b>(+53.99%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.91 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.68 (n/a)</td><td>0.09 (n/a)</td><td>193.60 (n/a)</td><td>166.52 (n/a)</td><td>163.20 (n/a)</td><td>146.00 (n/a)</td><td>18.51 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.68 (-13.76%)</td><td>0.65 (-8.10%)</td><td>0.65 (-10.47%)</td><td>0.57 (-1.56%)</td><td>0.04 <b>(-45.38%)</b></td><td>230.90 (+1.58%)</td><td>205.26 (+8.01%)</td><td>201.70 (+11.68%)</td><td>193.20 (+15.97%)</td><td>15.12 <b>(-35.90%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.79 (n/a)</td><td>0.70 (n/a)</td><td>0.73 (n/a)</td><td>0.58 (n/a)</td><td>0.08 (n/a)</td><td>227.30 (n/a)</td><td>190.04 (n/a)</td><td>180.60 (n/a)</td><td>166.60 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.96 (+5.83%)</td><td>0.81 (+9.60%)</td><td>0.87 <b>(+23.78%)</b></td><td>0.63 (-3.45%)</td><td>0.14 <b>(+38.35%)</b></td><td>208.50 (+3.58%)</td><td>166.30 (-7.70%)</td><td>151.50 (-19.20%)</td><td>137.20 (-5.51%)</td><td>29.76 <b>(+39.72%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.91 (n/a)</td><td>0.74 (n/a)</td><td>0.70 (n/a)</td><td>0.66 (n/a)</td><td>0.10 (n/a)</td><td>201.30 (n/a)</td><td>180.18 (n/a)</td><td>187.50 (n/a)</td><td>145.20 (n/a)</td><td>21.30 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.95 (-10.22%)</td><td>0.84 (-1.42%)</td><td>0.87 (+16.83%)</td><td>0.68 (+0.58%)</td><td>0.12 <b>(-37.21%)</b></td><td>193.10 (-0.57%)</td><td>159.04 (-0.56%)</td><td>152.40 (-14.38%)</td><td>138.70 (+11.41%)</td><td>23.42 <b>(-28.68%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>1.06 (n/a)</td><td>0.86 (n/a)</td><td>0.74 (n/a)</td><td>0.68 (n/a)</td><td>0.19 (n/a)</td><td>194.20 (n/a)</td><td>159.94 (n/a)</td><td>178.00 (n/a)</td><td>124.50 (n/a)</td><td>32.84 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (+3.72%)</td><td>0.02 (-2.16%)</td><td>0.03 (+1.88%)</td><td>0.01 <b>(-27.34%)</b></td><td>0.01 <b>(+66.63%)</b></td><td>284.80 <b>(+37.65%)</b></td><td>179.46 (+7.35%)</td><td>162.20 (-1.82%)</td><td>137.70 (-3.57%)</td><td>59.98 <b>(+133.70%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>167.18 (n/a)</td><td>165.20 (n/a)</td><td>142.80 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (-17.49%)</td><td>0.02 (-11.46%)</td><td>0.02 (-9.77%)</td><td>0.02 (-15.10%)</td><td>0.00 <b>(-27.00%)</b></td><td>209.70 (+17.74%)</td><td>179.58 (+12.59%)</td><td>182.30 (+10.89%)</td><td>152.00 <b>(+21.21%)</b></td><td>21.44 (+7.33%)</td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>159.50 (n/a)</td><td>164.40 (n/a)</td><td>125.40 (n/a)</td><td>19.98 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.00 (+2.27%)</td><td>0.00 (-0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+16.50%)</td><td>1021.27 (-0.58%)</td><td>970.59 (+0.35%)</td><td>962.28 (+1.17%)</td><td>903.26 (-3.58%)</td><td>46.69 <b>(+22.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1027.22 (n/a)</td><td>967.25 (n/a)</td><td>951.11 (n/a)</td><td>936.75 (n/a)</td><td>38.11 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.01 (+2.38%)</td><td>0.01 (+2.76%)</td><td>0.01 (+7.50%)</td><td>0.01 (-4.05%)</td><td>0.00 <b>(+79.44%)</b></td><td>1157.57 (+5.01%)</td><td>1005.69 (-1.85%)</td><td>956.33 (-6.25%)</td><td>952.56 (-2.06%)</td><td>88.03 <b>(+84.09%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1102.35 (n/a)</td><td>1024.64 (n/a)</td><td>1020.13 (n/a)</td><td>972.63 (n/a)</td><td>47.82 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.01 (+3.41%)</td><td>0.98 (+2.25%)</td><td>0.97 (+2.07%)</td><td>0.95 (+1.11%)</td><td>0.03 <b>(+68.18%)</b></td><td>2209.43 (-1.09%)</td><td>2147.04 (-2.17%)</td><td>2153.91 (-2.03%)</td><td>2069.37 (-3.30%)</td><td>55.18 <b>(+61.22%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.02 (n/a)</td><td>2233.84 (n/a)</td><td>2194.56 (n/a)</td><td>2198.47 (n/a)</td><td>2139.92 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>3.94 (+18.78%)</td><td>2.93 (+3.29%)</td><td>2.86 (+7.45%)</td><td>2.33 (-5.15%)</td><td>0.64 <b>(+67.75%)</b></td><td>224.90 (+5.44%)</td><td>185.02 (-1.15%)</td><td>183.00 (-6.92%)</td><td>132.90 (-15.83%)</td><td>36.60 <b>(+50.73%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.32 (n/a)</td><td>2.84 (n/a)</td><td>2.67 (n/a)</td><td>2.46 (n/a)</td><td>0.38 (n/a)</td><td>213.30 (n/a)</td><td>187.18 (n/a)</td><td>196.60 (n/a)</td><td>157.90 (n/a)</td><td>24.28 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.57 <b>(+21.16%)</b></td><td>4.55 (+8.92%)</td><td>4.29 (+5.70%)</td><td>4.01 (+5.22%)</td><td>0.61 <b>(+96.15%)</b></td><td>261.50 (-4.94%)</td><td>233.42 (-7.42%)</td><td>244.30 (-5.38%)</td><td>188.30 (-17.48%)</td><td>27.84 <b>(+51.39%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>4.60 (n/a)</td><td>4.18 (n/a)</td><td>4.06 (n/a)</td><td>3.81 (n/a)</td><td>0.31 (n/a)</td><td>275.10 (n/a)</td><td>252.12 (n/a)</td><td>258.20 (n/a)</td><td>228.20 (n/a)</td><td>18.39 (n/a)</td>
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
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.13 <b>(+25.97%)</b></td><td>2.76 (+8.51%)</td><td>2.61 (+4.47%)</td><td>2.14 (+3.64%)</td><td>0.80 <b>(+76.70%)</b></td><td>245.30 (-3.54%)</td><td>200.14 (-4.98%)</td><td>200.80 (-4.29%)</td><td>127.00 <b>(-20.62%)</b></td><td>46.14 <b>(+34.53%)</b></td>
</tr>
<tr>
<td><code>8354a4c</code> — 2026-09-12 01:13:36</td><td>3.28 (n/a)</td><td>2.55 (n/a)</td><td>2.50 (n/a)</td><td>2.06 (n/a)</td><td>0.45 (n/a)</td><td>254.30 (n/a)</td><td>210.62 (n/a)</td><td>209.80 (n/a)</td><td>160.00 (n/a)</td><td>34.30 (n/a)</td>
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
