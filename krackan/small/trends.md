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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (+1.85%)</td><td>0.08 (+5.67%)</td><td>0.08 (+1.03%)</td><td>0.07 (+8.60%)</td><td>0.01 <b>(-30.37%)</b></td><td>168.20 (-7.94%)</td><td>152.96 (-5.79%)</td><td>154.40 (-1.03%)</td><td>141.80 (-1.80%)</td><td>10.20 <b>(-37.76%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>182.70 (n/a)</td><td>162.36 (n/a)</td><td>156.00 (n/a)</td><td>144.40 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 <b>(-23.15%)</b></td><td>0.08 (-9.09%)</td><td>0.07 (-5.24%)</td><td>0.06 (-3.81%)</td><td>0.01 <b>(-51.84%)</b></td><td>191.20 (+3.97%)</td><td>163.52 (+6.85%)</td><td>169.60 (+5.54%)</td><td>135.90 <b>(+30.17%)</b></td><td>21.07 <b>(-35.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>183.90 (n/a)</td><td>153.04 (n/a)</td><td>160.70 (n/a)</td><td>104.40 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (-17.16%)</td><td>0.06 (-10.78%)</td><td>0.06 (-10.52%)</td><td>0.05 (-7.57%)</td><td>0.01 <b>(-30.25%)</b></td><td>237.80 (+8.19%)</td><td>193.34 (+10.95%)</td><td>189.10 (+11.76%)</td><td>156.50 <b>(+20.66%)</b></td><td>30.28 (-7.36%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>174.26 (n/a)</td><td>169.20 (n/a)</td><td>129.70 (n/a)</td><td>32.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.10 <b>(+37.01%)</b></td><td>0.07 <b>(+32.89%)</b></td><td>0.07 <b>(+30.31%)</b></td><td>0.06 <b>(+51.58%)</b></td><td>0.01 (+5.23%)</td><td>191.70 <b>(-34.03%)</b></td><td>171.76 <b>(-26.44%)</b></td><td>180.80 <b>(-23.29%)</b></td><td>124.80 <b>(-27.02%)</b></td><td>26.69 <b>(-51.63%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>290.60 (n/a)</td><td>233.50 (n/a)</td><td>235.70 (n/a)</td><td>171.00 (n/a)</td><td>55.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (-2.72%)</td><td>0.03 (-14.90%)</td><td>0.03 (-16.35%)</td><td>0.03 (-19.66%)</td><td>0.01 <b>(+32.21%)</b></td><td>194.60 <b>(+24.42%)</b></td><td>164.00 (+19.60%)</td><td>170.70 (+19.54%)</td><td>121.50 (+2.79%)</td><td>31.06 <b>(+74.96%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>156.40 (n/a)</td><td>137.12 (n/a)</td><td>142.80 (n/a)</td><td>118.20 (n/a)</td><td>17.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (+10.82%)</td><td>0.03 (+3.82%)</td><td>0.03 (+4.50%)</td><td>0.03 (+4.02%)</td><td>0.00 <b>(+45.95%)</b></td><td>199.20 (-3.86%)</td><td>174.54 (-3.17%)</td><td>171.30 (-4.30%)</td><td>149.00 (-9.75%)</td><td>20.61 <b>(+26.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>207.20 (n/a)</td><td>180.26 (n/a)</td><td>179.00 (n/a)</td><td>165.10 (n/a)</td><td>16.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (+14.25%)</td><td>0.04 (+3.65%)</td><td>0.04 (+0.42%)</td><td>0.03 (+0.75%)</td><td>0.01 <b>(+26.73%)</b></td><td>191.40 (-0.78%)</td><td>151.18 (-2.83%)</td><td>143.70 (-0.42%)</td><td>119.00 (-12.50%)</td><td>27.33 (+12.11%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>192.90 (n/a)</td><td>155.58 (n/a)</td><td>144.30 (n/a)</td><td>136.00 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (-13.16%)</td><td>0.03 (+1.48%)</td><td>0.03 (+12.46%)</td><td>0.03 (-4.89%)</td><td>0.01 <b>(-34.72%)</b></td><td>207.40 (+5.12%)</td><td>171.62 (-3.28%)</td><td>172.60 (-11.08%)</td><td>135.70 (+15.20%)</td><td>26.92 <b>(-20.23%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>177.44 (n/a)</td><td>194.10 (n/a)</td><td>117.80 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (+8.22%)</td><td>0.03 (-9.59%)</td><td>0.03 (-13.58%)</td><td>0.02 (-16.49%)</td><td>0.01 <b>(+57.61%)</b></td><td>224.70 (+19.78%)</td><td>179.18 (+14.36%)</td><td>181.00 (+15.73%)</td><td>112.90 (-7.53%)</td><td>41.39 <b>(+66.59%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>187.60 (n/a)</td><td>156.68 (n/a)</td><td>156.40 (n/a)</td><td>122.10 (n/a)</td><td>24.85 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (-2.05%)</td><td>0.03 (-13.13%)</td><td>0.03 (-14.90%)</td><td>0.02 (-10.59%)</td><td>0.01 (+10.98%)</td><td>249.90 (+11.86%)</td><td>198.78 (+16.18%)</td><td>194.50 (+17.52%)</td><td>140.50 (+2.11%)</td><td>40.20 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.40 (n/a)</td><td>171.10 (n/a)</td><td>165.50 (n/a)</td><td>137.60 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 <b>(-45.98%)</b></td><td>0.03 <b>(-25.74%)</b></td><td>0.03 (-9.48%)</td><td>0.02 <b>(-37.30%)</b></td><td>0.01 <b>(-54.76%)</b></td><td>270.50 <b>(+59.49%)</b></td><td>187.68 <b>(+32.04%)</b></td><td>165.70 (+10.47%)</td><td>159.40 <b>(+85.13%)</b></td><td>46.88 <b>(+44.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>169.60 (n/a)</td><td>142.14 (n/a)</td><td>150.00 (n/a)</td><td>86.10 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (+6.06%)</td><td>0.03 (-2.49%)</td><td>0.03 (-2.28%)</td><td>0.02 <b>(-26.40%)</b></td><td>0.01 <b>(+128.17%)</b></td><td>305.80 <b>(+35.85%)</b></td><td>210.18 (+6.68%)</td><td>191.60 (+2.30%)</td><td>168.50 (-5.71%)</td><td>56.22 <b>(+195.53%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>197.02 (n/a)</td><td>187.30 (n/a)</td><td>178.70 (n/a)</td><td>19.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>176.38 (n/a)</td><td>176.60 (n/a)</td><td>142.30 (n/a)</td><td>25.44 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>183.46 (n/a)</td><td>193.30 (n/a)</td><td>134.30 (n/a)</td><td>36.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.50 (n/a)</td><td>190.20 (n/a)</td><td>191.20 (n/a)</td><td>151.80 (n/a)</td><td>23.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>196.26 (n/a)</td><td>198.10 (n/a)</td><td>165.60 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.20 (n/a)</td><td>197.76 (n/a)</td><td>184.10 (n/a)</td><td>158.20 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>189.48 (n/a)</td><td>187.80 (n/a)</td><td>154.30 (n/a)</td><td>26.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.60 (n/a)</td><td>174.10 (n/a)</td><td>165.00 (n/a)</td><td>151.80 (n/a)</td><td>29.34 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>306.40 (n/a)</td><td>234.72 (n/a)</td><td>214.60 (n/a)</td><td>206.30 (n/a)</td><td>41.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>176.16 (n/a)</td><td>176.30 (n/a)</td><td>143.20 (n/a)</td><td>25.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>182.30 (n/a)</td><td>171.04 (n/a)</td><td>174.80 (n/a)</td><td>158.20 (n/a)</td><td>9.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>156.56 (n/a)</td><td>158.60 (n/a)</td><td>111.80 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.50 (n/a)</td><td>179.82 (n/a)</td><td>180.60 (n/a)</td><td>147.40 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.70 (n/a)</td><td>178.68 (n/a)</td><td>189.20 (n/a)</td><td>150.60 (n/a)</td><td>20.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>219.00 (n/a)</td><td>196.32 (n/a)</td><td>194.00 (n/a)</td><td>179.10 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.70 (n/a)</td><td>204.90 (n/a)</td><td>207.60 (n/a)</td><td>148.50 (n/a)</td><td>37.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.00 (n/a)</td><td>211.06 (n/a)</td><td>214.50 (n/a)</td><td>195.50 (n/a)</td><td>12.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.32 (+2.84%)</td><td>4.03 (+4.99%)</td><td>4.07 (+5.75%)</td><td>3.52 (+3.37%)</td><td>0.30 (-18.22%)</td><td>2672.50 (-3.26%)</td><td>2347.12 (-5.00%)</td><td>2309.90 (-5.44%)</td><td>2174.60 (-2.75%)</td><td>190.41 <b>(-20.93%)</b></td><td>1701.20 (+2.84%)</td><td>1583.85 (+4.99%)</td><td>1601.54 (+5.75%)</td><td>1384.25 (+3.37%)</td><td>119.02 (-18.22%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>4.21 (n/a)</td><td>3.84 (n/a)</td><td>3.85 (n/a)</td><td>3.40 (n/a)</td><td>0.37 (n/a)</td><td>2762.60 (n/a)</td><td>2470.76 (n/a)</td><td>2442.70 (n/a)</td><td>2236.20 (n/a)</td><td>240.79 (n/a)</td><td>1654.30 (n/a)</td><td>1508.60 (n/a)</td><td>1514.49 (n/a)</td><td>1339.10 (n/a)</td><td>145.53 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.10 (-0.21%)</td><td>0.90 (-2.88%)</td><td>0.96 (+0.29%)</td><td>0.70 (-4.18%)</td><td>0.17 <b>(+24.94%)</b></td><td>316.00 (+4.36%)</td><td>253.60 (+4.16%)</td><td>230.90 (-0.30%)</td><td>201.30 (+0.20%)</td><td>49.57 <b>(+31.24%)</b></td><td>46.88 (-0.21%)</td><td>38.33 (-2.88%)</td><td>40.88 (+0.29%)</td><td>29.87 (-4.18%)</td><td>7.20 <b>(+24.94%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.10 (n/a)</td><td>0.93 (n/a)</td><td>0.96 (n/a)</td><td>0.73 (n/a)</td><td>0.14 (n/a)</td><td>302.80 (n/a)</td><td>243.48 (n/a)</td><td>231.60 (n/a)</td><td>200.90 (n/a)</td><td>37.77 (n/a)</td><td>46.98 (n/a)</td><td>39.47 (n/a)</td><td>40.76 (n/a)</td><td>31.17 (n/a)</td><td>5.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.15 (+9.97%)</td><td>0.99 (+10.27%)</td><td>1.03 (+13.22%)</td><td>0.69 (+2.81%)</td><td>0.18 (+18.37%)</td><td>320.80 (-2.73%)</td><td>230.18 (-8.64%)</td><td>215.50 (-11.68%)</td><td>192.60 (-9.11%)</td><td>52.49 (+8.18%)</td><td>48.99 (+9.97%)</td><td>42.41 (+10.27%)</td><td>43.78 (+13.22%)</td><td>29.41 (+2.81%)</td><td>7.86 (+18.37%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td><td>0.91 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>329.80 (n/a)</td><td>251.96 (n/a)</td><td>244.00 (n/a)</td><td>211.90 (n/a)</td><td>48.52 (n/a)</td><td>44.55 (n/a)</td><td>38.47 (n/a)</td><td>38.67 (n/a)</td><td>28.61 (n/a)</td><td>6.64 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.53 (+1.42%)</td><td>0.53 (+1.42%)</td><td>0.53 (+1.40%)</td><td>0.53 (+1.56%)</td><td>0.00 <b>(-35.52%)</b></td><td>47905.70 (-1.54%)</td><td>47823.48 (-1.40%)</td><td>47797.00 (-1.38%)</td><td>47775.90 (-1.40%)</td><td>53.03 <b>(-37.44%)</b></td><td>359.59 (+1.42%)</td><td>359.24 (+1.42%)</td><td>359.43 (+1.40%)</td><td>358.62 (+1.56%)</td><td>0.40 <b>(-35.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48653.70 (n/a)</td><td>48502.76 (n/a)</td><td>48467.00 (n/a)</td><td>48456.60 (n/a)</td><td>84.77 (n/a)</td><td>354.54 (n/a)</td><td>354.20 (n/a)</td><td>354.46 (n/a)</td><td>353.11 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.91 (+1.22%)</td><td>0.90 (+1.52%)</td><td>0.90 (+1.63%)</td><td>0.90 (+1.81%)</td><td>0.00 <b>(-31.63%)</b></td><td>27915.10 (-1.78%)</td><td>27832.26 (-1.50%)</td><td>27887.30 (-1.61%)</td><td>27599.20 (-1.20%)</td><td>131.21 <b>(-33.68%)</b></td><td>622.48 (+1.22%)</td><td>617.28 (+1.52%)</td><td>616.05 (+1.63%)</td><td>615.43 (+1.81%)</td><td>2.93 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28420.40 (n/a)</td><td>28256.42 (n/a)</td><td>28342.30 (n/a)</td><td>27934.80 (n/a)</td><td>197.83 (n/a)</td><td>615.00 (n/a)</td><td>608.02 (n/a)</td><td>606.16 (n/a)</td><td>604.49 (n/a)</td><td>4.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.33 (+0.09%)</td><td>3.25 (+0.55%)</td><td>3.27 (+1.84%)</td><td>3.15 (+0.62%)</td><td>0.07 (-18.50%)</td><td>7993.00 (-0.62%)</td><td>7742.12 (-0.57%)</td><td>7707.10 (-1.80%)</td><td>7560.40 (-0.09%)</td><td>160.50 (-18.56%)</td><td>2272.36 (+0.09%)</td><td>2219.77 (+0.55%)</td><td>2229.11 (+1.84%)</td><td>2149.37 (+0.62%)</td><td>45.50 (-18.50%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.33 (n/a)</td><td>3.23 (n/a)</td><td>3.21 (n/a)</td><td>3.13 (n/a)</td><td>0.08 (n/a)</td><td>8042.70 (n/a)</td><td>7786.20 (n/a)</td><td>7848.70 (n/a)</td><td>7566.90 (n/a)</td><td>197.07 (n/a)</td><td>2270.41 (n/a)</td><td>2207.59 (n/a)</td><td>2188.89 (n/a)</td><td>2136.09 (n/a)</td><td>55.83 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.17 (+15.30%)</td><td>3.66 (+4.09%)</td><td>3.68 (+2.84%)</td><td>3.11 (-4.20%)</td><td>0.37 <b>(+147.15%)</b></td><td>2590.00 (+4.38%)</td><td>2221.24 (-3.25%)</td><td>2190.20 (-2.77%)</td><td>1935.20 (-13.27%)</td><td>234.73 <b>(+124.88%)</b></td><td>1092.37 (+15.30%)</td><td>959.92 (+4.09%)</td><td>965.17 (+2.84%)</td><td>816.19 (-4.20%)</td><td>97.85 <b>(+147.15%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>3.58 (n/a)</td><td>3.25 (n/a)</td><td>0.15 (n/a)</td><td>2481.30 (n/a)</td><td>2295.78 (n/a)</td><td>2252.50 (n/a)</td><td>2231.20 (n/a)</td><td>104.38 (n/a)</td><td>947.43 (n/a)</td><td>922.23 (n/a)</td><td>938.48 (n/a)</td><td>851.96 (n/a)</td><td>39.59 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.49 <b>(+50.69%)</b></td><td>0.36 (+17.26%)</td><td>0.33 (+6.61%)</td><td>0.32 (+15.15%)</td><td>0.07 <b>(+285.51%)</b></td><td>3836.00 (-13.15%)</td><td>3525.38 (-12.76%)</td><td>3760.60 (-6.20%)</td><td>2531.80 <b>(-33.64%)</b></td><td>559.38 <b>(+121.20%)</b></td><td>26.51 <b>(+50.69%)</b></td><td>19.53 (+17.26%)</td><td>17.85 (+6.61%)</td><td>17.49 (+15.15%)</td><td>3.91 <b>(+285.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>4416.90 (n/a)</td><td>4041.16 (n/a)</td><td>4009.00 (n/a)</td><td>3815.10 (n/a)</td><td>252.88 (n/a)</td><td>17.59 (n/a)</td><td>16.66 (n/a)</td><td>16.74 (n/a)</td><td>15.19 (n/a)</td><td>1.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>4.12 <b>(-35.44%)</b></td><td>3.68 <b>(-23.21%)</b></td><td>3.73 <b>(-21.62%)</b></td><td>3.36 (+3.79%)</td><td>0.31 <b>(-72.61%)</b></td><td>1978.60 (-3.65%)</td><td>1817.00 <b>(+24.94%)</b></td><td>1781.00 <b>(+27.59%)</b></td><td>1613.90 <b>(+54.90%)</b></td><td>147.86 <b>(-59.89%)</b></td><td>1273.42 <b>(-35.44%)</b></td><td>1137.24 <b>(-23.21%)</b></td><td>1153.96 <b>(-21.62%)</b></td><td>1038.74 (+3.79%)</td><td>94.42 <b>(-72.61%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>6.38 (n/a)</td><td>4.79 (n/a)</td><td>4.77 (n/a)</td><td>3.24 (n/a)</td><td>1.12 (n/a)</td><td>2053.50 (n/a)</td><td>1454.30 (n/a)</td><td>1395.90 (n/a)</td><td>1041.90 (n/a)</td><td>368.60 (n/a)</td><td>1972.59 (n/a)</td><td>1480.94 (n/a)</td><td>1472.32 (n/a)</td><td>1000.84 (n/a)</td><td>344.74 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>13.14 (n/a)</td><td>12.24 (n/a)</td><td>12.15 (n/a)</td><td>11.10 (n/a)</td><td>0.77 (n/a)</td><td>13.13 (n/a)</td><td>12.23 (n/a)</td><td>12.14 (n/a)</td><td>11.09 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>24.82 (-2.18%)</td><td>24.58 (+1.32%)</td><td>24.63 (+2.52%)</td><td>24.18 (+1.98%)</td><td>0.25 <b>(-62.57%)</b></td><td>24.80 (-2.18%)</td><td>24.56 (+1.32%)</td><td>24.61 (+2.52%)</td><td>24.17 (+1.98%)</td><td>0.24 <b>(-62.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>25.37 (n/a)</td><td>24.26 (n/a)</td><td>24.02 (n/a)</td><td>23.71 (n/a)</td><td>0.65 (n/a)</td><td>25.36 (n/a)</td><td>24.24 (n/a)</td><td>24.01 (n/a)</td><td>23.70 (n/a)</td><td>0.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>43.50 (+7.58%)</td><td>41.50 (+4.55%)</td><td>41.19 (+3.42%)</td><td>39.62 (+2.17%)</td><td>1.44 <b>(+139.49%)</b></td><td>43.48 (+7.58%)</td><td>41.48 (+4.55%)</td><td>41.17 (+3.42%)</td><td>39.60 (+2.17%)</td><td>1.44 <b>(+139.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>40.44 (n/a)</td><td>39.70 (n/a)</td><td>39.83 (n/a)</td><td>38.78 (n/a)</td><td>0.60 (n/a)</td><td>40.41 (n/a)</td><td>39.67 (n/a)</td><td>39.80 (n/a)</td><td>38.76 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>45.41 (+0.34%)</td><td>42.38 (-1.56%)</td><td>42.18 (-1.57%)</td><td>37.69 (-9.26%)</td><td>2.99 <b>(+120.93%)</b></td><td>45.38 (+0.34%)</td><td>42.36 (-1.56%)</td><td>42.16 (-1.57%)</td><td>37.67 (-9.26%)</td><td>2.99 <b>(+120.93%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>45.26 (n/a)</td><td>43.06 (n/a)</td><td>42.86 (n/a)</td><td>41.54 (n/a)</td><td>1.36 (n/a)</td><td>45.23 (n/a)</td><td>43.03 (n/a)</td><td>42.83 (n/a)</td><td>41.51 (n/a)</td><td>1.35 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>13.37 (n/a)</td><td>12.19 (n/a)</td><td>12.08 (n/a)</td><td>10.77 (n/a)</td><td>1.10 (n/a)</td><td>13.36 (n/a)</td><td>12.18 (n/a)</td><td>12.07 (n/a)</td><td>10.76 (n/a)</td><td>1.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>25.03 (+0.47%)</td><td>23.99 (+7.40%)</td><td>24.23 (+1.46%)</td><td>23.11 <b>(+48.08%)</b></td><td>0.79 <b>(-79.29%)</b></td><td>25.02 (+0.47%)</td><td>23.97 (+7.40%)</td><td>24.21 (+1.46%)</td><td>23.10 <b>(+48.08%)</b></td><td>0.79 <b>(-79.29%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>24.91 (n/a)</td><td>22.33 (n/a)</td><td>23.88 (n/a)</td><td>15.61 (n/a)</td><td>3.81 (n/a)</td><td>24.90 (n/a)</td><td>22.32 (n/a)</td><td>23.87 (n/a)</td><td>15.60 (n/a)</td><td>3.81 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>41.88 (+1.88%)</td><td>39.87 (+0.27%)</td><td>39.94 (-0.34%)</td><td>37.98 (+0.47%)</td><td>1.56 (+6.18%)</td><td>41.85 (+1.88%)</td><td>39.84 (+0.27%)</td><td>39.92 (-0.34%)</td><td>37.96 (+0.47%)</td><td>1.56 (+6.18%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>41.11 (n/a)</td><td>39.76 (n/a)</td><td>40.08 (n/a)</td><td>37.80 (n/a)</td><td>1.47 (n/a)</td><td>41.08 (n/a)</td><td>39.74 (n/a)</td><td>40.05 (n/a)</td><td>37.78 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>46.05 (+2.06%)</td><td>41.26 (-5.35%)</td><td>42.01 (-3.93%)</td><td>36.53 (-13.23%)</td><td>3.52 <b>(+196.96%)</b></td><td>46.02 (+2.06%)</td><td>41.23 (-5.35%)</td><td>41.98 (-3.93%)</td><td>36.51 (-13.23%)</td><td>3.52 <b>(+196.96%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>45.12 (n/a)</td><td>43.59 (n/a)</td><td>43.73 (n/a)</td><td>42.10 (n/a)</td><td>1.19 (n/a)</td><td>45.09 (n/a)</td><td>43.57 (n/a)</td><td>43.70 (n/a)</td><td>42.08 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>9.42 (-2.25%)</td><td>9.01 (-0.14%)</td><td>9.21 (+0.50%)</td><td>8.40 (+0.13%)</td><td>0.44 (-6.24%)</td><td>9.40 (-2.25%)</td><td>8.99 (-0.14%)</td><td>9.19 (+0.50%)</td><td>8.38 (+0.13%)</td><td>0.44 (-6.24%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>9.64 (n/a)</td><td>9.02 (n/a)</td><td>9.16 (n/a)</td><td>8.39 (n/a)</td><td>0.47 (n/a)</td><td>9.62 (n/a)</td><td>9.00 (n/a)</td><td>9.14 (n/a)</td><td>8.37 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.96 (-11.58%)</td><td>0.86 (-2.07%)</td><td>0.86 (-4.47%)</td><td>0.72 <b>(+46.82%)</b></td><td>0.09 <b>(-61.49%)</b></td><td>0.95 (-11.58%)</td><td>0.85 (-2.07%)</td><td>0.84 (-4.47%)</td><td>0.71 <b>(+46.82%)</b></td><td>0.09 <b>(-61.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.09 (n/a)</td><td>0.88 (n/a)</td><td>0.90 (n/a)</td><td>0.49 (n/a)</td><td>0.24 (n/a)</td><td>1.07 (n/a)</td><td>0.87 (n/a)</td><td>0.88 (n/a)</td><td>0.48 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.47 (+12.87%)</td><td>1.19 (-1.38%)</td><td>1.17 (-3.62%)</td><td>0.99 (-9.78%)</td><td>0.18 <b>(+139.11%)</b></td><td>1.45 (+12.87%)</td><td>1.17 (-1.38%)</td><td>1.16 (-3.62%)</td><td>0.98 (-9.78%)</td><td>0.18 <b>(+139.11%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.30 (n/a)</td><td>1.20 (n/a)</td><td>1.22 (n/a)</td><td>1.10 (n/a)</td><td>0.07 (n/a)</td><td>1.29 (n/a)</td><td>1.19 (n/a)</td><td>1.20 (n/a)</td><td>1.09 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>18.40 (-4.72%)</td><td>17.92 (+0.19%)</td><td>18.01 (-2.49%)</td><td>17.29 (+11.15%)</td><td>0.51 <b>(-66.58%)</b></td><td>18.19 (-4.72%)</td><td>17.71 (+0.19%)</td><td>17.80 (-2.49%)</td><td>17.09 (+11.15%)</td><td>0.50 <b>(-66.58%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>19.31 (n/a)</td><td>17.88 (n/a)</td><td>18.47 (n/a)</td><td>15.56 (n/a)</td><td>1.52 (n/a)</td><td>19.09 (n/a)</td><td>17.68 (n/a)</td><td>18.25 (n/a)</td><td>15.38 (n/a)</td><td>1.50 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>14.30 (+3.65%)</td><td>13.64 (+2.48%)</td><td>13.37 (+0.36%)</td><td>13.21 (+4.89%)</td><td>0.47 (-6.64%)</td><td>14.05 (+3.65%)</td><td>13.40 (+2.48%)</td><td>13.14 (+0.36%)</td><td>12.98 (+4.89%)</td><td>0.46 (-6.64%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>13.79 (n/a)</td><td>13.31 (n/a)</td><td>13.32 (n/a)</td><td>12.59 (n/a)</td><td>0.50 (n/a)</td><td>13.55 (n/a)</td><td>13.08 (n/a)</td><td>13.09 (n/a)</td><td>12.37 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>8.93 (+5.93%)</td><td>7.72 (-0.21%)</td><td>7.78 (-2.74%)</td><td>5.21 <b>(-26.07%)</b></td><td>1.52 <b>(+159.49%)</b></td><td>8.78 (+5.93%)</td><td>7.59 (-0.21%)</td><td>7.64 (-2.74%)</td><td>5.12 <b>(-26.07%)</b></td><td>1.49 <b>(+159.49%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>8.43 (n/a)</td><td>7.74 (n/a)</td><td>8.00 (n/a)</td><td>7.05 (n/a)</td><td>0.58 (n/a)</td><td>8.29 (n/a)</td><td>7.60 (n/a)</td><td>7.86 (n/a)</td><td>6.92 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>6.57 (-7.18%)</td><td>5.47 (-11.91%)</td><td>5.53 (-7.47%)</td><td>4.29 <b>(-20.96%)</b></td><td>0.87 <b>(+20.92%)</b></td><td>6.47 (-7.18%)</td><td>5.38 (-11.91%)</td><td>5.44 (-7.47%)</td><td>4.22 <b>(-20.96%)</b></td><td>0.86 <b>(+20.92%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>7.08 (n/a)</td><td>6.21 (n/a)</td><td>5.97 (n/a)</td><td>5.43 (n/a)</td><td>0.72 (n/a)</td><td>6.97 (n/a)</td><td>6.11 (n/a)</td><td>5.88 (n/a)</td><td>5.34 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>13.25 (n/a)</td><td>11.79 (n/a)</td><td>11.47 (n/a)</td><td>10.45 (n/a)</td><td>1.09 (n/a)</td><td>13.24 (n/a)</td><td>11.78 (n/a)</td><td>11.46 (n/a)</td><td>10.45 (n/a)</td><td>1.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>13.16 (n/a)</td><td>12.76 (n/a)</td><td>12.79 (n/a)</td><td>12.18 (n/a)</td><td>0.38 (n/a)</td><td>13.15 (n/a)</td><td>12.75 (n/a)</td><td>12.78 (n/a)</td><td>12.17 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.80 (n/a)</td><td>153.94 (n/a)</td><td>146.40 (n/a)</td><td>137.70 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.30 (n/a)</td><td>165.24 (n/a)</td><td>167.40 (n/a)</td><td>155.50 (n/a)</td><td>7.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>177.48 (n/a)</td><td>174.30 (n/a)</td><td>156.90 (n/a)</td><td>17.02 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>167.28 (n/a)</td><td>160.00 (n/a)</td><td>145.10 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>168.76 (n/a)</td><td>156.30 (n/a)</td><td>146.80 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.50 (n/a)</td><td>182.22 (n/a)</td><td>168.30 (n/a)</td><td>160.10 (n/a)</td><td>34.25 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>245.10 (n/a)</td><td>168.46 (n/a)</td><td>151.10 (n/a)</td><td>140.30 (n/a)</td><td>43.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>258.30 (n/a)</td><td>207.74 (n/a)</td><td>192.30 (n/a)</td><td>153.80 (n/a)</td><td>46.28 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-13.08%)</td><td>0.05 (-14.68%)</td><td>0.05 (-10.17%)</td><td>0.04 <b>(-26.50%)</b></td><td>0.01 <b>(+101.59%)</b></td><td>215.10 <b>(+36.05%)</b></td><td>176.36 (+18.41%)</td><td>165.40 (+11.38%)</td><td>159.70 (+15.06%)</td><td>22.85 <b>(+218.91%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>158.10 (n/a)</td><td>148.94 (n/a)</td><td>148.50 (n/a)</td><td>138.80 (n/a)</td><td>7.16 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-7.53%)</td><td>0.05 (+13.41%)</td><td>0.05 (+14.17%)</td><td>0.04 <b>(+88.29%)</b></td><td>0.01 <b>(-60.14%)</b></td><td>212.50 <b>(-46.90%)</b></td><td>177.22 <b>(-21.02%)</b></td><td>171.10 (-12.44%)</td><td>154.40 (+8.12%)</td><td>22.06 <b>(-78.31%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>400.20 (n/a)</td><td>224.40 (n/a)</td><td>195.40 (n/a)</td><td>142.80 (n/a)</td><td>101.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-11.36%)</td><td>0.04 <b>(-24.26%)</b></td><td>0.04 <b>(-21.82%)</b></td><td>0.02 <b>(-47.26%)</b></td><td>0.01 <b>(+67.37%)</b></td><td>384.30 <b>(+89.59%)</b></td><td>245.44 <b>(+43.06%)</b></td><td>211.00 <b>(+27.96%)</b></td><td>158.40 (+12.82%)</td><td>90.44 <b>(+260.37%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.70 (n/a)</td><td>171.56 (n/a)</td><td>164.90 (n/a)</td><td>140.40 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-11.23%)</td><td>0.05 (+1.59%)</td><td>0.04 (+1.81%)</td><td>0.04 (+16.29%)</td><td>0.01 <b>(-39.47%)</b></td><td>206.90 (-14.01%)</td><td>180.16 (-4.18%)</td><td>183.50 (-1.77%)</td><td>149.60 (+12.65%)</td><td>24.80 <b>(-41.00%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.60 (n/a)</td><td>188.02 (n/a)</td><td>186.80 (n/a)</td><td>132.80 (n/a)</td><td>42.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 <b>(-26.52%)</b></td><td>0.04 (-18.04%)</td><td>0.04 (-8.50%)</td><td>0.03 (-17.13%)</td><td>0.01 <b>(-36.16%)</b></td><td>241.80 <b>(+20.66%)</b></td><td>202.06 <b>(+20.15%)</b></td><td>205.90 (+9.29%)</td><td>161.90 <b>(+36.05%)</b></td><td>38.02 (+1.89%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>168.18 (n/a)</td><td>188.40 (n/a)</td><td>119.00 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (+8.08%)</td><td>0.05 (+6.60%)</td><td>0.05 (-1.34%)</td><td>0.04 (+19.91%)</td><td>0.01 <b>(-22.02%)</b></td><td>195.10 (-16.59%)</td><td>168.88 (-7.56%)</td><td>169.70 (+1.37%)</td><td>139.80 (-7.48%)</td><td>21.35 <b>(-39.72%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.90 (n/a)</td><td>182.70 (n/a)</td><td>167.40 (n/a)</td><td>151.10 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (-2.20%)</td><td>0.05 (-11.16%)</td><td>0.04 (-12.80%)</td><td>0.04 (-17.09%)</td><td>0.01 <b>(+35.09%)</b></td><td>212.60 <b>(+20.66%)</b></td><td>185.34 (+14.63%)</td><td>193.30 (+14.65%)</td><td>129.20 (+2.30%)</td><td>33.74 <b>(+67.18%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>161.68 (n/a)</td><td>168.60 (n/a)</td><td>126.30 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-8.44%)</td><td>0.04 (-11.53%)</td><td>0.04 (-6.99%)</td><td>0.04 (-13.71%)</td><td>0.00 (+2.19%)</td><td>225.50 (+15.88%)</td><td>197.64 (+13.34%)</td><td>190.70 (+7.50%)</td><td>171.10 (+9.26%)</td><td>22.62 <b>(+33.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.60 (n/a)</td><td>174.38 (n/a)</td><td>177.40 (n/a)</td><td>156.60 (n/a)</td><td>16.99 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 <b>(-37.41%)</b></td><td>0.04 (-19.18%)</td><td>0.05 (-8.21%)</td><td>0.03 (-12.32%)</td><td>0.01 <b>(-57.72%)</b></td><td>234.60 (+14.05%)</td><td>188.24 (+19.68%)</td><td>174.80 (+8.98%)</td><td>162.80 <b>(+59.76%)</b></td><td>29.82 (-19.22%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>205.70 (n/a)</td><td>157.28 (n/a)</td><td>160.40 (n/a)</td><td>101.90 (n/a)</td><td>36.91 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 <b>(-22.40%)</b></td><td>0.03 (-19.02%)</td><td>0.04 (-15.32%)</td><td>0.02 <b>(-29.59%)</b></td><td>0.00 <b>(+20.12%)</b></td><td>333.20 <b>(+42.03%)</b></td><td>254.02 <b>(+25.01%)</b></td><td>233.40 (+18.06%)</td><td>232.00 <b>(+28.82%)</b></td><td>44.36 <b>(+119.17%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.60 (n/a)</td><td>203.20 (n/a)</td><td>197.70 (n/a)</td><td>180.10 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 <b>(+25.91%)</b></td><td>0.06 <b>(+28.59%)</b></td><td>0.05 <b>(+34.59%)</b></td><td>0.04 <b>(+30.91%)</b></td><td>0.01 (+18.15%)</td><td>208.10 <b>(-23.63%)</b></td><td>155.50 <b>(-22.84%)</b></td><td>160.20 <b>(-25.70%)</b></td><td>115.50 <b>(-20.56%)</b></td><td>37.73 <b>(-27.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.50 (n/a)</td><td>201.52 (n/a)</td><td>215.60 (n/a)</td><td>145.40 (n/a)</td><td>52.20 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 <b>(+52.12%)</b></td><td>0.04 (+16.71%)</td><td>0.04 (+16.13%)</td><td>0.02 (-10.40%)</td><td>0.01 <b>(+252.32%)</b></td><td>353.30 (+11.59%)</td><td>240.58 (-5.69%)</td><td>206.90 (-13.90%)</td><td>153.20 <b>(-34.25%)</b></td><td>89.78 <b>(+158.89%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>316.60 (n/a)</td><td>255.10 (n/a)</td><td>240.30 (n/a)</td><td>233.00 (n/a)</td><td>34.68 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 <b>(-23.09%)</b></td><td>0.05 (-1.98%)</td><td>0.05 (+2.46%)</td><td>0.04 (+2.95%)</td><td>0.01 <b>(-58.58%)</b></td><td>212.40 (-2.88%)</td><td>178.08 (-1.95%)</td><td>175.10 (-2.40%)</td><td>151.50 <b>(+30.04%)</b></td><td>22.01 <b>(-46.42%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>181.62 (n/a)</td><td>179.40 (n/a)</td><td>116.50 (n/a)</td><td>41.08 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 <b>(-38.61%)</b></td><td>0.04 (-19.33%)</td><td>0.04 <b>(-21.41%)</b></td><td>0.04 (-5.44%)</td><td>0.00 <b>(-69.78%)</b></td><td>214.40 (+5.77%)</td><td>193.50 (+17.89%)</td><td>205.30 <b>(+27.20%)</b></td><td>167.30 <b>(+62.90%)</b></td><td>21.02 <b>(-48.21%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>202.70 (n/a)</td><td>164.14 (n/a)</td><td>161.40 (n/a)</td><td>102.70 (n/a)</td><td>40.58 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 <b>(+27.94%)</b></td><td>0.05 (+11.83%)</td><td>0.05 (+2.71%)</td><td>0.04 (+2.85%)</td><td>0.01 <b>(+252.60%)</b></td><td>194.00 (-2.76%)</td><td>171.10 (-9.43%)</td><td>179.30 (-2.61%)</td><td>142.20 <b>(-21.87%)</b></td><td>22.29 <b>(+168.22%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.50 (n/a)</td><td>188.92 (n/a)</td><td>184.10 (n/a)</td><td>182.00 (n/a)</td><td>8.31 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (-0.74%)</td><td>0.05 (+0.59%)</td><td>0.05 (+3.04%)</td><td>0.04 (-8.99%)</td><td>0.01 <b>(+24.74%)</b></td><td>209.40 (+9.86%)</td><td>170.76 (+1.22%)</td><td>169.20 (-2.98%)</td><td>126.00 (+0.72%)</td><td>37.86 <b>(+45.24%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.60 (n/a)</td><td>168.70 (n/a)</td><td>174.40 (n/a)</td><td>125.10 (n/a)</td><td>26.07 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 <b>(+28.30%)</b></td><td>0.05 (+15.13%)</td><td>0.05 (+9.91%)</td><td>0.04 (+7.78%)</td><td>0.01 <b>(+99.80%)</b></td><td>193.10 (-7.25%)</td><td>165.74 (-12.22%)</td><td>171.40 (-9.02%)</td><td>132.00 <b>(-22.03%)</b></td><td>22.81 <b>(+41.45%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.20 (n/a)</td><td>188.82 (n/a)</td><td>188.40 (n/a)</td><td>169.30 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (+13.57%)</td><td>0.05 <b>(+26.91%)</b></td><td>0.05 <b>(+28.92%)</b></td><td>0.04 <b>(+53.57%)</b></td><td>0.01 <b>(-25.30%)</b></td><td>199.90 <b>(-34.86%)</b></td><td>165.88 <b>(-23.59%)</b></td><td>162.50 <b>(-22.43%)</b></td><td>138.70 (-11.99%)</td><td>22.85 <b>(-58.20%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>306.90 (n/a)</td><td>217.10 (n/a)</td><td>209.50 (n/a)</td><td>157.60 (n/a)</td><td>54.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.18 (-0.07%)</td><td>0.18 (+0.08%)</td><td>0.18 (+0.22%)</td><td>0.18 (+0.01%)</td><td>0.00 (-6.86%)</td><td>47727.10 (-0.01%)</td><td>47575.24 (-0.08%)</td><td>47543.60 (-0.22%)</td><td>47469.90 (+0.07%)</td><td>108.65 (-6.79%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47731.80 (n/a)</td><td>47615.42 (n/a)</td><td>47646.20 (n/a)</td><td>47437.90 (n/a)</td><td>116.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.14 <b>(-35.26%)</b></td><td>0.13 <b>(-26.34%)</b></td><td>0.14 (-18.60%)</td><td>0.11 <b>(-23.82%)</b></td><td>0.02 <b>(-55.69%)</b></td><td>226.80 <b>(+31.25%)</b></td><td>194.62 <b>(+33.32%)</b></td><td>181.30 <b>(+22.83%)</b></td><td>171.20 <b>(+54.51%)</b></td><td>24.13 (-11.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.80 (n/a)</td><td>145.98 (n/a)</td><td>147.60 (n/a)</td><td>110.80 (n/a)</td><td>27.38 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.25 (-14.55%)</td><td>0.24 (-2.15%)</td><td>0.24 (+0.28%)</td><td>0.22 (+13.71%)</td><td>0.02 <b>(-61.58%)</b></td><td>190.50 (-12.05%)</td><td>174.60 (+0.37%)</td><td>173.60 (-0.29%)</td><td>162.30 (+17.10%)</td><td>11.32 <b>(-60.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>216.60 (n/a)</td><td>173.96 (n/a)</td><td>174.10 (n/a)</td><td>138.60 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.04 (-3.70%)</td><td>0.03 (-2.84%)</td><td>0.03 (-3.84%)</td><td>0.03 (+6.31%)</td><td>0.00 <b>(-25.68%)</b></td><td>197.90 (-5.90%)</td><td>176.56 (+1.45%)</td><td>175.00 (+3.98%)</td><td>139.00 (+3.89%)</td><td>23.74 <b>(-29.70%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>210.30 (n/a)</td><td>174.04 (n/a)</td><td>168.30 (n/a)</td><td>133.80 (n/a)</td><td>33.76 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (+17.58%)</td><td>0.06 <b>(+22.88%)</b></td><td>0.06 <b>(+26.99%)</b></td><td>0.04 (+9.92%)</td><td>0.01 <b>(+24.63%)</b></td><td>199.40 (-9.03%)</td><td>148.38 (-18.18%)</td><td>136.10 <b>(-21.28%)</b></td><td>116.10 (-14.95%)</td><td>33.26 (-5.41%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>181.36 (n/a)</td><td>172.90 (n/a)</td><td>136.50 (n/a)</td><td>35.17 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.10 (-5.11%)</td><td>0.09 <b>(+20.02%)</b></td><td>0.08 <b>(+26.96%)</b></td><td>0.07 <b>(+30.98%)</b></td><td>0.01 <b>(-43.02%)</b></td><td>168.90 <b>(-23.68%)</b></td><td>145.74 (-19.91%)</td><td>151.70 <b>(-21.24%)</b></td><td>120.20 (+5.35%)</td><td>19.63 <b>(-52.60%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>221.30 (n/a)</td><td>181.96 (n/a)</td><td>192.60 (n/a)</td><td>114.10 (n/a)</td><td>41.41 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (+11.29%)</td><td>0.05 (+6.57%)</td><td>0.05 (+10.76%)</td><td>0.04 (-5.93%)</td><td>0.01 <b>(+65.32%)</b></td><td>194.80 (+6.33%)</td><td>155.62 (-4.68%)</td><td>154.30 (-9.71%)</td><td>128.70 (-10.13%)</td><td>28.21 <b>(+56.38%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>163.26 (n/a)</td><td>170.90 (n/a)</td><td>143.20 (n/a)</td><td>18.04 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (+16.56%)</td><td>0.07 (+14.52%)</td><td>0.07 (+13.93%)</td><td>0.05 (-8.42%)</td><td>0.01 <b>(+90.60%)</b></td><td>221.40 (+9.17%)</td><td>159.32 (-10.36%)</td><td>155.20 (-12.22%)</td><td>127.90 (-14.22%)</td><td>37.15 <b>(+81.95%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>177.74 (n/a)</td><td>176.80 (n/a)</td><td>149.10 (n/a)</td><td>20.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (+17.58%)</td><td>0.05 (+1.09%)</td><td>0.05 (-8.75%)</td><td>0.04 (-10.66%)</td><td>0.01 <b>(+100.35%)</b></td><td>206.10 (+11.95%)</td><td>164.02 (+1.95%)</td><td>177.00 (+9.60%)</td><td>117.70 (-14.96%)</td><td>35.69 <b>(+88.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>160.88 (n/a)</td><td>161.50 (n/a)</td><td>138.40 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.09 <b>(+38.90%)</b></td><td>0.07 <b>(+22.58%)</b></td><td>0.06 <b>(+21.74%)</b></td><td>0.05 (-3.10%)</td><td>0.02 <b>(+186.56%)</b></td><td>221.10 (+3.22%)</td><td>162.40 (-14.75%)</td><td>158.50 (-17.83%)</td><td>115.50 <b>(-28.04%)</b></td><td>41.92 <b>(+116.44%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>190.50 (n/a)</td><td>192.90 (n/a)</td><td>160.50 (n/a)</td><td>19.37 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 <b>(+62.34%)</b></td><td>0.06 <b>(+62.86%)</b></td><td>0.07 <b>(+57.83%)</b></td><td>0.04 <b>(+83.30%)</b></td><td>0.01 <b>(+37.60%)</b></td><td>190.00 <b>(-45.43%)</b></td><td>139.20 <b>(-39.96%)</b></td><td>125.60 <b>(-36.63%)</b></td><td>108.70 <b>(-38.38%)</b></td><td>33.54 <b>(-53.36%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.20 (n/a)</td><td>231.84 (n/a)</td><td>198.20 (n/a)</td><td>176.40 (n/a)</td><td>71.90 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (+1.32%)</td><td>0.05 (+3.63%)</td><td>0.06 <b>(+20.25%)</b></td><td>0.04 (-9.55%)</td><td>0.01 <b>(+28.95%)</b></td><td>233.00 (+10.53%)</td><td>178.48 (-1.62%)</td><td>157.60 (-16.83%)</td><td>134.70 (-1.32%)</td><td>41.13 <b>(+48.69%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>181.42 (n/a)</td><td>189.50 (n/a)</td><td>136.50 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.07 (+13.25%)</td><td>0.05 (+12.51%)</td><td>0.05 (+11.44%)</td><td>0.04 (+10.74%)</td><td>0.01 <b>(+26.24%)</b></td><td>189.50 (-9.72%)</td><td>156.30 (-10.58%)</td><td>157.30 (-10.27%)</td><td>121.70 (-11.68%)</td><td>28.82 (+0.99%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>174.80 (n/a)</td><td>175.30 (n/a)</td><td>137.80 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.08 (-4.69%)</td><td>0.06 (+17.92%)</td><td>0.07 <b>(+53.30%)</b></td><td>0.04 (-0.51%)</td><td>0.02 (+18.05%)</td><td>256.90 (+0.51%)</td><td>170.90 (-11.84%)</td><td>127.10 <b>(-34.75%)</b></td><td>119.70 (+4.91%)</td><td>66.60 <b>(+29.30%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>255.60 (n/a)</td><td>193.86 (n/a)</td><td>194.80 (n/a)</td><td>114.10 (n/a)</td><td>51.51 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 <b>(+27.66%)</b></td><td>0.04 (+13.36%)</td><td>0.04 (+6.07%)</td><td>0.03 (-10.08%)</td><td>0.01 <b>(+87.07%)</b></td><td>299.60 (+11.21%)</td><td>195.12 (-7.94%)</td><td>185.50 (-5.74%)</td><td>144.70 <b>(-21.66%)</b></td><td>61.25 <b>(+70.71%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.40 (n/a)</td><td>211.96 (n/a)</td><td>196.80 (n/a)</td><td>184.70 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-5.89%)</td><td>0.05 (+11.54%)</td><td>0.05 (+8.75%)</td><td>0.04 <b>(+28.25%)</b></td><td>0.01 <b>(-34.28%)</b></td><td>229.20 <b>(-22.01%)</b></td><td>184.80 (-12.95%)</td><td>181.80 (-8.04%)</td><td>160.00 (+6.24%)</td><td>28.03 <b>(-46.51%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>293.90 (n/a)</td><td>212.30 (n/a)</td><td>197.70 (n/a)</td><td>150.60 (n/a)</td><td>52.40 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (-5.61%)</td><td>0.04 (+8.58%)</td><td>0.05 (+19.13%)</td><td>0.03 <b>(+20.93%)</b></td><td>0.01 <b>(-20.80%)</b></td><td>268.10 (-17.30%)</td><td>192.46 (-10.63%)</td><td>174.80 (-16.08%)</td><td>153.50 (+5.94%)</td><td>46.09 <b>(-31.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>324.20 (n/a)</td><td>215.34 (n/a)</td><td>208.30 (n/a)</td><td>144.90 (n/a)</td><td>67.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.06 (+15.06%)</td><td>0.05 (-2.31%)</td><td>0.04 (-8.36%)</td><td>0.03 <b>(-22.58%)</b></td><td>0.01 <b>(+71.49%)</b></td><td>297.50 <b>(+29.18%)</b></td><td>209.12 (+8.06%)</td><td>215.90 (+9.15%)</td><td>134.20 (-13.14%)</td><td>64.68 <b>(+89.73%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.30 (n/a)</td><td>193.52 (n/a)</td><td>197.80 (n/a)</td><td>154.50 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.05 (+9.83%)</td><td>0.03 (-0.28%)</td><td>0.04 (-9.47%)</td><td>0.03 (+2.74%)</td><td>0.01 (-1.10%)</td><td>321.90 (-2.66%)</td><td>246.92 (-0.61%)</td><td>229.70 (+10.43%)</td><td>170.00 (-8.94%)</td><td>62.58 (-12.37%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.70 (n/a)</td><td>248.44 (n/a)</td><td>208.00 (n/a)</td><td>186.70 (n/a)</td><td>71.42 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.74 (-12.78%)</td><td>0.65 (+1.79%)</td><td>0.65 (+9.83%)</td><td>0.54 (+4.41%)</td><td>0.07 <b>(-46.99%)</b></td><td>181.70 (-4.22%)</td><td>152.58 (-3.88%)</td><td>151.20 (-8.97%)</td><td>133.60 (+14.68%)</td><td>17.86 <b>(-40.77%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.84 (n/a)</td><td>0.64 (n/a)</td><td>0.59 (n/a)</td><td>0.52 (n/a)</td><td>0.13 (n/a)</td><td>189.70 (n/a)</td><td>158.74 (n/a)</td><td>166.10 (n/a)</td><td>116.50 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.69 (-14.16%)</td><td>0.63 (+3.73%)</td><td>0.67 (+12.83%)</td><td>0.46 (-2.57%)</td><td>0.10 <b>(-20.33%)</b></td><td>214.80 (+2.68%)</td><td>159.84 (-4.18%)</td><td>146.30 (-11.39%)</td><td>141.80 (+16.52%)</td><td>31.14 (-1.30%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.81 (n/a)</td><td>0.61 (n/a)</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.12 (n/a)</td><td>209.20 (n/a)</td><td>166.82 (n/a)</td><td>165.10 (n/a)</td><td>121.70 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.71 (-4.16%)</td><td>0.59 (-6.10%)</td><td>0.61 (-8.40%)</td><td>0.41 (-6.48%)</td><td>0.11 (-2.73%)</td><td>241.40 (+6.96%)</td><td>173.98 (+6.70%)</td><td>160.30 (+9.20%)</td><td>139.30 (+4.34%)</td><td>39.75 (+8.79%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.67 (n/a)</td><td>0.44 (n/a)</td><td>0.11 (n/a)</td><td>225.70 (n/a)</td><td>163.06 (n/a)</td><td>146.80 (n/a)</td><td>133.50 (n/a)</td><td>36.54 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.71 (-7.55%)</td><td>0.60 (+5.63%)</td><td>0.58 (+3.58%)</td><td>0.49 (+6.76%)</td><td>0.09 <b>(-26.70%)</b></td><td>201.20 (-6.33%)</td><td>167.18 (-6.82%)</td><td>169.90 (-3.41%)</td><td>137.80 (+8.16%)</td><td>25.79 <b>(-26.98%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.77 (n/a)</td><td>0.57 (n/a)</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.13 (n/a)</td><td>214.80 (n/a)</td><td>179.42 (n/a)</td><td>175.90 (n/a)</td><td>127.40 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.52 <b>(-27.27%)</b></td><td>0.46 (-14.16%)</td><td>0.47 (-7.54%)</td><td>0.32 (-2.18%)</td><td>0.08 <b>(-46.84%)</b></td><td>227.30 (+2.20%)</td><td>166.78 (+11.95%)</td><td>157.60 (+8.17%)</td><td>142.80 <b>(+37.57%)</b></td><td>34.88 <b>(-24.48%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.71 (n/a)</td><td>0.53 (n/a)</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.15 (n/a)</td><td>222.40 (n/a)</td><td>148.98 (n/a)</td><td>145.70 (n/a)</td><td>103.80 (n/a)</td><td>46.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.56 (-0.11%)</td><td>0.44 (-3.75%)</td><td>0.40 (-12.80%)</td><td>0.34 (-5.05%)</td><td>0.11 (+14.85%)</td><td>217.40 (+5.33%)</td><td>173.96 (+5.14%)</td><td>186.10 (+14.73%)</td><td>130.60 (+0.08%)</td><td>40.06 (+18.04%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>206.40 (n/a)</td><td>165.46 (n/a)</td><td>162.20 (n/a)</td><td>130.50 (n/a)</td><td>33.93 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.63 (+4.34%)</td><td>0.47 (-1.78%)</td><td>0.40 (-16.66%)</td><td>0.35 (+17.10%)</td><td>0.12 (-5.07%)</td><td>208.80 (-14.60%)</td><td>165.80 (+0.19%)</td><td>185.60 (+19.97%)</td><td>116.30 (-4.12%)</td><td>39.85 <b>(-21.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.61 (n/a)</td><td>0.48 (n/a)</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>244.50 (n/a)</td><td>165.48 (n/a)</td><td>154.70 (n/a)</td><td>121.30 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.50 (+10.24%)</td><td>0.39 (-0.65%)</td><td>0.38 (-9.04%)</td><td>0.32 (+0.20%)</td><td>0.07 <b>(+21.14%)</b></td><td>227.70 (-0.18%)</td><td>191.18 (+1.14%)</td><td>191.60 (+9.93%)</td><td>148.80 (-9.27%)</td><td>29.57 (+8.24%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.05 (n/a)</td><td>228.10 (n/a)</td><td>189.02 (n/a)</td><td>174.30 (n/a)</td><td>164.00 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.02 (-10.59%)</td><td>0.92 (+8.63%)</td><td>0.95 <b>(+27.77%)</b></td><td>0.70 (-1.03%)</td><td>0.13 <b>(-28.77%)</b></td><td>186.00 (+1.03%)</td><td>145.22 (-9.18%)</td><td>137.30 <b>(-21.77%)</b></td><td>128.20 (+11.87%)</td><td>23.87 (-19.29%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.14 (n/a)</td><td>0.85 (n/a)</td><td>0.75 (n/a)</td><td>0.71 (n/a)</td><td>0.18 (n/a)</td><td>184.10 (n/a)</td><td>159.90 (n/a)</td><td>175.50 (n/a)</td><td>114.60 (n/a)</td><td>29.57 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.04 (-9.83%)</td><td>0.87 (-6.03%)</td><td>0.90 (+5.96%)</td><td>0.70 (-3.18%)</td><td>0.14 <b>(-26.77%)</b></td><td>188.00 (+3.30%)</td><td>153.90 (+5.09%)</td><td>145.70 (-5.63%)</td><td>125.50 (+10.87%)</td><td>26.19 (-12.71%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.16 (n/a)</td><td>0.93 (n/a)</td><td>0.85 (n/a)</td><td>0.72 (n/a)</td><td>0.20 (n/a)</td><td>182.00 (n/a)</td><td>146.44 (n/a)</td><td>154.40 (n/a)</td><td>113.20 (n/a)</td><td>30.00 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.05 (+0.43%)</td><td>0.82 (-2.67%)</td><td>0.71 (-11.87%)</td><td>0.65 (+7.60%)</td><td>0.19 (+13.25%)</td><td>200.20 (-7.06%)</td><td>165.84 (+3.38%)</td><td>185.20 (+13.41%)</td><td>125.20 (-0.40%)</td><td>36.06 (+2.69%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.04 (n/a)</td><td>0.85 (n/a)</td><td>0.80 (n/a)</td><td>0.61 (n/a)</td><td>0.17 (n/a)</td><td>215.40 (n/a)</td><td>160.42 (n/a)</td><td>163.30 (n/a)</td><td>125.70 (n/a)</td><td>35.12 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (-14.40%)</td><td>0.02 <b>(-21.31%)</b></td><td>0.02 <b>(-32.02%)</b></td><td>0.02 (-17.97%)</td><td>0.00 (+0.74%)</td><td>221.80 <b>(+21.94%)</b></td><td>193.04 <b>(+28.21%)</b></td><td>209.20 <b>(+47.12%)</b></td><td>141.80 (+16.80%)</td><td>34.28 <b>(+43.33%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.90 (n/a)</td><td>150.56 (n/a)</td><td>142.20 (n/a)</td><td>121.40 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.02 (-1.44%)</td><td>0.02 (-3.16%)</td><td>0.02 (-6.05%)</td><td>0.02 (-6.36%)</td><td>0.00 <b>(+44.34%)</b></td><td>212.80 (+6.83%)</td><td>188.22 (+3.93%)</td><td>186.10 (+6.46%)</td><td>166.10 (+1.47%)</td><td>22.65 <b>(+54.62%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.20 (n/a)</td><td>181.10 (n/a)</td><td>174.80 (n/a)</td><td>163.70 (n/a)</td><td>14.65 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (+12.32%)</td><td>0.02 (+11.14%)</td><td>0.02 (+11.25%)</td><td>0.02 (+12.64%)</td><td>0.00 (+14.52%)</td><td>199.50 (-11.21%)</td><td>172.30 (-10.01%)</td><td>169.20 (-10.10%)</td><td>151.00 (-11.02%)</td><td>18.92 (-9.95%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>191.46 (n/a)</td><td>188.20 (n/a)</td><td>169.70 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.12 (+17.96%)</td><td>0.86 (+4.11%)</td><td>0.86 (+4.52%)</td><td>0.68 (-3.47%)</td><td>0.17 <b>(+87.17%)</b></td><td>193.10 (+3.59%)</td><td>158.30 (-2.02%)</td><td>154.30 (-4.28%)</td><td>118.40 (-15.25%)</td><td>29.57 <b>(+65.25%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.95 (n/a)</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.71 (n/a)</td><td>0.09 (n/a)</td><td>186.40 (n/a)</td><td>161.56 (n/a)</td><td>161.20 (n/a)</td><td>139.70 (n/a)</td><td>17.89 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.02 <b>(+28.91%)</b></td><td>0.84 <b>(+21.02%)</b></td><td>0.77 (+5.74%)</td><td>0.75 <b>(+50.75%)</b></td><td>0.11 (-2.03%)</td><td>175.70 <b>(-33.67%)</b></td><td>160.04 (-18.52%)</td><td>171.00 (-5.47%)</td><td>129.80 <b>(-22.41%)</b></td><td>19.62 <b>(-50.57%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.79 (n/a)</td><td>0.69 (n/a)</td><td>0.73 (n/a)</td><td>0.50 (n/a)</td><td>0.12 (n/a)</td><td>264.90 (n/a)</td><td>196.42 (n/a)</td><td>180.90 (n/a)</td><td>167.30 (n/a)</td><td>39.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.00 (+10.75%)</td><td>0.74 (-8.14%)</td><td>0.68 (-17.74%)</td><td>0.56 (-6.79%)</td><td>0.17 <b>(+36.70%)</b></td><td>236.20 (+7.31%)</td><td>186.08 (+10.59%)</td><td>195.10 <b>(+21.56%)</b></td><td>132.20 (-9.70%)</td><td>38.65 <b>(+28.06%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.90 (n/a)</td><td>0.80 (n/a)</td><td>0.82 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>220.10 (n/a)</td><td>168.26 (n/a)</td><td>160.50 (n/a)</td><td>146.40 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.88 (+16.53%)</td><td>0.77 (+14.56%)</td><td>0.77 (+18.09%)</td><td>0.70 (+14.36%)</td><td>0.07 (+11.67%)</td><td>188.50 (-12.57%)</td><td>172.46 (-12.75%)</td><td>172.50 (-15.32%)</td><td>150.80 (-14.17%)</td><td>14.08 (-16.87%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.65 (n/a)</td><td>0.61 (n/a)</td><td>0.06 (n/a)</td><td>215.60 (n/a)</td><td>197.66 (n/a)</td><td>203.70 (n/a)</td><td>175.70 (n/a)</td><td>16.94 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.11 (+13.41%)</td><td>0.89 (+9.87%)</td><td>0.87 (+10.64%)</td><td>0.70 (-3.02%)</td><td>0.16 <b>(+64.31%)</b></td><td>187.90 (+3.13%)</td><td>152.60 (-7.53%)</td><td>151.00 (-9.63%)</td><td>118.90 (-11.86%)</td><td>27.70 <b>(+53.12%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.98 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.72 (n/a)</td><td>0.10 (n/a)</td><td>182.20 (n/a)</td><td>165.02 (n/a)</td><td>167.10 (n/a)</td><td>134.90 (n/a)</td><td>18.09 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 <b>(+38.72%)</b></td><td>0.03 <b>(+47.72%)</b></td><td>0.03 <b>(+58.97%)</b></td><td>0.02 <b>(+40.48%)</b></td><td>0.00 <b>(+57.19%)</b></td><td>164.30 <b>(-28.84%)</b></td><td>142.22 <b>(-32.06%)</b></td><td>134.60 <b>(-37.10%)</b></td><td>122.40 <b>(-27.92%)</b></td><td>20.10 (-16.62%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>230.90 (n/a)</td><td>209.32 (n/a)</td><td>214.00 (n/a)</td><td>169.80 (n/a)</td><td>24.10 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.03 (-0.26%)</td><td>0.03 (+15.32%)</td><td>0.03 <b>(+20.00%)</b></td><td>0.02 <b>(+28.82%)</b></td><td>0.00 <b>(-30.87%)</b></td><td>184.30 <b>(-22.37%)</b></td><td>159.48 (-15.70%)</td><td>152.80 (-16.68%)</td><td>130.40 (+0.23%)</td><td>23.82 <b>(-45.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>237.40 (n/a)</td><td>189.18 (n/a)</td><td>183.40 (n/a)</td><td>130.10 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.56%)</td><td>0.00 <b>(-33.33%)</b></td><td>1036.62 (-1.73%)</td><td>977.71 (-0.24%)</td><td>967.06 (-0.15%)</td><td>949.52 (+0.60%)</td><td>33.93 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1054.89 (n/a)</td><td>980.07 (n/a)</td><td>968.55 (n/a)</td><td>943.90 (n/a)</td><td>44.92 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>0.01 (+0.00%)</td><td>0.01 (+0.50%)</td><td>0.01 (-1.23%)</td><td>0.01 (+9.59%)</td><td>0.00 <b>(-60.30%)</b></td><td>1026.15 (-8.71%)</td><td>1013.33 (-0.57%)</td><td>1021.13 (+1.47%)</td><td>978.24 (+0.48%)</td><td>19.77 <b>(-68.03%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1124.10 (n/a)</td><td>1019.17 (n/a)</td><td>1006.35 (n/a)</td><td>973.55 (n/a)</td><td>61.82 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>1.00 (-1.06%)</td><td>0.97 (-0.37%)</td><td>0.96 (-0.01%)</td><td>0.94 (-1.74%)</td><td>0.03 <b>(+23.57%)</b></td><td>2237.09 (+1.77%)</td><td>2173.28 (+0.39%)</td><td>2178.12 (+0.00%)</td><td>2104.50 (+1.07%)</td><td>60.82 <b>(+27.52%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>1.01 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2198.28 (n/a)</td><td>2164.87 (n/a)</td><td>2178.03 (n/a)</td><td>2082.22 (n/a)</td><td>47.69 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.27 (+4.45%)</td><td>2.79 (+7.57%)</td><td>2.63 (+11.01%)</td><td>2.48 (+6.32%)</td><td>0.35 (-0.19%)</td><td>211.80 (-5.95%)</td><td>189.96 (-7.16%)</td><td>199.50 (-9.89%)</td><td>160.60 (-4.23%)</td><td>22.90 (-11.19%)</td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.13 (n/a)</td><td>2.60 (n/a)</td><td>2.37 (n/a)</td><td>2.33 (n/a)</td><td>0.35 (n/a)</td><td>225.20 (n/a)</td><td>204.62 (n/a)</td><td>221.40 (n/a)</td><td>167.70 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>5.77 (-0.44%)</td><td>4.83 (-2.57%)</td><td>4.83 (+5.67%)</td><td>3.76 (-14.61%)</td><td>0.73 (+10.02%)</td><td>278.80 (+17.09%)</td><td>221.52 (+3.22%)</td><td>217.00 (-5.41%)</td><td>181.60 (+0.44%)</td><td>36.01 <b>(+30.96%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>5.80 (n/a)</td><td>4.95 (n/a)</td><td>4.57 (n/a)</td><td>4.40 (n/a)</td><td>0.67 (n/a)</td><td>238.10 (n/a)</td><td>214.60 (n/a)</td><td>229.40 (n/a)</td><td>180.80 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>7b55427</code> — 2026-09-11 19:32:23</td><td>3.45 (+1.31%)</td><td>3.14 (+17.06%)</td><td>3.28 <b>(+32.96%)</b></td><td>2.78 <b>(+36.32%)</b></td><td>0.30 <b>(-44.91%)</b></td><td>188.80 <b>(-26.62%)</b></td><td>168.46 (-16.74%)</td><td>159.70 <b>(-24.78%)</b></td><td>151.90 (-1.30%)</td><td>16.79 <b>(-59.04%)</b></td>
</tr>
<tr>
<td><code>72002fb</code> — 2026-09-09 02:10:33</td><td>3.41 (n/a)</td><td>2.68 (n/a)</td><td>2.47 (n/a)</td><td>2.04 (n/a)</td><td>0.55 (n/a)</td><td>257.30 (n/a)</td><td>202.34 (n/a)</td><td>212.30 (n/a)</td><td>153.90 (n/a)</td><td>41.00 (n/a)</td>
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
